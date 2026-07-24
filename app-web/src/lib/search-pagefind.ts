/**
 * 搜索页 Pagefind 初始化脚本
 * -----------------------------------------------------------------------------
 * 从 pages/search.astro 提取的客户端逻辑，负责：
 * - 动态加载 Pagefind 搜索库（生产环境从 /pagefind/pagefind.js 加载）
 * - 初始化 Pagefind UI 实例并挂载到 #search 容器
 * - 绑定模块/难度筛选器的 change 事件
 * - 支持 URL 参数 q 自动触发搜索
 * - View Transitions 兼容（astro:page-load / astro:before-swap 生命周期管理）
 *
 * 防重复初始化策略：
 * - pagefindInitialized 标志位：防止 astro:page-load 重复触发
 * - filterCleanups 清理数组：astro:before-swap 时移除事件监听器
 *
 * 开发模式降级：
 * - 开发模式下未生成搜索索引，显示提示信息引导用户运行 build
 */

/** Pagefind 模块类型（运行时动态导入，类型内联定义） */
interface PagefindModule {
  options(opts: Record<string, string>): Promise<void>;
  init(): Promise<void>;
  UI: new (config: { element: string; showSubResults: boolean; showImages: boolean }) => {
    filter(filters: Record<string, string>): void;
    triggerSearch(query: string): void;
  };
}

/** Pagefind 初始化守卫：避免 astro:page-load 与直接调用导致重复实例化 */
let pagefindInitialized = false;

/** 保存当前 filter change 监听器引用，便于 astro:before-swap 时移除 */
let filterCleanups: Array<() => void> = [];

/**
 * 初始化 Pagefind 搜索
 *
 * 核心执行流程：
 *   1. 检查 pagefindInitialized 标志，已初始化则跳过
 *   2. 开发模式显示降级提示（搜索索引仅 build 后生成）
 *   3. 动态导入 pagefind.js，配置 baseUrl/basePath
 *   4. 创建 UI 实例，绑定筛选器 change 事件
 *   5. 检查 URL 参数 q，自动触发搜索
 *   6. 标记 pagefindInitialized = true
 *
 * 异常处理：
 *   - 导入失败时显示"搜索索引尚未构建"提示
 */
async function initPagefind(): Promise<void> {
  // 已初始化则跳过，防止重复实例化造成 UI 重叠与内存泄漏
  if (pagefindInitialized) return;
  const base = import.meta.env.BASE_URL;
  const searchEl = document.getElementById('search');
  if (!searchEl) return;

  if (import.meta.env.DEV) {
    searchEl.innerHTML =
      '<p style="color:var(--color-text-tertiary);text-align:center;padding:2em;">开发模式下未生成搜索索引，请运行 npm run build 后使用。</p>';
    return;
  }

  try {
    const pagefind = (await import(
      /* @vite-ignore */ `${base}pagefind/pagefind.js`
    )) as PagefindModule;
    await pagefind.options({ baseUrl: base, basePath: `${base}pagefind/` });
    await pagefind.init();

    const ui = new pagefind.UI({
      element: '#search',
      showSubResults: true,
      showImages: false,
    });

    const filterModule = document.getElementById('filter-module') as HTMLSelectElement;
    const filterDifficulty = document.getElementById('filter-difficulty') as HTMLSelectElement;

    function applyFilters(): void {
      const filters: Record<string, string> = {};
      if (filterModule?.value) filters.module = filterModule.value;
      if (filterDifficulty?.value) filters.difficulty = filterDifficulty.value;
      if (Object.keys(filters).length > 0) {
        ui.filter(filters);
      } else {
        ui.filter({});
      }
    }

    filterModule?.addEventListener('change', applyFilters);
    filterDifficulty?.addEventListener('change', applyFilters);
    // 记录清理函数：before-swap 时调用，移除 change 监听器避免孤立引用
    filterCleanups = [
      () => filterModule?.removeEventListener('change', applyFilters),
      () => filterDifficulty?.removeEventListener('change', applyFilters),
    ];

    const params = new URLSearchParams(window.location.search);
    const q = params.get('q');
    if (q) {
      ui.triggerSearch(q);
    }
    // 标记已初始化，防止 astro:page-load 二次触发重复构建 UI
    pagefindInitialized = true;
  } catch {
    searchEl.innerHTML =
      '<p style="color:var(--color-text-tertiary);text-align:center;padding:2em;">搜索索引尚未构建，请先运行 npm run build</p>';
  }
}

// 注册 astro:page-load 初始化
document.addEventListener('astro:page-load', initPagefind);

// 页面切换前清理：移除 filter 监听器与 pagefind 初始化标记，允许新页面重新初始化
document.addEventListener(
  'astro:before-swap',
  () => {
    filterCleanups.forEach((cleanup) => cleanup());
    filterCleanups = [];
    pagefindInitialized = false;
    document.removeEventListener('astro:page-load', initPagefind);
  },
  { once: true }
);
