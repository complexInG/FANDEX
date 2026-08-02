---
order: 240
title: WebSocket
module: 'html5'
category: 前端技术
difficulty: intermediate
description: WebSocket
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/022-ServiceWorkerPWA'
  - 'html5/026-MicrodataJSONLD'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：聊天室里的“电话线”

HTTP 像“寄信”：每次都要你发一封信（请求），服务器才回一封信（响应），服务器不能主动给你写信。WebSocket 像“打电话”：连接建立后，双方随时都能说话，服务器有新消息可以直接推给你。

所以聊天、实时行情、在线协作、游戏同步都优先用 WebSocket。它的代价是连接需要保持（占用资源），断线了还要自己重连。

## 1. WebSocket 概述

| 特性       | HTTP      | WebSocket |
| ---------- | --------- | --------- |
| 通信模式   | 请求-响应 | 全双工    |
| 连接       | 短连接    | 持久连接  |
| 服务器推送 | 不支持，只能轮询 | 原生支持 |

**讲解：** HTTP 是“请求-响应”的短连接，服务器无法主动推送；WebSocket 是持久化的全双工通道，双向随时通信。HTTP 适合普通页面与 API，实时场景用 WebSocket。

## 2. WebSocket API

```javascript
const ws = new WebSocket('wss://example.com/chat');

ws.onopen = () => {
  console.log('连接已建立');
  ws.send('Hello!');
};
ws.onmessage = (e) => {
  console.log('收到消息:', e.data);
};
ws.onclose = (e) => {
  console.log('连接关闭:', e.code);
};
ws.onerror = () => {
  console.error('WebSocket 错误');
};
```

**讲解：**

- `new WebSocket('wss://...')` 建立连接，`wss://` 是加密版本（生产必用）；
- `onopen` 连接建立后发送数据，`onmessage` 接收服务器消息；
- `onclose`/`onerror` 处理关闭与异常，`readyState` 可查询连接状态。

### 连接状态

| readyState | 常量       | 说明       |
| ---------- | ---------- | ---------- |
| 0          | CONNECTING | 正在连接   |
| 1          | OPEN       | 连接已建立 |
| 2          | CLOSING    | 正在关闭   |
| 3          | CLOSED     | 已关闭     |

### 发送与关闭

```javascript
ws.send('文本消息');
ws.send(JSON.stringify({ type: 'chat', content: '你好' }));
ws.send(new ArrayBuffer(4));
ws.close(1000, '正常关闭');
```

**讲解：** `send` 支持文本、JSON 字符串与二进制（`ArrayBuffer`）；`close(code, reason)` 主动关闭，1000 表示正常关闭，业务错误可用 4000-4999 自定义码。

## 3. 断线重连

```javascript
class ReconnectingWebSocket {
  constructor(url, options = {}) {
    this.url = url;
    this.retries = 0;
    this.options = { reconnectInterval: 1000, ...options };
    this.connect();
  }
  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = (e) => {
      this.retries = 0;
      this.onopen?.(e);
    };
    this.ws.onmessage = (e) => this.onmessage?.(e);
    this.ws.onclose = (e) => {
      this.onclose?.(e);
      const delay = Math.min(this.options.reconnectInterval * Math.pow(1.5, this.retries), 30000);
      this.retries++;
      setTimeout(() => this.connect(), delay);
    };
  }
  send(data) {
    if (this.ws?.readyState === WebSocket.OPEN) this.ws.send(data);
  }
  close() {
    this.retries = Infinity;
    this.ws?.close();
  }
}
```

**讲解：**

- 断线后在 `onclose` 中按“指数退避”延迟重连：间隔 1 秒起步、1.5 倍递增、最长 30 秒；
- `retries` 归零逻辑让恢复连接后回到最短间隔；
- 关闭时把 `retries` 设为无限大，避免 `close()` 后仍自动重连。

## 4. 心跳机制

```javascript
setInterval(() => {
  if (ws.readyState === WebSocket.OPEN) ws.send(JSON.stringify({ type: 'ping' }));
}, 30000);
```

