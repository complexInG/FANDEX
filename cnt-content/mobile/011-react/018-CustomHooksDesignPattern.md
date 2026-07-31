# React 自定义 Hooks 设计模式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 自定义 Hook 基本结构

**基本写法：以 use 开头封装状态逻辑**
`function use<名称>(<参数>) { return <结果>; }`
```tsx
// 复用计数逻辑
function useCounter(initial = 0) {
  const [count, setCount] = useState(initial);
  const inc = () => setCount(c => c + 1);
  return { count, inc };
}
```

---

## 返回值约定

**基本写法：返回对象便于扩展**
`return { <字段1>, <字段2> };`
```tsx
// 调用方按需取用
return { value, setValue, reset };
```

---

**基本写法：返回数组便于重命名**
`return [<值1>, <值2>];`
```tsx
// 类似 useState 风格
return [state, setState];
```

---

## 依赖收集规则

**基本写法：在 Hook 内调用其他 Hooks 并声明依赖**
`useEffect(() => <副作用>, [<依赖>])`
```tsx
// 依赖必须完整声明
function useLog(value) {
  useEffect(() => console.log(value), [value]);
}
```

---

## useToggle 布尔切换

**基本写法：封装布尔状态切换**
`const [<值>, <切换>] = useToggle(<初值>)`
```tsx
// 弹窗开关复用
function useToggle(initial = false) {
  const [on, setOn] = useState(initial);
  const toggle = useCallback(() => setOn(v => !v), []);
  return [on, toggle];
}
```

---

## usePrevious 获取上一帧值

**基本写法：通过 ref 保存上次渲染值**
`const <上一值> = usePrevious(<值>)`
```tsx
// 对比前后值变化
function usePrevious(value) {
  const ref = useRef();
  useEffect(() => { ref.current = value; });
  return ref.current;
}
```

---

## useDebounce 防抖

**基本写法：延迟处理高频输入**
`const <防抖值> = useDebounce(<值>, <延迟毫秒>)`
```tsx
// 搜索框防抖
function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
}
```

---

## useThrottle 节流

**基本写法：限制调用频率**
`const <节流值> = useThrottle(<值>, <间隔毫秒>)`
```tsx
// 滚动位置节流
function useThrottle(value, limit = 200) {
  const [last, setLast] = useState(value);
  const [t, setT] = useState(0);
  useEffect(() => {
    const now = Date.now();
    if (now - t >= limit) {
      setLast(value);
      setT(now);
    }
  }, [value, limit, t]);
  return last;
}
```

---

## useLocalStorage 持久化状态

**基本写法：状态同步到 localStorage**
`const [<值>, <设置>] = useLocalStorage(<键>, <初值>)`
```tsx
// 刷新后状态保留
function useLocalStorage(key, initial) {
  const [value, setValue] = useState(() => {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : initial;
  });
  useEffect(() => localStorage.setItem(key, JSON.stringify(value)), [key, value]);
  return [value, setValue];
}
```

---

## useFetch 数据请求

**基本写法：封装 fetch 与状态**
`const { <数据>, <加载>, <错误> } = useFetch(<URL>)`
```tsx
// 通用请求复用
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(url).then(r => r.json()).then(setData).catch(setError).finally(() => setLoading(false));
  }, [url]);
  return { data, loading, error };
}
```

---

## useEventListener 事件监听

**基本写法：安全绑定与解绑事件**
`useEventListener(<目标>, <事件>, <处理>, [<依赖>])`
```tsx
// 自动清理监听
function useEventListener(target, event, handler, deps = []) {
  useEffect(() => {
    target.addEventListener(event, handler);
    return () => target.removeEventListener(event, handler);
  }, [target, event, handler, ...deps]);
}
```

---

## useWindowSize 视口尺寸

**基本写法：监听窗口变化返回尺寸**
`const { <宽>, <高> } = useWindowSize()`
```tsx
// 响应式断点判断
function useWindowSize() {
  const [size, setSize] = useState({ width: window.innerWidth, height: window.innerHeight });
  useEffect(() => {
    const onResize = () => setSize({ width: window.innerWidth, height: window.innerHeight });
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);
  return size;
}
```

---

## useMediaQuery 媒体查询

