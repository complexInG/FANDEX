---
order: 5
title: Astro 内容集合与 Schema
module: astro
category: Astro
difficulty: intermediate
description: 'Astro 内容集合：content.config.ts、defineCollection、glob loader、zod schema 与 getCollection 查询'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/003-PagesRouting
  - astro/006-IslandsClientComponents
prerequisites:
  - astro/002-QuickStartProject
---
## 1. 内容集合是什么

内容集合（Content Collections）是把一批 Markdown/MDX/JSON 文档组织起来、统一做类型校验与查询的机制。它解决内容站的三大痛点：

第一，元数据失控：frontmatter 字段缺失、类型写错，只有到渲染时才暴露；

第二，查询零散：每个页面各自读文件、解析，代码重复且易错；

第三，无类型安全：编辑器和编译器不知道文档里有什么字段。

内容集合用 schema（基于 Zod）为文档定义"数据结构"，加载时校验，查询时返回带类型的对象。

## 2. 配置内容集合

### 2.1 创建配置文件

Astro 5+ 在项目根目录（或 `src/` 下）创建 `content.config.ts`：

```ts
// content.config.ts
import { defineCollection, z } from 'astro:content'
import { glob } from 'astro/loaders'

// 定义 blog 集合：使用 glob loader 加载 src/content/blog/ 下的 .md 文件
const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.coerce.date(),          // 字符串自动转 Date
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
})

export const collections = { blog }
```

讲解：`defineCollection` 接收两个关键配置：`loader` 定义内容从哪里来、如何加载；`schema` 用 Zod 声明 frontmatter 的字段结构与类型。`z.coerce.date()` 自动把字符串日期转为 `Date` 对象，`default()` 为缺失字段提供默认值。

### 2.2 loader 类型对比

| Loader | 适用场景 | 说明 |
| --- | --- | --- |
| `glob` | 本地 Markdown/MDX/JSON 文件 | 按 glob 模式匹配 `src/content/` 下的文件 |
| `file` | 单个 JSON/YAML 文件 | 从一个文件加载整组数据 |
| 自定义 loader | CMS、数据库、API | 实现 Loader 接口从任意数据源拉取 |
| `glob` + live | 外部托管内容（Astro 6+） | 请求时实时拉取，无需重新构建 |

讲解：FANDEX 文档站即用 `glob` 加载 `cnt-content/full` 目录下 2000+ 篇 Markdown。Astro 6 起 live content collections 支持从外部数据源（CMS 等）按请求实时加载，适合内容频繁更新的场景。

## 3. 文档的 frontmatter 规范

集合内每篇文档的 frontmatter 必须通过 schema 校验：

```md
---
title: 内容集合使用指南
description: 学习如何定义 schema 并查询内容
pubDate: 2026-08-01
tags:
  - Astro
  - 内容
draft: false
---

这里是文档正文。frontmatter 与正文之间用空行分隔。
```

讲解：frontmatter 以 `---` 包裹，字段必须符合 schema 声明：缺少必填字段、类型错误、出现未声明字段都会导致构建失败并给出精确报错信息，从源头保证元数据质量。

## 4. 查询内容：getCollection

### 4.1 基础查询与排序

```astro
---
// src/pages/blog/index.astro
import { getCollection } from 'astro:content'

const posts = (await getCollection('blog'))
  .filter((post) => !post.data.draft)
  .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf())
---

<ul>
  {posts.map((post) => (
    <li>
      <a href={`/blog/${post.id}/`}>{post.data.title}</a>
      <time datetime={post.data.pubDate.toISOString()}>
        {post.data.pubDate.toLocaleDateString('zh-CN')}
      </time>
    </li>
  ))}
</ul>
```

讲解：`getCollection('blog')` 返回条目数组，每条包含 `id`（由文件名生成，如 `guide/first-post`）、`data`（校验后的 frontmatter）与 `body`（文档正文）。示例展示了过滤草稿、按日期倒序排序、渲染列表的完整流程。

### 4.2 按条件筛选

```ts
import { getCollection } from 'astro:content'

// 按标签筛选
const astroPosts = await getCollection('blog', ({ data }) =>
  data.tags.includes('Astro')
)
```

讲解：`getCollection` 第二参数接收过滤函数，实现按任意字段筛选。返回类型自动收窄，`astroPosts` 的 `data.tags` 一定是 `string[]`，无需手动断言。

## 5. 渲染内容：render 与 <Content />

### 5.1 渲染单篇文章

```astro
---
// src/pages/blog/[slug].astro
import { getCollection, render } from 'astro:content'
import BaseLayout from '../../layouts/BaseLayout.astro'

export async function getStaticPaths() {
  const posts = await getCollection('blog')
  return posts.map((post) => ({ params: { slug: post.id }, props: { post } }))
}

const { post } = Astro.props
const { Content } = await render(post)
---

<BaseLayout title={post.data.title}>
  <article>
    <h1>{post.data.title}</h1>
    <Content />
  </article>
</BaseLayout>
```

讲解：`render(post)` 把 Markdown 正文编译为渲染组件 `<Content />`，插入到模板即可输出完整文章。与 003 的动态路由配合，实现"一篇文档一个页面"的完整闭环。

### 5.2 render 返回的其他内容

`render` 还返回 `headings`（标题目录树，可用于生成文章目录）与 `remarkPluginFrontmatter`（插件产生的附加数据），是文档站目录组件的标准数据来源。

## 6. 内容集合与类型安全

`schema` 的类型会自动推断到查询结果：定义集合时写一次 Zod schema，全项目所有 `getCollection` 的返回值都会带上精确类型。修改 schema 后，`astro check` 能立刻发现所有字段用法不一致的代码位置。

```ts
// schema 变更后的类型即时生效
post.data.pubDate // 类型为 Date，可调用 toISOString()
post.data.tags    // 类型为 string[]
```

## 7. 实践建议

第一，schema 是契约：字段只增不删，新增字段要带 `default`，避免存量文档构建失败；

第二，索引字段齐全：`order`、`title`、`description` 等导航所需字段必须在 schema 中声明；

第三，正文与元数据分离：正文负责内容，frontmatter 负责结构化信息，职责清晰。

## 8. 参考资源

内容集合指南：https://docs.astro.build/zh-cn/guides/content-collections/

Content Layer API：https://docs.astro.build/zh-cn/reference/content-layer/

Astro Content 参考：https://docs.astro.build/zh-cn/reference/modules/astro-content/
