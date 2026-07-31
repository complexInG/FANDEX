# React Portal 与 DOM 操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## createPortal 渲染到任意节点

**基本写法：将子节点渲染到指定容器**
`createPortal(<子节点>, <容器>)`
```tsx
// 弹窗渲染到 body 避免层级污染
import { createPortal } from 'react-dom';
function Modal({ children }) {
  return createPortal(<div className="modal">{children}</div>, document.body);
}
```

---

**基本写法：指定容器引用**
`createPortal(<节点>, <ref>.current)`
```tsx
// 渲染到具名容器
const containerRef = useRef(null);
return createPortal(<Tooltip />, containerRef.current);
```

---

## Portal 事件冒泡

**基本写法：Portal 内事件仍向 React 父组件冒泡**
`<父组件 onClick={<处理>}> <Portal /> </父组件>`
```tsx
// DOM 层级脱离但事件保持 React 树
function App() {
  return <div onClick={() => console.log('点击捕获')}>
    <Modal>内容</Modal>
  </div>;
}
```

---

## Portal 模态框实现

**基本写法：模态框遮罩与内容**
`{<可见> && <Modal><内容></Modal>}`
```tsx
// 条件渲染弹窗
function Dialog({ open, onClose, children }) {
  if (!open) return null;
  return createPortal(
    <div className="overlay" onClick={onClose}>
      <div className="dialog" onClick={e => e.stopPropagation()}>{children}</div>
    </div>, document.body);
}
```

---

## useRef 获取 DOM

**基本写法：通过 ref 引用 DOM 元素**
`const <ref> = useRef(<初值>); <元素 ref={<ref>} />`
```tsx
// 挂载后访问 input
const inputRef = useRef(null);
useEffect(() => inputRef.current.focus(), []);
return <input ref={inputRef} />;
```

---

## 回调 Ref

**基本写法：使用函数接收 DOM 节点**
`<元素 ref={<节点> => <赋值>} />`
```tsx
// 节点挂载与卸载时回调
<input ref={node => { inputRef.current = node; }} />
```

---

## forwardRef 转发 ref

**基本写法：让子组件接收父级 ref**
`const <组件> = forwardRef((<props>, <ref>) => <JSX>)`
```tsx
// 父组件直接聚焦子组件内部 input
const FancyInput = forwardRef((props, ref) => (
  <input ref={ref} className="fancy" />
));
```

---

## useImperativeHandle 暴露方法

**基本写法：自定义暴露给父级的实例方法**
`useImperativeHandle(<ref>, () => ({ <方法> }), [<依赖>])`
```tsx
// 仅暴露 focus 而非整个 DOM
const FancyInput = forwardRef((props, ref) => {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus()
  }));
  return <input ref={inputRef} />;
});
```

---

## useRef 存储可变值

**基本写法：不触发渲染的容器**
`const <ref> = useRef(<初值>); <ref>.current = <新值>;`
```tsx
// 存储定时器 id
const timerRef = useRef(null);
timerRef.current = setInterval(tick, 1000);
```

---

## useRef 跨渲染保持引用

**基本写法：避免每次渲染重建对象**
`const <ref> = useRef(<对象>)`
```tsx
// 保持 Map 引用稳定
const cacheRef = useRef(new Map());
cacheRef.current.set(key, value);
```

---

## 直接操作 DOM

**基本写法：读取属性或调用方法**
`<ref>.current.<方法>()`
```tsx
// 滚动到顶部
listRef.current.scrollTo(0, 0);
```

---

## 测量元素尺寸

**基本写法：使用 getBoundingClientRect**
`const <rect> = <ref>.current.getBoundingClientRect()`
```tsx
// 计算位置
const rect = btnRef.current.getBoundingClientRect();
setPos({ x: rect.left, y: rect.top });
```

---

## ResizeObserver 监听尺寸

**基本写法：监听元素尺寸变化**
`new ResizeObserver(<回调>).observe(<节点>)`
```tsx
// 容器宽度变化时更新
useEffect(() => {
  const obs = new ResizeObserver(([entry]) => setWidth(entry.contentRect.width));
  if (boxRef.current) obs.observe(boxRef.current);
  return () => obs.disconnect();
}, []);
```

---

## focus 与 blur 控制

**基本写法：编程式聚焦失焦**
`<ref>.current.focus()`
```tsx
// 错误提示后自动聚焦
inputRef.current.focus();
inputRef.current.select();
```

---

## 滚动控制

**基本写法：滚动到指定位置**
`<ref>.current.scrollTo({ top: <位置>, behavior: 'smooth' })`
```tsx
// 平滑滚动到底部
listRef.current.scrollTo({ top: listRef.current.scrollHeight, behavior: 'smooth' });
```

---

## scrollIntoView 进入视口

**基本写法：元素滚动到可见区域**
`<ref>.current.scrollIntoView({ behavior: 'smooth', block: 'start' })`
```tsx
// 锚点定位
itemRef.current.scrollIntoView({ behavior: 'smooth' });
```

---

## Portal 与 SSR 兼容

**基本写法：服务端无 document 时安全降级**
`const <容器> = typeof document !== 'undefined' ? document.body : null`
```tsx
// 防止服务端报错
const target = typeof document !== 'undefined' ? document.body : null;
return target ? createPortal(children, target) : null;
```

---

## 选择器查询

**基本写法：在 ref 容器内查询子元素**
`<ref>.current.querySelector(<选择器>)`
```tsx
// 查找内部按钮
const btn = rootRef.current.querySelector('.submit-btn');
```

---

## className 操作

**基本写法：通过 ref 修改类名**
`<ref>.current.classList.add(<类名>)`
```tsx
// 动态添加高亮类
boxRef.current.classList.add('active');
boxRef.current.classList.remove('active');
```

---

## style 行内样式修改

**基本写法：直接修改 style 属性**
`<ref>.current.style.<属性> = <值>`
```tsx
// 设置位移
draggableRef.current.style.transform = `translateX(${x}px)`;
```

---

## 阻止默认与冒泡

**基本写法：在事件处理中调用原生方法**
`<事件对象>.preventDefault(); <事件对象>.stopPropagation();`
```tsx
// 阻止表单默认提交并停止冒泡
function handleSubmit(e) {
  e.preventDefault();
  e.stopPropagation();
}
```

---

## DOM 引用清理

**基本写法：组件卸载时清理资源**
`return () => { <ref>.current = null; }`
```tsx
// 避免内存泄漏
useEffect(() => {
  return () => { timerRef.current = null; };
}, []);
```

---

## ReactDOM flushSync

**基本写法：强制同步刷新 DOM**
`flushSync(() => <更新>)`
```tsx
// 需要立即读取更新后的 DOM
import { flushSync } from 'react-dom';
flushSync(() => setHighlight(true));
const rect = ref.current.getBoundingClientRect();
```

---

## createRoot 挂载根

**基本写法：React 18 挂载方式**
`createRoot(<容器>).render(<JSX>)`
```tsx
// 替代 ReactDOM.render
import { createRoot } from 'react-dom/client';
createRoot(document.getElementById('root')).render(<App />);
```

---

## unmountComponentAtNode 卸载

**基本写法：卸载根组件**
`<root>.unmount()`
```tsx
// 卸载并清理
const root = createRoot(container);
root.unmount();
```
