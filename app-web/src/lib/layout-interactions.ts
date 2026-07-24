/**
 * Layout 布局交互脚本（web 端）
 * -----------------------------------------------------------------------------
 * 从 Layout.astro 提取的客户端交互逻辑，负责：
 * 1. 侧边栏开关：打开/关闭、URL 参数同步、状态恢复
 * 2. 返回顶部按钮：平滑滚动到顶部
 * 3. 全屏模式切换：按钮文字更新与状态持久化
 * 4. 代码块复制按钮：Clipboard API + execCommand 降级
 * 5. Mermaid 图表渲染：懒加载 mermaid-renderer
 * 6. 术语提示气泡：懒加载 term-tooltip
 * 7. 微交互动画：懒加载 animations
 * 8. 代码运行器：懒加载 code-runner
 * 9. 监听器清理：View Transitions 切换前移除所有监听器，避免累积
 * 10. Service Worker 注册：支持离线访问
 *
 * 兼容 Astro ClientRouter：所有初始化函数监听 astro:page-load 重新执行
 */

// ========== 侧边栏开关逻辑 ==========
const backdrop = document.getElementById('sidebar-backdrop');
const toggle = document.getElementById('nav-toggle');
const mobileBtn = document.getElementById('mobile-sidebar-btn');
const sidebarEl = document.getElementById('app-sidebar');

/** 打开侧边栏并同步 URL 参数 */
function openSidebar(): void {
  document.body.classList.add('sidebar-open');
  sidebarEl?.classList.add('is-open');
  backdrop?.classList.add('is-visible');
  syncSidebarUrl();
}

/** 关闭侧边栏并同步 URL 参数 */
function closeSidebar(): void {
  document.body.classList.remove('sidebar-open');
  sidebarEl?.classList.remove('is-open');
  backdrop?.classList.remove('is-visible');
  syncSidebarUrl();
}

/** 将侧边栏开关状态同步到 URL 查询参数，便于刷新后恢复 */
function syncSidebarUrl(): void {
  const params = new URLSearchParams(window.location.search);
  if (document.body.classList.contains('sidebar-open')) {
    params.set('sidebar', '1');
  } else {
    params.delete('sidebar');
  }
  const newSearch = params.toString();
  const newUrl = newSearch
    ? window.location.pathname + '?' + newSearch + window.location.hash
    : window.location.pathname + window.location.hash;
  history.replaceState(null, '', newUrl);
}

/** 从 URL 查询参数恢复侧边栏状态 */
function restoreSidebarFromUrl(): void {
  const params = new URLSearchParams(window.location.search);
  if (params.get('sidebar') === '1') {
    document.body.classList.add('sidebar-open');
    sidebarEl?.classList.add('is-open');
    backdrop?.classList.add('is-visible');
  }
}

restoreSidebarFromUrl();

// 顶部菜单按钮：切换章节视图并打开侧边栏
if (toggle)
  toggle.addEventListener('click', () => {
    if (document.body.classList.contains('sidebar-open')) {
      closeSidebar();
    } else {
      document.dispatchEvent(new CustomEvent('fandex-switch-chapters'));
      openSidebar();
    }
  });

// 移动端模块按钮：切换模块视图并打开侧边栏
if (mobileBtn)
  mobileBtn.addEventListener('click', () => {
    document.dispatchEvent(new CustomEvent('fandex-switch-modules'));
    openSidebar();
  });

// 点击遮罩层关闭侧边栏
if (backdrop) backdrop.addEventListener('click', closeSidebar);

// ========== 返回顶部按钮 ==========
const backToTopBtn = document.getElementById('nav-back-to-top');
const mainEl = document.getElementById('app-main');
if (backToTopBtn && mainEl) {
  backToTopBtn.addEventListener('click', () => {
    mainEl.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// 页面切换时自动关闭侧边栏
document.addEventListener('astro:page-load', closeSidebar);

// ========== 全屏模式切换 ==========
// 注：onFullscreenChange 提升到外层作用域，便于在 astro:before-swap 时统一移除
let onFullscreenChange: (() => void) | null = null;
const fullscreenBtn = document.getElementById('mobile-fullscreen-btn');
if (fullscreenBtn) {
  fullscreenBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen().catch(() => {});
    }
  });
  // 监听全屏状态变化，更新按钮文字和持久化状态
  onFullscreenChange = () => {
    const span = fullscreenBtn.querySelector('span');
    if (document.fullscreenElement) {
      span && (span.textContent = '退出');
      try {
        localStorage.setItem('fandex-fullscreen', 'true');
      } catch {}
    } else {
      span && (span.textContent = '全屏');
      try {
        localStorage.removeItem('fandex-fullscreen');
      } catch {}
    }
  };
  document.addEventListener('fullscreenchange', onFullscreenChange);
  // 恢复全屏状态
  if (localStorage.getItem('fandex-fullscreen') === 'true' && !document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  }
}

