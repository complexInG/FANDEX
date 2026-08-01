---
order: 110
title: 'SVG 裁剪与蒙版'
module: svg
category: 'SVG Effects'
difficulty: advanced
description: 'clipPath 硬裁剪、mask 软蒙版、 luminance 与 alpha 蒙版技巧。'
author: fanquanpp
updated: '2026-08-01'
related:
  - svg/滤镜详解
  - svg/渐变与图案
  - svg/变换transform
prerequisites:
  - svg/滤镜详解
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《SVG 裁剪与蒙版》，属于 SVG 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 SVG 的核心概念、术语与标准写法。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 SVG 的工作原理与设计动机。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写符合 SVG 规范的完整实现。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 SVG 与相邻方案的差异与边界。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据场景评价 SVG 相关方案的优劣。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 SVG 与其他技术设计完整方案。

通过本节学习，读者应当能够把《SVG 裁剪与蒙版》纳入自己的知识网络，并与 SVG 模块的其他主题（矢量图形、路径、变换、动画）建立关联。

## 2. 历史动机与发展脉络

《SVG 裁剪与蒙版》是 SVG 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

SVG（可缩放矢量图形）于 2001 年由 W3C 标准化，是 Web 原生矢量格式；与位图不同，SVG 由几何描述构成，任意缩放不失真。
SVG 是 XML 方言：元素即图形（rect/circle/path），样式可用 CSS，交互可用事件；SPA 生态中常以内联 SVG 与图标组件使用。
现代应用：图标系统、数据可视化（D3）、地图、LOGO、动画与交互图形；浏览器对 SVG 的支持已非常完整。

回到本文主题：SVG 裁剪与蒙版 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《SVG 裁剪与蒙版》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

坐标系：viewBox 定义逻辑坐标（min-x min-y width height），preserveAspectRatio 控制缩放对齐。
基本图形：rect（矩形）、circle（圆）、ellipse（椭圆）、line（直线）、polyline/polygon（折线/多边形）。
路径 path：M/L/C/Q/A 命令组合任意曲线；fill 填充、stroke 描边。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 23 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# SVG 裁剪与蒙版 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. clipPath 裁剪路径

`<clipPath>` 定义硬裁剪区域，区域外的内容完全不显示（无过渡）。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle-clip">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
  </defs>
  <!-- 图像只在圆形区域内可见 -->
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
  <!-- 矩形被裁成圆形 -->
  <image href="photo.jpg" x="0" y="0" width="200" height="200" clip-path="url(#circle-clip)" />
</svg>
```

##### 1.1 clipPathUnits 坐标系

| 值                       | 说明                          |
| ------------------------ | ----------------------------- |
| `userSpaceOnUse`（默认） | 使用 SVG 用户坐标系           |
| `objectBoundingBox`      | 相对于应用元素的边界框（0-1） |

```html
<clipPath id="half" clipPathUnits="objectBoundingBox">
  <rect x="0" y="0" width="0.5" height="1" />
</clipPath>
<!-- 任意元素应用此裁剪，都只显示左半部分 -->
<rect width="100" height="100" clip-path="url(#half)" />
<circle cx="50" cy="50" r="30" clip-path="url(#half)" />
```

##### 1.2 文字裁剪

```html
<svg viewBox="0 0 400 100">
  <defs>
    <clipPath id="text-mask">
      <text x="200" y="70" text-anchor="middle" font-size="80" font-weight="bold">FANDEX</text>
    </clipPath>
  </defs>
  <!-- 渐变填充文字（通过裁剪实现） -->
  <rect width="400" height="100" fill="url(#rainbow)" clip-path="url(#text-mask)" />
</svg>
```

##### 1.3 多形状裁剪

```html
<clipPath id="holes">
  <circle cx="50" cy="50" r="30" />
  <circle cx="150" cy="50" r="30" />
  <circle cx="250" cy="50" r="30" />
</clipPath>
<rect width="300" height="100" fill="#4f5bd5" clip-path="url(#holes)" />
<!-- 出现三个圆形填充 -->
```

#### 2. mask 蒙版

`<mask>` 通过亮度或 alpha 通道实现软蒙版，灰度区域形成半透明效果。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <mask id="fade">
      <linearGradient id="fade-grad" x1="0%" x2="100%">
        <stop offset="0%" stop-color="#fff" />
        <stop offset="100%" stop-color="#000" />
      </linearGradient>
      <rect width="200" height="200" fill="url(#fade-grad)" />
    </mask>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
  <!-- 左侧不透明，右侧透明，形成渐隐效果 -->
</svg>
```

##### 2.1 蒙版颜色规则

| 蒙版颜色     | 效果     |
| ------------ | -------- |
| `#fff`（白） | 完全显示 |
| `#000`（黑） | 完全隐藏 |
| `#888`（灰） | 半透明   |
| 渐变白→黑    | 渐隐     |

##### 2.2 maskUnits / maskContentUnits

| 属性               | 说明                                      |
| ------------------ | ----------------------------------------- |
| `maskUnits`        | mask 区域坐标系（默认 objectBoundingBox） |
| `maskContentUnits` | 蒙版内容坐标系（默认 userSpaceOnUse）     |

```html
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
  <rect width="200" height="200" fill="#fff" />
</mask>
```

##### 2.3 mask-type 蒙版类型

```html
<mask id="alpha-mask" mask-type="alpha">
  <rect fill="rgba(255,255,255,0.5)" />
</mask>

<mask id="luma-mask" mask-type="luminance">
  <rect fill="#fff" />
</mask>
```

