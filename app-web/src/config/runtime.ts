/**
 * 运行时集中配置
 *
 * 统一管理站点地址、超时时长等可配置项。
 * 优先从 import.meta.env（环境变量）读取，回退到代码内默认值。
 *
 * 环境变量命名约定：
 * - 客户端可访问变量以 PUBLIC_ 前缀开头（Astro 约定）
 * - 在 .env 或 CI Secrets 中设置即可覆盖默认值
 *
 * 使用方式：
 *   import { RUNTIME } from '@/config/runtime';
 *   const timeout = RUNTIME.codeRunnerTimeoutMs;
 *
 * 偏差报备（DOMPurify 移除）：
 * - 原：包含 dompurifyCdn 字段，用于通过 CDN 加载 DOMPurify HTML 消毒库
 * - 新：全站未实际调用 window.DOMPurify.sanitize()，CDN 脚本从未被 .astro 文件加载
 * - 依据：经 rg 搜索确认 window.DOMPurify 与 DOMPurify.sanitize 在 src/ 下零引用
 * - 同时删除：src/types/dompurify.d.ts 全局类型声明
 */

/** 从环境变量读取字符串值，未设置时返回 fallback */
function envString(key: string, fallback: string): string {
  const value = import.meta.env[key] as string | undefined;
  return typeof value === 'string' && value.length > 0 ? value : fallback;
}

/** 从环境变量读取数值，未设置或无效时返回 fallback */
function envNumber(key: string, fallback: number): number {
  const raw = import.meta.env[key] as string | undefined;
  if (typeof raw !== 'string' || raw.length === 0) return fallback;
  const parsed = Number(raw);
  return Number.isFinite(parsed) ? parsed : fallback;
}

/** 集中配置对象：所有可配置项的唯一来源 */
export const RUNTIME = {
  /** 站点地址（用于 sitemap、canonical、RSS 等绝对链接生成） */
  siteUrl: envString('PUBLIC_SITE_URL', 'https://fanquanpp.github.io/FANDEX'),

  /** 代码运行器默认超时时间（毫秒），防止用户代码死循环 */
  codeRunnerTimeoutMs: envNumber('PUBLIC_CODE_RUNNER_TIMEOUT', 5000),
} as const;

/** 集中配置的类型声明，供外部模块引用 */
export type RuntimeConfig = typeof RUNTIME;
