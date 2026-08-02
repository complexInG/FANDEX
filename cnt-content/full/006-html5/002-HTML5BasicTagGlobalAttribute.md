---
order: 20
title: HTML5 基础标签与全局属性
module: 'html5'
category: 前端技术
difficulty: intermediate
description: 文本、列表、表格标签与全局属性详解。
author: Anonymous
updated: '2026-08-02'
related:
  - 'html5/001-HTML5OverviewCoreFeature'
  - 'html5/003-SemanticTag'
  - 'html5/004-Accessibility'
prerequisites: []
---

## 0. 核心认知：HTML 标签就是“搭积木”

在开始背标签之前，先理解一个道理：HTML 标签的本质，是告诉浏览器“这块内容是什么”，而不是“这块内容长什么样”。

| 你要表达的含义 | 用这个标签 | 而不是 |
| --- | --- | --- |
| 最重要的标题 | `<h1>` | 用大字加粗的 `<div>` |
| 一段普通文字 | `<p>` | 用 `<div>` 硬换行 |
| 一组并列的项目 | `<ul>` + `<li>` | 用 `<div>` + `<br>` 硬排 |
| 一个可点击的链接 | `<a>` | 用 `<div>` 加点击事件 |

记住：选择标签的唯一标准是“这个内容在语义上是什么”，而不是“我希望它长什么样”。样式是 CSS 的工作，不是 HTML 的工作。

### 0.1 使用频率分级：哪些标签必须背

| 标签 | 频率 | 说明 |
| --- | --- | --- |
| `<h1>`-`<h6>` | 必背 | 每页必用，构建标题层级 |
| `<p>` | 必背 | 每页必用，承载正文段落 |
| `<ul>`/`<ol>`/`<li>` | 必背 | 导航、列表必用 |
| `<a>` | 必背 | 链接必用 |
| `<img>` | 必背 | 图片必用 |
| `<span>` | 常用 | 行内包裹，配合样式或脚本 |
| `<strong>`/`<em>` | 了解 | 强调语义，CSS 可辅助表现 |
| `<mark>`/`<small>`/`<del>`/`<ins>` | 用到再查 | 低频语义标签，不用死记 |
| `<sub>`/`<sup>` | 知道即可 | 几乎不用，遇到时查文档 |

讲解：标为“必背”的标签要求手写无误；“用到再查”和“知道即可”的标签了解存在即可，遇到时再查文档。

## 1. 基础文本标签

基础文本标签用于定义和格式化网页中的文本内容，是构建网页结构的基础。

### 1.1 标题标签

标题标签用于定义网页中的标题，从 `<h1>` 到 `<h6>`，级别依次递减。
| 标签 | 描述 | 语义 |
|------|------|------|
| `<h1>` | 一级标题（必背） | 最重要的标题，通常用于页面主标题 |
| `<h2>` | 二级标题（必背） | 次要标题，通常用于章节标题 |
| `<h3>` | 三级标题（必背） | 子章节标题 |
| `<h4>` | 四级标题（了解） | 更小的子章节标题 |
| `<h5>` | 五级标题（了解） | 更次要的标题 |
| `<h6>` | 六级标题（了解） | 最次要的标题 |
**示例**：

```html
<h1>网站主标题</h1>
<h2>章节标题</h2>
<h3>子章节标题</h3>
<h4>子子章节标题</h4>
```

**讲解：**

- `<h1>` 到 `<h6>` 表示六级标题，级别逐级降低，构成页面大纲；
- 每页只保留一个 `<h1>`，后续章节从 `<h2>` 开始依次递进，不要跳级；
- 标题表达语义层级，字号样式应交给 CSS，而不是用标题硬撑视觉效果。

**最佳实践**：

- 每个页面应该只有一个 `<h1>` 标签，用于页面的主标题
- 标题应该按照层级顺序使用，不要跳过层级
- 标题内容应该简洁明了，能够准确反映章节内容

### 1.2 段落标签

`<p>` 标签用于定义段落，是最常用的文本容器之一。
**示例**：

```html
<p>这是一个段落。段落是网页中最基本的文本单位，用于组织和展示文本内容。</p>
<p>这是另一个段落。每个段落都会自动在前后添加空白，使文本更易于阅读。</p>
```

### 1.3 行内文本容器

`<span>` 标签是一个行内元素，用于对文本的一部分进行样式设置或标记。
**示例**：