| 值                  | 说明                      |
| ------------------- | ------------------------- |
| `luminance`（默认） | 根据亮度计算透明度        |
| `alpha`             | 根据 alpha 通道计算透明度 |

#### 3. clipPath vs mask 对比

| 维度     | clipPath               | mask                     |
| -------- | ---------------------- | ------------------------ |
| 边缘     | 硬边（无过渡）         | 软边（可渐变）           |
| 计算依据 | 几何形状               | 像素亮度/alpha           |
| 半透明   | 不支持                 | 支持                     |
| 性能     | 较优                   | 较重                     |
| 典型场景 | 头像圆形裁剪、文字镂空 | 渐隐、淡入淡出、复杂透明 |

#### 4. 圆形头像

```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <clipPath id="avatar">
      <circle cx="50" cy="50" r="48" />
    </clipPath>
  </defs>
  <image href="avatar.jpg" x="0" y="0" width="100" height="100" clip-path="url(#avatar)" />
  <circle cx="50" cy="50" r="48" fill="none" stroke="#4f5bd5" stroke-width="2" />
</svg>
```

#### 5. 渐隐遮罩

```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="vignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="band">
      <rect width="400" height="200" fill="url(#vignette)" />
    </mask>
  </defs>
  <rect width="400" height="200" fill="#4f5bd5" mask="url(#band)" />
  <!-- 上下渐隐，中间可见 -->
</svg>
```

#### 6. 文字渐变蒙版

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="rainbow" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#d63031" />
      <stop offset="25%" stop-color="#f9a825" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="75%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#8854d0" />
    </linearGradient>
    <mask id="text">
      <rect width="400" height="100" fill="#000" />
      <text
        x="200"
        y="70"
        text-anchor="middle"
        font-size="60"
        font-weight="bold"
        fill="#fff"
        font-family="sans-serif"
      >
        FANDEX
      </text>
    </mask>
  </defs>
  <rect width="400" height="100" fill="url(#rainbow)" mask="url(#text)" />
</svg>
```

**原理**：

- mask 黑色背景 = 隐藏
- 白色文字 = 显示
- 渐变 rect 通过 mask 只显示文字形状

#### 7. 反射倒影

```html
<svg viewBox="0 0 200 200">
  <defs>
    <linearGradient id="reflect-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#fff" stop-opacity="0" />
    </linearGradient>
    <mask id="reflect">
      <rect y="100" width="200" height="100" fill="url(#reflect-grad)" />
    </mask>
  </defs>
  <!-- 原图 -->
  <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  <!-- 倒影 -->
  <g transform="translate(0, 200) scale(1, -1)" mask="url(#reflect)" opacity="0.6">
    <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  </g>
</svg>
```

**原理**：

- `scale(1, -1)` 垂直翻转
- mask 渐变让倒影从顶部半透明到底部全透明

#### 8. clipPath 动画

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="reveal">
      <rect x="0" y="0" width="0" height="200">
        <animate attributeName="width" from="0" to="200" dur="2s" fill="freeze" />
      </rect>
    </clipPath>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#reveal)" />
</svg>
```

形成"从左到右揭开"动画效果。

#### 9. mask 动画

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="sweep" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="40%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="60%" stop-color="#000" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="sweep-mask">
      <rect width="400" height="100" fill="url(#sweep)">
        <animateTransform
          attributeName="transform"
          type="translate"
          from="-200 0"
          to="400 0"
          dur="3s"
          repeatCount="indefinite"
        />
      </rect>
    </mask>
  </defs>
  <text
    x="200"
    y="65"
    text-anchor="middle"
    font-size="40"
    font-weight="bold"
    fill="#4f5bd5"
    mask="url(#sweep-mask)"
  >
    FANDEX
  </text>
</svg>
```

形成"光带扫过文字"效果，常用于加载或强调动画。

#### 10. 多重裁剪

clipPath 与 mask 可同时应用，clipPath 先裁剪，mask 再蒙版。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <linearGradient id="fade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="bottom-fade">
      <rect width="200" height="200" fill="url(#fade)" />
    </mask>
  </defs>
  <image
    href="photo.jpg"
    width="200"
    height="200"
    clip-path="url(#circle)"
    mask="url(#bottom-fade)"
  />
  <!-- 先裁成圆形，再让底部渐隐 -->
</svg>
```

#### 11. 实战：粒子头像

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="avatar">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <radialGradient id="ring-grad" cx="50%" cy="50%" r="50%">
      <stop offset="80%" stop-color="#000" stop-opacity="0" />
      <stop offset="100%" stop-color="#4f5bd5" stop-opacity="1" />
    </radialGradient>
    <mask id="ring">
      <rect width="200" height="200" fill="url(#ring-grad)" />
    </mask>
  </defs>
  <!-- 头像主体 -->
  <image href="avatar.jpg" x="20" y="20" width="160" height="160" clip-path="url(#avatar)" />
  <!-- 外圈光环 -->
  <circle cx="100" cy="100" r="90" fill="#4f5bd5" mask="url(#ring)" />
</svg>
```

#### 12. 性能建议

| 优化           | 说明                               |
| -------------- | ---------------------------------- |
| 优先 clipPath  | 硬裁剪性能优于软蒙版               |
| 缩小 mask 区域 | mask x/y/width/height 限制计算范围 |
| 避免大图蒙版   | 高分辨率图像 + mask 会显著拖慢渲染 |
| 缓存复用       | 多个元素复用同一 mask 定义         |

下一篇介绍 symbol/use 的图形复用机制。
#### clipPath 裁剪路径

**clipPath 硬裁剪区域**
`<clipPath id="<id>" [clipPathUnits="<坐标系>"]><裁剪形状></clipPath>`
```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle-clip">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
  <image href="photo.jpg" x="0" y="0" width="200" height="200" clip-path="url(#circle-clip)" />
