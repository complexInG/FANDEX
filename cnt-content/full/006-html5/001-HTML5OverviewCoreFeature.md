---
order: 10
tags:
  - html5
difficulty: beginner
title: 'HTML5 概述与核心特性'
module: html5
category: 'HTML5 Basics'
description: 'HTML5 新特性、语义化标签与浏览器兼容性。'
author: Anonymous
related:
  - html5/基础标签与全局属性
  - html5/语义化标签
prerequisites: []
updated: '2026-08-01'
---
## 0. 零基础入门（从零开始）

### 0.3 学习路径

完成上面的第一步后，按以下顺序继续学习：

- 002-基础标签与全局属性：div、span、id、class 等最常用写法。
- 003-语义化标签：header、nav、main、article 的用途。
- 004-列表与链接：掌握页面导航的基本结构。
- 005-表单与验证：输入框、按钮与数据提交。


# HTML5 全局属性与文档结构 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## 1. HTML5 概述 (Overview)

HTML5 是超文本标记语言 (HyperText Markup Language) 的第五次重大修改，于 2014 年 10 月由 W3C 正式发布。它不仅是一种标记语言，更是一个完整的 Web 应用平台，为现代 Web 开发提供了强大的基础。

### 1.1 发展历程

| 时间 | 事件                                                             |
| ---- | ---------------------------------------------------------------- |
| 2004 | Web Hypertext Application Technology Working Group (WHATWG) 成立 |
| 2007 | W3C 重启 HTML 标准制定工作                                       |
| 2012 | HTML5 候选推荐标准发布                                           |
| 2014 | HTML5 正式推荐标准发布                                           |
| 2016 | HTML5.1 发布                                                     |
| 2017 | HTML5.2 发布                                                     |
| 2021 | HTML 规范移至 WHATWG，成为"活标准"                               |

### 1.2 核心特性 (Key Features)

| 特性                | 描述                                                      | 优势                                       |
| ------------------- | --------------------------------------------------------- | ------------------------------------------ |
| **语义化标签**      | 提供更具描述性的标签，如 `<header>`, `<nav>`, `<main>` 等 | 增强代码可读性，改善 SEO，提高无障碍性     |
| **多媒体支持**      | 原生 `<video>` 和 `<audio>` 标签                          | 无需插件，跨浏览器支持，简化媒体嵌入       |
| **图形绘制**        | `<canvas>` 2D/3D 绘制和 SVG 矢量图形                      | 高性能图形渲染，适合游戏和数据可视化       |
| **离线与存储**      | LocalStorage, SessionStorage, IndexedDB                   | 离线数据存储，提高应用性能，减少服务器负载 |
| **设备访问**        | 地理定位、摄像头、传感器、触摸事件                        | 支持移动设备功能，增强用户体验             |
| **新表单控件**      | `date`, `color`, `range`, `email` 等                      | 改善用户输入体验，内置验证功能             |
| **Web Workers**     | 后台线程处理                                              | 提高性能，避免 UI 阻塞                     |
| **WebSocket**       | 实时双向通信                                              | 低延迟，适合实时应用如聊天、游戏           |
| **Canvas API**      | 2D 图形绘制                                               | 适合游戏、图表、图像处理                   |
| **Geolocation API** | 地理位置服务                                              | 基于位置的应用，如地图、本地服务           |

## 2. 文档结构 (Document Structure)

### 2.1 基本结构

```html
<!DOCTYPE html>
<!-- HTML5 文档声明 -->
<html lang="zh-CN">
  <!-- 语言属性 -->
  <head>
    <meta charset="UTF-8" />
    <!-- 字符编码 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- 响应式设置 -->
    <meta name="description" content="HTML5 页面示例" />
    <!-- 页面描述 -->
    <meta name="keywords" content="HTML5, 语义化, 教程" />
    <!-- 关键词 -->
    <title>HTML5 页面</title>
    <!-- 页面标题 -->
    <link rel="stylesheet" href="styles.css" />
    <!-- 外部样式 -->
    <script src="script.js" defer></script>
    <!-- 外部脚本 -->
  </head>
  <body>
    <!-- 内容区域 -->
  </body>
</html>
```

