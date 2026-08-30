---
order: 10
title: svelte 模块文档合集
module: 'svelte'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-30'
related: []
prerequisites: []
---

<!-- ============================================================ svelte/001-SvelteOverview ============================================================ -->

## 0. 五分钟创建第一个应用（先读这里）

> 学习目标：跑起 SvelteKit 项目，写一个带点击计数的组件，理解 `.svelte` 文件长什么样。

```bash
npx sv create my-app
cd my-app
npm run dev
```

**讲解：**

1. `sv create` 是 Svelte 官方 CLI，选择 SvelteKit（全栈框架）模板并回车确认即可。
2. `npm run dev` 启动开发服务器，默认 `http://localhost:5173`。
3. 打开 `src/routes/+page.svelte`，修改内容保存后浏览器热更新。

## 1. Svelte 是什么

Svelte 是一个"编译时框架"：React/Vue 在浏览器里用虚拟 DOM 做 diff，Svelte 则在构建时把组件编译成**直接操作 DOM 的原生 JavaScript**，所以运行时体积小、性能好。

Svelte 5（2024-10 发布）引入 **runes**（符文）语法：用 `$state`、`$derived`、`$effect` 显式声明响应式，替代旧版的 `let` 自动响应式与 `store` 体系。

### 1.1 版本现状（2026-08）

- Svelte 5.55.x 与 SvelteKit 2.57.x 为当前稳定版（2026-05）。
- 新项目统一使用 SvelteKit 脚手架；`+page.svelte` 文件即路由。

## 2. 第一个组件

```svelte
<!-- src/routes/+page.svelte -->
<script>
  let count = $state(0)

  function add() {
    count += 1
  }
</script>

<main>
  <h1>你好，Svelte 5</h1>
  <p>点击次数：{count}</p>
  <button onclick={add}>加一</button>
</main>
```

**讲解：**

1. `<script>` 里的 `$state(0)` 声明响应式变量：修改 `count` 时，所有用到它的 DOM 自动更新。
2. 模板里用 `{count}` 插值输出；`onclick={add}` 绑定事件，注意 Svelte 用属性名 `onclick`，不是 `onClick`。
3. 这个组件编译后没有虚拟 DOM——按钮点击直接更新那一个 `<p>` 的文本。

## 3. 与传统框架对比

| 维度 | React | Vue | Svelte 5 |
| --- | --- | --- | --- |
| 运行时 | 虚拟 DOM + fiber | 虚拟 DOM + 响应式代理 | 无虚拟 DOM，编译期优化 |
| 状态写法 | useState | ref/reactive | $state（runes） |
| 派生值 | useMemo | computed | $derived |
| 副作用 | useEffect | watchEffect | $effect |
| 学习曲线 | 中 | 中 | 低（模板接近 HTML） |

## 4. 动手试试

1. 给计数器加一个"减一"按钮，并把数字为 0 时按钮禁用。
2. 在 `src/routes/about/+page.svelte` 新建"关于"页面，用 `<a href="/about">` 跳转。
3. 把标题改成输入框：`<input bind:value={title} />`，观察输入时标题实时变化。

## 5. 一句话记住

> Svelte 在编译期把组件变成高效原生代码；Svelte 5 用 `$state/$derived/$effect` 三个符文管理响应式。

<!-- ============================================================ svelte/002-SvelteKitQuickStart ============================================================ -->

## 0. 一句话理解

> SvelteKit 的路由是"加号文件"约定：`+page.svelte` 是页面，`+layout.svelte` 是共享布局，`+page.server.ts` 在服务器加载数据。

## 1. 项目结构

```text
my-app/
  src/
    routes/
      +layout.svelte       # 全局布局（导航、页脚）
      +page.svelte         # 首页 /
      about/
        +page.svelte       # /about
      posts/
        [id]/
          +page.svelte     # /posts/1 动态路由
    lib/                   # 共享组件与工具
  static/                  # 静态资源
```

**讲解：**

1. 每个 `+page.svelte` 对应一个 URL：目录名即路径，`[id]` 是动态段。
2. `+layout.svelte` 包裹其下所有页面：导航写在布局里，切换页面时不会整体刷新。
3. `src/lib/` 是模块别名 `$lib` 的根目录，共享组件放这里。

## 2. 布局与页面

```svelte
<!-- src/routes/+layout.svelte -->
<script>
  import "../app.css"
</script>

<header>
  <nav>
    <a href="/">首页</a>
    <a href="/about">关于</a>
  </nav>
</header>

<main>
  <slot />
</main>
```

**讲解：**

1. `<slot />` 是布局的"出口"：子页面内容会渲染在这里。
2. `<a href>` 普通链接即可；SvelteKit 会拦截导航做客户端过渡。
3. 布局文件里的导航在页面切换时保留，避免重复渲染。

## 3. 服务器数据加载

```typescript
// src/routes/posts/+page.server.ts
import type { PageServerLoad } from "./$types"

interface Post {
  id: number
  title: string
}

export const load: PageServerLoad = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts")
  const posts: Post[] = await res.json()
  return { posts: posts.slice(0, 10) }
}
```

```svelte
<!-- src/routes/posts/+page.svelte -->
<script>
  let { data } = $props()
</script>

<ul>
  {#each data.posts as post (post.id)}
    <li><a href={`/posts/${post.id}`}>{post.title}</a></li>
  {/each}
</ul>
```

