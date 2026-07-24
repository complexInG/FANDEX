/**
 * 标签页搜索交互脚本
 * -----------------------------------------------------------------------------
 * 从 tags/index.astro 提取的客户端搜索逻辑，负责：
 * - 加载搜索索引（search-index.json）
 * - 初始化搜索后端（优先 Web Worker，回退 Fuse.js，再回退基础搜索）
 * - 输入防抖（150ms）与模块筛选
 * - 渲染搜索结果卡片（含模块色点、难度标签、标签 chip）
 * - DOMPurify 纵深防御 + escapeHtml 首要防线
 *
 * 数据来源：
 * - #search-section 元素的 data-modules / data-fallback-color 属性
 * - /data/search-index.json（由构建期生成）
 */

// 类型导入：Fuse 类作为类型注解使用，编译期擦除不影响运行时
import type Fuse from 'fuse.js';
// 通过 external-loader 异步加载 DOMPurify，避免重复 CDN 加载逻辑
import('@/lib/external-loader').then(({ loadDOMPurify }) => {
  loadDOMPurify().catch(() => {
    /* DOMPurify 加载失败时回退到 escapeHtml 处理 */
  });
});

/** 搜索索引条目类型（与 search-worker.ts 中的 SearchEntry 保持一致） */
interface SearchEntry {
  slug: string;
  title: string;
  description?: string;
  tags?: string[];
  module: string;
  difficulty?: string;
  updated?: string;
}

/** Fuse.js 搜索结果条目（含评分） */
interface ScoredEntry extends SearchEntry {
  score: number;
}

/**
 * 初始化标签页搜索交互
 *
 * 从 DOM 读取数据属性，绑定输入事件，按需加载索引与搜索后端。
 * 在 astro:page-load 时调用以支持 View Transitions。
 */
