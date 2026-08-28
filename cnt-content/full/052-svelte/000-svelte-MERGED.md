---
order: 10
title: svelte 模块文档合集
module: 'svelte'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：052-svelte/001-SvelteOverview.md ============ -->


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



<!-- ============ 文档分隔线：052-svelte/002-SvelteKitQuickStart.md ============ -->


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



<!-- ============ 文档分隔线：052-svelte/003-ReactivityRunes.md ============ -->


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



<!-- ============ 文档分隔线：052-svelte/004-ComponentsTransitions.md ============ -->


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
