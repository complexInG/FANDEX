---
order: 64
title: 'History-API'
module: html5
category: HTML5
difficulty: intermediate
description: 'History API（pushState、replaceState）'
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/Web工作线程
  - 'html5/Service-Worker与PWA'
  - html5/全双工通信
  - html5/实时通信
prerequisites:
  - html5/概述与核心特性
---
## pushState 与 replaceState

**pushState 添加历史条目**
`history.pushState([state], [unused], [url])`
```javascript
// 添加新历史条目
history.pushState({ page: 'about' }, '', '/about');

// 不修改 URL
history.pushState({ page: 'about' }, '');

// 带 state 对象
history.pushState(
  { userId: 123, section: 'profile' },
  '',
  '/users/123/profile'
);

// 查询参数
history.pushState(null, '', '?page=2&sort=desc');

// 锚点
history.pushState(null, '', '#section1');
```

**replaceState 修改当前条目**
`history.replaceState([state], [unused], [url])`
```javascript
// 修改当前历史条目(不新增)
history.replaceState({ page: 'home' }, '', '/home');

// 更新 state 但保留 URL
history.replaceState({ updated: true }, '');
```

**参数说明**

| 参数      | 说明                                              |
| --------- | ------------------------------------------------- |
| `state`   | 状态对象(任意可序列化数据,最大约 640KB)         |
| `unused`  | 历史保留参数,建议传 `''`                          |
| `url`     | 新 URL(必须同源,可相对路径)                     |

> **注意**:`pushState` 和 `replaceState` 不会触发 `popstate` 事件,也不会加载新页面。

---

## 1. History API 概述

History API 允许 JavaScript 操作浏览器的历史记录栈，实现无刷新页面导航。

| 属性                | 说明                        |
| ------------------- | --------------------------- |
| `length`            | 历史记录栈中的条目数        |
| `scrollRestoration` | 滚动恢复策略（auto/manual） |
| `state`             | 当前历史条目的状态对象      |

## 2. 导航方法

```javascript
history.back(); // 后退
history.forward(); // 前进
history.go(-2); // 后退2步
```

## 3. popstate 事件

```javascript
window.addEventListener('popstate', (event) => {
  if (event.state) renderPage(event.state.page);
});
```

## 4. SPA 路由实现

```javascript
class Router {
  constructor() {
    this.routes = {};
    window.addEventListener('popstate', () => this.resolve());
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (link && link.origin === location.origin) {
        e.preventDefault();
        this.navigate(link.pathname);
      }
    });
  }
  addRoute(path, handler) {
    this.routes[path] = handler;
    return this;
  }
  navigate(path, state = {}) {
    history.pushState(state, '', path);
    this.resolve();
  }
  resolve() {
    (this.routes[location.pathname] || this.routes['*'])?.(history.state);
  }
}
```

## 5. 注意事项

- URL 必须同源
- 状态对象有大小限制（约 640KB）
- SPA 需服务端配置所有路由返回 index.html
## History 对象属性

**history 属性**
```javascript
history.length;                 // 历史栈中的条目数
history.state;                  // 当前条目的状态对象
history.scrollRestoration;      // 滚动恢复策略 'auto' | 'manual'
```

**scrollRestoration 设置**
```javascript
// 自动恢复滚动位置(默认)
history.scrollRestoration = 'auto';

// 手动管理滚动
history.scrollRestoration = 'manual';

// 查询
if (history.scrollRestoration === 'manual') {
  // 手动恢复
  window.scrollTo(0, savedScrollY);
}
```

---

## 导航方法

**back / forward / go**
```javascript
history.back();       // 后退一页
history.forward();    // 前进一页
history.go(-2);       // 后退 2 步
history.go(1);        // 前进 1 步
history.go(0);        // 刷新当前页
```

| 方法         | 说明               |
| ------------ | ------------------ |
| `back()`     | 等价于 `go(-1)`    |
| `forward()`  | 等价于 `go(1)`     |
| `go(n)`      | 前进/后退 n 步     |

---

## popstate 事件

**监听前进/后退**
```javascript
window.addEventListener('popstate', (event) => {
  console.log('state:', event.state); // 历史条目的 state 对象
  if (event.state) {
    renderPage(event.state.page);
  }
});
```

**触发 popstate 的操作**
- 浏览器后退按钮
- 浏览器前进按钮
- `history.back()` / `history.forward()` / `history.go()`
- 点击带 `#` 锚点链接(同源)

**手动触发(测试用)**
```javascript
// 不会触发 popstate
history.pushState({ page: 'test' }, '', '/test');

// 触发 popstate 事件
window.dispatchEvent(new PopStateEvent('popstate', { state: history.state }));
```

---

## hashchange 事件

**URL 锚点变化**
```javascript
window.addEventListener('hashchange', (event) => {
  console.log('旧 hash:', event.oldURL);
  console.log('新 hash:', event.newURL);
  console.log('当前 hash:', location.hash);
});

// 通过修改 hash 触发
location.hash = 'section2';
```

