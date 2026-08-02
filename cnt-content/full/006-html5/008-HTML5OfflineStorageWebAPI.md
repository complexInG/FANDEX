---
order: 80
title: HTML5 离线存储与 Web API
module: 'html5'
category: 前端技术
difficulty: intermediate
description: localStorage、sessionStorage、IndexedDB 与 Web Workers。
author: Anonymous
updated: '2026-08-02'
related:
  - 'html5/006-HTML5MultimediaCanvasDrawing'
  - 'html5/007-DocTypeDeclaration'
  - 'html5/009-MetadataCharacterEncoding'
  - 'html5/010-TextSemantic'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 为什么需要离线存储？——生活中的对应物

你有没有遇到过这些场景：网页刷新后，之前填的表单内容没了；关掉标签页，登录状态丢了；网络一断，页面就完全打不开。

HTML5 提供了一组“浏览器本地能力”，可以这样理解：

| 技术 | 生活类比 | 干什么用 |
| --- | --- | --- |
| `localStorage` | 衣柜 | 长期保存，关浏览器也不丢（主题、偏好） |
| `sessionStorage` | 购物车 | 本次会话有效，关标签页就清空（草稿、临时数据） |
| Web Worker | 助手 | 在后台帮你算，不挡住主页面操作 |
| Service Worker | 离线门店 | 网络断了也能开门营业（缓存页面） |
| Fetch API | 快递员 | 从服务器取数据、交数据 |

这节课的目标：学会把数据存在浏览器本地、在后台跑任务、离线也能打开页面。标为“必背”的 API 要熟练掌握，标为“了解”的知道场景即可。

## 1. Web 存储 (Web Storage)

Web Storage 提供了一种在浏览器中存储键值对数据的机制，相比 Cookie 具有更大的容量 (通常为 5MB+) 和更简单的 API。

### 1.1 localStorage

必背。

**特点**：

- 数据永久存储，除非手动清除
- 同一域名下的所有页面共享数据
- 数据不会随 HTTP 请求发送到服务器
  **操作方法**：

```javascript
// 存储数据
localStorage.setItem('name', 'Alice');
localStorage.setItem('age', '30');
// 读取数据
const name = localStorage.getItem('name');
const age = localStorage.getItem('age');
console.log(name, age); // 输出: Alice 30
// 删除数据
localStorage.removeItem('age');
// 清除所有数据
localStorage.clear();
// 遍历所有键值对
for (let i = 0; i < localStorage.length; i++) {
  const key = localStorage.key(i);
  const value = localStorage.getItem(key);
  console.log(`${key}: ${value}`);
}
```

**讲解：**

- `setItem`/`getItem`/`removeItem`/`clear` 是四个核心方法，分别对应增、查、删、清；
- `localStorage` 只能存字符串，数字 `30` 也会被转成字符串 `"30"`；
- `key(i)` 配合 `length` 可遍历全部键值对，但顺序不保证与写入顺序一致；
- 数据按“协议 + 域名 + 端口”隔离，不同站点互不可见。

**存储对象**：
localStorage 只能存储字符串，存储对象需要先序列化：

```javascript
// 存储对象
const user = { name: 'Bob', age: 25, email: 'bob@example.com' };
localStorage.setItem('user', JSON.stringify(user));
// 读取对象
const storedUser = JSON.parse(localStorage.getItem('user'));
console.log(storedUser.name); // 输出: Bob
```

**讲解：**

- `JSON.stringify` 把对象序列化成字符串后才能存储；
- 读取后必须用 `JSON.parse` 还原，直接取回的值会是字符串；
- 解析失败会抛异常，读取用户数据时建议用 `try/catch` 包裹。

### 1.2 sessionStorage

必背。API 与 `localStorage` 相同，差别只在生命周期。

**特点**：

- 数据仅在当前会话 (标签页) 有效，关闭标签页即失效
- 不同标签页之间的数据不共享
- 刷新页面数据仍然保留
  **操作方法**：

```javascript
// 存储数据
sessionStorage.setItem('token', 'abc123');
// 读取数据
const token = sessionStorage.getItem('token');
// 删除数据
sessionStorage.removeItem('token');
// 清除所有数据
sessionStorage.clear();
```

**讲解：**

