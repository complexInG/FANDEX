/**
 * 代码格式化服务（Prettier CDN 按需加载）
 *
 * 功能概述：
 *   - 前端实验（HTML/CSS/JS）与在线沙箱（JS/TS/Python）共享格式化能力
 *   - Prettier 与语言插件通过 CDN 动态 import，仅在用户点击格式化时加载
 *   - 暂不支持的语言（C/C++/Java/Go 等）返回原代码并给出提示
 *
 * 设计原则：
 *   - 不引入构建期依赖，避免增加主包体积；CDN 加载失败时静默降级
 *   - 格式化失败不修改用户代码，保证编辑内容安全
 */

/** Prettier CDN 版本 */
const PRETTIER_VERSION = '3.5.3';
/** Prettier CDN 基础路径 */
const PRETTIER_BASE = `https://cdn.jsdelivr.net/npm/prettier@${PRETTIER_VERSION}`;

/** 支持 Prettier 格式化的语言（键为沙箱语言标识） */
type FormattableLanguage = 'html' | 'css' | 'javascript' | 'typescript' | 'python';

/** 语言 → Prettier 解析器名 */
const PARSER_BY_LANGUAGE: Record<FormattableLanguage, string> = {
  html: 'html',
  css: 'css',
  javascript: 'babel',
  typescript: 'babel-ts',
  python: 'python',
};

/**
 * 动态加载 Prettier 插件
 * @param parser - Prettier 解析器名
 * @returns 插件模块对象
 */
async function loadPlugin(parser: string): Promise<unknown> {
  // 使用变量 URL + @vite-ignore，确保 Vite 构建期不解析 CDN 地址
  const pluginUrl = `${PRETTIER_BASE}/plugins/${parser}.mjs`;
  return import(/* @vite-ignore */ pluginUrl);
}

/**
 * 格式化代码
 * @param language - 语言标识
 * @param code - 原始代码
 * @returns 格式化结果；未支持的语言返回原代码与提示
 */
export async function formatCode(
  language: string,
  code: string,
): Promise<{ code: string; note: string }> {
  const parser = PARSER_BY_LANGUAGE[language as FormattableLanguage];
  if (!parser) {
    return { code, note: '该语言暂不支持自动格式化' };
  }
  try {
    // Prettier standalone 主模块（UMD 全局：window.prettier）
    const standaloneUrl = `${PRETTIER_BASE}/standalone.mjs`;
    const standalone = await import(/* @vite-ignore */ standaloneUrl);
    const format = (
      standalone as {
        format: (source: string, options: Record<string, unknown>) => Promise<string>;
      }
    ).format;
    if (typeof format !== 'function') {
      return { code, note: '格式化组件加载失败' };
    }
    // babel 解析器依赖 estree 插件，需一并加载
    const plugins = [await loadPlugin(parser)];
    if (parser === 'babel' || parser === 'babel-ts') {
      plugins.push(await loadPlugin('estree'));
    }
    const formatted = await format(code, {
      parser,
      plugins,
      printWidth: 88,
      tabWidth: 2,
      semi: true,
      singleQuote: true,
    });
    return { code: formatted, note: '' };
  } catch {
    // 网络或 CDN 异常时保持原代码，不打断编辑
    return { code, note: '格式化失败，已保留原代码' };
  }
}
