---
order: 10
title: nextjs 模块文档合集
module: 'nextjs'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：048-nextjs/001-NextJS16Overview.md ============ -->


## 0. 五分钟创建第一个项目（先读这里）

> 学习目标：跑起一个 Next.js 项目，理解"页面文件 = 路由"。

```bash
npx create-next-app@latest my-app --ts --app --tailwind --eslint
cd my-app
npm run dev
```

**讲解：**

1. `create-next-app` 是官方脚手架：`--ts` 使用 TypeScript，`--app` 使用 App Router（当前唯一推荐），`--tailwind` 预装 Tailwind CSS v4。
2. `npm run dev` 启动开发服务器，默认地址 `http://localhost:3000`。
3. 打开 `app/page.tsx`，修改文字保存，浏览器会热更新——这就是"文件即路由"的起点。

## 1. Next.js 是什么

Next.js 是 React 的全栈元框架，由 Vercel 维护。它在 React 之上补齐了生产应用需要的：

- 文件路由与布局系统（App Router）；
- 服务器组件（Server Components）与客户端组件；
- 数据获取、缓存与增量静态再生（ISR）；
- 图片、字体、SEO 元数据的内置优化；
- 前后端一体（Route Handlers、Server Actions）。

### 1.1 版本现状（2026-08）

- Next.js 16.2.x 为 Active LTS（16.0 于 2025-10 发布；16.2.11 为 2026-07 安全版本）。
- 要求 Node.js 20.9+，推荐 Node 22 LTS；React 19.2+。
- 新项目统一使用 App Router；Pages Router 仅用于维护存量项目。

## 2. 认识项目结构

```text
my-app/
  app/
    layout.tsx      # 根布局：所有页面共享的壳（html/body）
    page.tsx        # 首页，对应路径 /
    globals.css     # 全局样式
  public/           # 静态资源（图片等）
  package.json
  tsconfig.json
  next.config.ts    # Next.js 配置文件
```

**讲解：**

1. `app/` 目录下的每个文件都映射路由：`page.tsx` 是页面，`layout.tsx` 是布局。
2. 组件默认是**服务器组件**：在服务器上渲染成 HTML 再发给浏览器，代码里可以直接读数据库、访问环境变量。
3. 需要交互（onClick、useState）的文件要在顶部写 `"use client"`，标记为客户端组件。

## 3. 第一个页面：服务器组件

```tsx
// app/page.tsx
export default function Home() {
  return (
    <main>
      <h1>你好，Next.js 16</h1>
      <p>这个页面在服务器上渲染，浏览器里能看到完整 HTML。</p>
    </main>
  )
}
```

**讲解：**

1. `export default function Home()` 是页面组件的固定写法，文件名决定路由，函数名只用于开发调试。
2. 没有 `"use client"` 的组件默认是服务器组件：用户点击"查看源代码"能看到渲染好的完整内容，SEO 友好。
3. `main` 等语义化标签与 HTML 一致，配合 Tailwind 类名即可快速排版。

## 4. 动手试试

1. 在 `app/about/page.tsx` 新建一个"关于"页面，访问 `/about` 看是否生效。
2. 在首页加一张图片：把图片放进 `public/`，用 `<img src="/xxx.png" alt="描述" />`（进阶后用官方 `next/image`）。
3. 新建 `app/contact/page.tsx`，用 `<Link href="/about">` 在页面之间跳转（下一章详解路由）。

## 5. 一句话记住

> Next.js = React + 文件路由 + 服务器渲染；`app/` 里放 `page.tsx` 就有页面，默认服务器组件、需要交互才加 `"use client"`。



<!-- ============ 文档分隔线：048-nextjs/002-AppRouterRouting.md ============ -->


## 0. 一句话理解

> App Router 的文件约定：`page.tsx` 是页面、`layout.tsx` 是共享壳、`[参数]` 文件夹是动态路由、`loading/error/not-found` 是三种状态页面。

## 1. 布局嵌套

```tsx
// app/layout.tsx：根布局
import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "我的站点",
  description: "Next.js 16 学习示例"
}

export default function RootLayout({
  children
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN">
      <body>
        <header>全站导航</header>
        {children}
        <footer>页脚</footer>
      </body>
    </html>
  )
}
```

**讲解：**

1. `layout.tsx` 接收 `children`（子路由渲染结果），布局本身在切换子页面时**不会重新渲染**，导航条写在布局里可以避免整页刷新。
2. `metadata` 导出对象用于设置页面标题与描述，Next.js 会自动注入 `<head>`，这是内置 SEO 能力。
3. `lang="zh-CN"` 声明页面语言，有利于无障碍与搜索引擎。

## 2. 动态路由

创建文件夹 `app/posts/[id]/page.tsx`：

```tsx
import { notFound } from "next/navigation"

export default async function PostPage({
  params
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  if (!/^\d+$/.test(id)) notFound()

  return <main>文章编号：{id}</main>
}
```

**讲解：**

