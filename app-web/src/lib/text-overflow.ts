/**
 * 文本溢出跑马灯工具
 * ==================
 * 检测元素的文本是否溢出容器宽度，溢出时自动应用跑马灯动画，
 * 并监听窗口 resize 事件重新检测溢出状态。
 *
 * 核心数据流：
 *   CSS 选择器 → 匹配元素列表 → 逐个检测 scrollWidth > clientWidth
 *   溢出 → 添加 .text-marquee 类（触发 CSS 动画）
 *   未溢出 → 移除 .text-marquee 类
 *   window.resize → 防抖重新检测全部元素
 *
 * 使用方式：
 *   import { initTextMarqueeWithResize } from '@/lib/text-overflow';
 *   initTextMarqueeWithResize('.card-title');
 *
 * 依赖 CSS：
 *   .text-marquee 类需在对应样式文件中定义动画规则
 *   动画通常包含 translateX(0) → translateX(calc(-100% + container-width))
 */

/** 防抖延迟（毫秒），避免 resize 事件频繁触发检测 */
const RESIZE_DEBOUNCE_MS = 150;

/**
 * 检测单个元素是否文本溢出，并切换跑马灯类名
 * @param el - 目标 DOM 元素
 */
function checkOverflow(el: HTMLElement): void {
  // scrollWidth > clientWidth 表示内容宽度超出可见区域
  const isOverflowing = el.scrollWidth > el.clientWidth + 1; // +1 容差，避免亚像素误差
  el.classList.toggle('text-marquee', isOverflowing);
}

/**
 * 初始化指定选择器匹配元素的文本溢出跑马灯效果
 * 并绑定 resize 事件实现响应式重新检测
 *
 * @param selector - CSS 选择器，匹配需要检测溢出的元素
 */
export function initTextMarqueeWithResize(selector: string): void {
  const elements = document.querySelectorAll<HTMLElement>(selector);
  elements.forEach(checkOverflow);

  // 防抖 resize 监听：窗口大小变化时重新检测所有匹配元素
  let resizeTimer: ReturnType<typeof setTimeout> | null = null;
  window.addEventListener(
    'resize',
    () => {
      if (resizeTimer) clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        const els = document.querySelectorAll<HTMLElement>(selector);
        els.forEach(checkOverflow);
      }, RESIZE_DEBOUNCE_MS);
    },
    { passive: true },
  );
}
