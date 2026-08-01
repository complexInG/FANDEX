/**
 * 语法速览交互岛（SyntaxExplorer）
 * =============================================================================
 * 功能概述：
 * - 语言切换：通过彩色语言 chip 过滤语法卡片（无搜索，遵循"速查做减法"）
 * - 按需加载：卡片数据按语言拆分到 public/syntax-data/<module>.json，
 *   切换语言时 fetch 对应分块并缓存，避免页面内嵌 2MB 数据
 * - 代码复制：卡片代码块提供复制按钮（Clipboard API，失败静默降级）
 * - 分批渲染：每批渲染 PAGE_SIZE 张卡片，"加载更多"增量展开，保证滚动流畅
 *
 * 数据流：
 *   languages prop（页面内嵌索引）→ activeId state → fetch 语言分块
 *   → cards state → 过滤后分批渲染
 *
 * 设计说明：
 * - 并发保护：请求序号 ref 保证快速切换语言时旧响应不会覆盖新状态
 * - 缓存：已加载语言分块存于 Map ref，再次切换零网络开销
 * - 无障碍：chip 使用 aria-pressed，状态区使用 aria-live 播报加载结果
 */

import { useEffect, useRef, useState, type CSSProperties } from 'react';
import '@/styles/islands/syntax-explorer.css';

/** 语法速览语言元数据（与 syntax-service 类型一致） */
interface SyntaxLanguage {
  id: string;
  title: string;
  color: string;
  count: number;
  docCount: number;
}

/** 单张语法速查卡片 */
interface SyntaxCard {
  id: string;
  docTitle: string;
  section: string;
  name: string;
  formula: string;
  code: string;
  lang: string;
  truncated: boolean;
}

/** 语言分块 JSON 结构（scripts/build-syntax.mjs 输出） */
interface SyntaxLanguageData {
  module: string;
  cards: SyntaxCard[];
}

/** SyntaxExplorer 组件入参 */
interface SyntaxExplorerProps {
  /** 语言索引列表（由页面通过 syntax-service 提供） */
  languages: SyntaxLanguage[];
  /** 站点 base 路径（GitHub Pages 为 /FANDEX/），用于拼接数据与文档链接 */
  base: string;
}

/** 单批渲染的卡片数量：兼顾首屏密度与滚动性能 */
const PAGE_SIZE = 36;
/** 复制成功提示持续时长（毫秒） */
const COPIED_MS = 1600;

/** 未指定语言时的默认选中项（优先常用语言） */
const DEFAULT_LANGUAGE = 'javascript';

/**
 * 语法速览交互岛
 * 提供语言切换、按需加载、卡片渲染与代码复制能力
 */
