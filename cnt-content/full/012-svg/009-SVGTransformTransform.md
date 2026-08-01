---
order: 90
title: 'SVG 变换 transform'
module: svg
category: 'SVG Transform'
difficulty: intermediate
description: 'translate、rotate、scale、skew、matrix 与 transform-origin 变换组合。'
author: fanquanpp
updated: '2026-08-01'
related:
  - svg/坐标系与viewBox
  - svg/渐变与图案
  - svg/动画基础
prerequisites:
  - svg/坐标系与viewBox
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《SVG 变换 transform》，属于 SVG 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 SVG 的核心概念、术语与标准写法。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 SVG 的工作原理与设计动机。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写符合 SVG 规范的完整实现。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 SVG 与相邻方案的差异与边界。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据场景评价 SVG 相关方案的优劣。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 SVG 与其他技术设计完整方案。

通过本节学习，读者应当能够把《SVG 变换 transform》纳入自己的知识网络，并与 SVG 模块的其他主题（矢量图形、路径、变换、动画）建立关联。

## 2. 历史动机与发展脉络

《SVG 变换 transform》是 SVG 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

SVG（可缩放矢量图形）于 2001 年由 W3C 标准化，是 Web 原生矢量格式；与位图不同，SVG 由几何描述构成，任意缩放不失真。
SVG 是 XML 方言：元素即图形（rect/circle/path），样式可用 CSS，交互可用事件；SPA 生态中常以内联 SVG 与图标组件使用。
现代应用：图标系统、数据可视化（D3）、地图、LOGO、动画与交互图形；浏览器对 SVG 的支持已非常完整。

回到本文主题：SVG 变换 transform 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《SVG 变换 transform》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

坐标系：viewBox 定义逻辑坐标（min-x min-y width height），preserveAspectRatio 控制缩放对齐。
基本图形：rect（矩形）、circle（圆）、ellipse（椭圆）、line（直线）、polyline/polygon（折线/多边形）。
路径 path：M/L/C/Q/A 命令组合任意曲线；fill 填充、stroke 描边。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 23 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# SVG 变换 transform 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. transform 属性

`transform` 对元素或分组应用几何变换，**不影响后续元素的坐标系**（除非在 `<g>` 上）。

```html
<svg viewBox="0 0 200 200">
  <rect x="50" y="50" width="50" height="50" fill="#4f5bd5" />
  <rect x="50" y="50" width="50" height="50" fill="#d63031" transform="translate(60, 0)" />
</svg>
```

#### 2. 基本变换函数

##### 2.1 translate 平移

```html
<rect transform="translate(50, 30)" />
<!-- 或单轴 -->
<rect transform="translate(50, 0)" />
```

| 参数 | 说明                         |
| ---- | ---------------------------- |
| `tx` | X 方向偏移                   |
| `ty` | Y 方向偏移（可省略，默认 0） |

##### 2.2 rotate 旋转

```html
<rect transform="rotate(45)" />
<!-- 围绕指定点旋转 -->
<rect transform="rotate(45 100 100)" />
```

| 参数     | 说明                         |
| -------- | ---------------------------- |
| `angle`  | 旋转角度（度）               |
| `cx, cy` | 旋转中心（可省略，默认 0,0） |

> 单参数 `rotate(45)` 围绕原点 (0,0) 旋转，通常不是想要的效果。**常用 `rotate(angle cx cy)` 围绕元素中心旋转**。

##### 2.3 scale 缩放

```html
<rect transform="scale(1.5)" />
<!-- 双轴独立 -->
<rect transform="scale(1.5, 0.5)" />
```

| 参数 | 说明                                |
| ---- | ----------------------------------- |
| `sx` | X 方向缩放比                        |
| `sy` | Y 方向缩放比（可省略，默认等于 sx） |

> scale 会同时缩放 stroke-width。若需保持描边不变，使用 `vector-effect="non-scaling-stroke"`。

##### 2.4 skew 倾斜

```html
<rect transform="skewX(30)" /> <rect transform="skewY(15)" />
```

| 函数           | 说明        |
| -------------- | ----------- |
| `skewX(angle)` | 沿 X 轴倾斜 |
| `skewY(angle)` | 沐 Y 轴倾斜 |

#### 3. matrix 矩阵

所有变换本质都是 2D 仿射矩阵：`matrix(a, b, c, d, e, f)`。

```
| a c e |
| b d f |
| 0 0 1 |
```

变换公式：

- `x' = a*x + c*y + e`
- `y' = b*x + d*y + f`

