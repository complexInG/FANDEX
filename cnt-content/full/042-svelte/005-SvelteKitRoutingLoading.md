---
order: 50
title: SvelteKit 路由与数据加载
module: 'svelte'
category: 前端技术
difficulty: intermediate
description: +page/+layout/+server 与 load 函数：SvelteKit 的数据骨架。
author: fanquanpp
updated: '2026-08-28'
related:
  - 'svelte/003-ReactivityRunes'
  - 'typescript/003-TypeScriptOverviewEnvSetup'
prerequisites:
  - 'svelte/002-SvelteKitQuickStart'
---

## 0. 路由与数据加载全景（先读这里）

> 学习目标：读完本文，你能说清每个"加号文件"的职责；能为页面选对通用 load 或
> server load；会使用 params、url、fetch 三个 load 入参；理解流式 Promise 对首屏的
> 价值；能组织嵌套布局与布局组（group）；并用 hooks.server.ts 的 handle/locals
> 搭好服务端中间层，最后借助自动生成的 $types 类型安全地把数据接到组件里。

SvelteKit 把"页面在哪、数据谁来取、接口怎么暴露、错误怎么兜底、请求先经过谁"全部
编码进一组以加号开头的约定文件。入门篇（002）已经用过 `+page.svelte` 与
`+page.server.ts`，本文把它们补成完整的数据骨架。

## 1. 加号文件职责速查表

```text
src/routes/
  +layout.svelte            # 根布局：全站共享 UI（导航、页脚）
  +layout.server.ts         # 根布局级 server load：全站公共数据
  +error.svelte             # 兜底错误页：渲染 error 状态
  +page.svelte              # / 首页 UI
  +page.server.ts           # / 首页 server load
  blog/
    +server.ts              # /blog API 端点：导出 GET/POST 即接口
    [id]/
      +page.ts              # /blog/123 通用 load
      +page.svelte          # /blog/123 页面 UI
```

| 文件 | 运行环境 | 核心职责 | 缺失时的表现 |
| --- | --- | --- | --- |
| `+page.svelte` | 服务端 + 浏览器 | 页面 UI，接收 data/params/form | 路由没有界面 |
| `+page.ts` | 服务端 + 浏览器 | 通用 load，两端通吃的取数 | 无通用数据 |
| `+page.server.ts` | 仅服务端 | server load，可碰数据库与密钥 | 无私密数据 |
| `+layout.svelte` | 服务端 + 浏览器 | 嵌套 UI 外壳，`<slot />` 出口 | 子页面直接顶替该层 |
| `+layout.ts` / `+layout.server.ts` | 同 page 对应物 | 布局级数据，逐层向下合并 | 布局无数据 |
| `+error.svelte` | 服务端 + 浏览器 | 消费 `error` 属性渲染错误 UI | 使用框架默认错误页 |
| `+server.ts` | 仅服务端 | 导出 GET/POST 等函数即 API 端点 | 无法对外提供接口 |

**讲解：**

1. 目录名即 URL 段；`[id]` 是动态段，`[...rest]` 是通配段，捕获其余所有路径。
2. 一条路由可以只有 `+server.ts`（纯 API），也可以只有 `+page.svelte`（纯静态 UI）。
3. 加号文件名是保留约定，不能自造名字；框架按文件名装配路由树。

## 2. 两种 load：通用 load 与 server load

SvelteKit 提供两种 load 函数，区别只在"运行在哪、能碰什么"。

| 维度 | 通用 load（`+page.ts`） | server load（`+page.server.ts`） |
| --- | --- | --- |
| 运行位置 | 首次 SSR 在服务端，之后客户端导航在浏览器 | 永远只在服务端 |
| 能访问 | 公开 API、url、fetch | 数据库、密钥、headers、cookies、locals |
| 代码去向 | 会被打进客户端 bundle 发到浏览器 | 代码留在服务端，只下发返回值 |
| 典型用途 | 聚合多个公开接口、前端缓存友好 | 鉴权、私密数据、直连数据库 |

```ts
// src/routes/dashboard/+page.server.ts —— server load：只跑在服务器
import type { PageServerLoad } from "./$types"
import { error } from "@sveltejs/kit"

export const load: PageServerLoad = async ({ locals }) => {
  // locals 由 hooks 注入（见第 6 节），这里可安全使用会话信息
  const user = await db.user.findUnique({ where: { id: locals.user?.id } })
  if (!user) error(401, "请先登录") // SvelteKit 2 支持直接调用，无需 throw
  return { email: user.email } // 返回值序列化后交给页面，取数逻辑不出服务器
}
```

```ts
// src/routes/dashboard/+page.ts —— 通用 load：服务端与浏览器都会执行
import type { PageLoad } from "./$types"

export const load: PageLoad = async ({ fetch, parent }) => {
  const { session } = await parent() // 拿到上游（server load、布局 load）已合并的数据
  // 适合调用公开接口：SSR 直连一次，客户端导航时从浏览器直接请求
  const res = await fetch("https://api.example.com/trending")
  return { trending: await res.json(), session }
}
```

