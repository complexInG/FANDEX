---
order: 7
title: changesets 版本管理与发布
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: intermediate
description: 'changesets 版本管理：变更记录、版本 bump、CHANGELOG 生成与 npm 发布流程'
author: fanquanpp
updated: '2026-08-01'
related:
  - pnpm-monorepo/004-WorkspaceProtocol
  - pnpm-monorepo/005-CatalogManagement
  - pnpm-monorepo/008-MonorepoPractice
prerequisites:
  - pnpm-monorepo/003-WorkspaceSetup
---
## 1. changesets 是什么

changesets 是 Monorepo 版本管理与发布的社区标准方案。它把"发版"拆成两个环节：开发者在 PR 中记录变更意图（changeset），发版时统一计算各包的新版本并生成 CHANGELOG。

### 1.1 解决的问题

手工维护多包版本号容易出错：漏改某个依赖该包的版本引用、CHANGELOG 缺失、版本号冲突。changesets 用"变更集文件 + 自动版本计算"消除这些问题，并与 `workspace:` 协议发布转换天然配合。

## 2. 安装与配置

```bash
pnpm add -D @changesets/cli -w
pnpm changeset init
```

讲解：`init` 生成 `.changeset/config.json` 与 README。config.json 是发布行为的唯一配置入口。

```json
// .changeset/config.json
{
  "$schema": "https://unpkg.com/@changesets/config@3.0.0/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}
```

讲解：`access: "public"` 表示发布公开包（私有 scope 包需配合 npm 组织账号）；`baseBranch` 指明主分支名，用于计算变更范围；`updateInternalDependencies: "patch"` 表示内部依赖的 workspace 引用随版本变更同步更新到 patch 级别。

## 3. 记录变更：changeset add

### 3.1 交互式创建

```bash
pnpm changeset
# 或
pnpm changeset add
```

讲解：进入交互式界面：选择本次变更涉及哪些包、选择 bump 级别（major/minor/patch）、填写变更说明。完成后在 `.changeset/` 目录生成一个随机命名的 markdown 文件。

### 3.2 changeset 文件结构

```markdown
---
'@fandex/utils': minor
'@fandex/web': patch
---

新增 ID 格式化工具函数，修复 web 端日期显示问题。
```

讲解：frontmatter 中 `包名: 级别` 声明各包的版本提升类型；正文是变更说明，会被写入 CHANGELOG。多个 PR 各带一个 changeset 文件，互不冲突。

### 3.3 bump 级别选择

| 级别 | 触发条件 | 版本变化 |
| ---- | ---- | ---- |
| major | 破坏性变更（API 不兼容） | 1.0.0 → 2.0.0 |
| minor | 新增功能，向后兼容 | 1.0.0 → 1.1.0 |
| patch | 修复 bug，向后兼容 | 1.0.0 → 1.0.1 |

讲解：遵循语义化版本（SemVer）。不破坏兼容的新特性用 minor，bug 修复用 patch；破坏性 API 变更必须 major。

## 4. 版本管理：changeset version

发版时执行：

```bash
pnpm changeset version
```

讲解：消费所有待处理的 changeset 文件：更新各包 package.json 版本号、生成/追加 CHANGELOG.md、移除已处理的 changeset 文件。如果包 A 被包 B 以 `workspace:*` 引用，B 的依赖版本引用会同步更新。

```bash
git add .
git commit -m "chore: version packages"
```

讲解：version 只是修改版本元数据，不会发布；版本变更应作为一个独立 commit 提交，通常由 CI 自动完成。

## 5. 发布：changeset publish

```bash
pnpm changeset publish
```

讲解：按依赖拓扑顺序对"版本号高于 registry 中已有版本"的包执行 `pnpm publish`。发布时 pnpm 会把 `workspace:*` 转换为真实版本号（见 004 篇），消费者可正常安装。

### 5.1 发布前置条件

```json
// 各包 package.json 中补充发布元信息
{
  "name": "@fandex/utils",
  "version": "1.2.3",
  "publishConfig": {
    "access": "public"
  }
}
```

讲解：私有 scope（`@fandex/*`）发布到 npm 默认私有，需在 publishConfig 中声明 `access: "public"`。同时确认登录状态：`pnpm publish` 需要 npm 认证，pnpm 11 已原生实现登录/发布流程，不再依赖 npm CLI。

## 6. CI 自动化

标准的发布流水线分为两个 Job：

### 6.1 PR 检查

PR 中必须包含 changeset（或标记为 no-release）；合并后触发版本 Job：

```yaml
# .github/workflows/release.yml 片段
name: Release
on:
  push:
    branches: [main]
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: 11
      - uses: changesets/action@v1
        with:
          version: pnpm changeset version
          publish: pnpm changeset publish
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

讲解：changesets/action 检测 main 上存在待处理 changeset 时：先执行 version（创建"版本发布"PR 或直接提交），随后执行 publish 发布到 npm，并自动创建 GitHub Release。

## 7. 最佳实践

第一，每个 PR 都应附带 changeset；不涉及发版的改动（如文档）可运行 `pnpm changeset add --empty` 生成空 changeset 跳过发布。

第二，fixed 与 linked 配置用于"必须同版本发布"的包组（fixed 强制同版本、linked 仅同步 bump），谨慎使用。

第三，发布 tag：`changeset version` 默认不打 Git tag，可在 CI 中 `pnpm changeset tag` 补打，便于回滚定位。

## 8. 参考资源

Changesets 官方文档：https://changesets-docs.vercel.app/

Changesets GitHub 仓库：https://github.com/changesets/changesets

## 9. 小结

changesets 让 Monorepo 发版可追溯、可自动化：开发期提交变更集，合并后 CI 统一计算版本、生成 CHANGELOG、按拓扑发布。配合 pnpm 的 `workspace:` 协议转换，形成从代码合并到 npm 上线的完整闭环。
