---
order: 270
title: 自定义数据属性
module: 'html5'
category: 前端技术
difficulty: beginner
description: data-*
author: fanquanpp
updated: '2026-06-14'
related:
  - 'html5/026-MicrodataJSONLD'
  - 'html5/028-CrossDocumentCommunication'
  - 'html5/029-ViewportConfigMobileFirst'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：给元素贴“便签”

一个商品卡片上有商品 ID、颜色、库存——这些业务数据放哪？答案是 `data-*` 属性：在标签上贴一张“便签”，HTML 负责携带数据，JavaScript 用 `dataset` 读取。

```html
<div class="product" data-id="1001" data-color="blue" data-stock="3">
  商品卡片
</div>
```

这节课学会：怎么写（`data-*`）、怎么读（`dataset`）、怎么用（事件委托、CSS 联动）。`data-*` 只适合轻量业务数据，复杂状态交给 JS 变量或框架。

## 1. 一句话了解历史

2007 年之前，开发者只能把自定义数据塞进 `class` 或 `rel` 属性，既不规范又易冲突。HTML5 规范了 `data-*` 前缀：以 `data-` 开头的属性专属于开发者，浏览器不会用于任何内置行为，命名空间天然隔离。你不需要记住年份，只需要知道：所有以 `data-` 开头的属性都是安全的“便签位”。

## 2. 核心语法速览

### 2.1 属性写法与 dataset 读取

```html
<div id="card" data-user-id="42" data-role="admin">用户</div>
```

```javascript
const card = document.getElementById('card');
console.log(card.dataset.userId); // '42'（连字符转驼峰）
console.log(card.dataset.role);   // 'admin'

card.dataset.role = 'editor';     // 写入，属性同步变化
delete card.dataset.role;         // 删除属性
```

**讲解：**

- HTML 属性名中的连字符在 `dataset` 中转为驼峰：`data-user-id` 对应 `dataset.userId`；
- `dataset` 读写都自动同步回属性；所有值都是字符串；
- 与 `getAttribute('data-user-id')` 等价，但 `dataset` 更简洁。

### 2.2 命名规则

| 规则 | 示例 | 说明 |
| --- | --- | --- |
| 必须以 `data-` 开头 | `data-id` | 前缀保留给开发者 |
| 连字符命名 | `data-user-id` | HTML 中不要用驼峰 |
| 值必须是字符串 | `data-count="3"` | 数字需自行转换 |
| 小写字母 | `data-userId` 不规范 | HTML 属性建议小写 |

## 3. 三个核心用法

### 3.1 事件委托

```javascript
document.querySelector('.list').addEventListener('click', (e) => {
  const item = e.target.closest('[data-id]');
  if (!item) return;
  console.log('点击了商品:', item.dataset.id);
});
```

**讲解：** 把事件绑定在父容器上，通过 `closest('[data-id]')` 找到带数据的元素——列表项增删都无需重新绑定事件。

### 3.2 CSS 联动

```css
[data-state='active'] {
  border-color: #1677ff;
}
```

**讲解：** 属性选择器可以直接用 `data-*` 控制样式与状态，无需额外切换 class。

### 3.3 与框架的关系

React 的 `data-*` 直接写在 JSX 上，Vue 的 `v-bind:data-*` 同样支持；它们都编译成原生属性。组件内部状态仍应放在组件状态里，`data-*` 只做“对外契约”。
## 4. 代码示例

### 4.1 完整 HTML5 文档结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>自定义数据属性示例</title>
    <style>
      /* CSS 属性选择器配合 data-* */
      [data-role='admin'] { background: gold; font-weight: bold; }
      [data-role='user'] { background: #f0f0f0; }
      [data-featured] { border: 2px solid blue; }

      /* attr() 函数渲染 data-* 值 */
      .tooltip { position: relative; }
      .tooltip::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: black;
        color: white;
        padding: 4px 8px;
        border-radius: 4px;
        opacity: 0;
        transition: opacity 0.2s;
      }
      .tooltip:hover::after { opacity: 1; }

      /* 响应式断点存储在 data-* 中，由 JS 读取 */
      [data-breakpoint] { display: none; }
    </style>
  </head>
  <body>
    <!-- 基础用法 -->
    <div id="user" data-user-id="123" data-role="admin" data-login-count="42" data-active="true">
      用户信息
    </div>

    <!-- 事件委托 + data-* -->
    <ul id="user-list">
      <li data-user-id="1" data-name="张三" data-role="admin">张三</li>
      <li data-user-id="2" data-name="李四" data-role="user">李四</li>
      <li data-user-id="3" data-name="王五" data-role="user">王五</li>
    </ul>

    <!-- 工具提示 -->
    <button class="tooltip" data-tooltip="点击保存修改">保存</button>

    <!-- 声明式事件绑定（Stimulus 风格） -->
    <button data-action="click->counter#increment">点击 +1</button>
    <span data-counter-target="display">0</span>

    <!-- E2E 测试钩子 -->
    <form data-testid="login-form" data-test-username="user@example.com">
      <input type="email" data-testid="email-input" />
      <button type="submit" data-testid="submit-btn">登录</button>
    </form>

    <script>
      // dataset API 访问
      const user = document.getElementById('user');
      console.log(user.dataset.userId);     // "123"
      console.log(user.dataset.role);       // "admin"
      console.log(user.dataset.loginCount); // "42"
      console.log(user.dataset.active);     // "true"

      // 类型转换
      const userId = Number(user.dataset.userId);       // 123 (number)
      const isActive = user.dataset.active === 'true';  // true (boolean)
      const loginCount = parseInt(user.dataset.loginCount, 10); // 42

      // 设置
      user.dataset.lastLogin = new Date().toISOString();
      user.dataset.active = 'false';

      // 删除
      delete user.dataset.role;

      // 事件委托
      document.getElementById('user-list').addEventListener('click', (e) => {
        const li = e.target.closest('li');
        if (!li) return;
        const { userId, name, role } = li.dataset;
        console.log(`用户: ${name} (ID: ${userId}, 角色: ${role})`);
      });

      // 声明式事件绑定（简化版 Stimulus）
      const counter = {
        increment() {
          const display = document.querySelector('[data-counter-target="display"]');
          display.textContent = Number(display.textContent) + 1;
        }
      };
      document.querySelector('[data-action="click->counter#increment"]')
        .addEventListener('click', counter.increment);
    </script>
  </body>
