---
order: 8
title: Tailwind CSS v4 新特性
module: tailwind
category: Tailwind CSS
difficulty: intermediate
description: 'Tailwind CSS v4 新特性：Oxide 引擎、CSS-first 配置、自动检测与迁移指南'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/002-InstallConfig
  - tailwind/005-ThemeCustomization
prerequisites:
  - tailwind/002-InstallConfig
---

## 1. v4 版本背景

Tailwind CSS v4.0 于 2025 年 1 月发布，v4.3 于 2026 年 5 月发布。v4 是一次彻底的重写：构建引擎换用 Rust 编写（代号 Oxide），配置方式从 JavaScript 迁移到纯 CSS，核心目标只有一个——更快、更简单。

| 特性 | v3 | v4 |
| --- | --- | --- |
| 构建引擎 | Node.js | Rust（Oxide） |
| 配置方式 | tailwind.config.js | CSS（@theme） |
| 内容扫描 | content 数组 | 自动检测 + @source |
| 暗色模式 | 需配置 class 策略 | dark: 默认跟随系统，可 @custom-variant |
| 容器查询 | 官方插件 | 内置 |
| 色彩空间 | RGB/HEX | OKLCH |

## 2. Oxide Rust 引擎的性能提升

Oxide 引擎用 Rust 重写了编译管线，性能提升表现在三个维度：

第一，构建速度：全量构建与增量重建均比 v3 快数倍到数十倍，大型项目从秒级降到百毫秒级；

第二，内存占用：Rust 原生内存管理更高效，长时间 watch 模式不堆积内存；

第三，增量更新：源码变更后只重新生成受影响的部分，热更新延迟显著降低。

```bash
# v4 项目初始化示例
pnpm create vite@latest my-app -- --template react
cd my-app
pnpm add tailwindcss @tailwindcss/vite
```

讲解：Oxide 引擎对开发者透明，只需按 v4 方式安装即可自动获得性能收益，无需任何调优参数。

## 3. CSS-first 配置

v4 的核心变化：配置从 JS 文件迁移到 CSS。全部主题定制通过 `@theme` 完成：

```css
@import "tailwindcss";

@theme {
  --color-primary: oklch(0.623 0.214 259.8);
  --font-sans: "Inter", system-ui, sans-serif;
  --breakpoint-3xl: 1920px;
}
```

讲解：`@theme` 中每个 `--var` 既是 CSS 变量，又自动生成对应工具类。配置文件（tailwind.config.js）在 v4 中不再需要。

CSS-first 带来的收益：

第一，心智简化：不用在 JS 对象和 CSS 之间来回翻译，所有样式概念都在 CSS 中表达；

第二，调试友好：变量直接暴露在浏览器中，DevTools 可直接修改验证主题效果；

第三，生态统一：设计与工程共用同一份 CSS 变量，设计稿上的令牌能一字不差落到代码。

## 4. 自动内容检测

v4 不再需要 content 数组，安装后自动扫描源码中的模板文件：

```css
/* 旧：v3 需要配置文件声明扫描范围 */
/* tailwind.config.js
content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
*/

/* 新：v4 自动检测，零配置 */
@import "tailwindcss";
/* 仅当类名在扫描范围之外时，用 @source 补充 */
@source "../shared-components";
```

讲解：自动检测以入口 CSS 所在位置为基准向上寻找公共源码根，自动忽略 gitignore 文件与二进制文件。特殊情况用 `@source` 精确声明，见安装配置篇。

## 5. 内置容器查询

容器查询在 v3 需要 `@tailwindcss/container-queries` 插件，v4 直接内置：

```html
<div class="@container">
  <div class="grid grid-cols-1 @lg:grid-cols-3">
    <div>容器宽度达到 lg 断点时变三列</div>
  </div>
</div>
```

讲解：`@container` 声明容器，`@lg:` 等前缀查询容器宽度。组件在不同宽度的父容器中自动适配，是 v4 内置能力的典型代表。

## 6. 新增 scrollbar 工具类

v4 提供了原生的滚动条样式工具类，无需再写 `::-webkit-scrollbar`：

