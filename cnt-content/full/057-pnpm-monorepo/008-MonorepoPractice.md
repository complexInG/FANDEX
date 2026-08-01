---
order: 8
title: Monorepo 实战
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: intermediate
description: 'Monorepo 实战：apps/packages 结构设计、共享包示例与 CI 优化'
author: fanquanpp
updated: '2026-08-01'
related:
  - pnpm-monorepo/006-TurborepoTasks
  - pnpm-monorepo/007-ChangesetsRelease
prerequisites:
  - pnpm-monorepo/003-WorkspaceSetup
---
## 1. 目录结构设计

### 1.1 通用布局：apps 与 packages

成熟的 Monorepo 通常按"可部署物"与"可复用物"划分目录：

```text
my-monorepo/
  apps/                    # 可部署的应用
    web/                   # Web 应用
    docs/                  # 文档站
  packages/                # 可复用的共享库
    ui/                    # UI 组件库
    utils/                 # 工具函数
    config/                # 共享配置（eslint、tsconfig）
  tools/                   # 内部工具脚本
  pnpm-workspace.yaml
  turbo.json
  package.json
  .changeset/
```

讲解：`apps` 只放最终运行的产物（应用、站点），`packages` 放被应用的共享库。共享库独立发布（private 为 false 的除外），应用通常 private 不发布。这一约定让依赖方向清晰：apps 依赖 packages，packages 之间尽量单向。

### 1.2 工作空间声明

```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
  - 'tools/*'
```

讲解：glob 覆盖全部子目录；新增目录（如 apps/mobile）无需改配置，自动纳入工作空间。

## 2. 共享包示例

### 2.1 共享工具包

```json
// packages/utils/package.json
{
  "name": "@fandex/utils",
  "version": "1.2.3",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "scripts": {
    "build": "tsc -p tsconfig.json"
  }
}
```

```ts
// packages/utils/src/format.ts
export function formatId(id: string): string {
  return id.toUpperCase();
}
```

讲解：共享包声明 `main`/`types` 指向构建产物，消费方（app 或兄弟包）在编译后 import。共享包统一用 `@scope/` 命名空间前缀，便于识别与 scope 级权限管理。

### 2.2 应用引用共享包

```json
// apps/web/package.json
{
  "name": "@fandex/web",
  "dependencies": {
    "@fandex/utils": "workspace:*"
  },
  "scripts": {
    "build": "vite build"
  }
}
```

讲解：`workspace:*` 保证开发时解析到本地源码（004 篇），发布时自动转换。共享包改动无需发布即可被应用联调，这是 Monorepo 的核心价值。

## 3. 根脚本与开发体验

```json
// 根 package.json
{
  "private": true,
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev --parallel",
    "lint": "turbo run lint",
    "test": "turbo run test",
    "changeset": "changeset",
    "release": "changeset version && changeset publish"
  }
}
```

讲解：根脚本用 turbo 统一下发到各包；`turbo run dev --parallel` 一次启动所有应用开发服务器。新人只需记住 `pnpm install`、`pnpm dev`、`pnpm build` 三个命令即可上手。

## 4. CI 优化

### 4.1 安装与构建

```yaml
# .github/workflows/ci.yml 核心片段
steps:
  - uses: pnpm/action-setup@v4
    with:
      version: 11
  - uses: actions/setup-node@v4
    with:
      node-version: 22
      cache: pnpm
  - run: pnpm install --frozen-lockfile
  - run: turbo run lint test build --affected
```

讲解：`cache: pnpm` 让 GitHub Actions 缓存 pnpm store，安装秒级完成；`--frozen-lockfile` 保证可复现；`--affected` 只构建本次变更涉及的包，未变更包直接命中 turbo 缓存（006 篇）。

### 4.2 远程缓存接入

```yaml
env:
  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
  TURBO_TEAM: ${{ secrets.TURBO_TEAM }}
  TURBO_REMOTE_CACHE_ONLY: "true"
```

讲解：配置远程缓存后，CI 与本地共享构建产物；`TURBO_REMOTE_CACHE_ONLY` 让 CI 只读不写，避免多 Job 并发写冲突。

### 4.3 发布流水线

发布 Job 独立于 CI：CI 保证质量，发布 Job（changesets/action）负责版本计算与 npm 发布（007 篇），互不阻塞。

## 5. 常见问题与解决

| 问题 | 现象 | 解决 |
| ---- | ---- | ---- |
| 幽灵依赖 | 本地能跑、干净环境报 module not found | 保持严格隔离，谁使用谁声明，禁用 shamefully-hoist |
| 构建顺序错误 | 应用先构建找不到共享包产物 | 用 turbo dependsOn 或 pnpm --topological |
| 循环依赖 | 拓扑构建死循环 | 抽取共同部分下沉，重构包分层 |
| 版本漂移 | 多包 react 版本不一致 | 用 catalog + catalogMode: strict（005 篇） |
| lockfile 冲突 | 合并后 pnpm-lock.yaml 冲突 | 重新执行 pnpm install 自动修复，勿手改 |
| peer 依赖缺失 | 库类包运行时报找不到 react | 声明 peerDependencies，devDependencies 提供测试版本 |
| CI 全量重跑 | 小改动触发全仓构建 | turbo --affected + 远程缓存 |

### 5.1 依赖分析工具

```bash
pnpm why react          # 查看 react 被谁依赖、什么版本
pnpm list -r --depth 1  # 查看各包直接依赖
pnpm outdated -r        # 查看可升级的依赖
```

讲解：版本排查三连。配合 catalog 统一升级，多数版本问题在安装阶段就能被 pnpm 发现。

## 6. 参考资源

pnpm 官方文档（中文）：https://pnpm.io/zh/

Turborepo 官方文档：https://turborepo.com/docs

Changesets 官方文档：https://changesets-docs.vercel.app/

## 7. 小结

实战要点可归纳为四句话：目录分层（apps/packages）、依赖自包含（workspace: + catalog）、任务编排（turbo）、版本自动化（changesets）。从本模块 002 篇的底层机制到本篇的完整工程拼图，pnpm Monorepo 体系即可落地为可维护、可扩展、可自动化的生产级工程。