- `sessionStorage` 与 `localStorage` API 完全一致，差别只在生命周期；
- 数据随标签页会话结束而清除，刷新页面不会丢；
- 同一站点开多个标签页时，各标签页的 `sessionStorage` 相互独立。

### 1.3 Web Storage 与 Cookie 对比

| 特性       | localStorage | sessionStorage | Cookie          |
| ---------- | ------------ | -------------- | --------------- |
| 存储容量   | 约 5MB       | 约 5MB         | 约 4KB          |
| 存储时间   | 永久         | 会话期间       | 可设置过期时间  |
| 服务器发送 | 否           | 否             | 是 (随请求发送) |
| 作用域     | 同一域名     | 同一标签页     | 可设置路径      |
| API 复杂度 | 简单         | 简单           | 复杂            |

### 1.4 使用场景

- **localStorage**：存储用户偏好设置、主题选择、登录状态等需要长期保存的数据
- **sessionStorage**：存储临时会话数据、表单数据、购物车内容等仅在当前会话有效的数据

## 2. 地理定位 (Geolocation API)

了解即可。

Geolocation API 允许网页获取用户的地理位置信息，可用于地图应用、位置服务等场景。

### 2.1 基本用法

```javascript
// 获取当前位置
navigator.geolocation.getCurrentPosition(
  (position) => {
    console.log('纬度: ' + position.coords.latitude);
    console.log('经度: ' + position.coords.longitude);
    console.log('精度: ' + position.coords.accuracy + ' 米');
  },
  (error) => {
    console.error('获取位置失败:', error.message);
  }
);
```

**讲解：**

- `getCurrentPosition` 异步获取位置，成功与失败分别通过两个回调处理；
- 浏览器会弹出授权询问，用户拒绝时进入错误回调；
- `coords.accuracy` 表示精度（米），值越小定位越准，地图应用应优先展示高精度结果。

### 2.2 监听位置变化

```javascript
// 监听位置变化
const watchId = navigator.geolocation.watchPosition(
  (position) => {
    console.log('当前位置:', position.coords.latitude, position.coords.longitude);
  },
  (error) => {
    console.error('获取位置失败:', error.message);
  },
  {
    enableHighAccuracy: true, // 启用高精度模式
    timeout: 5000, // 超时时间
    maximumAge: 0, // 不使用缓存
  }
);
// 停止监听
// navigator.geolocation.clearWatch(watchId);
```

**讲解：**

- `watchPosition` 持续监听位置变化，返回的 `watchId` 用于停止监听；
- `enableHighAccuracy: true` 请求 GPS 等高精度定位，但更耗电；
- `timeout` 限制单次定位耗时，`maximumAge` 允许复用多久内的缓存结果。

### 2.3 位置对象属性

| 属性                      | 描述                            |
| ------------------------- | ------------------------------- |
| `coords.latitude`         | 纬度                            |
| `coords.longitude`        | 经度                            |
| `coords.accuracy`         | 位置精度 (米)                   |
| `coords.altitude`         | 海拔高度 (米)                   |
| `coords.altitudeAccuracy` | 海拔高度精度 (米)               |
| `coords.heading`          | 方向 (度，从正北开始顺时针计算) |
| `coords.speed`            | 速度 (米/秒)                    |
| `timestamp`               | 获取位置的时间戳                |

### 2.4 错误处理

| 错误代码 | 描述               |
| -------- | ------------------ |
| 0        | 未知错误           |
| 1        | 用户拒绝了位置请求 |
| 2        | 位置不可用         |
| 3        | 请求超时           |

### 2.5 使用场景

- 地图应用：显示用户当前位置
- 位置服务：附近的餐厅、商店等
- 导航应用：提供路线规划
- 社交应用：分享位置信息

## 3. Web Workers

了解即可（进阶内容：`Worker` 不能操作 DOM，只能做计算）。

Web Workers 允许在后台线程运行脚本，不阻塞 UI 渲染，适合处理大量计算任务。

### 3.1 基本用法

**创建 Worker**：

```javascript
// main.js
const worker = new Worker('worker.js');
// 发送消息给 Worker
worker.postMessage({ type: 'calculate', data: 1000000 });
// 接收 Worker 消息
worker.onmessage = function (event) {
  console.log('计算结果:', event.data);
};
// 处理错误
worker.onerror = function (error) {
  console.error('Worker 错误:', error);
};
```

