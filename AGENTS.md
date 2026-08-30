# FANDEX 仓库规则

## 仓库形态约束（最高优先级）

- 本仓库是单一 monorepo：根目录是唯一的仓库根，全仓库只有一个 `.git`。
- app-web、app-desktop、app-Android-new、app-Android-old 以及 cnt-content、
  shd-shared、tls-tools、thd-third-party、tools 均为根仓库下的普通子目录，
  严禁在其中初始化独立 Git 仓库（git init / 嵌套 .git / .gitmodules /
  submodule / 独立 remote），也不得将任何子目录当作独立项目维护。
- 子目录内如发现历史遗留的嵌套 .git 或独立仓库配置，应立即清理并在
  变更说明中报备。
- 子目录的 README 只能以"本目录是 FANDEX monorepo 的子项目"定位书写，
  完整说明指向根 README.md 与本文件；子目录 .gitignore 仅作为构建
  兜底保留，不得包含仓库级声明。

## 通用工程规范

- 代码与对话中一律不使用 emoji 表情。
- 代码项目中的图形需求：优先使用 SVG 或 Mermaid 自行绘制，不引入位图素材。
- 界面装饰禁止使用点状元素（圆点、胶囊圆点、点阵等），统一改为 1-4px 宽的竖条
  或几何刻度线；按钮、徽章、状态指示器一律使用直角小圆角（`--radius-md` 以内）。
- 代码需有完善、简洁的中文注释。
- 每次任务完成后删除一次性脚本、废弃代码文件等临时产物。
- 文档内容统一存放于 `cnt-content/full`；`cnt-content/syntax` 为语法速览
  专用速查素材源（由 `app-web/scripts/build-syntax.mjs` 消费）；
  `cnt-content/mobile` 为历史遗留目录，不作为网站内容源，不在其上执行统一化变更。

## 文档 frontmatter 规范

`cnt-content/full` 下每篇 Markdown 文档的顶部信息必须严格遵循以下规则。

### 字段集合与顺序

frontmatter 仅允许以下 10 个标准字段，且必须按此顺序书写：

```yaml
---
order: 40
title: 标题
module: '模块 id'
category: 分类中文名
difficulty: beginner
description: 一句话描述。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'module/文件名'
prerequisites:
  - 'module/文件名'
---
```

### 必填字段

- `title`：文档标题。
- `module`：模块 id，必须与 `shd-shared/metadata/modules.json` 中的模块 id 一致。
- `category`：分类中文名，必须为 modules.json `categoryLabels` 中的 7 个值之一
  （工具链 / 前端技术 / 后端技术 / 数据库 / 计算机科学 / 数学 / 云与基础设施），
  取模块 `categories` 数组的第一个分类对应的中文名。
- `difficulty`：难度，枚举 `beginner` / `intermediate` / `advanced`。
- `author`：作者，默认 `fanquanpp`。
- `updated`：最近一次更新时间，格式 `YYYY-MM-DD`；缺失时取该文件最近一次
  git 提交日期，其次取文件修改日期。

### order 编号规则

- 每个模块内部独立编号，从 10 开始、步长 10 递增（10、20、30……）。
- 编号顺序必须与学习顺序一致：先按当前 order 升序、再按文件名序号升序，
  重新生成连续编号；同一模块内不得出现重复 order。
- 新增文档时插入学习顺序中的对应位置，并整体重新编号。

### related / prerequisites 引用格式

- 统一为 `module/文件名`，文件名不带 `.md` 后缀，例如 `getting-started/002-DevEnvSetup`。
- 引用必须指向真实存在的文档；标题式、别名式引用需解析为文件名，
  指向不存在文档的死链应删除。
- `module` 必须是 modules.json 中的模块 id；历史旧名（如 network、math）需先映射。

### 禁止字段

以下历史扩展字段不得再出现在 frontmatter 中：
`tags`、`created`、`quiz`、`references`、`etymology`、
`estimatedReadingTime`、`lastReviewed`、`reviewer`、`readingTime`、`keywords`。

### 模块 -> 分类映射

按 modules.json 的主分类（categories 数组第一个元素）映射：

| 模块 id | 分类中文名 |
| --- | --- |
| getting-started / markdown / git / github / english / shell / pnpm-monorepo | 工具链 |
| html5 / css / javascript / typescript / vue3 / react / svg / astro / vite / tailwind / nextjs / svelte / angular | 前端技术 |
| java / kotlin / csharp / go / lua / harmonyos / python / rust / deno / bun / nestjs | 后端技术 |
| sql / mysql / postgresql / redis / mongodb | 数据库 |
| algorithm / cs-fundamentals / c / cpp | 计算机科学 |
| calculus / discrete-math / linear-algebra / probability-statistics | 数学 |
| devops / networking / cybersecurity / cloud-computing / iot / software-testing / software-engineering / software-architecture / engineering-practices / message-queue | 云与基础设施 |

## 校验入口

- `app-web/src/content.config.ts`：Astro content schema，负责必填字段的构建期校验。
- `app-web/scripts/content-audit.mjs`：内容质量审计，校验必填字段、字段白名单与引用格式。
