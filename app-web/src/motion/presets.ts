/**
 * Motion 动效预设库
 * =============================================================================
 * 可复用的 Motion variants 与 transition 预设，覆盖七大动效场景：
 *
 * 1. 入场（enter）    — 挂载 / 进入视口时揭示
 * 2. 退场（exit）     — 卸载 / 离开时移除（配合 AnimatePresence）
 * 3. 微交互（hover/tap）— 悬停 / 按压反馈
 * 4. 布局（layout）   — 共享布局、列表重排
 * 5. 滚动（reveal）   — 滚动触发揭示（配合 whileInView）
 * 6. 错峰（stagger）  — 子项依次入场
 * 7. 注意力（attention）— 克制的呼吸 / 信号循环
 *
 * ark 设计原则落实：
 * - 非纯 opacity 渐变，所有入场 / 揭示均附方向位移或缩放
 * - 直接交互 150-250ms，区域揭示 400-600ms，注意力循环 2000ms
 * - prefers-reduced-motion 由 MotionProvider 全局降级，此处不重复处理
 * =============================================================================
 */
import type { Variants, Transition } from 'motion/react';
import { motionDuration, motionEasing, motionSpring, motionStagger, motionTravel } from './tokens';

// ---------------------------------------------------------------------------
// 通用 Transition 预设
// ---------------------------------------------------------------------------

/** 快速过渡：直接交互（hover / tap / focus） */
const tFast: Transition = { duration: motionDuration.fast, ease: motionEasing.out };

/** 常规过渡：控件展开 / 入场 */
const tNormal: Transition = { duration: motionDuration.normal, ease: motionEasing.out };

/** 揭示过渡：区域入场 / 滚动揭示 */
const tReveal: Transition = { duration: motionDuration.slow, ease: motionEasing.out };

/** 退场过渡：加速离场 */
const tExit: Transition = { duration: motionDuration.fast, ease: motionEasing.in };

// ---------------------------------------------------------------------------
// 1. 入场变体（enter）
//    配合 initial="hidden" animate="visible" 使用
// ---------------------------------------------------------------------------

/** 上滑入场：opacity + Y 位移（最常用，卡片 / 列表项 / 段落） */
export const enterUp: Variants = {
  hidden: { opacity: 0, y: motionTravel.medium },
  visible: { opacity: 1, y: 0, transition: tNormal },
};

/** 下滑入场：从上方落入（下拉菜单顶部项） */
export const enterDown: Variants = {
  hidden: { opacity: 0, y: -motionTravel.medium },
  visible: { opacity: 1, y: 0, transition: tNormal },
};

/** 左滑入场：从右侧滑入（抽屉、侧栏） */
export const enterLeft: Variants = {
  hidden: { opacity: 0, x: motionTravel.medium },
  visible: { opacity: 1, x: 0, transition: tNormal },
};

/** 右滑入场：从左侧滑入（返回动画） */
export const enterRight: Variants = {
  hidden: { opacity: 0, x: -motionTravel.medium },
  visible: { opacity: 1, x: 0, transition: tNormal },
};

/** 缩放入场：opacity + scale（弹簧，用于弹层 / 模态 / 卡片聚焦） */
export const enterScale: Variants = {
  hidden: { opacity: 0, scale: 0.96 },
  visible: { opacity: 1, scale: 1, transition: motionSpring.gentle },
};

/** 纯淡入：仅当位移会破坏布局时使用（如全屏遮罩）；其余场景优先 enterUp */
export const enterFade: Variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: tNormal },
};

// ---------------------------------------------------------------------------
// 2. 退场变体（exit）
//    配合 AnimatePresence 的 exit 属性使用（variants 中 hidden 即退场目标态）
//    注意：exit 变体的 visible 是入场态，hidden 是退场态
// ---------------------------------------------------------------------------

/** 上滑退场：向上消失（列表项移除） */
export const exitUp: Variants = {
  visible: { opacity: 1, y: 0 },
  hidden: { opacity: 0, y: -motionTravel.small, transition: tExit },
};

/** 下滑退场：向下消失（下拉菜单收起） */
export const exitDown: Variants = {
  visible: { opacity: 1, y: 0 },
  hidden: { opacity: 0, y: motionTravel.small, transition: tExit },
};

/** 缩放退场：缩小消失（弹层关闭） */
export const exitScale: Variants = {
  visible: { opacity: 1, scale: 1 },
  hidden: { opacity: 0, scale: 0.96, transition: tExit },
};

// ---------------------------------------------------------------------------
// 3. 微交互变体（hover / tap）
//    配合 whileHover / whileTap 使用
// ---------------------------------------------------------------------------

/** 悬停抬起：hover 时 y 上移 + 轻微放大（卡片、按钮） */
export const hoverLift: Variants = {
  rest: { y: 0, scale: 1 },
  hover: { y: -motionTravel.micro, scale: 1.01, transition: tFast },
};

/** 按压下沉：tap 时轻微缩小（按钮、可点击卡片） */
export const tapPress: Variants = {
  rest: { scale: 1 },
  tap: { scale: 0.98, transition: tFast },
};

/** 信号条延展：hover 时左侧信号色条横向展开（ark 导航项标识） */
export const hoverSignal: Variants = {
  rest: { scaleX: 0 },
  hover: { scaleX: 1, transition: tFast },
};

// ---------------------------------------------------------------------------
// 4. 布局过渡（layout）
//    layout 动画直接用 motion 组件的 layout / layoutId 属性，无需 variants
//    此处导出常用 layout transition 预设
// ---------------------------------------------------------------------------

/** 布局过渡：列表重排、尺寸变化、共享元素过渡 */
export const layoutTransition: Transition = motionSpring.gentle;

