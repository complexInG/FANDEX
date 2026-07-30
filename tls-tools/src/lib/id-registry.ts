/**
 * ID 注册表管理模块
 *
 * 功能概述：
 * 维护 id-registry.json，提供 module_id 与 doc_id 的分配、查询、退役功能。
 * 分配规则：编号只增不复用，retired 后永久封存。
 *
 * ID 编码（去耦设计）：
 * - 模块 ID：M<NNN>（如 M001），不透明序号，不嵌入 english_short
 * - 文档 ID：D<NNNNN>（如 D00001），不透明序号，全局递增
 * - english_short / english_name 作为可变匹配字段独立存储，不参与 ID 构造
 * - 文档改名/模块改名时 ID 不变，仅更新匹配字段与 doc-id-map 映射
 *
 * 设计目的：
 * - 防止 ID 复用（核心约束）
 * - ID 与元数据解耦：重命名文件夹/文档不破坏 ID
 * - 工具链各模块（generate-manifest、allocate-id）通过此模块读写 id-registry
 *
 * 文件位置：
 * - id-registry.json 位于 cnt-content/full/_id-registry.json（内容层 full 目录，git 跟踪）
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { assertValidSchema } from './schema-loader';
import type { DocRecord, IdRegistry, ModuleRecord } from './types';

/** 当前模块所在目录 */
const __dirname = dirname(fileURLToPath(import.meta.url));

/** id-registry.json 默认路径（cnt-content/full/_id-registry.json） */
const DEFAULT_REGISTRY_PATH = resolve(__dirname, '..', '..', '..', 'cnt-content', 'full', '_id-registry.json');

/** 模块 ID 分配结果 */
export interface AllocatedModuleId {
  /** 分配的 module_id（M<NNN>） */
  module_id: string;
  /** 分配的序号（1-999） */
  sequence: number;
}

/** 文档 ID 分配结果 */
export interface AllocatedDocId {
  /** 分配的 doc_id（D<NNNNN>） */
  doc_id: string;
  /** 分配的全局序号（1-99999） */
  sequence: number;
}

/** 模块编号空间上限（含） */
const MODULE_SEQUENCE_MAX = 999;
/** 文档编号空间上限（含） */
const DOC_SEQUENCE_MAX = 99999;

/**
 * 加载 id-registry
 *
 * 输入：可选的注册表文件路径（默认 cnt-content/full/_id-registry.json）
 * 输出：IdRegistry 对象
 * 流程：
 * 1. 读取文件（不存在则返回空注册表）
 * 2. JSON 解析
 * 3. Schema 验证
 *
 * @param registryPath - 注册表文件路径（可选）
 * @returns IdRegistry 对象
 */
export function loadIdRegistry(registryPath: string = DEFAULT_REGISTRY_PATH): IdRegistry {
  if (!existsSync(registryPath)) {
    return createEmptyRegistry();
  }
  const content = readFileSync(registryPath, 'utf-8');
  const registry = JSON.parse(content) as IdRegistry;
  assertValidSchema('id-registry', registry, 'id-registry');
  return registry;
}

/**
 * 保存 id-registry
 *
 * 输入：IdRegistry 对象、可选的注册表文件路径
 * 输出：无（写入文件）
 * 流程：
 * 1. 更新 updated_at 时间戳与 next_*_sequence 计数器
 * 2. Schema 验证
 * 3. 写入文件（pretty JSON，2 空格缩进）
 *
 * @param registry - IdRegistry 对象
 * @param registryPath - 注册表文件路径（可选）
 */
export function saveIdRegistry(
  registry: IdRegistry,
  registryPath: string = DEFAULT_REGISTRY_PATH,
): void {
  /* 更新时间戳与计数器 */
  registry.updated_at = new Date().toISOString();
  registry.next_module_sequence = computeNextModuleSequence(registry);
  registry.next_doc_sequence = computeNextDocSequence(registry);

  /* Schema 验证 */
  assertValidSchema('id-registry', registry, 'id-registry');

  /* 确保目录存在 */
  const dir = dirname(registryPath);
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }

  /* 写入文件（pretty JSON，2 空格缩进，末尾换行） */
  const json = JSON.stringify(registry, null, 2);
  writeFileSync(registryPath, `${json}\n`, 'utf-8');
}

