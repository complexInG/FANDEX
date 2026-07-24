/**
 * 性能监控面板客户端逻辑
 * -----------------------------------------------------------------------------
 * 从 PerformanceMonitor.astro 提取的客户端脚本，负责：
 * - 折叠/展开/关闭面板
 * - 渲染 Web Vitals 指标卡片（LCP/INP/CLS/TTFB/FCP）
 * - 渲染分位数汇总（p50/p75/p95）
 * - 渲染资源加载瀑布图（PerformanceObserver Resource Timing）
 * - 导出 JSON / 清空记录
 * - 定时刷新（2 秒）与 View Transitions 兼容清理
 *
 * 仅在开发环境执行；生产环境组件未渲染，此脚本不注入
 */

// 引入类型定义：避免使用 mod.VitalRecord 等命名空间形式（mod 为运行时变量，不可作为类型）
import type { VitalRecord, VitalName, VitalPercentiles } from '@services/observability-service';

/**
 * 清除 panel 上挂载的定时器
 * 用于页面切换、面板关闭、面板重新初始化前清理 setInterval，避免内存泄漏
 */
function clearMonitorInterval(panel: HTMLElement): void {
  const existing = panel.dataset.intervalId;
  if (existing) {
    const id = Number(existing);
    if (!Number.isNaN(id)) window.clearInterval(id);
    delete panel.dataset.intervalId;
  }
}

