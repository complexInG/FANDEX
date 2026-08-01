---
order: 52
title: 文本语义
module: html5
category: HTML5
difficulty: beginner
description: 'h1-h6、p、strong、em、mark、time、address'
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/离线存储与WebAPI
  - html5/元数据与字符编码
  - html5/列表
  - html5/链接与锚点
prerequisites:
  - html5/概述与核心特性
---

# 文本语义 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 标题元素 h1-h6

HTML 提供六级标题，`<h1>` 最高，`<h6>` 最低，用于构建文档大纲。

**核心规则**：每个页面建议只有一个 `<h1>`；不要跳级；标题用于语义结构，不用于控制字号。

```html
<h1>网站主标题</h1>
<h2>章节标题</h2>
<h3>小节标题</h3>
```

## 2. 段落与文本元素

### 2.1 强调元素

| 元素       | 语义       | 默认样式 | 使用场景       |
| ---------- | ---------- | -------- | -------------- |
| `<em>`     | 语气强调   | 斜体     | 语音阅读时加重 |
| `<strong>` | 重要性强调 | 粗体     | 标记重要内容   |
| `<mark>`   | 相关性标记 | 黄色高亮 | 搜索结果高亮   |
| `<b>`      | 吸引注意   | 粗体     | 关键词         |
| `<i>`      | 不同语态   | 斜体     | 术语、外文     |
| `<small>`  | 附属细则   | 小字     | 免责声明       |

```html
<p><em>不要</em>在走廊奔跑</p>
<p><strong>警告：</strong>高压危险</p>
<p>搜索"<mark>HTML5</mark>"的结果</p>
```

### 2.2 术语与引用

```html
<dfn>HTML</dfn>是超文本标记语言
<abbr title="HyperText Markup Language">HTML</abbr>
<blockquote cite="https://example.com"><p>引用文字</p></blockquote>
H<sub>2</sub>O E=mc<sup>2</sup>
<code>console.log()</code>
<kbd>Ctrl</kbd> + <kbd>C</kbd>
```

## 3. time 元素

```html
<time datetime="2026-06-14">2026年6月14日</time>
<time datetime="2026-06-14T10:30:00+08:00">上午10:30</time>
<time datetime="PT2H30M">2小时30分钟</time>
```

| 类型     | 格式                | 示例                |
| -------- | ------------------- | ------------------- |
| 日期     | YYYY-MM-DD          | 2026-06-14          |
| 日期时间 | YYYY-MM-DDTHH:MM:SS | 2026-06-14T10:30:00 |
| 持续时间 | PnYnMnDTnHnMnS      | PT2H30M             |

## 4. address 元素

```html
<address>
  <a href="mailto:contact@example.com">contact@example.com</a><br />
  北京市朝阳区某某路123号
</address>
```

**注意**：`<address>` 用于联系信息，不是物理地址的通用容器；默认斜体显示。

## 5. 其他语义文本元素

```html
<p>价格：<del datetime="2026-01-01">¥99</del> <ins>¥79</ins></p>
<p>用户 <bdi>إبراهيم</bdi> 发表了评论</p>
<p>第一行<br />第二行</p>
<p>超长单词<wbr />可以在<wbr />此处<wbr />断行</p>
```
## 标题元素

**六级标题**
`<h1>...</h1>` ~ `<h6>...</h6>`
```html
<!-- 标题用于语义结构,不用于控制字号 -->
<h1>网站主标题</h1>
<h2>章节标题</h2>
<h3>小节标题</h3>
<h4>更小的子节标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```

---

## 段落与换行

**段落**
`<p>[内容]</p>`
```html
<!-- 段落自动添加上下边距 -->
<p>这是一个段落。</p>
```

**换行**
`<br>` | `<wbr>`
```html
<!-- br 强制换行,wbr 建议换行点(长单词) -->
<p>第一行<br />第二行</p>
<p>超长单词<wbr />可以在<wbr />此处<wbr />断行</p>
```

---

## 强调元素

**文本强调标签**

| 元素       | 语义       | 默认样式 | 使用场景       |
| ---------- | ---------- | -------- | -------------- |
| `<em>`     | 语气强调   | 斜体     | 语音阅读时加重 |
| `<strong>` | 重要性强调 | 粗体     | 标记重要内容   |
| `<mark>`   | 相关性标记 | 黄色高亮 | 搜索结果高亮   |
| `<b>`      | 吸引注意   | 粗体     | 关键词、产品名 |
| `<i>`      | 不同语态   | 斜体     | 术语、外文     |
| `<small>`  | 附属细则   | 小字     | 免责声明       |

