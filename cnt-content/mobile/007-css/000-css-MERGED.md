---
order: 10
title: css 模块文档合集
module: 'css'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：007-css/001-BackgroundEnhancement.md ============ -->

# CSS 背景增强

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## background-color 背景颜色

**基本写法：纯色背景**
`background-color: <颜色>;`
```css
/* 设置纯色背景 */
.box {
  background-color: #007bff;
}
```

---

**基本写法：透明背景**
`background-color: transparent;`
```css
/* 设置透明背景 */
.box {
  background-color: transparent;
}
```

---

**基本写法：rgba 半透明**
`background-color: rgba(<红>, <绿>, <蓝>, <透明度>);`
```css
/* 设置半透明背景 */
.overlay {
  background-color: rgba(0, 0, 0, 0.5);
}
```

---

**基本写法：hsl 颜色**
`background-color: hsl(<色相>, <饱和度>, <亮度>);`
```css
/* 使用 HSL 设置背景 */
.box {
  background-color: hsl(210, 100%, 50%);
}
```

---

## background-image 背景图片

**基本写法：url 背景图片**
`background-image: url("<路径>");`
```css
/* 设置背景图片 */
.hero {
  background-image: url("hero.jpg");
}
```

---

**基本写法：渐变背景**
`background-image: linear-gradient(<方向>, <颜色1>, <颜色2>);`
```css
/* 设置渐变背景 */
.header {
  background-image: linear-gradient(135deg, #007bff, #0056b3);
}
```

---

**单行写法：多重背景**
`background-image: <背景1>, <背景2>;`
```css
/* 单行设置多重背景 */
.box {
  background-image: url("overlay.png"), linear-gradient(135deg, #007bff, #0056b3);
}
```

---

**换行写法：多重背景**
`background-image: <背景1>, <背景2>, <背景3>;`
```css
/* 换行设置多重背景 */
.box {
  background-image:
    url("top-layer.png"),
    url("middle-layer.png"),
    linear-gradient(135deg, #007bff, #0056b3);
}
```

---

## background-repeat 重复

**基本写法：no-repeat 不重复**
`background-repeat: no-repeat;`
```css
/* 背景图片不重复 */
.hero {
  background-repeat: no-repeat;
}
```

---

**基本写法：repeat 重复**
`background-repeat: repeat;`
```css
/* 背景图片重复 */
.pattern {
  background-repeat: repeat;
}
```

---

**基本写法：repeat-x 水平重复**
`background-repeat: repeat-x;`
```css
/* 水平方向重复 */
.strip {
  background-repeat: repeat-x;
}
```

---

**基本写法：repeat-y 垂直重复**
`background-repeat: repeat-y;`
```css
/* 垂直方向重复 */
.strip {
  background-repeat: repeat-y;
}
```

---

**基本写法：round 适应重复**
`background-repeat: round;`
```css
/* 图片缩放适应重复 */
.pattern {
  background-repeat: round;
}
```

---

**基本写法：space 间隔重复**
`background-repeat: space;`
```css
/* 图片不裁剪间隔重复 */
.pattern {
  background-repeat: space;
}
```

---

## background-size 尺寸

**基本写法：cover 覆盖**
`background-size: cover;`
```css
/* 背景图片覆盖整个容器 */
.hero {
  background-size: cover;
}
```

---

**基本写法：contain 包含**
`background-size: contain;`
```css
/* 背景图片完整显示 */
.logo {
  background-size: contain;
}
```

---

**基本写法：固定尺寸**
`background-size: <宽度> <高度>;`
```css
/* 设置固定尺寸 */
.box {
  background-size: 100px 100px;
}
```

---

**基本写法：百分比尺寸**
`background-size: <百分比>;`
```css
/* 设置百分比尺寸 */
.box {
  background-size: 50% 50%;
}
```

---

## background-position 位置

**基本写法：关键字定位**
`background-position: <水平> <垂直>;`
```css
/* 使用关键字定位 */
.hero {
  background-position: center center;
}
```

---

**基本写法：百分比定位**
`background-position: <水平> <垂直>;`
```css
/* 使用百分比定位 */
.hero {
  background-position: 50% 50%;
}
```

---

**基本写法：像素定位**
`background-position: <x> <y>;`
```css
/* 使用像素定位 */
.sprite {
  background-position: -20px -40px;
}
```

---

**基本写法：top left 左上**
`background-position: top left;`
```css
/* 左上角定位 */
.box {
  background-position: top left;
}
```

---

**基本写法：center 居中**
`background-position: center;`
```css
/* 居中定位 */
.box {
  background-position: center;
}
```

---

## background-attachment 附件

**基本写法：scroll 滚动**
`background-attachment: scroll;`
```css
/* 背景随页面滚动 */
.box {
  background-attachment: scroll;
}
```

---

**基本写法：fixed 固定**
`background-attachment: fixed;`
```css
/* 背景固定不滚动 */
.hero {
  background-attachment: fixed;
}
```

---

**基本写法：local 局部滚动**
`background-attachment: local;`
```css
/* 背景随元素内容滚动 */
.scroll-box {
  background-attachment: local;
}
```

---

## background-origin 起点

**基本写法：padding-box 内边距起点**
`background-origin: padding-box;`
```css
/* 背景从 padding 区域开始 */
.box {
  background-origin: padding-box;
}
```

---

**基本写法：border-box 边框起点**
`background-origin: border-box;`
```css
/* 背景从 border 区域开始 */
.box {
  background-origin: border-box;
}
```

---

**基本写法：content-box 内容起点**
`background-origin: content-box;`
```css
/* 背景从 content 区域开始 */
.box {
  background-origin: content-box;
}
```

---

## background-clip 裁剪

**基本写法：border-box 边框裁剪**
`background-clip: border-box;`
```css
/* 背景裁剪到边框区域 */
.box {
  background-clip: border-box;
}
```

---

**基本写法：padding-box 内边距裁剪**
`background-clip: padding-box;`
```css
/* 背景裁剪到内边距区域 */
.box {
  background-clip: padding-box;
}
```

---

**基本写法：content-box 内容裁剪**
`background-clip: content-box;`
```css
/* 背景裁剪到内容区域 */
.box {
  background-clip: content-box;
}
```

---

**基本写法：text 文字裁剪**
`background-clip: text;`
```css
/* 背景裁剪为文字形状 */
.gradient-text {
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
}
```

---

## background 简写

**基本写法：background 简写**
`background: <颜色> url("<路径>") <重复> <位置>/<尺寸> <附件>;`
```css
/* 同时设置多个背景属性 */
.hero {
  background: #007bff url("hero.jpg") no-repeat center/cover fixed;
}
```

---

**单行写法：多重背景简写**
`background: <背景1>, <背景2>;`
```css
/* 单行设置多重背景 */
.box {
  background: url("top.png") no-repeat top left, url("bottom.png") no-repeat bottom right;
}
```

---

**换行写法：多重背景简写**
`background: <背景1>, <背景2>, <背景3>;`
```css
/* 换行设置多重背景 */
.box {
  background:
    url("top.png") no-repeat top left,
    url("middle.png") no-repeat center,
    url("bottom.png") no-repeat bottom right;
}
```

---

## 多重背景

**基本写法：多重背景图片**
`background-image: url("<图片1>"), url("<图片2>");`
```css
/* 多重背景图片叠加 */
.box {
  background-image: url("overlay.png"), url("base.jpg");
}
```

---

**基本写法：多重背景位置**
`background-position: <位置1>, <位置2>;`
```css
/* 分别设置多重背景位置 */
.box {
  background-position: top left, bottom right;
}
```

---

**基本写法：多重背景尺寸**
`background-size: <尺寸1>, <尺寸2>;`
```css
/* 分别设置多重背景尺寸 */
.box {
  background-size: 50% 50%, cover;
}
```

---

**基本写法：多重背景重复**
`background-repeat: <重复1>, <重复2>;`
```css
/* 分别设置多重背景重复方式 */
.box {
  background-repeat: no-repeat, repeat;
}
```

---

## background-blend-mode 混合

**基本写法：multiply 正片叠底**
`background-blend-mode: multiply;`
```css
/* 背景混合模式 */
.box {
  background-image: url("texture.png"), linear-gradient(red, blue);
  background-blend-mode: multiply;
}
```

---

**基本写法：screen 滤色**
`background-blend-mode: screen;`
```css
/* 滤色混合模式 */
.box {
  background-blend-mode: screen;
}
```

---

**基本写法：overlay 叠加**
`background-blend-mode: overlay;`
```css
/* 叠加混合模式 */
.box {
  background-blend-mode: overlay;
}
```

---

**基本写法：mix-blend-mode 元素混合**
`mix-blend-mode: <模式>;`
```css
/* 元素与背景混合 */
.text {
  mix-blend-mode: difference;
}
```

---

## 背景渐变