</svg>
```

##### clipPathUnits 坐标系

| 值                       | 说明                          |
| ------------------------ | ----------------------------- |
| `userSpaceOnUse`(默认) | 使用 SVG 用户坐标系           |
| `objectBoundingBox`      | 相对于应用元素的边界框(0-1) |

**objectBoundingBox 相对坐标系**
```html
<clipPath id="half" clipPathUnits="objectBoundingBox">
  <rect x="0" y="0" width="0.5" height="1" />
</clipPath>
<rect width="100" height="100" clip-path="url(#half)" />
<circle cx="50" cy="50" r="30" clip-path="url(#half)" />
```

##### 文字裁剪

**text 作为裁剪形状**
```html
<svg viewBox="0 0 400 100">
  <defs>
    <clipPath id="text-mask">
      <text x="200" y="70" text-anchor="middle" font-size="80" font-weight="bold">FANDEX</text>
    </clipPath>
  </defs>
  <rect width="400" height="100" fill="url(#rainbow)" clip-path="url(#text-mask)" />
</svg>
```

##### 多形状裁剪

**clipPath 包含多个形状**
```html
<clipPath id="holes">
  <circle cx="50" cy="50" r="30" />
  <circle cx="150" cy="50" r="30" />
  <circle cx="250" cy="50" r="30" />
</clipPath>
<rect width="300" height="100" fill="#4f5bd5" clip-path="url(#holes)" />
```

##### clip-path 应用属性

**clip-path 引用裁剪路径**
`clip-path="url(#<clipPath-id>)"`
```html
<rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
```

---

#### mask 蒙版

**mask 软蒙版**
`<mask id="<id>" [maskUnits="<区域坐标系>"] [maskContentUnits="<内容坐标系>"] [mask-type="<类型>"] [x="<x>"] [y="<y>"] [width="<w>"] [height="<h>"]><蒙版内容></mask>`
```html
<svg viewBox="0 0 200 200">
  <defs>
    <mask id="fade">
      <linearGradient id="fade-grad" x1="0%" x2="100%">
        <stop offset="0%" stop-color="#fff" />
        <stop offset="100%" stop-color="#000" />
      </linearGradient>
      <rect width="200" height="200" fill="url(#fade-grad)" />
    </mask>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
</svg>
```

##### 蒙版颜色规则

| 蒙版颜色     | 效果     |
| ------------ | -------- |
| `#fff`(白) | 完全显示 |
| `#000`(黑) | 完全隐藏 |
| `#888`(灰) | 半透明   |
| 渐变白->黑  | 渐隐     |

##### maskUnits / maskContentUnits

| 属性               | 说明                                       |
| ------------------ | ------------------------------------------ |
| `maskUnits`        | mask 区域坐标系(默认 objectBoundingBox)  |
| `maskContentUnits` | 蒙版内容坐标系(默认 userSpaceOnUse)      |

**userSpaceOnUse 区域显式声明**
```html
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
  <rect width="200" height="200" fill="#fff" />
</mask>
```

##### mask-type 蒙版类型

**mask-type 指定蒙版计算方式**
`mask-type="<luminance | alpha>"`
```html
<mask id="alpha-mask" mask-type="alpha">
  <rect fill="rgba(255,255,255,0.5)" />
</mask>

<mask id="luma-mask" mask-type="luminance">
  <rect fill="#fff" />
</mask>
```

| 值                  | 说明                      |
| ------------------- | ------------------------- |
| `luminance`(默认) | 根据亮度计算透明度        |
| `alpha`             | 根据 alpha 通道计算透明度 |

##### mask 应用属性

**mask 引用蒙版**
`mask="url(#<mask-id>)"`
```html
<rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
```

---

#### clipPath 与 mask 对比

| 维度     | clipPath               | mask                     |
| -------- | ---------------------- | ------------------------ |
| 边缘     | 硬边(无过渡)         | 软边(可渐变)           |
| 计算依据 | 几何形状               | 像素亮度/alpha           |
| 半透明   | 不支持                 | 支持                     |
| 典型场景 | 头像圆形裁剪、文字镂空 | 渐隐、淡入淡出、复杂透明 |

---

#### 圆形头像裁剪

**clipPath 圆形头像**
```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <clipPath id="avatar">
      <circle cx="50" cy="50" r="48" />
    </clipPath>
  </defs>
  <image href="avatar.jpg" x="0" y="0" width="100" height="100" clip-path="url(#avatar)" />
  <circle cx="50" cy="50" r="48" fill="none" stroke="#4f5bd5" stroke-width="2" />
</svg>
```

---

#### 渐隐遮罩

**linearGradient + mask 上下渐隐**
```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="vignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="band">
      <rect width="400" height="200" fill="url(#vignette)" />
    </mask>
  </defs>
  <rect width="400" height="200" fill="#4f5bd5" mask="url(#band)" />
</svg>
```

---

#### 文字渐变蒙版

**mask 实现文字渐变**
```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="rainbow" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#d63031" />
      <stop offset="25%" stop-color="#f9a825" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="75%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#8854d0" />
    </linearGradient>
    <mask id="text">
      <rect width="400" height="100" fill="#000" />
      <text
        x="200"
        y="70"
        text-anchor="middle"
        font-size="60"
        font-weight="bold"
        fill="#fff"
        font-family="sans-serif"
      >
        FANDEX
      </text>
    </mask>
  </defs>
  <rect width="400" height="100" fill="url(#rainbow)" mask="url(#text)" />
</svg>
```

