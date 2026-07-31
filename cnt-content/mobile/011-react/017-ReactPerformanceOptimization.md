# React 性能优化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## React.memo 组件记忆化

**基本写法：对函数组件进行浅比较记忆化**
`const <组件> = React.memo(<组件> [, <对比函数>])`
```tsx
// 仅当 props 变化时才重新渲染
const UserCard = React.memo(function UserCard({ name, age }) {
  return <div>{name} - {age}</div>;
});
```

---

**基本写法：自定义对比函数**
`React.memo(<组件>, (<prevProps>, <nextProps>) => <是否相等>)`
```tsx
// 返回 true 表示跳过渲染
const Item = React.memo(ItemBase, (prev, next) => prev.id === next.id);
```

---

## useMemo 缓存计算结果

**基本写法：缓存昂贵计算的结果**
`const <值> = useMemo(() => <计算>, [<依赖>])`
```tsx
// 仅当 deps 变化时重新计算
const sorted = useMemo(() => list.sort(), [list]);
```

---

**基本写法：缓存对象引用**
`const <对象> = useMemo(() => ({ <字段> }), [<依赖>])`
```tsx
// 避免每次渲染生成新对象引用
const style = useMemo(() => ({ color: 'red' }), []);
```

---

## useCallback 缓存函数引用

**基本写法：缓存函数实例避免子组件重渲染**
`const <函数> = useCallback((<参数>) => <逻辑>, [<依赖>])`
```tsx
// 配合 React.memo 子组件使用
const handleClick = useCallback(() => doAction(id), [id]);
```

---

## lazy 与 Suspense 延迟加载

**基本写法：动态导入组件**
`const <组件> = lazy(() => import(<路径>))`
```tsx
// 按需加载路由级组件
const Detail = lazy(() => import('./Detail'));
```

---

**基本写法：配合 Suspense 显示降级 UI**
`<Suspense fallback={<占位>}> <组件 /> </Suspense>`
```tsx
// 加载期间显示 fallback
<Suspense fallback={<Spinner />}>
  <Detail />
</Suspense>
```

---

**基本写法：嵌套 Suspense 边界**
`<Suspense fallback={<外层占位>}> <<父组件> /> </Suspense>`
```tsx
// 子组件独立Suspense避免整页阻塞
<Suspense fallback={<PageSkeleton />}>
  <Header />
  <Suspense fallback={<ListSkeleton />}>
    <List />
  </Suspense>
</Suspense>
```

---

## 列表虚拟化

**基本写法：长列表只渲染可见项**
`<虚拟列表 <数据>={数据} />`
```tsx
// 使用 react-window 减少 DOM 节点数量
import { FixedSizeList } from 'react-window';
<FixedSizeList height={600} itemCount={10000} itemSize={40} width={400}>
  {({ index, style }) => <div style={style}>行 {index}</div>}
</FixedSizeList>
```

---

## key 优化列表渲染

**基本写法：为列表项提供稳定唯一 key**
`<列表项 key={<唯一标识>} />`
```tsx
// 使用业务 id 而非数组索引
{todos.map(t => <TodoItem key={t.id} todo={t} />)}
```

---

## 状态拆分降低渲染范围

**基本写法：将高频更新状态隔离到独立子组件**
`function <子组件>() { const [<状态>, <设置>] = useState(<初值>); }`
```tsx
// 输入框高频更新不触发父组件渲染
function SearchInput() {
  const [text, setText] = useState('');
  return <input value={text} onChange={e => setText(e.target.value)} />;
}
```

---

## useDeferredValue 延迟更新

**基本写法：将非紧急更新标记为可延迟**
`const <延迟值> = useDeferredValue(<值>)`
```tsx
// 搜索结果可延迟，输入框保持流畅
const deferredQuery = useDeferredValue(query);
const results = useMemo(() => filter(deferredQuery), [deferredQuery]);
```

---

## 批量更新 Automatic Batching

**基本写法：同一事件中多次 setState 自动合并**
`<设置1>(<值1>); <设置2>(<值2>);`
```tsx
// React 18+ 自动批量合并为一次渲染
function handleClick() {
  setCount(c => c + 1);
  setFlag(f => !f);
}
```

---

