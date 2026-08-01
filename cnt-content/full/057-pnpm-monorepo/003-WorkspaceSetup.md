---
order: 3
title: 工作空间配置
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: beginner
description: 'pnpm workspace 配置：pnpm-workspace.yaml、packages 模式与安装命令'
author: fanquanpp
updated: '2026-08-01'
related:
  - pnpm-monorepo/002-PnpmCore
  - pnpm-monorepo/004-WorkspaceProtocol
  - pnpm-monorepo/005-CatalogManagement
prerequisites:
  - getting-started/013-PackageManager
---
## 1. 什么是工作空间

工作空间（workspace）是 pnpm 的多包管理能力：在同一个仓库里管理多个相互独立的包，这些包共享一份 `pnpm-lock.yaml`，依赖统一安装、统一解析。它是 Monorepo 工程模式的基石。

没有 workspace 时，每个子项目各自 `npm install`，会产生 N 份重复的 node_modules；有了 workspace，pnpm 一次 `pnpm install` 即可为全部包生成依赖，并通过符号链接让包之间互相引用（详见 004 篇）。

### 1.1 最小工作空间的三个文件

一个 pnpm workspace 至少包含：`pnpm-workspace.yaml`（声明哪些目录是包）、根 `package.json`（公共脚本与元数据）、`pnpm-lock.yaml`（由 pnpm 自动生成，必须提交到版本库）。

## 2. pnpm-workspace.yaml 配置

### 2.1 packages 模式

`packages` 字段用 glob 模式声明工作空间包含哪些目录：

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'          # 所有应用：apps/web、apps/docs
  - 'packages/*'      # 所有共享库：packages/utils、packages/ui
  - 'tools/*'         # 工具链
  - '!apps/legacy'    # 感叹号排除不需要纳入的目录
```

讲解：每个匹配到的目录都要求包含一个 package.json，被视为工作空间的一个包；`!` 前缀用于排除目录。glob 模式支持 `*`（单层）与 `**`（递归多层）。

### 2.2 常见模式示例

```yaml
packages:
  - 'app-*'           # FANDEX 风格：app-web、app-desktop 等前缀匹配
  - 'shd-shared'      # 单目录
  - 'shd-shared/*'
  - 'thd-third-party/*'
```

讲解：可以同时写多种模式，覆盖不同命名风格；注意 `shd-shared` 与 `shd-shared/*` 同时出现表示共享层自身的 package.json 及其子包都纳入工作空间。

## 3. 根 package.json

### 3.1 private 与 packageManager

```json
{
  "name": "fandex-monorepo",
  "private": true,
  "packageManager": "pnpm@11.0.0",
  "engines": {
    "node": ">=22"
  },
  "scripts": {
    "build": "pnpm -r --topological build",
    "dev:web": "pnpm --filter @fandex/web dev"
  }
}
```

讲解：`private: true` 防止根包被误发布到 npm；`packageManager` 字段配合 Corepack 固定 pnpm 版本，保证团队与 CI 使用同一版本；`engines.node` 声明 Node 最低版本。

### 3.2 根目录不要放业务依赖

根 package.json 只放工程级依赖（构建、lint、类型检查等开发工具），业务依赖应归属到具体包。根目录的依赖会暴露给所有包（提升），滥用会导致依赖职责混乱。

## 4. 安装命令 pnpm install

### 4.1 首次安装与增量安装

```bash
pnpm install            # 安装所有包的依赖，生成/更新 pnpm-lock.yaml
pnpm install -w         # 给根包安装开发依赖（-w 表示 workspace root）
```

讲解：`-w`（--workspace-root）把依赖加到根 package.json；不带参数时 pnpm 会读取全部包的依赖一次性安装。

### 4.2 锁定文件与冻结安装

```bash
# CI 或生产环境：严格按照 lockfile 安装，任何偏差直接报错
pnpm install --frozen-lockfile
```

讲解：`--frozen-lockfile` 不修改 pnpm-lock.yaml，若 lockfile 与 package.json 不一致则安装失败。CI 中必须使用，保证团队与线上环境依赖完全一致。

### 4.3 pnpm-lock.yaml 必须入库

pnpm-lock.yaml 记录了整个工作空间解析后的精确依赖树，是"可复现安装"的唯一依据。它应提交到 Git；不要把它加入 .gitignore。合并冲突时可运行 `pnpm install` 自动修复（lockfile 冲突通常可直接重新生成局部差异）。

## 5. 常用脚本与过滤

### 5.1 递归执行：-r

```bash
pnpm -r build               # 对所有包执行 build
pnpm -r --topological build # 按依赖拓扑顺序：先依赖后应用
pnpm -r --parallel lint     # 并行执行互不依赖的 lint
```

讲解：`--topological` 保证先构建被依赖的包，避免应用先构建却找不到依赖产物；`--parallel` 忽略拓扑关系并行执行，适合 lint 这类无依赖任务。

### 5.2 按包过滤：--filter / -F

```bash
pnpm -F @fandex/web dev          # 只运行 web 包的 dev
pnpm -F @fandex/utils add lodash # 给 utils 包添加依赖
pnpm -F @fandex/web --filter "…{@fandex/utils}…" test  # 连同依赖一起
```

讲解：`-F` 精确选中一个包；花括号过滤语法可以按依赖关系圈定范围，例如 `@{包}…` 表示该包及其依赖、`…{包}` 表示依赖它的包。

### 5.3 常用命令速查

| 命令 | 作用 |
| ---- | ---- |
| `pnpm -r build` | 所有包构建 |
| `pnpm -F <pkg> dev` | 单包开发 |
| `pnpm why <dep>` | 查看某个依赖的来源与版本 |
| `pnpm list -r` | 列出所有包及依赖 |
| `pnpm update` | 更新 lockfile 中的依赖版本 |
| `pnpm remove <dep> -F <pkg>` | 移除指定包依赖 |

## 6. 参考资源

pnpm workspaces 官方文档：https://pnpm.io/zh/workspaces

pnpm 过滤语法：https://pnpm.io/zh/filtering

pnpm CLI 命令参考：https://pnpm.io/zh/cli/install

## 7. 小结

工作空间由 `pnpm-workspace.yaml` 声明包范围、根 package.json 统一脚本、`pnpm-lock.yaml` 锁定依赖三部分组成。`-r`、`--filter`、`--topological` 是日常操作三件套。下一节讲解包之间如何通过 `workspace:` 协议互相引用。
