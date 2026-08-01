---
order: 8
title: Astro 构建与部署
module: astro
category: Astro
difficulty: intermediate
description: 'Astro 构建部署：SSG 静态生成、SSR 适配器、路由缓存与 Netlify/Vercel/Cloudflare 部署'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/005-ContentCollections
  - astro/009-Astro7Features
prerequisites:
  - astro/002-QuickStartProject
---
## 1. 构建流程概述

Astro 的构建分两步：先打包站点页面、内容与客户端组件为 JavaScript；再像运行小型服务器一样执行打包结果，为每个预渲染页面生成 HTML 输出到 `dist/`。

```bash
npm run build
```

讲解：构建产物在 `dist/` 目录，包含完整 HTML、CSS、经过优化的图片与按需加载的岛屿脚本。`npm run preview` 可在本地模拟生产环境预览产物。Astro 7 中构建管线全面加速（Rust 编译器 + Vite 8 + Rolldown），大型站点构建提速 15%-61%。

## 2. 输出模式：SSG 与 SSR

### 2.1 三种输出模式

| 模式 | 配置 | 渲染时机 | 适用场景 |
| --- | --- | --- | --- |
| 静态 SSG | `output: 'static'`（默认） | 构建期 | 博客、文档站、营销页 |
| 服务端 SSR | `output: 'server'` | 每次请求 | 个性化、登录态、动态数据 |
| 混合 Hybrid | `output: 'hybrid'` | 按页面 `prerender` 决定 | 大部分静态 + 少量动态 |

讲解：静态模式零服务器成本、可直接部署到任意静态托管；SSR 需要适配器提供的运行环境（Node 函数、边缘 Worker 等）；Hybrid 允许同一站点内部分页面静态、部分页面服务端渲染。

### 2.2 静态模式

```js
// astro.config.mjs
import { defineConfig } from 'astro/config'

export default defineConfig({
  output: 'static',
  site: 'https://docs.example.com',
  build: { format: 'directory' },  // 页面输出为 /about/index.html
})
```

讲解：静态站点无需任何运行环境，产物是一组纯静态文件，兼容性最好、响应最快。`site` 用于生成规范链接、sitemap 与 Open Graph 绝对地址。

## 3. SSR 与适配器

### 3.1 适配器的作用

SSR 时页面在请求时渲染，需要适配器把 Astro 接入目标平台的运行环境（Node 服务器、边缘函数、Serverless 函数）：

```bash
npx astro add node      # @astrojs/node
npx astro add netlify   # @astrojs/netlify
npx astro add vercel    # @astrojs/vercel
npx astro add cloudflare # @astrojs/cloudflare
```

讲解：`astro add` 会安装适配器并写入 `astro.config.mjs`。官方适配器覆盖 Node.js、Netlify、Vercel、Cloudflare、Deno、Bun 等主流运行环境。

### 3.2 配置示例

```js
// astro.config.mjs（以 Cloudflare 为例）
import { defineConfig } from 'astro/config'
import cloudflare from '@astrojs/cloudflare'

export default defineConfig({
  output: 'server',
  adapter: cloudflare(),
})
```

讲解：Astro 6 起 Cloudflare 适配器在开发、预渲染与生产全程运行 `workerd` 运行时，本地开发即可直接使用 KV、D1、R2 等绑定，行为与生产一致。

### 3.3 动态路由与 SSR

SSR 模式下动态路由不需要 `getStaticPaths`，`Astro.params` 在请求时按 URL 匹配：

```astro
---
// src/pages/product/[id].astro（SSR）
const { id } = Astro.params
const product = await fetchProduct(id)  // 请求时获取数据
---

<h1>{product.name}</h1>
```

讲解：SSR 模式下页面代码在每次请求时执行，可访问数据库、API、`Astro.cookies` 等请求级能力。注意区分：静态模式的动态路由在构建期展开，SSR 的动态路由在请求期匹配。

