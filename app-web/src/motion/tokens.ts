/**
 * Motion 令牌桥接层
 * =============================================================================
 * 将 ark CSS 动效令牌（src/styles/shared/tokens.css）映射为 Motion React API
 * 可用的 JS 常量，确保 CSS 动画与 Motion 组件动画的观感完全统一。
 *
 * 设计依据：ark-ui 设计语言（Motion 章节）
 * - 直接交互 180-350ms → fast(150) / normal(250)
 * - 区域揭示 500-900ms → slow(400) / slower(600)
 * - 注意力循环 1.6-2.4s → attention(2000)
 * - UI 反馈位移 4-16px → travel micro(4) ~ large(16)
 *
 * 同步约束：值必须与 tokens.css 中的 --motion-* 令牌保持一致，
 *          修改任一处需同步另一处。
 * =============================================================================
 */

/**
 * 时长（单位：秒，Motion React API 使用秒为单位）
 * 与 tokens.css 的 --motion-duration-* 一一对应
 */
export const motionDuration = {
  /** 75ms — 即时反馈（颜色切换、状态切换） */
  instant: 0.075,
  /** 150ms — 快速（悬停、焦点、直接交互） */
  fast: 0.15,
  /** 250ms — 常规（展开、收起、控件过渡） */
  normal: 0.25,
  /** 400ms — 慢速（页面过渡、区域揭示） */
  slow: 0.4,
  /** 600ms — 极慢（复杂编排、大型区域揭示） */
  slower: 0.6,
  /** 2000ms — 注意力循环（呼吸、信号闪烁等克制循环，ark: 1.6-2.4s） */
  attention: 2.0,
} as const;

/**
 * 缓动函数（cubic-bezier 四元组，供 Motion transition.ease 使用）
 * 与 tokens.css 的 --motion-easing-* 一一对应
 */
export const motionEasing = {
  /** 默认柔和入出 */
  default: [0.4, 0, 0.2, 1] as [number, number, number, number],
  /** 入，加速 */
  in: [0.4, 0, 1, 1] as [number, number, number, number],
  /** 出，减速（推荐交互） */
  out: [0, 0, 0.2, 1] as [number, number, number, number],
  /** 入出 */
  inOut: [0.4, 0, 0.2, 1] as [number, number, number, number],
  /** 弹簧近似（轻微过冲），用于 scale / 位移入场 */
  spring: [0.34, 1.56, 0.64, 1] as [number, number, number, number],
  /** 弹跳，用于强调反馈 */
  bounce: [0.68, -0.55, 0.265, 1.55] as [number, number, number, number],
};

/**
 * 物理弹簧预设（Motion 原生 spring 类型）
 * -----------------------------------------------------------------------------
 * 比 cubic-bezier 更自然：支持中断后延续动量，反向播放不生硬。
 * 适用于需要"物理感"的交互：拖拽回弹、列表重排、模态入场。
 */
export const motionSpring = {
  /** 轻弹：微交互释放（tap / press 回弹） */
  soft: { type: 'spring' as const, stiffness: 400, damping: 30, mass: 1 },
  /** 中弹：列表项入场、布局位移 */
  gentle: { type: 'spring' as const, stiffness: 280, damping: 24, mass: 1 },
  /** 硬弹：模态 / 抽屉入场，快速到位 */
  snappy: { type: 'spring' as const, stiffness: 520, damping: 34, mass: 1 },
  /** 慢弹：大型区域揭示，带呼吸感 */
  slow: { type: 'spring' as const, stiffness: 120, damping: 18, mass: 1 },
};

/**
 * 错峰延迟（单位：秒），用于 stagger 子项依次入场
 * 与 tokens.css 的 --motion-delay-stagger-* 一一对应
 */
export const motionStagger = {
  /** 50ms — 紧凑错峰（导航项、工具栏） */
  fast: 0.05,
  /** 100ms — 常规错峰（卡片网格） */
  normal: 0.1,
  /** 200ms — 宽松错峰（长列表、时间线） */
  slow: 0.2,
};

/**
 * 位移距离（单位：px）
 * 与 tokens.css 的 --motion-travel-* 一一对应
 * ark 建议：UI 反馈 4-16px，全区域过渡更大
 */
export const motionTravel = {
  /** 4px — 微反馈（图标抖动、按压下沉） */
  micro: 4,
  /** 8px — 常规位移（卡片入场） */
  small: 8,
  /** 12px — 区域内位移（抽屉、面板） */
  medium: 12,
  /** 16px — 较大位移（模态、弹层） */
  large: 16,
  /** 32px — 全区域过渡（页面段落揭示） */
  section: 32,
};
