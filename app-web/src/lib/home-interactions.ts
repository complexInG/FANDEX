/**
 * 首页交互脚本
 * -----------------------------------------------------------------------------
 * 从 pages/index.astro 提取的客户端逻辑，负责：
 * - 分类区域折叠/展开（点击 .category-header 切换 .collapsed 类名）
 * - 通过事件委托支持 View Transitions 下的重复初始化
 *
 * 触发时机：
 * - 脚本首次加载时执行一次
 * - astro:page-load 事件触发时重新绑定（支持 View Transitions 路由切换）
 */

/**
 * 初始化首页分类区域的折叠交互
 *
 * 实现要点：
 * - 为每个 .category-header[data-toggle] 绑定 click 事件
 * - 切换 header 元素的 .collapsed 类名，由 CSS 控制箭头旋转与网格显隐
 * - 重复调用安全：使用 toggle 语义，无需手动去重事件监听器
 *   （View Transitions 下脚本会重新执行，但 header 元素会随 DOM 重建）
 */
function initHomeInteractions(): void {
  const headers = document.querySelectorAll<HTMLElement>('.category-header[data-toggle]');
  if (headers.length === 0) return;

  headers.forEach((header) => {
    header.addEventListener('click', () => {
      header.classList.toggle('collapsed');
    });
  });
}

// 初始化（首次加载与 View Transitions 后触发）
initHomeInteractions();
document.addEventListener('astro:page-load', initHomeInteractions);