## 4. 路由缓存 Route Caching

对"内容偶尔变化但不必每次重新渲染"的页面，路由缓存可以显著降低成本。Astro 7 中路由缓存已稳定：

```js
// astro.config.mjs（SSR 项目）
export default defineConfig({
  output: 'server',
  routeRules: [
    {
      pattern: '/blog/**',
      maxAge: 60 * 60,      // 缓存 1 小时
      swr: 60 * 60 * 24,    // 过期后仍可服务旧内容（SWR 兜底）
    },
  ],
})
```

讲解：`routeRules` 按 URL 模式配置缓存：`maxAge` 定义缓存时长，`swr` 定义过期后继续提供旧内容的时间窗口，适合博客列表、文档页这类高读低写页面。静态站本身已有 CDN 缓存优势，此机制主要服务 SSR 站点。

### 4.1 CDN 缓存提供方（Astro 7 实验特性）

```js
import { defineConfig } from 'astro/config'
import cloudflare from '@astrojs/cloudflare'

export default defineConfig({
  output: 'server',
  adapter: cloudflare({ cdnCache: { provider: 'cloudflare' } }),
})
```

讲解：Astro 7 新增实验性 CDN 缓存提供方（Netlify、Vercel、Cloudflare），把 `routeRules` 的缓存配置下发到平台 CDN，响应缓存在边缘节点，全球就近返回，进一步降低源站压力。

## 5. 部署到主流平台

### 5.1 Netlify / Vercel（推荐流程）

在平台控制台导入 Git 仓库，配置构建命令与输出目录即可，平台自动识别 Astro：

| 平台 | 构建命令 | 输出目录 |
| --- | --- | --- |
| Netlify | `npm run build` | `dist` |
| Vercel | `npm run build` | `dist` |

讲解：Netlify 与 Vercel 对 Astro 提供第一方支持（Netlify 在 Astro 7 发布当日即完成适配），静态与 SSR 均开箱即用，支持自动预览部署与回滚。SSR 站点需在平台侧启用函数运行时。

### 5.2 Cloudflare Pages / Workers

```bash
npm run build
# 上传 dist/ 或通过适配器部署 Workers
wrangler pages deploy dist
```

讲解：Cloudflare Pages 适合静态站；使用 `@astrojs/cloudflare` 适配器时可直接部署为 Workers（`wrangler deploy`），在边缘运行 SSR。Astro 6+ 与 Cloudflare 深度合作，绑定（KV/D1/R2）在本地开发即完全可用。

### 5.3 通用静态托管

静态站点产物可以部署到任意平台：GitHub Pages、阿里云 OSS、S3、Nginx 等。子路径部署时配置 `base`：

```js
// astro.config.mjs
export default defineConfig({
  base: '/my-project/',   // 部署在域名子路径时必配
})
```

## 6. CI/CD 与质量门禁

```yaml
# .github/workflows/deploy.yml 示意
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22 }
      - run: npm ci
      - run: npm run build
      - run: npx astro check      # 类型检查作为构建门禁
```

讲解：CI 中执行安装、构建、类型检查三步，任何一步失败即阻断部署。FANDEX 的 CI 还包含链接检查与构建统计，保证 2000+ 篇文档构建稳定、无死链。

## 7. 部署检查清单

第一，`site` 与 `base` 配置正确，sitemap 与规范链接生成无误；

第二，SSR 站点确认适配器与平台运行时匹配；

第三，动态页面配置 `routeRules` 缓存策略，观察命中率；

第四，构建产物体积正常，无意外大 JS 包。

## 8. 参考资源

Astro 构建与预览：https://docs.astro.build/zh-cn/guides/builds/

部署指南：https://docs.astro.build/zh-cn/guides/deploy/

适配器参考：https://docs.astro.build/zh-cn/reference/adapter-reference/

路由缓存配置：https://docs.astro.build/zh-cn/reference/configuration-reference/
