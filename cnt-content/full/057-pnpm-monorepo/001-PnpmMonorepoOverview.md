---
order: 1
title: pnpm 与 Monorepo 工程化
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: intermediate
description: 'pnpm 与 Monorepo 工程化：workspace、内容寻址存储、依赖隔离、catalog、任务编排与发布'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/Vite构建工具
  - git/Git基础操作
  - devops/CI/CD流水线
prerequisites:
  - getting-started/包管理器
---
## 0. 零基础入门（从零开始）

### 0.1 零基础起点

本模块讲解 pnpm 与 Monorepo（单仓库多包）工程化。零基础可学，但建议先读完 013 包管理器、003-git 与 039 工程实践模块，并已安装 Node.js 与 pnpm。
先理解场景：一个项目可能同时包含网站、桌面应用、共享组件库三个部分。把它们放在一个 Git 仓库里统一管理，就是 Monorepo；pnpm 负责高效安装和隔离依赖。

### 0.2 第一个 pnpm workspace 项目

```json
// pnpm-workspace.yaml：声明哪些目录是“包”
packages:
  - 'apps/*'        # apps/web、apps/admin 都是包
  - 'packages/*'    # packages/ui、packages/utils 都是包

// packages/utils/package.json：声明依赖本地的 ui 包
{
  "name": "@my/utils",
  "dependencies": {
    "@my/ui": "workspace:*"   // 指向本地包
  }
}
```

pnpm-workspace.yaml 告诉 pnpm：apps 和 packages 目录下的每个子目录都是独立的“包”，它们可以互相引用。
workspace:* 是一种特殊版本号：表示“不要从 npm 下载，直接使用本仓库里那个包”。这样共享代码无需发布到 npm 就能联调。
在仓库根目录运行 pnpm install，pnpm 会一次性安装所有包的依赖，并按依赖关系建立链接。
之后可以用 pnpm --filter @my/utils dev 只启动指定包，或 pnpm -r build 按依赖顺序构建全部包。
这套结构就是 FANDEX 仓库本身采用的布局：app-web、shd-shared、tls-tools 都通过 workspace 关联。

### 0.3 学习路径

完成上面的第一步后，按以下顺序继续学习：

- 002-依赖管理机制：内容寻址存储与严格隔离。
- 003-常用命令：filter、递归构建、依赖分析。
- 004-版本与发布：changesets 管理多包版本。


## 1. 什么是 Monorepo

Monorepo（单仓库多包）是把多个应用、共享库与工具链放在同一个 Git 仓库中管理的工程模式。与之相对的是多仓库（Polyrepo）：每个项目独立仓库。

Monorepo 的优势：

第一，原子提交：跨包的修改一次提交，版本始终一致；

第二，统一依赖：依赖版本集中管理，避免各包漂移；

第三，代码复用：共享包通过 workspace 协议直接引用，无需发布到 npm 即可联调；

第四，统一 CI：一次流水线构建全部相关包。

代价是工具链复杂度：需要 workspace 管理、任务编排与构建缓存。pnpm 是目前 Node 生态中最适合 Monorepo 的包管理器之一。

## 2. pnpm 的核心机制

### 2.1 内容寻址存储

pnpm 把所有依赖包的内容存储在全局 store 中（按内容哈希寻址），项目通过硬链接引用。同一版本的依赖在多个项目中只存一份，节省磁盘；不同版本共存互不干扰。

### 2.2 严格依赖隔离

传统 npm 把依赖扁平提升到根 node_modules，导致“幽灵依赖”：代码可以 import 未声明的包。pnpm 的 node_modules 是符号链接结构，只有 package.json 中声明的依赖可见。

```text
node_modules/
  .pnpm/              # 内容寻址存储的链接层
  my-app -> .pnpm/my-app@1.0.0/node_modules/my-app
```

讲解：直接依赖通过符号链接暴露，间接依赖藏在 .pnpm 中不可见，从结构上杜绝幽灵依赖。

### 2.3 workspace 协议

`workspace:*` 让包依赖本地兄弟包：

```json
{
  "dependencies": {
    "@fandex/utils": "workspace:*"
  }
}
```

发布时 pnpm 会把 `workspace:*` 替换为实际版本号。

## 3. 工程结构

FANDEX 采用典型 Monorepo 布局：

```text
FANDEX/
  app-web/               # Web 应用（Astro + React）
  app-desktop/           # 桌面应用（Tauri + Expo）
  app-android/           # Android 应用（Expo）
  shd-shared/            # 共享层（tokens、utils、assets）
  tls-tools/             # 工具链（ID 分配、清单生成）
  thd-third-party/       # 第三方组件封装
  dcs-docs/              # 文档目录
  pnpm-workspace.yaml    # workspace 配置
  package.json
```

```yaml
# pnpm-workspace.yaml
packages:
  - 'app-*'
  - 'shd-shared'
  - 'shd-shared/*'
  - 'tls-tools'
  - 'thd-third-party/*'
```

讲解：glob 模式声明所有包目录；catalog 在同一个文件中统一核心依赖版本。