蒙版规则:
- mask 黑色背景 = 隐藏
- 白色文字 = 显示
- 渐变 rect 通过 mask 只显示文字形状

---

#### 反射倒影

**mask + scale 实现倒影**
```html
<svg viewBox="0 0 200 200">
  <defs>
    <linearGradient id="reflect-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#fff" stop-opacity="0" />
    </linearGradient>
    <mask id="reflect">
      <rect y="100" width="200" height="100" fill="url(#reflect-grad)" />
    </mask>
  </defs>
  <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  <g transform="translate(0, 200) scale(1, -1)" mask="url(#reflect)" opacity="0.6">
    <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  </g>
</svg>
```

变换说明:
- `scale(1, -1)` 垂直翻转
- mask 渐变让倒影从顶部半透明到底部全透明

---

#### clipPath 动画

**animate 裁剪形状属性**
```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="reveal">
      <rect x="0" y="0" width="0" height="200">
        <animate attributeName="width" from="0" to="200" dur="2s" fill="freeze" />
      </rect>
    </clipPath>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#reveal)" />
</svg>
```

通过动画 clipPath 内 rect 的 width 实现"从左到右揭开"效果。

---

#### mask 动画

**animateTransform 扫光蒙版**
```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="sweep" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="40%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="60%" stop-color="#000" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="sweep-mask">
      <rect width="400" height="100" fill="url(#sweep)">
        <animateTransform
          attributeName="transform"
          type="translate"
          from="-200 0"
          to="400 0"
          dur="3s"
          repeatCount="indefinite"
        />
      </rect>
    </mask>
  </defs>
  <text
    x="200"
    y="65"
    text-anchor="middle"
    font-size="40"
    font-weight="bold"
    fill="#4f5bd5"
    mask="url(#sweep-mask)"
  >
    FANDEX
  </text>
</svg>
```

通过 mask 内元素的 animateTransform 实现"光带扫过文字"效果。

---

#### 多重裁剪

**clipPath 与 mask 同时应用**
```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <linearGradient id="fade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="bottom-fade">
      <rect width="200" height="200" fill="url(#fade)" />
    </mask>
  </defs>
  <image
    href="photo.jpg"
    width="200"
    height="200"
    clip-path="url(#circle)"
    mask="url(#bottom-fade)"
  />
</svg>
```

clipPath 先裁剪(限定为圆形区域),mask 再蒙版(底部渐隐)。

---

#### 综合示例:粒子头像