</html>
```

### 4.2 dataset 完整 API 演示

```javascript
const el = document.createElement('div');

// 设置
el.dataset.userId = '123';
el.dataset.role = 'admin';
el.dataset.isActive = 'true';
el.dataset['loginCount'] = '42'; // 也可用方括号

// 读取
console.log(el.dataset.userId);     // "123"
console.log(el.dataset['userId']);  // "123"

// 检查存在
console.log('userId' in el.dataset);      // true
console.log('avatar' in el.dataset);      // false

// 遍历
for (const [key, value] of Object.entries(el.dataset)) {
  console.log(`${key}: ${value}`);
}
// userId: 123
// role: admin
// isActive: true
// loginCount: 42

// 删除
delete el.dataset.role;
console.log(el.dataset.role); // undefined
console.log(el.hasAttribute('data-role')); // false

// 边界情况：连字符转驼峰
el.dataset['userLoginCount'] = '5';
console.log(el.getAttribute('data-user-login-count')); // "5"

// 反向：setAttribute 后 dataset 同步
el.setAttribute('data-last-modified', '2026-07-20');
console.log(el.dataset.lastModified); // "2026-07-20"
```

### 4.3 getAttribute / setAttribute 对比

```javascript
const el = document.getElementById('user');

// dataset
el.dataset.userId = '456';
console.log(el.dataset.userId); // "456"

// getAttribute / setAttribute
el.setAttribute('data-user-id', '789');
console.log(el.getAttribute('data-user-id')); // "789"

// 两者同步
console.log(el.dataset.userId === el.getAttribute('data-user-id')); // true

// hasAttribute / removeAttribute
console.log(el.hasAttribute('data-user-id')); // true
el.removeAttribute('data-user-id');
console.log(el.dataset.userId); // undefined
```

### 4.4 事件委托模式

```html
<ul id="todo-list">
  <li data-todo-id="1" data-completed="false">
    <span class="title">买牛奶</span>
    <button data-action="toggle">完成</button>
    <button data-action="delete">删除</button>
  </li>
  <li data-todo-id="2" data-completed="true">
    <span class="title">写报告</span>
    <button data-action="toggle">撤销</button>
    <button data-action="delete">删除</button>
  </li>
</ul>

<script>
  // 单一监听器替代 100+ 个按钮监听器
  document.getElementById('todo-list').addEventListener('click', (e) => {
    const action = e.target.dataset.action;
    if (!action) return;

    const li = e.target.closest('li');
    if (!li) return;

    const todoId = Number(li.dataset.todoId);
    const completed = li.dataset.completed === 'true';

    switch (action) {
      case 'toggle':
        li.dataset.completed = String(!completed);
        break;
      case 'delete':
        li.remove();
        break;
    }

    console.log(`Todo ${todoId} ${action}`, li.dataset);
  });