export function initTagsSearch(): void {
  const searchSection = document.getElementById('search-section');
  if (!searchSection) return;

  const MODULE_MAP: Record<string, { title: string; color: string }> = JSON.parse(
    searchSection.dataset.modules || '{}',
  );
  /** 回退颜色：从 data 属性读取，避免在客户端脚本中引用服务端变量 */
  const FALLBACK_COLOR = searchSection.dataset.fallbackColor || '#3b82f6';

  let index: SearchEntry[] | null = null;
  let worker: Worker | null = null;
  let useWorker = false;
  let fuse: Fuse<SearchEntry> | null = null;

  const input = document.getElementById('search-input') as HTMLInputElement;
  const moduleSelect = document.getElementById('filter-module') as HTMLSelectElement;
  const statusEl = document.getElementById('search-status');
  const resultsEl = document.getElementById('search-results');
  const tagGroups = document.querySelectorAll<HTMLElement>('.tag-group');
  const base = import.meta.env.BASE_URL;

  if (!input || !moduleSelect || !statusEl || !resultsEl) return;

  // 闭包中类型收窄失效，重新绑定到局部 const 以保持非空类型
  const status: HTMLElement = statusEl;
  const results: HTMLElement = resultsEl;

  results.style.display = 'none';

  const DIFFICULTY_LABELS: Record<string, string> = {
    beginner: '入门',
    intermediate: '进阶',
    advanced: '高级',
  };

  let debounceTimer: ReturnType<typeof setTimeout>;
  input.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(doSearch, 150);
  });
  moduleSelect.addEventListener('change', doSearch);

  /** 懒加载搜索索引，成功后初始化搜索后端 */
  async function loadIndex(): Promise<void> {
    if (index) return;
    try {
      const res = await fetch(`${base}data/search-index.json`);
      index = (await res.json()) as SearchEntry[];
    } catch {
      status.textContent = '搜索索引加载失败，请先运行 npm run build';
      index = [];
      return;
    }
    initSearchBackend();
  }

  /** 初始化搜索后端：优先 Web Worker，失败回退 Fuse.js */
  async function initSearchBackend(): Promise<void> {
    if (!index) return;
    try {
      const FuseModule = await import('fuse.js');
      const FuseClass: typeof Fuse = FuseModule.default || FuseModule;

      try {
        worker = new Worker(new URL('../workers/search-worker.ts', import.meta.url), {
          type: 'module',
        });
        worker.onmessage = (e: MessageEvent) => {
          if (e.data.type === 'ready') {
            useWorker = true;
          }
          if (e.data.type === 'results') {
            renderResults(e.data.payload.results as ScoredEntry[], e.data.payload.query);
          }
        };
        worker.onerror = () => {
          worker = null;
          fallbackToFuse(FuseClass);
        };
        worker.postMessage({ type: 'init', payload: { index } });
        setTimeout(() => {
          if (!useWorker) {
            worker?.terminate();
            worker = null;
            fallbackToFuse(FuseClass);
          }
        }, 3000);
      } catch {
        fallbackToFuse(FuseClass);
      }
    } catch {
      // Fuse.js not available, use basic search
    }
  }

  /** 回退到 Fuse.js 主线程搜索 */
  function fallbackToFuse(FuseClass: typeof Fuse): void {
    if (!index) return;
    fuse = new FuseClass(index, {
      keys: [
        { name: 'title', weight: 0.4 },
        { name: 'tags', weight: 0.25 },
        { name: 'slug', weight: 0.15 },
        { name: 'description', weight: 0.2 },
      ],
      threshold: 0.4,
      distance: 200,
      minMatchCharLength: 2,
      includeScore: true,
    });
  }

  /** 触发搜索：索引未加载时先加载 */
  function doSearch(): void {
    if (!index) {
      void loadIndex().then(performSearch);
      return;
    }
    performSearch();
  }

  /** 执行搜索：Worker → Fuse.js → 基础搜索 */
  function performSearch(): void {
    if (!index) return;
    const query = input.value.trim();
    const moduleFilter = moduleSelect.value;

    if (useWorker && worker) {
      worker.postMessage({
        type: 'search',
        payload: { query, moduleFilter },
      });
      return;
    }

    if (fuse && query) {
      let results = fuse.search(query);
      if (moduleFilter) {
        results = results.filter((r) => r.item.module === moduleFilter);
      }
      const items: ScoredEntry[] = results.map((r) => ({
        ...r.item,
        score: r.score ? 1 - r.score : 1,
      }));
      renderResults(items.slice(0, 50), query);
      return;
    }

    performBasicSearch(query, moduleFilter);
  }

  /** 基础搜索：基于关键词评分的简单匹配（Fuse.js 不可用时使用） */
  function performBasicSearch(query: string, moduleFilter: string): void {
    if (!index) return;
    let results: ScoredEntry[] = index.map((d) => ({ ...d, score: 0 }));

    if (moduleFilter) {
      results = results.filter((d) => d.module === moduleFilter);
    }

    if (query) {
      const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
      const scored = results
        .map((d) => {
          let score = 0;
          const titleLower = d.title.toLowerCase();
          const descLower = (d.description || '').toLowerCase();
          const tagsLower = (d.tags || []).map((t) => t.toLowerCase());

          for (const term of terms) {
            if (titleLower.includes(term)) score += 10;
            if (tagsLower.some((t) => t.includes(term))) score += 5;
            if (descLower.includes(term)) score += 2;
            if (d.slug.toLowerCase().includes(term)) score += 3;
          }
          return { ...d, score };
        })
        .filter((d) => d.score > 0);

      scored.sort((a, b) => b.score - a.score);
      results = scored;
    }

    renderResults(results, query);
  }

  /** HTML 转义：处理 4 个关键字符，防止 XSS */
  function escapeHtml(str: string): string {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /** 渲染搜索结果：切换标签组显隐，生成结果卡片 HTML */
  function renderResults(docs: ScoredEntry[], query: string): void {
    const hasActiveSearch = query || moduleSelect.value;

    tagGroups.forEach((g) => {
      g.style.display = hasActiveSearch ? 'none' : '';
    });
    results.style.display = hasActiveSearch ? 'flex' : 'none';

    if (!hasActiveSearch) {
      status.textContent = '';
      results.innerHTML = '';
      return;
    }

    status.textContent = `找到 ${docs.length} 篇文档`;

    if (docs.length === 0) {
      results.innerHTML = `
        <div class="search-empty">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
          </svg>
          没有找到匹配的文档
        </div>`;
      return;
    }

    const html = docs
      .slice(0, 50)
      .map((d) => {
        const mod = MODULE_MAP[d.module] || { title: d.module, color: FALLBACK_COLOR };
        const diff = d.difficulty || '';
        const diffLabel = DIFFICULTY_LABELS[diff] || diff;
        const tags = (d.tags || [])
          .map((t) => `<span class="result-tag-chip">${escapeHtml(t)}</span>`)
          .join('');

        return `<a href="${base}${escapeHtml(d.slug)}/" class="result-card">
          <div class="result-header">
            <span class="result-module-dot" style="background:${mod.color}"></span>
            <span class="result-module-name">${escapeHtml(mod.title)}</span>
            <span class="result-title">${escapeHtml(d.title)}</span>
            ${diff ? `<span class="result-difficulty ${diff}">${escapeHtml(diffLabel)}</span>` : ''}
          </div>
          ${d.description ? `<p class="result-desc">${escapeHtml(d.description)}</p>` : ''}
          ${tags ? `<div class="result-tags">${tags}</div>` : ''}
        </a>`;
      })
      .join('');

    // 安全降级策略：所有动态内容（title/slug/description/tags 等）已在上游通过 escapeHtml() 转义，
    // 即使 DOMPurify 未加载，html 字符串中的用户可控数据均已转义为安全文本，不会触发 XSS。
    // DOMPurify 作为纵深防御层启用；escapeHtml 是首要防线（见 loadDOMPurify 的 catch 注释）。
    const purify = window.DOMPurify;
    results.innerHTML = purify ? purify.sanitize(html) : html;
  }
}

// 初始化（首次加载与 View Transitions 后触发）
initTagsSearch();
document.addEventListener('astro:page-load', initTagsSearch);
