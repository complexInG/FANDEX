---
order: 7
title: Vite 生产构建与代码分割
module: vite
category: Vite
difficulty: intermediate
description: 'Vite 生产构建：build 配置、输出目录、chunk 拆分、tree-shaking 与压缩'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/009-Vite8Rolldown
  - vite/008-PluginSystem
prerequisites:
  - vite/003-ConfigFile
---
## 1. 生产构建做了什么

`vite build` 把开发产物转换成可上线的优化版本，整个流程在 Vite 8 中由 **Rolldown** 统一完成（001 篇提到 Vite 8 之前的双引擎时代，009 篇详述单引擎架构）。一次构建包含：

```text
vite build 的执行链：
1. 入口分析：从 index.html 追踪所有模块
2. 转换与解析：TS/JSX 转 JS、处理 import 图
3. tree-shaking：删除未使用的代码
4. 代码分割：按动态 import 边界拆分 chunk
5. 压缩：JS/CSS 压缩 + 资源哈希
6. 输出到 dist/（默认）
```

讲解：开发环境（dev）不打包、按需转换；生产构建则相反——完整打包、深度优化。两者行为在 Vite 8 中由同一打包器承担，开发与生产行为差异大幅缩小。

## 2. build 配置核心项

```ts
// vite.config.ts
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    outDir: 'dist',            // 输出目录（相对项目根）
    assetsDir: 'assets',       // 静态资源子目录
    sourcemap: false,          // 是否生成 sourcemap，调试用 'hidden'
    minify: true,              // 是否压缩 JS
    target: 'baseline-widely-available', // 编译目标浏览器
    cssCodeSplit: true,        // CSS 代码分割（005 篇已述）
    assetsInlineLimit: 4096,   // 小于 4KB 的资源内联为 base64
    chunkSizeWarningLimit: 500, // chunk 超过 500KB 时警告
  },
})
```

| 选项 | 说明 |
| --- | --- |
| `outDir` | 构建产物目录，构建前自动清空该目录 |
| `sourcemap` | `true` 生成 .map 文件；`'hidden'` 生成但不写注释（避免暴露源码） |
| `target` | 目标浏览器语法，Vite 8 默认 `'baseline-widely-available'`（即大多数现代浏览器） |
| `emptyOutDir` | 默认 true，构建前清空 outDir（位于项目根目录之外时需显式开启） |

讲解：`sourcemap: 'hidden'` 适合线上排查错误但不想让源码映射对用户可见的场景；`minify` 在 Vite 8 中由 Rolldown 原生执行（基于 Oxc），不再依赖单独压缩器。

## 3. 代码分割：chunk 拆分

代码分割的目标是"按需加载 + 缓存复用"。三种主要手段：

### 3.1 动态 import（自动分割）

```ts
// 路由级懒加载：每个页面独立成 chunk
const UserPage = () => import('./pages/UserPage')
// React 写法
import { lazy } from 'react'
const UserPage = lazy(() => import('./pages/UserPage'))
```

讲解：`import()` 是代码分割的天然边界，构建时自动拆出独立 chunk 并按需加载。大型应用应保证"一个路由一个 chunk"。

### 3.2 自动 chunk 拆分（vendor）

Vite 默认会把 `node_modules` 中的依赖拆到 `vendor` chunk，使第三方库与业务代码分离，业务发布后浏览器可长期缓存 vendor。

### 3.3 manualChunks：手动分组

需要精细控制时用 `output.manualChunks`（Vite 8 由 Rolldown 支持，还新增了 Webpack 风格的 `advancedChunks` 规则，见 009 篇）：

```ts
// vite.config.ts
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // 将 echarts 及其子依赖合并为独立 chunk
          charts: ['echarts', 'echarts-gl'],
          // 将 UI 库单独拆出
          ui: ['antd', '@ant-design/icons'],
        },
      },
    },
  },
})
```

讲解：配置名仍叫 `rollupOptions`（Vite 8 中作为 Rolldown 的兼容入口，保持插件与配置兼容）。按"库"拆分能最大化缓存命中——某个库升级只重下对应 chunk。

## 4. tree-shaking：消除无用代码

tree-shaking 依赖 ES Module 的静态结构（`import`/`export` 在编译期确定），构建时删除"被引入但从未使用"的代码：

```ts
// utils.ts
export function used() { return 'ok' }
export function unused() { return 'dead code' }   // 会被删除

// main.ts
import { used } from './utils'
console.log(used())
```

讲解：只有通过 ESM `import` 导出的纯函数/常量能被可靠删除。为保证效果，请做到：使用 ESM 语法（勿用 CommonJS）；避免模块顶层产生副作用；第三方库选择提供 ESM 产物的版本。Rolldown 在 Vite 8 中还默认启用了更强的死代码消除与常量内联，产物体积进一步下降。

## 5. 资源压缩

| 产物类型 | 压缩方式 | 说明 |
| --- | --- | --- |
| JS | Rolldown 内置压缩（Oxc 实现） | 无需额外依赖 |
| CSS | Lightning CSS 压缩 | 默认启用，无需配置 |
| 图片/字体 | 不压缩（原样复制） | 需用图片优化插件 |
| HTML | 极简压缩 | 保留必要结构 |

讲解：Vite 8 不再依赖 esbuild 压缩 JS、也不再需要 cssnano——两者分别被 Rolldown（Oxc）与 Lightning CSS 取代。图片压缩不是 Vite 内置能力，可选用 `vite-plugin-imagemin` 或构建前处理。

## 6. 分析产物体积

终端输出的构建报告只到 chunk 级别，深入分析用可视化插件：

```bash
pnpm add -D rollup-plugin-visualizer
```

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import { visualizer } from 'rollup-plugin-visualizer'

export default defineConfig({
  plugins: [visualizer({ open: true })],  // 构建后自动打开分析页面
})
```

讲解：visualizer 生成交互式 treemap，能直观看到"哪个依赖占了多少体积"，是定位超大 chunk 的必备工具。Vite 8 还提供官方插件目录 https://registry.vite.dev/ 可按功能检索同类插件。

## 7. 常见陷阱

陷阱一：vendor chunk 过大。用 manualChunks 拆分按库分组，或用动态 import 降首屏体积。

陷阱二：构建成功但上线 404。检查 `base` 配置与部署子路径是否一致（004 篇）。

陷阱三：tree-shaking 失效。检查依赖是否为 ESM、模块是否有副作用，必要时配置 `build.rollupOptions.treeshake`。

陷阱四：console 与 debugger 残留。生产构建默认移除 `console.log`（可配 `esbuild` 相关选项调整），确认符合团队约定。

## 8. 参考资源

Vite 构建选项：https://vite.dev/config/build-options

Vite 部署指南：https://vite.dev/guide/static-deploy

Vite 中文文档：https://cn.vite.dev/