##### 3.1 各变换对应的矩阵

| 变换                | matrix 参数                        |
| ------------------- | ---------------------------------- |
| `translate(tx, ty)` | `matrix(1 0 0 1 tx ty)`            |
| `rotate(θ)`         | `matrix(cosθ sinθ -sinθ cosθ 0 0)` |
| `scale(s)`          | `matrix(s 0 0 s 0 0)`              |
| `skewX(θ)`          | `matrix(1 0 tanθ 1 0 0)`           |

##### 3.2 示例

```html
<rect transform="matrix(1 0 0 1 50 30)" />
<!-- 等价于 translate(50, 30) -->

<rect transform="matrix(0.707 0.707 -0.707 0.707 0 0)" />
<!-- 等价于 rotate(45) -->
```

#### 4. 变换组合

多个变换用空格分隔，**从右到左**应用（类似 CSS transform）。

```html
<!-- 先 translate 再 rotate（视觉上） -->
<rect transform="translate(100, 100) rotate(45)" />

<!-- 先 rotate 再 translate -->
<rect transform="rotate(45) translate(100, 0)" />
```

##### 4.1 顺序影响结果

```html
<svg viewBox="0 0 200 200">
  <!-- 原始矩形 -->
  <rect x="0" y="0" width="50" height="50" fill="#4f5bd5" />

  <!-- 先平移到 (100,100) 再绕原点旋转 45°：矩形被甩到远处 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#d63031"
    transform="rotate(45) translate(100,100)"
  />

  <!-- 先绕原点旋转 45° 再平移到 (100,100)：矩形在 (100,100) 处旋转 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#00b894"
    transform="translate(100,100) rotate(45)"
  />
</svg>
```

> **建议**：旋转用 `rotate(angle cx cy)` 形式，避免顺序歧义。

#### 5. transform-origin

SVG 2 引入 `transform-origin`，类似 CSS 的同名属性。

```html
<rect
  x="50"
  y="50"
  width="50"
  height="50"
  transform="rotate(45)"
  transform-origin="75px 75px"
  style="transform-box: fill-box"
/>
```

##### 5.1 transform-box

| 值         | 含义                          |
| ---------- | ----------------------------- |
| `view-box` | 以 SVG viewBox 为参考（默认） |
| `fill-box` | 以元素边界框为参考            |

```html
<style>
  .spin {
    transform-box: fill-box;
    transform-origin: center;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
<rect class="spin" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
```

> `transform-box: fill-box` + `transform-origin: center` 是 SVG 元素围绕自身中心旋转的标准模式。

#### 6. CSS transform 与 SVG transform

CSS transform 也可作用于 SVG 元素，但需注意坐标系差异。

##### 6.1 CSS 方式

```css
.logo {
  transform: rotate(45deg);
  transform-origin: 50% 50%;
  transform-box: fill-box;
}
```

```html
<svg viewBox="0 0 200 200">
  <rect class="logo" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
</svg>
```

##### 6.2 两者区别

| 维度       | SVG transform 属性        | CSS transform                        |
| ---------- | ------------------------- | ------------------------------------ |
| 语法       | `rotate(45 100 100)`      | `rotate(45deg)` + `transform-origin` |
| 单位       | 无单位（默认度/像素）     | 需 `deg`、`px`                       |
| 动画       | SMIL `<animateTransform>` | CSS `@keyframes`                     |
| 性能       | 略优（直接矩阵）          | 现代浏览器已优化                     |
| 浏览器支持 | 全部                      | SVG 2 后完整支持                     |

#### 7. animateTransform 变换动画

SMIL 提供 `<animateTransform>` 专门用于变换动画。

```html
<svg viewBox="0 0 200 200">
  <rect x="75" y="75" width="50" height="50" fill="#4f5bd5">
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 100 100"
      to="360 100 100"
      dur="4s"
      repeatCount="indefinite"
    />
  </rect>
</svg>
```

##### 7.1 多变换叠加 additive

```html
<g>
  <animateTransform
    attributeName="transform"
    type="translate"
    values="0 0; 100 0; 0 0"
    dur="4s"
    repeatCount="indefinite"
  />
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="0; 360"
    dur="2s"
    repeatCount="indefinite"
    additive="sum"
  />
  <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
</g>
```

`additive="sum"` 让多个 animateTransform 叠加，否则后一个会覆盖前一个。

#### 8. 嵌套变换

`<g>` 上的 transform 会作用于所有子元素，形成坐标系嵌套。