**基本写法：线性渐变**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>);`
```css
/* 线性渐变背景 */
.header {
  background: linear-gradient(135deg, #007bff, #0056b3);
}
```

---

**基本写法：多色线性渐变**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>, <颜色3>);`
```css
/* 多色线性渐变 */
.rainbow {
  background: linear-gradient(90deg, red, yellow, green);
}
```

---

**基本写法：径向渐变**
`background: radial-gradient(<形状>, <颜色1>, <颜色2>);`
```css
/* 径向渐变背景 */
.radial {
  background: radial-gradient(circle, #007bff, #0056b3);
}
```

---

**基本写法：圆锥渐变**
`background: conic-gradient(<颜色1>, <颜色2>, <颜色1>);`
```css
/* 圆锥渐变背景 */
.conic {
  background: conic-gradient(red, yellow, green, red);
}
```

---

**基本写法：重复线性渐变**
`background: repeating-linear-gradient(<方向>, <颜色1>, <颜色2> <宽度>);`
```css
/* 重复线性渐变 */
.stripes {
  background: repeating-linear-gradient(45deg, #007bff, #007bff 10px, #0056b3 10px, #0056b3 20px);
}
```

---

## 背景遮罩

**基本写法：mask 遮罩图片**
`mask-image: url("<遮罩>");`
```css
/* 使用图片作为遮罩 */
.box {
  mask-image: url("mask.png");
  -webkit-mask-image: url("mask.png");
}
```

---

**基本写法：mask 渐变遮罩**
`mask-image: linear-gradient(<方向>, <颜色1>, <颜色2>);`
```css
/* 使用渐变作为遮罩 */
.fade {
  mask-image: linear-gradient(to bottom, black, transparent);
  -webkit-mask-image: linear-gradient(to bottom, black, transparent);
}
```

---

**基本写法：mask-size 遮罩尺寸**
`mask-size: cover;`
```css
/* 遮罩尺寸覆盖 */
.box {
  mask-size: cover;
  -webkit-mask-size: cover;
}
```

---

**基本写法：mask-repeat 遮罩重复**
`mask-repeat: no-repeat;`
```css
/* 遮罩不重复 */
.box {
  mask-repeat: no-repeat;
  -webkit-mask-repeat: no-repeat;
}
```

---

## 背景滤镜

**基本写法：backdrop-filter 模糊**
`backdrop-filter: blur(<值>);`
```css
/* 背景模糊效果 */
.glass {
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}
```

---

**基本写法：backdrop-filter 亮度**
`backdrop-filter: brightness(<值>);`
```css
/* 背景亮度调整 */
.glass {
  backdrop-filter: brightness(1.2);
}
```

---

**基本写法：backdrop-filter 饱和度**
`backdrop-filter: saturate(<值>);`
```css
/* 背景饱和度调整 */
.glass {
  backdrop-filter: saturate(1.5);
}
```

---

**单行写法：多重 backdrop-filter**
`backdrop-filter: <滤镜1> <滤镜2>;`
```css
/* 单行组合多个背景滤镜 */
.glass {
  backdrop-filter: blur(10px) brightness(1.1) saturate(1.2);
}
```

---

**换行写法：多重 backdrop-filter**
`backdrop-filter: <滤镜1> <滤镜2> <滤镜3>;`
```css
/* 换行组合多个背景滤镜 */
.glass {
  backdrop-filter:
    blur(10px)
    brightness(1.1)
    saturate(1.2);
}
```

---

## CSS 背景新特性

**基本写法：background-clip 多值裁剪**
`background-clip: border-box|padding-box|content-box|text;`
```css
/* 控制背景绘制范围 */
.box {
  /* 背景延伸到边框外缘 */
  background-clip: border-box;
}
.text-gradient {
  /* 背景被裁剪为文字形状 */
  background: linear-gradient(90deg, #007bff, #00d4ff);
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
}
```

---

**基本写法：多重背景与 mix-blend-mode**
`background-image: <层1>, <层2>; mix-blend-mode: <模式>;`
```css
/* 多重背景叠加混合模式 */
.hero {
  background-image:
    linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
    url("hero.jpg");
  background-size: cover;
}
.overlay {
  mix-blend-mode: multiply;
  background: linear-gradient(red, blue);
}
```

---

**基本写法：backdrop-filter 背景滤镜**
`backdrop-filter: <滤镜函数>;`
```css
/* 毛玻璃效果:对元素背后内容应用滤镜 */
.glass {
  background-color: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
```

---

**基本写法：scroll-driven animations view-timeline**
`animation-timeline: view();`
```css
/* 滚动驱动动画:元素进出视口触发 */
@keyframes reveal {
  from { opacity: 0; transform: translateY(50px); }
  to { opacity: 1; transform: translateY(0); }
}
.card {
  animation: reveal linear;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}
```



<!-- ============ 文档分隔线：007-css/002-BorderRadius.md ============ -->

# CSS 边框圆角

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## border-radius 基础

**基本写法：统一圆角**
`border-radius: <值>;`
```css
/* 四个角相同圆角 */
.box {
  border-radius: 8px;
}
```

---

**基本写法：百分比圆角**
`border-radius: <百分比>;`
```css
/* 使用百分比圆角 */
.box {
  border-radius: 50%;
}
```

---

**基本写法：圆形**
`border-radius: 50%;`
```css
/* 创建圆形元素 */
.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
```

---

**基本写法：无圆角**
`border-radius: 0;`
```css
/* 移除圆角 */
.box {
  border-radius: 0;
}
```

---

## border-radius 多值

**基本写法：双值圆角**
`border-radius: <对角1> <对角2>;`
```css
/* 左上右下 和 右上左下 */
.box {
  border-radius: 10px 20px;
}
```

---

**基本写法：三值圆角**
`border-radius: <左上> <右上左下> <右下>;`
```css
/* 三个值设置圆角 */
.box {
  border-radius: 10px 20px 30px;
}
```

---

**单行写法：四值圆角**
`border-radius: <左上> <右上> <右下> <左下>;`
```css
/* 单行设置四个角不同圆角 */
.box {
  border-radius: 10px 20px 30px 40px;
}
```

---

**换行写法：四值圆角**
`border-top-left-radius: <值>; border-top-right-radius: <值>; border-bottom-right-radius: <值>; border-bottom-left-radius: <值>;`
```css
/* 换行设置四个角不同圆角 */
.box {
  border-top-left-radius: 10px;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 30px;
  border-bottom-left-radius: 40px;
}
```

---

## 单角圆角

**基本写法：左上角圆角**
`border-top-left-radius: <值>;`
```css
/* 仅设置左上角圆角 */
.box {
  border-top-left-radius: 10px;
}
```

---

**基本写法：右上角圆角**
`border-top-right-radius: <值>;`
```css
/* 仅设置右上角圆角 */
.box {
  border-top-right-radius: 10px;
}
```

---

**基本写法：右下角圆角**
`border-bottom-right-radius: <值>;`
```css
/* 仅设置右下角圆角 */
.box {
  border-bottom-right-radius: 10px;
}
```

---

**基本写法：左下角圆角**
`border-bottom-left-radius: <值>;`
```css
/* 仅设置左下角圆角 */
.box {
  border-bottom-left-radius: 10px;
}
```

---

## 椭圆圆角

**基本写法：椭圆角**
`border-radius: <水平> / <垂直>;`
```css
/* 设置椭圆角 */
.box {
  border-radius: 50% / 30%;
}
```

---

**基本写法：单角椭圆**
`border-top-left-radius: <水平> <垂直>;`
```css
/* 左上角椭圆 */
.box {
  border-top-left-radius: 50px 25px;
}
```

---

**基本写法：多角椭圆**
`border-radius: <水平1> <水平2> / <垂直1> <垂直2>;`
```css
/* 多角椭圆 */
.box {
  border-radius: 50px 20px / 25px 10px;
}
```

---

## border 边框

**基本写法：完整边框**
`border: <宽度> <样式> <颜色>;`
```css
/* 设置完整边框 */
.box {
  border: 1px solid #ccc;
}
```

---

**基本写法：border-width 单值**
`border-width: <值>;`
```css
/* 设置四条边框宽度 */
.box {
  border-width: 2px;
}
```

---

**基本写法：border-width 多值**
`border-width: <上> <右> <下> <左>;`
```css
/* 分别设置四条边框宽度 */
.box {
  border-width: 1px 2px 3px 4px;
}
```

---

**基本写法：border-style 实线**
`border-style: solid;`
```css
/* 设置边框样式为实线 */
.box {
  border-style: solid;
}
```

---

**基本写法：border-style 虚线**
`border-style: dashed;`
```css
/* 设置边框样式为虚线 */
.box {
  border-style: dashed;
}
```

---

**基本写法：border-style 点线**
`border-style: dotted;`
```css
/* 设置边框样式为点线 */
.box {
  border-style: dotted;
}
```

---

**基本写法：border-style 双线**
`border-style: double;`
```css
/* 设置边框样式为双线 */
.box {
  border-style: double;
}
```

---

**基本写法：border-color 边框颜色**
`border-color: <颜色>;`
```css
/* 设置边框颜色 */
.box {
  border-color: #007bff;
}
```

---

## 单边边框

**基本写法：顶边边框**
`border-top: <宽度> <样式> <颜色>;`
```css
/* 仅设置顶边边框 */
.box {
  border-top: 2px solid red;
}
```

---

**基本写法：右边边框**
`border-right: <宽度> <样式> <颜色>;`
```css
/* 仅设置右边边框 */
.box {
  border-right: 2px solid red;
}
```

---

**基本写法：底边边框**
`border-bottom: <宽度> <样式> <颜色>;`
```css
/* 仅设置底边边框 */
.box {
  border-bottom: 2px solid red;
}
```

---

**基本写法：左边边框**
`border-left: <宽度> <样式> <颜色>;`
```css
/* 仅设置左边边框 */
.box {
  border-left: 2px solid red;
}
```

---

**基本写法：无边框**
`border: none;`
```css
/* 移除边框 */
.no-border {
  border: none;
}
```

---

## border-image 边框图片

**基本写法：border-image 简写**
`border-image: url("<图片>") <切片> <重复>;`
```css
/* 使用图片作为边框 */
.box {
  border: 10px solid transparent;
  border-image: url("border.png") 30 round;
}
```

---

**基本写法：border-image-source 图片源**
`border-image-source: url("<图片>");`
```css
/* 设置边框图片源 */
.box {
  border-image-source: url("border.png");
}
```

---

**基本写法：border-image-slice 切片**
`border-image-slice: <值>;`
```css
/* 设置边框图片切片 */
.box {
  border-image-slice: 30;
}
```

---

**基本写法：border-image-width 宽度**
`border-image-width: <值>;`
```css
/* 设置边框图片宽度 */
.box {
  border-image-width: 10px;
}
```

---

**基本写法：border-image-outset 外延**
`border-image-outset: <值>;`
```css
/* 设置边框图片外延 */
.box {
  border-image-outset: 5px;
}
```

---

**基本写法：border-image-repeat 重复**
`border-image-repeat: round;`
```css
/* 边框图片平铺方式 */
.box {
  border-image-repeat: round;
}
```

---

## outline 轮廓

**基本写法：outline 完整轮廓**
`outline: <宽度> <样式> <颜色>;`
```css
/* 设置元素轮廓（不占空间） */
.input:focus {
  outline: 2px solid #007bff;
}
```

---

**基本写法：outline-offset 偏移**
`outline-offset: <值>;`
```css
/* 设置轮廓与元素的距离 */
.button:focus {
  outline: 2px solid blue;
  outline-offset: 4px;
}
```

---

**基本写法：outline-style 样式**
`outline-style: <样式>;`
```css
/* 设置轮廓样式 */
.box {
  outline-style: solid;
}
```

---

**基本写法：outline-width 宽度**
`outline-width: <值>;`
```css
/* 设置轮廓宽度 */
.box {
  outline-width: 2px;
}
```

---

**基本写法：outline-color 颜色**
`outline-color: <颜色>;`
```css
/* 设置轮廓颜色 */
.box {
  outline-color: #007bff;
}
```

---

**基本写法：移除轮廓**
`outline: none;`
```css
/* 移除默认轮廓 */
.input:focus {
  outline: none;
}
```

---

## 常见圆角效果

**基本写法：胶囊形**
`border-radius: <高度>;`
```css
/* 创建胶囊形按钮 */
.pill {
  height: 40px;
  border-radius: 20px;
}
```

---

**基本写法：顶部圆角**
`border-radius: <值> <值> 0 0;`
```css
/* 仅顶部圆角 */
.card-top {
  border-radius: 10px 10px 0 0;
}
```

---

**基本写法：底部圆角**
`border-radius: 0 0 <值> <值>;`
```css
/* 仅底部圆角 */
.card-bottom {
  border-radius: 0 0 10px 10px;
}
```

---

**基本写法：左侧圆角**
`border-radius: <值> 0 0 <值>;`
```css
/* 仅左侧圆角 */
.card-left {
  border-radius: 10px 0 0 10px;
}
```

---

**基本写法：右侧圆角**
`border-radius: 0 <值> <值> 0;`
```css
/* 仅右侧圆角 */
.card-right {
  border-radius: 0 10px 10px 0;
}
```

---

**基本写法：不对称圆角**
`border-radius: <值1> <值2> <值3> <值4>;`
```css
/* 创建不对称圆角 */
.blob {
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
}
```

---

## 响应式圆角

**基本写法：clamp 响应式圆角**
`border-radius: clamp(<最小>, <理想>, <最大>);`
```css
/* 响应式圆角 */
.box {
  border-radius: clamp(4px, 2vw, 16px);
}
```

---

**基本写法：媒体查询调整圆角**
`@media (max-width: <值>) { border-radius: <值>; }`
```css
/* 小屏幕调整圆角 */
.box {
  border-radius: 16px;
}
@media (max-width: 768px) {
  .box {
    border-radius: 8px;
  }
}
```

---

**基本写法：嵌套媒体查询圆角**
`.box { border-radius: <值>; @media (max-width: <值>) { border-radius: <值>; } }`
```css
/* CSS 原生嵌套媒体查询圆角 */
.box {
  border-radius: 16px;
  @media (max-width: 768px) {
    border-radius: 8px;
  }
}
```



<!-- ============ 文档分隔线：007-css/003-CascadeLayer.md ============ -->

# CSS 层叠层

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## @layer 定义

**基本写法：定义命名层**
`@layer <层名>;`
```css
/* 声明层叠层 */
@layer base;
@layer components;
@layer utilities;
```

---

**基本写法：定义并写入样式**
`@layer <层名> { <样式> }`
```css
/* 定义层并写入样式 */
@layer base {
  body {
    font-size: 16px;
  }
}
```

---

**单行写法：多层级声明**
`@layer <层1>, <层2>, <层3>;`
```css
/* 单行声明多个层叠层顺序 */
@layer base, components, utilities;
```

---

**换行写法：多层级声明**
`@layer <层1>, <层2>, <层3>;`
```css
/* 换行声明多个层叠层顺序 */
@layer
  base,
  components,
  utilities;
```

---

**基本写法：匿名层**
`@layer { <样式> }`
```css
/* 创建匿名层叠层 */
@layer {
  .box {
    padding: 10px;
  }
}
```

---

## 层优先级

**基本写法：层顺序决定优先级**
`@layer <低优先级>, <中优先级>, <高优先级>;`
```css
/* 后声明的层优先级更高 */
@layer base, components, utilities;
@layer base {
  p { color: black; }
}
@layer utilities {
  p { color: red; }
}
```

---

**基本写法：未分层样式优先**
`<选择器> { <样式> }`
```css
/* 未分层样式优先级高于所有层 */
p {
  color: blue;
}
@layer base {
  p { color: black; }
}
```

---

**基本写法：层内 !important 反转**
`<选择器> { <属性>: <值> !important; }`
```css
/* !important 在层间反转优先级 */
@layer base {
  p { color: black !important; }
}
@layer utilities {
  p { color: red; }
}
```

---

## 嵌套层

**基本写法：嵌套层定义**
`@layer <父层>.<子层> { <样式> }`
```css
/* 定义嵌套层叠层 */
@layer components.buttons {
  .btn {
    padding: 8px 16px;
  }
}
```

---

**基本写法：嵌套层顺序**
`@layer <父层>.<子层1>, <父层>.<子层2>;`
```css
/* 声明嵌套层顺序 */
@layer components.buttons, components.forms;
```

---

**基本写法：嵌套层内定义**
`@layer <父层> { @layer <子层> { <样式> } }`
```css
/* 在父层内定义子层 */
@layer components {
  @layer buttons {
    .btn { padding: 8px; }
  }
  @layer forms {
    .input { padding: 4px; }
  }
}
```

---

## @import 分层导入

**基本写法：@import 导入到层**
`@import url("<文件>") layer(<层名>);`
```css
/* 导入样式到指定层 */
@import url("reset.css") layer(base);
```

---

**基本写法：@import 带媒体查询导入层**
`@import url("<文件>") layer(<层名>) <媒体查询>;`
```css
/* 导入样式到层并应用媒体查询 */
@import url("mobile.css") layer(components) (max-width: 768px);
```

---

## 层与特异性

**基本写法：层优先于特异性**
`@layer <层名> { <高特异性选择器> { <样式> } }`
```css
/* 层优先级高于选择器特异性 */
@layer base {
  #header {
    color: black;
  }
}
.text-red {
  color: red;
}
```

---

**基本写法：同层内特异性生效**
`@layer <层名> { <低特异性>, <高特异性> { <样式> } }`
```css
/* 同一层内特异性正常生效 */
@layer base {
  p { color: black; }
  .highlight { color: red; }
}
```

---

## 实际应用模式

**基本写法：重置层**
`@layer base { <重置样式> }`
```css
/* 将重置样式放入 base 层 */
@layer base {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
}
```

---

**基本写法：组件层**
`@layer components { <组件样式> }`
```css
/* 将组件样式放入 components 层 */
@layer components {
  .card {
    padding: 16px;
    border: 1px solid #ccc;
  }
}
```

---

**基本写法：工具层**
`@layer utilities { <工具样式> }`
```css
/* 将工具类样式放入 utilities 层 */
@layer utilities {
  .text-center { text-align: center; }
  .mt-4 { margin-top: 1rem; }
}
```

---

**基本写法：主题层**
`@layer theme { <主题样式> }`
```css
/* 将主题样式放入 theme 层 */
@layer theme {
  :root {
    --primary: #007bff;
  }
}
```

---

## 层叠层与级联

**基本写法：层顺序覆盖**
`@layer <低层>, <高层>;`
```css
/* 后声明的层覆盖先声明的层 */
@layer base, theme, components;
@layer base {
  body { background: white; }
}
@layer theme {
  body { background: #f5f5f5; }
}
```

---

**基本写法：层内顺序**
`@layer <层名> { <样式1> <样式2> }`
```css
/* 同层内后定义的覆盖先定义的 */
@layer components {
  .btn { color: black; }
  .btn { color: red; }
}
```

---

## 层与媒体查询

**基本写法：媒体查询中重新排序**
`@media <条件> { @layer <新顺序>; }`
```css
/* 响应式调整层顺序 */
@media (max-width: 768px) {
  @layer base, utilities, components;
}
```

---

**基本写法：层内媒体查询**
`@layer <层名> { @media <条件> { <样式> } }`
```css
/* 在层内使用媒体查询 */
@layer components {
  .container {
    width: 100%;
    @media (min-width: 768px) {
      max-width: 720px;
    }
  }
}
```

---

## 层调试

**基本写法：层顺序检查**
`@layer <层1>, <层2>, <层3>;`
```css
/* 通过声明顺序检查层优先级 */
@layer base, components, utilities;
```

---

**基本写法：层覆盖测试**
`@layer <测试层> { <选择器> { <样式> } }`
```css
/* 临时添加层测试覆盖 */
@layer test {
  .box {
    border: 2px solid red;
  }
}
```

---

## @layer 与 @scope 进阶

**基本写法：@layer 命名层叠层**
`@layer <层1>, <层2>, <层3>;`
```css
/* 通过命名层叠层管理样式优先级 */
@layer reset, base, components, utilities;
@layer reset {
  * { margin: 0; padding: 0; box-sizing: border-box; }
}
@layer utilities {
  .text-center { text-align: center; }
}
```

---

**基本写法：@layer 匿名层**
`@layer { <样式声明> }`
```css
/* 匿名层按声明顺序参与层叠 */
@layer {
  /* 该样式进入匿名层,优先级低于未分层样式 */
  p { line-height: 1.5; }
}
```

---

**基本写法：@scope 与 @layer 对比**
`@layer <层名> { <样式> }  vs  @scope (<选择器>) { <样式> }`
```css
/* @layer 控制优先级,@scope 控制作用范围 */
@layer components {
  /* 通过层序控制优先级 */
  .title { color: black; }
}
@scope (.article) {
  /* 通过作用域限定应用范围 */
  .title { font-size: 1.5rem; }
}
```

---

**基本写法：@scope 与 cascade origins**
`@scope (<根>) to (<下限>) { <样式声明> }`
```css
/* @scope 不影响优先级,仅限定范围 */
@scope (.content) to (.ad) {
  /* 仅作用于 .content 内、.ad 之外 */
  a { color: #007bff; }
}
/* @scope 内样式特异性仍按选择器计算 */
```



<!-- ============ 文档分隔线：007-css/004-PositionDetailed.md ============ -->

# CSS 定位详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## position 定位类型

**基本写法：static 静态定位**
`position: static;`
```css
/* 默认定位，遵循文档流 */
.box {
  position: static;
}
```

---

**基本写法：relative 相对定位**
`position: relative;`
```css
/* 相对自身原位置偏移 */
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
/* 相对最近的非 static 祖先定位 */
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
/* 相对视口定位，不随滚动 */
.header {
  position: fixed;
  top: 0;
  width: 100%;
}
```

---

**基本写法：sticky 粘性定位**
`position: sticky;`
```css
/* 滚动到阈值时变为固定 */
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
/* 设置元素顶部偏移 */
.box {
  position: relative;
  top: 20px;
}
```

---

**基本写法：right 右侧偏移**
`right: <值>;`
```css
/* 设置元素右侧偏移 */
.box {
  position: absolute;
  right: 0;
}
```

---

**基本写法：bottom 底部偏移**
`bottom: <值>;`
```css
/* 设置元素底部偏移 */
.footer {
  position: fixed;
  bottom: 0;
}
```

---

**基本写法：left 左侧偏移**
`left: <值>;`
```css
/* 设置元素左侧偏移 */
.box {
  position: absolute;
  left: 50%;
}
```

---

**单行写法：多方向偏移**
`top: <值>; right: <值>; bottom: <值>; left: <值>;`
```css
/* 单行设置多方向偏移 */
.overlay {
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
}
```

---

**换行写法：多方向偏移**
`top: <值>; right: <值>; bottom: <值>; left: <值>;`
```css
/* 换行设置多方向偏移 */
.overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
```

---

## z-index 层叠顺序

**基本写法：z-index 层级**
`z-index: <数值>;`
```css
/* 设置元素层叠顺序 */
.modal {
  position: fixed;
  z-index: 1000;
}
```

---

**基本写法：z-index 负值**
`z-index: <-值>;`
```css
/* 将元素置于背景之后 */
.background {
  position: absolute;
  z-index: -1;
}
```

---

**基本写法：z-index auto**
`z-index: auto;`
```css
/* 默认层叠顺序 */
.box {
  position: relative;
  z-index: auto;
}
```

---

## 居中定位

**基本写法：绝对定位水平居中**
`left: 50%; transform: translateX(-50%);`
```css
/* 绝对定位元素水平居中 */
.center-x {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}
```

---

**基本写法：绝对定位垂直居中**
`top: 50%; transform: translateY(-50%);`
```css
/* 绝对定位元素垂直居中 */
.center-y {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

---

**基本写法：绝对定位双居中**
`top: 50%; left: 50%; transform: translate(-50%, -50%);`
```css
/* 绝对定位元素水平垂直居中 */
.center-xy {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

---

**基本写法：inset 居中**
`inset: 0; margin: auto;`
```css
/* 使用 inset 实现居中 */
.center-inset {
  position: absolute;
  inset: 0;
  margin: auto;
  width: 200px;
  height: 200px;
}
```

---

## inset 简写

**基本写法：inset 统一值**
`inset: <值>;`
```css
/* 四个方向偏移相同 */
.box {
  position: absolute;
  inset: 10px;
}
```

---

**基本写法：inset 双值**
`inset: <上下> <左右>;`
```css
/* 上下 10px，左右 20px */
.box {
  position: absolute;
  inset: 10px 20px;
}
```

---

**单行写法：inset 四值**
`inset: <上> <右> <下> <左>;`
```css
/* 单行设置四个方向偏移 */
.box {
  position: absolute;
  inset: 10px 20px 30px 40px;
}
```

---

**换行写法：inset 四值**
`inset: <上> <右> <下> <左>;`
```css
/* 换行设置四个方向偏移 */
.box {
  position: absolute;
  inset:
    10px
    20px
    30px
    40px;
}
```

---

## float 浮动

**基本写法：float 左浮动**
`float: left;`
```css
/* 元素向左浮动 */
.image {
  float: left;
  margin-right: 10px;
}
```

---

**基本写法：float 右浮动**
`float: right;`
```css
/* 元素向右浮动 */
.sidebar {
  float: right;
  width: 300px;
}
```

---

**基本写法：float none 不浮动**
`float: none;`
```css
/* 取消浮动 */
.no-float {
  float: none;
}
```

---

**基本写法：clear 清除浮动**
`clear: both;`
```css
/* 清除两侧浮动 */
.clearfix {
  clear: both;
}
```

---

**基本写法：clear 左侧清除**
`clear: left;`
```css
/* 清除左侧浮动 */
.box {
  clear: left;
}
```

---

**基本写法：clearfix 伪元素**
`.clearfix::after { content: ""; display: table; clear: both; }`
```css
/* 使用伪元素清除浮动 */
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

---

## clip 裁剪

**基本写法：clip-path 矩形裁剪**
`clip-path: inset(<值>);`
```css
/* 矩形裁剪 */
.box {
  clip-path: inset(10px);
}
```

---

**基本写法：clip-path 圆形裁剪**
`clip-path: circle(<半径> at <位置>);`
```css
/* 圆形裁剪 */
.avatar {
  clip-path: circle(50% at 50% 50%);
}
```

---

**基本写法：clip-path 椭圆裁剪**
`clip-path: ellipse(<水平> <垂直> at <位置>);`
```css
/* 椭圆裁剪 */
.box {
  clip-path: ellipse(50% 30% at 50% 50%);
}
```

---

**基本写法：clip-path 多边形裁剪**
`clip-path: polygon(<点1>, <点2>, ...);`
```css
/* 三角形裁剪 */
.triangle {
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}
```

---

## transform 变换

**基本写法：translate 平移**
`transform: translate(<x>, <y>);`
```css
/* 平移元素 */
.box {
  transform: translate(50px, 100px);
}
```

---

**基本写法：translateX 水平平移**
`transform: translateX(<值>);`
```css
/* 水平平移 */
.box {
  transform: translateX(100px);
}
```

---

**基本写法：translateY 垂直平移**
`transform: translateY(<值>);`
```css
/* 垂直平移 */
.box {
  transform: translateY(50px);
}
```

---

**基本写法：scale 缩放**
`transform: scale(<比例>);`
```css
/* 等比缩放 */
.box {
  transform: scale(1.5);
}
```

---

**基本写法：scale 双向缩放**
`transform: scale(<x>, <y>);`
```css
/* 分别设置 x 和 y 缩放 */
.box {
  transform: scale(2, 0.5);
}
```

---

**基本写法：rotate 旋转**
`transform: rotate(<角度>);`
```css
/* 旋转元素 */
.box {
  transform: rotate(45deg);
}
```

---

**基本写法：skew 倾斜**
`transform: skew(<x>, <y>);`
```css
/* 倾斜元素 */
.box {
  transform: skew(10deg, 5deg);
}
```

---

**单行写法：多重变换**
`transform: <变换1> <变换2> <变换3>;`
```css
/* 单行组合多个变换 */
.box {
  transform: translate(50px, 50px) rotate(45deg) scale(1.5);
}
```

---

**换行写法：多重变换**
`transform: <变换1> <变换2> <变换3>;`
```css
/* 换行组合多个变换 */
.box {
  transform:
    translate(50px, 50px)
    rotate(45deg)
    scale(1.5);
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

**基本写法：transform 3D 平移**
`transform: translate3d(<x>, <y>, <z>);`
```css
/* 3D 平移 */
.box {
  transform: translate3d(10px, 20px, 30px);
}
```

---

**基本写法：perspective 透视**
`perspective: <值>;`
```css
/* 设置 3D 透视距离 */
.container {
  perspective: 1000px;
}
```

---

**基本写法：transform-style 3D 空间**
`transform-style: preserve-3d;`
```css
/* 子元素保持 3D 位置 */
.container {
  transform-style: preserve-3d;
}
```

---

## 定位上下文

**基本写法：建立定位上下文**
`position: relative;`
```css
/* 父元素建立定位上下文 */
.parent {
  position: relative;
}
.child {
  position: absolute;
}
```

---

**基本写法：transform 建立上下文**
`transform: translateZ(0);`
```css
/* 使用 transform 创建定位上下文 */
.parent {
  transform: translateZ(0);
}
```

---

**基本写法：will-change 优化**
`will-change: <属性>;`
```css
/* 提示浏览器优化变换 */
.animated {
  will-change: transform;
}
```

---

## 层叠上下文

**基本写法：opacity 创建层叠上下文**
`opacity: <值>;`
```css
/* opacity 小于 1 创建层叠上下文 */
.overlay {
  opacity: 0.9;
}
```

---

**基本写法：filter 创建层叠上下文**
`filter: <滤镜>;`
```css
/* filter 创建层叠上下文 */
.blur {
  filter: blur(5px);
}
```

---

**基本写法：isolation 隔离**
`isolation: isolate;`
```css
/* 创建独立的层叠上下文 */
.modal {
  isolation: isolate;
}
```



<!-- ============ 文档分隔线：007-css/005-CSSAnimationTransition.md ============ -->

# CSS 动画与过渡

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## transition 过渡

**基本写法：transition-property 单属性**
`transition-property: <属性>;`
```css
/* 指定过渡属性 */
.box {
  transition-property: opacity;
}
```

---

**基本写法：transition-duration 时长**
`transition-duration: <时间>;`
```css
/* 设置过渡时长 */
.box {
  transition-duration: 0.3s;
}
```

---

**基本写法：transition-timing-function 缓动**
`transition-timing-function: <缓动函数>;`
```css
/* 设置缓动函数 */
.box {
  transition-timing-function: ease-in-out;
}
```

---

**基本写法：transition-delay 延迟**
`transition-delay: <时间>;`
```css
/* 设置过渡延迟 */
.box {
  transition-delay: 0.1s;
}
```

---

**基本写法：transition 简写**
`transition: <属性> <时长> <缓动> <延迟>;`
```css
/* 同时设置过渡属性 */
.box {
  transition: opacity 0.3s ease-in-out 0.1s;
}
```

---

**单行写法：多属性过渡**
`transition: <属性1> <时长1>, <属性2> <时长2>;`
```css
/* 单行设置多个属性过渡 */
.box {
  transition: opacity 0.3s, transform 0.5s;
}
```

---

**换行写法：多属性过渡**
`transition: <属性1> <时长1>, <属性2> <时长2>, <属性3> <时长3>;`
```css
/* 换行设置多个属性过渡 */
.box {
  transition:
    opacity 0.3s,
    transform 0.5s,
    background-color 0.2s;
}
```

---

**基本写法：transition all**
`transition: all <时长>;`
```css
/* 所有可过渡属性都应用过渡 */
.box {
  transition: all 0.3s;
}
```

---

## @keyframes 关键帧

**基本写法：from-to 关键帧**
`@keyframes <名称> { from { <样式> } to { <样式> } }`
```css
/* 定义从起点到终点的动画 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

---

**基本写法：百分比关键帧**
`@keyframes <名称> { 0% { <样式> } 50% { <样式> } 100% { <样式> } }`
```css
/* 定义多关键帧动画 */
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}
```

---

**单行写法：多属性关键帧**
`@keyframes <名称> { 0% { <属性1>: <值>; <属性2>: <值>; } }`
```css
/* 单行定义多属性关键帧 */
@keyframes slide {
  0% { transform: translateX(0); opacity: 1; }
  100% { transform: translateX(100px); opacity: 0; }
}
```

---

**换行写法：多属性关键帧**
`@keyframes <名称> { 0% { <属性1>: <值>; <属性2>: <值>; } }`
```css
/* 换行定义多属性关键帧 */
@keyframes slide {
  0% {
    transform: translateX(0);
    opacity: 1;
  }
  100% {
    transform: translateX(100px);
    opacity: 0;
  }
}
```

---

## animation 动画

**基本写法：animation-name 名称**
`animation-name: <动画名>;`
```css
/* 指定动画名称 */
.box {
  animation-name: fadeIn;
}
```

---

**基本写法：animation-duration 时长**
`animation-duration: <时间>;`
```css
/* 设置动画时长 */
.box {
  animation-duration: 2s;
}
```

---

**基本写法：animation-timing-function 缓动**
`animation-timing-function: <缓动函数>;`
```css
/* 设置动画缓动函数 */
.box {
  animation-timing-function: ease-in-out;
}
```

---

**基本写法：animation-delay 延迟**
`animation-delay: <时间>;`
```css
/* 设置动画延迟 */
.box {
  animation-delay: 0.5s;
}
```

---

**基本写法：animation-iteration-count 次数**
`animation-iteration-count: <次数>;`
```css
/* 设置动画播放次数 */
.box {
  animation-iteration-count: 3;
}
```

---

**基本写法：animation-iteration-count 无限**
`animation-iteration-count: infinite;`
```css
/* 无限循环播放 */
.box {
  animation-iteration-count: infinite;
}
```

---

**基本写法：animation-direction 方向**
`animation-direction: alternate;`
```css
/* 交替反向播放 */
.box {
  animation-direction: alternate;
}
```

---

**基本写法：animation-direction 反向**
`animation-direction: reverse;`
```css
/* 反向播放 */
.box {
  animation-direction: reverse;
}
```

---

**基本写法：animation-fill-mode 填充**
`animation-fill-mode: forwards;`
```css
/* 保持结束状态 */
.box {
  animation-fill-mode: forwards;
}
```

---

**基本写法：animation-fill-mode 双向**
`animation-fill-mode: both;`
```css
/* 同时应用开始和结束状态 */
.box {
  animation-fill-mode: both;
}
```

---

**基本写法：animation-play-state 播放**
`animation-play-state: running;`
```css
/* 动画运行中 */
.box {
  animation-play-state: running;
}
```

---

**基本写法：animation-play-state 暂停**
`animation-play-state: paused;`
```css
/* 暂停动画 */
.box:hover {
  animation-play-state: paused;
}
```

---

**基本写法：animation 简写**
`animation: <名称> <时长> <缓动> <延迟> <次数> <方向> <填充> <状态>;`
```css
/* 同时设置所有动画属性 */
.box {
  animation: fadeIn 2s ease-in-out 0.5s infinite alternate forwards;
}
```

---

**单行写法：多动画**
`animation: <动画1>, <动画2>;`
```css
/* 单行设置多个动画 */
.box {
  animation: fadeIn 2s, slideIn 1s;
}
```

---

**换行写法：多动画**
`animation: <动画1>, <动画2>, <动画3>;`
```css
/* 换行设置多个动画 */
.box {
  animation:
    fadeIn 2s,
    slideIn 1s,
    pulse 0.5s infinite;
}
```

---

## 缓动函数

**基本写法：ease 默认**
`transition-timing-function: ease;`
```css
/* 默认缓动 */
.box {
  transition-timing-function: ease;
}
```

---

**基本写法：linear 线性**
`transition-timing-function: linear;`
```css
/* 线性匀速 */
.box {
  transition-timing-function: linear;
}
```

---

**基本写法：ease-in 加速**
`transition-timing-function: ease-in;`
```css
/* 开始慢，结束快 */
.box {
  transition-timing-function: ease-in;
}
```

---

**基本写法：ease-out 减速**
`transition-timing-function: ease-out;`
```css
/* 开始快，结束慢 */
.box {
  transition-timing-function: ease-out;
}
```

---

**基本写法：cubic-bezier 自定义**
`transition-timing-function: cubic-bezier(<x1>, <y1>, <x2>, <y2>);`
```css
/* 自定义贝塞尔曲线 */
.box {
  transition-timing-function: cubic-bezier(0.25, 0.1, 0.25, 1);
}
```

---

**基本写法：steps 步进**
`transition-timing-function: steps(<步数>);`
```css
/* 分步过渡 */
.box {
  transition-timing-function: steps(4);
}
```

---

**基本写法：steps 跳跃**
`transition-timing-function: steps(<步数>, jump-none);`
```css
/* 步进不跳跃 */
.box {
  transition-timing-function: steps(4, jump-none);
}
```

---

## transform 变换动画

**基本写法：translate 平移动画**
`transform: translate(<x>, <y>);`
```css
/* 平移动画 */
.box {
  transition: transform 0.3s;
}
.box:hover {
  transform: translate(10px, 10px);
}
```

---

**基本写法：scale 缩放动画**
`transform: scale(<比例>);`
```css
/* 缩放动画 */
.box {
  transition: transform 0.3s;
}
.box:hover {
  transform: scale(1.1);
}
```

---

**基本写法：rotate 旋转动画**
`transform: rotate(<角度>);`
```css
/* 旋转动画 */
.box {
  transition: transform 0.5s;
}
.box:hover {
  transform: rotate(180deg);
}
```

---

**基本写法：3D 旋转动画**
`transform: rotateY(<角度>);`
```css
/* Y 轴 3D 旋转 */
.card {
  transition: transform 0.6s;
  transform-style: preserve-3d;
}
.card:hover {
  transform: rotateY(180deg);
}
```

---

## 常见动画效果

**基本写法：淡入动画**
`@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }`
```css
/* 淡入效果 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
.fade-in {
  animation: fadeIn 0.5s ease-out;
}
```

---

**基本写法：淡出动画**
`@keyframes fadeOut { from { opacity: 1; } to { opacity: 0; } }`
```css
/* 淡出效果 */
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
.fade-out {
  animation: fadeOut 0.5s ease-in;
}
```

---

**基本写法：滑入动画**
`@keyframes slideIn { from { transform: translateX(-100%); } to { transform: translateX(0); } }`
```css
/* 从左侧滑入 */
@keyframes slideIn {
  from { transform: translateX(-100%); }
  to { transform: translateX(0); }
}
.slide-in {
  animation: slideIn 0.5s ease-out;
}
```

---

**基本写法：弹跳动画**
`@keyframes bounce { 0%, 20%, 50%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-30px); } 60% { transform: translateY(-15px); } }`
```css
/* 弹跳效果 */
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(-30px); }
  60% { transform: translateY(-15px); }
}
.bounce {
  animation: bounce 1s;
}
```

---

**基本写法：旋转加载**
`@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }`
```css
/* 旋转加载动画 */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.spinner {
  animation: spin 1s linear infinite;
}
```

---

**基本写法：脉冲动画**
`@keyframes pulse { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.05); opacity: 0.8; } }`
```css
/* 脉冲效果 */
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.05); opacity: 0.8; }
}
.pulse {
  animation: pulse 2s ease-in-out infinite;
}
```

---

## 滚动驱动动画

**基本写法：animation-timeline 滚动**
`animation-timeline: scroll();`
```css
/* 滚动驱动动画 */
.box {
  animation: fadeIn linear;
  animation-timeline: scroll();
}
```

---

**基本写法：animation-timeline 视口**
`animation-timeline: view();`
```css
/* 元素进入视口时触发 */
.box {
  animation: fadeIn linear;
  animation-timeline: view();
}
```

---

**基本写法：view 轴向**
`animation-timeline: view(<轴>);`
```css
/* 指定视口轴向 */
.box {
  animation: fadeIn linear;
  animation-timeline: view(block);
}
```

---

## 性能优化

**基本写法：will-change 提示**
`will-change: <属性>;`
```css
/* 提示浏览器优化 */
.animated {
  will-change: transform, opacity;
}
```

---

**基本写法：transform 替代 position**
`transform: translate3d(<x>, <y>, 0);`
```css
/* 使用 transform 触发 GPU 加速 */
.box {
  transform: translate3d(0, 0, 0);
}
```

---

**基本写法：backface-visibility 隐藏背面**
`backface-visibility: hidden;`
```css
/* 翻转卡片隐藏背面 */
.card {
  backface-visibility: hidden;
}
```

---

**基本写法：contain 包含**
`contain: layout;`
```css
/* 限制重绘范围 */
.widget {
  contain: layout;
}
```

---

**基本写法：content-visibility 内容可见性**
`content-visibility: auto;`
```css
/* 自动跳过屏幕外内容渲染 */
.long-list {
  content-visibility: auto;
}
```

---

## 现代动画新特性

**基本写法：@starting-style 进入动画**
`@starting-style { <选择器> { <样式> } }`
```css
/* 元素首次显示时的起始样式,实现进入动画 */
.dialog {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.3s, transform 0.3s;
}
@starting-style {
  .dialog {
    opacity: 0;
    transform: translateY(20px);
  }
}
```

---

**基本写法：transition-behavior: allow-discrete**
`transition-behavior: allow-discrete;`
```css
/* 允许离散属性(如 display)参与过渡 */
.modal {
  transition: display 0.3s, opacity 0.3s;
  transition-behavior: allow-discrete;
}
.modal.hidden {
  display: none;
  opacity: 0;
}
```

---

**基本写法：scroll-driven animations animation-timeline**
`animation-timeline: scroll(<参数>);`
```css
/* 滚动驱动动画:页面滚动时持续触发 */
@keyframes progress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
.progress-bar {
  animation: progress linear;
  animation-timeline: scroll(root);
  transform-origin: left;
}
```

---

**基本写法：view-timeline 视图时间线**
`view-timeline: <名称> <轴>;`
```css
/* 元素进入视口时触发的视图时间线 */
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
.section {
  view-timeline: --section-timeline block;
  animation: fade-in linear;
  animation-timeline: --section-timeline;
}
```

---

**基本写法：interpolate-size: allow-keywords 高度 auto 过渡**
`interpolate-size: allow-keywords;`
```css
/* 允许对 height: auto 等关键字进行过渡 */
.accordion {
  interpolate-size: allow-keywords;
  height: auto;
  transition: height 0.3s ease;
}
.accordion.collapsed {
  height: 0;
}
```



<!-- ============ 文档分隔线：007-css/006-CSS3BoxModelDetailed.md ============ -->

# CSS 盒模型详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## box-sizing

**基本写法：content-box 标准盒模型**
`box-sizing: content-box;`
```css
/* width/height 只包含内容区 */
.box {
  box-sizing: content-box;
  width: 200px;
  padding: 20px;
}
```

---

**基本写法：border-box 怪异盒模型**
`box-sizing: border-box;`
```css
/* width/height 包含 padding 和 border */
.box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
}
```

---

**基本写法：全局 border-box**
`*, *::before, *::after { box-sizing: border-box; }`
```css
/* 全局应用 border-box */
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

## width 与 height

**基本写法：固定宽度**
`width: <长度>;`
```css
/* 设置固定宽度 */
.container {
  width: 1200px;
}
```

---

**基本写法：百分比宽度**
`width: <百分比>;`
```css
/* 设置相对于父元素的百分比宽度 */
.half {
  width: 50%;
}
```

---

**基本写法：视口宽度**
`width: <vw值>;`
```css
/* 设置相对于视口宽度的宽度 */
.full {
  width: 100vw;
}
```

---

**基本写法：最大宽度**
`max-width: <长度>;`
```css
/* 限制元素最大宽度 */
.container {
  max-width: 1200px;
  margin: 0 auto;
}
```

---

**基本写法：最小宽度**
`min-width: <长度>;`
```css
/* 限制元素最小宽度 */
.sidebar {
  min-width: 200px;
}
```

---

**基本写法：固定高度**
`height: <长度>;`
```css
/* 设置固定高度 */
.header {
  height: 60px;
}
```

---

**基本写法：视口高度**
`height: <vh值>;`
```css
/* 设置相对于视口高度的高度 */
.hero {
  height: 100vh;
}
```

---

**基本写法：max-height 最大高度**
`max-height: <长度>;`
```css
/* 限制元素最大高度 */
.scroll-area {
  max-height: 400px;
  overflow: auto;
}
```

---

**基本写法：min-height 最小高度**
`min-height: <长度>;`
```css
/* 限制元素最小高度 */
.card {
  min-height: 200px;
}
```

---

## margin 外边距

**基本写法：margin 单值**
`margin: <值>;`
```css
/* 四个方向外边距相同 */
.box {
  margin: 20px;
}
```

---

**基本写法：margin 双值**
`margin: <上下> <左右>;`
```css
/* 上下 20px，左右 10px */
.box {
  margin: 20px 10px;
}
```

---

**基本写法：margin 三值**
`margin: <上> <左右> <下>;`
```css
/* 上 10px，左右 20px，下 30px */
.box {
  margin: 10px 20px 30px;
}
```

---

**单行写法：margin 四值**
`margin: <上> <右> <下> <左>;`
```css
/* 单行设置四个方向外边距 */
.box {
  margin: 10px 20px 30px 40px;
}
```

---

**换行写法：margin 四值**
`margin-top: <值>; margin-right: <值>; margin-bottom: <值>; margin-left: <值>;`
```css
/* 换行设置四个方向外边距 */
.box {
  margin-top: 10px;
  margin-right: 20px;
  margin-bottom: 30px;
  margin-left: 40px;
}
```

---

**基本写法：margin auto 水平居中**
`margin: 0 auto;`
```css
/* 块级元素水平居中 */
.container {
  width: 800px;
  margin: 0 auto;
}
```

---

**基本写法：margin 负值**
`margin-<方向>: <-值>;`
```css
/* 使用负值偏移元素 */
.pull-up {
  margin-top: -20px;
}
```

---

## padding 内边距

**基本写法：padding 单值**
`padding: <值>;`
```css
/* 四个方向内边距相同 */
.box {
  padding: 20px;
}
```

---

**基本写法：padding 双值**
`padding: <上下> <左右>;`
```css
/* 上下 10px，左右 20px */
.box {
  padding: 10px 20px;
}
```

---

**基本写法：padding 三值**
`padding: <上> <左右> <下>;`
```css
/* 上 10px，左右 20px，下 30px */
.box {
  padding: 10px 20px 30px;
}
```

---

**单行写法：padding 四值**
`padding: <上> <右> <下> <左>;`
```css
/* 单行设置四个方向内边距 */
.box {
  padding: 10px 20px 30px 40px;
}
```

---

**换行写法：padding 四值**
`padding-top: <值>; padding-right: <值>; padding-bottom: <值>; padding-left: <值>;`
```css
/* 换行设置四个方向内边距 */
.box {
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 30px;
  padding-left: 40px;
}
```

---

## border 边框

**基本写法：border 完整边框**
`border: <宽度> <样式> <颜色>;`
```css
/* 设置完整边框 */
.box {
  border: 1px solid #ccc;
}
```

---

**基本写法：border-width 单值**
`border-width: <值>;`
```css
/* 设置四条边框宽度 */
.box {
  border-width: 2px;
}
```

---

