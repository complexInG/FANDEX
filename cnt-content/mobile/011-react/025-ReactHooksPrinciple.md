# React Hooks 原理与闭包陷阱

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Hooks 链表存储

**基本写法：组件对应 Fiber 的 memoizedState**
`<fiber>.memoizedState = <hook链表>`
```tsx
// 每次渲染按顺序构建链表
fiber.memoizedState = hook1;
hook1.next = hook2;
```

---

**基本写法：Hook 对象结构**
`type <Hook> = { memoizedState, baseState, baseQueue, queue, next }`
```tsx
// Hook 节点字段
{
  memoizedState: 0,
  queue: { pending: null },
  next: nextHook
}
```

---

## Hook 调用顺序约束

**基本写法：必须保证每次渲染调用顺序一致**
`use<A>(); use<B>();`
```tsx
// 顺序错乱会导致状态错位
function App() {
  const [a] = useState(0);
  const [b] = useState(0);
}
```

---

**基本写法：禁止在条件分支中调用**
`if (<条件>) useState(); // 错误`
```tsx
// 正确做法条件放在 hook 之后
const [v, setV] = useState(0);
if (cond) setV(1);
```

---

## mount 与 update 两套实现

**基本写法：首次挂载走 mount 队列**
`const <dispatch> = mountState(<初值>)`
```tsx
// 初次创建 hook 并初始化
const [state, dispatch] = mountState(initial);
```

---

**基本写法：更新走 update 队列**
`const <dispatch> = updateState()`
```tsx
// 复用已有 hook 处理更新
const [state, dispatch] = updateState();
```

---

## useState 实现

**基本写法：dispatchAction 创建 update**
`function <dispatchAction>(<hook>, <action>) { <update>.next = <update>; }`
```tsx
// 环形链表追加 update
const update = { action };
update.next = update;
hook.queue.pending = update;
```

---

**基本写法：render 时遍历 queue 计算新状态**
`while (<update> !== <first>) { <state> = <reducer>(<state>, <update>.action); }`
```tsx
// 逐一应用 action 得到最新 state
let newState = state;
while (update) {
  newState = reducer(newState, update.action);
  update = update.next;
}
```

---

## useReducer 实现

**基本写法：与 useState 类似但用 reducer**
`const [state, dispatch] = mountReducer(<reducer>, <初值>)`
```tsx
// dispatch 调用 reducer 计算新状态
dispatch({ type: 'INC' });
```

---

## useEffect 实现

**基本写法：effect 对象挂在 updateQueue**
`<hook>.updateQueue.lastEffect = <effect>`
```tsx
// effect 形成环形链表
effect.next = effect;
hook.updateQueue.lastEffect = effect;
```

---

**基本写法：effect 包含 create 与 destroy**
`type <Effect> = { tag, create, destroy, deps, next }`
```tsx
// create 是副作用函数 destroy 是清理函数
{
  create: () => subscribe(),
  destroy: () => unsubscribe(),
  deps: [id]
}
```

---

## deps 依赖比较

**基本写法：浅比较决定是否执行 effect**
`if (!<shallowEqual>(<prevDeps>, <nextDeps>)) <执行>`
```tsx
// Object.is 逐项比较
const areEqual = prevDeps.every((d, i) => Object.is(d, nextDeps[i]));
```

---

## useRef 实现

**基本写法：ref 对象首次创建后保持引用**
`const <ref> = { current: <初值> }`
```tsx
// ref 直接存入 memoizedState 不参与更新
hook.memoizedState = { current: initial };
```

---

## useMemo useCallback 实现

**基本写法：依赖不变返回缓存值**
`if (<depsChanged>) <重新计算> else <返回缓存>`
```tsx
// 缓存结果与依赖
if (depsChanged) {
  hook.memoizedState = [factory(), deps];
}
return hook.memoizedState[0];
```

---

## 闭包陷阱成因

