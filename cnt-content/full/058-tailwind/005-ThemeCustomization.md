---
order: 5
title: Tailwind CSS 主题定制与设计令牌
module: tailwind
category: Tailwind CSS
difficulty: intermediate
description: 'Tailwind CSS 主题定制：@theme 设计令牌、OKLCH 色彩与 CSS-first 配置'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/002-InstallConfig
  - tailwind/008-V4Features
prerequisites:
  - tailwind/002-InstallConfig
---

## 1. 设计令牌是什么

设计令牌（Design Token）是把"颜色、字号、间距、圆角"等设计决策命名为可复用变量的产物。主题定制本质上就是"重新定义这些令牌"，让 `bg-primary`、`text-sm` 指向你自己的品牌取值。

v4 之前，主题在 `tailwind.config.js` 中配置；v4 改为 CSS-first：用 `@theme` 块在 CSS 中声明令牌，浏览器与构建器共享同一套变量。

## 2. @theme 基础用法

```css
/* src/styles/global.css */
@import "tailwindcss";

@theme {
  --color-primary: #1677ff;
  --color-primary-hover: #4096ff;
  --color-surface: #ffffff;
  --color-text-main: #1f1f1f;
  --font-sans: "Inter", system-ui, sans-serif;
  --radius-card: 12px;
  --shadow-card: 0 2px 8px rgb(0 0 0 / 0.08);
}
```

```html
<button class="bg-primary text-white rounded-card px-4 py-2 hover:bg-primary-hover">
  主按钮
</button>
<div class="bg-surface shadow-card rounded-card text-text-main p-6">卡片</div>
```

讲解：`--color-primary` 会同时生成 `bg-primary`、`text-primary`、`border-primary`、`fill-primary` 等全套工具类；`--font-sans` 覆盖默认字体族；`--radius-card` 生成 `rounded-card`；`--shadow-card` 生成 `shadow-card`。

命名规则：`@theme` 中变量名对应的前缀决定工具类种类：

| 变量前缀 | 生成的工具类 |
| --- | --- |
| `--color-*` | `bg-*`、`text-*`、`border-*`、`fill-*` 等 |
| `--font-*` | `font-*`（字体族） |
| `--text-*` | `text-*`（字号） |
| `--spacing-*` | `p-*`、`m-*`、`gap-*`、`w-*` 等 |
| `--radius-*` | `rounded-*` |
| `--shadow-*` | `shadow-*` |
| `--breakpoint-*` | 响应式断点前缀 |

## 3. --color-* 与默认色板的关系

在 `@theme` 中定义 `--color-*` 有两种语义：

第一，新增令牌：定义 `--color-brand-500` 后，`bg-brand-500` 可用，默认色板不受影响；

第二，覆盖默认令牌：重新定义 `--color-blue-500`，会覆盖 Tailwind 预设的蓝色 500。

```css
@theme {
  /* 覆盖默认色板中的 blue 系，全站 blue-* 使用品牌蓝 */
  --color-blue-500: #1677ff;
  --color-blue-600: #0958d9;
  --color-blue-700: #003eb3;

  /* 新增品牌色系 */
  --color-brand-50: #e6f4ff;
  --color-brand-500: #1677ff;
  --color-brand-600: #0958d9;
}
```

讲解：覆盖默认令牌要谨慎，它会影响所有引用该令牌的内置类；新增品牌色则完全安全。推荐"新增 + 少量覆盖"的组合策略。

## 4. OKLCH 色彩空间

Tailwind v4 的默认调色板改用 OKLCH 色彩空间：

```css
@theme {
  /* 用 oklch() 定义颜色，亮度与饱和度更均匀 */
  --color-brand-500: oklch(0.623 0.214 259.8);
  --color-brand-600: oklch(0.546 0.245 262.9);
}
```

讲解：OKLCH 的三个参数分别是亮度 L（0-1）、饱和度 C、色相 H（角度）。相比 HEX/RGB，OKLCH 的色阶过渡在视觉上更均匀，明暗变化符合人眼感知，因此在同一色系内做 50-950 色阶时效果更好。

