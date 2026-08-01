/**
 * 全部模块面板按需挂载脚本
 * =============================================================================
 * 背景：
 * - Sidebar.astro 不再在服务端内联全站导航（每页约 500KB 重复 HTML）；
 * - 本脚本监听"切换到全部模块视图"事件，动态加载 SidebarModules 岛并挂载，
 *   未打开过该面板的页面不产生任何额外 DOM 与 JS 执行成本。
 *
 * 触发时机（覆盖全部入口）：
 * 1. Layout 派发的 fandex-switch-modules 事件（tabs 点击）；
 * 2. 直接点击"全部"tab（事件未及时派发时的兜底）；
 * 3. 页面加载/路由切换后，若持久化视图为"全部模块"（面板已可见），立即挂载。
 *
 * 生命周期：
 * - ClientRouter（View Transitions）页面切换后，旧容器随 DOM 替换，
 *   通过 astro:page-load 清理旧 React Root 并重置挂载标记；
 * - 挂载幂等：容器带 data-sidebar-modules-mounted 标记后跳过重复挂载。
 */

import { createElement } from 'react';
import { createRoot, type Root } from 'react-dom/client';

/** 面板滚动容器选择器（Sidebar.astro 中的挂载点） */
const ROOT_SELECTOR = '#sidebar-all-modules-scroll';
/** 全部模块面板选择器（用于判断可见性） */
const PANEL_SELECTOR = '#sidebar-all-modules-panel';
/** 挂载标记属性名 */
const MOUNTED_ATTR = 'data-sidebar-modules-mounted';

/** 当前 React Root 实例（页面切换时清理） */
let rootInstance: Root | null = null;

/**
 * 从挂载点容器读取配置
 * @param container - #sidebar-all-modules-scroll 容器
 * @returns 岛组件 props；moduleId 缺失时返回 null
 */
function parseProps(container: HTMLElement): {
  moduleId: string;
  currentSlug?: string;
} | null {
  const moduleId = container.getAttribute('data-module-id');
  if (!moduleId) return null;
  const currentSlug = container.getAttribute('data-current-slug') || undefined;
  // exactOptionalPropertyTypes：仅在存在时设置可选属性，避免显式赋 undefined
  const props: { moduleId: string; currentSlug?: string } = { moduleId };
  if (currentSlug) props.currentSlug = currentSlug;
  return props;
}

/**
 * 动态加载并挂载 SidebarModules 岛
 * 幂等：已挂载容器直接跳过；动态 import 失败时移除标记允许重试。
 */
export function mountSidebarModules(): void {
  const container = document.querySelector<HTMLElement>(ROOT_SELECTOR);
  if (!container || container.hasAttribute(MOUNTED_ATTR)) return;

  const props = parseProps(container);
  if (!props) return;

  container.setAttribute(MOUNTED_ATTR, 'true');
  import('@/islands/SidebarModules')
    .then(({ default: SidebarModules }) => {
      // 异步加载期间页面可能已切换，容器已被替换则放弃挂载
      if (!document.querySelector(ROOT_SELECTOR)) return;
      rootInstance = createRoot(container);
      rootInstance.render(createElement(SidebarModules, props));
    })
    .catch((err: unknown) => {
      console.error('[sidebar-modules-mount] 挂载失败:', err);
      container.removeAttribute(MOUNTED_ATTR);
    });
}

/**
 * 清理已挂载的 React Root（页面切换前调用）
 * 同时清除所有挂载标记，供新页面重新按需挂载。
 */
function cleanupSidebarModules(): void {
  rootInstance?.unmount();
  rootInstance = null;
  document
    .querySelectorAll<HTMLElement>(`[${MOUNTED_ATTR}]`)
    .forEach((el) => el.removeAttribute(MOUNTED_ATTR));
}

/**
 * 面板已可见时立即挂载
 * 用于持久化视图为"全部模块"的页面：路由切换后 restoreView 会把面板设为可见，
 * 此处延迟一帧再检查，确保视图恢复逻辑先执行。
 */
function ensureMountedWhenVisible(): void {
  requestAnimationFrame(() => {
    const panel = document.querySelector<HTMLElement>(PANEL_SELECTOR);
    if (panel && !panel.classList.contains('is-hidden')) {
      mountSidebarModules();
    }
  });
}

// Layout 派发的视图切换事件（tabs 点击的主路径）
document.addEventListener('fandex-switch-modules', mountSidebarModules);

// 兜底：直接点击"全部"tab（事件派发异常时仍能挂载）
document.addEventListener('click', (event) => {
  const target = event.target as HTMLElement | null;
  if (target?.closest?.('.fndx-sidebar__view-tab[data-view="modules"]')) {
    mountSidebarModules();
  }
});

// 首屏：持久化视图为"全部模块"时直接挂载
ensureMountedWhenVisible();

// 路由切换：先清理旧 Root，再按新页面状态决定是否挂载
document.addEventListener('astro:page-load', () => {
  cleanupSidebarModules();
  ensureMountedWhenVisible();
});