```html
<svg viewBox="0 0 400 200">
  <g transform="translate(100, 100)">
    <!-- 子坐标系原点平移到 (100,100) -->
    <g transform="rotate(45)">
      <!-- 再旋转 45° -->
      <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
    </g>
    <circle cx="0" cy="0" r="5" fill="#d63031" />
  </g>
</svg>
```

> 嵌套变换矩阵会相乘，最终变换是父子变换的复合。

#### 9. 实战：地球绕太阳

```html
<svg viewBox="0 0 400 400">
  <!-- 太阳 -->
  <circle cx="200" cy="200" r="40" fill="#f9a825" />
  <!-- 地球轨道 -->
  <circle cx="200" cy="200" r="120" fill="none" stroke="#ccc" stroke-dasharray="4 4" />
  <!-- 地球绕太阳公转 -->
  <g>
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 200 200"
      to="360 200 200"
      dur="8s"
      repeatCount="indefinite"
    />
    <!-- 地球自转 -->
    <g transform="translate(320, 200)">
      <circle cx="0" cy="0" r="15" fill="#4f5bd5">
        <animateTransform
          attributeName="transform"
          type="rotate"
          from="0"
          to="360"
          dur="2s"
          repeatCount="indefinite"
        />
      </circle>
    </g>
  </g>
</svg>
```

**结构**：

- 外层 `<g>` 绕太阳中心旋转 → 实现公转
- 内层 `<g>` translate 到轨道位置 → 地球位置
- 地球 circle 自身 animateTransform → 自转

#### 10. 常见陷阱

##### 10.1 rotate 默认绕原点

```html
<!-- 错误：矩形被甩到画布外 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45)" />

<!-- 正确：围绕矩形中心旋转 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45 100 100)" />
```

##### 10.2 scale 缩放描边

```html
<!-- 描边被放大到 6px -->
<rect stroke-width="2" transform="scale(3)" />

<!-- 保持描边不变 -->
<rect stroke-width="2" transform="scale(3)" vector-effect="non-scaling-stroke" />
```

##### 10.3 transform 与 viewBox 重复缩放

```html
<!-- viewBox 已缩放 2 倍，transform scale(2) 会再缩 2 倍 -->
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect width="50" height="50" transform="scale(2)" />
  <!-- 实际显示 200×200 -->
</svg>
```

下一篇介绍滤镜，构建阴影、模糊、光照等高级视觉效果。
#### transform 属性

**transform 几何变换**
`transform="<变换函数> <变换函数> ..."`
```html
<svg viewBox="0 0 200 200">
  <rect x="50" y="50" width="50" height="50" fill="#4f5bd5" />
  <rect x="50" y="50" width="50" height="50" fill="#d63031" transform="translate(60, 0)" />
</svg>
```

---

#### translate 平移

**translate 平移**
`transform="translate(<tx> [, <ty>])"`
```html
<rect transform="translate(50, 30)" />
<!-- 或单轴 -->
<rect transform="translate(50, 0)" />
```

| 参数 | 说明                         |
| ---- | ---------------------------- |
| `tx` | X 方向偏移                   |
| `ty` | Y 方向偏移(可省略,默认 0) |

---

#### rotate 旋转

**rotate 旋转**
`transform="rotate(<angle> [, <cx>, <cy>])"`
```html
<rect transform="rotate(45)" />
<!-- 围绕指定点旋转 -->
<rect transform="rotate(45 100 100)" />
```

| 参数     | 说明                         |
| -------- | ---------------------------- |
| `angle`  | 旋转角度(度)               |
| `cx, cy` | 旋转中心(可省略,默认 0,0) |

> 单参数 `rotate(45)` 围绕原点 (0,0) 旋转,通常不是想要的效果。**常用 `rotate(angle cx cy)` 围绕元素中心旋转**。

---

#### scale 缩放

**scale 缩放**
`transform="scale(<sx> [, <sy>])"`
```html
<rect transform="scale(1.5)" />
<!-- 双轴独立 -->
<rect transform="scale(1.5, 0.5)" />
```

| 参数 | 说明                                |
| ---- | ----------------------------------- |
| `sx` | X 方向缩放比                        |
| `sy` | Y 方向缩放比(可省略,默认等于 sx) |

> scale 会同时缩放 stroke-width。若需保持描边不变,使用 `vector-effect="non-scaling-stroke"`。

---

#### skew 倾斜

**skewX 沿 X 轴倾斜**
`transform="skewX(<angle>)"`
```html
<rect transform="skewX(30)" />
```