**基本写法：border-style 实线**
`border-style: solid;`
```css
/* 设置边框样式为实线 */
.box {
  border-style: solid;
}
```

---

**基本写法：border-style 虚线**
`border-style: dashed;`
```css
/* 设置边框样式为虚线 */
.box {
  border-style: dashed;
}
```

---

**基本写法：border-color 边框颜色**
`border-color: <颜色>;`
```css
/* 设置边框颜色 */
.box {
  border-color: #007bff;
}
```

---

**基本写法：单边边框**
`border-<方向>: <宽度> <样式> <颜色>;`
```css
/* 仅设置底边边框 */
.box {
  border-bottom: 2px solid red;
}
```

---

**基本写法：无边框**
`border: none;`
```css
/* 移除边框 */
.no-border {
  border: none;
}
```

---

## border-radius 圆角

**基本写法：统一圆角**
`border-radius: <值>;`
```css
/* 四个角相同圆角 */
.box {
  border-radius: 8px;
}
```

---

**基本写法：圆形**
`border-radius: 50%;`
```css
/* 创建圆形元素 */
.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
```

---

**基本写法：椭圆角**
`border-radius: <水平> / <垂直>;`
```css
/* 设置椭圆角 */
.box {
  border-radius: 50% / 30%;
}
```

---

**单行写法：四角不同圆角**
`border-radius: <左上> <右上> <右下> <左下>;`
```css
/* 单行设置四个角不同圆角 */
.box {
  border-radius: 10px 20px 30px 40px;
}
```

---

**换行写法：四角不同圆角**
`border-top-left-radius: <值>; border-top-right-radius: <值>; border-bottom-right-radius: <值>; border-bottom-left-radius: <值>;`
```css
/* 换行设置四个角不同圆角 */
.box {
  border-top-left-radius: 10px;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 30px;
  border-bottom-left-radius: 40px;
}
```

---

## outline 轮廓

**基本写法：outline 完整轮廓**
`outline: <宽度> <样式> <颜色>;`
```css
/* 设置元素轮廓（不占空间） */
.input:focus {
  outline: 2px solid #007bff;
}
```

---

**基本写法：outline-offset 偏移**
`outline-offset: <值>;`
```css
/* 设置轮廓与元素的距离 */
.button:focus {
  outline: 2px solid blue;
  outline-offset: 4px;
}
```

---

**基本写法：移除轮廓**
`outline: none;`
```css
/* 移除默认轮廓 */
.input:focus {
  outline: none;
}
```

---

## box-shadow 阴影

**基本写法：外阴影**
`box-shadow: <水平偏移> <垂直偏移> <模糊> <颜色>;`
```css
/* 设置外阴影 */
.box {
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：带扩展的外阴影**
`box-shadow: <水平> <垂直> <模糊> <扩展> <颜色>;`
```css
/* 设置带扩展的外阴影 */
.box {
  box-shadow: 2px 4px 8px 2px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：内阴影**
`box-shadow: inset <水平> <垂直> <模糊> <颜色>;`
```css
/* 设置内阴影 */
.box {
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}
```

---

**单行写法：多重阴影**
`box-shadow: <阴影1>, <阴影2>;`
```css
/* 单行设置多重阴影 */
.box {
  box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 4px 8px rgba(0,0,0,0.1);
}
```

---

**换行写法：多重阴影**
`box-shadow: <阴影1>, <阴影2>, <阴影3>;`
```css
/* 换行设置多重阴影 */
.box {
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.1),
    0 4px 8px rgba(0, 0, 0, 0.1),
    0 16px 32px rgba(0, 0, 0, 0.1);
}
```

---

## overflow 溢出

**基本写法：overflow 可见**
`overflow: visible;`
```css
/* 内容溢出时可见 */
.box {
  overflow: visible;
}
```

---

**基本写法：overflow 隐藏**
`overflow: hidden;`
```css
/* 内容溢出时隐藏 */
.box {
  overflow: hidden;
}
```

---

**基本写法：overflow 滚动**
`overflow: scroll;`
```css
/* 始终显示滚动条 */
.box {
  overflow: scroll;
}
```

---

**基本写法：overflow 自动**
`overflow: auto;`
```css
/* 需要时显示滚动条 */
.scroll-area {
  overflow: auto;
}
```

---

**基本写法：overflow-x 水平滚动**
`overflow-x: auto;`
```css
/* 水平方向自动滚动 */
.table-wrapper {
  overflow-x: auto;
}
```

---

**基本写法：overflow-y 垂直滚动**
`overflow-y: auto;`
```css
/* 垂直方向自动滚动 */
.list {
  max-height: 300px;
  overflow-y: auto;
}
```

---

**基本写法：text-overflow 省略号**
`text-overflow: ellipsis;`
```css
/* 文本溢出显示省略号 */
.text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

---

## display 显示类型

**基本写法：block 块级**
`display: block;`
```css
/* 设置为块级元素 */
.span-block {
  display: block;
}
```

---

**基本写法：inline 行内**
`display: inline;`
```css
/* 设置为行内元素 */
.div-inline {
  display: inline;
}
```

---

**基本写法：inline-block 行内块**
`display: inline-block;`
```css
/* 设置为行内块元素 */
.badge {
  display: inline-block;
  padding: 2px 8px;
}
```

---

**基本写法：none 隐藏**
`display: none;`
```css
/* 完全隐藏元素 */
.hidden {
  display: none;
}
```

---

**基本写法：flex 弹性布局**
`display: flex;`
```css
/* 设置为弹性容器 */
.container {
  display: flex;
}
```

---

**基本写法：grid 网格布局**
`display: grid;`
```css
/* 设置为网格容器 */
.layout {
  display: grid;
}
```

---

## visibility 可见性

**基本写法：visible 可见**
`visibility: visible;`
```css
/* 元素可见 */
.box {
  visibility: visible;
}
```

---

**基本写法：hidden 隐藏占位**
`visibility: hidden;`
```css
/* 元素隐藏但保留布局空间 */
.invisible {
  visibility: hidden;
}
```

---

**基本写法：collapse 表格折叠**
`visibility: collapse;`
```css
/* 表格行或列折叠 */
.row {
  visibility: collapse;
}
```

---

## content 内容生成

**基本写法：content 字符串**
`content: "<文本>";`
```css
/* 生成文本内容 */
.label::before {
  content: "标签: ";
}
```

---

**基本写法：content attr 属性**
`content: attr(<属性名>);`
```css
/* 生成元素属性值 */
a::after {
  content: " (" attr(href) ")";
}
```

---

**基本写法：content 空字符串**
`content: "";`
```css
/* 生成空内容用于布局 */
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

---

## 尺寸计算

**基本写法：calc 计算**
`width: calc(<表达式>);`
```css
/* 动态计算宽度 */
.sidebar {
  width: calc(100% - 250px);
}
```

---

**基本写法：calc 混合单位**
`height: calc(<值1> + <值2>);`
```css
/* 混合不同单位计算 */
.hero {
  height: calc(100vh - 60px);
}
```

---

**基本写法：min 取最小值**
`width: min(<值1>, <值2>);`
```css
/* 取两个值中的较小者 */
.container {
  width: min(100%, 1200px);
}
```

---

**基本写法：max 取最大值**
`width: max(<值1>, <值2>);`
```css
/* 取两个值中的较大者 */
.text {
  font-size: max(16px, 2vw);
}
```

---

**基本写法：clamp 区间值**
`width: clamp(<最小>, <理想>, <最大>);`
```css
/* 限制值在指定区间 */
.text {
  font-size: clamp(14px, 2vw, 24px);
}
```



<!-- ============ 文档分隔线：007-css/007-Gradient.md ============ -->

# CSS 渐变

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## linear-gradient 线性渐变

**基本写法：两色线性渐变**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>);`
```css
/* 两色线性渐变 */
.header {
  background: linear-gradient(135deg, #007bff, #0056b3);
}
```

---

**基本写法：三色线性渐变**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>, <颜色3>);`
```css
/* 三色线性渐变 */
.rainbow {
  background: linear-gradient(90deg, red, yellow, green);
}
```

---

**基本写法：to 方向渐变**
`background: linear-gradient(to <方向>, <颜色1>, <颜色2>);`
```css
/* 使用 to 关键字指定方向 */
.header {
  background: linear-gradient(to right, #007bff, #0056b3);
}
```

---

**基本写法：to 双方向渐变**
`background: linear-gradient(to <方向1> <方向2>, <颜色1>, <颜色2>);`
```css
/* 指定对角方向 */
.header {
  background: linear-gradient(to bottom right, #007bff, #0056b3);
}
```

---

**基本写法：角度渐变**
`background: linear-gradient(<角度>, <颜色1>, <颜色2>);`
```css
/* 使用角度指定方向 */
.header {
  background: linear-gradient(45deg, #007bff, #0056b3);
}
```

---

**基本写法：带位置渐变**
`background: linear-gradient(<方向>, <颜色1> <位置1>, <颜色2> <位置2>);`
```css
/* 指定颜色位置 */
.header {
  background: linear-gradient(90deg, #007bff 0%, #0056b3 100%);
}
```

---

**单行写法：多色多位置渐变**
`background: linear-gradient(<方向>, <颜色1> <位置1>, <颜色2> <位置2>, <颜色3> <位置3>);`
```css
/* 单行多色多位置渐变 */
.header {
  background: linear-gradient(90deg, #007bff 0%, #0056b3 50%, #003d7a 100%);
}
```

---

**换行写法：多色多位置渐变**
`background: linear-gradient(<方向>, <颜色1> <位置1>, <颜色2> <位置2>, <颜色3> <位置3>);`
```css
/* 换行多色多位置渐变 */
.header {
  background: linear-gradient(
    90deg,
    #007bff 0%,
    #0056b3 50%,
    #003d7a 100%
  );
}
```

---

**基本写法：硬边渐变**
`background: linear-gradient(<方向>, <颜色1> <位置>, <颜色2> <位置>);`
```css
/* 创建硬边过渡 */
.stripe {
  background: linear-gradient(90deg, #007bff 50%, #0056b3 50%);
}
```

---

## radial-gradient 径向渐变

**基本写法：圆形径向渐变**
`background: radial-gradient(circle, <颜色1>, <颜色2>);`
```css
/* 圆形径向渐变 */
.radial {
  background: radial-gradient(circle, #007bff, #0056b3);
}
```

---

**基本写法：椭圆径向渐变**
`background: radial-gradient(ellipse, <颜色1>, <颜色2>);`
```css
/* 椭圆径向渐变 */
.radial {
  background: radial-gradient(ellipse, #007bff, #0056b3);
}
```

---

**基本写法：带位置径向渐变**
`background: radial-gradient(circle at <位置>, <颜色1>, <颜色2>);`
```css
/* 指定圆心位置 */
.radial {
  background: radial-gradient(circle at top left, #007bff, #0056b3);
}
```

---

**基本写法：带尺寸径向渐变**
`background: radial-gradient(<尺寸> circle, <颜色1>, <颜色2>);`
```css
/* 指定圆尺寸 */
.radial {
  background: radial-gradient(100px circle, #007bff, #0056b3);
}
```

---

**基本写法：closest-side**
`background: radial-gradient(closest-side, <颜色1>, <颜色2>);`
```css
/* 渐变到最近的边 */
.radial {
  background: radial-gradient(closest-side, #007bff, #0056b3);
}
```

---

**基本写法：farthest-corner**
`background: radial-gradient(farthest-corner, <颜色1>, <颜色2>);`
```css
/* 渐变到最远的角 */
.radial {
  background: radial-gradient(farthest-corner, #007bff, #0056b3);
}
```

---

**基本写法：带颜色位置径向渐变**
`background: radial-gradient(circle, <颜色1> <位置1>, <颜色2> <位置2>);`
```css
/* 指定颜色位置 */
.radial {
  background: radial-gradient(circle, #007bff 0%, #0056b3 100%);
}
```

---

## conic-gradient 圆锥渐变

**基本写法：圆锥渐变**
`background: conic-gradient(<颜色1>, <颜色2>, <颜色1>);`
```css
/* 圆锥渐变 */
.conic {
  background: conic-gradient(red, yellow, green, red);
}
```

---

**基本写法：带角度圆锥渐变**
`background: conic-gradient(from <角度>, <颜色1>, <颜色2>);`
```css
/* 指定起始角度 */
.conic {
  background: conic-gradient(from 0deg, red, yellow, green, red);
}
```

---

**基本写法：带位置圆锥渐变**
`background: conic-gradient(from <角度> at <位置>, <颜色1>, <颜色2>);`
```css
/* 指定起始角度和位置 */
.conic {
  background: conic-gradient(from 0deg at center, red, yellow, green, red);
}
```

---

**基本写法：硬边圆锥渐变**
`background: conic-gradient(<颜色1> <角度1>, <颜色2> <角度2>);`
```css
/* 创建饼图效果 */
.pie {
  background: conic-gradient(red 0deg 90deg, blue 90deg 360deg);
}
```

---

## repeating-linear-gradient 重复线性渐变

**基本写法：重复线性渐变**
`background: repeating-linear-gradient(<方向>, <颜色1>, <颜色2> <宽度>);`
```css
/* 重复线性渐变 */
.stripes {
  background: repeating-linear-gradient(45deg, #007bff, #007bff 10px, #0056b3 10px, #0056b3 20px);
}
```

---

**基本写法：水平条纹**
`background: repeating-linear-gradient(<方向>, <颜色1> <宽度>, <颜色2> <宽度>);`
```css
/* 水平条纹背景 */
.stripes {
  background: repeating-linear-gradient(0deg, #007bff 0, #007bff 10px, #0056b3 10px, #0056b3 20px);
}
```

---

**基本写法：垂直条纹**
`background: repeating-linear-gradient(<方向>, <颜色1> <宽度>, <颜色2> <宽度>);`
```css
/* 垂直条纹背景 */
.stripes {
  background: repeating-linear-gradient(90deg, #007bff 0, #007bff 10px, #0056b3 10px, #0056b3 20px);
}
```

---

## repeating-radial-gradient 重复径向渐变

**基本写法：重复径向渐变**
`background: repeating-radial-gradient(circle, <颜色1>, <颜色2> <宽度>);`
```css
/* 重复径向渐变 */
.rings {
  background: repeating-radial-gradient(circle, #007bff 0, #007bff 10px, #0056b3 10px, #0056b3 20px);
}
```

---

**基本写法：同心圆**
`background: repeating-radial-gradient(<颜色1> <宽度>, <颜色2> <宽度>);`
```css
/* 同心圆效果 */
.rings {
  background: repeating-radial-gradient(circle at center, #007bff 0, #007bff 5px, transparent 5px, transparent 10px);
}
```

---

## 多重渐变

**单行写法：多重渐变**
`background: <渐变1>, <渐变2>;`
```css
/* 单行设置多重渐变 */
.box {
  background: linear-gradient(135deg, transparent, rgba(0,0,0,0.5)), radial-gradient(circle, #007bff, #0056b3);
}
```

---

**换行写法：多重渐变**
`background: <渐变1>, <渐变2>, <渐变3>;`
```css
/* 换行设置多重渐变 */
.box {
  background:
    linear-gradient(135deg, transparent, rgba(0,0,0,0.5)),
    radial-gradient(circle, #007bff, #0056b3),
    url("texture.png");
}
```

---

## 渐变与变量

**基本写法：使用变量定义渐变**
`:root { --gradient-<名>: <渐变值>; }`
```css
/* 定义渐变变量 */
:root {
  --gradient-primary: linear-gradient(135deg, #007bff, #0056b3);
  --gradient-secondary: linear-gradient(135deg, #6c757d, #495057);
}
```

---

**基本写法：使用渐变变量**
`background: var(--gradient-<名>);`
```css
/* 使用渐变变量 */
.header {
  background: var(--gradient-primary);
}
```

---

**基本写法：变量在渐变中使用**
`background: linear-gradient(<方向>, var(--<颜色1>), var(--<颜色2>));`
```css
/* 在渐变中使用颜色变量 */
.header {
  background: linear-gradient(135deg, var(--color-start), var(--color-end));
}
```

---

## 渐变方向

**基本写法：to top 向上**
`background: linear-gradient(to top, <颜色1>, <颜色2>);`
```css
/* 向上的渐变 */
.box {
  background: linear-gradient(to top, #007bff, #0056b3);
}
```

---

**基本写法：to bottom 向下**
`background: linear-gradient(to bottom, <颜色1>, <颜色2>);`
```css
/* 向下的渐变 */
.box {
  background: linear-gradient(to bottom, #007bff, #0056b3);
}
```

---

**基本写法：to left 向左**
`background: linear-gradient(to left, <颜色1>, <颜色2>);`
```css
/* 向左的渐变 */
.box {
  background: linear-gradient(to left, #007bff, #0056b3);
}
```

---

**基本写法：to right 向右**
`background: linear-gradient(to right, <颜色1>, <颜色2>);`
```css
/* 向右的渐变 */
.box {
  background: linear-gradient(to right, #007bff, #0056b3);
}
```

---

## 透明度渐变

**基本写法：透明渐变**
`background: linear-gradient(<方向>, transparent, <颜色>);`
```css
/* 从透明到不透明 */
.fade {
  background: linear-gradient(to bottom, transparent, #000000);
}
```

---

**基本写法：半透明渐变**
`background: linear-gradient(<方向>, rgba(<颜色>, <透明度1>), rgba(<颜色>, <透明度2>));`
```css
/* 半透明渐变 */
.overlay {
  background: linear-gradient(135deg, rgba(0,123,255,0.8), rgba(0,86,179,0.6));
}
```

---

**基本写法：淡出效果**
`background: linear-gradient(<方向>, <颜色>, transparent);`
```css
/* 从不透明到透明 */
.fade-out {
  background: linear-gradient(to bottom, #007bff, transparent);
}
```

---

## 渐变动画

**基本写法：渐变过渡**
`background-size: <尺寸>; transition: background-position <时长>;`
```css
/* 渐变背景过渡动画 */
.animated {
  background: linear-gradient(90deg, #007bff, #0056b3, #007bff);
  background-size: 200% 100%;
  transition: background-position 0.5s;
}
.animated:hover {
  background-position: 100% 0;
}
```

---

**基本写法：渐变流动动画**
`@keyframes <名称> { from { background-position: 0% 0%; } to { background-position: 100% 0%; } }`
```css
/* 渐变流动动画 */
@keyframes gradientFlow {
  from { background-position: 0% 0%; }
  to { background-position: 100% 0%; }
}
.flowing {
  background: linear-gradient(90deg, #007bff, #0056b3, #007bff);
  background-size: 200% 100%;
  animation: gradientFlow 3s linear infinite;
}
```

---

## 常见渐变效果

**基本写法：按钮渐变**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>);`
```css
/* 按钮渐变背景 */
.btn {
  background: linear-gradient(135deg, #007bff, #0056b3);
}
```

---

**基本写法：卡片渐变**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>);`
```css
/* 卡片渐变背景 */
.card {
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
}
```

---

**基本写法：遮罩渐变**
`background: linear-gradient(<方向>, transparent, <颜色>);`
```css
/* 底部遮罩渐变 */
.overlay {
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
}
```

---

**基本写法：网格背景**
`background: linear-gradient(<方向1>, <颜色> <宽度>, transparent <宽度>), linear-gradient(<方向2>, <颜色> <宽度>, transparent <宽度>);`
```css
/* 网格背景 */
.grid-bg {
  background:
    linear-gradient(90deg, #ccc 1px, transparent 1px),
    linear-gradient(0deg, #ccc 1px, transparent 1px);
  background-size: 20px 20px;
}
```

---

**基本写法：对角条纹**
`background: repeating-linear-gradient(45deg, <颜色1> <宽度>, <颜色2> <宽度>);`
```css
/* 对角条纹背景 */
.diagonal-stripes {
  background: repeating-linear-gradient(45deg, #007bff 0, #007bff 10px, #0056b3 10px, #0056b3 20px);
}
```

---

**基本写法：棋盘格背景**
`background: conic-gradient(<颜色1> <角度>, <颜色2> <角度>, <颜色1> <角度>, <颜色2> <角度>);`
```css
/* 棋盘格背景 */
.checkerboard {
  background: conic-gradient(#000 0deg 90deg, #fff 90deg 180deg, #000 180deg 270deg, #fff 270deg 360deg);
  background-size: 50px 50px;
}
```

---

## 渐变文本

**基本写法：渐变文字**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>); -webkit-background-clip: text; color: transparent;`
```css
/* 渐变文字效果 */
.gradient-text {
  background: linear-gradient(135deg, #007bff, #0056b3);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

---

**基本写法：多色渐变文字**
`background: linear-gradient(<方向>, <颜色1>, <颜色2>, <颜色3>); -webkit-background-clip: text; color: transparent;`
```css
/* 多色渐变文字 */
.rainbow-text {
  background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
```

---

## 响应式渐变

**基本写法：clamp 响应式渐变**
`background: linear-gradient(<角度>, <颜色1>, <颜色2>)`
```css
/* 响应式渐变角度 */
.box {
  background: linear-gradient(clamp(45deg, 10vw, 135deg), #007bff, #0056b3);
}
```

---

**基本写法：媒体查询调整渐变**
`@media (max-width: <值>) { background: <渐变>; }`
```css
/* 小屏幕调整渐变 */
.box {
  background: linear-gradient(135deg, #007bff, #0056b3);
}
@media (max-width: 768px) {
  .box {
    background: linear-gradient(180deg, #007bff, #0056b3);
  }
}
```

---

**基本写法：嵌套媒体查询渐变**
`.box { background: <渐变>; @media (max-width: <值>) { background: <渐变>; } }`
```css
/* CSS 原生嵌套媒体查询渐变 */
.box {
  background: linear-gradient(135deg, #007bff, #0056b3);
  @media (max-width: 768px) {
    background: linear-gradient(180deg, #007bff, #0056b3);
  }
}
```



<!-- ============ 文档分隔线：007-css/008-MediaQuery.md ============ -->

# CSS 媒体查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础语法

**基本写法：media 基本语法**
`@media <条件> { <样式> }`
```css
/* 基本媒体查询 */
@media screen {
  body {
    font-size: 16px;
  }
}
```

---

**基本写法：media 媒体类型**
`@media <类型> { <样式> }`
```css
/* 指定媒体类型 */
@media print {
  body {
    color: black;
  }
}
```

---

**基本写法：media screen 屏幕**
`@media screen { <样式> }`
```css
/* 屏幕设备样式 */
@media screen {
  .container {
    max-width: 1200px;
  }
}
```

---

**基本写法：media print 打印**
`@media print { <样式> }`
```css
/* 打印样式 */
@media print {
  .no-print {
    display: none;
  }
}
```

---

**基本写法：media all 所有**
`@media all { <样式> }`
```css
/* 所有设备 */
@media all {
  body {
    margin: 0;
  }
}
```

---

## 宽度查询

**基本写法：max-width 最大宽度**
`@media (max-width: <值>) { <样式> }`
```css
/* 屏幕宽度小于等于指定值 */
@media (max-width: 768px) {
  .container {
    padding: 10px;
  }
}
```

---

**基本写法：min-width 最小宽度**
`@media (min-width: <值>) { <样式> }`
```css
/* 屏幕宽度大于等于指定值 */
@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
}
```

---

**基本写法：宽度范围**
`@media (min-width: <值>) and (max-width: <值>) { <样式> }`
```css
/* 屏幕宽度在指定范围内 */
@media (min-width: 768px) and (max-width: 1024px) {
  .container {
    width: 750px;
  }
}
```

---

## 高度查询

**基本写法：max-height 最大高度**
`@media (max-height: <值>) { <样式> }`
```css
/* 屏幕高度小于等于指定值 */
@media (max-height: 500px) {
  .header {
    height: 40px;
  }
}
```

---

**基本写法：min-height 最小高度**
`@media (min-height: <值>) { <样式> }`
```css
/* 屏幕高度大于等于指定值 */
@media (min-height: 800px) {
  .hero {
    height: 600px;
  }
}
```

---

**基本写法：高度范围**
`@media (min-height: <值>) and (max-height: <值>) { <样式> }`
```css
/* 屏幕高度在指定范围内 */
@media (min-height: 600px) and (max-height: 900px) {
  .hero {
    height: 400px;
  }
}
```

---

## 方向查询

**基本写法：orientation 横屏**
`@media (orientation: landscape) { <样式> }`
```css
/* 横屏时应用 */
@media (orientation: landscape) {
  .layout {
    flex-direction: row;
  }
}
```

---

**基本写法：orientation 竖屏**
`@media (orientation: portrait) { <样式> }`
```css
/* 竖屏时应用 */
@media (orientation: portrait) {
  .layout {
    flex-direction: column;
  }
}
```

---

## 分辨率查询

**基本写法：min-resolution 最小分辨率**
`@media (min-resolution: <值>dppx) { <样式> }`
```css
/* 高分辨率屏幕 */
@media (min-resolution: 2dppx) {
  .logo {
    background-image: url('logo@2x.png');
  }
}
```

---

**基本写法：min-resolution dpi**
`@media (min-resolution: <值>dpi) { <样式> }`
```css
/* 指定 dpi 分辨率 */
@media (min-resolution: 192dpi) {
  .logo {
    background-image: url('logo@2x.png');
  }
}
```

---

## 逻辑操作符

**基本写法：and 与操作**
`@media (<条件1>) and (<条件2>) { <样式> }`
```css
/* 同时满足多个条件 */
@media (min-width: 768px) and (max-width: 1024px) {
  .container {
    width: 750px;
  }
}
```

---

**基本写法：or 或操作**
`@media (<条件1>), (<条件2>) { <样式> }`
```css
/* 满足任一条件 */
@media (max-width: 480px), (min-width: 1200px) {
  .sidebar {
    display: none;
  }
}
```

---

**基本写法：not 非 操作**
`@media not <条件> { <样式> }`
```css
/* 不满足条件时应用 */
@media not print {
  body {
    background: white;
  }
}
```

---

**基本写法：only 仅**
`@media only <类型> { <样式> }`
```css
/* 仅对支持媒体查询的设备应用 */
@media only screen {
  .container {
    max-width: 1200px;
  }
}
```

---

**单行写法：多逻辑组合**
`@media (<条件1>) and (<条件2>), (<条件3>) { <样式> }`
```css
/* 单行组合多个逻辑条件 */
@media (min-width: 768px) and (orientation: landscape), (min-width: 1200px) { .layout { flex-direction: row; } }
```

---

**换行写法：多逻辑组合**
`@media (<条件1>) and (<条件2>), (<条件3>) { <样式> }`
```css
/* 换行组合多个逻辑条件 */
@media (min-width: 768px) and (orientation: landscape),
       (min-width: 1200px) {
  .layout {
    flex-direction: row;
  }
}
```

---

## 用户偏好查询

**基本写法：prefers-color-scheme 暗色**
`@media (prefers-color-scheme: dark) { <样式> }`
```css
/* 用户偏好暗色主题 */
@media (prefers-color-scheme: dark) {
  body {
    background-color: #1a1a1a;
    color: #ffffff;
  }
}
```

---

**基本写法：prefers-color-scheme 亮色**
`@media (prefers-color-scheme: light) { <样式> }`
```css
/* 用户偏好亮色主题 */
@media (prefers-color-scheme: light) {
  body {
    background-color: #ffffff;
    color: #333333;
  }
}
```

---

**基本写法：prefers-reduced-motion 减少动画**
`@media (prefers-reduced-motion: reduce) { <样式> }`
```css
/* 用户偏好减少动画 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

**基本写法：prefers-reduced-motion 无偏好**
`@media (prefers-reduced-motion: no-preference) { <样式> }`
```css
/* 用户无动画偏好 */
@media (prefers-reduced-motion: no-preference) {
  .box {
    transition: transform 0.3s;
  }
}
```

---

**基本写法：prefers-contrast 高对比度**
`@media (prefers-contrast: more) { <样式> }`
```css
/* 用户偏好高对比度 */
@media (prefers-contrast: more) {
  .text {
    color: black;
    background: white;
  }
}
```

---

**基本写法：prefers-contrast 低对比度**
`@media (prefers-contrast: less) { <样式> }`
```css
/* 用户偏好低对比度 */
@media (prefers-contrast: less) {
  .text {
    color: #666;
    background: #f5f5f5;
  }
}
```

---

**基本写法：forced-colors 强制颜色**
`@media (forced-colors: active) { <样式> }`
```css
/* 系统强制颜色模式 */
@media (forced-colors: active) {
  .button {
    border: 1px solid ButtonText;
  }
}
```

---

## 设备特性查询

**基本写法：hover 悬停支持**
`@media (hover: hover) { <样式> }`
```css
/* 设备支持悬停 */
@media (hover: hover) {
  .button:hover {
    background-color: #0056b3;
  }
}
```

---

**基本写法：hover 无悬停**
`@media (hover: none) { <样式> }`
```css
/* 设备不支持悬停 */
@media (hover: none) {
  .button {
    padding: 12px 24px;
  }
}
```

---

**基本写法：pointer 精确指针**
`@media (pointer: fine) { <样式> }`
```css
/* 设备有精确指针 */
@media (pointer: fine) {
  .tooltip {
    display: block;
  }
}
```

---

**基本写法：pointer 粗略指针**
`@media (pointer: coarse) { <样式> }`
```css
/* 设备为粗略指针（触摸） */
@media (pointer: coarse) {
  .button {
    padding: 12px 24px;
  }
}
```

---

**基本写法：any-pointer 任一精确**
`@media (any-pointer: fine) { <样式> }`
```css
/* 任一输入设备为精确指针 */
@media (any-pointer: fine) {
  .tooltip {
    display: block;
  }
}
```

---

**基本写法：any-hover 任一悬停**
`@media (any-hover: hover) { <样式> }`
```css
/* 任一输入设备支持悬停 */
@media (any-hover: hover) {
  .button:hover {
    background-color: #0056b3;
  }
}
```

---

## 视口特性查询

**基本写法：aspect-ratio 宽高比**
`@media (aspect-ratio: <宽>/<高>) { <样式> }`
```css
/* 指定宽高比 */
@media (aspect-ratio: 16/9) {
  .video {
    width: 100%;
  }
}
```

---

**基本写法：min-aspect-ratio 最小宽高比**
`@media (min-aspect-ratio: <宽>/<高>) { <样式> }`
```css
/* 宽高比大于指定值 */
@media (min-aspect-ratio: 16/9) {
  .layout {
    flex-direction: row;
  }
}
```

---

**基本写法：max-aspect-ratio 最大宽高比**
`@media (max-aspect-ratio: <宽>/<高>) { <样式> }`
```css
/* 宽高比小于指定值 */
@media (max-aspect-ratio: 1/1) {
  .layout {
    flex-direction: column;
  }
}
```

---

## 媒体函数

**基本写法：range 语法**
`@media (width >= <值>) { <样式> }`
```css
/* 使用范围语法 */
@media (width >= 768px) {
  .container {
    max-width: 720px;
  }
}
```

---

**基本写法：range 区间**
`@media (<最小> <= width <= <最大>) { <样式> }`
```css
/* 使用区间语法 */
@media (768px <= width <= 1024px) {
  .container {
    width: 750px;
  }
}
```

---

**基本写法：not 否定**
`@media not (<条件>) { <样式> }`
```css
/* 否定条件 */
@media not (prefers-color-scheme: dark) {
  body {
    background: white;
  }
}
```

---

## 媒体查询嵌套

**基本写法：嵌套媒体查询**
`<选择器> { @media <条件> { <样式> } }`
```css
/* CSS 原生嵌套 */
.container {
  width: 100%;
  @media (min-width: 768px) {
    max-width: 720px;
  }
}
```

---

**单行写法：嵌套多媒体查询**
`<选择器> { @media <条件1> { <样式> } @media <条件2> { <样式> } }`
```css
/* 单行嵌套多个媒体查询 */
.col { width: 100%; @media (min-width: 768px) { width: 50%; } @media (min-width: 1200px) { width: 33%; } }
```

---

**换行写法：嵌套多媒体查询**
`<选择器> { @media <条件1> { <样式> } @media <条件2> { <样式> } }`
```css
/* 换行嵌套多个媒体查询 */
.col {
  width: 100%;
  @media (min-width: 768px) {
    width: 50%;
  }
  @media (min-width: 1200px) {
    width: 33%;
  }
}
```

---

## @import 媒体查询

**基本写法：@import 带媒体查询**
`@import url("<文件>") <条件>;`
```css
/* 导入样式并应用媒体查询 */
@import url("mobile.css") (max-width: 768px);
```

---

**基本写法：@import 多条件**
`@import url("<文件>") <条件1> and <条件2>;`
```css
/* 导入样式并应用多条件 */
@import url("tablet.css") (min-width: 768px) and (max-width: 1024px);
```

---

## @supports 特性查询

**基本写法：supports 属性支持**
`@supports (<属性>: <值>) { <样式> }`
```css
/* 检查属性支持 */
@supports (display: grid) {
  .container {
    display: grid;
  }
}
```

---

**基本写法：supports not 不支持**
`@supports not (<属性>: <值>) { <样式> }`
```css
/* 检查属性不支持 */
@supports not (display: grid) {
  .container {
    display: flex;
  }
}
```

---

**基本写法：supports and 与**
`@supports (<属性1>: <值>) and (<属性2>: <值>) { <样式> }`
```css
/* 同时检查多个属性支持 */
@supports (display: grid) and (gap: 10px) {
  .grid {
    display: grid;
    gap: 10px;
  }
}
```

---

**基本写法：supports or 或**
`@supports (<属性1>: <值>) or (<属性2>: <值>) { <样式> }`
```css
/* 检查任一属性支持 */
@supports (-webkit-backdrop-filter: blur(10px)) or (backdrop-filter: blur(10px)) {
  .modal {
    backdrop-filter: blur(10px);
  }
}
```

---

**基本写法：selector 选择器支持**
`@supports selector(<选择器>) { <样式> }`
```css
/* 检查选择器支持 */
@supports selector(:has(*)) {
  .card:has(img) {
    padding: 10px;
  }
}
```

---

## 断点规范

**基本写法：移动优先断点**
`@media (min-width: <值>) { <样式> }`
```css
/* 移动优先断点系统 */
.container { width: 100%; }
@media (min-width: 576px) { .container { max-width: 540px; } }
@media (min-width: 768px) { .container { max-width: 720px; } }
@media (min-width: 992px) { .container { max-width: 960px; } }
@media (min-width: 1200px) { .container { max-width: 1140px; } }
```

---

**基本写法：桌面优先断点**
`@media (max-width: <值>) { <样式> }`
```css
/* 桌面优先断点系统 */
.container { max-width: 1140px; }
@media (max-width: 1199px) { .container { max-width: 960px; } }
@media (max-width: 991px) { .container { max-width: 720px; } }
@media (max-width: 767px) { .container { max-width: 540px; } }
@media (max-width: 575px) { .container { max-width: 100%; } }
```

---

## 常见媒体查询模式

**基本写法：隐藏元素**
`@media (max-width: <值>) { <选择器> { display: none; } }`
```css
/* 小屏隐藏元素 */
@media (max-width: 768px) {
  .sidebar {
    display: none;
  }
}
```

---

**基本写法：切换布局**
`@media (max-width: <值>) { <选择器> { flex-direction: column; } }`
```css
/* 小屏切换为列布局 */
.layout {
  display: flex;
  flex-direction: row;
}
@media (max-width: 768px) {
  .layout {
    flex-direction: column;
  }
}
```

---

**基本写法：调整字号**
`@media (max-width: <值>) { <选择器> { font-size: <值>; } }`
```css
/* 小屏调整字号 */
.title {
  font-size: 2rem;
}
@media (max-width: 768px) {
  .title {
    font-size: 1.5rem;
  }
}
```

---

**基本写法：调整间距**
`@media (max-width: <值>) { <选择器> { padding: <值>; } }`
```css
/* 小屏调整间距 */
.section {
  padding: 40px;
}
@media (max-width: 768px) {
  .section {
    padding: 20px;
  }
}
```

---

## 用户偏好媒体查询(2024)

**基本写法：prefers-reduced-motion 减少动画**
`@media (prefers-reduced-motion: reduce) { <样式> }`
```css
/* 用户偏好减少动画,关闭非必要动效 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

**基本写法：prefers-color-scheme 色彩偏好**
`@media (prefers-color-scheme: <dark|light>) { <样式> }`
```css
/* 用户系统级色彩偏好 */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --text: #ffffff;
  }
  body {
    background-color: var(--bg);
    color: var(--text);
  }
}
```

---

**基本写法：prefers-contrast 对比度偏好**
`@media (prefers-contrast: <more|less|custom>) { <样式> }`
```css
/* 用户对比度偏好设置 */
@media (prefers-contrast: more) {
  .text {
    color: black;
    background: white;
    border: 2px solid black;
  }
}
```

---

**基本写法：prefers-reduced-transparency 减少透明**
`@media (prefers-reduced-transparency: reduce) { <样式> }`
```css
/* 用户偏好减少透明度效果 */
@media (prefers-reduced-transparency: reduce) {
  .modal {
    background-color: rgba(0, 0, 0, 0.95);
  }
  .glass {
    backdrop-filter: none;
    background-color: #f5f5f5;
  }
}
```

---

**基本写法：inverted-colors 反色模式**
`@media (inverted-colors: inverted) { <样式> }`
```css
/* 系统级颜色反转模式 */
@media (inverted-colors: inverted) {
  /* 反色模式下调整图片避免二次反转 */
  img,
  video {
    filter: invert(1);
  }
}
```



<!-- ============ 文档分隔线：007-css/009-PseudoClassDetailed.md ============ -->

# CSS 伪类详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 交互状态伪类

**基本写法：hover 悬停**
`<选择器>:hover { <样式> }`
```css
/* 鼠标悬停状态 */
.button:hover {
  background-color: #0056b3;
}
```

---

**基本写法：focus 聚焦**
`<选择器>:focus { <样式> }`
```css
/* 元素获得焦点 */
input:focus {
  border-color: #007bff;
}
```

---

**基本写法：focus-visible 键盘聚焦**
`<选择器>:focus-visible { <样式> }`
```css
/* 仅键盘聚焦时显示 */
button:focus-visible {
  outline: 2px solid #007bff;
}
```

---

**基本写法：focus-within 子元素聚焦**
`<选择器>:focus-within { <样式> }`
```css
/* 子元素获得焦点时 */
.form:focus-within {
  border-color: #007bff;
}
```

---

**基本写法：active 激活**
`<选择器>:active { <样式> }`
```css
/* 元素被激活（点击） */
.button:active {
  transform: scale(0.95);
}
```

---

**基本写法：visited 已访问**
`<选择器>:visited { <样式> }`
```css
/* 链接已访问状态 */
a:visited {
  color: purple;
}
```

---

**基本写法：link 未访问**
`<选择器>:link { <样式> }`
```css
/* 链接未访问状态 */
a:link {
  color: blue;
}
```

---

## 表单状态伪类

**基本写法：checked 选中**
`<选择器>:checked { <样式> }`
```css
/* 复选框或单选框选中 */
input:checked {
  accent-color: #007bff;
}
```

---

**基本写法：disabled 禁用**
`<选择器>:disabled { <样式> }`
```css
/* 表单元素禁用 */
input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}
```

---

**基本写法：enabled 可用**
`<选择器>:enabled { <样式> }`
```css
/* 表单元素可用 */
input:enabled {
  background-color: white;
}
```

---

**基本写法：required 必填**
`<选择器>:required { <样式> }`
```css
/* 必填字段 */
input:required {
  border-color: red;
}
```

---

**基本写法：optional 可选**
`<选择器>:optional { <样式> }`
```css
/* 可选字段 */
input:optional {
  border-color: #ccc;
}
```

---

**基本写法：valid 有效**
`<选择器>:valid { <样式> }`
```css
/* 表单验证通过 */
input:valid {
  border-color: green;
}
```

---

**基本写法：invalid 无效**
`<选择器>:invalid { <样式> }`
```css
/* 表单验证失败 */
input:invalid {
  border-color: red;
}
```

---

**基本写法：in-range 范围内**
`<选择器>:in-range { <样式> }`
```css
/* 数值在指定范围内 */
input:in-range {
  border-color: green;
}
```

---

**基本写法：out-of-range 范围外**
`<选择器>:out-of-range { <样式> }`
```css
/* 数值超出指定范围 */
input:out-of-range {
  border-color: red;
}
```

---

**基本写法：read-only 只读**
`<选择器>:read-only { <样式> }`
```css
/* 只读字段 */
input:read-only {
  background-color: #f5f5f5;
}
```

---

**基本写法：read-write 可读写**
`<选择器>:read-write { <样式> }`
```css
/* 可读写字段 */
input:read-write {
  background-color: white;
}
```

---

**基本写法：placeholder-shown 占位符显示**
`<选择器>:placeholder-shown { <样式> }`
```css
/* 显示占位符时 */
input:placeholder-shown {
  border-color: #ccc;
}
```

---

**基本写法：default 默认选中**
`<选择器>:default { <样式> }`
```css
/* 默认选中的表单元素 */
input:default {
  box-shadow: 0 0 2px blue;
}
```

---

## 结构伪类

**基本写法：first-child 首个子元素**
`<选择器>:first-child { <样式> }`
```css
/* 父元素的第一个子元素 */
li:first-child {
  font-weight: bold;
}
```

---

**基本写法：last-child 末尾子元素**
`<选择器>:last-child { <样式> }`
```css
/* 父元素的最后一个子元素 */
li:last-child {
  border-bottom: none;
}
```

---

**基本写法：only-child 唯一子元素**
`<选择器>:only-child { <样式> }`
```css
/* 父元素中唯一的子元素 */
div:only-child {
  border: 1px solid red;
}
```

---

**基本写法：nth-child 索引选择**
`<选择器>:nth-child(<n>) { <样式> }`
```css
/* 第 n 个子元素 */
li:nth-child(3) {
  color: red;
}
```

---

**基本写法：nth-child 奇数**
`<选择器>:nth-child(odd) { <样式> }`
```css
/* 所有奇数行 */
tr:nth-child(odd) {
  background-color: #f9f9f9;
}
```

---

**基本写法：nth-child 偶数**
`<选择器>:nth-child(even) { <样式> }`
```css
/* 所有偶数行 */
tr:nth-child(even) {
  background-color: #ffffff;
}
```

---

**基本写法：nth-child 公式**
`<选择器>:nth-child(<公式>) { <样式> }`
```css
/* 每隔 3 个元素 */
li:nth-child(3n+1) {
  color: blue;
}
```

---

**基本写法：nth-last-child 倒数索引**
`<选择器>:nth-last-child(<n>) { <样式> }`
```css
/* 倒数第 n 个子元素 */
li:nth-last-child(2) {
  color: red;
}
```

---

**基本写法：first-of-type 同类型首个**
`<选择器>:first-of-type { <样式> }`
```css
/* 同级同类型第一个元素 */
p:first-of-type {
  margin-top: 0;
}
```

---

**基本写法：last-of-type 同类型末尾**
`<选择器>:last-of-type { <样式> }`
```css
/* 同级同类型最后一个元素 */
p:last-of-type {
  margin-bottom: 0;
}
```

---

**基本写法：nth-of-type 索引选择**
`<选择器>:nth-of-type(<n>) { <样式> }`
```css
/* 同类型第 n 个元素 */
p:nth-of-type(2) {
  color: blue;
}
```

---

**基本写法：nth-last-of-type 倒数同类型**
`<选择器>:nth-last-of-type(<n>) { <样式> }`
```css
/* 同类型倒数第 n 个元素 */
p:nth-last-of-type(2) {
  color: red;
}
```

---

**基本写法：only-of-type 唯一同类型**
`<选择器>:only-of-type { <样式> }`
```css
/* 同类型唯一元素 */
img:only-of-type {
  border: 2px solid blue;
}
```

---

**基本写法：empty 空元素**
`<选择器>:empty { <样式> }`
```css
/* 没有子元素的元素 */
div:empty {
  display: none;
}
```

---

**基本写法：root 根元素**
`:root { <样式> }`
```css
/* 文档根元素 html */
:root {
  --primary-color: #007bff;
}
```

---

## 目标伪类

**基本写法：target 锚点目标**
`<选择器>:target { <样式> }`
```css
/* 当前锚点指向的元素 */
#section:target {
  background-color: #ffffcc;
}
```

---

## 语言伪类

**基本写法：lang 语言匹配**
`<选择器>:lang(<语言>) { <样式> }`
```css
/* 匹配指定语言 */
p:lang(zh) {
  font-family: "Microsoft YaHei", sans-serif;
}
```

---

## 否定伪类

**基本写法：not 否定**
`<选择器>:not(<排除选择器>) { <样式> }`
```css
/* 排除指定选择器 */
input:not([disabled]) {
  border: 1px solid #ccc;
}
```

---

**基本写法：not 多重否定**
`<选择器>:not(<选择器1>):not(<选择器2>) { <样式> }`
```css
/* 多重否定 */
input:not([disabled]):not([type="hidden"]) {
  border: 1px solid #ccc;
}
```

---

## 匹配伪类

**基本写法：is 匹配任一**
`:is(<选择器1>, <选择器2>) { <样式> }`
```css
/* 匹配多个选择器 */
:is(h1, h2, h3) {
  font-family: sans-serif;
}
```

---

**基本写法：where 匹配任一**
`:where(<选择器1>, <选择器2>) { <样式> }`
```css
/* 匹配多个选择器（零特异性） */
:where(.card, .panel) {
  padding: 1rem;
}
```

---

**基本写法：has 父选择器**
`<选择器>:has(<子选择器>) { <样式> }`
```css
/* 选中包含指定子元素的父元素 */
div:has(img) {
  padding: 10px;
}
```

---

**基本写法：has 否定**
`<选择器>:not(:has(<子选择器>)) { <样式> }`
```css
/* 不包含指定子元素 */
div:not(:has(img)) {
  background: #f5f5f5;
}
```



<!-- ============ 文档分隔线：007-css/010-PseudoElementDetailed.md ============ -->

# CSS 伪元素详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 伪元素

**基本写法：before 前置内容**
`<选择器>::before { content: <内容>; <样式> }`
```css
/* 在元素前插入内容 */
.quote::before {
  content: '"';
  color: gray;
}
```

---

**基本写法：after 后置内容**
`<选择器>::after { content: <内容>; <样式> }`
```css
/* 在元素后插入内容 */
.quote::after {
  content: '"';
  color: gray;
}
```

---

**基本写法：before 装饰元素**
`<选择器>::before { content: ""; <样式> }`
```css
/* 创建装饰性元素 */
.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: #007bff;
}
```

---

**基本写法：first-letter 首字母**
`<选择器>::first-letter { <样式> }`
```css
/* 段落首字母样式 */
p::first-letter {
  font-size: 2em;
  font-weight: bold;
}
```

---

**基本写法：first-line 首行**
`<选择器>::first-line { <样式> }`
```css
/* 段落首行样式 */
p::first-line {
  text-transform: uppercase;
}
```

---

**基本写法：selection 选中文本**
`<选择器>::selection { <样式> }`
```css
/* 自定义文本选中样式 */
::selection {
  background-color: #007bff;
  color: white;
}
```

---

**基本写法：placeholder 占位符**
`<选择器>::placeholder { <样式> }`
```css
/* 输入框占位符样式 */
input::placeholder {
  color: #999;
}
```

---

**基本写法：marker 列表标记**
`<选择器>::marker { <样式> }`
```css
/* 列表项标记样式 */
li::marker {
  color: #007bff;
  font-weight: bold;
}
```

---

**基本写法：backdrop 背景层**
`<选择器>::backdrop { <样式> }`
```css
/* 全屏元素背景层 */
dialog::backdrop {
  background: rgba(0, 0, 0, 0.5);
}
```

---

**基本写法：file-selector-button 文件选择按钮**
`<选择器>::file-selector-button { <样式> }`
```css
/* 文件输入框按钮样式 */
input[type="file"]::file-selector-button {
  padding: 8px 16px;
  background: #007bff;
  color: white;
  border: none;
}
```

---

## 伪元素内容生成

**基本写法：content 字符串**
`content: "<文本>";`
```css
/* 生成文本内容 */
.label::before {
  content: "标签: ";
}
```

---

**基本写法：content attr 属性**
`content: attr(<属性名>);`
```css
/* 生成元素属性值 */
a::after {
  content: " (" attr(href) ")";
}
```

---

**基本写法：content 空字符串**
`content: "";`
```css
/* 生成空内容用于布局 */
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