**讲解：**

1. 同一目录两种 load 并存时：server load 先执行，通用 load 通过 `parent()` 读到它的
   结果；最终 data 由两层返回值合并，键冲突时以更靠近页面的为准。
2. 判断法则：数据要秘密就放 server load；要在客户端导航时复用浏览器缓存、且无密钥
   顾虑，才考虑通用 load。
3. `error(status, message)` 抛出后由对应层级的 `+error.svelte` 渲染。

## 3. load 的入参：params、url、fetch

```ts
// src/routes/blog/[category]/[slug]/+page.server.ts
import type { PageServerLoad } from "./$types"
import { error, redirect } from "@sveltejs/kit"

export const load: PageServerLoad = async ({ params, url, fetch, setHeaders }) => {
  // params：动态段集合，只含路径段，不含查询参数
  // url：URL 对象，查询参数从 url.searchParams 取
  const page = Number(url.searchParams.get("page") ?? "1")
  if (url.searchParams.has("latest")) {
    redirect(307, `/blog/${params.category}`) // 旧链接迁移：重定向到规范地址
  }

  // fetch：SvelteKit 包装的请求函数，SSR 时自动携带 Cookie 并转发协议头，
  // 且同一路由内对相同 GET 地址有去重；推荐替代原生 fetch
  const res = await fetch(`/api/${params.category}/posts?page=${page}`)
  if (!res.ok) error(404, "分类不存在")
  const posts = await res.json()

  setHeaders({ "cache-control": "public, max-age=60" }) // 声明响应缓存策略
  return { posts, page }
}
```

**讲解：**

1. 记住口诀：路径参数用 `params`，查询参数用 `url.searchParams`，发请求用入参的
   `fetch`。
2. `url.pathname`、`url.origin` 也可用于构造绝对地址；改 URL 应跳转而非静默替换。
3. 需要让"某状态变化触发重跑 load"时，可用 `depends("app:posts")` 声明自定义依赖，
   再配合 `invalidate("app:posts")` 手动刷新。

## 4. 流式 Promise：骨架先行，数据后到

慢接口不该阻塞整页输出。server load 中**不 await 的 Promise** 会被 SvelteKit 流式
下发：HTML 骨架先到，慢数据随后补齐。

```ts
// src/routes/feed/+page.server.ts
import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async ({ fetch }) => {
  // 轻量数据照常 await，随首屏 HTML 一起返回
  const nav = await fetch("/api/nav").then((r) => r.json())
  // 慢查询刻意不 await：作为未完成 Promise 返回，触发流式传输（键名任意）
  const comments = fetch("/api/comments").then((r) => r.json())
  const stats = fetch("/api/stats").then((r) => r.json())
  return { nav, comments, stats }
}
```

```svelte
<!-- src/routes/feed/+page.svelte -->
<script lang="ts">
  let { data } = $props()
</script>

<h1>{data.nav.title}</h1>

<!-- 用 {#await} 消费流式 Promise：先渲染占位，完成后自动补上内容 -->
{#await data.comments}
  <p>评论加载中，请稍候……</p>
{:then comments}
  <ul>
    {#each comments as c (c.id)}
      <li>{c.body}</li>
    {/each}
  </ul>
{:catch}
  <p>评论加载失败，请稍后重试</p>
{/await}
```

**讲解：**

1. 流式只在"load 运行于服务端 + 页面被 SSR"时生效；客户端导航时通用 load 在浏览器
   执行，Promise 直接在本地完成，无需流式。
2. 流式内容对搜索引擎可能不可见，SEO 关键数据请 await 后返回。
3. 未 await 的 Promise 出错会走 `{:catch}` 分支，不会拖垮整页。

## 5. 嵌套布局与布局组（group）

```text
src/routes/
  +layout.svelte              # 根布局：全站必有（导航栏）
  (marketing)/
    +layout.svelte            # 营销布局：白底大标题
    pricing/+page.svelte      #  /pricing
    about/+page.svelte        #  /about
  (app)/
    +layout.svelte            # 应用布局：侧边栏
    +layout.server.ts         # 应用区统一鉴权：无登录直接 error(401)
    dashboard/+page.svelte    #  /dashboard
    settings/+page.svelte     #  /settings
```

```svelte
<!-- src/routes/+layout.svelte —— Svelte 5 布局：children 是一个代码片段 -->
<script lang="ts">
  import type { LayoutProps } from "./$types"

  let { children }: LayoutProps = $props()
</script>

<header>全站导航</header>
<main>
  {@render children()} <!-- 渲染下一层（子布局或页面） -->
</main>
```

**讲解：**

1. 布局沿目录逐层嵌套：渲染 `/dashboard` 时根布局、`(app)` 布局、页面从外到内依次
   包裹；每层 `+layout.ts`/`+layout.server.ts` 的数据也逐层合并给下层。
