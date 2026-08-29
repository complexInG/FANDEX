/**
 * Hero 区域
 * 对齐 FANDEX-Web index.astro Hero 风格：
 * - 紧凑徽章（hero-badge）+ 标题（FAN 用主色）+ 描述
 * - 统计栏（hero-stats）+ 1px 分隔线 + 快捷链接
 * - 主下载 CTA（主色填充）+ 次要 CTA（边框）
 * - 去除营销化大字号、琥珀色光斑背景
 */
import type { CSSProperties } from 'react';
import { latestVersion } from '../data/versions';
import { stats } from '../data/modules';

export function Hero() {
  return (
    <section
      id="top"
      className="relative bg-dot-grid"
      style={{ borderBottom: '1px solid var(--color-border-light)' }}
    >
      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-12 sm:py-16 text-center">
        {/* 版本徽章：紧凑 hero-badge */}
        <div
          className="inline-block mb-4"
          style={{
            fontFamily: 'var(--font-display)',
            fontSize: '0.7rem',
            fontWeight: 700,
            letterSpacing: '0.2em',
            color: 'var(--color-primary)',
            border: '1px solid var(--color-primary)',
            padding: '3px 14px',
          }}
        >
          {latestVersion.version} · 最新发布
        </div>

        {/* 主标题：FAN 用主色，对齐 FANDEX-Web hero-title */}
        <h1
          className="m-0 mb-2"
          style={{
            fontFamily: 'var(--font-display)',
            fontSize: '3rem',
            fontWeight: 800,
            letterSpacing: '0.25em',
            color: 'var(--color-text)',
          }}
        >
          <span style={{ color: 'var(--color-primary)' }}>FAN</span>DEX
          <span style={{ color: 'var(--color-text-tertiary)' }}>-App</span>
        </h1>

        {/* 描述：对齐 hero-desc */}
        <p
          className="m-0 mb-6 mx-auto"
          style={{
            fontSize: '0.9rem',
            color: 'var(--color-text-secondary)',
            maxWidth: '600px',
            letterSpacing: '0.02em',
          }}
        >
          Android 原生代码语法离线速查应用 · Kotlin + Jetpack Compose + Material 3
        </p>

        {/* 统计栏：对齐 hero-stats，1px 分隔线 */}
        <div
          className="flex items-center justify-center gap-4 flex-wrap mb-8"
          style={{
            fontFamily: 'var(--font-display)',
            fontSize: '0.82rem',
          }}
        >
          <StatItem num={String(stats.uniqueModuleCount)} label="模块" />
          <StatDivider />
          <StatItem num={String(stats.totalDocuments)} label="文档" />
          <StatDivider />
          <StatItem num={latestVersion.version} label="版本" />
          <StatDivider />
          <StatItem num="100%" label="离线" />
          <StatDivider />
          <a
            href="#download"
            className="inline-flex items-center gap-1 font-medium transition-opacity"
            style={{ color: 'var(--color-primary)' }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.8')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            下载 APK
          </a>
        </div>

        {/* 主下载 CTA：主色填充 + 次要边框 */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
          <a
            href={latestVersion.apk}
            download={latestVersion.apkName}
            className="inline-flex items-center gap-2 px-5 py-2.5 font-semibold transition-opacity w-full sm:w-auto justify-center"
            style={{
              backgroundColor: 'var(--color-primary)',
              color: 'var(--color-text-inverse)',
              borderRadius: '2px',
              fontSize: '0.9rem',
            }}
            onMouseEnter={(e) => (e.currentTarget.style.opacity = '0.9')}
            onMouseLeave={(e) => (e.currentTarget.style.opacity = '1')}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            下载 APK · {latestVersion.size}
          </a>
          <a
            href="#download"
            className="inline-flex items-center gap-2 px-5 py-2.5 font-semibold transition-colors w-full sm:w-auto justify-center"
            style={{
              border: '1px solid var(--color-border-strong)',
              color: 'var(--color-text-secondary)',
              borderRadius: '2px',
              fontSize: '0.9rem',
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.color = 'var(--color-primary)';
              e.currentTarget.style.borderColor = 'var(--color-primary)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.color = 'var(--color-text-secondary)';
              e.currentTarget.style.borderColor = 'var(--color-border-strong)';
            }}
          >
            查看历史版本
          </a>
        </div>

        {/* 元信息 */}
        <p
          className="mt-4 m-0"
          style={{
            fontSize: '0.75rem',
            color: 'var(--color-text-tertiary)',
            fontFamily: 'var(--font-mono)',
          }}
        >
          {latestVersion.require} · {latestVersion.apkName} · {latestVersion.date}
        </p>
      </div>
    </section>
  );
}

/** 统计项：数字 + 标签，纵向居中 */
function StatItem({ num, label }: { num: string; label: string }) {
  return (
    <div className="flex flex-col items-center gap-1 pb-1">
      <span
        className="font-bold"
        style={{
          fontSize: '1.3em',
          color: 'var(--color-text)',
        }}
      >
        {num}
      </span>
      <span
        style={{
          fontSize: '0.78em',
          color: 'var(--color-text-secondary)',
          letterSpacing: '0.04em',
        }}
      >
        {label}
      </span>
    </div>
  );
}

/** 统计栏 1px 分隔线：对齐 stat-divider */
function StatDivider() {
  const style: CSSProperties = {
    width: '1px',
    height: '24px',
    background: 'var(--color-border)',
  };
  return <span style={style} aria-hidden="true" />;
}