// ---------------------------------------------------------------------------
// 5. 滚动揭示变体（reveal）
//    配合 motion 组件的 whileInView="visible" initial="hidden" 使用
// ---------------------------------------------------------------------------

/** 滚动揭示 · 上滑：进入视口时从下方上滑入场（段落、卡片） */
export const revealUp: Variants = {
  hidden: { opacity: 0, y: motionTravel.large },
  visible: { opacity: 1, y: 0, transition: tReveal },
};

/** 滚动揭示 · 左滑：进入视口时从右侧滑入（横向时间线、步骤） */
export const revealLeft: Variants = {
  hidden: { opacity: 0, x: motionTravel.section },
  visible: { opacity: 1, x: 0, transition: tReveal },
};

/** 滚动揭示 · 缩放：进入视口时从 0.92 缩放至 1（图片、图示） */
export const revealScale: Variants = {
  hidden: { opacity: 0, scale: 0.92 },
  visible: { opacity: 1, scale: 1, transition: tReveal },
};

/** 滚动揭示视口配置：进入 20% 区域时触发一次，不重复播放 */
export const revealViewport: { once: boolean; amount: number } = {
  once: true,
  amount: 0.2,
};

// ---------------------------------------------------------------------------
// 6. 错峰容器（stagger）
//    父容器设置 variants + initial/animate，子项设置 enter* variants
// ---------------------------------------------------------------------------

/**
 * 创建错峰容器 variants
 * @param stagger - 子项间隔（秒）
 * @param delayChildren - 首项延迟（秒）
 */
export function createStaggerContainer(
  stagger: number = motionStagger.normal,
  delayChildren: number = 0
): Variants {
  return {
    hidden: {},
    visible: {
      transition: { staggerChildren: stagger, delayChildren },
    },
  };
}

/** 快速错峰容器（导航项、工具栏） */
export const staggerFast: Variants = createStaggerContainer(motionStagger.fast);

/** 常规错峰容器（卡片网格、模块列表） */
export const staggerNormal: Variants = createStaggerContainer(motionStagger.normal);

/** 宽松错峰容器（长列表、时间线、章节段落） */
export const staggerSlow: Variants = createStaggerContainer(motionStagger.slow);

// ---------------------------------------------------------------------------
// 7. 注意力循环变体（attention）
//    ark: 1.6-2.4s 克制循环，用于信号块呼吸、在线状态指示
//    注意：prefers-reduced-motion 启用时由 MotionProvider 自动降级为零时长
// ---------------------------------------------------------------------------

/** 呼吸：opacity 1 ↔ 0.5 的克制循环（信号块、在线指示灯） */
export const attentionBreath: Variants = {
  idle: {
    opacity: [1, 0.5, 1],
    transition: {
      duration: motionDuration.attention,
      ease: 'easeInOut',
      repeat: Infinity,
    },
  },
};

/** 信号脉冲：scale 1 ↔ 1.05 的克制循环（强调徽章、新内容标记） */
export const attentionPulse: Variants = {
  idle: {
    scale: [1, 1.05, 1],
    transition: {
      duration: motionDuration.attention,
      ease: 'easeInOut',
      repeat: Infinity,
    },
  },
};

// ---------------------------------------------------------------------------
// 8. 扩展预设（预留动效扩展点 · P7）
//    为后续多样化动效预留标准接口，避免临时硬编码导致重构困难。
//    使用方式：import { revealMasked, pageFade, marqueeScroll, hoverGlow } from '@/motion';
//    扩展原则：新增动效优先复用本节预设或在此追加，统一消费 motion 令牌。
// ---------------------------------------------------------------------------

/** 裁剪揭示：clip-path 从下向上揭开（图示、卡片聚焦、章节分隔）
 *  非纯 opacity，附 clip-path 方向位移，符合 ark 非纯渐变原则 */
export const revealMasked: Variants = {
  hidden: { opacity: 0, clipPath: 'inset(0 0 100% 0)' },
  visible: {
    opacity: 1,
    clipPath: 'inset(0 0 0% 0)',
    transition: tReveal,
  },
};

/** 页面过渡 · 淡入上滑：View Transitions 降级时的 JS 过渡备选
 *  配合 AnimatePresence 在路由切换时使用 */
export const pageFade: Variants = {
  hidden: { opacity: 0, y: motionTravel.small },
  visible: { opacity: 1, y: 0, transition: tNormal },
  exit: { opacity: 0, y: -motionTravel.small, transition: tExit },
};

/** 跑马灯滚动：横向无限循环（横向滑动器自动播放预留）
 *  预留给 .feature-track 后续接入 Motion 自动 marquee 滚动：
 *  通过 animate 控制 x 位移，配合重复节点实现无缝循环 */
export const marqueeScroll: Transition = {
  duration: 40,
  ease: 'linear',
  repeat: Infinity,
};

/** 悬停光晕：hover 时 boxShadow 扩散品牌色微光（按钮、卡片聚焦）
 *  与 hoverLift 组合使用，增强交互性强的动效反馈 */
export const hoverGlow: Variants = {
  rest: {
    boxShadow: '0 0 0 0 color-mix(in srgb, var(--color-accent-base) 0%, transparent)',
  },
  hover: {
    boxShadow: '0 0 0 4px color-mix(in srgb, var(--color-accent-base) 18%, transparent)',
    transition: tFast,
  },
};

/** 按钮按压涟漪：tap 时 scale 缩小 + 透明度变化（主按钮、操作按钮） */
export const tapRipple: Variants = {
  rest: { scale: 1 },
  tap: { scale: 0.96, transition: tFast },
};
