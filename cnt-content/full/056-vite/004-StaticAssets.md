---
order: 4
title: Vite 静态资源处理
module: vite
category: Vite
difficulty: beginner
description: 'Vite 静态资源：public 目录、import 引入、base 路径与资源压缩'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/003-ConfigFile
  - vite/007-BuildSplit
prerequisites:
  - vite/002-QuickStart
---
## 1. 两种资源引入方式

Vite 中静态资源有两条完全不同的处理路径，先用一张表记住核心区别：

| 方式 | 存放位置 | 构建处理 | 适用场景 |
| --- | --- | --- | --- |
| `public/` 目录 | `public/` | 原样复制，不做处理 | favicon、robots.txt、不常变的静态文件 |
| import 引入 | `src/` 任意位置 | 参与构建：压缩、加哈希、按需加载 | 图片、字体、SVG 等由代码引用的资源 |

```text
public/ 中的文件：public/logo.png  ->  dist/logo.png（路径不变）
import 引入的文件：src/assets/a.png ->  dist/assets/a-3f2b1c.png（自动加内容哈希）
```

讲解：两条路径不可混用。放进 `public/` 的文件不能通过 import 引入（会报错），应始终使用**绝对路径** `/logo.png` 引用；需要构建优化的资源则不要放进 `public/`。

## 2. public 目录

`public/` 目录下的文件会在构建时**原样复制**到产物根目录，适合存放不需要加工的静态文件：

```html
<!-- index.html 中引用 -->
<link rel="icon" type="image/svg+xml" href="/vite.svg" />
```

```bash
# public/robots.txt 构建后出现在 dist/robots.txt，路径不变
# 引用时用绝对路径（以 / 开头），且不能加 base 前缀
```

讲解：`public/` 的文件不会被压缩、不会加哈希、不能 import。生产环境若需设置 CDN，这些文件应通过 CDN 或 nginx 单独托管。注意：引用时写 `/vite.svg` 而不是 `vite.svg`，并且**不要**手动拼接 `base` 前缀——Vite 会自动处理 base（见第 4 节）。

## 3. import 引入资源

这是 Vite 推荐的资源使用方式，资源会参与构建并自动优化：

```ts
// src/main.ts
import logo from './assets/logo.png'
import data from './data.json'

const img = document.createElement('img')
img.src = logo
document.body.appendChild(img)

console.log(data.title)  // JSON 文件直接 import 为对象
```

讲解：Vite 默认支持图片（png/jpg/gif/svg/webp/avif）、字体（woff/woff2/eot/ttf/otf）、媒体（mp4/webm/ogg/mp3/wav）、`json` 等常见类型。import 后得到的是**处理后的 URL**（字符串），构建时自动加内容哈希实现长期缓存。

### 3.1 assetsInclude：扩展资源类型

不认识的扩展名需要手动登记：

```ts
// vite.config.ts
import { defineConfig } from 'vite'

export default defineConfig({
  assetsInclude: ['**/*.wasm', '**/*.pdf'],
})
```

讲解：`assetsInclude` 是 glob 数组，匹配到的文件会按静态资源处理。也可用 `?url` 后缀临时引入单个文件（见下）。

### 3.2 显式后缀与内联

```ts
// ?url：强制按 URL 处理，不参与其他转换
import workerUrl from './worker.js?url'

// ?inline：强制转成 base64 字符串内联进代码
import tinyIcon from './icon.svg?inline'
```

讲解：`?url` 常用于 Web Worker 等必须拿到文件地址的场景；`?inline` 适合小体积资源，减少请求数。小体积资源（默认小于 4KB）会自动内联为 base64，可通过 `build.assetsInlineLimit` 调整阈值。

### 3.3 import.meta.glob：批量导入

```ts
// 动态引入 src/pages 下所有 .ts 模块
const modules = import.meta.glob('./pages/*.ts')

// 遍历执行（懒加载）
for (const path in modules) {
  modules[path]().then((mod) => {
    console.log('加载', path, mod.default)
  })
}
```

讲解：`import.meta.glob` 返回 `{ 路径: 加载函数 }` 的映射，默认是懒加载（函数返回 Promise）。加 `{ eager: true }` 参数则改为同步导入。它在 Vite 8 中还支持大小写不敏感匹配（`{ caseSensitiveMatch: false }`），常用于路由自动注册、多语言文件加载。

## 4. base 与 URL 路径

`base` 决定所有资源引用的公共前缀，是部署配置的关键：

```ts
// vite.config.ts
export default defineConfig({
  // 部署到域名根路径
  base: '/',
  // 部署到 https://example.com/fandex/ 子路径
  // base: '/fandex/',
})
```

| 部署场景 | base 取值 | 产物中资源路径 |
| --- | --- | --- |
| 域名根路径 | `/` | `/assets/app-xxx.js` |
| 子路径 | `/fandex/` | `/fandex/assets/app-xxx.js` |
| CDN 绝对地址 | `https://cdn.xxx.com/` | `https://cdn.xxx.com/assets/...` |

讲解：`base` 必须是绝对路径或完整 URL，且**以 `/` 结尾**。import 引入的资源会自动拼接 base；`public/` 中的文件按绝对路径引用时也会自动处理，但 `public/` 内的**源码级引用**（如 css 中的 url 相对路径）不受 base 影响，这是常见的 404 坑。

## 5. 资源压缩与优化

Vite 8 对静态资源提供了开箱即用的优化能力：

```bash
# 构建时自动执行：
# 1. 图片/字体等二进制资源：超出 assetsInlineLimit 的不压缩，直接复制
# 2. 文本类资源（svg、css、js）：自动压缩
# 3. 资源名自动追加内容哈希
```

构建输出示例：

```text
dist/
├── assets/
│   ├── index-B3k2f0a1.js      # JS 产物（带哈希）
│   ├── index-Ckq5f2a2.css     # CSS 产物
│   └── logo-1a2b3c4d.png      # 图片（带哈希）
└── index.html
```

讲解：内容哈希（如 `logo-1a2b3c4d`）保证"内容不变则文件名不变"，配合服务器的 `Cache-Control: immutable` 可实现永久缓存，内容更新后哈希变化自动失效。SVG 建议通过 `?inline` 内联或直接放在组件中，减少请求。

## 6. 常见陷阱

陷阱一：`public/` 中的文件 import 报错。public 目录不支持 import，请移到 `src/assets/` 用相对/别名路径引入。

陷阱二：部署后资源 404。检查 `base` 是否与部署路径匹配，子路径部署必须设置 `base: '/子路径/'`。

陷阱三：引用 public 文件加了 base 前缀。`public` 文件用 `/xxx.png` 引用即可，Vite 会自动拼接 base，手动拼接会双写前缀。

陷阱四：大图拖慢加载。图片应走 `src/assets` + import 引入，并用构建插件（如 `vite-plugin-imagemin`）压缩，或直接使用 CDN 图床。

## 7. 参考资源

Vite 静态资源处理：https://vite.dev/guide/assets

Vite 构建选项（assetsInlineLimit 等）：https://vite.dev/config/build-options

Vite 中文文档：https://cn.vite.dev/
