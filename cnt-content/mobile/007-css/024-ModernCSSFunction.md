# 现代 CSS 函数速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## calc() 计算

**基本写法：calc 基本运算**
`calc(<值1> <运算符> <值2>);`
```css
/* 加减乘除运算 */
.box {
  width: calc(100% - 200px);
  height: calc(50vh + 50px);
  padding: calc(20px * 2);
}
```

---

**基本写法：calc 混合单位**
`calc(<单位1> <运算符> <单位2>);`
```css
/* 混合不同单位计算 */
.box {
  font-size: calc(1rem + 0.5vw);
  margin: calc(20px - 1em);
}
```

---

**基本写法：calc 嵌套**
`calc(<值> * calc(<值>));`
```css
/* calc 嵌套使用 */
.box {
  width: calc(100% - calc(200px + 2rem));
}
```

---

**基本写法：calc 配合变量**
`calc(var(--<变量>) <运算符> <值>);`
```css
/* 变量参与计算 */
.box {
  --base: 20px;
  padding: calc(var(--base) * 2);
}
```

---

**基本写法：calc 运算优先级**
`calc((<值1> + <值2>) * <值3>);`
```css
/* 括号控制运算优先级 */
.box {
  width: calc((100% - 40px) / 3);
}
```

---

## min() 取最小值

**基本写法：min 取最小**
`min(<值1>, <值2>[, ...]);`
```css
/* 取多个值中最小者 */
.box {
  width: min(50%, 300px);
}
```

---

**基本写法：min 混合单位**
`min(<单位1>, <单位2>);`
```css
/* 混合单位取最小 */
.text {
  font-size: min(5vw, 1.5rem);
}
```

---

**基本写法：min 多值**
`min(<值1>, <值2>, <值3>);`
```css
/* 多个值取最小 */
.box {
  width: min(100%, 800px, 90vw);
}
```

---

## max() 取最大值

**基本写法：max 取最大**
`max(<值1>, <值2>[, ...]);`
```css
/* 取多个值中最大者 */
.box {
  width: max(50%, 300px);
}
```

---

**基本写法：max 混合单位**
`max(<单位1>, <单位2>);`
```css
/* 字体不小于 16px */
.text {
  font-size: max(1rem, 16px);
}
```

---

**基本写法：max 多值**
`max(<值1>, <值2>, <值3>);`
```css
/* 多个值取最大 */
.box {
  min-height: max(100px, 10vh, 5rem);
}
```

---

## clamp() 钳制

**基本写法：clamp 钳制范围**
`clamp(<最小>, <理想>, <最大>);`
```css
/* 值在 1rem 到 3rem 之间理想 2vw+1rem */
h1 {
  font-size: clamp(1rem, 2vw + 1rem, 3rem);
}
```

---

**基本写法：clamp 响应式字体**
`clamp(<最小rem>, <理想vw>, <最大rem>);`
```css
/* 流式响应字体 */
p {
  font-size: clamp(1rem, 2.5vw, 1.5rem);
}
```

---

**基本写法：clamp 响应式间距**
`clamp(<最小>, <理想>, <最大>);`
```css
/* 流式响应间距 */
.section {
  padding: clamp(1rem, 4vw, 3rem);
}
```

---

**基本写法：clamp 响应式宽度**
`clamp(<最小>, <理想>, <最大>);`
```css
/* 容器最大宽度限制 */
.container {
  width: clamp(320px, 90vw, 1200px);
  margin: 0 auto;
}
```

---

**基本写法：clamp 等价 max min**
`max(<最小>, min(<理想>, <最大>));`
```css
/* clamp 等价写法 */
h1 {
  font-size: max(1rem, min(2vw + 1rem, 3rem));
}
```

---

## var() 变量引用

**基本写法：var 引用变量**
`var(--<属性名>);`
```css
/* 引用自定义属性 */
.box {
  color: var(--primary-color);
}
```

---

