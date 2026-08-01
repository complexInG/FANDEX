---
order: 9
title: Astro 7 新特性速览
module: astro
category: Astro
difficulty: intermediate
description: 'Astro 7 新特性：Rust 编译器、Sätteri Markdown 管线、Vite 8、Advanced Routing、路由缓存、CSP 与 AI 增强'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/005-ContentCollections
  - astro/008-BuildDeploy
prerequisites:
  - astro/003-PagesRouting
---
## 1. Astro 7 概述

Astro 7 于 2026 年 6 月 22 日发布，官方定位为"速度版本"（speed release）：不改变组件语法、岛屿架构与路由模型，而是把构建链路中最耗时的部分全部换成 Rust 原生实现。官方基准测试显示，真实站点构建提速 15%-61%，Markdown 密集的文档站收益最大。

升级方式（官方推荐）：

```bash
npx @astrojs/upgrade
```

讲解：`@astrojs/upgrade` 会同步升级 Astro 本体与全部官方集成、适配器，并处理破坏性变更提示。新项目直接 `npm create astro@latest` 即可获得 Astro 7。

## 2. Rust 编译器

`.astro` 组件的编译器从 Go 实现完全重写为 Rust：解析层基于 Oxc，CSS 作用域处理基于 Lightning CSS，按平台分发原生二进制（WASM 兜底）。

```astro
---
// 语法不变，编译路径已原生化
const items = ['Rust', 'Fast', 'Astro']
---

<ul>
  {items.map((item) => <li>{item}</li>)}
</ul>
```

讲解：开发者侧无感知，组件语法与行为保持一致，但编译更快、内存占用更低。同时编译器行为更严格：未闭合标签直接报错（不再自动修正无效 HTML），空白处理遵循 JSX 规则，两个行内元素间的换行不再产生可见空格，需要时显式书写。

## 3. Markdown/MDX Rust 管线：Sätteri

Astro 7 默认的 Markdown/MDX 处理器替换为 Sätteri——基于 Rust 的原生管线（CommonMark 解析用 pulldown-cmark，MDX 表达式解析用 Oxc）：

| 能力 | Sätteri 内置支持 |
| --- | --- |
| GFM（表格、任务列表等） | 原生 |
| 标题 ID、Frontmatter、Wiki 链接 | 原生 |
| 数学公式、指令（directives） | 原生 |
| remark/rehype 插件 | 需安装 `@astrojs/markdown-remark` 迁移 |

讲解：Sätteri 把常用能力内建到原生实现，插件按声明的节点类型路由，不再整树遍历，官方文档站与 Cloudflare 文档站切换后构建时间各减少 1 分钟以上。依赖 remark/rehype 插件的项目需单独安装 `@astrojs/markdown-remark` 以继续使用 unified 生态。

```js
// astro.config.mjs：仍可配置 Markdown 行为
export default defineConfig({
  markdown: {
    shikiConfig: { theme: 'github-dark' },  // 代码高亮主题
  },
})
```

## 4. Vite 8 与 Rolldown

Astro 7 升级到 Vite 8——Vite 史上最大版本之一：用 Rust 编写的 Rolldown 打包器统一替代 esbuild 与 Rollup，基准测试中比 Rollup 快 10-30 倍，同时兼容 Rollup 与 Vite 插件 API。

讲解：对大多数项目，升级无需改配置：`esbuild` 与 `rollupOptions` 配置会被 Vite 8 兼容层自动转换，既有 Vite 插件继续工作。打包阶段是 Astro 构建的第一步，其加速直接作用于全站。依赖 Vite 内部 API 的自定义集成需对照 Vite 8 迁移指南验证。

## 5. Advanced Routing：src/fetch.ts

高级路由在 Astro 7 中默认启用（此前为实验特性），新增 `src/fetch.ts` 入口，完全掌控请求管线：

```ts
// src/fetch.ts
export default {
  async fetch(request, ctx) {
    // 请求入口：可先做鉴权、日志等中间件处理
    ctx.logger.info(`请求进入：${request.url}`)

    // 中间件组合：每个 Astro 能力都是可组合的 fetch 处理
    const response = await ctx.render(request)
    response.headers.set('x-powered-by', 'Astro')
    return response
  },
}
```