**基本写法：返回是否匹配媒体查询**
`const <是否匹配> = useMediaQuery(<查询字符串>)`
```tsx
// 暗色模式检测
function useMediaQuery(query) {
  const [match, setMatch] = useState(() => window.matchMedia(query).matches);
  useEffect(() => {
    const mql = window.matchMedia(query);
    const onChange = () => setMatch(mql.matches);
    mql.addEventListener('change', onChange);
    return () => mql.removeEventListener('change', onChange);
  }, [query]);
  return match;
}
```

---

## useInterval 定时器

**基本写法：声明式定时器**
`useInterval(<回调>, <间隔毫秒>)`
```tsx
// 每秒更新避免内存泄漏
function useInterval(callback, delay) {
  const saved = useRef(callback);
  useEffect(() => { saved.current = callback; });
  useEffect(() => {
    const id = setInterval(() => saved.current(), delay);
    return () => clearInterval(id);
  }, [delay]);
}
```

---

## useClickAway 点击外部

**基本写法：点击元素外部触发回调**
`useClickAway(<ref>, <回调>)`
```tsx
// 关闭下拉菜单
function useClickAway(ref, handler) {
  useEffect(() => {
    const onClick = e => { if (ref.current && !ref.current.contains(e.target)) handler(); };
    document.addEventListener('mousedown', onClick);
    return () => document.removeEventListener('mousedown', onClick);
  }, [ref, handler]);
}
```

---

## useIntersectionObserver 曝光检测

**基本写法：检测元素是否进入视口**
`const [<ref>, <是否可见>] = useIntersectionObserver(<选项>)`
```tsx
// 无限滚动触发加载
function useIntersectionObserver(options) {
  const ref = useRef(null);
  const [visible, setVisible] = useState(false);
  useEffect(() => {
    const obs = new IntersectionObserver(([entry]) => setVisible(entry.isIntersecting), options);
    if (ref.current) obs.observe(ref.current);
    return () => obs.disconnect();
  }, [options]);
  return [ref, visible];
}
```

---

## useTitle 修改标题

**基本写法：动态设置文档标题**
`useTitle(<标题>)`
```tsx
// 路由切换更新标题
function useTitle(title) {
  useEffect(() => { document.title = title; }, [title]);
}
```

---

## useMount useUnmount 一次性副作用

**基本写法：仅挂载或卸载时执行**
`useMount(<回调>)`
```tsx
// 简化语义
function useMount(fn) {
  useEffect(() => fn(), []);
}
```

---

**基本写法：卸载清理**
`useUnmount(<清理回调>)`
```tsx
// 仅在卸载时执行
function useUnmount(fn) {
  const ref = useRef(fn);
  ref.current = fn;
  useEffect(() => () => ref.current(), []);
}
```

---

## 组合多个 Hooks

**基本写法：Hook 内调用其他 Hook**
`function use<名称>() { const <a> = use<A>(); const <b> = use<B>(); return { <a>, <b> }; }`
```tsx
// 组合防抖与请求
function useSearch(keyword) {
  const debounced = useDebounce(keyword, 300);
  return useFetch(`/api?q=${debounced}`);
}
```

---

## 参数解构与默认值

**基本写法：接收配置对象**
`function use<名称>({ <选项1> = <默认1>, <选项2> = <默认2> } = {})`
```tsx
// 提供灵活配置
function usePagination({ pageSize = 10, initial = 1 } = {}) {
  const [page, setPage] = useState(initial);
  return { page, pageSize, setPage };
}
```

---

## Hook 命名约束

**基本写法：必须以 use 开头**
`function use<名称>(<参数>) { }`
```tsx
// 否则 eslint-plugin-react-hooks 无法识别
function useAuth() { /* ... */ }
```

---

## 条件 Hook 禁止

**基本写法：Hook 不可在条件或循环中调用**
`if (<条件>) { useState(); } // 错误`
```tsx
// 正确做法：在条件内使用值
const [data] = useState(null);
if (cond) { process(data); }
```

---

## useReducer 封装复杂状态

**基本写法：用 reducer 抽象状态机**
`const [<状态>, <dispatch>] = useReducer(<reducer>, <初值>)`
```tsx
// 多字段关联更新封装为 Hook
function useForm(initial) {
  const [state, dispatch] = useReducer((s, a) => ({ ...s, ...a }), initial);
  return [state, dispatch];
}
```

---

## 自定义 Hook 测试

**基本写法：用 renderHook 测试**
`const { result } = renderHook(() => use<名称>())`
```tsx
// 测试 Hook 输出
import { renderHook } from '@testing-library/react';
const { result } = renderHook(() => useCounter(5));
expect(result.current.count).toBe(5);
```