**基本写法：var 带默认值**
`var(--<属性名>, <默认值>);`
```css
/* 变量未定义时使用默认值 */
.box {
  color: var(--text-color, #333);
}
```

---

## 颜色函数

**基本写法：rgb rgba 颜色**
`rgba(<r>, <g>, <b>, <alpha>);`
```css
/* RGBA 颜色带透明度 */
.box {
  background: rgba(52, 152, 219, 0.5);
}
```

---

**基本写法：hsl hsla 颜色**
`hsla(<色相>, <饱和度>, <亮度>, <alpha>);`
```css
/* HSLA 颜色 */
.box {
  background: hsla(210, 70%, 50%, 0.5);
}
```

---

**基本写法：现代 rgb 空格语法**
`rgb(<r> <g> <b> / <alpha>);`
```css
/* 现代空格分隔语法 */
.box {
  background: rgb(52 152 219 / 50%);
}
```

---

**基本写法：十六进制带透明度**
`#RRGGBBAA;`
```css
/* 8 位十六进制带透明度 */
.box {
  background: #3498db80;
}
```

---

**基本写法：color-mix 混合颜色**
`color-mix(in <色彩空间>, <颜色1> <比例>, <颜色2>);`
```css
/* 混合两种颜色 */
.box {
  background: color-mix(in srgb, #3498db 50%, white);
}
```

---

**基本写法：color-mix 基于 oklch**
`color-mix(in oklch, <颜色1> <比例>, <颜色2>);`
```css
/* OKLCH 色彩空间混合更准确 */
.box {
  background: color-mix(in oklch, var(--primary) 70%, black);
}
```

---

**基本写法：light-dark 明暗切换**
`light-dark(<浅色>, <深色>);`
```css
/* 自动明暗模式颜色 */
.text {
  color: light-dark(#333, #fff);
}
```

---

**基本写法：oklch 感知亮度颜色**
`oklch(<亮度> <色度> <色相>);`
```css
/* OKLCH 色彩空间 */
.box {
  background: oklch(60% 0.2 240);
}
```

---

**基本写法：相对颜色**
`oklch(from <基础色> <亮度> <色度> <色相>);`
```css
/* 基于现有颜色派生新颜色 */
.darker {
  background: oklch(from var(--primary) calc(l - 0.1) c h);
}
```

---

## 渐变函数

**基本写法：linear-gradient 线性渐变**
`linear-gradient(<角度>, <颜色1>, <颜色2>);`
```css
/* 线性渐变背景 */
.box {
  background: linear-gradient(45deg, #3498db, #2ecc71);
}
```

---

**基本写法：radial-gradient 径向渐变**
`radial-gradient(<形状>, <颜色1>, <颜色2>);`
```css
/* 径向渐变 */
.box {
  background: radial-gradient(circle, #3498db, #2c3e50);
}
```

---

**基本写法：conic-gradient 锥形渐变**
`conic-gradient(from <角度>, <颜色1>, <颜色2>);`
```css
/* 锥形渐变 */
.box {
  background: conic-gradient(from 0deg, red, yellow, green, red);
}
```

---

**基本写法：渐变停顿点**
`linear-gradient(<角度>, <颜色> <位置>, <颜色> <位置>);`
```css
/* 控制渐变停顿位置 */
.box {
  background: linear-gradient(to right, #3498db 0%, #2ecc71 50%, #f1c40f 100%);
}
```

---

## 形状与路径函数

**基本写法：path 路径**
`path("<SVG路径>");`
```css
/* 沿 SVG 路径运动 */
.element {
  offset-path: path("M 0 0 L 100 100");
  animation: move 3s;
}
```

---

**基本写法：clip-path 裁剪**
`clip-path: <形状函数>;`
```css
/* 圆形裁剪 */
.avatar {
  clip-path: circle(50%);
}
```

---

**基本写法：clip-path 多边形**
`clip-path: polygon(<点1>, <点2>, ...);`
```css
/* 三角形裁剪 */
.triangle {
  clip-path: polygon(50% 0, 0 100%, 100% 100%);
}
```

---

