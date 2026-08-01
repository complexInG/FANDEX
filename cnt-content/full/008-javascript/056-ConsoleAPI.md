---
order: 560
title: JavaScript console API 语法速查
module: javascript

category: '008-javascript'
difficulty: beginner
description: JavaScript console API 语法速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基础输出

**基本写法：log 多参数**
`console.log(<值>, [<值>...])`
```javascript
// 多参数空格分隔输出
console.log("id:", 1, "user:", { name: "Tom" });
```

---

**基本写法：info / debug / warn / error**
`console.<level>(<值>)`
```javascript
// 不同级别，渲染样式不同
console.info("信息");
console.debug("调试");
console.warn("警告");
console.error("错误");
```

---

## 格式化输出

**基本写法：格式占位符**
`console.log("<格式串>", <值>)`
```javascript
// %s 字符串 %d/%i 整数 %f 浮点 %o 对象 %c 样式
console.log("%s 有 %d 岁", "Tom", 18);
console.log("%c红色文字", "color:red;font-weight:bold");
```

---

**基本写法：对象表格**
`console.table(<数据>, [<列>])`
```javascript
// 数组或对象渲染为表格
console.table([{ id: 1, name: "A" }, { id: 2, name: "B" }]);
console.table(users, ["name"]);
```

---

**基本写法：分组输出**
`console.group([<标题>])` | `console.groupEnd()`
```javascript
// 折叠分组
console.group("用户信息");
console.log("name: Tom");
console.groupEnd();
// 默认展开
console.groupCollapsed("详情");
console.groupEnd();
```

---

## 计时与计数

**基本写法：计时器**
`console.time(<标签>)` | `console.timeEnd(<标签>)`
```javascript
// 测量代码执行耗时
console.time("loop");
for (let i = 0; i < 1e6; i++) {}
console.timeEnd("loop"); // loop: 1.23ms
```

---

**基本写法：计数器**
`console.count([<标签>])`
```javascript
// 统计调用次数
function fn() { console.count("fn"); }
fn(); fn(); // fn: 1 / fn: 2
console.countReset("fn");
```

---

## 断言与堆栈

**基本写法：断言**
`console.assert(<条件>, [<消息>])`
```javascript
// 条件为 false 才输出错误
console.assert(age >= 0, "年龄不能为负");
```

---

**基本写法：打印堆栈**
`console.trace([<消息>])`
```javascript
// 输出调用栈
function a() { b(); }
function b() { console.trace("位置"); }
a();
```

---

## 目录树与清屏

**基本写法：对象目录树**
`console.dir(<对象>, [<选项>])`
```javascript
// 以可展开树形显示
console.dir(document.body, { depth: 2, colors: true });
```

---

**基本写法：清屏**
`console.clear()`
```javascript
// 清空控制台
console.clear();
```

---

## 性能分析

**基本写法：性能采样**
`console.profile(<标签>)` | `console.profileEnd(<标签>)`
```javascript
// 配合浏览器性能分析器
console.profile("render");
render();
console.profileEnd("render");
```

---

**基本写法：时间戳**
`console.timeStamp(<标签>)`
```javascript
// 在性能时间轴打标记
console.timeStamp("start-render");
```

---

## Node.js 专属

**基本写法：控制台颜色（Node）**
`console.log("\x1b[31m%s\x1b[0m", "红")`
```javascript
// ANSI 转义码着色
// 31 红 32 绿 33 黄 34 蓝 0 重置
console.log("\x1b[32m成功\x1b[0m");
```

---

## 条件与流式

**基本写法：按级别条件输出**
`console.log(<值>)`
```javascript
// 自定义封装按级别过滤
const log = (level, ...args) => {
  if (LEVELS[level] >= LEVELS[config.level]) console[level](...args);
};
```

---

## 推荐实践

**基本写法：生产环境屏蔽**
`console.log(<值>)`
```javascript
// 构建时移除或重写
if (process.env.NODE_ENV === "production") {
  console.log = console.info = () => {};
}
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
| JavaScript Map/Set/WeakMap/WeakSet 语法速查 | 053-MapSetWeakMapWeakSet | 本文的并列主题 |
| JavaScript ArrayBuffer 与 TypedArray 语法速查 | 054-ArrayBufferTypedArray | 本文的并列主题 |
| JavaScript 包管理命令速查（npm/pnpm/yarn） | 055-PackageManagerCommands | 本文的并列主题 |
| JavaScript console API 语法速查 | 056-ConsoleAPI | 本文自身 |
