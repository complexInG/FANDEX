# React 状态管理方案对比

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Context API 跨组件共享

**基本写法：创建与提供 Context**
`const <Ctx> = createContext(<默认值>); <Ctx.Provider value={<值>}>`
```tsx
// 全局主题共享
const ThemeContext = createContext('light');
<ThemeContext.Provider value="dark"><App /></ThemeContext.Provider>
```

---

**基本写法：消费 Context**
`const <值> = useContext(<Ctx>)`
```tsx
// 子组件读取主题
const theme = useContext(ThemeContext);
```

---

**基本写法：拆分 Context 避免 redundant 渲染**
`const <静态Ctx> = createContext(); const <动态Ctx> = createContext();`
```tsx
// 静态方法与动态状态分离
const DispatchContext = createContext(null);
const StateContext = createContext(null);
```

---

## useReducer 复杂状态

**基本写法：用 reducer 管理多字段状态**
`const [<状态>, <dispatch>] = useReducer(<reducer>, <初值>, [<init>])`
```tsx
// 购物车状态机
const [cart, dispatch] = useReducer(cartReducer, { items: [], total: 0 });
dispatch({ type: 'ADD', item });
```

---

**基本写法：惰性初始化**
`useReducer(<reducer>, <初值参数>, <init函数>)`
```tsx
// 通过 init 函数计算初始状态
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

---

## Redux Toolkit 全局状态

**基本写法：configureStore 创建 store**
`const <store> = configureStore({ reducer: <reducers> })`
```tsx
// 组合切片
const store = configureStore({
  reducer: { user: userReducer, cart: cartReducer }
});
```

---

**基本写法：createSlice 定义切片**
`const <slice> = createSlice({ name, initialState, reducers })`
```tsx
// 自动生成 action 与 reducer
const counter = createSlice({
  name: 'counter',
  initialState: 0,
  reducers: { inc: s => s + 1, dec: s => s - 1 }
});
```

---

**基本写法：useSelector 订阅状态**
`const <值> = useSelector(<选择器>)`
```tsx
// 订阅 counter 切片
const count = useSelector(s => s.counter);
```

---

**基本写法：useDispatch 派发 action**
`const <dispatch> = useDispatch(); <dispatch>(<action>)`
```tsx
// 派发 inc action
const dispatch = useDispatch();
dispatch(counter.actions.inc());
```

---

**基本写法：createAsyncThunk 异步 action**
`const <thunk> = createAsyncThunk(<类型>, <异步函数>)`
```tsx
// 异步请求封装
const fetchUser = createAsyncThunk('user/fetch', async (id) => {
  return await api.getUser(id);
});
```

---

## Zustand 轻量状态

**基本写法：create 创建 store**
`const use<Store> = create((<set>, <get>) => ({ <状态>, <方法> }))`
```tsx
// 极简全局状态
const useStore = create((set) => ({
  count: 0,
  inc: () => set(s => ({ count: s.count + 1 }))
}));
```

---

**基本写法：组件内订阅**
`const <值> = use<Store>(s => s.<字段>)`
```tsx
// 选择性订阅避免多余渲染
const count = useStore(s => s.count);
const inc = useStore(s => s.inc);
```

---

**基本写法：在组件外访问**
`use<Store>.getState().<方法>()`
```tsx
// 非组件代码调用
useStore.getState().inc();
```

---

**基本写法：持久化中间件**
`create(<fn>, { persist: { key: <键> } })`
```tsx
// 同步到 localStorage
const useStore = create(persist((set) => ({ count: 0 }), { name: 'app-store' }));
```

---

## Jotai 原子化状态

**基本写法：atom 定义原子**
`const <原子> = atom(<初值>)`
```tsx
// 最小粒度状态
const countAtom = atom(0);
```

---

**基本写法：useAtom 读写原子**
`const [<值>, <设置>] = useAtom(<原子>)`
```tsx
// 组件订阅原子
const [count, setCount] = useAtom(countAtom);
```

---

**基本写法：派生 atom**
`const <派生> = atom(<get> => <计算>)`
```tsx
// 依赖其他原子计算
const doubleAtom = atom(get => get(countAtom) * 2);
```

---

**基本写法：可写派生 atom**
`const <派生> = atom(<get>, <set>)`
```tsx
// 自定义写入逻辑
const setOnlyAtom = atom(null, (get, set, val) => set(countAtom, val));
```

---

## Recoil 原子状态

**基本写法：atom 定义**
`const <state> = atom({ key, default })`
```tsx
// 唯一 key 标识
const fontSize = atom({ key: 'fontSize', default: 14 });
```

---

**基本写法：selector 派生**
`const <派生> = selector({ key, get })`
```tsx
// 派生状态
const label = selector({ key: 'label', get: ({ get }) => `字号${get(fontSize)}` });
```

---

**基本写法：useRecoilState 读写**
`const [<值>, <设置>] = useRecoilState(<atom>)`
```tsx
// 类似 useState 用法
const [size, setSize] = useRecoilState(fontSize);
```

---

## MobX 可观察状态

**基本写法：observable 定义状态**
`class <Store> { <字段> = observable(<初值>) }`
```tsx
// 类形式 store
class Counter { count = observable.box(0); }
```

---

**基本写法：observer 包裹组件**
`const <组件> = observer(() => <JSX>)`
```tsx
// 自动响应 observable 变化
const View = observer(() => <div>{store.count.get()}</div>);
```

---

## Valtio 代理状态

**基本写法：proxy 创建代理状态**
`const <state> = proxy({ <字段>: <值> })`
```tsx
// 直接修改触发更新
const state = proxy({ count: 0 });
state.count++;
```

---

**基本写法：useSnapshot 订阅**
`const <snap> = useSnapshot(<state>)`
```tsx
// 只读快照
const snap = useSnapshot(state);
return <div>{snap.count}</div>;
```

---

## nanostores 极简方案

**基本写法：createStore 定义原子**
`export const <store> = atom(<初值>)`
```tsx
// 跨框架复用
import { atom } from 'nanostores';
export const count = atom(0);
```

---

**基本写法：useStore 订阅**
`const <值> = useStore(<store>)`
```tsx
// React 适配器
import { useStore } from '@nanostores/react';
const value = useStore(count);
```

---

## 状态管理选型对比

**基本写法：按场景选择方案**
`<方案> = { 场景: <场景>, 体积: <大小>, 学习成本: <成本> }`
```tsx
// 决策依据
Context + useReducer  // 中小型应用内共享
Redux Toolkit          // 大型团队协作
Zustand                // 轻量偏好
Jotai / Recoil         // 原子化细粒度
```

---

## 状态分层

**基本写法：本地状态用 useState**
`const [<值>, <设置>] = useState(<初值>)`
```tsx
// 表单输入等局部状态
const [text, setText] = useState('');
```

---

**基本写法：服务端状态用 React Query**
`const { <数据>, <isLoading> } = useQuery({ queryKey, queryFn })`
```tsx
// 自动缓存与重试
import { useQuery } from '@tanstack/react-query';
const { data } = useQuery({ queryKey: ['user'], queryFn: fetchUser });
```

---

**基本写法：URL 状态用路由参数**
`const [<params>] = useSearchParams()`
```tsx
// 分页筛选条件持久化到 URL
const [params] = useSearchParams();
const page = params.get('page');
```

---

## Context 性能优化

**基本写法：使用 memo 与 useCallback 稳定 Provider 值**
`const <值> = useMemo(() => ({ <字段>, <方法> }), [<依赖>])`
```tsx
// 避免 value 每次新建对象
const value = useMemo(() => ({ user, logout }), [user]);
<UserContext.Provider value={value}>
```

---

## 状态调试

**基本写法：Redux DevTools 调试**
`configureStore({ devTools: true })`
```tsx
// 默认开启开发工具
const store = configureStore({ reducer, devTools: true });
```

---

**基本写法：Zustand 临时订阅**
`use<Store>.subscribe(<回调>)`
```tsx
// 监听变化
const unsub = useStore.subscribe(state => console.log(state));
```
