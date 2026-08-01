---
order: 530
title: JavaScript Map/Set/WeakMap/WeakSet 语法速查
module: 008-javascript
category: '008-javascript'
difficulty: beginner
description: JavaScript Map/Set/WeakMap/WeakSet 语法速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# JavaScript Map/Set/WeakMap/WeakSet 语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Map 基础

**基本写法：创建与增删改查**
`new Map([[<k>, <v>], ...])`
```javascript
// Map 保留插入顺序，键可为任意类型
const m = new Map([["a", 1]]);
m.set("b", 2);     // 添加
m.get("a");        // 1
m.has("b");        // true
m.size;            // 2
m.delete("a");     // 删除
m.clear();         // 清空
```

---

## Map 遍历

**基本写法：遍历键值对**
`<map>.forEach((<v>, <k>) => {})`
```javascript
// 按插入顺序遍历
const m = new Map([["a", 1], ["b", 2]]);
m.forEach((v, k) => console.log(k, v));
```

---

**基本写法：entries / keys / values**
`<map>.entries()`
```javascript
// 返回迭代器
for (const [k, v] of m.entries()) {}
for (const k of m.keys()) {}
for (const v of m.values()) {}
```

---

## Map 与对象互转

**基本写法：对象转 Map**
`new Map(Object.entries(<对象>))`
```javascript
// 对象转 Map
const obj = { a: 1, b: 2 };
const m = new Map(Object.entries(obj));
```

---

**基本写法：Map 转对象**
`Object.fromEntries(<map>)`
```javascript
// Map 转对象，键须为字符串
const obj = Object.fromEntries(m);
```

---

## Set 基础

**基本写法：创建与增删查**
`new Set([<可迭代>])`
```javascript
// Set 值唯一，自动去重
const s = new Set([1, 2, 2, 3]);
s.add(4);          // 添加
s.has(3);          // true
s.size;            // 4
s.delete(2);       // 删除
s.clear();         // 清空
```

---

## Set 去重与运算

**基本写法：数组去重**
`[...new Set(<数组>)]`
```javascript
// 利用 Set 唯一性去重
const uniq = [...new Set([1, 1, 2, 3, 3])]; // [1, 2, 3]
```

---

**基本写法：交集差集（ES2025 前）**
`new Set([...a].filter(x => b.has(x)))`
```javascript
// 兼容写法
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);
const inter = new Set([...a].filter(x => b.has(x))); // {2,3}
const diff = new Set([...a].filter(x => !b.has(x))); // {1}
```

---

## Set 遍历

**基本写法：遍历 Set**
`for (const <v> of <set>) {}`
```javascript
// Set 默认遍历 values
for (const v of s) {}
s.forEach(v => {});
```

---

## WeakMap 基础

**基本写法：创建与操作**
`new WeakMap([[<对象键>, <值>]])`
```javascript
// 键必须为对象，键被回收后自动清除该项
const wm = new WeakMap();
const key = {};
wm.set(key, "data");
wm.get(key);   // "data"
wm.has(key);   // true
wm.delete(key);
```

---

**基本写法：私有属性模拟**
`const wm = new WeakMap()` | `wm.set(this, <私有>)`
```javascript
// 利用 WeakMap 模拟私有字段
const priv = new WeakMap();
class Counter {
  constructor() { priv.set(this, 0); }
  inc() { priv.set(this, priv.get(this) + 1); }
  get val() { return priv.get(this); }
}
```

---

## WeakSet 基础

**基本写法：创建与操作**
`new WeakSet([<可迭代对象>])`
```javascript
// 只能存对象，弱引用
const ws = new WeakSet();
const o = {};
ws.add(o);
ws.has(o);   // true
ws.delete(o);
```

---

## WeakRef 与 FinalizationRegistry

**基本写法：弱引用对象**
`new WeakRef(<对象>)`
```javascript
// 不阻止垃圾回收
let obj = { data: 1 };
const ref = new WeakRef(obj);
ref.deref(); // 取值，被回收后返回 undefined
```

