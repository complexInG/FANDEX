/**
 * 文档服务模块
 * 封装 docs Content Collection 的所有查询、排序、分组、过滤逻辑
 * 作为 UI 层与 Data 层（getCollection）之间的唯一桥梁
 *
 * 设计原则：
 * - 所有 getCollection 调用仅限本模块内部
 * - 所有 async 函数均通过 try-catch 包裹，异常时返回安全默认值
 * - 类型从 Content Schema 推导，不手动重复定义
 *
 * 偏差报备（dev 模式 OOM 优化）：
 * - getDocStats() 原实现调用 getCollection('docs') 全量加载 2003 篇文档，
 *   dev 模式下导致 12GB 堆内存 OOM 崩溃
 * - 改为读取预构建的 JSON 缓存（scripts/build-stats.mjs 生成），
 *   零文档内容加载，dev 模式下首页不再 OOM
 * - build 模式下仍可使用原逻辑（但 JSON 缓存已足够，且性能更优）
 */
import { getCollection, type CollectionEntry } from 'astro:content';
import { docSlug } from '@/lib/modules';
// 阅读时长估算为纯函数工具，从 reading-time.ts 引入避免重复定义
import { computeReadingTime } from '@/lib/reading-time';
// 预构建的文档统计缓存（由 scripts/build-stats.mjs 生成，避免 dev 模式 OOM）
import docStatsCache from '@/data/doc-stats.json';

/** 文档条目类型（从 Content Schema 推导） */
type DocEntry = CollectionEntry<'docs'>;

/** 文档导航结果：上下篇文档 */
interface DocNavigation {
  /** 上一篇文档（按 order 排序），首篇时为 null */
  prev: DocEntry | null;
  /** 下一篇文档（按 order 排序），末篇时为 null */
  next: DocEntry | null;
}

/** 文档统计数据 */
interface DocStats {
  /** 文档总数 */
  totalDocs: number;
  /** 涉及的模块数 */
  totalModules: number;
  /** 涉及的分类数 */
  totalCategories: number;
  /** 标签总数（去重） */
  totalTags: number;
}

/**
 * 获取全部文档，按模块名和 order 顺序排序
 * 排序规则：先按 module 字段字母序，再按 order 升序
 * @returns 排序后的文档数组；异常时返回空数组
 */
export async function getAllDocs(): Promise<DocEntry[]> {
  try {
    const docs = await getCollection('docs');
    return docs.sort((a, b) => {
      if (a.data.module !== b.data.module) {
        return a.data.module.localeCompare(b.data.module);
      }
      return (a.data.order || 0) - (b.data.order || 0);
    });
  } catch {
    return [];
  }
}

/**
 * 获取指定模块的所有文档，按 order 升序排序
 * @param moduleId - 模块 ID
 * @returns 排序后的文档数组；异常时返回空数组
 */
export async function getDocsByModule(moduleId: string): Promise<DocEntry[]> {
  try {
    const docs = await getCollection('docs', ({ data }) => data.module === moduleId);
    return docs.sort((a, b) => (a.data.order || 0) - (b.data.order || 0));
  } catch {
    return [];
  }
}

/**
 * 获取指定模块下指定 slug 的文档
 * @param moduleId - 模块 ID
 * @param slug - 文档 slug（文件名去除 .md 后缀）
 * @returns 匹配的文档；未找到或异常时返回 null
 */
export async function getDocBySlug(moduleId: string, slug: string): Promise<DocEntry | null> {
  try {
    const docs = await getDocsByModule(moduleId);
    return docs.find((doc) => docSlug(doc.id) === slug) || null;
  } catch {
    return null;
  }
}

/**
 * 获取文档的上下篇导航信息
 * 根据当前文档在模块文档列表（按 order 排序）中的位置计算前后文档
 * @param moduleId - 模块 ID
 * @param slug - 当前文档 slug
 * @returns 包含 prev 和 next 的导航对象；异常或未找到时返回 { prev: null, next: null }
 */
export async function getDocNavigation(moduleId: string, slug: string): Promise<DocNavigation> {
  try {
    const docs = await getDocsByModule(moduleId);
    const currentIndex = docs.findIndex((doc) => docSlug(doc.id) === slug);
    if (currentIndex < 0) return { prev: null, next: null };
    // 使用 ?? null 将可能的 undefined（来自 noUncheckedIndexedAccess）收窄为 null
    // 保证返回类型与 DocNavigation 接口（DocEntry | null）严格匹配
    const prev = currentIndex > 0 ? (docs[currentIndex - 1] ?? null) : null;
    const next = currentIndex < docs.length - 1 ? (docs[currentIndex + 1] ?? null) : null;
    return { prev, next };
  } catch {
    return { prev: null, next: null };
  }
}

/**
 * 获取文档统计数据
 * 统计文档总数、模块数、分类数和标签数
 *
 * 优化说明（dev 模式 OOM 修复）：
 * - 原实现调用 getCollection('docs') 全量加载 2003 篇文档，
 *   dev 模式下导致 12GB 堆内存 OOM
 * - 改为读取预构建的 JSON 缓存（scripts/build-stats.mjs 生成），
 *   零文档内容加载，dev 模式下首页不再 OOM
 * - JSON 缓存由 dev / build 脚本启动前自动运行 build-stats.mjs 生成
 *
 * @returns 文档统计对象；缓存不可用时返回零值
 */
export async function getDocStats(): Promise<DocStats> {
  try {
    // 直接返回预构建的统计缓存，避免 getCollection('docs') 全量加载
    return {
      totalDocs: docStatsCache.totalDocs,
      totalModules: docStatsCache.totalModules,
      totalCategories: docStatsCache.totalCategories,
      totalTags: docStatsCache.totalTags,
    };
  } catch {
    return { totalDocs: 0, totalModules: 0, totalCategories: 0, totalTags: 0 };
  }
}

/**
 * 按分类获取文档
 * @param categoryId - 分类 ID（对应 frontmatter 中的 category 字段）
 * @returns 匹配分类的文档数组（按 order 排序）；异常时返回空数组
 */
export async function getDocsByCategory(categoryId: string): Promise<DocEntry[]> {
  try {
    const docs = await getCollection('docs', ({ data }) => data.category === categoryId);
    return docs.sort((a, b) => (a.data.order || 0) - (b.data.order || 0));
  } catch {
    return [];
  }
}

/**
 * 获取关联文档
 * 基于文档 frontmatter 中的 related 字段（相关文档引用列表）查找关联文档
 * 支持两种引用格式：纯 slug 或 "moduleId/slug" 完整路径
 * @param moduleId - 当前文档所属模块 ID
 * @param slug - 当前文档 slug
 * @returns 关联文档数组；异常或无关联时返回空数组
 */
export async function getRelatedDocs(moduleId: string, slug: string): Promise<DocEntry[]> {
  try {
    const current = await getDocBySlug(moduleId, slug);
    if (!current || current.data.related.length === 0) return [];
    const allDocs = await getAllDocs();
    const relatedRefs = new Set(current.data.related);
    return allDocs.filter((doc) => {
      const docSlugStr = docSlug(doc.id);
      const fullRef = `${doc.data.module}/${docSlugStr}`;
      return relatedRefs.has(docSlugStr) || relatedRefs.has(fullRef);
    });
  } catch {
    return [];
  }
}

export type { DocEntry, DocNavigation, DocStats };
export { computeReadingTime, docSlug };
