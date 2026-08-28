/**
 * 学习进度追踪模块（本地持久化）
 * =============================================================================
 * 功能概述：
 * - 文档页访问时自动记录「已读」（localStorage，键名 fandex-progress）
 * - 侧边栏章节导航为已读文档追加对勾标记（is-visited）
 * - 模块首页展示「已读 x / 共 N 篇」进度条（[data-progress-module] 容器）
 *
 * 设计原则：
 * - 纯本地记录，不上传不同步；清空浏览器数据即重置
 * - 全部为 DOM 装饰逻辑，不改变任何服务端渲染结构
 * - 与 View Transitions 兼容：所有装饰在 astro:page-load 时重跑
 * =============================================================================
 */

/** 进度记录结构：module/slug -> 最近访问时间戳 */
type ProgressMap = Record<string, number>;

/** localStorage 存储键 */
const STORAGE_KEY = 'fandex-progress';

/**
 * 读取全部进度记录
 * @returns 进度映射；存储不可用或数据损坏时返回空对象
 */
function readProgress(): ProgressMap {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return {};
    const parsed = JSON.parse(raw) as ProgressMap;
    return typeof parsed === 'object' && parsed !== null ? parsed : {};
  } catch {
    return {};
  }
}

/**
 * 写入进度记录（存储不可用时静默降级）
 * @param map - 进度映射
 */
function writeProgress(map: ProgressMap): void {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(map));
  } catch {
    /* 隐私模式等场景下静默忽略 */
  }
}

/**
 * 记录一篇文档为已读
 * @param moduleId - 模块 id
 * @param slug - 文档 slug
 */
export function markDocVisited(moduleId: string, slug: string): void {
  if (!moduleId || !slug) return;
  const map = readProgress();
  map[`${moduleId}/${slug}`] = Date.now();
  writeProgress(map);
}

/**
 * 判断一篇文档是否已读
 * @param moduleId - 模块 id
 * @param slug - 文档 slug
 */
export function isDocVisited(moduleId: string, slug: string): boolean {
  return Boolean(readProgress()[`${moduleId}/${slug}`]);
}

/**
 * 从站内文档链接解析 module/slug
 * 链接形如 {base}{module}/{slug}/（base 已在前缀中剥离）
 * @param href - 链接地址
 * @returns module/slug；无法解析时返回 null
 */
function parseDocHref(href: string): string | null {
  try {
    const url = new URL(href, window.location.origin);
    const base = import.meta.env.BASE_URL;
    if (!url.pathname.startsWith(base)) return null;
    const rest = url.pathname.slice(base.length).replace(/\/+$/, '');
    const parts = rest.split('/');
    // 仅识别 module/slug 两段结构（即文档详情页）
    if (parts.length === 2 && parts[0] && parts[1]) {
      return `${parts[0]}/${parts[1]}`;
    }
    return null;
  } catch {
    return null;
  }
}

/**
 * 侧边栏装饰：为已读文档链接追加 is-visited 标记
 * 章节导航与"全部模块"视图中的文档链接均生效
 */
function decorateSidebar(): void {
  const links = document.querySelectorAll<HTMLAnchorElement>(
    '.fndx-sidebar a[href], [class*="sidebar"] a[href]',
  );
  const progress = readProgress();
  links.forEach((link) => {
    const key = parseDocHref(link.getAttribute('href') ?? '');
    if (key && progress[key]) {
      link.classList.add('is-visited');
    }
  });
}

/**
 * 模块首页装饰：填充 [data-progress-module] 进度指示
 * 容器由 [module]/index.astro 渲染，携带 data-module / data-total 属性
 */
function decorateModuleProgress(): void {
  const host = document.querySelector<HTMLElement>('[data-progress-module]');
  if (!host || host.dataset.progressBound === '1') return;
  const moduleId = host.dataset.module ?? '';
  const total = Number(host.dataset.total ?? '0');
  if (!moduleId || total <= 0) return;

  const progress = readProgress();
  const read = Object.keys(progress).filter((key) => key.startsWith(`${moduleId}/`)).length;
  const ratio = Math.min(1, read / total);
  host.dataset.progressBound = '1';
  host.innerHTML = `
    <span class="doc-progress__text">已读 ${read} / ${total} 篇</span>
    <span class="doc-progress__bar" role="progressbar" aria-valuenow="${Math.round(ratio * 100)}" aria-valuemin="0" aria-valuemax="100">
      <i style="width:${Math.round(ratio * 100)}%"></i>
    </span>
  `;
}

/**
 * 页面装饰入口：挂载时与每次 View Transitions 页面加载后执行
 * 文档页同时记录当前文档为已读（通过 .doc-page 容器上的 data 属性）
 */
function onPageLoad(): void {
  const docRoot = document.getElementById('doc-root');
  if (docRoot?.dataset.module && docRoot.dataset.slug) {
    markDocVisited(docRoot.dataset.module, docRoot.dataset.slug);
  }
  decorateSidebar();
  decorateModuleProgress();
}

// SSR/预渲染环境不执行任何 DOM 逻辑（Astro 构建期会求值页面脚本模块）
if (!import.meta.env.SSR && typeof document !== 'undefined') {
  onPageLoad();
  document.addEventListener('astro:page-load', onPageLoad);
}
