/**
 * 练习与测验插件 - 工具函数集
 * =============================================================================
 * 从 remark-exercise.ts 提取的辅助函数，按职责分为四组：
 *
 * 1. HTML 工具：unescapeValue / escapeHtml / parseAttributes / appendAttrPart
 * 2. 文本提取：extractInlineText / extractRootContentText / extractBlockChildrenText /
 *              collectRangeText
 * 3. 围栏匹配：matchFenceOpen / isFenceClose / findCloseFenceIndex
 * 4. 数据构建：buildExerciseData / extractExercisesFromChildren /
 *              buildExerciseHtml / buildQuizHtml
 *
 * 依赖关系：所有函数仅依赖 types.ts 中的类型与常量，以及 mdast 类型定义。
 */

import type { Paragraph, PhrasingContent, RootContent } from 'mdast';
import {
  type AttributeMap,
  type ExerciseData,
  type FenceOpenMatch,
  ATTR_PATTERN,
  FENCE_CLOSE_PATTERN,
  FENCE_OPEN_PATTERN,
  KNOWN_ATTRS,
} from './types';

// ============================================================================
// 1. HTML 工具函数
// ============================================================================

/**
 * 反斜杠转义还原：将 \" 还原为 "，\' 还原为 '，\\ 还原为 \
 * 模式 \\(.) 匹配反斜杠加任意字符，保留该字符
 *
 * @param s - 待还原的字符串（可能包含转义序列）
 * @returns 还原后的字符串
 */
export function unescapeValue(s: string): string {
  return s.replace(/\\(.)/g, '$1');
}

/**
 * HTML 实体转义（防 XSS）
 *
 * 转义 5 个核心字符：& < > " '
 * 顺序重要：& 必须先转义，否则后续转义产生的 & 会被二次转义
 *
 * @param s - 原始字符串
 * @returns 转义后的 HTML 安全字符串
 */