**skewY 沿 Y 轴倾斜**
`transform="skewY(<angle>)"`
```html
<rect transform="skewY(15)" />
```

| 函数           | 说明        |
| -------------- | ----------- |
| `skewX(angle)` | 沿 X 轴倾斜 |
| `skewY(angle)` | 沿 Y 轴倾斜 |

---

#### matrix 矩阵

**matrix 2D 仿射矩阵**
`transform="matrix(<a>, <b>, <c>, <d>, <e>, <f>)"`

矩阵形式:
```
| a c e |
| b d f |
| 0 0 1 |
```

变换公式:
- `x' = a*x + c*y + e`
- `y' = b*x + d*y + f`

##### 各变换对应的矩阵

| 变换                | matrix 参数                        |
| ------------------- | ---------------------------------- |
| `translate(tx, ty)` | `matrix(1 0 0 1 tx ty)`            |
| `rotate(θ)`         | `matrix(cosθ sinθ -sinθ cosθ 0 0)` |
| `scale(s)`          | `matrix(s 0 0 s 0 0)`              |
| `skewX(θ)`          | `matrix(1 0 tanθ 1 0 0)`           |

##### 示例

**matrix 平移**
```html
<rect transform="matrix(1 0 0 1 50 30)" />
<!-- 等价于 translate(50, 30) -->
```

**matrix 旋转**
```html
<rect transform="matrix(0.707 0.707 -0.707 0.707 0 0)" />
<!-- 等价于 rotate(45) -->
```

---

#### 变换组合

**多变换空格分隔,从右到左应用**
`transform="<变换1> <变换2> ..."`
```html
<!-- 先 translate 再 rotate(视觉上) -->
<rect transform="translate(100, 100) rotate(45)" />

<!-- 先 rotate 再 translate -->
<rect transform="rotate(45) translate(100, 0)" />
```

##### 顺序影响结果

```html
<svg viewBox="0 0 200 200">
  <!-- 原始矩形 -->
  <rect x="0" y="0" width="50" height="50" fill="#4f5bd5" />

  <!-- 先平移到 (100,100) 再绕原点旋转 45°:矩形被甩到远处 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#d63031"
    transform="rotate(45) translate(100,100)"
  />

  <!-- 先绕原点旋转 45° 再平移到 (100,100):矩形在 (100,100) 处旋转 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#00b894"
    transform="translate(100,100) rotate(45)"
  />
</svg>
```

> **建议**:旋转用 `rotate(angle cx cy)` 形式,避免顺序歧义。

---

#### transform-origin

**transform-origin 变换原点**
`transform-origin="<x> <y>"` + `style="transform-box: fill-box"`
```html
<rect
  x="50"
  y="50"
  width="50"
  height="50"
  transform="rotate(45)"
  transform-origin="75px 75px"
  style="transform-box: fill-box"
/>
```

##### transform-box

| 值         | 含义                          |
| ---------- | ----------------------------- |
| `view-box` | 以 SVG viewBox 为参考(默认) |
| `fill-box` | 以元素边界框为参考            |

**围绕自身中心旋转**
```html
<style>
  .spin {
    transform-box: fill-box;
    transform-origin: center;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
<rect class="spin" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
```

> `transform-box: fill-box` + `transform-origin: center` 是 SVG 元素围绕自身中心旋转的标准模式。

---

#### CSS transform 与 SVG transform

##### CSS 方式

```css
.logo {
  transform: rotate(45deg);
  transform-origin: 50% 50%;
  transform-box: fill-box;
}
```

```html
<svg viewBox="0 0 200 200">
  <rect class="logo" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
</svg>
```

##### 两者区别

| 维度       | SVG transform 属性        | CSS transform                        |
| ---------- | ------------------------- | ------------------------------------ |
| 语法       | `rotate(45 100 100)`      | `rotate(45deg)` + `transform-origin` |
| 单位       | 无单位(默认度/像素)     | 需 `deg`、`px`                       |
| 动画       | SMIL `<animateTransform>` | CSS `@keyframes`                     |
| 性能       | 略优(直接矩阵)          | 现代浏览器已优化                     |
| 浏览器支持 | 全部                      | SVG 2 后完整支持                     |

---

#### animateTransform 变换动画

**animateTransform SMIL 变换动画**
`<animateTransform attributeName="transform" type="<变换类型>" from="<起始值>" to="<结束值>" dur="<时长>" [repeatCount="<重复>"] />`
```html
<svg viewBox="0 0 200 200">
  <rect x="75" y="75" width="50" height="50" fill="#4f5bd5">
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 100 100"
      to="360 100 100"
      dur="4s"
      repeatCount="indefinite"
    />
  </rect>
</svg>
```