**讲解：**

1. `+page.server.ts` 的 `load` 在服务器执行，返回的对象会成为页面的 `data`。
2. 页面组件用 `$props()` 接收数据——Svelte 5 中 `$props()` 是 runes 语法的属性入口。
3. `{#each 列表 as 项 (key)}` 是 Svelte 的列表渲染块，`(post.id)` 是稳定 key。
4. 动态路由页 `posts/[id]/+page.svelte` 里用 `$props()` 拿到 `params.id`。

## 4. 动态路由页面

```svelte
<!-- src/routes/posts/[id]/+page.svelte -->
<script>
  let { params } = $props()
</script>

<h1>文章 #{params.id}</h1>
<a href="/posts">返回列表</a>
```

**讲解：**

1. `params` 由框架注入，`params.id` 即 URL 里的动态段值。
2. 真实项目里在此调用 `+page.server.ts` 的 `load` 按 id 取文章详情。
3. 404 场景返回 `error(404, "文章不存在")`，SvelteKit 会渲染 `+error.svelte`。

## 5. 动手试试

1. 新建 `about/+page.svelte` 并添加链接，确认路由生效。
2. 给 `posts/[id]` 写一个 `+page.server.ts`，按 id 取单篇文章并在页面展示标题。
3. 在布局里加 `<a href="/posts/1">第一篇文章</a>` 测试动态路由跳转。

## 6. 一句话记住

> SvelteKit 的文件约定：`+page` 是页面、`+layout` 是外壳、`.server` 后缀在服务器取数；`$props()` 是数据入口。

<!-- ============================================================ svelte/003-ReactivityRunes ============================================================ -->

## 0. 一句话理解

> runes 是 Svelte 5 的响应式语法糖：`$state` 存数据、`$derived` 算派生值、`$effect` 做副作用；`bind:` 让表单与状态自动同步。

## 1. $state 与 $derived

```svelte
<script>
  let price = $state(100)
  let qty = $state(2)

  let total = $derived(price * qty)

  function changePrice() {
    price = 120
  }
</script>

<p>单价：{price}，数量：{qty}，合计：{total}</p>
<button onclick={changePrice}>改为 120</button>
```

**讲解：**

1. `$state(100)` 创建响应式变量；直接赋值 `price = 120` 就会触发更新，不需要 `setState`。
2. `$derived(表达式)` 声明派生值：`total` 依赖 `price` 与 `qty`，任一变化时自动重算。
3. 派生值只读，不要手动赋值；它保证"显示值"永远与"源数据"一致。

## 2. $effect 副作用

```svelte
<script>
  let keyword = $state("")

  $effect(() => {
    console.log(`搜索关键词：${keyword}`)
  })
</script>

<input bind:value={keyword} placeholder="输入关键词" />
```

**讲解：**

1. `$effect(() => {...})` 在组件挂载后执行，并自动追踪函数内读取的响应式值；`keyword` 变化时重新执行。
2. 适用场景：日志、同步本地存储、调用非响应式 API；**不要**用它手动更新其他响应式变量（会循环）。
3. 函数内返回清理函数可做取消订阅等清理（类似 useEffect 的 cleanup）。

## 3. bind: 双向绑定

```svelte
<script>
  let name = $state("")
  let agree = $state(false)
  let color = $state("#00b894")
</script>

<input bind:value={name} placeholder="姓名" />
<input type="checkbox" bind:checked={agree} />
<input type="color" bind:value={color} />

<p>
  姓名：{name || "未填写"}，同意：{agree ? "是" : "否"}，
  颜色：{color}
</p>
```

**讲解：**

1. `bind:value` 让输入框的值与变量双向同步：输入即改变量，改变量即更新输入框。
2. 复选框用 `bind:checked`，颜色选择器用 `bind:value`，不同控件绑定不同属性。
3. 相比 React 的受控组件（value + onChange），Svelte 的 bind 写法更短，但原理相同。

## 4. 旧版 store 与新项目选择

```typescript
// stores/counter.ts（Svelte 4 写法，兼容保留）
import { writable } from "svelte/store"

export const count = writable(0)
```

```svelte
<!-- 旧版用法 -->
<script>
  import { count } from "$lib/stores/counter"
</script>

<p>{$count}</p>
```

**讲解：**

1. `writable(0)` 创建 store，`$count` 的 `$` 前缀是模板里的自动订阅语法。
2. 新项目优先用 runes（`$state`），跨组件共享状态时可以用 `$state` + 模块级导出，或继续用 store。
3. Svelte 5 完全兼容 store 语法，存量项目无需立刻迁移。

## 5. 动手试试

1. 做一个"单价 x 数量"计算器，含减号按钮且数量最小为 1（按钮用 `disabled={qty <= 1}`）。
2. 用 `$effect` 把 `name` 保存到 `localStorage`，组件加载时读回。
3. 用模块级 `$state` 做一个跨页面共享的购物车计数（`export const cartCount = $state(0)`）。

## 6. 一句话记住

> 响应式三件套：`$state` 存、`$derived` 算、`$effect` 监听；表单交互用 `bind:` 自动同步。

<!-- ============================================================ svelte/004-ComponentsTransitions ============================================================ -->

## 0. 一句话理解

