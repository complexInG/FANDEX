# React 并发特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## useTransition 过渡更新

**基本写法：将状态更新标记为低优先级**
`const [<isPending>, <startTransition>] = useTransition()`
```tsx
// 切换标签页保持输入框响应
const [isPending, startTransition] = useTransition();
function changeTab(next) {
  startTransition(() => setTab(next));
}
```

---

**基本写法：展示过渡中状态**
`{<isPending> && <占位>}`
```tsx
// 显示加载指示
{isPending ? <Spinner /> : <Content />}
```

---

**基本写法：异步 Action**
`startTransition(async () => { <异步逻辑> })`
```tsx
// React 19 支持异步过渡
startTransition(async () => {
  const data = await fetchData();
  setResult(data);
});
```

---

## startTransition 全局函数

**基本写法：在组件外标记过渡更新**
`startTransition(() => <更新>)`
```tsx
// 从非组件代码触发过渡
import { startTransition } from 'react';
startTransition(() => store.setFilter('active'));
```

---

## useDeferredValue 延迟值

**基本写法：延迟非紧急值的更新**
`const <延迟值> = useDeferredValue(<值>)`
```tsx
// 搜索框输入即时响应结果延迟
const deferredQuery = useDeferredValue(query);
const results = useMemo(() => search(deferredQuery), [deferredQuery]);
```

---

**基本写法：检测是否处于滞后状态**
`const <是否滞后> = <值> !== <延迟值>`
```tsx
// 显示旧数据淡化效果
const isStale = query !== deferredQuery;
<div style={{ opacity: isStale ? 0.7 : 1 }}>{results}</div>
```

---

## Suspense 数据等待

**基本写法：包裹异步组件显示降级**
`<Suspense fallback={<占位>}> <异步组件 /> </Suspense>`
```tsx
// 数据未就绪时显示骨架
<Suspense fallback={<Skeleton />}>
  <Profile userId={id} />
</Suspense>
```

---

**基本写法：嵌套 Suspense 边界**
`<Suspense fallback={<外层>}> <Suspense fallback={<内层>}> <组件/> </Suspense> </Suspense>`
```tsx
// 不同区域独立 loading
<Suspense fallback={<PageFallback />}>
  <Header />
  <Suspense fallback={<ListFallback />}>
    <List />
  </Suspense>
</Suspense>
```

---

## Suspense 配合 lazy

**基本写法：路由级代码分割**
`const <组件> = lazy(() => import(<路径>))`
```tsx
// 按需加载并显示 fallback
const Settings = lazy(() => import('./Settings'));
<Suspense fallback={<Spinner />}><Settings /></Suspense>
```

---

## 并发更新优先级

**基本写法：紧急更新直接 setState**
`<设置>(<值>)`
```tsx
// 输入框立即响应属于高优先级
setInput(e.target.value);
```

---

**基本写法：非紧急更新放入 transition**
`startTransition(() => <设置>(<值>))`
```tsx
// 搜索结果可延迟
startTransition(() => setResults(filtered));
```

---

## 避免不必要的 loading

**基本写法：使用 useTransition 避免跳到 fallback**
`startTransition(() => <切换>)`
```tsx
// 切换 tab 时保留当前内容直到新内容就绪
startTransition(() => setTab(next));
```

---

## 并发渲染可中断

**基本写法：渲染过程可被打断让位高优先级**
`startTransition(() => <更新>)`
```tsx
// 用户输入打断后台渲染
function onType(v) {
  setInput(v); // 紧急
  startTransition(() => setMatches(filter(v))); // 可中断
}
```

---

## useSyncExternalStore 订阅外部

**基本写法：安全订阅外部 store 避免 tearing**
`const <快照> = useSyncExternalStore(<订阅>, <取值>, [<服务端取值>])`
```tsx
// 订阅 window 尺寸
const width = useSyncExternalStore(
  cb => window.addEventListener('resize', cb),
  () => window.innerWidth
);
```

---

**基本写法：提供 getServerSnapshot 支持 SSR**
`useSyncExternalStore(<订阅>, <取值>, <服务端取值>)`
```tsx
// 服务端返回默认值
const theme = useSyncExternalStore(subscribe, getSnapshot, () => 'light');
```

---

## 自动批处理

**基本写法：同一事件多次更新合并**
`<设置1>(<值1>); <设置2>(<值2>);`
```tsx
// React 18+ 自动合并为一次渲染
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
}
```

---

**基本写法：异步代码也自动批处理**
`await <异步>; <设置>(<值>);`
```tsx
// Promise 内的更新也会合并
async function load() {
  const data = await fetch();
  setList(data);
  setLoading(false);
}
```

---

## flushSync 强制同步

**基本写法：跳过批处理立即刷新**
`flushSync(() => <更新>)`
```tsx
// 需要立即读取 DOM 时使用
import { flushSync } from 'react-dom';
flushSync(() => setScroll(0));
window.scrollTo(0, 0);
```

---

## selectNode 调度提示

**基本写法：useDeferredValue 实现非阻塞渲染**
`const <延迟> = useDeferredValue(<值>)`
```tsx
// 大列表过滤不阻塞输入
const deferred = useDeferredValue(text);
const items = useMemo(() => heavyFilter(deferred), [deferred]);
```

---

## Offscreen 隐藏组件

**基本写法：保留组件状态但隐藏显示**
`<Offscreen mode="hidden"> <组件 /> </Offscreen>`
```tsx
// 切换标签保留滚动位置（实验性）
<Offscreen mode={visible ? 'visible' : 'hidden'}>
  <ExpensiveList />
</Offscreen>
```

---

## useOptimistic 乐观更新

**基本写法：在请求期间乐观展示结果**
`const [<乐观值>, <添加>] = useOptimistic(<状态>, <更新函数>)`
```tsx
// 立即显示新消息
const [messages, addOptimistic] = useOptimistic(messages, (state, newMsg) => [...state, newMsg]);
```

---

## Suspense List 协调多个 Suspense

**基本写法：控制多个 Suspense 揭示顺序**
`<SuspenseList revealOrder="forwards"> <Suspense>...</Suspense> </SuspenseList>`
```tsx
// 按顺序揭示内容（实验性 API）
<SuspenseList revealOrder="forwards">
  <Suspense fallback={<S1 />}><A /></Suspense>
  <Suspense fallback={<S2 />}><B /></Suspense>
</SuspenseList>
```

---

## React 19 Actions

**基本写法：在 startTransition 中执行异步函数即 Action**
`startTransition(async () => <异步>)`
```tsx
// Actions 自动管理 pending 与错误
const [isPending, startTransition] = useTransition();
startTransition(async () => await submitForm(data));
```

---

## 并发模式注意事项

**基本写法：transition 内不可包含读取状态副作用**
`startTransition(() => { <设置>; })`
```tsx
// 仅做状态更新不读取
startTransition(() => setTab(next));
```

---

## transition 与 Suspense 配合

**基本写法：transition 内挂起会显示当前 UI 而非 fallback**
`startTransition(() => <切换挂起组件>)`
```tsx
// 切换路由不闪烁 loading
startTransition(() => setRoute('/detail'));
```

---

## 性能权衡

**基本写法：仅对昂贵非紧急更新使用 transition**
`startTransition(() => <昂贵更新>)`
```tsx
// 简单更新无需 transition 开销
setCount(c => c + 1);
```