```html
<p>这是一段文本，其中 <span style="color: red;">红色部分</span> 是使用 span 标签标记的。</p>
```

### 1.4 强调标签

用于对文本进行强调，具有语义含义。
| 标签 | 描述 | 语义 |
|------|------|------|
| `<strong>` | 加粗（了解） | 表示重要内容 |
| `<em>` | 倾斜（了解） | 表示强调内容 |
| `<mark>` | 标记（用到再查） | 表示突出显示的内容 |
| `<small>` | 小号字体（用到再查） | 表示辅助性内容 |
| `<del>` | 删除线（用到再查） | 表示已删除的内容 |
| `<ins>` | 下划线（用到再查） | 表示已插入的内容 |
| `<sub>` | 下标（知道即可） | 表示下标文本 |
| `<sup>` | 上标（知道即可） | 表示上标文本 |
**示例**：

```html
<p>这是 <strong>重要内容</strong>，这是 <em>强调内容</em>。</p>
<p>这是 <mark>突出显示</mark> 的内容。</p>
<p>这是 <small>辅助性内容</small>。</p>
<p>这是 <del>已删除</del> 的内容，这是 <ins>已插入</ins> 的内容。</p>
<p>水的化学式是 H<sub>2</sub>O，2 的平方是 2<sup>2</sup>。</p>
```

### 1.5 换行和分割线

| 标签   | 描述                                   |
| ------ | -------------------------------------- |
| `<br>` | 换行标签，用于在文本中插入换行         |
| `<hr>` | 分割线标签，用于在页面中插入水平分割线 |

**示例**：

```html
<p>这是第一行<br />这是第二行</p>
<hr />
<p>这是分割线下面的内容</p>
```

## 2. 列表标签

列表标签用于组织和展示一系列相关的项目。

### 2.1 无序列表

无序列表使用 `<ul>` 标签定义，列表项使用 `<li>` 标签定义，默认使用圆点作为列表项标记。
**示例**：

```html
<h3>购物清单</h3>
<ul>
  <li>苹果</li>
  <li>香蕉</li>
  <li>橙子</li>
  <li>牛奶</li>
</ul>
```

### 2.2 有序列表

有序列表使用 `<ol>` 标签定义，列表项使用 `<li>` 标签定义，默认使用数字作为列表项标记。
**属性**：

- `start`: 指定列表的起始编号
- `reversed`: 倒序列表
- `type`: 指定编号类型（1, A, a, I, i）
  **示例**：

```html
 <h3>步骤说明</h3>
 <ol>
  <li>准备材料</li>
  <li>混合 ingredients</li>
  <li>加热</li>
  <li>冷却</li>
 </ol>
 <h3>倒序列表</h3>
 <ol reversed>
  <li>第四步</li>
  <li>第三步</li>
  <li>第二步</li>
  <li>第一步</li>
 </ol>
 <h3>字母编号列表</h3>
 <ol type="A">
  <li>选项 A</li>
  <li>选项 B</li>
  <li>选项 C</li>
 </ol>
```

**讲解：**

- `<ol>` 表示有序列表，列表项按编号顺序排列，适合步骤说明；
- `start` 指定起始编号，`reversed` 让编号倒序，`type` 切换编号样式（1/A/a/I/i）；
- 编号由浏览器自动生成，无需手工书写数字，便于插入或删除列表项。

### 2.3 定义列表

定义列表使用 `<dl>` 标签定义，术语使用 `<dt>` 标签定义，描述使用 `<dd>` 标签定义。
**示例**：

```html
<h3>术语解释</h3>
<dl>
<dt>HTML</dt>
<dd>超文本标记语言，用于创建网页结构</dd>
<dt>CSS</dt>
<dd>层叠样式表，用于美化网页</dd>
<dt>JavaScript</dt>
<dd>脚本语言，用于实现网页交互</dd>
</dl>
```

**讲解：**

- `<dl>` 是定义列表容器，`<dt>` 表示术语，`<dd>` 表示术语的说明；
- 一个 `<dt>` 可以对应多个 `<dd>`，用于表达“一对多”的释义关系；
- 定义列表适合术语表、键值对数据，不要用它做纯视觉排版。

### 2.4 嵌套列表

列表可以嵌套使用，创建层次结构。
**示例**：

