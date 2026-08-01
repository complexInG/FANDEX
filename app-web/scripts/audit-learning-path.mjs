/**
 * 学习路径审计脚本
 * =============================================================================
 * 功能概述：
 * 1. 校验 shd-shared/metadata/learning-path/ 下全部知识地图的结构合法性
 * 2. 校验地图引用的模块 ID 与文档 slug 是否真实存在
 * 3. 输出每门技术的覆盖统计与"待补充文档"缺口清单
 * 4. 可选：为缺口生成 Markdown 文档模板（--templates 目录）
 *
 * 使用方式：
 *   node scripts/audit-learning-path.mjs
 *   node scripts/audit-learning-path.mjs --write-report
 *   node scripts/audit-learning-path.mjs --templates ../tmp/gap-templates
 *
 * 设计说明：
 * - 直接扫描文件系统，不依赖 Astro 构建缓存（doc-index.json），可独立运行
 * - 数据结构校验使用 zod（app-web 已有依赖），保证与共享类型一致
 * - 报告写入 .trae/documents/ 便于作为内容工作清单持续维护
 * =============================================================================
 */
import { readdirSync, readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, dirname, basename, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { z } from 'zod';

const __dirname = dirname(fileURLToPath(import.meta.url));
/** FANDEX 仓库根目录 */
const ROOT = join(__dirname, '..', '..');
/** 学习路径数据目录 */
const MAP_DIR = join(ROOT, 'shd-shared', 'metadata', 'learning-path');
/** 共享模块元数据 */
const MODULES_PATH = join(ROOT, 'shd-shared', 'metadata', 'modules.json');
/** 内容目录 */
const CONTENT_DIR = join(ROOT, 'cnt-content', 'full');
/** 缺口报告输出目录 */
const REPORT_DIR = join(ROOT, '.trae', 'documents');

// ============================================================
// Schema 定义（与 shd-shared/utl-utils/learning-path.ts 对齐）
// ============================================================

const officialLinkSchema = z.object({
  label: z.string().min(1),
  url: z.string().url(),
});

const knowledgeNodeSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  desc: z.string().optional(),
  difficulty: z.enum(['beginner', 'intermediate', 'advanced']).optional(),
  doc: z.string().min(1).optional(),
  official: officialLinkSchema.optional(),
});

const knowledgeStageSchema = z.object({
  id: z.string().min(1),
  title: z.string().min(1),
  subtitle: z.string().optional(),
  nodes: z.array(knowledgeNodeSchema).min(1),
});

const technologyMapSchema = z.object({
  version: z.string(),
  module: z.string().min(1),
  summary: z.string(),
  stages: z.array(knowledgeStageSchema).min(1),
});

const indexSchema = z.object({
  version: z.string(),
  order: z.array(z.string()),
});

// ============================================================
// 数据加载
// ============================================================

/** 读取并解析 JSON 文件 */
function loadJson(filePath) {
  return JSON.parse(readFileSync(filePath, 'utf-8'));
}

/**
 * 扫描内容目录，构建 模块 -> slug 集合
 * @returns {{ docsByFolder: Map<string, Set<string>>, folderByModule: Map<string, string> }}
 *          已发布文档索引 + 模块 ID 到文件夹名的映射
 */
function scanContentDocs() {
  const docsByFolder = new Map();
  const folderByModule = new Map();
  const moduleDirs = readdirSync(CONTENT_DIR, { withFileTypes: true }).filter((e) =>
    e.isDirectory(),
  );
  for (const dir of moduleDirs) {
    const slugs = new Set();
    const dirPath = join(CONTENT_DIR, dir.name);
    for (const file of readdirSync(dirPath)) {
      if (extname(file) === '.md' || extname(file) === '.mdx') {
        slugs.add(basename(file, extname(file)));
      }
    }
    docsByFolder.set(dir.name, slugs);
    // 目录名格式：NNN-english-short，解析出模块 ID
    const match = dir.name.match(/^\d{3}-(.+)$/);
    if (match) folderByModule.set(match[1], dir.name);
  }
  return { docsByFolder, folderByModule };
}

/**
 * 读取模块元数据，返回 模块 ID -> 文件夹名 的映射
 */
function loadModuleFolders() {
  const modules = loadJson(MODULES_PATH).modules;
  return new Map(modules.map((m) => [m.id, m]));
}

// ============================================================
// 主流程
// ============================================================

