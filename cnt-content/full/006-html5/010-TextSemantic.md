---
order: 100
title: 文本语义
module: 'html5'
category: 前端技术
difficulty: beginner
description: h1-h6、p、strong、em、mark、time、address
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/008-HTML5OfflineStorageWebAPI'
  - 'html5/009-MetadataCharacterEncoding'
  - 'html5/011-List'
  - 'html5/012-LinkageAnchor'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：文字也有“语气”和“重点”

写文章时，你会用加粗、斜体、下划线表达强调。网页里的文本标签就是这些“排版语气”的语义版：`<strong>` 表示“这句话很重要”，`<em>` 表示“读的时候语气加重”。

选择指南：

| 想表达 | 用哪个 | 例子 |
| --- | --- | --- |
| 内容重要（警告、关键结论） | `<strong>` | 请勿酒后驾车 |
| 语气强调（读的时候重读） | `<em>` | 我“现在”就要 |
| 高亮相关结果 | `<mark>` | 搜索结果中的关键词 |
| 次要说明 | `<small>` | 版权、免责声明 |

必背：`h1`-`h6`、`p`、`strong`、`em`、`br`；了解即可：`mark`、`small`、`del`、`ins`、`sub`、`sup`、`bdi`、`wbr` 等，用到再查。

## 1. 标题元素 h1-h6

HTML 提供六级标题，`<h1>` 最高，`<h6>` 最低，用于构建文档大纲。

**核心规则**：每个页面建议只有一个 `<h1>`；不要跳级；标题用于语义结构，不用于控制字号。

```html
<h1>网站主标题</h1>
<h2>章节标题</h2>
<h3>小节标题</h3>
```

**讲解：**

- `h1` 是页面主标题，每页只有一个；`h2`-`h6` 逐级表示章节层次；
- 标题按层级使用，不要跳级，也不要为了字号硬套标题；
- 字号样式交给 CSS，标题标签只表达“这是第几级标题”。

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

**讲解：**

- `<em>` 表示语气强调（默认斜体），`<strong>` 表示重要性强调（默认粗体）；
- `<mark>` 标记与当前语境相关的内容，常用于搜索结果高亮；
- `b`/`i` 只是视觉样式，语义弱，能用 `strong`/`em` 时优先用后者。

### 2.2 术语与引用

```html
<dfn>HTML</dfn>是超文本标记语言
<abbr title="HyperText Markup Language">HTML</abbr>
<blockquote cite="https://example.com"><p>引用文字</p></blockquote>
H<sub>2</sub>O E=mc<sup>2</sup>
<code>console.log()</code>
<kbd>Ctrl</kbd> + <kbd>C</kbd>
```

**讲解：**

- `<dfn>` 标记术语的首次定义，`<abbr>` 配合 `title` 给出全称；
- `<blockquote>` 表示长引用，`cite` 属性指向出处；
- `<sub>`/`<sup>` 分别表示下标与上标（化学式、数学表达式）；
- `<code>` 表示代码片段，`<kbd>` 表示键盘按键。

## 3. time 元素

```html
<time datetime="2026-06-14">2026年6月14日</time>
<time datetime="2026-06-14T10:30:00+08:00">上午10:30</time>
<time datetime="PT2H30M">2小时30分钟</time>
```

**讲解：**

- `datetime` 提供机器可读的 ISO 8601 值，可见文本可以是“上周五”等自然表达；
- 日期时间带时区（`+08:00`）适合标注跨时区事件；
- `PT2H30M` 表示持续时间，用于视频长度、倒计时等场景。

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

**讲解：** 页面级联系信息放在 `<body>` 直属的 `<address>` 中；文章作者信息放在 `article` 内。普通地址文本应使用 `<p>`，不要滥用 `address`。

## 5. 其他语义文本元素

```html
<p>价格：<del datetime="2026-01-01">¥99</del> <ins>¥79</ins></p>
<p>用户 <bdi>إبراهيم</bdi> 发表了评论</p>
<p>第一行<br />第二行</p>
<p>超长单词<wbr />可以在<wbr />此处<wbr />断行</p>
```

**讲解：**

- `<del>` 标记已删除内容，`<ins>` 标记新增内容，常用于价格调整、修订记录；
- `<bdi>` 隔离双向文本（如阿拉伯语用户名），避免破坏周围文字方向；
- `<br>` 是强制换行，`<wbr>` 是“可断行点”，用于长单词、URL 的优雅折行。

## 6. 动手试试

### 入门版（必做）

1. 写一篇 100 字左右的“自我介绍”，要求包含：一个 `h1`、两个 `h2`、三个段落；
2. 在其中一句话上用 `<strong>` 强调关键信息，用 `<em>` 表达语气；
3. 用 `<time>` 标注今天的日期，用 `<address>` 写你的联系邮箱。

### 进阶版（选做）

1. 用 `<del>`/`<ins>` 写一条“原价 99 元，现价 79 元”的价格信息；
2. 用 `<blockquote>` 引用一句你喜欢的名言并标注出处；
3. 用 `<abbr>` 给一个缩写词补充全称，鼠标悬停查看效果。

## 7. 核心知识点

> 一句话记住文本语义：标题建层级，`strong` 表重要，`em` 表语气，`mark` 做高亮；日期用 `time`，联系用 `address`，其它标签用到再查。

- `h1`-`h6` 构建文档大纲，每页一个 `h1`，不跳级；
- `strong`（重要）与 `em`（语气）有明确语义，优先于 `b`/`i`；
- `mark` 高亮相关结果，`small` 表示附属细则；
- `time` 用 `datetime` 提供机器可读时间，`address` 只放联系信息；
- `del`/`ins` 表达修订，`sub`/`sup` 表达上下标，`bdi`/`wbr` 属于“用到再查”。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 用标题控制字号 | 层级语义被破坏，大纲混乱 | 标题表达层级，字号交给 CSS |
| 多个 `h1` | 页面主标题不唯一 | 每页只保留一个 `h1` |
| 滥用 `strong` | 全文都是“重要”，读屏负担大 | 只强调真正重要的信息 |
| `address` 放普通地址 | 语义错误，影响读屏理解 | 联系信息才用 `address` |
| 手写日期字符串 | 机器无法解析 | 用 `<time datetime>` 包裹 |
| 用 `br` 模拟段落 | 破坏段落语义 | 换段用 `p`，只有强制换行才用 `br` |

## 9. 扩展学习

- 列表语义：`html5/011-List` 掌握 `ul`/`ol`/`dl` 的选择；
- 链接语义：`html5/012-LinkageAnchor` 中链接文案与无障碍；
- 无障碍：`html5/004-Accessibility` 中读屏如何消费文本语义；
- 排版细节：`css/051-TypographyAndGridSystem` 控制文本的视觉呈现。
