/**
 * 内容扫描模块
 *
 * 功能概述：
 * 扫描 cnt-content/full/ 或 cnt-content/mobile/ 目录，提取模块与文档的物理元数据。
 * 仅负责文件层面的扫描与哈希计算，不涉及 ID 分配（ID 由 id-registry 管理）。
 *
 * 命名解析：
 * 通过 NamingStrategy 策略接口解析文件夹与文档名，正则模式由 naming.config.json
 * 集中配置，消除硬编码。修改命名规则只需调整配置文件，无需改动扫描器代码。
 *
 * 输出结构：
 * - 扫描结果按目录组织，每个子目录对应一个模块
 * - 每个模块下的 .md 文件对应一篇文档
 * - 模块元数据：english_short、folder_order、name、docs
 * - 文档元数据：title、english_name、doc_order、source_path、sha256、size、updated_at
 *
 * 与 generate-manifest 的协作：
 * - content-scanner 输出物理扫描结果
 * - generate-manifest 结合 id-registry 将物理结果映射为带 ID 的 manifest
 * - 映射规则：english_short 匹配 id-registry 中的模块，source_path 匹配 doc-id-map
 */

import { createHash } from 'node:crypto';
import { readFile, stat, readdir } from 'node:fs/promises';
import { readFileSync, existsSync } from 'node:fs';
import { join, relative, sep, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import fg from 'fast-glob';

/** 当前模块所在目录 */
const __dirname = dirname(fileURLToPath(import.meta.url));

/** naming.config.json 默认路径（shd-shared/metadata/naming.config.json） */
const DEFAULT_NAMING_CONFIG_PATH = resolve(
  __dirname,
  '..',
  '..',
  '..',
  'shd-shared',
  'metadata',
  'naming.config.json',
);

/** 命名配置：从 naming.config.json 加载的模式定义 */
export interface NamingConfig {
  config_version: string;
  folder: {
    pattern: string;
    groups: { order: number; english_short: number };
    order_min: number;
    order_max: number;
  };
  doc: {
    pattern: string;
    groups: { order: number; english_name: number };
    order_min: number;
    order_max: number;
  };
  english_short_pattern: { pattern: string };
  english_name_pattern: { pattern: string };
}

/** 命名策略接口：解析文件夹与文档名，提取序号与英文标识 */
export interface NamingStrategy {
  /** 解析文件夹名，返回 folder_order 与 english_short；不匹配返回 null */
  parseFolder(name: string): { folder_order: number; english_short: string } | null;
  /** 解析文档文件名，返回 doc_order 与 english_name；不匹配返回 null */
  parseDoc(fileName: string): { doc_order: number; english_name: string } | null;
}

/**
 * 可配置命名策略
 *
 * 依据 NamingConfig 的正则模式解析命名，所有模式来自配置文件，无硬编码。
 * 通过构造函数注入配置，便于测试与替换。
 */
export class ConfigurableNamingStrategy implements NamingStrategy {
  private readonly folderRegex: RegExp;
  private readonly docRegex: RegExp;

  constructor(private readonly config: NamingConfig) {
    this.folderRegex = new RegExp(config.folder.pattern);
    this.docRegex = new RegExp(config.doc.pattern);
  }

  parseFolder(name: string): { folder_order: number; english_short: string } | null {
    const m = this.folderRegex.exec(name);
    if (!m) {
      return null;
    }
    const order = parseInt(m[this.config.folder.groups.order]!, 10);
    const englishShort = m[this.config.folder.groups.english_short]!;
    if (!Number.isFinite(order) || !englishShort) {
      return null;
    }
    return { folder_order: order, english_short: englishShort };
  }

  parseDoc(fileName: string): { doc_order: number; english_name: string } | null {
    const m = this.docRegex.exec(fileName);
    if (!m) {
      return null;
    }
    const order = parseInt(m[this.config.doc.groups.order]!, 10);
    const englishName = m[this.config.doc.groups.english_name]!;
    if (!Number.isFinite(order) || !englishName) {
      return null;
    }
    return { doc_order: order, english_name: englishName };
  }
}

/**
 * 加载命名配置
 *
 * 输入：可选的配置文件路径（默认 shd-shared/metadata/naming.config.json）
 * 输出：NamingConfig 对象
 * 流程：读取 JSON → 基本校验 → 返回
 *
 * @param configPath - 配置文件路径（可选）
 * @returns NamingConfig 对象
 * @throws {Error} 配置文件不存在或解析失败
 */
export function loadNamingConfig(configPath: string = DEFAULT_NAMING_CONFIG_PATH): NamingConfig {
  if (!existsSync(configPath)) {
    throw new Error(`[content-scanner] naming.config.json 不存在: ${configPath}`);
  }
  const content = readFileSync(configPath, 'utf-8');
  const config = JSON.parse(content) as NamingConfig;
  if (!config.folder?.pattern || !config.doc?.pattern) {
    throw new Error('[content-scanner] naming.config.json 缺少 folder.pattern 或 doc.pattern');
  }
  return config;
}

/** 扫描出的文档元数据（不含 ID） */
export interface ScannedDoc {
  /** 文档标题（取 frontmatter title 或 english_name） */
  title: string;
  /** 文档英文名（来自文件名 PascalCase 部分） */
  english_name: string;
  /** 文档在模块内的位置序号（来自文件名 NNN 前缀） */
  doc_order: number;
  /** 文档相对路径（相对于 cnt-content/full/ 或 cnt-content/mobile/） */
  source_path: string;
  /** 文档文件内容的 SHA-256 哈希值（小写 hex） */
  sha256: string;
  /** 文档文件大小（字节） */
  size: number;
  /** 文档最近更新时间（ISO 8601 UTC，取文件 mtime） */
  updated_at: string;
  /** 文档 frontmatter 中的 tags（可选） */
  tags?: string[];
  /** 文档 frontmatter 中的 compat_version（可选） */
  compat_version?: string;
}

/** 扫描出的模块元数据（不含 ID） */
export interface ScannedModule {
  /** 模块英文简称（小写，来自文件夹名 english_short 部分） */
  english_short: string;
  /** 模块文件夹位置序号（来自文件夹名 NNN 前缀） */
  folder_order: number;
  /** 模块显示名称（默认取 english_short，可由 modules.json 覆盖） */
  name: string;
  /** 模块下的文档列表 */
  docs: ScannedDoc[];
}

/** 扫描结果 */
export interface ScanResult {
  /** 内容根目录绝对路径 */
  content_root: string;
  /** 扫描的模块列表（按 folder_order 升序） */
  modules: ScannedModule[];
  /** 未匹配命名规则的条目警告（迁移期用于发现遗漏） */
  warnings: string[];
}

/**
 * 扫描内容目录
 *
 * 输入：内容目录绝对路径、可选命名配置路径
 * 输出：ScanResult（含所有模块与文档的物理元数据）
 * 流程：
 * 1. 加载命名配置并构造策略
 * 2. 使用 fast-glob 扫描所有 .md 文件
 * 3. 按一级目录分组，用策略解析文件夹与文档名
 * 4. 对每个文件计算 sha256、size、mtime
 * 5. 解析 frontmatter 提取 title、tags、compat_version
 * 6. 模块按 folder_order 排序，文档按 doc_order 排序
 *
 * @param contentDir - 内容目录绝对路径
 * @param namingConfigPath - 命名配置文件路径（可选，默认 shd-shared/metadata/naming.config.json）
 * @returns 扫描结果
 */
export async function scanContentDir(
  contentDir: string,
  namingConfigPath: string = DEFAULT_NAMING_CONFIG_PATH,
): Promise<ScanResult> {
  const config = loadNamingConfig(namingConfigPath);
  const strategy = new ConfigurableNamingStrategy(config);
  const warnings: string[] = [];

  /* 扫描所有 .md 文件（排除 _ 开头的目录与文件，如 _drafts、_template、_id-registry.json；
     排除 MERGED 合集 —— 合集由各模块文档拼接生成，不参与 ID 分配，与 app-Android-new 生成器约定一致） */
  const mdFiles = await fg.glob('**/*.md', {
    cwd: contentDir,
    onlyFiles: true,
    ignore: ['_*', '_*/**', 'node_modules/**', '**/*-MERGED.md'],
    dot: false,
  });

  /* 按一级目录分组 */
  const moduleMap = new Map<string, ScannedModule>();

  for (const relativePath of mdFiles) {
    const pathParts = relativePath.split('/');
    if (pathParts.length < 2) {
      /* 根目录下的 .md 文件不属于任何模块，跳过 */
      continue;
    }
    const folderName = pathParts[0]!;
    const fileName = pathParts[pathParts.length - 1]!;

    /* 用策略解析文件夹名 */
    const folderParsed = strategy.parseFolder(folderName);
    if (!folderParsed) {
      warnings.push(`文件夹未匹配命名规则，跳过: ${folderName}/${fileName}`);
      continue;
    }

    /* 用策略解析文档名 */
    const docParsed = strategy.parseDoc(fileName);
    if (!docParsed) {
      warnings.push(`文档未匹配命名规则，跳过: ${relativePath}`);
      continue;
    }

    /* 获取或创建模块 */
    let module = moduleMap.get(folderParsed.english_short);
    if (!module) {
      module = {
        english_short: folderParsed.english_short,
        folder_order: folderParsed.folder_order,
        name: folderParsed.english_short,
        docs: [],
      };
      moduleMap.set(folderParsed.english_short, module);
    }

    /* 扫描文件元数据 */
    const absolutePath = join(contentDir, relativePath);
    const doc = await scanDocFile(
      absolutePath,
      relativePath,
      docParsed.doc_order,
      docParsed.english_name,
    );
    module.docs.push(doc);
  }

  /* 转换为数组并按 folder_order 排序；文档按 doc_order 排序 */
  const modules = Array.from(moduleMap.values()).sort(
    (a, b) => a.folder_order - b.folder_order,
  );
  for (const m of modules) {
    m.docs.sort((a, b) => a.doc_order - b.doc_order);
  }

  return {
    content_root: contentDir,
    modules,
    warnings,
  };
}

/**
 * 扫描单个文档文件
 *
 * 输入：文件绝对路径、相对路径、doc_order、english_name
 * 输出：ScannedDoc（含 sha256、size、updated_at、title 等）
 * 流程：
 * 1. 读取文件内容
 * 2. 计算 sha256
 * 3. 获取文件 stat（size、mtime）
 * 4. 解析 frontmatter 提取 title、tags、compat_version
 *
 * @param absolutePath - 文件绝对路径
 * @param relativePath - 文档相对路径（相对于 cnt-content 目录）
 * @param docOrder - 文档位置序号（来自文件名前缀）
 * @param englishName - 文档英文名（来自文件名 PascalCase 部分）
 * @returns 文档元数据
 */
async function scanDocFile(
  absolutePath: string,
  relativePath: string,
  docOrder: number,
  englishName: string,
): Promise<ScannedDoc> {
  const content = await readFile(absolutePath);
  const fileStat = await stat(absolutePath);

  /* 计算 sha256 */
  const sha256 = createHash('sha256').update(content).digest('hex');

  /* 解析 frontmatter */
  const contentStr = content.toString('utf-8');
  const frontmatter = parseFrontmatter(contentStr);

  /* 提取 title：优先 frontmatter.title，其次 english_name */
  const title = frontmatter.title || englishName;

  /* 标准化路径分隔符（统一使用 / ） */
  const normalizedPath = relativePath.split(sep).join('/');

  return {
    title,
    english_name: englishName,
    doc_order: docOrder,
    source_path: normalizedPath,
    sha256,
    size: fileStat.size,
    updated_at: fileStat.mtime.toISOString(),
    tags: frontmatter.tags,
    compat_version: frontmatter.compat_version,
  };
}

/**
 * 解析 Markdown frontmatter
 *
 * 输入：Markdown 文件内容
 * 输出：frontmatter 字段对象（title、tags、compat_version 等）
 * 流程：简易 YAML 解析，仅支持键值对与数组
 *
 * @param content - Markdown 文件内容
 * @returns frontmatter 字段对象
 */
function parseFrontmatter(content: string): {
  title?: string;
  tags?: string[];
  compat_version?: string;
  [key: string]: unknown;
} {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match?.[1]) {
    return {};
  }
  const raw = match[1];
  const data: { title?: string; tags?: string[]; compat_version?: string; [key: string]: unknown } = {};

  let currentKey: string | null = null;
  let inArray = false;

  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();

    /* 数组项 */
    if (inArray && currentKey && trimmed.startsWith('- ')) {
      const item = trimmed.slice(2).trim().replace(/^['"]|['"]$/g, '');
      const arr = data[currentKey];
      if (Array.isArray(arr)) {
        arr.push(item);
      }
      continue;
    }

    /* 退出数组 */
    if (inArray && !trimmed.startsWith('- ') && trimmed !== '') {
      inArray = false;
      currentKey = null;
    }

    /* 键值对 */
    const kvMatch = trimmed.match(/^(\w[\w-]*):\s*(.*)$/);
    if (kvMatch) {
      const k = kvMatch[1]!;
      const v = kvMatch[2]!.trim();

      if (v === '') {
        /* 可能是数组起始 */
        data[k] = [];
        currentKey = k;
        inArray = true;
      } else {
        /* 普通键值对 */
        const cleaned = v.replace(/^['"]|['"]$/g, '');
        if (cleaned) {
          data[k] = cleaned;
        }
        currentKey = k;
        inArray = false;
      }
    }
  }

  return data;
}
