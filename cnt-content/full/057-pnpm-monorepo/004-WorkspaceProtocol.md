---
order: 4
title: workspace 协议与内部依赖
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: intermediate
description: 'workspace: 协议用法、本地包引用与发布时版本转换'
author: fanquanpp
updated: '2026-08-01'
related:
  - pnpm-monorepo/003-WorkspaceSetup
  - pnpm-monorepo/005-CatalogManagement
  - pnpm-monorepo/007-ChangesetsRelease
prerequisites:
  - pnpm-monorepo/003-WorkspaceSetup
---
## 1. 什么是 workspace 协议

`workspace:` 是 pnpm（以及 yarn berry）在 package.json 中声明"依赖本仓库内另一个包"的专用协议。它让包之间的引用在开发时解析到本地源码目录，而不是去 npm registry 下载。

### 1.1 为什么不能直接写版本号

```json
{
  "dependencies": {
    "@fandex/utils": "^1.0.0"
  }
}
```

讲解：这样写，pnpm 会去 registry 查找 `@fandex/utils@^1.0.0`。如果该包从未发布，安装直接失败；即便发布了，版本也可能与本地源码不同步，违背"本地改完立即生效"的联调需求。工作空间内部引用必须使用 `workspace:` 协议。

## 2. 协议形式与语义

| 形式 | 语义 | 开发时解析 | 发布时转换 |
| ---- | ---- | ---- | ---- |
| `workspace:*` | 任意本地版本 | 本地包 | 替换为当前精确版本号，如 1.2.3 |
| `workspace:^` | 兼容范围内最新 | 本地包 | 替换为 `^1.2.3` |
| `workspace:~` | 补丁范围内最新 | 本地包 | 替换为 `~1.2.3` |

```json
{
  "dependencies": {
    "@fandex/utils": "workspace:*",
    "@fandex/tokens": "workspace:^"
  }
}
```

讲解：`workspace:*` 最常用，表示"只要本地有这个包就用它"；`workspace:^` 在发布后语义与 `^x.y.z` 等价，适合希望对共享包小版本升级敏感的库。开发阶段三者都解析到本地目录，行为差异只体现在发布产物中。

## 3. 本地包引用示例

### 3.1 添加内部依赖

```bash
# 语法：pnpm add <包名> --filter <目标包>
pnpm add @fandex/utils --filter @fandex/web
```

讲解：pnpm 检测到 `@fandex/utils` 是工作空间内的包，会自动写入 `workspace:*`，并把 node_modules 中对应目录符号链接到本地源码，改动即时生效。

### 3.2 引用共享包代码

```text
packages/
  utils/                 # @fandex/utils，导出工具函数
    package.json
    src/index.ts
  web/                   # @fandex/web，引用 utils
    package.json
    src/main.ts
```

```ts
// packages/web/src/main.ts：直接 import 共享包源码
import { formatId } from '@fandex/utils';
```

讲解：无需构建 utils 即可被 web 引用——只要构建工具（Vite、tsc）能解析符号链接到源码即可。若共享包需要先编译（如发布 CommonJS），则需要 `--topological build` 保证依赖先构建。

### 3.3 peerDependencies 场景

库类包（被他人安装的包）用 workspace 协议引用兄弟包时，更推荐放在 `peerDependencies` 中，避免打包进自己的产物，由使用者提供实现：

```json
{
  "peerDependencies": {
    "react": "^19.0.0"
  },
  "devDependencies": {
    "react": "workspace:*"
  }
}
```

讲解：peer 依赖声明"我要求对方环境里有 react"，devDependencies 中的 workspace 引用用于本地开发测试。

## 4. 发布时版本转换

运行 `pnpm publish` 或 `pnpm pack` 时，pnpm 会把 package.json 中的 `workspace:` 协议替换为实际版本：

```json
// 发布前（仓库内）
"@fandex/utils": "workspace:*"
```

```json
// 发布后（registry 上的产物）
"@fandex/utils": "1.2.3"
```

讲解：这一机制让"开发时用本地、发布后用真实版本"无缝衔接。用户从 registry 安装你的包时得到的是标准语义化版本依赖，任何包管理器（npm/yarn/pnpm）都能正常解析。转换只发生在发布产物中，仓库内文件不会被改写。

## 5. 内部依赖与幽灵依赖

工作空间包之间同样遵循严格隔离：web 引用 utils，但 utils 依赖的 lodash 对 web 不可见。web 若直接 import lodash，必须在自己的 package.json 中显式声明：

```bash
# 正确做法：谁使用谁声明
pnpm add lodash --filter @fandex/web
```

讲解：包间依赖是"代码依赖"与"依赖关系"两层。即便 utils 被链接到 web 的 node_modules，utils 的依赖树也不会向 web 暴露。保持每个包依赖自包含，是避免 Monorepo 幽灵依赖的关键。

## 6. 常见问题

问题一：循环依赖。A 依赖 B、B 依赖 A，拓扑构建无法排序。解决：重新分层，抽取共同依赖到更底层的 C。

问题二：误用 `file:` 协议。`file:../utils` 是复制/链接目录的快照语义，发布时不会转换版本，还会破坏符号链接结构。内部引用一律使用 `workspace:`。

问题三：版本不一致告警。多个包声明了不同版本的同一共享包，可运行 `pnpm why <包名>` 排查来源，再用 catalog 统一（见 005 篇）。

## 7. 参考资源

pnpm workspace 协议官方文档：https://pnpm.io/zh/workspaces

pnpm 过滤与 workspace 脚本：https://pnpm.io/zh/scripts

## 8. 小结

`workspace:*` 是 Monorepo 内部依赖的"正确打开方式"：开发时链接本地源码、发布时自动转换为真实版本。配合 `--filter` 精准管理每个包的依赖，配合 `--topological` 保证构建顺序，即可搭建健康的内部依赖体系。