2. 布局组 `(marketing)` 只负责组织文件，括号目录名不会出现在 URL 里。
3. 布局组的另一价值是"重置布局链"：组内页面只继承根布局与本组布局，不会被组外兄弟
   目录的布局影响。
4. Svelte 5 推荐用 `let { children } = $props()` 加 `{@render children()}`；旧写法
   `<slot />` 仍然兼容，两套代码库混读时要能认出来。

## 6. 服务端钩子：handle 与 locals

```ts
// src/hooks.server.ts —— 每个进入 SvelteKit 的请求都先经过 handle
import type { Handle } from "@sveltejs/kit"
import { sequence } from "@sveltejs/kit/hooks"
import { parseSession } from "$lib/server/auth"

const auth: Handle = async ({ event, resolve }) => {
  // 从 Cookie 解析会话，把用户挂到 locals：本次请求的"私人储物柜"
  event.locals.user = parseSession(event.cookies.get("session") ?? "")
  return resolve(event)
}

const logging: Handle = async ({ event, resolve }) => {
  const start = Date.now()
  const response = await resolve(event)
  // 简易访问日志：方法、路径、状态码、耗时
  console.log(`${event.request.method} ${event.url.pathname} -> ${response.status} (${Date.now() - start}ms)`)
  return response
}

export const handle = sequence(auth, logging) // 多个钩子按声明顺序串联
```

```ts
// src/app.d.ts —— 给 locals 声明全局类型，供 load/action/hook 共用
declare global {
  namespace App {
    interface Locals {
      user: { id: string; name: string } | null
    }
  }
}

export {}
```

**讲解：**

1. `locals` 是"每请求隔离"的内存空间：请求之间互不可见，是放会话、租户信息的唯一
   正确位置（对比第 7 篇讲的全局变量陷阱）。
2. 鉴权中间层的标准做法：hook 只负责"识别你是谁"，"你能干什么"留在 server load 与
   action 里按需校验。
3. `hooks.server.ts` 只参与服务端构建，永不进入浏览器 bundle；另有 `handleFetch`
   （拦截出站请求，例如给外部 API 补 Cookie）与 `handleError`（统一错误上报）。

## 7. 类型安全：自动生成的 $types

SvelteKit 会为每条路由生成虚拟模块 `./$types`：load 的入参、返回值、页面的 props
全部精确推断，无需手写接口。

```svelte
<!-- src/routes/dashboard/+page.svelte -->
<script lang="ts">
  import type { PageProps } from "./$types" // SvelteKit 2.16 起推荐

  // data 的类型已经包含 server load 与布局 load 合并后的全部字段
  let { data, form }: PageProps = $props()
</script>

<h1>{data.email}</h1>
```

```ts
// src/routes/dashboard/+page.server.ts —— load 函数同样有自动类型
import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async (event) => {
  // event.params、event.locals 均按当前路由与 app.d.ts 精确推断
  return { email: "user@example.com" }
}
```

**讲解：**

1. `./$types` 由 `vite dev`、`vite build` 或 `svelte-kit sync` 生成；类型报错时先跑
   一次 `npm run prepare`（即 sync）再检查。
2. `PageProps`/`LayoutProps` 覆盖 `data`、`params`、`form` 等页面 props；旧代码中的
   `PageData`、`LayoutServerData` 等仍可用，新项目优先用 Props 系列（以官方文档为准）。
3. 不仅是 load：`+server.ts` 的 `RequestHandler`、表单的 `Actions` 都出自同一套生成
   机制，这正是不用后端框架也能"前后端同构类型"的原因。

## 小结与延伸

> 加号文件分工：页面用 `+page.svelte`，公开取数用 `+page.ts`，私密取数用
> `+page.server.ts`，接口用 `+server.ts`，兜底用 `+error.svelte`；请求先过 hooks，
> locals 存会话，`./$types` 保类型。

1. 路由装配是纯约定：目录给 URL，加号文件给行为，记住职责表就记住了一半 SvelteKit。
2. 两种 load 的分界线是"能不能进浏览器"，凡是密钥、数据库、用户会话一律 server load。
3. 流式 Promise 用"骨架先行"换取感知性能，但 SEO 内容不要流式。
4. 布局组解决"多套外壳"的组织问题，URL 不变、布局链隔离。
5. hooks + locals 是鉴权中间层，`./$types` 是类型安全底座，两者都是零配置的。

**动手试试：**

1. 给 `blog/[id]` 同时写 `+page.server.ts` 与 `+page.ts`，在通用 load 里用 `parent()`
   观察数据合并顺序。
2. 做一个慢接口（`await new Promise((r) => setTimeout(r, 2000))`），用流式 Promise 与
   `{#await}` 对比首屏时间。
3. 用布局组把站点拆成 `(marketing)` 与 `(app)` 两套布局，并在 `(app)` 的
   `+layout.server.ts` 里校验 `locals.user`。

**延伸阅读：** SvelteKit 官方文档的 The load function、Hooks、Types 三章；本模块
下一篇 006 讲表单与 action，是 load 之外的另一半服务端交互。
