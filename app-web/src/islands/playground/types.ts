/**
 * Playground 共享类型定义
 *
 * 功能概述：
 *   - 前端实验（CodePen 风格）作品结构
 *   - 编程/算法练习题目结构
 *   - 本地存储记录结构
 *
 * 设计原则：
 *   - 所有数据均保存在用户浏览器本地（IndexedDB + localStorage），不做任何分享/上传
 *   - 类型保持扁平，便于 JSON 序列化到 IndexedDB
 */

/** 前端实验布局模式 */
export type FrontendLayout = 'top' | 'left';

/** 前端实验作品（保存到本地作品库的记录） */
export interface FrontendPen {
  /** 唯一 ID；草稿固定为 'draft'，保存到作品库后使用随机 UUID */
  id: string;
  /** 作品标题 */
  title: string;
  /** HTML 源码 */
  html: string;
  /** CSS 源码 */
  css: string;
  /** JavaScript 源码 */
  js: string;
  /** 是否自动运行预览 */
  autoRun: boolean;
  /** 编辑器布局（编辑器区域在上方或左侧） */
  layout: FrontendLayout;
  /** 是否显示 HTML 编辑器 */
  showHtml: boolean;
  /** 是否显示 CSS 编辑器 */
  showCss: boolean;
  /** 是否显示 JS 编辑器 */
  showJs: boolean;
  /** 是否显示控制台面板 */
  showConsole: boolean;
  /** 创建时间戳（毫秒） */
  createdAt: number;
  /** 最后修改时间戳（毫秒） */
  updatedAt: number;
  /** 最后打开时间戳（毫秒） */
  lastOpenedAt: number;
}

/** 练习支持的语言（Go 在浏览器沙箱暂不支持，不进入选择列表） */
export type LabLanguage = 'javascript' | 'typescript' | 'python' | 'c' | 'cpp';

/** 题目难度 */
export type ExerciseDifficulty = '入门' | '进阶' | '挑战';

/** 测试用例：函数调用参数与期望结果 */
export interface ExerciseCase {
  /** 调用被测试函数的参数列表 */
  args: unknown[];
  /** 期望返回值（mutate 类型题目为参数数组被修改后的期望值） */
  expected: unknown;
}

/** 题目测试方式 */
export type ExerciseKind = 'call' | 'mutate';

/** C/C++ 参数类型（供 C 测试脚手架生成字面量） */
export type CArgType = 'int' | 'str' | 'int[]';

/** C/C++ 返回值类型（供 C 测试脚手架生成比较代码） */
export type CReturnType = 'int' | 'bool' | 'void';

/** C/C++ 函数签名元数据 */
export interface CSignature {
  /** 返回值类型 */
  returnType: CReturnType;
  /** 参数类型列表（顺序与函数签名一致） */
  argTypes: CArgType[];
}

/** 算法练习题目定义（内置目录，随站点版本发布） */
export interface Exercise {
  /** 题目唯一 ID */
  id: string;
  /** 题目名称 */
  title: string;
  /** 难度等级 */
  difficulty: ExerciseDifficulty;
  /** 标签（用于展示与筛选） */
  tags: string[];
  /** 题目说明（纯文本，支持换行） */
  description: string;
  /** 输入输出约定与示例 */
  example: string;
  /** 被测试函数名 */
  functionName: string;
  /** 测试方式：call=比较返回值；mutate=比较参数数组修改结果 */
  kind: ExerciseKind;
  /** C/C++ 签名元数据（用于生成 C 测试脚手架） */
  cSignature: CSignature;
  /** 内置测试用例 */
  cases: ExerciseCase[];
  /** 各语言起始代码模板 */
  starters: Partial<Record<LabLanguage, string>>;
  /** 解题提示（可折叠展示） */
  hints: string[];
}

/** 练习提交记录（每个 题目+语言 一条，保存在 IndexedDB） */
export interface LabRecord {
  /** 记录 ID：`{exerciseId}:{language}` */
  id: string;
  /** 题目 ID */
  exerciseId: string;
  /** 语言 */
  language: LabLanguage;
  /** 用户代码（自动保存，刷新不丢失） */
  code: string;
  /** 最近一次运行状态：solved=全部用例通过；failed=存在失败 */
  status: 'solved' | 'failed';
  /** 累计运行次数 */
  attempts: number;
  /** 累计通过次数 */
  solvedCount: number;
  /** 最近一次运行耗时（毫秒） */
  lastDurationMs: number;
  /** 最近一次运行的通过用例数 */
  lastPassed: number;
  /** 最近一次运行的失败用例数 */
  lastFailed: number;
  /** 最近一次运行时间戳 */
  lastRunAt: number;
  /** 记录创建时间戳 */
  createdAt: number;
}

/** 控制台日志条目（前端实验预览区捕获） */
export interface ConsoleEntry {
  /** 日志类型 */
  kind: 'log' | 'info' | 'warn' | 'error';
  /** 日志文本 */
  text: string;
  /** 捕获时间戳 */
  time: number;
}

/** 本地作品库统计信息（首页展示） */
export interface PlaygroundStats {
  /** 作品库中的前端实验数量 */
  penCount: number;
  /** 已练习过的 题目+语言 组合数 */
  labCount: number;
  /** 全部用例通过过的记录数 */
  solvedCount: number;
  /** 累计运行次数 */
  totalAttempts: number;
  /** 浏览器为当前站点分配的存储配额（字节） */
  quotaBytes: number;
  /** 当前站点已使用的存储（字节） */
  usageBytes: number;
}
