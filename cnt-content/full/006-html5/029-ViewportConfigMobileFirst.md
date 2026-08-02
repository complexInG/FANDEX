---
order: 290
title: 视口配置与移动优先
module: 'html5'
category: 前端技术
difficulty: beginner
description: viewport、移动优先设计
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/027-CustomDataAttribute'
  - 'html5/028-CrossDocumentCommunication'
  - 'html5/030-HTML5ProjectExampleInteractiveFormApplication'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：没有 viewport，手机就“假装是电脑”

早期手机浏览器为了显示桌面网页，会把页面按 980px 宽度渲染再缩小——结果字小得看不清。`<meta name="viewport">` 告诉浏览器“按设备宽度渲染”，是移动端适配的第一行代码。

把 viewport 想象成“画框”：`width=device-width` 让画框等于屏幕宽度，`initial-scale=1.0` 让内容不缩放。少了这行配置，移动优先设计无从谈起。

## 1. 视口概念

| 视口类型     | 说明                          |
| ------------ | ----------------------------- |
| **布局视口** | 浏览器用于计算 CSS 布局的视口 |
| **视觉视口** | 用户实际看到的区域            |
| **理想视口** | 设备屏幕的理想尺寸            |

```javascript
console.log(document.documentElement.clientWidth); // 布局视口
console.log(window.visualViewport.width); // 视觉视口
```

**讲解：**

- 布局视口决定 CSS 百分比与媒体查询的基准；
- 视觉视口是用户当前看到的区域，放大页面时会变化；
- 理想视口是设备推荐尺寸，`device-width` 就是取它的宽度。

## 2. viewport meta 标签

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

| 属性            | 值                 | 说明             |
| --------------- | ------------------ | ---------------- |
| `width`         | device-width       | 布局视口宽度     |
| `initial-scale` | 1.0                | 初始缩放比例     |
| `maximum-scale` | 1.0-10.0           | 最大缩放比例     |
| `user-scalable` | yes/no             | 是否允许用户缩放 |
| `viewport-fit`  | auto/contain/cover | 适配刘海屏       |

> **可访问性警告**：禁止用户缩放会影响视力不佳的用户，WCAG 要求支持 200% 缩放。

**讲解：** `width=device-width` + `initial-scale=1.0` 是标准组合；`viewport-fit=cover` 用于全面屏；不要设置 `user-scalable=no` 或过小的 `maximum-scale`，否则违反可访问性要求。

## 3. 设备像素比

$$
\text{DPR} = \frac{\text{物理像素}}{\text{CSS 像素}}
$$

```javascript
console.log(window.devicePixelRatio); // 1, 2, 3 等
```

**讲解：** DPR = 物理像素 / CSS 像素。DPR 为 2 的屏幕，一个 CSS 像素对应 4 个物理像素；开发时用 CSS 像素思考，图片资源按 DPR 提供 2x/3x 版本。

## 4. 移动优先设计

```css
/* 移动优先：基础样式 */
.container {
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

/* 平板 */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    flex-direction: row;
  }
}

/* 桌面 */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

## 5. 安全区域适配

```css
.header {
  padding-top: env(safe-area-inset-top);
}
.footer {
  padding-bottom: env(safe-area-inset-bottom);
}
```

## 6. 响应式断点

| 断点 | 宽度     | 设备   |
| ---- | -------- | ------ |
| xs   | < 576px  | 手机   |
| sm   | ≥ 576px  | 大手机 |
| md   | ≥ 768px  | 平板   |
| lg   | ≥ 992px  | 小桌面 |
| xl   | ≥ 1200px | 桌面   |

## 7. 进阶知识点

### 7.1 VisualViewport API

```javascript
window.visualViewport.addEventListener('resize', () => {
  console.log('视觉视口:', window.visualViewport.width);
});
```

**讲解：**

- 移动端键盘弹出、页面缩放时视觉视口变化，布局视口不变；
- `visualViewport` 事件可用于“输入框被键盘遮挡”等场景的自动滚动；
- 桌面浏览器同样支持，可用于缩放监听的统一实现。

### 7.2 触摸事件

```javascript
element.addEventListener('touchstart', (e) => {
  console.log('触摸点:', e.touches.length);
});
```

**讲解：** 触摸事件（`touchstart`/`touchmove`/`touchend`）提供触点坐标；现代开发更推荐 Pointer Events（统一鼠标/触摸/笔），需要手势识别时使用 Hammer.js 等库。

## 8. 动手试试

1. 新建一个页面，先不写 viewport meta，用手机模式预览，对比文字大小；
2. 加上 `width=device-width, initial-scale=1.0` 再对比；
3. 用开发者工具切换不同设备，观察 `clientWidth` 与 `devicePixelRatio` 的变化；
4. 进阶挑战：做一个“移动优先”的两栏布局，在 768px 断点以上变为并排。

## 9. 核心知识点

> 一句话记住 viewport：`width=device-width` 画框对齐屏幕，`initial-scale=1.0` 不缩放；`viewport-fit=cover` 管刘海，`user-scalable` 别禁用。

- 布局视口/视觉视口/理想视口是三个不同概念；
- 移动端必备：`<meta name="viewport" content="width=device-width, initial-scale=1.0">`；
- DPR = 物理像素 / CSS 像素，高清图按 2x/3x 提供；
- 移动优先：先写基础样式，再用 `min-width` 媒体查询增强；
- `env(safe-area-inset-*)` 适配刘海屏安全区域；
- 禁止缩放违反 WCAG，不要禁用用户缩放。

## 10. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 viewport meta | 手机按桌面宽度渲染，文字极小 | 每个页面都加标准 viewport |
| 固定 `maximum-scale=1` | 用户无法缩放，违反 WCAG | 移除或设合理的放大范围 |
| 只用 CSS 像素不提供高清图 | 高分屏模糊 | 按 DPR 提供 2x/3x 图片 |
| 桌面优先开发 | 移动端体验差 | 移动优先 + min-width 增强 |
| 忽略刘海屏 | 内容被遮挡 | `viewport-fit=cover` + safe-area 变量 |

## 11. 扩展学习

- 响应式：`css/019-MediaQuery` 断点与媒体查询完整语法；
- 图片适配：`html5/013-ImageResponsiveImage` 的 srcset 与 DPR；
- 移动端布局：`css/030-ResponsiveDesign` 响应式设计模式；
- 安全区域：Apple 的 safe-area-inset 文档与 `env()` 函数用法。
