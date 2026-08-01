---
order: 550
title: JavaScript 包管理命令速查（npm/pnpm/yarn）
module: 008-javascript
category: '008-javascript'
difficulty: beginner
description: JavaScript 包管理命令速查（npm/pnpm/yarn） 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# JavaScript 包管理命令速查（npm/pnpm/yarn）

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 初始化项目

**基本写法：生成 package.json**
`npm init [-y]` | `pnpm init` | `yarn init [-y]`
```bash
# -y 使用默认值跳过提问
npm init -y
pnpm init
yarn init -y
```

---

## 安装依赖

**基本写法：安装全部依赖**
`npm install` | `pnpm install` | `yarn`
```bash
# 读取 lock 文件安装
npm install        # npm
pnpm install       # pnpm
yarn               # yarn
```

---

**基本写法：添加单个包**
`npm install <包> [-D|-g]`
```bash
# -D 开发依赖 -g 全局
npm install lodash            # 生产依赖
npm install -D vitest         # 开发依赖
npm install -g typescript     # 全局安装
pnpm add lodash
pnpm add -D vitest
yarn add lodash
yarn add --dev vitest
```

---

**基本写法：指定版本安装**
`npm install <包>@<版本>`
```bash
# 版本范围
npm install react@18.2.0
npm install react@"^18.0.0"
npm install react@latest
pnpm add react@18.2.0
yarn add react@18.2.0
```

---

## 卸载与更新

**基本写法：卸载依赖**
`npm uninstall <包>` | `pnpm remove <包>` | `yarn remove <包>`
```bash
npm uninstall lodash
pnpm remove lodash
yarn remove lodash
```

---

**基本写法：更新依赖**
`npm update [<包>]` | `pnpm update [<包>]` | `yarn upgrade [<包>]`
```bash
npm update react
pnpm update react
yarn upgrade react
```

---

## 运行脚本

**基本写法：执行 package.json scripts**
`npm run <脚本>` | `pnpm <脚本>` | `yarn <脚本>`
```bash
# package.json: "scripts": { "dev": "vite" }
npm run dev
pnpm dev          # pnpm 可省略 run
yarn dev          # yarn 也可省略 run
```

---

**基本写法：npx 执行本地命令**
`npx <命令>`
```bash
# 执行 node_modules/.bin 下的命令
npx tsc --noEmit
npx create-vite my-app
pnpm dlx create-vite my-app   # pnpm 等价
yarn dlx create-vite my-app
```

---

## 锁文件与严格安装

**基本写法：按 lock 文件严格安装**
`npm ci` | `pnpm install --frozen-lockfile` | `yarn install --frozen-lockfile`
```bash
# CI 环境推荐，不修改 lock
npm ci
pnpm install --frozen-lockfile
yarn install --frozen-lockfile
```

---

## 工作区 Monorepo

**基本写法：定义工作区**
`<根 package.json>: "workspaces": ["packages/*"]`
```json
{
  "private": true,
  "workspaces": ["packages/*", "apps/*"]
}
```

---

**基本写法：工作区命令**
`npm -w <包> <命令>` | `pnpm --filter <包> <命令>` | `yarn workspace <包> <命令>`
```bash
# 在指定工作区执行
npm -w @a/core run build
pnpm --filter @a/core build
yarn workspace @a/core build
```

---

**基本写法：安装工作区包**
`npm -w <包A> i <包B>` | `pnpm add <包B> --filter <包A>`
```bash
# 给 app 安装内部包
npm -w apps/web i @a/core
pnpm add @a/core --filter apps/web
yarn workspace apps/web add @a/core
```

---

## 查询信息

**基本写法：查看包信息**
`npm view <包> [<字段>]`
```bash
npm view react version
npm view react versions --json
pnpm view react version
```

---

**基本写法：列出依赖树**
`npm ls [<包>]` | `pnpm list` | `yarn list`
```bash
npm ls react
npm ls --depth=1
pnpm why react    # 解释为何依赖
```

---

## 清理与缓存

**基本写法：清理 node_modules**
`rm -rf node_modules` + 重装
```bash
# 彻底重装
rm -rf node_modules package-lock.json
npm install
```

---

**基本写法：缓存管理**
`npm cache clean --force` | `pnpm store prune`
```bash
npm cache clean --force
pnpm store prune
yarn cache clean
```

---

## 发布与镜像

**基本写法：设置镜像源**
`npm config set registry <url>`
```bash
npm config set registry https://registry.npmmirror.com
npm config get registry
pnpm config set registry https://registry.npmmirror.com
```

---

**基本写法：发布包**
`npm publish`
```bash
npm publish           # 发布到 registry
npm publish --access public  # 公开 scoped 包
npm deprecate <包>@<版本> "废弃说明"
```

---

## pnpm 硬链接特性

**基本写法：pnpm 全局存储**
`pnpm config set store-dir <路径>`
```bash
# pnpm 用硬链接复用全局存储，节省磁盘
pnpm config get store-dir
pnpm install   # 自动链接 store
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
| JavaScript 包管理命令速查（npm/pnpm/yarn） | 055-PackageManagerCommands | 本文自身 |
| JavaScript console API 语法速查 | 056-ConsoleAPI | 本文的并列主题 |
