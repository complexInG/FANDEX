---
order: 6
title: Turborepo 任务编排
module: pnpm-monorepo
category: pnpm 与 Monorepo
difficulty: intermediate
description: 'Turborepo 任务编排：turbo.json、tasks 配置、dependsOn 依赖与缓存机制'
author: fanquanpp
updated: '2026-08-01'
related:
  - pnpm-monorepo/003-WorkspaceSetup
  - pnpm-monorepo/008-MonorepoPractice
prerequisites:
  - pnpm-monorepo/003-WorkspaceSetup
---
## 1. 为什么需要任务编排

pnpm 的 `-r --topological build` 能按依赖顺序构建，但每次改动都会全量重跑所有包的任务。随着包数量增长，CI 时间线性膨胀。Turborepo 在 pnpm 之上增加了两层能力：任务依赖图编排与基于哈希的构建缓存。

### 1.1 pnpm 原生的局限

pnpm 只管"安装依赖、按拓扑跑脚本"，不知道构建产物是什么、是否可以被复用。Turborepo 接管"跑什么、先跑谁、能否跳过"的决策，pnpm 仍负责依赖安装，二者分工互补。

## 2. 安装与初始化

```bash
pnpm add -D turbo -w
npx turbo init
```

讲解：turbo 作为根包的 devDependencies 安装（`-w` 写到根 package.json）；`turbo init` 生成最小化的 turbo.json。

## 3. tasks 配置

turbo.json 中的 `tasks` 字段（Turbo 2.x 语法，旧版为 pipeline）声明每个任务的行为：

```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": []
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

讲解：`build` 的 `dependsOn: ["^build"]` 表示"先构建所有依赖我的包"（`^` 前缀代表依赖关系方向）；`outputs` 声明任务产生的文件，用于缓存恢复；`dev` 是长驻进程，`cache: false` 不缓存、`persistent: true` 标记为不退出任务。

### 3.1 dependsOn 规则

| 写法 | 含义 |
| ---- | ---- |
| `dependsOn: []` | 无依赖，可并行 |
| `dependsOn: ["^build"]` | 先执行所有被依赖包（依赖我的）的 build |
| `dependsOn: ["build"]` | 先执行本包自己的 build |
| `dependsOn: ["^build", "lint"]` | 组合：先依赖包 build，再本包 lint |

讲解：`^` 前缀的语义与 pnpm 的拓扑排序一致，但 turbo 的调度粒度更细，还能在依赖图之外组合本包内的任务顺序。

## 4. 缓存机制

### 4.1 本地缓存

turbo 以"任务输入指纹"决定是否命中缓存：指纹包括源码文件内容、依赖版本、环境变量、turbo.json 配置等。命中时直接从缓存目录恢复 `outputs` 声明的内容，跳过执行：

```bash
turbo run build        # 未变更的包显示 FULL TURBO，毫秒级完成
turbo run build --force # 强制全部重跑，忽略缓存
```

讲解：第二次运行同一任务时，未改动的包直接命中缓存（输出 FULL TURBO），只有真正变更的包才执行，CI 提速可达数量级。

### 4.2 远程缓存

远程缓存把缓存产物上传到共享存储（Vercel Remote Caching、自建服务或任意支持该协议的对象存储），让 CI 与本地共享缓存：

```bash
turbo login            # 登录 Vercel 账号
turbo link             # 关联远程缓存
```

讲解：团队每个成员的本地缓存互不共享，远程缓存让"CI 构建过的包，本地直接复用"成为可能。注意远程缓存仅缓存构建产物，不涉及源码上传。

### 4.3 inputs 精确控制

```json
{
  "tasks": {
    "build": {
      "inputs": ["src/**", "tsconfig.json", "package.json"],
      "outputs": ["dist/**"]
    }
  }
}
```

讲解：`inputs` 限定参与指纹计算的路径，例如 README 改动不影响 build 指纹；精确的 inputs 能提高缓存命中率，避免无效重跑。

## 5. 常用命令

```bash
turbo run build            # 运行所有包的 build（等效 turbo build）
turbo build test lint      # 一次运行多个任务
turbo run build --filter=@fandex/web   # 只跑指定包及其依赖的任务
turbo run build --affected # 只跑相对 base 分支有变更的包
turbo run dev --parallel   # 并行启动多个 dev 进程
turbo run build --dry      # 预览执行计划，不真正执行
```

讲解：`--affected` 结合 Git 比较（默认 `--base` 指向 main）圈定变更范围，是 CI 按变更集构建的核心；`--dry` 打印计划图，便于调试依赖关系。

## 6. 与 pnpm 原生能力对比

| 能力 | pnpm -r | Turborepo |
| ---- | ---- | ---- |
| 依赖拓扑排序 | 支持 | 支持且更细粒度 |
| 任务缓存 | 无 | 本地 + 远程 |
| 并行调度 | 支持 | 支持 |
| 增量构建 | 无 | 缓存跳过 |
| 产物声明 | 无 | outputs |

讲解：小型 Monorepo 用 pnpm 原生脚本足够；超过 10 个包或 CI 变慢时，引入 Turborepo 收益明显。二者完全兼容：turbo 内部仍调用各包的 package.json scripts。

## 7. 参考资源

Turborepo 官方文档：https://turborepo.com/docs

Turborepo 缓存文档：https://turborepo.com/docs/caching

turbo.json 配置参考：https://turborepo.com/docs/reference/configuration

## 8. 小结

Turborepo 用 `tasks` 声明任务依赖、用哈希指纹缓存产物、用远程缓存共享加速，是 pnpm Monorepo 的标准任务编排搭档。构建产物缓存与"变更集驱动"的结合，让大规模仓库的 CI 保持在分钟级以内。
