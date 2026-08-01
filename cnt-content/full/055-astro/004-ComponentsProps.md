---
order: 4
title: Astro 组件与 Props 插槽
module: astro
category: Astro
difficulty: beginner
description: 'Astro 组件体系：组件结构、Props 传参、Slot 插槽与作用域样式'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/003-PagesRouting
  - astro/006-IslandsClientComponents
prerequisites:
  - astro/002-QuickStartProject
---
## 1. 组件化思想

组件是把"结构 + 逻辑 + 样式"封装为可复用单元的方式。Astro 组件以 `.astro` 为扩展名，兼具三大特性：

第一，前端优先：模板语法接近原生 HTML，学习成本低；

第二，默认无 JS：组件在构建期渲染为纯 HTML，不向浏览器发送任何脚本；

第三，可组合：页面是组件，组件可以嵌套组件，布局是特殊的组件。

## 2. 组件文件结构

每个 `.astro` 组件由三部分组成：

```astro
---
// 第一部分：组件脚本（frontmatter）
// 在构建期于服务端执行，可以导入模块、读取数据
const greeting = '你好，Astro'
---

<!-- 第二部分：组件模板 -->
<p>{greeting}</p>

<style>
  /* 第三部分：组件样式，默认自动作用域隔离 */
  p { color: #2563eb; }
</style>
```

讲解：frontmatter 中的代码在构建期运行，不会打包进浏览器脚本；模板渲染 HTML 输出；`<style>` 中的样式默认自动加作用域（scoped），只影响本组件内的元素。三部分相互独立，职责清晰。

## 3. 组件引用组件

### 3.1 导入与使用

```astro
---
// src/pages/index.astro
import Card from '../components/Card.astro'
import Header from '../components/Header.astro'
---

<Header />
<Card title="文章一" />
<Card title="文章二" />
```

讲解：在 frontmatter 中用 `import` 导入组件，模板中即可像使用 HTML 标签一样使用。组件名建议使用 PascalCase，与原生 HTML 标签区分。一个页面可以组合任意多个组件。

### 3.2 内置组件

Astro 还提供三个无需导入的内置组件：`<Code />`（代码高亮）、`<Image />` 与 `<Picture />`（图片优化，见 007）、`<Debug />`（开发调试）。它们由框架提供，开箱即用。

## 4. Props：向组件传参

### 4.1 定义与接收 Props

```astro
---
// src/components/Card.astro
interface Props {
  title: string
  description?: string   // 可选属性
  tags?: string[]        // 数组类型
}

const { title, description = '暂无描述', tags = [] } = Astro.props
---

<article class="card">
  <h2>{title}</h2>
  <p>{description}</p>
  {tags.length > 0 && (
    <ul>
      {tags.map((tag) => <li>{tag}</li>)}
    </ul>
  )}
</article>
```

讲解：`interface Props` 声明组件接受的属性类型，与 TypeScript 一致，编辑器会提供完整补全与类型检查；`Astro.props` 接收传入的全部属性，可配合解构与默认值使用。可选属性用 `?` 标记。

### 4.2 使用组件并传参

```astro
---
import Card from '../components/Card.astro'
---

<Card title="Astro 入门" description="从零开始学习 Astro" tags={['框架', '教程']} />
<Card title="无描述的卡片" />
```

讲解：属性名为 `camelCase`，布尔属性（如 `<Card featured />`）传入 `true`。静态字符串直接书写，动态值用 `{}` 包裹表达式。类型不符时构建期即报错，是 Astro 组件的安全网。

## 5. Slot 插槽

### 5.1 默认插槽

Props 适合传结构化数据，但有时需要把一整块 HTML 内容交给组件去"占位摆放"，此时用插槽：

```astro
---
// src/components/Alert.astro
---

<div class="alert">
  <slot />  <!-- 使用方传入的内容渲染到这里 -->
</div>
```

