# React Compiler 自动记忆化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Compiler 概念

**基本写法：编译期自动插入 memo 化逻辑**
`react-compiler <源文件>`
```bash
# React Compiler 自动优化无需手动 memo
npx react-compiler build src
```

---

## 安装与启用

**基本写法：安装 babel 插件**
`npm i -D babel-plugin-react-compiler`
```bash
# 安装编译器插件
npm install --save-dev babel-plugin-react-compiler
```

---

**基本写法：babel 配置启用**
`plugins: ['react-compiler']`
```json
// babel.config.json
{
  "plugins": ["babel-plugin-react-compiler"]
}
```

---

**基本写法：Vite 项目启用**
`plugins: [react({ babel: { plugins: ['babel-plugin-react-compiler'] } })]`
```js
// vite.config.js
import react from '@vitejs/plugin-react';
export default {
  plugins: [react({ babel: { plugins: ['babel-plugin-react-compiler'] } })]
};
```

---

## 替代 useMemo

**基本写法：编译后自动缓存计算结果**
`const <值> = <计算>;`
```tsx
// 不再需要手写 useMemo
const sorted = list.sort();
// 编译器自动缓存
```

---

## 替代 useCallback

**基本写法：函数引用自动稳定**
`const <fn> = () => <逻辑>;`
```tsx
// 不再需要 useCallback 包装
const handleClick = () => doAction(id);
// 子组件不会因新引用而重渲染
```

---

## 替代 React.memo

**基本写法：组件 props 自动浅比较**
`function <组件>(<props>) { }`
```tsx
// 无需手动包裹 React.memo
function User({ name }) { return <div>{name}</div>; }
```

---

## 编译范围控制

**基本写法：通过 compilationMode 控制**
`'use no memo'`
```tsx
// 顶部注释禁用编译
'use no memo';
function MyComponent() {}
```

---

**基本写法：全局配置 sources**
`{ sources: (filename) => <是否编译> }`
```js
// 配置文件过滤
export default {
  sources: (filename) => filename.includes('/components/')
};
```

---

## eslint 规则

**基本写法：eslint-plugin-react-compiler 检测违规**
`plugins: ['react-compiler']`
```json
// .eslintrc
{
  "plugins": ["react-compiler"],
  "rules": { "react-compiler/react-compiler": "error" }
}
```

---

## 自动追踪依赖

**基本写法：编译器分析变量依赖**
`const <值> = <依赖1> + <依赖2>;`
```tsx
// 自动识别 list 与 key 为依赖
const item = list.find(i => i.id === key);
```

---

## ref 读取处理

**基本写法：编译器识别 ref.current 读取**
`const <值> = <ref>.current;`
```tsx
// ref 读取不会被记忆化
const node = inputRef.current;
```

---

## 副作用安全

**基本写法：编译器保留 effect 语义**
`useEffect(() => <副作用>, [<依赖>])`
```tsx
// 编译器不会破坏 effect 执行时机
useEffect(() => subscribe(id), [id]);
```

---

## 闭包正确性

**基本写法：编译器保证闭包变量最新**
`const <fn> = () => <使用state>;`
```tsx
// 自动避免 stale closure
const [count] = useState(0);
const log = () => console.log(count);
```

---

## 与现有 memo 共存

**基本写法：渐进迁移保留手写 memo**
`const <组件> = React.memo(<基础>)`
```tsx
// 已有 memo 不会被破坏
const User = React.memo(UserBase);
```

---

## 性能基线对比

**基本写法：通过 Profiler 验证收益**
`<Profiler id={<id>} onRender={<cb>}>`
```tsx
// 对比启用前后渲染次数
<Profiler id="App" onRender={(id, phase, time) => log(phase, time)}>
  <App />
</Profiler>
```

---

## 不适用场景

**基本写法：手动 memo 仍可保留**
`useMemo(() => <计算>, [<依赖>])`
```tsx
// 极端场景手动控制更精确
const heavy = useMemo(() => compute(big), [big]);
```

---

## 类型支持

**基本写法：TypeScript 项目直接启用**
`babel: { plugins: ['babel-plugin-react-compiler'] }`
```tsx
// 类型推断不受影响
const data: User = fetchUser();
```

---

## CI 集成

**基本写法：构建流程默认启用**
`npm run build`
```bash
# 构建时自动编译
npm run build
```

---

## 调试编译输出

**基本写法：查看编译后的代码**
`react-compiler <文件> --print`
```bash
# 输出编译后源码便于排查
npx react-compiler src/App.tsx --print
```

---

## 与 React 19 配合

**基本写法：React 19 默认推荐启用**
`react@19 + babel-plugin-react-compiler`
```bash
# React 19 应用最佳搭配
npm install react@19 babel-plugin-react-compiler
```

---

## 抑制规则违反

**基本写法：修复违规写法而非禁用**
`const <稳定> = useRef(<值>);`
```tsx
// 避免在渲染中创建新对象
const cache = useRef(new Map());
```

---

## 命令行工具

**基本写法：CLI 编译单文件**
`npx react-compiler <入口>`
```bash
# 命令行编译检查
npx react-compiler src/App.tsx
```

---

## 与 Next.js 集成

**基本写法：Next.js 15 自动启用**
`module.exports = { reactCompiler: true }`
```js
// next.config.js
module.exports = {
  experimental: { reactCompiler: true }
};
```

---

## 测试影响

**基本写法：测试代码可排除编译**
`{ sources: (f) => !f.includes('.test.') }`
```js
// 排除测试文件
export default { sources: (f) => !f.includes('__tests__') };
```
