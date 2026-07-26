/**
 * 首页交互脚本（回转寿司式自动滚动 + 真·无限循环）
 * -----------------------------------------------------------------------------
 * 负责：
 * - 分类区域折叠/展开
 * - 横向滑动器自动滚动（conveyor belt 效果）
 * - 真·双向无限循环（requestAnimationFrame 驱动，无 scroll 边界）
 * - 奇偶反向滚动 + 速度差异（模块数量越少越快）
 * - 悬停暂停（各模块独立）
 * - 鼠标拖拽 + 物理惯性 + 触控板水平滑动
 * - 导航按钮控制（平移 2 张卡片宽度）
 * - 卡片标题溢出时 marquee 滚动
 *
 * 核心实现：
 * - transform: translateX(offset) 驱动，offset 取模回绕实现无缝循环
 * - 克隆卡片集确保总宽度 ≥ 视窗 + 单份宽度，避免回绕空窗
 * - 悬停/拖拽时暂停自动滚动，由 mouseleave 恢复
 * ----------------------------------------------------------------------------- */
import { initTextMarqueeWithResize } from '@/lib/text-overflow';

/** 基础滚动速度（像素/帧），用于计算每个分类的滚动速度 */
const BASE_SPEED_PX_PER_FRAME = 0.3;

/** 速度随机加速因子上限（0.25 = 最多加速 25%） */
const SPEED_RANDOM_FACTOR = 0.25;

/** 物理惯性：摩擦系数（每帧速度衰减比例，0.95 = 每帧保留 95% 速度） */
const INERTIA_FRICTION = 0.95;

/** 物理惯性：悬停时加速衰减系数（用户悬停时惯性更快停止） */
const INERTIA_HOVER_ACCELERATE = 0.85;

/** 物理惯性：触发阈值（释放时速度低于此值不启用惯性，单位 px/帧） */
const INERTIA_MIN_VELOCITY = 2;

/** 物理惯性：最小停止速度（速度低于此值时惯性终止） */
const INERTIA_STOP_VELOCITY = 0.1;

/** 拖拽阈值（像素）：移动超过此距离才认定为拖拽，未超过时保护 click 事件
 *  修复：原实现按下即更新 transform，微小抖动导致卡片位移、click 不触发、无法跳转
 *  引入阈值后，5px 以内的移动不更新 transform，浏览器正常派发 click 给 <a> */
const DRAG_THRESHOLD = 5;

/** 物理惯性：最大持续时间（毫秒），防止无限惯性 */
const INERTIA_MAX_DURATION = 2500;

/** 卡片数量对速度的影响系数（数量越少速度越快） */
const CARD_COUNT_SPEED_BOOST = 0.04;

/** 最大速度提升（卡片极少时速度上限） */
const MAX_SPEED_BOOST = 0.6;

/**
 * 初始化首页分类区域的折叠交互
 */
function initHomeInteractions(): void {
  const leads = document.querySelectorAll<HTMLElement>('.category-header__lead[data-toggle]');
  leads.forEach((lead) => {
    if (lead.dataset.bound === 'true') return;
    lead.dataset.bound = 'true';

    lead.addEventListener('click', () => {
      const section = lead.closest('.category-section');
      if (section) {
        section.classList.toggle('collapsed');
      }
    });
  });
}

/**
 * 单个滑动器实例的状态与控制逻辑
 */
interface ScrollerState {
  /** 当前 translateX 偏移量（像素） */
  offset: number;
  /** 单份卡片集宽度（像素），用于取模回绕 */
  cardSetWidth: number;
  /** 滚动方向：'left' 向左（offset 递减）| 'right' 向右（offset 递增） */
  direction: 'left' | 'right';
  /** 每帧移动速度（像素/帧） */
  speed: number;
  /** 是否暂停自动滚动（悬停或拖拽时） */
  isPaused: boolean;
  /** 鼠标是否悬停在 scroller 内
   *  用于 onPointerUp / animateInertia 判断是否应保持暂停：
   *  鼠标在 scroller 内时由 mouseenter 设置为 true，pointerup 后不恢复自动滚动，
   *  避免 track 在 click 事件前位移导致 <a> 跳转失败；mouseleave 时恢复 */
  isHovering: boolean;
  /** 鼠标是否已按下（按压状态，不等同于实际拖拽） */
  isDragging: boolean;
  /** 是否已越过 DRAG_THRESHOLD，进入实际拖拽状态
   *  为 false 时 onPointerMove 不更新 transform，保护 click 事件派发 */
  hasDragStarted: boolean;
  /** requestAnimationFrame 的 ID，用于取消 */
  rafId: number | null;
  /** 物理惯性：当前惯性速度（px/帧，正负代表方向） */
  inertiaVelocity: number;
  /** 物理惯性：是否正在惯性滑动中
   *  惯性期间禁用自动滚动 animate，由 animateInertia 接管 offset 更新 */
  isInertiaActive: boolean;
  /** 物理惯性：惯性动画 rafId，用于取消 */
  inertiaRafId: number | null;
  /** 物理惯性：惯性开始时间戳，用于限制最大持续时间 */
  inertiaStartTime: number;
}

