---
order: 7
title: Tailwind CSS 组件复用
module: tailwind
category: Tailwind CSS
difficulty: intermediate
description: 'Tailwind CSS 组件复用：@apply、@layer、@plugin 与组件封装'
author: fanquanpp
updated: '2026-08-01'
related:
  - tailwind/003-UtilityCore
  - tailwind/005-ThemeCustomization
prerequisites:
  - tailwind/003-UtilityCore
---

## 1. 复用的两种思路

工具类写多了，会发现自己反复粘贴同一组类名。解决复用的路径有两条：

第一，组件级复用：在 React/Vue 中封装组件，类名写在组件内部，调用方只传 props。这是主流推荐方案；

第二，CSS 级复用：用 `@apply` 把一组工具类提取为一个自定义类。适合"无框架的纯 HTML 项目"或"工具类组合实在过长"的场景。

两条路径可以并存：组件封装管结构，`@apply` 管样式沉淀。

## 2. @apply 组合工具类

```css
@import "tailwindcss";

@layer components {
  .btn-primary {
    @apply inline-flex items-center justify-center rounded-lg bg-blue-600 px-4 py-2 font-medium text-white transition-colors hover:bg-blue-700;
  }
}
```

```html
<button class="btn-primary">主按钮</button>
<a href="#" class="btn-primary">作为链接使用</a>
```

讲解：`@apply` 把工具类"编译回"普通 CSS 规则。`.btn-primary` 封装了按钮的完整样式，使用时一行类名即可，且与组件框架无关。

`@apply` 支持变体与令牌引用：

```css
@layer components {
  .card {
    @apply rounded-xl border border-gray-200 bg-white p-6 shadow-sm dark:border-gray-800 dark:bg-gray-900;
  }
}
```

讲解：`dark:` 变体可以出现在 `@apply` 内部，编译器会展开为对应的暗色规则。`@apply` 中也可以使用 `@theme` 定义的令牌类（如 `bg-primary`）。

## 3. @layer 分层

v4 用 `@layer` 管理层叠顺序，Tailwind 定义了四个内置层：

| 层 | 内容 | 优先级（后者覆盖前者） |
| --- | --- | --- |
| `@layer theme` | 设计令牌（`--color-*` 等变量） | 1 |
| `@layer base` | Preflight 重置、`@theme` 生成的基础样式 | 2 |
| `@layer components` | `@apply` 提取的组件类 | 3 |
| `@layer utilities` | 工具类 | 4 |

```css
@import "tailwindcss";

@layer base {
  /* 全局基础样式：作用于 base 层，位于工具类之下 */
  body {
    @apply antialiased text-gray-800;
  }
}

@layer components {
  .btn-primary { @apply ...; }
}
```

讲解：组件类放进 `@layer components` 后，工具类（utilities 层）优先级更高，因此"元素同时有组件类和工具类"时，工具类会覆盖组件类，这符合直觉：覆盖细节时直接用工具类。

## 4. @plugin 插件机制

v4 用 `@plugin` 指令加载插件，替代 v3 的 `plugins` 配置项。插件可以注册工具类、组件类或自定义变体。

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";
@plugin "./my-plugin.js";
```

讲解：`@plugin` 可加载 npm 包或本地文件路径。官方常用插件包括排版插件 `@tailwindcss/typography`（美化长文阅读）与表单插件 `@tailwindcss/forms`（表单控件样式重置）。

```js
// my-plugin.js —— 注册一个自定义工具类
import plugin from 'tailwindcss/plugin'

export default plugin.withOptions(() => {
  return {
    utilities: {
      '.text-balance': { 'text-wrap': 'balance' },
    },
  }
})
```

讲解：插件 API 用于需要编程式注册类名的场景。绝大多数项目用不到自定义插件，优先考虑 `@utility`；只有需要"动态生成大量类名"或"发布可共享配置"时才写插件。

## 5. @theme inline 的注意事项

`@theme inline` 用于"令牌值引用其他令牌且需要内联展开"的场景：

```css
@theme inline {
  --color-primary: var(--color-blue-600);
}

