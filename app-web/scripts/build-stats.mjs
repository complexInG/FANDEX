/**
 * 文档统计预构建脚本
 * =============================================================================
 * 核心执行流程：
 *   1. 递归扫描 cnt-content/full 目录下所有 .md / .mdx 文件
 *   2. 解析每篇文档的 frontmatter，提取 module / category / tags 字段
 *   3. 聚合统计：文档总数、模块数、分类数、标签数
 *   4. 输出 JSON 到 app-web/src/data/doc-stats.json
 *
 * 设计目的：
 *   - 避免首页 getDocStats() 在 dev 模式下调用 getCollection('docs') 全量加载
 *     2003 篇文档导致 OOM（12GB 堆内存仍不足）
 *   - 预构建后首页直接读取 JSON 缓存，零文档内容加载
 *   - dev 脚本启动前自动运行，build 脚本也已包含
 *
 * 性能：扫描 2003 篇文档约 1-2 秒（纯文件系统读取 + 正则解析）
 * =============================================================================
 */
import { readdirSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const contentDir = join(__dirname, '..', '..', 'cnt-content', 'full');
const outputPath = join(__dirname, '..', 'src', 'data', 'doc-stats.json');

/**
 * 递归扫描目录，收集所有 .md / .mdx 文件路径
 * @param {string} dir - 扫描目录
 * @param {string[]} result - 累积的文件路径数组
 * @returns {string[]} 全部 Markdown 文件路径
 */
function collectMarkdownFiles(dir, result = []) {
  const entries = readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = join(dir, entry.name);
    if (entry.isDirectory()) {
      collectMarkdownFiles(fullPath, result);
    } else {
      const ext = extname(entry.name);
      if (ext === '.md' || ext === '.mdx') {
        result.push(fullPath);
      }
    }
  }
  return result;
}

/**
 * 从 Markdown 文件内容中解析 frontmatter 字段
 * 使用正则提取，避免引入 gray-matter 等依赖
 * @param {string} content - 文件完整内容
 * @returns {{ module?: string, category?: string, tags: string[] }}
 */
function parseFrontmatter(content) {
  const result = { module: undefined, category: undefined, tags: [] };
  const fmMatch = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fmMatch) return result;
  const fm = fmMatch[1];

  // module 字段（单值）
  const moduleMatch = fm.match(/^module:\s*(.+)$/m);
  if (moduleMatch) {
    result.module = moduleMatch[1].trim().replace(/['"]/g, '');
  }

  // category 字段（单值，optional）
  const categoryMatch = fm.match(/^category:\s*(.+)$/m);
  if (categoryMatch) {
    result.category = categoryMatch[1].trim().replace(/['"]/g, '');
  }

  // tags 字段（数组，支持 inline [a, b, c] 和 block 格式）
  const tagsInlineMatch = fm.match(/^tags:\s*\[([\s\S]*?)\]/m);
  if (tagsInlineMatch) {
    result.tags = tagsInlineMatch[1]
      .split(',')
      .map((t) => t.trim().replace(/['"]/g, ''))
      .filter(Boolean);
  } else {
    // block 格式：tags:\n  - a\n  - b
    const tagsBlockMatch = fm.match(/^tags:\s*\r?\n((?:\s+-\s+.+\r?\n?)+)/m);
    if (tagsBlockMatch) {
      result.tags = tagsBlockMatch[1]
        .split('\n')
        .map((line) => line.replace(/^\s+-\s+/, '').trim().replace(/['"]/g, ''))
        .filter(Boolean);
    }
  }

  return result;
}

/**
 * 主函数：扫描文档并生成统计 JSON
 */
function main() {
  console.log('[build-stats] Scanning', contentDir);
  const files = collectMarkdownFiles(contentDir);
  console.log(`[build-stats] Found ${files.length} markdown files`);

  const moduleSet = new Set();
  const categorySet = new Set();
  const tagSet = new Set();

  for (const filePath of files) {
    try {
      const content = readFileSync(filePath, 'utf-8');
      const fm = parseFrontmatter(content);
      if (fm.module) moduleSet.add(fm.module);
      if (fm.category) categorySet.add(fm.category);
      for (const tag of fm.tags) tagSet.add(tag);
    } catch {
      // 读取失败时静默跳过
    }
  }

  const stats = {
    totalDocs: files.length,
    totalModules: moduleSet.size,
    totalCategories: categorySet.size,
    totalTags: tagSet.size,
    generatedAt: new Date().toISOString(),
  };

  console.log('[build-stats] Stats:', JSON.stringify(stats, null, 2));

  // 确保输出目录存在
  mkdirSync(dirname(outputPath), { recursive: true });
  writeFileSync(outputPath, JSON.stringify(stats, null, 2) + '\n', 'utf-8');
  console.log('[build-stats] Written to', outputPath);
}

main();