##### 多变换叠加 additive

**additive="sum" 多变换叠加**
```html
<g>
  <animateTransform
    attributeName="transform"
    type="translate"
    values="0 0; 100 0; 0 0"
    dur="4s"
    repeatCount="indefinite"
  />
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="0; 360"
    dur="2s"
    repeatCount="indefinite"
    additive="sum"
  />
  <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
</g>
```

`additive="sum"` 让多个 animateTransform 叠加,否则后一个会覆盖前一个。

---

#### 嵌套变换

**g 上的 transform 作用于所有子元素**
```html
<svg viewBox="0 0 400 200">
  <g transform="translate(100, 100)">
    <!-- 子坐标系原点平移到 (100,100) -->
    <g transform="rotate(45)">
      <!-- 再旋转 45° -->
      <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
    </g>
    <circle cx="0" cy="0" r="5" fill="#d63031" />
  </g>
</svg>
```

> 嵌套变换矩阵会相乘,最终变换是父子变换的复合。

---

#### 综合示例:地球绕太阳

**公转 + 自转**
```html
<svg viewBox="0 0 400 400">
  <!-- 太阳 -->
  <circle cx="200" cy="200" r="40" fill="#f9a825" />
  <!-- 地球轨道 -->
  <circle cx="200" cy="200" r="120" fill="none" stroke="#ccc" stroke-dasharray="4 4" />
  <!-- 地球绕太阳公转 -->
  <g>
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 200 200"
      to="360 200 200"
      dur="8s"
      repeatCount="indefinite"
    />
    <!-- 地球自转 -->
    <g transform="translate(320, 200)">
      <circle cx="0" cy="0" r="15" fill="#4f5bd5">
        <animateTransform
          attributeName="transform"
          type="rotate"
          from="0"
          to="360"
          dur="2s"
          repeatCount="indefinite"
        />
      </circle>
    </g>
  </g>
</svg>
```

结构:
- 外层 `<g>` 绕太阳中心旋转 → 实现公转
- 内层 `<g>` translate 到轨道位置 → 地球位置
- 地球 circle 自身 animateTransform → 自转

---

#### 常见陷阱

##### rotate 默认绕原点

```html
<!-- 错误:矩形被甩到画布外 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45)" />

<!-- 正确:围绕矩形中心旋转 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45 100 100)" />
```

##### scale 缩放描边

```html
<!-- 描边被放大到 6px -->
<rect stroke-width="2" transform="scale(3)" />

<!-- 保持描边不变 -->
<rect stroke-width="2" transform="scale(3)" vector-effect="non-scaling-stroke" />
```

##### transform 与 viewBox 重复缩放

