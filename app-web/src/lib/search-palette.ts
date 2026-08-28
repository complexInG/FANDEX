/**
 * 全站搜索命令面板（pagefind 驱动）
 * =============================================================================
 * 功能概述：
 * - Ctrl/Cmd + K 或点击导航搜索按钮打开命令面板，全文检索全站文档
 * - 索引由 pagefind 在构建后生成（dist/pagefind/，见 package.json build 脚本），
 *   首次打开面板时惰性加载 pagefind 运行时，未加载成功（如 dev 环境）时给出提示
 * - 输入防抖 200ms，展示标题/面包屑/摘要片段，支持上下键选择、Enter 跳转
 * - 与 View Transitions 兼容：面板 DOM 按需创建，keydown 绑定在 window 上
 *   （ClientRouter 导航不重执行模块脚本，监听器天然持久）
 *
 * 设计原则：
 * - 零框架依赖的纯 DOM 实现，不增加任何岛屿水合成本
 * - 索引与运行时全部同源静态文件，无外部服务
 * =============================================================================
 */

/** 站点基础路径（与 import.meta.env.BASE_URL 一致，构建期内联） */
const BASE = import.meta.env.BASE_URL;
/** 每次展示的最大结果数 */
const MAX_RESULTS = 10;
/** 输入防抖时长（毫秒） */
const DEBOUNCE_MS = 200;

/** pagefind 结果条目的最小结构声明 */
interface PagefindData {
  /** 页面地址（相对 dist 根目录） */
  url: string;
  /** 页面元信息 */
  meta: { title?: string };
  /** 高亮摘要 HTML */
  excerpt: string;
  /** 面包屑（pagefind 内置层级） */
  breadcrumbs?: Array<{ title?: string }>;
}

/** pagefind 模块的最小接口声明 */
interface PagefindAPI {
  search: (query: string) => Promise<{ results: Array<{ data: () => Promise<PagefindData> }> }>;
}

/** 已加载的 pagefind 实例缓存 */
let pagefindInstance: PagefindAPI | null = null;
/** 面板 DOM 引用（按需创建） */
let panel: HTMLDialogElement | null = null;
/** 输入框引用 */
let inputEl: HTMLInputElement | null = null;
/** 结果容器引用 */
let listEl: HTMLElement | null = null;
/** 状态提示引用 */
let statusEl: HTMLElement | null = null;
/** 防抖计时器 */
let debounceTimer: number | undefined;
/** 当前键盘焦点在结果列表中的下标 */
let activeIndex = -1;

/**
 * 惰性加载 pagefind 运行时
 * @returns pagefind API；索引不存在（dev 环境）时返回 null
 */
async function loadPagefind(): Promise<PagefindAPI | null> {
  if (pagefindInstance) return pagefindInstance;
  try {
    const mod = await import(/* @vite-ignore */ `${BASE}pagefind/pagefind.js`);
    const pagefind = (mod.default ?? mod) as PagefindAPI;
    pagefindInstance = pagefind;
    return pagefind;
  } catch {
    return null;
  }
}

/**
 * 创建面板 DOM 结构（仅首次调用时执行）
 */
function ensurePanel(): HTMLDialogElement {
  if (panel) return panel;

  panel = document.createElement('dialog');
  panel.className = 'search-palette';
  panel.setAttribute('aria-label', '全站搜索');
  panel.innerHTML = `
    <div class="search-palette__head">
      <span class="search-palette__mark" aria-hidden="true"></span>
      <input
        class="search-palette__input"
        type="search"
        placeholder="搜索文档、语法与知识点"
        aria-label="搜索关键词"
        autocomplete="off"
        spellcheck="false"
      />
      <kbd class="search-palette__kbd">Esc</kbd>
    </div>
    <div class="search-palette__status" role="status"></div>
    <ul class="search-palette__list" role="listbox" aria-label="搜索结果"></ul>
    <div class="search-palette__foot">上下键选择 · Enter 打开 · Esc 关闭</div>
  `;
  document.body.appendChild(panel);

  inputEl = panel.querySelector('.search-palette__input');
  listEl = panel.querySelector('.search-palette__list');
  statusEl = panel.querySelector('.search-palette__status');

  // 关闭行为：点击遮罩或 Esc（dialog 原生支持 Esc 关闭）
  panel.addEventListener('click', (e) => {
    const target = e.target as HTMLElement;
    if (target === panel) closePalette();
  });
  panel.addEventListener('close', () => {
    activeIndex = -1;
  });

  // 输入防抖搜索
  inputEl?.addEventListener('input', () => {
    window.clearTimeout(debounceTimer);
    debounceTimer = window.setTimeout(() => {
      void runSearch(inputEl?.value.trim() ?? '');
    }, DEBOUNCE_MS);
  });

  // 键盘导航：上下选择，Enter 打开
  panel.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      const items = listEl?.querySelectorAll<HTMLAnchorElement>('.search-palette__item');
      if (!items || items.length === 0) return;
      const delta = e.key === 'ArrowDown' ? 1 : -1;
      activeIndex = (activeIndex + delta + items.length) % items.length;
      items.forEach((item, index) => item.setAttribute('aria-selected', String(index === activeIndex)));
      items[activeIndex]?.scrollIntoView({ block: 'nearest' });
    } else if (e.key === 'Enter') {
      const items = listEl?.querySelectorAll<HTMLAnchorElement>('.search-palette__item');
      const target = items?.[Math.max(0, activeIndex)];
      if (target) {
        e.preventDefault();
        target.click();
      }
    }
  });

  return panel;
}