---

**基本写法：垃圾回收回调**
`new FinalizationRegistry(<回调>)`
```javascript
// 对象被回收时触发清理
const registry = new FinalizationRegistry(held => {
  console.log("释放", held);
});
registry.register(obj, "标记值");
```

---

## Map 与 Object 区别

**基本写法：键类型与顺序**
`<map>.set(<任意键>, <值>)`
```javascript
// Map 键可为对象函数，Object 键转字符串
const m = new Map();
const key = {};
m.set(key, 1); // 对象作键
// Object 作键会被转成 "[object Object]"
```

---

## 性能与选择

**基本写法：频繁增删用 Map**
`<map>.set(<k>, <v>)`
```javascript
// Map 频繁增删性能优于 Object
// 大数据量查找 Map 接近 O(1)
// 需要键为非字符串时必须用 Map
```

---

## 参考文献



MDN JavaScript 文档：https://developer.mozilla.org/zh-CN/docs/Web/JavaScript
ECMAScript 规范：https://tc39.es/ecma262/
Node.js 官方文档：https://nodejs.org/docs/latest/api/
JavaScript 秘密花园：https://bonsaiden.github.io/JavaScript-Garden/
Can I use：https://caniuse.com/

## 延伸阅读



JavaScript 基础语法，见 008-javascript 模块文档。
TypeScript 类型系统，见 009-typescript 模块。
浏览器 DOM 与事件，见 006-html5/007-css 模块。
前端框架 React/Vue，见 011-react/010-vue3 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 JavaScript 课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 事件循环深入

宏任务：script、setTimeout、setInterval、I/O、UI 渲染；微任务：Promise.then、queueMicrotask、MutationObserver。
每轮循环：执行一个宏任务，清空整个微任务队列，必要时渲染；微任务中产生的微任务继续执行，可能饿死宏任务。
Node 的事件循环分阶段：timers、pending callbacks、idle、poll、check、close；process.nextTick 优先于微任务。
调试技巧：用 Performance API 测量；async 栈追踪定位未处理拒绝。

### 13.2 this 与作用域

