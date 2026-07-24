/**
 * 进度仪表盘工具函数
 * =============================================================================
 * 从 islands/ProgressDashboard.tsx 提取的纯函数工具集，包含：
 * - 题型/状态中文标签映射
 * - docSlug 解析
 * - 阅读时长、日期、相对时间格式化
 * - 文档 URL 构造
 *
 * 设计说明：
 * - 所有函数均为纯函数（无副作用、不依赖组件闭包状态），可安全提取至模块级别
 * - getDocUrl 内部读取 import.meta.env.BASE_URL（构建时常量），无需外部传入 base
 * - 提取至模块级别有助于 Vite 进行 tree-shaking 与潜在的代码复用
 */

/** 题型 → 中文标签映射表 */
const TYPE_LABELS: Record<string, string> = {
  'fill-blank': '填空',
  choice: '选择',
  'code-fix': '代码修正',
  'open-ended': '开放性',
};

/** 阅读状态 → 中文标签映射表 */
const STATUS_LABELS: Record<string, string> = {
  completed: '已完成',
  reading: '阅读中',
  'not-started': '未开始',
};

/**
 * 题型中文标签
 * @param type - 习题类型
 * @returns 中文标签；未知类型原样返回
 */
export function typeLabel(type: string): string {
  return TYPE_LABELS[type] ?? type;
}

/**
 * 阅读状态中文标签
 * @param status - 阅读状态
 * @returns 中文标签；未知状态原样返回
 */
export function statusLabel(status: string): string {
  return STATUS_LABELS[status] ?? status;
}

/**
 * 从 docSlug 中提取 slug 部分（用于显示标题）
 * @param docSlug - 文档唯一标识（可能为 "moduleId/slug" 格式）
 * @returns slug 部分（首个 "/" 之后的内容；无 "/" 时原样返回）
 */
export function extractSlug(docSlug: string): string {
  const idx = docSlug.indexOf('/');
  return idx >= 0 ? docSlug.slice(idx + 1) : docSlug;
}

/**
 * 格式化阅读时长（秒 → 可读字符串）
 * @param seconds - 总秒数
 * @returns 形如 "1h 23m" 或 "5m" 的字符串；0 秒返回 "0m"
 */
export function formatReadingTime(seconds: number): string {
  if (seconds <= 0) return '0m';
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  if (hours > 0) return `${hours}h${minutes > 0 ? ` ${minutes}m` : ''}`;
  return `${minutes}m`;
}

/**
 * 格式化时间戳为可读日期
 * @param timestamp - 时间戳（ms）；undefined 或假值返回空字符串
 * @returns YYYY-MM-DD 格式字符串
 */
export function formatDate(timestamp: number | undefined): string {
  if (!timestamp) return '';
  const d = new Date(timestamp);
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * 格式化为相对时间（如 "3 天前"）
 * @param timestamp - 时间戳（ms）；undefined 或假值返回空字符串
 * @returns 相对时间字符串；超过 30 天回退为 YYYY-MM-DD 日期格式
 */
export function formatRelativeTime(timestamp: number | undefined): string {
  if (!timestamp) return '';
  const now = Date.now();
  const diff = now - timestamp;
  const seconds = Math.floor(diff / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (days >= 30) return formatDate(timestamp);
  if (days >= 1) return `${days} 天前`;
  if (hours >= 1) return `${hours} 小时前`;
  if (minutes >= 1) return `${minutes} 分钟前`;
  return '刚刚';
}

/**
 * 构造文档 URL
 * @param moduleId - 模块 ID
 * @param docSlug - 文档 slug（可为 "moduleId/slug" 格式或纯 slug）
 * @returns 文档页面 URL（含 BASE_URL 前缀）
 */
export function getDocUrl(moduleId: string, docSlug: string): string {
  const base = import.meta.env.BASE_URL;
  const slug = extractSlug(docSlug);
  return `${base}${moduleId}/${slug}/`;
}