```html
<!-- viewBox 已缩放 2 倍,transform scale(2) 会再缩 2 倍 -->
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect width="50" height="50" transform="scale(2)" />
  <!-- 实际显示 200×200 -->
</svg>
```


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["SVG 变换 transform"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《SVG 变换 transform》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

坐标系：viewBox 定义逻辑坐标（min-x min-y width height），preserveAspectRatio 控制缩放对齐。
基本图形：rect（矩形）、circle（圆）、ellipse（椭圆）、line（直线）、polyline/polygon（折线/多边形）。
路径 path：M/L/C/Q/A 命令组合任意曲线；fill 填充、stroke 描边。
变换与动画：transform 平移缩放旋转；CSS/SMIL 动画控制属性过渡。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1. transform 属性

该示例来自原文《1. transform 属性》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <rect x="50" y="50" width="50" height="50" fill="#4f5bd5" />
  <rect x="50" y="50" width="50" height="50" fill="#d63031" transform="translate(60, 0)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：2.1 translate 平移

该示例来自原文《2.1 translate 平移》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="translate(50, 30)" />
<!-- 或单轴 -->
<rect transform="translate(50, 0)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：2.2 rotate 旋转

该示例来自原文《2.2 rotate 旋转》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="rotate(45)" />
<!-- 围绕指定点旋转 -->
<rect transform="rotate(45 100 100)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：2.3 scale 缩放

该示例来自原文《2.3 scale 缩放》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="scale(1.5)" />
<!-- 双轴独立 -->
<rect transform="scale(1.5, 0.5)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：2.4 skew 倾斜

该示例来自原文《2.4 skew 倾斜》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="skewX(30)" /> <rect transform="skewY(15)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：3. matrix 矩阵

该示例来自原文《3. matrix 矩阵》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```text
| a c e |
| b d f |
| 0 0 1 |
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：3.2 示例

该示例来自原文《3.2 示例》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="matrix(1 0 0 1 50 30)" />
<!-- 等价于 translate(50, 30) -->

<rect transform="matrix(0.707 0.707 -0.707 0.707 0 0)" />
<!-- 等价于 rotate(45) -->
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：4. 变换组合

该示例来自原文《4. 变换组合》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- 先 translate 再 rotate（视觉上） -->
<rect transform="translate(100, 100) rotate(45)" />

<!-- 先 rotate 再 translate -->
<rect transform="rotate(45) translate(100, 0)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：4.1 顺序影响结果

该示例来自原文《4.1 顺序影响结果》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <!-- 原始矩形 -->
  <rect x="0" y="0" width="50" height="50" fill="#4f5bd5" />

  <!-- 先平移到 (100,100) 再绕原点旋转 45°：矩形被甩到远处 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#d63031"
    transform="rotate(45) translate(100,100)"
  />

  <!-- 先绕原点旋转 45° 再平移到 (100,100)：矩形在 (100,100) 处旋转 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#00b894"
    transform="translate(100,100) rotate(45)"
  />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：5. transform-origin

该示例来自原文《5. transform-origin》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect
  x="50"
  y="50"
  width="50"
  height="50"
  transform="rotate(45)"
  transform-origin="75px 75px"
  style="transform-box: fill-box"
/>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：5.1 transform-box

该示例来自原文《5.1 transform-box》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<style>
  .spin {
    transform-box: fill-box;
    transform-origin: center;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
<rect class="spin" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 1 类关键结构（class）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：6.1 CSS 方式

该示例来自原文《6.1 CSS 方式》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```css
.logo {
  transform: rotate(45deg);
  transform-origin: 50% 50%;
  transform-box: fill-box;
}
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：6.1 CSS 方式

该示例来自原文《6.1 CSS 方式》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <rect class="logo" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 1 类关键结构（class）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：7. animateTransform 变换动画

该示例来自原文《7. animateTransform 变换动画》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <rect x="75" y="75" width="50" height="50" fill="#4f5bd5">
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 100 100"
      to="360 100 100"
      dur="4s"
      repeatCount="indefinite"
    />
  </rect>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：7.1 多变换叠加 additive

该示例来自原文《7.1 多变换叠加 additive》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<g>
  <animateTransform
    attributeName="transform"
    type="translate"
    values="0 0; 100 0; 0 0"
    dur="4s"
    repeatCount="indefinite"
  />
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="0; 360"
    dur="2s"
    repeatCount="indefinite"
    additive="sum"
  />
  <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
</g>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：8. 嵌套变换

该示例来自原文《8. 嵌套变换》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 200">
  <g transform="translate(100, 100)">
    <!-- 子坐标系原点平移到 (100,100) -->
    <g transform="rotate(45)">
      <!-- 再旋转 45° -->
      <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
    </g>
    <circle cx="0" cy="0" r="5" fill="#d63031" />
  </g>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：9. 实战：地球绕太阳

该示例来自原文《9. 实战：地球绕太阳》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 400">
  <!-- 太阳 -->
  <circle cx="200" cy="200" r="40" fill="#f9a825" />
  <!-- 地球轨道 -->
  <circle cx="200" cy="200" r="120" fill="none" stroke="#ccc" stroke-dasharray="4 4" />
  <!-- 地球绕太阳公转 -->
  <g>
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 200 200"
      to="360 200 200"
      dur="8s"
      repeatCount="indefinite"
    />
    <!-- 地球自转 -->
    <g transform="translate(320, 200)">
      <circle cx="0" cy="0" r="15" fill="#4f5bd5">
        <animateTransform
          attributeName="transform"
          type="rotate"
          from="0"
          to="360"
          dur="2s"
          repeatCount="indefinite"
        />
      </circle>
    </g>
  </g>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 30 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：10.1 rotate 默认绕原点

该示例来自原文《10.1 rotate 默认绕原点》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- 错误：矩形被甩到画布外 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45)" />

<!-- 正确：围绕矩形中心旋转 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45 100 100)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：10.2 scale 缩放描边

该示例来自原文《10.2 scale 缩放描边》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- 描边被放大到 6px -->
<rect stroke-width="2" transform="scale(3)" />

