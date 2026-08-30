/**
 * MERGED 合集再生成脚本（tools/ 内容工程脚本）
 * -----------------------------------------------------------------------------
 * 由各模块子文档重新生成 000-<module>-MERGED.md 合集文件，保证合集内容与
 * 当前文档结构（编号、清单、顺序）一致。
 *
 * 规则：
 * - 子文档按文件名编号升序拼接，frontmatter 剥离
 * - 分隔线：<!-- ============ <module>/<文件名> ============ -->（不含目录号，
 *   避免模块重排后注释再次过时）
 * - 合集 frontmatter 统一重建（order: 10、updated 取今日）
 * - 行尾统一 LF
 *
 * 用法：node tools/regen-merged.mjs
 */
import { readdirSync, readFileSync, writeFileSync, rmSync, existsSync } from 'node:fs';
import { join, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..', 'cnt-content', 'full');
const TODAY = new Date().toISOString().slice(0, 10);

const fmRe = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?/;
const catRe = /^category:\s*(.+?)\s*$/m;

const moduleDirs = readdirSync(ROOT, { withFileTypes: true })
  .filter(e => e.isDirectory())
  .map(e => e.name);

let made = 0, removed = 0;
for (const dirName of moduleDirs) {
  const module = dirName.replace(/^\d+-/, '');
  const moduleDir = join(ROOT, dirName);
  const mergedName = `000-${module}-MERGED.md`;
  const mergedPath = join(moduleDir, mergedName);

  // 子文档：排除既有 MERGED，按文件名编号升序
  const subdocs = readdirSync(moduleDir)
    .filter(f => f.endsWith('.md') && !f.startsWith('000-'))
    .sort((a, b) => parseInt(a.slice(0, 3), 10) - parseInt(b.slice(0, 3), 10));

  if (subdocs.length === 0) {
    // 空模块：移除旧合集，避免留下无内容的空合集页
    if (existsSync(mergedPath)) { rmSync(mergedPath); removed++; }
    continue;
  }

  // 分类取第一篇子文档的 category（与合集 frontmatter 约定一致）
  const first = readFileSync(join(moduleDir, subdocs[0]), 'utf-8');
  const firstFm = first.match(fmRe);
  const catMatch = firstFm ? (firstFm[1].match(catRe) || []) : [];
  const category = catMatch[1] || '工具链';

  const sep = '============================================================';
  const parts = [];
  for (const sub of subdocs) {
    const content = readFileSync(join(moduleDir, sub), 'utf-8');
    const body = content.replace(fmRe, '').replace(/^\s*\n/, '');
    parts.push(`<!-- ${sep} ${module}/${sub.replace(/\.md$/, '')} ${sep} -->\n\n${body.trimEnd()}\n`);
  }

  const merged = [
    '---',
    'order: 10',
    `title: ${module} 模块文档合集`,
    `module: '${module}'`,
    `category: ${category}`,
    'difficulty: intermediate',
    'description: 本模块全部文档合并生成的完整合集，按学习顺序排列。',
    'author: fanquanpp',
    `updated: '${TODAY}'`,
    'related: []',
    'prerequisites: []',
    '---',
    '',
    parts.join('\n'),
  ].join('\n');

  writeFileSync(mergedPath, merged, 'utf-8');
  made++;
}
console.log(`MERGED regenerated: ${made} 个生成，${removed} 个空合集移除`);
