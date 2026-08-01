/**
 * 微交互动画脚本
 * -----------------------------------------------------------------------------
 * 负责：
 * - 模块卡片悬停高亮（通过 CSS 类切换，避免内联样式重绘开销）
 * - 锚点链接平滑滚动（在 #app-main 容器内滚动至目标元素）
 *
 * 设计原则：
 * - 仅绑定交互类名切换，视觉表现由 CSS 控制（card-hovered 类）
 * - 锚点滚动通过 scrollTo({ behavior: 'smooth' }) 触发浏览器原生平滑滚动
 * - 与 View Transitions 兼容：每次 astro:page-load 重新执行绑定
 * - 绑定守卫：通过 dataset.bound 防止同一元素重复绑定
 */

/**
 * 初始化微交互动画
 * 包含模块卡片悬停效果与锚点链接平滑滚动
 */
export function initAnimations(): void {
  // 模块卡片悬停：通过 mouseenter/mouseleave 切换 .card-hovered 类
  // 视觉表现（如阴影）由 components.css 中的 .module-card.card-hovered 定义
  document.querySelectorAll<HTMLElement>('.module-card').forEach((card) => {
    if (card.dataset.bound === '1') return;
    card.dataset.bound = '1';
    card.addEventListener('mouseenter', () => card.classList.add('card-hovered'));
    card.addEventListener('mouseleave', () => card.classList.remove('card-hovered'));
  });

  // 锚点链接平滑滚动：处理 #app-main 容器内的 a[href^="#"] 链接
  document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]').forEach((anchor) => {
    if (anchor.dataset.bound === '1') return;
    anchor.dataset.bound = '1';

    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      // 空锚点跳过
      if (!href || href === '#') return;
      const target = document.querySelector<HTMLElement>(href);
      if (!target) return;

      e.preventDefault();
      const main = document.getElementById('app-main');
      if (!main) return;

      // 计算目标元素相对 #app-main 的滚动位置
      const mainRect = main.getBoundingClientRect();
      const targetRect = target.getBoundingClientRect();
      // 减去 20px 顶部偏移，避免目标紧贴容器顶边
      main.scrollTo({
        top: main.scrollTop + targetRect.top - mainRect.top - 20,
        behavior: 'smooth',
      });
    });
  });
}