> 父子通信两条路：属性（$props）从父到子，回调函数从子到父；过渡动画是 Svelte 的杀手锏，一条 `transition:fade` 指令即可。

## 1. 父传子：$props

```svelte
<!-- src/lib/Card.svelte -->
<script>
  let { title, description = "暂无描述" } = $props()
</script>

<article>
  <h2>{title}</h2>
  <p>{description}</p>
</article>
```

```svelte
<!-- 使用处 -->
<script>
  import Card from "$lib/Card.svelte"
</script>

<Card title="第一课" description="Svelte 组件通信" />
<Card title="默认描述示例" />
```

**讲解：**

1. `$props()` 返回组件收到的全部属性，解构出来即可使用。
2. `description = "暂无描述"` 是默认值：调用方不传时使用默认值。
3. 使用组件时像 HTML 标签一样传属性：`<Card title="..." />`。

## 2. 子传父：回调函数

```svelte
<!-- src/lib/ConfirmButton.svelte -->
<script>
  let { label = "删除", onConfirm } = $props()
</script>

<button
  onclick={() => {
    if (confirm("确定？")) onConfirm()
  }}
>
  {label}
</button>
```

```svelte
<!-- 使用处 -->
<script>
  import ConfirmButton from "$lib/ConfirmButton.svelte"

  function handleDelete() {
    console.log("执行删除")
  }
</script>

<ConfirmButton label="删除文章" onConfirm={handleDelete} />
```

**讲解：**

1. 子组件把"要通知父组件的事"声明为函数属性（`onConfirm`），父组件传入自己的处理函数。
2. 点击按钮后子组件调用 `onConfirm()`，父组件的 `handleDelete` 执行——数据流保持单向。
3. 这是 Svelte 5 推荐的子传父方式（旧版用 `createEventDispatcher`，新项目不必再用）。

## 3. bind:this 与组件绑定

```svelte
<!-- src/lib/InputBox.svelte -->
<script>
  let { value = $bindable(""), onchange } = $props()
</script>

<input
  bind:value={value}
  oninput={(e) => onchange?.(e.currentTarget.value)}
/>
```

**讲解：**

1. `$bindable("")` 把属性声明为"可双向绑定"：父组件传 `value` 时同步回传，不传时用空字符串默认值。
2. `bind:value={value}` 让输入框与这个可绑定属性双向同步——这是 Svelte 5 中"受控组件"的标准写法。
3. `onchange?.(...)` 是可选调用：父组件没传回调时安全跳过。
4. 需要直接操作 DOM 时用 `bind:this={element}` 拿到元素引用。

## 4. 过渡与动画

```svelte
<script>
  import { fade, slide } from "svelte/transition"
  import { flip } from "svelte/animate"

  let items = $state(["苹果", "香蕉", "橙子"])
  let visible = $state(true)
</script>

<button onclick={() => (visible = !visible)}>切换</button>

{#if visible}
  <p transition:fade={{ duration: 300 }}>淡入淡出</p>
  <p transition:slide={{ duration: 300 }}>滑入滑出</p>
{/if}

<ul>
  {#each items as item (item)}
    <li animate:flip>{item}</li>
  {/each}
</ul>
```

**讲解：**

1. `transition:fade` / `transition:slide` 在元素进入与离开时自动播放动画，参数对象控制时长。
2. `animate:flip` 让列表重排时其他项平滑移动，配合 `{#each}` 的 key 使用。
3. 动画均可用 CSS 变量与自定义 easing 控制；记得配合 `prefers-reduced-motion` 做无障碍降级。

## 5. 动手试试

1. 做一个 `TodoItem` 组件：接收 `todo` 属性，删除按钮通过回调通知父组件。
2. 给列表删除项加 `transition:fly` 飞出动画。
3. 用 `$derived` 统计未完成数量并显示在标题栏。

## 6. 一句话记住

> 父传子用 `$props()`，子传父用回调属性；列表动画一条 `animate:flip`，进出场一条 `transition:fade`。

<!-- ============================================================ svelte/005-SvelteKitRoutingLoading ============================================================ -->

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

<!-- ============================================================ svelte/006-FormActionsProgressive ============================================================ -->

## 0. 什么是渐进增强（先读这里）

> 学习目标：读完本文，你能用 actions 在服务端处理表单提交；区分 default 与具名
> action；理解 `form` 属性如何回填结果、`use:enhance` 如何把整页刷新升级为无刷新
> 交互；会用 fail(400) 与 redirect(303) 表达服务端结论；能落地"服务端唯一真相"的
> 校验模式，并把权限检查写在 action 内部；最后能判断何时该用 action、何时该用
> API 端点。

Form Actions 是 SvelteKit 的核心哲学：`<form>` 是原生 HTML 元素，不依赖 JavaScript
就能工作，框架在其上叠加增强。业务代码只写在服务端 action 里，客户端一行 `fetch`
都不用写。

## 1. 最小可用：default action

```svelte
<!-- src/routes/feedback/+page.svelte -->
<form method="POST">
  <!-- input 的 name 是服务端取值的键 -->
  <textarea name="message" rows="4" required></textarea>
  <button type="submit">提交反馈</button>
</form>
```

