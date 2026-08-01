---
order: 1
title: Astro 框架概述与文档站实践
module: astro
category: Astro
difficulty: beginner
description: 'Astro 静态站点框架概述：岛屿架构、内容集合、路由、部署与文档站实践'
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/HTML5语义化
  - vite/Vite构建工具
  - markdown/Markdown语法指南
  - tailwind/TailwindCSS概述
prerequisites:
  - html5/HTML5语义化
  - markdown/Markdown语法指南
---
## 0. 零基础入门（从零开始）

### 0.1 零基础起点

本模块讲解 Astro 静态站点框架。零基础可学，但建议先完成 006-html5 与 007-css 两个模块，并且已经会打开命令行、安装过 Node.js 18+。
Astro 用来做什么：把 Markdown/HTML 文档变成网站。FANDEX 这个文档站本身就是用 Astro 构建的——学完本模块你就能理解整个站点的运作方式。

### 0.2 第一个 Astro 页面

```bash
# 创建项目（官方脚手架）
pnpm create astro@latest my-site -- --template minimal
# 进入项目并安装依赖
cd my-site && pnpm install
# 启动开发服务器，浏览器打开 http://localhost:4321
pnpm dev
```

create astro 命令生成一个最小项目骨架；--template minimal 表示只保留最基础的文件，方便从零理解。
项目里最重要的目录是 src/pages：里面的 .astro 文件就是网页。每个文件对应一个 URL。
pnpm dev 启动开发服务器：修改文件保存后浏览器自动刷新，这就是“开发预览”。
打开 src/pages/index.astro 你会看到类似 HTML 的代码——Astro 的页面文件本质就是 HTML 加一些扩展语法，学过 HTML 就能看懂。
完成这四步，你已经跑起了一个真实的网站；后续学习路由、布局、Markdown 内容集合，就能搭出完整的文档站。

### 0.3 学习路径

完成上面的第一步后，按以下顺序继续学习：

- 002-页面与路由：src/pages 的文件如何映射为 URL。
- 003-组件与布局：复用页头页脚等公共结构。
- 004-内容集合：用 Markdown 管理文章与文档。


## 1. Astro 是什么

Astro 是一个面向内容驱动网站（博客、文档站、营销页）的 Web 框架，2021 年发布，当前主流版本为 Astro 5-7。它的核心思想是：默认输出零 JavaScript 的静态 HTML，只有显式标记的交互组件才在浏览器加载脚本。这一模式被称为“岛屿架构”（Islands Architecture）。

Astro 底层由 Vite 驱动，支持 Markdown/MDX、内容集合（Content Collections）、视图过渡（View Transitions）、SSR 与多种部署适配器。FANDEX 文档站即采用 Astro 构建。

## 2. 设计动机：内容站的性能困境

传统 SPA（单页应用）把所有逻辑打包成一个大 JS bundle，浏览器必须先下载并执行 JS 才能渲染内容。对博客与文档站而言，大部分页面是静态文本，JS 只用于少量交互（目录高亮、搜索、主题切换）——为 10% 的交互付出 100% 的 JS 成本显然不划算。

Astro 的解法：

第一，构建期渲染：页面在构建时输出完整 HTML，首屏无需 JS；

第二，按需水合：交互组件用 `client:` 指令显式声明加载时机；

第三，框架无关：同一页面可以混合使用 React、Vue、Svelte 组件（岛屿）。

## 3. 项目结构

```text
my-astro-site/
  src/
    pages/          # 路由：每个 .astro/.md 文件对应一个页面
      index.astro
      about.md
    components/     # 组件（.astro、.jsx、.vue 等）
    layouts/        # 布局组件
    content/        # 内容集合（docs/blog）
    styles/
  public/           # 静态资源
  astro.config.mjs  # Astro 配置
  package.json
```

讲解：`src/pages` 是文件路由：`pages/about.md` 生成 `/about` 页面；`pages/blog/[slug].astro` 是动态路由。

## 4. 组件与页面

### 4.1 .astro 组件结构

```astro
---
// frontmatter：组件逻辑（在服务端/构建期执行）
import Layout from '../layouts/BaseLayout.astro'
const title = "欢迎"
---

<!-- 模板：HTML + 组件 -->
<Layout pageTitle={title}>
  <h1>{title}</h1>
  <p>这是 Astro 组件。</p>
</Layout>
```

讲解：`---` 之间的代码在构建期运行（可访问文件系统、环境变量），不会发送到浏览器；模板部分输出 HTML。

### 4.2 岛屿：交互组件

```astro
---
import SearchBox from '../components/SearchBox.tsx'
---

<!-- client:load：页面加载时水合 React 组件 -->
<SearchBox client:load />

<!-- client:visible：组件进入视口才加载 -->
<ThemeToggle client:visible />
```

讲解：`client:` 指令决定 JS 注入时机：`load`（立即）、`idle`（空闲）、`visible`（可见）、`only`（仅客户端）。没有指令的组件只输出服务端渲染的 HTML。

## 5. 内容集合

内容集合用 schema 校验 frontmatter，让 Markdown 文档获得类型安全：

```ts
// src/content.config.ts
import { defineCollection, z } from 'astro:content'

const docs = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    order: z.number().default(0),
    updated: z.coerce.date().optional(),
  }),
})

export const collections = { docs }
```

查询与渲染：