### 2.2 语义化文档结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>语义化 HTML5 页面</title>
  </head>
  <body>
    <header>
      <!-- 页面头部：Logo、标题、导航 -->
      <h1>网站标题</h1>
      <nav>
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">关于我们</a></li>
          <li><a href="#">联系我们</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <!-- 主要内容区域 -->
      <section>
        <h2>新闻资讯</h2>
        <article>
          <h3>HTML5 新特性介绍</h3>
          <p>HTML5 带来了许多新特性，如语义化标签、多媒体支持等...</p>
        </article>
        <article>
          <h3>Web 开发趋势</h3>
          <p>现代 Web 开发正在向更高效、更安全的方向发展...</p>
        </article>
      </section>
      <aside>
        <!-- 侧边栏：相关链接、广告等 -->
        <h3>相关资源</h3>
        <ul>
          <li><a href="#">HTML5 教程</a></li>
          <li><a href="#">CSS3 指南</a></li>
          <li><a href="#">JavaScript 参考</a></li>
        </ul>
      </aside>
    </main>
    <footer>
      <!-- 页面底部：版权信息、联系方式等 -->
      <p>&copy; 2026 网站名称. 保留所有权利.</p>
    </footer>
  </body>
</html>
```

## 3. 语义化标签 (Semantic Tags)

### 3.1 核心语义化标签

| 标签           | 描述                 | 使用场景               |
| -------------- | -------------------- | ---------------------- |
| `<header>`     | 页面或区块的头部     | 网站标题、Logo、导航栏 |
| `<nav>`        | 导航链接区域         | 主导航、面包屑导航     |
| `<main>`       | 页面的主要内容       | 唯一的主要内容区域     |
| `<article>`    | 独立的文章内容       | 博客文章、新闻、评论   |
| `<section>`    | 文档中的区块         | 主题相关的内容组       |
| `<aside>`      | 侧边栏或附属信息     | 相关链接、广告、引用   |
| `<footer>`     | 页面或区块的底部     | 版权信息、联系方式     |
| `<figure>`     | 独立的媒体内容       | 图片、图表、代码块     |
| `<figcaption>` | 媒体内容的标题或说明 | 图片 caption、图表说明 |
| `<mark>`       | 突出显示的文本       | 搜索结果高亮、重点内容 |
| `<time>`       | 日期或时间           | 发布日期、事件时间     |
| `<address>`    | 联系信息             | 作者地址、公司联系信息 |

### 3.2 语义化标签使用示例

#### 3.2.1 文章页面结构

```html
 <article>
  <header>
  <h1>HTML5 语义化标签的最佳实践</h1>
  <p>发布于 <time datetime="2026-04-05">2026年4月5日</time> by <address>张三</address></p>
  </header>
  <section>
  <h2>什么是语义化标签</h2>
  <p>语义化标签是指能够清晰描述其内容含义的 HTML 标签...</p>
  </section>
  <section>
  <h2>为什么使用语义化标签</h2>
  <p>语义化标签可以提高代码可读性、改善 SEO、增强无障碍性...</p>
  </section>
  <figure>
  <img src="semantic-tags.png" alt="语义化标签示意图">
  <figcaption>HTML5 语义化标签结构示意图</figcaption>
  </figure>
  <footer>
  <p>本文由张三编写，版权所有 &copy; 2026</p>
  </footer>
 </article>
```

#### 3.2.2 导航菜单

```html
<nav>
  <ul>
    <li><a href="#">首页</a></li>
    <li>
      <a href="#">产品</a>
      <ul>
        <li><a href="#">产品1</a></li>
        <li><a href="#">产品2</a></li>
        <li><a href="#">产品3</a></li>
      </ul>
    </li>
    <li><a href="#">关于我们</a></li>
    <li><a href="#">联系我们</a></li>
  </ul>
</nav>
```

#### 3.2.3 侧边栏

```html
<aside>
  <h3>相关文章</h3>
  <ul>
    <li><a href="#">CSS3 新特性介绍</a></li>
    <li><a href="#">JavaScript 异步编程</a></li>
    <li><a href="#">响应式设计最佳实践</a></li>
  </ul>
  <h3>订阅我们</h3>
  <form>
    <input type="email" placeholder="输入您的邮箱" />
    <button type="submit">订阅</button>
  </form>