**讲解：** 中间设备（代理、负载均衡）会回收静默连接，客户端定时发送 `ping` 让连接保持活跃；服务器应回复 `pong`，连续未收到回复就主动重连。间隔通常 30-60 秒。

## 5. 进阶知识点

### 5.1 SSE：单向推送的轻量方案

```javascript
const eventSource = new EventSource('/api/events');
eventSource.onmessage = (e) => {
  console.log('收到事件:', e.data);
};
eventSource.addEventListener('update', (e) => {
  console.log('自定义事件:', e.data);
});
eventSource.close();
```

**讲解：**

- SSE 是“服务器到客户端”的单向推送，基于普通 HTTP，自动重连；
- 适合新闻流、通知、日志等单向场景；聊天等双向场景仍需 WebSocket；
- WebSocket 双向、支持二进制；SSE 单向、只支持文本，但实现简单。

| 特性 | WebSocket | SSE |
| --- | --- | --- |
| 通信方向 | 双向 | 服务器到客户端 |
| 协议 | ws/wss | HTTP |
| 自动重连 | 需手动实现 | 内置 |
| 二进制 | 支持 | 不支持 |

## 6. 动手试试

### 入门版（必做）

先复制下面这个最小示例到本地 `ws.html`，双击打开即可连接公开回显服务：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>WebSocket 最小示例</title>
  </head>
  <body>
    <button id="send">发送 Hello</button>
    <pre id="log"></pre>
    <script>
      const log = document.getElementById('log');
      const ws = new WebSocket('wss://echo.websocket.org');
      ws.onopen = () => (log.textContent += '连接已建立\n');
      ws.onmessage = (e) => (log.textContent += '收到: ' + e.data + '\n');
      ws.onerror = () => (log.textContent += '连接出错\n');
      document.getElementById('send').onclick = () => {
        ws.send('Hello!');
      };
    </script>
  </body>
</html>
```

1. 用公开的 WebSocket 回显服务（如 wss://echo.websocket.org）连接，发送消息并接收回显；
2. 在页面显示连接状态（`readyState`）与收发日志；
3. 断开网络（开发者工具 Offline），观察 `onclose` 触发。

### 进阶版（选做）

1. 实现带指数退避的自动重连，并显示重连次数；
2. 加心跳：每 30 秒发 `ping`，收到 `pong` 才继续；
3. 用 SSE 订阅一个公开事件流，对比与 WebSocket 的体验差异。

## 7. 核心知识点

> 一句话记住 WebSocket：`new WebSocket` 建连接，`onmessage` 收消息，`send` 发消息；断线重连加心跳，生产必用 `wss://`。

- WebSocket 是持久化全双工通道，服务器可主动推送；
- 四个事件：`onopen`/`onmessage`/`onclose`/`onerror`；
- `readyState`：CONNECTING/OPEN/CLOSING/CLOSED；
- `send` 支持文本、JSON、二进制；`close(code, reason)` 主动关闭；
- 断线重连 + 心跳是生产环境的标配；
- 单向推送可考虑 SSE，双向实时才用 WebSocket。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 使用 `ws://` | 明文传输，数据可被窃听 | 生产环境统一 `wss://` |
| 无重连逻辑 | 断线后连接永久失效 | 实现指数退避重连 |
| 无心跳 | 中间设备回收静默连接 | 定时 ping/pong |
| 不处理粘包/顺序 | 消息可能乱序或合并 | 消息带 id/seq，客户端排序 |
| 连接数不回收 | 资源泄漏 | 页面卸载时 `close()` |
| 广播无权限校验 | 任何人可发消息 | 服务端鉴权 + 消息校验 |

## 9. 扩展学习

- 实时传输：`html5/025-WebRTC` 对比 WebSocket 与点对点媒体流；
- 服务端：Node.js 的 `ws` 库与 Socket.IO 的使用；
- 消息格式：JSON 协议设计（type/payload）与错误码约定；
- 性能：`javascript/059-CoreWebVitalsAndPerformanceMetrics` 中长连接对资源的影响。