**基本写法：clip-path inset**
`clip-path: inset(<上> <右> <下> <左> round <圆角>);`
```css
/* 矩形裁剪带圆角 */
.box {
  clip-path: inset(10% 10% 10% 10% round 20px);
}
```

---

## 滤镜函数

**基本写法：blur 模糊**
`filter: blur(<半径>);`
```css
/* 高斯模糊 */
.glass {
  filter: blur(5px);
}
```

---

**基本写法：brightness 亮度**
`filter: brightness(<比例>);`
```css
/* 提亮 1.5 倍 */
.image {
  filter: brightness(1.5);
}
```

---

**基本写法：contrast 对比度**
`filter: contrast(<比例>);`
```css
/* 提高对比度 */
.image {
  filter: contrast(1.2);
}
```

---

**基本写法：grayscale 灰度**
`filter: grayscale(<比例>);`
```css
/* 完全灰度 */
.image {
  filter: grayscale(1);
}
```

---

**基本写法：组合滤镜**
`filter: <滤镜1> <滤镜2>;`
```css
/* 多个滤镜组合 */
.image {
  filter: brightness(1.1) contrast(1.2) saturate(1.5);
}
```

---

## 数学函数组合

**基本写法：clamp 配合 calc**
`clamp(<最小>, calc(<表达式>), <最大>);`
```css
/* clamp 内嵌 calc */
.box {
  width: clamp(200px, calc(50vw - 100px), 800px);
}
```

---

**基本写法：min 配合 max**
`min(<值>, max(<值>, <值>));`
```css
/* min max 嵌套 */
.box {
  width: min(90vw, max(300px, 50vw));
}
```

---

**基本写法：calc 配合 min/max**
`calc(min(<值1>, <值2>) + <值>);`
```css
/* 复杂函数组合 */
.box {
  padding: calc(min(5vw, 30px) + 10px);
}
```

---

## 实用模式

**基本写法：响应式排版比例**
`clamp(<最小rem>, calc(<系数>vw + <基础rem>), <最大rem>);`
```css
/* 标准流式字体公式 */
h1 { font-size: clamp(2rem, calc(2.5vw + 1rem), 3.5rem); }
h2 { font-size: clamp(1.5rem, calc(2vw + 0.5rem), 2.5rem); }
p { font-size: clamp(1rem, calc(0.5vw + 0.9rem), 1.25rem); }
```

---

**基本写法：响应式容器**
`width: min(<值1>, <值2>); margin: 0 auto;`
```css
/* 自适应容器最大宽度 */
.container {
  width: min(90vw, 1200px);
  margin-inline: auto;
}
```

---

**基本写法：动态间距**
`gap: clamp(<最小>, <理想>, <最大>);`
```css
/* 流式响应间距 */
.grid {
  display: grid;
  gap: clamp(0.5rem, 2vw, 2rem);
}
```

---

**基本写法：基于视口的高度**
`height: calc(100vh - <偏移>);`
```css
/* 全屏减去导航高度 */
.main {
  height: calc(100vh - 60px);
}
```

---

## 其他函数

**基本写法：env 环境变量**
`env(<变量名>, <默认值>);`
```css
/* 安全区适配刘海屏 */
.app {
  padding-top: env(safe-area-inset-top, 0);
  padding-bottom: env(safe-area-inset-bottom, 0);
}
```

---

**基本写法：attr 属性值（增强版）**
`attr(<属性名> <类型>, <默认值>);`
```css
/* 从 HTML 属性读取值（2024+ 类型化 attr） */
.tooltip {
  --pos: attr(data-position);
  /* 实验性：attr(data-size px, 16px); */
}
```

---

**基本写法：counter 计数器**
`counter(<名称>);`
```css
/* 自动编号 */
h2::before {
  content: counter(chapter) ". ";
}
```

---

**基本写法：counter 嵌套**
`counters(<名称>, "<分隔符>");`
```css
/* 多级编号 */
li::before {
  content: counters(section, ".") " ";
}
```