export function SyntaxExplorer({ languages, base }: SyntaxExplorerProps) {
  /** 当前选中的语言 ID */
  const [activeId, setActiveId] = useState<string>(
    () =>
      languages.find((lang) => lang.id === DEFAULT_LANGUAGE)?.id ??
      languages[0]?.id ??
      '',
  );
  /** 当前语言的卡片列表；null 表示尚未加载完成 */
  const [cards, setCards] = useState<SyntaxCard[] | null>(null);
  /** 是否正在加载语言分块 */
  const [loading, setLoading] = useState(false);
  /** 加载失败信息；为空表示正常 */
  const [error, setError] = useState('');
  /** 当前可见卡片数量（分批渲染） */
  const [visibleCount, setVisibleCount] = useState(PAGE_SIZE);
  /** 最近一次复制成功的卡片 ID，用于按钮反馈 */
  const [copiedId, setCopiedId] = useState('');
  /** 已加载语言分块缓存：切换回已访问语言时零网络开销 */
  const cacheRef = useRef<Map<string, SyntaxCard[]>>(new Map());
  /** 请求序号：防止快速切换时旧响应覆盖新语言状态 */
  const requestSeqRef = useRef(0);
  /** 复制反馈定时器句柄（组件卸载时清理） */
  const copiedTimerRef = useRef<number | undefined>(undefined);

  const active = languages.find((lang) => lang.id === activeId);
  const activeColor = active?.color || 'var(--color-accent-base)';

  /**
   * 切换语言：清空旧卡片并触发对应分块加载
   * @param id - 目标语言 ID
   */
  function selectLanguage(id: string): void {
    if (id === activeId) return;
    setActiveId(id);
  }

  /**
   * 复制卡片代码到剪贴板
   * @param card - 目标卡片（含代码与 ID）
   */
  async function copyCode(card: SyntaxCard): Promise<void> {
    try {
      await navigator.clipboard.writeText(card.code);
      setCopiedId(card.id);
      window.clearTimeout(copiedTimerRef.current);
      copiedTimerRef.current = window.setTimeout(() => {
        setCopiedId((current) => (current === card.id ? '' : current));
      }, COPIED_MS);
    } catch {
      // 剪贴板权限不可用时静默降级，不打断用户操作
    }
  }

  /**
   * 加载语言分块并更新卡片状态
   * 使用请求序号防止竞态：仅当响应仍是最新请求时写入状态
   * @param id - 语言 ID
   */
  async function loadLanguage(id: string): Promise<void> {
    const seq = ++requestSeqRef.current;
    // 已缓存数据直接渲染，无需网络请求
    const cached = cacheRef.current.get(id);
    if (cached) {
      setCards(cached);
      setLoading(false);
      setError('');
      setVisibleCount(PAGE_SIZE);
      return;
    }
    setLoading(true);
    setError('');
    setVisibleCount(PAGE_SIZE);
    try {
      const response = await fetch(`${base}syntax-data/${id}.json`, {
        // 静态分块不可变，允许浏览器复用缓存
        cache: 'force-cache',
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const data = (await response.json()) as SyntaxLanguageData;
      const cardList = Array.isArray(data.cards) ? data.cards : [];
      cacheRef.current.set(id, cardList);
      // 竞态保护：仅最新请求可写入状态
      if (seq !== requestSeqRef.current) return;
      setCards(cardList);
    } catch {
      if (seq !== requestSeqRef.current) return;
      setError('语法数据加载失败，请稍后重试或切换其他语言');
    } finally {
      if (seq === requestSeqRef.current) setLoading(false);
    }
  }

  // 语言切换或首次挂载时加载对应分块
  useEffect(() => {
    if (!activeId) return;
    void loadLanguage(activeId);
    // 组件卸载时清理复制反馈定时器
    return () => window.clearTimeout(copiedTimerRef.current);
  }, [activeId]);

  const visibleCards = cards?.slice(0, visibleCount) ?? [];

  return (
    <div className="syntax-explorer">
      {/* 语言切换区：彩色 chip 导航，颜色跟随模块分类主题色 */}
      <nav className="syntax-langs" aria-label="语法语言切换">
        {languages.map((lang) => {
          const isActive = lang.id === activeId;
          return (
            <button
              key={lang.id}
              type="button"
              className={`syntax-lang-chip${isActive ? ' is-active' : ''}`}
              style={{ '--lang-color': lang.color } as CSSProperties}
              aria-pressed={isActive}
              onClick={() => selectLanguage(lang.id)}
            >
              <span className="syntax-lang-dot" aria-hidden="true" />
              <span className="syntax-lang-name">{lang.title}</span>
              <span className="syntax-lang-count">{lang.count}</span>
            </button>
          );
        })}
      </nav>

      {/* 当前语言元信息：供屏幕阅读器播报加载状态 */}
      <div className="syntax-meta" aria-live="polite">
        {loading
          ? '正在加载语法卡片'
          : active
            ? `${active.title} · ${active.count} 个语法点 · 来自 ${active.docCount} 篇文档`
            : ''}
      </div>

      {/* 加载失败提示 */}
      {error && (
        <div className="syntax-error" role="alert">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10" />
            <line x1="12" y1="8" x2="12" y2="12" />
            <line x1="12" y1="16" x2="12.01" y2="16" />
          </svg>
          <span>{error}</span>
        </div>
      )}

      {/* 卡片网格：分批渲染，保持首屏与滚动性能 */}
      {cards && cards.length > 0 && (
        <>
          <div className="syntax-grid">
            {visibleCards.map((card, index) => (
              <article
                className="syntax-card"
                key={card.id}
                style={
                  {
                    '--lang-color': activeColor,
                    animationDelay: `${Math.min(index, 12) * 24}ms`,
                  } as CSSProperties
                }
              >
                {/* 卡片头部：语言徽标 + 来源文档 */}
                <div className="syntax-card__top">
                  <span className="syntax-card__badge" style={{ backgroundColor: activeColor }}>
                    {active?.title}
                  </span>
                  <span className="syntax-card__doc" title={card.docTitle}>
                    {card.docTitle}
                  </span>
                </div>

                {/* 语法要点：小节标题 + 写法名称 + 行内公式 */}
                <h3 className="syntax-card__section">{card.section}</h3>
                <p className="syntax-card__name">{card.name}</p>
                {card.formula && <code className="syntax-card__formula">{card.formula}</code>}

                {/* 示例代码：语言标签 + 复制按钮 + 代码区 */}
                <div className="syntax-card__code">
                  <div className="syntax-card__codebar">
                    <span className="syntax-card__lang">{card.lang}</span>
                    <button
                      type="button"
                      className="syntax-card__copy"
                      aria-label={copiedId === card.id ? '已复制' : '复制代码'}
                      onClick={() => void copyCode(card)}
                    >
                      {copiedId === card.id ? (
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                          <polyline points="20 6 9 17 4 12" />
                        </svg>
                      ) : (
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <rect x="9" y="9" width="13" height="13" rx="2" />
                          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
                        </svg>
                      )}
                      <span>{copiedId === card.id ? '已复制' : '复制'}</span>
                    </button>
                  </div>
                  <pre className="syntax-card__pre">
                    <code>{card.code}</code>
                  </pre>
                  {card.truncated && (
                    <div className="syntax-card__truncated">示例已省略，详见完整文档</div>
                  )}
                </div>

                {/* 卡片底部：跳转完整模块文档 */}
                <a className="syntax-card__link" href={`${base}${active?.id}/`}>
                  <span>查看 {active?.title} 完整文档</span>
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <line x1="5" y1="12" x2="19" y2="12" />
                    <polyline points="12 5 19 12 12 19" />
                  </svg>
                </a>
              </article>
            ))}
          </div>

          {/* 增量加载：未展示完时提供"加载更多" */}
          {visibleCount < cards.length && (
            <button
              type="button"
              className="syntax-more"
              onClick={() => setVisibleCount((current) => current + PAGE_SIZE)}
            >
              加载更多（剩余 {cards.length - visibleCount} 条）
            </button>
          )}
        </>
      )}

      {/* 空数据兜底：语言分块为空时提示（正常情况不会出现） */}
      {!loading && !error && cards && cards.length === 0 && (
        <div className="syntax-empty">该语言暂无速查卡片</div>
      )}
    </div>
  );
}

export default SyntaxExplorer;
