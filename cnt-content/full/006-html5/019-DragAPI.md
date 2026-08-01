---
order: 60
title: 拖拽API
module: html5
category: HTML5
difficulty: intermediate
description: drag/drop
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/progress与meter
  - html5/WebComponents与PWA开发
  - html5/地理位置定位
  - html5/Web工作线程
prerequisites:
  - html5/概述与核心特性
---
## 1. 拖拽 API 概述

HTML5 原生拖拽 API 允许用户通过拖拽操作在页面内或页面间移动元素和数据。

### 1.1 事件

| 事件        | 触发时机           | 用途                    |
| ----------- | ------------------ | ----------------------- |
| `dragstart` | 开始拖拽           | 设置拖拽数据            |
| `drag`      | 拖拽过程中持续触发 | 更新状态                |
| `dragend`   | 拖拽结束           | 清理状态                |
| `dragenter` | 拖拽进入目标       | 高亮放置区域            |
| `dragover`  | 拖拽在目标上方     | **必须 preventDefault** |
| `dragleave` | 拖拽离开目标       | 取消高亮                |
| `drop`      | 在目标上释放       | 处理放置逻辑            |

## 2. 基本实现

```html
<div id="draggable" draggable="true">拖拽我</div>
<div id="dropzone">放置区域</div>
```

```javascript
const draggable = document.getElementById('draggable');
const dropzone = document.getElementById('dropzone');

draggable.addEventListener('dragstart', (e) => {
  e.dataTransfer.setData('text/plain', e.target.id);
  e.dataTransfer.effectAllowed = 'move';
});

dropzone.addEventListener('dragover', (e) => {
  e.preventDefault(); // 必须！否则无法触发 drop
});

dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  const id = e.dataTransfer.getData('text/plain');
  dropzone.appendChild(document.getElementById(id));
});
```

## 3. DataTransfer 对象

```javascript
e.dataTransfer.setData('text/plain', '文本数据');
e.dataTransfer.setData('application/json', JSON.stringify({ id: 1 }));
e.dataTransfer.effectAllowed = 'move';
e.dataTransfer.dropEffect = 'copy';

// 自定义拖拽图像
const img = new Image();
img.src = 'drag-icon.png';
e.dataTransfer.setDragImage(img, 0, 0);
```

## 4. 文件拖拽

```javascript
dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  const files = e.dataTransfer.files;
  for (const file of files) {
    console.log(`文件名: ${file.name}, 大小: ${file.size} bytes`);
  }
});
```
## draggable 属性

**启用元素拖拽**
`<element draggable="true | false">`

```html
<!-- 将元素标记为可拖拽 -->
<div id="draggable" draggable="true">拖拽我</div>
<div id="dropzone">放置区域</div>

<!-- 图片和带 href 的链接默认可拖拽,无需设置 -->
<img src="logo.png" alt="Logo" />
<a href="/page">链接</a>
```

---

## 拖拽事件

**事件触发顺序表**

| 事件        | 触发对象   | 触发时机             | 用途                    |
| ----------- | ---------- | -------------------- | ----------------------- |
| `dragstart` | 拖拽元素   | 开始拖拽             | 设置拖拽数据            |
| `drag`      | 拖拽元素   | 拖拽过程中持续触发   | 更新状态                |
| `dragend`   | 拖拽元素   | 拖拽结束             | 清理状态                |
| `dragenter` | 放置目标   | 拖拽进入目标         | 高亮放置区域            |
| `dragover`  | 放置目标   | 拖拽在目标上方移动   | **必须 preventDefault** |
| `dragleave` | 放置目标   | 拖拽离开目标         | 取消高亮                |
| `drop`      | 放置目标   | 在目标上释放         | 处理放置逻辑            |

---

## 基本拖拽实现

**HTML 结构**
`<div draggable="true">源</div> <div>目标</div>`

```html
<!-- 拖拽源与放置目标 -->
<div id="draggable" draggable="true">拖拽我</div>
<div id="dropzone">放置区域</div>
```

**JavaScript 事件绑定**
`element.addEventListener('dragstart' | 'dragover' | 'drop', handler)`

