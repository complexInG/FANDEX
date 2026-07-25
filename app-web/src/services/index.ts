/**
 * Service 层统一入口
 * UI 层（pages/components/islands）禁止直接导入 services 内部模块，必须从此文件导入
 * Data 层（getCollection 等）仅允许在 services 内部调用
 *
 * 偏差报备（ProgressToggle 功能删除）：
 * - 原：包含 progress-service 进度服务（getProgress/setProgress/getProgressStats 等）
 * - 新：ProgressToggle（已读/未读）功能已删除，progress-service 及相关类型已移除
 * - 依据：用户明确要求删除 ProgressToggle 及其相关的一切功能、代码、组件、服务
 *
 * 偏差报备（学习路径页删除）：
 * - 原：包含 learning-path-service 学习路径服务（getAllPaths/getPath/getPathProgress 等）
 * - 新：roadmap.astro 学习路径页已删除，learning-path-service 及相关类型已移除
 * - 依据：用户明确要求彻底删除 roadmap.astro 学习路径页及其相关内容
 */

// ── 文档服务 ──
export {
  getAllDocs,
  getDocsByModule,
  getDocBySlug,
  getDocNavigation,
  getDocStats,
  getDocsByCategory,
  getRelatedDocs,
  computeReadingTime,
  docSlug,
} from './doc-service';
export type { DocEntry, DocNavigation, DocStats } from './doc-service';

// ── 模块服务 ──
export {
  getAllModules,
  getModule,
  getModulesByCategory,
  getPrimaryCategory,
  getModulePrerequisites,
  getCategories,
} from './module-service';
export type { Module, CategoryInfo } from './module-service';

// ── 代码运行服务 ──
// 多语言代码沙箱（JS/TS/Python/C/C++），Web Worker 隔离 + 5 秒超时保护
export { runCode, disposeCodeRunner } from './code-runner-service';
export type { RunRequest, RunResult, CodeLanguage } from './code-runner-service';

// ── 可观测性服务 ──
// Web Vitals 性能指标采集（LCP/INP/CLS/TTFB/FCP），持久化到 localStorage
// 提供 p50/p75/p95 分位数统计与 JSON 导出，供 PerformanceMonitor 与外部监控使用
export {
  recordVital,
  getVitals,
  getVitalsSummary,
  clearVitals,
  exportVitalsJSON,
} from './observability-service';
export type {
  VitalName,
  VitalRating,
  VitalRecord,
  VitalPercentiles,
  VitalsSummary,
} from './observability-service';
