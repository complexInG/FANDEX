# JavaScript 事件循环机制

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 调用栈与堆

**基本写法：调用栈执行同步代码**
`<函数调用>`
```javascript
// 同步代码按调用栈后进先出执行
function a() { b(); }
function b() { console.log("done"); }
a();
```

---

## 宏任务与微任务

**基本写法：微任务队列**
`queueMicrotask(<回调>)`
```javascript
// 微任务在当前宏任务结束后立即执行
queueMicrotask(() => console.log("micro"));
```

---

**基本写法：宏任务队列**
`setTimeout(<回调>, <延迟>)`
```javascript
// 宏任务在下一次事件循环执行
setTimeout(() => console.log("macro"), 0);
```

---

**基本写法：微任务优先于宏任务**
`Promise.resolve().then(<回调>)`
```javascript
// then 回调作为微任务先于 setTimeout 执行
Promise.resolve().then(() => console.log("micro"));
setTimeout(() => console.log("macro"), 0);
```

---

## 事件循环阶段

**基本写法：Node.js 事件循环阶段**
`timers -> pending -> poll -> check -> close callbacks`
```javascript
// timers 执行 setTimeout setInterval
// check 执行 setImmediate
// poll 执行 I/O 回调
setTimeout(() => {}, 0);     // timers 阶段
setImmediate(() => {});      // check 阶段
```

---

**基本写法：浏览器事件循环**
`执行脚本 -> 微任务 -> requestAnimationFrame -> 渲染 -> 宏任务`
```javascript
// 浏览器每个宏任务后清空微任务队列
console.log("script");
setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("promise"));
```

---

## process.nextTick

**基本写法：nextTick 优先级最高**
`process.nextTick(<回调>)`
```javascript
// Node.js 中 nextTick 早于微任务执行
process.nextTick(() => console.log("nextTick"));
Promise.resolve().then(() => console.log("promise"));
```

---

## async await 转换

**基本写法：await 转为 then 链**
`await <promise>`
```javascript
// await 之后的代码相当于 then 回调作为微任务
async function fn() {
    console.log(1);
    await Promise.resolve();
    console.log(3);
}
fn();
console.log(2);  // 输出顺序 1 2 3
```

---

## 任务队列实战

**基本写法：输出顺序判断**
`<同步> -> <微任务> -> <宏任务>`
```javascript
// 经典执行顺序示例
console.log("start");
setTimeout(() => console.log("timeout"));
Promise.resolve().then(() => console.log("promise"));
console.log("end");
// 输出顺序 start end promise timeout
```

---

**基本写法：嵌套微任务**
`<微任务>.then(<回调>)`
```javascript
// 微任务中产生的微任务在同一阶段清空
Promise.resolve()
    .then(() => Promise.resolve())
    .then(() => console.log("nested"));
```

---

**基本写法：宏任务嵌套**
`setTimeout(() => setTimeout(<回调>))`
```javascript
// 宏任务中产生的宏任务进入下一轮循环
setTimeout(() => {
    setTimeout(() => console.log("inner"));
}, 0);
```

---

## requestAnimationFrame

**基本写法：rAF 在渲染前执行**
`requestAnimationFrame(<回调>)`
```javascript
// rAF 在浏览器重绘前调用适合动画
requestAnimationFrame(() => console.log("rAF"));
```

---

**基本写法：rAF 与 setTimeout 区别**
`requestAnimationFrame(<回调>)`
```javascript
// rAF 同步浏览器刷新率通常 60fps
let start = performance.now();
requestAnimationFrame(t => console.log(t - start));
```

---

## 任务拆分

**基本写法：长任务拆分**
`setTimeout(<回调>, 0)`
```javascript
// 拆分长任务避免阻塞主线程
function chunk(tasks) {
    if (tasks.length === 0) return;
    const task = tasks.shift();
    task();
    setTimeout(() => chunk(tasks), 0);
}
```

---

**基本写法：使用 scheduler.yield**
`await scheduler.yield()`
```javascript
// ES2024+ 让出主线程继续执行后续代码
async function work() {
    for (const item of items) {
        process(item);
        await scheduler.yield();
    }
}
```

---

## MessageChannel

**基本写法：MessageChannel 创建宏任务**
`new MessageChannel()`
```javascript
// MessageChannel 端口通信是宏任务
const { port1, port2 } = new MessageChannel();
port1.onmessage = () => console.log("received");
port2.postMessage(null);
```

---

## 异步执行顺序

**基本写法：综合执行顺序**
`<script> -> <micro> -> <macro>`
```javascript
// 同步代码 -> 微任务 -> 宏任务 -> 渲染
console.log(1);
setTimeout(() => console.log(2));
Promise.resolve().then(() => console.log(3));
queueMicrotask(() => console.log(4));
console.log(5);
// 输出 1 5 3 4 2
```

---

## 浏览器渲染时机

**基本写法：渲染与任务交错**
`<宏任务> -> <微任务> -> <rAF> -> <渲染>`
```javascript
// 一帧内执行顺序宏任务清空微任务 rAF 渲染
setTimeout(() => console.log("task"));
requestAnimationFrame(() => console.log("rAF"));
Promise.resolve().then(() => console.log("micro"));
```

---

## 实用模式

**基本写法：nextTick 工具函数**
`Promise.resolve().then(<回调>)`
```javascript
// 浏览器实现 nextTick 等同微任务
const nextTick = fn => Promise.resolve().then(fn);
nextTick(() => console.log("next tick"));
```

---

**基本写法：立即 resolved Promise**
`Promise.resolve().then(<回调>)`
```javascript
// 已 resolved 的 then 仍是异步微任务
Promise.resolve().then(() => console.log("async"));
console.log("sync");
```
