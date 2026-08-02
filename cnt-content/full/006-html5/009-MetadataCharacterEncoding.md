---
order: 90
title: 元数据与字符编码
module: 'html5'
category: 前端技术
difficulty: beginner
description: meta、title、link、UTF-8
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/007-DocTypeDeclaration'
  - 'html5/008-HTML5OfflineStorageWebAPI'
  - 'html5/010-TextSemantic'
  - 'html5/011-List'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：`<head>` 是网页的“身份证和说明书”

`<body>` 里的内容是给用户看的，`<head>` 里的内容则是给浏览器、搜索引擎和社交平台看的“说明书”：字符编码告诉浏览器怎么读字，`title` 是网页的名字，`description` 是摘要，`link` 声明资源关系。

其中最关键的是字符编码。可以这样理解：文字在电脑里都是数字，编码就是“数字与文字的翻译规则”。网页用 UTF-8 翻译，浏览器却用 GBK 翻译，就会出现乱码——就像同一句英文，有人按法语发音读，读出来完全不像。

所以 `<meta charset="UTF-8">` 必须写在 `<head>` 最前面，先告诉浏览器“请按 UTF-8 翻译”，后面的文字才不会读错。

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

**讲解：**

- `<meta charset>` 声明编码，`viewport` 配置移动端，`description` 是搜索引擎摘要；
- `<title>` 显示在标签页与搜索结果中，是网页的“名字”；
- `<link rel="stylesheet">` 引入样式表，属于资源关系类元数据。

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

**讲解：** `charset` 声明必须放在 `<head>` 最前面，否则浏览器可能先用默认编码（如 Windows 的 GBK）解析，中文就会变成乱码。

### 2.2 SEO 元数据

```html
<meta name="description" content="深入讲解 HTML5 元数据与字符编码" />
<meta name="robots" content="index, follow" />
<meta name="author" content="fanquanpp" />
```

**讲解：**

- `description` 是搜索结果里显示的摘要，建议一句话说明页面内容；
- `robots` 告诉搜索引擎是否收录（`index`）与是否跟踪链接（`follow`）；
- 关键词 `keywords` 已被搜索引擎忽略，不应再依赖它做 SEO。

### 2.3 Open Graph 与社交分享

```html
<meta property="og:title" content="页面标题" />
<meta property="og:description" content="页面描述" />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta name="twitter:card" content="summary_large_image" />
```

**讲解：**

- `og:title`/`og:description`/`og:image` 决定链接分享到微信、Facebook 等平台时展示的卡片内容；
- `twitter:card` 控制 Twitter 的卡片样式，`summary_large_image` 表示大图卡片；
- 不配置时社交平台只能抓取页面标题，分享效果会大打折扣。

### 2.4 安全相关元数据

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />
<meta name="referrer" content="strict-origin-when-cross-origin" />
```

**讲解：**

- `Content-Security-Policy`（CSP）限制页面可加载的资源来源，是防 XSS 的重要防线；
- `referrer` 策略控制跳转时是否携带来源地址，`strict-origin-when-cross-origin` 是兼顾隐私与功能的默认推荐；
- 安全策略也可以由服务器响应头配置，`meta` 方式是静态页面的替代方案。

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
**讲解：**

- `stylesheet` 引入样式，`icon` 设置站点图标，`preconnect` 提前建立连接；
- `preload` 预加载关键资源（如字体），`canonical` 声明页面的规范地址，避免重复内容；
- 预加载要克制：只针对当前页立即需要的资源。

## 5. 进阶知识点

### 5.1 style 与 script

```html
<style>
  body {
    margin: 0;
  }
</style>
<script src="app.js" defer></script>
```

**讲解：**

- `<style>` 内联样式只建议用于单页小项目，多页项目应提取为外部 CSS；
- `<script src="..." defer>` 延迟执行脚本，避免阻塞解析；
- 两者都放在 `<head>` 时，注意顺序：样式先加载，脚本按需延迟。

### 5.2 base 元素

```html
<base href="https://example.com/docs/" target="_blank" />
```

**讲解：**

- `<base>` 设置页面内所有相对链接的基准地址，影响其后所有 `a`/`img` 等资源；
- 一个页面只能有一个 `<base>`，且必须放在其他带 URL 的元素之前；
- 误用会全局改变链接行为，工程中较少使用，了解即可。

## 6. 动手试试

### 入门版（必做）

1. 新建 `encoding.html`，写入中文内容并声明 `<meta charset="UTF-8">`，用浏览器打开确认显示正常；
2. 删除 `<meta charset>` 行，刷新页面，观察中文是否变成乱码；
3. 把 `charset` 改成 `GBK`（同时把文件另存为 GBK 编码），观察浏览器如何表现。

### 进阶版（选做）

1. 在页面里补全 `description`、`og:title`、`og:image`，分享到社交平台查看卡片效果；
2. 用浏览器开发者工具的网络面板查看响应头里的 `Content-Type: text/html; charset=utf-8`；
3. 尝试配置一个简单的 CSP（只允许同源脚本），观察外部脚本被拦截。

## 7. 核心知识点

> 一句话记住元数据：`charset` 放最前防乱码，`title` 命名页面，`description` 写摘要，`viewport` 管移动端，`link` 引资源。

- 元数据放在 `<head>` 中，是给浏览器、搜索引擎和社交平台看的说明；
- `<meta charset="UTF-8">` 必须位于文档前 1024 字节内，且先于 `<title>`；
- UTF-8 是 1-4 字节的变长编码，兼容 ASCII，是 Web 的默认编码；
- 编码优先级：BOM > HTTP 响应头 > meta 声明；
- `description`/`robots` 服务 SEO，Open Graph 服务社交分享，CSP 服务安全；
- `<link>` 负责样式、图标、预连接、预加载与规范地址。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| charset 声明靠后 | 浏览器先用默认编码解析导致乱码 | 放在 `<head>` 第一行 |
| 编辑器与声明不一致 | 文件是 UTF-8 却声明 GBK（或反之） | 统一编辑器保存编码为 UTF-8 |
| 依赖 `keywords` | 搜索引擎已忽略该标签 | 用 `description` 与真实内容做 SEO |
| CSP 过于严格 | 误伤第三方脚本、字体、图片 | 先用 `Content-Security-Policy-Report-Only` 试运行 |
| 滥用 `preload` | 预加载过多资源抢占带宽 | 只预加载首屏关键资源 |
| 多个 `<base>` | 只有第一个生效，链接基准混乱 | 全页只保留一个或不用 |

## 9. 扩展学习

- 字符集：`javascript/015-UnicodePropertyEscape` 了解 Unicode 属性转义；
- 性能：`html5/031-CriticalRenderingPathAndResourceLoading` 中资源加载策略；
- 安全：`javascript/044-ErrorBoundaryGlobalErrorCatch` 与 CSP 的配合；
- SEO：`css/043-HTMLSemanticSEO` 全面理解语义化与元数据的组合；
- 移动端：`html5/029-ViewportConfigMobileFirst` 深入 viewport 配置。
