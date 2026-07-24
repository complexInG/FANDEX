/**
 * 学习路径页面交互脚本
 * -----------------------------------------------------------------------------
 * 从 roadmap.astro 提取的客户端交互逻辑，负责：
 * - 路径选择 Tab 切换
 * - 从 services 异步获取路径进度
 * - 渲染模块时间线与进度条
 * - 监听 astro:page-load 以支持 View Transitions
 *
 * 使用方式：在 roadmap.astro 中通过 <script> 标签 import 本模块即可触发执行
 */

/** 优先级标签映射（运行时从 JSON 注入） */
let priorityLabels: Record<string, string> = {
  required: '必学',
  recommended: '推荐',
  optional: '可选',
};
/** 优先级颜色映射（运行时从 JSON 注入） */
let priorityColors: Record<string, string> = {
  required: '#ef4444',
  recommended: '#f59e0b',
  optional: '#6b7280',
};

/** 模块元数据映射（从全局 modules 数组构建，用于显示模块名） */
interface ModuleMeta {
  id: string;
  title: string;
  description: string;
}
let moduleMap: Map<string, ModuleMeta> = new Map();

/** 基础路径 */
const base = import.meta.env.BASE_URL;

/**
 * 从页面注入的 JSON 脚本中读取优先级映射
 */
function loadInjectedData(): void {
  const labelsEl = document.getElementById('priority-labels');
  const colorsEl = document.getElementById('priority-colors');
  if (labelsEl?.textContent) {
    try {
      priorityLabels = JSON.parse(labelsEl.textContent) as Record<string, string>;
    } catch {
      /* 使用默认值 */
    }
  }
  if (colorsEl?.textContent) {
    try {
      priorityColors = JSON.parse(colorsEl.textContent) as Record<string, string>;
    } catch {
      /* 使用默认值 */
    }
  }
}

/**
 * 从页面 HTML 中提取模块元数据（基于 .roadmap-module-card 元素的 data-progress-module 属性与文本）
 */
function buildModuleMap(): void {
  moduleMap = new Map();
  document.querySelectorAll('[data-progress-module]').forEach((card) => {
    const el = card as HTMLElement;
    const moduleId = el.getAttribute('data-progress-module');
    if (!moduleId) return;
    const titleEl = el.querySelector('.rm-title');
    const descEl = el.querySelector('.rm-desc');
    moduleMap.set(moduleId, {
      id: moduleId,
      title: titleEl?.textContent ?? moduleId,
      description: descEl?.textContent ?? '',
    });
  });
}

/**
 * 激活指定路径 Tab，并触发详情渲染
 * @param pathId - 路径 ID
 * @param pathName - 路径名称（用于显示）
 */
async function selectPath(pathId: string, pathName: string): Promise<void> {
  // 更新 Tab 状态
  document.querySelectorAll('.path-tab').forEach((tab) => {
    const el = tab as HTMLElement;
    el.setAttribute('aria-selected', el.dataset.pathId === pathId ? 'true' : 'false');
  });

  // 显示加载状态
  const detailEl = document.getElementById('path-detail');
  if (!detailEl) return;
  detailEl.innerHTML = '<div class="path-detail-loading">加载路径数据...</div>';

  try {
    // 动态导入 service（避免 SSR 阶段加载）
    const [{ getPathProgress }] = await Promise.all([import('@/services/learning-path-service')]);

    const progress = await getPathProgress(pathId);

    renderPathDetail(pathName, progress);
  } catch {
    detailEl.innerHTML = '<div class="path-detail-loading">加载失败，请刷新页面重试</div>';
  }
}

/** 路径进度数据结构（与服务端 getPathProgress 返回值对齐） */
interface PathProgressData {
  pathName: string;
  requiredTotal: number;
  requiredCompleted: number;
  totalModules: number;
  completedModules: number;
  inProgressModules: number;
  completionRate: number;
  totalEstimatedHours: number;
  modules: Array<{
    moduleId: string;
    moduleTitle: string;
    moduleDescription: string;
    priority: string;
    estimatedHours: number;
    dependsOn: string[];
    totalDocs: number;
    completedDocs: number;
    inProgressDocs: number;
    completionRate: number;
    unlocked: boolean;
  }>;
}

/**
 * 渲染路径详情到 #path-detail 容器
 * @param pathName - 路径名称
 * @param progress - 路径进度对象
 */