```html
 <h3>课程大纲</h3>
 <ul>
  <li>HTML 基础
  <ul>
  <li>标签语法</li>
  <li>语义化标签</li>
  <li>表单元素</li>
  </ul>
  </li>
  <li>CSS 基础
  <ul>
  <li>选择器</li>
  <li>盒模型</li>
  <li>布局技巧</li>
  </ul>
  </li>
  <li>JavaScript 基础
  <ul>
  <li>变量和数据类型</li>
  <li>控制流</li>
  <li>函数</li>
  </ul>
  </li>
 </ul>
```

**讲解：**

- 嵌套列表通过“`<li>` 内再放 `<ul>`/`<ol>`”实现多级层级；
- 浏览器会自动缩进子列表，形成清晰的目录结构；
- 注意嵌套深度不要过深，超过三层时应考虑用页面导航替代。

### 2.5 三种列表的选择指南

| 场景 | 用什么 | 为什么 |
| --- | --- | --- |
| 导航菜单、购物清单、功能列表 | `<ul>` | 项目之间是并列关系，顺序无关紧要 |
| 操作步骤、排行榜、流程说明 | `<ol>` | 顺序本身有意义，1 到 2 到 3 不可颠倒 |
| 术语表、问答对、键值对 | `<dl>` | 每个项目由“术语 + 定义”成对出现 |

## 3. 超链接与多媒体

### 3.1 超链接

超链接使用 `<a>` 标签定义，用于链接到其他网页、文件或位置。
**属性**：

- `href`: 指定链接目标
- `target`: 指定打开链接的方式
- `_self`: 在当前窗口打开（默认）
- `_blank`: 在新窗口打开
- `_parent`: 在父框架打开
- `_top`: 在整个窗口打开
- `title`: 指定悬停提示文字
- `rel`: 指定链接与当前页面的关系
  **示例**：

```html
 <!-- 链接到外部网站 -->
 <a href="https://www.example.com" target="_blank">访问示例网站</a>
 <!-- 链接到同一网站的其他页面 -->
 <a href="about.html">关于我们</a>
 <!-- 链接到页面内的锚点 -->
 <a href="#section1">跳转到第一部分</a>
 <!-- 链接到电子邮件 -->
 <a href="mailto:info@example.com">发送邮件</a>
 <!-- 链接到电话 -->
 <a href="tel:+1234567890">拨打电话</a>
```

**讲解：**

- `href` 决定链接目标：网页、锚点、`mailto:` 邮件或 `tel:` 电话；
- `target="_blank"` 在新标签页打开，应同时搭配 `rel="noopener"` 防止反向标签页劫持；
- 锚点链接 `#section1` 跳转到页面内 `id="section1"` 的元素，无需重新加载页面。

### 3.2 图像

图像使用 `<img>` 标签定义，用于在网页中插入图片。
**属性**：

- `src`: 指定图像源文件路径
- `alt`: 指定图像的替代文本（对 SEO 和无障碍至关重要）
- `width`: 指定图像宽度
- `height`: 指定图像高度
- `title`: 指定悬停提示文字
- `loading`: 指定图像加载方式（`lazy` 用于延迟加载）
  **示例**：

```html
<!-- 基本图像 -->
<img src="images/photo.jpg" alt="美丽的风景" width="400" height="300" />
<!-- 带有标题的图像 -->
<img src="images/logo.png" alt="网站标志" title="网站标志" />
<!-- 延迟加载的图像 -->
<img src="images/large-image.jpg" alt="大型图像" loading="lazy" />
```

**讲解：**

- `src` 指定图片地址，`alt` 提供替代文本，图片加载失败时仍可理解内容；
- 显式给出 `width`/`height` 可让浏览器提前预留空间，避免布局抖动（CLS）；
- `loading="lazy"` 让图片进入视口附近再加载，适合长页面中的非首屏图片。

### 3.3 其他多媒体标签

| 标签       | 描述             |
| ---------- | ---------------- |
| `<audio>`  | 用于播放音频文件 |
| `<video>`  | 用于播放视频文件 |
| `<iframe>` | 用于嵌入其他网页 |

**示例**：

```html
<!-- 音频播放器 -->
<audio controls>
<source src="audio/song.mp3" type="audio/mpeg" />
您的浏览器不支持音频元素。
</audio>
<!-- 视频播放器 -->
<video controls width="600">
<source src="video/movie.mp4" type="video/mp4" />
您的浏览器不支持视频元素。
</video>
<!-- 嵌入网页 -->
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.1422937950146!2d-74.0061380845947!3d40.71277577933185!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25a22a3bda30d%3A0xb89d1fe6bc499443!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sus!4v1620000000000!5m2!1sen!2sus"
  width="600"
  height="450"
  style="border: 0"
  allowfullscreen
  loading="lazy"
></iframe>
```