## 4. catalog 统一版本

```yaml
catalog:
  react: ^19.0.0
  typescript: ^5.7.0
  vite: ^6.0.0
```

各包通过 `catalog:` 协议引用：

```json
{
  "dependencies": {
    "react": "catalog:"
  }
}
```

讲解：catalog 是 pnpm 9+ 的特性，让“依赖版本单一事实来源”成为可能；升级版本只需改一处。

## 5. 常用命令

```bash
pnpm install                     # 安装全部 workspace 依赖
pnpm --filter @fandex/web dev    # 只操作指定包
pnpm -r build                    # 递归构建所有包
pnpm -r --topological build      # 按依赖拓扑顺序构建
pnpm -F @fandex/web add lodash   # 给指定包添加依赖
pnpm why react                   # 查看依赖来源
pnpm store prune                 # 清理全局 store
```

讲解：`--filter` 精确定位包；`--topological` 保证先构建依赖再构建应用；`--parallel` 并行执行无依赖关系的任务。

## 6. 任务编排与缓存

大型 Monorepo 推荐 Turborepo：

```json
{
  "turbo": {
    "tasks": {
      "build": {
        "dependsOn": ["^build"],
        "outputs": ["dist/**"]
      },
      "test": {
        "dependsOn": ["build"],
        "outputs": []
      }
    }
  }
}
```

讲解：`dependsOn: ["^build"]` 表示先构建依赖；turbo 按输入文件哈希缓存任务结果，未变更的包直接复用缓存，CI 提速显著。

## 7. 版本管理与发布

Changesets 是 Monorepo 版本管理的标准方案：

```bash
pnpm changeset add        # 记录变更（major/minor/patch）
pnpm changeset version    # 更新版本与 CHANGELOG
pnpm changeset publish    # 发布到 npm
```

发布流程：CI 检查 changeset 存在 -> 合并 PR -> 发布流水线执行 version + publish。

## 8. CI 最佳实践

```yaml
# GitHub Actions 片段
steps:
  - uses: pnpm/action-setup@v4
    with:
      version: 10
  - uses: actions/setup-node@v4
    with:
      node-version: 22
      cache: pnpm
  - run: pnpm install --frozen-lockfile
  - run: pnpm -r --topological build
  - run: pnpm -r test
```

讲解：`--frozen-lockfile` 保证按 lockfile 精确安装；`cache: pnpm` 缓存 store 与依赖。

## 9. 常见陷阱

陷阱一：幽灵依赖。代码 import 了未声明的包，本地能跑、干净环境失败。用 pnpm 隔离并在 CI 强制 frozen-lockfile。

陷阱二：构建顺序错误。应用先于依赖构建失败。用 `--topological` 或 turbo 的 dependsOn。

陷阱三：忽略 lockfile 提交。团队环境不一致。pnpm-lock.yaml 必须入库。

陷阱四：版本漂移。各包直接写不同版本。用 catalog 统一。

陷阱五：循环依赖。包间互相引用导致构建死循环。重新设计分层。

陷阱六：大仓库 CI 慢。全量任务重复跑。用 turbo 缓存与 affected 模式。

## 10. 参考资源

pnpm 官方文档：https://pnpm.io/zh/

pnpm workspace：https://pnpm.io/zh/workspaces

Turborepo：https://turborepo.com/

Changesets：https://changesets-docs.vercel.app/

黑马程序员 Bilibili 空间：https://space.bilibili.com/37974444

## 11. 小结

pnpm + Monorepo 是现代前端工程化的主流组合：内容寻址存储节省磁盘，严格隔离保证正确性，catalog 统一版本，turbo 加速构建。FANDEX 即采用这一架构管理三端应用与共享层。

## 参考文献



pnpm 官方文档：https://pnpm.io/zh/
pnpm workspace 文档：https://pnpm.io/zh/workspaces
Turborepo：https://turborepo.com/
Changesets：https://changesets-docs.vercel.app/
Monorepo 模式（Nx 博客）：https://nx.dev/blog/

## 延伸阅读



FANDEX 项目结构解析，见 058-pnpm-monorepo 模块文档。
Vite 多包构建，见 056-vite 模块。
CI/CD 与发布，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供工程化课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 pnpm 存储与链接机制

全局 store：按内容哈希存储包；硬链接到项目 node_modules/.pnpm。
符号链接：项目直接依赖链接到 .pnpm 中对应版本；间接依赖不暴露。
hoist 选项：shamefully-hoist 模拟 npm 扁平结构（慎用）。
诊断：pnpm store status、why 命令分析依赖来源。

### 13.2 Monorepo 任务编排

拓扑构建：先构建依赖再构建应用；pnpm -r --topological。
缓存：turbo 按输入哈希缓存任务结果；远程缓存加速 CI。
过滤器：--filter 精确选择任务范围；affected 模式只跑变更相关。
并行与限制：--parallel 与 --concurrency 平衡资源。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| pnpm 与 Monorepo 工程化 | 001-PnpmMonorepoOverview | 本文自身 |
