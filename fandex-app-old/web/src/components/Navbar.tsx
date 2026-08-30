/**
 * 顶部导航栏
 * 对齐 FANDEX-Web HomeLayout 导航风格：
 * - 1px 底部分割线，半透明背景 + backdrop-blur
 * - 品牌 FAN 用主色（Sky 天蓝），DEX 用正文色
 * - 链接采用直角/微小圆角边框，hover 高亮主色
 * - 主题切换按钮与 GitHub 图标按钮统一尺寸
 */
import type { CSSProperties, MouseEvent, ReactNode } from 'react';

interface NavbarProps {
  theme: 'light' | 'dark';
  onToggleTheme: () => void;
  onOpenNotice?: () => void;
}

export function Navbar({ theme, onToggleTheme, onOpenNotice }: NavbarProps) {
  return (
    <header
      className="sticky top-0 z-50 border-b backdrop-blur-md transition-colors"
      style={{
        borderColor: 'var(--color-border)',
        backgroundColor: 'color-mix(in oklab, var(--color-bg) 85%, transparent)',
      }}
    >
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-14 flex items-center justify-between">
        {/* 品牌标识 */}
        <a href="#top" className="flex items-center gap-2 group">
          <span
            className="inline-flex items-center justify-center w-7 h-7 font-extrabold text-sm"
            style={{
              backgroundColor: 'var(--color-primary)',
              color: 'var(--color-text-inverse)',
              borderRadius: '2px',
            }}
          >
            F
          </span>
          <span
            className="font-bold tracking-wider text-sm"
            style={{ fontFamily: 'var(--font-display)' }}
          >
            <span style={{ color: 'var(--color-primary)' }}>FAN</span>
            <span style={{ color: 'var(--color-text)' }}>DEX</span>
            <span style={{ color: 'var(--color-text-tertiary)' }}>-App</span>
          </span>
        </a>

        {/* 右侧操作 */}
        <nav className="flex items-center gap-2">
          <NavLink href="#download">下载</NavLink>
          <NavLink href="#modules">模块</NavLink>
          {onOpenNotice && (
            <IconButton onClick={onOpenNotice} label="查看通知">
              <svg
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                aria-hidden="true"
              >
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
                <path d="M13.73 21a2 2 0 0 1-3.46 0" />
              </svg>
            </IconButton>
          )}
          <IconButton
            href="https://github.com/fanquanpp/FANDEX-App"
            label="GitHub 仓库"
            external
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.53-1.34-1.3-1.7-1.3-1.7-1.06-.72.08-.71.08-.71 1.17.08 1.79 1.2 1.79 1.2 1.04 1.79 2.73 1.27 3.4.97.1-.75.41-1.27.74-1.56-2.55-.29-5.23-1.28-5.23-5.69 0-1.26.45-2.28 1.2-3.09-.12-.29-.52-1.46.11-3.05 0 0 .98-.31 3.2 1.18a11.1 11.1 0 0 1 5.83 0c2.22-1.49 3.2-1.18 3.2-1.18.63 1.59.23 2.76.11 3.05.75.81 1.2 1.83 1.2 3.09 0 4.42-2.69 5.39-5.25 5.68.42.36.79 1.08.79 2.18v3.23c0 .31.21.68.8.56A11.51 11.51 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5Z" />
            </svg>
          </IconButton>
          <IconButton onClick={onToggleTheme} label="切换主题">
            {theme === 'light' ? (
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
              </svg>
            ) : (
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <circle cx="12" cy="12" r="4" />
                <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41" />
              </svg>
            )}
          </IconButton>
        </nav>
      </div>
    </header>
  );
}

/** 导航链接：直角边框，hover 高亮主色 */
function NavLink({ href, children }: { href: string; children: ReactNode }) {
  return (
    <a
      href={href}
      className="hidden sm:inline-flex items-center px-3 py-1.5 text-sm transition-colors"
      style={{
        border: '1px solid var(--color-border)',
        borderRadius: '2px',
        color: 'var(--color-text-secondary)',
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.color = 'var(--color-primary)';
        e.currentTarget.style.borderColor = 'var(--color-primary)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.color = 'var(--color-text-secondary)';
        e.currentTarget.style.borderColor = 'var(--color-border)';
      }}
    >
      {children}
    </a>
  );
}

/** 图标按钮：直角边框，统一 32x32 尺寸 */
function IconButton({
  children,
  href,
  onClick,
  label,
  external,
}: {
  children: ReactNode;
  href?: string;
  onClick?: () => void;
  label: string;
  external?: boolean;
}) {
  const style: CSSProperties = {
    border: '1px solid var(--color-border)',
    borderRadius: '2px',
    color: 'var(--color-text-secondary)',
  };
  const hoverStyle: Partial<CSSProperties> = {
    color: 'var(--color-primary)',
    borderColor: 'var(--color-primary)',
  };
  const baseClass =
    'inline-flex items-center justify-center w-8 h-8 transition-colors';
  const handleEnter = (e: MouseEvent<HTMLElement>) => {
    Object.assign(e.currentTarget.style, hoverStyle);
  };
  const handleLeave = (e: MouseEvent<HTMLElement>) => {
    Object.assign(e.currentTarget.style, {
      color: 'var(--color-text-secondary)',
      borderColor: 'var(--color-border)',
    });
  };
  if (href) {
    return (
      <a
        href={href}
        target={external ? '_blank' : undefined}
        rel={external ? 'noreferrer' : undefined}
        aria-label={label}
        className={baseClass}
        style={style}
        onMouseEnter={handleEnter}
        onMouseLeave={handleLeave}
      >
        {children}
      </a>
    );
  }
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={label}
      className={baseClass}
      style={style}
      onMouseEnter={handleEnter}
      onMouseLeave={handleLeave}
    >
      {children}
    </button>
  );
}
