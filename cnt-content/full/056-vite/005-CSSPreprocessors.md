---
order: 5
title: Vite CSS 与预处理器
module: vite
category: Vite
difficulty: intermediate
description: 'Vite 样式方案：CSS Modules、SCSS/LESS、PostCSS 与 Tailwind 集成'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/004-StaticAssets
  - vite/007-BuildSplit
prerequisites:
  - vite/003-ConfigFile
---
## 1. Vite 对 CSS 的开箱支持

Vite 对 CSS 的处理几乎零配置：在 JS/TS 中 `import './style.css'`，开发环境由 dev server 注入，生产构建自动抽取为独立的 `.css` 文件并压缩。

```ts
// main.ts
import './style.css'   // 引入后自动生效
```

讲解：Vite 会解析 CSS 中的 `@import` 与 `url()` 引用（图片、字体等资源会走 004 篇介绍的静态资源管线），并把 CSS 与 JS 的依赖关系绑定——某个 CSS 仅被特定 chunk 使用时会跟随拆分，实现按需加载。生产构建默认启用 **CSS 代码分割**，见第 6 节。

## 2. CSS Modules：局部作用域

CSS 的全局作用域是样式冲突的根源。CSS Modules 让每个类名自动变成带哈希的局部名字：

```css
/* Button.module.css */
.btn {
  padding: 8px 16px;
  background: #4f46e5;
}
.active {
  opacity: 0.6;
}
```

```tsx
// Button.tsx
import styles from './Button.module.css'

export function Button({ active }: { active: boolean }) {
  return <button className={`${styles.btn} ${active ? styles.active : ''}`}>
    Click
  </button>
}
```

讲解：约定规则是文件名以 `.module.css` 结尾（`.module.scss` 同理）。构建后 `styles.btn` 会被替换成类似 `_btn_1x3f2` 的唯一类名，从根本上避免样式冲突。

| 写法 | 作用 |
| --- | --- |
| `.module.css` / `.module.scss` 结尾 | 启用 CSS Modules |
| 普通 `.css` | 全局样式 |

也可以关闭某文件的局部化，或自定义命名规则：

```ts
// vite.config.ts
export default defineConfig({
  css: {
    modules: {
      // 生成更具可读性的类名（开发环境）
      generateScopedName: '[name]__[local]__[hash:base64:5]',
    },
  },
})
```

讲解：生产构建默认采用短哈希类名以压缩体积；开发环境建议用 `[name]__[local]` 便于调试。全局样式（normalize.css 等）仍建议用普通 `.css`。

## 3. 集成 SCSS / LESS

Vite 本身不做预处理器编译，但内置了对它们的识别。只需安装对应编译器：

```bash
# SCSS / Sass
pnpm add -D sass
# LESS
pnpm add -D less
```

安装后即可直接使用：

```scss
// styles/main.scss
$primary: #4f46e5;

.card {
  color: $primary;
  &:hover {
    opacity: 0.8;
  }
}
```

```ts
import './styles/main.scss'   // 无需任何配置
```

讲解：Vite 8 使用**现代 Sass API** 编译（依赖 `sass-embedded` 时速度更快）。注意：以前常见的 `dart-sass` 兼容写法在旧版本弃用，若编译报错请检查 sass 版本。

### 3.1 共享变量：additionalData

多个组件都要用同一套 SCSS 变量时，用 `additionalData` 全局注入，避免每个文件重复 `@import`：

```ts
// vite.config.ts
export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        // 每个 scss 文件自动注入这两行
        additionalData: `@use "/src/styles/variables" as *;`,
      },
    },
  },
})
```

讲解：注意 `@use` 语法（Sass 推荐替代 `@import`）要求导入的 `_variables.scss` 中变量使用 `!default` 定义。`additionalData` 只注入到源文件，不会影响第三方库。

## 4. PostCSS：自动加前缀等

PostCSS 是一个 CSS 后处理生态，Vite 内置支持。创建 `postcss.config.js`（或 `postcss.config.cjs`）即可：

```js
// postcss.config.js
export default {
  plugins: {
    // 自动添加浏览器厂商前缀（-webkit-、-moz- 等）
    autoprefixer: {},
  },
}
```

```bash
pnpm add -D autoprefixer
```

讲解：Vite 读取项目根目录的 PostCSS 配置并自动应用。autoprefixer 需配合 `browserslist`（在 package.json 或 `.browserslistrc` 中声明目标浏览器）。**性能提示**：Vite 8 中生产构建的 CSS 压缩默认由 Lightning CSS 承担（见 009 篇），无需再装 cssnano。

## 5. 集成 Tailwind CSS

以 Tailwind CSS v4 为例（v4 改为原生 CSS 优先、零配置）：

```bash
pnpm add tailwindcss @tailwindcss/vite
```

```ts
// vite.config.ts
import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
})
```

```css
/* src/index.css */
@import "tailwindcss";
```

```ts
// main.ts 中引入
import './index.css'
```

讲解：v4 通过 Vite 插件直接工作，不再需要 `tailwind.config.js` 与 PostCSS 配置。若使用 Tailwind v3，则是 `pnpm add -D tailwindcss postcss autoprefixer` + 初始化配置 + PostCSS 插件方式，二者配置入口不同，注意区分版本。

## 6. CSS 代码分割与按需加载

生产构建默认行为：

```text
每个异步 chunk（动态 import 引入的模块）中使用的 CSS
会被抽取到独立的 .css 文件，随 chunk 一起按需加载
```

```ts
// 路由懒加载组件，其样式自动独立成 chunk 并按需加载
const Dashboard = lazy(() => import('./pages/Dashboard'))
```

讲解：这意味着"只访问首页不下载管理页样式"。若希望全量打包为单个 CSS 文件，可设置：

```ts
// vite.config.ts
export default defineConfig({
  build: {
    cssCodeSplit: false,   // 关闭 CSS 分割，合并为一个文件
  },
})
```

讲解：小项目或整页风格统一时可关闭分割减少请求；大型应用建议保留默认，配合路由懒加载实现样式按需。

## 7. 常见陷阱

陷阱一：SCSS 变量在组件中未定义。检查 `additionalData` 注入路径是否正确、是否用了 `!default`。

陷阱二：类名被压缩后难以调试。开发环境 CSS Modules 用可读命名（见 2 节配置）。

陷阱三：Tailwind v4 指令不生效。确认 `@import "tailwindcss"` 写入了入口 CSS 且插件已注册。

陷阱四：预处理器安装后未重启。新增依赖后需重启 dev server 才会生效。

## 8. 参考资源

Vite CSS 特性：https://vite.dev/guide/features#css

Vite 预处理器配置：https://vite.dev/config/shared-options#css-preprocessoroptions

Tailwind CSS 官方文档：https://tailwindcss.com/docs/installation/using-vite
