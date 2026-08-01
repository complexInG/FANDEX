---
order: 7
title: Astro 样式与资源优化
module: astro
category: Astro
difficulty: intermediate
description: 'Astro 样式体系：scoped CSS、全局样式、Fonts API、Image 组件与 SVG 优化'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/002-QuickStartProject
  - astro/009-Astro7Features
prerequisites:
  - astro/002-QuickStartProject
---
## 1. Astro 的样式方案

Astro 对 CSS 的处理理念与组件一致：默认隔离、按需输出、构建期优化。主要方案对比：

| 方案 | 写法 | 作用域 | 适用场景 |
| --- | --- | --- | --- |
| `<style>` | 组件内标签 | 自动 scoped | 组件局部样式（首选） |
| 全局样式 | `import './global.css'` | 全局 | 主题变量、Reset、字体 |
| CSS Modules | `*.module.css` | scoped | 框架组件（React/Vue）中使用 |
| Tailwind | `@tailwindcss/vite` 集成 | 按类名 | 工具类优先的项目 |
| `<style is:global>` | 显式声明 | 全局 | 覆盖第三方内容样式 |

讲解：默认推荐"组件 scoped + 少量全局主题样式"的组合。Tailwind 等集成通过 `npx astro add tailwind` 安装，Astro 7 内置 Tailwind 4 支持。

## 2. scoped 与全局样式

### 2.1 组件 scoped 样式

```astro
---
// src/components/Card.astro
---

<div class="card">
  <h2 class="title">卡片标题</h2>
</div>

<style>
  .card {
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1rem;
  }
  .title {
    margin: 0 0 0.5rem;
    font-size: 1.25rem;
  }
</style>
```

讲解：构建时 Astro 为每个 class 追加哈希（如 `.card:where(.astro-xyz123)`），保证样式只作用于本组件。即使另一个组件写了相同的 `.card` 也不会冲突，删除组件时样式随之消失，无样式泄漏。

### 2.2 全局样式与主题变量

```css
/* src/styles/global.css */
:root {
  --color-primary: #2563eb;
  --color-text: #1f2937;
  --border-color: #e5e7eb;
  --font-sans: 'Inter', system-ui, sans-serif;
}

body {
  margin: 0;
  font-family: var(--font-sans);
  color: var(--color-text);
}
```

```astro
---
// 在布局组件中引入，全站生效
import '../styles/global.css'
---
```

讲解：主题类内容（颜色、间距、字体）用 CSS 变量定义在 `:root`，各组件通过 `var(--color-primary)` 引用，实现主题统一与后续可维护。全局样式只在布局或页面中导入一次，构建时会被去重合并。

## 3. Fonts API（Astro 6+）

自定义字体常面临自托管、加载性能、隐私等复杂问题。Astro 6 起内置 Fonts API，自动完成下载、缓存、回退字体生成与预加载：

```js
// astro.config.mjs
import { defineConfig, fontProviders } from 'astro/config'

export default defineConfig({
  fonts: [
    {
      provider: fontProviders.google(),   // 从 Google Fonts 拉取并自托管
      family: 'Inter',
      weights: [400, 500, 700],
      subsets: ['latin'],
    },
    {
      provider: fontProviders.local(),    // 使用本地字体文件
      family: 'MyFont',
      path: './src/assets/MyFont.woff2',
    },
  ],
})
```

讲解：内置 provider 包括 Google、Fontsource、Adobe、Bunny、Fontshare 与 Local 等。Astro 在构建期下载字体文件并自托管（不再依赖第三方域名，符合隐私要求），自动生成 `font-display` 优化与回退字形（fallback metrics），避免布局偏移（CLS）。

### 3.1 页面中使用字体

```astro
---
import { Font } from 'astro/fonts'
---

<Font family="Inter" weights={[400, 700]} />
<h1 class="display">使用 Inter 字体的标题</h1>

<style>
  .display { font-family: 'Inter', system-ui, sans-serif; }
</style>
```

讲解：`<Font />` 组件在页面 head 中输出字体 CSS 与预加载链接。未用 `fontProviders` 配置的字体仍可直接用 CSS 引用，但建议统一走 Fonts API 以获得预加载与优化收益。

## 4. 图片优化：astro:assets

### 4.1 资源目录约定

图片等资源放 `src/assets/`（参与构建处理，可优化）或 `public/`（原样拷贝，不处理）。需要优化时用 `src/assets/`。

### 4.2 Image 组件

```astro
---
// src/components/Hero.astro
import { Image } from 'astro:assets'
import heroImg from '../assets/hero.jpg'
---

<Image
  src={heroImg}
  alt="课程封面"
  width={1200}
  height={675}
  format="webp"
  loading="lazy"
/>
```

讲解：`<Image />` 在构建期完成格式转换（webp/avif）、尺寸压缩与哈希重命名，自动输出 `srcset` 响应式尺寸并生成合适的 `width`/`height` 占位，防止 CLS。`format="webp"` 指定目标格式；可叠加 `densities`、`sizes` 适配不同屏幕。

### 4.3 Picture 组件与 getImage

```astro
---
import { Picture, getImage } from 'astro:assets'
import banner from '../assets/banner.png'
---

<!-- Picture：自动生成多格式多尺寸组合 -->
<Picture
  src={banner}
  formats={['avif', 'webp']}
  sizes="(max-width: 800px) 100vw, 800px"
  alt="横幅"
/>

<!-- getImage：编程式获取优化后的 URL -->
<script>
  const optimized = await getImage({ src: banner, width: 400 })
</script>
```

讲解：`<Picture />` 按浏览器支持自动选择 avif/webp/png，输出多个 `<source>`；`getImage` 在代码中动态生成优化 URL，适合内容集合正文里的图片处理。远程图片需在 `astro.config.mjs` 的 `image.domains`（或 `remotePatterns`）中登记域名。

### 4.4 内容集合中的图片

```ts
// content.config.ts
import { defineCollection, z } from 'astro:content'

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    heroImage: z.image().optional(),  // 图片字段自动验证并优化
  }),
})
```

讲解：schema 用 `z.image()` 声明图片字段，`getCollection` 返回的图片可直接传给 `<Image />`，在查询阶段就完成元数据校验与优化链路。

## 5. SVG 优化

Astro 支持把 SVG 文件作为组件导入：

```astro
---
// 把 SVG 导入为组件，可直接修改 fill 等属性
import Logo from '../assets/logo.svg?astro'
---

<Logo class="logo" />
<svg class="icon" aria-hidden="true">…</svg>

<style>
  .logo { width: 120px; height: 40px; }
</style>
```

讲解：`?astro` 后缀把 SVG 编译为 Astro 组件，可传 props、套样式，并自动清理无用属性。简单图标建议直接用内联 `<svg>` 或精灵图（sprite）合并，减少请求数；复杂插图用 `?astro` 保持可维护性。

## 6. 性能基线建议

第一，CSS 变量承载主题，scoped 样式承载组件细节，避免全局选择器滥用；

第二，字体统一走 Fonts API，确保预加载与回退完整；

第三，图片一律经 `<Image />` 处理，杜绝原图直出；

第四，`public/` 只放 favicon、robots.txt 等无需优化的静态文件。

## 7. 参考资源

Astro 样式指南：https://docs.astro.build/zh-cn/guides/styling/

Fonts API 指南：https://docs.astro.build/zh-cn/guides/fonts/

图片优化指南：https://docs.astro.build/zh-cn/guides/images/