```ts
// src/routes/feedback/+page.server.ts
import type { Actions } from "./$types"

export const actions: Actions = {
  default: async ({ request }) => {
    const data = await request.formData() // 解析出的 FormData
    const message = String(data.get("message") ?? "")
    await saveFeedback(message) // 落库、发通知等副作用都写在服务端
    return { success: true } // 返回值会交给页面的 form 属性
  }
}
```

**讲解：**

1. `export const actions` 只能出现在 `+page.server.ts`（或 `+layout.server.ts`）中，
   这意味着处理函数永远运行在服务器，表单里没有任何业务逻辑可被窥探。
2. `<form method="POST">` 不写 `action` 属性时，提交目标就是当前路由的 default
   action——这就是"表单即接口"。
3. `request.formData()` 返回标准 `FormData`；`data.get()` 结果类型是
   `FormDataEntryValue | null`，用 `String(... ?? "")` 归一成字符串最稳妥。

## 2. 具名 action：一个页面多个动作

```svelte
<!-- src/routes/todos/+page.svelte -->
<form method="POST" action="?/create">
  <!-- action="?/名字" 指向同名 action -->
  <input name="title" placeholder="新待办" required />
  <button type="submit">创建</button>
</form>

{#each data.todos as todo (todo.id)}
  <li>
    {todo.title}
    <!-- 按钮级覆盖：同一表单内不同按钮触发不同 action -->
    <button type="submit" formaction="?/delete" name="id" value={todo.id}>
      删除
    </button>
  </li>
{/each}
```

```ts
// src/routes/todos/+page.server.ts
import type { Actions } from "./$types"

export const actions: Actions = {
  create: async ({ request }) => {
    const data = await request.formData()
    await db.todo.create({ data: { title: String(data.get("title")) } })
    return { ok: true }
  },
  delete: async ({ request }) => {
    const data = await request.formData()
    await db.todo.delete({ where: { id: String(data.get("id")) } })
    return { ok: true }
  }
}
```

| 表单写法 | 命中的 action |
| --- | --- |
| `<form method="POST">`（不写 action） | `default` |
| `<form method="POST" action="?/create">` | `create` |
| `<button formaction="?/delete">` | `delete`（覆盖表单级 action） |
| `<button formaction>` 带自身 `name/value` | 该按钮的值随提交一起发送 |

**讲解：**

1. `?/create` 的 `?` 表示"当前路由"，整体读作"当前页面的 create action"。
2. 一个页面承载整组增删改，是 actions 与 REST 风格 API 最大的体验差异：不必为每个
   动作单开一个端点文件。

## 3. form 属性与 use:enhance

action 的返回值去哪了？它成为页面的 `form` 属性；而 `use:enhance` 决定这次提交是
"整页刷新"还是"无刷新更新"。

```svelte
<!-- src/routes/subscribe/+page.svelte -->
<script lang="ts">
  import { enhance } from "$app/forms"
  import type { PageProps } from "./$types"

  let { form }: PageProps = $props() // action 返回值 / fail 数据都从这里来
</script>

<form method="POST" use:enhance>
  <!-- 加 use:enhance 即启用无刷新提交 -->
  <input name="email" type="email" required />
  <button type="submit">订阅</button>
</form>

{#if form?.errors}
  <!-- fail 返回的数据 -->
  <p role="alert">{form.errors.email}</p>
{:else if form?.success}
  <p>订阅成功，请查收邮件</p>
{/if}
```

| 对比项 | 不加 use:enhance | 加 use:enhance |
| --- | --- | --- |
| 提交方式 | 浏览器原生 POST，整页刷新 | 框架用 fetch 提交，原地更新 |
| 结果传达 | 服务端重新渲染页面并注入 form | 直接更新 form 属性 |
| 无 JS 环境 | 正常工作（这就是渐进增强的底线） | 自动退回原生行为 |
| load 重跑 | 页面重新执行 | 成功时 invalidateAll 重跑 load |

`use:enhance` 对不同响应的默认行为：

| 响应类型 | 默认处理 |
| --- | --- |
| success | invalidateAll 刷新所有 load，更新 form，重置表单 |
| failure | 只更新 form（保留用户输入，不清空） |
| redirect | 自动 goto 到目标地址 |
| error | 交给 `+error.svelte` 渲染 |

**讲解：**

1. `form` 属性在页面初次进入时是 `undefined`，提交后才有值；读取时全部用可选链。
2. 即使不做任何自定义，`use:enhance` 也值得加：不刷新、自动更新 form、成功后刷新
   数据，三件事零代码完成。

## 4. fail(400) 与 redirect(303)：服务端的两种答复

```ts
// src/routes/login/+page.server.ts
import { fail, redirect } from "@sveltejs/kit"
import type { Actions } from "./$types"

export const actions: Actions = {
  default: async ({ request, cookies }) => {
    const data = await request.formData()
    const email = String(data.get("email") ?? "")
    const password = String(data.get("password") ?? "")

    const user = await verifyUser(email, password)
    if (!user) {
      // fail：带状态码与数据"返回"页面，form 属性可拿到 errors 与 values
      return fail(400, {
        errors: { password: "邮箱或密码错误" },
        values: { email } // 回填用户已输入的部分，避免重打
      })
    }

    cookies.set("session", await createSession(user.id), {
      path: "/",
      httpOnly: true // 会话 Cookie 必须防脚本读取
    })
    redirect(303, "/dashboard") // redirect 是"抛出"式，之后的代码不会执行
  }
}
```

