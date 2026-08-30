# 更新日志（CHANGELOG）

本文件记录 FANDEX 单仓库的版本发布历史与各版本变更说明。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循语义化版本（SemVer）。

> 发布说明约定：`android-release.yml` 工作流在打 `v*` 标签发布时，
> 会自动提取本文档中对应 `## [vX.Y.Z]` 段落作为 GitHub Release 说明。

## [Unreleased]

### 新增

- 仓库根 README 与本 CHANGELOG：完善仓库介绍与版本更新说明。
- 语法速览页与学习路线页视觉提级：新增头部统计横幅（语言 / 语法点 /
  文档总量，路线 / 阶段总量），条目增加序号、分类色药丸与阶段几何刻度条，
  与首页同等级的视觉层次。
- 语法速览 / 学习路线共用 `StatsBar` 统计横幅组件（`ui/components/Common.kt`）。

### 变更

- 仓库形态治理：确认单一 monorepo（根目录唯一 `.git`），全面扫描确认
  无嵌套 `.git`、无 `.gitmodules`、无 submodule 记录；`LICENSE` 由
  `app-Android-old` 上提至仓库根统一许可归属；`app-Android-new/README.md`
  补充 monorepo 子项目定位声明并修正过时版本与文档规模信息；
  AGENTS.md 新增"仓库形态约束"章节，明确禁止在子目录初始化独立
  Git 仓库或将其当作独立项目维护。
- 目录结构重组：
  - `app-android` 更名为 `app-Android-new`（新技术栈 Android 工程主线）；
  - 旧版 FANDEX-App 归档目录更名为 `app-Android-old`，并参考
    `app-Android-new` 精简为纯 Android 工程结构（移除旧仓库 .github
    工作流、web 官网、screenshots 与独立文档，Android 工程上提至目录根）；
  - 同步更新根 .gitignore、pnpm-workspace、tsconfig、CI 工作流与
    内容生成脚本中的全部路径引用。
- 旧版 App 内置文档整体替换为 cnt-content 内容源：
  - 新增 `app-Android-old/scripts/generate-legacy-content.mjs` 内容管线，
    从 `cnt-content/full` 与 `shd-shared/metadata/modules.json` 生成
    `dist-mobile` 文档与索引；
  - 文档由 22 模块 313 篇（中文文件名）扩展为 54 模块 1903 篇（英文 slug），
    与主仓库内容完全同源；
  - 旧版 `ContentLoader` 数据契约保持不变，文档中文标题改由索引
    `documents` 数组提供（取自 frontmatter）。
- SVG 图标资源统一：`shd-shared/assets/icons/app-icon.svg` 与
  `favicon.svg` 统一为同一设计基准（蓝色对角渐变 + 白色 F），
  `app-Android-new` 启动图标同步（背景品牌蓝渐变、前景白色 F）。
- `app-Android-old` release 构建签名回退策略：无正式 keystore 时
  回退 debug 签名（与 `app-Android-new` 分发策略一致），CI 可直接出包。
- CI（android-release.yml）升级为双端并行构建与发布：
  - matrix 同时构建 `app-Android-new` 与 `app-Android-old`；
  - `v*` 标签发布时 Release 附带双端 APK（`FANDEX-<tag>.apk` /
    `FANDEX-Legacy-<tag>.apk`，applicationId 不同可并存安装）；
  - 发布说明自动提取本 CHANGELOG 对应版本段落。

### 修复

- `app-Android-new` 深浅色模式下按钮与搜索图标全部为黑色的问题：
  `FdxIconButton` 默认着色由 `Color.Unspecified`（退化为 LocalContentColor
  默认黑）改为主题 `onSurface` 语义色，搜索框 leadingIcon 显式使用
  `fgTertiary` 占位色。
- `app-web` 构建（GitHub Actions）在约 1900 篇文档连续高亮时
  Shiki oniguruma WASM 内存越界（`memory access out of bounds`，
  构建 14 分钟后失败）：高亮引擎切换为 Shiki JavaScript 正则引擎
  （`createJavaScriptRegexEngine`，forgiving 模式），构建稳定通过。

### 性能

- `app-Android-new` mermaid 图表缩放 / 平移手势内核重写：
  - 手势进行中锁定容器高度、停止向原生回报，切断「JS 回报 → Compose
    重布局 → WebView 尺寸变化」的每帧反馈循环，缩放拖拽恢复流畅；
  - touchmove 高频事件经 requestAnimationFrame 合帧，舞台固定合成层
    （will-change + translate3d）；
  - 双指手势升级为捏合缩放 + 二维拖动（以捏合中心为焦点），
    放大后可纵向查看全图。

### 移除

- `app-Android-old` 死代码清理（经符号级引用审计确认零调用，
  编译验证通过）：`ui/enhancements` 下 StatusColors、SkeletonScreen、
  DarkModeTuning、SpringAnimations、ParallaxScroll、Tilt3DModifier、
  CustomScrollbar、MicroInteractions 八个文件，以及历史预留层
  `ui/background/L6CardGradientBorder`。
- `app-Android-new` 首页私有 `SectionHeader` 重复实现，统一使用共享版。

## [v1.x] — 历史版本

- 单仓库整合：三端统一 React 生态（web / desktop / android 占位）
  + 共享内容层（cnt-content / shd-shared / tls-tools / thd-third-party）。
- 旧版 FANDEX-App 完整源码迁入仓库归档（后续重组为 `app-Android-old`）。
- 历史变更详见各子工程内部文档与提交历史。
