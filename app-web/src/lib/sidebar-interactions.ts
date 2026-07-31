/**
 * 侧边栏交互脚本（web 端）
 * -----------------------------------------------------------------------------
 * 负责：
 * 1. 滚动位置记忆：点击文档链接前保存到 sessionStorage，页面加载后恢复
 * 2. 模块折叠：点击展开按钮切换子文档列表显隐，状态持久化到 localStorage
 * 3. 全部模块视图切换：响应 Layout 的事件，切换章节/全部模块面板
 * 4. 侧边栏整体折叠/展开收纳
 *
 * 状态类约定（配合 @fandex/styles 的 .fndx-sidebar 样式）：
 * - .is-active   激活态（当前文档链接）
 * - .is-hidden   隐藏态（互斥面板切换）
 * - .is-collapsed 折叠态（模块子文档列表 / 侧边栏整体折叠）
 *
 * 与 Layout 集成：
 * - body.sidebar-open 由 Layout 控制抽屉显隐
 * - fandex-switch-chapters / fandex-switch-modules 事件由 Layout 派发
 */

/** sessionStorage 键名：侧边栏滚动位置 */
const SIDEBAR_SCROLL_KEY = 'fandex-sidebar-scroll';

/** localStorage 键名：模块折叠状态（记录已展开的 moduleId 集合） */
const MODULE_EXPANDED_KEY = 'fandex-sidebar-expanded';

/** localStorage 键名：侧边栏整体折叠状态（'1' = 折叠，无值 = 展开） */
const SIDEBAR_COLLAPSED_KEY = 'fandex-sidebar-collapsed';

/** localStorage 键名：侧边栏视图状态（'chapters' | 'modules'）
 *  记录用户上次选择的视图，页面切换后恢复 */
const SIDEBAR_VIEW_KEY = 'fandex-sidebar-view';

/**
 * 读取已展开模块集合
 * @returns 已展开的 moduleId 集合
 */
function readExpandedSet(): Set<string> {
  try {
    const raw = localStorage.getItem(MODULE_EXPANDED_KEY);
    if (!raw) return new Set();
    const arr = JSON.parse(raw) as string[];
    return new Set(Array.isArray(arr) ? arr : []);
  } catch {
    return new Set();
  }
}

/**
 * 写入已展开模块集合
 * @param set - 已展开的 moduleId 集合
 */
function writeExpandedSet(set: Set<string>): void {
  try {
    localStorage.setItem(MODULE_EXPANDED_KEY, JSON.stringify(Array.from(set)));
  } catch {
    /* localStorage 不可用时静默降级 */
  }
}

/**
 * 初始化侧边栏整体折叠/展开收纳
 *
 * 实现说明：
 * - 折叠按钮 (#sidebar-collapse-btn) 点击后为侧边栏添加 .is-collapsed 类
 * - 浮动展开按钮 (#sidebar-expand-fab) 点击后移除 .is-collapsed 类
 * - 折叠状态持久化到 localStorage，页面切换后恢复
 * - 折叠时主内容区自动扩展填满释放的空间（由 CSS grid 自动处理）
 */
