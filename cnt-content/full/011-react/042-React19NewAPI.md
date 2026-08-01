---
order: 103
title: 'React-19新增API'
module: react
category: 'dev-lang'
difficulty: advanced
description: 'React 19新增API详解：use、ref as prop、文档元数据、Actions。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'react/Server-Components与Client-Components'
  - react/Next.js应用路由
  - react/并发渲染与可中断更新
  - react/错误边界与Sentry集成
prerequisites:
  - react/概述与环境配置
---

# React 19 新 Hooks 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. use() API

```jsx
import { use } from 'react';

function UserProfile({ userPromise }) {
  const user = use(userPromise); // 读取 Promise/Context
  return <h1>{user.name}</h1>;
}
```

`use()` 可以在条件语句中调用（打破 Hook 规则），但仅限 Promise 和 Context。

## 2. ref as prop

```jsx
// React 19: ref 作为普通 prop
function Input({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// 不再需要 forwardRef
```

## 3. 文档元数据

```jsx
function BlogPost() {
  return (
    <>
      <title>文章标题</title>
      <meta name="description" content="文章描述" />
      <article>内容</article>
    </>
  );
}
```

React 自动将 `<title>` 和 `<meta>` 提升到 `<head>` 中。

## 4. Actions

```jsx
import { useActionState } from 'react';

async function submitForm(formData) {
  const response = await fetch('/api/submit', {
    method: 'POST',
    body: formData,
  });
  return response.json();
}

function Form() {
  const [state, submitAction, isPending] = useActionState(submitForm, null);

  return (
    <form action={submitAction}>
      <input name="title" />
      <button type="submit" disabled={isPending}>
        {isPending ? '提交中...' : '提交'}
      </button>
    </form>
  );
}
```

## 5. useOptimistic

```jsx
import { useOptimistic } from 'react';

function TodoList({ todos }) {
  const [optimisticTodos, addOptimistic] = useOptimistic(todos, (state, newTodo) => [
    ...state,
    { ...newTodo, pending: true },
  ]);

  async function addTodo(title) {
    addOptimistic({ id: Date.now(), title });
    await saveTodo(title);
  }

  return (
    <ul>
      {optimisticTodos.map((todo) => (
        <li key={todo.id} style={{ opacity: todo.pending ? 0.5 : 1 }}>
          {todo.title}
        </li>
      ))}
    </ul>
  );
}
```

## 6. useFormStatus

```jsx
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? '提交中...' : '提交'}</button>;
}
```
## useActionState 异步表单状态

**useActionState**
`const [<state>, <action>, [<isPending>]] = useActionState(<action>, <initialState>, [<permalink>]);`
```tsx
import { useActionState } from 'react';

async function increment(prev: number, formData: FormData) {
  return prev + Number(formData.get('step'));
}

function Counter() {
  const [count, action] = useActionState(increment, 0);
  return (
    <form action={action}>
      <input type="number" name="step" />
      <button>+</button>
      <span>{count}</span>
    </form>
  );
}
```

**带 pending 状态**
```tsx
const [state, action, isPending] = useActionState(submitAction, null);
```

---

## useFormStatus 表单提交状态

**useFormStatus**
`const { pending, data, method, action } = useFormStatus();`
```tsx
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? '提交中...' : '提交'}
    </button>
  );
}
```

**完整字段**
```tsx
function DebugForm() {
  const { pending, data, method, action } = useFormStatus();
  // pending: boolean      是否提交中
  // data: FormData | null  表单数据
  // method: string        'post' | 'get'
  // action: Function      提交动作
  return <button disabled={pending}>Save</button>;
}
```

---

## useOptimistic 乐观更新

**useOptimistic**
`const [<optimisticState>, <addOptimistic>] = useOptimistic(<state>, <reducer>);`
```tsx
import { useOptimistic } from 'react';

function ThumbsUp({ likes }: { likes: number }) {
  const [optimisticLikes, addOptimistic] = useOptimistic(
    likes,
    (state, delta: number) => state + delta
  );

  const onClick = async () => {
    addOptimistic(1);
    await fetch('/api/like', { method: 'POST' });
  };

  return <button onClick={onClick}>{optimisticLikes}</button>;
}
```