---

**基本写法：content url 图片**
`content: url("<图片路径>");`
```css
/* 生成图片内容 */
.icon::before {
  content: url("icon.png");
}
```

---

**基本写法：content 计数器**
`content: counter(<计数器名>);`
```css
/* 显示计数器值 */
li::before {
  content: counter(item) ". ";
}
```

---

## 计数器

**基本写法：counter-reset 重置计数器**
`counter-reset: <计数器名> <初始值>;`
```css
/* 重置计数器 */
ol {
  counter-reset: section;
}
```

---

**基本写法：counter-increment 递增计数器**
`counter-increment: <计数器名> <步长>;`
```css
/* 计数器递增 */
li {
  counter-increment: section;
}
```

---

**基本写法：counter 显示计数器**
`content: counter(<计数器名>);`
```css
/* 显示计数器值 */
li::before {
  content: "第 " counter(section) " 章: ";
}
```

---

**基本写法：counter 自定义样式**
`content: counter(<计数器名>, <样式>);`
```css
/* 计数器使用中文数字 */
li::before {
  content: counter(section, cjk-ideographic) "、";
}
```

---

**基本写法：counters 嵌套计数器**
`content: counters(<计数器名>, "<分隔符>");`
```css
/* 嵌套计数器 */
li::before {
  content: counters(section, ".") " ";
}
```

---

## 伪元素动画

**基本写法：伪元素过渡**
`<选择器>::before { transition: <属性> <时长>; }`
```css
/* 伪元素过渡动画 */
.button::before {
  transition: transform 0.3s;
}
.button:hover::before {
  transform: scaleX(1);
}
```

---

**基本写法：伪元素动画**
`<选择器>::after { animation: <名称> <时长>; }`
```css
/* 伪元素动画 */
.loader::after {
  animation: spin 1s linear infinite;
}
```

---

## 伪元素布局

**基本写法：clearfix 清除浮动**
`.clearfix::after { content: ""; display: table; clear: both; }`
```css
/* 清除浮动 */
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

---

**基本写法：tooltip 工具提示**
`<选择器>::after { content: attr(data-tooltip); <样式> }`
```css
/* 使用伪元素创建工具提示 */
[data-tooltip]::after {
  content: attr(data-tooltip);
  position: absolute;
  background: black;
  color: white;
  padding: 4px 8px;
  opacity: 0;
  transition: opacity 0.3s;
}
[data-tooltip]:hover::after {
  opacity: 1;
}
```

---

**基本写法：下划线动画**
`<选择器>::after { content: ""; <样式> }`
```css
/* 悬停下划线动画 */
.link::after {
  content: "";
  display: block;
  width: 0;
  height: 2px;
  background: currentColor;
  transition: width 0.3s;
}
.link:hover::after {
  width: 100%;
}
```



<!-- ============ 文档分隔线：007-css/011-ResponsiveDesign.md ============ -->

# CSS 响应式设计

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## viewport 视口设置

**基本写法：viewport 基础**
`<meta name="viewport" content="width=device-width, initial-scale=1">`
```css
/* HTML 中设置视口元信息 */
```

---

**基本写法：viewport 禁止缩放**
`<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">`
```css
/* 禁止用户缩放 */
```

---

## 媒体查询基础

**基本写法：max-width 最大宽度**
`@media (max-width: <值>) { <样式> }`
```css
/* 屏幕宽度小于等于指定值时应用 */
@media (max-width: 768px) {
  .container {
    padding: 10px;
  }
}
```

---

**基本写法：min-width 最小宽度**
`@media (min-width: <值>) { <样式> }`
```css
/* 屏幕宽度大于等于指定值时应用 */
@media (min-width: 1200px) {
  .container {
    max-width: 1200px;
  }
}
```

---

**基本写法：范围媒体查询**
`@media (min-width: <值>) and (max-width: <值>) { <样式> }`
```css
/* 屏幕宽度在指定范围内时应用 */
@media (min-width: 768px) and (max-width: 1024px) {
  .container {
    width: 750px;
  }
}
```

---

**基本写法：max-height 最大高度**
`@media (max-height: <值>) { <样式> }`
```css
/* 屏幕高度小于等于指定值时应用 */
@media (max-height: 500px) {
  .header {
    height: 40px;
  }
}
```

---

**基本写法：orientation 横屏**
`@media (orientation: landscape) { <样式> }`
```css
/* 横屏时应用 */
@media (orientation: landscape) {
  .layout {
    flex-direction: row;
  }
}
```

---

**基本写法：orientation 竖屏**
`@media (orientation: portrait) { <样式> }`
```css
/* 竖屏时应用 */
@media (orientation: portrait) {
  .layout {
    flex-direction: column;
  }
}
```

---

## 媒体特性

**基本写法：prefers-color-scheme 暗色**
`@media (prefers-color-scheme: dark) { <样式> }`
```css
/* 用户偏好暗色主题 */
@media (prefers-color-scheme: dark) {
  body {
    background-color: #1a1a1a;
    color: #ffffff;
  }
}
```

---

**基本写法：prefers-color-scheme 亮色**
`@media (prefers-color-scheme: light) { <样式> }`
```css
/* 用户偏好亮色主题 */
@media (prefers-color-scheme: light) {
  body {
    background-color: #ffffff;
    color: #333333;
  }
}
```

---

**基本写法：prefers-reduced-motion 减少动画**
`@media (prefers-reduced-motion: reduce) { <样式> }`
```css
/* 用户偏好减少动画 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

**基本写法：prefers-contrast 高对比度**
`@media (prefers-contrast: more) { <样式> }`
```css
/* 用户偏好高对比度 */
@media (prefers-contrast: more) {
  .text {
    color: black;
    background: white;
  }
}
```

---

**基本写法：hover 悬停支持**
`@media (hover: hover) { <样式> }`
```css
/* 设备支持悬停时应用 */
@media (hover: hover) {
  .button:hover {
    background-color: #0056b3;
  }
}
```

---

**基本写法：pointer 精确指针**
`@media (pointer: fine) { <样式> }`
```css
/* 设备有精确指针（鼠标）时应用 */
@media (pointer: fine) {
  .tooltip {
    display: block;
  }
}
```

---

**基本写法：pointer 粗略指针**
`@media (pointer: coarse) { <样式> }`
```css
/* 设备为粗略指针（触摸）时应用 */
@media (pointer: coarse) {
  .button {
    padding: 12px 24px;
  }
}
```

---

## 断点系统

**基本写法：移动优先断点**
`@media (min-width: <值>) { <样式> }`
```css
/* 移动优先：从小到大递增 */
.container {
  width: 100%;
}
@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
}
```

---

**基本写法：桌面优先断点**
`@media (max-width: <值>) { <样式> }`
```css
/* 桌面优先：从大到小递减 */
.container {
  max-width: 1200px;
}
@media (max-width: 768px) {
  .container {
    max-width: 100%;
  }
}
```

---

**单行写法：多断点**
`@media (min-width: <值1>) { <样式> } @media (min-width: <值2>) { <样式> }`
```css
/* 单行定义多个断点 */
.col { width: 100%; }
@media (min-width: 768px) { .col { width: 50%; } }
@media (min-width: 1200px) { .col { width: 33.33%; } }
```

---

**换行写法：多断点**
`@media (min-width: <值>) { <样式> }`
```css
/* 换行定义多个断点 */
.col {
  width: 100%;
}

@media (min-width: 768px) {
  .col {
    width: 50%;
  }
}

