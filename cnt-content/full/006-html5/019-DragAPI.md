---
order: 190
title: 拖拽API
module: 'html5'
category: 前端技术
difficulty: intermediate
description: drag/drop
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/017-ProgressMeter'
  - 'html5/018-WebComponentsPWADevelopment'
  - 'html5/020-Geolocation'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：拖拽就在你身边

把文件拖进网页上传、把卡片拖到另一个列表排序、把图片拖到画布里——这些交互都基于 HTML5 拖拽 API。

拖拽需要双方配合：被拖的元素（drag source）提供数据，放置区域（drop target）接收数据。记住一个关键点：放置区必须监听 `dragover` 并调用 `preventDefault()`，否则浏览器默认不允许放置，`drop` 事件永远不会触发。

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

**讲解：**

- 被拖元素加 `draggable="true"`，在 `dragstart` 中用 `setData` 写入要传递的数据；
- 放置区在 `dragover` 中必须 `preventDefault()`，这是能触发 `drop` 的前提；
- `drop` 中读取数据并移动元素，实现“拖到哪、放到哪”。

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

**讲解：**

- `setData(type, data)` 写入数据，`getData(type)` 读取，类型常用 `text/plain` 与 `application/json`；
- `effectAllowed` 声明源端允许的操作，`dropEffect` 声明目标端实际执行的操作（move/copy/link）；
- `setDragImage` 自定义拖拽时跟随鼠标的缩略图。

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

**讲解：**

- 拖入系统文件时，`e.dataTransfer.files` 是文件列表，与 `<input type="file">` 的 `files` 一致；
- 每个 `file` 有 `name`、`size`、`type`，可配合 FileReader 预览图片；
- 常用组合是“拖拽上传”：drop 后把文件放进 `FormData` 再 `fetch` 提交。

## 5. 进阶知识点

### 5.1 限制拖拽方向（鼠标实现）

```javascript
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
  // 只允许水平方向拖拽
  if (Math.abs(dx) > Math.abs(dy)) {
    element.style.left = `${dx}px`;
  }
});
```

**讲解：**

- 比较横向位移与纵向位移的绝对值，可以判断用户意图是“水平拖”还是“垂直拖”；
- 这种“按下-移动-释放”模式是原生 DnD 之外的另一套实现，适合滑块、调整大小等场景；
- 记住在 `mouseup` 时把 `isDragging` 复位。

## 6. 动手试试

### 入门版（必做）

先复制下面这个最小示例到本地 `drag.html`，双击打开即可试验：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>拖拽最小示例</title>
    <style>
      #box { width: 120px; height: 60px; background: #1677ff; color: #fff;
             display: flex; align-items: center; justify-content: center; }
      #zone { width: 300px; height: 160px; margin-top: 20px;
              border: 2px dashed #999; display: flex;
              align-items: center; justify-content: center; }
    </style>
  </head>
  <body>
    <div id="box" draggable="true">拖拽我</div>
    <div id="zone">放置区域</div>
    <script>
      const box = document.getElementById('box');
      const zone = document.getElementById('zone');
      box.addEventListener('dragstart', (e) => {
        e.dataTransfer.setData('text/plain', 'box');
      });
      zone.addEventListener('dragover', (e) => e.preventDefault());
      zone.addEventListener('drop', (e) => {
        e.preventDefault();
        zone.textContent = '收到：' + e.dataTransfer.getData('text/plain');
      });
    </script>
  </body>
</html>
```

1. 实现“把卡片拖到垃圾桶删除”：一个可拖元素 + 一个放置区，drop 后移除元素；
2. 在 `dragstart` 中写入 `text/plain` 数据，在 `drop` 中读取并显示；
3. 实现文件拖拽：把图片拖到区域后，用 FileReader 在页面预览。

### 进阶版（选做）

1. 做一个可拖拽排序的列表：拖起一项，移动到其它项时交换位置；
2. 用 `setDragImage` 自定义拖拽缩略图；
3. 给放置区加高亮与禁用状态，拖拽进入时变色、离开时恢复。

## 7. 核心知识点

> 一句话记住拖拽：源端 `dragstart` 写数据，目标端 `dragover` 放行、`drop` 收数据；文件拖拽看 `dataTransfer.files`。

- 被拖元素：`draggable="true"` + `dragstart`（写入数据）；
- 放置区域：`dragover` 必须 `preventDefault()`，`drop` 处理放置；
- `dataTransfer` 是数据与效果的载体：`setData`/`getData`/`effectAllowed`/`dropEffect`；
- 文件拖拽：`e.dataTransfer.files` + FileReader/FormData 实现拖拽上传；
- 生命周期：`dragstart` → `drag` → `dragend`，配合 `dragenter`/`dragleave` 做视觉反馈。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 `preventDefault()` | `drop` 永远不触发 | `dragover` 中必须放行 |
| 未设置 `draggable` | 元素不可拖 | 目标元素加 `draggable="true"` |
| 数据只在 `dragstart` 写 | 其它事件中读取为空 | 统一在 `dragstart` 中 `setData` |
| 忽略 `dropEffect` | 移动/复制行为不明确 | 按场景设置 move/copy |
| 未处理 `dragend` 清理 | 状态残留 | 结束后复位视觉状态 |
| 触屏设备不生效 | 原生 DnD 不支持触摸 | 触屏用 Pointer Events 或第三方库 |

## 9. 扩展学习

- 文件读取：`html5/008-HTML5OfflineStorageWebAPI` 中 File API；
- 触屏拖拽：`html5/020-Geolocation` 之外的 Pointer Events 教程；
- 排序组件：Vue/React 生态中的 drag-and-drop 库（vuedraggable、dnd-kit）；
- 无障碍：拖拽交互需要为键盘用户提供替代操作（如上下移动按钮）。
