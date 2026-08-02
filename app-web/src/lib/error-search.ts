/**
 * 404 错误页交互脚本
 * -----------------------------------------------------------------------------
 * 由 pages/404.astro 引入，负责：
 * - 展示当前失效路径（借鉴主流文档站 404 的「死链路径」惯例）
 * - 根据路径段生成「你可能想访问」智能建议
 * - 全模块卡片搜索过滤（默认仅展示前 12 个，搜索时展开全部命中项）
 * - 键盘交互：/ 聚焦搜索、Enter 打开首个结果、Esc 清空
 *
 * 触发时机：
 * - 脚本首次加载时执行一次
 * - astro:page-load 事件触发时重新绑定（兼容 View Transitions 路由切换）
 *
 * 注：404 页面为独立 HTML（未使用 Layout 组件），故无 View Transitions，
 * 但保留 astro:page-load 监听以与其他页面脚本保持一致的初始化模式。
 */

/** 默认可见的模块卡片数量，避免 46 个模块一次性撑满首屏 */
const DEFAULT_VISIBLE_COUNT = 12;

/** 智能建议所需的轻量元数据（由页面 data-suggest-meta 注入） */
interface SuggestMeta {
  /** 站点基础路径，如 /FANDEX/ */
  base: string;
  /** 全部模块 id 与标题 */
  modules: Array<{ id: string; title: string }>;
  /** 已配置学习路径地图的模块 id 列表 */
  learningPaths: string[];
}

/** 智能建议链接项 */
interface SuggestLink {
  label: string;
  href: string;
}

/**
 * 读取页面注入的建议元数据
 * @returns 解析后的元数据；缺失或损坏时返回 null
 */
function readSuggestMeta(): SuggestMeta | null {
  const raw = document.body.dataset.suggestMeta;
  if (!raw) return null;
  try {
    return JSON.parse(raw) as SuggestMeta;
  } catch {
    return null;
  }
}

/**
 * 将当前路径解析为相对基础路径的路径段
 * 例如 /FANDEX/learning-path/vue3/1 -> ['learning-path', 'vue3', '1']
 * @param meta - 站点元数据（含 base）
 * @returns 非空路径段数组
 */
function pathSegments(meta: SuggestMeta): string[] {
  const path = window.location.pathname;
  let rest = path;
  if (meta.base && meta.base !== '/' && path.startsWith(meta.base)) {
    rest = path.slice(meta.base.length);
  } else {
    rest = rest.replace(/^\/+/, '');
  }
  return rest.split('/').filter(Boolean);
}

/**
 * 展示用户实际访问的失效路径
 * 文案结构参考主流文档站 404：明确写出「不存在的链接」便于用户核对输入
 */
function renderPath(): void {
  const block = document.getElementById('error-path-block');
  const value = document.getElementById('error-path-value');
  if (!block || !value) return;
  value.textContent = window.location.pathname;
  block.hidden = false;
}

/**
 * 根据路径段生成智能建议链接
 * 规则：
 * - /learning-path/<tech>/...：tech 已配置地图时指向该技术学习路径，否则指向总览
 * - /syntax/...、/playground/...：指向对应功能页
 * - /<module>/...：指向该模块首页（slug 不存在或已改名时最接近的入口）
 * - 其他情况：展示学习路径 / 语法速查 / 在线编程三个默认入口
 */