```javascript
const draggable = document.getElementById('draggable');
const dropzone = document.getElementById('dropzone');

// 拖拽开始:设置数据与效果
draggable.addEventListener('dragstart', (e) => {
  e.dataTransfer.setData('text/plain', e.target.id); // 设置拖拽数据
  e.dataTransfer.effectAllowed = 'move';             // 允许的效果:copy | move | link
});

// 拖拽悬停:必须阻止默认行为,否则无法触发 drop
dropzone.addEventListener('dragover', (e) => {
  e.preventDefault();
  e.dataTransfer.dropEffect = 'move'; // 设置放置效果
});

// 拖拽进入:高亮目标
dropzone.addEventListener('dragenter', (e) => {
  e.preventDefault();
  dropzone.classList.add('drag-over');
});

// 拖拽离开:取消高亮
dropzone.addEventListener('dragleave', () => {
  dropzone.classList.remove('drag-over');
});

// 放置:处理数据
dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropzone.classList.remove('drag-over');
  const id = e.dataTransfer.getData('text/plain'); // 获取拖拽数据
  const draggedEl = document.getElementById(id);
  dropzone.appendChild(draggedEl);
});
```

---

## DataTransfer 对象

**DataTransfer 方法表**

| 方法                              | 说明                          |
| --------------------------------- | ----------------------------- |
| `setData(format, data)`           | 设置指定格式的数据            |
| `getData(format)`                 | 读取指定格式的数据            |
| `clearData([format])`             | 清除数据                      |
| `setDragImage(img, x, y)`         | 设置自定义拖拽图像            |
| `types`                           | 只读属性,数据格式数组        |
| `files`                           | 只读属性,FileList 对象       |
| `items`                           | 只读属性,DataTransferItemList |

**常用数据格式**
`e.dataTransfer.setData('text/plain' | 'text/uri-list' | 'text/html', data)`

```javascript
// 设置多种格式的数据
e.dataTransfer.setData('text/plain', '纯文本数据');
e.dataTransfer.setData('text/uri-list', 'https://example.com');
e.dataTransfer.setData('text/html', '<strong>HTML 数据</strong>');
e.dataTransfer.setData('application/json', JSON.stringify({ id: 1, name: '张三' }));

// 读取数据(在 drop 事件中)
const text = e.dataTransfer.getData('text/plain');
const json = JSON.parse(e.dataTransfer.getData('application/json'));
```

**拖拽效果设置**
`e.dataTransfer.effectAllowed = 'copy | move | link | copyMove | all | none'`

```javascript
// 设置允许的效果
e.dataTransfer.effectAllowed = 'copy';   // 仅复制
e.dataTransfer.effectAllowed = 'move';   // 仅移动
e.dataTransfer.effectAllowed = 'link';   // 仅链接
e.dataTransfer.effectAllowed = 'copyMove'; // 复制或移动

// 设置放置效果(在 dragover 事件中)
e.dataTransfer.dropEffect = 'copy'; // copy | move | link | none
```

**自定义拖拽图像**
`e.dataTransfer.setDragImage(<element>, <offsetX>, <offsetY>)`

```javascript
// 使用自定义图像作为拖拽预览
draggable.addEventListener('dragstart', (e) => {
  const img = new Image();
  img.src = 'drag-icon.png';
  e.dataTransfer.setDragImage(img, 10, 10); // 偏移量(像素)
});
```

---

## 文件拖拽

**获取拖入的文件**
`e.dataTransfer.files` 或 `e.dataTransfer.items`

```javascript
// 处理拖拽上传的文件
dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  const files = e.dataTransfer.files; // FileList 对象
  for (const file of files) {
    console.log(`文件名: ${file.name}`);
    console.log(`大小: ${file.size} bytes`);
    console.log(`类型: ${file.type}`);
    console.log(`最后修改: ${new Date(file.lastModified).toLocaleString()}`);
  }
});
```

**异步读取文件内容**
`file.text() | file.arrayBuffer() | reader.readAsDataURL(file)`

