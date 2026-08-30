# 更新日志（CHANGELOG）

本文件记录 FANDEX 单仓库的版本发布历史与各版本变更说明。
格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循语义化版本（SemVer）。

> 发布说明约定：`android-release.yml` 工作流在打 `v*` 标签发布时，
> 会自动提取本文档中对应 `## [vX.Y.Z]` 段落作为 GitHub Release 说明。

## [v2.0.0] - 2026-08-30

本版本包含三大主线：Android 双端体验升级、面向零基础学习者的内容体系重构、
仓库治理与发布链路完善。

### Android 双端体验升级（app-Android-new）

- 修复深浅色模式下按钮与搜索图标全黑问题（FdxIconButton 默认着色改主题语义色）；
- mermaid 图表缩放 / 平移手势内核重写：切断每帧布局回环、rAF 合帧、双指
  二维拖动，缩放拖拽恢复流畅；
- 语法速览页与学习路线页视觉提级至首页同等级（统计横幅、序号、计数药丸、
  阶段几何刻度条）；三页区块标题统一使用共享 SectionHeader；
- SVG 图标统一至 app-web favicon 设计基准，启动图标同步（蓝渐变 + 白 F）。

### 面向零基础学习者的内容体系重构（cnt-content）

- 认知启航层：getting-started 新增计算机 / 编程 / 互联网三篇认知课；
  12 个语言类模块各补"是什么与第一次运行"零基础入门篇（合计 15 篇，
  全部标注 level: zero-beginner 与 estimatedHours）；
- 模块精简与合并：删除 english / lua / harmonyos / 数学四件套 / iot（200 篇），
  message-queue 并入 software-architecture、deno/bun 并入 javascript；
  模块总数 54 -> 43，内容 1718 篇；
- frontmatter 扩展：schema 新增可选 level（五级分层）与 estimatedHours 字段，
  AGENTS.md 规范同步；
- 归档提示：404 页对 11 个已归档模块展示专门说明；
- 全仓 frontmatter 引用 6940 处、learning-path 引用 1075 处全量校验，
  修复历史遗留死链，死链归零。

### 仓库治理与发布链路

- 单一 monorepo 治理：确认根目录唯一 .git，无嵌套仓库与 submodule；
  LICENSE 上提至根目录统一许可归属，新增 CONTRIBUTING.md 与 DISCLAIMER.md；
- README 面向零基础学习者重写（学习主线表、真实构建命令、许可与免责）；
- CI 触发拆分修复：on.push 同时定义 branches 与 tags 为 AND 语义导致单独
  push 标签不触发，发布（android-release.yml，tags 触发）与构建校验
  （android-build.yml，main 触发）拆分为两个工作流；
- 删除 cnt-content/mobile 历史遗留目录（690 篇，语法素材已迁至
  cnt-content/syntax）。

### 版本与命名

- 双端 versionName 统一为 2.0.0（versionCode old 15 / new 5）；
- app-Android-old 安装名改为 FANDEXO，与主线 FANDEX 并存可辨；
- 更新自检 API 迁移至本仓库 FANDEX/releases/latest，资产匹配改为
  FANDEX-Legacy-v*。

### 修复

- app-Android-old gradlew 缺少可执行权限导致 CI 构建失败（exit 126）；
- app-Android-old release 签名回退策略（无 keystore 时回退 debug 签名）；
- web 构建高亮引擎切换 Shiki JS 正则引擎，修复 oniguruma WASM 内存越界。

## [v1.x] — 历史版本

- 单仓库整合：三端统一 React 生态（web / desktop / android 占位）
  + 共享内容层（cnt-content / shd-shared / tls-tools / thd-third-party）。
- 旧版 FANDEX-App 完整源码迁入仓库归档（后续重组为 `app-Android-old`）。
- 历史变更详见各子工程内部文档与提交历史。
