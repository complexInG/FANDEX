/**
 * 主题切换 Hook
 * 对齐 FANDEX-Web docs/design-system.md 双主题机制：
 * - light / dark 双主题，持久化到 localStorage（key: fandex-theme）
 * - 默认跟随系统 prefers-color-scheme
 * - 监听系统主题变化，用户未显式设置时跟随系统
 * - 同步 document.documentElement.colorScheme，确保浏览器原生控件响应
 * - 与 index.html 防闪烁脚本协同：脚本在 HTML 解析前设置 data-theme，Hook 在挂载后接管
 */
import { useEffect, useState } from 'react';

type Theme = 'light' | 'dark';

const STORAGE_KEY = 'fandex-theme';

function getInitialTheme(): Theme {
  if (typeof window === 'undefined') return 'light';
  // 优先读取 localStorage（用户显式选择）
  const stored = localStorage.getItem(STORAGE_KEY) as Theme | null;
  if (stored === 'light' || stored === 'dark') return stored;
  // 未显式设置时跟随系统
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function useTheme() {
  const [theme, setTheme] = useState<Theme>(getInitialTheme);

  // 主题应用与持久化
  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    document.documentElement.style.colorScheme = theme;
    localStorage.setItem(STORAGE_KEY, theme);
  }, [theme]);

  // 监听系统主题变化：用户未显式设置时跟随系统
  useEffect(() => {
    const media = window.matchMedia('(prefers-color-scheme: dark)');
    const handleChange = (e: MediaQueryListEvent) => {
      const stored = localStorage.getItem(STORAGE_KEY);
      // 仅在用户未显式设置时跟随系统
      if (!stored) {
        setTheme(e.matches ? 'dark' : 'light');
      }
    };
    media.addEventListener('change', handleChange);
    return () => media.removeEventListener('change', handleChange);
  }, []);

  const toggle = () => {
    setTheme((prev) => (prev === 'light' ? 'dark' : 'light'));
  };

  return { theme, toggle };
}
