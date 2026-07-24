/**
 * 404 错误页模块搜索脚本
 * -----------------------------------------------------------------------------
 * 从 pages/404.astro 提取的客户端搜索逻辑，负责：
 * - 监听搜索输入框的 input 事件
 * - 按模块名称过滤模块卡片列表
 * - 通过 toggle .hidden 类名控制卡片显隐
 *
 * 触发时机：
 * - 脚本首次加载时执行一次
 * - astro:page-load 事件触发时重新绑定（支持 View Transitions 路由切换）
 *
 * 注：404 页面为独立 HTML（未使用 Layout 组件），故无 View Transitions，
 * 但保留 astro:page-load 监听以保持与其他页面脚本一致的初始化模式。
 */

/**
 * 初始化 404 页面的模块搜索交互
 *
 * 实现要点：
 * - 读取 #error-search-input 与 #error-modules 元素
 * - 遍历 .error-module-card，按 .error-module-name 文本匹配过滤
 * - 输入为空时显示全部卡片；输入非空时仅显示名称包含关键词的卡片
 */
function initErrorSearch(): void {
  const input = document.getElementById('error-search-input') as HTMLInputElement | null;
  const modulesEl = document.getElementById('error-modules');
  if (!input || !modulesEl) return;

  const cards = modulesEl.querySelectorAll<HTMLElement>('.error-module-card');
  input.addEventListener('input', () => {
    const q = input.value.toLowerCase();
    cards.forEach((card) => {
      const name = card.querySelector('.error-module-name')?.textContent?.toLowerCase() || '';
      card.classList.toggle('hidden', q.length > 0 && !name.includes(q));
    });
  });
}

// 初始化
initErrorSearch();
document.addEventListener('astro:page-load', initErrorSearch);
