---
order: 1
title: Vite 构建工具概述
module: vite
category: Vite
difficulty: beginner
description: 'Vite 构建工具概述：开发服务器、HMR、依赖预构建、生产构建与工程配置'
author: fanquanpp
updated: '2026-08-01'
related:
  - javascript/JavaScript基础
  - typescript/TypeScript基础
  - astro/Astro框架概述
  - pnpm-monorepo/pnpm与Monorepo工程化
prerequisites:
  - javascript/JavaScript基础
---
## 0. 零基础入门（从零开始）

### 0.1 零基础起点

本模块讲解 Vite 构建工具。零基础可学，但需要：已安装 Node.js 18+、pnpm，并至少写过一次简单的 HTML/JavaScript（见 006-html5 与 008-javascript 模块）。
Vite 解决什么问题：现代前端项目文件很多、依赖很多，需要一个工具把几十个文件“组装”成浏览器能直接运行的样子，并在开发时即时预览。Vite 就是当前最主流的这个工具。

### 0.2 第一个 Vite 项目

```bash
# 用模板创建项目（这里选 react-ts：React + TypeScript）
pnpm create vite my-app --template react-ts
# 安装依赖并启动开发服务器
cd my-app && pnpm install && pnpm dev
# 浏览器打开 http://localhost:5173 即可看到页面
```

create vite 是官方脚手架命令，--template react-ts 指定项目模板；模板决定语言与框架的初始配置。
pnpm install 安装 package.json 中声明的所有依赖，生成 node_modules 目录。
pnpm dev 启动 Vite 开发服务器：它不会打包整个项目，而是按需把浏览器请求的文件即时转换返回，所以冷启动只需几百毫秒。
修改 src 下的任意文件，页面会毫秒级热更新（HMR），且不会丢失页面状态——这是 Vite 对比旧工具最大的体验优势。
开发完成后再用 pnpm build 生成生产版本：Vite 会调用 Rollup 做压缩、代码分割等优化，输出到 dist 目录。

## 1. Vite 是什么

Vite（法语“快”的意思）是尤雨溪于 2020 年发布的下一代前端构建工具，2021 年起成为 Vue 官方推荐，随后被 React、Svelte、Astro 等生态广泛采用。它的核心创新是：开发环境基于原生 ES Modules，按需编译；生产环境基于 Rollup，深度优化。

Vite 由两部分组成：

开发服务器：冷启动快、HMR 毫秒级；

构建器：`vite build` 调用 Rollup 输出生产优化产物。

## 2. 为什么需要 Vite：打包器的困境

Webpack 等传统打包器在开发时把整个应用打包成 bundle，项目越大启动越慢；热更新也要重新打包受影响部分。Vite 利用浏览器原生 ESM 支持，让浏览器直接按需请求模块，服务器只转换单个文件，冷启动与 HMR 速度几乎与项目规模无关。

Vite 的工作流程：

第一，依赖预构建：node_modules 中的 CommonJS/多文件依赖用 esbuild 预打包为 ESM，缓存到 `node_modules/.vite`；

第二，源码按需转换：浏览器请求 `.vue`、`.tsx` 文件时，Vite 即时转译为浏览器可执行的 JS；

第三，HMR：模块图跟踪依赖，修改后只推送受影响的模块。

## 3. 快速上手

```bash
# 创建项目（react-ts 模板）
pnpm create vite my-app --template react-ts
cd my-app
pnpm install
pnpm dev      # 启动开发服务器（默认 5173）
pnpm build    # 生产构建
pnpm preview  # 预览构建产物
```

