import { defineCollection } from 'astro:content';
// Astro 7 同时弃用了从 'astro:content' 与 'astro:schema' 导出 z 的方式（ts(6385) 'z' is deprecated）。
// 改为从 'zod' 直接导入（zod 4.x 已作为 astro 的传递依赖存在于 node_modules），
// 并在 package.json 显式声明依赖以锁定版本，避免传递依赖变更导致构建失败。
// 依据：https://docs.astro.build/en/upgrade-guides/v7/ + npm list zod 验证
import { z } from 'zod';
import { glob } from 'astro/loaders';

/**
 * FANDEX 内容 Collection Schema 定义
 *
 * Astro 7 迁移说明：
 * - 原 src/content/config.ts 已迁移至 src/content.config.ts（Astro 6+ 要求）
 * - type: 'content' 已替换为 glob loader（Astro 6+ 移除 legacy content collections）
 * - glob pattern 同时匹配 .md 与 .mdx 文件
 *
 * Phase 2.0 结构化字段严格化：
 * - references：参考文献（ACM Reference Format）
 * - etymology：词源条目
 * - estimatedReadingTime：预估阅读时长（分钟）
 * - lastReviewed：最后审阅日期
 * - reviewer：审阅人
 *
 * 设计原则：
 * 1. 存量数据已迁移归一化（references 两代格式合并、etymology 统一为数组），
 *    因此 references/etymology 恢复严格 schema 校验；
 * 2. learningObjectives / exercises 字段已随内容清理移除（存量 0 使用），
 *    schema 不再为已废弃字段预留宽容；
 * 3. 保留 quiz 字段（向后兼容，QuizBlock 仍消费该字段）；
 * 4. 新增字段必须同时通过本 schema 与 content-audit 的覆盖审计，禁止再引入 z.any()。
 */

// ============================================================
// 共享子 Schema 定义
// ============================================================

/**
 * 参考文献类型枚举
 * 用于 references 字段，标识参考文献的载体形式
 */
const ReferenceTypeSchema = z.enum([
  'book',
  'journal',
  'conference',
  'technical-report',
  'standard',
  'website',
  'documentation',
  'video',
  'course',
]);

/**
 * 参考文献条目 Schema
 * 遵循 ACM Reference Format 的字段划分
 *
 * volume/issue 原设计为 number，但学术文献中这些字段
 * 经常使用字符串（如 issue: "OOPSLA"、"Special Issue"）。
 * 临时改为 union(number, string) 以兼容存量数据。
 *
 * 存量数据中的历史键（isbn / publisher / edition / pagesNote / number）在
 * 数据迁移时被保留为可选字段，避免恢复严格校验后静默丢字段；
 * note 字段用于保存旧版纯文本引用（字符串条目）的原始全文，供追溯审计。
 */
export const ReferenceSchema = z.object({
  type: ReferenceTypeSchema,
  authors: z.array(z.string()).default([]),
  year: z.number(),
  title: z.string(),
  venue: z.string().default(''),
  volume: z.union([z.number(), z.string()]).optional(),
  issue: z.union([z.number(), z.string()]).optional(),
  pages: z.string().optional(),
  pagesNote: z.string().optional(),
  doi: z.string().optional(),
  url: z.string().optional(),
  accessedDate: z.coerce.date().optional(),
  version: z.string().optional(),
  // ISBN 在部分存量文档中未加引号，YAML 会解析为数字，故用 coerce 统一为字符串
  isbn: z.coerce.string().optional(),
  publisher: z.string().optional(),
  edition: z.string().optional(),
  number: z.union([z.number(), z.string()]).optional(),
  note: z.string().optional(),
});

/**
 * 词源条目 Schema
 * 用于记录计算机术语的英文原词与词源说明
 * 存量数据中的单对象形态已迁移为数组，english 缺失条目已按词源补全。
 */
export const EtymologyEntrySchema = z.object({
  term: z.string(),
  english: z.string(),
  origin: z.string(),
});

// ============================================================
// docs Collection
// ============================================================

// （仓库整理后路径变更）：
// 原：app-web/src/content/docs（已删除）
// 新：cnt-content/full（单仓库根目录下的统一内容源）
// base 路径相对于 content.config.ts 所在的 app-web/src/ 目录
const docs = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: '../cnt-content/full',
    // 内容量较大（2000+ 篇）：延迟渲染避免 data store 序列化超限
    // render(entry) 仍会在页面构建时按需渲染，行为不受影响
    deferRender: true,
    generateId: ({ entry }) => entry.replace(/[#\\]/g, '-'),
  }),
  schema: z.object({
    // === 现有字段（保持不变，向后兼容） ===
    title: z.string(),
    module: z.string(),
    category: z.string().optional(),
    tags: z.array(z.string()).default([]),
    difficulty: z.enum(['beginner', 'intermediate', 'advanced']).optional(),
    order: z.number().default(0),
    created: z.coerce.date().optional(),
    updated: z.coerce.date().optional(),
    author: z.string().default('fanquanpp'),
    description: z.string().optional(),
    readingTime: z.number().optional(),
    related: z.array(z.string()).default([]),
    prerequisites: z.array(z.string()).default([]),
    quiz: z
      .array(
        z.union([
          z.object({
            type: z.literal('fill'),
            question: z.string(),
            answer: z.string(),
            hint: z.string().optional(),
          }),
          z.object({
            type: z.literal('choice'),
            question: z.string(),
            options: z.array(z.string()),
            answer: z.number(),
            explanation: z.string().optional(),
          }),
          z.object({
            type: z.literal('fix'),
            question: z.string(),
            code: z.string().optional(),
            answer: z.string(),
            explanation: z.string().optional(),
          }),
        ])
      )
      .default([]),
    // === 结构化字段（Phase 2.0，严格校验） ===
    // references / etymology 已完成存量归一化迁移（2026-08-01），
    // 此处直接使用严格 schema，任何新增字段缺失或格式漂移都会在构建期报错。
    references: z.array(ReferenceSchema).default([]).describe('参考文献列表，遵循 ACM Reference Format'),
    etymology: z.array(EtymologyEntrySchema).default([]).describe('词源条目，计算机术语的英文原词与词源'),
    estimatedReadingTime: z.number().optional().describe('预估阅读时长（分钟）'),
    lastReviewed: z.coerce.date().optional().describe('最后审阅日期'),
    reviewer: z.string().optional().describe('审阅人'),
  }),
});

export const collections = { docs };