/** 运行入口 */
function main() {
  const args = process.argv.slice(2);
  const writeReport = args.includes('--write-report');
  const templatesArg = args.indexOf('--templates');
  const templatesDir = templatesArg >= 0 ? args[templatesArg + 1] : null;

  const modules = loadModuleFolders();
  const { docsByFolder, folderByModule } = scanContentDocs();
  const index = indexSchema.parse(loadJson(join(MAP_DIR, 'index.json')));
  const moduleIds = new Set(modules.keys());

  let errors = 0;
  let warnings = 0;
  const rows = [];
  const gapRows = [];

  // 校验索引中的模块是否都存在地图文件
  for (const id of index.order) {
    if (!existsSync(join(MAP_DIR, `${id}.json`))) {
      console.error(`[FAIL] index.json 引用了不存在的地图文件: ${id}.json`);
      errors++;
    }
  }

  // 逐一校验并统计每门技术
  for (const moduleId of index.order) {
    const filePath = join(MAP_DIR, `${moduleId}.json`);
    if (!existsSync(filePath)) continue;

    let map;
    try {
      map = technologyMapSchema.parse(loadJson(filePath));
    } catch (err) {
      console.error(`[FAIL] ${moduleId}.json 结构校验失败:`, err.issues ?? err.message);
      errors++;
      continue;
    }

    if (!moduleIds.has(map.module)) {
      console.error(`[FAIL] ${moduleId}.json 引用了不存在的模块 ID: ${map.module}`);
      errors++;
    }

    const nodeIds = new Set();
    const stageIds = new Set();
    let docs = 0;
    let gaps = 0;

    for (const stage of map.stages) {
      if (stageIds.has(stage.id)) {
        console.error(`[FAIL] ${moduleId}.json 阶段 ID 重复: ${stage.id}`);
        errors++;
      }
      stageIds.add(stage.id);

      for (const node of stage.nodes) {
        if (nodeIds.has(node.id)) {
          console.error(`[FAIL] ${moduleId}.json 节点 ID 重复: ${node.id}`);
          errors++;
        }
        nodeIds.add(node.id);

        if (node.doc) {
          const folder = folderByModule.get(map.module);
          const exists = folder ? docsByFolder.get(folder)?.has(node.doc) : false;
          if (!exists) {
            console.error(
              `[FAIL] ${moduleId}.json 节点 ${node.id} 引用的文档不存在: ${node.doc}`,
            );
            errors++;
          } else {
            docs++;
          }
        } else {
          gaps++;
          gapRows.push({
            module: map.module,
            moduleTitle: modules.get(map.module)?.title ?? map.module,
            stage: stage.title,
            node,
          });
        }
      }
    }

    rows.push({
      module: map.module,
      title: modules.get(map.module)?.title ?? map.module,
      stages: map.stages.length,
      nodes: nodeIds.size,
      docs,
      gaps,
    });
    console.log(
      `[OK] ${map.module.padEnd(12)} 阶段 ${map.stages.length}  知识点 ${nodeIds.size}  已覆盖 ${docs}  缺口 ${gaps}`,
    );
  }

  // 检查内容目录中是否还有未收录进地图的模块（提示性）
  for (const moduleId of moduleIds) {
    if (!index.order.includes(moduleId)) {
      console.warn(`[WARN] 模块 ${moduleId} 尚未配置学习路径地图`);
      warnings++;
    }
  }

  // ============================================================
  // 输出报告
  // ============================================================
  const total = rows.reduce((acc, r) => acc + r.nodes, 0);
  const totalDocs = rows.reduce((acc, r) => acc + r.docs, 0);
  const totalGaps = rows.reduce((acc, r) => acc + r.gaps, 0);

  const report = [
    '# 学习路径缺口审计报告',
    '',
    `> 生成时间：${new Date().toISOString()}`,
    `> 技术数量：${rows.length} ｜ 知识点：${total} ｜ 已覆盖：${totalDocs} ｜ 缺口：${totalGaps}`,
    '',
    '## 总览',
    '',
    '| 技术 | 阶段 | 知识点 | 已覆盖 | 缺口 |',
    '| --- | --- | --- | --- | --- |',
    ...rows.map(
      (r) => `| ${r.title}（${r.module}） | ${r.stages} | ${r.nodes} | ${r.docs} | ${r.gaps} |`,
    ),
    '',
    '## 待补充文档清单',
    '',
    ...(gapRows.length
      ? gapRows.map(
          (g) =>
            `- [ ] **${g.moduleTitle}** ${g.node.title}（${g.stage}）｜建议难度：${g.node.difficulty ?? '未指定'}｜${g.node.desc ?? ''}`,
        )
      : ['- 当前没有缺口，全部知识点均已有文档。']),
    '',
  ].join('\n');

  if (writeReport) {
    mkdirSync(REPORT_DIR, { recursive: true });
    const reportPath = join(REPORT_DIR, 'learning-path-gap-report.md');
    writeFileSync(reportPath, report, 'utf-8');
    console.log(`\n报告已写入: ${reportPath}`);
  }

  // 生成缺口文档模板
  if (templatesDir && gapRows.length > 0) {
    mkdirSync(templatesDir, { recursive: true });
    for (const gap of gapRows) {
      const moduleInfo = modules.get(gap.module);
      const folderName = moduleInfo
        ? `${String(moduleInfo.folder_order).padStart(3, '0')}-${moduleInfo.id}`
        : gap.module;
      const fileName = `${gap.node.id}.md`;
      const template = [
        '---',
        `order: 0`,
        `title: ${gap.node.title}`,
        `module: ${gap.module}`,
        `category: '${folderName}'`,
        `difficulty: ${gap.node.difficulty ?? 'beginner'}`,
        `description: ${gap.node.desc ?? ''}`,
        `author: fanquanpp`,
        `updated: '2026-08-02'`,
        `related: []`,
        `prerequisites: []`,
        '---',
        '',
        `# ${gap.node.title}`,
        '',
        `> ${gap.node.desc ?? '待补充说明'}`,
        '',
        '## 一句话理解',
        '',
        '## 核心概念',
        '',
        '## 代码示例',
        '',
        '## 常见误区',
        '',
        '## 自测',
        '',
      ].join('\n');
      const target = join(templatesDir, gap.module, fileName);
      mkdirSync(join(templatesDir, gap.module), { recursive: true });
      if (!existsSync(target)) writeFileSync(target, template, 'utf-8');
    }
    console.log(`模板已写入: ${templatesDir}`);
  }

  console.log(`\n结果: ${errors} errors, ${warnings} warnings`);
  process.exit(errors > 0 ? 1 : 0);
}

main();
