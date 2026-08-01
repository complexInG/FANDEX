---
order: 102
title: 'Next.js-App-Router'
module: react
category: 'dev-lang'
difficulty: advanced
description: 'Next.js App Router详解：文件夹约定、布局、加载态、错误态。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'react/React-Compiler自动记忆化'
  - 'react/Server-Components与Client-Components'
  - 'react/React-19新增API'
  - react/并发渲染与可中断更新
prerequisites:
  - react/概述与环境配置
---

# Next.js App Router API 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 文件夹约定

### 1.1 路由结构

```
app/
  layout.tsx          # 根布局
  page.tsx            # 首页 /
  loading.tsx         # 全局加载态
  error.tsx           # 全局错误态
  not-found.tsx       # 404 页面
  about/
    page.tsx          # /about
  blog/
    layout.tsx        # /blog 布局
    page.tsx          # /blog
    [slug]/
      page.tsx        # /blog/:slug
```

### 1.2 特殊文件

| 文件            | 用途           |
| --------------- | -------------- |
| `layout.tsx`    | 共享布局       |
| `page.tsx`      | 路由页面       |
| `loading.tsx`   | 加载状态       |
| `error.tsx`     | 错误处理       |
| `not-found.tsx` | 404            |
| `template.tsx`  | 重新挂载的布局 |
| `default.tsx`   | 并行路由默认   |

## 2. 布局嵌套

```tsx
// app/layout.tsx
export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <nav>导航</nav>
        {children}
      </body>
    </html>
  );
}

// app/blog/layout.tsx
export default function BlogLayout({ children }) {
  return (
    <div className="blog-layout">
      <Sidebar />
      {children}
    </div>
  );
}
```

## 3. 加载态

```tsx
// app/blog/loading.tsx
export default function Loading() {
  return <Skeleton />;
}
```

Next.js 自动用 Suspense 包裹页面，显示 loading.tsx。

## 4. 错误态

```tsx
// app/error.tsx
'use client';

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>出错了</h2>
      <button onClick={reset}>重试</button>
    </div>
  );
}
```

## 5. 数据获取

```tsx
// Server Component 中直接 async
async function Page() {
  const data = await fetch('https://api.example.com/data');
  return <div>{data.title}</div>;
}
```
## 文件约定 (File Conventions)

**layout.tsx 布局**
`app/<segment>/layout.tsx`
```tsx
export default function Layout({ children }: { children: React.ReactNode }) {
  return <section>{children}</section>;
}
```

**page.tsx 页面**
`app/<segment>/page.tsx`
```tsx
export default function Page() {
  return <h1>Home</h1>;
}
```

**loading.tsx 加载态**
`app/<segment>/loading.tsx`
```tsx
export default function Loading() {
  return <Spinner />;
}
```

**error.tsx 错误边界**
`app/<segment>/error.tsx`
```tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div>
      <p>{error.message}</p>
      <button onClick={reset}>重试</button>
    </div>
  );
}
```

**not-found.tsx 404 页面**
`app/<segment>/not-found.tsx`
```tsx
export default function NotFound() {
  return <h1>页面不存在</h1>;
}
```

**template.tsx 模板**
`app/<segment>/template.tsx`
```tsx
export default function Template({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>;
}
```

**default.tsx 默认插槽**
`app/<segment>/default.tsx`
```tsx
export default function Default() {
  return <p>默认内容</p>;
}
```

**route.ts API 路由**
`app/api/<name>/route.ts`
```tsx
export async function GET(request: Request) {
  return Response.json({ ok: true });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json(body, { status: 201 });
}
```

**middleware.ts 中间件**
`middleware.ts`
```tsx
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  return NextResponse.next();
}

export const config = {
  matcher: ['/dashboard/:path*'],
};
```

---

## 动态路由文件

**动态路由 [param]**
`app/users/[id]/page.tsx`
```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <h1>User {id}</h1>;
}
```

**catch-all [...slug]**
`app/docs/[...slug]/page.tsx`
```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string[] }>;
}) {
  const { slug } = await params;
  return <p>{slug.join('/')}</p>;
}
```

**catch-all 可选 [[...slug]]**
`app/docs/[[...slug]]/page.tsx`
```tsx
export default async function Page({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}) {
  const { slug } = await params;
  return <p>{slug?.join('/') ?? 'home'}</p>;
}
```