function initSidebarCollapse(): void {
  const sidebar = document.getElementById('app-sidebar');
  const collapseBtn = document.getElementById('sidebar-collapse-btn');
  const expandFab = document.getElementById('sidebar-expand-fab');
  if (!sidebar || !collapseBtn || !expandFab) return;

  // 避免重复绑定
  if (collapseBtn.dataset.bound === '1') return;
  collapseBtn.dataset.bound = '1';

  /** 应用折叠状态到 DOM */
  const applyCollapsedState = (collapsed: boolean): void => {
    // 同步管理 <html> 上的 sidebar-collapsed 标记类（FOUC 防护，与 BaseLayout 内联脚本协同）
    document.documentElement.classList.toggle('sidebar-collapsed', collapsed);
    if (collapsed) {
      sidebar.classList.add('is-collapsed');
      expandFab.classList.add('is-visible');
    } else {
      sidebar.classList.remove('is-collapsed');
      expandFab.classList.remove('is-visible');
    }
  };

  // 恢复持久化状态
  const savedCollapsed = localStorage.getItem(SIDEBAR_COLLAPSED_KEY) === '1';
  applyCollapsedState(savedCollapsed);

  // 折叠按钮：点击折叠
  collapseBtn.addEventListener('click', () => {
    const willCollapse = !sidebar.classList.contains('is-collapsed');
    applyCollapsedState(willCollapse);
    try {
      if (willCollapse) {
        localStorage.setItem(SIDEBAR_COLLAPSED_KEY, '1');
      } else {
        localStorage.removeItem(SIDEBAR_COLLAPSED_KEY);
      }
    } catch {
      /* localStorage 不可用时静默降级 */
    }
  });

  // 展开按钮：点击展开
  if (expandFab.dataset.bound !== '1') {
    expandFab.dataset.bound = '1';
    expandFab.addEventListener('click', () => {
      applyCollapsedState(false);
      try {
        localStorage.removeItem(SIDEBAR_COLLAPSED_KEY);
      } catch {
        /* localStorage 不可用时静默降级 */
      }
    });
  }
}

/**
 * 初始化侧边栏交互（首屏 + ClientRouter 跳转后）
 *
 * 调用顺序说明（重要）：
 * 1. initCloseButton / initModuleToggle — 绑定事件，不操作 DOM 显隐
 * 2. restoreModuleExpandState — 恢复模块展开，改变 sidebar-scroll 内容高度
 * 3. initSidebarCollapse — 应用整体折叠态，改变 sidebar 容器可见性
 * 4. initScrollMemory — 最后恢复滚动位置，此时内容高度与容器可见性均已稳定
 *
 * 时序修复：原实现将 initScrollMemory 置于首位，导致 restoreModuleExpandState
 * 改变容器高度后、requestAnimationFrame 恢复时可能因折叠态导致 scrollTop 失效。
 * 调整到最后确保恢复时 DOM 状态已确定。
 */
function initSidebar(): void {
  initCloseButton();
  initModuleToggle();
  restoreModuleExpandState();
  initSidebarCollapse();
  initViewTabs();
  restoreView();
  initScrollMemory();
}

/**
 * 滚动位置记忆：导航前保存，加载后恢复
 *
 * 恢复策略：
 * - 若侧边栏处于整体折叠态（is-collapsed），sidebar-scroll 不可见，
 *   此时设置 scrollTop 无效（浏览器可能重置为 0）。
 *   保留 sessionStorage 供用户展开侧边栏后下次 page-load 恢复。
 * - 仅在可见态下恢复并清除 sessionStorage，避免陈旧数据干扰。
 *
 * 绑定守卫说明：
 * - ClientRouter 跳转后 DOM 被替换，旧监听随节点销毁（经核查 Layout 未对 sidebar
 *   使用 transition:persist），理论上不会累积。
 * - 但为与 initModuleToggle/initSidebarCollapse 保持一致的防御性风格，
 *   统一补充 data-bound 守卫，防止节点复用场景下的重复绑定。
 */
function initScrollMemory(): void {
  const sidebarScroll = document.getElementById('sidebar-scroll');
  if (!sidebarScroll) return;

  // 检测整体折叠态：折叠时 sidebar-scroll 不可见，跳过恢复并保留 sessionStorage
  const sidebar = document.getElementById('app-sidebar');
  const isCollapsed = sidebar?.classList.contains('is-collapsed') ?? false;

  const saved = sessionStorage.getItem(SIDEBAR_SCROLL_KEY);
  if (saved && !isCollapsed) {
    // requestAnimationFrame 延迟到下一帧渲染前恢复，此时同步 DOM 修改已应用、布局稳定
    requestAnimationFrame(() => {
      sidebarScroll.scrollTop = Number(saved);
      sessionStorage.removeItem(SIDEBAR_SCROLL_KEY);
    });
  }

  // 点击文档链接前保存滚动位置（补充绑定守卫，避免重复绑定多次写入 sessionStorage）
  sidebarScroll.querySelectorAll<HTMLAnchorElement>('a[href]').forEach((link) => {
    if (link.dataset.scrollBound === '1') return;
    link.dataset.scrollBound = '1';
    link.addEventListener('click', () => {
      sessionStorage.setItem(SIDEBAR_SCROLL_KEY, String(sidebarScroll.scrollTop));
    });
  });
}