讲解：`src/fetch.ts` 采用标准 fetch handler 模式（Request 进、Response 出，与 Cloudflare Workers、WinterCG 运行时一致），并兼容 Hono 中间件，可以直接复用 Hono 生态。它把鉴权、日志、响应头改写等横切关注点集中在一个文件。注意 `src/fetch.ts` 是保留文件名，已有同名文件需改名。

## 6. 路由缓存与 CDN 缓存提供方

### 6.1 路由缓存稳定

Astro 6 实验性的路由缓存在 Astro 7 转正，通过 `routeRules` 按 URL 配置：

```js
export default defineConfig({
  output: 'server',
  routeRules: [
    {
      pattern: '/docs/**',
      maxAge: 3600,      // 缓存 1 小时
      swr: 86400,        // 过期后 24 小时内仍提供旧内容
    },
  ],
})
```

讲解：`maxAge` 定义缓存有效期，`swr` 定义过期后继续服务旧内容的窗口（Stale-While-Revalidate）。高读低写的页面（文档、列表）收益最大。"最快的构建是不发生的构建"——缓存命中时根本不需要渲染。

### 6.2 实验性 CDN 缓存提供方

```js
import netlify from '@astrojs/netlify'

export default defineConfig({
  output: 'server',
  adapter: netlify({ cdnCache: { provider: 'netlify' } }),
})
```

讲解：Astro 7 为 Netlify、Vercel、Cloudflare 提供实验性 CDN 缓存提供方：把 `routeRules` 的缓存配置下发到平台边缘，全球节点就近返回缓存响应，进一步降低源站压力。

## 7. CSP 安全策略

CSP（Content Security Policy）从 Astro 6 起内置 API，Astro 7 继续完善，用于限制浏览器可加载的资源来源，防御 XSS：

```js
// astro.config.mjs
export default defineConfig({
  security: {
    contentSecurityPolicy: {
      'default-src': ["'self'"],
      'script-src': ["'self'", "'wasm-unsafe-eval'"],
      'style-src': ["'self'", "'unsafe-inline'"],
      'img-src': ["'self'", 'data:', 'https://assets.example.com'],
      'font-src': ["'self'", 'data:'],
    },
  },
})
```

讲解：构建时 Astro 依据配置生成 CSP 响应头（SSR）或 `<meta>` 标签（静态），并自动放行 Astro 自身需要的规则。配置需覆盖三类资源：脚本、样式、图片字体。收紧 `script-src` 是文档站最常见的 XSS 防护手段。

## 8. AI 增强：JSON 日志与后台开发服务器

Astro 7 针对 AI 编程工具优化了开发体验：

第一，自动识别编码代理：检测到 AI 环境时自动启用后台模式与 JSON 日志；

第二，后台开发服务器：`astro dev` 不再阻塞终端，等待服务可用后返回 URL 与进程 ID 并转入后台；

第三，进程管理命令：`astro dev status`（查看状态）、`astro dev logs`（查看日志）、`astro dev stop`（停止服务）；

第四，健康检查端点：每个开发服务器暴露 `/_astro/status` 供探测；

第五，结构化 JSON 日志：`context.logger` 在 API 路由与中间件中始终可用，内置 `json`、`node`、`console` 处理器，输出机器可读的日志。

```bash
astro dev status
# 输出示例（JSON）：
# {"status":"running","pid":1234,"url":"http://localhost:4321"}
```

讲解：AI 编程工具此前执行 `astro dev` 常遇到"命令不退出、重复启动、无法判断就绪"等问题，Astro 7 通过后台模式 + JSON 日志提供标准化的开发协议，也让开发者直接受益于更干净的终端输出。

## 9. 升级注意事项

第一，模板语法更严格：未闭合标签会构建报错，存量项目的非规范 HTML 需修正；

第二，Markdown 插件检查：使用 remark/rehype/recma 的项目需迁移或安装 `@astrojs/markdown-remark`；

第三，Vite 深层集成：依赖 Vite 内部 API 的集成需按 Vite 8 迁移指南测试；

第四，Astro DB 已弃用：`astro db` 相关 CLI 命令移除，改用独立数据库客户端。

## 10. 参考资源

Astro 7 发布公告：https://astro.build/blog/astro-7/

Astro 7 升级指南：https://docs.astro.build/en/guides/upgrade-to/v7/

Vite 8 发布说明：https://vite.dev/blog/announcing-vite8

Rolldown 项目：https://rolldown.rs/

Astro 官方文档（中文）：https://docs.astro.build/zh-cn/
