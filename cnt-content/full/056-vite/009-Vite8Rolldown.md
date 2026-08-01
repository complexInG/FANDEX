---
order: 9
title: Vite 8 与 Rolldown 新特性
module: vite
category: Vite
difficulty: intermediate
description: 'Vite 8 单引擎架构：Rolldown、Oxc、Lightning CSS、Bundled Dev Mode 与迁移指南'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/007-BuildSplit
  - vite/008-PluginSystem
prerequisites:
  - vite/002-QuickStart
  - vite/007-BuildSplit
---
## 1. Vite 8：一次历史性架构升级

Vite 8 于 2026 年 3 月 12 日正式发布，是自 Vite 2 以来最重大的架构变革。核心变化一句话：**开发与生产统一使用基于 Rust 的 Rolldown 作为唯一打包器**，彻底告别了持续多年的"开发用 esbuild、生产用 Rollup"双引擎架构。

```text
Vite 8 之前的双引擎：
  开发：esbuild（预构建、TS/JSX 转换）
  生产：Rollup（打包、代码分割、tree-shaking）
  痛点：两套转换管线、两套插件系统、dev/prod 行为不一致

Vite 8 的单引擎：
  开发 + 生产：Rolldown（Rust 编写，兼容 Rollup 插件 API）
  收益：行为一致、构建更快、插件生态不变
```

讲解：双引擎时代，"开发正常、上线报错"的根源在于两套管线对模块解析、代码分割边界、CJS 互操作的处理存在差异。单引擎让模块解析、代码分割与转换管线在开发和生产中完全一致，"本地能跑，上线就挂"这类问题从架构上被消除。

## 2. Rolldown：Rust 打包器

Rolldown 由 VoidZero 团队开发（同一团队维护 Oxc），与 Rollup 的关系是"功能兼容、性能超越"。

| 对比维度 | Rollup（旧） | Rolldown（Vite 8） |
| --- | --- | --- |
| 语言 | JavaScript | Rust |
| 相对构建速度 | 基线 | 快 10-30 倍（项目越大差距越大） |
| 插件 API | 兼容基线 | 完全兼容 Rollup/Vite 插件 API |
| 生态 | 成熟 | 可复用全部 Vite/Rollup 插件 |

真实案例数据（来源：官方博客与 VoidZero 技术博客）：

| 团队 | 效果 |
| --- | --- |
| Linear | 构建从 46 秒降至 6 秒 |
| Ramp | 构建时间减少 57% |
| Beehiiv | 构建时间减少 64% |
| Mercedes-Benz.io | 构建时间减少最多 38% |

讲解：性能提升来自 Rust 原生执行（解析、转换、压缩都在原生层完成），以及模块级持久化缓存——增量构建时无需重复处理未变化模块。典型中型 Vue/React 项目（50-100 个组件）构建时间从 8-12 秒降到 1-3 秒。

## 3. Oxc：统一的语言基础设施

Rolldown 的解析、转换与压缩全部构建在 **Oxc**（Rust 编写的 JS/TS 工具链）之上，替代了 esbuild 的角色：

```text
Oxc 生态全家桶：
  Oxc Parser      解析 JS/TS/JSX
  Oxc Transformer 转换 TS/JSX -> JS（替代 esbuild）
  Oxc Minifier    代码压缩（替代 terser/esbuild 压缩）
  Rolldown        打包（基于 Oxc）
  Oxlint          代码检查（ESLint 替代者）
  Oxfmt           代码格式化（Prettier 替代者）
```

讲解：整套工具共享同一个解析器、解析器与模块互操作层，从根上避免了 ESLint 与 Prettier 对代码解析不一致的历史问题。对 Vite 用户而言，最直接的感受是：**Vite 8 不再内置 esbuild**，TS/JSX 转换与压缩由 Rolldown 内部基于 Oxc 完成，功能等价但更快。

## 4. Lightning CSS 与 CSS 管线

Vite 8 的 CSS 压缩默认由 **Lightning CSS**（Rust 编写的 CSS 处理引擎）承担：

```text
Vite 8 CSS 管线：
  预处理器（sass/less）-> PostCSS 插件 -> Lightning CSS（压缩 + 降级 + 前缀）
```

讲解：以前需要额外安装 cssnano 压缩 CSS，Vite 8 内置的 Lightning CSS 已覆盖"压缩、autoprefixer、语法降级"等能力，多数项目不再需要单独配置。Vite 8.1 进一步推进"默认启用 Lightning CSS 转换"的实验，未来连 PostCSS 的日常角色都可能被逐步替代。