---

## async params / searchParams

**page props 类型**
```tsx
type PageProps = {
  params: Promise<{ [key: string]: string }>;
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
};

export default async function Page({ params, searchParams }: PageProps) {
  const { id } = await params;
  const { q } = await searchParams;
  return <div>{id} - {q}</div>;
}
```

---

## cookies / headers

**cookies 服务端**
`import { cookies } from 'next/headers';`
```tsx
import { cookies } from 'next/headers';

export default async function Page() {
  const cookieStore = await cookies();
  const token = cookieStore.get('token')?.value;
  return <p>{token}</p>;
}
```

**cookies 设置**
```tsx
const cookieStore = await cookies();
cookieStore.set('theme', 'dark', {
  httpOnly: true,
  secure: true,
  maxAge: 60 * 60 * 24 * 7,
  path: '/',
});
```

**headers 服务端**
`import { headers } from 'next/headers';`
```tsx
import { headers } from 'next/headers';

export default async function Page() {
  const headerList = await headers();
  const userAgent = headerList.get('user-agent');
  return <p>{userAgent}</p>;
}
```

---

## Server Actions

**'use server'**
```tsx
// app/actions.ts
'use server';

export async function createItem(formData: FormData) {
  const title = formData.get('title') as string;
  await db.items.create({ data: { title } });
}

// 调用
'use client';
import { createItem } from '@/app/actions';

function Form() {
  return (
    <form action={createItem}>
      <input name="title" />
      <button type="submit">创建</button>
    </form>
  );
}
```

**inline server action**
```tsx
export default function Page() {
  async function submit(formData: FormData) {
    'use server';
    await db.items.create({ data: { title: formData.get('title') as string } });
  }
  return <form action={submit}><input name="title" /><button>OK</button></form>;
}
```

---

## Layout / Page 元数据

**metadata 静态**
`export const metadata: Metadata = {...}`
```tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: '用户中心',
  description: '用户信息管理',
  openGraph: { images: ['/og.png'] },
};
```

**generateMetadata 动态**
`export async function generateMetadata({ params }): Promise<Metadata>`
```tsx
export async function generateMetadata({
  params,
}: {
  params: Promise<{ id: string }>;
}): Promise<Metadata> {
  const { id } = await params;
  const user = await getUser(id);
  return { title: user.name };
}
```

---

## navigation API

**useRouter**
`import { useRouter } from 'next/navigation';`
```tsx
'use client';
import { useRouter } from 'next/navigation';

export default function Page() {
  const router = useRouter();
  return (
    <button onClick={() => router.push('/login')}>登录</button>
    <button onClick={() => router.back()}>返回</button>
    <button onClick={() => router.refresh()}>刷新</button>
  );
}
```

**usePathname / useSearchParams**
```tsx
'use client';
import { usePathname, useSearchParams } from 'next/navigation';

function Breadcrumb() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const q = searchParams.get('q');
  return <span>{pathname}{q ? `?q=${q}` : ''}</span>;
}
```

---

## Link 与 Image

**Link**
`<Link href=<path> [prefetch]>...</Link>`
```tsx
import Link from 'next/link';

<Link href="/dashboard">控制台</Link>
<Link href={{ pathname: '/users', query: { id: '1' } }}>用户</Link>
<Link href="/about" prefetch={false}>关于</Link>
```

**Image 优化图片**
`<Image src=<src> alt=<alt> [width] [height] [fill] />`
```tsx
import Image from 'next/image';

<Image src="/logo.png" alt="Logo" width={120} height={40} />
<Image src={user.avatar} alt={user.name} fill sizes="(max-width: 768px) 100vw" />
```

---

## generateStaticParams

**静态参数生成**
`export async function generateStaticParams()`
```tsx
export async function generateStaticParams() {
  const users = await db.users.findMany();
  return users.map(u => ({ id: u.id }));
}

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  return <h1>{id}</h1>;
}
```

---

## Suspense 与流式渲染

**Suspense 边界**
```tsx
import { Suspense } from 'react';

export default function Page() {
  return (
    <Suspense fallback={<Spinner />}>
      <AsyncComponent />
    </Suspense>
  );
}
```

**loading.tsx 等价**
```tsx
// app/dashboard/loading.tsx
export default function Loading() {
  return <div>加载中...</div>;
}
```