**clipPath + radialGradient mask 组合**
```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="avatar">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <radialGradient id="ring-grad" cx="50%" cy="50%" r="50%">
      <stop offset="80%" stop-color="#000" stop-opacity="0" />
      <stop offset="100%" stop-color="#4f5bd5" stop-opacity="1" />
    </radialGradient>
    <mask id="ring">
      <rect width="200" height="200" fill="url(#ring-grad)" />
    </mask>
  </defs>
  <image href="avatar.jpg" x="20" y="20" width="160" height="160" clip-path="url(#avatar)" />
  <circle cx="100" cy="100" r="90" fill="#4f5bd5" mask="url(#ring)" />
</svg>
```


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["SVG 裁剪与蒙版"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《SVG 裁剪与蒙版》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

坐标系：viewBox 定义逻辑坐标（min-x min-y width height），preserveAspectRatio 控制缩放对齐。
基本图形：rect（矩形）、circle（圆）、ellipse（椭圆）、line（直线）、polyline/polygon（折线/多边形）。
路径 path：M/L/C/Q/A 命令组合任意曲线；fill 填充、stroke 描边。
变换与动画：transform 平移缩放旋转；CSS/SMIL 动画控制属性过渡。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1. clipPath 裁剪路径

该示例来自原文《1. clipPath 裁剪路径》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle-clip">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
  </defs>
  <!-- 图像只在圆形区域内可见 -->
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
  <!-- 矩形被裁成圆形 -->
  <image href="photo.jpg" x="0" y="0" width="200" height="200" clip-path="url(#circle-clip)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：1.1 clipPathUnits 坐标系

该示例来自原文《1.1 clipPathUnits 坐标系》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<clipPath id="half" clipPathUnits="objectBoundingBox">
  <rect x="0" y="0" width="0.5" height="1" />
</clipPath>
<!-- 任意元素应用此裁剪，都只显示左半部分 -->
<rect width="100" height="100" clip-path="url(#half)" />
<circle cx="50" cy="50" r="30" clip-path="url(#half)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：1.2 文字裁剪

该示例来自原文《1.2 文字裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 100">
  <defs>
    <clipPath id="text-mask">
      <text x="200" y="70" text-anchor="middle" font-size="80" font-weight="bold">FANDEX</text>
    </clipPath>
  </defs>
  <!-- 渐变填充文字（通过裁剪实现） -->
  <rect width="400" height="100" fill="url(#rainbow)" clip-path="url(#text-mask)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：1.3 多形状裁剪

该示例来自原文《1.3 多形状裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<clipPath id="holes">
  <circle cx="50" cy="50" r="30" />
  <circle cx="150" cy="50" r="30" />
  <circle cx="250" cy="50" r="30" />
</clipPath>
<rect width="300" height="100" fill="#4f5bd5" clip-path="url(#holes)" />
<!-- 出现三个圆形填充 -->
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：2. mask 蒙版

该示例来自原文《2. mask 蒙版》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <mask id="fade">
      <linearGradient id="fade-grad" x1="0%" x2="100%">
        <stop offset="0%" stop-color="#fff" />
        <stop offset="100%" stop-color="#000" />
      </linearGradient>
      <rect width="200" height="200" fill="url(#fade-grad)" />
    </mask>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
  <!-- 左侧不透明，右侧透明，形成渐隐效果 -->
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：2.2 maskUnits / maskContentUnits

该示例来自原文《2.2 maskUnits / maskContentUnits》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
  <rect width="200" height="200" fill="#fff" />
</mask>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：2.3 mask-type 蒙版类型

该示例来自原文《2.3 mask-type 蒙版类型》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<mask id="alpha-mask" mask-type="alpha">
  <rect fill="rgba(255,255,255,0.5)" />
</mask>

<mask id="luma-mask" mask-type="luminance">
  <rect fill="#fff" />
</mask>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：4. 圆形头像

该示例来自原文《4. 圆形头像》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <clipPath id="avatar">
      <circle cx="50" cy="50" r="48" />
    </clipPath>
  </defs>
  <image href="avatar.jpg" x="0" y="0" width="100" height="100" clip-path="url(#avatar)" />
  <circle cx="50" cy="50" r="48" fill="none" stroke="#4f5bd5" stroke-width="2" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：5. 渐隐遮罩

该示例来自原文《5. 渐隐遮罩》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="vignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="band">
      <rect width="400" height="200" fill="url(#vignette)" />
    </mask>
  </defs>
  <rect width="400" height="200" fill="#4f5bd5" mask="url(#band)" />
  <!-- 上下渐隐，中间可见 -->
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：6. 文字渐变蒙版

该示例来自原文《6. 文字渐变蒙版》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="rainbow" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#d63031" />
      <stop offset="25%" stop-color="#f9a825" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="75%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#8854d0" />
    </linearGradient>
    <mask id="text">
      <rect width="400" height="100" fill="#000" />
      <text
        x="200"
        y="70"
        text-anchor="middle"
        font-size="60"
        font-weight="bold"
        fill="#fff"
        font-family="sans-serif"
      >
        FANDEX
      </text>
    </mask>
  </defs>
  <rect width="400" height="100" fill="url(#rainbow)" mask="url(#text)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 26 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：7. 反射倒影

该示例来自原文《7. 反射倒影》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <linearGradient id="reflect-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#fff" stop-opacity="0" />
    </linearGradient>
    <mask id="reflect">
      <rect y="100" width="200" height="100" fill="url(#reflect-grad)" />
    </mask>
  </defs>
  <!-- 原图 -->
  <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  <!-- 倒影 -->
  <g transform="translate(0, 200) scale(1, -1)" mask="url(#reflect)" opacity="0.6">
    <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  </g>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：8. clipPath 动画

该示例来自原文《8. clipPath 动画》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="reveal">
      <rect x="0" y="0" width="0" height="200">
        <animate attributeName="width" from="0" to="200" dur="2s" fill="freeze" />
      </rect>
    </clipPath>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#reveal)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：9. mask 动画

该示例来自原文《9. mask 动画》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="sweep" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="40%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="60%" stop-color="#000" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="sweep-mask">
      <rect width="400" height="100" fill="url(#sweep)">
        <animateTransform
          attributeName="transform"
          type="translate"
          from="-200 0"
          to="400 0"
          dur="3s"
          repeatCount="indefinite"
        />
      </rect>
    </mask>
  </defs>
  <text
    x="200"
    y="65"
    text-anchor="middle"
    font-size="40"
    font-weight="bold"
    fill="#4f5bd5"
    mask="url(#sweep-mask)"
  >
    FANDEX
  </text>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 34 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：10. 多重裁剪

该示例来自原文《10. 多重裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <linearGradient id="fade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="bottom-fade">
      <rect width="200" height="200" fill="url(#fade)" />
    </mask>
  </defs>
  <image
    href="photo.jpg"
    width="200"
    height="200"
    clip-path="url(#circle)"
    mask="url(#bottom-fade)"
  />
  <!-- 先裁成圆形，再让底部渐隐 -->
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：11. 实战：粒子头像

该示例来自原文《11. 实战：粒子头像》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="avatar">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <radialGradient id="ring-grad" cx="50%" cy="50%" r="50%">
      <stop offset="80%" stop-color="#000" stop-opacity="0" />
      <stop offset="100%" stop-color="#4f5bd5" stop-opacity="1" />
    </radialGradient>
    <mask id="ring">
      <rect width="200" height="200" fill="url(#ring-grad)" />
    </mask>
  </defs>
  <!-- 头像主体 -->
  <image href="avatar.jpg" x="20" y="20" width="160" height="160" clip-path="url(#avatar)" />
  <!-- 外圈光环 -->
  <circle cx="100" cy="100" r="90" fill="#4f5bd5" mask="url(#ring)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：clipPath 裁剪路径

该示例来自原文《clipPath 裁剪路径》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle-clip">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
  <image href="photo.jpg" x="0" y="0" width="200" height="200" clip-path="url(#circle-clip)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：clipPathUnits 坐标系

该示例来自原文《clipPathUnits 坐标系》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<clipPath id="half" clipPathUnits="objectBoundingBox">
  <rect x="0" y="0" width="0.5" height="1" />
</clipPath>
<rect width="100" height="100" clip-path="url(#half)" />
<circle cx="50" cy="50" r="30" clip-path="url(#half)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：文字裁剪

该示例来自原文《文字裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 100">
  <defs>
    <clipPath id="text-mask">
      <text x="200" y="70" text-anchor="middle" font-size="80" font-weight="bold">FANDEX</text>
    </clipPath>
  </defs>
  <rect width="400" height="100" fill="url(#rainbow)" clip-path="url(#text-mask)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：多形状裁剪

该示例来自原文《多形状裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<clipPath id="holes">
  <circle cx="50" cy="50" r="30" />
  <circle cx="150" cy="50" r="30" />
  <circle cx="250" cy="50" r="30" />
</clipPath>
<rect width="300" height="100" fill="#4f5bd5" clip-path="url(#holes)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：clip-path 应用属性

该示例来自原文《clip-path 应用属性》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：mask 蒙版

该示例来自原文《mask 蒙版》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <mask id="fade">
      <linearGradient id="fade-grad" x1="0%" x2="100%">
        <stop offset="0%" stop-color="#fff" />
        <stop offset="100%" stop-color="#000" />
      </linearGradient>
      <rect width="200" height="200" fill="url(#fade-grad)" />
    </mask>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：maskUnits / maskContentUnits

该示例来自原文《maskUnits / maskContentUnits》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
  <rect width="200" height="200" fill="#fff" />
</mask>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：mask-type 蒙版类型

该示例来自原文《mask-type 蒙版类型》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<mask id="alpha-mask" mask-type="alpha">
  <rect fill="rgba(255,255,255,0.5)" />
</mask>

<mask id="luma-mask" mask-type="luminance">
  <rect fill="#fff" />
</mask>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：mask 应用属性

该示例来自原文《mask 应用属性》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：圆形头像裁剪

该示例来自原文《圆形头像裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <clipPath id="avatar">
      <circle cx="50" cy="50" r="48" />
    </clipPath>
  </defs>
  <image href="avatar.jpg" x="0" y="0" width="100" height="100" clip-path="url(#avatar)" />
  <circle cx="50" cy="50" r="48" fill="none" stroke="#4f5bd5" stroke-width="2" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：渐隐遮罩

该示例来自原文《渐隐遮罩》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="vignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="band">
      <rect width="400" height="200" fill="url(#vignette)" />
    </mask>
  </defs>
  <rect width="400" height="200" fill="#4f5bd5" mask="url(#band)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：文字渐变蒙版

该示例来自原文《文字渐变蒙版》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="rainbow" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#d63031" />
      <stop offset="25%" stop-color="#f9a825" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="75%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#8854d0" />
    </linearGradient>
    <mask id="text">
      <rect width="400" height="100" fill="#000" />
      <text
        x="200"
        y="70"
        text-anchor="middle"
        font-size="60"
        font-weight="bold"
        fill="#fff"
        font-family="sans-serif"
      >
        FANDEX
      </text>
    </mask>
  </defs>
  <rect width="400" height="100" fill="url(#rainbow)" mask="url(#text)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 26 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：反射倒影

该示例来自原文《反射倒影》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <linearGradient id="reflect-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#fff" stop-opacity="0" />
    </linearGradient>
    <mask id="reflect">
      <rect y="100" width="200" height="100" fill="url(#reflect-grad)" />
    </mask>
  </defs>
  <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  <g transform="translate(0, 200) scale(1, -1)" mask="url(#reflect)" opacity="0.6">
    <rect x="50" y="20" width="100" height="80" fill="#4f5bd5" />
  </g>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.29 示例：clipPath 动画

该示例来自原文《clipPath 动画》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="reveal">
      <rect x="0" y="0" width="0" height="200">
        <animate attributeName="width" from="0" to="200" dur="2s" fill="freeze" />
      </rect>
    </clipPath>
  </defs>
  <rect width="200" height="200" fill="#4f5bd5" clip-path="url(#reveal)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.30 示例：mask 动画

该示例来自原文《mask 动画》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="sweep" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#000" />
      <stop offset="40%" stop-color="#000" />
      <stop offset="50%" stop-color="#fff" />
      <stop offset="60%" stop-color="#000" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="sweep-mask">
      <rect width="400" height="100" fill="url(#sweep)">
        <animateTransform
          attributeName="transform"
          type="translate"
          from="-200 0"
          to="400 0"
          dur="3s"
          repeatCount="indefinite"
        />
      </rect>
    </mask>
  </defs>
  <text
    x="200"
    y="65"
    text-anchor="middle"
    font-size="40"
    font-weight="bold"
    fill="#4f5bd5"
    mask="url(#sweep-mask)"
  >
    FANDEX
  </text>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 34 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.31 示例：多重裁剪

该示例来自原文《多重裁剪》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="circle">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <linearGradient id="fade" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fff" />
      <stop offset="100%" stop-color="#000" />
    </linearGradient>
    <mask id="bottom-fade">
      <rect width="200" height="200" fill="url(#fade)" />
    </mask>
  </defs>
  <image
    href="photo.jpg"
    width="200"
    height="200"
    clip-path="url(#circle)"
    mask="url(#bottom-fade)"
  />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 21 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.32 示例：综合示例:粒子头像

该示例来自原文《综合示例:粒子头像》小节，用于演示SVG 裁剪与蒙版相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <clipPath id="avatar">
      <circle cx="100" cy="100" r="80" />
    </clipPath>
    <radialGradient id="ring-grad" cx="50%" cy="50%" r="50%">
      <stop offset="80%" stop-color="#000" stop-opacity="0" />
      <stop offset="100%" stop-color="#4f5bd5" stop-opacity="1" />
    </radialGradient>
    <mask id="ring">
      <rect width="200" height="200" fill="url(#ring-grad)" />
    </mask>
  </defs>
  <image href="avatar.jpg" x="20" y="20" width="160" height="160" clip-path="url(#avatar)" />
  <circle cx="100" cy="100" r="90" fill="#4f5bd5" mask="url(#ring)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《SVG 裁剪与蒙版》定位的最快路径。下面从多个维度与相邻方案进行对比。

SVG 与 canvas：SVG 矢量、可交互、DOM 友好；canvas 位图、高性能、适合游戏。
SVG 与 PNG：SVG 无损缩放、体积小；PNG 兼容极旧环境但位图放大模糊。
SMIL 与 CSS 动画：CSS 更现代，SMIL 支持部分高级特性；现代项目优先 CSS/Web Animations。

对比的目的不是分出绝对优劣，而是建立选择依据：不同约束条件下，最优解不同。读者应把每个对比维度转化为决策检查清单。

## 7. 常见陷阱与最佳实践

本节整理该主题的高频错误与推荐做法。每个陷阱先描述现象，再解释原因，最后给出最佳实践。

### 7.1 viewBox 缺失

缩放行为异常。始终定义 viewBox 与宽高。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，viewBox 缺失 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，viewBox 缺失 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理viewBox 缺失的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.2 无命名空间

内联 SVG 需 xmlns；HTML5 中内联可省略但外部文件必须。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，无命名空间 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，无命名空间 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理无命名空间的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.3 路径命令错误

坐标格式错误导致图形缺失。检查命令字母与数字。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，路径命令错误 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，路径命令错误 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理路径命令错误的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.4 fill-rule 混淆

非零环绕与奇偶规则结果不同。按需选择。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，fill-rule 混淆 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，fill-rule 混淆 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理fill-rule 混淆的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.5 动画性能

逐帧修改 DOM 属性卡顿。使用 transform 与 CSS 动画。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，动画性能 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，动画性能 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理动画性能的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.6 可访问性缺失

SVG 无 role/title 时屏幕阅读器忽略。添加 role="img" 与 title。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，可访问性缺失 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，可访问性缺失 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理可访问性缺失的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.7 字体依赖

text 元素依赖系统字体。需要一致性时转路径或使用 web 字体。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，字体依赖 一般源于对 SVG 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，字体依赖 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理字体依赖的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.0 最佳实践总览

1. 图标组件化（React/Vue）统一尺寸与样式。
2. 图形语义化：装饰用 aria-hidden，信息图提供 title/desc。
3. 性能：复用 symbol/use 减少重复；大图使用懒加载。

把这些最佳实践固化为团队规范与代码评审检查项，是避免同类问题反复出现的关键。

## 8. 工程实践

本节把《SVG 裁剪与蒙版》放入真实工程场景，给出可复用的模式与组织方法。

图标系统：symbol + use 组合 sprite；图标组件接受 size/color props。
数据可视化：D3 生成 SVG 元素；响应式 viewBox 自适应容器。
优化：SVGO 压缩；关键图形内联，非关键用 img 懒加载。

### 8.1 工程实践的原则拆解

以上工程实践可以归纳为四条原则。第一，配置与代码分离：SVG 项目中环境差异应通过配置注入，而不是散落在代码分支中；这保证同一份代码可以在开发、测试、生产环境一致运行。

第二，接口稳定优先：对外接口（函数签名、协议、数据格式）一旦被消费方依赖，变更成本极高；设计时应预留扩展点并保持向后兼容。

第三，可观测性内置：日志、指标与追踪应该在功能开发时同步设计，而不是故障发生后补救；没有观测手段的模块等于黑盒。

第四，变更可回滚：任何发布都应有对应的回滚方案；数据库迁移、配置变更与代码发布一样需要版本管理与逆向路径。

### 8.2 实践落地的检查清单

- [ ] 图标系统：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 数据可视化：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 优化：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。

工程实践的共性原则：配置与代码分离、接口稳定优先、可观测性内置、变更可回滚。这些原则适用于本主题的所有实现。

## 9. 案例研究

本节通过一个完整案例把《SVG 裁剪与蒙版》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

需求：实现带 hover 交互的折线统计图。
方案：D3 计算坐标生成 path，CSS 过渡动画，tooltip 跟随。
要点：viewport 响应式；坐标轴刻度清晰；无数据时显示空态。
验证：多分辨率截图、交互测试、axe 可访问性。

### 9.1 案例的扩展讨论

把案例中的方案放大到真实规模，需要额外考虑三个问题：

第一，规模：当数据量或并发量上升一个数量级时，原方案中的数据结构、缓存策略与任务调度是否仍然成立？通常需要引入分层与异步。

第二，团队：多人协作时，模块边界、接口契约与代码所有权必须明确；案例中的实现应拆分为可独立测试的单元，并配合文档说明设计意图。

第三，演进：上线后的需求变化不可避免；方案设计时应预留扩展点（配置化、插件化、事件化），并定期用真实指标验证假设。


案例研究的学习方法：先独立阅读需求，尝试在脑中形成方案，再对照实现与讲解，最后思考“如果约束变化（数据量、并发、团队规模），方案应如何调整”。

## 10. 知识要点总结与深入讲解

本节以讲解形式汇总全文要点，替代传统的习题与自测，读者不需要答题，只需跟随解释建立完整的认知框架。

关于《SVG 裁剪与蒙版》的核心结论：

SVG 是 Web 的矢量基础设施，理解坐标系与路径就掌握了核心。
内联 SVG 可被 CSS/JS 完全控制，是组件化图标的理想载体。
性能与可访问性并重：复用、压缩、语义化。

原文档各小节的要点回顾：

- 1. clipPath 裁剪路径：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. mask 蒙版：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. clipPath vs mask 对比：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. 圆形头像：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. 渐隐遮罩：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 文字渐变蒙版：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 7. 反射倒影：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 8. clipPath 动画：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 9. mask 动画：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 10. 多重裁剪：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 11. 实战：粒子头像：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 12. 性能建议：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- clipPath 裁剪路径：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- mask 蒙版：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- clipPath 与 mask 对比：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 圆形头像裁剪：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 渐隐遮罩：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 文字渐变蒙版：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 反射倒影：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- clipPath 动画：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- mask 动画：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 多重裁剪：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 综合示例:粒子头像：该小节围绕SVG 裁剪与蒙版展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

把以上要点与第 3-9 节的内容对照复习，即可完成对本文主题的闭环学习。

## 11. 参考文献


MDN SVG 文档：https://developer.mozilla.org/zh-CN/docs/Web/SVG
SVG 规范（W3C）：https://www.w3.org/TR/SVG2/
SVGO 优化工具：https://github.com/svg/svgo
D3.js：https://d3js.org/

## 12. 延伸阅读


SVG 图形语法，见 012-svg 模块文档。
CSS 样式与动画，见 007-css 模块。
React/Vue 图标组件实践，见 011-react/010-vue3 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供前端图形课程。

## 14. 模块知识图谱与学习路径

本文属于 SVG 模块。为了把《SVG 裁剪与蒙版》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["SVG 裁剪与蒙版"]
    N0["SVG 概述与环境配置"]
    N1["SVG 基础语法与文档结构"]
    N0 --> N1
    N2["SVG 坐标系与 viewBox"]
    N1 --> N2
    N3["SVG 基本图形详解"]
    N2 --> N3
    N4["SVG 路径 path 详解"]
    N3 --> N4
    N5["SVG 文本与排版"]
    N4 --> N5
    N6["SVG 颜色与填充"]
    N5 --> N6
    N7["SVG 渐变与图案"]
    N6 --> N7
    N8["SVG 变换 transform"]
    N7 --> N8
    N9["SVG 滤镜详解"]
    N8 --> N9
    N10["SVG 裁剪与蒙版"]
    N9 --> N10
    N11["SVG 符号与复用"]
    N10 --> N11
    N12["SVG 动画基础"]
    N11 --> N12
    N13["SVG CSS 样式化"]
    N12 --> N13
```

上图为模块主题的推荐学习顺序示意图（仅展示前若干主题）。各主题之间存在三类关联：

第一，前置依赖关系：早期主题是后期主题的基础，例如环境与语法先行、进阶主题随后；

第二，横向并列关系：同一层级主题从不同角度覆盖模块能力，学习顺序可以按兴趣调整；

第三，工程组合关系：多个主题在真实项目中组合使用，例如配置、性能与安全主题往往出现在同一系统的不同层面。

### 14.1 模块主题速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| SVG 概述与环境配置 | 001-SVGOverviewEnvSetup | 本文的前置基础 |
| SVG 基础语法与文档结构 | 002-SVGBasicSyntaxDocStructure | 本文的前置基础 |
| SVG 坐标系与 viewBox | 003-SVGCoordinateSystemViewBox | 本文的并列主题 |
| SVG 基本图形详解 | 004-SVGBasicShapeDetailed | 本文的并列主题 |
| SVG 路径 path 详解 | 005-SVGPathPathDetailed | 本文的并列主题 |
| SVG 文本与排版 | 006-SVGTextTypography | 本文的并列主题 |
| SVG 颜色与填充 | 007-SVGColorFill | 本文的并列主题 |
| SVG 渐变与图案 | 008-SVGGradientPattern | 本文的并列主题 |
| SVG 变换 transform | 009-SVGTransformTransform | 本文的并列主题 |
| SVG 滤镜详解 | 010-SVGFilterDetailed | 本文的并列主题 |
| SVG 裁剪与蒙版 | 011-SVGClipMask | 本文自身 |
| SVG 符号与复用 | 012-SVGSymbolReuse | 本文的并列主题 |
| SVG 动画基础 | 013-SVGAnimationBasics | 本文的前置基础 |
| SVG CSS 样式化 | 014-SVGCSSStyling | 本文的并列主题 |
| SVG JavaScript 交互 | 015-SVGJavaScriptInteraction | 本文的并列主题 |
| SVG 响应式与性能 | 016-SVGResponsivePerformance | 本文的性能延伸 |
| SVG 图标与可访问性 | 017-SVGIconAccessibility | 本文的并列主题 |
| SVG 实战项目 | 018-SVGPracticeProject | 本文的综合应用 |

速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。

## 15. 术语表

下表整理《SVG 裁剪与蒙版》及 SVG 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

| 术语 | 释义 |
| --- | --- |
| 坐标系 | viewBox 定义逻辑坐标（min-x min-y width height），preserveAspectRatio 控制缩放对齐。 |
| 基本图形 | rect（矩形）、circle（圆）、ellipse（椭圆）、line（直线）、polyline/polygon（折线/多边形）。 |
| 路径 path | M/L/C/Q/A 命令组合任意曲线；fill 填充、stroke 描边。 |
| 变换与动画 | transform 平移缩放旋转；CSS/SMIL 动画控制属性过渡。 |
| viewBox 缺失（易错点） | 参见常见陷阱章节的详细讲解 |
| 无命名空间（易错点） | 参见常见陷阱章节的详细讲解 |
| 路径命令错误（易错点） | 参见常见陷阱章节的详细讲解 |
| fill-rule 混淆（易错点） | 参见常见陷阱章节的详细讲解 |
| 动画性能（易错点） | 参见常见陷阱章节的详细讲解 |
| 可访问性缺失（易错点） | 参见常见陷阱章节的详细讲解 |

术语表与正文配合使用：先通读正文，遇到模糊术语回查本表；长期使用后术语会自然进入工作记忆。