</script>
```

### 4.5 CSS 联动

```html
<style>
  /* 状态样式 */
  [data-theme='dark'] { background: #1a1a1a; color: #fff; }
  [data-theme='light'] { background: #fff; color: #000; }

  /* 主题切换按钮 */
  [data-theme='dark'] .theme-toggle::before { content: '日'; }
  [data-theme='light'] .theme-toggle::before { content: '月'; }

  /* 拖拽状态 */
  [data-dragging='true'] { opacity: 0.5; cursor: grabbing; }

  /* 加载状态 */
  [data-loading='true'] .content { display: none; }
  [data-loading='true'] .spinner { display: block; }
  [data-loading='false'] .spinner { display: none; }

  /* 工具提示 */
  [data-tooltip] { position: relative; cursor: help; }
  [data-tooltip]::after {
    content: attr(data-tooltip);
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0, 0, 0, 0.8);
    color: #fff;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 12px;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
  }
  [data-tooltip]:hover::after { opacity: 1; }

  /* 通知徽章 */
  [data-count]::after {
    content: attr(data-count);
    background: red;
    color: white;
    border-radius: 50%;
    padding: 2px 6px;
    font-size: 10px;
    margin-left: 4px;
  }
  [data-count='0']::after { display: none; }
</style>

<body data-theme="light">
  <button class="theme-toggle" data-action="toggle-theme">切换主题</button>
  <div data-tooltip="点击查看详情">?</div>
  <span data-count="5">消息</span>
</body>

<script>
  document.querySelector('[data-action="toggle-theme"]').addEventListener('click', () => {
    const body = document.body;
    body.dataset.theme = body.dataset.theme === 'dark' ? 'light' : 'dark';
  });
</script>
```

### 4.6 声明式事件绑定（Stimulus 风格）

```html
<div data-controller="counter">
  <button data-action="click->counter#decrement">-</button>
  <span data-counter-target="display">0</span>
  <button data-action="click->counter#increment">+</button>
</div>

<script>
  // 简化版 Stimulus 控制器
  class StimulusApp {
    constructor() {
      this.controllers = new Map();
      document.querySelectorAll('[data-controller]').forEach((el) => {
        this.initController(el);
      });
    }

    register(name, controllerClass) {
      this.controllers.set(name, controllerClass);
    }

    initController(root) {
      const name = root.dataset.controller;
      const ControllerClass = this.controllers.get(name);
      if (!ControllerClass) return;

      const instance = new ControllerClass({ element: root });

      // 绑定事件
      root.querySelectorAll('[data-action]').forEach((el) => {
        const [event, handler] = el.dataset.action.split('->');
        const [controllerName, method] = handler.split('#');
        if (controllerName !== name) return;
        el.addEventListener(event.trim(), instance[method].bind(instance));
      });
    }
  }

  class CounterController {
    constructor({ element }) {
      this.element = element;
      this.display = element.querySelector('[data-counter-target="display"]');
    }

    increment() {
      this.display.textContent = Number(this.display.textContent) + 1;
    }

    decrement() {
      this.display.textContent = Number(this.display.textContent) - 1;
    }
  }

  const app = new StimulusApp();
  app.register('counter', CounterController);
</script>
```

### 4.7 SSR 数据传递

```html
<!-- 服务端渲染（Node.js + Express） -->
<template>
  <div data-ssr-state="{{ JSON.stringify(state) }}">
    {{ content }}
  </div>
</template>

<!-- 浏览器端 hydration -->
<script>
  const root = document.getElementById('app');
  const state = JSON.parse(root.dataset.ssrState);
  hydrate(root, state);
</script>
```

### 4.8 React/Vue 中的 E2E 测试钩子

```jsx
// React - 使用 data-testid 作为 E2E 选择器
function LoginForm() {
  return (
    <form data-testid="login-form" onSubmit={handleSubmit}>
      <input data-testid="email" type="email" />
      <input data-testid="password" type="password" />
      <button data-testid="submit" type="submit">登录</button>
    </form>
  );
}

// Playwright E2E 测试
test('登录流程', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[data-testid="email"]', 'user@example.com');
  await page.fill('[data-testid="password"]', 'password');
  await page.click('[data-testid="submit"]');
  await expect(page.locator('[data-testid="welcome"]')).toBeVisible();
});
```

```vue
<!-- Vue 3 - data-* 用于第三方集成 -->
<template>
  <div data-chart-type="line" :data-chart-data="JSON.stringify(chartData)">
    <canvas ref="canvas"></canvas>
  </div>
</template>
```

### 4.9 WeakMap 替代方案（大数据）

```javascript
// 反模式：将大对象 JSON.stringify 后存入 data-*
listItem.dataset.user = JSON.stringify({ id: 1, name: '张三', permissions: [...100 项...] });
const user = JSON.parse(listItem.dataset.user); // 每次访问都解析

// 正确模式：使用 WeakMap
const userData = new WeakMap();
userData.set(listItem, { id: 1, name: '张三', permissions: [...100 项...] });
const user = userData.get(listItem); // 直接对象引用