**讲解：**

- `new Worker('worker.js')` 创建后台线程，主线程通过 `postMessage` 发送任务；
- `onmessage` 接收 Worker 回传的结果，`onerror` 捕获 Worker 内的异常；
- Worker 与主线程通过“消息”通信，不能直接共享 DOM 和变量。

**Worker 脚本 (worker.js)**：

```javascript
// 接收消息
self.onmessage = function (event) {
  const { type, data } = event.data;
  if (type === 'calculate') {
    // 执行密集计算
    let result = 0;
    for (let i = 0; i < data; i++) {
      result += i;
    }
    // 发送结果
    self.postMessage(result);
  }
};
```

**讲解：**

- Worker 内没有 `window`/`document`，用 `self` 指代全局对象；
- `self.onmessage` 接收主线程消息，`self.postMessage(result)` 回传结果；
- 密集循环在 Worker 中执行时，页面 UI 不会卡顿。

### 3.2 终止 Worker

```javascript
// 终止 Worker
worker.terminate();
```

**讲解：**

- `terminate()` 立即停止 Worker，正在执行的任务也会被中断；
- 任务完成后主动终止可以释放内存与线程资源；
- 需要复用时重新 `new Worker()` 创建即可，Worker 无法重启。

### 3.3 类型

- **Dedicated Workers**：专用 Worker，只能被创建它的脚本使用
- **Shared Workers**：共享 Worker，可以被多个脚本使用
- **Service Workers**：用于离线缓存和后台同步

### 3.4 使用场景

- 密集计算：数学运算、图像处理
- 数据处理：大数据集分析、排序
- 后台任务：文件上传、数据同步

## 4. 离线应用 (Service Workers)

了解即可（PWA 的核心，入门阶段知道“注册 → 缓存 → 拦截请求”三步即可）。

Service Workers 是一种特殊的 Web Worker，用于拦截网络请求、实现离线缓存，是 Progressive Web App (PWA) 的核心技术。

### 4.1 注册 Service Worker

```javascript
// 注册 Service Worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', async () => {
    try {
      const registration = await navigator.serviceWorker.register('/sw.js');
      console.log('Service Worker 注册成功:', registration.scope);
    } catch (error) {
      console.error('Service Worker 注册失败:', error);
    }
  });
}
```

**讲解：**

- 注册前先判断 `'serviceWorker' in navigator`，不支持的环境直接跳过；
- 放在 `load` 事件后注册，避免与首屏关键资源竞争；
- `register('/sw.js')` 的路径决定作用域：`/sw.js` 管理整个站点，子目录脚本只管理该目录。

### 4.2 Service Worker 脚本 (sw.js)

```javascript
 // 缓存名称
 const CACHE_NAME = 'my-cache-v1';
 // 需要缓存的资源
 const urlsToCache = [
  '/',
  '/index.html',
  '/styles.css',
  '/script.js',
  '/images/logo.png'
 ]
 // 安装事件 - 缓存资源
 self.addEventListener('install', (event) => {
  event.waitUntil(
  caches.open(CACHE_NAME)
  .then((cache) => {
  console.log('打开缓存');
  return cache.addAll(urlsToCache);
 })
 );
 });
 // 激活事件 - 清理旧缓存
 self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
  caches.keys().then((cacheNames) => {
  return Promise.all(
  cacheNames.map((cacheName) => {
  if (cacheWhitelist.indexOf(cacheName) === -1) {
  return caches.delete(cacheName);
  }
  })
  );
 })
 );
 });
 // fetch 事件 - 拦截网络请求
 self.addEventListener('fetch', (event) => {
  event.respondWith(
  caches.match(event.request)
  .then((response) => {
  // 如果缓存中有响应，则返回缓存
  if (response) {
  return response;
  }
  // 否则发起网络请求
  return fetch(event.request)
  .then((response) => {
  // 检查响应是否有效
  if (!response || response.status !== 200 || response.type !== 'basic') {
  return response;
  }
  // 克隆响应
  const responseToCache = response.clone();
  // 将响应添加到缓存
  caches.open(CACHE_NAME)
  .then((cache) => {
  cache.put(event.request, responseToCache);
  });
  return response;
  });
 })
 );
 });
```