/* 对比普通 @theme：值为字面量，运行时不会跟随 blue-600 变化 */
@theme {
  --color-primary: var(--color-blue-600);
}
```

讲解：`@theme inline` 把变量值直接内联到工具类声明处，不再保留变量引用链。适合"语义令牌引用基础令牌"且希望类名直接使用最终值的场景；普通 `@theme` 保留引用，适合需要运行时换肤。

使用注意：

第一，`@theme inline` 中的变量不会出现在最终的 `:root` 中，DevTools 里看不到该变量；

第二，默认主题的变量内部使用 `@theme inline` 展开，以保证工具类取值稳定；

第三，需要"类名渲染结果独立于 CSS 变量链"时使用 inline，其余情况用普通 `@theme`。

## 6. @starting-style 入场动画

`@starting-style` 是 CSS 原生规则，用于定义元素首次渲染（或 display 从 none 切换）前的起始样式，配合过渡实现入场动画。v4 工具类中可直接使用：

```css
@layer base {
  @starting-style {
    .fade-in {
      opacity: 0;
      transform: translateY(8px);
    }
  }
}

@layer components {
  .fade-in {
    @apply transition-all duration-300;
  }
}
```

```html
<div class="fade-in">页面加载时淡入上移</div>
```

讲解：`@starting-style` 声明"动画起点"，元素进入文档时从起点过渡到正常样式。与 JS 控制的显隐（display 切换）配合，可实现平滑的弹出面板动画，无需引入动画库。

## 7. 与组件库配合

### 7.1 组件库 + 工具类覆盖

以 React 组件库（如 Headless UI、shadcn/ui）为例，其组件内部已定义基础样式，Tailwind 负责外观层：

```tsx
import { Menu } from '@headlessui/react'

export function Dropdown() {
  return (
    <Menu>
      <Menu.Button className="rounded-md bg-gray-900 px-4 py-2 text-sm text-white">
        选项
      </Menu.Button>
      <Menu.Items className="mt-2 w-48 rounded-lg border bg-white p-1 shadow-lg">
        <Menu.Item>
          {({ active }) => (
            <a className={`block px-3 py-2 text-sm ${active ? 'bg-gray-100' : ''}`}>
              菜单项
            </a>
          )}
        </Menu.Item>
      </Menu.Items>
    </Menu>
  )
}
```

讲解：Headless UI 只管理交互逻辑，外观全部由 Tailwind 类名驱动，`active` 状态通过回调类名动态拼接。这种"逻辑组件 + 样式工具类"的分工是主流实践。

### 7.2 类名合并工具

动态拼接类名时，用 `clsx` 与 `tailwind-merge` 保证类名不冲突：

```tsx
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function Button({ variant = 'primary', className = '' }) {
  return (
    <button
      className={twMerge(
        'rounded-lg px-4 py-2 font-medium',
        variant === 'primary' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-800',
        className,
      )}
    >
      按钮
    </button>
  )
}
```

讲解：`twMerge` 能识别同一属性的工具类并保留最后一个，避免外部传入 `bg-red-500` 时与内部 `bg-blue-600` 冲突产生两条背景规则。

## 8. 复用决策速查

| 场景 | 推荐方案 |
| --- | --- |
| 组件框架项目 | 组件封装 + 工具类（不写 @apply） |
| 纯 HTML / 服务端模板 | `@apply` 提取组件类 |
| 需要共享的复杂样式 | `@utility` 或插件 |
| 官方插件能力（排版/表单） | `@plugin` 引入 |
| 入场动画 | `@starting-style` + 过渡 |

## 参考资源

Tailwind 官方 Functions & Directives：https://tailwindcss.com/docs/functions-and-directives

@apply 文档：https://tailwindcss.com/docs/functions-and-directives#apply

tailwind-merge：https://github.com/dcastil/tailwind-merge

## 小结

组件复用没有银弹：框架项目优先组件封装，纯 HTML 项目用 `@apply` 提取，共享能力走 `@plugin`，动画用 `@starting-style`。工具类始终是最终的表达方式，复用只是把它们组织得更好。