**乐观消息列表**
```tsx
const [messages, addMessage] = useOptimistic(
  realMessages,
  (state, newMsg: Message) => [...state, { ...newMsg, status: 'pending' }]
);

async function send(text: string) {
  addMessage({ id: Date.now(), text });
  await api.post(text);
}
```

---

## use 读取资源

**use(promise)**
`const <value> = use(<promise>);`
```tsx
import { use } from 'react';

function User({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise);
  return <h1>{user.name}</h1>;
}
```

**use(context)**
`const <value> = use(<Context>);`
```tsx
import { use } from 'react';

function Header() {
  const theme = use(ThemeContext);
  return <header className={theme}>...</header>;
}
```

**use 在条件中**
```tsx
function Comments({ show, commentsPromise }: Props) {
  if (show) {
    const comments = use(commentsPromise);
    return <List comments={comments} />;
  }
  return null;
}
```

---

## ref 作为 props

**ref 直接传递**
`<Component ref={<ref>} />`
```tsx
function Input({ ref }: { ref: React.Ref<HTMLInputElement> }) {
  return <input ref={ref} />;
}

const ref = useRef<HTMLInputElement>(null);
<Input ref={ref} />;
```

---

## forwardRef 兼容签名

**forwardRef 类型签名变化**
`const <Component> = forwardRef<<T>, <Props>>((<props>, <ref>) => <JSX.Element>);`
```tsx
const Input = forwardRef<HTMLInputElement, Props>(
  ({ placeholder }, ref) => <input ref={ref} placeholder={placeholder} />
);
```

---

## ref 回调清理函数

**ref 回调返回清理函数**
`ref={(<el>) => { return () => <cleanup>; }}`
```tsx
<div ref={(el) => {
  if (el) observe(el);
  return () => unobserve(el);
}} />
```

---

## Document Metadata

**原生 metadata 标签**
`<title>` / `<meta>` / `<link>`
```tsx
function Page() {
  return (
    <>
      <title>用户中心</title>
      <meta name="description" content="用户信息管理" />
      <link rel="canonical" href="/users" />
    </>
  );
}
```

---

## 资源加载 API

**preload 预加载**
`preload(<href>, <options>);`
```tsx
import { preload } from 'react-dom';
preload('/fonts/inter.woff2', { as: 'font' });
```

**preinit 预初始化**
`preinit(<href>, <options>);`
```tsx
import { preinit } from 'react-dom';
preinit('/css/style.css', { as: 'style' });
```

**preconnect 预连接**
`preconnect(<href>, <options>);`
```tsx
import { preconnect } from 'react-dom';
preconnect('https://cdn.example.com');
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

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 渲染原理与协调

React 渲染分阶段：render（构建元素树）、reconcile（diff）、commit（DOM 变更与副作用）。
diff 算法基于类型与 key：同类型复用实例，不同类型重建；列表 diff 按 key 匹配。
并发特性：useTransition 标记低优先级更新可中断；Suspense 等待异步边界。
React Compiler 自动记忆组件，减少手工 useMemo。

### 13.2 状态架构模式

状态分类：服务端状态（缓存数据）与客户端状态（UI 偏好）；分开管理。
TanStack Query：查询键（queryKey）+ 缓存生命周期（staleTime/gcTime）+ 失效策略。
Zustand：create 定义 store，selector 订阅切片，避免多余渲染。
表单状态：受控 + 校验库（React Hook Form + Zod）。

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
| Next.js-App-Router | 041-NextJsAppRouter | 本文的并列主题 |
| React-19新增API | 042-React19NewAPI | 本文自身 |
| 并发渲染与可中断更新 | 043-ConcurrentRenderInterruptible | 本文的并列主题 |
| 错误边界与Sentry集成 | 044-ErrorBoundarySentry | 本文的并列主题 |
| 自定义Hooks复用逻辑 | 045-CustomHooksReuseLogic | 本文的并列主题 |
| React Vite 与工具链命令 | 046-ReactViteToolchainCommand | 本文的并列主题 |