**讲解：**

- `install` 阶段把核心资源写入缓存，`waitUntil` 保证缓存完成前不中断安装；
- `activate` 阶段删除旧版本缓存，用白名单保留当前版本；
- `fetch` 阶段拦截网络请求：命中缓存直接返回（Cache First），未命中则请求网络并写入缓存；
- 缓存响应必须 `clone()`，因为响应体只能被消费一次；
- Service Worker 只在 HTTPS（或 localhost）下生效，且首次注册后需要刷新两次才能接管页面。

### 4.3 缓存策略

- **Cache First**：优先从缓存获取，无缓存再请求网络
- **Network First**：优先从网络获取，网络失败再从缓存获取
- **Cache Only**：只从缓存获取
- **Network Only**：只从网络获取
- **Stale While Revalidate**：先从缓存获取，同时请求网络更新缓存

### 4.4 使用场景

- 离线应用：即使没有网络也能访问应用
- 性能优化：缓存静态资源，提高加载速度
- 后台同步：在网络可用时同步数据
- 推送通知：即使应用未打开也能收到通知

## 5. Fetch API

必背。现代浏览器请求服务器的标准方式，替代旧的 `XMLHttpRequest`。

Fetch API 是现代化的异步网络请求方案，替代原生的 `XMLHttpRequest`，提供了更简洁、灵活的 API。

### 5.1 基本用法

```javascript
// GET 请求
fetch('https://api.example.com/data')
  .then((response) => {
    if (!response.ok) {
      throw new Error('网络响应失败');
    }
    return response.json();
  })
  .then((data) => {
    console.log('数据:', data);
  })
 .catch((error) => {
  console.error('错误:', error);
  });
```

**讲解：**

- `fetch(url)` 默认发起 GET 请求，返回 Promise；
- `response.ok` 表示 HTTP 状态码是否在 200-299 区间，失败时手动抛错；
- `response.json()` 把响应体解析为对象，`.catch` 统一处理网络与解析错误。

### 5.2 POST 请求

```javascript
 // POST 请求
 fetch('https://api.example.com/users', {
  method: 'POST',
  headers: {
  'Content-Type': 'application/json'
  },
  body: JSON.stringify({
  name: 'John Doe',
  email: 'john@example.com'
  })
 })
  .then((response) => response.json())
  .then((data) => {
  console.log('创建用户成功:', data);
  })
  .catch((error) => {
  console.error('错误:', error);
 });
```

**讲解：**

- 第二个参数是配置对象：`method` 指定方法，`headers` 声明内容类型，`body` 携带数据；
- POST 的 `body` 必须序列化为 JSON 字符串，服务端才能按 JSON 解析；
- 不设置 `Content-Type: application/json` 时，服务端可能无法识别请求体格式。

### 5.3 请求选项

```javascript
const options = {
  method: 'GET', // GET, POST, PUT, DELETE, etc.
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer token123',
  },
  body: JSON.stringify(data), // POST 请求时使用
  mode: 'cors', // cors, no-cors, same-origin
  credentials: 'include', // include, same-origin, omit
  cache: 'default', // default, no-store, reload, no-cache, force-cache, only-if-cached
  redirect: 'follow', // follow, error, manual
  referrer: 'no-referrer', // no-referrer, client
  referrerPolicy: 'no-referrer',
  integrity: 'sha256-abc123',
  keepalive: false,
  signal: abortController.signal, // 用于取消请求
};
fetch('https://api.example.com/data', options)
  .then((response) => response.json())
  .then((data) => console.log(data));
```

**讲解：**

- `mode: 'cors'` 控制跨域策略，`credentials: 'include'` 决定是否携带 Cookie；
- `redirect: 'follow'` 自动跟随重定向，`manual` 则交给代码处理；
- `signal` 关联取消控制器，是 5.4 节取消请求的基础；
- 这些选项按需设置，默认值已覆盖多数场景，不需要全部手写。

### 5.4 取消请求

```javascript
 // 创建 AbortController
 const abortController = new AbortController();
 // 发送请求
 fetch('https://api.example.com/data', {
  signal: abortController.signal
 })
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => {
  if (error.name === 'AbortError') {
  console.log('请求已取消');
  } else {
  console.error('错误:', error);
  }
  });
 // 取消请求
 setTimeout(() => {
  abortController.abort();
 });
```

