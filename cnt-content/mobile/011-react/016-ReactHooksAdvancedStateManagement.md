# React Hooks 进阶与状态管理速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## useState 状态

**基本写法：基本状态**
`const [<值>, <设置函数>] = useState(<初始值>);`
```typescript
// 基础状态
import { useState } from 'react';
const [count, setCount] = useState(0);
setCount(count + 1);
```

---

**基本写法：函数式更新**
`<set函数>((<旧值>) => <新值>);`
```typescript
// 基于前值更新
setCount(prev => prev + 1);
```

---

**基本写法：对象状态**
`const [<状态>, <设置函数>] = useState({ <字段>: <值> });`
```typescript
// 对象状态
const [user, setUser] = useState({ name: '', age: 0 });
setUser(prev => ({ ...prev, name: 'Alice' }));
```

---

**基本写法：懒初始化**
`const [<值>, <setter>] = useState(() => <计算>);`
```typescript
// 惰性初始化（仅首次渲染计算）
const [data, setData] = useState(() => loadDataFromStorage());
```

---

## useEffect 副作用

**基本写法：每次渲染后执行**
`useEffect(() => { <副作用> });`
```typescript
// 无依赖，每次渲染后执行
useEffect(() => {
    console.log('rendered');
});
```

---

**基本写法：挂载时执行一次**
`useEffect(() => { <副作用> }, []);`
```typescript
// 仅挂载时执行
useEffect(() => {
    fetchData();
}, []);
```

---

**基本写法：依赖变化时执行**
`useEffect(() => { <副作用> }, [<依赖>...]);`
```typescript
// 依赖变化时执行
useEffect(() => {
    fetchUser(userId);
}, [userId]);
```

---

**基本写法：清理副作用**
`useEffect(() => { return () => <清理>; }, [<依赖>]);`
```typescript
// 清理定时器
useEffect(() => {
    const timer = setInterval(tick, 1000);
    return () => clearInterval(timer);
}, []);
```

---

## useRef 引用

**基本写法：引用 DOM**
`const <ref> = useRef(<初始值>);`
```typescript
// DOM 引用
const inputRef = useRef<HTMLInputElement>(null);
useEffect(() => {
    inputRef.current?.focus();
}, []);
```

---

**基本写法：可变值容器**
`const <ref> = useRef(<初始值>);`
```typescript
// 保存可变值（不触发重渲染）
const timerRef = useRef<number>();
timerRef.current = setInterval(tick, 1000);
```

---

## useMemo 与 useCallback

**基本写法：useMemo 缓存计算**
`const <值> = useMemo(() => <计算>, [<依赖>]);`
```typescript
// 缓存昂贵计算
const sorted = useMemo(() => {
    return [...data].sort((a, b) => a - b);
}, [data]);
```

---

**基本写法：useCallback 缓存函数**
`const <函数> = useCallback(() => { }, [<依赖>]);`
```typescript
// 缓存函数引用
const handleClick = useCallback(() => {
    setCount(c => c + 1);
}, []);
```

---

## useContext 上下文

**基本写法：创建 Context**
`const <Context> = createContext(<默认值>);`
```typescript
// 创建 Context
import { createContext } from 'react';
const ThemeContext = createContext('light');
```

---

**基本写法：Provider 提供值**
`<<Context>.Provider value={<值>}>`
```tsx
// 提供上下文值
<ThemeContext.Provider value="dark">
    <App />
</ThemeContext.Provider>
```

---

**基本写法：useContext 消费**
`const <值> = useContext(<Context>);`
```typescript
// 消费上下文
import { useContext } from 'react';
const theme = useContext(ThemeContext);
```

---

## useReducer 复杂状态

**基本写法：useReducer**
`const [<状态>, <dispatch>] = useReducer(<reducer>, <初始值>);`
```typescript
// 复杂状态管理
import { useReducer } from 'react';
type State = { count: number };
type Action = { type: 'inc' } | { type: 'dec' };
function reducer(state: State, action: Action): State {
    switch (action.type) {
        case 'inc': return { count: state.count + 1 };
        case 'dec': return { count: state.count - 1 };
    }
}
const [state, dispatch] = useReducer(reducer, { count: 0 });
dispatch({ type: 'inc' });
```

---

## 自定义 Hook

**基本写法：自定义 Hook**
`function use<名称>(<参数>) { return <值>; }`
```typescript
// 自定义 Hook
function useLocalStorage(key: string, initial: string) {
    const [value, setValue] = useState(() => localStorage.getItem(key) || initial);
    useEffect(() => {
        localStorage.setItem(key, value);
    }, [key, value]);
    return [value, setValue] as const;
}
```

---

## 状态管理库

**基本写法：Zustand 创建 Store**
`const use<Store> = create((<set>) => ({ }));`
```typescript
// Zustand Store
import { create } from 'zustand';
interface BearStore {
    bears: number;
    addBear: () => void;
}
const useBearStore = create<BearStore>((set) => ({
    bears: 0,
    addBear: () => set((s) => ({ bears: s.bears + 1 })),
}));
// 使用
const bears = useBearStore((s) => s.bears);
const addBear = useBearStore((s) => s.addBear);
```

---

**基本写法：Jotai 原子状态**
`const <atom> = atom(<初始值>);`
```typescript
// Jotai 原子
import { atom, useAtom } from 'jotai';
const countAtom = atom(0);
function Counter() {
    const [count, setCount] = useAtom(countAtom);
    return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

---

## React 19 新特性

**基本写法：useActionState 表单状态**
`const [<状态>, <action>, <是否提交中>] = useActionState(<action>, <初始>);`
```typescript
// React 19 表单
import { useActionState } from 'react';
async function submitAction(prevState: string, formData: FormData) {
    return await save(formData);
}
const [state, action, isPending] = useActionState(submitAction, '');
```

---

**基本写法：use 读取 Promise**
`const <值> = use(<Promise>);`
```typescript
// React 19 use 读取异步值
import { use } from 'react';
function Message({ messagePromise }) {
    const message = use(messagePromise);
    return <p>{message}</p>;
}
```

---

**基本写法：useOptimistic 乐观更新**
`const [<optimisticValue>, <addOptimistic>] = useOptimistic(<实际值>, <reducer>);`
```typescript
// 乐观更新
import { useOptimistic } from 'react';
const [optimisticCount, addOptimistic] = useOptimistic(
    count,
    (state, newCount) => newCount
);
```