</aside>
```

## 4. 优势与最佳实践

### 4.1 优势

- **SEO 友好**: 搜索引擎能更好地理解页面结构，提高搜索排名
- **无障碍性 (Accessibility)**: 屏幕阅读器更容易解析，提高网站可访问性
- **开发效率**: 减少对 `div` 的滥用，代码结构更清晰
- **维护性**: 语义化代码更易于理解和维护
- **跨设备兼容性**: 更好地支持移动设备和不同屏幕尺寸

### 4.2 最佳实践

#### 4.2.1 语义化标签使用原则

1. **使用正确的标签**: 根据内容的实际含义选择合适的标签
2. **避免过度使用**: 不要为了语义化而滥用标签
3. **保持层次结构**: 合理嵌套标签，保持清晰的文档结构
4. **结合 ARIA 属性**: 对于复杂的 UI 组件，使用 ARIA 属性增强无障碍性
5. **考虑浏览器兼容性**: 对于旧浏览器，提供适当的降级方案

#### 4.2.2 文档结构最佳实践

1. **使用单一的 `<main>` 标签**: 每个页面应该只有一个主要内容区域
2. **合理使用 `<section>` 和 `<article>`**: `<article>` 用于独立的内容，`<section>` 用于主题相关的内容组
3. **使用 `<header>` 和 `<footer>`**: 为页面和区块提供清晰的头部和底部
4. **导航使用 `<nav>`**: 明确标识导航链接区域
5. **侧边栏使用 `<aside>`**: 区分主要内容和附属信息

#### 4.2.3 代码风格

1. **缩进一致**: 使用 2 或 4 个空格进行缩进
2. **标签小写**: HTML5 标签建议使用小写
3. **引号使用**: 属性值使用双引号
4. **自闭合标签**: 对于没有内容的标签，使用自闭合形式
5. **注释清晰**: 添加适当的注释，提高代码可读性

## 5. 常见问题与解决方案

### 5.1 浏览器兼容性

**问题**: 旧浏览器不支持 HTML5 语义化标签
**解决方案**:

1. 使用 HTML5 Shiv: 为旧 IE 浏览器添加语义化标签支持
2. 添加 CSS 样式: 为语义化标签添加 `display: block` 样式
3. 使用 polyfill: 为不支持的特性提供替代实现

```html
<!-- HTML5 Shiv 用于 IE8 及以下版本 -->
<!--[if lt IE 9]>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js"></script>
<![endif]-->
<style>
  /* 为语义化标签添加块级显示 */
  header,
  nav,
  main,
  article,
  section,
  aside,
  footer,
  figure,
  figcaption {
    display: block;
  }
