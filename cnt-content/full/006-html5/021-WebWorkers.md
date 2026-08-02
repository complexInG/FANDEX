---
order: 210
title: Web-Workers
module: 'html5'
category: 前端技术
difficulty: advanced
description: Web Workers
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/019-DragAPI'
  - 'html5/020-Geolocation'
  - 'html5/022-ServiceWorkerPWA'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：别让“重活”堵住页面

想象你在页面上点了一个“计算”按钮，页面立刻卡住、按钮点不动、动画停摆——因为 JS 是单线程的，长时间运算会阻塞界面。

Web Worker 就是“雇一个帮手在后台干重活”：主线程负责界面交互，Worker 负责密集计算，两边用消息通信。需要注意：Worker 里没有 DOM，不能直接操作页面元素。

## 内联 Worker

**通过 Blob 创建内联 Worker**
```javascript
const code = `
  self.onmessage = (e) => {
    const result = e.data.reduce((s, n) => s + n * n, 0);
    self.postMessage(result);
  };
`;
const blob = new Blob([code], { type: 'application/javascript' });
const worker = new Worker(URL.createObjectURL(blob));

worker.postMessage([1, 2, 3, 4, 5]);
worker.onmessage = (e) => console.log('结果:', e.data);
```

**讲解：**

- 内联 Worker 把代码写成字符串，用 `Blob` + `URL.createObjectURL` 生成 Worker 脚本；
- 适合“小段逻辑不想单独建文件”的场景（如演示、单文件页面）；
- `reduce` 在主线程之外的 Worker 中执行，页面不会卡顿。

---

## 1. Web Workers 概述

Web Workers 允许在后台线程中运行 JavaScript，避免 CPU 密集型任务阻塞主线程。

| 特性         | 主线程 | Worker 线程 |
| ------------ | ------ | ----------- |
| DOM 访问     | 支持   | 不支持      |
| 网络请求     | 支持   | 支持（fetch/XHR） |
| IndexedDB    | 支持   | 支持        |
| localStorage | 支持   | 不支持      |

## 2. Dedicated Worker

**主线程**：

```javascript
const worker = new Worker('worker.js');
worker.postMessage({ type: 'CALCULATE', data: [1, 2, 3, 4, 5] });
worker.onmessage = (e) => console.log('Worker 返回:', e.data);
worker.onerror = (e) => console.error('Worker 错误:', e.message);
worker.terminate();
```

**讲解：**

- `new Worker('worker.js')` 创建专用 Worker，`postMessage` 发送任务；
- `onmessage` 接收结果，`onerror` 捕获错误，`terminate()` 立即终止；
- Worker 与主线程通过结构化克隆传递数据，不能共享 DOM 与全局变量。

**Worker 线程（worker.js）**：

```javascript
self.onmessage = (e) => {
  const { type, data } = e.data;
  if (type === 'CALCULATE') {
    const result = data.reduce((sum, n) => sum + n * n, 0);
    self.postMessage({ type: 'RESULT', data: result });
  }
};
```

**讲解：**

- Worker 内用 `self` 指代全局对象，`self.onmessage` 接收消息；
- 消息内容按 `type` 区分任务类型，处理完用 `self.postMessage` 回传；
- 长时间循环放在这里执行，UI 保持流畅。

### Transferable Objects

```javascript
const buffer = new ArrayBuffer(1024 * 1024);
worker.postMessage({ buffer }, [buffer]); // 零拷贝传输
```

**讲解：**

- 第二个参数是“转移列表”：把 `ArrayBuffer` 的所有权转移给 Worker，零拷贝；
- 转移后主线程不能再使用该 buffer，适合大文件、图像数据处理；
- 普通对象传递会序列化复制，大数据场景用 Transferable 更高效。

## 3. Shared Worker

```javascript
const worker = new SharedWorker('shared-worker.js');
worker.port.start();
worker.port.postMessage('Hello');
worker.port.onmessage = (e) => console.log('收到:', e.data);
```

**讲解：**

- `SharedWorker` 可被多个页面共享，通信必须通过 `port`（端口）；
- `port.start()` 激活端口，`postMessage`/`onmessage` 都在 `port` 上；
- 共享 Worker 适合“多个标签页共享一个数据源”的场景。

## 4. Worker 池

```javascript
class WorkerPool {
  constructor(workerScript, poolSize = navigator.hardwareConcurrency) {
    this.workers = Array.from({ length: poolSize }, () => new Worker(workerScript));
  }
  execute(data) {
    return new Promise((resolve) => {
      const worker = this.workers.pop();
      worker.onmessage = (e) => {
        resolve(e.data);
        this.workers.push(worker);
      };
      worker.postMessage(data);
    });
  }
  terminate() {
    this.workers.forEach((w) => w.terminate());
  }
}
```

