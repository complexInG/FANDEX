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
 */

/** 从环境变量读取字符串值，未设置时返回 fallback */
function envString(key: string, fallback: string): string {
  const value = import.meta.env[key] as string | undefined;
  return typeof value === 'string' && value.length > 0 ? value : fallback;
}

/** 集中配置对象：所有可配置项的唯一来源 */
export const RUNTIME = {
  /** 站点地址（用于 sitemap、canonical、RSS 等绝对链接生成） */
  siteUrl: envString('PUBLIC_SITE_URL', 'https://fanquanpp.github.io/FANDEX'),
} as const;

/** 集中配置的类型声明，供外部模块引用 */
export type RuntimeConfig = typeof RUNTIME;