/**
 * 初始化单个滑动器的自动滚动、无限循环、拖拽与导航按钮
 */
function initScroller(scroller: HTMLElement, rowIndex: number): void {
  const track = scroller.querySelector<HTMLElement>('[data-track]');
  if (!track) return;

  // 首次初始化标记
  if (track.dataset.initialized === 'true') return;

  const cards = Array.from(track.children) as HTMLElement[];
  if (cards.length === 0) return;

  // 测量单份卡片集宽度（在克隆前使用原始卡片计算）
  // 动态计算克隆份数，确保总宽度 ≥ 视窗 + 单份宽度，避免回绕时视窗右侧空窗
  const gapStr = getComputedStyle(track).gap;
  const gap = parseFloat(gapStr) || 16;
  let originalCardSetWidth = 0;
  for (const card of cards) {
    originalCardSetWidth += card.getBoundingClientRect().width + gap;
  }
  const viewportWidth = scroller.clientWidth;

  // 计算需要的份数：总宽度 ≥ 视窗宽度 + 单份宽度
  // 保证 offset 从 0 回绕到 -cardSetWidth 时视窗始终有内容
  // 最少 2 份（原始 + 1 份克隆），卡片少时自动增加至 3 份或更多
  const neededCopies = Math.max(
    2,
    Math.ceil((viewportWidth + originalCardSetWidth) / originalCardSetWidth),
  );

  // 克隆 neededCopies - 1 份（原始已有 1 份），实现无缝循环
  for (let i = 1; i < neededCopies; i++) {
    cards.forEach((card) => {
      const clone = card.cloneNode(true) as HTMLElement;
      clone.setAttribute('aria-hidden', 'true');
      clone.setAttribute('tabindex', '-1');
      clone.style.animation = 'none';
      track.appendChild(clone);
    });
  }

  track.dataset.initialized = 'true';

  // 确定滚动方向：rowIndex 0, 2, 4... 向左；1, 3, 5... 向右
  const direction: 'left' | 'right' = rowIndex % 2 === 0 ? 'left' : 'right';

  // 计算单份卡片集宽度（总宽度 / 份数）
  // 无论克隆多少份，除以份数即为单份宽度，取模回绕逻辑不变
  const measureCardSetWidth = (): number => {
    return track.scrollWidth / neededCopies;
  };

  // 计算滚动速度：卡片数量越少速度越快
  // speed = BASE_SPEED * (1 + boost) * (1 - random * 0.25)
  // boost = min(MAX_SPEED_BOOST, CARD_COUNT_SPEED_BOOST * (20 - cardCount))
  const cardCount = cards.length;
  const speedBoost = Math.min(MAX_SPEED_BOOST, CARD_COUNT_SPEED_BOOST * Math.max(0, 20 - cardCount));
  const randomFactor = 1 - Math.random() * SPEED_RANDOM_FACTOR;
  const speed = BASE_SPEED_PX_PER_FRAME * (1 + speedBoost) * randomFactor;

  // 尊重用户减少动效偏好
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const state: ScrollerState = {
    offset: 0,
    cardSetWidth: measureCardSetWidth(),
    direction,
    speed,
    isPaused: reduceMotion,
    isHovering: false,
    isDragging: false,
    hasDragStarted: false,
    rafId: null,
    inertiaVelocity: 0,
    isInertiaActive: false,
    inertiaRafId: null,
    inertiaStartTime: 0,
  };

  /**
   * 将 offset 取模回绕到 [-cardSetWidth, 0] 范围，保持无缝循环
   * @param rawOffset 原始偏移量
   * @returns 规范化后的偏移量
   */
  const normalizeOffset = (rawOffset: number): number => {
    let result = rawOffset;
    while (result > 0) {
      result -= state.cardSetWidth;
    }
    while (result < -state.cardSetWidth) {
      result += state.cardSetWidth;
    }
    return result;
  };

  /**
   * 自动滚动动画循环
   * 每帧更新 offset 并应用到 transform，取模回绕实现无缝循环
   * 惯性激活时跳过自动滚动，由 animateInertia 接管
   */
  const animate = (): void => {
    if (!state.isPaused && !state.isDragging && !state.isInertiaActive) {
      // 更新偏移量
      if (state.direction === 'left') {
        state.offset -= state.speed;
        // 向左滚动：offset 超过 -cardSetWidth 时回绕到 0
        if (state.offset <= -state.cardSetWidth) {
          state.offset += state.cardSetWidth;
        }
      } else {
        state.offset += state.speed;
        // 向右滚动：offset 超过 0 时回绕到 -cardSetWidth
        if (state.offset >= 0) {
          state.offset -= state.cardSetWidth;
        }
      }
      // 应用 transform
      track.style.transform = `translateX(${state.offset}px)`;
    }
    state.rafId = requestAnimationFrame(animate);
  };

  // 启动动画循环
  state.rafId = requestAnimationFrame(animate);

  // ========== 悬停暂停 ==========
  // mouseenter/mouseleave 管理 isHovering 标志，供 onPointerUp / animateInertia 判断
  // 鼠标在 scroller 内时保持暂停，避免 pointerup 后 track 位移导致 click 失效
  scroller.addEventListener('mouseenter', () => {
    state.isHovering = true;
    state.isPaused = true;
  });
  scroller.addEventListener('mouseleave', () => {
    state.isHovering = false;
    if (!state.isDragging) {
      state.isPaused = reduceMotion;
    }
  });

  // ========== 鼠标拖拽 + 物理惯性 ==========
  let startX = 0;
  let startOffset = 0;
  let dragDistance = 0;
  let pointerId: number | null = null;
  let suppressClick = false;
  // 速度追踪：记录最近一次 move 的时间戳与位置，用于计算释放瞬时速度
  let lastMoveTime = 0;
  let lastMoveX = 0;

  /**
   * 物理惯性动画循环
   * - 每帧 offset += inertiaVelocity，并应用摩擦系数衰减
   * - 悬停时使用 INERTIA_HOVER_ACCELERATE 加速衰减，快速停止
   * - 速度低于 INERTIA_STOP_VELOCITY 或超过 INERTIA_MAX_DURATION 时终止
   * - 终止后恢复自动滚动
   */
  const animateInertia = (): void => {
    if (!state.isInertiaActive) return;

    const elapsed = performance.now() - state.inertiaStartTime;
    // 终止条件：超时或速度过低
    if (elapsed > INERTIA_MAX_DURATION || Math.abs(state.inertiaVelocity) < INERTIA_STOP_VELOCITY) {
      state.isInertiaActive = false;
      state.inertiaVelocity = 0;
      state.inertiaRafId = null;
      // 惯性结束，恢复自动滚动：鼠标仍在 scroller 内时保持暂停（由 mouseleave 恢复）
      state.isPaused = state.isDragging || state.isHovering || reduceMotion;
      return;
    }

    // 更新 offset
    state.offset = normalizeOffset(state.offset + state.inertiaVelocity);
    track.style.transform = `translateX(${state.offset}px)`;

    // 摩擦衰减：悬停时加速衰减，否则标准摩擦
    const friction = state.isPaused ? INERTIA_HOVER_ACCELERATE : INERTIA_FRICTION;
    state.inertiaVelocity *= friction;

    state.inertiaRafId = requestAnimationFrame(animateInertia);
  };

  /**
   * 启动物理惯性滑动
   * @param releaseVelocity 释放时的瞬时速度（px/帧，正负代表方向）
   * 速度低于 INERTIA_MIN_VELOCITY 不启用惯性
   */
  const startInertia = (releaseVelocity: number): void => {
    if (Math.abs(releaseVelocity) < INERTIA_MIN_VELOCITY) {
      // 慢速无惯性，直接恢复自动滚动
      state.isInertiaActive = false;
      state.inertiaVelocity = 0;
      return;
    }
    state.isInertiaActive = true;
    state.inertiaVelocity = releaseVelocity;
    state.inertiaStartTime = performance.now();
    // 惯性期间暂停自动滚动
    state.isPaused = true;
    if (state.inertiaRafId !== null) {
      cancelAnimationFrame(state.inertiaRafId);
    }
    state.inertiaRafId = requestAnimationFrame(animateInertia);
  };

  const onPointerDown = (e: PointerEvent) => {
    if (e.pointerType !== 'mouse' || e.button !== 0) return;
    // 拖拽开始时取消任何进行中的惯性
    if (state.inertiaRafId !== null) {
      cancelAnimationFrame(state.inertiaRafId);
      state.inertiaRafId = null;
    }
    state.isInertiaActive = false;
    state.inertiaVelocity = 0;
    state.isDragging = true;
    // pointerdown 时鼠标必然在 scroller 内，强制标记 isHovering = true
    // 防止页面加载时鼠标已在 scroller 内导致 mouseenter 未触发、isHovering 为 false
    // 此时 pointerup 后 isPaused 被设为 false，track 在 click 前位移，click 不派发
    state.isHovering = true;
    state.isPaused = true;
    state.hasDragStarted = false;
    dragDistance = 0;
    startX = e.clientX;
    startOffset = state.offset;
    lastMoveTime = performance.now();
    lastMoveX = e.clientX;
    pointerId = e.pointerId;
    // 不在按下时立即 setPointerCapture：会重定向 pointerup 到 scroller，
    // 导致 pointerdown(<a>) 与 pointerup(scroller) 不在同一元素，click 不派发。
    // 延迟到 onPointerMove 越过阈值后才捕获指针，保护普通点击的 click 派发。
  };

  const onPointerMove = (e: PointerEvent) => {
    if (!state.isDragging || e.pointerId !== pointerId) return;
    const dx = e.clientX - startX;
    dragDistance = Math.abs(dx);

    // 拖拽阈值闸门：未越过 DRAG_THRESHOLD 前不更新 transform，不添加 is-dragging 类
    // 这是 click 事件得以正常派发的关键 —— 卡片不位移，浏览器判定为有效点击
    if (!state.hasDragStarted) {
      if (dragDistance <= DRAG_THRESHOLD) {
        return;
      }
      // 首次越过阈值，进入实际拖拽：切换光标、标记启动
      state.hasDragStarted = true;
      scroller.classList.add('is-dragging');
      // 越过阈值后才捕获指针，确保拖拽中即使鼠标移出 scroller 仍能接收事件
      // 此时 click 已被 suppressClick 抑制，不影响跳转
      try {
        scroller.setPointerCapture(e.pointerId);
      } catch {
        // 安全降级
      }
    }

    // 手动更新 offset，实时跟手
    let newOffset = startOffset + dx;
    // 取模回绕，保持 offset 在 [-cardSetWidth, 0] 范围内
    newOffset = normalizeOffset(newOffset);
    state.offset = newOffset;
    track.style.transform = `translateX(${state.offset}px)`;

    // 速度追踪：基于最近一次 move 的位移与时间差计算瞬时速度（px/帧，约 16ms）
    const now = performance.now();
    const dt = now - lastMoveTime;
    if (dt > 0) {
      const moveDx = e.clientX - lastMoveX;
      // 换算为 px/帧（假设 60fps，1 帧 ≈ 16.67ms）
      state.inertiaVelocity = (moveDx / dt) * 16.67;
    }
    lastMoveTime = now;
    lastMoveX = e.clientX;
  };

  const onPointerUp = (e: PointerEvent) => {
    if (!state.isDragging || e.pointerId !== pointerId) return;
    state.isDragging = false;
    // 只有真正拖拽过（越过阈值）才释放指针捕获并抑制 click
    // 未拖拽时未调用 setPointerCapture，无需 release，click 正常派发给 <a>
    if (state.hasDragStarted) {
      try {
        scroller.releasePointerCapture(e.pointerId);
      } catch {
        // 安全降级
      }
      suppressClick = true;
      window.setTimeout(() => {
        suppressClick = false;
      }, 120);
      // 启动物理惯性（慢速 < 2px/帧 时无惯性，由 startInertia 内部判断）
      startInertia(state.inertiaVelocity);
    }
    pointerId = null;
    scroller.classList.remove('is-dragging');
    state.hasDragStarted = false;

    // 若未启用惯性，恢复自动滚动：鼠标仍在 scroller 内时保持暂停
    // 由 mouseleave 在鼠标离开时恢复自动滚动，避免 click 前 track 位移
    if (!state.isInertiaActive) {
      state.isPaused = state.isHovering || reduceMotion;
    }
  };

  scroller.addEventListener('pointerdown', onPointerDown);
  scroller.addEventListener('pointermove', onPointerMove);
  scroller.addEventListener('pointerup', onPointerUp);
  scroller.addEventListener('pointercancel', onPointerUp);

  // 捕获阶段抑制拖拽后的卡片链接点击
  scroller.addEventListener(
    'click',
    (e) => {
      if (suppressClick) {
        e.preventDefault();
        e.stopPropagation();
      }
    },
    true,
  );

  // ========== 导航按钮 ==========
  const section = scroller.closest('.category-section');
  if (section) {
    const navBtns = section.querySelectorAll<HTMLButtonElement>('[data-nav]');
    navBtns.forEach((btn) => {
      if (btn.dataset.bound === 'true') return;
      btn.dataset.bound = 'true';

      btn.addEventListener('click', () => {
        const dir = parseInt(btn.dataset.nav || '1', 10);
        const firstCard = cards[0];
        if (!firstCard) return;
        const cardWidth = firstCard.getBoundingClientRect().width;
        const gapStr = getComputedStyle(track).gap;
        const gap = parseFloat(gapStr) || 16;
        const step = (cardWidth + gap) * 2;

        // 导航按钮：暂停自动滚动，平滑过渡到新 offset，然后恢复
        const wasPaused = state.isPaused;
        state.isPaused = true;
        const targetOffset = state.offset - dir * step;
        const startOffset = state.offset;
        const duration = 300; // ms
        const startTime = performance.now();

        const easeOut = (t: number): number => 1 - Math.pow(1 - t, 3);

        const animateNav = (now: number): void => {
          const elapsed = now - startTime;
          const progress = Math.min(1, elapsed / duration);
          const eased = easeOut(progress);
          let newOffset = startOffset + (targetOffset - startOffset) * eased;
          // 取模回绕
          while (newOffset > 0) {
            newOffset -= state.cardSetWidth;
          }
          while (newOffset < -state.cardSetWidth) {
            newOffset += state.cardSetWidth;
          }
          state.offset = newOffset;
          track.style.transform = `translateX(${state.offset}px)`;
          if (progress < 1) {
            requestAnimationFrame(animateNav);
          } else {
            // 恢复自动滚动
            state.isPaused = wasPaused;
          }
        };
        requestAnimationFrame(animateNav);
      });
    });
  }

  // ========== 触控板双指水平滑动 ==========
  // 触控板双指水平滑动触发 wheel 事件（deltaX），而非 pointer 事件
  // 当 deltaX 绝对值大于 deltaY 时认定为水平滑动，更新 offset 并暂停自动滚动
  const onWheel = (e: WheelEvent) => {
    // 仅处理水平为主的滑动（deltaX 绝对值大于 deltaY）
    if (Math.abs(e.deltaX) <= Math.abs(e.deltaY)) return;
    if (Math.abs(e.deltaX) < 2) return;
    e.preventDefault();
    // 暂停自动滚动，让用户手动控制
    state.isPaused = true;
    // 更新 offset（deltaX 为正表示向右滑动，track 应向左移动）
    state.offset = normalizeOffset(state.offset - e.deltaX);
    track.style.transform = `translateX(${state.offset}px)`;
  };
  scroller.addEventListener('wheel', onWheel, { passive: false });

  // ========== 响应窗口大小变化 ==========
  // 窗口大小变化时重新计算 cardSetWidth
  const handleResize = (): void => {
    state.cardSetWidth = measureCardSetWidth();
  };
  window.addEventListener('resize', handleResize);

  // ========== View Transitions 清理 ==========
  // 页面切换时取消动画帧（含自动滚动与物理惯性），避免内存泄漏
  const cleanup = (): void => {
    if (state.rafId !== null) {
      cancelAnimationFrame(state.rafId);
    }
    if (state.inertiaRafId !== null) {
      cancelAnimationFrame(state.inertiaRafId);
    }
    window.removeEventListener('resize', handleResize);
    scroller.removeEventListener('wheel', onWheel);
    document.removeEventListener('astro:before-swap', cleanup);
  };
  document.addEventListener('astro:before-swap', cleanup);
}

/**
 * 初始化所有横向滑动器
 */
function initScrollers(): void {
  const scrollers = document.querySelectorAll<HTMLElement>('[data-scroller]');
  scrollers.forEach((scroller, index) => {
    initScroller(scroller, index);
  });
}

// 初始化（首次加载与 View Transitions 后触发）
initHomeInteractions();
initScrollers();
// 卡片标题溢出检测与 marquee 启用（在 scroller 初始化含卡片克隆后执行）
initTextMarqueeWithResize('.card-title');
document.addEventListener('astro:page-load', () => {
  initHomeInteractions();
  initScrollers();
  initTextMarqueeWithResize('.card-title');
});