**讲解：**

- Worker 池预创建多个 Worker，任务来时取空闲 Worker 执行，执行完归还；
- `navigator.hardwareConcurrency` 返回 CPU 逻辑核心数，可作为池大小参考；
- 避免“每个任务新建 Worker”的开销，适合批量密集计算。

## 5. 进阶知识点

### 5.1 MessageChannel 双向通信

```javascript
const channel = new MessageChannel();
const worker1 = new Worker('worker1.js');
const worker2 = new Worker('worker2.js');

// 把两个端口分别转移给两个 Worker
worker1.postMessage({ port: channel.port1 }, [channel.port1]);
worker2.postMessage({ port: channel.port2 }, [channel.port2]);
```

**讲解：**

- `MessageChannel` 创建一条双向通道，`port1`/`port2` 是通道两端；
- 把端口转移给 Worker 后，两个 Worker 可直接互相通信，无需主线程中转；
- 端口转移使用 Transferable 列表（第二个参数），转移后主线程不再持有。

### 5.2 BroadcastChannel 广播

```javascript
const bc = new BroadcastChannel('app-updates');
bc.postMessage('数据已更新');
bc.onmessage = (e) => console.log('收到广播:', e.data);
```

**讲解：**

- `BroadcastChannel` 实现同源页面间的消息广播，所有监听同一频道的页面都能收到；
- 适合“一个标签页修改数据，其它标签页同步刷新”的场景；
- 与 `storage` 事件相比，它不限于存储变化，通用性更强。

### 5.3 Worker 中可用的 API

| API | Worker 中是否可用 |
| --- | --- |
| `fetch`/XHR | 可用 |
| `IndexedDB` | 可用 |
| `setTimeout`/`setInterval` | 可用 |
| `WebSocket` | 可用 |
| `localStorage`/`sessionStorage` | 不可用 |
| DOM / `window` / `document` | 不可用 |

## 6. 动手试试

### 入门版（必做）

1. 写一个页面：点击按钮后执行 1 亿次循环求和，先在主线程跑一次（观察卡顿），再用 Worker 跑一次（观察流畅）；
2. 在 Worker 中计算一组数字的平方和，把结果发回主线程显示；
3. 在主线程用 `postMessage` 传递对象，Worker 处理后回传。

### 进阶版（选做）

1. 用 Transferable 把大 `ArrayBuffer` 转移给 Worker 处理，对比普通拷贝的耗时；
2. 实现一个 Worker 池，并行计算 100 个任务；
3. 用 `BroadcastChannel` 让两个标签页同步“计数”状态。

## 7. 核心知识点

> 一句话记住 Worker：主线程管界面，Worker 管计算；`postMessage` 通信，`terminate` 善后；DOM 不能碰，Transferable 可提速。

- `new Worker(url)` 创建后台线程，`postMessage`/`onmessage` 收发消息；
- Worker 无 DOM 权限，适合计算、图像处理、数据解析等重活；
- `SharedWorker` 多页面共享，需通过 `port` 通信；
- Worker 池复用线程，避免频繁创建销毁的开销；
- `MessageChannel` 让 Worker 之间直接通信，`BroadcastChannel` 做页面广播；
- 不再使用时 `terminate()` 释放资源。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| Worker 里操作 DOM | 直接报错 | 计算完 `postMessage` 回主线程渲染 |
| 频繁创建/销毁 Worker | 启动开销大 | 使用 Worker 池复用 |
| 忘记 `terminate` | 线程与内存泄漏 | 任务完成或页面卸载时终止 |
| 大对象普通传递 | 序列化复制耗时 | 用 Transferable 转移所有权 |
| SharedWorker 忘记 `start()` | 消息收不到 | 创建后调用 `port.start()` |
| Worker 报错无监听 | 静默失败难排查 | 注册 `onerror` 统一处理 |

## 9. 扩展学习

- 离线场景：`html5/022-ServiceWorkerPWA` 中 Service Worker（Worker 家族的一员）；
- 数据缓存：`html5/008-HTML5OfflineStorageWebAPI` 中 Worker 与 IndexedDB 的配合；
- 性能：`javascript/047-DebugPerformanceOptimization` 用性能面板分析主线程任务；
- 并发模式：`javascript/035-AsyncConcurrencyControl` 对比异步任务与 Worker 的取舍。
