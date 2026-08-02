/**
 * prismjs 轻量类型声明
 * 项目仅使用 highlight 与 languages 两个 API，无需引入完整 @types/prismjs
 */
declare module 'prismjs' {
  /** 语言语法表（组件文件加载后按语言名注册） */
  export const languages: Record<string, unknown>;

  /**
   * 将代码高亮为带 token class 的 HTML 字符串
   * @param code - 原始代码文本
   * @param grammar - 目标语言语法对象
   * @param language - 语言名（用于回退与别名）
   * @returns 高亮后的 HTML
   */
  export function highlight(code: string, grammar: unknown, language: string): string;

  const Prism: {
    languages: typeof languages;
    highlight: typeof highlight;
  };

  export default Prism;
}