/**
 * 创建空注册表
 *
 * @returns 空 IdRegistry 对象
 */
function createEmptyRegistry(): IdRegistry {
  return {
    registry_version: '1.0.0',
    updated_at: new Date().toISOString(),
    next_module_sequence: 1,
    next_doc_sequence: 1,
    modules: [],
    docs: [],
  };
}

/**
 * 计算下一个待分配的模块序号
 *
 * 扫描所有已分配的模块序号，返回最小的未占用序号（自 1 起）。
 * 若所有序号（1-999）均已占用，返回 1000（表示编号空间耗尽）。
 *
 * @param registry - IdRegistry 对象
 * @returns 下一个待分配的模块序号（1-1000）
 */
function computeNextModuleSequence(registry: IdRegistry): number {
  const usedSequences = new Set(registry.modules.map((m) => m.sequence));
  for (let seq = 1; seq <= MODULE_SEQUENCE_MAX; seq++) {
    if (!usedSequences.has(seq)) {
      return seq;
    }
  }
  return MODULE_SEQUENCE_MAX + 1;
}

/**
 * 计算下一个待分配的文档序号
 *
 * 扫描所有已分配的文档序号，返回最小的未占用序号（自 1 起，全局递增）。
 * 若所有序号（1-99999）均已占用，返回 100000（表示编号空间耗尽）。
 *
 * @param registry - IdRegistry 对象
 * @returns 下一个待分配的文档序号（1-100000）
 */
function computeNextDocSequence(registry: IdRegistry): number {
  const usedSequences = new Set(registry.docs.map((d) => d.sequence));
  for (let seq = 1; seq <= DOC_SEQUENCE_MAX; seq++) {
    if (!usedSequences.has(seq)) {
      return seq;
    }
  }
  return DOC_SEQUENCE_MAX + 1;
}

/**
 * 分配新 module_id
 *
 * 输入：IdRegistry 对象、模块英文简称、模块显示名称、文件夹位置序号
 * 输出：分配结果（含 module_id 与 sequence）
 * 流程：
 * 1. 校验 english_short 格式（小写字母开头，允许字母数字与连字符）
 * 2. 校验 english_short 未被占用（active 状态）
 * 3. 扫描最小未占用 sequence（1-999）
 * 4. 构造 module_id 为 M<NNN>（不嵌入 english_short）
 * 5. 构造 ModuleRecord（含 folder_order）并加入 registry.modules
 *
 * @param registry - IdRegistry 对象（会被修改）
 * @param englishShort - 模块英文简称（小写，允许连字符）
 * @param name - 模块显示名称（中文）
 * @param folderOrder - 文件夹位置序号（1-999，来自文件夹 NNN 前缀）
 * @returns 分配结果
 * @throws {Error} english_short 格式错误或已被占用，或编号空间耗尽
 */
export function allocateModuleId(
  registry: IdRegistry,
  englishShort: string,
  name: string,
  folderOrder: number,
): AllocatedModuleId {
  /* 校验 english_short 格式（允许连字符，对齐 naming.config） */
  if (!/^[a-z][a-z0-9-]*$/.test(englishShort)) {
    throw new Error(
      `[id-registry] english_short 格式错误: ${englishShort}（需小写字母开头，允许字母数字与连字符）`,
    );
  }

  /* 校验 folder_order 范围 */
  if (!Number.isInteger(folderOrder) || folderOrder < 1 || folderOrder > 999) {
    throw new Error(
      `[id-registry] folder_order 范围错误: ${folderOrder}（需 1-999 整数）`,
    );
  }

  /* 校验 english_short 未被 active 模块占用 */
  const existingActive = registry.modules.find(
    (m) => m.english_short === englishShort && m.status === 'active',
  );
  if (existingActive) {
    throw new Error(
      `[id-registry] english_short 已被占用: ${englishShort}（当前归属 ${existingActive.module_id}）`,
    );
  }

  /* 扫描最小未占用 sequence（1-999） */
  const usedSequences = new Set(registry.modules.map((m) => m.sequence));
  let sequence = -1;
  for (let seq = 1; seq <= MODULE_SEQUENCE_MAX; seq++) {
    if (!usedSequences.has(seq)) {
      sequence = seq;
      break;
    }
  }
  if (sequence === -1) {
    throw new Error('[id-registry] 模块编号空间耗尽（1-999 均已分配）');
  }

  /* 构造 module_id：M<NNN>，不嵌入 english_short */
  const moduleId = `M${String(sequence).padStart(3, '0')}`;

  /* 构造 ModuleRecord 并加入 registry */
  const record: ModuleRecord = {
    module_id: moduleId,
    english_short: englishShort,
    sequence,
    folder_order: folderOrder,
    name,
    allocated_at: new Date().toISOString(),
    status: 'active',
  };
  registry.modules.push(record);

  return { module_id: moduleId, sequence };
}