**基本写法：flushSync 强制同步刷新**
`flushSync(() => { <更新> })`
```tsx
// 需要立即反映 DOM 时使用
import { flushSync } from 'react-dom';
flushSync(() => setScrollTop(0));
```

---

## Profiler 性能分析

**基本写法：测量组件渲染耗时**
`<Profiler id={<标识>} onRender={<回调>}> <子组件 /> </Profiler>`
```tsx
// 收集渲染阶段与耗时
<Profiler id="App" onRender={(id, phase, actualTime) => console.log(id, phase, actualTime)}>
  <App />
</Profiler>
```

---

## 图片与资源懒加载

**基本写法：图片原生懒加载**
`<img src={<路径>} loading="lazy" />`
```tsx
// 视口进入时再加载图片
<img src="/a.jpg" loading="lazy" alt="封面" />
```

---

## 代码分割按路由

**基本写法：路由配置级懒加载**
`const <页面> = lazy(() => import(<页面路径>))`
```tsx
// 每个路由独立 chunk
const Home = lazy(() => import('./pages/Home'));
const User = lazy(() => import('./pages/User'));
```

---

## Context 渲染优化

**基本写法：拆分 Context 避免无关消费者更新**
`const <静态Context> = createContext(<静态值>); const <动态Context> = createContext(<动态值>);`
```tsx
// 静态与高频更新状态分离
const ThemeContext = createContext('light');
const UserContext = createContext(null);
```

---

## ref 读取而非订阅

**基本写法：频繁变化的值不进 state**
`const <ref> = useRef(<初值>); <ref>.current = <新值>;`
```tsx
// 不触发渲染的容器
const timerRef = useRef(null);
timerRef.current = setInterval(tick, 1000);
```

---

## 使用 Production 构建

**基本写法：生产环境去除开发警告**
`npm run build`
```bash
# 生产构建自动启用优化
npm run build
```

---

## Strict Mode 排查副作用

**基本写法：开发期双重渲染检测副作用**
`<React.StrictMode> <根组件 /> </React.StrictMode>`
```tsx
// 开发环境帮助发现不纯渲染
<React.StrictMode>
  <App />
</React.StrictMode>
```

---

## Web Worker 卸载计算

**基本写法：将繁重任务交给 Worker**
`const <worker> = new Worker(new URL(<脚本>, import.meta.url))`
```tsx
// 主线程保持响应
const worker = new Worker(new URL('./heavy.js', import.meta.url));
worker.postMessage(data);
```

---

## useSyncExternalStore 订阅外部源

**基本写法：安全订阅外部 store**
`const <值> = useSyncExternalStore(<订阅>, <快照>, [<服务端快照>])`
```tsx
// 避免 tearing 撕裂问题
const width = useSyncExternalStore(subscribeResize, () => window.innerWidth);
```

---

## 避免内联对象与函数

**基本写法：将常量对象提到组件外**
`const <常量对象> = { <字段> };`
```tsx
// 防止每次渲染新建对象破坏 memo
const HEADER_STYLE = { padding: 8 };
function Header() { return <div style={HEADER_STYLE} />; }
```

---

## useTransition 降低更新优先级

**基本写法：将昂贵更新标记为过渡**
`const [<isPending>, <startTransition>] = useTransition()`
```tsx
// 切换标签页时保持交互响应
const [isPending, startTransition] = useTransition();
startTransition(() => setTab(target));
```

---

## 虚拟化表格优化

**基本写法：表格按行虚拟化**
`<FixedSizeList <数据>={行} itemSize={<行高>} >`
```tsx
// 万行数据表格仍流畅
<FixedSizeList height={500} itemCount={rows.length} itemSize={36} width="100%">
  {({ index, style, data }) => <Row style={style} data={data[index]} />}
</FixedSizeList>
```

---

## tree shaking 减小体积

**基本写法：按命名导入而非整体引入**
`import { <命名> } from <库>`
```tsx
// 仅打包使用到的工具函数
import { debounce } from 'lodash-es';
```

---

## 预加载关键资源

**基本写法：在入口注入资源预取**
`<link rel="preload" href=<资源> as=<类型> />`
```tsx
// 关键字体提前加载
<link rel="preload" href="/fonts.woff2" as="font" type="font/woff2" crossOrigin />
```