```svelte
<!-- 登录表单：value 绑定回填值 -->
<input name="email" value={form?.values?.email ?? ""} />
{#if form?.errors?.password}
  <p role="alert">{form.errors.password}</p>
{/if}
```

**讲解：**

1. `fail` 与 `redirect` 都从 `@sveltejs/kit` 导入；`fail` 用 `return`，`redirect` 是
   直接调用抛出（SvelteKit 2 无需 `throw` 前缀）。
2. POST 成功后重定向用 `303`：浏览器收到后会改用 GET 请求目标页，避免"刷新重复
   提交"，这就是经典的 PRG（Post/Redirect/Get）模式。
3. `fail` 的第二个参数就是交给 `form` 的数据；约定 `errors` 放错误、`values` 放回填
   值，页面渲染就有稳定契约。

## 5. 自定义 use:enhance：pending 态与取消

默认增强之外，常见需求是"提交中禁用按钮"与"提交前拦截"。自定义回调即可。

```svelte
<!-- src/routes/todos/+page.svelte -->
<script lang="ts">
  import { enhance } from "$app/forms"

  let submitting = $state(false) // pending 态用 runes 维护
</script>

<form
  method="POST"
  action="?/create"
  use:enhance={({ formElement, formData, cancel }) => {
    // 提交前回调：可拿到表单元素、formData，并能取消本次提交
    if (String(formData.get("title") ?? "").trim() === "") {
      cancel() // 阻止请求发出，表单恢复原状
      return
    }
    submitting = true
    // 返回的函数在响应到达后执行：可拿到 result 与 update
    return async ({ result, update }) => {
      submitting = false
      if (result.type === "failure") {
        console.log("服务端校验未通过", result.data) // 可自定义提示
      }
      await update({ reset: false }) // 默认成功后清空表单，这里保留输入
    }
  }}
>
  <input name="title" />
  <button type="submit" disabled={submitting}>
    {submitting ? "提交中……" : "添加"}
  </button>
</form>
```

**讲解：**

1. 提交前回调参数：`formElement`（DOM 表单）、`formData`（待发送数据）、
   `cancel`（取消函数）；不返回函数则走默认处理。
2. 响应回调参数：`result`（服务端结果对象，含 `type` 与 `data`）、`update`（等价于
   "执行默认行为"，可传 `{ reset: false }` 控制是否清空表单）。
3. 想完全接管就不调用 `update`，自行处理 `result`；一般场景
   `update({ reset: false })` 已够用。

## 6. 校验：服务端是唯一真相（zod）

```ts
// src/routes/signup/+page.server.ts
import { fail } from "@sveltejs/kit"
import { z } from "zod"
import type { Actions } from "./$types"

// Schema 一处定义：服务端校验 + 类型推导共用
const signupSchema = z.object({
  email: z.string().email("邮箱格式不正确"),
  password: z.string().min(8, "密码至少 8 位"),
  nickname: z.string().min(2, "昵称至少 2 个字符").max(20, "昵称过长")
})

export const actions: Actions = {
  default: async ({ request }) => {
    const raw = Object.fromEntries(await request.formData())
    const parsed = signupSchema.safeParse(raw)

    if (!parsed.success) {
      // 把字段错误整理成 { 字段名: 提示 } 的结构
      const errors: Record<string, string> = {}
      for (const issue of parsed.error.issues) {
        const key = String(issue.path[0])
        errors[key] ??= issue.message // 同一字段只保留第一条
      }
      return fail(400, { errors, values: raw })
    }

    await createUser(parsed.data) // parsed.data 已是校验过的强类型数据
    return { success: true }
  }
}
```

**讲解：**

1. 原则：HTML 的 `required`、`type="email"` 只是体验优化；绕过浏览器的任何请求
   （curl、脚本）都必须被服务端 Schema 拦截，所以服务端校验不可省略。
2. `safeParse` 不抛异常，返回 `{ success, data }` 或 `{ success, error }`；业务层
   只消费 `parsed.data`，天然获得类型收窄。
3. zod 不同大版本的 API 略有差异（如错误结构），以所用版本文档为准；校验失败统一
   `fail(400, { errors, values })`，页面端就有一套稳定的渲染契约。

## 7. 权限检查与 actions 对比 API 端点

```ts
// src/routes/posts/[id]/+page.server.ts
import { fail, redirect } from "@sveltejs/kit"
import type { Actions } from "./$types"

export const actions: Actions = {
  delete: async ({ locals, params }) => {
    // 鉴权紧贴业务入口：locals 由 hooks 注入（见第 5 篇第 6 节）
    if (!locals.user) return fail(401, { message: "请先登录" })

    const post = await db.post.findUnique({ where: { id: params.id } })
    if (!post) return fail(404, { message: "文章不存在" })
    if (post.authorId !== locals.user.id) {
      return fail(403, { message: "只能删除自己的文章" }) // 授权校验不可省略
    }

    await db.post.delete({ where: { id: params.id } })
    redirect(303, "/posts")
  }
}
```

| 维度 | Form Actions | `+server.ts` API 端点 |
| --- | --- | --- |
| 调用方 | 本站 `<form>`（人） | 任意 HTTP 客户端（程序） |
| 返回形式 | 数据 / fail / redirect 混用 | 纯 `Response` 对象 |
| 无 JS 可用 | 天然支持，可整页降级 | 不适用 |
| 页面联动 | 自动更新 form、刷新 load | 需要自己写状态同步 |
| CSRF | 默认受 SvelteKit 跨站 POST 保护 | 同样受保护 |
| 典型场景 | 页面内增删改、登录注册 | 公开 API、Webhook、多端共用接口 |