**讲解：**

- `<audio>`/`<video>` 内部可放多个 `<source>` 供浏览器按格式依次尝试，fallback 文本用于不支持时的提示；
- `controls` 属性显示浏览器原生控制条，移除后需自行实现播放控制；
- `<iframe>` 用于嵌入第三方页面，应设置 `width`/`height` 并谨慎使用 `allowfullscreen`。

## 4. 全局属性

全局属性是几乎所有 HTML 元素都支持的属性，用于提供额外的信息或功能。

### 4.1 基本全局属性

| 属性              | 描述                                            | 示例                                   |
| ----------------- | ----------------------------------------------- | -------------------------------------- |
| `id`              | 唯一标识符，用于通过 JavaScript 或 CSS 选择元素 | `id="header"`                          |
| `class`           | 样式类名，用于为元素应用 CSS 样式               | `class="container main"`               |
| `style`           | 行内样式，直接在元素上定义样式                  | `style="color: red; font-size: 16px;"` |
| `title`           | 悬停提示文字，当鼠标悬停在元素上时显示          | `title="这是一个提示"`                 |
| `hidden`          | 隐藏元素，使其不显示在页面上                    | `hidden`                               |
| `contenteditable` | 使元素内容可编辑                                | `contenteditable=""`                   |
| `spellcheck`      | 启用或禁用拼写检查                              | `spellcheck=""`                        |
| `tabindex`        | 指定元素在 Tab 键顺序中的位置                   | `tabindex="1"`                         |
| `accesskey`       | 指定访问元素的快捷键                            | `accesskey="k"`                        |

**示例**：

```html
 <!-- 使用 id 和 class -->
 <div id="header" class="container">
  <h1>网站标题</h1>
 </div>
 <!-- 使用行内样式 -->
 <p style="color: blue; font-weight: bold;">这是蓝色粗体文本</p>
 <!-- 使用 title 属性 -->
 <a href="#" title="点击这里">链接</a>
 <!-- 使用 hidden 属性 -->
 <div hidden>这个元素是隐藏的</div>
 <!-- 使用 contenteditable 属性 -->
 <div contenteditable="">点击此处编辑内容</div>
```

**讲解：**

- `id` 在页面内必须唯一，`class` 可复用，二者分别是“身份”与“分类”；
- `hidden` 是布尔属性，存在即生效，等价于 CSS `display: none` 的语义层实现；
- `contenteditable` 让普通元素变为可编辑区域，多用于富文本与笔记类应用。

### 4.2 自定义数据属性

`data-*` 属性用于存储自定义数据，这些数据可以通过 JavaScript 访问。
**语法**：`data-属性名="值"`
**示例**：

```html
 <!-- 存储产品信息 -->
 <div class="product" data-id="123" data-name="iPhone 13" data-price="799">
  <h3>iPhone 13</h3>
  <p>价格: $799</p>
 </div>
 <!-- 通过 JavaScript 访问 -->
 <script>
  const product = document.querySelector('.product');
  const productId = product.dataset.id;
  const productName = product.dataset.name;
  const productPrice = product.dataset.price;
  console.log(`产品 ID: ${productId}, 名称: ${productName}, 价格: $${productPrice}`);
 </script>
```

**讲解：**

- `data-*` 以 `data-` 前缀承载自定义数据，不污染标准属性命名空间；
- JavaScript 通过 `element.dataset` 读取，`data-price` 对应 `dataset.price`；
- 适合存放与元素绑定的业务数据，复杂状态仍应交给框架或状态管理。

### 4.3 其他全局属性

| 属性        | 描述                         | 示例                                             |
| ----------- | ---------------------------- | ------------------------------------------------ |
| `lang`      | 指定元素内容的语言           | `lang="zh-CN"`                                   |
| `dir`       | 指定文本方向                 | `dir="ltr"` (从左到右) 或 `dir="rtl"` (从右到左) |
| `translate` | 指定是否翻译元素内容         | `translate="no"`                                 |
| `draggable` | 指定元素是否可拖动           | `draggable=""`                                   |
| `dropzone`  | 指定元素作为放置目标时的行为 | `dropzone="copy"`                                |