function renderPathDetail(pathName: string, progress: PathProgressData): void {
  const detailEl = document.getElementById('path-detail');
  if (!detailEl) return;

  const modulesHtml = progress.modules
    .map((mod): string => {
      const meta = moduleMap.get(mod.moduleId);
      const title = meta?.title ?? mod.moduleTitle ?? mod.moduleId;
      const desc = meta?.description ?? mod.moduleDescription ?? '';
      const priorityLabel = priorityLabels[mod.priority] ?? mod.priority;
      const priorityColor = priorityColors[mod.priority] ?? '#6b7280';
      const isCompleted = mod.completionRate === 100;
      const isInProgress = mod.completionRate > 0 && mod.completionRate < 100;
      const isLocked = !mod.unlocked;
      const itemClass = isCompleted ? 'completed' : isLocked ? 'locked' : '';
      const actionClass = isCompleted ? 'completed' : isLocked ? 'locked' : '';
      const actionText = isCompleted
        ? '已完成'
        : isInProgress
          ? '继续学习'
          : isLocked
            ? '未解锁'
            : '开始学习';
      const progressFillClass = isCompleted ? 'complete' : '';
      const depsText =
        mod.dependsOn.length > 0
          ? `前置：${mod.dependsOn.map((d) => moduleMap.get(d)?.title ?? d).join('、')}`
          : '';

      return `
      <div class="path-module-item ${itemClass}" style="--module-color:${priorityColor}">
        <a class="path-module-card" href="${base}${mod.moduleId}/">
          <div class="path-module-row">
            <div>
              <div class="path-module-name">${title}</div>
              <div class="path-module-desc">${desc}</div>
              <div class="path-module-meta">
                <span class="path-module-priority" style="background:${priorityColor}">${priorityLabel}</span>
                <span class="path-module-hours">约 ${mod.estimatedHours} 小时</span>
                ${depsText ? `<span class="path-module-deps">${depsText}</span>` : ''}
              </div>
              <div class="path-module-progress">
                <div class="path-module-progress-track">
                  <div class="path-module-progress-fill ${progressFillClass}" style="width:${mod.completionRate}%"></div>
                </div>
                <span class="path-module-progress-text">${mod.completionRate}%</span>
              </div>
              <span class="path-module-action ${actionClass}">${actionText}</span>
            </div>
          </div>
        </a>
      </div>
    `;
    })
    .join('');

  detailEl.innerHTML = `
    <div class="path-detail-header">
      <h3 class="path-detail-title">${progress.pathName || pathName}</h3>
      <div class="path-detail-stats">
        <span class="path-detail-stat">共 <strong>${progress.totalModules}</strong> 个模块</span>
        <span class="path-detail-stat">已完成 <strong>${progress.completedModules}</strong></span>
        <span class="path-detail-stat">进行中 <strong>${progress.inProgressModules}</strong></span>
        <span class="path-detail-stat">必学 <strong>${progress.requiredCompleted}/${progress.requiredTotal}</strong></span>
        <span class="path-detail-stat">预计 <strong>${progress.totalEstimatedHours}</strong> 小时</span>
      </div>
    </div>
    <div class="path-completion">
      <div class="path-completion-header">
        <span class="path-completion-label">整体完成度</span>
        <span class="path-completion-value">${progress.completionRate}%</span>
      </div>
      <div class="path-completion-track">
        <div class="path-completion-fill" style="width:${progress.completionRate}%"></div>
      </div>
    </div>
    <div class="path-modules-timeline">
      ${modulesHtml}
    </div>
  `;
}

/**
 * 初始化路径选择交互
 */
function initPathSelector(): void {
  loadInjectedData();
  buildModuleMap();

  const tabs = document.querySelectorAll('.path-tab');
  if (tabs.length === 0) return;

  // Tab 点击事件
  tabs.forEach((tab) => {
    const el = tab as HTMLElement;
    el.addEventListener('click', () => {
      const pathId = el.dataset.pathId;
      const pathName = el.dataset.pathName;
      if (pathId && pathName) {
        void selectPath(pathId, pathName);
      }
    });
  });

  // 默认激活第一个路径
  const firstTab = tabs[0] as HTMLElement;
  if (firstTab) {
    const pathId = firstTab.dataset.pathId;
    const pathName = firstTab.dataset.pathName;
    if (pathId && pathName) {
      void selectPath(pathId, pathName);
    }
  }
}

/**
 * 更新学习阶段时间线的模块进度条
 * 基于 localStorage 中的 fandex-progress 数据
 */
function updateRoadmapProgress(): void {
  let progress: Record<string, { status: string }> = {};
  try {
    const raw = localStorage.getItem('fandex-progress');
    if (raw) progress = JSON.parse(raw) as Record<string, { status: string }>;
  } catch {
    /* ignore */
  }

  document.querySelectorAll('[data-progress-module]').forEach((card) => {
    const el = card as HTMLElement;
    const moduleId = el.getAttribute('data-progress-module');
    const bar = el.querySelector('[data-progress-bar]') as HTMLElement | null;
    if (!moduleId || !bar) return;

    const allKeys = Object.keys(progress).filter((k) => k.startsWith(moduleId + '/'));
    const total = allKeys.length || 1;
    const done = allKeys.filter((k) => progress[k]?.status === 'done').length;
    const pct = allKeys.length > 0 ? Math.round((done / total) * 100) : 0;
    bar.style.setProperty('--progress-pct', `${pct}%`);
  });
}

// 初始化（首次加载与 View Transitions 后触发）
function onPageLoad(): void {
  initPathSelector();
  updateRoadmapProgress();
}

onPageLoad();
document.addEventListener('astro:page-load', onPageLoad);
document.addEventListener('fandex-progress-change', updateRoadmapProgress);