**讲解：**

- `AbortController` 通过 `signal` 与请求绑定，调用 `abort()` 即取消请求；
- 取消后 Promise 以 `AbortError` 拒绝，在 `.catch` 中按 `error.name` 区分；
- 适用于“用户离开页面”“输入框内容变化”等需要放弃旧请求的场景。

### 5.5 与 async/await 结合

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    if (!response.ok) {
      throw new Error('网络响应失败');
    }
    const data = await response.json();
    console.log('数据:', data);
    return data;
  } catch (error) {
    console.error('错误:', error);
    throw error;
  }
}
// 调用函数
fetchData();
```

**讲解：**

- `await fetch(...)` 让异步请求像同步代码一样顺序书写，可读性更好；
- `try/catch` 捕获网络错误，`throw error` 把错误继续向上抛给调用方；
- `async` 函数总是返回 Promise，调用方可以用 `.catch` 或外层 `await` 处理失败。

## 6. 其他 Web API

了解即可。Notification、Intersection Observer、File、Canvas 都属于“用到再查”。

### 6.1 Notification API

用于向用户显示通知：

```javascript
// 请求通知权限
if ('Notification' in window) {
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      // 发送通知
      new Notification('通知标题', {
        body: '通知内容',
        icon: '/images/icon.png',
      });
    }
  });
}
```

**讲解：**

- 发送通知前必须先 `requestPermission()`，用户拒绝后无法再次弹窗；
- `new Notification(title, { body, icon })` 创建系统级通知；
- 通知权限属于敏感能力，只在“确有价值”的场景申请，避免被用户永久拒绝。

### 6.2 Intersection Observer API

用于检测元素是否进入视口：

```javascript
// 创建 Intersection Observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      // 元素进入视口
      console.log('元素进入视口');
      entry.target.classList.add('visible');
    } else {
      // 元素离开视口
      console.log('元素离开视口');
      entry.target.classList.remove('visible');
    }
  });
});
// 观察元素
const element = document.querySelector('.target');
observer.observe(element);
```

**讲解：**

- `IntersectionObserver` 异步监听元素与视口的交叉状态，不阻塞主线程；
- `entry.isIntersecting` 表示元素是否进入视口，适合实现懒加载与滚动动画；
- `observe(target)` 开始监听，`unobserve()` 停止，`disconnect()` 关闭全部监听。

### 6.3 File API

用于处理文件上传和读取：

```javascript
// 监听文件选择
const fileInput = document.querySelector('input[type="file"]');
fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  // 检查文件类型
  if (file.type.startsWith('image/')) {
    // 读取文件
    const reader = new FileReader();
    reader.onload = (e) => {
      // 显示图片
      const img = document.createElement('img');
      img.src = e.target.result;
      document.body.appendChild(img);
    };
    reader.readAsDataURL(file);
  }
});
```

**讲解：**

- `event.target.files` 是用户选择的文件列表，`files[0]` 取第一个文件；
- `file.type.startsWith('image/')` 在读取前校验文件类型；
- `FileReader.readAsDataURL` 把文件读成 data URL，赋值给 `img.src` 即可预览。

### 6.4 Canvas API

用于绘制图形：

```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
// 绘制矩形
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 50);
// 绘制圆形
ctx.beginPath();
ctx.arc(150, 100, 30, 0, Math.PI * 2);
ctx.fillStyle = 'blue';
ctx.fill();
```

**讲解：**

- 本小节只展示 Canvas 的“最小可用”写法：获取上下文后即可绘制；
- `fillRect` 直接填充矩形，`arc` 需要配合 `beginPath()` 与 `fill()`；
- Canvas 的完整能力（变换、动画、交互）见 `html5/006-HTML5MultimediaCanvasDrawing`。

## 7. 实际应用示例

### 7.1 示例 1：本地存储用户偏好

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>本地存储用户偏好</title>
    <!-- 样式将在后续 CSS 课程中学习，本示例只保留结构与交互逻辑 -->
  </head>
  <body>
    <div class="container">
      <h1>本地存储用户偏好</h1>
      <div class="theme-toggle">
        <label for="darkMode">深色模式:</label>
        <input type="checkbox" id="darkMode" />
      </div>
      <p>此示例展示如何使用 localStorage 存储用户的主题偏好。</p>
      <p>当你切换主题时，偏好会被保存到本地存储，下次打开页面时会自动应用。</p>
    </div>
    <script>
      const darkModeToggle = document.getElementById('darkMode');
      const body = document.body;
      // 加载保存的主题偏好
      const savedTheme = localStorage.getItem('darkMode');
      if (savedTheme === '') {
        body.classList.add('dark-theme');
        darkModeToggle.checked = true;
      }
      // 监听主题切换
      darkModeToggle.addEventListener('change', function () {
        if (this.checked) {
          body.classList.add('dark-theme');
          localStorage.setItem('darkMode', '');
        } else {
          body.classList.remove('dark-theme');
          localStorage.setItem('darkMode', 'false');
        }
      });
    </script>
  </body>
</html>
```