function renderSuggestions(): void {
  const meta = readSuggestMeta();
  const block = document.getElementById('error-suggest');
  const list = document.getElementById('error-suggest-links');
  if (!meta || !block || !list) return;

  const segments = pathSegments(meta);
  const links: SuggestLink[] = [];

  if (segments[0] === 'learning-path') {
    const tech = segments[1];
    const techMeta = meta.modules.find((m) => m.id === tech);
    if (tech && meta.learningPaths.includes(tech)) {
      links.push({
        label: `${techMeta?.title ?? tech} 学习路径`,
        href: `${meta.base}learning-path/${tech}/`,
      });
    } else {
      links.push({ label: '学习路径总览', href: `${meta.base}learning-path/` });
    }
  } else if (segments[0] === 'syntax') {
    links.push({ label: '语法速查', href: `${meta.base}syntax/` });
  } else if (segments[0] === 'playground') {
    links.push({ label: '在线编程', href: `${meta.base}playground/` });
  } else if (segments[0]) {
    const mod = meta.modules.find((m) => m.id === segments[0]);
    if (mod) {
      links.push({ label: `${mod.title} 模块首页`, href: `${meta.base}${mod.id}/` });
    }
  }

  // 未命中任何规则时提供三个全局入口作为兜底
  if (links.length === 0) {
    links.push(
      { label: '学习路径', href: `${meta.base}learning-path/` },
      { label: '语法速查', href: `${meta.base}syntax/` },
      { label: '在线编程', href: `${meta.base}playground/` },
    );
  }

  // 渲染建议链接（每次重建，避免累积旧节点）
  list.replaceChildren();
  for (const link of links) {
    const anchor = document.createElement('a');
    anchor.className = 'error-suggest-link';
    anchor.href = link.href;
    anchor.textContent = link.label;
    list.appendChild(anchor);
  }
  block.hidden = false;
}

/**
 * 初始化 404 页面交互
 *
 * 实现要点：
 * - 读取 #error-search-input 与 #error-modules 元素
 * - 输入为空时恢复默认展示（前 DEFAULT_VISIBLE_COUNT 个）
 * - 输入非空时按 data-search 全文匹配并展示全部命中卡片
 * - Enter 打开第一个可见卡片，Esc 清空，/ 聚焦输入框
 */
function initErrorSearch(): void {
  const input = document.getElementById('error-search-input') as HTMLInputElement | null;
  const modulesEl = document.getElementById('error-modules');
  const countEl = document.getElementById('error-search-count');
  const metaEl = document.getElementById('error-search-meta');
  const emptyEl = document.getElementById('error-empty');
  const clearBtn = document.getElementById('error-search-clear');
  if (!input || !modulesEl) return;

  const cards = Array.from(modulesEl.querySelectorAll<HTMLAnchorElement>('.error-module-card'));

  // 每次初始化都刷新路径与建议，保证路由切换后数据一致
  renderPath();
  renderSuggestions();

  /** 恢复默认展示：前 12 个可见，其余折叠 */
  const reset = (): void => {
    cards.forEach((card, index) => {
      card.classList.toggle('is-extra', index >= DEFAULT_VISIBLE_COUNT);
      card.classList.remove('is-hidden');
    });
    if (metaEl) metaEl.hidden = true;
    if (emptyEl) emptyEl.hidden = true;
  };

  /** 按关键词过滤模块卡片，并同步计数与空状态 */
  const applyQuery = (query: string): void => {
    const keyword = query.trim().toLowerCase();
    if (!keyword) {
      reset();
      return;
    }

    let matchCount = 0;
    cards.forEach((card) => {
      const searchText = (card.dataset.search || '').toLowerCase();
      const matched = searchText.includes(keyword);
      card.classList.toggle('is-hidden', !matched);
      // 命中项即使位于前 12 个之外也展开显示
      if (matched) card.classList.remove('is-extra');
      if (matched) matchCount += 1;
    });

    if (countEl) countEl.textContent = `匹配 ${matchCount} 个模块`;
    if (metaEl) metaEl.hidden = false;
    if (emptyEl) emptyEl.hidden = matchCount > 0;
  };

  input.addEventListener('input', () => applyQuery(input.value));

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      input.value = '';
      input.focus();
      reset();
    });
  }

  input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      const firstVisible = cards.find((card) => !card.classList.contains('is-hidden'));
      if (firstVisible) {
        window.location.href = firstVisible.href;
      }
    }
    if (event.key === 'Escape') {
      input.value = '';
      reset();
    }
  });

  // 全局 / 快捷键聚焦搜索（输入类元素内不触发）
  document.addEventListener('keydown', (event) => {
    if (event.key !== '/' || document.activeElement === input) return;
    const tag = (document.activeElement?.tagName || '').toLowerCase();
    const active = document.activeElement as HTMLElement | null;
    if (tag === 'input' || tag === 'textarea' || active?.isContentEditable) return;
    event.preventDefault();
    input.focus();
  });

  reset();
}

// 初始化
initErrorSearch();
document.addEventListener('astro:page-load', initErrorSearch);