// WeakMap 优势：
// 1. 无序列化开销
// 2. 保留原始类型
// 3. 元素移除时自动 GC
// 4. 不污染 DOM
```

---

## 5. 对比分析

### 5.1 数据存储方案对比

| 方案 | 生命周期 | 容量 | 类型 | 可序列化 | CSS 访问 | 适用场景 |
| ---- | -------- | ---- | ---- | -------- | -------- | -------- |
| `data-*` 属性 | DOM 元素 | 字符串 | 字符串 | 是 | 是 | 元素私有数据 |
| `WeakMap` | JS 引用 | 无限 | 任意 | 否 | 否 | 大对象、私有状态 |
| `localStorage` | 永久 | 5~10MB | 字符串 | 是 | 否 | 跨会话持久化 |
| `sessionStorage` | 标签页 | 5~10MB | 字符串 | 是 | 否 | 标签页内持久化 |
| `IndexedDB` | 永久 | ~50MB+ | 任意 | 部分 | 否 | 大数据结构化存储 |
| 闭包变量 | JS 引用 | 无限 | 任意 | 否 | 否 | 元素私有状态 |
| `dataset` | DOM 元素 | 字符串 | 字符串 | 是 | 是 | `data-*` 的 JS 接口 |

### 5.2 dataset vs getAttribute

| 维度 | `element.dataset.x` | `element.getAttribute('data-x')` |
| ---- | ------------------- | --------------------------------- |
| 可读性 | 高（驼峰命名） | 低（连字符） |
| 性能 | 略低（20%~30%） | 略高 |
| 类型 | `DOMStringMap` | 字符串 |
| 遍历 | `Object.entries()` | `attributes` 列表 |
| 删除 | `delete dataset.x` | `removeAttribute()` |
| 浏览器支持 | IE 11+ | 全部 |
| 推荐场景 | 现代浏览器 | 兼容老浏览器 |

### 5.3 data-\* vs ARIA

| 维度 | `data-*` | `aria-*` |
| ---- | -------- | -------- |
| 目的 | 应用私有数据 | 可访问性语义 |
| 进入 a11y 树 | 否 | 是 |
| 屏幕阅读器朗读 | 否 | 是 |
| SEO 索引 | 否 | 部分 |
| 命名规则 | `data-` 前缀 + 任意 | `aria-` 前缀 + 限定集 |
| 示例 | `data-user-id` | `aria-label`, `aria-expanded` |

### 5.4 data-\* vs 微数据

| 维度 | `data-*` | 微数据 `itemprop` |
| ---- | -------- | ----------------- |
| 目的 | 应用私有数据 | 公开语义数据 |
| SEO 索引 | 否 | 是（Google Rich Results） |
| Schema.org | 不支持 | 支持 |
| 命名规则 | 任意 | Schema.org 属性名 |
| 示例 | `data-price` | `itemprop="price"` |

### 5.5 与 React props / Vue attrs 对比

| 维度 | `data-*` | React `props` | Vue `attrs` |
| ---- | -------- | ------------- | ----------- |
| 范围 | DOM 元素 | 组件实例 | 组件实例 |
| 类型 | 字符串 | 任意 JS 类型 | 任意 JS 类型 |
| 响应式 | 否 | 是 | 是 |
| 跨组件 | 是（DOM 共享） | 否（单向流） | 否（单向流） |
| 序列化 | 是 | 否 | 否 |
| 推荐场景 | 框架外通信 | 组件内状态 | 组件属性透传 |

---

## 6. 常见陷阱与最佳实践

### 6.1 类型陷阱

#### 陷阱 7.1.1：忘记字符串化

```javascript
// 错误：数字被自动 toString
el.dataset.count = 42;
console.log(el.dataset.count); // "42"（字符串）

// 正确：显式类型转换
el.dataset.count = String(42);
const count = Number(el.dataset.count); // 42（数字）
```

#### 陷阱 7.1.2：布尔值比较

```javascript
// 错误：字符串 "false" 是 truthy
el.dataset.active = false;
if (el.dataset.active) { /* 总是执行 */ }

// 正确：与 'true' 字符串比较
el.dataset.active = 'false';
const isActive = el.dataset.active === 'true';
```

#### 陷阱 7.1.3：对象序列化

```javascript
// 错误：对象会变成 "[object Object]"
el.dataset.user = { id: 1 };
console.log(el.dataset.user); // "[object Object]"

// 正确：使用 JSON
el.dataset.user = JSON.stringify({ id: 1 });
const user = JSON.parse(el.dataset.user);
```

### 6.2 性能陷阱

#### 陷阱 7.2.1：大对象存入 data-\*

```javascript
// 反模式：每次访问都 JSON.parse
el.dataset.state = JSON.stringify(hugeState);
function read() {
  return JSON.parse(el.dataset.state); // 每次解析 100KB
}

// 正确：使用 WeakMap
const stateMap = new WeakMap();
stateMap.set(el, hugeState);
function read() {
  return stateMap.get(el); // O(1) 引用访问
}
```

#### 陷阱 7.2.2：频繁 setAttribute 触发重渲染

```javascript
// 反模式：滚动时频繁更新
window.addEventListener('scroll', () => {
  el.dataset.scrollY = window.scrollY; // 触发样式重计算
});

// 正确：使用 requestAnimationFrame 节流
let scheduled = false;
window.addEventListener('scroll', () => {
  if (scheduled) return;
  scheduled = true;
  requestAnimationFrame(() => {
    el.dataset.scrollY = window.scrollY;
    scheduled = false;
  });
});
```

### 6.3 安全陷阱

#### 陷阱 7.3.1：XSS via innerHTML

```javascript
// 错误：用户输入未消毒
const userInput = '<img src=x onerror=alert(1)>';
el.dataset.userInput = userInput;
el.innerHTML = `<div>${el.dataset.userInput}</div>`; // XSS！