```javascript
// 读取文本文件
const text = await file.text();

// 读取为 ArrayBuffer
const buffer = await file.arrayBuffer();

// 使用 FileReader 读取为 Data URL(图片预览)
const reader = new FileReader();
reader.onload = (e) => {
  const img = document.createElement('img');
  img.src = e.target.result;
  document.body.appendChild(img);
};
reader.readAsDataURL(file);
```

---

## 拖拽方向控制

**仅允许垂直/水平拖拽**
`if (Math.abs(dx) > Math.abs(dy)) { ... }`

```javascript
// 限制为水平拖拽
let isDragging = false;
let startX, startY;

element.addEventListener('mousedown', (e) => {
  isDragging = true;
  startX = e.clientX;
  startY = e.clientY;
});

document.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  const dx = e.clientX - startX;
  const dy = e.clientY - startY;
  // 仅水平方向有效
  if (Math.abs(dx) > Math.abs(dy)) {
    element.style.left = `${dx}px`;
  }
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});
```

---

## 注意事项

- **dragover 必须 preventDefault**:否则 `drop` 事件不会触发
- **数据类型一致性**:`setData` 和 `getData` 的 format 参数必须完全一致
- **安全性**:拖拽内容来源不可信时,需进行数据校验,防止 XSS
- **触摸设备**:原生 HTML5 拖拽 API 在移动端支持有限,需使用 polyfill 或自定义实现
- **可访问性**:拖拽操作对屏幕阅读器不友好,需提供等价的非拖拽操作方式(如按钮)
- **DataTransfer 生命周期**:`getData` 仅在 `drop` 事件中可读取,`dragstart` 中设置的数据在 `dragover` 中无法读取

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| HTML5 概述与核心特性 | 001-HTML5OverviewCoreFeature | 本文的前置基础 |
| HTML5 基础标签与全局属性 | 002-HTML5BasicTagGlobalAttribute | 本文的前置基础 |
| 语义化标签 | 003-SemanticTag | 本文的并列主题 |
| 无障碍访问 | 004-Accessibility | 本文的并列主题 |
| HTML5 表单与验证 | 005-HTML5FormValidation | 本文的并列主题 |
| HTML5 多媒体与 Canvas 绘图 | 006-HTML5MultimediaCanvasDrawing | 本文的并列主题 |
| 文档类型声明 | 007-DocTypeDeclaration | 本文的并列主题 |
| HTML5 离线存储与 Web API | 008-HTML5OfflineStorageWebAPI | 本文的并列主题 |
| 元数据与字符编码 | 009-MetadataCharacterEncoding | 本文的并列主题 |
| 文本语义 | 010-TextSemantic | 本文的并列主题 |
| 列表 | 011-List | 本文的并列主题 |
| 链接与锚点 | 012-LinkageAnchor | 本文的并列主题 |
| 图像与响应式图片 | 013-ImageResponsiveImage | 本文的并列主题 |
| 音频与视频 | 014-AudioVideo | 本文的并列主题 |
| SVG | 015-SVG | 本文的并列主题 |
| 嵌入式内容 | 016-EmbeddedContent | 本文的并列主题 |
| progress与meter | 017-ProgressMeter | 本文的并列主题 |
| Web Components 与 PWA 开发 | 018-WebComponentsPWADevelopment | 本文的并列主题 |
| 拖拽API | 019-DragAPI | 本文自身 |
| 地理位置定位 | 020-Geolocation | 本文的并列主题 |
| Web-Workers | 021-WebWorkers | 本文的并列主题 |
| Service-Worker与PWA | 022-ServiceWorkerPWA | 本文的并列主题 |
| History-API | 023-HistoryAPI | 本文的并列主题 |
| WebSocket | 024-WebSocket | 本文的并列主题 |
| WebRTC | 025-WebRTC | 本文的并列主题 |
| 微数据与JSON-LD | 026-MicrodataJSONLD | 本文的并列主题 |
| 自定义数据属性 | 027-CustomDataAttribute | 本文的并列主题 |
| 跨文档通信 | 028-CrossDocumentCommunication | 本文的并列主题 |
| 视口配置与移动优先 | 029-ViewportConfigMobileFirst | 本文的并列主题 |
| HTML5 项目示例：交互式表单应用 | 030-HTML5ProjectExampleInteractiveFormApplication | 本文的综合应用 |
