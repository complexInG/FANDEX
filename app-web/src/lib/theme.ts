/**
 * 主题管理模块（web 端）
 * =============================================================================
 * 职责：
 *   1. 提供主题读取/写入的统一 API，封装 localStorage 持久化
 *   2. 提供 SSR 安全的主题检测
 *   3. 提供 View Transitions 切换后的主题重应用（解决 FOUC 闪烁）
 *   4. 提供 meta theme-color 动态更新（移动端浏览器 UI 适配）
 *   5. 提供跨标签页主题同步
 *
 * FOUC（Flash of Unstyled Content）防护体系：
 *   - 第一层：<head> 内联同步脚本，在 body 渲染前设置 data-theme（见 BaseLayout.astro）
 *   - 第二层：astro:after-swap 事件监听，View Transitions 切换后重新应用主题
 *   - 第三层：meta theme-color 动态更新，移动端浏览器 UI 颜色同步
 *   - 第四层：ThemeToggle 组件挂载时二次确认（防止内联脚本未执行）
 *
 * 存储 key：fandex-theme
 * 值：'light' | 'dark'
 * 无存储值时跟随系统偏好 prefers-color-scheme
 * =============================================================================
 */
import { getItem, setItem, onStorageChange } from './storage';

/** 主题类型 */
export type Theme = 'light' | 'dark';

/** 主题存储 key */
export const THEME_STORAGE_KEY = 'fandex-theme';

/** 亮色模式 theme-color 值（移动端浏览器 UI） */
const THEME_COLOR_LIGHT = '#ffffff';

/** 暗色模式 theme-color 值（移动端浏览器 UI） */
const THEME_COLOR_DARK = '#0a0e14';

/**
 * 检测系统暗色模式偏好
 * SSR 环境或 matchMedia 不可用时返回 false
 *
 * @returns 系统是否偏好暗色模式
 */
export function prefersDarkMode(): boolean {
  if (typeof window === 'undefined' || !window.matchMedia) return false;
  return window.matchMedia('(prefers-color-scheme: dark)').matches;
}

/**
 * 从 localStorage 读取已保存的主题偏好
 * 无保存值或异常时返回 null（调用方应回退到系统偏好）
 *
 * @returns 已保存的主题；无保存值时返回 null
 */
export function getSavedTheme(): Theme | null {
  const raw = getItem(THEME_STORAGE_KEY);
  if (raw === 'light' || raw === 'dark') return raw;
  return null;
}

/**
 * 获取当前应应用的主题
 * 优先级：localStorage 保存值 > 系统偏好 > 默认 light
 *
 * @returns 当前应应用的主题
 */
export function getResolvedTheme(): Theme {
  const saved = getSavedTheme();
  if (saved) return saved;
  return prefersDarkMode() ? 'dark' : 'light';
}

/**
 * 将主题应用到 document.documentElement
 * 设置 data-theme 属性 + colorScheme 样式 + meta theme-color
 *
 * @param theme - 要应用的主题
 */
export function applyTheme(theme: Theme): void {
  if (typeof document === 'undefined') return;
  // 设置 data-theme 属性（驱动 CSS 变量切换）
  document.documentElement.setAttribute('data-theme', theme);
  // 设置 colorScheme（影响表单控件、滚动条等原生 UI）
  document.documentElement.style.colorScheme = theme;
  // 更新 meta theme-color（移动端浏览器地址栏/状态栏颜色同步）
  updateMetaThemeColor(theme);
}

/**
 * 持久化主题到 localStorage 并应用到 DOM
 *
 * @param theme - 要保存并应用的主题
 */
export function setTheme(theme: Theme): void {
  setItem(THEME_STORAGE_KEY, theme);
  applyTheme(theme);
}

/**
 * 切换主题（light <-> dark）
 *
 * @returns 切换后的新主题
 */
export function toggleTheme(): Theme {
  const current = getResolvedTheme();
  const next: Theme = current === 'dark' ? 'light' : 'dark';
  setTheme(next);
  return next;
}

/**
 * 更新 meta[name="theme-color"] 标签
 * 移动端浏览器使用此值渲染地址栏/状态栏背景
 * 若标签不存在则创建
 *
 * @param theme - 当前主题
 */
export function updateMetaThemeColor(theme: Theme): void {
  if (typeof document === 'undefined') return;
  const color = theme === 'dark' ? THEME_COLOR_DARK : THEME_COLOR_LIGHT;
  let meta = document.querySelector('meta[name="theme-color"]');
  if (!meta) {
    meta = document.createElement('meta');
    meta.setAttribute('name', 'theme-color');
    document.head.appendChild(meta);
  }
  meta.setAttribute('content', color);
}

/**
 * 初始化 View Transitions 主题持久化
 * 监听 astro:after-swap 事件，在页面切换后重新应用已保存的主题
 * 解决 ClientRouter 切换页面时 data-theme 属性丢失导致的白闪问题
 *
 * 此函数应在客户端脚本入口调用一次，自动管理生命周期
 */
export function initThemePersistence(): void {
  if (typeof document === 'undefined') return;

  // View Transitions 切换后重新应用主题
  // ClientRouter 会替换 document.documentElement，可能导致 data-theme 丢失
  document.addEventListener('astro:after-swap', () => {
    applyTheme(getResolvedTheme());
  });

  // 跨标签页同步：其他标签页切换主题时，当前标签页同步更新
  onStorageChange(THEME_STORAGE_KEY, (newValue) => {
    if (newValue === 'light' || newValue === 'dark') {
      applyTheme(newValue);
    }
  });

  // 系统主题变化时，若用户未手动设置过主题则跟随系统
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      // 仅在用户未手动设置主题时跟随系统
      if (!getSavedTheme()) {
        applyTheme(e.matches ? 'dark' : 'light');
      }
    });
  }
}