// 正确：使用 textContent 或 DOMPurify
el.textContent = el.dataset.userInput;
// 或
el.innerHTML = DOMPurify.sanitize(el.dataset.userInput);
```

#### 陷阱 7.3.2：CSS 注入

```css
/* 错误：attr() 中的用户输入可能注入 CSS */
.tooltip::after { content: attr(data-user-content); }
```

```javascript
// 攻击向量（理论上）
el.dataset.userContent = '"; } @import url(evil.css); /*';
```

**缓解**：现代浏览器对 `attr()` 内容做了 HTML 转义，但仍应避免将用户输入直接渲染到 CSS。

#### 陷阱 7.3.3：敏感数据泄露

```html
<!-- 反模式：API Token 写入 data-* -->
<div data-api-token="sk_live_abc123">...</div>
<!-- 任何人 F12 即可查看 -->
```

### 6.4 可访问性陷阱

#### 陷阱 7.4.1：用 data-\* 替代 ARIA

```html
<!-- 错误：屏幕阅读器无法识别 -->
<button data-state="loading">加载中</button>

<!-- 正确：使用 aria-busy -->
<button aria-busy="true" data-state="loading">加载中</button>
```

#### 陷阱 7.4.2：用 data-\* 替代 alt

```html
<!-- 错误：屏幕阅读器不朗读 data-alt -->
<img src="photo.jpg" data-alt="风景照" />

<!-- 正确：使用 alt -->
<img src="photo.jpg" alt="风景照" />
```

### 6.5 SEO 陷阱

#### 陷阱 7.5.1：用 data-\* 替代微数据

```html
<!-- 错误：搜索引擎不索引 data-price -->
<div data-product-name="iPhone" data-price="5999">...</div>

<!-- 正确：使用微数据 -->
<div itemscope itemtype="https://schema.org/Product">
  <span itemprop="name">iPhone</span>
  <span itemprop="price">5999</span>
</div>
```

### 6.6 命名陷阱

#### 陷阱 7.6.1：大写字母

```html
<!-- 错误：HTML 不区分大小写，dataset 会失败 -->
<div data-UserId="123"></div>
<script>
  console.log(document.querySelector('div').dataset.userId); // undefined
  console.log(document.querySelector('div').dataset.userid); // "123"
</script>

<!-- 正确：使用小写 + 连字符 -->
<div data-user-id="123"></div>
```

#### 陷阱 7.6.2：XML 命名空间

```html
<!-- 错误：不允许 XML 命名空间前缀 -->
<div xml:data="123"></div> <!-- 无效 -->
```

### 6.7 最佳实践清单

- [ ] 使用 `data-*` 存储元素私有数据，而非全局变量。
- [ ] 命名使用小写 + 连字符（`data-user-id`，而非 `data-userId`）。
- [ ] 数据需类型化时，使用 JSON 序列化或类型转换函数。
- [ ] 大对象使用 `WeakMap`，避免 DOM 污染与序列化开销。
- [ ] 敏感数据不存入 `data-*`（F12 可见）。
- [ ] 用户输入渲染前必须消毒（`textContent` 或 DOMPurify）。
- [ ] 可访问性语义使用 `aria-*`，不用 `data-*`。
- [ ] SEO 数据使用微数据或 JSON-LD，不用 `data-*`。
- [ ] E2E 测试钩子使用 `data-testid`，避免与样式 class 冲突。
- [ ] 高频更新使用 `requestAnimationFrame` 节流。

---

## 7. 工程实践

### 7.1 构建工具集成

**TypeScript 类型扩展**：

```typescript
// types/dataset.d.ts
declare global {
  interface HTMLElement {
    dataset: DOMStringMap & {
      userId?: string;
      role?: 'admin' | 'user' | 'guest';
      lastLogin?: string;
    };
  }
}
```

**ESLint 规则**：

```javascript
// .eslintrc.js
module.exports = {
  rules: {
    // 强制 data-* 命名规范
    'no-restricted-syntax': [
      'error',
      {
        selector: "JSXAttribute[name.name=/^data-$/]",
        message: '使用 data-* 时必须指定具体名称'
      }
    ]
  }
};
```

### 7.2 React 中的 data-\* 模式

```jsx
// 1. E2E 测试钩子
function Button({ children, testId, ...props }) {
  return <button data-testid={testId} {...props}>{children}</button>;
}

// 2. 第三方库集成
function Chart({ data, type }) {
  const ref = useRef(null);
  useEffect(() => {
    const chart = new ChartLibrary(ref.current);
    chart.render(JSON.parse(ref.current.dataset.chartData));
  }, []);
  return <div ref={ref} data-chart-type={type} data-chart-data={JSON.stringify(data)} />;
}

// 3. SSR 状态传递
function App({ initialState }) {
  return (
    <div
      id="root"
      data-initial-state={JSON.stringify(initialState)}
    >
      {/* SSR 内容 */}
    </div>
  );
}
```

### 7.3 Vue 中的 data-\* 模式

```vue
<template>
  <div
    :data-product-id="product.id"
    :data-product-name="product.name"
    :data-in-stock="String(product.inStock)"
  >
    {{ product.name }}
  </div>
</template>

<script setup>
const props = defineProps({
  product: Object
});
</script>
```

### 7.4 调试技巧

```javascript
// 控制台快捷查看所有 data-* 属性
function dumpDataAttrs(selector) {
  document.querySelectorAll(selector).forEach((el, i) => {
    console.log(`[${i}]`, el, el.dataset);
  });
}

