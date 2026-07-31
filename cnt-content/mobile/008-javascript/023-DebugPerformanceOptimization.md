# JavaScript 调试与性能优化 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## console API

**基本写法：分类输出**
`console.<方法>(<内容>)`
```javascript
// 不同级别日志
console.log("info"); console.warn("warn"); console.error("err");
```

---

**基本写法：分组输出**
`console.group(<标题>)` | `console.groupEnd()`
```javascript
// 折叠分组日志
console.group("user");
console.log("name", name);
console.groupEnd();
```

---

**基本写法：表格输出**
`console.table(<数据>)`
```javascript
// 以表格形式展示对象数组
console.table([{ id: 1, name: "Tom" }, { id: 2, name: "Jerry" }]);
```

---

**基本写法：计时**
`console.time(<标签>)` | `console.timeEnd(<标签>)`
```javascript
// 测量代码执行时间
console.time("loop");
for (let i = 0; i < 1000; i++) {}
console.timeEnd("loop");
```

---

**基本写法：计数**
`console.count(<标签>)`
```javascript
// 统计调用次数
function fn() { console.count("fn"); }
```

---

**基本写法：断言**
`console.assert(<条件>, <消息>)`
```javascript
// 条件为假才输出错误
console.assert(value > 0, "value must be positive");
```

---

**基本写法：堆栈追踪**
`console.trace(<消息>)`
```javascript
// 输出调用堆栈
function inner() { console.trace("here"); }
```

---

## debugger 断点

**基本写法：debugger 语句**
`debugger`
```javascript
// 代码中插入断点打开开发者工具时暂停
function fn() { debugger; }
```

---

## performance API

**基本写法：性能时间戳**
`performance.now()`
```javascript
// 高精度时间戳精确到微秒
let start = performance.now();
work();
console.log(performance.now() - start);
```

---

**基本写法：标记测量**
`performance.mark(<名称>)`
```javascript
// 标记时间点
performance.mark("start");
work();
performance.mark("end");
performance.measure("duration", "start", "end");
```

---

**基本写法：获取测量结果**
`performance.getEntriesByName(<名称>)`
```javascript
// 读取测量数据
let measures = performance.getEntriesByName("duration");
console.log(measures[0].duration);
```

---

**基本写法：清理条目**
`performance.clearMarks()` | `performance.clearMeasures()`
```javascript
// 清除标记和测量
performance.clearMarks();
performance.clearMeasures();
```

---

## 性能指标

**基本写法：页面加载性能**
`performance.timing`
```javascript
// 读取页面加载各阶段时间
let t = performance.timing;
let loadTime = t.loadEventEnd - t.navigationStart;
```

---

**基本写法：navigationEntry**
`performance.getEntriesByType("navigation")`
```javascript
// 现代方式获取导航性能
let [nav] = performance.getEntriesByType("navigation");
console.log(nav.domContentLoadedEventEnd);
```

---

**基本写法：资源加载**
`performance.getEntriesByType("resource")`
```javascript
// 获取所有资源加载耗时
let resources = performance.getEntriesByType("resource");
resources.forEach(r => console.log(r.name, r.duration));
```

---

**基本写法：Observer 监听**
`new PerformanceObserver(<回调>)`
```javascript
// 监听性能条目产生
let observer = new PerformanceObserver(list => {
    list.getEntries().forEach(entry => console.log(entry));
});
observer.observe({ entryTypes: ["measure", "resource"] });
```

---

## Web Vitals

**基本写法：核心指标**
`new PerformanceObserver(<回调>)`
```javascript
// 监听 LCP 最大内容绘制
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("LCP", e.startTime));
}).observe({ type: "largest-contentful-paint", buffered: true });
```

---

**基本写法：FID 首次输入延迟**
`new PerformanceObserver(<回调>)`
```javascript
// 监听首次交互延迟
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("FID", e.processingStart - e.startTime));
}).observe({ type: "first-input", buffered: true });
```

---

**基本写法：CLS 布局偏移**
`new PerformanceObserver(<回调>)`
```javascript
// 监听布局偏移累计
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("CLS", e.value));
}).observe({ type: "layout-shift", buffered: true });
```

---

## 内存监测

**基本写法：堆快照**
`performance.memory`
```javascript
// Chrome 提供内存使用估算
let mem = performance.memory;
console.log(mem.usedJSHeapSize, mem.totalJSHeapSize);
```

---

**基本写法：垃圾回收触发**
`window.gc && gc()`
```javascript
// 需要启动参数开启强制 GC 调试用
if (window.gc) window.gc();
```

---

## 长任务监测

**基本写法：长任务观察**
`new PerformanceObserver(<回调>)`
```javascript
// 监听超过 50ms 的任务
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("long task", e.duration));
}).observe({ entryTypes: ["longtask"] });
```

---

## requestAnimationFrame