/**
 * 执行搜索并渲染结果
 * @param query - 搜索关键词；空串时清空结果区
 */
async function runSearch(query: string): Promise<void> {
  if (!listEl || !statusEl) return;
  if (!query) {
    listEl.innerHTML = '';
    statusEl.textContent = '输入关键词开始检索';
    return;
  }

  const pagefind = await loadPagefind();
  if (!pagefind) {
    statusEl.textContent = '搜索索引不可用（本地开发环境请先执行完整构建）';
    return;
  }

  statusEl.textContent = '检索中';
  try {
    const { results } = await pagefind.search(query);
    const datas = await Promise.all(results.slice(0, MAX_RESULTS).map((r) => r.data()));
    listEl.innerHTML = '';
    activeIndex = datas.length > 0 ? 0 : -1;

    if (datas.length === 0) {
      statusEl.textContent = `未找到与「${query}」相关的内容`;
      return;
    }
    statusEl.textContent = `共 ${results.length} 条结果`;

    datas.forEach((data, index) => {
      const li = document.createElement('li');
      li.className = 'search-palette__entry';
      const a = document.createElement('a');
      a.className = 'search-palette__item';
      a.setAttribute('role', 'option');
      a.setAttribute('aria-selected', String(index === 0));
      // pagefind 地址相对 dist 根目录，补齐站点 base 前缀
      const href = data.url.startsWith(BASE) ? data.url : `${BASE}${data.url.replace(/^\//, '')}`;
      a.href = href;
      const crumb = data.breadcrumbs?.map((b) => b.title).filter(Boolean).join(' / ');
      a.innerHTML = `
        <span class="search-palette__title">${data.meta?.title ?? '未命名文档'}</span>
        ${crumb ? `<span class="search-palette__crumb">${crumb}</span>` : ''}
        <span class="search-palette__excerpt">${data.excerpt}</span>
      `;
      // 点击后关闭面板，交给 ClientRouter 完成跳转
      a.addEventListener('click', () => closePalette());
      li.appendChild(a);
      listEl?.appendChild(li);
    });
  } catch {
    statusEl.textContent = '检索失败，请稍后重试';
  }
}

/** 打开面板并聚焦输入框 */
function openPalette(): void {
  const dialog = ensurePanel();
  if (dialog.open) return;
  dialog.showModal();
  if (inputEl) {
    inputEl.value = '';
    inputEl.focus();
  }
  if (statusEl) statusEl.textContent = '输入关键词开始检索';
  if (listEl) listEl.innerHTML = '';
}

/** 关闭面板 */
function closePalette(): void {
  panel?.close();
}

// SSR/预渲染环境不执行任何 DOM 逻辑（Astro 构建期会求值页面脚本模块）
if (!import.meta.env.SSR && typeof window !== 'undefined') {
  // 全局快捷键：Ctrl/Cmd + K 打开（window 级绑定，ClientRouter 导航后依然有效）
  window.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
    e.preventDefault();
    if (panel?.open) {
      closePalette();
    } else {
      openPalette();
    }
  }
});

// 导航栏搜索按钮（存在时）触发打开；View Transitions 切页后重新绑定
function bindTrigger(): void {
  document.querySelectorAll<HTMLElement>('[data-search-trigger]').forEach((btn) => {
    btn.addEventListener('click', openPalette);
  });
}
bindTrigger();
document.addEventListener('astro:page-load', bindTrigger);
}