```html
<!-- 强调标签综合 -->
<p><em>不要</em>在走廊奔跑</p>
<p><strong>警告:</strong>高压危险</p>
<p>搜索"<mark>HTML5</mark>"的结果</p>
<p>这是 <b>关键词</b>,这是 <i>术语</i>。</p>
<p><small>本活动最终解释权归本公司所有</small></p>
```

---

## 术语与引用

**定义与缩写**
`<dfn>[术语]</dfn>` | `<abbr title="<全称>">[缩写]</abbr>`
```html
<dfn>HTML</dfn>是超文本标记语言
<abbr title="HyperText Markup Language">HTML</abbr>
```

**引用**
`<blockquote cite="<URL>">[内容]</blockquote>` | `<q cite="<URL>">[内容]</q>` | `<cite>[作品名]</cite>`
```html
<!-- 块级引用 -->
<blockquote cite="https://example.com">
  <p>引用文字</p>
</blockquote>

<!-- 行内引用 -->
<p>他说:<q>你好</q></p>

<!-- 作品标题 -->
参考:<cite>JavaScript高级程序设计</cite>
```

---

## 上下标与代码

**上下标**
`<sub>[下标]</sub>` | `<sup>[上标]</sup>`
```html
<!-- 数学公式与化学式 -->
H<sub>2</sub>O
E=mc<sup>2</sup>
```

**代码与键盘**
`<code>[代码]</code>` | `<pre>[预格式化]</pre>` | `<kbd>[按键]</kbd>` | `<samp>[输出]</samp>` | `<var>[变量]</var>`
```html
<!-- 行内代码 -->
<code>console.log()</code>

<!-- 代码块 -->
<pre><code>function hello() {
  console.log('Hello');
}</code></pre>

<!-- 键盘按键 -->
按 <kbd>Ctrl</kbd> + <kbd>C</kbd> 复制

<!-- 程序输出 -->
<samp>Compilation successful</samp>

<!-- 变量 -->
<var>x</var> = 10
```

---

## 修改记录

**删除与插入**
`<del [datetime="<日期>"]>[内容]</del>` | `<ins [datetime="<日期>"]>[内容]</ins>`
```html
<!-- 价格变更 -->
<p>价格:<del datetime="2026-01-01">¥99</del> <ins>¥79</ins></p>
```

---

## 隔离与方向

**双向隔离**
`<bdi>[文本]</bdi>` | `<bdo dir="ltr|rtl">[文本]</bdo>`
```html
<!-- bdi 隔离方向不明的文本(如用户名) -->
<p>用户 <bdi>إبراهيم</bdi> 发表了评论</p>

<!-- bdo 强制文本方向 -->
<bdo dir="rtl">这段文字从右到左显示</bdo>
```

---

## 时间元素

**time 元素**
`<time datetime="<ISO日期>" [pubdate]>[显示文本]</time>`
```html
<!-- 日期 -->
<time datetime="2026-06-14">2026年6月14日</time>

<!-- 日期时间(带时区) -->
<time datetime="2026-06-14T10:30:00+08:00">上午10:30</time>

<!-- 持续时间 -->
<time datetime="PT2H30M">2小时30分钟</time>

<!-- 发布日期 -->
<time datetime="2026-06-14" pubdate>发布于 2026-06-14</time>
```

| 类型     | 格式                | 示例                |
| -------- | ------------------- | ------------------- |
| 日期     | YYYY-MM-DD          | 2026-06-14          |
| 日期时间 | YYYY-MM-DDThh:mm:ss | 2026-06-14T10:30:00 |
| 带时区   | YYYY-MM-DDThh:mm:ssTZD | 2026-06-14T10:30:00+08:00 |
| 持续时间 | PnYnMnDTnHnMnS      | PT2H30M             |

---

## 联系信息

**address 元素**
`<address>...[a|br|文本]...</address>`
```html
<!-- 用于文档作者/文章作者的联系信息 -->
<address>
  <a href="mailto:contact@example.com">contact@example.com</a><br />
  北京市朝阳区某某路123号
</address>
```

---

## 高亮与注音

