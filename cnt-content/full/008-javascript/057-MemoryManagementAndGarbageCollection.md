---
order: 570
title: JavaScript 垃圾回收与内存管理
module: javascript
category: '008-javascript'
difficulty: advanced
description: 用可达性、标记清除、分代回收三个模型讲透 JavaScript 的自动内存管理，并给出写代码时避免内存泄漏的实用清单。
author: fanquanpp
created: '2026-08-02'
updated: '2026-08-02'
related:
  - 'javascript/031-ClosureMemoryLeakOptimization'
  - 'javascript/045-MemoryLeakTroubleshoot'
prerequisites:
  - 'javascript/016-FunctionScopeClosure'
quiz:
  - type: choice
    question: 以下哪种对象会被 JavaScript 引擎判定为"不可达"并回收？
    options:
      - 被全局变量引用的对象
      - 被当前调用栈局部变量引用的对象
      - 只被一个已销毁闭包间接引用、且无任何根可达路径的对象
      - 被 WeakMap 中键引用的对象
    answer: 2
    explanation: 只有从根（全局对象、调用栈等）出发无法到达的对象才会被回收；WeakMap 的键不产生强引用，但值本身仍要看是否可达。
  - type: fill
    question: 标记清除算法分为____与____两个阶段。
    answer: 标记；清除
    hint: 先遍历根标记可达对象，再回收未标记对象。
references:
  - type: documentation
    authors:
      - MDN Contributors
    year: 2026
    title: JavaScript 内存管理
    venue: MDN
    url: https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Memory_management
    accessedDate: '2026-08-02'
  - type: website
    authors:
      - V8 Team
    year: 2026
    title: V8 博客：垃圾回收相关文章
    venue: v8.dev
    url: https://v8.dev/blog
    accessedDate: '2026-08-02'
etymology:
  - term: 垃圾回收
    english: Garbage Collection
    origin: 源于 Lisp 语言 1959 年提出的自动内存管理思想，把"不再使用的对象"比作需要清扫的垃圾。
  - term: 可达性
    english: Reachability
    origin: 图论术语，指从根节点出发能否沿引用边到达某个对象。
estimatedReadingTime: 8
lastReviewed: '2026-08-02'
reviewer: fanquanpp
---

## 一句话理解

JavaScript 的内存管理 = 分配内存 + 使用内存 + 自动回收内存。
引擎会定期回收"从根出发再也找不到"的对象，你不需要手动 free，但必须理解什么算"找不到"。

## 为什么需要了解

- 自动回收不等于零内存问题：事件监听、定时器、闭包都可能悄悄把对象"养"到老。
- 排查卡顿和内存暴涨时，先能说清"哪些对象是活的、谁在引用它"，才能定位泄漏。
- 面试常问的 WeakMap/WeakSet、闭包泄漏、内存快照，全部建立在可达性模型上。

## 核心概念：可达性

引擎把一组对象当作"根（roots）"：

- 全局对象（浏览器里的 `window`）
- 当前正在执行的函数调用栈上的变量
- 被模块级变量长期持有的引用

从根出发，沿着对象的引用链能访问到的对象就是**可达的**，必须保留；访问不到的，就是垃圾。

```javascript
// 例：闭包为什么可能造成泄漏
function createHolder() {
  const bigData = new Array(1e6).fill('x'); // 大对象
  return () => console.log('hold'); // 闭包不引用 bigData，但词法环境整体被保留
}
const holder = createHolder(); // 闭包被全局变量 holder 长期持有
// bigData 是否存活？取决于引擎是否做"闭包变量分析"，
// 保险做法：不用的大对象不要放在被长期持有的闭包作用域里。
```

## 标记清除：最基础的算法

1. **标记**：从根出发，深度遍历所有引用，给可达对象打标记。
2. **清除**：扫描堆，回收没有标记的对象，并清掉标记供下一轮使用。

```javascript
let a = { name: 'alive' }; // 可达：被变量 a 引用
let b = { name: 'dead' };
a = null; // { name: 'alive' } 仍然可达吗？不，a 现在指向 null
// 此时 { name: 'alive' } 与 { name: 'dead' } 都不可达，等待回收
```

## 分代回收：V8 的工程化改进

对象按存活时间分到两代：

| 代 | 特点 | 回收策略 |
| --- | --- | --- |
| 新生代 | 大部分对象朝生暮死 | Scavenger：复制存活对象到新空间，回收快 |
| 老生代 | 经历过多次回收仍存活 | 标记-压缩：标记后把存活对象搬移紧凑，减少碎片 |

对象从新生代"晋升"到老生代的阈值是启发式的。作为应用开发者，你不需要记住具体参数，
但要明白：**频繁创建大量临时对象会增加 GC 压力**，表现为卡顿。

## 写代码时的实用清单

- 全局变量是隐式根，能少则少；模块内部状态用局部作用域管理。
- 事件监听、`setInterval`、`ResizeObserver` 等用完要解绑/清除。
- 缓存场景优先 `WeakMap` / `WeakSet`：键不产生强引用，键被回收时条目自动消失。
- 大对象不需要立刻释放，但要避免被"看起来没用的闭包"长期持有。

```javascript
// 弱引用缓存的正确姿势
const cache = new WeakMap();

function process(el) {
  if (!cache.has(el)) {
    cache.set(el, expensiveCompute(el));
  }
  return cache.get(el);
}
// el 从 DOM 移除后，WeakMap 条目不阻碍 el 回收
```

## 常见误解

| 误解 | 真相 |
| --- | --- |
| 闭包一定会内存泄漏 | 只有闭包被长期持有且作用域里藏着大对象才会 |
| 手动置 null 是必须的 | 现代引擎按可达性回收，置 null 只在你主动切断引用时有意义 |
| 内存占用高就是泄漏 | 缓存、池化、长列表都合法占用内存；泄漏是"无引用却无法回收"或"持续增长" |
| `WeakMap` 值不会泄漏 | 值本身仍被强引用，只有键是弱引用 |

## 小结

把"内存管理"翻译成三个问题：谁是根？谁可达？谁在引用它？
回答清楚这三个问题，大部分泄漏问题都能自己定位。
下一步建议阅读 [闭包的内存泄露与优化](/FANDEX/javascript/031-ClosureMemoryLeakOptimization/) 与
[内存泄漏排查](/FANDEX/javascript/045-MemoryLeakTroubleshoot/) 实战篇。
