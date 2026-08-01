# CSS 响应式设计速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 媒体查询基础

**基本写法：max-width 最大宽度**
`@media (max-width: <值>) { }`
```css
/* 宽度小于等于 768px 时生效 */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

---

**基本写法：min-width 最小宽度**
`@media (min-width: <值>) { }`
```css
/* 宽度大于等于 1024px 时生效 */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
  }
}
```

---

**基本写法：范围查询**
`@media (min-width: <值>) and (max-width: <值>) { }`
```css
/* 平板尺寸范围 */
@media (min-width: 768px) and (max-width: 1024px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

---

**基本写法：screen 设备类型**
`@media screen and (max-width: <值>) { }`
```css
/* 仅屏幕设备生效 */
@media screen and (max-width: 768px) {
  .sidebar {
    display: none;
  }
}
```

---

**基本写法：print 打印样式**
`@media print { }`
```css
/* 打印时隐藏元素 */
@media print {
  .no-print {
    display: none;
  }
}
```

---

## 断点系统

**基本写法：移动优先断点**
`@media (min-width: <断点>) { }`
```css
/* 移动优先从小到大 */
/* 默认移动端样式 */
.container { padding: 10px; }
/* 平板 */
@media (min-width: 768px) {
  .container { padding: 20px; }
}
/* 桌面 */
@media (min-width: 1024px) {
  .container { padding: 30px; }
}
```

---

**基本写法：桌面优先断点**
`@media (max-width: <断点>) { }`
```css
/* 桌面优先从大到小 */
.container { padding: 30px; }
@media (max-width: 1024px) {
  .container { padding: 20px; }
}
@media (max-width: 768px) {
  .container { padding: 10px; }
}
```

---

## 媒体特性

**基本写法：orientation 方向**
`@media (orientation: landscape | portrait) { }`
```css
/* 横屏时生效 */
@media (orientation: landscape) {
  .video {
    height: 100vh;
  }
}
```

---

**基本写法：prefers-color-scheme 暗色模式**
`@media (prefers-color-scheme: dark) { }`
```css
/* 跟随系统暗色模式 */
@media (prefers-color-scheme: dark) {
  body {
    background: #1a1a1a;
    color: #fff;
  }
}
```

---

**基本写法：prefers-reduced-motion 减少动画**
`@media (prefers-reduced-motion: reduce) { }`
```css
/* 用户偏好减少动画 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms;
    transition-duration: 0.01ms;
  }
}
```

---

**基本写法：prefers-contrast 高对比度**
`@media (prefers-contrast: more) { }`
```css
/* 高对比度偏好 */
@media (prefers-contrast: more) {
  .text {
    color: black;
    background: white;
  }
}
```

---

**基本写法：hover 悬停支持**
`@media (hover: hover) { }`
```css
/* 仅支持悬停设备生效 */
@media (hover: hover) {
  .button:hover {
    background: #2980b9;
  }
}
```

---

**基本写法：pointer 指针类型**
`@media (pointer: fine | coarse) { }`
```css
/* 粗指针（触摸屏）放大点击区域 */
@media (pointer: coarse) {
  .button {
    padding: 16px 24px;
  }
}
```

---

## 容器查询（2023+）

**基本写法：container-type 容器类型**
`container-type: inline-size;`
```css
/* 定义查询容器 */
.card {
  container-type: inline-size;
}
```

---

**基本写法：container-name 命名容器**
`container-name: <名称>;`
```css
/* 命名容器便于区分 */
.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}
```

---

**基本写法：container 简写**
`container: <名称> / <类型>;`
```css
/* 简写定义容器 */
.sidebar {
  container: sidebar / inline-size;
}
```

---

**基本写法：@container 查询**
`@container (<条件>) { }`
```css
/* 容器宽度小于 400px 时 */
.card {
  container-type: inline-size;
}
@container (max-width: 400px) {
  .card-title {
    font-size: 14px;
  }
}
```

---

**基本写法：命名容器查询**
`@container <名称> (<条件>) { }`
```css
/* 查询指定命名容器 */
@container sidebar (min-width: 200px) {
  .widget {
    display: grid;
  }
}
```

---

**基本写法：容器查询单位 cqi**
`font-size: <数值>cqi;`
```css
/* 基于容器内联尺寸的字体 */
.title {
  font-size: 5cqi;
}
```

---

**基本写法：容器查询单位列表**
`<数值>cqw | cqh | cqi | cqb | cqmin | cqmax;`
```css
/* 各类容器查询单位 */
.box {
  width: 50cqw;   /* 容器宽度 50% */
  height: 30cqh;  /* 容器高度 30% */
  font-size: 3cqmin;  /* 容器较小边 3% */
}
```

---

## 响应式排版

**基本写法：流式字体**
`font-size: clamp(<最小>, <理想>, <最大>);`
```css
/* 流式响应字体 */
h1 {
  font-size: clamp(1.5rem, 5vw, 3rem);
}
```

---

**基本写法：rem + vw 组合**
`font-size: calc(<rem> + <vw>);`
```css
/* 兼顾缩放与视口 */
p {
  font-size: calc(1rem + 0.5vw);
}
```

---

**基本写法：响应式间距**
`padding: clamp(<最小>, <理想>, <最大>);`
```css
/* 流式响应间距 */
.section {
  padding: clamp(1rem, 4vw, 3rem);
}
```

---

## 响应式图片

**基本写法：max-width 图片自适应**
`max-width: 100%; height: auto;`
```css
/* 图片自适应容器宽度 */
img {
  max-width: 100%;
  height: auto;
}
```

---

**基本写法：aspect-ratio 保持比例**
`aspect-ratio: <宽> / <高>;`
```css
/* 保持 16:9 比例 */
.video {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```

---

**基本写法：picture 源切换**
`<picture><source><img></picture>`
```css
/* 配合 picture 元素响应式图片 */
/* HTML: <picture>
  <source media="(min-width: 800px)" srcset="large.jpg">
  <img src="small.jpg">
</picture> */
img {
  max-width: 100%;
}
```

---

**基本写法：object-fit 图片裁剪**
`object-fit: cover | contain | fill;`
```css
/* 图片填充方式 */
.avatar {
  width: 100px;
  height: 100px;
  object-fit: cover;
}
```

---

## 响应式布局模式

**基本写法：移动优先 flex 切换**
`display: flex; @media (min-width: <值>) { flex-direction: row; }`
```css
/* 移动端列桌面端行 */
.nav {
  display: flex;
  flex-direction: column;
}
@media (min-width: 768px) {
  .nav {
    flex-direction: row;
  }
}
```

---

**基本写法：响应式网格列数**
`grid-template-columns: 1fr; @media (min-width: <值>) { repeat(<n>, 1fr); }`
```css
/* 不同屏幕不同列数 */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

---

**基本写法：auto-fit 自动响应**
`grid-template-columns: repeat(auto-fit, minmax(<最小>, 1fr));`
```css
/* 无需媒体查询的自适应网格 */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

---

**基本写法：隐藏显示元素**
`display: none; @media (min-width: <值>) { display: block; }`
```css
/* 小屏隐藏大屏显示 */
.sidebar {
  display: none;
}
@media (min-width: 1024px) {
  .sidebar {
    display: block;
  }
}
```

---

## 新媒体特性（2024+）

**基本写法：prefers-reduced-transparency**
`@media (prefers-reduced-transparency: reduce) { }`
```css
/* 减少透明度偏好 */
@media (prefers-reduced-transparency: reduce) {
  .overlay {
    opacity: 1;
  }
}
```

---

**基本写法：prefers-reduced-data**
`@media (prefers-reduced-data: reduce) { }`
```css
/* 减少数据使用偏好 */
@media (prefers-reduced-data: reduce) {
  .hero-video {
    display: none;
  }
}
```

---

**基本写法：环境范围查询**
`@media (width >= <值>) { }`
```css
/* 现代范围语法 */
@media (width >= 768px) {
  .container {
    max-width: 1200px;
  }
}
```

---

**基本写法：范围组合简写**
`@media (768px <= width <= 1024px) { }`
```css
/* 范围简写语法 */
@media (768px <= width <= 1024px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```