</style>
```

### 5.2 语义化过度

**问题**: 为了语义化而滥用标签，导致代码结构混乱
**解决方案**:

1. 遵循 HTML 规范，只在合适的场景使用语义化标签
2. 对于简单的布局，使用 `div` 是合理的
3. 保持代码简洁，避免不必要的嵌套

### 5.3 无障碍性问题

**问题**: 语义化标签使用不当，影响屏幕阅读器的解析
**解决方案**:

1. 使用 `alt` 属性为图片提供替代文本
2. 使用 `aria-label` 和 `aria-labelledby` 为元素提供额外的描述
3. 确保表单元素有正确的标签关联
4. 测试屏幕阅读器的解析效果

## 6. 实际应用示例

### 6.1 博客页面结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>我的博客</title>
    <style>
      /* 简单的样式 */
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
      }
      header,
      nav,
      main,
      article,
      section,
      aside,
      footer {
        display: block;
      }
      header {
        background: #333;
        color: white;
        padding: 1rem;
      }
      nav ul {
        list-style: none;
        padding: 0;
      }
      nav ul li {
        display: inline;
        margin-right: 1rem;
      }
      nav ul li a {
        color: white;
        text-decoration: none;
      }
      main {
        display: flex;
        padding: 1rem;
      }
      section {
        flex: 3;
        margin-right: 1rem;
      }
      aside {
        flex: 1;
        background: #f4f4f4;
        padding: 1rem;
      }
      article {
        background: #f9f9f9;
        padding: 1rem;
        margin-bottom: 1rem;
      }
      footer {
        background: #333;
        color: white;
        text-align: center;
        padding: 1rem;
        margin-top: 1rem;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>我的博客</h1>
      <nav>
        <ul>
          <li><a href="#">首页</a></li>
          <li><a href="#">文章</a></li>
          <li><a href="#">关于我</a></li>
          <li><a href="#">联系我</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <section>
        <article>
          <header>
            <h2>HTML5 语义化标签的使用</h2>
            <p>发布于 <time datetime="2026-04-05">2026年4月5日</time></p>
          </header>
          <p>
            HTML5 引入了许多语义化标签，如 header、nav、main、article
            等。这些标签使得网页结构更加清晰，有利于搜索引擎优化和无障碍访问。
          </p>
          <figure>
            <img src="semantic-structure.png" alt="HTML5 语义化结构" />
            <figcaption>HTML5 语义化结构示意图</figcaption>
          </figure>
          <p>
            使用语义化标签时，需要注意合理嵌套，保持清晰的层次结构。同时，要考虑浏览器兼容性，为旧浏览器提供适当的降级方案。
          </p>
        </article>
        <article>
          <header>
            <h2>CSS3 新特性介绍</h2>
            <p>发布于 <time datetime="2026-04-01">2026年4月1日</time></p>
          </header>
          <p>
            CSS3
            带来了许多新特性，如圆角、阴影、渐变、动画等。这些特性使得网页设计更加丰富多样，同时减少了对图片的依赖。
          </p>
          <p>
            在使用 CSS3
            特性时，需要注意浏览器兼容性，为不同的浏览器添加适当的前缀，或者使用工具自动处理前缀问题。
          </p>
        </article>
      </section>
      <aside>
        <h3>关于博主</h3>
        <p>我是一名 Web 开发工程师，专注于前端技术的学习和分享。</p>
        <h3>热门文章</h3>
        <ul>
          <li><a href="#">JavaScript 异步编程</a></li>
          <li><a href="#">响应式设计最佳实践</a></li>
          <li><a href="#">Web 性能优化技巧</a></li>
        </ul>
        <h3>订阅我们</h3>
        <form>
          <input type="email" placeholder="输入您的邮箱" />
          <button type="submit">订阅</button>
        </form>
      </aside>
    </main>
    <footer>
      <p>&copy; 2026 我的博客. 保留所有权利.</p>
    </footer>
  </body>
</html>
```

### 6.2 产品展示页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>产品展示</title>
    <style>
      /* 简单的样式 */
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
      }
      header {
        background: #f8f8f8;
        padding: 1rem;
        border-bottom: 1px solid #ddd;
      }
      nav ul {
        list-style: none;
        padding: 0;
      }
      nav ul li {
        display: inline;
        margin-right: 1rem;
      }
      nav ul li a {
        text-decoration: none;
        color: #333;
      }
      main {
        padding: 2rem;
      }
      section {
        margin-bottom: 2rem;
      }
      .product-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1rem;
      }
      article {
        border: 1px solid #ddd;
        padding: 1rem;
        border-radius: 4px;
      }
      article img {
        max-width: 100%;
        height: auto;
      }
      footer {
        background: #333;
        color: white;
        text-align: center;
        padding: 1rem;
        margin-top: 2rem;
      }
    </style>
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
      <section>
        <h2>热门产品</h2>
        <div class="product-grid">
          <article>
            <img src="product1.jpg" alt="产品1" />
            <h3>产品1</h3>
            <p>这是一款高性能的产品，具有多种功能和优势。</p>
            <p><strong>价格: ¥199</strong></p>
            <button>加入购物车</button>
          </article>
          <article>
            <img src="product2.jpg" alt="产品2" />
            <h3>产品2</h3>
            <p>这是一款设计精美的产品，适合各种场景使用。</p>
            <p><strong>价格: ¥299</strong></p>
            <button>加入购物车</button>
          </article>
          <article>
            <img src="product3.jpg" alt="产品3" />
            <h3>产品3</h3>
            <p>这是一款性价比高的产品，受到广大用户的喜爱。</p>
            <p><strong>价格: ¥149</strong></p>
            <button>加入购物车</button>
          </article>
        </div>
      </section>
      <section>
        <h2>新品上市</h2>
        <div class="product-grid">
          <article>
            <img src="product4.jpg" alt="产品4" />
            <h3>产品4</h3>
            <p>这是我们最新推出的产品，具有创新的设计和功能。</p>
            <p><strong>价格: ¥399</strong></p>
            <button>加入购物车</button>
          </article>
          <article>
            <img src="product5.jpg" alt="产品5" />
            <h3>产品5</h3>
            <p>这是一款专为专业用户设计的产品，性能卓越。</p>
            <p><strong>价格: ¥499</strong></p>
            <button>加入购物车</button>
          </article>
        </div>
      </section>
    </main>
    <footer>
      <p>&copy; 2026 产品展示. 保留所有权利.</p>
    </footer>
  </body>