四种绑定：直接调用（undefined/global）、方法调用（对象）、call/apply/bind（显式）、箭头函数（词法）。
class 方法默认严格模式，事件回调中 this 丢失需绑定或箭头函数。
作用域链：全局 -> 模块 -> 函数 -> 块级（let/const）；闭包保留整个作用域链。
工程建议：避免 this 魔法，优先箭头函数与显式参数。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| JavaScript 概述与运行环境 | 001-JavaScriptOverviewRuntimeEnv | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 变量与数据类型 | 003-VariableDataType | 本文的并列主题 |
| 数据类型与运算符 | 004-DataTypeOperator | 本文的并列主题 |
| 控制流 | 005-ControlFlow | 本文的并列主题 |
| 高阶函数 | 006-HigherOrderFunction | 本文的并列主题 |
| 递归与尾调用优化 | 007-LinearGeneticProgramming | 本文的性能延伸 |
| 柯里化与偏函数 | 008-CurryAndFunctionComposition | 本文的并列主题 |
| 生成器函数 | 009-CoroutinesInJavaScript | 本文的并列主题 |
| Proxy与Reflect | 010-ExploringES6ProxiesAndReflect | 本文的并列主题 |
| Object扩展 | 011-ObjectReference | 本文的并列主题 |
| 事件循环 | 012-EventLoop | 本文的并列主题 |
| 具名捕获组 | 013-ES2018RegExpNamedCaptureGroups | 本文的并列主题 |
| 断言 | 014-Assert | 本文的并列主题 |
| Unicode属性转义 | 015-UnicodePropertyEscape | 本文的并列主题 |
| 函数、作用域与闭包 | 016-FunctionScopeClosure | 本文的并列主题 |
| 自定义Error | 017-ErrorReferenceAndControlFlowAndErrorHandling | 本文的并列主题 |
| BOM | 018-CrossDocumentMessaging | 本文的并列主题 |
| 网络请求API | 019-ImageOptimization | 本文的并列主题 |
| Web存储API | 020-StorageForTheWeb | 本文的并列主题 |
| 索引数据库 | 021-IndexedDBADatabaseInYourBrowser | 本文的并列主题 |
| Temporal | 022-TemporalJavaScriptAPI | 本文的并列主题 |
| 迭代器帮助器 | 023-IteratorHelper | 本文的并列主题 |
| Promise构造器 | 024-YouDonTKnowJSAsyncPerformance | 本文的并列主题 |
| Records与Tuples | 025-RecordsTuples | 本文的并列主题 |
| 对象与数组 | 026-ObjectArray | 本文的并列主题 |
| DOM 操作与事件 | 027-DOMOperationEvent | 本文的并列主题 |
| JavaScript 最新特性与运行时 | 028-JavaScriptLatestFeature | 本文的并列主题 |
| JavaScript 模块化 | 029-JavaScriptModular | 本文的并列主题 |
| 异步编程 | 030-AsyncProgramming | 本文的并列主题 |
| 闭包的内存泄露与优化 | 031-ClosureMemoryLeakOptimization | 本文的性能延伸 |
| 原型链继承与class本质 | 032-PrototypeChainClassEssence | 本文的并列主题 |
| 事件循环详解 | 033-EventLoopDetailed | 本文的并列主题 |
| Promise静态方法 | 034-PromiseStaticMethod | 本文的并列主题 |
| 异步并发控制 | 035-AsyncConcurrencyControl | 本文的并列主题 |
| ES6+ 新特性 | 036-ES6NewFeatures | 本文的并列主题 |
| 深拷贝与浅拷贝 | 037-DeepShallowCopy | 本文的并列主题 |
| 防抖与节流 | 038-DebounceThrottle | 本文的并列主题 |
| 数组高阶方法 | 039-ArrayHigherOrderMethod | 本文的并列主题 |
| Proxy与Reflect实际应用 | 040-ProxyReflectPractice | 本文的并列主题 |
| 模块动态导入与代码分割 | 041-ModuleDynamicImportCodeSplitting | 本文的并列主题 |
| JavaScript 原型与继承 | 042-JavaScriptPrototypeInheritance | 本文的并列主题 |
| 正则表达式 | 043-Regex | 本文的并列主题 |
| 错误边界与全局错误捕获 | 044-ErrorBoundaryGlobalErrorCatch | 本文的并列主题 |
| 内存泄漏排查 | 045-MemoryLeakTroubleshoot | 本文的并列主题 |
| Web API 与浏览器接口 | 046-WebAPIBrowserInterface | 本文的并列主题 |
| 调试与性能优化 | 047-DebugPerformanceOptimization | 本文的性能延伸 |
| 典型项目实战 | 048-TypicalProjectPractice | 本文的综合应用 |
| Node.js 高级特性与性能优化 | 049-NodeJsAdvancedFeaturePerformanceOptimization | 本文的性能延伸 |
| JavaScript 项目示例：待办事项应用 | 050-JavaScriptProjectExampleTodoApp | 本文的综合应用 |
| JavaScript 理论知识点 | 051-JavaScriptTheory | 本文的并列主题 |
| ES2023/2024/2025 新特性 | 052-ES2024NewFeatures | 本文的并列主题 |
| JavaScript Map/Set/WeakMap/WeakSet 语法速查 | 053-MapSetWeakMapWeakSet | 本文自身 |
| JavaScript ArrayBuffer 与 TypedArray 语法速查 | 054-ArrayBufferTypedArray | 本文的并列主题 |
| JavaScript 包管理命令速查（npm/pnpm/yarn） | 055-PackageManagerCommands | 本文的并列主题 |
| JavaScript console API 语法速查 | 056-ConsoleAPI | 本文的并列主题 |