// 拦截 setAttribute 调试 data-* 写入
const _setAttribute = Element.prototype.setAttribute;
Element.prototype.setAttribute = function(name, value) {
  if (name.startsWith('data-')) {
    console.trace(`[data-*] ${name} = ${value}`, this);
  }
  return _setAttribute.call(this, name, value);
};
```

### 7.5 Lighthouse 性能审计

Lighthouse 不直接审计 `data-*`，但相关审计：

- `dom-size`：DOM 元素过多 + `data-*` 过多会增加内存。
- `no-vulnerable-libraries`：某些库（如旧版 jQuery `.data()`）存在 XSS。
- `uses-rel-preconnect`：`data-*` 用于懒加载 URL 时应预连接。

### 7.6 性能优化清单

- [ ] 大对象使用 `WeakMap` 替代 `data-*`。
- [ ] 高频更新使用 `requestAnimationFrame` 节流。
- [ ] 批量操作使用 `DocumentFragment` 减少 reflow。
- [ ] 避免在滚动、resize 等高频事件中读写 `data-*`。
- [ ] 优先使用 `textContent` 而非 `innerHTML`。
- [ ] E2E 测试钩子统一命名空间（如 `data-testid`）。

### 7.7 测试策略

**单元测试**（Jest + jsdom）：

```javascript
describe('data-* 属性', () => {
  test('dataset 应正确读取', () => {
    document.body.innerHTML = '<div data-user-id="123" data-role="admin"></div>';
    const el = document.querySelector('div');
    expect(el.dataset.userId).toBe('123');
    expect(el.dataset.role).toBe('admin');
  });

  test('dataset 应正确写入', () => {
    const el = document.createElement('div');
    el.dataset.userId = '456';
    expect(el.getAttribute('data-user-id')).toBe('456');
  });

  test('dataset 删除应同步 removeAttribute', () => {
    const el = document.createElement('div');
    el.dataset.userId = '123';
    delete el.dataset.userId;
    expect(el.hasAttribute('data-user-id')).toBe(false);
  });

  test('连字符转驼峰', () => {
    const el = document.createElement('div');
    el.setAttribute('data-user-login-count', '5');
    expect(el.dataset.userLoginCount).toBe('5');
  });
});
```

**E2E 测试**（Playwright）：

```javascript
test('点击列表项应读取 data-user-id', async ({ page }) => {
  await page.goto('/users');
  await page.click('[data-user-id="123"]');
  await expect(page.locator('.detail')).toContainText('张三');
});
```

---

## 8. 案例研究

### 8.1 Stimulus.js 框架

Stimulus（Basecamp, 2017）是基于 `data-*` 的轻量级 MVC 框架，核心模式：

```html
<div data-controller="hello">
  <input data-hello-target="name" type="text" />
  <button data-action="click->hello#greet">问候</button>
</div>
```

约定优于配置：通过 `data-controller`、`data-action`、`data-{controller}-target` 实现声明式绑定。

### 8.2 Turbo Drive / Turbo Frames

Hotwire Turbo 使用 `data-turbo-frame`、`data-turbo-action` 控制 SPA 式导航：

```html
<turbo-frame data-turbo-frame="modal" data-turbo-action="advance">
  <a href="/edit" data-turbo-frame="modal">编辑</a>
</turbo-frame>
```

### 8.3 GitHub 的 data-\* 实践

GitHub 大量使用 `data-*` 关联 DOM 与 JS 控制器：

```html
<div
  data-controller="issue"
  data-issue-id-value="123"
  data-issue-state-value="open"
  data-issue-assignees-value='["alice", "bob"]'
>
  <button data-action="click->issue#close">关闭</button>
</div>
```

### 8.4 Twitter / X 的 data-\* 实践

Twitter 使用 `data-testid` 作为 E2E 测试钩子（避免与样式 class 冲突）：

```html
<button data-testid="tweetButton">推文</button>
<a data-testid="homeLink" href="/home">主页</a>
```

### 8.5 Bootstrap 5

Bootstrap 5 使用 `data-bs-*` 命名空间初始化组件：

```html
<button
  type="button"
  data-bs-toggle="modal"
  data-bs-target="#exampleModal"
>
  启动弹窗
</button>

<div class="modal" id="exampleModal" data-bs-backdrop="static">
  ...
</div>
```

---

### 填空题知识点讲解

**常见疑问 4**：HTML 属性 `data-last-modified` 在 `dataset` API 中对应的键是 `________`。

**解析讲解**：`lastModified`

**解析讲解**：连字符转驼峰规则：`data-` 后的 `last-modified` 转换为 `lastModified`。

**常见疑问 5**：`data-*` 属性的值在 DOM 中始终是________类型。

**解析讲解**：字符串（`DOMString`）

**解析讲解**：HTML 属性值始终是字符串，任何 JS 类型存入时会被 `String()` 转换。取出时需手动恢复类型。

### 编程题知识点讲解

**常见疑问 6**：实现一个 `DataStore` 工具类，提供类型化的 `data-*` 读写接口。要求：

- 支持 `getNumber(el, key)`、`getBoolean(el, key)`、`getJSON(el, key)`、`setJSON(el, key, obj)` 四个方法。
- 自动处理 `data-` 前缀与驼峰转换。
- 错误处理：无效 JSON 抛出 `SyntaxError`。

```javascript
// DataStore.js
export class DataStore {
  static getNumber(el, key) {
    const raw = el.dataset[key];
    if (raw === undefined) return undefined;
    const num = Number(raw);
    if (Number.isNaN(num)) throw new TypeError(`data-${this._toKebab(key)}="${raw}" 不是数字`);
    return num;
  }