</html>
```

## 7. 总结

HTML5 是现代 Web 开发的基础，它的语义化标签和新特性为 Web 应用提供了强大的支持。通过使用语义化标签，我们可以创建结构清晰、易于理解和维护的网页，同时提高 SEO 和无障碍性。
在实际开发中，我们应该遵循 HTML5 的最佳实践，合理使用语义化标签，保持代码的清晰和简洁。同时，要考虑浏览器兼容性，为不同的浏览器提供适当的降级方案。
随着 Web 技术的不断发展，HTML5 也在不断演进，我们需要持续学习和关注最新的标准和实践，以创建更好的 Web 应用。

---

## 延伸阅读

- [CSS](css/overview-and-syntax)
- [JavaScript](javascript/overview)
## HTML5 文档基本结构

**最小 HTML5 文档**
`<!DOCTYPE html> <html lang="..."> <head>...</head> <body>...</body> </html>`

```html
<!DOCTYPE html>
<!-- HTML5 文档类型声明 -->
<html lang="zh-CN">
  <!-- lang 属性指定文档语言 -->
  <head>
    <meta charset="UTF-8" />
    <!-- 字符编码声明 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- 移动端视口配置 -->
    <title>页面标题</title>
    <!-- 文档标题(必填) -->
  </head>
  <body>
    <!-- 页面内容 -->
  </body>
</html>
```

**head 头部元数据元素**

| 元素                    | 作用                           | 示例                                                |
| ----------------------- | ------------------------------ | --------------------------------------------------- |
| `<title>`               | 文档标题(必填)               | `<title>页面标题</title>`                           |
| `<meta charset>`        | 字符编码                       | `<meta charset="UTF-8" />`                          |
| `<meta name="viewport">`| 移动端视口                     | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| `<meta name="description">` | 页面描述(SEO)            | `<meta name="description" content="页面描述">`      |
| `<meta name="keywords">`    | 关键词(SEO,已废弃)       | `<meta name="keywords" content="HTML5, CSS3">`      |
| `<meta name="author">`      | 作者                       | `<meta name="author" content="张三">`               |
| `<meta http-equiv="refresh">` | 自动刷新                  | `<meta http-equiv="refresh" content="30">`          |
| `<link rel="stylesheet">`   | 外部样式表                 | `<link rel="stylesheet" href="style.css">`          |
| `<link rel="icon">`         | 网站图标                   | `<link rel="icon" href="favicon.ico">`              |
| `<link rel="canonical">`    | 规范链接(SEO)            | `<link rel="canonical" href="https://...">`         |
| `<link rel="preconnect">`   | 预连接                    | `<link rel="preconnect" href="https://cdn.example.com">` |
| `<link rel="preload">`      | 预加载                    | `<link rel="preload" href="font.woff2" as="font">`  |
| `<script>`                  | 脚本                      | `<script src="app.js" defer></script>`              |
| `<style>`                   | 内联样式                  | `<style>body{margin:0}</style>`                     |
| `<base>`                    | 基准 URL                  | `<base href="https://example.com/" target="_blank">`|

---

## 语义化文档结构

**完整文档骨架**

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>语义化页面结构</title>
  </head>
  <body>
    <header><!-- 页面头部 --></header>
    <nav><!-- 导航 --></nav>
    <main>
      <article><!-- 独立内容 --></article>
      <section><!-- 区块 --></section>
      <aside><!-- 侧边栏 --></aside>
    </main>
    <footer><!-- 页脚 --></footer>
  </body>
</html>
```

