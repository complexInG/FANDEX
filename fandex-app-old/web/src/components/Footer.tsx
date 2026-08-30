/**
 * 页脚
 * 严格对齐 FANDEX-Web index.astro 的 home-footer 风格：
 * - 极简文字链接 + 分隔线
 * - 统计信息行
 * - 技术栈行
 * - 简短声明
 * - 版权
 * 无多列布局、无大段声明文字
 */
import { latestVersion } from '../data/versions';
import { stats } from '../data/modules';

export function Footer() {
  return (
    <footer
      className="py-8 mt-auto"
      style={{ borderTop: '1px solid var(--color-border-light)' }}
    >
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        {/* FANDEX 生态链接：对齐 footer-eco-links */}
        <div
          className="flex items-center justify-center gap-3 flex-wrap mb-3"
          style={{ fontSize: '0.8rem' }}
        >
          <a
            href="https://github.com/fanquanpp/FANDEX-web"
            target="_blank"
            rel="noreferrer"
            className="transition-opacity"
            style={{ color: 'var(--color-primary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            FANDEX-web · 线上平台
          </a>
          <span style={{ color: 'var(--color-text-tertiary)' }}>|</span>
          <a
            href="https://github.com/fanquanpp/FANDEX-exe"
            target="_blank"
            rel="noreferrer"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            FANDEX-exe · 桌面端
          </a>
          <span style={{ color: 'var(--color-text-tertiary)' }}>|</span>
          <a
            href="https://github.com/fanquanpp/FANDEX-App"
            target="_blank"
            rel="noreferrer"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            FANDEX-App · 移动端
          </a>
        </div>

        {/* 快捷链接：对齐 footer-links */}
        <div
          className="flex items-center justify-center gap-3 flex-wrap mb-3"
          style={{ fontSize: '0.8rem' }}
        >
          <a
            href="#download"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            下载
          </a>
          <span style={{ color: 'var(--color-text-tertiary)' }}>|</span>
          <a
            href="#modules"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            模块
          </a>
          <span style={{ color: 'var(--color-text-tertiary)' }}>|</span>
          <a
            href={`https://github.com/fanquanpp/FANDEX-App/releases/tag/${latestVersion.version}`}
            target="_blank"
            rel="noreferrer"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            Release Notes
          </a>
          <span style={{ color: 'var(--color-text-tertiary)' }}>|</span>
          <a
            href="https://github.com/fanquanpp/FANDEX-App/issues"
            target="_blank"
            rel="noreferrer"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            问题反馈
          </a>
          <span style={{ color: 'var(--color-text-tertiary)' }}>|</span>
          <a
            href="https://github.com/fanquanpp/FANDEX-App"
            target="_blank"
            rel="noreferrer"
            className="transition-opacity"
            style={{ color: 'var(--color-text-secondary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            GitHub
          </a>
        </div>

        {/* 统计行：对齐 footer-stats */}
        <div
          className="flex items-center justify-center gap-2 flex-wrap mb-2"
          style={{
            fontSize: '0.75rem',
            fontFamily: 'var(--font-mono)',
            color: 'var(--color-text-tertiary)',
          }}
        >
          <span>{latestVersion.version} 最新版本</span>
          <span>·</span>
          <span>{stats.totalDocuments} 篇文档</span>
          <span>·</span>
          <span>{stats.uniqueModuleCount} 个模块</span>
          <span>·</span>
          <span>{latestVersion.size} APK</span>
        </div>

        {/* 技术栈行：对齐 footer-tech */}
        <div
          className="text-center mb-2"
          style={{
            fontSize: '0.72rem',
            fontFamily: 'var(--font-mono)',
            color: 'var(--color-text-tertiary)',
          }}
        >
          Built with Kotlin + Jetpack Compose · Hosted on GitHub Pages
        </div>

        {/* 简短声明：对齐 footer-notice */}
        <div
          className="text-center mb-2"
          style={{
            fontSize: '0.72rem',
            color: 'var(--color-text-tertiary)',
          }}
        >
          内容由人工与 AI 共同编撰，可能存在遗漏或错误，请结合官方资料独立验证
        </div>
        <div
          className="text-center mb-3"
          style={{
            fontSize: '0.72rem',
            color: 'var(--color-text-tertiary)',
          }}
        >
          除"更新自检"功能访问 GitHub Release API 外，本应用无任何网络请求
        </div>

        {/* 版权：对齐 footer-copyright */}
        <div
          className="text-center"
          style={{
            fontSize: '0.72rem',
            fontFamily: 'var(--font-mono)',
            color: 'var(--color-text-tertiary)',
          }}
        >
          Copyright (c) 2024-{new Date().getFullYear()} fanquanpp · MIT License
        </div>
      </div>
    </footer>
  );
}