/**
 * 移动端关闭按钮（与 Layout 的 body.sidebar-open 集成）
 * 补充绑定守卫，与 initModuleToggle/initSidebarCollapse 风格统一
 */
function initCloseButton(): void {
  const closeBtn = document.getElementById('sidebar-close-btn');
  if (!closeBtn) return;
  if (closeBtn.dataset.bound === '1') return;
  closeBtn.dataset.bound = '1';
  closeBtn.addEventListener('click', () => {
    document.body.classList.remove('sidebar-open');
    const sidebar = document.getElementById('app-sidebar');
    sidebar?.classList.remove('is-open');
  });
}

/**
 * 初始化模块折叠/展开交互
 *
 * 实现说明：
 * - 委托方式监听 .fndx-sidebar__module-arrow 点击事件
 * - 点击切换同级的 .fndx-sidebar__module-docs 的 is-collapsed 类
 * - 通过 aria-expanded 属性驱动 CSS 旋转箭头
 * - 持久化展开状态到 localStorage
 */
function initModuleToggle(): void {
  const buttons = document.querySelectorAll<HTMLButtonElement>(
    '.fndx-sidebar__module-arrow[data-module-toggle]',
  );
  if (buttons.length === 0) return;

  buttons.forEach((btn) => {
    // 避免重复绑定
    if (btn.dataset.bound === '1') return;
    btn.dataset.bound = '1';

    btn.addEventListener('click', (event) => {
      event.preventDefault();
      event.stopPropagation();

      const moduleId = btn.getAttribute('data-module-toggle');
      if (!moduleId) return;

      const li = btn.closest('.fndx-sidebar__module') as HTMLElement | null;
      if (!li) return;

      const docsList = li.querySelector<HTMLUListElement>('.fndx-sidebar__module-docs');
      if (!docsList) return;

      const willExpand = docsList.classList.contains('is-collapsed');
      if (willExpand) {
        docsList.classList.remove('is-collapsed');
        btn.setAttribute('aria-expanded', 'true');
      } else {
        docsList.classList.add('is-collapsed');
        btn.setAttribute('aria-expanded', 'false');
      }

      // 持久化
      const expandedSet = readExpandedSet();
      if (willExpand) {
        expandedSet.add(moduleId);
      } else {
        expandedSet.delete(moduleId);
      }
      writeExpandedSet(expandedSet);
    });
  });
}

/**
 * 恢复模块展开状态
 * 页面加载时根据 localStorage 中记录的展开集合，恢复对应模块的展开状态
 *
 * 设计说明（为何使用全局集合而非按页面隔离）：
 * - 模块 ID 全局唯一（如 frontend/javascript），"全部模块"面板在所有文档页渲染相同的模块列表
 * - 全局集合是预期行为：用户在任意页面展开某模块后，导航到其他页面时该模块保持展开
 * - 若按页面 key 隔离会导致导航后模块折叠回默认态，破坏用户预期
 * - querySelectorAll('.fndx-sidebar__module') 仅匹配当前 DOM 存在的模块项，
 *   已删除的模块即使残留于集合也不会被恢复（无匹配 DOM 节点），无幽灵展开风险
 * - 集合体积上限为模块总数（约 50+ 个 ID，~1KB），不存在无限增长问题
 */
function restoreModuleExpandState(): void {
  const expandedSet = readExpandedSet();
  if (expandedSet.size === 0) return;

  const groups = document.querySelectorAll<HTMLElement>('.fndx-sidebar__module');
  groups.forEach((li) => {
    const moduleId = li.getAttribute('data-module');
    if (!moduleId || !expandedSet.has(moduleId)) return;

    const docsList = li.querySelector<HTMLUListElement>('.fndx-sidebar__module-docs');
    const btn = li.querySelector<HTMLButtonElement>('.fndx-sidebar__module-arrow');
    if (!docsList || !btn) return;

    docsList.classList.remove('is-collapsed');
    btn.setAttribute('aria-expanded', 'true');
  });
}

