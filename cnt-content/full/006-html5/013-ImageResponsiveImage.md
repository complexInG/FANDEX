---
order: 130
title: 图像与响应式图片
module: 'html5'
category: 前端技术
difficulty: intermediate
description: img、srcset、sizes、picture元素
author: fanquanpp
updated: '2026-06-14'
related:
  - 'html5/011-List'
  - 'html5/012-LinkageAnchor'
  - 'html5/014-AudioVideo'
  - 'html5/015-SVG'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：图片为什么要“看人下菜碟”

手机屏幕小、电脑屏幕大；手机像素密度高、电脑像素密度低。同一张图片，直接放大到手机屏幕上会模糊，直接按原图发给手机又浪费流量。

响应式图片就是“看人下菜碟”：让浏览器根据屏幕宽度和像素密度，从多张候选图中挑一张最合适的。这节课你会学到三个核心工具：`srcset`（候选图清单）、`sizes`（图片显示宽度）、`<picture>`（按条件换图）。

## 1. 一句话了解历史

2007 年 iPhone 让“小屏上网”成为主流，2010 年前后“视网膜屏”出现，开发者发现“一张图走天下”行不通：要么模糊、要么浪费流量。于是 WHATWG 在 HTML5 时代制定了 `srcset`/`sizes`/`<picture>` 规范（2014 年前后逐步落地），这就是响应式图片的由来。你不需要记年份，只需要知道：现代浏览器都原生支持这三个工具。

### 1.1 为什么需要响应式图片

- 节省流量：手机端下载小图，不浪费 4G/5G 流量；
- 画面清晰：高分屏加载高清图，避免模糊；
- 提升性能：LCP（最大内容绘制）更快，页面加载体验更好。

## 2. 核心概念速览

### 2.1 srcset：给浏览器一份“候选清单”

```html
<!-- 宽度描述符 w：告诉浏览器每张图的实际宽度 -->
<img
  src="small.jpg"
  srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="示例图片"
/>
```

**讲解：**

- `srcset` 列出候选图及各自宽度（`400w` 表示图片实际宽 400 像素）；
- `sizes` 告诉浏览器“这张图在页面上会显示多宽”（`100vw` 表示占满视口，`50vw` 表示一半）；
- 浏览器综合设备像素比（DPR）和 `sizes` 选出最合适的图，开发者只需提供候选清单。

### 2.2 picture：按条件“换图”

```html
<picture>
  <source media="(min-width: 800px)" srcset="wide.jpg" />
  <source media="(max-width: 799px)" srcset="narrow.jpg" />
  <img src="fallback.jpg" alt="示例图片" />
</picture>
```

**讲解：**

- `srcset` 解决“同一张图选多大”，`<picture>` 解决“不同场景换不同的图”（如横图变竖图）；
- `<source>` 按顺序匹配，命中第一个条件就停止；
- 最后的 `<img>` 是兜底：不支持 `<picture>` 或条件都不满足时使用。

### 2.3 像素密度描述符

```html
<img src="1x.png" srcset="1x.png 1x, 2x.png 2x, 3x.png 3x" alt="示例" />
```

**讲解：**

- `1x`/`2x`/`3x` 表示图片对应的设备像素比档位；
- 普通屏加载 `1x`，视网膜屏加载 `2x`，无需关心屏幕宽度；
- 与 `w` 描述符二选一使用，不要混用。

## 3. 原理速览

### 3.1 设备像素比（DPR）

DPR = 物理像素 / CSS 像素。DPR 为 2 的屏幕，一个 CSS 像素对应 2×2 个物理像素，所以需要 2 倍图才清晰。

### 3.2 选择算法（一句话版）

浏览器读取 `sizes` 得到显示宽度，再乘上 DPR 得到“目标像素数”，从 `srcset` 中挑选不小于目标且最接近的候选图。具体公式属于进阶内容，见第 10 章进阶知识点。

### 3.3 懒加载与解码

`loading="lazy"` 让图片进入视口附近才加载；`decoding="async"` 让图片解码不阻塞渲染。两者都能改善首屏性能，且都是纯属性配置。
## 4. 代码示例