/**
 * 分配新 doc_id
 *
 * 输入：IdRegistry 对象、所属 module_id、文档标题、文档位置序号、文档英文名
 * 输出：分配结果（含 doc_id 与全局 sequence）
 * 流程：
 * 1. 校验 module_id 存在且 active
 * 2. 扫描最小未占用全局 doc sequence（1-99999）
 * 3. 构造 doc_id 为 D<NNNNN>（不嵌入 english_short）
 * 4. 构造 DocRecord（含 doc_order、english_name）并加入 registry.docs
 *
 * @param registry - IdRegistry 对象（会被修改）
 * @param moduleId - 所属模块 ID（M<NNN>）
 * @param title - 文档标题
 * @param docOrder - 文档在模块内的位置序号（1-999，来自文件名 NNN 前缀）
 * @param englishName - 文档英文名（PascalCase，来自文件名）
 * @returns 分配结果
 * @throws {Error} module_id 不存在、非 active，或文档编号空间耗尽
 */
export function allocateDocId(
  registry: IdRegistry,
  moduleId: string,
  title: string,
  docOrder: number,
  englishName: string,
): AllocatedDocId {
  /* 查找模块 */
  const module = registry.modules.find((m) => m.module_id === moduleId);
  if (!module) {
    throw new Error(`[id-registry] module_id 不存在: ${moduleId}`);
  }
  if (module.status !== 'active') {
    throw new Error(`[id-registry] module_id 非 active: ${moduleId}（当前 ${module.status}）`);
  }

  /* 校验 doc_order 范围 */
  if (!Number.isInteger(docOrder) || docOrder < 1 || docOrder > 999) {
    throw new Error(
      `[id-registry] doc_order 范围错误: ${docOrder}（需 1-999 整数）`,
    );
  }

  /* 校验 english_name 非空 */
  if (!englishName || !/^[A-Za-z][A-Za-z0-9-]*$/.test(englishName)) {
    throw new Error(
      `[id-registry] english_name 格式错误: ${englishName}（需字母开头，允许字母数字与连字符）`,
    );
  }

  /* 扫描最小未占用全局 doc sequence（1-99999） */
  const usedDocSequences = new Set(registry.docs.map((d) => d.sequence));
  let sequence = -1;
  for (let seq = 1; seq <= DOC_SEQUENCE_MAX; seq++) {
    if (!usedDocSequences.has(seq)) {
      sequence = seq;
      break;
    }
  }
  if (sequence === -1) {
    throw new Error(`[id-registry] 文档编号空间耗尽（1-99999 均已分配）`);
  }

  /* 构造 doc_id：D<NNNNN>，不嵌入 english_short */
  const docId = `D${String(sequence).padStart(5, '0')}`;

  /* 构造 DocRecord 并加入 registry */
  const record: DocRecord = {
    doc_id: docId,
    module_id: moduleId,
    sequence,
    doc_order: docOrder,
    english_name: englishName,
    title,
    allocated_at: new Date().toISOString(),
    status: 'active',
  };
  registry.docs.push(record);

  return { doc_id: docId, sequence };
}

/**
 * 退役 module_id
 *
 * 输入：IdRegistry 对象、module_id
 * 输出：无（修改 registry）
 * 流程：
 * 1. 查找模块记录
 * 2. 校验当前状态为 active
 * 3. 更新状态为 retired，记录 retired_at
 * 4. 同时退役此模块下所有 active 文档
 *
 * @param registry - IdRegistry 对象（会被修改）
 * @param moduleId - 待退役的 module_id
 * @throws {Error} module_id 不存在或已 retired
 */