**代码结构解析：**

（1）结构：页面由主题选择、备注输入、保存按钮、读取按钮组成；

（2）保存：`localStorage.setItem` 写入主题色与备注，刷新后依然存在；

（3）读取：页面加载时从 `localStorage` 恢复上次的选择，实现“记住用户偏好”；

（4）边界：读取的字符串需判断是否存在，避免初次访问时出现 `null` 报错。

### 7.2 示例 2：地理定位应用

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>地理定位应用</title>
    <!-- 样式将在后续 CSS 课程中学习，本示例只保留结构与交互逻辑 -->
  </head>
  <body>
    <div class="container">
      <h1>地理定位应用</h1>
      <button id="getLocation">获取当前位置</button>
      <div class="location-info" id="locationInfo"></div>
      <div class="error" id="errorMessage"></div>
    </div>
    <script>
      const getLocationBtn = document.getElementById('getLocation');
      const locationInfo = document.getElementById('locationInfo');
      const errorMessage = document.getElementById('errorMessage');
      getLocationBtn.addEventListener('click', function () {
        if ('geolocation' in navigator) {
          locationInfo.innerHTML = '<p>正在获取位置...</p>';
          errorMessage.textContent = '';
          navigator.geolocation.getCurrentPosition(
            (position) => {
              const { latitude, longitude, accuracy } = position.coords;
              locationInfo.innerHTML = `
  <h3>当前位置</h3>
  <p>纬度: ${latitude.toFixed(6)}</p>
  <p>经度: ${longitude.toFixed(6)}</p>
  <p>精度: ${accuracy.toFixed(2)} 米</p>
  <p>时间: ${new Date(position.timestamp).toLocaleString()}</p>
  `;
            },
            (error) => {
              let errorText = '';
              switch (error.code) {
                case error.PERMISSION_DENIED:
                  errorText = '用户拒绝了位置请求';
                  break;
                case error.POSITION_UNAVAILABLE:
                  errorText = '位置信息不可用';
                  break;
                case error.TIMEOUT:
                  errorText = '获取位置超时';
                  break;
                default:
                  errorText = '获取位置时发生未知错误';
              }
              errorMessage.textContent = errorText;
              locationInfo.innerHTML = '';
            },
            {
              enableHighAccuracy: true,
              timeout: 10000,
              maximumAge: 0,
            }
          );
        } else {
          errorMessage.textContent = '您的浏览器不支持地理定位';
        }
      });
    </script>
  </body>
