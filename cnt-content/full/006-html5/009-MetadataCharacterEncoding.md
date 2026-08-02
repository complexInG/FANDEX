---
order: 51
title: 元数据与字符编码
module: html5
category: HTML5
difficulty: beginner
description: 'meta、title、link、UTF-8'
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/文档类型声明
  - html5/离线存储与WebAPI
  - html5/文本语义
  - html5/列表
prerequisites:
  - html5/概述与核心特性
---
## 1. 元数据概述

元数据（Metadata）是"关于数据的数据"，在 HTML 中通过 `<head>` 内的元素描述文档的属性、行为和关系。

```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="页面描述" />
  <title>页面标题</title>
  <link rel="stylesheet" href="styles.css" />
</head>
```

### 1.1 元数据分类

| 类别     | 元素                | 作用                     |
| -------- | ------------------- | ------------------------ |
| 字符编码 | `<meta charset>`    | 声明文档编码             |
| 视口配置 | `<meta viewport>`   | 移动端适配               |
| SEO 相关 | `<meta name>`       | 描述、关键词、机器人指令 |
| 社交分享 | `<meta property>`   | Open Graph、Twitter Card |
| 安全策略 | `<meta http-equiv>` | CSP、CORS                |
| 资源关系 | `<link>`            | 样式表、图标、预加载     |

## 2. meta 元素详解

### 2.1 字符编码声明

```html
<meta charset="UTF-8" />
```

**关键规则**：编码声明必须在文档前 1024 字节内；必须在 `<title>` 之前声明，防止 XSS 攻击；推荐始终使用 UTF-8。

### 2.2 SEO 元数据

```html
<meta name="description" content="深入讲解 HTML5 元数据与字符编码" />
<meta name="robots" content="index, follow" />
<meta name="author" content="fanquanpp" />
```

### 2.3 Open Graph 与社交分享

```html
<meta property="og:title" content="页面标题" />
<meta property="og:description" content="页面描述" />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta name="twitter:card" content="summary_large_image" />
```

### 2.4 安全相关元数据

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
<meta name="referrer" content="strict-origin-when-cross-origin" />
```

## 3. UTF-8 字符编码

### 3.1 UTF-8 编码原理

UTF-8 是一种变长编码，使用 1-4 个字节表示 Unicode 码点：

| 码点范围           | 字节数 | 编码格式                              |
| ------------------ | ------ | ------------------------------------- |
| U+0000 ~ U+007F    | 1      | `0xxxxxxx`                            |
| U+0080 ~ U+07FF    | 2      | `110xxxxx 10xxxxxx`                   |
| U+0800 ~ U+FFFF    | 3      | `1110xxxx 10xxxxxx 10xxxxxx`          |
| U+10000 ~ U+10FFFF | 4      | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

中文字符"中"（U+4E2D）的 UTF-8 编码：

$$
\text{UTF-8} = \text{0xE4 0xB8 0xAD}
$$

### 3.2 编码声明优先级

BOM > HTTP Content-Type 头 > meta charset 声明

## 4. link 元素

```html
<link rel="stylesheet" href="styles.css" />
<link rel="icon" type="image/png" href="/favicon.png" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preload" href="font.woff2" as="font" crossorigin />
<link rel="canonical" href="https://example.com/page" />
```
## head 容器

**文档头部容器**
`<head>...[meta|title|link|style|script]...</head>`
```html
<!-- 文档头部基础结构 -->
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="页面描述" />
  <title>页面标题</title>
  <link rel="stylesheet" href="styles.css" />
</head>
```

| 类别     | 元素                | 作用                     |
| -------- | ------------------- | ------------------------ |
| 字符编码 | `<meta charset>`    | 声明文档编码             |
| 视口配置 | `<meta viewport>`   | 移动端适配               |
| SEO 相关 | `<meta name>`       | 描述、关键词、机器人指令 |
| 社交分享 | `<meta property>`   | Open Graph、Twitter Card |
| 安全策略 | `<meta http-equiv>` | CSP、CORS                |
| 资源关系 | `<link>`            | 样式表、图标、预加载     |

---

## meta 元素

**字符编码声明**
`<meta charset="<编码>" />`
```html
<!-- 必须在文档前 1024 字节内,title 之前 -->
<meta charset="UTF-8" />
```

**SEO 元数据**
`<meta name="<名称>" content="<内容>" />`
```html
<!-- 页面描述 -->
<meta name="description" content="深入讲解 HTML5 元数据与字符编码" />

<!-- 搜索引擎指令 -->
<meta name="robots" content="index, follow" />

<!-- 作者 -->
<meta name="author" content="fanquanpp" />

<!-- 关键词 -->
<meta name="keywords" content="HTML5,meta,字符编码" />
```

**Open Graph 社交分享**
`<meta property="og:<属性>" content="<值>" />`
```html
<!-- Facebook / 微博等社交平台分享 -->
<meta property="og:title" content="页面标题" />
<meta property="og:description" content="页面描述" />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta property="og:url" content="https://example.com/page" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="页面标题" />
```

**安全相关元数据**
`<meta http-equiv="<HTTP头>" content="<值>" />`
```html
<!-- 内容安全策略 -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />

<!-- Referrer 策略 -->
<meta name="referrer" content="strict-origin-when-cross-origin" />

<!-- X-UA-Compatible -->
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
```

---

## viewport 视口配置

**移动端视口**
`<meta name="viewport" content="<键>=<值>, <键>=<值>" />`
```html
<!-- 标准移动端配置 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<!-- 禁止用户缩放(不推荐,影响可访问性) -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

<!-- 适配刘海屏 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
```

| 属性            | 值                 | 说明             |
| --------------- | ------------------ | ---------------- |
| `width`         | device-width / 数值 | 布局视口宽度     |
| `height`        | device-height / 数值 | 布局视口高度     |
| `initial-scale` | 0.1 ~ 10.0         | 初始缩放比例     |
| `minimum-scale` | 0.1 ~ 10.0         | 最小缩放比例     |
| `maximum-scale` | 0.1 ~ 10.0         | 最大缩放比例     |
| `user-scalable` | yes / no           | 是否允许用户缩放 |
| `viewport-fit`  | auto / contain / cover | 适配刘海屏     |

---

## title 元素

**文档标题**
`<title>[标题文本]</title>`
```html
<!-- 浏览器标签页标题,SEO 重要字段 -->
<title>页面标题 - 网站名称</title>
```

---

## link 元素

**资源关系**
`<link rel="<关系>" [type="<MIME>"] [href="<URL>"] [media="<媒体查询>"] />`
```html
<!-- 样式表 -->
<link rel="stylesheet" href="styles.css" />

<!-- 网站图标 -->
<link rel="icon" type="image/png" href="/favicon.png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />

<!-- 预连接(加速第三方资源) -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="dns-prefetch" href="https://fonts.googleapis.com" />

<!-- 预加载关键资源 -->
<link rel="preload" href="font.woff2" as="font" crossorigin />
<link rel="preload" href="hero.jpg" as="image" />

<!-- 规范化 URL -->
<link rel="canonical" href="https://example.com/page" />

<!-- 替代语言版本 -->
<link rel="alternate" hreflang="en" href="https://example.com/en/page" />
<link rel="alternate" hreflang="zh-CN" href="https://example.com/zh/page" />

<!-- manifest(PWA) -->
<link rel="manifest" href="/manifest.json" />
```

| rel 值          | 作用              |
| --------------- | ----------------- |
| `stylesheet`    | 样式表            |
| `icon`          | 网站图标          |
| `preconnect`    | 预连接域名        |
| `dns-prefetch`  | DNS 预解析        |
| `preload`       | 预加载资源        |
| `prefetch`      | 预获取下一页资源  |
| `canonical`     | 规范化 URL        |
| `alternate`     | 替代版本          |
| `manifest`      | PWA manifest      |

---

## style 与 script

**内联样式**
`<style [type="text/css"] [media="<媒体查询>"]>[CSS]</style>`
```html
<style>
  body { font-family: Arial, sans-serif; }
</style>
```

**脚本引入**
`<script src="<URL>" [type="<类型>"] [defer] [async] [crossorigin]></script>`
```html
<!-- 外部脚本,defer 等文档解析完后执行 -->
<script src="app.js" defer></script>

<!-- 异步加载 -->
<script src="analytics.js" async></script>

<!-- 模块脚本 -->
<script type="module" src="app.mjs"></script>

<!-- 内联脚本 -->
<script>
  console.log('页面加载完成');
</script>
```

| 属性     | 作用                              |
| -------- | --------------------------------- |
| `defer`  | 延迟执行(按顺序,DOMContentLoaded 前) |
| `async`  | 异步执行(下载完即执行,不保证顺序)  |
| `type="module"` | ES 模块                  |
| `crossorigin`   | 跨域脚本                |

---

## base 元素

**基准 URL**
`<base href="<URL>" [target="<目标>"] />`
```html
<!-- 文档内所有相对 URL 的基准 -->
<base href="https://www.example.com/" target="_blank" />
```

---

## UTF-8 字符编码

**UTF-8 编码原理**

| 码点范围           | 字节数 | 编码格式                              |
| ------------------ | ------ | ------------------------------------- |
| U+0000 ~ U+007F    | 1      | `0xxxxxxx`                            |
| U+0080 ~ U+07FF    | 2      | `110xxxxx 10xxxxxx`                   |
| U+0800 ~ U+FFFF    | 3      | `1110xxxx 10xxxxxx 10xxxxxx`          |
| U+10000 ~ U+10FFFF | 4      | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

**编码声明优先级**
`BOM > HTTP Content-Type 头 > meta charset 声明`

**JavaScript 检测编码**
```javascript
// 获取文档字符编码
console.log(document.characterSet); // 'UTF-8'
console.log(document.inputEncoding);
```

## 延伸阅读
HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。
CSS 样式与布局，见 007-css 模块。
JavaScript DOM 操作，见 008-javascript 模块。
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