/** 初始化性能监控面板（首屏 + ClientRouter 跳转后） */
function initPerformanceMonitor(): void {
  const panel = document.getElementById('fandex-perf-monitor');
  if (!panel) return;

  // 先清除可能存在的旧定时器（Astro View Transitions 切换页面后再次初始化时清理）
  clearMonitorInterval(panel);

  const toggleBtn = document.getElementById('perf-monitor-toggle');
  const closeBtn = document.getElementById('perf-monitor-close');
  const vitalsGrid = document.getElementById('perf-vitals-grid');
  const summaryEl = document.getElementById('perf-summary');
  const waterfallEl = document.getElementById('perf-waterfall');
  const exportBtn = document.getElementById('perf-export');
  const clearBtn = document.getElementById('perf-clear');

  // 折叠/展开
  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      panel.classList.toggle('collapsed');
    });
  }

  // 关闭面板：同时清理定时器避免后台空跑
  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      panel.style.display = 'none';
      clearMonitorInterval(panel);
    });
  }

  // 动态导入 Service 层（避免 SSR 阶段加载）
  type ObservabilityModule = typeof import('@services/observability-service');
  async function loadObservability(): Promise<ObservabilityModule | null> {
    try {
      const mod = await import('@services/observability-service');
      return mod;
    } catch {
      return null;
    }
  }

  // 格式化毫秒数值
  function formatMs(value: number): string {
    if (!value || value === 0) return '—';
    if (value < 10) return value.toFixed(1) + 'ms';
    return Math.round(value) + 'ms';
  }

  // 格式化 CLS（无量纲小数）
  function formatCls(value: number): string {
    if (!value || value === 0) return '—';
    return value.toFixed(3);
  }

  // 根据 rating 获取 CSS 类名
  function ratingClass(rating: string): string {
    if (rating === 'good') return 'rating-good';
    if (rating === 'needs-improvement') return 'rating-needs-improvement';
    return 'rating-poor';
  }

  /**
   * HTML 特殊字符转义：用于将不可信文本安全嵌入 innerHTML 模板
   * @param str - 待转义的原始字符串
   * @returns 转义后的安全字符串（& < > " ' 已转为 HTML 实体）
   */
  function escapeHtml(str: string): string {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // 渲染当前页面 Web Vitals
  async function renderVitals(): Promise<void> {
    if (!vitalsGrid) return;
    const mod = await loadObservability();
    if (!mod) return;
    try {
      const all = mod.getVitals(20);
      // 按指标名称分组取最新一条
      const latest = new Map<string, VitalRecord>();
      for (const v of all) {
        if (!latest.has(v.name)) latest.set(v.name, v);
      }
      const names: VitalName[] = ['LCP', 'INP', 'CLS', 'TTFB', 'FCP'];
      const html = names
        .map((name) => {
          const v = latest.get(name);
          const value = v ? (name === 'CLS' ? formatCls(v.value) : formatMs(v.value)) : '—';
          const rating = v ? v.rating : 'good';
          return `
            <div class="perf-vital-card ${ratingClass(rating)}">
              <div class="perf-vital-name">${name}</div>
              <div class="perf-vital-value">${value}</div>
            </div>
          `;
        })
        .join('');
      vitalsGrid.innerHTML = html;
    } catch {
      vitalsGrid.innerHTML = '<p class="perf-empty">读取失败</p>';
    }
  }

  // 渲染汇总统计
  async function renderSummary(): Promise<void> {
    if (!summaryEl) return;
    const mod = await loadObservability();
    if (!mod) return;
    try {
      const s = mod.getVitalsSummary();
      const rows: Array<{ label: string; p: VitalPercentiles; fmt: (v: number) => string }> = [
        { label: 'LCP', p: s.lcp, fmt: formatMs },
        { label: 'INP', p: s.inp, fmt: formatMs },
        { label: 'CLS', p: s.cls, fmt: formatCls },
        { label: 'TTFB', p: s.ttfb, fmt: formatMs },
        { label: 'FCP', p: s.fcp, fmt: formatMs },
      ];
      const html = rows
        .map(
          (r) => `
          <div class="perf-summary-row">
            <span class="perf-summary-label">${r.label}</span>
            <span class="perf-summary-values">p50 ${r.fmt(r.p.p50)} · p75 ${r.fmt(r.p.p75)} · p95 ${r.fmt(r.p.p95)}</span>
          </div>
        `,
        )
        .join('');
      summaryEl.innerHTML = html;
    } catch {
      summaryEl.innerHTML = '<p class="perf-empty">读取失败</p>';
    }
  }

  // 资源瀑布图：通过 performance.getEntriesByType 读取资源加载记录
  // 数据来源为浏览器 Performance API，e.name 为资源 URL，经 escapeHtml 转义后嵌入 HTML 属性与文本
  function renderWaterfall(): void {
    if (!waterfallEl) return;
    try {
      const entries = performance.getEntriesByType('resource') as PerformanceResourceTiming[];
      // 取最近 20 项，按 startTime 排序
      const recent = entries.slice(-20).sort((a, b) => a.startTime - b.startTime);
      if (recent.length === 0) {
        waterfallEl.innerHTML = '<p class="perf-empty">暂无资源加载记录</p>';
        return;
      }
      const maxEnd = Math.max(...recent.map((e) => e.responseEnd));
      const minStart = Math.min(...recent.map((e) => e.startTime));
      const totalSpan = Math.max(maxEnd - minStart, 1);
      const html = recent
        .map((e) => {
          // 资源 URL 转义后用于 title 属性与显示文本，防止 URL 中特殊字符触发 XSS
          const safeName = escapeHtml(e.name.split('/').pop() || e.name);
          const safeTitle = escapeHtml(e.name);
          const left = ((e.startTime - minStart) / totalSpan) * 100;
          const width = Math.max((e.duration / totalSpan) * 100, 2);
          const duration =
            e.duration < 10 ? e.duration.toFixed(1) + 'ms' : Math.round(e.duration) + 'ms';
          return `
            <div class="perf-waterfall-item">
              <span class="perf-waterfall-name" title="${safeTitle}">${safeName}</span>
              <div class="perf-waterfall-bar-container">
                <div class="perf-waterfall-bar" style="left:${left}%;width:${width}%"></div>
              </div>
              <span class="perf-waterfall-duration">${duration}</span>
            </div>
          `;
        })
        .join('');
      waterfallEl.innerHTML = html;
    } catch {
      waterfallEl.innerHTML = '<p class="perf-empty">读取失败</p>';
    }
  }

  // 导出 JSON
  if (exportBtn) {
    exportBtn.addEventListener('click', async () => {
      const mod = await loadObservability();
      if (!mod) return;
      try {
        const json = mod.exportVitalsJSON();
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'fandex-web-vitals.json';
        a.click();
        URL.revokeObjectURL(url);
      } catch {
        // 异常时静默忽略
      }
    });
  }

  // 清空记录
  if (clearBtn) {
    clearBtn.addEventListener('click', async () => {
      const mod = await loadObservability();
      if (!mod) return;
      try {
        mod.clearVitals();
        await renderVitals();
        await renderSummary();
      } catch {
        // 异常时静默忽略
      }
    });
  }

  // 初次渲染
  void renderVitals();
  void renderSummary();
  renderWaterfall();

  // 定时刷新（每 2 秒）：将 intervalId 存入 dataset 便于页面切换/面板关闭时清理
  const intervalId = window.setInterval(() => {
    void renderVitals();
    void renderSummary();
    renderWaterfall();
  }, 2000);
  panel.dataset.intervalId = String(intervalId);
}

// Astro View Transitions 兼容：页面切换前清理旧定时器，避免累积内存泄漏
document.addEventListener('astro:before-swap', () => {
  const panel = document.getElementById('fandex-perf-monitor');
  if (panel) clearMonitorInterval(panel);
});
// 页面切换后重新初始化
document.addEventListener('astro:page-load', initPerformanceMonitor);
initPerformanceMonitor();
