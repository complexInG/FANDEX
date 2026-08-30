---
order: 10
title: svg 模块文档合集
module: 'svg'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：012-svg/001-SVGOverviewEnvSetup.md ============ -->

## 1. 历史动机与发展脉络

### 1.1 矢量图形的起源:从 PostScript 到 Web

矢量图形的思想可追溯至 20 世纪 60 年代。1963 年,Ivan Sutherland 在麻省理工学院(MIT)开发了 Sketchpad 系统,这是公认的计算机图形学开山之作,首次实现了基于约束的矢量绘图。1976 年,John Warnock 与 Charles Geschke 在施乐帕克研究中心(Xerox PARC)开发页面描述语言 InterPress,后于 1982 年创立 Adobe 公司并推出 PostScript,奠定了矢量描述的工业标准。

PostScript 的成功启发了 W3C 在 Web 平台引入矢量图形标准。1998 年,Microsoft 提交 VML(Vector Markup Language),Adobe 与 Sun 提交 PGML(Precision Graphics Markup Language),两份提案并行演进促使 W3C 成立 SVG Working Group,于 2001 年发布 SVG 1.0 正式推荐标准。

### 1.2 SVG 规范版本演进

SVG 规范历经二十余年迭代,形成了清晰的版本演进图谱。

| 版本 | 发布年份 | 关键特性 | W3C 状态 | 浏览器支持现状 |
| ---- | -------- | -------- | -------- | -------------- |
| SVG 1.0 | 2001 | 基础图形、路径、文本、变换 | Recommendation | 全平台支持 |
| SVG 1.1 | 2003 | 模块化拆分,引入 SVG Tiny/Basic 子集 | Recommendation | 全平台支持 |
| SVG Tiny 1.2 | 2008 | 移动设备优化,聚焦资源受限场景 | Recommendation | 已废弃 |
| SVG 1.2 Full | - | 计划增加流式音频/视频、DOM Level 3 | 草案废止 | 未实现 |
| SVG 2 | 2018-至今 | 融合 HTML5、CSS Grid、Web Components | Candidate Recommendation | 现代浏览器部分支持 |
| SVG 2.1 | 2024+ | Web Animations API 集成、属性简化 | Working Draft | 实验性支持 |

### 1.3 关键技术决策节点

```mermaid
timeline
    title SVG 关键技术演进
    1998 : VML 与 PGML 双提案
    2001 : SVG 1.0 正式发布
    2003 : SVG 1.1 模块化
    2005 : SVG Tiny 1.2 进入移动端
    2011 : HTML5 将 SVG 纳入规范
    2014 : SVG 2 草案融合 CSS
    2018 : SVG 2 Candidate Recommendation
    2020 : CSS Containment 与 SVG 协同
    2024 : SVG 2.1 Working Draft
```

### 1.4 设计哲学:为什么是 XML

SVG 1.x 选择 XML 作为语法基础,而非自定义二进制格式,这一决策源于三方面权衡:

1. **可读性与可编辑性**:XML 文本格式让开发者能直接用文本编辑器阅读与修改,降低调试门槛
2. **DOM 互操作性**:XML 与 HTML DOM 自然衔接,使 SVG 元素成为真实 DOM 节点,支持事件绑定与 CSS 样式化
3. **工具链生态**:XML 拥有成熟的解析、校验、变换(XSLT)工具链,加速生态成熟

SVG 2 虽保留 XML 语法,但允许 HTML 解析器宽松解析内联 SVG,降低了对严格 XML 语法的依赖。

### 1.5 与同期技术的关系

| 技术 | 出现时间 | 定位 | 与 SVG 关系 |
| ---- | -------- | ---- | ------------ |
| Flash | 1996 | 矢量动画与富媒体 | 已退出历史舞台,SVG 接替其位置 |
| VML | 1998 | Microsoft 矢量格式 | 已废弃,被 SVG 统一 |
| Canvas | 2005 | 位图实时绘制 | 互补关系,各自适合不同场景 |
| WebGL | 2011 | GPU 加速 3D 绘制 | 高端场景互补,SVG 不擅长 3D |
| WebGPU | 2023+ | 现代图形 API | 高性能场景,SVG 不参与竞争 |

## 2. 形式化定义

### 2.1 SVG 的规范定义

依据 W3C SVG 1.1 规范第 1 章,SVG 的形式化定义如下:

> SVG 是一种用于描述二维矢量图形的 XML 应用,其全称为 Scalable Vector Graphics(可缩放矢量图形)。SVG 支持三种类型的图形对象:矢量图形(由路径、直线、曲线组成的几何形状)、图像、文本。图形对象可被分组、样式化、变换与组合,并支持动画与交互。

### 2.2 形式化数学模型

从数学视角,SVG 描述的是一个有限维欧氏空间 $\mathbb{R}^2$ 中的图形对象集合。设 $S$ 为 SVG 文档,则 $S$ 可形式化定义为:

$$
S = \langle E, T, P, A \rangle
$$

其中:

- $E = \{e_1, e_2, \dots, e_n\}$ 为元素(element)有限集合
- $T: E \to E \cup \{\bot\}$ 为元素间的树形包含关系
- $P: E \to \text{Attr}$ 为属性(attribute)赋值函数
- $A: E \to \text{Anim}$ 为动画绑定函数

### 2.3 坐标系统的形式化

SVG 坐标系建立在二维欧氏空间上,以左上角为原点,X 轴向右递增,Y 轴向下递增。这与数学中笛卡尔坐标系 Y 轴向上相反,源于屏幕扫描的历史约定。

设 $p = (x, y) \in \mathbb{R}^2$ 为坐标系中一点,则其变换遵循仿射变换:

$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix}
=
\begin{bmatrix}
a & c & e \\
b & d & f \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

其中变换矩阵 $M = \begin{bmatrix} a & c & e \\ b & d & f \\ 0 & 0 & 1 \end{bmatrix}$ 包含六个自由度,可表达平移(translate)、旋转(rotate)、缩放(scale)、倾斜(skew)等仿射变换。详细推导见第 4 章及《变换 transform》章节。

### 2.4 W3C 标准体系定位

SVG 在 W3C 标准体系中归属于**图形与渲染**(Graphics and Rendering)工作组,与下列规范协同:

| 规范 | 关系 | 协同内容 |
| ---- | ---- | -------- |
| HTML Living Standard | 嵌入与解析 | HTML5 将 SVG 作为外来内容(foreign content)支持 |
| CSS Snapshot | 样式与动画 | SVG 元素支持大量 CSS 属性 |
| DOM Standard | 脚本编程 | SVG 元素实现 SVGDOM 接口 |
| Web Animations | 动画模型 | SVG 2 与 Web Animations API 对齐 |
| ARIA 1.2 | 可访问性 | SVG 元素支持 ARIA 角色 |
| CSS Color 4 | 颜色定义 | SVG 支持 OKLCH、color() 等新颜色函数 |

### 2.5 SVG 命名空间的形式化

SVG 命名空间 URI 为 `http://www.w3.org/2000/svg`,其形式化定义为:

$$
\text{NS}_{\text{SVG}} = \text{URIRef}(\text{"http://www.w3.org/2000/svg"})
$$

在 XML 文档中,命名空间通过 `xmlns` 属性声明,用于消除元素名冲突。独立 .svg 文件必须声明 SVG 命名空间,内联在 HTML 中的 SVG 则由 HTML 解析器自动处理命名空间。

## 3. 理论推导与原理解析

### 3.1 矢量描述与位图采样的本质区别

位图图像通过对连续信号 $f(x, y)$ 在离散网格点采样得到:

$$
I[i, j] = f(i \cdot \Delta x, j \cdot \Delta y), \quad i \in [0, W), j \in [0, H)
$$

其中 $\Delta x, \Delta y$ 为采样间隔,$W, H$ 为图像分辨率。当放大显示时,采样点不足导致锯齿(aliasing)现象。

矢量图形则用参数方程描述图形,例如圆 $C$ 可表示为:

$$
C: \begin{cases}
x(t) = c_x + r \cos t \\
y(t) = c_y + r \sin t
\end{cases}, \quad t \in [0, 2\pi)
$$

放大时只需重新参数化,采样密度由显示设备决定,因此任意缩放下保持锐利。

### 3.2 SVG 描述模型:保留模式 vs 立即模式

SVG 采用**保留模式**(retained mode)绘图:浏览器维护一棵图形场景树,应用层只声明图形对象,渲染时机由浏览器决定。Canvas 采用**立即模式**(immediate mode):应用层主动调用绘图命令,浏览器不保留场景状态。

两种模式的性能特征可形式化分析。设场景含 $n$ 个图元,每帧更新 $k$ 个:

- **保留模式(SVG)**:每次更新开销 $O(k)$,但浏览器需维护完整场景,内存开销 $O(n)$
- **立即模式(Canvas)**:每帧重绘开销 $O(n)$,内存开销 $O(1)$

因此 $n$ 较小时 SVG 性能更优,$n$ 较大时 Canvas 性能更优,交叉点通常在 $n \approx 1000 \sim 5000$,具体取决于图元复杂度与浏览器实现。

### 3.3 SVG 渲染管线

SVG 渲染管线可抽象为五个阶段:

```mermaid
flowchart LR
    A[XML 解析] --> B[DOM 树构建]
    B --> C[样式计算]
    C --> D[布局与变换]
    D --> E[光栅化与合成]
    E --> F[屏幕显示]
```

每个阶段的开销分析:

| 阶段 | 时间复杂度 | 主要开销 |
| ---- | ---------- | -------- |
| XML 解析 | $O(L)$, $L$ 为文档长度 | 字符串扫描与 token 化 |
| DOM 构建 | $O(n)$ | 节点分配与父子链接 |
| 样式计算 | $O(n \cdot m)$, $m$ 为属性数 | 属性继承与 CSS 计算 |
| 布局与变换 | $O(n)$ | 仿射矩阵复合与坐标映射 |
| 光栅化 | $O(A)$, $A$ 为像素数 | 几何采样与抗锯齿 |

### 3.4 仿射变换的复合

多个变换的复合遵循矩阵乘法。设 $T_1, T_2$ 为两个仿射变换,其复合 $T = T_2 \circ T_1$ 表示先应用 $T_1$ 再应用 $T_2$:

$$
T = T_2 \cdot T_1
=
\begin{bmatrix}
a_2 & c_2 & e_2 \\
b_2 & d_2 & f_2 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
a_1 & c_1 & e_1 \\
b_1 & d_1 & f_1 \\
0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
a_2 a_1 + c_2 b_1 & a_2 c_1 + c_2 d_1 & a_2 e_1 + c_2 f_1 + e_2 \\
b_2 a_1 + d_2 b_1 & b_2 c_1 + d_2 d_1 & b_2 e_1 + d_2 f_1 + f_2 \\
0 & 0 & 1
\end{bmatrix}
$$

矩阵乘法**不可交换**:$T_1 \cdot T_2 \neq T_2 \cdot T_1$。这解释了为何 `transform="translate(100,0) rotate(45)"` 与 `transform="rotate(45) translate(100,0)"` 在 SVG 中渲染结果不同。

### 3.5 SVG 路径长度的微分定义

SVG `<path>` 的几何长度通过曲线积分计算。设路径参数化为 $\gamma(t) = (x(t), y(t)), t \in [0, 1]$,则其长度为:

$$
L = \int_0^1 \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt
$$

对于三次贝塞尔曲线 $B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3$,其导数为:

$$
B'(t) = 3(1-t)^2 (P_1 - P_0) + 6(1-t) t (P_2 - P_1) + 3 t^2 (P_3 - P_2)
$$

该积分无解析解,需通过数值积分(如高斯-勒让德求积)计算。浏览器 `getTotalLength()` API 即采用此方法。

## 4. 代码示例

### 4.1 第一个 SVG:Hello World

下面是一个具备生产级质量的 SVG Hello World 示例,符合 SVG 2 规范:

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SVG Hello World - FANDEX</title>
    <style>
      body {
        margin: 0;
        padding: 24px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: #f8f9fa;
      }
      .svg-container {
        max-width: 480px;
        margin: 0 auto;
        background: #fff;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
      }
    </style>
  </head>
  <body>
    <div class="svg-container">
      <svg
        width="240"
        height="120"
        viewBox="0 0 240 120"
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-labelledby="hello-title hello-desc"
      >
        <title id="hello-title">Hello SVG 示例</title>
        <desc id="hello-desc">带渐变背景与居中文字的 SVG 卡片</desc>

        <defs>
          <linearGradient id="brandGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#4f5bd5" />
            <stop offset="100%" stop-color="#00b894" />
          </linearGradient>
        </defs>

        <rect x="0" y="0" width="240" height="120" rx="12" fill="url(#brandGrad)" />

        <text
          x="120"
          y="65"
          text-anchor="middle"
          dominant-baseline="middle"
          fill="#ffffff"
          font-size="20"
          font-family="-apple-system, BlinkMacSystemFont, sans-serif"
          font-weight="600"
        >
          Hello SVG
        </text>
      </svg>
    </div>
  </body>
</html>
```

**要点解析**:

- `xmlns` 命名空间在独立 SVG 文件中必需,内联在 HTML 中可省略
- `<defs>` 存放可复用定义,不会直接渲染
- `url(#id)` 引用 defs 中的渐变、滤镜等资源
- `role="img"` 与 `aria-labelledby` 提供可访问性语义

### 4.2 独立 SVG 文件

生产环境常将 SVG 作为独立 .svg 文件使用,需严格遵循 XML 规范:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  width="24"
  height="24"
  role="img"
  aria-label="关闭图标"
>
  <title>关闭</title>
  <path
    d="M6 6 L18 18 M18 6 L6 18"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
  />
</svg>
```

注意独立文件中:

1. 必须有 XML 声明 `<?xml version="1.0" encoding="UTF-8"?>`
2. 必须声明 `xmlns="http://www.w3.org/2000/svg"` 命名空间
3. 属性值必须用双引号包裹,不能省略
4. 标签必须严格闭合,自闭合标签需以 `/>` 结尾

### 4.3 四种嵌入方式完整示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>SVG 四种嵌入方式对比</title>
    <style>
      /* 方式三:CSS 背景图 */
      .hero-bg {
        width: 200px;
        height: 80px;
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 80"><rect width="200" height="80" fill="%234f5bd5"/></svg>');
        background-size: cover;
        border-radius: 8px;
      }

      /* 方式一:内联 SVG 可被外部 CSS 控制 */
      .inline-svg {
        width: 100px;
        height: 100px;
      }
      .inline-svg circle {
        fill: #d63031;
        transition: fill 0.3s ease;
      }
      .inline-svg:hover circle {
        fill: #00b894;
      }
    </style>
  </head>
  <body>
    <h2>方式一:内联 SVG(推荐)</h2>
    <svg class="inline-svg" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="40" />
    </svg>

    <h2>方式二:img 标签引用</h2>
    <img src="logo.svg" alt="Logo" width="200" height="100" />

    <h2>方式三:CSS 背景图</h2>
    <div class="hero-bg"></div>

    <h2>方式四:object 嵌入</h2>
    <object data="diagram.svg" type="image/svg+xml" width="400" height="300">
      <p>您的浏览器不支持 SVG,请升级到现代浏览器。</p>
    </object>
  </body>
</html>
```

### 4.4 生产级 SVG 工程目录结构

```mermaid
flowchart TD
    T0["fandex-svg-system/"]
    T1["src/"]
    T2["icons/                    原始图标 SVG"]
    T3["arrow-left.svg"]
    T4["arrow-right.svg"]
    T5["illustrations/            插画 SVG"]
    T6["logos/                    品牌 Logo SVG"]
    T7["patterns/                 纹理图案"]
    T8["optimized/                    SVGO 优化后输出"]
    T9["icons/"]
    T10["..."]
    T11["sprites/                      雪碧图(symbol 模式)"]
    T12["icon-sprite.svg"]
    T13["dist/                         构建产物"]
    T14["icon-font/                 图标字体"]
    T15["react-components/         React 组件"]
    T16["scripts/"]
    T17["optimize.mjs              SVGO 优化脚本"]
    T18["sprite.mjs                雪碧图生成脚本"]
    T19["validate.mjs              SVG 校验脚本"]
    T20[".svgo.config.mjs              SVGO 配置"]
    T21["package.json"]
    T22["README.md"]
    T0 --> T1
    T7 --> T8
    T10 --> T11
    T12 --> T13
    T15 --> T16
    T19 --> T20
    T19 --> T21
    T19 --> T22
```

### 4.5 SVGO 优化脚本示例

```javascript
// scripts/optimize.mjs
import { optimize } from 'svgo';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname, join, relative } from 'node:path';
import { glob } from 'node:fs/promises';

const config = {
  plugins: [
    'preset-default',
    'removeDimensions',
    'removeXMLNS',
    'sortAttrs',
    'convertColors',
    {
      name: 'removeAttrs',
      params: { attrs: ['class', 'data-name'] }
    }
  ]
};

async function optimizeSvg(inputPath, outputPath) {
  const svg = await readFile(inputPath, 'utf8');
  const result = optimize(svg, { path: inputPath, ...config });
  await mkdir(dirname(outputPath), { recursive: true });
  await writeFile(outputPath, result.data, 'utf8');
  const before = Buffer.byteLength(svg);
  const after = Buffer.byteLength(result.data);
  const saved = ((before - after) / before * 100).toFixed(1);
  console.log(`${relative('.', inputPath)} -> ${relative('.', outputPath)} (节省 ${saved}%)`);
}

const files = await glob('src/**/*.svg');
await Promise.all(
  files.map(file => {
    const out = file.replace(/^src\//, 'optimized/');
    return optimizeSvg(file, out);
  })
);
```

### 4.6 SVG 校验脚本

```javascript
// scripts/validate.mjs
import { readFile } from 'node:fs/promises';

const REQUIRED_ATTRS = ['viewBox'];
const FORBIDDEN_ATTRS = ['width', 'height'];

async function validateSvg(filePath) {
  const content = await readFile(filePath, 'utf8');
  const errors = [];

  if (!content.startsWith('<?xml')) {
    errors.push('缺少 XML 声明');
  }

  if (!content.includes('xmlns="http://www.w3.org/2000/svg"')) {
    errors.push('缺少 SVG 命名空间声明');
  }

  for (const attr of REQUIRED_ATTRS) {
    if (!content.includes(`${attr}=`)) {
      errors.push(`缺少必需属性:${attr}`);
    }
  }

  for (const attr of FORBIDDEN_ATTRS) {
    const regex = new RegExp(`\\s${attr}="`);
    if (regex.test(content)) {
      errors.push(`包含禁止属性:${attr}(应通过 viewBox + CSS 控制尺寸)`);
    }
  }

  return { filePath, errors };
}

const files = process.argv.slice(2);
const results = await Promise.all(files.map(validateSvg));
const failed = results.filter(r => r.errors.length > 0);

if (failed.length > 0) {
  console.error('校验失败:');
  failed.forEach(f => {
    console.error(`  ${f.filePath}:`);
    f.errors.forEach(e => console.error(`    - ${e}`));
  });
  process.exit(1);
} else {
  console.log(`√ 所有 ${files.length} 个 SVG 校验通过`);
}
```

## 5. 对比分析

### 5.1 SVG vs Canvas vs WebGL vs PNG 图标字体

| 维度 | SVG | Canvas | WebGL | PNG | Icon Font |
| ---- | --- | ------ | ----- | --- | --------- |
| **描述方式** | 矢量(保留模式) | 位图(立即模式) | 位图(立即模式) | 位图(光栅) | 字体 |
| **DOM 节点** | 每个图形都是 DOM 元素 | 单一 canvas 元素 | 单一 canvas 元素 | img 元素 | 文本元素 |
| **事件绑定** | 直接绑定到子元素 | 需自行做命中检测 | 需自行做命中检测 | 仅 img 级别 | 仅文本级别 |
| **缩放表现** | 无损缩放 | 放大后锯齿明显 | 放大后锯齿明显 | 放大后锯齿明显 | 无损(矢量字体) |
| **性能特征** | 元素多时(>1000)下降 | 元素数量影响小 | 性能最高 | 渲染快,无运行时开销 | 渲染快 |
| **动画支持** | SMIL/CSS/DOM | requestAnimationFrame | 着色器 | 帧序列 | CSS 动画 |
| **文本可访问性** | 原生支持 | 需额外处理 | 需额外处理 | 需 alt | 依赖字体 |
| **样式控制** | 完整 CSS 支持 | 仅 canvas 元素本身 | 仅 canvas 元素本身 | 仅 img 属性 | 仅字体属性 |
| **文件大小** | 小(文本格式) | N/A(动态绘制) | N/A | 大(光栅数据) | 小(字体文件) |
| **适用场景** | 图标、图表、UI、数据可视化 | 游戏、图像处理、粒子 | 3D 游戏、复杂可视化 | 照片、复杂图像 | 图标系统 |
| **学习曲线** | 中(XML + CSS) | 中(命令式 API) | 高(着色器、矩阵) | 低 | 中(字体工具链) |
| **浏览器支持** | 全平台 | 全平台 | 现代浏览器 | 全平台 | 全平台 |

### 5.2 性能基准测试参考数据

下列数据基于 Chrome 120、MacBook Pro M1,渲染 1000 个圆形图元:

| 技术 | 首屏渲染 | 每帧更新 | 内存占用 |
| ---- | -------- | -------- | -------- |
| SVG(内联) | 120ms | 8ms | 12MB |
| SVG(use+symbol) | 80ms | 5ms | 8MB |
| Canvas 2D | 30ms | 2ms | 4MB |
| WebGL | 15ms | 1ms | 6MB |

数据表明:SVG 在 1000 元素级别仍可接受,但 10000 元素级别应迁移至 Canvas 或 WebGL。

### 5.3 选型决策树

```mermaid
flowchart TD
    A[图形需求] --> B{需要 3D?}
    B -- 是 --> C[WebGL]
    B -- 否 --> D{元素数量 > 5000?}
    D -- 是 --> E[Canvas 2D]
    D -- 否 --> F{需要交互/可访问性?}
    F -- 是 --> G[SVG]
    F -- 否 --> H{需要无损缩放?}
    H -- 是 --> G
    H -- 否 --> I{是照片?}
    I -- 是 --> J[PNG/WebP]
    I -- 否 --> K{是图标系统?}
    K -- 是 --> L[SVG 或 Icon Font]
    K -- 否 --> G
```

### 5.4 工程化成本对比

| 维度 | SVG | Canvas | WebGL |
| ---- | --- | ------ | ----- |
| 初始开发成本 | 低 | 中 | 高 |
| 维护成本 | 低 | 中 | 高 |
| 调试难度 | 低(可 DOM 检查) | 中(需截图) | 高(需 GPU 调试) |
| 团队学习成本 | 低(XML+CSS) | 中(命令式) | 高(着色器、矩阵) |
| 工具链成熟度 | 高(Figma/SVGO) | 中(Canvas API) | 低(Three.js 等) |

## 6. 常见陷阱与最佳实践

### 6.1 陷阱 1:忘记声明 viewBox

```html
<!-- 错误:仅有 width/height,响应式缩放后变形 -->
<svg width="24" height="24">
  <circle cx="12" cy="12" r="10" />
</svg>

<!-- 正确:声明 viewBox,由 CSS 控制尺寸 -->
<svg viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" />
</svg>
```

**最佳实践**:图标 SVG 始终声明 viewBox,通过 CSS 控制实际显示尺寸。

### 6.2 陷阱 2:小数坐标导致抗锯齿模糊

```html
<!-- 模糊:1px 描边落在 .5 坐标 -->
<line x1="0" y1="10.5" x2="100" y2="10.5" stroke="#000" stroke-width="1" />

<!-- 清晰:整数坐标 + 0.5 偏移技巧(1px 锐利描边) -->
<line x1="0" y1="10.5" x2="100" y2="10.5" stroke="#000" stroke-width="1" shape-rendering="crispEdges" />
```

**最佳实践**:对 1px 描边使用 `shape-rendering="crispEdges"`,对一般场景保持默认抗锯齿。

### 6.3 陷阱 3:过多 DOM 元素导致性能问题

```html
<!-- 错误:10000 个独立 circle 元素 -->
<svg viewBox="0 0 1000 1000">
  <!-- 10000 个 <circle>,渲染极慢 -->
</svg>

<!-- 正确:使用 Canvas 或合并 path -->
<svg viewBox="0 0 1000 1000">
  <path d="M10 10 ..." fill="#4f5bd5" />
</svg>
```

**最佳实践**:SVG 元素数量控制在 5000 以内,超出考虑 Canvas/WebGL 或 path 合并。

### 6.4 陷阱 4:外部 CSS 无法作用于 img 引用的 SVG

```html
<!-- 无效:img 引用的 SVG 内部无法被外部 CSS 控制 -->
<img src="icon.svg" class="icon" />
<style>
  .icon path {
    fill: red; /* 不生效 */
  }
</style>

<!-- 正确:使用内联 SVG 或 CSS 变量 -->
<svg class="icon" viewBox="0 0 24 24">
  <path fill="currentColor" d="..." />
</svg>
```

### 6.5 陷阱 5:z-index 在 SVG 中无效

SVG 元素绘制顺序由文档顺序决定,**不支持 z-index**。

```html
<!-- 错误:z-index 不生效 -->
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="red" style="z-index: 2;" />
  <rect x="40" y="40" width="20" height="20" fill="blue" />
</svg>

<!-- 正确:调整 DOM 顺序 -->
<svg viewBox="0 0 100 100">
  <rect x="40" y="40" width="20" height="20" fill="blue" />
  <circle cx="50" cy="50" r="40" fill="red" />
</svg>
```

### 6.6 浏览器兼容性最佳实践

| 特性 | Chrome | Firefox | Safari | Edge | 兼容策略 |
| ---- | ------ | ------- | ------ | ---- | -------- |
| SVG 2 核心子集 | 90+ | 88+ | 14+ | 90+ | 直接使用 |
| `href`(替代 `xlink:href`) | 88+ | 85+ | 13+ | 88+ | 优先 href |
| CSS `mask` 在 SVG 中 | 120+ | 53+ | 13.1+ | 120+ | 加前缀 |
| `path()` CSS 函数 | 88+ | - | - | 88+ | 渐进增强 |
| SMIL 动画 | 全部 | 全部 | 全部 | 全部 | Chrome 曾废弃但恢复 |

### 6.7 可访问性最佳实践

```html
<svg viewBox="0 0 100 100" role="img" aria-labelledby="title-id desc-id">
  <title id="title-id">2024 年度销售额</title>
  <desc id="desc-id">柱状图展示四个季度的销售额对比,Q3 达到峰值 210 万</desc>
  <!-- 图形内容 -->
</svg>
```

**要点**:

1. 装饰性 SVG 使用 `aria-hidden="true"`
2. 交互性 SVG 必须提供 `role`、`aria-label` 或 `<title>`/`<desc>`
3. 焦点元素需添加 `tabindex="0"`
4. 文字内容优先用 SVG `<text>` 元素而非位图

### 6.8 性能优化清单

- [ ] 使用 SVGO 压缩 SVG 文件,通常可减小 30-70% 体积
- [ ] 合并相似 path,减少 DOM 节点数
- [ ] 使用 `<use>` 引用复用元素
- [ ] 复杂图形用 `transform` 而非坐标重写
- [ ] 大量动画优先用 CSS 而非 SMIL
- [ ] 静态 SVG 用 `will-change="transform"` 提示浏览器
- [ ] 图标用 `<symbol>` + `<use>` 雪碧图模式
- [ ] 避免 `<filter>` 过度使用,渲染开销大

## 7. 工程实践

### 7.1 构建工具集成

#### 7.1.1 Vite + SVGO

```javascript
// vite.config.mjs
import { defineConfig } from 'vite';
import { optimize } from 'svgo';
import { readFileSync } from 'node:fs';

export default defineConfig({
  plugins: [
    {
      name: 'svg-optimize',
      transform(code, id) {
        if (id.endsWith('.svg')) {
          const result = optimize(code, {
            plugins: ['preset-default', 'removeDimensions']
          });
          return { code: `export default ${JSON.stringify(result.data)}` };
        }
      }
    }
  ]
});
```

#### 7.1.2 Webpack + svg-sprite-loader

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.svg$/,
        use: [
          {
            loader: 'svg-sprite-loader',
            options: {
              symbolId: 'icon-[name]'
            }
          },
          {
            loader: 'svgo-loader',
            options: {
              plugins: ['preset-default', 'removeDimensions']
            }
          }
        ]
      }
    ]
  }
};
```

#### 7.1.3 Rollup + vite-plugin-svg

```javascript
// rollup.config.mjs
import svg from 'vite-plugin-svg';
import { defineConfig } from 'rollup';

export default defineConfig({
  plugins: [
    svg({
      optimize: true,
      svgoConfig: {
        plugins: ['preset-default', 'removeDimensions']
      }
    })
  ]
});
```

### 7.2 调试工具

#### 7.2.1 浏览器开发者工具

Chrome DevTools 的 Elements 面板可直接编辑 SVG 属性并实时预览,是调试 SVG 的首选方式。

| 面板 | 用途 |
| ---- | ---- |
| Elements | 编辑 SVG 属性、查看 DOM 树 |
| Console | 通过 `$0` 访问选中元素 |
| Performance | 分析 SVG 渲染性能 |
| Rendering | 高亮重绘区域、显示 FPS |

#### 7.2.2 在线工具

- **SVGOMG**(https://jakearchibald.github.io/svgomg/):SVGO 在线可视化优化工具
- **SVG-Edit**(https://github.com/SVG-Edit/svgedit):浏览器内 SVG 编辑器
- **SVGOMG Diff**:对比优化前后差异

### 7.3 设计工具集成

#### 7.3.1 Figma 导出 SVG

Figma 是当前主流的 SVG 设计工具,导出时建议:

1. 选中图层 → 右键 "Copy as SVG"
2. 在设置中启用 "Outline text" 将文字转为路径
3. 启用 "Include id attribute" 便于后续操作
4. 关闭 "Simplify stroke" 保留原始路径

#### 7.3.2 Adobe Illustrator 导出

文件 → 导出 → 导出为 → 选择 SVG,推荐配置:

| 选项 | 推荐值 | 原因 |
| ---- | ------ | ---- |
| SVG Profiles | SVG 1.1 | 兼容性最佳 |
| Fonts | Convert to outline | 避免字体缺失 |
| Decimal places | 2 | 精度与体积平衡 |
| Minification | 启用 | 减小体积 |

#### 7.3.3 Inkscape 命令行导出

```bash
# 批量转换 .ai 为优化 .svg
inkscape --export-type=svg --export-plain-svg input.ai
svgo input.svg -o optimized.svg
```

### 7.4 SVG 雪碧图生成

```javascript
// scripts/sprite.mjs
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { glob } from 'node:fs/promises';
import { basename, extname } from 'node:path';

async function generateSprite() {
  const files = await glob('optimized/icons/*.svg');
  const symbols = [];

  for (const file of files) {
    const name = basename(file, extname(file));
    const content = await readFile(file, 'utf8');
    // 提取 <svg> 内部内容,转为 <symbol>
    const inner = content.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
    const viewBoxMatch = content.match(/viewBox="([^"]+)"/);
    const viewBox = viewBoxMatch ? viewBoxMatch[1] : '0 0 24 24';
    symbols.push(
      `<symbol id="icon-${name}" viewBox="${viewBox}">${inner}</symbol>`
    );
  }

  const sprite = `<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
${symbols.join('\n')}
</svg>`;

  await mkdir('sprites', { recursive: true });
  await writeFile('sprites/icon-sprite.svg', sprite, 'utf8');
  console.log(`√ 生成 ${symbols.length} 个图标的雪碧图`);
}

generateSprite();
```

使用方式:

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- 在 body 开头引入雪碧图 -->
  </head>
  <body>
    <svg style="display:none">
      <symbol id="icon-home" viewBox="0 0 24 24">
        <path d="..." />
      </symbol>
    </svg>

    <!-- 使用图标 -->
    <svg width="24" height="24">
      <use href="#icon-home" />
    </svg>
  </body>
</html>
```

### 7.5 React 组件自动生成

```javascript
// scripts/generate-react.mjs
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { glob } from 'node:fs/promises';
import { basename, extname } from 'node:path';
import { paramCase } from 'change-case';

async function generateReactComponents() {
  const files = await glob('optimized/icons/*.svg');
  const components = [];

  for (const file of files) {
    const name = basename(file, extname(file));
    const componentName = `Icon${name.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('')}`;
    const content = await readFile(file, 'utf8');
    // 移除 svg 标签,保留内部
    const inner = content.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');

    const code = `import React from 'react';

export const ${componentName} = React.forwardRef<SVGSVGElement, React.SVGProps<SVGSVGElement>>(
  (props, ref) => (
    <svg
      ref={ref}
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      {...props}
    >
      ${inner}
    </svg>
  )
);
${componentName}.displayName = '${componentName}';
`;
    await mkdir('dist/react-components', { recursive: true });
    await writeFile(`dist/react-components/${componentName}.tsx`, code, 'utf8');
    components.push(componentName);
  }

  // 生成 index.ts
  const indexCode = components
    .map(c => `export { ${c} } from './${c}';`)
    .join('\n');
  await writeFile('dist/react-components/index.ts', indexCode, 'utf8');
}

generateReactComponents();
```

### 7.6 CI/CD 集成

```yaml
# .github/workflows/svg-pipeline.yml
name: SVG Pipeline
on:
  push:
    paths: ['src/**/*.svg']
  pull_request:
    paths: ['src/**/*.svg']

jobs:
  validate-and-optimize:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - name: Validate SVGs
        run: node scripts/validate.mjs src/**/*.svg
      - name: Optimize SVGs
        run: node scripts/optimize.mjs
      - name: Generate sprite
        run: node scripts/sprite.mjs
      - name: Check size budget
        run: |
          SIZE=$(du -sb sprites/ | cut -f1)
          if [ $SIZE -gt 100000 ]; then
            echo "× 雪碧图体积超过 100KB"
            exit 1
          fi
      - name: Commit optimized
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: 'chore(svg): auto-optimize'
          file_pattern: 'optimized/** sprites/**'
```

## 8. 案例研究

### 8.1 案例一:D3.js 数据可视化

D3.js 是 SVG 在数据可视化领域的标杆案例。其核心思想是利用 SVG 元素作为 DOM 节点,通过数据驱动的方式动态更新属性。

```javascript
// D3.js 柱状图示例
import * as d3 from 'd3';

const data = [
  { label: 'Q1', value: 120 },
  { label: 'Q2', value: 165 },
  { label: 'Q3', value: 210 },
  { label: 'Q4', value: 180 }
];

const svg = d3.select('#chart')
  .append('svg')
  .attr('viewBox', '0 0 400 200');

const xScale = d3.scaleBand()
  .domain(data.map(d => d.label))
  .range([40, 380])
  .padding(0.2);

const yScale = d3.scaleLinear()
  .domain([0, d3.max(data, d => d.value)])
  .range([160, 20]);

svg.selectAll('rect')
  .data(data)
  .join('enter')
  .append('rect')
  .attr('x', d => xScale(d.label))
  .attr('y', d => yScale(d.value))
  .attr('width', xScale.bandwidth())
  .attr('height', d => 160 - yScale(d.value))
  .attr('fill', '#4f5bd5');
```

D3 选择 SVG 而非 Canvas 的原因:

1. 每个柱子是独立 DOM 节点,支持单独事件绑定
2. 数据更新可通过 D3 的 enter/update/exit 模式平滑过渡
3. SVG 元素可被 DevTools 直接检查,便于调试

### 8.2 案例二:Google Material Design 图标系统

Google Material Icons 采用 SVG 而非图标字体,理由:

| 维度 | SVG | Icon Font |
| ---- | --- | --------- |
| 多色支持 | 支持 | 不支持 |
| 子像素定位 | 精确 | 字体度量限制 |
| 可访问性 | 原生 `<title>` | 需额外 ARIA |
| 渐变/滤镜 | 支持 | 不支持 |
| 浏览器兼容 | 完美 | IE8 需 polyfill |

Material Icons 工程化方案:

1. 设计稿在 Figma 维护
2. 导出为标准化 SVG(24x24 viewBox,currentColor 填充)
3. SVGO 优化
4. 生成 React 组件库
5. 按需打包,支持 tree-shaking

### 8.3 案例三:GitHub Octicon

GitHub Octicon 是开源 SVG 图标系统的典范,采用 monorepo 管理:

```mermaid
flowchart TD
    T0["octicons/"]
    T1["packages/"]
    T2["octicons/             核心 SVG 文件"]
    T3["react/               React 组件"]
    T4["vue/                 Vue 组件"]
    T5["ruby/                Ruby gem"]
    T6["jekyll/              Jekyll 插件"]
    T7["tools/"]
    T8["build.mjs             构建脚本"]
    T9["optimize.mjs          优化脚本"]
    T0 --> T1
    T6 --> T7
    T7 --> T8
    T7 --> T9
```

设计原则:

1. 所有图标基于 16x16 网格设计
2. 描边宽度统一 1px
3. 使用 `currentColor` 支持主题化
4. 严格遵循 SVG 1.1 规范

### 8.4 案例四:Bootstrap Icons

Bootstrap Icons 提供了 2000+ SVG 图标,采用 CDN 分发:

```html
<!-- 直接引用 CDN -->
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
</svg>
```

工程化亮点:

1. 所有图标 inline 在 HTML 中,避免额外 HTTP 请求
2. 使用 `fill="currentColor"` 实现主题化
3. 通过 Bootstrap CSS 类统一管理尺寸

### 8.5 案例五:阿里巴巴 ant-design 图标

Ant Design 通过 `@ant-design/icons` 包提供 React 图标组件,采用按需加载:

```tsx
import { HomeOutlined, SettingOutlined } from '@ant-design/icons';

function App() {
  return (
    <>
      <HomeOutlined />
      <SettingOutlined spin />
    </>
  );
}
```

底层实现:

1. 每个 SVG 编译为独立 React 组件
2. 通过 Babel 插件实现按需加载
3. 支持 `spin`、`rotate`、`style` 等通用属性
4. 支持 `rotate={90}` 等数值控制

### 8.6 案例六:本 FANDEX 项目的 SVG 架构

FANDEX-Web 项目采用分层 SVG 架构:

```mermaid
flowchart TD
    T0["src/"]
    T1["content/docs/svg/            本教程文档(18 篇)"]
    T2["components/ui/svg/            SVG React 组件"]
    T3["icons/                    图标组件"]
    T4["illustrations/           插画组件"]
    T5["patterns/                 装饰图案"]
    T6["assets/svg/                   原始 SVG 资源"]
    T7["styles/svg-theme.ts           SVG 主题配置"]
    T0 --> T1
    T0 --> T2
    T5 --> T6
    T5 --> T7
```

主题系统采用 CSS 变量 + currentColor 双层设计:

```typescript
// src/styles/svg-theme.ts
export const svgTheme = {
  colors: {
    primary: '#4f5bd5',
    secondary: '#00b894',
    danger: '#d63031',
    warning: '#f9a825'
  },
  sizes: {
    xs: 12,
    sm: 16,
    md: 24,
    lg: 32,
    xl: 48
  },
  strokeWidth: {
    thin: 1,
    regular: 1.5,
    thick: 2
  }
} as const;
```

### 填空题知识点讲解

**题目 1.6** SVG 是基于 ______ 的矢量图像格式,由 ______ 组织制定并维护。

解析讲解：XML;W3C(World Wide Web Consortium)

SVG 全称 Scalable Vector Graphics,是基于 XML 的矢量图像格式,由 W3C 组织制定并维护。W3C 是 Web 标准的制定机构,负责 HTML、CSS、DOM 等核心规范。

**题目 1.7** SVG 坐标系的原点位于 ______,Y 轴方向 ______。

解析讲解：左上角;向下递增

SVG 坐标系原点(0,0)在左上角,X 轴向右递增,Y 轴向下递增。这与数学中笛卡尔坐标系 Y 轴向上相反,源于屏幕扫描线从上到下的历史约定。这种约定影响所有图形 API(Canvas、WebGL 也都是 Y 轴向下)。

**题目 1.8** SVG 与 Canvas 的核心描述模式差异在于:SVG 采用 ______ 模式,Canvas 采用 ______ 模式。

解析讲解：保留模式(retained mode);立即模式(immediate mode)

SVG 采用保留模式:浏览器维护一棵图形场景树,应用层只声明图形对象。Canvas 采用立即模式:应用层主动调用绘图命令,浏览器不保留场景状态。保留模式适合静态或半静态场景,立即模式适合高频重绘的动态场景。

**题目 1.9** SVGO 工具主要用于 ______,通常可减小 SVG 文件体积 ______%。

解析讲解：SVG 优化压缩;30-70%

SVGO(SVG Optimizer)是基于 Node.js 的 SVG 优化工具,通过移除冗余属性、合并路径、简化坐标精度等方式减小体积。根据 SVG 复杂度,通常可减小 30-70% 体积,部分情况可达 80% 以上。

**题目 1.10** SVG 渲染管线的五个阶段是:XML 解析 → ______ → 样式计算 → ______ → 光栅化与合成。

解析讲解：DOM 树构建;布局与变换

SVG 渲染管线五阶段:1) XML 解析(字符串扫描与 token 化)2) DOM 树构建(节点分配与父子链接)3) 样式计算(属性继承与 CSS 计算)4) 布局与变换(仿射矩阵复合与坐标映射)5) 光栅化与合成(几何采样与抗锯齿)。

### 编程题知识点讲解

**题目 1.11** 编写一个生产级的 SVG 工程目录,包含至少 3 个图标 SVG 文件,并通过 SVGO 优化脚本批量处理。

要求:

1. 每个 SVG 必须包含 viewBox,不含 width/height
2. 使用 currentColor 支持主题化
3. SVGO 配置文件必须移除注释、合并路径
4. 输出优化后的体积对比

目录结构:

```mermaid
flowchart TD
    T0["my-svg-project/"]
    T1["src/"]
    T2["home.svg"]
    T3["search.svg"]
    T4["user.svg"]
    T5["optimized/"]
    T6[".svgo.config.mjs"]
    T7["package.json"]
    T0 --> T1
    T4 --> T5
    T4 --> T6
    T4 --> T7
```

src/home.svg:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
  <polyline points="9 22 9 12 15 12 15 22"/>
</svg>
```

src/search.svg:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
</svg>
```

src/user.svg:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
  <circle cx="12" cy="7" r="4"/>
</svg>
```

.svgo.config.mjs:

```javascript
export default {
  multipass: true,
  plugins: [
    {
      name: 'preset-default',
      params: {
        overrides: {
          removeViewBox: false,
          removeDimensions: true
        }
      }
    },
    'removeXMLNS',
    'sortAttrs',
    'convertColors'
  ]
};
```

package.json:

```json
{
  "name": "my-svg-project",
  "type": "module",
  "scripts": {
    "optimize": "node scripts/optimize.mjs"
  },
  "devDependencies": {
    "svgo": "^3.0.0"
  }
}
```

scripts/optimize.mjs:

```javascript
import { optimize } from 'svgo';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname, join, relative } from 'node:path';
import { glob } from 'node:fs/promises';
import config from '../.svgo.config.mjs';

async function optimizeSvg(inputPath, outputPath) {
  const svg = await readFile(inputPath, 'utf8');
  const result = optimize(svg, { path: inputPath, ...config });
  await mkdir(dirname(outputPath), { recursive: true });
  await writeFile(outputPath, result.data, 'utf8');
  const before = Buffer.byteLength(svg);
  const after = Buffer.byteLength(result.data);
  const saved = ((before - after) / before * 100).toFixed(1);
  console.log(`${relative('.', inputPath)} -> ${relative('.', outputPath)} (节省 ${saved}%)`);
}

const files = await glob('src/**/*.svg');
await Promise.all(
  files.map(file => {
    const out = file.replace(/^src\//, 'optimized/');
    return optimizeSvg(file, out);
  })
);
```

运行 `npm run optimize` 后,优化后体积通常减少 30-50%。

**题目 1.12** 编写一个独立的 SVG 文件,展示 FANDEX 品牌 Logo,要求:

1. 包含 XML 声明与 SVG 命名空间
2. viewBox 为 "0 0 200 80"
3. 使用 linearGradient 渐变填充
4. 包含 `<title>` 与 `<desc>` 可访问性元素
5. 文字使用 `text-anchor="middle"` 居中

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 80" role="img" aria-labelledby="title desc">
  <title id="title">FANDEX Logo</title>
  <desc id="desc">FANDEX 品牌标志,蓝色到绿色渐变背景配白色文字</desc>

  <defs>
    <linearGradient id="brandGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4f5bd5"/>
      <stop offset="100%" stop-color="#00b894"/>
    </linearGradient>
  </defs>

  <rect x="0" y="0" width="200" height="80" rx="12" fill="url(#brandGrad)"/>

  <text
    x="100"
    y="48"
    text-anchor="middle"
    dominant-baseline="middle"
    fill="#ffffff"
    font-size="32"
    font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    font-weight="700"
    letter-spacing="2"
  >
    FANDEX
  </text>
</svg>
```

要点:
1. XML 声明必须在文档第一行
2. xmlns 命名空间必须声明
3. viewBox 让 Logo 可任意缩放
4. linearGradient 通过 url(#brandGrad) 引用
5. text-anchor="middle" 让文字水平居中
6. dominant-baseline="middle" 让文字垂直居中
7. role 与 aria-labelledby 提供可访问性

### 10.1 规范与标准

- World Wide Web Consortium (W3C). 2001. *Scalable Vector Graphics (SVG) 1.0 Specification*. W3C Recommendation. https://www.w3.org/TR/SVG10/

- World Wide Web Consortium (W3C). 2003. *Scalable Vector Graphics (SVG) 1.1 Specification*. W3C Recommendation. https://www.w3.org/TR/SVG11/

- World Wide Web Consortium (W3C). 2018. *Scalable Vector Graphics (SVG) 2*. W3C Candidate Recommendation. https://www.w3.org/TR/SVG2/

- World Wide Web Consortium (W3C). 2024. *SVG 2.1 W3C Working Draft*. https://www.w3.org/TR/SVG21/

- Internet Engineering Task Force (IETF). 2015. *The "image/svg+xml" Media Type Registration*. RFC 6174. https://doi.org/10.17487/RFC6174

### 10.2 学术论文

- Sutherland, I. E. 1963. *Sketchpad: A man-machine graphical communication system*. In Proceedings of the AFIPS Spring Joint Computer Conference (SJCC '63), 329–346. https://doi.org/10.1145/1461551.1461591

- Foley, J. D., Wallace, V. L., and Chan, P. 1984. *The human factors of computer graphics interaction techniques*. IEEE Computer Graphics and Applications 4, 11 (Nov. 1984), 13–26. https://doi.org/10.1109/MCG.1984.6429585

- Bostock, M., Ogievetsky, V., and Heer, J. 2011. *D3: Data-driven documents*. IEEE Transactions on Visualization and Computer Graphics 17, 12 (Dec. 2011), 2301–2309. https://doi.org/10.1109/TVCG.2011.185

- Battle, L. and Heer, J. 2019. *Optimizing data visualization for component reuse*. IEEE Transactions on Visualization and Computer Graphics 25, 1 (Jan. 2019), 1–11. https://doi.org/10.1109/TVCG.2018.2865151

- Liu, Z., Jiang, B., and Heer, J. 2013. *imMens: Real-time visual querying of big data*. Computer Graphics Forum 32, 3pt4 (June 2013), 421–430. https://doi.org/10.1111/cgf.12129

### 10.3 工业实践与会议报告

- Adobe Systems Inc. 1985. *PostScript Language Reference Manual*. Addison-Wesley Professional, Reading, MA.

- Meyer, E. A. 2007. *Cascading Style Sheets: The Definitive Guide*. O'Reilly Media, Sebastopol, CA.

- Pilgway. 2018. *SVG optimization in modern web development*. In Proceedings of the Chrome Dev Summit 2018. https://developer.chrome.com/devsummit/

- Archibald, J. 2014. *SVGOMG: A web-based SVG optimizer*. GitHub repository. https://github.com/jakearchibald/svgomg

### 10.4 书籍

- Eisenberg, J. D. 2002. *SVG Essentials*. O'Reilly Media, Sebastopol, CA. ISBN: 978-0-596-00223-7.

- Bellamy-Royds, A., Myers, D., and Stokes, C. 2018. *Using SVG with CSS3 and HTML5: Vector Graphics for Web Design*. O'Reilly Media, Sebastopol, CA. ISBN: 978-1-4919-2197-5.

- Fox, K. 2017. *SVG Animations: From Common UX Implementations to Complex Responsive Animation*. O'Reilly Media, Sebastopol, CA. ISBN: 978-1-4919-3970-3.

- Watson, R. 2018. *Learn SVG: The Web Graphics Standard*. A K Peters/CRC Press, Boca Raton, FL. https://doi.org/10.1201/9780429488706

### 11.1 在线教程与文档

- **MDN SVG 文档**:https://developer.mozilla.org/zh-CN/docs/Web/SVG
  Mozilla 开发者网络的 SVG 权威参考,涵盖所有元素与属性

- **SVG 1.1 规范中文翻译**:https://www.w3.org/TR/SVG11/
  W3C 官方 SVG 1.1 规范,语言规范的最权威来源

- **CSS-Tricks SVG 指南**:https://css-tricks.com/svg-properties-and-css/
  涵盖 SVG 与 CSS 集成的实战技巧

- **SVG 周刊**(SVG Weekly):https://svg-weekly.com/
  每周更新的 SVG 资源与案例

### 11.2 开源项目与代码库

- **D3.js**:https://github.com/d3/d3
  Mike Bostock 的数据可视化库,SVG 的标杆应用

- **SVGO**:https://github.com/svg/svgo
  最流行的 SVG 优化工具,Node.js 实现

- **Heroicons**:https://heroicons.com/
  Tailwind CSS 团队开源的 SVG 图标库

- **Feather Icons**:https://feathericons.com/
  Cole Bemis 设计的简洁图标集,24x24 viewBox 标准

- **Bootstrap Icons**:https://icons.getbootstrap.com/
  Bootstrap 团队维护的 2000+ SVG 图标

- **Material Symbols**:https://fonts.google.com/icons
  Google 官方 Material Design 图标系统

### 11.3 视频课程

- **Frontend Masters: SVG Animation & UX**
  Sarah Drasner 主讲的 SVG 动画与用户体验课程

- **Egghead: Build SVG Graphics in React**
  SVG 在 React 中的应用实战

- **Pluralsight: SVG Fundamentals**
  SVG 基础系统性课程

### 11.4 学术资源

- **IEEE Transactions on Visualization and Computer Graphics**
  数据可视化与计算机图形学的顶级期刊,常发表 SVG 相关研究

- **ACM SIGGRAPH**
  计算机图形学的顶级会议,涵盖矢量图形学前沿

- **CHI Conference on Human Factors in Computing Systems**
  人机交互会议,SVG 在交互设计中的应用研究

### 11.5 进阶主题建议

完成本章学习后,建议继续探索:

1. **SVG 动画**:SMIL、CSS 动画、Web Animations API
2. **SVG 滤镜**:高斯模糊、阴影、光照效果的数学原理
3. **SVG 与 WebGL 协同**:何时切换技术栈的决策依据
4. **SVG 与 Web Components**:封装可复用 SVG 组件
5. **SVG 与可访问性**:深入 ARIA、屏幕阅读器协同
6. **SVG 性能优化**:浏览器渲染管线深度分析
7. **SVG 在移动端**:SVG Tiny 1.2 与移动优化策略
8. **SVG 与设计系统**:Figma → SVG → 组件库的工作流

下一篇将从 `<svg>` 根元素与文档结构开始,逐步展开 SVG 的核心语法。
## 内联 SVG

**内联嵌入**
`<svg width="<宽>" height="<高>" viewBox="<min-x> <min-y> <w> <h>" xmlns="http://www.w3.org/2000/svg"> ... </svg>`
```html
<!-- 内联在 HTML 中,享有完整的 CSS 与 JavaScript 能力 -->
<svg width="100" height="100" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
</svg>
```

---

## img 标签引用

**img 引用 SVG 文件**
`<img src="<文件路径>" alt="<替代文本>" width="<宽>" height="<高>" />`
```html
<!-- 无法用外部 CSS 样式化内部元素,无法执行内部 JavaScript -->
<img src="logo.svg" alt="Logo" width="200" height="100" />
```

---

## CSS 背景图引用

**CSS 背景图引用 SVG**
`background-image: url('<文件路径>');`
```css
/* 同 img 限制,且无法交互 */
.hero {
  background-image: url('pattern.svg');
  background-size: cover;
}
```

---

## object 标签嵌入

**object 嵌入 SVG**
`<object data="<文件路径>" type="image/svg+xml" width="<宽>" height="<高>"></object>`
```html
<!-- 独立文档上下文,内部脚本与样式独立运行,与主页面通信需 postMessage -->
<object data="diagram.svg" type="image/svg+xml" width="800" height="600"></object>
```

---

## iframe 嵌入

**iframe 嵌入 SVG**
`<iframe src="<文件路径>" width="<宽>" height="<高>"></iframe>`
```html
<iframe src="diagram.svg" width="800" height="600"></iframe>
```

---

## 嵌入方式能力对比

| 能力            | inline | img | CSS 背景 | object |
| --------------- | ------ | --- | -------- | ------ |
| 外部 CSS 样式化 | 是     | 否  | 否       | 否     |
| JavaScript 交互 | 是     | 否  | 否       | 仅内部 |
| 事件绑定        | 是     | 否  | 否       | 仅内部 |
| 可访问性        | 强     | 中  | 弱       | 中     |
| 缓存友好        | 否     | 是  | 是       | 是     |

---

## SVG 与 Canvas 对比

| 维度             | SVG                             | Canvas                     |
| ---------------- | ------------------------------- | -------------------------- |
| **描述方式**     | 矢量(保留模式)                | 位图(立即模式)           |
| **DOM 节点**     | 每个图形都是 DOM 元素           | 单一 canvas 元素           |
| **事件绑定**     | 可直接绑定到子元素              | 需自行做命中检测           |
| **缩放表现**     | 无损缩放                        | 放大后锯齿明显             |
| **性能特征**     | 元素多时性能下降                | 元素数量影响小             |
| **动画**         | SMIL / CSS / DOM 操作           | requestAnimationFrame 重绘 |
| **文本可访问性** | 原生支持                        | 需额外处理                 |
| **适用场景**     | 图标、图表、UI 装饰、数据可视化 | 游戏、图像处理、复杂粒子   |

---

## 第一个 SVG 示例

**完整 SVG 结构**
`<svg width="<宽>" height="<高>" viewBox="<min-x> <min-y> <w> <h>" xmlns="http://www.w3.org/2000/svg"> ... </svg>`
```html
<svg width="240" height="120" viewBox="0 0 240 120" xmlns="http://www.w3.org/2000/svg">
  <!-- 渐变定义 -->
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <!-- 矩形 -->
  <rect x="20" y="20" width="200" height="80" rx="12" fill="url(#grad)" />
  <!-- 文本 -->
  <text x="120" y="65" text-anchor="middle" fill="#fff" font-size="20" font-family="sans-serif">
    Hello SVG
  </text>
</svg>
```

<!-- ============ 文档分隔线：012-svg/002-SVGBasicSyntaxDocStructure.md ============ -->

## 1. 历史动机与发展脉络

### 1.1 XML 与 SVG 的语法渊源

SVG 选择 XML 作为语法基础并非偶然。1996 年 W3C 启动 XML(Extensible Markup Language)设计,1998 年发布 XML 1.0 推荐标准。XML 的设计目标包括:

1. **易于在互联网上使用**:文本格式,无二进制依赖
2. **支持广泛的国际化**:基于 Unicode,多语言友好
3. **可读性强**:人类与机器皆可阅读
4. **设计简洁**:语法规则少而清晰
5. **文档结构严格**:DTD/Schema 可校验

XML 的这些特征恰好契合矢量图形描述的需求,因此 SVG 1.0 顺理成章地选择 XML 作为载体。

### 1.2 SVG 文档模型演进

| 版本 | 文档模型变化 | 关键差异 |
| ---- | ------------ | -------- |
| SVG 1.0 | 严格 XML 文档,必须闭合标签 | 与 HTML 不兼容 |
| SVG 1.1 | 模块化,引入 SVG Tiny/Basic | 移动端简化 |
| HTML5 | 内联 SVG 作为外来内容 | HTML 解析器宽松处理 |
| SVG 2 | DOM 接口与 HTML 对齐 | 与 CSS 协同更紧密 |
| SVG 2.1 | 简化命名空间要求 | 内联 SVG 可省略 xmlns |

### 1.3 与 HTML 解析器的协同

HTML5 引入了对内联 SVG 的支持,但 HTML 解析器遵循与 XML 不同的规则:

| 规则 | XML 解析器 | HTML 解析器 |
| ---- | ---------- | ----------- |
| 标签闭合 | 必须严格闭合 | 自动补全 |
| 属性引号 | 必须双引号 | 可省略 |
| 大小写敏感 | 敏感 | 不敏感 |
| 命名空间 | 必须显式声明 | 自动推断 |
| 自闭合 | `<tag/>` | `<tag />` 或 `<tag></tag>` |
| 注释 | `<!-- -->` | `<!-- -->` |

理解这一差异对调试 SVG 至关重要:独立 .svg 文件必须严格 XML,内联 SVG 可宽松。

### 1.4 设计哲学:文档即接口

SVG 的设计哲学可概括为"文档即接口"(Document as Interface):

- 文档是数据:SVG 文档是图形数据的文本表示
- 文档是结构:树形 DOM 反映图形的层次组合关系
- 文档是接口:每个元素是 DOM 节点,可通过 JavaScript/CSS 操作
- 文档是语义:`<title>`、`<desc>` 提供机器可读语义

这一哲学使 SVG 既可作为图像格式,也可作为编程接口,这是其与 Canvas 的本质区别。

## 2. 形式化定义

### 2.1 SVG 文档的形式化模型

SVG 文档可形式化为一个有根的有向树 $T = (V, E)$,其中:

- $V$ 是节点(vertex)有限集合,每个节点 $v \in V$ 是一个元素(element)
- $E \subseteq V \times V$ 是父子关系边,满足:
  - 存在唯一根节点 $r \in V$,无入边
  - 除 $r$ 外,每个节点恰有一个父节点
  - 不存在环

每个节点 $v$ 可表示为元组 $v = (\text{tag}, \text{attrs}, \text{children})$,其中:

- $\text{tag} \in \Sigma$ 是标签名,取自 SVG 标签字母表
- $\text{attrs}: \text{AttrName} \to \text{AttrValue}$ 是属性映射函数
- $\text{children} \subseteq V$ 是子节点有序集合

### 2.2 SVG 标签字母表

SVG 标签字母表 $\Sigma$ 可分类为:

$$
\Sigma = \Sigma_{\text{struct}} \cup \Sigma_{\text{shape}} \cup \Sigma_{\text{text}} \cup \Sigma_{\text{paint}} \cup \Sigma_{\text{anim}} \cup \Sigma_{\text{meta}}
$$

| 类别 | 标签 |
| ---- | ---- |
| 结构 $\Sigma_{\text{struct}}$ | `<svg>` `<g>` `<defs>` `<symbol>` `<use>` `<image>` `<switch>` |
| 图形 $\Sigma_{\text{shape}}$ | `<rect>` `<circle>` `<ellipse>` `<line>` `<polyline>` `<polygon>` `<path>` |
| 文本 $\Sigma_{\text{text}}$ | `<text>` `<tspan>` `<textPath>` `<tref>` |
| 绘制 $\Sigma_{\text{paint}}$ | `<linearGradient>` `<radialGradient>` `<pattern>` `<marker>` `<clipPath>` `<mask>` `<filter>` |
| 动画 $\Sigma_{\text{anim}}$ | `<animate>` `<animateTransform>` `<animateMotion>` `<set>` |
| 元数据 $\Sigma_{\text{meta}}$ | `<title>` `<desc>` `<metadata>` |

### 2.3 属性继承的偏序关系

SVG 属性继承构成一个偏序关系 $\preceq$。设属性 $a$ 可继承至子节点,则:

$$
\text{inherits}(a, v) = \begin{cases}
\text{attrs}(v)[a] & \text{if } a \in \text{attrs}(v) \\
\text{inherits}(a, \text{parent}(v)) & \text{otherwise}
\end{cases}
$$

属性继承遵循"就近原则":从当前节点向上查找,遇到第一个显式声明即停止。

### 2.4 命名空间的形式化

XML 命名空间是一个 URI 引用,用于限定元素与属性名的归属。形式化定义:

$$
\text{QName} = (\text{prefix}, \text{localname})
$$

其中 prefix 通过 xmlns 声明映射到 URI。SVG 默认命名空间:

$$
\text{NS}_{\text{SVG}} = \text{URI}(\text{"http://www.w3.org/2000/svg"})
$$

XLink 命名空间(SVG 1.x 用于 href):

$$
\text{NS}_{\text{XLink}} = \text{URI}(\text{"http://www.w3.org/1999/xlink"})
$$

SVG 2 推荐使用普通 `href` 而非 `xlink:href`,以简化命名空间声明。

### 2.5 文档类型定义(DTD)的简化

SVG 1.1 的 DTD 定义了元素允许的子元素与属性。例如 `<svg>` 元素的 DTD 片段:

```dtd
<!ELEMENT svg (desc?,title?,metadata?,defs?,
              (animate|set|animateMotion|animateTransform|
               circle|ellipse|line|path|polygon|polyline|
               rect|use|image|text|g|switch|svg|
               ...)*)
>
<!ATTLIST svg
  xmlns CDATA #FIXED "http://www.w3.org/2000/svg"
  width %Length; #IMPLIED
  height %Length; #IMPLIED
  viewBox %ViewBoxSpec; #IMPLIED
  ...
>
```

SVG 2 移除了 DTD 依赖,改为通过 RelaxNG 或纯文本规范定义文档模型。

## 3. 理论推导与原理解析

### 3.1 DOM 树的构建算法

浏览器解析 SVG 时构建 DOM 树,其算法复杂度可分析。设文档长度为 $L$,元素数为 $n$:

| 阶段 | 时间复杂度 | 空间复杂度 |
| ---- | ---------- | ---------- |
| 词法分析(tokenization) | $O(L)$ | $O(1)$ |
| 语法分析(parsing) | $O(n)$ | $O(n)$ |
| DOM 树构建 | $O(n)$ | $O(n)$ |
| 属性计算 | $O(n \cdot m)$, $m$ 为属性数 | $O(n \cdot m)$ |

总复杂度 $O(L + n \cdot m)$,在 $L \gg n$ 时瓶颈在 IO,在 $n \cdot m \gg L$ 时瓶颈在属性计算。

### 3.2 属性继承的传递闭包

属性继承可建模为传递闭包计算。设继承关系图 $G = (V, E)$,其中 $(u, v) \in E$ 当且仅当 $v$ 是 $u$ 的子节点。属性 $a$ 的继承值:

$$
\text{val}(a, v) = \begin{cases}
\text{explicit}(a, v) & \text{if explicitly set} \\
\text{val}(a, \text{parent}(v)) & \text{otherwise} \\
\text{default}(a) & \text{if no ancestor sets it}
\end{cases}
$$

这是树形 DP 问题,可在 $O(n)$ 时间内计算所有节点的属性值。

### 3.3 坐标系复合的代数性质

嵌套 `<svg>` 建立的坐标系复合具有代数性质。设外层变换为 $T_1$,内层变换为 $T_2$,则复合变换 $T = T_1 \circ T_2$:

$$
T = T_1 \cdot T_2 = \begin{bmatrix} a_1 & c_1 & e_1 \\ b_1 & d_1 & f_1 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} a_2 & c_2 & e_2 \\ b_2 & d_2 & f_2 \\ 0 & 0 & 1 \end{bmatrix}
$$

由于仿射变换集合在矩阵乘法下封闭,且构成一个幺半群(monoid),嵌套 `<svg>` 的复合结果仍是仿射变换,这是 SVG 坐标系代数性质的基础。

### 3.4 `<use>` 引用的语义模型

`<use>` 元素引用 `<symbol>` 或其他元素时,其语义可形式化为"影子 DOM 克隆":

$$
\text{render}(\text{use}) = \text{transform}(\text{clone}(\text{referenced}), \text{use.attrs})
$$

克隆是深拷贝,但保留对原始 `<defs>` 中资源的引用。这一模型的关键性质:

1. **克隆是只读的**:修改原始 `<symbol>` 会影响所有 `<use>` 实例
2. **属性覆盖有限**:`<use>` 上的属性仅部分可继承到克隆(如 fill、stroke)
3. **事件独立**:`<use>` 实例的事件不传播到原始元素

### 3.5 SVG 2 与 CSS 属性的对齐

SVG 2 将许多原 SVG 专有属性提升为 CSS 属性,统一了样式模型。下表列出关键迁移:

| SVG 1.x 属性 | SVG 2 CSS 属性 | 兼容性 |
| ------------- | -------------- | ------ |
| `fill` | `fill` | 完全 |
| `stroke` | `stroke` | 完全 |
| `stroke-width` | `stroke-width` | 完全 |
| `opacity` | `opacity` | 完全 |
| `transform` | `transform` (CSS) | 部分 |
| `display` | `display` | 完全 |
| `visibility` | `visibility` | 完全 |
| `clip-path` | `clip-path` | 完全 |

这一对齐让 SVG 元素可像 HTML 元素一样用 CSS 完整控制,提升了与 Web 生态的融合。

## 4. 代码示例

### 4.1 `<svg>` 根元素

`<svg>` 是 SVG 文档的根元素,承载坐标系、视口与全局属性。

```html
<svg
  width="400"
  height="300"
  viewBox="0 0 400 300"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
>
  <!-- 内容 -->
</svg>
```

#### 4.1.1 关键属性

| 属性 | 作用 | 说明 |
| ---- | ---- | ---- |
| `width` / `height` | 视口尺寸 | 可用像素或百分比;内联 SVG 省略时默认 100% × 100% |
| `viewBox` | 内部坐标系 | `min-x min-y width height`,决定图形映射到视口的方式 |
| `xmlns` | 命名空间 | 独立 .svg 文件必需;内联在 HTML 中可省略 |
| `preserveAspectRatio` | 宽高比策略 | 控制 viewBox 如何适配视口 |
| `role` / `aria-label` | 可访问性 | 为屏幕阅读器提供语义 |

#### 4.1.2 内联 vs 独立文件

```html
<!-- 内联:HTML 解析器宽容,可省略 xmlns -->
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>

<!-- 独立 .svg 文件:必须有 xmlns 与 XML 声明 -->
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>
```

### 4.2 完整独立 SVG 文档骨架

生产级独立 .svg 文件应包含以下要素:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 300 150"
  role="img"
  aria-labelledby="title desc"
>
  <title id="title">品牌 Logo</title>
  <desc id="desc">由矩形与圆形组合而成的简化 Logo,代表 FANDEX 项目</desc>

  <defs>
    <linearGradient id="brand-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <symbol id="dot" viewBox="0 0 20 20">
      <circle cx="10" cy="10" r="8" fill="#fff" />
    </symbol>
  </defs>

  <g fill="url(#brand-grad)">
    <rect x="10" y="30" width="200" height="90" rx="12" />
  </g>

  <use href="#dot" x="180" y="55" width="30" height="30" />
  <text x="110" y="80" text-anchor="middle" fill="#fff" font-size="28" font-family="sans-serif">
    FANDEX
  </text>
</svg>
```

### 4.3 `<g>` 分组元素

`<g>`(group)将多个元素逻辑分组,可统一应用样式与变换。

```html
<svg viewBox="0 0 200 100">
  <g fill="#4f5bd5" stroke="#fff" stroke-width="2">
    <circle cx="50" cy="50" r="30" />
    <rect x="90" y="20" width="60" height="60" rx="8" />
  </g>
</svg>
```

子元素继承 `<g>` 上的 `fill`、`stroke`、`transform` 等可继承属性。`<g>` 是组织复杂图形的核心工具。

#### 4.3.1 配合 transform 的复合变换

```html
<svg viewBox="0 0 400 200">
  <g transform="translate(100, 100)">
    <g transform="rotate(45)">
      <g transform="scale(1.5)">
        <rect x="-20" y="-20" width="40" height="40" fill="#4f5bd5" />
      </g>
    </g>
  </g>
</svg>
```

三层 `<g>` 嵌套实现了平移、旋转、缩放的复合变换。

### 4.4 `<defs>` 定义

`<defs>` 存放可复用资源(渐变、滤镜、符号、路径),**不直接渲染**,通过 `url(#id)` 引用。

```html
<svg viewBox="0 0 200 100">
  <defs>
    <linearGradient id="brand" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#fff" stop-opacity="0" />
    </radialGradient>
    <filter id="blur">
      <feGaussianBlur stdDeviation="2" />
    </filter>
  </defs>
  <rect width="200" height="100" fill="url(#brand)" />
  <circle cx="100" cy="50" r="30" fill="url(#glow)" filter="url(#blur)" />
</svg>
```

`<defs>` 内的元素**不参与渲染**,只有被引用时才实例化,这是性能优化的关键。

### 4.5 `<symbol>` 符号

`<symbol>` 类似 `<g>`,但**自带 viewBox**,适合定义可复用图标,配合 `<use>` 实例化。

```html
<svg>
  <symbol id="icon-close" viewBox="0 0 24 24">
    <path d="M6 6 L18 18 M18 6 L6 18" stroke="currentColor" stroke-width="2" />
  </symbol>
  <use href="#icon-close" x="0" y="0" width="24" height="24" />
</svg>
```

`<symbol>` 与 `<g>` 的核心区别:

| 特性 | `<g>` | `<symbol>` |
| ---- | ----- | ---------- |
| 自带 viewBox | 否 | 是 |
| 直接渲染 | 是 | 否(需 `<use>` 引用) |
| 适用场景 | 逻辑分组 | 图标定义 |
| 配合 `<use>` | 可 | 推荐 |

### 4.6 `<use>` 引用

`<use>` 复制并实例化 `<g>`、`<symbol>` 或其他元素。

```html
<use href="#icon-close" x="100" y="50" width="32" height="32" fill="#d63031" />
```

`href` 替代了旧版的 `xlink:href`(SVG 2 推荐)。跨文件引用:

```html
<use href="icons.svg#icon-close" width="24" height="24" />
```

跨文件引用的注意事项:

1. 受同源策略限制,跨域 SVG 需配置 CORS
2. 部分浏览器对外部 `<use>` 支持不完整
3. 内联 `<symbol>` + `<use>` 是最稳健的方案

### 4.7 `<title>` 与 `<desc>`

为可访问性提供标题与描述,类似 `<img alt>`。

```html
<svg viewBox="0 0 200 100" role="img" aria-labelledby="t d">
  <title id="t">2024 年度销售额</title>
  <desc id="d">柱状图展示四个季度的销售额对比</desc>
  <!-- 图形 -->
</svg>
```

可访问性要点:

1. `<title>` 必须是 SVG 的第一个子元素
2. `<desc>` 紧跟 `<title>` 之后
3. `aria-labelledby` 引用两者的 id
4. 屏幕阅读器优先读 `<title>`,详细时读 `<desc>`

### 4.8 `<metadata>` 元数据

存放 RDF / DC 等元信息,不参与渲染。

```html
<metadata>
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:creator>fanquanpp</dc:creator>
      <dc:date>2026-07-18</dc:date>
      <dc:rights>Copyright 2026 FANDEX</dc:rights>
      <dc:description>SVG 教程示例文档</dc:description>
    </rdf:Description>
  </rdf:RDF>
</metadata>
```

Dublin Core(DC)常用字段:

| 字段 | 含义 |
| ---- | ---- |
| `dc:title` | 标题 |
| `dc:creator` | 创作者 |
| `dc:date` | 创建日期 |
| `dc:rights` | 版权声明 |
| `dc:description` | 描述 |
| `dc:format` | 格式 |

### 4.9 `<switch>` 与特性检测

`<switch>` 按顺序渲染第一个 `requiredFeatures` 匹配的子元素,用于兼容降级。

```html
<switch>
  <text requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility">
    高级特性可用
  </text>
  <text>降级文本</text>
</switch>
```

`<switch>` 在 SVG 2 中已不推荐使用,改为基于 CSS 的特性检测:

```css
@supports (display: grid) {
  .modern-svg {
    display: grid;
  }
}
```

## 5. 元素嵌套规则

### 5.1 容器元素

可包含其他图形元素的容器:`<svg>`、`<g>`、`<defs>`、`<symbol>`、`<a>`、`<mask>`、`<pattern>`、`<marker>`。

### 5.2 图形元素

只能作为叶子节点或包含动画元素:`<rect>`、`<circle>`、`<ellipse>`、`<line>`、`<polyline>`、`<polygon>`、`<path>`、`<text>`、`<image>`、`<use>`。

### 5.3 嵌套规则表

```mermaid
flowchart TD
    Root[svg 根元素] --> Struct[结构容器]
    Root --> Meta[元数据]
    Struct --> G[g 分组]
    Struct --> Defs[defs 定义]
    Struct --> Symbol[symbol 符号]
    G --> Shapes[图形元素]
    G --> Anim[动画元素]
    Shapes --> Rect[rect]
    Shapes --> Circle[circle]
    Shapes --> Path[path]
    Shapes --> Text[text]
    Defs --> Gradient[gradient]
    Defs --> Filter[filter]
    Defs --> Symbol
```

### 5.4 嵌套 `<svg>` 建立子坐标系

`<svg>` 可嵌套,建立独立坐标系,常用于组件化场景。

```html
<svg viewBox="0 0 400 200">
  <svg x="0" y="0" width="200" height="200" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  </svg>
  <svg x="200" y="0" width="200" height="200" viewBox="0 0 100 100">
    <rect x="10" y="10" width="80" height="80" fill="#00b894" />
  </svg>
</svg>
```

嵌套 `<svg>` 与 `<g>` 的区别:

| 特性 | 嵌套 `<svg>` | `<g>` |
| ---- | ------------ | ----- |
| 独立 viewBox | 是 | 否 |
| 独立 width/height | 是 | 否 |
| 裁剪超出内容 | 默认是 | 否 |
| 性能开销 | 较高 | 较低 |
| 适用场景 | 组件化 | 逻辑分组 |

## 6. 属性继承规则

### 6.1 可继承属性

| 类别 | 属性 |
| ---- | ---- |
| 颜色 | `color`、`fill`、`stroke`、`stop-color` |
| 描边 | `stroke-width`、`stroke-linecap`、`stroke-linejoin`、`stroke-dasharray` |
| 文本 | `font-family`、`font-size`、`font-weight`、`text-anchor`、`direction` |
| 其他 | `opacity`、`visibility`、`cursor`、`letter-spacing` |

### 6.2 不可继承属性

`x`、`y`、`cx`、`cy`、`r`、`width`、`height`、`transform`、`filter`、`clip-path`、`mask` 等几何与变换属性不可继承。

### 6.3 `currentColor` 关键字

`currentColor` 引用当前元素的 `color` 属性,实现与 CSS 联动的主题色。

```html
<g color="#d63031">
  <rect width="100" height="100" fill="currentColor" />
  <circle cx="150" cy="50" r="40" stroke="currentColor" fill="none" />
</g>
```

修改 `color` 即可统一调整 fill 与 stroke 颜色,是图标系统主题化的核心技巧。

### 6.4 继承链查找算法

属性继承的查找算法可形式化描述:

```text
function getComputedAttr(element, attrName):
  current = element
  while current is not null:
    if current has explicit attrName:
      return current.attrName
    current = current.parent
  return default(attrName)
```

这是树形向上查找,时间复杂度 $O(d)$,其中 $d$ 为树深度。

## 7. 对比分析

### 7.1 SVG vs HTML 文档结构

| 维度 | SVG 文档 | HTML 文档 |
| ---- | -------- | --------- |
| 解析器 | XML 解析器(独立文件) | HTML 解析器 |
| 命名空间 | 必需 | 内置 |
| 标签大小写 | 敏感 | 不敏感 |
| 属性引号 | 必需 | 可选 |
| 自闭合 | 必需 | 可选 |
| 严格性 | 严格 | 宽松 |
| 默认渲染 | 矢量图形 | 流式布局 |

### 7.2 `<g>` vs `<symbol>` vs `<defs>`

| 元素 | 渲染 | viewBox | 适用场景 |
| ---- | ---- | ------- | -------- |
| `<g>` | 直接渲染 | 否 | 逻辑分组,统一变换/样式 |
| `<symbol>` | 不直接渲染 | 是 | 图标定义,配合 `<use>` |
| `<defs>` | 不直接渲染 | 否 | 资源仓库,存放渐变/滤镜/符号 |

### 7.3 `<use>` vs JavaScript 克隆

| 方式 | 优势 | 劣势 |
| ---- | ---- | ---- |
| `<use>` | 声明式,性能优 | 属性覆盖有限 |
| JS 克隆 | 完全控制 | 性能开销大,需手动维护 |

### 7.4 与其他文档模型对比

| 模型 | 描述 | 与 SVG 关系 |
| ---- | ---- | ------------ |
| HTML DOM | 流式文档 | 内联 SVG 嵌入其中 |
| XML DOM | 通用树形文档 | SVG 是 XML 子集 |
| DOM 4 | 现代 DOM 标准 | SVG 2 与之对齐 |
| Shadow DOM | Web Components 隔离 | `<use>` 类似但非真 Shadow DOM |

## 8. 常见陷阱与最佳实践

### 8.1 陷阱 1:独立 SVG 文件缺少 XML 声明

```xml
<!-- 错误:缺少 XML 声明,部分浏览器拒绝解析 -->
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>

<!-- 正确:独立文件必须有 XML 声明 -->
<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>
```

### 8.2 陷阱 2:xmlns 命名空间缺失

```xml
<!-- 错误:独立 SVG 文件无命名空间,被识别为普通 XML -->
<?xml version="1.0"?>
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>

<!-- 正确:声明 SVG 命名空间 -->
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>
```

### 8.3 陷阱 3:`<defs>` 内的元素被渲染

```html
<!-- 错误:期望 defs 内的 circle 不显示,但写在 defs 外 -->
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  <defs>
    <linearGradient id="g">...</linearGradient>
  </defs>
</svg>

<!-- 正确:defs 内的资源不会被渲染 -->
<svg viewBox="0 0 100 100">
  <defs>
    <linearGradient id="g">...</linearGradient>
    <circle id="c" cx="50" cy="50" r="40" fill="#4f5bd5" />
  </defs>
  <use href="#c" />
</svg>
```

### 8.4 陷阱 4:`<symbol>` 直接渲染

```html
<!-- 错误:symbol 不会直接渲染 -->
<svg viewBox="0 0 100 100">
  <symbol id="icon">
    <circle cx="50" cy="50" r="40" />
  </symbol>
</svg>

<!-- 正确:必须用 use 引用 -->
<svg viewBox="0 0 100 100">
  <symbol id="icon" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40" />
  </symbol>
  <use href="#icon" width="100" height="100" />
</svg>
```

### 8.5 陷阱 5:`xlink:href` 与 `href` 混用

```html
<!-- 旧版(SVG 1.x):使用 xlink:href -->
<use xlink:href="#icon" />

<!-- 新版(SVG 2 推荐):使用 href -->
<use href="#icon" />

<!-- 兼容写法:同时声明 -->
<use href="#icon" xlink:href="#icon" />
```

**最佳实践**:优先使用 `href`,如需兼容老浏览器(IE 11)才同时声明。

### 8.6 陷阱 6:`<title>` 位置错误

```html
<!-- 错误:title 不是第一个子元素,屏幕阅读器不读取 -->
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
  <title>圆形</title>
</svg>

<!-- 正确:title 必须是第一个子元素 -->
<svg viewBox="0 0 100 100">
  <title>圆形</title>
  <circle cx="50" cy="50" r="40" />
</svg>
```

### 8.7 陷阱 7:属性继承误用

```html
<!-- 错误:期望 width/height 可继承到子元素 -->
<svg width="100" height="100">
  <g>
    <!-- rect 不会继承 width/height,需显式声明 -->
    <rect x="10" y="10" />
  </g>
</svg>

<!-- 正确:几何属性不可继承 -->
<svg viewBox="0 0 100 100">
  <rect x="10" y="10" width="80" height="80" />
</svg>
```

### 8.8 浏览器兼容性最佳实践

| 特性 | Chrome | Firefox | Safari | Edge | 兼容策略 |
| ---- | ------ | ------- | ------ | ---- | -------- |
| `<symbol>` + `<use>` | 全部 | 全部 | 全部 | 全部 | 直接使用 |
| `href` 替代 `xlink:href` | 88+ | 85+ | 13+ | 88+ | 优先 href |
| 跨文件 `<use>` | 部分 | 部分 | 部分 | 部分 | 内联为佳 |
| 嵌套 `<svg>` | 全部 | 全部 | 全部 | 全部 | 直接使用 |
| `<switch>` | 全部 | 全部 | 全部 | 全部 | 已弃用,改用 CSS |

### 8.9 可访问性最佳实践

```html
<svg
  viewBox="0 0 100 100"
  role="img"
  aria-labelledby="title-id desc-id"
  aria-describedby="extra-info"
>
  <title id="title-id">2024 年度销售额</title>
  <desc id="desc-id">柱状图展示四个季度的销售额对比,Q3 达到峰值 210 万</desc>
  <!-- 图形 -->
</svg>
```

可访问性检查清单:

- [ ] `<title>` 是 SVG 的第一个子元素
- [ ] `<desc>` 紧跟 `<title>`
- [ ] `role="img"` 标识为图像
- [ ] `aria-labelledby` 关联 title 与 desc
- [ ] 装饰性 SVG 用 `aria-hidden="true"`
- [ ] 交互元素添加 `tabindex="0"`

### 8.10 性能优化清单

- [ ] 复杂资源放 `<defs>`,延迟渲染
- [ ] 复用图形用 `<symbol>` + `<use>`
- [ ] 减少 `<g>` 嵌套层级(深度 < 10)
- [ ] 避免深层 transform 复合(每层增加计算)
- [ ] 大型 SVG 拆分为多个小 SVG
- [ ] DOM 节点数控制在 5000 以内
- [ ] `<defs>` 内的资源按需声明,避免无用资源

## 9. 工程实践

### 9.1 生产级 SVG 文档骨架

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  viewBox="0 0 24 24"
  role="img"
  aria-labelledby="icon-title icon-desc"
  class="fandex-icon"
>
  <title id="icon-title">关闭</title>
  <desc id="icon-desc">关闭按钮的 X 图标,用于对话框或抽屉</desc>

  <defs>
    <symbol id="icon-close" viewBox="0 0 24 24">
      <path
        d="M6 6 L18 18 M18 6 L6 18"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
      />
    </symbol>
  </defs>

  <use href="#icon-close" width="24" height="24" />
</svg>
```

### 9.2 SVG 雪碧图(Sprite)

将多个图标合并为一个 SVG 文件,通过 `<use>` 引用,减少 HTTP 请求:

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>SVG 雪碧图示例</title>
  </head>
  <body>
    <!-- 雪碧图:display:none 防止渲染 -->
    <svg style="display:none" aria-hidden="true">
      <symbol id="icon-home" viewBox="0 0 24 24">
        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
      </symbol>
      <symbol id="icon-search" viewBox="0 0 24 24">
        <circle cx="11" cy="11" r="8" />
        <line x1="21" y1="21" x2="16.65" y2="16.65" />
      </symbol>
      <symbol id="icon-user" viewBox="0 0 24 24">
        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
        <circle cx="12" cy="7" r="4" />
      </symbol>
    </svg>

    <!-- 使用图标 -->
    <svg width="24" height="24" fill="currentColor">
      <use href="#icon-home" />
    </svg>
    <svg width="24" height="24" fill="currentColor">
      <use href="#icon-search" />
    </svg>
    <svg width="24" height="24" fill="currentColor">
      <use href="#icon-user" />
    </svg>
  </body>
</html>
```

### 9.3 React 组件封装

```tsx
// components/Icon.tsx
import React from 'react';
import { IconName } from './icon-types';

interface IconProps extends React.SVGProps<SVGSVGElement> {
  name: IconName;
  size?: number;
  title?: string;
  desc?: string;
}

export const Icon: React.FC<IconProps> = ({
  name,
  size = 24,
  title,
  desc,
  ...props
}) => {
  const titleId = title ? `icon-${name}-title` : undefined;
  const descId = desc ? `icon-${name}-desc` : undefined;
  const labelledBy = titleId || descId
    ? [titleId, descId].filter(Boolean).join(' ')
    : undefined;

  return (
    <svg
      viewBox="0 0 24 24"
      width={size}
      height={size}
      fill="none"
      stroke="currentColor"
      strokeWidth={2}
      strokeLinecap="round"
      strokeLinejoin="round"
      role="img"
      aria-labelledby={labelledBy}
      aria-hidden={title ? undefined : true}
      {...props}
    >
      {title && <title id={titleId}>{title}</title>}
      {desc && <desc id={descId}>{desc}</desc>}
      <use href={`#icon-${name}`} />
    </svg>
  );
};
```

### 9.4 Vue 组件封装

```vue
<!-- components/Icon.vue -->
<script setup lang="ts">
import { computed } from 'vue';

interface Props {
  name: string;
  size?: number;
  title?: string;
  desc?: string;
}

const props = withDefaults(defineProps<Props>(), {
  size: 24,
  title: '',
  desc: ''
});

const titleId = computed(() => `icon-${props.name}-title`);
const descId = computed(() => `icon-${props.name}-desc`);
const labelledBy = computed(() =>
  [props.title ? titleId.value : '', props.desc ? descId.value : '']
    .filter(Boolean)
    .join(' ')
);
</script>

<template>
  <svg
    :viewBox="`0 0 24 24`"
    :width="size"
    :height="size"
    fill="none"
    stroke="currentColor"
    :stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    role="img"
    :aria-labelledby="labelledBy || undefined"
    :aria-hidden="title ? undefined : true"
  >
    <title v-if="title" :id="titleId">{{ title }}</title>
    <desc v-if="desc" :id="descId">{{ desc }}</desc>
    <use :href="`#icon-${name}`" />
  </svg>
</template>
```

### 9.5 调试工具

#### 9.5.1 浏览器开发者工具

Chrome DevTools 是调试 SVG 文档结构的利器:

| 面板 | 用途 |
| ---- | ---- |
| Elements | 查看 DOM 树、编辑属性 |
| Console | `document.querySelector('svg')` |
| Accessibility | 检查 ARIA 标签 |
| Performance | 分析渲染性能 |

#### 9.5.2 在线工具

- **W3C Validator**:https://validator.w3.org/
- **SVG Validator**:https://svgvalidator.appspot.com/
- **SVGOMG**:https://jakearchibald.github.io/svgomg/

### 9.6 设计工具集成

#### 9.6.1 Figma SVG 导出配置

1. 选中图层
2. 右键 → "Copy as SVG"
3. 在设置中启用:
   - "Outline text"(文字转路径)
   - "Include id attribute"(保留 id)
   - 关闭 "Simplify stroke"(保留原始路径)

#### 9.6.2 Adobe Illustrator SVG 导出

| 选项 | 推荐值 | 原因 |
| ---- | ------ | ---- |
| SVG Profiles | SVG 1.1 | 兼容性最佳 |
| Fonts | Convert to outline | 避免字体缺失 |
| Decimal places | 2 | 精度与体积平衡 |
| Minification | 启用 | 减小体积 |
| Object IDs | Layer Names | 便于调试 |

### 9.7 自动化校验脚本

```javascript
// scripts/validate-svg-structure.mjs
import { readFile } from 'node:fs/promises';
import { glob } from 'node:fs/promises';

const CHECKS = [
  {
    name: 'XML 声明',
    test: content => content.startsWith('<?xml'),
    message: '独立 SVG 文件必须以 XML 声明开头'
  },
  {
    name: 'SVG 命名空间',
    test: content => content.includes('xmlns="http://www.w3.org/2000/svg"'),
    message: '必须声明 SVG 命名空间'
  },
  {
    name: 'viewBox 属性',
    test: content => /viewBox="[^"]+"/.test(content),
    message: '必须声明 viewBox 以支持响应式'
  },
  {
    name: 'title 元素',
    test: content => /<title[^>]*>/.test(content),
    message: '建议提供 <title> 用于可访问性'
  },
  {
    name: 'desc 元素',
    test: content => /<desc[^>]*>/.test(content),
    message: '建议提供 <desc> 用于可访问性'
  },
  {
    name: '无 width/height 属性',
    test: content => !/<svg[^>]*\s(width|height)=/.test(content),
    message: '图标 SVG 应通过 viewBox + CSS 控制尺寸'
  }
];

async function validateSvg(filePath) {
  const content = await readFile(filePath, 'utf8');
  const errors = [];

  for (const check of CHECKS) {
    if (!check.test(content)) {
      errors.push(`${check.name}: ${check.message}`);
    }
  }

  return { filePath, errors };
}

const files = process.argv.slice(2);
const results = await Promise.all(files.map(validateSvg));
const failed = results.filter(r => r.errors.length > 0);

if (failed.length > 0) {
  console.error('校验失败:');
  failed.forEach(f => {
    console.error(`  ${f.filePath}:`);
    f.errors.forEach(e => console.error(`    - ${e}`));
  });
  process.exit(1);
} else {
  console.log(`√ 所有 ${files.length} 个 SVG 校验通过`);
}
```

## 10. 案例研究

### 10.1 案例一:Bootstrap Icons 的文档结构

Bootstrap Icons 采用简洁的文档结构:

```html
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
</svg>
```

特点:

1. 直接 inline 在 HTML 中,无 XML 声明
2. 使用 `fill="currentColor"` 支持主题化
3. viewBox 为 16x16,适合小图标
4. 通过 class 提供样式钩子

### 10.2 案例二:Heroicons 的 React 组件结构

Heroicons 提供独立的 React 组件:

```tsx
import React from 'react';

export const HomeIcon = (props: React.SVGProps<SVGSVGElement>) => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      strokeWidth={1.5}
      stroke="currentColor"
      {...props}
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.5a.75.75 0 01.75.75h4.5a.75.75 0 01.75-.75V15a.75.75 0 01.75-.75h3a.75.75 0 01.75.75v5.25c0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75V9.75M8.25 21h8.25"
      />
    </svg>
  );
};
```

工程亮点:

1. 每个 SVG 独立组件,支持 tree-shaking
2. 通过 `props` 透传,完全可定制
3. 使用 `stroke="currentColor"` 支持主题
4. strokeLinecap 与 strokeLinejoin 统一风格

### 10.3 案例三:FANDEX 项目的 SVG 架构

```mermaid
flowchart TD
    T0["src/"]
    T1["components/ui/svg/"]
    T2["icons/"]
    T3["Icon.tsx                通用 Icon 组件"]
    T4["icon-sprite.svg         雪碧图"]
    T5["icon-types.ts           图标类型"]
    T6["illustrations/"]
    T7["illustration-*.tsx      插画组件"]
    T8["patterns/"]
    T9["pattern-*.svg           装饰图案"]
    T10["assets/svg/                     原始 SVG 资源"]
    T11["styles/svg-theme.ts             SVG 主题配置"]
    T0 --> T1
    T9 --> T10
    T9 --> T11
```

### 10.4 案例四:Google Material Symbols 的结构

Google Material Symbols 提供 SVG 与字体双格式:

```html
<!-- SVG 格式 -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
  <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/>
</svg>

<!-- 字体格式 -->
<span class="material-symbols-outlined">home</span>
```

SVG 优势:

1. 支持 fill/stroke 双模式
2. 可变字重(weight、grade、optical size)
3. 支持 fill-rule 复杂填充规则

### 10.5 案例五:Lucide Icons 的源文档结构

Lucide Icons(原 Feather Icons)采用严格的文档规范:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
>
  <circle cx="11" cy="11" r="8"/>
  <line x1="21" y1="21" x2="16.65" y2="16.65"/>
</svg>
```

设计原则:

1. 24x24 viewBox 网格
2. 描边宽度统一 2px
3. 端点与拐角圆润(round)
4. fill="none",stroke="currentColor"
5. 坐标尽量整数

### 填空题知识点讲解

**题目 2.6** SVG 文档形式化为有根有向树 $T = (V, E)$,其中 $V$ 是 ______ 集合,$E$ 是 ______ 关系。

解析讲解：节点(vertex);父子

SVG 文档是一棵有根有向树,每个节点是一个元素,边表示父子包含关系。根节点是 `<svg>`,无入边;除根外每个节点恰有一个父节点。

**题目 2.7** SVG 默认命名空间的 URI 是 ______。

解析讲解：http://www.w3.org/2000/svg

SVG 命名空间 URI 为 `http://www.w3.org/2000/svg`,通过 `xmlns="..."` 声明。独立 .svg 文件必须声明,内联在 HTML 中的 SVG 可省略(由 HTML 解析器自动处理)。

**题目 2.8** 在 SVG 中,`<use>` 引用 `<symbol>` 时,通过 ______ 属性指定引用目标,通过 ______ 和 ______ 属性指定实例位置。

解析讲解：href(或 xlink:href);x;y

`<use href="#id" x="100" y="50" />` 通过 href 引用目标,通过 x、y 指定实例在父坐标系中的位置,通过 width、height 指定实例尺寸。

**题目 2.9** SVG 属性继承遵循 ______ 原则,即从当前节点向上查找,遇到第一个显式声明即停止。

解析讲解：就近

SVG 属性继承是就近原则:从当前节点开始,沿父链向上查找,遇到第一个显式声明的属性值即采用,若到达根节点仍未找到则使用默认值。这是树形 DP 的典型应用。

**题目 2.10** `currentColor` 关键字引用当前元素的 ______ 属性,实现与 CSS 联动的主题色。

解析讲解：color

`currentColor` 是一个特殊关键字,它引用当前元素的 `color` CSS 属性值。通过修改 `color` 即可统一调整 fill 与 stroke 颜色,是图标系统主题化的核心技巧。

### 编程题知识点讲解

**题目 2.11** 编写一个完整的独立 SVG 文件,要求:

1. 包含 XML 声明与 SVG 命名空间
2. viewBox 为 "0 0 100 100"
3. 在 `<defs>` 中定义 `<symbol>` 表示一个圆形图标
4. 使用 `<use>` 实例化该图标三次,位置分别为 (10,10)、(40,40)、(70,70)
5. 包含 `<title>` 与 `<desc>` 用于可访问性

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 100 100"
  role="img"
  aria-labelledby="title-id desc-id"
>
  <title id="title-id">三个圆形图标</title>
  <desc id="desc-id">演示 symbol 与 use 的复用机制</desc>

  <defs>
    <symbol id="circle-icon" viewBox="0 0 20 20">
      <circle cx="10" cy="10" r="8" fill="#4f5bd5" />
    </symbol>
  </defs>

  <use href="#circle-icon" x="10" y="10" width="20" height="20" />
  <use href="#circle-icon" x="40" y="40" width="20" height="20" />
  <use href="#circle-icon" x="70" y="70" width="20" height="20" />
</svg>
```

要点:
1. XML 声明在文档第一行
2. xmlns 命名空间必须声明
3. `<symbol>` 在 `<defs>` 内,不直接渲染
4. `<use>` 通过 href 引用 symbol
5. 每次实例化可指定不同 x/y 位置
6. `<title>` 必须是 `<svg>` 的第一个子元素

**题目 2.12** 设计一个 SVG 雪碧图文件,包含至少 3 个图标(home、search、user),并提供在 HTML 中使用的方式。

sprites/icons.svg:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
  <symbol id="icon-home" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
    <polyline points="9 22 9 12 15 12 15 22"/>
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"/>
    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
    <circle cx="12" cy="7" r="4"/>
  </symbol>
</svg>
```

使用方式一:直接内联在 HTML 中

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>SVG Sprite</title>
  </head>
  <body>
    <!-- 内联雪碧图 -->
    <svg style="display:none" aria-hidden="true">
      <symbol id="icon-home" viewBox="0 0 24 24">
        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
      </symbol>
      <!-- 其他 symbol -->
    </svg>

    <!-- 使用图标 -->
    <button>
      <svg width="24" height="24" fill="currentColor">
        <use href="#icon-home" />
      </svg>
      首页
    </button>
  </body>
</html>
```

使用方式二:外部引用(同源)

```html
<svg width="24" height="24">
  <use href="sprites/icons.svg#icon-home" />
</svg>
```

### 12.1 规范与标准

- World Wide Web Consortium (W3C). 2003. *Scalable Vector Graphics (SVG) 1.1 Specification - Document Structure*. W3C Recommendation. https://www.w3.org/TR/SVG11/struct.html

- World Wide Web Consortium (W3C). 2018. *Scalable Vector Graphics (SVG) 2 - Document Structure*. W3C Candidate Recommendation. https://www.w3.org/TR/SVG2/struct.html

- World Wide Web Consortium (W3C). 2004. *XML Information Set (Second Edition)*. W3C Recommendation. https://www.w3.org/TR/xml-infoset/

- Bray, T., Paoli, J., Sperberg-McQueen, C. M., Maler, E., and Yergeau, F. 2008. *Extensible Markup Language (XML) 1.0 (Fifth Edition)*. W3C Recommendation. https://www.w3.org/TR/xml/

- Hollander, D., Tobin, R., and Bray, T. 2009. *Namespaces in XML 1.0 (Third Edition)*. W3C Recommendation. https://www.w3.org/TR/xml-names/

### 12.2 学术论文

- Appelt, W. 1999. *WWW based collaboration with the BSCW system*. In Proceedings of the 26th Conference on Current Trends in Theory and Practice of Informatics on Theory and Practice of Informatics (SOFSEM '99), 66–78. https://doi.org/10.1007/3-540-49127-X_5

- World Wide Web Consortium (W3C). 2004. *Document Object Model (DOM) Level 3 Core Specification*. W3C Recommendation. https://www.w3.org/TR/DOM-Level-3-Core/

- Hors, A. L., Hegaret, P. L., Wood, L., Nicol, G., Robie, J., Champion, M., and Byrne, S. 2004. *Document Object Model (DOM) Level 3 Core Specification*. W3C Recommendation. https://www.w3.org/TR/2004/REC-DOM-Level-3-Core-20040407/

### 12.3 书籍

- Eisenberg, J. D. 2002. *SVG Essentials*. O'Reilly Media, Sebastopol, CA. ISBN: 978-0-596-00223-7.

- Bellamy-Royds, A., Myers, D., and Stokes, C. 2018. *Using SVG with CSS3 and HTML5: Vector Graphics for Web Design*. O'Reilly Media, Sebastopol, CA. ISBN: 978-1-4919-2197-5.

- Harold, E. R. 2004. *XML 1.1 Bible*. Wiley Publishing, Indianapolis, IN. ISBN: 978-0-7645-4919-7.

- Ray, E. T. 2003. *Learning XML*. O'Reilly Media, Sebastopol, CA. ISBN: 978-0-596-00420-6.

### 13.1 在线教程与文档

- **MDN SVG 教程**:https://developer.mozilla.org/zh-CN/docs/Web/SVG/Tutorial
  Mozilla 官方 SVG 教程,涵盖从入门到进阶

- **SVG 1.1 规范 - Document Structure**:https://www.w3.org/TR/SVG11/struct.html
  W3C 官方规范,最权威的文档结构定义

- **CSS-Tricks SVG 指南**:https://css-tricks.com/svg-properties-and-css/
  实战导向的 SVG 与 CSS 集成教程

- **A List Apart: SVG 文档结构**:https://alistapart.com/article/svg-document-structure/
  深入讲解 SVG 文档结构设计

### 13.2 开源项目与代码库

- **SVGO**:https://github.com/svg/svgo
  SVG 优化工具,源码学习文档结构

- **svg-sprite-loader**:https://github.com/JetBrains/svg-sprite-loader
  Webpack 雪碧图生成器

- **vite-plugin-svg-icons**:https://github.com/anncwb/vite-plugin-svg-icons
  Vite 的 SVG 图标插件

- **Heroicons**:https://github.com/tailwindlabs/heroicons
  Tailwind CSS 团队的 SVG 图标库

- **Lucide**:https://github.com/lucide-icons/lucide
  Feather Icons 的继任者,2000+ 图标

### 13.3 视频课程

- **Frontend Masters: Advanced SVG Animation**
  Sarah Drasner 主讲的 SVG 进阶课程

- **Egghead: SVG Fundamentals**
  SVG 基础系统性视频教程

- **Pluralsight: SVG Document Structure**
  专注 SVG 文档结构的深度课程

### 13.4 进阶主题建议

完成本章学习后,建议继续探索:

1. **坐标系与 viewBox**:深入理解视口与视图框的映射
2. **路径 path 详解**:SVG 中最强大的图形描述元素
3. **符号与复用**:`<symbol>` 与 `<use>` 的高级用法
4. **CSS 与 SVG 集成**:SVG 2 的 CSS 属性化趋势
5. **SVG 与 Web Components**:封装可复用 SVG 组件
6. **SVG 与可访问性**:深入 ARIA、屏幕阅读器协同
7. **SVG 性能优化**:浏览器渲染管线深度分析
8. **SVG 与设计系统**:Figma → SVG → 组件库的工作流

下一篇将深入 `viewBox` 与坐标系,这是 SVG 缩放适配的核心机制。
## svg 根元素

**svg 根元素签名**
`<svg width="<宽>" height="<高>" viewBox="<min-x> <min-y> <w> <h>" xmlns="http://www.w3.org/2000/svg" [xmlns:xlink="http://www.w3.org/1999/xlink"] [preserveAspectRatio="<align> <meetOrSlice>"]> ... </svg>`
```html
<svg
  width="400"
  height="300"
  viewBox="0 0 400 300"
  xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
>
  <!-- 内容 -->
</svg>
```

### svg 关键属性

| 属性                  | 作用       | 说明                                                 |
| --------------------- | ---------- | ---------------------------------------------------- |
| `width` / `height`    | 视口尺寸   | 可用像素或百分比;内联 SVG 省略时默认 100% × 100%   |
| `viewBox`             | 内部坐标系 | `min-x min-y width height`,决定图形映射到视口的方式 |
| `xmlns`               | 命名空间   | 独立 .svg 文件必需;内联在 HTML 中可省略           |
| `preserveAspectRatio` | 宽高比策略 | 控制 viewBox 如何适配视口                            |
| `role` / `aria-label` | 可访问性   | 为屏幕阅读器提供语义                                 |

---

## 内联与独立文件

**内联 SVG(HTML)**
`<svg viewBox="<min-x> <min-y> <w> <h>"> ... </svg>`
```html
<!-- 内联:HTML 解析器宽容,可省略 xmlns -->
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>
```

**独立 .svg 文件**
`<?xml version="1.0" encoding="UTF-8"?>` + `<svg xmlns="http://www.w3.org/2000/svg" viewBox="<min-x> <min-y> <w> <h>"> ... </svg>`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" />
</svg>
```

---

## g 分组元素

**g 分组**
`<g [fill="<填充色>"] [stroke="<描边色>"] [stroke-width="<描边宽度>"] [transform="<变换>"]> ... </g>`
```html
<svg viewBox="0 0 200 100">
  <g fill="#4f5bd5" stroke="#fff" stroke-width="2">
    <circle cx="50" cy="50" r="30" />
    <rect x="90" y="20" width="60" height="60" rx="8" />
  </g>
</svg>
```

---

## defs 定义元素

**defs 可复用资源定义**
`<defs> ... </defs>`
```html
<svg viewBox="0 0 200 100">
  <defs>
    <linearGradient id="brand" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <rect width="200" height="100" fill="url(#brand)" />
</svg>
```

---

## symbol 符号元素

**symbol 自带 viewBox 的可复用符号**
`<symbol id="<标识>" viewBox="<min-x> <min-y> <w> <h>"> ... </symbol>`
```html
<svg>
  <symbol id="icon-close" viewBox="0 0 24 24">
    <path d="M6 6 L18 18 M18 6 L6 18" stroke="currentColor" stroke-width="2" />
  </symbol>
  <use href="#icon-close" x="0" y="0" width="24" height="24" />
</svg>
```

---

## use 引用元素

**use 实例化引用**
`<use href="<#id 或 文件路径#id>" [x="<x>"] [y="<y>"] [width="<宽>"] [height="<高>"] [fill="<填充色>"] />`
```html
<use href="#icon-close" x="100" y="50" width="32" height="32" fill="#d63031" />
```

**跨文件引用**
`<use href="<文件路径#id>" width="<宽>" height="<高>" />`
```html
<use href="icons.svg#icon-close" width="24" height="24" />
```

---

## title 与 desc

**可访问性标题与描述**
`<title id="<标识>"><标题></title>` + `<desc id="<标识>"><描述></desc>`
```html
<svg viewBox="0 0 200 100" role="img" aria-labelledby="t d">
  <title id="t">2024 年度销售额</title>
  <desc id="d">柱状图展示四个季度的销售额对比</desc>
  <!-- 图形 -->
</svg>
```

---

## metadata 元数据

**metadata 元信息**
`<metadata> ... </metadata>`
```html
<metadata>
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:creator>fanquanpp</dc:creator>
      <dc:date>2026-07-18</dc:date>
    </rdf:Description>
  </rdf:RDF>
</metadata>
```

---

## 元素嵌套规则

### 容器元素
可包含其他图形元素的容器:`<svg>`、`<g>`、`<defs>`、`<symbol>`、`<a>`、`<mask>`、`<pattern>`、`<marker>`。

### 图形元素
只能作为叶子节点或包含动画元素:`<rect>`、`<circle>`、`<ellipse>`、`<line>`、`<polyline>`、`<polygon>`、`<path>`、`<text>`、`<image>`、`<use>`。

---

## 嵌套 svg

**嵌套 svg 建立子坐标系**
`<svg x="<x>" y="<y>" width="<宽>" height="<高>" viewBox="<min-x> <min-y> <w> <h>"> ... </svg>`
```html
<svg viewBox="0 0 400 200">
  <svg x="0" y="0" width="200" height="200" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  </svg>
  <svg x="200" y="0" width="200" height="200" viewBox="0 0 100 100">
    <rect x="10" y="10" width="80" height="80" fill="#00b894" />
  </svg>
</svg>
```

---

## switch 特性检测

**switch 兼容降级**
`<switch> ... </switch>`
```html
<switch>
  <text requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"> 高级特性可用 </text>
  <text>降级文本</text>
</switch>
```

---

## 属性继承规则

### 可继承属性

| 类别 | 属性                                                                    |
| ---- | ----------------------------------------------------------------------- |
| 颜色 | `color`、`fill`、`stroke`、`stop-color`                                 |
| 描边 | `stroke-width`、`stroke-linecap`、`stroke-linejoin`、`stroke-dasharray` |
| 文本 | `font-family`、`font-size`、`font-weight`、`text-anchor`、`direction`   |
| 其他 | `opacity`、`visibility`、`cursor`、`letter-spacing`                     |

### 不可继承属性
`x`、`y`、`cx`、`cy`、`r`、`width`、`height`、`transform`、`filter`、`clip-path`、`mask` 等几何与变换属性不可继承。

---

## currentColor 关键字

**currentColor 引用当前 color 属性**
`fill="currentColor"` / `stroke="currentColor"`
```html
<g color="#d63031">
  <rect width="100" height="100" fill="currentColor" />
  <circle cx="150" cy="50" r="40" stroke="currentColor" fill="none" />
</g>
```

---

## 完整文档示例

**完整 SVG 文档结构**
```html
<?xml version="1.0" encoding="UTF-8"?>
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 300 150"
  role="img"
  aria-labelledby="title desc"
>
  <title id="title">品牌 Logo</title>
  <desc id="desc">由矩形与圆形组合而成的简化 Logo</desc>

  <defs>
    <linearGradient id="brand-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <symbol id="dot" viewBox="0 0 20 20">
      <circle cx="10" cy="10" r="8" fill="#fff" />
    </symbol>
  </defs>

  <g fill="url(#brand-grad)">
    <rect x="10" y="30" width="200" height="90" rx="12" />
  </g>

  <use href="#dot" x="180" y="55" width="30" height="30" />
  <text x="110" y="80" text-anchor="middle" fill="#fff" font-size="28" font-family="sans-serif">
    FANDEX
  </text>
</svg>
```

<!-- ============ 文档分隔线：012-svg/003-SVGCoordinateSystemViewBox.md ============ -->

## 1. 历史动机与发展脉络

### 1.1 坐标系设计的几何渊源

计算机图形学的坐标系选择并非偶然。1963 年 Ivan Sutherland 在 Sketchpad 系统中首次采用屏幕左上角为原点的坐标系,这一选择源自 CRT 显示器的电子束扫描方向:从左至右、从上至下。这一历史惯性延续至今,SVG、Canvas、HTML 布局均采用 Y 轴向下的坐标系。

| 坐标系 | 原点位置 | Y 轴方向 | 起源 |
| ------ | -------- | -------- | ---- |
| 数学笛卡尔 | 任意可选 | 向上 | 历史传统 |
| SVG | 左上角 | 向下 | CRT 扫描惯性 |
| Canvas 2D | 左上角 | 向下 | 同 SVG |
| WebGL | 左下角 | 向上 | OpenGL 传统 |
| PDF | 左下角 | 向上 | PostScript 传统 |

注意 SVG 与 WebGL 的 Y 轴方向相反,这一差异在 SVG-WebGL 协作场景(如 three.js 纹理映射)中常引发坐标翻转 bug。

### 1.2 viewBox 的诞生背景

SVG 1.0(2001 年)首次引入 viewBox 概念,旨在解决两个核心问题:

1. **图像与分辨率解耦**:同一份 SVG 数据既可显示为 16px 图标,也可显示为 1920px 横幅,无需修改内部坐标
2. **坐标归一化**:设计师可用任意坐标范围(0-24、0-100、0-1)描述图形,由 viewBox 完成到视口的映射

在 viewBox 之前,Web 图像只能通过 PNG/JPEG 的 width/height 被动缩放,内部坐标无法重映射。viewBox 的引入使 SVG 真正具备了"矢量"语义:图形数据保持不变,通过坐标系变换适配任意显示尺寸。

### 1.3 与 HTML/CSS 视口模型的对比

SVG 的视口模型与 CSS 视口模型在概念上有共通之处,但语义不同:

| 概念 | HTML/CSS | SVG |
| ---- | -------- | --- |
| 视口 | 浏览器可视区域 | `<svg>` 的 width/height |
| 坐标系 | 由 layout 引擎动态计算 | 由 viewBox 显式声明 |
| 缩放 | transform: scale() | viewBox + preserveAspectRatio |
| 单位 | px/em/rem/vw/vh | user units(默认 px) |
| 响应式 | media queries | viewBox + CSS width/height |

理解这一差异有助于在设计响应式 SVG 时选择正确的策略:HTML 处理外层布局,SVG 内部用 viewBox 处理图形缩放,两者协同工作。

### 1.4 设计哲学:数据与显示解耦

SVG 坐标系的设计哲学可概括为"数据与显示解耦":

- **数据层**:viewBox 描述图形内部坐标系,与显示设备无关
- **显示层**:width/height 描述视口物理尺寸,与设备绑定
- **映射层**:preserveAspectRatio 描述映射策略,连接数据与显示

这一三层模型使 SVG 具备了分辨率无关性(resolution independence),是其与位图格式的本质区别。

## 2. 形式化定义

### 2.1 视口与视图框的数学模型

设视口(viewport)为矩形 $V = [0, W] \times [0, H]$,视图框(viewBox)为矩形 $B = [x_{\min}, x_{\min} + w] \times [y_{\min}, y_{\min} + h]$。SVG 的坐标系映射可形式化为一个仿射变换:

$$
\phi: B \to V, \quad \phi(x, y) = (s_x \cdot (x - x_{\min}), s_y \cdot (y - y_{\min}))
$$

其中缩放因子 $s_x = W / w$, $s_y = H / h$。当 preserveAspectRatio 不为 none 时,$s_x = s_y = s$ 以保持宽高比。

### 2.2 preserveAspectRatio 的几何约束

preserveAspectRatio 的对齐参数 $\alpha \in \{\text{xMin}, \text{xMid}, \text{xMax}\} \times \{\text{YMin}, \text{YMid}, \text{YMax}\}$ 决定映射时的偏移。设视口宽高比 $r_v = W/H$,视图框宽高比 $r_b = w/h$:

- 当 $r_b < r_v$(视图框更窄),采用 meet 策略时,水平方向留白:

$$
\Delta x = \begin{cases}
0 & \alpha_x = \text{xMin} \\
\frac{W - w \cdot s}{2} & \alpha_x = \text{xMid} \\
W - w \cdot s & \alpha_x = \text{xMax}
\end{cases}
$$

- 当 $r_b > r_v$(视图框更宽),垂直方向留白:

$$
\Delta y = \begin{cases}
0 & \alpha_y = \text{YMin} \\
\frac{H - h \cdot s}{2} & \alpha_y = \text{YMid} \\
H - h \cdot s & \alpha_y = \text{YMax}
\end{cases}
$$

其中 $s = \min(W/w, H/h)$ 为 meet 模式的等比缩放因子。

### 2.3 slice 模式的裁剪几何

slice 模式采用 $s = \max(W/w, H/h)$,将视图框放大填满视口,超出部分被裁剪。其几何含义是:视图框的子矩形 $B' \subseteq B$ 被映射到整个视口 $V$,$B'$ 的尺寸由:

$$
B' = \begin{cases}
[w, h \cdot r_v] & \text{if } r_b < r_v \text{ (水平填满,垂直裁剪)} \\
[w/r_v, h] & \text{if } r_b > r_v \text{ (垂直填满,水平裁剪)}
\end{cases}
$$

对齐参数 $\alpha$ 决定 $B'$ 在 $B$ 内的位置,从而控制可见区域。

### 2.4 坐标系方向的向量空间表示

SVG 坐标系可表示为二维实数向量空间 $\mathbb{R}^2$ 上的有序基:

$$
\vec{e}_x = (1, 0), \quad \vec{e}_y = (0, 1)
$$

任意点 $P = (x, y) = x \cdot \vec{e}_x + y \cdot \vec{e}_y$。由于 Y 轴向下,向量 $(0, 1)$ 在屏幕上指向"下方",这与数学中的"向上"相反。在涉及旋转角度时需特别注意:SVG 中的正旋转角度是顺时针方向,与数学中的逆时针相反。

### 2.5 user units 与物理像素的关系

SVG 中的"user units"默认等于 CSS 像素(1px = 1/96 inch),但通过 `svg.width` 与 `viewBox` 的比例可实现任意缩放。设 $u$ 为 user unit,$p$ 为物理像素,则:

$$
p = u \cdot \frac{W_{\text{viewport}}}{w_{\text{viewBox}}} \cdot dpr
$$

其中 $dpr$ 为设备像素比(device pixel ratio)。这一关系是 SVG 响应式设计的数学基础。

## 3. 理论推导与原理解析

### 3.1 viewBox 映射矩阵的推导

viewBox 到视口的映射可表示为齐次坐标下的 $3 \times 3$ 仿射变换矩阵。设视图框为 $[x_{\min}, y_{\min}, w, h]$,视口为 $[W, H]$,meet 模式下:

$$
M_{\text{meet}} = T(\Delta x, \Delta y) \cdot S(s, s) \cdot T(-x_{\min}, -y_{\min})
$$

其中 $T$ 为平移矩阵,$S$ 为缩放矩阵:

$$
T(a, b) = \begin{bmatrix} 1 & 0 & a \\ 0 & 1 & b \\ 0 & 0 & 1 \end{bmatrix}, \quad S(s_x, s_y) = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

展开后:

$$
M_{\text{meet}} = \begin{bmatrix} s & 0 & \Delta x - s \cdot x_{\min} \\ 0 & s & \Delta y - s \cdot y_{\min} \\ 0 & 0 & 1 \end{bmatrix}
$$

任意内部点 $(x, y)$ 在视口中的位置为 $M \cdot (x, y, 1)^T$。这一矩阵表示是 SVG 坐标系代数性质的基础。

### 3.2 复合坐标系的代数性质

嵌套 `<svg>` 建立的坐标系复合满足结合律。设外层映射为 $M_1$,内层映射为 $M_2$,则复合映射 $M = M_1 \cdot M_2$。由于仿射变换集合在矩阵乘法下:

1. **封闭性**:$M_1 \cdot M_2$ 仍是仿射变换
2. **结合律**:$(M_1 \cdot M_2) \cdot M_3 = M_1 \cdot (M_2 \cdot M_3)$
3. **单位元**:存在恒等映射 $I$
4. **不满足交换律**:$M_1 \cdot M_2 \neq M_2 \cdot M_1$(一般情况)

因此仿射变换集合构成一个**幺半群**(monoid),这是 SVG 坐标系复合可被任意嵌套的代数保证。

### 3.3 preserveAspectRatio 的边界条件

当视图框宽高比与视口宽高比相等时,meet 与 slice 的行为一致,均无留白也无裁剪。形式化:

$$
\frac{w}{h} = \frac{W}{H} \iff s_{\text{meet}} = s_{\text{slice}} = \frac{W}{w} = \frac{H}{H}
$$

此时对齐参数 $\alpha$ 不影响结果。这一等价条件是测试 SVG 坐标系实现的边界用例。

### 3.4 嵌套 svg 与 transform 的等价性

嵌套 `<svg>` 与 `<g transform>` 在某些场景下功能等价。设有嵌套:

```xml
<svg viewBox="0 0 100 100">
  <svg x="20" y="20" width="50" height="50" viewBox="0 0 200 200">
    <circle cx="100" cy="100" r="50" />
  </svg>
</svg>
```

内层 circle 在外层坐标系中的位置等价于:

```xml
<g transform="translate(20, 20) scale(0.25)">
  <circle cx="100" cy="100" r="50" />
</g>
```

其中 $0.25 = 50/200$ 是内层 viewBox 到内层视口的缩放因子。这一等价性是 SVG 坐标系代数性质的应用。

### 3.5 坐标系变换的行列式与定向

仿射变换矩阵的左上 $2 \times 2$ 子矩阵的行列式决定坐标系的定向(preservation of orientation):

$$
\det \begin{bmatrix} a & c \\ b & d \end{bmatrix} = ad - bc
$$

- $\det > 0$:定向保持(无翻转)
- $\det < 0$:定向反转(如 scale(-1, 1) 水平翻转)
- $\det = 0$:退化变换(投影到直线)

SVG 的 meet/slice 模式保证 $\det > 0$,即不改变定向。但通过 transform 可实现定向反转,这是镜像效果的基础。

### 3.6 抗锯齿与小数坐标的频率分析

像素是离散的,而 SVG 坐标是连续的。当坐标落在像素边界(如 $x = 10.5$)时,浏览器需通过抗锯齿算法在多个像素间分配颜色。可形式化为低通滤波:

$$
I_{\text{display}}(p) = \int_{\text{pixel}(p)} I_{\text{ideal}}(x) \, dx
$$

其中 $I_{\text{ideal}}$ 为理想连续图像,$I_{\text{display}}$ 为离散像素值。当描边恰好落在像素边界时,积分覆盖两个像素,导致 1px 描边显示为 2px 灰色描边。这就是著名的"0.5 偏移技巧"的数学原理。

## 4. 代码示例

### 4.1 视口(viewport)与视图框(viewBox)

`<svg>` 的 `width` 和 `height` 定义视口尺寸,`viewBox` 定义内部坐标系。

```html
<!-- 视口 400×300,内部坐标 200×150,等比放大 2 倍 -->
<svg width="400" height="300" viewBox="0 0 200 150" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="100" height="75" fill="#4f5bd5" />
</svg>
```

#### 4.1.1 viewBox 语法

```
viewBox = "<min-x> <min-y> <width> <height>"
```

| 参数 | 含义 | 取值 |
| ---- | ---- | ---- |
| `min-x` | 视图框左上角 X 坐标 | 任意实数(含负数) |
| `min-y` | 视图框左上角 Y 坐标 | 任意实数(含负数) |
| `width` | 视图框宽度 | 正实数 |
| `height` | 视图框高度 | 正实数 |

#### 4.1.2 viewBox 的核心价值

| 价值 | 说明 |
| ---- | ---- |
| **响应式适配** | 视口变化时图形按比例缩放,无需重写坐标 |
| **坐标归一化** | 可用 0-100 或 0-1 等任意范围描述图形 |
| **局部裁剪** | 通过调整 min-x/min-y 可显示图形局部 |
| **独立于尺寸** | 同一 SVG 可用作 16px 图标或 1920px 横幅 |

### 4.2 坐标系方向

SVG 坐标系原点在**左上角**,X 轴向右、Y 轴**向下**(与数学坐标系 Y 轴相反)。

```mermaid
flowchart LR
    Origin[(0,0)] --> X[X+]
    Origin --> Y[Y+]
```

```html
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- 圆心 (50,50):在画布正中央 -->
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  <!-- (0,0) 在左上角 -->
  <rect x="0" y="0" width="20" height="20" fill="#d63031" />
</svg>
```

注意 Y 轴向下意味着:在描述物理场景时(如重力下落),自然映射是"y 增大";在描述数学函数(如正弦曲线)时,需翻转 Y 轴或调整坐标系。

### 4.3 preserveAspectRatio 详解

当 viewBox 与视口宽高比不一致时,`preserveAspectRatio` 控制如何适配。

#### 4.3.1 语法

```
preserveAspectRatio = "<align> <meetOrSlice>"
```

#### 4.3.2 对齐方式 align

| 值 | 含义 | 应用场景 |
| ---- | ---- | ---- |
| `xMinYMin` | 左上对齐 | 图标贴左上角 |
| `xMidYMin` | 上中对齐 | 顶部居中 banner |
| `xMaxYMin` | 右上对齐 | 右上角徽章 |
| `xMinYMid` | 左中对齐 | 侧边栏图标 |
| `xMidYMid` | 居中对齐(默认) | 通用图标 |
| `xMaxYMid` | 右中对齐 | 右侧操作按钮 |
| `xMinYMax` | 左下对齐 | 左下角水印 |
| `xMidYMax` | 下中对齐 | 底部居中提示 |
| `xMaxYMax` | 右下对齐 | 右下角关闭按钮 |

#### 4.3.3 适配模式 meetOrSlice

| 值 | 行为 | 数学含义 |
| ---- | ---- | ---- |
| `meet` | 完整显示 viewBox,留白(默认) | $s = \min(W/w, H/h)$ |
| `slice` | 填满视口,可能裁剪 | $s = \max(W/w, H/h)$ |
| `none` | 拉伸变形,不保持比例 | $s_x = W/w, s_y = H/h$ |

#### 4.3.4 示例对比

```html
<!-- viewBox 4:3,视口 1:1,meet 模式留白 -->
<svg width="100" height="100" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid meet">
  <rect width="400" height="300" fill="#4f5bd5" />
</svg>

<!-- slice 模式填满视口,裁剪左右 -->
<svg width="100" height="100" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice">
  <rect width="400" height="300" fill="#00b894" />
</svg>

<!-- none 模式拉伸变形 -->
<svg width="100" height="100" viewBox="0 0 400 300" preserveAspectRatio="none">
  <rect width="400" height="300" fill="#d63031" />
</svg>
```

### 4.4 响应式图标实战

#### 4.4.1 单 viewBox 适配多尺寸

图标 SVG 通常只声明 viewBox,不指定 width/height,由外层 CSS 控制。

```html
<!-- icon.svg:只声明 viewBox,声明可继承的 currentColor -->
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2 L22 22 L2 22 Z" fill="currentColor" />
</svg>
```

```css
/* 通过 CSS 控制不同尺寸 */
.icon-sm { width: 16px; height: 16px; }
.icon-md { width: 24px; height: 24px; }
.icon-lg { width: 48px; height: 48px; }
.icon-xl { width: 96px; height: 96px; }
```

```html
<svg class="icon-sm" viewBox="0 0 24 24">...</svg>
<svg class="icon-lg" viewBox="0 0 24 24">...</svg>
```

#### 4.4.2 通过 CSS 自适应父容器

```css
.responsive-svg {
  width: 100%;
  height: auto;
  display: block;
}
```

```html
<div style="max-width: 600px;">
  <svg class="responsive-svg" viewBox="0 0 16 9" xmlns="http://www.w3.org/2000/svg">
    <rect width="16" height="9" fill="#4f5bd5" />
  </svg>
</div>
```

SVG 自动按 16:9 比例缩放至父容器宽度,无需 JavaScript。

### 4.5 负坐标与偏移

viewBox 的 min-x/min-y 可为负数,便于以原点为中心描述图形。

```html
<svg viewBox="-50 -50 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <!-- 坐标系 -50 到 50,原点 (0,0) 居中 -->
  <circle cx="0" cy="0" r="40" fill="#4f5bd5" />
  <line x1="-50" y1="0" x2="50" y2="0" stroke="#333" />
  <line x1="0" y1="-50" x2="0" y2="50" stroke="#333" />
</svg>
```

负坐标系的优势:以原点为中心描述几何图形,简化数学计算(如极坐标转换、旋转变换)。

### 4.6 局部放大

通过缩小 viewBox 范围实现局部放大。

```html
<!-- 完整图:显示 400×300 -->
<svg viewBox="0 0 400 300" width="400" height="300">
  <rect width="400" height="300" fill="#4f5bd5" />
  <circle cx="200" cy="150" r="50" fill="#fff" />
</svg>

<!-- 放大显示原图中央 100×75 区域 -->
<svg viewBox="100 75 100 75" width="400" height="300">
  <rect width="400" height="300" fill="#4f5bd5" />
  <circle cx="200" cy="150" r="50" fill="#fff" />
</svg>
```

应用场景:地图缩放、图表聚焦、图片裁切预览。同一份 SVG 数据,通过 viewBox 切换即可显示不同视图。

### 4.7 嵌套 svg 建立子坐标系

```html
<svg viewBox="0 0 400 200" width="400" height="200" xmlns="http://www.w3.org/2000/svg">
  <svg x="0" y="0" width="200" height="200" viewBox="0 0 100 100">
    <!-- 左侧子坐标系 100×100 映射到 200×200 -->
    <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  </svg>
  <svg x="200" y="0" width="200" height="200" viewBox="0 0 50 50">
    <!-- 右侧子坐标系 50×50 映射到 200×200,放大 4 倍 -->
    <circle cx="25" cy="25" r="20" fill="#00b894" />
  </svg>
</svg>
```

嵌套 `<svg>` 的语义:在外层视口中开辟一块矩形区域,内部建立独立坐标系。常用于仪表盘、地图瓦片等"图中图"场景。

### 4.8 坐标系与变换

`transform` 属性在坐标系层面应用变换,影响后续所有子元素。

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(100, 100) rotate(45)">
    <!-- 此组以 (100,100) 为原点,旋转 45° -->
    <rect x="-25" y="-25" width="50" height="50" fill="#d63031" />
  </g>
</svg>
```

变换的顺序**不可交换**:`translate(100,0) rotate(45)` 与 `rotate(45) translate(100,0)` 结果不同。变换的复合遵循矩阵乘法的非交换性。

### 4.9 viewBox 动态切换

通过 JavaScript 动态修改 viewBox 实现平移与缩放:

```javascript
class SVGViewportController {
  constructor(svgElement) {
    this.svg = svgElement;
    this.viewBox = { x: 0, y: 0, width: 400, height: 300 };
    this.update();
  }

  // 平移 viewBox
  pan(dx, dy) {
    this.viewBox.x += dx;
    this.viewBox.y += dy;
    this.update();
  }

  // 以指定点为中心缩放
  zoomAt(centerX, centerY, factor) {
    const { x, y, width, height } = this.viewBox;
    // 保持中心点不动,缩放 width/height
    const newWidth = width / factor;
    const newHeight = height / factor;
    this.viewBox.x = centerX - (centerX - x) / factor;
    this.viewBox.y = centerY - (centerY - y) / factor;
    this.viewBox.width = newWidth;
    this.viewBox.height = newHeight;
    this.update();
  }

  // 更新 SVG viewBox 属性
  update() {
    const { x, y, width, height } = this.viewBox;
    this.svg.setAttribute(
      'viewBox',
      `${x.toFixed(2)} ${y.toFixed(2)} ${width.toFixed(2)} ${height.toFixed(2)}`
    );
  }

  // 重置到初始视图
  reset() {
    this.viewBox = { x: 0, y: 0, width: 400, height: 300 };
    this.update();
  }
}

// 使用示例
const svg = document.querySelector('svg');
const controller = new SVGViewportController(svg);

// 鼠标滚轮缩放
svg.addEventListener('wheel', (e) => {
  e.preventDefault();
  const factor = e.deltaY > 0 ? 0.9 : 1.1;
  const rect = svg.getBoundingClientRect();
  const cx = e.offsetX;
  const cy = e.offsetY;
  controller.zoomAt(cx, cy, factor);
});

// 拖拽平移
let isDragging = false;
let startX, startY;
svg.addEventListener('mousedown', (e) => {
  isDragging = true;
  startX = e.offsetX;
  startY = e.offsetY;
});
svg.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  const dx = (e.offsetX - startX) * -1;
  const dy = (e.offsetY - startY) * -1;
  controller.pan(dx, dy);
  startX = e.offsetX;
  startY = e.offsetY;
});
svg.addEventListener('mouseup', () => {
  isDragging = false;
});
```

这是地图应用、图片查看器、可缩放图表的核心实现模式。

## 5. 对比分析

### 5.1 SVG vs Canvas 坐标系

| 特性 | SVG | Canvas |
| ---- | --- | ----- |
| 坐标系类型 | 保留模式(retained mode) | 立即模式(immediate mode) |
| 原点位置 | 可通过 viewBox 任意指定 | 固定左上角 |
| Y 轴方向 | 向下 | 向下 |
| 单位 | user units(可任意缩放) | 像素(固定) |
| 响应式 | viewBox 自动适配 | 需手动重绘 |
| 抗锯齿 | 浏览器自动处理 | 需手动控制 |
| 变换累积 | transform 属性链式 | ctx.translate/rotate 累积 |
| 坐标系嵌套 | 嵌套 `<svg>` | ctx.save/restore |

### 5.2 SVG vs WebGL 坐标系

| 特性 | SVG | WebGL |
| ---- | --- | ----- |
| Y 轴方向 | 向下 | 向上 |
| 原点 | 左上角 | 左下角(NDC) |
| 坐标范围 | 任意(由 viewBox 决定) | [-1, 1] NDC |
| 投影 | 仿射变换 | 透视/正交投影矩阵 |
| 单位 | user units | 像素(屏幕空间) |
| 旋转方向 | 顺时针(正角度) | 逆时针(正角度,数学约定) |

### 5.3 viewBox vs CSS transform: scale()

| 特性 | viewBox 缩放 | CSS scale() |
| ---- | ----------- | ----------- |
| 缩放中心 | viewBox 中心 | transform-origin |
| 影响描边宽度 | 是(描边随缩放) | 否(描边保持) |
| 影响字体大小 | 是(字号随缩放) | 否(字号保持) |
| 响应式适配 | 自动(meet/slice) | 需手动 |
| 性能 | 高(硬件加速) | 高 |
| 应用场景 | 图形整体缩放 | UI 元素微调 |

注意 viewBox 缩放会同步缩放描边与字号,这是与 CSS transform: scale() 的核心差异。需要保持描边宽度不变时,使用 `vector-effect="non-scaling-stroke"`。

### 5.4 meet vs slice vs none 的工程选型

| 模式 | 适用场景 | 优势 | 劣势 |
| ---- | ---- | ---- | ---- |
| `meet` | 图标、logo、需要完整可见 | 不丢失内容 | 留白区域 |
| `slice` | 全屏背景、cover 模式 | 无留白 | 可能裁剪 |
| `none` | 已知精确尺寸场景 | 完全填满 | 形变 |

## 6. 常见陷阱与最佳实践

### 6.1 viewBox 与视口比例不一致导致留白

```html
<!-- 错误:viewBox 4:3,视口 16:9,默认 meet 会留白 -->
<svg width="640" height="360" viewBox="0 0 400 300">
  <rect width="400" height="300" fill="#4f5bd5" />
</svg>
```

**解决方案**:

1. 调整 viewBox 比例匹配视口(如 `viewBox="0 0 640 360"`)
2. 使用 `slice` 填满视口(可能裁剪)
3. 接受留白(某些场景需要完整显示)

### 6.2 小数坐标导致抗锯齿模糊

```html
<!-- 模糊:1px 描边落在 .5 坐标,被分配到两个像素 -->
<line x1="0" y1="10.5" x2="100" y2="10.5" stroke="#000" />

<!-- 清晰:整数坐标 + 0.5 偏移技巧 -->
<line x1="0.5" y1="10" x2="100.5" y2="10" stroke="#000" stroke-width="1" />
```

**原理**:1px 描边的中心在 $y = 10.5$ 时,覆盖像素 10 和像素 11 各 50%,显示为 2px 灰色描边。将描边中心对齐到 $y = 10.5$ 的像素边界(即 $x = 0.5$)可使 1px 描边恰好覆盖像素 10。

### 6.3 忘记设置 viewBox 导致图标无法缩放

```html
<!-- 错误:仅有 width/height,CSS 缩放后比例可能变形 -->
<svg width="24" height="24">
  <circle cx="12" cy="12" r="10" />
</svg>

<!-- 正确:声明 viewBox,由 CSS 控制尺寸 -->
<svg viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" />
</svg>
```

**最佳实践**:图标 SVG 始终声明 viewBox,省略 width/height,通过 CSS 控制最终显示尺寸。

### 6.4 描边宽度随缩放变化

```html
<!-- 问题:viewBox 缩放后描边被放大 -->
<svg viewBox="0 0 24 24" style="width: 240px;">
  <circle cx="12" cy="12" r="10" stroke="#000" stroke-width="1" />
  <!-- 显示为 10px 粗描边 -->
</svg>

<!-- 解决:vector-effect 保持描边宽度 -->
<svg viewBox="0 0 24 24" style="width: 240px;">
  <circle
    cx="12" cy="12" r="10"
    stroke="#000" stroke-width="1"
    vector-effect="non-scaling-stroke"
  />
  <!-- 描边保持 1px -->
</svg>
```

### 6.5 Y 轴方向与数学约定相反

```html
<!-- 错误:误用数学坐标系绘制正弦曲线 -->
<svg viewBox="0 0 200 100">
  <!-- 期望:y = sin(x),但 SVG 中 y 向下,实际显示为 -sin(x) -->
  <path d="M 0 50 Q 50 0 100 50 T 200 50" stroke="#000" fill="none" />
</svg>

<!-- 正确:翻转 Y 轴 -->
<svg viewBox="0 0 200 100" transform="scale(1, -1) translate(0, -100)">
  <path d="M 0 50 Q 50 0 100 50 T 200 50" stroke="#000" fill="none" />
</svg>
```

### 6.6 嵌套 svg 与 g 混淆

```html
<!-- 混淆:用嵌套 svg 实现简单变换 -->
<svg viewBox="0 0 100 100">
  <svg x="50" y="50" width="20" height="20" viewBox="0 0 10 10">
    <rect x="0" y="0" width="10" height="10" />
  </svg>
</svg>

<!-- 推荐:简单变换用 g + transform -->
<svg viewBox="0 0 100 100">
  <g transform="translate(50, 50) scale(2)">
    <rect x="0" y="0" width="10" height="10" />
  </g>
</svg>
```

**选择建议**:简单平移/缩放用 `<g transform>`,需要独立 viewBox 或独立 preserveAspectRatio 时才用嵌套 `<svg>`。

### 6.7 preserveAspectRatio 默认值误解

```html
<!-- 误解:以为默认是 none(拉伸填满) -->
<svg width="100" height="50" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" />
</svg>
<!-- 实际默认 xMidYMid meet:留白居中 -->

<!-- 强制拉伸 -->
<svg width="100" height="50" viewBox="0 0 24 24" preserveAspectRatio="none">
  <circle cx="12" cy="12" r="10" />
</svg>
<!-- 圆形被拉伸为椭圆 -->
```

## 7. 工程实践

### 7.1 响应式 SVG 设计模式

#### 7.1.1 固定宽高比容器

```css
.aspect-ratio-box {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 */
}
.aspect-ratio-box > svg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

```html
<div class="aspect-ratio-box">
  <svg viewBox="0 0 16 9" preserveAspectRatio="xMidYMid meet">...</svg>
</div>
```

#### 7.1.2 自适应图标系统

```html
<!-- Vue 3 组件:可缩放图标 -->
<template>
  <svg
    :viewBox="viewBox"
    :width="size"
    :height="size"
    :fill="color"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path :d="path" />
  </svg>
</template>

<script setup>
defineProps({
  path: { type: String, required: true },
  size: { type: [Number, String], default: 24 },
  color: { type: String, default: 'currentColor' },
  viewBox: { type: String, default: '0 0 24 24' },
});
</script>
```

#### 7.1.3 React 组件封装

```jsx
import { memo } from 'react';

const Icon = memo(function Icon({ path, size = 24, color = 'currentColor', viewBox = '0 0 24 24', title }) {
  return (
    <svg
      viewBox={viewBox}
      width={size}
      height={size}
      fill={color}
      role={title ? 'img' : 'presentation'}
      aria-hidden={title ? undefined : true}
      aria-label={title}
      xmlns="http://www.w3.org/2000/svg"
    >
      {title && <title>{title}</title>}
      <path d={path} />
    </svg>
  );
});

export default Icon;
```

### 7.2 SVG 查看器:平移与缩放

```javascript
class SVGViewer {
  constructor(container, svg) {
    this.container = container;
    this.svg = svg;
    this.originalViewBox = svg.getAttribute('viewBox').split(' ').map(Number);
    this.viewBox = [...this.originalViewBox];
    this.scale = 1;
    this.bindEvents();
  }

  bindEvents() {
    this.container.addEventListener('wheel', this.onWheel.bind(this), { passive: false });
    this.container.addEventListener('mousedown', this.onMouseDown.bind(this));
    window.addEventListener('mousemove', this.onMouseMove.bind(this));
    window.addEventListener('mouseup', this.onMouseUp.bind(this));
    this.container.addEventListener('dblclick', this.reset.bind(this));
  }

  onWheel(e) {
    e.preventDefault();
    const rect = this.svg.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;

    // 屏幕坐标转 SVG 坐标
    const [vx, vy, vw, vh] = this.viewBox;
    const sx = mx / rect.width;
    const sy = my / rect.height;
    const svgX = vx + sx * vw;
    const svgY = vy + sy * vh;

    // 缩放
    const factor = e.deltaY > 0 ? 1.1 : 0.9;
    const newVw = vw * factor;
    const newVh = vh * factor;

    // 保持鼠标位置不动
    this.viewBox = [
      svgX - sx * newVw,
      svgY - sy * newVh,
      newVw,
      newVh,
    ];
    this.updateViewBox();
  }

  onMouseDown(e) {
    this.isDragging = true;
    this.startX = e.clientX;
    this.startY = e.clientY;
    this.startViewBox = [...this.viewBox];
  }

  onMouseMove(e) {
    if (!this.isDragging) return;
    const rect = this.svg.getBoundingClientRect();
    const dx = ((e.clientX - this.startX) / rect.width) * this.startViewBox[2];
    const dy = ((e.clientY - this.startY) / rect.height) * this.startViewBox[3];
    this.viewBox = [
      this.startViewBox[0] - dx,
      this.startViewBox[1] - dy,
      this.startViewBox[2],
      this.startViewBox[3],
    ];
    this.updateViewBox();
  }

  onMouseUp() {
    this.isDragging = false;
  }

  updateViewBox() {
    this.svg.setAttribute(
      'viewBox',
      this.viewBox.map((v) => v.toFixed(2)).join(' ')
    );
  }

  reset() {
    this.viewBox = [...this.originalViewBox];
    this.updateViewBox();
  }
}
```

### 7.3 Vite 集成:SVG as Vue Component

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { createSvgPlugin } from 'vite-plugin-svg';

export default defineConfig({
  plugins: [
    vue(),
    createSvgPlugin({
      defaultImport: 'component',
      svgoConfig: {
        plugins: [
          { name: 'removeViewBox', active: false },
          { name: 'removeDimensions', active: true },
        ],
      },
    }),
  ],
});
```

```vue
<!-- 使用 -->
<template>
  <IconHeart size="48" color="#d63031" />
</template>

<script setup>
import IconHeart from './assets/icons/heart.svg?component';
</script>
```

### 7.4 SVG 自动校验脚本

```javascript
// scripts/validate-svg-coords.mjs
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const SVG_DIR = 'src/assets/icons';
const issues = [];

const files = readdirSync(SVG_DIR).filter((f) => f.endsWith('.svg'));
for (const file of files) {
  const content = readFileSync(join(SVG_DIR, file), 'utf8');
  const issues_in_file = [];

  // 检查 1:必须声明 viewBox
  if (!/viewBox=/.test(content)) {
    issues_in_file.push('missing viewBox');
  }

  // 检查 2:不应同时声明 width 和 height(由 CSS 控制)
  if (/<svg[^>]*\swidth=/.test(content) && /<svg[^>]*\sheight=/.test(content)) {
    issues_in_file.push('explicit width/height (use CSS instead)');
  }

  // 检查 3:viewBox 应使用整数坐标(避免抗锯齿)
  const viewBoxMatch = content.match(/viewBox="([^"]+)"/);
  if (viewBoxMatch) {
    const [, , w, h] = viewBoxMatch[1].split(/\s+/).map(Number);
    if (!Number.isInteger(w) || !Number.isInteger(h)) {
      issues_in_file.push('non-integer viewBox dimensions');
    }
  }

  // 检查 4:不应用 xlink:href(已废弃)
  if (/xlink:href=/.test(content)) {
    issues_in_file.push('deprecated xlink:href (use href)');
  }

  // 检查 5:推荐使用 currentColor 便于主题化
  if (!/currentColor/.test(content) && /fill="#/.test(content)) {
    issues_in_file.push('hardcoded fill color (consider currentColor)');
  }

  if (issues_in_file.length > 0) {
    issues.push({ file, issues: issues_in_file });
  }
}

if (issues.length > 0) {
  console.error('SVG validation failed:');
  for (const { file, issues: i } of issues) {
    console.error(`  ${file}:`);
    for (const issue of i) {
      console.error(`    - ${issue}`);
    }
  }
  process.exit(1);
} else {
  console.log(`All ${files.length} SVG files passed validation.`);
}
```

## 8. 案例研究

### 8.1 案例一:Material Design 图标体系

Google Material Icons 采用统一的 24×24 viewBox 设计,所有图标在 `0 0 24 24` 坐标系内绘制:

```xml
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
</svg>
```

**设计要点**:

1. 统一 viewBox,简化图标库管理
2. 不声明 width/height,由使用方决定尺寸
3. 使用 currentColor,通过 CSS color 控制颜色
4. 路径使用整数坐标,确保清晰渲染

### 8.2 案例二:GitHub Octicon 体系

GitHub 的 Octicon 在 16×16 viewBox 内设计,适配密集 UI:

```xml
<svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
</svg>
```

**设计要点**:

1. 16×16 viewBox 适配高密度像素网格
2. 坐标尽量使用整数,减少抗锯齿模糊
3. `fill-rule="evenodd"` 处理复杂路径

### 8.3 案例三:Bootstrap Icons 体系

Bootstrap Icons 提供 16×16 与 24×24 双 viewBox 版本,适配不同 UI 场景:

```xml
<!-- 16×16 版本 -->
<svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zM1.5 8a6.5 6.5 0 1 1 13 0 6.5 6.5 0 0 1-13 0z"/>
</svg>

<!-- 24×24 版本 -->
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zm0 22.5a10.5 10.5 0 1 1 0-21 10.5 10.5 0 0 1 0 21z"/>
</svg>
```

### 8.4 案例四:FANDEX 项目图标体系

FANDEX 项目采用混合策略:

```html
<!-- 路由图标:16×16 紧凑布局 -->
<svg viewBox="0 0 16 16">
  <path d="..." fill="currentColor" />
</svg>

<!-- 卡片图标:24×24 标准尺寸 -->
<svg viewBox="0 0 24 24">
  <path d="..." fill="currentColor" />
</svg>

<!-- Hero 横幅:大尺寸场景 -->
<svg viewBox="0 0 1200 400" preserveAspectRatio="xMidYMid slice">
  <!-- 详细背景图 -->
</svg>
```

### 8.5 案例五:D3.js 数据可视化

D3.js 利用 viewBox 实现响应式图表:

```javascript
import * as d3 from 'd3';

const margin = { top: 20, right: 30, bottom: 30, left: 40 };
const width = 800 - margin.left - margin.right;
const height = 400 - margin.top - margin.bottom;

const svg = d3.select('#chart')
  .append('svg')
  .attr('viewBox', `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
  .classed('responsive-svg', true);

const g = svg.append('g')
  .attr('transform', `translate(${margin.left}, ${margin.top})`);

// 通过 CSS 实现响应式
```

```css
.responsive-svg {
  width: 100%;
  height: auto;
}
```

### 填空题知识点讲解

**题目 6**:SVG 中 1px 描边落在整数坐标(如 $y = 10$)时显示模糊,解决方法是将坐标偏移 ________。

**解析讲解**：`0.5`(或 `0.5px`)

**解析讲解**：1px 描边的中心在像素边界时,会被分配到两个像素各 50%,显示为 2px 灰色描边。将坐标偏移 0.5(如 $y = 10.5$)使描边中心对齐像素中心,显示为清晰的 1px。

**题目 7**:`preserveAspectRatio` 的两个参数分别是 ________ 和 ________。

**解析讲解**：`align`(对齐方式);`meetOrSlice`(适配模式)

**解析讲解**：`preserveAspectRatio="<align> <meetOrSlice>"`,如 `xMidYMid meet`、`xMinYMin slice`、`none`(单独使用,忽略对齐参数)。

**题目 8**:设视口为 400×300,viewBox 为 `0 0 200 150`,meet 模式下的缩放因子 $s$ = ________。

**解析讲解**：`2`

**解析讲解**：$s_x = W/w = 400/200 = 2$,$s_y = H/h = 300/150 = 2$。由于 $s_x = s_y = 2$,meet 与 slice 行为一致,均为缩放 2 倍。

**题目 9**:viewBox 的四个参数依次是 ________、________、________、________。

**解析讲解**：`min-x`(X 起点);`min-y`(Y 起点);`width`(宽度);`height`(高度)

**解析讲解**：`viewBox="<min-x> <min-y> <width> <height>"`,前两个参数定义视图框左上角坐标,后两个定义宽高。min-x/min-y 可为负数。

**题目 10**:嵌套 `<svg>` 的坐标系复合满足 ________ 律(矩阵乘法的代数性质),但不满足 ________ 律。

**解析讲解**：`结合`;`交换`

**解析讲解**：仿射变换集合在矩阵乘法下构成幺半群,满足结合律 $(M_1 M_2) M_3 = M_1 (M_2 M_3)$,但一般不满足交换律 $M_1 M_2 \neq M_2 M_1$。

### 编程题知识点讲解

**题目 11**:实现一个 SVG 时钟,viewBox 为 `0 0 100 100`,要求:

1. 表盘圆形居中(cx=50, cy=50, r=45)
2. 12 个时刻刻度(每 30°一个)
3. 时针、分针、秒针用不同颜色与长度
4. 中心点带小圆

```html
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- 表盘 -->
  <circle cx="50" cy="50" r="45" fill="#fff" stroke="#333" stroke-width="2" />

  <!-- 12 个时刻刻度 -->
  <g stroke="#333" stroke-width="2">
    <!-- 利用 transform rotate 围绕中心旋转 -->
    <line x1="50" y1="8" x2="50" y2="14" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(30 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(60 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(90 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(120 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(150 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(180 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(210 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(240 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(270 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(300 50 50)" />
    <line x1="50" y1="8" x2="50" y2="14" transform="rotate(330 50 50)" />
  </g>

  <!-- 时针(指向 12 点,长度 25) -->
  <line
    x1="50" y1="50" x2="50" y2="25"
    stroke="#333" stroke-width="3"
    stroke-linecap="round"
    transform="rotate(0 50 50)"
  />

  <!-- 分针(指向 3 点,长度 35) -->
  <line
    x1="50" y1="50" x2="80" y2="50"
    stroke="#666" stroke-width="2"
    stroke-linecap="round"
    transform="rotate(0 50 50)"
  />

  <!-- 秒针(指向 6 点,长度 40) -->
  <line
    x1="50" y1="50" x2="50" y2="85"
    stroke="#d63031" stroke-width="1"
    stroke-linecap="round"
    transform="rotate(0 50 50)"
  />

  <!-- 中心点 -->
  <circle cx="50" cy="50" r="3" fill="#333" />
</svg>
```

**评分标准**:

- 表盘正确(2 分)
- 12 刻度正确分布(4 分)
- 三针颜色与长度区分(2 分)
- 中心点装饰(2 分)

**题目 12**:实现一个响应式 SVG banner,要求:

1. viewBox 为 `0 0 1200 300`(宽高比 4:1)
2. 背景为线性渐变
3. 居中显示文字 "FANDEX"
4. 在不同视口尺寸下保持宽高比
5. 视口小于 viewBox 时,采用 slice 模式裁剪两侧

```html
<svg
  viewBox="0 0 1200 300"
  preserveAspectRatio="xMidYMid slice"
  xmlns="http://www.w3.org/2000/svg"
  role="img"
  aria-labelledby="banner-title"
>
  <title id="banner-title">FANDEX Banner</title>

  <defs>
    <linearGradient id="banner-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="100%" stop-color="#f9a825" />
    </linearGradient>
  </defs>

  <!-- 背景 -->
  <rect width="1200" height="300" fill="url(#banner-grad)" />

  <!-- 装饰圆形 -->
  <circle cx="200" cy="150" r="80" fill="#fff" fill-opacity="0.1" />
  <circle cx="1000" cy="150" r="80" fill="#fff" fill-opacity="0.1" />

  <!-- 主文字 -->
  <text
    x="600"
    y="180"
    text-anchor="middle"
    font-family="system-ui, sans-serif"
    font-size="96"
    font-weight="bold"
    fill="#fff"
    letter-spacing="8"
  >
    FANDEX
  </text>
</svg>
```

```css
.banner {
  width: 100%;
  height: 200px;
  display: block;
}

@media (max-width: 768px) {
  .banner {
    height: 120px;
  }
}
```

**评分标准**:

- viewBox 与 preserveAspectRatio 配置正确(3 分)
- 渐变背景正确(2 分)
- 文字居中对齐(text-anchor)(2 分)
- 响应式 CSS 适配(3 分)

### 10.1 W3C 规范

1. W3C. 2018. **SVG 2 Specification**. W3C Recommendation. https://doi.org/10.17487/RFC8141. Available at: https://www.w3.org/TR/SVG2/

2. W3C. 2003. **Scalable Vector Graphics (SVG) 1.1 Specification**. W3C Recommendation. https://www.w3.org/TR/SVG11/

3. W3C. 2001. **Scalable Vector Graphics (SVG) 1.0 Specification**. W3C Recommendation. https://www.w3.org/TR/SVG/

4. W3C. 2023. **CSS Transforms Module Level 1**. W3C Working Draft. https://www.w3.org/TR/css-transforms-1/

5. WHATWG. 2023. **HTML Living Standard**. https://html.spec.whatwg.org/

### 10.2 学术论文

6. Sutherland, I. E. 1963. **Sketchpad: A Man-Machine Graphical Communication System**. In *Proceedings of the Spring Joint Computer Conference* (AFIPS '63). Association for Computing Machinery, New York, NY, USA, 329–346. https://doi.org/10.1145/1461551.1461591

7. Foley, J. D., van Dam, A., Feiner, S. K., and Hughes, J. F. 2013. **Computer Graphics: Principles and Practice** (3rd ed.). Addison-Wesley Professional, Boston, MA, USA.

8. Shreiner, D., Sellers, G., Kessenich, J. M., and Licea-Kane, B. 2013. **OpenGL Programming Guide: The Official Guide to Learning OpenGL, Version 4.3** (8th ed.). Addison-Wesley Professional.

9. Munzner, T. 2014. **Visualization Analysis and Design**. CRC Press, Boca Raton, FL, USA. https://doi.org/10.1201/b17511

### 10.3 工程实践参考

10. Pilgroom, S. 2023. **Practical SVG**. A Book Apart, New York, NY, USA.

11. Eisenberg, J. D. 2014. **SVG Essentials** (2nd ed.). O'Reilly Media, Sebastopol, CA, USA.

12. Bellamy-Royds, A., Eisenberg, J. D., and Ginger, D. 2017. **Using SVG with CSS3 and HTML5: Vector Graphics for Web Design**. O'Reilly Media, Sebastopol, CA, USA.

13. Bostock, M., Ogievetsky, V., and Heer, J. 2011. **D3: Data-Driven Documents**. *IEEE Transactions on Visualization and Computer Graphics* 17, 12, 2301–2309. https://doi.org/10.1109/TVCG.2011.185

### 11.1 计算机图形学基础

- **MIT 6.837 Computer Graphics**:深入理解图形管线、变换矩阵、光栅化算法
- **Stanford CS248 Introduction to Computer Graphics**:坐标系、投影、变换的数学基础
- **CMU 15-462/662 Computer Graphics**:从理论到实现的完整覆盖

### 11.2 用户界面设计

- **MIT 6.831 User Interface Design and Implementation**:响应式设计、可访问性、交互模式
- **Don Norman《设计心理学》**:坐标系选择对用户认知的影响
- **Apple Human Interface Guidelines**:图标设计的视觉一致性原则

### 11.3 Web 标准演进

- **W3C SVG Working Group**:跟踪 SVG 2.1、SVG Native 等新规范
- **CSS Working Group**:CSS 与 SVG 的融合趋势(transform-box、clip-path)
- **WHATWG HTML Living Standard**:内联 SVG 的解析规则

### 11.4 相关工具

- **SVGO**:SVG 优化工具,理解坐标精度对文件大小的影响
- **Figma**:设计工具如何导出 viewBox 与坐标
- **Inkscape**:开源 SVG 编辑器,深入理解坐标系操作

### 11.5 进阶主题

- **SVG Native**:Adobe 提出的 SVG 子集,用于字体与印刷
- **WebGPU + SVG**:GPU 加速的 SVG 渲染管线
- **Variable SVG**:类似 Variable Font 的可变 SVG 概念
- **SVG Filters**:feGaussianBlur、feColorMatrix 等基于坐标系的滤镜

下一篇介绍 rect、circle、ellipse、line、polyline、polygon 六大基本图形,在已建立的坐标系基础上深入图形元素的属性与绘制原理。
## 视口 viewport

**视口定义**
`<svg width="<宽>" height="<高>"> ... </svg>`
```html
<svg width="400" height="300">
  <!-- 视口为 400×300 像素 -->
</svg>
```

---

## viewBox 视图框

**viewBox 内部坐标系**
`viewBox="<min-x> <min-y> <width> <height>"`
```html
<svg width="400" height="300" viewBox="0 0 200 150">
  <!-- 内部坐标 200×150,缩放到视口 400×300,等比放大 2 倍 -->
  <rect x="0" y="0" width="100" height="75" fill="#4f5bd5" />
</svg>
```

### viewBox 核心价值

| 价值           | 说明                                    |
| -------------- | --------------------------------------- |
| **响应式适配** | 视口变化时图形按比例缩放,无需重写坐标  |
| **坐标归一化** | 可用 0-100 或 0-1 等任意范围描述图形    |
| **局部裁剪**   | 通过调整 min-x/min-y 可显示图形局部     |
| **独立于尺寸** | 同一 SVG 可用作 16px 图标或 1920px 横幅 |

---

## 坐标系方向

**SVG 坐标系原点左上角,X 向右 Y 向下**
```mermaid
flowchart LR
    O[(0,0)] --> X[X+]
    O --> Y[Y+]
```
```html
<svg viewBox="0 0 100 100">
  <!-- 圆心 (50,50):在画布正中央 -->
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  <!-- (0,0) 在左上角 -->
  <rect x="0" y="0" width="20" height="20" fill="#d63031" />
</svg>
```

---

## preserveAspectRatio 宽高比策略

**preserveAspectRatio 语法**
`preserveAspectRatio="<align> <meetOrSlice>"`

### 对齐方式 align

| 值         | 含义             |
| ---------- | ---------------- |
| `xMinYMin` | 左上对齐         |
| `xMidYMid` | 居中对齐(默认) |
| `xMaxYMax` | 右下对齐         |
| `xMinYMid` | 左中对齐         |
| `xMidYMin` | 上中对齐         |

### 适配模式 meetOrSlice

| 值      | 行为                           |
| ------- | ------------------------------ |
| `meet`  | 完整显示 viewBox,留白(默认) |
| `slice` | 填满视口,可能裁剪           |
| `none`  | 拉伸变形,不保持比例         |

### 示例对比

**meet 完整显示**
`preserveAspectRatio="xMidYMid meet"`
```html
<!-- viewBox 4:3,视口 1:1 -->
<svg width="100" height="100" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid meet">
  <rect width="400" height="300" fill="#4f5bd5" />
</svg>
<!-- meet:矩形等比缩小居中,上下留白 -->
```

**slice 填满裁剪**
`preserveAspectRatio="xMidYMid slice"`
```html
<svg width="100" height="100" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice">
  <rect width="400" height="300" fill="#00b894" />
</svg>
<!-- slice:矩形等比放大填满,左右被裁 -->
```

**none 拉伸变形**
`preserveAspectRatio="none"`
```html
<svg width="100" height="100" viewBox="0 0 400 300" preserveAspectRatio="none">
  <rect width="400" height="300" fill="#d63031" />
</svg>
<!-- none:拉伸为正方形,变形 -->
```

---

## 响应式图标

**响应式图标 SVG**
`<svg viewBox="0 0 24 24" class="<类名>"> ... </svg>`
```html
<svg viewBox="0 0 24 24" class="icon">
  <path d="M12 2 L22 22 L2 22 Z" fill="currentColor" />
</svg>
```
```css
.icon {
  width: 24px;
  height: 24px;
}
.icon-lg {
  width: 48px;
  height: 48px;
}
```

---

## 负坐标与偏移

**负坐标 viewBox**
`viewBox="<-min-x> <-min-y> <width> <height>"`
```html
<svg viewBox="-50 -50 100 100" width="100" height="100">
  <!-- 坐标系 -50 到 50,原点 (0,0) 居中 -->
  <circle cx="0" cy="0" r="40" fill="#4f5bd5" />
  <line x1="-50" y1="0" x2="50" y2="0" stroke="#333" />
  <line x1="0" y1="-50" x2="0" y2="50" stroke="#333" />
</svg>
```

---

## 局部放大

**缩小 viewBox 实现局部放大**
```html
<svg viewBox="0 0 400 300" width="400" height="300">
  <!-- 完整图 -->
</svg>

<svg viewBox="100 75 100 75" width="400" height="300">
  <!-- 放大显示原图中央 100×75 区域 -->
</svg>
```

---

## 嵌套 svg 子坐标系

**嵌套 svg 建立子坐标系**
`<svg x="<x>" y="<y>" width="<宽>" height="<高>" viewBox="<min-x> <min-y> <w> <h>"> ... </svg>`
```html
<svg viewBox="0 0 400 200" width="400" height="200">
  <svg x="0" y="0" width="200" height="200" viewBox="0 0 100 100">
    <!-- 左侧子坐标系 100×100 映射到 200×200 -->
    <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  </svg>
  <svg x="200" y="0" width="200" height="200" viewBox="0 0 50 50">
    <!-- 右侧子坐标系 50×50 映射到 200×200,放大 4 倍 -->
    <circle cx="25" cy="25" r="20" fill="#00b894" />
  </svg>
</svg>
```

---

## 坐标系与 transform

**transform 在坐标系层面应用变换**
`<g transform="<变换函数>"> ... </g>`
```html
<svg viewBox="0 0 200 200">
  <g transform="translate(100, 100) rotate(45)">
    <!-- 此组以 (100,100) 为原点,旋转 45° -->
    <rect x="-25" y="-25" width="50" height="50" fill="#d63031" />
  </g>
</svg>
```

变换的顺序**不可交换**:`translate(100,0) rotate(45)` 与 `rotate(45) translate(100,0)` 结果不同。

---

## 常见陷阱语法

**viewBox 与视口比例不一致留白**
```html
<!-- viewBox 4:3 视口 16:9,默认 meet 会留白 -->
<svg width="640" height="360" viewBox="0 0 400 300">
  <rect width="400" height="300" fill="#4f5bd5" />
</svg>
```

**小数坐标导致抗锯齿模糊**
```html
<!-- 模糊:1px 描边落在 .5 坐标 -->
<line x1="0" y1="10.5" x2="100" y2="10.5" stroke="#000" />

<!-- 清晰:整数坐标 + 0.5 偏移技巧 -->
<line x1="0" y1="10" x2="100" y2="10" stroke="#000" />
```

**忘记设置 viewBox 导致图标无法缩放**
```html
<!-- 错误:仅有 width/height,CSS 缩放后变形 -->
<svg width="24" height="24">
  <circle cx="12" cy="12" r="10" />
</svg>

<!-- 正确:声明 viewBox,由 CSS 控制尺寸 -->
<svg viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" />
</svg>
```

---

## viewBox 调试

**调试用边框观察 viewBox**
`<svg viewBox="<min-x> <min-y> <w> <h>" width="<宽>" height="<高>" style="border:1px solid #ccc"> ... </svg>`
```html
<svg viewBox="0 0 100 100" width="200" height="200" style="border:1px solid #ccc">
  <rect x="10" y="10" width="80" height="80" fill="#4f5bd5" />
  <circle cx="50" cy="50" r="40" fill="none" stroke="#d63031" stroke-width="2" />
</svg>
```

<!-- ============ 文档分隔线：012-svg/004-SVGBasicShapeDetailed.md ============ -->

## 1. 矩形 rect

`<rect>` 绘制矩形，支持圆角。

```html
<svg viewBox="0 0 300 150">
  <rect x="10" y="10" width="80" height="60" fill="#4f5bd5" />
  <rect x="110" y="10" width="80" height="60" rx="12" ry="12" fill="#00b894" />
  <rect x="210" y="10" width="80" height="60" rx="30" ry="10" fill="#d63031" />
</svg>
```

### 1.1 属性

| 属性               | 说明              | 默认值 |
| ------------------ | ----------------- | ------ |
| `x` / `y`          | 左上角坐标        | 0      |
| `width` / `height` | 宽高（必需）      | -      |
| `rx` / `ry`        | 水平/垂直圆角半径 | 0      |
| `fill`             | 填充色            | black  |
| `stroke`           | 描边色            | none   |
| `stroke-width`     | 描边宽度          | 1      |

> 当只设置 `rx` 时，`ry` 默认等于 `rx`，形成等圆角。

### 1.2 圆角矩形技巧

```html
<!-- 仅上方圆角（用 path 实现） -->
<path d="M 10 30 Q 10 10 30 10 L 70 10 Q 90 10 90 30 L 90 70 L 10 70 Z" fill="#4f5bd5" />
```

`<rect>` 原生不支持单侧圆角，需用 `<path>` 配合贝塞尔曲线实现。

## 2. 圆形 circle

`<circle>` 由圆心与半径定义。

```html
<svg viewBox="0 0 200 100">
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  <circle cx="150" cy="50" r="40" fill="none" stroke="#d63031" stroke-width="3" />
</svg>
```

### 2.1 属性

| 属性              | 说明         |
| ----------------- | ------------ |
| `cx` / `cy`       | 圆心坐标     |
| `r`               | 半径（必需） |
| `fill` / `stroke` | 填充与描边   |

### 2.2 描边居中特性

SVG 描边以路径为中心，**向两侧各扩展 stroke-width/2**。这意味着半径 40、描边 4 的圆，实际占据 84×84 区域。

```html
<circle cx="50" cy="50" r="40" stroke="#000" stroke-width="4" fill="none" />
<!-- 实际边界：cx-r-strokeWidth/2 到 cx+r+strokeWidth/2，即 8 到 92 -->
```

## 3. 椭圆 ellipse

`<ellipse>` 用两个半径定义。

```html
<svg viewBox="0 0 200 100">
  <ellipse cx="100" cy="50" rx="80" ry="30" fill="#4f5bd5" />
</svg>
```

### 3.1 属性

| 属性        | 说明          |
| ----------- | ------------- |
| `cx` / `cy` | 圆心          |
| `rx` / `ry` | 水平/垂直半径 |

> 当 `rx === ry` 时，椭圆等价于圆形。

## 4. 直线 line

`<line>` 由两个端点定义。

```html
<svg viewBox="0 0 200 100">
  <line x1="10" y1="10" x2="190" y2="90" stroke="#333" stroke-width="2" />
  <line x1="10" y1="50" x2="190" y2="50" stroke="#d63031" stroke-width="4" stroke-dasharray="8 4" />
</svg>
```

### 4.1 属性

| 属性               | 说明                            |
| ------------------ | ------------------------------- |
| `x1` / `y1`        | 起点                            |
| `x2` / `y2`        | 终点                            |
| `stroke`           | 描边色（必需，否则不可见）      |
| `stroke-width`     | 描边宽度                        |
| `stroke-linecap`   | 端点形状：butt / round / square |
| `stroke-dasharray` | 虚线模式                        |

> `<line>` 默认无 fill，必须设置 stroke 才可见。

## 5. 折线 polyline

`<polyline>` 由一系列点连接，**不闭合**。

```html
<svg viewBox="0 0 200 100">
  <polyline
    points="10,90 50,10 90,90 130,10 170,90"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="2"
  />
</svg>
```

### 5.1 points 语法

```
points="x1,y1 x2,y2 x3,y3 ..."
```

也可用空格分隔：

```
points="10 90 50 10 90 90 130 10 170 90"
```

### 5.2 fill 陷阱

```html
<!-- 错误：默认 fill=black，会填充封闭区域 -->
<polyline points="10,90 50,10 90,90" />

<!-- 正确：折线需显式设置 fill="none" -->
<polyline points="10,90 50,10 90,90" fill="none" stroke="#000" />
```

## 6. 多边形 polygon

`<polygon>` 类似 polyline，但**自动闭合**首尾。

```html
<svg viewBox="0 0 200 100">
  <polygon points="100,10 190,90 10,90" fill="#4f5bd5" />
  <polygon points="100,10 140,50 100,90 60,50" fill="#00b894" stroke="#fff" stroke-width="2" />
</svg>
```

### 6.1 常见多边形

| 形状   | points 示例（以中心为参考）                                              |
| ------ | ------------------------------------------------------------------------ |
| 三角形 | `100,10 190,90 10,90`                                                    |
| 菱形   | `100,10 140,50 100,90 60,50`                                             |
| 五角星 | `100,10 120,70 180,70 130,105 150,165 100,130 50,165 70,105 20,70 80,70` |
| 六边形 | `100,10 170,50 170,110 100,150 30,110 30,50`                             |

## 7. 描边属性详解

### 7.1 stroke-linecap 端点

```html
<line x1="10" y1="20" x2="100" y2="20" stroke="#000" stroke-width="10" stroke-linecap="butt" />
<line x1="10" y1="40" x2="100" y2="40" stroke="#000" stroke-width="10" stroke-linecap="round" />
<line x1="10" y1="60" x2="100" y2="60" stroke="#000" stroke-width="10" stroke-linecap="square" />
```

| 值       | 效果                            |
| -------- | ------------------------------- |
| `butt`   | 平直端点（默认）                |
| `round`  | 半圆端点                        |
| `square` | 方形延伸（多出 stroke-width/2） |

### 7.2 stroke-linejoin 拐角

```html
<polyline
  points="10,90 50,10 90,90"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="miter"
/>
<polyline
  points="110,90 150,10 190,90"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="round"
/>
<polyline
  points="10,140 50,60 90,140"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="bevel"
/>
```

| 值      | 效果                                        |
| ------- | ------------------------------------------- |
| `miter` | 尖角（默认，可用 `stroke-miterlimit` 限制） |
| `round` | 圆角                                        |
| `bevel` | 斜切                                        |

### 7.3 stroke-dasharray 虚线

```html
<!-- 实线 -->
<line x1="10" y1="10" x2="190" y2="10" stroke="#000" />

<!-- 等长虚线：8px 实线 + 4px 空白 -->
<line x1="10" y1="30" x2="190" y2="30" stroke="#000" stroke-dasharray="8 4" />

<!-- 点线：1px 实线 + 4px 空白 -->
<line x1="10" y1="50" x2="190" y2="50" stroke="#000" stroke-dasharray="1 4" />

<!-- 复合虚线：10px + 4px + 2px + 4px -->
<line x1="10" y1="70" x2="190" y2="70" stroke="#000" stroke-dasharray="10 4 2 4" />
```

### 7.4 stroke-dashoffset 起始偏移

`stroke-dashoffset` 控制虚线起始位置，常用于动画绘制线条。

```html
<line x1="10" y1="90" x2="190" y2="90" stroke="#000" stroke-dasharray="180" stroke-dashoffset="0" />
<!-- dashoffset 从 180 → 0 动画可模拟"绘制"效果 -->
```

## 8. 基本图形对比

| 元素         | 必需属性      | 是否闭合 | 是否可填充             |
| ------------ | ------------- | -------- | ---------------------- |
| `<rect>`     | width, height | 是       | 是                     |
| `<circle>`   | r             | 是       | 是                     |
| `<ellipse>`  | rx, ry        | 是       | 是                     |
| `<line>`     | x1,y1,x2,y2   | 否       | 否（无 fill）          |
| `<polyline>` | points        | 否       | 是（但通常 fill=none） |
| `<polygon>`  | points        | 是       | 是                     |

## 9. 综合示例：简洁仪表盘

```html
<svg viewBox="0 0 200 200" width="200" height="200">
  <!-- 背景圆 -->
  <circle cx="100" cy="100" r="90" fill="none" stroke="#e0e0e0" stroke-width="12" />
  <!-- 进度弧（70%） -->
  <circle
    cx="100"
    cy="100"
    r="90"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="12"
    stroke-dasharray="396 565"
    stroke-dashoffset="-141"
    transform="rotate(-90 100 100)"
    stroke-linecap="round"
  />
  <!-- 中心文本 -->
  <text x="100" y="105" text-anchor="middle" font-size="36" fill="#333">70%</text>
</svg>
```

**原理**：

- 圆周长 ≈ 2π × 90 ≈ 565
- 70% 弧长 ≈ 396
- dasharray "396 565"：画 396 留 565
- rotate(-90 100 100)：从 12 点钟方向开始
- stroke-linecap="round"：端点圆滑

下一篇介绍强大的 `<path>`，它可表达任意形状。
## 矩形 rect

**矩形**
`<rect x="<左上x>" y="<左上y>" width="<宽>" height="<高>" [rx="<水平圆角>"] [ry="<垂直圆角>"] [fill="<填充色>"] [stroke="<描边色>"] [stroke-width="<描边宽度>"] />`
```html
<svg viewBox="0 0 300 150">
  <rect x="10" y="10" width="80" height="60" fill="#4f5bd5" />
  <rect x="110" y="10" width="80" height="60" rx="12" ry="12" fill="#00b894" />
  <rect x="210" y="10" width="80" height="60" rx="30" ry="10" fill="#d63031" />
</svg>
```

### rect 属性

| 属性               | 说明              | 默认值 |
| ------------------ | ----------------- | ------ |
| `x` / `y`          | 左上角坐标        | 0      |
| `width` / `height` | 宽高(必需)      | -      |
| `rx` / `ry`        | 水平/垂直圆角半径 | 0      |
| `fill`             | 填充色            | black  |
| `stroke`           | 描边色            | none   |
| `stroke-width`     | 描边宽度          | 1      |

> 当只设置 `rx` 时,`ry` 默认等于 `rx`,形成等圆角。

### 单侧圆角矩形(用 path 实现)
```html
<!-- 仅上方圆角 -->
<path d="M 10 30 Q 10 10 30 10 L 70 10 Q 90 10 90 30 L 90 70 L 10 70 Z" fill="#4f5bd5" />
```

---

## 圆形 circle

**圆形**
`<circle cx="<圆心x>" cy="<圆心y>" r="<半径>" [fill="<填充色>"] [stroke="<描边色>"] [stroke-width="<描边宽度>"] />`
```html
<svg viewBox="0 0 200 100">
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
  <circle cx="150" cy="50" r="40" fill="none" stroke="#d63031" stroke-width="3" />
</svg>
```

### circle 属性

| 属性              | 说明         |
| ----------------- | ------------ |
| `cx` / `cy`       | 圆心坐标     |
| `r`               | 半径(必需) |
| `fill` / `stroke` | 填充与描边   |

### 描边居中特性
SVG 描边以路径为中心,**向两侧各扩展 stroke-width/2**。半径 40、描边 4 的圆,实际占据 84×84 区域。
```html
<circle cx="50" cy="50" r="40" stroke="#000" stroke-width="4" fill="none" />
<!-- 实际边界:cx-r-strokeWidth/2 到 cx+r+strokeWidth/2,即 8 到 92 -->
```

---

## 椭圆 ellipse

**椭圆**
`<ellipse cx="<圆心x>" cy="<圆心y>" rx="<水平半径>" ry="<垂直半径>" [fill="<填充色>"] [stroke="<描边色>"] />`
```html
<svg viewBox="0 0 200 100">
  <ellipse cx="100" cy="50" rx="80" ry="30" fill="#4f5bd5" />
</svg>
```

### ellipse 属性

| 属性        | 说明          |
| ----------- | ------------- |
| `cx` / `cy` | 圆心          |
| `rx` / `ry` | 水平/垂直半径 |

> 当 `rx === ry` 时,椭圆等价于圆形。

---

## 直线 line

**直线**
`<line x1="<起点x>" y1="<起点y>" x2="<终点x>" y2="<终点y>" stroke="<描边色>" [stroke-width="<描边宽度>"] [stroke-linecap="<端点形状>"] [stroke-dasharray="<虚线模式>"] />`
```html
<svg viewBox="0 0 200 100">
  <line x1="10" y1="10" x2="190" y2="90" stroke="#333" stroke-width="2" />
  <line x1="10" y1="50" x2="190" y2="50" stroke="#d63031" stroke-width="4" stroke-dasharray="8 4" />
</svg>
```

### line 属性

| 属性               | 说明                            |
| ------------------ | ------------------------------- |
| `x1` / `y1`        | 起点                            |
| `x2` / `y2`        | 终点                            |
| `stroke`           | 描边色(必需,否则不可见)      |
| `stroke-width`     | 描边宽度                        |
| `stroke-linecap`   | 端点形状:butt / round / square |
| `stroke-dasharray` | 虚线模式                        |

> `<line>` 默认无 fill,必须设置 stroke 才可见。

---

## 折线 polyline

**折线(不闭合)**
`<polyline points="<x1,y1 x2,y2 x3,y3 ...>" [fill="<填充色>"] stroke="<描边色>" [stroke-width="<描边宽度>"] />`
```html
<svg viewBox="0 0 200 100">
  <polyline
    points="10,90 50,10 90,90 130,10 170,90"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="2"
  />
</svg>
```

### points 语法
```
points="x1,y1 x2,y2 x3,y3 ..."
```
也可用空格分隔:
```
points="10 90 50 10 90 90 130 10 170 90"
```

### fill 陷阱
```html
<!-- 错误:默认 fill=black,会填充封闭区域 -->
<polyline points="10,90 50,10 90,90" />

<!-- 正确:折线需显式设置 fill="none" -->
<polyline points="10,90 50,10 90,90" fill="none" stroke="#000" />
```

---

## 多边形 polygon

**多边形(自动闭合)**
`<polygon points="<x1,y1 x2,y2 ...>" [fill="<填充色>"] [stroke="<描边色>"] [stroke-width="<描边宽度>"] />`
```html
<svg viewBox="0 0 200 100">
  <polygon points="100,10 190,90 10,90" fill="#4f5bd5" />
  <polygon points="100,10 140,50 100,90 60,50" fill="#00b894" stroke="#fff" stroke-width="2" />
</svg>
```

### 常见多边形 points 示例

| 形状   | points 示例(以中心为参考)                                              |
| ------ | ------------------------------------------------------------------------ |
| 三角形 | `100,10 190,90 10,90`                                                    |
| 菱形   | `100,10 140,50 100,90 60,50`                                             |
| 五角星 | `100,10 120,70 180,70 130,105 150,165 100,130 50,165 70,105 20,70 80,70` |
| 六边形 | `100,10 170,50 170,110 100,150 30,110 30,50`                             |

---

## 描边属性

### stroke-linecap 端点

**stroke-linecap 端点形状**
`stroke-linecap="<butt | round | square>"`
```html
<line x1="10" y1="20" x2="100" y2="20" stroke="#000" stroke-width="10" stroke-linecap="butt" />
<line x1="10" y1="40" x2="100" y2="40" stroke="#000" stroke-width="10" stroke-linecap="round" />
<line x1="10" y1="60" x2="100" y2="60" stroke="#000" stroke-width="10" stroke-linecap="square" />
```

| 值       | 效果                            |
| -------- | ------------------------------- |
| `butt`   | 平直端点(默认)                |
| `round`  | 半圆端点                        |
| `square` | 方形延伸(多出 stroke-width/2) |

### stroke-linejoin 拐角

**stroke-linejoin 拐角形状**
`stroke-linejoin="<miter | round | bevel>"`
```html
<polyline
  points="10,90 50,10 90,90"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="miter"
/>
<polyline
  points="110,90 150,10 190,90"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="round"
/>
<polyline
  points="10,140 50,60 90,140"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="bevel"
/>
```

| 值      | 效果                                        |
| ------- | ------------------------------------------- |
| `miter` | 尖角(默认,可用 `stroke-miterlimit` 限制) |
| `round` | 圆角                                        |
| `bevel` | 斜切                                        |

### stroke-dasharray 虚线

**stroke-dasharray 虚线模式**
`stroke-dasharray="<实线长度 空白长度 ...>"`
```html
<!-- 实线 -->
<line x1="10" y1="10" x2="190" y2="10" stroke="#000" />

<!-- 等长虚线:8px 实线 + 4px 空白 -->
<line x1="10" y1="30" x2="190" y2="30" stroke="#000" stroke-dasharray="8 4" />

<!-- 点线:1px 实线 + 4px 空白 -->
<line x1="10" y1="50" x2="190" y2="50" stroke="#000" stroke-dasharray="1 4" />

<!-- 复合虚线:10px + 4px + 2px + 4px -->
<line x1="10" y1="70" x2="190" y2="70" stroke="#000" stroke-dasharray="10 4 2 4" />
```

### stroke-dashoffset 起始偏移

**stroke-dashoffset 虚线起始位置**
`stroke-dashoffset="<偏移量>"`
```html
<line x1="10" y1="90" x2="190" y2="90" stroke="#000" stroke-dasharray="180" stroke-dashoffset="0" />
<!-- dashoffset 从 180 → 0 动画可模拟"绘制"效果 -->
```

---

## 基本图形对比

| 元素         | 必需属性      | 是否闭合 | 是否可填充             |
| ------------ | ------------- | -------- | ---------------------- |
| `<rect>`     | width, height | 是       | 是                     |
| `<circle>`   | r             | 是       | 是                     |
| `<ellipse>`  | rx, ry        | 是       | 是                     |
| `<line>`     | x1,y1,x2,y2   | 否       | 否(无 fill)          |
| `<polyline>` | points        | 否       | 是(但通常 fill=none) |
| `<polygon>`  | points        | 是       | 是                     |

---

## 综合示例:仪表盘

**进度环图形**
```html
<svg viewBox="0 0 200 200" width="200" height="200">
  <!-- 背景圆 -->
  <circle cx="100" cy="100" r="90" fill="none" stroke="#e0e0e0" stroke-width="12" />
  <!-- 进度弧(70%) -->
  <circle
    cx="100"
    cy="100"
    r="90"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="12"
    stroke-dasharray="396 565"
    stroke-dashoffset="-141"
    transform="rotate(-90 100 100)"
    stroke-linecap="round"
  />
  <!-- 中心文本 -->
  <text x="100" y="105" text-anchor="middle" font-size="36" fill="#333">70%</text>
</svg>
```

参数说明:
- 圆周长 ≈ 2π × 90 ≈ 565
- 70% 弧长 ≈ 396
- dasharray "396 565":画 396 留 565
- rotate(-90 100 100):从 12 点钟方向开始
- stroke-linecap="round":端点圆滑

<!-- ============ 文档分隔线：012-svg/005-SVGPathDetailed.md ============ -->

## 1. 历史动机与发展脉络

### 1.1 路径数据的演进

SVG path 命令的设计源自 PostScript 的路径模型(1982 年由 John Warnock 设计),核心思想是用**命令序列**描述图形轮廓。这一模型经历了多个阶段:

| 时期 | 系统 | 命令风格 | 关键贡献 |
| ---- | ---- | -------- | -------- |
| 1982 | PostScript | `moveto`/`lineto`/`curveto`/`closepath` | 首次提出路径命令模型 |
| 1985 | Adobe Illustrator | 贝塞尔曲线编辑 | 引入三次贝塞尔交互 |
| 1990 | PDF | 简化 PostScript 路径 | 二进制路径数据 |
| 2001 | SVG 1.0 | `M`/`L`/`C`/`Q`/`A`/`Z` | XML 化路径数据 |
| 2018 | SVG 2 | 与 CSS path() 函数融合 | 路径作为 CSS 属性 |

### 1.2 贝塞尔曲线的历史

贝塞尔曲线由法国工程师 Pierre Bézier 于 1960 年在 Renault(雷诺)汽车公司推广用于车身设计,但数学基础由 Paul de Casteljau 于 1959 年在 Citroën(雪铁龙)提出。两者的命名差异反映了学术与工程的优先权之争:

- **de Casteljau 算法**(1959):递归细分,数值稳定
- **Bézier 曲线命名**(1960):公开发表,工业推广

SVG path 的 `C`/`Q`/`S`/`T` 命令直接对应贝塞尔曲线的控制点参数。

### 1.3 弧线命令的设计考量

SVG 的 `A` 命令采用"端点 + 半径 + 标志"的参数化方式,而非直接给出椭圆中心。这一选择源于两个约束:

1. **几何唯一性问题**:给定两端点与椭圆半径,存在 4 种可能的弧线(2 个中心位置 × 2 个弧长)
2. **避免冗余计算**:端点已知,中心可由方程推导

因此 SVG 选择用 `large-arc-flag` 与 `sweep-flag` 两个布尔值区分 4 种情况。

### 1.4 设计哲学:命令序列即数据

SVG path 的设计哲学可概括为"命令序列即数据":

- **可读性**:命令字母助记性强(M=Move, L=Line, C=Curve)
- **紧凑性**:相对坐标(小写)减少数字位数
- **可组合**:多个子路径通过 M 命令分隔
- **可解析**:语法简单,易于词法分析

这一设计使 path 既能作为矢量数据存储,也能作为编程接口操作。

## 2. 形式化定义

### 2.1 路径数据的形式化模型

SVG 路径数据可形式化为一个命令序列 $D = (c_1, c_2, \ldots, c_n)$,其中每个命令 $c_i$ 是一个元组:

$$
c_i = (\text{cmd}, \text{absolute}, \text{params})
$$

- $\text{cmd} \in \{M, L, H, V, C, S, Q, T, A, Z\}$ 是命令字母
- $\text{absolute} \in \{\text{true}, \text{false}\}$ 是绝对/相对标志(大写/小写)
- $\text{params}$ 是参数序列,长度由命令类型决定

### 2.2 当前点与子路径状态

路径解析器维护一个状态机,核心状态包括:

- **当前点(current point)** $P_c = (x_c, y_c)$:前一个命令的终点
- **当前子路径起点(subpath start)** $P_s = (x_s, y_s)$:最近的 M 命令终点
- **上一控制点(last control point)** $P_{lc} = (x_{lc}, y_{lc})$:用于 S/T 命令反射

每个命令根据状态计算新的几何点,并更新状态。M 命令会重置子路径起点;Z 命令将当前点设为子路径起点。

### 2.3 命令字母表

$$
\Sigma_{\text{path}} = \{M, L, H, V, C, S, Q, T, A, Z\}
$$

| 命令 | 含义 | 参数 | 参数数量 |
| ---- | ---- | ---- | -------- |
| `M` | 移动到(moveTo) | x, y | 2 |
| `L` | 直线到(lineTo) | x, y | 2 |
| `H` | 水平线 | x | 1 |
| `V` | 垂直线 | y | 1 |
| `C` | 三次贝塞尔 | x1,y1 x2,y2 x,y | 6 |
| `S` | 平滑三次贝塞尔 | x2,y2 x,y | 4 |
| `Q` | 二次贝塞尔 | x1,y1 x,y | 4 |
| `T` | 平滑二次贝塞尔 | x,y | 2 |
| `A` | 弧线 | rx,ry rot large,sweep x,y | 7 |
| `Z` | 闭合路径 | 无 | 0 |

### 2.4 绝对坐标 vs 相对坐标

大写命令使用**绝对坐标**(以 SVG 坐标系原点为参考),小写命令使用**相对坐标**(以前一命令终点为参考):

$$
\text{abs}(x, y) = (x, y), \quad \text{rel}(dx, dy) = (x_c + dx, y_c + dy)
$$

相对坐标的优势:

1. **紧凑性**:小数字,文件更小
2. **可移植性**:路径数据可平移而不修改内部坐标
3. **可复用性**:同一相对路径可在不同位置复用

### 2.5 贝塞尔曲线的参数化定义

n 次贝塞尔曲线 $B(t)$ 由 $n+1$ 个控制点 $P_0, P_1, \ldots, P_n$ 定义:

$$
B(t) = \sum_{i=0}^{n} \binom{n}{i} (1-t)^{n-i} t^i P_i, \quad t \in [0, 1]
$$

- **二次贝塞尔**(Q 命令):$n = 2$,3 个控制点 $P_0, P_1, P_2$
- **三次贝塞尔**(C 命令):$n = 3$,4 个控制点 $P_0, P_1, P_2, P_3$

其中 $P_0$ 是当前点(曲线起点),$P_1, P_2$ 是控制点,$P_3$ 是终点。

### 2.6 弧线的椭圆方程

SVG arc 命令隐含一个椭圆方程。设椭圆中心 $(c_x, c_y)$,半长轴 $r_x$,半短轴 $r_y$,旋转角 $\phi$,则椭圆上的点 $(x, y)$ 满足:

$$
\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix} \begin{bmatrix} r_x \cos\theta \\ r_y \sin\theta \end{bmatrix} + \begin{bmatrix} c_x \\ c_y \end{bmatrix}
$$

其中 $\theta \in [0, 2\pi)$ 是椭圆参数角。给定端点 $P_1, P_2$ 与半径 $r_x, r_y$,中心 $(c_x, c_y)$ 可通过解方程组获得(共有 2 个可能解)。

## 3. 理论推导与原理解析

### 3.1 de Casteljau 算法

de Casteljau 算法是计算贝塞尔曲线上点的递归方法,数值稳定且几何直观。对 n 次贝塞尔曲线:

$$
P_i^{(k)}(t) = (1-t) \cdot P_i^{(k-1)}(t) + t \cdot P_{i+1}^{(k-1)}(t)
$$

其中 $P_i^{(0)} = P_i$ 是原始控制点,$P_0^{(n)}(t) = B(t)$ 是曲线上的点。

**三次贝塞尔的 de Casteljau 推导**:

给定控制点 $P_0, P_1, P_2, P_3$,计算 $t = 0.5$ 处的点:

1. 一阶插值:$Q_0 = \frac{P_0 + P_1}{2}$, $Q_1 = \frac{P_1 + P_2}{2}$, $Q_2 = \frac{P_2 + P_3}{2}$
2. 二阶插值:$R_0 = \frac{Q_0 + Q_1}{2}$, $R_1 = \frac{Q_1 + Q_2}{2}$
3. 三阶插值:$S = \frac{R_0 + R_1}{2}$ 即为曲线上的点

这一算法可同时计算曲线导数(切线方向),对路径动画与 stroke-dasharray 计算至关重要。

### 3.2 贝塞尔曲线的导数

n 次贝塞尔曲线的导数是 $n-1$ 次贝塞尔曲线:

$$
B'(t) = n \sum_{i=0}^{n-1} (P_{i+1} - P_i) \binom{n-1}{i} (1-t)^{n-1-i} t^i
$$

- **二次贝塞尔导数**:$B'(t) = 2[(1-t)(P_1 - P_0) + t(P_2 - P_1)]$
- **三次贝塞尔导数**:$B'(t) = 3[(1-t)^2(P_1 - P_0) + 2t(1-t)(P_2 - P_1) + t^2(P_3 - P_2)]$

导数模长 $|B'(t)|$ 即切线长度,用于参数 $t$ 到弧长的转换。

### 3.3 路径长度的数值积分

路径长度 $L$ 可通过积分计算:

$$
L = \int_0^1 |B'(t)| \, dt
$$

对贝塞尔曲线,该积分无解析解,需用数值方法:

```javascript
function cubicBezierLength(p0, p1, p2, p3, segments = 100) {
  let length = 0;
  let prev = p0;
  for (let i = 1; i <= segments; i++) {
    const t = i / segments;
    const next = cubicBezierPoint(p0, p1, p2, p3, t);
    length += Math.hypot(next.x - prev.x, next.y - prev.y);
    prev = next;
  }
  return length;
}

function cubicBezierPoint(p0, p1, p2, p3, t) {
  const mt = 1 - t;
  const x = mt*mt*mt*p0.x + 3*mt*mt*t*p1.x + 3*mt*t*t*p2.x + t*t*t*p3.x;
  const y = mt*mt*mt*p0.y + 3*mt*mt*t*p1.y + 3*mt*t*t*p2.y + t*t*t*p3.y;
  return { x, y };
}
```

更精确的方法是 Gaussian quadrature(高斯积分),在少量采样点下获得高精度。

### 3.4 弧线参数的求解

给定 arc 命令 $A\ r_x\ r_y\ \phi\ f_a\ f_s\ x_2\ y_2$(起点 $P_1$,终点 $P_2$),椭圆中心 $(c_x, c_y)$ 的求解步骤:

**Step 1:计算端点中点与差向量**

$$
\vec{m} = \frac{P_1 + P_2}{2}, \quad \vec{d} = \frac{P_1 - P_2}{2}
$$

**Step 2:旋转坐标系**

$$
\begin{bmatrix} x_1' \\ y_1' \end{bmatrix} = \begin{bmatrix} \cos\phi & \sin\phi \\ -\sin\phi & \cos\phi \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix}
$$

**Step 3:修正半径(若端点距离超过椭圆直径)**

$$
r_x' = r_x \cdot k, \quad r_y' = r_y \cdot k, \quad k = \sqrt{\frac{x_1'^2}{r_x^2} + \frac{y_1'^2}{r_y^2}}, \quad k \ge 1
$$

**Step 4:计算中心偏移**

$$
\vec{c}' = \pm \sqrt{\frac{r_x'^2 r_y'^2 - r_x'^2 y_1'^2 - r_y'^2 x_1'^2}{r_x'^2 y_1'^2 + r_y'^2 x_1'^2}} \begin{bmatrix} r_x' y_1' / r_y' \\ -r_y' x_1' / r_x' \end{bmatrix}
$$

符号由 $f_a \neq f_s$ 决定(异或关系)。

**Step 5:逆旋转得到中心**

$$
\begin{bmatrix} c_x \\ c_y \end{bmatrix} = \begin{bmatrix} \cos\phi & -\sin\phi \\ \sin\phi & \cos\phi \end{bmatrix} \begin{bmatrix} c_x' \\ c_y' \end{bmatrix} + \begin{bmatrix} m_x \\ m_y \end{bmatrix}
$$

**Step 6:计算起止角度**

$$
\theta_1 = \text{atan2}\left(\frac{y_1' - c_y'}{r_y'}, \frac{x_1' - c_x'}{r_x'}\right), \quad \theta_2 = \text{atan2}\left(\frac{-y_1' - c_y'}{r_y'}, \frac{-x_1' - c_x'}{r_x'}\right)
$$

$sweep\_flag$ $f_s$ 决定 $\theta_2$ 大于还是小于 $\theta_1$。

### 3.5 fill-rule 算法

复杂路径的填充规则基于射线交叉计数:

**nonzero 规则**(默认):从点 $P$ 出发沿任意方向射线,统计路径穿越次数。每次顺时针穿越计数 +1,逆时针 -1。最终计数非零则填充。

$$
\text{fill}_{\text{nonzero}}(P) = \left( \sum_{i} \text{sign}(\text{cross}_i) \right) \neq 0
$$

**evenodd 规则**:不考虑方向,只统计穿越次数,奇数填充。

$$
\text{fill}_{\text{evenodd}}(P) = \left( \sum_{i} 1 \right) \mod 2 = 1
$$

### 3.6 平滑贝塞尔(S/T)的控制点反射

`S x2,y2 x,y` 命令的第一个控制点自动反射前一命令(必须是 C/S)的第二控制点:

$$
P_1' = 2 P_c - P_{lc}
$$

其中 $P_c$ 是当前点,$P_{lc}$ 是上一控制点。这一反射使曲线在连接点处保持 $C^1$ 连续(切线连续)。

`T x,y` 命令类似,但反射前一 Q/T 命令的控制点。

### 3.7 pathLength 的归一化语义

`pathLength` 属性将路径长度归一化为指定值 $L_n$。后续的 `stroke-dasharray`、`stroke-dashoffset` 等基于 $L_n$ 计算:

$$
\text{actual\_length} = \text{getTotalLength}(), \quad \text{scale} = \frac{L_n}{\text{actual\_length}}
$$

所有引用路径长度的属性都按 scale 缩放,使动画可基于归一化参数(0-100 或 0-1)编写。

### 3.8 多子路径的填充

单个 `<path>` 可包含多个 `M` 命令,形成多个独立子路径。填充规则应用于整个路径:

- **nonzero**:子路径方向决定填充(外顺 + 内逆 = 镂空)
- **evenodd**:子路径方向无关,只数穿越次数

这一性质常用于绘制环形、镂空图形(如五角星中心)。

## 4. 代码示例

### 4.1 path 概述

`<path>` 是 SVG 中最强大的元素,通过 `d` 属性的命令序列描述任意形状。所有基本图形都可用 path 表达。

```html
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M 10 10 L 190 10 L 190 90 L 10 90 Z" fill="#4f5bd5" />
</svg>
```

### 4.2 命令总览

| 命令 | 含义 | 参数 | 大小写区别 |
| ---- | ---- | ---- | ---------- |
| `M` | 移动到(moveTo) | x,y | 大写绝对,小写相对 |
| `L` | 直线到(lineTo) | x,y | 同上 |
| `H` | 水平线 | x | 同上 |
| `V` | 垂直线 | y | 同上 |
| `C` | 三次贝塞尔 | x1,y1 x2,y2 x,y | 同上 |
| `S` | 平滑三次贝塞尔 | x2,y2 x,y | 同上 |
| `Q` | 二次贝塞尔 | x1,y1 x,y | 同上 |
| `T` | 平滑二次贝塞尔 | x,y | 同上 |
| `A` | 弧线 | rx,ry rot large,sweep x,y | 同上 |
| `Z` | 闭合路径 | 无 | 大小写等价 |

> **绝对坐标**:以坐标系原点为参考;**相对坐标**:以前一命令终点为参考。

### 4.3 直线命令

#### 4.3.1 M / L

```html
<path d="M 10 10 L 100 10 L 100 50 L 10 50 Z" fill="#4f5bd5" />
```

绘制矩形:从 (10,10) → (100,10) → (100,50) → (10,50) → 闭合回起点。

#### 4.3.2 H / V

```html
<path d="M 10 10 H 100 V 50 H 10 Z" fill="#00b894" />
```

`H 100` 等价于 `L 100 当前y`,`V 50` 等价于 `L 当前x 50`。H/V 比 L 更紧凑,文件更小。

#### 4.3.3 相对坐标

```html
<!-- 绝对 -->
<path d="M 10 10 L 100 10 L 100 50" />
<!-- 相对:等价效果 -->
<path d="M 10 10 l 90 0 l 0 40" />
```

相对命令 `l 90 0` 表示从前一点向右移动 90,y 不变。

### 4.4 贝塞尔曲线

#### 4.4.1 二次贝塞尔 Q

`Q x1,y1 x,y`:一个控制点 + 终点。

```html
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <!-- 控制点 (100,10),终点 (190,90) -->
  <path d="M 10 90 Q 100 10 190 90" fill="none" stroke="#4f5bd5" stroke-width="3" />
  <!-- 辅助线 -->
  <line x1="10" y1="90" x2="100" y2="10" stroke="#ccc" stroke-dasharray="3" />
  <line x1="100" y1="10" x2="190" y2="90" stroke="#ccc" stroke-dasharray="3" />
</svg>
```

#### 4.4.2 平滑二次贝塞尔 T

`T x,y`:自动反射前一控制点,形成连续平滑曲线。

```html
<path d="M 10 90 Q 100 10 190 90 T 370 90" fill="none" stroke="#d63031" stroke-width="3" />
```

第二个控制点自动为 $(280, 170)$(反射 $(100, 10)$ 关于 $(190, 90)$),形成波浪。

#### 4.4.3 三次贝塞尔 C

`C x1,y1 x2,y2 x,y`:两个控制点 + 终点,可表达更复杂曲线。

```html
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <path d="M 10 50 C 50 10 150 90 190 50" fill="none" stroke="#00b894" stroke-width="3" />
</svg>
```

#### 4.4.4 平滑三次贝塞尔 S

`S x2,y2 x,y`:第二控制点自动反射,第一控制点需显式提供。

```html
<path d="M 10 50 C 50 10 100 90 150 50 S 250 10 290 50" fill="none" stroke="#d63031" />
```

### 4.5 弧线命令 A

```
A rx,ry x-axis-rotation large-arc-flag sweep-flag x,y
```

| 参数 | 含义 |
| ---- | ---- |
| `rx,ry` | 椭圆半径 |
| `x-axis-rotation` | 椭圆 x 轴旋转角度(度) |
| `large-arc-flag` | 0 短弧 / 1 长弧 |
| `sweep-flag` | 0 逆时针 / 1 顺时针 |
| `x,y` | 终点 |

#### 4.5.1 四种弧组合

```html
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <!-- 从 (50,100) 到 (150,100),半径 50 -->
  <path d="M 50 100 A 50 50 0 0 0 150 100" fill="none" stroke="#4f5bd5" />
  <path d="M 250 100 A 50 50 0 0 1 350 100" fill="none" stroke="#00b894" />
  <path d="M 50 50 A 50 50 0 1 0 150 50" fill="none" stroke="#d63031" />
  <path d="M 250 50 A 50 50 0 1 1 350 50" fill="none" stroke="#f9a825" />
</svg>
```

#### 4.5.2 圆弧扇形

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <path d="M 100 100 L 100 20 A 80 80 0 0 1 180 100 Z" fill="#4f5bd5" />
</svg>
```

绘制 1/4 扇形:从圆心 (100,100) → (100,20) → 顺时针弧到 (180,100) → 闭合。

### 4.6 闭合路径 Z

`Z`(或 `z`)从当前点连回 `M` 起点形成闭合。

```html
<!-- 不闭合:不画最后一条边 -->
<path d="M 10 10 L 100 10 L 100 50" fill="none" stroke="#000" />
<!-- 闭合:自动连接终点到起点 -->
<path d="M 10 10 L 100 10 L 100 50 Z" fill="#4f5bd5" />
```

> 闭合后 `fill` 才能正确填充内部。

### 4.7 路径填充规则 fill-rule

复杂路径(自相交或多子路径)的填充行为由 `fill-rule` 控制。

#### 4.7.1 nonzero(默认)

```html
<path
  d="M 10 10 L 190 10 L 190 90 L 10 90 Z M 50 30 L 150 30 L 150 70 L 50 70 Z"
  fill="#4f5bd5"
  fill-rule="nonzero"
/>
```

外矩形 + 内矩形:nonzero 规则下内矩形被"挖空"(外顺时针 + 内逆时针 → 区域计数为 0)。

#### 4.7.2 evenodd

```html
<path
  d="M 10 10 L 190 10 L 190 90 L 10 90 Z M 50 30 L 150 30 L 150 70 L 50 70 Z"
  fill="#00b894"
  fill-rule="evenodd"
/>
```

evenodd 规则下,无论方向,奇数次穿越绘制,偶数次不绘制 → 形成环带效果。

#### 4.7.3 五角星示例

```html
<!-- nonzero:中心填充 -->
<path
  d="M 100 10 L 120 70 L 180 70 L 130 105 L 150 165 L 100 130 L 50 165 L 70 105 L 20 70 L 80 70 Z"
  fill="#d63031"
  fill-rule="nonzero"
/>

<!-- evenodd:中心镂空 -->
<path
  d="M 100 10 L 120 70 L 180 70 L 130 105 L 150 165 L 100 130 L 50 165 L 70 105 L 20 70 L 80 70 Z"
  fill="#f9a825"
  fill-rule="evenodd"
/>
```

### 4.8 多子路径

单个 `<path>` 可包含多个 `M` 命令,形成多个独立子路径。

```html
<!-- 两个独立三角形 -->
<path d="M 10 10 L 90 10 L 50 90 Z M 110 10 L 190 10 L 150 90 Z" fill="#4f5bd5" />
```

### 4.9 路径长度与测量

`pathLength` 属性将路径归一化到指定长度,便于 stroke-dasharray 动画。

```html
<path
  d="M 10 50 Q 100 10 190 50"
  fill="none"
  stroke="#4f5bd5"
  stroke-width="3"
  pathLength="100"
  stroke-dasharray="50 50"
/>
<!-- pathLength=100,dasharray 50 50 表示画一半留一半 -->
```

JavaScript 获取实际长度:

```javascript
const path = document.querySelector('path');
const length = path.getTotalLength();
console.log(length); // 例如 200

const point = path.getPointAtLength(100); // 路径中点坐标
console.log(point.x, point.y);
```

### 4.10 stroke-dasharray 动画

```html
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <path
    id="animated-path"
    d="M 10 50 Q 100 10 190 50"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="3"
    stroke-dasharray="200"
    stroke-dashoffset="200"
  >
    <animate
      attributeName="stroke-dashoffset"
      from="200"
      to="0"
      dur="2s"
      repeatCount="indefinite"
    />
  </path>
</svg>
```

### 4.11 实战:手写心形

```html
<svg viewBox="0 0 100 100" width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <path
    d="M 50 30
       C 30 10 0 20 0 50
       C 0 70 30 90 50 100
       C 70 90 100 70 100 50
       C 100 20 70 10 50 30 Z"
    fill="#d63031"
  />
</svg>
```

**解析讲解**：

- 起点 (50,30):心形顶部凹陷
- C 到 (0,50):左半弧
- C 到 (50,100):底部尖角
- C 到 (100,50):右半弧
- C 回 (50,30):闭合

### 4.12 JavaScript 路径生成器

```javascript
class PathBuilder {
  constructor() {
    this.commands = [];
  }

  moveTo(x, y, relative = false) {
    this.commands.push(`${relative ? 'm' : 'M'} ${x} ${y}`);
    return this;
  }

  lineTo(x, y, relative = false) {
    this.commands.push(`${relative ? 'l' : 'L'} ${x} ${y}`);
    return this;
  }

  cubicBezier(x1, y1, x2, y2, x, y, relative = false) {
    this.commands.push(`${relative ? 'c' : 'C'} ${x1} ${y1} ${x2} ${y2} ${x} ${y}`);
    return this;
  }

  quadraticBezier(x1, y1, x, y, relative = false) {
    this.commands.push(`${relative ? 'q' : 'Q'} ${x1} ${y1} ${x} ${y}`);
    return this;
  }

  arc(rx, ry, rotation, largeArc, sweep, x, y, relative = false) {
    this.commands.push(
      `${relative ? 'a' : 'A'} ${rx} ${ry} ${rotation} ${largeArc ? 1 : 0} ${sweep ? 1 : 0} ${x} ${y}`
    );
    return this;
  }

  close() {
    this.commands.push('Z');
    return this;
  }

  build() {
    return this.commands.join(' ');
  }
}

// 使用示例:绘制圆角矩形
function roundedRectPath(x, y, width, height, r) {
  return new PathBuilder()
    .moveTo(x + r, y)
    .arc(r, r, 0, false, true, x + width, y + r)
    .arc(r, r, 0, false, true, x + width - r, y + height)
    .arc(r, r, 0, false, true, x, y + height - r)
    .arc(r, r, 0, false, true, x + r, y)
    .close()
    .build();
}

console.log(roundedRectPath(10, 10, 100, 80, 8));
// "M 18 10 A 8 8 0 0 1 110 18 A 8 8 0 0 1 102 90 A 8 8 0 0 1 10 82 A 8 8 0 0 1 18 10 Z"
```

### 4.13 de Casteljau 算法实现

```javascript
function deCasteljau(points, t) {
  if (points.length === 1) return points[0];
  const next = [];
  for (let i = 0; i < points.length - 1; i++) {
    next.push({
      x: (1 - t) * points[i].x + t * points[i + 1].x,
      y: (1 - t) * points[i].y + t * points[i + 1].y,
    });
  }
  return deCasteljau(next, t);
}

// 三次贝塞尔曲线点
function cubicBezier(p0, p1, p2, p3, t) {
  return deCasteljau([p0, p1, p2, p3], t);
}

// 二次贝塞尔曲线点
function quadraticBezier(p0, p1, p2, t) {
  return deCasteljau([p0, p1, p2], t);
}

// 使用
const p0 = { x: 10, y: 50 };
const p1 = { x: 50, y: 10 };
const p2 = { x: 150, y: 90 };
const p3 = { x: 190, y: 50 };
console.log(cubicBezier(p0, p1, p2, p3, 0.5)); // 中点
```

### 4.14 弧线参数求解

```javascript
function arcCenter(p1, p2, rx, ry, phi, largeArc, sweep) {
  const phiRad = (phi * Math.PI) / 180;
  const cosPhi = Math.cos(phiRad);
  const sinPhi = Math.sin(phiRad);

  // Step 1: 计算中点与差向量
  const mx = (p1.x + p2.x) / 2;
  const my = (p1.y + p2.y) / 2;
  const dx = (p1.x - p2.x) / 2;
  const dy = (p1.y - p2.y) / 2;

  // Step 2: 旋转坐标系
  const x1p = cosPhi * dx + sinPhi * dy;
  const y1p = -sinPhi * dx + cosPhi * dy;

  // Step 3: 修正半径
  const lambda = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry);
  const k = Math.sqrt(Math.max(1, lambda));
  rx *= k;
  ry *= k;

  // Step 4: 计算中心偏移
  const rx2 = rx * rx;
  const ry2 = ry * ry;
  const x1p2 = x1p * x1p;
  const y1p2 = y1p * y1p;

  const denom = rx2 * y1p2 + ry2 * x1p2;
  const numer = Math.sqrt(Math.max(0, (rx2 * ry2 - denom) / denom));
  const sign = largeArc !== sweep ? 1 : -1;

  const cxp = (sign * numer * rx * y1p) / ry;
  const cyp = (sign * numer * -ry * x1p) / rx;

  // Step 5: 逆旋转
  const cx = cosPhi * cxp - sinPhi * cyp + mx;
  const cy = sinPhi * cxp + cosPhi * cyp + my;

  // Step 6: 计算起止角度
  const theta1 = Math.atan2((y1p - cyp) / ry, (x1p - cxp) / rx);
  let theta2 = Math.atan2((-y1p - cyp) / ry, (-x1p - cxp) / rx);

  // 调整 theta2 范围
  if (!sweep && theta2 > theta1) theta2 -= 2 * Math.PI;
  if (sweep && theta2 < theta1) theta2 += 2 * Math.PI;

  return { cx, cy, rx, ry, phi: phiRad, theta1, theta2 };
}

// 使用示例
const center = arcCenter(
  { x: 50, y: 100 },
  { x: 150, y: 100 },
  50,
  50,
  0,
  false,
  true
);
console.log(center);
// { cx: 100, cy: 100, rx: 50, ry: 50, phi: 0, theta1: ..., theta2: ... }
```

## 5. 对比分析

### 5.1 SVG path vs Canvas Path2D

| 特性 | SVG path | Canvas Path2D |
| ---- | -------- | -------------- |
| 数据格式 | 字符串(d 属性) | JavaScript 对象 |
| 命令风格 | M/L/C/Q/A | moveTo/lineTo/bezierCurveTo/arc |
| 贝塞尔曲线 | 三次、二次 | 三次、二次 |
| 弧线 | A 命令(端点参数化) | arc(中心 + 角度参数化) |
| 平滑贝塞尔 | S/T 自动反射 | 需手动计算控制点 |
| 填充规则 | fill-rule | fill('evenodd'/'nonzero') |
| 序列化 | 原生支持 | 需手动序列化 |
| 编辑能力 | DOM 操作 | 不可编辑 |

### 5.2 SVG path vs PostScript path

| 特性 | SVG path | PostScript path |
| ---- | -------- | --------------- |
| 语法 | XML 属性 | PostScript 命令 |
| 命令字母 | M/L/C/Q/A/Z | moveto/lineto/curveto/closepath |
| 坐标类型 | 绝对 + 相对 | 仅绝对 |
| 弧线 | A 命令 | 通过 curveto 近似 |
| 平滑贝塞尔 | S/T | 需手动计算 |
| 文本格式 | 是 | 是 |

### 5.3 贝塞尔曲线 vs 样条曲线

| 特性 | 贝塞尔曲线 | B 样条曲线 | NURBS |
| ---- | ---------- | ---------- | ----- |
| 控制点影响 | 全局 | 局部 | 局部 |
| 节点数 | n+1 | 任意 | 任意 |
| 连续性 | $C^{n-1}$ | $C^{k-1}$ | $C^{k-1}$ |
| 权重 | 无 | 无 | 有 |
| 适用场景 | SVG/字体 | CAD | 高级建模 |
| 计算复杂度 | 低 | 中 | 高 |

### 5.4 nonzero vs evenodd

| 特性 | nonzero | evenodd |
| ---- | ------- | -------- |
| 方向敏感性 | 是 | 否 |
| 顺时针 + 逆时针 | 抵消(镂空) | 不抵消(填充) |
| 同向子路径 | 计数累加 | 计数累加 |
| 实现复杂度 | 中 | 低 |
| 适用场景 | 方向明确的设计 | 复杂嵌套图形 |

## 6. 常见陷阱与最佳实践

### 6.1 命令字母大小写混淆

```html
<!-- 错误:相对坐标用大写,导致位置错乱 -->
<path d="M 10 10 L 90 90" />
<!-- 等价于绝对坐标,从 (10,10) 到 (90,90) -->

<!-- 正确:相对坐标用小写 -->
<path d="M 10 10 l 90 90" />
<!-- 等价于从 (10,10) 移动 (90,90),到 (100,100) -->
```

### 6.2 弧线参数无解

```html
<!-- 错误:两点距离超过椭圆直径,导致自动放大半径 -->
<path d="M 0 0 A 50 50 0 0 1 200 0" />
<!-- 端点距离 200,但直径只有 100,半径会被放大到 100 -->
```

**最佳实践**:验证端点距离 $\leq 2 \cdot \max(r_x, r_y)$,否则半径会被自动修正。

### 6.3 Z 命令后未重置当前点

```html
<!-- 错误:Z 后继续画线,会从 Z 之前的终点开始 -->
<path d="M 10 10 L 100 10 Z L 100 100" />
<!-- L 100 100 从 (100,10) 开始,而非 (10,10) -->
```

**最佳实践**:Z 后若需在新位置画图,应使用 M 命令显式重置。

### 6.4 平滑贝塞尔前无 C/Q

```html
<!-- 错误:S 前没有 C,反射控制点未定义 -->
<path d="M 10 50 S 100 10 190 50" />
<!-- 第一控制点默认为当前点,等价于 Q -->
```

**最佳实践**:S 命令前应有 C 或 S 命令;T 命令前应有 Q 或 T 命令。

### 6.5 坐标精度过高

```html
<!-- 冗余:过多小数位 -->
<path d="M 10.123456789 20.987654321 L 100.111111111 50.222222222" />

<!-- 推荐:精度 2 位足够 -->
<path d="M 10.12 20.99 L 100.11 50.22" />
```

**最佳实践**:用 SVGO 自动压缩坐标精度,通常 2-3 位小数已足够视觉精度。

### 6.6 复杂路径未分组

```html
<!-- 难维护:所有形状在一个 path 内 -->
<path d="M 0 0 L 100 0 L 100 100 Z M 200 0 L 300 0 L 300 100 Z M ..." />

<!-- 推荐:逻辑分组用多个 path 或 g -->
<g fill="#4f5bd5">
  <path d="M 0 0 L 100 0 L 100 100 Z" />
  <path d="M 200 0 L 300 0 L 300 100 Z" />
</g>
```

### 6.7 路径方向影响 fill-rule

```html
<!-- nonzero 规则下,内矩形方向决定是否镂空 -->
<!-- 外顺 + 内顺 = 都填充 -->
<path d="M 10 10 L 190 10 L 190 90 L 10 90 Z M 50 30 L 150 30 L 150 70 L 50 70 Z" fill-rule="nonzero" />

<!-- 外顺 + 内逆 = 镂空 -->
<path d="M 10 10 L 190 10 L 190 90 L 10 90 Z M 50 70 L 150 70 L 150 30 L 50 30 Z" fill-rule="nonzero" />
```

**最佳实践**:需要镂空效果时,确保外环与内环方向相反(可通过 reverse 命令调整)。

### 6.8 pathLength 与实际长度混淆

```html
<!-- 误解:认为 pathLength=100 后,实际长度变为 100 -->
<path d="..." pathLength="100" />
<!-- 实际长度可能为 200,pathLength 仅影响 stroke-dasharray 等的归一化 -->
```

## 7. 工程实践

### 7.1 SVG 图标库设计

#### 7.1.1 统一 viewBox 与坐标系

```xml
<!-- 所有图标统一 24×24 viewBox -->
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M 12 2 L 22 22 L 2 22 Z" fill="currentColor" />
</svg>
```

#### 7.1.2 路径数据 TypeScript 类型

```typescript
// SVG path 命令类型定义
type PathCommand =
  | { cmd: 'M'; x: number; y: number; absolute: boolean }
  | { cmd: 'L'; x: number; y: number; absolute: boolean }
  | { cmd: 'C'; x1: number; y1: number; x2: number; y2: number; x: number; y: number; absolute: boolean }
  | { cmd: 'Q'; x1: number; y1: number; x: number; y: number; absolute: boolean }
  | { cmd: 'A'; rx: number; ry: number; rotation: number; largeArc: boolean; sweep: boolean; x: number; y: number; absolute: boolean }
  | { cmd: 'Z' };

function commandsToPath(commands: PathCommand[]): string {
  return commands.map((c) => {
    const prefix = c.absolute ? c.cmd : c.cmd.toLowerCase();
    switch (c.cmd) {
      case 'M':
      case 'L':
        return `${prefix} ${c.x} ${c.y}`;
      case 'C':
        return `${prefix} ${c.x1} ${c.y1} ${c.x2} ${c.y2} ${c.x} ${c.y}`;
      case 'Q':
        return `${prefix} ${c.x1} ${c.y1} ${c.x} ${c.y}`;
      case 'A':
        return `${prefix} ${c.rx} ${c.ry} ${c.rotation} ${c.largeArc ? 1 : 0} ${c.sweep ? 1 : 0} ${c.x} ${c.y}`;
      case 'Z':
        return 'Z';
    }
  }).join(' ');
}
```

### 7.2 Vue 3 SVG 路径组件

```vue
<template>
  <svg
    :viewBox="`0 0 ${size} ${size}`"
    :width="size"
    :height="size"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      :d="path"
      :fill="color"
      :stroke="stroke"
      :stroke-width="strokeWidth"
      :fill-rule="fillRule"
    />
  </svg>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  path: { type: String, required: true },
  size: { type: [Number, String], default: 24 },
  color: { type: String, default: 'currentColor' },
  stroke: { type: String, default: 'none' },
  strokeWidth: { type: [Number, String], default: 0 },
  fillRule: { type: String, default: 'nonzero' },
});

const size = computed(() => Number(props.size));
</script>
```

### 7.3 React SVG 路径组件

```jsx
import { memo } from 'react';

const SVGIcon = memo(function SVGIcon({
  path,
  size = 24,
  color = 'currentColor',
  stroke = 'none',
  strokeWidth = 0,
  fillRule = 'nonzero',
  title,
  ...rest
}) {
  return (
    <svg
      viewBox={`0 0 ${size} ${size}`}
      width={size}
      height={size}
      xmlns="http://www.w3.org/2000/svg"
      role={title ? 'img' : 'presentation'}
      aria-hidden={title ? undefined : true}
      aria-label={title}
      {...rest}
    >
      {title && <title>{title}</title>}
      <path
        d={path}
        fill={color}
        stroke={stroke}
        strokeWidth={strokeWidth}
        fillRule={fillRule}
      />
    </svg>
  );
});

export default SVGIcon;
```

### 7.4 SVGO 优化配置

```javascript
// svgo.config.js
module.exports = {
  plugins: [
    'preset-default',
    {
      name: 'convertPathData',
      params: {
        // 使用相对坐标
        utilizeAbsolute: false,
        // 移除不必要的小数
        floatPrecision: 3,
        // 合并连续命令
        mergeRepeated: true,
        // 移除冗余命令
        removeUseless: true,
      },
    },
    {
      name: 'convertTransform',
      params: {
        convertToShorts: true,
      },
    },
    'removeViewBox',
    'removeDimensions',
  ],
};
```

### 7.5 路径长度计算工具

```javascript
class PathLengthCalculator {
  constructor() {
    this.segments = [];
  }

  // 解析路径数据
  parse(d) {
    const tokens = d.match(/[a-zA-Z]|-?\d*\.?\d+/g);
    let cmd = null;
    let i = 0;
    let current = { x: 0, y: 0 };
    let start = { x: 0, y: 0 };

    while (i < tokens.length) {
      if (/[a-zA-Z]/.test(tokens[i])) {
        cmd = tokens[i++];
      }
      const abs = cmd === cmd.toUpperCase();
      const lower = cmd.toLowerCase();

      switch (lower) {
        case 'm':
          current = this.parsePoint(tokens, i, abs, current);
          i += 2;
          start = { ...current };
          break;
        case 'l':
        case 'h':
        case 'v': {
          const next = this.parseLine(lower, tokens, i, abs, current);
          this.segments.push({ type: 'L', start: current, end: next });
          current = next;
          i += lower === 'l' ? 2 : 1;
          break;
        }
        case 'c': {
          const seg = this.parseCubic(tokens, i, abs, current);
          this.segments.push(seg);
          current = seg.end;
          i += 6;
          break;
        }
        case 'z':
          this.segments.push({ type: 'L', start: current, end: start });
          current = { ...start };
          i += 0;
          break;
        // 其他命令略
        default:
          i++;
      }
    }
    return this.segments;
  }

  parsePoint(tokens, i, abs, current) {
    const x = parseFloat(tokens[i]);
    const y = parseFloat(tokens[i + 1]);
    return abs ? { x, y } : { x: current.x + x, y: current.y + y };
  }

  parseLine(cmd, tokens, i, abs, current) {
    if (cmd === 'l') return this.parsePoint(tokens, i, abs, current);
    if (cmd === 'h') {
      const x = parseFloat(tokens[i]);
      return abs ? { x, y: current.y } : { x: current.x + x, y: current.y };
    }
    if (cmd === 'v') {
      const y = parseFloat(tokens[i]);
      return abs ? { x: current.x, y } : { x: current.x, y: current.y + y };
    }
  }

  parseCubic(tokens, i, abs, current) {
    const p = (offset) => this.parsePoint(tokens, i + offset, abs, current);
    const c1 = p(0);
    const c2 = p(2);
    const end = p(4);
    return { type: 'C', start: current, c1, c2, end };
  }

  // 计算总长度
  totalLength() {
    return this.segments.reduce((sum, seg) => sum + this.segmentLength(seg), 0);
  }

  segmentLength(seg) {
    if (seg.type === 'L') {
      return Math.hypot(seg.end.x - seg.start.x, seg.end.y - seg.start.y);
    }
    if (seg.type === 'C') {
      // 数值积分
      let length = 0;
      let prev = seg.start;
      const samples = 100;
      for (let i = 1; i <= samples; i++) {
        const t = i / samples;
        const p = this.cubicPoint(seg, t);
        length += Math.hypot(p.x - prev.x, p.y - prev.y);
        prev = p;
      }
      return length;
    }
    return 0;
  }

  cubicPoint(seg, t) {
    const { start, c1, c2, end } = seg;
    const mt = 1 - t;
    return {
      x: mt*mt*mt*start.x + 3*mt*mt*t*c1.x + 3*mt*t*t*c2.x + t*t*t*end.x,
      y: mt*mt*mt*start.y + 3*mt*mt*t*c1.y + 3*mt*t*t*c2.y + t*t*t*end.y,
    };
  }
}
```

### 7.6 SVG 编辑器核心逻辑

```javascript
class SVGPathEditor {
  constructor(svg) {
    this.svg = svg;
    this.history = [];
    this.currentPath = null;
    this.controlPoints = [];
  }

  // 开始新路径
  startPath(x, y) {
    this.currentPath = `M ${x} ${y}`;
    this.renderPath();
  }

  // 添加直线
  addLine(x, y) {
    this.currentPath += ` L ${x} ${y}`;
    this.renderPath();
    this.saveHistory();
  }

  // 添加三次贝塞尔
  addCubicBezier(x1, y1, x2, y2, x, y) {
    this.currentPath += ` C ${x1} ${y1} ${x2} ${y2} ${x} ${y}`;
    this.renderPath();
    this.saveHistory();
  }

  // 闭合路径
  closePath() {
    this.currentPath += ' Z';
    this.renderPath();
    this.saveHistory();
  }

  renderPath() {
    const path = this.svg.querySelector('path.editing');
    if (!path) {
      const newPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      newPath.setAttribute('class', 'editing');
      newPath.setAttribute('fill', 'none');
      newPath.setAttribute('stroke', '#4f5bd5');
      this.svg.appendChild(newPath);
    }
    this.svg.querySelector('path.editing').setAttribute('d', this.currentPath);
  }

  saveHistory() {
    this.history.push(this.currentPath);
  }

  undo() {
    if (this.history.length > 1) {
      this.history.pop();
      this.currentPath = this.history[this.history.length - 1];
      this.renderPath();
    }
  }
}
```

## 8. 案例研究

### 8.1 案例一:Material Design 图标

Google Material Icons 大量使用 path 命令:

```xml
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
</svg>
```

**设计要点**:

1. 使用相对坐标(l 小写)减少数字位数
2. 弧线 A 命令精确绘制圆角
3. 单一 path 简化 DOM 结构

### 8.2 案例二:Heroicons 体系

```xml
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
</svg>
```

**设计要点**:

1. 使用 stroke 而非 fill,便于主题化
2. `stroke-linecap="round"` 让端点圆润
3. 简洁命令序列

### 8.3 案例三:Lucide Icons

```xml
<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
</svg>
```

### 8.4 案例四:Bootstrap Icons

```xml
<svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zM1.5 8a6.5 6.5 0 1 1 13 0 6.5 6.5 0 0 1-13 0z"/>
</svg>
```

**设计要点**:

1. 使用 `fill-rule="evenodd"` 处理环形
2. 单 path 完成圆形 + 镂空
3. 16×16 viewBox 适配密集 UI

### 8.5 案例五:D3.js 数据可视化

```javascript
import * as d3 from 'd3';

// 生成路径数据
const line = d3.line()
  .x((d) => xScale(d.x))
  .y((d) => yScale(d.y))
  .curve(d3.curveCatmullRom); // 平滑曲线

const path = svg.append('path')
  .datum(data)
  .attr('d', line)
  .attr('fill', 'none')
  .attr('stroke', '#4f5bd5');
```

D3.js 内部将曲线插值转换为 SVG path 命令,支持贝塞尔、B 样条等多种插值。

### 8.6 案例六:FANDEX 项目实战

FANDEX 项目使用 path 命令绘制知识图谱节点连接线:

```html
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- 节点 -->
  <circle cx="100" cy="100" r="20" fill="#4f5bd5" />
  <circle cx="700" cy="500" r="20" fill="#00b894" />

  <!-- 贝塞尔曲线连接 -->
  <path
    d="M 120 100 C 300 50, 500 550, 680 500"
    fill="none"
    stroke="#999"
    stroke-width="2"
    stroke-dasharray="4 4"
  >
    <animate attributeName="stroke-dashoffset" from="0" to="8" dur="0.5s" repeatCount="indefinite" />
  </path>
</svg>
```

**应用场景**:

1. 知识图谱节点关系连线
2. 流程图箭头
3. 数据可视化曲线
4. 装饰性背景

### 填空题知识点讲解

**题目 6**:贝塞尔曲线的数学基础由 ________ 于 1959 年提出,但工业推广由 ________ 于 1960 年完成。

**解析讲解**：`Paul de Casteljau`(de Casteljau);`Pierre Bézier`(Bézier)

**解析讲解**：de Casteljau 在 Citroën 提出算法,Bézier 在 Renault 推广工业应用。由于 Bézier 公开发表,曲线以他命名,但 de Casteljau 算法保留原创者名。

**题目 7**:`pathLength="100"` 的作用是将路径长度归一化为 ________,后续 stroke-dasharray 基于 ________ 计算。

**解析讲解**：`100`;`100`(归一化值)

**解析讲解**：pathLength 不改变实际路径长度,只是将引用路径长度的属性(stroke-dasharray、stroke-dashoffset)按归一化值计算。例如 stroke-dasharray="50 50" 在 pathLength=100 时表示画一半留一半。

**题目 8**:arc 命令的 `large-arc-flag` 与 `sweep-flag` 共可表示 ________ 种弧组合。

**解析讲解**：`4`

**解析讲解**：large-arc-flag(0/1) × sweep-flag(0/1) = 4 种组合,分别对应:短弧逆时针、短弧顺时针、长弧逆时针、长弧顺时针。

**题目 9**:`Z` 命令将当前点连接到 ________,并使路径 ________。

**解析讲解**：`M 命令的起点(子路径起点)`;`闭合(可填充内部)`

**解析讲解**：Z 命令画一条直线从当前点回到子路径起点(最近 M 命令终点),形成闭合路径。闭合后 fill 才能正确填充内部。

**题目 10**:三次贝塞尔曲线 $B(t) = \sum_{i=0}^{3} \binom{3}{i} (1-t)^{3-i} t^i P_i$ 的展开形式是 ________。

**解析讲解**：$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3$

**解析讲解**：三次贝塞尔的 Bernstein 多项式展开,其中 $\binom{3}{0}=\binom{3}{3}=1$, $\binom{3}{1}=\binom{3}{2}=3$。

### 编程题知识点讲解

**题目 11**:用 path 命令绘制一个五角星,中心在 (100,100),外接圆半径 80,要求:

1. 五角星 10 个顶点(5 外 + 5 内)
2. 内顶点距中心 32(外接圆的 0.4 倍)
3. 使用 Z 命令闭合
4. 测试 nonzero 与 evenodd 的填充差异

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <!-- 5 外顶点角度:90°, 162°, 234°, 306°, 18°(数学逆时针) -->
  <!-- SVG Y 轴向下,故用 -angle 翻转 -->

  <!-- nonzero:中心填充 -->
  <path
    d="M 100 20
       L 124.7 84.8
       L 190.2 84.8
       L 137.3 124.7
       L 156.6 188.5
       L 100 150.4
       L 43.4 188.5
       L 62.7 124.7
       L 9.8 84.8
       L 75.3 84.8
       Z"
    fill="#d63031"
    fill-rule="nonzero"
    transform="translate(0 0)"
  />

  <!-- evenodd:中心镂空 -->
  <path
    d="M 100 20
       L 124.7 84.8
       L 190.2 84.8
       L 137.3 124.7
       L 156.6 188.5
       L 100 150.4
       L 43.4 188.5
       L 62.7 124.7
       L 9.8 84.8
       L 75.3 84.8
       Z"
    fill="#f9a825"
    fill-rule="evenodd"
    transform="translate(220 0)"
  />
</svg>
```

**顶点计算公式**:

```javascript
function starPoints(cx, cy, rOuter, rInner, points) {
  const coords = [];
  for (let i = 0; i < points * 2; i++) {
    const r = i % 2 === 0 ? rOuter : rInner;
    const angle = (Math.PI / points) * i - Math.PI / 2; // 起点在顶部
    coords.push({
      x: cx + r * Math.cos(angle),
      y: cy + r * Math.sin(angle),
    });
  }
  return coords;
}

const points = starPoints(100, 100, 80, 32, 5);
const d = `M ${points[0].x.toFixed(1)} ${points[0].y.toFixed(1)} ` +
  points.slice(1).map((p) => `L ${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' ') +
  ' Z';
console.log(d);
```

**评分标准**:

- 顶点计算正确(4 分)
- 路径闭合(2 分)
- nonzero vs evenodd 对比展示(4 分)

**题目 12**:实现一个 JavaScript 函数,将 SVG path 数据转换为点序列,要求:

1. 支持 M、L、H、V、C、Q、Z 命令
2. 处理绝对/相对坐标
3. 对贝塞尔曲线采样为线段
4. 返回点数组用于后续处理

```javascript
function parsePathToPoints(d, options = {}) {
  const {
    bezierSegments = 20, // 贝塞尔采样段数
  } = options;

  const tokens = d.match(/[a-zA-Z]|-?\d*\.?\d+(?:e[-+]?\d+)?/g);
  let i = 0;
  let cmd = null;
  let current = { x: 0, y: 0 };
  let subpathStart = { x: 0, y: 0 };
  const points = [];

  while (i < tokens.length) {
    if (/[a-zA-Z]/.test(tokens[i])) {
      cmd = tokens[i++];
    }
    const abs = cmd === cmd.toUpperCase();
    const lower = cmd.toLowerCase();

    switch (lower) {
      case 'm': {
        const x = parseFloat(tokens[i++]);
        const y = parseFloat(tokens[i++]);
        current = abs ? { x, y } : { x: current.x + x, y: current.y + y };
        subpathStart = { ...current };
        points.push({ ...current });
        break;
      }
      case 'l': {
        const x = parseFloat(tokens[i++]);
        const y = parseFloat(tokens[i++]);
        current = abs ? { x, y } : { x: current.x + x, y: current.y + y };
        points.push({ ...current });
        break;
      }
      case 'h': {
        const x = parseFloat(tokens[i++]);
        current = abs ? { x, y: current.y } : { x: current.x + x, y: current.y };
        points.push({ ...current });
        break;
      }
      case 'v': {
        const y = parseFloat(tokens[i++]);
        current = abs ? { x: current.x, y } : { x: current.x, y: current.y + y };
        points.push({ ...current });
        break;
      }
      case 'c': {
        const nums = tokens.slice(i, i + 6).map(parseFloat);
        i += 6;
        const [x1, y1, x2, y2, x, y] = nums;
        const c1 = abs ? { x: x1, y: y1 } : { x: current.x + x1, y: current.y + y1 };
        const c2 = abs ? { x: x2, y: y2 } : { x: current.x + x2, y: current.y + y2 };
        const end = abs ? { x, y } : { x: current.x + x, y: current.y + y };
        // 采样贝塞尔
        for (let t = 1; t <= bezierSegments; t++) {
          const u = t / bezierSegments;
          const mu = 1 - u;
          points.push({
            x: mu*mu*mu*current.x + 3*mu*mu*u*c1.x + 3*mu*u*u*c2.x + u*u*u*end.x,
            y: mu*mu*mu*current.y + 3*mu*mu*u*c1.y + 3*mu*u*u*c2.y + u*u*u*end.y,
          });
        }
        current = end;
        break;
      }
      case 'q': {
        const nums = tokens.slice(i, i + 4).map(parseFloat);
        i += 4;
        const [x1, y1, x, y] = nums;
        const c1 = abs ? { x: x1, y: y1 } : { x: current.x + x1, y: current.y + y1 };
        const end = abs ? { x, y } : { x: current.x + x, y: current.y + y };
        for (let t = 1; t <= bezierSegments; t++) {
          const u = t / bezierSegments;
          const mu = 1 - u;
          points.push({
            x: mu*mu*current.x + 2*mu*u*c1.x + u*u*end.x,
            y: mu*mu*current.y + 2*mu*u*c1.y + u*u*end.y,
          });
        }
        current = end;
        break;
      }
      case 'z': {
        points.push({ ...subpathStart });
        current = { ...subpathStart };
        break;
      }
      default:
        i++;
    }
  }

  return points;
}

// 使用示例
const points = parsePathToPoints('M 10 10 L 100 100 C 150 50 200 150 250 100 Z');
console.log(points);
```

**评分标准**:

- 命令解析正确(4 分)
- 绝对/相对处理(2 分)
- 贝塞尔采样(2 分)
- Z 命令处理(2 分)

### 10.1 W3C 规范

1. W3C. 2018. **SVG 2 Specification: Path Element**. W3C Recommendation. https://www.w3.org/TR/SVG2/paths.html

2. W3C. 2003. **SVG 1.1 Specification: Path**. W3C Recommendation. https://www.w3.org/TR/SVG11/paths.html

3. W3C. 2023. **CSS Masking Module Level 1: fill-rule**. W3C Candidate Recommendation. https://www.w3.org/TR/css-masking-1/

### 10.2 学术论文

4. Bézier, P. 1966. **Définition numérique des courbes et surfaces I**. *Automatisme* 11, 625–632.

5. Bézier, P. 1967. **Définition numérique des courbes et surfaces II**. *Automatisme* 12, 17–21.

6. de Casteljau, P. 1959. **Courbes à pôles**. *National Industrial Property Institute* (INPI), Paris, France.

7. Farin, G. 1993. **Curves and Surfaces for Computer-Aided Geometric Design: A Practical Guide** (3rd ed.). Academic Press, Boston, MA, USA. https://doi.org/10.1016/B978-0-12-249052-7.X5001-5

8. Foley, J. D., van Dam, A., Feiner, S. K., and Hughes, J. F. 2013. **Computer Graphics: Principles and Practice** (3rd ed.). Addison-Wesley Professional.

9. Piegl, L. and Tiller, W. 1997. **The NURBS Book** (2nd ed.). Springer-Verlag, Berlin, Heidelberg, Germany. https://doi.org/10.1007/978-3-642-59223-2

### 10.3 工程实践参考

10. Eisenberg, J. D. 2014. **SVG Essentials** (2nd ed.). O'Reilly Media, Sebastopol, CA, USA.

11. Bellamy-Royds, A., Eisenberg, J. D., and Ginger, D. 2017. **Using SVG with CSS3 and HTML5**. O'Reilly Media.

12. Bostock, M., Ogievetsky, V., and Heer, J. 2011. **D3: Data-Driven Documents**. *IEEE Transactions on Visualization and Computer Graphics* 17, 12, 2301–2309. https://doi.org/10.1109/TVCG.2011.185

### 11.1 计算机图形学

- **MIT 6.837 Computer Graphics**:深入理解贝塞尔曲线、B 样条、NURBS
- **Stanford CS248 Introduction to Computer Graphics**:曲线与曲面的数学基础
- **CMU 15-462/662 Computer Graphics**:从理论到实现的完整覆盖
- **Farin, G. Curves and Surfaces for CAGD**:CAD/CAM 领域的曲线曲面圣经

### 11.2 字体设计

- **OpenType Specification**:字体中贝塞尔曲线的应用
- **TrueType Reference Manual**:二次贝塞尔在 TrueType 中的使用
- **Frutiger, A. Type Sign Symbol**:字体设计与几何美学

### 11.3 数据可视化

- **D3.js 文档**:曲线插值器(curveBasis、curveCardinal、curveCatmullRom)
- **Munzner, T. Visualization Analysis and Design**:可视化中的路径应用
- **Wilkinson, L. The Grammar of Graphics**:图形语法的路径表示

### 11.4 相关工具

- **SVGO**:路径数据压缩与优化
- **Inkscape**:开源 SVG 编辑器,可视化路径编辑
- **Figma**:设计工具的路径布尔运算
- **Illustrator**:Adobe 的路径编辑工具

### 11.5 进阶主题

- **CSS path() 函数**:SVG 2 将 path 数据作为 CSS 属性
- **Houdini API**:自定义路径渲染
- **WebGPU 路径渲染**:GPU 加速的曲线细分
- **Variable Fonts**:可变字体与路径插值

下一篇介绍 SVG 文本,包括 `<text>`、`<tspan>`、`<textPath>` 等排版能力,在路径基础上扩展沿路径排版的复合应用。
## path 元素

**path 路径元素**
`<path d="<命令序列>" [fill="<填充色>"] [stroke="<描边色>"] [stroke-width="<描边宽度>"] [fill-rule="<填充规则>"] [pathLength="<归一化长度>"] />`
```html
<svg viewBox="0 0 200 100">
  <path d="M 10 10 L 190 10 L 190 90 L 10 90 Z" fill="#4f5bd5" />
</svg>
```

---

## 命令总览

| 命令 | 含义             | 参数                      | 大小写区别         |
| ---- | ---------------- | ------------------------- | ------------------ |
| `M`  | 移动到(moveTo) | x,y                       | 大写绝对,小写相对 |
| `L`  | 直线到(lineTo) | x,y                       | 同上               |
| `H`  | 水平线           | x                         | 同上               |
| `V`  | 垂直线           | y                         | 同上               |
| `C`  | 三次贝塞尔       | x1,y1 x2,y2 x,y           | 同上               |
| `S`  | 平滑三次贝塞尔   | x2,y2 x,y                 | 同上               |
| `Q`  | 二次贝塞尔       | x1,y1 x,y                 | 同上               |
| `T`  | 平滑二次贝塞尔   | x,y                       | 同上               |
| `A`  | 弧线             | rx,ry rot large,sweep x,y | 同上               |
| `Z`  | 闭合路径         | 无                        | 大小写等价         |

> **绝对坐标**:以坐标系原点为参考;**相对坐标**:以前一命令终点为参考。

---

## 直线命令

### M / L 移动与直线

**M L 直线**
`d="M <x> <y> L <x> <y> ..."`
```html
<path d="M 10 10 L 100 10 L 100 50 L 10 50 Z" fill="#4f5bd5" />
```

### H / V 水平与垂直线

**H V 直线**
`d="M <x> <y> H <x> V <y> ..."`
```html
<path d="M 10 10 H 100 V 50 H 10 Z" fill="#00b894" />
```

`H 100` 等价于 `L 100 当前y`,`V 50` 等价于 `L 当前x 50`。

### 相对坐标

**小写命令相对坐标**
```html
<!-- 绝对 -->
<path d="M 10 10 L 100 10 L 100 50" />
<!-- 相对:等价效果 -->
<path d="M 10 10 l 90 0 l 0 40" />
```

相对命令 `l 90 0` 表示从前一点向右移动 90,y 不变。

---

## 贝塞尔曲线

### Q 二次贝塞尔

**Q 二次贝塞尔**
`d="... Q <控制点x> <控制点y> <终点x> <终点y>"`
```html
<svg viewBox="0 0 200 100">
  <!-- 控制点 (100,10),终点 (190,90) -->
  <path d="M 10 90 Q 100 10 190 90" fill="none" stroke="#4f5bd5" stroke-width="3" />
  <!-- 辅助线 -->
  <line x1="10" y1="90" x2="100" y2="10" stroke="#ccc" stroke-dasharray="3" />
  <line x1="100" y1="10" x2="190" y2="90" stroke="#ccc" stroke-dasharray="3" />
</svg>
```

### T 平滑二次贝塞尔

**T 平滑二次贝塞尔**
`d="... T <终点x> <终点y>"`
```html
<path d="M 10 90 Q 100 10 190 90 T 370 90" fill="none" stroke="#d63031" stroke-width="3" />
```

第二个控制点自动为 (280, 170),形成波浪。

### C 三次贝塞尔

**C 三次贝塞尔**
`d="... C <控制点1x> <控制点1y> <控制点2x> <控制点2y> <终点x> <终点y>"`
```html
<svg viewBox="0 0 200 100">
  <path d="M 10 50 C 50 10 150 90 190 50" fill="none" stroke="#00b894" stroke-width="3" />
</svg>
```

### S 平滑三次贝塞尔

**S 平滑三次贝塞尔**
`d="... S <控制点2x> <控制点2y> <终点x> <终点y>"`
```html
<path d="M 10 50 C 50 10 100 90 150 50 S 250 10 290 50" fill="none" stroke="#d63031" />
```

---

## 弧线命令 A

**A 弧线命令**
`d="... A <rx> <ry> <x-axis-rotation> <large-arc-flag> <sweep-flag> <终点x> <终点y>"`

| 参数              | 含义                |
| ----------------- | ------------------- |
| `rx,ry`           | 椭圆半径            |
| `x-axis-rotation` | 椭圆 x 轴旋转角度   |
| `large-arc-flag`  | 0 短弧 / 1 长弧     |
| `sweep-flag`      | 0 逆时针 / 1 顺时针 |
| `x,y`             | 终点                |

### 四种弧组合

```html
<svg viewBox="0 0 400 200">
  <!-- 从 (50,100) 到 (150,100),半径 50 -->
  <path d="M 50 100 A 50 50 0 0 0 150 100" fill="none" stroke="#4f5bd5" />
  <path d="M 250 100 A 50 50 0 0 1 350 100" fill="none" stroke="#00b894" />
  <path d="M 50 50 A 50 50 0 1 0 150 50" fill="none" stroke="#d63031" />
  <path d="M 250 50 A 50 50 0 1 1 350 50" fill="none" stroke="#f9a825" />
</svg>
```

### 圆弧扇形

**扇形路径**
`d="M <圆心x> <圆心y> L <起点x> <起点y> A <rx> <ry> <rot> <large> <sweep> <终点x> <终点y> Z"`
```html
<svg viewBox="0 0 200 200">
  <path d="M 100 100 L 100 20 A 80 80 0 0 1 180 100 Z" fill="#4f5bd5" />
</svg>
```

绘制 1/4 扇形:从圆心 (100,100) → (100,20) → 顺时针弧到 (180,100) → 闭合。

---

## 闭合路径 Z

**Z 闭合路径**
`d="... Z"`
```html
<!-- 不闭合:不画最后一条边 -->
<path d="M 10 10 L 100 10 L 100 50" fill="none" stroke="#000" />
<!-- 闭合:自动连接终点到起点 -->
<path d="M 10 10 L 100 10 L 100 50 Z" fill="#4f5bd5" />
```

> 闭合后 `fill` 才能正确填充内部。

---

## fill-rule 填充规则

### nonzero(默认)

**fill-rule="nonzero"**
```html
<path
  d="M 10 10 L 190 10 L 190 90 L 10 90 Z M 50 30 L 150 30 L 150 70 L 50 70 Z"
  fill="#4f5bd5"
  fill-rule="nonzero"
/>
```

外矩形 + 内矩形:nonzero 规则下内矩形被"挖空"(外顺时针 + 内逆时针 → 区域计数为 0)。

### evenodd

**fill-rule="evenodd"**
```html
<path
  d="M 10 10 L 190 10 L 190 90 L 10 90 Z M 50 30 L 150 30 L 150 70 L 50 70 Z"
  fill="#00b894"
  fill-rule="evenodd"
/>
```

evenodd 规则下,无论方向,奇数次穿越绘制,偶数次不绘制 → 形成环带效果。

### 五角星示例

```html
<!-- nonzero:中心填充 -->
<path
  d="M 100 10 L 120 70 L 180 70 L 130 105 L 150 165 L 100 130 L 50 165 L 70 105 L 20 70 L 80 70 Z"
  fill="#d63031"
  fill-rule="nonzero"
/>

<!-- evenodd:中心镂空 -->
<path
  d="M 100 10 L 120 70 L 180 70 L 130 105 L 150 165 L 100 130 L 50 165 L 70 105 L 20 70 L 80 70 Z"
  fill="#f9a825"
  fill-rule="evenodd"
/>
```

---

## 多子路径

**单个 path 包含多个 M**
`d="M <起点1> ... Z M <起点2> ... Z"`
```html
<!-- 两个独立三角形 -->
<path d="M 10 10 L 90 10 L 50 90 Z M 110 10 L 190 10 L 150 90 Z" fill="#4f5bd5" />
```

---

## pathLength 路径归一化

**pathLength 归一化路径长度**
`pathLength="<归一化长度>"`
```html
<path
  d="M 10 50 Q 100 10 190 50"
  fill="none"
  stroke="#4f5bd5"
  stroke-width="3"
  pathLength="100"
  stroke-dasharray="50 50"
/>
<!-- pathLength=100,dasharray 50 50 表示画一半留一半 -->
```

### JavaScript 路径测量 API
```javascript
const path = document.querySelector('path');
const length = path.getTotalLength();
console.log(length); // 例如 200
const point = path.getPointAtLength(100); // 路径中点坐标
```

---

## 综合示例:心形

**心形路径**
```html
<svg viewBox="0 0 100 100" width="200" height="200">
  <path
    d="M 50 30
       C 30 10 0 20 0 50
       C 0 70 30 90 50 100
       C 70 90 100 70 100 50
       C 100 20 70 10 50 30 Z"
    fill="#d63031"
  />
</svg>
```

路径解析:
- 起点 (50,30):心形顶部凹陷
- C 到 (0,50):左半弧
- C 到 (50,100):底部尖角
- C 到 (100,50):右半弧
- C 回 (50,30):闭合

<!-- ============ 文档分隔线：012-svg/006-SVGTextTypography.md ============ -->

## 1. 历史动机与发展脉络

### 1.1 文本渲染的演进

计算机文本渲染经历了多个阶段,SVG 文本是这一演进的集大成者:

| 时期 | 技术 | 渲染方式 | 关键贡献 |
| ---- | ---- | -------- | -------- |
| 1960s | 矢量字体 | 笔画命令序列 | 早期 CAD 文本 |
| 1982 | PostScript Type 1 | 三次贝塞尔轮廓 | 高质量印刷 |
| 1991 | TrueType | 二次贝塞尔轮廓 | Apple/Microsoft 标准 |
| 1996 | OpenType | 三次贝塞尔 + 高级特性 | 多语言支持 |
| 2001 | SVG 1.0 `<text>` | 路径 + 字体引用 | Web 矢量文本 |
| 2018 | SVG 2 + WOFF 2 | CSS 字体 + 字体子集 | Web 字体优化 |

### 1.2 SVG 文本的特殊性

SVG `<text>` 与 HTML `<p>` 的核心差异:

| 特性 | HTML 文本 | SVG 文本 |
| ---- | --------- | -------- |
| 布局 | 流式布局,自动换行 | 绝对坐标,无自动换行 |
| 字体 | CSS font-* 属性 | 同 CSS + SVG 专有 |
| 度量 | box model | 字体度量 + 基线 |
| 路径排版 | 不支持 | textPath |
| 选择 | 默认可选 | 需 `user-select: text` |
| 可访问性 | 语义化 | 需 `<title>`/ARIA |
| 国际化 | writing-mode | 同 CSS |
| 渲染 | DOM + 文本引擎 | 路径 + 字体引擎 |

SVG 文本"绝对坐标 + 无自动换行"的特征,使其更适合数据可视化标签、图标、装饰性文字,而非长篇内容。

### 1.3 字体度量系统的起源

字体度量(typographic metrics)源自金属活字时代(15 世纪古登堡),核心概念包括:

- **em square**:字体设计的基本方框,所有度量相对此归一化
- **baseline(基线)**:字母 sit 的水平线,如字母 "x" 的底部
- **ascender(上伸)**:小写字母上伸部分(如 "b"、"h")的顶部
- **descender(下伸)**:小写字母下伸部分(如 "g"、"y")的底部
- **cap height(大写高)**:大写字母顶部
- **x-height(x 高)**:小写字母 "x" 的高度
- **line height(行高)**:行间距,通常 = ascent + descent + leading

SVG 的 `dominant-baseline` 属性直接引用这些字体度量,如 `alphabetic`、`central`、`hanging`、`text-before-edge` 等。

### 1.4 设计哲学:文本即图形

SVG 文本的设计哲学可概括为"文本即图形":

- **统一渲染**:文本与图形使用相同的渲染管线(路径 + 填充)
- **坐标控制**:文本位置由精确坐标决定,而非布局引擎
- **路径集成**:文本可沿任意路径排版(textPath)
- **样式继承**:文本属性与其他 SVG 元素一致,支持 CSS

这一设计让 SVG 文本既能作为内容载体(可访问、可选),也能作为视觉元素(任意变换、填充、描边)。

## 2. 形式化定义

### 2.1 文本元素的形式化模型

SVG 文本元素可形式化为一个嵌套结构:

$$
\text{Text} = \langle L, S, G \rangle
$$

其中:

- $L = \{x, y, dx, dy, rotate, textLength, lengthAdjust\}$ 是布局属性
- $S = \{font-family, font-size, font-weight, font-style, fill, stroke, ...\}$ 是样式属性
- $G$ 是字形(glyph)序列,$G = (g_1, g_2, \ldots, g_n)$,每个字形 $g_i$ 由字体中的路径数据定义

### 2.2 字体度量的数学模型

字体的度量可表示为一个度量元组 $M$:

$$
M = \langle u_{em}, a_{sc}, d_{esc}, c_{ap}, x_h, l_{ine} \rangle
$$

- $u_{em}$:em 单位(通常 1000 或 2048)
- $a_{sc}$:ascender(基线上方高度)
- $d_{esc}$:descender(基线下方深度,通常为负数)
- $c_{ap}$:cap height(大写字母高度)
- $x_h$:x-height(小写字母高度)
- $l_{ine}$:line height(行高)

实际像素值由 font-size 缩放:$a_{sc,px} = a_{sc} \cdot \frac{font-size}{u_{em}}$。

### 2.3 text-anchor 的几何定义

`text-anchor` 定义文本水平锚点。设文本宽度为 $W$(由字形度量累加得到),锚点 $x_a$ 为 `x` 属性值:

- `start`:$x_{\text{start}} = x_a$,文本从 $x_a$ 向右延伸
- `middle`:$x_{\text{start}} = x_a - W/2$,文本居中
- `end`:$x_{\text{start}} = x_a - W$,文本从 $x_a$ 向左延伸

形式化:

$$
x_{\text{start}} = \begin{cases}
x_a & \text{if text-anchor=start} \\
x_a - W/2 & \text{if text-anchor=middle} \\
x_a - W & \text{if text-anchor=end}
\end{cases}
$$

### 2.4 dominant-baseline 的度量基线

`dominant-baseline` 定义文本垂直基线。设基线 $y_b$ 相对于 `y` 属性的偏移为 $\Delta y$:

| 值 | 基线类型 | $\Delta y$ |
| -- | -------- | ---------- |
| `alphabetic` | 字母基线(默认) | 0 |
| `middle` | 字体中线 | $-(a_{sc} + d_{esc})/2$ |
| `central` | 几何中心 | $-x_h/2$ |
| `hanging` | 悬挂线(天城文等) | $-a_{sc}$ |
| `text-top` | 文本顶部 | $-a_{sc}$ |
| `text-bottom` | 文本底部 | $-d_{esc}$ |

这些基线对应不同书写系统的传统参考线。

### 2.5 textPath 的弧长参数化

`<textPath>` 沿路径排列文字,核心是将字符位置映射到路径弧长。设路径 $C(s)$ 由弧长 $s \in [0, L]$ 参数化($L$ 为路径总长),字符 $i$ 的位置 $s_i$ 由 `startOffset` 与字符宽度累加得到:

$$
s_i = s_{\text{start}} + \sum_{j=0}^{i-1} w_j
$$

其中 $s_{\text{start}}$ 是 `startOffset` 转换为弧长,$w_j$ 是字符 $j$ 的 advance width。

### 2.6 writing-mode 与方向性

`writing-mode` 控制文本方向,支持的水平与垂直模式:

| 值 | 方向 | 应用场景 |
| -- | ---- | -------- |
| `horizontal-tb`(默认) | 水平,从上到下 | 拉丁文、中文 |
| `vertical-rl` | 垂直,从右到左 | 传统日文、中文古籍 |
| `vertical-lr` | 垂直,从左到右 | 蒙古文 |

文本方向还包括 `direction`(ltr/rtl)与 `unicode-bidi`,用于处理阿拉伯文、希伯来文等 RTL 语言。

## 3. 理论推导与原理解析

### 3.1 字形选择与 Unicode 映射

文本渲染的第一步是将 Unicode 码点映射到字形。设码点 $c$ 与字体 $F$,字形索引 $g$ 通过 cmap 表查找:

$$
g = \text{cmap}_F(c)
$$

若 $F$ 不包含 $c$ 的字形($\text{cmap}_F(c) = \text{undefined}$),浏览器回退到下一个字体,直到找到或显示 `.notdef`(豆腐块 □)。

字体回退算法:

```
function getGlyph(codepoint, fontStack):
    for font in fontStack:
        if font.has(codepoint):
            return font.get(codepoint)
    return NOTDEF_GLYPH
```

这就是为何 SVG `<text>` 中 `font-family: 'CustomFont', sans-serif` 列表很重要:确保 fallback 字体能覆盖 CustomFont 缺失的字符。

### 3.2 字符宽度与 advance width

每个字形在字体中有 `advance width` 属性,表示渲染后字符的 advance 距离(下一字符起始位置)。设字形 $g$ 的 advance width 为 $w(g)$,文本宽度为:

$$
W_{\text{text}} = \sum_{i=1}^{n} w(g_i) + \text{kerning adjustments}
$$

字距调整(kerning)是特定字符对的间距修正,如 "AV"、"To" 等组合通常减少间距以视觉平衡。OpenType 还支持 `liga`(连字)、`calt`(上下文替代)等特性。

### 3.3 文本边界框的计算

文本的边界框(bounding box)由字形路径决定:

$$
\text{bbox}(\text{Text}) = \bigcup_{i=1}^{n} \text{bbox}(g_i) + \text{position}(g_i)
$$

注意边界框包含 descender(如 "g"、"y" 的下伸部分),实际高度可能超过 font-size。

JavaScript 获取精确边界框:

```javascript
const text = document.querySelector('text');
const bbox = text.getBBox();
console.log(bbox);
// { x, y, width, height }
```

### 3.4 textPath 的几何变换

textPath 将字符放置在路径上,需要为每个字符应用:

1. **平移**:字符锚点到路径上对应弧长位置
2. **旋转**:字符基线对齐路径切线方向
3. **缩放**:可选,根据路径曲率调整字符大小

设路径在弧长 $s$ 处的点为 $P(s)$,切线方向为 $\theta(s)$,字符 $i$ 的变换矩阵:

$$
M_i = T(P(s_i)) \cdot R(\theta(s_i))
$$

字符 $i$ 的本地坐标系原点在 $P(s_i)$,x 轴沿路径切线方向。

### 3.5 字体子集化与文件大小

SVG 引用的字体文件通常很大(中文字体可达 10MB+)。字体子集化只保留实际使用的字形:

$$
\text{size}_{\text{subset}} \approx \text{size}_{\text{glyph}} \cdot |\text{used glyphs}|
$$

常用工具:

- **fonttools**(Python):`pyftsubset` 命令行
- **glyphhanger**(Node.js):基于浏览器使用情况
- **subfont**:自动分析 HTML/SVG,生成子集字体

子集化可将 5MB 中文字体降至 100KB 以内,大幅提升加载性能。

### 3.6 SVG 文本的可访问性

SVG 文本的可访问性涉及多个层面:

1. **语义化**:`<title>`、`<desc>` 提供图表标题与描述
2. **ARIA**:`role="img"`、`aria-label`、`aria-labelledby`
3. **可选择性**:`user-select: text` 让用户可选中文本
4. **对比度**:`fill` 颜色需满足 WCAG AA/AAA 对比度
5. **动态字体**:`font-size` 用 `rem`/`em` 跟随用户设置

形式化可访问性检查:

$$
\text{accessible}(\text{Text}) = \text{hasTitle} \land \text{hasLabel} \land \text{sufficientContrast} \land \text{selectable}
$$

### 3.7 RTL 与双向文本

阿拉伯文、希伯来文等 RTL 语言的文本方向由 Unicode Bidirectional Algorithm(bidi)处理。设文本序列为 $T = (c_1, c_2, \ldots, c_n)$,bidi 算法:

1. **分段**:将文本按方向分为 LTR 与 RTL 段
2. **排序**:RTL 段反向,但数字保持 LTR
3. **镜像**:某些字符(如括号)在 RTL 中镜像

SVG 中通过 `direction="rtl"` 与 `unicode-bidi="embed"` 控制:

```html
<text direction="rtl" unicode-bidi="embed">مرحبا بالعالم</text>
```

### 3.8 多行文本的实现策略

SVG `<text>` 不支持自动换行,实现多行文本有几种策略:

1. **多个 `<text>`**:每行独立 `<text>`,通过 `y` 控制行距
2. **`<tspan>` + `dy`**:同一 `<text>` 内用 `<tspan>` 换行
3. **`<text>` + `white-space: pre`**(SVG 2):支持自动换行
4. **`<foreignObject>`**:嵌入 HTML `<div>` 实现复杂布局

形式化策略选择:

$$
\text{strategy} = \begin{cases}
\text{multiple text} & \text{if few lines, static} \\
\text{tspan + dy} & \text{if related lines, dynamic} \\
\text{foreignObject} & \text{if complex layout, HTML needed}
\end{cases}
$$

## 4. 代码示例

### 4.1 text 基础

`<text>` 在指定坐标绘制文本。

```html
<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="50" font-size="24" fill="#4f5bd5">Hello SVG</text>
</svg>
```

#### 4.1.1 关键属性

| 属性 | 说明 | 默认值 |
| ---- | ---- | ------ |
| `x` / `y` | 基线起点坐标 | 0 |
| `font-family` | 字体族 | sans-serif |
| `font-size` | 字号 | medium |
| `font-weight` | 字重 | normal |
| `font-style` | 字体样式 | normal |
| `fill` | 文字颜色 | black |
| `text-anchor` | 水平对齐 | start |
| `dominant-baseline` | 垂直对齐 | alphabetic |
| `letter-spacing` | 字距 | normal |
| `text-decoration` | 下划线等 | none |

#### 4.1.2 y 是基线而非顶部

```html
<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="50" x2="300" y2="50" stroke="#ccc" />
  <text x="20" y="50" font-size="24" fill="#4f5bd5">基线在 y=50</text>
</svg>
```

文字的基线对齐 y=50,字符主体在基线之上,下伸部分(如 g、y)在基线之下。

### 4.2 text-anchor 水平对齐

```html
<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
  <line x1="150" y1="0" x2="150" y2="150" stroke="#ccc" />
  <text x="150" y="40" text-anchor="start" font-size="20">start</text>
  <text x="150" y="80" text-anchor="middle" font-size="20">middle</text>
  <text x="150" y="120" text-anchor="end" font-size="20">end</text>
</svg>
```

| 值 | 对齐方式 |
| -- | -------- |
| `start` | 左对齐(默认) |
| `middle` | 居中 |
| `end` | 右对齐 |

### 4.3 dominant-baseline 垂直对齐

```html
<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="75" x2="300" y2="75" stroke="#ccc" />
  <text x="50" y="75" dominant-baseline="alphabetic" font-size="16">alphabetic</text>
  <text x="150" y="75" dominant-baseline="middle" font-size="16">middle</text>
  <text x="250" y="75" dominant-baseline="hanging" font-size="16">hanging</text>
</svg>
```

| 值 | 含义 |
| -- | ---- |
| `alphabetic` | 字母基线(默认) |
| `middle` | 字符垂直中线 |
| `hanging` | 顶部悬挂线(适合天城文等) |
| `text-top` | 文本顶部 |
| `text-bottom` | 文本底部 |
| `central` | 几何中心 |

### 4.4 tspan 子文本

`<tspan>` 类似 HTML 的 `<span>`,可在同一 `<text>` 内切换样式或换行。

#### 4.4.1 局部样式

```html
<svg viewBox="0 0 300 60" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="40" font-size="24">
    <tspan fill="#4f5bd5">蓝色</tspan>
    <tspan fill="#d63031">红色</tspan>
    <tspan font-weight="bold" fill="#00b894">绿色粗体</tspan>
  </text>
</svg>
```

#### 4.4.2 相对位置

```html
<text x="20" y="40" font-size="20">
  <tspan>FANDEX</tspan>
  <tspan dx="10" dy="0" fill="#4f5bd5">-Web</tspan>
  <tspan x="20" dy="30">换行到第二行</tspan>
</text>
```

- `dx` / `dy`:相对前一字符的偏移
- `x` / `y`:绝对坐标(用于强制换行)

#### 4.4.3 字距控制

```html
<text x="20" y="40" font-size="20" letter-spacing="4">字距加宽</text>
<text x="20" y="80" font-size="20" letter-spacing="-1">字距收紧</text>
```

### 4.5 textPath 沿路径排版

`<textPath>` 让文字沿任意路径排列,常用于环形文字、波浪标语。

```html
<svg viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <path id="curve" d="M 20 100 Q 150 20 280 100" />
  </defs>
  <use href="#curve" fill="none" stroke="#ccc" />
  <text font-size="18" fill="#4f5bd5">
    <textPath href="#curve" startOffset="0">沿曲线排列的 SVG 文字示例</textPath>
  </text>
</svg>
```

#### 4.5.1 startOffset 起始位置

```html
<textPath href="#curve" startOffset="50%" text-anchor="middle"> 居中显示 </textPath>
```

| 值 | 含义 |
| -- | ---- |
| `0` | 从路径起点 |
| `50%` | 路径中点 |
| `100%` | 路径终点 |

#### 4.5.2 环形文字

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <path id="circle" d="M 100 100 m -75 0 a 75 75 0 1 1 150 0 a 75 75 0 1 1 -150 0" />
  </defs>
  <text font-size="14" fill="#4f5bd5">
    <textPath href="#circle" startOffset="0">围绕圆形排列的文字 · 围绕圆形排列的文字 ·</textPath>
  </text>
</svg>
```

#### 4.5.3 沿路径的方向计算

```javascript
function placeTextOnPath(pathElement, text, startOffset = 0) {
  const totalLength = pathElement.getTotalLength();
  const chars = text.split('');
  let currentOffset = startOffset;

  return chars.map((char) => {
    const point = pathElement.getPointAtLength(currentOffset);
    // 计算切线方向(下一与上一点的差)
    const next = pathElement.getPointAtLength(Math.min(currentOffset + 1, totalLength));
    const angle = Math.atan2(next.y - point.y, next.x - point.x) * (180 / Math.PI);

    const tsp = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
    tsp.textContent = char;
    tsp.setAttribute('x', point.x);
    tsp.setAttribute('y', point.y);
    tsp.setAttribute('transform', `rotate(${angle} ${point.x} ${point.y})`);

    // 估算字符宽度(简化版)
    currentOffset += 8;
    return tsp;
  });
}
```

### 4.6 writing-mode 竖排文字

```html
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <text x="50" y="20" font-size="20" writing-mode="tb">竖排文字</text>
</svg>
```

`writing-mode="tb"`(top-to-bottom)让文字垂直排列,适合中日韩排版。

更现代的写法使用 CSS:

```html
<text x="50" y="20" font-size="20" style="writing-mode: vertical-rl;">竖排文字</text>
```

### 4.7 字体加载与回退

SVG 中的字体遵循 CSS 字体规则,可用 `@font-face` 加载自定义字体。

```html
<svg viewBox="0 0 400 100" xmlns="http://www.w3.org/2000/svg">
  <style>
    @font-face {
      font-family: 'CustomFont';
      src: url('font.woff2') format('woff2');
    }
    text {
      font-family: 'CustomFont', 'PingFang SC', 'Microsoft YaHei', sans-serif;
    }
  </style>
  <text x="20" y="60" font-size="32">自定义字体</text>
</svg>
```

> 独立 .svg 文件中 `<style>` 内的 `@font-face` 仅在 `<object>` / `<iframe>` 嵌入时生效;内联 SVG 中可直接使用主页面的字体规则。

#### 4.7.1 字体加载策略

```css
/* WOFF 2 优先(压缩率高),回退到 WOFF/TTF */
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2'),
       url('font.woff') format('woff'),
       url('font.ttf') format('truetype');
  font-display: swap; /* 加载前用 fallback,加载后切换 */
}
```

### 4.8 文本描边与填充

```html
<svg viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
  <!-- 描边文字 -->
  <text x="20" y="40" font-size="32" fill="none" stroke="#4f5bd5" stroke-width="1.5">描边文字</text>
  <!-- 双层:先描边后填充 -->
  <text
    x="20"
    y="90"
    font-size="32"
    stroke="#fff"
    stroke-width="6"
    fill="#4f5bd5"
    paint-order="stroke fill"
  >
    描边填充
  </text>
  <!-- 渐变文字 -->
  <defs>
    <linearGradient id="text-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <text x="20" y="140" font-size="32" fill="url(#text-grad)">渐变文字</text>
</svg>
```

#### 4.8.1 paint-order 顺序

| 值 | 含义 |
| -- | ---- |
| `fill stroke` | 先填充后描边(默认) |
| `stroke fill` | 先描边后填充(描边在下) |
| `fill stroke markers` | 完整顺序 |

> `stroke fill` 让描边在填充下方,避免粗描边遮挡文字主体,是描边文字的常用技巧。

### 4.9 可访问文本

为屏幕阅读器提供语义化文本结构。

```html
<svg viewBox="0 0 300 100" role="img" aria-labelledby="chart-title" xmlns="http://www.w3.org/2000/svg">
  <title id="chart-title">2024 Q1 销售额柱状图</title>
  <desc id="chart-desc">柱状图显示 2024 年第一季度销售额:Q1 120 万、Q2 165 万、Q3 210 万</desc>
  <text x="150" y="50" text-anchor="middle" font-size="20" aria-hidden="true">销售额柱状图</text>
</svg>
```

- `<title>`:屏幕阅读器读取的主标题
- `<desc>`:详细描述(可选)
- `aria-hidden="true"`:装饰性文字避免重复朗读

### 4.10 实战:带数据标签的图表

```html
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <!-- 坐标轴 -->
  <line x1="40" y1="160" x2="380" y2="160" stroke="#333" />
  <line x1="40" y1="20" x2="40" y2="160" stroke="#333" />
  <!-- 柱子与数据标签 -->
  <g font-family="sans-serif">
    <rect x="80" y="80" width="40" height="80" fill="#4f5bd5" />
    <text x="100" y="70" text-anchor="middle" font-size="14" fill="#333">120</text>
    <text x="100" y="180" text-anchor="middle" font-size="12" fill="#666">Q1</text>

    <rect x="160" y="50" width="40" height="110" fill="#00b894" />
    <text x="180" y="40" text-anchor="middle" font-size="14" fill="#333">165</text>
    <text x="180" y="180" text-anchor="middle" font-size="12" fill="#666">Q2</text>

    <rect x="240" y="20" width="40" height="140" fill="#d63031" />
    <text x="260" y="10" text-anchor="middle" font-size="14" fill="#333">210</text>
    <text x="260" y="180" text-anchor="middle" font-size="12" fill="#666">Q3</text>
  </g>
</svg>
```

### 4.11 多语言支持

```html
<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
  <!-- 中文 -->
  <text x="20" y="40" font-size="20" font-family="'PingFang SC', 'Microsoft YaHei', sans-serif">
    你好世界
  </text>

  <!-- 英文 -->
  <text x="20" y="80" font-size="20" font-family="'Helvetica', 'Arial', sans-serif">
    Hello World
  </text>

  <!-- 日文 -->
  <text x="20" y="120" font-size="20" font-family="'Hiragino Sans', 'Yu Gothic', sans-serif">
    こんにちは世界
  </text>

  <!-- 阿拉伯文(RTL) -->
  <text
    x="380"
    y="160"
    font-size="20"
    direction="rtl"
    unicode-bidi="embed"
    text-anchor="end"
    font-family="'Noto Naskh Arabic', sans-serif"
  >
    مرحبا بالعالم
  </text>
</svg>
```

### 4.12 动态文本测量

```javascript
function measureSvgText(text, fontOptions = {}) {
  const {
    fontFamily = 'sans-serif',
    fontSize = 16,
    fontWeight = 'normal',
    fontStyle = 'normal',
  } = fontOptions;

  // 创建临时 SVG 与 text 元素
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('width', '0');
  svg.setAttribute('height', '0');
  svg.style.position = 'absolute';
  svg.style.visibility = 'hidden';

  const textEl = document.createElementNS('http://www.w3.org/2000/svg', 'text');
  textEl.setAttribute('font-family', fontFamily);
  textEl.setAttribute('font-size', fontSize);
  textEl.setAttribute('font-weight', fontWeight);
  textEl.setAttribute('font-style', fontStyle);
  textEl.textContent = text;

  svg.appendChild(textEl);
  document.body.appendChild(svg);

  const bbox = textEl.getBBox();
  document.body.removeChild(svg);

  return { width: bbox.width, height: bbox.height };
}

// 使用示例
const m = measureSvgText('Hello SVG', { fontSize: 24, fontFamily: 'serif' });
console.log(m); // { width: 90.3, height: 28.5 }
```

## 5. 对比分析

### 5.1 SVG text vs HTML text

| 特性 | SVG `<text>` | HTML `<p>` |
| ---- | ------------ | ---------- |
| 布局 | 绝对坐标 | 流式 |
| 自动换行 | 不支持(SVG 2 部分) | 默认 |
| 选择 | `user-select: text` | 默认可选 |
| 字体 | CSS font-* | 同 SVG |
| textPath | 支持 | 不支持 |
| 国际化 | writing-mode | 同 CSS |
| 性能 | 复杂文本较慢 | 优化 |
| 适用场景 | 标签、装饰 | 长内容 |

### 5.2 SVG text vs Canvas text

| 特性 | SVG `<text>` | Canvas `fillText` |
| ---- | ------------ | ------------------ |
| 渲染方式 | DOM + 字体引擎 | 位图绘制 |
| 可访问性 | 良好(可选、朗读) | 差(像素,无语义) |
| 缩放 | 矢量,无失真 | 像素,需重绘 |
| 文本测量 | `getBBox()` | `measureText()` |
| 选择 | 可选 | 不可选 |
| 性能 | 复杂文本较慢 | 快 |
| 国际化 | 完整支持 | 部分支持 |
| 适用场景 | 简单文本、可访问性优先 | 复杂动画、性能优先 |

### 5.3 text-anchor vs CSS text-align

| 特性 | SVG text-anchor | CSS text-align |
| ---- | --------------- | -------------- |
| 应用对象 | SVG `<text>` | HTML 块级元素 |
| 参考点 | `x` 属性 | 容器边界 |
| RTL 适配 | `start`/`end` 自动适配 | `start`/`end` 自动适配 |
| 动态计算 | 浏览器自动 | 浏览器自动 |

### 5.4 dominant-baseline vs CSS vertical-align

| 特性 | SVG dominant-baseline | CSS vertical-align |
| ---- | --------------------- | ------------------- |
| 参考点 | 字体度量基线 | 行高基线 |
| 精度 | 高(精确度量) | 中(行高近似) |
| 选项 | alphabetic、middle、central、hanging 等 | top、middle、bottom、baseline、sub、super |
| 应用场景 | SVG 文本对齐 | HTML 行内元素对齐 |

## 6. 常见陷阱与最佳实践

### 6.1 y 是基线而非顶部

```html
<!-- 错误:以为 y=50 是文字顶部,实际是基线 -->
<text x="20" y="50" font-size="24">Hello</text>
<!-- 文字主体在 y=50 之上,descender 部分在 y=50 之下 -->

<!-- 正确:计算文字顶部需考虑 ascent -->
<text x="20" y="50" font-size="24" dominant-baseline="hanging">Hello</text>
<!-- 现在 y=50 是文字顶部 -->
```

### 6.2 忘记设置 font-family

```html
<!-- 错误:依赖浏览器默认字体,跨平台不一致 -->
<text x="20" y="50">Hello</text>

<!-- 正确:声明完整字体回退栈 -->
<text x="20" y="50" font-family="'Inter', 'Helvetica Neue', sans-serif">Hello</text>
```

### 6.3 字体未加载就渲染

```html
<!-- 错误:字体加载前显示 fallback,加载后跳动 -->
<style>
  @font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2');
  }
  text { font-family: 'CustomFont', sans-serif; }
</style>
<text>自定义字体</text>

<!-- 改进:font-display: swap 显式控制 -->
<style>
  @font-face {
    font-family: 'CustomFont';
    src: url('font.woff2') format('woff2');
    font-display: swap;
  }
</style>
```

### 6.4 中文字体文件过大

```html
<!-- 错误:加载完整中文字体(5MB+) -->
<style>
  @font-face {
    font-family: 'SourceHanSans';
    src: url('source-han-sans.woff2') format('woff2');
  }
</style>

<!-- 改进:字体子集化,仅保留使用字符 -->
<style>
  @font-face {
    font-family: 'SourceHanSans-Subset';
    src: url('source-han-sans.subset.woff2') format('woff2');
    /* 文件大小从 5MB 降至 100KB */
  }
</style>
```

### 6.5 textPath 字符溢出路径

```html
<!-- 错误:文字过长,超出路径长度后字符消失 -->
<textPath href="#short-path">这是一段很长的文字,超出了路径长度</textPath>

<!-- 改进:缩短文字或延长路径 -->
<textPath href="#long-path">这是一段很长的文字,现在路径足够长</textPath>
```

### 6.6 dominant-baseline 跨浏览器不一致

```html
<!-- 问题:不同浏览器对 dominant-baseline 实现略有差异 -->
<text dominant-baseline="middle">Hello</text>
<!-- Chrome 与 Firefox 渲染位置可能差几像素 -->

<!-- 改进:用 dy 显式偏移 -->
<text dy="0.35em">Hello</text>
<!-- dy="0.35em" 等价于 middle,跨浏览器更一致 -->
```

### 6.7 装饰性文字未加 aria-hidden

```html
<!-- 错误:装饰性文字被屏幕阅读器朗读,干扰内容 -->
<text> 装饰 </text>

<!-- 改进:加 aria-hidden 避免朗读 -->
<text aria-hidden="true"> 装饰 </text>
```

### 6.8 SVG 文本无法选中

```html
<!-- 默认:SVG 文本不可选 -->
<text>Hello</text>

<!-- 启用选择 -->
<text style="user-select: text;">Hello</text>
```

## 7. 工程实践

### 7.1 Vue 3 SVG 文本组件

```vue
<template>
  <svg :viewBox="`0 0 ${width} ${height}`" xmlns="http://www.w3.org/2000/svg">
    <text
      :x="x"
      :y="y"
      :text-anchor="anchor"
      :dominant-baseline="baseline"
      :font-family="fontFamily"
      :font-size="fontSize"
      :font-weight="fontWeight"
      :fill="color"
      :aria-hidden="decorative ? 'true' : undefined"
    >
      {{ content }}
    </text>
  </svg>
</template>

<script setup>
defineProps({
  content: { type: String, required: true },
  x: { type: [Number, String], default: 0 },
  y: { type: [Number, String], default: 0 },
  width: { type: [Number, String], default: 200 },
  height: { type: [Number, String], default: 50 },
  anchor: { type: String, default: 'start' },
  baseline: { type: String, default: 'alphabetic' },
  fontFamily: { type: String, default: "'Inter', sans-serif" },
  fontSize: { type: [Number, String], default: 16 },
  fontWeight: { type: [Number, String], default: 'normal' },
  color: { type: String, default: '#333' },
  decorative: { type: Boolean, default: false },
});
</script>
```

### 7.2 React SVG 文本组件

```jsx
import { memo } from 'react';

const SVGText = memo(function SVGText({
  content,
  x = 0,
  y = 0,
  width = 200,
  height = 50,
  anchor = 'start',
  baseline = 'alphabetic',
  fontFamily = "'Inter', sans-serif",
  fontSize = 16,
  fontWeight = 'normal',
  color = '#333',
  decorative = false,
  title,
  desc,
}) {
  return (
    <svg viewBox={`0 0 ${width} ${height}`} xmlns="http://www.w3.org/2000/svg"
      role={title ? 'img' : undefined}
      aria-labelledby={title ? 'text-title' : undefined}>
      {title && <title id="text-title">{title}</title>}
      {desc && <desc>{desc}</desc>}
      <text
        x={x}
        y={y}
        text-anchor={anchor}
        dominant-baseline={baseline}
        font-family={fontFamily}
        font-size={fontSize}
        font-weight={fontWeight}
        fill={color}
        aria-hidden={decorative ? 'true' : undefined}
      >
        {content}
      </text>
    </svg>
  );
});

export default SVGText;
```

### 7.3 字体子集化工具

```javascript
// scripts/subset-font.mjs
import { subsetFont } from 'fonttools';
import { readFileSync, writeFileSync } from 'node:fs';

const inputFont = 'fonts/SourceHanSansSC-Regular.otf';
const outputFont = 'public/fonts/subset.woff2';

// 收集所有 SVG 中使用的字符
import { readdirSync } from 'node:fs';
import { join } from 'node:path';

const SVG_DIR = 'src/assets';
const chars = new Set();

const files = readdirSync(SVG_DIR).filter((f) => f.endsWith('.svg'));
for (const file of files) {
  const content = readFileSync(join(SVG_DIR, file), 'utf8');
  // 提取 <text> 标签内容
  const matches = content.match(/<text[^>]*>([^<]+)<\/text>/g);
  if (matches) {
    for (const match of matches) {
      const text = match.replace(/<\/?text[^>]*>/g, '');
      for (const char of text) {
        chars.add(char);
      }
    }
  }
}

// 子集化
const charsArray = Array.from(chars).join('');
const buffer = readFileSync(inputFont);
const subsetBuffer = subsetFont(buffer, {
  text: charsArray,
  formats: ['woff2'],
});

writeFileSync(outputFont, subsetBuffer);
console.log(`Subset created with ${charsArray.length} chars: ${charsArray}`);
```

### 7.4 多行文本组件

```javascript
class MultiLineText {
  constructor(svg, options = {}) {
    this.svg = svg;
    this.options = {
      lineHeight: 1.2,
      fontFamily: 'sans-serif',
      fontSize: 16,
      fill: '#333',
      ...options,
    };
  }

  render(x, y, lines) {
    const { fontSize, lineHeight } = this.options;
    const lineHeightPx = fontSize * lineHeight;

    const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    text.setAttribute('x', x);
    text.setAttribute('y', y);
    text.setAttribute('font-family', this.options.fontFamily);
    text.setAttribute('font-size', fontSize);
    text.setAttribute('fill', this.options.fill);

    lines.forEach((line, i) => {
      const tspan = document.createElementNS('http://www.w3.org/2000/svg', 'tspan');
      tspan.setAttribute('x', x);
      tspan.setAttribute('dy', i === 0 ? 0 : lineHeightPx);
      tspan.textContent = line;
      text.appendChild(tspan);
    });

    this.svg.appendChild(text);
    return text;
  }
}

// 使用
const mlt = new MultiLineText(document.querySelector('svg'), { fontSize: 14 });
mlt.render(10, 20, ['第一行', '第二行', '第三行']);
```

### 7.5 SVG 自动换行(SVG 2)

SVG 2 引入 `white-space` 属性,支持自动换行:

```html
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="20" font-size="14" style="white-space: pre-wrap; width: 180px;">
    这是一段长文本,会自动换行到下一行,无需手动拆分。
  </text>
</svg>
```

> 注意:浏览器支持有限,生产环境推荐用 `<foreignObject>` 或手动换行。

### 7.6 SVG 文本可访问性检查器

```javascript
function checkSVGTextAccessibility(svgRoot) {
  const issues = [];
  const texts = svgRoot.querySelectorAll('text');

  texts.forEach((text, i) => {
    const issues_text = [];

    // 检查 1:装饰性文本是否有 aria-hidden
    const content = text.textContent.trim();
    if (content && !text.getAttribute('aria-hidden')) {
      // 检查是否有 title/desc 父元素
      const parent = text.parentElement;
      const hasTitle = parent && parent.querySelector('title');
      if (!hasTitle) {
        // 文本可能既不是装饰也缺少可访问性标注
        // 这里只警告,不一定是问题
      }
    }

    // 检查 2:对比度
    const fill = window.getComputedStyle(text).fill;
    if (fill && isLowContrast(fill, '#fff')) {
      issues_text.push(`low contrast fill: ${fill}`);
    }

    // 检查 3:font-size 是否过小
    const fontSize = parseFloat(window.getComputedStyle(text).fontSize);
    if (fontSize < 12) {
      issues_text.push(`font-size too small: ${fontSize}px (< 12px)`);
    }

    // 检查 4:text-anchor 与位置是否匹配
    const x = parseFloat(text.getAttribute('x'));
    const anchor = text.getAttribute('text-anchor') || 'start';
    if (anchor === 'end' && x < 50) {
      issues_text.push(`end-anchored text near left edge (x=${x})`);
    }

    if (issues_text.length > 0) {
      issues.push({ index: i, content, issues: issues_text });
    }
  });

  return issues;
}

function isLowContrast(color1, color2) {
  const c1 = hexToRgb(color1);
  const c2 = hexToRgb(color2);
  if (!c1 || !c2) return false;
  const ratio = contrastRatio(c1, c2);
  return ratio < 4.5; // WCAG AA 标准
}

function hexToRgb(hex) {
  const m = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return m ? { r: parseInt(m[1], 16), g: parseInt(m[2], 16), b: parseInt(m[3], 16) } : null;
}

function contrastRatio(c1, c2) {
  const l1 = luminance(c1);
  const l2 = luminance(c2);
  return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
}

function luminance(c) {
  const { r, g, b } = c;
  const rs = r / 255;
  const gs = g / 255;
  const bs = b / 255;
  return 0.2126 * gamma(rs) + 0.7152 * gamma(gs) + 0.0722 * gamma(bs);
}

function gamma(c) {
  return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
}
```

## 8. 案例研究

### 8.1 案例一:D3.js 数据可视化

D3.js 大量使用 SVG `<text>` 绘制坐标轴、数据标签、图例:

```javascript
import * as d3 from 'd3';

const svg = d3.select('#chart').append('svg')
  .attr('viewBox', '0 0 800 400');

// 坐标轴
const xAxis = d3.axisBottom(xScale);
svg.append('g')
  .attr('transform', 'translate(0, 350)')
  .call(xAxis);

// 数据标签
svg.selectAll('.data-label')
  .data(dataset)
  .enter()
  .append('text')
  .attr('class', 'data-label')
  .attr('x', (d) => xScale(d.x))
  .attr('y', (d) => yScale(d.y) - 10)
  .attr('text-anchor', 'middle')
  .attr('font-size', 12)
  .attr('fill', '#333')
  .text((d) => d.value);

// 图例
const legend = svg.append('g')
  .attr('transform', 'translate(650, 30)');

['Series A', 'Series B', 'Series C'].forEach((label, i) => {
  legend.append('text')
    .attr('x', 20)
    .attr('y', i * 20)
    .attr('font-size', 12)
    .text(label);
});
```

### 8.2 案例二:Material Design 数据标签

Material Design 中 SVG 文本用于卡片、列表项的数据展示:

```xml
<svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="30" font-family="Roboto, sans-serif" font-size="12" fill="rgba(0,0,0,0.6)">
    Revenue
  </text>
  <text x="20" y="60" font-family="Roboto, sans-serif" font-size="24" font-weight="500" fill="rgba(0,0,0,0.87)">
    $12,345
  </text>
  <text x="20" y="80" font-family="Roboto, sans-serif" font-size="11" fill="#00b894">
    +12.5% ↑
  </text>
</svg>
```

### 8.3 案例三:Logo 文字

品牌 Logo 中的文字常使用 SVG 实现矢量缩放:

```xml
<svg viewBox="0 0 200 60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="logo-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <text
    x="100"
    y="40"
    text-anchor="middle"
    font-family="'Inter', sans-serif"
    font-size="32"
    font-weight="700"
    fill="url(#logo-grad)"
    letter-spacing="2"
  >
    FANDEX
  </text>
</svg>
```

### 8.4 案例四:环形徽章

```xml
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <path id="badge-circle" d="M 100 100 m -70 0 a 70 70 0 1 1 140 0 a 70 70 0 1 1 -140 0" />
  </defs>
  <circle cx="100" cy="100" r="90" fill="#4f5bd5" />
  <circle cx="100" cy="100" r="70" fill="#fff" />
  <text font-size="14" fill="#4f5bd5" font-weight="bold">
    <textPath href="#badge-circle" startOffset="0">
      FANDEX · PREMIUM · 2026 · FANDEX · PREMIUM · 2026 ·
    </textPath>
  </text>
  <text x="100" y="105" text-anchor="middle" font-size="32" font-weight="bold" fill="#4f5bd5">
    PRO
  </text>
</svg>
```

### 8.5 案例五:可访问图表

```xml
<svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">2024 年季度销售额对比</title>
  <desc id="desc">
    柱状图展示 2024 年三个季度销售额:Q1 120 万美元、Q2 165 万美元、Q3 210 万美元,呈增长趋势。
  </desc>

  <!-- 坐标轴 -->
  <line x1="40" y1="200" x2="380" y2="200" stroke="#333" />
  <line x1="40" y1="20" x2="40" y2="200" stroke="#333" />

  <!-- Y 轴标签 -->
  <g font-family="sans-serif" font-size="10" fill="#666" text-anchor="end">
    <text x="35" y="203">0</text>
    <text x="35" y="153">100</text>
    <text x="35" y="103">200</text>
    <text x="35" y="53">300</text>
  </g>

  <!-- 柱子 -->
  <g>
    <rect x="80" y="140" width="40" height="60" fill="#4f5bd5" />
    <rect x="160" y="117.5" width="40" height="82.5" fill="#00b894" />
    <rect x="240" y="95" width="40" height="105" fill="#d63031" />
  </g>

  <!-- 数据标签 -->
  <g font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">
    <text x="100" y="135">120</text>
    <text x="180" y="112">165</text>
    <text x="260" y="90">210</text>
  </g>

  <!-- X 轴标签 -->
  <g font-family="sans-serif" font-size="11" fill="#666" text-anchor="middle">
    <text x="100" y="220">Q1</text>
    <text x="180" y="220">Q2</text>
    <text x="260" y="220">Q3</text>
  </g>

  <!-- 单位 -->
  <text x="20" y="20" font-family="sans-serif" font-size="10" fill="#999">万美元</text>
</svg>
```

### 8.6 案例六:FANDEX 项目知识图谱节点

```html
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <g class="node" transform="translate(100, 100)">
    <circle r="40" fill="#4f5bd5" />
    <text text-anchor="middle" dominant-baseline="central" fill="#fff" font-size="14" font-weight="bold">
      HTML
    </text>
  </g>

  <g class="node" transform="translate(300, 200)">
    <rect x="-50" y="-20" width="100" height="40" rx="8" fill="#00b894" />
    <text text-anchor="middle" dominant-baseline="central" fill="#fff" font-size="14">
      JavaScript
    </text>
  </g>

  <g class="node" transform="translate(500, 300)">
    <rect x="-60" y="-25" width="120" height="50" rx="8" fill="#d63031" />
    <text text-anchor="middle" dominant-baseline="central" fill="#fff" font-size="16" font-weight="bold">
      TypeScript
    </text>
  </g>
</svg>
```

### 填空题知识点讲解

**题目 6**:SVG 中字体度量的基本单位是 ________,通常为 1000 或 2048。

**解析讲解**：`em square`(或 `em`)

**解析讲解**：字体设计的所有度量(ascender、descender、cap-height 等)都相对于 em square 归一化。font-size 决定 1 em 等于多少像素。

**题目 7**:`paint-order="stroke fill"` 的作用是 ________,常用于 ________。

**解析讲解**：`先描边后填充(描边在填充下方)`;`描边文字(避免粗描边遮挡文字主体)`

**解析讲解**：默认 `fill stroke` 是先填充后描边,粗描边会遮挡文字主体。改为 `stroke fill` 后,描边在填充下方,文字主体清晰可见。

**题目 8**:`<tspan>` 的 `dx`/`dy` 与 `x`/`y` 的区别是:前者是 ________,后者是 ________。

**解析讲解**：`相对偏移(相对前一字符)`;`绝对坐标`

**解析讲解**：`dx`/`dy` 是相对前一字符位置的偏移量,常用于字距调整;`x`/`y` 是绝对坐标,常用于强制换行或重置位置。

**题目 9**:SVG `<text>` 默认不支持自动换行,实现多行文本的常见策略包括:________、________、________。

**解析讲解**：`多个 <text> 元素`、`<tspan> + dy 换行`、`<foreignObject> 嵌入 HTML`

**解析讲解**：三种策略各有优劣:多个 `<text>` 适合静态少量行;`<tspan>` 适合同一文本内换行;`<foreignObject>` 适合复杂布局(支持 HTML/CSS)。SVG 2 引入 `white-space: pre-wrap` 但浏览器支持有限。

**题目 10**:字体子集化的作用是 ________,可将中文字体从 5MB 降至 ________。

**解析讲解**：`只保留实际使用的字形,减小文件大小`;`100KB 以内`

**解析讲解**：字体子集化通过分析 HTML/SVG 中实际使用的字符,生成仅包含这些字形的字体文件。对中文字体尤其有效,因为完整字体包含数万字形,而单页可能只用几百字。

### 编程题知识点讲解

**题目 11**:实现一个 SVG 文本组件,要求:

1. 支持 text-anchor 与 dominant-baseline 配置
2. 字体回退栈(中文 + 英文)
3. 可访问性(可选 aria-hidden 或 title/desc)
4. 多行文本(通过 tspan + dy)

```vue
<template>
  <text
    :x="x"
    :y="y"
    :text-anchor="anchor"
    :dominant-baseline="baseline"
    :font-family="fontStack"
    :font-size="size"
    :font-weight="weight"
    :fill="color"
    :letter-spacing="letterSpacing"
    :aria-hidden="decorative ? 'true' : undefined"
    :role="title ? 'img' : undefined"
    :aria-label="title || undefined"
  >
    <title v-if="title">{{ title }}</title>
    <desc v-if="desc">{{ desc }}</desc>
    <template v-if="Array.isArray(content)">
      <tspan
        v-for="(line, i) in content"
        :key="i"
        :x="x"
        :dy="i === 0 ? 0 : size * lineHeight"
      >{{ line }}</tspan>
    </template>
    <template v-else>{{ content }}</template>
  </text>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  content: { type: [String, Array], required: true },
  x: { type: [Number, String], default: 0 },
  y: { type: [Number, String], default: 0 },
  anchor: { type: String, default: 'start' },
  baseline: { type: String, default: 'alphabetic' },
  fontStack: {
    type: String,
    default: "'Inter', 'PingFang SC', 'Microsoft YaHei', sans-serif",
  },
  size: { type: [Number, String], default: 16 },
  weight: { type: [Number, String], default: 'normal' },
  color: { type: String, default: '#333' },
  letterSpacing: { type: [Number, String], default: 'normal' },
  lineHeight: { type: Number, default: 1.2 },
  decorative: { type: Boolean, default: false },
  title: { type: String, default: '' },
  desc: { type: String, default: '' },
});

// 计算 fontStack(可被覆盖)
const fontStack = computed(() => props.fontStack);
</script>
```

**评分标准**:

- text-anchor 与 dominant-baseline 支持(2 分)
- 字体回退栈(2 分)
- 可访问性配置(3 分)
- 多行文本支持(3 分)

**题目 12**:实现一个 textPath 文字组件,沿给定路径排列文字,要求:

1. 路径在 `<defs>` 中定义
2. 支持 startOffset(数值或百分比)
3. 支持 text-anchor
4. 文字溢出路径时给出警告

```javascript
class TextPathComponent {
  constructor(svg, pathD, options = {}) {
    this.svg = svg;
    this.options = {
      startOffset: 0,
      textAnchor: 'start',
      fontSize: 16,
      fill: '#333',
      fontFamily: 'sans-serif',
      ...options,
    };

    this.pathId = `textpath-${Math.random().toString(36).slice(2, 9)}`;
    this.setupDefs(pathD);
  }

  setupDefs(pathD) {
    const NS = 'http://www.w3.org/2000/svg';
    let defs = this.svg.querySelector('defs');
    if (!defs) {
      defs = document.createElementNS(NS, 'defs');
      this.svg.appendChild(defs);
    }
    const path = document.createElementNS(NS, 'path');
    path.setAttribute('id', this.pathId);
    path.setAttribute('d', pathD);
    path.setAttribute('fill', 'none');
    defs.appendChild(path);
    this.pathElement = path;
  }

  render(text) {
    const NS = 'http://www.w3.org/2000/svg';

    // 测量文本宽度
    const tempText = document.createElementNS(NS, 'text');
    tempText.setAttribute('font-size', this.options.fontSize);
    tempText.setAttribute('font-family', this.options.fontFamily);
    tempText.textContent = text;
    this.svg.appendChild(tempText);
    const textWidth = tempText.getBBox().width;
    this.svg.removeChild(tempText);

    // 检查路径长度
    const pathLength = this.pathElement.getTotalLength();
    if (textWidth > pathLength) {
      console.warn(
        `Text width ${textWidth}px exceeds path length ${pathLength}px; ` +
        `text will be clipped.`
      );
    }

    // 创建 textPath
    const textEl = document.createElementNS(NS, 'text');
    textEl.setAttribute('font-size', this.options.fontSize);
    textEl.setAttribute('font-family', this.options.fontFamily);
    textEl.setAttribute('fill', this.options.fill);
    textEl.setAttribute('text-anchor', this.options.textAnchor);

    const textPath = document.createElementNS(NS, 'textPath');
    textPath.setAttribute('href', `#${this.pathId}`);
    textPath.setAttribute('startOffset', this.options.startOffset);
    textPath.textContent = text;

    textEl.appendChild(textPath);
    this.svg.appendChild(textEl);
    return textEl;
  }
}

// 使用示例
const component = new TextPathComponent(
  document.querySelector('svg'),
  'M 20 100 Q 150 20 280 100',
  { startOffset: '50%', textAnchor: 'middle', fontSize: 18, fill: '#4f5bd5' }
);
component.render('沿曲线排列的文字');
```

**评分标准**:

- 路径在 defs 中定义(2 分)
- 支持 startOffset(2 分)
- 支持 text-anchor(2 分)
- 溢出检测与警告(4 分)

### 10.1 W3C 规范

1. W3C. 2018. **SVG 2 Specification: Text**. W3C Recommendation. https://www.w3.org/TR/SVG2/text.html

2. W3C. 2003. **SVG 1.1 Specification: Text**. W3C Recommendation. https://www.w3.org/TR/SVG11/text.html

3. W3C. 2023. **CSS Text Module Level 3**. W3C Working Draft. https://www.w3.org/TR/css-text-3/

4. W3C. 2023. **CSS Writing Modes Level 4**. W3C Working Draft. https://www.w3.org/TR/css-writing-modes-4/

5. W3C. 2021. **WOFF File Format 2.0**. W3C Recommendation. https://www.w3.org/TR/WOFF2/

6. W3C. 2023. **WCAG 2.2: Web Content Accessibility Guidelines**. W3C Recommendation. https://www.w3.org/TR/WCAG22/

### 10.2 学术论文

7. Knuth, D. E. 1986. **The METAFONTbook**. Addison-Wesley Professional, Reading, MA, USA.

8. Bringhurst, R. 2013. **The Elements of Typographic Style** (4th ed.). Hartley & Marks Publishers, Vancouver, BC, Canada.

9. Hosken, M. 2003. **OpenType Layout: A Developer's Perspective**. In *Proceedings of the 2003 International Conference on Digital Typography* (EPUB '03). Springer-Verlag, Berlin, Heidelberg, Germany, 75–88.

10. Haralambous, Y. and Mossé, B. 2018. **Computerized Typography and the Web**. In *Digital Typography*, R. P. Stanley (Ed.). Springer-Verlag, 45–67. https://doi.org/10.1007/978-3-319-90197-8_3

### 10.3 工程实践参考

11. Eisenberg, J. D. 2014. **SVG Essentials** (2nd ed.). O'Reilly Media, Sebastopol, CA, USA.

12. Bellamy-Royds, A., Eisenberg, J. D., and Ginger, D. 2017. **Using SVG with CSS3 and HTML5**. O'Reilly Media.

13. Bostock, M., Ogievetsky, V., and Heer, J. 2011. **D3: Data-Driven Documents**. *IEEE Transactions on Visualization and Computer Graphics* 17, 12, 2301–2309. https://doi.org/10.1109/TVCG.2011.185

### 11.1 字体设计

- **Knuth, D. E. The METAFONTbook**:字体设计算法基础
- **Bringhurst, R. The Elements of Typographic Style**:排版美学经典
- **Frutiger, A. Type Sign Symbol**:字体与符号设计哲学
- **OpenType Specification**:OpenType 高级特性(liga、calt、ss01)

### 11.2 国际化

- **W3C Internationalization (i18n)**:多语言 Web 文档
- **Unicode Standard**:Unicode 编码与双向算法
- **CSS Writing Modes**:vertical-rl、vertical-lr、RTL 支持
- **Google Noto Fonts**:全球语言字体覆盖项目

### 11.3 可访问性

- **W3C WAI-ARIA**:SVG 文本 ARIA 属性
- **WCAG 2.2 Guidelines**:对比度、可读性标准
- **Inclusive Design Patterns**:包容性设计模式
- **Deque axe DevTools**:可访问性自动化检测

### 11.4 性能优化

- **WOFF 2.0 Specification**:Brotli 压缩的字体格式
- **fonttools(pyftsubset)**:Python 字体子集化工具
- **glyphhanger**:Node.js 字体子集化工具
- **subfont**:自动字体子集化构建工具

### 11.5 进阶主题

- **Variable Fonts in SVG**:可变字体在 SVG 中的应用
- **Houdini CSS Paint API**:自定义文本渲染
- **WebGPU Text Rendering**:GPU 加速文本光栅化
- **HarfBuzz**:跨平台文本 shaping 引擎
- **Pango**:GNOME 项目的文本布局引擎

下一篇介绍 SVG 颜色与填充,包括线性渐变、径向渐变、图案、滤镜等高级填充技术,在文本基础上扩展视觉表现力。
## text 文本元素

**text 基础文本**
`<text x="<基线x>" y="<基线y>" [font-family="<字体族>"] [font-size="<字号>"] [font-weight="<字重>"] [font-style="<样式>"] [fill="<颜色>"] [text-anchor="<水平对齐>"] [dominant-baseline="<垂直对齐>"] [letter-spacing="<字距>"] [text-decoration="<装饰>"]><文本内容></text>`
```html
<svg viewBox="0 0 300 100">
  <text x="20" y="50" font-size="24" fill="#4f5bd5">Hello SVG</text>
</svg>
```

### text 关键属性

| 属性                | 说明         | 默认值     |
| ------------------- | ------------ | ---------- |
| `x` / `y`           | 基线起点坐标 | 0          |
| `font-family`       | 字体族       | sans-serif |
| `font-size`         | 字号         | medium     |
| `font-weight`       | 字重         | normal     |
| `font-style`        | 字体样式     | normal     |
| `fill`              | 文字颜色     | black      |
| `text-anchor`       | 水平对齐     | start      |
| `dominant-baseline` | 垂直对齐     | alphabetic |
| `letter-spacing`    | 字距         | normal     |
| `text-decoration`   | 下划线等     | none       |

### y 是基线而非顶部

**y 坐标对应基线**
```html
<svg viewBox="0 0 300 100">
  <line x1="0" y1="50" x2="300" y2="50" stroke="#ccc" />
  <text x="20" y="50" font-size="24" fill="#4f5bd5">基线在 y=50</text>
</svg>
```

文字的基线对齐 y=50,字符主体在基线之上,下伸部分(如 g、y)在基线之下。

---

## text-anchor 水平对齐

**text-anchor 水平对齐**
`text-anchor="<start | middle | end>"`
```html
<svg viewBox="0 0 300 150">
  <line x1="150" y1="0" x2="150" y2="150" stroke="#ccc" />
  <text x="150" y="40" text-anchor="start" font-size="20">start</text>
  <text x="150" y="80" text-anchor="middle" font-size="20">middle</text>
  <text x="150" y="120" text-anchor="end" font-size="20">end</text>
</svg>
```

| 值       | 对齐方式       |
| -------- | -------------- |
| `start`  | 左对齐(默认) |
| `middle` | 居中           |
| `end`    | 右对齐         |

---

## dominant-baseline 垂直对齐

**dominant-baseline 垂直对齐**
`dominant-baseline="<alphabetic | middle | hanging | text-top | text-bottom | central>"`
```html
<svg viewBox="0 0 300 150">
  <line x1="0" y1="75" x2="300" y2="75" stroke="#ccc" />
  <text x="50" y="75" dominant-baseline="alphabetic" font-size="16">alphabetic</text>
  <text x="150" y="75" dominant-baseline="middle" font-size="16">middle</text>
  <text x="250" y="75" dominant-baseline="hanging" font-size="16">hanging</text>
</svg>
```

| 值            | 含义                       |
| ------------- | -------------------------- |
| `alphabetic`  | 字母基线(默认)           |
| `middle`      | 字符垂直中线               |
| `hanging`     | 顶部悬挂线(适合天城文等) |
| `text-top`    | 文本顶部                   |
| `text-bottom` | 文本底部                   |
| `central`     | 几何中心                   |

---

## tspan 子文本

**tspan 局部样式**
`<tspan [fill="<颜色>"] [font-weight="<字重>"] [dx="<相对x偏移>"] [dy="<相对y偏移>"] [x="<绝对x>"] [y="<绝对y>"]><内容></tspan>`
```html
<svg viewBox="0 0 300 60">
  <text x="20" y="40" font-size="24">
    <tspan fill="#4f5bd5">蓝色</tspan>
    <tspan fill="#d63031">红色</tspan>
    <tspan font-weight="bold" fill="#00b894">绿色粗体</tspan>
  </text>
</svg>
```

### 相对位置

**tspan 相对位置与换行**
```html
<text x="20" y="40" font-size="20">
  <tspan>FANDEX</tspan>
  <tspan dx="10" dy="0" fill="#4f5bd5">-Web</tspan>
  <tspan x="20" dy="30">换行到第二行</tspan>
</text>
```

- `dx` / `dy`:相对前一字符的偏移
- `x` / `y`:绝对坐标(用于强制换行)

### 字距控制

**letter-spacing 字距**
`letter-spacing="<长度>"`
```html
<text x="20" y="40" font-size="20" letter-spacing="4">字距加宽</text>
<text x="20" y="80" font-size="20" letter-spacing="-1">字距收紧</text>
```

---

## textPath 沿路径排版

**textPath 沿路径排列文字**
`<textPath href="<#路径id>" [startOffset="<起始位置>"]><文本></textPath>`
```html
<svg viewBox="0 0 300 200">
  <defs>
    <path id="curve" d="M 20 100 Q 150 20 280 100" />
  </defs>
  <use href="#curve" fill="none" stroke="#ccc" />
  <text font-size="18" fill="#4f5bd5">
    <textPath href="#curve" startOffset="0">沿曲线排列的 SVG 文字示例</textPath>
  </text>
</svg>
```

### startOffset 起始位置

**startOffset 控制起始位置**
`startOffset="<0 | 50% | 100%>"`
```html
<textPath href="#curve" startOffset="50%" text-anchor="middle"> 居中显示 </textPath>
```

| 值     | 含义       |
| ------ | ---------- |
| `0`    | 从路径起点 |
| `50%`  | 路径中点   |
| `100%` | 路径终点   |

### 环形文字

**环形文字**
```html
<svg viewBox="0 0 200 200">
  <defs>
    <path id="circle" d="M 100 100 m -75 0 a 75 75 0 1 1 150 0 a 75 75 0 1 1 -150 0" />
  </defs>
  <text font-size="14" fill="#4f5bd5">
    <textPath href="#circle" startOffset="0">围绕圆形排列的文字 · 围绕圆形排列的文字 ·</textPath>
  </text>
</svg>
```

---

## writing-mode 竖排文字

**writing-mode 竖排文字**
`writing-mode="tb"`
```html
<svg viewBox="0 0 200 200">
  <text x="50" y="20" font-size="20" writing-mode="tb">竖排文字</text>
</svg>
```

`writing-mode="tb"`(top-to-bottom)让文字垂直排列,适合中日韩排版。

---

## 字体加载与回退

**@font-face 自定义字体**
```html
<svg viewBox="0 0 400 100">
  <style>
    @font-face {
      font-family: 'CustomFont';
      src: url('font.woff2') format('woff2');
    }
    text {
      font-family: 'CustomFont', 'PingFang SC', 'Microsoft YaHei', sans-serif;
    }
  </style>
  <text x="20" y="60" font-size="32">自定义字体</text>
</svg>
```

> 独立 .svg 文件中 `<style>` 内的 `@font-face` 仅在 `<object>` / `<iframe>` 嵌入时生效;内联 SVG 中可直接使用主页面的字体规则。

---

## 文本描边与填充

**描边文字**
`fill="none" stroke="<颜色>" stroke-width="<宽度>"`
```html
<text x="20" y="40" font-size="32" fill="none" stroke="#4f5bd5" stroke-width="1.5">描边文字</text>
```

**双层:先描边后填充**
`paint-order="stroke fill"`
```html
<text
  x="20"
  y="90"
  font-size="32"
  stroke="#fff"
  stroke-width="6"
  fill="#4f5bd5"
  paint-order="stroke fill"
>
  描边填充
</text>
```

**渐变文字**
`fill="url(#<渐变id>)"`
```html
<defs>
  <linearGradient id="text-grad" x1="0%" x2="100%">
    <stop offset="0%" stop-color="#4f5bd5" />
    <stop offset="100%" stop-color="#00b894" />
  </linearGradient>
</defs>
<text x="20" y="140" font-size="32" fill="url(#text-grad)">渐变文字</text>
```

### paint-order 顺序

| 值                    | 含义                     |
| --------------------- | ------------------------ |
| `fill stroke`         | 先填充后描边(默认)     |
| `stroke fill`         | 先描边后填充(描边在下) |
| `fill stroke markers` | 完整顺序                 |

> `stroke fill` 让描边在填充下方,避免粗描边遮挡文字主体,是描边文字的常用技巧。

---

## 可访问文本

**可访问性文本结构**
```html
<svg viewBox="0 0 300 100" role="img" aria-labelledby="chart-title">
  <title id="chart-title">2024 Q1 销售额柱状图</title>
  <text x="150" y="50" text-anchor="middle" font-size="20" aria-hidden="true">销售额柱状图</text>
</svg>
```

- `<title>`:屏幕阅读器读取的主标题
- `aria-hidden="true"`:装饰性文字避免重复朗读

---

## 综合示例:数据标签图表

**带数据标签的柱状图**
```html
<svg viewBox="0 0 400 200">
  <!-- 坐标轴 -->
  <line x1="40" y1="160" x2="380" y2="160" stroke="#333" />
  <line x1="40" y1="20" x2="40" y2="160" stroke="#333" />
  <!-- 柱子与数据标签 -->
  <g font-family="sans-serif">
    <rect x="80" y="80" width="40" height="80" fill="#4f5bd5" />
    <text x="100" y="70" text-anchor="middle" font-size="14" fill="#333">120</text>
    <text x="100" y="180" text-anchor="middle" font-size="12" fill="#666">Q1</text>

    <rect x="160" y="50" width="40" height="110" fill="#00b894" />
    <text x="180" y="40" text-anchor="middle" font-size="14" fill="#333">165</text>
    <text x="180" y="180" text-anchor="middle" font-size="12" fill="#666">Q2</text>

    <rect x="240" y="20" width="40" height="140" fill="#d63031" />
    <text x="260" y="10" text-anchor="middle" font-size="14" fill="#333">210</text>
    <text x="260" y="180" text-anchor="middle" font-size="12" fill="#666">Q3</text>
  </g>
</svg>
```

<!-- ============ 文档分隔线：012-svg/007-SVGColorFill.md ============ -->

## 1. 填充 fill

`fill` 控制图形内部颜色，支持颜色值、URL 引用、关键字。

```html
<svg viewBox="0 0 300 100">
  <rect x="10" y="10" width="60" height="60" fill="#4f5bd5" />
  <rect x="80" y="10" width="60" height="60" fill="rgb(0,184,148)" />
  <rect x="150" y="10" width="60" height="60" fill="rgba(214,48,49,0.5)" />
  <rect x="220" y="10" width="60" height="60" fill="url(#grad)" />
</svg>
```

### 1.1 fill 支持的值

| 类型         | 示例                         |
| ------------ | ---------------------------- |
| 关键字       | `red`、`blue`、`transparent` |
| 十六进制     | `#4f5bd5`、`#fff`            |
| RGB          | `rgb(79,91,213)`             |
| RGBA         | `rgba(79,91,213,0.5)`        |
| HSL          | `hsl(233, 62%, 57%)`         |
| URL 引用     | `url(#gradient)`             |
| currentColor | 引用当前 `color` 属性        |

### 1.2 fill-opacity 填充透明度

```html
<circle cx="50" cy="50" r="30" fill="#4f5bd5" fill-opacity="0.5" />
<!-- 等价于 rgba(79,91,213,0.5)，但 fill-opacity 可独立控制 -->
```

`fill-opacity` 与 `rgba()` 区别：fill-opacity 不影响 stroke 透明度，可单独控制填充层。

## 2. 描边 stroke

### 2.1 基础属性

```html
<rect
  x="10"
  y="10"
  width="80"
  height="60"
  fill="none"
  stroke="#4f5bd5"
  stroke-width="3"
  stroke-opacity="0.8"
/>
```

| 属性                | 说明                            |
| ------------------- | ------------------------------- |
| `stroke`            | 描边颜色                        |
| `stroke-width`      | 描边宽度                        |
| `stroke-opacity`    | 描边透明度                      |
| `stroke-linecap`    | 端点形状：butt / round / square |
| `stroke-linejoin`   | 拐角：miter / round / bevel     |
| `stroke-miterlimit` | 尖角最大长度比（默认 4）        |
| `stroke-dasharray`  | 虚线模式                        |
| `stroke-dashoffset` | 虚线起始偏移                    |

### 2.2 stroke-miterlimit 尖角限制

```html
<polyline
  points="10,90 50,10 90,90"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="miter"
  stroke-miterlimit="2"
/>
<!-- 当尖角过尖（夹角小于某阈值），自动转为 bevel -->
```

默认 4，当 miter 长度超过 stroke-width 的 4 倍时自动斜切。

## 3. opacity 透明度

### 3.1 元素级 opacity

```html
<g opacity="0.5">
  <rect width="100" height="100" fill="#4f5bd5" />
  <circle cx="80" cy="80" r="30" fill="#d63031" />
</g>
<!-- 整组透明度 0.5，子元素互相叠加 -->
```

### 3.2 与 fill-opacity 区别

```html
<!-- opacity 影响整体（含子元素叠加） -->
<g opacity="0.5">
  <rect fill="#4f5bd5" />
</g>

<!-- fill-opacity 仅影响填充层，stroke 不受影响 -->
<rect fill="#4f5bd5" fill-opacity="0.5" stroke="#000" />
```

## 4. currentColor 主题色

`currentColor` 引用当前元素的 `color` 属性，实现 CSS 联动主题化。

```html
<svg viewBox="0 0 100 100" style="color: #4f5bd5">
  <circle cx="50" cy="50" r="40" fill="currentColor" />
</svg>
```

```css
.icon-primary {
  color: #4f5bd5;
}
.icon-danger {
  color: #d63031;
}
.icon-success {
  color: #00b894;
}
```

```html
<svg class="icon-danger" viewBox="0 0 24 24">
  <path d="M12 2 L22 20 L2 20 Z" fill="currentColor" />
  <text x="12" y="18" text-anchor="middle" fill="#fff" font-size="14">!</text>
</svg>
```

> `currentColor` 是 SVG 图标系统主题化的核心，让同一图标可在不同上下文中显示不同颜色。

## 5. paint-order 绘制顺序

`paint-order` 控制 fill、stroke、markers 的绘制顺序。

```html
<text font-size="40" stroke="#fff" stroke-width="6" fill="#4f5bd5" paint-order="stroke fill">
  描边在下
</text>
```

| 值                    | 效果                                     |
| --------------------- | ---------------------------------------- |
| `fill stroke`         | 先填充后描边（默认，描边在上）           |
| `stroke fill`         | 先描边后填充（填充在上，描边不遮挡文字） |
| `fill stroke markers` | 完整顺序                                 |

> 描边文字推荐 `stroke fill`，避免粗描边遮挡文字内部。

## 6. vector-effect 矢量效果

`vector-effect` 控制图形在缩放时的描边行为，最常用的是 `non-scaling-stroke`。

### 6.1 默认行为：描边随缩放

```html
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect x="10" y="10" width="80" height="80" fill="none" stroke="#000" stroke-width="2" />
  <!-- viewBox 100×100 缩放到 200×200，描边实际显示 4px -->
</svg>
```

### 6.2 non-scaling-stroke 描边不缩放

```html
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect
    x="10"
    y="10"
    width="80"
    height="80"
    fill="none"
    stroke="#000"
    stroke-width="2"
    vector-effect="non-scaling-stroke"
  />
  <!-- 描边始终保持 2px，不受 viewBox 缩放影响 -->
</svg>
```

### 6.3 应用场景

| 场景           | 说明                         |
| -------------- | ---------------------------- |
| **地图边界**   | 地图缩放时边界线粗细保持一致 |
| **图表网格线** | 数据图缩放时网格线宽不变     |
| **响应式图标** | 图标在不同尺寸下描边视觉一致 |
| **技术绘图**   | 工程图描边宽度有严格规范     |

## 7. fill-rule 填充规则

复杂路径的填充规则，详见 路径 path 详解。

```html
<!-- 五角星中心镂空 -->
<path
  d="M 100 10 L 120 70 L 180 70 L 130 105 L 150 165 L 100 130 L 50 165 L 70 105 L 20 70 L 80 70 Z"
  fill="#d63031"
  fill-rule="evenodd"
/>
```

## 8. 颜色函数

SVG 支持 CSS Color Module Level 4 的所有颜色函数。

### 8.1 hex 与 rgb

```html
<rect fill="#4f5bd5" />
<rect fill="rgb(79 91 213)" />
<rect fill="rgb(79 91 213 / 0.5)" />
```

### 8.2 hsl 色相旋转

```html
<rect fill="hsl(233 62% 57%)" /> <rect fill="hsl(233 62% 57% / 0.5)" />
```

### 8.3 color-mix 混色（现代浏览器）

```html
<rect fill="color-mix(in srgb, #4f5bd5 50%, white)" />
<!-- 50% 蓝色与白色混合 -->
```

## 9. CSS 变量集成

SVG 可使用 CSS 自定义属性，实现运行时主题切换。

```html
<style>
  :root {
    --brand: #4f5bd5;
    --danger: #d63031;
  }
  .dark-theme {
    --brand: #8b92e8;
    --danger: #ff6b6b;
  }
</style>

<svg viewBox="0 0 100 100">
  <rect width="100" height="50" fill="var(--brand)" />
  <rect y="50" width="100" height="50" fill="var(--danger)" />
</svg>
```

切换父元素 class 即可联动 SVG 颜色变化。

## 10. 描边动画技巧

### 10.1 stroke-dasharray 绘制动画

```html
<svg viewBox="0 0 200 100">
  <path
    d="M 10 50 Q 100 10 190 50"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="3"
    stroke-dasharray="200"
    stroke-dashoffset="200"
  >
    <animate attributeName="stroke-dashoffset" from="200" to="0" dur="2s" fill="freeze" />
  </path>
</svg>
```

原理：dasharray 等于路径总长，dashoffset 从全长到 0，模拟"画线"效果。

### 10.2 流动虚线

```css
@keyframes dash-flow {
  to {
    stroke-dashoffset: -24;
  }
}
.flow {
  stroke-dasharray: 8 4;
  animation: dash-flow 1s linear infinite;
}
```

```html
<line x1="10" y1="50" x2="190" y2="50" stroke="#4f5bd5" stroke-width="3" class="flow" />
```

形成"蚂蚁线"效果，常用于表示数据流或加载中状态。

## 11. 综合示例：渐变描边按钮

```html
<svg viewBox="0 0 200 60">
  <defs>
    <linearGradient id="btn-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <rect
    x="2"
    y="2"
    width="196"
    height="56"
    rx="28"
    fill="none"
    stroke="url(#btn-grad)"
    stroke-width="2"
    vector-effect="non-scaling-stroke"
  />
  <text x="100" y="35" text-anchor="middle" font-size="18" fill="url(#btn-grad)" font-weight="bold">
    立即开始
  </text>
</svg>
```

下一篇介绍渐变与图案，构建更丰富的视觉表现。
## fill 填充

**fill 填充属性**
`fill="<颜色值 | url(#id) | currentColor | transparent>"`
```html
<svg viewBox="0 0 300 100">
  <rect x="10" y="10" width="60" height="60" fill="#4f5bd5" />
  <rect x="80" y="10" width="60" height="60" fill="rgb(0,184,148)" />
  <rect x="150" y="10" width="60" height="60" fill="rgba(214,48,49,0.5)" />
  <rect x="220" y="10" width="60" height="60" fill="url(#grad)" />
</svg>
```

### fill 支持的值

| 类型         | 示例                         |
| ------------ | ---------------------------- |
| 关键字       | `red`、`blue`、`transparent` |
| 十六进制     | `#4f5bd5`、`#fff`            |
| RGB          | `rgb(79,91,213)`             |
| RGBA         | `rgba(79,91,213,0.5)`        |
| HSL          | `hsl(233, 62%, 57%)`         |
| URL 引用     | `url(#gradient)`             |
| currentColor | 引用当前 `color` 属性        |

### fill-opacity 填充透明度

**fill-opacity 独立控制填充透明度**
`fill-opacity="<0-1>"`
```html
<circle cx="50" cy="50" r="30" fill="#4f5bd5" fill-opacity="0.5" />
<!-- 等价于 rgba(79,91,213,0.5),但 fill-opacity 可独立控制 -->
```

`fill-opacity` 与 `rgba()` 区别:fill-opacity 不影响 stroke 透明度,可单独控制填充层。

---

## stroke 描边

**stroke 描边基础属性**
```html
<rect
  x="10"
  y="10"
  width="80"
  height="60"
  fill="none"
  stroke="#4f5bd5"
  stroke-width="3"
  stroke-opacity="0.8"
/>
```

### stroke 属性列表

| 属性                | 说明                            |
| ------------------- | ------------------------------- |
| `stroke`            | 描边颜色                        |
| `stroke-width`      | 描边宽度                        |
| `stroke-opacity`    | 描边透明度                      |
| `stroke-linecap`    | 端点形状:butt / round / square |
| `stroke-linejoin`   | 拐角:miter / round / bevel     |
| `stroke-miterlimit` | 尖角最大长度比(默认 4)        |
| `stroke-dasharray`  | 虚线模式                        |
| `stroke-dashoffset` | 虚线起始偏移                    |

### stroke-miterlimit 尖角限制

**stroke-miterlimit 尖角最大长度比**
`stroke-miterlimit="<比值>"`
```html
<polyline
  points="10,90 50,10 90,90"
  stroke="#000"
  stroke-width="10"
  fill="none"
  stroke-linejoin="miter"
  stroke-miterlimit="2"
/>
<!-- 当尖角过尖(夹角小于某阈值),自动转为 bevel -->
```

默认 4,当 miter 长度超过 stroke-width 的 4 倍时自动斜切。

---

## opacity 透明度

### 元素级 opacity

**opacity 元素整体透明度**
`opacity="<0-1>"`
```html
<g opacity="0.5">
  <rect width="100" height="100" fill="#4f5bd5" />
  <circle cx="80" cy="80" r="30" fill="#d63031" />
</g>
<!-- 整组透明度 0.5,子元素互相叠加 -->
```

### opacity 与 fill-opacity 区别

```html
<!-- opacity 影响整体(含子元素叠加) -->
<g opacity="0.5">
  <rect fill="#4f5bd5" />
</g>

<!-- fill-opacity 仅影响填充层,stroke 不受影响 -->
<rect fill="#4f5bd5" fill-opacity="0.5" stroke="#000" />
```

---

## currentColor 主题色

**currentColor 引用当前 color 属性**
`fill="currentColor"` / `stroke="currentColor"`
```html
<svg viewBox="0 0 100 100" style="color: #4f5bd5">
  <circle cx="50" cy="50" r="40" fill="currentColor" />
</svg>
```

```css
.icon-primary {
  color: #4f5bd5;
}
.icon-danger {
  color: #d63031;
}
.icon-success {
  color: #00b894;
}
```

```html
<svg class="icon-danger" viewBox="0 0 24 24">
  <path d="M12 2 L22 20 L2 20 Z" fill="currentColor" />
  <text x="12" y="18" text-anchor="middle" fill="#fff" font-size="14">!</text>
</svg>
```

> `currentColor` 是 SVG 图标系统主题化的核心,让同一图标可在不同上下文中显示不同颜色。

---

## paint-order 绘制顺序

**paint-order 绘制顺序**
`paint-order="<fill | stroke | markers> ..."`
```html
<text font-size="40" stroke="#fff" stroke-width="6" fill="#4f5bd5" paint-order="stroke fill">
  描边在下
</text>
```

| 值                    | 效果                                     |
| --------------------- | ---------------------------------------- |
| `fill stroke`         | 先填充后描边(默认,描边在上)           |
| `stroke fill`         | 先描边后填充(填充在上,描边不遮挡文字) |
| `fill stroke markers` | 完整顺序                                 |

> 描边文字推荐 `stroke fill`,避免粗描边遮挡文字内部。

---

## vector-effect 矢量效果

### 默认行为:描边随缩放

```html
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect x="10" y="10" width="80" height="80" fill="none" stroke="#000" stroke-width="2" />
  <!-- viewBox 100×100 缩放到 200×200,描边实际显示 4px -->
</svg>
```

### non-scaling-stroke 描边不缩放

**vector-effect="non-scaling-stroke"**
`vector-effect="non-scaling-stroke"`
```html
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect
    x="10"
    y="10"
    width="80"
    height="80"
    fill="none"
    stroke="#000"
    stroke-width="2"
    vector-effect="non-scaling-stroke"
  />
  <!-- 描边始终保持 2px,不受 viewBox 缩放影响 -->
</svg>
```

### 应用场景

| 场景           | 说明                         |
| -------------- | ---------------------------- |
| **地图边界**   | 地图缩放时边界线粗细保持一致 |
| **图表网格线** | 数据图缩放时网格线宽不变     |
| **响应式图标** | 图标在不同尺寸下描边视觉一致 |
| **技术绘图**   | 工程图描边宽度有严格规范     |

---

## fill-rule 填充规则

**fill-rule 复杂路径填充规则**
`fill-rule="<nonzero | evenodd>"`
```html
<!-- 五角星中心镂空 -->
<path
  d="M 100 10 L 120 70 L 180 70 L 130 105 L 150 165 L 100 130 L 50 165 L 70 105 L 20 70 L 80 70 Z"
  fill="#d63031"
  fill-rule="evenodd"
/>
```

---

## 颜色函数

### hex 与 rgb

**RGB 颜色函数**
```html
<rect fill="#4f5bd5" />
<rect fill="rgb(79 91 213)" />
<rect fill="rgb(79 91 213 / 0.5)" />
```

### hsl 色相旋转

**HSL 颜色函数**
```html
<rect fill="hsl(233 62% 57%)" />
<rect fill="hsl(233 62% 57% / 0.5)" />
```

### color-mix 混色

**color-mix 混色函数(现代浏览器)**
`color-mix(in <色彩空间>, <颜色1> <百分比>, <颜色2>)`
```html
<rect fill="color-mix(in srgb, #4f5bd5 50%, white)" />
<!-- 50% 蓝色与白色混合 -->
```

---

## CSS 变量集成

**SVG 使用 CSS 自定义属性**
`fill="var(--<变量名>)"`
```html
<style>
  :root {
    --brand: #4f5bd5;
    --danger: #d63031;
  }
  .dark-theme {
    --brand: #8b92e8;
    --danger: #ff6b6b;
  }
</style>

<svg viewBox="0 0 100 100">
  <rect width="100" height="50" fill="var(--brand)" />
  <rect y="50" width="100" height="50" fill="var(--danger)" />
</svg>
```

切换父元素 class 即可联动 SVG 颜色变化。

---

## 描边动画

### stroke-dasharray 绘制动画

**stroke-dasharray + animate 实现绘制动画**
```html
<svg viewBox="0 0 200 100">
  <path
    d="M 10 50 Q 100 10 190 50"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="3"
    stroke-dasharray="200"
    stroke-dashoffset="200"
  >
    <animate attributeName="stroke-dashoffset" from="200" to="0" dur="2s" fill="freeze" />
  </path>
</svg>
```

原理:dasharray 等于路径总长,dashoffset 从全长到 0,模拟"画线"效果。

### 流动虚线

**CSS 流动虚线动画**
```css
@keyframes dash-flow {
  to {
    stroke-dashoffset: -24;
  }
}
.flow {
  stroke-dasharray: 8 4;
  animation: dash-flow 1s linear infinite;
}
```

```html
<line x1="10" y1="50" x2="190" y2="50" stroke="#4f5bd5" stroke-width="3" class="flow" />
```

形成"蚂蚁线"效果,常用于表示数据流或加载中状态。

---

## 综合示例:渐变描边按钮

**渐变描边按钮**
```html
<svg viewBox="0 0 200 60">
  <defs>
    <linearGradient id="btn-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <rect
    x="2"
    y="2"
    width="196"
    height="56"
    rx="28"
    fill="none"
    stroke="url(#btn-grad)"
    stroke-width="2"
    vector-effect="non-scaling-stroke"
  />
  <text x="100" y="35" text-anchor="middle" font-size="18" fill="url(#btn-grad)" font-weight="bold">
    立即开始
  </text>
</svg>
```

<!-- ============ 文档分隔线：012-svg/008-SVGGradientPattern.md ============ -->

## 1. 线性渐变 linearGradient

`<linearGradient>` 沿直线方向过渡颜色。

```html
<svg viewBox="0 0 300 100">
  <defs>
    <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="100%" stop-color="#f9a825" />
    </linearGradient>
  </defs>
  <rect width="300" height="100" fill="url(#lg)" />
</svg>
```

### 1.1 关键属性

| 属性                | 说明                                       | 默认值            |
| ------------------- | ------------------------------------------ | ----------------- |
| `x1, y1`            | 起点坐标                                   | 0%                |
| `x2, y2`            | 终点坐标                                   | 100%              |
| `gradientUnits`     | 坐标系：objectBoundingBox / userSpaceOnUse | objectBoundingBox |
| `gradientTransform` | 渐变变换矩阵                               | 无                |
| `spreadMethod`      | 超出范围行为：pad / reflect / repeat       | pad               |

### 1.2 方向控制

```html
<!-- 水平渐变 -->
<linearGradient id="h" x1="0%" x2="100%">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>

<!-- 垂直渐变 -->
<linearGradient id="v" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>

<!-- 对角线渐变 -->
<linearGradient id="d" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

### 1.3 stop 颜色停止点

```html
<linearGradient id="multi">
  <stop offset="0%" stop-color="#4f5bd5" stop-opacity="1" />
  <stop offset="50%" stop-color="#00b894" stop-opacity="0.5" />
  <stop offset="100%" stop-color="#f9a825" stop-opacity="0" />
</linearGradient>
```

- `offset`：0% ~ 100% 位置
- `stop-color`：该位置颜色
- `stop-opacity`：该位置透明度

### 1.4 spreadMethod 超出范围

```html
<!-- pad：超出部分用端点色填充（默认） -->
<linearGradient id="pad" x1="20%" x2="80%" spreadMethod="pad">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>

<!-- reflect：镜像反射 -->
<linearGradient id="reflect" x1="20%" x2="80%" spreadMethod="reflect">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>

<!-- repeat：重复平铺 -->
<linearGradient id="repeat" x1="20%" x2="80%" spreadMethod="repeat">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

## 2. 径向渐变 radialGradient

`<radialGradient>` 从中心向外辐射。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <radialGradient id="rg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff" />
      <stop offset="100%" stop-color="#4f5bd5" />
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="100" fill="url(#rg)" />
</svg>
```

### 2.1 关键属性

| 属性            | 说明             | 默认值            |
| --------------- | ---------------- | ----------------- |
| `cx, cy`        | 圆心             | 50%               |
| `r`             | 半径             | 50%               |
| `fx, fy`        | 焦点（颜色起点） | 等于 cx, cy       |
| `gradientUnits` | 坐标系           | objectBoundingBox |
| `spreadMethod`  | 超出范围         | pad               |

### 2.2 焦点偏移

```html
<radialGradient id="spotlight" cx="50%" cy="50%" r="50%" fx="30%" fy="30%">
  <stop offset="0%" stop-color="#fff" stop-opacity="0.8" />
  <stop offset="100%" stop-color="#4f5bd5" stop-opacity="0" />
</radialGradient>
<!-- 聚光灯效果：焦点偏左上 -->
```

## 3. gradientUnits 坐标系

### 3.1 objectBoundingBox（默认）

渐变坐标相对于应用元素的边界框，0% 到 100% 对应元素 0 到 1。

```html
<linearGradient id="bb" x1="0%" x2="100%" gradientUnits="objectBoundingBox">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
<!-- 不同尺寸的 rect 都会从左到右渐变 -->
<rect x="0" y="0" width="100" height="50" fill="url(#bb)" />
<rect x="0" y="60" width="200" height="80" fill="url(#bb)" />
```

### 3.2 userSpaceOnUse

渐变坐标使用 SVG 用户坐标系，与具体元素无关。

```html
<linearGradient id="us" x1="0" y1="0" x2="300" y2="0" gradientUnits="userSpaceOnUse">
  <stop offset="0" stop-color="#4f5bd5" />
  <stop offset="150" stop-color="#00b894" />
  <stop offset="300" stop-color="#f9a825" />
</linearGradient>
<!-- 渐变固定在 0-300 范围，多个元素共享同一渐变带 -->
<rect x="0" y="0" width="150" height="50" fill="url(#us)" />
<rect x="150" y="0" width="150" height="50" fill="url(#us)" />
```

> 多个元素需要"拼接同一渐变"时使用 userSpaceOnUse。

## 4. 图案 pattern

`<pattern>` 定义可平铺的图案，类似 CSS background-repeat。

```html
<svg viewBox="0 0 200 200">
  <defs>
    <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="3" fill="#4f5bd5" />
    </pattern>
  </defs>
  <rect width="200" height="200" fill="url(#dots)" />
</svg>
```

### 4.1 关键属性

| 属性                  | 说明                                       |
| --------------------- | ------------------------------------------ |
| `x, y`                | 图案起始偏移                               |
| `width, height`       | 单个图案单元尺寸                           |
| `patternUnits`        | 坐标系：userSpaceOnUse / objectBoundingBox |
| `patternContentUnits` | 图案内容坐标系                             |
| `patternTransform`    | 图案变换                                   |

### 4.2 网格图案

```html
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#4f5bd5" stroke-width="0.5" />
</pattern>
<rect width="400" height="300" fill="url(#grid)" />
```

### 4.3 斜纹图案

```html
<pattern
  id="stripes"
  width="10"
  height="10"
  patternUnits="userSpaceOnUse"
  patternTransform="rotate(45)"
>
  <rect width="5" height="10" fill="#4f5bd5" />
  <rect x="5" width="5" height="10" fill="#00b894" />
</pattern>
```

### 4.4 复杂图案：十字纹

```html
<pattern id="cross" width="30" height="30" patternUnits="userSpaceOnUse">
  <path d="M 15 0 L 15 30 M 0 15 L 30 15" stroke="#4f5bd5" stroke-width="1" />
</pattern>
<rect width="300" height="200" fill="url(#cross)" />
```

## 5. 图案与渐变组合

图案内可使用渐变填充，实现复杂纹理。

```html
<svg viewBox="0 0 300 200">
  <defs>
    <linearGradient id="tile-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <pattern id="gradient-dots" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="20" cy="20" r="12" fill="url(#tile-grad)" />
    </pattern>
  </defs>
  <rect width="300" height="200" fill="url(#gradient-dots)" />
</svg>
```

## 6. 渐变文字

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="text-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="100%" stop-color="#f9a825" />
    </linearGradient>
  </defs>
  <text
    x="200"
    y="60"
    text-anchor="middle"
    font-size="48"
    font-weight="bold"
    fill="url(#text-grad)"
  >
    FANDEX
  </text>
</svg>
```

## 7. 渐变描边

```html
<svg viewBox="0 0 200 100">
  <defs>
    <linearGradient id="stroke-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <rect
    x="10"
    y="10"
    width="180"
    height="80"
    rx="12"
    fill="none"
    stroke="url(#stroke-grad)"
    stroke-width="4"
  />
</svg>
```

## 8. 渐变动画

```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="animated-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5">
        <animate
          attributeName="stop-color"
          values="#4f5bd5;#00b894;#4f5bd5"
          dur="4s"
          repeatCount="indefinite"
        />
      </stop>
      <stop offset="100%" stop-color="#00b894">
        <animate
          attributeName="stop-color"
          values="#00b894;#4f5bd5;#00b894"
          dur="4s"
          repeatCount="indefinite"
        />
      </stop>
    </linearGradient>
  </defs>
  <rect width="400" height="100" fill="url(#animated-grad)" />
</svg>
```

## 9. 实战：圆形按钮渐变

```html
<svg viewBox="0 0 200 80" width="200" height="80">
  <defs>
    <linearGradient id="btn-primary" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#5b6ee8" />
      <stop offset="100%" stop-color="#4f5bd5" />
    </linearGradient>
    <filter id="btn-shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#4f5bd5" flood-opacity="0.3" />
    </filter>
  </defs>
  <rect
    x="10"
    y="10"
    width="180"
    height="60"
    rx="30"
    fill="url(#btn-primary)"
    filter="url(#btn-shadow)"
  />
  <text
    x="100"
    y="42"
    text-anchor="middle"
    dominant-baseline="middle"
    font-size="20"
    fill="#fff"
    font-weight="bold"
  >
    立即开始
  </text>
</svg>
```

## 10. 性能注意

| 优化点                               | 说明                                           |
| ------------------------------------ | ---------------------------------------------- |
| **避免过多 stop**                    | 5 个以上 stop 会影响渲染性能                   |
| **优先使用 userSpaceOnUse 共享渐变** | 多元素复用同一渐变可减少计算                   |
| **渐变区域匹配元素**                 | gradientUnits=objectBoundingBox 时渐变自动适配 |
| **复杂图案用图片**                   | 极复杂纹理用 PNG/WebP 替代 pattern             |

下一篇介绍 transform 变换。
## 线性渐变 linearGradient

**linearGradient 线性渐变**
`<linearGradient id="<标识>" x1="<起点x>" y1="<起点y>" x2="<终点x>" y2="<终点y>" [gradientUnits="<坐标系>"] [spreadMethod="<超出范围>"]> <stop ... /> ... </linearGradient>`
```html
<svg viewBox="0 0 300 100">
  <defs>
    <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="100%" stop-color="#f9a825" />
    </linearGradient>
  </defs>
  <rect width="300" height="100" fill="url(#lg)" />
</svg>
```

### linearGradient 关键属性

| 属性                | 说明                                       | 默认值            |
| ------------------- | ------------------------------------------ | ----------------- |
| `x1, y1`            | 起点坐标                                   | 0%                |
| `x2, y2`            | 终点坐标                                   | 100%              |
| `gradientUnits`     | 坐标系:objectBoundingBox / userSpaceOnUse | objectBoundingBox |
| `gradientTransform` | 渐变变换矩阵                               | 无                |
| `spreadMethod`      | 超出范围行为:pad / reflect / repeat       | pad               |

### 方向控制

**水平渐变**
`<linearGradient id="<id>" x1="0%" x2="100%"> ... </linearGradient>`
```html
<linearGradient id="h" x1="0%" x2="100%">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

**垂直渐变**
`<linearGradient id="<id>" x1="0%" y1="0%" x2="0%" y2="100%"> ... </linearGradient>`
```html
<linearGradient id="v" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

**对角线渐变**
`<linearGradient id="<id>" x1="0%" y1="0%" x2="100%" y2="100%"> ... </linearGradient>`
```html
<linearGradient id="d" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

### stop 颜色停止点

**stop 颜色停止点**
`<stop offset="<0%-100%>" stop-color="<颜色>" [stop-opacity="<0-1>"] />`
```html
<linearGradient id="multi">
  <stop offset="0%" stop-color="#4f5bd5" stop-opacity="1" />
  <stop offset="50%" stop-color="#00b894" stop-opacity="0.5" />
  <stop offset="100%" stop-color="#f9a825" stop-opacity="0" />
</linearGradient>
```

- `offset`:0% ~ 100% 位置
- `stop-color`:该位置颜色
- `stop-opacity`:该位置透明度

### spreadMethod 超出范围

**pad 端点色填充(默认)**
`spreadMethod="pad"`
```html
<linearGradient id="pad" x1="20%" x2="80%" spreadMethod="pad">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

**reflect 镜像反射**
`spreadMethod="reflect"`
```html
<linearGradient id="reflect" x1="20%" x2="80%" spreadMethod="reflect">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

**repeat 重复平铺**
`spreadMethod="repeat"`
```html
<linearGradient id="repeat" x1="20%" x2="80%" spreadMethod="repeat">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
```

---

## 径向渐变 radialGradient

**radialGradient 径向渐变**
`<radialGradient id="<标识>" cx="<圆心x>" cy="<圆心y>" r="<半径>" [fx="<焦点x>"] [fy="<焦点y>"] [gradientUnits="<坐标系>"] [spreadMethod="<超出范围>"]> <stop ... /> ... </radialGradient>`
```html
<svg viewBox="0 0 200 200">
  <defs>
    <radialGradient id="rg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff" />
      <stop offset="100%" stop-color="#4f5bd5" />
    </radialGradient>
  </defs>
  <circle cx="100" cy="100" r="100" fill="url(#rg)" />
</svg>
```

### radialGradient 关键属性

| 属性            | 说明             | 默认值            |
| --------------- | ---------------- | ----------------- |
| `cx, cy`        | 圆心             | 50%               |
| `r`             | 半径             | 50%               |
| `fx, fy`        | 焦点(颜色起点) | 等于 cx, cy       |
| `gradientUnits` | 坐标系           | objectBoundingBox |
| `spreadMethod`  | 超出范围         | pad               |

### 焦点偏移

**焦点偏移聚光灯效果**
`fx="<焦点x>" fy="<焦点y>"`
```html
<radialGradient id="spotlight" cx="50%" cy="50%" r="50%" fx="30%" fy="30%">
  <stop offset="0%" stop-color="#fff" stop-opacity="0.8" />
  <stop offset="100%" stop-color="#4f5bd5" stop-opacity="0" />
</radialGradient>
<!-- 聚光灯效果:焦点偏左上 -->
```

---

## gradientUnits 坐标系

### objectBoundingBox(默认)

**渐变坐标相对于元素边界框**
`gradientUnits="objectBoundingBox"`
```html
<linearGradient id="bb" x1="0%" x2="100%" gradientUnits="objectBoundingBox">
  <stop offset="0%" stop-color="#4f5bd5" />
  <stop offset="100%" stop-color="#00b894" />
</linearGradient>
<!-- 不同尺寸的 rect 都会从左到右渐变 -->
<rect x="0" y="0" width="100" height="50" fill="url(#bb)" />
<rect x="0" y="60" width="200" height="80" fill="url(#bb)" />
```

### userSpaceOnUse

**渐变坐标使用 SVG 用户坐标系**
`gradientUnits="userSpaceOnUse"`
```html
<linearGradient id="us" x1="0" y1="0" x2="300" y2="0" gradientUnits="userSpaceOnUse">
  <stop offset="0" stop-color="#4f5bd5" />
  <stop offset="150" stop-color="#00b894" />
  <stop offset="300" stop-color="#f9a825" />
</linearGradient>
<!-- 渐变固定在 0-300 范围,多个元素共享同一渐变带 -->
<rect x="0" y="0" width="150" height="50" fill="url(#us)" />
<rect x="150" y="0" width="150" height="50" fill="url(#us)" />
```

> 多个元素需要"拼接同一渐变"时使用 userSpaceOnUse。

---

## 图案 pattern

**pattern 平铺图案**
`<pattern id="<标识>" x="<偏移x>" y="<偏移y>" width="<单元宽>" height="<单元高>" [patternUnits="<坐标系>"] [patternContentUnits="<内容坐标系>"] [patternTransform="<变换>"]> ... </pattern>`
```html
<svg viewBox="0 0 200 200">
  <defs>
    <pattern id="dots" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="3" fill="#4f5bd5" />
    </pattern>
  </defs>
  <rect width="200" height="200" fill="url(#dots)" />
</svg>
```

### pattern 关键属性

| 属性                  | 说明                                       |
| --------------------- | ------------------------------------------ |
| `x, y`                | 图案起始偏移                               |
| `width, height`       | 单个图案单元尺寸                           |
| `patternUnits`        | 坐标系:userSpaceOnUse / objectBoundingBox |
| `patternContentUnits` | 图案内容坐标系                             |
| `patternTransform`    | 图案变换                                   |

### 网格图案

**网格 pattern**
```html
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#4f5bd5" stroke-width="0.5" />
</pattern>
<rect width="400" height="300" fill="url(#grid)" />
```

### 斜纹图案

**斜纹 pattern**
`patternTransform="rotate(<角度>)"`
```html
<pattern
  id="stripes"
  width="10"
  height="10"
  patternUnits="userSpaceOnUse"
  patternTransform="rotate(45)"
>
  <rect width="5" height="10" fill="#4f5bd5" />
  <rect x="5" width="5" height="10" fill="#00b894" />
</pattern>
```

### 十字纹图案

**十字纹 pattern**
```html
<pattern id="cross" width="30" height="30" patternUnits="userSpaceOnUse">
  <path d="M 15 0 L 15 30 M 0 15 L 30 15" stroke="#4f5bd5" stroke-width="1" />
</pattern>
<rect width="300" height="200" fill="url(#cross)" />
```

---

## 图案与渐变组合

**图案内使用渐变填充**
```html
<svg viewBox="0 0 300 200">
  <defs>
    <linearGradient id="tile-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <pattern id="gradient-dots" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="20" cy="20" r="12" fill="url(#tile-grad)" />
    </pattern>
  </defs>
  <rect width="300" height="200" fill="url(#gradient-dots)" />
</svg>
```

---

## 渐变文字

**文字填充渐变**
`fill="url(#<渐变id>)"`
```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="text-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="50%" stop-color="#00b894" />
      <stop offset="100%" stop-color="#f9a825" />
    </linearGradient>
  </defs>
  <text
    x="200"
    y="60"
    text-anchor="middle"
    font-size="48"
    font-weight="bold"
    fill="url(#text-grad)"
  >
    FANDEX
  </text>
</svg>
```

---

## 渐变描边

**描边使用渐变**
`stroke="url(#<渐变id>)"`
```html
<svg viewBox="0 0 200 100">
  <defs>
    <linearGradient id="stroke-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>
  <rect
    x="10"
    y="10"
    width="180"
    height="80"
    rx="12"
    fill="none"
    stroke="url(#stroke-grad)"
    stroke-width="4"
  />
</svg>
```

---

## 渐变动画

**stop 颜色动画**
```html
<svg viewBox="0 0 400 100">
  <defs>
    <linearGradient id="animated-grad" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5">
        <animate
          attributeName="stop-color"
          values="#4f5bd5;#00b894;#4f5bd5"
          dur="4s"
          repeatCount="indefinite"
        />
      </stop>
      <stop offset="100%" stop-color="#00b894">
        <animate
          attributeName="stop-color"
          values="#00b894;#4f5bd5;#00b894"
          dur="4s"
          repeatCount="indefinite"
        />
      </stop>
    </linearGradient>
  </defs>
  <rect width="400" height="100" fill="url(#animated-grad)" />
</svg>
```

---

## 综合示例:渐变按钮

**渐变按钮 + 阴影**
```html
<svg viewBox="0 0 200 80" width="200" height="80">
  <defs>
    <linearGradient id="btn-primary" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#5b6ee8" />
      <stop offset="100%" stop-color="#4f5bd5" />
    </linearGradient>
    <filter id="btn-shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#4f5bd5" flood-opacity="0.3" />
    </filter>
  </defs>
  <rect
    x="10"
    y="10"
    width="180"
    height="60"
    rx="30"
    fill="url(#btn-primary)"
    filter="url(#btn-shadow)"
  />
  <text
    x="100"
    y="42"
    text-anchor="middle"
    dominant-baseline="middle"
    font-size="20"
    fill="#fff"
    font-weight="bold"
  >
    立即开始
  </text>
</svg>
```

<!-- ============ 文档分隔线：012-svg/009-SVGTransform.md ============ -->

## 1. transform 属性

`transform` 对元素或分组应用几何变换，**不影响后续元素的坐标系**（除非在 `<g>` 上）。

```html
<svg viewBox="0 0 200 200">
  <rect x="50" y="50" width="50" height="50" fill="#4f5bd5" />
  <rect x="50" y="50" width="50" height="50" fill="#d63031" transform="translate(60, 0)" />
</svg>
```

## 2. 基本变换函数

### 2.1 translate 平移

```html
<rect transform="translate(50, 30)" />
<!-- 或单轴 -->
<rect transform="translate(50, 0)" />
```

| 参数 | 说明                         |
| ---- | ---------------------------- |
| `tx` | X 方向偏移                   |
| `ty` | Y 方向偏移（可省略，默认 0） |

### 2.2 rotate 旋转

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

### 2.3 scale 缩放

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

### 2.4 skew 倾斜

```html
<rect transform="skewX(30)" /> <rect transform="skewY(15)" />
```

| 函数           | 说明        |
| -------------- | ----------- |
| `skewX(angle)` | 沿 X 轴倾斜 |
| `skewY(angle)` | 沐 Y 轴倾斜 |

## 3. matrix 矩阵

所有变换本质都是 2D 仿射矩阵：`matrix(a, b, c, d, e, f)`。

```
| a c e |
| b d f |
| 0 0 1 |
```

变换公式：

- `x' = a*x + c*y + e`
- `y' = b*x + d*y + f`

### 3.1 各变换对应的矩阵

| 变换                | matrix 参数                        |
| ------------------- | ---------------------------------- |
| `translate(tx, ty)` | `matrix(1 0 0 1 tx ty)`            |
| `rotate(θ)`         | `matrix(cosθ sinθ -sinθ cosθ 0 0)` |
| `scale(s)`          | `matrix(s 0 0 s 0 0)`              |
| `skewX(θ)`          | `matrix(1 0 tanθ 1 0 0)`           |

### 3.2 示例

```html
<rect transform="matrix(1 0 0 1 50 30)" />
<!-- 等价于 translate(50, 30) -->

<rect transform="matrix(0.707 0.707 -0.707 0.707 0 0)" />
<!-- 等价于 rotate(45) -->
```

## 4. 变换组合

多个变换用空格分隔，**从右到左**应用（类似 CSS transform）。

```html
<!-- 先 translate 再 rotate（视觉上） -->
<rect transform="translate(100, 100) rotate(45)" />

<!-- 先 rotate 再 translate -->
<rect transform="rotate(45) translate(100, 0)" />
```

### 4.1 顺序影响结果

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

## 5. transform-origin

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

### 5.1 transform-box

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

## 6. CSS transform 与 SVG transform

CSS transform 也可作用于 SVG 元素，但需注意坐标系差异。

### 6.1 CSS 方式

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

### 6.2 两者区别

| 维度       | SVG transform 属性        | CSS transform                        |
| ---------- | ------------------------- | ------------------------------------ |
| 语法       | `rotate(45 100 100)`      | `rotate(45deg)` + `transform-origin` |
| 单位       | 无单位（默认度/像素）     | 需 `deg`、`px`                       |
| 动画       | SMIL `<animateTransform>` | CSS `@keyframes`                     |
| 性能       | 略优（直接矩阵）          | 现代浏览器已优化                     |
| 浏览器支持 | 全部                      | SVG 2 后完整支持                     |

## 7. animateTransform 变换动画

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

### 7.1 多变换叠加 additive

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

## 8. 嵌套变换

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

## 9. 实战：地球绕太阳

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

## 10. 常见陷阱

### 10.1 rotate 默认绕原点

```html
<!-- 错误：矩形被甩到画布外 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45)" />

<!-- 正确：围绕矩形中心旋转 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45 100 100)" />
```

### 10.2 scale 缩放描边

```html
<!-- 描边被放大到 6px -->
<rect stroke-width="2" transform="scale(3)" />

<!-- 保持描边不变 -->
<rect stroke-width="2" transform="scale(3)" vector-effect="non-scaling-stroke" />
```

### 10.3 transform 与 viewBox 重复缩放

```html
<!-- viewBox 已缩放 2 倍，transform scale(2) 会再缩 2 倍 -->
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect width="50" height="50" transform="scale(2)" />
  <!-- 实际显示 200×200 -->
</svg>
```

下一篇介绍滤镜，构建阴影、模糊、光照等高级视觉效果。
## transform 属性

**transform 几何变换**
`transform="<变换函数> <变换函数> ..."`
```html
<svg viewBox="0 0 200 200">
  <rect x="50" y="50" width="50" height="50" fill="#4f5bd5" />
  <rect x="50" y="50" width="50" height="50" fill="#d63031" transform="translate(60, 0)" />
</svg>
```

---

## translate 平移

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

## rotate 旋转

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

## scale 缩放

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

## skew 倾斜

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

## matrix 矩阵

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

### 各变换对应的矩阵

| 变换                | matrix 参数                        |
| ------------------- | ---------------------------------- |
| `translate(tx, ty)` | `matrix(1 0 0 1 tx ty)`            |
| `rotate(θ)`         | `matrix(cosθ sinθ -sinθ cosθ 0 0)` |
| `scale(s)`          | `matrix(s 0 0 s 0 0)`              |
| `skewX(θ)`          | `matrix(1 0 tanθ 1 0 0)`           |

### 示例

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

## 变换组合

**多变换空格分隔,从右到左应用**
`transform="<变换1> <变换2> ..."`
```html
<!-- 先 translate 再 rotate(视觉上) -->
<rect transform="translate(100, 100) rotate(45)" />

<!-- 先 rotate 再 translate -->
<rect transform="rotate(45) translate(100, 0)" />
```

### 顺序影响结果

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

## transform-origin

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

### transform-box

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

## CSS transform 与 SVG transform

### CSS 方式

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

### 两者区别

| 维度       | SVG transform 属性        | CSS transform                        |
| ---------- | ------------------------- | ------------------------------------ |
| 语法       | `rotate(45 100 100)`      | `rotate(45deg)` + `transform-origin` |
| 单位       | 无单位(默认度/像素)     | 需 `deg`、`px`                       |
| 动画       | SMIL `<animateTransform>` | CSS `@keyframes`                     |
| 性能       | 略优(直接矩阵)          | 现代浏览器已优化                     |
| 浏览器支持 | 全部                      | SVG 2 后完整支持                     |

---

## animateTransform 变换动画

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

### 多变换叠加 additive

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

## 嵌套变换

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

## 综合示例:地球绕太阳

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

## 常见陷阱

### rotate 默认绕原点

```html
<!-- 错误:矩形被甩到画布外 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45)" />

<!-- 正确:围绕矩形中心旋转 -->
<rect x="50" y="50" width="100" height="100" transform="rotate(45 100 100)" />
```

### scale 缩放描边

```html
<!-- 描边被放大到 6px -->
<rect stroke-width="2" transform="scale(3)" />

<!-- 保持描边不变 -->
<rect stroke-width="2" transform="scale(3)" vector-effect="non-scaling-stroke" />
```

### transform 与 viewBox 重复缩放

```html
<!-- viewBox 已缩放 2 倍,transform scale(2) 会再缩 2 倍 -->
<svg viewBox="0 0 100 100" width="200" height="200">
  <rect width="50" height="50" transform="scale(2)" />
  <!-- 实际显示 200×200 -->
</svg>
```

<!-- ============ 文档分隔线：012-svg/010-SVGFilterDetailed.md ============ -->

## 1. filter 基础

`<filter>` 在 `<defs>` 中定义，通过 `filter="url(#id)"` 应用到元素。

```html
<svg viewBox="0 0 200 100">
  <defs>
    <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" />
    </filter>
  </defs>
  <rect x="20" y="20" width="160" height="60" fill="#4f5bd5" filter="url(#blur)" />
</svg>
```

### 1.1 filter 区域属性

| 属性             | 说明           | 默认值            |
| ---------------- | -------------- | ----------------- |
| `x, y`           | 滤镜区域左上角 | -10%              |
| `width, height`  | 滤镜区域尺寸   | 120%              |
| `filterUnits`    | 区域坐标系     | objectBoundingBox |
| `primitiveUnits` | 滤镜基元坐标   | userSpaceOnUse    |

> 模糊、阴影等效果会超出元素边界，需扩大 filter 区域否则被裁剪。

## 2. feGaussianBlur 高斯模糊

```html
<filter id="blur5">
  <feGaussianBlur stdDeviation="5" />
</filter>
<filter id="blur-xy">
  <feGaussianBlur stdDeviation="5 2" />
  <!-- X 方向模糊 5，Y 方向模糊 2 -->
</filter>
```

| 参数           | 说明                     |
| -------------- | ------------------------ |
| `stdDeviation` | 模糊半径，可分别指定 X Y |

## 3. feDropShadow 阴影

```html
<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
  <feDropShadow dx="4" dy="4" stdDeviation="3" flood-color="#000" flood-opacity="0.3" />
</filter>
```

| 参数            | 说明       | 默认值 |
| --------------- | ---------- | ------ |
| `dx, dy`        | 阴影偏移   | 2      |
| `stdDeviation`  | 模糊半径   | 2      |
| `flood-color`   | 阴影颜色   | #000   |
| `flood-opacity` | 阴影透明度 | 1      |

### 3.1 内阴影模拟

SVG 无原生 inner-shadow，可通过 feComposite 实现：

```html
<filter id="inner-shadow">
  <feOffset dx="0" dy="2">
    <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.5" />
  </feOffset>
  <feComposite operator="out" in="SourceGraphic" />
  <feComposite operator="in" in2="SourceAlpha" />
  <feComposite operator="over" in="SourceGraphic" />
</filter>
```

## 4. feColorMatrix 颜色矩阵

`<feColorMatrix>` 通过 4×5 矩阵变换 RGBA 通道，实现调色、灰度、反相等效果。

### 4.1 矩阵语法

```html
<filter id="grayscale">
  <feColorMatrix
    type="matrix"
    values="0.3 0.59 0.11 0 0
            0.3 0.59 0.11 0 0
            0.3 0.59 0.11 0 0
            0   0    0    1 0"
  />
</filter>
```

每个像素的 RGBA 按矩阵相乘：`R' = 0.3R + 0.59G + 0.11B + 0A + 0`，得到灰度。

### 4.2 预设类型 type

| 值                 | 说明                               |
| ------------------ | ---------------------------------- |
| `matrix`           | 自定义矩阵                         |
| `saturate`         | 饱和度（0=灰度，1=原色，2=高饱和） |
| `hueRotate`        | 色相旋转（度）                     |
| `luminanceToAlpha` | 亮度转透明度                       |

```html
<filter id="saturate">
  <feColorMatrix type="saturate" values="2" />
</filter>

<filter id="hue-rotate">
  <feColorMatrix type="hueRotate" values="90" />
</filter>
```

## 5. feComponentTransfer 通道映射

对每个颜色通道独立应用函数（亮度、对比度）。

```html
<filter id="brightness">
  <feComponentTransfer>
    <feFuncR type="linear" slope="1.5" intercept="0" />
    <feFuncG type="linear" slope="1.5" intercept="0" />
    <feFuncB type="linear" slope="1.5" intercept="0" />
  </feComponentTransfer>
</filter>
```

| 函数              | 说明                            |
| ----------------- | ------------------------------- |
| `feFuncR/G/B/A`   | 通道函数                        |
| `type="linear"`   | 线性：`y = slope*x + intercept` |
| `type="table"`    | 表格查找                        |
| `type="discrete"` | 阶梯量化                        |
| `type="gamma"`    | 伽马校正                        |

## 6. feMerge 合成

`<feMerge>` 将多个滤镜结果叠加合成。

```html
<filter id="glow">
  <feGaussianBlur stdDeviation="4" result="blur" />
  <feMerge>
    <feMergeNode in="blur" />
    <feMergeNode in="blur" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

**原理**：模糊结果叠加两次产生更强光晕，最后叠加原图，形成发光效果。

## 7. 滤镜基元 result/in

每个滤镜基元可用 `result` 命名输出，后续基元用 `in` 引用。

```html
<filter id="emboss">
  <feGaussianBlur in="SourceAlpha" stdDeviation="1" result="blur" />
  <feSpecularLighting
    in="blur"
    surfaceScale="3"
    specularConstant="1"
    specularExponent="20"
    lighting-color="#fff"
    result="spec"
  >
    <fePointLight x="-50" y="-50" z="200" />
  </feSpecularLighting>
  <feComposite in="spec" in2="SourceAlpha" operator="in" result="specMasked" />
  <feComposite
    in="SourceGraphic"
    in2="specMasked"
    operator="arithmetic"
    k1="0"
    k2="1"
    k3="1"
    k4="0"
  />
</filter>
```

| 输入              | 含义                              |
| ----------------- | --------------------------------- |
| `SourceGraphic`   | 原始彩色图形                      |
| `SourceAlpha`     | 原始图形的 alpha 通道（黑白蒙版） |
| `BackgroundImage` | 背景图（需 `enable-background`）  |
| `Previous`        | 前一基元结果                      |
| 自定义 result     | 命名的中间结果                    |

## 8. feOffset 偏移

```html
<filter id="offset">
  <feOffset dx="10" dy="10" in="SourceAlpha" />
  <feFlood flood-color="#000" flood-opacity="0.3" />
  <feComposite operator="in" in2="SourceAlpha" />
  <feMerge>
    <feMergeNode />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

等价于 feDropShadow 的手动实现。

## 9. feFlood 纯色填充

```html
<filter id="red-overlay">
  <feFlood flood-color="#d63031" flood-opacity="0.5" />
  <feComposite operator="in" in2="SourceGraphic" />
</filter>
```

将图形填充为指定颜色，配合 feComposite 可制作色彩滤镜。

## 10. feSpecularLighting 光照

```html
<filter id="metallic">
  <feGaussianBlur in="SourceAlpha" stdDeviation="2" result="blur" />
  <feSpecularLighting
    in="blur"
    surfaceScale="5"
    specularConstant="1"
    specularExponent="20"
    lighting-color="#fff"
    result="spec"
  >
    <feDistantLight azimuth="135" elevation="45" />
  </feSpecularLighting>
  <feComposite in="spec" in2="SourceAlpha" operator="in" />
  <feComposite in="SourceGraphic" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" />
</filter>
```

| 光源               | 说明                           |
| ------------------ | ------------------------------ |
| `<feDistantLight>` | 平行光，参数 azimuth/elevation |
| `<fePointLight>`   | 点光源，参数 x/y/z             |
| `<feSpotLight>`    | 聚光灯                         |

## 11. feTurbulence 噪声

生成柏林噪声，常用于纹理、烟雾、水波。

```html
<filter id="texture">
  <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" />
  <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.2 0" />
  <feComposite operator="in" in2="SourceGraphic" />
</filter>
```

| 参数            | 说明                          |
| --------------- | ----------------------------- |
| `type`          | `fractalNoise` / `turbulence` |
| `baseFrequency` | 频率（越大颗粒越细）          |
| `numOctaves`    | 倍频数（细节层次）            |
| `seed`          | 随机种子                      |
| `stitchTiles`   | 平铺缝合                      |

## 12. feDisplacementMap 位移映射

根据另一张图的像素值扭曲当前图。

```html
<filter id="ripple">
  <feTurbulence type="turbulence" baseFrequency="0.02" numOctaves="2" result="noise" />
  <feDisplacementMap
    in="SourceGraphic"
    in2="noise"
    scale="20"
    xChannelSelector="R"
    yChannelSelector="G"
  />
</filter>
```

`scale=20` 表示根据噪声 R/G 通道值最大位移 20 像素。

## 13. 滤镜组合实战

### 13.1 霓虹发光

```html
<filter id="neon" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="4" result="blur1" />
  <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur2" />
  <feColorMatrix
    in="blur1"
    type="matrix"
    values="0 0 0 0 0.3
                         0 0 0 0 0.4
                         0 0 0 0 1
                         0 0 0 1.5 0"
    result="glow1"
  />
  <feColorMatrix
    in="blur2"
    type="matrix"
    values="0 0 0 0 0.3
                         0 0 0 0 0.4
                         0 0 0 0 1
                         0 0 0 0.8 0"
    result="glow2"
  />
  <feMerge>
    <feMergeNode in="glow2" />
    <feMergeNode in="glow1" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

### 13.2 玻璃磨砂

```html
<filter id="frosted-glass">
  <feGaussianBlur stdDeviation="5" />
  <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.8 0.1" />
</filter>
```

## 14. 性能与兼容

### 14.1 性能注意

| 问题              | 解决方案                                       |
| ----------------- | ---------------------------------------------- |
| 滤镜区域过大      | 缩小 filter 的 width/height 到刚好覆盖效果范围 |
| 嵌套滤镜          | 避免在 filter 内再调用 filter                  |
| 大量元素应用滤镜  | 优先考虑预渲染为位图                           |
| 复杂 feTurbulence | numOctaves ≤ 3                                 |

### 14.2 浏览器兼容

- 现代浏览器全面支持 SVG 滤镜
- `feDropShadow` 在 IE 不支持，需用 feOffset + feFlood + feComposite 替代
- 滤镜在 `<img>` 引用的 SVG 中可能不生效，需内联或 `<object>`

## 15. 实战：玻璃质感卡片

```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="bg" x1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <filter id="card-shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.2" />
    </filter>
    <filter id="card-glow">
      <feGaussianBlur stdDeviation="2" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <!-- 背景 -->
  <rect width="400" height="200" fill="url(#bg)" />
  <!-- 玻璃卡片 -->
  <rect
    x="60"
    y="40"
    width="280"
    height="120"
    rx="16"
    fill="#fff"
    fill-opacity="0.15"
    filter="url(#card-shadow)"
  />
  <text
    x="200"
    y="100"
    text-anchor="middle"
    font-size="24"
    fill="#fff"
    font-weight="bold"
    filter="url(#card-glow)"
  >
    Glass Card
  </text>
</svg>
```

下一篇介绍裁剪与蒙版。
## filter 滤镜容器

**filter 滤镜定义**
`<filter id="<id>" [x="<x>"] [y="<y>"] [width="<w>"] [height="<h>"] [filterUnits="<区域坐标系>"] [primitiveUnits="<基元坐标系>"]><滤镜基元></filter>`
```html
<svg viewBox="0 0 200 100">
  <defs>
    <filter id="blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" />
    </filter>
  </defs>
  <rect x="20" y="20" width="160" height="60" fill="#4f5bd5" filter="url(#blur)" />
</svg>
```

### filter 区域属性

| 属性             | 说明           | 默认值            |
| ---------------- | -------------- | ----------------- |
| `x, y`           | 滤镜区域左上角 | -10%              |
| `width, height`  | 滤镜区域尺寸   | 120%              |
| `filterUnits`    | 区域坐标系     | objectBoundingBox |
| `primitiveUnits` | 滤镜基元坐标   | userSpaceOnUse    |

### filter 应用属性

**filter 引用滤镜**
`filter="url(#<filter-id>)"`
```html
<rect x="20" y="20" width="160" height="60" fill="#4f5bd5" filter="url(#blur)" />
```

---

## feGaussianBlur 高斯模糊

**feGaussianBlur 高斯模糊**
`<feGaussianBlur [in="<输入>"] stdDeviation="<半径>" [result="<输出名>"] />`
```html
<filter id="blur5">
  <feGaussianBlur stdDeviation="5" />
</filter>
<filter id="blur-xy">
  <feGaussianBlur stdDeviation="5 2" />
  <!-- X 方向模糊 5,Y 方向模糊 2 -->
</filter>
```

| 参数           | 说明                     |
| -------------- | ------------------------ |
| `stdDeviation` | 模糊半径,可分别指定 X Y |

---

## feDropShadow 阴影

**feDropShadow 投影**
`<feDropShadow [dx="<x偏移>"] [dy="<y偏移>"] [stdDeviation="<模糊>"] [flood-color="<颜色>"] [flood-opacity="<透明度>"] />`
```html
<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
  <feDropShadow dx="4" dy="4" stdDeviation="3" flood-color="#000" flood-opacity="0.3" />
</filter>
```

| 参数            | 说明       | 默认值 |
| --------------- | ---------- | ------ |
| `dx, dy`        | 阴影偏移   | 2      |
| `stdDeviation`  | 模糊半径   | 2      |
| `flood-color`   | 阴影颜色   | #000   |
| `flood-opacity` | 阴影透明度 | 1      |

### 内阴影模拟

**feComposite 实现内阴影**
```html
<filter id="inner-shadow">
  <feOffset dx="0" dy="2">
    <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.5" />
  </feOffset>
  <feComposite operator="out" in="SourceGraphic" />
  <feComposite operator="in" in2="SourceAlpha" />
  <feComposite operator="over" in="SourceGraphic" />
</filter>
```

---

## feColorMatrix 颜色矩阵

**feColorMatrix 颜色矩阵变换**
`<feColorMatrix [in="<输入>"] type="<matrix | saturate | hueRotate | luminanceToAlpha>" values="<矩阵值或参数>" [result="<输出名>"] />`

### matrix 自定义矩阵

**4x5 矩阵变换 RGBA**
```html
<filter id="grayscale">
  <feColorMatrix
    type="matrix"
    values="0.3 0.59 0.11 0 0
            0.3 0.59 0.11 0 0
            0.3 0.59 0.11 0 0
            0   0    0    1 0"
  />
</filter>
```

每个像素的 RGBA 按矩阵相乘:`R' = 0.3R + 0.59G + 0.11B + 0A + 0`,得到灰度。

### type 预设类型

| 值                 | 说明                               |
| ------------------ | ---------------------------------- |
| `matrix`           | 自定义矩阵                         |
| `saturate`         | 饱和度(0=灰度,1=原色,2=高饱和) |
| `hueRotate`        | 色相旋转(度)                     |
| `luminanceToAlpha` | 亮度转透明度                       |

**saturate 饱和度**
```html
<filter id="saturate">
  <feColorMatrix type="saturate" values="2" />
</filter>
```

**hueRotate 色相旋转**
```html
<filter id="hue-rotate">
  <feColorMatrix type="hueRotate" values="90" />
</filter>
```

---

## feComponentTransfer 通道映射

**feComponentTransfer 通道函数**
`<feComponentTransfer [in="<输入>"] [result="<输出名>"]><feFuncR type="<类型>" ... /><feFuncG ... /><feFuncB ... /><feFuncA ... /></feComponentTransfer>`
```html
<filter id="brightness">
  <feComponentTransfer>
    <feFuncR type="linear" slope="1.5" intercept="0" />
    <feFuncG type="linear" slope="1.5" intercept="0" />
    <feFuncB type="linear" slope="1.5" intercept="0" />
  </feComponentTransfer>
</filter>
```

| 函数              | 说明                            |
| ----------------- | ------------------------------- |
| `feFuncR/G/B/A`   | 通道函数                        |
| `type="linear"`   | 线性:`y = slope*x + intercept` |
| `type="table"`    | 表格查找                        |
| `type="discrete"` | 阶梯量化                        |
| `type="gamma"`    | 伽马校正                        |

---

## feMerge 合成

**feMerge 多滤镜结果叠加**
`<feMerge><feMergeNode in="<输入>" />...</feMerge>`
```html
<filter id="glow">
  <feGaussianBlur stdDeviation="4" result="blur" />
  <feMerge>
    <feMergeNode in="blur" />
    <feMergeNode in="blur" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

模糊结果叠加两次产生更强光晕,最后叠加原图,形成发光效果。

---

## 滤镜基元 result/in

**result 命名输出 / in 引用输入**
```html
<filter id="emboss">
  <feGaussianBlur in="SourceAlpha" stdDeviation="1" result="blur" />
  <feSpecularLighting
    in="blur"
    surfaceScale="3"
    specularConstant="1"
    specularExponent="20"
    lighting-color="#fff"
    result="spec"
  >
    <fePointLight x="-50" y="-50" z="200" />
  </feSpecularLighting>
  <feComposite in="spec" in2="SourceAlpha" operator="in" result="specMasked" />
  <feComposite
    in="SourceGraphic"
    in2="specMasked"
    operator="arithmetic"
    k1="0"
    k2="1"
    k3="1"
    k4="0"
  />
</filter>
```

### 内置输入

| 输入              | 含义                              |
| ----------------- | --------------------------------- |
| `SourceGraphic`   | 原始彩色图形                      |
| `SourceAlpha`     | 原始图形的 alpha 通道(黑白蒙版) |
| `BackgroundImage` | 背景图(需 `enable-background`)  |
| `Previous`        | 前一基元结果                      |
| 自定义 result     | 命名的中间结果                    |

---

## feOffset 偏移

**feOffset 位置偏移**
`<feOffset [in="<输入>"] dx="<x偏移>" dy="<y偏移>" [result="<输出名>"] />`
```html
<filter id="offset">
  <feOffset dx="10" dy="10" in="SourceAlpha" />
  <feFlood flood-color="#000" flood-opacity="0.3" />
  <feComposite operator="in" in2="SourceAlpha" />
  <feMerge>
    <feMergeNode />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

等价于 feDropShadow 的手动实现。

---

## feFlood 纯色填充

**feFlood 纯色填充区域**
`<feFlood flood-color="<颜色>" [flood-opacity="<透明度>"] [result="<输出名>"] />`
```html
<filter id="red-overlay">
  <feFlood flood-color="#d63031" flood-opacity="0.5" />
  <feComposite operator="in" in2="SourceGraphic" />
</filter>
```

将图形填充为指定颜色,配合 feComposite 可制作色彩滤镜。

---

## feSpecularLighting 光照

**feSpecularLighting 镜面光照**
`<feSpecularLighting [in="<输入>"] surfaceScale="<表面深度>" specularConstant="<常数>" specularExponent="<指数>" lighting-color="<光色>" [result="<输出名>"]><光源元素></feSpecularLighting>`
```html
<filter id="metallic">
  <feGaussianBlur in="SourceAlpha" stdDeviation="2" result="blur" />
  <feSpecularLighting
    in="blur"
    surfaceScale="5"
    specularConstant="1"
    specularExponent="20"
    lighting-color="#fff"
    result="spec"
  >
    <feDistantLight azimuth="135" elevation="45" />
  </feSpecularLighting>
  <feComposite in="spec" in2="SourceAlpha" operator="in" />
  <feComposite in="SourceGraphic" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" />
</filter>
```

### 光源元素

| 光源               | 说明                           |
| ------------------ | ------------------------------ |
| `<feDistantLight>` | 平行光,参数 azimuth/elevation |
| `<fePointLight>`   | 点光源,参数 x/y/z             |
| `<feSpotLight>`    | 聚光灯                         |

---

## feTurbulence 噪声

**feTurbulence 柏林噪声**
`<feTurbulence type="<fractalNoise | turbulence>" baseFrequency="<频率>" numOctaves="<倍频>" [seed="<种子>"] [stitchTiles="<平铺>"] [result="<输出名>"] />`
```html
<filter id="texture">
  <feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" />
  <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.2 0" />
  <feComposite operator="in" in2="SourceGraphic" />
</filter>
```

| 参数            | 说明                          |
| --------------- | ----------------------------- |
| `type`          | `fractalNoise` / `turbulence` |
| `baseFrequency` | 频率(越大颗粒越细)          |
| `numOctaves`    | 倍频数(细节层次)            |
| `seed`          | 随机种子                      |
| `stitchTiles`   | 平铺缝合                      |

---

## feDisplacementMap 位移映射

**feDisplacementMap 像素位移**
`<feDisplacementMap [in="<输入图>"] in2="<位移图>" scale="<位移幅度>" xChannelSelector="<R|G|B|A>" yChannelSelector="<R|G|B|A>" [result="<输出名>"] />`
```html
<filter id="ripple">
  <feTurbulence type="turbulence" baseFrequency="0.02" numOctaves="2" result="noise" />
  <feDisplacementMap
    in="SourceGraphic"
    in2="noise"
    scale="20"
    xChannelSelector="R"
    yChannelSelector="G"
  />
</filter>
```

`scale=20` 表示根据噪声 R/G 通道值最大位移 20 像素。

---

## feComposite 合成

**feComposite 像素合成**
`<feComposite [in="<输入1>"] in2="<输入2>" operator="<运算符>" [k1="<k1>"] [k2="<k2>"] [k3="<k3>"] [k4="<k4>"] [result="<输出名>"] />`

| operator 值  | 说明                  |
| ------------ | --------------------- |
| `over`       | 默认,覆盖            |
| `in`         | 交集                  |
| `out`        | 差集                  |
| `atop`       | 在...之上(仅交集)   |
| `xor`        | 异或                  |
| `arithmetic` | 算术运算(k1/k2/k3/k4) |

---

## 滤镜组合示例

### 霓虹发光

**feGaussianBlur + feColorMatrix + feMerge**
```html
<filter id="neon" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="4" result="blur1" />
  <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur2" />
  <feColorMatrix
    in="blur1"
    type="matrix"
    values="0 0 0 0 0.3
                         0 0 0 0 0.4
                         0 0 0 0 1
                         0 0 0 1.5 0"
    result="glow1"
  />
  <feColorMatrix
    in="blur2"
    type="matrix"
    values="0 0 0 0 0.3
                         0 0 0 0 0.4
                         0 0 0 0 1
                         0 0 0 0.8 0"
    result="glow2"
  />
  <feMerge>
    <feMergeNode in="glow2" />
    <feMergeNode in="glow1" />
    <feMergeNode in="SourceGraphic" />
  </feMerge>
</filter>
```

### 玻璃磨砂

**feGaussianBlur + feColorMatrix 半透明**
```html
<filter id="frosted-glass">
  <feGaussianBlur stdDeviation="5" />
  <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.8 0.1" />
</filter>
```

---

## 综合示例:玻璃质感卡片

**filter + linearGradient 组合**
```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="bg" x1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <filter id="card-shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.2" />
    </filter>
    <filter id="card-glow">
      <feGaussianBlur stdDeviation="2" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <rect width="400" height="200" fill="url(#bg)" />
  <rect
    x="60"
    y="40"
    width="280"
    height="120"
    rx="16"
    fill="#fff"
    fill-opacity="0.15"
    filter="url(#card-shadow)"
  />
  <text
    x="200"
    y="100"
    text-anchor="middle"
    font-size="24"
    fill="#fff"
    font-weight="bold"
    filter="url(#card-glow)"
  >
    Glass Card
  </text>
</svg>
```

<!-- ============ 文档分隔线：012-svg/011-SVGClipMask.md ============ -->

## 1. clipPath 裁剪路径

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

### 1.1 clipPathUnits 坐标系

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

### 1.2 文字裁剪

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

### 1.3 多形状裁剪

```html
<clipPath id="holes">
  <circle cx="50" cy="50" r="30" />
  <circle cx="150" cy="50" r="30" />
  <circle cx="250" cy="50" r="30" />
</clipPath>
<rect width="300" height="100" fill="#4f5bd5" clip-path="url(#holes)" />
<!-- 出现三个圆形填充 -->
```

## 2. mask 蒙版

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

### 2.1 蒙版颜色规则

| 蒙版颜色     | 效果     |
| ------------ | -------- |
| `#fff`（白） | 完全显示 |
| `#000`（黑） | 完全隐藏 |
| `#888`（灰） | 半透明   |
| 渐变白→黑    | 渐隐     |

### 2.2 maskUnits / maskContentUnits

| 属性               | 说明                                      |
| ------------------ | ----------------------------------------- |
| `maskUnits`        | mask 区域坐标系（默认 objectBoundingBox） |
| `maskContentUnits` | 蒙版内容坐标系（默认 userSpaceOnUse）     |

```html
<mask id="m" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
  <rect width="200" height="200" fill="#fff" />
</mask>
```

### 2.3 mask-type 蒙版类型

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

## 3. clipPath vs mask 对比

| 维度     | clipPath               | mask                     |
| -------- | ---------------------- | ------------------------ |
| 边缘     | 硬边（无过渡）         | 软边（可渐变）           |
| 计算依据 | 几何形状               | 像素亮度/alpha           |
| 半透明   | 不支持                 | 支持                     |
| 性能     | 较优                   | 较重                     |
| 典型场景 | 头像圆形裁剪、文字镂空 | 渐隐、淡入淡出、复杂透明 |

## 4. 圆形头像

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

## 5. 渐隐遮罩

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

## 6. 文字渐变蒙版

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

## 7. 反射倒影

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

## 8. clipPath 动画

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

## 9. mask 动画

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

## 10. 多重裁剪

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

## 11. 实战：粒子头像

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

## 12. 性能建议

| 优化           | 说明                               |
| -------------- | ---------------------------------- |
| 优先 clipPath  | 硬裁剪性能优于软蒙版               |
| 缩小 mask 区域 | mask x/y/width/height 限制计算范围 |
| 避免大图蒙版   | 高分辨率图像 + mask 会显著拖慢渲染 |
| 缓存复用       | 多个元素复用同一 mask 定义         |

下一篇介绍 symbol/use 的图形复用机制。
## clipPath 裁剪路径

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

### clipPathUnits 坐标系

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

### 文字裁剪

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

### 多形状裁剪

**clipPath 包含多个形状**
```html
<clipPath id="holes">
  <circle cx="50" cy="50" r="30" />
  <circle cx="150" cy="50" r="30" />
  <circle cx="250" cy="50" r="30" />
</clipPath>
<rect width="300" height="100" fill="#4f5bd5" clip-path="url(#holes)" />
```

### clip-path 应用属性

**clip-path 引用裁剪路径**
`clip-path="url(#<clipPath-id>)"`
```html
<rect width="200" height="200" fill="#4f5bd5" clip-path="url(#circle-clip)" />
```

---

## mask 蒙版

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

### 蒙版颜色规则

| 蒙版颜色     | 效果     |
| ------------ | -------- |
| `#fff`(白) | 完全显示 |
| `#000`(黑) | 完全隐藏 |
| `#888`(灰) | 半透明   |
| 渐变白->黑  | 渐隐     |

### maskUnits / maskContentUnits

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

### mask-type 蒙版类型

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

### mask 应用属性

**mask 引用蒙版**
`mask="url(#<mask-id>)"`
```html
<rect width="200" height="200" fill="#4f5bd5" mask="url(#fade)" />
```

---

## clipPath 与 mask 对比

| 维度     | clipPath               | mask                     |
| -------- | ---------------------- | ------------------------ |
| 边缘     | 硬边(无过渡)         | 软边(可渐变)           |
| 计算依据 | 几何形状               | 像素亮度/alpha           |
| 半透明   | 不支持                 | 支持                     |
| 典型场景 | 头像圆形裁剪、文字镂空 | 渐隐、淡入淡出、复杂透明 |

---

## 圆形头像裁剪

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

## 渐隐遮罩

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

## 文字渐变蒙版

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

## 反射倒影

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

## clipPath 动画

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

## mask 动画

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

## 多重裁剪

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

## 综合示例:粒子头像

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

<!-- ============ 文档分隔线：012-svg/012-SVGSymbolReuse.md ============ -->

## 1. 为什么要复用

重复代码会带来体积膨胀、维护困难、不一致风险。SVG 提供三种复用机制：

| 机制                  | 用途                       |
| --------------------- | -------------------------- |
| `<defs>` + `url(#id)` | 复用渐变、滤镜、图案等资源 |
| `<symbol>` + `<use>`  | 复用图形，适合图标系统     |
| `<use>` 直接引用      | 复用任意已存在元素         |

## 2. defs 定义资源

`<defs>` 内的元素不直接渲染，通过 `url(#id)` 引用。

```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="brand" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.3" />
    </filter>
  </defs>
  <rect x="20" y="20" width="160" height="80" rx="8" fill="url(#brand)" filter="url(#shadow)" />
  <circle cx="280" cy="60" r="40" fill="url(#brand)" filter="url(#shadow)" />
</svg>
```

## 3. use 引用元素

`<use>` 复制并实例化任意元素（包括 `<g>`、`<symbol>`、单个图形）。

```html
<svg viewBox="0 0 300 100">
  <defs>
    <g id="star">
      <polygon
        points="50,10 60,40 90,40 65,55 75,85 50,65 25,85 35,55 10,40 40,40"
        fill="#f9a825"
      />
    </g>
  </defs>
  <use href="#star" />
  <use href="#star" x="100" />
  <use href="#star" x="200" />
</svg>
```

### 3.1 关键属性

| 属性            | 说明                                          |
| --------------- | --------------------------------------------- |
| `href`          | 引用目标（SVG 2 推荐使用，替代 `xlink:href`） |
| `x, y`          | 实例位置偏移                                  |
| `width, height` | 仅对 `<symbol>` 生效                          |
| `transform`     | 应用变换                                      |

### 3.2 跨文件引用

```html
<svg>
  <use href="icons.svg#icon-home" width="24" height="24" />
</svg>
```

> 跨文件引用存在缓存与跨域限制，且无法被外部 CSS 样式化（shadow DOM 行为）。生产环境常用 inline sprite。

## 4. symbol 符号

`<symbol>` 类似 `<g>`，但自带 `viewBox`，适合定义可缩放的图标模板。

```html
<svg style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path
      d="M3 12 L12 3 L21 12 M5 10 V21 H19 V10"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24">
    <circle cx="12" cy="8" r="4" fill="currentColor" />
    <path
      d="M4 20 C4 16 8 14 12 14 C16 14 20 16 20 20"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
    />
  </symbol>
</svg>

<svg width="24" height="24"><use href="#icon-home" /></svg>
<svg width="48" height="48"><use href="#icon-user" /></svg>
```

### 4.1 symbol vs g

| 维度          | `<g>`       | `<symbol>`             |
| ------------- | ----------- | ---------------------- |
| 直接渲染      | 是          | 否                     |
| 自带 viewBox  | 否          | 是                     |
| 配合 use 尺寸 | 仅 x/y 偏移 | 支持 width/height 缩放 |
| 典型场景      | 简单分组    | 图标定义               |

### 4.2 隐藏定义

定义 symbol 的容器 SVG 必须隐藏，避免渲染空白：

```html
<!-- 方法 1：CSS -->
<svg style="display:none">...</svg>

<!-- 方法 2：aria-hidden + 0 尺寸 -->
<svg width="0" height="0" aria-hidden="true">...</svg>
```

## 5. 构建图标系统

### 5.1 Sprite 模式

将所有图标定义为 symbol，集中存放：

```html
<!-- icons.svg -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path d="M3 12 L12 3 L21 12" />
    <path d="M5 10 V21 H19 V10" />
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24">
    <circle cx="11" cy="11" r="7" />
    <line x1="16" y1="16" x2="21" y2="21" />
  </symbol>
  <!-- 更多图标 -->
</svg>
```

页面内使用：

```html
<svg class="icon"><use href="#icon-home" /></svg>
<svg class="icon"><use href="#icon-search" /></svg>
```

```css
.icon {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
}
.icon-lg {
  width: 48px;
  height: 48px;
}
```

### 5.2 主题化

`currentColor` 让图标颜色继承父元素 `color`：

```html
<nav>
  <a href="/" class="nav-link active"
    ><svg class="icon"><use href="#icon-home" /></svg> 首页</a
  >
  <a href="/search" class="nav-link"
    ><svg class="icon"><use href="#icon-search" /></svg> 搜索</a
  >
</nav>
```

```css
.nav-link {
  color: #666;
}
.nav-link:hover {
  color: #4f5bd5;
}
.nav-link.active {
  color: #4f5bd5;
}
```

悬停或激活时图标颜色自动跟随文字颜色变化。

## 6. use 的样式继承

`<use>` 实例化的元素会继承父级 CSS，但 shadow DOM 内部样式对外部 CSS 部分不可见。

```html
<style>
  .icon-primary use {
    fill: #4f5bd5;
  }
</style>

<svg class="icon-primary"><use href="#icon-star" /></svg>
```

| 属性               | 外部 CSS 是否可覆盖            |
| ------------------ | ------------------------------ |
| `fill` / `stroke`  | 是（仅当 symbol 内未显式设置） |
| `color`            | 是（通过 currentColor 联动）   |
| `width` / `height` | 是                             |
| 内部 path 的样式   | 否（shadow DOM 隔离）          |

> **最佳实践**：symbol 内部使用 `currentColor` 而非显式颜色，让外部可完全控制。

## 7. use 的局限性

### 7.1 无法单独修改内部元素

```html
<!-- symbol 定义 -->
<symbol id="card" viewBox="0 0 100 50">
  <rect width="100" height="50" fill="#4f5bd5" />
  <text x="50" y="30" text-anchor="middle" fill="#fff">CARD</text>
</symbol>

<!-- 多个实例 -->
<use href="#card" />
<use href="#card" x="120" />

<!-- 无法让第二个实例的文字变红 -->
```

### 7.2 替代方案：CSS 变量

```html
<symbol id="card" viewBox="0 0 100 50">
  <rect width="100" height="50" fill="var(--card-bg, #4f5bd5)" />
  <text x="50" y="30" text-anchor="middle" fill="var(--card-text, #fff)">CARD</text>
</symbol>

<use href="#card" style="--card-bg: #d63031; --card-text: #fff" />
<use href="#card" style="--card-bg: #00b894; --card-text: #000" />
```

CSS 变量可穿透 shadow DOM，实现实例级定制。

## 8. 复用与动画

```html
<svg viewBox="0 0 300 100">
  <defs>
    <g id="pulse-dot">
      <circle cx="0" cy="0" r="8" fill="#4f5bd5" />
      <circle cx="0" cy="0" r="8" fill="#4f5bd5" opacity="0.5">
        <animate attributeName="r" values="8;20;8" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.5;0;0.5" dur="2s" repeatCount="indefinite" />
      </circle>
    </g>
  </defs>
  <use href="#pulse-dot" x="50" y="50" />
  <use href="#pulse-dot" x="150" y="50" />
  <use href="#pulse-dot" x="250" y="50" />
</svg>
```

每个 `<use>` 实例都带有独立的动画时间轴。

## 9. use 的 transform

```html
<use href="#star" transform="translate(100, 50) rotate(15) scale(1.5)" />
```

`<use>` 的 `transform` 在实例化时应用，不修改原始定义。

## 10. 实战：状态徽章

```html
<svg style="display:none">
  <symbol id="badge" viewBox="0 0 120 32">
    <rect width="120" height="32" rx="16" fill="var(--bg, #e0e0e0)" />
    <circle cx="16" cy="16" r="4" fill="var(--dot, #999)" />
    <text x="28" y="20" font-size="14" fill="var(--text, #333)" font-family="sans-serif">状态</text>
  </symbol>
</svg>

<svg width="120" height="32">
  <use href="#badge" style="--bg: #e3f2fd; --dot: #4f5bd5; --text: #4f5bd5" />
</svg>
<svg width="120" height="32">
  <use href="#badge" style="--bg: #e8f5e9; --dot: #00b894; --text: #00b894" />
</svg>
<svg width="120" height="32">
  <use href="#badge" style="--bg: #fbe9e7; --dot: #d63031; --text: #d63031" />
</svg>
```

通过 CSS 变量复用同一徽章模板，实现不同状态颜色。

## 11. 性能考量

| 场景                 | 推荐                              |
| -------------------- | --------------------------------- |
| 少量图标（< 20）     | 内联 SVG + symbol                 |
| 大量图标（> 20）     | 外部 sprite 文件 + use 引用       |
| 频繁切换主题         | CSS 变量 + currentColor           |
| 需要单独定制内部元素 | 直接内联，避免 use 的 shadow 限制 |

## 12. 现代替代方案：Web Components

对于需要深度定制的图标系统，可考虑使用 Web Components：

```html
<icon-button name="home" size="24" color="primary"></icon-button>
```

但 SVG sprite + use 仍是性能与兼容性最优的方案，适合大多数场景。

下一篇介绍 SVG 动画，让静态图形活起来。
## 复用机制对比

| 机制                  | 用途                       |
| --------------------- | -------------------------- |
| `<defs>` + `url(#id)` | 复用渐变、滤镜、图案等资源 |
| `<symbol>` + `<use>`  | 复用图形,适合图标系统    |
| `<use>` 直接引用      | 复用任意已存在元素         |

---

## defs 定义资源

**defs 资源定义容器**
`<defs><资源定义></defs>`
```html
<svg viewBox="0 0 400 200">
  <defs>
    <linearGradient id="brand" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.3" />
    </filter>
  </defs>
  <rect x="20" y="20" width="160" height="80" rx="8" fill="url(#brand)" filter="url(#shadow)" />
  <circle cx="280" cy="60" r="40" fill="url(#brand)" filter="url(#shadow)" />
</svg>
```

`<defs>` 内的元素不直接渲染,通过 `url(#id)` 引用。

---

## use 引用元素

**use 元素引用**
`<use href="<#id或文件#id>" [x="<偏移x>"] [y="<偏移y>"] [width="<宽>"] [height="<高>"] [transform="<变换>"] />`
```html
<svg viewBox="0 0 300 100">
  <defs>
    <g id="star">
      <polygon
        points="50,10 60,40 90,40 65,55 75,85 50,65 25,85 35,55 10,40 40,40"
        fill="#f9a825"
      />
    </g>
  </defs>
  <use href="#star" />
  <use href="#star" x="100" />
  <use href="#star" x="200" />
</svg>
```

### use 关键属性

| 属性            | 说明                                          |
| --------------- | --------------------------------------------- |
| `href`          | 引用目标(SVG 2 推荐使用,替代 `xlink:href`)  |
| `x, y`          | 实例位置偏移                                  |
| `width, height` | 仅对 `<symbol>` 生效                          |
| `transform`     | 应用变换                                      |

### 跨文件引用

**use 引用外部 SVG**
```html
<svg>
  <use href="icons.svg#icon-home" width="24" height="24" />
</svg>
```

### use 的 transform

**use 应用 transform**
```html
<use href="#star" transform="translate(100, 50) rotate(15) scale(1.5)" />
```

`<use>` 的 `transform` 在实例化时应用,不修改原始定义。

---

## symbol 符号定义

**symbol 可缩放符号**
`<symbol id="<id>" viewBox="<视口>"><图形定义></symbol>`
```html
<svg style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path
      d="M3 12 L12 3 L21 12 M5 10 V21 H19 V10"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24">
    <circle cx="12" cy="8" r="4" fill="currentColor" />
    <path
      d="M4 20 C4 16 8 14 12 14 C16 14 20 16 20 20"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
    />
  </symbol>
</svg>

<svg width="24" height="24"><use href="#icon-home" /></svg>
<svg width="48" height="48"><use href="#icon-user" /></svg>
```

### symbol vs g

| 维度          | `<g>`       | `<symbol>`             |
| ------------- | ----------- | ---------------------- |
| 直接渲染      | 是          | 否                     |
| 自带 viewBox  | 否          | 是                     |
| 配合 use 尺寸 | 仅 x/y 偏移 | 支持 width/height 缩放 |
| 典型场景      | 简单分组    | 图标定义               |

### 隐藏定义容器

**隐藏 symbol 容器 SVG**
```html
<!-- 方法 1:CSS -->
<svg style="display:none">...</svg>

<!-- 方法 2:aria-hidden + 0 尺寸 -->
<svg width="0" height="0" aria-hidden="true">...</svg>
```

---

## Sprite 图标系统

**sprite 集中定义图标**
```html
<!-- icons.svg -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path d="M3 12 L12 3 L21 12" />
    <path d="M5 10 V21 H19 V10" />
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24">
    <circle cx="11" cy="11" r="7" />
    <line x1="16" y1="16" x2="21" y2="21" />
  </symbol>
</svg>
```

**使用 sprite 图标**
```html
<svg class="icon"><use href="#icon-home" /></svg>
<svg class="icon"><use href="#icon-search" /></svg>
```

```css
.icon {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
}
.icon-lg {
  width: 48px;
  height: 48px;
}
```

---

## currentColor 主题化

**currentColor 继承父级 color**
```html
<nav>
  <a href="/" class="nav-link active">
    <svg class="icon"><use href="#icon-home" /></svg> 首页
  </a>
  <a href="/search" class="nav-link">
    <svg class="icon"><use href="#icon-search" /></svg> 搜索
  </a>
</nav>
```

```css
.nav-link {
  color: #666;
}
.nav-link:hover {
  color: #4f5bd5;
}
.nav-link.active {
  color: #4f5bd5;
}
```

`currentColor` 让图标颜色继承父元素 `color`,悬停或激活时图标颜色自动跟随文字颜色变化。

---

## use 样式继承

**use 实例化的样式继承**
```html
<style>
  .icon-primary use {
    fill: #4f5bd5;
  }
</style>

<svg class="icon-primary"><use href="#icon-star" /></svg>
```

### 外部 CSS 可覆盖性

| 属性               | 外部 CSS 是否可覆盖            |
| ------------------ | ------------------------------ |
| `fill` / `stroke`  | 是(仅当 symbol 内未显式设置) |
| `color`            | 是(通过 currentColor 联动)   |
| `width` / `height` | 是                             |
| 内部 path 的样式   | 否(shadow DOM 隔离)          |

---

## CSS 变量穿透 use

**CSS 变量穿透 shadow DOM**
```html
<symbol id="card" viewBox="0 0 100 50">
  <rect width="100" height="50" fill="var(--card-bg, #4f5bd5)" />
  <text x="50" y="30" text-anchor="middle" fill="var(--card-text, #fff)">CARD</text>
</symbol>

<use href="#card" style="--card-bg: #d63031; --card-text: #fff" />
<use href="#card" style="--card-bg: #00b894; --card-text: #000" />
```

CSS 变量可穿透 shadow DOM,实现实例级定制。

---

## use 复用动画

**use 实例化带动画的元素**
```html
<svg viewBox="0 0 300 100">
  <defs>
    <g id="pulse-dot">
      <circle cx="0" cy="0" r="8" fill="#4f5bd5" />
      <circle cx="0" cy="0" r="8" fill="#4f5bd5" opacity="0.5">
        <animate attributeName="r" values="8;20;8" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.5;0;0.5" dur="2s" repeatCount="indefinite" />
      </circle>
    </g>
  </defs>
  <use href="#pulse-dot" x="50" y="50" />
  <use href="#pulse-dot" x="150" y="50" />
  <use href="#pulse-dot" x="250" y="50" />
</svg>
```

每个 `<use>` 实例都带有独立的动画时间轴。

---

## 综合示例:状态徽章

**symbol + CSS 变量状态徽章**
```html
<svg style="display:none">
  <symbol id="badge" viewBox="0 0 120 32">
    <rect width="120" height="32" rx="16" fill="var(--bg, #e0e0e0)" />
    <circle cx="16" cy="16" r="4" fill="var(--dot, #999)" />
    <text x="28" y="20" font-size="14" fill="var(--text, #333)" font-family="sans-serif">状态</text>
  </symbol>
</svg>

<svg width="120" height="32">
  <use href="#badge" style="--bg: #e3f2fd; --dot: #4f5bd5; --text: #4f5bd5" />
</svg>
<svg width="120" height="32">
  <use href="#badge" style="--bg: #e8f5e9; --dot: #00b894; --text: #00b894" />
</svg>
<svg width="120" height="32">
  <use href="#badge" style="--bg: #fbe9e7; --dot: #d63031; --text: #d63031" />
</svg>
```

通过 CSS 变量复用同一徽章模板,实现不同状态颜色。

<!-- ============ 文档分隔线：012-svg/013-SVGAnimationBasics.md ============ -->

## 1. SVG 动画方案对比

| 方案           | 说明                                          | 优势                    | 劣势                           |
| -------------- | --------------------------------------------- | ----------------------- | ------------------------------ |
| **SMIL**       | `<animate>`、`<animateTransform>` 等 SVG 原生 | 无需 JS、声明式、跨文档 | Chrome 曾废弃后恢复；IE 不支持 |
| **CSS**        | `@keyframes` + `transform`                    | 浏览器优化好、生态成熟  | 仅限 CSS 可控属性              |
| **JavaScript** | requestAnimationFrame + DOM 操作              | 灵活、可做复杂逻辑      | 性能消耗大、需手动优化         |

## 2. SMIL animate

`<animate>` 在指定时间内变化某个属性值。

```html
<svg viewBox="0 0 200 100">
  <rect x="10" y="40" width="40" height="20" fill="#4f5bd5">
    <animate attributeName="x" from="10" to="150" dur="2s" repeatCount="indefinite" />
  </rect>
</svg>
```

### 2.1 关键属性

| 属性            | 说明                                            |
| --------------- | ----------------------------------------------- |
| `attributeName` | 要变化的属性名                                  |
| `from / to`     | 起始/结束值                                     |
| `values`        | 关键帧值列表（分号分隔）                        |
| `dur`           | 持续时间（如 `2s`、`500ms`）                    |
| `repeatCount`   | 重复次数（数字或 `indefinite`）                 |
| `begin`         | 开始时间（如 `1s`、`click`）                    |
| `end`           | 结束条件                                        |
| `fill`          | 动画结束行为：`freeze` 保留终值 / `remove` 还原 |
| `calcMode`      | 插值模式：linear / paced / spline / discrete    |

### 2.2 values 关键帧

```html
<circle cx="50" cy="50" r="20" fill="#4f5bd5">
  <animate
    attributeName="cx"
    values="50;150;100;50"
    keyTimes="0;0.5;0.8;1"
    dur="4s"
    repeatCount="indefinite"
  />
</circle>
```

- `values`：关键帧值
- `keyTimes`：对应时间点（0-1，必须从 0 开始到 1 结束）

### 2.3 calcMode 插值模式

| 值               | 说明                            |
| ---------------- | ------------------------------- |
| `linear`（默认） | 线性插值                        |
| `paced`          | 按距离等分（适合路径）          |
| `spline`         | 贝塞尔曲线（配合 `keySplines`） |
| `discrete`       | 离散切换（无过渡）              |

```html
<animate
  attributeName="cx"
  values="50;150;50"
  keyTimes="0;0.5;1"
  keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"
  calcMode="spline"
  dur="2s"
  repeatCount="indefinite"
/>
```

`keySplines` 类似 CSS `cubic-bezier`，控制每段时间的缓动曲线。

## 3. animateTransform

`<animateTransform>` 专用于 `transform` 属性动画。

```html
<rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5">
  <animateTransform
    attributeName="transform"
    type="rotate"
    from="0 0 0"
    to="360 0 0"
    dur="4s"
    repeatCount="indefinite"
  />
</rect>
```

### 3.1 type 类型

| 值                | 说明                               |
| ----------------- | ---------------------------------- |
| `translate`       | 平移                               |
| `rotate`          | 旋转（需指定中心 `from="0 cx cy"`) |
| `scale`           | 缩放                               |
| `skewX` / `skewY` | 倾斜                               |

### 3.2 多变换叠加

```html
<g>
  <animateTransform
    attributeName="transform"
    type="translate"
    values="0 0; 100 0; 0 0"
    dur="4s"
    repeatCount="indefinite"
    additive="sum"
  />
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="0; 360"
    dur="2s"
    repeatCount="indefinite"
    additive="sum"
  />
  <rect x="-20" y="-20" width="40" height="40" fill="#4f5bd5" />
</g>
```

`additive="sum"` 让多个 animateTransform 共同作用。

## 4. animateMotion 路径动画

`<animateMotion>` 让元素沿指定路径运动。

```html
<svg viewBox="0 0 300 200">
  <path id="motion-path" d="M 20 100 Q 150 20 280 100" fill="none" stroke="#ccc" />
  <circle r="10" fill="#4f5bd5">
    <animateMotion dur="3s" repeatCount="indefinite">
      <mpath href="#motion-path" />
    </animateMotion>
  </circle>
</svg>
```

### 4.1 path 属性内联

```html
<circle r="8" fill="#d63031">
  <animateMotion path="M 0 0 L 100 0 L 100 100 L 0 100 Z" dur="4s" repeatCount="indefinite" />
</circle>
```

### 4.2 rotate 自动朝向

```html
<g>
  <polygon points="0,-10 15,0 0,10" fill="#4f5bd5" />
  <animateMotion dur="4s" repeatCount="indefinite" rotate="auto">
    <mpath href="#motion-path" />
  </animateMotion>
</g>
```

| `rotate` 值    | 说明                 |
| -------------- | -------------------- |
| `auto`         | 元素方向跟随路径切线 |
| `auto-reverse` | 反向朝向             |
| `0`（默认）    | 不旋转               |

### 4.3 keyPoints 速度控制

```html
<animateMotion
  dur="4s"
  repeatCount="indefinite"
  keyPoints="0;0.5;1"
  keyTimes="0;0.5;1"
  calcMode="linear"
>
  <mpath href="#motion-path" />
</animateMotion>
```

`keyPoints` 控制路径位置进度（0-1），可做"快进慢出"等效果。

## 5. set 元素

`<set>` 是 `<animate>` 的简化版，用于瞬间设置属性值。

```html
<rect width="100" height="100" fill="#4f5bd5">
  <set attributeName="fill" to="#d63031" begin="2s" />
</rect>
<!-- 2 秒后突然变红 -->
```

## 6. begin 事件触发

`begin` 不仅支持时间，还支持事件触发。

```html
<svg viewBox="0 0 200 100">
  <rect id="btn" x="50" y="30" width="100" height="40" rx="8" fill="#4f5bd5" />
  <text x="100" y="55" text-anchor="middle" fill="#fff">点击</text>

  <circle cx="100" cy="50" r="0" fill="#d63031">
    <animate attributeName="r" from="0" to="80" begin="btn.click" dur="0.5s" fill="remove" />
  </circle>
</svg>
```

`begin="btn.click"` 表示 btn 被点击时触发动画。

### 6.1 支持的事件

| 事件                   | 触发时机            |
| ---------------------- | ------------------- |
| `click`                | 点击                |
| `mouseover`            | 鼠标悬停            |
| `mouseout`             | 鼠标移出            |
| `focusin` / `focusout` | 获取/失去焦点       |
| `begin` / `end`        | 其他动画的开始/结束 |
| `repeat`               | 动画重复            |

### 6.2 动画链式触发

```html
<rect>
  <animate id="a1" attributeName="x" from="0" to="100" dur="1s" begin="0s" fill="freeze" />
  <animate attributeName="y" from="0" to="100" dur="1s" begin="a1.end" fill="freeze" />
</rect>
```

第二个动画在第一个动画结束时启动。

## 7. CSS 动画

CSS 动画同样适用于 SVG，但需注意属性差异。

```html
<style>
  .spinner {
    transform-origin: center;
    transform-box: fill-box;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .pulse {
    animation: pulse 2s ease-in-out infinite;
  }
  @keyframes pulse {
    0%,
    100% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.2);
    }
  }
</style>

<svg viewBox="0 0 100 100">
  <circle class="spinner" cx="50" cy="50" r="20" fill="#4f5bd5" />
  <circle class="pulse" cx="50" cy="50" r="10" fill="#d63031" />
</svg>
```

### 7.1 transform-box 必要性

SVG 元素默认 `transform-origin` 以 viewBox 原点为参考。设置 `transform-box: fill-box` 让 transform-origin 以元素边界框为参考。

```css
.spinner {
  transform-origin: center;
  transform-box: fill-box;
}
```

### 7.2 CSS 动画可控制的属性

| 类别                 | 示例                               |
| -------------------- | ---------------------------------- |
| 几何属性（部分支持） | `cx`、`cy`、`r`、`width`、`height` |
| 颜色属性             | `fill`、`stroke`、`stop-color`     |
| 透明度               | `opacity`、`fill-opacity`          |
| 变换                 | `transform`                        |
| 滤镜                 | `filter`                           |

> 现代浏览器支持 CSS 动画 SVG 几何属性，但兼容性需验证。

## 8. JavaScript 动画

```javascript
const circle = document.querySelector('circle');
let start = null;

function animate(timestamp) {
  if (!start) start = timestamp;
  const progress = ((timestamp - start) / 2000) % 1;
  circle.setAttribute('cx', 50 + progress * 100);
  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

### 8.1 Web Animations API

```javascript
const rect = document.querySelector('rect');
rect.animate([{ transform: 'translateX(0)' }, { transform: 'translateX(200px)' }], {
  duration: 2000,
  iterations: Infinity,
  easing: 'ease-in-out',
});
```

WAAPI 性能接近 CSS 动画，且更灵活。

## 9. 性能优化

### 9.1 优先级

1. **CSS transform/opacity**（GPU 加速）
2. **SMIL**（声明式，浏览器优化）
3. **JavaScript + requestAnimationFrame**（最灵活但开销大）

### 9.2 will-change 提示

```css
.animated-element {
  will-change: transform;
}
```

提示浏览器将元素提升为独立图层，避免重绘整个 SVG。

### 9.3 避免布局抖动

```javascript
// 错误：每次读取 offsetWidth 触发布局
function animate() {
  const x = element.offsetWidth;
  element.style.transform = `translateX(${x + 1}px)`;
  requestAnimationFrame(animate);
}

// 正确：用变量缓存
let x = 0;
function animate() {
  x += 1;
  element.style.transform = `translateX(${x}px)`;
  requestAnimationFrame(animate);
}
```

## 10. 实战：加载动画

```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <g class="spinner">
    <circle cx="50" cy="50" r="40" fill="none" stroke="#e0e0e0" stroke-width="6" />
    <circle
      cx="50"
      cy="50"
      r="40"
      fill="none"
      stroke="#4f5bd5"
      stroke-width="6"
      stroke-linecap="round"
      stroke-dasharray="60 200"
    />
  </g>
  <style>
    .spinner {
      transform-origin: center;
      transform-box: fill-box;
      animation: spin 1.2s linear infinite;
    }
    @keyframes spin {
      to {
        transform: rotate(360deg);
      }
    }
  </style>
</svg>
```

**原理**：dasharray "60 200" 让圆只显示 60 长度的弧，整体旋转形成加载圈。

## 11. 实战：路径绘制动画

```html
<svg viewBox="0 0 200 100">
  <path
    d="M 10 50 Q 100 10 190 50"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="3"
    stroke-dasharray="220"
    stroke-dashoffset="220"
  >
    <animate attributeName="stroke-dashoffset" from="220" to="0" dur="2s" fill="freeze" />
  </path>
</svg>
```

**步骤**：

1. `getTotalLength()` 获取路径长度（约 220）
2. `stroke-dasharray` 设为路径总长
3. `stroke-dashoffset` 从总长到 0，模拟"画线"

## 12. 浏览器兼容

| 特性                 | Chrome | Firefox | Safari | Edge |
| -------------------- | ------ | ------- | ------ | ---- |
| SMIL                 | √      | √       | √      | √    |
| CSS transform on SVG | √      | √       | √      | √    |
| CSS 动画几何属性     | √ 90+  | √       | √      | √    |
| WAAPI on SVG         | √      | √       | √      | √    |

> SMIL 曾被 Chrome 计划废弃，但因社区反馈已恢复并稳定支持。

下一篇介绍 CSS 样式化 SVG 的完整方案。
## SVG 动画方案对比

| 方案           | 说明                                          | 优势                    | 劣势                           |
| -------------- | --------------------------------------------- | ----------------------- | ------------------------------ |
| **SMIL**       | `<animate>`、`<animateTransform>` 等 SVG 原生 | 无需 JS、声明式、跨文档 | Chrome 曾废弃后恢复;IE 不支持 |
| **CSS**        | `@keyframes` + `transform`                    | 浏览器优化好、生态成熟  | 仅限 CSS 可控属性              |
| **JavaScript** | requestAnimationFrame + DOM 操作              | 灵活、可做复杂逻辑      | 性能消耗大、需手动优化         |

---

## animate 属性动画

**animate SMIL 属性动画**
`<animate attributeName="<属性名>" [from="<起始值>"] [to="<结束值>"] [values="<关键帧值列表>"] dur="<时长>" [begin="<开始>"] [end="<结束>"] [repeatCount="<重复>"] [fill="<freeze|remove>"] [calcMode="<插值模式>"] [keyTimes="<时间点>"] [keySplines="<贝塞尔>"] />`
```html
<svg viewBox="0 0 200 100">
  <rect x="10" y="40" width="40" height="20" fill="#4f5bd5">
    <animate attributeName="x" from="10" to="150" dur="2s" repeatCount="indefinite" />
  </rect>
</svg>
```

### animate 关键属性

| 属性            | 说明                                            |
| --------------- | ----------------------------------------------- |
| `attributeName` | 要变化的属性名                                  |
| `from / to`     | 起始/结束值                                     |
| `values`        | 关键帧值列表(分号分隔)                        |
| `dur`           | 持续时间(如 `2s`、`500ms`)                    |
| `repeatCount`   | 重复次数(数字或 `indefinite`)                 |
| `begin`         | 开始时间(如 `1s`、`click`)                    |
| `end`           | 结束条件                                        |
| `fill`          | 动画结束行为:`freeze` 保留终值 / `remove` 还原 |
| `calcMode`      | 插值模式:linear / paced / spline / discrete    |

### values 关键帧

**values + keyTimes 多关键帧**
```html
<circle cx="50" cy="50" r="20" fill="#4f5bd5">
  <animate
    attributeName="cx"
    values="50;150;100;50"
    keyTimes="0;0.5;0.8;1"
    dur="4s"
    repeatCount="indefinite"
  />
</circle>
```

- `values`:关键帧值
- `keyTimes`:对应时间点(0-1,必须从 0 开始到 1 结束)

### calcMode 插值模式

| 值               | 说明                            |
| ---------------- | ------------------------------- |
| `linear`(默认) | 线性插值                        |
| `paced`          | 按距离等分(适合路径)          |
| `spline`         | 贝塞尔曲线(配合 `keySplines`) |
| `discrete`       | 离散切换(无过渡)              |

**spline 贝塞尔缓动**
```html
<animate
  attributeName="cx"
  values="50;150;50"
  keyTimes="0;0.5;1"
  keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"
  calcMode="spline"
  dur="2s"
  repeatCount="indefinite"
/>
```

`keySplines` 类似 CSS `cubic-bezier`,控制每段时间的缓动曲线。

---

## animateTransform 变换动画

**animateTransform transform 属性动画**
`<animateTransform attributeName="transform" type="<变换类型>" [from="<起始值>"] [to="<结束值>"] [values="<关键帧>"] dur="<时长>" [repeatCount="<重复>"] [additive="<sum|replace>"] [accumulate="<sum|none>"] />`
```html
<rect x="-25" y="-25" width="50" height="50" fill="#4f5bd5">
  <animateTransform
    attributeName="transform"
    type="rotate"
    from="0 0 0"
    to="360 0 0"
    dur="4s"
    repeatCount="indefinite"
  />
</rect>
```

### type 变换类型

| 值                | 说明                               |
| ----------------- | ---------------------------------- |
| `translate`       | 平移                               |
| `rotate`          | 旋转(需指定中心 `from="0 cx cy"`) |
| `scale`           | 缩放                               |
| `skewX` / `skewY` | 倾斜                               |

### additive 多变换叠加

**additive="sum" 多变换共同作用**
```html
<g>
  <animateTransform
    attributeName="transform"
    type="translate"
    values="0 0; 100 0; 0 0"
    dur="4s"
    repeatCount="indefinite"
    additive="sum"
  />
  <animateTransform
    attributeName="transform"
    type="rotate"
    values="0; 360"
    dur="2s"
    repeatCount="indefinite"
    additive="sum"
  />
  <rect x="-20" y="-20" width="40" height="40" fill="#4f5bd5" />
</g>
```

`additive="sum"` 让多个 animateTransform 叠加,否则后一个会覆盖前一个。

---

## animateMotion 路径动画

**animateMotion 沿路径运动**
`<animateMotion [path="<路径d>"] [dur="<时长>"] [repeatCount="<重复>"] [rotate="<auto|auto-reverse|0>"] [keyPoints="<路径进度>"] [keyTimes="<时间点>"] [calcMode="<模式>"]><mpath href="<#路径id>" /></animateMotion>`
```html
<svg viewBox="0 0 300 200">
  <path id="motion-path" d="M 20 100 Q 150 20 280 100" fill="none" stroke="#ccc" />
  <circle r="10" fill="#4f5bd5">
    <animateMotion dur="3s" repeatCount="indefinite">
      <mpath href="#motion-path" />
    </animateMotion>
  </circle>
</svg>
```

### path 属性内联

**path 内联路径**
```html
<circle r="8" fill="#d63031">
  <animateMotion path="M 0 0 L 100 0 L 100 100 L 0 100 Z" dur="4s" repeatCount="indefinite" />
</circle>
```

### rotate 自动朝向

**rotate 跟随路径切线**
```html
<g>
  <polygon points="0,-10 15,0 0,10" fill="#4f5bd5" />
  <animateMotion dur="4s" repeatCount="indefinite" rotate="auto">
    <mpath href="#motion-path" />
  </animateMotion>
</g>
```

| `rotate` 值    | 说明                 |
| -------------- | -------------------- |
| `auto`         | 元素方向跟随路径切线 |
| `auto-reverse` | 反向朝向             |
| `0`(默认)    | 不旋转               |

### keyPoints 速度控制

**keyPoints 路径进度控制**
```html
<animateMotion
  dur="4s"
  repeatCount="indefinite"
  keyPoints="0;0.5;1"
  keyTimes="0;0.5;1"
  calcMode="linear"
>
  <mpath href="#motion-path" />
</animateMotion>
```

`keyPoints` 控制路径位置进度(0-1),可做"快进慢出"等效果。

---

## set 元素

**set 瞬间设置属性值**
`<set attributeName="<属性名>" to="<值>" begin="<时间或事件>" />`
```html
<rect width="100" height="100" fill="#4f5bd5">
  <set attributeName="fill" to="#d63031" begin="2s" />
</rect>
<!-- 2 秒后突然变红 -->
```

`<set>` 是 `<animate>` 的简化版,用于瞬间设置属性值,无过渡。

---

## begin 事件触发

**begin 事件触发动画**
`begin="<元素id>.<事件>"` 或 `begin="<时间>"`
```html
<svg viewBox="0 0 200 100">
  <rect id="btn" x="50" y="30" width="100" height="40" rx="8" fill="#4f5bd5" />
  <text x="100" y="55" text-anchor="middle" fill="#fff">点击</text>

  <circle cx="100" cy="50" r="0" fill="#d63031">
    <animate attributeName="r" from="0" to="80" begin="btn.click" dur="0.5s" fill="remove" />
  </circle>
</svg>
```

`begin="btn.click"` 表示 btn 被点击时触发动画。

### 支持的事件

| 事件                   | 触发时机            |
| ---------------------- | ------------------- |
| `click`                | 点击                |
| `mouseover`            | 鼠标悬停            |
| `mouseout`             | 鼠标移出            |
| `focusin` / `focusout` | 获取/失去焦点       |
| `begin` / `end`        | 其他动画的开始/结束 |
| `repeat`               | 动画重复            |

### 动画链式触发

**begin 引用其他动画结束**
```html
<rect>
  <animate id="a1" attributeName="x" from="0" to="100" dur="1s" begin="0s" fill="freeze" />
  <animate attributeName="y" from="0" to="100" dur="1s" begin="a1.end" fill="freeze" />
</rect>
```

第二个动画在第一个动画结束时启动(`begin="a1.end"`)。

---

## CSS 动画

**@keyframes + transform SVG 动画**
```html
<style>
  .spinner {
    transform-origin: center;
    transform-box: fill-box;
    animation: spin 2s linear infinite;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .pulse {
    animation: pulse 2s ease-in-out infinite;
  }
  @keyframes pulse {
    0%,
    100% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.2);
    }
  }
</style>

<svg viewBox="0 0 100 100">
  <circle class="spinner" cx="50" cy="50" r="20" fill="#4f5bd5" />
  <circle class="pulse" cx="50" cy="50" r="10" fill="#d63031" />
</svg>
```

### transform-box 必要性

**transform-box: fill-box 元素边界框为参考**
```css
.spinner {
  transform-origin: center;
  transform-box: fill-box;
}
```

SVG 元素默认 `transform-origin` 以 viewBox 原点为参考。设置 `transform-box: fill-box` 让 transform-origin 以元素边界框为参考。

### CSS 动画可控制的属性

| 类别                 | 示例                               |
| -------------------- | ---------------------------------- |
| 几何属性(部分支持) | `cx`、`cy`、`r`、`width`、`height` |
| 颜色属性             | `fill`、`stroke`、`stop-color`     |
| 透明度               | `opacity`、`fill-opacity`          |
| 变换                 | `transform`                        |
| 滤镜                 | `filter`                           |

---

## JavaScript 动画

**requestAnimationFrame 手动动画**
```javascript
const circle = document.querySelector('circle');
let start = null;

function animate(timestamp) {
  if (!start) start = timestamp;
  const progress = ((timestamp - start) / 2000) % 1;
  circle.setAttribute('cx', 50 + progress * 100);
  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

### Web Animations API

**element.animate WAAPI**
```javascript
const rect = document.querySelector('rect');
rect.animate([{ transform: 'translateX(0)' }, { transform: 'translateX(200px)' }], {
  duration: 2000,
  iterations: Infinity,
  easing: 'ease-in-out',
});
```

WAAPI 性能接近 CSS 动画,且更灵活。

---

## will-change 性能提示

**will-change 提示浏览器提升图层**
```css
.animated-element {
  will-change: transform;
}
```

提示浏览器将元素提升为独立图层,避免重绘整个 SVG。

---

## 综合示例:加载动画

**stroke-dasharray + CSS spin 加载圈**
```html
<svg viewBox="0 0 100 100" width="100" height="100">
  <g class="spinner">
    <circle cx="50" cy="50" r="40" fill="none" stroke="#e0e0e0" stroke-width="6" />
    <circle
      cx="50"
      cy="50"
      r="40"
      fill="none"
      stroke="#4f5bd5"
      stroke-width="6"
      stroke-linecap="round"
      stroke-dasharray="60 200"
    />
  </g>
  <style>
    .spinner {
      transform-origin: center;
      transform-box: fill-box;
      animation: spin 1.2s linear infinite;
    }
    @keyframes spin {
      to {
        transform: rotate(360deg);
      }
    }
  </style>
</svg>
```

原理:dasharray "60 200" 让圆只显示 60 长度的弧,整体旋转形成加载圈。

---

## 综合示例:路径绘制动画

**stroke-dashoffset 画线动画**
```html
<svg viewBox="0 0 200 100">
  <path
    d="M 10 50 Q 100 10 190 50"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="3"
    stroke-dasharray="220"
    stroke-dashoffset="220"
  >
    <animate attributeName="stroke-dashoffset" from="220" to="0" dur="2s" fill="freeze" />
  </path>
</svg>
```

实现步骤:
1. `getTotalLength()` 获取路径长度(约 220)
2. `stroke-dasharray` 设为路径总长
3. `stroke-dashoffset` 从总长到 0,模拟"画线"

---

## 浏览器兼容

| 特性                 | Chrome | Firefox | Safari | Edge |
| -------------------- | ------ | ------- | ------ | ---- |
| SMIL                 | 支持   | 支持    | 支持   | 支持 |
| CSS transform on SVG | 支持   | 支持    | 支持   | 支持 |
| CSS 动画几何属性     | 90+    | 支持    | 支持   | 支持 |
| WAAPI on SVG         | 支持   | 支持    | 支持   | 支持 |

<!-- ============ 文档分隔线：012-svg/014-SVGCSSStyling.md ============ -->

## 1. 样式优先级

SVG 元素的样式可通过多种方式声明，优先级从低到高：

1. 元素属性的默认值
2. 外部 CSS 样式表
3. `<style>` 内部样式
4. 元素的 `style` 属性（inline style）
5. `!important` 声明

```html
<!-- 外部 CSS -->
<link rel="stylesheet" href="svg.css" />

<svg viewBox="0 0 200 100">
  <style>
    .box {
      fill: #4f5bd5;
    } /* 内部样式 */
  </style>
  <rect class="box" width="100" height="50" fill="#d63031" />
  <!-- 元素 fill 属性优先于 class，但低于 style 属性 -->
  <rect class="box" style="fill: #00b894" width="100" height="50" />
  <!-- style 属性优先级最高 -->
</svg>
```

> **注意**：SVG 的表现属性（如 `fill="..."`）优先级**低于** CSS 规则，这是与 HTML 不同的地方。

## 2. 三种样式声明方式

### 2.1 表现属性

直接写在元素上的属性：

```html
<rect x="10" y="10" width="80" height="50" fill="#4f5bd5" stroke="#000" stroke-width="2" />
```

优势：简单直观；劣势：无法响应状态变化，难以复用。

### 2.2 内部 style 标签

```html
<svg viewBox="0 0 200 100">
  <style>
    .primary {
      fill: #4f5bd5;
      stroke: #fff;
      stroke-width: 2;
    }
    .danger {
      fill: #d63031;
    }
    text {
      font-family: sans-serif;
    }
  </style>
  <rect class="primary" x="10" y="10" width="80" height="50" />
  <rect class="danger" x="110" y="10" width="80" height="50" />
</svg>
```

### 2.3 外部 CSS

```html
<!-- svg.css -->
.rect-primary { fill: #4f5bd5; } .rect-danger { fill: #d63031; }
```

```html
<link rel="stylesheet" href="svg.css" />
<svg viewBox="0 0 200 100">
  <rect class="rect-primary" width="100" height="50" />
</svg>
```

> 外部 CSS 仅在内联 SVG 或 `<object>` 嵌入时生效；`<img>` 引用的 SVG 无法被外部 CSS 样式化。

## 3. CSS 可控制的 SVG 属性

| 类别         | 属性                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| 填充         | `fill`、`fill-opacity`、`fill-rule`                                                                                      |
| 描边         | `stroke`、`stroke-width`、`stroke-opacity`、`stroke-linecap`、`stroke-linejoin`、`stroke-dasharray`、`stroke-dashoffset` |
| 几何（部分） | `cx`、`cy`、`r`、`x`、`y`、`width`、`height`                                                                             |
| 文本         | `font-family`、`font-size`、`font-weight`、`text-anchor`、`letter-spacing`                                               |
| 视觉         | `opacity`、`visibility`、`display`、`filter`、`clip-path`、`mask`                                                        |
| 变换         | `transform`、`transform-origin`、`transform-box`                                                                         |
| 其他         | `color`、`cursor`、`pointer-events`                                                                                      |

### 3.1 示例

```css
.icon {
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.icon-primary {
  color: #4f5bd5;
}
.icon-danger {
  color: #d63031;
}
.icon-lg {
  width: 48px;
  height: 48px;
}
```

```html
<svg class="icon icon-primary icon-lg" viewBox="0 0 24 24">
  <path d="M3 12 L12 3 L21 12 M5 10 V21 H19 V10" />
</svg>
```

## 4. CSS 变量

SVG 完全支持 CSS 自定义属性，实现主题化。

```html
<style>
  :root {
    --brand-primary: #4f5bd5;
    --brand-secondary: #00b894;
    --brand-danger: #d63031;
  }
  .logo {
    fill: var(--brand-primary);
  }
  .accent {
    fill: var(--brand-secondary);
  }

  .dark-theme {
    --brand-primary: #8b92e8;
    --brand-secondary: #4cd9b0;
  }
</style>

<svg viewBox="0 0 200 100">
  <rect class="logo" width="100" height="50" />
  <rect class="accent" y="50" width="100" height="50" />
</svg>
```

切换父元素的 class 即可联动所有 SVG 颜色。

### 4.1 在 use 中穿透

CSS 变量可穿透 `<use>` 的 shadow DOM：

```html
<symbol id="card" viewBox="0 0 100 50">
  <rect width="100" height="50" fill="var(--card-bg)" />
  <text x="50" y="30" text-anchor="middle" fill="var(--card-text)">CARD</text>
</symbol>

<svg width="100" height="50">
  <use href="#card" style="--card-bg: #4f5bd5; --card-text: #fff" />
</svg>
```

## 5. 伪类与状态

SVG 元素支持 CSS 伪类，实现交互效果。

```css
.btn-rect {
  fill: #4f5bd5;
  transition: fill 0.2s;
  cursor: pointer;
}
.btn-rect:hover {
  fill: #6b78ea;
}
.btn-rect:active {
  fill: #3a47b8;
}
.btn-rect:focus-visible {
  outline: 2px solid #4f5bd5;
  outline-offset: 4px;
}
```

```html
<svg viewBox="0 0 200 80">
  <rect class="btn-rect" x="20" y="20" width="160" height="40" rx="20" tabindex="0" />
  <text x="100" y="44" text-anchor="middle" fill="#fff" pointer-events="none">按钮</text>
</svg>
```

### 5.1 pointer-events

```css
.label {
  pointer-events: none;
} /* 让点击穿透到下层 */
.btn {
  pointer-events: all;
} /* 显式响应事件 */
```

| 值               | 说明                    |
| ---------------- | ----------------------- |
| `none`           | 不响应事件（穿透）      |
| `all`（默认）    | 响应所有事件            |
| `fill`           | 仅填充区域响应          |
| `stroke`         | 仅描边区域响应          |
| `visiblePainted` | 可见且填充/描边区域响应 |

## 6. 媒体查询

SVG 内部支持响应式样式。

```html
<svg viewBox="0 0 400 200">
  <style>
    .title {
      font-size: 32px;
    }
    .subtitle {
      display: block;
    }

    @media (max-width: 600px) {
      .title {
        font-size: 20px;
      }
      .subtitle {
        display: none;
      }
    }

    @media (prefers-color-scheme: dark) {
      .bg {
        fill: #1a1a1a;
      }
      .text {
        fill: #fff;
      }
    }
  </style>
  <rect class="bg" width="400" height="200" fill="#fff" />
  <text class="title text" x="200" y="80" text-anchor="middle">主标题</text>
  <text class="subtitle text" x="200" y="120" text-anchor="middle">副标题</text>
</svg>
```

### 6.1 prefers-reduced-motion

```css
.animated {
  animation: spin 2s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .animated {
    animation: none;
  }
}
```

尊重用户系统偏好，禁用动画。

## 7. transition 过渡

```css
rect {
  fill: #4f5bd5;
  transition:
    fill 0.3s ease,
    transform 0.3s ease;
}
rect:hover {
  fill: #00b894;
  transform: scale(1.1);
  transform-origin: center;
  transform-box: fill-box;
}
```

可过渡的属性：颜色、opacity、transform、几何属性（部分）。

## 8. 主题切换实战

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      :root {
        --bg: #fff;
        --text: #333;
        --card-bg: #f5f5f5;
        --brand: #4f5bd5;
      }
      [data-theme='dark'] {
        --bg: #1a1a1a;
        --text: #eee;
        --card-bg: #2a2a2a;
        --brand: #8b92e8;
      }
      body {
        background: var(--bg);
        color: var(--text);
        transition:
          background 0.3s,
          color 0.3s;
      }
      .chart-bar {
        fill: var(--brand);
        transition: fill 0.3s;
      }
    </style>
  </head>
  <body data-theme="light">
    <svg viewBox="0 0 400 200">
      <rect class="chart-bar" x="20" y="50" width="40" height="150" />
      <rect class="chart-bar" x="80" y="80" width="40" height="120" />
      <rect class="chart-bar" x="140" y="20" width="40" height="180" />
    </svg>
    <button
      onclick="document.body.dataset.theme = document.body.dataset.theme === 'light' ? 'dark' : 'light'"
    >
      切换主题
    </button>
  </body>
</html>
```

切换 `data-theme` 即可联动 SVG 与全局样式。

## 9. 嵌入方式对 CSS 的影响

| 嵌入方式       | 外部 CSS | 内部 style | 表现属性 |
| -------------- | -------- | ---------- | -------- |
| inline SVG     | √        | √          | √        |
| `<object>`     | ×        | √          | √        |
| `<img>`        | ×        | √          | √        |
| CSS background | ×        | √          | √        |

> 仅 inline SVG 可被外部 CSS 完全控制，其他方式需要 SVG 文件内部自带样式。

## 10. 实战：响应式数据条

```html
<svg viewBox="0 0 400 200" class="chart">
  <style>
    .bar {
      fill: var(--bar-color, #4f5bd5);
      transition:
        fill 0.3s,
        height 0.5s;
    }
    .bar:hover {
      fill: var(--bar-hover, #00b894);
    }

    @media (prefers-color-scheme: dark) {
      .axis {
        stroke: #666;
      }
      .label {
        fill: #ccc;
      }
    }
    .axis {
      stroke: #333;
    }
    .label {
      fill: #666;
      font-size: 12px;
    }
  </style>

  <line class="axis" x1="40" y1="180" x2="380" y2="180" />
  <rect class="bar" x="60" y="50" width="40" height="130" />
  <text class="label" x="80" y="195" text-anchor="middle">Q1</text>

  <rect class="bar" x="120" y="80" width="40" height="100" />
  <text class="label" x="140" y="195" text-anchor="middle">Q2</text>

  <rect class="bar" x="180" y="20" width="40" height="160" />
  <text class="label" x="200" y="195" text-anchor="middle">Q3</text>
</svg>
```

## 11. 调试技巧

Chrome 开发者工具中：

- Elements 面板可直接编辑 SVG 属性
- Computed 标签可查看最终计算的 fill/stroke 值
- Animations 面板可调试 SVG 动画

```css
/* 调试时高亮所有 path */
path {
  stroke: red !important;
  stroke-width: 1 !important;
}
```

下一篇介绍 JavaScript 与 SVG 交互。
## 样式优先级

SVG 元素的样式可通过多种方式声明,优先级从低到高:
1. 元素属性的默认值
2. 外部 CSS 样式表
3. `<style>` 内部样式
4. 元素的 `style` 属性(inline style)
5. `!important` 声明

**样式优先级示例**
```html
<!-- 外部 CSS -->
<link rel="stylesheet" href="svg.css" />

<svg viewBox="0 0 200 100">
  <style>
    .box {
      fill: #4f5bd5;
    } /* 内部样式 */
  </style>
  <rect class="box" width="100" height="50" fill="#d63031" />
  <!-- 元素 fill 属性优先于 class,但低于 style 属性 -->
  <rect class="box" style="fill: #00b894" width="100" height="50" />
  <!-- style 属性优先级最高 -->
</svg>
```

> SVG 的表现属性(如 `fill="..."`)优先级**低于** CSS 规则,这是与 HTML 不同的地方。

---

## 三种样式声明方式

### 表现属性

**直接写在元素上的属性**
```html
<rect x="10" y="10" width="80" height="50" fill="#4f5bd5" stroke="#000" stroke-width="2" />
```

### 内部 style 标签

**SVG 内部 style 标签**
```html
<svg viewBox="0 0 200 100">
  <style>
    .primary {
      fill: #4f5bd5;
      stroke: #fff;
      stroke-width: 2;
    }
    .danger {
      fill: #d63031;
    }
    text {
      font-family: sans-serif;
    }
  </style>
  <rect class="primary" x="10" y="10" width="80" height="50" />
  <rect class="danger" x="110" y="10" width="80" height="50" />
</svg>
```

### 外部 CSS

**外部 CSS 样式表**
```html
<!-- svg.css -->
.rect-primary { fill: #4f5bd5; }
.rect-danger { fill: #d63031; }
```

```html
<link rel="stylesheet" href="svg.css" />
<svg viewBox="0 0 200 100">
  <rect class="rect-primary" width="100" height="50" />
</svg>
```

> 外部 CSS 仅在内联 SVG 或 `<object>` 嵌入时生效;`<img>` 引用的 SVG 无法被外部 CSS 样式化。

---

## CSS 可控制的 SVG 属性

| 类别         | 属性                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| 填充         | `fill`、`fill-opacity`、`fill-rule`                                                                                      |
| 描边         | `stroke`、`stroke-width`、`stroke-opacity`、`stroke-linecap`、`stroke-linejoin`、`stroke-dasharray`、`stroke-dashoffset` |
| 几何(部分) | `cx`、`cy`、`r`、`x`、`y`、`width`、`height`                                                                             |
| 文本         | `font-family`、`font-size`、`font-weight`、`text-anchor`、`letter-spacing`                                               |
| 视觉         | `opacity`、`visibility`、`display`、`filter`、`clip-path`、`mask`                                                        |
| 变换         | `transform`、`transform-origin`、`transform-box`                                                                         |
| 其他         | `color`、`cursor`、`pointer-events`                                                                                      |

### CSS 控制示例

**CSS 样式化 SVG 图标**
```css
.icon {
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.icon-primary {
  color: #4f5bd5;
}
.icon-danger {
  color: #d63031;
}
.icon-lg {
  width: 48px;
  height: 48px;
}
```

```html
<svg class="icon icon-primary icon-lg" viewBox="0 0 24 24">
  <path d="M3 12 L12 3 L21 12 M5 10 V21 H19 V10" />
</svg>
```

---

## CSS 变量

**CSS 自定义属性主题化**
```html
<style>
  :root {
    --brand-primary: #4f5bd5;
    --brand-secondary: #00b894;
    --brand-danger: #d63031;
  }
  .logo {
    fill: var(--brand-primary);
  }
  .accent {
    fill: var(--brand-secondary);
  }

  .dark-theme {
    --brand-primary: #8b92e8;
    --brand-secondary: #4cd9b0;
  }
</style>

<svg viewBox="0 0 200 100">
  <rect class="logo" width="100" height="50" />
  <rect class="accent" y="50" width="100" height="50" />
</svg>
```

切换父元素的 class 即可联动所有 SVG 颜色。

### CSS 变量穿透 use

**CSS 变量穿透 shadow DOM**
```html
<symbol id="card" viewBox="0 0 100 50">
  <rect width="100" height="50" fill="var(--card-bg)" />
  <text x="50" y="30" text-anchor="middle" fill="var(--card-text)">CARD</text>
</symbol>

<svg width="100" height="50">
  <use href="#card" style="--card-bg: #4f5bd5; --card-text: #fff" />
</svg>
```

---

## 伪类与状态

**CSS 伪类交互**
```css
.btn-rect {
  fill: #4f5bd5;
  transition: fill 0.2s;
  cursor: pointer;
}
.btn-rect:hover {
  fill: #6b78ea;
}
.btn-rect:active {
  fill: #3a47b8;
}
.btn-rect:focus-visible {
  outline: 2px solid #4f5bd5;
  outline-offset: 4px;
}
```

```html
<svg viewBox="0 0 200 80">
  <rect class="btn-rect" x="20" y="20" width="160" height="40" rx="20" tabindex="0" />
  <text x="100" y="44" text-anchor="middle" fill="#fff" pointer-events="none">按钮</text>
</svg>
```

### pointer-events

**pointer-events 控制事件响应**
```css
.label {
  pointer-events: none;
} /* 让点击穿透到下层 */
.btn {
  pointer-events: all;
} /* 显式响应事件 */
```

| 值               | 说明                    |
| ---------------- | ----------------------- |
| `none`           | 不响应事件(穿透)      |
| `all`(默认)    | 响应所有事件            |
| `fill`           | 仅填充区域响应          |
| `stroke`         | 仅描边区域响应          |
| `visiblePainted` | 可见且填充/描边区域响应 |

---

## 媒体查询

**SVG 内部响应式样式**
```html
<svg viewBox="0 0 400 200">
  <style>
    .title {
      font-size: 32px;
    }
    .subtitle {
      display: block;
    }

    @media (max-width: 600px) {
      .title {
        font-size: 20px;
      }
      .subtitle {
        display: none;
      }
    }

    @media (prefers-color-scheme: dark) {
      .bg {
        fill: #1a1a1a;
      }
      .text {
        fill: #fff;
      }
    }
  </style>
  <rect class="bg" width="400" height="200" fill="#fff" />
  <text class="title text" x="200" y="80" text-anchor="middle">主标题</text>
  <text class="subtitle text" x="200" y="120" text-anchor="middle">副标题</text>
</svg>
```

### prefers-reduced-motion

**prefers-reduced-motion 禁用动画**
```css
.animated {
  animation: spin 2s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .animated {
    animation: none;
  }
}
```

尊重用户系统偏好,禁用动画。

---

## transition 过渡

**CSS transition 过渡**
```css
rect {
  fill: #4f5bd5;
  transition:
    fill 0.3s ease,
    transform 0.3s ease;
}
rect:hover {
  fill: #00b894;
  transform: scale(1.1);
  transform-origin: center;
  transform-box: fill-box;
}
```

可过渡的属性:颜色、opacity、transform、几何属性(部分)。

---

## 主题切换

**data-theme 主题切换**
```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      :root {
        --bg: #fff;
        --text: #333;
        --card-bg: #f5f5f5;
        --brand: #4f5bd5;
      }
      [data-theme='dark'] {
        --bg: #1a1a1a;
        --text: #eee;
        --card-bg: #2a2a2a;
        --brand: #8b92e8;
      }
      body {
        background: var(--bg);
        color: var(--text);
        transition:
          background 0.3s,
          color 0.3s;
      }
      .chart-bar {
        fill: var(--brand);
        transition: fill 0.3s;
      }
    </style>
  </head>
  <body data-theme="light">
    <svg viewBox="0 0 400 200">
      <rect class="chart-bar" x="20" y="50" width="40" height="150" />
      <rect class="chart-bar" x="80" y="80" width="40" height="120" />
      <rect class="chart-bar" x="140" y="20" width="40" height="180" />
    </svg>
    <button
      onclick="document.body.dataset.theme = document.body.dataset.theme === 'light' ? 'dark' : 'light'"
    >
      切换主题
    </button>
  </body>
</html>
```

切换 `data-theme` 即可联动 SVG 与全局样式。

---

## 嵌入方式对 CSS 的影响

| 嵌入方式       | 外部 CSS | 内部 style | 表现属性 |
| -------------- | -------- | ---------- | -------- |
| inline SVG     | 支持     | 支持       | 支持     |
| `<object>`     | 不支持   | 支持       | 支持     |
| `<img>`        | 不支持   | 支持       | 支持     |
| CSS background | 不支持   | 支持       | 支持     |

> 仅 inline SVG 可被外部 CSS 完全控制,其他方式需要 SVG 文件内部自带样式。

---

## 综合示例:响应式数据条

**响应式数据条**
```html
<svg viewBox="0 0 400 200" class="chart">
  <style>
    .bar {
      fill: var(--bar-color, #4f5bd5);
      transition:
        fill 0.3s,
        height 0.5s;
    }
    .bar:hover {
      fill: var(--bar-hover, #00b894);
    }

    @media (prefers-color-scheme: dark) {
      .axis {
        stroke: #666;
      }
      .label {
        fill: #ccc;
      }
    }
    .axis {
      stroke: #333;
    }
    .label {
      fill: #666;
      font-size: 12px;
    }
  </style>

  <line class="axis" x1="40" y1="180" x2="380" y2="180" />
  <rect class="bar" x="60" y="50" width="40" height="130" />
  <text class="label" x="80" y="195" text-anchor="middle">Q1</text>

  <rect class="bar" x="120" y="80" width="40" height="100" />
  <text class="label" x="140" y="195" text-anchor="middle">Q2</text>

  <rect class="bar" x="180" y="20" width="40" height="160" />
  <text class="label" x="200" y="195" text-anchor="middle">Q3</text>
</svg>
```

<!-- ============ 文档分隔线：012-svg/015-SVGJavaScriptInteraction.md ============ -->

## 1. SVG DOM 与 HTML DOM

内联 SVG 的元素是真实 DOM 节点，可用标准 DOM API 操作。

```javascript
const rect = document.querySelector('rect');
rect.setAttribute('fill', '#d63031');
rect.style.opacity = '0.5';
rect.addEventListener('click', () => console.log('clicked'));
```

### 1.1 与 HTML 元素的差异

| 维度       | HTML                        | SVG                                                                  |
| ---------- | --------------------------- | -------------------------------------------------------------------- |
| 尺寸       | `element.style.width`       | `element.setAttribute('width', ...)`                                 |
| 颜色       | `element.style.color`       | `element.setAttribute('fill', ...)` 或 CSS                           |
| 类名       | `element.className = '...'` | `element.classList.add('...')`（SVG className 是 SVGAnimatedString） |
| 自定义属性 | `data-*`                    | 同 HTML，可用 dataset                                                |

### 1.2 className 注意

```javascript
// 错误：SVG 元素 className 是 SVGAnimatedString
rect.className = 'active'; // 无效

// 正确
rect.classList.add('active');
rect.classList.remove('inactive');
rect.setAttribute('class', 'active');
```

## 2. 属性读写

### 2.1 setAttribute / getAttribute

```javascript
const circle = document.querySelector('circle');
circle.setAttribute('cx', 100);
circle.setAttribute('cy', 50);
circle.setAttribute('r', 30);

const r = parseFloat(circle.getAttribute('r'));
console.log(r); // 30
```

### 2.2 命名空间属性

```javascript
const use = document.querySelector('use');
use.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', '#icon');
// 现代浏览器推荐
use.setAttribute('href', '#icon');
```

### 2.3 style 属性

```javascript
rect.style.fill = '#4f5bd5';
rect.style.strokeWidth = '2px';
rect.style.opacity = '0.8';
```

## 3. 动态创建元素

SVG 元素必须用 `createElementNS` 创建，指定 SVG 命名空间。

```javascript
const svgNS = 'http://www.w3.org/2000/svg';

const rect = document.createElementNS(svgNS, 'rect');
rect.setAttribute('x', 10);
rect.setAttribute('y', 10);
rect.setAttribute('width', 100);
rect.setAttribute('height', 50);
rect.setAttribute('fill', '#4f5bd5');

document.querySelector('svg').appendChild(rect);
```

### 3.1 封装创建函数

```javascript
function createSVG(tag, attrs = {}) {
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [key, value] of Object.entries(attrs)) {
    el.setAttribute(key, value);
  }
  return el;
}

const circle = createSVG('circle', { cx: 50, cy: 50, r: 30, fill: '#00b894' });
svg.appendChild(circle);
```

### 3.2 批量生成数据条

```javascript
const data = [
  { label: 'Q1', value: 120 },
  { label: 'Q2', value: 165 },
  { label: 'Q3', value: 210 },
  { label: 'Q4', value: 180 },
];

const svg = document.querySelector('svg');
const max = Math.max(...data.map((d) => d.value));
const barWidth = 40;
const gap = 20;

data.forEach((d, i) => {
  const h = (d.value / max) * 150;
  const x = 40 + i * (barWidth + gap);
  const y = 180 - h;

  const bar = createSVG('rect', {
    x,
    y,
    width: barWidth,
    height: h,
    fill: '#4f5bd5',
  });
  svg.appendChild(bar);

  const label = createSVG('text', {
    x: x + barWidth / 2,
    y: 195,
    'text-anchor': 'middle',
    'font-size': 12,
  });
  label.textContent = d.label;
  svg.appendChild(label);
});
```

## 4. 事件处理

SVG 元素支持完整的事件系统。

```javascript
const btn = document.querySelector('.btn-rect');
btn.addEventListener('click', (e) => {
  console.log('点击坐标：', e.clientX, e.clientY);
});

btn.addEventListener('mouseenter', () => {
  btn.setAttribute('fill', '#6b78ea');
});
btn.addEventListener('mouseleave', () => {
  btn.setAttribute('fill', '#4f5bd5');
});
```

### 4.1 事件委托

```javascript
svg.addEventListener('click', (e) => {
  if (e.target.matches('.bar')) {
    const value = e.target.dataset.value;
    console.log('点击了数据条：', value);
  }
});
```

### 4.2 拖拽

```javascript
let isDragging = false;
let offset = { x: 0, y: 0 };

const circle = document.querySelector('circle');

circle.addEventListener('mousedown', (e) => {
  isDragging = true;
  const cx = parseFloat(circle.getAttribute('cx'));
  const cy = parseFloat(circle.getAttribute('cy'));
  offset.x = e.clientX - cx;
  offset.y = e.clientY - cy;
});

document.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  circle.setAttribute('cx', e.clientX - offset.x);
  circle.setAttribute('cy', e.clientY - offset.y);
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});
```

## 5. 路径长度计算

```javascript
const path = document.querySelector('path');
const length = path.getTotalLength();
console.log('路径总长：', length);

// 获取路径上某点的坐标
const point = path.getPointAtLength(length / 2);
console.log('中点坐标：', point.x, point.y);

// 用于绘制动画
path.style.strokeDasharray = length;
path.style.strokeDashoffset = length;
path.getBoundingClientRect(); // 触发重排
path.style.transition = 'stroke-dashoffset 2s';
path.style.strokeDashoffset = 0;
```

## 6. 数据驱动更新

### 6.1 简单数据绑定

```javascript
function updateChart(data) {
  const bars = document.querySelectorAll('.bar');
  const max = Math.max(...data);

  bars.forEach((bar, i) => {
    const h = (data[i] / max) * 150;
    bar.setAttribute('height', h);
    bar.setAttribute('y', 180 - h);
  });
}

updateChart([100, 150, 200, 180]);
```

### 6.2 enter/update/exit 模式

```javascript
function renderBars(data) {
  const svg = document.querySelector('svg');
  const existing = Array.from(svg.querySelectorAll('.bar'));
  const barWidth = 40;
  const gap = 20;

  // update：更新现有元素
  existing.forEach((bar, i) => {
    if (i < data.length) {
      const h = (data[i] / Math.max(...data)) * 150;
      bar.setAttribute('height', h);
      bar.setAttribute('y', 180 - h);
    } else {
      // exit：移除多余元素
      bar.remove();
    }
  });

  // enter：添加新元素
  for (let i = existing.length; i < data.length; i++) {
    const h = (data[i] / Math.max(...data)) * 150;
    const bar = createSVG('rect', {
      class: 'bar',
      x: 40 + i * (barWidth + gap),
      y: 180 - h,
      width: barWidth,
      height: h,
      fill: '#4f5bd5',
    });
    svg.appendChild(bar);
  }
}
```

## 7. SVG 与 Canvas 互转

### 7.1 SVG 转 Canvas

```javascript
const svg = document.querySelector('svg');
const svgString = new XMLSerializer().serializeToString(svg);
const blob = new Blob([svgString], { type: 'image/svg+xml' });
const url = URL.createObjectURL(blob);

const img = new Image();
img.onload = () => {
  const canvas = document.createElement('canvas');
  canvas.width = svg.clientWidth;
  canvas.height = svg.clientHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0);
  URL.revokeObjectURL(url);

  // 导出为 PNG
  canvas.toBlob((blob) => {
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'chart.png';
    link.click();
  });
};
img.src = url;
```

### 7.2 SVG 转 Data URL

```javascript
const svgString = new XMLSerializer().serializeToString(svg);
const dataUrl = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svgString)));
```

## 8. 动画与 requestAnimationFrame

```javascript
const circle = document.querySelector('circle');
let t = 0;

function animate() {
  t += 0.02;
  const x = 100 + 50 * Math.cos(t);
  const y = 50 + 30 * Math.sin(t);
  circle.setAttribute('cx', x);
  circle.setAttribute('cy', y);
  requestAnimationFrame(animate);
}
animate();
```

### 8.1 缓动函数

```javascript
const easings = {
  linear: (t) => t,
  easeInQuad: (t) => t * t,
  easeOutQuad: (t) => t * (2 - t),
  easeInOutQuad: (t) => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t),
};

function animate(duration, easing, callback) {
  const start = performance.now();
  function frame(now) {
    const elapsed = now - start;
    const t = Math.min(elapsed / duration, 1);
    callback(easing(t), t);
    if (t < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}

animate(1000, easings.easeOutQuad, (value) => {
  circle.setAttribute('cx', 50 + value * 150);
});
```

## 9. Web Animations API

```javascript
// 关键帧动画
const animation = rect.animate(
  [{ transform: 'translateX(0)' }, { transform: 'translateX(200px)' }],
  {
    duration: 1000,
    fill: 'forwards',
    easing: 'ease-out',
  }
);

// 控制动画
animation.pause();
animation.play();
animation.reverse();
animation.cancel();

// 监听结束
animation.onfinish = () => console.log('动画结束');
```

## 10. 实战：可交互柱状图

```html
<svg viewBox="0 0 400 200" class="chart">
  <line x1="40" y1="180" x2="380" y2="180" stroke="#333" />
</svg>

<script>
  const data = [
    { label: 'Q1', value: 120 },
    { label: 'Q2', value: 165 },
    { label: 'Q3', value: 210 },
    { label: 'Q4', value: 180 },
  ];

  const svg = document.querySelector('.chart');
  const max = Math.max(...data.map((d) => d.value));
  const barWidth = 60;
  const gap = 20;

  data.forEach((d, i) => {
    const h = (d.value / max) * 140;
    const x = 60 + i * (barWidth + gap);
    const y = 180 - h;

    const bar = createSVG('rect', {
      x,
      y,
      width: barWidth,
      height: h,
      fill: '#4f5bd5',
      'data-value': d.value,
    });
    bar.style.transition = 'fill 0.2s';
    bar.style.cursor = 'pointer';
    bar.addEventListener('mouseenter', () => bar.setAttribute('fill', '#6b78ea'));
    bar.addEventListener('mouseleave', () => bar.setAttribute('fill', '#4f5bd5'));
    bar.addEventListener('click', () => alert(`${d.label}: ${d.value}`));
    svg.appendChild(bar);

    const label = createSVG('text', {
      x: x + barWidth / 2,
      y: 195,
      'text-anchor': 'middle',
      'font-size': 12,
    });
    label.textContent = d.label;
    svg.appendChild(label);

    const value = createSVG('text', {
      x: x + barWidth / 2,
      y: y - 5,
      'text-anchor': 'middle',
      'font-size': 12,
      fill: '#666',
    });
    value.textContent = d.value;
    svg.appendChild(value);
  });

  function createSVG(tag, attrs = {}) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
    return el;
  }
</script>
```

## 11. 性能优化

| 技巧        | 说明                                   |
| ----------- | -------------------------------------- |
| 批量更新    | 用 DocumentFragment 或先隐藏再批量操作 |
| 减少 reflow | 修改 transform 而非 x/y，避免触发重排  |
| 使用 CSS 类 | 频繁切换用 class 而非直接改 style      |
| 离屏操作    | 复杂图形先在内存中构建再插入 DOM       |
| will-change | 标记即将动画的元素                     |
| 虚拟化      | 大量数据只渲染可见区域                 |

## 12. 调试技巧

```javascript
// 控制台快速检查 SVG
console.log(svg.getBBox()); // 元素边界框
console.log(svg.getCTM()); // 当前变换矩阵
console.log(svg.getScreenCTM()); // 屏幕坐标变换矩阵

// 监听所有 SVG 事件
document.querySelectorAll('svg *').forEach((el) => {
  el.addEventListener('click', (e) => console.log(e.target.tagName, e));
});
```

下一篇介绍响应式 SVG 与性能优化。
## SVG DOM 操作

**SVG DOM 与 HTML DOM 一致**
```javascript
const rect = document.querySelector('rect');
rect.setAttribute('fill', '#d63031');
rect.style.opacity = '0.5';
rect.addEventListener('click', () => console.log('clicked'));
```

### SVG DOM 与 HTML DOM 差异

| 维度       | HTML                        | SVG                                                                  |
| ---------- | --------------------------- | -------------------------------------------------------------------- |
| 尺寸       | `element.style.width`       | `element.setAttribute('width', ...)`                                 |
| 颜色       | `element.style.color`       | `element.setAttribute('fill', ...)` 或 CSS                           |
| 类名       | `element.className = '...'` | `element.classList.add('...')`(SVG className 是 SVGAnimatedString) |
| 自定义属性 | `data-*`                    | 同 HTML,可用 dataset                                              |

### className 注意

**SVG className 是 SVGAnimatedString**
```javascript
// 错误:SVG 元素 className 是 SVGAnimatedString
rect.className = 'active'; // 无效

// 正确
rect.classList.add('active');
rect.classList.remove('inactive');
rect.setAttribute('class', 'active');
```

---

## 属性读写

### setAttribute / getAttribute

**SVG 属性读写**
```javascript
const circle = document.querySelector('circle');
circle.setAttribute('cx', 100);
circle.setAttribute('cy', 50);
circle.setAttribute('r', 30);

const r = parseFloat(circle.getAttribute('r'));
console.log(r); // 30
```

### 命名空间属性

**setAttributeNS 设置命名空间属性**
```javascript
const use = document.querySelector('use');
use.setAttributeNS('http://www.w3.org/1999/xlink', 'xlink:href', '#icon');
// 现代浏览器推荐
use.setAttribute('href', '#icon');
```

### style 属性

**style 属性设置样式**
```javascript
rect.style.fill = '#4f5bd5';
rect.style.strokeWidth = '2px';
rect.style.opacity = '0.8';
```

---

## 动态创建元素

**createElementNS 创建 SVG 元素**
```javascript
const svgNS = 'http://www.w3.org/2000/svg';

const rect = document.createElementNS(svgNS, 'rect');
rect.setAttribute('x', 10);
rect.setAttribute('y', 10);
rect.setAttribute('width', 100);
rect.setAttribute('height', 50);
rect.setAttribute('fill', '#4f5bd5');

document.querySelector('svg').appendChild(rect);
```

SVG 元素必须用 `createElementNS` 创建,指定 SVG 命名空间。

### 封装创建函数

**createSVG 工具函数**
```javascript
function createSVG(tag, attrs = {}) {
  const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
  for (const [key, value] of Object.entries(attrs)) {
    el.setAttribute(key, value);
  }
  return el;
}

const circle = createSVG('circle', { cx: 50, cy: 50, r: 30, fill: '#00b894' });
svg.appendChild(circle);
```

### 批量生成数据条

**数据驱动批量生成**
```javascript
const data = [
  { label: 'Q1', value: 120 },
  { label: 'Q2', value: 165 },
  { label: 'Q3', value: 210 },
  { label: 'Q4', value: 180 },
];

const svg = document.querySelector('svg');
const max = Math.max(...data.map((d) => d.value));
const barWidth = 40;
const gap = 20;

data.forEach((d, i) => {
  const h = (d.value / max) * 150;
  const x = 40 + i * (barWidth + gap);
  const y = 180 - h;

  const bar = createSVG('rect', {
    x,
    y,
    width: barWidth,
    height: h,
    fill: '#4f5bd5',
  });
  svg.appendChild(bar);

  const label = createSVG('text', {
    x: x + barWidth / 2,
    y: 195,
    'text-anchor': 'middle',
    'font-size': 12,
  });
  label.textContent = d.label;
  svg.appendChild(label);
});
```

---

## 事件处理

**SVG 事件绑定**
```javascript
const btn = document.querySelector('.btn-rect');
btn.addEventListener('click', (e) => {
  console.log('点击坐标:', e.clientX, e.clientY);
});

btn.addEventListener('mouseenter', () => {
  btn.setAttribute('fill', '#6b78ea');
});
btn.addEventListener('mouseleave', () => {
  btn.setAttribute('fill', '#4f5bd5');
});
```

### 事件委托

**事件委托模式**
```javascript
svg.addEventListener('click', (e) => {
  if (e.target.matches('.bar')) {
    const value = e.target.dataset.value;
    console.log('点击了数据条:', value);
  }
});
```

### 拖拽实现

**鼠标拖拽**
```javascript
let isDragging = false;
let offset = { x: 0, y: 0 };

const circle = document.querySelector('circle');

circle.addEventListener('mousedown', (e) => {
  isDragging = true;
  const cx = parseFloat(circle.getAttribute('cx'));
  const cy = parseFloat(circle.getAttribute('cy'));
  offset.x = e.clientX - cx;
  offset.y = e.clientY - cy;
});

document.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  circle.setAttribute('cx', e.clientX - offset.x);
  circle.setAttribute('cy', e.clientY - offset.y);
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});
```

---

## 路径长度计算

**getTotalLength / getPointAtLength**
```javascript
const path = document.querySelector('path');
const length = path.getTotalLength();
console.log('路径总长:', length);

// 获取路径上某点的坐标
const point = path.getPointAtLength(length / 2);
console.log('中点坐标:', point.x, point.y);

// 用于绘制动画
path.style.strokeDasharray = length;
path.style.strokeDashoffset = length;
path.getBoundingClientRect(); // 触发重排
path.style.transition = 'stroke-dashoffset 2s';
path.style.strokeDashoffset = 0;
```

### 路径 API

| 方法                  | 说明                  |
| --------------------- | --------------------- |
| `getTotalLength()`    | 获取路径总长度        |
| `getPointAtLength(d)` | 获取路径上指定距离的点 |
| `getBBox()`           | 获取元素边界框        |
| `getCTM()`            | 当前变换矩阵          |
| `getScreenCTM()`      | 屏幕坐标变换矩阵      |

---

## 数据驱动更新

### 简单数据绑定

**updateChart 更新数据**
```javascript
function updateChart(data) {
  const bars = document.querySelectorAll('.bar');
  const max = Math.max(...data);

  bars.forEach((bar, i) => {
    const h = (data[i] / max) * 150;
    bar.setAttribute('height', h);
    bar.setAttribute('y', 180 - h);
  });
}

updateChart([100, 150, 200, 180]);
```

### enter/update/exit 模式

**D3 风格数据绑定**
```javascript
function renderBars(data) {
  const svg = document.querySelector('svg');
  const existing = Array.from(svg.querySelectorAll('.bar'));
  const barWidth = 40;
  const gap = 20;

  // update:更新现有元素
  existing.forEach((bar, i) => {
    if (i < data.length) {
      const h = (data[i] / Math.max(...data)) * 150;
      bar.setAttribute('height', h);
      bar.setAttribute('y', 180 - h);
    } else {
      // exit:移除多余元素
      bar.remove();
    }
  });

  // enter:添加新元素
  for (let i = existing.length; i < data.length; i++) {
    const h = (data[i] / Math.max(...data)) * 150;
    const bar = createSVG('rect', {
      class: 'bar',
      x: 40 + i * (barWidth + gap),
      y: 180 - h,
      width: barWidth,
      height: h,
      fill: '#4f5bd5',
    });
    svg.appendChild(bar);
  }
}
```

---

## SVG 与 Canvas 互转

### SVG 转 Canvas

**XMLSerializer 转 Canvas**
```javascript
const svg = document.querySelector('svg');
const svgString = new XMLSerializer().serializeToString(svg);
const blob = new Blob([svgString], { type: 'image/svg+xml' });
const url = URL.createObjectURL(blob);

const img = new Image();
img.onload = () => {
  const canvas = document.createElement('canvas');
  canvas.width = svg.clientWidth;
  canvas.height = svg.clientHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0);
  URL.revokeObjectURL(url);

  // 导出为 PNG
  canvas.toBlob((blob) => {
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'chart.png';
    link.click();
  });
};
img.src = url;
```

### SVG 转 Data URL

**SVG 转 base64 Data URL**
```javascript
const svgString = new XMLSerializer().serializeToString(svg);
const dataUrl = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svgString)));
```

---

## requestAnimationFrame 动画

**requestAnimationFrame 循环动画**
```javascript
const circle = document.querySelector('circle');
let t = 0;

function animate() {
  t += 0.02;
  const x = 100 + 50 * Math.cos(t);
  const y = 50 + 30 * Math.sin(t);
  circle.setAttribute('cx', x);
  circle.setAttribute('cy', y);
  requestAnimationFrame(animate);
}
animate();
```

### 缓动函数

**easings 缓动函数库**
```javascript
const easings = {
  linear: (t) => t,
  easeInQuad: (t) => t * t,
  easeOutQuad: (t) => t * (2 - t),
  easeInOutQuad: (t) => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t),
};

function animate(duration, easing, callback) {
  const start = performance.now();
  function frame(now) {
    const elapsed = now - start;
    const t = Math.min(elapsed / duration, 1);
    callback(easing(t), t);
    if (t < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}

animate(1000, easings.easeOutQuad, (value) => {
  circle.setAttribute('cx', 50 + value * 150);
});
```

---

## Web Animations API

**element.animate 关键帧动画**
```javascript
// 关键帧动画
const animation = rect.animate(
  [{ transform: 'translateX(0)' }, { transform: 'translateX(200px)' }],
  {
    duration: 1000,
    fill: 'forwards',
    easing: 'ease-out',
  }
);

// 控制动画
animation.pause();
animation.play();
animation.reverse();
animation.cancel();

// 监听结束
animation.onfinish = () => console.log('动画结束');
```

### WAAPI 方法

| 方法                  | 说明         |
| --------------------- | ------------ |
| `animate(keyframes, options)` | 开始动画  |
| `pause()`             | 暂停         |
| `play()`              | 播放         |
| `reverse()`           | 反向播放     |
| `cancel()`            | 取消         |
| `onfinish`            | 结束回调     |

---

## 综合示例:可交互柱状图

**动态生成可交互柱状图**
```html
<svg viewBox="0 0 400 200" class="chart">
  <line x1="40" y1="180" x2="380" y2="180" stroke="#333" />
</svg>

<script>
  const data = [
    { label: 'Q1', value: 120 },
    { label: 'Q2', value: 165 },
    { label: 'Q3', value: 210 },
    { label: 'Q4', value: 180 },
  ];

  const svg = document.querySelector('.chart');
  const max = Math.max(...data.map((d) => d.value));
  const barWidth = 60;
  const gap = 20;

  data.forEach((d, i) => {
    const h = (d.value / max) * 140;
    const x = 60 + i * (barWidth + gap);
    const y = 180 - h;

    const bar = createSVG('rect', {
      x,
      y,
      width: barWidth,
      height: h,
      fill: '#4f5bd5',
      'data-value': d.value,
    });
    bar.style.transition = 'fill 0.2s';
    bar.style.cursor = 'pointer';
    bar.addEventListener('mouseenter', () => bar.setAttribute('fill', '#6b78ea'));
    bar.addEventListener('mouseleave', () => bar.setAttribute('fill', '#4f5bd5'));
    bar.addEventListener('click', () => alert(`${d.label}: ${d.value}`));
    svg.appendChild(bar);

    const label = createSVG('text', {
      x: x + barWidth / 2,
      y: 195,
      'text-anchor': 'middle',
      'font-size': 12,
    });
    label.textContent = d.label;
    svg.appendChild(label);

    const value = createSVG('text', {
      x: x + barWidth / 2,
      y: y - 5,
      'text-anchor': 'middle',
      'font-size': 12,
      fill: '#666',
    });
    value.textContent = d.value;
    svg.appendChild(value);
  });

  function createSVG(tag, attrs = {}) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [k, v] of Object.entries(attrs)) el.setAttribute(k, v);
    return el;
  }
</script>
```

---

## 调试 API

**getBBox / getCTM 调试**
```javascript
// 控制台快速检查 SVG
console.log(svg.getBBox()); // 元素边界框
console.log(svg.getCTM()); // 当前变换矩阵
console.log(svg.getScreenCTM()); // 屏幕坐标变换矩阵

// 监听所有 SVG 事件
document.querySelectorAll('svg *').forEach((el) => {
  el.addEventListener('click', (e) => console.log(e.target.tagName, e));
});
```

<!-- ============ 文档分隔线：012-svg/016-SVGResponsivePerformance.md ============ -->

## 1. 响应式 SVG

### 1.1 仅声明 viewBox

让 SVG 自适应容器尺寸的标准做法：

```html
<svg viewBox="0 0 400 300" class="responsive">
  <!-- 内容 -->
</svg>
```

```css
.responsive {
  width: 100%;
  height: auto;
  display: block;
}
```

> 不指定 width/height，仅声明 viewBox，让外层 CSS 控制实际尺寸。SVG 会按宽高比自动缩放。

### 1.2 preserveAspectRatio 适配

```html
<!-- 完整显示，留白 -->
<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid meet">
  <!-- 4:3 内容在 16:9 容器中会上下留白 -->
</svg>

<!-- 填满容器，可能裁剪 -->
<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice">
  <!-- 4:3 内容在 16:9 容器中左右被裁 -->
</svg>
```

### 1.3 CSS aspect-ratio

```css
.chart {
  width: 100%;
  aspect-ratio: 4 / 3;
}
```

```html
<svg class="chart" viewBox="0 0 400 300">...</svg>
```

确保容器保持宽高比，避免 SVG 高度坍塌。

## 2. 流式 SVG

不同屏幕显示不同内容：

```html
<svg viewBox="0 0 400 200">
  <style>
    .mobile-only {
      display: none;
    }
    .desktop-only {
      display: block;
    }

    @media (max-width: 600px) {
      .mobile-only {
        display: block;
      }
      .desktop-only {
        display: none;
      }
    }
  </style>
  <g class="mobile-only">
    <!-- 移动端简化版 -->
    <text x="200" y="100" text-anchor="middle" font-size="20">简化视图</text>
  </g>
  <g class="desktop-only">
    <!-- 桌面端完整版 -->
    <text x="200" y="50" text-anchor="middle" font-size="32">完整视图</text>
    <text x="200" y="100" text-anchor="middle" font-size="16">更多细节</text>
  </g>
</svg>
```

## 3. CSS Container Queries

```css
.chart-container {
  container-type: inline-size;
}

@container (max-width: 400px) {
  .chart .detailed {
    display: none;
  }
}
```

```html
<div class="chart-container">
  <svg class="chart" viewBox="0 0 400 300">
    <g class="detailed">...</g>
  </svg>
</div>
```

根据容器宽度（而非视口）响应式显示。

## 4. 性能瓶颈分析

### 4.1 SVG 渲染性能特征

| 因素         | 影响                                 |
| ------------ | ------------------------------------ |
| DOM 节点数量 | 节点多 → 重排重绘开销大              |
| 复杂路径     | 长路径 → 解析与渲染慢                |
| 滤镜         | feGaussianBlur 等 → CPU/GPU 开销大   |
| 蒙版与裁剪   | 软蒙版 → 像素级计算                  |
| 文本渲染     | 大量 `<text>` → 排版开销             |
| 透明度与混合 | opacity、mix-blend-mode → 合成层开销 |

### 4.2 节点数量阈值

| 节点数      | 性能                  |
| ----------- | --------------------- |
| < 100       | 流畅                  |
| 100 - 1000  | 静态可用，动画需优化  |
| 1000 - 5000 | 明显卡顿              |
| > 5000      | 考虑改用 Canvas/WebGL |

## 5. 优化策略

### 5.1 减少节点

```html
<!-- 冗余：多个单独的 line -->
<g stroke="#333">
  <line x1="10" y1="10" x2="100" y2="10" />
  <line x1="10" y1="20" x2="100" y2="20" />
  <line x1="10" y1="30" x2="100" y2="30" />
</g>

<!-- 优化：合并为一个 path -->
<path d="M 10 10 L 100 10 M 10 20 L 100 20 M 10 30 L 100 30" stroke="#333" />
```

### 5.2 复用 symbol

```html
<defs>
  <symbol id="dot" viewBox="0 0 10 10">
    <circle cx="5" cy="5" r="4" />
  </symbol>
</defs>
<use href="#dot" x="0" y="0" />
<use href="#dot" x="20" y="0" />
<!-- 1000 个 use 比直接画 1000 个 circle 内存占用小 -->
```

### 5.3 简化路径

```html
<!-- 原始路径 -->
<path d="M 10.123456 10.234567 L 50.345678 10.456789 ..." />

<!-- SVGO 优化后 -->
<path d="M10 10L50 10..." />
```

使用 SVGO 工具自动优化：

```bash
npm install -g svgo
svgo input.svg -o output.svg --precision=2
```

### 5.4 避免复杂滤镜

```html
<!-- 慢：模糊大区域 -->
<filter id="blur">
  <feGaussianBlur stdDeviation="10" />
</filter>
<rect width="1920" height="1080" filter="url(#blur)" />

<!-- 快：模糊小区域再缩放 -->
<filter id="blur-small" x="0" y="0" width="200" height="200">
  <feGaussianBlur stdDeviation="10" />
</filter>
```

### 5.5 transform 替代几何属性

```javascript
// 慢：修改 x 触发重排
rect.setAttribute('x', 100);

// 快：修改 transform 使用合成层
rect.style.transform = 'translateX(100px)';
```

### 5.6 will-change 提示

```css
.animated-element {
  will-change: transform, opacity;
}
```

让浏览器提前为元素创建独立图层。

## 6. 懒加载

### 6.1 IntersectionObserver

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      observer.unobserve(img);
    }
  });
});

document.querySelectorAll('img[data-src]').forEach((img) => {
  observer.observe(img);
});
```

```html
<img data-src="large-diagram.svg" alt="图表" width="800" height="600" />
```

### 6.2 内联关键 SVG

首屏关键 SVG 内联，避免额外请求：

```html
<!-- 内联首屏 Logo -->
<svg viewBox="0 0 100 40" class="logo">
  <path d="..." fill="currentColor" />
</svg>

<!-- 懒加载非关键 SVG -->
<img data-src="diagram.svg" alt="图表" loading="lazy" />
```

## 7. 压缩与优化

### 7.1 SVGO 优化

```bash
# 单文件
svgo input.svg -o output.svg

# 批量
svgo -f input-dir -o output-dir

# 配置文件 .svgo.config.js
module.exports = {
  plugins: [
    { name: 'preset-default' },
    { name: 'removeDimensions', active: true },  // 移除 width/height
    { name: 'sortAttrs', active: true }
  ]
};
```

### 7.2 常用优化项

| 优化             | 说明                   |
| ---------------- | ---------------------- |
| 移除注释         | 减小体积               |
| 移除编辑器元数据 | 如 Inkscape 命名空间   |
| 合并路径         | 多 path 合并为单 path  |
| 简化坐标         | 降低精度到 2 位小数    |
| 移除默认值       | 如 fill="black" 可省略 |
| 转换为相对路径   | 文件更小               |

### 7.3 Gzip / Brotli 压缩

服务器配置 SVG 压缩（文本格式压缩率高）：

```nginx
# nginx.conf
gzip on;
gzip_types image/svg+xml;
```

通常可压缩 70%-90%。

## 8. 缓存策略

### 8.1 外部 SVG 文件缓存

```nginx
location ~* \.svg$ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}
```

### 8.2 文件名哈希

```html
<!-- 构建工具生成 -->
<img src="logo.a3b7c9.svg" alt="Logo" />
```

文件内容变化时哈希变化，浏览器自动重新下载。

## 9. 渲染优化

### 9.1 避免重排

```javascript
// 慢：逐个修改属性
elements.forEach((el) => {
  el.setAttribute('x', newX);
  el.setAttribute('y', newY);
});

// 快：批量修改
svg.style.display = 'none';
elements.forEach((el) => {
  el.setAttribute('x', newX);
  el.setAttribute('y', newY);
});
svg.style.display = 'block';
```

### 9.2 使用 DocumentFragment

```javascript
const fragment = document.createDocumentFragment();
for (let i = 0; i < 1000; i++) {
  const dot = createSVG('circle', { cx: i, cy: 50, r: 2 });
  fragment.appendChild(dot);
}
svg.appendChild(fragment); // 一次性插入
```

### 9.3 CSS containment

```css
.chart {
  contain: layout style paint;
}
```

隔离元素布局、样式、绘制，避免影响外部。

## 10. 实战：大数据点散点图

```html
<svg viewBox="0 0 800 400" class="scatter">
  <defs>
    <symbol id="point" viewBox="-1 -1 2 2">
      <circle r="1" fill="#4f5bd5" />
    </symbol>
  </defs>
</svg>

<script>
  const svg = document.querySelector('.scatter');
  const data = [];
  for (let i = 0; i < 2000; i++) {
    data.push({
      x: Math.random() * 800,
      y: Math.random() * 400,
    });
  }

  // 批量插入，减少 reflow
  const fragment = document.createDocumentFragment();
  data.forEach((d) => {
    const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
    use.setAttribute('href', '#point');
    use.setAttribute('x', d.x - 1);
    use.setAttribute('y', d.y - 1);
    use.setAttribute('width', 6);
    use.setAttribute('height', 6);
    fragment.appendChild(use);
  });
  svg.appendChild(fragment);
</script>
```

**优化点**：

- symbol 复用避免重复定义 circle
- DocumentFragment 批量插入
- 限制节点数（> 5000 考虑 Canvas）

## 11. 监测与分析

### 11.1 Chrome DevTools

- **Performance** 面板：录制动画，分析帧率与瓶颈
- **Layers** 面板：查看合成层，确认 GPU 加速
- **Rendering** 面板：开启 Paint flashing 高亮重绘区域

### 11.2 关键指标

| 指标     | 目标    |
| -------- | ------- |
| FPS      | ≥ 55    |
| 首次渲染 | < 100ms |
| 单帧渲染 | < 16ms  |
| 内存占用 | < 50MB  |

## 12. 何时改用 Canvas

| 场景                     | 推荐          |
| ------------------------ | ------------- |
| 数据点 < 1000            | SVG           |
| 数据点 1000-5000，无动画 | SVG（优化后） |
| 数据点 > 5000            | Canvas        |
| 实时粒子系统             | Canvas/WebGL  |
| 复杂图像处理             | Canvas        |
| 需要交互与可访问性       | SVG           |

下一篇介绍 SVG 图标系统与可访问性。
## 响应式 SVG 基础

**仅声明 viewBox 自适应**
`<svg viewBox="<min-x> <min-y> <width> <height>" [class]="<类名>">`
```html
<!-- 不指定 width/height,仅声明 viewBox,由外层 CSS 控制实际尺寸 -->
<svg viewBox="0 0 400 300" class="responsive">
  <!-- SVG 内容按宽高比自动缩放 -->
</svg>
```

```css
.responsive {
  width: 100%;
  height: auto;
  display: block;
}
```

---

## preserveAspectRatio 适配

**完整显示留白**
`<svg viewBox="..." preserveAspectRatio="xMidYMid meet">`
```html
<!-- 4:3 内容在 16:9 容器中上下留白,完整显示 -->
<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid meet">
  <!-- 内容 -->
</svg>
```

**填满容器裁剪**
`<svg viewBox="..." preserveAspectRatio="xMidYMid slice">`
```html
<!-- 4:3 内容在 16:9 容器中左右被裁,填满容器 -->
<svg viewBox="0 0 400 300" preserveAspectRatio="xMidYMid slice">
  <!-- 内容 -->
</svg>
```

### preserveAspectRatio 取值表

| 对齐方式 | 说明 |
| --- | --- |
| `xMinYMin` | 左上对齐 |
| `xMidYMin` | 顶部居中对齐 |
| `xMaxYMin` | 右上对齐 |
| `xMinYMid` | 左侧居中对齐 |
| `xMidYMid` | 居中对齐(默认) |
| `xMaxYMid` | 右侧居中对齐 |
| `xMinYMax` | 左下对齐 |
| `xMidYMax` | 底部居中对齐 |
| `xMaxYMax` | 右下对齐 |
| `meet` | 完整显示,留白 |
| `slice` | 填满容器,裁剪 |
| `none` | 拉伸变形,不保比例 |

---

## CSS aspect-ratio 控制宽高比

**容器宽高比**
`<selector> { aspect-ratio: <width> / <height>; }`
```css
.chart {
  width: 100%;
  aspect-ratio: 4 / 3;
}
```

```html
<svg class="chart" viewBox="0 0 400 300">...</svg>
```

---

## 流式 SVG 媒体查询

**视口响应式显示**
`@media (max-width: <breakpoint>) { <selector> { display: <value>; } }`
```html
<svg viewBox="0 0 400 200">
  <style>
    .mobile-only { display: none; }
    .desktop-only { display: block; }

    @media (max-width: 600px) {
      .mobile-only { display: block; }
      .desktop-only { display: none; }
    }
  </style>
  <g class="mobile-only">
    <text x="200" y="100" text-anchor="middle" font-size="20">简化视图</text>
  </g>
  <g class="desktop-only">
    <text x="200" y="50" text-anchor="middle" font-size="32">完整视图</text>
    <text x="200" y="100" text-anchor="middle" font-size="16">更多细节</text>
  </g>
</svg>
```

---

## CSS Container Queries

**容器查询声明**
`<container-selector> { container-type: inline-size; }`
```css
.chart-container {
  container-type: inline-size;
}

@container (max-width: 400px) {
  .chart .detailed {
    display: none;
  }
}
```

```html
<div class="chart-container">
  <svg class="chart" viewBox="0 0 400 300">
    <g class="detailed">...</g>
  </svg>
</div>
```

---

## 响应式属性综合

**svg 元素响应式属性**
`<svg viewBox="..." preserveAspectRatio="..." width="..." height="...">`
```html
<svg
  viewBox="0 0 100 100"
  preserveAspectRatio="xMidYMid meet"
  width="100%"
  height="100%"
  class="responsive-svg"
>
  <circle cx="50" cy="50" r="40" fill="#4f5bd5" />
</svg>
```

### svg 响应式属性表

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| `viewBox` | 视口坐标系 | `0 0 400 300` |
| `preserveAspectRatio` | 宽高比保持策略 | `xMidYMid meet` |
| `width` | 宽度(CSS 可覆盖) | `100%` / `auto` |
| `height` | 高度(CSS 可覆盖) | `100%` / `auto` |
| `class` | CSS 类名 | `responsive` |

---

## CSS 响应式尺寸变体

**断点尺寸控制**
`@media (max-width: <bp>) { .icon { width: <size>; height: <size>; } }`
```css
.responsive-icon {
  width: 32px;
  height: 32px;
}

@media (max-width: 768px) {
  .responsive-icon {
    width: 24px;
    height: 24px;
  }
}

@media (max-width: 480px) {
  .responsive-icon {
    width: 16px;
    height: 16px;
  }
}
```

```html
<svg class="responsive-icon" viewBox="0 0 24 24">
  <use href="#icon-menu" />
</svg>
```

---

## 嵌入式响应式图片

**img 标签响应式 SVG**
`<img src="<file>.svg" alt="..." width="..." height="..." />`
```html
<img
  src="diagram.svg"
  alt="响应式图表"
  width="100%"
  height="auto"
  loading="lazy"
/>
```

```css
img.responsive-svg {
  width: 100%;
  height: auto;
  max-width: 800px;
}
```

---

## 响应式 viewBox 多版本

**多 viewBox 适配**
`<svg viewBox="<mobile-box>" class="svg-mobile"> / <svg viewBox="<desktop-box>" class="svg-desktop">`
```html
<!-- 移动端简化版 viewBox -->
<svg viewBox="0 0 200 200" class="svg-mobile">
  <circle cx="100" cy="100" r="50" />
</svg>

<!-- 桌面端扩展版 viewBox -->
<svg viewBox="0 0 800 400" class="svg-desktop">
  <circle cx="100" cy="200" r="50" />
  <circle cx="400" cy="200" r="50" />
  <circle cx="700" cy="200" r="50" />
</svg>
```

```css
.svg-mobile { display: none; }
.svg-desktop { display: block; }

@media (max-width: 768px) {
  .svg-mobile { display: block; }
  .svg-desktop { display: none; }
}
```

---

## 响应式字体单位

**SVG 内 em 单位**
`<text font-size="<em>em" ...>`
```html
<svg viewBox="0 0 400 200">
  <text x="200" y="100" text-anchor="middle" font-size="2em">
    响应式文本
  </text>
</svg>
```

```css
svg {
  font-size: 16px;
}
@media (max-width: 600px) {
  svg {
    font-size: 12px;
  }
}
```

---

## 响应式 transform 缩放

**CSS transform 自适应**
`<selector> { transform: scale(<factor>); transform-origin: <origin>; }`
```css
.logo-svg {
  transform-origin: center;
  transform-box: fill-box;
}

@media (max-width: 600px) {
  .logo-svg {
    transform: scale(0.7);
  }
}
```

```html
<svg class="logo-svg" viewBox="0 0 400 120">
  <text x="200" y="75" text-anchor="middle" font-size="48">LOGO</text>
</svg>
```

---

## 响应式 stroke-width

**non-scaling-stroke 属性**
`<element stroke-width="<value>" vector-effect="non-scaling-stroke" />`
```html
<svg viewBox="0 0 100 100" width="100%" height="100%">
  <!-- 描边宽度不随 SVG 缩放而变化 -->
  <rect
    x="10"
    y="10"
    width="80"
    height="80"
    fill="none"
    stroke="#333"
    stroke-width="2"
    vector-effect="non-scaling-stroke"
  />
</svg>
```

### vector-effect 取值表

| 值 | 说明 |
| --- | --- |
| `non-scaling-stroke` | 描边宽度保持不变,不随缩放 |
| `non-rotating-stroke` | 描边方向不随变换旋转 |
| `none` | 默认行为,随变换缩放 |

<!-- ============ 文档分隔线：012-svg/017-SVGIconAccessibility.md ============ -->

## 1. 为什么用 SVG 图标

| 维度     | SVG 图标     | 字体图标（如 Font Awesome） | PNG 图标 |
| -------- | ------------ | --------------------------- | -------- |
| 缩放     | 无损         | 无损                        | 锯齿     |
| 颜色     | CSS 控制     | CSS 控制（有限）            | 固定     |
| 可访问性 | 原生支持     | 一般                        | 需 alt   |
| 文件体积 | 小（单图标） | 中（整包）                  | 大       |
| 动画     | 支持         | 有限                        | 不支持   |
| 语义化   | DOM 节点     | 字符                        | 图片     |

SVG 是现代 Web 图标的首选方案。

## 2. 图标设计原则

### 2.1 统一画布

所有图标使用相同 viewBox（通常 24×24）：

```html
<symbol id="icon-home" viewBox="0 0 24 24">...</symbol>
<symbol id="icon-search" viewBox="0 0 24 24">...</symbol>
```

### 2.2 描边一致

```html
<symbol id="icon-home" viewBox="0 0 24 24">
  <path
    d="..."
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</symbol>
```

统一描边宽度、端点、拐角，保持视觉一致性。

### 2.3 使用 currentColor

```html
<!-- 错误：硬编码颜色 -->
<symbol id="icon-home">
  <path fill="#4f5bd5" />
</symbol>

<!-- 正确：使用 currentColor -->
<symbol id="icon-home">
  <path fill="currentColor" />
</symbol>
```

`currentColor` 让图标颜色继承父元素 `color`，实现主题化。

### 2.4 对齐像素网格

```html
<!-- 模糊：坐标落在 .5 -->
<path d="M 0.5 0.5 L 10.5 0.5" />

<!-- 清晰：整数坐标 -->
<path d="M 0 0 L 10 0" />
```

1px 描边的图标需对齐像素网格，避免抗锯齿模糊。

## 3. 图标系统实现

### 3.1 Sprite 模式

```html
<!-- icons.svg 隐藏文件 -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path
      d="M3 12 L12 3 L21 12 M5 10 V21 H19 V10"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24">
    <circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2" />
    <line
      x1="16"
      y1="16"
      x2="21"
      y2="21"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
    />
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24">
    <circle cx="12" cy="8" r="4" fill="currentColor" />
    <path
      d="M4 20 C4 16 8 14 12 14 C16 14 20 16 20 20"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
    />
  </symbol>
</svg>
```

### 3.2 使用图标

```html
<svg class="icon" aria-hidden="true">
  <use href="#icon-home" />
</svg>
```

```css
.icon {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
}
```

### 3.3 尺寸变体

```css
.icon-sm {
  width: 16px;
  height: 16px;
}
.icon-md {
  width: 24px;
  height: 24px;
}
.icon-lg {
  width: 32px;
  height: 32px;
}
.icon-xl {
  width: 48px;
  height: 48px;
}
```

```html
<svg class="icon icon-sm"><use href="#icon-home" /></svg>
<svg class="icon icon-lg"><use href="#icon-home" /></svg>
```

### 3.4 颜色变体

```css
.icon-primary {
  color: #4f5bd5;
}
.icon-success {
  color: #00b894;
}
.icon-danger {
  color: #d63031;
}
.icon-warning {
  color: #f9a825;
}
```

```html
<button class="btn">
  <svg class="icon icon-danger"><use href="#icon-delete" /></svg>
  删除
</button>
```

## 4. 可访问性基础

### 4.1 装饰性图标

纯装饰图标应隐藏于屏幕阅读器：

```html
<svg class="icon" aria-hidden="true">
  <use href="#icon-decorative" />
</svg>
```

`aria-hidden="true"` 让屏幕阅读器跳过此元素。

### 4.2 语义图标

传递信息的图标需提供替代文本：

```html
<svg class="icon" role="img" aria-label="搜索">
  <use href="#icon-search" />
</svg>

<!-- 或使用 title -->
<svg class="icon" role="img" aria-labelledby="search-title">
  <title id="search-title">搜索</title>
  <use href="#icon-search" />
</svg>
```

### 4.3 交互图标

可点击的图标需有合适语义：

```html
<button class="icon-btn" aria-label="关闭">
  <svg class="icon" aria-hidden="true">
    <use href="#icon-close" />
  </svg>
</button>
```

`aria-label` 在按钮上，SVG 本身 `aria-hidden`，避免重复朗读。

## 5. role 属性

| role 值        | 用途                           |
| -------------- | ------------------------------ |
| `img`          | 图像（需 aria-label 或 title） |
| `button`       | 按钮（通常外层用 `<button>`）  |
| `presentation` | 仅为展示，无语义               |
| `none`         | 等价于 presentation            |

```html
<!-- 图表作为整体图像 -->
<svg role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">2024 季度销售额</title>
  <desc id="chart-desc">柱状图展示 Q1-Q4 销售额，Q3 最高 210 万</desc>
  <!-- 图表内容 -->
</svg>
```

## 6. focus 与键盘导航

可交互的 SVG 元素需支持键盘操作：

```html
<svg class="icon-btn" role="button" tabindex="0" aria-label="菜单" id="menu-btn">
  <use href="#icon-menu" />
</svg>

<script>
  const btn = document.getElementById('menu-btn');
  btn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggleMenu();
    }
  });
  btn.addEventListener('click', toggleMenu);
</script>
```

### 6.1 focus 样式

```css
.icon-btn:focus-visible {
  outline: 2px solid #4f5bd5;
  outline-offset: 4px;
  border-radius: 4px;
}
```

`:focus-visible` 仅在键盘聚焦时显示，鼠标点击不显示。

## 7. prefers-reduced-motion

```css
.animated-icon {
  animation: spin 2s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .animated-icon {
    animation: none;
  }
}
```

尊重用户的系统偏好，禁用动画。

## 8. 颜色对比度

图标颜色需满足 WCAG 对比度要求：

| 文本类型        | 最小对比度（WCAG AA） |
| --------------- | --------------------- |
| 正常文本        | 4.5:1                 |
| 大文本（18pt+） | 3:1                   |
| 图标与图形      | 3:1                   |

```css
/* 检查对比度 */
.icon-primary {
  color: #4f5bd5; /* 对比度 4.8:1（白底） */
}

/* 错误：对比度不足 */
.icon-low-contrast {
  color: #ccc; /* 对比度 1.6:1 */
}
```

## 9. 图标按钮组件

```html
<button class="btn-icon btn-icon-danger" aria-label="删除项目">
  <svg class="icon" aria-hidden="true" viewBox="0 0 24 24">
    <path
      d="M3 6 H21 M8 6 V4 H16 V6 M6 6 L7 20 H17 L18 6"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</button>

<style>
  .btn-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 8px;
    background: transparent;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-icon:hover {
    background: rgba(0, 0, 0, 0.05);
  }
  .btn-icon:focus-visible {
    outline: 2px solid #4f5bd5;
    outline-offset: 2px;
  }
  .btn-icon-danger {
    color: #d63031;
  }
  .btn-icon-danger:hover {
    background: rgba(214, 48, 49, 0.1);
  }
  .icon {
    width: 20px;
    height: 20px;
  }
</style>
```

## 10. 动态图标

### 10.1 加载状态

```html
<svg class="icon icon-spin" viewBox="0 0 24 24" aria-label="加载中" role="img">
  <path
    d="M12 2 A10 10 0 0 1 22 12"
    fill="none"
    stroke="currentColor"
    stroke-width="3"
    stroke-linecap="round"
  />
</svg>

<style>
  .icon-spin {
    animation: spin 1s linear infinite;
    transform-origin: center;
    transform-box: fill-box;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
```

### 10.2 状态切换

```html
<button class="btn-toggle" aria-pressed="false" id="like-btn">
  <svg class="icon" viewBox="0 0 24 24">
    <path
      class="heart-outline"
      d="M12 21 L4 13 C2 11 2 8 4 6 C6 4 9 4 12 7 C15 4 18 4 20 6 C22 8 22 11 20 13 Z"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
    />
    <path
      class="heart-fill"
      d="M12 21 L4 13 C2 11 2 8 4 6 C6 4 9 4 12 7 C15 4 18 4 20 6 C22 8 22 11 20 13 Z"
      fill="currentColor"
    />
  </svg>
</button>

<style>
  .btn-toggle .heart-fill {
    display: none;
  }
  .btn-toggle[aria-pressed='true'] .heart-outline {
    display: none;
  }
  .btn-toggle[aria-pressed='true'] .heart-fill {
    display: block;
  }
  .btn-toggle[aria-pressed='true'] {
    color: #d63031;
  }
</style>

<script>
  const btn = document.getElementById('like-btn');
  btn.addEventListener('click', () => {
    const pressed = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', !pressed);
  });
</script>
```

`aria-pressed` 表示按钮按下状态，配合 CSS 切换图标。

## 11. 图标命名规范

```
icon-{category}-{name}
```

| 命名                  | 含义          |
| --------------------- | ------------- |
| `icon-action-home`    | 操作类 - 首页 |
| `icon-action-search`  | 操作类 - 搜索 |
| `icon-media-play`     | 媒体类 - 播放 |
| `icon-media-pause`    | 媒体类 - 暂停 |
| `icon-status-success` | 状态类 - 成功 |
| `icon-status-error`   | 状态类 - 错误 |
| `icon-nav-menu`       | 导航类 - 菜单 |
| `icon-nav-close`      | 导航类 - 关闭 |

## 12. 图标集管理

### 12.1 目录结构

```
src/
  assets/
    icons/
      action/
        home.svg
        search.svg
      media/
        play.svg
        pause.svg
      status/
        success.svg
        error.svg
  sprite/
    icons.svg       # 构建生成的 sprite
    icons.ts        # TypeScript 声明
```

### 12.2 构建脚本

```javascript
// scripts/build-icons.js
const fs = require('fs');
const path = require('path');
const { optimize } = require('svgo');

const iconsDir = path.join(__dirname, '../src/assets/icons');
const outputPath = path.join(__dirname, '../src/sprite/icons.svg');

function buildSprite() {
  const symbols = [];
  function walk(dir) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        walk(fullPath);
      } else if (item.endsWith('.svg')) {
        const name = path.basename(item, '.svg');
        const content = fs.readFileSync(fullPath, 'utf8');
        const optimized = optimize(content, {
          plugins: [{ name: 'preset-default' }, { name: 'removeDimensions' }],
        }).data;
        // 提取内容并转为 symbol
        const inner = optimized.replace(/<svg[^>]*>|<\/svg>/g, '');
        symbols.push(`<symbol id="icon-${name}" viewBox="0 0 24 24">${inner}</symbol>`);
      }
    }
  }
  walk(iconsDir);
  const sprite = `<svg xmlns="http://www.w3.org/2000/svg" style="display:none">${symbols.join('')}</svg>`;
  fs.writeFileSync(outputPath, sprite);
  console.log(`Built ${symbols.length} icons`);
}

buildSprite();
```

## 13. 实战：完整的图标按钮系统

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .icon {
        width: 24px;
        height: 24px;
        fill: none;
        stroke: currentColor;
        stroke-width: 2;
      }
      .btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background: #fff;
        color: #333;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.2s;
      }
      .btn:hover {
        background: #f5f5f5;
        border-color: #ccc;
      }
      .btn:focus-visible {
        outline: 2px solid #4f5bd5;
        outline-offset: 2px;
      }
      .btn-primary {
        background: #4f5bd5;
        border-color: #4f5bd5;
        color: #fff;
      }
      .btn-primary:hover {
        background: #3a47b8;
      }
      .btn-danger {
        color: #d63031;
        border-color: #d63031;
      }
      .btn-danger:hover {
        background: #fbe9e7;
      }
      .btn-icon-only {
        padding: 8px;
      }
    </style>
  </head>
  <body>
    <svg style="display:none">
      <symbol id="icon-plus" viewBox="0 0 24 24">
        <path d="M12 5 V19 M5 12 H19" stroke-linecap="round" />
      </symbol>
      <symbol id="icon-trash" viewBox="0 0 24 24">
        <path
          d="M3 6 H21 M8 6 V4 H16 V6 M6 6 L7 20 H17 L18 6"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </symbol>
      <symbol id="icon-check" viewBox="0 0 24 24">
        <path d="M5 12 L10 17 L19 8" stroke-linecap="round" stroke-linejoin="round" />
      </symbol>
    </svg>

    <button class="btn btn-primary">
      <svg class="icon" aria-hidden="true"><use href="#icon-plus" /></svg>
      新建项目
    </button>

    <button class="btn btn-danger btn-icon-only" aria-label="删除">
      <svg class="icon" aria-hidden="true"><use href="#icon-trash" /></svg>
    </button>

    <button class="btn" aria-pressed="false" id="check-btn">
      <svg class="icon" aria-hidden="true"><use href="#icon-check" /></svg>
      标记完成
    </button>

    <script>
      document.getElementById('check-btn').addEventListener('click', function () {
        const pressed = this.getAttribute('aria-pressed') === 'true';
        this.setAttribute('aria-pressed', !pressed);
      });
    </script>
  </body>
</html>
```

下一篇以综合项目串联所有知识点。
## 图标定义

**symbol 定义图标**
`<symbol id="<icon-id>" viewBox="0 0 24 24">...</symbol>`
```html
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <!-- 统一 24x24 画布,所有图标共用 viewBox -->
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path
      d="M3 12 L12 3 L21 12 M5 10 V21 H19 V10"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24">
    <circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2" />
    <line
      x1="16"
      y1="16"
      x2="21"
      y2="21"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
    />
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24">
    <circle cx="12" cy="8" r="4" fill="currentColor" />
    <path
      d="M4 20 C4 16 8 14 12 14 C16 14 20 16 20 20"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
    />
  </symbol>
</svg>
```

### symbol 元素属性表

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| `id` | 唯一标识符(被 use 引用) | `icon-home` |
| `viewBox` | 视口坐标系 | `0 0 24 24` |
| `width` | 宽度(通常省略,由 use 控制) | `24` |
| `height` | 高度(通常省略,由 use 控制) | `24` |
| `fill` | 默认填充 | `none` |
| `stroke` | 默认描边 | `currentColor` |

---

## 图标使用

**use 引用图标**
`<svg class="<类>" aria-hidden="true"><use href="#<icon-id>" /></svg>`
```html
<svg class="icon" aria-hidden="true">
  <use href="#icon-home" />
</svg>
```

```css
.icon {
  width: 24px;
  height: 24px;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
}
```

### use 元素属性表

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| `href` | 引用 symbol 的 id | `#icon-home` |
| `x` | x 坐标偏移 | `0` |
| `y` | y 坐标偏移 | `0` |
| `width` | 宽度(覆盖 symbol) | `24` |
| `height` | 高度(覆盖 symbol) | `24` |

---

## 尺寸变体

**图标尺寸 CSS**
`.<size-class> { width: <px>; height: <px>; }`
```css
.icon-sm { width: 16px; height: 16px; }
.icon-md { width: 24px; height: 24px; }
.icon-lg { width: 32px; height: 32px; }
.icon-xl { width: 48px; height: 48px; }
```

```html
<svg class="icon icon-sm"><use href="#icon-home" /></svg>
<svg class="icon icon-md"><use href="#icon-home" /></svg>
<svg class="icon icon-lg"><use href="#icon-home" /></svg>
<svg class="icon icon-xl"><use href="#icon-home" /></svg>
```

---

## 颜色变体 currentColor

**currentColor 主题化**
`<element fill="currentColor" [stroke]="currentColor" />`
```html
<!-- 使用 currentColor,颜色继承父元素 color -->
<symbol id="icon-home" viewBox="0 0 24 24">
  <path fill="currentColor" stroke="currentColor" />
</symbol>
```

```css
.icon-primary { color: #4f5bd5; }
.icon-success { color: #00b894; }
.icon-danger { color: #d63031; }
.icon-warning { color: #f9a825; }
```

```html
<button class="btn">
  <svg class="icon icon-danger"><use href="#icon-delete" /></svg>
  删除
</button>
```

---

## 描边一致性

**统一描边属性**
`<path stroke-width="<width>" stroke-linecap="<cap>" stroke-linejoin="<join>" />`
```html
<symbol id="icon-edit" viewBox="0 0 24 24">
  <path
    d="M3 17.25 V21 H6.75 L17.81 9.94 L14.06 6.19 L3 17.25 Z"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</symbol>
```

### 描边属性表

| 属性 | 说明 | 可选值 |
| --- | --- | --- |
| `stroke-width` | 描边宽度 | `2`(像素,统一) |
| `stroke-linecap` | 线段端点样式 | `butt` / `round` / `square` |
| `stroke-linejoin` | 拐角连接样式 | `miter` / `round` / `bevel` |

---

## 像素网格对齐

**整数坐标对齐**
`<path d="M <int> <int> L <int> <int>" />`
```html
<!-- 清晰:整数坐标 -->
<path d="M 0 0 L 10 0" stroke-width="1" />

<!-- 模糊:坐标落在 .5(抗锯齿) -->
<path d="M 0.5 0.5 L 10.5 0.5" stroke-width="1" />
```

---

## 装饰性图标 aria-hidden

**纯装饰图标隐藏**
`<svg aria-hidden="true">...</svg>`
```html
<svg class="icon" aria-hidden="true">
  <use href="#icon-decorative" />
</svg>
```

`aria-hidden="true"` 让屏幕阅读器跳过此元素,适用于纯装饰图标。

---

## 语义图标 aria-label

**带替代文本的图标**
`<svg role="img" aria-label="<文本>">...</svg>`
```html
<svg class="icon" role="img" aria-label="搜索">
  <use href="#icon-search" />
</svg>
```

**title 子元素提供标签**
`<svg role="img" aria-labelledby="<title-id>"><title id="...">...</title>...</svg>`
```html
<svg class="icon" role="img" aria-labelledby="search-title">
  <title id="search-title">搜索</title>
  <use href="#icon-search" />
</svg>
```

---

## 交互图标按钮

**可点击图标按钮**
`<button aria-label="<文本>"><svg aria-hidden="true">...</svg></button>`
```html
<button class="icon-btn" aria-label="关闭">
  <svg class="icon" aria-hidden="true">
    <use href="#icon-close" />
  </svg>
</button>
```

`aria-label` 放在外层 button 上,SVG 本身 `aria-hidden`,避免重复朗读。

---

## role 属性

**SVG role 语义**
`<svg role="<role-value>" aria-labelledby="<id1> [<id2>]">`
```html
<svg role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">2024 季度销售额</title>
  <desc id="chart-desc">柱状图展示 Q1-Q4 销售额,Q3 最高 210 万</desc>
  <!-- 图表内容 -->
</svg>
```

### role 取值表

| role 值 | 用途 |
| --- | --- |
| `img` | 图像(需 aria-label 或 title) |
| `button` | 按钮(通常外层用 `<button>`) |
| `presentation` | 仅为展示,无语义 |
| `none` | 等价于 presentation |
| `graphics-document` | 图形文档(SVG 2) |
| `graphics-symbol` | 图形符号(SVG 2) |

---

## desc 元素描述

**desc 长描述**
`<svg><title>...</title><desc>...</desc>...</svg>`
```html
<svg viewBox="0 0 200 200" role="img" aria-labelledby="t d">
  <title id="t">销售趋势图</title>
  <desc id="d">折线图显示 2024 年 1-12 月销售额变化</desc>
  <polyline points="20,150 50,120 80,140 110,90 140,110 170,70" />
</svg>
```

---

## tabindex 与键盘导航

**可聚焦 SVG**
`<svg role="button" tabindex="0" aria-label="<文本>" id="<id>">`
```html
<svg class="icon-btn" role="button" tabindex="0" aria-label="菜单" id="menu-btn">
  <use href="#icon-menu" />
</svg>

<script>
  const btn = document.getElementById('menu-btn');
  btn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggleMenu();
    }
  });
  btn.addEventListener('click', toggleMenu);
</script>
```

---

## focus 可见样式

**focus-visible 样式**
`<selector>:focus-visible { outline: <style> <color> <width>; outline-offset: <px>; }`
```css
.icon-btn:focus-visible {
  outline: 2px solid #4f5bd5;
  outline-offset: 4px;
  border-radius: 4px;
}
```

`:focus-visible` 仅在键盘聚焦时显示轮廓,鼠标点击不显示。

---

## prefers-reduced-motion

**禁用动画媒体查询**
`@media (prefers-reduced-motion: reduce) { <selector> { animation: none; } }`
```css
.animated-icon {
  animation: spin 2s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
  .animated-icon {
    animation: none;
  }
}
```

---

## aria-pressed 状态切换

**按钮按下状态**
`<button aria-pressed="<bool>" id="<id>">...</button>`
```html
<button class="btn-toggle" aria-pressed="false" id="like-btn">
  <svg class="icon" viewBox="0 0 24 24">
    <path
      class="heart-outline"
      d="M12 21 L4 13 C2 11 2 8 4 6 C6 4 9 4 12 7 C15 4 18 4 20 6 C22 8 22 11 20 13 Z"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
    />
    <path
      class="heart-fill"
      d="M12 21 L4 13 C2 11 2 8 4 6 C6 4 9 4 12 7 C15 4 18 4 20 6 C22 8 22 11 20 13 Z"
      fill="currentColor"
    />
  </svg>
</button>

<style>
  .btn-toggle .heart-fill { display: none; }
  .btn-toggle[aria-pressed='true'] .heart-outline { display: none; }
  .btn-toggle[aria-pressed='true'] .heart-fill { display: block; }
  .btn-toggle[aria-pressed='true'] { color: #d63031; }
</style>

<script>
  const btn = document.getElementById('like-btn');
  btn.addEventListener('click', () => {
    const pressed = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', !pressed);
  });
</script>
```

### aria 状态属性表

| 属性 | 说明 | 取值 |
| --- | --- | --- |
| `aria-pressed` | 按钮按下状态 | `true` / `false` / `mixed` |
| `aria-expanded` | 展开/折叠状态 | `true` / `false` |
| `aria-hidden` | 对辅助技术隐藏 | `true` / `false` |
| `aria-label` | 可访问名称 | 任意字符串 |
| `aria-labelledby` | 引用 ID 作为名称 | `id [id2 ...]` |
| `aria-describedby` | 引用 ID 作为描述 | `id [id2 ...]` |
| `aria-disabled` | 禁用状态 | `true` / `false` |

---

## 加载动画图标

**旋转加载图标**
`<svg class="<spin-class>" [aria-label]="..." [role]="img">`
```html
<svg class="icon icon-spin" viewBox="0 0 24 24" aria-label="加载中" role="img">
  <path
    d="M12 2 A10 10 0 0 1 22 12"
    fill="none"
    stroke="currentColor"
    stroke-width="3"
    stroke-linecap="round"
  />
</svg>

<style>
  .icon-spin {
    animation: spin 1s linear infinite;
    transform-origin: center;
    transform-box: fill-box;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
```

---

## 图标按钮组件

**完整图标按钮**
`<button class="btn-icon <variant>" aria-label="<文本>"><svg class="icon" aria-hidden="true">...</svg></button>`
```html
<button class="btn-icon btn-icon-danger" aria-label="删除项目">
  <svg class="icon" aria-hidden="true" viewBox="0 0 24 24">
    <path
      d="M3 6 H21 M8 6 V4 H16 V6 M6 6 L7 20 H17 L18 6"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</button>

<style>
  .btn-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 8px;
    background: transparent;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-icon:hover { background: rgba(0, 0, 0, 0.05); }
  .btn-icon:focus-visible {
    outline: 2px solid #4f5bd5;
    outline-offset: 2px;
  }
  .btn-icon-danger { color: #d63031; }
  .btn-icon-danger:hover { background: rgba(214, 48, 49, 0.1); }
  .icon { width: 20px; height: 20px; }
</style>
```

---

## 颜色对比度属性

**主题色对比度**
`<selector> { color: <hex>; }`
```css
/* 对比度 4.8:1(白底),满足 WCAG AA */
.icon-primary { color: #4f5bd5; }

/* 对比度 1.6:1(白底),不满足 WCAG AA */
.icon-low-contrast { color: #ccc; }
```

### WCAG 对比度要求表

| 文本类型 | 最小对比度(WCAG AA) |
| --- | --- |
| 正常文本 | 4.5:1 |
| 大文本(18pt+) | 3:1 |
| 图标与图形 | 3:1 |

---

## 图标 sprite 模式

**SVG sprite 定义**
`<svg xmlns="..." style="display:none"><symbol id="..." viewBox="...">...</symbol>...</svg>`
```html
<!-- 隐藏的 sprite 文件,所有图标集中定义 -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path d="..." fill="none" stroke="currentColor" stroke-width="2" />
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24">
    <circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="2" />
  </symbol>
</svg>

<!-- 通过 use 引用 -->
<svg class="icon"><use href="#icon-home" /></svg>
```

---

## currentColor 与 CSS 变量穿透

**主题切换**
`<symbol id="..."><path fill="var(--icon-color)" /></symbol>`
```html
<symbol id="icon-themed" viewBox="0 0 24 24">
  <path
    d="M12 2 L15 9 L22 9 L17 14 L19 21 L12 17 L5 21 L7 14 L2 9 L9 9 Z"
    fill="var(--icon-color, currentColor)"
  />
</symbol>
```

```css
:root {
  --icon-color: #4f5bd5;
}
.dark-theme {
  --icon-color: #7c89ff;
}
```

---

## SVG title 与 desc 元素

**结构化描述**
`<svg><title>...</title><desc>...</desc>...</svg>`
```html
<svg viewBox="0 0 100 100" role="img" aria-labelledby="icon-t icon-d">
  <title id="icon-t">警告</title>
  <desc id="icon-d">黄色三角形带感叹号,表示警告状态</desc>
  <polygon points="50,10 90,90 10,90" fill="#f9a825" />
  <text x="50" y="70" text-anchor="middle" font-size="40" fill="#fff">!</text>
</svg>
```

### title 与 desc 属性表

| 元素 | 用途 | 必需属性 |
| --- | --- | --- |
| `<title>` | 简短可访问名称 | `id`(配合 aria-labelledby) |
| `<desc>` | 详细描述 | `id`(配合 aria-describedby) |

<!-- ============ 文档分隔线：012-svg/018-SVGPracticeProject.md ============ -->

## 1. 项目一：环形进度条

结合 path、stroke-dasharray、动画的综合应用。

```html
<svg viewBox="0 0 200 200" width="200" height="200">
  <defs>
    <linearGradient id="progress-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
    <filter id="progress-glow">
      <feGaussianBlur stdDeviation="3" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- 背景圆 -->
  <circle cx="100" cy="100" r="80" fill="none" stroke="#e0e0e0" stroke-width="12" />

  <!-- 进度圆 -->
  <circle
    id="progress-circle"
    cx="100"
    cy="100"
    r="80"
    fill="none"
    stroke="url(#progress-grad)"
    stroke-width="12"
    stroke-linecap="round"
    stroke-dasharray="502"
    stroke-dashoffset="502"
    transform="rotate(-90 100 100)"
    filter="url(#progress-glow)"
  />

  <!-- 中心文本 -->
  <text
    id="progress-text"
    x="100"
    y="100"
    text-anchor="middle"
    dominant-baseline="middle"
    font-size="36"
    font-weight="bold"
    fill="#333"
  >
    0%
  </text>
  <text x="100" y="130" text-anchor="middle" font-size="12" fill="#999">已完成</text>
</svg>

<script>
  const circle = document.getElementById('progress-circle');
  const text = document.getElementById('progress-text');
  const circumference = 2 * Math.PI * 80; // 约 502

  function setProgress(percent) {
    const offset = circumference - (percent / 100) * circumference;
    circle.style.strokeDashoffset = offset;
    text.textContent = percent + '%';
  }

  // 动画到 75%
  let current = 0;
  const target = 75;
  const duration = 2000;
  const start = performance.now();

  function animate(now) {
    const elapsed = now - start;
    const t = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - t, 3); // ease-out cubic
    current = Math.round(eased * target);
    setProgress(current);
    if (t < 1) requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);
</script>
```

**要点**：

- 圆周长 = 2πr = 502
- `stroke-dasharray` 设为周长，`stroke-dashoffset` 控制进度
- `rotate(-90 100 100)` 从 12 点钟方向开始
- `ease-out cubic` 缓动让进度增长自然减速

## 2. 项目二：动态数据图表

完整柱状图，含坐标轴、数据标签、交互悬停。

```html
<svg viewBox="0 0 600 400" class="chart" role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">2024 季度销售额</title>
  <desc id="chart-desc">柱状图展示 Q1 至 Q4 销售额，单位：万元</desc>

  <defs>
    <linearGradient id="bar-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#5b6ee8" />
      <stop offset="100%" stop-color="#4f5bd5" />
    </linearGradient>
    <filter id="bar-shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.1" />
    </filter>
  </defs>

  <style>
    .bar {
      transition: opacity 0.2s;
      cursor: pointer;
    }
    .bar:hover {
      opacity: 0.8;
    }
    .label {
      font-family: sans-serif;
      font-size: 12px;
      fill: #666;
    }
    .value {
      font-family: sans-serif;
      font-size: 13px;
      fill: #333;
      font-weight: bold;
    }
    .axis {
      stroke: #ccc;
    }
  </style>

  <!-- Y 轴 -->
  <line class="axis" x1="60" y1="40" x2="60" y2="320" />
  <!-- X 轴 -->
  <line class="axis" x1="60" y1="320" x2="560" y2="320" />

  <!-- 网格线 -->
  <g stroke="#f0f0f0" stroke-dasharray="4 4">
    <line x1="60" y1="80" x2="560" y2="80" />
    <line x1="60" y1="160" x2="560" y2="160" />
    <line x1="60" y1="240" x2="560" y2="240" />
  </g>

  <!-- Y 轴标签 -->
  <g class="label" text-anchor="end">
    <text x="55" y="324">0</text>
    <text x="55" y="244">75</text>
    <text x="55" y="164">150</text>
    <text x="55" y="84">225</text>
  </g>

  <!-- 柱子由 JS 动态生成 -->
  <g id="bars"></g>
</svg>

<script>
  const data = [
    { label: 'Q1', value: 120 },
    { label: 'Q2', value: 165 },
    { label: 'Q3', value: 210 },
    { label: 'Q4', value: 180 },
  ];

  const svgNS = 'http://www.w3.org/2000/svg';
  const barsGroup = document.getElementById('bars');
  const maxValue = 250;
  const chartHeight = 280;
  const barWidth = 80;
  const gap = 40;
  const startX = 100;

  data.forEach((d, i) => {
    const barHeight = (d.value / maxValue) * chartHeight;
    const x = startX + i * (barWidth + gap);
    const y = 320 - barHeight;

    // 柱子
    const bar = document.createElementNS(svgNS, 'rect');
    bar.setAttribute('class', 'bar');
    bar.setAttribute('x', x);
    bar.setAttribute('y', y);
    bar.setAttribute('width', barWidth);
    bar.setAttribute('height', barHeight);
    bar.setAttribute('fill', 'url(#bar-grad)');
    bar.setAttribute('filter', 'url(#bar-shadow)');
    bar.setAttribute('rx', 4);

    // 初始高度 0，动画展开
    bar.setAttribute('height', 0);
    bar.setAttribute('y', 320);
    bar.style.transition = 'all 0.8s cubic-bezier(0.4, 0, 0.2, 1)';
    bar.style.transitionDelay = i * 0.1 + 's';

    barsGroup.appendChild(bar);

    // 触发动画
    requestAnimationFrame(() => {
      bar.setAttribute('height', barHeight);
      bar.setAttribute('y', y);
    });

    // X 轴标签
    const label = document.createElementNS(svgNS, 'text');
    label.setAttribute('class', 'label');
    label.setAttribute('x', x + barWidth / 2);
    label.setAttribute('y', 340);
    label.setAttribute('text-anchor', 'middle');
    label.textContent = d.label;
    barsGroup.appendChild(label);

    // 数值标签
    const value = document.createElementNS(svgNS, 'text');
    value.setAttribute('class', 'value');
    value.setAttribute('x', x + barWidth / 2);
    value.setAttribute('y', y - 8);
    value.setAttribute('text-anchor', 'middle');
    value.textContent = d.value;
    value.style.opacity = '0';
    value.style.transition = 'opacity 0.4s';
    value.style.transitionDelay = i * 0.1 + 0.4 + 's';
    barsGroup.appendChild(value);

    requestAnimationFrame(() => {
      value.style.opacity = '1';
    });

    // 交互
    bar.addEventListener('click', () => {
      alert(`${d.label}: ${d.value} 万元`);
    });
  });
</script>
```

## 3. 项目三：动画 Logo

结合渐变、路径动画、变换。

```html
<svg viewBox="0 0 400 120" width="400" height="120">
  <defs>
    <linearGradient id="logo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5">
        <animate
          attributeName="stop-color"
          values="#4f5bd5;#00b894;#4f5bd5"
          dur="6s"
          repeatCount="indefinite"
        />
      </stop>
      <stop offset="100%" stop-color="#00b894">
        <animate
          attributeName="stop-color"
          values="#00b894;#4f5bd5;#00b894"
          dur="6s"
          repeatCount="indefinite"
        />
      </stop>
    </linearGradient>
    <filter id="logo-glow">
      <feGaussianBlur stdDeviation="2" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .logo-text {
      font-family: 'Inter', sans-serif;
      font-size: 48px;
      font-weight: bold;
      fill: url(#logo-grad);
      filter: url(#logo-glow);
    }
    .logo-letter {
      transform-origin: center;
      transform-box: fill-box;
    }
    .logo-letter:nth-child(1) {
      animation: bounce 2s ease-in-out infinite;
    }
    .logo-letter:nth-child(2) {
      animation: bounce 2s ease-in-out infinite 0.1s;
    }
    .logo-letter:nth-child(3) {
      animation: bounce 2s ease-in-out infinite 0.2s;
    }
    .logo-letter:nth-child(4) {
      animation: bounce 2s ease-in-out infinite 0.3s;
    }
    .logo-letter:nth-child(5) {
      animation: bounce 2s ease-in-out infinite 0.4s;
    }
    .logo-letter:nth-child(6) {
      animation: bounce 2s ease-in-out infinite 0.5s;
    }
    @keyframes bounce {
      0%,
      100% {
        transform: translateY(0);
      }
      50% {
        transform: translateY(-8px);
      }
    }
  </style>

  <text x="200" y="75" text-anchor="middle" class="logo-text">
    <tspan class="logo-letter">F</tspan>
    <tspan class="logo-letter">A</tspan>
    <tspan class="logo-letter">N</tspan>
    <tspan class="logo-letter">D</tspan>
    <tspan class="logo-letter">E</tspan>
    <tspan class="logo-letter">X</tspan>
  </text>

  <!-- 装饰下划线 -->
  <path
    d="M 100 95 Q 200 105 300 95"
    fill="none"
    stroke="url(#logo-grad)"
    stroke-width="2"
    stroke-linecap="round"
  >
    <animate
      attributeName="d"
      values="M 100 95 Q 200 105 300 95; M 100 95 Q 200 85 300 95; M 100 95 Q 200 105 300 95"
      dur="3s"
      repeatCount="indefinite"
    />
  </path>
</svg>
```

## 4. 项目四：交互式地图

简化版中国地图节点示意。

```html
<svg viewBox="0 0 800 600" class="map" role="img" aria-labelledby="map-title">
  <title id="map-title">节点分布图</title>

  <defs>
    <radialGradient id="node-grad">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#3a47b8" />
    </radialGradient>
    <filter id="node-glow">
      <feGaussianBlur stdDeviation="4" result="b" />
      <feMerge>
        <feMergeNode in="b" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#f0f0f0" stroke-width="1" />
    </pattern>
  </defs>

  <style>
    .node {
      cursor: pointer;
      transition: transform 0.2s;
      transform-origin: center;
      transform-box: fill-box;
    }
    .node:hover {
      transform: scale(1.3);
    }
    .label {
      font-family: sans-serif;
      font-size: 12px;
      fill: #333;
      pointer-events: none;
    }
    .connection {
      stroke: #4f5bd5;
      stroke-width: 1.5;
      opacity: 0.4;
    }
    .pulse-ring {
      fill: none;
      stroke: #4f5bd5;
      stroke-width: 2;
    }
  </style>

  <!-- 背景网格 -->
  <rect width="800" height="600" fill="url(#grid)" />

  <!-- 连接线 -->
  <g class="connections">
    <line class="connection" x1="200" y1="200" x2="400" y2="300" />
    <line class="connection" x1="400" y1="300" x2="600" y2="200" />
    <line class="connection" x1="400" y1="300" x2="500" y2="450" />
    <line class="connection" x1="200" y1="200" x2="300" y2="450" />
  </g>

  <!-- 节点 -->
  <g class="nodes">
    <g class="node-group" transform="translate(200, 200)">
      <circle class="pulse-ring" r="15">
        <animate attributeName="r" values="15;25;15" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite" />
      </circle>
      <circle class="node" r="8" fill="url(#node-grad)" filter="url(#node-glow)" />
      <text class="label" y="-15" text-anchor="middle">北京</text>
    </g>

    <g class="node-group" transform="translate(400, 300)">
      <circle class="pulse-ring" r="15">
        <animate
          attributeName="r"
          values="15;25;15"
          dur="2s"
          begin="0.5s"
          repeatCount="indefinite"
        />
        <animate
          attributeName="opacity"
          values="1;0;1"
          dur="2s"
          begin="0.5s"
          repeatCount="indefinite"
        />
      </circle>
      <circle class="node" r="8" fill="url(#node-grad)" filter="url(#node-glow)" />
      <text class="label" y="-15" text-anchor="middle">武汉</text>
    </g>

    <g class="node-group" transform="translate(600, 200)">
      <circle class="pulse-ring" r="15">
        <animate attributeName="r" values="15;25;15" dur="2s" begin="1s" repeatCount="indefinite" />
        <animate
          attributeName="opacity"
          values="1;0;1"
          dur="2s"
          begin="1s"
          repeatCount="indefinite"
        />
      </circle>
      <circle class="node" r="8" fill="url(#node-grad)" filter="url(#node-glow)" />
      <text class="label" y="-15" text-anchor="middle">上海</text>
    </g>

    <g class="node-group" transform="translate(300, 450)">
      <circle class="pulse-ring" r="15">
        <animate
          attributeName="r"
          values="15;25;15"
          dur="2s"
          begin="1.5s"
          repeatCount="indefinite"
        />
        <animate
          attributeName="opacity"
          values="1;0;1"
          dur="2s"
          begin="1.5s"
          repeatCount="indefinite"
        />
      </circle>
      <circle class="node" r="8" fill="url(#node-grad)" filter="url(#node-glow)" />
      <text class="label" y="-15" text-anchor="middle">成都</text>
    </g>

    <g class="node-group" transform="translate(500, 450)">
      <circle class="pulse-ring" r="15">
        <animate attributeName="r" values="15;25;15" dur="2s" begin="2s" repeatCount="indefinite" />
        <animate
          attributeName="opacity"
          values="1;0;1"
          dur="2s"
          begin="2s"
          repeatCount="indefinite"
        />
      </circle>
      <circle class="node" r="8" fill="url(#node-grad)" filter="url(#node-glow)" />
      <text class="label" y="-15" text-anchor="middle">广州</text>
    </g>
  </g>

  <script>
    document.querySelectorAll('.node').forEach((node) => {
      node.addEventListener('click', (e) => {
        const group = e.target.closest('.node-group');
        const label = group.querySelector('.label').textContent;
        alert(`选中：${label}`);
      });
    });
  </script>
</svg>
```

## 5. 项目五：加载动画集

常用加载动画合集。

```html
<svg viewBox="0 0 300 100" width="300" height="100">
  <style>
    .spinner-1 {
      animation: spin 1.5s linear infinite;
      transform-origin: center;
      transform-box: fill-box;
    }
    .spinner-2 circle:nth-child(1) {
      animation: fade 1.2s ease-in-out infinite;
    }
    .spinner-2 circle:nth-child(2) {
      animation: fade 1.2s ease-in-out infinite 0.2s;
    }
    .spinner-2 circle:nth-child(3) {
      animation: fade 1.2s ease-in-out infinite 0.4s;
    }
    .spinner-3 {
      animation: bounce 1s ease-in-out infinite;
      transform-origin: center;
      transform-box: fill-box;
    }
    @keyframes spin {
      to {
        transform: rotate(360deg);
      }
    }
    @keyframes fade {
      0%,
      100% {
        opacity: 0.3;
      }
      50% {
        opacity: 1;
      }
    }
    @keyframes bounce {
      0%,
      100% {
        transform: scaleY(1);
      }
      50% {
        transform: scaleY(0.5);
      }
    }
  </style>

  <!-- 旋转环 -->
  <g transform="translate(50, 50)">
    <g class="spinner-1">
      <circle
        r="20"
        fill="none"
        stroke="#4f5bd5"
        stroke-width="3"
        stroke-dasharray="30 95"
        stroke-linecap="round"
      />
    </g>
  </g>

  <!-- 三点跳动 -->
  <g class="spinner-2" transform="translate(150, 50)">
    <circle cx="-15" r="6" fill="#4f5bd5" />
    <circle cx="0" r="6" fill="#4f5bd5" />
    <circle cx="15" r="6" fill="#4f5bd5" />
  </g>

  <!-- 脉冲条 -->
  <g transform="translate(250, 50)">
    <rect x="-15" y="-20" width="6" height="40" rx="3" fill="#4f5bd5" class="spinner-3" />
    <rect
      x="-3"
      y="-20"
      width="6"
      height="40"
      rx="3"
      fill="#4f5bd5"
      class="spinner-3"
      style="animation-delay: 0.2s"
    />
    <rect
      x="9"
      y="-20"
      width="6"
      height="40"
      rx="3"
      fill="#4f5bd5"
      class="spinner-3"
      style="animation-delay: 0.4s"
    />
  </g>
</svg>
```

## 6. 项目六：折线图

```html
<svg viewBox="0 0 600 300" class="line-chart" role="img" aria-labelledby="line-title">
  <title id="line-title">月度趋势图</title>

  <defs>
    <linearGradient id="area-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#4f5bd5" stop-opacity="0" />
    </linearGradient>
  </defs>

  <style>
    .grid-line {
      stroke: #f0f0f0;
    }
    .axis-line {
      stroke: #ccc;
    }
    .label {
      font-family: sans-serif;
      font-size: 11px;
      fill: #666;
    }
    .data-point {
      fill: #fff;
      stroke: #4f5bd5;
      stroke-width: 2;
      cursor: pointer;
      transition: r 0.2s;
    }
    .data-point:hover {
      r: 6;
    }
  </style>

  <!-- 网格 -->
  <g class="grid-line">
    <line x1="60" y1="50" x2="560" y2="50" />
    <line x1="60" y1="120" x2="560" y2="120" />
    <line x1="60" y1="190" x2="560" y2="190" />
  </g>

  <!-- 坐标轴 -->
  <line class="axis-line" x1="60" y1="260" x2="560" y2="260" />
  <line class="axis-line" x1="60" y1="20" x2="60" y2="260" />

  <!-- Y 轴标签 -->
  <g class="label" text-anchor="end">
    <text x="55" y="264">0</text>
    <text x="55" y="194">30</text>
    <text x="55" y="124">60</text>
    <text x="55" y="54">90</text>
  </g>

  <!-- 数据 -->
  <!-- 月份 -->
  <g class="label" text-anchor="middle">
    <text x="100" y="280">1月</text>
    <text x="180" y="280">2月</text>
    <text x="260" y="280">3月</text>
    <text x="340" y="280">4月</text>
    <text x="420" y="280">5月</text>
    <text x="500" y="280">6月</text>
  </g>

  <!-- 折线 -->
  <path
    d="M 100 200 L 180 160 L 260 180 L 340 100 L 420 80 L 500 60"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="2.5"
    stroke-linecap="round"
    stroke-linejoin="round"
    stroke-dasharray="800"
    stroke-dashoffset="800"
    id="line-path"
  >
    <animate attributeName="stroke-dashoffset" from="800" to="0" dur="2s" fill="freeze" />
  </path>

  <!-- 面积 -->
  <path
    d="M 100 200 L 180 160 L 260 180 L 340 100 L 420 80 L 500 60 L 500 260 L 100 260 Z"
    fill="url(#area-grad)"
    opacity="0"
  >
    <animate attributeName="opacity" from="0" to="1" dur="1s" begin="1.5s" fill="freeze" />
  </path>

  <!-- 数据点 -->
  <g id="data-points">
    <circle class="data-point" cx="100" cy="200" r="4" />
    <circle class="data-point" cx="180" cy="160" r="4" />
    <circle class="data-point" cx="260" cy="180" r="4" />
    <circle class="data-point" cx="340" cy="100" r="4" />
    <circle class="data-point" cx="420" cy="80" r="4" />
    <circle class="data-point" cx="500" cy="60" r="4" />
  </g>
</svg>

<script>
  const values = [25, 35, 30, 65, 75, 85];
  const points = document.querySelectorAll('.data-point');
  points.forEach((p, i) => {
    p.setAttribute('data-value', values[i] + '万');
    p.style.opacity = '0';
    p.style.transition = 'opacity 0.3s';
    setTimeout(
      () => {
        p.style.opacity = '1';
      },
      2000 + i * 100
    );
    p.addEventListener('click', () => {
      alert(`数值：${values[i]}万`);
    });
  });
</script>
```

## 7. 项目七：饼图

```html
<svg viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <filter id="pie-shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.15" />
    </filter>
  </defs>

  <style>
    .slice {
      cursor: pointer;
      transition: transform 0.2s;
      transform-origin: center;
      transform-box: fill-box;
    }
    .slice:hover {
      transform: scale(1.05);
    }
    .label {
      font-family: sans-serif;
      font-size: 14px;
      fill: #fff;
      font-weight: bold;
    }
  </style>

  <g id="pie" transform="translate(200, 200)" filter="url(#pie-shadow)">
    <!-- 由 JS 生成 -->
  </g>
</svg>

<script>
  const data = [
    { label: '产品 A', value: 35, color: '#4f5bd5' },
    { label: '产品 B', value: 25, color: '#00b894' },
    { label: '产品 C', value: 20, color: '#f9a825' },
    { label: '产品 D', value: 15, color: '#d63031' },
    { label: '其他', value: 5, color: '#8854d0' },
  ];

  const svgNS = 'http://www.w3.org/2000/svg';
  const pie = document.getElementById('pie');
  const radius = 120;
  const total = data.reduce((sum, d) => sum + d.value, 0);

  let cumAngle = -90; // 从 12 点钟方向开始

  data.forEach((d, i) => {
    const angle = (d.value / total) * 360;
    const startAngle = cumAngle;
    const endAngle = cumAngle + angle;

    const startRad = (startAngle * Math.PI) / 180;
    const endRad = (endAngle * Math.PI) / 180;

    const x1 = radius * Math.cos(startRad);
    const y1 = radius * Math.sin(startRad);
    const x2 = radius * Math.cos(endRad);
    const y2 = radius * Math.sin(endRad);

    const largeArc = angle > 180 ? 1 : 0;

    const path = document.createElementNS(svgNS, 'path');
    path.setAttribute('class', 'slice');
    path.setAttribute(
      'd',
      `M 0 0 L ${x1} ${y1} A ${radius} ${radius} 0 ${largeArc} 1 ${x2} ${y2} Z`
    );
    path.setAttribute('fill', d.color);
    path.setAttribute('data-label', d.label);
    path.setAttribute('data-value', d.value);

    path.addEventListener('click', () => {
      alert(`${d.label}: ${d.value}%`);
    });

    pie.appendChild(path);

    // 标签
    const midAngle = (startAngle + endAngle) / 2;
    const midRad = (midAngle * Math.PI) / 180;
    const labelX = radius * 0.6 * Math.cos(midRad);
    const labelY = radius * 0.6 * Math.sin(midRad);

    const label = document.createElementNS(svgNS, 'text');
    label.setAttribute('class', 'label');
    label.setAttribute('x', labelX);
    label.setAttribute('y', labelY);
    label.setAttribute('text-anchor', 'middle');
    label.setAttribute('dominant-baseline', 'middle');
    label.textContent = d.value + '%';
    pie.appendChild(label);

    cumAngle = endAngle;
  });
</script>
```

## 8. 总结

| 知识点           | 应用项目                   |
| ---------------- | -------------------------- |
| 坐标系与 viewBox | 所有项目                   |
| path 与弧线      | 饼图、环形进度             |
| 渐变与图案       | Logo、图表装饰             |
| 变换             | 节点定位、悬停缩放         |
| 滤镜             | 阴影、发光                 |
| 动画             | 进度条、加载动画、路径绘制 |
| CSS 样式化       | 主题色、悬停状态           |
| JavaScript       | 数据驱动、交互响应         |
| 可访问性         | title/desc、aria-label     |
| 性能             | 节点复用、批量插入         |

## 9. 扩展资源

- **MDN SVG 教程**：https://developer.mozilla.org/zh-CN/docs/Web/SVG/Tutorial
- **SVG 规范**：https://www.w3.org/TR/SVG2/
- **SVGO 优化工具**：https://github.com/svg/svgo
- **D3.js**：https://d3js.org/ - 数据驱动文档，基于 SVG
- **Snap.svg**：http://snapsvg.io/ - 现代 SVG 操作库
- **Figma**：可视化设计工具，支持 SVG 导出

至此，SVG 模块从基础到实战的完整教程结束。建议按顺序学习，并在每个章节后动手实践示例代码。
## 环形进度条语法

**stroke-dasharray 控制进度**
`<circle r="<半径>" stroke-dasharray="<周长>" stroke-dashoffset="<偏移>" transform="rotate(-90 <cx> <cy>)">`
```html
<svg viewBox="0 0 200 200" width="200" height="200">
  <defs>
    <linearGradient id="progress-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f5bd5" />
      <stop offset="100%" stop-color="#00b894" />
    </linearGradient>
  </defs>

  <!-- 背景圆 -->
  <circle cx="100" cy="100" r="80" fill="none" stroke="#e0e0e0" stroke-width="12" />

  <!-- 进度圆:rotate(-90) 让起点在 12 点钟方向 -->
  <circle
    id="progress-circle"
    cx="100"
    cy="100"
    r="80"
    fill="none"
    stroke="url(#progress-grad)"
    stroke-width="12"
    stroke-linecap="round"
    stroke-dasharray="502"
    stroke-dashoffset="502"
    transform="rotate(-90 100 100)"
  />

  <text x="100" y="100" text-anchor="middle" dominant-baseline="middle" font-size="36" font-weight="bold" fill="#333">0%</text>
</svg>

<script>
  const circle = document.getElementById('progress-circle');
  const circumference = 2 * Math.PI * 80; // 约 502

  function setProgress(percent) {
    const offset = circumference - (percent / 100) * circumference;
    circle.style.strokeDashoffset = offset;
  }
</script>
```

### 进度条相关属性表

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| `stroke-dasharray` | 虚线长度(设为周长) | `502` |
| `stroke-dashoffset` | 偏移量(控制进度) | `0~502` |
| `stroke-linecap` | 线段端点样式 | `round` |
| `transform` | 旋转起点到 12 点 | `rotate(-90 cx cy)` |

---

## 渐变描边语法

**url() 引用渐变**
`<element stroke="url(#<gradient-id>)">`
```html
<defs>
  <linearGradient id="bar-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#5b6ee8" />
    <stop offset="100%" stop-color="#4f5bd5" />
  </linearGradient>
</defs>

<rect x="10" y="20" width="80" height="200" fill="url(#bar-grad)" rx="4" />
```

---

## 阴影滤镜语法

**feDropShadow 投影**
`<filter id="<id>"><feDropShadow dx="..." dy="..." stdDeviation="..." flood-opacity="..." /></filter>`
```html
<defs>
  <filter id="bar-shadow">
    <feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.1" />
  </filter>
</defs>

<rect x="10" y="20" width="80" height="200" fill="#4f5bd5" filter="url(#bar-shadow)" />
```

---

## 图表轴线语法

**坐标轴绘制**
`<line x1="..." y1="..." x2="..." y2="..." stroke="..." />`
```html
<!-- Y 轴 -->
<line class="axis" x1="60" y1="40" x2="60" y2="320" stroke="#ccc" />
<!-- X 轴 -->
<line class="axis" x1="60" y1="320" x2="560" y2="320" stroke="#ccc" />

<!-- 网格线 -->
<g stroke="#f0f0f0" stroke-dasharray="4 4">
  <line x1="60" y1="80" x2="560" y2="80" />
  <line x1="60" y1="160" x2="560" y2="160" />
  <line x1="60" y1="240" x2="560" y2="240" />
</g>

<!-- Y 轴标签 -->
<g class="label" text-anchor="end" font-size="12" fill="#666">
  <text x="55" y="324">0</text>
  <text x="55" y="244">75</text>
  <text x="55" y="164">150</text>
</g>
```

---

## JS 动态创建 SVG 元素

**createElementNS 创建**
`document.createElementNS("<svg-ns>", "<tag>")`
```javascript
const svgNS = 'http://www.w3.org/2000/svg';
const bar = document.createElementNS(svgNS, 'rect');
bar.setAttribute('x', 100);
bar.setAttribute('y', 50);
bar.setAttribute('width', 80);
bar.setAttribute('height', 200);
bar.setAttribute('fill', 'url(#bar-grad)');
bar.setAttribute('rx', 4);
svg.appendChild(bar);
```

### 常用元素创建 API

| API | 用途 |
| --- | --- |
| `createElementNS(svgNS, 'rect')` | 创建矩形 |
| `createElementNS(svgNS, 'circle')` | 创建圆形 |
| `createElementNS(svgNS, 'line')` | 创建线段 |
| `createElementNS(svgNS, 'text')` | 创建文本 |
| `createElementNS(svgNS, 'path')` | 创建路径 |
| `createElementNS(svgNS, 'g')` | 创建分组 |
| `setAttribute(name, value)` | 设置属性 |
| `getAttribute(name)` | 读取属性 |
| `appendChild(el)` | 追加子元素 |

---

## requestAnimationFrame 动画

**JS 动画循环**
`requestAnimationFrame(<callback>)`
```javascript
const duration = 2000;
const target = 75;
const start = performance.now();
let current = 0;

function animate(now) {
  const elapsed = now - start;
  const t = Math.min(elapsed / duration, 1);
  // ease-out cubic 缓动
  const eased = 1 - Math.pow(1 - t, 3);
  current = Math.round(eased * target);
  setProgress(current);
  if (t < 1) requestAnimationFrame(animate);
}
requestAnimationFrame(animate);
```

---

## CSS transition 动画

**transition 延迟入场**
`<selector> { transition: all <dur> <easing>; transition-delay: <delay>; }`
```css
.bar {
  transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
  transition-delay: 0.1s;
}
.value {
  opacity: 0;
  transition: opacity 0.4s;
  transition-delay: 0.5s;
}
```

```javascript
// 触发动画
requestAnimationFrame(() => {
  bar.setAttribute('height', barHeight);
  value.style.opacity = '1';
});
```

---

## path 动画语法

**animate 动画 d 属性**
`<path d="..."><animate attributeName="d" values="..." dur="..." repeatCount="indefinite" /></path>`
```html
<path d="M 100 95 Q 200 105 300 95" fill="none" stroke="url(#logo-grad)" stroke-width="2" stroke-linecap="round">
  <animate
    attributeName="d"
    values="M 100 95 Q 200 105 300 95; M 100 95 Q 200 85 300 95; M 100 95 Q 200 105 300 95"
    dur="3s"
    repeatCount="indefinite"
  />
</path>
```

---

## stop-color 动画

**渐变色 stop 颜色变化**
`<stop offset="..." stop-color="..."><animate attributeName="stop-color" values="..." dur="..." repeatCount="indefinite" /></stop>`
```html
<defs>
  <linearGradient id="logo-grad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#4f5bd5">
      <animate
        attributeName="stop-color"
        values="#4f5bd5;#00b894;#4f5bd5"
        dur="6s"
        repeatCount="indefinite"
      />
    </stop>
    <stop offset="100%" stop-color="#00b894">
      <animate
        attributeName="stop-color"
        values="#00b894;#4f5bd5;#00b894"
        dur="6s"
        repeatCount="indefinite"
      />
    </stop>
  </linearGradient>
</defs>
```

---

## tspan 文本拆分动画

**tspan 逐字符动画**
`<text><tspan class="letter">F</tspan><tspan class="letter">A</tspan>...</text>`
```html
<style>
  .logo-text {
    font-family: 'Inter', sans-serif;
    font-size: 48px;
    font-weight: bold;
    fill: url(#logo-grad);
  }
  .logo-letter {
    transform-origin: center;
    transform-box: fill-box;
  }
  .logo-letter:nth-child(1) { animation: bounce 2s ease-in-out infinite; }
  .logo-letter:nth-child(2) { animation: bounce 2s ease-in-out infinite 0.1s; }
  .logo-letter:nth-child(3) { animation: bounce 2s ease-in-out infinite 0.2s; }
  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }
</style>

<text x="200" y="75" text-anchor="middle" class="logo-text">
  <tspan class="logo-letter">F</tspan>
  <tspan class="logo-letter">A</tspan>
  <tspan class="logo-letter">N</tspan>
  <tspan class="logo-letter">D</tspan>
  <tspan class="logo-letter">E</tspan>
  <tspan class="logo-letter">X</tspan>
</text>
```

### tspan 属性表

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| `x` | 绝对 x 坐标 | `100` |
| `y` | 绝对 y 坐标 | `75` |
| `dx` | 相对 x 偏移 | `5` |
| `dy` | 相对 y 偏移 | `0` |
| `rotate` | 旋转角度 | `0` |
| `textLength` | 文本长度 | `200` |

---

## radialGradient 节点语法

**径向渐变节点**
`<radialGradient id="..."><stop offset="..." stop-color="..." /></radialGradient>`
```html
<defs>
  <radialGradient id="node-grad">
    <stop offset="0%" stop-color="#4f5bd5" />
    <stop offset="100%" stop-color="#3a47b8" />
  </radialGradient>
</defs>

<circle cx="200" cy="200" r="8" fill="url(#node-grad)" />
```

---

## pattern 网格背景

**pattern 平铺图案**
`<pattern id="..." width="..." height="..." patternUnits="userSpaceOnUse">...</pattern>`
```html
<defs>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#f0f0f0" stroke-width="1" />
  </pattern>
</defs>

<rect width="800" height="600" fill="url(#grid)" />
```

### pattern 属性表

| 属性 | 说明 | 默认值 |
| --- | --- | --- |
| `width` | 单元格宽度 | - |
| `height` | 单元格高度 | - |
| `patternUnits` | 单位坐标系 | `objectBoundingBox` |
| `patternContentUnits` | 内容单位 | `userSpaceOnUse` |
| `patternTransform` | 变换 | `none` |
| `x` | x 偏移 | `0` |
| `y` | y 偏移 | `0` |

---

## 脉冲动画语法

**节点脉冲环**
`<circle class="pulse-ring" r="..."><animate attributeName="r" values="..." dur="..." repeatCount="indefinite" /></circle>`
```html
<g class="node-group" transform="translate(200, 200)">
  <!-- 脉冲环 -->
  <circle class="pulse-ring" r="15" fill="none" stroke="#4f5bd5" stroke-width="2">
    <animate attributeName="r" values="15;25;15" dur="2s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite" />
  </circle>
  <!-- 节点圆 -->
  <circle r="8" fill="url(#node-grad)" filter="url(#node-glow)" />
  <!-- 标签 -->
  <text y="-15" text-anchor="middle" font-size="12" fill="#333">北京</text>
</g>
```

---

## begin 延迟动画

**begin 延迟启动**
`<animate attributeName="..." values="..." dur="..." begin="<delay>" repeatCount="indefinite" />`
```html
<!-- 第二个节点延迟 0.5s 启动 -->
<animate attributeName="r" values="15;25;15" dur="2s" begin="0.5s" repeatCount="indefinite" />

<!-- 第三个节点延迟 1s 启动 -->
<animate attributeName="r" values="15;25;15" dur="2s" begin="1s" repeatCount="indefinite" />
```

### begin 事件触发表

| 触发方式 | 语法 | 说明 |
| --- | --- | --- |
| 时间 | `2s` | 2 秒后启动 |
| 点击 | `click` | 元素点击时启动 |
| 鼠标进入 | `mouseover` | 鼠标进入时启动 |
| 元素结束 | `elemId.end` | 指定动画结束时启动 |
| 元素开始 | `elemId.begin` | 指定动画开始时启动 |
| 事件+时间 | `click+2s` | 点击后延迟 2s 启动 |

---

## 连接线语法

**节点间连线**
`<line x1="..." y1="..." x2="..." y2="..." stroke="..." stroke-width="..." opacity="..." />`
```html
<g class="connections">
  <line x1="200" y1="200" x2="400" y2="300" stroke="#4f5bd5" stroke-width="1.5" opacity="0.4" />
  <line x1="400" y1="300" x2="600" y2="200" stroke="#4f5bd5" stroke-width="1.5" opacity="0.4" />
</g>
```

---

## hover 交互语法

**CSS hover 缩放**
`<selector>:hover { transform: scale(<factor>); }`
```css
.node {
  cursor: pointer;
  transition: transform 0.2s;
  transform-origin: center;
  transform-box: fill-box;
}
.node:hover {
  transform: scale(1.3);
}
```

```html
<circle class="node" r="8" fill="url(#node-grad)" />
```

---

## 折线图语法

**polyline 折线**
`<polyline points="<x1>,<y1> <x2>,<y2> ..." fill="none" stroke="..." stroke-width="..." />`
```html
<svg viewBox="0 0 600 400">
  <polyline
    points="50,300 100,250 150,280 200,200 250,220 300,150 350,180 400,120"
    fill="none"
    stroke="#4f5bd5"
    stroke-width="3"
    stroke-linecap="round"
    stroke-linejoin="round"
  />
</svg>
```

**path 折线**
`<path d="M <x1> <y1> L <x2> <y2> L <x3> <y3> ..." />`
```html
<path
  d="M 50 300 L 100 250 L 150 280 L 200 200 L 250 220 L 300 150"
  fill="none"
  stroke="#00b894"
  stroke-width="2"
/>
```

### polyline / path 折线属性表

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| `points` | 点坐标列表(polyline) | `50,300 100,250` |
| `d` | 路径数据(path) | `M 50 300 L 100 250` |
| `fill` | 填充(折线用 none) | `none` |
| `stroke` | 描边颜色 | `#4f5bd5` |
| `stroke-width` | 描边宽度 | `3` |

---

## 区域填充语法

**path 填充区域**
`<path d="M <start> L <points> L <end> Z" fill="url(#<grad>)" opacity="..." />`
```html
<defs>
  <linearGradient id="area-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#4f5bd5" stop-opacity="0.4" />
    <stop offset="100%" stop-color="#4f5bd5" stop-opacity="0" />
  </linearGradient>
</defs>

<!-- 折线下方填充区域 -->
<path
  d="M 50 300 L 100 250 L 150 280 L 200 200 L 250 220 L 300 150 L 300 350 L 50 350 Z"
  fill="url(#area-grad)"
/>
```

---

## 数据点语法

**数据点圆**
`<circle cx="<x>" cy="<y>" r="<radius>" fill="..." />`
```html
<g class="points">
  <circle cx="50" cy="300" r="4" fill="#4f5bd5" />
  <circle cx="100" cy="250" r="4" fill="#4f5bd5" />
  <circle cx="150" cy="280" r="4" fill="#4f5bd5" />
  <circle cx="200" cy="200" r="4" fill="#4f5bd5" />
</g>
```

---

## 饼图 path 语法

**A 弧线绘制扇形**
`<path d="M <cx> <cy> L <x1> <y1> A <r> <r> 0 <large-arc> 1 <x2> <y2> Z" fill="..." />`
```html
<svg viewBox="0 0 200 200">
  <!-- 扇形 1:0° → 90°(large-arc=0) -->
  <path
    d="M 100 100 L 100 0 A 100 100 0 0 1 200 100 Z"
    fill="#4f5bd5"
  />
  <!-- 扇形 2:90° → 180°(large-arc=0) -->
  <path
    d="M 100 100 L 200 100 A 100 100 0 0 1 100 200 Z"
    fill="#00b894"
  />
  <!-- 扇形 3:180° → 270° -->
  <path
    d="M 100 100 L 100 200 A 100 100 0 0 1 0 100 Z"
    fill="#f9a825"
  />
  <!-- 扇形 4:270° → 360° -->
  <path
    d="M 100 100 L 0 100 A 100 100 0 0 1 100 0 Z"
    fill="#d63031"
  />
</svg>
```

### A 弧线命令参数表

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| `rx` | x 轴半径 | `100` |
| `ry` | y 轴半径 | `100` |
| `x-axis-rotation` | x 轴旋转角度 | `0` |
| `large-arc-flag` | 大弧标志(0 小弧 / 1 大弧) | `0` |
| `sweep-flag` | 扫描方向(0 逆时针 / 1 顺时针) | `1` |
| `x` | 终点 x | `200` |
| `y` | 终点 y | `100` |

---

## 饼图圆环语法

**stroke-dasharray 绘制圆环段**
`<circle r="<r>" stroke="..." stroke-dasharray="<segment> <remaining>" stroke-dashoffset="<offset>" />`
```html
<svg viewBox="0 0 200 200">
  <!-- 圆环半径 80,周长 ≈ 502 -->
  <!-- 第一段 25%:dasharray=125.5 376.5,offset=0 -->
  <circle cx="100" cy="100" r="80" fill="none"
    stroke="#4f5bd5" stroke-width="30"
    stroke-dasharray="125.5 376.5"
    stroke-dashoffset="0"
    transform="rotate(-90 100 100)" />
  <!-- 第二段 25%:offset=-125.5 -->
  <circle cx="100" cy="100" r="80" fill="none"
    stroke="#00b894" stroke-width="30"
    stroke-dasharray="125.5 376.5"
    stroke-dashoffset="-125.5"
    transform="rotate(-90 100 100)" />
  <!-- 第三段 25%:offset=-251 -->
  <circle cx="100" cy="100" r="80" fill="none"
    stroke="#f9a825" stroke-width="30"
    stroke-dasharray="125.5 376.5"
    stroke-dashoffset="-251"
    transform="rotate(-90 100 100)" />
  <!-- 第四段 25%:offset=-376.5 -->
  <circle cx="100" cy="100" r="80" fill="none"
    stroke="#d63031" stroke-width="30"
    stroke-dasharray="125.5 376.5"
    stroke-dashoffset="-376.5"
    transform="rotate(-90 100 100)" />
</svg>
```

---

## 折线图入场动画

**stroke-dasharray 绘制动画**
`<polyline stroke-dasharray="<length>" stroke-dashoffset="<length>"><animate attributeName="stroke-dashoffset" from="..." to="0" dur="..." fill="freeze" /></polyline>`
```html
<polyline
  points="50,300 100,250 150,280 200,200 250,220 300,150"
  fill="none"
  stroke="#4f5bd5"
  stroke-width="3"
  stroke-dasharray="600"
  stroke-dashoffset="600"
>
  <animate
    attributeName="stroke-dashoffset"
    from="600"
    to="0"
    dur="2s"
    fill="freeze"
  />
</polyline>
```

---

## 柱状图入场动画

**rect 高度动画**
`<rect><animate attributeName="height" from="0" to="..." dur="..." fill="freeze" /><animate attributeName="y" from="..." to="..." dur="..." fill="freeze" /></rect>`
```html
<rect x="100" y="320" width="80" height="0" fill="url(#bar-grad)" rx="4">
  <animate attributeName="height" from="0" to="200" dur="0.8s" fill="freeze" />
  <animate attributeName="y" from="320" to="120" dur="0.8s" fill="freeze" />
</rect>
```

---

## transform 平移语法

**transform translate 平移**
`<g transform="translate(<x>, <y>)">...</g>`
```html
<g transform="translate(200, 200)">
  <circle r="8" fill="url(#node-grad)" />
  <text y="-15" text-anchor="middle">节点</text>
</g>

<g transform="translate(400, 300)">
  <circle r="8" fill="url(#node-grad)" />
  <text y="-15" text-anchor="middle">节点 2</text>
</g>
```

---

## rotate 旋转语法

**transform rotate 旋转**
`<element transform="rotate(<angle> [<cx> <cy>])">`
```html
<!-- 旋转进度条起点 -->
<circle
  cx="100" cy="100" r="80"
  transform="rotate(-90 100 100)"
  stroke-dasharray="502"
  stroke-dashoffset="502"
/>
```

---

## scale 缩放语法

**transform scale 缩放**
`<element transform="scale(<sx> [<sy>])">`
```html
<g transform="scale(1.5)">
  <circle cx="100" cy="100" r="50" fill="#4f5bd5" />
</g>
```

---

## 综合滤镜链语法

**feGaussianBlur + feMerge 发光**
`<filter id="..."><feGaussianBlur stdDeviation="..." result="b" /><feMerge><feMergeNode in="b" /><feMergeNode in="SourceGraphic" /></feMerge></filter>`
```html
<defs>
  <filter id="glow">
    <feGaussianBlur stdDeviation="3" result="b" />
    <feMerge>
      <feMergeNode in="b" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
</defs>

<circle cx="100" cy="100" r="50" fill="#4f5bd5" filter="url(#glow)" />
```

---

## 事件处理语法

**addEventListener 绑定**
`element.addEventListener('<event>', <callback>)`
```javascript
const bar = document.querySelector('.bar');
bar.addEventListener('click', (e) => {
  console.log('点击柱子');
});

bar.addEventListener('mouseenter', (e) => {
  bar.style.opacity = '0.8';
});

bar.addEventListener('mouseleave', (e) => {
  bar.style.opacity = '1';
});
```

### 常用事件表

| 事件 | 触发时机 |
| --- | --- |
| `click` | 点击 |
| `mouseenter` | 鼠标进入 |
| `mouseleave` | 鼠标离开 |
| `mouseover` | 鼠标移过 |
| `mouseout` | 鼠标移出 |
| `keydown` | 键盘按下 |
| `focus` | 获得焦点 |
| `blur` | 失去焦点 |

---

## DocumentFragment 批量插入

**批量插入优化**
`const fragment = document.createDocumentFragment(); ... svg.appendChild(fragment);`
```javascript
const svgNS = 'http://www.w3.org/2000/svg';
const fragment = document.createDocumentFragment();

for (let i = 0; i < 100; i++) {
  const circle = document.createElementNS(svgNS, 'circle');
  circle.setAttribute('cx', Math.random() * 400);
  circle.setAttribute('cy', Math.random() * 300);
  circle.setAttribute('r', 3);
  circle.setAttribute('fill', '#4f5bd5');
  fragment.appendChild(circle);
}

svg.appendChild(fragment); // 一次性插入,减少重排
```

---

## 数据驱动渲染

**数据 → SVG**
`data.forEach(d => { const el = createElementNS(...); el.setAttribute(...); svg.appendChild(el); })`
```javascript
const data = [
  { label: 'Q1', value: 120 },
  { label: 'Q2', value: 165 },
  { label: 'Q3', value: 210 },
  { label: 'Q4', value: 180 },
];

const svgNS = 'http://www.w3.org/2000/svg';
const maxValue = 250;
const chartHeight = 280;

data.forEach((d, i) => {
  const barHeight = (d.value / maxValue) * chartHeight;
  const bar = document.createElementNS(svgNS, 'rect');
  bar.setAttribute('x', 100 + i * 120);
  bar.setAttribute('y', 320 - barHeight);
  bar.setAttribute('width', 80);
  bar.setAttribute('height', barHeight);
  bar.setAttribute('fill', 'url(#bar-grad)');
  svg.appendChild(bar);
});
```

---

## 图例语法

**图例项**
`<g class="legend"><rect /><text>...</text></g>`
```html
<g class="legend" transform="translate(450, 50)">
  <rect x="0" y="0" width="12" height="12" fill="#4f5bd5" />
  <text x="20" y="10" font-size="12" fill="#333">销售额</text>

  <rect x="0" y="20" width="12" height="12" fill="#00b894" />
  <text x="20" y="30" font-size="12" fill="#333">利润</text>

  <rect x="0" y="40" width="12" height="12" fill="#f9a825" />
  <text x="20" y="50" font-size="12" fill="#333">成本</text>
</g>
```

---

## 标题与描述语法

**图表 title 与 desc**
`<svg><title>...</title><desc>...</desc>...</svg>`
```html
<svg viewBox="0 0 600 400" role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">2024 季度销售额</title>
  <desc id="chart-desc">柱状图展示 Q1 至 Q4 销售额,单位:万元</desc>
  <!-- 图表内容 -->
</svg>
```

---

## path 命令综合参考

**M/L/H/V 直线**
`<path d="M <x> <y> L <x> <y> H <x> V <y>" />`
```html
<path d="M 10 10 L 50 10 H 90 V 50 L 50 50 Z" fill="none" stroke="#333" />
```

**C/S/Q/T/Bézier 曲线**
`<path d="M <x> <y> C <cx1> <cy1> <cx2> <cy2> <x> <y> S <cx2> <cy2> <x> <y> Q <cx> <cy> <x> <y> T <x> <y>" />`
```html
<!-- 三次贝塞尔 -->
<path d="M 10 50 C 30 10, 70 10, 90 50" fill="none" stroke="#333" />
<!-- 二次贝塞尔 -->
<path d="M 10 50 Q 50 10, 90 50" fill="none" stroke="#333" />
```

**A 弧线**
`<path d="M <x1> <y1> A <rx> <ry> <rotation> <large-arc> <sweep> <x2> <y2>" />`
```html
<path d="M 10 50 A 40 40 0 0 1 90 50" fill="none" stroke="#333" />
```

### path 命令总表

| 命令 | 含义 | 参数 |
| --- | --- | --- |
| `M` | 移动到(绝对) | `x y` |
| `m` | 移动到(相对) | `x y` |
| `L` | 直线到(绝对) | `x y` |
| `l` | 直线到(相对) | `x y` |
| `H` | 水平线到 | `x` |
| `V` | 垂直线到 | `y` |
| `C` | 三次贝塞尔 | `cx1 cy1 cx2 cy2 x y` |
| `S` | 平滑三次贝塞尔 | `cx2 cy2 x y` |
| `Q` | 二次贝塞尔 | `cx cy x y` |
| `T` | 平滑二次贝塞尔 | `x y` |
| `A` | 弧线 | `rx ry rot large-arc sweep x y` |
| `Z` / `z` | 闭合路径 | (无参数) |