**示例**：

```html
 <!-- 指定语言 -->
 <div lang="en">This is English text</div>
 <div lang="zh-CN">这是中文文本</div>
 <!-- 指定文本方向 -->
 <div dir="rtl">مرحبا بالعالم</div> <!-- 阿拉伯语，从右到左 -->
 <!-- 指定不可翻译 -->
 <div translate="no">品牌名称: Apple</div>
 <!-- 指定可拖动 -->
 <div draggable="">可拖动元素</div>
```

**讲解：**

- `lang` 与 `dir` 影响拼写检查、翻译工具和文本方向，多语言页面必须正确设置；
- `translate="no"` 告诉翻译工具不要翻译品牌名等专有内容；
- `draggable` 开启 HTML5 拖拽，配合拖拽事件实现排序、上传等交互。

## 5. 语义化标签

HTML5 引入了一系列语义化标签，用于更清晰地描述网页结构。
| 标签 | 描述 |
|------|------|
| `<header>` | 页面或section的头部 |
| `<nav>` | 导航链接区域 |
| `<main>` | 页面的主要内容 |
| `<section>` | 文档中的节 |
| `<article>` | 独立的内容块 |
| `<aside>` | 侧边栏或附加内容 |
| `<footer>` | 页面或section的底部 |
| `<figure>` | 图表、图像等 |
| `<figcaption>` | 图表的标题 |

注意：`<div>` 是“无语义容器”，仅用于样式分组或脚本挂载；能用上面任一语义标签表达时，就不要用 `div`。

**示例**：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>语义化标签示例</title>
  </head>
  <body>
    <header>
      <h1>网站标题</h1>
      <nav>
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">关于</a></li>
          <li><a href="#">服务</a></li>
          <li><a href="#">联系</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <section>
        <h2>新闻</h2>
        <article>
          <h3>最新新闻标题</h3>
          <p>新闻内容...</p>
        </article>
        <article>
          <h3>另一则新闻</h3>
          <p>新闻内容...</p>
        </article>
      </section>
      <aside>
        <h3>侧边栏</h3>
        <p>侧边栏内容...</p>
      </aside>
    </main>
    <footer>
      <p>2026 网站名称. 保留所有权利.</p>
    </footer>
  </body>
</html>
```

**讲解：**

- 页面骨架由 `header`、`nav`、`main`、`aside`、`footer` 组成，层级一目了然；
- `main` 只出现一次，内部按主题拆分为 `section`，独立内容用 `article`；
- 该结构对搜索引擎与屏幕阅读器都友好，是“语义化优先”的标准写法。

## 6. 实际应用示例

### 6.1 示例 1：基本网页结构（纯 HTML 骨架）

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>基本网页结构</title>
    <!-- 注意：本示例只有 HTML 骨架，没有 CSS 样式 -->
    <!-- 样式将在后续 CSS 课程中学习 -->
  </head>
  <body>
    <!-- ====== 页面头部 ====== -->
    <header>
      <h1>我的网站</h1>
      <nav>
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">关于</a></li>
          <li><a href="#">服务</a></li>
          <li><a href="#">联系</a></li>
        </ul>
      </nav>
    </header>

    <!-- ====== 页面主体 ====== -->
    <main>
      <section>
        <h2>欢迎访问我的网站</h2>
        <p>这是一个使用 HTML5 基础标签构建的网页。</p>
        <p>HTML5 提供了丰富的标签和属性，用于创建结构清晰、语义化的网页。</p>
      </section>

      <section>
        <h2>服务列表</h2>
        <ul>
          <li>网站设计</li>
          <li>前端开发</li>
          <li>后端开发</li>
          <li>移动应用开发</li>
        </ul>
      </section>

      <section>
        <h2>联系我们</h2>
        <p>邮箱：<a href="mailto:info@example.com">info@example.com</a></p>
        <p>电话：<a href="tel:+1234567890">123-456-7890</a></p>
      </section>
    </main>

    <!-- ====== 页面底部 ====== -->
    <footer>
      <p>&copy; 2026 我的网站. 保留所有权利.</p>
    </footer>
  </body>
</html>
```

**讲解：**

- 这个页面在浏览器中会显示为“白底黑字”的朴素风格——这正是 HTML 的本职工作：只负责内容和结构，不负责美化；
- `header` 包住标题与导航，`main` 包住三个 `section`，`footer` 放版权信息，三段结构一目了然；
- 导航里的 `<ul>` 和“服务列表”里的 `<ul>` 表达的都是“一组并列项目”，语义正确；
- `mailto:` 与 `tel:` 链接让用户点击后直接唤起邮件与拨号应用。