1. 文件夹名 `[id]` 表示动态段：`/posts/42` 会匹配并把 `id` 设为 `"42"`。
2. Next.js 15+ 中 `params` 是 Promise，必须 `await` 后才能读取。
3. `notFound()` 会触发最近的 `not-found.tsx`，返回 404 页面；示例用正则校验"必须是数字"。
4. 多段动态路由用 `[...slug]`（匹配 1 段以上）或 `[[...slug]]`（可匹配 0 段）。

## 3. 导航

```tsx
import Link from "next/link"

export default function Nav() {
  return (
    <nav>
      <Link href="/">首页</Link>
      <Link href="/about">关于</Link>
      <Link href={`/posts/${42}`}>文章 42</Link>
    </nav>
  )
}
```

**讲解：**

1. `next/link` 是客户端导航：点击后不会整页刷新，Next.js 会预取视口内的链接页面。
2. 服务端组件里也能用 `Link`，它最终在客户端接管导航。
3. 编程式跳转用 `useRouter()`（来自 `next/navigation`，必须在 `"use client"` 组件里）。

## 4. 加载与错误状态

```tsx
// app/posts/[id]/loading.tsx
export default function Loading() {
  return <p>加载中……</p>
}
```

```tsx
// app/posts/[id]/error.tsx（"use client" 是必须的）
"use client"

export default function Error({ reset }: { reset: () => void }) {
  return (
    <div>
      <p>出错了</p>
      <button onClick={reset}>重试</button>
    </div>
  )
}
```

**讲解：**

1. `loading.tsx` 在路由进入 Suspense 加载态时显示，配合流式渲染避免白屏。
2. `error.tsx` 必须标注 `"use client"`，因为错误边界需要在浏览器里捕获并交互。
3. `reset` 函数由 Next.js 注入，点击后重新渲染出错的页面。

## 5. 动手试试

1. 给 `app/posts/[id]/page.tsx` 加 `generateStaticParams`，预习静态生成：
   ```tsx
   export function generateStaticParams() {
     return [{ id: "1" }, { id: "2" }]
   }
   ```
2. 在 `app/posts/` 下新建 `not-found.tsx`，访问一个非数字 id，确认 404 页面生效。
3. 把导航改成动态生成的文章列表（先写死 5 个 id）。

## 6. 一句话记住

> 路由就是文件夹约定：`page` 管页面、`layout` 管外壳、`[id]` 管动态参数、`loading/error/not-found` 管三种状态。



<!-- ============ 文档分隔线：048-nextjs/003-DataFetchingCaching.md ============ -->


## 0. 一句话理解

> 服务器组件里可以直接 `await fetch()` 拿数据；缓存策略就三个词：`force-cache` 存起来、`no-store` 不存、`revalidate` 定期更新。

## 1. 服务器组件直接取数

```tsx
// app/posts/page.tsx
interface Post {
  id: number
  title: string
}

export default async function PostsPage() {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts")
  const posts: Post[] = await res.json()

  return (
    <ul>
      {posts.slice(0, 10).map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

**讲解：**

1. 页面组件标 `async` 后可直接 `await` 网络请求——这段代码运行在服务器上，不会出现在浏览器端 JS 里。
2. `res.json()` 把响应解析为对象数组；用 `interface Post` 声明类型后，`post.title` 有完整类型提示。
3. `key` 属性是 React 列表渲染的要求，用稳定的 `post.id` 而不是数组下标。

## 2. 缓存策略

```tsx
// 静态：构建时抓一次，之后直接读缓存（默认）
await fetch("https://api.example.com/static")

// 动态：每次请求都重新抓取
await fetch("https://api.example.com/dynamic", { cache: "no-store" })

// 增量：每 60 秒后台重新生成一次
await fetch("https://api.example.com/price", { next: { revalidate: 60 } })
```

**讲解：**

1. 不传选项时 Next.js 会尽力静态化：构建时抓取并缓存，适合内容型页面。
2. `cache: "no-store"` 跳过缓存，适合登录态、实时库存等数据。
3. `next.revalidate: 60` 实现 ISR：用户仍读到旧缓存，后台每 60 秒最多重建一次，兼顾速度与新鲜度。

## 3. 客户端数据获取

```tsx
"use client"

import { useEffect, useState } from "react"

export default function LiveTime() {
  const [now, setNow] = useState("")

  useEffect(() => {
    const timer = setInterval(() => {
      setNow(new Date().toLocaleTimeString())
    }, 1000)
    return () => clearInterval(timer)
  }, [])

  return <p>现在时间：{now}</p>
}
```

**讲解：**

1. 需要实时更新、用户交互的数据才放客户端组件（`"use client"`）。
2. `useEffect` 在浏览器挂载后执行，`return () => clearInterval(timer)` 是清理函数，防止组件卸载后定时器泄漏。
3. 更复杂的数据请求建议使用 `useSWR` 或 TanStack Query 管理缓存与重试。

## 4. Server Actions：表单提交

```tsx
// app/contact/page.tsx
async function submit(formData: FormData) {
  "use server"

  const name = formData.get("name")
  // 生产环境：写入数据库或调用 API
  console.log("收到提交：", name)
}