**讲解：**

1. 权限检查必须写在 action 内部，而不是只靠隐藏按钮——前端隐藏只是体验，服务端
   校验才是安全。
2. 经验法则：为"这个页面"服务就用 actions，为"多个客户端"服务才开 `+server.ts`；
   两者可以共存于同一目录。
3. SvelteKit 默认拒绝跨站 POST 提交（CSRF 保护基于 Origin 头），部署在反代后面时
   注意正确转发协议与主机头（以官方文档为准）。

## 小结与延伸

> 表单提交的完整链路：`<form method="POST">` 命中 action，服务端校验后
> `return fail` 回填错误、`redirect(303)` 跳转成功；`use:enhance` 把这条链路升级成
> 无刷新交互，而没有 JS 时一切照常。

1. actions 是"表单即接口"：`default` 与具名 action 覆盖一个页面的全部写操作。
2. `form` 属性是服务端与页面之间的回传通道，`errors`/`values` 是常用契约。
3. `fail(400)` 失败回填、`redirect(303)` 成功跳转，两种答复覆盖绝大多数场景。
4. 校验只认服务端 Schema；权限检查写在 action 里，不信任任何前端状态。
5. actions 面向页面，`+server.ts` 面向程序，按调用方选型而不是按习惯。

**动手试试：**

1. 把第 4 节的登录页跑起来，故意输错密码，观察 form 回填与地址栏变化；再删掉
   `use:enhance` 对比整页刷新的行为。
2. 给待办页面加"切换完成状态"的具名 action，按钮用 `formaction` 触发。
3. 在 action 里打印 `locals.user`，未登录时直接 `fail(401)`，验证 hooks 与 actions
   的配合。

**延伸阅读：** SvelteKit 官方文档的 Form actions 与 Progressive enhancement 两章；
本模块第 5 篇的 hooks 一节是本文权限检查的前置知识。

<!-- ============================================================ svelte/007-StateSharingDeployment ============================================================ -->

## 0. 从组件到生产（先读这里）

> 学习目标：读完本文，你能用 `.svelte.ts` 模块编写跨组件的 runes 共享状态；说清
> "全局变量在 SSR 下串号"的原理与规避规则；会用 context API 组织组件树内状态；
> 能区分四类环境变量模块并正确放置密钥；会按场景选择 adapter 并切换 ssr/prerender
> 渲染开关；最后能独立完成 Node 服务器、静态托管与容器化三种部署。

前三篇解决了"页面怎么写、数据怎么来、表单怎么提交"，本篇补上工程化收尾：状态放
哪里、配置从哪读、构建产物往哪发。这三件事做错，本地好好的应用上了生产就会出
诡异的串号、泄露或 404。

## 1. 跨组件共享状态：.svelte.ts 模块

给文件名加上 `.svelte` 后缀（`.svelte.ts`），runes 就能在普通模块中使用——这是
Svelte 5 官方推荐的跨组件状态方案，取代了大部分 Svelte 4 的 store 场景。

```ts
// src/lib/stores/cart.svelte.ts —— 文件名带 .svelte 才会编译 runes
export const cart = $state({
  items: [] as { id: string; qty: number }[],
  // getter 也能参与响应式：total 随 items 自动更新
  get total() {
    return this.items.reduce((sum, item) => sum + item.qty, 0)
  },
  add(id: string) {
    const found = this.items.find((item) => item.id === id)
    if (found) found.qty += 1
    else this.items.push({ id, qty: 1 })
  },
  clear() {
    this.items.length = 0
  }
})
```

```svelte
<!-- 任意组件：导入即共享同一份响应式状态 -->
<script lang="ts">
  import { cart } from "$lib/stores/cart.svelte"
</script>

<p>购物车共 {cart.total} 件</p>
<button onclick={() => cart.add("sku-001")}>加入购物车</button>
<button onclick={() => cart.clear()}>清空</button>
```

**讲解：**

1. 模块级 `$state` 必须挂在对象或类实例上：编译器禁止导出"可重新赋值"的
   `let x = $state()`，因为模块外的代码改不了引用；所以统一用"改属性"而非"换值"。
2. 所有导入方拿到同一个代理对象，任意组件改 `items`，所有使用 `cart.total` 的地方
   同步更新——这正是 003 篇 `$state` 深度响应式的跨文件版本。
3. 也可以导出类，在使用处 `new` 出实例：状态由组件树持有，隔离性更好（见第 3 节）。

## 2. 为什么不能随手用全局变量

```ts
// src/lib/bad.ts —— 错误示范，勿在生产代码中这样写
export let requestCount = 0 // 普通模块变量：非响应式，且 SSR 下全局共享

export function track() {
  requestCount += 1 // 浏览器里 UI 不会更新；服务器里所有请求一起累加
}
```