</html>
```

**代码结构解析：**

（1）定位：`getCurrentPosition` 获取经纬度与精度，成功回调更新页面文本；

（2）错误分支：按 `error.code` 区分“拒绝授权/位置不可用/超时”，给出对应提示；

（3）展示：用模板字符串把坐标格式化到指定小数位，时间戳转为本地时间；

（4）授权提示：浏览器首次访问会弹出定位授权，拒绝后走错误分支。

### 7.3 示例 3：使用 Fetch API 获取数据

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Fetch API 示例</title>
    <!-- 样式将在后续 CSS 课程中学习，本示例只保留结构与交互逻辑 -->
  </head>
  <body>
    <div class="container">
      <h1>Fetch API 示例</h1>
      <button id="fetchPosts">获取帖子</button>
      <div class="posts" id="postsContainer"></div>
    </div>
    <script>
      const fetchPostsBtn = document.getElementById('fetchPosts');
      const postsContainer = document.getElementById('postsContainer');
      fetchPostsBtn.addEventListener('click', async function () {
        try {
          postsContainer.innerHTML = '<div class="loading">加载中...</div>';
          // 使用 Fetch API 获取数据
          const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=10');
          if (!response.ok) {
            throw new Error('网络响应失败');
          }
          const posts = await response.json();
          // 渲染帖子
          postsContainer.innerHTML = posts
            .map(
              (post) => `
  <div class="post">
  <h3>${post.title}</h3>
  <p>${post.body}</p>
  </div>
  `
            )
            .join('');
        } catch (error) {
          postsContainer.innerHTML = `<div class="error">错误: ${error.message}</div>`;
        }
      });
    </script>
  </body>
</html>
```

**代码结构解析：**

（1）请求：`fetch` 获取远程 JSON 数据，`response.ok` 检查状态码；

（2）渲染：把数组数据映射成列表项插入页面，实现“数据驱动视图”；

（3）错误处理：`.catch` 捕获网络异常并显示错误信息；

（4）加载状态：请求期间显示“加载中”，完成后替换内容，提升体验。

## 8. 最佳实践

### 8.1 Web Storage 最佳实践

- **数据类型**：localStorage 和 sessionStorage 只能存储字符串，存储对象时需要使用 JSON.stringify() 和 JSON.parse()
- **存储容量**：不要存储过大的数据，避免超出存储限制
- **敏感数据**：不要存储敏感数据（如密码），这些数据应该存储在服务器端
- **性能**：频繁读写 localStorage 可能影响性能，建议批量操作
- **兼容性**：虽然现代浏览器都支持 Web Storage，但仍需考虑旧浏览器的兼容性

### 8.2 Geolocation API 最佳实践

- **权限请求**：在需要时才请求位置权限，不要在页面加载时就请求
- **错误处理**：妥善处理位置获取失败的情况
- **精度设置**：根据实际需求设置精度，高精度模式会消耗更多电量
- **用户隐私**：尊重用户隐私，明确告知用户位置信息的使用目的

### 8.3 Web Workers 最佳实践

- **适用场景**：只在需要处理大量计算时使用 Web Workers，避免过度使用
- **通信开销**：注意 Worker 与主线程之间的通信开销，避免频繁通信
- **资源管理**：在不需要时及时终止 Worker，避免资源浪费
- **错误处理**：妥善处理 Worker 中的错误

### 8.4 Service Workers 最佳实践

- **缓存策略**：根据资源类型选择合适的缓存策略
- **缓存版本**：合理管理缓存版本，避免缓存过期问题
- **网络请求**：正确处理网络请求，避免无限循环
- **调试**：使用 Chrome DevTools 进行 Service Worker 调试
- **更新**：正确处理 Service Worker 的更新流程

### 8.5 Fetch API 最佳实践

- **错误处理**：始终处理 fetch 请求的错误，包括网络错误和 HTTP 错误
- **请求配置**：根据实际需求配置请求选项，如 headers、credentials 等
- **响应处理**：根据响应类型选择合适的处理方法，如 response.json()、response.text() 等
- **取消请求**：在需要时使用 AbortController 取消请求
- **超时处理**：实现请求超时处理，避免长时间等待

### 8.6 通用最佳实践

- **特性检测**：在使用 Web API 前进行特性检测，确保浏览器支持
- **性能优化**：注意 API 的性能影响，避免过度使用
- **安全性**：遵循安全最佳实践，避免 XSS、CSRF 等攻击
- **可访问性**：确保应用对所有用户可访问，包括使用辅助技术的用户
- **测试**：在不同浏览器和设备上测试应用，确保兼容性

## 8. 进阶知识点

### 8.1 Storage 事件：跨标签页同步

```javascript
// 当其他标签页修改 localStorage 时触发（当前标签页自身不触发）
window.addEventListener('storage', (event) => {
  console.log('变更的键:', event.key);
  console.log('旧值:', event.oldValue);
  console.log('新值:', event.newValue);
  console.log('URL:', event.url);
});
```

**讲解：**