## 参考文献



React 官方文档：https://react.dev/
React 19 发布说明：https://react.dev/blog/2024/12/05/react-19
TanStack Query：https://tanstack.com/query/latest
Zustand：https://zustand.docs.pmnd.rs/
Next.js：https://nextjs.org/

## 延伸阅读



React Hooks 深入，见 011-react 模块 Hooks 文档。
React 与 TypeScript 类型，见 009-typescript 模块。
前端构建与 Vite，见 057-vite 模块（如已加入）。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 React 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与环境配置 | 001-OverviewEnvSetup | 本文的前置基础 |
| 组件与Props | 002-ComponentProps | 本文的并列主题 |
| 状态与事件 | 003-StateEvent | 本文的并列主题 |
| Hooks深入 | 004-HooksDeep | 本文的原理深化 |
| Context与全局状态 | 005-ContextGlobalState | 本文的并列主题 |
| React19新特性 | 006-React19NewFeatures | 本文的并列主题 |
| 路由与数据获取 | 007-RouteDataFetch | 本文的并列主题 |
| 性能优化 | 008-PerformanceOptimization | 本文的性能延伸 |
| 测试与工程化 | 009-TestEngineering | 本文的并列主题 |
| Next.js全栈开发 | 010-NextJSFullStack | 本文的并列主题 |
| JSX深度解析 | 011-JSXDeepAnalysis | 本文的并列主题 |
| Fiber架构 | 012-FiberArchitecture | 本文的原理深化 |
| Concurrent模式 | 013-ConcurrentMode | 本文的并列主题 |
| Server-Components | 014-ServerComponents | 本文的并列主题 |
| Hooks原理 | 015-HooksPrinciple | 本文的原理深化 |
| 自定义Hooks设计模式 | 016-CustomHooksDesignPattern | 本文的并列主题 |
| 状态管理方案对比 | 017-StateManagementSolutionComparison | 本文的并列主题 |
| React性能优化 | 018-ReactPerformance | 本文的性能延伸 |
| React错误边界 | 019-ReactErrorBoundary | 本文的并列主题 |
| React表单处理 | 020-ReactForm | 本文的并列主题 |
| React与TypeScript | 021-ReactTypeScript | 本文的并列主题 |
| React测试 | 022-ReactTest | 本文的并列主题 |
| React路由进阶 | 023-ReactRouteAdvanced | 本文的并列主题 |
| React国际化 | 024-ReactI18n | 本文的并列主题 |
| React动画 | 025-ReactAnimation | 本文的并列主题 |
| React服务端渲染 | 026-ReactSSR | 本文的并列主题 |
| React设计模式 | 027-ReactDesignPattern | 本文的并列主题 |
| React与WebAssembly | 028-ReactWebAssembly | 本文的并列主题 |
| React与WebSocket | 029-ReactWebSocket | 本文的并列主题 |
| React与GraphQL | 030-ReactGraphQL | 本文的并列主题 |
| React与微前端 | 031-ReactMicroFrontend | 本文的并列主题 |
| React无障碍 | 032-ReactAccessibility | 本文的并列主题 |
| React与PWA | 033-ReactPWA | 本文的并列主题 |
| React与Canvas | 034-ReactCanvas | 本文的并列主题 |
| React与D3 | 035-ReactD3 | 本文的并列主题 |
| React与Storybook | 036-ReactStorybook | 本文的并列主题 |
| React与CI-CD | 037-ReactCICD | 本文的并列主题 |
| React与Monorepo | 038-ReactMonorepo | 本文的并列主题 |
| React-Compiler自动记忆化 | 039-ReactCompilerAutoMemoization | 本文的并列主题 |
| Server-Components与Client-Components | 040-ServerClientComponents | 本文的并列主题 |
| Next.js-App-Router | 041-NextJsAppRouter | 本文自身 |
| React-19新增API | 042-React19NewAPI | 本文的并列主题 |
| 并发渲染与可中断更新 | 043-ConcurrentRenderInterruptible | 本文的并列主题 |
| 错误边界与Sentry集成 | 044-ErrorBoundarySentry | 本文的并列主题 |
| 自定义Hooks复用逻辑 | 045-CustomHooksReuseLogic | 本文的并列主题 |
| React Vite 与工具链命令 | 046-ReactViteToolchainCommand | 本文的并列主题 |