**基本写法：动画帧回调**
`requestAnimationFrame(<回调>)`
```javascript
// 在下次重绘前执行适合动画
function loop() {
    update();
    requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

---

**基本写法：取消动画帧**
`cancelAnimationFrame(<id>)`
```javascript
// 取消动画帧请求
let id = requestAnimationFrame(loop);
cancelAnimationFrame(id);
```

---

## requestIdleCallback

**基本写法：空闲时段执行**
`requestIdleCallback(<回调>)`
```javascript
// 浏览器空闲时执行低优先级任务
requestIdleCallback(deadline => {
    while (deadline.timeRemaining() > 0) doWork();
});
```

---

**基本写法：超时选项**
`requestIdleCallback(<回调>, { timeout: <毫秒> })`
```javascript
// 强制在指定时间内执行
requestIdleCallback(fn, { timeout: 2000 });
```

---

## 长任务拆分

**基本写法：分片处理大数组**
`async function <chunk>(<数组>, <大小>)`
```javascript
// 使用 scheduler.yield 拆分
async function chunk(arr, size) {
    for (let i = 0; i < arr.length; i += size) {
        process(arr.slice(i, i + size));
        await scheduler.yield();
    }
}
```

---

**基本写法：使用 setTimeout 让出**
`setTimeout(<回调>, 0)`
```javascript
// 拆分长任务避免阻塞
function chunk(tasks) {
    if (!tasks.length) return;
    tasks.shift()();
    setTimeout(() => chunk(tasks), 0);
}
```

---

## 错误捕获

**基本写法：全局错误监听**
`window.addEventListener("error", <回调>)`
```javascript
// 捕获同步错误与资源加载失败
window.addEventListener("error", e => {
    console.log(e.message, e.filename);
});
```

---

**基本写法：Promise 未处理拒绝**
`window.addEventListener("unhandledrejection", <回调>)`
```javascript
// 捕获未处理的 Promise 拒绝
window.addEventListener("unhandledrejection", e => {
    console.log(e.reason);
});
```

---

## 调试工具

**基本写法：断点条件**
`if (<条件>) debugger`
```javascript
// 满足条件才触发断点
for (let i = 0; i < 1000; i++) {
    if (i === 500) debugger;
}
```

---

**基本写法：logpoint 调试**
`console.log(<变量>)`
```javascript
// 使用浏览器 logpoint 不污染代码
// 在 Sources 面板设置行号日志
```

---

## 网络调试

**基本写法：fetch 包装日志**
`function <fetchLog>(<url>, <选项>)`
```javascript
// 包装 fetch 记录请求耗时
async function fetchLog(url, opts) {
    let start = performance.now();
    let res = await fetch(url, opts);
    console.log(url, performance.now() - start);
    return res;
}
```

---

## 性能优化策略

**基本写法：防抖节流**
`<节流>(<回调>, <等待>)`
```javascript
// 限制高频事件触发频率
window.addEventListener("scroll", throttle(fn, 100));
```

---

**基本写法：事件委托**
`<父节点>.addEventListener(<事件>, <回调>)`
```javascript
// 减少监听器数量
list.addEventListener("click", e => {});
```

---

**基本写法：虚拟列表**
`<容器>.addEventListener("scroll", <节流>(<回调>))`
```javascript
// 大列表只渲染可见项
function renderVisible(start, end) {
    container.innerHTML = items.slice(start, end).map(render).join("");
}
```

---

**基本写法：IntersectionObserver 懒加载**
`new IntersectionObserver(<回调>)`
```javascript
// 图片进入视口才加载
let io = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) { e.target.src = e.target.dataset.src; io.unobserve(e.target); }
    });
});
imgs.forEach(img => io.observe(img));
```

---

## 内存优化

**基本写法：解除引用**
`<变量> = null`
```javascript
// 不再使用的大对象置 null 利于 GC
let bigData = loadData();
process(bigData);
bigData = null;
```

---

**基本写法：WeakMap 弱引用**
`new WeakMap()`
```javascript
// 弱引用键不影响垃圾回收
let cache = new WeakMap();
cache.set(obj, data);
```

---

**基本写法：对象池复用**
`function <pool>(<工厂>)`
```javascript
// 复用对象减少 GC 压力
function pool(factory) {
    let list = [];
    return { get: () => list.pop() || factory(), put: o => list.push(o) };
}
```

---

## 实用工具

**基本写法：性能测量装饰器**
`function <measure>(<函数>)`
```javascript
// 自动测量函数执行时间
function measure(fn, name = fn.name) {
    return function (...args) {
        console.time(name);
        let result = fn.apply(this, args);
        console.timeEnd(name);
        return result;
    };
}
```

---

**基本写法：FPS 监测**
`function <fpsMonitor>()`
```javascript
// 监测动画帧率
function fpsMonitor() {
    let last = performance.now(), frames = 0;
    function loop() {
        frames++;
        let now = performance.now();
        if (now - last >= 1000) {
            console.log("FPS", frames); frames = 0; last = now;
        }
        requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
}
```
