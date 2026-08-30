/**
 * 模块矩阵展示区
 * 严格对齐 FANDEX-Web index.astro 的 category-section + feature-grid 风格：
 * - 分类折叠（category-header + category-toggle）
 * - 1px 网格分割线（grid + 1px gap + 背景色形成分割线）
 * - 模块卡片直角无边框，依赖网格线分隔
 * - 跨分类模块（HTML5/SVG）在对应分类下重复出现
 */
import { useState } from 'react';
import { categories, stats } from '../data/modules';

export function ModuleMatrix() {
  // 默认全部展开
  const [expandedCats, setExpandedCats] = useState<Set<string>>(
    new Set(categories.map((c) => c.id)),
  );

  const toggleCat = (id: string) => {
    setExpandedCats((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  return (
    <section
      id="modules"
      className="py-12 sm:py-16"
      style={{
        borderTop: '1px solid var(--color-border-light)',
        backgroundColor: 'var(--color-bg-card)',
      }}
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
            内容矩阵
          </h2>
          <p style={{ fontSize: '0.875rem', color: 'var(--color-text-secondary)' }}>
            覆盖 {stats.categoryCount} 大分类 · {stats.uniqueModuleCount} 个模块 ·{' '}
            {stats.totalDocuments} 篇代码语法速查文档
          </p>
        </div>

        {/* 分类列表：对齐 category-section */}
        <div className="space-y-4">
          {categories.map((cat) => {
            const isExpanded = expandedCats.has(cat.id);
            return (
              <div key={cat.id}>
                {/* 分类标题：对齐 category-header */}
                <button
                  type="button"
                  onClick={() => toggleCat(cat.id)}
                  className="w-full flex items-center justify-between py-2 transition-colors"
                  style={{
                    borderBottom: '1px solid var(--color-border)',
                  }}
                  aria-expanded={isExpanded}
                >
                  <div className="flex items-center gap-2">
                    <span
                      style={{
                        fontSize: '0.85rem',
                        fontWeight: 600,
                        color: cat.color,
                        letterSpacing: '0.04em',
                      }}
                    >
                      {cat.label}
                    </span>
                    <span
                      style={{
                        fontSize: '0.7rem',
                        fontFamily: 'var(--font-mono)',
                        color: 'var(--color-text-tertiary)',
                      }}
                    >
                      {cat.modules.length} 模块
                    </span>
                  </div>
                  <svg
                    className="transition-transform"
                    style={{
                      width: '14px',
                      height: '14px',
                      color: 'var(--color-text-tertiary)',
                      transform: isExpanded ? 'rotate(0deg)' : 'rotate(-90deg)',
                    }}
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    aria-hidden="true"
                  >
                    <polyline points="6 9 12 15 18 9" />
                  </svg>
                </button>

                {/* 模块网格：对齐 feature-grid，1px 网格分割线 */}
                {isExpanded && (
                  <div
                    style={{
                      display: 'grid',
                      gridTemplateColumns:
                        'repeat(auto-fill, minmax(220px, 1fr))',
                      gap: '1px',
                      backgroundColor: 'var(--color-border)',
                      border: '1px solid var(--color-border)',
                      marginTop: '-1px',
                    }}
                  >
                    {cat.modules.map((m, idx) => (
                      <div
                        key={`${cat.id}-${m.id}-${idx}`}
                        className="flex items-center justify-between px-3 py-2.5 transition-colors"
                        style={{
                          backgroundColor: 'var(--color-bg)',
                        }}
                        onMouseEnter={(e) =>
                          (e.currentTarget.style.backgroundColor =
                            'var(--color-bg-hover)')
                        }
                        onMouseLeave={(e) =>
                          (e.currentTarget.style.backgroundColor = 'var(--color-bg)')
                        }
                      >
                        <span
                          style={{
                            fontSize: '0.85rem',
                            fontWeight: 500,
                            color: 'var(--color-text)',
                          }}
                        >
                          {m.title}
                        </span>
                        <span
                          style={{
                            fontSize: '0.7rem',
                            fontFamily: 'var(--font-mono)',
                            color: 'var(--color-text-tertiary)',
                          }}
                        >
                          {m.docCount}
                        </span>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* 底部统计：对齐 FANDEX-Web footer-stats 风格 */}
        <div
          className="mt-8 pt-6 flex items-center justify-center gap-3 flex-wrap"
          style={{ borderTop: '1px solid var(--color-border-light)' }}
        >
          <span
            style={{
              fontSize: '0.8rem',
              fontFamily: 'var(--font-mono)',
              color: 'var(--color-text-tertiary)',
            }}
          >
            {stats.totalDocuments} 篇文档
          </span>
          <span style={{ color: 'var(--color-text-tertiary)' }}>·</span>
          <span
            style={{
              fontSize: '0.8rem',
              fontFamily: 'var(--font-mono)',
              color: 'var(--color-text-tertiary)',
            }}
          >
            {stats.uniqueModuleCount} 唯一模块
          </span>
          <span style={{ color: 'var(--color-text-tertiary)' }}>·</span>
          <span
            style={{
              fontSize: '0.8rem',
              fontFamily: 'var(--font-mono)',
              color: 'var(--color-text-tertiary)',
            }}
          >
            {stats.moduleEntries} 数组条目
          </span>
          <span style={{ color: 'var(--color-text-tertiary)' }}>·</span>
          <span
            style={{
              fontSize: '0.8rem',
              fontFamily: 'var(--font-mono)',
              color: 'var(--color-text-tertiary)',
            }}
          >
            HTML5 / SVG 跨 markup + frontend 双分类
          </span>
        </div>
      </div>
    </section>
  );
}
