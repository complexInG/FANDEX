/**
 * 练习与测验 Markdown 解析插件（remark 插件）- 入口模块
 * =============================================================================
 * 遍历 Markdown AST 中的 paragraph 节点，识别 `:::exercise` 与 `:::quiz`
 * 自定义提示块语法，将其替换为带 data 属性的容器 div，供客户端脚本
 * 扫描并渲染交互式练习组件。
 *
 * 支持格式：
 *   1. exercise 提示块（独立练习）
 *      :::exercise{type="fill-blank" id="ex-001" answer="指针"}
 *      指针是一个存储内存____的变量。
 *      :::
 *
 *   2. quiz 提示块（测验容器，可嵌套多个 exercise）
 *      :::quiz{id="quiz-001" title="指针基础测验"}
 *      :::exercise{type="choice" id="q1" answer="A"}
 *      A. 0x7fff
 *      B. 0
 *      :::
 *      :::
 *
 * 输出 HTML 结构：
 *   <div data-exercise data-type="fill-blank" data-id="ex-001"
 *        data-answer="指针" data-prompt="..."></div>
 *
 *   <div data-quiz data-id="quiz-001" data-title="..."
 *        data-exercises="[{&quot;type&quot;:&quot;choice&quot;,...}]"></div>
 *
 * 设计原则：
 * - 安全转义：所有用户内容（prompt、answer、title 等）经 HTML 实体转义后
 *   嵌入 data-* 属性，避免 XSS 注入；JSON 序列化后再 HTML 转义
 * - 类型严格：使用 mdast 类型定义，无 any/unknown，无 ts-ignore
 * - 嵌套感知：quiz 内可嵌套多个 exercise，关闭标记 ::: 通过深度计数匹配
 * - 已知属性白名单：type、id、answer、title、prompt、explanation、
 *   keyPoints、difficulty、cognitiveLevel，未知属性自动忽略
 *
 * 模块拆分：
 * - types.ts   类型定义与正则/属性常量
 * - utils.ts   HTML 工具、文本提取、围栏匹配、数据构建
 * - index.ts   主插件函数（本文件）
 *
 * 客户端扫描：
 *   客户端脚本扫描 [data-exercise] / [data-quiz] 元素，读取 dataset 属性，
 *   渲染交互式练习与测验组件
 */

import { visit, SKIP } from 'unist-util-visit';
import type { Root, Paragraph, Html } from 'mdast';
import {
  buildExerciseHtml,
  buildQuizHtml,
  collectRangeText,
  extractExercisesFromChildren,
  findCloseFenceIndex,
  matchFenceOpen,
} from './utils';

/**
 * remark-exercise 插件工厂函数
 *
 * 核心执行流程：
 *   1. 使用 visit 遍历 MDAST 中所有 paragraph 节点
 *   2. 检测段落是否为 :::exercise / :::quiz 开启标记
 *   3. 命中开启标记后，向后续兄弟节点查找匹配的关闭标记 :::
 *      （通过深度计数处理 quiz 内嵌套 exercise 的场景）
 *   4. 收集开启与关闭之间的内容：
 *      - exercise：提取纯文本作为 prompt
 *      - quiz：递归提取内部嵌套 exercise 数组
 *   5. 用单个 html 节点替换 [开启..关闭] 整个区间
 *   6. 返回 [SKIP, index+1] 跳过已替换区间，避免重复访问
 *
 * visit 行为说明：
 *   - visit 自动递归进入 blockquote / listItem 等容器节点，
 *     无需手动实现递归
 *   - splice 替换区间后，返回 [SKIP, index+1] 告知 visit：
 *     SKIP = 不再访问被替换节点的子节点（避免访问已移除的文本节点）
 *     index+1 = 下一次访问从插入的 html 节点的下一个兄弟开始
 *
 * @returns remark 插件函数，接收 Root 树并就地变换
 */
export function remarkExercise(): (tree: Root) => void {
  return (tree: Root): void => {
    visit(tree, 'paragraph', (node: Paragraph, index, parent) => {
      // 跳过无父节点或无索引的节点（理论上不会发生，TS 类型保护）
      if (!parent || typeof index !== 'number') return;

      // 检测当前段落是否为 fence 开启标记
      const openMatch = matchFenceOpen(node);
      if (openMatch === null) return;

      // 查找匹配的关闭标记（嵌套感知）
      const closeIdx = findCloseFenceIndex(parent.children, index + 1);
      if (closeIdx === -1) {
        // 未找到关闭标记：保留原节点，避免破坏文档
        return;
      }

      let htmlContent: string;
      if (openMatch.kind === 'exercise') {
        // exercise 提示块：收集主体文本作为 prompt
        const bodyText = collectRangeText(parent.children, index + 1, closeIdx);
        htmlContent = buildExerciseHtml(openMatch.attrs, bodyText);
      } else {
        // quiz 提示块：提取内部嵌套 exercise 数组
        const innerChildren = parent.children.slice(index + 1, closeIdx);
        const exercises = extractExercisesFromChildren(innerChildren);
        htmlContent = buildQuizHtml(openMatch.attrs, exercises);
      }

      // 构建 html 节点替换原提示块区间
      const htmlNode: Html = { type: 'html', value: htmlContent };

      // 用单个 html 节点替换 [index..closeIdx] 区间（含两端）
      // splice(start, deleteCount, ...items)：从 index 开始删除
      // (closeIdx - index + 1) 个节点，插入 1 个 html 节点
      parent.children.splice(index, closeIdx - index + 1, htmlNode);

      // 返回 [SKIP, index+1]：
      //   SKIP - 不访问被替换节点（已移除）的子节点
      //   index+1 - 下一次访问从 html 节点的下一个兄弟开始
      return [SKIP, index + 1];
    });
  };
}
