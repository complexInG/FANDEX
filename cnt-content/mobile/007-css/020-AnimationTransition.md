# CSS 动画与过渡速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 过渡 transition

**基本写法：transition 单属性**
`transition: <属性> <时长> <缓动> <延迟>;`
```css
/* 颜色过渡 0.3 秒 */
.button {
  transition: color 0.3s ease;
}
```

---

**基本写法：transition 多属性**
`transition: <属性1> <时长>, <属性2> <时长>;`
```css
/* 多属性分别过渡 */
.card {
  transition: transform 0.3s ease, opacity 0.5s ease;
}
```

---

**基本写法：transition all**
`transition: all <时长> <缓动>;`
```css
/* 所有属性过渡 */
.box {
  transition: all 0.3s ease;
}
```

---

**基本写法：分别设置**
`transition-property: <属性>; transition-duration: <时长>; transition-timing-function: <缓动>; transition-delay: <延迟>;`
```css
/* 分属性设置过渡 */
.box {
  transition-property: transform, opacity;
  transition-duration: 0.3s, 0.5s;
  transition-timing-function: ease-in-out;
  transition-delay: 0s, 0.1s;
}
```

---

**基本写法：缓动函数**
`transition-timing-function: linear | ease | ease-in | ease-out | ease-in-out;`
```css
/* 不同缓动效果 */
.ease-out {
  transition-timing-function: ease-out;
}
```

---

**基本写法：cubic-bezier 自定义缓动**
`transition-timing-function: cubic-bezier(<x1>, <y1>, <x2>, <y2>);`
```css
/* 自定义贝塞尔曲线 */
.custom {
  transition-timing-function: cubic-bezier(0.68, -0.55, 0.27, 1.55);
}
```

---

**基本写法：steps 阶跃**
`transition-timing-function: steps(<步数>, jump-start|jump-end|jump-none|jump-both);`
```css
/* 5 步阶跃动画 */
.steps {
  transition-timing-function: steps(5, end);
}
```

---

## 关键帧动画 @keyframes

**换行写法：定义关键帧**
`@keyframes <名称> { from { } to { } }`
```css
/* 从透明到不透明 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

---

**换行写法：百分比关键帧**
`@keyframes <名称> { 0% {} 50% {} 100% {} }`
```css
/* 多阶段动画 */
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}
```

---

**基本写法：使用动画**
`animation: <名称> <时长> <缓动> <延迟> <次数> <方向> <填充> <状态>;`
```css
/* 应用动画 */
.element {
  animation: fadeIn 1s ease 0s 1 normal forwards;
}
```

---

**基本写法：animation 简写**
`animation: <名称> <时长> <次数>;`
```css
/* 简写常用属性 */
.element {
  animation: bounce 1s infinite;
}
```

---

**基本写法：循环播放**
`animation-iteration-count: infinite;`
```css
/* 无限循环动画 */
.spinner {
  animation: spin 2s linear infinite;
}
```

---

**基本写法：交替方向**
`animation-direction: alternate;`
```css
/* 来回交替播放 */
.pulse {
  animation: pulse 1s ease-in-out infinite alternate;
}
```

---

**基本写法：填充模式**
`animation-fill-mode: none | forwards | backwards | both;`
```css
/* 保持结束状态 */
.element {
  animation: fadeIn 1s forwards;
}
```

---

**基本写法：暂停与播放**
`animation-play-state: running | paused;`
```css
/* 鼠标悬停暂停动画 */
.carousel:hover {
  animation-play-state: paused;
}
```

---

## 变换 transform

**基本写法：translate 平移**
`transform: translate(<x>, <y>);`
```css
/* 平移元素 */
.box {
  transform: translate(50px, 100px);
}
```

---

**基本写法：translateX/Y 单向平移**
`transform: translateX(<值>);`
```css
/* 水平平移 */
.box {
  transform: translateX(50px);
}
```

---

**基本写法：scale 缩放**
`transform: scale(<比例>);`
```css
/* 放大 1.5 倍 */
.box {
  transform: scale(1.5);
}
```

---

**基本写法：rotate 旋转**
`transform: rotate(<角度>);`
```css
/* 旋转 45 度 */
.box {
  transform: rotate(45deg);
}
```

---

**基本写法：skew 倾斜**
`transform: skew(<x角度>, <y角度>);`
```css
/* 倾斜变形 */
.box {
  transform: skew(10deg, 5deg);
}
```

---

**基本写法：组合变换**
`transform: translate() rotate() scale();`
```css
/* 多个变换组合 */
.box {
  transform: translate(50px, 0) rotate(45deg) scale(1.2);
}
```

---

**基本写法：3D 变换**
`transform: perspective(<距离>) rotateY(<角度>);`
```css
/* 3D 翻转效果 */
.card {
  transform: perspective(1000px) rotateY(180deg);
}
```

---

**基本写法：transform-origin 变换原点**
`transform-origin: <x> <y>;`
```css
/* 设置变换原点 */
.box {
  transform-origin: top left;
  transform: rotate(45deg);
}
```

---

## 滚动驱动动画（2024+）

**基本写法：scroll-timeline 滚动时间线**
`animation-timeline: scroll();`
```css
/* 进度条随滚动增长 */
.progress {
  animation: grow linear;
  animation-timeline: scroll();
}
@keyframes grow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