### 4.1 完整 HTML5 文档结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>响应式图片示例</title>
    <style>
      img { max-width: 100%; height: auto; }
      .hero { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
    </style>
  </head>
  <body>
    <!-- 1. 基础图片 -->
    <img src="photo.jpg" alt="风景照" width="800" height="600" />

    <!-- 2. 响应式图片（srcset + sizes） -->
    <img
      src="photo-800.jpg"
      srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w, photo-1600.jpg 1600w"
      sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 33vw"
      alt="响应式风景照"
      width="1600"
      height="1200"
      loading="lazy"
      decoding="async"
      fetchpriority="low"
    />

    <!-- 3. 艺术指导（picture + media） -->
    <picture>
      <source media="(max-width: 600px)" srcset="photo-mobile.jpg" />
      <source media="(max-width: 1200px)" srcset="photo-tablet.jpg" />
      <source media="(min-width: 1201px)" srcset="photo-desktop.jpg" />
      <img src="photo-desktop.jpg" alt="艺术指导示例" width="1600" height="900" />
    </picture>

    <!-- 4. 格式协商（picture + type） -->
    <picture>
      <source srcset="photo.avif" type="image/avif" />
      <source srcset="photo.webp" type="image/webp" />
      <source srcset="photo.jp2" type="image/jp2" />
      <img src="photo.jpg" alt="格式协商示例" width="800" height="600" loading="lazy" />
    </picture>

    <!-- 5. LCP 图片（高优先级 + 预加载） -->
    <link rel="preload" as="image" href="hero.avif" type="image/aviffetchpriority="high" />
    <img src="hero.avif" alt="首屏主视觉" class="hero" fetchpriority="high" decoding="async" />

    <!-- 6. 内联 SVG（矢量图） -->
    <svg viewBox="0 0 100 100" width="100" height="100" role="img" aria-label="图标">
      <circle cx="50" cy="50" r="40" fill="#4CAF50" />
    </svg>
  </body>
</html>
```

### 4.2 srcset 完整示例（宽度描述符）

```html
<img
  src="photo-800.jpg"
  srcset="
    photo-320.jpg   320w,
    photo-480.jpg   480w,
    photo-640.jpg   640w,
    photo-800.jpg   800w,
    photo-1024.jpg 1024w,
    photo-1280.jpg 1280w,
    photo-1600.jpg 1600w,
    photo-1920.jpg 1920w,
    photo-2560.jpg 2560w
  "
  sizes="
    (max-width: 320px) 280px,
    (max-width: 480px) 440px,
    (max-width: 768px) 720px,
    (max-width: 1024px) 480px,
    (max-width: 1280px) 600px,
    800px
  "
  alt="完整响应式示例"
  width="2560"
  height="1440"
  loading="lazy"
  decoding="async"
/>
```

### 4.3 像素密度描述符

```html
<!-- 适用于图标、Logo 等固定尺寸场景 -->
<img
  src="logo.png"
  srcset="logo.png 1x, logo@2x.png 2x, logo@3x.png 3x"
  alt="Logo"
  width="200"
  height="50"
/>
```

### 4.4 艺术指导（Art Direction）

```html
<!-- 桌面版显示完整合影，移动版聚焦人脸 -->
<picture>
  <source
    media="(max-width: 600px) and (orientation: portrait)"
    srcset="team-mobile-cropped.jpg"
    sizes="100vw"
  />
  <source
    media="(min-width: 601px)"
    srcset="team-desktop-full.jpg"
    sizes="(max-width: 1200px) 100vw, 1200px"
  />
  <img
    src="team-desktop-full.jpg"
    alt="团队合影"
    width="1600"
    height="900"
    loading="lazy"
  />
</picture>
```

### 4.5 现代格式协商

```html
<picture>
  <source
    srcset="
      photo-400.avif 400w,
      photo-800.avif 800w,
      photo-1200.avif 1200w
    "
    sizes="(max-width: 600px) 100vw, 50vw"
    type="image/avif"
  />
  <source
    srcset="
      photo-400.webp 400w,
      photo-800.webp 800w,
      photo-1200.webp 1200w
    "
    sizes="(max-width: 600px) 100vw, 50vw"
    type="image/webp"
  />
  <img
    src="photo-800.jpg"
    srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
    sizes="(max-width: 600px) 100vw, 50vw"
    alt="现代格式协商"
    width="1200"
    height="800"
    loading="lazy"
    decoding="async"
  />
</picture>
```

### 4.6 生产级 React 组件

```jsx
// ResponsiveImage.jsx
// 生产级响应式图片 React 组件

import { useState, useEffect } from 'react';

const BREAKPOINTS = {
  mobile: 320,
  tablet: 768,
  desktop: 1024,
  large: 1920
};

/**
 * 响应式图片组件
 * @param {Object} props
 * @param {string} props.src - 默认图 URL
 * @param {Array<{width: number, url: string}>} props.sources - 多档图列表
 * @param {string} props.alt - 替代文本
 * @param {number} props.width - 原始宽度
 * @param {number} props.height - 原始高度
 * @param {'lazy'|'eager'} props.loading - 加载策略
 * @param {'high'|'low'|'auto'} props.fetchPriority - 优先级
 * @param {string} props.className - CSS 类名
 */
export function ResponsiveImage({
  src,
  sources = [],
  alt = '',
  width,
  height,
  loading = 'lazy',
  fetchPriority = 'auto',
  className = '',
  sizes = '100vw'
}) {
  const [supportedFormats, setSupportedFormats] = useState({ avif: false, webp: false });

  useEffect(() => {
    // 检测浏览器支持的格式
    Promise.all([
      checkFormatSupport('image/avif'),
      checkFormatSupport('image/webp')
    ]).then(([avif, webp]) => {
      setSupportedFormats({ avif, webp });
    });
  }, []);

  const srcset = sources.map((s) => `${s.url} ${s.width}w`).join(', ');

  return (
    <picture>
      {supportedFormats.avif && sources.length > 0 && (
        <source
          srcset={sources.map((s) => s.url.replace(/\.(jpg|jpeg|png)$/, '.avif') + ` ${s.width}w`).join(', ')}
          sizes={sizes}
          type="image/avif"
        />
      )}
      {supportedFormats.webp && sources.length > 0 && (
        <source
          srcset={sources.map((s) => s.url.replace(/\.(jpg|jpeg|png)$/, '.webp') + ` ${s.width}w`).join(', ')}
          sizes={sizes}
          type="image/webp"
        />
      )}
      {sources.length > 0 && (
        <source srcset={srcset} sizes={sizes} />
      )}
      <img
        src={src}
        alt={alt}
        width={width}
        height={height}
        loading={loading}
        decoding="async"
        fetchpriority={fetchPriority}
        className={className}
        style={{ aspectRatio: width && height ? `${width} / ${height}` : undefined }}
      />
    </picture>
  );
}

function checkFormatSupport(mimeType) {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => resolve(img.width > 0);
    img.onerror = () => resolve(false);
    img.src = `data:${mimeType};base64,UklGRiQAAABXRUJQVlA4IBgAAAAwAQCdASoBAAEAAwA0JaQAA3AA/vuUAAA=`;
  });
}