**基本写法：effect 捕获旧值导致 stale closure**
`useEffect(() => <使用旧值>, [])`
```tsx
// 空依赖导致捕获首次渲染的 count
const [count] = useState(0);
useEffect(() => {
  const id = setInterval(() => console.log(count), 1000);
  return () => clearInterval(id);
}, []);
```

---

## 闭包陷阱解决依赖

**基本写法：补全依赖项**
`useEffect(() => <逻辑>, [<依赖>])`
```tsx
// 加入 count 让每次更新重建 effect
useEffect(() => {
  const id = setInterval(() => console.log(count), 1000);
  return () => clearInterval(id);
}, [count]);
```

---

## 使用 ref 规避闭包

**基本写法：ref.current 始终是最新值**
`const <latest> = useRef(<值>); <latest>.current = <值>;`
```tsx
// 通过 ref 读取最新 count
const countRef = useRef(count);
countRef.current = count;
useEffect(() => {
  const id = setInterval(() => console.log(countRef.current), 1000);
  return () => clearInterval(id);
}, []);
```

---

## useEffectEvent 规避闭包

**基本写法：使用实验性 useEffectEvent 抽离非响应式逻辑**
`const <fn> = useEffectEvent(<回调>)`
```tsx
// 内部访问最新 props 不进依赖
const onTick = useEffectEvent(() => console.log(count));
useEffect(() => {
  const id = setInterval(onTick, 1000);
  return () => clearInterval(id);
}, []);
```

---

## useReducer 解决闭包

**基本写法：dispatch 引用稳定不捕获旧值**
`dispatch({ type: 'INC' })`
```tsx
// dispatch 永远是最新的不进依赖
useEffect(() => {
  const id = setInterval(() => dispatch({ type: 'INC' }), 1000);
  return () => clearInterval(id);
}, [dispatch]);
```

---

## setState 函数式更新

**基本写法：使用函数式更新读取最新 state**
`setCount(c => c + 1)`
```tsx
// 避免依赖外部 count
setInterval(() => setCount(c => c + 1), 1000);
```

---

## Hook 规则 ESLint 校验

**基本写法：eslint-plugin-react-hooks 强制规则**
`npm i -D eslint-plugin-react-hooks`
```bash
# 安装后自动检测违反规则的写法
npm install --save-dev eslint-plugin-react-hooks
```

---

## 自定义 Hook 闭包

**基本写法：自定义 Hook 也要注意依赖**
`function use<名称>(<值>) { useEffect(() => <用值>, [<值>]); }`
```tsx
// 内部依赖必须完整
function useTimer(cb) {
  useEffect(() => {
    const id = setInterval(cb, 1000);
    return () => clearInterval(id);
  }, [cb]);
}
```

---

## useState 惰性初始化

**基本写法：传入函数仅首次调用**
`useState(() => <昂贵计算>)`
```tsx
// 避免每次渲染重复计算
const [data] = useState(() => heavyCompute());
```

---

## bailout 优化

**基本写法：props 与 state 未变跳过渲染**
`if (<oldProps> === <newProps>) bailout`
```tsx
// 浅比较决定是否跳过子树处理
if (Object.is(prevProps, nextProps)) return bailout;
```

---

## 并发模式下 Hook 行为

**基本写法：transition 内 setState 走低优先级 lane**
`startTransition(() => <setState>)`
```tsx
// 标记为非紧急更新
startTransition(() => setList(bigData));
```

---

## 严格模式双重渲染

**基本写法：开发环境两次渲染检测副作用**
`<React.StrictMode> <App/> </React.StrictMode>`
```tsx
// 帮助发现不纯函数副作用
<React.StrictMode><App /></React.StrictMode>
```

---

## Hook 与 Fiber 关系

**基本写法：每次渲染重建 hook 链表**
`<render> -> <遍历hook链表> -> <执行hook函数>`
```tsx
// 通过 current.memoizedState 复用上次状态
renderHooks(fiber);
```
