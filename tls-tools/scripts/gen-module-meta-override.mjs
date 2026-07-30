/**
 * 模块元数据覆盖文件生成脚本
 * =============================================================================
 * 功能：
 *   读取 shd-shared/metadata/modules.json（三端共享模块元数据源），
 *   转换为 generate-manifest --modules-meta 期望的 ModuleMetaOverride[] 格式，
 *   输出到 shd-shared/metadata/module-meta-override.json。
 *
 * 字段映射：
 *   modules[].id            → english_short（模块英文简称，对应目录名）
 *   modules[].title         → name（模块中文显示名）
 *   modules[].icon          → icon（模块图标标识）
 *   modules[].description   → description（模块简介）
 *   categoryColors[categories[0]] → color（取首个分类的主题色）
 *
 * 使用方式：
 *   node tls-tools/scripts/gen-module-meta-override.mjs
 *
 * 输出：
 *   shd-shared/metadata/module-meta-override.json
 * =============================================================================
 */
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
/** FANDEX 仓库根目录（scripts/ → tls-tools/ → FANDEX/） */
const FANDEX_ROOT = resolve(__dirname, '..', '..');

/** 输入：三端共享模块元数据源 */
const INPUT_PATH = join(FANDEX_ROOT, 'shd-shared', 'metadata', 'modules.json');
/** 输出：generate-manifest 可消费的覆盖文件 */
const OUTPUT_PATH = join(FANDEX_ROOT, 'shd-shared', 'metadata', 'module-meta-override.json');

/**
 * 主函数：读取 modules.json，转换为 ModuleMetaOverride[]，写入输出文件
 */
function main() {
  console.log('[gen-meta-override] 读取模块元数据源:', INPUT_PATH);
  const raw = readFileSync(INPUT_PATH, 'utf-8');
  const data = JSON.parse(raw);

  if (!Array.isArray(data.modules)) {
    throw new Error('modules.json 结构异常：缺少 modules 数组');
  }

  /** 分类颜色映射表（categoryColors[categoryId] → hex） */
  const categoryColors = data.categoryColors || {};
  /** 分类中文标签映射（用于回退说明，当前未直接使用） */
  const categoryLabels = data.categoryLabels || {};

  /**
   * 转换单个模块条目
   * @param {object} m - modules.json 中的模块条目
   * @returns {object} ModuleMetaOverride 格式条目
   */
  const overrides = data.modules.map((m) => {
    /** 取首个分类作为主题色来源（模块可属多个分类，取主分类） */
    const primaryCategory = Array.isArray(m.categories) && m.categories.length > 0
      ? m.categories[0]
      : null;
    const color = primaryCategory ? categoryColors[primaryCategory] : undefined;

    /** 构造覆盖条目，undefined 字段在 JSON.stringify 时自动忽略 */
    const entry = {
      english_short: m.id,
      name: m.title,
    };
    if (m.icon) entry.icon = m.icon;
    if (color) entry.color = color;
    if (m.description) entry.description = m.description;
    return entry;
  });

  /** 写入输出文件（紧凑数组格式，保留可读性） */
  const json = JSON.stringify(overrides, null, 2);
  writeFileSync(OUTPUT_PATH, `${json}\n`, 'utf-8');

  console.log('[gen-meta-override] 转换完成');
  console.log(`[gen-meta-override]   模块数: ${overrides.length}`);
  console.log(`[gen-meta-override]   含 icon: ${overrides.filter((e) => e.icon).length}`);
  console.log(`[gen-meta-override]   含 color: ${overrides.filter((e) => e.color).length}`);
  console.log(`[gen-meta-override]   含 description: ${overrides.filter((e) => e.description).length}`);
  console.log(`[gen-meta-override]   输出路径: ${OUTPUT_PATH}`);
}

main();
