# CSS 定位与浮动速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## position 定位

**基本写法：static 静态定位**
`position: static;`
```css
/* 默认静态定位不脱离文档流 */
.box {
  position: static;
}
```

---

**基本写法：relative 相对定位**
`position: relative;`
```css
/* 相对原位置偏移 */
.box {
  position: relative;
  top: 10px;
  left: 20px;
}
```

---

**基本写法：absolute 绝对定位**
`position: absolute;`
```css
/* 相对最近已定位祖先 */
.box {
  position: absolute;
  top: 0;
  right: 0;
}
```

---

**基本写法：fixed 固定定位**
`position: fixed;`
```css
/* 相对视口固定 */
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}
```

---

**基本写法：sticky 粘性定位**
`position: sticky;`
```css
/* 滚动到阈值时固定 */
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
}
```

---

## 偏移属性

**基本写法：top 顶部偏移**
`top: <值>;`
```css
/* 距离顶部 50px */
.box {
  position: absolute;
  top: 50px;
}
```

---

**基本写法：right 右侧偏移**
`right: <值>;`
```css
/* 距离右侧 20px */
.box {
  position: absolute;
  right: 20px;
}
```

---

**基本写法：bottom 底部偏移**
`bottom: <值>;`
```css
/* 距离底部 0 */
.footer {
  position: fixed;
  bottom: 0;
}
```

---

**基本写法：left 左侧偏移**
`left: <值>;`
```css
/* 距离左侧 100px */
.box {
  position: absolute;
  left: 100px;
}
```

---

**基本写法：inset 简写**
`inset: <上> <右> <下> <左>;`
```css
/* 同时设置四个偏移 */
.box {
  position: absolute;
  inset: 10px 20px 10px 20px;
}
```

---

**基本写法：inset 单值**
`inset: <值>;`
```css
/* 四个方向相同偏移 */
.fullscreen {
  position: absolute;
  inset: 0;
}
```

---

## z-index 层级

**基本写法：z-index 层叠顺序**
`z-index: <数值>;`
```css
/* 设置层叠顺序 */
.modal {
  position: fixed;
  z-index: 1000;
}
```

---

**基本写法：负 z-index**
`z-index: -1;`
```css
/* 置于普通元素之后 */
.bg-image {
  position: absolute;
  z-index: -1;
}
```

---

**基本写法：auto 自动层级**
`z-index: auto;`
```css
/* 默认自动层叠顺序 */
.box {
  position: relative;
  z-index: auto;
}
```

---

## 层叠上下文

**基本写法：isolation 隔离层叠**
`isolation: isolate;`
```css
/* 创建独立层叠上下文 */
.modal {
  isolation: isolate;
}
```

---

**基本写法：transform 创建层叠上下文**
`transform: translateZ(0);`
```css
/* transform 创建层叠上下文 */
.box {
  position: relative;
  transform: translateZ(0);
  z-index: 1;
}
```

---

**基本写法：opacity 创建层叠上下文**
`opacity: 0.99;`
```css
/* opacity 小于 1 创建层叠上下文 */
.overlay {
  position: absolute;
  opacity: 0.99;
}
```

---

## 浮动 float

**基本写法：左浮动**
`float: left;`
```css
/* 元素左浮动 */
.thumbnail {
  float: left;
  margin-right: 10px;
}
```

---

**基本写法：右浮动**
`float: right;`
```css
/* 元素右浮动 */
.sidebar {
  float: right;
  width: 300px;
}
```

---

**基本写法：不浮动**
`float: none;`
```css
/* 取消浮动 */
.box {
  float: none;
}
```

---

**基本写法：inline-start 起始方向浮动**
`float: inline-start;`
```css
/* 根据书写方向浮动到起始边 */
.icon {
  float: inline-start;
}
```

---

## 清除浮动

**基本写法：clear 清除**
`clear: left | right | both;`
```css
/* 清除两侧浮动 */
.footer {
  clear: both;
}
```

---

**基本写法：clearfix 经典清除**
`.clearfix::after { content: ""; display: table; clear: both; }`
```css
/* 经典清除浮动方案 */
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

---

**基本写法：clearfix 现代写法**
`.clearfix { display: flow-root; }`
```css
/* 现代清除浮动方案 */
.container {
  display: flow-root;
}
```

---

## 常见布局模式

**基本写法：文字环绕图片**
`float: left;`
```css
/* 图片浮动文字环绕 */
.article img {
  float: left;
  margin: 0 15px 5px 0;
}
.article p {
  overflow: hidden;
}
```

---

**基本写法：两栏布局浮动**
`float: left; float: right;`
```css
/* 浮动两栏布局 */
.sidebar {
  float: left;
  width: 250px;
}
.main {
  margin-left: 270px;
}
```

---

**基本写法：绝对定位居中**
`position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);`
```css
/* 绝对定位实现居中 */
.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

---

**基本写法：绝对定位 margin auto 居中**
`position: absolute; inset: 0; margin: auto;`
```css
/* margin auto 实现居中 */
.center {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 200px;
  height: 200px;
}
```

---

**基本写法：粘性导航栏**
`position: sticky; top: 0;`
```css
/* 滚动吸顶导航 */
.navbar {
  position: sticky;
  top: 0;
  background: white;
  z-index: 100;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

---

**基本写法：固定侧边栏**
`position: fixed;`
```css
/* 固定侧边栏 */
.sidebar {
  position: fixed;
  top: 60px;
  left: 0;
  bottom: 0;
  width: 250px;
  overflow-y: auto;
}
.main {
  margin-left: 250px;
}
```

---

**基本写法：模态框居中**
`position: fixed; inset: 0;`
```css
/* 全屏模态框居中 */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

**基本写法：工具提示定位**
`position: absolute;`
```css
/* 相对父元素绝对定位 */
.tooltip-wrapper {
  position: relative;
}
.tooltip {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
}
```

---

## 现代 CSS 锚点定位（2024+）

**基本写法：anchor-name 定义锚点**
`anchor-name: --<名称>;`
```css
/* 定义锚点元素 */
.button {
  anchor-name: --my-button;
}
```

---

**基本写法：position absolute 锚定**
`position: absolute; anchor-default: --<名称>;`
```css
/* 工具提示锚定到按钮 */
.tooltip {
  position: absolute;
  anchor-default: --my-button;
  top: anchor(bottom);
  left: anchor(center);
}
```

---

**基本写法：anchor 定位函数**
`top: anchor(<位置>);`
```css
/* 基于锚点位置定位 */
.tooltip {
  position: absolute;
  top: anchor(--btn bottom);
  left: anchor(--btn center);
  transform: translateX(-50%);
}
```

---

**基本写法：position-try 锚点避让**
`position-try: flip-block;`
```css
/* 空间不足时自动翻转 */
.tooltip {
  position: absolute;
  top: anchor(bottom);
  position-try: flip-block, flip-inline;
}
```

---

**基本写法：position-anchor 关联锚点**
`position-anchor: --<名称>;`
```css
/* 显式关联锚点 */
.tooltip {
  position: absolute;
  position-anchor: --my-button;
  top: anchor(bottom);
}
```