**ruby 注音**
`<ruby>[字]<rt>[拼音]</rt></ruby>`
```html
<!-- 中日韩文字注音 -->
<ruby>汉<rt>hàn</rt></ruby>字
<ruby>日本<rt>にほん</rt></ruby>
```

**rp 注音回退**
```html
<ruby>
  汉<rp>(</rp><rt>hàn</rt><rp>)</rp>
</ruby>
```

## 参考文献



WHATWG HTML Living Standard：https://html.spec.whatwg.org/
MDN HTML 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTML
W3C Markup Validation Service：https://validator.w3.org/
WebAIM 可访问性指南：https://webaim.org/

## 延伸阅读



HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。
CSS 样式与布局，见 007-css 模块。
JavaScript DOM 操作，见 008-javascript 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 HTML/CSS 课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 HTML 解析与 DOM 树

浏览器解析 HTML 时先 tokenize 再建树；解析器对错误标记有容错规则（错误恢复算法）。
DOM 是内存中的树结构：元素节点、文本节点、属性；document.querySelector 沿树查找。
渲染流程：HTML -> DOM，CSS -> CSSOM，合并为渲染树，布局与绘制；理解流程可定位性能瓶颈。
脚本与解析：defer 延后执行，async 异步执行，模块脚本默认 defer 语义。

### 13.2 表单校验与无障碍

原生校验：required、pattern、min/max、type 约束；novalidate 可关闭，交由 JS 自定义。
校验 UI：:invalid/:valid 伪类样式；aria-invalid 标记错误；错误信息用 aria-describedby 关联。
键盘可达：所有交互元素可 Tab 聚焦，焦点可见，弹层焦点管理（trap）。
屏幕阅读器测试：NVDA/VoiceOver 实际朗读验证语义。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| HTML5 概述与核心特性 | 001-HTML5OverviewCoreFeature | 本文的前置基础 |
| HTML5 基础标签与全局属性 | 002-HTML5BasicTagGlobalAttribute | 本文的前置基础 |
| 语义化标签 | 003-SemanticTag | 本文的并列主题 |
| 无障碍访问 | 004-Accessibility | 本文的并列主题 |
| HTML5 表单与验证 | 005-HTML5FormValidation | 本文的并列主题 |
| HTML5 多媒体与 Canvas 绘图 | 006-HTML5MultimediaCanvasDrawing | 本文的并列主题 |
| 文档类型声明 | 007-DocTypeDeclaration | 本文的并列主题 |
| HTML5 离线存储与 Web API | 008-HTML5OfflineStorageWebAPI | 本文的并列主题 |
| 元数据与字符编码 | 009-MetadataCharacterEncoding | 本文的并列主题 |
| 文本语义 | 010-TextSemantic | 本文自身 |
| 列表 | 011-List | 本文的并列主题 |
| 链接与锚点 | 012-LinkageAnchor | 本文的并列主题 |
| 图像与响应式图片 | 013-ImageResponsiveImage | 本文的并列主题 |
| 音频与视频 | 014-AudioVideo | 本文的并列主题 |
| SVG | 015-SVG | 本文的并列主题 |
| 嵌入式内容 | 016-EmbeddedContent | 本文的并列主题 |
| progress与meter | 017-ProgressMeter | 本文的并列主题 |
| Web Components 与 PWA 开发 | 018-WebComponentsPWADevelopment | 本文的并列主题 |
| 拖拽API | 019-DragAPI | 本文的并列主题 |
| 地理位置定位 | 020-Geolocation | 本文的并列主题 |
| Web-Workers | 021-WebWorkers | 本文的并列主题 |
| Service-Worker与PWA | 022-ServiceWorkerPWA | 本文的并列主题 |
| History-API | 023-HistoryAPI | 本文的并列主题 |
| WebSocket | 024-WebSocket | 本文的并列主题 |
| WebRTC | 025-WebRTC | 本文的并列主题 |
| 微数据与JSON-LD | 026-MicrodataJSONLD | 本文的并列主题 |
| 自定义数据属性 | 027-CustomDataAttribute | 本文的并列主题 |
| 跨文档通信 | 028-CrossDocumentCommunication | 本文的并列主题 |
| 视口配置与移动优先 | 029-ViewportConfigMobileFirst | 本文的并列主题 |
| HTML5 项目示例：交互式表单应用 | 030-HTML5ProjectExampleInteractiveFormApplication | 本文的综合应用 |