**语义化结构元素表**

| 元素          | 作用                  | 使用场景                  |
| ------------- | --------------------- | ------------------------- |
| `<header>`    | 页面或区块的头部      | 网站标题、Logo、导航栏    |
| `<nav>`       | 导航链接区域          | 主导航、面包屑导航        |
| `<main>`      | 主要内容(每页唯一)   | 唯一的主要内容区域        |
| `<article>`   | 独立完整的内容        | 文章、新闻、评论、产品卡  |
| `<section>`   | 主题相关的内容区块    | 章节、章节分组            |
| `<aside>`     | 侧边栏或附属信息      | 相关链接、广告、引用      |
| `<footer>`    | 页面或区块的底部      | 版权信息、联系方式        |
| `<figure>`    | 独立的媒体内容        | 图片、图表、代码块        |
| `<figcaption>`| figure 的标题         | 图片说明、图表标题        |
| `<details>`   | 可折叠的详细信息      | FAQ、技术详情             |
| `<summary>`   | details 的标题        | 折叠区域的标题            |
| `<dialog>`    | 对话框/模态框         | 模态对话框                |
| `<search>`    | 搜索区域(HTML Living Standard) | 站点搜索表单    |

---

## HTML5 全局属性

**核心全局属性表**

| 属性            | 作用                          | 示例                              |
| --------------- | ----------------------------- | --------------------------------- |
| `id`            | 元素唯一标识                  | `<div id="header">`               |
| `class`         | 类名(可多个,空格分隔)      | `<div class="box active">`        |
| `style`         | 内联样式                      | `<div style="color:red">`         |
| `title`         | 鼠标悬停提示                  | `<a title="点击查看详情">`        |
| `lang`          | 元素内容语言                  | `<p lang="en">Hello</p>`          |
| `dir`           | 文本方向                      | `<p dir="rtl">...</p>` (ltr/rtl/auto) |
| `tabindex`      | Tab 键焦点顺序                | `<div tabindex="0">`              |
| `accesskey`     | 快捷键                        | `<button accesskey="s">`          |
| `hidden`        | 隐藏元素                     | `<div hidden>...</div>`           |
| `draggable`     | 是否可拖拽                    | `<div draggable="true">`          |
| `spellcheck`    | 拼写检查                      | `<input spellcheck="true">`       |
| `translate`     | 是否翻译                     | `<p translate="no">Brand</p>`     |
| `contenteditable`| 内容可编辑                  | `<div contenteditable="true">`    |
| `contextmenu`   | 上下文菜单(已废弃)         | -                                 |
| `tabindex`      | 焦点顺序                     | `<div tabindex="0">`              |

**data-* 自定义数据属性**
`data-<name>="<value>"`

```html
<!-- 存储自定义数据(详见"自定义数据属性"章节) -->
<div data-user-id="123" data-role="admin">用户信息</div>
```

---

## ARIA 无障碍属性

**常用 ARIA 属性(详见"无障碍访问"章节)**

```html
<!-- 主要 ARIA 属性 -->
<div
  role="button"
  aria-label="关闭"
  aria-hidden="false"
  aria-disabled="false"
  aria-expanded="true"
  aria-controls="menu"
  aria-live="polite"
  aria-current="page"
>
  ...
</div>
```

---

## 事件处理属性

**HTML 事件属性表**

