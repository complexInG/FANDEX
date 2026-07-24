/**
 * Motion 全局配置 Provider
 * =============================================================================
 * 为 Web 端交互岛屿（islands）提供统一的 Motion 运行时配置：
 *
 * 1. reducedMotion="user"
 *    遵循系统 prefers-reduced-motion 偏好。用户启用"减少动效"时，Motion 自动将
 *    动画压为零时长并禁用 layout 动画，保证可访问性降级，无需在各组件重复处理。
 *
 * 2. 默认过渡预设
 *    设置常规时长 + out 缓动作为全局默认，子组件可通过自身 transition 属性覆盖。
 *
 * 使用方式：
 * 由于 Astro 群岛（islands）各自独立水合，无法跨岛屿共享单一 Provider 实例，
 * 每个交互岛屿需在根节点各自包裹 <MotionProvider>。reducedMotion 行为由 Motion
 * 内部读取系统偏好，所有包裹的岛屿行为一致。
 *
 * 示例：
 * ```tsx
 * import { MotionProvider } from '@/motion';
 * import { motion } from 'motion/react';
 *
 * export function MyIsland() {
 *   return (
 *     <MotionProvider>
 *       <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
 *         内容
 *       </motion.div>
 *     </MotionProvider>
 *   );
 * }
 * ```
 * =============================================================================
 */
import { MotionConfig } from 'motion/react';
import type { ReactNode } from 'react';
import { motionDuration, motionEasing } from './tokens';

interface MotionProviderProps {
  /** 子节点 */
  children: ReactNode;
}

/** 全局默认过渡：常规时长 + out 缓动（适用于大多数入场 / 交互场景） */
const defaultTransition = {
  duration: motionDuration.normal,
  ease: motionEasing.out,
};

/**
 * Motion 全局配置 Provider
 * 包裹交互岛屿根节点，统一 reduced-motion 降级策略与默认过渡
 */
export function MotionProvider({ children }: MotionProviderProps) {
  return (
    <MotionConfig reducedMotion="user" transition={defaultTransition}>
      {children}
    </MotionConfig>
  );
}

export default MotionProvider;
