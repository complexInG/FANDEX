/**
 * 侧边栏交互脚本（web 端）
 * -----------------------------------------------------------------------------
 * 从 Sidebar.astro 提取的客户端交互逻辑，负责：
 * 1. 滚动位置记忆：点击文档链接前保存到 sessionStorage，页面加载后恢复
 * 2. 进度标记：从 localStorage 读取进度数据，更新文档链接的圆点颜色
 * 3. 模块折叠：点击展开按钮切换子文档列表显隐，状态持久化到 localStorage
 * 4. 全部模块视图切换：响应 Layout 的事件，切换章节/全部模块面板
 *
 * 状态类约定（配合 @fandex/styles 的 .fndx-sidebar 样式）：
 * - .is-active   激活态（当前文档链接）
 * - .is-hidden   隐藏态（互斥面板切换）
 * - .is-collapsed 折叠态（模块子文档列表）
 * - .is-completed / .is-reading 进度指示器状态
 *
 * 与 Layout 集成：
 * - body.sidebar-open 由 Layout 控制抽屉显隐
 * - fandex-switch-chapters / fandex-switch-modules 事件由 Layout 派发
 */

/** sessionStorage 键名：侧边栏滚动位置 */
const SIDEBAR_SCROLL_KEY = 'fandex-sidebar-scroll';

/** localStorage 键名：阅读进度 */
const PROGRESS_KEY = 'fandex-progress';

/** localStorage 键名：模块折叠状态（记录已展开的 moduleId 集合） */
const MODULE_EXPANDED_KEY = 'fandex-sidebar-expanded';

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

/** 初始化侧边栏交互（首屏 + ClientRouter 跳转后） */
function initSidebar(): void {
  initScrollMemory();
  initProgressIndicators();
  initCloseButton();
  initModuleToggle();
  restoreModuleExpandState();
}

/** 滚动位置记忆：导航前保存，加载后恢复 */
function initScrollMemory(): void {
  const sidebarScroll = document.getElementById('sidebar-scroll');
  if (!sidebarScroll) return;

  /** 恢复滚动位置 */
  const saved = sessionStorage.getItem(SIDEBAR_SCROLL_KEY);
  if (saved) {
    requestAnimationFrame(() => {
      sidebarScroll.scrollTop = Number(saved);
      sessionStorage.removeItem(SIDEBAR_SCROLL_KEY);
    });
  }

  /** 点击文档链接前保存滚动位置 */
  sidebarScroll.querySelectorAll<HTMLAnchorElement>('a[href]').forEach((link) => {
    link.addEventListener('click', () => {
      sessionStorage.setItem(SIDEBAR_SCROLL_KEY, String(sidebarScroll.scrollTop));
    });
  });
}

/**
 * 进度指示器更新
 * 从 localStorage 读取进度数据，更新文档链接前的圆点颜色
 * - read：is-completed（success 绿色实心）
 * - reading：is-reading（warning 琥珀色实心）
 * - unread：默认边框色
 */
function initProgressIndicators(): void {
  const progressLinks = document.querySelectorAll<HTMLElement>(
    '.fndx-sidebar__link[data-progress-slug]',
  );
  if (progressLinks.length === 0) return;

  /** 从 localStorage 解析进度数据（兼容多种存储结构） */
  let progressMap: Record<string, { status?: string }> = {};
  try {
    const raw = localStorage.getItem(PROGRESS_KEY);
    if (raw) {
      const parsed = JSON.parse(raw) as {
        state?: { progress?: Record<string, { status?: string }> };
        progress?: Record<string, { status?: string }> };
      progressMap = parsed.state?.progress ?? parsed.progress ?? {};
    }
  } catch {
    /* localStorage 数据损坏时静默降级 */
  }

  progressLinks.forEach((link) => {
    const slug = link.getAttribute('data-progress-slug');
    if (!slug) return;
    const indicator = link.querySelector<HTMLElement>('.fndx-sidebar__progress');
    if (!indicator) return;

    // 重置状态类
    indicator.classList.remove('is-completed', 'is-reading');

    const entry = progressMap[slug];
    if (!entry?.status) return;

    if (entry.status === 'read' || entry.status === 'done') {
      indicator.classList.add('is-completed');
    } else if (entry.status === 'reading') {
      indicator.classList.add('is-reading');
    }
  });
}

/** 移动端关闭按钮（与 Layout 的 body.sidebar-open 集成） */
function initCloseButton(): void {
  const closeBtn = document.getElementById('sidebar-close-btn');
  closeBtn?.addEventListener('click', () => {
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

/** 切换到章节视图（响应 Layout 的 fandex-switch-chapters 事件） */
function showChapterView(): void {
  const chaptersPanel = document.getElementById('sidebar-panel-chapters');
  const allModulesPanel = document.getElementById('sidebar-all-modules-panel');
  const chaptersNav = document.getElementById('sidebar-chapters-panel');

  chaptersPanel?.classList.remove('is-hidden');
  allModulesPanel?.classList.add('is-hidden');
  chaptersNav?.classList.remove('is-hidden');
}

/** 切换到全部模块视图（响应 Layout 的 fandex-switch-modules 事件） */
function showModulesView(): void {
  const chaptersPanel = document.getElementById('sidebar-panel-chapters');
  const allModulesPanel = document.getElementById('sidebar-all-modules-panel');
  const chaptersNav = document.getElementById('sidebar-chapters-panel');

  chaptersPanel?.classList.add('is-hidden');
  allModulesPanel?.classList.remove('is-hidden');
  chaptersNav?.classList.add('is-hidden');
}

// 初始化（首屏 + ClientRouter 跳转后）
initSidebar();
document.addEventListener('astro:page-load', initSidebar);

// 监听全局进度变化事件
document.addEventListener('fandex-progress-change', initProgressIndicators);

// 监听来自 Layout 的视图切换事件
document.addEventListener('fandex-switch-chapters', showChapterView);
document.addEventListener('fandex-switch-modules', showModulesView);
