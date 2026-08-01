---
order: 540
title: JavaScript ArrayBuffer 与 TypedArray 语法速查
module: javascript

category: '008-javascript'
difficulty: beginner
description: JavaScript ArrayBuffer 与 TypedArray 语法速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ArrayBuffer 基础

**基本写法：创建定长缓冲**
`new ArrayBuffer(<字节数>)`
```javascript
// 原始二进制数据，固定长度
const buf = new ArrayBuffer(16);
buf.byteLength; // 16
buf.detached;   // false（是否被转移）
```

---

**基本写法：可扩容 ArrayBuffer（ES2024）**
`new ArrayBuffer(<长度>, { maxByteLength: <最大> })`
```javascript
// 创建可调整大小的缓冲
const buf = new ArrayBuffer(8, { maxByteLength: 32 });
buf.resizable;        // true
buf.maxByteLength;    // 32
buf.resize(16);       // 扩容
buf.resize(4);        // 缩容
```

---

**基本写法：transfer 转移所有权（ES2024）**
`<buffer>.transfer([<新字节长度>])`
```javascript
// 转移后原 buffer 被分离不可用
const a = new ArrayBuffer(8);
const b = a.transfer();   // a.detached === true
```

---

## TypedArray 类型

**基本写法：创建各类定型数组**
`new <TypedArray>(<长度>)`
```javascript
// 常见类型
new Int8Array(4);        // 8 位有符号
new Uint8Array(4);       // 8 位无符号
new Uint8ClampedArray(4);// 钳制 0-255
new Int16Array(4);       // 16 位有符号
new Uint16Array(4);      // 16 位无符号
new Int32Array(4);       // 32 位有符号
new Uint32Array(4);      // 32 位无符号
new Float32Array(4);     // 32 位浮点
new Float64Array(4);     // 64 位浮点
new BigInt64Array(4n);   // 64 位大整数
new BigUint64Array(4n);  // 64 位无符号大整数
new Float16Array(4);     // 16 位浮点（ES2025）
```

---

**基本写法：从数组或缓冲创建**
`new <TypedArray>(<可迭代>)` | `new <TypedArray>(<buffer>, [<偏移>], [<长度>])`
```javascript
// 从数组创建
const a = new Uint8Array([1, 2, 3]);
// 共享底层 ArrayBuffer
const buf = new ArrayBuffer(8);
const view = new Uint8Array(buf, 0, 4); // 偏移 0，长度 4
```

---

## TypedArray 属性与操作

**基本写法：底层视图属性**
`<view>.buffer` | `<view>.byteLength` | `<view>.byteOffset`
```javascript
// 访问底层 buffer 与位置
const v = new Int32Array(buf, 4, 2);
v.buffer;      // 底层 ArrayBuffer
v.byteLength;  // 占用字节数
v.byteOffset;  // 在 buffer 中的偏移
v.length;      // 元素个数
```

---

**基本写法：set 复制数据**
`<view>.set(<数组或定型数组>, [<偏移>])`
```javascript
// 批量写入
const v = new Uint8Array(8);
v.set([10, 20, 30], 2); // 从偏移 2 开始写入
```

---

**基本写法：subarray 共享视图**
`<view>.subarray([<开始>, <结束>])`
```javascript
// 返回共享内存的子视图
const v = new Uint8Array([1, 2, 3, 4]);
const sub = v.subarray(1, 3); // [2, 3]，修改 sub 影响 v
```

---

## DataView 视图

**基本写法：创建 DataView**
`new DataView(<buffer>, [<偏移>], [<长度>])`
```javascript
// 可混用大小端读写不同类型
const dv = new DataView(new ArrayBuffer(8));
dv.setInt8(0, 127);
dv.getInt8(0);    // 127
```

---

**基本写法：指定字节序读写**
`<dv>.setInt32(<偏移>, <值>, [<小端>])`
```javascript
// 第三个参数 true 表示小端序
dv.setInt32(0, 0x12345678, true);
dv.getInt32(0, true);     // 305419896
dv.getFloat64(0, true);   // 读取 64 位浮点
```

---

## SharedArrayBuffer 与 Atomics

**基本写法：共享缓冲**
`new SharedArrayBuffer(<字节数>)`
```javascript
// 可跨线程共享（Worker）
const sab = new SharedArrayBuffer(16);
const view = new Int32Array(sab);
```

---

**基本写法：原子操作**
`Atomics.add(<view>, <索引>, <值>)`
```javascript
// 原子读改写，避免竞态
const view = new Int32Array(sab);
Atomics.store(view, 0, 10);
Atomics.add(view, 0, 5);     // 返回旧值 10
Atomics.load(view, 0);       // 15
Atomics.compareExchange(view, 0, 15, 20); // 期望 15 才写 20
```

---

**基本写法：等待与通知**
`Atomics.wait(<view>, <索引>, <期望值>)` | `Atomics.notify(<view>, <索引>, [<数量>])`
```javascript
// 线程间同步
Atomics.wait(view, 0, 0);        // 阻塞直到被通知
Atomics.notify(view, 0, 1);      // 唤醒 1 个等待者
Atomics.waitAsync(view, 0, 0);   // 异步等待（ES2024）
```

---

## 编码转换

**基本写法：字符串与 TypedArray 互转**
`new TextEncoder().encode(<字符串>)`
```javascript
// UTF-8 编解码
const enc = new TextEncoder();
const bytes = enc.encode("中文"); // Uint8Array
const dec = new TextDecoder("utf-8");
dec.decode(bytes); // "中文"
```

---

## 字节序判断

**基本写法：判断大小端**
`new Uint8Array(new Uint32Array([1]).buffer)`
```javascript
// 小端序返回 [1,0,0,0]，大端序返回 [0,0,0,1]
const le = new Uint8Array(new Uint32Array([1]).buffer)[0] === 1;
console.log(le ? "little-endian" : "big-endian");
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
| JavaScript ArrayBuffer 与 TypedArray 语法速查 | 054-ArrayBufferTypedArray | 本文自身 |
| JavaScript 包管理命令速查（npm/pnpm/yarn） | 055-PackageManagerCommands | 本文的并列主题 |
| JavaScript console API 语法速查 | 056-ConsoleAPI | 本文的并列主题 |