| 问题 | 普通全局变量 | `.svelte.ts` 中的 `$state` |
| --- | --- | --- |
| 响应式 | 无，UI 不更新 | 有，改动自动同步到所有使用处 |
| 浏览器内 | 每个标签页独立，尚可接受 | 每个标签页独立，符合直觉 |
| SSR 服务器 | 模块只加载一次，所有请求共享同一实例 | 同样共享（见下方规则） |
| 与用户相关的数据 | 会串号：用户 A 的数据漏给用户 B | 会串号：同理 |

**讲解：**

1. 服务器上模块只在进程启动时执行一次，"全局变量"被所有并发请求共用——这不是
   软微弱，是真实的数据越权事故来源。
2. 规则一：**请求级数据（用户、会话、租户）绝不放任何模块级变量**，一律走
   `locals`（第 5 篇）与 load 函数。
3. 规则二：模块级 `$state` 只放与用户无关的轻量状态（如"侧边栏是否折叠"），或
   确认只在浏览器使用的状态（用 `browser` 判断守卫）。
4. 规则三：需要"每棵组件树一份"的状态时，在组件里 `new` 出实例或用 context 下发
   （下一节）——SSR 渲染每个请求都会重建组件树，状态天然按请求隔离。

## 3. context API：组件树内的状态

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import { setContext } from "svelte"
  import type { LayoutProps } from "./$types"

  let { children }: LayoutProps = $props()

  // 在根布局初始化：每个请求渲染时都会重新执行，天然按请求隔离
  const theme = $state({ mode: "light" })
  setContext("theme", {
    get mode() {
      return theme.mode
    },
    toggle: () => (theme.mode = theme.mode === "light" ? "dark" : "light")
  })
</script>

{@render children()}
```

```svelte
<!-- 任意深度的子组件 -->
<script lang="ts">
  import { getContext } from "svelte"

  const theme = getContext("theme") // 沿组件树向上查找最近一次 setContext
</script>

<button onclick={theme.toggle}>切换主题（当前 {theme.mode}）</button>
```

**讲解：**

1. `setContext(key, value)` 必须在组件初始化阶段（顶层同步代码）调用，不能放在
   事件回调或 `$effect` 里；`getContext` 按键向上查找，拿不到返回 `undefined`。
2. context 是"树级"作用域：只沿当前分支向下可见，兄弟分支互不可见；SSR 时每棵
   请求树独立，正是第 2 节规则三的落地方式。
3. 典型用途：主题、国际化文案、表单上下文这类"一段 UI 共用、但不必进全局"的状态。
4. 键可用 `Symbol()` 避免命名冲突；要共享可写状态时，传 getter 或方法而非裸对象
   引用，防止调用方绕过接口直接改内部值。

## 4. 环境变量：static 与 dynamic

```bash
# .env（加入 .gitignore，绝不入库；可提交 .env.example 作为模板）
DATABASE_URL="postgres://user:pass@localhost:5432/app"
PAYMENT_API_KEY="sk-test-xxxxxxxx"
PUBLIC_APP_NAME="FANDEX"
```

```ts
// src/routes/api/health/+server.ts —— 只在服务端导入私有变量
import { DATABASE_URL, PUBLIC_APP_NAME } from "$env/static/private"
import { json } from "@sveltejs/kit"

export async function GET() {
  // 私有变量只在服务端代码中可用，构建时未使用会被剔除，不会泄漏
  return json({ db: DATABASE_URL !== "", name: PUBLIC_APP_NAME })
}
```

```svelte
<!-- 浏览器代码中只能使用 PUBLIC_ 前缀变量 -->
<script lang="ts">
  import { PUBLIC_APP_NAME } from "$env/static/public"
</script>