### 6.2 示例 2：产品展示页面（纯 HTML 骨架）

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>产品展示</title>
    <!-- 注意：本示例只有 HTML 骨架，没有 CSS 样式 -->
  </head>
  <body>
    <header>
      <h1>产品展示</h1>
      <nav>
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">产品</a></li>
          <li><a href="#">关于我们</a></li>
          <li><a href="#">联系我们</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <h2>热门产品</h2>
      <section>
        <article class="product" data-id="1" data-name="智能手机" data-price="2999">
          <h3>智能手机</h3>
          <p>6.5 英寸屏幕，128GB 存储，4800 万像素摄像头</p>
          <p>价格：2999 元</p>
        </article>
        <article class="product" data-id="2" data-name="笔记本电脑" data-price="5999">
          <h3>笔记本电脑</h3>
          <p>14 英寸屏幕，8GB 内存，512GB 固态硬盘</p>
          <p>价格：5999 元</p>
        </article>
        <article class="product" data-id="3" data-name="平板电脑" data-price="1999">
          <h3>平板电脑</h3>
          <p>10.5 英寸屏幕，64GB 存储，支持手写笔</p>
          <p>价格：1999 元</p>
        </article>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 产品展示. 保留所有权利.</p>
    </footer>
  </body>
</html>
```

**讲解：**

- 每个产品用 `article` 表达“独立可复用”的内容，后续加样式或交互都不影响结构；
- `data-id`、`data-name`、`data-price` 是自定义数据属性，JavaScript 课程会用它实现“点击查看详情”；
- 页面没有写任何 CSS，先保证结构正确，网格布局等美化留给 CSS 课程。
## 7. 最佳实践

### 7.1 语义化标签的使用

- **使用语义化标签**：优先使用语义化标签（如 `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`）来构建网页结构，而不是使用通用的 `<div>` 标签。
- **正确嵌套**：确保标签的嵌套顺序正确，例如 `<li>` 必须在 `<ul>` 或 `<ol>` 内部。
- **避免过度使用**：不要为了使用语义化标签而过度使用，应该根据内容的实际含义选择合适的标签。

### 7.2 全局属性的使用

- **id 的唯一性**：确保每个元素的 `id` 属性值在页面中是唯一的。
- **class 的复用**：使用 `class` 属性来为多个元素应用相同的样式，提高代码的可维护性。
- **避免行内样式**：尽量避免使用 `style` 属性直接在元素上定义样式，应该使用 CSS 文件或 `<style>` 标签。
- **合理使用 data-\* 属性**：使用 `data-*` 属性来存储与元素相关的自定义数据，而不是使用 `id` 或 `class` 来存储数据。

### 7.3 链接和图像的最佳实践

- **链接的可访问性**：为链接添加 `title` 属性，提供额外的上下文信息。
- **图像的 alt 属性**：为所有图像添加 `alt` 属性，描述图像的内容，这对 SEO 和无障碍访问都很重要。
- **图像的尺寸**：为图像指定 `width` 和 `height` 属性，这样浏览器可以在加载图像之前预留空间，避免页面布局跳动。
- **图像的延迟加载**：对于大型图像，使用 `loading="lazy"` 属性来延迟加载，提高页面加载速度。

### 7.4 代码风格

- **缩进**：使用一致的缩进（通常是 2 或 4 个空格）来提高代码的可读性。
- **大小写**：HTML 标签和属性通常使用小写。
- **引号**：属性值应该使用双引号包围。
- **注释**：为复杂的代码添加注释，提高代码的可维护性。

## 8. 进阶知识点

### 8.1 可折叠内容：details 与 summary

```html
<!-- 默认折叠 -->
<details>
  <summary>常见问题：如何重置密码？</summary>
  <p>请访问登录页面，点击“忘记密码”链接。</p>
</details>

<!-- 默认展开 -->
<details open>
  <summary>使用说明</summary>
  <p>这是默认展开的说明内容。</p>