---

**基本写法：view-timeline 视图时间线**
`animation-timeline: view();`
```css
/* 元素进入视口时动画 */
.card {
  animation: fade-in linear;
  animation-timeline: view();
}
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

---

**基本写法：指定滚动轴**
`animation-timeline: scroll(nearest block);`
```css
/* 指定最近滚动容器块轴 */
.element {
  animation-timeline: scroll(nearest block);
}
```

---

## 视图过渡 View Transitions（2023+）

**基本写法：视图过渡基础**
`view-transition-name: <名称>;`
```css
/* 为元素命名参与视图过渡 */
.hero {
  view-transition-name: hero-image;
}
```

---

**换行写法：自定义过渡动画**
`::view-transition-<名称> { animation: <名称> <时长>; }`
```css
/* 自定义视图过渡动画 */
::view-transition-old(hero-image) {
  animation: fade-out 0.3s;
}
::view-transition-new(hero-image) {
  animation: fade-in 0.3s;
}
```

---

## 性能优化

**基本写法：will-change 提示**
`will-change: <属性>;`
```css
/* 提示浏览器预先优化 */
.animated {
  will-change: transform, opacity;
}
```

---

**基本写法：优先 transform 与 opacity**
`transform: translate3d(<x>, <y>, 0);`
```css
/* 触发 GPU 加速的变换 */
.box {
  transform: translate3d(0, 0, 0);
}
```

---

**基本写法：contain 性能隔离**
`contain: layout | paint | style | size;`
```css
/* 隔离元素提升渲染性能 */
.widget {
  contain: layout paint style;
}
```

---

**基本写法：content-visibility 虚拟内容**
`content-visibility: auto;`
```css
/* 视口外内容跳过渲染 */
.long-list-item {
  content-visibility: auto;
  contain-intrinsic-size: 100px;
}
```

---

## 常见动画模式

**换行写法：加载旋转**
`@keyframes spin { to { transform: rotate(360deg); } }`
```css
/* 加载旋转动画 */
@keyframes spin {
  to { transform: rotate(360deg); }
}
.spinner {
  animation: spin 1s linear infinite;
}
```

---

**换行写法：脉冲效果**
`@keyframes pulse { 50% { transform: scale(1.1); } }`
```css
/* 脉冲缩放效果 */
@keyframes pulse {
  50% { transform: scale(1.1); }
}
.pulse {
  animation: pulse 1.5s ease-in-out infinite;
}
```

---

**换行写法：抖动效果**
`@keyframes shake { 25% { transform: translateX(-5px); } 75% { transform: translateX(5px); } }`
```css
/* 左右抖动 */
@keyframes shake {
  25% { transform: translateX(-5px); }
  75% { transform: translateX(5px); }
}
.shake {
  animation: shake 0.3s ease-in-out;
}
```

---

**换行写法：淡入上移**
`@keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }`
```css
/* 淡入上移进入动画 */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.enter {
  animation: fadeUp 0.5s ease-out;
}
```
