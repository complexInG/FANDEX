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