```astro
---
import { getCollection } from 'astro:content'

// 按 order 排序获取全部文档
const docs = (await getCollection('docs')).sort(
  (a, b) => a.data.order - b.data.order
)
---

<ul>
  {docs.map((doc) => (
    <li><a href={`/docs/${doc.id}/`}>{doc.data.title}</a></li>
  ))}
</ul>
```

讲解：`getCollection` 返回带类型的数据；`doc.id` 由文件名生成。schema 校验失败时构建直接报错，从源头保证元数据质量。

## 6. 布局、样式与集成

### 6.1 布局组件

```astro
---
// src/layouts/BaseLayout.astro
interface Props {
  title: string
}
const { title } = Astro.props
---

<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <slot name="head" />
  </head>
  <body>
    <slot /> <!-- 页面内容插槽 -->
  </body>
</html>
```

### 6.2 样式

Astro 支持全局 CSS、`<style>` 作用域样式（自动 scoped）、CSS Modules、Tailwind 集成。现代项目推荐 Tailwind 4 + 设计令牌。

### 6.3 常用集成

`@astrojs/react`（React 岛屿）、`@astrojs/mdx`（MDX 文档）、`@astrojs/sitemap`（站点地图）、`@astrojs/rss`（RSS 订阅）、Shiki（代码高亮）、KaTeX（数学公式）。

## 7. 路由、SSR 与部署

### 7.1 静态与 SSR

默认 `output: 'static'` 构建期生成全部页面；`output: 'server'` 启用 SSR，配合适配器（Node、Netlify、Cloudflare）在服务端渲染动态页面。文档站通常用静态输出。

### 7.2 部署

`astro build` 输出 `dist/` 目录，可部署到任意静态托管（GitHub Pages、Netlify、Vercel、OSS）。CI 中执行 `pnpm build` 并上传产物即可。

## 8. 性能与 SEO

性能基线：

第一，零 JS 默认：页面 HTML 直接可读，LCP 极快；

第二，图片优化：`astro:assets` 的 `<Image />` 组件自动压缩、响应式、防 CLS；

第三，字体与 CSS 优化：构建期内联关键资源。

SEO 内置：语义化 HTML、sitemap、RSS、规范链接、Open Graph 标签。

## 9. 文档站实践（FANDEX 模式）

FANDEX 文档站的关键设计：

内容源：`cnt-content/full` 目录作为内容集合，2000+ 篇 Markdown 文档；

元数据：frontmatter 统一（title、order、module、difficulty、related、prerequisites）；

导航：按模块与 order 自动生成目录与面包屑；

检索：搜索组件作为岛屿按需加载；

构建：`node scripts/build-stats.mjs && astro build`，CI 门禁包含构建与链接检查。

```mermaid
flowchart LR
    A["Markdown 文档"] --> B["内容集合 schema 校验"]
    B --> C["Astro 构建"]
    C --> D["静态 HTML 输出"]
    D --> E["交互岛屿（搜索/主题）"]
    E --> F["部署到静态托管"]
```

## 10. 常见陷阱

陷阱一：忘记 `client:` 指令，组件完全没有交互。交互组件必须显式水合。

陷阱二：在 frontmatter 中访问浏览器 API。frontmatter 在构建期执行，用 `client:only` 或条件判断。

陷阱三：内容集合 schema 过松，元数据错误到运行时才暴露。

陷阱四：全站 SSR 导致失去静态优势。按页面选择输出模式。

陷阱五：忽略构建报告。用 `astro build` 的产物分析监控每页 JS 体积。

## 11. 参考资源

Astro 官方文档：https://docs.astro.build/zh-cn/

Astro 主题市场：https://astro.build/themes/

Astro 集成目录：https://astro.build/integrations/

Astro 官方博客：https://astro.build/blog/

尚硅谷 Bilibili 空间：https://space.bilibili.com/302417610

## 12. 小结

Astro 重新定义了内容站的性能基线：默认零 JS、按需交互、内容优先。对文档站与内容密集型站点，Astro 是目前最合适的选择之一；理解岛屿架构与内容集合，就能发挥它的全部优势。

## 参考文献



Astro 官方文档：https://docs.astro.build/zh-cn/
Astro 主题市场：https://astro.build/themes/
Astro 集成：https://astro.build/integrations/
Astro 博客：https://astro.build/blog/

## 延伸阅读



Vite 构建机制，见 056-vite 模块。
Markdown/MDX 写作，见 002-markdown 模块。
Tailwind 样式，见 058-tailwind 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供前端工程化课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 内容集合与类型安全

定义 schema（zod）：title、description、日期、标签；集合加载时校验。
getCollection('docs') 返回类型化条目；slug 由文件名或 frontmatter 决定。
Content Layer（Astro 5+）：从远程或本地数据源加载，缓存策略可配置。
实践：文档站把全部课程文档注册为集合，目录与搜索基于集合生成。

### 13.2 岛屿架构原理

静态页面输出 HTML 与 CSS；client:load 组件单独打包为岛屿脚本。
指令：client:load（加载即水合）、client:idle（空闲）、client:visible（可见）、client:only（仅客户端）。
水合成本：每个岛屿独立 JS 块，页面级状态传递用 store（nanostores）。
性能分析：astro build 报告每页 JS 大小，按报告调整指令。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Astro 框架概述与文档站实践 | 001-AstroOverview | 本文自身 |