```astro
---
// 使用方
import Alert from '../components/Alert.astro'
---

<Alert>
  <strong>提示：</strong>这是一条自定义的提示内容。
</Alert>
```

讲解：`<slot />` 是插槽出口，组件标签之间写入的内容会渲染到出口位置。这是布局组件（如 003 中的 BaseLayout）实现"内容注入"的底层机制。

### 5.2 具名插槽

一个组件需要多个占位时，用 `name` 区分：

```astro
---
// src/components/ArticleLayout.astro
interface Props { title: string }
const { title } = Astro.props
---

<article>
  <header><slot name="header" /></header>
  <h1>{title}</h1>
  <main><slot /></main>             <!-- 默认插槽 -->
  <footer><slot name="footer" /></footer>
</article>
```

```astro
---
// 使用方
import ArticleLayout from '../components/ArticleLayout.astro'
---

<ArticleLayout title="插槽示例">
  <span slot="header">发布于 2026-08-01</span>
  <p>这里是正文内容，进入默认插槽。</p>
  <p slot="footer">版权信息</p>
</ArticleLayout>
```

讲解：通过 `slot="名称"` 属性把内容定向到对应的具名插槽；未标注 `slot` 的内容进入默认插槽。布局、页面骨架类组件常用此模式组合头部、正文、侧栏等区域。

### 5.3 插槽回退内容

```astro
<slot>这是默认内容，调用方未传内容时显示</slot>
```

讲解：插槽内可以写回退内容：使用方提供了内容则显示提供的内容，否则显示回退内容。适合为可选区域提供合理默认值。

## 6. 模板中的常用语法

| 语法 | 作用 | 示例 |
| --- | --- | --- |
| `{变量}` | 输出表达式结果 | `{title}` |
| `{条件 && <p>…</p>}` | 条件渲染 | `{isLoggedIn && <p>已登录</p>}` |
| `{arr.map(...)}` | 列表渲染 | `{items.map(i => <li>{i}</li>)}` |
| `{三元表达式}` | 条件分支 | `{a ? '是' : '否'}` |

讲解：模板只支持"表达式"（计算出一个值），不支持完整的语句（如 `if`、`for`），因此用 `&&`、三元、`map` 组合实现条件与循环。这与 JSX 的规则一致，熟悉 React 的读者可以无缝迁移。

## 7. 局部样式 scoped

### 7.1 自动作用域

```astro
<style>
  /* 自动编译为带 hash 的类名，只影响本组件 */
  .card { border: 1px solid #ddd; }
  h2 { margin: 0; }
</style>
```

讲解：组件内 `<style>` 的规则会被自动加作用域（如 `.card` 变为 `.card:where(.astro-abc123)`），且不会向下穿透到子组件。即使多个组件都写 `.card`，也不会互相污染。

### 7.2 需要覆盖作用域的情况

```astro
<style>
  :global(.markdown-body) h2 { font-size: 1.4rem; }
</style>
```

讲解：`<style is:global>` 或 `:global()` 包裹的规则不做作用域处理，可用于覆盖子组件、或作用于 Markdown 渲染出的全局内容。它是打破"组件隔离"的显式出口，应谨慎使用，避免全局样式失控。

## 8. 组件实践建议

第一，单一职责：一个组件只做一件事，如 `Card` 只负责卡片展示；

第二，数据向下传递：页面持有数据，通过 Props 下发给展示型组件；

第三，样式随组件走：默认 scoped 样式优先，全局样式只放主题级内容（颜色变量、字体等）；

第四，命名清晰：组件文件名用 PascalCase，如 `Pagination.astro`、`SearchBox.astro`。

## 9. 参考资源

Astro 组件语法：https://docs.astro.build/zh-cn/basics/astro-components/

Props 与插槽参考：https://docs.astro.build/zh-cn/reference/astro-components/

Astro 内置组件：https://docs.astro.build/zh-cn/reference/builtin-components/
