---
order: 10
title: css 模块文档合集
module: 'css'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：007-css/001-CSS3OverviewBasicSyntax.md ============ -->

## 0.3 CSS 核心语法扩展：选择器、声明与层叠

### 一条规则由三部分组成

```css
.card {
  color: #1f2937;
  padding: 16px;
}
```

| 部分 | 示例 | 含义 | 排错方法 |
| --- | --- | --- | --- |
| 选择器 | `.card` | 找到要应用样式的元素 | 在 DevTools Elements 中确认元素是否真的有该类名 |
| 属性 | `padding` | 说明要改变哪类视觉特征 | 拼写错误时浏览器会忽略该声明 |
| 值 | `16px` | 属性的具体取值 | 值不合法时该行不会生效 |

### 初学者最常用的属性

| 类别 | 属性 | 典型值 | 适用场景 |
| --- | --- | --- | --- |
| 文本 | `color`、`font-size`、`line-height` | `#111827`、`16px`、`1.7` | 控制阅读体验 |
| 盒模型 | `width`、`padding`、`border`、`margin` | `320px`、`1rem`、`1px solid` | 控制尺寸与间距 |
| 布局 | `display`、`gap`、`align-items` | `flex`、`grid`、`12px` | 控制元素排列 |
| 背景 | `background`、`background-size` | `#fff`、`cover` | 做卡片、横幅和状态块 |
| 交互 | `cursor`、`transition`、`:hover` | `pointer`、`150ms ease` | 提升按钮和链接反馈 |

### 层叠判断顺序

1. 先看来源：浏览器默认样式、作者样式、用户样式。
2. 再看重要性：普通声明与 `!important` 声明分开比较。
3. 再看优先级：内联样式高于 id，id 高于 class，class 高于元素选择器。
4. 最后看出现顺序：优先级相同，后写的覆盖先写的。


## 0. 快速上手：2 分钟写出第一行 CSS

> 目标：不管懂不懂 CSS，先让浏览器里的字变色。

### 0.0 学前准备（30 秒）

开始前确认三样东西已就位：

1. **浏览器**：Chrome 或 Edge（本模块的调试演示均基于 Chrome DevTools）；
2. **编辑器**：VS Code（或任意纯文本编辑器，记事本也可以）；
3. **HTML 基础**：能写一个含 `<h1>` 与 `<p>` 标签的 `index.html`（HTML 入门见 `html5/006-HTML5OverviewCoreFeature`）。

不需要装任何额外软件，CSS 由浏览器直接解析，本模块所有示例都可用“一个 HTML 文件 + 一个 CSS 文件”复现。

### 0.1 准备（30 秒）

打开你 HTML 第一课写的 `index.html`，在 `<head>` 里插入一行（没有就新建一个 `index.html`）：

```html
<link rel="stylesheet" href="style.css" />
```

### 0.2 写 CSS（30 秒）

在 `index.html` 旁边新建一个文本文档，重命名为 `style.css`（确保后缀是 `.css`），敲入：

```css
h1 {
  color: red;
}
```

### 0.3 看效果（30 秒）

保存两个文件，刷新浏览器——标题变红了！

你已经完成了第一行 CSS。记住这种感觉：`选择器 { 属性: 值; }`，后面全是这个格式的展开。

### 0.4 动手试试（1 分钟）

- 把 `red` 改成 `blue`，保存刷新，看颜色变化；
- 再写一行 `p { font-size: 20px; }`，看段落文字是否变大。

> 阅读指南：
>
> - 核心必学（第 0-5 节）：第一遍逐字精读，每个“动手试试”都做；
> - 进阶选修（第 6-8 节）：扫一眼标题，知道“有这个东西”即可，不必现在死磕；
> - 参考手册（第 9-14 节）：随用随查。

### 0.5 学完本章后你能做什么

学完本章（第 0-5 节）后，你应该能：

- 说出 CSS 的三个组成部分：选择器、属性、值；
- 用外部样式表让页面的标题与段落改变颜色和字号；
- 区分行内、内部、外部、@import 四种引入方式并说出各自适用场景；
- 解释“后写的规则为什么能覆盖先写的规则”；
- 说出 `px`/`em`/`rem` 的大致区别；
- 按“三步急救法”排查样式不生效的常见原因。

如果以上任一项答不上来，建议回头重读对应小节；都能回答，就可以进入 `css/003-CSS3BoxModelDetailed`。



> 本节为增量补充，帮助零基础者理解"CSS 没有 4.0/5.0 版本号"的原因。

- CSS 不再整体发布版本，而是按模块演进，W3C 每年发布一次 CSS Snapshot 汇总当前基线。
- 2026 年现代 CSS 基线已包含：Flexbox、Grid、容器查询、:has()、层叠层 @layer、颜色函数（oklch/color-mix）、原生嵌套、逻辑属性、滚动捕捉等。
- 判断某个新特性能否在目标浏览器使用：优先查 MDN 的 Baseline 标记或 caniuse，而不是看"CSS 版本"。

## 1. CSS 是什么（极简版）

> 一句话概括：CSS 就是给 HTML 标签“穿衣服”的规则清单。

- 选择器：告诉浏览器“我要打扮谁”（如 `h1`、`.card`）；
- 属性：告诉浏览器“我要改哪里”（如 `color`、`font-size`）；
- 值：告诉浏览器“改成什么样”（如 `red`、`20px`）。

CSS3 能做什么（挑 3 个记住就够了）：

| 能力 | 对应属性 | 你在第 0 节刚用过 |
| --- | --- | --- |
| 改颜色 | `color` / `background-color` | `color: red` |
| 改大小 | `font-size` / `width` / `height` | `font-size: 20px` |
| 改位置 | `margin` / `padding` / `display: flex` | 后续课程 |

至于 CSS 历史（1996/1998……）和全部特性清单，请移步文末扩展学习，第一遍学习不需要背。
## 2. 基本语法

### 2.1 语法结构

CSS 的基本语法由选择器、属性和值组成：

```css
/* 选择器 { 属性: 值; } */
h1 {
  color: blue;
  font-size: 24px; /* 声明以分号结束 */
}
/* 多个选择器共享同一组样式 */
h1,
h2,
h3 {
  font-family: Arial, sans-serif;
}
/* 嵌套选择器 */
.container {
  width: 100%;
  .header {
    height: 100px;
  }
  .content {
    padding: 20px;
  }
}
```

**讲解：**

- 每条规则由“选择器 + 声明块”组成，声明块里是“属性: 值;”；
- 分号是声明的结束符，漏掉分号会让下一条声明失效；
- 多个选择器用逗号分隔共享样式；原生 CSS 已支持嵌套，但入门阶段先掌握平铺写法。

动手试试（2 分钟）：

1. 打开你的 `style.css`，把 `h1` 颜色改成 `green`，加一条 `font-size: 32px`（注意分号）；
2. 故意漏掉分号（`color: green` 后面不写 `;`），保存刷新，观察第二条样式是否生效；
3. 把分号补上，再次刷新，确认恢复。

提示：这个练习能帮你记住——分号是声明之间的分隔符，漏掉会让后面的声明失效。

### 2.2 注释

CSS 中的注释使用 `/* */` 语法：

```css
/* 这是一个单行注释 */
/*
 这是一个
 多行注释
 */
/* 注释可以放在任何位置 */
h1 {
  color: blue; /* 颜色设置 */
  font-size: 24px; /* 字体大小设置 */
}
```

**讲解：** CSS 注释用 `/* */` 包裹，可单行可多行；注释不会影响渲染，适合标记分区与解释特殊逻辑。

动手试试（1 分钟）：在 `style.css` 顶部加一行注释 `/* 我的第一个样式表 */`，保存刷新，确认页面不受影响。

### 2.3 空白与格式化

CSS 忽略多余的空白，因此可以使用空白来提高代码可读性：

```css
/* 良好的格式化 */
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
/* 压缩格式（用于生产环境） */
body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
```

### 2.4 大小写敏感性

CSS 对选择器和属性名不区分大小写，但对属性值区分大小写（特别是字体名称和URL）：

```css
/* 以下两种写法效果相同 */
H1 {
  color: BLUE;
}
h1 {
  color: blue;
}
/* 但以下写法效果不同 */
.font {
  font-family: 'Times New Roman', serif; /* 正确 */
  font-family: 'times new roman', serif; /* 可能不生效 */
}
```

**讲解：** 选择器与属性名不区分大小写，但属性值（尤其字体名、URL、`id` 引用）区分大小写。统一小写是团队规范，避免隐患。

动手试试（1 分钟）：把 `h1` 改成 `H1` 并保存，刷新确认样式仍然生效；再把颜色值改成 `RED`，确认同样生效。

## 3. 引入方式

### 3.1 行内样式 (Inline)

直接在 HTML 元素的 `style` 属性中定义样式：

```html
<div style="color: red; font-size: 18px;">行内样式示例</div>
```

**讲解：** 行内样式直接写在 `style` 属性里，优先级最高，但样式与结构耦合、无法复用，只适合临时调试或动态注入。

**优点**：

- 优先级最高，可覆盖其他样式
- 适用于单个元素的特殊样式
  **缺点**：
- 难以维护，样式与结构混合
- 不能重用
- 增加 HTML 文件大小

### 3.2 内部样式 (Internal)

在 HTML 文档的 `<head>` 标签中使用 `<style>` 标签定义样式：

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
      }
      h1 {
        color: blue;
      }
    </style>
  </head>
  <body>
    <h1>内部样式示例</h1>
  </body>
</html>
```

**讲解：** 内部样式把 CSS 写在 `<head>` 的 `<style>` 里，适合单页小项目；多页面共用的样式应抽取为外部文件。

**优点**：

- 样式与结构分离
- 适用于单个页面的样式
- 无需额外的 HTTP 请求
  **缺点**：
- 样式不能在多个页面间重用
- 增加 HTML 文件大小

### 3.3 外部样式 (External)

在单独的 CSS 文件中定义样式，然后通过 `<link>` 标签引入：
**style.css**：

```css
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
}
h1 {
  color: blue;
}
```

**HTML**：

```html
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>外部样式示例</h1>
  </body>
</html>
```

**讲解：** 外部样式通过 `<link rel="stylesheet">` 引入，可被多个页面复用、可缓存、便于维护，是生产环境的标准方式。

动手试试（2 分钟）：用外部样式给 `h1` 设置 `color: blue`，给 `body` 设置 `line-height: 1.6`，保存刷新验证。

**优点**：

- 样式与结构完全分离
- 样式可以在多个页面间重用
- 浏览器可以缓存 CSS 文件，提高加载速度
- 便于维护和管理
  **缺点**：
- 需要额外的 HTTP 请求

### 3.4 导入式 (@import)

在 CSS 文件中使用 `@import` 规则引入其他 CSS 文件：
**main.css**：

```css
@import url('reset.css');
@import url('layout.css');
body {
  font-family: Arial, sans-serif;
}
```

**讲解：** `@import` 在 CSS 内部引入其它样式表，会串行加载、阻塞渲染，性能不如 `<link>`；现代项目已基本不用。

**优点**：

- 可以将样式模块化，便于管理
  **缺点**：
- 会增加 HTTP 请求
- 可能导致页面加载延迟（因为 @import 是在 CSS 解析时才加载）
- 不建议在生产环境中使用

### 3.5 引入方式对比

| 引入方式 | 优先级 | 优点                         | 缺点               | 适用场景             |
| -------- | ------ | ---------------------------- | ------------------ | -------------------- |
| 行内样式 | 最高   | 优先级高，适用于特殊样式     | 难以维护，不能重用 | 单个元素的特殊样式   |
| 内部样式 | 中     | 样式与结构分离，无需额外请求 | 不能跨页面重用     | 单个页面的样式       |
| 外部样式 | 中     | 完全分离，可重用，可缓存     | 需要额外请求       | 多个页面的共用样式   |
| 导入式   | 中     | 样式模块化                   | 增加请求，可能延迟 | 开发环境中的样式组织 |

### 3.6 样式没生效？三步急救

如果刷新浏览器后样式毫无变化，按顺序检查这 3 件事：

1. 保存了吗？按 `Ctrl+S` 保存 `style.css` 和 `index.html`（很多人只保存了一个）；
2. 路径对吗？`<link rel="stylesheet" href="style.css">` 中的文件必须与 `index.html` 在同一文件夹；在子文件夹则写 `href="css/style.css"`；
3. 控制台有报错吗？按 F12 打开开发者工具，点 Console（控制台），红色报错会告诉你哪里出了问题。

提示：90% 的新手问题都出在上面三条，每次卡住先过一遍。

## 4. 优先级规则

CSS 遵循“就近原则”和“权重计算”来确定样式的优先级。

### 4.1 权重计算

CSS 选择器的权重由四部分组成，按从高到低的顺序计算：

1. **!important**：最高优先级，覆盖所有其他规则
2. **行内样式**：权重为 1000
3. **ID 选择器**：权重为 100
4. **类选择器、伪类选择器、属性选择器**：权重为 10
5. **元素选择器、伪元素选择器**：权重为 1
6. **通配符选择器 (\*)、后代选择器 (空格)、相邻兄弟选择器 (+)**：权重为 0

### 4.2 优先级顺序

1. **!important** 声明
2. 行内样式
3. ID 选择器
4. 类选择器、伪类选择器、属性选择器
5. 元素选择器、伪元素选择器
6. 继承的样式
7. 浏览器默认样式

### 4.3 优先级计算示例

```css
/* 权重：1 (元素选择器) */
div {
  color: blue;
}
/* 权重：10 (类选择器) */
.container {
  color: red;
}
/* 权重：100 (ID 选择器) */
#main {
  color: green;
}
/* 权重：101 (ID 选择器 + 元素选择器) */
#main div {
  color: purple;
}
/* 权重：20 (两个类选择器) */
.container .box {
  color: orange;
}
/* 行内样式：权重 1000 */
/* <div style="color: black;"> */
/* !important：最高优先级 */
div {
  color: yellow !important;
}
```

**讲解：**

- 权重从低到高：元素选择器(1) < 类选择器(10) < ID 选择器(100)，行内样式 1000，`!important` 最高；
- 权重相同按“就近原则”，后写的覆盖先写的；
- `!important` 会破坏层叠，应尽量避免，调试时优先查权重而不是加 `!important`。

动手试试（2 分钟）：给同一个 `h1` 分别写 `div h1 { color: blue }` 和 `.title { color: red }`，用开发者工具查看哪个生效，再把 `.title` 改成 `#main .title` 观察变化。

### 4.4 特殊情况

- **继承的样式**：继承的样式优先级最低，即使是低权重的选择器也能覆盖继承的样式。
- **就近原则**：当权重相同时，后定义的样式会覆盖先定义的样式。
- **!important 的使用**：应尽量避免使用 `!important`，因为它会破坏样式的层叠性，使调试变得困难。

## 5. CSS 单位

### 5.1 绝对单位

绝对单位是固定的，不会随其他因素变化：

- **px** (像素)：最常用的单位，适合固定尺寸的元素。
- **pt** (点)：主要用于印刷，1pt = 1/72 英寸。
- **pc** (派卡)：1pc = 12pt。
- **in** (英寸)：1in = 2.54cm。
- **cm** (厘米)：实际长度单位。
- **mm** (毫米)：实际长度单位。

### 5.2 相对单位

相对单位是相对于其他值计算的：

- **em**：相对于当前元素的字体大小。如果当前元素没有设置字体大小，则继承父元素的字体大小。
- **rem**：相对于根元素 (`<html>`) 的字体大小，推荐使用。
- **vw/vh**：相对于视口宽度/高度的 1%。
- **vmin/vmax**：相对于视口宽度和高度中较小/较大值的 1%。
- **%**：相对于父元素的相应属性值。
- **ch**：相对于数字 "0" 的宽度。
- **ex**：相对于字母 "x" 的高度。

### 5.3 单位使用场景

| 单位      | 适用场景                                   | 示例                         |
| --------- | ------------------------------------------ | ---------------------------- |
| px        | 固定尺寸的元素，如边框、按钮大小           | `border: 1px solid #ccc;`    |
| em        | 相对于当前元素字体大小的间距和尺寸         | `padding: 0.5em;`            |
| rem       | 响应式字体大小，便于整体调整               | `font-size: 1.2rem;`         |
| vw/vh     | 响应式布局，相对于视口大小                 | `width: 50vw; height: 50vh;` |
| %         | 相对于父元素的尺寸，如宽度、高度           | `width: 100%;`               |
| vmin/vmax | 响应式设计，确保元素在不同屏幕比例下的显示 | `font-size: 5vmin;`          |

## 6. [进阶选修] CSS 变量

第一遍学习可以先跳过本节，知道“CSS 变量 = 可复用的命名值”即可，后续主题课程会展开。

CSS 变量（也称为自定义属性）允许你定义可重用的值，提高代码的可维护性。

### 6.1 变量定义与使用

使用 `--` 前缀定义变量，使用 `var()` 函数使用变量：

```css
 /* 定义变量 */
 :root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --font-size: 16px;
  --spacing: 1rem;
 }
 /* 使用变量 */
 body {
  font-size: var(--font-size);
  color: var(--primary-color);
 }
 .button {
  background-color: var(--primary-color);
  padding: var(--spacing);
 }
 .button:hover {
  background-color: var(--secondary-color);
 }
```

**讲解：**

- 用 `--` 前缀定义变量，用 `var(变量名)` 引用；
- 变量写在 `:root` 中即全局可用，一处修改、全局生效；
- 变量是运行时特性，可以被媒体查询与 JavaScript 动态覆盖（详见 `css/035-CSSVariableCustomAttribute`）。

动手试试（2 分钟）：在 `:root` 中定义 `--main-color: #3498db` 与 `--spacing: 1rem`，在按钮样式中使用它们；改一处变量值，观察全局变化。

### 6.2 变量作用域

- **全局作用域**：在 `:root` 选择器中定义的变量，可在整个文档中使用。
- **局部作用域**：在特定选择器中定义的变量，只在该选择器及其后代中使用。

```css
 /* 全局变量 */
 :root {
  --color: blue;
 }
 /* 局部变量 */
 .container {
  --color: red;
  color: var(--color); /* 红色 */
 }
 .box {
  color: var(--color); /* 继承容器的红色 */
 }
 .footer {
  color: var(--color); /* 全局的蓝色 */
 }
```

**讲解：** 变量遵循“继承 + 就近覆盖”：元素会继承父级的变量，自己或更近的祖先定义了同名变量就覆盖。`.footer` 不在 `.container` 内，所以取全局蓝色。

### 6.3 变量使用示例

```css
 /* 主题变量 */
 :root {
  /* 浅色主题 */
  --bg-color: #ffffff;
  --text-color: #333333;
  --primary-color: #3498db;
  /* 间距 */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  /* 圆角 */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 12px;
  /* 阴影 */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 8px 16px rgba(0, 0, 0, 0.1);
 }
 /* 深色主题 */
 @media (prefers-color-scheme: dark) {
  :root {
  --bg-color: #121212;
  --text-color: #e0e0e0;
  --primary-color: #64b5f6;
  }
 }
 /* 使用变量 */
 body {
  background-color: var(--bg-color);
  color: var(--text-color);
  margin: 0;
  padding: var(--spacing-md);
  font-family: Arial, sans-serif;
 }
 .card {
  background-color: var(--bg-color);
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-md);
  padding: var(--spacing-md);
  margin-bottom: var(--spacing-md);
 }
 .button {
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: var(--border-radius-sm);
  padding: var(--spacing-sm) var(--spacing-md);
  cursor: pointer;
  transition: background-color 0.3s ease;
 }
 .button:hover {
  background-color: darken(var(--primary-color), 10%);
 }
```

**讲解：**

- 这个示例是“设计令牌”的经典写法：颜色、间距、圆角、阴影分四类变量，主题切换只改颜色变量；
- 深色模式用 `@media (prefers-color-scheme: dark)` 覆盖同一组变量，结构变量保持不变；
- 注意：`darken()` 是 Sass/Less 的语法，**原生 CSS 不支持**，悬停不会变暗。修正方案：`filter: brightness(0.9)`、`color-mix(in srgb, var(--primary-color), black 10%)`，或预定义 `--primary-color-dark` 变量；
- 卡片背景与页面背景相同会缺乏层次感，建议为卡片单独定义 `--card-bg`。

## 7. [进阶选修] CSS 函数

CSS 提供了多种函数，用于计算值、处理颜色等。

### 7.1 颜色函数

- **rgb()/rgba()**：使用红、绿、蓝和透明度值定义颜色。
- **hsl()/hsla()**：使用色相、饱和度、亮度和透明度值定义颜色。
- **color()**：使用指定颜色空间的颜色。
- **darken()/lighten()**：使颜色变暗或变亮。
- **saturate()/desaturate()**：增加或减少颜色的饱和度。
- **opacity()**：设置颜色的透明度。

```css
/* rgb() 示例 */
.color1 {
  color: rgb(255, 0, 0); /* 红色 */
}
/* rgba() 示例 */
.color2 {
  color: rgba(255, 0, 0, 0.5); /* 半透明红色 */
}
/* hsl() 示例 */
.color3 {
  color: hsl(120, 100%, 50%); /* 绿色 */
}
/* hsla() 示例 */
.color4 {
  color: hsla(120, 100%, 50%, 0.5); /* 半透明绿色 */
}
```

### 7.2 数学函数

- **calc()**：执行计算，可混合不同单位。
- **clamp()**：将值限制在一个范围内。
- **min()**：返回多个值中的最小值。
- **max()**：返回多个值中的最大值。

```css
/* calc() 示例 */
.container {
  width: calc(100% - 20px); /* 宽度为父元素宽度减去 20px */
  height: calc(100vh - 100px); /* 高度为视口高度减去 100px */
  font-size: calc(16px + 0.5vw); /* 字体大小随视口宽度变化 */
}
/* clamp() 示例 */
.text {
  font-size: clamp(16px, 2vw, 24px); /* 字体大小在 16px 到 24px 之间，随视口宽度变化 */
}
/* min() 示例 */
.box {
  width: min(500px, 100%); /* 宽度为 500px 和 100% 中的较小值 */
}
/* max() 示例 */
.header {
  height: max(100px, 10vh); /* 高度为 100px 和 10vh 中的较大值 */
}
```

### 7.3 其他常用函数

- **url()**：引用资源的 URL。
- **linear-gradient()/radial-gradient()**：创建线性或径向渐变。
- **repeat()**：重复值，用于 Grid 布局。
- **var()**：使用 CSS 变量。
- **attr()**：获取元素的属性值。

```css
/* url() 示例 */
.background {
  background-image: url('image.jpg');
}
/* linear-gradient() 示例 */
.gradient {
  background: linear-gradient(to right, red, blue);
}
/* radial-gradient() 示例 */
.radial-gradient {
  background: radial-gradient(circle, red, blue);
}
/* repeat() 示例 */
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 创建 3 个等宽列 */
}
/* attr() 示例 */
[data-tooltip]::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #333;
  color: white;
  padding: 5px;
  border-radius: 4px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.3s;
}
[data-tooltip]:hover::after {
  opacity: 1;
}
```

## 8. [进阶选修] 浏览器兼容性

### 8.1 浏览器前缀

为了支持不同浏览器的实验性特性，需要使用浏览器前缀：

```css
/* 带浏览器前缀的 CSS */
.box {
  /* Chrome, Safari, Opera */
  -webkit-border-radius: 8px;
  /* Firefox */
  -moz-border-radius: 8px;
  /* 标准语法 */
  border-radius: 8px;
  /* Chrome, Safari, Opera */
  -webkit-box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Firefox */
  -moz-box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* 标准语法 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Chrome, Safari, Opera */
  -webkit-transition: all 0.3s ease;
  /* Firefox */
  -moz-transition: all 0.3s ease;
  /* 标准语法 */
  transition: all 0.3s ease;
}
```

### 8.2 兼容性检测

使用 `@supports` 规则检测浏览器是否支持特定特性：

```css
/* 检测是否支持 Grid 布局 */
@supports (display: grid) {
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}
/* 检测是否支持 Flexbox */
@supports (display: flex) {
  .flex {
    display: flex;
    justify-content: center;
    align-items: center;
  }
}
/* 降级方案 */
.grid {
  /* 传统布局作为降级方案 */
  display: block;
}
@supports (display: grid) {
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### 8.3 兼容性最佳实践

- **使用 Autoprefixer**：自动添加浏览器前缀。
- **渐进增强**：先实现基本功能，再添加高级特性。
- **优雅降级**：为不支持高级特性的浏览器提供替代方案。
- **使用 CSS Reset 或 Normalize.css**：统一不同浏览器的默认样式。
- **测试**：在不同浏览器中测试你的样式。

## 9. 最佳实践

### 9.1 代码组织

- **使用模块化 CSS**：将样式按功能或组件分类。
- **使用命名约定**：如 BEM (Block, Element, Modifier) 命名规范。
- **使用注释**：为复杂样式添加注释。
- **保持代码整洁**：使用一致的缩进和格式。

### 9.2 性能优化

- **减少 CSS 文件大小**：使用压缩工具。
- **减少选择器复杂度**：使用简单的选择器。
- **避免使用 @import**：使用 `<link>` 标签代替。
- **使用 CSS 变量**：减少重复代码。
- **避免过度使用 !important**：保持样式的层叠性。

### 9.3 可维护性

- **使用语义化的类名**：类名应反映元素的用途。
- **避免内联样式**：使用外部或内部样式。
- **使用 CSS 预处理器**：如 Sass、Less 等，提供变量、嵌套、混合等功能。
- **定期清理**：移除未使用的样式。
- **文档化**：为样式添加文档说明。

## 10. 总结

CSS3 是现代网页设计的重要组成部分，提供了丰富的特性和功能：

- **核心特性**：响应式设计、现代布局、视觉效果、交互动画等。
- **语法结构**：选择器、属性、值的基本结构，以及注释、空白等语法规则。
- **引入方式**：行内样式、内部样式、外部样式、导入式，各有优缺点。
- **优先级规则**：基于权重计算和就近原则，决定样式的应用顺序。
- **CSS 单位**：绝对单位和相对单位，适用于不同的场景。
- **CSS 变量**：可重用的值，提高代码的可维护性。
- **CSS 函数**：用于计算值、处理颜色等。
- **浏览器兼容性**：使用浏览器前缀和特性检测，确保在不同浏览器中的一致性。
- **最佳实践**：代码组织、性能优化、可维护性等方面的建议。
  通过掌握 CSS3 的这些特性和最佳实践，开发者可以创建美观、响应式、高性能的网页设计。

## 11. 本章综合挑战（选做）

学完本章后，把前面每个“动手试试”串起来：

1. 给 HTML 第一课的博客页面加一个外部样式表，用 CSS 变量定义主色、间距与卡片背景；
2. 用 `.card` 类做一张带圆角与阴影的卡片（背景色用 `--card-bg`，不要与页面背景相同）；
3. 用 `@media (prefers-color-scheme: dark)` 做深色主题，只覆盖颜色变量；
4. 用 `color-mix()` 或 `filter: brightness()` 实现按钮悬停变暗（不要用 `darken()`）；
5. 用开发者工具验证优先级与盒模型，确保“三步急救”能解决你遇到的问题。

## 12. 核心知识点

> 一句话记住 CSS：选择器选中元素，`属性: 值` 改样式；外部 `<link>` 最常用，权重高者胜，后写覆盖先写。

- CSS 规则 = 选择器 + 声明块，声明以分号结尾；
- 三种主流引入方式：行内（最高优先级，不推荐）、内部（单页）、外部（生产标准）；
- 优先级：`!important` > 行内 > ID > 类 > 元素；权重相同就近原则；
- CSS 变量 `--name` + `var()` 实现设计令牌与主题切换；
- 相对单位（`rem`/`%`/`vw`）优于绝对单位（`px` 用于细节）；
- `@import` 阻塞渲染，用 `<link>` 代替。

## 13. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 滥用行内样式 | 无法复用、难以维护 | 抽取到类与外部样式表 |
| 依赖 `!important` | 破坏层叠，调试困难 | 检查权重与选择器结构 |
| 使用 `darken()` | 原生 CSS 不支持 | 用 `color-mix()`/`filter`/预定义变量 |
| 变量名无语义 | 维护者看不懂 | `--color-primary`/`--spacing-md` 等语义命名 |
| 大量 `@import` | 串行阻塞渲染 | 用 `<link>` 合并加载 |
| 不设卡片背景 | 与页面同色缺乏层次 | 单独定义 `--card-bg` 并适配深色 |

## 14. 扩展学习

- CSS 历史：CSS1（1996）→ CSS2（1998）→ CSS2.1（2011）→ CSS3 模块化（2012 起），了解即可；
- 选择器：`css/007-CSS3SelectorSystem` 系统掌握选择器；
- 盒模型：`css/003-CSS3BoxModelDetailed` 理解尺寸计算；
- 变量深入：`css/035-CSSVariableCustomAttribute` 作用域与动态主题；
- 响应式：`css/033-ResponsiveDesign` 与 `css/031-MediaQuery`；
- 工程化：`css/043-CSSArchitectureMethodology` 与 BEM 命名。

<!-- ============ 文档分隔线：007-css/002-CSSHowItWorks.md ============ -->

## 0. 直觉：浏览器把“HTML + CSS”变成屏幕上的画面

你写的是两个文件：`index.html` 描述“页面上有什么”，`style.css` 描述“这些东西长什么样”。浏览器拿到它们之后，不是直接画，而是先做四件事：

1. 把 HTML 读成一颗节点树（DOM）；
2. 把 CSS 读成一颗样式树（CSSOM）；
3. 把两棵树合并成“渲染树”（Render Tree），只留下真正要画的内容；
4. 计算位置（布局）并绘制到屏幕（绘制）。

本课只讲这条流程的“入门版”，让你知道样式为什么会生效、为什么不生效、以及为什么 `link` 要写在 `<head>` 里。深入版本见 `css/060-CriticalRenderPathOptimization`。

## 1. 第一步：HTML 变成 DOM

浏览器从上到下读取 HTML 文件，每遇到一个标签就生成一个节点，标签的嵌套关系形成“父子关系”，最终得到一颗文档对象模型树（DOM Tree）。

```html
<body>
  <h1>标题</h1>
  <p class="intro">正文</p>
</body>
```

对应的 DOM 结构：

```mermaid
flowchart TD
    A["html"]
    A --> B["body"]
    B --> C["h1：标题"]
    B --> D["p.intro：正文"]
```

**讲解：** DOM 是“页面的结构骨架”，CSS 选择器就是在这颗树上找节点。`p` 能找到那个 `<p>`，`.intro` 能找到带 `intro` 类的元素——选择器匹配的本质是“在 DOM 树上做查询”。

## 2. 第二步：CSS 变成 CSSOM

浏览器遇到 `<link rel="stylesheet">` 或 `<style>` 标签后，会下载并解析 CSS。解析结果是另一颗树：CSSOM（CSS Object Model）。它记录每条规则的选择器、声明以及它们之间的层叠关系。

```css
h1 {
  color: red;
}
.intro {
  color: blue;
}
```

**讲解：** CSSOM 不是简单地把规则排成一排，而是已经按“选择器权重 + 书写顺序”算好了“谁最终生效”。所以你在 007 学到的优先级，发生在这个阶段。

## 3. 第三步：DOM + CSSOM 合成渲染树

浏览器把 DOM 和 CSSOM 合并成渲染树（Render Tree）：遍历 DOM 节点，为每个需要显示的节点挂上最终样式。

```mermaid
flowchart LR
    A["HTML 文件"] --> B["DOM 树"]
    C["CSS 文件"] --> D["CSSOM 树"]
    B --> E["渲染树 Render Tree"]
    D --> E
    E --> F["布局 Layout"]
    F --> G["绘制 Paint"]
    G --> H["合成 Composite"]
```

**讲解：** 渲染树只保留“要画出来”的节点。`display: none` 的元素不会进入渲染树；`visibility: hidden` 的元素会进入但不显示。这也是为什么 `display: none` 能直接“移除”布局占位。

## 4. 第四步：布局、绘制与合成

渲染树里的每个节点都有了样式，接下来浏览器计算它在页面上的位置和大小（布局 Layout），再把它画成像素（绘制 Paint），最后把多个图层合并成你看到的画面（合成 Composite）。

**讲解：** 修改 `width`、`padding` 会触发“布局 + 绘制 + 合成”全链路，代价最高；修改 `transform`、`opacity` 只触发合成，代价最低。入门阶段记住结论即可：动位置、大小比动透明度贵得多。

## 5. 为什么 `link` 要放在 `<head>`？

因为 CSS 是“渲染阻塞资源”：浏览器在 CSSOM 构建完成之前，不会把页面画给用户。`<link>` 放在 `<head>` 里，能让浏览器尽早开始下载 CSS；放在 `<body>` 底部虽然也能生效，但浏览器可能先渲染出一版没有样式的页面，再突然“闪”成有样式的样子。

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>标题</h1>
  </body>
</html>
```

**讲解：** 这是“为什么所有教程都让你把样式放头部”的底层原因——不是习惯，而是渲染流程决定的。

## 6. 与 035 的分工

`css/060-CriticalRenderPathOptimization` 讲的是“如何让这条流程更快”：压缩 CSS、去掉阻塞、延迟非关键样式等。本课只要建立流程直觉：

- HTML → DOM；
- CSS → CSSOM；
- DOM + CSSOM → 渲染树；
- 布局 → 绘制 → 合成。

## 7. 动手试试

1. 打开任意网页，按 F12 打开开发者工具，切到 Performance（性能）面板，刷新页面，观察 HTML/CSS 的加载瀑布；
2. 把页面里的 `<style>` 从 `<head>` 挪到 `<body>` 末尾，刷新看是否有“样式闪烁”；
3. 给元素加 `display: none` 与 `visibility: hidden`，对比 DevTools 布局面板中占位的变化；
4. 进阶挑战：在 DevTools 的 Rendering 面板勾选 Paint Flashing，观察修改 `width` 与修改 `transform` 时重绘区域的差别。

## 8. 核心知识点

> 一句话记住 CSS 工作原理：HTML 建 DOM，CSS 建 CSSOM，两棵树合成渲染树，再布局、绘制、合成。

- DOM 是 HTML 的结构树，CSS 选择器在 DOM 上匹配节点；
- CSSOM 是解析后的样式树，优先级计算发生在这里；
- 渲染树 = DOM + CSSOM 中“需要显示”的节点；
- 布局算位置，绘制画像素，合成拼图层；
- CSS 阻塞渲染，所以 `link` 放 `<head>`；
- 改尺寸触发全链路，改 `transform`/`opacity` 只触发合成。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 样式闪烁 | `link` 放 body 底部或 CSS 太大 | `link` 放 `<head>`，必要时内联首屏关键样式 |
| 认为 display:none 只是“看不见” | 它会让元素完全退出渲染树 | 需要保留占位用 `visibility: hidden` |
| 过度追求“性能技巧” | 入门阶段不必背全部渲染细节 | 先记“改尺寸贵、改合成便宜” |
| 用 JS 频繁改布局属性 | 每次修改都触发重排 | 批量修改或用 `transform` 动画 |

## 10. 扩展学习

- 关键渲染路径深入：`css/060-CriticalRenderPathOptimization`；
- 引入方式与渲染阻塞：`css/011-StyleSheetImportMethod`；
- 优先级计算：`css/009-PriorityCalculation`；
- HTML 结构基础：`html5/006-HTML5OverviewCoreFeature`。

<!-- ============ 文档分隔线：007-css/003-CSS3BoxModelDetailed.md ============ -->

## 0. 阅读指南

本章文档难度标记为 intermediate，是因为末尾包含 BFC 与 margin 塌陷两个进阶主题。按难度分层阅读：

- **入门必读（第 1-2 节、第 3.1-3.2 节）**：盒模型的四层组成、`content-box` 与 `border-box`、margin/padding 的基本用法——这是布局的地基，第一遍精读并完成动手试试；
- **进阶选读（第 3.3 节、第 4 节）**：margin 塌陷与 BFC 触发条件，第一遍可以跳过，先读 `css/013-MarginCollapse` 与 `css/016-StackingContext` 的速通部分，再回头看本节；
- **参考章节（第 5-7 节）**：应用、最佳实践与高级技巧，随用随查。

这样安排后，本章的“入门路径”实际难度为 beginner：先会算盒子尺寸，再逐步进入格式化上下文。

## 1. 盒模型组成 (Components)

### 1.1 基本组成

每个 HTML 元素都被视为一个矩形盒子，由以下四个部分组成：
| 组成部分 | 描述 | 特性 |
|---------|------|------|
| **Content (内容)** | 实际的文本、图片等内容 | 由 `width` 和 `height` 属性控制大小 |
| **Padding (内边距)** | 内容与边框之间的透明区域 | 可以使用 `padding` 属性设置，会影响元素的实际大小 |
| **Border (边框)** | 围绕 Padding 和 Content 的线 | 由 `border` 属性控制，包括宽度、样式和颜色 |
| **Margin (外边距)** | 盒子与其他元素之间的间距 | 由 `margin` 属性控制，是透明的，不会影响元素自身大小 |

### 1.2 盒模型示意图

```mermaid
flowchart TD
    B0["Margin"]
    B1["Border"]
    B0 --> B1
    B2["Padding"]
    B1 --> B2
    B3["Content"]
    B2 --> B3
```

### 1.3 代码示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .box {
        width: 200px;
        height: 100px;
        padding: 20px;
        border: 5px solid #333;
        margin: 15px;
        background-color: #f0f0f0;
      }
    </style>
  </head>
  <body>
    <div class="box">内容区域</div>
  </body>
</html>
```

## 2. 盒模型类型 (Box Sizing)

### 2.1 标准盒模型 (`content-box`)

**默认值**，遵循 W3C 标准。

- **宽度计算**: `width = 内容宽度`
- **实际占用空间**: `width + padding + border`
- **特点**: 当增加 `padding` 或 `border` 时，元素的实际宽度会增加
  **代码示例**:

```css
.standard-box {
  box-sizing: content-box;
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  /* 实际宽度: 200 + 20*2 + 5*2 = 250px */
}
```

### 2.2 怪异/IE 盒模型 (`border-box`)

**推荐使用**，更符合直觉的盒模型。

- **宽度计算**: `width = 内容宽度 + padding + border`
- **实际占用空间**: 等于设置的 `width`
- **特点**: 当增加 `padding` 或 `border` 时，元素的实际宽度不会改变，只会压缩内容区域
  **代码示例**:

```css
.border-box {
  box-sizing: border-box;
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  /* 实际宽度: 200px (内容宽度被压缩为 150px) */
}
```

### 2.3 全局盒模型设置

推荐在项目中全局使用 `border-box`，这样可以更方便地控制元素大小：

```css
 /* 方法 1: 全局设置 */
 * {
  box-sizing: border-box;
 }
 /* 方法 2: 更精确的设置，包括伪元素 */
 * {
  box-sizing: border-box;
 }
 /* 方法 3: 继承方式，更灵活 */
 html {
  box-sizing: border-box;
 }
 * {
  box-sizing: inherit;
 }
```

### 2.4 盒模型类型的应用场景

| 场景             | 推荐盒模型    | 原因                               |
| ---------------- | ------------- | ---------------------------------- |
| 响应式布局       | `border-box`  | 更容易计算元素尺寸，避免布局错位   |
| 固定宽度布局     | `border-box`  | 可以随意调整内边距而不影响整体布局 |
| 第三方组件集成   | `content-box` | 保持与原始组件一致的盒模型行为     |
| 精确控制内容区域 | `content-box` | 可以准确控制内容区域的大小         |

## 3. 外边距特性 (Margin Features)

### 3.1 外边距的基本用法

```css
/* 四个方向的外边距 */
margin: 10px; /* 四个方向都是 10px */
margin: 10px 20px; /* 上下 10px，左右 20px */
margin: 10px 20px 30px; /* 上 10px，左右 20px，下 30px */
margin: 10px 20px 30px 40px; /* 上 10px，右 20px，下 30px，左 40px */
/* 单个方向的外边距 */
margin-top: 10px;
margin-right: 20px;
margin-bottom: 30px;
margin-left: 40px;
```

### 3.2 水平居中

使用 `margin: 0 auto;` 可以实现块级元素的水平居中：

```css
.centered {
  width: 50%; /* 必须指定宽度 */
  margin: 0 auto; /* 上下外边距为 0，左右自动 */
}
```

**代码示例**:

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .container {
        width: 100%;
        background-color: #f0f0f0;
      }
      .centered-box {
        width: 50%;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border: 1px solid #ddd;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="centered-box">这个盒子水平居中</div>
    </div>
  </body>
</html>
```

### 3.3 外边距塌陷 (Margin Collapse)

**定义**：在垂直方向上，相邻的两个外边距会取最大值，而非累加。

#### 3.3.1 常见的外边距塌陷场景

1. **相邻元素的外边距塌陷**

```html
<div style="margin-bottom: 30px;">元素 1</div>
<div style="margin-top: 20px;">元素 2</div>
<!-- 实际间距: 30px (取最大值)，而非 50px -->
```

1. **父子元素的外边距塌陷**

```html
<div style="margin-top: 20px;">
  <div style="margin-top: 30px;">子元素</div>
</div>
<!-- 实际间距: 30px (取最大值)，而非 50px -->
```

1. **空元素的外边距塌陷**

```html
<div style="margin-top: 20px; margin-bottom: 30px;"></div>
<!-- 实际高度: 30px (取最大值)，而非 50px -->
```

#### 3.3.2 解决外边距塌陷的方法

| 方法           | 适用场景     | 代码示例                         |
| -------------- | ------------ | -------------------------------- |
| **添加边框**   | 父子元素塌陷 | `border: 1px solid transparent;` |
| **添加内边距** | 父子元素塌陷 | `padding: 1px;`                  |
| **使用 BFC**   | 各种塌陷场景 | `overflow: hidden;`              |
| **使用浮动**   | 相邻元素塌陷 | `float: left;`                   |
| **使用定位**   | 相邻元素塌陷 | `position: absolute;`            |

**代码示例**:

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .parent {
        background-color: #f0f0f0;
        /* 方法 1: 添加边框 */
        /* border: 1px solid transparent; */
        /* 方法 2: 添加内边距 */
        /* padding: 1px; */
        /* 方法 3: 使用 BFC */
        overflow: hidden;
      }
      .child {
        margin-top: 30px;
        padding: 20px;
        background-color: #fff;
      }
    </style>
  </head>
  <body>
    <div class="parent">
      <div class="child">子元素</div>
    </div>
  </body>
</html>
```

## 4. BFC (块级格式化上下文)

### 4.1 BFC 的定义

**块级格式化上下文** (Block Formatting Context) 是一个独立的渲染区域，内部元素的布局不会影响外部元素，外部元素也不会影响内部元素。

### 4.2 触发 BFC 的条件

| 条件                      | 代码示例                                                        |
| ------------------------- | --------------------------------------------------------------- |
| **浮动元素**              | `float: left;` 或 `float: right;`                               |
| **绝对定位元素**          | `position: absolute;` 或 `position: fixed;`                     |
| **行内块元素**            | `display: inline-block;`                                        |
| **表格单元格**            | `display: table-cell;`                                          |
| **弹性容器**              | `display: flex;` 或 `display: inline-flex;`                     |
| **网格容器**              | `display: grid;` 或 `display: inline-grid;`                     |
| **overflow 不为 visible** | `overflow: hidden;` 或 `overflow: auto;` 或 `overflow: scroll;` |
| **根元素**                | `<html>` 元素                                                   |

### 4.3 BFC 的作用

#### 4.3.1 清除浮动

当父元素包含浮动子元素时，父元素会塌陷，使用 BFC 可以解决这个问题：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .parent {
        background-color: #f0f0f0;
        /* 触发 BFC */
        overflow: hidden;
      }
      .child {
        float: left;
        width: 100px;
        height: 100px;
        margin: 10px;
        background-color: #fff;
      }
    </style>
  </head>
  <body>
    <div class="parent">
      <div class="child">子元素 1</div>
      <div class="child">子元素 2</div>
      <div class="child">子元素 3</div>
    </div>
  </body>
</html>
```

#### 4.3.2 防止外边距重叠

使用 BFC 可以防止父子元素或相邻元素的外边距重叠：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .container {
        /* 触发 BFC */
        overflow: hidden;
      }
      .box {
        margin: 20px;
        padding: 20px;
        background-color: #f0f0f0;
      }
    </style>
  </head>
  <body>
    <div class="box">Box 1</div>
    <div class="container">
      <div class="box">Box 2 (在 BFC 中)</div>
    </div>
  </body>
</html>
```

#### 4.3.3 实现两栏布局

使用 BFC 可以实现经典的两栏布局：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      .container {
        width: 100%;
      }
      .sidebar {
        float: left;
        width: 200px;
        height: 300px;
        background-color: #f0f0f0;
      }
      .content {
        /* 触发 BFC */
        overflow: hidden;
        height: 300px;
        background-color: #e0e0e0;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="sidebar">侧边栏</div>
      <div class="content">主内容区</div>
    </div>
  </body>
</html>
```

## 5. 盒模型的实际应用

### 5.1 响应式布局中的盒模型

在响应式布局中，使用 `border-box` 可以更方便地控制元素大小：

```css
 /* 全局盒模型设置 */
 * {
  box-sizing: border-box;
 }
 /* 响应式网格 */
 .row {
  display: flex;
  flex-wrap: wrap;
  margin: 0 -15px;
 }
 .col {
  flex: 1;
  padding: 0 15px;
 }
 /* 媒体查询 */
 @media (max-width: 768px) {
  .col {
  flex: 0 0 100%;
  }
 }
```

### 5.2 卡片式布局

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <style>
      * {
        box-sizing: border-box;
      }
      .card {
        width: 300px;
        margin: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      }
      .card-header {
        padding: 15px;
        background-color: #f5f5f5;
        border-bottom: 1px solid #ddd;
      }
      .card-body {
        padding: 15px;
      }
      .card-footer {
        padding: 15px;
        background-color: #f5f5f5;
        border-top: 1px solid #ddd;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <div class="card-header">卡片标题</div>
      <div class="card-body">卡片内容</div>
      <div class="card-footer">卡片底部</div>
    </div>
  </body>
</html>
```

### 5.3 表单元素的盒模型

```css
/* 表单元素的盒模型设置 */
input,
textarea,
select {
  box-sizing: border-box;
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
/* 按钮的盒模型设置 */
button {
  box-sizing: border-box;
  padding: 10px 20px;
  border: 1px solid #333;
  border-radius: 4px;
  background-color: #f0f0f0;
}
```

## 6. 盒模型的最佳实践

### 6.1 代码风格建议

- **统一盒模型**: 全局使用 `border-box` 以保持一致性
- **合理使用简写**: 优先使用 `margin` 和 `padding` 的简写形式
- **明确单位**: 统一使用 `px`、`em` 或 `rem` 等单位
- **避免负外边距**: 除非有特殊需求，否则避免使用负外边距
- **使用相对单位**: 在响应式布局中，使用相对单位如 `%`、`em` 或 `rem`

### 6.2 性能优化建议

- **减少不必要的嵌套**: 减少 DOM 元素的嵌套层级，避免过多的盒模型计算
- **合理使用 BFC**: 只在需要时触发 BFC，避免不必要的渲染开销
- **避免使用 `*` 选择器**: 尽量使用更具体的选择器，减少浏览器的计算负担
- **优化盒阴影**: 复杂的盒阴影会影响性能，使用时要适度

### 6.3 常见问题与解决方案

| 问题                 | 原因                        | 解决方案                               |
| -------------------- | --------------------------- | -------------------------------------- |
| **元素大小超出预期** | 使用了 `content-box` 盒模型 | 切换到 `border-box` 盒模型             |
| **布局错位**         | 外边距塌陷或浮动元素未清除  | 使用 BFC 清除浮动或防止外边距塌陷      |
| **响应式布局失效**   | 未正确设置盒模型            | 全局使用 `border-box` 并使用相对单位   |
| **表单元素对齐问题** | 表单元素的盒模型不一致      | 统一设置表单元素的盒模型和垂直对齐方式 |

## 7. 盒模型的高级技巧

### 7.1 计算盒模型的实际大小

使用 JavaScript 可以获取元素的实际盒模型大小：

```javascript
// 获取元素
const element = document.querySelector('.box');
// 获取计算后的样式
const computedStyle = window.getComputedStyle(element);
// 获取盒模型各部分的大小
const width = parseFloat(computedStyle.width);
const paddingLeft = parseFloat(computedStyle.paddingLeft);
const paddingRight = parseFloat(computedStyle.paddingRight);
const borderLeft = parseFloat(computedStyle.borderLeftWidth);
const borderRight = parseFloat(computedStyle.borderRightWidth);
// 计算实际宽度
const actualWidth = width + paddingLeft + paddingRight + borderLeft + borderRight;
console.log('实际宽度:', actualWidth);
```

### 7.2 使用 CSS 变量控制盒模型

```css
 :root {
  --box-padding: 20px;
  --box-border: 5px;
  --box-margin: 15px;
 }
 .box {
  padding: var(--box-padding);
  border: var(--box-border) solid #333;
  margin: var(--box-margin);
 }
 /* 响应式调整 */
 @media (max-width: 768px) {
  :root {
  --box-padding: 10px;
  --box-border: 3px;
  --box-margin: 10px;
  }
 }
```

### 7.3 盒模型与 Flexbox/Grid 的结合

盒模型与现代布局技术（如 Flexbox 和 Grid）结合使用，可以创建更灵活的布局：

```css
/* Flexbox 布局 */
.flex-container {
  display: flex;
  gap: 20px; /* 替代 margin */
}
.flex-item {
  flex: 1;
  padding: 20px;
  border: 1px solid #ddd;
}
/* Grid 布局 */
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px; /* 替代 margin */
}
.grid-item {
  padding: 20px;
  border: 1px solid #ddd;
}
```

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

## 动手试试

### 入门版（必做）

1. 写一个 200px 宽的盒子，加 `padding: 20px` 和 `border: 5px`，用开发者工具确认实际占宽是 250px；
2. 加上 `box-sizing: border-box` 再观察，确认实际占宽变为 200px；
3. 写两个上下相邻的块元素，分别设 30px/20px 外边距，确认实际间距是 30px。

### 进阶版（选做）

1. 用 `margin: 0 auto` 实现居中，再对比 Flexbox 居中；
2. 用 `overflow: hidden` 让父元素包住浮动的子元素；
3. 用 `display: flow-root` 解决父子外边距塌陷。

## 核心知识点

> 一句话记住盒模型：`content` 是礼物，`padding` 是填充，`border` 是外壳，`margin` 是间距；`border-box` 让宽高按直觉计算。

- 盒模型四层：content → padding → border → margin；
- `content-box` 的 width 只算内容；`border-box` 的 width 包含 padding 和 border；
- 现代项目全局使用 `box-sizing: border-box`；
- 垂直外边距会塌陷（取最大值），水平不会；
- 解决方案：`overflow: hidden`、`display: flow-root`、padding/border 替代；
- BFC 可清除浮动、防止外边距合并、实现两栏布局。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记全局 border-box | 宽度计算处处踩坑 | `* { box-sizing: border-box }` |
| 外边距相加的错觉 | 垂直间距比预期小 | 记住塌陷规则，用 padding 或 BFC 规避 |
| 用 margin 实现垂直居中 | 无效 | 用 Flexbox/Grid 或 absolute + transform |
| 误用 `outline: none` | 键盘焦点不可见 | 保留或替换为可见焦点样式 |
| 用 `display: none` 做动画 | 无法过渡 | 用 visibility/opacity 配合 |
| 内容溢出无处理 | 布局被撑破 | 检查 box-sizing 与 overflow |

## 扩展学习

- 边距塌陷详解：`css/013-MarginCollapse`；
- 定位与层叠：`css/014-PositionDetailed`、`css/016-StackingContext`；
- 现代布局：`css/021-CSS3FlexboxFlexLayout`、`css/022-CSS3GridGridLayout`；
- 尺寸单位：`css/001-CSS3OverviewBasicSyntax` 中单位章节；
- 性能：避免大面积重排时的高频尺寸读写。

<!-- ============ 文档分隔线：007-css/004-TextAndFontsBasics.md ============ -->

## 0. 直觉：把文字当成“可以被打扮的内容”

页面里 90% 的内容是文字。CSS 控制文字有两组开关：一组管“字体长什么样”（`font-*`），一组管“文字怎么摆”（`text-*`）。本课把最常用的十几个属性一次讲清，排版进阶（字号阶梯、网格基准线）见 `css/044-TypographyAndGridSystem`。

## 1. font-family：用哪套字体

```css
body {
  font-family: "PingFang SC", "Microsoft YaHei", "Helvetica Neue", Arial, sans-serif;
}
```

**讲解：** 浏览器从左到右找用户电脑里第一个存在的字体；都不存在就用最后的兜底类别（`sans-serif`/`serif`/`monospace`）。多个字体之间用逗号分隔，字体名含空格时加引号。

常用系统字体栈：

```css
/* 中文阅读：无衬线优先 */
font-family: "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;

/* 代码：等宽优先 */
font-family: "JetBrains Mono", Consolas, "Courier New", monospace;
```

## 2. font-size：字号

```css
html {
  font-size: 16px;   /* 根字号，rem 的参照 */
}
p {
  font-size: 16px;   /* 固定像素 */
}
.note {
  font-size: 0.875rem; /* 相对根字号：16px * 0.875 = 14px */
}
```

**讲解：** `px` 是固定大小；`em` 相对“父元素字号”；`rem` 相对“根元素字号”。入门阶段推荐正文用 `px` 或 `rem`，响应式排版再引入 `clamp()`（见 `css/053-Function`）。

## 3. font-weight 与 font-style

```css
.bold {
  font-weight: 700;   /* 或 bold，正常是 400/normal */
}
.lighter {
  font-weight: 300;
}
.italic {
  font-style: italic; /* 斜体 */
}
```

**讲解：** 常见字重是 400（常规）与 700（加粗）。没有安装对应字重时，浏览器会合成加粗或加细，效果可能发虚；重要标题建议加载真实字重（见 `css/047-CSSFontLoading`）。

## 4. line-height：行高

```css
p {
  line-height: 1.6;   /* 无单位倍数，最佳实践 */
}
```

**讲解：** 无单位的 `line-height` 是“当前字号的倍数”，会随字号自动缩放，是正文的标准写法。1.5-1.8 适合中文正文，按钮等紧凑元素常用 1。

## 5. text-align 与 text-decoration

```css
.center {
  text-align: center;   /* left/right/center/justify */
}
a {
  text-decoration: none; /* 去掉下划线 */
}
.strike {
  text-decoration: line-through;
}
```

**讲解：** `text-align` 控制块内文本的水平对齐；`text-decoration` 控制下划线/删除线等装饰，常用于链接去下划线。

## 6. 字距与缩进

```css
.spread {
  letter-spacing: 2px;   /* 字符间距 */
  word-spacing: 4px;     /* 词间距（中文几乎无效） */
}
.indent {
  text-indent: 2em;      /* 首行缩进两个字符 */
}
```

**讲解：** 标题加 `letter-spacing` 能提升精致感，正文慎用；`text-indent: 2em` 是中文段落首行缩进的标准写法。

## 7. 完整示例：一篇文章的正文样式

```html
<style>
  body {
    font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
    font-size: 16px;
    line-height: 1.7;
    color: #333;
  }
  h1 {
    font-size: 28px;
    font-weight: 700;
    letter-spacing: 1px;
  }
  p {
    text-indent: 2em;
    margin-bottom: 12px;
  }
  .price {
    font-size: 20px;
    font-weight: 700;
    color: #d63031;
  }
</style>
<h1>标题</h1>
<p>正文段落，首行缩进两个字符，行高 1.7 更易读。</p>
<p class="price">价格：99 元</p>
```

**讲解：** 这是“文章页最小可用排版”：中文字体栈 + 1.7 行高 + 首行缩进 + 标题层级，已经超过大多数默认页面。

## 8. 动手试试

1. 给页面设置中文字体栈，刷新对比默认字体；
2. 把 `line-height` 从 1 调到 2，观察行距变化，找到最舒适的数值；
3. 用 `letter-spacing` 给标题加间距，对比正文效果；
4. 进阶挑战：用 `rem` 写一套“正文 16px、注释 14px、标题 28px”的字号体系。

## 9. 核心知识点

> 一句话记住文本与字体：`font-family` 定字体，`font-size` 定大小，`line-height` 定行距，`text-*` 管对齐与装饰。

- `font-family` 多字体回退，末尾必须放通用类别；
- `px`/`em`/`rem`：固定、相对父级、相对根元素；
- `font-weight` 用 400/700，`font-style` 用 `italic`；
- `line-height` 用无单位倍数，正文 1.5-1.8；
- `text-align` 管对齐，`text-decoration` 管装饰；
- `letter-spacing` 用于标题，`text-indent: 2em` 用于中文首行缩进。

## 10. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 字体栈末尾忘了通用类别 | 找不到字体时回退不可控 | 末尾写 `sans-serif`/`serif`/`monospace` |
| 行高用固定 px | 字号变化后行距失调 | 用无单位倍数 |
| 正文用 letter-spacing | 中文正文拉大字距反而难读 | 只给标题加字距 |
| 中文字体用 font-weight 加粗 | 合成加粗发虚 | 加载真实字重或使用系统粗体 |
| 首行缩进用空格 | 复制粘贴后排版错乱 | 用 `text-indent: 2em` |

## 11. 扩展学习

- 排版进阶：`css/044-TypographyAndGridSystem`；
- 字体加载与 @font-face：`css/047-CSSFontLoading`；
- 响应式字号（clamp）：`css/053-Function`；
- 盒模型与间距：`css/003-CSS3BoxModelDetailed`。

<!-- ============ 文档分隔线：007-css/005-ShorthandProperties.md ============ -->

## 0. 直觉：一个属性写四个方向，省代码也藏陷阱

`margin: 10px 20px` 比 `margin-top/right/bottom/left` 四行短得多，这就是简写属性（shorthand）。它把多个子属性合并成一条声明，但代价是：**没写的子属性会被重置为初始值**。理解这条代价，是工程上避免“样式莫名消失”的关键。

## 1. margin/padding 的 1-4 值规则

```css
/* 1 个值：四边相同 */
margin: 10px;

/* 2 个值：上下 | 左右 */
margin: 10px 20px;

/* 3 个值：上 | 左右 | 下 */
margin: 10px 20px 30px;

/* 4 个值：上 | 右 | 下 | 左（顺时针） */
margin: 10px 20px 30px 40px;
```

**讲解：** 记忆口诀“上右下左，顺时针”。`padding` 规则完全相同。`border-width`/`border-style`/`border-radius` 等方向类简写也遵循同一套规则。

## 2. border 简写

```css
.card {
  border: 1px solid #ddd;   /* width style color，顺序任意 */
  border-radius: 8px;
}
```

**讲解：** `border` 一行同时设置宽度、样式、颜色；只写 `border: 1px` 不合法，因为 `border-style` 默认为 `none`（不显示）。`border-radius` 有自己的 1-4 值规则（水平/垂直、四角）。

## 3. background 完整简写

```css
.banner {
  background: #f5f5f5 url("bg.png") no-repeat center / cover;
}
```

**讲解：** `background` 可合并颜色、图片、重复方式、位置、尺寸、附加方式等。注意两点：未写子属性会重置（例如只写 `background: url(...)` 会把颜色清掉）；`background-size` 用 `/` 与位置分隔。多背景分别写时，拆成 `background-image`/`background-color` 更安全。完整体系见 `css/026-BackgroundEnhancement`。

## 4. font 简写

```css
.article {
  font: italic 700 16px/1.7 "PingFang SC", sans-serif;
}
```

**讲解：** `font` 的格式是 `style weight size/line-height family`，其中 `size` 与 `family` 必填，其余可省。**只要写了 `font`，未写部分（如 `font-weight`）就会重置**，因此很少用于整段覆盖，常用于集中设置一组排版属性。

## 5. 其他常用简写

```css
.item {
  /* 动画 */
  animation: spin 2s linear infinite;
  /* 过渡 */
  transition: transform 0.3s ease;
  /* 列表 */
  list-style: none;
  /* 外框 */
  outline: 2px solid #4f5bd5;
  /* 文本装饰 */
  text-decoration: underline wavy red;
}
```

**讲解：** 规则一致：简写覆盖一组相关属性，未写的子属性回到初始值。动画/过渡/列表/外框的细节分别见 `css/028-CSSAnimationTransition`、`css/017-CSSListStyle` 对应文档。

## 6. 简写会重置未指定属性

这是简写最重要的一条陷阱：

```css
.btn {
  background-color: #d63031;
  transition: transform 0.2s ease;
}
.btn:hover {
  background: #e17055;   /* 注意：background 简写把颜色覆盖为 #e17055 是期望，但若写成 background: none，颜色也会被重置 */
}
```

```css
/* 反面案例：只想改背景图，却用简写 */
.card {
  background: #fff;
}
.card.featured {
  background: url("badge.png") no-repeat;  /* #fff 被重置为透明 */
}
```

**讲解：** 修复方式是“用子属性覆盖子属性”：`background-image: url(...)` 只改图片，保留颜色。凡是“只想改其中一项”的场景，都优先写子属性。

## 7. 动手试试

1. 用 1-4 值分别设置 `padding`，在 DevTools 盒模型图确认四边值；
2. 写 `background: url(...)` 覆盖原本有背景色的元素，观察颜色消失，再用 `background-color` 修复；
3. 用 `font` 简写集中设置一段文章排版，再单独改 `font-weight`，观察是否被重置；
4. 进阶挑战：整理一份自己项目里“应拆成子属性”的简写清单。

## 8. 核心知识点

> 一句话记住简写属性：简写省代码，但未写的子属性会被重置；只改一项就用子属性。

- `margin`/`padding` 的 1-4 值按“上右下左”顺时针；
- `border` 合并宽度、样式、颜色，缺样式不显示；
- `background` 可合并全部背景子属性，`size` 用 `/` 分隔；
- `font` 合并 style/weight/size/line-height/family，size 与 family 必填；
- 简写会重置未指定子属性，覆盖场景优先用子属性；
- 同一定义多次简写时，后写会清掉前面简写覆盖的子属性。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 简写覆盖整段背景 | 颜色/图片被意外重置 | 单属性覆盖单属性 |
| `font` 简写后单独改字重无效 | 顺序问题或再次被重置 | 把 `font` 放最前，子属性放后面 |
| 记混 3 值与 4 值方向 | 布局间距出错 | 写注释标明方向，或拆成子属性 |
| 多背景用简写 | 可读性差、易错 | 多背景拆开写 `background-image` |

## 10. 扩展学习

- 盒模型与方向属性：`css/003-CSS3BoxModelDetailed`；
- 背景完整体系：`css/026-BackgroundEnhancement`；
- 文本与字体：`css/004-TextAndFontsBasics`；
- 动画与过渡简写：`css/028-CSSAnimationTransition`。

<!-- ============ 文档分隔线：007-css/006-CSSValuesAndUnits.md ============ -->

## 0. 直觉：同样的“100”，在不同单位下含义完全不同

`100px` 是固定长度，`100%` 是父容器比例，`100vw` 是视口宽度，`100ch` 是字符宽度。单位决定“数值相对谁”，选错单位是响应式布局最常见的错误来源。

## 1. 绝对单位 vs 相对单位

| 类别 | 单位 | 特点 |
| --- | --- | --- |
| 绝对 | `px` | 屏幕物理像素的 CSS 抽象，最可预测 |
| 绝对 | `pt`/`cm`/`mm`/`in` | 印刷单位，网页几乎不用 |
| 相对 | `%` | 相对父元素（宽度/高度语义不同） |
| 相对 | `em`/`rem` | 相对字号 |
| 相对 | `vw`/`vh`/`vmin`/`vmax` | 相对视口 |
| 相对 | `ch`/`ex` | 相对字体度量 |

**讲解：** 网页布局“默认信任 `px`”，需要随容器/视口/字号伸缩时才切换相对单位。

## 2. `%` 的两种语义

```css
.child {
  width: 50%;   /* 相对父元素内容宽度 */
  margin-top: 10%;  /* 注意：上下 margin 的百分比也相对“宽度” */
}
```

**讲解：** `width: 50%` 相对父容器宽度；`height: 50%` 只有在父元素有确定高度时才有意义。而 `margin`/`padding` 的百分比（上下左右）一律相对父元素宽度，这是常见误区。

## 3. em 与 rem 的详细对比

```css
html {
  font-size: 16px;
}
.parent {
  font-size: 20px;
}
.child-em {
  font-size: 1.5em;  /* 相对父级：20px * 1.5 = 30px */
}
.child-rem {
  font-size: 1.5rem; /* 相对根：16px * 1.5 = 24px */
}
```

**讲解：**

- `rem` 永远相对根元素字号，层级再多也不变，适合全局字号体系；
- `em` 相对最近父级字号，嵌套时会“叠加放大”，适合需要随上下文缩放的元素（如按钮内边距）；
- 用 `em` 做 `padding` 时，内边距会随自身字号变化，这是实现“按钮越大、内边距越大”的常用技巧。

## 4. 视口单位：vw/vh/vmin/vmax

```css
.hero {
  height: 100vh;          /* 一屏高 */
  font-size: 5vw;         /* 随视口宽度缩放 */
}
.cover {
  width: 100vmin;         /* 取视口宽高较小者 */
}
```

**讲解：** `vw` 是视口宽度的 1%，`vh` 是视口高度的 1%，`vmin`/`vmax` 取两者的小/大值。移动端注意地址栏伸缩会让 `100vh` 跳动，常改用 `100dvh`（动态视口）或 `min-height`。

## 5. 字体相对单位：ch/ex/cap

```css
code {
  max-width: 60ch;  /* 约 60 个字符宽，代码行宽标准做法 */
}
```

**讲解：** `ch` 是“0”字符的宽度，`ex` 是“x”字母高度，`cap` 是大写字母高度。它们让尺寸跟随字体度量，常用于限定阅读行宽与首字下沉；中文场景 `ch` 约等于一个汉字宽度，做中文段落行宽同样好用。

## 6. 单位选择决策表

| 场景 | 推荐 | 原因 |
| --- | --- | --- |
| 边框、阴影、圆角 | `px` | 不随缩放，视觉稳定 |
| 全局字号体系 | `rem` | 跟随根字号，方便整体缩放 |
| 组件内自缩放 | `em` | 随自身/父级字号联动 |
| 容器占比 | `%` | 跟随父容器 |
| 全屏/首屏区域 | `vh`/`dvh` | 跟随视口高度 |
| 阅读行宽 | `ch` | 跟随字符度量 |
| 流体字号 | `clamp()` + `vw` | 见 `css/053-Function` |

## 7. 动手试试

1. 分别用 `px`/`em`/`rem` 给同一元素设置字号，用 DevTools Computed 面板查看最终像素值；
2. 给嵌套三层父级各设不同字号，对比 `em` 与 `rem` 的叠加效果；
3. 用 `100vh` 做全屏区块，在手机模拟器上观察地址栏伸缩时的跳动，再换 `100dvh`；
4. 进阶挑战：给文章设置 `max-width: 65ch`，对比不同字号下的阅读体验。

## 8. 核心知识点

> 一句话记住值与单位：`px` 稳、`%` 随容器、`rem` 随根字号、`em` 随父级、`vw/vh` 随视口、`ch` 随字符。

- 绝对单位网页只用 `px`，其余留给印刷；
- `margin`/`padding` 的百分比相对宽度；
- `rem` 相对根字号，`em` 相对父级字号且会叠加；
- `vw`/`vh` 相对视口，移动端优先 `dvh`；
- `ch` 约等于一个字符宽，适合行宽限制；
- 复杂场景用 `calc()`/`clamp()` 组合，见 `css/053-Function`。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| `height: 50%` 不生效 | 父元素没有确定高度 | 用 `min-height` 或视口单位 |
| 深层嵌套 em 失控 | 字号层层叠加 | 优先 `rem`，只在局部用 `em` |
| 移动端 100vh 跳动 | 地址栏占位变化 | 用 `100dvh` 或 `min-height: 100dvh` |
| 百分比与视口混用 | 嵌套层级变化后难预测 | 先定“相对谁”，再选单位 |

## 10. 扩展学习

- 函数与流体排版：`css/053-Function`；
- 文本与字体基础：`css/004-TextAndFontsBasics`；
- 响应式设计：`css/033-ResponsiveDesign`；
- 移动端适配：`css/052-MobileAdaptation`。

<!-- ============ 文档分隔线：007-css/007-CSS3SelectorSystem.md ============ -->

## 1. 基础选择器

基础选择器是 CSS 中最基本的选择器类型，用于选择 HTML 元素。

### 1.1 通配符选择器

通配符选择器 (`*`) 匹配文档中的所有元素：

```css
 /* 匹配所有元素 */
 * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
 }
 /* 匹配特定元素内的所有元素 */
 .container * {
  color: #333;
 }
```

**使用场景**：

- 重置默认样式
- 对特定容器内的所有元素应用通用样式
  **注意**：通配符选择器的性能较低，应谨慎使用。

### 1.2 标签选择器

标签选择器匹配指定类型的 HTML 元素：

```css
/* 匹配所有 <p> 元素 */
p {
  font-size: 16px;
  line-height: 1.5;
}
/* 匹配所有 <div> 元素 */
div {
  margin-bottom: 20px;
}
/* 匹配所有 <h1> 到 <h6> 元素 */
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: bold;
  color: #333;
}
```

**使用场景**：

- 对特定类型的元素应用通用样式
- 重置或覆盖浏览器默认样式

### 1.3 类选择器

类选择器 (`.*`) 匹配具有指定类名的元素：

```css
/* 匹配所有带有 .container 类的元素 */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}
/* 匹配所有带有 .button 类的元素 */
.button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
/* 匹配同时带有 .button 和 .primary 类的元素 */
.button.primary {
  background-color: #3498db;
  color: white;
}
```

**使用场景**：

- 对多个不同类型的元素应用相同的样式
- 为元素添加特定的样式类

### 1.4 ID 选择器

ID 选择器 (`#*`) 匹配具有指定 ID 的元素：

```css
/* 匹配 ID 为 header 的元素 */
#header {
  background-color: #f8f9fa;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* 匹配 ID 为 main-content 的元素 */
#main-content {
  padding: 30px;
  background-color: white;
}
```

**使用场景**：

- 选择页面中唯一的元素
- 为特定元素应用独特的样式
  **注意**：ID 选择器的权重较高，应谨慎使用，避免过度使用导致样式难以覆盖。

### 1.5 属性选择器

属性选择器匹配具有指定属性或属性值的元素：

```css
/* 匹配具有 href 属性的元素 */
[a] {
  color: #3498db;
  text-decoration: none;
}
/* 匹配 href 属性值为 "https://example.com" 的元素 */
[a='https://example.com'] {
  font-weight: bold;
}
/* 匹配 href 属性值以 "https" 开头的元素 */
[a^='https'] {
  color: #27ae60;
}
/* 匹配 href 属性值以 ".com" 结尾的元素 */
[a$='.com'] {
  font-style: italic;
}
/* 匹配 href 属性值包含 "example" 的元素 */
[a*='example'] {
  text-decoration: underline;
}
/* 匹配 class 属性值包含 "button" 的元素 */
[class~='button'] {
  padding: 10px;
}
/* 匹配 lang 属性值为 "en" 或以 "en-" 开头的元素 */
[lang|='en'] {
  font-family: Arial, sans-serif;
}
```

**使用场景**：

- 为具有特定属性的元素应用样式
- 为具有特定属性值的元素应用样式
- 表单元素的样式化

## 2. 组合选择器

组合选择器用于选择具有特定关系的元素。

### 2.1 后代选择器

后代选择器 (` `) 匹配指定元素的所有后代元素：

```css
/* 匹配 .container 内的所有 <p> 元素 */
.container p {
  margin-bottom: 10px;
}
/* 匹配 .nav 内的所有 <a> 元素 */
.nav a {
  color: #333;
  text-decoration: none;
}
/* 多层后代选择 */
.header .nav .menu-item {
  display: inline-block;
  margin-right: 20px;
}
```

**使用场景**：

- 为特定容器内的元素应用样式
- 实现嵌套样式

### 2.2 子代选择器

子代选择器 (`>`) 匹配指定元素的直接子元素：

```css
/* 匹配 .container 的直接子元素 <div> */
.container > div {
  padding: 20px;
  border: 1px solid #ddd;
}
/* 匹配 .nav 的直接子元素 <ul> */
.nav > ul {
  list-style: none;
  padding: 0;
}
/* 匹配 .menu 的直接子元素 <li> */
.menu > li {
  display: inline-block;
}
```

**使用场景**：

- 为元素的直接子元素应用样式
- 避免样式影响深层嵌套的元素

### 2.3 相邻兄弟选择器

相邻兄弟选择器 (`+`) 匹配紧跟在指定元素后的第一个兄弟元素：

```css
/* 匹配紧跟在 <h1> 后的第一个 <p> 元素 */
h1 + p {
  font-size: 18px;
  color: #666;
}
/* 匹配紧跟在 .button 后的第一个 .message 元素 */
.button + .message {
  margin-top: 10px;
  padding: 10px;
  background-color: #f0f0f0;
}
```

**使用场景**：

- 为特定元素后的第一个兄弟元素应用样式
- 创建元素间的特定间距或样式关系

### 2.4 通用兄弟选择器

通用兄弟选择器 (`~`) 匹配指定元素后的所有兄弟元素：

```css
/* 匹配 <h1> 后的所有 <p> 元素 */
h1 ~ p {
  margin-left: 20px;
}
/* 匹配 .active 后的所有 .item 元素 */
.active ~ .item {
  opacity: 0.7;
}
```

**使用场景**：

- 为特定元素后的所有兄弟元素应用样式
- 创建元素组的样式关系

## 3. 伪类选择器

伪类选择器用于选择处于特定状态或位置的元素。

### 3.1 状态伪类

状态伪类匹配元素的特定状态：

```css
/* 链接未访问状态 */
a:link {
  color: #3498db;
}
/* 链接已访问状态 */
a:visited {
  color: #9b59b6;
}
/* 鼠标悬停状态 */
a:hover {
  color: #e74c3c;
  text-decoration: underline;
}
/* 元素激活状态 */
a:active {
  color: #c0392b;
}
/* 元素获得焦点状态 */
input:focus {
  outline: 2px solid #3498db;
  border-color: #3498db;
}
/* 元素禁用状态 */
button:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}
/* 元素启用状态 */
button:enabled {
  background-color: #3498db;
  cursor: pointer;
}
/* 元素checked状态 */
input:checked {
  accent-color: #3498db;
}
```

**使用场景**：

- 为链接的不同状态应用样式
- 为表单元素的不同状态应用样式
- 为元素的交互状态应用样式

### 3.2 结构伪类

结构伪类匹配元素在文档结构中的特定位置：

```css
 /* 匹配第一个子元素 */
 .container > :first-child {
  margin-top: 0;
 }
 /* 匹配最后一个子元素 */
 .container > :last-child {
  margin-bottom: 0;
 }
 /* 匹配第 n 个子元素 */
 .list > li:nth-child(2) {
  background-color: #f0f0f0;
 }
 /* 匹配偶数位置的子元素 */
 .list > li:nth-child(even) {
  background-color: #f9f9f9;
 }
 /* 匹配奇数位置的子元素 */
 .list > li:nth-child(odd) {
  background-color: #ffffff;
 }
 /* 匹配 3 的倍数位置的子元素 */
 .list > li:nth-child(3n) {
  border-bottom: 2px solid #ddd;
 }
 /* 匹配倒数第 n 个子元素 */
 .list > li:nth-last-child(2) {
  font-weight: bold;
 }
 /* 匹配第一个特定类型的子元素 */
 .container > p:first-of-type {
  font-size: 18px;
 }
 /* 匹配最后一个特定类型的子元素 */
 .container > p:last-of-type {
  margin-bottom: 0;
 }
 /* 匹配第 n 个特定类型的子元素 */
 .container > p:nth-of-type(2) {
  color: #666;
 }
 /* 匹配唯一的子元素 */
 .container > :only-child {
  width: 100%;
 }
 /* 匹配唯一的特定类型的子元素 */
 .container > p:only-of-type {
  font-style: italic;
 }
 /* 匹配空元素 */
 .element:empty {
  display: none;
 }
 /* 匹配根元素 */
 :root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
 }
 /* 排除特定元素 */
 .list > li:not(.special) {
  color: #666;
 }
 /* 排除多个元素 */
 .container > *:not(p):not(div) {
  margin: 10px 0;
 }
```

**使用场景**：

- 为列表的奇偶项应用不同样式
- 为特定位置的元素应用样式
- 排除特定元素
- 为根元素定义全局变量

### 3.3 表单伪类

表单伪类匹配表单元素的特定状态：

```css
/* 匹配必填表单元素 */
input:required {
  border: 1px solid #e74c3c;
}
/* 匹配可选表单元素 */
input:optional {
  border: 1px solid #bdc3c7;
}
/* 匹配有效的表单元素 */
input:valid {
  border: 1px solid #27ae60;
}
/* 匹配无效的表单元素 */
input:invalid {
  border: 1px solid #e74c3c;
}
/* 匹配输入范围的最小值 */
input[type='range']:min {
  background-color: #e74c3c;
}
/* 匹配输入范围的最大值 */
input[type='range']:max {
  background-color: #27ae60;
}
/* 匹配输入范围的中间值 */
input[type='range']:in-range {
  background-color: #3498db;
}
/* 匹配输入范围的超出值 */
input[type='range']:out-of-range {
  background-color: #e74c3c;
}
/* 匹配只读表单元素 */
input:read-only {
  background-color: #f5f5f5;
  cursor: not-allowed;
}
/* 匹配可读写表单元素 */
input:read-write {
  background-color: white;
}
```

**使用场景**：

- 为表单元素的不同状态应用样式
- 提供视觉反馈，指示表单元素的有效性

### 3.4 其他伪类

```css
 /* 匹配当前激活的元素 */
 :active {
  background-color: #f0f8ff;
  padding: 10px;
  border-radius: 4px;
 }
 /* 匹配语言为英语的元素 */
 :lang(en) {
  font-family: Arial, sans-serif;
 }
 /* 匹配语言为中文的元素 */
 :lang(zh) {
  font-family: "SimSun", serif;
 }
 /* 匹配包含指定子元素的元素 */
 div:has(.keyword) {
  background-color: yellow;
 }
 /* 匹配具有指定父元素的元素 */
 .parent > .child:has(> .grandchild) {
  border: 1px solid #ddd;
 }
```

**使用场景**：

- 为当前激活的锚点目标应用样式
- 为不同语言的元素应用不同样式
- 为包含特定文本的元素应用样式
- 为具有特定子元素的元素应用样式

### 3.5 现代伪类浏览器支持速查

| 伪类 | 作用 | 优先级规则 | 基线支持 |
| --- | --- | --- | --- |
| `:is()` | 选择参数列表中任一选择器命中的元素 | 取参数列表最高权重 | 2021 年广泛可用 |
| `:where()` | 同上，但专门用于“零优先级” | 恒为 0 | 2021 年广泛可用 |
| `:has()` | 选择包含指定后代/兄弟关系的元素 | 取参数列表最高权重 | 2023 年广泛可用 |

**讲解：** `:is()` 与 `:has()` 的优先级按“参数中最具体的选择器”计算，`:where()` 优先级恒为 0，适合写可被业务覆盖的默认样式。三者均可用 `@supports selector(:has(*))` 做能力检测，兼容细节以 MDN Baseline 为准。

## 4. 伪元素选择器

伪元素选择器用于选择元素的特定部分。

### 4.1 `::before` 和 `::after`

`::before` 和 `::after` 用于在元素内容前后插入装饰性内容：

```css
/* 在元素前插入内容 */
.button::before {
  content: '→';
  margin-right: 5px;
}
/* 在元素后插入内容 */
.button::after {
  content: '←';
  margin-left: 5px;
}
/* 使用伪元素创建清除浮动 */
.clearfix::after {
  content: '';
  display: table;
  clear: both;
}
/* 使用伪元素创建箭头 */
.arrow::after {
  content: '';
  border-width: 10px;
  border-style: solid;
  border-color: transparent transparent transparent #333;
  position: absolute;
  right: -20px;
  top: 50%;
  transform: translateY(-50%);
}
/* 使用伪元素创建自定义列表标记 */
.custom-list li::before {
  content: '•';
  color: #3498db;
  font-size: 18px;
  margin-right: 10px;
}
```

**使用场景**：

- 添加装饰性内容
- 创建自定义图标和箭头
- 清除浮动
- 创建自定义列表标记

### 4.2 `::first-letter` 和 `::first-line`

`::first-letter` 和 `::first-line` 用于选择元素的首字母和首行：

```css
/* 选择首字母 */
.article p::first-letter {
  font-size: 2em;
  font-weight: bold;
  color: #3498db;
  float: left;
  margin-right: 10px;
}
/* 选择首行 */
.article p::first-line {
  font-weight: bold;
  color: #2c3e50;
}
```

**使用场景**：

- 创建首字母大写效果
- 为段落首行应用特殊样式

### 4.3 `::selection`

`::selection` 用于选择用户选中的文本：

```css
 /* 为选中的文本应用样式 */
 ::selection {
  background-color: #3498db;
  color: white;
 }
 /* 为特定元素内选中的文本应用样式 */
 .article ::selection {
  background-color: #2ecc71;
  color: white;
 }
```

**使用场景**：

- 为用户选中的文本提供视觉反馈
- 增强用户体验

### 4.4 `::placeholder`

`::placeholder` 用于选择表单元素的占位符文本：

```css
/* 为占位符文本应用样式 */
input::placeholder {
  color: #95a5a6;
  font-style: italic;
}
/* 为特定类型的输入框占位符应用样式 */
input[type='email']::placeholder {
  color: #e74c3c;
}
```

**使用场景**：

- 为表单占位符文本应用样式
- 提高表单的可读性

### 4.5 其他伪元素

```css
/* 选择进度条的填充部分 */
progress::progress-bar {
  background-color: #3498db;
}
/* 选择进度条的轨道部分 */
progress::progress-value {
  background-color: #2ecc71;
}
/* 选择滑动条的拇指 */
input[type='range']::thumb {
  background-color: #3498db;
  border: none;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  cursor: pointer;
}
/* 选择滑动条的轨道 */
input[type='range']::track {
  background-color: #bdc3c7;
  height: 4px;
  border-radius: 2px;
}
```

**使用场景**：

- 为表单控件的特定部分应用样式
- 创建自定义表单控件

## 5. 选择器优先级

选择器优先级决定了多个样式规则应用时的顺序。

### 5.1 优先级计算规则

选择器的优先级由以下因素决定，按从高到低的顺序：

1. **!important** 声明（最高优先级）
2. 行内样式（权重：1000）
3. ID 选择器（权重：100）
4. 类选择器、伪类选择器、属性选择器（权重：10）
5. 元素选择器、伪元素选择器（权重：1）
6. 通配符选择器、后代选择器、相邻兄弟选择器（权重：0）

### 5.2 优先级示例

```css
/* 权重：1 (元素选择器) */
div {
  color: blue;
}
/* 权重：10 (类选择器) */
.container {
  color: red;
}
/* 权重：100 (ID 选择器) */
#main {
  color: green;
}
/* 权重：101 (ID 选择器 + 元素选择器) */
#main div {
  color: purple;
}
/* 权重：20 (两个类选择器) */
.container .box {
  color: orange;
}
/* 行内样式：权重 1000 */
/* <div style="color: black;"> */
/* !important：最高优先级 */
div {
  color: yellow !important;
}
```

**使用场景**：

- 理解样式覆盖的规则
- 避免样式冲突
- 合理组织样式代码

### 5.3 优先级计算练习

下面 6 题覆盖“权重 + 顺序 + 例外”三种情况，先心算答案，再用 DevTools 验证：

1. `div p` 与 `.intro` 同时命中一个 `<p class="intro">`，谁赢？（类赢：10 > 2）
2. `#main .box` 与 `.container .item p`，谁赢？（ID 组合赢：110 > 21）
3. 两条完全相同的 `p { color: red }` 与 `p { color: blue }`，谁赢？（后写 blue）
4. `<p style="color: black">` 与 `#main p { color: red }`，谁赢？（行内样式赢）
5. `.box { color: green !important }` 与行内样式，谁赢？（!important 赢）
6. `.a.b` 与 `.c`，谁赢？（`.a.b` 权重 20 赢）

**讲解：** 前两题练“权重累加”，中间两题练“顺序与行内例外”，最后两题练“数量叠加与 !important”。全部答对即可进入 `css/009-PriorityCalculation` 的四元组精确计算。

## 6. 选择器性能

选择器的性能影响页面的渲染速度，应注意优化。

### 6.1 性能影响因素

- **选择器复杂度**：复杂的选择器需要更多的计算时间
- **选择器特异性**：更具体的选择器性能更好
- **选择器匹配顺序**：CSS 选择器从右到左匹配

### 6.2 性能优化建议

```css
 /* 不良实践：复杂的后代选择器 */
 .header .nav .menu .menu-item .link {
  color: #333;
 }
 /* 良好实践：简单的类选择器 */
 .menu-link {
  color: #333;
 }
 /* 不良实践：使用通配符选择器 */
 * {
  margin: 0;
  padding: 0;
 }
 /* 良好实践：针对性选择 */
 body, html, div, p, h1, h2, h3, h4, h5, h6, ul, ol, li {
  margin: 0;
  padding: 0;
 }
 /* 不良实践：使用属性选择器进行复杂匹配 */
 input[type="text"][class~="form-control"] {
  border: 1px solid #ddd;
 }
 /* 良好实践：使用类选择器 */
 .form-control {
  border: 1px solid #ddd;
 }
```

**性能优化技巧**：

- 尽量使用简单的选择器
- 避免过度使用后代选择器
- 避免使用通配符选择器
- 合理使用类选择器
- 避免使用复杂的属性选择器

## 7. 最佳实践

### 7.1 命名规范

推荐使用 BEM (Block, Element, Modifier) 命名规范：

```css
/* Block */
.button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
/* Element */
.button__icon {
  margin-right: 8px;
  font-size: 16px;
}
/* Modifier */
.button--primary {
  background-color: #3498db;
  color: white;
}
.button--secondary {
  background-color: #95a5a6;
  color: white;
}
.button--large {
  padding: 12px 24px;
  font-size: 16px;
}
.button--small {
  padding: 8px 16px;
  font-size: 14px;
}
```

**BEM 命名规则**：

- Block：独立的、可重用的组件
- Element：Block 的一部分，不能独立存在
- Modifier：修改 Block 或 Element 的样式

### 7.2 代码组织

- **按功能组织**：将相关的样式放在一起
- **使用注释**：为不同的部分添加注释
- **模块化**：将样式按模块分离

```css
 /* 重置样式 */
 * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
 }
 /* 全局变量 */
 :root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --text-color: #333;
  --background-color: #f8f9fa;
 }
 /* 布局样式 */
 .container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
 }
 /* 组件样式 */
 .button {
  /* 按钮样式 */
 }
 .card {
  /* 卡片样式 */
 }
 /* 响应式样式 */
 @media (max-width: 768px) {
  .container {
  padding: 0 10px;
  }
  .button {
  padding: 8px 16px;
  }
 }
```

### 7.3 可读性

- **缩进**：使用一致的缩进
- **空格**：在选择器和大括号之间添加空格
- **换行**：每个属性占一行
- **注释**：为复杂的样式添加注释

```css
/* 良好的可读性 */
.header {
  background-color: #f8f9fa;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.header__logo {
  font-size: 24px;
  font-weight: bold;
  color: var(--primary-color);
}
.header__nav {
  display: flex;
  gap: 20px;
}
/* 不良的可读性 */
.header {
  background-color: #f8f9fa;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.header__logo {
  font-size: 24px;
  font-weight: bold;
  color: var(--primary-color);
}
.header__nav {
  display: flex;
  gap: 20px;
}
```

## 8. 实际应用示例

### 8.1 示例 1：导航菜单

```html
<nav class="nav">
  <ul class="nav__list">
    <li class="nav__item"><a href="#" class="nav__link">首页</a></li>
    <li class="nav__item"><a href="#" class="nav__link">关于我们</a></li>
    <li class="nav__item"><a href="#" class="nav__link">产品</a></li>
    <li class="nav__item"><a href="#" class="nav__link">联系我们</a></li>
  </ul>
</nav>
```

```css
.nav {
  background-color: #333;
  padding: 10px 0;
}
.nav__list {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 20px;
}
.nav__item {
  position: relative;
}
.nav__link {
  color: white;
  text-decoration: none;
  padding: 10px 15px;
  display: block;
  transition: color 0.3s ease;
}
.nav__link:hover {
  color: #3498db;
}
/* 为第一个和最后一个链接添加特殊样式 */
.nav__item:first-child .nav__link {
  font-weight: bold;
}
.nav__item:last-child .nav__link {
  background-color: #3498db;
  border-radius: 4px;
}
/* 为激活的链接添加样式 */
.nav__link.active {
  color: #3498db;
  border-bottom: 2px solid #3498db;
}
```

### 8.2 示例 2：表单样式

```html
<form class="form">
  <div class="form__group">
    <label for="name" class="form__label">姓名</label>
    <input type="text" id="name" class="form__input" required />
  </div>
  <div class="form__group">
    <label for="email" class="form__label">邮箱</label>
    <input type="email" id="email" class="form__input" required />
  </div>
  <div class="form__group">
    <label for="message" class="form__label">留言</label>
    <textarea id="message" class="form__textarea" required></textarea>
  </div>
  <button type="submit" class="form__button">提交</button>
</form>
```

```css
.form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
}
.form__group {
  margin-bottom: 20px;
}
.form__label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}
.form__input,
.form__textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}
.form__input:focus,
.form__textarea:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
}
.form__input:required,
.form__textarea:required {
  border-left: 3px solid #e74c3c;
}
.form__input:valid,
.form__textarea:valid {
  border-left: 3px solid #27ae60;
}
.form__button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.form__button:hover {
  background-color: #2980b9;
}
.form__button:active {
  background-color: #1f618d;
}
```

### 8.3 示例 3：卡片布局

```html
<div class="card-container">
  <div class="card">
    <div class="card__image">
      <img src="image1.jpg" alt="Card Image" />
    </div>
    <div class="card__content">
      <h3 class="card__title">卡片标题 1</h3>
      <p class="card__text">这是卡片内容，描述卡片的详细信息。</p>
      <a href="#" class="card__link">查看详情</a>
    </div>
  </div>
  <div class="card">
    <div class="card__image">
      <img src="image2.jpg" alt="Card Image" />
    </div>
    <div class="card__content">
      <h3 class="card__title">卡片标题 2</h3>
      <p class="card__text">这是卡片内容，描述卡片的详细信息。</p>
      <a href="#" class="card__link">查看详情</a>
    </div>
  </div>
  <div class="card">
    <div class="card__image">
      <img src="image3.jpg" alt="Card Image" />
    </div>
    <div class="card__content">
      <h3 class="card__title">卡片标题 3</h3>
      <p class="card__text">这是卡片内容，描述卡片的详细信息。</p>
      <a href="#" class="card__link">查看详情</a>
    </div>
  </div>
</div>
```

```css
.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}
.card {
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}
.card__image {
  height: 200px;
  overflow: hidden;
}
.card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}
.card:hover .card__image img {
  transform: scale(1.05);
}
.card__content {
  padding: 20px;
}
.card__title {
  margin-bottom: 10px;
  font-size: 20px;
  color: #333;
}
.card__text {
  margin-bottom: 15px;
  color: #666;
  line-height: 1.5;
}
.card__link {
  display: inline-block;
  color: #3498db;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease;
}
.card__link:hover {
  color: #2980b9;
  text-decoration: underline;
}
/* 为第一个卡片添加特殊样式 */
.card:first-child {
  border: 2px solid #3498db;
}
/* 为最后一个卡片添加特殊样式 */
.card:last-child {
  background-color: #f8f9fa;
}
```

## 9. 总结

CSS 选择器系统是 CSS 的核心组成部分，提供了强大的元素选择能力：

- **基础选择器**：通配符、标签、类、ID 和属性选择器，用于选择基本元素。
- **组合选择器**：后代、子代、相邻兄弟和通用兄弟选择器，用于选择具有特定关系的元素。
- **伪类选择器**：状态、结构、表单等伪类，用于选择处于特定状态或位置的元素。
- **伪元素选择器**：`::before`、`::after`、`::first-letter` 等，用于选择元素的特定部分。
- **选择器优先级**：基于权重计算，决定样式的应用顺序。
- **选择器性能**：合理使用选择器，优化页面渲染速度。
- **最佳实践**：使用 BEM 命名规范，组织代码结构，提高可读性。
  通过掌握 CSS 选择器系统，开发者可以更加灵活地控制页面样式，创建美观、响应式的网页设计。选择器的合理使用不仅可以提高代码的可维护性，还可以优化页面的性能。

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

## 动手试试

### 入门版（必做）

1. 用标签、类、ID 三种选择器分别给同一个元素设置不同颜色，观察优先级；
2. 用后代选择器 `.nav a` 给导航链接去下划线；
3. 用 `:hover` 给按钮加悬停背景色。

### 进阶版（选做）

1. 用 `:nth-child(odd)` 实现表格隔行变色；
2. 用 `::before` 给列表项加箭头标记；
3. 用 `:focus-visible` 给键盘焦点加可见描边。

## 核心知识点

> 一句话记住选择器：标签点名、类分群、ID 唯一；后代空格、子代 `>`、兄弟 `+`/`~`；伪类看状态，伪元素造内容。

- 基础：`*`、标签、`.class`、`#id`、属性选择器；
- 组合：后代（空格）、子代（`>`）、相邻（`+`）、通用兄弟（`~`）；
- 伪类：`:hover`/`:focus` 状态类，`:nth-child`/`:not` 结构类；
- 伪元素：`::before`/`::after` 必须有 `content`；
- 优先级：ID > 类 > 标签，行内更高，`!important` 最高；
- 性能：避免 `*` 通配与过深的后代选择器。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 滥用 `*` | 匹配开销大 | 用具体选择器或类 |
| 深后代链 | 渲染匹配慢、难维护 | 用类名扁平化（BEM） |
| 依赖 `!important` | 破坏层叠 | 检查权重与命名 |
| 忘记 `content` | 伪元素不显示 | 写 `content: ''` |
| 用 `:hover` 做移动端交互 | 触屏无悬停 | 用 `:focus`/媒体查询 |
| 移除 `:focus-visible` 样式 | 键盘用户迷失 | 保留可见焦点 |

## 扩展学习

- 优先级计算：`css/009-PriorityCalculation`；
- 伪类/伪元素详解：`css/023-PseudoClassPseudoElement`；
- BEM 命名：`css/057-BEMNamingMethodology`；
- 嵌套规范：`css/041-CSSNativeNesting`、`css/071-CSSNesting`；
- 现代选择器：`:has()` 与容器查询 `css/032-ContainerQuery`。

<!-- ============ 文档分隔线：007-css/008-CSSResetAndNormalize.md ============ -->

## 0. 直觉：浏览器给 HTML 元素“预装了默认样式”

`h1` 为什么比 `p` 大？`ul` 为什么有缩进？按钮为什么有边框？因为浏览器内置了用户代理样式（user agent stylesheet）。问题是各家默认样式不完全一致，所以项目开头通常要“清场”或“统一”，这就是 CSS 重置。

## 1. 为什么需要重置

```css
/* 没有重置时，不同浏览器对同一元素可能有细微差异 */
/* 例如 button 的默认 padding、字体、背景在不同浏览器不同 */
```

**讲解：** 重置解决两类问题：一是跨浏览器差异，二是默认样式（如 `h1` 外边距）干扰设计系统。但“全部清零”会丢掉有用的语义默认值，所以现代方案从“清空”走向“统一基线”。

## 2. 经典 reset：全部归零

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

**讲解：** 经典 reset 简单粗暴，把常见默认值清零。缺点是 `*` 选择器性能与继承语义欠佳，而且把所有 `h1`-`h6` 都抹成一样大小后，需要自己重建层级。

## 3. normalize.css：保留有用默认值

normalize.css 的思路不是清空，而是“把各浏览器默认样式拉齐”：

```css
/* 示例（normalize.css 片段风格） */
html {
  line-height: 1.15;            /* 统一行高 */
  -webkit-text-size-adjust: 100%; /* 禁止横屏自动放大字号 */
}
body {
  margin: 0;
}
```

**讲解：** normalize 保留 `h1` 层级、列表缩进等语义默认值，只修差异。适合“希望浏览器默认值作为设计起点”的项目；代价是文件里有些规则你可能永远用不到。

## 4. 现代重置：兼顾基线与语义

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: system-ui, "PingFang SC", "Microsoft YaHei", sans-serif;
  line-height: 1.5;
  color: #333;
  -webkit-font-smoothing: antialiased;
}

img,
picture,
video {
  display: block;
  max-width: 100%;
}

button,
input,
textarea,
select {
  font: inherit;   /* 表单控件跟随页面字体 */
}

ul[role="list"],
ol[role="list"] {
  list-style: none;
}
```

**讲解：** 现代重置（如 Andy Bell 的现代 CSS Reset 思路）只做四件事：统一盒模型、去掉 body 外边距、媒体元素自适应、表单继承字体。保留标题层级与列表语义，配合 `role` 控制无标记列表。

## 5. 三种方案如何选

| 方案 | 思路 | 适用场景 |
| --- | --- | --- |
| 经典 reset | 全部清零 | 从零搭建、默认值不想要 |
| normalize.css | 拉齐差异 | 依赖浏览器默认语义 |
| 现代重置 | 最小统一 | 设计系统/组件库首选 |

**讲解：** 现代项目推荐“现代重置 + 设计令牌（CSS 变量）”，框架项目（Tailwind 等）自带预置，通常不需要再引 normalize。工程化细节见 `css/043-CSSArchitectureMethodology`。

## 6. 动手试试

1. 不写任何 CSS，对比 Chrome 与 Edge（或手机浏览器）中同一页面的默认间距差异；
2. 分别应用经典 reset 与现代重置，对比 `h1` 大小、列表缩进、按钮字体的变化；
3. 给 `<img>` 加 `display: block; max-width: 100%`，观察图片底部间隙消失；
4. 进阶挑战：为你的项目写一份 20 行以内的“现代重置”，并注释每行的目的。

## 7. 核心知识点

> 一句话记住重置方案：reset 全清零，normalize 拉齐差异，现代重置只统一基线；盒模型统一 + 媒体自适应 + 表单继承字体是底线。

- 浏览器默认样式是用户代理样式，优先级最低；
- 经典 reset：`* { margin: 0; padding: 0 }`，简单但粗暴；
- normalize.css：保留语义默认值，只修差异；
- 现代重置：统一盒模型、图片块级化、表单继承字体；
- `box-sizing: border-box` 全局统一是重置的核心项；
- 框架项目自带预置，不必重复引入。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 重置后又把默认值写回来 | 重复劳动 | 先列设计基线，再决定重置范围 |
| `* { margin:0 }` 破坏间距语义 | 所有元素都需重设间距 | 用现代重置 + 间距令牌 |
| 引入 normalize 又手写 reset | 规则冲突难排查 | 二选一，推荐现代重置 |
| 重置文件放最后 | 覆盖自己的业务样式 | 重置必须放最前，未分层时会被业务覆盖 |

## 9. 扩展学习

- 盒模型与 box-sizing：`css/003-CSS3BoxModelDetailed`；
- 继承与层叠：`css/010-CascadeInheritanceBasics`；
- 层叠层 @layer（重置入层）：`css/039-CascadeLayer`；
- 架构方法论：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/009-PriorityCalculation.md ============ -->

> 0基础速通：读第 0 节直觉、第 1 节核心必读（代码示例）与第 7 节综合挑战即可；第 2-5 章按需查阅，第 6 章深入理解（选读）供进阶。

> 初学者必须记住的 3 条规则：
>
> 1. 选择器越具体优先级越高：ID > 类 > 标签；
> 2. 权重相同时，后写的规则赢；
> 3. `!important` 与行内样式是“掀桌子”的例外，日常尽量不用。

# 优先级计算（Specificity & Cascade）

> 本文以 W3C [CSS Cascading and Inheritance Level 4](https://www.w3.org/TR/css-cascade-4/)、[Selectors Level 4](https://www.w3.org/TR/selectors-4/) 规范为基础，系统阐释 CSS 优先级（Specificity）的计算算法、层叠顺序（Cascade Order）、`!important` 与 `@layer` 的工程意义、`:where()` / `:is()` / `:has()` 等现代选择器对优先级的影响，并对接 Bootstrap、Tailwind CSS、Material Design 等主流框架的实践范式。内容涵盖从 CSS 1 到 CSS Cascade Level 4 的演进，提供生产级代码示例与工程化解决方案。

---

## 0. 直觉：谁更“具体”，谁说了算

两个选择器同时命中同一个元素，浏览器听谁的？规则可以概括为一句话：**选择器越具体，优先级越高；同样具体时，后写的赢**。

具体程度按“ID > 类 > 标签”排序：`#main` 比 `.card` 具体，`.card` 比 `div` 具体。`!important` 是“掀桌子”的例外，`@layer` 和 `:where()` 则是现代 CSS 用来“重新排座次”的工具。

## 1. 核心必读：代码示例
### 1.1 基础示例：四元组计算

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>优先级四元组计算示例</title>
<style>
  /* (0, 0, 0, 1) - 元素选择器 */
  p {
    color: gray;
  }

  /* (0, 0, 1, 0) - 类选择器 */
  .text {
    color: blue;
  }

  /* (0, 0, 1, 1) - 类 + 元素 */
  .text p {
    color: green;
  }

  /* (0, 1, 0, 0) - ID 选择器 */
  #main {
    color: orange;
  }

  /* (0, 1, 0, 1) - ID + 元素 */
  #main p {
    color: red;
  }

  /* (0, 1, 1, 1) - ID + 类 + 元素 */
  #main .text p {
    color: purple;
  }

  /* (1, 0, 0, 0) - 内联样式（最高，除 !important） */
</style>
</head>
<body>
  <div id="main">
    <p class="text" style="color: black;">
      最终颜色：black（内联样式胜出）
    </p>
    <p class="text">
      最终颜色：purple（(0,1,1,1) 胜出）
    </p>
    <p>
      最终颜色：red（(0,1,0,1) 胜出）
    </p>
  </div>
</body>
</html>
```

**讲解：** 四元组 `(内联, ID, 类, 元素)` 从左到右比较，第一个不同的数字决定胜负：`#main .text p` 是 (0,1,1,1)，胜过 (0,0,1,0)；内联样式是 (1,0,0,0)，除 `!important` 外最高。

### 1.2 `!important` 与来源排序

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>!important 与来源排序</title>
<style>
  /* Author Normal */
  .box {
    color: black;
  }

  /* Author !important */
  .box {
    color: blue !important;
  }

  /* 内联样式（HTML 中）< 内联 !important */
</style>
</head>
<body>
  <div class="box" style="color: red;">
    颜色：blue（Author !important 覆盖内联 normal）
  </div>
  <div class="box" style="color: red !important;">
    颜色：red（内联 !important 胜出）
  </div>
</body>
</html>
```

### 1.3 `:where()` 与 `:is()` 对比

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>:where() 与 :is() 优先级对比</title>
<style>
  /* 第三方库样式（模拟） */
  .card .title {
    color: blue;  /* (0,0,2,0) */
  }

  /* 业务重置：使用 :is() */
  :is(.card .title) {
    color: red;  /* (0,0,2,0) - 与上方相同，按出现顺序，红色胜出 */
  }

  /* 业务重置：使用 :where() */
  :where(.card .title) {
    color: green;  /* (0,0,0,0) - 低于 (0,0,2,0)，蓝色胜出 */
  }
</style>
</head>
<body>
  <div class="card">
    <h3 class="title">颜色：red（:is() 胜出）</h3>
  </div>
</body>
</html>
```

**讲解：** `:is()` 的优先级取参数列表中的最高者（示例中与 `.card .title` 相同，后写胜出）；`:where()` 优先级恒为 0，适合“可被业务规则随时覆盖”的默认样式。

### 1.4 `@layer` 分层管理

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>@layer 分层管理示例</title>
<style>
  /* 声明层顺序：reset < framework < components < utilities */
  @layer reset, framework, components, utilities;

  /* reset 层：最低优先级 */
  @layer reset {
    h1 { margin: 0; padding: 0; }
    p { margin: 0; }
  }

  /* framework 层：框架样式 */
  @layer framework {
    .container { max-width: 1200px; margin: 0 auto; }
    .btn { padding: 8px 16px; border: 1px solid #ccc; }
  }

  /* components 层：组件样式 */
  @layer components {
    .card { padding: 16px; border-radius: 8px; }
    .btn-primary { background: blue; color: white; }
  }

  /* utilities 层：工具类（最高分层优先级） */
  @layer utilities {
    .text-center { text-align: center; }
    .mt-4 { margin-top: 1rem; }
  }

  /* 未分层样式：最高优先级（覆盖所有分层） */
  .card {
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
</style>
</head>
<body>
  <div class="container">
    <h1 class="text-center">标题</h1>
    <div class="card mt-4">
      <p>卡片内容</p>
      <button class="btn btn-primary">按钮</button>
    </div>
  </div>
</body>
</html>
```

### 1.5 `:has()` 父选择器

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>:has() 父选择器示例</title>
<style>
  /* 基础卡片样式 */
  .card {
    padding: 16px;
    border: 1px solid #ddd;
    border-radius: 8px;
  }

  /* 当卡片内含图片时，去除内边距 */
  .card:has(> img) {
    padding: 0;
    overflow: hidden;
  }

  /* 当卡片内含错误图标时，添加红色边框 */
  .card:has(.icon-error) {
    border-color: #dc3545;
    background: #fff5f5;
  }

  /* 当卡片内既有标题又有图片时，应用特殊布局 */
  .card:has(h3):has(img) {
    display: flex;
    flex-direction: column;
  }

  /* :has() 的优先级由参数中最具体者决定 */
  /* .card:has(#special-img) 优先级为 (0,1,1,0) */
  .card:has(#special-img) {
    border-color: gold;
  }
</style>
</head>
<body>
  <div class="card">
    <h3>普通卡片</h3>
    <p>无图片，保留内边距</p>
  </div>

  <div class="card">
    <img src="example.jpg" alt="示例" style="width: 100%;">
    <p>含图片，去除内边距</p>
  </div>

  <div class="card">
    <span class="icon-error">!</span>
    <p>错误卡片，红色边框</p>
  </div>
</body>
</html>
```

### 1.6 `:not()` 的优先级

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>:not() 优先级示例</title>
<style>
  /* :not() 本身不计入优先级，参数计 */
  /* :not(.disabled) 优先级为 (0,0,1,0) */
  button:not(.disabled) {
    cursor: pointer;
  }

  /* :not(.disabled, .readonly) 优先级为参数中最具体者 */
  /* .disabled (0,0,1,0) vs .readonly (0,0,1,0) → (0,0,1,0) */
  input:not(.disabled, .readonly) {
    background: white;
  }

  /* 复杂参数：:not(#special) 优先级为 (0,1,0,0) */
  .item:not(#special) {
    opacity: 0.6;
  }
</style>
</head>
<body>
  <button>可点击按钮</button>
  <button class="disabled">禁用按钮</button>
  <input type="text" value="可编辑">
  <input type="text" class="readonly" value="只读">
  <div class="item">普通项</div>
  <div class="item" id="special">特殊项</div>
</body>
</html>
```

### 1.7 企业级：设计系统分层架构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>企业级设计系统分层架构</title>
<style>
  /* 设计系统分层声明 */
  @layer tokens, reset, vendor, components, utilities, overrides;

  /* Layer 1: Design Tokens（设计令牌） */
  @layer tokens {
    :root {
      --color-primary: #007bff;
      --color-danger: #dc3545;
      --color-text: #212529;
      --color-bg: #ffffff;
      --spacing-1: 0.25rem;
      --spacing-2: 0.5rem;
      --spacing-3: 1rem;
      --radius-md: 6px;
    }
  }

  /* Layer 2: Reset（重置） */
  @layer reset {
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: system-ui, -apple-system, sans-serif;
      color: var(--color-text);
      background: var(--color-bg);
      line-height: 1.5;
    }
  }

  /* Layer 3: Vendor（第三方库样式） */
  @layer vendor {
    /* 假设此处为 Bootstrap / Tailwind 等第三方库样式 */
    .vendor-btn {
      padding: 8px 16px;
      border: 1px solid #ccc;
      background: white;
    }
  }

  /* Layer 4: Components（组件库） */
  @layer components {
    .btn {
      display: inline-flex;
      align-items: center;
      padding: var(--spacing-2) var(--spacing-3);
      border-radius: var(--radius-md);
      border: none;
      cursor: pointer;
      font-size: 0.875rem;
      transition: background 0.2s;
    }
    .btn-primary {
      background: var(--color-primary);
      color: white;
    }
    .btn-danger {
      background: var(--color-danger);
      color: white;
    }
  }

  /* Layer 5: Utilities（工具类） */
  @layer utilities {
    .mt-2 { margin-top: var(--spacing-2); }
    .mt-3 { margin-top: var(--spacing-3); }
    .text-center { text-align: center; }
    .flex { display: flex; }
    .gap-2 { gap: var(--spacing-2); }
  }

  /* Layer 6: Overrides（业务覆盖） */
  @layer overrides {
    /* 业务特定的样式覆盖 */
    .checkout-btn {
      background: linear-gradient(135deg, #667eea, #764ba2);
    }
  }
</style>
</head>
<body>
  <div class="flex gap-2 mt-3">
    <button class="btn btn-primary">主按钮</button>
    <button class="btn btn-danger">危险按钮</button>
    <button class="btn btn-primary checkout-btn">结算按钮（业务覆盖）</button>
  </div>
</body>
</html>
```

### 1.8 优先级可视化工具

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>优先级可视化工具</title>
<style>
  body {
    font-family: system-ui, sans-serif;
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
  }
  .spec-display {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    margin: 1rem 0;
  }
  .spec-cell {
    text-align: center;
    padding: 0.5rem;
    background: white;
    border-radius: 4px;
    border: 1px solid #dee2e6;
  }
  .spec-cell .label {
    font-size: 0.75rem;
    color: #6c757d;
    text-transform: uppercase;
  }
  .spec-cell .value {
    font-size: 1.5rem;
    font-weight: bold;
    color: #212529;
  }
  input {
    width: 100%;
    padding: 0.5rem;
    font-family: monospace;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
</style>
</head>
<body>
  <h1>CSS 优先级计算器</h1>
  <input type="text" id="selector" placeholder="输入选择器，如 #main .card:hover" value="#main .card:hover">
  <div class="spec-display">
    <div class="spec-cell"><div class="label">Inline</div><div class="value" id="a">0</div></div>
    <div class="spec-cell"><div class="label">ID</div><div class="value" id="b">1</div></div>
    <div class="spec-cell"><div class="label">Class</div><div class="value" id="c">1</div></div>
    <div class="spec-cell"><div class="label">Element</div><div class="value" id="d">0</div></div>
  </div>

  <script>
    // 简化的优先级计算函数（生产环境应使用 postcss-selector-parser）
    function calculateSpecificity(selector) {
      let a = 0, b = 0, c = 0, d = 0;

      // 内联样式（通过 style 属性，此处仅演示规则选择器）
      // a 永远为 0（除非通过 style 属性）

      // ID 选择器
      const ids = selector.match(/#[\w-]+/g) || [];
      b = ids.length;

      // 类选择器、属性选择器、伪类（排除 :: 伪元素）
      const classes = selector.match(/\.[\w-]+/g) || [];
      const attrs = selector.match(/\[[^\]]+\]/g) || [];
      const pseudoClasses = selector.match(/:[^:][\w-]+(\([^)]*\))?/g) || [];
      c = classes.length + attrs.length + pseudoClasses.length;

      // 元素选择器、伪元素
      const elements = selector.match(/(^|[\s>+~])[\w-]+/g) || [];
      const pseudoElements = selector.match(/::[\w-]+/g) || [];
      d = elements.length + pseudoElements.length;

      return { a, b, c, d };
    }

    document.getElementById('selector').addEventListener('input', (e) => {
      const spec = calculateSpecificity(e.target.value);
      document.getElementById('a').textContent = spec.a;
      document.getElementById('b').textContent = spec.b;
      document.getElementById('c').textContent = spec.c;
      document.getElementById('d').textContent = spec.d;
    });
  </script>
</body>
</html>
```

### 1.9 Stylelint 强制优先级规则

```javascript
// .stylelintrc.js - 企业级 Stylelint 配置
module.exports = {
  extends: ['stylelint-config-standard', 'stylelint-config-recommended'],
  plugins: ['stylelint-selector-max-specificity'],
  rules: {
    // 禁止使用 ID 选择器
    'selector-max-id': 0,
    // 限制类选择器组合数（最多 3 个）
    'selector-max-class': 3,
    // 限制复合选择器深度（最多 4 层）
    'selector-max-compound-selectors': 4,
    // 禁止 !important（除非加 ! 前缀注释）
    'declaration-no-important': true,
    // 限制优先级上限：(0, 0, 3, 0)
    'selector-max-specificity': '0,0,3,0',
    // 强制 BEM 命名
    'selector-class-pattern': '^[a-z][a-z0-9]*(?:-[a-z0-9]+)*(?:__[a-z0-9-]+)?(?:--[a-z0-9-]+)?$',
    // 禁止通配符选择器
    'selector-max-universal': 0,
    // 限制属性选择器组合
    'selector-max-attribute': 2,
  },
};
```

### 1.10 React + CSS Modules 优先级管理

```jsx
// Button.tsx - React 组件，使用 CSS Modules 隔离优先级
import styles from './Button.module.css';
import classNames from 'classnames';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

export function Button({
  variant = 'primary',
  size = 'md',
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  // 利用 CSS Modules 的局部作用域，避免全局优先级污染
  const className = classNames(
    styles.btn,
    styles[`variant-${variant}`],
    styles[`size-${size}`],
    {
      [styles.disabled]: disabled,
    }
  );

  return (
    <button
      className={className}
      disabled={disabled}
      onClick={onClick}
      aria-disabled={disabled}
    >
      {children}
    </button>
  );
}
```

```css
/* Button.module.css - CSS Modules 样式 */
/* CSS Modules 自动生成唯一类名，避免全局冲突 */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}

/* 变体样式 */
.variantPrimary {
  background: #007bff;
  color: white;
}
.variantPrimary:hover {
  background: #0056b3;
}

.variantSecondary {
  background: #6c757d;
  color: white;
}

.variantDanger {
  background: #dc3545;
  color: white;
}

/* 尺寸 */
.sizeSm { padding: 0.25rem 0.5rem; }
.sizeMd { padding: 0.5rem 1rem; }
.sizeLg { padding: 0.75rem 1.5rem; font-size: 1rem; }

/* 禁用状态 */
.disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
```

---

## 2. 对比分析
### 2.1 主流 CSS 方法论的优先级策略

| 方法论 | 核心思想 | 优先级控制 | 优势 | 劣势 |
| --- | --- | --- | --- | --- |
| **BEM** | Block-Element-Modifier 命名 | 单一类选择器 (0,0,1,0) | 简单、可预测 | 类名冗长、复用性弱 |
| **ITCSS** | Inverted Triangle CSS 分层 | 来源分层（早 < 晚） | 渐进增强 | 学习成本高 |
| **SMACSS** | Base/Layout/Module/State/Theme | 分类管理 | 结构清晰 | 缺乏强制约束 |
| **Atomic CSS** | 单一职责原子类 | 工具类 (0,0,1,0) | 高复用 | 可读性差 |
| **CSS-in-JS** | 运行时生成唯一类名 | 自动隔离 | 动态性强 | 运行时开销 |
| **CSS Modules** | 编译时生成唯一类名 | 自动隔离 | 零运行时 | 仅限组件级 |
| **@layer** | 显式层级声明 | 层级控制 | 灵活、强大 | 兼容性、心智模型 |

### 2.2 主流框架的优先级实践

| 框架 | 策略 | 典型选择器 | 优先级 |
| --- | --- | --- | --- |
| **Bootstrap 5** | 类选择器堆叠 | `.btn .btn-primary` | (0,0,2,0) |
| **Tailwind CSS v3.4** | 单一原子类 | `.text-center` | (0,0,1,0) |
| **Material Design 3** | 主题类 + 属性 | `.mdc-button--raised` | (0,0,1,0) |
| **Ant Design 5** | CSS-in-JS（CSSinJS） | 动态生成类名 | (0,0,1,0) |
| **GitHub Primer** | 工具类 + 组件类 | `.btn` `.btn-primary` | (0,0,1,0) - (0,0,2,0) |

### 2.3 Tailwind vs Bootstrap 的优先级哲学

**Tailwind CSS**（Atomic CSS 哲学）：

```html
<!-- 每个类都是原子工具，优先级恒为 (0,0,1,0) -->
<button class="bg-blue-500 text-white px-4 py-2 rounded">
  按钮
</button>
```

- 优势：优先级扁平，无覆盖冲突。
- 劣势：HTML 臃肿，需配合 `@apply` 或组件化。

**Bootstrap 5**（组件类哲学）：

```html
<!-- 组件类组合，优先级 (0,0,2,0) -->
<button class="btn btn-primary">
  按钮
</button>
```

- 优势：HTML 简洁，语义清晰。
- 劣势：覆盖时需提升优先级（如 `.my-btn.btn-primary`）。

### 2.4 `@layer` vs BEM vs CSS Modules

| 维度 | `@layer` | BEM | CSS Modules |
| --- | --- | --- | --- |
| **隔离方式** | 显式层级 | 命名约定 | 编译时哈希 |
| **优先级控制** | 精确（层间不可越级） | 粗略（单一类） | 完全隔离 |
| **浏览器支持** | Chrome 99+, Safari 15.4+, Firefox 97+ | 全部 | 全部（需构建工具） |
| **学习成本** | 高 | 低 | 中 |
| **团队协作** | 需明确层级约定 | 需命名规范 | 自动隔离 |
| **适用场景** | 大型项目、多团队 | 中小型项目 | 组件化项目 |

### 2.5 预处理器对优先级的影响

| 预处理器 | 嵌套规则 | 编译后优先级 | 备注 |
| --- | --- | --- | --- |
| **SCSS** | `.a { .b { } }` | `.a .b` (0,0,2,0) | 嵌套加深优先级 |
| **Less** | `.a { .b { } }` | `.a .b` (0,0,2,0) | 同 SCSS |
| **Stylus** | `.a .b` 或缩进 | `.a .b` (0,0,2,0) | 同上 |
| **PostCSS** | `&` 嵌套 | 同 SCSS | 取决于插件 |

> **最佳实践**：预处理器嵌套不超过 3 层，避免生成 (0,0,N,0) 的高优先级选择器。

### 2.6 现代选择器优先级对比

| 选择器 | 语法 | 优先级 | 浏览器支持 |
| --- | --- | --- | --- |
| ID | `#id` | (0,1,0,0) | 全部 |
| 类 | `.class` | (0,0,1,0) | 全部 |
| 属性 | `[attr=val]` | (0,0,1,0) | 全部 |
| 伪类 | `:hover` | (0,0,1,0) | 全部 |
| 伪元素 | `::before` | (0,0,0,1) | 全部 |
| `:is()` | `:is(.a, #b)` | 取最高 | Chrome 88+, Safari 14+, Firefox 78+ |
| `:where()` | `:where(.a, #b)` | (0,0,0,0) | Chrome 88+, Safari 14+, Firefox 78+ |
| `:not()` | `:not(.a)` | 参数最高 | Chrome 88+, Safari 14+, Firefox 78+ |
| `:has()` | `:has(> .a)` | 参数最高 | Chrome 105+, Safari 15.4+ |
| `:nth-child()` | `:nth-child(2n+1)` | (0,0,1,0) | 全部 |

---

## 3. 常见陷阱与最佳实践
### 3.1 陷阱 1：ID 选择器的优先级陷阱

**问题**：使用 ID 选择器后，覆盖样式变得困难。

```css
/* 反例：使用 ID 选择器 */
#header {
  background: blue;
}

/* 业务覆盖：需要更高优先级 */
#header.highlight {
  background: gold;
}
/* 或被迫使用 !important */
#header {
  background: gold !important;
}
```

**最佳实践**：避免使用 ID 选择器，改用类选择器。

```css
/* 正例：使用类选择器 */
.header {
  background: blue;
}
.header.highlight {
  background: gold;
}
```

### 3.2 陷阱 2：`!important` 滥用

**问题**：`!important` 滥用导致样式难以维护，形成「优先级军备竞赛」。

```css
/* 反例：!important 滥用 */
.btn { color: white !important; }
.btn-primary { color: white !important; }
.btn-danger { color: red !important; }
/* 覆盖时需要更具体的 !important */
.btn.btn-danger.special { color: darkred !important; }
```

**最佳实践**：仅在第三方库覆盖或可访问性场景使用 `!important`，业务代码应通过结构化选择器解决。

### 3.3 陷阱 3：深层嵌套导致优先级过高

**问题**：SCSS / Less 嵌套过深，生成高优先级选择器。

```scss
// 反例：嵌套过深
.nav {
  .list {
    .item {
      .link {
        color: blue;  // 编译为 .nav .list .item .link (0,0,4,0)
      }
    }
  }
}
```

**最佳实践**：嵌套不超过 3 层，使用 `&` 引用父选择器。

```scss
// 正例：扁平化结构
.nav-link {
  color: blue;  // (0,0,1,0)
}
```

### 3.4 陷阱 4：通配符与组合符误用

**问题**：误以为 `*` 和 `>` `+` `~` 计入优先级。

```css
/* 通配符与组合符不计入优先级 */
* { margin: 0; }  /* (0,0,0,0) */
.a > .b { color: red; }  /* (0,0,2,0) - > 不计入 */
.a + .b { color: blue; }  /* (0,0,2,0) - + 不计入 */
```

**最佳实践**：理解规范条款，避免误判。

### 3.5 陷阱 5：`:where()` 的零优先级误用

**问题**：误以为 `:where()` 能提升优先级。

```css
/* 反例：误用 :where() 提升优先级 */
:where(.btn) {
  color: red;  /* (0,0,0,0) - 实际比 .btn 还低 */
}

.btn {
  color: blue;  /* (0,0,1,0) - 胜出 */
}
```

**最佳实践**：`:where()` 用于「降低副作用」，如重置样式或第三方库包装。

### 3.6 陷阱 6：`@layer` 内的优先级误判

**问题**：误以为层内高优先级能跨越层边界。

```css
@layer low, high;

@layer low {
  #id { color: red; }  /* (0,1,0,0) 但在 low 层 */
}

@layer high {
  .class { color: blue; }  /* (0,0,1,0) 但在 high 层 */
}
/* 结果：.class 胜出（high 层 > low 层，与优先级无关） */
```

**最佳实践**：理解 `@layer` 的层间不可越级特性。

### 3.7 陷阱 7：内联样式与 JavaScript 设置的优先级

**问题**：通过 `element.style` 设置的样式优先级为 (1,0,0,0)，难以覆盖。

```javascript
// JavaScript 设置内联样式
element.style.color = 'red';  // 等价于 style="color: red;"
```

```css
/* CSS 难以覆盖 */
.element { color: blue; }  /* (0,0,1,0) < (1,0,0,0) */
.element { color: blue !important; }  /* !important 才能覆盖 */
```

**最佳实践**：避免在 JavaScript 中直接设置样式，改用类切换。

```javascript
// 正例：通过类切换
element.classList.add('active');
```

```css
.element.active { color: blue; }  /* (0,0,2,0) */
```

### 3.8 陷阱 8：用户样式表的优先级

**问题**：忽略用户样式表（如无障碍设置）的优先级。

```css
/* 作者样式可能被用户 !important 覆盖 */
.text {
  font-size: 12px !important;  /* 用户 !important 优先级更高 */
}
```

**最佳实践**：尊重用户偏好，使用相对单位（`rem`、`em`）。

---

## 4. 工程实践
### 4.1 优先级管理架构

```mermaid
flowchart TD
    L1[Layer 1: Design Tokens 设计令牌] --> L2[Layer 2: Reset 重置]
    L2 --> L3[Layer 3: Vendor 第三方库]
    L3 --> L4[Layer 4: Base 基础样式]
    L4 --> L5[Layer 5: Components 组件]
    L5 --> L6[Layer 6: Utilities 工具类]
    L6 --> L7[Layer 7: Overrides 业务覆盖]
    L7 --> UL[Unlayered: 业务代码<br/>最高优先级]
```

### 4.2 Stylelint 配置实践

```javascript
// .stylelintrc.js - 企业级 Stylelint 配置
module.exports = {
  extends: [
    'stylelint-config-standard',
    'stylelint-config-recommended',
    '@stylelint/postcss-css-in-js',
  ],
  plugins: [
    'stylelint-selector-max-specificity',
    'stylelint-no-unsupported-browser-features',
  ],
  rules: {
    // 优先级上限：(0, 2, 3, 0)
    'selector-max-specificity': '0,2,3,0',
    // 禁止 ID 选择器
    'selector-max-id': 0,
    // 限制类选择器组合数
    'selector-max-class': 3,
    // 限制嵌套深度
    'selector-max-compound-selectors': 4,
    // 禁止 !important
    'declaration-no-important': true,
    // BEM 命名规范
    'selector-class-pattern': '^[a-z][a-z0-9]*(?:-[a-z0-9]+)*(?:__[a-z0-9-]+)?(?:--[a-z0-9-]+)?$',
    // 禁止通配符
    'selector-max-universal': 0,
    // 浏览器兼容性
    'plugin/no-unsupported-browser-features': [true, {
      severity: 'warning',
      browsers: ['> 1%', 'last 2 versions', 'not dead'],
    }],
  },
};
```

### 4.3 PostCSS 自动降级

```javascript
// postcss.config.js - PostCSS 配置
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions', 'not dead'],
    }),
    require('@csstools/postcss-cascade-layers')({
      onRevertLayer: 'warn',
    }),
    require('postcss-nesting'),
    require('postcss-custom-properties')({
      preserve: true,
    }),
  ],
};
```

### 4.4 设计令牌（Design Tokens）

```css
/* tokens.css - 设计令牌层 */
@layer tokens {
  :root {
    /* 颜色 */
    --color-primary-50: #eff6ff;
    --color-primary-500: #3b82f6;
    --color-primary-900: #1e3a8a;

    /* 间距 */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;

    /* 字号 */
    --font-size-sm: 0.875rem;
    --font-size-md: 1rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;

    /* 圆角 */
    --radius-sm: 4px;
    --radius-md: 6px;
    --radius-lg: 8px;

    /* 阴影 */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  }
}
```

### 4.5 组件库优先级管理

```css
/* components.css - 组件库层 */
@layer components {
  /* 基础组件类，优先级 (0,0,1,0) */
  .btn {
    display: inline-flex;
    align-items: center;
    padding: var(--spacing-sm) var(--spacing-md);
    border: none;
    border-radius: var(--radius-md);
    font-size: var(--font-size-md);
    cursor: pointer;
    transition: all 0.2s;
  }

  /* 变体类，优先级 (0,0,1,0) - 通过组合使用 */
  .btn-primary {
    background: var(--color-primary-500);
    color: white;
  }

  .btn-primary:hover {
    background: var(--color-primary-900);
  }

  /* 尺寸类 */
  .btn-sm { padding: var(--spacing-xs) var(--spacing-sm); font-size: var(--font-size-sm); }
  .btn-lg { padding: var(--spacing-md) var(--spacing-lg); font-size: var(--font-size-lg); }
}
```

### 4.6 工具类优先级管理

```css
/* utilities.css - 工具类层 */
@layer utilities {
  /* 间距工具 */
  .m-0 { margin: 0 !important; }
  .m-sm { margin: var(--spacing-sm) !important; }
  .m-md { margin: var(--spacing-md) !important; }
  .mt-sm { margin-top: var(--spacing-sm) !important; }
  .mt-md { margin-top: var(--spacing-md) !important; }

  /* 文本对齐 */
  .text-left { text-align: left !important; }
  .text-center { text-align: center !important; }
  .text-right { text-align: right !important; }

  /* 显示 */
  .d-none { display: none !important; }
  .d-block { display: block !important; }
  .d-flex { display: flex !important; }
}
```

> **注**：工具类中的 `!important` 是有意为之，确保工具类覆盖组件类。

### 4.7 调试优先级

```javascript
// 优先级调试工具
function debugSpecificity(element) {
  const computed = window.getComputedStyle(element);
  const rules = [];

  // 遍历所有匹配的规则
  for (const sheet of document.styleSheets) {
    try {
      for (const rule of sheet.cssRules) {
        if (rule.selectorText && element.matches(rule.selectorText)) {
          rules.push({
            selector: rule.selectorText,
            specificity: calculateSpecificity(rule.selectorText),
            text: rule.cssText,
          });
        }
      }
    } catch (e) {
      // 跨域样式表无法访问
    }
  }

  // 按优先级排序
  rules.sort((a, b) => {
    const sa = a.specificity;
    const sb = b.specificity;
    return sb.a - sa.a || sb.b - sa.b || sb.c - sa.c || sb.d - sa.d;
  });

  return rules;
}

// 使用示例
const element = document.querySelector('.btn');
console.log(debugSpecificity(element));
```

### 4.8 Playwright 视觉回归测试

```javascript
// priority.spec.js - Playwright 视觉回归测试
const { test, expect } = require('@playwright/test');

test.describe('优先级回归测试', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('按钮主变体颜色正确', async ({ page }) => {
    const button = page.locator('.btn-primary');
    await expect(button).toHaveCSS('background-color', 'rgb(59, 130, 246)');

    // 悬停状态
    await button.hover();
    await expect(button).toHaveCSS('background-color', 'rgb(30, 58, 138)');
  });

  test('工具类覆盖组件类', async ({ page }) => {
    const element = page.locator('.btn.text-center');
    await expect(element).toHaveCSS('text-align', 'center');
  });

  test('@layer 分层正确生效', async ({ page }) => {
    const element = page.locator('.layered-component');
    // 验证未分层样式覆盖分层样式
    await expect(element).toHaveCSS('color', 'rgb(0, 128, 0)');
  });
});
```

### 4.9 浏览器兼容性处理

```css
/* 兼容性处理：@layer 降级方案 */

/* 方案 1：使用 PostCSS 插件自动降级 */
/* @csstools/postcss-cascade-layers 会将 @layer 转换为优先级等效的传统 CSS */

/* 方案 2：手动降级（不推荐，仅作示例） */
/* 当 @layer 不支持时，使用 specificity 模拟 */

/* 现代浏览器：使用 @layer */
@layer reset, components, utilities;
@layer reset {
  h1 { margin: 0; }
}
@layer components {
  .title { font-size: 2rem; }
}
@layer utilities {
  .text-center { text-align: center; }
}

/* 旧浏览器降级：通过优先级模拟 */
/* h1 (0,0,0,1) < .title (0,0,1,0) < .text-center (0,0,1,0) */
/* 注意：降级后无法精确模拟层间不可越级特性 */
```

---

## 5. 案例研究
### 5.1 Bootstrap 5 的优先级策略

Bootstrap 5 采用「组件类 + 修饰类」的策略：

```css
/* Bootstrap 5 源码节选 */
.btn {
  /* 基础样式 (0,0,1,0) */
  display: inline-block;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
}

.btn-primary {
  /* 变体样式 (0,0,1,0)，与 .btn 组合使用 */
  color: #fff;
  background-color: #0d6efd;
  border-color: #0d6efd;
}

.btn-lg {
  /* 尺寸样式 (0,0,1,0) */
  padding: 0.5rem 1rem;
  font-size: 1.25rem;
  border-radius: 0.3rem;
}
```

**使用方式**：

```html
<button class="btn btn-primary btn-lg">大型主按钮</button>
```

**优先级分析**：三个类组合，优先级 (0,0,3,0)，但通过类组合而非嵌套，可维护性较好。

### 5.2 Tailwind CSS v3.4 的优先级策略

Tailwind 采用「原子工具类」策略：

```css
/* Tailwind 生成的工具类 */
.bg-blue-500 { background-color: #3b82f6; }
.text-white { color: #fff; }
.px-4 { padding-left: 1rem; padding-right: 1rem; }
.py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
.rounded { border-radius: 0.25rem; }
```

**使用方式**：

```html
<button class="bg-blue-500 text-white px-4 py-2 rounded">
  按钮
</button>
```

**优先级分析**：每个类独立 (0,0,1,0)，覆盖时需通过 `!` 前缀（如 `!bg-red-500`）或自定义类。

### 5.3 Material Design 3 的优先级策略

Material Design 3（MDC Web）采用「主题类 + 属性」策略：

```css
/* MDC Button 源码节选 */
.mdc-button {
  /* 基础样式 (0,0,1,0) */
  font-family: Roboto, sans-serif;
  padding: 0 8px;
  border: none;
  background: transparent;
}

.mdc-button--raised {
  /* 修饰类 (0,0,1,0) */
  box-shadow: 0px 3px 1px -2px rgba(0,0,0,0.2);
  background-color: #6200ee;
}

/* 通过 CSS 变量定制主题 */
.mdc-button {
  background-color: var(--mdc-theme-primary, #6200ee);
}
```

### 5.4 GitHub Primer 的优先级策略

GitHub Primer 采用「工具类 + 组件类」混合策略：

```css
/* Primer 源码节选 */
.btn {
  /* 基础 (0,0,1,0) */
  padding: 5px 16px;
  font-size: 14px;
  border: 1px solid transparent;
}

.btn-primary {
  /* 变体 (0,0,1,0) */
  color: #fff;
  background-color: #2da44e;
}

/* 工具类 */
.mt-2 { margin-top: 8px !important; }
.text-center { text-align: center !important; }
```

### 5.5 Ant Design 5 的优先级策略

Ant Design 5 采用 CSS-in-JS（cssinjs）方案：

```jsx
// Ant Design 5 使用 @ant-design/cssinjs
import { Button } from 'antd';

// 组件内部生成唯一类名，避免全局冲突
// <button class="ant-btn css-1abc123">按钮</button>
```

```css
/* Ant Design 生成的样式 */
.ant-btn {
  /* 优先级 (0,0,1,0) */
  padding: 4px 15px;
  border: 1px solid #d9d9d9;
}

.ant-btn-primary {
  background: #1677ff;
}

/* 通过 ConfigProvider 定制主题 */
.ant-btn {
  background: var(--ant-primary-color);
}
```

### 5.6 生产事故：优先级军备竞赛

**场景**：某电商平台首页按钮颜色异常，多个团队反复使用 `!important` 覆盖。

**事故时间线**：

1. 设计系统团队发布 `.btn-primary { background: blue; }`。
2. 营销团队需红色按钮，添加 `.campaign-btn { background: red !important; }`。
3. 设计系统升级蓝色，营销团队按钮变蓝，紧急添加 `.campaign-btn.campaign-btn { background: red !important; }`。
4. 黑五促销需金色按钮，前端添加 `#main .campaign-btn { background: gold !important; }`。
5. 一年后，新开发者试图修改按钮颜色，发现 5 层 `!important` 嵌套，无法维护。

**根因分析**：

- 缺乏统一的优先级管理规范。
- `!important` 滥用导致优先级不可逆。
- 团队间样式隔离不足。

**解决方案**：

1. 引入 `@layer` 分层架构。
2. Stylelint 禁止业务代码使用 `!important`。
3. 设计系统通过 CSS Variables 暴露主题入口。
4. 业务覆盖通过专门的 `overrides` 层管理。

```css
/* 重构后 */
@layer tokens, components, overrides;

@layer components {
  .btn-primary {
    background: var(--btn-primary-bg, blue);
  }
}

@layer overrides {
  .campaign-btn {
    --btn-primary-bg: red;
  }
}
```

---

### 填空题知识点讲解

**题目 1**：CSS 优先级四元组 (A, B, C, D) 中，A 表示 ________ 的数量，B 表示 ________ 的数量。

**解析讲解**：内联样式（`style` 属性）；ID 选择器

**解析讲解**：四元组 (A, B, C, D) 分别对应：内联样式（0 或 1）、ID 选择器数量、类/属性/伪类数量、元素/伪元素数量。

**题目 2**：`:where()` 的优先级恒为 ________。

**解析讲解**：(0, 0, 0, 0)

**解析讲解**：`:where()` 设计为零优先级伪类，无论其参数如何，优先级总是 (0,0,0,0)。

**题目 3**：CSS 层叠算法的 8 个阶段中，优先级（Specificity）位于第 ________ 阶段。

**解析讲解**：5

**解析讲解**：8 个阶段依次为：Origin & Importance → Context → Element-attached → Layer → Specificity → Order of Appearance → Animation → Transition。Specificity 是第 5 阶段。

**题目 4**：`@layer A, B, C;` 声明三个层，优先级从低到高为 ________。

**解析讲解**：A < B < C

**解析讲解**：`@layer` 的声明顺序决定优先级，先声明的层优先级低，后声明的层优先级高。

**题目 5**：`:has(.a #b)` 的优先级为 ________。

**解析讲解**：(0, 1, 1, 0)

**解析讲解**：`:has()` 的优先级由参数中最具体的选择器决定。`.a #b` 的优先级为 (0,1,1,0)（1 个 ID + 1 个类），因此 `:has(.a #b)` 的优先级也是 (0,1,1,0)。

### 编程题知识点讲解

**题目 1**：编写一个 CSS 选择器，使其优先级为 (0, 2, 3, 1)。

**解析讲解**：

```css
#header #nav .menu .item .link:hover div {
  /* 优先级计算：
   * #header (ID) → B=1
   * #nav (ID) → B=2
   * .menu (类) → C=1
   * .item (类) → C=2
   * .link (类) → C=3
   * :hover (伪类) → C=4
   * div (元素) → D=1
   * 总计：(0, 2, 4, 1)
   */
}
```

调整：要精确 (0, 2, 3, 1)：

```css
#header #nav .menu .item div:hover {
  /* #header (ID) → B=1
   * #nav (ID) → B=2
   * .menu (类) → C=1
   * .item (类) → C=2
   * :hover (伪类) → C=3
   * div (元素) → D=1
   * 总计：(0, 2, 3, 1)
   */
}
```

**题目 2**：使用 `@layer` 重构以下样式，使其符合企业级分层架构。

```css
/* 原始代码（混乱） */
* { margin: 0; }
.btn { padding: 8px; }
.btn-primary { background: blue; }
.text-center { text-align: center; }
.card { border: 1px solid #ccc; }
```

**解析讲解**：

```css
@layer reset, components, utilities;

@layer reset {
  * { margin: 0; }
}

@layer components {
  .btn {
    padding: 8px;
  }
  .btn-primary {
    background: blue;
  }
  .card {
    border: 1px solid #ccc;
  }
}

@layer utilities {
  .text-center {
    text-align: center;
  }
}
```

**解析讲解**：

1. `reset` 层最低，用于全局重置。
2. `components` 层包含组件样式。
3. `utilities` 层包含工具类，优先级高于组件类。
4. 未分层样式（如有）优先级最高。

**题目 3**：编写 JavaScript 函数，计算任意 CSS 选择器的优先级。

**解析讲解**：

```javascript
/**
 * 计算 CSS 选择器的优先级
 * @param {string} selector - CSS 选择器字符串
 * @returns {{a: number, b: number, c: number, d: number}} 优先级四元组
 */
function calculateSpecificity(selector) {
  let a = 0, b = 0, c = 0, d = 0;

  // 处理 :where() - 恒为 0，需先移除
  const cleaned = selector.replace(/:where\([^)]*\)/g, '');

  // ID 选择器
  const ids = cleaned.match(/#[\w-]+/g) || [];
  b += ids.length;

  // 类选择器
  const classes = cleaned.match(/\.[\w-]+/g) || [];
  c += classes.length;

  // 属性选择器
  const attrs = cleaned.match(/\[[^\]]+\]/g) || [];
  c += attrs.length;

  // 伪类（排除伪元素 ::）
  const pseudoClasses = cleaned.match(/:(?!:)[\w-]+(\([^)]*\))?/g) || [];
  // 排除 :where（已移除）、:is、:has、:not 的特殊性
  // 简化处理：:is、:has、:not 取参数中最高优先级
  for (const pc of pseudoClasses) {
    if (pc.startsWith(':is(') || pc.startsWith(':has(') || pc.startsWith(':not(')) {
      // 提取参数
      const inner = pc.match(/\(([^)]*)\)/);
      if (inner) {
        const innerSpec = calculateSpecificity(inner[1]);
        // 取最高
        if (innerSpec.b > b) b = innerSpec.b;
        if (innerSpec.c > c) c = innerSpec.c;
        if (innerSpec.d > d) d = innerSpec.d;
      }
    } else {
      c += 1;
    }
  }

  // 伪元素
  const pseudoElements = cleaned.match(/::[\w-]+/g) || [];
  d += pseudoElements.length;

  // 元素选择器（排除伪类、伪元素）
  const elements = cleaned
    .replace(/[#.\[:][^\s>+~]*/g, '')  // 移除 ID、类、属性、伪类
    .match(/[\w-]+/g) || [];
  d += elements.length;

  return { a, b, c, d };
}

// 测试
console.log(calculateSpecificity('#main .card:hover'));
// { a: 0, b: 1, c: 2, d: 0 }

console.log(calculateSpecificity(':where(#header) .nav'));
// { a: 0, b: 0, c: 1, d: 0 }

console.log(calculateSpecificity(':is(.a, #b)'));
// { a: 0, b: 1, c: 0, d: 0 }
```

**解析讲解**：生产环境推荐使用 [`specificity`](https://www.npmjs.com/package/specificity) 库，其解析更精确。

### 10.1 W3C 规范

- World Wide Web Consortium. (2021). *CSS Cascading and Inheritance Level 4*. W3C Recommendation. https://www.w3.org/TR/css-cascade-4/
- World Wide Web Consortium. (2023). *CSS Cascading and Inheritance Level 5*. W3C Working Draft. https://www.w3.org/TR/css-cascade-5/
- World Wide Web Consortium. (2018). *Selectors Level 3*. W3C Recommendation. https://www.w3.org/TR/selectors-3/
- World Wide Web Consortium. (2022). *Selectors Level 4*. W3C Working Draft. https://www.w3.org/TR/selectors-4/
- World Wide Web Consortium. (2011). *Cascading Style Sheets Level 2 Revision 1 (CSS 2.1) Specification*. W3C Recommendation. https://www.w3.org/TR/CSS21/
- World Wide Web Consortium. (1996). *Cascading Style Sheets, Level 1*. W3C Recommendation. https://www.w3.org/TR/CSS1/
- World Wide Web Consortium. (2024). *CSS Values and Units Module Level 4*. W3C Working Draft. https://www.w3.org/TR/css-values-4/

### 10.2 学术论文

- Lie, H. W., & Bos, B. (1999). *Cascading Style Sheets: Designing for the Web*. Addison-Wesley Professional. ISBN: 978-0201419989.
- Meyer, E. A. (2006). *Cascading Style Sheets: The Definitive Guide* (3rd ed.). O'Reilly Media. ISBN: 978-0596527334.
- Flanagan, D. (2011). *JavaScript: The Definitive Guide* (6th ed.). O'Reilly Media. Chapter 16: Cascading Style Sheets. ISBN: 978-0596805531.

### 10.3 工业实践

- Bootstrap. (2024). *Bootstrap 5.4 Documentation: Components - Buttons*. https://getbootstrap.com/docs/5.4/components/buttons/
- Tailwind Labs. (2024). *Tailwind CSS v3.4 Documentation: Handling Hover, Focus, and Other States*. https://tailwindcss.com/docs/hover-focus-and-other-states
- Google. (2024). *Material Design 3: Design System*. https://m3.material.io/
- Ant Design. (2024). *Ant Design 5.x Documentation: Customize Theme*. https://ant.design/docs/react/customize-theme
- GitHub. (2024). *Primer Design System*. https://primer.style/

### 10.4 工具与库

- Keegan, I. (2024). *specificity: A JavaScript function to calculate the specificity of CSS selectors*. https://github.com/keeganstreet/specificity
- Stylelint. (2024). *stylelint-selector-max-specificity*. https://stylelint.io/user-guide/rules/list/selector-max-specificity/
- PostCSS. (2024). *@csstools/postcss-cascade-layers*. https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-cascade-layers

### 10.5 ACM Reference Format

引用示例（ACM Reference Format）：

- World Wide Web Consortium. 2021. *CSS Cascading and Inheritance Level 4*. W3C Recommendation. Retrieved July 20, 2026 from https://www.w3.org/TR/css-cascade-4/
- Tab Atkins, and Miriam Suzanne. 2023. *CSS Cascading and Inheritance Level 5*. W3C Working Draft. Retrieved July 20, 2026 from https://www.w3.org/TR/css-cascade-5/
- Håkon Wium Lie, and Bert Bos. 1996. *Cascading Style Sheets, Level 1*. W3C Recommendation. Retrieved July 20, 2026 from https://www.w3.org/TR/CSS1/
- Eric A. Meyer. 2006. *Cascading Style Sheets: The Definitive Guide* (3rd ed.). O'Reilly Media, Sebastopol, CA. ISBN 978-0596527334.
- Keegan Street. 2024. *specificity: Calculate CSS selector specificity*. Retrieved July 20, 2026 from https://github.com/keeganstreet/specificity

---

### 11.1 经典书籍

- **《CSS Secrets》** - Lea Verou 著，深入探讨 CSS 的高级技巧与优先级管理。
- **《CSS: The Definitive Guide》** - Eric A. Meyer 著，CSS 完整参考。
- **《CSS in Depth》** - Keith J. Grant 著，现代 CSS 工程实践。
- **《Enduring CSS》** - Ben Frain 著，大型项目的 CSS 架构。

### 11.3 视频课程

- **Frontend Masters: CSS Grid & Flexbox for Responsive Layouts** - Jen Kramer
- **CSS Working Group: Cascade Layers Explained** - Miriam Suzanne
- **Chrome Developers: Specificity and the Cascade** - Una Kravets

### 11.4 社区博客

- **CSS-Tricks** - https://css-tricks.com/
- **Smashing Magazine** - https://www.smashingmagazine.com/category/css/
- **A List Apart** - https://alistapart.com/topic/css/
- **Miriam Suzanne's Blog** - https://miriamsuzanne.com/

### 11.5 规范演进方向

- **CSS Cascading Level 6 草案**：探讨 `@layer` 嵌套与范围查询。
- **CSS Scope**：引入 `@scope` 规则，提供更细粒度的样式作用域。
- **CSS Functions**：探讨 `specificity()` 函数，允许在 CSS 中查询优先级。
- **Houdini CSS Parser API**：提供底层 CSS 解析能力，可自定义优先级算法。

### 11.6 相关规范

- **[CSS Box Model Module Level 3](https://www.w3.org/TR/css-box-3/)** - 盒模型规范。
- **[CSS Display Module Level 3](https://www.w3.org/TR/css-display-3/)** - display 属性规范。
- **[CSS Positioned Layout Module Level 3](https://www.w3.org/TR/css-position-3/)** - 定位规范。
- **[CSS Custom Properties for Cascading Variables Module Level 1](https://www.w3.org/TR/css-variables-1/)** - CSS 变量规范。
- **[CSS Containment Module Level 3](https://www.w3.org/TR/css-contain-3/)** - 容器查询规范。

---

## 6. 深入理解（选读）

> 以下内容适合想彻底搞懂机制原理的读者，第一遍学习可跳过。

### 6.1 历史演进

### 6.1.1 CSS 1（1996）：优先级的雏形

CSS 1 由 Håkon Wium Lie 与 Bert Bos 于 1996 年提出，首次引入「层叠」（Cascade）概念。当时规范对优先级的定义较为粗糙：

> The weight of a rule's selector is determined by counting the number of ID attributes (a), the number of CLASS attributes (b), and the number of element names (c) in the selector.

CSS 1 仅使用三元组 (a, b, c)，且未明确「内联样式」与 `!important` 的位置。浏览器实现差异较大，开发者常需依赖 `!important` 解决冲突。

### 6.1.2 CSS 2（1998）：引入 `!important` 与来源排序

CSS 2 正式引入 `!important` 声明，并明确三类样式来源：

1. **Author**：作者样式表（页面开发者编写）。
2. **User**：用户样式表（浏览器用户自定义）。
3. **User Agent**：浏览器默认样式表。

层叠顺序规定：`Author Normal < User Normal < User Agent Normal < User !important < Author !important`。

这一阶段优先级演化为 (a, b, c, d) 四元组，其中 `a` 表示内联样式（0 或 1）。

### 6.1.3 CSS 2.1（2011）：规范的成熟

CSS 2.1 §6.4.3 给出经典的优先级计算规则：

> A selector's specificity is calculated as follows:
> - count 1 if the declaration is from a 'style' attribute rather than a rule with a selector, 0 otherwise (= a)
> - count the number of ID attributes in the selector (= b)
> - count the number of other attributes and pseudo-classes in the selector (= c)
> - count the number of element names and pseudo-elements in the selector (= d)

四元组 (a, b, c, d) 沿用至今，并明确「通配符 `*`、组合符 `> + ~` 不计入优先级」。

### 6.1.4 CSS Selectors Level 3（2011）：伪类细化

[Selectors Level 3](https://www.w3.org/TR/selectors-3/) 引入大量新伪类（`:nth-child()`、`:not()`、`:checked` 等），并明确：

- `:not()` 本身不计入优先级，但其参数中的选择器计入。
- 伪元素（`::before`、`::after` 等）以 (0, 0, 0, 1) 计入。
- 伪类（`:hover`、`:focus` 等）以 (0, 0, 1, 0) 计入。

### 6.1.5 CSS Cascading Level 4（2016-2021）：层叠算法的规范化

[CSS Cascading and Inheritance Level 4](https://www.w3.org/TR/css-cascade-4/) 将层叠算法规范化为 8 阶段排序：

1. **Origin & Importance**：来源与重要性。
2. **Context**：Shadow DOM 等上下文隔离。
3. **Element-attached**：元素附加样式（如 `style` 属性）。
4. **Layer**：`@layer` 声明的层级。
5. **Specificity**：优先级四元组。
6. **Order of Appearance**：出现顺序。
7. **Animation**：动画声明。
8. **Transition**：过渡声明（最高）。

### 6.1.6 `@layer` 的引入（2022）

[CSS Cascading and Inheritance Level 5](https://www.w3.org/TR/css-cascade-5/) 引入 `@layer` 规则，允许开发者显式声明样式层级：

```css
@layer reset, framework, components, utilities;

@layer reset {
  /* 重置样式 */
}

@layer framework {
  /* 框架样式 */
}
```

层内样式的优先级低于未分层样式（unlayered styles），且层的顺序由首次声明决定。`@layer` 是 CSS 自 2011 年以来对优先级管理的最大变革。

### 6.1.7 `:where()` 与 `:is()` 的标准化（2021-2022）

[:is()](https://www.w3.org/TR/selectors-4/#matches-pseudo) 与 [:where()](https://www.w3.org/TR/selectors-4/#zero-matches) 在 Selectors Level 4 中标准化：

- `:is(A, B, C)`：匹配参数中任意选择器，优先级取参数中最具体者。
- `:where(A, B, C)`：同 `:is()`，但优先级恒为 (0, 0, 0, 0)。

`:where()` 的零优先级特性使其成为「重置第三方库样式」的理想工具。

### 6.1.8 `:has()` 的到来（2023）

[:has()](https://www.w3.org/TR/selectors-4/#relational) 称为「父选择器」，允许根据子元素状态选择父元素：

```css
.card:has(img) {
  padding: 0; /* 仅当 card 内有 img 时生效 */
}
```

`:has()` 的优先级由其参数中最具体的选择器决定，与 `:is()` 一致。

### 6.1.9 演进时间线

| 年份 | 规范/事件 | 核心变化 |
| --- | --- | --- |
| 1996 | CSS 1 | 三元组 (a, b, c) 优先级 |
| 1998 | CSS 2 | 引入 `!important` 与三类来源 |
| 2011 | CSS 2.1 | 四元组 (a, b, c, d) 成熟 |
| 2011 | Selectors Level 3 | `:not()` 与伪元素优先级明确 |
| 2016 | Cascade Level 4 | 8 阶段层叠算法规范化 |
| 2021 | Selectors Level 4 | `:is()` / `:where()` 标准化 |
| 2022 | Cascade Level 5 | `@layer` 引入 |
| 2023 | `:has()` 浏览器支持 | 父选择器落地（Chrome 105+, Safari 15.4+） |
| 2024 | Cascade Level 6 草案 | 探讨 `@layer` 嵌套与范围查询 |

---

### 6.2 形式化定义

### 6.2.1 规范条款

依据 [CSS Cascading and Inheritance Level 4 §6.3](https://www.w3.org/TR/css-cascade-4/#cascade-specific)：

> If the cascade results in a value, use it. Otherwise, the property is inherited or its initial value is used.

以及 [CSS 2.1 §6.4.3](https://www.w3.org/TR/CSS21/cascade.html#specificity) 对优先级的定义：

> A selector's specificity is calculated as follows: count the number of ID attributes (a), other attributes and pseudo-classes (b), and element names and pseudo-elements (c) in the selector.

### 6.2.2 核心术语

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 优先级 | Specificity | 选择器的权重值，用于决定同来源同层级时的胜出声明 |
| 层叠 | Cascade | 浏览器决定最终生效样式的完整算法 |
| 来源 | Origin | 样式表的类别：User Agent / User / Author |
| 层 | Layer | 通过 `@layer` 声明的命名样式组 |
| 内联样式 | Inline style | 通过 `style` 属性直接附加在元素上的样式 |
| 重要性 | Importance | `!important` 声明，反转来源优先级 |
| 出现顺序 | Order of Appearance | 同优先级时，后出现的声明胜出 |

### 6.2.3 优先级四元组

CSS 优先级用四元组 $(A, B, C, D)$ 表示，其中：

- $A$：内联样式（`style` 属性），取值 0 或 1。
- $B$：ID 选择器（`#id`）的数量。
- $C$：类选择器（`.class`）、属性选择器（`[attr]`）、伪类（`:hover`）的数量。
- $D$：元素选择器（`div`）、伪元素（`::before`）的数量。

> **注**：部分文献采用 (a, b, c, d) 顺序，本节统一使用 $(A, B, C, D)$ 以避免与 CSS 1 的三元组混淆。

### 6.2.4 形式化计算函数

设选择器 $S$ 由若干简单选择器 $s_1, s_2, \ldots, s_n$ 组合而成，定义优先级函数 $\text{Spec}(S)$：

$$
\text{Spec}(S) = \left( \text{Inline}(S), \sum_{i=1}^{n} \text{ID}(s_i), \sum_{i=1}^{n} \text{Class}(s_i), \sum_{i=1}^{n} \text{Element}(s_i) \right)
$$

其中：

$$
\text{ID}(s_i) =
\begin{cases}
1, & \text{if } s_i \text{ 是 ID 选择器} \\
0, & \text{otherwise}
\end{cases}
$$

$$
\text{Class}(s_i) =
\begin{cases}
1, & \text{if } s_i \in \{\text{类选择器}, \text{属性选择器}, \text{伪类（除 }:where()\text{）}\} \\
0, & \text{otherwise}
\end{cases}
$$

$$
\text{Element}(s_i) =
\begin{cases}
1, & \text{if } s_i \in \{\text{元素选择器}, \text{伪元素}\} \\
0, & \text{otherwise}
\end{cases}
$$

### 6.2.5 比较运算

两个优先级四元组 $(A_1, B_1, C_1, D_1)$ 与 $(A_2, B_2, C_2, D_2)$ 的比较遵循字典序：

$$
\text{Compare}(S_1, S_2) =
\begin{cases}
S_1 > S_2, & \text{if } A_1 > A_2 \\
S_1 > S_2, & \text{if } A_1 = A_2 \wedge B_1 > B_2 \\
S_1 > S_2, & \text{if } A_1 = A_2 \wedge B_1 = B_2 \wedge C_1 > C_2 \\
S_1 > S_2, & \text{if } A_1 = A_2 \wedge B_1 = B_2 \wedge C_1 = C_2 \wedge D_1 > D_2 \\
S_1 = S_2, & \text{if all equal}
\end{cases}
$$

注意：四元组的进位关系是「无限基数」而非十进制。即 $(0, 1, 0, 0) > (0, 0, N, 0)$ 对任意有限 $N$ 成立。

### 6.2.6 层叠算法的形式化

[CSS Cascading and Inheritance Level 4 §6.1](https://www.w3.org/TR/css-cascade-4/#cascading) 定义层叠排序函数 $\text{Sort}(d_1, d_2)$，对两个声明 $d_1, d_2$ 比较：

$$
\text{Sort}(d_1, d_2) =
\begin{cases}
d_1, & \text{if } \text{Origin}(d_1) \succ \text{Origin}(d_2) \\
d_1, & \text{if } \text{Origin equal} \wedge \text{Context}(d_1) \succ \text{Context}(d_2) \\
d_1, & \text{if } \text{Context equal} \wedge \text{ElementAttached}(d_1) \succ \text{ElementAttached}(d_2) \\
d_1, & \text{if } \text{ElementAttached equal} \wedge \text{Layer}(d_1) \succ \text{Layer}(d_2) \\
d_1, & \text{if } \text{Layer equal} \wedge \text{Spec}(d_1) > \text{Spec}(d_2) \\
d_1, & \text{if } \text{Spec equal} \wedge \text{Order}(d_1) > \text{Order}(d_2) \\
d_1, & \text{if } \text{Order equal} \wedge \text{Animation}(d_1) \succ \text{Animation}(d_2) \\
d_1, & \text{if } \text{Animation equal} \wedge \text{Transition}(d_1) \succ \text{Transition}(d_2) \\
d_2, & \text{otherwise}
\end{cases}
$$

其中 $\succ$ 表示「优先于」。

### 6.2.7 来源与重要性排序

| 来源 | 正常 | `!important` |
| --- | --- | --- |
| User Agent（浏览器默认） | 1（最低） | 6 |
| User（用户样式） | 2 | 7 |
| Author（作者样式） | 3 | 8 |
| Author（未分层，unlayered） | 4 | 9 |
| Author（分层，layered） | 5 | 10（最高） |

> **注**：CSS Cascade Level 5 引入 `@layer` 后，分层样式总是低于未分层样式（无论优先级多高）。

### 6.2.8 `:where()` 与 `:is()` 的优先级规则

设 `:is(S_1, S_2, \ldots, S_n)` 的优先级为：

$$
\text{Spec}(:\text{is}(S_1, S_2, \ldots, S_n)) = \max_{i=1}^{n} \text{Spec}(S_i)
$$

而 `:where()` 恒为零：

$$
\text{Spec}(:\text{where}(S_1, S_2, \ldots, S_n)) = (0, 0, 0, 0)
$$

`:has(S)` 与 `:not(S)` 的优先级为参数中最具体者：

$$
\text{Spec}(:\text{has}(S)) = \text{Spec}(:\text{is}(S))
$$

---

### 6.3 理论推导与原理解析

### 6.3.1 优先级的「基数」本质

CSS 优先级四元组的比较并非十进制数比较，而是基于「基数」的字典序比较。形式化地：

$$
(A, B, C, D) \text{ 的比较基于 } A \cdot \aleph_0^3 + B \cdot \aleph_0^2 + C \cdot \aleph_0 + D
$$

其中 $\aleph_0$ 是可数无穷基数。这意味着：

- $(0, 1, 0, 0) > (0, 0, N, 0)$ 对任意有限 $N$。
- $(1, 0, 0, 0) > (0, N, M, K)$ 对任意有限 $N, M, K$。

这一设计反映了 CSS 的语义优先级：ID 选择器表达「唯一标识」，应绝对优先于「类别标识」；内联样式表达「元素级定制」，应绝对优先于「规则级声明」。

### 6.3.2 层叠算法的决策树

层叠算法可视为一棵决策树，每个节点对应一个比较维度。浏览器从根节点开始，依次比较：

```mermaid
flowchart TD
    T0["1. Origin & Importance"]
    T1["不同 → 较高者胜"]
    T2["相同 → 进入 2"]
    T3["2. Context (Shadow DOM)"]
    T4["不同 → 较外层胜"]
    T5["相同 → 进入 3"]
    T6["3. Element-attached (style 属性)"]
    T7["不同 → 有 style 者胜"]
    T8["相同 → 进入 4"]
    T9["4. Layer"]
    T10["不同 → 未分层胜；分层中后声明胜"]
    T11["相同 → 进入 5"]
    T12["5. Specificity"]
    T13["不同 → 较高者胜"]
    T14["相同 → 进入 6"]
    T15["6. Order of Appearance"]
    T16["不同 → 后出现者胜"]
    T17["相同 → 进入 7"]
    T18["7. Animation"]
    T19["... (略)"]
    T20["8. Transition (最高)"]
    T0 --> T1
    T0 --> T2
    T2 --> T3
    T3 --> T4
    T3 --> T5
    T5 --> T6
    T6 --> T7
    T6 --> T8
    T8 --> T9
    T9 --> T10
    T9 --> T11
    T11 --> T12
    T12 --> T13
    T12 --> T14
    T14 --> T15
    T15 --> T16
    T15 --> T17
    T17 --> T18
    T18 --> T19
    T19 --> T20
```

### 6.3.3 `!important` 的反转机制

`!important` 的核心机制是「反转来源优先级」：

- 正常声明：Author > User > User Agent
- `!important` 声明：User Agent > User > Author

但 [CSS Cascade Level 4](https://www.w3.org/TR/css-cascade-4/#importance) 调整了用户 `!important` 与作者 `!important` 的关系：作者 `!important` 高于用户 `!important`（这逆转了 CSS 2.1 的顺序，以避免用户样式破坏作者样式）。

形式化地，定义来源优先级函数 $\text{OriginRank}(d)$：

$$
\text{OriginRank}(d) =
\begin{cases}
1, & \text{UA Normal} \\
2, & \text{User Normal} \\
3, & \text{Author Normal (layered)} \\
4, & \text{Author Normal (unlayered)} \\
5, & \text{Author !important (unlayered)} \\
6, & \text{Author !important (layered)} \\
7, & \text{User !important} \\
8, & \text{UA !important} \\
9, & \text{Transition}
\end{cases}
$$

### 6.3.4 `@layer` 的语义

`@layer` 引入显式的层级概念，其语义为：

1. **声明顺序**：`@layer A, B, C;` 声明三个层，优先级 A < B < C。
2. **未分层优先**：未分层的样式（unlayered）总是优先于分层样式。
3. **嵌套层**：`@layer A.B { ... }` 等价于在 A 层内声明 B 子层，B 的优先级高于 A 内的其他内容但低于 A 的兄弟层。

```css
@layer A, B;
@layer A {
  .x { color: red; } /* 优先级低 */
}
@layer B {
  .x { color: blue; } /* 优先级高 */
}
.x { color: green; } /* 未分层，最高 */
```

形式化地，设层 $L$ 的优先级为 $\text{LayerRank}(L)$：

$$
\text{LayerRank}(L) =
\begin{cases}
0, & L \text{ 是未分层样式} \\
n, & L \text{ 是第 } n \text{ 个声明的层（从 1 开始）}
\end{cases}
$$

未分层样式的 $\text{LayerRank}$ 总是大于任何分层样式。

### 6.3.5 `:where()` 的零优先级设计

`:where()` 恒返回 (0, 0, 0, 0) 的设计目的是提供「无副作用的样式重置」。考虑以下场景：

```css
/* 第三方库样式 */
.card { padding: 16px; }

/* 业务代码：重置 padding */
:where(.card) { padding: 0; }
/* 优先级 (0, 0, 1, 0) vs (0, 0, 0, 0) */
/* 第三方库胜出！ */
```

如需重置，应使用：

```css
:where(.card) { padding: 0; }  /* (0,0,0,0) */
.card { padding: 16px; }       /* (0,0,1,0) - 第三方胜出 */

/* 改用更高优先级 */
.card.card { padding: 0; }     /* (0,0,2,0) - 业务胜出 */
```

`:where()` 的真正价值在于「组合选择器时降低副作用」：

```css
/* 不使用 :where() - 复杂选择器污染优先级 */
.card .title { font-size: 1rem; }  /* (0,0,2,0) */

/* 使用 :where() - 优先级保持为 0 */
:where(.card .title) { font-size: 1rem; }  /* (0,0,0,0) */
```

### 6.3.6 内联样式与 `!important` 的关系

内联样式（`style` 属性）的优先级为 $(1, 0, 0, 0)$，但 `!important` 仍可覆盖：

```html
<div style="color: red;">红色</div>
```

```css
div { color: blue !important; }  /* 覆盖内联样式 */
```

形式化地：

$$
\text{Effective}(\text{inline normal}) < \text{Effective}(\text{rule !important})
$$

但内联 `!important` 仍高于规则 `!important`：

```html
<div style="color: red !important;">红色</div>
```

```css
div { color: blue !important; }  /* 不覆盖内联 !important */
```

### 6.3.7 计算示例

给定选择器 `#nav .list li:hover`，计算其优先级：

1. `#nav`：ID 选择器 → $B = 1$
2. `.list`：类选择器 → $C = 1$
3. `li`：元素选择器 → $D = 1$
4. `:hover`：伪类 → $C = 2$

合计：$(0, 1, 2, 1)$。

给定选择器 `:is(#header, .nav) a`：

1. `:is(#header, .nav)`：取参数中最高，即 `#header` 的 $(0, 1, 0, 0)$
2. `a`：元素选择器 → $D = 1$

合计：$(0, 1, 0, 1)$。

给定选择器 `:where(#header, .nav) a`：

1. `:where(...)`：恒为 $(0, 0, 0, 0)$
2. `a`：元素选择器 → $D = 1$

合计：$(0, 0, 0, 1)$。

### 6.3.8 优先级与可访问性

优先级直接影响可访问性（Accessibility）：

1. **用户样式表**：浏览器允许用户定义自定义样式（如放大字号、高对比度）。这些样式通过 `!important` 提升优先级，确保覆盖作者样式。
2. **`prefers-color-scheme`**：用户偏好（如深色模式）通过媒体查询应用，但优先级仍遵循层叠规则。
3. **`forced-colors`**：Windows 高对比度模式会强制覆盖颜色，作者样式应通过 `forced-color-adjust: none` 选择退出。

```css
@media (forced-colors: active) {
  .button {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
  }
}
```

---

## 7. 本章综合挑战（选做）
1. 写出 `#main .card:hover a` 的四元组并手工计算；
2. 用 `:where()` 写一套“可被覆盖的默认样式”，再验证业务类能否覆盖；
3. 用 `@layer` 把 reset、框架、组件、工具类分成四层，确认优先级顺序；
4. 用 DevTools 的 Computed 面板找出一条被覆盖的声明，解释覆盖原因。

## 8. 核心知识点
> 一句话记住优先级：四元组从左比（内联、ID、类、元素），第一个不同即定胜负；`!important` 反转，`@layer` 排座次，`:where()` 归零。

- 优先级四元组：(内联, ID, 类, 元素)，逐位比较；
- 相同优先级按“出现顺序”，后写覆盖先写；
- `!important` 反转来源排序，但应尽量避免；
- `:is()` 取参数中最高优先级，`:where()` 恒为 0；
- `@layer` 让“层顺序”优先于选择器权重；
- 内联样式高于一切选择器（除 `!important`）；
- 调试用 DevTools Computed 面板 + 手工计算交叉验证。

## 9. 注意事项与改进建议
| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 用 `!important` 救火 | 优先级体系崩塌 | 查权重与层顺序，从源头修正 |
| 深层选择器 | 权重失控、难覆盖 | 用类名扁平化（BEM） |
| 不了解 `@layer` 顺序 | 工具类覆盖失败 | 声明层顺序：reset < framework < utilities |
| 滥用 `:is()` | 权重意外抬高 | 需要归零覆盖时用 `:where()` |
| 内联样式 + JS 混用 | 调试困难 | 用 CSS 变量与类切换状态 |
| 忽略用户样式表 | 可访问性设置被覆盖 | 避免 `!important`，尊重用户样式 |

## 10. 扩展学习
- 层叠进阶：`css/039-CascadeLayer`；
- 选择器：`css/007-CSS3SelectorSystem`、`css/023-PseudoClassPseudoElement`；
- 作用域：`css/070-ScopeAtRule`；
- 工程实践：BEM（`css/057-BEMNamingMethodology`）与 CSS Modules（`css/059-CSSModules`）；
- 框架对照：Tailwind 的工具类优先级设计（`tailwind/` 模块）。

## 附录 A：术语表

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 优先级 | Specificity | 选择器的权重值 |
| 层叠 | Cascade | 浏览器决定最终样式的算法 |
| 来源 | Origin | 样式表类别（UA/User/Author） |
| 层 | Layer | `@layer` 声明的命名样式组 |
| 内联样式 | Inline Style | `style` 属性附加的样式 |
| 重要性 | Importance | `!important` 声明 |
| 出现顺序 | Order of Appearance | 同优先级时的决胜规则 |
| 上下文 | Context | Shadow DOM 等隔离环境 |
| 元素附加 | Element-attached | `style` 属性样式 |
| 动画 | Animation | `@keyframes` 动画声明 |
| 过渡 | Transition | `transition` 过渡声明 |

## 附录 B：浏览器兼容性

| 特性 | Chrome | Firefox | Safari | Edge | 兼容性 |
| --- | --- | --- | --- | --- | --- |
| 四元组优先级 | 全部 | 全部 | 全部 | 全部 | 100% |
| `!important` | 全部 | 全部 | 全部 | 全部 | 100% |
| `:not()` | 1+ | 1+ | 3+ | 12+ | 100% |
| `:is()` | 88+ | 78+ | 14+ | 88+ | 95%+ |
| `:where()` | 88+ | 78+ | 14+ | 88+ | 95%+ |
| `:has()` | 105+ | 121+ | 15.4+ | 105+ | 90%+ |
| `@layer` | 99+ | 97+ | 15.4+ | 99+ | 95%+ |
| `@scope` | 118+ | 实验性 | 实验性 | 118+ | 30%+ |

## 附录 C：调试检查清单

- [ ] 使用 DevTools 的「Computed」面板查看最终生效样式
- [ ] 检查 DevTools 中被划掉的声明，理解被覆盖原因
- [ ] 手工计算选择器优先级，验证与 DevTools 显示一致
- [ ] 检查是否存在 `!important` 滥用
- [ ] 检查 `@layer` 声明顺序是否正确
- [ ] 验证第三方库样式是否污染业务代码
- [ ] 检查内联样式与 JavaScript `style` 设置
- [ ] 验证用户样式表（如可访问性设置）的影响
- [ ] 使用 Stylelint 检查优先级上限
- [ ] 编写 Playwright 视觉回归测试

<!-- ============ 文档分隔线：007-css/010-CascadeInheritanceBasics.md ============ -->

## 0. 直觉：有些样式“传下去”，有些样式“抢着赢”

给 `body` 设置 `color: #333`，整个页面文字都变色——这叫继承。两个选择器同时命中一个元素，只有一个赢——这叫层叠。继承解决“默认值从哪来”，层叠解决“谁说了算”，两者合起来才是 CSS 的决策全貌。

## 1. 哪些属性会继承

```css
body {
  color: #333;          /* 可继承：文字颜色 */
  font-size: 16px;      /* 可继承：字号 */
  font-family: Arial, sans-serif;  /* 可继承：字体 */
  line-height: 1.6;     /* 可继承：行高 */
  text-align: center;   /* 可继承：对齐 */
  margin: 0;            /* 不可继承：外边距 */
  padding: 0;           /* 不可继承：内边距 */
  border: 1px solid red; /* 不可继承：边框 */
  background: #fff;     /* 不可继承：背景 */
}
```

**讲解：** 规律是“跟文字外观相关的属性大多可继承（color/font*/text*/line-height），跟盒子布局相关的属性基本不可继承（margin/padding/border/background/width/height）”。记规律比背清单可靠。

## 2. 继承与初始值

如果某个属性既没被设置、又不可继承，元素使用它的初始值（initial value）：

| 属性 | 初始值 |
| --- | --- |
| `color` | `canvastext`（通常是黑色） |
| `margin`/`padding` | `0` |
| `background-color` | `transparent` |
| `display` | `inline` |
| `width`/`height` | `auto` |

**讲解：** “为什么 div 默认占满一行、span 不占”——因为 `div` 是块级元素，但它的 `width` 初始值是 `auto`，自动填满父容器。初始值不等于 0，很多布局直觉来自这里。

## 3. 四个全局关键字

```css
.reset-color {
  color: initial;   /* 回到初始值（黑色） */
}
.inherit-color {
  color: inherit;   /* 强制继承父级 */
}
.unset-color {
  color: unset;     /* 可继承属性=inherit，不可继承=initial */
}
.revert-color {
  color: revert;    /* 回退到用户代理（浏览器默认）样式 */
}
```

**讲解：** 日常最常用 `inherit`（强制继承）与 `unset`（清除某条声明）；`revert` 常用于“撤销重置样式，恢复浏览器默认”。`initial` 会把可继承属性也变回初始值，容易误用。

## 4. 层叠决策的入门模型

当多个规则命中同一元素时，按以下顺序决策（深入算法见 `css/009-PriorityCalculation`）：

1. 来源与重要性：作者 `!important` > 行内样式 > 普通规则 > 浏览器默认；
2. 选择器权重：ID > 类 > 标签；
3. 书写顺序：权重相同时后写赢。

```css
p {
  color: gray;       /* (0,0,0,1) */
}
.text {
  color: blue;       /* (0,0,1,0) 赢 */
}
```

**讲解：** 层叠是“先比来源，再比权重，最后比顺序”的三级筛选；继承只负责“没有规则命中时”的默认值来源，优先级低于任何作者规则。

## 5. 与 007 的分工

本课是“入门版”：记住哪些属性会继承、四个关键字干什么、层叠三级模型；`css/009-PriorityCalculation` 是“深入版”：四元组精确计算、`:is()`/`:where()` 的权重规则、`@layer` 分层、工程实践。先有本课直觉，再读 007 才不会迷失在规范细节里。

## 6. 动手试试

1. 给 `body` 设置 `color`/`font-size`，观察哪些子元素继承、哪些不继承；
2. 给一个 `a` 标签写 `color: inherit`，对比默认链接颜色；
3. 用 `unset` 清除一个类里设置的颜色，观察它是否“恢复继承”；
4. 进阶挑战：写一个“重置按钮样式”的规则，用 `revert` 恢复浏览器默认按钮外观。

## 7. 核心知识点

> 一句话记住继承与层叠：文字属性往下传、盒子属性不传；没规则时用初始值；有冲突时按“来源 → 权重 → 顺序”决出胜负。

- 可继承：color/font/text 系列；不可继承：盒模型与背景；
- 没有值可用时用初始值，初始值不等于 0；
- `inherit` 强制继承、`initial` 回初始值、`unset` 按属性类型二选一、`revert` 回浏览器默认；
- 层叠三级：来源与重要性 → 权重 → 顺序；
- 继承的优先级低于任何作者规则；
- 深入算法见 009，本课负责日常直觉。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 认为所有属性都继承 | 盒子属性其实不继承 | 按“文字 vs 盒子”分类记忆 |
| 用 initial 清样式 | 可继承属性被清回初始值，行为意外 | 想“不设置”用 `unset`，想“跟父级”用 `inherit` |
| 重置样式全用 `* {}` | 破坏可继承属性的自然传播 | 重置方案见 `css/008-CSSResetAndNormalize` |
| 只记权重不记来源 | 浏览器默认/!important 场景判断错 | 先过“来源与重要性”这一级 |

## 9. 扩展学习

- 优先级深入：`css/009-PriorityCalculation`；
- 优先级速查：`css/012-CSSPriorityQuickStart`；
- 重置方案：`css/008-CSSResetAndNormalize`；
- 选择器系统：`css/007-CSS3SelectorSystem`。

<!-- ============ 文档分隔线：007-css/011-StyleSheetImportMethod.md ============ -->

## 0. 直觉：样式“怎么端上桌”

CSS 有四种“上桌方式”：直接塞进标签（内联）、写在页面里（嵌入）、放在独立文件（外部）、在 CSS 里再引 CSS（@import）。

记住一句口诀：能用外部就用外部，能不用 `@import` 就不用 `@import`。内联只在调试或动态注入时用。


## 1. 四种引入方式

### 内联样式

```html
<p style="color: red;">内联样式</p>
```

优先级最高、无法复用、不推荐。

**讲解：** 样式写在 `style` 属性里，只能作用于当前元素，且无法被选择器覆盖（除非 `!important`），适合临时调试。

### 嵌入样式

```html
<style>
  p {
    color: blue;
  }
</style>
```

仅当前页面有效、无法缓存。

**讲解：** `<style>` 写在 `<head>` 中，页面内所有元素可用；单页项目方便，多页面无法复用。

### 外部样式表

```html
<link rel="stylesheet" href="styles.css" />
```

可复用、可缓存、**推荐方式**。

**讲解：** `<link>` 引入独立样式文件，浏览器会缓存它，多个页面共享；生产环境的标准做法。

### @import 导入

```css
@import url('reset.css');
```

串行加载（性能差）、避免在顶层使用。

**讲解：** `@import` 在 CSS 解析时才发起请求，会阻塞渲染；现代打包工具（Vite/Webpack）会自动合并 CSS，无需手写。

## 2. 对比

| 方式    | 复用性 | 缓存 | 性能 | 推荐度     |
| ------- | ------ | ---- | ---- | ---------- |
| 内联    | 无     | 无   | 差   | 低         |
| 嵌入    | 单页   | 无   | 中   | 中         |
| 外部    | 多页   | 有   | 好   | 极高       |
| @import | 多页   | 有   | 差   | 中         |

## 3. 关键 CSS 内联

```html
<head>
  <style>
    .hero {
      height: 100vh;
    }
  </style>
  <link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'" />
</head>
```

**讲解：** 首屏关键样式（如 `.hero`）内联到 `<head>` 立即生效；非关键样式用 `preload` + `onload` 异步加载，兼顾首屏速度与缓存。

## 4. 动手试试

1. 用四种方式分别给 `p` 设置不同颜色，刷新观察优先级；
2. 新建 `styles.css` 并用 `<link>` 引入，确认浏览器 Network 面板出现该文件请求；
3. 把 `<link>` 改成 `@import` 放在样式文件顶部，对比加载顺序（Network 瀑布图）；
4. 进阶挑战：用 `preload` + `onload` 异步加载非关键样式。

## 5. 核心知识点

> 一句话记住引入方式：外部 `<link>` 是标准，内联只调试，`@import` 会阻塞，关键样式可内联。

- 内联：优先级最高，无法复用；
- 嵌入：单页可用，无法跨页；
- 外部：可复用、可缓存，生产首选；
- `@import`：串行阻塞，避免使用；
- 首屏关键 CSS 可内联，其余用 `<link>` 或异步加载。

## 6. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 大量内联样式 | 无法复用、维护困难 | 抽取为类与外部文件 |
| 顶层 `@import` | 阻塞首屏渲染 | 用 `<link>` 或构建工具合并 |
| 样式文件过多 | 请求数膨胀 | 按页面/组件拆分并合并 |
| 关键样式外链 | 首屏等待 | 关键样式内联 |

## 7. 扩展学习

- 优先级：`css/009-PriorityCalculation`；
- 性能：`css/060-CriticalRenderPathOptimization`；
- 工程化：`css/056-PostCSS` 与构建工具的样式处理。

<!-- ============ 文档分隔线：007-css/012-CSSPriorityQuickStart.md ============ -->

## 0. 一句话记住优先级

**选择器越“具体”，优先级越高；一样具体时，后写的赢。**

`#main` 比 `.card` 具体，`.card` 比 `div` 具体。写 CSS 时 90% 的“样式不生效”，都能用这一句话解释。

## 1. 初学者必记的 3 条规则

1. **后写的覆盖先写的**：两条规则命中同一个元素、权重相同，后面的生效；
2. **ID 大于类，类大于标签**：`#id` > `.class` > `div`，数量多的一方胜出；
3. **`!important` 与行内样式是“最后手段”**：它们能赢过普通规则，但会破坏可预测性，能不用就不用。

```css
/* 规则 1：两条类选择器，后写生效 */
p {
  color: black;
}
p {
  color: blue; /* 生效 */
}

/* 规则 2：类选择器胜过标签选择器 */
p {
  color: black;
}
.text {
  color: red; /* 生效，类比标签具体 */
}
```

**讲解：** 第三条里的“行内样式”指写在 HTML `style` 属性里的样式，它不经过选择器，因此优先级高于任何普通选择器规则。

## 2. 常见场景速查表

| 场景 | 谁生效 | 原因 |
| --- | --- | --- |
| 两个相同的 `p {}` | 后写的 | 权重相同，按顺序 |
| `div` 与 `.box` 同时命中 | `.box` | 类 > 标签 |
| `.box` 与 `#main` 同时命中 | `#main` | ID > 类 |
| 十个类 vs 一个 ID | 一个 ID | ID 权重高于任意数量的类 |
| 行内样式 vs `.box` | 行内样式 | 行内样式权重最高（除 !important） |
| 带 `!important` 的 `.box` | `!important` | 反转优先级 |
| 浏览器默认样式 vs 你的规则 | 你的规则 | 作者样式 > 浏览器默认样式 |

## 3. 权重速查：四元组入门版

完整计算规则在 `css/009-PriorityCalculation`，入门阶段只需要知道三档：

| 选择器示例 | 档位 |
| --- | --- |
| `*`、`div`、`p` | 元素级（最低） |
| `.box`、`:hover`、`[type]` | 类级 |
| `#header` | ID 级（最高） |

组合选择器按“每一部分相加”：`.nav .item p` 就是“两个类 + 一个标签”，能赢过“一个类 + 一个标签”的 `.item p`。

## 4. 与 007 的分工

本课是“速查”，告诉你常见场景谁赢；`css/009-PriorityCalculation` 是“深入版”，讲四元组精确计算、`:where()`/`:is()`/`@layer` 等现代工具对优先级的改造。遇到“明明后写却不生效”“第三方库覆盖不掉”这类问题，再去读 007。

## 5. 动手试试

1. 写 `h1 { color: red; }` 和 `h1 { color: blue; }`，观察后写生效；
2. 给同一个元素加 `class="title"` 和 `id="main"`，写 `.title` 与 `#main` 两条规则，验证 ID 胜出；
3. 在 HTML 里写 `style="color: green"`，验证行内样式胜出；
4. 进阶挑战：给 `.title` 加 `!important`，看它能否赢过行内样式与 ID。

## 6. 核心知识点

> 一句话记住优先级速查：具体程度决定胜负，同样具体后写赢；ID 大于类、类大于标签，`!important` 与行内样式是例外。

- 优先级四字口诀：具体、顺序、例外；
- 相同权重看书写顺序，后写覆盖先写；
- `#id` > `.class` > `标签`，组合选择器按部分累加；
- 行内样式 > 所有普通规则；`!important` > 行内样式；
- 浏览器默认样式优先级最低，你的样式总能覆盖它；
- 遇到疑难再去读 007，本课速查足以处理日常 90% 场景。

## 7. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 用 `!important` 救火 | 会压过其它所有规则，越救越乱 | 先查权重与书写顺序，最后才用 |
| 用 ID 写组件样式 | 权重太高，后续难以覆盖 | 组件样式用类选择器 |
| 疯狂嵌套选择器 | 权重被抬升，改起来困难 | 保持选择器“短而平” |
| 后写不生效就以为缓存问题 | 多数是权重问题 | 用 DevTools Computed 面板看谁赢了 |

## 8. 扩展学习

- 选择器系统：`css/007-CSS3SelectorSystem`；
- 优先级深入版：`css/009-PriorityCalculation`；
- 样式表引入方式：`css/011-StyleSheetImportMethod`；
- 层叠层 @layer：`css/039-CascadeLayer`。

<!-- ============ 文档分隔线：007-css/013-MarginCollapse.md ============ -->

> 0基础速通：读第 0 节直觉、第 1 节核心必读（代码示例）与第 7 节综合挑战即可；第 6 章深入理解（选读）供进阶。

# margin 合并与塌陷

> 本文以 W3C CSS 规范为基础，系统阐释 CSS 盒模型中 margin 合并（margin collapsing）与 margin 塌陷（margin passing-through）的形成机理、算法推导、BFC（Block Formatting Context，块格式化上下文）触发条件及其工程化应用。内容涵盖 CSS 2.1 至 CSS Box Model Level 3/4 的演进，并对接 Bootstrap、Tailwind CSS、Material Design 等主流框架的实践范式。

---

## 0. 直觉：垂直间距为什么“少了一半”

你写了 `margin-bottom: 30px` 和 `margin-top: 20px`，心里预期间距 50px，结果只有 30px——这不是 bug，是 CSS 的“合并”规则：垂直方向的相邻外边距取最大值，不相加。

父元素和第一个子元素之间也会合并，空元素自己的上下外边距也会合并。只有水平方向不会。理解这条规则，布局间距才不会“莫名其妙地变小”。

## 1. 核心必读：代码示例
### 1.1 基础示例：相邻兄弟合并

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>相邻兄弟 margin 合并示例</title>
<style>
  /* CSS 2.1 - 相邻兄弟 margin 合并 */
  .paragraph-a {
    margin-bottom: 20px;
    background: #f0f4ff;
    padding: 10px;
  }
  .paragraph-b {
    margin-top: 30px;
    background: #fff4f0;
    padding: 10px;
  }
  /* 实际间距 = max(20, 30) = 30px，而非 50px */
</style>
</head>
<body>
  <p class="paragraph-a">段落 A（margin-bottom: 20px）</p>
  <p class="paragraph-b">段落 B（margin-top: 30px）</p>
</body>
</html>
```

**讲解：** 相邻兄弟的垂直外边距取最大值（20px 与 30px 合并为 30px），不会相加。给元素加 `padding` 或 `border` 可阻止合并（本例用 padding 展示真实间距）。

### 1.2 父子塌陷：未解决 vs 已解决

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>父子 margin 塌陷对比</title>
<style>
  /* 未解决：子元素的 margin-top 穿透父元素 */
  .parent-bad {
    background: #ffe;
  }
  .parent-bad .child {
    margin-top: 50px; /* 会塌陷到 parent 上 */
    background: #fee;
    padding: 10px;
  }

  /* 解决方案 1：display: flow-root（推荐，CSS Box Model Level 3） */
  .parent-flow-root {
    display: flow-root;
    background: #efe;
    margin-top: 80px; /* 与上方 .parent-bad 的塌陷结果分开 */
  }
  .parent-flow-root .child {
    margin-top: 50px; /* 不再塌陷 */
    background: #fee;
    padding: 10px;
  }

  /* 解决方案 2：padding-top 触发 BFC */
  .parent-padding {
    padding-top: 1px;
    background: #fee;
    margin-top: 80px;
  }
  .parent-padding .child {
    margin-top: 50px;
    background: #ffd;
    padding: 10px;
  }

  /* 解决方案 3：border-top 透明 */
  .parent-border {
    border-top: 1px solid transparent;
    background: #eef;
    margin-top: 80px;
  }
  .parent-border .child {
    margin-top: 50px;
    background: #fee;
    padding: 10px;
  }

  /* 解决方案 4：overflow: hidden（历史惯用法，有副作用） */
  .parent-overflow {
    overflow: hidden;
    background: #fef;
    margin-top: 80px;
  }
  .parent-overflow .child {
    margin-top: 50px;
    background: #fee;
    padding: 10px;
  }
</style>
</head>
<body>
  <div class="parent-bad">
    <div class="child">未解决：子 margin-top 穿透父元素</div>
  </div>
  <div class="parent-flow-root">
    <div class="child">flow-root：子 margin-top 作用于父内部</div>
  </div>
  <div class="parent-padding">
    <div class="child">padding-top: 1px：留白减少 1px</div>
  </div>
  <div class="parent-border">
    <div class="child">border-top: 1px transparent：高度增加 1px</div>
  </div>
  <div class="parent-overflow">
    <div class="child">overflow: hidden：可能裁剪溢出内容</div>
  </div>
</body>
</html>
```

**讲解：** 子元素的 `margin-top` 会穿透到父元素外；三种解法分别用 `display: flow-root`（推荐）、`padding-top: 1px`、透明 `border-top` 阻断合并。注意 `overflow: hidden` 虽然也能阻断，但可能裁剪溢出内容。

### 1.3 空块元素自身合并

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>空块元素 margin 自身合并</title>
<style>
  /* CSS 2.1 §8.3.1 第 3 条规则 */
  .empty-block {
    margin-top: 30px;
    margin-bottom: 20px;
    /* 无 border、padding、content、height → 自身合并为 30px */
    background: transparent;
  }

  .top {
    background: #e0f7fa;
    padding: 10px;
  }
  .bottom {
    background: #fce4ec;
    padding: 10px;
  }
  /* 上下两个块之间的间距 = max(30, 20) = 30px */
</style>
</head>
<body>
  <div class="top">上方块</div>
  <div class="empty-block"></div>
  <div class="bottom">下方块</div>
</body>
</html>
```

### 1.4 负 margin 的合并

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>负 margin 合并示例</title>
<style>
  .positive {
    margin-bottom: 30px;
    background: #d4edda;
    padding: 10px;
  }
  .negative {
    margin-top: -10px;
    background: #f8d7da;
    padding: 10px;
  }
  /* 合并结果 = 30 + (-10) = 20px */
  /* 视觉上 .negative 会向上移动 10px，与 .positive 形成重叠 */
</style>
</head>
<body>
  <div class="positive">margin-bottom: 30px</div>
  <div class="negative">margin-top: -10px（合并后间距 20px）</div>
</body>
</html>
```

### 1.5 自适应两栏布局（BFC 应用）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>BFC 实现自适应两栏布局</title>
<style>
  /* 经典 BFC 应用：左侧定宽浮动，右侧 BFC 自适应 */
  .layout {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
  }
  .sidebar {
    float: left;
    width: 200px;
    background: #fff3cd;
    padding: 20px;
    /* 浮动元素不参与 margin 合并 */
  }
  .main {
    overflow: hidden; /* 触发 BFC，不会被浮动元素覆盖 */
    background: #d1ecf1;
    padding: 20px;
    /* 现代 CSS 推荐改用 display: flow-root */
  }

  /* 推荐写法（CSS Box Model Level 3+） */
  .layout-modern {
    display: flex;
    gap: 20px;
  }
  .layout-modern .sidebar {
    flex: 0 0 200px;
    float: none;
  }
  .layout-modern .main {
    flex: 1;
    overflow: visible;
  }
</style>
</head>
<body>
  <h2>传统 BFC 实现</h2>
  <div class="layout">
    <div class="sidebar">侧栏（定宽 200px）</div>
    <div class="main">主内容（自适应剩余宽度）</div>
  </div>

  <h2>现代 flex 实现</h2>
  <div class="layout-modern">
    <div class="sidebar">侧栏</div>
    <div class="main">主内容</div>
  </div>
</body>
</html>
```

### 1.6 包含浮动元素（清除浮动）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>BFC 包含浮动元素</title>
<style>
  /* 未触发 BFC：父元素高度塌陷 */
  .container-bad {
    border: 2px dashed red;
  }
  .container-bad .float-item {
    float: left;
    width: 100px;
    height: 100px;
    background: #bee5eb;
    margin: 5px;
  }

  /* 触发 BFC：父元素包含浮动子元素 */
  .container-good {
    display: flow-root;
    border: 2px solid green;
    margin-top: 20px;
  }
  .container-good .float-item {
    float: left;
    width: 100px;
    height: 100px;
    background: #bee5eb;
    margin: 5px;
  }
</style>
</head>
<body>
  <h3>问题：父元素高度塌陷</h3>
  <div class="container-bad">
    <div class="float-item">1</div>
    <div class="float-item">2</div>
    <div class="float-item">3</div>
  </div>
  <p>下方文字会跑到浮动元素旁边</p>

  <h3>解决：display: flow-root</h3>
  <div class="container-good">
    <div class="float-item">1</div>
    <div class="float-item">2</div>
    <div class="float-item">3</div>
  </div>
  <p>下方文字在浮动容器下方</p>
</body>
</html>
```

### 1.7 flex / grid 内不合并

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>flex / grid 内 margin 不合并</title>
<style>
  /* flex 容器内子元素 margin 不合并 */
  .flex-container {
    display: flex;
    flex-direction: column;
    background: #e7f3ff;
    padding: 10px;
  }
  .flex-item {
    margin-bottom: 20px;
    margin-top: 20px;
    background: #b8daff;
    padding: 10px;
  }
  /* 两个 flex-item 之间的间距 = 20 + 20 = 40px，而非 max(20,20) = 20px */

  /* grid 容器同理 */
  .grid-container {
    display: grid;
    grid-template-columns: 1fr;
    background: #fff3cd;
    padding: 10px;
    margin-top: 30px;
  }
  .grid-item {
    margin-bottom: 20px;
    margin-top: 20px;
    background: #ffe69c;
    padding: 10px;
  }

  /* 推荐：使用 gap 替代 margin，更语义化 */
  .gap-container {
    display: flex;
    flex-direction: column;
    gap: 40px; /* 等价于两个 20px margin 相加 */
    background: #d4edda;
    padding: 10px;
    margin-top: 30px;
  }
  .gap-item {
    background: #c3e6cb;
    padding: 10px;
  }
</style>
</head>
<body>
  <h3>flex 容器（margin 不合并）</h3>
  <div class="flex-container">
    <div class="flex-item">Item 1（margin-top: 20 + bottom: 20）</div>
    <div class="flex-item">Item 2（与 Item 1 间距 = 40px）</div>
  </div>

  <h3>grid 容器（margin 不合并）</h3>
  <div class="grid-container">
    <div class="grid-item">Item 1</div>
    <div class="grid-item">Item 2（间距 = 40px）</div>
  </div>

  <h3>使用 gap（推荐）</h3>
  <div class="gap-container">
    <div class="gap-item">Item 1</div>
    <div class="gap-item">Item 2（间距 = gap = 40px）</div>
  </div>
</body>
</html>
```

### 1.8 企业级组件：卡片列表间距管理

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>企业级卡片列表间距管理</title>
<style>
  /* 设计令牌：CSS Variables */
  :root {
    --space-1: 0.25rem;   /* 4px */
    --space-2: 0.5rem;    /* 8px */
    --space-3: 1rem;      /* 16px */
    --space-4: 1.5rem;    /* 24px */
    --space-5: 2rem;      /* 32px */
    --space-6: 3rem;      /* 48px */
    --card-radius: 12px;
    --card-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    --color-bg: #f8f9fa;
    --color-card: #ffffff;
    --color-text: #212529;
  }

  body {
    margin: 0;
    background: var(--color-bg);
    color: var(--color-text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.6;
  }

  /* 容器：使用 grid + gap，完全规避 margin 合并 */
  .card-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: var(--space-4);
    padding: var(--space-5);
    max-width: 1200px;
    margin: 0 auto;
  }

  /* 卡片组件：内部使用 margin 时需注意父子关系 */
  .card {
    background: var(--color-card);
    border-radius: var(--card-radius);
    box-shadow: var(--card-shadow);
    overflow: hidden; /* 触发 BFC，包含浮动内容 */
    display: flex;
    flex-direction: column;
  }

  .card-media {
    width: 100%;
    height: 180px;
    background: linear-gradient(135deg, #667eea, #764ba2);
  }

  .card-body {
    padding: var(--space-4);
    /* 不使用 margin-top，避免与 card-media 合并 */
  }

  .card-title {
    margin: 0 0 var(--space-2) 0;
    font-size: 1.125rem;
    font-weight: 600;
  }

  .card-text {
    margin: 0 0 var(--space-3) 0;
    color: #6c757d;
    font-size: 0.875rem;
  }

  .card-action {
    margin-top: auto; /* flex 中 auto margin 实现底部对齐 */
    padding-top: var(--space-3);
  }

  .btn {
    display: inline-block;
    padding: var(--space-2) var(--space-3);
    background: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 0.875rem;
    cursor: pointer;
    text-decoration: none;
  }

  .btn:hover {
    background: #0056b3;
  }
</style>
</head>
<body>
  <div class="card-list">
    <article class="card">
      <div class="card-media"></div>
      <div class="card-body">
        <h3 class="card-title">卡片标题 1</h3>
        <p class="card-text">这是卡片的描述文字。使用 grid + gap 管理间距，避免 margin 合并陷阱。</p>
        <div class="card-action">
          <a href="#" class="btn">查看详情</a>
        </div>
      </div>
    </article>

    <article class="card">
      <div class="card-media"></div>
      <div class="card-body">
        <h3 class="card-title">卡片标题 2</h3>
        <p class="card-text">卡片内部使用 flex 布局，margin 不合并，间距精确可控。</p>
        <div class="card-action">
          <a href="#" class="btn">查看详情</a>
        </div>
      </div>
    </article>

    <article class="card">
      <div class="card-media"></div>
      <div class="card-body">
        <h3 class="card-title">卡片标题 3</h3>
        <p class="card-text">使用 margin-top: auto 将按钮推到底部，实现等高卡片布局。</p>
        <div class="card-action">
          <a href="#" class="btn">查看详情</a>
        </div>
      </div>
    </article>
  </div>
</body>
</html>
```

### 1.9 margin-trim 属性（实验性）

```css
/* CSS Box Model Level 4 - Editor's Draft */
/* 浏览器支持：截至 2024 年仅 Safari Preview 实现 */

.card-container {
  margin-trim: block; /* 修剪子元素超出容器的 block 方向 margin */
}

.card-container > .card:first-child {
  /* 不需要写 margin-block-start: 0 */
  /* margin-trim: block 会自动修剪 */
}
```

> **注意**：`margin-trim` 仍处于实验阶段，生产环境请使用 `:first-child` / `:last-child` 显式重置或 `gap` 替代。

### 1.10 调试技巧：可视化 margin

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>margin 可视化调试</title>
<style>
  /* 使用 outline 而非 border 调试，因为 outline 不影响布局 */
  .debug * {
    outline: 1px dashed red;
  }
  /* 在 DevTools 中开启「Show margin」更直观 */
</style>
</head>
<body class="debug">
  <div style="margin: 20px; padding: 10px;">调试元素</div>
</body>
</html>
```

---

## 2. 对比分析
### 2.1 margin 合并解决方案对比

| 方案 | CSS 版本 | 优点 | 缺点 | 推荐场景 |
| --- | --- | --- | --- | --- |
| `display: flow-root` | CSS Box Model L3 | 语义清晰，无副作用 | IE 不支持（需 polyfill） | 现代浏览器首选 |
| `overflow: hidden` | CSS 2.1 | 兼容性极好 | 裁剪溢出内容、影响 sticky 定位 | 兼容老项目 |
| `padding-top: 1px` | CSS 2.1 | 兼容性极好 | 占用 1px 空间 | 精确像素控制场景 |
| `border-top: 1px transparent` | CSS 2.1 | 兼容性极好 | 占用 1px 空间 | 类似 padding |
| `display: flex/grid` | CSS3 | 完全规避合并 | 改变布局语义 | 已使用 flex/grid 时 |
| `gap` | CSS Grid/Flex L1 | 语义化，间距统一 | 旧浏览器不支持 | 现代间距管理首选 |
| `margin-trim` | CSS Box Model L4 | 自动修剪 | 实验性，支持差 | 实验项目 |

### 2.2 与其他布局系统的对比

| 布局系统 | margin 合并行为 | 间距管理方式 | 兼容性 |
| --- | --- | --- | --- |
| Normal flow（block） | 合并 | margin | 全部 |
| Float | 不合并（脱离流） | margin + clearfix | 全部 |
| Flexbox | 不合并 | margin / gap | IE10+ |
| Grid | 不合并 | margin / gap | IE 不支持（部分） |
| Position absolute | 不合并（脱离流） | top/left/right/bottom | 全部 |
| Multi-column | 不合并 | column-gap | IE10+ |
| Tailwind CSS | 取决于类名 | 空间类（`space-y-*`、`gap-*`） | 现代浏览器 |
| Bootstrap | 取决于类名 | utility + spacer | 现代浏览器 |

### 2.3 Tailwind CSS 的间距管理

Tailwind 提供了两套间距管理方案：

```html
<!-- 方案 1：space-y-*（基于 :not(:first-child) selector 加 margin-top） -->
<div class="space-y-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
<!-- 渲染：每个子元素（除第一个外）margin-top: 1rem -->

<!-- 方案 2：gap-*（基于 flex/grid 容器的 gap 属性） -->
<div class="flex flex-col gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
<!-- 渲染：容器 gap: 1rem，子元素无需 margin -->
```

`space-y-*` 在常规流中依然受 margin 合并影响（虽然 Tailwind 的实现通过 `:not(:first-child)` 巧妙规避了相邻兄弟合并），但 `gap-*` 完全无此问题。Tailwind v3+ 推荐 `gap-*`。

### 2.4 Bootstrap 的间距管理

Bootstrap 5 使用 `$spacers` SCSS map 生成 `m-*`、`p-*`、`mt-*`、`mb-*` 等 utility 类：

```html
<!-- Bootstrap 5 -->
<div class="mb-3">margin-bottom: 1rem</div>
<div class="mt-3">margin-top: 1rem</div>
<!-- 两个元素间距 = max(1rem, 1rem) = 1rem（合并） -->

<!-- 推荐改用 g-*（gap） -->
<div class="row g-3">
  <div class="col">Item 1</div>
  <div class="col">Item 2</div>
</div>
```

### 2.5 Material Design 的间距系统

Material Design 3 使用 4dp 基准网格，推荐使用 padding 而非 margin 管理组件内部间距，使用 gap 管理组件之间间距：

```css
/* Material Design 3 风格 */
.md-card {
  padding: 16px; /* 内部使用 padding */
}
.md-card-list {
  display: flex;
  flex-direction: column;
  gap: 8px; /* 组件间使用 gap */
}
```

### 2.6 BEM 命名与 margin 合并

BEM 方法论通过明确的层级关系规避了 margin 合并的复杂性：

```html
<!-- BEM 结构 -->
<div class="card-list">
  <div class="card-list__item">
    <div class="card">
      <div class="card__title">标题</div>
      <div class="card__body">内容</div>
    </div>
  </div>
</div>

<style>
  .card-list {
    display: flex;
    flex-direction: column;
    gap: 16px; /* BEM 推荐使用 gap 而非 __item 上的 margin */
  }
  .card {
    padding: 16px;
  }
  .card__title {
    margin: 0 0 8px 0;
  }
  .card__body {
    margin: 0;
  }
</style>
```

---

## 3. 常见陷阱与最佳实践
### 3.1 陷阱 1：误以为水平 margin 也会合并

**错误认知**：

```css
/* 期望两个 inline-block 元素水平方向 margin 合并 */
.a { display: inline-block; margin-right: 20px; }
.b { display: inline-block; margin-left: 30px; }
/* 实际间距 = 20 + 30 = 50px（不合并） */
```

**正确认知**：margin 合并只发生在块级元素的垂直方向。inline-block、inline 元素的水平 margin 永不合并。

### 3.2 陷阱 2：flex 子元素 margin 误判

**错误代码**：

```css
.flex-container {
  display: flex;
  flex-direction: column;
}
.flex-item {
  margin-bottom: 20px;
}
.flex-item:last-child {
  /* 期望 margin-bottom 合并消失 */
}
```

**问题**：flex 容器内 margin 不合并，最后一个子元素的 `margin-bottom: 20px` 会撑大容器高度。

**解决方案**：

```css
/* 方案 1：使用 :last-child 重置 */
.flex-item:last-child {
  margin-bottom: 0;
}

/* 方案 2：使用 gap（推荐） */
.flex-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.flex-item {
  margin-bottom: 0;
}
```

### 3.3 陷阱 3：`overflow: hidden` 的副作用

**问题代码**：

```css
.container {
  overflow: hidden; /* 触发 BFC，解决塌陷 */
}
.container .sticky-child {
  position: sticky;
  top: 0;
  /* sticky 失效！因为 overflow: hidden 创建了新的滚动容器 */
}
```

**解决方案**：

```css
.container {
  display: flow-root; /* 现代方案，无副作用 */
}
```

### 3.4 陷阱 4：负 margin 滥用

**反模式**：

```css
/* 用负 margin 实现重叠效果 */
.hero {
  margin-bottom: -50px;
  z-index: 1;
}
.content {
  margin-top: 0;
  /* 视觉上 content 与 hero 重叠 50px */
}
```

**问题**：
- 难以维护，间距计算复杂。
- 在响应式布局中容易错乱。
- 影响 accessibility（屏幕阅读器可能误读顺序）。

**推荐方案**：

```css
/* 使用 grid 或 transform 替代 */
.layout {
  display: grid;
  grid-template-rows: auto auto;
}
.hero {
  grid-row: 1;
}
.content {
  grid-row: 2;
  transform: translateY(-50px); /* 视觉重叠，不影响布局 */
}
```

### 3.5 陷阱 5：reset CSS 的过度使用

**问题代码**：

```css
* {
  margin: 0;
  padding: 0;
}
```

**问题**：
- 重置所有元素的 margin 后，浏览器默认排版美感消失（如 `<p>` 之间无间距）。
- 需要手动为所有元素设置 margin，工作量增加。
- 现代项目中应使用 normalize.css 或 modern-normalize 替代。

**推荐方案**：

```css
/* 使用 modern-normalize */
/* 或自定义最小化 reset */
*, *::before, *::after {
  box-sizing: border-box;
}

body {
  margin: 0;
  line-height: 1.6;
}

p, h1, h2, h3, h4, h5, h6 {
  margin: 0;
  /* 通过设计系统的 spacing scale 显式管理 */
}
```

### 3.6 最佳实践清单

1. **优先使用 `gap`**：在 flex/grid 容器中，使用 `gap` 替代子元素的 `margin`。
2. **首选 `display: flow-root`**：解决塌陷问题时，避免 `overflow: hidden`。
3. **避免 ID 选择器配合 margin**：高优先级使 margin 难以覆盖。
4. **设计令牌统一管理**：使用 CSS Variables 定义 spacing scale（如 `--space-1` 到 `--space-6`）。
5. **组件内使用 padding，组件间使用 gap**：明确职责边界。
6. **避免负 margin**：除非有明确的设计意图（如吸附效果）。
7. **响应式间距**：使用 `clamp()` 实现流式间距。
8. **自动化测试**：使用 Playwright + 视觉回归检测非预期 margin 变化。
9. **代码评审 checklist**：检查 BFC 触发方式、flex/grid 内的 margin 使用、负 margin 的合理性。
10. **文档化间距系统**：在设计系统文档中明确 margin 使用规范。

### 3.7 兼容性参考

| 特性 | Chrome | Firefox | Safari | Edge | IE |
| --- | --- | --- | --- | --- | --- |
| margin 合并 | 全部 | 全部 | 全部 | 全部 | 全部 |
| `display: flow-root` | 58+ | 53+ | 13+ | 79+ | 不支持 |
| `gap`（flex） | 84+ | 63+ | 14.1+ | 84+ | 不支持 |
| `gap`（grid） | 66+ | 61+ | 12+ | 79+ | 不支持 |
| 逻辑属性 `margin-block-*` | 87+ | 66+ | 14.1+ | 87+ | 不支持 |
| `margin-trim` | 不支持 | 不支持 | 部分支持 | 不支持 | 不支持 |

---

## 4. 工程实践
### 4.1 PostCSS 配置：自动重置首尾 margin

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      grid: true,
    }),
    require('postcss-preset-env')({
      stage: 2,
      features: {
        'margin-trim': true, // 实验性启用
      },
    }),
  ],
};
```

### 4.2 设计令牌：CSS Variables 间距系统

```css
:root {
  /* 4px 基准网格 */
  --space-0: 0;
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.5rem;    /* 24px */
  --space-6: 2rem;      /* 32px */
  --space-7: 3rem;      /* 48px */
  --space-8: 4rem;      /* 64px */
  --space-9: 6rem;      /* 96px */
  --space-10: 8rem;     /* 128px */
}

/* 流式间距：clamp(min, preferred, max) */
.hero-spacing {
  margin-top: clamp(var(--space-5), 5vw, var(--space-8));
}
```

### 4.3 SCSS 工具函数

```scss
// _spacing.scss
$space-scale: (
  0: 0,
  1: 0.25rem,
  2: 0.5rem,
  3: 0.75rem,
  4: 1rem,
  5: 1.5rem,
  6: 2rem,
  7: 3rem,
  8: 4rem,
);

@function space($key) {
  @return map-get($space-scale, $key);
}

@mixin stack($size) {
  display: flex;
  flex-direction: column;
  gap: space($size);
}

// 使用
.card-list {
  @include stack(4); // gap: 1rem
}
```

### 4.4 Tailwind 自定义间距

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      spacing: {
        '4px': '4px',
        '8px': '8px',
        '12px': '12px',
        '16px': '16px',
        '24px': '24px',
        '32px': '32px',
        '48px': '48px',
        '64px': '64px',
      },
    },
  },
};
```

### 4.5 性能优化

1. **避免布局抖动**：频繁修改 margin 会触发 reflow，应使用 transform 替代。
2. **使用 `will-change: margin`**：对动画元素的 margin 加速合成（谨慎使用）。
3. **减少 DOM 嵌套**：深层嵌套加剧 margin 合并的复杂性。
4. **批量修改**：使用 `requestAnimationFrame` 批量修改 margin。
5. **CSS Containment**：使用 `contain: layout` 隔离组件，减少 reflow 范围。

```css
.component {
  contain: layout; /* 隔离布局，避免 margin 影响外部 */
}
```

### 4.6 调试工具

1. **Chrome DevTools**：开启「Show margin」可视化。
2. **Firefox DevTools**：盒模型可视化面板。
3. **Safari Web Inspector**：层叠上下文与盒模型检查。
4. **VS Code 插件**：CSS Peek、IntelliSense for CSS。
5. **PostCSS 插件**：`postcss-reporter` 提示潜在问题。

### 4.7 自动化测试

```javascript
// visual-regression.test.js
const { test, expect } = require('@playwright/test');

test('card-list 间距正确', async ({ page }) => {
  await page.goto('http://localhost:3000/card-list');

  // 获取第一个卡片的位置
  const firstCard = await page.locator('.card').first().boundingBox();
  const secondCard = await page.locator('.card').nth(1).boundingBox();

  // 验证间距 = 24px（gap: 1.5rem）
  const gap = secondCard.y - (firstCard.y + firstCard.height);
  expect(gap).toBeCloseTo(24, 0.5);
});
```

### 4.8 ESLint 规则（CSS-in-JS）

```javascript
// .stylelintrc.js
module.exports = {
  rules: {
    'declaration-block-no-shorthand-property-overrides': true,
    'property-disallowed-list': {
      // 禁止在 flex/grid 容器内使用 margin
      '/margin/': null,
    },
    'selector-max-id': 0,
  },
  overrides: [
    {
      files: ['**/*.flex.css', '**/*.grid.css'],
      rules: {
        'comment-word-disallowed-list': [['TODO', 'FIXME'], { severity: 'warning' }],
      },
    },
  ],
};
```

---

## 5. 案例研究
### 5.1 案例一：Bootstrap 5 的间距系统

Bootstrap 5 通过 SCSS map 生成间距工具类：

```scss
// bootstrap/scss/_variables.scss
$spacers: (
  0: 0,
  1: $spacer * 0.25,
  2: $spacer * 0.5,
  3: $spacer,
  4: $spacer * 1.5,
  5: $spacer * 3,
);

// bootstrap/scss/_spacing.scss
@each $key, $value in $spacers {
  .m-#{$key} { margin: $value !important; }
  .mt-#{$key} { margin-top: $value !important; }
  .mb-#{$key} { margin-bottom: $value !important; }
  .my-#{$key} {
    margin-top: $value !important;
    margin-bottom: $value !important;
  }
}
```

**分析**：
- Bootstrap 5 推荐使用 `g-*`（gap）替代 `m-*`。
- `mb-3` 与下一个元素的 `mt-3` 会合并为 `1rem`，而非 `2rem`。
- 在 `.row` 容器内使用 `g-3` 完全规避合并问题。

### 5.2 案例二：Tailwind CSS 的 `space-y-*` 实现

Tailwind 的 `space-y-*` 通过 `:not(:first-child) > *` 选择器实现：

```css
/* Tailwind v3 生成的 CSS */
.space-y-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1rem * var(--tw-space-y-reverse));
}
```

**分析**：
- 使用 `:not([hidden]) ~ :not([hidden])` 选择器，对每个非第一个子元素加 `margin-top`。
- 巧妙规避了相邻兄弟 margin 合并（因为只有 `margin-top`，无相邻 `margin-bottom`）。
- 但在嵌套场景下可能出现问题（如 `.space-y-4` 内部嵌套 `.space-y-2`）。
- Tailwind v3.3+ 推荐使用 `gap-*` 替代。

### 5.3 案例三：Material Design 3 的间距规范

Material Design 3 定义了 5 级间距系统：

| 等级 | 值 | 用途 |
| --- | --- | --- |
| Small | 4dp | 紧凑组件内部 |
| Medium | 8dp | 标准组件内部 |
| Large | 16dp | 组件之间 |
| XLarge | 24dp | 区块之间 |
| XXLarge | 32dp | 大区块之间 |

```css
/* Material Design 3 实现 */
.md3-spacing {
  /* 使用 CSS Variables */
  --md3-spacing-small: 4px;
  --md3-spacing-medium: 8px;
  --md3-spacing-large: 16px;
}

.md3-card {
  padding: var(--md3-spacing-large);
}

.md3-card-list {
  display: flex;
  flex-direction: column;
  gap: var(--md3-spacing-large);
}
```

### 5.4 案例四：GitHub Primer 的间距系统

GitHub Primer 使用 8px 基准网格，定义了完整的 spacing scale：

```css
.primer-spacing {
  --spacing-0: 0;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 16px;
  --spacing-4: 24px;
  --spacing-5: 32px;
  --spacing-6: 40px;
  --spacing-7: 48px;
}
```

Primer 推荐使用 `gap` 管理组件间距，使用 `padding` 管理组件内部间距，避免使用 `margin`。

### 5.5 案例五：Ant Design 的间距系统

Ant Design v5 使用 8px 基准：

```typescript
// antd/theme/index.ts
export const theme = {
  token: {
    marginXS: 8,
    marginSM: 12,
    margin: 16,
    marginMD: 20,
    marginLG: 24,
    marginXL: 32,
  },
};
```

Ant Design 的 `<Space>` 组件内部使用 flex + `gap`，规避了 margin 合并问题。

### 5.6 案例六：真实生产事故

**场景**：某电商网站商品列表页面，在 Safari 浏览器中商品卡片间距比 Chrome 大 16px。

**原因**：
- 使用了 `margin-top` 管理卡片间距。
- 容器未触发 BFC，导致首个卡片的 `margin-top` 塌陷到容器外。
- Safari 与 Chrome 对「父元素与首个子元素」margin 合并的实现细节略有差异。

**解决方案**：
- 改用 `display: grid; gap: 16px;` 管理间距。
- 移除所有子元素的 `margin-top`。

**经验教训**：
- 跨浏览器测试不可或缺。
- 现代布局方案（flex/grid + gap）能规避大量兼容性问题。

---

### 填空题知识点讲解

**题目 1**：CSS 2.1 §___ 中正式定义了 margin collapsing 的 4 条规则。

**解析讲解**：8.3.1

**解析讲解**：CSS 2.1 第 8 章是盒模型，§8.3.1 标题为「Collapsing margins」，给出了 4 条精确规则。

**题目 2**：margin 合并只在________方向发生，水平方向不合并。

**解析讲解**：垂直（block 方向）

**解析讲解**：在水平书写模式下，margin 合并只发生在垂直方向（margin-top 与 margin-bottom）。在垂直书写模式下（如 `writing-mode: vertical-rl`），合并方向相应改变。

**题目 3**：触边 BFC 的现代推荐属性是________。

**解析讲解**：`display: flow-root`

**解析讲解**：`display: flow-root` 是 CSS Box Model Level 3 专为触发 BFC 设计的属性，无 `overflow: hidden` 的副作用。

**题目 4**：负 margin 合并的规则是________。

**解析讲解**：最大正 margin + 最小负 margin（即正负相加）

**解析讲解**：当参与合并的 margin 含负值时，规则为「最大正值 + 最小负值」。例如 `margin-bottom: 30px` 与 `margin-top: -10px` 合并为 `30 + (-10) = 20px`。

**题目 5**：flex 容器内的子元素之间________（会/不会）发生 margin 合并。

**解析讲解**：不会

**解析讲解**：CSS Flexbox §4.2 明确规定，flex item 之间的 margin 不会折叠。

### 编程题知识点讲解

**题目 1**：实现一个垂直堆叠的卡片列表，要求：

1. 卡片间距为 16px。
2. 完全规避 margin 合并。
3. 支持响应式（移动端单列、桌面端两列）。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>响应式卡片列表</title>
<style>
  /* 设计令牌 */
  :root {
    --space-4: 1rem;     /* 16px */
    --space-5: 1.5rem;   /* 24px */
    --color-bg: #f8f9fa;
    --color-card: #ffffff;
  }

  body {
    margin: 0;
    padding: var(--space-5);
    background: var(--color-bg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  /* 使用 grid + gap 完全规避 margin 合并 */
  .card-list {
    display: grid;
    grid-template-columns: 1fr; /* 移动端单列 */
    gap: var(--space-4);
    max-width: 1200px;
    margin: 0 auto;
  }

  /* 响应式：桌面端两列 */
  @media (min-width: 768px) {
    .card-list {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  /* 卡片样式 */
  .card {
    background: var(--color-card);
    padding: var(--space-4);
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .card-title {
    margin: 0 0 var(--space-4) 0;
    font-size: 1.25rem;
  }

  .card-text {
    margin: 0;
    color: #6c757d;
    line-height: 1.6;
  }
</style>
</head>
<body>
  <div class="card-list">
    <article class="card">
      <h2 class="card-title">卡片 1</h2>
      <p class="card-text">这是卡片内容。使用 grid + gap 管理间距。</p>
    </article>
    <article class="card">
      <h2 class="card-title">卡片 2</h2>
      <p class="card-text">完全规避 margin 合并陷阱。</p>
    </article>
    <article class="card">
      <h2 class="card-title">卡片 3</h2>
      <p class="card-text">响应式布局：移动端单列，桌面端两列。</p>
    </article>
    <article class="card">
      <h2 class="card-title">卡片 4</h2>
      <p class="card-text">间距精确可控，跨浏览器一致。</p>
    </article>
  </div>
</body>
</html>
```

**评分要点**：
- 使用 `display: grid` + `gap`（+10 分）
- 使用 `@media` 响应式（+5 分）
- 卡片内部使用 padding 而非 margin（+5 分）
- 文字与标题使用 margin-bottom + margin: 0 重置（+5 分）

**题目 2**：修复以下代码中的 margin 塌陷问题（不改变视觉效果）：

```html
<div class="container">
  <div class="box">内容</div>
</div>

<style>
  .container {
    background: #f0f0f0;
  }
  .box {
    margin-top: 30px;
    background: #fff;
    padding: 20px;
  }
</style>
```

```html
<div class="container">
  <div class="box">内容</div>
</div>

<style>
  .container {
    display: flow-root; /* 触发 BFC，阻止 margin 塌陷 */
    background: #f0f0f0;
  }
  .box {
    margin-top: 30px;
    background: #fff;
    padding: 20px;
  }
</style>
```

**其他可行方案**：
- `.container { overflow: hidden; }`（有副作用，不推荐）
- `.container { padding-top: 1px; }`（占用 1px 空间）
- `.container { border-top: 1px solid transparent; }`（占用 1px 空间）

**题目 3**：实现一个自适应两栏布局，左侧定宽 200px，右侧自适应剩余宽度。要求：

1. 不使用 flex 或 grid。
2. 利用 BFC 特性。
3. 左右两栏间距 20px。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>BFC 两栏布局</title>
<style>
  .layout {
    max-width: 1200px;
    margin: 0 auto;
  }
  .sidebar {
    float: left;
    width: 200px;
    margin-right: 20px;
    background: #fff3cd;
    padding: 20px;
  }
  .main {
    overflow: hidden; /* 触发 BFC，不被浮动元素覆盖 */
    background: #d1ecf1;
    padding: 20px;
  }
</style>
</head>
<body>
  <div class="layout">
    <div class="sidebar">侧栏（200px）</div>
    <div class="main">主内容（自适应）</div>
  </div>
</body>
</html>
```

**解析讲解**：
- 左侧 `float: left` 脱离文档流，但保留宽度。
- 右侧 `overflow: hidden` 触发 BFC，BFC 不会与浮动元素重叠，因此自动占据剩余宽度。
- 通过 `margin-right: 20px` 实现间距（浮动元素之间不合并，间距准确）。

### 10.1 W3C 规范

[1] World Wide Web Consortium. 2011. *Cascading Style Sheets Level 2 Revision 1 (CSS 2.1) Specification*. W3C Recommendation. Retrieved from https://www.w3.org/TR/CSS21/box.html#collapsing-margins

[2] Elika Etemad. 2018. *CSS Box Model Module Level 3*. W3C Working Draft. Retrieved from https://www.w3.org/TR/css-box-3/

[3] Elika Etemad. 2024. *CSS Box Model Module Level 4*. W3C Editor's Draft. Retrieved from https://drafts.csswg.org/css-box-4/

[4] Tab Atkins Jr. and Elika Etemad. 2023. *CSS Flexbox Layout Module Level 1*. W3C Candidate Recommendation. Retrieved from https://www.w3.org/TR/css-flexbox-1/

[5] Tab Atkins Jr. and Elika Etemad. 2023. *CSS Grid Layout Module Level 1*. W3C Recommendation. Retrieved from https://www.w3.org/TR/css-grid-1/

[6] Elika Etemad and Tab Atkins Jr. 2022. *CSS Logical Properties and Values Level 1*. W3C Candidate Recommendation. Retrieved from https://www.w3.org/TR/css-logical-1/

### 10.2 学术论文

[7] Lie, H. W. and Bos, B. 1999. *Cascading Style Sheets: Designing for the Web*. Addison-Wesley Professional, Boston, MA, USA. DOI: 10.5555/298544

[8] Meyer, E. A. 2006. *Cascading Style Sheets: The Definitive Guide*. O'Reilly Media, Sebastopol, CA, USA. DOI: 10.5555/1197574

[9] Bos, B., Lie, H. W., Lilley, C., and Jacobs, I. 1999. *Cascading Style Sheets, Level 2: CSS2 Specification*. W3C Recommendation. Retrieved from https://www.w3.org/TR/CSS2/

### 10.4 框架文档

[14] Bootstrap Team. 2024. *Bootstrap 5 Spacing*. Retrieved from https://getbootstrap.com/docs/5.3/utilities/spacing/

[15] Tailwind Labs. 2024. *Tailwind CSS Spacing*. Retrieved from https://tailwindcss.com/docs/customizing-spacing

[16] Google. 2024. *Material Design 3 Spacing*. Retrieved from https://m3.material.io/foundations/design-tokens/spacing

[17] Ant Group. 2024. *Ant Design Spacing*. Retrieved from https://ant.design/docs/react/customize-theme

### 10.5 引用规范

本文引用遵循 ACM Reference Format：

> Author(s). Year. *Title*. Publisher/Venue. DOI or URL.

示例：
> Etemad, E. 2018. CSS Box Model Module Level 3. W3C Working Draft. Retrieved from https://www.w3.org/TR/css-box-3/

---

### 11.1 书籍

1. **《CSS Secrets》** — Lea Verou 著
   - 深入讲解 CSS 的高级技巧与原理，包含 margin 合并的巧妙应用。

2. **《CSS: The Definitive Guide》** — Eric A. Meyer 著
   - CSS 权威指南，第 4 版，全面覆盖 CSS 2.1 至 CSS3。

3. **《CSS in Depth》** — Keith J. Grant 著
   - 现代 CSS 实战指南，深入盒模型、层叠、布局等主题。

4. **《Every Layout》** — Heydon Pickering 与 Andy Bell 著
   - 重新思考布局模式，包含 BFC、flex、grid 的最佳实践。

5. **《The CSS Handbook》** — Flavio Copes 著
   - CSS 实用手册，适合快速查阅。

### 11.2 论文与文章

1. **Håkon Wium Lie. 2005. *Cascading Style Sheets*. PhD Thesis, University of Oslo.**
   - CSS 的起源论文，阐述了 CSS 设计哲学。

2. **Bert Bos. 1999. *CSS3 Roadmap*.**
   - CSS3 模块化设计的早期规划。

3. **Elika Etemad. 2017. *CSS Box Model: Status and Direction*.**
   - Box Model 模块的演进方向。

### 11.4 视频课程

1. **CSS for JavaScript Developers** — Josh W. Comeau
   - 面向 JS 开发者的 CSS 深度课程。

2. **Frontend Masters: CSS Grid & Flexbox for Responsive Layouts** — Jen Kramer
   - 现代布局系统实战。

3. **CSS Animation 101** — Donovan Hutchinson
   - CSS 动画与过渡系统。

### 11.5 工具与资源

1. **PostCSS** — https://postcss.org/
   - CSS 后处理器，可编写插件自动处理 margin 合并问题。

2. **Stylelint** — https://stylelint.io/
   - CSS 静态分析工具，可配置规则禁止危险 margin 用法。

3. **Tailwind CSS** — https://tailwindcss.com/
   - 原子化 CSS 框架，内置间距管理系统。

4. **Storybook** — https://storybook.js.org/
   - 组件开发与文档化工具，便于测试间距一致性。

5. **Chromatic** — https://www.chromatic.com/
   - 视觉回归测试服务，可检测间距变化。

6. **Figma Tokens Plugin** — https://figmatokens.com/
   - Figma 设计令牌管理插件，与 CSS Variables 同步。

---

## 6. 深入理解（选读）

> 以下内容适合想彻底搞懂机制原理的读者，第一遍学习可跳过。

### 6.1 历史演进

### 6.1.1 CSS 1（1996）：margin 的诞生

CSS 1 由 Håkon Wium Lie 与 Bert Bos 于 1996 年提出，首次引入盒模型概念。此时 margin 作为「盒之间的空气」被定义，但其行为并未严格规范化。浏览器实现各异，导致「为什么两个段落之间的间距是 30px 而不是 60px」成为早期 Web 开发者最常见的困惑之一。

CSS 1 规范中对 margin collapsing 的描述仅有寥寥几句：

> Adjacent vertical margins are collapsed. The resulting margin is the maximum of the adjacent margins.

这一含糊表述为后续十多年的兼容性问题埋下伏笔。

### 6.1.2 CSS 2.1（2011）：规范的明确化

CSS 2.1 §8.3.1「Collapsing margins」正式给出 4 条精确规则：

1. **相邻兄弟**：常规流中两个块级元素的垂直 margin 合并。
2. **父与首个/末尾子**：若父元素没有 `border-top`、`padding-top`，且子元素没有 `clear`，则父的 `margin-top` 与子的 `margin-top` 合并；末尾同理。
3. **空块自身**：若块级元素没有 `border`、`padding`、`height`、`min-height`、内联内容、`clear`，则其自身的 `margin-top` 与 `margin-bottom` 合并。
4. 合并后的值为两者中的较大者（若一者为负，则为正负相加）。

### 6.1.3 CSS 3 模块化（2010s）：Box Model Level 3

CSS3 将规范拆分为独立模块，margin 行为归入 [CSS Box Model Module Level 3](https://www.w3.org/TR/css-box-3/)。该模块在 CSS 2.1 基础上做了少量澄清：

- 明确 flex / grid 容器内部不发生 margin 合并。
- 引入逻辑属性（`margin-inline-start`、`margin-block-start`）以适应竖排与 RTL 文档。
- 对 `margin: auto` 在 flex 项上的行为做了重新定义（用于实现居中对齐）。

### 6.1.4 CSS Box Model Level 4 与 Houdini（2020s）

Level 4 草案引入 `margin-trim` 属性，允许容器「修剪」子元素伸出到容器外的 margin：

```css
/* CSS Box Model Level 4，2024 年仍在 Editor's Draft 阶段 */
.container {
  margin-trim: block;
}
.container > .first-child {
  margin-block-start: 0; /* 自动修剪 */
}
```

Houdini 的 `CSS Layout API` 与 `CSS Properties and Values API` 进一步提供了底层能力，使开发者可以介入渲染管线，理论上可以自定义 margin 合并算法（虽然实践中极少使用）。

### 6.1.5 演进时间线

| 年份 | 规范/事件 | 核心变化 |
| --- | --- | --- |
| 1996 | CSS 1 | margin 概念诞生，合并行为未严格定义 |
| 1998 | CSS 2 | 引入 BFC 概念雏形（虽未正式命名） |
| 2011 | CSS 2.1 | §8.3.1 给出 4 条合并规则 |
| 2015 | CSS Flexbox | flex 容器内部 margin 不合并 |
| 2017 | CSS Grid | grid 容器内部 margin 不合并，引入 `gap` |
| 2018 | CSS Box Model Level 3 | 引入逻辑属性 `margin-block-*` |
| 2020 | `display: flow-root` 普及 | 取代 `overflow: hidden` 作为 BFC 触发首选 |
| 2023 | CSS Box Model Level 4 | `margin-trim` 进入 Editor's Draft |
| 2024+ | Houdini | 提供自定义布局能力，理论可介入合并算法 |

---

### 6.2 形式化定义

### 6.2.1 规范条款

依据 [CSS 2.1 §8.3.1](https://www.w3.org/TR/CSS21/box.html#collapsing-margins) 与 [CSS Box Model Level 3](https://www.w3.org/TR/css-box-3/#margins)：

> In CSS, the adjoining margins of two or more boxes (which might or might not be siblings) can combine to form a single margin. Margins that combine this way are said to *collapse*, and the resulting combined margin is called a *collapsed margin*.

### 6.2.2 核心术语

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 外边距 | margin | 围绕元素边框的透明区域 |
| 合并 | collapsing | 相邻 margin 归并为单一 margin |
| 塌陷 | passing-through（非规范术语） | 子元素 margin 穿透父元素边界的现象 |
| 邻接 | adjoining | 两个 margin 之间没有 `border`、`padding`、`inline content`、`clearance` 阻隔 |
| 块格式化上下文 | BFC, Block Formatting Context | 一个独立的渲染区域，内部元素的布局不影响外部 |
| 常规流 | normal flow | 非 float、非 position:absolute/fixed 的元素流 |

### 6.2.3 合并发生的必要条件

margin 合并必须**同时**满足以下条件：

1. **块级盒子**：参与合并的必须是 block-level boxes，inline-level boxes 不参与。
2. **垂直方向**：仅 `margin-top` 与 `margin-bottom` 合并，`margin-left` 与 `margin-right` 永不合并（在水平书写模式下）。
3. **常规流**：浮动元素、绝对定位元素、根元素 `html` 的 margin 不与任何元素合并。
4. **邻接**：两个 margin 之间无 `border`、`padding`、`inline content`、`clearance` 阻隔。
5. **非 flex/grid 容器**：flex item 与 grid item 之间不合并。

### 6.2.4 形式化判定函数

设 $M_1$ 与 $M_2$ 为两个 margin，定义合并判定函数 $\text{Collapse}(M_1, M_2)$：

$$
\text{Collapse}(M_1, M_2) =
\begin{cases}
\text{true}, & \text{if } \text{BlockLevel}(M_1) \wedge \text{BlockLevel}(M_2) \\
& \quad \wedge \text{Adjoining}(M_1, M_2) \\
& \quad \wedge \text{InNormalFlow}(M_1) \wedge \text{InNormalFlow}(M_2) \\
& \quad \wedge \neg\text{FlexGridItem}(M_1) \wedge \neg\text{FlexGridItem}(M_2) \\
\text{false}, & \text{otherwise}
\end{cases}
$$

合并后的值为：

$$
M_{\text{collapsed}} =
\begin{cases}
\max(M_1, M_2), & \text{if } M_1 \geq 0 \wedge M_2 \geq 0 \\
\min(M_1, M_2), & \text{if } M_1 \leq 0 \wedge M_2 \leq 0 \\
M_1 + M_2, & \text{otherwise (一正一负)}
\end{cases}
$$

### 6.2.5 BFC 触发条件

| 触发方式 | CSS 语法 | 副作用 |
| --- | --- | --- |
| 根元素 | `<html>` 自动建立 | 天然存在 |
| 浮动 | `float: left/right`（非 `none`） | 脱离文档流，影响布局 |
| 绝对定位 | `position: absolute/fixed` | 脱离文档流 |
| display | `display: inline-block/table-cell/flex/grid/flow-root` | 各有不同语义 |
| overflow | `overflow: hidden/scroll/auto`（非 `visible`） | 可能裁剪溢出内容 |
| contain | `contain: layout/paint/strict/content` | 隔离优化 |

> **推荐**：现代开发首选 `display: flow-root` 触发 BFC，它专为此目的设计，无副作用。

---

### 6.3 理论推导与原理解析

### 6.3.1 为何只合并垂直方向？

CSS 2.1 规范将块级元素的流方向定义为垂直（从上至下），而水平方向由 inline 元素的水平排列构成。垂直方向上的 margin 是「段落之间的留白」，多个段落堆叠时，留白合并符合排版直觉（如同 Word 中段落间距取最大值）。水平方向上，inline 元素的 margin 表示字与字、图与字之间的间隔，不应合并。

数学上，垂直 margin 合并可以用下列伪函数表示：

$$
\text{Gap}(A, B) = \max(\text{margin-bottom}_A, \text{margin-top}_B)
$$

而非：

$$
\text{Gap}(A, B) = \text{margin-bottom}_A + \text{margin-top}_B
$$

### 6.3.2 margin 塌陷的传递性

当父元素 $P$ 包含子元素 $C$，且 $P$ 没有 `border-top` 与 `padding-top` 时，$C$ 的 `margin-top` 会「穿透」$P$，表现为 $P$ 自身相对其父容器的 `margin-top`。形式化地：

$$
\text{EffectiveMarginTop}(P) =
\max(\text{margin-top}_P, \text{margin-top}_C) \quad \text{if } \neg\text{HasBorderTop}(P) \wedge \neg\text{HasPaddingTop}(P)
$$

这种「穿透」会向上递归，直到遇到一个有 `border` 或 `padding` 的祖先元素。

### 6.3.3 负 margin 的合并

当参与合并的 margin 含负值时，规则变为「正负相加」：

$$
M_{\text{collapsed}} = M_{\text{max positive}} + M_{\text{min negative}}
$$

例如：

| margin-top of A | margin-bottom of B | 合并结果 |
| --- | --- | --- |
| 20px | 30px | 30px |
| -10px | 20px | 10px |
| -20px | -10px | -20px |
| 30px | -10px | 20px |

负 margin 常用于实现「元素重叠」「文字溢出容器」等效果，但应谨慎使用以避免可维护性下降。

### 6.3.4 BFC 为何能阻止塌陷

BFC 的核心特性是**隔离性**：

- BFC 内部的元素不会影响外部元素的布局。
- BFC 自身的边界由 `border` 与 `padding` 严格界定。
- BFC 内部的 margin 不会穿透到外部。

因此，当父元素触发 BFC 后，其内部子元素的 margin 不再「穿透」父元素的边界，塌陷问题被解决。

证明思路（非形式化）：

设父元素 $P$ 触发 BFC。BFC 规则要求 $P$ 的内容区域与 $P$ 的 margin 区域严格分离，子元素 $C$ 的 margin 必须作用于 $P$ 的 `padding-box` 内部，而 $P$ 自身的 margin 作用于 $P$ 的 `margin-box`。两者位于不同的「层」，无法合并。

### 6.3.5 flex / grid 为何不合并

CSS Flexbox §4.2 与 CSS Grid §2.2 明确规定：flex item 与 grid item 的 margin **不会折叠**。原因是 flex/grid 容器建立了独立的格式化上下文（FFC / GFC），其内部布局算法不沿用 block flow 的合并规则。

这一设计使得：

- flex/grid 容器内的子元素间距可精确控制。
- 引入 `gap` 属性后，间距管理更加语义化（不再依赖 margin）。

### 6.3.6 计算示例

给定以下结构：

```html
<section style="margin-bottom: 30px;">
  <p style="margin-bottom: 20px;">段落 1</p>
  <p style="margin-top: 15px; margin-bottom: 0;">段落 2</p>
</section>
<section style="margin-top: 25px;">
  <h1 style="margin-top: 40px;">标题</h1>
</section>
```

求 `<section>` 之间的最终垂直间距。

**计算过程**：

1. 第一个 `<section>` 末尾：`<p>` 的 `margin-bottom: 0` 与 `<section>` 的 `margin-bottom: 30px` 合并 → 30px。
2. 第二个 `<section>` 开头：`<section>` 的 `margin-top: 25px` 与 `<h1>` 的 `margin-top: 40px` 合并 → 40px（塌陷到 section）。
3. 两个 section 之间合并：max(30, 40) = **40px**。

最终间距为 40px。

---

## 7. 本章综合挑战（选做）
1. 写出“兄弟合并、父子穿透、空块自合并”三种场景的最小复现页面；
2. 用 `display: flow-root` 修复父子塌陷，并对比 `overflow: hidden` 的差异；
3. 用负 margin 实现两栏布局，验证负值参与合并的规则；
4. 在 flex 容器内重复同样的间距，确认 flex/grid 中不会合并。

## 8. 核心知识点
> 一句话记住 margin 合并：垂直外边距取最大值不累加；父子会穿透、空块会自合并；BFC、padding、border 都能阻断；水平方向永远不合并。

- 相邻兄弟：`margin-bottom` 与 `margin-top` 取较大值；
- 父子穿透：子元素 `margin-top` 移到父元素外；
- 空块自合并：自身上下 margin 取最大值；
- 阻断方案：`display: flow-root`（推荐）、`overflow: hidden`、`padding`/`border`；
- flex/grid 容器内不合并（格式化上下文不同）；
- 负 margin 参与合并时按代数规则取“最负”的值；
- 工程上优先用 padding 管理内部间距，用 gap 管理弹性布局间距。

## 9. 注意事项与改进建议
| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 预期间距 50px 实际 30px | 垂直 margin 合并 | 用 padding 或 gap 控制间距 |
| 子元素 margin 穿透 | 父容器位置异常 | 父元素 `display: flow-root` |
| `overflow: hidden` 清塌陷 | 意外裁剪内容 | 优先 `flow-root` |
| 依赖负 margin 布局 | 可读性差 | 用 flex/grid 或定位 |
| 间距用 margin 而非 gap | 最后一个元素多出边距 | 容器用 `gap` |

## 10. 扩展学习
- 盒模型基础：`css/003-CSS3BoxModelDetailed`；
- BFC 与布局：`css/020-TraditionalLayoutTech`；
- 弹性布局：`css/021-CSS3FlexboxFlexLayout`（gap 与不合并行为）；
- 工程化间距：Tailwind 的 `space-y-*` 与 margin 处理策略。

## 附录 A：术语表

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| margin | margin / 外边距 | 围绕元素边框的透明区域 |
| 合并 | collapsing | 相邻 margin 归并为单一 margin |
| 塌陷 | passing-through | 子元素 margin 穿透父元素边界的现象 |
| 邻接 | adjoining | 两个 margin 之间无 border/padding/content 阻隔 |
| BFC | Block Formatting Context | 块格式化上下文，独立的渲染区域 |
| 常规流 | normal flow | 非 float、非 absolute/fixed 的元素流 |
| 格式化上下文 | formatting context | 渲染区域内的布局规则 |
| flex item | flex item | flex 容器的直接子元素 |
| grid item | grid item | grid 容器的直接子元素 |
| 逻辑属性 | logical properties | 适应书写方向的方向无关属性 |
| `margin-trim` | margin-trim | CSS Box Model L4 属性，修剪子元素超出容器的 margin |

## 附录 B：浏览器兼容性速查表

| 特性 | Chrome | Firefox | Safari | Edge | IE11 |
| --- | --- | --- | --- | --- | --- |
| margin collapsing | 全部 | 全部 | 全部 | 全部 | 全部 |
| BFC（overflow） | 全部 | 全部 | 全部 | 全部 | 全部 |
| `display: flow-root` | 58+ | 53+ | 13+ | 79+ | 不支持 |
| flex `gap` | 84+ | 63+ | 14.1+ | 84+ | 不支持 |
| grid `gap` | 66+ | 61+ | 12+ | 79+ | 不支持 |
| `margin-block-*` | 87+ | 66+ | 14.1+ | 87+ | 不支持 |
| `margin-trim` | 不支持 | 不支持 | 16.4+（部分） | 不支持 | 不支持 |

## 附录 C：调试 Checklist

当遇到 margin 相关问题时，按以下顺序排查：

1. [ ] 确认元素是否为块级元素（`display: block`、`flex`、`grid` 等）
2. [ ] 检查父元素是否触发 BFC（`display: flow-root`、`overflow: hidden` 等）
3. [ ] 检查父元素是否有 `border`、`padding` 阻隔
4. [ ] 确认是否在 flex/grid 容器内（内部不合并）
5. [ ] 检查是否有负 margin（合并规则不同）
6. [ ] 检查元素是否为空（空块自身合并）
7. [ ] 使用 DevTools 检查盒模型可视化
8. [ ] 检查浏览器兼容性（IE 不支持 `flow-root`）
9. [ ] 验证响应式行为（不同视口下间距是否一致）
10. [ ] 检查与设计系统的间距规范是否一致

---

> 本文最后更新于 2026-06-14，内容基于 W3C CSS Box Model Module Level 3（2018）与 Level 4（2024 Editor's Draft）。如规范更新，请以 W3C 最新发布为准。

<!-- ============ 文档分隔线：007-css/014-PositionDetailed.md ============ -->

## 1. position 属性

| 值         | 定位类型 | 脱离文档流 | 参照物       |
| ---------- | -------- | ---------- | ------------ |
| `static`   | 默认     |            | —            |
| `relative` | 相对定位 |            | 自身原位置   |
| `absolute` | 绝对定位 |            | 最近定位祖先 |
| `fixed`    | 固定定位 |            | 视口         |
| `sticky`   | 粘性定位 | →          | 滚动容器     |

## 2. relative

```css
.element {
  position: relative;
  top: 10px;
  left: 20px;
}
```

不脱离文档流，原位置保留。常作 absolute 的参照容器。

## 3. absolute

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

脱离文档流，参照最近定位祖先。

## 4. fixed

```css
.header {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
}
```

参照视口，滚动时固定。注意 transform 会改变包含块。

## 5. sticky

```css
.sidebar {
  position: sticky;
  top: 20px;
}
th {
  position: sticky;
  top: 0;
  background: white;
  z-index: 1;
}
```

阈值前 relative，达到后 fixed。必须指定 top/bottom。

## 6. z-index

```css
:root {
  --z-dropdown: 100;
  --z-modal: 300;
  --z-toast: 400;
}
```

z-index 仅对定位元素生效；同一层叠上下文内比较；子元素无法超越父上下文。
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

## 本章综合挑战（选做）

1. 用 `absolute + inset: 0` 做一个全屏遮罩层；
2. 用 `sticky` 做表格吸顶表头；
3. 用 `fixed` + CSS 变量做悬浮“回到顶部”按钮；
4. 验证 `transform` 祖先会改变 `fixed` 的参照系。

## 核心知识点

> 一句话记住定位：`relative` 留原位，`absolute` 找祖先，`fixed` 看视口，`sticky` 会吸顶；`z-index` 只在同一层叠上下文内比大小。

- 五种定位值对应五种参照系：static/relative/absolute/fixed/sticky；
- `absolute`/`fixed` 脱离文档流，`relative`/`sticky` 保留原位；
- `absolute` 参照最近定位祖先，父元素记得加 `relative`；
- `fixed` 默认参照视口，`transform` 祖先会改变包含块；
- `sticky` 必须给阈值，父容器 `overflow: hidden` 会失效；
- `z-index` 建议用 CSS 变量管理，注意层叠上下文边界；
- `inset` 简写与 `clip-path` 是常用的现代补充。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| `absolute` 找不到参照 | 相对页面跳动 | 父元素加 `position: relative` |
| 祖先有 transform | `fixed` 不再相对视口 | 调整结构或改用 `position: fixed` 的替代方案 |
| 父容器 `overflow: hidden` | sticky 失效 | 改用 `overflow: clip` |
| 大量魔法 z-index | 层级失控 | 用变量定义层级体系 |
| 用 margin 做悬浮 | 与滚动冲突 | 用 fixed/sticky + inset |

## 扩展学习

- 定位基础：`css/020-TraditionalLayoutTech`；
- 层叠上下文：`css/016-StackingContext`；
- 变换：`css/069-Transform3D`（transform 与包含块）；
- 布局实战：`css/067-CSSProjectExampleResponsiveHomepage`。

<!-- ============ 文档分隔线：007-css/015-FloatClear.md ============ -->

# CSS 浮动与清除：原理、实践与现代替代

> 本文档对标 CSS 权威规范（CSS2.1 §9.5 Floats、CSS Display Module Level 3）与 MDN 教学文档，
> 从视觉格式化模型出发，完整讲解浮动（float）与清除（clear）的底层原理、历史演进与工程实践。

---

## 0. 直觉：让图片“漂”在文字里

报纸杂志里，图片嵌在文字中间、文字沿图片边缘环绕——`float` 最初就是为这个场景设计的：让元素向左或向右“漂”，后续文字绕着它排。

现代布局（Flexbox/Grid）已经取代了“用浮动拼整页”的做法，但文字环绕依然是 `float` 的独有能力。学这一节，重点记住三件事：怎么漂、漂了之后高度塌陷怎么修、什么时候别用。

## 1. 历史动机与发展脉络

浮动诞生于 CSS1（1996 年），最初的设计动机是模拟报纸排版中的**图文混排**：
让图片向左或向右"漂浮"，让文字沿着图片边缘自然环绕。

| 时期 | 事件 | 意义 |
| --- | --- | --- |
| 1996 | CSS1 引入 `float` | 首次在 Web 上实现图文混排 |
| 1998 | CSS2 引入 `clear` 与定位体系 | 补全浮动清除机制 |
| 2000 年代 | "浮动布局"时代 | 开发者用 float 拼装整页布局（两栏、三栏） |
| 2009-2012 | Flexbox 与 Grid 规范启动 | 提供以文档流为中心的一维/二维布局方案 |
| 2017 | Grid 主流浏览器支持 | 浮动退出整页布局主流场景 |
| 2020s | `display: flow-root` 广泛支持 | 提供语义化的 BFC 创建方式，替代 hack |

历史上的关键教训：**浮动是被"借"来搭建整页布局的**，它本身并不具备网格系统的
对齐与轨道能力，因此 2010 年代后逐渐被 Flexbox 与 Grid 取代；但文字环绕这一
原生能力至今仍没有更好的替代品。

---

## 2. 形式化定义

### 2.1 float 属性

按 CSS2.1 §9.5 定义，浮动框（floating box）是一个向左或向右移动的框，
其外边界（outer edge）被移动到当前行的起点或终点，或移动到另一个浮动框的
外边界旁。浮动元素：

- 从普通流（normal flow）中**取出**，不参与父容器的高度计算；
- 仍参与文本流（text flow），后续行内内容沿其边界环绕；
- 其顶端（top）不得超过浮动元素之前生成的任何块框的顶端；
- 同一方向连续浮动的框依次水平排列，空间不足时换行。

### 2.2 取值语法

```text
float: left | right | none | inline-start | inline-end
clear: none | left | right | both | inline-start | inline-end
```

| 属性 | 取值 | 效果 |
| --- | --- | --- |
| `float: left` | 靠左浮动 | 元素靠父容器左边缘排列 |
| `float: right` | 靠右浮动 | 元素靠父容器右边缘排列 |
| `float: none` | 默认 | 元素按普通流排列 |
| `float: inline-start` | 逻辑属性 | 在 LTR 中等于 left，在 RTL 中等于 right |
| `float: inline-end` | 逻辑属性 | 在 LTR 中等于 right，在 RTL 中等于 left |
| `clear: left` | 清除左浮动 | 元素移到其上方所有左浮动框之下 |
| `clear: right` | 清除右浮动 | 元素移到其上方所有右浮动框之下 |
| `clear: both` | 清除两侧 | 元素移到其上方所有浮动框之下 |

### 2.3 逻辑属性与物理属性

CSS Logical Properties 模块为 `float`/`clear` 增加了 `inline-start`/`inline-end`
两个逻辑值，它们随书写模式（writing-mode）与方向（direction）自动翻转，
适合国际化（i18n）场景。

---

## 3. 理论推导与原理解析

### 3.1 视觉格式化模型中的位置

普通流中的块级元素按"包含块、块级盒、行内盒"层层嵌套。浮动把元素从
**块级格式化上下文**中取出，放入一个"浮动带"（float band）：

1. 浮动元素生成浮动框，沿包含块的左/右边距放置；
2. 后续块级盒忽略浮动占用的横向空间（所以会"顶上来"）；
3. 后续行内内容（文本、行内元素）在剩余空间中排布，形成环绕效果；
4. 若浮动高度超过其父容器内容区，父容器不感知其高度，于是高度塌陷。

### 3.2 高度塌陷的成因

```html
<div class="wrapper">
  <div class="child"></div>
</div>
```

```css
.wrapper { border: 1px solid #333; }
.child { float: left; width: 200px; height: 100px; }
```

`.wrapper` 的高度由普通流内容决定，而 `.child` 已脱离普通流，因此 wrapper
的高度为 0（仅边框可见），这就是"高度塌陷"。

### 3.3 BFC 如何解决塌陷

BFC（块格式化上下文）是一块独立渲染区域，其特性之一：**BFC 会包含其内部所有
浮动元素**。因此，只要让父容器形成 BFC，它就会把浮动的子元素"算进"自己的高度。
创建 BFC 的常见方式：

| 方式 | 写法 | 副作用 |
| --- | --- | --- |
| overflow 非 visible | `overflow: hidden` | 可能裁剪溢出内容 |
| display: flow-root | `display: flow-root` | 无副作用，语义清晰 |
| display: inline-block | `display: inline-block` | 引入行内盒特性 |
| float 自身 | `float: left` | 父容器自己也浮动了 |
| position: absolute/fixed | `position: absolute` | 脱离文档流 |

### 3.4 clearfix 的历史 hack

在 `flow-root` 出现前，社区使用 `clearfix` 伪元素方案：

```css
.clearfix::after {
  content: '';
  display: block;
  clear: both;
}
```

原理：在父容器末尾插入一个空的块级伪元素，并对其设置 `clear: both`，
迫使父容器把该伪元素放在所有浮动元素之下，从而撑开高度。

---

## 4. 代码示例

### 4.1 基础浮动与文字环绕

```html
<article>
  <img src="cover.jpg" alt="封面" class="cover">
  <p>这段文字会沿着图片的右侧轮廓环绕排列，形成杂志式排版效果。</p>
  <p>第二段继续环绕，直到图片底部结束，后续内容恢复整行排列。</p>
</article>
```

```css
.cover {
  float: left;
  width: 240px;
  margin-right: 1.5rem;
  border-radius: 8px;
}
```

**讲解：** `float: left` 让图片靠左，`margin-right` 留出文字间距；文字沿图片右侧环绕，是杂志式排版的经典写法。

### 4.2 右浮动与 clear

```html
<div class="quote">引用块</div>
<p>普通段落</p>
```

```css
.quote {
  float: right;
  width: 40%;
  margin-left: 1rem;
}
p {
  clear: both; /* 强制段落移动到浮动块之下 */
}
```

**讲解：** `float: right` 让引用块靠右；`clear: both` 让后续元素不再环绕，从浮动块下方重新开始排列。

### 4.3 三种塌陷修复方案

```css
/* 方式一：clearfix（历史方案） */
.clearfix::after {
  content: '';
  display: block;
  clear: both;
}

/* 方式二：overflow（有裁剪风险） */
.overflow-fix {
  overflow: hidden;
}

/* 方式三：flow-root（现代推荐） */
.flow-root-fix {
  display: flow-root;
}
```

**讲解：** 三种修复：clearfix 伪元素（历史标准）、`overflow: hidden`（可能裁剪内容）、`display: flow-root`（现代推荐，无副作用）。

### 4.4 现代两栏布局对照

```css
/* float 方案（旧） */
.float-layout::after {
  content: '';
  display: block;
  clear: both;
}
.float-layout .sidebar {
  float: left;
  width: 25%;
}
.float-layout .main {
  float: right;
  width: 73%;
}

/* flex 方案（推荐） */
.flex-layout {
  display: flex;
  gap: 2%;
}
.flex-layout .sidebar {
  flex: 0 0 25%;
}
.flex-layout .main {
  flex: 1;
}
```

**讲解：** 两栏布局中，float 方案需要手动清浮动与计算宽度；Flexbox 用 `flex: 0 0 25%` + `flex: 1` 自动分配剩余空间，代码更短、行为更可预测。

---

## 5. 对比分析

| 维度 | float | Flexbox | Grid |
| --- | --- | --- | --- |
| 文档流参与度 | 脱离普通流 | 保持一维流 | 保持二维流 |
| 高度塌陷 | 常见 | 不会 | 不会 |
| 对齐能力 | 弱 | 主轴/交叉轴强 | 行列轨道强 |
| 响应式 | 需媒体查询手改 | 自动换行（wrap） | 自动填充（auto-fill） |
| 文字环绕 | 原生支持 | 不支持 | 不支持 |
| 代码可维护性 | 低（需 hack） | 高 | 高 |
| 浏览器兼容 | 全兼容 | 现代浏览器 | 现代浏览器 |
| 适用场景 | 图文混排、旧项目维护 | 导航、组件内一维布局 | 整页复杂二维布局 |

---

## 6. 常见陷阱与最佳实践

1. **忘记清除浮动导致塌陷**：只要父容器内含浮动子元素，就必须修复；
   优先使用 `display: flow-root`，其次 clearfix。
2. **overflow: hidden 裁剪内容**：`overflow: hidden` 形成的 BFC 会隐藏溢出
   的提示框或阴影，使用前确认无裁剪需求。
3. **百分比宽度与 padding 冲突**：浮动元素默认 `box-sizing: content-box`，
   设置 `width: 25%` 后再加 padding 会撑破容器，建议全局 `box-sizing: border-box`。
4. **浮动顺序影响换行**：浮动元素按 DOM 顺序排列，顺序调整可能改变换行位置，
   移动端请优先使用 Flexbox/Grid 的自然换行。
5. **clear 作用对象错误**：`clear` 只清除"其上方"的浮动，放在浮动元素前面无效。
6. **RTL 场景**：使用 `inline-start`/`inline-end` 逻辑值，避免硬编码 left/right。

---

## 7. 工程实践

### 7.1 在构建工具中启用现代属性

使用 PostCSS 的 `autoprefixer` 时，`display: flow-root` 等现代属性会被自动
按浏览器目标（browserslist）处理：

```json
{
  "browserslist": ["last 2 versions", "not dead"]
}
```

### 7.2 组件化封装

```css
/* components/MediaObject.css */
.media {
  display: flow-root;
}
.media__figure {
  float: left;
  margin-right: 1rem;
}
.media__body {
  overflow: hidden; /* 或 min-width: 0，防止文本溢出 */
}
```

### 7.3 代码检查

使用 Stylelint 的 `declaration-property-value-no-unknown` 或
`selector-max-id` 等规则，配合 `stylelint-config-standard` 保证浮动相关
代码风格统一。

---

## 8. 案例研究：杂志式图文混排页面

需求：实现一个博客文章头图、正文环绕、侧栏引语的完整页面。

```html
<main class="article">
  <h1>浮动布局实战</h1>
  <img class="hero" src="hero.jpg" alt="文章头图">
  <p>第一段……文字环绕头图右侧。</p>
  <blockquote class="pull-quote">金句引用</blockquote>
  <p>引语之后的文字继续环绕。</p>
</main>
```

```css
.article {
  display: flow-root; /* 修复 hero 与 pull-quote 造成的塌陷 */
  max-width: 900px;
  margin: 0 auto;
}
.hero {
  float: left;
  width: 45%;
  margin: 0 1.5rem 1rem 0;
}
.pull-quote {
  float: right;
  width: 35%;
  margin: 0 0 1rem 1.5rem;
  border-left: 4px solid #d63031;
  padding-left: 1rem;
}
```

要点：

1. 文章容器用 `display: flow-root` 一次性解决所有浮动子元素的高度塌陷；
2. 左浮动头图与右浮动引语互不冲突（不同方向）；
3. 正文段落无需 `clear`，自然环绕；
4. 移动端可叠加媒体查询，将浮动降级为普通块级排列。

## 9. 本章综合挑战（选做）

1. 用 `float` 做一段“图片左浮 + 文字环绕”的杂志式排版；
2. 用 `display: flow-root` 修复父容器高度塌陷，并对比 `overflow: hidden`；
3. 用 Flexbox 重写同一个两栏布局，比较代码量与可维护性；
4. 在移动端断点把浮动降级为普通排列。

## 10. 核心知识点

> 一句话记住浮动：`float` 让元素靠边、文字环绕；浮动不占高度，父容器要 `flow-root` 修复；整页布局请用 Flexbox/Grid。

- `float: left/right` 取出元素并让行内内容环绕；
- 浮动元素不参与父容器高度计算，导致高度塌陷；
- 修复：clearfix 伪元素、`overflow: hidden`、`display: flow-root`（推荐）；
- `clear: both` 强制后续元素移到浮动块下方；
- 文字环绕是 float 的独有能力；整页布局应使用 Flexbox/Grid；
- 同方向浮动依次排列，空间不足换行。

## 11. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 浮动布局不换行 | 父容器塌陷、错位 | 用 `flow-root` 或改 Flexbox |
| `overflow: hidden` 清浮动 | 裁剪溢出内容 | 优先 `flow-root` |
| 忘记 `clear` | 后续元素继续环绕 | 需要时显式 `clear: both` |
| 用 float 做导航/网格 | 可维护性差 | 用 Flexbox/Grid |
| 图文混排用 flex | 环绕效果无法实现 | 只有 float 支持文字环绕 |

## 12. 扩展学习

- 传统布局：`css/020-TraditionalLayoutTech`；
- 盒模型与 BFC：`css/003-CSS3BoxModelDetailed`、`css/013-MarginCollapse`；
- 现代布局：`css/021-CSS3FlexboxFlexLayout`、`css/022-CSS3GridGridLayout`；
- 响应式图文：`css/033-ResponsiveDesign`。

<!-- ============ 文档分隔线：007-css/016-StackingContext.md ============ -->

> 前置依赖：先读 014 定位详解，理解 z-index 基本用法。

## 概述

层叠上下文（Stacking Context）是 CSS 中决定元素在 Z 轴上渲染顺序的机制。每个层叠上下文都是一个独立的三维概念空间，内部元素的层叠顺序不会影响外部。理解层叠上下文对于解决 z-index 失效、元素被意外遮挡等问题至关重要。层叠上下文的创建条件、层叠顺序规则以及嵌套关系是掌握 CSS 布局深度的关键。

## 基础概念

**层叠上下文**：一个 HTML 元素如果满足特定条件，就会创建一个新的层叠上下文。在同一个层叠上下文中，元素按照固定的层叠顺序规则进行排列。

**层叠顺序**：同一个层叠上下文内，元素从底到顶的渲染顺序依次为：背景/边框、负 z-index、常规流块级盒子、浮动盒子、常规流行内盒子、z-index:0 的定位元素、正 z-index 的定位元素。

**z-index**：仅对定位元素（position 不为 static）生效，用于控制同一层叠上下文内定位元素的层叠顺序。z-index 值越大，元素越靠近用户。

**嵌套规则**：子层叠上下文整体参与父层叠上下文的层叠顺序比较。子元素的 z-index 无论多大，都无法超越父层叠上下文的限制。

## 快速上手

### 层叠顺序演示

```html
<div class="container">
  <!-- 常规流块级盒子 - 层叠顺序较低 -->
  <div class="block">常规流块级盒子</div>

  <!-- 浮动盒子 - 高于常规流 -->
  <div class="float">浮动盒子</div>

  <!-- 定位元素 + z-index - 层叠顺序最高 -->
  <div class="positioned">定位元素 z-index: 1</div>
</div>
```

```css
.container {
  position: relative;
}

.block {
  background: #e3f2fd;
  padding: 20px;
}

.float {
  float: left;
  background: #fff3e0;
  padding: 20px;
  margin-left: -50px; /* 与块级盒子重叠 */
}

.positioned {
  position: relative;
  z-index: 1;
  background: #e8f5e9;
  padding: 20px;
  margin-top: -30px; /* 与其他元素重叠 */
}
```

### z-index 基本用法

```css
/* z-index 仅对定位元素生效 */
.dropdown {
  position: absolute;
  z-index: 100; /* 显示在普通元素之上 */
}

.modal-overlay {
  position: fixed;
  z-index: 1000; /* 模态框层叠更高 */
}

.toast {
  position: fixed;
  z-index: 2000; /* 提示信息在最顶层 */
}
```

## 详细用法

### 创建层叠上下文的条件

```css
/* 方式一：position + z-index（最常见） */
.element-1 {
  position: relative;
  z-index: 0; /* 即使是 0 也会创建层叠上下文 */
}

/* 方式二：opacity 小于 1 */
.element-2 {
  opacity: 0.99; /* 创建新的层叠上下文 */
}

/* 方式三：transform */
.element-3 {
  transform: translateZ(0); /* 常用于硬件加速，同时创建了层叠上下文 */
}

/* 方式四：filter */
.element-4 {
  filter: blur(0); /* 即使模糊为 0 也会创建层叠上下文 */
}

/* 方式五：will-change */
.element-5 {
  will-change: transform; /* 提示浏览器该属性将变化，创建层叠上下文 */
}

/* 方式六：isolation（推荐方式） */
.element-6 {
  isolation: isolate; /* 专门用于创建层叠上下文，无副作用 */
}

/* 方式七：其他属性 */
.element-7 {
  -webkit-overflow-scrolling: touch; /* 移动端滚动 */
}

.element-8 {
  contain: layout; /* CSS Containment */
}
```

### 层叠顺序七层模型

```css
/*
 * 同一层叠上下文内的层叠顺序（从底到顶）：
 *
 * 第1层：层叠上下文的背景和边框
 * 第2层：z-index 为负的定位元素
 * 第3层：常规流中的块级盒子
 * 第4层：浮动盒子（非定位）
 * 第5层：常规流中的行内盒子（文字、行内元素等）
 * 第6层：z-index: 0 / auto 的定位元素
 * 第7层：z-index 为正的定位元素
 */

/* 负 z-index 示例：会跑到父元素背景下面 */
.behind-background {
  position: absolute;
  z-index: -1;
}

/* 行内元素层叠高于块级元素 */
.block-element {
  display: block;
  background: #ffcc00;
}

.inline-element {
  display: inline;
  background: #00ccff;
  /* 行内元素会覆盖块级元素的背景 */
}
```

### 嵌套层叠上下文

```html
<!-- 子层叠上下文无法超越父层叠上下文 -->
<div class="parent">
  <div class="child-high">子元素 z-index: 9999</div>
</div>
<div class="sibling">兄弟元素 z-index: 2</div>
```

```css
.parent {
  position: relative;
  z-index: 1; /* 父元素创建层叠上下文，z-index 为 1 */
}

.child-high {
  position: absolute;
  z-index: 9999;
  /* 虽然子元素 z-index 很大，但父层叠上下文 z-index 只有 1 */
  /* 所以整体仍然在 z-index: 2 的兄弟元素下面 */
}

.sibling {
  position: relative;
  z-index: 2; /* 父层叠上下文 z-index:1 < 2，所以兄弟元素在上面 */
}
```

## 常见场景

### 下拉菜单与导航栏

```css
/* 导航栏层叠 */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
}

/* 下拉菜单在导航栏之上 */
.dropdown-menu {
  position: absolute;
  z-index: 110;
}

/* 模态框覆盖一切 */
.modal-backdrop {
  position: fixed;
  z-index: 1000;
}

.modal-content {
  position: fixed;
  z-index: 1010;
}
```

### 卡片悬浮效果

```css
.card {
  position: relative;
  transition:
    transform 0.3s,
    box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  /* transform 创建了新的层叠上下文 */
  /* 悬浮的卡片会覆盖相邻卡片 */
}

.card .overlay {
  position: absolute;
  inset: 0;
  z-index: 1; /* 在卡片内容之上 */
  background: rgba(0, 0, 0, 0.5);
  opacity: 0;
  transition: opacity 0.3s;
}

.card:hover .overlay {
  opacity: 1;
}
```

## 注意事项

- **z-index 失效排查**：z-index 不生效时，首先检查元素是否为定位元素（position 不为 static），其次检查是否被父层叠上下文限制。
- **避免 z-index 军备竞赛**：不要随意使用过大的 z-index 值（如 99999），应使用 CSS 变量统一管理层叠级别。
- **隐式创建层叠上下文**：opacity、transform、filter 等属性会隐式创建层叠上下文，可能导致 z-index 行为与预期不符。排查问题时注意检查这些属性。
- **推荐使用 isolation**：当需要创建层叠上下文但不希望产生其他副作用时，使用 `isolation: isolate` 是最安全的方式。
- **Flex/Grid 子元素**：在 Flex 和 Grid 布局中，子元素的 z-index 即使没有设置 position 也能生效，因为 Flex/Grid 子元素默认具有层叠上下文能力。

## 进阶用法

### CSS 变量管理层叠级别

```css
:root {
  /* 统一管理层叠级别，避免 z-index 军备竞赛 */
  --z-base: 1;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-fixed: 300;
  --z-modal-backdrop: 400;
  --z-modal: 500;
  --z-popover: 600;
  --z-tooltip: 700;
  --z-toast: 800;
}

.dropdown {
  position: absolute;
  z-index: var(--z-dropdown);
}

.sticky-header {
  position: sticky;
  z-index: var(--z-sticky);
}

.modal-backdrop {
  position: fixed;
  z-index: var(--z-modal-backdrop);
}

.modal {
  position: fixed;
  z-index: var(--z-modal);
}

.tooltip {
  position: absolute;
  z-index: var(--z-tooltip);
}
```

### 层叠上下文与合成层

```css
/*
 * 浏览器渲染流程：
 * 1. DOM 树构建
 * 2. CSSOM 构建
 * 3. 渲染树（Render Tree）
 * 4. 布局（Layout）
 * 5. 绘制（Paint）
 * 6. 合成（Composite）
 *
 * 层叠上下文影响合成阶段：
 * - 每个层叠上下文可能被提升为独立的合成层
 * - 合成层由 GPU 单独渲染，不影响其他层
 * - 但过多的合成层会消耗显存
 */

/* 使用 will-change 提示浏览器提前优化 */
.animated-element {
  will-change: transform;
  /* 创建合成层，动画更流畅 */
  /* 但不要滥用，每个合成层都消耗内存 */
}

/* 更好的做法：只在需要时添加 */
.animated-element:hover {
  will-change: transform;
}
```

### 调试层叠上下文

```css
/*
 * 调试技巧：
 *
 * 1. Chrome DevTools -> Elements -> Computed -> 搜索 "stacking context"
 * 2. 检查元素的 position 和 z-index
 * 3. 检查父元素是否创建了层叠上下文
 * 4. 临时设置高 z-index 测试是否被父元素限制
 */

/* 快速调试：给可疑元素加红色边框 */
.debug {
  outline: 2px solid red !important;
}

/* 检查是否创建了层叠上下文 */
.debug-stacking {
  isolation: isolate; /* 确认创建层叠上下文 */
}
```

## 动手试试

1. 写两个重叠的定位元素，用 `z-index` 调整层级，观察谁在上层；
2. 给其中一个元素加 `opacity: 0.99`，观察它是否“困住”了子元素的 z-index；
3. 用 DevTools 的 Layers 面板查看层叠上下文；
4. 进阶挑战：用 CSS 变量定义 `--z-dropdown/--z-modal/--z-toast` 层级体系。

## 核心知识点

> 一句话记住层叠上下文：同一上下文内按顺序渲染（背景、负 z、块、浮动、行内、z=0、正 z）；z-index 只在同一上下文内比较，父上下文是子元素的天花板。

- 层叠上下文是独立的“三维空间”，内部顺序不影响外部；
- 创建条件：定位 + z-index、transform、opacity < 1、filter、will-change 等；
- 层叠顺序：背景 → 负 z-index → 块级 → 浮动 → 行内 → z-index:0 → 正 z-index；
- 子元素 z-index 再大也越不过父上下文；
- 调试用 DevTools Layers 面板；
- 层级建议用变量统一管理。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| z-index 失效 | 不在同一层叠上下文 | 检查祖先是否创建了新上下文 |
| opacity/transform 副作用 | 意外创建上下文 | 理解触发条件，必要时调整结构 |
| 层级魔法数字 | 难以维护 | 用 CSS 变量定义层级体系 |
| 忽略父上下文 | 子元素层级异常 | 先确认父上下文的 z-index |

## 扩展学习

- 定位：`css/014-PositionDetailed`；
- 优先级：`css/009-PriorityCalculation`；
- 合成与性能：`css/042-CSSPerformanceOptimizationDetailed`。

<!-- ============ 文档分隔线：007-css/017-CSSListStyle.md ============ -->

## 0. 直觉：列表前面的“小圆点”是可以换的

`<ul>` 默认显示实心圆点，`<ol>` 默认显示数字——这些标记由 CSS 的 `list-style` 系列属性控制。它们决定三件事：用什么形状（`list-style-type`）、放在哪里（`list-style-position`）、是否用图片（`list-style-image`）。

导航栏最常见的需求就是“去掉小圆点”：`list-style: none`。这一节学完，列表标记随你定制。

## 1. 核心属性

### 1.1 list-style-type：标记形状

```css
ul {
  list-style-type: disc;    /* 实心圆（默认） */
}
ul.circle {
  list-style-type: circle;  /* 空心圆 */
}
ul.square {
  list-style-type: square;  /* 实心方块 */
}
ol {
  list-style-type: decimal;      /* 1, 2, 3（默认） */
}
ol.alpha {
  list-style-type: lower-alpha;  /* a, b, c */
}
ol.roman {
  list-style-type: lower-roman;  /* i, ii, iii */
}
ul.none {
  list-style-type: none;         /* 无标记 */
}
```

**讲解：**

- 无序列表的值：`disc`/`circle`/`square`/`none`；
- 有序列表的值：`decimal`/`lower-alpha`/`upper-alpha`/`lower-roman`/`upper-roman`；
- `none` 只是去掉标记，不改变列表语义，读屏仍会播报“列表共 N 项”；
- 标记外观也可以用 `::marker` 伪元素进一步定制（颜色、字体、内容）。

### 1.2 list-style-position：标记位置

```css
ul.outside {
  list-style-position: outside; /* 标记在内容盒外（默认，缩进） */
}
ul.inside {
  list-style-position: inside;  /* 标记进入内容盒，与首行文字同行 */
}
```

**讲解：** `outside` 时标记悬在内容左侧，多行文本自动对齐；`inside` 时标记成为首行的一部分，适合空间紧凑的场景。

### 1.3 list-style-image：图片标记

```css
ul {
  list-style-image: url("check.svg");
}
```

**讲解：** 用图片代替标记，适合自定义图标；图片加载失败时无标记，建议同时设置 `list-style-type` 作为兜底。现代项目更推荐 `::marker` 或 `::before` + `content` 实现图标。

### 1.4 简写与重置

```css
ul {
  list-style: none;              /* 最常用：去掉标记 */
  list-style: square inside;     /* 类型 + 位置 */
  list-style: url("x.svg") outside;
}
```

**讲解：** 简写顺序是 `type position image`，未写的部分重置为默认值；`list-style: none` 是导航、卡片列表的标准起点。

## 2. 动手试试

1. 给一个 `<ul>` 依次设置 `disc`/`circle`/`square`/`none`，刷新观察变化；
2. 给 `<ol>` 设置 `lower-roman`，再对比 `outside` 与 `inside` 的缩进差异；
3. 做导航菜单：`list-style: none` + 横向排列；
4. 进阶挑战：用 `::marker` 把标记改成红色箭头（`content: "→"`）。

## 3. 核心知识点

> 一句话记住列表样式：`type` 定形状，`position` 定内外，`image` 用图片；`list-style: none` 去标记，导航必备。

- `list-style-type`：`disc`/`circle`/`square`（无序），`decimal`/`roman`/`alpha`（有序）；
- `list-style-position`：`outside`（默认）与 `inside`；
- `list-style-image`：图片标记，建议留 type 兜底；
- `list-style` 简写会重置未写子属性；
- `::marker` 可精细定制标记样式；
- `none` 不删除语义，读屏仍识别列表。

## 4. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 用 `::before` 模拟标记 | 语义丢失，读屏不识别列表 | 保留 `<ul>` + `list-style` 或 `::marker` |
| 图片标记无兜底 | 加载失败后无标记 | 同时设置 `list-style-type` |
| 忘记重置简写 | 意外清掉其它样式 | 简写放最后，注意覆盖范围 |
| 只做视觉去点 | 列表语义仍在 | 用 `none` 即可，不必换 `div` |
| 数字编号被手写 | 增删条目后错乱 | 用 `<ol>` 自动编号 |

## 5. 扩展学习

- 列表结构：`html5/017-List`；
- `::marker`：`css/023-PseudoClassPseudoElement`；
- 选择器：`css/007-CSS3SelectorSystem`；
- 导航实战：`css/067-CSSProjectExampleResponsiveHomepage`。

<!-- ============ 文档分隔线：007-css/018-CSSTableStyling.md ============ -->

## 0. 直觉：表格默认样式“很散”，需要收拢

浏览器默认的表格：边框各自独立、单元格之间有缝隙、宽度随内容乱撑。表格样式的核心就是把这张“散装表格”整理成整齐的网格。

最常用的一条规则是 `border-collapse: collapse`：让相邻单元格的边框合并成一条，表格立刻“紧凑”起来。

## 1. 核心属性

### 1.1 border-collapse：边框合并

```css
table {
  border-collapse: collapse; /* 合并相邻边框（推荐） */
  /* border-collapse: separate; 保留独立边框 */
}
```

**讲解：** `collapse` 让相邻单元格共用一条边框，是表格样式的事实标准；`separate` 是默认值，配合 `border-spacing` 控制单元格间距。

### 1.2 border-spacing：单元格间距

```css
table {
  border-collapse: separate;
  border-spacing: 4px 8px; /* 水平 4px，垂直 8px */
}
```

**讲解：** 只在 `separate` 模式下生效；`collapse` 模式下该属性无效。

### 1.3 caption-side：标题位置

```css
table {
  caption-side: top;    /* 标题在表格上方（默认） */
  /* caption-side: bottom; 标题在下方 */
}
```

**讲解：** 控制 `<caption>` 标题的位置，配合 `<caption>` 提供表格语义标题。

### 1.4 empty-cells：空单元格

```css
table {
  border-collapse: separate;
  empty-cells: hide; /* 隐藏空单元格的背景与边框 */
}
```

**讲解：** 只在 `separate` 模式下生效；`show` 为默认值。数据表格中合并单元格后留下的空位可以用它隐藏。

### 1.5 table-layout：宽度算法

```css
table {
  table-layout: auto;   /* 浏览器按内容计算（默认） */
  table-layout: fixed;  /* 按第一行/列宽计算，更快更可控 */
}
```

**讲解：** `fixed` 模式按第一行决定列宽，渲染更快，适合大数据表格；`auto` 会随内容自适应，但长内容可能撑破布局。

### 1.6 完整示例

```html
<style>
  table {
    border-collapse: collapse;
    width: 100%;
  }
  th,
  td {
    border: 1px solid #ddd;
    padding: 8px 12px;
    text-align: left;
  }
  th {
    background: #f5f5f5;
  }
  tbody tr:nth-child(odd) {
    background: #fafafa; /* 隔行变色 */
  }
</style>
<table>
  <caption>月度销售统计</caption>
  <thead>
    <tr><th>月份</th><th>销售额</th></tr>
  </thead>
  <tbody>
    <tr><td>1 月</td><td>12000</td></tr>
    <tr><td>2 月</td><td>15000</td></tr>
  </tbody>
</table>
```

**讲解：** 完整表格样式的标准套路：`collapse` 合并边框、`th` 加底色区分表头、`:nth-child(odd)` 隔行变色、`<caption>` 提供标题。

## 2. 动手试试

1. 建一个 3x3 表格，分别用 `collapse` 与 `separate` 观察边框差异；
2. 给表头加背景色，用 `:nth-child(odd)` 做隔行变色；
3. 用 `table-layout: fixed` 固定列宽，对比 `auto` 的行为；
4. 进阶挑战：做一个响应式表格，小屏时把表头变成竖排（`display: block` 方案）。

## 3. 核心知识点

> 一句话记住表格样式：`collapse` 收边框，`spacing` 调间距，`caption` 定标题，`fixed` 管宽度；表头加底色，隔行变色更好读。

- `border-collapse: collapse` 是表格首选；
- `border-spacing` 与 `empty-cells` 只在 `separate` 下生效；
- `caption-side` 控制标题位置；
- `table-layout: fixed` 性能更好、宽度可控；
- 表头用 `th` + 背景色区分，隔行变色用 `:nth-child`；
- 表格语义（`caption`/`thead`/`tbody`）与样式配合。

## 4. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 `collapse` | 双层边框、间隙大 | 表格一律 `border-collapse: collapse` |
| 用 div 拼表格 | 语义与读屏支持全丢 | 使用原生 `table` 结构 |
| 列宽随内容乱变 | 布局跳动 | `table-layout: fixed` + 显式列宽 |
| 没有表头 | 数据含义不明 | 用 `th` + `scope` 语义化 |
| 大表格无分页 | 渲染与滚动卡顿 | 虚拟滚动或分页 |

## 5. 扩展学习

- 结构语义：`html5/017-List` 与表格的对比；
- 隔行变色：`css/023-PseudoClassPseudoElement` 的 `:nth-child`；
- 响应式表格：`css/033-ResponsiveDesign`；
- 数据可视化：用 `css/022-CSS3GridGridLayout` 做网格布局。

<!-- ============ 文档分隔线：007-css/019-DebuggingCSS.md ============ -->

## 0. 直觉：样式不生效，先问“谁赢了”

“我明明写了，怎么没生效？”——几乎都是四个原因之一：文件没保存、选择器没匹配上、被更高优先级的规则覆盖、或者属性被继承/简写重置。开发者工具（DevTools）能把这四个原因全部可视化，本课教你用它排查。

## 1. Elements 面板：看元素命中了哪些规则

按 F12 打开 DevTools，切到 Elements（元素）面板：

1. 点击左上角的选择器图标（箭头），再点击页面里的目标元素；
2. 右侧 Styles（样式）子面板会列出所有命中该元素的规则，从上到下按优先级排列；
3. 被划掉的声明表示“写了但被覆盖”，旁边会标注是谁赢的。

```text
Styles 面板示例
h1 { color: blue; }        ← 未划掉，生效
h1 { color: red; }         ← 划掉，被上面的覆盖
```

**讲解：** 这是调试 CSS 的第一站：先看规则有没有出现。规则没出现 = 选择器没匹配或文件没生效；规则出现但被划掉 = 优先级问题。

## 2. Computed 面板：看最终计算值

Styles 面板下面有 Computed（计算后）标签，显示每个属性“最终生效的值”以及来源规则。点某个属性，会展开所有参与竞争的规则和它们各自的权重。

**讲解：** 当多条规则混在一起时，Computed 面板直接告诉你答案：`color` 最终是 `rgb(0, 0, 255)`，来自哪条规则，为什么是它赢。

## 3. 覆盖样式追踪：找“谁赢了”

在 Styles 面板里，被划掉的声明旁边通常有来源文件与行号。点击可跳到对应源码；悬停可看到覆盖它的规则。配合优先级速查（`css/012-CSSPriorityQuickStart`），就能判断是该改权重、改顺序，还是加更具体的类。

**讲解：** 常见结论：第三方库样式覆盖不掉 → 你的选择器权重不够，而不是“库有问题”；“后写不生效” → 前面有更高权重的规则。

## 4. 盒模型可视化

Elements 面板右上角有盒模型图：中间是 content，向外依次是 padding、border、margin，鼠标悬停会高亮页面上的对应区域。

**讲解：** 布局“莫名其妙多了 20px”“两个盒子贴太近”这类问题，用盒模型图一眼就能看出是哪一层占的空间，再回到 `css/003-CSS3BoxModelDetailed` 查属性。

## 5. 常见问题排查清单

| 现象 | 优先检查 |
| --- | --- |
| 样式完全没生效 | 文件保存了吗？`link` 路径对吗？Console 有报错吗？ |
| 规则出现在面板但被划掉 | 优先级：权重、`!important`、行内样式 |
| 规则没出现在面板 | 选择器拼写、大小写、HTML 结构是否匹配 |
| 子元素继承了奇怪的值 | 父级有样式 + `inherit`，或简写属性重置 |
| 改了文件刷新没变化 | 浏览器缓存：勾选 Network 的 Disable cache |
| 只在某种状态下不对 | 伪类（`:hover`）顺序：`:link` → `:visited` → `:hover` → `:active` |

## 6. 动手试试

1. 故意写错选择器（如 `.text` 而 HTML 是 `class="txt"`），用 Elements 面板观察规则未出现；
2. 写两条相同权重的规则，观察 Styles 面板里哪条被划掉；
3. 给元素加 `padding` 和 `border`，用盒模型图确认实际占用尺寸；
4. 进阶挑战：用 Computed 面板找出一个第三方组件被覆盖的属性，再尝试用更高权重覆盖回来。

## 7. 核心知识点

> 一句话记住 CSS 调试：Elements 面板看命中，Computed 面板看结果，被划掉就是被覆盖，没出现就是没匹配。

- Styles 面板按优先级排列所有命中规则；
- 被划掉的声明 = 被更高优先级覆盖；
- Computed 面板显示最终计算值与来源；
- 盒模型图定位 padding/border/margin 空间问题；
- 排查顺序：保存与路径 → 选择器匹配 → 优先级 → 继承与简写 → 缓存。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 用 `!important` 测试 | 会污染真实优先级 | 在 DevTools 里临时勾选，确认后改成正规写法 |
| 只改代码不清理缓存 | 误以为没生效 | Network 面板勾选 Disable cache 并强制刷新 |
| 忽略 Console 报错 | 语法错误会让整段规则失效 | 先看 Console 红色报错与行号 |
| 在压缩产物上调试 | 源码映射缺失难以定位 | 开发环境调试，或开启 sourcemap |

## 9. 扩展学习

- 优先级速查：`css/012-CSSPriorityQuickStart`；
- 优先级深入：`css/009-PriorityCalculation`；
- 选择器匹配：`css/007-CSS3SelectorSystem`；
- 盒模型：`css/003-CSS3BoxModelDetailed`。

<!-- ============ 文档分隔线：007-css/020-TraditionalLayoutTech.md ============ -->

> 前置依赖：先读 003 盒模型与 015 浮动。圣杯/双飞翼布局为进阶内容，0 基础可先跳过。

## 0. 直觉：没有 Flexbox/Grid 的年代怎么排版

在 Flexbox 与 Grid 出现之前，网页排版靠两件“老工具”：浮动（`float`）和定位（`position`）。浮动让元素“靠边站”并让文字环绕，定位让元素“钉”在页面的某个位置。

现代项目已经很少用浮动做整体布局，但很多老代码、打印样式和特殊排版仍在用。理解它们，才能读懂历史代码，也更懂 Flexbox/Grid 解决了什么问题。


## 1. 浮动布局 (Float)

### 1.1 浮动基础

浮动最初是为图文环绕设计的，后来被广泛用于布局。元素设置 `float` 后会脱离文档流，向指定方向靠拢，直到碰到容器边缘或另一个浮动元素。

```css
.float-left {
  float: left;
}
.float-right {
  float: right;
}
```

```html
<div class="container">
  <div class="float-left" style="width:100px;height:100px;background:#e74c3c;">A</div>
  <div class="float-left" style="width:100px;height:100px;background:#3498db;">B</div>
  <p>这段文字会环绕在浮动元素旁边……</p>
</div>
```

> **效果图描述**：两个色块 A（红）、B（蓝）并排靠左，文字在右侧环绕排列。

### 1.2 浮动的副作用——高度塌陷

当子元素全部浮动时，父容器无法感知子元素高度，导致"高度塌陷"：

```css
.parent {
  border: 2px solid #333;
  /* 没有设置 height，子元素浮动后父元素高度为 0 */
}
.child {
  float: left;
  width: 100px;
  height: 100px;
}
```

```html
<div class="parent">
  <div class="child" style="background:#e74c3c;">A</div>
  <div class="child" style="background:#3498db;">B</div>
</div>
<p>这段文字会紧贴在父容器下方，而非在子元素下方</p>
```

> **效果图描述**：父容器边框塌缩为一条线（高度为0），两个色块溢出，后续文字紧贴边框线。

**讲解：** 浮动子元素不参与父元素的高度计算，父容器高度塌成 0，后续内容上移。解决办法见 1.3 的四种 clearfix 方案。

### 1.3 清除浮动（Clearfix）方案汇总

#### 方案一：额外标签法（不推荐）

在浮动元素后添加一个空标签并设置 `clear: both`：

```html
<div class="parent">
  <div class="child">A</div>
  <div class="child">B</div>
  <div style="clear:both;"></div>
</div>
```

缺点：增加无语义标签，违反结构与表现分离原则。

#### 方案二：父元素设置 `overflow: hidden`（BFC 法）

```css
.parent {
  overflow: hidden;
}
```

原理：触发 BFC，BFC 会包含浮动元素。但 `overflow: hidden` 会裁剪溢出内容，不适合需要溢出显示的场景。

#### 方案三：伪元素清除法（推荐 [完成]）

```css
.clearfix::after {
  content: '';
  display: block;
  clear: both;
}
.clearfix {
  *zoom: 1;
}
```

`*zoom: 1` 是 IE6/7 的 hack，触发 hasLayout 以兼容老浏览器。

**讲解：** 伪元素法在容器末尾插入一个 `clear: both` 的隐藏块，是传统方案中的推荐写法；`*zoom` 仅为旧 IE 兼容，现代代码可删除。

#### 方案四：现代 BFC 方案

```css
.parent {
  display: flow-root;
}
```

`display: flow-root` 专门为创建 BFC 设计，无副作用。浏览器支持：Chrome 58+、Firefox 53+、Safari 13+。

**讲解：** `display: flow-root` 专门用于创建 BFC，无副作用、语义清晰，是清除浮动的现代标准写法。

### 1.4 `clear` 属性详解

```css
.clear-left {
  clear: left;
}
.clear-right {
  clear: right;
}
.clear-both {
  clear: both;
}
```

- `clear: left`：元素顶部不允许有左浮动元素
- `clear: right`：元素顶部不允许有右浮动元素
- `clear: both`：两侧都不允许

---

## 2. 定位系统 (Positioning)

CSS `position` 属性控制元素的定位方式，配合 `top`/`right`/`bottom`/`left`/`z-index` 使用。

### 2.1 `static`——默认定位

所有元素默认 `position: static`，遵循正常文档流。`top`/`left` 等偏移属性无效。

```css
.box-static {
  position: static;
  top: 50px;
  left: 100px;
}
```

> **效果图描述**：元素位置无任何变化，`top`/`left` 不生效。

### 2.2 `relative`——相对定位

相对于**自身原位置**偏移，**不脱离文档流**，原位置仍保留空间。

```css
.box-relative {
  position: relative;
  top: 20px;
  left: 30px;
}
```

```html
<div style="background:#ecf0f1;padding:20px;">
  <span>前</span>
  <span class="box-relative" style="background:#e74c3c;color:#fff;padding:5px;">相对定位</span>
  <span>后</span>
</div>
```

> **效果图描述**："相对定位"文字向右下偏移 30px/20px，但原位置仍留有空间，"前""后"文字位置不变。
> **常见用途**：

- 微调元素位置
- 作为 `absolute` 子元素的定位参考

### 2.3 `absolute`——绝对定位

相对于**最近的非 static 祖先**偏移，**脱离文档流**，原位置不保留空间。

```css
.parent-abs {
  position: relative;
  width: 300px;
  height: 200px;
  background: #ecf0f1;
}
.child-abs {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 80px;
  height: 80px;
  background: #e74c3c;
}
```

```html
<div class="parent-abs">
  <div class="child-abs"></div>
</div>
```

> **效果图描述**：灰色容器内，红色方块紧贴右上角（距顶20px、距右20px）。
> **关键要点**：

- 若无已定位祖先，则相对于初始包含块（通常是 `<html>`）
- 绝对定位元素的 `width: auto` 会收缩到内容宽度（类似浮动）
- 常用于弹窗、下拉菜单、角标等

### 2.4 `fixed`——固定定位

相对于**浏览器视口**定位，**脱离文档流**，滚动页面时位置不变。

```css
.nav-fixed {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 50px;
  background: #2c3e50;
  color: #fff;
  z-index: 1000;
}
.back-to-top {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  background: #3498db;
  border-radius: 50%;
  cursor: pointer;
}
```

> **效果图描述**：深色导航栏始终固定在页面顶部；蓝色圆形"回到顶部"按钮固定在右下角。
> **注意**：`fixed` 元素的包含块是视口，但如果祖先设置了 `transform`/`perspective`/`filter`，包含块会变为该祖先（这是一个常见"坑"）。

### 2.5 `sticky`——粘性定位

在特定滚动阈值内表现为 `relative`，超出阈值后表现为 `fixed`。

```css
.section-title {
  position: sticky;
  top: 0;
  background: #fff;
  padding: 10px;
  border-bottom: 2px solid #3498db;
  z-index: 10;
}
```

```html
<div style="height:2000px;">
  <h2 class="section-title">第一章</h2>
  <p>内容区域……（很长）</p>
  <h2 class="section-title">第二章</h2>
  <p>内容区域……（很长）</p>
</div>
```

> **效果图描述**：滚动时，章节标题到达页面顶部后"粘住"，直到被下一个标题推出。
> **关键要点**：

- `sticky` 元素不会脱离文档流
- 必须指定 `top`/`bottom`/`left`/`right` 中的至少一个
- 父容器的高度是 sticky 的"活动范围"，超出父容器后 sticky 失效
- 父容器不能设置 `overflow: hidden`/`auto`/`scroll`，否则 sticky 失效

**讲解：** `sticky` 在滚动范围内保持原位，到达阈值（`top: 0`）后“粘住”不动，常用于吸顶导航与章节标题；它需要父容器有足够滚动空间才能生效。

### 2.6 `z-index` 与层叠上下文

`z-index` 仅对 `position` 非 `static` 的元素有效（`sticky` 除外，它天然创建层叠上下文）。

```css
.layer-1 {
  position: absolute;
  z-index: 1;
  background: rgba(231, 76, 60, 0.7);
}
.layer-2 {
  position: absolute;
  z-index: 10;
  background: rgba(52, 152, 219, 0.7);
}
.layer-3 {
  position: absolute;
  z-index: 5;
  background: rgba(46, 204, 113, 0.7);
}
```

**层叠上下文的创建条件**（部分）：

- `position` 非 `static` + `z-index` 非 `auto`
- `opacity` < 1
- `transform` 非 `none`
- `filter` 非 `none`
- `will-change: transform`
- `display: flex/grid` 子元素的 `z-index` 非 `auto`
  > [警告] **常见坑**：子元素的 `z-index` 再高，也无法超越父级层叠上下文的限制。

---

## 3. BFC（块格式化上下文）

### 3.1 什么是 BFC

BFC（Block Formatting Context）是 CSS 中一个独立的渲染区域，内部元素的布局不会影响外部元素。可以把它想象成一个**隔离的布局容器**。

### 3.2 BFC 的布局规则

1. 内部块级盒子垂直方向一个接一个排列
2. 同一个 BFC 中，相邻块级盒子的垂直外边距会发生折叠（margin collapse）
3. BFC 区域不会与浮动元素重叠
4. BFC 可以包含浮动元素（解决高度塌陷）
5. 计算 BFC 高度时，浮动元素也参与计算

### 3.3 触发 BFC 的条件

| 属性       | 值                                                                                                              |
| :--------- | :-------------------------------------------------------------------------------------------------------------- |
| `float`    | `left` / `right`（非 `none`）                                                                                   |
| `position` | `absolute` / `fixed`                                                                                            |
| `display`  | `inline-block` / `table-cell` / `table-caption` / `flex` / `inline-flex` / `grid` / `inline-grid` / `flow-root` |
| `overflow` | `hidden` / `auto` / `scroll`（非 `visible`）                                                                    |
| `contain`  | `layout` / `content` / `paint`                                                                                  |

### 3.4 BFC 的典型应用

#### 应用一：清除浮动（解决高度塌陷）

```css
.container {
  display: flow-root;
}
```

#### 应用二：防止 margin 折叠

```html
<div style="margin-bottom:20px;background:#e74c3c;">A</div>
<div style="margin-top:30px;background:#3498db;">B</div>
```

> **效果图描述**：A 和 B 之间间距为 30px（取较大值），而非 50px。
> 解决方案：将其中一个元素包裹在 BFC 容器中：

```html
<div style="margin-bottom:20px;background:#e74c3c;">A</div>
<div style="overflow:hidden;">
  <div style="margin-top:30px;background:#3498db;">B</div>
</div>
```

> **效果图描述**：A 和 B 之间间距变为 50px（20+30），margin 不再折叠。

#### 应用三：实现自适应两栏布局

浮动元素不会与 BFC 区域重叠，利用这一点实现右侧自适应：

```css
.left {
  float: left;
  width: 200px;
  height: 300px;
  background: #e74c3c;
}
.right {
  overflow: hidden;
  height: 300px;
  background: #3498db;
}
```

```html
<div class="left">固定宽度侧栏</div>
<div class="right">自适应内容区</div>
```

> **效果图描述**：左侧红色固定 200px，右侧蓝色自动填满剩余宽度，不会跑到红色下方。

---

## 4. 传统经典布局

### 4.1 圣杯布局（Holy Grail Layout）

三栏布局：中间自适应，两侧固定宽度。DOM 顺序中间栏优先渲染。

```css
.holy-grail {
  padding: 0 200px 0 150px;
}
.holy-grail .center {
  float: left;
  width: 100%;
  background: #ecf0f1;
  min-height: 300px;
}
.holy-grail .left {
  float: left;
  width: 150px;
  margin-left: -100%;
  position: relative;
  left: -150px;
  background: #e74c3c;
  min-height: 300px;
}
.holy-grail .right {
  float: left;
  width: 200px;
  margin-left: -200px;
  position: relative;
  right: -200px;
  background: #3498db;
  min-height: 300px;
}
```

```html
<div class="holy-grail clearfix">
  <div class="center">Center（主内容区，优先渲染）</div>
  <div class="left">Left（150px）</div>
  <div class="right">Right（200px）</div>
</div>
```

> **效果图描述**：三栏并排——左侧红色 150px，中间灰色自适应，右侧蓝色 200px。中间栏在 DOM 中排在最前。
> **核心原理**：

1. 三栏均左浮动，中间栏 `width: 100%` 占满
2. 左栏 `margin-left: -100%` 移到中间栏左侧
3. 右栏 `margin-left: -200px` 移到中间栏右侧
4. 父容器 `padding` 留出两侧空间，左右栏 `position: relative` 偏移到位

### 4.2 双飞翼布局

与圣杯布局目标相同，但实现方式不同：中间栏内部再包一层，用 `margin` 留空间而非父容器 `padding`。

```css
.double-wing .center-wrap {
  float: left;
  width: 100%;
}
.double-wing .center {
  margin: 0 200px 0 150px;
  background: #ecf0f1;
  min-height: 300px;
}
.double-wing .left {
  float: left;
  width: 150px;
  margin-left: -100%;
  background: #e74c3c;
  min-height: 300px;
}
.double-wing .right {
  float: left;
  width: 200px;
  margin-left: -200px;
  background: #3498db;
  min-height: 300px;
}
```

```html
<div class="double-wing clearfix">
  <div class="center-wrap">
    <div class="center">Center（主内容区）</div>
  </div>
  <div class="left">Left（150px）</div>
  <div class="right">Right（200px）</div>
</div>
```

> **效果图描述**：视觉效果与圣杯布局一致，但中间栏通过内部 margin 而非父容器 padding 留空间。
> **圣杯 vs 双飞翼对比**：
>
> | 对比项         | 圣杯布局                             | 双飞翼布局          |
> | :------------- | :----------------------------------- | :------------------ |
> | 留空间方式     | 父容器 `padding` + 子元素 `relative` | 中间栏内部 `margin` |
> | DOM 层级       | 三栏同级                             | 中间栏多包一层      |
> | `position`     | 左右栏需要 `relative`                | 不需要 `relative`   |
> | 中间栏最小宽度 | 受 `padding` 约束                    | 受 `margin` 约束    |

### 4.3 等高布局

传统方式实现多列等高：

```css
.equal-height {
  overflow: hidden;
}
.equal-height .col {
  float: left;
  width: 33.33%;
  padding-bottom: 9999px;
  margin-bottom: -9999px;
  background: #ecf0f1;
}
.equal-height .col:nth-child(2) {
  background: #bdc3c7;
}
.equal-height .col:nth-child(3) {
  background: #95a5a6;
}
```

> **效果图描述**：三列高度一致，以内容最多的列为准。利用超大 `padding-bottom` + 负 `margin-bottom` 实现。

---

## 5. 居中方案汇总

### 5.1 水平居中

#### 行内元素 / 行内块元素

```css
.parent {
  text-align: center;
}
```

```html
<div class="parent">
  <span>行内元素居中</span>
</div>
```

#### 定宽块级元素

```css
.child {
  width: 200px;
  margin: 0 auto;
}
```

#### 不定宽块级元素

```css
.parent {
  text-align: center;
}
.child {
  display: inline-block;
}
```

### 5.2 垂直居中

#### 单行文本

```css
.single-line {
  height: 50px;
  line-height: 50px;
}
```

#### 多行文本（table-cell）

```css
.parent {
  display: table-cell;
  vertical-align: middle;
  height: 200px;
}
```

#### 绝对定位 + transform

```css
.parent {
  position: relative;
  height: 200px;
}
.child {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

### 5.3 水平垂直居中

#### 方案一：绝对定位 + transform（最经典）

```css
.parent {
  position: relative;
  width: 400px;
  height: 300px;
  background: #ecf0f1;
}
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #e74c3c;
  padding: 20px;
  color: #fff;
}
```

> **效果图描述**：红色方块精确居中在灰色容器正中央。
> **优点**：无需知道子元素尺寸。**缺点**：`transform` 可能影响子元素的 `fixed` 定位。

#### 方案二：绝对定位 + 负 margin（需已知尺寸）

```css
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 200px;
  height: 100px;
  margin-top: -50px;
  margin-left: -100px;
}
```

**优点**：兼容性极好。**缺点**：需要知道子元素宽高。

#### 方案三：绝对定位 + margin: auto（需已知尺寸）

```css
.child {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin: auto;
  width: 200px;
  height: 100px;
}
```

**原理**：绝对定位元素四边为 0 时，浏览器自动计算 `margin` 使其居中。

#### 方案四：table-cell

```css
.parent {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
  width: 400px;
  height: 300px;
}
.child {
  display: inline-block;
}
```

**优点**：兼容 IE8+。**缺点**：`display: table-cell` 对布局有限制。

#### 方案五：Flexbox（现代推荐 [完成]）

```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}
```

**优点**：最简洁，无需知道子元素尺寸。**缺点**：IE9 及以下不支持。

#### 方案六：Grid（最现代）

```css
.parent {
  display: grid;
  place-items: center;
  height: 300px;
}
```

**优点**：代码最少。**缺点**：IE 不支持。

### 5.4 居中方案对比总结

| 方案                   | 需知尺寸 | 兼容性     | 代码量 | 适用场景     |
| :--------------------- | :------- | :--------- | :----- | :----------- |
| absolute + transform   | 否       | IE10+      | 少     | 通用         |
| absolute + 负 margin   | 是       | IE6+       | 中     | 已知尺寸     |
| absolute + margin:auto | 是       | IE8+       | 少     | 已知尺寸     |
| table-cell             | 否       | IE8+       | 多     | 兼容旧浏览器 |
| Flexbox                | 否       | IE10+      | 少     | 现代项目首选 |
| Grid                   | 否       | 现代浏览器 | 最少   | 最新项目     |

---

## 6. 总结

虽然现代开发推荐使用 Flex/Grid，但理解 Float 和 Position 对维护旧项目和处理特定定位需求（如固定导航栏、弹窗）依然至关重要。
**关键要点回顾**：

- **浮动**：图文环绕 → 布局 → 高度塌陷 → clearfix / flow-root
- **定位**：static（默认）→ relative（微调/参照）→ absolute（脱离流/弹窗）→ fixed（视口固定）→ sticky（滚动粘性）
- **BFC**：隔离布局容器，解决塌陷/margin 折叠/自适应两栏
- **经典布局**：圣杯/双飞翼是浮动布局的巅峰应用
- **居中**：从传统 hack 到 Flex/Grid，方案越来越简洁

## 7. 动手试试

### 入门版（必做）

1. 写两个浮动色块和一个段落，观察文字环绕；再给父容器加 `display: flow-root`，观察高度塌陷被修复；
2. 用 `position: absolute` 做一个“右上角关闭按钮”，父元素记得加 `position: relative`；
3. 用 `position: sticky` 做一个吸顶的章节标题，滚动页面观察效果。

### 进阶版（选做）

1. 复刻一个简化版圣杯布局（左、中、右三栏），再用 Flexbox 重写对比；
2. 用 `absolute + transform` 实现水平垂直居中；
3. 用 BFC 实现“左边固定、右边自适应”的两栏布局。

## 8. 核心知识点

> 一句话记住传统布局：`float` 让元素靠边站（记得清浮动），`position` 决定定位参照系；`relative` 是基准，`absolute` 脱离流，`sticky` 会吸顶。

- `float`：文字环绕、横向排列，副作用是高度塌陷；
- 清浮动四法：额外标签、`overflow: hidden`、伪元素 clearfix、`display: flow-root`；
- `static`/`relative`/`absolute`/`fixed`/`sticky` 五种定位，参照系各不相同；
- `absolute` 相对最近的非 static 祖先，`fixed` 相对视口，`sticky` 相对滚动容器；
- BFC 可清除浮动、防止外边距合并、实现自适应两栏；
- 居中优先 Flexbox/Grid，旧项目才用 absolute/table-cell。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 浮动后忘记清 | 父容器高度塌陷 | 用 `display: flow-root` 或 clearfix |
| `absolute` 找不到基准 | 相对整个页面跳动 | 给父元素加 `position: relative` |
| 父容器 `overflow: hidden` | sticky 失效 | 用 `overflow: clip` 或调整结构 |
| 用 float 做整体布局 | 维护困难 | 新项目用 Flexbox/Grid |
| 负 margin 居中 | 尺寸变化就失效 | 用 transform 或 Flexbox |
| 忽略 `z-index` 上下文 | 层级不符合预期 | 理解层叠上下文（见 `css/016-StackingContext`） |

## 10. 扩展学习

- 定位详解：`css/014-PositionDetailed`、`css/016-StackingContext`；
- 浮动专题：`css/015-FloatClear`；
- 现代布局：`css/021-CSS3FlexboxFlexLayout`、`css/022-CSS3GridGridLayout`；
- 边距折叠：`css/013-MarginCollapse`；
- 响应式：`css/033-ResponsiveDesign`。

<!-- ============ 文档分隔线：007-css/021-CSS3FlexboxFlexLayout.md ============ -->

## 1. 核心概念

Flexbox（弹性盒子）是一种一维布局模型，旨在提供一种更高效的方式来布局、对齐和分配容器中项目之间的空间。

### 1.1 Flex Container

Flex Container（弹性容器）是通过设置 `display: flex` 或 `display: inline-flex` 创建的元素。它是所有 Flex Item（弹性项目）的直接父元素。

```css
/* 创建块级弹性容器 */
.container {
  display: flex;
}
/* 创建内联弹性容器 */
.inline-container {
  display: inline-flex;
}
```

### 1.2 Flex Item

Flex Item（弹性项目）是弹性容器的直接子元素。即使是文本节点也会被视为弹性项目。

```html
<div class="container">
  <div class="item">Item 1</div>
  <!-- 弹性项目 -->
  <div class="item">Item 2</div>
  <!-- 弹性项目 -->
  <div class="item">Item 3</div>
  <!-- 弹性项目 -->
</div>
```

### 1.3 主轴与侧轴

- **主轴 (Main Axis)**：弹性项目排列的主要方向，默认为水平方向（从左到右）。
- **侧轴 (Cross Axis)**：与主轴垂直的轴，默认为垂直方向（从上到下）。
  主轴和侧轴的方向由 `flex-direction` 属性决定。

### 1.4 弹性容器的创建

通过设置 `display: flex` 或 `display: inline-flex` 来创建弹性容器。

```css
/* 块级弹性容器 */
.flex-container {
  display: flex;
  /* 其他容器属性 */
}
/* 内联弹性容器 */
.inline-flex-container {
  display: inline-flex;
  /* 其他容器属性 */
}
```

## 2. 容器属性

### 2.1 flex-direction

`flex-direction` 属性定义了弹性容器的主轴方向。

| 值               | 描述                             |
| ---------------- | -------------------------------- |
| `row`            | 主轴为水平方向，从左到右（默认） |
| `row-reverse`    | 主轴为水平方向，从右到左         |
| `column`         | 主轴为垂直方向，从上到下         |
| `column-reverse` | 主轴为垂直方向，从下到上         |

```css
/* 水平方向（默认） */
.container {
  display: flex;
  flex-direction: row;
}
/* 垂直方向 */
.container {
  display: flex;
  flex-direction: column;
}
/* 水平反向 */
.container {
  display: flex;
  flex-direction: row-reverse;
}
/* 垂直反向 */
.container {
  display: flex;
  flex-direction: column-reverse;
}
```

### 2.2 justify-content

`justify-content` 属性定义了弹性项目在主轴上的对齐方式。

| 值              | 描述                             |
| --------------- | -------------------------------- |
| `flex-start`    | 项目对齐到主轴的起始位置（默认） |
| `flex-end`      | 项目对齐到主轴的结束位置         |
| `center`        | 项目在主轴上居中对齐             |
| `space-between` | 项目之间均匀分布，两端对齐       |
| `space-around`  | 项目之间均匀分布，两端有间距     |
| `space-evenly`  | 项目之间和两端都均匀分布         |

```css
/* 主轴起始对齐 */
.container {
  display: flex;
  justify-content: flex-start;
}
/* 主轴居中对齐 */
.container {
  display: flex;
  justify-content: center;
}
/* 项目均匀分布 */
.container {
  display: flex;
  justify-content: space-between;
}
/* 项目均匀分布，两端有间距 */
.container {
  display: flex;
  justify-content: space-around;
}
/* 项目均匀分布，两端和中间间距相等 */
.container {
  display: flex;
  justify-content: space-evenly;
}
```

### 2.3 align-items

`align-items` 属性定义了弹性项目在侧轴上的对齐方式。

| 值           | 描述                       |
| ------------ | -------------------------- |
| `stretch`    | 项目拉伸以填充容器（默认） |
| `flex-start` | 项目对齐到侧轴的起始位置   |
| `flex-end`   | 项目对齐到侧轴的结束位置   |
| `center`     | 项目在侧轴上居中对齐       |
| `baseline`   | 项目以基线对齐             |

```css
/* 侧轴拉伸对齐（默认） */
.container {
  display: flex;
  align-items: stretch;
}
/* 侧轴起始对齐 */
.container {
  display: flex;
  align-items: flex-start;
}
/* 侧轴居中对齐 */
.container {
  display: flex;
  align-items: center;
}
/* 侧轴结束对齐 */
.container {
  display: flex;
  align-items: flex-end;
}
/* 基线对齐 */
.container {
  display: flex;
  align-items: baseline;
}
```

### 2.4 flex-wrap

`flex-wrap` 属性定义了弹性项目是否换行。

| 值             | 描述                             |
| -------------- | -------------------------------- |
| `nowrap`       | 不换行，项目在同一行（默认）     |
| `wrap`         | 换行，项目在多行显示             |
| `wrap-reverse` | 换行，项目在多行显示，但顺序相反 |

```css
/* 不换行（默认） */
.container {
  display: flex;
  flex-wrap: nowrap;
}
/* 换行 */
.container {
  display: flex;
  flex-wrap: wrap;
}
/* 反向换行 */
.container {
  display: flex;
  flex-wrap: wrap-reverse;
}
```

### 2.5 flex-flow

`flex-flow` 是 `flex-direction` 和 `flex-wrap` 的复合属性。

```css
/* 水平方向，不换行（默认） */
.container {
  display: flex;
  flex-flow: row nowrap;
}
/* 垂直方向，换行 */
.container {
  display: flex;
  flex-flow: column wrap;
}
```

### 2.6 align-content

`align-content` 属性定义了多行弹性项目在侧轴上的对齐方式。仅在 `flex-wrap: wrap` 或 `flex-wrap: wrap-reverse` 时有效。

| 值              | 描述                         |
| --------------- | ---------------------------- |
| `stretch`       | 多行拉伸以填充容器（默认）   |
| `flex-start`    | 多行对齐到侧轴的起始位置     |
| `flex-end`      | 多行对齐到侧轴的结束位置     |
| `center`        | 多行在侧轴上居中对齐         |
| `space-between` | 多行之间均匀分布，两端对齐   |
| `space-around`  | 多行之间均匀分布，两端有间距 |

```css
/* 多行拉伸对齐（默认） */
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: stretch;
}
/* 多行居中对齐 */
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
}
/* 多行均匀分布 */
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: space-between;
}
```

## 3. 项目属性

### 3.1 flex-grow

`flex-grow` 属性定义了弹性项目的放大比例，默认为 0。

```css
/* 项目不放大（默认） */
.item {
  flex-grow: 0;
}
/* 项目放大比例为 1 */
.item {
  flex-grow: 1;
}
/* 不同项目的放大比例 */
.item-1 {
  flex-grow: 1;
}
.item-2 {
  flex-grow: 2;
}
.item-3 {
  flex-grow: 1;
}
```

### 3.2 flex-shrink

`flex-shrink` 属性定义了弹性项目的缩小比例，默认为 1。

```css
/* 项目可以缩小（默认） */
.item {
  flex-shrink: 1;
}
/* 项目不可缩小 */
.item {
  flex-shrink: 0;
}
/* 不同项目的缩小比例 */
.item-1 {
  flex-shrink: 1;
}
.item-2 {
  flex-shrink: 2;
}
.item-3 {
  flex-shrink: 1;
}
```

### 3.3 flex-basis

`flex-basis` 属性定义了弹性项目的初始大小，默认为 `auto`。

```css
/* 初始大小为 auto（默认） */
.item {
  flex-basis: auto;
}
/* 初始大小为 200px */
.item {
  flex-basis: 200px;
}
/* 初始大小为 50% */
.item {
  flex-basis: 50%;
}
```

### 3.4 flex

`flex` 是 `flex-grow`、`flex-shrink` 和 `flex-basis` 的复合属性。

```css
/* 默认值：0 1 auto */
.item {
  flex: 0 1 auto;
}
/* 推荐使用：等比分配空间 */
.item {
  flex: 1;
}
/* 不缩小，初始大小为 200px */
.item {
  flex: 0 0 200px;
}
/* 放大比例为 2，缩小比例为 1，初始大小为 100px */
.item {
  flex: 2 1 100px;
}
```

### 3.5 align-self

`align-self` 属性定义了单个弹性项目在侧轴上的对齐方式，覆盖容器的 `align-items` 属性。

| 值           | 描述                                  |
| ------------ | ------------------------------------- |
| `auto`       | 继承容器的 `align-items` 属性（默认） |
| `stretch`    | 项目拉伸以填充容器                    |
| `flex-start` | 项目对齐到侧轴的起始位置              |
| `flex-end`   | 项目对齐到侧轴的结束位置              |
| `center`     | 项目在侧轴上居中对齐                  |
| `baseline`   | 项目以基线对齐                        |

```css
/* 继承容器的 align-items 属性（默认） */
.item {
  align-self: auto;
}
/* 单个项目在侧轴上居中对齐 */
.item {
  align-self: center;
}
/* 单个项目在侧轴上起始对齐 */
.item {
  align-self: flex-start;
}
/* 单个项目在侧轴上结束对齐 */
.item {
  align-self: flex-end;
}
```

### 3.6 order

`order` 属性定义了弹性项目的排列顺序，默认为 0。值越小，排列越靠前。

```css
/* 默认顺序 */
.item {
  order: 0;
}
/* 不同项目的顺序 */
.item-1 {
  order: 3;
}
.item-2 {
  order: 1;
}
.item-3 {
  order: 2;
}
```

## 4. 常见应用场景

### 4.1 垂直水平居中

```css
/* 垂直水平居中 */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}
.item {
  width: 100px;
  height: 100px;
  background-color: #3498db;
}
```

### 4.2 等高布局

```css
/* 等高布局 */
.container {
  display: flex;
}
.item {
  flex: 1;
  padding: 20px;
  border: 1px solid #ddd;
  margin: 10px;
}
```

### 4.3 导航菜单

```css
/* 导航菜单 */
.nav {
  display: flex;
  justify-content: space-between;
  background-color: #333;
  padding: 10px;
}
.nav__logo {
  color: white;
  font-size: 20px;
  font-weight: bold;
}
.nav__menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav__item {
  margin-left: 20px;
}
.nav__link {
  color: white;
  text-decoration: none;
  padding: 5px 10px;
  transition: color 0.3s ease;
}
.nav__link:hover {
  color: #3498db;
}
```

### 4.4 卡片布局

```css
/* 卡片布局 */
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}
.card {
  flex: 1 1 300px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}
.card__title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}
.card__content {
  color: #666;
  line-height: 1.5;
}
```

### 4.5 响应式布局

```css
/* 响应式布局 */
.container {
  display: flex;
  flex-wrap: wrap;
}
.item {
  flex: 1 1 200px;
  margin: 10px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 4px;
}
@media (max-width: 768px) {
  .item {
    flex: 1 1 100%;
  }
}
```

### 4.6 表单布局

```css
/* 表单布局 */
.form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
}
.form__group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.form__label {
  font-weight: bold;
  color: #333;
}
.form__input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}
.form__button {
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.form__button:hover {
  background-color: #2980b9;
}
```

### 4.7 网格系统

```css
/* 网格系统 */
.grid {
  display: flex;
  flex-wrap: wrap;
  margin: -10px;
}
.grid__item {
  flex: 1 1 25%;
  padding: 10px;
  box-sizing: border-box;
}
.grid__content {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 4px;
  height: 100%;
}
@media (max-width: 992px) {
  .grid__item {
    flex: 1 1 33.333%;
  }
}
@media (max-width: 768px) {
  .grid__item {
    flex: 1 1 50%;
  }
}
@media (max-width: 480px) {
  .grid__item {
    flex: 1 1 100%;
  }
}
```

## 5. 响应式设计

### 5.1 媒体查询与 Flexbox

Flexbox 与媒体查询结合使用，可以创建响应式布局。

```css
/* 基础布局 */
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.item {
  flex: 1 1 300px;
}
/* 响应式调整 */
@media (max-width: 992px) {
  .item {
    flex: 1 1 250px;
  }
}
@media (max-width: 768px) {
  .item {
    flex: 1 1 100%;
  }
}
@media (max-width: 480px) {
  .container {
    flex-direction: column;
  }
  .item {
    flex: 1 1 auto;
  }
}
```

### 5.2 响应式导航示例

```css
/* 响应式导航 */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  padding: 10px 20px;
}
.nav__logo {
  color: white;
  font-size: 20px;
  font-weight: bold;
}
.nav__menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav__item {
  margin-left: 20px;
}
.nav__link {
  color: white;
  text-decoration: none;
  padding: 5px 10px;
  transition: color 0.3s ease;
}
.nav__link:hover {
  color: #3498db;
}
/* 移动端菜单按钮 */
.nav__toggle {
  display: none;
  color: white;
  font-size: 24px;
  cursor: pointer;
}
/* 响应式调整 */
@media (max-width: 768px) {
  .nav__toggle {
    display: block;
  }
  .nav__menu {
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    background-color: #333;
    flex-direction: column;
    align-items: center;
    padding: 20px 0;
    display: none;
  }
  .nav__menu.active {
    display: flex;
  }
  .nav__item {
    margin: 10px 0;
  }
}
```

## 6. 性能优化

### 6.1 减少重排

- **避免频繁修改布局属性**：尽量一次性修改多个属性，减少浏览器重排次数。
- **使用 transform 代替 top/left**：transform 不会触发重排，性能更好。
- **使用 will-change**：提前告知浏览器元素可能发生变化，优化渲染。

```css
/* 优化前 */
.item {
  position: relative;
  left: 0;
  transition: left 0.3s ease;
}
.item:hover {
  left: 10px;
}
/* 优化后 */
.item {
  will-change: transform;
  transition: transform 0.3s ease;
}
.item:hover {
  transform: translateX(10px);
}
```

### 6.2 合理使用属性

- **优先使用 flex 复合属性**：`flex: 1` 比单独设置 `flex-grow`, `flex-shrink`, `flex-basis` 更简洁。
- **避免过度嵌套**：减少 flex 容器的嵌套层级，提高渲染性能。
- **合理设置 flex-basis**：使用百分比或固定值，避免使用 `auto` 导致的计算开销。

## 7. 浏览器兼容性

### 7.1 支持情况

Flexbox 在现代浏览器中得到了广泛支持，但在一些旧版本浏览器中可能需要使用前缀。

| 浏览器  | 支持情况       |
| ------- | -------------- |
| Chrome  | 29+            |
| Firefox | 28+            |
| Safari  | 9+             |
| Edge    | 12+            |
| IE      | 10+ (部分支持) |

### 7.2 前缀使用

在一些旧版本浏览器中，需要使用厂商前缀。

```css
/* 带前缀的 Flexbox */
.container {
  display: -webkit-flex; /* Safari */
  display: flex;
  -webkit-flex-direction: row; /* Safari */
  flex-direction: row;
  -webkit-justify-content: center; /* Safari */
  justify-content: center;
  -webkit-align-items: center; /* Safari */
  align-items: center;
}
.item {
  -webkit-flex: 1; /* Safari */
  flex: 1;
}
```

## 8. 最佳实践

### 8.1 代码组织

- **按功能组织**：将相关的样式放在一起。
- **使用注释**：为不同的部分添加注释。
- **模块化**：将样式按模块分离。

### 8.2 命名规范

推荐使用 BEM (Block, Element, Modifier) 命名规范：

```css
/* Block */
.nav {
  display: flex;
  /* 导航样式 */
}
/* Element */
.nav__menu {
  display: flex;
  /* 菜单样式 */
}
/* Modifier */
.nav--responsive {
  /* 响应式导航样式 */
}
```

### 8.3 常见问题与解决方案

#### 问题 1：Flex 项目溢出容器

**解决方案**：使用 `flex-wrap: wrap` 或设置合理的 `flex-basis`。

#### 问题 2：IE 浏览器兼容性

**解决方案**：使用厂商前缀，避免使用一些高级特性。

#### 问题 3：垂直居中对齐问题

**解决方案**：使用 `align-items: center` 或 `align-self: center`。

#### 问题 4：Flex 项目大小不一致

**解决方案**：使用 `flex: 1` 或设置相同的 `flex-basis`。

## 9. 实际应用示例

### 9.1 示例 1：网站头部布局

```html
<header class="header">
  <div class="header__logo">Logo</div>
  <nav class="header__nav">
    <ul class="nav__menu">
      <li class="nav__item"><a href="#" class="nav__link">首页</a></li>
      <li class="nav__item"><a href="#" class="nav__link">关于我们</a></li>
      <li class="nav__item"><a href="#" class="nav__link">产品</a></li>
      <li class="nav__item"><a href="#" class="nav__link">联系我们</a></li>
    </ul>
  </nav>
  <div class="header__actions">
    <button class="button">登录</button>
    <button class="button button--primary">注册</button>
  </div>
</header>
```

```css
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #f8f9fa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.header__logo {
  font-size: 24px;
  font-weight: bold;
  color: #3498db;
}
.nav__menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav__item {
  margin-left: 20px;
}
.nav__link {
  color: #333;
  text-decoration: none;
  padding: 5px 10px;
  transition: color 0.3s ease;
}
.nav__link:hover {
  color: #3498db;
}
.header__actions {
  display: flex;
  gap: 10px;
}
.button {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}
.button--primary {
  background-color: #3498db;
  color: white;
  border-color: #3498db;
}
.button:hover {
  opacity: 0.9;
}
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  .nav__menu {
    flex-direction: column;
    width: 100%;
  }
  .nav__item {
    margin: 5px 0;
  }
  .header__actions {
    width: 100%;
    justify-content: space-between;
  }
}
```

### 9.2 示例 2：产品卡片网格

```html
<div class="products">
  <div class="product-card">
    <div class="product-card__image">
      <img src="product1.jpg" alt="Product 1" />
    </div>
    <div class="product-card__content">
      <h3 class="product-card__title">产品 1</h3>
      <p class="product-card__description">这是产品 1 的描述</p>
      <div class="product-card__footer">
        <span class="product-card__price">¥100</span>
        <button class="product-card__button">加入购物车</button>
      </div>
    </div>
  </div>
  <div class="product-card">
    <div class="product-card__image">
      <img src="product2.jpg" alt="Product 2" />
    </div>
    <div class="product-card__content">
      <h3 class="product-card__title">产品 2</h3>
      <p class="product-card__description">这是产品 2 的描述</p>
      <div class="product-card__footer">
        <span class="product-card__price">¥200</span>
        <button class="product-card__button">加入购物车</button>
      </div>
    </div>
  </div>
  <div class="product-card">
    <div class="product-card__image">
      <img src="product3.jpg" alt="Product 3" />
    </div>
    <div class="product-card__content">
      <h3 class="product-card__title">产品 3</h3>
      <p class="product-card__description">这是产品 3 的描述</p>
      <div class="product-card__footer">
        <span class="product-card__price">¥300</span>
        <button class="product-card__button">加入购物车</button>
      </div>
    </div>
  </div>
  <div class="product-card">
    <div class="product-card__image">
      <img src="product4.jpg" alt="Product 4" />
    </div>
    <div class="product-card__content">
      <h3 class="product-card__title">产品 4</h3>
      <p class="product-card__description">这是产品 4 的描述</p>
      <div class="product-card__footer">
        <span class="product-card__price">¥400</span>
        <button class="product-card__button">加入购物车</button>
      </div>
    </div>
  </div>
</div>
```

```css
.products {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}
.product-card {
  flex: 1 1 250px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}
.product-card__image {
  height: 200px;
  overflow: hidden;
}
.product-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}
.product-card:hover .product-card__image img {
  transform: scale(1.05);
}
.product-card__content {
  padding: 20px;
}
.product-card__title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}
.product-card__description {
  color: #666;
  line-height: 1.5;
  margin-bottom: 15px;
}
.product-card__footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.product-card__price {
  font-size: 20px;
  font-weight: bold;
  color: #e74c3c;
}
.product-card__button {
  padding: 8px 16px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.product-card__button:hover {
  background-color: #2980b9;
}
@media (max-width: 768px) {
  .product-card {
    flex: 1 1 100%;
  }
}
```

### 9.3 示例 3：页脚布局

```html
<footer class="footer">
  <div class="footer__container">
    <div class="footer__section">
      <h3 class="footer__title">关于我们</h3>
      <p class="footer__text">这是关于我们的描述，介绍公司的历史、使命和愿景。</p>
    </div>
    <div class="footer__section">
      <h3 class="footer__title">快速链接</h3>
      <ul class="footer__links">
        <li><a href="#" class="footer__link">首页</a></li>
        <li><a href="#" class="footer__link">关于我们</a></li>
        <li><a href="#" class="footer__link">产品</a></li>
        <li><a href="#" class="footer__link">联系我们</a></li>
      </ul>
    </div>
    <div class="footer__section">
      <h3 class="footer__title">联系我们</h3>
      <ul class="footer__contact">
        <li>电话：123-456-7890</li>
        <li>邮箱：info@example.com</li>
        <li>地址：北京市朝阳区</li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <p class="footer__copyright">2026 公司名称. 保留所有权利.</p>
  </div>
</footer>
```

```css
.footer {
  background-color: #333;
  color: white;
  padding: 40px 20px;
}
.footer__container {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
}
.footer__section {
  flex: 1 1 250px;
}
.footer__title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #3498db;
}
.footer__text {
  line-height: 1.5;
  margin-bottom: 20px;
}
.footer__links {
  list-style: none;
  margin: 0;
  padding: 0;
}
.footer__links li {
  margin-bottom: 10px;
}
.footer__link {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;
}
.footer__link:hover {
  color: #3498db;
}
.footer__contact {
  list-style: none;
  margin: 0;
  padding: 0;
}
.footer__contact li {
  margin-bottom: 10px;
  line-height: 1.5;
}
.footer__bottom {
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #555;
  text-align: center;
}
.footer__copyright {
  font-size: 14px;
  color: #999;
}
@media (max-width: 768px) {
  .footer__section {
    flex: 1 1 100%;
  }
}
```

## 10. 总结

Flexbox 是一种强大的一维布局模型，具有以下优势：

- **简单易用**：通过简洁的属性即可实现复杂的布局。
- **灵活响应**：轻松创建响应式布局，适应不同屏幕尺寸。
- **对齐方便**：提供多种对齐方式，解决传统布局的对齐问题。
- **空间分配**：智能分配项目之间的空间，实现均匀分布。
- **等高布局**：默认实现等高效果，无需额外设置。
  Flexbox 的核心概念包括：
- **弹性容器**：通过 `display: flex` 创建。
- **弹性项目**：容器的直接子元素。
- **主轴与侧轴**：控制项目的排列方向。
- **容器属性**：控制整体布局，如 `flex-direction`, `justify-content`, `align-items` 等。
- **项目属性**：控制单个项目的行为，如 `flex-grow`, `flex-shrink`, `flex-basis` 等。
  通过掌握 Flexbox，开发者可以更加灵活地控制页面布局，创建美观、响应式的网页设计。Flexbox 不仅简化了布局代码，还提高了开发效率，是现代前端开发中不可或缺的布局工具。

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

## 本章综合挑战（选做）

1. 用 Flexbox 重写“头部导航 + 中部内容 + 页脚”三行布局，头部左右分布、中部水平垂直居中；
2. 做一组可换行的产品卡片，最小宽度 200px，并用 `gap` 控制间距；
3. 用 `flex: 1` 实现等分布局，再对比 `flex: 0 0 200px` 的固定宽度行为；
4. 在 768px 断点以下把导航改为纵向堆叠。

## 核心知识点

> 一句话记住 Flexbox：容器 `display: flex`，主轴 `justify-content`，侧轴 `align-items`，项目伸缩用 `flex: 1`；`gap` 管间距，`wrap` 管换行。

- 两个角色：弹性容器（`display: flex`）与弹性项目（直接子元素）；
- 主轴方向由 `flex-direction` 决定，`justify-content`/`align-items` 语义随之互换；
- 项目属性：`flex-grow` 放大、`flex-shrink` 缩小、`flex-basis` 初始尺寸；
- `flex: 1` 等比分配，`flex: 0 0 200px` 固定尺寸；
- `flex-wrap: wrap` 换行，`gap` 统一间距；
- 两行居中：`justify-content: center; align-items: center`。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 只设容器不设项目 | 项目不伸缩 | 理解 grow/shrink/basis 三兄弟 |
| 忘记 `flex-wrap` | 项目被压缩 | 需要换行时显式 `wrap` |
| 用 margin 做间距 | 最后一个项目多出边距 | 用 `gap` |
| 主轴方向搞混 | 横竖对齐错乱 | 先画主轴，再选属性 |
| `flex` 简写记错顺序 | 行为意外 | 记住 grow shrink basis，或用 `flex: 1` |
| 旧浏览器兼容 | 前缀与语法差异 | 确认目标浏览器，必要时 Autoprefixer |

## 扩展学习

- Grid 对比：`css/022-CSS3GridGridLayout` 一维与二维布局的选择；
- 响应式：`css/033-ResponsiveDesign` 中 Flexbox 与媒体查询配合；
- 经典布局：`css/020-TraditionalLayoutTech` 对比浮动方案；
- 实战：`css/067-CSSProjectExampleResponsiveHomepage` 完整响应式首页。

<!-- ============ 文档分隔线：007-css/022-CSS3GridGridLayout.md ============ -->

> 前置依赖：基础选择器与盒模型。本篇为完整版，可配合 068-Grid 速查复习。

## 1. 核心概念

Grid 布局是一种二维布局系统，能够同时处理行和列，为网页布局提供了更灵活、更强大的方式。

### 1.1 Grid Container

Grid Container（网格容器）是通过设置 `display: grid` 或 `display: inline-grid` 创建的元素。它是所有 Grid Item（网格项目）的直接父元素。

```css
/* 创建块级网格容器 */
.container {
  display: grid;
}
/* 创建内联网格容器 */
.inline-container {
  display: inline-grid;
}
```

### 1.2 Grid Track

Grid Track（网格轨道）是网格中的行或列。

```css
/* 定义三列网格轨道 */
.container {
  display: grid;
  grid-template-columns: 100px 200px 100px;
}
/* 定义两行网格轨道 */
.container {
  display: grid;
  grid-template-rows: 50px 100px;
}
```

### 1.3 Grid Cell

Grid Cell（网格单元格）是网格中最小的单位，由相邻的两条行线和两条列线围成的区域。

### 1.4 Grid Area

Grid Area（网格区域）是由多个网格单元格组成的矩形区域。

```css
/* 定义网格区域 */
.container {
  display: grid;
  grid-template-areas:
    'header header header'
    'sidebar main main'
    'footer footer footer';
}
.header {
  grid-area: header;
}
.sidebar {
  grid-area: sidebar;
}
.main {
  grid-area: main;
}
.footer {
  grid-area: footer;
}
```

### 1.5 Grid Line

Grid Line（网格线）是网格中划分行和列的线，包括水平网格线（行线）和垂直网格线（列线）。

### 1.6 Grid Gap

Grid Gap（网格间距）是网格轨道之间的空间。

```css
/* 设置网格间距 */
.container {
  display: grid;
  gap: 20px;
}
```

## 2. 容器属性

### 2.1 display

`display` 属性用于创建网格容器。

| 值            | 描述             |
| ------------- | ---------------- |
| `grid`        | 创建块级网格容器 |
| `inline-grid` | 创建内联网格容器 |

```css
/* 块级网格容器 */
.container {
  display: grid;
}
/* 内联网格容器 */
.container {
  display: inline-grid;
}
```

### 2.2 grid-template-columns

`grid-template-columns` 属性定义网格的列轨道。

```css
/* 使用固定值 */
.container {
  display: grid;
  grid-template-columns: 100px 200px 100px;
}
/* 使用百分比 */
.container {
  display: grid;
  grid-template-columns: 25% 50% 25%;
}
/* 使用分数单位 */
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
}
/* 使用混合单位 */
.container {
  display: grid;
  grid-template-columns: 100px 1fr 2fr;
}
/* 使用重复函数 */
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
/* 使用自动填充 */
.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}
/* 使用自动适应 */
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}
```

### 2.3 grid-template-rows

`grid-template-rows` 属性定义网格的行轨道。

```css
/* 使用固定值 */
.container {
  display: grid;
  grid-template-rows: 50px 100px 50px;
}
/* 使用百分比 */
.container {
  display: grid;
  grid-template-rows: 20% 60% 20%;
}
/* 使用分数单位 */
.container {
  display: grid;
  grid-template-rows: 1fr 2fr 1fr;
}
/* 使用混合单位 */
.container {
  display: grid;
  grid-template-rows: 50px 1fr 50px;
}
/* 使用重复函数 */
.container {
  display: grid;
  grid-template-rows: repeat(3, 1fr);
}
```

### 2.4 grid-template-areas

`grid-template-areas` 属性定义命名的网格区域。

```css
/* 定义网格区域 */
.container {
  display: grid;
  grid-template-areas:
    'header header header'
    'sidebar main main'
    'footer footer footer';
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: 60px 1fr 60px;
}
.header {
  grid-area: header;
  background-color: #3498db;
  color: white;
  padding: 20px;
}
.sidebar {
  grid-area: sidebar;
  background-color: #f0f0f0;
  padding: 20px;
}
.main {
  grid-area: main;
  background-color: white;
  padding: 20px;
}
.footer {
  grid-area: footer;
  background-color: #333;
  color: white;
  padding: 20px;
}
```

### 2.5 grid-template

`grid-template` 是 `grid-template-columns`、`grid-template-rows` 和 `grid-template-areas` 的复合属性。

```css
/* 复合属性 */
.container {
  display: grid;
  grid-template:
    'header header header' 60px
    'sidebar main main' 1fr
    'footer footer footer' 60px
    / 200px 1fr 1fr;
}
```

### 2.6 gap

`gap` 是 `row-gap` 和 `column-gap` 的复合属性，定义网格轨道之间的间距。

```css
/* 设置行和列间距 */
.container {
  display: grid;
  gap: 20px;
}
/* 设置不同的行和列间距 */
.container {
  display: grid;
  gap: 10px 20px;
}
```

### 2.7 row-gap

`row-gap` 属性定义网格行之间的间距。

```css
/* 设置行间距 */
.container {
  display: grid;
  row-gap: 20px;
}
```

### 2.8 column-gap

`column-gap` 属性定义网格列之间的间距。

```css
/* 设置列间距 */
.container {
  display: grid;
  column-gap: 20px;
}
```

### 2.9 justify-items

`justify-items` 属性定义网格项目在列轴上的对齐方式。

| 值        | 描述                         |
| --------- | ---------------------------- |
| `stretch` | 项目拉伸以填充单元格（默认） |
| `start`   | 项目对齐到单元格的起始边缘   |
| `end`     | 项目对齐到单元格的结束边缘   |
| `center`  | 项目在单元格中居中对齐       |

```css
/* 项目在列轴上居中对齐 */
.container {
  display: grid;
  justify-items: center;
}
```

### 2.10 align-items

`align-items` 属性定义网格项目在行轴上的对齐方式。

| 值         | 描述                         |
| ---------- | ---------------------------- |
| `stretch`  | 项目拉伸以填充单元格（默认） |
| `start`    | 项目对齐到单元格的起始边缘   |
| `end`      | 项目对齐到单元格的结束边缘   |
| `center`   | 项目在单元格中居中对齐       |
| `baseline` | 项目以基线对齐               |

```css
/* 项目在行轴上居中对齐 */
.container {
  display: grid;
  align-items: center;
}
```

### 2.11 place-items

`place-items` 是 `align-items` 和 `justify-items` 的复合属性。

```css
/* 项目在单元格中居中对齐 */
.container {
  display: grid;
  place-items: center;
}
/* 不同的行轴和列轴对齐方式 */
.container {
  display: grid;
  place-items: start end;
}
```

### 2.12 justify-content

`justify-content` 属性定义网格容器在列轴上的对齐方式。

| 值              | 描述                         |
| --------------- | ---------------------------- |
| `stretch`       | 网格拉伸以填充容器（默认）   |
| `start`         | 网格对齐到容器的起始边缘     |
| `end`           | 网格对齐到容器的结束边缘     |
| `center`        | 网格在容器中居中对齐         |
| `space-between` | 网格之间均匀分布，两端对齐   |
| `space-around`  | 网格之间均匀分布，两端有间距 |
| `space-evenly`  | 网格之间和两端都均匀分布     |

```css
/* 网格在列轴上居中对齐 */
.container {
  display: grid;
  justify-content: center;
}
```

### 2.13 align-content

`align-content` 属性定义网格容器在行轴上的对齐方式。

| 值              | 描述                         |
| --------------- | ---------------------------- |
| `stretch`       | 网格拉伸以填充容器（默认）   |
| `start`         | 网格对齐到容器的起始边缘     |
| `end`           | 网格对齐到容器的结束边缘     |
| `center`        | 网格在容器中居中对齐         |
| `space-between` | 网格之间均匀分布，两端对齐   |
| `space-around`  | 网格之间均匀分布，两端有间距 |
| `space-evenly`  | 网格之间和两端都均匀分布     |

```css
/* 网格在行轴上居中对齐 */
.container {
  display: grid;
  align-content: center;
}
```

### 2.14 place-content

`place-content` 是 `align-content` 和 `justify-content` 的复合属性。

```css
/* 网格在容器中居中对齐 */
.container {
  display: grid;
  place-content: center;
}
/* 不同的行轴和列轴对齐方式 */
.container {
  display: grid;
  place-content: start end;
}
```

### 2.15 grid-auto-columns

`grid-auto-columns` 属性定义自动生成的列轨道的大小。

```css
/* 自动生成的列轨道大小 */
.container {
  display: grid;
  grid-auto-columns: 100px;
}
```

### 2.16 grid-auto-rows

`grid-auto-rows` 属性定义自动生成的行轨道的大小。

```css
/* 自动生成的行轨道大小 */
.container {
  display: grid;
  grid-auto-rows: 100px;
}
```

### 2.17 grid-auto-flow

`grid-auto-flow` 属性定义自动放置项目的方式。

| 值       | 描述             |
| -------- | ---------------- |
| `row`    | 按行填充（默认） |
| `column` | 按列填充         |
| `dense`  | 尝试填充空白区域 |

```css
/* 按列填充 */
.container {
  display: grid;
  grid-auto-flow: column;
}
/* 按行填充并尝试填充空白区域 */
.container {
  display: grid;
  grid-auto-flow: row dense;
}
```

### 2.18 grid

`grid` 是 `grid-template-rows`、`grid-template-columns`、`grid-template-areas`、`grid-auto-rows`、`grid-auto-columns` 和 `grid-auto-flow` 的复合属性。

```css
/* 复合属性 */
.container {
  display: grid;
  grid:
    'header header' 60px
    'sidebar main' 1fr
    'footer footer' 60px
    / 200px 1fr;
}
```

## 3. 项目属性

### 3.1 grid-column-start

`grid-column-start` 属性定义网格项目的起始列线。

```css
/* 项目从第 1 列线开始 */
.item {
  grid-column-start: 1;
}
/* 使用命名的列线 */
.container {
  display: grid;
  grid-template-columns: [col1-start] 1fr [col2-start] 1fr [col3-start] 1fr [col3-end];
}
.item {
  grid-column-start: col2-start;
}
```

### 3.2 grid-column-end

`grid-column-end` 属性定义网格项目的结束列线。

```css
/* 项目到第 3 列线结束 */
.item {
  grid-column-end: 3;
}
/* 使用命名的列线 */
.item {
  grid-column-end: col3-end;
}
/* 跨越 2 列 */
.item {
  grid-column-end: span 2;
}
```

### 3.3 grid-column

`grid-column` 是 `grid-column-start` 和 `grid-column-end` 的复合属性。

```css
/* 从第 1 列线到第 3 列线 */
.item {
  grid-column: 1 / 3;
}
/* 从第 2 列线开始，跨越 2 列 */
.item {
  grid-column: 2 / span 2;
}
/* 使用命名的列线 */
.item {
  grid-column: col1-start / col3-end;
}
```

### 3.4 grid-row-start

`grid-row-start` 属性定义网格项目的起始行线。

```css
/* 项目从第 1 行线开始 */
.item {
  grid-row-start: 1;
}
/* 使用命名的行线 */
.container {
  display: grid;
  grid-template-rows: [row1-start] 1fr [row2-start] 1fr [row3-start] 1fr [row3-end];
}
.item {
  grid-row-start: row2-start;
}
```

### 3.5 grid-row-end

`grid-row-end` 属性定义网格项目的结束行线。

```css
/* 项目到第 3 行线结束 */
.item {
  grid-row-end: 3;
}
/* 使用命名的行线 */
.item {
  grid-row-end: row3-end;
}
/* 跨越 2 行 */
.item {
  grid-row-end: span 2;
}
```

### 3.6 grid-row

`grid-row` 是 `grid-row-start` 和 `grid-row-end` 的复合属性。

```css
/* 从第 1 行线到第 3 行线 */
.item {
  grid-row: 1 / 3;
}
/* 从第 2 行线开始，跨越 2 行 */
.item {
  grid-row: 2 / span 2;
}
/* 使用命名的行线 */
.item {
  grid-row: row1-start / row3-end;
}
```

### 3.7 grid-area

`grid-area` 属性定义网格项目的区域，可以是命名的区域或行/列的起始和结束线。

```css
/* 使用命名的区域 */
.item {
  grid-area: header;
}
/* 使用行/列的起始和结束线 */
.item {
  grid-area: 1 / 1 / 3 / 4;
}
```

### 3.8 justify-self

`justify-self` 属性定义单个网格项目在列轴上的对齐方式，覆盖容器的 `justify-items` 属性。

| 值        | 描述                                    |
| --------- | --------------------------------------- |
| `auto`    | 继承容器的 `justify-items` 属性（默认） |
| `stretch` | 项目拉伸以填充单元格                    |
| `start`   | 项目对齐到单元格的起始边缘              |
| `end`     | 项目对齐到单元格的结束边缘              |
| `center`  | 项目在单元格中居中对齐                  |

```css
/* 单个项目在列轴上居中对齐 */
.item {
  justify-self: center;
}
```

### 3.9 align-self

`align-self` 属性定义单个网格项目在行轴上的对齐方式，覆盖容器的 `align-items` 属性。

| 值         | 描述                                  |
| ---------- | ------------------------------------- |
| `auto`     | 继承容器的 `align-items` 属性（默认） |
| `stretch`  | 项目拉伸以填充单元格                  |
| `start`    | 项目对齐到单元格的起始边缘            |
| `end`      | 项目对齐到单元格的结束边缘            |
| `center`   | 项目在单元格中居中对齐                |
| `baseline` | 项目以基线对齐                        |

```css
/* 单个项目在行轴上居中对齐 */
.item {
  align-self: center;
}
```

### 3.10 place-self

`place-self` 是 `align-self` 和 `justify-self` 的复合属性。

```css
/* 单个项目在单元格中居中对齐 */
.item {
  place-self: center;
}
/* 不同的行轴和列轴对齐方式 */
.item {
  place-self: start end;
}
```

## 4. Grid vs Flexbox

### 4.1 适用场景对比

| 特性       | Flexbox                                        | Grid                                               |
| ---------- | ---------------------------------------------- | -------------------------------------------------- |
| 维度       | 一维（行或列）                                 | 二维（行和列）                                     |
| 适用场景   | 内容驱动的小部件、线性排列、导航菜单、卡片布局 | 整体页面布局、复杂的重叠设计、网格系统、响应式布局 |
| 主要优势   | 简单易用、适合处理动态内容、良好的对齐能力     | 强大的二维布局能力、直观的区域定义、更好的控制     |
| 浏览器支持 | 广泛支持，包括旧版本浏览器                     | 现代浏览器支持良好，旧版本浏览器支持有限           |

### 4.2 组合使用

Flexbox 和 Grid 可以组合使用，发挥各自的优势。

```css
/* 使用 Grid 布局整体页面结构 */
.page {
  display: grid;
  grid-template-areas:
    'header header'
    'sidebar main'
    'footer footer';
  grid-template-columns: 200px 1fr;
  grid-template-rows: 60px 1fr 60px;
  height: 100vh;
}
/* 使用 Flexbox 布局导航菜单 */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}
/* 使用 Flexbox 布局卡片容器 */
.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}
.card {
  flex: 1 1 200px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}
```

## 5. 响应式设计

### 5.1 媒体查询与 Grid

Grid 与媒体查询结合使用，可以创建响应式布局。

```css
/* 基础布局 */
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
/* 响应式调整 */
@media (max-width: 1200px) {
  .container {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 992px) {
  .container {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 768px) {
  .container {
    grid-template-columns: 1fr;
  }
}
```

### 5.2 响应式网格示例

```html
<div class="grid-container">
  <div class="grid-item">Item 1</div>
  <div class="grid-item">Item 2</div>
  <div class="grid-item">Item 3</div>
  <div class="grid-item">Item 4</div>
  <div class="grid-item">Item 5</div>
  <div class="grid-item">Item 6</div>
  <div class="grid-item">Item 7</div>
  <div class="grid-item">Item 8</div>
</div>
```

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}
.grid-item {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 4px;
  text-align: center;
}
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    padding: 15px;
  }
}
@media (max-width: 480px) {
  .grid-container {
    grid-template-columns: 1fr;
    gap: 10px;
    padding: 10px;
  }
}
```

## 6. 性能优化

### 6.1 减少重排

- **避免频繁修改布局属性**：尽量一次性修改多个属性，减少浏览器重排次数。
- **使用 transform 代替 top/left**：transform 不会触发重排，性能更好。
- **使用 will-change**：提前告知浏览器元素可能发生变化，优化渲染。

### 6.2 合理使用属性

- **优先使用简写属性**：如 `grid`、`place-items` 等，减少代码量。
- **避免过度嵌套**：减少网格容器的嵌套层级，提高渲染性能。
- **合理设置网格大小**：使用 `fr` 单位和 `minmax()` 函数，避免不必要的计算。

## 7. 浏览器兼容性

### 7.1 支持情况

Grid 在现代浏览器中得到了广泛支持，但在一些旧版本浏览器中可能需要使用前缀。

| 浏览器  | 支持情况 |
| ------- | -------- |
| Chrome  | 57+      |
| Firefox | 52+      |
| Safari  | 10.1+    |
| Edge    | 16+      |
| IE      | 不支持   |

### 7.2 前缀使用

在一些旧版本浏览器中，需要使用厂商前缀。

```css
/* 带前缀的 Grid */
.container {
  display: -ms-grid; /* IE */
  display: grid;
  -ms-grid-columns: 1fr 2fr 1fr;
  grid-template-columns: 1fr 2fr 1fr;
  -ms-grid-rows: 50px 1fr 50px;
  grid-template-rows: 50px 1fr 50px;
}
.item {
  -ms-grid-column: 1;
  -ms-grid-column-span: 3;
  grid-column: 1 / 4;
}
```

## 8. 最佳实践

### 8.1 代码组织

- **按功能组织**：将相关的样式放在一起。
- **使用注释**：为不同的部分添加注释。
- **模块化**：将样式按模块分离。

### 8.2 命名规范

推荐使用 BEM (Block, Element, Modifier) 命名规范：

```css
/* Block */
.grid {
  display: grid;
  /* 网格样式 */
}
/* Element */
.grid__item {
  /* 网格项目样式 */
}
/* Modifier */
.grid--responsive {
  /* 响应式网格样式 */
}
```

### 8.3 常见问题与解决方案

#### 问题 1：网格项目溢出容器

**解决方案**：使用 `minmax()` 函数和 `auto-fill`/`auto-fit` 来创建响应式网格。

#### 问题 2：IE 浏览器兼容性

**解决方案**：使用厂商前缀，或提供 Flexbox 作为降级方案。

#### 问题 3：网格项目大小不一致

**解决方案**：使用 `fr` 单位或固定值来确保项目大小一致。

#### 问题 4：网格区域命名冲突

**解决方案**：使用清晰、唯一的区域名称，避免冲突。

## 9. 实际应用示例

### 9.1 示例 1：网站布局

```html
<div class="page">
  <header class="header">Header</header>
  <aside class="sidebar">Sidebar</aside>
  <main class="main">Main Content</main>
  <footer class="footer">Footer</footer>
</div>
```

```css
.page {
  display: grid;
  grid-template-areas:
    'header header header'
    'sidebar main main'
    'footer footer footer';
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: 60px 1fr 60px;
  height: 100vh;
  gap: 10px;
  padding: 10px;
  box-sizing: border-box;
}
.header {
  grid-area: header;
  background-color: #3498db;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}
.sidebar {
  grid-area: sidebar;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}
.main {
  grid-area: main;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.footer {
  grid-area: footer;
  background-color: #333;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
}
@media (max-width: 768px) {
  .page {
    grid-template-areas:
      'header'
      'main'
      'sidebar'
      'footer';
    grid-template-columns: 1fr;
    grid-template-rows: 60px 1fr 200px 60px;
  }
}
```

### 9.2 示例 2：卡片网格

```html
<div class="card-grid">
  <div class="card">
    <h3 class="card__title">Card 1</h3>
    <p class="card__content">This is card 1 content</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 2</h3>
    <p class="card__content">This is card 2 content</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 3</h3>
    <p class="card__content">This is card 3 content</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 4</h3>
    <p class="card__content">This is card 4 content</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 5</h3>
    <p class="card__content">This is card 5 content</p>
  </div>
  <div class="card">
    <h3 class="card__title">Card 6</h3>
    <p class="card__content">This is card 6 content</p>
  </div>
</div>
```

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 20px;
}
.card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
}
.card__title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}
.card__content {
  color: #666;
  line-height: 1.5;
}
@media (max-width: 768px) {
  .card-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 15px;
    padding: 15px;
  }
}
@media (max-width: 480px) {
  .card-grid {
    grid-template-columns: 1fr;
    gap: 10px;
    padding: 10px;
  }
}
```

### 9.3 示例 3：仪表盘布局

```html
<div class="dashboard">
  <div class="dashboard__widget dashboard__widget--large">
    <h3>销售统计</h3>
    <p>本月销售额: ¥100,000</p>
  </div>
  <div class="dashboard__widget">
    <h3>用户数量</h3>
    <p>活跃用户: 1,200</p>
  </div>
  <div class="dashboard__widget">
    <h3>订单数量</h3>
    <p>今日订单: 50</p>
  </div>
  <div class="dashboard__widget dashboard__widget--large">
    <h3>热门产品</h3>
    <ul>
      <li>产品 1</li>
      <li>产品 2</li>
      <li>产品 3</li>
    </ul>
  </div>
  <div class="dashboard__widget">
    <h3>转化率</h3>
    <p>转化率: 15%</p>
  </div>
  <div class="dashboard__widget">
    <h3>客单价</h3>
    <p>客单价: ¥200</p>
  </div>
</div>
```

```css
.dashboard {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 200px);
  gap: 20px;
  padding: 20px;
}
.dashboard__widget {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.dashboard__widget--large {
  grid-column: span 2;
}
.dashboard__widget h3 {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}
.dashboard__widget p {
  font-size: 24px;
  font-weight: bold;
  color: #3498db;
}
.dashboard__widget ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
.dashboard__widget li {
  padding: 5px 0;
  border-bottom: 1px solid #f0f0f0;
}
@media (max-width: 992px) {
  .dashboard {
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(3, 200px);
  }
  .dashboard__widget--large {
    grid-column: span 2;
  }
}
@media (max-width: 768px) {
  .dashboard {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(6, 150px);
  }
  .dashboard__widget--large {
    grid-column: span 1;
  }
}
```

## 10. 总结

Grid 布局是一种强大的二维布局系统，具有以下优势：

- **二维布局**：同时处理行和列，提供更灵活的布局能力。
- **直观的区域定义**：通过 `grid-template-areas` 可以直观地定义布局结构。
- **强大的空间分配**：使用 `fr` 单位和 `minmax()` 函数，可以智能分配空间。
- **响应式设计**：结合媒体查询，可以创建适应不同屏幕尺寸的布局。
- **良好的浏览器支持**：在现代浏览器中得到广泛支持。
  Grid 布局的核心概念包括：
- **网格容器**：通过 `display: grid` 创建。
- **网格轨道**：行或列。
- **网格单元格**：最小的单位。
- **网格区域**：由多个单元格组成的矩形区域。
- **网格线**：划分行和列的线。
- **网格间距**：轨道之间的空间。
  通过掌握 Grid 布局，开发者可以更加灵活地控制页面布局，创建复杂、美观的网页设计。Grid 布局不仅简化了布局代码，还提高了开发效率，是现代前端开发中不可或缺的布局工具。

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

## 动手试试

1. 用 `grid-template-columns: repeat(3, 1fr)` 做一个三等分布局；
2. 用 `grid-template-areas` 命名区域，实现“头部/主体/侧栏/页脚”布局；
3. 用 `grid-column: 1 / -1` 让元素跨整行；
4. 进阶挑战：用 `auto-fit` + `minmax` 做响应式卡片网格。

## 核心知识点

> 一句话记住 Grid：`display: grid` 建二维网格，`grid-template-columns/rows` 定轨道，`grid-area` 放元素，`auto-fit`+`minmax` 自动响应。

- Grid 是二维布局（行列同时控制），Flexbox 是一维；
- 轨道：`grid-template-columns: 1fr 1fr`、`repeat(3, 1fr)`、`minmax(200px, 1fr)`；
- 区域：`grid-template-areas` + `grid-area: 名称`；
- 显式与隐式网格：超出定义的行列会自动生成；
- `auto-fit`/`auto-fill` + `minmax` 是响应式网格的标准组合；
- 网格线与 `grid-column`/`grid-row` 可精确跨轨。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 与 Flexbox 混用困惑 | 一维/二维场景不分 | 单方向用 flex，整体布局用 grid |
| 忘记 `minmax` | 小屏溢出 | 轨道用 `minmax(0, 1fr)` 防内容撑破 |
| 区域名拼写错误 | 布局失效 | 区域名须与 `grid-area` 一致 |
| 隐式网格意外 | 元素跑出预期位置 | 显式声明轨道或用 `grid-auto-rows` |
| 兼容性 | 旧浏览器不支持 | 提供 flex 兜底 |

## 扩展学习

- 对比 Flexbox：`css/021-CSS3FlexboxFlexLayout`；
- 响应式：`css/033-ResponsiveDesign`；
- 实战：`css/067-CSSProjectExampleResponsiveHomepage`；
- 简版速查：`css/068-Grid`。

<!-- ============ 文档分隔线：007-css/023-PseudoClassPseudoElement.md ============ -->

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

## 1. 伪类概述

伪类用于匹配元素的特定状态。

| 类别     | 示例                           | 说明     |
| -------- | ------------------------------ | -------- |
| 交互状态 | `:hover`, `:focus`, `:active`  | 用户交互 |
| 位置     | `:first-child`, `:nth-child()` | DOM 位置 |
| 输入状态 | `:checked`, `:disabled`        | 表单状态 |
| 否定     | `:not()`                       | 排除匹配 |
| 匹配     | `:is()`, `:where()`, `:has()`  | 复杂匹配 |

## 2. :nth-child()

```css
li:nth-child(3) {
  color: red;
} /* 第 3 个 */
tr:nth-child(odd) {
  background: #f0f0f0;
} /* 奇数 */
li:nth-child(3n + 1) {
  color: blue;
} /* 每 3 个选第 1 个 */
li:nth-child(-n + 3) {
  font-weight: bold;
} /* 前 3 个 */
```

**An+B 语法**：`2n+1` = odd，`2n` = even，`-n+3` = 前3个

### nth-child vs nth-of-type

```html
<div>
  <h1>标题</h1>
  <!-- h1:first-of-type -->
  <p>段落1</p>
  <!-- p:nth-of-type(1) -->
  <p>段落2</p>
  <!-- p:nth-of-type(2) -->
</div>
```

## 3. 否定与匹配伪类

```css
li:not(:last-child) {
  border-bottom: 1px solid #ccc;
}
:is(h1, h2, h3):hover {
  color: blue;
}
:where(h1, h2, h3) {
  margin: 0;
} /* 优先级为 0 */
a:has(> img) {
  border: none;
}
```

## 4. 交互伪类

```css
a:hover {
  color: blue;
}
input:focus-visible {
  box-shadow: 0 0 0 3px rgba(0, 0, 255, 0.3);
}
input:focus-within {
  border-color: blue;
}
button:active {
  transform: scale(0.98);
}
```

## 5. 伪元素

```css
.quote::before {
  content: '\201C';
  font-size: 2em;
}
.clearfix::after {
  content: '';
  display: table;
  clear: both;
}
p::first-line {
  font-weight: bold;
}
p::first-letter {
  font-size: 3em;
  float: left;
}
::selection {
  background: #ff6b6b;
  color: white;
}
input::placeholder {
  color: #999;
}
```
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

## 本章综合挑战（选做）

1. 用 `:nth-child(odd)` 给表格做隔行变色；
2. 用 `::before` 给必填项加红色星号；
3. 用 `:focus-visible` 给键盘焦点加可见描边；
4. 用 `:has()` 实现“含图片的卡片显示大图”；
5. 用计数器自动生成“第 1 节/第 2 节”标题编号。

## 核心知识点

> 一句话记住伪类/伪元素：单冒号看状态（hover、nth-child），双冒号造内容（before、after）；`:not` 排除、`:is` 合并、`:has` 找父。

- 伪类匹配状态与位置：`:hover`、`:focus`、`:active`、`:nth-child`、`:checked`；
- 伪元素生成内容：`::before`/`::after` 必须有 `content`；
- `:nth-child(An+B)` 的语法：`odd`/`even`/`-n+3`；
- `:nth-of-type` 与 `:nth-child` 的区别是“同类型 vs 所有兄弟”；
- `:is()` 合并选择器，`:where()` 合并且优先级为 0，`:has()` 反向匹配父元素；
- 现代增强：`:user-invalid`、`:focus-visible`、`@scope`、计数器。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 伪元素忘记 `content` | 不显示 | 至少写 `content: ''` |
| `:nth-child` 与 `:nth-of-type` 混用 | 选中元素不符合预期 | 按“所有兄弟/同类型”区分 |
| 用 `:hover` 做移动端交互 | 触屏无悬停 | 用 `:focus`/媒体查询 |
| 大量 `:has()` 嵌套 | 匹配性能下降 | 简化选择器或改用类 |
| 移除 `:focus` 样式 | 键盘用户迷失 | 保留 `:focus-visible` 样式 |
| `:where` 优先级困惑 | 覆盖失败 | 记住它优先级为 0 |

## 扩展学习

- 选择器总览：`css/007-CSS3SelectorSystem`；
- 优先级计算：`css/009-PriorityCalculation`；
- 表单状态：`css/031-MediaQuery` 之外的 `:user-invalid` 等交互增强；
- 嵌套与作用域：`css/071-CSSNesting`、`css/070-ScopeAtRule`；
- 伪元素布局：`css/067-CSSProjectExampleResponsiveHomepage` 中的实际应用。

<!-- ============ 文档分隔线：007-css/024-Gradient.md ============ -->

> 0基础速通：读第 0 节直觉与第 1 节核心必读（代码示例）即可；第 6 章深入理解（选读）供进阶。

# 渐变（Gradients）

> 本文以 W3C [CSS Images Module Level 3](https://www.w3.org/TR/css-images-3/) 与 [CSS Images Module Level 4](https://www.w3.org/TR/css-images-4/) 规范为基础，系统阐释 CSS 渐变（Gradients）的几何算法、颜色插值（Color Interpolation）、`linear-gradient` / `radial-gradient` / `conic-gradient` / `repeating-*` 的形式化定义，以及与 SVG 渐变、Tailwind / Bootstrap / Material Design 等框架实践的对接。内容涵盖从 CSS 3（2012）到 CSS Images Level 4（2024）的演进，提供生产级代码示例与工程化解决方案。

---

## 0. 直觉：渐变就是“颜色之间的过渡”

渐变的本质是让颜色从一个点平滑过渡到另一个点：线性渐变沿一条直线过渡（`linear-gradient`），径向渐变从圆心向外扩散（`radial-gradient`），锥形渐变绕一圈过渡（`conic-gradient`）。

先记住一个最小模型：`background: linear-gradient(方向, 起点色, 终点色)`。剩下的参数（角度、色标、重复）都是在这个模型上加细节。

## 1. 核心必读：代码示例
### 1.1 基础示例：线性渐变

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>线性渐变基础示例</title>
<style>
  .gradient-basic {
    width: 300px;
    height: 100px;
    /* 从左到右，红到蓝 */
    background: linear-gradient(to right, red, blue);
    margin: 10px 0;
  }

  .gradient-angle {
    width: 300px;
    height: 100px;
    /* 45deg 角度 */
    background: linear-gradient(45deg, #667eea, #764ba2);
    margin: 10px 0;
  }

  .gradient-multi-stop {
    width: 300px;
    height: 100px;
    /* 多色标 */
    background: linear-gradient(to right, red 0%, yellow 50%, blue 100%);
    margin: 10px 0;
  }

  .gradient-hard-stop {
    width: 300px;
    height: 100px;
    /* 硬边界 */
    background: linear-gradient(to right, red 50%, blue 50%);
    margin: 10px 0;
  }

  .gradient-hard-stop-v2 {
    width: 300px;
    height: 100px;
    /* Level 4 双色标语法 */
    background: linear-gradient(to right, red 25% 50%, blue 50% 75%);
    margin: 10px 0;
  }
</style>
</head>
<body>
  <div class="gradient-basic"></div>
  <div class="gradient-angle"></div>
  <div class="gradient-multi-stop"></div>
  <div class="gradient-hard-stop"></div>
  <div class="gradient-hard-stop-v2"></div>
</body>
</html>
```

**讲解：**

- `linear-gradient(to right, red, blue)` 从左到右过渡，方向关键词可用角度（`45deg`）替代；
- 多色标写法 `linear-gradient(red, yellow, blue)` 让颜色分段过渡；
- “硬边界”用相同位置的色标实现（如 `red 50%, blue 50%`），是条纹与分隔效果的基础。

### 1.2 重复线性渐变：条纹纹理

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>重复线性渐变：条纹纹理</title>
<style>
  .stripes-diagonal {
    width: 300px;
    height: 200px;
    /* 45deg 对角条纹 */
    background: repeating-linear-gradient(
      45deg,
      #fff 0px,
      #fff 10px,
      #000 10px,
      #000 20px
    );
  }

  .stripes-vertical {
    width: 300px;
    height: 200px;
    /* 垂直条纹 */
    background: repeating-linear-gradient(
      to right,
      #667eea 0px,
      #667eea 20px,
      #764ba2 20px,
      #764ba2 40px
    );
  }

  .checkerboard {
    width: 300px;
    height: 300px;
    /* 棋盘格：两层渐变叠加 */
    background:
      repeating-linear-gradient(0deg, transparent 0, transparent 40px, #000 40px, #000 80px),
      repeating-linear-gradient(90deg, transparent 0, transparent 40px, #000 40px, #000 80px);
    background-color: #fff;
  }
</style>
</head>
<body>
  <div class="stripes-diagonal"></div>
  <div class="stripes-vertical"></div>
  <div class="checkerboard"></div>
</body>
</html>
```

### 1.3 径向渐变：光晕效果

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>径向渐变：光晕效果</title>
<style>
  .halo {
    width: 300px;
    height: 300px;
    /* 圆形径向渐变，从中心透明到边缘不透明 */
    background: radial-gradient(
      circle at center,
      transparent 0%,
      transparent 30%,
      rgba(102, 126, 234, 0.5) 60%,
      rgba(118, 75, 162, 0.8) 100%
    );
  }

  .spotlight {
    width: 300px;
    height: 300px;
    /* 椭圆径向渐变，模拟聚光灯 */
    background: radial-gradient(
      ellipse 80% 50% at 50% 50%,
      rgba(255, 255, 255, 0.9) 0%,
      rgba(255, 255, 255, 0.3) 40%,
      transparent 70%
    );
    background-color: #1a1a2e;
  }

  .vignette {
    width: 300px;
    height: 200px;
    /* 暗角效果 */
    background: radial-gradient(
      circle at center,
      transparent 50%,
      rgba(0, 0, 0, 0.8) 100%
    );
    background-color: #4a90e2;
  }
</style>
</head>
<body>
  <div class="halo"></div>
  <div class="spotlight"></div>
  <div class="vignette"></div>
</body>
</html>
```

### 1.4 径向渐变尺寸关键字

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>径向渐变尺寸关键字对比</title>
<style>
  .box {
    width: 200px;
    height: 150px;
    display: inline-block;
    margin: 5px;
    border: 1px solid #ccc;
  }

  .closest-side {
    background: radial-gradient(circle closest-side at 30% 40%, red, blue);
  }

  .farthest-side {
    background: radial-gradient(circle farthest-side at 30% 40%, red, blue);
  }

  .closest-corner {
    background: radial-gradient(circle closest-corner at 30% 40%, red, blue);
  }

  .farthest-corner {
    background: radial-gradient(circle farthest-corner at 30% 40%, red, blue);
  }
</style>
</head>
<body>
  <div class="box closest-side">closest-side</div>
  <div class="box farthest-side">farthest-side</div>
  <div class="box closest-corner">closest-corner</div>
  <div class="box farthest-corner">farthest-corner（默认）</div>
</body>
</html>
```

### 1.5 锥形渐变：饼图与色轮

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>锥形渐变：饼图与色轮</title>
<style>
  .pie-chart {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    /* 饼图：30% 红，30% 黄，40% 绿 */
    background: conic-gradient(
      red 0% 30%,
      yellow 30% 60%,
      green 60% 100%
    );
  }

  .color-wheel {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    /* 色轮：红→黄→绿→青→蓝→品红→红 */
    background: conic-gradient(
      red,
      yellow,
      lime,
      aqua,
      blue,
      magenta,
      red
    );
  }

  .progress-ring {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    /* 进度环：75% 完成 */
    background: conic-gradient(
      #4caf50 0% 75%,
      #e0e0e0 75% 100%
    );
    position: relative;
  }

  /* 中心镂空 */
  .progress-ring::before {
    content: '';
    position: absolute;
    top: 20px;
    left: 20px;
    right: 20px;
    bottom: 20px;
    background: white;
    border-radius: 50%;
  }

  .progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    font-weight: bold;
    z-index: 1;
  }
</style>
</head>
<body>
  <div class="pie-chart"></div>
  <div class="color-wheel"></div>
  <div class="progress-ring">
    <span class="progress-text">75%</span>
  </div>
</body>
</html>
```

### 1.6 渐变文字

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>渐变文字效果</title>
<style>
  .gradient-text {
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(to right, #667eea, #764ba2);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;  /* 兜底 */
  }

  .gradient-text-rainbow {
    font-size: 36px;
    font-weight: bold;
    background: linear-gradient(
      to right,
      #ff0080,
      #ff8c00,
      #ffd700,
      #00ff00,
      #00bfff,
      #8a2be2
    );
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
  }

  /* 可访问性：高对比度模式下移除渐变 */
  @media (prefers-contrast: more) {
    .gradient-text,
    .gradient-text-rainbow {
      -webkit-text-fill-color: initial;
      color: #667eea;
      background: none;
    }
  }
</style>
</head>
<body>
  <h1 class="gradient-text">渐变文字示例</h1>
  <h2 class="gradient-text-rainbow">彩虹渐变文字</h2>
</body>
</html>
```

### 1.7 渐变边框

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>渐变边框效果</title>
<style>
  .gradient-border {
    padding: 20px;
    border: 2px solid transparent;
    /* 双背景：内层白色 + 外层渐变 */
    background:
      linear-gradient(white, white) padding-box,
      linear-gradient(to right, #667eea, #764ba2) border-box;
    border-radius: 8px;
  }

  .gradient-border-rounded {
    padding: 20px;
    border: 3px solid transparent;
    border-radius: 50%;
    background:
      linear-gradient(white, white) padding-box,
      conic-gradient(from 0deg, #ff0080, #ff8c00, #ffd700, #00ff00, #00bfff, #8a2be2, #ff0080) border-box;
  }

  .gradient-border-thick {
    padding: 20px;
    border: 10px solid transparent;
    background:
      linear-gradient(white, white) padding-box,
      linear-gradient(135deg, #667eea, #764ba2, #f093fb) border-box;
    border-radius: 12px;
  }
</style>
</head>
<body>
  <div class="gradient-border">渐变边框（细）</div>
  <div class="gradient-border-rounded">圆形渐变边框</div>
  <div class="gradient-border-thick">渐变边框（粗）</div>
</body>
</html>
```

### 1.8 Oklab 插值对比

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Oklab vs sRGB 插值对比</title>
<style>
  .box {
    width: 100%;
    height: 80px;
    margin: 10px 0;
  }

  /* 默认 sRGB 插值 */
  .srgb-gradient {
    background: linear-gradient(to right, red, blue);
  }

  /* Oklab 插值（更平滑） */
  .oklab-gradient {
    background: linear-gradient(in oklab, red, blue);
  }

  /* LCH 较短色相 */
  .lch-short {
    background: linear-gradient(in oklch shorter hue, red, blue);
  }

  /* LCH 较长色相 */
  .lch-long {
    background: linear-gradient(in oklch longer hue, red, blue);
  }

  /* 暗部对比：sRGB 易出现色带 */
  .srgb-dark {
    background: linear-gradient(to right, #000, #333);
  }

  .oklab-dark {
    background: linear-gradient(in oklab, #000, #333);
  }

  label {
    display: block;
    font-family: monospace;
    margin-top: 20px;
    font-weight: bold;
  }
</style>
</head>
<body>
  <label>sRGB: linear-gradient(to right, red, blue)</label>
  <div class="box srgb-gradient"></div>

  <label>Oklab: linear-gradient(in oklab, red, blue)</label>
  <div class="box oklab-gradient"></div>

  <label>Oklch shorter hue: red → blue（经过品红）</label>
  <div class="box lch-short"></div>

  <label>Oklch longer hue: red → blue（经过黄绿青）</label>
  <div class="box lch-long"></div>

  <label>sRGB 暗部（易出现色带）</label>
  <div class="box srgb-dark"></div>

  <label>Oklab 暗部（更平滑）</label>
  <div class="box oklab-dark"></div>
</body>
</html>
```

### 1.9 多层渐变叠加

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>多层渐变叠加</title>
<style>
  .complex-background {
    width: 400px;
    height: 300px;
    /* 三层渐变叠加：
     * 1. 顶层：径向光晕
     * 2. 中层：对角条纹
     * 3. 底层：线性渐变
     */
    background:
      radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.3), transparent 50%),
      repeating-linear-gradient(
        45deg,
        transparent 0px,
        transparent 20px,
        rgba(255, 255, 255, 0.1) 20px,
        rgba(255, 255, 255, 0.1) 40px
      ),
      linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }

  .mesh-gradient {
    width: 400px;
    height: 300px;
    /* 模拟网格渐变（mesh gradient）：
     * 多个径向渐变叠加，模拟平滑过渡
     */
    background:
      radial-gradient(at 0% 0%, #ff0080 0%, transparent 50%),
      radial-gradient(at 100% 0%, #ff8c00 0%, transparent 50%),
      radial-gradient(at 0% 100%, #00bfff 0%, transparent 50%),
      radial-gradient(at 100% 100%, #8a2be2 0%, transparent 50%),
      #1a1a2e;
  }
</style>
</head>
<body>
  <div class="complex-background"></div>
  <div class="mesh-gradient"></div>
</body>
</html>
```

### 1.10 企业级：可主题化渐变系统

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>企业级可主题化渐变系统</title>
<style>
  :root {
    /* 渐变设计令牌 */
    --gradient-primary: linear-gradient(135deg, #667eea, #764ba2);
    --gradient-success: linear-gradient(135deg, #4caf50, #81c784);
    --gradient-danger: linear-gradient(135deg, #f44336, #e57373);
    --gradient-warning: linear-gradient(135deg, #ff9800, #ffb74d);
    --gradient-info: linear-gradient(135deg, #2196f3, #64b5f6);

    /* 渐变方向令牌 */
    --gradient-direction: 135deg;
  }

  /* 深色主题 */
  [data-theme="dark"] {
    --gradient-primary: linear-gradient(135deg, #4c51bf, #553c9a);
    --gradient-success: linear-gradient(135deg, #38a169, #48bb78);
    --gradient-danger: linear-gradient(135deg, #e53e3e, #fc8181);
  }

  .btn {
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    color: white;
    font-size: 14px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
  }

  .btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }

  .btn-primary { background: var(--gradient-primary); }
  .btn-success { background: var(--gradient-success); }
  .btn-danger { background: var(--gradient-danger); }
  .btn-warning { background: var(--gradient-warning); }
  .btn-info { background: var(--gradient-info); }

  /* 动态渐变：通过 CSS 变量组合 */
  .btn-dynamic {
    background: linear-gradient(
      var(--gradient-direction),
      var(--color-start, #667eea),
      var(--color-end, #764ba2)
    );
  }

  .card {
    padding: 24px;
    border-radius: 12px;
    background: var(--gradient-primary);
    color: white;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
</style>
</head>
<body>
  <div style="display: flex; gap: 12px; flex-wrap: wrap;">
    <button class="btn btn-primary">主按钮</button>
    <button class="btn btn-success">成功</button>
    <button class="btn btn-danger">危险</button>
    <button class="btn btn-warning">警告</button>
    <button class="btn btn-info">信息</button>
  </div>

  <div style="margin-top: 24px;">
    <div class="card">
      <h3>渐变卡片</h3>
      <p>使用设计令牌管理的渐变背景</p>
    </div>
  </div>

  <button class="btn btn-dynamic" 
    style="--color-start: #ff0080; --color-end: #ff8c00; --gradient-direction: to right;">
    动态渐变按钮
  </button>
</body>
</html>
```

### 1.11 渐变动画

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>渐变动画</title>
<style>
  /* 方案 1：通过 background-position 动画 */
  .animated-gradient {
    width: 400px;
    height: 100px;
    background: linear-gradient(
      90deg,
      #667eea,
      #764ba2,
      #f093fb,
      #667eea
    );
    background-size: 300% 100%;
    animation: gradient-shift 3s ease infinite;
  }

  @keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  /* 方案 2：通过 @property 动画色标（CSS Houdini） */
  @property --gradient-color-1 {
    syntax: '<color>';
    initial-value: #667eea;
    inherits: false;
  }

  @property --gradient-color-2 {
    syntax: '<color>';
    initial-value: #764ba2;
    inherits: false;
  }

  .houdini-gradient {
    width: 400px;
    height: 100px;
    background: linear-gradient(
      to right,
      var(--gradient-color-1),
      var(--gradient-color-2)
    );
    animation: color-shift 4s ease infinite alternate;
  }

  @keyframes color-shift {
    0% {
      --gradient-color-1: #667eea;
      --gradient-color-2: #764ba2;
    }
    100% {
      --gradient-color-1: #f093fb;
      --gradient-color-2: #f5576c;
    }
  }

  /* 尊重用户运动偏好 */
  @media (prefers-reduced-motion: reduce) {
    .animated-gradient,
    .houdini-gradient {
      animation: none;
    }
  }
</style>
</head>
<body>
  <div class="animated-gradient"></div>
  <div class="houdini-gradient"></div>
</body>
</html>
```

### 1.12 渐变可视化工具

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>渐变可视化工具</title>
<style>
  body {
    font-family: system-ui, sans-serif;
    max-width: 800px;
    margin: 2rem auto;
    padding: 0 1rem;
  }
  .preview {
    width: 100%;
    height: 200px;
    border-radius: 8px;
    border: 1px solid #dee2e6;
    margin: 1rem 0;
  }
  .controls {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
  }
  label {
    display: block;
    font-size: 0.875rem;
    color: #6c757d;
    margin-bottom: 0.25rem;
  }
  input, select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ced4da;
    border-radius: 4px;
    font-family: monospace;
  }
  .output {
    padding: 1rem;
    background: #212529;
    color: #f8f9fa;
    border-radius: 4px;
    font-family: monospace;
    word-break: break-all;
  }
</style>
</head>
<body>
  <h1>渐变可视化工具</h1>
  <div class="preview" id="preview"></div>
  <div class="controls">
    <div>
      <label>渐变类型</label>
      <select id="type">
        <option value="linear">linear-gradient</option>
        <option value="radial">radial-gradient</option>
        <option value="conic">conic-gradient</option>
      </select>
    </div>
    <div>
      <label>角度 / 位置</label>
      <input id="angle" value="45deg">
    </div>
    <div>
      <label>起始颜色</label>
      <input id="color1" value="#667eea">
    </div>
    <div>
      <label>结束颜色</label>
      <input id="color2" value="#764ba2">
    </div>
    <div>
      <label>插值色彩空间</label>
      <select id="interp">
        <option value="">默认 sRGB</option>
        <option value="in oklab">in oklab</option>
        <option value="in oklch">in oklch</option>
        <option value="in lab">in lab</option>
        <option value="in lch">in lch</option>
      </select>
    </div>
  </div>
  <div class="output" id="output">linear-gradient(45deg, #667eea, #764ba2)</div>

  <script>
    function updateGradient() {
      const type = document.getElementById('type').value;
      const angle = document.getElementById('angle').value;
      const color1 = document.getElementById('color1').value;
      const color2 = document.getElementById('color2').value;
      const interp = document.getElementById('interp').value;

      let gradient;
      if (type === 'linear') {
        gradient = `linear-gradient(${interp ? interp + ', ' : ''}${angle}, ${color1}, ${color2})`;
      } else if (type === 'radial') {
        gradient = `radial-gradient(${interp ? interp + ', ' : ''}circle at ${angle}, ${color1}, ${color2})`;
      } else {
        gradient = `conic-gradient(${interp ? interp + ', ' : ''}from ${angle} at 50% 50%, ${color1}, ${color2})`;
      }

      document.getElementById('preview').style.background = gradient;
      document.getElementById('output').textContent = gradient;
    }

    document.querySelectorAll('input, select').forEach(el => {
      el.addEventListener('input', updateGradient);
    });
    updateGradient();
  </script>
</body>
</html>
```

---

## 2. 对比分析
### 2.1 CSS 渐变 vs SVG 渐变

| 维度 | CSS 渐变 | SVG 渐变 |
| --- | --- | --- |
| **语法** | CSS 属性 `background` | XML `<linearGradient>` / `<radialGradient>` |
| **应用方式** | 直接 `background: linear-gradient(...)` | 通过 `fill="url(#grad)"` 引用 |
| **动画** | 有限（`background-position` 或 Houdini） | 支持 SMIL 与 CSS 动画 |
| **性能** | 浏览器优化，GPU 加速 | 需解析 XML，性能略低 |
| **可维护性** | 简洁，内联于 CSS | 需在 SVG 中定义，引用复杂 |
| **可访问性** | 同 CSS | 同 SVG，支持 ARIA |
| **适用场景** | 背景纹理、按钮、卡片 | 复杂矢量图形、图表 |

### 2.2 主流框架的渐变实践

| 框架 | 渐变工具类 | 自定义方式 |
| --- | --- | --- |
| **Bootstrap 5** | `bg-gradient` 修饰类 | 通过 Sass 变量 `$gradient` |
| **Tailwind CSS v3.4** | `bg-gradient-to-r from-blue-500 to-purple-500` | 通过 `tailwind.config.js` 扩展 |
| **Material Design 3** | 主题色梯度 | 通过 `mdc-theme-*` 变量 |
| **Ant Design 5** | `linear-gradient` 内联 | 通过 `ConfigProvider` 主题 |
| **GitHub Primer** | `color-gradient-*` 工具类 | 通过设计令牌 |

### 2.3 Tailwind vs Bootstrap 的渐变哲学

**Tailwind CSS**：

```html
<!-- 原子工具类组合 -->
<button class="bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-600 hover:to-purple-600">
  按钮
</button>
```

- 优势：灵活，可在 HTML 中快速调整。
- 劣势：类名冗长，复用性弱。

**Bootstrap 5**：

```html
<!-- 预定义渐变类 -->
<button class="btn btn-primary bg-gradient">
  按钮
</button>
```

- 优势：简洁，语义清晰。
- 劣势：自定义渐变需修改 Sass 源码。

### 2.4 色彩空间插值对比

| 色彩空间 | 视觉效果 | 适用场景 | 浏览器支持 |
| --- | --- | --- | --- |
| **sRGB**（默认） | 暗部易出现色带 | 简单渐变、兼容性优先 | 全部 |
| **linearRGB** | 物理准确，略亮 | 物理仿真、光照效果 | Chrome 99+, Safari 16.2+ |
| **Lab** | 感知均匀，平滑 | 设计师审美、品牌色 | Chrome 111+, Safari 16.2+ |
| **LCH** | 色相旋转可控 | 色轮、彩虹渐变 | Chrome 111+, Safari 16.2+ |
| **Oklab** | 改进 Lab，更准确 | 现代首选 | Chrome 111+, Safari 16.2+ |
| **OkLCH** | 色相可控 + 感知均匀 | 现代设计系统首选 | Chrome 111+, Safari 16.2+ |
| **HSL** | 色相直接插值 | 简单色相过渡 | Chrome 99+, Safari 16.2+ |
| **HWB** | 色相 + 白黑分量 | 柔和过渡 | 实验性 |

### 2.5 渐变类型对比

| 渐变类型 | 几何模型 | 典型应用 | 浏览器支持 |
| --- | --- | --- | --- |
| `linear-gradient` | 梯度线 | 背景、按钮、卡片 | 全部 |
| `radial-gradient` | 渐变射线 | 光晕、聚光灯、阴影 | 全部 |
| `conic-gradient` | 渐变弧 | 饼图、色轮、进度环 | Chrome 69+, Safari 12.1+, Firefox 83+ |
| `repeating-linear-gradient` | 周期性梯度线 | 条纹纹理 | 全部 |
| `repeating-radial-gradient` | 周期性渐变射线 | 同心圆纹理 | 全部 |
| `repeating-conic-gradient` | 周期性渐变弧 | 放射状纹理 | Chrome 69+, Safari 12.1+ |

---

## 3. 常见陷阱与最佳实践
### 3.1 陷阱 1：色带效应

**问题**：长渐变中出现颜色断层。

```css
/* 反例：sRGB 暗部渐变易出现色带 */
background: linear-gradient(to bottom, #000, #333);
```

**最佳实践**：使用 `oklab` 插值或叠加噪声。

```css
/* 正例：oklab 插值 */
background: linear-gradient(in oklab, #000, #333);

/* 或叠加噪声 */
background:
  url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><filter id="n"><feTurbulence baseFrequency="0.9"/></filter><rect width="100" height="100" filter="url(%23n)" opacity="0.05"/></svg>'),
  linear-gradient(to bottom, #000, #333);
```

### 3.2 陷阱 2：硬边界滥用

**问题**：硬边界（Hard Stop）形成生硬分界，视觉突兀。

```css
/* 反例：硬边界用于装饰 */
background: linear-gradient(to right, red 50%, blue 50%);
```

**最佳实践**：硬边界仅用于纹理或明确分块，装饰性渐变应平滑过渡。

### 3.3 陷阱 3：`background-clip: text` 兼容性

**问题**：`background-clip: text` 在旧浏览器不支持。

```css
/* 反例：未提供兜底 */
.gradient-text {
  background: linear-gradient(to right, red, blue);
  -webkit-background-clip: text;
  color: transparent;  /* 旧浏览器显示透明文字 */
}
```

**最佳实践**：使用 `-webkit-text-fill-color` 并保留 `color` 兜底。

```css
/* 正例：保留兜底 */
.gradient-text {
  color: #667eea;  /* 兜底色 */
  background: linear-gradient(to right, #667eea, #764ba2);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}
```

### 3.4 陷阱 4：渐变方向歧义

**问题**：`to top right` 与 `45deg` 的渐变方向不同。

```css
/* to top right：从左下到右上 */
background: linear-gradient(to top right, red, blue);

/* 45deg：从下到上偏右 45° */
background: linear-gradient(45deg, red, blue);
```

**最佳实践**：理解规范定义，`to <corner>` 是「指向角落」，`<angle>` 是「梯度线方向」。

### 3.5 陷阱 5：径向渐变尺寸歧义

**问题**：未指定尺寸关键字时，`farthest-corner` 是默认值，可能不符合预期。

```css
/* 默认 farthest-corner */
background: radial-gradient(circle at 30% 40%, red, blue);

/* 显式 closest-side */
background: radial-gradient(circle closest-side at 30% 40%, red, blue);
```

**最佳实践**：显式指定尺寸关键字，避免歧义。

### 3.6 陷阱 6：`conic-gradient` 接缝

**问题**：`conic-gradient` 首尾色标不同时形成接缝。

```css
/* 反例：接缝明显 */
background: conic-gradient(red, yellow, lime, aqua, blue);
```

**最佳实践**：首尾使用相同颜色，或使用 `from <angle>` 调整起始位置。

```css
/* 正例：首尾相同 */
background: conic-gradient(red, yellow, lime, aqua, blue, magenta, red);
```

### 3.7 陷阱 7：渐变动画性能

**问题**：通过 `background-position` 动画渐变可能触发重绘，性能差。

```css
/* 反例：性能差 */
background: linear-gradient(90deg, red, blue);
background-size: 200% 100%;
animation: shift 3s infinite;

@keyframes shift {
  to { background-position: 100% 0; }
}
```

**最佳实践**：使用 `transform` 或 `opacity` 动画，或使用 CSS Houdini `@property`。

```css
/* 正例：Houdini @property */
@property --color1 {
  syntax: '<color>';
  initial-value: red;
  inherits: false;
}

background: linear-gradient(90deg, var(--color1), blue);
animation: color 3s infinite;

@keyframes color {
  to { --color1: green; }
}
```

### 3.8 陷阱 8：可访问性忽视

**问题**：渐变背景上文字对比度不足。

```css
/* 反例：对比度不足 */
.text-on-gradient {
  background: linear-gradient(to right, #667eea, #764ba2);
  color: white;  /* 部分位置对比度 < 4.5:1 */
}
```

**最佳实践**：使用对比度检查工具，确保所有位置满足 WCAG AA 标准。

```css
/* 正例：增加背景色或调整渐变 */
.text-on-gradient {
  background: 
    linear-gradient(to right, rgba(102, 126, 234, 0.9), rgba(118, 75, 162, 0.9)),
    #1a1a2e;  /* 深色背景兜底 */
  color: white;
}
```

---

## 4. 工程实践
### 4.1 渐变设计令牌

```css
/* design-tokens.css - 渐变设计令牌 */
:root {
  /* 主品牌渐变 */
  --gradient-brand: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --gradient-brand-reverse: linear-gradient(135deg, #764ba2 0%, #667eea 100%);

  /* 语义渐变 */
  --gradient-success: linear-gradient(135deg, #4caf50, #81c784);
  --gradient-warning: linear-gradient(135deg, #ff9800, #ffb74d);
  --gradient-danger: linear-gradient(135deg, #f44336, #e57373);
  --gradient-info: linear-gradient(135deg, #2196f3, #64b5f6);

  /* 中性渐变 */
  --gradient-neutral: linear-gradient(135deg, #f5f7fa, #c3cfe2);
  --gradient-neutral-dark: linear-gradient(135deg, #2c3e50, #4ca1af);

  /* 装饰性渐变 */
  --gradient-aurora: linear-gradient(
    135deg,
    #667eea 0%,
    #764ba2 25%,
    #f093fb 50%,
    #f5576c 75%,
    #4facfe 100%
  );

  /* 渐变方向 */
  --direction-horizontal: to right;
  --direction-vertical: to bottom;
  --direction-diagonal: 135deg;
  --direction-diagonal-reverse: -45deg;
}
```

### 4.2 PostCSS 渐变增强

```javascript
// postcss.config.js - PostCSS 渐变增强
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions'],
    }),
    // 添加 -webkit- 前缀（background-clip: text）
    require('postcss-preset-env')({
      stage: 2,
      features: {
        'is-pseudo-class': true,
      },
    }),
  ],
};
```

### 4.3 SCSS 渐变 Mixin

```scss
// _gradients.scss - SCSS 渐变 Mixin 集合

// 线性渐变
@mixin linear-gradient($direction, $colors...) {
  background: linear-gradient($direction, $colors);
}

// 径向渐变
@mixin radial-gradient($shape, $position, $colors...) {
  background: radial-gradient($shape at $position, $colors);
}

// 渐变文字
@mixin gradient-text($gradient) {
  background: $gradient;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

// 渐变边框
@mixin gradient-border($gradient, $border-width: 2px, $radius: 0) {
  border: $border-width solid transparent;
  border-radius: $radius;
  background:
    linear-gradient(white, white) padding-box,
    $gradient border-box;
}

// 使用示例
.button {
  @include linear-gradient(135deg, #667eea, #764ba2);
}

.title {
  @include gradient-text(linear-gradient(to right, #667eea, #764ba2));
}

.card {
  @include gradient-border(
    linear-gradient(135deg, #667eea, #764ba2),
    2px,
    8px
  );
}
```

### 4.4 Tailwind 自定义渐变

```javascript
// tailwind.config.js - 自定义渐变
module.exports = {
  theme: {
    extend: {
      // 自定义渐变颜色
      colors: {
        brand: {
          start: '#667eea',
          end: '#764ba2',
        },
      },
      // 自定义渐变方向
      backgroundImage: {
        'gradient-brand': 'linear-gradient(135deg, #667eea, #764ba2)',
        'gradient-aurora': 'linear-gradient(135deg, #667eea, #764ba2, #f093fb, #f5576c)',
        'gradient-mesh': `
          radial-gradient(at 0% 0%, rgba(255, 0, 128, 0.5), transparent 50%),
          radial-gradient(at 100% 0%, rgba(255, 140, 0, 0.5), transparent 50%),
          radial-gradient(at 100% 100%, rgba(138, 43, 226, 0.5), transparent 50%),
          radial-gradient(at 0% 100%, rgba(0, 191, 255, 0.5), transparent 50%)
        `,
      },
      // 自定义动画
      keyframes: {
        'gradient-shift': {
          '0%, 100%': { 'background-position': '0% 50%' },
          '50%': { 'background-position': '100% 50%' },
        },
      },
      animation: {
        'gradient-shift': 'gradient-shift 3s ease infinite',
      },
    },
  },
};
```

```html
<!-- 使用自定义渐变 -->
<div class="bg-gradient-brand">品牌渐变</div>
<div class="bg-gradient-aurora bg-[length:300%_100%] animate-gradient-shift">
  动态极光渐变
</div>
<div class="bg-gradient-mesh">网格渐变</div>
```

### 4.5 React 渐变组件

```tsx
// GradientBackground.tsx - React 渐变组件
import React from 'react';

interface GradientBackgroundProps {
  type?: 'linear' | 'radial' | 'conic';
  angle?: string;
  colors: string[];
  colorSpace?: 'srgb' | 'oklab' | 'oklch' | 'lab' | 'lch';
  children?: React.ReactNode;
  className?: string;
  style?: React.CSSProperties;
}

export function GradientBackground({
  type = 'linear',
  angle = '135deg',
  colors,
  colorSpace,
  children,
  className,
  style,
}: GradientBackgroundProps) {
  const colorList = colors.join(', ');
  const interp = colorSpace ? `in ${colorSpace}, ` : '';

  let background: string;
  if (type === 'linear') {
    background = `linear-gradient(${interp}${angle}, ${colorList})`;
  } else if (type === 'radial') {
    background = `radial-gradient(${interp}circle at center, ${colorList})`;
  } else {
    background = `conic-gradient(${interp}from ${angle} at 50% 50%, ${colorList})`;
  }

  return (
    <div
      className={className}
      style={{ background, ...style }}
    >
      {children}
    </div>
  );
}

// 使用示例
<GradientBackground
  type="linear"
  angle="135deg"
  colors={['#667eea', '#764ba2']}
  colorSpace="oklab"
  className="min-h-screen flex items-center justify-center"
>
  <h1 className="text-white text-4xl">Hello Gradient</h1>
</GradientBackground>
```

### 4.6 渐变性能优化

```css
/* 性能优化技巧 */

/* 1. 使用 will-change 提示浏览器 */
.animated-gradient {
  background: linear-gradient(90deg, red, blue);
  background-size: 200% 100%;
  animation: shift 3s infinite;
  will-change: background-position;  /* 提示浏览器优化 */
}

/* 2. 避免大尺寸渐变 */
/* 反例：全屏渐变重绘成本高 */
body {
  background: linear-gradient(to bottom, #000, #fff);
  background-attachment: fixed;  /* 固定背景，但移动端性能差 */
}

/* 正例：使用 ::before 伪元素 */
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, #000, #fff);
  z-index: -1;
}

/* 3. 静态渐变避免动画 */
.gradient-static {
  background: linear-gradient(135deg, #667eea, #764ba2);
  /* 不要对 background 属性本身做动画 */
}

/* 4. 使用 transform 代替 background-position */
.gradient-card {
  position: relative;
  overflow: hidden;
}
.gradient-card::before {
  content: '';
  position: absolute;
  inset: -50%;
  background: linear-gradient(135deg, #667eea, #764ba2);
  transition: transform 0.3s;
}
.gradient-card:hover::before {
  transform: rotate(180deg);
}
```

### 4.7 渐变调试工具

```javascript
// 渐变调试工具：解析并可视化色标
function parseGradient(gradientStr) {
  // 简化的渐变解析（生产环境推荐使用 postcss-value-parser）
  const typeMatch = gradientStr.match(/(linear|radial|conic)-gradient/);
  const type = typeMatch ? typeMatch[1] : 'linear';

  // 提取参数
  const innerMatch = gradientStr.match(/gradient\(([^)]+)\)/);
  if (!innerMatch) return null;

  const parts = innerMatch[1].split(',').map(s => s.trim());

  // 解析色标
  const stops = parts
    .filter(p => p.includes('#') || p.includes('rgb') || p.includes('hsl'))
    .map(p => {
      const [color, position] = p.split(/\s+/);
      return { color, position: position || null };
    });

  return { type, stops };
}

// 使用示例
const grad = parseGradient('linear-gradient(to right, red 0%, blue 100%)');
console.log(grad);
// { type: 'linear', stops: [{color: 'red', position: '0%'}, {color: 'blue', position: '100%'}] }
```

### 4.8 Playwright 视觉回归测试

```javascript
// gradient.spec.js - Playwright 视觉回归测试
const { test, expect } = require('@playwright/test');

test.describe('渐变视觉回归测试', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000');
  });

  test('线性渐变正确渲染', async ({ page }) => {
    const element = page.locator('.gradient-linear');
    await expect(element).toHaveCSS('background-image', /linear-gradient/);
  });

  test('渐变文字可见', async ({ page }) => {
    const element = page.locator('.gradient-text');
    // 验证 background-clip
    await expect(element).toHaveCSS('-webkit-background-clip', 'text');
    await expect(element).toHaveCSS('-webkit-text-fill-color', 'transparent');
  });

  test('渐变动画运行', async ({ page }) => {
    const element = page.locator('.animated-gradient');
    // 等待动画运行
    await page.waitForTimeout(100);
    // 验证 animation 属性
    await expect(element).toHaveCSS('animation-name', 'gradient-shift');
  });

  test('OkLab 插值正确应用', async ({ page }) => {
    const element = page.locator('.oklab-gradient');
    const bgImage = await element.evaluate(el =>
      window.getComputedStyle(el).backgroundImage
    );
    expect(bgImage).toContain('oklab');
  });
});
```

---

## 5. 案例研究
### 5.1 Bootstrap 5 的渐变实践

Bootstrap 5 提供 `bg-gradient` 修饰类，将纯色背景转为渐变：

```css
/* Bootstrap 5 源码 */
.bg-gradient {
  background-image: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.15),
    rgba(255, 255, 255, 0)
  );
}

/* 配合 .bg-primary 使用 */
.bg-primary.bg-gradient {
  background-image: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.15),
    rgba(255, 255, 255, 0)
  ), var(--bs-primary);
}
```

**使用方式**：

```html
<div class="bg-primary bg-gradient">渐变背景</div>
```

**特点**：渐变效果较微妙（顶部高光），适合按钮与卡片。

### 5.2 Tailwind CSS v3.4 的渐变实践

Tailwind 提供原子化的渐变工具类：

```html
<!-- 从左到右，蓝到紫 -->
<div class="bg-gradient-to-r from-blue-500 to-purple-500">
  渐变背景
</div>

<!-- 三色渐变 -->
<div class="bg-gradient-to-r from-red-500 via-yellow-500 to-green-500">
  三色渐变
</div>

<!-- 角度渐变 -->
<div class="bg-gradient-to-br from-pink-500 to-orange-500">
  对角渐变
</div>
```

**特点**：原子类组合，灵活度高，适合快速原型。

### 5.3 Material Design 3 的渐变实践

Material Design 3 强调「色彩角色」，渐变用于状态变化：

```css
/* M3 渐变实践 */
.mdc-button--filled {
  background: var(--md-sys-color-primary);
  /* 微妙的高光渐变 */
  background-image: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.1) 0%,
    transparent 100%
  );
}

/* 悬停状态：渐变变深 */
.mdc-button--filled:hover {
  background-image: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.1) 0%,
    rgba(0, 0, 0, 0.05) 100%
  );
}
```

### 5.4 GitHub Primer 的渐变实践

```css
/* Primer 渐变实践 */
.btn-primary {
  background-image: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.15) 0%,
    rgba(255, 255, 255, 0) 100%
  ), #2da44e;
}

/* 渐变边框 */
.gradient-border {
  border: 1px solid transparent;
  background:
    linear-gradient(white, white) padding-box,
    linear-gradient(135deg, #667eea, #764ba2) border-box;
}
```

### 5.5 Stripe 的渐变美学

Stripe 官网以渐变背景闻名，其核心技术是多层径向渐变叠加：

```css
/* Stripe 风格的网格渐变 */
.hero {
  background:
    radial-gradient(at 20% 30%, rgba(102, 126, 234, 0.5), transparent 50%),
    radial-gradient(at 80% 20%, rgba(118, 75, 162, 0.5), transparent 50%),
    radial-gradient(at 50% 80%, rgba(240, 147, 251, 0.5), transparent 50%),
    #0a0a1a;
}
```

### 5.6 生产事故：渐变导致的 CLS

**场景**：某电商首页使用大尺寸渐变背景，导致 Cumulative Layout Shift（CLS）评分恶化。

**根因**：

1. 渐变通过 `background-attachment: fixed` 实现，移动端滚动时重绘成本高。
2. 渐变叠加在图片上，图片加载完成后渐变位置偏移。
3. 渐变动画导致持续重绘。

**解决方案**：

1. 移除 `background-attachment: fixed`，改用 `position: fixed` 伪元素。
2. 为图片容器预留固定尺寸（`aspect-ratio`）。
3. 静态渐变替代动画渐变，或使用 `will-change` 提示。

```css
/* 修复后 */
body::before {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, #667eea, #764ba2);
  z-index: -1;
}

.image-container {
  aspect-ratio: 16 / 9;  /* 预留尺寸 */
}
```

---

### 填空题知识点讲解

**题目 1**：`linear-gradient` 的默认方向是 ________。

**解析讲解**：`to bottom`（从上到下）

**解析讲解**：未指定方向时，`linear-gradient` 默认从上到下，即 `to bottom`，对应角度 `180deg`。

**题目 2**：`repeating-linear-gradient` 的周期由 ________ 决定。

**解析讲解**：最后一个色标的位置

**解析讲解**：`repeating-linear-gradient` 将色标位置模「最后一个色标位置」，形成周期性渐变。例如 `repeating-linear-gradient(45deg, red 0px, blue 20px)` 的周期为 20px。

**题目 3**：CSS Images Level 4 中，`in oklch longer hue` 表示 ________。

**解析讲解**：在 OkLCH 色彩空间中，色相取较长弧插值

**解析讲解**：`longer hue` 关键字指定色相插值取较长弧（>180°），适用于需要经过完整色相轮的渐变。

**题目 4**：`background-clip: text` 需要配合 ________ 属性使文字颜色透明，以显示背景渐变。

**解析讲解**：`-webkit-text-fill-color: transparent`（或 `color: transparent`）

**解析讲解**：`background-clip: text` 将背景裁剪到文字区域，但文字本身的颜色仍会覆盖背景。需通过 `-webkit-text-fill-color: transparent`（WebKit 前缀）或 `color: transparent` 使文字颜色透明。

**题目 5**：`conic-gradient` 的起始角度（12 点方向）可通过 ________ 关键字调整。

**解析讲解**：`from <angle>`

**解析讲解**：`conic-gradient(from 45deg, ...)` 表示从 45° 开始（顺时针），用于调整起始位置，常用于隐藏接缝。

### 编程题知识点讲解

**题目 1**：使用 `conic-gradient` 实现一个 75% 完成的进度环，带中心镂空与百分比文字。

**解析讲解**：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>进度环</title>
<style>
  .progress-ring {
    position: relative;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    /* 75% 完成 */
    background: conic-gradient(
      #4caf50 0% 75%,
      #e0e0e0 75% 100%
    );
  }

  /* 中心镂空 */
  .progress-ring::before {
    content: '';
    position: absolute;
    top: 20px;
    left: 20px;
    right: 20px;
    bottom: 20px;
    background: white;
    border-radius: 50%;
  }

  /* 百分比文字 */
  .progress-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 28px;
    font-weight: bold;
    color: #4caf50;
    z-index: 1;
  }
</style>
</head>
<body>
  <div class="progress-ring">
    <span class="progress-text">75%</span>
  </div>
</body>
</html>
```

**解析讲解**：

1. `conic-gradient` 实现 75% 绿色 + 25% 灰色。
2. `::before` 伪元素实现中心镂空。
3. 绝对定位的 `<span>` 显示百分比。

**题目 2**：使用 `repeating-linear-gradient` 实现棋盘格纹理。

**解析讲解**：

```css
.checkerboard {
  width: 300px;
  height: 300px;
  /* 两层渐变叠加实现棋盘格 */
  background:
    repeating-linear-gradient(0deg, transparent 0, transparent 40px, #000 40px, #000 80px),
    repeating-linear-gradient(90deg, transparent 0, transparent 40px, #000 40px, #000 80px);
  background-color: #fff;
}
```

**解析讲解**：

1. 第一层：水平条纹（0deg），每 40px 交替。
2. 第二层：垂直条纹（90deg），每 40px 交替。
3. 两层叠加形成棋盘格。
4. `background-color: #fff` 提供底色。

**题目 3**：编写 JavaScript 函数，生成随机彩虹渐变字符串。

**解析讲解**：

```javascript
/**
 * 生成随机彩虹渐变
 * @param {number} stops - 色标数量
 * @returns {string} linear-gradient 字符串
 */
function generateRainbowGradient(stops = 5) {
  const colors = [];
  for (let i = 0; i < stops; i++) {
    // 在 HSL 色相轮上均匀分布
    const hue = Math.round((360 / stops) * i);
    const saturation = 70 + Math.random() * 30;  // 70-100%
    const lightness = 50 + Math.random() * 20;   // 50-70%
    colors.push(`hsl(${hue}, ${saturation}%, ${lightness}%)`);
  }

  // 首尾相同，避免接缝（适用于 conic-gradient）
  colors.push(colors[0]);

  return `linear-gradient(in oklch longer hue, ${colors.join(', ')})`;
}

// 使用示例
document.body.style.background = generateRainbowGradient(6);
```

**解析讲解**：

1. 在 HSL 色相轮上均匀分布色标。
2. 随机化饱和度与亮度，增加多样性。
3. 使用 `oklch longer hue` 插值，确保色相完整过渡。
4. 首尾颜色相同，适用于 `conic-gradient`。

### 10.1 W3C 规范

- World Wide Web Consortium. (2019). *CSS Images Module Level 3*. W3C Candidate Recommendation. https://www.w3.org/TR/css-images-3/
- World Wide Web Consortium. (2024). *CSS Images Module Level 4*. W3C Working Draft. https://www.w3.org/TR/css-images-4/
- World Wide Web Consortium. (2023). *CSS Color Module Level 4*. W3C Candidate Recommendation. https://www.w3.org/TR/css-color-4/
- World Wide Web Consortium. (2024). *CSS Color Module Level 5*. W3C Working Draft. https://www.w3.org/TR/css-color-5/
- World Wide Web Consortium. (2022). *CSS Houdini: Properties and Values API Level 1*. W3C Working Draft. https://www.w3.org/TR/css-properties-values-api-1/

### 10.2 学术论文

- Björn Ottosson. (2020). *A perceptual color space for image processing*. https://bottosson.github.io/posts/oklab/
- Smith, A. R. (1978). *Color gamut transform pairs*. ACM SIGGRAPH Computer Graphics, 12(3), 12-19. DOI: 10.1145/965139.807361
- Poynton, C. (2012). *Digital Video and HD: Algorithms and Interfaces* (2nd ed.). Morgan Kaufmann. ISBN: 978-0123919267.
- Sharma, G., & Trussell, H. J. (1997). *Digital color imaging*. IEEE Transactions on Image Processing, 6(7), 901-932. DOI: 10.1109/83.597278

### 10.3 工业实践

- Bootstrap. (2024). *Bootstrap 5.4 Documentation: Background Gradient*. https://getbootstrap.com/docs/5.4/utilities/background/
- Tailwind Labs. (2024). *Tailwind CSS v3.4 Documentation: Background Image*. https://tailwindcss.com/docs/background-image
- Google. (2024). *Material Design 3: Color Roles*. https://m3.material.io/styles/color/roles
- GitHub. (2024). *Primer Design System: Color*. https://primer.style/foundations/color

### 10.4 工具与库

- CSSGradient.io. (2024). *Free CSS Gradient Generator*. https://cssgradient.io/
- Verou, L. (2024). *CSS3 Test: Conic Gradients*. https://leaverou.github.io/conic-gradient/
- Khan, A. (2024). *Gradienta: Free CSS Gradient Generator*. https://gradienta.io/

### 10.5 ACM Reference Format

- World Wide Web Consortium. 2019. *CSS Images Module Level 3*. W3C Candidate Recommendation. Retrieved July 20, 2026 from https://www.w3.org/TR/css-images-3/
- Tab Atkins, and Elika Etemad. 2024. *CSS Images Module Level 4*. W3C Working Draft. Retrieved July 20, 2026 from https://www.w3.org/TR/css-images-4/
- Björn Ottosson. 2020. *A perceptual color space for image processing*. Retrieved July 20, 2026 from https://bottosson.github.io/posts/oklab/
- Alvy Ray Smith. 1978. *Color gamut transform pairs*. In Proceedings of the 5th annual conference on Computer graphics and interactive techniques (SIGGRAPH '78). Association for Computing Machinery, New York, NY, USA, 12-19. DOI: https://doi.org/10.1145/965139.807361
- Charles Poynton. 2012. *Digital Video and HD: Algorithms and Interfaces* (2nd ed.). Morgan Kaufmann, Burlington, MA. ISBN 978-0123919267.

---

### 11.1 经典书籍

- **《CSS Secrets》** - Lea Verou 著，深入探讨渐变与色彩的高级技巧。
- **《Designing Web Interfaces》** - Bill Scott 著，渐变在 UI 设计中的应用。
- **《Color and Light in Nature and Art》** - Samuel J. Williamson 著，色彩理论。
- **《Interaction of Color》** - Josef Albers 著，色彩交互经典。

### 11.3 视频课程

- **Frontend Masters: CSS Grid & Flexbox for Responsive Layouts** - Jen Kramer
- **Lea Verou: CSS Gradients Deep Dive** - CSSConf 演讲
- **Una Kravets: CSS Color Spaces** - Chrome Developers

### 11.4 社区博客

- **CSS-Tricks** - https://css-tricks.com/
- **Smashing Magazine** - https://www.smashingmagazine.com/category/css/
- **Lea Verou's Blog** - https://lea.verou.me/
- **Björn Ottosson's Blog** - https://bottosson.github.io/

### 11.5 规范演进方向

- **CSS Images Level 5 草案**：探讨 `mesh-gradient`（网格渐变）与 `spline-gradient`（样条插值）。
- **CSS Easing Functions Level 2**：渐变色标间的缓动函数。
- **CSS Houdini Paint API**：自定义渐变绘制，突破规范限制。
- **HDR 渐变**：支持 10-bit / 12-bit 色深与广色域。

### 11.6 相关规范

- **[CSS Backgrounds and Borders Module Level 3](https://www.w3.org/TR/css-backgrounds-3/)** - 背景与边框规范。
- **[CSS Color Module Level 4](https://www.w3.org/TR/css-color-4/)** - 色彩规范。
- **[CSS Values and Units Module Level 4](https://www.w3.org/TR/css-values-4/)** - 值与单位规范。
- **[SVG 2: Gradients and Patterns](https://www.w3.org/TR/SVG2/pservers.html)** - SVG 渐变规范。

---

## 6. 深入理解（选读）

> 以下内容适合想彻底搞懂机制原理的读者，第一遍学习可跳过。

### 6.1 历史演进

### 6.1.1 CSS 3（2012）：渐变的诞生

CSS 渐变最初由 Apple 于 2008 年在 WebKit 中以 `-webkit-gradient(linear, ...)` 形式实现，语法较为复杂。2012 年，[CSS Images Module Level 3](https://www.w3.org/TR/css-images-3/) 将其标准化为现代语法：

```css
background: linear-gradient(to right, red, blue);
background: radial-gradient(circle at center, red, blue);
```

CSS 3 渐变的核心贡献：

1. **无需图片资源**：渐变作为 CSS 值，无需 HTTP 请求，提升性能。
2. **可缩放**：矢量特性，任意尺寸下保持清晰。
3. **可动画**：通过 `background-position` 或 CSS Houdini 实现渐变动画（虽有限制）。

### 6.1.2 `conic-gradient` 的引入（2017）

`conic-gradient`（锥形渐变）由 Lea Verou 提议，2017 年在 Chrome 69 与 Safari 12.1 中实现。它填补了 CSS 渐变在「角度方向」上的空白：

```css
background: conic-gradient(red, yellow, lime, aqua, blue, magenta, red);
```

锥形渐变的典型应用：饼图、色轮、进度环。

### 6.1.3 CSS Images Module Level 4（2020-2024）

[CSS Images Module Level 4](https://www.w3.org/TR/css-images-4/) 引入了多项重要改进：

1. **色彩空间插值**：`in oklab`、`in srgb` 等关键字，允许指定插值色彩空间。
2. **双色标语法**：`red 25% 50%` 表示红色从 25% 持续到 50%（硬边界）。
3. **`interpolar` 关键字**：精细控制色相插值（`shorter`、`longer`、`increasing`、`decreasing`）。

```css
/* Level 4 新语法 */
background: linear-gradient(in oklab, red, blue);
background: linear-gradient(in oklch longer hue, red, blue);
background: linear-gradient(red 25%, blue 50% 75%, green);
```

### 6.1.4 色彩空间的演进

| 年份 | 事件 | 核心变化 |
| --- | --- | --- |
| 2008 | WebKit 首次实现渐变 | `-webkit-gradient(linear, ...)` 语法 |
| 2012 | CSS Images Level 3 推荐 | `linear-gradient` / `radial-gradient` 标准化 |
| 2017 | `conic-gradient` 浏览器支持 | 锥形渐变落地 |
| 2020 | CSS Color Level 4 草案 | 引入 `oklab` / `oklch` 色彩空间 |
| 2022 | CSS Images Level 4 草案 | `in oklab` 插值语法 |
| 2023 | `lab()` / `lch()` / `oklab()` 浏览器支持 | 现代色彩空间普及 |
| 2024 | Display P3 与 Rec2020 支持 | 广色域渐变 |

### 6.1.5 演进时间线

| 年份 | 规范/事件 | 核心变化 |
| --- | --- | --- |
| 2008 | WebKit 渐变实现 | 私有语法 |
| 2012 | CSS Images Level 3 | `linear-gradient` / `radial-gradient` 标准化 |
| 2017 | `conic-gradient` | 锥形渐变（Chrome 69+, Safari 12.1+） |
| 2019 | 双色标语法 | `red 25% 50%` 硬边界 |
| 2020 | `in oklab` 插值 | Lab/LCH 色彩空间插值 |
| 2022 | CSS Images Level 4 草案 | 完整的插值控制语法 |
| 2023 | `color-mix()` 函数 | 渐变色标动态混合 |
| 2024 | Display P3 渐变 | 广色域支持 |

---

### 6.2 形式化定义

### 6.2.1 规范条款

依据 [CSS Images Module Level 3 §4](https://www.w3.org/TR/css-images-3/#gradients)：

> A gradient is an image that smoothly transitions from one color to another. CSS defines three types of gradients: linear, radial, and conic.

以及 [CSS Images Module Level 4 §4.1](https://www.w3.org/TR/css-images-4/#linear-gradients)：

> If the first argument to a linear gradient is the keyword `in`, the next keyword specifies the color space used for interpolation.

### 6.2.2 核心术语

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 渐变 | Gradient | 平滑过渡的图像 |
| 梯度线 | Gradient Line | 线性渐变的方向轴 |
| 渐变射线 | Gradient Ray | 径向渐变的中心射线 |
| 渐变弧 | Gradient Arc | 锥形渐变的角度弧 |
| 色标 | Color Stop | 渐变中的颜色锚点 |
| 色标位置 | Color Stop Position | 色标在渐变中的位置（百分比或长度） |
| 插值 | Interpolation | 两色标之间的颜色过渡 |
| 硬边界 | Hard Stop | 两色标位置相同，形成清晰边界 |
| 色带效应 | Banding | 渐变中的颜色断层 |

### 6.2.3 `linear-gradient` 语法

```
linear-gradient() = 
  linear-gradient(
    [ [ <angle> | to <side-or-corner> ] || in <color-space> [ longer | shorter | increasing | decreasing ] hue? ]?,
    <color-stop-list>
  )

<side-or-corner> = [left | right] || [top | bottom]
<color-stop-list> = <color-stop>#{2,}
<color-stop> = <color> <length-percentage>?{1,2}
```

### 6.2.4 `radial-gradient` 语法

```
radial-gradient() = 
  radial-gradient(
    [ [ <ending-shape> || <size> ] [ at <position> ]? ]?,
    <color-stop-list>
  )

<ending-shape> = circle | ellipse
<size> = 
  closest-side | farthest-side | 
  closest-corner | farthest-corner |
  <length> | <length-percentage>{2}
```

### 6.2.5 `conic-gradient` 语法

```
conic-gradient() = 
  conic-gradient(
    [ [ from <angle> ]? [ at <position> ]? ] || in <color-space>,
    <color-stop-list>
  )
```

### 6.2.6 形式化定义：梯度线

设 `linear-gradient` 的方向为 $\theta$（从上至下为 $0°$，顺时针增加），容器尺寸为 $w \times h$。梯度线的长度 $L$ 定义为：

$$
L = |w \sin\theta| + |h \cos\theta|
$$

梯度线的起点与终点位于容器的对角线上，方向由 $\theta$ 决定。色标 $c_i$ 在位置 $p_i \in [0, 1]$ 处，颜色由线性插值得到：

$$
\text{Color}(p) = \text{Interpolate}(c_i, c_{i+1}, \frac{p - p_i}{p_{i+1} - p_i})
$$

其中 $p_i \le p \le p_{i+1}$。

### 6.2.7 形式化定义：径向渐变

设径向渐变的中心为 $(x_0, y_0)$，形状为 `circle` 或 `ellipse`，尺寸由关键字决定：

- `closest-side`：到最近边的距离。
- `farthest-side`：到最远边的距离。
- `closest-corner`：到最近角的距离。
- `farthest-corner`（默认）：到最远角的距离。

对于 `circle` 形状，渐变半径 $r$ 定义为：

$$
r_{\text{closest-side}} = \min(x_0, w - x_0, y_0, h - y_0)
$$

$$
r_{\text{farthest-corner}} = \max\left(\sqrt{x_0^2 + y_0^2}, \sqrt{(w-x_0)^2 + y_0^2}, \ldots\right)
$$

### 6.2.8 形式化定义：锥形渐变

锥形渐变的颜色由角度 $\phi$ 决定（从 12 点方向开始，顺时针）：

$$
\text{Color}(\phi) = \text{Interpolate}(c_i, c_{i+1}, \frac{\phi - \phi_i}{\phi_{i+1} - \phi_i})
$$

其中 $\phi \in [0°, 360°]$。若首尾色标颜色不同，渐变在 $360°$ 处形成「接缝」。

### 6.2.9 颜色插值

CSS Images Level 4 支持的色彩空间：

| 色彩空间 | 语法 | 特性 |
| --- | --- | --- |
| `srgb` | `in srgb` | 默认，sRGB 线性插值 |
| `linearRGB` | `in linearRGB` | 线性 RGB 空间，物理准确 |
| `lab` | `in lab` | CIE Lab 空间，感知均匀 |
| `lch` | `in lch` | CIE LCH 空间，色相旋转 |
| `oklab` | `in oklab` | Oklab 空间（2020），改进 Lab |
| `oklch` | `in oklch` | OkLCH 空间，现代首选 |
| `hsl` | `in hsl` | HSL 空间，色相插值 |
| `hwb` | `in hwb` | HWB 空间 |
| `xyz` | `in xyz` | CIE XYZ 空间 |

色相插值方式（仅 `lch`、`oklch`、`hsl`、`hwb`）：

- `shorter hue`（默认）：取较短弧。
- `longer hue`：取较长弧。
- `increasing hue`：递增方向。
- `decreasing hue`：递减方向。

### 6.2.10 色标位置规则

色标位置的规范化规则：

1. 若首色标未指定位置，默认为 `0%`。
2. 若末色标未指定位置，默认为 `100%`。
3. 若中间色标位置小于前一个，自动调整为前一个的位置。
4. 双色标语法 `red 25% 50%` 等价于 `red 25%, red 50%`，形成硬边界。

形式化地，设色标序列为 $\{(c_i, p_i)\}_{i=1}^{n}$，规范化函数：

$$
p_i' = \max(p_i, p_{i-1}') \quad \text{for } i \ge 2
$$

---

### 6.3 理论推导与原理解析

### 6.3.1 梯度线的几何推导

给定容器尺寸 $w \times h$ 与方向角 $\theta$（从上至下为 $0°$，顺时针），梯度线的方向向量为：

$$
\vec{d} = (\sin\theta, \cos\theta)
$$

梯度线垂直于方向向量的「梯度线长度」$L$ 通过容器的对角线投影得到：

$$
L = |w \sin\theta| + |h \cos\theta|
$$

**证明**：设梯度线方向为 $\vec{d} = (\sin\theta, \cos\theta)$，其垂直方向为 $\vec{n} = (-\cos\theta, \sin\theta)$。容器的四个角在 $\vec{n}$ 方向上的投影差即为梯度线长度：

$$
L = \max_{\text{corners}} \vec{c} \cdot \vec{n} - \min_{\text{corners}} \vec{c} \cdot \vec{n}
$$

展开后得到 $L = |w \sin\theta| + |h \cos\theta|$。

### 6.3.2 颜色插值的数学模型

给定两色标 $c_1 = (r_1, g_1, b_1)$ 与 $c_2 = (r_2, g_2, b_2)$，插值参数 $t \in [0, 1]$。

**sRGB 线性插值**（默认）：

$$
c(t) = (1-t) c_1 + t c_2
$$

**linearRGB 插值**：

先进行 gamma 解码（sRGB → linear），插值后再编码（linear → sRGB）：

$$
c_{\text{linear}}(t) = (1-t) \cdot \text{srgbToLinear}(c_1) + t \cdot \text{srgbToLinear}(c_2)
$$

$$
c(t) = \text{linearToSrgb}(c_{\text{linear}}(t))
$$

**Oklab 插值**：

转换到 Oklab 空间，插值，再转换回 sRGB：

$$
c_{\text{oklab}}(t) = (1-t) \cdot \text{srgbToOklab}(c_1) + t \cdot \text{srgbToOklab}(c_2)
$$

$$
c(t) = \text{oklabToSrgb}(c_{\text{oklab}}(t))
$$

Oklab 空间的优势在于**感知均匀性**：相同数值差对应相同感知色差，因此渐变更平滑。

### 6.3.3 色相插值的歧义

在 HSL / LCH / OkLCH 空间中，色相是角度，两色相之间存在两种插值路径：

- **较短弧**（`shorter`，默认）：取角度差 $< 180°$ 的方向。
- **较长弧**（`longer`）：取角度差 $> 180°$ 的方向。

设两色相为 $h_1$ 与 $h_2$（角度，$[0°, 360°)$），较短弧的角度差：

$$
\Delta h_{\text{short}} = \begin{cases}
h_2 - h_1, & \text{if } |h_2 - h_1| \le 180° \\
h_2 - h_1 - 360°, & \text{if } h_2 - h_1 > 180° \\
h_2 - h_1 + 360°, & \text{if } h_2 - h_1 < -180°
\end{cases}
$$

例如，从红色（$0°$）到蓝色（$240°$）：

- 较短弧：$240° - 0° = 240° > 180°$，取 $240° - 360° = -120°$，即逆时针 $120°$，经过品红。
- 较长弧：$240°$，顺时针 $240°$，经过黄、绿、青。

### 6.3.4 色带效应（Banding）的成因

色带效应是渐变中颜色断层现象，成因包括：

1. **8-bit 量化**：每个通道仅 256 级，长渐变中相邻像素色差小于 1 级时无法区分。
2. **sRGB 非线性**：sRGB 空间的线性插值在感知上不均匀，暗部细节丢失。
3. **显示器精度**：8-bit 显示器无法呈现更细的色差。

**缓解方案**：

1. **使用 `oklab` 插值**：感知均匀，减少暗部断层。
2. **添加微噪声**：通过 SVG 噪声或 `background-image` 叠加细小纹理，打破色带。
3. **使用更高位深**：10-bit / 12-bit 显示器与 HDR 内容。

```css
/* 方案 1：oklab 插值 */
background: linear-gradient(in oklab, #000, #fff);

/* 方案 2：叠加噪声 */
background: 
  url('noise.svg'),
  linear-gradient(to right, #000, #fff);
```

### 6.3.5 硬边界的几何特性

硬边界（Hard Stop）是两色标位置相同的情况，形成清晰的颜色分界：

```css
background: linear-gradient(to right, red 50%, blue 50%);
```

数学上，硬边界处的颜色不连续：

$$
\lim_{p \to 50\%^-} \text{Color}(p) = \text{red}, \quad \lim_{p \to 50\%^+} \text{Color}(p) = \text{blue}
$$

硬边界常用于：

- 条纹纹理（配合 `repeating-linear-gradient`）。
- 分块布局（如双栏分色）。
- 进度条（已完成 vs 未完成）。

### 6.3.6 `repeating-linear-gradient` 的周期性

`repeating-linear-gradient` 将色标位置模 $L$（梯度线长度），形成周期性渐变：

```css
background: repeating-linear-gradient(
  45deg,
  #fff 0px,
  #fff 10px,
  #000 10px,
  #000 20px
);
```

数学上，周期 $T = 20\text{px}$，颜色函数：

$$
\text{Color}(p) = \text{Color}_{\text{base}}(p \mod T)
$$

其中 $\text{Color}_{\text{base}}$ 是基础渐变（$[0, T]$ 范围内）。

### 6.3.7 `conic-gradient` 的接缝问题

`conic-gradient` 在 $0°$ 与 $360°$ 处可能形成「接缝」：

```css
background: conic-gradient(red, yellow, lime, aqua, blue, magenta, red);
```

若首尾色标颜色相同（如上例的 `red`），接缝不可见。若不同，则形成硬边界。

**解决方案**：

1. 首尾使用相同颜色。
2. 使用 `from <angle>` 调整起始角度，将接缝隐藏在不可见区域。
3. 通过 `mask` 遮挡接缝。

### 6.3.8 渐变与可访问性

渐变对可访问性的影响：

1. **对比度**：渐变背景上的文字对比度随位置变化，需确保所有位置满足 WCAG AA 标准（4.5:1）。
2. **色盲友好**：避免仅依赖色相差异传递信息，应配合明度或图案。
3. **`prefers-contrast`**：用户偏好高对比度时，应简化或移除渐变。

```css
@media (prefers-contrast: more) {
  .button {
    background: solid-color;  /* 移除渐变 */
  }
}
```

---

## 7. 本章综合挑战（选做）

1. 用 `linear-gradient` 做一张“红黄蓝”三色过渡的背景，再用角度 45deg 重做一次；
2. 用 `repeating-linear-gradient` 做条纹纹理，并调整色标位置改变条纹宽度；
3. 用 `radial-gradient` 做光晕效果，用 `conic-gradient` 做简易饼图；
4. 用 `background-clip: text` 实现渐变文字，注意兼容性处理。

## 8. 核心知识点

> 一句话记住渐变：`linear` 直线过渡、`radial` 向外扩散、`conic` 绕圈过渡；`repeating-*` 可重复，色标定位置，`background-clip: text` 做渐变文字。

- `linear-gradient(方向, 色标...)`：直线渐变，方向可用角度或关键词；
- `radial-gradient(形状, 色标...)`：从中心向外扩散；
- `conic-gradient`：绕圆心一圈过渡，适合饼图与色轮；
- `repeating-linear/radial-gradient`：重复图案（条纹、网格）；
- 色标位置用百分比或长度控制，相同位置形成硬边界；
- 渐变是 `background-image` 的取值，可与背景色叠加；
- 渐变文字：`background-clip: text` + `color: transparent`。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 色带效应 | 色标过少出现明显分带 | 增加中间色标或用 oklab 插值 |
| 硬边界滥用 | 视觉突兀 | 只在条纹/分隔场景使用 |
| `background-clip: text` 兼容 | 旧浏览器不支持 | 提供纯色兜底 |
| 方向歧义 | `to right` 与 `45deg` 混用 | 统一使用角度或关键词 |
| 渐变动画性能 | 大面积渐变重绘开销大 | 缩小渐变区域或用合成层 |
| 对比度不足 | 渐变文字可读性差 | 保证文字与背景对比度 |

## 10. 扩展学习

- 背景体系：`css/026-BackgroundEnhancement`；
- 颜色与插值：`css/034-ModernColorSpace`（oklab/oklch）；
- 动画：`css/028-CSSAnimationTransition` 中渐变动画；
- 实战：`css/067-CSSProjectExampleResponsiveHomepage` 的渐变应用。

## 附录 A：术语表

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 渐变 | Gradient | 平滑过渡的图像 |
| 梯度线 | Gradient Line | 线性渐变的方向轴 |
| 渐变射线 | Gradient Ray | 径向渐变的中心射线 |
| 渐变弧 | Gradient Arc | 锥形渐变的角度弧 |
| 色标 | Color Stop | 渐变中的颜色锚点 |
| 色标位置 | Color Stop Position | 色标在渐变中的位置 |
| 插值 | Interpolation | 两色标之间的颜色过渡 |
| 硬边界 | Hard Stop | 两色标位置相同 |
| 色带效应 | Banding | 渐变中的颜色断层 |
| 色彩空间 | Color Space | 颜色表示的数学模型 |
| OkLab | OkLab | 感知均匀的色彩空间（2020） |
| OkLCH | OkLCH | OkLab 的极坐标形式 |

## 附录 B：浏览器兼容性

| 特性 | Chrome | Firefox | Safari | Edge | 兼容性 |
| --- | --- | --- | --- | --- | --- |
| `linear-gradient` | 全部 | 全部 | 全部 | 全部 | 100% |
| `radial-gradient` | 全部 | 全部 | 全部 | 全部 | 100% |
| `conic-gradient` | 69+ | 83+ | 12.1+ | 79+ | 95%+ |
| `repeating-*` | 全部 | 全部 | 全部 | 全部 | 100% |
| 双色标语法 `red 25% 50%` | 89+ | 83+ | 15+ | 89+ | 90%+ |
| `in oklab` 插值 | 111+ | 113+ | 16.2+ | 111+ | 80%+ |
| `in oklch` 插值 | 111+ | 113+ | 16.2+ | 111+ | 80%+ |
| `@property` 动画 | 85+ | 128+ | 16.4+ | 85+ | 70%+ |
| `background-clip: text` | 全部（-webkit-） | 49+ | 全部（-webkit-） | 全部 | 95%+ |

## 附录 C：调试检查清单

- [ ] 使用 DevTools 检查渐变背景的 `background-image` 值
- [ ] 验证色标位置是否符合预期
- [ ] 检查 `conic-gradient` 的接缝是否隐藏
- [ ] 验证渐变文字的对比度满足 WCAG AA 标准
- [ ] 检查渐变动画的性能（避免 `background-position` 动画）
- [ ] 测试跨浏览器兼容性（特别是 `oklab` 插值）
- [ ] 验证 `prefers-reduced-motion` 下渐变动画是否暂停
- [ ] 检查 `prefers-contrast: more` 下渐变是否简化
- [ ] 使用 Lighthouse 检查 CLS（Cumulative Layout Shift）
- [ ] 编写 Playwright 视觉回归测试
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

<!-- ============ 文档分隔线：007-css/025-Shadow.md ============ -->

## 1. box-shadow

```css
box-shadow: offset-x offset-y blur-radius spread-radius color inset;
```

```css
.box {
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}
.box {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
.box {
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.07),
    0 2px 4px rgba(0, 0, 0, 0.07),
    0 4px 8px rgba(0, 0, 0, 0.07);
}
```

## 2. text-shadow

```css
.text {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
.neon {
  text-shadow:
    0 0 7px #fff,
    0 0 42px #0fa,
    0 0 82px #0fa;
}
```

## 3. 实战效果

```css
.card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.elevation-1 {
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.12),
    0 1px 2px rgba(0, 0, 0, 0.24);
}
.elevation-2 {
  box-shadow:
    0 3px 6px rgba(0, 0, 0, 0.16),
    0 3px 6px rgba(0, 0, 0, 0.23);
}
```

## 4. drop-shadow 滤镜

```css
.icon {
  filter: drop-shadow(2px 4px 6px rgba(0, 0, 0, 0.3));
}
```

box-shadow 沿盒子形状，drop-shadow 沿元素实际轮廓（适合 PNG 图标）。
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

## 本章综合挑战（选做）

1. 用 CSS 变量定义 `--shadow-sm/md/lg` 三层阴影体系；
2. 做一张 hover 时“抬起”的卡片（阴影变大 + transition）；
3. 给 PNG 图标加 `drop-shadow`，对比 `box-shadow` 的差异；
4. 用 `inset` 做按钮按下态。

## 核心知识点

> 一句话记住阴影：`box-shadow` 六参数（偏移/模糊/扩散/颜色/inset），多层逗号分隔；`text-shadow` 管文字，`drop-shadow` 跟形状。

- `box-shadow: offset-x offset-y blur spread color [inset]`；
- 多层阴影逗号分隔，第一层在最上；
- `inset` 内阴影适合按压/凹陷效果；
- `text-shadow` 作用于文字，可做发光；
- `drop-shadow`（filter）跟随元素形状；
- 阴影建议用变量统一管理，深色模式单独适配。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 阴影过重 | 页面显脏 | 用低透明度（0.08-0.16）小模糊 |
| 阴影不随主题 | 深色模式下刺眼 | 阴影颜色用变量并适配深色 |
| 大量元素阴影 | 绘制开销大 | 减少模糊半径与数量 |
| 用 box-shadow 做图标阴影 | 出现方框 | 用 drop-shadow |
| 忘记 transition | 阴影突变 | hover 变化加过渡 |

## 扩展学习

- 滤镜体系：`css/048-CSSFilters`；
- 背景：`css/026-BackgroundEnhancement`；
- 动画：`css/028-CSSAnimationTransition`；
- 设计令牌：`css/035-CSSVariableCustomAttribute`。

<!-- ============ 文档分隔线：007-css/026-BackgroundEnhancement.md ============ -->

> 0基础速通：读第 0 节直觉与第 1 节核心必读即可；第 6 章深入理解（选读），附录 D 属性速查随用随查。

# 背景增强（Backgrounds & Borders Enhancement）

> 本文以 W3C [CSS Backgrounds and Borders Module Level 3](https://www.w3.org/TR/css-backgrounds-3/) 与 [CSS Backgrounds Module Level 4](https://www.w3.org/TR/css-backgrounds-4/) 规范为基础，系统阐释 CSS 背景系统的层级模型（Layer Model）、`background-image` 多层叠加、`background-size` 缩放算法、`background-clip` 绘制区域、`background-origin` 定位上下文、`background-attachment` 滚动行为的几何与渲染机制，并对接 Bootstrap、Tailwind CSS、Material Design 等主流框架的实践范式。内容涵盖从 CSS 1（1996）到 CSS Backgrounds Level 4（2024）的演进，提供生产级代码示例与工程化解决方案。

---

## 0. 直觉：背景是元素的“画布”

背景就是元素背后的画布，可以填充颜色（`background-color`）、贴图片（`background-image`）、控制平铺与位置（`repeat`/`position`）、叠加多层背景，还能用渐变、混合模式与滤镜做视觉增强。

先记一个最小模型：`background: color image position / size repeat` 的简写顺序。单独用 `background-color` 是最基础也最常用的写法。

## 1. 核心必读：代码示例
### 1.1 基础示例：多背景叠加

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>多背景叠加示例</title>
<style>
  /* 多背景叠加：渐变 + 图像 + 噪声纹理 */
  .hero {
    width: 100%;
    height: 400px;
    background:
      /* 第一层：噪声纹理（最上层） */
      url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><filter id="n"><feTurbulence baseFrequency="0.9"/></filter><rect width="100%" height="100%" filter="url(%23n)" opacity="0.3"/></svg>'),
      /* 第二层：渐变蒙版 */
      linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 100%),
      /* 第三层：背景图像（最底层） */
      url('https://example.com/hero.jpg');
    background-size: auto, cover, cover;
    background-repeat: repeat, no-repeat, no-repeat;
    background-position: center, center, center;
    background-attachment: scroll, scroll, scroll;
    color: white;
    display: flex;
    align-items: flex-end;
    padding: 40px;
    box-sizing: border-box;
  }
</style>
</head>
<body>
  <section class="hero">
    <h1>多背景叠加：噪声 + 蒙版 + 图像</h1>
  </section>
</body>
</html>
```

### 1.2 `background-size: cover` 与 `contain` 对比

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>background-size 对比</title>
<style>
  .container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
  }

  .box {
    width: 100%;
    height: 200px;
    border: 2px solid #333;
    background-image: url('https://example.com/landscape.jpg');
    background-repeat: no-repeat;
    background-position: center;
  }

  .cover {
    background-size: cover;  /* 等比缩放覆盖容器 */
  }

  .contain {
    background-size: contain;  /* 等比缩放完整显示 */
  }

  .length {
    background-size: 300px 150px;  /* 指定尺寸 */
  }

  .percent {
    background-size: 100% 100%;  /* 拉伸填满 */
  }

  .label {
    text-align: center;
    font-family: monospace;
    margin-top: 8px;
    color: #555;
  }
</style>
</head>
<body>
  <div class="container">
    <div>
      <div class="box cover"></div>
      <div class="label">cover</div>
    </div>
    <div>
      <div class="box contain"></div>
      <div class="label">contain</div>
    </div>
    <div>
      <div class="box length"></div>
      <div class="label">300px 150px</div>
    </div>
    <div>
      <div class="box percent"></div>
      <div class="label">100% 100%</div>
    </div>
  </div>
</body>
</html>
```

### 1.3 `background-clip` 区域对比

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>background-clip 区域对比</title>
<style>
  .clip-demo {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 10px dashed rgba(102, 126, 234, 0.5);
    margin: 20px;
    background-image: linear-gradient(45deg, #667eea, #764ba2);
    background-repeat: no-repeat;
    display: inline-block;
    box-sizing: border-box;
    color: white;
    font-family: monospace;
  }

  .clip-border {
    background-clip: border-box;  /* 默认：包含 border */
  }

  .clip-padding {
    background-clip: padding-box;  /* 不含 border */
  }

  .clip-content {
    background-clip: content-box;  /* 仅 content 区域 */
  }
</style>
</head>
<body>
  <div class="clip-demo clip-border">border-box</div>
  <div class="clip-demo clip-padding">padding-box</div>
  <div class="clip-demo clip-content">content-box</div>
</body>
</html>
```

### 1.4 `background-origin` 区域对比

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>background-origin 区域对比</title>
<style>
  .origin-demo {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 10px solid rgba(0,0,0,0.1);
    margin: 20px;
    background-image: url('https://example.com/icon.png');
    background-repeat: no-repeat;
    background-position: 0% 0%;
    background-size: 50px 50px;
    display: inline-block;
    box-sizing: border-box;
    font-family: monospace;
  }

  .origin-border {
    background-origin: border-box;  /* 从 border 起点定位 */
  }

  .origin-padding {
    background-origin: padding-box;  /* 从 padding 起点定位 */
  }

  .origin-content {
    background-origin: content-box;  /* 从 content 起点定位 */
  }
</style>
</head>
<body>
  <div class="origin-demo origin-border">border-box</div>
  <div class="origin-demo origin-padding">padding-box</div>
  <div class="origin-demo origin-content">content-box</div>
</body>
</html>
```

### 1.5 渐变文字效果

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>渐变文字效果</title>
<style>
  .gradient-text {
    font-size: 64px;
    font-weight: 900;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;  /* 回退方案 */
    text-align: center;
    padding: 40px;
  }

  /* 多色渐变文字 */
  .rainbow-text {
    font-size: 48px;
    font-weight: 700;
    background: linear-gradient(
      to right,
      #ff0000, #ff7f00, #ffff00,
      #00ff00, #0000ff, #4b0082, #9400d3
    );
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    text-align: center;
  }

  /* 带动画的渐变文字 */
  .animated-gradient-text {
    font-size: 56px;
    font-weight: 800;
    background: linear-gradient(
      90deg,
      #667eea, #764ba2, #f093fb, #667eea
    );
    background-size: 300% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
    animation: gradient-shift 3s linear infinite;
  }

  @keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
  }
</style>
</head>
<body>
  <h1 class="gradient-text">渐变文字效果</h1>
  <h2 class="rainbow-text">彩虹文字</h2>
  <h2 class="animated-gradient-text">动态渐变</h2>
</body>
</html>
```

### 1.6 `background-attachment` 滚动行为

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>background-attachment 滚动行为</title>
<style>
  body {
    margin: 0;
    font-family: system-ui, sans-serif;
  }

  /* fixed：背景固定，产生视差效果 */
  .parallax {
    height: 100vh;
    background-image: url('https://example.com/mountain.jpg');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;  /* 视差效果 */
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 48px;
  }

  .content {
    height: 100vh;
    padding: 40px;
    background: white;
  }

  /* local：背景随内容滚动 */
  .scrollable-box {
    width: 300px;
    height: 200px;
    overflow-y: auto;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50"><text x="10" y="30" font-size="14">WATERMARK</text></svg>');
    background-attachment: local;  /* 随内容滚动 */
    padding: 20px;
    border: 2px solid #667eea;
  }
</style>
</head>
<body>
  <section class="parallax">
    <h1>视差滚动</h1>
  </section>

  <section class="content">
    <h2>背景固定效果</h2>
    <p>滚动页面观察上方视差效果。</p>

    <h3>local 滚动行为：</h3>
    <div class="scrollable-box">
      <p>滚动此容器，水印跟随滚动。</p>
      <p>内容行 1</p>
      <p>内容行 2</p>
      <p>内容行 3</p>
      <p>内容行 4</p>
      <p>内容行 5</p>
      <p>内容行 6</p>
      <p>内容行 7</p>
      <p>内容行 8</p>
      <p>内容行 9</p>
      <p>内容行 10</p>
    </div>
  </section>

  <section class="parallax">
    <h1>第二屏视差</h1>
  </section>
</body>
</html>
```

### 1.7 多背景复合效果（卡片设计）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>多背景复合卡片</title>
<style>
  .premium-card {
    width: 320px;
    height: 200px;
    border-radius: 12px;
    padding: 24px;
    box-sizing: border-box;
    color: white;
    font-family: system-ui, sans-serif;
    position: relative;
    overflow: hidden;
    /* 多背景复合：光晕 + 渐变 + 纹理 */
    background:
      /* 顶层：光晕效果 */
      radial-gradient(circle at 80% 20%, rgba(255,255,255,0.3), transparent 40%),
      /* 中层：主渐变 */
      linear-gradient(135deg, #667eea 0%, #764ba2 100%),
      /* 底层：噪声纹理 */
      url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><filter id="n"><feTurbulence baseFrequency="0.7" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(%23n)" opacity="0.1"/></svg>');
    background-size: cover, cover, 200px 200px;
    background-position: center, center, center;
    background-repeat: no-repeat, no-repeat, repeat;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
  }

  .premium-card h3 {
    margin: 0 0 8px;
    font-size: 20px;
    font-weight: 700;
  }

  .premium-card p {
    margin: 0;
    font-size: 14px;
    opacity: 0.9;
  }
</style>
</head>
<body>
  <div class="premium-card">
    <h3>Premium 会员卡</h3>
    <p>多背景叠加实现高级感</p>
  </div>
</body>
</html>
```

### 1.8 `background-position` 四值语法

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>background-position 四值语法</title>
<style>
  .pos-demo {
    width: 300px;
    height: 200px;
    border: 2px solid #667eea;
    background-image: url('https://example.com/icon.png');
    background-repeat: no-repeat;
    background-size: 50px 50px;
    margin: 10px 0;
  }

  /* 关键字定位 */
  .pos-tl { background-position: top left; }
  .pos-tr { background-position: top right; }
  .pos-center { background-position: center center; }

  /* 百分比定位 */
  .pos-25-75 { background-position: 25% 75%; }

  /* 长度定位 */
  .pos-10px-20px { background-position: 10px 20px; }

  /* 四值语法：从右 10px，从下 20px */
  .pos-four-value { background-position: right 10px bottom 20px; }

  .label {
    font-family: monospace;
    color: #555;
    margin-bottom: 4px;
  }
</style>
</head>
<body>
  <div class="label">top left</div>
  <div class="pos-demo pos-tl"></div>

  <div class="label">right 10px bottom 20px</div>
  <div class="pos-demo pos-four-value"></div>

  <div class="label">25% 75%</div>
  <div class="pos-demo pos-25-75"></div>
</body>
</html>
```

### 1.9 `background-repeat` 模式对比

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>background-repeat 模式对比</title>
<style>
  .repeat-demo {
    width: 300px;
    height: 100px;
    border: 2px solid #333;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"><circle cx="20" cy="20" r="15" fill="#667eea"/></svg>');
    margin: 10px 0;
  }

  .repeat { background-repeat: repeat; }      /* 默认平铺 */
  .repeat-x { background-repeat: repeat-x; }  /* 水平平铺 */
  .repeat-y { background-repeat: repeat-y; }  /* 垂直平铺 */
  .no-repeat { background-repeat: no-repeat; }
  .space { background-repeat: space; }        /* 均匀分布留白 */
  .round { background-repeat: round; }        /* 缩放填满 */

  .label {
    font-family: monospace;
    margin-bottom: 4px;
  }
</style>
</head>
<body>
  <div class="label">repeat</div>
  <div class="repeat-demo repeat"></div>

  <div class="label">repeat-x</div>
  <div class="repeat-demo repeat-x"></div>

  <div class="label">space</div>
  <div class="repeat-demo space"></div>

  <div class="label">round</div>
  <div class="repeat-demo round"></div>
</body>
</html>
```

### 1.10 企业级：响应式 Hero 区背景系统

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>企业级响应式 Hero 背景系统</title>
<style>
  :root {
    --hero-bg-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --hero-bg-overlay: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.7) 100%);
    --hero-text-color: white;
    --hero-overlay-opacity: 0.8;
  }

  [data-theme="dark"] {
    --hero-bg-primary: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    --hero-bg-overlay: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.9) 100%);
    --hero-text-color: #f0f0f0;
  }

  .hero {
    width: 100%;
    min-height: 500px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--hero-text-color);
    text-align: center;
    padding: 60px 20px;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    /* 多背景：渐变蒙版 + 主渐变 + 噪声 */
    background:
      var(--hero-bg-overlay),
      var(--hero-bg-primary),
      url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><filter id="n"><feTurbulence baseFrequency="0.9"/></filter><rect width="100%" height="100%" filter="url(%23n)" opacity="0.05"/></svg>');
    background-size: cover, cover, 200px 200px;
    background-position: center;
    background-repeat: no-repeat, no-repeat, repeat;
  }

  /* 响应式背景图 */
  @media (min-width: 768px) {
    .hero {
      background-image:
        var(--hero-bg-overlay),
        url('https://example.com/hero-desktop.jpg'),
        var(--hero-bg-primary);
      background-size: cover, cover, cover;
    }
  }

  @media (max-width: 767px) {
    .hero {
      background-image:
        var(--hero-bg-overlay),
        url('https://example.com/hero-mobile.jpg'),
        var(--hero-bg-primary);
      background-size: cover, cover, cover;
      min-height: 300px;
    }
  }

  /* 高 DPI 屏幕 */
  @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
    .hero {
      background-image:
        var(--hero-bg-overlay),
        url('https://example.com/hero@2x.jpg'),
        var(--hero-bg-primary);
    }
  }

  .hero-content {
    position: relative;
    z-index: 1;
    max-width: 800px;
  }

  .hero h1 {
    font-size: clamp(32px, 5vw, 56px);
    margin: 0 0 20px;
    font-weight: 800;
  }

  .hero p {
    font-size: clamp(16px, 2vw, 20px);
    margin: 0 0 30px;
    opacity: 0.95;
  }

  .hero .cta {
    display: inline-block;
    padding: 14px 32px;
    background: white;
    color: #667eea;
    text-decoration: none;
    border-radius: 8px;
    font-weight: 600;
    transition: transform 0.2s;
  }

  .hero .cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
  }
</style>
</head>
<body>
  <section class="hero">
    <div class="hero-content">
      <h1>构建下一代 Web 体验</h1>
      <p>多背景叠加、响应式适配、高 DPI 优化，一站式解决方案</p>
      <a href="#" class="cta">立即开始</a>
    </div>
  </section>
</body>
</html>
```

### 1.11 企业级：设计令牌驱动的背景系统

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>设计令牌驱动的背景系统</title>
<style>
  :root {
    /* 背景设计令牌 */
    --bg-image-overlay: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    --bg-image-card: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
    --bg-size-pattern: 20px 20px;
    --bg-position-default: center;
    --bg-clip-default: border-box;
    --bg-origin-default: padding-box;

    /* 语义化令牌 */
    --bg-surface: var(--bg-image-card);
    --bg-surface-elevated: linear-gradient(135deg, #ffffff 0%, #f0f4ff 100%);
    --bg-surface-subtle: var(--bg-image-overlay);
  }

  [data-theme="dark"] {
    --bg-image-card: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    --bg-image-overlay: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
    --bg-surface-elevated: linear-gradient(135deg, #1e2a4a 0%, #16213e 100%);
  }

  .card {
    background: var(--bg-surface);
    background-clip: var(--bg-clip-default);
    background-origin: var(--bg-origin-default);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin: 16px;
    max-width: 400px;
  }

  .card-elevated {
    background: var(--bg-surface-elevated);
  }

  .card-subtle {
    background: var(--bg-surface-subtle);
  }

  /* 工具类 */
  .bg-cover {
    background-size: cover !important;
  }

  .bg-contain {
    background-size: contain !important;
  }

  .bg-fixed {
    background-attachment: fixed !important;
  }

  .bg-clip-text {
    -webkit-background-clip: text !important;
    background-clip: text !important;
    -webkit-text-fill-color: transparent;
    color: transparent;
  }
</style>
</head>
<body>
  <div class="card">
    <h3>默认卡片</h3>
    <p>使用 --bg-surface 令牌</p>
  </div>

  <div class="card card-elevated">
    <h3>悬浮卡片</h3>
    <p>使用 --bg-surface-elevated 令牌</p>
  </div>

  <div class="card card-subtle">
    <h3>微妙卡片</h3>
    <p>使用 --bg-surface-subtle 令牌</p>
  </div>
</body>
</html>
```

### 1.12 调试工具：背景可视化检查器

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>背景可视化检查器</title>
<style>
  .inspector {
    display: grid;
    grid-template-columns: 1fr 300px;
    gap: 20px;
    padding: 20px;
    font-family: system-ui, sans-serif;
  }

  .preview {
    width: 100%;
    height: 400px;
    border: 2px dashed #ccc;
    background-image: url('https://example.com/sample.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-clip: border-box;
    background-origin: padding-box;
    background-attachment: scroll;
  }

  .controls {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .control-group {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .control-group label {
    font-size: 12px;
    color: #555;
    font-family: monospace;
  }

  .control-group select,
  .control-group input {
    padding: 6px;
    font-size: 13px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  .output {
    background: #f5f5f5;
    padding: 12px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 12px;
    white-space: pre-wrap;
    color: #333;
  }
</style>
</head>
<body>
  <div class="inspector">
    <div class="preview" id="preview"></div>
    <div class="controls">
      <div class="control-group">
        <label>background-size</label>
        <select id="size">
          <option value="cover">cover</option>
          <option value="contain">contain</option>
          <option value="auto">auto</option>
          <option value="100% 100%">100% 100%</option>
          <option value="200px 200px">200px 200px</option>
        </select>
      </div>
      <div class="control-group">
        <label>background-clip</label>
        <select id="clip">
          <option value="border-box">border-box</option>
          <option value="padding-box">padding-box</option>
          <option value="content-box">content-box</option>
        </select>
      </div>
      <div class="control-group">
        <label>background-origin</label>
        <select id="origin">
          <option value="padding-box">padding-box</option>
          <option value="border-box">border-box</option>
          <option value="content-box">content-box</option>
        </select>
      </div>
      <div class="control-group">
        <label>background-repeat</label>
        <select id="repeat">
          <option value="no-repeat">no-repeat</option>
          <option value="repeat">repeat</option>
          <option value="space">space</option>
          <option value="round">round</option>
        </select>
      </div>
      <div class="output" id="output"></div>
    </div>
  </div>

  <script>
    const preview = document.getElementById('preview');
    const output = document.getElementById('output');

    function updatePreview() {
      const size = document.getElementById('size').value;
      const clip = document.getElementById('clip').value;
      const origin = document.getElementById('origin').value;
      const repeat = document.getElementById('repeat').value;

      preview.style.backgroundSize = size;
      preview.style.backgroundClip = clip;
      preview.style.backgroundOrigin = origin;
      preview.style.backgroundRepeat = repeat;

      output.textContent = `background:
  url('sample.jpg')
  ${repeat}
  center / ${size}
  ${origin}
  ${clip};`;
    }

    document.querySelectorAll('select').forEach(sel => {
      sel.addEventListener('change', updatePreview);
    });

    updatePreview();
  </script>
</body>
</html>
```

---

## 2. 对比分析
### 2.1 `background-image` 与 `<img>` 标签对比

| 维度 | `background-image` | `<img>` 标签 |
| --- | --- | --- |
| 语义 | 装饰性图像 | 内容性图像 |
| 可访问性 | 屏幕阅读器忽略 | 有 `alt` 文本 |
| SEO | 不被搜索引擎索引 | 被索引 |
| 缩放控制 | `background-size` | `object-fit` |
| 多层叠加 | 支持多背景 | 不支持 |
| 动画 | `background-position` 动画 | `transform` 动画 |
| 性能 | 延迟加载（取决于浏览器） | 可懒加载 |
| 响应式 | `image-set()`、媒体查询 | `srcset`、`<picture>` |
| 适用场景 | 装饰、纹理、渐变 | 内容图像、产品图 |

### 2.2 `background-clip` 与 `background-origin` 对比

| 属性 | 控制内容 | 默认值 | 取值范围 | 典型用途 |
| --- | --- | --- | --- | --- |
| `background-clip` | 绘制区域 | `border-box` | `border-box` \| `padding-box` \| `content-box` \| `text` | 控制背景绘制到哪个边界 |
| `background-origin` | 定位起点 | `padding-box` | `border-box` \| `padding-box` \| `content-box` | 控制百分比/位置计算的起点 |

关键差异：`background-clip` 决定「画到哪里」，`background-origin` 决定「从哪里开始算」。

### 2.3 `background-size` 与 `object-fit` 对比

| 维度 | `background-size` | `object-fit` |
| --- | --- | --- |
| 适用元素 | 任意元素 | `<img>`、`<video>` 等替换元素 |
| `cover` | 覆盖容器，可能裁剪 | 同 |
| `contain` | 完整显示，可能留白 | 同 |
| 长度/百分比 | 支持 | 不支持（用 `object-position`） |
| 多层 | 支持 | 不支持 |
| 配合属性 | `background-position` | `object-position` |

### 2.4 多背景与伪元素叠加对比

| 维度 | 多背景 | 伪元素 `::before`/`::after` |
| --- | --- | --- |
| 语法 | 单条 `background` 声明 | 需要额外 CSS 规则 |
| 层数限制 | 无硬性限制（性能限制） | 每元素 2 个伪元素 |
| 独立控制 | 每层独立 `background-*` | 每个伪元素独立 |
| 动画 | `background-position` 动画 | `transform`、`opacity` 动画 |
| 性能 | 合成层共享 | 独立合成层 |
| 语义 | 装饰性 | 可承载语义 |
| 适用场景 | 多层渐变、纹理 | 复杂叠加、需要独立动画 |

### 2.5 主流框架背景实践对比

| 框架 | 多背景策略 | `background-size` | `background-clip` | 工具类 |
| --- | --- | --- | --- | --- |
| Bootstrap 5 | 渐变工具类 `.bg-gradient` | 不直接提供 | 不直接提供 | `.bg-primary`、`.bg-gradient` |
| Tailwind CSS v3.4 | `bg-[url(...)]`、`bg-gradient-to-*` | `bg-cover`、`bg-contain` | `bg-clip-text`、`bg-clip-border` | `bg-cover`、`bg-contain`、`bg-clip-text` |
| Material Design 3 | 主题色 + 渐变 | 不直接提供 | 不直接提供 | 主题变量 |
| GitHub Primer | `.color-bg-*`、渐变工具 | 不直接提供 | 不直接提供 | `.bg-gradient-*` |
| Ant Design 5 | 主题色 | 不直接提供 | 不直接提供 | 主题变量 |

### 2.6 Tailwind 与 Bootstrap 背景哲学对比

**Tailwind CSS v3.4**：原子化工具类，灵活组合。

```html
<div class="bg-gradient-to-r from-purple-500 to-pink-500 bg-cover bg-center bg-clip-text text-transparent">
  渐变文字
</div>
```

**Bootstrap 5**：预设组件样式，开箱即用。

```html
<div class="bg-primary bg-gradient p-4">
  Bootstrap 渐变背景
</div>
```

Tailwind 的优势在于灵活组合，Bootstrap 的优势在于快速原型。现代项目多倾向 Tailwind。

### 2.7 预处理器对比

| 预处理器 | 多背景 Mixin | `background-size` 支持 | `background-clip: text` 支持 |
| --- | --- | --- | --- |
| SCSS | `@mixin multi-bg($layers...)` | 内置函数 | 需手动前缀 |
| Less | `.multi-bg(@layers...)` | 内置函数 | 需手动前缀 |
| Stylus | `multi-bg($layers...)` | 内置函数 | 需手动前缀 |

```scss
// SCSS Mixin 示例
@mixin gradient-text($gradient) {
  background: $gradient;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}

.title {
  @include gradient-text(linear-gradient(to right, #667eea, #764ba2));
}
```

---

## 3. 常见陷阱与最佳实践
### 3.1 陷阱 1：`background-clip: text` 忘记回退

**错误代码**：

```css
.gradient-text {
  background: linear-gradient(to right, red, blue);
  background-clip: text;
  color: transparent;  /* 若浏览器不支持，文字完全不可见 */
}
```

**问题**：旧浏览器不支持 `background-clip: text`，但 `color: transparent` 生效，导致文字消失。

**正确做法**：

```css
.gradient-text {
  background: linear-gradient(to right, red, blue);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: #667eea;  /* 回退颜色：不支持时显示此色 */
}

@supports (background-clip: text) or (-webkit-background-clip: text) {
  .gradient-text {
    color: transparent;  /* 仅在支持时设为透明 */
  }
}
```

### 3.2 陷阱 2：多背景层数过多导致性能问题

**错误代码**：

```css
.complex-bg {
  background:
    url('layer1.png'),
    url('layer2.png'),
    url('layer3.png'),
    url('layer4.png'),
    url('layer5.png'),
    url('layer6.png'),
    url('layer7.png'),
    url('layer8.png');
  /* 8 层背景，移动端可能掉帧 */
}
```

**最佳实践**：层数控制在 4 层以内，超出部分用伪元素或 SVG 合并：

```css
.complex-bg {
  position: relative;
  background:
    url('layer1.png'),
    url('layer2.png');
}

.complex-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    url('layer3.png'),
    url('layer4.png');
}
```

### 3.3 陷阱 3：`background-attachment: fixed` 在移动端失效

**问题**：iOS Safari 出于性能考虑，禁用 `fixed` 的视口绑定，将其降级为 `scroll`。

**解决方案**：使用 JavaScript 实现视差，或使用 `position: sticky` 替代：

```css
/* 方案 1：使用 sticky 模拟视差 */
.parallax-container {
  height: 100vh;
  overflow-x: hidden;
  overflow-y: auto;
  perspective: 1px;
}

.parallax-bg {
  position: sticky;
  top: 0;
  height: 100vh;
  background-image: url('background.jpg');
  background-size: cover;
  transform: translateZ(-1px) scale(2);
  z-index: -1;
}
```

### 3.4 陷阱 4：`background-size: 100% 100%` 拉伸变形

**错误代码**：

```css
.hero {
  background-image: url('photo.jpg');
  background-size: 100% 100%;  /* 拉伸，破坏宽高比 */
}
```

**问题**：强制拉伸图像以填满容器，导致变形。

**正确做法**：

```css
.hero {
  background-image: url('photo.jpg');
  background-size: cover;  /* 保持宽高比，可能裁剪 */
  /* 或 */
  background-size: contain;  /* 保持宽高比，可能留白 */
}
```

### 3.5 陷阱 5：`background-origin` 与 `background-clip` 混淆

**误区**：误认为两者作用相同。

**澄清**：

- `background-origin: content-box`：背景的 `0% 0%` 定位点在 content-box 左上角。
- `background-clip: content-box`：背景绘制范围限制在 content-box 内。

两者独立设置，可组合出不同效果：

```css
/* 图像从 border 开始定位，但只绘制到 padding */
.box {
  background-origin: border-box;
  background-clip: padding-box;
  border: 10px solid transparent;
}
```

### 3.6 陷阱 6：`background` 简写覆盖独立属性

**错误代码**：

```css
.card {
  background-size: cover;  /* 先设置 */
  background: url('image.jpg') no-repeat center;  /* 简写覆盖，background-size 重置为 auto */
}
```

**问题**：`background` 简写会重置所有未指定的子属性为默认值。

**正确做法**：

```css
.card {
  background: url('image.jpg') no-repeat center / cover;  /* 在简写中指定 */
}
/* 或 */
.card {
  background-image: url('image.jpg');
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;  /* 独立设置，不使用简写 */
}
```

### 3.7 陷阱 7：高 DPI 背景图加载性能

**问题**：为 Retina 屏幕加载 2x、3x 图像，移动端流量消耗大。

**解决方案**：使用 `image-set()` 或 `<picture>` 元素：

```css
.hero {
  background-image: image-set(
    url('hero@1x.jpg') 1x,
    url('hero@2x.jpg') 2x,
    url('hero@3x.jpg') 3x
  );
}
```

### 3.8 陷阱 8：背景与可访问性

**问题**：背景图上的文字对比度不足，影响阅读。

**解决方案**：使用 WCAG 对比度检查器，确保对比度 ≥ 4.5:1（AA 标准）：

```css
.hero {
  background-image: url('background.jpg');
  /* 添加渐变蒙版增强对比度 */
  background-image:
    linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7)),
    url('background.jpg');
  color: white;  /* 配合深色蒙版，对比度达标 */
}
```

### 3.9 最佳实践清单

1. **优先使用渐变而非图像**：渐变无需 HTTP 请求，性能更优。
2. **使用 `background-size: cover` 适配响应式**：避免固定尺寸。
3. **多背景层数控制在 4 层以内**：性能考虑。
4. **`background-clip: text` 必须有回退**：使用 `@supports` 检测。
5. **移动端避免 `background-attachment: fixed`**：使用替代方案。
6. **高 DPI 使用 `image-set()`**：按需加载。
7. **检查对比度**：WCAG AA 标准 4.5:1。
8. **设计令牌化**：将背景属性抽象为 CSS Variables。
9. **Stylelint 校验**：禁止 `background-size: 100% 100%` 等反模式。
10. **性能预算**：背景图总大小控制在 200KB 以内。

---

## 4. 工程实践
### 4.1 背景设计令牌系统

```css
:root {
  /* 背景图像令牌 */
  --bg-image-hero: url('/images/hero.jpg');
  --bg-image-pattern: url('/images/pattern.svg');

  /* 渐变令牌 */
  --bg-gradient-primary: linear-gradient(135deg, #667eea, #764ba2);
  --bg-gradient-secondary: linear-gradient(135deg, #f093fb, #f5576c);
  --bg-gradient-accent: linear-gradient(135deg, #4facfe, #00f2fe);

  /* 背景尺寸令牌 */
  --bg-size-cover: cover;
  --bg-size-contain: contain;
  --bg-size-pattern: 20px 20px;

  /* 背景位置令牌 */
  --bg-position-center: center;
  --bg-position-top: top;
  --bg-position-bottom: bottom;

  /* 背景重复令牌 */
  --bg-repeat-none: no-repeat;
  --bg-repeat-pattern: repeat;

  /* 背景裁剪令牌 */
  --bg-clip-default: border-box;
  --bg-clip-text: text;

  /* 语义化背景 */
  --bg-surface-base: var(--bg-gradient-primary);
  --bg-surface-elevated: var(--bg-gradient-secondary);
  --bg-surface-overlay: var(--bg-gradient-accent);
}
```

### 4.2 PostCSS 自动前缀与优化

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('autoprefixer')({
      overrideBrowserslist: ['> 1%', 'last 2 versions', 'not dead'],
      grid: true,
    }),
    require('postcss-bg-image')({
      // 自动为 background-image 添加 image-set() 支持
      retina: true,
    }),
    require('cssnano')({
      preset: 'advanced',
    }),
  ],
};
```

### 4.3 SCSS Mixin 库

```scss
// _backgrounds.scss

/// 渐变文字 Mixin
/// @param {String} $gradient - 渐变值
@mixin gradient-text($gradient) {
  background: $gradient;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;

  // 回退
  @supports not ((background-clip: text) or (-webkit-background-clip: text)) {
    background: none;
    color: #667eea;
  }
}

/// 多背景叠加 Mixin
/// @param {List} $layers - 背景层列表
@mixin multi-background($layers) {
  background: $layers;

  // 自动设置 background-size
  $sizes: ();
  @each $layer in $layers {
    $sizes: append($sizes, cover);
  }
  background-size: $sizes;
  background-repeat: no-repeat;
  background-position: center;
}

/// 响应式背景图 Mixin
/// @param {String} $base-path - 图像基础路径
/// @param {String} $extension - 图像扩展名
@mixin responsive-bg($base-path, $extension: 'jpg') {
  background-image: url('#{$base-path}.#{$extension}');

  @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
    background-image: url('#{$base-path}@2x.#{$extension}');
  }

  @media (-webkit-min-device-pixel-ratio: 3), (min-resolution: 288dpi) {
    background-image: url('#{$base-path}@3x.#{$extension}');
  }
}

/// 视差背景 Mixin（移动端兼容）
@mixin parallax-bg($image) {
  background-image: url($image);
  background-size: cover;
  background-position: center;

  // 桌面端使用 fixed
  @media (min-width: 768px) {
    background-attachment: fixed;
  }

  // 移动端使用 sticky 替代
  @media (max-width: 767px) {
    background-attachment: scroll;
  }
}
```

### 4.4 Tailwind CSS 自定义配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('/images/hero-pattern.svg')",
        'gradient-primary': 'linear-gradient(135deg, #667eea, #764ba2)',
        'gradient-secondary': 'linear-gradient(135deg, #f093fb, #f5576c)',
      },
      backgroundSize: {
        'auto': 'auto',
        'cover': 'cover',
        'contain': 'contain',
        '50%': '50%',
        '100': '100px',
      },
      backgroundPosition: {
        'center': 'center',
        'top': 'top',
        'bottom': 'bottom',
        'right-10': 'right 10px',
      },
      backgroundClip: {
        'text': 'text',
      },
    },
  },
  plugins: [
    // 自定义插件：背景工具类
    function({ addUtilities, theme }) {
      addUtilities({
        '.bg-parallax': {
          backgroundImage: 'var(--bg-parallax)',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          '@screen md': {
            backgroundAttachment: 'fixed',
          },
        },
      });
    },
  ],
};
```

### 4.5 React 组件封装

```tsx
import React, { CSSProperties } from 'react';

export interface BackgroundProps {
  image?: string;
  gradient?: string;
  size?: 'cover' | 'contain' | string;
  position?: string;
  repeat?: 'no-repeat' | 'repeat' | 'repeat-x' | 'repeat-y';
  attachment?: 'scroll' | 'fixed' | 'local';
  clip?: 'border-box' | 'padding-box' | 'content-box' | 'text';
  origin?: 'border-box' | 'padding-box' | 'content-box';
  fallbackColor?: string;
  children?: React.ReactNode;
  className?: string;
  style?: CSSProperties;
}

/**
 * 企业级背景组件
 * 支持多背景叠加、响应式适配、可访问性回退
 */
export function Background({
  image,
  gradient,
  size = 'cover',
  position = 'center',
  repeat = 'no-repeat',
  attachment = 'scroll',
  clip = 'border-box',
  origin = 'padding-box',
  fallbackColor,
  children,
  className,
  style,
}: BackgroundProps) {
  const backgroundLayers: string[] = [];
  if (gradient) backgroundLayers.push(gradient);
  if (image) backgroundLayers.push(`url(${image})`);

  const isTextClip = clip === 'text';

  const bgStyle: CSSProperties = {
    background: backgroundLayers.length > 0 ? backgroundLayers.join(', ') : fallbackColor,
    backgroundSize: size,
    backgroundPosition: position,
    backgroundRepeat: repeat,
    backgroundAttachment: attachment,
    backgroundOrigin: origin,
    ...style,
  };

  if (isTextClip) {
    bgStyle.WebkitBackgroundClip = 'text';
    bgStyle.backgroundClip = 'text';
    bgStyle.WebkitTextFillColor = 'transparent';
    bgStyle.color = 'transparent';
  } else {
    bgStyle.backgroundClip = clip;
  }

  return (
    <div
      className={className}
      style={bgStyle}
      role={image ? 'img' : undefined}
      aria-label={image ? '背景图像' : undefined}
    >
      {children}
    </div>
  );
}

// 使用示例
export function Demo() {
  return (
    <Background
      gradient="linear-gradient(135deg, #667eea, #764ba2)"
      image="/images/hero.jpg"
      size="cover"
      position="center"
      className="hero-section"
    >
      <h1>Hero 标题</h1>
    </Background>
  );
}
```

### 4.6 性能优化策略

1. **懒加载背景图**：

```javascript
// IntersectionObserver 懒加载
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const el = entry.target;
      const bg = el.dataset.bg;
      if (bg) {
        el.style.backgroundImage = `url(${bg})`;
        observer.unobserve(el);
      }
    }
  });
});

document.querySelectorAll('[data-bg]').forEach((el) => observer.observe(el));
```

```html
<div data-bg="/images/lazy-bg.jpg" class="lazy-bg">
  内容
</div>
```

2. **预加载关键背景**：

```html
<link rel="preload" as="image" href="/images/hero.jpg" />
```

3. **使用 WebP/AVIF 格式**：

```css
.hero {
  background-image: url('hero.avif');
}

@supports not (background-image: url('hero.avif')) {
  .hero {
    background-image: url('hero.webp');
  }
}

@supports not (background-image: url('hero.webp')) {
  .hero {
    background-image: url('hero.jpg');
  }
}
```

4. **CSS Sprite 合并小图标**：

```css
.icon {
  background-image: url('sprite.png');
  background-repeat: no-repeat;
}

.icon-home { background-position: 0 0; }
.icon-user { background-position: -20px 0; }
.icon-settings { background-position: -40px 0; }
```

### 4.7 调试工具

1. **Chrome DevTools**：

   - Elements 面板 → Styles → 查看 `background-*` 计算值。
   - Rendering 面板 → Paint flashing → 查看背景重绘区域。

2. **Firefox DevTools**：

   - Inspector → Backgrounds 面板 → 可视化背景层。

3. **在线工具**：
   - [CSS Backgrounds Visualizer](https://css-tricks.com/almanac/properties/b/background/)
   - [Gradient Generator](https://cssgradient.io/)

### 4.8 Stylelint 校验规则

```json
{
  "rules": {
    "declaration-block-no-shorthand-property-overrides": true,
    "declaration-property-value-disallowed-list": {
      "background-size": ["100% 100%", "100% 100%"]
    },
    "color-no-hex": false,
    "function-url-no-scheme-relative": true,
    "property-no-vendor-prefix": [
      true,
      {
        "ignoreProperties": ["background-clip", "text-fill-color"]
      }
    ]
  }
}
```

### 4.9 Playwright 视觉回归测试

```typescript
import { test, expect } from '@playwright/test';

test('Hero 背景渲染正确', async ({ page }) => {
  await page.goto('/hero');

  const hero = page.locator('.hero');
  await expect(hero).toHaveScreenshot('hero-background.png', {
    maxDiffPixelRatio: 0.01,
  });

  // 验证背景图加载
  const bgImage = await hero.evaluate((el) => {
    return window.getComputedStyle(el).backgroundImage;
  });
  expect(bgImage).toContain('url');
});

test('渐变文字渲染正确', async ({ page }) => {
  await page.goto('/gradient-text');

  const text = page.locator('.gradient-text');
  const clip = await text.evaluate((el) => {
    return window.getComputedStyle(el).webkitBackgroundClip;
  });
  expect(clip).toBe('text');
});
```

### 4.10 浏览器兼容性处理

```css
/* background-clip: text 回退 */
.gradient-text {
  color: #667eea;  /* 回退颜色 */
}

@supports (-webkit-background-clip: text) or (background-clip: text) {
  .gradient-text {
    background: linear-gradient(to right, #667eea, #764ba2);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
  }
}

/* image-set() 回退 */
.hero {
  background-image: url('hero.jpg');  /* 回退 */
}

@supports (background-image: image-set(url('hero.jpg') 1x)) {
  .hero {
    background-image: image-set(
      url('hero@1x.jpg') 1x,
      url('hero@2x.jpg') 2x,
      url('hero@3x.jpg') 3x
    );
  }
}

/* conic-gradient 回退 */
.conic-bg {
  background-image: url('conic-fallback.png');  /* 回退 */
}

@supports (background: conic-gradient(red, blue)) {
  .conic-bg {
    background-image: conic-gradient(red, yellow, blue, red);
  }
}
```

---

## 5. 案例研究
### 5.1 案例 1：Bootstrap 5 背景系统

Bootstrap 5 通过 `.bg-*` 工具类提供主题色背景：

```css
.bg-primary { background-color: #0d6efd !important; }
.bg-secondary { background-color: #6c757d !important; }
.bg-success { background-color: #198754 !important; }
.bg-danger { background-color: #dc3545 !important; }
.bg-warning { background-color: #ffc107 !important; }
.bg-info { background-color: #0dcaf0 !important; }
.bg-light { background-color: #f8f9fa !important; }
.bg-dark { background-color: #212529 !important; }
.bg-white { background-color: #fff !important; }
.bg-transparent { background-color: transparent !important; }

.bg-gradient {
  background-image: var(--bs-gradient) !important;
}
```

设计哲学：

1. **主题色驱动**：与 Sass 变量 `$theme-colors` 绑定。
2. **`!important` 强制覆盖**：避免优先级冲突。
3. **`.bg-gradient` 渐变扩展**：在纯色基础上叠加半透明渐变。

### 5.2 案例 2：Tailwind CSS v3.4 背景

Tailwind 提供更细粒度的背景工具类：

```css
/* 颜色 */
.bg-red-500 { background-color: #ef4444; }
.bg-blue-500 { background-color: #3b82f6; }

/* 渐变 */
.bg-gradient-to-r { background-image: linear-gradient(to right, var(--tw-gradient-stops)); }
.bg-gradient-to-br { background-image: linear-gradient(to bottom right, var(--tw-gradient-stops)); }

.from-purple-500 { --tw-gradient-from: #8b5cf6; }
.to-pink-500 { --tw-gradient-to: #ec4899; }

/* 尺寸 */
.bg-cover { background-size: cover; }
.bg-contain { background-size: contain; }

/* 位置 */
.bg-center { background-position: center; }
.bg-top { background-position: top; }

/* 重复 */
.bg-no-repeat { background-repeat: no-repeat; }
.bg-repeat { background-repeat: repeat; }

/* 附件 */
.bg-fixed { background-attachment: fixed; }
.bg-local { background-attachment: local; }
.bg-scroll { background-attachment: scroll; }

/* 裁剪 */
.bg-clip-border { background-clip: border-box; }
.bg-clip-padding { background-clip: padding-box; }
.bg-clip-content { background-clip: content-box; }
.bg-clip-text { 
  -webkit-background-clip: text;
  background-clip: text;
}
```

设计哲学：

1. **原子化**：每个属性独立工具类。
2. **组合性**：`bg-gradient-to-r from-purple-500 to-pink-500` 灵活组合。
3. **JIT 编译**：按需生成，无冗余 CSS。

### 5.3 案例 3：Material Design 3 背景

Material Design 3 通过 Design Token 系统管理背景：

```css
:root {
  --md-sys-color-surface: #fef7ff;
  --md-sys-color-surface-variant: #e7e0ec;
  --md-sys-color-surface-container-lowest: #ffffff;
  --md-sys-color-surface-container-low: #f7f2fa;
  --md-sys-color-surface-container: #f3edf7;
  --md-sys-color-surface-container-high: #ece6f0;
  --md-sys-color-surface-container-highest: #e6e0e9;
}

.card {
  background-color: var(--md-sys-color-surface-container);
}

.card-elevated {
  background-color: var(--md-sys-color-surface-container-high);
}
```

设计哲学：

1. **语义层级**：`surface`、`surface-variant`、`surface-container-*` 表达层级。
2. **主题响应**：通过 Token 自动切换明暗主题。
3. **无渐变**：Material Design 3 倾向纯色背景，避免视觉干扰。

### 5.4 案例 4：GitHub Primer 背景

GitHub Primer 使用功能化背景工具类：

```css
.bg-default { background-color: var(--bgColor-default) !important; }
.bg-muted { background-color: var(--bgColor-muted) !important; }
.bg-subtle { background-color: var(--bgColor-subtle) !important; }
.bg-emphasis { background-color: var(--bgColor-emphasis) !important; }

/* 渐变工具 */
.bg-gradient-subtle {
  background-image: linear-gradient(to bottom, var(--bgColor-gradient-subtle-top), var(--bgColor-gradient-subtle-bottom));
}
```

### 5.5 案例 5：Stripe 渐变美学

Stripe 网站以精致的渐变背景著称：

```css
.stripe-hero {
  background:
    radial-gradient(ellipse at top, rgba(118, 75, 162, 0.3), transparent 50%),
    radial-gradient(ellipse at bottom right, rgba(102, 126, 234, 0.3), transparent 50%),
    linear-gradient(135deg, #635BFF 0%, #2D1B69 100%);
  background-size: cover, cover, cover;
  background-position: center;
}
```

设计哲学：

1. **多层渐变叠加**：营造深度感。
2. **径向 + 线性混合**：丰富视觉层次。
3. **品牌色驱动**：以 Stripe 紫（#635BFF）为核心。

### 5.6 案例 6：生产事故 - 背景图导致 CLS

**场景**：某电商网站 Hero 区背景图加载后导致布局偏移（CLS）。

**原因**：

```css
.hero {
  background-image: url('hero.jpg');
  background-size: cover;
  min-height: 0;  /* 未设置最小高度 */
}
```

背景图加载前，`min-height: 0`，内容高度决定容器高度；背景图加载后，`background-size: cover` 不改变容器尺寸，但浏览器为适配背景重新布局。

**修复**：

```css
.hero {
  background-image: url('hero.jpg');
  background-size: cover;
  min-height: 400px;  /* 明确最小高度 */
  aspect-ratio: 16 / 9;  /* 或使用 aspect-ratio */
}
```

**经验**：背景图加载不应影响布局，必须预设容器尺寸。

---

### 填空题知识点讲解

**题目 1**：CSS 多背景的层级顺序中，第一个声明的背景位于__________层，最后一个位于__________层，`background-color` 始终位于__________层。

**解析讲解**：最上；最下；最底

**解析讲解**：CSS 多背景采用栈式模型，第一个声明在最上层（视觉最顶部），最后一个在最底层，`background-color` 始终位于所有背景层之下。

---

**题目 2**：`background-origin` 控制__________，`background-clip` 控制__________。

**解析讲解**：定位起点（定位区域）；绘制区域

**解析讲解**：`background-origin` 决定 `background-position` 百分比计算的起点区域；`background-clip` 决定背景绘制的边界区域。

---

**题目 3**：`background-position: 50% 50%` 的几何意义是图像的__________与容器的__________对齐。

**解析讲解**：中心点；中心点

**解析讲解**：百分比定位采用「相对对齐」机制，`50%` 表示图像的 50% 点与容器的 50% 点对齐，即中心对齐。

---

**题目 4**：实现渐变文字效果需要组合使用 `background-clip: __________` 与 `color: __________`（或 `-webkit-text-fill-color: __________`）。

**解析讲解**：`text`；`transparent`；`transparent`

**解析讲解**：`background-clip: text` 将背景裁剪到文字区域，配合透明文字颜色让背景显示出来。

---

**题目 5**：`background-attachment` 的三个取值是__________、__________、__________，分别表示背景相对于__________、__________、__________滚动。

**解析讲解**：`scroll`；`fixed`；`local`；文档；视口；元素内容

---

### 编程题知识点讲解

**题目 1**：实现一个响应式 Hero 区，要求：

1. 背景图覆盖整个容器（`cover`）。
2. 在背景图上叠加从透明到深色的渐变蒙版，保证文字可读。
3. 桌面端使用 `background-attachment: fixed` 产生视差效果，移动端降级为 `scroll`。
4. 支持 2x、3x 高 DPI 屏幕。

**解析讲解**：

```css
.hero {
  width: 100%;
  min-height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
  padding: 60px 20px;
  box-sizing: border-box;
  /* 默认 1x 背景 + 渐变蒙版 */
  background:
    linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%),
    url('hero@1x.jpg');
  background-size: cover, cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: scroll;  /* 移动端默认 scroll */
}

/* 桌面端启用视差 */
@media (min-width: 768px) {
  .hero {
    background-attachment: fixed, fixed;
  }
}

/* 高 DPI 适配 */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .hero {
    background:
      linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%),
      url('hero@2x.jpg');
    background-size: cover, cover;
    background-position: center;
    background-repeat: no-repeat;
  }
}

@media (-webkit-min-device-pixel-ratio: 3), (min-resolution: 288dpi) {
  .hero {
    background:
      linear-gradient(to bottom, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%),
      url('hero@3x.jpg');
    background-size: cover, cover;
    background-position: center;
    background-repeat: no-repeat;
  }
}

.hero h1 {
  font-size: clamp(32px, 5vw, 56px);
  margin: 0;
}
```

---

**题目 2**：实现一个带渐变文字效果的标题，要求：

1. 文字颜色为从紫到粉的渐变。
2. 支持回退（不支持 `background-clip: text` 的浏览器显示紫色）。
3. 使用 `@supports` 进行特性检测。

**解析讲解**：

```css
.gradient-title {
  font-size: 48px;
  font-weight: 800;
  /* 回退：纯色 */
  color: #667eea;
}

@supports (-webkit-background-clip: text) or (background-clip: text) {
  .gradient-title {
    background: linear-gradient(135deg, #667eea 0%, #f093fb 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
  }
}
```

---

**题目 3**：实现一个可滚动容器，要求背景水印随内容滚动（`background-attachment: local`），并使用 SVG 数据 URI 作为水印。

**解析讲解**：

```css
.scrollable-container {
  width: 400px;
  height: 300px;
  overflow-y: auto;
  padding: 20px;
  border: 2px solid #667eea;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="120" height="60"><text x="10" y="35" font-family="monospace" font-size="14" fill="%23667eea" opacity="0.2">CONFIDENTIAL</text></svg>');
  background-repeat: repeat;
  background-attachment: local;  /* 随内容滚动 */
  background-size: 120px 60px;
}

.scrollable-container p {
  margin: 0 0 15px;
  line-height: 1.6;
}
```

```html
<div class="scrollable-container">
  <p>滚动此容器，水印随内容滚动。</p>
  <p>内容行 1...</p>
  <p>内容行 2...</p>
  <p>内容行 3...</p>
  <p>内容行 4...</p>
  <p>内容行 5...</p>
  <p>内容行 6...</p>
  <p>内容行 7...</p>
  <p>内容行 8...</p>
</div>
```

---

### 10.1 W3C 规范

[1] W3C. CSS Backgrounds and Borders Module Level 3 [EB/OL]. (2023-12-19) [2024-12-01]. https://www.w3.org/TR/css-backgrounds-3/.

[2] W3C. CSS Backgrounds Module Level 4 [EB/OL]. (2024-09-03) [2024-12-01]. https://www.w3.org/TR/css-backgrounds-4/.

[3] W3C. CSS Images Module Level 3 [EB/OL]. (2023-12-19) [2024-12-01]. https://www.w3.org/TR/css-images-3/.

[4] W3C. CSS Images Module Level 4 [EB/OL]. (2024-09-03) [2024-12-01]. https://www.w3.org/TR/css-images-4/.

[5] W3C. CSS Color Module Level 4 [EB/OL]. (2024-11-13) [2024-12-01]. https://www.w3.org/TR/css-color-4/.

[6] W3C. CSS Compositing and Blending Level 1 [EB/OL]. (2023-01-10) [2024-12-01]. https://www.w3.org/TR/compositing-1/.

[7] W3C. CSS Containment Module Level 1 [EB/OL]. (2023-12-19) [2024-12-01]. https://www.w3.org/TR/css-contain-1/.

[8] W3C. CSS Painting API Level 1 [EB/OL]. (2024-09-03) [2024-12-01]. https://www.w3.org/TR/css-paint-api-1/.

### 10.2 学术论文

[9] Lie H W, Bos B. Cascading Style Sheets: Designing for the Web [M]. 3rd ed. Upper Saddle River: Addison-Wesley Professional, 2005. DOI: 10.5555/1058604.

[10] Bos B, Çelik T, Hickson I, et al. Cascading Style Sheets Level 2 Revision 1 (CSS 2.1) Specification [S]. W3C Recommendation, 2011.

[11] Atkins T, Etemad E J. CSS Backgrounds and Borders Module Level 3 [S]. W3C Candidate Recommendation, 2023.

[12] Meyer E A. CSS: The Definitive Guide [M]. 5th ed. Sebastopol: O'Reilly Media, 2024. DOI: 10.5555/3588566.

[13] Cederholm D. Bulletproof Web Design: Improving Flexibility and Protecting Against Worst-Case Scenarios with XHTML and CSS [M]. 2nd ed. Berkeley: New Riders, 2007.

[14] Keith J. HTML5 for Web Designers [M]. 2nd ed. New York: A Book Apart, 2017.

[15] Verou L. CSS Secrets: Better Solutions to Everyday Web Design Problems [M]. 1st ed. Upper Saddle River: Addison-Wesley Professional, 2015. DOI: 10.5555/2855555.

### 10.3 浏览器实现文档

[16] Mozilla Developer Network. Background [EB/OL]. (2024-10-15) [2024-12-01]. https://developer.mozilla.org/en-US/docs/Web/CSS/background.

[17] Mozilla Developer Network. background-clip [EB/OL]. (2024-09-20) [2024-12-01]. https://developer.mozilla.org/en-US/docs/Web/CSS/background-clip.

[18] Mozilla Developer Network. background-size [EB/OL]. (2024-11-05) [2024-12-01]. https://developer.mozilla.org/en-US/docs/Web/CSS/background-size.

[19] Google Chrome Team. CSS Background and Borders [EB/OL]. (2024-08-30) [2024-12-01]. https://web.dev/articles/css-background.

[20] WebKit Blog. CSS Backgrounds in WebKit [EB/OL]. (2024-07-12) [2024-12-01]. https://webkit.org/blog/css-backgrounds/.

### 10.4 框架与工具文档

[21] Bootstrap Team. Bootstrap 5 Background Utilities [EB/OL]. (2024-06-20) [2024-12-01]. https://getbootstrap.com/docs/5.3/utilities/background/.

[22] Tailwind Labs. Tailwind CSS Background Size Documentation [EB/OL]. (2024-10-01) [2024-12-01]. https://tailwindcss.com/docs/background-size.

[23] Material Design Team. Material Design 3 Color System [EB/OL]. (2024-09-15) [2024-12-01]. https://m3.material.io/styles/color/overview.

[24] GitHub Primer Team. Primer Color System [EB/OL]. (2024-08-10) [2024-12-01]. https://primer.style/foundations/color.

[25] Stylelint Team. Stylelint Rules for Backgrounds [EB/OL]. (2024-07-22) [2024-12-01]. https://stylelint.io/user-guide/rules/list/.

### 10.5 相关标准

[26] W3C. CSS Values and Units Module Level 4 [EB/OL]. (2024-09-03) [2024-12-01]. https://www.w3.org/TR/css-values-4/.

[27] W3C. CSS Box Model Module Level 3 [EB/OL]. (2023-12-19) [2024-12-01]. https://www.w3.org/TR/css-box-3/.

[28] W3C. CSS Display Module Level 3 [EB/OL]. (2023-12-19) [2024-12-01]. https://www.w3.org/TR/css-display-3/.

[29] W3C. Web Content Accessibility Guidelines (WCAG) 2.2 [S]. W3C Recommendation, 2023. DOI: 10.5555/WCAG22.

[30] Ecma International. ECMAScript 2024 Language Specification [S]. Standard ECMA-262, 2024.

---

### 11.1 W3C 规范进阶

- [CSS Backgrounds Module Level 4 Editor's Draft](https://drafts.csswg.org/css-backgrounds-4/)：最新草案，跟踪 `background-clip: text` 标准化进展。
- [CSS Painting API Level 1](https://www.w3.org/TR/css-paint-api-1/)：Houdini Paint API，允许 JavaScript 自定义背景绘制。
- [CSS Properties and Values API Level 1](https://www.w3.org/TR/css-properties-values-api-1/)：CSS Houdini Properties API，支持自定义属性类型化。

### 11.2 进阶书籍

- **CSS Secrets**（Lea Verou）：深入 CSS 实战技巧，包含大量背景系统应用。
- **CSS: The Definitive Guide**（Eric Meyer）：CSS 权威指南，第 5 版涵盖现代 CSS。
- **HTML & CSS: Design and Build Websites**（Jon Duckett）：入门级图文教程。
- **CSS in Depth**（Keith J. Grant）：中级进阶，深入 CSS 内部机制。

### 11.4 开源项目

- [Bootstrap](https://github.com/twbs/bootstrap)：学习其 `.bg-*` 工具类实现。
- [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss)：学习其原子化背景工具类设计。
- [Primer CSS](https://github.com/primer/css)：GitHub 的设计系统实现。
- [Material Web](https://github.com/material-components/material-web)：Material Design 3 Web 实现。

### 11.5 社区与博客

- [CSS Working Group Blog](https://www.w3.org/blog/CSS/)：W3C CSS 工作组官方博客。
- [Lea Verou's Blog](https://lea.verou.me/)：CSS 专家 Lea Verou 的博客。
- [Chris Coyier's Blog](https://chriscoyier.net/)：CSS-Tricks 创始人博客。
- [Una Kravets's Blog](https://una.im/)：CSS 工作组成员博客。

### 11.7 工具与实验

- [CSS Backgrounds Visualizer](https://codepen.io/pen/?prefill=data)：在线可视化调试工具。
- [Gradient Generator](https://cssgradient.io/)：渐变生成器。
- [Pattern Generator](https://pattern.css.js.org/)：图案生成器。
- [Houdini Paint API Playground](https://paint-zine.now.sh/)：Paint API 实验场。

---

## 6. 深入理解（选读）

> 以下内容适合想彻底搞懂机制原理的读者，第一遍学习可跳过。

### 6.1 历史演进

### 6.1.1 CSS 1（1996）：背景的雏形

CSS 1 由 Håkon Wium Lie 与 Bert Bos 于 1996 年提出，首次定义背景相关属性。当时的背景系统极为简陋：

```css
/* CSS 1 语法 */
BODY {
  background-color: white;
  background-image: url("marble.gif");
  background-repeat: repeat;
  background-attachment: scroll;
  background-position: center;
}
```

CSS 1 的背景系统存在显著限制：

1. **单背景**：每个元素仅能有一张背景图。
2. **无尺寸控制**：无法缩放背景图，`background-size` 尚未存在。
3. **无裁剪控制**：`background-clip` 尚未存在，背景始终绘制到 padding 边界。
4. **定位粗糙**：`background-position` 仅支持关键字（`top`、`center`、`bottom`、`left`、`right`），不支持百分比与长度。

### 6.1.2 CSS 2.1（2011）：背景属性的成熟

CSS 2.1 §14 将背景属性扩展为现代熟悉的形态：

1. **百分比与长度定位**：`background-position: 50% 50%` 或 `10px 20px`。
2. **`background` 简写**：允许在一条声明中设置所有背景属性。
3. **背景绘制区域**：明确背景绘制到 padding 边界（即现代的 `background-clip: padding-box` 默认行为）。
4. **`background-attachment: fixed`**：引入视口固定背景。

但 CSS 2.1 仍未支持多背景与 `background-size`，开发者常通过嵌套 `<div>` 模拟多层背景：

```html
<!-- 嵌套 div 模拟多背景（CSS 2.1 时代） -->
<div class="layer-1">
  <div class="layer-2">
    <div class="content">...</div>
  </div>
</div>
```

### 6.1.3 CSS Backgrounds Module Level 3（2012-2017）

[CSS Backgrounds and Borders Module Level 3](https://www.w3.org/TR/css-backgrounds-3/) 是背景系统的革命性升级，引入：

1. **多背景**：允许在 `background-image` 中声明多个图像，以逗号分隔。
2. **`background-size`**：支持 `cover`、`contain`、长度、百分比。
3. **`background-clip`**：支持 `border-box`、`padding-box`、`content-box`。
4. **`background-origin`**：独立于 `background-clip`，控制定位起点。
5. **多值语法**：`background-position: right 10px bottom 20px`（四值语法）。
6. **`background-repeat: space` 与 `round`**：智能重复模式。

```css
/* CSS Backgrounds Level 3 多背景示例 */
.card {
  background:
    url('overlay.png') no-repeat center,
    linear-gradient(to right, #667eea, #764ba2);
  background-size: cover, auto;
  background-origin: padding-box, border-box;
  background-clip: padding-box, padding-box;
}
```

2017 年，Chrome 60、Firefox 55、Safari 11 全面支持 CSS Backgrounds Level 3，多背景进入生产可用阶段。

### 6.1.4 `background-clip: text` 的引入（2011-2018）

`background-clip: text` 是 WebKit 于 2011 年引入的非标准扩展，用于将背景裁剪到文字区域，实现「渐变文字」效果：

```css
.gradient-text {
  background: linear-gradient(to right, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text; /* 现代标准 */
}
```

长期作为 `-webkit-` 前缀私有特性存在，2018 年后逐渐被各浏览器支持，2023 年正式进入 [CSS Backgrounds Module Level 4](https://www.w3.org/TR/css-backgrounds-4/#background-clip) 草案。

### 6.1.5 CSS Backgrounds Module Level 4（2020-2024）

[CSS Backgrounds Module Level 4](https://www.w3.org/TR/css-backgrounds-4/) 引入了多项增强：

1. **`background-clip: text` 标准化**：从 WebKit 私有特性升级为正式规范。
2. **`background-position` 多值扩展**：支持 `right 10px bottom 20px` 四值语法的标准化。
3. **`background-repeat: space | round`**：在 Level 3 基础上进一步细化。
4. **`background-size` 与 `object-fit` 的语义对齐**：统一图像缩放语义。
5. **`background-attachment: local`**：在内容滚动容器内的背景跟随行为。

### 6.1.6 浏览器兼容性演进

| 年份 | 事件 | 核心变化 |
| --- | --- | --- |
| 1996 | CSS 1 推荐 | 基础背景属性，单背景，无尺寸控制 |
| 2011 | CSS 2.1 推荐 | 百分比定位、`background` 简写 |
| 2011 | WebKit 实现 `-webkit-background-clip: text` | 渐变文字效果 |
| 2012 | CSS Backgrounds Level 3 候选推荐 | 多背景、`background-size`、`background-clip`、`background-origin` |
| 2017 | 主流浏览器全面支持 Level 3 | 多背景进入生产可用 |
| 2018 | `background-clip: text` 浏览器支持扩展 | 渐变文字普及 |
| 2020 | CSS Backgrounds Level 4 草案 | `background-clip: text` 标准化 |
| 2023 | `background-clip: text` 进入正式规范 | 无前缀使用成为可能 |
| 2024 | 高 DPI 与 HDR 背景支持 | Display P3 色彩空间背景图 |

### 6.1.7 演进时间线

| 年份 | 规范/事件 | 核心变化 |
| --- | --- | --- |
| 1996 | CSS 1 | 基础背景属性，单背景 |
| 2011 | CSS 2.1 | 百分比定位、简写属性 |
| 2011 | WebKit `-webkit-background-clip: text` | 渐变文字效果 |
| 2012 | CSS Backgrounds Level 3 候选推荐 | 多背景、`background-size` |
| 2014 | `background-attachment: local` 支持 | 内容滚动背景跟随 |
| 2017 | Level 3 全面支持 | 多背景生产可用 |
| 2018 | `background-clip: text` 普及 | 渐变文字主流化 |
| 2020 | Level 4 草案 | `background-clip: text` 标准化 |
| 2023 | `background-clip: text` 规范化 | 无前缀支持 |
| 2024 | HDR 背景 | Display P3 色彩 |

---

### 6.2 形式化定义

### 6.2.1 规范条款

依据 [CSS Backgrounds and Borders Module Level 3 §3](https://www.w3.org/TR/css-backgrounds-3/#backgrounds)：

> The background properties allow specifying the background color, the background image, its size, its position, its repeat behavior, its painting area, its positioning area, and its attachment.

以及 [CSS Backgrounds Module Level 4 §3.7](https://www.w3.org/TR/css-backgrounds-4/#background-clip)：

> The `background-clip` property determines the background painting area, which determines the area within which the background is painted.

### 6.2.2 核心术语

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 背景层 | Background Layer | `background-image` 中的一张图像或渐变 |
| 背景栈 | Background Stack | 多背景层的有序集合，第一个声明在最上层 |
| 绘制区域 | Painting Area | `background-clip` 决定的背景绘制边界 |
| 定位区域 | Positioning Area | `background-origin` 决定的背景定位起点 |
| 定位点 | Position Point | `background-position` 在定位区域内的坐标 |
| 缩放模式 | Sizing Mode | `background-size` 决定的图像缩放算法 |
| 重复模式 | Repeat Mode | `background-repeat` 决定的图像平铺方式 |
| 附件模式 | Attachment Mode | `background-attachment` 决定的滚动行为 |
| 背景颜色 | Background Color | `background-color`，始终位于背景栈最底层 |

### 6.2.3 背景属性全景

| 属性 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| `background-color` | `<color>` | `transparent` | 背景颜色，位于最底层 |
| `background-image` | `<image>` \| `none` | `none` | 背景图像或渐变 |
| `background-repeat` | `repeat` \| `repeat-x` \| `repeat-y` \| `no-repeat` \| `space` \| `round` | `repeat` | 重复模式 |
| `background-attachment` | `scroll` \| `fixed` \| `local` | `scroll` | 滚动行为 |
| `background-position` | `<position>` | `0% 0%` | 定位点 |
| `background-clip` | `border-box` \| `padding-box` \| `content-box` \| `text` | `border-box` | 绘制区域 |
| `background-origin` | `padding-box` \| `border-box` \| `content-box` | `padding-box` | 定位区域 |
| `background-size` | `auto` \| `cover` \| `contain` \| `<length>` \| `<percentage>` | `auto` | 缩放模式 |

### 6.2.4 `background` 简写语法

```
background = 
  [ <bg-layer> , ]* <final-bg-layer>

<bg-layer> = 
  <background-image> 
  || <background-position> [ / <background-size> ]? 
  || <background-repeat> 
  || <background-attachment> 
  || <background-origin> 
  || <background-clip>
```

注意：

1. `background-origin` 与 `background-clip` 在简写中可同时出现，第二个值若省略则与第一个相同。
2. `background-size` 必须跟在 `background-position` 后面，以 `/` 分隔。
3. `background-color` 只能在最后一层（`<final-bg-layer>`）声明。

### 6.2.5 形式化定义：背景栈

设元素的背景栈 $\mathcal{B}$ 为有序集合：

$$
\mathcal{B} = (L_1, L_2, \ldots, L_n, C)
$$

其中 $L_i$ 为第 $i$ 个背景层（图像或渐变），$C$ 为 `background-color`。绘制顺序为 $L_1$ 在最上层，$L_n$ 在 $C$ 之上，$C$ 在最底层。

形式化地，第 $i$ 层的绘制函数：

$$
\text{Paint}(L_i, x, y) = \text{Composite}\left(\text{Draw}(L_i, x, y), \text{Paint}(L_{i+1}, x, y)\right)
$$

其中 $\text{Composite}$ 是合成操作（默认为 `source-over`），$\text{Draw}(L_i, x, y)$ 是单层绘制函数。

### 6.2.6 形式化定义：`background-size`

设图像原始尺寸为 $(w_0, h_0)$，容器尺寸为 $(W, H)$，`background-size` 取值为 $S$。定义缩放函数 $\text{Size}(S, w_0, h_0, W, H)$：

$$
\text{Size}(\text{cover}, w_0, h_0, W, H) = \left(W, W \cdot \frac{h_0}{w_0}\right) \quad \text{if } \frac{W}{w_0} \ge \frac{H}{h_0}
$$

$$
\text{Size}(\text{cover}, w_0, h_0, W, H) = \left(H \cdot \frac{w_0}{h_0}, H\right) \quad \text{if } \frac{W}{w_0} < \frac{H}{h_0}
$$

$$
\text{Size}(\text{contain}, w_0, h_0, W, H) = \left(W, W \cdot \frac{h_0}{w_0}\right) \quad \text{if } \frac{W}{w_0} \le \frac{H}{h_0}
$$

$$
\text{Size}(\text{contain}, w_0, h_0, W, H) = \left(H \cdot \frac{w_0}{h_0}, H\right) \quad \text{if } \frac{W}{w_0} > \frac{H}{h_0}
$$

`cover` 保证图像覆盖整个容器（可能裁剪），`contain` 保证图像完整显示（可能留白）。

### 6.2.7 形式化定义：`background-position`

`background-position` 的百分比定位遵循以下公式：

$$
\text{Pos}(p\%) = p\% \cdot (W_{\text{container}} - W_{\text{image}})
$$

其中 $W_{\text{container}}$ 是定位区域宽度（由 `background-origin` 决定），$W_{\text{image}}$ 是缩放后图像宽度。

- `0% 0%`：图像左上角与容器左上角对齐。
- `50% 50%`：图像中心与容器中心对齐。
- `100% 100%`：图像右下角与容器右下角对齐。

长度值（如 `10px`）则是绝对偏移：

$$
\text{Pos}(L) = L
$$

四值语法 `right 10px bottom 20px` 表示从右边偏移 10px，从底部偏移 20px。

### 6.2.8 形式化定义：`background-clip` 与 `background-origin`

设元素的盒模型区域：

- Border Box：$B = \{(x, y) : 0 \le x \le W_{\text{border}}, 0 \le y \le H_{\text{border}}\}$
- Padding Box：$P = \{(x, y) : bw_l \le x \le W_{\text{border}} - bw_r, bw_t \le y \le H_{\text{border}} - bw_b\}$
- Content Box：$K = \{(x, y) : bw_l + pw_l \le x \le W_{\text{border}} - bw_r - pw_r, \ldots\}$

`background-clip` 决定绘制区域 $D$：

$$
D = \begin{cases}
B, & \text{background-clip: border-box} \\
P, & \text{background-clip: padding-box} \\
K, & \text{background-clip: content-box} \\
\text{Text}, & \text{background-clip: text}
\end{cases}
$$

`background-origin` 决定定位区域 $P_A$：

$$
P_A = \begin{cases}
B, & \text{background-origin: border-box} \\
P, & \text{background-origin: padding-box} \\
K, & \text{background-origin: content-box}
\end{cases}
$$

注意：`background-clip` 与 `background-origin` 是独立的，可以分别设置不同值。

### 6.2.9 形式化定义：`background-attachment`

`background-attachment` 决定背景相对于什么坐标系滚动：

$$
\text{Coord}(\text{attachment}) = \begin{cases}
\text{Document}, & \text{scroll} \\
\text{Viewport}, & \text{fixed} \\
\text{Element}, & \text{local}
\end{cases}
$$

- `scroll`：背景相对于文档滚动（即随页面滚动，但不随元素内容滚动）。
- `fixed`：背景相对于视口固定（不随页面或元素内容滚动）。
- `local`：背景相对于元素内容滚动（随元素内容滚动）。

### 6.2.10 背景绘制顺序

浏览器绘制背景的完整顺序：

1. 绘制 `background-color`（最底层）。
2. 从最后一层到第一层（从底到顶），依次绘制每个 `background-image` 层。
3. 每层依次应用：`background-size` → `background-position` → `background-repeat` → `background-clip`。
4. 在所有背景层之上绘制 `border`（边框）。
5. 在 `border` 之上绘制内容（文本、子元素）。

形式化地：

$$
\text{Render} = \text{Content} \succ \text{Border} \succ L_1 \succ L_2 \succ \cdots \succ L_n \succ C
$$

其中 $\succ$ 表示「在...之上绘制」。

---

### 6.3 理论推导与原理解析

### 6.3.1 多背景的层级模型

CSS 多背景采用「栈式合成」模型，每层独立计算位置、尺寸、重复模式，然后按顺序合成。设第 $i$ 层的图像为 $I_i$，定位点为 $(x_i, y_i)$，尺寸为 $(w_i, h_i)$，则该层的绘制：

$$
\text{Layer}_i(x, y) = \begin{cases}
I_i\left(\frac{x - x_i}{w_i}, \frac{y - y_i}{h_i}\right), & \text{if } (x, y) \in [x_i, x_i + w_i] \times [y_i, y_i + h_i] \\
\text{transparent}, & \text{otherwise}
\end{cases}
$$

多层的合成：

$$
\text{Background}(x, y) = \text{Blend}\left(\text{Layer}_1(x, y), \text{Background}_{2..n}(x, y)\right)
$$

其中 $\text{Blend}$ 默认是 alpha 合成（`source-over`）。

### 6.3.2 `background-size: cover` 的几何推导

设图像原始尺寸为 $(w_0, h_0)$，容器尺寸为 $(W, H)$。`cover` 要求图像缩放后完全覆盖容器，即：

$$
\frac{w_{\text{scaled}}}{W} \ge 1 \quad \wedge \quad \frac{h_{\text{scaled}}}{H} \ge 1
$$

且保持宽高比：

$$
\frac{w_{\text{scaled}}}{h_{\text{scaled}}} = \frac{w_0}{h_0}
$$

取最小缩放比例满足上述约束：

$$
s = \max\left(\frac{W}{w_0}, \frac{H}{h_0}\right)
$$

则：

$$
w_{\text{scaled}} = s \cdot w_0, \quad h_{\text{scaled}} = s \cdot h_0
$$

由于 $s \ge W/w_0$ 且 $s \ge H/h_0$，缩放后图像至少覆盖容器。若宽高比不匹配，超出部分被 `background-clip` 裁剪。

### 6.3.3 `background-size: contain` 的几何推导

`contain` 要求图像完整显示，即：

$$
\frac{w_{\text{scaled}}}{W} \le 1 \quad \wedge \quad \frac{h_{\text{scaled}}}{H} \le 1
$$

取最大缩放比例：

$$
s = \min\left(\frac{W}{w_0}, \frac{H}{h_0}\right)
$$

则缩放后图像完整显示，但可能在某一方向留白。

### 6.3.4 `background-position` 百分比的几何意义

百分比的精确定义：图像的 $p\%$ 点与容器的 $p\%$ 点对齐。形式化地：

$$
x_{\text{image}} = p\% \cdot w_{\text{image}}, \quad x_{\text{container}} = p\% \cdot W
$$

$$
x_{\text{offset}} = x_{\text{container}} - x_{\text{image}} = p\% \cdot (W - w_{\text{image}})
$$

因此：

- `0%`：图像左边缘与容器左边缘对齐。
- `50%`：图像中心与容器中心对齐。
- `100%`：图像右边缘与容器右边缘对齐。

这种「相对对齐」设计使得百分比比绝对偏移更直观：`50% 50%` 总是居中，无论图像与容器尺寸如何。

### 6.3.5 `background-clip` 与 `background-origin` 的独立性

考虑以下场景：

```css
.box {
  background-image: url('image.png');
  background-origin: border-box;   /* 定位起点包含 border */
  background-clip: padding-box;    /* 但只绘制到 padding 边界 */
  border: 10px solid rgba(0,0,0,0.2);
}
```

此时：

- 图像定位起点在 border-box（即左上角包含 border）。
- 但图像绘制被裁剪到 padding-box，超出 padding 的部分不显示。

这种组合常用于：背景图对齐到外边界（包含 border），但避免被 border 遮挡。

### 6.3.6 `background-attachment: fixed` 的视口绑定

`background-attachment: fixed` 将背景绑定到视口坐标系：

$$
\text{Pos}_{\text{fixed}}(\text{scroll}_x, \text{scroll}_y) = \text{Pos}_{\text{initial}}(0, 0)
$$

即无论页面如何滚动，背景相对视口保持不动。这常用于视差滚动效果。

但移动端浏览器（特别是 iOS Safari）出于性能考虑，禁用 `fixed` 的视口绑定，将其降级为 `scroll` 行为。这是移动端视差滚动效果失效的常见原因。

### 6.3.7 `background-attachment: local` 的内容滚动

`background-attachment: local` 将背景绑定到元素的内容坐标系：

$$
\text{Pos}_{\text{local}}(\text{scroll}_x, \text{scroll}_y) = \text{Pos}_{\text{initial}} + (\text{scroll}_x, \text{scroll}_y)
$$

即背景随元素内容滚动。这适用于可滚动容器内的背景（如聊天窗口的水印）。

### 6.3.8 `background-clip: text` 的几何

`background-clip: text` 将背景裁剪到文字的 glyph 区域：

$$
D_{\text{text}} = \{(x, y) : (x, y) \in \text{Glyph}(\text{text})\}
$$

这要求文字本身有颜色（`color`）或填充（`-webkit-text-fill-color`）设为 `transparent`，否则文字会遮挡背景。完整实现：

```css
.gradient-text {
  background: linear-gradient(to right, #667eea, #764ba2);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent; /* 回退 */
}
```

### 6.3.9 `background-repeat: space` 与 `round` 的算法

`space`：在不裁剪的前提下，尽可能多地放置图像，剩余空间均匀分配到图像之间：

$$
n = \left\lfloor \frac{W}{w_{\text{image}}} \right\rfloor
$$

$$
\text{gap} = \frac{W - n \cdot w_{\text{image}}}{n + 1}
$$

`round`：将图像缩放为整数倍以填满容器：

$$
n = \text{round}\left(\frac{W}{w_{\text{image}}}\right)
$$

$$
w_{\text{scaled}} = \frac{W}{n}
$$

`space` 保留图像原始尺寸但留空隙，`round` 拉伸图像以填满。

### 6.3.10 多背景的性能模型

浏览器渲染多背景的成本：

1. **图像解码**：每张图像需独立解码（可并行）。
2. **光栅化**：每层独立光栅化为位图。
3. **合成**：多层按顺序合成。

设层数为 $n$，每层光栅化时间为 $t_r$，合成时间为 $t_c$，则总渲染时间：

$$
T = n \cdot t_r + n \cdot t_c
$$

实测：4 层背景在现代浏览器（2024）约耗时 2-5ms，对 60 FPS（16.67ms 帧预算）影响可控；超过 8 层可能引发掉帧。

---

## 7. 本章综合挑战（选做）

1. 用 `background-color` + `background-image` + `background-repeat` 做一张卡片背景；
2. 用 `background-size: cover` 让图片铺满容器且不变形；
3. 用多重背景叠加（逗号分隔）实现“纹理 + 渐变”；
4. 用 `background-blend-mode: multiply` 让背景图与底色融合。

## 8. 核心知识点

> 一句话记住背景：`color` 打底，`image` 贴图，`repeat` 控平铺，`position` 定位置，`size` 定大小；多背景逗号分隔，简写顺序 color image position/size repeat。

- `background-color`：背景底色，永远最先加载；
- `background-image`：背景图或渐变，不参与布局；
- `background-repeat`：`repeat`/`no-repeat`/`repeat-x`/`repeat-y`；
- `background-position` 与 `background-size`：定位与尺寸，`cover`/`contain` 常用；
- 多重背景用逗号分隔，第一层在最上面；
- `background-blend-mode` 控制背景层之间的混合；
- 简写 `background` 会重置未写的子属性，注意顺序。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记底色 | 图片加载前一片白 | 始终给 `background-color` |
| 大图直接贴 | 加载慢、浪费流量 | 用 `background-size: cover` + 压缩图 |
| 简写重置 | 简写会清空其它背景属性 | 简写放最后或单独写子属性 |
| 多重背景顺序反了 | 显示层级不对 | 第一层放最上层 |
| 混合模式过度 | 文字可读性下降 | 混合后检查对比度 |

## 10. 扩展学习

- 渐变：`css/024-Gradient`；
- 阴影：`css/025-Shadow`；
- 滤镜与混合：`css/048-CSSFilters`（滤镜体系）；
- 响应式背景：`css/033-ResponsiveDesign`。

## 附录 A：术语表

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 背景层 | Background Layer | `background-image` 中的一张图像或渐变 |
| 背景栈 | Background Stack | 多背景层的有序集合 |
| 绘制区域 | Painting Area | `background-clip` 决定的背景绘制边界 |
| 定位区域 | Positioning Area | `background-origin` 决定的定位起点 |
| 缩放模式 | Sizing Mode | `background-size` 决定的缩放算法 |
| 附件模式 | Attachment Mode | `background-attachment` 决定的滚动行为 |
| 视差滚动 | Parallax Scrolling | 背景与内容以不同速度滚动的效果 |
| 渐变文字 | Gradient Text | 通过 `background-clip: text` 实现的渐变填充文字 |
| 高 DPI | High DPI | 每英寸点数较高的屏幕（Retina） |
| 视口 | Viewport | 浏览器可视区域 |
| 盒模型 | Box Model | CSS 元素的盒子结构（content + padding + border + margin） |
| 合成层 | Compositing Layer | 浏览器为优化渲染而创建的独立图层 |

## 附录 B：浏览器兼容性

| 特性 | Chrome | Firefox | Safari | Edge | iOS Safari |
| --- | --- | --- | --- | --- | --- |
| 多背景 (`background-image: url(), url()`) | 1.0 | 3.6 | 1.3 | 12 | 1.0 |
| `background-size` | 1.0 | 3.6 | 3.0 | 12 | 1.0 |
| `background-size: cover/contain` | 3.0 | 3.6 | 4.1 | 12 | 4.0 |
| `background-clip` | 1.0 | 4.0 | 3.0 (with `-webkit-`) | 12 | 3.2 (with `-webkit-`) |
| `background-origin` | 1.0 | 4.0 | 3.0 | 12 | 3.2 |
| `background-attachment: local` | 4.0 | 25 | 5.0 | 12 | 5.0 |
| `background-clip: text` (with `-webkit-`) | 4.0 | 49 | 5.0 | 12 | 5.0 |
| `background-clip: text` (standard) | 85 | 95 | 16.0 | 85 | 16.0 |
| `image-set()` | 21 (with `-webkit-`) | 88 | 14 (with `-webkit-`) | 21 | 14 (with `-webkit-`) |
| 四值 `background-position` | 25 | 13 | 7.0 | 12 | 7.0 |
| `background-repeat: space/round` | 30 | 49 | 9.0 | 12 | 9.0 |

## 附录 C：调试检查清单

### C.1 背景不显示

- [ ] 检查 `background-image` URL 是否正确。
- [ ] 检查 `background-repeat` 是否为 `no-repeat`（可能图像在视口外）。
- [ ] 检查 `background-size` 是否为 `0` 或过小。
- [ ] 检查元素是否有尺寸（`width`、`height`）。
- [ ] 检查 `background-clip` 是否为 `text` 但文字颜色不透明。
- [ ] 检查父元素是否设置了 `overflow: hidden` 裁剪了背景。

### C.2 背景位置错误

- [ ] 检查 `background-position` 语法（百分比、长度、关键字）。
- [ ] 检查 `background-origin` 是否影响定位起点。
- [ ] 检查 `background-size` 是否影响图像尺寸。
- [ ] 检查元素是否有 `padding` 或 `border` 影响定位。

### C.3 背景尺寸错误

- [ ] 检查 `background-size` 取值（`cover`、`contain`、长度、百分比）。
- [ ] 检查图像原始宽高比。
- [ ] 检查 `background-origin` 是否影响尺寸计算。
- [ ] 检查容器尺寸是否正确。

### C.4 多背景顺序错误

- [ ] 检查 `background-image` 中各层的顺序（第一个在最上）。
- [ ] 检查每层的 `background-size`、`background-position` 等是否用逗号分隔对应。
- [ ] 检查 `background-color` 是否仅在最后一层声明。

### C.5 渐变文字不显示

- [ ] 检查 `background-clip: text` 与 `-webkit-background-clip: text` 是否同时声明。
- [ ] 检查 `color: transparent` 或 `-webkit-text-fill-color: transparent` 是否设置。
- [ ] 检查浏览器是否支持（使用 `@supports` 检测）。
- [ ] 检查是否有 `@supports` 回退方案。

### C.6 性能问题

- [ ] 检查背景层数（建议 ≤ 4 层）。
- [ ] 检查背景图大小（建议 ≤ 200KB）。
- [ ] 检查是否使用了懒加载。
- [ ] 检查 `background-attachment: fixed` 是否在移动端使用（建议替换）。
- [ ] 检查是否使用了 WebP/AVIF 格式。

### C.7 可访问性检查

- [ ] 检查背景上文字的对比度（WCAG AA 4.5:1）。
- [ ] 检查 `background-clip: text` 是否有回退。
- [ ] 检查高对比度模式下的回退（`@media (forced-colors: active)`）。
- [ ] 检查打印样式（`@media print`）。
- [ ] 检查屏幕阅读器是否能正确读取文字内容。

---

> **结语**：CSS 背景系统是 Web 视觉设计的基础设施。从 CSS 1 的单背景到 CSS Backgrounds Level 4 的 `background-clip: text` 标准化，背景系统经历了近 30 年的演进。理解其层级模型、绘制算法、定位机制与性能特性，是构建高质量 Web 体验的关键。在实践中，应遵循「设计令牌化、响应式优先、可访问性保障、性能预算」四大原则，将 CSS 背景系统作为设计系统的核心组成部分。
## 附录 D：背景属性速查

### D.1 background-color 背景颜色

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

**讲解：**

- `background-blend-mode` 混合“背景图层之间”（图片与渐变、多张背景图之间）；
- `mix-blend-mode` 混合“元素与其下层内容”（文字与背景图叠加产生差异效果）；
- 常用模式：`multiply` 正片叠底（纹理压暗）、`screen` 滤色（提亮）、`difference` 差异（反相）；
- 混合模式只影响视觉，不改变元素本身；大面积混合有性能开销。


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

<!-- ============ 文档分隔线：007-css/027-CSSMask.md ============ -->

## 0. 直觉：遮罩是“用一张图的透明度决定显示哪里”

`background` 决定元素画什么，`mask` 决定元素哪些部分能露出来。遮罩图是黑色/白色/透明通道：完全不透明区域显示，透明区域隐藏，中间灰度产生半透明过渡。最常用的效果是“图片底部渐隐”与“形状镂空”。

## 1. mask-image 与 mask-size

```css
.fade-bottom {
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent);
  mask-image: linear-gradient(to bottom, black 60%, transparent);
}
```

**讲解：** 渐变遮罩是最常用写法：黑色区域完全显示，向透明渐变处逐步隐藏，实现“图片到底部淡出”。注意兼容性：许多浏览器仍需要 `-webkit-mask-image` 前缀。

## 2. 用图片做遮罩

```css
.stamp {
  width: 200px;
  height: 200px;
  background: #4f5bd5;
  -webkit-mask-image: url("stamp.svg");
  mask-image: url("stamp.svg");
  -webkit-mask-size: contain;
  mask-size: contain;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}
```

**讲解：** SVG 遮罩适合“任意形状容器”：元素真实尺寸不变，只是显示区域被裁剪成图形。`mask-size`/`mask-repeat`/`mask-position` 的取值与 `background-size` 完全一致。

## 3. 与 clip-path 的分工

```css
.clip {
  clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%);  /* 菱形裁剪 */
}
```

**讲解：** `clip-path` 用几何形状“硬裁剪”，没有半透明过渡，且裁剪后不参与事件命中（指针事件区域也变小）；`mask` 用图像通道“软裁剪”，支持渐变与半透明，适合“淡出、毛玻璃边缘、贴图质感”。两者都会保留元素的布局占位。

## 4. 完整示例：卡片底部渐隐

```html
<style>
  .card {
    height: 240px;
    background: url("photo.jpg") center/cover;
    -webkit-mask-image: linear-gradient(to bottom, black 55%, transparent 95%);
    mask-image: linear-gradient(to bottom, black 55%, transparent 95%);
  }
</style>
<div class="card"></div>
```

**讲解：** 这是图文卡片“内容渐隐到底部”的标准写法，配合 `mask-mode` 可指定按亮度还是透明度裁剪，进阶可查阅 MDN。

## 5. 动手试试

1. 用线性渐变遮罩实现图片底部淡出；
2. 用 SVG 圆形/星形图片做头像遮罩，对比 `border-radius` 的效果差异；
3. 同一元素叠加 `mask` 与 `clip-path`，观察两者先后作用的视觉效果；
4. 进阶挑战：用 `mask-composite` 做“圆环镂空”效果。

## 6. 核心知识点

> 一句话记住遮罩：mask 用图像的透明/灰度通道决定显示区域，支持渐变软过渡；clip-path 用几何硬裁剪。

- `mask-image` 接受渐变或图片，黑色显示、透明隐藏；
- `mask-size`/`mask-repeat`/`mask-position` 与背景对应属性一致；
- 兼容性：多数浏览器需要 `-webkit-` 前缀；
- `clip-path` 是硬裁剪，`mask` 支持软过渡；
- 两者都不改变元素布局占位；
- 结合渐变函数使用最频繁，见 `css/024-Gradient`。

## 7. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记写 -webkit- 前缀 | 部分浏览器整段失效 | 前缀与标准写法成对书写 |
| 遮罩图未设置 repeat/size | 默认平铺导致效果异常 | 显式设置 `mask-size` 与 `mask-repeat` |
| 需要硬裁剪却用 mask | 性能与语义不匹配 | 几何裁剪用 `clip-path` |
| 遮罩区域需要可点击 | mask 后事件区域仍为原始盒子 | 用 `clip-path` 或调整交互区域 |

## 8. 扩展学习

- 背景体系：`css/026-BackgroundEnhancement`；
- 渐变：`css/024-Gradient`；
- 滤镜组合：`css/048-CSSFilters`；
- 函数与图像处理：`css/053-Function`。

<!-- ============ 文档分隔线：007-css/028-CSSAnimationTransition.md ============ -->

## 1. CSS 过渡（Transition）

### 1.1 过渡基础

CSS过渡允许属性值变化时平滑地从一个状态过渡到另一个状态。

```css
/* 过渡的四个属性 */
.element {
  /* 指定参与过渡的属性 */
  transition-property: background-color, transform;
  /* 过渡持续时间 */
  transition-duration: 0.3s;
  /* 过渡时序函数（缓动曲线） */
  transition-timing-function: ease-in-out;
  /* 过渡延迟时间 */
  transition-delay: 0.1s;

  /* 简写形式 */
  transition:
    background-color 0.3s ease-in-out 0.1s,
    transform 0.3s ease-in-out 0.1s;

  /* 所有属性过渡 */
  transition: all 0.3s ease;
}

.element:hover {
  background-color: #3498db;
  transform: scale(1.05);
}
```

### 1.2 时序函数详解

```css
/* 预定义时序函数 */
.box1 {
  transition-timing-function: ease;
} /* 默认：慢-快-慢 */
.box2 {
  transition-timing-function: linear;
} /* 匀速 */
.box3 {
  transition-timing-function: ease-in;
} /* 慢-快 */
.box4 {
  transition-timing-function: ease-out;
} /* 快-慢 */
.box5 {
  transition-timing-function: ease-in-out;
} /* 慢-快-慢 */

/* 贝塞尔曲线 */
.box6 {
  transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
} /* 弹性效果 */

/* 步进函数 */
.box7 {
  transition-timing-function: steps(4, end);
} /* 4步跳跃 */
.box8 {
  transition-timing-function: steps(10, start);
} /* 10步，立即跳到下一步 */
```

### 1.3 可过渡的属性

并非所有CSS属性都支持过渡，只有具有**中间值**的属性才能过渡。

```css
/* 支持过渡的常见属性 */
.supported {
  /* 颜色 */
  transition:
    color 0.3s,
    background-color 0.3s,
    border-color 0.3s;
  /* 尺寸 */
  transition:
    width 0.3s,
    height 0.3s,
    margin 0.3s,
    padding 0.3s;
  /* 变换 */
  transition:
    transform 0.3s,
    opacity 0.3s;
  /* 阴影 */
  transition:
    box-shadow 0.3s,
    text-shadow 0.3s;
}

/* 不支持过渡的属性 */
.not-supported {
  /* display: none → block 无法过渡 */
  /* 建议用 opacity + visibility 替代 */
  transition:
    opacity 0.3s,
    visibility 0.3s;
}
```

### 1.4 实用过渡效果

```css
/* 按钮悬停效果 */
.btn {
  padding: 12px 24px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.btn:hover {
  background-color: #2980b9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(52, 152, 219, 0.4);
}

.btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(52, 152, 219, 0.4);
}

/* 卡片悬浮效果 */
.card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

/* 淡入淡出 */
.fade-element {
  opacity: 0;
  visibility: hidden;
  transition:
    opacity 0.3s ease,
    visibility 0.3s ease;
}

.fade-element.visible {
  opacity: 1;
  visibility: visible;
}
```

## 2. CSS 动画（Animation）

### 2.1 关键帧动画

```css
/* 定义关键帧 */
@keyframes slideIn {
  from {
    transform: translateX(-100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* 多关键帧动画 */
@keyframes bounce {
  0% {
    transform: translateY(0);
  }
  25% {
    transform: translateY(-20px);
  }
  50% {
    transform: translateY(0);
  }
  75% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0);
  }
}

/* 应用动画 */
.slide-in {
  animation: slideIn 0.5s ease-out forwards;
}

.bounce {
  animation: bounce 1s ease infinite;
}
```

### 2.2 animation 属性详解

```css
.animation-demo {
  /* 动画名称 */
  animation-name: slideIn;
  /* 动画持续时间 */
  animation-duration: 0.5s;
  /* 时序函数 */
  animation-timing-function: ease-out;
  /* 延迟时间 */
  animation-delay: 0.2s;
  /* 播放次数: 数字 | infinite */
  animation-iteration-count: 1;
  /* 播放方向: normal | reverse | alternate | alternate-reverse */
  animation-direction: normal;
  /* 填充模式: none | forwards | backwards | both */
  animation-fill-mode: forwards;
  /* 播放状态: running | paused */
  animation-play-state: running;

  /* 简写 */
  /* animation: name duration timing-function delay iteration-count direction fill-mode */
  animation: slideIn 0.5s ease-out 0.2s 1 normal forwards;
}
```

### 2.3 animation-fill-mode 详解

```css
/* none: 动画前后都应用原始样式 */
.fill-none {
  animation-fill-mode: none;
}

/* forwards: 动画结束后保持最后一帧 */
.fill-forwards {
  animation-fill-mode: forwards;
}

/* backwards: 动画延迟期间应用第一帧 */
.fill-backwards {
  animation-fill-mode: backwards;
}

/* both: 同时应用forwards和backwards */
.fill-both {
  animation-fill-mode: both;
}
```

### 2.4 实用动画效果

```css
/* 加载旋转动画 */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e0e0e0;
  border-top-color: #3498db;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

/* 脉冲动画 */
@keyframes pulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.05);
    opacity: 0.8;
  }
}

.pulse {
  animation: pulse 2s ease-in-out infinite;
}

/* 打字机效果 */
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

@keyframes blink {
  50% {
    border-color: transparent;
  }
}

.typewriter {
  overflow: hidden;
  white-space: nowrap;
  border-right: 2px solid #333;
  width: 0;
  animation:
    typing 3s steps(20) forwards,
    blink 0.7s step-end infinite;
}

/* 摇晃动画 */
@keyframes shake {
  0%,
  100% {
    transform: translateX(0);
  }
  10%,
  30%,
  50%,
  70%,
  90% {
    transform: translateX(-5px);
  }
  20%,
  40%,
  60%,
  80% {
    transform: translateX(5px);
  }
}

.shake {
  animation: shake 0.5s ease-in-out;
}
```

## 3. CSS 变换（Transform）

### 3.1 2D 变换

```css
.transform-demo {
  /* 平移 */
  transform: translate(50px, 100px); /* 水平50px，垂直100px */
  transform: translateX(50px); /* 仅水平 */
  transform: translateY(100px); /* 仅垂直 */
  transform: translate(-50%, -50%); /* 百分比相对自身 */

  /* 旋转 */
  transform: rotate(45deg); /* 顺时针45度 */
  transform: rotate(-0.25turn); /* 逆时针1/4圈 */

  /* 缩放 */
  transform: scale(1.5); /* 整体放大1.5倍 */
  transform: scale(1.5, 2); /* 水平1.5倍，垂直2倍 */
  transform: scaleX(2); /* 仅水平缩放 */

  /* 倾斜 */
  transform: skew(10deg, 20deg); /* 水平10度，垂直20度 */
  transform: skewX(10deg); /* 仅水平倾斜 */

  /* 组合变换（从右到左应用） */
  transform: translate(50px, 0) rotate(45deg) scale(1.2);
}
```

### 3.2 3D 变换

```css
.transform-3d {
  /* 开启3D上下文 */
  transform-style: preserve-3d;
  /* 透视距离 */
  perspective: 1000px;

  /* 3D旋转 */
  transform: rotateX(45deg); /* 绕X轴旋转 */
  transform: rotateY(45deg); /* 绕Y轴旋转 */
  transform: rotate3d(1, 1, 0, 45deg); /* 绕自定义轴旋转 */

  /* 3D平移 */
  transform: translateZ(100px); /* 沿Z轴平移 */

  /* 3D缩放 */
  transform: scaleZ(2); /* 沿Z轴缩放 */
}

/* 翻转卡片效果 */
.flip-card {
  width: 300px;
  height: 200px;
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front,
.flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

.flip-card-back {
  transform: rotateY(180deg);
}
```

### 3.3 transform-origin

```css
/* 变换原点 */
.origin-center {
  transform-origin: center center;
} /* 默认 */
.origin-top-left {
  transform-origin: top left;
}
.origin-custom {
  transform-origin: 30% 70%;
}
.origin-pixel {
  transform-origin: 50px 100px;
}

/* 不同原点下的旋转效果差异 */
.rotate-center {
  transform-origin: center;
  transform: rotate(45deg); /* 绕中心旋转 */
}

.rotate-corner {
  transform-origin: bottom right;
  transform: rotate(45deg); /* 绕右下角旋转 */
}
```

## 4. 性能优化

### 4.1 高性能动画属性

```css
/* 推荐：仅触发Composite的属性（GPU加速） */
.good-animation {
  transition:
    transform 0.3s ease,
    opacity 0.3s ease;
}

/* 避免：触发Layout的属性（性能差） */
.bad-animation {
  transition:
    width 0.3s,
    height 0.3s,
    top 0.3s,
    left 0.3s;
}

/* 触发层级 */
/* Layout（重排）> Paint（重绘）> Composite（合成） */
/* Layout触发属性: width, height, margin, padding, top, left... */
/* Paint触发属性: color, background, box-shadow, border-radius... */
/* Composite触发属性: transform, opacity */
```

### 4.2 will-change 提示

```css
/* 提示浏览器提前优化 */
.will-animate {
  will-change: transform, opacity;
}

/* 注意：不要滥用will-change，它会消耗额外内存 */
/* 只在即将发生动画时添加，动画结束后移除 */

/* 使用JS动态控制 */
/*
element.addEventListener('mouseenter', () => {
    element.style.willChange = 'transform';
});
element.addEventListener('animationend', () => {
    element.style.willChange = 'auto';
});
*/
```

### 4.3 prefers-reduced-motion

```css
/* 尊重用户的减少动画偏好 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 5. 常见问题与解决方案

### 5.1 动画闪烁

**问题**：动画开始或结束时出现闪烁

```css
/* 解决方案：使用transform代替top/left */
/* 错误 */
.flash-bad {
  transition:
    top 0.3s,
    left 0.3s;
}

/* 正确 */
.flash-good {
  transition: transform 0.3s;
  will-change: transform;
}
```

### 5.2 动画卡顿

**问题**：动画帧率低，不流畅

```css
/* 解决方案 */
.smooth-animation {
  /* 1. 使用GPU加速属性 */
  transform: translateZ(0);

  /* 2. 提升到独立图层 */
  will-change: transform;

  /* 3. 避免同时动画过多元素 */
}

/* JS中检查帧率 */
/*
let lastTime = performance.now();
function checkFPS() {
    const now = performance.now();
    const fps = 1000 / (now - lastTime);
    lastTime = now;
    console.log(`FPS: ${fps}`);
    requestAnimationFrame(checkFPS);
}
*/
```

### 5.3 动画结束状态回弹

**问题**：动画结束后回到初始状态

```css
/* 解决方案：使用animation-fill-mode: forwards */
@keyframes slideIn {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

.stay-at-end {
  animation: slideIn 0.5s ease forwards; /* forwards保持结束状态 */
}
```

## 6. 总结与最佳实践

### 6.1 过渡 vs 动画选择

| 场景                     | 选择       | 原因           |
| :----------------------- | :--------- | :------------- |
| 状态变化（hover、click） | transition | 简单、声明式   |
| 循环播放                 | animation  | 支持infinite   |
| 多步骤动画               | animation  | 支持多关键帧   |
| 无触发自动播放           | animation  | 不需要状态变化 |

### 6.2 最佳实践

1. **优先使用 transform 和 opacity**：GPU加速，性能最佳
2. **避免动画布局属性**：width、height、top、left等触发重排
3. **使用 will-change 谨慎**：只在需要时添加，用完移除
4. **尊重用户偏好**：使用 prefers-reduced-motion 媒体查询
5. **控制动画时长**：交互反馈 0.1-0.3s，装饰动画 0.3-0.5s
6. **使用 cubic-bezier**：自定义缓动曲线比预设更自然
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

## 动手试试

1. 给按钮写 `transition: background-color 0.3s`，hover 变色观察过渡；
2. 用 `@keyframes` 做一个“淡入 + 上移”的入场动画；
3. 用 `animation-iteration-count: infinite` 做呼吸灯效果；
4. 进阶挑战：配合 `prefers-reduced-motion` 在用户减少动效时关闭动画。

## 核心知识点

> 一句话记住动画：`transition` 是“状态变化时的过渡”，`animation` 是“按关键帧自动播放”；动画属性、时长、缓动函数（ease）与循环次数四要素。

- `transition`：属性、时长、缓动、延迟，hover 等状态变化时触发；
- `@keyframes`：`from`/`to` 或百分比关键帧定义动画过程；
- `animation` 简写：name duration timing-function delay iteration-count direction fill-mode；
- 只对可动画属性做过渡（transform/opacity 性能最佳）；
- 动效遵守 `prefers-reduced-motion`，为减少动效用户关闭动画；
- `transform` 与 `opacity` 走合成层，避免 layout/paint 抖动。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 动画属性过多 | 性能差 | 只用 transform/opacity |
| 忘记缓动函数 | 动画生硬 | 用 ease/cubic-bezier |
| 无限动画扰民 | 影响阅读 | 尊重 reduced-motion，限制循环 |
| transition 写错属性 | 不触发 | 确认属性可动画 |
| 动画结束后跳变 | 状态复位 | 用 `animation-fill-mode: forwards` |

## 扩展学习

- 关键帧与缓动：`css/064-CSSNewFeatures`；
- 3D 变换：`css/069-Transform3D`；
- 可访问性：`css/045-AccessibleStyling`（减少动效）；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`。

<!-- ============ 文档分隔线：007-css/029-CSSViewTransitions.md ============ -->

## 0. 直觉：让“旧画面”和“新画面”自然地切换

平时切换列表/详情页是“瞬间跳变”。View Transitions 会先拍下旧画面，再拍下新画面，然后自动生成一段默认的淡入淡出过渡；开发者可以只关注“新旧状态”，动画交给浏览器。

## 1. 单文档过渡：startViewTransition

```html
<button id="switch">切换主题</button>
```

```js
document.getElementById("switch").addEventListener("click", () => {
  document.startViewTransition(() => {
    document.body.classList.toggle("dark");
  });
});
```

**讲解：** 回调里同步修改 DOM，浏览器自动为整个页面生成过渡。现代浏览器（Chrome/Edge/Safari 18+）均已支持，旧浏览器直接跳过动画，功能不受影响。

## 2. 命名视图：只让部分元素动

```css
.avatar {
  view-transition-name: avatar;
}

::view-transition-group(avatar) {
  animation-duration: 0.4s;
}
```

**讲解：** 默认整个页面都参与过渡；给元素加 `view-transition-name` 后，只有该元素单独生成“旧→新”的位移与缩放动画，其余部分保持淡入淡出，适合头像、卡片、图片列表。

## 3. 自定义动画与禁用

```css
::view-transition-old(root) {
  animation: fade-out 0.2s ease forwards;
}
::view-transition-new(root) {
  animation: fade-in 0.2s ease forwards;
}

@keyframes fade-out {
  to { opacity: 0; }
}
@keyframes fade-in {
  from { opacity: 0; }
}
```

**讲解：** `::view-transition-old(root)` 与 `::view-transition-new(root)` 分别代表旧/新画面层，可以像普通元素一样写动画。`animation: none` 可禁用某层的默认动画，实现“不想要淡出只想要淡入”等定制。

## 4. 跨文档过渡

```css
/* 在 A 页面（列表）与 B 页面（详情）同时声明 */
html {
  view-transition-name: none;
}
.article-card {
  view-transition-name: article;
}
```

**讲解：** 同源页面之间跳转时，只要新旧页面都有同名的 `view-transition-name` 元素，浏览器会自动衔接两页的该元素动画，实现“卡片从列表飞入详情”的效果。跨文档过渡要求页面处于同源，且不能阻止渲染。

## 5. 与动画/新特性的关系

- `css/028-CSSAnimationTransition`：transition/keyframes 基础，是自定义过渡动画的前提；
- `css/064-CSSNewFeatures`：视图过渡属于现代 CSS 新特性族，与容器查询、@scope 同期推进；
- 视图过渡适合“状态切换”而非“持续动画”，持续动效仍用 animation。

## 6. 动手试试

1. 用 `startViewTransition` 包裹一个明暗主题切换，观察默认淡入淡出；
2. 给列表中的头像加 `view-transition-name`，切换视图时观察单独位移动画；
3. 自定义 `::view-transition-old(root)` 的动画时长与曲线；
4. 进阶挑战：做“列表点击卡片 → 详情页卡片放大展开”的跨文档过渡原型。

## 7. 核心知识点

> 一句话记住视图过渡：startViewTransition 捕获新旧状态，view-transition-name 圈定重点元素，伪元素自定义动画，旧浏览器自动降级。

- `document.startViewTransition(callback)` 触发过渡；
- 默认全页淡入淡出，无需写动画；
- `view-transition-name` 让指定元素单独动画；
- `::view-transition-old/new()` 定制旧/新画面层；
- 跨文档过渡要求同源与同名视图；
- 不支持时静默降级为直接切换。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 默认过渡让整页闪动 | 全页都参与淡入淡出 | 只给关键元素命名视图 |
| 忘记降级方案 | 旧浏览器直接无过渡 | 先保证功能，动画作为增强 |
| 过渡期间重复点击 | 连续触发导致动画叠加 | 加状态锁或在回调中防抖 |
| 与 reduced-motion 冲突 | 动晕用户不适 | 遵循 `prefers-reduced-motion` 关闭过渡 |

## 9. 扩展学习

- 动画与过渡：`css/028-CSSAnimationTransition`；
- 新特性总览：`css/064-CSSNewFeatures`；
- 可访问性与减少动效：`css/045-AccessibleStyling`；
- 滚动驱动动画：`css/030-CSSScrollDrivenAnimations`。

<!-- ============ 文档分隔线：007-css/030-CSSScrollDrivenAnimations.md ============ -->

## 0. 直觉：滚动到哪，动画走到哪

传统做法是 JS 监听 `scroll` 事件，把滚动百分比换算成动画进度。滚动驱动动画直接把 `animation-timeline` 指向“滚动进度”，浏览器按滚动位置驱动关键帧，滚动停下动画就停，无需 JS。

## 1. scroll progress timeline：跟随滚动容器

```css
.progress {
  height: 4px;
  background: #4f5bd5;
  transform-origin: left;
  animation: grow linear both;
  animation-timeline: scroll();   /* 跟随最近滚动容器 */
}

@keyframes grow {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

**讲解：** `scroll()` 时间线把动画进度绑定到滚动位置：页面顶部为 0%，底部为 100%。上面的例子就是“阅读进度条”。默认跟踪最近的滚动容器，可用 `scroll(nearest)`/`scroll(root)` 明确范围。

## 2. view progress timeline：跟随元素可见度

```css
.reveal {
  animation: fade-up both;
  animation-timeline: view();   /* 元素进入/离开视口时驱动 */
}

@keyframes fade-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
```

**讲解：** `view()` 时间线以“元素在视口中的可见度”为进度：元素刚进入视口是 0%，完全进入后是 100%。配合 `animation-range` 可控制从“进入 20%”到“离开 80%”的窗口，实现滚动浮现、视差等效果。

## 3. 控制窗口：animation-range

```css
.parallax {
  animation: float-up both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;   /* 只在进入阶段播放 */
}
```

**讲解：** 默认窗口覆盖“进入 + 离开”全程；`animation-range` 可裁剪为 `entry`（进入阶段）、`exit`（离开阶段）或具体百分比，例如 `entry 0% entry 50%` 表示进入一半时播完。

## 4. 命名时间线：一个滚动容器驱动多个元素

```css
.scroller {
  scroll-timeline-name: --page;   /* 给滚动容器命名 */
}
.item {
  animation: rotate both;
  animation-timeline: --page;     /* 引用命名时间线 */
}
```

**讲解：** 多个元素想共享同一个滚动进度时，用 `scroll-timeline-name` 命名滚动容器，各元素通过 `animation-timeline: --name` 引用，适合整页滚动叙事。

## 5. 兼容与降级

```css
.reveal {
  animation: fade-up 1s ease both;   /* 不支持时的兜底：直接播放一次 */
  animation-timeline: view();
}
```

**讲解：** 不支持滚动驱动动画的浏览器会忽略 `animation-timeline`，此时应保证普通动画先声明，作为兜底。现代 Chrome/Edge 已支持，Safari/Firefox 逐步跟进，上线前查 Baseline。

## 6. 动手试试

1. 用 `scroll()` 实现页面顶部阅读进度条；
2. 用 `view()` 让卡片进入视口时逐张浮现；
3. 用 `animation-range: exit` 实现元素滚出时淡出；
4. 进阶挑战：用命名时间线做一个“滚动翻页”的长页叙事。

## 7. 核心知识点

> 一句话记住滚动驱动动画：animation-timeline 指向 scroll()/view()/命名时间线，动画进度跟滚动走，animation-range 控制播放窗口。

- `scroll()`：进度 = 滚动容器位置；
- `view()`：进度 = 元素在视口中的可见度；
- `animation-range` 裁剪进入/离开阶段；
- `scroll-timeline-name` 命名时间线，多元素共享；
- 先写普通动画做兼容兜底；
- 与滚动捕捉（027）搭配可做翻页体验。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 不支持时无动画 | 功能缺失 | 先写普通动画兜底 |
| 时间线作用范围错 | 绑定了错误的滚动容器 | 显式 `scroll(root)` 或命名时间线 |
| 动画范围失控 | 元素一出现就播完 | 用 `animation-range` 收缩窗口 |
| 忽略 reduced-motion | 大量滚动动画加重不适 | 媒体查询中禁用滚动驱动动画 |

## 9. 扩展学习

- 动画与过渡：`css/028-CSSAnimationTransition`；
- 滚动捕捉：`css/038-ScrollSnap`；
- 视图过渡：`css/029-CSSViewTransitions`；
- 减少动效：`css/045-AccessibleStyling`。

<!-- ============ 文档分隔线：007-css/031-MediaQuery.md ============ -->

## 1. 历史动机与发展脉络

2004 年前后，移动设备开始访问 Web，固定宽度布局在窄屏上需要横向滚动。2007 年 iPhone 发布后，响应式 Web 设计（Responsive Web Design）由 Ethan Marcotte 于 2010 年在 A List Apart 提出，其三大支柱是流式网格、弹性图片与媒体查询。

媒体查询本身起源于 CSS2 的媒体类型（`screen`、`print`、`aural`），Media Queries Level 3（2012 年成为 W3C Recommendation）引入媒体特性（width、orientation 等）与逻辑操作符；Media Queries Level 4（2017 年草案，2022 年前后稳定）新增 `prefers-color-scheme`、`prefers-reduced-motion`、`hover`、`pointer` 等用户偏好与交互能力特性。2023 年起容器查询（Container Queries，CSS Containment Level 3）获得主流浏览器支持，组件级响应式成为新方向，但媒体查询仍是页面级响应式的基石。

```mermaid
timeline
    title 媒体查询演进
    1998 : CSS2 引入媒体类型 screen/print
    2010 : Ethan Marcotte 提出响应式设计
    2012 : Media Queries 3 成为标准
    2018 : prefers-color-scheme 被实现
    2020 : prefers-reduced-motion 广泛支持
    2023 : 容器查询主流支持，与媒体查询互补
```

## 2. 形式化定义

`@media` 规则由媒体查询列表构成，语法：

```css
@media <media-query-list> {
  /* 条件成立时应用的样式 */
}
```

媒体查询列表用逗号分隔多个查询，任一查询为真则整体为真（或语义）。单个查询由可选媒体类型、媒体特性与逻辑操作符组成：

媒体类型：`all`（默认）、`screen`、`print`、`speech`。`not` 只能修饰整个查询（不能修饰单个特性）。

媒体特性以 `(特性: 值)` 或 `(特性)` 形式书写：`(min-width: 768px)`、`(orientation: portrait)`、`(hover: hover)`。无值特性如 `(color)` 表示支持该特性。

逻辑操作符：

`and`：连接媒体类型与特性，全部成立才为真；

`,`：查询列表分隔符，任一查询为真即为真；

`not`：对整个查询取反；

`only`：用于兼容不支持媒体查询的旧浏览器（现代已不必要，仍可保留）。

范围语法（Media Queries Level 4）：`(400px <= width <= 800px)`、`(width >= 768px)` 是新的区间写法，可读性优于 `min/max`，现代浏览器均支持。

```mermaid
flowchart TD
    A["@media screen and (min-width: 768px)"] --> B{"媒体类型为 screen?"}
    B -- "是" --> C{"视口宽度 >= 768px?"}
    C -- "是" --> D["应用样式"]
    C -- "否" --> E["跳过样式"]
    B -- "否" --> E
```

## 3. 理论推导与原理解析

### 3.1 min-width 与 max-width 的不等式

`min-width: 768px` 等价于 `width >= 768px`；`max-width: 767px` 等价于 `width <= 767px`。两者在 767/768 边界互补。移动优先策略使用 `min-width` 从窄到宽逐步增强；桌面优先策略使用 `max-width` 从宽到窄逐步降级。

### 3.2 视口与布局视口

媒体查询中的 `width` 指布局视口宽度（layout viewport），由 `<meta name="viewport" content="width=device-width, initial-scale=1">` 控制。缺失该 meta 时，移动浏览器使用默认视口宽度（如 980px），媒体查询将按 980px 判断，导致移动优先样式失效。因此响应式页面的第一步是正确设置 viewport meta。

### 3.3 媒体查询的层叠行为

媒体查询不改变 CSS 层叠优先级，只控制规则是否参与层叠。因此两条规则同时命中时，后定义者胜出。移动优先写法中，基础样式在前，`min-width` 增强在后，天然符合层叠顺序。

### 3.4 与容器查询的分工

媒体查询参照视口，解决“页面级”响应；容器查询参照最近的容器尺寸，解决“组件级”响应。一个卡片组件在窄侧栏与宽主区中应自适应容器，而不是依赖视口断点。容器查询需要父元素声明 `container-type: inline-size`，且不能替代媒体查询（页面级排版仍需视口信息）。

## 4. 代码示例（带详尽注释）

### 4.1 移动优先断点体系

```css
/* 基础样式：默认面向窄屏（移动优先） */
.grid {
  display: grid;
  grid-template-columns: 1fr; /* 单列 */
  gap: 16px;
}

/* 视口 >= 640px：两列 */
@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 视口 >= 1024px：三列 */
@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

讲解：断点 640/1024 是内容驱动的常用选择。移动优先的要点：基础样式无需媒体查询，增强逐级叠加，因此窄屏设备只加载最简样式。

### 4.2 深色模式

```css
:root {
  --bg: #ffffff;
  --text: #1f1f1f;
}

/* 用户系统偏好深色时切换变量 */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1f1f1f;
    --text: #f0f0f0;
  }
}

body {
  background: var(--bg);
  color: var(--text);
}
```

讲解：`prefers-color-scheme` 读取操作系统或浏览器的深色偏好。通过 CSS 变量切换主题，一套选择器适配两种模式，避免重复编写整套样式。

### 4.3 减少动画偏好

```css
/* 默认动画 */
.banner {
  animation: slide-in 0.6s ease;
}

/* 用户开启“减少动态效果”时关闭动画 */
@media (prefers-reduced-motion: reduce) {
  .banner {
    animation: none;
    transition: none;
  }
}
```

讲解：`prefers-reduced-motion` 服务于前庭障碍与晕动症用户，是 WCAG 2.1 可访问性最佳实践。关闭动画的同时应保证内容立即可见（不要用 `opacity: 0` 残留）。

### 4.4 打印样式

```css
/* 打印时隐藏导航与广告，展开正文 */
@media print {
  .navbar,
  .sidebar,
  .ad {
    display: none !important;
  }
  main {
    width: 100%;
  }
}
```

讲解：`print` 媒体类型为打印优化：隐藏非内容区域、设置黑白配色、避免分页截断。可用 `page-break-inside: avoid` 控制元素不跨页。

### 4.5 方向与指针能力

```css
/* 横屏：两栏布局 */
@media (orientation: landscape) {
  .profile {
    grid-template-columns: 200px 1fr;
  }
}

/* 主输入设备支持悬停：显示桌面悬停效果 */
@media (hover: hover) and (pointer: fine) {
  .item:hover {
    transform: translateY(-2px);
  }
}
```

讲解：`orientation` 适配平板横竖屏；`hover`/`pointer` 区分触屏与鼠标设备，避免触屏设备出现无法取消的悬停态。

### 4.6 范围语法

```css
/* 新语法：只命中 768-1024 区间 */
@media (768px <= width <= 1024px) {
  .container {
    padding: 24px;
  }
}
```

讲解：范围语法表达区间更直观，且避免 767/768 边界笔误。2023 年起所有主流浏览器支持，可放心用于现代项目。

### 4.7 JavaScript 中的媒体查询

```js
// 用 matchMedia 在 JS 中响应视口变化
const mq = window.matchMedia('(min-width: 1024px)')

function handleChange(e) {
  // e.matches 表示当前是否命中
  console.log('桌面布局:', e.matches)
}

mq.addEventListener('change', handleChange)
handleChange(mq) // 初始化执行一次
```

讲解：`matchMedia` 返回 MediaQueryList，`change` 事件在命中状态变化时触发。注意使用 `addEventListener` 而非已废弃的 `addListener`，并清理监听避免泄漏。

### 4.8 响应式图片

```html
<!-- 根据视口宽度选择图片资源 -->
<img src="small.jpg"
     srcset="small.jpg 480w, medium.jpg 960w, large.jpg 1440w"
     sizes="(max-width: 640px) 100vw, 50vw"
     alt="响应式示例图片">
```

讲解：`srcset` 按资源宽度声明候选，`sizes` 告诉浏览器图片在布局中的实际宽度，浏览器综合视口、DPR 与带宽自动选择。这是媒体查询之外的响应式图片标准方案。

## 5. 对比分析

### 5.1 媒体查询与容器查询

| 维度 | 媒体查询 | 容器查询 |
| --- | --- | --- |
| 参照对象 | 视口 | 最近容器 |
| 粒度 | 页面级 | 组件级 |
| 前置条件 | 无 | 父元素 container-type |
| 适用 | 整体布局 | 复用组件 |

### 5.2 min-width 与 max-width 策略

移动优先（min-width）代码路径短、性能好、渐进增强；桌面优先（max-width）适合改造存量桌面站点。新项目推荐移动优先。

### 5.3 @media 与 @import media

`<link media="...">` 与 `@import url(...) media` 也能条件加载样式表，但会额外产生请求；`@media` 内联规则没有请求开销。性能敏感场景优先内联媒体查询。

## 6. 常见陷阱与最佳实践

陷阱一：缺少 viewport meta，移动端媒体查询失效。

陷阱二：断点基于固定设备（iPhone 宽度），设备碎片化导致维护失控。最佳实践：基于内容换行点选择断点。

陷阱三：`max-width: 767px` 与 `min-width: 768px` 间隙或重叠。使用范围语法或统一取整策略。

陷阱四：媒体查询嵌套在组件 scoped 样式中时，Vue/React 的 scoped 机制不影响媒体查询（媒体查询作用于全局视口），可放心使用。

陷阱五：深色模式只改背景不改图片/阴影，出现刺眼白色卡片。最佳实践：用 CSS 变量覆盖全部颜色令牌。

陷阱六：`prefers-reduced-motion: reduce` 下仍保留 `scroll-behavior: smooth`。应同时关闭平滑滚动。

陷阱七：媒体查询中写 `not (min-width: 768px)` 的非法组合。`not` 修饰整个查询，等价写法为 `@media not all and (min-width: 768px)`。

## 7. 工程实践

### 7.1 断点设计令牌

```css
:root {
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
}
```

讲解：断点值收敛为令牌，配合注释说明每个断点的内容动机（如“列表换两列”“导航收起为汉堡”），避免随意新增断点。

### 7.2 组合查询的组件化

```css
/* 桌面端且在浅色模式下：给卡片添加悬停投影 */
@media (min-width: 1024px) and (prefers-color-scheme: light) {
  .card:hover {
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  }
}
```

讲解：`and` 组合多个维度条件。组合越多越脆弱，建议每个查询只解决一个维度的适配。

## 8. 案例研究：文档站点完整响应式方案

需求：文档站桌面三栏（目录/正文/相关）、平板两栏、手机单栏，支持深色模式与减少动画。

```css
/* 移动优先基础：单栏 */
.layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
  padding: 16px;
}

/* 平板：正文 + 目录 */
@media (min-width: 768px) {
  .layout {
    grid-template-columns: 240px 1fr;
  }
}

/* 桌面：三栏 */
@media (min-width: 1280px) {
  .layout {
    grid-template-columns: 240px 1fr 220px;
  }
}

/* 深色模式变量覆盖 */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #16181d;
    --text: #e6e6e6;
    --border: #2d3138;
  }
}

/* 减少动画 */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

讲解：方案分层清晰：布局断点解决结构，色彩变量解决主题，动画偏好解决无障碍。每层独立演进，互不干扰。`animation-duration: 0.01ms` 的技巧让动画“瞬间完成”而非硬性禁用，避免依赖动画完成的逻辑挂起。

## 9. 知识要点总结与深入讲解

媒体查询的条件本质是“视口/环境特性谓词”，命中则参与层叠。移动优先的核心是把默认样式写成窄屏最优，再用 `min-width` 逐级增强。

用户偏好类媒体查询（深色、减少动画、对比度）是 CSS 与现代操作系统的桥梁，它们不是设备特性而是用户意图，理应获得更高优先级的设计关注。

容器查询与媒体查询的分工可以总结为：页面排版问视口，组件排版问容器。两者配合才能覆盖现代响应式设计的全部场景。

### 1. @media 语法

```css
@media screen and (min-width: 768px) {
  /* 样式 */
}
```

#### 媒体类型：`all`（默认）、`screen`、`print`、`speech`

#### 逻辑操作符：`and`、逗号（or）、`not`、`only`

### 1. 常用媒体特性

```css
@media (min-width: 768px) {
} /* 视口宽度 */
@media (orientation: portrait) {
} /* 竖屏 */
@media (prefers-color-scheme: dark) {
} /* 深色模式 */
@media (prefers-reduced-motion: reduce) {
} /* 减少动画 */
@media (hover: hover) {
} /* 支持悬停 */
@media (pointer: fine) {
} /* 精确指针 */
```

### 2. 响应式断点

```css
.container {
  padding: 1rem;
}
@media (min-width: 576px) {
  .container {
    padding: 1.5rem;
  }
}
@media (min-width: 768px) {
  .container {
    padding: 2rem;
  }
}
@media (min-width: 992px) {
  .container {
    max-width: 960px;
    margin: 0 auto;
  }
}
```

### 3. 深色模式

```css
:root {
  --bg: #fff;
  --text: #333;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --text: #e0e0e0;
  }
}
```

### 4. JavaScript 检测

```javascript
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
  console.log('深色模式:', e.matches);
});
```
### 基础语法

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

### 宽度查询

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

### 高度查询

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

### 方向查询

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

### 分辨率查询

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

### 逻辑操作符

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

### 用户偏好查询

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

### 设备特性查询

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

### 视口特性查询

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

### 媒体函数

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

### 媒体查询嵌套

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

### @import 媒体查询

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

### @supports 特性查询

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

### 断点规范

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

### 常见媒体查询模式

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

### 用户偏好媒体查询(2024)

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

## 动手试试

1. 写一个两栏布局，在 768px 断点以下变为单栏；
2. 用 `prefers-color-scheme: dark` 给页面加深色主题；
3. 用 `(min-width: 600px) and (max-width: 900px)` 测试区间命中；
4. 进阶挑战：用 `prefers-reduced-motion` 关闭动画。

## 核心知识点

> 一句话记住媒体查询：`@media (条件)` 按视口/系统偏好切换样式；断点用 min-width 移动优先，深色与减少动效都要考虑。

- 语法：`@media (min-width: 768px) { ... }`；
- 移动优先：基础样式给移动端，`min-width` 向上增强；
- 常用条件：`min-width`/`max-width`、`prefers-color-scheme`、`prefers-reduced-motion`、`orientation`；
- 多个条件用 `and`/`or`/`not` 组合；
- 断点跟着内容走，不跟设备走；
- 深色模式只需覆盖颜色变量。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 断点拍脑袋 | 内容断裂 | 按内容实际需要设断点 |
| 桌面优先 | 移动端体验差 | 移动优先 + min-width |
| 大量重复媒体查询 | 维护困难 | 用 CSS 变量与容器查询配合 |
| 忘记深色模式 | 夜间刺眼 | 颜色全部走变量并适配 |
| 忽略 reduced-motion | 动效扰民 | 媒体查询关闭动画 |

## 扩展学习

- 容器查询：`css/032-ContainerQuery`；
- 响应式设计：`css/033-ResponsiveDesign`；
- 移动适配：`css/052-MobileAdaptation`；
- 可访问性：`css/045-AccessibleStyling`。

<!-- ============ 文档分隔线：007-css/032-ContainerQuery.md ============ -->

> 前置依赖：先掌握 031 媒体查询。0基础速通：读第 0 节直觉与第 1 节核心必读即可；第 6 章深入理解（选读）供进阶。

# 容器查询（Container Queries）

> 本文以 W3C CSS Containment Module Level 3 与 Container Queries Level 3 规范为基础，系统阐释容器查询（Container Queries）的设计动机、语法体系、`container-type` 与 `container-name` 的语义、`@container` 规则的算法、style queries 的实验性能力，以及与媒体查询（Media Queries）的差异。内容对标 Bootstrap、Tailwind CSS、Material Design 等主流框架的响应式实践，提供生产级代码示例与工程化解决方案。

---

## 0. 直觉：让组件“看自己的容器”而不是屏幕

媒体查询（`@media`）根据**视口**宽度响应；容器查询（`@container`）根据**父容器**宽度响应。同一个卡片组件，放在窄栏里就变窄，放在宽栏里就变宽——组件真正做到了“自带响应式”。

三步用法：给容器加 `container-type: inline-size` 建立上下文，然后用 `@container (min-width: 400px)` 写条件样式，需要时用 `cqw` 等单位取容器尺寸。

## 1. 核心必读：代码示例
### 1.1 基础示例：响应式卡片

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>容器查询基础示例</title>
<style>
  /* CSS Containment Level 3 - 容器查询基础 */
  .card-container {
    container-type: inline-size;
    /* 等价于 container: inline-size */
  }

  /* 默认样式：窄容器下的垂直布局 */
  .card {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
  }

  /* 宽容器下的水平布局 */
  @container (min-width: 400px) {
    .card {
      flex-direction: row;
      align-items: center;
    }
    .card-media {
      flex: 0 0 120px;
    }
  }

  /* 更宽容器下的两行布局 */
  @container (min-width: 700px) {
    .card {
      padding: 2rem;
      gap: 2rem;
    }
    .card-title {
      font-size: 1.5rem;
    }
  }

  .card-media {
    height: 120px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 6px;
  }

  .card-body {
    flex: 1;
  }

  .card-title {
    margin: 0 0 0.5rem 0;
    font-size: 1.125rem;
  }

  .card-text {
    margin: 0;
    color: #6c757d;
  }
</style>
</head>
<body>
  <!-- 调整外层容器宽度可见卡片自动切换布局 -->
  <div style="width: 350px;">
    <div class="card-container">
      <article class="card">
        <div class="card-media"></div>
        <div class="card-body">
          <h3 class="card-title">卡片标题</h3>
          <p class="card-text">窄容器：垂直布局</p>
        </div>
      </article>
    </div>
  </div>

  <div style="width: 500px; margin-top: 20px;">
    <div class="card-container">
      <article class="card">
        <div class="card-media"></div>
        <div class="card-body">
          <h3 class="card-title">卡片标题</h3>
          <p class="card-text">宽容器：水平布局</p>
        </div>
      </article>
    </div>
  </div>
</body>
</html>
```

### 1.2 命名容器：嵌套场景

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>命名容器的嵌套查询</title>
<style>
  /* 外层容器命名为 sidebar */
  .sidebar {
    container-type: inline-size;
    container-name: sidebar;
  }

  /* 内层容器命名为 card */
  .card-wrapper {
    container-type: inline-size;
    container-name: card;
  }

  /* 根据 sidebar 宽度切换整体布局 */
  @container sidebar (min-width: 300px) {
    .widget {
      padding: 1.5rem;
    }
  }

  /* 根据 card 容器宽度切换卡片布局 */
  @container card (min-width: 250px) {
    .card {
      display: flex;
      gap: 1rem;
    }
  }

  /* 复合查询：两个容器都满足条件 */
  @container sidebar (min-width: 300px) and card (min-width: 250px) {
    .card {
      background: #e7f3ff;
    }
  }
</style>
</head>
<body>
  <aside class="sidebar">
    <div class="widget">
      <div class="card-wrapper">
        <article class="card">卡片内容</article>
      </div>
    </div>
  </aside>
</body>
</html>
```

### 1.3 `container-type: size`：查询高度

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>size 容器查询：根据高度切换布局</title>
<style>
  /* size 容器：可查询宽与高，但容器需显式高度 */
  .hero-container {
    container-type: size;
    width: 100%;
    height: 400px; /* 必须显式高度 */
    border: 2px solid #dee2e6;
  }

  .hero {
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 2rem;
  }

  /* 矮容器：紧凑布局 */
  @container (max-height: 200px) {
    .hero {
      flex-direction: row;
      padding: 1rem;
    }
    .hero-title {
      font-size: 1.25rem;
    }
  }

  /* 高容器：扩展布局 */
  @container (min-height: 300px) and (min-width: 600px) {
    .hero {
      padding: 4rem;
    }
    .hero-title {
      font-size: 3rem;
    }
  }

  .hero-title {
    margin: 0 0 1rem 0;
    font-size: 2rem;
  }

  .hero-subtitle {
    margin: 0;
    font-size: 1rem;
    opacity: 0.9;
  }
</style>
</head>
<body>
  <h3>矮容器（高度 150px）</h3>
  <div class="hero-container" style="height: 150px;">
    <div class="hero">
      <h2 class="hero-title">Hero 标题</h2>
      <p class="hero-subtitle">副标题</p>
    </div>
  </div>

  <h3>高容器（高度 400px）</h3>
  <div class="hero-container">
    <div class="hero">
      <h2 class="hero-title">Hero 标题</h2>
      <p class="hero-subtitle">副标题</p>
    </div>
  </div>
</body>
</html>
```

### 1.4 `cqi` 单位：响应式字体

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>cqi 单位：响应式字体</title>
<style>
  .responsive-text-container {
    container-type: inline-size;
    width: 100%;
  }

  .headline {
    /* 字体大小 = 容器宽度的 8% */
    font-size: 8cqi;
    line-height: 1.2;
    margin: 0;
    word-break: break-word;
  }

  .subhead {
    /* 副标题 = 容器宽度的 4% */
    font-size: 4cqi;
    color: #6c757d;
    margin: 1cqi 0 0 0;
  }

  /* 配合 clamp 限制范围 */
  .clamped-text {
    font-size: clamp(1rem, 5cqi, 3rem);
  }
</style>
</head>
<body>
  <div style="width: 600px;">
    <div class="responsive-text-container">
      <h1 class="headline">响应式标题</h1>
      <p class="subhead">副标题</p>
      <p class="clamped-text">限制范围的响应式文本</p>
    </div>
  </div>

  <div style="width: 300px; margin-top: 20px;">
    <div class="responsive-text-container">
      <h1 class="headline">响应式标题</h1>
      <p class="subhead">副标题</p>
      <p class="clamped-text">限制范围的响应式文本</p>
    </div>
  </div>
</body>
</html>
```

### 1.5 Style Queries：主题切换（实验性）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Style Queries：基于 CSS 变量切换主题</title>
<style>
  /* 实验性：截至 2024 年仅 Chrome 111+ 部分支持 */
  .theme-container {
    container-type: inline-size;
    --theme: light;
    --accent: #007bff;
  }

  .theme-container[data-theme="dark"] {
    --theme: dark;
    --accent: #4dabf7;
  }

  /* 默认浅色 */
  .card {
    background: #ffffff;
    color: #212529;
    border: 1px solid #dee2e6;
    padding: 1rem;
    border-radius: 8px;
  }

  /* 深色主题 */
  @container style(--theme: dark) {
    .card {
      background: #1a1a1a;
      color: #f8f9fa;
      border-color: #343a40;
    }
  }

  /* 根据强调色调整按钮 */
  @container style(--accent: #007bff) {
    .btn {
      background: #007bff;
    }
  }
  @container style(--accent: #4dabf7) {
    .btn {
      background: #4dabf7;
    }
  }

  .btn {
    display: inline-block;
    padding: 0.5rem 1rem;
    color: white;
    border: none;
    border-radius: 4px;
    margin-top: 0.5rem;
    cursor: pointer;
  }
</style>
</head>
<body>
  <div class="theme-container" data-theme="light">
    <div class="card">
      <h3>浅色主题卡片</h3>
      <p>主题由容器的 --theme 变量驱动</p>
      <button class="btn">按钮</button>
    </div>
  </div>

  <div class="theme-container" data-theme="dark" style="margin-top: 20px;">
    <div class="card">
      <h3>深色主题卡片</h3>
      <p>主题由容器的 --theme 变量驱动</p>
      <button class="btn">按钮</button>
    </div>
  </div>
</body>
</html>
```

### 1.6 企业级组件：可复用响应式卡片

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>企业级响应式卡片组件</title>
<style>
  :root {
    --color-primary: #667eea;
    --color-primary-dark: #764ba2;
    --color-text: #212529;
    --color-text-muted: #6c757d;
    --color-bg: #f8f9fa;
    --color-card: #ffffff;
    --radius-md: 8px;
    --radius-lg: 12px;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    padding: 2rem;
    background: var(--color-bg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: var(--color-text);
  }

  /* 容器查询包装器 */
  .responsive-card {
    container-type: inline-size;
    container-name: card;
  }

  /* 卡片基础样式 */
  .card {
    background: var(--color-card);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  /* 默认（窄容器）：垂直紧凑布局 */
  .card__media {
    width: 100%;
    height: 160px;
    background: linear-gradient(135deg, var(--color-primary), var(--color-primary-dark));
  }

  .card__body {
    padding: 1rem;
  }

  .card__title {
    margin: 0 0 0.5rem 0;
    font-size: 1rem;
    font-weight: 600;
  }

  .card__text {
    margin: 0 0 0.75rem 0;
    font-size: 0.875rem;
    color: var(--color-text-muted);
    line-height: 1.5;
  }

  .card__action {
    display: flex;
    gap: 0.5rem;
  }

  .btn {
    display: inline-block;
    padding: 0.5rem 0.875rem;
    font-size: 0.875rem;
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    text-decoration: none;
    transition: background 0.2s;
  }

  .btn--primary {
    background: var(--color-primary);
    color: white;
  }

  .btn--primary:hover {
    background: var(--color-primary-dark);
  }

  .btn--ghost {
    background: transparent;
    color: var(--color-primary);
    border: 1px solid var(--color-primary);
  }

  /* 中等容器（300px+）：水平布局 */
  @container card (min-width: 300px) {
    .card {
      flex-direction: row;
    }
    .card__media {
      flex: 0 0 140px;
      height: auto;
    }
    .card__body {
      padding: 1.25rem;
    }
    .card__title {
      font-size: 1.125rem;
    }
  }

  /* 大容器（500px+）：扩展布局 */
  @container card (min-width: 500px) {
    .card {
      box-shadow: var(--shadow-md);
    }
    .card__media {
      flex: 0 0 200px;
    }
    .card__body {
      padding: 2rem;
    }
    .card__title {
      font-size: 1.5rem;
      margin-bottom: 0.75rem;
    }
    .card__text {
      font-size: 1rem;
      margin-bottom: 1.5rem;
    }
  }

  /* 响应式字体：cqi 单位 */
  .card__title {
    font-size: clamp(1rem, 5cqi, 1.5rem);
  }
</style>
</head>
<body>
  <h2>同一组件在不同容器宽度下自动适配</h2>

  <h3>窄容器（240px）</h3>
  <div style="width: 240px;">
    <div class="responsive-card">
      <article class="card">
        <div class="card__media"></div>
        <div class="card__body">
          <h3 class="card__title">卡片标题</h3>
          <p class="card__text">这是卡片描述文字，会随容器宽度自动调整布局。</p>
          <div class="card__action">
            <a href="#" class="btn btn--primary">主操作</a>
            <a href="#" class="btn btn--ghost">次操作</a>
          </div>
        </div>
      </article>
    </div>
  </div>

  <h3>中等容器（400px）</h3>
  <div style="width: 400px;">
    <div class="responsive-card">
      <article class="card">
        <div class="card__media"></div>
        <div class="card__body">
          <h3 class="card__title">卡片标题</h3>
          <p class="card__text">这是卡片描述文字，会随容器宽度自动调整布局。</p>
          <div class="card__action">
            <a href="#" class="btn btn--primary">主操作</a>
            <a href="#" class="btn btn--ghost">次操作</a>
          </div>
        </div>
      </article>
    </div>
  </div>

  <h3>宽容器（600px）</h3>
  <div style="width: 600px;">
    <div class="responsive-card">
      <article class="card">
        <div class="card__media"></div>
        <div class="card__body">
          <h3 class="card__title">卡片标题</h3>
          <p class="card__text">这是卡片描述文字，会随容器宽度自动调整布局。</p>
          <div class="card__action">
            <a href="#" class="btn btn--primary">主操作</a>
            <a href="#" class="btn btn--ghost">次操作</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</body>
</html>
```

### 1.7 渐进增强：兼容旧浏览器

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>渐进增强：兼容不支持容器查询的浏览器</title>
<style>
  /* 1. 基础样式：所有浏览器可见 */
  .card {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
  }

  /* 2. 媒体查询兜底：旧浏览器使用视口查询 */
  @media (min-width: 768px) {
    .card {
      flex-direction: row;
    }
  }

  /* 3. 容器查询：现代浏览器覆盖媒体查询 */
  @supports (container-type: inline-size) {
    .card-container {
      container-type: inline-size;
    }
    @container (min-width: 400px) {
      .card {
        flex-direction: row;
      }
    }
  }
</style>
</head>
<body>
  <div class="card-container">
    <article class="card">
      <div>媒体</div>
      <div>内容</div>
    </article>
  </div>
</body>
</html>
```

### 1.8 React 组件示例

```jsx
// ResponsiveCard.jsx
import React from 'react';
import './ResponsiveCard.css';

export default function ResponsiveCard({ title, text, image }) {
  return (
    <div className="responsive-card">
      <article className="card">
        <div className="card__media" style={{ backgroundImage: `url(${image})` }} />
        <div className="card__body">
          <h3 className="card__title">{title}</h3>
          <p className="card__text">{text}</p>
        </div>
      </article>
    </div>
  );
}

// ResponsiveCard.css
.responsive-card {
  container-type: inline-size;
}

.card {
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
}

.card__media {
  height: 160px;
  background-size: cover;
  background-position: center;
}

.card__body {
  padding: 1rem;
}

@container (min-width: 400px) {
  .card {
    flex-direction: row;
  }
  .card__media {
    flex: 0 0 140px;
    height: auto;
  }
}
```

### 1.9 Vue 组件示例

```vue
<!-- ResponsiveCard.vue -->
<template>
  <div class="responsive-card">
    <article class="card">
      <div class="card__media" :style="{ backgroundImage: `url(${image})` }"></div>
      <div class="card__body">
        <h3 class="card__title">{{ title }}</h3>
        <p class="card__text">{{ text }}</p>
      </div>
    </article>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  text: String,
  image: String,
});
</script>

<style scoped>
.responsive-card {
  container-type: inline-size;
}

.card {
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
}

.card__media {
  height: 160px;
  background-size: cover;
  background-position: center;
}

.card__body {
  padding: 1rem;
}

@container (min-width: 400px) {
  .card {
    flex-direction: row;
  }
  .card__media {
    flex: 0 0 140px;
    height: auto;
  }
}
</style>
```

### 1.10 调试技巧：DevTools 可视化

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>容器查询调试</title>
<style>
  /* Chrome DevTools 105+ 支持 @container 标记 */
  .debug-container {
    container-type: inline-size;
    /* DevTools 会在元素旁显示 @container 标签 */
    outline: 2px dashed #007bff;
    padding: 0.5rem;
  }

  .debug-container::before {
    content: '@container';
    display: block;
    font-size: 0.75rem;
    color: #007bff;
    margin-bottom: 0.5rem;
  }
</style>
</head>
<body>
  <div class="debug-container">
    <p>调试内容</p>
  </div>
</body>
</html>
```

---

## 2. 对比分析
### 2.1 容器查询 vs 媒体查询

| 维度 | 媒体查询 `@media` | 容器查询 `@container` |
| --- | --- | --- |
| 参照物 | 视口（viewport） | 父容器（container） |
| 组件独立性 | 差（依赖视口） | 优（组件自包含） |
| 复用性 | 低（需根据视口重写） | 高（组件即适配） |
| SSR 友好 | 优（视口已知） | 差（容器尺寸未知） |
| 浏览器支持 | 全部 | Chrome 105+、Safari 16+、Firefox 110+ |
| 单位 | `vw`、`vh`、`vi`、`vb` | `cqw`、`cqh`、`cqi`、`cqb` |
| 嵌套查询 | 不支持 | 支持（`container-name`） |
| 主题切换 | `prefers-color-scheme` | `style(--var)`（实验） |

### 2.2 容器查询 vs ResizeObserver

| 维度 | 容器查询 `@container` | ResizeObserver（JS） |
| --- | --- | --- |
| 实现方式 | 纯 CSS | JavaScript |
| 性能 | 浏览器优化 | 可能引起 reflow |
| 同步性 | 与渲染管线同步 | 异步回调 |
| 复杂条件 | 支持组合查询 | 需手动逻辑 |
| 学习成本 | 低（CSS 语法） | 中（JS API） |
| 兼容性 | 现代浏览器 | 现代浏览器 |
| SSR | 不友好 | 不友好 |
| 推荐 | 布局适配 | 复杂逻辑场景 |

### 2.3 容器查询 vs CSS 变量驱动

| 维度 | 容器查询 | CSS 变量（props 传递） |
| --- | --- | --- |
| 数据流 | 自动（基于布局） | 显式（props 传递） |
| 灵活性 | 仅尺寸/样式 | 任意值 |
| SSR | 不友好 | 友好（服务端可计算） |
| 学习成本 | 低 | 中（需要 props 设计） |
| 适用场景 | 视觉适配 | 业务逻辑切换 |

### 2.4 容器查询与 Tailwind CSS

Tailwind CSS v3.4+ 支持容器查询插件：

```html
<!-- Tailwind CSS v3.4 容器查询插件 -->
<div class="@container">
  <div class="flex flex-col @md:flex-row">
    <div class="@md:w-1/3">媒体</div>
    <div class="@md:w-2/3">内容</div>
  </div>
</div>
```

配置：

```javascript
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/container-queries'),
  ],
};
```

### 2.5 容器查询与 Bootstrap

Bootstrap 5.3+ 开始在部分组件中使用容器查询：

```scss
// Bootstrap 5.3 源码示例
.card {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card-body {
    padding: 1.5rem;
  }
}
```

### 2.6 容器查询与 Material Design

Material Design 3 在组件库 MDC Web 中引入容器查询：

```css
/* Material Design 3 风格 */
.md-card {
  container-type: inline-size;
}

@container (min-width: 360px) {
  .md-card__primary {
    padding: 16px;
  }
}

@container (min-width: 600px) {
  .md-card__primary {
    padding: 24px;
  }
}
```

---

## 3. 常见陷阱与最佳实践
### 3.1 陷阱 1：`container-type: size` 导致高度塌陷

**问题代码**：

```css
.card-container {
  container-type: size;
  /* 未设置高度，导致容器高度为 0 */
}
.card-container .card {
  height: 200px;
}
```

**问题**：`container-type: size` 隐式触发 `contain: size`，使容器高度不再被子元素撑开，导致高度为 0。

**解决方案**：

```css
/* 方案 1：使用 inline-size（推荐） */
.card-container {
  container-type: inline-size;
}

/* 方案 2：显式设置高度 */
.card-container {
  container-type: size;
  height: 400px;
}
```

### 3.2 陷阱 2：忘记声明 `container-type`

**问题代码**：

```css
.card-wrapper {
  /* 忘记写 container-type */
}

@container (min-width: 400px) {
  .card { /* 永不匹配！ */ }
}
```

**解决方案**：

```css
.card-wrapper {
  container-type: inline-size;
  /* 或简写：container: inline-size */
}
```

### 3.3 陷阱 3：SSR 场景下的布局抖动

**问题**：服务端渲染时，容器尺寸未知，`@container` 规则无法预先评估。客户端 hydration 后，容器尺寸变化可能导致布局抖动（CLS）。

**解决方案**：

```html
<!-- 1. 提供默认样式（不依赖容器） -->
<style>
  .card {
    display: flex;
    flex-direction: column;
  }
</style>

<!-- 2. 客户端 hydration 后再应用容器查询 -->
<style>
  @supports (container-type: inline-size) {
    .card-container {
      container-type: inline-size;
    }
    @container (min-width: 400px) {
      .card {
        flex-direction: row;
      }
    }
  }
</style>
```

### 3.4 陷阱 4：`@container` 与 `@media` 混淆

**错误代码**：

```css
/* 错误：@container 中使用视口单位 */
@container (min-width: 100vw) {
  .card { /* 永不匹配！ */ }
}

/* 错误：@media 中使用容器单位 */
@media (min-width: 100cqw) {
  .card { /* 永不匹配！ */ }
}
```

**正确用法**：

```css
/* @container 使用容器尺寸 */
@container (min-width: 400px) {
  .card { /* ... */ }
}

/* @media 使用视口尺寸 */
@media (min-width: 768px) {
  .card { /* ... */ }
}
```

### 3.5 陷阱 5：嵌套容器未命名

**问题代码**：

```css
.outer { container-type: inline-size; }
.inner { container-type: inline-size; }

@container (min-width: 800px) {
  .card { /* 匹配 .inner（最近的），而非 .outer */ }
}
```

**解决方案**：

```css
.outer {
  container-type: inline-size;
  container-name: outer;
}
.inner {
  container-type: inline-size;
  container-name: inner;
}

@container outer (min-width: 800px) {
  .card { /* 精确匹配 .outer */ }
}
```

### 3.6 最佳实践清单

1. **优先使用 `inline-size`**：除非需要查询高度，否则使用 `inline-size` 而非 `size`。
2. **为嵌套容器命名**：使用 `container-name` 避免歧义。
3. **提供默认样式**：在 `@container` 规则外提供基础样式，兼容旧浏览器。
4. **配合 `@supports`**：使用特性查询渐进增强。
5. **使用 `cqi` 单位**：响应式字体优先用 `cqi` 而非 `vw`。
6. **避免 `size` 容器内子元素撑高**：`size` 容器必须显式高度。
7. **SSR 谨慎使用**：容器查询在 SSR 下不友好，需配合 hydration 策略。
8. **测试 CLS**：使用 Lighthouse 检查容器查询导致的布局抖动。
9. **Storybook 测试**：在各种容器尺寸下进行视觉回归。
10. **文档化容器边界**：在组件文档中说明容器查询的断点。

### 3.7 兼容性参考

| 特性 | Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- | --- |
| `container-type` | 105+ | 110+ | 16+ | 105+ |
| `container-name` | 105+ | 110+ | 16+ | 105+ |
| `@container` 尺寸查询 | 105+ | 110+ | 16+ | 105+ |
| `cqw` / `cqi` 单位 | 105+ | 110+ | 16+ | 105+ |
| `container-name` 命名 | 105+ | 110+ | 16+ | 105+ |
| Style Queries `style()` | 111+（部分） | 不支持 | 不支持 | 111+（部分） |
| Tailwind `@container` 插件 | 需 v3.4+ | 需 v3.4+ | 需 v3.4+ | 需 v3.4+ |

---

## 4. 工程实践
### 4.1 PostCSS 容器查询 polyfill

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('postcss-preset-env')({
      stage: 2,
      features: {
        'container-queries': true,
      },
    }),
  ],
};
```

### 4.2 设计令牌：容器断点系统

```css
:root {
  /* 容器断点 */
  --container-sm: 240px;
  --container-md: 400px;
  --container-lg: 600px;
  --container-xl: 800px;
}

.card-container {
  container-type: inline-size;
}

@container (min-width: var(--container-md)) {
  .card {
    /* ... */
  }
}
```

### 4.3 SCSS 工具 mixin

```scss
// _container-queries.scss
@mixin container($name: none) {
  container-type: inline-size;
  @if $name != none {
    container-name: $name;
  }
}

@mixin cq($condition, $name: null) {
  @if $name {
    @container #{$name} #{$condition} {
      @content;
    }
  } @else {
    @container #{$condition} {
      @content;
    }
  }
}

// 使用
.card-wrapper {
  @include container(card);
}

.card {
  display: flex;
  flex-direction: column;

  @include cq('(min-width: 400px)', card) {
    flex-direction: row;
  }
}
```

### 4.4 Tailwind 配置

```javascript
// tailwind.config.js
module.exports = {
  plugins: [
    require('@tailwindcss/container-queries'),
  ],
  theme: {
    extend: {
      containers: {
        sm: '240px',
        md: '400px',
        lg: '600px',
      },
    },
  },
};
```

### 4.5 性能优化

1. **避免 `size` 容器**：除非必须，使用 `inline-size` 减少布局开销。
2. **限制容器数量**：每个 `container-type` 都会创建独立的布局上下文，过多会降低性能。
3. **使用 `contain` 优化**：在不需查询的容器上使用 `contain: layout` 提升性能。
4. **避免深嵌套**：嵌套容器会增加布局复杂度。
5. **CSS Containment**：使用 `contain: layout paint` 隔离组件。

```css
.component {
  contain: layout paint; /* 隔离布局与绘制 */
}
```

### 4.6 调试工具

1. **Chrome DevTools 105+**：在 Elements 面板显示 `@container` 标记。
2. **Firefox DevTools**：盒模型可视化中显示容器边界。
3. **Safari Web Inspector**：CSS 编辑器支持 `@container` 语法高亮。
4. **VS Code 插件**：CSS Language Service 支持 `@container` 智能补全。

### 4.7 自动化测试

```javascript
// container-queries.test.js
const { test, expect } = require('@playwright/test');

test('卡片在窄容器下垂直布局', async ({ page }) => {
  await page.goto('http://localhost:3000/card');
  await page.setViewportSize({ width: 800, height: 600 });

  // 设置容器宽度为 300px
  await page.locator('.card-container').evaluate((el) => {
    el.style.width = '300px';
  });

  const card = await page.locator('.card').first();
  const flexDirection = await card.evaluate(
    (el) => getComputedStyle(el).flexDirection
  );

  expect(flexDirection).toBe('column');
});

test('卡片在宽容器下水平布局', async ({ page }) => {
  await page.goto('http://localhost:3000/card');

  await page.locator('.card-container').evaluate((el) => {
    el.style.width = '500px';
  });

  const card = await page.locator('.card').first();
  const flexDirection = await card.evaluate(
    (el) => getComputedStyle(el).flexDirection
  );

  expect(flexDirection).toBe('row');
});
```

### 4.8 ESLint 规则（CSS-in-JS）

```javascript
// .stylelintrc.js
module.exports = {
  rules: {
    'at-rule-no-unknown': [
      true,
      {
        ignoreAtRules: ['container', 'media', 'supports'],
      },
    ],
    'custom-property-pattern': '^--[a-z][a-z0-9-]*$',
  },
};
```

---

## 5. 案例研究
### 5.1 案例一：Bootstrap 5.3 的容器查询实践

Bootstrap 5.3 在部分组件中引入容器查询，例如卡片组件：

```scss
// bootstrap/scss/_card.scss
.card {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card-body {
    padding: 1.5rem;
  }
  .card-title {
    font-size: 1.25rem;
  }
}
```

**分析**：
- Bootstrap 5.3 仍以媒体查询为主，容器查询为辅。
- 通过容器查询，卡片组件在不同栅格列中表现一致。

### 5.2 案例二：Tailwind CSS 的 `@container` 插件

Tailwind v3.4 提供 `@tailwindcss/container-queries` 插件：

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row">
    <div class="@md:w-1/3">媒体</div>
    <div class="@md:w-2/3">内容</div>
  </div>
</div>
```

生成的 CSS：

```css
.\@container {
  container-type: inline-size;
}
@\container (min-width: 28rem) {
  .\@md\:flex-row {
    flex-direction: row;
  }
}
```

**分析**：
- 使用 `@` 前缀避免与媒体查询 `md:` 冲突。
- 断点（`@sm`、`@md`、`@lg`）与媒体查询断点一致。

### 5.3 案例三：Material Design 3 的容器查询

Material Design 3 在 MDC Web 中使用容器查询：

```css
/* MDC Card */
.mdc-card {
  container-type: inline-size;
}

@container (min-width: 360px) {
  .mdc-card__primary {
    padding: 16px;
  }
}

@container (min-width: 600px) {
  .mdc-card__primary {
    padding: 24px;
  }
}
```

**分析**：
- 遵循 Material Design 的 8dp 网格。
- 卡片在 Drawer、Modal、Full-screen 三种容器中表现一致。

### 5.4 案例四：GitHub Primer 的容器查询

GitHub Primer 在部分组件中使用容器查询：

```css
.primer-card {
  container-type: inline-size;
}

@container (min-width: 360px) {
  .primer-card__body {
    padding: 16px;
  }
}
```

### 5.5 案例五：Ant Design 的容器查询

Ant Design v5 部分组件支持容器查询：

```css
.ant-card {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .ant-card-body {
    padding: 24px;
  }
}
```

### 5.6 案例六：真实生产实践

**场景**：某新闻网站的文章卡片，可能出现在侧栏（240px）、主内容区（640px）、全屏 Modal（1200px）三种场景。

**传统方案**：

```jsx
// 需要根据父组件传递 variant prop
<Card variant="sidebar" />     // 240px
<Card variant="main" />        // 640px
<Card variant="modal" />       // 1200px
```

**容器查询方案**：

```jsx
// 同一组件，自适应容器
<Card />
```

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 200px) and (max-width: 400px) {
  .card { /* sidebar 样式 */ }
}
@container (min-width: 400px) and (max-width: 800px) {
  .card { /* main 样式 */ }
}
@container (min-width: 800px) {
  .card { /* modal 样式 */ }
}
```

**收益**：
- 组件复用性大幅提升。
- 无需为每个场景编写不同组件。
- 维护成本降低 60%。

---

### 填空题知识点讲解

**题目 1**：容器查询的规范属于 CSS ________ Module Level 3。

**解析讲解**：Containment

**解析讲解**：容器查询规范归入 [CSS Containment Module Level 3](https://www.w3.org/TR/css-contain-3/)。

**题目 2**：声明 `container-type: size` 会隐式触发 `contain: ________`。

**解析讲解**：`size`

**解析讲解**：`container-type: size` 隐式触发 `contain: size`，使容器尺寸不受子元素影响，从而打破循环依赖。

**题目 3**：`cqi` 单位的全称是 ________。

**解析讲解**：container query inline

**解析讲解**：`cqi` 全称为 container query inline，是容器 inline 方向尺寸的 1%。

**题目 4**：容器查询的命名属性是 ________。

**解析讲解**：`container-name`

**解析讲解**：`container-name` 属性为容器命名，用于在嵌套场景下精确匹配 `@container` 规则。

**题目 5**：Style Queries 使用 `________()` 函数查询容器的 CSS 变量。

**解析讲解**：`style`

**解析讲解**：Style Queries 使用 `style()` 函数查询容器的 CSS 变量，例如 `@container style(--theme: dark)`。

### 编程题知识点讲解

**题目 1**：实现一个响应式导航栏组件，要求：

1. 窄容器（< 400px）：垂直堆叠，菜单折叠为汉堡按钮。
2. 中等容器（400-700px）：水平排列，菜单展开。
3. 宽容器（> 700px）：水平排列，菜单展开并显示搜索框。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>响应式导航栏</title>
<style>
  .nav-container {
    container-type: inline-size;
    container-name: nav;
    background: #1a1a1a;
    padding: 1rem;
  }

  .nav {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .nav__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .nav__brand {
    color: white;
    font-size: 1.25rem;
    font-weight: bold;
  }

  .nav__toggle {
    display: block;
    background: transparent;
    border: none;
    color: white;
    font-size: 1.5rem;
    cursor: pointer;
  }

  .nav__menu {
    display: none;
    flex-direction: column;
    gap: 0.5rem;
  }

  .nav__menu a {
    color: white;
    text-decoration: none;
    padding: 0.5rem;
    border-radius: 4px;
  }

  .nav__menu a:hover {
    background: rgba(255, 255, 255, 0.1);
  }

  .nav__search {
    display: none;
  }

  /* 中等容器：水平布局 */
  @container nav (min-width: 400px) {
    .nav {
      flex-direction: row;
      align-items: center;
      gap: 2rem;
    }
    .nav__toggle {
      display: none;
    }
    .nav__menu {
      display: flex;
      flex-direction: row;
      gap: 1rem;
    }
  }

  /* 宽容器：显示搜索框 */
  @container nav (min-width: 700px) {
    .nav__search {
      display: block;
      margin-left: auto;
    }
    .nav__search input {
      padding: 0.5rem 1rem;
      border-radius: 20px;
      border: none;
      background: rgba(255, 255, 255, 0.1);
      color: white;
      width: 200px;
    }
  }
</style>
</head>
<body>
  <div class="nav-container" style="width: 300px;">
    <nav class="nav">
      <div class="nav__header">
        <div class="nav__brand">Brand</div>
        <button class="nav__toggle">菜单</button>
      </div>
      <div class="nav__menu">
        <a href="#">首页</a>
        <a href="#">产品</a>
        <a href="#">关于</a>
      </div>
      <div class="nav__search">
        <input type="search" placeholder="搜索...">
      </div>
    </nav>
  </div>

  <div class="nav-container" style="width: 500px; margin-top: 20px;">
    <nav class="nav">
      <div class="nav__header">
        <div class="nav__brand">Brand</div>
        <button class="nav__toggle">菜单</button>
      </div>
      <div class="nav__menu">
        <a href="#">首页</a>
        <a href="#">产品</a>
        <a href="#">关于</a>
      </div>
      <div class="nav__search">
        <input type="search" placeholder="搜索...">
      </div>
    </nav>
  </div>

  <div class="nav-container" style="width: 800px; margin-top: 20px;">
    <nav class="nav">
      <div class="nav__header">
        <div class="nav__brand">Brand</div>
        <button class="nav__toggle">菜单</button>
      </div>
      <div class="nav__menu">
        <a href="#">首页</a>
        <a href="#">产品</a>
        <a href="#">关于</a>
      </div>
      <div class="nav__search">
        <input type="search" placeholder="搜索...">
      </div>
    </nav>
  </div>
</body>
</html>
```

**评分要点**：
- 使用 `container-type: inline-size`（+10 分）
- 使用 `container-name` 命名（+5 分）
- 三个断点的样式切换（+10 分）
- 默认样式（窄容器）正确（+5 分）

**题目 2**：修复以下代码中的错误：

```css
.card-container {
  container-type: size;
}
.card-container .card {
  height: 200px;
}
@container (min-height: 300px) {
  .card-container .card {
    height: 400px;
  }
}
```

**问题**：`container-type: size` 触发 `contain: size`，但容器未显式设置高度，导致容器高度为 0，`@container (min-height: 300px)` 永不匹配。

**解决方案**：

```css
.card-container {
  container-type: size;
  height: 500px; /* 显式设置高度 */
}
.card-container .card {
  height: 200px;
}
@container (min-height: 300px) {
  .card-container .card {
    height: 400px;
  }
}
```

或者改用 `inline-size`（仅查询宽度）：

```css
.card-container {
  container-type: inline-size;
  /* 高度仍可被子元素撑开 */
}
.card-container .card {
  height: 200px;
}
@container (min-width: 400px) {
  .card-container .card {
    height: 400px;
  }
}
```

**题目 3**：使用容器查询实现一个响应式图片网格：

1. 窄容器（< 400px）：单列。
2. 中等容器（400-700px）：双列。
3. 宽容器（> 700px）：三列。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>响应式图片网格</title>
<style>
  .grid-container {
    container-type: inline-size;
    container-name: grid;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .grid__item {
    aspect-ratio: 1;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 8px;
  }

  @container grid (min-width: 400px) {
    .grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @container grid (min-width: 700px) {
    .grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }
</style>
</head>
<body>
  <div class="grid-container" style="width: 300px;">
    <div class="grid">
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
    </div>
  </div>

  <div class="grid-container" style="width: 500px; margin-top: 20px;">
    <div class="grid">
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
    </div>
  </div>

  <div class="grid-container" style="width: 800px; margin-top: 20px;">
    <div class="grid">
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
      <div class="grid__item"></div>
    </div>
  </div>
</body>
</html>
```

### 10.1 W3C 规范

[1] Miriam Suzanne and Tab Atkins Jr. 2024. *CSS Containment Module Level 3*. W3C Working Draft. Retrieved from https://www.w3.org/TR/css-contain-3/

[2] Tab Atkins Jr., Elika Etemad, and Florian Rivoal. 2022. *CSS Containment Module Level 1*. W3C Recommendation. Retrieved from https://www.w3.org/TR/css-contain-1/

[3] Miriam Suzanne. 2023. *Container Queries Level 3*. W3C Working Draft. Retrieved from https://drafts.csswg.org/css-contain-3/

[4] Florian Rivoal. 2022. *CSS Conditional Rules Module Level 3*. W3C Candidate Recommendation. Retrieved from https://www.w3.org/TR/css-conditional-3/

### 10.2 学术论文与文章

[5] Suzanne, M. 2021. *Container Queries: A Quick Start Guide*. CSS-Tricks. Retrieved from https://css-tricks.com/container-queries-a-quick-start-guide/

[6] Atkins, T. 2021. *CSS Containment Level 3: Container Queries*. W3C Editor's Draft. Retrieved from https://drafts.csswg.org/css-contain-3/

[7] Verou, L. 2022. *CSS Variables and Container Queries*. Smashing Magazine. Retrieved from https://www.smashingmagazine.com/2022/css-variables-container-queries/

### 10.4 框架文档

[12] Tailwind Labs. 2024. *Tailwind CSS Container Queries Plugin*. Retrieved from https://github.com/tailwindlabs/tailwindcss-container-queries

[13] Bootstrap Team. 2024. *Bootstrap 5.3 Container Queries*. Retrieved from https://getbootstrap.com/docs/5.3/layout/css-grid/

[14] Google. 2024. *Material Design 3 Container Queries*. Retrieved from https://m3.material.io/foundations/layout/applying-layout/window-size-classes

### 10.5 引用规范

本文引用遵循 ACM Reference Format：

> Author(s). Year. *Title*. Publisher/Venue. DOI or URL.

示例：
> Suzanne, M. and Atkins, T. Jr. 2024. CSS Containment Module Level 3. W3C Working Draft. Retrieved from https://www.w3.org/TR/css-contain-3/

---

### 11.1 书籍

1. **《CSS in Depth》** — Keith J. Grant 著
   - 第 2 版深入讲解容器查询与现代 CSS。

2. **《CSS Secrets》** — Lea Verou 著
   - CSS 高级技巧，包含布局与响应式。

3. **《Every Layout》** — Heydon Pickering 与 Andy Bell 著
   - 重新思考布局模式，包含容器查询实践。

4. **《Modern CSS》** — Joe Liang 著
   - 现代 CSS 实战指南，覆盖容器查询、CSS 变量等。

### 11.2 论文与文章

1. **Miriam Suzanne. 2021. *Container Queries: The End of Responsive Design as We Know It*. A List Apart.**
   - 容器查询的设计动机与未来。

2. **Una Kravets. 2022. *Container Queries are Actually Coming*. CSS-Tricks.**
   - 容器查询的实战指南。

3. **Bramus. 2022. *Container Queries in Chrome 105*. web.dev.**
   - Chrome 实现细节与性能分析。

### 11.4 视频课程

1. **Frontend Masters: CSS Container Queries** — Una Kravets
   - 容器查询深度课程。

2. **Container Queries: From Zero to Hero** — Kevin Powell
   - YouTube 上的容器查询实战教程。

3. **CSS for JavaScript Developers** — Josh W. Comeau
   - 包含容器查询章节。

### 11.5 工具与资源

1. **PostCSS Container Queries** — https://github.com/postcss/postcss-preset-env
   - PostCSS 插件，提供容器查询 polyfill。

2. **@tailwindcss/container-queries** — https://github.com/tailwindlabs/tailwindcss-container-queries
   - Tailwind 容器查询插件。

3. **Storybook** — https://storybook.js.org/
   - 组件开发工具，便于测试容器查询。

4. **Chromatic** — https://www.chromatic.com/
   - 视觉回归测试服务。

5. **Playwright** — https://playwright.dev/
   - 端到端测试框架，支持容器尺寸模拟。

---

## 6. 深入理解（选读）

> 以下内容适合想彻底搞懂机制原理的读者，第一遍学习可跳过。

### 6.1 历史演进

### 6.1.1 媒体查询的局限（2010s）

CSS Media Queries 在 2012 年随 CSS3 引入，让 Web 设计进入响应式时代。开发者通过 `@media (min-width: 768px)` 等条件针对视口尺寸适配。然而，组件化时代的到来暴露了媒体查询的根本缺陷：

```html
<!-- 一个卡片组件可能出现在侧栏（200px 宽）或主内容区（800px 宽） -->
<aside class="sidebar">
  <Card /> <!-- 在 200px 容器内仍按视口（如 1440px）的样式渲染 -->
</aside>
<main class="content">
  <Card /> <!-- 在 800px 容器内 -->
</main>
```

问题：卡片组件无法感知自身容器的实际宽度，只能依赖父级传递 props 或 JS 监听 ResizeObserver。这种「视口驱动」的响应式与「组件驱动」的设计系统存在根本矛盾。

### 6.1.2 早期尝试：Element Query（2013-2017）

社区曾提出「Element Queries」构想：

```css
/* 假想语法，从未标准化 */
.card(min-width: 400px) {
  display: flex;
}
```

但元素查询存在循环依赖问题：若元素 A 的样式依赖于自身的宽度，而样式又影响宽度，将导致无限循环。例如：

```css
/* 循环依赖示例 */
.box(min-width: 200px) {
  width: 100px; /* 改变自身宽度，触发条件失效，再变回... */
}
```

W3C 长期拒绝将元素查询纳入规范，正是因为此问题。

### 6.1.3 CSS Containment 的引入（2016）

[CSS Containment Module Level 1](https://www.w3.org/TR/css-contain-1/) 引入了 `contain` 属性，允许浏览器隔离元素的渲染，提升性能：

```css
.component {
  contain: layout paint size; /* 隔离布局、绘制与尺寸 */
}
```

`contain: size` 的关键意义：明确告知浏览器「该元素的尺寸不受子元素影响」，从而打破元素查询的循环依赖。这为容器查询奠定了基础。

### 6.1.4 Container Queries Level 3（2021-2023）

2021 年，Miriam Suzanne 与 Tab Atkins 在 [CSS Containment Module Level 3](https://www.w3.org/TR/css-contain-3/) 中正式提出容器查询规范：

- `container-type` 属性：声明元素为查询容器。
- `container-name` 属性：为容器命名，支持多层嵌套时的精确匹配。
- `@container` 规则：根据容器条件应用样式。
- `cqw`、`cqh`、`cqi`、`cqb`、`cqmin`、`cqmax` 单位：相对于容器尺寸的长度单位。

2022 年 8 月，Chrome 105、Safari 16、Firefox 110 相继实现容器查询，正式进入生产可用阶段。

### 6.1.5 Style Queries 的实验（2023+）

容器查询的下一阶段是「样式查询」（Style Queries），允许根据容器的 CSS 变量或计算样式应用规则：

```css
@container style(--theme: dark) {
  .card {
    background: #1a1a1a;
  }
}
```

截至 2024 年，Chrome 111+ 部分支持，Safari 与 Firefox 仍在实现中。

### 6.1.6 演进时间线

| 年份 | 事件 | 核心变化 |
| --- | --- | --- |
| 2012 | CSS Media Queries Level 3 推荐 | 视口驱动响应式 |
| 2013 | 社区提出 Element Query | 因循环依赖被否决 |
| 2016 | CSS Containment Level 1 | 引入 `contain` 属性 |
| 2019 | Miriam Suzanne 提议 Container Query | 基于 containment 解决循环 |
| 2021 | CSS Containment Level 3 草案 | `container-type`、`@container` 规范化 |
| 2022.8 | Chrome 105 / Safari 16 实现 | 容器查询进入生产可用 |
| 2023 | Style Queries 实验 | `style(--var: val)` 查询 |
| 2024 | 容器查询单位普及 | `cqi` 单位被广泛使用 |

---

### 6.2 形式化定义

### 6.2.1 规范条款

依据 [CSS Containment Module Level 3 §3](https://www.w3.org/TR/css-contain-3/#container-queries)：

> A container query allows styling of elements based on the size of a container element rather than the viewport.

### 6.2.2 核心属性

| 属性 | 取值 | 默认 | 说明 |
| --- | --- | --- | --- |
| `container-type` | `normal` \| `inline-size` \| `size` | `normal` | 声明容器类型 |
| `container-name` | `<custom-ident>+` \| `none` | `none` | 容器命名 |
| `container` | `<container-type>` \|\| `<container-name>` | - | 简写属性 |

### 6.2.3 `@container` 规则语法

```
@container [ <container-name> ]? <container-condition> {
  <stylesheet>
}
```

其中 `<container-condition>` 支持以下查询：

- 尺寸查询：`(min-width: 400px)`、`(max-width: 800px)`、`(orientation: landscape)`
- 复合查询：`(min-width: 400px) and (max-width: 800px)`、`not (min-width: 400px)`
- 样式查询（实验）：`style(--theme: dark)`、`style(--accent-color: blue)`

### 6.2.4 容器查询单位

| 单位 | 含义 | 对应视口单位 |
| --- | --- | --- |
| `cqw` | 容器宽度的 1% | `vw` |
| `cqh` | 容器高度的 1% | `vh` |
| `cqi` | 容器 inline 方向的 1% | `vi` |
| `cqb` | 容器 block 方向的 1% | `vb` |
| `cqmin` | `cqi` 与 `cqb` 中较小者 | `vmin` |
| `cqmax` | `cqi` 与 `cqb` 中较大者 | `vmax` |

### 6.2.5 形式化定义

设容器 $C$ 的 `container-type` 为 $T \in \{\text{normal}, \text{inline-size}, \text{size}\}$，则：

- 若 $T = \text{normal}$：$C$ 不是查询容器，`@container` 规则不匹配。
- 若 $T = \text{inline-size}$：$C$ 是 inline-size 容器，可查询 `width`、`inline-size`、`aspect-ratio`。
- 若 $T = \text{size}$：$C$ 是 size 容器，可查询 `width`、`height`、`inline-size`、`block-size`、`aspect-ratio`、`orientation`。

`@container` 规则的匹配函数：

$$
\text{Match}(@container, E) =
\begin{cases}
\text{true}, & \text{if } \exists C \in \text{Ancestors}(E) \text{ s.t. } \\
& \quad \text{Type}(C) \neq \text{normal} \\
& \quad \wedge \text{Name}(C) = \text{Name}(@container) \\
& \quad \wedge \text{Condition}(@container, C) = \text{true} \\
\text{false}, & \text{otherwise}
\end{cases}
$$

其中 `Ancestors(E)` 是元素 E 的祖先链中最近的匹配容器。

### 6.2.6 循环依赖的解决

CSS Containment Level 3 通过 `contain: size`（由 `container-type: size` 隐式触发）解决循环依赖：

- 容器的尺寸被声明为「与子元素无关」，浏览器先布局容器，再应用 `@container` 规则。
- 子元素的样式变化不会回流影响容器尺寸，从而打破循环。

形式化地：

$$
\text{Layout}(C) \to \text{Evaluate}(@container, C) \to \text{Layout}(\text{Children}(C))
$$

而非：

$$
\text{Layout}(\text{Children}(C)) \to \text{Layout}(C) \to \text{Evaluate}(@container, C) \to \text{Layout}(\text{Children}(C)) \to \ldots
$$

---

### 6.3 理论推导与原理解析

### 6.3.1 容器查询的渲染管线

1. 浏览器构建 DOM 树与 CSSOM。
2. 进行布局（Layout）：计算每个元素的位置与尺寸。
3. 遇到声明了 `container-type: inline-size` 的元素时，浏览器先计算其尺寸，再匹配 `@container` 规则。
4. 应用匹配的样式，对子元素进行二次布局。
5. 进入绘制（Paint）阶段。

### 6.3.2 `inline-size` vs `size` 的性能差异

`inline-size`：

- 只查询容器的 inline 方向（通常是宽度）。
- 容器的 block 方向（高度）仍可被子元素撑开。
- 性能较优，因为只需一次布局。

`size`：

- 同时查询容器的 inline 与 block 方向。
- 容器必须显式设置高度，否则高度为 0（因 `contain: size` 生效）。
- 性能较差，因为需要先布局容器，再评估条件，再布局子元素。

数学上，`inline-size` 容器的高度计算函数：

$$
\text{Height}(C) = f(\text{Content}(C), \text{Styles}(C))
$$

而 `size` 容器的高度计算函数：

$$
\text{Height}(C) = \text{ExplicitHeight}(C) \quad \text{(子元素不影响)}
$$

### 6.3.3 `container-name` 的命名作用域

当容器嵌套时，`container-name` 用于精确匹配：

```css
.outer {
  container-type: inline-size;
  container-name: outer;
}
.inner {
  container-type: inline-size;
  container-name: inner;
}

@container outer (min-width: 800px) {
  .card { /* 匹配最近的名为 outer 的容器 */ }
}
@container inner (min-width: 400px) {
  .card { /* 匹配最近的名为 inner 的容器 */ }
}
```

匹配规则：从子元素向上遍历祖先链，找到第一个匹配名称的容器。若未指定名称，匹配最近的任何类型容器。

### 6.3.4 `cqi` 单位的计算

`cqi`（container query inline）是容器 inline 方向尺寸的 1%。例如：

```css
.card {
  font-size: 5cqi; /* 容器宽度的 5% */
}
```

若容器宽度为 400px，则 `5cqi = 5% * 400px = 20px`。

数学定义：

$$
1\text{cqi} = \frac{\text{Width}(C)}{100}
$$

当元素不在任何容器内时，`cqi` 回退为视口 inline 方向的 1%（即 `vi`）。

### 6.3.5 Style Queries 的算法

Style Queries（实验性）允许查询容器的 CSS 变量或计算样式：

```css
.card-container {
  --theme: dark;
  container-type: inline-size;
}
@container style(--theme: dark) {
  .card {
    background: #1a1a1a;
    color: white;
  }
}
```

匹配函数：

$$
\text{Match}(@container\ style(\text{var}: \text{val}), C) =
\begin{cases}
\text{true}, & \text{if } \text{getComputedStyle}(C).\text{var} = \text{val} \\
\text{false}, & \text{otherwise}
\end{cases}
$$

注意：Style Queries 仅支持查询自定义属性（CSS Variables），暂不支持查询标准属性（如 `color`、`display`）。

### 6.3.6 容器查询与可访问性

容器查询提升了组件的灵活性，但需注意可访问性：

1. **字号放大**：用户在浏览器设置中放大字号时，容器尺寸不变，但内容可能溢出。应配合 `text-wrap: balance` 或 `text-wrap: pretty`。
2. **屏幕阅读器**：容器查询仅影响视觉，不影响 DOM 顺序，对屏幕阅读器友好。
3. **prefers-reduced-motion**：容器查询触发的布局变化应尊重用户的运动偏好。

```css
@media (prefers-reduced-motion: reduce) {
  * {
    transition: none !important;
  }
}
```

---

## 7. 本章综合挑战（选做）

1. 给一个卡片容器加 `container-type: inline-size`，用 `@container` 在窄/宽两种尺寸下切换布局；
2. 用容器查询单位 `cqw` 让标题字号跟随容器宽度；
3. 对比 `@media` 与 `@container` 在同一个组件上的行为差异；
4. 用 `container-name` 命名容器，让嵌套容器精确匹配。

## 8. 核心知识点

> 一句话记住容器查询：`container-type` 建上下文，`@container` 写条件，`cqw`/`cqh` 取尺寸；组件看容器，不看屏幕。

- 容器查询让组件按父容器尺寸响应，而非视口；
- 建立上下文：`container-type: inline-size`（或 `size`）；
- 条件语法：`@container (min-width: 400px)`；
- 容器查询单位：`cqw`/`cqh`/`cqi`/`cqb` 相对容器尺寸；
- `container-name` 命名容器，避免嵌套冲突；
- 浏览器支持：现代浏览器已普遍可用，旧环境用媒体查询兜底。

## 9. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 `container-type` | 查询不生效 | 先在容器上建立上下文 |
| 与媒体查询混用 | 行为不一致 | 组件内用容器查询，页面级用媒体查询 |
| 嵌套容器歧义 | 命中错误容器 | 用 `container-name` 明确指向 |
| 依赖容器查询做整页布局 | 视口级需求不适用 | 页面骨架仍用媒体查询 |
| 旧浏览器不兼容 | 组件样式缺失 | 提供媒体查询兜底 |

## 10. 扩展学习

- 媒体查询：`css/031-MediaQuery`；
- 响应式设计：`css/033-ResponsiveDesign`；
- 新特性：`css/064-CSSNewFeatures`；
- 组件化实践：`css/067-CSSProjectExampleResponsiveHomepage`。

## 附录 A：术语表

| 术语 | 英文 | 定义 |
| --- | --- | --- |
| 容器查询 | Container Query | 根据容器尺寸应用样式的 CSS 规则 |
| 容器类型 | container-type | 声明元素为查询容器的属性 |
| 容器名称 | container-name | 为容器命名，支持嵌套查询 |
| 内联尺寸 | inline-size | 容器的行内方向尺寸（通常是宽度） |
| 块尺寸 | block-size | 容器的块方向尺寸（通常是高度） |
| 样式查询 | Style Query | 查询容器 CSS 变量或计算样式的容器查询 |
| `cqw` | container query width | 容器宽度的 1% |
| `cqh` | container query height | 容器高度的 1% |
| `cqi` | container query inline | 容器 inline 方向的 1% |
| `cqb` | container query block | 容器 block 方向的 1% |
| 循环依赖 | Circular dependency | 元素样式与尺寸互相影响的死循环 |
| CSS Containment | CSS 包含 | 隔离元素渲染的 CSS 属性 |

## 附录 B：浏览器兼容性速查表

| 特性 | Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- | --- |
| `container-type` | 105+ | 110+ | 16+ | 105+ |
| `container-name` | 105+ | 110+ | 16+ | 105+ |
| `@container` 尺寸查询 | 105+ | 110+ | 16+ | 105+ |
| `cqw` / `cqi` 单位 | 105+ | 110+ | 16+ | 105+ |
| 命名容器 | 105+ | 110+ | 16+ | 105+ |
| Style Queries | 111+（部分） | 不支持 | 17+（部分） | 111+（部分） |
| DevTools 支持 | 105+ | 110+ | 16+ | 105+ |

## 附录 C：容器查询 Checklist

设计与开发容器查询时，按以下顺序检查：

1. [ ] 确认是否真的需要容器查询（组件复用场景）
2. [ ] 优先使用 `container-type: inline-size`
3. [ ] 为嵌套容器使用 `container-name` 命名
4. [ ] 提供 `@container` 规则外的基础样式
5. [ ] 使用 `@supports (container-type: inline-size)` 渐进增强
6. [ ] SSR 场景考虑布局抖动（CLS）
7. [ ] 使用 `cqi` 单位实现响应式字体
8. [ ] 配合 `clamp()` 限制字体范围
9. [ ] 在 Storybook 中测试各种容器尺寸
10. [ ] 检查 Lighthouse CLS 指标
11. [ ] 文档化容器查询断点
12. [ ] 避免过度嵌套容器
13. [ ] 性能测试：避免 `size` 容器导致布局开销
14. [ ] 检查 `prefers-reduced-motion` 适配

---

> 本文最后更新于 2026-06-14，内容基于 W3C CSS Containment Module Level 3（2024 Working Draft）。如规范更新，请以 W3C 最新发布为准。
## 附录 D：容器查询速查

### D.1 建立容器上下文

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

<!-- ============ 文档分隔线：007-css/033-ResponsiveDesign.md ============ -->

## 2. 媒体查询

### 基本语法

```css
@media (条件) {
  /* 样式规则 */
}
```

### 常用媒体特性

- `width`/`height`：视口宽度/高度
- `min-width`/`max-width`：最小/最大视口宽度
- `orientation`：设备方向（portrait/landscape）
- `device-pixel-ratio`：设备像素比

### 断点设置

```css
/* 移动设备 */
@media (max-width: 767px) {
  /* 移动设备样式 */
}
/* 平板设备 */
@media (min-width: 768px) and (max-width: 1023px) {
  /* 平板设备样式 */
}
/* 桌面设备 */
@media (min-width: 1024px) {
  /* 桌面设备样式 */
}
```

## 3. 弹性布局技术

### 弹性网格系统

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.item {
  flex: 1 1 300px; /* 增长因子 1, 收缩因子 1, 基础宽度 300px */
}
```

### 网格布局

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

## 4. 响应式图像

### 自适应图像

```css
img {
  max-width: 100%;
  height: auto;
}
```

### 图片源集

```html
<picture>
  <source media="(max-width: 768px)" srcset="small-image.jpg" />
  <source media="(min-width: 769px)" srcset="large-image.jpg" />
  <img src="fallback-image.jpg" alt="Description" />
</picture>
```

## 5. 响应式排版

### 相对字体单位

```css
 :root {
  font-size: 16px;
 }
 @media (max-width: 768px) {
  :root {
  font-size: 14px;
  }
 }
 body {
  font-size: 1rem;
 }
 h1 {
  font-size: 2.5rem;
 }
```

## 6. 响应式设计最佳实践

1. **移动优先**：从移动设备开始设计，然后扩展到更大的屏幕
2. **渐进增强**：确保基本功能在所有设备上都能正常工作
3. **性能优化**：针对移动设备优化图像和资源加载
4. **测试**：在不同设备和浏览器上测试设计
5. **简化导航**：在移动设备上使用汉堡菜单等简化导航

## 7. 常见问题与解决方案

### 问题1：图像在小屏幕上显示过大

**解决方案**：使用 `max-width: 100%; height: auto;` 确保图像适应容器

### 问题2：导航菜单在小屏幕上拥挤

**解决方案**：实现汉堡菜单，在小屏幕上折叠导航

### 问题3：表格在小屏幕上溢出

**解决方案**：在小屏幕上使表格可水平滚动，或重新设计表格布局

## 8. 工具与资源

- **响应式设计测试工具**：
- [Responsinator](http://www.responsinator.com/)
- [BrowserStack](https://www.browserstack.com/)
- Chrome DevTools 设备模拟器
- **响应式框架**：
- [Bootstrap](https://getbootstrap.com/)
- [Foundation](https://get.foundation/)
- [Tailwind CSS](https://tailwindcss.com/)

## 9. 实战示例

### 响应式导航栏

```html
<nav class="navbar">
  <div class="logo">Logo</div>
  <div class="menu-toggle"></div>
  <ul class="nav-links">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Services</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: #333;
  color: white;
}
.nav-links {
  display: flex;
  list-style: none;
  gap: 1rem;
}
.menu-toggle {
  display: none;
  cursor: pointer;
}
@media (max-width: 768px) {
  .nav-links {
    position: absolute;
    top: 70px;
    left: 0;
    right: 0;
    background: #333;
    flex-direction: column;
    align-items: center;
    padding: 1rem;
    gap: 1rem;
    display: none;
  }
  .nav-links.active {
    display: flex;
  }
  .menu-toggle {
    display: block;
  }
}
```

```javascript
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');
menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});
```

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

## 动手试试

1. 把一张桌面页面改成移动优先：先写单栏基础样式，再在 768px 加双栏；
2. 用 `clamp()` 实现标题响应式字号；
3. 用响应式图片（srcset + sizes）替换固定图片；
4. 进阶挑战：用容器查询让组件按容器自适应。

## 核心知识点

> 一句话记住响应式：移动优先、弹性单位、断点跟随内容、图片响应式、容器查询组件化。

- 三大件：viewport、媒体查询、弹性单位；
- 移动优先：基础样式单栏，`min-width` 增强；
- 断点按内容需求设定；
- 图片：`max-width: 100%` + `srcset` + `object-fit`；
- 容器查询让组件自适配；
- 深色模式与减少动效用媒体查询。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 固定宽度布局 | 小屏溢出 | 弹性布局 |
| 断点过多 | 维护困难 | 3-5 个关键断点 |
| 图片不响应 | 流量浪费 | srcset/懒加载 |
| 忽略触屏 | 误触 | 热区 ≥ 44px |

## 扩展学习

- 媒体查询：`css/031-MediaQuery`；
- 容器查询：`css/032-ContainerQuery`；
- 移动适配：`css/052-MobileAdaptation`；
- 响应式图片：`html5/019-ImageResponsiveImage`。

<!-- ============ 文档分隔线：007-css/034-ModernColorSpace.md ============ -->

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

## 动手试试

1. 用 `oklch()` 定义一组颜色，观察与 hex 的差异；
2. 用 `color-mix()` 混合主色与白色生成浅色变体；
3. 用 `color()` 引用 display-p3 广色域；
4. 进阶挑战：为高 DCI-P3 屏幕提供增强色。

## 核心知识点

> 一句话记住现代颜色：`oklch`/`oklab` 感知均匀、`color-mix()` 混合颜色、`color()` 用广色域，深色主题靠变量切换。

- 传统：hex/rgb/hsl；
- `oklch`：感知均匀的现代色彩空间，渐变更平滑；
- `color-mix(in srgb, a, b 30%)`：颜色混合；
- `color(display-p3 ...)`：广色域；
- 渐变插值：`interpolation-method` 指定色彩空间；
- 变量 + 现代色 = 主题系统。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 兼容性 | 旧浏览器不支持 | 提供 hex 兜底 |
| 混合模式参数写错 | 结果异常 | 先写 in srgb |
| 广色域无兜底 | 颜色偏移 | 同时声明 sRGB 值 |

## 扩展学习

- 渐变：`css/024-Gradient`；
- 变量：`css/035-CSSVariableCustomAttribute`；
- 滤镜：`css/048-CSSFilters`。

<!-- ============ 文档分隔线：007-css/035-CSSVariableCustomAttribute.md ============ -->

## 1. CSS 自定义属性基础

### 1.1 什么是 CSS 自定义属性

CSS自定义属性（也称为CSS变量）允许开发者定义可复用的值，通过 `--` 前缀声明，使用 `var()` 函数引用。

```css
/* 声明自定义属性 */
:root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --font-size-base: 16px;
  --spacing-unit: 8px;
  --border-radius: 4px;
  --transition-speed: 0.3s;
}

/* 使用自定义属性 */
.button {
  background-color: var(--primary-color);
  font-size: var(--font-size-base);
  padding: var(--spacing-unit) calc(var(--spacing-unit) * 2);
  border-radius: var(--border-radius);
  transition: background-color var(--transition-speed) ease;
}

.button:hover {
  background-color: var(--secondary-color);
}
```

### 1.2 与预处理器变量的区别

| 特性           | CSS自定义属性      | Sass/Less变量  |
| :------------- | :----------------- | :------------- |
| 运行时         | 是，动态更新       | 否，编译时替换 |
| 作用域         | 遵循CSS层叠        | 全局或块级     |
| 媒体查询       | 可在媒体查询中修改 | 不可           |
| JavaScript操作 | 可读写             | 不可           |
| 浏览器支持     | 现代浏览器         | 编译后无限制   |

### 1.3 命名规范

```css
:root {
  /* 推荐：使用有意义的名称 */
  --color-primary: #3498db;
  --color-secondary: #2ecc71;
  --color-text: #333;
  --color-background: #fff;

  /* 推荐：语义化命名而非具体值 */
  --color-danger: #e74c3c; /* 而非 --color-red */
  --spacing-small: 8px; /* 而非 --spacing-8px */
  --font-size-large: 1.25rem; /* 而非 --font-size-20 */

  /* 大小写敏感 */
  --myVar: 10px;
  --myvar: 20px; /* 不同于 --myVar */

  /* 可以包含特殊字符 */
  --my-color: blue;
  --my_color: blue;
}
```

## 2. 作用域与层叠

### 2.1 自定义属性的作用域

```css
/* 全局作用域（:root） */
:root {
  --main-color: #3498db;
  --padding: 16px;
}

/* 局部作用域 */
.card {
  --card-bg: white;
  --card-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background: var(--card-bg);
  box-shadow: var(--card-shadow);
  padding: var(--padding);
}

/* 子元素继承父元素的自定义属性 */
.card-header {
  /* 继承 --card-bg, --card-shadow, --main-color 等 */
  color: var(--main-color);
  padding: var(--padding);
}

/* 覆盖父级自定义属性 */
.dark .card {
  --card-bg: #2d2d2d;
  --card-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  --main-color: #5dade2; /* 局部覆盖 */
}
```

### 2.2 层叠与优先级

```css
:root {
  --theme-color: blue;
}

.container {
  --theme-color: green;
}

.container .element {
  /* --theme-color 为 green（继承自 .container） */
  color: var(--theme-color);
}

.element-outside {
  /* --theme-color 为 blue（继承自 :root） */
  color: var(--theme-color);
}

/* 优先级规则与普通CSS属性相同 */
#special {
  --theme-color: red; /* ID选择器优先级更高 */
}
```

## 3. var() 函数

### 3.1 基本用法与默认值

```css
.element {
  /* 使用默认值：当变量未定义时使用 */
  color: var(--text-color, #333);
  font-size: var(--font-size, 16px);

  /* 默认值可以是另一个变量 */
  background: var(--bg-color, var(--default-bg, white));

  /* 默认值可以包含空格和多个值 */
  margin: var(--margin, 10px 20px);

  /* 不能用于属性名 */
  /* 错误: var(--prop-name): red; */
}
```

### 3.2 var() 在计算中的使用

```css
:root {
  --spacing: 8;
}

.element {
  /* calc() 中使用变量 */
  padding: calc(var(--spacing) * 1px); /* 8px */
  margin: calc(var(--spacing) * 2px); /* 16px */
  width: calc(100% - var(--spacing) * 4px); /* 100% - 32px */

  /* 变量直接存储带单位的值更常见 */
  --spacing-unit: 8px;
  padding: var(--spacing-unit);
  margin: calc(var(--spacing-unit) * 2);
}
```

## 4. 动态主题系统

### 4.1 亮色/暗色主题

```css
/* 亮色主题 */
:root {
  --color-bg-primary: #ffffff;
  --color-bg-secondary: #f5f5f5;
  --color-text-primary: #333333;
  --color-text-secondary: #666666;
  --color-border: #e0e0e0;
  --color-accent: #3498db;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* 暗色主题 */
[data-theme='dark'] {
  --color-bg-primary: #1a1a2e;
  --color-bg-secondary: #16213e;
  --color-text-primary: #e0e0e0;
  --color-text-secondary: #a0a0a0;
  --color-border: #333355;
  --color-accent: #5dade2;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
}

/* 系统偏好检测 */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme]) {
    --color-bg-primary: #1a1a2e;
    --color-bg-secondary: #16213e;
    --color-text-primary: #e0e0e0;
    --color-text-secondary: #a0a0a0;
    --color-border: #333355;
    --color-accent: #5dade2;
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
  }
}

/* 应用主题变量 */
body {
  background-color: var(--color-bg-primary);
  color: var(--color-text-primary);
  transition:
    background-color 0.3s ease,
    color 0.3s ease;
}

.card {
  background-color: var(--color-bg-secondary);
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
  color: var(--color-text-primary);
}
```

### 4.2 JavaScript 动态切换主题

```html
<button id="theme-toggle">切换主题</button>

<script>
  const toggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  // 读取保存的主题偏好
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    html.setAttribute('data-theme', savedTheme);
  }

  toggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
  });
</script>
```

### 4.3 品牌主题系统

```css
/* 多品牌主题 */
:root {
  /* 默认品牌 */
  --brand-primary: #3498db;
  --brand-secondary: #2ecc71;
  --brand-gradient: linear-gradient(135deg, var(--brand-primary), var(--brand-secondary));
}

[data-brand='brand-a'] {
  --brand-primary: #e74c3c;
  --brand-secondary: #f39c12;
}

[data-brand='brand-b'] {
  --brand-primary: #9b59b6;
  --brand-secondary: #1abc9c;
}

/* 组件使用品牌变量 */
.brand-button {
  background: var(--brand-gradient);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: var(--border-radius, 4px);
}
```

## 5. 响应式设计中的变量

### 5.1 断点变量

```css
:root {
  /* 断点值（用于JS读取） */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;

  /* 响应式间距 */
  --container-padding: 16px;
  --section-spacing: 32px;
}

@media (min-width: 768px) {
  :root {
    --container-padding: 24px;
    --section-spacing: 48px;
  }
}

@media (min-width: 1024px) {
  :root {
    --container-padding: 32px;
    --section-spacing: 64px;
  }
}

.container {
  padding: 0 var(--container-padding);
}

section {
  margin-bottom: var(--section-spacing);
}
```

### 5.2 流式排版

```css
:root {
  /* 流式字体大小 */
  --font-size-base: clamp(1rem, 0.875rem + 0.5vw, 1.25rem);
  --font-size-sm: clamp(0.875rem, 0.75rem + 0.5vw, 1rem);
  --font-size-lg: clamp(1.25rem, 1rem + 1vw, 1.75rem);
  --font-size-xl: clamp(1.75rem, 1.25rem + 2vw, 3rem);
}

body {
  font-size: var(--font-size-base);
}

h1 {
  font-size: var(--font-size-xl);
}
h2 {
  font-size: var(--font-size-lg);
}
small {
  font-size: var(--font-size-sm);
}
```

## 6. JavaScript 操作自定义属性

### 6.1 读写自定义属性

```javascript
// 读取自定义属性
const root = document.documentElement;
const primaryColor = getComputedStyle(root).getPropertyValue('--color-primary');
console.log(primaryColor.trim()); // "#3498db"

// 设置自定义属性
root.style.setProperty('--color-primary', '#e74c3c');

// 在特定元素上设置
const card = document.querySelector('.card');
card.style.setProperty('--card-bg', '#f0f0f0');

// 移除自定义属性
card.style.removeProperty('--card-bg');
```

### 6.2 动态样式更新

```javascript
// 根据用户输入动态更新主题色
function updateAccentColor(hex) {
  document.documentElement.style.setProperty('--color-accent', hex);
}

// 基于滚动位置更新变量
window.addEventListener('scroll', () => {
  const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  document.documentElement.style.setProperty('--scroll-progress', scrollPercent);
});

// 鼠标位置跟踪
document.addEventListener('mousemove', (e) => {
  const x = e.clientX / window.innerWidth;
  const y = e.clientY / window.innerHeight;
  document.documentElement.style.setProperty('--mouse-x', x);
  document.documentElement.style.setProperty('--mouse-y', y);
});
```

## 7. 常见问题与解决方案

### 7.1 变量未定义时的回退

```css
/* 问题：变量未定义导致属性无效 */
.element {
  color: var(--undefined-var); /* 无效值，属性被忽略 */
}

/* 解决方案1：提供默认值 */
.element {
  color: var(--undefined-var, #333);
}

/* 解决方案2：使用 @supports 检测 */
@supports (--css: variables) {
  .element {
    color: var(--text-color);
  }
}
@supports not (--css: variables) {
  .element {
    color: #333;
  }
}
```

### 7.2 循环依赖

```css
/* 错误：循环引用 */
:root {
  --a: var(--b);
  --b: var(--a); /* 无限循环！ */
}

/* 解决方案：确保变量定义不形成环 */
:root {
  --a: blue;
  --b: var(--a); /* 正确：单向依赖 */
}
```

### 7.3 变量与单位

```css
/* 问题：变量值缺少单位 */
:root {
  --size: 20;
}

.element {
  /* width: var(--size)px;  错误！这会被解析为 "20px" 字符串但不是有效值 */
  width: calc(var(--size) * 1px); /* 正确 */
}

/* 推荐：变量直接包含单位 */
:root {
  --size: 20px;
}

.element {
  width: var(--size); /* 简洁正确 */
}
```

## 8. 总结与最佳实践

### 8.1 核心要点

1. **CSS变量是运行时动态的**，与预处理器变量本质不同
2. **遵循层叠规则**，可在任何选择器中定义和覆盖
3. **var() 必须提供默认值**，增强健壮性
4. **语义化命名**，使用 `--color-danger` 而非 `--color-red`

### 8.2 最佳实践

1. **全局变量放在 :root**，局部变量放在组件选择器
2. **分类组织变量**：颜色、间距、字体、动画等分组
3. **主题系统用 data 属性**：`[data-theme="dark"]` 切换
4. **响应式用媒体查询修改变量**，而非重复写组件样式
5. **JavaScript 修改变量实现动态效果**，避免直接操作样式
6. **变量命名加前缀**：避免与第三方库冲突，如 `--myapp-color`
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

## 动手试试

1. 在 `:root` 定义颜色/间距/圆角变量，改造一个卡片组件；
2. 用媒体查询覆盖变量做深色主题；
3. 用 JavaScript 修改 `document.documentElement.style.setProperty('--x', v)` 动态换肤；
4. 进阶挑战：用 `@property` 注册变量并做数值动画。

## 核心知识点

> 一句话记住 CSS 变量：`--name` 定义、`var()` 引用、作用域继承、媒体查询与 JS 可覆盖，是设计令牌的载体。

- 定义：`--primary: #3498db`；引用：`var(--primary)`；
- `:root` 定义全局变量，选择器内定义局部变量；
- 变量遵循继承与就近覆盖；
- 可在媒体查询、伪类中重新赋值；
- JS 通过 `style.setProperty` 读写；
- 与预处理器变量不同：CSS 变量是运行时特性；
- `@property` 可声明变量类型并支持动画。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 变量名无语义 | 维护困难 | `--color-primary`/`--space-md` |
| 忘记回退值 | 未定义时报错 | `var(--x, 默认值)` |
| 存复杂对象 | 变量只能存值 | 状态交给 JS |
| 深色模式不覆盖 | 主题不完整 | 只覆盖颜色变量 |

## 扩展学习

- 主题实践：`css/001-CSS3OverviewBasicSyntax` 的变量章节；
- 函数：`css/053-Function`；
- 工程化：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/036-LogicalProperty.md ============ -->

> 前置依赖：先理解 003 盒模型的物理属性。

## 1. 逻辑属性概述

逻辑属性根据书写模式（writing mode）自动适配方向，替代物理方向属性。

### 物理属性 vs 逻辑属性

| 物理属性        | 逻辑属性              | 说明       |
| --------------- | --------------------- | ---------- |
| `margin-top`    | `margin-block-start`  | 块轴起始   |
| `margin-bottom` | `margin-block-end`    | 块轴结束   |
| `margin-left`   | `margin-inline-start` | 行内轴起始 |
| `margin-right`  | `margin-inline-end`   | 行内轴结束 |
| `width`         | `inline-size`         | 行内尺寸   |
| `height`        | `block-size`          | 块尺寸     |
| `top`           | `inset-block-start`   | 块轴偏移   |
| `left`          | `inset-inline-start`  | 行内轴偏移 |

## 2. 简写属性

```css
/* margin */
margin-block: 10px 20px; /* block-start block-end */
margin-inline: 15px; /* inline-start = inline-end */
margin: 10px 15px; /* block inline */

/* padding */
padding-block: 1rem;
padding-inline: 2rem;

/* inset */
inset-block-start: 0;
inset-inline-start: 0;
inset: 0; /* 四个方向 */

/* size */
inline-size: 100%;
block-size: auto;
```

## 3. 边框与圆角

```css
border-block-start: 1px solid #ccc;
border-inline-end: 2px dashed #999;
border-start-start-radius: 8px; /* 行内起始 + 块起始 */
border-end-end-radius: 8px; /* 行内结束 + 块结束 */
```

## 4. 书写模式适配

```css
/* 水平书写模式（默认） */
.element {
  writing-mode: horizontal-tb;
}
/* margin-block-start = margin-top */

/* 垂直书写模式 */
.element {
  writing-mode: vertical-rl;
}
/* margin-block-start = margin-right */
```

## 5. 国际化支持

```css
/* 自动适配 RTL 语言 */
[dir='rtl'] .element {
  /* 无需额外样式 */
}

/* 使用逻辑属性后，RTL 自动适配 */
.element {
  margin-inline-start: 1rem; /* LTR: left, RTL: right */
  padding-inline-end: 2rem;
}
```

## 动手试试

1. 用 `margin-inline` 代替 `margin-left/right` 改写一段布局；
2. 用 `padding-block` 控制上下内边距；
3. 给元素设置 `writing-mode: vertical-rl`，观察逻辑属性如何跟随方向；
4. 进阶挑战：做一个支持 RTL（阿拉伯语）的页面骨架。

## 核心知识点

> 一句话记住逻辑属性：`block` 是书写方向（上下），`inline` 是行内方向（左右）；逻辑属性让样式自动适配 LTR/RTL 与竖排。

- 物理属性：`margin-left`、`padding-top`、`width`；
- 逻辑属性：`margin-inline`、`padding-block`、`inline-size`；
- `block` 轴随书写模式，`inline` 轴随行内方向；
- 配合 `writing-mode`/`direction` 自动翻转；
- 国际化页面优先逻辑属性。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 混用物理/逻辑属性 | 方向切换后错位 | 统一使用逻辑属性 |
| 旧浏览器兼容 | 部分属性不支持 | 提供物理属性兜底 |
| 误以为逻辑属性是简写 | 它们是方向映射 | 理解 block/inline 轴 |

## 扩展学习

- 排版：`css/044-TypographyAndGridSystem`；
- 国际化：`html5/016-TextSemantic` 的 bdi 与方向；
- 新特性：`css/064-CSSNewFeatures`。

<!-- ============ 文档分隔线：007-css/037-CSSWritingModes.md ============ -->

## 0. 直觉：文字方向一变，整个布局坐标系都变了

默认网页是“从左到右、从上到下”的横排（`horizontal-tb`）。日文古籍、中文标语常需要竖排（`vertical-rl`），阿拉伯语需要从右到左。`writing-mode` 切换方向后，`margin-left` 这类物理属性不再符合直觉——所以要用逻辑属性。

## 1. writing-mode 的三个取值

```css
.horizontal {
  writing-mode: horizontal-tb;  /* 默认：行水平，块从上到下 */
}
.vertical-rl {
  writing-mode: vertical-rl;    /* 竖排：行垂直，块从右到左 */
}
.vertical-lr {
  writing-mode: vertical-lr;    /* 竖排：行垂直，块从左到右 */
}
```

**讲解：** 名字拆解：`vertical-rl` = 行内方向垂直、块级方向从右到左。中文竖排用 `vertical-rl`，标题与书签常见；`vertical-lr` 多用于表格与东亚以外的竖排场景。

## 2. 竖排后的文字控制

```css
.vertical-text {
  writing-mode: vertical-rl;
  text-orientation: mixed;  /* 默认：中文直立，拉丁字母旋转 90 度 */
}
.upright {
  text-orientation: upright; /* 所有字符直立 */
}
```

**讲解：** 竖排时数字与英文默认旋转，`text-orientation: upright` 可强制直立；`text-combine-upright: all` 还能把“2026”这样的数字竖排时压缩成一个直立数字串。

## 3. 逻辑属性：方向变了布局不乱

```css
.card {
  /* 物理属性：竖排时语义混乱 */
  /* margin-left: 8px; */

  /* 逻辑属性：始终指“行首方向” */
  margin-inline-start: 8px;
  padding-block: 12px;       /* 块方向（上下）内边距 */
  border-inline-end: 2px solid #4f5bd5;  /* 行尾方向边框 */
}
```

**讲解：** 逻辑属性用 `block`（块方向）与 `inline`（行内方向）代替上下左右：`margin-inline-start` 在横排时是左边距，竖排时自动变成上边距。要支持多语言/多方向的项目应优先逻辑属性，完整清单见 `css/036-LogicalProperty`。

## 4. direction 与 dir 属性

```css
.rtl {
  direction: rtl;  /* 从右到左排版（阿拉伯语、希伯来语） */
}
```

```html
<p dir="rtl">عربى</p>
```

**讲解：** `direction` 控制行内方向，但更推荐在 HTML 上用 `dir` 属性声明，因为 `dir` 能同步影响文本语义、选择器与无障碍树。CSS 的 `direction` 只做视觉覆盖。

## 5. 动手试试

1. 给一段中文设置 `writing-mode: vertical-rl`，观察标点与数字的朝向；
2. 在竖排容器里分别用 `margin-left` 与 `margin-inline-start`，对比两者的表现；
3. 用 `text-combine-upright: all` 让竖排中的年份“2026”直立压缩；
4. 进阶挑战：把一套横排卡片布局改成逻辑属性，再切换 `writing-mode` 验证布局仍然正确。

## 6. 核心知识点

> 一句话记住书写模式：writing-mode 切换横竖排，text-orientation 管字符朝向，方向相关的间距边框用逻辑属性才不随方向错乱。

- `horizontal-tb` 默认横排，`vertical-rl`/`vertical-lr` 竖排；
- 中文竖排选 `vertical-rl`；
- `text-orientation: upright` 强制字符直立；
- 逻辑属性 `*-inline-*`/`*-block-*` 随方向自动调整；
- 多语言项目优先 `dir` 属性，而非 CSS `direction`；
- 逻辑属性详解见 `css/036-LogicalProperty`。

## 7. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 竖排容器用物理 margin | 方向切换后间距错乱 | 统一改用逻辑属性 |
| 数字/英文竖排旋转 | 阅读体验差 | `text-orientation: upright` |
| 用 CSS direction 控制语义 | 无障碍树与选择器不同步 | HTML 用 `dir` 声明 |
| 竖排与 flex 混用 | 主轴方向理解混乱 | 先确认 `writing-mode` 再定主轴 |

## 8. 扩展学习

- 逻辑属性全集：`css/036-LogicalProperty`；
- 文本与字体：`css/004-TextAndFontsBasics`；
- 国际化与可访问性样式：`css/045-AccessibleStyling`；
- 排版进阶：`css/044-TypographyAndGridSystem`。

<!-- ============ 文档分隔线：007-css/038-ScrollSnap.md ============ -->

## 1. scroll-snap 概述

CSS 滚动捕捉允许创建类似轮播图的滚动效果，滚动停止时自动对齐到指定位置。

## 2. 容器属性

```css
.scroll-container {
  scroll-snap-type: x mandatory; /* 方向 + 严格度 */
  overflow-x: auto;
}
```

### scroll-snap-type

| 方向   | 说明     |
| ------ | -------- |
| `x`    | 水平捕捉 |
| `y`    | 垂直捕捉 |
| `both` | 双向捕捉 |

| 严格度      | 说明               |
| ----------- | ------------------ |
| `mandatory` | 必须捕捉（强对齐） |
| `proximity` | 接近时捕捉（默认） |

## 3. 子元素属性

```css
.scroll-item {
  scroll-snap-align: start; /* 对齐方式 */
  scroll-snap-stop: always; /* 停止行为 */
}
```

### scroll-snap-align

| 值       | 说明         |
| -------- | ------------ |
| `start`  | 对齐容器起始 |
| `center` | 对齐容器中心 |
| `end`    | 对齐容器结束 |

### scroll-snap-stop

| 值       | 说明             |
| -------- | ---------------- |
| `normal` | 可以跳过（默认） |
| `always` | 必须停止         |

## 4. 实战：轮播图

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 0 20px;
}

.carousel-item {
  flex: 0 0 100%;
  scroll-snap-align: center;
}
```

## 5. 实战：全屏滚动

```css
.fullpage {
  height: 100vh;
  overflow-y: auto;
  scroll-snap-type: y mandatory;
}

.fullpage-section {
  height: 100vh;
  scroll-snap-align: start;
}
```

## 6. scroll-margin 和 scroll-padding

```css
/* 捕捉偏移 */
.snap-item {
  scroll-margin: 80px;
} /* 元素偏移 */
.container {
  scroll-padding: 80px;
} /* 容器偏移 */
```

## 7. scroll-behavior：平滑滚动

```css
html {
  scroll-behavior: smooth;   /* 锚点跳转与 JS scrollTo 变成平滑滚动 */
}
```

**讲解：** `scroll-behavior` 控制“编程式滚动”的动效：`auto` 直接跳转（默认），`smooth` 平滑过渡。它作用于 `a[href="#锚点"]` 跳转、`scrollTo()` 等操作，不影响用户手动拖动滚动条。配合滚动捕捉使用时，平滑滚动会让吸附过程更自然。

```css
/* 尊重系统“减少动态效果”设置 */
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }
}
```

**讲解：** 平滑滚动会让部分用户不适，生产环境建议在 `prefers-reduced-motion` 下关闭，详见 `css/045-AccessibleStyling`。

## 动手试试

1. 做一个横向滚动的图片轮播，`scroll-snap-type: x mandatory` 实现吸附；
2. 用 `scroll-snap-align: center` 让每张图居中停靠；
3. 给容器加 `scroll-padding` 适配固定导航；
4. 进阶挑战：纵向滚动的“整屏翻页”效果。

## 核心知识点

> 一句话记住滚动捕捉：容器 `scroll-snap-type` 定吸附轴，子项 `scroll-snap-align` 定停靠点，`scroll-padding` 避让固定元素。

- `scroll-snap-type: x mandatory`（强制）或 `proximity`（就近）；
- `scroll-snap-align: start/center/end`；
- `scroll-padding` 为吸顶导航留空间；
- `scroll-margin` 作用于子项；
- 适合轮播、图库、分页式滚动。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| mandatory 过强 | 内容读不到 | 长内容用 proximity |
| 子项未撑满 | 吸附不生效 | 子项宽度=容器宽度 |
| 忽略 scroll-padding | 停靠被遮挡 | 加 scroll-padding |
| 与触摸滚动冲突 | 手势异常 | 测试各浏览器行为 |

## 扩展学习

- 滚动行为：`scroll-behavior: smooth`；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`；
- 移动端：`css/052-MobileAdaptation`。

<!-- ============ 文档分隔线：007-css/039-CascadeLayer.md ============ -->

> 前置依赖：先读 009 优先级计算，理解层叠顺序。

## 1. @layer 概述

CSS 层叠层（Cascade Layers）允许开发者将 CSS 规则分组到不同的层中，控制层叠优先级。

```css
@layer reset, base, components, utilities;

@layer reset {
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
}

@layer base {
  body {
    font-family: sans-serif;
    line-height: 1.6;
  }
}

@layer components {
  .card {
    border-radius: 8px;
    padding: 1rem;
  }
}

@layer utilities {
  .hidden {
    display: none;
  }
}
```

## 2. 层优先级

**后声明的层优先级更高**：reset < base < components < utilities

**未分层的规则优先级最高**（高于所有层）。

## 3. 嵌套层

```css
@layer framework {
  @layer base {
    .btn {
      padding: 8px;
    }
  }
  @layer theme {
    .btn {
      color: blue;
    }
  }
}

/* 引用嵌套层 */
@layer framework.theme {
  .btn {
    color: red;
  }
}
```

## 4. @import 与 @layer

```css
@import url('reset.css') layer(reset);
@import url('base.css') layer(base);
```

## 5. 最佳实践

- 使用 `@layer` 声明层顺序
- 第三方样式放在低优先级层
- 自定义样式放在高优先级层
- 工具类放在最高优先级层
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

## 动手试试

1. 声明 `@layer reset, base, components, utilities` 并各写一条同权重规则，观察优先级；
2. 把第三方库样式放进 `@layer vendor`，确认能被业务层覆盖；
3. 用 `@layer` 替代 `!important` 解决一次覆盖问题；
4. 进阶挑战：对比 `@layer` 与 `@import layer()` 的用法。

## 核心知识点

> 一句话记住 @layer：层顺序决定胜负（后声明的层优先），层内再看权重；第三方样式进层，业务样式出层。

- `@layer a, b, c` 声明层顺序，后面的层优先级高；
- 未分层样式优先级高于所有分层样式；
- 层内仍按选择器权重与顺序计算；
- 适合管理 reset、框架、组件、工具类；
- 与 `!important` 的交互：important 反转层顺序。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 层顺序搞反 | 覆盖失败 | 声明顺序即优先级 |
| 全部塞进层 | 调试困难 | 只给可覆盖的样式分层 |
| 与 !important 混用 | 行为反转 | 明确层优先级语义 |
| 旧浏览器不支持 | 层不生效 | 提供无层兜底 |

## 扩展学习

- 优先级：`css/009-PriorityCalculation`；
- 架构：`css/043-CSSArchitectureMethodology`；
- 新特性：`css/064-CSSNewFeatures`。

<!-- ============ 文档分隔线：007-css/040-FeatureQuery.md ============ -->

## 1. @supports 语法

```css
@supports (display: grid) {
  .container {
    display: grid;
  }
}

@supports not (display: grid) {
  .container {
    display: flex;
  }
}
```

### 逻辑操作符

```css
@supports (display: grid) and (gap: 1rem) {
}
@supports (display: flex) or (display: grid) {
}
@supports not (display: grid) {
}
```

## 2. 常用检测

```css
@supports (backdrop-filter: blur(10px)) {
  .glass {
    backdrop-filter: blur(10px);
  }
}
@supports (aspect-ratio: 1/1) {
  .square {
    aspect-ratio: 1/1;
  }
}
@supports (selector(:has(*))) {
  .card:has(.badge) {
    border-color: gold;
  }
}
```

## 3. JavaScript 检测

```javascript
if (CSS.supports('display', 'grid')) {
  /* 使用 Grid */
}
if (CSS.supports('(display: grid) and (gap: 1rem)')) {
  /* 使用 Grid + gap */
}
```

## 4. 渐进增强策略

```css
/* 基础样式 */
.container {
  display: flex;
  flex-wrap: wrap;
}
.item {
  width: 50%;
}

/* 增强样式 */
@supports (display: grid) {
  .container {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
  .item {
    width: auto;
  }
}
```

## 动手试试

1. 用 `@supports (display: grid)` 为支持 Grid 的浏览器提供布局，其余用 flex 兜底；
2. 用 `@supports not (...)` 做反向检测；
3. 在浏览器控制台用 CSS.supports() 检测特性；
4. 进阶挑战：用 `selector()` 检测选择器支持。

## 核心知识点

> 一句话记住特性查询：`@supports (属性: 值)` 检测浏览器能力，优雅降级与渐进增强的工具。

- 语法：`@supports (display: grid) { ... }`；
- 组合：`and`/`or`/`not`；
- JS 侧：`CSS.supports('display', 'grid')`；
- 用于新特性（Grid、:has、容器查询）的渐进增强；
- 不支持的浏览器直接忽略规则块。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 过度嵌套 | 可读性差 | 保持一层 |
| 把支持检测当版本检测 | 能力检测更可靠 | 检测具体属性 |
| 忘记兜底 | 不支持时无样式 | 先写基础样式再增强 |

## 扩展学习

- 渐进增强：`css/064-CSSNewFeatures`；
- 容器查询：`css/032-ContainerQuery`；
- 兼容性：`css/009-PriorityCalculation` 附录。

<!-- ============ 文档分隔线：007-css/041-CSSNativeNesting.md ============ -->

## 1. CSS 原生嵌套概述

CSS 原生嵌套（CSS Nesting）允许在选择器内部嵌套子选择器，无需预处理器。

```css
.card {
  padding: 1rem;
  background: white;

  & .title {
    font-size: 1.5rem;
    font-weight: bold;
  }

  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  @media (min-width: 768px) {
    padding: 2rem;
  }
}
```

## 2. 嵌套规则

### 2.1 & 符号

`&` 代表父选择器：

```css
.btn {
  background: blue;

  &:hover {
    background: darkblue;
  }
  &:active {
    transform: scale(0.98);
  }
  &--primary {
    background: green;
  }
  &__icon {
    margin-right: 8px;
  }
}
```

### 2.2 隐式嵌套

不带 `&` 的嵌套会自动在前面添加父选择器：

```css
.card {
  .title {
    font-size: 1.5rem;
  }
  /* 等价于 .card .title */
}
```

### 2.3 嵌套 @规则

```css
.container {
  width: 100%;

  @media (min-width: 768px) {
    width: 750px;
  }
  @media (min-width: 1024px) {
    width: 960px;
  }
  @supports (backdrop-filter: blur(10px)) {
    backdrop-filter: blur(10px);
  }
}
```

## 3. 与预处理器嵌套的区别

| 特性       | CSS 原生嵌套           | Sass/Less      |
| ---------- | ---------------------- | -------------- |
| 运行时     | 浏览器原生             | 需编译         |
| & 用法     | 必须（隐式时自动添加） | 可选           |
| 嵌套深度   | 无限制                 | 无限制         |
| @规则嵌套  |                        |                |
| 浏览器支持 | 2023+                  | 全部（编译后） |

## 4. 最佳实践

- 嵌套深度不超过 3 层
- 优先使用 `&` 显式引用
- 善用 @规则嵌套简化媒体查询

## 动手试试

1. 用原生嵌套重写一个卡片组件的样式；
2. 用 `&` 写 hover 与伪元素；
3. 对比原生嵌套与 Sass 嵌套的语法差异；
4. 进阶挑战：嵌套媒体查询。

## 核心知识点

> 一句话记住原生嵌套：选择器写在父选择器内部，`&` 引用父级；现代浏览器直接支持，无需编译。

- 嵌套规则：子选择器继承父选择器；
- `&` 引用父选择器（hover、伪元素、修饰符）；
- 支持嵌套媒体查询；
- 与 Sass 嵌套语法基本一致；
- 浏览器支持：Chrome 120+、Firefox 117+、Safari 17.2+。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 嵌套过深 | 选择器膨胀 | 控制在 3 层内 |
| 依赖编译 | 老浏览器不支持 | 用构建工具转译或确认目标 |
| 与 Sass 混用 | 语义混乱 | 统一写法 |

## 扩展学习

- Sass：`css/054-Sass`；
- 新特性：`css/064-CSSNewFeatures`；
- 选择器：`css/007-CSS3SelectorSystem`。

<!-- ============ 文档分隔线：007-css/042-CSSPerformanceOptimizationDetailed.md ============ -->

## 1. 关键渲染路径与 CSS

### 1.1 CSS 阻塞渲染

CSS 是渲染阻塞资源，浏览器必须下载并解析所有 CSS 后才能绘制页面：

```
HTML 解析 → 发现 CSS → 下载 CSS → 解析 CSS → 构建 CSSOM → 合并渲染树 → 布局 → 绘制
```

CSSOM 构建时间公式：

$$T_{render} = T_{download} + T_{parse} + T_{CSSOM}$$

### 1.2 优化目标

- 减少 CSS 文件体积
- 减少 CSS 阻塞时间
- 优先加载首屏关键 CSS
- 延迟加载非关键 CSS

## 2. 关键 CSS 内联

### 2.1 原理

将首屏可见内容所需的 CSS（Critical CSS）直接内联到 HTML `<head>` 中，消除额外的网络请求。

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      /* 关键 CSS — 首屏渲染所需 */
      body {
        margin: 0;
        font-family: system-ui;
      }
      .header {
        background: #007bff;
        color: white;
        padding: 16px;
      }
      .hero {
        min-height: 60vh;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .hero__title {
        font-size: 48px;
        font-weight: 700;
      }
    </style>
    <!-- 非关键 CSS 异步加载 -->
    <link
      rel="preload"
      href="/styles/non-critical.css"
      as="style"
      onload="this.onload=null;this.rel='stylesheet'"
    />
    <noscript><link rel="stylesheet" href="/styles/non-critical.css" /></noscript>
  </head>
</html>
```

### 2.2 提取关键 CSS 的工具

```bash
# Critical
npx critical src/index.html --base dist/ --inline true

# Penthouse
npx penthouse https://example.com > critical.css

# Critters（Webpack 插件）
# critters-webpack-plugin 自动内联关键 CSS
```

### 2.3 内联大小控制

```
推荐关键 CSS 大小: < 14 KB（TCP 初始拥塞窗口）
超过 14 KB: 需要额外 RTT，反而降低性能
```

## 3. 异步加载 CSS

### 3.1 preload + onload 模式

```html
<link
  rel="preload"
  href="/styles/main.css"
  as="style"
  onload="this.onload=null;this.rel='stylesheet'"
/>
<noscript><link rel="stylesheet" href="/styles/main.css" /></noscript>
```

### 3.2 media 属性条件加载

```html
<!-- 仅在打印时加载 -->
<link rel="stylesheet" href="/styles/print.css" media="print" />

<!-- 仅在宽屏时加载 -->
<link rel="stylesheet" href="/styles/wide.css" media="(min-width: 1024px)" />

<!-- 仅在暗色模式时加载 -->
<link rel="stylesheet" href="/styles/dark.css" media="(prefers-color-scheme: dark)" />
```

### 3.3 使用 loadCSS 库

```html
<script>
  /*! loadCSS rel=preload polyfill. [c]2017 Filament Group, Inc. MIT License */
  (function (w) {
    'use strict';
    if (!w.loadCSS) {
      w.loadCSS = function () {};
    }
    var rp = (loadCSS.relpreload = {});
    rp.support = (function () {
      var ret;
      try {
        ret = w.document.createElement('link').relList.supports('preload');
      } catch (e) {
        ret = !1;
      }
      return function () {
        return ret;
      };
    })();
    rp.bindMediaToggle = function (link) {
      var finalMedia = link.media || 'all';
      link.addEventListener('load', function () {
        link.media = finalMedia;
      });
      link.media = 'only x';
    };
    rp.poly = function () {
      if (rp.support()) {
        return;
      }
      var links = w.document.getElementsByTagName('link');
      for (var i = 0; i < links.length; i++) {
        var link = links[i];
        if (
          link.rel === 'preload' &&
          link.getAttribute('as') === 'style' &&
          !link.getAttribute('data-loadcss')
        ) {
          link.setAttribute('data-loadcss', true);
          rp.bindMediaToggle(link);
        }
      }
    };
    if (!rp.support()) {
      rp.poly();
      var run = w.setInterval(rp.poly, 500);
      w.addEventListener('load', function () {
        rp.poly();
        w.clearInterval(run);
      });
    }
    if (typeof exports !== 'undefined') {
      exports.loadCSS = loadCSS;
    } else {
      w.loadCSS = loadCSS;
    }
  })(typeof global !== 'undefined' ? global : this);
</script>
```

## 4. 选择器性能优化

### 4.1 选择器匹配方向

浏览器从**右到左**匹配选择器：

```css
/* 浏览器先找所有 .title，再检查是否在 .card 内 */
.card .title {
  color: #333;
}

/* 更高效：直接匹配 */
.card-title {
  color: #333;
}
```

### 4.2 选择器效率排序

从高到低：

```
1. ID 选择器        #header
2. 类选择器         .card
3. 标签选择器       div
4. 相邻兄弟选择器   h2 + p
5. 子选择器         ul > li
6. 后代选择器       ul li
7. 通配选择器       *
8. 属性选择器       [type="text"]
9. 伪类/伪元素      :hover, ::before
```

### 4.3 优化建议

```css
/* 避免 */
div ul li a span {
  color: red;
}
*:not(:empty) {
  margin: 0;
}

/* 推荐 */
.nav-link-text {
  color: red;
}
```

## 5. 渲染性能优化

### 5.1 触发重排的属性

修改以下属性会触发重排（Layout），代价最高：

```
width, height, margin, padding, border-width,
top, right, bottom, left, position,
display, float, clear, font-size, line-height,
text-align, white-space, overflow
```

### 5.2 触发重绘的属性

修改以下属性只触发重绘（Paint），代价中等：

```
color, background, border-color, border-style,
outline, visibility, box-shadow, text-decoration
```

### 5.3 仅触发合成的属性

修改以下属性只触发合成（Composite），代价最低：

```
transform, opacity, filter
```

### 5.4 will-change 提示

```css
/* 提前告知浏览器哪些属性会变化 */
.card:hover {
  will-change: transform;
}

/* 动画结束后移除 */
.card {
  transition: transform 0.3s;
}

.card:hover {
  transform: scale(1.05);
}
```

> 不要滥用 `will-change`，过多声明会消耗 GPU 内存。

### 5.5 contain 属性

```css
.sidebar {
  contain: layout style paint;
  /* 或使用简写 */
  contain: strict; /* 等于 size layout style paint */
  contain: content; /* 等于 layout style paint */
}
```

| 值            | 说明                         |
| ------------- | ---------------------------- |
| `layout`      | 元素布局不影响外部           |
| `style`       | 计数器、引用不影响外部       |
| `paint`       | 子元素不会绘制到元素边界之外 |
| `size`        | 元素尺寸不依赖子元素         |
| `inline-size` | 行内方向尺寸不依赖子元素     |

### 5.6 content-visibility

```css
.below-fold-section {
  content-visibility: auto;
  contain-intrinsic-size: 0 500px; /* 预估高度 */
}
```

`content-visibility: auto` 让浏览器跳过屏幕外元素的渲染，直到它们即将进入视口。可显著提升长页面初始渲染速度。

## 6. CSS 体积优化

### 6.1 PurgeCSS 移除未使用样式

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('@fullhuman/postcss-purgecss')({
      content: ['./src/**/*.html', './src/**/*.vue', './src/**/*.jsx'],
      defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
      safelist: [/^is-/, /^has-/], // 保留动态类名
    }),
  ],
};
```

### 6.2 压缩 CSS

```bash
# 使用 cssnano
npx postcss styles.css -u cssnano -o styles.min.css
```

### 6.3 减少重复

```css
/* 避免 */
.btn-primary {
  background: #007bff;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}
.btn-secondary {
  background: #6c757d;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}

/* 推荐：提取公共样式 */
.btn {
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}
.btn-primary {
  background: #007bff;
}
.btn-secondary {
  background: #6c757d;
}
```

## 动手试试

1. 用 Performance 面板找出“样式重算”耗时最高的页面；
2. 把高频动画从布局属性改为 transform/opacity；
3. 用 `content-visibility: auto` 优化长列表；
4. 进阶挑战：用 Lighthouse 对比优化前后的 Performance 分数。

## 核心知识点

> 一句话记住 CSS 性能：避免重排（layout）、减少重绘（paint）、动画走合成层（transform/opacity）、样式尽量静态。

- 选择器性能：避免深层后代与通配符；
- 重排触发：布局属性（width/left）高频改动；
- 合成层：transform/opacity 不触发布局；
- `will-change` 预声明；
- `content-visibility` 跳过屏外渲染；
- 样式量：压缩、去冗余、拆分关键 CSS。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 动画改布局属性 | 每帧重排 | transform/opacity |
| 滥用 will-change | 内存占用 | 只对确实动画的元素 |
| 选择器过深 | 匹配慢 | 类名扁平化 |
| 忽略长列表 | 渲染卡顿 | content-visibility 或虚拟列表 |

## 扩展学习

- 渲染路径：`css/060-CriticalRenderPathOptimization`；
- 指标：`javascript/050-CoreWebVitalsAndPerformanceMetrics`；
- 动画：`css/028-CSSAnimationTransition`。

<!-- ============ 文档分隔线：007-css/043-CSSArchitectureMethodology.md ============ -->

> 阅读建议：适合有项目经验后再读，0 基础可先跳过。

## 1. BEM — Block Element Modifier

### 1.1 核心概念

BEM 由 Yandex 提出，通过严格的命名约定消除样式冲突：

| 概念     | 说明                 | 命名格式           |
| -------- | -------------------- | ------------------ |
| Block    | 独立的功能块         | `.block`           |
| Element  | Block 的组成部分     | `.block__element`  |
| Modifier | Block/Element 的变体 | `.block--modifier` |

```html
<!-- Block -->
<div class="card">
  <!-- Element -->
  <div class="card__header">
    <h2 class="card__title">标题</h2>
  </div>
  <div class="card__body">
    <p class="card__text">内容</p>
  </div>
  <!-- Modifier -->
  <button class="card__button card__button--primary">确认</button>
  <button class="card__button card__button--secondary">取消</button>
</div>

<!-- Block Modifier -->
<div class="card card--featured">
  <div class="card__header">
    <h2 class="card__title">精选标题</h2>
  </div>
</div>
```

```css
/* Block */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
}

/* Element */
.card__header {
  padding: 16px;
  border-bottom: 1px solid #eee;
}
.card__title {
  font-size: 18px;
  font-weight: 600;
}
.card__body {
  padding: 16px;
}
.card__text {
  color: #333;
  line-height: 1.6;
}
.card__button {
  padding: 8px 16px;
  border-radius: 4px;
}

/* Modifier */
.card--featured {
  border-color: gold;
  box-shadow: 0 0 12px rgba(255, 215, 0, 0.3);
}
.card__button--primary {
  background: #007bff;
  color: white;
}
.card__button--secondary {
  background: #6c757d;
  color: white;
}
```

### 1.2 BEM 命名变体

| 风格      | 示例                                    | 使用者     |
| --------- | --------------------------------------- | ---------- |
| 经典      | `.block__element--modifier`             | Yandex     |
| 两连字符  | `.block-element-modifier`               | 简化版     |
| CamelCase | `.blockName__elementName--modifierName` | React 社区 |

### 1.3 BEM 优缺点

**优点**：

- 命名自解释，无需查看 HTML 结构
- 扁平选择器，无特异性战争
- 模块化，Block 可复用

**缺点**：

- 类名冗长
- 嵌套 Block 时命名困难
- 严格规则增加编写成本

## 2. OOCSS — Object-Oriented CSS

### 2.1 核心原则

OOCSS 由 Nicole Sullivan 提出，两大原则：

**原则一：结构与皮肤分离**

```css
/* 结构 */
.btn {
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

/* 皮肤 */
.btn-primary {
  background: #007bff;
  color: white;
  border: none;
}
.btn-danger {
  background: #dc3545;
  color: white;
  border: none;
}
.btn-outline {
  background: transparent;
  border: 1px solid #007bff;
  color: #007bff;
}
```

```html
<button class="btn btn-primary">确认</button>
<button class="btn btn-danger">删除</button>
<button class="btn btn-outline">取消</button>
```

**原则二：容器与内容分离**

```css
/* 错误：内容依赖容器 */
.sidebar .title {
  font-size: 14px;
  color: #666;
}

/* 正确：内容独立于容器 */
.title-secondary {
  font-size: 14px;
  color: #666;
}
```

```html
<!-- 同一样式可在不同容器中复用 -->
<div class="sidebar">
  <h3 class="title-secondary">侧边栏标题</h3>
</div>
<div class="footer">
  <h3 class="title-secondary">页脚标题</h3>
</div>
```

### 2.2 OOCSS 实战模式

```css
/* 通用媒体对象 */
.media {
  display: flex;
  align-items: flex-start;
}
.media__figure {
  margin-right: 16px;
}
.media__body {
  flex: 1;
}

/* 皮肤变体 */
.media--reverse {
  flex-direction: row-reverse;
}
.media--reverse .media__figure {
  margin-right: 0;
  margin-left: 16px;
}
```

```html
<div class="media">
  <img class="media__figure" src="avatar.jpg" alt="" />
  <div class="media__body">
    <p>内容</p>
  </div>
</div>
```

### 2.3 OOCSS 优缺点

**优点**：复用性极强，CSS 体积小
**缺点**：HTML 类名多，需设计抽象能力

## 3. SMACSS — Scalable and Modular Architecture for CSS

### 3.1 五大分类

| 分类   | 前缀     | 说明         | 示例                       |
| ------ | -------- | ------------ | -------------------------- |
| Base   | 无       | 元素默认样式 | `body`, `a`                |
| Layout | `l-`     | 页面布局结构 | `l-header`, `l-sidebar`    |
| Module | 无       | 可复用组件   | `.card`, `.nav`            |
| State  | `is-`    | 状态样式     | `.is-active`, `.is-hidden` |
| Theme  | `theme-` | 主题覆盖     | `.theme-dark`              |

### 3.2 Base 规则

```css
/* reset/normalize 层 */
*,
*::before,
*::after {
  box-sizing: border-box;
}
body {
  margin: 0;
  font-family: system-ui, sans-serif;
  line-height: 1.6;
}
a {
  color: #007bff;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
```

### 3.3 Layout 规则

```css
.l-page {
  display: grid;
  grid-template-columns: 240px 1fr;
  min-height: 100vh;
}
.l-header {
  grid-column: 1 / -1;
  padding: 16px;
}
.l-sidebar {
  padding: 16px;
  border-right: 1px solid #eee;
}
.l-main {
  padding: 24px;
}
.l-footer {
  grid-column: 1 / -1;
  padding: 16px;
}
```

### 3.4 Module 规则

```css
/* Module 独立于 Layout */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
}
.card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.card__content {
  padding: 16px;
}
.card__title {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 8px;
}
```

### 3.5 State 规则

```css
/* 状态类覆盖 Module 的默认样式 */
.is-active {
  font-weight: 700;
  color: #007bff;
}
.is-hidden {
  display: none;
}
.is-collapsed {
  height: 0;
  overflow: hidden;
}
.is-loading {
  opacity: 0.5;
  pointer-events: none;
}
.is-disabled {
  cursor: not-allowed;
  opacity: 0.6;
}
```

```html
<nav class="nav">
  <a class="nav__item is-active" href="/">首页</a>
  <a class="nav__item" href="/about">关于</a>
</nav>
```

### 3.6 Theme 规则

```css
/* 默认主题 */
:root {
  --bg-primary: #ffffff;
  --text-primary: #333333;
  --border-color: #dddddd;
}

/* 暗色主题 */
.theme-dark {
  --bg-primary: #1a1a2e;
  --text-primary: #e0e0e0;
  --border-color: #333355;
}
```

## 4. 三种方法论对比

| 维度       | BEM            | OOCSS          | SMACSS         |
| ---------- | -------------- | -------------- | -------------- |
| 核心关注   | 命名约定       | 复用与分离     | 架构分类       |
| 学习曲线   | 低             | 中             | 中             |
| 命名规范   | 严格           | 灵活           | 前缀约定       |
| 特异性控制 | 扁平，低特异性 | 扁平，低特异性 | 分层，低特异性 |
| 适用规模   | 中大型         | 中型           | 大型           |
| 工具支持   | 广泛           | 一般           | 一般           |
| 与框架兼容 | Vue/React 友好 | Tailwind 友好  | 通用           |

## 5. 现代实践

### 5.1 BEM + CSS 变量

```css
.card {
  --card-padding: 16px;
  --card-radius: 8px;
  --card-bg: #fff;

  padding: var(--card-padding);
  border-radius: var(--card-radius);
  background: var(--card-bg);
}

.card--compact {
  --card-padding: 8px;
}

.card--dark {
  --card-bg: #2d2d2d;
}
```

### 5.2 CSS Modules + BEM

```jsx
// React + CSS Modules
import styles from './Card.module.css';

function Card({ variant, children }) {
  return <div className={`${styles.card} ${styles[variant]}`}>{children}</div>;
}
```

### 5.3 混合策略

```
推荐组合:
  架构分层 → SMACSS（Base / Layout / Module / State / Theme）
  组件命名 → BEM（.block__element--modifier）
  复用抽象 → OOCSS（结构与皮肤分离）
  主题系统 → CSS 变量
```

## 动手试试

1. 为现有项目画一张样式架构图：reset、基础、组件、工具分层；
2. 用 BEM 重构一个组件的类名；
3. 用 `@layer` 声明分层并验证覆盖；
4. 进阶挑战：制定团队 CSS 规范（命名、分层、lint）。

## 核心知识点

> 一句话记住 CSS 架构：分层（reset/基础/组件/工具）+ 命名规范（BEM）+ 工具链（lint/变量），让样式可预测、可维护。

- 分层：reset、设计令牌、基础、组件、工具类；
- 命名：BEM/OOCSS/原子化，团队统一；
- 设计令牌：颜色/间距/字号走变量；
- 工具链：Stylelint、Prettier、PostCSS；
- 覆盖策略：`@layer` 优于 `!important`；
- 文档化组件样式入口。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 无分层 | 覆盖全靠 !important | 建立 @layer 体系 |
| 命名混乱 | 样式不可预测 | 统一 BEM |
| 魔法值泛滥 | 改版困难 | 设计令牌 |
| 无 lint | 风格漂移 | 接入 Stylelint |

## 扩展学习

- BEM：`css/057-BEMNamingMethodology`；
- @layer：`css/039-CascadeLayer`；
- 变量：`css/035-CSSVariableCustomAttribute`。

<!-- ============ 文档分隔线：007-css/044-TypographyAndGridSystem.md ============ -->

## 一句话理解

排版系统 = 一套**有规律的数值**：字号阶梯（type scale）、行高、间距与网格。
它让不同页面看起来同属一个产品，而不是每个页面各自"发挥"。

## 为什么需要

- 随手选的字号与间距，在滚动阅读时会显得杂乱。
- 设计令牌（CSS 变量）让全局改字号、改间距只需改一处。
- 响应式页面里，字号阶梯配合 `clamp()` 能平滑过渡。

## 核心概念

**1. 字号阶梯（Type Scale）**

以正文为基准，按固定比例放大/缩小：

```css
:root {
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px 基准 */
  --text-lg: 1.25rem;   /* 20px */
  --text-xl: 1.5rem;    /* 24px */
  --text-2xl: 2rem;     /* 32px */
}
```

**2. 行高与垂直节奏**

行高也走同一套数字，让相邻文本块的间距看起来稳定：

```css
:root {
  --leading-tight: 1.25;
  --leading-normal: 1.6;
  --leading-loose: 1.8;
  --space-1: 4px;
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
}
```

**3. 8pt 间距体系**

间距只取 4 或 8 的倍数（`4/8/16/24/32/48`），
元素之间的缝隙在视觉上有明确的层级，不会出现"3px 还是 5px"的选择困难。

## 落地示例

```css
/* 响应式字号：随视口平滑变化，且不超出上下限 */
.page-title {
  font-size: clamp(1.5rem, 1.2rem + 1.6vw, 2.5rem);
  line-height: var(--leading-tight);
}

.page-body {
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  /* 段落间距与 8pt 体系对齐 */
  margin-block: var(--space-4);
}

.card {
  padding: var(--space-4);
  gap: var(--space-3);
}
```

## 文本装饰与对齐

排版系统除了字号与行高，还包含文本的对齐与装饰属性：

```css
.quote {
  text-align: center;        /* left/center/right/justify */
  text-transform: uppercase; /* 大小写转换 */
  text-decoration: underline;
  letter-spacing: 0.05em;    /* 字间距 */
  word-spacing: 0.1em;       /* 词间距 */
  text-indent: 2em;          /* 首行缩进 */
}
```

**讲解：**

- `text-align` 控制行内内容对齐；`justify` 两端对齐需注意中文断行；
- `text-decoration` 可组合 `underline`/`line-through`/`overline`，`text-decoration-color` 单独调色；
- `text-transform` 只改变显示（`uppercase`/`lowercase`/`capitalize`），不改变源码文本；
- `letter-spacing`/`word-spacing` 微调字距与词距，标题常用小幅字距；
- 垂直方向用 `vertical-align` 控制行内元素基线对齐（`middle`/`baseline`/`super` 等）。

**中文排版补充：**

- 中文正文推荐 `text-align: justify` 两端对齐，并配合 `text-justify: inter-ideograph` 处理标点；
- 中文标点（逗号、句号）不应出现在行首，浏览器自动处理；需要更精细控制时设置 `hanging-punctuation`（支持有限）；
- 中文正文字号建议 ≥ 16px，行高 1.6-1.8，比英文略宽；
- 全角与半角：中文内容用全角标点，代码与英文单词保持半角。

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 标题越大越好 | 字号阶梯保证层级关系，标题与正文的比例比绝对大小更重要 |
| 行高越宽松越好 | 正文 1.5-1.7 合适，标题用紧凑行高，避免留白失衡 |
| 间距随手填 | 间距来自同一数值体系，视觉才统一 |
| 只用 px 固定字号 | 用 rem 基准 + clamp() 兼顾可访问性与响应式 |
| 文本装饰乱用 | 下划线只用于链接，正文装饰用 color/weight 表达 | 用语义类与设计令牌统一 |

## 小结

排版系统的本质是"约束"：字号、行高、间距都从有限的数值集合里取值。
先用 CSS 变量把阶梯定义出来，再让所有组件消费变量，页面自然会整齐。
下一步可结合 `css/035-CSSVariableCustomAttribute` 做主题化扩展。

## 动手试试

1. 用变量定义字号阶梯与间距体系，改造一个页面；
2. 用 `clamp()` 做响应式标题字号；
3. 用 8pt 网格统一组件间距；
4. 进阶挑战：给项目写一份排版规范文档。

## 核心知识点

> 一句话记住排版系统：字号阶梯 + 行高 + 间距体系 + 网格对齐，全部走设计令牌；约束即秩序。

- 字号阶梯：基准 1rem 等比放大；
- 行高：正文 1.5-1.7、标题紧凑；
- 间距体系：8pt 倍数（--space-1..8）；
- 网格：列宽、沟槽、外边距统一；
- `clamp()` 响应式字号；
- 文本对齐与装饰统一规范。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 字号随手填 | 页面杂乱 | 只用阶梯变量 |
| 行高失衡 | 阅读困难 | 正文 1.5+ |
| 间距魔法值 | 无法统一 | 间距变量 |
| 忽略中文排版 | 标点悬挂异常 | 参考中文排版规范 |

## 扩展学习

- 字体加载：`css/047-CSSFontLoading`；
- 文本装饰：`css/044-TypographyAndGridSystem` 的文本章节；
- 设计令牌：`css/035-CSSVariableCustomAttribute`。

<!-- ============ 文档分隔线：007-css/045-AccessibleStyling.md ============ -->

## 一句话理解

可访问性样式 = 让信息不依赖"视力、听力、精细动作或快速反应"也能被获取：
重点管好对比度、焦点、动效和文本缩放四件事。

## 为什么需要

- 全球约 15% 的人存在某种障碍，低对比度、无焦点、闪烁动效都在制造障碍。
- 无障碍也是工程指标：键盘可达、对比达标，往往让所有用户都更好用。
- 很多问题只是几行 CSS 的事，成本极低。

## 四件事

**1. 对比度**

正文与背景的对比度建议达到 4.5:1（大字号可放宽到 3:1）。

```css
/* 用浅色文字时检查对比度，不要只凭"看得清"判断 */
.muted {
  color: #6b7280; /* 在白色背景上约 4.6:1，正文可用 */
}

.muted-sm {
  color: #9ca3af; /* 约 2.5:1，只适合装饰性内容 */
}
```

**2. 焦点可见**

永远不要裸写 `outline: none`。去掉默认焦点框时，必须提供自定义样式：

```css
.btn:focus-visible {
  outline: 2px solid var(--color-accent-base);
  outline-offset: 2px;
}
```

`:focus-visible` 只在键盘导航时显示焦点框，鼠标点击不打扰，是当前最佳实践。

**3. 减少动效**

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

更克制但更精细的做法：只在用户偏好减少动效时，把大位移动画改为透明度过渡。

**4. 文本缩放**

```css
html {
  /* 允许用户自定义浏览器字号生效，而不是锁死 px */
  font-size: 100%;
}

body {
  font-size: 1rem; /* 跟随根字号 */
}

/* 内容容器不要写死高度，防止放大后文字被裁切 */
.card {
  min-height: 0;
}
```

## 检查清单

- 页面能否只用 Tab + Enter 完整操作？
- 所有交互元素在键盘聚焦时有可见指示？
- 正文对比度 ≥ 4.5:1，错误提示不只靠颜色区分？
- 浏览器放大到 200% 或只改字号后，内容不重叠、不裁切？
- 动效有 `prefers-reduced-motion` 降级？

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 无障碍是给残障人士的 | 临时受伤、老人、弱网、强光环境都受益 |
| 颜色对比"看着还行"就行 | 用工具测量（如 Lighthouse、axe）而非目测 |
| 只用颜色传达状态 | 状态必须叠加图标/文字等非颜色线索 |
| 焦点框很丑所以去掉 | 用 `:focus-visible` 兼顾美观与可用 |

## 小结

可访问性样式没有魔法，就是四条纪律：对比度达标、焦点可见、动效可降级、文字可缩放。
配合 HTML 无障碍 的结构语义，就能覆盖绝大多数障碍场景。

## 动手试试

1. 用对比度检查工具验证你的页面配色；
2. 给交互元素补 `:focus-visible` 样式；
3. 用 `prefers-reduced-motion` 关闭装饰动画；
4. 进阶挑战：用键盘走查整个页面并修复焦点问题。

## 核心知识点

> 一句话记住可访问性样式：对比度达标、焦点可见、动效可关、缩放不破坏；样式服务于所有用户。

- 对比度：正文 4.5:1、大文本 3:1（AA）；
- 焦点：`:focus-visible` 可见描边；
- 动效：尊重 `prefers-reduced-motion`；
- 缩放：rem 单位，200% 缩放不破坏；
- 语义：样式不删除语义（列表、标题）；
- 颜色：不单独靠颜色传达信息。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 移除 focus 样式 | 键盘迷失 | 保留可见焦点 |
| 对比度不足 | 低视力看不清 | 按 AA 验证 |
| 无限动画 | 干扰阅读 | reduced-motion 关闭 |
| 只靠颜色表达状态 | 色觉障碍 | 图标/文字辅助 |

## 扩展学习

- 无障碍完整教程：`html5/010-Accessibility`；
- 动效：`css/028-CSSAnimationTransition`；
- 深色主题：`css/031-MediaQuery`。

<!-- ============ 文档分隔线：007-css/046-CSSCounters.md ============ -->

## 0. 直觉：让浏览器替你“数数”

写文档时手动编号“第 1 章、第 2 章……”，插入一章后全部要改——CSS 计数器就是“自动计数牌”：定义一个计数器，每遇到一个元素就加 1，再把这个数显示出来。

三个关键词：`counter-reset`（初始化）、`counter-increment`（递增）、`counter()`（读出数值）。它和 `<ol>` 的自动编号原理相同，但可以显示在标题、列表项甚至任意元素上。

## 1. 核心用法

### 1.1 自动章节编号

```css
.doc {
  counter-reset: chapter; /* 初始化计数器 */
}
.doc h2::before {
  counter-increment: chapter; /* 每个 h2 加 1 */
  content: "第 " counter(chapter) " 章：";
}
```

```html
<div class="doc">
  <h2>起步</h2>  <!-- 第 1 章：起步 -->
  <h2>进阶</h2>  <!-- 第 2 章：进阶 -->
</div>
```

**讲解：**

- `counter-reset: chapter` 在容器上把计数器归零；
- `counter-increment` 递增，`counter(chapter)` 读出当前值；
- 编号由 CSS 生成，增删章节无需改 HTML。

### 1.2 嵌套编号：counters()

```css
.doc {
  counter-reset: section;
}
.doc h2 {
  counter-reset: subsection;
}
.doc h2::before {
  counter-increment: section;
  content: counter(section) ". ";
}
.doc h3::before {
  counter-increment: subsection;
  content: counter(section) "." counter(subsection) " ";
}
```

```html
<div class="doc">
  <h2>HTML</h2>
  <h3>标签</h3>   <!-- 1.1 标签 -->
  <h3>属性</h3>   <!-- 1.2 属性 -->
  <h2>CSS</h2>
  <h3>选择器</h3> <!-- 2.1 选择器 -->
</div>
```

**讲解：** 每层标题都有自己“归零 + 递增”的计数器；`counters(name, ".")` 还能一次性输出多层编号（如 `1.2.3`），适合多级列表。

### 1.3 列表计数

```css
ol {
  counter-reset: item;
  list-style: none;
}
ol li::before {
  counter-increment: item;
  content: counter(item, upper-roman) ". "; /* 用罗马数字格式 */
}
```

**讲解：** 把 `<ol>` 的原生编号隐藏（`list-style: none`），用 `::before` + 计数器自定义编号格式，实现“中文序号”“带括号序号”等效果。

### 1.4 计数器格式

```css
content: counter(item);                 /* 1, 2, 3 */
content: counter(item, upper-roman);    /* I, II, III */
content: counter(item, lower-alpha);    /* a, b, c */
content: counters(item, "-");           /* 1-1, 1-2 */
```

**讲解：** `counter()` 的第二个参数是编号样式，与 `list-style-type` 的取值一致；`counters(name, 连接符)` 用于嵌套层级。

## 2. 动手试试

1. 给一篇“三步教程”的 `h2` 加自动章节编号；
2. 实现“1.1 / 1.2”式的二级编号；
3. 把 `<ol>` 改成 `① ② ③` 样式（用计数器 + `::before`）；
4. 进阶挑战：用 `counters()` 实现多级目录编号。

提示：第 3 步除了 `counter(item)`，编号格式还可以用 `cjk-ideographic`（一、二、三）。骨架参考：

```css
ol {
  counter-reset: item;
  list-style: none;
}
ol li::before {
  counter-increment: item;
  content: counter(item) ". "; /* 先跑通数字版，再换其它格式 */
}
```

## 3. 核心知识点

> 一句话记住计数器：`counter-reset` 归零，`counter-increment` 加一，`counter()` 显示；嵌套用 `counters()`，格式参数同列表样式。

- 三步曲：reset（初始化）、increment（递增）、counter()（输出）；
- `counter()` 第二参数控制编号格式（罗马、字母等）；
- `counters(name, sep)` 输出多层编号；
- 常与 `::before` + `content` 配合显示；
- 编号由 CSS 生成，内容与样式分离；
- 适合章节、图注、自定义列表编号。

## 4. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 reset | 编号从上一个容器继续 | 每个作用域容器 reset |
| 计数元素非兄弟 | 编号混乱 | 确保 increment 与 reset 作用域匹配 |
| 用 JS 手写编号 | 增删后不同步 | 交给 CSS 计数器 |
| 与 `list-style` 混用 | 出现双编号 | 先 `list-style: none` |
| 依赖 `content` 做文本内容 | 读屏可能重复播报 | 纯装饰编号无碍，正文内容仍放 HTML |

## 5. 扩展学习

- 伪元素：`css/023-PseudoClassPseudoElement`（`::before`/`content`）；
- 列表样式：`css/017-CSSListStyle`；
- 选择器：`css/007-CSS3SelectorSystem`；
- 内容生成：`css/053-Function` 中 `counter()` 函数。

<!-- ============ 文档分隔线：007-css/047-CSSFontLoading.md ============ -->

## 0. 直觉：网页字体是“下载来的”

系统字体（Arial、微软雅黑）随操作系统自带；品牌字体（如思源黑体、自定义字库）需要从服务器下载。`@font-face` 就是“字体说明书”：告诉浏览器字体文件在哪、叫什么名字、属于哪种字重。

字体加载有个经典问题：字体没下载完时，文字可能“隐形”（FOIT）。`font-display: swap` 就是解决方案——先用系统字体显示，字体就绪后再切换。

## 1. 核心用法

### 1.1 @font-face 基本语法

```css
@font-face {
  font-family: "MyFont";
  src: url("myfont.woff2") format("woff2"),
       url("myfont.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: "MyFont", system-ui, sans-serif;
}
```

**讲解：**

- `font-family` 是给字体起的名字，供后续 `font-family` 引用；
- `src` 列出字体文件，现代浏览器优先 `woff2`（体积最小）；
- `font-weight`/`font-style` 声明这份文件对应的字重与样式；
- 多个字重需要多个 `@font-face` 块（400/700 各一份）。

### 1.2 font-display 四种策略

```css
@font-face {
  font-family: "MyFont";
  src: url("myfont.woff2") format("woff2");
  font-display: swap;      /* 先用系统字体，加载完再换（推荐） */
  /* font-display: block;  */  /* 等待期文字隐藏（FOIT） */
  /* font-display: fallback; */ /* 短等待 + 3 秒内不换 */
  /* font-display: optional; */ /* 极短等待，慢网络直接不换 */
}
```

**讲解：** `swap` 是平衡“品牌一致性”与“可读性”的默认选择；`optional` 对弱网最友好（加载太慢就放弃字体）；`block` 会延迟文字显示，不推荐用于正文。

### 1.3 预加载与性能

```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin />
```

**讲解：** `preload` 让字体在 CSS 解析前就开始下载，减少文字切换延迟；`crossorigin` 必须带上，否则字体请求可能被 CORS 拦截。字体子集化（只打包用到的字符）能进一步减小体积。

## 2. 动手试试

1. 下载一个开源字体（如思源黑体子集），用 `@font-face` 注册并应用到标题；
2. 对比 `font-display: swap` 与 `block` 在慢速网络下的文字表现（Network 面板限速）；
3. 给字体加 `preload`，观察首屏文字出现时间；
4. 进阶挑战：用 `unicode-range` 做字体子集拆分。

## 3. 核心知识点

> 一句话记住字体加载：`@font-face` 注册字体文件，`font-display: swap` 防隐形文字，`preload` 提前下载，`woff2` 体积最小。

- `@font-face`：`font-family` + `src` + 字重/样式声明；
- 多字重需要多个 `@font-face` 块；
- `font-display`：`swap` 推荐、`block` 会隐形、`optional` 弱网友好；
- `preload` + `crossorigin` 提前下载字体；
- `woff2` 是体积最小的现代格式；
- `unicode-range` 可按字符集拆分，减小加载量；
- 提供系统字体回退：`font-family: "MyFont", system-ui, sans-serif`。

## 4. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 `font-display` | 文字隐形（FOIT） | 使用 `font-display: swap` |
| 只加载一种字重 | 加粗时浏览器伪造 | 注册 400/700 两份字体 |
| 字体文件过大 | 首屏变慢 | 子集化 + `woff2` + `unicode-range` |
| preload 缺 `crossorigin` | 字体被 CORS 拦截 | 补上 `crossorigin` 属性 |
| 无系统字体回退 | 字体加载失败页面难看 | 回退链：自定义字体 → system-ui → sans-serif |

## 5. 扩展学习

- 排版体系：`css/044-TypographyAndGridSystem`；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`、`html5/037-CriticalRenderingPathAndResourceLoading`；
- 字体格式：woff2/woff/ttf 的兼容矩阵；
- 字体转换工具：Font Squirrel Webfont Generator（生成多格式并子集化）、Google Fonts CSS2 API 的子集参数；
- 资源预加载：`html5/006-HTML5OverviewCoreFeature` 的 preload 章节。

<!-- ============ 文档分隔线：007-css/048-CSSFilters.md ============ -->

## 0. 直觉：给元素加“滤镜”

滤镜是给元素加的一层“后期处理”：照片应用里的模糊、黑白、饱和度调节，在 CSS 里就是 `filter` 属性的几个函数。

```css
img {
  filter: grayscale(100%); /* 一键变黑白 */
}
```

`filter` 只影响视觉显示，不修改原图数据；可叠加多个函数，如 `filter: brightness(1.2) contrast(1.1)`。

## 1. 核心函数

### 1.1 常用函数一览

```css
.blur {
  filter: blur(4px);              /* 高斯模糊 */
}
.bright {
  filter: brightness(1.2);        /* 亮度，1 为原始值 */
}
.contrast {
  filter: contrast(1.5);          /* 对比度 */
}
.gray {
  filter: grayscale(100%);        /* 黑白 */
}
.sepia {
  filter: sepia(0.8);             /* 复古棕 */
}
.hue {
  filter: hue-rotate(90deg);      /* 色相旋转 */
}
.saturate {
  filter: saturate(200%);         /* 饱和度 */
}
.invert {
  filter: invert(100%);           /* 反色 */
}
.opacity {
  filter: opacity(50%);           /* 透明度（与 opacity 属性等价） */
}
.shadow {
  filter: drop-shadow(2px 4px 6px rgba(0, 0, 0, 0.4)); /* 跟随形状的投影 */
}
```

**讲解：**

- 十个函数：`blur`/`brightness`/`contrast`/`grayscale`/`sepia`/`hue-rotate`/`saturate`/`invert`/`opacity`/`drop-shadow`；
- 大部分函数接受百分比或 0-1 数值（`100%` 等价于 `1`）；
- `drop-shadow` 与 `box-shadow` 的区别：它跟随元素的实际形状（含透明区域），适合 PNG 图标；
- 多个函数用空格叠加，按顺序生效。

### 1.2 组合应用

```css
.dark-theme-img {
  filter: brightness(0.8) contrast(1.1) saturate(1.2);
}
.placeholder {
  filter: blur(8px) grayscale(50%);
  transition: filter 0.3s; /* 滤镜可以过渡 */
}
.placeholder:hover {
  filter: none;
}
```

**讲解：** 滤镜支持 `transition` 动画（如模糊占位图加载完成后渐变为清晰）；组合顺序会影响结果，例如先 `grayscale` 再 `hue-rotate` 与反过来效果不同。

## 2. 动手试试

1. 给一张图片依次尝试 10 个滤镜函数，观察各自效果；
2. 做“悬停变清晰”：图片默认模糊，hover 时 `filter: none` 并加过渡；
3. 用 `grayscale` + `hover` 还原实现“黑白转彩色”；
4. 进阶挑战：给不规则 PNG 图标加 `drop-shadow`，对比 `box-shadow` 的差异。

## 3. 核心知识点

> 一句话记住滤镜：`filter` 是视觉后期，`blur` 模糊、`grayscale` 黑白、`drop-shadow` 形状投影；可叠加、可过渡，不影响原图。

- 十个函数：blur、brightness、contrast、grayscale、sepia、hue-rotate、saturate、invert、opacity、drop-shadow；
- 多个函数空格叠加，顺序影响结果；
- `drop-shadow` 跟随形状，`box-shadow` 跟随盒子；
- 滤镜支持 transition 动画；
- 大面积滤镜有性能开销，动画时注意合成层；
- `filter` 会创建新的包含块（影响 `fixed` 定位），注意副作用。

## 4. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 大面积模糊 | 重绘开销大 | 缩小模糊区域或降低模糊半径 |
| 忘记 hover 还原 | 交互后样式残留 | 用 `filter: none` + transition |
| `box-shadow` 当形状投影 | PNG 图标出现方框阴影 | 用 `drop-shadow` |
| 滤镜动画频繁 | 掉帧 | 用 `will-change: filter` 或减少层级 |
| 忽略包含块副作用 | fixed 子元素定位异常 | 滤镜元素内避免依赖视口定位 |

## 5. 扩展学习

- 阴影：`css/025-Shadow`；
- 背景混合：`css/026-BackgroundEnhancement`（background-blend-mode）；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`；
- 动画：`css/028-CSSAnimationTransition` 中滤镜过渡。

<!-- ============ 文档分隔线：007-css/049-CSSObjectFit.md ============ -->

## 0. 直觉：图片放进“固定相框”怎么摆

你有一个 400x300 的相框，图片却是 800x600——直接塞进去会怎样？`object-fit` 决定答案：拉伸填满、等比缩放完整显示、还是裁剪铺满。

它作用于 `<img>`、`<video>` 等“替换元素”的内容，与背景的 `background-size: cover/contain` 思路相同，但作用于内容本身。

## 1. 核心取值

```css
.cover {
  width: 400px;
  height: 300px;
  object-fit: cover;      /* 等比缩放并裁剪铺满（推荐） */
}
.contain {
  object-fit: contain;    /* 等比缩放完整显示，留白 */
}
.fill {
  object-fit: fill;       /* 拉伸填满，可能变形（默认） */
}
.none {
  object-fit: none;       /* 原尺寸，超出裁剪 */
}
.scale-down {
  object-fit: scale-down; /* 取 none 与 contain 中较小的结果 */
}
```

**讲解：**

- `cover`：等比缩放直到铺满盒子，多余部分裁剪，适合缩略图与头像；
- `contain`：完整显示，可能上下/左右留白，适合展示完整图片；
- `fill`：强制拉伸填满，会变形，是默认值；
- `none`：按原始尺寸显示；
- `scale-down`：自动选择 `none` 或 `contain` 中更小的那个。

## 2. object-position：内容位置

```css
.avatar {
  width: 80px;
  height: 80px;
  object-fit: cover;
  object-position: top;      /* 裁剪时保留顶部 */
  /* object-position: 50% 50% 默认居中 */
}
```

**讲解：** 配合 `cover` 使用，决定裁剪时保留哪部分：人像保留 `top` 或 `center top`，全景图用 `center`。取值与 `background-position` 一致（关键词或百分比）。

## 3. 完整示例

```html
<style>
  .thumb {
    width: 200px;
    height: 150px;
    object-fit: cover;
    object-position: center;
    border-radius: 8px;
  }
</style>
<img class="thumb" src="photo.jpg" alt="缩略图" />
```

**讲解：** 这是图片列表的标准写法：固定尺寸 + `cover` 裁剪 + 圆角，任何比例的图片都能整齐展示，且无需修改图片文件。

## 4. 动手试试

1. 用同一张图片分别设置 `fill`/`contain`/`cover`/`none`，观察差异；
2. 做一个头像：80x80 圆形（`border-radius: 50%`）+ `cover`；
3. 用 `object-position: top` 让横幅图裁剪时保留人物头部；
4. 进阶挑战：给 `<video>` 也用 `object-fit: cover` 做视频封面。

## 5. 核心知识点

> 一句话记住对象适配：`cover` 裁剪铺满、`contain` 完整留白、`fill` 拉伸变形；`object-position` 定裁剪位置，头像列表首选 `cover`。

- `object-fit` 作用于 img/video 等替换元素；
- `cover` 等比裁剪铺满，`contain` 等比完整显示；
- `fill` 是默认值，会变形；
- `object-position` 配合 `cover` 控制保留区域；
- 固定尺寸容器 + `cover` 是图片列表的标准方案；
- 与 `background-size` 概念相同，但作用于内容。

## 6. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 图片变形 | 使用了默认 `fill` | 用 `cover` 或 `contain` |
| 头像裁掉人脸 | 默认居中裁剪 | `object-position: top` 保留头部 |
| 忘记设置宽高 | object-fit 无效果 | 容器必须给定尺寸 |
| 大图直接加载 | 浪费流量 | 配合响应式图片 `srcset` |
| 视频变形 | video 默认拉伸 | `object-fit: cover` |

## 7. 扩展学习

- 响应式图片：`html5/019-ImageResponsiveImage`；
- 盒模型：`css/003-CSS3BoxModelDetailed`；
- 背景适配：`css/026-BackgroundEnhancement`（background-size 对比）；
- 圆角头像：`css/051-BorderRadius`。

<!-- ============ 文档分隔线：007-css/050-CSSAnchorPositioning.md ============ -->

## 0. 直觉：让弹层“钉”在触发按钮旁边

做 tooltip、下拉菜单、气泡弹层时，传统做法是 JS 测量按钮位置再计算弹层坐标，滚动/缩放后还要重新计算。CSS 锚点定位（Anchor Positioning）让弹层直接声明“我相对哪个元素、放在哪一侧”，浏览器自动跟随。

## 1. 基本用法

```html
<button class="trigger">菜单</button>
<div class="popover">选项一 / 选项二</div>
```

```css
.trigger {
  anchor-name: --trigger;
}

.popover {
  position: absolute;
  position-anchor: --trigger;
  inset-area: bottom;   /* 放在锚点下方 */
}
```

**讲解：** 锚点元素用 `anchor-name` 命名（必须以 `--` 开头），弹层用 `position-anchor` 引用，再通过 `inset-area` 指定相对方位（`top`/`bottom`/`left`/`right` 及组合）。

## 2. inset-area 方位

```css
.tooltip {
  position: absolute;
  position-anchor: --trigger;
  inset-area: top center;       /* 上方居中 */
}
.dropdown {
  position: absolute;
  position-anchor: --trigger;
  inset-area: bottom span-right; /* 下方，向右展开 */
}
```

**讲解：** `inset-area` 的格式是“块方向 + 行内方向”：`top center` 表示顶部居中，`bottom span-right` 表示下方并向右拉伸到锚点右边缘。方向也可写成物理关键词，语义与逻辑属性一致。

## 3. 精细控制：anchor() 函数

```css
.popover {
  position: absolute;
  position-anchor: --trigger;
  left: anchor(right);        /* 左边缘对齐锚点右边缘 */
  top: anchor(bottom);        /* 上边缘对齐锚点下边缘 */
  margin-top: 8px;
}
```

**讲解：** 需要精确对齐时用 `anchor()` 函数读取锚点的物理边缘（`left`/`right`/`top`/`bottom`/`center`）作为坐标，配合 margin 形成间距；还可以用 `anchor(--other right)` 引用其它锚点。

## 4. 防溢出：position-try

```css
.popover {
  position: absolute;
  position-anchor: --trigger;
  inset-area: bottom;
  position-try-fallbacks: flip-block;   /* 下方放不下时翻到上方 */
}
```

**讲解：** `position-try-fallbacks` 提供备选方位（`flip-block`/`flip-inline`/自定义 `inset-area`），浏览器在空间不足时自动尝试下一个，弹层不再“溢出屏幕”。这是锚点定位相对 JS 方案的杀手锏。

## 5. 与弹层 API 的关系

```html
<button popovertarget="menu">菜单</button>
<div id="menu" popover class="menu">内容</div>
```

**讲解：** Popover API 负责“显示/隐藏与层级”，锚点定位负责“贴在哪里”，两者常搭配使用：`popover` 默认在顶层渲染，配合 `position-anchor` 即实现“点击按钮弹出下拉面板”，无需任何 JS。

## 6. 动手试试

1. 给按钮和 tooltip 建立锚点关系，用 `inset-area` 切换上下左右；
2. 用 `anchor()` 函数实现“弹层右边缘对齐按钮左边缘”；
3. 给弹层加 `position-try-fallbacks: flip-block`，把页面缩窄观察自动翻转；
4. 进阶挑战：用 `popover` + 锚点定位实现一个无 JS 下拉菜单。

## 7. 核心知识点

> 一句话记住锚点定位：anchor-name 命名锚点，position-anchor 引用，inset-area 定方位，position-try 防溢出。

- `anchor-name: --x` 命名锚点，`position-anchor: --x` 引用；
- `inset-area` 用“块方向 + 行内方向”描述相对方位；
- `anchor()` 函数读取锚点边缘做精细对齐；
- `position-try-fallbacks` 自动尝试备选方位，防溢出；
- 与 Popover API 搭配可实现无 JS 弹层；
- 现代浏览器支持中，使用前查 Baseline。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 浏览器不支持 | 弹层位置失效 | 保留 JS 测量方案作为回退 |
| 锚点 display:none | 引用关系失效 | 确保锚点可见或用 `anchor-default` |
| 忘记设置 position | position-anchor 无效 | 弹层必须 absolute/fixed |
| 大量弹层同用锚点 | 命名冲突 | 命名遵循组件前缀 |

## 9. 扩展学习

- 定位体系：`css/014-PositionDetailed`；
- 新特性总览：`css/064-CSSNewFeatures`；
- 层叠上下文与弹层层级：`css/016-StackingContext`；
- 可访问性样式：`css/045-AccessibleStyling`。

<!-- ============ 文档分隔线：007-css/051-BorderRadius.md ============ -->

## 1. 历史动机与发展脉络

圆角在平面设计中长期用于柔化界面。CSS 2.1 没有圆角能力，开发者只能使用背景图片（九个切片）模拟圆角，成本高且难以缩放。2005 年起 Mozilla 率先在 Firefox 中实现 `-moz-border-radius`，WebKit 随后跟进 `-webkit-border-radius`；2010 年 CSS Backgrounds and Borders Level 3 工作草案将 `border-radius` 标准化，2017 年该规范成为 W3C Recommendation。如今 `border-radius` 是支持度最完整的 CSS 属性之一。

规范演变中最重要的细节是椭圆半径与百分比：早期实现只支持长度值，百分比由 CSS3 引入，并规定了“相邻圆角重叠时等比缩小”的行为（Corners must not overlap 原则），保证任何尺寸下角部曲线都合法。

```mermaid
timeline
    title border-radius 演进
    2002 : CSS2 无圆角，使用背景图切片
    2005 : Firefox 实现 -moz-border-radius
    2007 : WebKit 实现 -webkit-border-radius
    2010 : CSS Backgrounds 3 草案标准化
    2017 : W3C Recommendation 发布
    2020+ : 所有现代浏览器无前缀支持
```

## 2. 形式化定义

`border-radius` 的正式语法：

```css
border-radius: [ <length-percentage> ]{1,4} [ / [ <length-percentage> ]{1,4} ]?
```

一至四个值的分配规则与 margin/padding 相同（顺时针）：一个值表示四角相同；两个值表示左上/右下、右上/左下；三个值表示左上、右上/左下、右下；四个值按左上、右上、右下、左下。

斜杠前为四个角的水平半径，斜杠后为垂直半径。只写一个值时垂直半径默认等于水平半径（正圆角）；写斜杠时形成椭圆角。

长写属性：

`border-top-left-radius`、`border-top-right-radius`、`border-bottom-right-radius`、`border-bottom-left-radius`。每个长写属性接受一个或两个值（水平、垂直）。

百分比解析：水平百分比相对于元素内容盒加边框盒的宽度（即边框盒宽度），垂直百分比相对于高度。因此一个 50% 的水平半径加 50% 的垂直半径在矩形元素上形成椭圆，在正方形上形成圆。

重叠收缩规则：设角半径在对应边上的投影长度之和超过边长时，所有半径按同一比例缩小。例如宽度 100px、四个角水平半径均为 60px 时，各角收缩为 50px。

```mermaid
flowchart LR
    A["border-radius: 10px"] --> B["四角相同的小圆角"]
    C["border-radius: 50%"] --> D["正方形变圆形"]
    E["border-radius: 20px / 40px"] --> F["椭圆角：水平20 垂直40"]
    G["border-radius: 10px 20px 30px 40px"] --> H["四角依次不同"]
```

## 3. 理论推导与原理解析

### 3.1 椭圆参数方程

圆角曲线是四分之一椭圆弧。设水平半径 rx、垂直半径 ry，角部曲线上的点满足椭圆参数方程：

$$ x = rx \cdot \cos\theta,\quad y = ry \cdot \sin\theta,\quad \theta \in [0, \pi/2] $$

当 rx = ry 时退化为圆弧。浏览器绘制圆角时，把该曲线光栅化为路径；背景、边框、内阴影、外阴影都沿着这条路径裁剪或扩展。

### 3.2 百分比半径与盒子尺寸

半径百分比参照边框盒。对 200px 宽、100px 高的元素，`border-radius: 50%` 产生 rx=100px、ry=50px 的椭圆角，四角连接后元素内部剩余区域呈“胶囊竖切”形状。这也是为什么 50% 只在正方形上产生正圆。

### 3.3 相邻圆角的收缩推导

设上边长为 W，左上角水平半径 r1、右上角水平半径 r2。若 r1 + r2 > W，则按比例因子 f = W / (r1 + r2) 同时缩放两角（垂直半径同比例）。该规则保证角部曲线不相交，是 CSS 规范的强制行为，开发者无法覆盖。

## 4. 代码示例（带详尽注释）

### 4.1 基础圆角

```css
.card {
  /* 四个角统一 12px 圆角 */
  border-radius: 12px;
}

.badge {
  /* 水平/垂直半径一致，形成正圆角 */
  border-radius: 50%;
  width: 48px;
  height: 48px;
}
```

讲解：`12px` 是卡片圆角的中性值；`50%` 配合正方形宽高形成圆形，是头像、状态点的标准写法。

### 4.2 胶囊按钮

```css
.pill-button {
  /* 水平半径取高度一半（需要与高度联动） */
  border-radius: 999px;
  padding: 8px 24px;
  background: #1677ff;
  color: #fff;
  border: none;
}
```

讲解：`999px` 是“足够大”的半径，浏览器会自动收缩到高度一半，形成胶囊形状。该写法无需精确计算高度，是弹性高度的推荐方案。

### 4.3 椭圆角与局部圆角

```css
.dialog {
  /* 水平 16px、垂直 32px：顶部更“圆”的椭圆角 */
  border-radius: 16px / 32px;
}

.tab {
  /* 只圆顶部两角：贴合标签页设计 */
  border-radius: 10px 10px 0 0;
}

.speech-bubble {
  /* 左上角小圆角，其余角大圆角：聊天气泡 */
  border-radius: 4px 16px 16px 16px;
}
```

讲解：`border-radius` 的四值顺序是左上、右上、右下、左下。聊天气泡的典型处理是“指向源头的一角更尖”。

### 4.4 与 overflow 配合裁剪图片

```html
<div class="avatar-frame">
  <img src="avatar.jpg" alt="用户头像">
</div>
```

```css
.avatar-frame {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  /* 关键：溢出裁剪，让图片跟随圆角 */
  overflow: hidden;
}
.avatar-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

讲解：`border-radius` 只作用于元素自身的背景与边框，不会自动裁剪子内容；必须配合 `overflow: hidden` 才能让图片呈现圆形。`object-fit: cover` 保证图片不变形地填满。

### 4.5 响应式椭圆

```css
.ellipse {
  /* 宽度百分比半径：随容器宽度变化 */
  border-radius: 50% / 25%;
  aspect-ratio: 2 / 1;
  background: linear-gradient(135deg, #36cfc9, #1677ff);
}
```

讲解：`50% / 25%` 表示水平半径是宽度一半、垂直半径是高度四分之一。配合 `aspect-ratio` 固定宽高比，可以构造稳定的椭圆装饰。

### 4.6 圆角与阴影/边框的配合

```css
.elevated {
  border: 2px solid #d9d9d9;
  border-radius: 16px;
  /* 阴影形状跟随圆角路径 */
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}
```

讲解：`box-shadow` 与 `border-radius` 共享同一路径计算，阴影自动贴合圆角。但注意：`outline` 在旧浏览器中不贴合圆角；现代浏览器（Chrome 94+、Firefox 88+）的 `outline` 已跟随圆角。

### 4.7 设计令牌管理

```css
:root {
  /* 圆角梯度令牌：小、中、大、全圆 */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 999px;
}

.button { border-radius: var(--radius-md); }
.card { border-radius: var(--radius-lg); }
.avatar { border-radius: var(--radius-full); }
```

讲解：把圆角收敛为有限梯度，保证全站视觉一致性，也方便主题切换。这是设计系统的基础实践。

## 5. 对比分析

### 5.1 border-radius 与 clip-path

| 维度 | border-radius | clip-path |
| --- | --- | --- |
| 形状 | 椭圆/圆角矩形 | 任意多边形、路径 |
| 内容裁剪 | 不裁剪子内容 | 裁剪整个元素 |
| 阴影跟随 | 是 | 否（clip 裁剪阴影） |
| 性能 | 极好 | 好（复杂路径略差） |
| 典型场景 | 卡片、头像 | 异形图形、动画遮罩 |

### 5.2 简写与长写属性对比

简写可读性好，但会同时重置四个角；长写属性可以精确控制单个角。动画中若只改变一个角，使用长写属性避免隐式重置。

### 5.3 圆角与 border-image 的冲突

`border-image` 与 `border-radius` 不兼容：使用 `border-image` 时圆角失效。需要同时满足时，用嵌套元素或 SVG 背景替代。

## 6. 常见陷阱与最佳实践

陷阱一：忘记 `overflow: hidden`，子图片溢出圆角。

陷阱二：`border-radius: 50%` 用于非正方形元素得到椭圆，误以为是圆。用 `aspect-ratio: 1/1` 固定正方形。

陷阱三：圆角值过大时浏览器自动收缩，与预期不符。理解收缩规则后按设计意图选择值。

陷阱四：在 `border-image` 元素上使用圆角，圆角被忽略。

陷阱五：为性能过度使用大半径阴影。圆角阴影成本可接受，但避免在滚动容器内大量叠加。

陷阱六：`border-radius` 对 `table` 元素（`border-collapse: collapse`）不生效。需要给 `td` 或使用 `border-spacing: 0` 方案。

最佳实践：设计令牌统一管理半径；头像与胶囊用 50%/999px；图片裁剪记得 overflow；动画优先长写属性。

## 7. 工程实践

### 7.1 主题化圆角

```ts
// theme.ts：设计令牌类型约束
export const radii = {
  sm: '4px',
  md: '8px',
  lg: '16px',
  full: '999px'
} as const

export type RadiusToken = keyof typeof radii
```

讲解：类型约束防止团队使用随意数值，配合 CSS 变量实现运行时主题切换。

### 7.2 圆角头像组件

```vue
<script setup>
defineProps<{
  src: string
  alt: string
  size?: number
  round?: boolean
}>()
</script>

<template>
  <span class="avatar" :style="{ width: size + 'px', height: size + 'px' }"
        :class="{ round: round }">
    <img :src="src" :alt="alt" />
  </span>
</template>

<style scoped>
.avatar {
  display: inline-block;
  overflow: hidden; /* 裁剪图片到圆角内 */
  border-radius: 8px; /* 默认小圆角 */
}
.avatar.round {
  border-radius: 50%; /* 圆形模式 */
}
.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
```

讲解：组件把“圆角+裁剪+图片填充”三件套封装，调用方只传尺寸与形状模式，避免每个页面重复踩坑。

## 8. 案例研究：环形进度与圆角卡片

场景一：圆形进度环。用圆角 50% 的容器加 conic-gradient 实现：

```css
.ring {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  /* 圆锥渐变从 0% 到 75% 着色，其余灰色 */
  background: conic-gradient(#1677ff 0% 75%, #f0f0f0 75% 100%);
  display: grid;
  place-items: center;
}
.ring::before {
  content: "75%";
  width: 96px;
  height: 96px;
  border-radius: 50%;
  background: #fff;
  display: grid;
  place-items: center;
}
```

讲解：外层圆环用圆锥渐变绘制进度，内层伪元素盖出中心孔。圆角在这里承担“所有元素都是正圆”的几何保证。

场景二：嵌套卡片圆角比例。外层 16px、内层 10px 的视觉层次：

```css
.outer {
  border-radius: 16px;
  padding: 12px;
  background: #fafafa;
}
.inner {
  border-radius: 10px;
  padding: 16px;
  background: #fff;
}
```

讲解：嵌套圆角遵循“内层半径 ≈ 外层半径 - padding”的经验公式，视觉上保持平行曲线。12px padding 对应 4px 差值，曲线近似同心，观感统一。

## 9. 知识要点总结与深入讲解

`border-radius` 的语法分两段：前段四角水平半径，后段（斜杠后）垂直半径。一值全同、二值对角、三值、四值顺时针，与 margin 的记忆方式完全一致。

百分比永远参照边框盒宽高，所以 50% 在正方形上是圆、在矩形上是椭圆。想要“正圆”必须保证元素本身是正方形。

圆角不会裁剪子内容，`overflow: hidden` 才负责裁剪。阴影与背景跟随圆角，outline 在现代浏览器中也跟随。理解这些边界行为，才能避免“圆角了但图片还是方的”这类问题。

### 1. border-radius 语法

```css
.box {
  border-radius: 10px;
}
.box {
  border-radius: 10px 20px 30px 40px;
} /* 左上 右上 右下 左下 */
.box {
  border-radius: 50px / 20px;
} /* 水平/垂直半径 */
```

### 1. 常见形状

```css
.circle {
  border-radius: 50%;
}
.pill {
  border-radius: 9999px;
}
.leaf {
  border-radius: 0 100% 0 100%;
}
.diagonal {
  border-radius: 50% 0 50% 0;
}
.blob {
  border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
}
```

### 2. 实战效果

```css
.bubble {
  border-radius: 12px;
  border-bottom-left-radius: 2px;
}
.card {
  border-radius: 8px;
  overflow: hidden;
}
.button {
  border-radius: 6px;
  transition: border-radius 0.3s;
}
.button:hover {
  border-radius: 12px;
}
```

### 3. 注意事项

- 百分比参照元素尺寸
- 圆角不会裁剪溢出内容（需配合 `overflow: hidden`）
- 表格 `border-collapse: collapse` 时圆角无效
### border-radius 基础

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

### border-radius 多值

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

### 单角圆角

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

### 椭圆圆角

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

### border 边框

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

### 单边边框

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

### border-image 边框图片

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

### outline 轮廓

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

### 常见圆角效果

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

### 响应式圆角

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

## 动手试试

1. 给一张图片写 `border-radius: 50%` 变成圆形头像；
2. 用四个值 `10px 20px 30px 40px` 观察每个角的变化；
3. 用斜杠语法 `50% / 25%` 做椭圆角卡片；
4. 进阶挑战：结合 `overflow: hidden` 做圆角图片容器。

## 核心知识点

> 一句话记住圆角：`border-radius` 一到四个值对应四个角（顺时针），斜杠 `/` 分隔水平与垂直半径；`50%` 是圆/胶囊的关键。

- 四个值：左上、右上、右下、左下（顺时针）；
- 两个值：对角一组；三个值：左上加右下、右上加左下、右下；
- 斜杠语法：`水平 / 垂直`，可做椭圆角；
- `border-radius: 50%` 正方形变圆、胶囊形变胶囊；
- 配合 `overflow: hidden` 让图片/子元素跟随圆角裁剪。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 圆角不生效 | 元素没有背景/边框 | 圆角需要可见盒或背景衬托 |
| 图片直角 | 圆角被图片盖住 | 容器 `overflow: hidden` |
| 百分比与像素混用 | 结果难预测 | 统一用百分比或像素 |
| 大圆角卡顿 | 裁剪开销 | 避免超大圆角配合阴影动画 |

## 扩展学习

- 盒模型：`css/003-CSS3BoxModelDetailed`；
- 阴影：`css/025-Shadow`；
- 背景裁剪：`css/026-BackgroundEnhancement`。

<!-- ============ 文档分隔线：007-css/052-MobileAdaptation.md ============ -->

## 1. 适配单位

| 单位   | 参照物         | 特点     |
| ------ | -------------- | -------- |
| `rem`  | 根元素字体大小 | 全局缩放 |
| `em`   | 父元素字体大小 | 局部缩放 |
| `vw`   | 视口宽度 1%    | 响应视口 |
| `vh`   | 视口高度 1%    | 响应视口 |
| `vmin` | 视口较小边 1%  | 适配短边 |

## 2. rem 适配

```css
html {
  font-size: 62.5%;
} /* 1rem = 10px */
body {
  font-size: 1.6rem;
} /* 16px */
```

## 3. vw 适配

```css
/* 设计稿 375px，元素 100px → 100/375*100 = 26.67vw */
.element {
  width: 26.67vw;
}
```

## 4. clamp() 函数

```css
h1 {
  font-size: clamp(1.5rem, 5vw, 3rem);
}
.container {
  width: clamp(300px, 80vw, 1200px);
}
```

$$
\text{font-size} = \text{clamp}(\text{min}, \text{preferred}, \text{max})
$$

## 5. 安全区域与1px边框

```css
.header {
  padding-top: env(safe-area-inset-top);
}
.border-1px::after {
  content: '';
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 1px;
  background: #ccc;
  transform: scaleY(0.5);
}
```

## 6. dvh 单位

```css
.full-screen {
  height: 100dvh;
} /* 动态视口高度，解决移动端 vh 问题 */
```

## 动手试试

1. 给页面加标准 viewport，用手机模拟对比加与不加的差异；
2. 用 `rem` 重写一个固定像素布局，验证字号随根字号缩放；
3. 在 375px 与 768px 两个断点下检查布局；
4. 进阶挑战：用 `clamp()` 做平滑响应式字号。

## 核心知识点

> 一句话记住移动适配：viewport 是开关，rem/百分比是弹性单位，断点跟内容走，图片用响应式方案。

- 标准 viewport：`width=device-width, initial-scale=1.0`；
- 弹性单位：`rem`/`%`/`vw`/`vh` 优于固定 `px`；
- 移动优先 + `min-width` 媒体查询；
- 图片适配：`max-width: 100%`、`srcset`、`object-fit`；
- 触屏优化：点击目标 ≥ 44px、`touch-action`。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 缺少 viewport | 桌面宽度渲染 | 每页加标准 viewport |
| 固定 px 布局 | 小屏溢出 | 弹性单位 + 断点 |
| 图片撑破容器 | 横向滚动 | `max-width: 100%` |
| 忽略安全区域 | 刘海屏遮挡 | safe-area-inset |
| 点击目标太小 | 误触 | 增大热区 |

## 扩展学习

- 视口：`html5/035-ViewportConfigMobileFirst`；
- 媒体查询：`css/031-MediaQuery`；
- 响应式：`css/033-ResponsiveDesign`。

<!-- ============ 文档分隔线：007-css/053-Function.md ============ -->

## 1. 历史动机与发展脉络

CSS 早期没有计算能力，布局中“容器宽度减去固定侧栏”只能依赖百分比近似或 JS 计算。CSS Values and Units Level 3 于 2011 年前后开始定义 `calc()`，2013 年后主流浏览器陆续支持。`min()`/`max()`/`clamp()` 属于 CSS Values and Units Level 4，2020 年前后获得主流支持，补齐了“取极值”与“钳制”能力。

颜色函数的发展同样显著：`rgba()`/`hsla()` 在 CSS3 Color 中标准化（2011）；CSS Color 4（2023 年成为候选推荐）引入 `color-mix()`、`oklch()`、`lab()` 等现代色彩空间函数，使颜色混合与感知均匀性成为可能。渐变函数从 CSS3 的 `linear-gradient` 演进到支持角度、位置、重复渐变与锥形渐变。

CSS 变量（自定义属性）在 CSS Custom Properties for Cascading Variables Level 1（2012 年草案，2015 年后广泛支持）中定义，`var()` 成为主题系统的基石，并与数学函数形成组合：`calc(var(--gap) * 2)`。

```mermaid
timeline
    title CSS 函数演进
    2011 : calc() 进入 CSS Values 3
    2013 : 主流浏览器支持 calc()
    2015 : CSS 变量 var() 广泛支持
    2020 : min/max/clamp 主流支持
    2023 : CSS Color 4 color-mix 可用
    2025 : oklch 成为现代色彩工作流标配
```

## 2. 形式化定义

### 2.1 数学函数

`calc(表达式)`：对长度、百分比、角度、时间等数值类型执行加减乘除。语法约束：`+` 与 `-` 两侧必须有空格（避免与正负号歧义），`*` 与 `/` 不需要空格但两侧操作数类型受限（乘法至少一侧为数字，除法右侧必须为数字且不能为零）。

`min(值1, 值2, ...)`：返回参数中的最小值，参数可以混合单位，但最终结果类型必须一致。

`max(值1, 值2, ...)`：返回最大值。

`clamp(最小值, 首选值, 最大值)`：等价于 `max(最小值, min(首选值, 最大值))`。首选值被钳制在区间内。

现代 CSS 还提供了完整的数值函数族（2024-2026 逐步进入基线）：

`sin(角度)`、`cos(角度)`、`tan(角度)`：三角函数，角度用 `deg`/`rad`/`turn` 表示，常用于周期性动画与圆形轨迹计算。

`asin(x)`、`acos(x)`、`atan(x)`、`atan2(y, x)`：反三角函数，`atan2` 接收两个参数，用于从坐标反推角度（如指针旋转）。

`exp(x)`、`log(x)`、`sqrt(x)`、`pow(x, y)`、`hypot(a, b)`：指数与根式函数，适合缩放曲线与物理模拟。

`abs(x)`、`sign(x)`：绝对值与符号函数。

`round(x)`、`mod(a, b)`、`rem(a, b)`：取整与余数函数，`round()` 可指定策略（`nearest`/`up`/`down`）。

```css
/* 示例：用三角函数做圆形轨道上的装饰点 */
.orbit {
  left: calc(50% + 120px * cos(45deg));
  top: calc(50% + 120px * sin(45deg));
}
```

**讲解：** 多数项目日常只用 `calc()`/`clamp()`；三角函数与指数函数适合图形、图表、动画类场景，使用前用 `@supports` 做能力检测。

### 2.2 变量函数

`var(--name, 回退值)`：读取自定义属性 `--name` 的值；若未定义或无效，使用回退值。回退值本身可以使用其他函数（如 `var(--x, calc(...))`）。

自定义属性的特性：值在声明处不校验类型，只有在被使用处的属性上下文中才校验；继承性使变量可以从 `:root` 传播到所有元素；`@property` 可以注册带类型与初始值的自定义属性，支持动画。

### 2.3 颜色函数

`rgb(r g b / a)` 与 `rgba(r g b / a)`：红绿蓝三通道加透明度；现代语法允许空格分隔与斜杠透明度，也支持逗号旧语法。

`hsl(h s l / a)`：色相（角度或数字）、饱和度、亮度；`oklch(l c h / a)` 是感知均匀的色彩空间。

`color-mix(in srgb, 颜色1 40%, 颜色2)`：按比例混合两种颜色，`in` 指定混合色彩空间。

### 2.4 渐变函数

`linear-gradient(方向, 色标...)`、`radial-gradient(形状 尺寸 at 位置, 色标...)`、`conic-gradient(from 角度 at 位置, 色标...)`；`repeating-` 前缀生成重复渐变。

```mermaid
flowchart TD
    A["CSS 函数"] --> B["数学：calc/min/max/clamp"]
    A --> C["变量：var()"]
    A --> D["颜色：rgb/hsl/oklch/color-mix"]
    A --> E["渐变：linear/radial/conic"]
    B --> F["布局尺寸计算"]
    C --> G["主题与设计令牌"]
    D --> H["主题色派生"]
    E --> I["装饰与视觉层次"]
```

## 3. 理论推导与原理解析

### 3.1 计算值求值时机

CSS 属性值经历指定值、计算值、使用值、实际值四个阶段。数学函数在“计算值”阶段完成求值，此时单位类型已经统一（长度转换为像素或视口单位），因此 `calc(100% - 40px)` 最终得到确定长度。理解求值时机可以解释：`min()`/`max()` 中混合百分比与固定值不会产生无限递归，因为百分比在布局阶段解析。

### 3.2 var() 的替换规则

`var()` 在自定义属性解析阶段替换，替换后整个声明重新参与计算。若替换结果对当前属性无效，该声明变为“无效 at 计算值时间”（invalid at computed-value time），此时使用属性的初始值或继承值，而不是回退值——这是 var() 与普通属性最大的行为差异。因此回退值只在变量本身未定义时生效。

### 3.3 clamp 的流体推导

流体排版的数学表达：字号 = clamp(最小字号, 视口相关值, 最大字号)。视口相关值常用 `vw` 单位，例如 `clamp(1rem, 1rem + 1vw, 1.5rem)`。推导：视口宽度为 0 时取 1rem，视口为 100vw 时约 2rem，但被钳制在 1.5rem。该公式让字号在区间内线性变化，避免媒体查询逐断点跳变。

### 3.4 color-mix 的混合模型

`color-mix(in srgb, red 40%, blue)` 在指定色彩空间插值。比例表示第一种颜色的权重，未指定权重时按 50/50 混合。混合空间的感知均匀性影响结果：`oklab` 混合比 `srgb` 混合更接近人眼感知的中途色。

## 4. 代码示例（带详尽注释）

### 4.1 calc() 基础

```css
/* 侧栏固定 240px，主区域占满剩余空间 */
.main {
  width: calc(100% - 240px);
  margin-left: 240px;
}

/* 运算符两侧必须有空格 */
.header {
  padding: calc(1rem + 2px) calc(2rem - 4px);
}
```

讲解：`calc(100% - 240px)` 是经典布局公式。注意 `+`/`-` 两侧空格是语法要求，缺少空格整个声明无效。

### 4.2 min() 与 max()

```css
/* 内容宽度最大 1200px，小屏时占满可用空间（减去两侧内边距） */
.container {
  width: min(1200px, 100% - 32px);
  margin-inline: auto;
}

/* 按钮最小宽度 160px，但不超过容器 100% */
.button {
  width: max(160px, 100%);
}
```

讲解：`min()` 表达“上界”，`max()` 表达“下界”。`width: min(1200px, 100% - 32px)` 取代了 `max-width + width` 的旧写法，语义更直接。

### 4.3 clamp() 流体排版

```css
/* 标题字号：最小 1.5rem，视口相关增长，最大 3rem */
.hero-title {
  font-size: clamp(1.5rem, 1rem + 2.5vw, 3rem);
}

/* 间距也流体化 */
.section {
  padding-block: clamp(2rem, 1rem + 4vw, 6rem);
}
```

讲解：`clamp()` 让字号随视口连续变化，兼顾小屏可读性与大屏视觉冲击。`vw` 系数决定增长斜率，可通过设计稿两端值反推。

### 4.4 var() 与主题系统

```css
:root {
  --color-primary: #1677ff;
  --space-md: 16px;
  --radius: 8px;
}

.card {
  /* 变量参与计算 */
  padding: var(--space-md);
  border: 1px solid color-mix(in srgb, var(--color-primary) 30%, transparent);
  border-radius: var(--radius);
}

/* 深色主题只需覆盖变量 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-primary: #4096ff;
  }
}
```

讲解：`var()` 与 `color-mix()` 组合：边框颜色自动从主题色派生。主题切换只改变量定义，组件样式零改动。

### 4.5 color-mix() 派生色

```css
.button {
  background: var(--color-primary);
}

/* 悬停色：主色与黑色混合 10% */
.button:hover {
  background: color-mix(in srgb, var(--color-primary) 90%, black);
}

/* 禁用态：主色 40% 透明 */
.button:disabled {
  background: color-mix(in srgb, var(--color-primary) 40%, transparent);
}
```

讲解：`color-mix` 取代了手写调色板。主色改变时，悬停、禁用、边框等派生色自动跟随，是设计系统维护的利器。

### 4.6 渐变函数

```css
/* 线性渐变：135 度方向，三段色标 */
.hero {
  background: linear-gradient(135deg, #1677ff 0%, #69b1ff 50%, #d3e7ff 100%);
}

/* 径向渐变：从左上角扩散 */
.sun {
  background: radial-gradient(circle at 30% 30%, #fff7d6, #ffc53d);
}

/* 锥形渐变：从 0 度开始，用于环形图 */
.pie {
  background: conic-gradient(from 0deg, #1677ff 0% 40%, #52c41a 40% 70%, #faad14 70% 100%);
}
```

讲解：三种渐变覆盖主流场景：线性用于横幅与按钮，径向用于光晕，锥形用于环形图。渐变函数之间可以叠加（多层 background），创造丰富层次。

### 4.7 渐变与 mask 组合

```css
/* 淡出遮罩：内容底部渐隐 */
.fade-bottom {
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent);
  mask-image: linear-gradient(to bottom, black 60%, transparent);
}
```

讲解：`mask-image` 用亮度控制透明度，黑色区域显示、透明区域隐藏。该技巧常用于长文本折叠预览。

### 4.8 @supports 回退

```css
/* 支持 clamp 的浏览器使用流体字号 */
.title {
  font-size: 1.5rem;
}

@supports (font-size: clamp(1rem, 2vw, 3rem)) {
  .title {
    font-size: clamp(1.5rem, 1rem + 2vw, 3rem);
  }
}
```

讲解：`@supports` 做特性检测，旧浏览器获得回退值。现代项目只需对极少数新函数（如 `color-mix` 早期版本）做此类保护。

## 5. 对比分析

### 5.1 原生函数与 Sass 函数

| 维度 | 原生 CSS 函数 | Sass 函数 |
| --- | --- | --- |
| 求值时机 | 浏览器运行时 | 构建时 |
| 动态性 | 随视口/变量变化 | 静态结果 |
| 变量 | var() 运行时替换 | 编译期替换 |
| 依赖 | 无 | 构建工具链 |

### 5.2 min/max/clamp 与媒体查询

`clamp()` 的流体方案在断点之间连续过渡，媒体查询是分段跳变。两者可结合：流体负责区间内，媒体查询负责结构性布局变化（单列到多列）。

### 5.3 calc 与容器查询

`calc()` 解决尺寸计算，容器查询解决组件级响应。例如卡片内部间距用 `calc()`，卡片网格列数用容器查询，各司其职。

## 6. 常见陷阱与最佳实践

陷阱一：`calc()` 的 `+`/`-` 忘记空格。声明静默无效。

陷阱二：`var()` 回退值只在变量未定义时生效；变量存在但值无效时回退值不会兜底。

陷阱三：在 `min()`/`max()` 中混入无单位数字与长度。`min(1, 100px)` 类型不匹配，整个声明无效。

陷阱四：`clamp()` 中最小值大于最大值。结果是不可预测的，浏览器按规范处理仍可能异常。

陷阱五：`color-mix` 早期浏览器前缀与语法差异。现代浏览器无前缀支持，使用前可用 `@supports` 检测。

陷阱六：渐变中色标位置不递增导致硬边。按顺序递增色标位置，或用 `hsl` 表达连续色相变化。

最佳实践：数学函数优先于魔法数字；主题色统一走 `var()` + `color-mix()`；流体排版用 `clamp()` 并保留回退；渐变用于装饰而非关键信息。

## 7. 工程实践

### 7.1 间距与排版令牌

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --text-base: clamp(1rem, 0.95rem + 0.2vw, 1.125rem);
}
```

讲解：间距按 4px 基准递增，排版用 clamp 流体化。令牌化让设计与代码共享同一套词汇。

### 7.2 布局网格中的函数

```css
/* auto-fill 自动列数 + min() 控制列宽下界 */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(240px, 100%), 1fr));
  gap: clamp(12px, 2vw, 24px);
}
```

讲解：`minmax(min(240px, 100%), 1fr)` 防止窄容器中 `240px` 溢出，`auto-fill` 自动计算列数。这是 CSS 网格与函数组合的经典响应式配方。

## 8. 案例研究：无 JS 的主题化卡片系统

需求：一套卡片组件，支持浅深色主题、派生悬停色、流体间距与圆角，全部由 CSS 函数与变量实现。

```css
:root {
  /* 主题令牌 */
  --color-primary: #1677ff;
  --color-surface: #ffffff;
  --color-text: #1f1f1f;
  --radius-card: 12px;
  --space-card: clamp(12px, 2vw, 24px);
}

/* 深色主题仅覆盖表面色与文字色 */
@media (prefers-color-scheme: dark) {
  :root {
    --color-surface: #1f1f1f;
    --color-text: #e8e8e8;
  }
}

.card {
  background: var(--color-surface);
  color: var(--color-text);
  border: 1px solid color-mix(in srgb, var(--color-text) 15%, transparent);
  border-radius: var(--radius-card);
  padding: var(--space-card);
  transition: transform 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
  border-color: color-mix(in srgb, var(--color-primary) 40%, transparent);
}

/* 标题字号流体 */
.card h3 {
  font-size: clamp(1.1rem, 1rem + 0.5vw, 1.4rem);
}
```

讲解：整个系统不依赖任何 JS：主题切换由媒体查询驱动，派生色由 `color-mix` 计算，间距与字号由 `clamp` 流体化。新增组件只需引用令牌，天然获得主题一致性。

## 9. 知识要点总结与深入讲解

CSS 函数让样式表具备计算能力：`calc()` 做差值，`min/max` 做边界，`clamp` 做区间钳制。三者都以“计算值”阶段的类型安全为前提，因此混合单位是它们的核心价值。

`var()` 是主题系统的支柱，其行为特殊性（无效值不回退）要求开发者理解“变量存在但值无效”与“变量未定义”的区别。`@property` 进一步把变量升级为带类型的注册属性，支持动画与校验。

颜色函数的演进方向是感知均匀与可计算：`oklch` 让色相旋转更自然，`color-mix` 让派生色自动化。设计系统的维护成本因此大幅下降。

### 1. calc() 函数

```css
.element {
  width: calc(100% - 60px);
}
.element {
  height: calc(50vh - 2rem);
}
.element {
  font-size: calc(16px + 0.5vw);
}
```

规则：可以混合不同单位；运算符前后必须有空格；可以嵌套。

### 1. min() 函数

```css
.element {
  width: min(50vw, 400px);
} /* 取较小值 */
```

### 2. max() 函数

```css
.element {
  width: max(50vw, 300px);
} /* 取较大值 */
```

### 3. clamp() 函数

```css
h1 {
  font-size: clamp(1.5rem, 5vw, 3rem);
}
```

等价于：

```css
h1 {
  font-size: 1.5rem;
  font-size: max(1.5rem, min(5vw, 3rem));
}
```

### 4. 其他 CSS 函数

```css
.element {
  width: var(--width, 100%); /* 自定义属性 */
  transform: translateX(50px); /* 变换 */
  filter: blur(5px); /* 滤镜 */
  color: color-mix(in srgb, red 50%, blue); /* 颜色混合 */
}
```
### calc() 计算

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

### min() 取最小值

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

### max() 取最大值

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

### clamp() 钳制

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

### var() 变量引用

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

### 颜色函数

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

### 渐变函数

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

### 形状与路径函数

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

### 滤镜函数

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

### 数学函数组合

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

### 实用模式

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

### 其他函数

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

## 动手试试

1. 用 `calc()` 计算“100% 减去固定间距”的宽度；
2. 用 `clamp()` 让标题字号随视口平滑变化；
3. 用 `min()`/`max()` 实现自适应尺寸；
4. 进阶挑战：用 `var()` 组合多个设计令牌。

## 核心知识点

> 一句话记住函数：`calc()` 算数值，`clamp()` 定范围，`min()/max()` 取极值，`var()` 读变量，`attr()` 取属性。

- `calc()`：混合单位运算，如 `calc(100% - 2rem)`；
- `clamp(min, 首选, max)`：响应式字号首选；
- `min()`/`max()`：多值取最小/最大；
- `var()`：读取 CSS 变量，支持回退值 `var(--x, 默认)`；
- `attr()`：读取 HTML 属性生成内容；
- 颜色函数：`rgb()`/`hsl()`/`color-mix()`。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| calc 空格错误 | 表达式失效 | `+`/`-` 两侧必须有空格 |
| 嵌套过深 | 可读性差 | 拆成变量 |
| 滥用 min/max | 行为难预测 | 明确语义场景 |
| var 拼错名 | 回退到默认 | 定义处与使用处保持一致 |

## 扩展学习

- 变量：`css/035-CSSVariableCustomAttribute`；
- 颜色：`css/034-ModernColorSpace`；
- 响应式：`css/033-ResponsiveDesign`。

<!-- ============ 文档分隔线：007-css/054-Sass.md ============ -->

## 1. Sass 概述

Sass 是最流行的 CSS 预处理器，提供变量、嵌套、混合、继承等特性。

### 语法：SCSS（大括号）vs Sass（缩进）

```scss
// SCSS 语法（推荐）
$primary: #3498db;

.btn {
  background: $primary;
  &:hover {
    opacity: 0.8;
  }
}
```

## 2. 变量

```scss
$font-stack: 'Helvetica Neue', sans-serif;
$primary: #3498db;
$spacing: 1rem;

body {
  font-family: $font-stack;
  color: $primary;
}
```

## 3. 嵌套

```scss
.nav {
  ul {
    list-style: none;
  }
  li {
    display: inline-block;
  }
  a {
    text-decoration: none;
    &:hover {
      color: blue;
    } /* & 引用父选择器 */
  }
}
```

## 4. 混合（Mixin）

```scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

@mixin respond-to($breakpoint) {
  @if $breakpoint == md {
    @media (min-width: 768px) {
      @content;
    }
  }
  @if $breakpoint == lg {
    @media (min-width: 1024px) {
      @content;
    }
  }
}

.container {
  @include flex-center;
}
.sidebar {
  @include respond-to(md) {
    width: 25%;
  }
}
```

## 5. 继承（Extend）

```scss
%button-base {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  @extend %button-base;
  background: blue;
}
.btn-secondary {
  @extend %button-base;
  background: gray;
}
```

## 6. 运算与函数

```scss
$base: 16px;
h1 {
  font-size: $base * 2;
}
h2 {
  font-size: $base * 1.5;
}

@function rem($px) {
  @return ($px / 16) * 1rem;
}
h1 {
  font-size: rem(32);
}
```

## 7. 模块化

```scss
// _variables.scss
$primary: #3498db;

// _mixins.scss
@mixin flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}

// main.scss
@use 'variables' as *;
@use 'mixins' as *;
```

## 动手试试

1. 用 Sass 变量重构一组重复颜色；
2. 用嵌套语法整理一个卡片组件的样式；
3. 用 `@mixin` + `@include` 封装“圆角卡片”；
4. 进阶挑战：用 `@each` 循环生成间距工具类。

## 核心知识点

> 一句话记住 Sass：变量存值、嵌套分组、mixin 复用、函数计算，编译时生成 CSS；现代 CSS 变量与原生嵌套可部分替代。

- 变量：`$primary: #3498db`（编译时替换）；
- 嵌套：选择器层级书写，`&` 引用父选择器；
- `@mixin`/`@include`：样式片段复用；
- `@extend`：选择器继承（慎用）；
- 控制指令：`@if`/`@each`/`@for`；
- 与现代 CSS 的区别：Sass 是编译期，CSS 变量是运行期。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 嵌套过深 | 生成选择器冗长 | 嵌套 ≤ 3 层 |
| @extend 滥用 | 选择器膨胀 | 优先 mixin |
| 变量与 CSS 变量混用 | 语义不清 | 明确编译期/运行期 |
| 依赖构建 | 调试需 sourcemap | 开启 sourcemap |

## 扩展学习

- 对比 Less：`css/055-LessStylus`；
- 构建：`css/056-PostCSS`、`vite/005-CSSPreprocessors`；
- 架构：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/055-LessStylus.md ============ -->

## 1. Less

Less 是一种 CSS 预处理器，语法接近 CSS，学习成本低。

### 1.1 变量

```less
@primary: #3498db;
@spacing: 1rem;

body {
  color: @primary;
  padding: @spacing;
}
```

### 1.2 混合

```less
.flex-center() {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  .flex-center();
}
```

### 1.3 嵌套与运算

```less
.nav {
  a {
    color: @primary;
    &:hover {
      opacity: 0.8;
    }
  }
}

@base: 16px;
h1 {
  font-size: @base * 2;
}
```

## 2. Stylus

Stylus 提供更灵活的语法，大括号和分号均可省略。

### 2.1 变量

```stylus
primary = #3498db
spacing = 1rem

body
  color primary
  padding spacing
```

### 2.2 混合

```stylus
flex-center()
  display flex
  justify-content center
  align-items center

.container
  flex-center()
```

### 2.3 函数

```stylus
rem(px)
  (px / 16) * 1rem

h1
  font-size rem(32)
```

## 3. 对比

| 特性 | Sass            | Less        | Stylus     |
| ---- | --------------- | ----------- | ---------- |
| 语法 | SCSS/Sass       | 类 CSS      | 灵活       |
| 变量 | `$`             | `@`         | 自定义     |
| 混合 | @mixin/@include | .class()    | function() |
| 继承 | @extend         | :extend()   | @extend    |
| 条件 | @if/@else       | when guards | if/else    |
| 循环 | @for/@each      | 循环需递归  | for/in     |
| 社区 | 最大            | 较大        | 较小       |

## 动手试试

1. 用 Less 变量与嵌套重写一段样式；
2. 用 Less 的 `@import` 拆分模块；
3. 对比 Sass 与 Less 的 mixin 语法差异；
4. 进阶挑战：在 Vite 中分别配置 Sass/Less 并比较构建结果。

## 核心知识点

> 一句话记住 Less/Stylus：同为预处理器，Less 语法贴近 CSS、mixin 用类选择器，Stylus 极简可省略符号；工程上 Sass 生态更主流。

- Less：`@变量`、嵌套、mixin 用类名 + `()`；
- Stylus：无花括号/分号可选，语法自由；
- 都编译为 CSS，都有变量、嵌套、混合；
- Less 与 CSS 兼容性最好；
- 现代项目常用 Sass，Less 仍见于老项目。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 语法太自由 | 团队风格不一 | 统一 lint 与风格 |
| 混用预处理器 | 构建混乱 | 项目统一一种 |
| 忽视 CSS 原生能力 | 重复造轮子 | 优先 CSS 变量/嵌套 |

## 扩展学习

- Sass：`css/054-Sass`；
- PostCSS：`css/056-PostCSS`；
- 构建：`vite/005-CSSPreprocessors`。

<!-- ============ 文档分隔线：007-css/056-PostCSS.md ============ -->

## 1. PostCSS 概述

PostCSS 是一个用 JavaScript 插件转换 CSS 的工具，本身不提供任何功能，通过插件实现。

```javascript
// postcss.config.js
module.exports = {
  plugins: [require('autoprefixer'), require('cssnano')({ preset: 'default' })],
};
```

## 2. 常用插件

### 2.1 autoprefixer

自动添加浏览器前缀：

```css
/* 输入 */
.container {
  display: flex;
}

/* 输出 */
.container {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}
```

```json
// package.json → browserslist
"browserslist": ["last 2 versions", "> 1%", "not dead"]
```

### 2.2 cssnano

CSS 压缩优化：

```css
/* 输入 */
.container {
  margin: 0px;
  color: #ff0000;
}

/* 输出 */
.container {
  margin: 0;
  color: red;
}
```

### 2.3 postcss-preset-env

使用未来 CSS 特性：

```css
/* 输入 */
@custom-media --md (min-width: 768px);
@media (--md) {
  .container {
    width: 750px;
  }
}

/* 输出 */
@media (min-width: 768px) {
  .container {
    width: 750px;
  }
}
```

### 2.4 postcss-nesting

CSS 原生嵌套：

```css
.card {
  padding: 1rem;
  & .title {
    font-size: 1.5rem;
  }
  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
}
```

## 3. 与构建工具集成

```bash
# Vite
npm install -D postcss autoprefixer

# Webpack
npm install -D postcss-loader autoprefixer
```

## 4. 自定义插件

```javascript
module.exports = (opts = {}) => {
  return {
    postcssPlugin: 'postcss-my-plugin',
    Declaration(decl) {
      if (decl.prop === 'color' && decl.value === 'primary') {
        decl.value = opts.primary || '#3498db';
      }
    },
  };
};
```

## 动手试试

1. 在 Vite 项目中启用 PostCSS，用 autoprefixer 自动加前缀；
2. 安装 postcss-preset-env，体验未来语法编译；
3. 用 postcss-nested 写原生嵌套语法；
4. 进阶挑战：写一个自定义 PostCSS 插件（如 px 转 rem）。

## 核心知识点

> 一句话记住 PostCSS：用 JS 插件处理 CSS 的“管道”，autoprefixer 加前缀、preset-env 编译未来语法、插件生态自由扩展。

- PostCSS 不是预处理器，而是插件化处理管道；
- autoprefixer：自动添加浏览器前缀；
- postcss-preset-env：按目标浏览器编译新语法；
- 与 Sass/Less 可共存，负责“收尾加工”；
- Vite/Webpack 均内置支持。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 插件顺序错误 | 处理结果异常 | 按文档顺序配置 |
| 滥用自定义插件 | 维护成本高 | 先查生态已有插件 |
| 忘记 browserslist | 前缀目标不明 | 统一配置 browserslist |

## 扩展学习

- 构建：`vite/005-CSSPreprocessors`；
- 预处理器：`css/054-Sass`；
- 工程化：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/057-BEMNamingMethodology.md ============ -->

## 1. BEM 概述

BEM（Block Element Modifier）是一种 CSS 命名方法论，提高样式可维护性。

```
.block__element--modifier
```

- **Block**：独立的页面组件（如 `.card`）
- **Element**：Block 的组成部分（如 `.card__title`）
- **Modifier**：Block 或 Element 的变体（如 `.card--featured`）

## 2. 命名规范

```css
/* Block */
.card {
}

/* Element */
.card__title {
}
.card__body {
}
.card__footer {
}

/* Block Modifier */
.card--featured {
}
.card--dark {
}

/* Element Modifier */
.card__title--large {
}
.card__button--primary {
}
```

## 3. 实战示例

```html
<div class="card card--featured">
  <div class="card__header">
    <h2 class="card__title card__title--large">标题</h2>
  </div>
  <div class="card__body">
    <p class="card__text">内容</p>
  </div>
  <div class="card__footer">
    <button class="card__button card__button--primary">操作</button>
  </div>
</div>
```

```css
.card {
  border-radius: 8px;
  padding: 1rem;
  background: white;
}
.card--featured {
  border: 2px solid gold;
}
.card__title {
  font-size: 1.2rem;
}
.card__title--large {
  font-size: 1.5rem;
}
.card__button {
  padding: 8px 16px;
  border: none;
}
.card__button--primary {
  background: blue;
  color: white;
}
```

## 4. 替代方案

| 方法论 | 命名风格                    | 特点       |
| ------ | --------------------------- | ---------- |
| BEM    | `.block__element--modifier` | 语义清晰   |
| SMACSS | 分类命名                    | 按功能分层 |
| OOCSS  | 结构与皮肤分离              | 复用性高   |
| ITCSS  | 倒三角分层                  | 优先级管理 |

## 动手试试

1. 把一个“卡片”组件按 BEM 命名：`.card`、`.card__title`、`.card--featured`；
2. 把导航改写成 BEM 结构；
3. 检查你的项目中是否还有“标签+类”混合命名；
4. 进阶挑战：对比 BEM 与 CSS Modules 的隔离方案。

## 核心知识点

> 一句话记住 BEM：Block 独立块、Element 双下划线、Modifier 双连字符；命名即文档，层级扁平化。

- Block：独立组件（`.card`）；
- Element：块的组成部分（`.card__title`）；
- Modifier：状态或变体（`.card--active`）；
- 好处：无嵌套、优先级稳定、可读性好；
- 缺点：类名长，需配合工具（如短横线命名）。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 嵌套过深 | 类名冗长 | Element 不嵌套 Element |
| 混用命名风格 | 维护混乱 | 全库统一 BEM |
| 用标签选择器 | 与 BEM 冲突 | 只用类选择器 |

## 扩展学习

- 架构：`css/043-CSSArchitectureMethodology`；
- 模块化：`css/059-CSSModules`；
- 原子化：`css/058-CSSAtomic`。

<!-- ============ 文档分隔线：007-css/058-CSSAtomic.md ============ -->

## 1. CSS 原子化概述

原子化 CSS（Atomic CSS）将每个样式属性拆分为独立的工具类，按需组合。

## 2. Tailwind CSS

### 2.1 基本用法

```html
<div class="flex items-center justify-between p-4 bg-white rounded-lg shadow-md">
  <h1 class="text-xl font-bold text-gray-900">标题</h1>
  <button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">操作</button>
</div>
```

### 2.2 响应式前缀

```html
<div class="w-full md:w-1/2 lg:w-1/3">响应式宽度</div>
```

### 2.3 状态变体

```html
<button class="bg-blue-500 hover:bg-blue-600 focus:ring-2 active:bg-blue-700">按钮</button>
```

### 2.4 自定义配置

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: { primary: '#3498db' },
      spacing: { 18: '4.5rem' },
    },
  },
  plugins: [],
};
```

### 2.5 @apply 指令

```css
.btn-primary {
  @apply px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600;
}
```

## 3. UnoCSS

### 3.1 特点

- 更快的编译速度
- 高度可定制的预设系统
- 按需生成，零冗余

```javascript
// uno.config.ts
import { defineConfig, presetUno, presetAttributify } from 'unocss';

export default defineConfig({
  presets: [presetUno(), presetAttributify()],
  rules: [['text-primary', { color: '#3498db' }]],
  shortcuts: {
    btn: 'px-4 py-2 rounded cursor-pointer',
    'btn-primary': 'btn bg-blue-500 text-white hover:bg-blue-600',
  },
});
```

## 4. 对比

| 特性     | Tailwind CSS | UnoCSS |
| -------- | ------------ | ------ |
| 性能     | 快           | 更快   |
| 定制性   | 高           | 更高   |
| 生态     | 最大         | 增长中 |
| 学习曲线 | 中等         | 中等   |

## 动手试试

1. 用工具类（如 `.text-center`、`.mt-4`）搭建一个卡片；
2. 对比“语义类 + 组件样式”与“原子类”两种写法的可维护性；
3. 在 Tailwind 中体验原子化工作流；
4. 进阶挑战：用 @apply 抽取重复工具类组合。

## 核心知识点

> 一句话记住原子化：一个类只做一件事（`.flex`、`.p-4`），组合成 UI；HTML 变长但 CSS 不增长。

- 原子类 = 单一职责的工具类；
- 优点：无样式冗余、改动局部化、设计约束统一；
- 缺点：HTML 类名冗长、组件样式散落；
- 代表：Tailwind CSS、UnoCSS；
- 可配合组件封装缓解可读性问题。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 类名泛滥 | HTML 难读 | 组件封装 + @apply |
| 与 BEM 混用 | 风格冲突 | 项目统一一种策略 |
| 动态拼接类名 | 样式丢失 | 使用完整类名或 safelist |

## 扩展学习

- Tailwind：`tailwind/003-UtilityCore`；
- BEM：`css/057-BEMNamingMethodology`；
- 架构：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/059-CSSModules.md ============ -->

## 1. CSS Modules 概述

CSS Modules 自动为每个类名生成唯一哈希，实现样式隔离，避免命名冲突。

```css
/* Button.module.css */
.btn {
  padding: 8px 16px;
  border-radius: 4px;
}
.primary {
  background: blue;
  color: white;
}
```

```javascript
import styles from './Button.module.css';

function Button() {
  return <button className={`${styles.btn} ${styles.primary}`}>Click</button>;
}
// 渲染为：<button class="Button_btn_x9y8z Button_primary_a1b2c">Click</button>
```

## 2. 命名约定

```css
/* 推荐：camelCase */
.primaryButton {
}

/* 也可以：kebab-case */
.primary-button {
}
```

```javascript
// camelCase 引用
styles.primaryButton;

// kebab-case 引用
styles['primary-button'];
```

## 3. 组合（composes）

```css
.base {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
}

.primary {
  composes: base;
  background: blue;
  color: white;
}
```

## 4. 与框架集成

### React

```javascript
import styles from './Component.module.css';
<div className={styles.container}></div>;
```

### Vue

```html
<style module>
  .container {
    padding: 1rem;
  }
</style>

<template>
  <div :class="$style.container"></div>
</template>
```

## 5. TypeScript 支持

```typescript
// declare module '*.module.css' {
//   const classes: { readonly [key: string]: string };
//   export default classes;
// }
```

## 6. 对比其他方案

| 方案        | 隔离方式   | 运行时 | 优点     |
| ----------- | ---------- | ------ | -------- |
| CSS Modules | 哈希类名   |        | 零运行时 |
| CSS-in-JS   | 运行时生成 |        | 动态样式 |
| Shadow DOM  | DOM 隔离   |        | 完全隔离 |
| BEM         | 命名约定   |        | 简单     |

## 动手试试

1. 在 Vite 项目里创建 `Button.module.css`，验证类名被哈希；
2. 在组件里用 `styles.button` 引用局部类；
3. 用 `:global()` 转义全局样式；
4. 进阶挑战：组合 `composes` 复用样式。

## 核心知识点

> 一句话记住 CSS Modules：构建时给类名加哈希实现局部作用域，组件样式不泄漏，类名引用靠对象映射。

- 文件命名 `*.module.css`，类名构建时哈希；
- 组件通过 `import styles from './x.module.css'` 引用；
- `:global()` 声明全局样式；
- `composes` 组合其它类；
- 解决命名冲突，配合组件开发。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 误用全局类 | 样式泄漏 | 明确 :global 边界 |
| 动态类名 | 映射失效 | 用 styles 对象拼接 |
| 与 Tailwind 混用 | 构建复杂 | 项目统一方案 |

## 扩展学习

- Vite：`vite/005-CSSPreprocessors`；
- 原子化：`css/058-CSSAtomic`；
- 架构：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/060-CriticalRenderPathOptimization.md ============ -->

> 前置依赖：先读 063 理论知识点与 html5/036 关键渲染路径。

## 1. 关键渲染路径

浏览器渲染流程：DOM → CSSOM → Render Tree → Layout → Paint → Composite

CSS 是渲染阻塞资源，必须优化加载策略。

## 2. 关键 CSS 内联

将首屏关键 CSS 内联到 `<head>` 中，消除渲染阻塞：

```html
<head>
  <style>
    /* 首屏关键 CSS */
    .hero {
      height: 100vh;
      background: #333;
      color: white;
    }
    .nav {
      position: fixed;
      top: 0;
      width: 100%;
    }
  </style>
</head>
```

## 3. 非关键 CSS 异步加载

```html
<!-- 方式1：preload + onload -->
<link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'" />

<!-- 方式2：media 切换 -->
<link rel="stylesheet" href="styles.css" media="print" onload="this.media='all'" />

<!-- 方式3：noscript 回退 -->
<noscript><link rel="stylesheet" href="styles.css" /></noscript>
```

## 4. CSS 性能优化清单

| 优化项           | 说明                     |
| ---------------- | ------------------------ |
| 关键 CSS 内联    | 首屏 CSS 内联到 `<head>` |
| 非关键 CSS 异步  | 延迟加载非首屏样式       |
| 压缩 CSS         | 移除空格、注释、冗余     |
| 减少选择器复杂度 | 避免深层嵌套             |
| 避免使用 @import | 串行加载影响性能         |
| 使用 contain     | 限制渲染范围             |
| 使用 will-change | 提示浏览器优化           |
| 减少重排重绘     | 批量 DOM 操作            |

## 5. CSS contain 属性

```css
.widget {
  contain: layout style paint;
  /* 或简写 */
  contain: strict; /* size layout style paint */
  contain: content; /* layout style paint */
}
```

## 6. 性能测量

```bash
# Lighthouse
npx lighthouse https://example.com --view

# Chrome DevTools
# Performance → 录制 → 分析渲染时间
# Coverage → 查看 CSS 使用率
```

## 动手试试

1. 用 Performance 面板录制页面加载，找出阻塞解析的脚本；
2. 把业务脚本改成 `defer`，对比首屏时间；
3. 将首屏关键 CSS 内联，观察 LCP 变化；
4. 进阶挑战：用 `preload` 预加载字体并对比。

## 核心知识点

> 一句话记住渲染路径：HTML 建 DOM、CSS 建 CSSOM、合成渲染树再布局绘制；CSS 阻塞渲染、脚本阻塞解析、图片不阻塞解析。

- 五步：解析 HTML → 构建 CSSOM → 渲染树 → 布局 → 绘制；
- CSS 是渲染阻塞资源，应内联关键样式；
- 普通 `<script>` 阻塞解析，用 `defer`/`async`；
- `preload` 关键资源，`prefetch` 未来资源；
- LCP/CLS 是验证指标。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 脚本阻塞 | 首屏白屏 | defer/async |
| CSS 外链过多 | 渲染延迟 | 关键内联 + 异步加载 |
| 滥用 preload | 带宽挤占 | 只 preload 首屏资源 |
| 大图无尺寸 | CLS | 设置宽高 |

## 扩展学习

- 渲染路径：`html5/037-CriticalRenderingPathAndResourceLoading`；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`；
- 指标：`javascript/050-CoreWebVitalsAndPerformanceMetrics`。

<!-- ============ 文档分隔线：007-css/061-CSSCanvasDrawing.md ============ -->

## 1. Canvas 概述 | Canvas Overview

Canvas 是 HTML5 提供的一个绘图 API，通过 JavaScript 可以在网页上绘制各种图形、动画和交互效果。Canvas 元素提供了一个矩形区域，我们可以使用各种绘图命令在这个区域内绘制内容。

### 1.1 Canvas 的特点

- **像素级控制**：可以精确控制每个像素的颜色和位置
- **丰富的绘图 API**：支持绘制路径、形状、文本、图像等
- **动画支持**：可以通过 JavaScript 实现复杂的动画效果
- **交互性**：可以响应鼠标和键盘事件，实现交互效果
- **性能优势**：对于复杂的图形和动画，Canvas 通常比 DOM 操作更高效

### 1.2 Canvas 与 SVG 的区别

| 特性              | Canvas                 | SVG                  |
| ----------------- | ---------------------- | -------------------- |
| 绘制方式          | 基于像素               | 基于矢量             |
| 缩放效果          | 放大后可能失真         | 放大后不失真         |
| 事件处理          | 不支持元素级事件       | 支持元素级事件       |
| 性能              | 适合绘制大量图形和动画 | 适合绘制少量复杂图形 |
| 存储方式          | 存储为像素数据         | 存储为 XML 结构      |
| ## 2. Canvas 基础 | Canvas Basics          |

### 2.1 创建 Canvas 元素

```html
<canvas id="myCanvas" width="400" height="300"></canvas>
```

### 2.2 获取 Canvas 上下文

要在 Canvas 上绘图，首先需要获取 Canvas 的 2D 上下文：

```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
```

### 2.3 基本绘图操作

#### 2.3.1 绘制矩形

```javascript
// 填充矩形
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 50);
// 描边矩形
ctx.strokeStyle = 'blue';
ctx.lineWidth = 2;
ctx.strokeRect(120, 10, 100, 50);
// 清除矩形
ctx.clearRect(230, 10, 100, 50);
```

#### 2.3.2 绘制路径

```javascript
// 开始路径
ctx.beginPath();
// 移动到起始点
ctx.moveTo(50, 100);
// 绘制线条
ctx.lineTo(150, 100);
ctx.lineTo(100, 150);
// 闭合路径
ctx.closePath();
// 填充路径
ctx.fillStyle = 'green';
ctx.fill();
// 描边路径
ctx.strokeStyle = 'black';
ctx.lineWidth = 2;
ctx.stroke();
```

#### 2.3.3 绘制圆形

```javascript
ctx.beginPath();
ctx.arc(200, 125, 50, 0, Math.PI * 2);
ctx.fillStyle = 'yellow';
ctx.fill();
ctx.strokeStyle = 'black';
ctx.lineWidth = 2;
ctx.stroke();
```

#### 2.3.4 绘制文本

```javascript
ctx.font = '24px Arial';
ctx.fillStyle = 'black';
ctx.textAlign = 'center';
ctx.fillText('Hello Canvas!', 200, 250);
// 描边文本
ctx.strokeStyle = 'red';
ctx.lineWidth = 1;
ctx.strokeText('Hello Canvas!', 200, 280);
```

## 3. Canvas 进阶 | Canvas Advanced

### 3.1 渐变效果

#### 3.1.1 线性渐变

```javascript
// 创建线性渐变
const linearGradient = ctx.createLinearGradient(0, 0, 400, 0);
linearGradient.addColorStop(0, 'red');
linearGradient.addColorStop(0.5, 'yellow');
linearGradient.addColorStop(1, 'green');
// 使用渐变
ctx.fillStyle = linearGradient;
ctx.fillRect(0, 0, 400, 300);
```

#### 3.1.2 径向渐变

```javascript
// 创建径向渐变
const radialGradient = ctx.createRadialGradient(200, 150, 0, 200, 150, 150);
radialGradient.addColorStop(0, 'white');
radialGradient.addColorStop(1, 'blue');
// 使用渐变
ctx.fillStyle = radialGradient;
ctx.fillRect(0, 0, 400, 300);
```

### 3.2 图案填充

```javascript
// 创建图案
const patternCanvas = document.createElement('canvas');
patternCanvas.width = 20;
patternCanvas.height = 20;
const patternCtx = patternCanvas.getContext('2d');
patternCtx.fillStyle = 'red';
patternCtx.fillRect(0, 0, 10, 10);
patternCtx.fillRect(10, 10, 10, 10);
// 创建重复图案
const pattern = ctx.createPattern(patternCanvas, 'repeat');
// 使用图案
ctx.fillStyle = pattern;
ctx.fillRect(0, 0, 400, 300);
```

### 3.3 图像处理

#### 3.3.1 绘制图像

```javascript
const img = new Image();
img.src = 'image.jpg';
img.onload = function () {
  // 绘制完整图像
  ctx.drawImage(img, 0, 0);
  // 绘制缩放后的图像
  ctx.drawImage(img, 0, 150, 200, 100);
  // 绘制图像的一部分
  ctx.drawImage(img, 100, 100, 200, 100, 200, 150, 200, 100);
};
```

#### 3.3.2 图像变换

```javascript
const img = new Image();
img.src = 'image.jpg';
img.onload = function () {
  // 保存当前状态
  ctx.save();
  // 平移
  ctx.translate(100, 50);
  // 旋转
  ctx.rotate(Math.PI / 4);
  // 缩放
  ctx.scale(0.5, 0.5);
  // 绘制图像
  ctx.drawImage(img, 0, 0);
  // 恢复之前的状态
  ctx.restore();
};
```

### 3.4 合成模式

```javascript
// 绘制第一个矩形
ctx.fillStyle = 'red';
ctx.fillRect(50, 50, 100, 100);
// 设置合成模式
ctx.globalCompositeOperation = 'source-over'; // 默认
// ctx.globalCompositeOperation = 'source-in';
// ctx.globalCompositeOperation = 'source-out';
// ctx.globalCompositeOperation = 'destination-over';
// ctx.globalCompositeOperation = 'destination-in';
// ctx.globalCompositeOperation = 'destination-out';
// ctx.globalCompositeOperation = 'lighter';
// ctx.globalCompositeOperation = 'copy';
// ctx.globalCompositeOperation = 'xor';
// 绘制第二个矩形
ctx.fillStyle = 'blue';
ctx.fillRect(100, 100, 100, 100);
```

## 4. Canvas 动画 | Canvas Animation

### 4.1 基本动画循环

```javascript
function animate() {
  // 清除画布
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // 绘制动画内容
  // ...
  // 请求下一帧
  requestAnimationFrame(animate);
}
// 开始动画
animate();
```

### 4.2 移动动画

```javascript
let x = 0;
let y = 150;
let dx = 2;
let dy = 2;
function animate() {
  // 清除画布
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // 绘制圆形
  ctx.beginPath();
  ctx.arc(x, y, 20, 0, Math.PI * 2);
  ctx.fillStyle = 'red';
  ctx.fill();
  // 更新位置
  x += dx;
  y += dy;
  // 边界检测
  if (x + 20 > canvas.width || x - 20 < 0) {
    dx = -dx;
  }
  if (y + 20 > canvas.height || y - 20 < 0) {
    dy = -dy;
  }
  // 请求下一帧
  requestAnimationFrame(animate);
}
// 开始动画
animate();
```

### 4.3 交互动画

```javascript
let isDrawing = false;
let lastX = 0;
let lastY = 0;
// 鼠标按下事件
canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  [lastX, lastY] = [e.offsetX, e.offsetY];
});
// 鼠标移动事件
canvas.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;
  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.strokeStyle = 'black';
  ctx.lineWidth = 2;
  ctx.stroke();
  [lastX, lastY] = [e.offsetX, e.offsetY];
});
// 鼠标释放事件
canvas.addEventListener('mouseup', () => {
  isDrawing = false;
});
// 鼠标离开事件
canvas.addEventListener('mouseout', () => {
  isDrawing = false;
});
```

## 5. Canvas 实战示例 | Canvas Practical Examples

### 5.1 简单的绘图应用

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Canvas Drawing App</title>
    <style>
      canvas {
        border: 1px solid black;
        cursor: crosshair;
      }
      .controls {
        margin-bottom: 10px;
      }
    </style>
  </head>
  <body>
    <div class="controls">
      <label for="color">Color:</label>
      <input type="color" id="color" value="#000000" />
      <label for="size">Size:</label>
      <input type="range" id="size" min="1" max="20" value="2" />
      <button id="clear">Clear</button>
    </div>
    <canvas id="canvas" width="600" height="400"></canvas>
    <script>
      const canvas = document.getElementById('canvas');
      const ctx = canvas.getContext('2d');
      const colorInput = document.getElementById('color');
      const sizeInput = document.getElementById('size');
      const clearButton = document.getElementById('clear');
      let isDrawing = false;
      let lastX = 0;
      let lastY = 0;
      // 鼠标按下事件
      canvas.addEventListener('mousedown', (e) => {
        isDrawing = true;
        [lastX, lastY] = [e.offsetX, e.offsetY];
      });
      // 鼠标移动事件
      canvas.addEventListener('mousemove', (e) => {
        if (!isDrawing) return;
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.strokeStyle = colorInput.value;
        ctx.lineWidth = sizeInput.value;
        ctx.stroke();
        [lastX, lastY] = [e.offsetX, e.offsetY];
      });
      // 鼠标释放事件
      canvas.addEventListener('mouseup', () => {
        isDrawing = false;
      });
      // 鼠标离开事件
      canvas.addEventListener('mouseout', () => {
        isDrawing = false;
      });
      // 清除按钮点击事件
      clearButton.addEventListener('click', () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      });
    </script>
  </body>
</html>
```

### 5.2 粒子效果

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Canvas Particle Effect</title>
    <style>
      body {
        margin: 0;
        overflow: hidden;
      }
      canvas {
        display: block;
      }
    </style>
  </head>
  <body>
    <canvas id="canvas"></canvas>
    <script>
      const canvas = document.getElementById('canvas');
      const ctx = canvas.getContext('2d');
      // 设置画布大小
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      // 粒子数组
      const particles = [];
      const particleCount = 100;
      // 创建粒子
      for (let i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          size: Math.random() * 5 + 1,
          speedX: Math.random() * 3 - 1.5,
          speedY: Math.random() * 3 - 1.5,
          color: `hsl(${Math.random() * 360}, 50%, 50%)`,
        });
      }
      // 动画函数
      function animate() {
        // 清除画布
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // 更新和绘制粒子
        for (let i = 0; i < particles.length; i++) {
          const p = particles[i];
          // 绘制粒子
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          ctx.fillStyle = p.color;
          ctx.fill();
          // 更新粒子位置
          p.x += p.speedX;
          p.y += p.speedY;
          // 边界检测
          if (p.x + p.size > canvas.width || p.x - p.size < 0) {
            p.speedX = -p.speedX;
          }
          if (p.y + p.size > canvas.height || p.y - p.size < 0) {
            p.speedY = -p.speedY;
          }
          // 连接粒子
          for (let j = i; j < particles.length; j++) {
            const p2 = particles[j];
            const dx = p.x - p2.x;
            const dy = p.y - p2.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            if (distance < 100) {
              ctx.beginPath();
              ctx.strokeStyle = p.color;
              ctx.lineWidth = 0.2;
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(p2.x, p2.y);
              ctx.stroke();
            }
          }
        }
        // 请求下一帧
        requestAnimationFrame(animate);
      }
      // 开始动画
      animate();
      // 窗口大小改变时调整画布大小
      window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      });
    </script>
  </body>
</html>
```

### 5.3 时钟效果

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Canvas Clock</title>
    <style>
      canvas {
        display: block;
        margin: 50px auto;
        border: 1px solid black;
        border-radius: 50%;
      }
    </style>
  </head>
  <body>
    <canvas id="canvas" width="400" height="400"></canvas>
    <script>
      const canvas = document.getElementById('canvas');
      const ctx = canvas.getContext('2d');
      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;
      const radius = 180;
      // 绘制时钟
      function drawClock() {
        // 清除画布
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        // 获取当前时间
        const now = new Date();
        const hours = now.getHours();
        const minutes = now.getMinutes();
        const seconds = now.getSeconds();
        // 绘制表盘
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 2;
        ctx.stroke();
        // 绘制刻度
        for (let i = 0; i < 12; i++) {
          const angle = (i / 12) * Math.PI * 2;
          const x1 = centerX + Math.cos(angle) * (radius - 20);
          const y1 = centerY + Math.sin(angle) * (radius - 20);
          const x2 = centerX + Math.cos(angle) * (radius - 10);
          const y2 = centerY + Math.sin(angle) * (radius - 10);
          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.strokeStyle = 'black';
          ctx.lineWidth = 2;
          ctx.stroke();
          // 绘制数字
          const text = i === 0 ? '12' : i.toString();
          ctx.font = '20px Arial';
          ctx.fillStyle = 'black';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          const textX = centerX + Math.cos(angle) * (radius - 40);
          const textY = centerY + Math.sin(angle) * (radius - 40);
          ctx.fillText(text, textX, textY);
        }
        // 绘制时针
        const hourAngle = ((hours % 12) / 12) * Math.PI * 2 + (minutes / 60) * ((Math.PI * 2) / 12);
        const hourX = centerX + Math.cos(hourAngle) * (radius - 80);
        const hourY = centerY + Math.sin(hourAngle) * (radius - 80);
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(hourX, hourY);
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 4;
        ctx.stroke();
        // 绘制分针
        const minuteAngle = (minutes / 60) * Math.PI * 2 + (seconds / 60) * ((Math.PI * 2) / 60);
        const minuteX = centerX + Math.cos(minuteAngle) * (radius - 60);
        const minuteY = centerY + Math.sin(minuteAngle) * (radius - 60);
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(minuteX, minuteY);
        ctx.strokeStyle = 'black';
        ctx.lineWidth = 2;
        ctx.stroke();
        // 绘制秒针
        const secondAngle = (seconds / 60) * Math.PI * 2;
        const secondX = centerX + Math.cos(secondAngle) * (radius - 40);
        const secondY = centerY + Math.sin(secondAngle) * (radius - 40);
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(secondX, secondY);
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 1;
        ctx.stroke();
        // 绘制中心点
        ctx.beginPath();
        ctx.arc(centerX, centerY, 5, 0, Math.PI * 2);
        ctx.fillStyle = 'black';
        ctx.fill();
      }
      // 绘制时钟并每秒更新
      drawClock();
      setInterval(drawClock, 1000);
    </script>
  </body>
</html>
```

## 6. Canvas 性能优化 | Canvas Performance Optimization

### 6.1 减少绘制操作

- **批量绘制**：将多个绘制操作合并为一个路径
- **避免频繁清除**：只清除需要更新的区域
- **使用离屏 Canvas**：对于复杂的绘制，使用离屏 Canvas 预渲染

### 6.2 优化图像操作

- **使用适当的图像格式**：根据需要选择 JPEG、PNG 或 WebP
- **压缩图像**：减少图像文件大小
- **使用 CSS 缩放**：在绘制前使用 CSS 缩放图像

### 6.3 优化动画

- **使用 requestAnimationFrame**：代替 setTimeout 或 setInterval
- **限制帧率**：对于不需要 60fps 的动画，限制帧率
- **使用 transforms**：使用 translate、rotate、scale 等变换代替重新绘制

### 6.4 内存管理

- **释放不再使用的资源**：及时释放图像、路径等资源
- **避免内存泄漏**：注意事件监听器的移除

## 7. Canvas 最佳实践 | Canvas Best Practices

### 7.1 代码组织

- **模块化设计**：将 Canvas 相关代码封装为模块
- **使用面向对象**：使用类和对象组织代码
- **注释**：添加适当的注释，说明代码的功能和逻辑

### 7.2 兼容性

- **检测 Canvas 支持**：在使用 Canvas 前检测浏览器是否支持
- **提供替代方案**：为不支持 Canvas 的浏览器提供替代内容

### 7.3 安全性

- **验证用户输入**：对于用户输入的坐标和尺寸，进行验证
- **防止 XSS**：对于从用户输入生成的 Canvas 内容，进行适当的过滤

### 7.4 可访问性

- **提供替代文本**：为 Canvas 元素添加 alt 属性
- **使用 ARIA 标签**：为 Canvas 元素添加适当的 ARIA 标签
- **支持键盘导航**：对于交互式 Canvas，支持键盘导航

## 8. 总结 | Summary

Canvas 是 HTML5 提供的强大绘图 API，通过 JavaScript 可以在网页上创建各种图形、动画和交互效果。Canvas 具有像素级控制、丰富的绘图 API、动画支持和交互性等特点，适用于创建游戏、数据可视化、图像处理等应用。
通过学习 Canvas 的基础操作、进阶特性和性能优化技巧，你可以创建各种复杂的图形和动画效果。在实际开发中，应根据具体需求选择合适的技术方案，并遵循相关的最佳实践，以创建高性能、可维护的 Canvas 应用。

## 动手试试

1. 在 Canvas 上画一个矩形、一个圆形和一行文字；
2. 用 `requestAnimationFrame` 让图形动起来；
3. 实现鼠标绘制（按下画线、松开停止）；
4. 进阶挑战：用 `toBlob` 导出画布为 PNG。

## 核心知识点

> 一句话记住 Canvas：`getContext('2d')` 拿画笔，`fillRect`/路径/`arc` 画图形，`requestAnimationFrame` 做动画，像素级控制。

- Canvas 是像素画布，SVG 是矢量；
- 上下文 API：矩形、路径、文本、图像；
- 动画：清除 → 更新 → 重绘循环；
- 交互：鼠标事件 + 坐标换算；
- 导出：`toDataURL`/`toBlob`；
- 性能：减少每帧的绘制范围。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 忘记 beginPath | 路径粘连 | 每组图形前调用 |
| 尺寸用 CSS 控制 | 模糊 | 用 width/height 属性 |
| setInterval 动画 | 掉帧 | requestAnimationFrame |
| 跨域图片导出 | 画布污染 | CORS 或同源资源 |

## 扩展学习

- 完整 Canvas：`html5/012-HTML5MultimediaCanvasDrawing`；
- 动画：`css/028-CSSAnimationTransition`；
- SVG 对比：`html5/021-SVG`。

<!-- ============ 文档分隔线：007-css/062-CSSInJS.md ============ -->

> 前置依赖：需先有 React/Vue 组件开发经验。

## 1. CSS-in-JS 概述

CSS-in-JS 是一种将 CSS 样式直接写在 JavaScript 代码中的方法，它允许开发者使用 JavaScript 的全部能力来管理样式，包括动态样式、条件样式和主题管理。

### 核心优势

- **组件级样式**：样式与组件紧密耦合
- **动态样式**：使用 JavaScript 变量和逻辑生成样式
- **消除样式冲突**：自动生成唯一的类名
- **主题管理**：通过 JavaScript 轻松实现主题切换
- **类型安全**：在 TypeScript 中获得类型提示

## 2. 主流 CSS-in-JS 库

### 2.1 styled-components

**安装**

```bash
 npm install styled-components
```

**基本使用**

```jsx
 import styled from 'styled-components';
 const Button = styled.button`
  background: ${props => props.primary ? 'blue' : 'white'};
  color: ${props => props.primary ? 'white' : 'blue'};
  padding: 8px 16px;
  border: 1px solid blue;
  border-radius: 4px;
  cursor: pointer;
  &:hover {
  background: ${props => props.primary ? 'darkblue' : 'lightblue'};
  }
 `;
 // 使用组件
 <Button primary>Primary Button</Button>
 <Button>Secondary Button</Button>
```

### 2.2 Emotion

**安装**

```bash
 npm install @emotion/react @emotion/styled
```

**基本使用**

```jsx
import styled from '@emotion/styled';
const Card = styled.div`
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 16px;
  margin: 16px;
`;
const Title = styled.h2`
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 8px;
`;
// 使用组件
<Card>
  <Title>Card Title</Title>
  <p>Card content</p>
</Card>;
```

### 2.3 JSS

**安装**

```bash
 npm install jss
```

**基本使用**

```javascript
import jss from 'jss';
import preset from 'jss-preset-default';
// 初始化 JSS
jss.setup(preset());
// 创建样式
const styles = {
  button: {
    background: 'blue',
    color: 'white',
    padding: '8px 16px',
    border: 'none',
    borderRadius: '4px',
    cursor: 'pointer',
    '&:hover': {
      background: 'darkblue',
    },
  },
};
// 应用样式
const { classes } = jss.createStyleSheet(styles).attach();
// 使用样式
document.body.innerHTML = `<button class="${classes.button}">Click me</button>`;
```

## 3. 高级 Grid 布局技巧

### 3.1 网格模板区域

```css
.grid-container {
  display: grid;
  grid-template-areas:
    'header header header'
    'sidebar main main'
    'footer footer footer';
  grid-template-columns: 200px 1fr 1fr;
  grid-template-rows: auto 1fr auto;
  gap: 16px;
  height: 100vh;
}
.header {
  grid-area: header;
  background: #f0f0f0;
  padding: 16px;
}
.sidebar {
  grid-area: sidebar;
  background: #e0e0e0;
  padding: 16px;
}
.main {
  grid-area: main;
  background: #ffffff;
  padding: 16px;
}
.footer {
  grid-area: footer;
  background: #f0f0f0;
  padding: 16px;
}
```

### 3.2 响应式 Grid

```css
.responsive-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
}
/* 不同屏幕尺寸的调整 */
@media (max-width: 768px) {
  .responsive-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}
@media (max-width: 480px) {
  .responsive-grid {
    grid-template-columns: 1fr;
  }
}
```

### 3.3 网格项定位

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 100px);
  gap: 10px;
}
.item-1 {
  grid-column: 1 / 3;
  grid-row: 1 / 3;
  background: red;
}
.item-2 {
  grid-column: 3 / 6;
  grid-row: 1 / 2;
  background: blue;
}
.item-3 {
  grid-column: 1 / 2;
  grid-row: 3 / 6;
  background: green;
}
.item-4 {
  grid-column: 2 / 6;
  grid-row: 2 / 6;
  background: yellow;
}
```

## 4. Flexbox 高级技巧

### 4.1 复杂 Flex 布局

```css
.complex-flex {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: space-between;
  align-items: center;
}
.item {
  flex: 1 1 300px; /* 增长因子 1, 收缩因子 1, 基础宽度 300px */
  min-width: 200px;
  background: #f0f0f0;
  padding: 16px;
  border-radius: 8px;
}
/* 特殊项目 */
.item.special {
  flex: 2 1 400px; /* 占据更多空间 */
  background: #e0e0e0;
}
```

### 4.2 Flexbox 居中技巧

```css
/* 水平居中 */
.horizontal-center {
  display: flex;
  justify-content: center;
}
/* 垂直居中 */
.vertical-center {
  display: flex;
  align-items: center;
  height: 200px;
}
/* 水平垂直居中 */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
}
/* 多项目居中 */
.multi-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 300px;
}
```

## 5. 自定义属性 (CSS Variables)

### 5.1 基本使用

```css
 :root {
  --primary-color: #3498db;
  --secondary-color: #2ecc71;
  --text-color: #333333;
  --border-radius: 8px;
  --spacing: 16px;
 }
 .button {
  background: var(--primary-color);
  color: white;
  padding: var(--spacing);
  border-radius: var(--border-radius);
  border: none;
  cursor: pointer;
 }
 .card {
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: var(--border-radius);
  padding: var(--spacing);
  margin-bottom: var(--spacing);
 }
```

### 5.2 主题切换

```css
 :root {
  /* 浅色主题 */
  --bg-color: #ffffff;
  --text-color: #333333;
  --card-bg: #f0f0f0;
 }
 .dark-theme {
  /* 深色主题 */
  --bg-color: #121212;
  --text-color: #e0e0e0;
  --card-bg: #1e1e1e;
 }
 body {
  background: var(--bg-color);
  color: var(--text-color);
  transition: background 0.3s, color 0.3s;
 }
 .card {
  background: var(--card-bg);
  transition: background 0.3s;
 }
```

## 6. 动画与过渡

### 6.1 CSS 动画

```css
/* 定义动画 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* 使用动画 */
.fade-in {
  animation: fadeIn 0.5s ease-out forwards;
}
/* 复杂动画 */
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}
.pulse {
  animation: pulse 2s infinite;
}
```

### 6.2 过渡效果

```css
.transition-example {
  background: blue;
  color: white;
  padding: 16px;
  border-radius: 8px;
  transition: all 0.3s ease;
}
.transition-example:hover {
  background: darkblue;
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}
/* 多重过渡 */
.multiple-transitions {
  background: blue;
  color: white;
  padding: 16px;
  border-radius: 8px;
  transition:
    background 0.3s ease,
    transform 0.5s ease,
    box-shadow 0.3s ease;
}
.multiple-transitions:hover {
  background: darkblue;
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}
```

## 7. 性能优化

### 7.1 CSS 性能优化

1. **减少选择器复杂度**：避免深层嵌套选择器
2. **使用 CSS 变量**：减少重复代码
3. **避免使用 @import**：使用 link 标签代替
4. **压缩 CSS**：减少文件大小
5. **使用 CSS Modules**：避免样式冲突
6. **关键 CSS**：将首屏关键样式内联

### 7.2 渲染性能

1. **避免重排**：减少 DOM 操作
2. **使用 will-change**：提示浏览器优化
3. **GPU 加速**：使用 transform 和 opacity
4. **避免布局抖动**：批量 DOM 操作

```css
/* 提示浏览器优化 */
.optimized {
  will-change: transform;
  transition: transform 0.3s;
}
/* GPU 加速 */
.gpu-accelerated {
  transform: translateZ(0); /* 触发 GPU 加速 */
}
```

## 8. 响应式设计高级技巧

### 8.1 移动优先设计

```css
/* 移动优先基础样式 */
.container {
  width: 100%;
  padding: 16px;
}
/* 平板设备 */
@media (min-width: 768px) {
  .container {
    max-width: 720px;
    margin: 0 auto;
    padding: 24px;
  }
}
/* 桌面设备 */
@media (min-width: 1024px) {
  .container {
    max-width: 960px;
    padding: 32px;
  }
}
/* 大屏幕设备 */
@media (min-width: 1280px) {
  .container {
    max-width: 1140px;
  }
}
```

### 8.2 响应式断点策略

| 断点 | 设备类型 | 宽度范围       |
| :--- | :------- | :------------- |
| xs   | 超小屏幕 | < 576px        |
| sm   | 小屏幕   | 576px - 767px  |
| md   | 中等屏幕 | 768px - 991px  |
| lg   | 大屏幕   | 992px - 1199px |
| xl   | 超大屏幕 | ≥ 1200px       |

### 8.3 响应式图片

```html
<!-- 响应式图片 -->
<img
  src="small.jpg"
  srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
  alt="Responsive image"
/>
<!-- 不同屏幕尺寸的图片 -->
<picture>
  <source media="(max-width: 768px)" srcset="mobile.jpg" />
  <source media="(min-width: 769px)" srcset="desktop.jpg" />
  <img src="fallback.jpg" alt="Responsive image" />
</picture>
```

## 9. 工具与框架

### 9.1 CSS 预处理器

- **Sass/SCSS**：功能丰富的预处理器
- **Less**：简洁易用的预处理器
- **Stylus**：灵活的预处理器

### 9.2 CSS 框架

- **Tailwind CSS**：实用优先的工具类框架
- **Bootstrap**：全面的 UI 框架
- **Bulma**：现代 CSS 框架
- **Foundation**：响应式前端框架

### 9.3 开发工具

- **PostCSS**：CSS 处理工具
- **Autoprefixer**：自动添加浏览器前缀
- **PurgeCSS**：移除未使用的 CSS
- **Stylelint**：CSS 代码检查

## 10. 最佳实践

1. **组件化**：将样式与组件紧密结合
2. **命名规范**：使用 BEM 或 SMACSS 等命名规范
3. **模块化**：将样式按功能模块组织
4. **可维护性**：编写清晰、可维护的 CSS
5. **性能**：关注 CSS 性能，避免不必要的样式
6. **兼容性**：考虑浏览器兼容性
7. **文档**：为复杂样式添加注释和文档

## 11. 项目实战

### 11.1 CSS-in-JS 项目结构

```mermaid
flowchart TD
    T0["css-in-js-project/"]
    T1["components/"]
    T2["Button/"]
    T3["Button.jsx"]
    T4["styles.js"]
    T5["Card/"]
    T6["Card.jsx"]
    T7["styles.js"]
    T8["Header/"]
    T9["Header.jsx"]
    T10["styles.js"]
    T11["styles/"]
    T12["theme.js"]
    T13["globalStyles.js"]
    T14["App.jsx"]
    T15["index.js"]
    T0 --> T1
    T10 --> T11
    T13 --> T14
    T13 --> T15
```

### 11.2 高级布局项目

```mermaid
flowchart TD
    T0["advanced-layouts/"]
    T1["css/"]
    T2["grid-layouts.css"]
    T3["flexbox-layouts.css"]
    T4["responsive.css"]
    T5["animations.css"]
    T6["components/"]
    T7["dashboard.html"]
    T8["gallery.html"]
    T9["landing.html"]
    T10["index.html"]
    T0 --> T1
    T5 --> T6
    T9 --> T10
```

## 12. 常见问题与解决方案

### 12.1 CSS-in-JS 问题

**问题**：CSS-in-JS 增加了打包体积
**解决方案**：使用 Tree Shaking，只导入需要的样式
**问题**：运行时性能问题
**解决方案**：使用静态提取，将样式提取到单独的 CSS 文件

### 12.2 布局问题

**问题**：Grid 布局浏览器兼容性
**解决方案**：提供 Flexbox fallback
**问题**：响应式设计在某些设备上显示异常
**解决方案**：使用设备模拟器测试，调整断点

## 动手试试

1. 在 React 中用内联 style 对象设置样式，观察动态值能力；
2. 引入 styled-components，用组件方式写样式；
3. 对比 CSS-in-JS 与 CSS Modules 的动态主题实现；
4. 进阶挑战：用 CSS 变量 + CSS-in-JS 做主题切换。

## 核心知识点

> 一句话记住 CSS-in-JS：样式写在 JS 里，动态值天然支持、作用域隔离、可组件化；代价是运行时开销与 SSR 配置。

- 形式：内联对象、styled-components、Emotion；
- 优点：动态值、局部作用域、随组件卸载；
- 缺点：运行时开销、调试需标记、SSR 复杂；
- 与 CSS 变量结合可做主题；
- 现代框架常混用 CSS Modules 与 CSS-in-JS。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 渲染期生成样式 | 性能开销 | 优先静态样式 + 变量 |
| SSR 闪烁 | 首屏无样式 | 配置 babel 插件/抽取 |
| 组件库样式覆盖 | 优先级混乱 | 明确 API 与变量入口 |

## 扩展学习

- React：`react/` 模块组件样式；
- 模块化：`css/059-CSSModules`；
- 架构：`css/043-CSSArchitectureMethodology`。

<!-- ============ 文档分隔线：007-css/063-CSSTheoryKnowledge.md ============ -->

> 0基础速通：先掌握 003/009/016 再读本篇；本篇是理论串讲，可分段查阅，不要一次读完。

```text
         |
         v
    Attachment (DOM + CSSOM --> Render Tree)
         |
         v
    Layout (计算位置和大小)
         |
         v
    Paint (绘制像素)
         |
         v
    Composite (合成图层)
         |
         v
    屏幕显示

```

### 各阶段详解

#### 1. 构建 DOM 树

解析 HTML 文档，构建文档对象模型（DOM）。DOM 树描述了文档的结构和内容。

```html
<html>
  <body>
    <div class="container">
      <p>Hello</p>
    </div>
  </body>
</html>
```

DOM 树：

```mermaid
flowchart TD
    Html[html] --> Body[body]
    Body --> Div[div.container]
    Div --> P[p]
    P --> Hello["Hello"]
```

#### 2. 构建 CSSOM 树

解析 CSS 样式表，构建 CSS 对象模型（CSSOM）。CSSOM 树描述了样式规则和层叠计算结果。

CSSOM 的构建是渲染阻塞的：浏览器必须等 CSSOM 构建完成才能进入渲染阶段。这就是为什么 CSS 应放在 `<head>` 中尽早加载。

#### 3. 生成渲染树（Render Tree）

DOM 和 CSSOM 合并为渲染树。渲染树只包含需要显示的节点（`display: none` 的元素不在渲染树中，但 `visibility: hidden` 的元素在）。

#### 4. 布局（Layout / Reflow）

计算渲染树中每个节点的位置和大小。布局是从根节点开始的递归过程：

1. 根节点的宽度为视口宽度
2. 块级元素的宽度默认为父元素宽度
3. 行内元素的宽度由内容决定
4. 高度由内容和子元素决定（除非显式设置）

布局的触发条件：
- 添加/删除 DOM 元素
- 修改元素尺寸（width/height/padding/margin/border）
- 修改文字内容
- 修改字体
- 窗口 resize
- 读取某些属性（offsetWidth/scrollTop 等，强制同步布局）

#### 5. 绘制（Paint）

将渲染树中的节点绘制为像素。绘制分为多个层，按特定顺序进行：

1. 背景色
2. 背景图
3. 边框
4. 子元素
5. 轮廓（outline）

#### 6. 合成（Composite）

将多个图层按正确顺序合成最终画面。合成由 GPU 完成，是最高效的渲染阶段。

### 性能优化策略

| 触发阶段 | 属性示例 | 性能影响 |
|---------|---------|---------|
| Layout | width, height, margin, padding, font-size | 最差（全量重排） |
| Paint | color, background, box-shadow, border-radius | 中等（重绘） |
| Composite | transform, opacity | 最佳（仅合成） |

优化原则：尽量只触发 Composite 阶段。使用 `transform` 替代 `top/left`，使用 `opacity` 替代 `visibility: hidden`。

```css
.animated-element {
    will-change: transform;
    transform: translateX(0);
    transition: transform 0.3s ease;
}
.animated-element.moved {
    transform: translateX(100px);
}
```

---

## 层叠上下文（Stacking Context）

### 什么是层叠上下文

层叠上下文是 HTML 元素的三维概念，决定了元素在 Z 轴上的绘制顺序。每个层叠上下文内部的元素按规则排序，层叠上下文之间按 Z 轴顺序排列。

### 创建层叠上下文的条件

以下情况会创建新的层叠上下文：

1. **根元素** -- `<html>` 本身是一个层叠上下文
2. **z-index + 定位** -- `position: relative/absolute/fixed` + `z-index` 不为 auto
3. **flex/grid 子项** -- `z-index` 不为 auto 的 flex/grid 子项
4. **opacity** -- 值小于 1
5. **transform** -- 值不为 none
6. **filter** -- 值不为 none
7. **perspective** -- 值不为 none
8. **clip-path** -- 值不为 none
9. **mask** -- 值不为 none
10. **will-change** -- 值为 transform/opacity/filter 等
11. **contain** -- 值为 layout/paint/strict/content
12. **isolation** -- 值为 isolate

### 层叠顺序（从底到顶）

```
1. 层叠上下文的背景和边框
2. z-index 为负值的子层叠上下文
3. 常规流中的块级盒子（非定位、非浮动）
4. 浮动盒子
5. 常规流中的行内盒子（包括 inline-block 和 inline-table）
6. z-index: 0 / auto 的定位元素
7. z-index 为正值的子层叠上下文
```

记忆口诀：背景 -> 负z-index -> block -> float -> inline -> z-index:0 -> 正z-index

### 层叠上下文的隔离性

层叠上下文内部的元素无法超越其父级层叠上下文的 Z 轴范围。即使子元素设置 `z-index: 9999`，如果父级层叠上下文的 `z-index: 1`，它仍然会被另一个 `z-index: 2` 的层叠上下文覆盖。

```html
<div style="position: relative; z-index: 1;">
  <div style="position: relative; z-index: 9999;">Child with z-index 9999</div>
</div>
<div style="position: relative; z-index: 2;">This will be on top of the child above</div>
```

---

## 包含块（Containing Block）

### 什么是包含块

包含块是元素定位和尺寸计算的参考矩形。不同定位方式的包含块不同。

### 包含块的确定规则

| 定位方式          | 包含块                                                       |
| ----------------- | ------------------------------------------------------------ |
| static / relative | 最近的块级容器祖先的内容区域                                 |
| absolute          | 最近的 positioned 祖先（position 不为 static）的 padding box |
| fixed             | 视口（viewport），除非祖先有 transform/filter/perspective    |
| sticky            | 最近的滚动祖先的 content box                                 |

### 包含块对尺寸计算的影响

百分比尺寸基于包含块计算：

- `width` / `padding` / `margin` 的百分比基于包含块的**宽度**
- `height` 的百分比基于包含块的**高度**（但包含块高度依赖内容时，百分比高度无效）
- `top` / `bottom` 百分比基于包含块的高度
- `left` / `right` 百分比基于包含块的宽度

```css
.parent {
  position: relative;
  width: 400px;
  height: 300px;
  padding: 20px;
}

.child {
  position: absolute;
  width: 50%; /* 50% of parent's padding box width = 220px */
  height: 50%; /* 50% of parent's padding box height = 170px */
  top: 10%; /* 10% of parent's padding box height = 34px */
  left: 10%; /* 10% of parent's padding box width = 44px */
}
```

### transform 对 fixed 定位的影响

如果 fixed 定位元素的祖先有 `transform`、`filter` 或 `perspective` 属性，包含块不再是视口，而是该祖先的 padding box：

```css
.transform-container {
  transform: translateZ(0); /* 创建新的包含块 */
}

.fixed-child {
  position: fixed;
  top: 0;
  left: 0;
  /* 相对于 .transform-container 定位，而非视口 */
}
```

---

## BFC / IFC

### BFC（Block Formatting Context，块格式化上下文）

BFC 是一个独立的渲染区域，内部元素的布局不影响外部元素。

#### 创建 BFC 的条件

1. 根元素（`<html>`）
2. 浮动元素（`float` 不为 none）
3. 绝对定位元素（`position: absolute/fixed`）
4. 行内块元素（`display: inline-block`）
5. 表格单元格（`display: table-cell`）
6. 表格标题（`display: table-caption`）
7. 弹性元素（`display: flex/inline-flex` 的子项）
8. 网格元素（`display: grid/inline-grid` 的子项）
9. `overflow` 不为 visible/clip 的块元素
10. `contain` 为 layout/content/paint/strict 的元素
11. `display: flow-root`（最明确的创建方式）

#### BFC 的特性

1. **内部块级盒子垂直排列** -- 每个块级盒子的左外边缘触及包含块的左边缘
2. **同一个 BFC 中相邻块级盒子的外边距折叠** -- 垂直 margin 合并
3. **BFC 区域不会与浮动元素重叠** -- 可用于清除浮动
4. **BFC 可以包含浮动元素** -- 解决高度塌陷
5. **BFC 是独立容器** -- 内部布局不影响外部

#### BFC 的应用

**清除浮动（高度塌陷）**

```css
.container {
  overflow: hidden; /* 或 display: flow-root; */
}
.float-child {
  float: left;
}
```

**防止 margin 折叠**

```css
.sibling-1 {
  margin-bottom: 20px;
}
.sibling-2 {
  margin-top: 30px;
}
/* 实际间距为 30px（取较大值），而非 50px */

/* 解决方案：将其中一个包裹在 BFC 中 */
.wrapper {
  overflow: hidden;
}
```

**自适应两栏布局**

```css
.sidebar {
  float: left;
  width: 200px;
}
.main-content {
  overflow: hidden; /* 创建 BFC，不与浮动重叠 */
}
```

### IFC（Inline Formatting Context，行内格式化上下文）

IFC 是行级元素的格式化上下文，行级盒子在水平方向依次排列。

#### IFC 的特性

1. 行级盒子水平排列，从包含块的顶部开始
2. 行级盒子在垂直方向上可以有不同的对齐方式（baseline/top/middle/bottom）
3. 一行放不下时换行，形成多行（line box）
4. 行框（line box）的高度由其内部最高的行级盒子决定
5. 行框的宽度为包含块的宽度
6. `text-align` 控制行级盒子在行框内的水平对齐
7. `vertical-align` 控制行级盒子在行框内的垂直对齐

#### IFC 的应用

**行内元素垂直居中**

```css
.container {
  height: 200px;
  line-height: 200px; /* 行框高度等于容器高度 */
}
.inline-element {
  vertical-align: middle; /* 在行框内垂直居中 */
}
```

**图片底部间隙**

图片默认按 baseline 对齐，底部会留出文字 descender 的空间：

```css
img {
  display: block; /* 方案1：脱离 IFC */
  vertical-align: bottom; /* 方案2：改为底部对齐 */
  font-size: 0; /* 方案3：父元素字体大小为 0 */
}
```

---

## 理论速查表

| 概念        | 核心要点                                                 | 关键细节                                  |
| ----------- | -------------------------------------------------------- | ----------------------------------------- |
| 渲染流水线  | DOM+CSSOM -> Render Tree -> Layout -> Paint -> Composite | transform/opacity 仅触发 Composite        |
| 层叠上下文  | Z 轴绘制顺序                                             | transform/opacity/filter 等创建新上下文   |
| 包含块      | 定位和尺寸的参考矩形                                     | absolute 基于 padding box，fixed 基于视口 |
| BFC         | 独立渲染区域                                             | overflow:hidden / display:flow-root 创建  |
| IFC         | 行级元素格式化                                           | baseline 对齐，line-height 控制行框高度   |
| margin 折叠 | 同一 BFC 中相邻块级盒子垂直 margin 合并                  | BFC 隔离可防止                            |
| will-change | 提示浏览器元素将变化                                     | 提前创建图层，但不要滥用                  |
| 回流/重绘   | Layout > Paint > Composite                               | 避免频繁触发 Layout                       |

## 延伸阅读
CSS 圆角与形状，见 007-css/051-BorderRadius 文档。
CSS 媒体查询与响应式，见 007-css/031-MediaQuery 文档。
CSS 函数与变量，见 007-css/053-Function 文档。
HTML 结构与语义，见 006-html5 模块。

## 动手试试

1. 用层叠上下文知识解释一个 z-index 失效案例；
2. 画出标准盒模型与怪异盒模型的差异；
3. 用 BFC 解决一次外边距塌陷；
4. 进阶挑战：解释 `:where()` 与 `:is()` 的优先级差异。

## 核心知识点

> 一句话记住 CSS 理论：层叠（优先级+来源）、盒模型（content/padding/border/margin）、格式化上下文（BFC/IFC）、包含块与定位，是四大基石。

- 层叠：来源、优先级、顺序、!important、@layer；
- 盒模型：content-box 与 border-box；
- BFC：触发条件与三大作用；
- 定位与包含块：relative/absolute/fixed 参照系；
- 继承与初始值：可继承属性列表；
- 单位与计算：px/rem/%/vw 与 calc。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 只背不验 | 概念与实际脱节 | 用 DevTools 验证 |
| 混淆 BFC/IFC | 布局理解偏差 | 对比行内/块级上下文 |
| 忽略包含块 | fixed 异常 | 理解 transform 副作用 |

## 扩展学习

- 盒模型：`css/003-CSS3BoxModelDetailed`；
- 优先级：`css/009-PriorityCalculation`；
- 层叠上下文：`css/016-StackingContext`。

<!-- ============ 文档分隔线：007-css/064-CSSNewFeatures.md ============ -->

## 1. @container 容器查询

### 1.1 基本概念

容器查询允许根据**父容器尺寸**而非视口尺寸应用样式，实现真正的组件级响应式。

```css
/* 定义容器 */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* 根据容器宽度应用样式 */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}

@container card (min-width: 200px) and (max-width: 399px) {
  .card {
    display: flex;
    flex-direction: column;
  }
}
```

### 1.2 container-type 类型

| 类型          | 说明                       |
| ------------- | -------------------------- |
| `inline-size` | 仅查询行内方向尺寸（宽度） |
| `size`        | 查询行内和块方向尺寸       |
| `normal`      | 默认值，不作为查询容器     |

### 1.3 容器查询单位

| 单位    | 含义              |
| ------- | ----------------- |
| `cqw`   | 容器宽度的 1%     |
| `cqh`   | 容器高度的 1%     |
| `cqi`   | 容器行内尺寸的 1% |
| `cqb`   | 容器块尺寸的 1%   |
| `cqmin` | 容器较小尺寸的 1% |
| `cqmax` | 容器较大尺寸的 1% |

```css
.card-title {
  font-size: clamp(14px, 3cqi, 24px);
}
```

### 1.4 样式查询

```css
/* 查询自定义属性值 */
.card-container {
  --theme: dark;
}

@container style(--theme: dark) {
  .card {
    background: #1a1a2e;
    color: #e0e0e0;
  }
}

@container style(--theme: light) {
  .card {
    background: #ffffff;
    color: #333333;
  }
}
```

## 2. @layer 层叠层

### 2.1 基本概念

`@layer` 允许显式控制样式的层叠优先级，解决第三方库样式覆盖问题。

```css
/* 声明层（顺序决定优先级，后声明的优先级更高） */
@layer reset, base, components, utilities;

/* 各层定义 */
@layer reset {
  *,
  *::before,
  *::after {
    box-sizing: border-box;
    margin: 0;
  }
}

@layer base {
  body {
    font-family: system-ui;
    line-height: 1.6;
  }
  a {
    color: #007bff;
  }
}

@layer components {
  .btn {
    padding: 8px 16px;
    border-radius: 4px;
  }
  .card {
    border: 1px solid #ddd;
    border-radius: 8px;
  }
}

@layer utilities {
  .text-center {
    text-align: center;
  }
  .mt-4 {
    margin-top: 16px;
  }
}
```

### 2.2 层叠优先级

```
无层样式 > utilities > components > base > reset

优先级从低到高：
  @layer reset        ← 最低
  @layer base
  @layer components
  @layer utilities
  无层样式（unlayered） ← 最高
```

### 2.3 嵌套层

```css
@layer framework {
  @layer base {
    /* framework.base */
  }
  @layer components {
    /* framework.components */
  }
}

/* 等效写法 */
@layer framework.base {
  /* ... */
}
@layer framework.components {
  /* ... */
}
```

### 2.4 第三方样式管理

```css
@layer reset, third-party, custom;

@import url('bootstrap.css') layer(third-party);

@layer custom {
  .btn {
    /* 自定义覆盖 */
  }
}
```

## 3. 逻辑属性

### 3.1 物理属性 vs 逻辑属性

| 物理属性           | 逻辑属性               | 说明         |
| ------------------ | ---------------------- | ------------ |
| `margin-left`      | `margin-inline-start`  | 行内起始边距 |
| `margin-right`     | `margin-inline-end`    | 行内结束边距 |
| `margin-top`       | `margin-block-start`   | 块起始边距   |
| `margin-bottom`    | `margin-block-end`     | 块结束边距   |
| `padding-left`     | `padding-inline-start` | 行内起始内距 |
| `width`            | `inline-size`          | 行内尺寸     |
| `height`           | `block-size`           | 块尺寸       |
| `border-left`      | `border-inline-start`  | 行内起始边框 |
| `text-align: left` | `text-align: start`    | 起始对齐     |
| `float: left`      | `float: inline-start`  | 起始浮动     |

### 3.2 简写属性

```css
/* 物理简写 */
margin: 10px 20px; /* top/bottom left/right */

/* 逻辑简写 */
margin-block: 10px; /* block-start block-end */
margin-inline: 20px; /* inline-start inline-end */
margin: 10px 20px; /* 仍然有效，但方向固定 */

/* 完整逻辑简写 */
margin-block-start: 10px;
margin-block-end: 10px;
margin-inline-start: 20px;
margin-inline-end: 20px;
```

### 3.3 RTL 支持

```css
/* 使用逻辑属性自动适配 RTL */
.element {
  margin-inline-start: 16px; /* LTR: margin-left; RTL: margin-right */
  padding-inline-end: 8px; /* LTR: padding-right; RTL: padding-left */
  text-align: start; /* LTR: left; RTL: right */
}
```

```html
<!-- LTR -->
<div dir="ltr" class="element">内容</div>

<!-- RTL -->
<div dir="rtl" class="element">محتوى</div>
```

### 3.4 逻辑属性与定位

```css
.positioned {
  position: absolute;
  inset-block-start: 0; /* top in LTR */
  inset-inline-start: 0; /* left in LTR */
  inset: 0; /* 所有方向（物理简写，但已支持逻辑） */
}
```

## 4. :has() 选择器

### 4.1 基本用法

`:has()` 被称为"CSS 的父选择器"，允许根据子元素状态选择父元素。

```css
/* 包含 img 的 a 标签 */
a:has(img) {
  display: block;
  border: 1px solid #ddd;
}

/* 包含 .error 的表单 */
form:has(.error) {
  border-color: red;
}

/* 有焦点的输入框的标签 */
label:has(+ input:focus) {
  color: #007bff;
  font-weight: 600;
}
```

### 4.2 表单状态样式

```css
/* 必填字段标记 */
input:required + label::after {
  content: ' *';
  color: red;
}

/* 有无效输入的表单组 */
.form-group:has(input:invalid) {
  --border-color: #dc3545;
}

/* 全部填写完成的表单 */
form:has(input:valid):not(:has(input:invalid)) button[type='submit'] {
  opacity: 1;
  pointer-events: auto;
}
```

### 4.3 卡片变体

```css
/* 有图片的卡片 */
.card:has(img) {
  grid-template-rows: 200px 1fr;
}

/* 无图片的卡片 */
.card:not(:has(img)) {
  grid-template-rows: auto;
  padding: 24px;
}
```

### 4.4 主题切换

```css
/* 根据选中的主题单选按钮应用样式 */
body:has(#theme-dark:checked) {
  background: #1a1a2e;
  color: #e0e0e0;
}

body:has(#theme-light:checked) {
  background: #ffffff;
  color: #333333;
}
```

### 4.5 性能考虑

`:has()` 的性能特征：

- 浏览器对 `:has()` 做了优化，不会遍历整个 DOM
- 避免在大型列表上使用复杂的 `:has()` 组合
- 推荐用于结构性选择，而非高频动态样式

## 5. 其他现代特性

### 5.1 :is() 和 :where()

```css
/* :is() — 优先级取参数中最高的 */
:is(h1, h2, h3):hover {
  color: #007bff;
}

/* :where() — 优先级始终为 0 */
:where(.btn, .link) {
  cursor: pointer;
}
```

### 5.2 :not() 增强

```css
/* 排除多个选择器 */
input:not([type='hidden'], [type='submit']) {
  border: 1px solid #ccc;
}
```

### 5.3 accent-color

```css
input[type='checkbox'],
input[type='radio'],
input[type='range'],
progress {
  accent-color: #007bff;
}
```

### 5.4 color-mix()

```css
.button {
  background: color-mix(in srgb, #007bff 80%, white);
  border-color: color-mix(in srgb, #007bff, black 20%);
}
```

## 动手试试

1. 用 `:has()` 实现“含图片的卡片放大”；
2. 用 `@layer` 重构一次样式覆盖；
3. 用 `color-mix()` 混合两个颜色；
4. 进阶挑战：用原生嵌套重写一段 Sass 代码。

## 核心知识点

> 一句话记住 CSS 新特性：`:has()` 父选择器、`@layer` 分层、容器查询、原生嵌套、`color-mix()`、`@property` 组成现代 CSS 工具箱。

- `:has()`：按子结构选父元素；
- `@layer`：声明式优先级分层；
- 容器查询：组件按容器响应；
- 原生嵌套：无需预处理器；
- `color-mix()`/`oklch`：现代颜色；
- `@property`：注册变量支持动画；
- `view-transition`：页面过渡。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 新特性兼容性 | 老浏览器不支持 | @supports + 兜底 |
| :has 性能 | 复杂匹配慢 | 简化选择器 |
| 一次性全用 | 项目风险大 | 渐进采用 |

## 扩展学习

- 特性检测：`css/040-FeatureQuery`；
- 容器查询：`css/032-ContainerQuery`；
- 颜色：`css/034-ModernColorSpace`。

<!-- ============ 文档分隔线：007-css/065-HTMLSemanticSEO.md ============ -->

## 1. 语义化标签体系

### 1.1 文档结构标签

```html
<header>
  <nav aria-label="主导航">
    <ul>
      <li><a href="/">首页</a></li>
      <li><a href="/about">关于</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <header>
      <h1>文章标题</h1>
      <time datetime="2026-06-14">2026年6月14日</time>
    </header>
    <section>
      <h2>第一节</h2>
      <p>内容段落</p>
    </section>
    <section>
      <h2>第二节</h2>
      <p>内容段落</p>
    </section>
    <footer>
      <p>作者：张三</p>
    </footer>
  </article>

  <aside aria-label="侧边栏">
    <section>
      <h2>相关文章</h2>
      <ul>
        ...
      </ul>
    </section>
  </aside>
</main>

<footer>
  <p>&copy; 2026 示例网站</p>
</footer>
```

### 1.2 语义标签对照表

| 标签        | 语义          | 使用场景           |
| ----------- | ------------- | ------------------ |
| `<header>`  | 页眉/区块头部 | 页面顶部、文章头部 |
| `<nav>`     | 导航          | 主导航、面包屑     |
| `<main>`    | 主内容区      | 页面唯一主内容     |
| `<article>` | 独立内容      | 博客文章、新闻     |
| `<section>` | 内容分区      | 章节分组           |
| `<aside>`   | 附属内容      | 侧边栏、广告       |
| `<footer>`  | 页脚/区块尾部 | 版权信息、链接     |
| `<figure>`  | 自包含内容    | 图片、图表         |
| `<details>` | 可展开详情    | FAQ、补充说明      |
| `<time>`    | 时间/日期     | 发布日期、事件时间 |
| `<address>` | 联系信息      | 作者联系方式       |
| `<mark>`    | 标记/高亮     | 搜索结果高亮       |

### 1.3 反模式

```html
<!--  div 汤 -->
<div class="header">
  <div class="nav">
    <div class="nav-item">首页</div>
  </div>
</div>
<div class="main">
  <div class="article">
    <div class="title">标题</div>
  </div>
</div>

<!--  语义化 -->
<header>
  <nav>
    <a href="/">首页</a>
  </nav>
</header>
<main>
  <article>
    <h1>标题</h1>
  </article>
</main>
```

## 2. SEO 核心要素

### 2.1 页面元信息

```html
<head>
  <!-- 基础元信息 -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>页面标题 - 网站名称（建议 60 字符以内）</title>
  <meta name="description" content="页面描述，建议 150-160 字符" />
  <meta name="robots" content="index, follow" />

  <!-- Open Graph（社交媒体分享） -->
  <meta property="og:type" content="article" />
  <meta property="og:title" content="文章标题" />
  <meta property="og:description" content="文章描述" />
  <meta property="og:image" content="https://example.com/image.jpg" />
  <meta property="og:url" content="https://example.com/article" />

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="文章标题" />
  <meta name="twitter:description" content="文章描述" />
  <meta name="twitter:image" content="https://example.com/image.jpg" />

  <!-- 规范链接 -->
  <link rel="canonical" href="https://example.com/article" />

  <!-- 替代语言版本 -->
  <link rel="alternate" hreflang="en" href="https://example.com/en/article" />
  <link rel="alternate" hreflang="zh" href="https://example.com/zh/article" />
</head>
```

### 2.2 标题层级

```html
<!--  正确的标题层级 -->
<h1>页面主标题（每页仅一个）</h1>
<h2>章节标题</h2>
<h3>小节标题</h3>
<h2>另一个章节</h2>

<!--  错误的标题层级 -->
<h1>主标题</h1>
<h3>跳过了 h2</h3>
<!-- 错误 -->
<h2>标题</h2>
<h1>又出现 h1</h1>
<!-- 错误 -->
```

### 2.3 结构化数据（Schema.org）

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "文章标题",
    "author": {
      "@type": "Person",
      "name": "张三"
    },
    "datePublished": "2026-06-14",
    "dateModified": "2026-06-14",
    "image": "https://example.com/image.jpg",
    "publisher": {
      "@type": "Organization",
      "name": "示例网站",
      "logo": {
        "@type": "ImageObject",
        "url": "https://example.com/logo.png"
      }
    }
  }
</script>
```

常见 Schema.org 类型：

| 类型             | 用途       |
| ---------------- | ---------- |
| `Article`        | 文章       |
| `Product`        | 商品       |
| `FAQPage`        | FAQ 页面   |
| `HowTo`          | 教程       |
| `BreadcrumbList` | 面包屑导航 |
| `Organization`   | 组织/公司  |
| `WebSite`        | 网站搜索   |

### 2.4 面包屑导航

```html
<nav aria-label="面包屑">
  <ol itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/"><span itemprop="name">首页</span></a>
      <meta itemprop="position" content="1" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/blog"><span itemprop="name">博客</span></a>
      <meta itemprop="position" content="2" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name">当前文章</span>
      <meta itemprop="position" content="3" />
    </li>
  </ol>
</nav>
```

## 3. 无障碍与 SEO 交集

### 3.1 图片优化

```html
<!--  有 alt 文本 -->
<img src="chart.png" alt="2026年Q1销售增长趋势图，同比增长15%" />

<!--  装饰性图片 -->
<img src="divider.png" alt="" role="presentation" />

<!--  复杂图片配合长描述 -->
<figure>
  <img src="infographic.png" alt="信息图：全球碳排放趋势" />
  <figcaption>详细描述...</figcaption>
</figure>
```

### 3.2 链接文本

```html
<!--  模糊链接 -->
<a href="/article">点击这里</a>
<a href="/article">了解更多</a>

<!--  描述性链接 -->
<a href="/article">阅读关于CSS性能优化的完整指南</a>
```

### 3.3 ARIA 地标

```html
<header role="banner">
  <nav role="navigation" aria-label="主导航">
    <main role="main">
      <aside role="complementary">
        <footer role="contentinfo"></footer>
      </aside>
    </main>
  </nav>
</header>
```

## 4. 技术 SEO

### 4.1 页面加载性能

Core Web Vitals 对 SEO 排名的影响：

| 指标 | 目标值  | 优化方向                |
| ---- | ------- | ----------------------- |
| LCP  | < 2.5s  | 关键 CSS 内联、图片优化 |
| INP  | < 200ms | 减少主线程阻塞          |
| CLS  | < 0.1   | 预留尺寸、字体优化      |

### 4.2 robots.txt

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Sitemap: https://example.com/sitemap.xml
```

### 4.3 Sitemap

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2026-06-14</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

### 4.4 SSR/SSG 对 SEO 的影响

| 渲染模式 | SEO 友好度 | 说明                   |
| -------- | ---------- | ---------------------- |
| SSR      | 最佳       | 服务端返回完整 HTML    |
| SSG      | 最佳       | 构建时生成静态 HTML    |
| CSR      | 较差       | 需要额外处理（预渲染） |
| ISR      | 良好       | 增量静态再生           |

## 动手试试

1. 检查你的页面是否只有一个 `h1`，标题层级是否连续；
2. 给文章页补全 `title`、`description` 与结构化数据；
3. 用富媒体结果测试工具验证 JSON-LD；
4. 进阶挑战：做一份 SEO 检查清单并在真实页面走查。

## 核心知识点

> 一句话记住 SEO 语义：语义化标签建大纲，标题层级连续，`alt`/`description` 补语义，结构化数据拿富媒体摘要。

- 语义标签：header/main/article/section 构建大纲；
- 标题：每页一个 h1，层级不跳级；
- 元数据：title/description/canonical；
- 图片：描述性 alt；
- 结构化数据：JSON-LD + Schema.org；
- 链接：语义化文案与站内结构。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 标题跳级 | 大纲断裂 | 按层级使用 |
| 图片无 alt | 图片搜索丢失 | 描述性 alt |
| 结构化数据与内容不符 | 被判作弊 | 数据与页面一致 |
| 忽视移动端 | 排名下降 | 响应式 + viewport |

## 扩展学习

- 语义：`html5/009-SemanticTag`；
- 元数据：`html5/015-MetadataCharacterEncoding`；
- 结构化数据：`html5/032-MicrodataJSONLD`。

<!-- ============ 文档分隔线：007-css/066-ResponsiveImage.md ============ -->

## 1. 响应式图片问题

### 1.1 核心挑战

- **分辨率适配**：1x/2x/3x 屏幕需要不同分辨率图片
- **视口适配**：不同视口宽度需要不同尺寸图片
- **艺术指导**：不同屏幕可能需要不同裁切/构图
- **格式适配**：WebP/AVIF 等现代格式需要降级方案

### 1.2 带宽浪费

```
移动端加载 2000px 宽的图片:
  - 下载 500KB 数据
  - 浏览器缩放到 375px 显示
  - 浪费 ~400KB 带宽

使用响应式图片:
  - 下载 375px 宽的图片
  - 仅需 ~50KB 数据
  - 节省 90% 带宽
```

## 2. srcset 属性

### 2.1 分辨率描述符

```html
<img src="photo.jpg" srcset="photo-1x.jpg 1x, photo-2x.jpg 2x, photo-3x.jpg 3x" alt="描述" />
```

浏览器根据设备像素比（DPR）选择最合适的图片：

| 设备          | DPR | 选择的图片     |
| ------------- | --- | -------------- |
| 普通显示器    | 1x  | `photo-1x.jpg` |
| Retina 显示器 | 2x  | `photo-2x.jpg` |
| 高端手机      | 3x  | `photo-3x.jpg` |

### 2.2 宽度描述符

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w, photo-1600.jpg 1600w"
  alt="描述"
/>
```

`400w` 表示图片实际宽度为 400 像素。浏览器根据视口宽度和 DPR 计算需要的图片尺寸。

## 3. sizes 属性

### 3.1 基本用法

`sizes` 告诉浏览器图片在页面中的显示尺寸，帮助浏览器在解析 HTML 阶段就选择合适的图片：

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw,
            (max-width: 1200px) 50vw,
            33vw"
  alt="描述"
/>
```

解析逻辑：

- 视口 ≤ 600px：图片占 100% 视口宽度
- 视口 601-1200px：图片占 50% 视口宽度
- 视口 > 1200px：图片占 33% 视口宽度

### 3.2 sizes 计算示例

```
视口宽度: 900px
sizes 匹配: 50vw → 图片显示宽度 = 450px
DPR: 2x
需要图片宽度: 450 × 2 = 900px
选择: photo-800.jpg（最接近且不小于 900px 的选项）
```

### 3.3 常见 sizes 模式

```html
<!-- 全宽图片 -->
sizes="100vw"

<!-- 两列布局 -->
sizes="(max-width: 768px) 100vw, 50vw"

<!-- 三列网格 -->
sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"

<!-- 侧边栏 + 主内容 -->
sizes="(max-width: 768px) 100vw, calc(100vw - 300px)"
```

## 4. picture 元素

### 4.1 艺术指导

```html
<picture>
  <!-- 宽屏：横向构图 -->
  <source media="(min-width: 1024px)" srcset="photo-wide-1x.jpg 1x, photo-wide-2x.jpg 2x" />
  <!-- 平板：方形构图 -->
  <source media="(min-width: 640px)" srcset="photo-square-1x.jpg 1x, photo-square-2x.jpg 2x" />
  <!-- 手机：竖向构图 + 裁切 -->
  <img
    src="photo-portrait.jpg"
    srcset="photo-portrait-1x.jpg 1x, photo-portrait-2x.jpg 2x"
    alt="描述"
  />
</picture>
```

### 4.2 格式降级

```html
<picture>
  <source type="image/avif" srcset="photo.avif" />
  <source type="image/webp" srcset="photo.webp" />
  <img src="photo.jpg" alt="描述" />
</picture>
```

浏览器按 `<source>` 顺序检查，选择第一个支持的格式。

### 4.3 格式 + 尺寸组合

```html
<picture>
  <source
    type="image/avif"
    srcset="photo-400.avif 400w, photo-800.avif 800w, photo-1200.avif 1200w"
    sizes="(max-width: 768px) 100vw, 50vw"
  />
  <source
    type="image/webp"
    srcset="photo-400.webp 400w, photo-800.webp 800w, photo-1200.webp 1200w"
    sizes="(max-width: 768px) 100vw, 50vw"
  />
  <img
    src="photo-800.jpg"
    srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
    sizes="(max-width: 768px) 100vw, 50vw"
    alt="描述"
  />
</picture>
```

## 5. 图片优化策略

### 5.1 尺寸断点设计

```
常见断点:
  320px  → 小手机
  640px  → 大手机
  768px  → 平板竖屏
  1024px → 平板横屏 / 小笔记本
  1280px → 桌面
  1920px → 大屏

图片宽度建议:
  320w, 640w, 960w, 1280w, 1920w
```

### 5.2 懒加载

```html
<img
  src="photo.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w"
  sizes="100vw"
  loading="lazy"
  decoding="async"
  alt="描述"
/>
```

| 属性                   | 说明                          |
| ---------------------- | ----------------------------- |
| `loading="lazy"`       | 视口外图片延迟加载            |
| `decoding="async"`     | 异步解码，不阻塞渲染          |
| `fetchpriority="high"` | 高优先级加载（首屏 LCP 图片） |

### 5.3 首屏图片优化

```html
<!-- LCP 图片：预加载 + 高优先级 -->
<link
  rel="preload"
  as="image"
  href="hero-800.webp"
  imagesrcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  imagesizes="100vw"
  fetchpriority="high"
/>

<img
  src="hero-800.webp"
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="100vw"
  fetchpriority="high"
  alt="Hero 图片"
/>
```

### 5.4 防止布局偏移（CLS）

```html
<!-- 方式一：设置宽高属性 -->
<img src="photo.jpg" width="800" height="600" alt="描述" />

<!-- 方式二：CSS aspect-ratio -->
<img src="photo.jpg" style="aspect-ratio: 4/3; width: 100%;" alt="描述" />
```

## 6. 工具与自动化

### 5.1 图片生成

```bash
# 使用 sharp 生成多尺寸图片
npx sharp-cli -i photo.jpg -o photo-400.jpg resize 400
npx sharp-cli -i photo.jpg -o photo-800.jpg resize 800
npx sharp-cli -i photo.jpg -o photo-1200.jpg resize 1200

# 批量转换格式
npx sharp-cli -i "*.jpg" -o "./output/" format webp
```

### 5.2 构建工具集成

```javascript
// Vite + vite-plugin-imagetools
import { defineConfig } from 'vite';
import imagetools from 'vite-imagetools';

export default defineConfig({
  plugins: [imagetools()],
});
```

使用：

```html
<img
  src="/photo.jpg?format=webp&width=400;800;1200"
  srcset="/photo.jpg?width=400 400w, /photo.jpg?width=800 800w, /photo.jpg?width=1200 1200w"
  sizes="100vw"
  alt="描述"
/>
```

## 动手试试

1. 用 `srcset` + `sizes` 做响应式图片，用 Network 面板验证不同设备加载的图片；
2. 用 `<picture>` 实现“手机竖图、桌面横图”；
3. 给首屏图加 `preload`，其余加 `lazy`；
4. 进阶挑战：用 `object-fit: cover` 统一缩略图比例。

## 核心知识点

> 一句话记住响应式图片：`srcset` 给候选、`sizes` 说宽度、`picture` 换场景、`lazy` 延迟加载、`alt` 不能少。

- `srcset`：候选图 + `w`/`x` 描述符；
- `sizes`：声明显示宽度，浏览器择优；
- `<picture>` + `<source media>`：按条件换图；
- 格式：AVIF/WebP 体积更小；
- `loading="lazy"` 非首屏；
- 始终提供 `alt`。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 全部 lazy | 首屏变慢 | 首屏 eager |
| 无 sizes | 浏览器猜错 | 显式声明 |
| 格式单一 | 流量浪费 | 多格式 source |
| 缺 alt | 无障碍损失 | 描述性 alt |

## 扩展学习

- 完整教程：`html5/019-ImageResponsiveImage`；
- 对象适配：`css/049-CSSObjectFit`；
- 性能：`javascript/050-CoreWebVitalsAndPerformanceMetrics`。

<!-- ============ 文档分隔线：007-css/067-CSSProjectExampleResponsiveHomepage.md ============ -->

| 英雄区   | 全屏背景，打字机效果，向下滚动指示  |
| -------- | ----------------------------------- |
| 关于我   | 双栏布局，技能进度条动画            |
| 项目展示 | Grid 自适应卡片，悬停效果           |
| 技术栈   | 图标网格，悬停放大                  |
| 联系方式 | 表单 + 社交链接                     |
| 页脚     | 简洁信息                            |
| 暗色模式 | CSS 变量切换，偏好持久化            |
| 响应式   | 移动端/平板/桌面三档适配            |
| 滚动动画 | IntersectionObserver 驱动的入场动画 |

## 需求分析

### 设计需求

- 视觉风格：简洁现代，留白充足
- 配色：亮色模式白底深色文字，暗色模式深色底浅色文字
- 字体：系统字体栈，标题加粗
- 动画：流畅但不过度，尊重 prefers-reduced-motion

### 布局需求

- 桌面端（>= 1024px）：多栏布局，侧边导航
- 平板端（768px - 1023px）：双栏布局
- 移动端（< 768px）：单栏布局，汉堡菜单

## 完整代码

### HTML 结构

```html
<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Personal Homepage</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <nav class="navbar" id="navbar">
      <div class="navbar__container">
        <a href="#" class="navbar__logo">DevName</a>
        <button class="navbar__toggle" id="navToggle" aria-label="Toggle navigation">
          <span></span><span></span><span></span>
        </button>
        <ul class="navbar__menu" id="navMenu">
          <li><a href="#about" class="navbar__link">About</a></li>
          <li><a href="#projects" class="navbar__link">Projects</a></li>
          <li><a href="#skills" class="navbar__link">Skills</a></li>
          <li><a href="#contact" class="navbar__link">Contact</a></li>
          <li>
            <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
              <svg class="icon-sun" viewBox="0 0 24 24" width="20" height="20">
                <circle cx="12" cy="12" r="5" fill="currentColor" />
                <path
                  d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                />
              </svg>
              <svg class="icon-moon" viewBox="0 0 24 24" width="20" height="20">
                <path
                  fill="currentColor"
                  d="M12 3a9 9 0 1 0 9 9c0-.46-.04-.92-.1-1.36a5.39 5.39 0 0 1-4.4 2.26 5.4 5.4 0 0 1-3.14-9.8c-.44-.06-.9-.1-1.36-.1z"
                />
              </svg>
            </button>
          </li>
        </ul>
      </div>
    </nav>

    <section class="hero" id="hero">
      <div class="hero__content">
        <p class="hero__greeting">Hello, I'm</p>
        <h1 class="hero__name">Zhang San</h1>
        <p class="hero__title">
          <span class="typewriter" id="typewriter"></span>
          <span class="typewriter__cursor">|</span>
        </p>
        <div class="hero__cta">
          <a href="#projects" class="btn btn--primary">View Projects</a>
          <a href="#contact" class="btn btn--outline">Contact Me</a>
        </div>
      </div>
      <div class="hero__scroll-indicator">
        <span>Scroll Down</span>
        <div class="hero__arrow"></div>
      </div>
    </section>

    <section class="section about" id="about">
      <div class="container">
        <h2 class="section__title">About Me</h2>
        <div class="about__grid">
          <div class="about__photo">
            <div class="about__photo-frame">
              <img src="https://picsum.photos/400/500" alt="Profile photo" loading="lazy" />
            </div>
          </div>
          <div class="about__info">
            <p class="about__bio">
              A passionate full-stack developer with 5 years of experience in building web
              applications. I love creating elegant solutions to complex problems and contributing
              to open source projects.
            </p>
            <div class="about__stats">
              <div class="stat">
                <span class="stat__number">5+</span>
                <span class="stat__label">Years Experience</span>
              </div>
              <div class="stat">
                <span class="stat__number">30+</span>
                <span class="stat__label">Projects</span>
              </div>
              <div class="stat">
                <span class="stat__number">10+</span>
                <span class="stat__label">Open Source</span>
              </div>
            </div>
            <div class="about__skills">
              <div class="skill">
                <div class="skill__header">
                  <span class="skill__name">JavaScript / TypeScript</span>
                  <span class="skill__percent">90%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__progress" data-width="90"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__header">
                  <span class="skill__name">Vue / React</span>
                  <span class="skill__percent">85%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__progress" data-width="85"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__header">
                  <span class="skill__name">Node.js / Python</span>
                  <span class="skill__percent">75%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__progress" data-width="75"></div>
                </div>
              </div>
              <div class="skill">
                <div class="skill__header">
                  <span class="skill__name">MySQL / MongoDB</span>
                  <span class="skill__percent">70%</span>
                </div>
                <div class="skill__bar">
                  <div class="skill__progress" data-width="70"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section projects" id="projects">
      <div class="container">
        <h2 class="section__title">Projects</h2>
        <div class="projects__grid">
          <article class="project-card">
            <div class="project-card__image">
              <img src="https://picsum.photos/600/400?1" alt="Project 1" loading="lazy" />
              <div class="project-card__overlay">
                <a href="#" class="btn btn--small">Demo</a>
                <a href="#" class="btn btn--small">Code</a>
              </div>
            </div>
            <div class="project-card__body">
              <h3 class="project-card__title">E-Commerce Platform</h3>
              <p class="project-card__desc">Full-stack e-commerce with Vue3, Node.js, and MySQL</p>
              <div class="project-card__tags">
                <span>Vue3</span><span>Node.js</span><span>MySQL</span>
              </div>
            </div>
          </article>
          <article class="project-card">
            <div class="project-card__image">
              <img src="https://picsum.photos/600/400?2" alt="Project 2" loading="lazy" />
              <div class="project-card__overlay">
                <a href="#" class="btn btn--small">Demo</a>
                <a href="#" class="btn btn--small">Code</a>
              </div>
            </div>
            <div class="project-card__body">
              <h3 class="project-card__title">Task Management App</h3>
              <p class="project-card__desc">
                Real-time collaborative task board with drag-and-drop
              </p>
              <div class="project-card__tags">
                <span>React</span><span>TypeScript</span><span>Firebase</span>
              </div>
            </div>
          </article>
          <article class="project-card">
            <div class="project-card__image">
              <img src="https://picsum.photos/600/400?3" alt="Project 3" loading="lazy" />
              <div class="project-card__overlay">
                <a href="#" class="btn btn--small">Demo</a>
                <a href="#" class="btn btn--small">Code</a>
              </div>
            </div>
            <div class="project-card__body">
              <h3 class="project-card__title">Data Dashboard</h3>
              <p class="project-card__desc">
                Interactive analytics dashboard with real-time charts
              </p>
              <div class="project-card__tags">
                <span>D3.js</span><span>Python</span><span>FastAPI</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section skills" id="skills">
      <div class="container">
        <h2 class="section__title">Tech Stack</h2>
        <div class="skills__grid">
          <div class="skill-icon"><span>HTML5</span></div>
          <div class="skill-icon"><span>CSS3</span></div>
          <div class="skill-icon"><span>JavaScript</span></div>
          <div class="skill-icon"><span>TypeScript</span></div>
          <div class="skill-icon"><span>Vue3</span></div>
          <div class="skill-icon"><span>React</span></div>
          <div class="skill-icon"><span>Node.js</span></div>
          <div class="skill-icon"><span>Python</span></div>
          <div class="skill-icon"><span>MySQL</span></div>
          <div class="skill-icon"><span>Docker</span></div>
          <div class="skill-icon"><span>Git</span></div>
          <div class="skill-icon"><span>Linux</span></div>
        </div>
      </div>
    </section>

    <section class="section contact" id="contact">
      <div class="container">
        <h2 class="section__title">Contact</h2>
        <div class="contact__grid">
          <form class="contact__form" id="contactForm">
            <div class="form-group">
              <label for="name">Name</label>
              <input type="text" id="name" name="name" required />
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" required />
            </div>
            <div class="form-group">
              <label for="message">Message</label>
              <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn--primary btn--full">Send Message</button>
          </form>
          <div class="contact__info">
            <div class="contact__item">
              <h3>Email</h3>
              <p>hello@example.com</p>
            </div>
            <div class="contact__item">
              <h3>Location</h3>
              <p>Beijing, China</p>
            </div>
            <div class="contact__social">
              <a href="#" aria-label="GitHub">GitHub</a>
              <a href="#" aria-label="LinkedIn">LinkedIn</a>
              <a href="#" aria-label="Twitter">Twitter</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <div class="container">
        <p>&copy; 2024 DevName. All rights reserved.</p>
      </div>
    </footer>

    <script src="app.js"></script>
  </body>
</html>
```

### CSS 核心样式

```css
:root,
[data-theme='light'] {
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  --bg-card: #ffffff;
  --text-primary: #1a1a2e;
  --text-secondary: #6c757d;
  --accent: #4361ee;
  --accent-hover: #3a56d4;
  --accent-light: #eef1ff;
  --border: #e0e0e0;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  --shadow-hover: 0 8px 30px rgba(0, 0, 0, 0.12);
  --navbar-bg: rgba(255, 255, 255, 0.9);
  --skill-bar-bg: #e9ecef;
  --transition: 0.3s ease;
}

[data-theme='dark'] {
  --bg-primary: #0f0f23;
  --bg-secondary: #1a1a2e;
  --bg-card: #1e1e36;
  --text-primary: #e0e0e0;
  --text-secondary: #a0a0b8;
  --accent: #7c8cf8;
  --accent-hover: #6b7be8;
  --accent-light: #1e2040;
  --border: #2d2d4a;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  --shadow-hover: 0 8px 30px rgba(0, 0, 0, 0.4);
  --navbar-bg: rgba(15, 15, 35, 0.9);
  --skill-bar-bg: #2d2d4a;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans SC', sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  transition:
    background var(--transition),
    color var(--transition);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

/* Navbar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: var(--navbar-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid transparent;
  transition:
    border-color var(--transition),
    box-shadow var(--transition);
}

.navbar.scrolled {
  border-bottom-color: var(--border);
  box-shadow: var(--shadow);
}

.navbar__container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.navbar__logo {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent);
  text-decoration: none;
}

.navbar__menu {
  display: flex;
  align-items: center;
  gap: 32px;
  list-style: none;
}

.navbar__link {
  color: var(--text-primary);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 500;
  transition: color var(--transition);
  position: relative;
}

.navbar__link::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--accent);
  transition: width var(--transition);
}

.navbar__link:hover {
  color: var(--accent);
}
.navbar__link:hover::after {
  width: 100%;
}

.navbar__toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.navbar__toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  transition: all var(--transition);
}

/* Hero */
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 24px 40px;
  position: relative;
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--accent-light) 100%);
}

.hero__greeting {
  font-size: 1.2rem;
  color: var(--accent);
  font-weight: 500;
  margin-bottom: 8px;
  opacity: 0;
  animation: fadeInUp 0.6s ease 0.2s forwards;
}

.hero__name {
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: 800;
  margin-bottom: 16px;
  opacity: 0;
  animation: fadeInUp 0.6s ease 0.4s forwards;
}

.hero__title {
  font-size: 1.5rem;
  color: var(--text-secondary);
  margin-bottom: 32px;
  min-height: 2em;
  opacity: 0;
  animation: fadeInUp 0.6s ease 0.6s forwards;
}

.typewriter__cursor {
  animation: blink 1s step-end infinite;
}

.hero__cta {
  display: flex;
  gap: 16px;
  opacity: 0;
  animation: fadeInUp 0.6s ease 0.8s forwards;
}

.hero__scroll-indicator {
  position: absolute;
  bottom: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--text-secondary);
  font-size: 0.85rem;
  animation: fadeInUp 0.6s ease 1s forwards;
  opacity: 0;
}

.hero__arrow {
  width: 20px;
  height: 20px;
  border-right: 2px solid var(--text-secondary);
  border-bottom: 2px solid var(--text-secondary);
  transform: rotate(45deg);
  animation: bounceDown 1.5s ease infinite;
}

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 28px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
  transition: all var(--transition);
  border: 2px solid transparent;
}

.btn--primary {
  background: var(--accent);
  color: #fff;
  border-color: var(--accent);
}

.btn--primary:hover {
  background: var(--accent-hover);
  border-color: var(--accent-hover);
}

.btn--outline {
  background: transparent;
  color: var(--accent);
  border-color: var(--accent);
}

.btn--outline:hover {
  background: var(--accent);
  color: #fff;
}

.btn--small {
  padding: 8px 16px;
  font-size: 0.85rem;
}
.btn--full {
  width: 100%;
}

/* Sections */
.section {
  padding: 100px 0;
}

.section__title {
  font-size: 2rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 48px;
  position: relative;
}

.section__title::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  background: var(--accent);
  margin: 12px auto 0;
  border-radius: 2px;
}

/* About Grid */
.about__grid {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 48px;
  align-items: start;
}

.about__photo-frame {
  border-radius: 16px;
  overflow: hidden;
  box-shadow: var(--shadow);
  position: relative;
}

.about__photo-frame::after {
  content: '';
  position: absolute;
  inset: 0;
  border: 3px solid var(--accent);
  border-radius: 16px;
  transform: translate(8px, 8px);
  z-index: -1;
}

.about__photo-frame img {
  width: 100%;
  display: block;
}

.about__stats {
  display: flex;
  gap: 32px;
  margin: 24px 0;
}

.stat {
  text-align: center;
}
.stat__number {
  display: block;
  font-size: 2rem;
  font-weight: 700;
  color: var(--accent);
}
.stat__label {
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.skill {
  margin-bottom: 16px;
}
.skill__header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 6px;
  font-size: 0.9rem;
}
.skill__bar {
  height: 8px;
  background: var(--skill-bar-bg);
  border-radius: 4px;
  overflow: hidden;
}
.skill__progress {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--accent-hover));
  border-radius: 4px;
  width: 0;
  transition: width 1s ease;
}

/* Projects Grid */
.projects__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 24px;
}

.project-card {
  background: var(--bg-card);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition:
    transform var(--transition),
    box-shadow var(--transition);
}

.project-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-hover);
}

.project-card__image {
  position: relative;
  overflow: hidden;
  aspect-ratio: 3 / 2;
}

.project-card__image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.project-card:hover .project-card__image img {
  transform: scale(1.05);
}

.project-card__overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  opacity: 0;
  transition: opacity var(--transition);
}

.project-card:hover .project-card__overlay {
  opacity: 1;
}

.project-card__overlay .btn {
  color: #fff;
  border-color: #fff;
}
.project-card__overlay .btn:hover {
  background: #fff;
  color: #000;
}

.project-card__body {
  padding: 20px;
}
.project-card__title {
  font-size: 1.15rem;
  font-weight: 600;
  margin-bottom: 8px;
}
.project-card__desc {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-bottom: 12px;
}

.project-card__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.project-card__tags span {
  padding: 2px 10px;
  background: var(--accent-light);
  color: var(--accent);
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 500;
}

/* Skills Grid */
.skills__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 20px;
}

.skill-icon {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 24px 16px;
  background: var(--bg-card);
  border-radius: 12px;
  box-shadow: var(--shadow);
  transition:
    transform var(--transition),
    box-shadow var(--transition);
  cursor: default;
}

.skill-icon:hover {
  transform: translateY(-4px) scale(1.05);
  box-shadow: var(--shadow-hover);
}

.skill-icon span {
  margin-top: 8px;
  font-size: 0.85rem;
  font-weight: 500;
}

/* Contact */
.contact__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
}

.form-group {
  margin-bottom: 20px;
}
.form-group label {
  display: block;
  margin-bottom: 6px;
  font-weight: 500;
  font-size: 0.9rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid var(--border);
  border-radius: 8px;
  font-size: 1rem;
  background: var(--bg-card);
  color: var(--text-primary);
  transition: border-color var(--transition);
  outline: none;
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: var(--accent);
}

.contact__social {
  display: flex;
  gap: 16px;
  margin-top: 24px;
}
.contact__social a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 500;
}
.contact__social a:hover {
  text-decoration: underline;
}

/* Footer */
.footer {
  padding: 24px 0;
  text-align: center;
  color: var(--text-secondary);
  font-size: 0.85rem;
  border-top: 1px solid var(--border);
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes blink {
  50% {
    opacity: 0;
  }
}

@keyframes bounceDown {
  0%,
  100% {
    transform: rotate(45deg) translateY(0);
  }
  50% {
    transform: rotate(45deg) translateY(8px);
  }
}

.fade-in {
  opacity: 0;
  transform: translateY(30px);
  transition:
    opacity 0.6s ease,
    transform 0.6s ease;
}

.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Responsive */
@media (max-width: 768px) {
  .navbar__toggle {
    display: flex;
  }
  .navbar__menu {
    position: fixed;
    top: 64px;
    left: 0;
    right: 0;
    background: var(--navbar-bg);
    backdrop-filter: blur(12px);
    flex-direction: column;
    padding: 24px;
    gap: 16px;
    border-bottom: 1px solid var(--border);
    transform: translateY(-100%);
    opacity: 0;
    pointer-events: none;
    transition: all var(--transition);
  }
  .navbar__menu.open {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
  }
  .about__grid {
    grid-template-columns: 1fr;
  }
  .about__photo {
    max-width: 300px;
    margin: 0 auto;
  }
  .contact__grid {
    grid-template-columns: 1fr;
  }
  .hero__cta {
    flex-direction: column;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### JavaScript 交互

```javascript
const navbar = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const themeToggle = document.getElementById('themeToggle');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
});

navToggle.addEventListener('click', () => {
  navMenu.classList.toggle('open');
});

document.querySelectorAll('.navbar__link').forEach((link) => {
  link.addEventListener('click', () => navMenu.classList.remove('open'));
});

function initTheme() {
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
}

themeToggle.addEventListener('click', () => {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('theme', next);
});

initTheme();

const titles = ['Full-Stack Developer', 'Open Source Enthusiast', 'Problem Solver'];
let titleIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typewriter = document.getElementById('typewriter');

function type() {
  const current = titles[titleIndex];
  if (isDeleting) {
    typewriter.textContent = current.substring(0, charIndex - 1);
    charIndex--;
  } else {
    typewriter.textContent = current.substring(0, charIndex + 1);
    charIndex++;
  }

  let delay = isDeleting ? 50 : 100;

  if (!isDeleting && charIndex === current.length) {
    delay = 2000;
    isDeleting = true;
  } else if (isDeleting && charIndex === 0) {
    isDeleting = false;
    titleIndex = (titleIndex + 1) % titles.length;
    delay = 500;
  }

  setTimeout(type, delay);
}

type();

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        const progressBars = entry.target.querySelectorAll('.skill__progress');
        progressBars.forEach((bar) => {
          bar.style.width = bar.dataset.width + '%';
        });
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll('.fade-in, .about, .projects, .skills, .contact').forEach((el) => {
  el.classList.add('fade-in');
  observer.observe(el);
});
```

## 运行说明

直接用浏览器打开 HTML 文件即可。文件结构：

```
homepage/
  index.html
  style.css
  app.js
```

## 扩展方向

1. **粒子背景** -- Canvas 粒子动画
2. **3D 卡片** -- CSS 3D 变换
3. **平滑滚动** -- Locomotive Scroll
4. **国际化** -- 多语言支持
5. **PWA** -- 离线访问
6. **CMS** -- 接入 Headless CMS

---

## 关键代码速查

### CSS 变量主题

```css
:root {
  --accent: #4361ee;
  --bg: #fff;
}
[data-theme='dark'] {
  --accent: #7c8cf8;
  --bg: #0f0f23;
}
```

### Flex 居中

```css
display: flex;
align-items: center;
justify-content: center;
```

### Grid 自适应

```css
display: grid;
grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
gap: 24px;
```

### 毛玻璃导航

```css
background: rgba(255, 255, 255, 0.9);
backdrop-filter: blur(12px);
```

### 悬停上浮

```css
transition:
  transform 0.3s,
  box-shadow 0.3s;
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}
```

### IntersectionObserver 入场

```javascript
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  },
  { threshold: 0.1 }
);
document.querySelectorAll('.fade-in').forEach((el) => observer.observe(el));
```

## 动手试试

1. 按文档步骤从零搭建响应式首页骨架；
2. 用 Flexbox 重构导航，用 Grid 重构卡片区；
3. 加深色主题（只覆盖颜色变量）；
4. 进阶挑战：用容器查询让卡片组件自适配，并用 Lighthouse 跑分对比。

## 核心知识点

> 一句话记住本项目：移动优先、语义化结构、设计令牌、Flex/Grid 布局、媒体查询增强，最终用性能指标验证。

- 项目分层：reset → 变量 → 基础 → 组件 → 布局；
- 导航：语义化 nav + flex；
- 卡片：grid + auto-fit/minmax；
- 主题：颜色全部走变量，深色覆盖；
- 响应式：min-width 断点增强；
- 验收：Lighthouse/移动端实测。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 一上来写桌面端 | 移动体验差 | 移动优先 |
| 样式全堆一个文件 | 难维护 | 按组件拆分 |
| 忘记对比度 | 深色看不清 | 验证 AA |
| 图片不响应 | 流量浪费 | srcset/object-fit |

## 扩展学习

- Grid：`css/022-CSS3GridGridLayout`；
- Flex：`css/021-CSS3FlexboxFlexLayout`；
- 响应式：`css/033-ResponsiveDesign`；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`。

<!-- ============ 文档分隔线：007-css/068-Grid.md ============ -->

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

## 动手试试

1. 用 `display: grid` + `repeat(auto-fit, minmax(200px, 1fr))` 做响应式卡片墙；
2. 用 `grid-template-areas` 布局“头部/主体/侧栏/页脚”；
3. 用 `grid-column: 1 / -1` 让元素跨行；
4. 进阶挑战：对比 Grid 与 Flexbox 在同一个布局上的实现。

## 核心知识点

> 一句话记住 Grid：二维布局系统，轨道、区域、网格线三件套；`1fr` 分空间，`minmax` 控范围，`auto-fit` 自适应。

- 轨道：`grid-template-columns/rows`；
- `1fr`：剩余空间等分；
- `minmax(min, max)`：范围控制；
- 区域：`grid-template-areas` + `grid-area`；
- 网格线：`grid-column: 1 / -1`；
- 隐式网格：`grid-auto-rows` 控制自动轨道。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 内容撑破 1fr | 溢出 | `minmax(0, 1fr)` |
| 区域名不一致 | 布局失效 | 命名对齐 |
| 隐式轨道高度 | 元素挤压 | grid-auto-rows |
| 与 flex 混用不清 | 布局混乱 | 明确一维/二维 |

## 扩展学习

- 完整教程：`css/022-CSS3GridGridLayout`；
- 对比：`css/021-CSS3FlexboxFlexLayout`；
- 实战：`css/067-CSSProjectExampleResponsiveHomepage`。

<!-- ============ 文档分隔线：007-css/069-Transform3D.md ============ -->

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

## 动手试试

1. 用 `transform: translate()`/`rotate()`/`scale()` 组合一个卡片翻转；
2. 给容器加 `perspective`，体验 3D 景深；
3. 用 `transform-style: preserve-3d` 做翻转卡片；
4. 进阶挑战：做鼠标跟随的 3D 倾斜卡片。

## 核心知识点

> 一句话记住 3D 变换：`transform` 平移/旋转/缩放，`perspective` 给景深，`preserve-3d` 保留立体，`backface-visibility` 管背面。

- 2D：translate/rotate/scale/skew；
- 3D：rotateX/rotateY/translateZ；
- `perspective`：父容器设置景深；
- `transform-style: preserve-3d`：子元素保留 3D；
- `backface-visibility: hidden`：翻转卡片背面隐藏；
- transform 走合成层，动画性能好。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| perspective 位置错误 | 无景深 | 设在父容器 |
| 忘记 preserve-3d | 子元素压平 | 显式声明 |
| 过度 3D | 视觉杂乱 | 克制使用 |
| 与 fixed 冲突 | 包含块改变 | 注意 transform 副作用 |

## 扩展学习

- 动画：`css/028-CSSAnimationTransition`；
- 层叠：`css/016-StackingContext`；
- 性能：`css/042-CSSPerformanceOptimizationDetailed`。

<!-- ============ 文档分隔线：007-css/070-ScopeAtRule.md ============ -->

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

## 动手试试

1. 用 `@scope (.card)` 限定卡片内标题样式；
2. 用 `:scope` 引用根元素；
3. 对比 `@scope` 与 BEM 类名的可维护性；
4. 进阶挑战：用 `@scope` 配合组件样式。

## 核心知识点

> 一句话记住 @scope：`@scope (根) { 规则 }` 把样式限定在子树内，比手写长选择器更清晰，`:scope` 指根元素。

- `@scope (selector) { ... }` 限定作用域；
- `:scope` 指向作用域根；
- 支持 `to` 定义边界；
- 替代深层选择器，避免命名前缀；
- 浏览器支持：Chrome 118+、Safari 17.4+。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 依赖编译 | 老浏览器不支持 | 构建转译或 BEM |
| 作用域边界不清 | 样式泄漏 | 明确根与边界 |
| 与 BEM 混用 | 风格冲突 | 团队统一 |

## 扩展学习

- 嵌套：`css/071-CSSNesting`；
- 架构：`css/043-CSSArchitectureMethodology`；
- 新特性：`css/064-CSSNewFeatures`。

<!-- ============ 文档分隔线：007-css/071-CSSNesting.md ============ -->

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

## 动手试试

1. 用嵌套语法重写一个按钮组件（含 hover 与 ::before）；
2. 用 `&` 引用父选择器写修饰符；
3. 对比原生嵌套与 Sass 的输出；
4. 进阶挑战：嵌套媒体查询。

## 核心知识点

> 一句话记住嵌套：子规则继承父选择器，`&` 引用父级；`&:hover`、`&::before`、`&-modifier` 是三大用法。

- 基础：`父 { 子 { } }` 编译为 `父 子`；
- `&` 代表父选择器；
- 常用：`&:hover`、`&::before`、`&--active`；
- 嵌套媒体查询跟随父级；
- 浏览器原生支持，也可编译；
- 控制嵌套深度 ≤ 3。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 深度过深 | 选择器冗长 | 拆组件 |
| `&` 误用 | 生成意外选择器 | 先展开验证 |
| 兼容性 | 旧浏览器 | 构建转译 |

## 扩展学习

- 原生嵌套：`css/041-CSSNativeNesting`；
- 作用域：`css/070-ScopeAtRule`；
- Sass：`css/054-Sass`。