```html
<div class="h-40 overflow-y-scroll scrollbar-thin scrollbar-thumb-gray-400 scrollbar-track-gray-100">
  可滚动内容
</div>
```

```css
/* 也可用 @theme 定制滚动条颜色令牌 */
@theme {
  --color-scrollbar: #94a3b8;
  --color-scrollbar-hover: #64748b;
}
```

讲解：`scrollbar-thin` 控制粗细，`scrollbar-thumb-*` 与 `scrollbar-track-*` 控制滑块与轨道颜色（支持全部颜色令牌）。Firefox 浏览器使用对应的 `scrollbar-width`、`scrollbar-color` 原生属性，Tailwind 已做兼容处理。

## 7. 全新调色板

v4 的默认调色板重新设计，改用 OKLCH 色彩空间：

| 维度 | v3 调色板 | v4 调色板 |
| --- | --- | --- |
| 色彩空间 | RGB | OKLCH |
| 色阶数量 | 每色相 10 阶（50-900） | 每色相 11 阶（50-950） |
| 色相覆盖 | 22 个 | 22 个（含新增的 olive 等） |
| 视觉均匀度 | 部分色阶过渡不均 | 亮度、饱和度过渡均匀 |

```html
<button class="bg-blue-500 text-white">v3 风格</button>
<button class="bg-blue-600 text-white">v4 下建议用 600 级获得相近观感</button>
```

讲解：因为色彩空间改变，同一色阶号的最终显示颜色与 v3 不同。迁移时视觉观感可能变化，建议逐页检查重点颜色。

## 8. 迁移指南：v3 到 v4

### 8.1 安装与入口

```bash
pnpm add tailwindcss @tailwindcss/vite
```

```css
/* 旧 */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* 新 */
@import "tailwindcss";
```

讲解：三行指令合并为一行 `@import`，这是迁移的第一步，也是改动面最大的部分。

### 8.2 配置文件迁移

```css
/* 旧 tailwind.config.js 的 theme.extend 转为： */
@theme {
  --color-brand-500: #1677ff;
  --font-sans: "Inter", sans-serif;
}
```

讲解：`theme.extend` 中的内容按命名空间（color/font/spacing/breakpoint）转写为 `--var`。未扩展的默认配置直接删除，v4 内置。

### 8.3 暗色模式配置迁移

```css
/* 旧：tailwind.config.js 中 darkMode: 'class' */
/* 新：CSS 中自定义变体 */
@custom-variant dark (&:where(.dark, .dark *));
```

### 8.4 常见破坏性变化自查

第一，默认边框颜色变化：v3 默认 `border` 为 gray-200，v4 默认使用 `currentColor`，涉及边框需显式指定颜色；

第二，调色板色号观感变化：OKLCH 下同一色号显示不同，重点检查品牌色；

第三，`shadow-sm` 等阴影值微调，容器圆角默认值变化，核对设计稿；

第四，动态类名拼接（`bg-${color}-500`）在 v4 中同样不被扫描，改用完整类名。

### 8.5 官方迁移工具

```bash
npx @tailwindcss/upgrade
```

讲解：官方提供的自动化迁移工具，会重写 CSS 入口、迁移配置、处理常见语法差异。建议在 git 分支上执行，逐条审查改动后再合并。

## 9. 是否值得迁移

| 场景 | 建议 |
| --- | --- |
| 新项目 | 直接用 v4，无历史包袱 |
| 中小型 v3 项目 | 迁移成本低，收益明显，建议迁移 |
| 大型 v3 项目 | 评估调色板观感变化与插件生态兼容性后分批迁移 |
| 深度依赖 v3 生态插件 | 确认插件已支持 v4 再迁移 |

## 参考资源

Tailwind 官方 v4 发布公告：https://tailwindcss.com/blog/tailwindcss-v4

Tailwind 官方升级指南：https://tailwindcss.com/docs/upgrade-guide

Tailwind 中文文档：https://www.tailwindcss.cn/docs

## 小结

v4 用 Rust 引擎解决性能、用 CSS-first 配置解决复杂度、用自动检测解决配置负担，并把容器查询、新调色板、scrollbar 工具类直接内置。对 FANDEX 平台而言，新项目直接采用 v4，老项目按迁移指南逐步升级即可。
