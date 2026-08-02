---
order: 230
title: History-API
module: 'html5'
category: 前端技术
difficulty: intermediate
description: History API（pushState、replaceState）
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/022-ServiceWorkerPWA'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：单页应用的“地址栏魔法”

在 Vue/React 单页应用里，点击“关于”页面不刷新，但地址栏从 `/` 变成了 `/about`，还能正常使用前进后退——这就是 History API 的功劳。

它的核心是 `history.pushState` 和 `history.replaceState`：不重新加载页面，只修改地址栏 URL 和历史栈，页面内容由 JavaScript 自行切换。这是现代前端路由（history 模式）的基石。

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

**讲解：**

- `pushState(state, '', url)` 往历史栈压入一个新条目，URL 改变但页面不刷新；
- `state` 可携带任意可序列化数据，在 `popstate` 事件中读回；
- URL 必须同源；`pushState` 不会触发 `popstate`，也不会加载新页面。

**replaceState 修改当前条目**
`history.replaceState([state], [unused], [url])`
```javascript
// 修改当前历史条目(不新增)
history.replaceState({ page: 'home' }, '', '/home');

// 更新 state 但保留 URL
history.replaceState({ updated: true }, '');
```

**讲解：** `replaceState` 与 `pushState` 的区别：不新增历史条目，而是替换当前条目，适合“表单状态保存”等不希望产生多余后退步骤的场景。

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

**讲解：** `back()`/`forward()` 等价于 `go(-1)`/`go(1)`；`go(n)` 按相对步数移动历史栈，超出范围时静默无操作。

## 3. popstate 事件

```javascript
window.addEventListener('popstate', (event) => {
  if (event.state) renderPage(event.state.page);
});
```

**讲解：**

- `popstate` 在用户点击前进/后退、或调用 `back()`/`go()` 时触发；
- `pushState`/`replaceState` 本身不触发它，所以路由切换后要手动渲染；
- `event.state` 就是 `pushState` 时写入的状态对象，可用于恢复页面。

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

**讲解：**

- 点击站内链接时 `preventDefault()` 拦截默认跳转，改走 `navigate()`；
- `navigate` 用 `pushState` 更新 URL 并立即渲染；浏览器前进后退触发 `popstate` 再渲染；
- 拦截时校验 `link.origin === location.origin`，站外链接保持默认行为；
- 生产环境还需处理 404 兜底（服务器把未知路径重写到 `index.html`）。

## 5. 注意事项

- URL 必须同源
- 状态对象有大小限制（约 640KB）
- SPA 需服务端配置所有路由返回 index.html

## 6. 进阶知识点

### 6.1 hashchange 事件与 hash 路由

```javascript
window.addEventListener('hashchange', (event) => {
  console.log('旧 URL:', event.oldURL);
  console.log('新 URL:', event.newURL);
  console.log('当前 hash:', location.hash);
});

// 修改 hash 会触发 hashchange，且不会刷新页面
location.hash = 'section2';
```

**讲解：**

- 修改 `location.hash` 会触发 `hashchange`，比 `pushState` 更简单；
- hash 路由无需服务器配合，但 URL 中会带 `#`，语义上不如 history 模式干净；
- Vue Router 的 hash 模式与锚点跳转共用 hash 机制，使用时要区分用途。

### 6.2 URL 对象与查询参数

```javascript
const url = new URL('https://example.com/path?name=Alice&age=30#section');

console.log(url.pathname); // '/path'
console.log(url.search);   // '?name=Alice&age=30'
console.log(url.hash);     // '#section'

// 查询参数读写
const params = new URLSearchParams(url.search);
console.log(params.get('name')); // 'Alice'
params.set('age', '31');
```

**讲解：**

- `new URL()` 把地址解析成结构化对象，属性包括 `protocol`/`host`/`pathname`/`search`/`hash`；
- `URLSearchParams` 提供 `get`/`set`/`has`/`delete` 等查询参数操作；
- 路由切换时用它读写查询参数，比字符串拼接更安全。

## 7. 动手试试

### 入门版（必做）

1. 写三个按钮：跳转 `/page1`、`/page2`、返回上一页，分别用 `pushState` 和 `back()` 实现；
2. 监听 `popstate`，在页面显示当前路径；
3. 用 `replaceState` 把当前路径替换为 `/updated`，观察后退行为与 `pushState` 的差异。

### 进阶版（选做）

1. 实现一个 10 行的迷你路由：点击站内链接切换“首页/关于/联系”三个视图；
2. 用 `URLSearchParams` 实现分页参数 `?page=1` 的读写；
3. 对比 hash 路由与 history 路由在“直接刷新/分享链接”时的行为差异。

## 8. 核心知识点

> 一句话记住 History API：`pushState` 加条目，`replaceState` 换当前；`popstate` 响应前进后退，路由刷新靠 JS 重渲染。

- `pushState(state, '', url)` 新增历史条目，不刷新页面；
- `replaceState` 替换当前条目，适合状态保存；
- `popstate` 在前进/后退时触发，读取 `event.state` 恢复页面；
- `back()`/`forward()`/`go(n)` 操作历史栈；
- `pushState` 要求同源 URL，不触发 `popstate`；
- hashchange 是更简单的替代方案，适合无需服务器配置的场景。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 刷新后 404 | history 路由刷新时服务器无对应文件 | 服务器配置 SPA fallback 到 index.html |
| 忘记监听 `popstate` | 前进后退页面不更新 | 路由初始化时注册 `popstate` |
| 站外链接被拦截 | 误拦截外部跳转 | 校验 `link.origin === location.origin` |
| state 存超大对象 | 超过 640KB 抛异常 | 只存 ID 等轻量信息，数据放 Store/IndexedDB |
| 用 hash 存业务状态 | URL 变脏且与锚点冲突 | 业务状态用 history 模式或查询参数 |
| 忽略滚动恢复 | 后退后位置丢失 | 配合 `scrollRestoration` 或手动恢复 |

## 10. 扩展学习

- 路由框架：Vue Router / React Router 的 history 模式配置；
- 前端路由原理：`javascript/041-ModuleDynamicImportCodeSplitting` 与路由懒加载；
- URL 标准：`javascript/043-Regex` 或 WHATWG URL 规范；
- 服务器配置：Nginx `try_files` 的 SPA fallback 写法。