## 4. 配置文件

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'node:path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  server: {
    port: 5173,
    proxy: {
      // 开发环境代理 API 请求
      '/api': 'http://localhost:8080',
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        // 手动分包：稳定依赖合并为一个 chunk
        manualChunks: {
          react: ['react', 'react-dom'],
        },
      },
    },
  },
})
```

讲解：alias 让 `@/` 指向 src；proxy 解决开发期跨域；manualChunks 控制产物分包。配置是 TypeScript 文件，自带类型提示。

## 5. 环境变量与模式

```bash
# .env / .env.development / .env.production
VITE_API_BASE=/api
VITE_APP_TITLE=FANDEX
```

只有 `VITE_` 前缀的变量会暴露给客户端代码：

```ts
const api = import.meta.env.VITE_API_BASE
const isProd = import.meta.env.PROD
```

讲解：`import.meta.env` 是 Vite 注入的环境对象；敏感信息（密钥）绝不能放在 VITE_ 变量中。

## 6. 依赖优化与性能

### 6.1 预构建缓存

依赖变化或配置修改后，删除 `node_modules/.vite` 并重启即可。CI 中缓存该目录可加速安装后的首次启动。

### 6.2 代码分割

```ts
// 动态导入：路由级分包
const AdminPage = lazy(() => import('./pages/AdminPage'))
```

### 6.3 产物分析

```bash
pnpm add -D rollup-plugin-visualizer
```

在配置中启用后，构建会生成可视化报告，帮助定位超大 chunk。

## 7. Vite 与框架集成

官方插件：

`@vitejs/plugin-react`：React Fast Refresh；

`@vitejs/plugin-vue`：Vue SFC 支持；

`@vitejs/plugin-legacy`：旧浏览器兼容（转换 + polyfill）。

库模式（发布 npm 包）：

```ts
export default defineConfig({
  build: {
    lib: {
      entry: 'src/index.ts',
      formats: ['es', 'cjs'],
      fileName: 'index',
    },
  },
})
```

## 8. 测试与质量

Vitest 与 Vite 共享配置，零配置接入：

```ts
// 测试文件 sum.test.ts
import { describe, it, expect } from 'vitest'
import { sum } from './sum'

describe('sum', () => {
  it('计算两个数之和', () => {
    expect(sum(1, 2)).toBe(3)
  })
})
```

质量门禁：`pnpm typecheck`（tsc --noEmit）+ `pnpm lint`（ESLint）+ `pnpm test`（Vitest）+ `pnpm build`。

## 9. 常见陷阱

陷阱一：开发正常、构建失败。多为依赖使用了浏览器不支持的语法；配置 `build.target` 与插件。

陷阱二：路径别名在 TS 中报错。同步配置 tsconfig 的 paths。

陷阱三：环境变量泄漏。只使用 VITE_ 前缀，敏感信息走服务端。

陷阱四：HMR 失效。修改 vite.config 或新增插件后需重启。

陷阱五：忽略 base 配置。部署到子路径时资源 404，设置 `base: '/repo-name/'`。

## 10. 参考资源

Vite 官方文档：https://cn.vitejs.dev/

Vite 生态列表：https://github.com/vitejs/awesome-vite

Vitest：https://cn.vitest.dev/

Rollup 文档：https://rollupjs.org/

尚硅谷 Bilibili 空间：https://space.bilibili.com/302417610

## 11. 小结

Vite 用“原生 ESM + 按需编译”解决了开发体验问题，用 Rollup 保证生产质量。理解它的双引擎设计与配置项，是前端工程化的必修课。

## 参考文献

Vite 官方文档：https://cn.vitejs.dev/
Vite 插件市场：https://github.com/vitejs/awesome-vite
Vitest：https://cn.vitest.dev/
Rollup 文档：https://rollupjs.org/

## 延伸阅读

Astro 构建集成 Vite，见 055-astro 模块。
前端框架工程化，见 011-react/010-vue3 模块。
Monorepo 中的 Vite，见 057-pnpm-monorepo 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Vite 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 HMR 协议与模块图

模块图：文件到模块的映射；变更触发依赖链分析。
HMR API：import.meta.hot.accept/decline；框架插件自动接入。
边界：非模块化脚本与 CSS 的更新策略；失效时整页 reload。
调试：vite --debug 观察转换与更新日志。

### 13.2 构建优化实战

代码分割：动态 import 路由级分包；manualChunks 聚合稳定依赖。
资源优化：图片压缩、SVG 内联、字体子集。
产物分析：rollup-plugin-visualizer 识别大块。
缓存策略：文件哈希 + 长期缓存头。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Vite 构建工具概述 | 001-ViteOverview | 本文自身 |