<!-- 保持描边不变 -->
<rect stroke-width="2" transform="scale(3)" vector-effect="non-scaling-stroke" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：10.3 transform 与 viewBox 重复缩放

该示例来自原文《10.3 transform 与 viewBox 重复缩放》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- viewBox 已缩放 2 倍，transform scale(2) 会再缩 2 倍 -->
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect width="50" height="50" transform="scale(2)" />
  <!-- 实际显示 200×200 -->
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：transform 属性

该示例来自原文《transform 属性》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <rect x="50" y="50" width="50" height="50" fill="#4f5bd5" />
  <rect x="50" y="50" width="50" height="50" fill="#d63031" transform="translate(60, 0)" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：translate 平移

该示例来自原文《translate 平移》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="translate(50, 30)" />
<!-- 或单轴 -->
<rect transform="translate(50, 0)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：rotate 旋转

该示例来自原文《rotate 旋转》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="rotate(45)" />
<!-- 围绕指定点旋转 -->
<rect transform="rotate(45 100 100)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：scale 缩放

该示例来自原文《scale 缩放》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="scale(1.5)" />
<!-- 双轴独立 -->
<rect transform="scale(1.5, 0.5)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：skew 倾斜

该示例来自原文《skew 倾斜》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="skewX(30)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：skew 倾斜

该示例来自原文《skew 倾斜》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="skewY(15)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 1 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：matrix 矩阵

该示例来自原文《matrix 矩阵》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```text
| a c e |
| b d f |
| 0 0 1 |
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：示例

该示例来自原文《示例》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="matrix(1 0 0 1 50 30)" />
<!-- 等价于 translate(50, 30) -->
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.29 示例：示例

该示例来自原文《示例》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect transform="matrix(0.707 0.707 -0.707 0.707 0 0)" />
<!-- 等价于 rotate(45) -->
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.30 示例：变换组合

该示例来自原文《变换组合》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- 先 translate 再 rotate(视觉上) -->
<rect transform="translate(100, 100) rotate(45)" />

<!-- 先 rotate 再 translate -->
<rect transform="rotate(45) translate(100, 0)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.31 示例：顺序影响结果

该示例来自原文《顺序影响结果》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <!-- 原始矩形 -->
  <rect x="0" y="0" width="50" height="50" fill="#4f5bd5" />

  <!-- 先平移到 (100,100) 再绕原点旋转 45°:矩形被甩到远处 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#d63031"
    transform="rotate(45) translate(100,100)"
  />

  <!-- 先绕原点旋转 45° 再平移到 (100,100):矩形在 (100,100) 处旋转 -->
  <rect
    x="0"
    y="0"
    width="50"
    height="50"
    fill="#00b894"
    transform="translate(100,100) rotate(45)"
  />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.32 示例：transform-origin

该示例来自原文《transform-origin》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<rect
  x="50"
  y="50"
  width="50"
  height="50"
  transform="rotate(45)"
  transform-origin="75px 75px"
  style="transform-box: fill-box"
/>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.33 示例：transform-box

该示例来自原文《transform-box》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<style>
  .spin {
    transform-box: fill-box;
    transform-origin: center;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
<rect class="spin" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 1 类关键结构（class）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.34 示例：CSS 方式

该示例来自原文《CSS 方式》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```css
.logo {
  transform: rotate(45deg);
  transform-origin: 50% 50%;
  transform-box: fill-box;
}
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.35 示例：CSS 方式

该示例来自原文《CSS 方式》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <rect class="logo" x="50" y="50" width="100" height="100" fill="#4f5bd5" />
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 1 类关键结构（class）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.36 示例：animateTransform 变换动画

该示例来自原文《animateTransform 变换动画》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 200 200">
  <rect x="75" y="75" width="50" height="50" fill="#4f5bd5">
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 100 100"
      to="360 100 100"
      dur="4s"
      repeatCount="indefinite"
    />
  </rect>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.37 示例：多变换叠加 additive

该示例来自原文《多变换叠加 additive》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<g>
  <animateTransform
    attributeName="transform"
    type="translate"
    values="0 0; 100 0; 0 0"
    dur="4s"
    repeatCount="indefinite"
  />
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="0; 360"
    dur="2s"
    repeatCount="indefinite"
    additive="sum"
  />
  <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
</g>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.38 示例：嵌套变换

该示例来自原文《嵌套变换》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 200">
  <g transform="translate(100, 100)">
    <!-- 子坐标系原点平移到 (100,100) -->
    <g transform="rotate(45)">
      <!-- 再旋转 45° -->
      <rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5" />
    </g>
    <circle cx="0" cy="0" r="5" fill="#d63031" />
  </g>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.39 示例：综合示例:地球绕太阳

