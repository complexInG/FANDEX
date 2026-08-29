/**
 * FANDEX-App 版本数据
 * 数据源：GitHub Releases (https://github.com/fanquanpp/FANDEX-App/releases)
 * 每个版本包含：版本号、徽章、下载链接、更新日期、包大小、系统要求、变更日志
 */

export interface FandexVersion {
  id: string;
  version: string;
  badge: string;
  date: string;
  size: string;
  require: string;
  apk: string;
  apkName: string;
  summary: string;
  changes: string[];
}

export const versions: FandexVersion[] = [
  {
    id: '3.7.0',
    version: 'v3.7.0',
    badge: '最新版',
    date: '2026-07-21',
    size: '3.15 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.7.0/FANDEX-App_3.7.0.apk',
    apkName: 'FANDEX-App_3.7.0.apk',
    summary: '代码质量优化 + 主题过渡动画 + 多语言精简',
    changes: [
      '静默异常处理统一添加日志输出（27 处），便于问题排查',
      'ContentLoader 资源关闭改用 use{} 块，避免资源泄漏',
      '主题解耦闭环：4 处 isSystemInDarkTheme() 调用迁移至 LocalIsDarkTheme',
      'GitHub API URL 迁移至 BuildConfig 配置化，便于环境切换',
      'OkHttpClient 单例复用，优化网络连接开销',
      '多语言精简：仅保留简体中文，移除繁体中文支持',
      '主题切换新增 400ms 颜色过渡动画，三套配色同步过渡',
      'versionCode 12 → 13 / versionName 3.6.0 → 3.7.0',
    ],
  },
  {
    id: '3.6.0',
    version: 'v3.6.0',
    badge: '综合优化',
    date: '2026-07-20',
    size: '3.15 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.6.0/FANDEX-v3.6.0.apk',
    apkName: 'FANDEX-v3.6.0.apk',
    summary: 'Android App 综合优化：双主题启动图 + 列表动效 + 光晕清理 + UI 显示大小调节',
    changes: [
      '主题不同步修复：GlassCard / SkeletonScreen 等组件通过 LocalIsDarkTheme 统一注入',
      'Splash 启动图双主题适配，随用户主题切换',
      '清理光晕发散模糊类效果，回归克制几何装饰风格',
      '列表滑入动效：4 处 LazyColumn / LazyRow 添加 animateItem 动效',
      '新增 UI 显示大小全局调节（0.8x - 1.4x），侧边栏 Slider 入口',
      '修复文章页翻页滚动位置未重置 bug',
      '新增 values-night/colors.xml 覆盖，保证冷启动主题一致',
      'versionCode 11 → 12 / versionName 3.5.0 → 3.6.0',
    ],
  },
  {
    id: '3.5.0',
    version: 'v3.5.0',
    badge: '内容重编',
    date: '2026-07-20',
    size: '3.14 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.5.0/FANDEX-v3.5.0.apk',
    apkName: 'FANDEX-v3.5.0.apk',
    summary: '内容审查重编：删除 3 个非语法模块，5 模块按 App 规范重编',
    changes: [
      '删除 DevOps / GitHub / 软件测试 3 个非独立语法体系模块（共 90 篇）',
      'HTML5 重编：30 篇，删除概念+实战，保留标签语法+API 签名',
      'SVG 重编：18 篇，删除历史+性能建议，保留元素签名+path 命令',
      'React 重编：45→15 篇，删除原理/对比/工程化，保留 Hooks+组件+路由 API',
      'Vue3 重编：35→20 篇，删除原理/实战/对比，保留 Composition API+SFC+内置组件',
      'HarmonyOS 重编：33→20 篇，删除 Stage/FA 对比+签名+调试，保留装饰器+ArkUI+系统 API',
      '所有文档统一删除 YAML frontmatter，采用语法签名+代码示例结构',
      '删除概述/原理/对比/实战等非语法内容',
      '最终内容矩阵：22 模块 / 313 篇文档（modules 数组 24 条，含 HTML5/SVG 跨分类副本）',
      '更新 build.gradle.kts versionCode 11 / versionName 3.5.0',
      '同步 README.md 徽章与内容矩阵、CHANGELOG.md 追加 v3.5.0 条目',
    ],
  },
  {
    id: '3.4.0',
    version: 'v3.4.0',
    badge: '里程碑',
    date: '2026-07-20',
    size: '3.60 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.4.0/FANDEX-v3.4.0.apk',
    apkName: 'FANDEX-v3.4.0.apk',
    summary: '补充 8 个新模块（251 篇文档），模块总数 17→25',
    changes: [
      '新增 8 个模块：HTML5 / SVG / React / Vue3 / HarmonyOS / DevOps / GitHub / 软件测试',
      '共新增 251 篇代码语法速查文档',
      'HTML5 与 SVG 跨分类归属：markup + frontend',
      'modules 数组 17→27（含 2 条跨分类副本）',
      '文档总数 210→461',
      '实现跨分类模块的多入口展示',
      '更新 index.json 元数据 documentMeta.updated.3.4.0',
      'APK 大小 2.84→3.60 MB',
    ],
  },
  {
    id: '3.3.0',
    version: 'v3.3.0',
    badge: '内容扩充',
    date: '2026-07-20',
    size: '2.84 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.3.0/FANDEX-v3.3.0.apk',
    apkName: 'FANDEX-v3.3.0.apk',
    summary: '合并短中期任务：JS/CSS 新特性 + 长文拆分 + 文档元数据系统',
    changes: [
      '新增 8 篇 JavaScript 新特性文档（ES2024 + ES2025 共 39 项语法）',
      '新增 8 篇 CSS 新特性文档（2024-2025 共 35 项语法）',
      '拆分 3 篇长文为 6 篇（Kotlin / CSS / Python 模块）',
      '建立文档元数据系统：index.json 新增 documentMeta 字段',
      '接入 markdownlint-cli2 + GitHub Actions CI 检查',
      '文档矩阵 207→210，无代码变更影响应用逻辑或签名',
    ],
  },
  {
    id: '3.2.0',
    version: 'v3.2.0',
    badge: '内容优化',
    date: '2026-07-20',
    size: '2.83 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.2.0/FANDEX-v3.2.0.apk',
    apkName: 'FANDEX-v3.2.0.apk',
    summary: '全量文档优化升级：扫描 17 模块 207 篇文档',
    changes: [
      '扫描 17 模块 / 207 篇文档（65,385 行）完成格式合规与内容刷新',
      '修复 Redis 模块 5 篇文档的格式合规问题',
      '补充 8 篇基础文档新特性（Python 3.13+ / Java 25+ / TS 5.x 等）',
      '更新 6 处过时 README 条目',
      '版本号 v3.1.0 → v3.2.0（versionCode 7→8）',
    ],
  },
  {
    id: '3.1.0',
    version: 'v3.1.0',
    badge: '体验优化',
    date: '2026-07-20',
    size: '2.83 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.1.0/FANDEX-v3.1.0.apk',
    apkName: 'FANDEX-v3.1.0.apk',
    summary: '12 项体验优化：动画、数学公式、背景装饰、双主题',
    changes: [
      '新增 4 种页面过渡动画（PageTransitions.kt + HomeActivity.kt）',
      '修复数学公式渲染：新增 MathFormulaRenderer.kt 并接入 ComposeMarkdown',
      '移除背景发光色晕，符合简约有质感设计目标',
      '浅色模式下装饰可见度增强',
      '点阵系统重新规划布局',
      '更新自检功能增加提示文案',
      '界面文本本地化为简繁中文（移除第三语言）',
      '启动页固定 1.5 秒时长，含文字动画',
    ],
  },
  {
    id: '3.0.0',
    version: 'v3.0.0',
    badge: '架构重构',
    date: '2026-07-20',
    size: '2.69 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v3.0.0/FANDEX-v3.0.0.apk',
    apkName: 'FANDEX-v3.0.0.apk',
    summary: 'Android 原生重构：Kotlin + Jetpack Compose + Material 3',
    changes: [
      '技术栈全量升级：Kotlin 2.4.10 / AGP 9.3.0 / Compose BOM 最新',
      '6 层叠加背景装饰系统，替代旧 Tauri 方向',
      '14 项 UIUX 增强（过渡动画 / 双主题 / 字号调节等）',
      '新增更新自检功能（WorkManager 周期任务）',
      'Markdown 渲染：commonmark AST → Compose 组件，无 WebView',
      '20+ 语言代码块语法高亮，含浅色/深色主题与复制按钮',
      '60 个单元测试全部通过',
      'Release APK v2 签名验证通过',
      'Redmi K60（Android 15）真机验证 PASS',
    ],
  },
  {
    id: '2.1.0',
    version: 'v2.1.0',
    badge: '视觉系统',
    date: '2026-07-16',
    size: '2.30 MB',
    require: 'Android 8.0+',
    apk: 'https://github.com/fanquanpp/FANDEX-App/releases/download/v2.1.0/FANDEX-v2.1.0.apk',
    apkName: 'FANDEX-v2.1.0.apk',
    summary: '构成主义几何背景装饰系统，视觉体系全面升级',
    changes: [
      '新增构成主义几何背景装饰系统，4 种视图变体、11 种装饰元素',
      '基于 Jetpack Compose Canvas 原生绘制，双主题透明度梯度适配',
      '启动页、首页、模块页、加载态全面接入视觉系统',
      '主题系统扩充 GeoDecorColors 装饰色板 tokens',
      'README 文档新增设计语言与视觉系统章节',
      '17 模块 207 篇文档，离线速查',
      'Kotlin + Jetpack Compose + Material 3',
      '深色/浅色双模式',
      '完全离线运行，无网络权限',
    ],
  },
];

/** 最新版本（数组首项） */
export const latestVersion: FandexVersion = versions[0];

/** 按主版本号分组（如 v3.x.x） */
export interface VersionGroup {
  range: string;
  versions: FandexVersion[];
}

export const versionGroups: VersionGroup[] = versions.reduce((groups, v) => {
  const major = v.version.split('.')[0]; // "v3" / "v2"
  const range = `${major}.x.x`;
  let group = groups.find((g) => g.range === range);
  if (!group) {
    group = { range, versions: [] };
    groups.push(group);
  }
  group.versions.push(v);
  return groups;
}, [] as VersionGroup[]);
