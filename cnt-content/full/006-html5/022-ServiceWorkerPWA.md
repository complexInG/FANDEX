---
order: 220
title: Service-Worker与PWA
module: 'html5'
category: 前端技术
difficulty: advanced
description: Service Worker与PWA
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/020-Geolocation'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：断网也能打开的“网页 App”

坐地铁时信号不好，很多网页 App 依然能打开、能浏览——靠的就是 Service Worker：一个独立于页面的“后台脚本”，提前把资源缓存下来，网络请求先经过它。

它和普通 Worker 的区别：普通 Worker 是“帮手”，Service Worker 是“门卫”——所有网络请求都要先经过它，它决定放行（网络）、给缓存，还是先给缓存再后台更新。

## 1. Service Worker 概述

Service Worker 是浏览器后台独立于网页运行的脚本，充当网络代理，支持离线缓存、推送通知和后台同步。

**生命周期**：Installing → Installed(Waiting) → Activating → Activated → Redundant

```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('/sw.js', { scope: '/' })
    .then((reg) => console.log('注册成功'))
    .catch((err) => console.error('注册失败:', err));
}
```

**讲解：**

- 注册前先判断 `'serviceWorker' in navigator`，避免旧浏览器报错；
- `register('/sw.js', { scope: '/' })` 的路径决定控制范围，`/` 表示整个站点；
- 注册不立即生效：首次加载页面不受控，需要刷新一次（或 `clients.claim()`）后才接管。

## 2. 生命周期事件

```javascript
const CACHE_NAME = 'app-v1';
const CACHE_URLS = ['/', '/index.html', '/styles.css', '/app.js'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches
      .open(CACHE_NAME)
      .then((cache) => cache.addAll(CACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((names) =>
        Promise.all(names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n)))
      )
      .then(() => self.clients.claim())
  );
});
```

**讲解：**

- `install`：安装时预缓存核心资源，`waitUntil` 保证缓存完成；`skipWaiting()` 让新版本立即激活；
- `activate`：激活时删除旧版本缓存，`clients.claim()` 让已打开的页面立即受控；
- 版本升级流程：改 `CACHE_NAME`（如 `app-v2`）→ 新 SW 安装 → 激活清理旧缓存。

## 3. 缓存策略

| 策略                       | 说明                   | 适用场景   |
| -------------------------- | ---------------------- | ---------- |
| **Cache First**            | 优先缓存               | 静态资源   |
| **Network First**          | 优先网络               | API 请求   |
| **Stale While Revalidate** | 缓存即时响应，后台更新 | 非关键 API |

```javascript
// Cache First
self.addEventListener('fetch', (event) => {
  event.respondWith(caches.match(event.request).then((cached) => cached || fetch(event.request)));
});
```

**讲解：**

- Cache First：命中缓存直接返回，适合哈希命名的静态资源；
- 上面是精简版（不写回缓存），生产版需要在网络响应后 `clone()` 并 `cache.put`；
- API 请求建议 Network First，保证数据新鲜；非关键数据用 Stale While Revalidate。

## 4. PWA 基础

```json
{
  "name": "我的应用",
  "short_name": "我的App",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#1976d2",
  "icons": [{ "src": "/icons/192.png", "sizes": "192x192", "type": "image/png" }]
}
```

**讲解：**

- `name`/`short_name` 是应用名，`start_url` 是安装后打开的地址；
- `display: "standalone"` 让应用以独立窗口运行，不显示浏览器地址栏；
- `theme_color` 与图标（`icons`）决定安装后的外观，配合 `<link rel="manifest">` 使用。

## 5. 推送通知与后台同步

```javascript
// 推送通知
self.addEventListener('push', (event) => {
  const data = event.data?.json() ?? { title: '新消息' };
  event.waitUntil(self.registration.showNotification(data.title, { body: data.body }));
});

// 后台同步
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-data') event.waitUntil(syncData());
});
```

**讲解：**

- `push` 事件在服务器推送到达时触发，用 `showNotification` 展示通知；
- `sync` 事件在网络恢复后触发，适合补发离线时未完成的请求；
- 推送需要 VAPID 密钥与订阅流程（`PushManager.subscribe`），后台同步是实验性能力，两者都需要服务器配合。

## 6. 进阶知识点

### 6.1 Clients API：与页面通信

```javascript
// 在 Service Worker 中获取所有页面客户端
const clients = await self.clients.matchAll({ includeUncontrolled: true, type: 'window' });

// 向所有页面发送消息（如“新版本已就绪”）
clients.forEach((client) => client.postMessage({ type: 'UPDATE' }));

// 打开新窗口
await self.clients.openWindow('https://example.com');
```

**讲解：**

- `clients.matchAll` 获取受控的页面列表，`type: 'window'` 只取标签页；
- `postMessage` 通知页面“缓存已更新”，页面收到后可提示用户刷新；
- `openWindow` 可从推送通知点击事件中打开指定页面。

## 7. 动手试试

### 入门版（必做）

1. 在本地静态服务器（如 `npx serve`）上注册 Service Worker，缓存首页与 CSS；
2. 打开浏览器开发者工具，在 Network 面板勾选 Offline，刷新页面确认仍能打开；
3. 修改缓存版本号（`app-v2`），确认旧缓存被清理。

### 进阶版（选做）

1. 实现 Network First 的 API 缓存策略，断网时返回最后一次成功的数据；
2. 用 `clients.matchAll` 在 SW 更新后通知页面弹“有新版本，点击刷新”；
3. 配合 Web App Manifest 让页面可安装到桌面。

## 8. 核心知识点

> 一句话记住 Service Worker：注册在页面，脚本管缓存；install 预存，activate 清理，fetch 拦截请求；HTTPS 才能用。

- Service Worker 是独立于页面的网络代理脚本，支持离线、推送、后台同步；
- 生命周期：install（预缓存）→ activate（清旧缓存）→ fetch（拦截请求）；
- 缓存策略：Cache First（静态资源）、Network First（API）、Stale While Revalidate（非关键数据）；
- Manifest 让网页可安装：`name`/`start_url`/`display`/`icons`；
- 只在 HTTPS 或 localhost 下生效，更新后通常需要刷新两次；
- Clients API 用于 SW 与页面通信。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 缓存无版本管理 | 更新后用户永远拿旧资源 | 版本化缓存名 + activate 清理 |
| 缓存 API 响应 | 数据过期 | API 用 Network First 或加过期时间 |
| 忘记 `clone()` | 响应体只能消费一次，写入缓存报错 | 写入前 `response.clone()` |
| 页面未受控 | 注册后首次刷新仍走网络 | `clients.claim()` 或提示刷新 |
| 缓存了不该缓存的页面 | 登录态等敏感内容被离线保存 | 只缓存公共静态资源 |
| 本地 http 测试失败 | SW 只在 HTTPS/localhost 生效 | 使用 localhost 或本地 HTTPS |

## 10. 扩展学习

- 基础铺垫：`html5/008-HTML5OfflineStorageWebAPI` 的 Cache Storage 与离线章节；
- 组件对比：`html5/018-WebComponentsPWADevelopment` 中 PWA 三件套；
- 推送完整流程：Web Push 协议与 VAPID 密钥管理；
- 性能：`javascript/059-CoreWebVitalsAndPerformanceMetrics` 中缓存对加载指标的影响；
- 工程化：Workbox 库封装注册、缓存与更新逻辑。