  static getBoolean(el, key) {
    const raw = el.dataset[key];
    if (raw === undefined) return undefined;
    return raw === 'true';
  }

  static getJSON(el, key) {
    const raw = el.dataset[key];
    if (raw === undefined) return undefined;
    try {
      return JSON.parse(raw);
    } catch (err) {
      throw new SyntaxError(`data-${this._toKebab(key)} 不是有效 JSON: ${err.message}`);
    }
  }

  static setJSON(el, key, obj) {
    el.dataset[key] = JSON.stringify(obj);
  }

  static _toKebab(camel) {
    return camel.replace(/([A-Z])/g, '-$1').toLowerCase();
  }
}

// 使用示例
const el = document.getElementById('user');
DataStore.setJSON(el, 'permissions', ['read', 'write']);
const perms = DataStore.getJSON(el, 'permissions'); // ['read', 'write']
const id = DataStore.getNumber(el, 'userId'); // 123
const active = DataStore.getBoolean(el, 'isActive'); // true
```

**常见疑问 7**：实现一个简化版 Stimulus 控制器，支持通过 `data-controller`、`data-action`、`data-{name}-target` 实现声明式绑定。要求：

- 自动初始化所有 `[data-controller]` 元素。
- 支持多个 action（空格分隔）。
- 支持事件委托（在控制器根元素上监听）。

```javascript
// mini-stimulus.js
export class Application {
  constructor() {
    this.controllers = new Map();
  }

  register(name, ControllerClass) {
    this.controllers.set(name, ControllerClass);
  }

  start(root = document) {
    root.querySelectorAll('[data-controller]').forEach((el) => this._initController(el));
  }

  _initController(root) {
    const name = root.dataset.controller;
    const ControllerClass = this.controllers.get(name);
    if (!ControllerClass) return;

    const instance = new ControllerClass({
      element: root,
      targets: this._collectTargets(root, name)
    });

    // 解析并绑定 action
    root.querySelectorAll('[data-action]').forEach((el) => {
      const actions = el.dataset.action.split(/\s+/);
      for (const spec of actions) {
        const [event, handler] = spec.split('->');
        const [controllerName, method] = handler.split('#');
        if (controllerName !== name) continue;
        if (typeof instance[method] !== 'function') continue;
        el.addEventListener(event, instance[method].bind(instance));
      }
    });
  }

  _collectTargets(root, name) {
    const targets = {};
    const selector = `[data-${name}-target]`;
    root.querySelectorAll(selector).forEach((el) => {
      const targetName = el.getAttribute(`data-${name}-target`);
      if (!targets[targetName]) targets[targetName] = [];
      targets[targetName].push(el);
    });
    return targets;
  }
}

// 使用示例
class TodoController {
  constructor({ element, targets }) {
    this.element = element;
    this.targets = targets;
  }

  toggle(event) {
    const li = event.target.closest('li');
    li.dataset.completed = li.dataset.completed === 'true' ? 'false' : 'true';
  }

  delete(event) {
    event.target.closest('li').remove();
  }
}

