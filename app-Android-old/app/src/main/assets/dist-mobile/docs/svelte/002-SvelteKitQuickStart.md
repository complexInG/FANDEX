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