- `storage` 事件只在“其他标签页”修改存储时触发，用于多标签页同步；
- `event.key` 为 `null` 表示调用了 `clear()`，`newValue` 为 `null` 表示删除；
- 典型场景：设置页修改主题后，其他标签页立即收到通知并应用新主题。

| 属性 | 说明 |
| --- | --- |
| `key` | 变更的键（`null` 表示 clear） |
| `newValue` | 新值（`null` 表示删除） |
| `oldValue` | 旧值（`null` 表示新增） |
| `url` | 触发变更的页面 URL |

### 8.2 Cache Storage API

```javascript
// Cache First 策略：优先缓存，未命中再请求网络
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return (
        cached ||
        fetch(event.request).then((response) => {
          // 克隆响应：响应体只能被消费一次
          const responseClone = response.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseClone);
          });
          return response;
        })
      );
    })
  );
});
```

**讲解：**

- `caches.open(name)` 打开命名缓存，`cache.put(request, response)` 写入映射；
- `caches.match(request)` 在全部缓存中查找，命中则直接返回；
- 响应必须 `clone()` 后再写入缓存，因为响应体只能被消费一次；
- `cache.addAll([...])` 是“请求并缓存”的快捷方式，适合安装阶段预缓存。

## 9. 动手试试

### 入门版（必做）

1. 主题切换器：用 `localStorage` 保存页面主题（浅色/深色），刷新后主题不丢失；
2. 表单草稿：用 `sessionStorage` 保存输入框内容，刷新页面后自动恢复（关掉标签页则清空）；
3. 用 `fetch` 请求一个公开 API（如天气接口），把结果渲染到页面上。

### 进阶版（选做）

1. 用 IntersectionObserver 实现图片懒加载：图片进入视口才设置 `src`；
2. 给页面注册 Service Worker，实现断网后仍能打开首页（缓存 `index.html` 与静态资源）；
3. 打开两个标签页，用 `storage` 事件让主题修改实时同步到另一个标签页。

## 10. 核心知识点

> 一句话记住浏览器存储：长期保存用 `localStorage`，会话临时用 `sessionStorage`；请求数据用 `fetch`，后台计算找 `Worker`，离线兜底靠 Service Worker。

- `localStorage`：约 5MB，跨标签页共享，永久保存，只能存字符串；
- `sessionStorage`：标签页级会话数据，关闭标签页即清除；
- 对象存储必须 `JSON.stringify`/`JSON.parse` 序列化；
- `fetch` 是必背 API：`response.ok` 检查状态、`response.json()` 解析数据、`.catch` 处理错误；
- `AbortController` 可取消请求，避免过期响应覆盖新结果；
- Geolocation/Worker/Service Worker/Notification 等属于“用到再查”的进阶能力。

## 11. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 把敏感数据放 localStorage | 任何页面脚本都能读取，XSS 后可被窃取 | Token 优先放 HttpOnly Cookie，本地只放非敏感偏好 |
| 同步大对象 | 每次 `setItem` 都是同步操作，大数据会卡顿 | 大文件用 IndexedDB，本地存储只放轻量数据 |
| 忘记序列化 | 直接存对象得到 `"[object Object]"` | 写入前 `JSON.stringify`，读取后 `JSON.parse` 并容错 |
| 不检查 `response.ok` | HTTP 404/500 也按成功处理 | 先检查 `ok` 再解析，失败时抛错 |
| 无条件注册 Service Worker | 破坏用户对缓存的预期，更新困难 | 使用版本化缓存名并清理旧版本 |
| 滥用 `watchPosition` | 持续定位耗电、侵犯隐私 | 用 `getCurrentPosition` 单次获取，用后 `clearWatch` |

## 12. 扩展学习

- 存储进阶：`javascript/020-StorageForTheWeb` 对比 Cookie/Web Storage/IndexedDB 的完整取舍；
- 离线进阶：`html5/022-ServiceWorkerPWA` 深入 Service Worker 生命周期与缓存策略；
- 通信：`html5/024-WebSocket` 实时数据通道与 `fetch` 的差异；
- 性能：`javascript/059-CoreWebVitalsAndPerformanceMetrics` 中本地缓存对加载指标的影响；
- 安全：`javascript/044-ErrorBoundaryGlobalErrorCatch` 与 CSP 内容安全策略的配合。