</details>
```

**讲解：**

- `<details>` 提供原生折叠容器，`<summary>` 是始终可见的标题行；
- 添加 `open` 属性可让内容默认展开，移除后默认折叠；
- 无需 JavaScript 即可实现 FAQ、详情展开等交互，且天然支持键盘操作。

### 8.2 原生对话框：dialog

```html
<dialog id="myDialog">
  <form method="dialog">
    <p>请确认操作</p>
    <button>取消</button>
    <button value="confirm">确认</button>
  </form>
</dialog>

<script>
  const dialog = document.getElementById('myDialog');
  dialog.showModal(); // 以模态方式显示，自动聚焦并屏蔽背景交互
  dialog.close();     // 关闭对话框
</script>
```

**讲解：**

- `showModal()` 打开模态框，`show()` 打开非模态框，二者行为不同；
- `method="dialog"` 让表单提交直接关闭对话框，并通过 `returnValue` 带回按钮值；
- 模态框自带焦点管理，可搭配 `::backdrop` 伪元素定制遮罩样式。

### 8.3 轻量弹出层：popover

```html
<button popovertarget="my-popover">打开弹出层</button>

<div id="my-popover" popover>
  <p>这是一个弹出层内容</p>
  <button popovertarget="my-popover" popovertargetaction="hide">关闭</button>
</div>
```

**讲解：**

- `popover` 属性把元素声明为弹出层，默认隐藏，由触发按钮控制显隐；
- `popovertarget` 声明触发按钮，`popovertargetaction` 可选 `toggle`/`show`/`hide`；
- 弹出层自动置于顶层（top layer），无需手动管理 `z-index`。

## 9. 动手试试：写一个“我的个人简介”页面

> 目标：用今天学的标签，写一个“我的个人简介”页面。

要求：

1. 页面标题为“关于我”；
2. 有一个一级标题 `<h1>` 显示你的名字；
3. 用 `<p>` 写一段自我介绍；
4. 用 `<ul>` 列出你的 3 个爱好；
5. 用 `<ol>` 列出你今天的 3 件事；
6. 用 `<a>` 放一个你最喜欢的网站链接（`target="_blank"`）。

挑战（可选）：

- 用 `<figure>` + `<figcaption>` 放一张图片；
- 用 `<dl>` 列出 3 个你学会的 HTML 标签及其含义；
- 用 `<details>` + `<summary>` 做一个“展开看更多”区域。

## 10. 核心知识点

- 标题（`h1`-`h6`）、段落（`p`）、强调（`strong`/`em`）等文本标签构成内容语义；
- 无序列表 `ul`、有序列表 `ol`、定义列表 `dl` 各有适用场景，嵌套可表达层级；
- 链接 `a` 支持网页、锚点、`mailto`、`tel` 四种目标；图片必须提供 `alt`；
- `id`、`class`、`data-*` 等全局属性服务于样式、脚本与数据绑定；
- 语义化标签（`header`/`nav`/`main`/`article`/`section`/`aside`/`footer`）构建标准页面骨架。

## 11. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 页面出现多个 `h1` | 标题层级混乱，影响大纲与 SEO | 全页只保留一个 `h1`，其余从 `h2` 开始 |
| `target="_blank"` 缺少 `rel` | 新页面可通过 `window.opener` 操作原页面 | 添加 `rel="noopener noreferrer"` |
| 图片缺 `alt` 或尺寸 | 加载失败无替代信息，且布局抖动 | 内容图写描述性 `alt`，并给出 `width`/`height` |
| 用 `div` 模拟列表/标题 | 语义缺失，屏幕阅读器无法识别结构 | 改用 `ul`/`ol`/`dl` 与标题标签 |
| 行内样式泛滥 | 样式与结构耦合，难以维护 | 抽取到 CSS 类，按类名复用 |
| 表单控件缺少 `label` | 点击文字无法聚焦，无障碍性差 | 用 `<label for>` 或嵌套方式关联 |
| 滥用 `details`/`dialog` | 语义不匹配或兼容性考虑不足 | 先确认语义，再检查浏览器支持度后降级 |

## 12. 扩展学习

- 表单方向：深入 `html5/005-HTML5FormValidation` 学习输入类型与验证 API；
- 语义方向：阅读 `html5/003-SemanticTag` 掌握 `article` 与 `section` 的边界；
- 数据方向：结合 `html5/027-CustomDataAttribute` 实践 `data-*` 与 `dataset`；
- 无障碍方向：参考 `html5/004-Accessibility` 补齐 ARIA 与键盘导航；
- 媒体方向：在 `html5/014-AudioVideo` 中学习 `audio`/`video` 的完整 API。