@media (min-width: 1200px) {
  .col {
    width: 33.33%;
  }
}
```

---

## 响应式单位

**基本写法：vw 视口宽度单位**
`width: <vw值>;`
```css
/* 相对于视口宽度的尺寸 */
.hero {
  width: 50vw;
}
```

---

**基本写法：vh 视口高度单位**
`height: <vh值>;`
```css
/* 相对于视口高度的尺寸 */
.hero {
  height: 100vh;
}
```

---

**基本写法：vmin 最小视口**
`width: <vmin值>;`
```css
/* 相对于视口较小边的尺寸 */
.logo {
  width: 10vmin;
}
```

---

**基本写法：vmax 最大视口**
`width: <vmax值>;`
```css
/* 相对于视口较大边的尺寸 */
.logo {
  width: 10vmax;
}
```

---

**基本写法：rem 根字号单位**
`font-size: <rem值>;`
```css
/* 相对于根元素字号的尺寸 */
.text {
  font-size: 1.2rem;
}
```

---

**基本写法：em 相对字号单位**
`padding: <em值>;`
```css
/* 相对于父元素字号的尺寸 */
.box {
  font-size: 16px;
  padding: 1.5em;
}
```

---

## 响应式字体

**基本写法：clamp 响应式字号**
`font-size: clamp(<最小>, <理想>, <最大>);`
```css
/* 字号在区间内响应式变化 */
.title {
  font-size: clamp(1.5rem, 4vw, 3rem);
}
```

---

**基本写法：vw 字号**
`font-size: <vw值>;`
```css
/* 视口宽度相关字号 */
.title {
  font-size: 5vw;
}
```

---

**基本写法：calc 混合计算字号**
`font-size: calc(<值1> + <值2>);`
```css
/* 混合单位计算字号 */
.title {
  font-size: calc(16px + 2vw);
}
```

---

## 响应式图片

**基本写法：max-width 图片自适应**
`img { max-width: 100%; height: auto; }`
```css
/* 图片自适应容器宽度 */
img {
  max-width: 100%;
  height: auto;
}
```

---

**基本写法：object-fit 图片裁剪**
`object-fit: cover;`
```css
/* 图片填充容器并裁剪 */
.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

---

**基本写法：picture 响应式图片**
`<picture> <source media="(<条件>)" srcset="<图片>"> <img src="<默认>"> </picture>`
```css
/* 根据屏幕加载不同图片 */
```

---

**基本写法：srcset 响应式图片**
`<img srcset="<图片1> <宽度1>, <图片2> <宽度2>" src="<默认>">`
```css
/* 根据屏幕密度加载不同图片 */
```

---

## 容器查询

**基本写法：container-type 容器**
`container-type: inline-size;`
```css
/* 定义容器查询上下文 */
.sidebar {
  container-type: inline-size;
}
```

---

**基本写法：container-name 命名容器**
`container-name: <名称>;`
```css
/* 命名容器 */
.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}
```

---

**基本写法：@container 容器查询**
`@container <名称> (min-width: <值>) { <样式> }`
```css
/* 基于容器尺寸应用样式 */
@container sidebar (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```

---

**基本写法：container 简写**
`container: <名称> / inline-size;`
```css
/* 同时设置容器名称和类型 */
.sidebar {
  container: sidebar / inline-size;
}
```

---

## CSS 嵌套媒体查询

**基本写法：嵌套媒体查询**
`<选择器> { @media <条件> { <样式> } }`
```css
/* CSS 原生嵌套媒体查询 */
.container {
  width: 100%;
  @media (min-width: 768px) {
    max-width: 720px;
  }
}
```

---

**单行写法：嵌套多媒体查询**
`<选择器> { @media <条件1> { <样式> } @media <条件2> { <样式> } }`
```css
/* 单行嵌套多个媒体查询 */
.col { width: 100%; @media (min-width: 768px) { width: 50%; } @media (min-width: 1200px) { width: 33%; } }
```

---

**换行写法：嵌套多媒体查询**
`<选择器> { @media <条件1> { <样式> } @media <条件2> { <样式> } }`
```css
/* 换行嵌套多个媒体查询 */
.col {
  width: 100%;
  @media (min-width: 768px) {
    width: 50%;
  }
  @media (min-width: 1200px) {
    width: 33%;
  }
}
```

---

## 响应式工具

**基本写法：min 取最小值**
`width: min(<值1>, <值2>);`
```css
/* 取两个值中的较小者 */
.container {
  width: min(100%, 1200px);
}
```

---

**基本写法：max 取最大值**
`font-size: max(<值1>, <值2>);`
```css
/* 取两个值中的较大者 */
.text {
  font-size: max(16px, 2vw);
}
```

---

**基本写法：clamp 区间值**
`width: clamp(<最小>, <理想>, <最大>);`
```css
/* 限制值在指定区间 */
.text {
  font-size: clamp(14px, 2vw, 24px);
}
```

---

**基本写法：calc 计算**
`width: calc(<表达式>);`
```css
/* 动态计算尺寸 */
.sidebar {
  width: calc(100% - 250px);
}
```

---

## 响应式布局模式

**基本写法：移动优先 Flex**
`display: flex; flex-direction: column; @media (min-width: <值>) { flex-direction: row; }`
```css
/* 移动优先的 Flex 布局 */
.layout {
  display: flex;
  flex-direction: column;
  @media (min-width: 768px) {
    flex-direction: row;
  }
}
```

---

**基本写法：响应式 Grid**
`display: grid; grid-template-columns: 1fr; @media (min-width: <值>) { grid-template-columns: repeat(2, 1fr); }`
```css
/* 响应式 Grid 布局 */
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

---

**基本写法：自动适应 Grid**
`grid-template-columns: repeat(auto-fit, minmax(<值>, 1fr));`
```css
/* 自动适应屏幕的 Grid */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

---

**基本写法：隐藏显示元素**
`display: none; @media (min-width: <值>) { display: block; }`
```css
/* 小屏隐藏，大屏显示 */
.sidebar {
  display: none;
  @media (min-width: 1024px) {
    display: block;
  }
}
```

---

## 现代响应式新特性

**基本写法：Container Queries 容器查询(@container)**
`@container <名称> [(<条件>)] { <样式> }`
```css
/* 基于父容器尺寸响应样式 */
.sidebar {
  container-type: inline-size;
  container-name: sidebar;
}
@container sidebar (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}
```

---

**基本写法：Container Query Units(cqw/cqh/cqi)**
`width: <数值>cqi;`
```css
/* 容器查询单位:1cqi = 容器 inline 尺寸 1% */
.card {
  /* 字号基于容器宽度自适应 */
  font-size: clamp(1rem, 5cqi, 2rem);
  padding: 2cqi;
}
```

---

**基本写法：Prefers-reduced-transparency**
`@media (prefers-reduced-transparency: reduce) { <样式> }`
```css
/* 用户偏好减少透明效果 */
@media (prefers-reduced-transparency: reduce) {
  .glass {
    background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: none;
  }
}
```

---

**基本写法：Prefers-reduced-data**
`@media (prefers-reduced-data: reduce) { <样式> }`
```css
/* 用户偏好节省流量 */
@media (prefers-reduced-data: reduce) {
  .hero {
    background-image: none;
    background-color: #007bff;
  }
}
```

---

**基本写法：@media (scripting: none)**
`@media (scripting: none) { <样式> }`
```css
/* 检测脚本是否可用 */
@media (scripting: none) {
  /* 无 JS 时显示备用内容 */
  .no-js-fallback {
    display: block;
  }
  .js-only {
    display: none;
  }
}
```



<!-- ============ 文档分隔线：007-css/012-CSS3SelectorSystem.md ============ -->

# CSS 选择器系统

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础选择器

**基本写法：元素选择器**
`<标签名> { <样式声明> }`
```css
/* 选中所有 div 元素 */
div {
  display: block;
}
```

---

**基本写法：类选择器**
`.<类名> { <样式声明> }`
```css
/* 选中所有带 container 类的元素 */
.container {
  width: 100%;
}
```

---

**基本写法：ID 选择器**
`#<ID名> { <样式声明> }`
```css
/* 选中 id 为 header 的元素 */
#header {
  position: sticky;
}
```

---

**基本写法：通配选择器**
`* { <样式声明> }`
```css
/* 选中所有元素 */
* {
  margin: 0;
  padding: 0;
}
```

---

**基本写法：属性选择器存在**
`[<属性名>] { <样式声明> }`
```css
/* 选中所有带 disabled 属性的元素 */
[disabled] {
  opacity: 0.5;
}
```

---

**基本写法：属性选择器精确匹配**
`[<属性名>="<值>"] { <样式声明> }`
```css
/* 选中 type 为 text 的 input */
[type="text"] {
  border: 1px solid #ccc;
}
```

---

**基本写法：属性选择器包含单词**
`[<属性名>~="<值>"] { <样式声明> }`
```css
/* 选中 class 包含 active 单词的元素 */
[class~="active"] {
  color: red;
}
```

---

**基本写法：属性选择器前缀匹配**
`[<属性名>^="<值>"] { <样式声明> }`
```css
/* 选中 href 以 https 开头的 a */
[href^="https"] {
  color: green;
}
```

---

**基本写法：属性选择器后缀匹配**
`[<属性名>$="<值>"] { <样式声明> }`
```css
/* 选中 href 以 .pdf 结尾的 a */
[href$=".pdf"] {
  color: red;
}
```

---

**基本写法：属性选择器包含子串**
`[<属性名>*="<值>"] { <样式声明> }`
```css
/* 选中 src 包含 avatar 的 img */
[src*="avatar"] {
  border-radius: 50%;
}
```

---

## 组合选择器

**基本写法：后代选择器**
`<父选择器> <子选择器> { <样式声明> }`
```css
/* 选中 nav 内的所有 a 元素 */
nav a {
  text-decoration: none;
}
```

---

**基本写法：子代选择器**
`<父选择器> > <子选择器> { <样式声明> }`
```css
/* 选中 ul 的直接子元素 li */
ul > li {
  list-style: none;
}
```

---

**基本写法：相邻兄弟选择器**
`<前选择器> + <后选择器> { <样式声明> }`
```css
/* 选中 h1 后紧邻的 p */
h1 + p {
  margin-top: 0;
}
```

---

**基本写法：通用兄弟选择器**
`<前选择器> ~ <后选择器> { <样式声明> }`
```css
/* 选中 h1 后所有的同级 p */
h1 ~ p {
  color: gray;
}
```

---

**单行写法：多选择器分组**
`<选择器1>, <选择器2> { <样式声明> }`
```css
/* 单行同时选中 h1 和 h2 */
h1, h2 {
  font-weight: bold;
}
```

---

**换行写法：多选择器分组**
`<选择器1>, <选择器2>, <选择器3> { <样式声明> }`
```css
/* 换行同时选中多个标题 */
h1,
h2,
h3,
h4 {
  font-family: sans-serif;
}
```

---

## 伪类选择器

**基本写法：hover 悬停**
`<选择器>:hover { <样式声明> }`
```css
/* 鼠标悬停时变色 */
.button:hover {
  background-color: #0056b3;
}
```

---

**基本写法：focus 聚焦**
`<选择器>:focus { <样式声明> }`
```css
/* 输入框聚焦时高亮 */
input:focus {
  border-color: #007bff;
}
```

---

**基本写法：active 激活**
`<选择器>:active { <样式声明> }`
```css
/* 按钮按下时缩小 */
.button:active {
  transform: scale(0.95);
}
```

---

**基本写法：first-child 首个子元素**
`<选择器>:first-child { <样式声明> }`
```css
/* 选中父元素的第一个子元素 */
li:first-child {
  font-weight: bold;
}
```

---

**基本写法：last-child 末尾子元素**
`<选择器>:last-child { <样式声明> }`
```css
/* 选中父元素的最后一个子元素 */
li:last-child {
  border-bottom: none;
}
```

---

**基本写法：nth-child 索引选择**
`<选择器>:nth-child(<n>) { <样式声明> }`
```css
/* 选中第 3 个子元素 */
li:nth-child(3) {
  color: red;
}
```

---

**基本写法：nth-child 奇数**
`<选择器>:nth-child(odd) { <样式声明> }`
```css
/* 选中所有奇数行 */
tr:nth-child(odd) {
  background-color: #f9f9f9;
}
```

---

**基本写法：nth-child 偶数**
`<选择器>:nth-child(even) { <样式声明> }`
```css
/* 选中所有偶数行 */
tr:nth-child(even) {
  background-color: #ffffff;
}
```

---

**基本写法：nth-child 公式**
`<选择器>:nth-child(<公式>) { <样式声明> }`
```css
/* 每隔 3 个元素选中一次 */
li:nth-child(3n+1) {
  color: blue;
}
```

---

**基本写法：not 否定伪类**
`<选择器>:not(<排除选择器>) { <样式声明> }`
```css
/* 选中所有非 disabled 的 input */
input:not([disabled]) {
  border: 1px solid #ccc;
}
```

---

**基本写法：checked 选中状态**
`<选择器>:checked { <样式声明> }`
```css
/* 选中被勾选的复选框 */
input:checked {
  accent-color: #007bff;
}
```

---

**基本写法：disabled 禁用状态**
`<选择器>:disabled { <样式声明> }`
```css
/* 选中被禁用的表单元素 */
input:disabled {
  background-color: #f5f5f5;
}
```

---

## 伪元素选择器

**基本写法：before 前置内容**
`<选择器>::before { content: <内容>; <样式声明> }`
```css
/* 在元素前插入内容 */
.quote::before {
  content: '"';
  color: gray;
}
```

---

**基本写法：after 后置内容**
`<选择器>::after { content: <内容>; <样式声明> }`
```css
/* 在元素后插入内容 */
.quote::after {
  content: '"';
  color: gray;
}
```

---

**基本写法：first-letter 首字母**
`<选择器>::first-letter { <样式声明> }`
```css
/* 选中段落首字母 */
p::first-letter {
  font-size: 2em;
  font-weight: bold;
}
```

---

**基本写法：first-line 首行**
`<选择器>::first-line { <样式声明> }`
```css
/* 选中段落首行 */
p::first-line {
  text-transform: uppercase;
}
```

---

**基本写法：selection 选中文本**
`<选择器>::selection { <样式声明> }`
```css
/* 自定义文本选中样式 */
::selection {
  background-color: #007bff;
  color: white;
}
```

---

**基本写法：placeholder 占位符**
`<选择器>::placeholder { <样式声明> }`
```css
/* 自定义输入框占位符样式 */
input::placeholder {
  color: #999;
}
```

---

## 结构伪类

**基本写法：first-of-type 同类型首个**
`<选择器>:first-of-type { <样式声明> }`
```css
/* 选中同级同类型的第一个元素 */
p:first-of-type {
  margin-top: 0;
}
```

---

**基本写法：last-of-type 同类型末尾**
`<选择器>:last-of-type { <样式声明> }`
```css
/* 选中同级同类型的最后一个元素 */
p:last-of-type {
  margin-bottom: 0;
}
```

---

**基本写法：nth-of-type 索引选择**
`<选择器>:nth-of-type(<n>) { <样式声明> }`
```css
/* 选中第 2 个 p 元素 */
p:nth-of-type(2) {
  color: blue;
}
```

---

**基本写法：only-child 唯一子元素**
`<选择器>:only-child { <样式声明> }`
```css
/* 选中父元素中唯一的子元素 */
div:only-child {
  border: 1px solid red;
}
```

---

**基本写法：empty 空元素**
`<选择器>:empty { <样式声明> }`
```css
/* 选中没有子元素的元素 */
div:empty {
  display: none;
}
```

---

## 表单伪类

**基本写法：required 必填字段**
`<选择器>:required { <样式声明> }`
```css
/* 标记必填字段 */
input:required {
  border-color: red;
}
```

---

**基本写法：valid 有效状态**
`<选择器>:valid { <样式声明> }`
```css
/* 表单验证通过时样式 */
input:valid {
  border-color: green;
}
```

---

**基本写法：invalid 无效状态**
`<选择器>:invalid { <样式声明> }`
```css
/* 表单验证失败时样式 */
input:invalid {
  border-color: red;
}
```

---

## 关系选择器

**基本写法：has 父选择器**
`<选择器>:has(<子选择器>) { <样式声明> }`
```css
/* 选中包含 img 的 div */
div:has(img) {
  padding: 10px;
}
```

---

**基本写法：is 匹配任一**
`:is(<选择器1>, <选择器2>) { <样式声明> }`
```css
/* 匹配多个选择器中的任一个 */
:is(h1, h2, h3) {
  font-family: sans-serif;
}
```

---

**基本写法：where 匹配任一**
`:where(<选择器1>, <选择器2>) { <样式声明> }`
```css
/* 匹配多个选择器（零特异性） */
:where(.card, .panel) {
  padding: 1rem;
}
```

---

## 目标伪类

**基本写法：target 锚点目标**
`<选择器>:target { <样式声明> }`
```css
/* 选中当前锚点指向的元素 */
#section:target {
  background-color: #ffffcc;
}
```

---

**基本写法：root 根元素**
`:root { <样式声明> }`
```css
/* 选中文档根元素 html */
:root {
  --primary-color: #007bff;
}
```

---

## 嵌套选择器 (CSS Nesting)

**基本写法：嵌套选择器**
`<父选择器> { & <子选择器> { <样式声明> } }`
```css
/* CSS 原生嵌套语法 */
.card {
  padding: 1rem;
  & h2 {
    color: blue;
  }
}
```

---

**基本写法：嵌套伪类**
`<选择器> { &:<伪类> { <样式声明> } }`
```css
/* 嵌套伪类选择器 */
.button {
  background: blue;
  &:hover {
    background: darkblue;
  }
}
```

---

**基本写法：嵌套媒体查询**
`<选择器> { @media <条件> { <样式声明> } }`
```css
/* 嵌套媒体查询 */
.container {
  width: 100%;
  @media (min-width: 768px) {
    width: 750px;
  }
}
```

---

## CSS Nesting 原生嵌套(2023-2024)

**基本写法：原生嵌套基本语法(& 嵌套)**
`<父选择器> { & <子选择器> { <样式声明> } }`
```css
/* 原生 CSS 嵌套,无需预处理器 */
.card {
  padding: 1rem;
  & .title {
    font-size: 1.5rem;
  }
  & .body {
    color: #333;
  }
}
```

---

**基本写法：嵌套与组合器**
`<选择器> { &<组合器><目标> { <样式声明> } }`
```css
/* 嵌套中直接使用组合器 */
.nav {
  & > li {
    list-style: none;
  }
  & + .sidebar {
    margin-left: 20px;
  }
  & ~ .footer {
    border-top: 1px solid #ccc;
  }
}
```

---

**基本写法：嵌套中的层叠层级**
`<选择器> { & { <样式声明> } }`
```css
/* 显式 & 表示父选择器,影响层叠特异性 */
.button {
  background: blue;
  & {
    /* 等价于 .button 特异性 */
    color: white;
  }
  &:hover {
    /* 等价于 .button:hover */
    background: darkblue;
  }
}
```

---

**基本写法：@scope 作用域选择器(2024)**
`@scope (<根选择器>) to (<下限选择器>) { <样式声明> }`
```css
/* @scope 限定样式作用范围 */
@scope (.article) to (.comment) {
  /* 仅作用于 .article 内、.comment 之外的内容 */
  p {
    line-height: 1.6;
  }
  img {
    max-width: 100%;
  }
}
```

---

**基本写法：@scope 邻近选择器**
`@scope (<条件选择器>) { <样式声明> }`
```css
/* @scope 结合 :has 实现条件作用域 */
@scope (.card:has(img)) {
  /* 仅当 .card 内含图片时应用 */
  .content {
    padding-top: 0;
  }
}
```



<!-- ============ 文档分隔线：007-css/013-Shadow.md ============ -->

# CSS 阴影

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## box-shadow 盒阴影