| 事件属性          | 触发时机              | 应用元素              |
| ----------------- | --------------------- | --------------------- |
| `onclick`         | 点击                  | 几乎所有元素          |
| `ondblclick`      | 双击                  | 几乎所有元素          |
| `onmousedown`     | 鼠标按下              | 几乎所有元素          |
| `onmouseup`       | 鼠标释放              | 几乎所有元素          |
| `onmouseover`     | 鼠标移入              | 几乎所有元素          |
| `onmouseout`      | 鼠标移出              | 几乎所有元素          |
| `onmousemove`     | 鼠标移动              | 几乎所有元素          |
| `onkeydown`       | 键盘按下              | 表单元素、可聚焦元素  |
| `onkeyup`         | 键盘释放              | 表单元素、可聚焦元素  |
| `onkeypress`      | 键盘按住(已废弃)    | 表单元素、可聚焦元素  |
| `onfocus`         | 获得焦点              | 表单元素、可聚焦元素  |
| `onblur`          | 失去焦点              | 表单元素、可聚焦元素  |
| `onchange`        | 值改变并失焦          | input、select、textarea |
| `oninput`         | 值改变(实时)        | input、textarea       |
| `onsubmit`        | 表单提交              | `<form>`              |
| `onreset`         | 表单重置              | `<form>`              |
| `onload`          | 加载完成              | `<body>`、`<img>`、`<iframe>` |
| `onunload`        | 卸载(已废弃)        | `<body>`              |
| `onresize`        | 窗口大小改变          | `<body>`              |
| `onscroll`        | 滚动                  | 可滚动元素            |
| `oncontextmenu`   | 右键菜单              | 几乎所有元素          |
| `ondrag`          | 拖拽中                | 可拖拽元素            |
| `ondrop`          | 放置                  | 放置目标              |
| `oncopy`          | 复制                  | 可选中文本元素        |
| `onpaste`         | 粘贴                  | 表单元素              |

---

## 字符编码与 viewport

**字符编码声明**
`<meta charset="<encoding>">`

```html
<!-- UTF-8 是 HTML5 推荐编码,必须放在 <head> 的最前面 -->
<meta charset="UTF-8" />

<!-- 其他常用编码 -->
<meta charset="UTF-16" />
<meta charset="ISO-8859-1" />
```

**viewport 视口配置(移动端必填)**
`<meta name="viewport" content="<key>=<value>, <key>=<value>, ...">`

```html
<!-- 标准移动端视口配置 -->
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=5.0, user-scalable=yes"
/>
```

**viewport 属性表**

| 属性                | 作用                          | 示例值              |
| ------------------- | ----------------------------- | ------------------- |
| `width`             | 视口宽度                      | `device-width` 或数字 |
| `height`            | 视口高度                      | `device-height` 或数字 |
| `initial-scale`     | 初始缩放比例                  | `1.0`               |
| `minimum-scale`     | 最小缩放比例                  | `1.0`               |
| `maximum-scale`     | 最大缩放比例                  | `5.0`               |
| `user-scalable`     | 是否允许用户缩放              | `yes` 或 `no`       |
| `viewport-fit`      | 视口形状(刘海屏适配)        | `auto` / `contain` / `cover` |

---

## 资源预加载

**link rel 预加载类型**
`<link rel="<type>" href="<url>" as="<resource-type>">`

```html
<!-- 预连接(提前建立连接) -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin />

<!-- DNS 预解析 -->
<link rel="dns-prefetch" href="//cdn.example.com" />

<!-- 预加载关键资源 -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="critical.css" as="style" />
<link rel="preload" href="hero.jpg" as="image" />

<!-- 预获取(空闲时获取) -->
<link rel="prefetch" href="next-page.html" />

<!-- 预渲染(已废弃,改用 prefetch) -->
<link rel="prerender" href="next-page.html" />
```

**as 属性值表**

| 值              | 资源类型         |
| --------------- | ---------------- |
| `audio`         | 音频文件         |
| `document`      | HTML 文档        |
| `embed`         | 嵌入资源         |
| `fetch`         | fetch/XHR 请求   |
| `font`          | 字体文件         |
| `image`         | 图片             |
| `object`        | 插件资源         |
| `script`        | JavaScript       |
| `style`         | CSS 样式表       |
| `track`         | WebVTT 文件      |
| `video`         | 视频文件         |
| `worker`        | Web Worker       |

---

## script 标签属性

**script 加载策略**
`<script src="..." defer | async></script>`