该示例来自原文《综合示例:地球绕太阳》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<svg viewBox="0 0 400 400">
  <!-- 太阳 -->
  <circle cx="200" cy="200" r="40" fill="#f9a825" />
  <!-- 地球轨道 -->
  <circle cx="200" cy="200" r="120" fill="none" stroke="#ccc" stroke-dasharray="4 4" />
  <!-- 地球绕太阳公转 -->
  <g>
    <animateTransform
      attributeName="transform"
      type="rotate"
      from="0 200 200"
      to="360 200 200"
      dur="8s"
      repeatCount="indefinite"
    />
    <!-- 地球自转 -->
    <g transform="translate(320, 200)">
      <circle cx="0" cy="0" r="15" fill="#4f5bd5">
        <animateTransform
          attributeName="transform"
          type="rotate"
          from="0"
          to="360"
          dur="2s"
          repeatCount="indefinite"
        />
      </circle>
    </g>
  </g>
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 30 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.40 示例：rotate 默认绕原点

该示例来自原文《rotate 默认绕原点》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- 错误:矩形被甩到画布外 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45)" />

<!-- 正确:围绕矩形中心旋转 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45 100 100)" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.41 示例：scale 缩放描边

该示例来自原文《scale 缩放描边》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- 描边被放大到 6px -->
<rect stroke-width="2" transform="scale(3)" />

<!-- 保持描边不变 -->
<rect stroke-width="2" transform="scale(3)" vector-effect="non-scaling-stroke" />
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.42 示例：transform 与 viewBox 重复缩放

该示例来自原文《transform 与 viewBox 重复缩放》小节，用于演示SVG 变换 transform相关操作。阅读时请先看代码结构，再看其后的讲解。

```html
<!-- viewBox 已缩放 2 倍,transform scale(2) 会再缩 2 倍 -->
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect width="50" height="50" transform="scale(2)" />
  <!-- 实际显示 200×200 -->
</svg>
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《SVG 变换 transform》定位的最快路径。下面从多个维度与相邻方案进行对比。

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

本节把《SVG 变换 transform》放入真实工程场景，给出可复用的模式与组织方法。

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

本节通过一个完整案例把《SVG 变换 transform》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

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

关于《SVG 变换 transform》的核心结论：

SVG 是 Web 的矢量基础设施，理解坐标系与路径就掌握了核心。
内联 SVG 可被 CSS/JS 完全控制，是组件化图标的理想载体。
性能与可访问性并重：复用、压缩、语义化。

原文档各小节的要点回顾：

- 1. transform 属性：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. 基本变换函数：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. matrix 矩阵：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. 变换组合：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. transform-origin：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. CSS transform 与 SVG transform：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 7. animateTransform 变换动画：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 8. 嵌套变换：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 9. 实战：地球绕太阳：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 10. 常见陷阱：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- transform 属性：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- translate 平移：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- rotate 旋转：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- scale 缩放：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- skew 倾斜：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- matrix 矩阵：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 变换组合：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- transform-origin：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- CSS transform 与 SVG transform：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- animateTransform 变换动画：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 嵌套变换：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 综合示例:地球绕太阳：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 常见陷阱：该小节围绕SVG 变换 transform展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

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

本文属于 SVG 模块。为了把《SVG 变换 transform》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["SVG 变换 transform"]
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
| SVG 变换 transform | 009-SVGTransformTransform | 本文自身 |
| SVG 滤镜详解 | 010-SVGFilterDetailed | 本文的并列主题 |
| SVG 裁剪与蒙版 | 011-SVGClipMask | 本文的并列主题 |
| SVG 符号与复用 | 012-SVGSymbolReuse | 本文的并列主题 |
| SVG 动画基础 | 013-SVGAnimationBasics | 本文的前置基础 |
| SVG CSS 样式化 | 014-SVGCSSStyling | 本文的并列主题 |
| SVG JavaScript 交互 | 015-SVGJavaScriptInteraction | 本文的并列主题 |
| SVG 响应式与性能 | 016-SVGResponsivePerformance | 本文的性能延伸 |
| SVG 图标与可访问性 | 017-SVGIconAccessibility | 本文的并列主题 |
| SVG 实战项目 | 018-SVGPracticeProject | 本文的综合应用 |

速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。

## 15. 术语表

下表整理《SVG 变换 transform》及 SVG 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

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