export default function ContactPage() {
  return (
    <form action={submit}>
      <input name="name" placeholder="你的名字" required />
      <button type="submit">提交</button>
    </form>
  )
}
```

**讲解：**

1. 函数内部标注 `"use server"` 后成为 Server Action：浏览器把表单数据发给服务器执行，不需要自己写 API 路由。
2. `formData.get("name")` 读取表单字段，字段名以 `input` 的 `name` 属性为准。
3. 没有 JavaScript 也能提交，这是渐进增强；执行成功后可用 `revalidatePath("/")` 刷新相关页面缓存。

## 5. 动手试试

1. 把首页改成从 `jsonplaceholder` 拉取 10 条文章并展示。
2. 给文章列表加 `{ next: { revalidate: 30 } }`，观察构建日志中的重新验证行为。
3. 写一个 Server Action 收集"订阅邮箱"，提交后在页面上方显示成功提示（提示可用 `useActionState`）。

## 6. 一句话记住

> 能服务器取数就在服务器取；`no-store` 求实时、`revalidate` 求平衡、默认缓存求速度；表单用 Server Action 最省事。



<!-- ============ 文档分隔线：048-nextjs/004-DeploymentOptimization.md ============ -->


## 0. 一句话理解

> 部署 = `next build` 产出优化后的产物；优化 = 图片走 next/image、字体走 next/font、慢查询加缓存。

## 1. 构建与产物

```bash
npm run build
```

**讲解：**

1. 构建时 Next.js 会输出三类页面：静态页（SSG）、ISR 页（按 revalidate 更新）、动态页（SSR 或客户端渲染）。
2. 构建日志里 `○` 表示静态、`ƒ` 表示动态、`●` 表示 ISR，新项目应尽量让更多页面静态化。
3. 产物默认输出到 `.next/`；用 Docker 部署时参考 `next.config.ts` 的 `output: "standalone"` 模式，只复制运行所需文件。

## 2. 环境变量

```bash
# .env.local（仅本机，不提交 git）
DATABASE_URL="postgres://..."
NEXT_PUBLIC_SITE_URL="https://example.com"
```

```tsx
// 服务端读取
const dbUrl = process.env.DATABASE_URL
// 客户端读取（必须 NEXT_PUBLIC_ 前缀，会打包进浏览器代码）
const siteUrl = process.env.NEXT_PUBLIC_SITE_URL
```

**讲解：**

1. 不带前缀的变量只在服务器端可用，密钥（数据库密码、API Key）绝不能加 `NEXT_PUBLIC_`。
2. 以 `NEXT_PUBLIC_` 开头的变量会被内联进浏览器包，任何人都能看到，只放公开信息。
3. 生产环境在部署平台配置同名变量即可覆盖，不需要改代码。

## 3. 图片与字体优化

```tsx
import Image from "next/image"
import { Inter } from "next/font/google"

const inter = Inter({ subsets: ["latin"] })

export default function Home() {
  return (
    <main className={inter.className}>
      <Image
        src="/hero.png"
        alt="首页横幅"
        width={1200}
        height={600}
        priority
      />
    </main>
  )
}
```

**讲解：**

1. `next/image` 自动做响应式尺寸、WebP/AVIF 转换与懒加载；`priority` 让首屏图片提前加载。
2. `width/height` 必须提供，用来预留空间防止布局偏移（CLS）。
3. `next/font` 自动托管字体并优化加载，避免第三方字体阻塞渲染；中文字体体积大，建议只引入需要的字重或使用子集。

## 4. 核心性能指标自查

| 指标 | 含义 | 常见优化 |
| --- | --- | --- |
| LCP | 最大内容绘制（首屏） | 图片加 priority、减少阻塞脚本、服务端渲染关键内容 |
| CLS | 布局偏移 | 图片/字体预留尺寸，避免内容弹出 |
| INP | 交互延迟 | 减少客户端 JS、拆分组件、避免长任务 |
| TTFB | 首字节时间 | 使用 CDN 边缘缓存、数据库查询优化、ISR |

## 5. 部署方式选择

- **Vercel**：官方平台，push 即部署，推荐学习与中小企业使用；
- **自托管 Node**：`output: "standalone"` + Docker + Nginx 反向代理；
- **静态导出**：纯静态站可 `output: "export"` 部署到任意静态托管，但会失去 SSR/ISR 能力。

## 6. 动手试试

1. 把项目部署到 Vercel（`vercel` 命令或 GitHub 导入），观察构建日志中的路由类型。
2. 用 Chrome DevTools 的 Lighthouse 跑一次性能报告，对照上表优化其中一项。
3. 写一个 Dockerfile（多阶段构建 + standalone 输出），本地 `docker build` 成功。

## 7. 一句话记住

> 构建时能静态就静态，密钥只进服务端环境变量，图片字体交给 next/image 与 next/font，性能报告用 Lighthouse 说话。