/** 更新视图切换 tabs 的 active 状态与 aria-selected
 *  @param view - 目标视图标识 */
function updateTabsActive(view: 'chapters' | 'modules'): void {
  document.querySelectorAll<HTMLButtonElement>('.fndx-sidebar__view-tab').forEach((tab) => {
    const isActive = tab.dataset.view === view;
    tab.classList.toggle('is-active', isActive);
    tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
  });
}

/** 持久化视图状态到 localStorage */
function persistView(view: 'chapters' | 'modules'): void {
  try {
    localStorage.setItem(SIDEBAR_VIEW_KEY, view);
  } catch {
    /* localStorage 不可用时静默降级 */
  }
}

/**
 * 初始化视图切换 tabs 点击交互
 *
 * 实现说明：
 * - 查询 .fndx-sidebar__view-tab 按钮元素，绑定 click 事件
 * - 点击后调用 showChapterView / showModulesView 切换面板
 * - 绑定守卫 data-bound 防止 ClientRouter 跳转后重复绑定
 */
function initViewTabs(): void {
  const tabs = document.querySelectorAll<HTMLButtonElement>('.fndx-sidebar__view-tab');
  if (tabs.length === 0) return;

  tabs.forEach((tab) => {
    if (tab.dataset.bound === '1') return;
    tab.dataset.bound = '1';

    tab.addEventListener('click', () => {
      const view = tab.dataset.view;
      if (view === 'chapters') {
        showChapterView();
      } else if (view === 'modules') {
        showModulesView();
      }
    });
  });
}

/**
 * 恢复视图状态（页面加载时从 localStorage 读取）
 *
 * 行为：
 * - 默认章节视图（与 SSR 渲染的默认状态一致，无 FOUC）
 * - 若上次停留在全部模块视图，则切换到全部模块面板
 * - 读取失败时默认章节视图
 */
function restoreView(): void {
  let view: 'chapters' | 'modules' = 'chapters';
  try {
    const saved = localStorage.getItem(SIDEBAR_VIEW_KEY);
    if (saved === 'modules') view = 'modules';
  } catch {
    /* localStorage 不可用时默认章节视图 */
  }
  if (view === 'modules') {
    showModulesView();
  } else {
    showChapterView();
  }
}

/** 切换到章节视图（响应 tabs 点击或 Layout 的 fandex-switch-chapters 事件）
 *  仅操作两个 nav 面板的 is-hidden 类，#sidebar-panel-chapters（ul）在面板内部，
 *  面板隐藏时自然不可见，无需单独操作 */
function showChapterView(): void {
  const chaptersNav = document.getElementById('sidebar-chapters-panel');
  const allModulesPanel = document.getElementById('sidebar-all-modules-panel');

  chaptersNav?.classList.remove('is-hidden');
  allModulesPanel?.classList.add('is-hidden');
  updateTabsActive('chapters');
  persistView('chapters');
}

/** 切换到全部模块视图（响应 tabs 点击或 Layout 的 fandex-switch-modules 事件） */
function showModulesView(): void {
  const chaptersNav = document.getElementById('sidebar-chapters-panel');
  const allModulesPanel = document.getElementById('sidebar-all-modules-panel');

  chaptersNav?.classList.add('is-hidden');
  allModulesPanel?.classList.remove('is-hidden');
  updateTabsActive('modules');
  persistView('modules');
}

// 初始化（首屏 + ClientRouter 跳转后）
initSidebar();
document.addEventListener('astro:page-load', initSidebar);

// 监听来自 Layout 的视图切换事件
document.addEventListener('fandex-switch-chapters', showChapterView);
document.addEventListener('fandex-switch-modules', showModulesView);