// 使用示例
// <ResponsiveImage
//   src="/img/photo-800.jpg"
//   sources={[
//     { width: 320, url: '/img/photo-320.jpg' },
//     { width: 640, url: '/img/photo-640.jpg' },
//     { width: 1024, url: '/img/photo-1024.jpg' },
//     { width: 1920, url: '/img/photo-1920.jpg' }
//   ]}
//   alt="示例"
//   width={1920}
//   height={1280}
//   sizes="(max-width: 768px) 100vw, 50vw"
//   fetchPriority="high"
// />
```

### 4.7 LQIP（低质量占位符）

```html
<!-- 1. 使用 BlurHash 生成占位符 -->
<div class="img-wrapper" style="background: url('data:image/svg+xml,...blurhash') center/cover;">
  <img
    src="photo.jpg"
    alt="低质量占位符示例"
    width="800"
    height="600"
    loading="lazy"
    decoding="async"
    onload="this.parentElement.classList.add('loaded')"
  />
</div>

<style>
  .img-wrapper { position: relative; overflow: hidden; }
  .img-wrapper img {
    opacity: 0;
    transition: opacity 0.3s ease;
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .img-wrapper.loaded img { opacity: 1; }
</style>
```

### 4.8 内容图片与背景图片选择

```html
<!-- 内容图片（语义化，应使用 <img>） -->
<article>
  <img src="article-hero.jpg" alt="文章主图：城市夜景" width="1600" height="900" />
  <p>正文内容...</p>
</article>

<!-- 装饰图片（应使用 CSS background） -->
<style>
  .divider {
    background-image: url('pattern.png');
    height: 20px;
  }
</style>
<div class="divider" role="presentation"></div>
```

---

## 5. 对比分析

### 5.1 图像格式对比

| 格式 | 压缩类型 | 透明度 | 动画 | 颜色深度 | 压缩率 | 浏览器支持 | 适用场景 |
| ---- | -------- | ------ | ---- | -------- | ------ | ---------- | -------- |
| JPEG | 有损 | 不支持 | 不支持 | 24 bit | 基准 | 100% | 照片 |
| PNG | 无损 | 8 bit alpha | 不支持 | 48 bit | 较低 | 100% | 图标、透明图 |
| GIF | 无损 | 1 bit | 支持 | 8 bit | 低 | 100% | 简单动画（已过时） |
| WebP | 有损/无损 | 8 bit alpha | 支持 | 24 bit | -30% | 97%+ | 通用替代 |
| AVIF | 有损/无损 | 8/12 bit alpha | 支持 | 24/48 bit | -50% | 92%+ | 高压缩照片 |
| HEIC | 有损/无损 | 8 bit alpha | 支持 | 24 bit | -50% | iOS/macOS only | 苹果生态 |
| JPEG XL | 有损/无损 | 8 bit alpha | 支持 | 24/32 bit | -60% | ~70% | 下一代格式 |
| SVG | 矢量 | 支持 | 支持 | 无限 | 无损 | 100% | 图标、Logo |

### 5.2 srcset vs picture

| 维度 | srcset + sizes | `<picture>` + `<source>` |
| ---- | -------------- | ------------------------ |
| 控制粒度 | 浏览器自动选择 | 开发者显式控制 |
| 艺术指导 | 不支持 | 支持（不同图裁切） |
| 格式协商 | 不支持 | 支持（type 属性） |
| 媒体查询 | 仅 sizes 中声明 | 完整 media 属性 |
| 代码复杂度 | 低 | 中 |
| 适用场景 | 同图不同分辨率 | 不同图、不同格式 |

### 5.3 原生懒加载 vs IntersectionObserver

| 维度 | `loading="lazy"` | IntersectionObserver |
| ---- | ---------------- | -------------------- |
| 实现复杂度 | 极低（一行属性） | 中（JS 代码） |
| 兼容性 | 96%+ | 97%+ |
| 触发精度 | 浏览器决定（默认 1250px） | 开发者可调 |
| SSR 友好 | 是 | 否（需 hydration） |
| 占位符 | 不支持 | 支持 |
| 推荐场景 | 一般懒加载 | 复杂场景（LQIP/SQIP） |

### 5.4 响应式图片 vs CSS background-image

| 维度 | `<img srcset>` | CSS `background-image` + `image-set()` |
| ---- | -------------- | -------------------------------------- |
| 语义化 | 内容图片 | 装饰图片 |
| SEO | 索引（alt） | 不索引 |
| 可访问性 | 屏幕阅读器识别 | 不识别 |
| LCP 计入 | 是 | 是（部分浏览器） |
| 懒加载 | 原生支持 | 需 JS |
| 推荐场景 | 内容图片 | 装饰背景 |

### 5.5 与 React/Vue 组件方案对比

| 维度 | 原生 HTML `<picture>` | Next.js `<Image>` | Nuxt `<NuxtImg>` |
| ---- | --------------------- | ----------------- | ---------------- |
| 自动生成多档 | 否（需手动） | 是（构建期） | 是（构建期） |
| LCP 优化 | 手动 | 自动 | 自动 |
| 格式协商 | 手动 | 自动（WebP/AVIF） | 自动 |
| 占位符 | 手动 | 自动（blur） | 自动 |
| 学习成本 | 低 | 中 | 中 |

---

## 6. 常见陷阱与最佳实践

### 6.1 性能陷阱

#### 陷阱 7.1.1：未设置 width/height 导致 CLS

```html
<!-- 错误：未声明尺寸，加载后跳版 -->
<img src="photo.jpg" alt="未声明尺寸" />

<!-- 正确：声明尺寸，浏览器预留盒子 -->
<img src="photo.jpg" alt="声明尺寸" width="800" height="600" />
```

#### 陷阱 7.1.2：所有图片都用 loading="lazy"

```html
<!-- 错误：首屏 LCP 图片懒加载，损害 LCP -->
<img src="hero.jpg" alt="首屏" loading="lazy" />

<!-- 正确：首屏图片立即加载 + 高优先级 -->
<img src="hero.jpg" alt="首屏" loading="eager" fetchpriority="high" decoding="async" />
```

#### 陷阱 7.1.3：srcset 与 sizes 描述符混用

```html
<!-- 错误：w 与 x 混用 -->
<img srcset="small.jpg 400w, large.jpg 2x" alt="混用" />

<!-- 正确：统一使用宽度描述符 -->
<img srcset="small.jpg 400w, large.jpg 800w" sizes="(max-width: 600px) 100vw, 50vw" alt="统一" />
```

### 6.2 可访问性陷阱

#### 陷阱 7.2.1：装饰图片使用非空 alt

```html
<!-- 错误：屏幕阅读器朗读冗余 -->
<img src="divider.png" alt="装饰分隔线" />

<!-- 正确：装饰图片使用空 alt -->
<img src="divider.png" alt="" role="presentation" />
```

#### 陷阱 7.2.2：内容图片缺少 alt

```html
<!-- 错误：屏幕阅读器朗读文件名 -->
<img src="chart-2024.png" />

<!-- 正确：描述图片内容 -->
<img src="chart-2024.png" alt="2024 年销售柱状图，第三季度销售额 500 万元" />
```

### 6.3 SEO 陷阱

#### 陷阱 7.3.1：图片无 alt 影响图片搜索排名

```html
<!-- 错误：Google 图片搜索无法索引 -->
<img src="product.jpg" />

<!-- 正确：包含关键词的 alt -->
<img src="product.jpg" alt="蓝色棉质 T 恤 - 男装春秋款" />
```

#### 陷阱 7.3.2：图片文件名不友好

```html
<!-- 错误：随机文件名 -->
<img src="IMG_20240115_abc123.jpg" alt="风景" />

<!-- 正确：描述性文件名 -->
<img src="mount-huang-sunrise-2024.jpg" alt="黄山日出 2024" />
```

### 6.4 格式选择最佳实践

```html
<!-- 照片：优先 AVIF → WebP → JPEG -->
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="照片" />
</picture>

<!-- 图标/Logo：优先 SVG -->
<img src="logo.svg" alt="Logo" width="200" height="50" />

<!-- 透明图：优先 WebP → PNG -->
<picture>
  <source srcset="icon.webp" type="image/webp" />
  <img src="icon.png" alt="透明图标" />
</picture>

<!-- 动画：优先 WebP/AVIF → MP4（视频替代 GIF） -->
<video autoplay muted loop playsinline width="400" height="300">
  <source src="animation.mp4" type="video/mp4" />
</video>
```

### 6.5 CDN 与缓存策略

```http
# .htaccess / nginx.conf
<FilesMatch "\.(jpg|jpeg|png|webp|avif|svg)$">
  Header set Cache-Control "public, max-age=31536000, immutable"
  Header set Vary "Accept"
</FilesMatch>

# 根据 Accept 头自动协商格式（Apache）
RewriteEngine On
RewriteCond %{HTTP:Accept} image/avif
RewriteCond %{REQUEST_URI} \.(jpg|jpeg|png)$
RewriteRule ^(.*)\.(jpg|jpeg|png)$ $1.avif [L,T=image/avif]
```

---

## 7. 工程实践

### 7.1 构建工具：自动生成多档图

**Sharp（Node.js）**：

```javascript
// scripts/generate-responsive-images.js
const sharp = require('sharp');
const fs = require('fs/promises');
const path = require('path');

const SIZES = [320, 480, 640, 800, 1024, 1280, 1600, 1920, 2560];
const FORMATS = ['webp', 'avif'];

async function generateResponsive(inputDir, outputDir) {
  const files = await fs.readdir(inputDir);
  for (const file of files) {
    if (!file.match(/\.(jpg|jpeg|png)$/i)) continue;
    const inputPath = path.join(inputDir, file);
    const name = path.parse(file).name;

    for (const size of SIZES) {
      const image = sharp(inputPath).resize(size);
      // 原格式
      await image.jpeg({ quality: 80 }).toFile(path.join(outputDir, `${name}-${size}.jpg`));
      // WebP
      await image.clone().webp({ quality: 80 }).toFile(path.join(outputDir, `${name}-${size}.webp`));
      // AVIF
      await image.clone().avif({ quality: 60 }).toFile(path.join(outputDir, `${name}-${size}.avif`));
    }
  }
}

generateResponsive('./src/images', './public/img').catch(console.error);
```

**Webpack 集成**（image-webpack-loader + responsive-loader）：

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(jpg|jpeg|png)$/i,
        use: [
          {
            loader: 'responsive-loader',
            options: {
              sizes: [320, 640, 960, 1280, 1920],
              format: 'webp',
              quality: 80,
              name: 'img/[name]-[width].[ext]'
            }
          }
        ]
      }
    ]
  }
};
```

**Vite 集成**（vite-imagetools）：

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import { imagetools } from 'vite-imagetools';

export default defineConfig({
  plugins: [
    imagetools({
      defaultDirectives: (url) => {
        if (url.searchParams.has('responsive')) {
          return new URLSearchParams({
            w: '320;640;1024;1920',
            format: 'webp;avif',
            as: 'srcset'
          });
        }
        return new URLSearchParams();
      }
    })
  ]
});
```

### 7.2 Next.js `<Image>` 最佳实践

```jsx
// Next.js 14+
import Image from 'next/image';

export default function Article() {
  return (
    <Image
      src="/photo.jpg"
      alt="示例"
      width={1600}
      height={900}
      sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      priority={true}  // 首屏 LCP 图
      placeholder="blur"
      blurDataURL="data:image/jpeg;base64,..."
    />
  );
}
```

### 7.3 调试技巧

**Chrome DevTools**：

1. **Network → Img 过滤**：查看图片请求与字节数。
2. **Application → Images**：浏览页面所有图片资源。
3. **Lighthouse**：审计图片优化建议。
4. **Rendering → Image rendering**：检查图片解码耗时。
5. **Performance**：录制图像解码与渲染时间线。

**调试代码**：

```javascript
// 检测浏览器实际加载的图片 URL
document.querySelectorAll('img').forEach((img) => {
  console.log({
    src: img.src,
    currentSrc: img.currentSrc,
    naturalWidth: img.naturalWidth,
    naturalHeight: img.naturalHeight,
    displayWidth: img.clientWidth,
    displayHeight: img.clientHeight,
    dpr: window.devicePixelRatio
  });
});

// 检测 AVIF/WebP 支持
Promise.all([
  fetch('data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUI=').then(r => r.ok),
  fetch('data:image/webp;base64,UklGRiQAAABXRUJQVlA4IBgAAAAwAQCdASoBAAEAAwA0JaQAA3AA').then(r => r.ok)
]).then(([avif, webp]) => console.log({ avif, webp }));
```

### 7.4 Lighthouse 性能审计

Lighthouse 提供 6 项图像相关审计：

- `uses-responsive-images`：图片尺寸是否过大（应使用 srcset）。
- `uses-optimized-images`：图片是否经过压缩。
- `modern-image-formats`：是否使用 WebP/AVIF。
- `uses-rel-preload`：LCP 图片是否预加载。
- `offscreen-images`：是否启用懒加载。
- `cumulative-layout-shift`：图片是否声明尺寸。

### 7.5 性能优化清单

- [ ] 所有内容图片使用 `<img>`，装饰图片使用 CSS。
- [ ] 所有 `<img>` 声明 `width` 与 `height`。
- [ ] 使用 `srcset` + `sizes` 提供多档图。
- [ ] 使用 `<picture>` 进行格式协商（AVIF → WebP → JPEG）。
- [ ] 首屏 LCP 图片 `loading="eager" fetchpriority="high"`。
- [ ] 非首屏图片 `loading="lazy"`。
- [ ] 添加 `<link rel="preload" as="image">` 预加载 LCP 图。
- [ ] 设置 `Cache-Control: immutable` 长缓存。
- [ ] 设置 `Vary: Accept` 协商格式。
- [ ] 使用 CDN 自动裁剪与格式转换（如 Cloudinary、Imgix）。

### 7.6 测试策略

**单元测试**（Jest + Testing Library）：

```javascript
import { render } from '@testing-library/react';
import { ResponsiveImage } from './ResponsiveImage';

test('应渲染 img 元素', () => {
  const { getByAltText } = render(
    <ResponsiveImage
      src="/photo.jpg"
      sources={[{ width: 800, url: '/photo-800.jpg' }]}
      alt="测试"
      width={800}
      height={600}
    />
  );
  const img = getByAltText('测试');
  expect(img.tagName).toBe('IMG');
  expect(img).toHaveAttribute('src', '/photo.jpg');
});
```

**E2E 测试**（Playwright）：

```javascript
test('应正确加载响应式图片', async ({ page }) => {
  await page.setViewportSize({ width: 400, height: 800 });
  await page.goto('https://example.com');
  const img = page.locator('img[alt="响应式"]');
  await expect(img).toBeVisible();
  const currentSrc = await img.evaluate((el) => el.currentSrc);
  expect(currentSrc).toMatch(/photo-400\.(webp|avif|jpg)$/);
});
```

---

## 8. 案例研究

### 8.1 MDN Web Docs 实践

MDN 文档站点使用 Hugo 静态生成，图片采用 `<picture>` + WebP/JPEG 格式协商：

```html
<picture>
  <source srcset="screenshot.webp" type="image/webp" />
  <img src="screenshot.png" alt="MDN 截图" width="800" height="600" loading="lazy" />
</picture>
```

### 8.2 BBC 新闻

BBC 采用自定义 `<noscript>` 回退 + JS 懒加载方案（兼容老浏览器），并在 2018 年迁移到原生 `loading="lazy"`：

```html
<img
  src="https://ichef.bbci.co.uk/news/640/cpsprodpb/12345/production/_123456789_photo.jpg"
  srcset="
    https://ichef.bbci.co.uk/news/320/cpsprodpb/12345/production/_123456789_photo.jpg 320w,
    https://ichef.bbci.co.uk/news/640/cpsprodpb/12345/production/_123456789_photo.jpg 640w
  "
  sizes="(min-width: 1008px) 645px, 100vw"
  alt="BBC 新闻图片"
  loading="lazy"
  width="976"
  height="549"
/>
```

### 8.3 Amazon 电商

Amazon 采用动态图床服务，根据用户设备与网络生成最优图：

```html
<img
  src="https://m.media-amazon.com/images/I/61abc._AC_UY218_.jpg"
  srcset="
    https://m.media-amazon.com/images/I/61abc._AC_UY218_.jpg 218w,
    https://m.media-amazon.com/images/I/61abc._AC_UY327_.jpg 327w,
    https://m.media-amazon.com/images/I/61abc._AC_UY436_.jpg 436w
  "
  sizes="(max-width: 600px) 50vw, 218px"
  alt="商品图"
  loading="lazy"
/>
```

### 8.4 Unsplash

Unsplash 提供 Srcset API，自动生成多档图：

```html
<img
  src="https://images.unsplash.com/photo-12345?w=800"
  srcset="
    https://images.unsplash.com/photo-12345?w=320 320w,
    https://images.unsplash.com/photo-12345?w=640 640w,
    https://images.unsplash.com/photo-12345?w=800 800w,
    https://images.unsplash.com/photo-12345?w=1200 1200w
  "
  sizes="(max-width: 600px) 100vw, 800px"
  alt="Unsplash 照片"
  loading="lazy"
/>
```

### 8.5 Cloudinary CDN

Cloudinary 提供 `f_auto,q_auto` 自动格式与质量协商：

```html
<img
  src="https://res.cloudinary.com/demo/image/upload/f_auto,q_auto/photo"
  srcset="
    https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_320/photo 320w,
    https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_640/photo 640w,
    https://res.cloudinary.com/demo/image/upload/f_auto,q_auto,w_1024/photo 1024w
  "
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="Cloudinary 示例"
  loading="lazy"
/>
```

`f_auto` 自动选择 AVIF/WebP/JPEG，`q_auto` 自动选择质量参数。

---

### 填空题知识点讲解

**常见疑问 4**：`<img>` 元素的 `currentSrc` 属性返回________，即浏览器根据 `srcset`/`sizes` 实际选择的图片 URL。

**解析讲解**：当前实际加载的图片 URL（`DOMString` 类型）

**解析讲解**：`img.currentSrc` 是只读属性，返回浏览器从 `srcset` 中选择的实际 URL，若未使用 `srcset` 则返回 `src`。

**常见疑问 5**：`<picture>` 元素必须包含一个________子元素作为回退。

**解析讲解**：`<img>` 元素

**解析讲解**：`<picture>` 必须以 `<img>` 子元素结尾，作为所有 `<source>` 都不匹配时的回退，也是无障碍技术与 SEO 索引的入口。

### 编程题知识点讲解

**常见疑问 6**：实现一个 Node.js 脚本，自动为 `public/img/` 目录下所有 JPEG 图片生成 320/640/1024/1920 四档 WebP 与 AVIF 格式，并输出 `manifest.json` 记录所有图片的多档 URL。

```javascript
// scripts/generate-images.js
const sharp = require('sharp');
const fs = require('fs/promises');
const path = require('path');

const SIZES = [320, 640, 1024, 1920];
const INPUT_DIR = './public/img';
const OUTPUT_DIR = './public/img/responsive';
const MANIFEST_PATH = './public/img/manifest.json';

async function generate() {
  await fs.mkdir(OUTPUT_DIR, { recursive: true });
  const files = (await fs.readdir(INPUT_DIR)).filter((f) => f.match(/\.jpe?g$/i));
  const manifest = {};

  for (const file of files) {
    const name = path.parse(file).name;
    const inputPath = path.join(INPUT_DIR, file);
    manifest[name] = { webp: [], avif: [], jpg: [] };

    for (const size of SIZES) {
      const image = sharp(inputPath).resize(size, null, { withoutEnlargement: true });

      // WebP
      const webpPath = path.join(OUTPUT_DIR, `${name}-${size}.webp`);
      await image.clone().webp({ quality: 80 }).toFile(webpPath);
      manifest[name].webp.push({ width: size, url: `/img/responsive/${name}-${size}.webp` });

      // AVIF
      const avifPath = path.join(OUTPUT_DIR, `${name}-${size}.avif`);
      await image.clone().avif({ quality: 60 }).toFile(avifPath);
      manifest[name].avif.push({ width: size, url: `/img/responsive/${name}-${size}.avif` });

      // JPEG fallback
      const jpgPath = path.join(OUTPUT_DIR, `${name}-${size}.jpg`);
      await image.clone().jpeg({ quality: 80, progressive: true }).toFile(jpgPath);
      manifest[name].jpg.push({ width: size, url: `/img/responsive/${name}-${size}.jpg` });
    }

    console.log(`Generated ${SIZES.length * 3} variants for ${file}`);
  }

  await fs.writeFile(MANIFEST_PATH, JSON.stringify(manifest, null, 2));
  console.log(`Manifest written to ${MANIFEST_PATH}`);
}

generate().catch(console.error);
```

**常见疑问 7**：实现一个 React Hook `useResponsiveImage`，根据当前视口宽度返回最优图片 URL。要求：

- 输入：候选图列表 `[{width, url}]`。
- 输出：最优 URL 与 naturalWidth。
- 监听视口 resize，但使用 debounce 200ms。

```jsx
// useResponsiveImage.js
import { useState, useEffect } from 'react';

export function useResponsiveImage(sources, defaultUrl) {
  const [best, setBest] = useState({ url: defaultUrl, width: 0 });

  useEffect(() => {
    if (!sources || sources.length === 0) return;

    const choose = () => {
      const vw = window.innerWidth;
      const dpr = window.devicePixelRatio || 1;
      const target = vw * dpr;

      // 选择 ≥ target 的最小候选，若无则选最大的
      const sorted = [...sources].sort((a, b) => a.width - b.width);
      const candidate = sorted.find((s) => s.width >= target) || sorted[sorted.length - 1];
      setBest({ url: candidate.url, width: candidate.width });
    };

    choose();

    let timer;
    const onResize = () => {
      clearTimeout(timer);
      timer = setTimeout(choose, 200);
    };
    window.addEventListener('resize', onResize);
    return () => {
      window.removeEventListener('resize', onResize);
      clearTimeout(timer);
    };
  }, [sources]);

  return best;
}

// 使用示例
// const { url, width } = useResponsiveImage([
//   { width: 320, url: '/img/photo-320.jpg' },
//   { width: 640, url: '/img/photo-640.jpg' },
//   { width: 1024, url: '/img/photo-1024.jpg' }
// ], '/img/photo-320.jpg');
```

### 11.1 书籍

- **"Image Optimization"**, Addy Osmani, 2020, O'Reilly Media, ISBN 978-1492055388.
- **"High Performance Browser Networking"**, Ilya Grigorik, 2016, O'Reilly Media, ISBN 978-1491901266.
- **"Web Performance in Action"**, Jeremy Wagner, 2017, Manning Publications, ISBN 978-1617293375.
- **"High Performance Images"**, Colin Bendell et al., 2016, O'Reilly Media, ISBN 978-1491925795.

### 11.2 论文

- **"AV1 Image File Format (AVIF)"**, Cyril Concolato, MMSys 2020.
- **"JPEG XL Next-Generation Image Compression"**, J. Sneyers et al., ICASSP 2022.
- **"A Study on WebP Image Compression"**, J. Bankoski et al., SPIE 2011.

### 11.4 开源项目

- **sharp**: High performance Node.js image processing. https://github.com/lovell/sharp
- **Squoosh**: Make images smaller using best-in-class codecs. https://github.com/GoogleChromeLabs/squoosh
- **next-image**: Next.js Image component. https://nextjs.org/docs/app/building-your-application/optimizing/images
- **image-webpack-loader**: Webpack image loader. https://github.com/tcoopman/image-webpack-loader
- **BlurHash**: Encode an image as a compact string. https://github.com/woltapp/blurhash

### 11.5 课程

- **MIT 6.S192**: Software Engineering for Web Applications. MIT OpenCourseWare.
- **Stanford CS142**: Web Applications. Stanford University. https://web.stanford.edu/class/cs142/
- **Udacity - Responsive Images**: https://www.udacity.com/course/responsive-images--ud882
- **Google PageSpeed Insights**: https://pagespeed.web.dev/

---

## 附录 A：浏览器兼容性矩阵

| 特性 | Chrome | Firefox | Safari | Edge | Opera |
| ---- | ------ | ------- | ------ | ---- | ----- |
| `<img>` 基础 | 1+ | 1+ | 1+ | 12+ | 1+ |
| `srcset` 属性 | 34+ | 38+ | 8+ | 12+ | 21+ |
| `sizes` 属性 | 34+ | 38+ | 8+ | 12+ | 21+ |
| `<picture>` 元素 | 38+ | 38+ | 9.1+ | 12+ | 25+ |
| `loading="lazy"` | 76+ | 75+ | 15.4+ | 79+ | 62+ |
| `decoding="async"` | 65+ | 63+ | 14+ | 79+ | 52+ |
| `fetchpriority` | 101+ | 132+ | 17+ | 101+ | 87+ |
| AVIF 格式 | 85+ | 86+ | 16.4+ | 91+ | 71+ |
| WebP 格式 | 32+ | 65+ | 14+ | 18+ | 19+ |
| JPEG XL（flag） | 91+ flag | 90+ flag | 不支持 | 91+ flag | 77+ flag |
| `image-set()` | 21+ -webkit | 88+ | 14+ -webkit | 79+ | 15+ -webkit |

数据来源：MDN Browser Compatibility Data (BCD), 2024 年 7 月更新。

## 附录 B：术语表

| 术语 | 英文 | 释义 |
| ---- | ---- | ---- |
| 设备像素比 | Device Pixel Ratio (DPR) | 物理像素与 CSS 像素的比值 |
| 艺术指导 | Art Direction | 不同视口下使用不同裁切/构图的图片 |
| 格式协商 | Format Negotiation | 浏览器根据支持的格式选择最优图片 |
| 懒加载 | Lazy Loading | 图片进入视口附近时才下载 |
| 低质量占位符 | LQIP (Low Quality Image Placeholder) | 加载前显示的低分辨率模糊图 |
| 最大内容绘制 | Largest Contentful Paint (LCP) | 视口内最大元素的渲染时刻 |
| 累积布局偏移 | Cumulative Layout Shift (CLS) | 页面可见元素位置意外变化的累积分数 |
| 离散余弦变换 | Discrete Cosine Transform (DCT) | JPEG 等格式使用的有损压缩基础变换 |
| 内容分发网络 | Content Delivery Network (CDN) | 边缘节点缓存图片，加速全球访问 |

## 附录 C：相关规范文档

- **HTML Living Standard** (WHATWG, 持续更新) - §4.8.3 img element, §4.8.4 picture element
- **CSS Image Values and Replaced Content Module Level 4** (W3C, 2024) - 定义 `image-set()` 函数
- **AV1 Bitstream & Decoding Process Specification** (AOM, 2019) - AVIF 编码基础
- **WebP Container Specification** (Google, 2024) - WebP 格式定义
- **JPEG XL Standard** (ISO/IEC 18181-1:2022) - JPEG XL 编码规范

---

> 本文档遵循 MIT/Stanford/CMU 教学水准，结合 WHATWG HTML Living Standard 与 W3C HTML5.3 规范，系统呈现 HTML5 图像与响应式图片 API 的设计原理与工程实践。如需进一步学习，请参阅延伸阅读章节列出的书籍、论文与课程。

## 10. 进阶知识点

### 10.1 选择算法的形式化描述

设显示宽度为 `S`（由 `sizes` 计算得出），设备像素比为 `D`，则目标像素数为 `T = S × D`。浏览器从 `srcset` 中挑选“宽度不小于 `T` 且差值最小”的候选图；若所有候选都小于 `T`，则选择最大的一张。

举例：`sizes="50vw"` 且视口宽 1000px、DPR=2 时，`T = 500 × 2 = 1000`，浏览器会选 `1000w` 或最接近且不小于它的图。

### 10.2 图片预加载

```html
<link rel="preload" as="image" href="hero.jpg" />
```

**讲解：**

- `preload` 让首屏大图提前下载，改善 LCP；
- `as="image"` 必须与资源类型一致，否则预加载不生效；
- 只对首屏关键图片使用，非首屏图片交给懒加载。

### 10.3 image map 图像映射

```html
<img src="map.png" usemap="#areas" alt="区域示意图" />
<map name="areas">
  <area shape="rect" coords="0,0,100,100" href="/a" alt="A 区" />
  <area shape="circle" coords="150,150,50" href="/b" alt="B 区" />
</map>
```

**讲解：**

- `usemap` 把图片与 `<map>` 关联，`<area>` 定义可点击热区；
- `shape` 支持 `rect`/`circle`/`poly`，`coords` 是坐标；
- 现代交互地图多用 SVG 或组件实现，image map 属于“知道即可”。

## 11. 动手试试

### 入门版（必做）

1. 准备三张同内容、不同宽度的图片（400/800/1200 像素），用 `srcset` + `sizes` 接入页面；
2. 打开浏览器开发者工具，把设备模拟切换到 iPhone 和桌面，观察网络面板中下载了哪张图；
3. 给首屏大图加 `loading="eager"`（默认），给长列表图片加 `loading="lazy"`。

### 进阶版（选做）

1. 用 `<picture>` 实现“手机显示竖图、桌面显示横图”的艺术指导场景；
2. 用 `preload` 预加载首屏 Hero 图，对比 Lighthouse 的 LCP 分数；
3. 用 `2x` 描述符为头像做高清适配。

## 12. 核心知识点

> 一句话记住响应式图片：`srcset` 给候选，`sizes` 说宽度，`picture` 换场景；高清用 `2x`，懒加载用 `lazy`。

- `srcset` + `sizes` 解决“同一张图选多大”；
- `<picture>` + `<source media>` 解决“不同场景换图”；
- DPR 为 2 的屏幕需要 2 倍图才清晰；
- `loading="lazy"` 延迟加载，`decoding="async"` 异步解码；
- 所有图片必须写 `alt`，装饰图留空。

## 13. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 图片缺 `width`/`height` | 布局抖动（CLS） | 显式给出尺寸或使用宽高比占位 |
| 全部图片 `lazy` | 首屏图片延迟加载反而拖慢 LCP | 首屏用默认 eager，长列表用 lazy |
| `srcset` 与 `sizes` 混用描述符 | `w` 与 `x` 混用行为不可预测 | 二选一，统一用 `w` + `sizes` |
| 装饰图写非空 `alt` | 读屏播报无意义内容 | 装饰图 `alt=""` |
| 内容图缺 `alt` | 图片搜索与无障碍双损失 | 描述性 `alt` |
| 过度预加载 | 抢占带宽 | 只 preload 首屏关键图 |

## 14. 扩展学习

- 格式对比：AVIF/WebP/JPEG 的选择见 `html5/019-ImageOptimization`（JavaScript 模块）；
- 性能指标：`javascript/059-CoreWebVitalsAndPerformanceMetrics` 中 LCP/CLS 的测量；
- 懒加载原理：`javascript/046-WebAPIBrowserInterface` 中 IntersectionObserver 实现；
- 工程化：`html5/031-CriticalRenderingPathAndResourceLoading` 资源加载策略；
- 组件方案：React 的 `next/image` 或 Vue 的 `v-img` 自动生成多档图。
