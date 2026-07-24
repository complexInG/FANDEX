/**
 * Motion 动效体系统一出口
 * =============================================================================
 * Web 端动效基础架构，基于 Motion（原 Framer Motion）React API。
 *
 * 分层设计：
 * - tokens         动效令牌桥接（CSS ↔ JS），与 styles/shared/tokens.css 同步
 * - MotionProvider 全局 MotionConfig，reduced-motion 降级 + 默认过渡
 * - presets        可复用 variants / transition 预设（七大动效场景）
 *
 * 使用示例：
 * ```tsx
 * import { MotionProvider, enterUp, staggerNormal } from '@/motion';
 * import { motion } from 'motion/react';
 *
 * export function ModuleGrid() {
 *   return (
 *     <MotionProvider>
 *       <motion.ul
 *         variants={staggerNormal}
 *         initial="hidden"
 *         animate="visible"
 *       >
 *         <motion.li variants={enterUp}>模块 A</motion.li>
 *         <motion.li variants={enterUp}>模块 B</motion.li>
 *       </motion.ul>
 *     </MotionProvider>
 *   );
 * }
 * ```
 *
 * 扩展预留：
 * - 后续按需新增 revealMasked（clip-path 裁剪揭示）、pageTransition（页面过渡）
 *   等高级预设，统一在此出口导出
 * - 三端动效独立：本目录为 app-web 专属，desktop / android 各自维护
 * =============================================================================
 */

export * from './tokens';
export * from './MotionProvider';
export * from './presets';