<h1>{PUBLIC_APP_NAME}</h1>
```

| 模块 | 可用位置 | 注入时机 | 典型用途 |
| --- | --- | --- | --- |
| `$env/static/private` | 仅服务端 | 构建时内联为字面量 | 数据库连接、密钥 |
| `$env/static/public` | 服务端 + 浏览器 | 构建时内联 | 站点名、公开配置 |
| `$env/dynamic/private` | 仅服务端 | 运行时读 `process.env` | 部署后才注入的密钥 |
| `$env/dynamic/public` | 服务端 + 浏览器 | 运行时读取 | 运行时可变的公开配置 |

**讲解：**

1. `static` 系列：构建时替换为字面量，tree-shaking 友好、类型完整，但改配置必须
   重新构建；`dynamic` 系列：运行时从真实环境读取，适合容器或平台动态注入，代价是
   失去内联优化。
2. 带 `PUBLIC_` 前缀的变量会进入浏览器 bundle，等同于公开信息；敏感值一旦误用
   `PUBLIC_` 即泄露，代码评审要盯住这个前缀。
3. 未使用的私有变量会被构建期剔除，这是"用哪个导哪个"的意义：不要写
   `import * as env` 一把全捞。
4. 变量的类型声明由 `svelte-kit sync` 依据 `.env` 生成，新增变量后重跑
   `npm run prepare` 即可消除类型报错。

## 5. 渲染开关：ssr 与 prerender

```ts
// src/routes/+layout.ts —— 全局默认：整站开启预渲染
export const prerender = true // 构建期生成静态 HTML
export const ssr = true // 服务端渲染开关
// export const csr = false // 还可关闭客户端运行时（极少用，了解即可）
```

```ts
// src/routes/dashboard/+page.ts —— 单页覆盖：后台页退出预渲染
export const prerender = false // 每个用户看到的都不同，不能预渲染
export const ssr = false // 再关掉 SSR：变成纯客户端渲染（类 SPA）
```

| ssr | prerender | 实际行为 | 适用场景 |
| --- | --- | --- | --- |
| true | false | 每次请求时服务器渲染 | 个性化页面（框架默认） |
| true | true | 构建期渲染成静态 HTML | 文档站、营销页、内容站 |
| false | true | 构建期只产出空壳 HTML | 配合静态托管的 SPA 模式 |
| false | false | 纯客户端渲染 | 强依赖浏览器 API 的后台页 |

**讲解：**

1. 开关写在 `+layout.ts` 即作用于其下所有路由，单页用 `+page.ts` 覆盖；两处都是
   编译期导出常量，不是运行时函数。
2. 预渲染动态路由需要枚举：用 `export const entries = () => [{ id: "1" }, ...]`
   提供列表，或保证页面被链接爬到；`prerender = true` 时 SvelteKit 会从 `/` 出发
   抓取全站链接。
3. 预渲染页面里的 load 在构建期执行——不能依赖 Cookie、`locals` 等请求时信息。
4. 组合口诀：内容不变选预渲染，人各不同走 SSR，浏览器专属才关 SSR。

## 6. adapter 选型与部署实操

| adapter | 构建产物 | 适用场景 |
| --- | --- | --- |
| `adapter-auto` | 由检测到的托管平台决定 | Vercel、Netlify 等零配置部署 |
| `adapter-node` | 独立 Node 服务器 | 自有服务器、容器、内网环境 |
| `adapter-static` | 纯静态文件 | GitHub Pages、对象存储 + CDN |

```js
// svelte.config.js —— 切换 adapter 只改这一处
import adapter from "@sveltejs/adapter-node"
import { vitePreprocess } from "@sveltejs/vite-plugin-svelte"

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),
  kit: {
    adapter: adapter({ out: "build" }) // 产物输出到 build/ 目录
  }
}

export default config
```

```bash
# 方式一：Node 服务器（adapter-node）
npm run build          # 产出 build/ 目录
ORIGIN=https://example.com PORT=3000 node build
# ORIGIN 用于让表单 CSRF 校验与绝对 URL 生成正确，生产环境建议显式指定
```

```js
// 方式二：静态托管（adapter-static），要求全站 prerender 或提供 fallback
import adapter from "@sveltejs/adapter-static"

/** @type {import('@sveltejs/kit').Config} */
export default {
  kit: {
    adapter: adapter({
      pages: "build",
      fallback: "index.html" // 未预渲染的路径回退到该 HTML（SPA 模式）
    })
  }
}
```

```dockerfile
# 方式三：容器化（多阶段构建，adapter-node）
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && pnpm install --frozen-lockfile
COPY . .
RUN pnpm run build

FROM node:22-alpine
WORKDIR /app
# adapter-node 产物运行需要 build/ 与生产依赖
COPY --from=build /app/build ./build
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./package.json
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "build/index.js"]
```

**讲解：**

1. 选型顺序：有托管平台先用 `adapter-auto`；要上自有服务器或容器选
   `adapter-node`；页面全部可预渲染才用 `adapter-static`。
2. `adapter-static` 硬性要求：`prerender = true`（或每个入口页可达）；做不到就配置
   `fallback` 走 SPA 回退，刷新任意路径都不会 404。
3. `adapter-node` 的运行时行为由环境变量控制：`PORT`、`HOST`、`ORIGIN` 常用；
   反向代理后务必设置 `ORIGIN`，否则表单 CSRF 校验会误伤正常请求。
4. 容器部署把密钥交给运行时环境（`$env/dynamic/private` 或平台注入），不要在
   构建阶段把生产密钥打进镜像层。

## 小结与延伸

> 状态放三处：跨组件的客户端状态进 `.svelte.ts`，树级状态进 context，请求级数据
> 进 locals/load；配置分四类 `$env` 模块，密钥只走服务端；部署按平台选 adapter，
> 内容站开 prerender，应用站默认 SSR。

1. `.svelte.ts` 是 Svelte 5 的跨组件状态正解，但记住 SSR 共享三规则（第 2 节）。
2. context 拿来下发树级状态，每棵组件树独立副本，天然规避 SSR 串号。
3. `$env/static/private` 与 `$env/static/public` 的边界就是服务端与浏览器的边界，
   `PUBLIC_` 前缀即公开承诺。
4. `ssr`/`prerender` 是编译期开关，`+layout.ts` 定基调、`+page.ts` 做覆盖。
5. adapter 决定产物形态：托管平台、Node 服务器、纯静态三条路，切换只改
   `svelte.config.js` 一处。

**动手试试：**

1. 写一个 `sidebar.svelte.ts` 共享折叠状态，再故意把用户对象放进去，用两个浏览器
   窗口观察 SSR 串号，最后迁到 `locals` 修复。
2. 用 `$env/static/public` 做站点名，分别跑 dev 与 build，观察变量内联进产物。
3. 把一个练习项目先后用 `adapter-node` 本地启动与 `adapter-static` 预渲染，对比
   两种产物目录结构。

**延伸阅读：** Svelte 官方文档 State 与 Context 章节、SvelteKit 官方文档
Environment variables 与 Adapters 章节；至此 svelte 模块 1-7 篇构成从语法到上线的
完整链路。
