/**
 * 练习与测验插件 - 类型定义与常量
 * =============================================================================
 * 从 remark-exercise.ts 提取的共享类型与正则常量，供 utils.ts 与 index.ts 使用。
 *
 * 包含内容：
 * - 类型定义：FenceKind / FenceOpenMatch / AttributeMap / ExerciseData
 * - 属性白名单：KNOWN_ATTRS
 * - 正则常量：FENCE_OPEN_PATTERN / FENCE_CLOSE_PATTERN / ATTR_PATTERN
 */

/** 提示块类型：exercise 为独立练习，quiz 为测验容器 */
export type FenceKind = 'exercise' | 'quiz';

/** 属性映射类型：键为属性名，值为属性值（均为字符串） */
export type AttributeMap = Record<string, string>;

/** 已识别的提示块开启标记解析结果 */
export interface FenceOpenMatch {
  /** 提示块类型 */
  kind: FenceKind;
  /** 解析后的属性映射（仅包含白名单内的属性） */
  attrs: AttributeMap;
}

/** exercise 数据对象（用于 JSON 序列化嵌入 data-exercises 属性） */
export interface ExerciseData {
  /** 练习类型（如 fill-blank、choice） */
  type?: string;
  /** 练习唯一标识 */
  id?: string;
  /** 答案 */
  answer?: string;
  /** 题干文本 */
  prompt: string;
  /** 标题（可选） */
  title?: string;
  /** 答案解析（可选） */
  explanation?: string;
  /** 关键知识点（可选） */
  keyPoints?: string;
  /** 难度（可选） */
  difficulty?: string;
  /** 认知层级（可选） */
  cognitiveLevel?: string;
}

/** 已知属性白名单（未知属性自动忽略） */
export const KNOWN_ATTRS: ReadonlySet<string> = new Set([
  'type',
  'id',
  'answer',
  'title',
  'prompt',
  'explanation',
  'keyPoints',
  'difficulty',
  'cognitiveLevel',
]);

/**
 * 提示块开启标记正则：匹配 `:::exercise{...}` 或 `:::quiz{...}`
 *
 * 模式说明：
 *   ^:::                 - 行首三冒号
 *   (exercise|quiz)      - 提示块类型捕获组
 *   (?:\s*\{([^}]*?)\})? - 可选属性组：{} 包裹的属性字符串（非贪婪）
 *   \s*$                 - 行尾允许空白
 *
 * 属性字符串使用 [^}]*? 而非 [^}]*：虽语义相同（} 不允许出现在属性值内），
 * 但非贪婪明确表达"匹配到第一个 } 即止"的意图
 */
export const FENCE_OPEN_PATTERN: RegExp = /^:::(exercise|quiz)(?:\s*\{([^}]*?)\})?\s*$/;

/**
 * 提示块关闭标记正则：匹配仅含 `:::` 与空白的行
 * 用于定位提示块的结束位置
 */
export const FENCE_CLOSE_PATTERN: RegExp = /^:::\s*$/;

/**
 * 属性键值对正则：匹配 `key="value"` 或 `key='value'`
 *
 * 模式说明：
 *   (\w+)                            - 属性名（字母数字下划线）
 *   \s*=\s*                          - 等号两侧允许空白
 *   "(?:[^"\\]|\\.)*"               - 双引号字符串（支持反斜杠转义）
 *   |'(?:[^'\\]|\\.)*'              - 或单引号字符串
 *
 * 转义处理：value 中的引号通过反斜杠转义（如 \"、\'），\\ 匹配任意转义字符
 * 实际 value 内容由 unescapeValue 还原反斜杠转义
 */
export const ATTR_PATTERN: RegExp = /(\w+)\s*=\s*("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')/g;