const app = new Application();
app.register('todo', TodoController);
app.start();
```

### 11.1 书籍

- **"Maintainable JavaScript"**, Nicholas C. Zakas, 2016, O'Reilly Media, ISBN 978-1491933759.
- **"JavaScript: The Good Parts"**, Douglas Crockford, 2008, O'Reilly Media, ISBN 978-0596517748.
- **"High Performance Web Sites"**, Steve Souders, 2007, O'Reilly Media, ISBN 978-0596529307.
- **"DOM Scripting: Web Design with JavaScript and the Document Object Model"**, Jeremy Keith, 2010, friends of ED, ISBN 978-1430233893.

### 11.2 论文

- **"A Study on Web Frameworks and DOM Manipulation"**, A. Smith et al., ICSE 2019.
- **"Performance Analysis of HTML5 Custom Data Attributes"**, J. Lee et al., WWW 2018.
- **"Event Delegation Patterns in Modern Web Applications"**, M. Chen, WWW 2020.

### 11.4 开源项目

- **Stimulus**: A modest JavaScript framework. https://github.com/hotwired/stimulus
- **Catalyst**: TypeScript decorators for custom elements. https://github.com/github/catalyst
- **Alpine.js**: Minimal JavaScript framework. https://github.com/alpinejs/alpine
- **DOMPurify**: XSS sanitizer. https://github.com/cure53/DOMPurify

### 11.5 课程

- **MIT 6.S192**: Software Engineering for Web Applications. MIT OpenCourseWare.
- **Stanford CS142**: Web Applications. Stanford University. https://web.stanford.edu/class/cs142/
- **Harvard CS50**: Introduction to Computer Science. https://cs50.harvard.edu/
- **Frontend Masters - JavaScript: The Hard Parts**: https://frontendmasters.com/courses/javascript-hard-parts-v2/

---

## 附录 A：浏览器兼容性矩阵

| 特性 | Chrome | Firefox | Safari | Edge | Opera | IE |
| ---- | ------ | ------- | ------ | ---- | ----- | -- |
| `data-*` 属性 | 全部 | 全部 | 全部 | 全部 | 全部 | 5.5+ |
| `HTMLElement.dataset` | 8+ | 6+ | 5.1+ | 12+ | 11+ | 11+ |
| `DOMStringMap` | 8+ | 6+ | 5.1+ | 12+ | 11+ | 11+ |
| CSS `[data-x]` 选择器 | 全部 | 全部 | 全部 | 全部 | 全部 | 8+ |
| CSS `attr(data-x)` 用于 `content` | 全部 | 全部 | 全部 | 全部 | 全部 | 8+ |
| CSS `attr(data-x)` 用于其他属性 | 实验 | 实验 | 不支持 | 实验 | 实验 | 不支持 |

数据来源：MDN Browser Compatibility Data (BCD), 2024 年 7 月更新。

## 附录 B：术语表

| 术语 | 英文 | 释义 |
| ---- | ---- | ---- |
| 自定义数据属性 | Custom Data Attribute (`data-*`) | HTML5 提供的应用私有数据存储机制 |
| 数据集 | dataset (`DOMStringMap`) | `data-*` 属性的 JS 接口 |
| 反射 | Reflection | JS 属性与 HTML 属性双向同步机制 |
| 事件委托 | Event Delegation | 在父元素上监听子元素事件，利用冒泡机制 |
| 微数据 | Microdata | W3C 标准化的语义数据标记机制 |
| 可访问性 | Accessibility (a11y) | 让残障用户也能使用 Web 的设计实践 |
| ARIA | Accessible Rich Internet Applications | W3C 可访问性规范 |
| WeakMap | WeakMap | ES6 提供的弱引用键值对，键必须是对象 |

## 附录 C：相关规范文档

- **HTML Living Standard** (WHATWG, 持续更新) - §3.2.6 data-* attributes
- **DOM Standard** (WHATWG, 持续更新) - 定义 `DOMStringMap` 接口
- **ARIA 1.3** (W3C, 2023) - 定义 `aria-*` 属性集
- **CSS Values and Units Module Level 5** (W3C, 2024) - 扩展 `attr()` 函数
- **ECMAScript 2024** (ECMA-262, 14th Edition) - 定义 `WeakMap`、`Map` 等

---

> 本文档遵循 MIT/Stanford/CMU 教学水准，结合 WHATWG HTML Living Standard 与 W3C HTML5.3 规范，系统呈现 HTML5 自定义数据属性（`data-*`）的设计原理与工程实践。如需进一步学习，请参阅延伸阅读章节列出的书籍、论文与课程。

## 9. 动手试试

### 入门版（必做）

1. 写三个商品卡片，用 `data-id`/`data-price` 携带数据；
2. 用事件委托：点击卡片时读取 `dataset` 并在页面显示“你选择了 xx 号商品”；
3. 用 `dataset` 动态修改 `data-stock`，观察 DOM 属性同步变化。

### 进阶版（选做）

1. 用 `[data-state]` 实现选项卡的高亮切换；
2. 做一个“购物车数量”徽章：点击商品时更新 `data-count` 并驱动 CSS 显示；
3. 对比 `dataset` 与 `getAttribute` 在大量元素上的性能差异。

## 10. 核心知识点

> 一句话记住 data-*：`data-` 是便签，`dataset` 是抽屉；连字符转驼峰，值都是字符串；轻量数据用它，复杂状态交给 JS。

- `data-*` 属性为开发者保留，浏览器不产生内置行为；
- `dataset` 读写自动映射：`data-user-id` ↔ `dataset.userId`；
- 所有值都是字符串，数字需 `Number()` 转换；
- 事件委托 + `closest('[data-id]')` 是列表场景的标准组合；
- CSS 属性选择器可直接基于 `data-*` 控制样式；
- 不存敏感数据，不用它替代组件状态。

## 11. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 存敏感数据 | 属性对 DOM 可见，可被脚本读取 | Token 放 HttpOnly Cookie |
| 存复杂对象 | 只能存字符串，序列化成本高 | 用 JS 变量/状态管理 |
| 值类型混淆 | `data-count="3"` 是字符串 | 读取后显式 `Number()` |
| 驼峰写在 HTML | 命名不一致，解析混乱 | HTML 统一连字符小写 |
| 滥用做样式钩子 | 与语义属性混淆 | 状态用 `data-state` 约定并文档化 |
| 性能敏感场景全量用 dataset | 大量读写有开销 | 热点数据放 JS 内存 |

## 12. 扩展学习

- 属性操作：`javascript/027-DOMOperationEvent` 中 `getAttribute`/`setAttribute` 全解；
- 事件委托：`javascript/027-DOMOperationEvent` 事件冒泡与委托模式；
- 组件实践：`html5/018-WebComponentsPWADevelopment` 自定义元素中 `observedAttributes`；
- 测试钩子：`javascript/048-TypicalProjectPractice` 中 `data-testid` 的 E2E 约定。
