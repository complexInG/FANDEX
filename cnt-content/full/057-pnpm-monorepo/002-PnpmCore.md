---
order: 2
title: pnpm 核心特性
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: beginner
description: 'pnpm 核心机制：内容寻址存储、符号链接与严格依赖隔离'
author: fanquanpp
updated: '2026-08-01'
related:
  - pnpm-monorepo/003-WorkspaceSetup
  - pnpm-monorepo/004-WorkspaceProtocol
prerequisites:
  - getting-started/013-PackageManager
---
## 1. pnpm 是什么

pnpm 是 Node.js 生态的包管理器，与 npm、yarn 同类，但它通过"内容寻址存储 + 符号链接 + 严格依赖隔离"三套机制，从根源上解决了传统包管理器的两个痛点：磁盘浪费与幽灵依赖。

当前 pnpm 11.x 要求 Node.js 22 及以上版本，本身为纯 ESM 实现。相比 npm，pnpm 的优势并非"安装更快"这一个点，而是整体安装模型更正确：每个项目只声明并访问自己真正依赖的包。

### 1.1 与 npm 的定位差异

| 维度 | npm / yarn | pnpm |
| ---- | ---- | ---- |
| 磁盘占用 | 每项目各存一份，多项目重复 | 全局 store 只存一份，硬链接复用 |
| node_modules 结构 | 扁平提升 | 符号链接 + .pnpm 虚拟存储 |
| 幽灵依赖 | 普遍存在 | 结构上杜绝 |
| 适合场景 | 单包项目 | 单包与 Monorepo 均适合 |

## 2. 内容寻址存储（Content-Addressable Store）

### 2.1 工作原理

pnpm 将下载的依赖包内容存入一个全局 store，目录按内容哈希命名。同一个版本的包，无论被多少项目引用，在 store 中只有一份；项目安装时通过硬链接把 store 中的文件链接到自己的 node_modules。

```bash
# 查看 store 路径与使用情况
pnpm store path
pnpm store status
# 清理 store 中未被任何项目引用的孤儿包
pnpm store prune
```

讲解：`pnpm store path` 打印全局 store 目录；`prune` 会删除不再被引用的包，释放磁盘空间，可定期在 CI 或本地执行。

### 2.2 硬链接与节省磁盘

硬链接（hard link）让多个路径指向同一份物理数据，不复制内容。10 个项目都安装 lodash，磁盘上只有一份 lodash 数据；硬链接本身几乎不占空间。pnpm 11 将原来的"每包一个 JSON 索引"升级为单个 SQLite 数据库（store v11），安装时更少的系统调用，速度更快。

### 2.3 store 的共享前提

硬链接要求 store 与项目位于同一磁盘分区；跨盘符的项目无法硬链接，pnpm 会退回复制（copy）模式，此时节省磁盘的效果打折扣。Windows 上建议将 store 与工作目录放在同一盘符，或通过 `store-dir` 配置统一存放。

## 3. 符号链接 node_modules

### 3.1 三层结构

pnpm 的 node_modules 不再是扁平目录，而是由"直接依赖符号链接 + .pnpm 虚拟存储"组成：

```text
my-project/
  node_modules/
    .pnpm/                      # 虚拟存储：所有真实包文件按版本存放
      lodash@4.17.21/
      react@19.0.0/
    react -> .pnpm/react@19.0.0/node_modules/react   # 直接依赖符号链接
    lodash -> .pnpm/lodash@4.17.21/node_modules/lodash
```

讲解：node_modules 顶层只有 package.json 中显式声明的直接依赖（通过符号链接指向 .pnpm 内的真实文件）；间接依赖藏在 .pnpm 深处，对项目代码不可见。

### 3.2 版本共存

同一个包的不同版本可以并存于 .pnpm，例如 `react@18.0.0` 与 `react@19.0.0` 各自独立目录，互不干扰。这在 npm 扁平结构下需要复杂的提升策略才能勉强实现，pnpm 从结构上天然支持。

## 4. 严格依赖隔离

### 4.1 幽灵依赖问题

npm 把依赖扁平提升到根 node_modules，导致项目可以 import 自己没有声明的包——这就是幽灵依赖。本地开发时它"恰好能跑"，一旦某层依赖被移除或版本变化，项目在干净环境（如 CI）中突然报错。

```js
// 危险写法：react 并未声明在 package.json 中，却因提升而可见
import { useState } from 'react';
```

讲解：pnpm 下这种写法直接报"module not found"，因为顶层符号链接只暴露声明的依赖。错误在安装后立即暴露，而不是留到生产环境。

### 4.2 严格模式对比

pnpm 默认即严格隔离。若想恢复 npm 的扁平行为，可配置 `shamefully-hoist`，但会同时恢复幽灵依赖问题，生产项目不应使用。

```yaml
# pnpm-workspace.yaml（不推荐）
shamefully-hoist: true
```

讲解：该配置模拟 npm 扁平提升，仅用于迁移过渡或某些极端兼容场景；正常工程请保持默认严格模式。

## 5. 性能优势

第一，安装快：store 命中后无需重新下载，硬链接本地完成，速度接近秒级。

第二，磁盘省：多项目共享 store，node_modules 体积大幅小于 npm。

第三，构建快：严格的依赖声明让打包器（webpack、Vite）能更准确地分析模块图，配合只读的符号链接可减少文件监听开销。

第四，安全：pnpm 11 默认开启供应链保护，`minimumReleaseAge` 默认 1440（新发布不足 1 天的包不解析）、`blockExoticSubdeps` 默认开启，降低被投毒包攻击的风险。

## 6. 配置体系（.npmrc 与 pnpm 11）

### 6.1 pnpm 11 的配置变化

pnpm 11 将配置拆分为两类：`.npmrc` 只保留 registry 与认证相关配置；其余 pnpm 设置统一写在 `pnpm-workspace.yaml`（项目级）或全局 `config.yaml`（用户级）。环境变量统一使用 `pnpm_config_` 前缀。

```ini
# .npmrc：仅放 registry 与认证
registry=https://registry.npmjs.org/
//registry.npmjs.org/:_authToken=${PNPM_AUTH_TOKEN}
```

讲解：`${...}` 语法引用环境变量，避免把 token 硬编码进文件；token 通常通过 CI 的 secrets 注入。

### 6.2 常用设置示例

```yaml
# pnpm-workspace.yaml 中的 pnpm 设置
store-dir: .pnpm-store
virtual-store-dir: node_modules/.pnpm
allowBuilds:
  electron: true
  esbuild: false
```

讲解：pnpm 11 用 `allowBuilds` 白名单/黑名单统一管理依赖的构建脚本执行（替代旧版 onlyBuiltDependencies 等多项配置），只放行信任的包执行 postinstall。

## 7. 参考资源

pnpm 官方文档（中文）：https://pnpm.io/zh/

pnpm 11 发布说明：https://pnpm.io/blog/releases/11.0

pnpm 设置参考：https://pnpm.io/settings

## 8. 小结

pnpm 的三大核心机制——内容寻址存储、符号链接 node_modules、严格依赖隔离——共同解决了磁盘浪费与幽灵依赖两大工程问题。理解这些机制是掌握 Monorepo 工作空间的前提，下一节介绍如何用它配置多包工作空间。
