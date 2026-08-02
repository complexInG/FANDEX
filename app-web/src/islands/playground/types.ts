/**
 * Playground 共享类型定义
 *
 * 功能概述：
 *   - 前端实验（CodePen 风格）作品结构
 *   - 在线编程沙箱语言结构
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
  /** 各编辑器面板的弹性权重（HTML/CSS/JS 相对比例，用于拖拽调整边界） */
  paneWeights: { html: number; css: number; js: number };
  /** 是否显示控制台面板 */
  showConsole: boolean;
  /** 创建时间戳（毫秒） */
  createdAt: number;
  /** 最后修改时间戳（毫秒） */
  updatedAt: number;
  /** 最后打开时间戳（毫秒） */
  lastOpenedAt: number;
}

/** 在线编程沙箱支持的语言（编辑与高亮全覆盖；运行能力由浏览器沙箱运行时决定） */
export type LabLanguage =
  | 'javascript'
  | 'typescript'
  | 'python'
  | 'c'
  | 'cpp'
  | 'go'
  | 'java'
  | 'kotlin'
  | 'rust'
  | 'csharp'
  | 'lua'
  | 'sql'
  | 'shell';

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
  /** 已编辑过的语言数 */
  languageCount: number;
  /** 浏览器为当前站点分配的存储配额（字节） */
  quotaBytes: number;
  /** 当前站点已使用的存储（字节） */
  usageBytes: number;
}
