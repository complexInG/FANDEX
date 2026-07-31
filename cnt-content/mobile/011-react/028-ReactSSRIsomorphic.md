# React SSR 与同构渲染

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SSR 基本流程

**基本写法：renderToString 渲染为字符串**
`const <html> = renderToString(<App />)`
```tsx
// 服务器端将组件渲染为 HTML
import { renderToString } from 'react-dom/server';
const html = renderToString(<App />);
```

---

**基本写法：hydrateRoot 客户端注水**
`hydrateRoot(<容器>, <App>)`
```tsx
// 复用服务端 HTML 并附加事件
import { hydrateRoot } from 'react-dom/client';
hydrateRoot(document.getElementById('root'), <App />);
```

---

## renderToPipeableStream 流式渲染

**基本写法：Node 流式输出**
`const <stream> = renderToPipeableStream(<App>)`
```tsx
// 边渲染边发送提升首屏
import { renderToPipeableStream } from 'react-dom/server';
const { pipe } = renderToPipeableStream(<App />, {
  onShellReady() { pipe(res); }
});
```

---

**基本写法：Web Streams 边缘环境**
`renderToReadableStream(<App>)`
```tsx
// Cloudflare Workers 等环境使用
import { renderToReadableStream } from 'react-dom/server';
const stream = await renderToReadableStream(<App />);
```

---

## Suspense 服务端流式

**基本写法：Suspense 配合流式 SSR**
`<Suspense fallback={<占位>}> <异步组件> </Suspense>`
```tsx
// 数据未就绪先发送 fallback
<Suspense fallback={<Spinner />}>
  <Comments />
</Suspense>
```

---

## 同构路由

**基本写法：客户端与服务器共用路由配置**
`const <routes> = [<路由对象>]`
```tsx
// 共享路由配置
const routes = [
  { path: '/', element: <Home /> },
  { path: '/user', element: <User /> }
];
```

---

## 数据预取

**基本写法：renderToPipeableStream 前获取数据**
`await <fetchAllData>(<匹配路由>)`
```tsx
// 进入渲染前完成数据请求
const data = await fetchInitialData(url);
renderToPipeableStream(<App initialData={data} />);
```

---

## 注水不匹配 Hydration Mismatch

**基本写法：避免服务端与客户端渲染差异**
`const <date> = new Date() // 服务端客户端不一致`
```tsx
// 使用 useEffect 在客户端修正
const [val, setVal] = useState(serverValue);
useEffect(() => setVal(clientValue), []);
```

---

## 选择性注水 Selective Hydration

**基本写法：用户交互优先注水**
`<Suspense> <懒加载组件> </Suspense>`
```tsx
// 点击某区域优先注水其他区域保持挂起
<Suspense fallback={<Fallback />}>
  <LazyComponent />
</Suspense>
```

---

## 静态站点生成 SSG

**基本写法：构建时预渲染**
`renderToStaticMarkup(<App />)`
```tsx
// 生成纯静态 HTML
import { renderToStaticMarkup } from 'react-dom/server';
fs.writeFileSync('index.html', renderToStaticMarkup(<App />));
```

---

## 服务器组件 Server Components

**基本写法：组件默认服务端执行**
`export default function <ServerComponent>() { }`
```tsx
// 仅在服务端运行不发送到客户端
export default async function Posts() {
  const posts = await db.query();
  return <List items={posts} />;
}
```

---

**基本写法：'use client' 标记客户端组件**
`'use client'`
```tsx
// 需要交互或 hooks 的组件
'use client';
import { useState } from 'react';
export default function Counter() { /* */ }
```

---

**基本写法：'use server' 标记 Server Action**
`'use server'`
```tsx
// 在服务端执行的函数
async function save() {
  'use server';
  await db.insert();
}
```

---

## Next.js App Router 同构

**基本写法：app 目录默认服务端组件**
`app/page.tsx`
```tsx
// 文件即路由默认 SSR
export default async function Page() {
  const data = await fetch('https://api');
  return <div>{data.json()}</div>;
}
```

---

**基本写法：动态路由参数**
`app/post/[id]/page.tsx`
```tsx
// 路径参数注入 props
export default function Post({ params }) {
  return <h1>{params.id}</h1>;
}
```

---

## 注水数据序列化

**基本写法：服务端数据通过 script 注入**
`<script dangerouslySetInnerHTML={{ __html: JSON.stringify(<data>) }} />`
```tsx
// 客户端读取初始数据
<script id="initial" type="application/json" dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }} />
```

---

## 客户端读取注水数据

**基本写法：从 script 读取数据**
`JSON.parse(document.getElementById('initial').textContent)`
```tsx
// 客户端注水时复用
const initial = JSON.parse(document.getElementById('initial').textContent);
```

---

## Express 集成

**基本写法：Express 中间件渲染**
`app.get('*', (req, res) => <渲染>)`
```tsx
// 通用中间件处理路由
app.get('*', (req, res) => {
  const html = renderToString(<App url={req.url} />);
  res.send(`<div id="root">${html}</div>`);
});
```

---

## 流式错误处理

**基本写法：onShellError 处理外壳错误**
`renderToPipeableStream(<App>, { onShellError })`
```tsx
// 外壳渲染失败时降级
const { pipe } = renderToPipeableStream(<App />, {
  onShellError(err) { res.status(500).send(err.message); }
});
```

---

## loading.tsx 流式加载

**基本写法：Next.js 文件约定**
`app/loading.tsx`
```tsx
// 自动包裹 Suspense
export default function Loading() {
  return <Spinner />;
}
```

---

## error.tsx 错误边界

**基本写法：Next.js 错误文件约定**
`app/error.tsx`
```tsx
// 路由级错误边界
'use client';
export default function Error({ error }) {
  return <h1>出错了 {error.message}</h1>;
}
```

---

## notFound.tsx 404 页面

**基本写法：未找到页面约定**
`app/not-found.tsx`
```tsx
// 路由未匹配时显示
export default function NotFound() {
  return <h1>页面不存在</h1>;
}
```

---

## metadata 文档头

**基本写法：导出 metadata 对象**
`export const <metadata> = { title, description }`
```tsx
// 服务端注入 head
export const metadata = {
  title: '首页',
  description: '站点描述'
};
```

---

## SEO 与 SSR

**基本写法：服务端渲染保证爬虫可见**
`renderToPipeableStream(<App />)`
```tsx
// 完整 HTML 输出利于 SEO
const html = await renderToPipeableStream(<App />);
```

---

## 客户端导航

**基本写法：注水后使用 Link 客户端路由**
`<Link to="<路径>">`
```tsx
// 避免整页刷新
<Link to="/about">关于</Link>
```

---

## 缓存策略

**基本写法：构建时生成 ISR**
`export const <revalidate> = <秒>`
```tsx
// Next.js 增量静态再生
export const revalidate = 60;
```