实际项目可以直接用 HEX（如 `#1677ff`）或 `oklch()` 混用，构建时浏览器原生支持 oklch 函数。若需兼容旧浏览器，Tailwind 会自动生成兜底颜色。

## 5. 与 tailwind.config.js 对比

| 维度 | v3（tailwind.config.js） | v4（@theme 块） |
| --- | --- | --- |
| 配置位置 | JS 配置文件 | 项目 CSS 文件 |
| 主题定义 | `theme.extend` 对象 | `--var` 变量声明 |
| 内容扫描 | `content` 数组 | 自动检测 + `@source` |
| 动态主题切换 | 需 JS 注入变量 | CSS 变量天然支持运行时覆盖 |
| 类型提示 | 无 | 编辑器可识别 CSS 变量 |

v3 写法（仅作对比，v4 不再使用）：

```js
// tailwind.config.js（v3 旧写法）
module.exports = {
  content: ['./src/**/*.{html,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: { primary: '#1677ff' },
    },
  },
}
```

v4 等价写法：

```css
@theme {
  --color-primary: #1677ff;
}
```

讲解：v4 将"配置"彻底收敛进 CSS：学习心智更小，配置文件数量减少，且 CSS 变量在浏览器端可见，可直接用 DevTools 调试主题。

## 6. 设计令牌落地实践

### 6.1 令牌分层

工程上建议把令牌分为三层：

第一层，基础令牌：原始取值，如 `--color-blue-500: #1677ff`、`--spacing-4: 1rem`；

第二层，语义令牌：映射业务语义，如 `--color-primary: var(--color-blue-500)`、`--color-danger: var(--color-red-500)`；

第三层，组件令牌：落到具体组件，如 `--color-btn-bg: var(--color-primary)`。

```css
@theme {
  /* 基础层 */
  --color-blue-500: #1677ff;
  --color-red-500: #f5222d;

  /* 语义层：通过引用基础令牌形成依赖 */
  --color-primary: var(--color-blue-500);
  --color-danger: var(--color-red-500);
}
```

讲解：语义层引用基础层后，未来换肤只需改基础层，语义层与组件层无需变动。

### 6.2 运行时换肤

因为令牌就是 CSS 变量，运行时换肤只需覆盖变量：

```js
// theme-switcher.js
const themes = {
  light: { '--color-primary': '#1677ff', '--color-surface': '#ffffff' },
  dark: { '--color-primary': '#4096ff', '--color-surface': '#141414' },
}

function applyTheme(name) {
  const vars = themes[name]
  const root = document.documentElement
  for (const [key, value] of Object.entries(vars)) {
    root.style.setProperty(key, value)
  }
}
```

讲解：组件里全部使用语义类（`bg-primary`、`bg-surface`），切换主题时 JS 只改变量，样式零改动。这是 CSS-first 相比旧配置方案的核心红利。

### 6.3 覆盖默认令牌的注意点

在 `@theme` 之外覆盖 CSS 变量不会自动生成新工具类，只会影响已生成类名的运行时取值：

```css
:root {
  /* 运行时覆盖，不影响构建期生成的类 */
  --color-primary: #4096ff;
}
```

讲解：构建期令牌在 `@theme` 内定义；运行时动态覆盖写在 `:root` 或元素上。两者职责不同，不要混淆。

## 7. 调试主题

第一，使用浏览器 DevTools：打开样式面板能看到 `bg-primary` 展开为 `background-color: var(--color-primary)`，沿变量链追溯取值；

第二，检查构建产物：v4 只输出实际使用到的令牌，未使用的 `--color-*` 不会进入最终 CSS；

第三，编辑器提示：安装官方 VS Code 扩展后，类名悬停可看到对应的 CSS 声明与令牌来源。

## 参考资源

Tailwind 官方主题文档：https://tailwindcss.com/docs/theme

Tailwind 官方颜色文档：https://tailwindcss.com/docs/colors

OKLCH 介绍：https://developer.mozilla.org/zh-CN/docs/Web/CSS/color_value/oklch

## 小结

`@theme` 让设计令牌以 CSS 变量形态存在，同时生成全套工具类。语义化分层 + 运行时变量覆盖，实现了"改一处、全站生效"的主题能力。下一篇讲解响应式与暗色模式，进一步发挥令牌的威力。