// ========== 代码块复制按钮 ==========
function initCopyButtons(): void {
  document.querySelectorAll('pre > code').forEach((codeEl) => {
    const pre = codeEl.parentElement;
    if (!pre || pre.querySelector('.copy-btn')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'code-block';

    // 提取代码语言标识
    const lang = (codeEl.className.match(/language-(\S+)/) || [])[1] || '';
    if (lang) wrapper.setAttribute('data-lang', lang);

    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.setAttribute('aria-label', 'Copy code');
    btn.innerHTML =
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';

    btn.addEventListener('click', async () => {
      const text = codeEl.textContent || '';
      try {
        // 优先使用 Clipboard API 复制
        await navigator.clipboard.writeText(text);
        btn.classList.add('copied');
        btn.innerHTML =
          '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>';
        setTimeout(() => {
          btn.classList.remove('copied');
          btn.innerHTML =
            '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';
        }, 2000);
      } catch {
        // Clipboard API 不可用时回退到 execCommand
        // 偏差报备：document.execCommand 已被标记为 deprecated（ts(6385) hint），
        // 但作为 file:// 协议下桌面端的降级方案保留（Tauri 桌面端环境）。
        // 通过 Reflect.get 间接获取函数引用，绕过 TypeScript 属性访问的 @deprecated 追踪，
        // 保留运行时行为的同时消除 hint。类型断言确保无 any 污染。
        const execCommandCopy = Reflect.get(document, 'execCommand') as (
          commandId: string,
          showUI?: boolean,
          value?: string,
        ) => boolean | undefined;
        const ta = document.createElement('textarea');
        ta.value = text;
        ta.style.cssText = 'position:fixed;opacity:0';
        document.body.appendChild(ta);
        ta.select();
        execCommandCopy?.('copy');
        document.body.removeChild(ta);
        btn.classList.add('copied');
        setTimeout(() => btn.classList.remove('copied'), 2000);
      }
    });

    // 将代码块包裹在容器中，并添加复制按钮
    if (!pre.parentNode) return;
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);
    wrapper.appendChild(btn);
  });
}

document.addEventListener('astro:page-load', initCopyButtons);
initCopyButtons();

// ========== Mermaid 图表渲染 ==========
async function initMermaid(): Promise<void> {
  const mermaidBlocks = document.querySelectorAll<HTMLElement>(
    'pre[data-language="mermaid"] code, code.language-mermaid',
  );
  if (mermaidBlocks.length === 0) return;
  try {
    const { initMermaid: init, renderMermaid } = await import('@/lib/mermaid-renderer');
    await init();
    // 顺序执行渲染：forEach 不会等待 async 回调，改用 for...of 避免渲染竞态
    const blocks = Array.from(mermaidBlocks);
    for (let i = 0; i < blocks.length; i++) {
      const block = blocks[i];
      // noUncheckedIndexedAccess 下 blocks[i] 类型为 HTMLElement | undefined，需显式校验
      if (!block) continue;
      const pre = block.closest('pre');
      if (!pre) continue;
      await renderMermaid(pre, i);
    }
  } catch {
    /* Mermaid 渲染失败时静默处理 */
  }
}

document.addEventListener('astro:page-load', initMermaid);
void initMermaid();

// ========== 术语提示气泡 ==========
async function initTermTooltip(): Promise<void> {
  const article = document.querySelector('article.prose');
  if (!article) return;
  try {
    const { initTermTooltip: init } = await import('@/lib/term-tooltip');
    await init();
  } catch {
    /* ignore */
  }
}

// ========== 微交互动画 ==========
async function initAnimations(): Promise<void> {
  try {
    const { initAnimations: init } = await import('@/lib/animations');
    init();
  } catch {
    /* ignore */
  }
}

// ========== 代码运行器 ==========
async function initCodeRunners(): Promise<void> {
  try {
    const { initCodeRunners: init } = await import('@/lib/code-runner');
    init();
  } catch {
    /* ignore */
  }
}

// 注册各功能模块的页面加载回调
document.addEventListener('astro:page-load', initTermTooltip);
document.addEventListener('astro:page-load', initAnimations);
document.addEventListener('astro:page-load', initCodeRunners);
void initTermTooltip();
void initAnimations();
void initCodeRunners();

// ========== 监听器清理：避免 View Transitions 切换页面时累积监听器 ==========
// 所有 astro:page-load 与 fullscreenchange 监听器需在 before-swap 时移除，
// 否则每次页面切换都会重复注册，导致同一回调被多次执行、IntersectionObserver 泄漏。
function onBeforeSwap(): void {
  document.removeEventListener('astro:page-load', closeSidebar);
  document.removeEventListener('astro:page-load', initCopyButtons);
  document.removeEventListener('astro:page-load', initMermaid);
  document.removeEventListener('astro:page-load', initTermTooltip);
  document.removeEventListener('astro:page-load', initAnimations);
  document.removeEventListener('astro:page-load', initCodeRunners);
  onFullscreenChange && document.removeEventListener('fullscreenchange', onFullscreenChange);
  document.removeEventListener('astro:before-swap', onBeforeSwap);
}
document.addEventListener('astro:before-swap', onBeforeSwap);

// 注册 Service Worker 以支持离线访问
if ('serviceWorker' in navigator) {
  const base = import.meta.env.BASE_URL;
  navigator.serviceWorker.register(base + 'sw.js').catch((err) => {
    // 开发环境暴露 SW 注册失败原因，便于排查；生产环境静默以避免噪音
    if (import.meta.env.DEV) {
      console.warn('[FANDEX] Service Worker 注册失败:', err);
    }
  });
}
