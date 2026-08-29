/**
 * 版本下载区
 * 对齐 FANDEX-Web 折叠分类 + 1px 网格分割线风格：
 * - 按主版本号分组（category-header 可折叠）
 * - 版本列表使用 1px 网格分割线（grid + gap + 背景色）
 * - 每个版本卡片可展开查看完整变更日志
 */
import { useState } from 'react';
import { versionGroups, latestVersion } from '../data/versions';

export function DownloadSection() {
  // 默认展开最新分组
  const [expandedGroups, setExpandedGroups] = useState<Set<string>>(
    new Set([versionGroups[0]?.range]),
  );
  // 默认展开最新版本详情
  const [expandedVersions, setExpandedVersions] = useState<Set<string>>(
    new Set([latestVersion.id]),
  );

  const toggleGroup = (range: string) => {
    setExpandedGroups((prev) => {
      const next = new Set(prev);
      if (next.has(range)) next.delete(range);
      else next.add(range);
      return next;
    });
  };

  const toggleVersion = (id: string) => {
    setExpandedVersions((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  return (
    <section
      id="download"
      className="py-12 sm:py-16"
      style={{ borderTop: '1px solid var(--color-border-light)' }}
    >
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        {/* 区域标题 */}
        <div className="mb-8">
          <h2
            className="m-0 mb-2"
            style={{
              fontFamily: 'var(--font-display)',
              fontSize: '1.5rem',
              fontWeight: 700,
              color: 'var(--color-text)',
            }}
          >
            版本下载
          </h2>
          <p style={{ fontSize: '0.875rem', color: 'var(--color-text-secondary)' }}>
            所有版本均通过 fandex-release.jks 签名，建议优先下载最新版。
          </p>
        </div>

        {/* 分组列表 */}
        <div className="space-y-3">
          {versionGroups.map((group) => {
            const isExpanded = expandedGroups.has(group.range);
            return (
              <div
                key={group.range}
                style={{
                  border: '1px solid var(--color-border)',
                  borderRadius: '2px',
                  backgroundColor: 'var(--color-bg-card)',
                }}
              >
                {/* 分组标题：对齐 category-header */}
                <button
                  type="button"
                  onClick={() => toggleGroup(group.range)}
                  className="w-full flex items-center justify-between px-4 py-3 transition-colors"
                  style={{ backgroundColor: 'transparent' }}
                  onMouseEnter={(e) =>
                    (e.currentTarget.style.backgroundColor = 'var(--color-bg-hover)')
                  }
                  onMouseLeave={(e) =>
                    (e.currentTarget.style.backgroundColor = 'transparent')
                  }
                  aria-expanded={isExpanded}
                >
                  <div className="flex items-center gap-3">
                    <span
                      style={{
                        fontFamily: 'var(--font-mono)',
                        fontSize: '0.875rem',
                        color: 'var(--color-primary)',
                        fontWeight: 600,
                      }}
                    >
                      {group.range}
                    </span>
                    <span
                      style={{
                        fontSize: '0.75rem',
                        padding: '2px 8px',
                        backgroundColor: 'var(--color-bg-active)',
                        color: 'var(--color-text-secondary)',
                        borderRadius: '2px',
                      }}
                    >
                      {group.versions.length} 个版本
                    </span>
                  </div>
                  <ChevronIcon expanded={isExpanded} />
                </button>

                {/* 分组内容：1px 网格分割线 */}
                {isExpanded && (
                  <div
                    style={{
                      borderTop: '1px solid var(--color-border)',
                      backgroundColor: 'var(--color-border)',
                    }}
                  >
                    {group.versions.map((v, idx) => {
                      const isLatest = v.id === latestVersion.id;
                      const isVersionExpanded = expandedVersions.has(v.id);
                      return (
                        <div
                          key={v.id}
                          style={{
                            backgroundColor: 'var(--color-bg)',
                            ...(idx > 0 ? { borderTop: '1px solid var(--color-border)' } : {}),
                          }}
                        >
                          <button
                            type="button"
                            onClick={() => toggleVersion(v.id)}
                            className="w-full flex items-start justify-between gap-4 text-left px-4 py-3 transition-colors"
                            style={{ backgroundColor: 'transparent' }}
                            onMouseEnter={(e) =>
                              (e.currentTarget.style.backgroundColor =
                                'var(--color-bg-hover)')
                            }
                            onMouseLeave={(e) =>
                              (e.currentTarget.style.backgroundColor = 'transparent')
                            }
                            aria-expanded={isVersionExpanded}
                          >
                            <div className="flex-1 min-w-0">
                              <div className="flex items-center gap-2 mb-1 flex-wrap">
                                <span
                                  style={{
                                    fontFamily: 'var(--font-mono)',
                                    fontWeight: 600,
                                    fontSize: '0.95rem',
                                    color: 'var(--color-text)',
                                  }}
                                >
                                  {v.version}
                                </span>
                                <span
                                  style={{
                                    fontSize: '0.7rem',
                                    padding: '2px 8px',
                                    borderRadius: '2px',
                                    color: isLatest
                                      ? 'var(--color-text-inverse)'
                                      : 'var(--color-text-secondary)',
                                    backgroundColor: isLatest
                                      ? 'var(--color-primary)'
                                      : 'var(--color-bg-active)',
                                  }}
                                >
                                  {v.badge}
                                </span>
                              </div>
                              <p
                                className="m-0 mb-1"
                                style={{
                                  fontSize: '0.85rem',
                                  color: 'var(--color-text-secondary)',
                                }}
                              >
                                {v.summary}
                              </p>
                              <p
                                className="m-0"
                                style={{
                                  fontSize: '0.75rem',
                                  fontFamily: 'var(--font-mono)',
                                  color: 'var(--color-text-tertiary)',
                                }}
                              >
                                {v.date} · {v.size} · {v.require}
                              </p>
                            </div>
                            <ChevronIcon expanded={isVersionExpanded} />
                          </button>

                          {/* 版本详情 */}
                          {isVersionExpanded && (
                            <div
                              className="px-4 py-3"
                              style={{
                                borderTop: '1px solid var(--color-border-light)',
                                backgroundColor: 'var(--color-bg-card)',
                              }}
                            >
                              <h4
                                className="m-0 mb-2"
                                style={{
                                  fontSize: '0.8rem',
                                  fontWeight: 600,
                                  color: 'var(--color-text-secondary)',
                                }}
                              >
                                更新内容
                              </h4>
                              <ul className="space-y-1.5 mb-3 m-0 p-0 list-none">
                                {v.changes.map((change, cidx) => (
                                  <li
                                    key={cidx}
                                    className="flex items-start gap-2"
                                    style={{
                                      fontSize: '0.85rem',
                                      color: 'var(--color-text-secondary)',
                                      lineHeight: 1.6,
                                    }}
                                  >
                                    <span
                                      style={{
                                        color: 'var(--color-primary)',
                                        marginTop: '4px',
                                        flexShrink: 0,
                                      }}
                                    >
                                      •
                                    </span>
                                    <span>{change}</span>
                                  </li>
                                ))}
                              </ul>
                              <a
                                href={v.apk}
                                download={v.apkName}
                                className="inline-flex items-center gap-2 px-3 py-1.5 font-semibold transition-opacity"
                                style={{
                                  backgroundColor: 'var(--color-primary)',
                                  color: 'var(--color-text-inverse)',
                                  borderRadius: '2px',
                                  fontSize: '0.8rem',
                                }}
                                onMouseEnter={(e) =>
                                  (e.currentTarget.style.opacity = '0.9')
                                }
                                onMouseLeave={(e) =>
                                  (e.currentTarget.style.opacity = '1')
                                }
                              >
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                                  <polyline points="7 10 12 15 17 10" />
                                  <line x1="12" y1="15" x2="12" y2="3" />
                                </svg>
                                下载 APK
                              </a>
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

/** 折叠箭头图标：展开时旋转 90° */
function ChevronIcon({ expanded }: { expanded: boolean }) {
  return (
    <svg
      className="flex-shrink-0 transition-transform"
      style={{
        width: '14px',
        height: '14px',
        color: 'var(--color-text-tertiary)',
        transform: expanded ? 'rotate(90deg)' : 'rotate(0deg)',
      }}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <polyline points="9 18 15 12 9 6" />
    </svg>
  );
}
