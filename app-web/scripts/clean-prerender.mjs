/**
 * 清理 Astro 构建中间产物 .prerender
 * =============================================================================
 * 背景：
 * - Astro 7 + glob loader（deferRender: true）会在 dist/.prerender 生成
 *   内容层中间 JS（含 per-page 内容 chunk 与完整内容数据，实测约 490MB）；
 * - 生成的静态 HTML 页面不引用这些文件（部署实测引用数为 0），
 *   若不清理，dist 会超过 GitHub Pages 1GB 软限制。
 *
 * 调用时机：
 * - 由 build 脚本在 astro build 之后自动执行；
 * - qa-check.mjs 亦会校验 .prerender 不存在，防止回归。
 */
import { existsSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

/** 当前脚本所在目录 */
const __dirname = dirname(fileURLToPath(import.meta.url));
/** Astro 构建输出目录 */
const DIST_DIR = join(__dirname, '..', 'dist');
/** 待清理的中间产物目录 */
const PRERENDER_DIR = join(DIST_DIR, '.prerender');

// 仅在该目录存在时删除，避免误删其他路径；路径已固定且位于 dist 内
if (existsSync(PRERENDER_DIR)) {
  rmSync(PRERENDER_DIR, { recursive: true, force: true });
  console.log(`[clean-prerender] 已清理中间产物: ${PRERENDER_DIR}`);
} else {
  console.log('[clean-prerender] 无需清理（.prerender 不存在）');
}