```html
<!-- 普通加载:阻塞 HTML 解析,立即下载执行 -->
<script src="script.js"></script>

<!-- async:异步下载,下载完立即执行(不保证顺序) -->
<script src="analytics.js" async></script>

<!-- defer:异步下载,HTML 解析完成后按顺序执行 -->
<script src="app.js" defer></script>

<!-- 内联模块(默认 defer) -->
<script type="module">
  import { greet } from './utils.js';
  greet();
</script>

<!-- 指定 MIME 类型 -->
<script type="text/javascript" src="script.js"></script>
<script type="module" src="app.js"></script>
<script type="application/json">{"key":"value"}</script>
```

**async vs defer 对比**

| 属性     | 下载     | 执行时机                  | 执行顺序      | 适用场景            |
| -------- | -------- | ------------------------- | ------------- | ------------------- |
| 无       | 阻塞     | 下载完立即执行            | 源顺序        | 关键脚本            |
| `async`  | 不阻塞   | 下载完立即执行            | 不保证顺序    | 独立第三方脚本      |
| `defer`  | 不阻塞   | HTML 解析完成后执行       | 源顺序        | 依赖 DOM 的脚本     |

---

## HTML5 新增特性元素

**HTML Living Standard 2025 新增**

```html
<!-- <dialog> 原生对话框元素 -->
<dialog id="modal">
  <form method="dialog">
    <p>确认操作?</p>
    <button>取消</button>
    <button value="confirm">确认</button>
  </form>
</dialog>

<!-- popover 属性(原生弹出层) -->
<button popovertarget="mypopover">打开弹出</button>
<div id="mypopover" popover>
  <p>这是一个弹出层</p>
</div>

<!-- <search> 搜索区域 -->
<search>
  <form action="/search">
    <input type="search" name="q" />
    <button>搜索</button>
  </form>
</search>

<!-- <details> 可折叠区域 -->
<details>
  <summary>更多详情</summary>
  <p>这里是详细内容</p>
</details>

<!-- loading="lazy" 懒加载 -->
<img src="image.jpg" loading="lazy" alt="..." />

<!-- <template> 内容模板 -->
<template id="card-template">
  <div class="card">
    <h3></h3>
    <p></p>
  </div>
</template>
```

---

## 注意事项

- **DOCTYPE 必填**:HTML5 文档必须以 `<!DOCTYPE html>` 开头(不区分大小写)
- **charset 位置**:`<meta charset>` 必须放在 `<head>` 的最前面,前 1024 字节内
- **viewport 必填**:移动端页面必须配置 viewport,否则会以桌面宽度渲染
- **lang 属性**:应为 `<html>` 指定 `lang` 属性,有助于 SEO 和无障碍访问
- **title 必填**:每个页面必须有唯一的 `<title>`,长度建议 30-60 字符
- **语义化优先**:使用语义化标签(header、nav、main)替代无意义 div
- **script 位置**:推荐 `<script defer>` 放在 `<head>` 中,而非 `<body>` 末尾
- **preconnect 跨域**:跨域资源预加载需添加 `crossorigin` 属性

## 参考文献



WHATWG HTML Living Standard：https://html.spec.whatwg.org/
MDN HTML 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTML
W3C Markup Validation Service：https://validator.w3.org/
WebAIM 可访问性指南：https://webaim.org/

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| HTML5 概述与核心特性 | 001-HTML5OverviewCoreFeature | 本文自身 |
| HTML5 基础标签与全局属性 | 002-HTML5BasicTagGlobalAttribute | 本文的前置基础 |
| 语义化标签 | 003-SemanticTag | 本文的并列主题 |
| 无障碍访问 | 004-Accessibility | 本文的并列主题 |
| HTML5 表单与验证 | 005-HTML5FormValidation | 本文的并列主题 |
| HTML5 多媒体与 Canvas 绘图 | 006-HTML5MultimediaCanvasDrawing | 本文的并列主题 |
| 文档类型声明 | 007-DocTypeDeclaration | 本文的并列主题 |
| HTML5 离线存储与 Web API | 008-HTML5OfflineStorageWebAPI | 本文的并列主题 |
| 元数据与字符编码 | 009-MetadataCharacterEncoding | 本文的并列主题 |
| 文本语义 | 010-TextSemantic | 本文的并列主题 |
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