export function retireModuleId(registry: IdRegistry, moduleId: string): void {
  const module = registry.modules.find((m) => m.module_id === moduleId);
  if (!module) {
    throw new Error(`[id-registry] module_id 不存在: ${moduleId}`);
  }
  if (module.status !== 'active') {
    throw new Error(`[id-registry] module_id 已 retired: ${moduleId}`);
  }
  module.status = 'retired';
  module.retired_at = new Date().toISOString();

  /* 同时退役此模块下所有 active 文档 */
  for (const doc of registry.docs) {
    if (doc.module_id === moduleId && doc.status === 'active') {
      doc.status = 'retired';
      doc.retired_at = new Date().toISOString();
    }
  }
}

/**
 * 退役 doc_id
 *
 * 输入：IdRegistry 对象、doc_id
 * 输出：无（修改 registry）
 * 流程：
 * 1. 查找文档记录
 * 2. 校验当前状态为 active
 * 3. 更新状态为 retired，记录 retired_at
 *
 * @param registry - IdRegistry 对象（会被修改）
 * @param docId - 待退役的 doc_id
 * @throws {Error} doc_id 不存在或已 retired
 */
export function retireDocId(registry: IdRegistry, docId: string): void {
  const doc = registry.docs.find((d) => d.doc_id === docId);
  if (!doc) {
    throw new Error(`[id-registry] doc_id 不存在: ${docId}`);
  }
  if (doc.status !== 'active') {
    throw new Error(`[id-registry] doc_id 已 retired: ${docId}`);
  }
  doc.status = 'retired';
  doc.retired_at = new Date().toISOString();
}

/**
 * 查询 module_id 是否存在（含 active 与 retired）
 *
 * @param registry - IdRegistry 对象
 * @param moduleId - 待查询的 module_id
 * @returns 是否存在
 */
export function moduleExists(registry: IdRegistry, moduleId: string): boolean {
  return registry.modules.some((m) => m.module_id === moduleId);
}

/**
 * 查询 doc_id 是否存在（含 active 与 retired）
 *
 * @param registry - IdRegistry 对象
 * @param docId - 待查询的 doc_id
 * @returns 是否存在
 */
export function docExists(registry: IdRegistry, docId: string): boolean {
  return registry.docs.some((d) => d.doc_id === docId);
}

/**
 * 查询 module_id 是否活跃
 *
 * @param registry - IdRegistry 对象
 * @param moduleId - 待查询的 module_id
 * @returns 是否活跃（true 表示 active）
 */
export function isModuleActive(registry: IdRegistry, moduleId: string): boolean {
  const module = registry.modules.find((m) => m.module_id === moduleId);
  return module?.status === 'active';
}

/**
 * 查询 doc_id 是否活跃
 *
 * @param registry - IdRegistry 对象
 * @param docId - 待查询的 doc_id
 * @returns 是否活跃（true 表示 active）
 */
export function isDocActive(registry: IdRegistry, docId: string): boolean {
  const doc = registry.docs.find((d) => d.doc_id === docId);
  return doc?.status === 'active';
}

/**
 * 获取模块记录
 *
 * @param registry - IdRegistry 对象
 * @param moduleId - 模块 ID
 * @returns 模块记录（不存在返回 undefined）
 */
export function getModuleRecord(registry: IdRegistry, moduleId: string): ModuleRecord | undefined {
  return registry.modules.find((m) => m.module_id === moduleId);
}

/**
 * 获取文档记录
 *
 * @param registry - IdRegistry 对象
 * @param docId - 文档 ID
 * @returns 文档记录（不存在返回 undefined）
 */
export function getDocRecord(registry: IdRegistry, docId: string): DocRecord | undefined {
  return registry.docs.find((d) => d.doc_id === docId);
}

/**
 * 获取 id-registry.json 默认路径
 *
 * @returns 默认路径
 */
export function getDefaultRegistryPath(): string {
  return DEFAULT_REGISTRY_PATH;
}