export function escapeHtml(s: string): string {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/**
 * 解析属性字符串为属性映射
 *
 * 核心执行流程：
 *   1. 使用 matchAll 全局匹配所有 key="value" 或 key='value' 对
 *   2. 跳过未在 KNOWN_ATTRS 白名单内的属性
 *   3. 去除首尾引号并还原反斜杠转义
 *   4. 返回属性映射对象
 *
 * 边界处理：
 *   - 空字符串返回空对象
 *   - 重复键以最后一次为准（matchAll 按顺序处理）
 *   - 未闭合引号不匹配（正则要求完整闭合）
 *
 * @param attrStr - 属性字符串（如 `type="fill-blank" id="ex-001"`）
 * @returns 属性映射对象（仅包含白名单属性）
 */
export function parseAttributes(attrStr: string): AttributeMap {
  const result: AttributeMap = {};
  // 处理 attrStr 为空字符串或纯空白的边界情况
  if (attrStr.trim().length === 0) {
    return result;
  }

  // 全局匹配需使用 String.matchAll，避免 exec 循环的复杂状态管理
  for (const match of attrStr.matchAll(ATTR_PATTERN)) {
    // noUncheckedIndexedAccess：match[1] / match[2] 类型为 string | undefined
    const key = match[1];
    const rawValue = match[2];
    if (key === undefined || rawValue === undefined) continue;
    if (!KNOWN_ATTRS.has(key)) continue;

    // 去除首尾引号（slice 比 replace 更安全，不会误改内部字符）
    const inner = rawValue.slice(1, -1);
    result[key] = unescapeValue(inner);
  }

  return result;
}

/**
 * 向属性片段数组追加单个 data-* 属性（值为 undefined 时跳过）
 *
 * @param parts - 属性片段数组（已包含的字符串）
 * @param key - 属性名（如 type、id）
 * @param value - 属性值（undefined 时跳过）
 */
export function appendAttrPart(parts: string[], key: string, value: string | undefined): void {
  if (value === undefined) return;
  parts.push(` data-${key}="${escapeHtml(value)}"`);
}

// ============================================================================
// 2. 文本提取函数
// ============================================================================

/**
 * 递归提取行内内容的纯文本
 *
 * 处理的节点类型：
 *   - text / inlineCode / html：直接取 value
 *   - strong / emphasis / delete / link / linkReference：递归子节点
 *   - image / imageReference：取 alt 文本
 *   - break：转为换行符
 *   - 其他类型：忽略
 *
 * @param nodes - 行内内容节点数组
 * @returns 拼接后的纯文本
 */
export function extractInlineText(nodes: readonly PhrasingContent[]): string {
  const parts: string[] = [];
  for (const node of nodes) {
    switch (node.type) {
      case 'text':
      case 'inlineCode':
      case 'html':
        parts.push(node.value);
        break;
      case 'strong':
      case 'emphasis':
      case 'delete':
      case 'link':
      case 'linkReference':
        parts.push(extractInlineText(node.children));
        break;
      case 'image':
      case 'imageReference':
        // 图片节点的 alt 属性为可选字符串，nullish 检查后使用
        if (node.alt) {
          parts.push(node.alt);
        }
        break;
      case 'break':
        parts.push('\n');
        break;
      default:
        // 忽略 footnoteReference 等不常见类型
        break;
    }
  }
  return parts.join('');
}

/**
 * 从 RootContent 节点提取纯文本
 *
 * 处理的块级节点类型：
 *   - paragraph / heading：递归提取行内内容
 *   - code / html：直接取 value
 *   - blockquote / listItem：递归处理子节点
 *   - table / thematicBreak / list 等：返回空字符串或简化文本
 *
 * @param node - 根级内容节点
 * @returns 节点的纯文本表示
 */
export function extractRootContentText(node: RootContent): string {
  switch (node.type) {
    case 'paragraph':
    case 'heading':
      return extractInlineText(node.children);
    case 'code':
    case 'html':
      return node.value;
    case 'blockquote':
    case 'listItem':
      // 递归处理嵌套块，子节点为数组
      return extractBlockChildrenText(node.children);
    case 'table':
      // 表格简化处理：按行提取单元格文本
      return node.children
        .map((row) => row.children.map((cell) => extractInlineText(cell.children)).join(' | '))
        .join('\n');
    case 'list':
      return extractBlockChildrenText(node.children);
    case 'thematicBreak':
      return '';
    default:
      // 兼容扩展类型（如 mdxJsxFlowElement 等），忽略未知类型
      return '';
  }
}

/**
 * 递归提取块级子节点数组的纯文本
 *
 * @param children - 块级节点数组（Parent.children 的子集）
 * @returns 拼接后的纯文本
 */
export function extractBlockChildrenText(children: readonly RootContent[]): string {
  const parts: string[] = [];
  for (const child of children) {
    const text = extractRootContentText(child);
    if (text.length > 0) {
      parts.push(text);
    }
  }
  return parts.join('\n\n');
}

/**
 * 收集范围内子节点的纯文本（用空行连接段落）
 *
 * 用于提取 exercise 提示块的 prompt 文本
 *
 * @param children - 父节点的子节点数组
 * @param startIdx - 起始索引（含）
 * @param endIdx - 结束索引（不含）
 * @returns 拼接后的纯文本，首尾空白已去除
 */
export function collectRangeText(
  children: readonly RootContent[],
  startIdx: number,
  endIdx: number
): string {
  const parts: string[] = [];
  for (let i = startIdx; i < endIdx; i++) {
    // noUncheckedIndexedAccess：children[i] 类型为 RootContent | undefined
    const child = children[i];
    if (!child) continue;

    const text = extractRootContentText(child);
    if (text.length > 0) {
      parts.push(text);
    }
  }
  // 段落间用空行连接，保留视觉分隔；首尾 trim 去除多余空白
  return parts.join('\n\n').trim();
}

// ============================================================================
// 3. 围栏匹配函数
// ============================================================================

/**
 * 检测段落是否为提示块开启标记
 *
 * 核心执行流程：
 *   1. 段落必须仅含单个 text 子节点（多节点段落不视为 fence）
 *   2. 文本需匹配 FENCE_OPEN_PATTERN 正则
 *   3. 解析属性字符串并返回结构化结果
 *
 * @param paragraph - 待检测的段落节点
 * @returns 匹配结果对象；不匹配返回 null
 */
export function matchFenceOpen(paragraph: Paragraph): FenceOpenMatch | null {
  // 段落必须仅含单个文本子节点，避免误匹配含格式化内容的段落
  if (paragraph.children.length !== 1) return null;

  // noUncheckedIndexedAccess：children[0] 类型为 PhrasingContent | undefined
  const onlyChild = paragraph.children[0];
  if (!onlyChild || onlyChild.type !== 'text') return null;

  const match = onlyChild.value.match(FENCE_OPEN_PATTERN);
  if (!match) return null;

  // match[1] 为提示块类型（exercise | quiz），正则保证存在但 TS 不感知
  const kind = match[1];
  if (kind !== 'exercise' && kind !== 'quiz') return null;

  // match[2] 为属性字符串（可能为 undefined 表示无属性）
  const attrStr = match[2] ?? '';

  return {
    kind,
    attrs: parseAttributes(attrStr),
  };
}

/**
 * 检测段落是否为提示块关闭标记 `:::`
 *
 * @param paragraph - 待检测的段落节点
 * @returns 是关闭标记返回 true，否则 false
 */
export function isFenceClose(paragraph: Paragraph): boolean {
  if (paragraph.children.length !== 1) return false;

  // noUncheckedIndexedAccess：children[0] 类型为 PhrasingContent | undefined
  const onlyChild = paragraph.children[0];
  if (!onlyChild || onlyChild.type !== 'text') return false;

  return FENCE_CLOSE_PATTERN.test(onlyChild.value);
}

/**
 * 从指定位置向后查找匹配的关闭标记 :::（嵌套感知）
 *
 * 核心执行流程：
 *   1. 从 startIdx 开始遍历 children
 *   2. 遇到开启标记（:::exercise 或 :::quiz）深度 +1
 *   3. 遇到关闭标记（:::）深度 -1，深度归零时返回当前索引
 *   4. 遍历结束未找到返回 -1
 *
 * 嵌套处理说明：
 *   quiz 内可嵌套 exercise，exercise 内理论上也可再嵌套（虽不常见）。
 *   通过深度计数统一处理任意层级嵌套，避免 mismatched 关闭标记。
 *
 * @param children - 父节点的子节点数组
 * @param startIdx - 起始搜索索引（不含）
 * @returns 关闭标记索引；未找到返回 -1
 */
export function findCloseFenceIndex(children: readonly RootContent[], startIdx: number): number {
  let depth = 0;
  for (let i = startIdx; i < children.length; i++) {
    // noUncheckedIndexedAccess：children[i] 类型为 RootContent | undefined
    const child = children[i];
    if (!child || child.type !== 'paragraph') continue;

    // 先检测关闭标记（避免将 :::exercise 误判为关闭）
    // 关闭标记 ::: 严格匹配 FENCE_CLOSE_PATTERN
    if (isFenceClose(child)) {
      if (depth === 0) {
        return i;
      }
      depth--;
      continue;
    }

    // 开启标记深度 +1
    const openMatch = matchFenceOpen(child);
    if (openMatch !== null) {
      depth++;
    }
  }
  return -1;
}

// ============================================================================
// 4. 数据构建函数
// ============================================================================

/**
 * 构建单个 exercise 数据对象
 *
 * 核心执行流程：
 *   1. 以 bodyText 作为 prompt（提示块主体文本）
 *   2. 若 attrs.prompt 显式设置，则覆盖 bodyText
 *   3. 条件添加可选属性（exactOptionalPropertyTypes 要求不能赋 undefined）
 *
 * @param attrs - 解析后的属性映射
 * @param bodyText - 提示块主体文本
 * @returns exercise 数据对象
 */
export function buildExerciseData(attrs: AttributeMap, bodyText: string): ExerciseData {
  // prompt 属性优先：允许通过属性覆盖主体文本
  const promptFromAttrs = attrs.prompt;
  const prompt = promptFromAttrs !== undefined ? promptFromAttrs : bodyText;

  // exactOptionalPropertyTypes：可选属性不能赋 undefined，
  // 必须条件判断后赋值
  const data: ExerciseData = { prompt };

  if (attrs.type !== undefined) data.type = attrs.type;
  if (attrs.id !== undefined) data.id = attrs.id;
  if (attrs.answer !== undefined) data.answer = attrs.answer;
  if (attrs.title !== undefined) data.title = attrs.title;
  if (attrs.explanation !== undefined) data.explanation = attrs.explanation;
  if (attrs.keyPoints !== undefined) data.keyPoints = attrs.keyPoints;
  if (attrs.difficulty !== undefined) data.difficulty = attrs.difficulty;
  if (attrs.cognitiveLevel !== undefined) data.cognitiveLevel = attrs.cognitiveLevel;

  return data;
}

/**
 * 从 quiz 内部子节点提取嵌套的 exercise 数据数组
 *
 * 核心执行流程：
 *   1. 遍历 children，查找 :::exercise 开启标记
 *   2. 对每个 exercise，查找其匹配的关闭标记 :::
 *   3. 收集开启与关闭之间的子节点文本作为 prompt
 *   4. 合并属性与 prompt 构建 ExerciseData 对象
 *   5. 跳过已处理的 exercise 块，继续扫描
 *
 * 非 exercise 内容（如 quiz 内的直接文本）会被忽略
 *
 * @param children - quiz 提示块内部的子节点数组
 * @returns exercise 数据对象数组
 */
export function extractExercisesFromChildren(children: readonly RootContent[]): ExerciseData[] {
  const result: ExerciseData[] = [];
  let i = 0;

  while (i < children.length) {
    // noUncheckedIndexedAccess：children[i] 类型为 RootContent | undefined
    const child = children[i];
    if (child && child.type === 'paragraph') {
      const openMatch = matchFenceOpen(child);

      // 仅处理 exercise 类型；忽略 quiz 嵌套（不支持 quiz 内嵌 quiz）
      if (openMatch !== null && openMatch.kind === 'exercise') {
        const closeIdx = findCloseFenceIndex(children, i + 1);
        if (closeIdx !== -1) {
          const bodyText = collectRangeText(children, i + 1, closeIdx);
          result.push(buildExerciseData(openMatch.attrs, bodyText));
          i = closeIdx + 1;
          continue;
        }
      }
    }
    i++;
  }

  return result;
}

/**
 * 构建 exercise 容器 div 的 HTML 字符串
 *
 * 生成结构：
 *   <div data-exercise data-type="..." data-id="..." data-answer="..."
 *        data-prompt="..."></div>
 *
 * 属性顺序：data-exercise（布尔）→ type → id → answer → prompt → 其他
 *
 * @param attrs - 解析后的属性映射
 * @param bodyText - 提示块主体文本
 * @returns HTML 字符串
 */
export function buildExerciseHtml(attrs: AttributeMap, bodyText: string): string {
  // prompt 属性优先：允许通过属性覆盖主体文本
  const promptFromAttrs = attrs.prompt;
  const prompt = promptFromAttrs !== undefined ? promptFromAttrs : bodyText;

  // 收集属性片段，按预期顺序输出
  const parts: string[] = ['<div data-exercise'];

  appendAttrPart(parts, 'type', attrs.type);
  appendAttrPart(parts, 'id', attrs.id);
  appendAttrPart(parts, 'answer', attrs.answer);
  // prompt 总是输出（即使为空字符串，保持属性结构稳定）
  parts.push(` data-prompt="${escapeHtml(prompt)}"`);
  appendAttrPart(parts, 'title', attrs.title);
  appendAttrPart(parts, 'explanation', attrs.explanation);
  appendAttrPart(parts, 'keyPoints', attrs.keyPoints);
  appendAttrPart(parts, 'difficulty', attrs.difficulty);
  appendAttrPart(parts, 'cognitiveLevel', attrs.cognitiveLevel);

  parts.push('></div>');
  return parts.join('');
}

/**
 * 构建 quiz 容器 div 的 HTML 字符串
 *
 * 生成结构：
 *   <div data-quiz data-id="..." data-title="..."
 *        data-exercises="JSON"></div>
 *
 * JSON 序列化策略：
 *   1. 使用 JSON.stringify 序列化 exercises 数组
 *   2. 使用 escapeHtml 转义所有特殊字符（& < > " '）
 *   3. 嵌入双引号属性中，浏览器解析时 &quot; 还原为 "
 *   4. 客户端读取 dataset.exercises 后 JSON.parse 即可
 *
 * @param attrs - 解析后的属性映射
 * @param exercises - 嵌套 exercise 数据数组
 * @returns HTML 字符串
 */
export function buildQuizHtml(attrs: AttributeMap, exercises: ExerciseData[]): string {
  const parts: string[] = ['<div data-quiz'];

  appendAttrPart(parts, 'id', attrs.id);
  appendAttrPart(parts, 'title', attrs.title);

  // JSON 序列化后 HTML 转义，确保安全嵌入属性
  // 客户端读取后浏览器自动解码 HTML 实体，再 JSON.parse 得到原始对象
  const exercisesJson = JSON.stringify(exercises);
  parts.push(` data-exercises="${escapeHtml(exercisesJson)}"`);

  parts.push('></div>');
  return parts.join('');
}