## 5. Bundled Dev Mode：大型应用新选项

Vite 以"不打包的开发服务器"闻名，但应用规模极大时（数千上万个模块），浏览器逐个请求模块的开销会拖慢启动与整页刷新。Vite 8.1 提供实验性的 **Bundled Dev Mode**（此前称 Full Bundle Mode），让开发环境也可以像生产一样打包输出。

```text
无打包 dev：浏览器按需请求每个模块（中小项目最优）
Bundled Dev：一次性打包再服务（大型应用启动/刷新更快，HMR 依然即时）
```

官方基准数据（应用含约 1 万个 React 组件时）：

| 指标 | 提升幅度 |
| --- | --- |
| 启动速度 | 约 15 倍 |
| 整页刷新 | 约 10 倍 |
| 网络请求数 | 减少到约 1/10 |
| HMR | 保持即时 |

讲解：实测中 Linear 团队冷启动渲染快 3 倍、整页刷新快约 40%。Bundled Dev Mode 目前在 Vite 8.1 中为实验性特性（侧重浏览器端与基础插件），大型单体应用可尝鲜，使用大量第三方插件的项目建议等待生态适配。除该模式外，Vite 8 系列还新增了实验性 chunk import map（提升缓存效率）与 Wasm ESM 集成支持。

## 6. 对插件生态的影响

Rolldown 在设计上以"Rollup 插件兼容"为第一目标，因此迁移成本很低：

```text
绝大多数现有 Vite/Rollup 插件在 Vite 8 中开箱即用，无需改动
```

两个值得了解的生态新特性：

```text
1. Hook Filters（钩子过滤）：
   插件声明 id/code/moduleType 过滤器后，不匹配的文件
   不再进入 JS 桥接层，插件再多也不线性拖慢构建

2. 内置 Rust 插件：
   replace 等高频场景提供 Rust 原生实现，配置更简单、性能更好

3. registry.vite.dev：
   官方插件目录，每日同步 npm 数据，可检索 Vite/Rolldown/Rollup 插件
```

讲解：Hook Filters 是 Rolldown 给插件作者的"性能福利"——以前每个插件都要对每个模块执行一次 JS 调用，现在过滤器直接在 Rust 层拦截。对普通使用者而言，只需知道：升级到 Vite 8 后插件照常工作，但建议同步升级插件到兼容版本。

## 7. 升级迁移指南

从 Vite 7 升级到 Vite 8 总体是平滑的：

```bash
# 1. 升级核心与框架插件
pnpm add -D vite@latest @vitejs/plugin-react@latest
# 或 Vue 项目
pnpm add -D vite@latest @vitejs/plugin-vue@latest
```

```text
2. 检查要点（官方迁移指南）：
   - 配置文件 vite.config.ts 通常无需改动（rollupOptions 等保持兼容）
   - 确认 Node 版本满足要求（20.19+ 或 22.12+）
   - 删除或替换依赖 esbuild 专属行为的代码（Vite 8 不再内置 esbuild）
   - 第三方插件升级到最新版，冷门插件如异常再查官方兼容性说明
```

讲解：Vite 8 无需任何 opt-in 标记，Rolldown 即为默认打包器；配置层面 `rollupOptions`、插件钩子等沿用 Rollup 语义。升级后建议对比产物体积与行为——Rolldown 默认启用更激进的死代码消除与常量内联，产物通常更小；若某个边界行为与旧版本不同，可在官方迁移指南中确认是否已知变更。

## 8. 内置 devtools 与调试体验

Vite 8 内置了 **Vite Devtools**（浏览器扩展形态），调试体验更接近"开箱即用"：

```text
常用能力：
  查看模块依赖图与转换结果
  查看/触发依赖预构建
  检查 HMR 边界与更新事件
  分析构建产物 chunk 构成
```

讲解：内置 devtools 替代了以往需要单独安装浏览器扩展的方式，配合终端日志（如 `vite --debug`）可完整观察模块图与构建管线。这也是 008 篇"钩子机制"的最佳可视化学习工具。

## 9. 参考资源

Vite 8 发布公告：https://vite.dev/blog/announcing-vite8

Vite 升级迁移指南：https://vite.dev/guide/migration

Rolldown 官方文档：https://rolldown.rs/

VoidZero 技术博客：https://voidzero.dev/posts

Vite 中文文档：https://cn.vite.dev/
