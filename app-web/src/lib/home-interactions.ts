/**
 * 首页交互脚本（P7 重构 · 回转寿司式自动滚动 + 真·无限循环）
 * -----------------------------------------------------------------------------
 * 从 pages/index.astro 提取的客户端逻辑，负责：
 * - 分类区域折叠/展开（点击 .category-header__lead 切换 .collapsed 类名）
 * - 横向滑动器自动滚动（回转寿司式 conveyor belt 效果）
 * - 真·双向无限循环（requestAnimationFrame 驱动，无 scroll 边界限制）
 * - 奇偶反向滚动（奇数行向左，偶数行向右）
 * - 速度差异（模块数量越少越快，1.25 倍随机差距）
 * - 悬停暂停（鼠标悬停模块卡片时暂停该行自动滚动，各模块独立）
 * - 鼠标拖拽手动滑动（拖拽时暂停动画，释放后恢复）
 * - 导航按钮控制（点击平移 2 张卡片宽度）
 * - Task 5.3：卡片标题溢出时自动左右滚动（marquee）
 *
 * 回转寿司式自动滚动实现原理（requestAnimationFrame 驱动）：
 * - 每帧通过 transform: translateX(offset) 更新 track 位置
 * - offset 持续递减（向左）或递增（向右），实现连续滚动
 * - 当 offset 超过单份卡片集宽度时，取模回绕实现无缝循环
 * - 卡片集克隆一份（总宽度 2x），回绕时视觉无跳变
 * - 速度 = baseSpeed * (1 - random * 0.25)，模块数量越少 baseSpeed 越快
 *
 * 真·无限循环（无边界）实现：
 * - 不使用 scrollLeft（有边界限制），改用 transform 驱动
 * - offset 取模回绕，用户永远不会到达"开头"或"结尾"
 * - 鼠标拖拽时暂停自动滚动，手动调整 offset，释放后恢复
 *
 * 悬停暂停实现：
 * - mouseenter 时设置 isPaused = true，停止 offset 递增
 * - mouseleave 时设置 isPaused = false，恢复自动滚动
 * - 各模块独立：每个 scroller 实例维护自己的状态
 * -----------------------------------------------------------------------------
 */
import { initTextMarqueeWithResize } from '@/lib/text-overflow';

/** 基础滚动速度（像素/帧），用于计算每个分类的滚动速度
 *  Task 2.1：由 0.6 减半至 0.3，降低自动滚动速度避免视觉疲劳与卡顿感 */
const BASE_SPEED_PX_PER_FRAME = 0.3;

/** 速度随机加速因子上限（0.25 = 最多加速 25%） */
const SPEED_RANDOM_FACTOR = 0.25;

/** 物理惯性：摩擦系数（每帧速度衰减比例，0.95 = 每帧保留 95% 速度）
 *  Task 2.2：拖拽释放后根据释放速度施加指数衰减，模拟自然摩擦 */
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
  /** 鼠标是否已按下（按压状态，不等同于实际拖拽）
   *  实际拖拽以 hasDragStarted 为准，未越过阈值前不更新 transform */
  isDragging: boolean;
  /** 是否已越过 DRAG_THRESHOLD，进入实际拖拽状态
   *  为 false 时 onPointerMove 不更新 transform，保护 click 事件正常派发 */
  hasDragStarted: boolean;
  /** requestAnimationFrame 的 ID，用于取消 */
  rafId: number | null;
  /** 物理惯性：当前惯性速度（px/帧，正负代表方向）
   *  Task 2.2：拖拽释放后根据此值施加指数衰减，模拟自然摩擦 */
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
  // 修复：原实现固定克隆 1 份（总宽度 2x），卡片少于 10 个时
  // 单份宽度 < 视窗宽度，滚动回绕时视窗右侧出现空窗
  // 改为根据视窗宽度动态计算份数，确保总宽度 ≥ 视窗 + 单份宽度
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
   * 每帧更新 offset 并应用到 transform
   * 取模回绕实现无缝循环
   * Task 2.2：惯性激活时跳过自动滚动，由 animateInertia 接管
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
  scroller.addEventListener('mouseenter', () => {
    state.isPaused = true;
  });
  scroller.addEventListener('mouseleave', () => {
    if (!state.isDragging) {
      state.isPaused = reduceMotion;
    }
  });

  // ========== 鼠标拖拽 + 物理惯性（Task 2.2）==========
  let startX = 0;
  let startOffset = 0;
  let dragDistance = 0;
  let pointerId: number | null = null;
  let suppressClick = false;
  // 速度追踪：记录最近一次 move 的时间戳与位置，用于计算释放瞬时速度
  let lastMoveTime = 0;
  let lastMoveX = 0;

  /**
   * 物理惯性动画循环（Task 2.2）
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
      // 惯性结束，恢复自动滚动（除非仍在悬停或 reduceMotion）
      state.isPaused = state.isDragging ? true : reduceMotion;
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
   * Task 2.2：速度低于 INERTIA_MIN_VELOCITY 不启用惯性
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
    // 重置拖拽启动标记：未越过 DRAG_THRESHOLD 前不更新 transform，保护 click
    state.hasDragStarted = false;
    dragDistance = 0;
    startX = e.clientX;
    startOffset = state.offset;
    lastMoveTime = performance.now();
    lastMoveX = e.clientX;
    pointerId = e.pointerId;
    try {
      scroller.setPointerCapture(e.pointerId);
    } catch {
      // 安全降级
    }
    // 不立即添加 is-dragging 类：延迟到 onPointerMove 越过阈值后，
    // 避免点击时光标立即变 grabbing 造成"不能点击"的视觉暗示
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
    try {
      scroller.releasePointerCapture(e.pointerId);
    } catch {
      // 安全降级
    }
    pointerId = null;
    scroller.classList.remove('is-dragging');

    // 只有真正拖拽过（越过阈值）才抑制 click 并启动惯性
    // 未拖拽时 hasDragStarted 为 false，不抑制 click，让 <a> 正常跳转
    if (state.hasDragStarted) {
      suppressClick = true;
      window.setTimeout(() => {
        suppressClick = false;
      }, 120);
      // Task 2.2：启动物理惯性（慢速 < 2px/帧 时无惯性，由 startInertia 内部判断）
      startInertia(state.inertiaVelocity);
    }
    state.hasDragStarted = false;

    // 若未启用惯性，恢复自动滚动
    if (!state.isInertiaActive) {
      state.isPaused = reduceMotion;
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
  // 修复：原实现仅处理 pointerType === 'mouse'，触控板双指滑动无法触发拖拽
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
// Task 5.3：卡片标题溢出检测与 marquee 启用
// 在 scroller 初始化（含卡片克隆）后执行，确保原始与克隆卡片均被检测
initTextMarqueeWithResize('.card-title');
document.addEventListener('astro:page-load', () => {
  initHomeInteractions();
  initScrollers();
  // Task 5.3：View Transitions 后重新检测溢出
  initTextMarqueeWithResize('.card-title');
});