**基本写法：外阴影**
`box-shadow: <水平偏移> <垂直偏移> <模糊> <颜色>;`
```css
/* 设置外阴影 */
.box {
  box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：带扩展的外阴影**
`box-shadow: <水平> <垂直> <模糊> <扩展> <颜色>;`
```css
/* 设置带扩展的外阴影 */
.box {
  box-shadow: 2px 4px 8px 2px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：内阴影**
`box-shadow: inset <水平> <垂直> <模糊> <颜色>;`
```css
/* 设置内阴影 */
.box {
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}
```

---

**基本写法：无阴影**
`box-shadow: none;`
```css
/* 移除阴影 */
.box {
  box-shadow: none;
}
```

---

**单行写法：多重阴影**
`box-shadow: <阴影1>, <阴影2>;`
```css
/* 单行设置多重阴影 */
.box {
  box-shadow: 0 2px 4px rgba(0,0,0,0.2), 0 4px 8px rgba(0,0,0,0.1);
}
```

---

**换行写法：多重阴影**
`box-shadow: <阴影1>, <阴影2>, <阴影3>;`
```css
/* 换行设置多重阴影 */
.box {
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.1),
    0 4px 8px rgba(0, 0, 0, 0.1),
    0 16px 32px rgba(0, 0, 0, 0.1);
}
```

---

## 常见阴影效果

**基本写法：柔和阴影**
`box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);`
```css
/* 柔和的卡片阴影 */
.card {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：深阴影**
`box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);`
```css
/* 较深的阴影 */
.modal {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}
```

---

**基本写法：底部阴影**
`box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);`
```css
/* 仅底部阴影 */
.header {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：四周阴影**
`box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);`
```css
/* 四周均匀阴影 */
.box {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：彩色阴影**
`box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);`
```css
/* 彩色阴影效果 */
.button {
  box-shadow: 0 4px 12px rgba(0, 123, 255, 0.3);
}
```

---

## 材料设计阴影

**基本写法：Material 阴影 1 级**
`box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);`
```css
/* Material Design 1 级阴影 */
.z1 {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
```

---

**基本写法：Material 阴影 2 级**
`box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);`
```css
/* Material Design 2 级阴影 */
.z2 {
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
}
```

---

**基本写法：Material 阴影 3 级**
`box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);`
```css
/* Material Design 3 级阴影 */
.z3 {
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}
```

---

**基本写法：Material 阴影 4 级**
`box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);`
```css
/* Material Design 4 级阴影 */
.z4 {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}
```

---

**基本写法：Material 阴影 5 级**
`box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);`
```css
/* Material Design 5 级阴影 */
.z5 {
  box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
}
```

---

## text-shadow 文字阴影

**基本写法：文字阴影**
`text-shadow: <水平> <垂直> <模糊> <颜色>;`
```css
/* 设置文字阴影 */
.title {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
```

---

**基本写法：文字发光**
`text-shadow: 0 0 10px <颜色>;`
```css
/* 文字发光效果 */
.glow {
  text-shadow: 0 0 10px rgba(0, 123, 255, 0.8);
}
```

---

**基本写法：文字描边**
`text-shadow: <方向1> <颜色>, <方向2> <颜色>, <方向3> <颜色>, <方向4> <颜色>;`
```css
/* 文字描边效果 */
.outline {
  text-shadow:
    -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000;
}
```

---

**单行写法：多重文字阴影**
`text-shadow: <阴影1>, <阴影2>;`
```css
/* 单行设置多重文字阴影 */
.text {
  text-shadow: 1px 1px 2px black, 0 0 10px blue;
}
```

---

**换行写法：多重文字阴影**
`text-shadow: <阴影1>, <阴影2>, <阴影3>;`
```css
/* 换行设置多重文字阴影 */
.text {
  text-shadow:
    1px 1px 2px black,
    0 0 10px blue,
    0 0 20px darkblue;
}
```

---

## drop-shadow 滤镜阴影

**基本写法：drop-shadow 滤镜**
`filter: drop-shadow(<水平> <垂直> <模糊> <颜色>);`
```css
/* 使用滤镜创建阴影（跟随形状） */
.image {
  filter: drop-shadow(2px 4px 8px rgba(0, 0, 0, 0.3));
}
```

---

**基本写法：PNG 阴影**
`filter: drop-shadow(<水平> <垂直> <模糊> <颜色>);`
```css
/* 为透明 PNG 创建跟随形状的阴影 */
.logo {
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.3));
}
```

---

## 阴影动画

**基本写法：阴影过渡**
`transition: box-shadow <时长>;`
```css
/* 阴影过渡动画 */
.card {
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：阴影悬停效果**
`<选择器>:hover { box-shadow: <阴影>; }`
```css
/* 悬停时增强阴影 */
.button {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}
.button:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
```

---

**基本写法：阴影按下效果**
`<选择器>:active { box-shadow: <阴影>; }`
```css
/* 按下时减弱阴影 */
.button:active {
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}
```

---

## 阴影变量

**基本写法：定义阴影变量**
`:root { --shadow-<名>: <阴影值>; }`
```css
/* 定义阴影变量 */
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：使用阴影变量**
`box-shadow: var(--shadow-<名>);`
```css
/* 使用阴影变量 */
.card {
  box-shadow: var(--shadow-md);
}
```

---

## 响应式阴影

**基本写法：clamp 响应式阴影**
`box-shadow: 0 clamp(<最小>, <理想>, <最大>) <模糊> <颜色>;`
```css
/* 响应式阴影 */
.box {
  box-shadow: 0 clamp(2px, 1vw, 8px) 12px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：媒体查询调整阴影**
`@media (max-width: <值>) { box-shadow: <值>; }`
```css
/* 小屏幕调整阴影 */
.card {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
@media (max-width: 768px) {
  .card {
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }
}
```

---

## 内阴影效果

**基本写法：内凹效果**
`box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);`
```css
/* 创建内凹效果 */
.inset {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：内凸效果**
`box-shadow: inset 0 -2px 4px rgba(0, 0, 0, 0.1);`
```css
/* 创建内凸效果 */
.outset {
  box-shadow: inset 0 -2px 4px rgba(0, 0, 0, 0.1);
}
```

---

**基本写法：浮雕效果**
`box-shadow: inset 1px 1px 2px rgba(255,255,255,0.5), inset -1px -1px 2px rgba(0,0,0,0.1);`
```css
/* 创建浮雕效果 */
.embossed {
  box-shadow:
    inset 1px 1px 2px rgba(255,255,255,0.5),
    inset -1px -1px 2px rgba(0,0,0,0.1);
}
```

---

## 长阴影

**单行写法：长阴影**
`box-shadow: <偏移1> <颜色>, <偏移2> <颜色>, <偏移3> <颜色>;`
```css
/* 单行长阴影效果 */
.long-shadow {
  box-shadow: 1px 1px rgba(0,0,0,0.1), 2px 2px rgba(0,0,0,0.1), 3px 3px rgba(0,0,0,0.1);
}
```

---

**换行写法：长阴影**
`box-shadow: <偏移1> <颜色>, <偏移2> <颜色>, <偏移3> <颜色>;`
```css
/* 换行长阴影效果 */
.long-shadow {
  box-shadow:
    1px 1px rgba(0,0,0,0.1),
    2px 2px rgba(0,0,0,0.1),
    3px 3px rgba(0,0,0,0.1),
    4px 4px rgba(0,0,0,0.1),
    5px 5px rgba(0,0,0,0.1);
}
```

---

## 霓虹阴影

**基本写法：霓虹发光**
`box-shadow: 0 0 <模糊> <颜色>, 0 0 <模糊2> <颜色>;`
```css
/* 霓虹发光效果 */
.neon {
  box-shadow: 0 0 5px #007bff, 0 0 10px #007bff;
}
```

---

**基本写法：彩色霓虹**
`box-shadow: 0 0 <模糊> <颜色1>, 0 0 <模糊2> <颜色2>;`
```css
/* 多色霓虹效果 */
.neon-multi {
  box-shadow:
    0 0 5px #ff00ff,
    0 0 10px #00ffff;
}
```



<!-- ============ 文档分隔线：007-css/014-CSSVariableCustomAttribute.md ============ -->

# CSS 变量与自定义属性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量定义

**基本写法：定义全局变量**
`:root { --<变量名>: <值>; }`
```css
/* 在根元素定义全局变量 */
:root {
  --primary-color: #007bff;
}
```

---

**基本写法：定义局部变量**
`<选择器> { --<变量名>: <值>; }`
```css
/* 在特定元素定义局部变量 */
.card {
  --card-padding: 20px;
}
```

---

**基本写法：定义颜色变量**
`--<变量名>: <颜色值>;`
```css
/* 定义颜色变量 */
:root {
  --text-color: #333333;
  --bg-color: #ffffff;
}
```

---

**基本写法：定义尺寸变量**
`--<变量名>: <长度值>;`
```css
/* 定义尺寸变量 */
:root {
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
}
```

---

**基本写法：定义字号变量**
`--<变量名>: <字号值>;`
```css
/* 定义字号变量 */
:root {
  --font-size-base: 16px;
  --font-size-lg: 1.25rem;
}
```

---

**基本写法：定义字体变量**
`--<变量名>: <字体栈>;`
```css
/* 定义字体变量 */
:root {
  --font-family-sans: "Helvetica Neue", sans-serif;
  --font-family-mono: "Fira Code", monospace;
}
```

---

**基本写法：定义动画变量**
`--<变量名>: <动画值>;`
```css
/* 定义动画变量 */
:root {
  --transition-fast: 0.2s ease-in-out;
  --transition-slow: 0.5s ease;
}
```

---

## 变量使用

**基本写法：使用变量**
`<属性>: var(--<变量名>);`
```css
/* 使用自定义变量 */
.button {
  background-color: var(--primary-color);
  padding: var(--spacing-md);
}
```

---

**基本写法：变量带默认值**
`<属性>: var(--<变量名>, <默认值>);`
```css
/* 变量未定义时使用默认值 */
.box {
  padding: var(--custom-padding, 10px);
}
```

---

**基本写法：变量嵌套使用**
`--<变量名>: var(--<其他变量>);`
```css
/* 变量引用其他变量 */
:root {
  --base-spacing: 10px;
  --double-spacing: calc(var(--base-spacing) * 2);
}
```

---

**基本写法：变量在 calc 中使用**
`<属性>: calc(<表达式> var(--<变量名>));`
```css
/* 在 calc 中使用变量 */
.box {
  width: calc(100% - var(--sidebar-width));
  margin: calc(var(--spacing-md) * 2);
}
```

---

**基本写法：变量在渐变中使用**
`background: linear-gradient(<方向>, var(--<颜色1>), var(--<颜色2>));`
```css
/* 在渐变中使用变量 */
.header {
  background: linear-gradient(135deg, var(--color-start), var(--color-end));
}
```

---

**基本写法：变量在 transform 中使用**
`transform: translate(var(--<x>), var(--<y>));`
```css
/* 在 transform 中使用变量 */
.box {
  transform: translate(var(--offset-x), var(--offset-y));
}
```

---

## 变量作用域

**基本写法：全局变量**
`:root { --<变量名>: <值>; }`
```css
/* 全局作用域变量 */
:root {
  --global-color: #007bff;
}
```

---

**基本写法：局部变量覆盖**
`<选择器> { --<变量名>: <新值>; }`
```css
/* 局部覆盖全局变量 */
.dark-theme {
  --bg-color: #1a1a1a;
  --text-color: #ffffff;
}
```

---

**基本写法：组件级变量**
`.<组件类> { --<变量名>: <值>; }`
```css
/* 组件作用域变量 */
.card {
  --card-bg: white;
  --card-border: 1px solid #ccc;
  background: var(--card-bg);
  border: var(--card-border);
}
```

---

**基本写法：媒体查询中修改变量**
`@media <条件> { :root { --<变量名>: <新值>; } }`
```css
/* 响应式调整变量值 */
:root {
  --font-size: 16px;
}
@media (max-width: 768px) {
  :root {
    --font-size: 14px;
  }
}
```

---

## 主题切换

**基本写法：亮色主题变量**
`[data-theme="light"] { --<变量名>: <值>; }`
```css
/* 亮色主题变量定义 */
[data-theme="light"] {
  --bg-color: #ffffff;
  --text-color: #333333;
  --border-color: #cccccc;
}
```

---

**基本写法：暗色主题变量**
`[data-theme="dark"] { --<变量名>: <值>; }`
```css
/* 暗色主题变量定义 */
[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #ffffff;
  --border-color: #444444;
}
```

---

**基本写法：使用主题变量**
`<属性>: var(--<变量名>);`
```css
/* 应用主题变量 */
body {
  background-color: var(--bg-color);
  color: var(--text-color);
}
```

---

**基本写法：prefers-color-scheme 自动切换**
`@media (prefers-color-scheme: dark) { :root { --<变量名>: <值>; } }`
```css
/* 跟随系统主题自动切换 */
:root {
  --bg-color: #ffffff;
  --text-color: #333333;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg-color: #1a1a1a;
    --text-color: #ffffff;
  }
}
```

---

## 变量与 JavaScript

**基本写法：JavaScript 读取变量**
`getComputedStyle(<元素>).getPropertyValue('--<变量名>')`
```css
/* JavaScript 读取 CSS 变量 */
```

---

**基本写法：JavaScript 设置变量**
`<元素>.style.setProperty('--<变量名>', <值>)`
```css
/* JavaScript 设置 CSS 变量 */
```

---

## 变量继承

**基本写法：变量继承**
`<父选择器> { --<变量名>: <值>; } <子选择器> { <属性>: var(--<变量名>); }`
```css
/* 子元素继承父元素变量 */
.parent {
  --text-size: 18px;
}
.child {
  font-size: var(--text-size);
}
```

---

**基本写法：变量覆盖继承**
`<子选择器> { --<变量名>: <新值>; }`
```css
/* 子元素覆盖继承的变量 */
.parent {
  --text-size: 18px;
}
.child {
  --text-size: 24px;
  font-size: var(--text-size);
}
```

---

## 设计令牌系统

**单行写法：多颜色变量定义**
`:root { --color-<名1>: <值1>; --color-<名2>: <值2>; --color-<名3>: <值3>; }`
```css
/* 单行定义颜色令牌系统 */
:root { --color-primary: #007bff; --color-secondary: #6c757d; --color-success: #28a745; --color-danger: #dc3545; }
```

---

**换行写法：多颜色变量定义**
`:root { --color-<名>: <值>; }`
```css
/* 换行定义颜色令牌系统 */
:root {
  --color-primary: #007bff;
  --color-secondary: #6c757d;
  --color-success: #28a745;
  --color-danger: #dc3545;
  --color-warning: #ffc107;
  --color-info: #17a2b8;
}
```

---

**单行写法：多尺寸变量定义**
`:root { --size-<名1>: <值1>; --size-<名2>: <值2>; --size-<名3>: <值3>; }`
```css
/* 单行定义尺寸令牌系统 */
:root { --size-sm: 8px; --size-md: 16px; --size-lg: 24px; --size-xl: 32px; }
```

---

**换行写法：多尺寸变量定义**
`:root { --size-<名>: <值>; }`
```css
/* 换行定义尺寸令牌系统 */
:root {
  --size-xs: 4px;
  --size-sm: 8px;
  --size-md: 16px;
  --size-lg: 24px;
  --size-xl: 32px;
  --size-2xl: 48px;
}
```

---

**单行写法：多字号变量定义**
`:root { --font-size-<名1>: <值1>; --font-size-<名2>: <值2>; --font-size-<名3>: <值3>; }`
```css
/* 单行定义字号令牌系统 */
:root { --font-size-sm: 0.875rem; --font-size-base: 1rem; --font-size-lg: 1.25rem; --font-size-xl: 1.5rem; }
```

---

**换行写法：多字号变量定义**
`:root { --font-size-<名>: <值>; }`
```css
/* 换行定义字号令牌系统 */
:root {
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.25rem;
  --font-size-xl: 1.5rem;
  --font-size-2xl: 2rem;
  --font-size-3xl: 3rem;
}
```

---

## 变量类型与 @property

**基本写法：@property 定义类型**
`@property --<变量名> { syntax: "<类型>"; inherits: <布尔>; initial-value: <值>; }`
```css
/* 定义带类型的自定义属性 */
@property --angle {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
```

---

**基本写法：@property 颜色类型**
`@property --<变量名> { syntax: "<color>"; inherits: true; initial-value: <颜色>; }`
```css
/* 定义颜色类型自定义属性 */
@property --theme-color {
  syntax: "<color>";
  inherits: true;
  initial-value: #007bff;
}
```

---

**基本写法：@property 长度类型**
`@property --<变量名> { syntax: "<length>"; inherits: true; initial-value: <长度>; }`
```css
/* 定义长度类型自定义属性 */
@property --spacing {
  syntax: "<length>";
  inherits: true;
  initial-value: 16px;
}
```

---

**基本写法：@property 动画**
`@keyframes <名称> { from { --<变量名>: <值1>; } to { --<变量名>: <值2>; } }`
```css
/* 使用 @property 实现变量动画 */
@property --rotation {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}
@keyframes spin {
  from { --rotation: 0deg; }
  to { --rotation: 360deg; }
}
.spinner {
  animation: spin 1s linear infinite;
  transform: rotate(var(--rotation));
}
```

---

## 变量回退值

**基本写法：单层回退**
`<属性>: var(--<变量名>, <默认值>);`
```css
/* 变量未定义时使用默认值 */
.box {
  color: var(--text-color, #333333);
}
```

---

**基本写法：多层回退**
`<属性>: var(--<变量1>, var(--<变量2>, <默认值>));`
```css
/* 多层变量回退 */
.box {
  color: var(--custom-color, var(--theme-color), #333333);
}
```

---

## 变量与 calc 计算

**基本写法：变量乘法**
`<属性>: calc(var(--<变量>) * <系数>);`
```css
/* 变量乘法计算 */
.box {
  width: calc(var(--base-width) * 2);
}
```

---

**基本写法：变量加法**
`<属性>: calc(var(--<变量1>) + var(--<变量2>));`
```css
/* 变量加法计算 */
.box {
  padding: calc(var(--spacing-sm) + var(--spacing-md));
}
```

---

**基本写法：变量减法**
`<属性>: calc(var(--<变量1>) - var(--<变量2>));`
```css
/* 变量减法计算 */
.box {
  margin: calc(var(--container-width) - var(--content-width));
}
```

---

**基本写法：变量除法**
`<属性>: calc(var(--<变量>) / <系数>);`
```css
/* 变量除法计算 */
.box {
  width: calc(var(--full-width) / 3);
}
```



<!-- ============ 文档分隔线：007-css/015-CSS3FlexboxFlexLayout.md ============ -->

# CSS Flexbox 弹性布局

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 容器属性

**基本写法：flex 容器**
`display: flex;`
```css
/* 设置为弹性容器 */
.container {
  display: flex;
}
```

---

**基本写法：inline-flex 行内容器**
`display: inline-flex;`
```css
/* 设置为行内弹性容器 */
.badge {
  display: inline-flex;
}
```

---

**基本写法：flex-direction 行方向**
`flex-direction: row;`
```css
/* 主轴为水平方向 */
.container {
  flex-direction: row;
}
```

---

**基本写法：flex-direction 列方向**
`flex-direction: column;`
```css
/* 主轴为垂直方向 */
.container {
  flex-direction: column;
}
```

---

**基本写法：flex-direction 反向行**
`flex-direction: row-reverse;`
```css
/* 主轴为水平反向 */
.container {
  flex-direction: row-reverse;
}
```

---

**基本写法：flex-direction 反向列**
`flex-direction: column-reverse;`
```css
/* 主轴为垂直反向 */
.container {
  flex-direction: column-reverse;
}
```

---

**基本写法：flex-wrap 不换行**
`flex-wrap: nowrap;`
```css
/* 子元素不换行 */
.container {
  flex-wrap: nowrap;
}
```

---

**基本写法：flex-wrap 换行**
`flex-wrap: wrap;`
```css
/* 子元素自动换行 */
.container {
  flex-wrap: wrap;
}
```

---

**基本写法：flex-wrap 反向换行**
`flex-wrap: wrap-reverse;`
```css
/* 子元素反向换行 */
.container {
  flex-wrap: wrap-reverse;
}
```

---

**基本写法：flex-flow 简写**
`flex-flow: <方向> <换行>;`
```css
/* 同时设置方向和换行 */
.container {
  flex-flow: row wrap;
}
```

---

**基本写法：justify-content 主轴起始**
`justify-content: flex-start;`
```css
/* 主轴起始对齐 */
.container {
  justify-content: flex-start;
}
```

---

**基本写法：justify-content 主轴居中**
`justify-content: center;`
```css
/* 主轴居中对齐 */
.container {
  justify-content: center;
}
```

---

**基本写法：justify-content 主轴末尾**
`justify-content: flex-end;`
```css
/* 主轴末尾对齐 */
.container {
  justify-content: flex-end;
}
```

---

**基本写法：justify-content 两端对齐**
`justify-content: space-between;`
```css
/* 两端对齐，间距相等 */
.container {
  justify-content: space-between;
}
```

---

**基本写法：justify-content 均匀分布**
`justify-content: space-evenly;`
```css
/* 均匀分布，间距相同 */
.container {
  justify-content: space-evenly;
}
```

---

**基本写法：justify-content 环绕分布**
`justify-content: space-around;`
```css
/* 环绕分布，两端间距为中间一半 */
.container {
  justify-content: space-around;
}
```

---

**基本写法：align-items 交叉轴起始**
`align-items: flex-start;`
```css
/* 交叉轴起始对齐 */
.container {
  align-items: flex-start;
}
```

---

**基本写法：align-items 交叉轴居中**
`align-items: center;`
```css
/* 交叉轴居中对齐 */
.container {
  align-items: center;
}
```

---

**基本写法：align-items 交叉轴末尾**
`align-items: flex-end;`
```css
/* 交叉轴末尾对齐 */
.container {
  align-items: flex-end;
}
```

---

**基本写法：align-items 拉伸**
`align-items: stretch;`
```css
/* 子元素拉伸填满交叉轴 */
.container {
  align-items: stretch;
}
```

---

**基本写法：align-items 基线对齐**
`align-items: baseline;`
```css
/* 基线对齐 */
.container {
  align-items: baseline;
}
```

---

**基本写法：align-content 多行起始**
`align-content: flex-start;`
```css
/* 多行时交叉轴起始对齐 */
.container {
  flex-wrap: wrap;
  align-content: flex-start;
}
```

---

**基本写法：align-content 多行居中**
`align-content: center;`
```css
/* 多行时交叉轴居中对齐 */
.container {
  flex-wrap: wrap;
  align-content: center;
}
```

---

**基本写法：align-content 多行两端对齐**
`align-content: space-between;`
```css
/* 多行时两端对齐 */
.container {
  flex-wrap: wrap;
  align-content: space-between;
}
```

---

**基本写法：gap 间距**
`gap: <值>;`
```css
/* 设置子元素间距 */
.grid {
  display: flex;
  gap: 20px;
}
```

---

**基本写法：gap 双值**
`gap: <行间距> <列间距>;`
```css
/* 分别设置行列间距 */
.grid {
  gap: 20px 10px;
}
```

---

**基本写法：row-gap 行间距**
`row-gap: <值>;`
```css
/* 仅设置行间距 */
.grid {
  row-gap: 20px;
}
```

---

**基本写法：column-gap 列间距**
`column-gap: <值>;`
```css
/* 仅设置列间距 */
.grid {
  column-gap: 10px;
}
```

---

## 子元素属性

**基本写法：flex-grow 放大**
`flex-grow: <数值>;`
```css
/* 子元素放大比例 */
.item {
  flex-grow: 1;
}
```

---

**基本写法：flex-shrink 缩小**
`flex-shrink: <数值>;`
```css
/* 子元素缩小比例 */
.item {
  flex-shrink: 0;
}
```

---

**基本写法：flex-basis 基础尺寸**
`flex-basis: <长度>;`
```css
/* 子元素基础尺寸 */
.item {
  flex-basis: 200px;
}
```

---

**基本写法：flex-basis 百分比**
`flex-basis: <百分比>;`
```css
/* 基础尺寸为百分比 */
.item {
  flex-basis: 50%;
}
```

---

**基本写法：flex 简写**
`flex: <grow> <shrink> <basis>;`
```css
/* 同时设置三个属性 */
.item {
  flex: 1 1 0%;
}
```

---

**基本写法：flex auto**
`flex: auto;`
```css
/* 等价于 flex: 1 1 auto */
.item {
  flex: auto;
}
```

---

**基本写法：flex none**
`flex: none;`
```css
/* 等价于 flex: 0 0 auto */
.item {
  flex: none;
}
```

---

**基本写法：order 排序**
`order: <数值>;`
```css
/* 设置子元素排序 */
.item {
  order: -1;
}
```

---

**基本写法：align-self 单独对齐**
`align-self: <对齐方式>;`
```css
/* 单独设置交叉轴对齐 */
.item {
  align-self: center;
}
```

---

**基本写法：align-self 拉伸**
`align-self: stretch;`
```css
/* 单独拉伸 */
.item {
  align-self: stretch;
}
```

---

## 常见布局模式

**基本写法：水平垂直居中**
`display: flex; justify-content: center; align-items: center;`
```css
/* Flex 实现水平垂直居中 */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

**基本写法：两栏布局**
`display: flex;`
```css
/* 左侧固定，右侧自适应 */
.layout {
  display: flex;
}
.sidebar {
  width: 250px;
  flex-shrink: 0;
}
.main {
  flex-grow: 1;
}
```

---

**基本写法：三栏布局**
`display: flex;`
```css
/* 两侧固定，中间自适应 */
.layout {
  display: flex;
}
.left {
  width: 200px;
  flex-shrink: 0;
}
.center {
  flex-grow: 1;
}
.right {
  width: 200px;
  flex-shrink: 0;
}
```

---

**基本写法：等宽分布**
`display: flex;`
```css
/* 子元素等宽分布 */
.equal {
  display: flex;
}
.equal > * {
  flex: 1;
}
```

---

**基本写法：底部固定**
`display: flex; flex-direction: column; min-height: 100vh;`
```css
/* 页脚固定在底部 */
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.content {
  flex: 1;
}
```

---

**基本写法：导航栏布局**
`display: flex; justify-content: space-between;`
```css
/* 导航栏两端对齐 */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

---

**基本写法：卡片网格**
`display: flex; flex-wrap: wrap; gap: <值>;`
```css
/* 自适应卡片网格 */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.card {
  flex: 1 1 300px;
}
```

---

## 响应式 Flex

**基本写法：嵌套媒体查询**
`@media (max-width: <值>) { flex-direction: column; }`
```css
/* 小屏幕切换为列方向 */
.container {
  display: flex;
  flex-direction: row;
}
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

---

**基本写法：嵌套媒体查询**
`.container { display: flex; @media (max-width: <值>) { flex-direction: column; } }`
```css
/* CSS 原生嵌套媒体查询 */
.container {
  display: flex;
  @media (max-width: 768px) {
    flex-direction: column;
  }
}
```

---

**基本写法：响应式间距**
`gap: clamp(<最小>, <理想>, <最大>);`
```css
/* 响应式间距 */
.grid {
  display: flex;
  gap: clamp(10px, 2vw, 30px);
}
```

---

## Flexbox 新特性

**基本写法：align-content 与 justify-content 在 flex 中的统一**
`justify-content: <值>; align-content: <值>;`
```css
/* 现代浏览器中 align-content 在单行 flex 也生效 */
.flex-container {
  display: flex;
  flex-wrap: wrap;
  /* 主轴与交叉轴均匀分布 */
  justify-content: space-between;
  align-content: space-between;
  min-height: 300px;
}
```

---

**基本写法：gap 属性在 flex 中的应用**
`gap: <行间距> <列间距>;`
```css
/* flex 布局中 gap 自动处理子元素间距 */
.toolbar {
  display: flex;
  flex-wrap: wrap;
  /* 行间距 8px,列间距 16px */
  gap: 8px 16px;
}
.toolbar > * {
  /* 无需 margin 处理间距 */
  flex: 0 0 auto;
}
```

---

**基本写法：flex-basis content 关键字**
`flex-basis: content;`
```css
/* content 表示根据内容自动计算基础尺寸 */
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.tag {
  /* 基础尺寸由内容决定,不再使用 max-content */
  flex-basis: content;
  flex-grow: 0;
  flex-shrink: 1;
}
```



<!-- ============ 文档分隔线：007-css/016-CSS3GridGridLayout.md ============ -->

# CSS Grid 网格布局

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 容器属性

**基本写法：grid 容器**
`display: grid;`
```css
/* 设置为网格容器 */
.container {
  display: grid;
}
```

---

**基本写法：inline-grid 行内容器**
`display: inline-grid;`
```css
/* 设置为行内网格容器 */
.badge {
  display: inline-grid;
}
```

---

**基本写法：grid-template-columns 固定列**
`grid-template-columns: <宽度> <宽度> ...;`
```css
/* 定义固定列宽 */
.container {
  grid-template-columns: 200px 200px 200px;
}
```

---

**基本写法：grid-template-columns fr 单位**
`grid-template-columns: <比例> <比例> ...;`
```css
/* 使用 fr 比例单位 */
.container {
  grid-template-columns: 1fr 2fr 1fr;
}
```

---

**基本写法：grid-template-columns repeat**
`grid-template-columns: repeat(<次数>, <宽度>);`
```css
/* 重复定义列 */
.container {
  grid-template-columns: repeat(3, 1fr);
}
```

---

**基本写法：grid-template-columns auto-fill**
`grid-template-columns: repeat(auto-fill, minmax(<最小>, 1fr));`
```css
/* 自动填充列数 */
.container {
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}
```

---

**基本写法：grid-template-columns auto-fit**
`grid-template-columns: repeat(auto-fit, minmax(<最小>, 1fr));`
```css
/* 自动适应列数 */
.container {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

---

**基本写法：grid-template-rows 固定行**
`grid-template-rows: <高度> <高度> ...;`
```css
/* 定义固定行高 */
.container {
  grid-template-rows: 100px 200px;
}
```

---

**基本写法：grid-template-rows fr 单位**
`grid-template-rows: <比例> <比例> ...;`
```css
/* 使用 fr 比例单位 */
.container {
  grid-template-rows: 1fr 2fr;
}
```

---

**基本写法：grid-template-areas 区域**
`grid-template-areas: "<区域定义>" ...;`
```css
/* 定义网格区域 */
.layout {
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
}
```

---

**基本写法：grid-template 简写**
`grid-template: <行定义> / <列定义>;`
```css
/* 同时定义行和列 */
.container {
  grid-template: 100px 1fr / 200px 1fr;
}
```

---

## 间距属性

**基本写法：gap 间距**
`gap: <值>;`
```css
/* 设置行列间距 */
.grid {
  gap: 20px;
}
```

---

**基本写法：gap 双值**
`gap: <行间距> <列间距>;`
```css
/* 分别设置行列间距 */
.grid {
  gap: 20px 10px;
}
```

---

**基本写法：row-gap 行间距**
`row-gap: <值>;`
```css
/* 仅设置行间距 */
.grid {
  row-gap: 20px;
}
```

---

**基本写法：column-gap 列间距**
`column-gap: <值>;`
```css
/* 仅设置列间距 */
.grid {
  column-gap: 10px;
}
```

---

## 对齐属性

**基本写法：justify-items 单元格水平对齐**
`justify-items: <对齐方式>;`
```css
/* 单元格内容水平对齐 */
.container {
  justify-items: center;
}
```

---

**基本写法：align-items 单元格垂直对齐**
`align-items: <对齐方式>;`
```css
/* 单元格内容垂直对齐 */
.container {
  align-items: center;
}
```

---

**基本写法：place-items 简写**
`place-items: <垂直> <水平>;`
```css
/* 同时设置垂直水平对齐 */
.container {
  place-items: center center;
}
```

---

**基本写法：justify-content 网格水平对齐**
`justify-content: <对齐方式>;`
```css
/* 整个网格水平对齐 */
.container {
  justify-content: center;
}
```

---

**基本写法：align-content 网格垂直对齐**
`align-content: <对齐方式>;`
```css
/* 整个网格垂直对齐 */
.container {
  align-content: center;
}
```

---

**基本写法：place-content 简写**
`place-content: <垂直> <水平>;`
```css
/* 同时设置网格垂直水平对齐 */
.container {
  place-content: center center;
}
```

---

## 子元素属性

**基本写法：grid-column-start 起始列**
`grid-column-start: <数值>;`
```css
/* 设置起始列 */
.item {
  grid-column-start: 2;
}
```

---

**基本写法：grid-column-end 结束列**
`grid-column-end: <数值>;`
```css
/* 设置结束列 */
.item {
  grid-column-end: 4;
}
```

---

**基本写法：grid-column 简写**
`grid-column: <起始> / <结束>;`
```css
/* 同时设置起始结束列 */
.item {
  grid-column: 1 / 3;
}
```

---

**基本写法：grid-column 跨度**
`grid-column: span <数值>;`
```css
/* 设置跨列数 */
.item {
  grid-column: span 2;
}
```

---

**基本写法：grid-row-start 起始行**
`grid-row-start: <数值>;`
```css
/* 设置起始行 */
.item {
  grid-row-start: 1;
}
```

---

**基本写法：grid-row-end 结束行**
`grid-row-end: <数值>;`
```css
/* 设置结束行 */
.item {
  grid-row-end: 3;
}
```

---

**基本写法：grid-row 简写**
`grid-row: <起始> / <结束>;`
```css
/* 同时设置起始结束行 */
.item {
  grid-row: 1 / 3;
}
```

---

**基本写法：grid-row 跨度**
`grid-row: span <数值>;`
```css
/* 设置跨行数 */
.item {
  grid-row: span 2;
}
```

---

**基本写法：grid-area 区域命名**
`grid-area: <区域名>;`
```css
/* 指定区域名 */
.header {
  grid-area: header;
}
```

---

**基本写法：grid-area 简写**
`grid-area: <起始行> / <起始列> / <结束行> / <结束列>;`
```css
/* 同时设置行列起始结束 */
.item {
  grid-area: 1 / 1 / 3 / 3;
}
```

---

**基本写法：justify-self 单独水平对齐**
`justify-self: <对齐方式>;`
```css
/* 单独设置水平对齐 */
.item {
  justify-self: start;
}
```

---

**基本写法：align-self 单独垂直对齐**
`align-self: <对齐方式>;`
```css
/* 单独设置垂直对齐 */
.item {
  align-self: end;
}
```

---

**基本写法：place-self 简写**
`place-self: <垂直> <水平>;`
```css
/* 同时设置单独垂直水平对齐 */
.item {
  place-self: center center;
}
```

---

## 自动布局

**基本写法：grid-auto-rows 自动行高**
`grid-auto-rows: <高度>;`
```css
/* 设置自动行高 */
.container {
  grid-auto-rows: 100px;
}
```

---

**基本写法：grid-auto-columns 自动列宽**
`grid-auto-columns: <宽度>;`
```css
/* 设置自动列宽 */
.container {
  grid-auto-columns: 200px;
}
```

---

**基本写法：grid-auto-flow 行方向**
`grid-auto-flow: row;`
```css
/* 自动填充按行排列 */
.container {
  grid-auto-flow: row;
}
```

---

**基本写法：grid-auto-flow 列方向**
`grid-auto-flow: column;`
```css
/* 自动填充按列排列 */
.container {
  grid-auto-flow: column;
}
```

---

**基本写法：grid-auto-flow 密集填充**
`grid-auto-flow: row dense;`
```css
/* 密集填充空缺 */
.container {
  grid-auto-flow: row dense;
}
```

---

## 常见布局模式

**基本写法：圣杯布局**
`grid-template-areas: "<区域定义>";`
```css
/* 经典三栏布局 */
.holy-grail {
  display: grid;
  grid-template-areas:
    "header header header"
    "nav main aside"
    "footer footer footer";
  grid-template-rows: 60px 1fr 40px;
  grid-template-columns: 200px 1fr 200px;
}
```

---

**基本写法：卡片网格**
`grid-template-columns: repeat(auto-fill, minmax(<值>, 1fr));`
```css
/* 响应式卡片网格 */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}
```

---

**基本写法：12 列网格**
`grid-template-columns: repeat(12, 1fr);`
```css
/* 12 列网格系统 */
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}
.col-6 {
  grid-column: span 6;
}
```

---

**基本写法：水平垂直居中**
`display: grid; place-items: center;`
```css
/* Grid 实现水平垂直居中 */
.center {
  display: grid;
  place-items: center;
}
```

---

**基本写法：响应式网格**
`grid-template-columns: repeat(auto-fit, minmax(<值>, 1fr));`
```css
/* 自动适应屏幕的网格 */
.responsive {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
  gap: 20px;
}
```

---

## 命名网格线

**基本写法：命名网格线**
`grid-template-columns: [<线名>] <宽度> [<线名>] <宽度>;`
```css
/* 使用命名网格线 */
.container {
  grid-template-columns: [start] 200px [middle] 1fr [end];
}
```

---

**基本写法：引用命名网格线**
`grid-column-start: <线名>;`
```css
/* 引用命名网格线 */
.item {
  grid-column-start: start;
  grid-column-end: end;
}
```

---

**基本写法：多名称网格线**
`grid-template-columns: [<名1> <名2>] <宽度>;`
```css
/* 网格线多个名称 */
.container {
  grid-template-columns: [start sidebar-start] 200px [main-start] 1fr [end];
}
```

---

## 子网格

**基本写法：subgrid 子网格**
`grid-template-columns: subgrid;`
```css
/* 子元素继承父网格 */
.nested {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: 1 / 4;
}
```

---

**基本写法：subgrid 子网格行**
`grid-template-rows: subgrid;`
```css
/* 子元素继承父网格行 */
.nested {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: 1 / 3;
}
```

---

## 响应式 Grid

**基本写法：嵌套媒体查询**
`@media (max-width: <值>) { grid-template-columns: 1fr; }`
```css
/* 小屏幕切换为单列 */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
@media (max-width: 768px) {
  .grid {
    grid-template-columns: 1fr;
  }
}
```

---

**基本写法：嵌套媒体查询**
`.grid { display: grid; @media (max-width: <值>) { grid-template-columns: 1fr; } }`
```css
/* CSS 原生嵌套媒体查询 */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
}
```

---

**基本写法：minmax 响应式**
`grid-template-columns: repeat(auto-fit, minmax(<最小>, <最大>));`
```css
/* 使用 minmax 实现响应式 */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

---

## Grid 新特性

**基本写法：subgrid 子网格**
`grid-template-columns: subgrid;`
```css
/* 子网格继承父网格的轨道定义 */
.card {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 10px;
}
.card-body {
  display: grid;
  /* 继承父网格列定义与间距 */
  grid-template-columns: subgrid;
  grid-column: 1 / -1;
}
```

---

**基本写法：grid-template-rows/columns masonry 砌体布局**
`grid-template-rows: masonry;`
```css
/* 砌体布局:类似 Pinterest 瀑布流 */
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  /* 行轨道按砌体方式排列 */
  grid-template-rows: masonry;
  gap: 16px;
}
```

---

**基本写法：grid auto-fit 与 auto-fill 区别**
`grid-template-columns: repeat(auto-fit|auto-fill, minmax(<值>, 1fr));`
```css
/* auto-fit:空轨道折叠,元素拉伸填满 */
.grid-fit {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
/* auto-fill:保留空轨道,元素不拉伸 */
.grid-fill {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}
```

---

**基本写法：Container Query 与 Grid 结合**
`container-type: inline-size; @container <名称> (min-width: <值>) { grid-template-columns: <值>; }`
```css
/* 容器查询驱动 Grid 布局响应式 */
.cards-wrapper {
  container-type: inline-size;
  container-name: cards;
}
.cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}
@container cards (min-width: 600px) {
  .cards {
    grid-template-columns: repeat(2, 1fr);
  }
}
@container cards (min-width: 900px) {
  .cards {
    grid-template-columns: repeat(3, 1fr);
  }
}
```



<!-- ============ 文档分隔线：007-css/017-Flexbox.md ============ -->

# CSS Flexbox 布局速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 容器属性

**基本写法：flex 容器**
`display: flex;`
```css
/* 设置弹性容器 */
.container {
  display: flex;
}
```

---

**基本写法：inline-flex 行内容器**
`display: inline-flex;`
```css
/* 行内弹性容器 */
.badge {
  display: inline-flex;
}
```

---

**基本写法：主轴方向**
`flex-direction: row | row-reverse | column | column-reverse;`
```css
/* 主轴为水平方向 */
.row {
  flex-direction: row;
}
/* 主轴为垂直方向 */
.col {
  flex-direction: column;
}
```

---

**基本写法：是否换行**
`flex-wrap: nowrap | wrap | wrap-reverse;`
```css
/* 子元素自动换行 */
.container {
  flex-wrap: wrap;
}
```

---

**基本写法：flex-flow 简写**
`flex-flow: <方向> <换行>;`
```css
/* 同时设置方向和换行 */
.container {
  flex-flow: row wrap;
}
```

---

**基本写法：主轴对齐**
`justify-content: flex-start | center | flex-end | space-between | space-around | space-evenly;`
```css
/* 主轴均匀分布间距相同 */
.container {
  justify-content: space-evenly;
}
```

---

**基本写法：交叉轴对齐**
`align-items: flex-start | center | flex-end | stretch | baseline;`
```css
/* 交叉轴居中对齐 */
.container {
  align-items: center;
}
```

---

**基本写法：多行交叉轴对齐**
`align-content: flex-start | center | flex-end | space-between | space-around | stretch;`
```css
/* 多行时交叉轴两端对齐 */
.container {
  flex-wrap: wrap;
  align-content: space-between;
}
```

---

**基本写法：gap 间距**
`gap: <值>;`
```css
/* 子元素间距 */
.container {
  display: flex;
  gap: 20px;
}
```

---

**基本写法：gap 行列双值**
`gap: <行间距> <列间距>;`
```css
/* 分别设置行列间距 */
.grid {
  gap: 20px 10px;
}
```

---

## 子元素属性

**基本写法：flex-grow 放大比例**
`flex-grow: <数值>;`
```css
/* 子元素放大比例 */
.item {
  flex-grow: 1;
}
```

---

**基本写法：flex-shrink 缩小比例**
`flex-shrink: <数值>;`
```css
/* 不缩小 */
.item {
  flex-shrink: 0;
}
```

---

**基本写法：flex-basis 基础尺寸**
`flex-basis: <长度> | <百分比> | content;`
```css
/* 基础尺寸由内容决定 */
.tag {
  flex-basis: content;
}
```

---

**基本写法：flex 简写**
`flex: <grow> <shrink> <basis>;`
```css
/* 同时设置三个属性 */
.item {
  flex: 1 1 0%;
}
```

---

**基本写法：flex 关键字**
`flex: auto | none | 1;`
```css
/* 等价于 flex: 1 1 auto */
.item-auto {
  flex: auto;
}
/* 等价于 flex: 0 0 auto */
.item-none {
  flex: none;
}
```

---

**基本写法：order 排序**
`order: <数值>;`
```css
/* 设置子元素排序（默认 0） */
.item {
  order: -1;
}
```

---

**基本写法：align-self 单独对齐**
`align-self: auto | flex-start | center | flex-end | stretch;`
```css
/* 单独设置交叉轴对齐 */
.item {
  align-self: center;
}
```

---

## 常见布局模式

**基本写法：水平垂直居中**
`display: flex; justify-content: center; align-items: center;`
```css
/* Flex 居中方案 */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

---

**基本写法：两栏布局**
`display: flex;`
```css
/* 左侧固定右侧自适应 */
.layout {
  display: flex;
}
.sidebar {
  width: 250px;
  flex-shrink: 0;
}
.main {
  flex-grow: 1;
}
```

---

**基本写法：三栏布局**
`display: flex;`
```css
/* 两侧固定中间自适应 */
.layout {
  display: flex;
}
.left, .right {
  width: 200px;
  flex-shrink: 0;
}
.center {
  flex-grow: 1;
}
```

---

**基本写法：等宽分布**
`display: flex;`
```css
/* 子元素等宽分布 */
.equal {
  display: flex;
}
.equal > * {
  flex: 1;
}
```

---

**基本写法：底部固定布局**
`display: flex; flex-direction: column; min-height: 100vh;`
```css
/* 页脚固定在底部 */
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.content {
  flex: 1;
}
```

---

**基本写法：卡片自适应网格**
`display: flex; flex-wrap: wrap; gap: <值>;`
```css
/* 自适应卡片网格 */
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.card {
  flex: 1 1 300px;
}
```

---

## 响应式 Flex

**基本写法：媒体查询切换方向**
`@media (max-width: <值>) { flex-direction: column; }`
```css
/* 小屏幕切换为列方向 */
.container {
  display: flex;
  flex-direction: row;
}
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

---

**基本写法：原生嵌套媒体查询**
`.container { display: flex; @media (max-width: <值>) { flex-direction: column; } }`
```css
/* CSS 原生嵌套写法 */
.container {
  display: flex;
  @media (max-width: 768px) {
    flex-direction: column;
  }
}
```

---

**基本写法：响应式间距**
`gap: clamp(<最小>, <理想>, <最大>);`
```css
/* 流式响应间距 */
.grid {
  display: flex;
  gap: clamp(10px, 2vw, 30px);
}
```

---

## Flexbox 新特性

**基本写法：单行 align-content 生效**
`align-content: <值>;`
```css
/* 现代浏览器单行也支持 align-content */
.flex {
  display: flex;
  align-content: center;
  min-height: 200px;
}
```

---

**基本写法：place-content 简写**
`place-content: <align-content> <justify-content>;`
```css
/* 同时设置两个对齐属性 */
.container {
  display: flex;
  flex-wrap: wrap;
  place-content: center space-between;
}
```

---

**基本写法：place-items 简写**
`place-items: <align-items> <justify-items>;`
```css
/* 同时设置 items 对齐 */
.container {
  display: flex;
  place-items: center;
}
```



<!-- ============ 文档分隔线：007-css/018-Grid.md ============ -->

# CSS Grid 布局速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 容器属性

**基本写法：grid 容器**
`display: grid;`
```css
/* 设置网格容器 */
.container {
  display: grid;
}
```

---

**基本写法：inline-grid 行内网格**
`display: inline-grid;`
```css
/* 行内网格容器 */
.row {
  display: inline-grid;
}
```

---

**基本写法：定义列轨道**
`grid-template-columns: <值> [值 ...];`
```css
/* 定义三列等宽 */
.container {
  grid-template-columns: 1fr 1fr 1fr;
}
```

---

**基本写法：repeat 重复**
`grid-template-columns: repeat(<数量>, <值>);`
```css
/* 重复 3 列等宽 */
.container {
  grid-template-columns: repeat(3, 1fr);
}
```

---

**基本写法：auto-fill 自动填充**
`grid-template-columns: repeat(auto-fill, minmax(<最小>, 1fr));`
```css
/* 响应式自动填充列 */
.container {
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
}
```

---

**基本写法：auto-fit 自动适应**
`grid-template-columns: repeat(auto-fit, minmax(<最小>, 1fr));`
```css
/* 自动适应并拉伸填满 */
.container {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

---

**基本写法：定义行轨道**
`grid-template-rows: <值> [值 ...];`
```css
/* 定义行高度 */
.container {
  grid-template-rows: 100px auto 100px;
}
```

---

**基本写法：fr 单位**
`grid-template-columns: 1fr 2fr 1fr;`
```css
/* 按比例分配空间 */
.container {
  grid-template-columns: 1fr 2fr 1fr;
}
```

---

**基本写法：minmax 最小最大**
`grid-template-columns: minmax(<最小>, <最大>);`
```css
/* 列宽最小 200px 最大 1fr */
.container {
  grid-template-columns: minmax(200px, 1fr);
}
```

---

**基本写法：gap 间距**
`gap: <值>;`
```css
/* 网格间距 */
.container {
  gap: 20px;
}
```

---

**基本写法：gap 行列分开**
`row-gap: <值>; column-gap: <值>;`
```css
/* 分别设置行列间距 */
.container {
  row-gap: 20px;
  column-gap: 10px;
}
```

---

## 网格线与区域

**基本写法：命名网格线**
`grid-template-columns: [线名] <值> [线名];`
```css
/* 命名网格线 */
.container {
  grid-template-columns: [start] 1fr [middle] 1fr [end];
}
```

---

**基本写法：grid-template-areas 区域**
`grid-template-areas: "<区域定义>";`
```css
/* 命名网格区域 */
.container {
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}
```

---

**基本写法：项目放置到区域**
`grid-area: <区域名>;`
```css
/* 将项目放入指定区域 */
.header {
  grid-area: header;
}
.main {
  grid-area: main;
}
```

---

**基本写法：基于线放置**
`grid-column: <起线> / <止线>;`
```css
/* 跨越指定网格线 */
.item {
  grid-column: 1 / 3;
  grid-row: 1 / 2;
}
```

---

**基本写法：span 跨越**
`grid-column: span <数量>;`
```css
/* 跨越指定列数 */
.item {
  grid-column: span 2;
}
```

---

**基本写法：grid-area 简写**
`grid-area: <行起> / <列起> / <行止> / <列止>;`
```css
/* 同时指定行列起止 */
.item {
  grid-area: 1 / 1 / 3 / 3;
}
```

---

## 对齐属性

**基本写法：justify-items 水平对齐**
`justify-items: start | end | center | stretch;`
```css
/* 网格项水平对齐 */
.container {
  justify-items: center;
}
```

---

**基本写法：align-items 垂直对齐**
`align-items: start | end | center | stretch;`
```css
/* 网格项垂直对齐 */
.container {
  align-items: center;
}
```

---

**基本写法：justify-content 整体水平**
`justify-content: start | end | center | space-between | space-around | space-evenly;`
```css
/* 整个网格水平对齐 */
.container {
  justify-content: space-between;
}
```

---

**基本写法：align-content 整体垂直**
`align-content: start | end | center | space-between | space-around;`
```css
/* 整个网格垂直对齐 */
.container {
  align-content: center;
}
```

---

**基本写法：place-items 简写**
`place-items: <align-items> <justify-items>;`
```css
/* 同时设置垂直水平对齐 */
.container {
  place-items: center;
}
```

---

## 自动布局

**基本写法：自动流方向**
`grid-auto-flow: row | column | dense;`
```css
/* 稠密填充避免空隙 */
.container {
  grid-auto-flow: dense;
}
```

---

**基本写法：行方向稠密**
`grid-auto-flow: row dense;`
```css
/* 行方向稠密排列 */
.container {
  grid-auto-flow: row dense;
}
```

---

**基本写法：自动轨道尺寸**
`grid-auto-rows: <值>; grid-auto-columns: <值>;`
```css
/* 自动生成行高 */
.container {
  grid-auto-rows: minmax(100px, auto);
}
```

---

## 常见布局模式

**基本写法：圣杯布局**
`display: grid; grid-template-areas: "...";`
```css
/* 经典三栏圣杯布局 */
.layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}
```

---

**基本写法：响应式卡片网格**
`grid-template-columns: repeat(auto-fill, minmax(<最小>, 1fr));`
```css
/* 自适应卡片网格 */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}
```

---

**基本写法：12 列网格系统**
`grid-template-columns: repeat(12, 1fr);`
```css
/* 12 列栅格系统 */
.grid12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 20px;
}
.col-6 {
  grid-column: span 6;
}
.col-4 {
  grid-column: span 4;
}
```

---

## 现代 Grid 特性

**基本写法：subgrid 子网格**
`grid-template-columns: subgrid;`
```css
/* 子网格继承父网格轨道 */
.nested {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: 1 / -1;
}
```

---

**基本写法：容器查询单位**
`grid-template-columns: repeat(auto-fill, minmax(20cqi, 1fr));`
```css
/* 基于容器尺寸的列宽 */
.card {
  container-type: inline-size;
}
.card-inner {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(20cqi, 1fr));
}
```

---

**基本写法：aspect-ratio 控制比例**
`aspect-ratio: <宽> / <高>;`
```css
/* 网格项保持 16:9 比例 */
.video-item {
  aspect-ratio: 16 / 9;
}
```

---

**基本写法：masonry 瀑布流（实验性）**
`grid-template-rows: masonry;`
```css
/* CSS Grid 瀑布流布局（实验特性） */
.masonry {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: masonry;
}
```



<!-- ============ 文档分隔线：007-css/019-CSSVariable.md ============ -->

# CSS 变量自定义属性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本定义与使用

**基本写法：定义自定义属性**
`--<属性名>: <值>;`
```css
/* 在 :root 定义全局变量 */
:root {
  --primary-color: #3498db;
  --font-size: 16px;
}
```

---

**基本写法：使用 var()**
`color: var(--<属性名>);`
```css
/* 引用自定义属性 */
.button {
  color: var(--primary-color);
  font-size: var(--font-size);
}
```

---

**基本写法：带默认值的 var()**
`var(--<属性名>, <默认值>);`
```css
/* 变量未定义时使用默认值 */
.text {
  color: var(--text-color, #333);
}
```

---

**基本写法：嵌套默认值**
`var(--<属性名>, var(--<其他属性>, <默认值>));`
```css
/* 多层回退默认值 */
.text {
  color: var(--theme-color, var(--default-color, black));
}
```

---

## 作用域

**基本写法：全局作用域**
`:root { --<属性名>: <值>; }`
```css
/* :root 定义的变量全局可用 */
:root {
  --spacing: 16px;
}
```

---

**基本写法：局部作用域**
`<选择器> { --<属性名>: <值>; }`
```css
/* 仅在 .card 内有效 */
.card {
  --padding: 24px;
  padding: var(--padding);
}
```

---

**基本写法：作用域覆盖**
`<子选择器> { --<属性名>: <新值>; }`
```css
/* 子作用域覆盖父作用域 */
.card {
  --text-color: black;
}
.card.dark {
  --text-color: white;
}
```

---

**基本写法：媒体查询作用域**
`@media (<条件>) { :root { --<属性名>: <值>; } }`
```css
/* 响应式调整变量值 */
:root {
  --font-size: 18px;
}
@media (max-width: 768px) {
  :root {
    --font-size: 16px;
  }
}
```

---

## 类型化自定义属性

**基本写法：@property 定义类型**
`@property --<属性名> { syntax: <类型>; inherits: <是否继承>; initial-value: <初始值>; }`
```css
/* 定义带类型的自定义属性 */
@property --angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}
```

---

**基本写法：颜色类型**
`@property --<属性名> { syntax: '<color>'; ... }`
```css
/* 颜色类型变量支持动画过渡 */
@property --theme-color {
  syntax: '<color>';
  inherits: true;
  initial-value: #3498db;
}
```

---

**基本写法：长度类型**
`@property --<属性名> { syntax: '<length>'; ... }`
```css
/* 长度类型变量 */
@property --spacing {
  syntax: '<length>';
  inherits: true;
  initial-value: 16px;
}
```

---

**基本写法：整数类型**
`@property --<属性名> { syntax: '<integer>'; ... }`
```css
/* 整数类型变量 */
@property --count {
  syntax: '<integer>';
  inherits: false;
  initial-value: 3;
}
```

---

## 常见用法

**基本写法：主题色系统**
`:root { --<语义名>: <值>; }`
```css
/* 设计令牌语义化命名 */
:root {
  --color-primary: #3498db;
  --color-secondary: #2ecc71;
  --color-danger: #e74c3c;
  --color-text: #333;
  --color-bg: #fff;
}
```

---

**基本写法：暗色主题**
`[data-theme="dark"] { --<属性名>: <值>; }`
```css
/* 通过 data 属性切换暗色主题 */
[data-theme="dark"] {
  --color-text: #fff;
  --color-bg: #1a1a1a;
  --color-primary: #5dade2;
}
```

---

**基本写法：prefers-color-scheme 暗色**
`@media (prefers-color-scheme: dark) { :root { --<属性名>: <值>; } }`
```css
/* 跟随系统暗色模式 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #fff;
    --color-bg: #1a1a1a;
  }
}
```

---

**基本写法：spacing 比例系统**
`:root { --space-<级数>: <值>; }`
```css
/* 8px 间距比例系统 */
:root {
  --space-1: 0.5rem;
  --space-2: 1rem;
  --space-3: 1.5rem;
  --space-4: 2rem;
  --space-5: 3rem;
}
```

---

**基本写法：字体大小比例**
`:root { --text-<语义名>: <值>; }`
```css
/* 字体大小令牌 */
:root {
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
}
```

---

## 进阶用法

**基本写法：JavaScript 读写**
`element.style.setProperty('<属性名>', <值>);`
```css
/* JS 动态修改变量 */
/* document.documentElement.style.setProperty('--primary', '#ff0000'); */
:root {
  --primary: #3498db;
}
```

---

**基本写法：calc 中使用**
`calc(var(--<属性名>) * <系数>);`
```css
/* 变量参与计算 */
.box {
  width: calc(var(--base-width) * 2);
  padding: calc(var(--spacing) / 2);
}
```

---

**基本写法：变量组合**
`var(--<属性1>) var(--<属性2>);`
```css
/* 多变量组合成完整值 */
.box {
  margin: var(--spacing) var(--spacing-lg);
  border: var(--border-width) solid var(--border-color);
}
```

---

**基本写法：响应式字体**
`font-size: clamp(<最小>, var(--<变量>), <最大>);`
```css
/* 流式响应字体结合变量 */
:root {
  --font-scale: 2vw;
}
h1 {
  font-size: clamp(1.5rem, var(--font-scale) + 1rem, 3rem);
}
```

---

## light-dark() 函数（2024+）

**基本写法：light-dark 自动明暗**
`color: light-dark(<浅色>, <深色>);`
```css
/* 根据配色方案自动切换颜色 */
.text {
  color: light-dark(#333, #fff);
  background: light-dark(#fff, #1a1a1a);
}
```

---

**基本写法：配合 color-scheme**
`color-scheme: light dark;`
```css
/* 声明支持明暗两种配色 */
:root {
  color-scheme: light dark;
}
```

---

## color-mix() 混合颜色

**基本写法：color-mix 混合**
`color: color-mix(in <色彩空间>, <颜色1> <比例>, <颜色2>);`
```css
/* 混合两种颜色 */
.box {
  background: color-mix(in srgb, var(--primary) 50%, white);
}
```

---

**基本写法：基于变量的颜色变体**
`color: color-mix(in srgb, var(--color) <比例>, <其他色>);`
```css
/* 生成颜色的明暗变体 */
.button {
  background: var(--primary);
  border-color: color-mix(in srgb, var(--primary) 80%, black);
}
.button:hover {
  background: color-mix(in srgb, var(--primary) 80%, white);
}
```



<!-- ============ 文档分隔线：007-css/020-AnimationTransition.md ============ -->

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



<!-- ============ 文档分隔线：007-css/021-ResponsiveDesign.md ============ -->

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



<!-- ============ 文档分隔线：007-css/022-PseudoClassPseudoElement.md ============ -->

# CSS 伪类与伪元素速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 链接与交互伪类

**基本写法：:link 未访问链接**
`a:link { }`
```css
/* 未访问链接样式 */
a:link {
  color: blue;
}
```

---

**基本写法：:visited 已访问链接**
`a:visited { }`
```css
/* 已访问链接样式 */
a:visited {
  color: purple;
}
```

---

**基本写法：:hover 悬停**
`<选择器>:hover { }`
```css
/* 鼠标悬停样式 */
.button:hover {
  background: #2980b9;
}
```

---

**基本写法：:active 激活**
`<选择器>:active { }`
```css
/* 鼠标按下样式 */
.button:active {
  transform: scale(0.95);
}
```

---

**基本写法：:focus 获得焦点**
`<选择器>:focus { }`
```css
/* 获得焦点样式 */
input:focus {
  border-color: #3498db;
  outline: none;
}
```

---

**基本写法：:focus-visible 键盘焦点**
`<选择器>:focus-visible { }`
```css
/* 仅键盘聚焦时显示焦点框 */
input:focus-visible {
  outline: 2px solid #3498db;
}
```

---

**基本写法：:focus-within 子元素聚焦**
`<选择器>:focus-within { }`
```css
/* 子元素获得焦点时父元素样式 */
.form:focus-within {
  border-color: #3498db;
}
```

---

## 表单伪类

**基本写法：:checked 选中状态**
`input:checked { }`
```css
/* 复选框选中样式 */
input:checked + label {
  color: #27ae60;
}
```

---

**基本写法：:disabled 禁用**
`input:disabled { }`
```css
/* 禁用输入框样式 */
input:disabled {
  background: #f0f0f0;
  cursor: not-allowed;
}
```

---

**基本写法：:enabled 可用**
`input:enabled { }`
```css
/* 可用输入框样式 */
input:enabled {
  background: white;
}
```

---

**基本写法：:required 必填**
`input:required { }`
```css
/* 必填字段样式 */
input:required {
  border-left: 3px solid #e74c3c;
}
```

---

**基本写法：:valid 有效**
`input:valid { }`
```css
/* 校验通过样式 */
input:valid {
  border-color: #27ae60;
}
```

---

**基本写法：:invalid 无效**
`input:invalid { }`
```css
/* 校验失败样式 */
input:invalid {
  border-color: #e74c3c;
}
```

---

**基本写法：:placeholder-shown 占位显示**
`input:placeholder-shown { }`
```css
/* 输入框为空显示占位符时 */
input:placeholder-shown {
  background: #fafafa;
}
```

---

**基本写法：:read-only 只读**
`input:read-only { }`
```css
/* 只读输入框样式 */
input:read-only {
  background: #f5f5f5;
}
```

---

## 结构伪类

**基本写法：:first-child 第一个子元素**
`<选择器>:first-child { }`
```css
/* 第一个列表项样式 */
li:first-child {
  font-weight: bold;
}
```

---

**基本写法：:last-child 最后一个子元素**
`<选择器>:last-child { }`
```css
/* 最后一个列表项样式 */
li:last-child {
  border-bottom: none;
}
```

---

**基本写法：:only-child 唯一子元素**
`<选择器>:only-child { }`
```css
/* 父元素唯一子元素样式 */
.icon:only-child {
  margin: 0 auto;
}
```

---

**基本写法：:first-of-type 同类型首个**
`<选择器>:first-of-type { }`
```css
/* 第一个段落样式 */
p:first-of-type {
  font-size: 1.2em;
}
```

---

**基本写法：:last-of-type 同类型末个**
`<选择器>:last-of-type { }`
```css
/* 最后一个段落样式 */
p:last-of-type {
  margin-bottom: 0;
}
```

---

**基本写法：:nth-child 第 N 个子元素**
`<选择器>:nth-child(<n>) { }`
```css
/* 第 2 个子元素 */
li:nth-child(2) {
  color: red;
}
```

---

**基本写法：:nth-child 奇偶**
`<选择器>:nth-child(odd | even) { }`
```css
/* 隔行变色 */
tr:nth-child(even) {
  background: #f9f9f9;
}
```

---

**基本写法：:nth-child 公式**
`<选择器>:nth-child(<公式>) { }`
```css
/* 每 3 个元素选第 1 个 */
li:nth-child(3n+1) {
  color: blue;
}
```

---

**基本写法：:nth-last-child 倒数第 N 个**
`<选择器>:nth-last-child(<n>) { }`
```css
/* 倒数第 2 个子元素 */
li:nth-last-child(2) {
  color: green;
}
```

---

**基本写法：:nth-of-type 同类型第 N 个**
`<选择器>:nth-of-type(<n>) { }`
```css
/* 第 2 个段落 */
p:nth-of-type(2) {
  color: red;
}
```

---

**基本写法：:empty 空元素**
`<选择器>:empty { }`
```css
/* 空段落隐藏 */
p:empty {
  display: none;
}
```

---

**基本写法：:root 根元素**
`:root { }`
```css
/* 定义全局 CSS 变量 */
:root {
  --primary: #3498db;
}
```

---

## 否定与匹配伪类

**基本写法：:not 否定**
`<选择器>:not(<排除选择器>) { }`
```css
/* 非特殊按钮的样式 */
.button:not(.special) {
  background: gray;
}
```

---

**基本写法：:not 多条件否定**
`<选择器>:not(<选择器1>, <选择器2>) { }`
```css
/* 排除多个选择器 */
input:not(:disabled, [type="hidden"]) {
  border: 1px solid #ccc;
}
```

---

**基本写法：:is 匹配任一**
`<选择器>:is(<选择器1>, <选择器2>) { }`
```css
/* 匹配多个标题级别 */
:is(h1, h2, h3) {
  color: #333;
}
```

---

**基本写法：:where 匹配任一（零优先级）**
`<选择器>:where(<选择器1>, <选择器2>) { }`
```css
/* 零优先级匹配便于覆盖 */
:where(.card) .title {
  font-size: 1.2em;
}
```

---

## 状态伪类

**基本写法：:target 目标锚点**
`<选择器>:target { }`
```css
/* 锚点目标高亮 */
.section:target {
  background: #fffacd;
}
```

---

**基本写法：:default 默认选项**
`input:default { }`
```css
/* 默认选中的单选按钮 */
input:default {
  box-shadow: 0 0 0 2px #3498db;
}
```

---

**基本写法：:indeterminate 不确定状态**
`input:indeterminate { }`
```css
/* 不确定状态复选框 */
input:indeterminate {
  background: gray;
}
```

---

## 伪元素

**基本写法：::before 前置内容**
`<选择器>::before { content: <内容>; }`
```css
/* 添加前置图标 */
.link::before {
  content: "→ ";
}
```

---

**基本写法：::after 后置内容**
`<选择器>::after { content: <内容>; }`
```css
/* 添加后置内容 */
.required::after {
  content: " *";
  color: red;
}
```

---

**基本写法：::first-letter 首字母**
`<选择器>::first-letter { }`
```css
/* 段落首字母放大 */
p::first-letter {
  font-size: 2em;
  float: left;
}
```

---

**基本写法：::first-line 首行**
`<选择器>::first-line { }`
```css
/* 段落首行样式 */
p::first-line {
  font-weight: bold;
}
```

---

**基本写法：::selection 选中文本**
`::selection { }`
```css
/* 选中文本样式 */
::selection {
  background: #3498db;
  color: white;
}
```

---

**基本写法：::placeholder 占位符**
`input::placeholder { }`
```css
/* 占位符文本样式 */
input::placeholder {
  color: #999;
}
```

---

**基本写法：::marker 列表标记**
`li::marker { }`
```css
/* 列表项标记样式 */
li::marker {
  color: #3498db;
  font-weight: bold;
}
```

---

**基本写法：::file-selector-button 文件按钮**
`input[type=file]::file-selector-button { }`
```css
/* 文件选择按钮样式 */
input[type=file]::file-selector-button {
  background: #3498db;
  color: white;
  border: none;
  padding: 6px 12px;
}
```

---

## 现代 CSS 伪类（2024+）

**基本写法：:has 父级选择**
`<选择器>:has(<子选择器>) { }`
```css
/* 包含图片的卡片样式 */
.card:has(img) {
  padding: 0;
}
```

---

**基本写法：:has 否定形式**
`<选择器>:not(:has(<子选择器>)) { }`
```css
/* 不包含错误的表单 */
.form:not(:has(.error)) {
  border-color: #27ae60;
}
```

---

**基本写法：:has 多条件**
`<选择器>:has(<选择器1>, <选择器2>) { }`
```css
/* 包含图片或视频的容器 */
.container:has(img, video) {
  aspect-ratio: 16 / 9;
}
```

---

**基本写法：:defined 自定义元素已定义**
`<选择器>:defined { }`
```css
/* 自定义元素定义后显示 */
custom-element:not(:defined) {
  display: none;
}
```

---

**基本写法：:modal 模态框**
`<选择器>:modal { }`
```css
/* 原生模态框样式 */
dialog:modal {
  border: none;
  border-radius: 8px;
}
```

---

**基本写法：:fullscreen 全屏**
`<选择器>:fullscreen { }`
```css
/* 全屏元素样式 */
.video:fullscreen {
  width: 100vw;
  height: 100vh;
}
```

---

**基本写法：:picture-in-picture 画中画**
`<选择器>:picture-in-picture { }`
```css
/* 画中画视频样式 */
video:picture-in-picture {
  border: 2px solid #3498db;
}
```

---

**基本写法：:playing 播放中**
`<选择器>:playing { }`
```css
/* 视频播放时样式 */
video:playing {
  filter: brightness(1.1);
}
```

---

## @scope 作用域（2024+）

**基本写法：@scope 限定作用域**
`@scope (<选择器>) { <规则> }`
```css
/* 限定样式作用范围 */
@scope (.card) {
  .title {
    color: red;
  }
}
```

---

**基本写法：@scope 范围限定**
`@scope (<起>) to (<止>) { }`
```css
/* 限定到 .start 到 .end 之间 */
@scope (.start) to (.end) {
  p {
    color: blue;
  }
}
```



<!-- ============ 文档分隔线：007-css/023-PositionFloat.md ============ -->

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



<!-- ============ 文档分隔线：007-css/024-ModernCSSFunction.md ============ -->

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



<!-- ============ 文档分隔线：007-css/025-Transform3D.md ============ -->

# CSS transform 与 3D 变换语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 2D 变换

**基本写法：平移**
`transform: translate(<tx>, <ty>);`
```css
/* 沿 X/Y 轴平移 */
.box { transform: translate(50px, 20px); }
.box { transform: translateX(50px); }
.box { transform: translateY(20px); }
.box { transform: translate(-50%, -50%); }  /* 常用于居中 */
```

---

**基本写法：缩放**
`transform: scale(<sx> [, <sy>]);`
```css
/* 缩放比例，1 为原始大小 */
.box { transform: scale(2); }          /* 整体放大 2 倍 */
.box { transform: scale(2, 0.5); }     /* X 放大 2 倍 Y 缩小一半 */
.box { transform: scaleX(1.5); }
.box { transform: scaleY(0.8); }
```

---

**基本写法：旋转**
`transform: rotate(<角度>);`
```css
/* 顺时针旋转 */
.box { transform: rotate(45deg); }
.box { transform: rotate(0.5turn); }   /* 半圈 */
.box { transform: rotate(-90deg); }
```

---

**基本写法：倾斜**
`transform: skew(<ax> [, <ay>]);`
```css
/* 倾斜变换 */
.box { transform: skew(10deg, 5deg); }
.box { transform: skewX(15deg); }
.box { transform: skewY(10deg); }
```

---

**基本写法：矩阵变换**
`transform: matrix(<a>, <b>, <c>, <d>, <e>, <f>);`
```css
/* 2D 仿射矩阵，等价于 translate+scale+rotate+skew */
.box { transform: matrix(1, 0, 0, 1, 50, 20); }  /* 等价 translate(50px,20px) */
```

---

## 3D 变换

**基本写法：3D 平移**
`transform: translate3d(<tx>, <ty>, <tz>);`
```css
/* 三轴平移，tz 为 Z 轴（正值朝向观察者） */
.box { transform: translate3d(10px, 20px, 100px); }
.box { transform: translateZ(100px); }
```

---

**基本写法：3D 缩放**
`transform: scale3d(<sx>, <sy>, <sz>);`
```css
/* 三轴缩放 */
.box { transform: scale3d(1.5, 1.5, 1.5); }
.box { transform: scaleZ(2); }
```

---

**基本写法：3D 旋转**
`transform: rotate3d(<x>, <y>, <z>, <角度>);`
```css
/* 绕任意轴旋转，(x,y,z) 为方向向量 */
.box { transform: rotate3d(1, 0, 0, 45deg); }   /* 绕 X 轴 */
.box { transform: rotate3d(0, 1, 0, 45deg); }   /* 绕 Y 轴 */
.box { transform: rotate3d(0, 0, 1, 45deg); }   /* 绕 Z 轴，等价 rotate */
.box { transform: rotate3d(1, 1, 0, 60deg); }   /* 绕对角轴 */

/* 简写 */
.box { transform: rotateX(45deg); }
.box { transform: rotateY(45deg); }
.box { transform: rotateZ(45deg); }
```

---

**基本写法：3D 矩阵**
`transform: matrix3d(<16 个值>);`
```css
/* 4x4 3D 变换矩阵 */
.box { transform: matrix3d(
    1,0,0,0,
    0,1,0,0,
    0,0,1,0,
    50,20,100,1
); }
```

---

**基本写法：透视**
`transform: perspective(<距离>);`
```css
/* 直接在 transform 中设置透视距离 */
.box { transform: perspective(800px) rotateY(45deg); }
```

---

## 多重变换

**基本写法：链式组合**
`transform: <函数1> <函数2> ...;`
```css
/* 从右向左依次应用 */
.box { transform: translate(50px, 0) rotate(45deg); }
.box { transform: scale(1.2) rotateY(30deg) translateZ(50px); }
```

---

## 3D 上下文属性

**基本写法：父级透视**
`perspective: <距离>;`
```css
/* 设置在父元素上，作用于所有子元素的 3D 变换 */
.scene { perspective: 800px; }
.scene .box { transform: rotateY(45deg); }
```

---

**基本写法：透视原点**
`perspective-origin: <x> <y>;`
```css
/* 控制消失点位置 */
.scene { perspective: 800px; perspective-origin: center top; }
.scene { perspective-origin: 25% 75%; }
```

---

**基本写法：变换原点**
`transform-origin: <x> <y> [<z>];`
```css
/* 设置变换中心点 */
.box { transform-origin: center center; }    /* 默认 */
.box { transform-origin: top left; }
.box { transform-origin: 50% 100%; }
.box { transform-origin: 0 0 100px; }        /* 含 Z 轴 */
```

---

**基本写法：变换样式**
`transform-style: flat | preserve-3d;`
```css
/* preserve-3d 让子元素保留 3D 位置 */
.parent { transform-style: preserve-3d; }
```

---

**基本写法：背面可见性**
`backface-visibility: visible | hidden;`
```css
/* 翻转卡片背面隐藏 */
.card { backface-visibility: hidden; }
.back { transform: rotateY(180deg); }
```

---

## 单独变换属性

**基本写法：独立 transform 属性**
`translate: <tx> <ty>;` `rotate: <角度>;` `scale: <sx> <sy>;`
```css
/* 不影响其他变换，便于动画 */
.box { translate: 50px 20px; }
.box { rotate: 45deg; }
.box { scale: 1.2; }
/* 三者独立于 transform，可分别动画化 */
```

---

## 注意事项速查

**基本写法：GPU 加速提示**
`transform: translateZ(0);`
```css
/* 触发 GPU 层提升，常用于性能优化 */
.box { will-change: transform; transform: translateZ(0); }
```

---

**基本写法：变换不影响文档流**
`transform: <函数>`
```css
/* transform 不影响周围元素布局，仅视觉变换 */
.box { transform: rotate(10deg); }  /* 相邻元素不重排 */
```



<!-- ============ 文档分隔线：007-css/026-ContainerQuery.md ============ -->

# CSS 容器查询语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 建立容器上下文

**基本写法：声明查询容器**
`container-type: <size|inline-size|normal>;`
```css
/* 设置元素为查询容器 */
.sidebar { container-type: inline-size; }
.card-wrap { container-type: size; }
/* size：可查宽高；inline-size：仅查行向（最常用）；normal：非尺寸容器 */
```

---

**基本写法：命名容器**
`container-name: <名称>;`
```css
/* 给容器命名以便精确查询 */
.layout { container-type: inline-size; container-name: layout; }
.sidebar { container-type: inline-size; container-name: sidebar; }
```

---

**基本写法：容器简写**
`container: <名称> / <类型>;`
```css
/* 一次声明名称与类型 */
.layout { container: layout / inline-size; }
.anon { container: inline-size; }   /* 仅类型，匿名容器 */
```

---

## 容器查询

**基本写法：基本查询**
`@container (<条件>) { ... }`
```css
/* 查询最近的祖先容器 */
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

---

**基本写法：命名容器查询**
`@container <名称> (<条件>) { ... }`
```css
/* 指定查询某个命名容器 */
.sidebar { container-type: inline-size; container-name: sidebar; }
@container sidebar (min-width: 300px) {
  .menu { display: flex; }
}
```

---

**基本写法：范围查询**
`@container (<min-width>) and (<max-width>)`
```css
/* 多条件组合 */
@container (min-width: 400px) and (max-width: 800px) {
  .card { padding: 20px; }
}
```

---

**基本写法：方向查询**
`@container (orientation: <landscape|portrait>)`
```css
/* 按容器方向应用样式 */
@container (orientation: landscape) {
  .media { flex-direction: row; }
}
```

---

**基本写法：高度查询**
`@container (<min-height>)`
```css
/* 需要 container-type: size 才能查 block 方向 */
.hero { container-type: size; }
@container (min-height: 500px) {
  .hero-title { font-size: 4rem; }
}
```

---

## 容器查询单位

**基本写法：容器相对单位**
`<值><cqw|cqh|cqi|cqb|cqmin|cqmax>`
```css
/* 单位速查 */
/* cqw    容器宽度的 1%        */
/* cqh    容器高度的 1%        */
/* cqi    容器内联尺寸的 1%    */
/* cqb    容器块尺寸的 1%      */
/* cqmin  cqi 与 cqb 较小者    */
/* cqmax  cqi 与 cqb 较大者    */
.title { font-size: clamp(1rem, 5cqi, 3rem); }
.gap { margin: 2cqi; }
```

---

## 样式查询

**基本写法：按自定义属性查询**
`@container style(<属性>: <值>)`
```css
/* 根据容器自定义属性应用样式 */
.theme { container-type: normal; container-name: theme; --theme: dark; }
@container theme style(--theme: dark) {
  .card { background: #222; color: #eee; }
}
```

---

**基本写法：按计算样式查询**
`@container style(<属性>: <值>)`
```css
/* 查询容器计算后的样式值 */
.card-wrap { container-name: card; }
@container card style(font-size: 1.5rem) {
  .title { font-weight: 700; }
}
```

---

## 逻辑组合

**基本写法：and / or / not**
`@container (<条件>) and (<条件>) { ... }`
```css
/* 多条件逻辑 */
@container (min-width: 400px) and (orientation: landscape) {
  .card { display: grid; grid-template-columns: 2fr 1fr; }
}

@container (max-width: 200px) or (orientation: portrait) {
  .card { flex-direction: column; }
}

@container not (min-width: 400px) {
  .card { font-size: 0.9rem; }
}
```

---

## 媒体查询与容器查询对比

**基本写法：视口 vs 容器**
```css
/* 媒体查询：基于视口 */
@media (min-width: 768px) {
  .card { flex-direction: row; }
}

/* 容器查询：基于父容器，组件更可复用 */
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

---

## 注意事项速查

**基本写法：size 容器需显式高度**
`container-type: size;`
```css
/* size 类型不能从子元素推导高度，否则高度坍缩 */
.hero {
  container-type: size;
  height: 100vh;   /* 必须显式设置高度 */
}
```

---

**基本写法：容器查询后代选择器**
```css
/* @container 内的规则作用于容器后代 */
.card-wrap { container-type: inline-size; }
@container (min-width: 400px) {
  .card .title { font-size: 1.5rem; }
  .card .body { padding: 16px; }
}
```



<!-- ============ 文档分隔线：007-css/027-ScopeAtRule.md ============ -->

# CSS @scope 规则语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础语法

**基本写法：定义作用域**
`@scope (<根选择器>) { <规则集> }`
```css
/* 样式仅作用于 .card 子树内 */
@scope (.card) {
  p { color: gray; }
  img { border-radius: 8px; }
}
```

---

**基本写法：甜甜圈作用域（带上限）**
`@scope (<根>) to (<下限>) { <规则集> }`
```css
/* 上界 .article-body，下界 figure，中间区域生效 */
@scope (.article-body) to (figure) {
  img { border: 5px solid black; }
}
/* figure 内部的 img 不受影响，形成"甜甜圈洞" */
```

---

**基本写法：行内 @scope（省略前导）**
```html
<!-- <style> 内的 @scope 自动以父元素为根 -->
<parent-element>
  <style>
    @scope {
      p { color: red; }   <!-- 仅作用于 parent-element 内 -->
    }
  </style>
</parent-element>
```

---

## 多根作用域

**基本写法：多根选择器列表**
`@scope (<根1>, <根2>) { <规则集> }`
```css
/* 多个根共享同一组规则 */
@scope (.mike, .jane) {
  p { color: grey; }
}
```

---

**基本写法：多下限选择器**
`@scope (<根>) to (<下限1>, <下限2>) { <规则集> }`
```css
/* 多个下限同时排除 */
@scope (.article) to (.ad, .quote) {
  p { line-height: 1.6; }
}
```

---

## :scope 伪类

**基本写法：引用作用域根**
`:scope`
```css
/* :scope 指向 @scope 的根元素本身 */
@scope (.card) {
  :scope { padding: 16px; }       /* 等价 .card { padding: 16px; } */
  :scope > h2 { margin-top: 0; }  /* .card 的直接 h2 */
}
```

---

**基本写法：:scope 提升优先级**
```css
/* 普通选择器优先级 0-0-1，加 :scope 后为 0-1-1 */
@scope (.card) {
  img { /* 0-0-1 */ }
  :scope img { /* 0-1-1，优先级更高 */ }
}
```

---

## 作用域与嵌套

**基本写法：在 @scope 中嵌套**
```css
/* @scope 内可使用原生嵌套 */
@scope (.card) {
  & { padding: 16px; }
  & .title { font-weight: bold; }
  & :hover { background: #fafafa; }
}
```

---

**基本写法：@scope 嵌套到规则中**
```css
/* 在组件样式块内声明 @scope */
.card {
  color: black;
  @scope (&) to (& .legacy) {
    p { color: inherit; }
  }
}
```

---

## 级联与优先级

**基本写法：作用域邻近性**
```css
/* 当多个 @scope 都匹配时，DOM 距离更近的根胜出 */
/* 级联顺序：来源 > 重要性 > 层级 > 作用域邻近性 > 优先级 > 顺序 */
@scope (.outer) { h3 { color: red; } }
@scope (.inner) { h3 { color: blue; } }   /* 胜出（更近） */
```

---

**基本写法：与 @layer 组合**
```css
/* @scope 可置于层内 */
@layer components {
  @scope (.card) {
    .title { font-size: 1.2rem; }
  }
}
```

---

## 注意事项速查

**基本写法：选择器隔离而非样式隔离**
`@scope (<根>) { <规则> }`
```css
/* @scope 限制选择器匹配范围，但不阻止继承 */
@scope (.card) {
  p { color: red; }   /* 仅匹配 .card 内的 p */
}
/* 父元素继承的样式仍会作用到 .card 内 */
```

---

**基本写法：@scope 不影响自身之外的元素**
```css
/* 避免全局污染 */
p { color: black; }              /* 全局 */
@scope (.special) {
  p { color: red; }              /* 仅 .special 内 */
}
.special 外的 p 仍是黑色
```



<!-- ============ 文档分隔线：007-css/028-CSSNesting.md ============ -->

# CSS 原生嵌套语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础嵌套

**基本写法：子代选择器嵌套**
```css
/* 子选择器直接写在父规则内 */
.card {
  background: white;

  .title {
    font-weight: bold;
  }

  .body {
    padding: 15px;
  }
}
/* 等价于 .card { } .card .title { } .card .body { } */
```

---

**基本写法：& 嵌套选择器**
`&`
```css
/* & 代表父选择器，用于复合或附加 */
.button {
  background: blue;
  &:hover { background: darkblue; }       /* .button:hover */
  &.primary { border-color: navy; }       /* .button.primary */
  & > span { font-weight: bold; }         /* .button > span */
}
```

---

**基本写法：& 用于伪类伪元素**
```css
.link {
  color: blue;
  &:hover { color: darkblue; }
  &:focus-visible { outline: 2px solid; }
  &::before { content: "›"; }
}
```

---

## 嵌套使用场景

**基本写法：组合选择器**
`&<复合>`
```css
/* 父子复合（无空格） */
.card {
  &.active { border-color: green; }
  &[disabled] { opacity: 0.5; }
  &:nth-child(2n) { background: #f5f5f5; }
}
```

---

**基本写法：后代选择器（不带 &）**
```css
/* 不带 & 时自动加空格，作用于后代 */
.navbar {
  .brand { font-weight: bold; }
  .links { margin-left: auto; }
  .links .link { padding: 0 15px; }
}
```

---

**基本写法：& 后置反转上下文**
`<选择器> &`
```css
/* 把 & 放后面，反转父子关系 */
.card {
  .dark-theme & {
    background: #333;
    color: #eee;
  }
}
/* 等价 .dark-theme .card { } */
```

---

**基本写法：多次使用 &**
```css
/* & 可在嵌套选择器中多次出现 */
.button {
  & + & { margin-left: 8px; }      /* 相邻兄弟 button */
  & ~ & { opacity: 0.8; }
}
```

---

## 嵌套 at 规则

**基本写法：嵌套 @media**
```css
/* 媒体查询直接写在组件规则内 */
.navbar {
  display: flex;

  @media (max-width: 768px) {
    display: block;
    .links { display: none; }
  }

  @media (prefers-color-scheme: dark) {
    background: #222;
  }
}
```

---

**基本写法：嵌套 @supports / @container**
```css
.card {
  @supports (backdrop-filter: blur(10px)) {
    backdrop-filter: blur(10px);
  }

  @container (min-width: 400px) {
    flex-direction: row;
  }
}
```

---

## 混合声明与规则

**基本写法：声明与嵌套混合**
```css
/* 属性声明与嵌套规则可同时存在 */
.card {
  background: white;        /* 属性 */
  border-radius: 8px;

  .title { font-weight: bold; }   /* 嵌套规则 */
  &:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
}
```

---

## 注意事项速查

**基本写法：HTML 元素需用 & 前缀（旧浏览器兼容）**
```css
/* 标签选择器嵌套建议加 &，兼容 Safari 17.2 之前 */
.box {
  & h2 { color: red; }    /* 推荐：所有浏览器支持 */
  /* h2 { color: red; } */ /* Safari 17.1 及之前可能无效 */
}

/* class / id 嵌套无需 & */
.box {
  .title { color: red; }  /* 兼容性好 */
}
```

---

**基本写法：避免过度嵌套**
```css
/* 不推荐：嵌套过深 */
.card {
  .body {
    .content {
      .item {
        .title { color: red; }   /* 4 层，难以覆盖 */
      }
    }
  }
}

/* 推荐：保持 2-3 层，配合 BEM 或扁平选择器 */
.card .item .title { color: red; }
```

---

**基本写法：& 不能代表伪元素**
```css
/* & 类似 :is()，不能表示 ::before/::after */
.parent {
  &::before { content: ""; }      /* 正确：直接写伪元素 */
  /* .child &::before 会被忽略，因 :is() 不支持伪元素 */
}
```



<!-- ============ 文档分隔线：007-css/029-ModernColorSpace.md ============ -->

# CSS 现代色彩空间语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## oklch / oklab 感知均匀色彩

**基本写法：oklch 颜色**
`oklch(<L> <C> <H> [, <alpha>])`
```css
/* L 亮度 0%-100% / 0-1；C 色度 0+；H 色相 0-360 */
.brand {
  color: oklch(60% 0.15 250);          /* 蓝色调 */
  background: oklch(95% 0.02 250);     /* 浅背景 */
  border-color: oklch(50% 0.2 250 / 0.5); /* 带透明度 */
}
```

---

**基本写法：oklab 颜色**
`oklab(<L> <a> <b> [, <alpha>])`
```css
/* 直角坐标形式，a 红-绿轴，b 黄-蓝轴 */
.brand {
  color: oklab(60% 0.1 0.1);
  background: oklab(95% 0 0);   /* 接近中性灰 */
}
```

---

**基本写法：lab / lch 颜色**
`lab(<L> <a> <b> [, <alpha>])`
```css
/* CIE Lab/Lch 色彩空间 */
.brand {
  color: lab(60% 40 30);
  color: lch(60% 50 250);        /* Lch 极坐标形式 */
}
```

---

## 宽色域 color()

**基本写法：display-p3 广色域**
`color(<色彩空间> <R> <G> <B> [, <alpha>])`
```css
/* 超出 sRGB 的鲜艳颜色 */
.vivid {
  color: color(display-p3 1 0 0);          /* 鲜红，sRGB 无法表达 */
  background: color(display-p3 0 1 0);
  border-color: color(display-p3 0 0 1 / 0.5);
}

/* 其他色彩空间 */
.rec2020 { color: color(rec2020 0.8 0.2 0.1); }
.srgb-linear { color: color(srgb-linear 0.5 0.5 0.5); }
```

---

## color-mix() 颜色混合

**基本写法：基本混合**
`color-mix(in <色彩空间>, <颜色1> [<百分比>], <颜色2> [<百分比>])`
```css
/* 在 oklch 中混合红蓝各 50% */
.brand {
  color: color-mix(in oklch, red, blue);
  background: color-mix(in srgb, plum, #f00);
}
```

---

**基本写法：指定百分比**
`color-mix(in <空间>, <颜色> <p1>, <颜色> <p2>)`
```css
/* 60% 红 + 40% 蓝 */
.brand {
  color: color-mix(in oklab, red 60%, blue 40%);
  /* 比例之和可不为 100%，会自动归一化 */
  color: color-mix(in oklch, red 70%, blue 50%);  /* 归一化为 58.3%/41.7% */
}
```

---

**基本写法：极坐标色相插值**
`color-mix(in <极坐标空间> <hue 方法>, <颜色>, <颜色>)`
```css
/* hue 插值方法：shorter / longer / increasing / decreasing */
.brand {
  color: color-mix(in oklch shorter hue, blue, yellow);
  color: color-mix(in lch longer hue, orange, purple);
  color: color-mix(in hsl increasing hue, red, green);
}
```

---

**基本写法：混合生成派生色**
`color-mix(in <空间>, <基色>, <黑|白> <百分比>)`
```css
/* 从主色派生明暗变体 */
:root {
  --brand: oklch(60% 0.2 250);
  --brand-dark:  color-mix(in srgb, var(--brand), black 70%);
  --brand-light: color-mix(in srgb, var(--brand), white 70%);
  --brand-hover: color-mix(in oklch, var(--brand), white 15%);
}
```

---

## 相对颜色语法

**基本写法：从原色派生**
`oklch(from <原色> <L> <C> <H> [, <alpha>])`
```css
/* from 关键字基于已有颜色派生 */
:root {
  --brand: oklch(60% 0.2 250);
  --brand-soft: oklch(from var(--brand) calc(l + 0.1) c h);   /* 提亮 10% */
  --brand-deep: oklch(from var(--brand) calc(l - 0.2) c h);   /* 加深 */
  --brand-muted: oklch(from var(--brand) l calc(c * 0.5) h);  /* 降饱和 */
}
```

---

**基本写法：rgb 相对颜色**
`rgb(from <原色> <R> <G> <B> [, <A>])`
```css
/* 通道变量 r g b / alpha */
.btn {
  --base: #3366cc;
  background: rgb(from var(--base) r g b / 0.5);     /* 仅改透明度 */
  border-color: rgb(from var(--base) calc(r * 0.7) calc(g * 0.7) calc(b * 0.7));
}
```

---

## light-dark() 明暗模式

**基本写法：自动跟随配色**
`light-dark(<亮色>, <暗色>)`
```css
/* 依据 prefers-color-scheme 自动切换 */
:root { color-scheme: light dark; }
.text {
  color: light-dark(#333, #eee);                       /* 亮/暗自动切换 */
  background: light-dark(white, oklch(20% 0.01 250));
  border-color: light-dark(#ccc, #444);
}
```

---

## color-contrast() 对比色

**基本写法：选择最高对比色**
`color-contrast(<背景色> vs <候选1>, <候选2>, ...)`
```css
/* 浏览器自动选择与背景对比度达标的颜色 */
.badge {
  background: #f60;
  color: color-contrast(#f60 vs white, black);   /* 选 black */
}
```

---

## 注意事项速查

**基本写法：oklch 的感知均匀性**
`oklch(<L> <C> <H>)`
```css
/* 同样 L 值不同色相视觉亮度一致，适合生成色阶 */
:root {
  --c-50:  oklch(95% 0.02 250);
  --c-100: oklch(88% 0.06 250);
  --c-500: oklch(60% 0.18 250);
  --c-900: oklch(28% 0.10 250);
}
/* HSL 的 L 不具备此特性，视觉亮度会随色相波动 */
```

---

**基本写法：色彩空间互转**
`color-mix(in <目标空间>, <原色> 100%, <原色> 0%)`
```css
/* 技巧：用 color-mix 把颜色转换到目标色彩空间 */
.converted {
  color: color-mix(in oklch, var(--some-hex) 100%, transparent);
}
```
