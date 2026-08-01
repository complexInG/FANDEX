---
order: 3
title: Astro 页面与路由
module: astro
category: Astro
difficulty: beginner
description: 'Astro 文件路由：静态路由、动态路由 [slug]、getStaticPaths 与页面布局'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/004-ComponentsProps
  - astro/005-ContentCollections
prerequisites:
  - astro/002-QuickStartProject
---
## 1. 路由是什么

Astro 采用"文件路由"（File-based Routing）：`src/pages/` 目录下每个文件（`.astro`、`.md`、`.mdx`）对应站点的一个 URL。文件的路径即页面的路由，无需手动注册路由表，新增文件就是新增页面。

这种设计有两大好处：其一，路由与文件一一对应，可读性高、好维护；其二，构建期即可枚举全部页面并输出静态 HTML，天然适配内容站。

## 2. 静态路由

### 2.1 路由映射规则

| 文件路径（src/pages/ 下） | 生成的 URL |
| --- | --- |
| `index.astro` | `/` |
| `about.astro` | `/about` |
| `blog/index.astro` | `/blog` |
| `blog/post.md` | `/blog/post` |
| `docs/guide/getting-started.md` | `/docs/guide/getting-started` |

讲解：`index.astro` 是目录的入口页面；其余文件名直接对应路径段。URL 末尾是否带 `/` 取决于部署配置，通常统一为无尾斜杠，静态托管平台一般都能正确处理。

### 2.2 页面中引用链接

```astro
---
// src/pages/index.astro
---

<nav>
  <a href="/">首页</a>
  <a href="/about">关于</a>
  <a href="/blog">博客</a>
</nav>
```

讲解：页面间跳转使用普通 `<a>` 链接即可。链接路径以 `/` 开头表示站点根路径。若部署在子路径（如 GitHub Pages 的 `/repo/`），需要在 `astro.config.mjs` 中配置 `base: '/repo/'`，并推荐使用 `Astro.url` 或内置 `<Link>` 生成正确路径。

## 3. 动态路由：[slug]

内容站常有大量结构相同的页面（如每篇博客文章一个页面），不可能为每个内容手写文件。此时用方括号语法声明动态参数：

```astro
---
// src/pages/blog/[slug].astro
export async function getStaticPaths() {
  const posts = [
    { slug: 'hello', title: '你好，世界' },
    { slug: 'astro-guide', title: 'Astro 入门' },
  ]
  return posts.map((post) => ({
    params: { slug: post.slug },
    props: { title: post.title },
  }))
}

const { slug } = Astro.params
const { title } = Astro.props
---

<h1>{title}</h1>
<p>当前文章：{slug}</p>
```

讲解：`[slug]` 中括号代表一个动态路径段。`getStaticPaths` 返回数组，每一项包含 `params`（路由参数）与 `props`（传入页面的数据）。本例生成 `/blog/hello` 与 `/blog/astro-guide` 两个静态页面。`Astro.params` 读取当前路由参数，`Astro.props` 读取 `props` 数据。

### 3.1 getStaticPaths 的返回值

`getStaticPaths` 返回项的字段说明：

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `params` | 是 | 路由参数对象，键必须与文件名中的 `[...]` 占位符一一对应 |
| `props` | 否 | 传给页面的任意数据，可在模板中通过 `Astro.props` 访问 |

讲解：静态模式下，`getStaticPaths` 在构建期执行，动态路由必须通过它声明生成哪些页面；漏掉的参数组合不会生成对应页面。这与 SSR 模式（按请求实时匹配）形成对比，静态模式适合内容规模可枚举的站点。

## 4. 多参数与 Rest 参数

### 4.1 多级动态参数

```text
src/pages/docs/[lang]/[chapter].astro  →  /docs/zh/intro
```

讲解：`[lang]` 与 `[chapter]` 两个占位符对应 URL 的两个路径段，`getStaticPaths` 中 `params` 需同时提供 `lang` 与 `chapter` 两个键。

### 4.2 Rest 参数 [...path]

```astro
---
// src/pages/docs/[...path].astro
export function getStaticPaths() {
  return [
    { params: { path: 'getting-started' } },
    { params: { path: 'guides/deploy' } },  // 匹配多级路径
    { params: { path: undefined } },        // 匹配 /docs
  ]
}
const { path } = Astro.params
---

<p>文档路径：{path ?? '首页'}</p>
```

讲解：`[...path]` 匹配剩余的所有路径段，返回的 `path` 是数组或 `undefined`（匹配根路径时）。这适合为文档、分类等不确定层级的内容统一渲染页面。

## 5. 页面布局 Layout

### 5.1 布局组件与插槽

页面级的公共结构（HTML 骨架、导航、页脚）应抽成布局组件：

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
    <header>站点导航</header>
    <main>
      <slot />  <!-- 默认插槽：页面内容 -->
    </main>
    <footer>页脚信息</footer>
  </body>
</html>
```

讲解：`<slot />` 是插槽，页面内容会注入到默认插槽位置；`<slot name="head" />` 是具名插槽，页面可以通过 `slot="head"` 属性向布局的 head 区域追加内容。

### 5.2 页面使用布局

```astro
---
// src/pages/about.astro
import BaseLayout from '../layouts/BaseLayout.astro'
---

<BaseLayout title="关于我们">
  <h1>关于我们</h1>
  <p>这是一个使用布局组件的页面。</p>
</BaseLayout>
```

讲解：页面只需负责自身内容，通过 Props 向布局传 `title`，通过插槽提供正文。这样全站保持一致的结构与样式，是内容站组织页面的标准做法。

## 6. 特殊页面与重定向

### 6.1 404 页面

```astro
---
// src/pages/404.astro
---

<h1>页面不存在</h1>
<p>你访问的页面可能已被移动或删除。</p>
```

讲解：`404.astro` 自动生成 404 错误页，静态托管平台与 SSR 服务器都会在找不到路由时返回它。

### 6.2 页面级重定向

```astro
---
// src/pages/old-page.astro
export const prerender = true
return new Response(null, {
  status: 301,
  headers: { Location: '/new-page' },
})
---
```

讲解：在页面 frontmatter 中直接返回 `Response` 即可实现重定向，常用于旧链接迁移。更简单的场景也可在 `astro.config.mjs` 的 `redirects` 配置中声明静态重定向映射。

## 7. 路由与页面数据的配合

动态路由 + 内容集合（见 005-ContentCollections）是内容站的黄金组合：先用 `getCollection` 查询全部内容，再用 `getStaticPaths` 为每篇内容生成页面。典型流程：

```astro
---
// src/pages/blog/[slug].astro
import { getCollection } from 'astro:content'

export async function getStaticPaths() {
  const posts = await getCollection('blog')
  return posts.map((post) => ({
    params: { slug: post.id },
    props: { post },
  }))
}

const { post } = Astro.props
---

<h1>{post.data.title}</h1>
```

讲解：`getCollection('blog')` 读取内容集合的全部条目，`post.id` 作为路由参数。页面内容即集合条目，schema 校验保证数据完整，构建期自动生成所有文章页面。

## 8. 参考资源

Astro 路由指南：https://docs.astro.build/zh-cn/guides/routing/

Astro 页面与布局：https://docs.astro.build/zh-cn/basics/astro-pages/

Astro 布局组件：https://docs.astro.build/zh-cn/basics/layouts/
