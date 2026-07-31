# React 设计模式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 高阶组件 HOC

**基本写法：包装组件增强功能**
`function <withX>>(<组件>) { return function <增强组件>(<props>) { return <<组件> {...<props>} /> } }`
```tsx
// 通用日志增强
function withLogger(Wrapped) {
  return function New(props) {
    useEffect(() => console.log('render'), []);
    return <Wrapped {...props} />;
  };
}
```

---

**基本写法：HOC 注入额外 props**
`function <withX>(<组件>) { return (props) => <<组件> {...props} <额外字段>={<值>} /> }`
```tsx
// 注入用户信息
function withUser(Wrapped) {
  return props => <Wrapped {...props} user={useUser()} />;
}
```

---

**基本写法：组合多个 HOC**
`const <增强> = <withA>(<withB>(<组件>))`
```tsx
// 自下而上依次包装
const App = withAuth(withLogger(Base));
```

---

## Render Props 模式

**基本写法：通过 prop 函数共享渲染逻辑**
`<组件 render={<渲染函数>} />`
```tsx
// 调用方决定渲染内容
<Mouse render={({ x, y }) => <p>{x},{y}</p>} />
```

---

**基本写法：children as function**
`<组件>{<渲染函数>}</组件>`
```tsx
// 使用 children 函数
<Mouse>{({ x, y }) => <Dot x={x} y={y} />}</Mouse>
```

---

**基本写法：实现 Render Props 组件**
`function <组件>(<props>) { return props.children(<状态>); }`
```tsx
// 提供者暴露内部状态
function Mouse({ children }) {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  return children(pos);
}
```

---

## Compound Components 复合组件

**基本写法：通过 Context 共享内部状态**
`<容器> <子A /> <子B /> </容器>`
```tsx
// 灵活组合但状态联动
<Select>
  <Select.Trigger />
  <Select.Option value="1" />
</Select>
```

---

**基本写法：父组件提供 Context**
`const <Ctx> = createContext(); <Ctx.Provider value={<状态>}>`
```tsx
// 内部状态共享给子组件
const SelectCtx = createContext();
function Select({ children }) {
  const [open, setOpen] = useState(false);
  return <SelectCtx.Provider value={{ open, setOpen }}>{children}</SelectCtx.Provider>;
}
```

---

## 自定义 Hook 替代 HOC

**基本写法：用 Hook 复用逻辑**
`const <逻辑> = use<名称>();`
```tsx
// 替代 HOC 的更优方案
const user = useUser();
return <Profile user={user} />;
```

---

## Provider 模式

**基本写法：顶层 Provider 注入依赖**
`<Provider value={<服务>}> <App /> </Provider>`
```tsx
// 依赖注入
const ApiContext = createContext();
<ApiContext.Provider value={api}><App /></ApiContext.Provider>
```

---

## 受控与非受控组件

**基本写法：受控组件由 props 驱动**
`<input value={<值>} onChange={<处理>} />`
```tsx
// 父组件完全控制
<input value={text} onChange={e => setText(e.target.value)} />
```

---

**基本写法：非受控组件使用 defaultValue**
`<input defaultValue={<值>} ref={<ref>} />`
```tsx
// 内部状态由 DOM 管理
<input defaultValue={init} ref={inputRef} />
```

---

## Forwarding Refs

**基本写法：forwardRef 转发 ref**
`const <组件> = forwardRef((<props>, <ref>) => <JSX>)`
```tsx
// 让父组件访问内部 DOM
const Input = forwardRef((props, ref) => <input ref={ref} {...props} />);
```

---

## Container/Presentational 模式

**基本写法：容器组件负责数据**
`function <容器>() { const <数据> = <获取>(); return <展示 <数据>={<数据>} /> }`
```tsx
// 数据与视图分离
function UserContainer() {
  const user = useUser();
  return <UserView user={user} />;
}
```

---

**基本写法：展示组件纯渲染**
`function <展示>({ <数据> }) { return <JSX>; }`
```tsx
// 不含副作用只渲染 props
function UserView({ user }) { return <div>{user.name}</div>; }
```

---

## 状态提升

**基本写法：共享状态放到共同父级**
`function <父>() { const [<共享>, <设置>] = useState(); <<A> <共享>={<共享>} /> <<B> <设置>={<设置>} /> }`
```tsx
// 多子组件共享数据
function App() {
  const [text, setText] = useState('');
  return <><Input value={text} onChange={setText} /><Preview text={text} /></>;
}
```

---

## 组合优于继承

**基本写法：通过 props.children 组合**
`function <布局>(<props>) { return <div>{<props>.children}</div>; }`
```tsx
// 灵活嵌套内容
function Card({ children }) { return <div className="card">{children}</div>; }
```

---

## Specialization 特化

**基本写法：基于通用组件派生专用组件**
`function <特化>(<props>) { return <通用 <特定字段>={<值>} {...<props>} /> }`
```tsx
// 派生特定按钮
function PrimaryButton(props) {
  return <Button color="blue" {...props} />;
}
```

---

## Render Optimization 模式

**基本写法：memo 避免重渲染**
`const <组件> = React.memo(<基础组件>)`
```tsx
// props 不变时跳过渲染
const List = React.memo(ListBase);
```

---

## Error Boundary 模式

**基本写法：class 组件捕获子树错误**
`class <Boundary> extends React.Component { static getDerivedStateFromError() {} }`
```tsx
// 捕获渲染错误降级 UI
class SafeArea extends React.Component {
  state = { hasError: false };
  static getDerivedStateFromError() { return { hasError: true }; }
  render() { return this.state.hasError ? <Fallback /> : this.props.children; }
}
```

---

## Slot 模式

**基本写法：通过具名 props 实现插槽**
`<布局 <header>={<A>} <body>={<B>} />`
```tsx
// 多处内容注入
<Layout header={<Header />} body={<Content />} />
```

---

## Hooks 复用模式

**基本写法：将副作用抽成 Hook**
`function use<名称>(<参数>) { useEffect(() => <副作用>, [<依赖>]); }`
```tsx
// 逻辑复用统一入口
function useTrack(event) { useEffect(() => log(event), [event]); }
```

---

## Context Selector 模式

**基本写法：拆分 Context 或使用 selector 库**
`const <部分> = useContextSelector(<Ctx>, <选择器>)`
```tsx
// 精确订阅避免多余渲染
const value = useContextSelector(Ctx, s => s.field);
```

---

## Factory Component 模式

**基本写法：动态创建组件**
`function create<组件>(<配置>) { return function <组件>(<props>) { /* */ }; }`
```tsx
// 按配置生成组件
function createInput(type) {
  return props => <input type={type} {...props} />;
}
```

---

## 容器组合模式

**基本写法：组合多个 Provider**
`const <App> = <withA>(<withB>(<根>))`
```tsx
// 串联多个 Provider
function withProviders(...providers) {
  return Comp => props => providers.reduceRight((acc, P) => <P>{acc}</P>, <Comp {...props} />);
}
```