---

## SPA 路由实现

**HashRouter 哈希路由**
```javascript
class HashRouter {
  constructor() {
    this.routes = {};
    window.addEventListener('hashchange', () => this.resolve());
    window.addEventListener('load', () => this.resolve());
  }

  addRoute(path, handler) {
    this.routes[path] = handler;
    return this;
  }

  navigate(path) {
    location.hash = path;
  }

  resolve() {
    const path = location.hash.slice(1) || '/';
    (this.routes[path] || this.routes['*'])?.();
  }
}

// 使用
const router = new HashRouter();
router
  .addRoute('/', () => renderHome())
  .addRoute('/about', () => renderAbout())
  .addRoute('/contact', () => renderContact());

// 导航
router.navigate('/about'); // URL 变为 #/about
```

**HistoryRouter History API 路由**
```javascript
class HistoryRouter {
  constructor() {
    this.routes = {};
    window.addEventListener('popstate', () => this.resolve());

    // 拦截链接点击
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (link && link.origin === location.origin) {
        e.preventDefault();
        this.navigate(link.pathname);
      }
    });
  }

  addRoute(path, handler) {
    this.routes[path] = handler;
    return this;
  }

  navigate(path, state = {}) {
    history.pushState(state, '', path);
    this.resolve();
  }

  resolve() {
    const path = location.pathname;
    (this.routes[path] || this.routes['*'])?.(history.state);
  }
}

// 使用
const router = new HistoryRouter();
router
  .addRoute('/', () => renderHome())
  .addRoute('/users', () => renderUsers())
  .addRoute('/users/:id', () => renderUserDetail());
```

---

## URL 对象操作

**URL 解析**
```javascript
const url = new URL('https://example.com/path?name=Alice&age=30#section');

url.protocol; // 'https:'
url.host;     // 'example.com'
url.hostname; // 'example.com'
url.port;     // ''
url.pathname; // '/path'
url.search;   // '?name=Alice&age=30'
url.hash;     // '#section'
url.origin;   // 'https://example.com'
```

**URLSearchParams 查询参数**
```javascript
const params = new URLSearchParams('?name=Alice&age=30');

params.get('name');      // 'Alice'
params.getAll('tag');    // 数组
params.has('age');       // true
params.set('age', '25'); // 修改
params.append('tag', 'a'); // 添加
params.delete('name');   // 删除
params.toString();       // 'age=25&tag=a'

// 遍历
for (const [key, value] of params) {
  console.log(key, value);
}
```

**修改当前 URL 参数**
```javascript
const url = new URL(location.href);
url.searchParams.set('page', '2');
url.searchParams.delete('filter');
history.pushState(null, '', url.toString());
```

---

## 注意事项

**同源策略**
```javascript
// 错误:跨域 URL
history.pushState(null, '', 'https://other.com/page'); // 抛出 SecurityError

// 正确:同源 URL
history.pushState(null, '', '/page');
history.pushState(null, '', location.origin + '/page');
```

**state 大小限制**
```javascript
// 状态对象最大约 640KB(序列化后)
history.pushState({ data: 'large data...' }, '', '/page');

// 推荐用 sessionStorage / IndexedDB 存储大对象
sessionStorage.setItem('pageState', JSON.stringify(largeData));
history.pushState({ storageKey: 'pageState' }, '', '/page');
```

**服务端配置**
```javascript
// SPA 所有路由需服务端返回 index.html
// Nginx 配置示例:
// location / {
//   try_files $uri $uri/ /index.html;
// }
```

## 参考文献

WHATWG HTML Living Standard：https://html.spec.whatwg.org/
MDN HTML 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTML
W3C Markup Validation Service：https://validator.w3.org/
WebAIM 可访问性指南：https://webaim.org/

## 延伸阅读

HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。
CSS 样式与布局，见 007-css 模块。
JavaScript DOM 操作，见 008-javascript 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 HTML/CSS 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 HTML 解析与 DOM 树

浏览器解析 HTML 时先 tokenize 再建树；解析器对错误标记有容错规则（错误恢复算法）。
DOM 是内存中的树结构：元素节点、文本节点、属性；document.querySelector 沿树查找。
渲染流程：HTML -> DOM，CSS -> CSSOM，合并为渲染树，布局与绘制；理解流程可定位性能瓶颈。
脚本与解析：defer 延后执行，async 异步执行，模块脚本默认 defer 语义。

### 13.2 表单校验与无障碍

原生校验：required、pattern、min/max、type 约束；novalidate 可关闭，交由 JS 自定义。
校验 UI：:invalid/:valid 伪类样式；aria-invalid 标记错误；错误信息用 aria-describedby 关联。
键盘可达：所有交互元素可 Tab 聚焦，焦点可见，弹层焦点管理（trap）。
屏幕阅读器测试：NVDA/VoiceOver 实际朗读验证语义。
