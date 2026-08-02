---
order: 520
title: 可访问性样式
module: 'css'
category: 前端技术
difficulty: intermediate
description: 让样式不成为障碍：对比度、焦点可见、减少动效与文本缩放，四个维度讲清可访问性样式的落地要点。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/004-Accessibility'
  - 'css/023-CSSVariableCustomAttribute'
prerequisites:
  - 'css/019-MediaQuery'
---


## 一句话理解

可访问性样式 = 让信息不依赖"视力、听力、精细动作或快速反应"也能被获取：
重点管好对比度、焦点、动效和文本缩放四件事。

## 为什么需要

- 全球约 15% 的人存在某种障碍，低对比度、无焦点、闪烁动效都在制造障碍。
- 无障碍也是工程指标：键盘可达、对比达标，往往让所有用户都更好用。
- 很多问题只是几行 CSS 的事，成本极低。

## 四件事

**1. 对比度**

正文与背景的对比度建议达到 4.5:1（大字号可放宽到 3:1）。

```css
/* 用浅色文字时检查对比度，不要只凭"看得清"判断 */
.muted {
  color: #6b7280; /* 在白色背景上约 4.6:1，正文可用 */
}

.muted-sm {
  color: #9ca3af; /* 约 2.5:1，只适合装饰性内容 */
}
```

**2. 焦点可见**

永远不要裸写 `outline: none`。去掉默认焦点框时，必须提供自定义样式：

```css
.btn:focus-visible {
  outline: 2px solid var(--color-accent-base);
  outline-offset: 2px;
}
```

`:focus-visible` 只在键盘导航时显示焦点框，鼠标点击不打扰，是当前最佳实践。

**3. 减少动效**

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

更克制但更精细的做法：只在用户偏好减少动效时，把大位移动画改为透明度过渡。

**4. 文本缩放**

```css
html {
  /* 允许用户自定义浏览器字号生效，而不是锁死 px */
  font-size: 100%;
}

body {
  font-size: 1rem; /* 跟随根字号 */
}

/* 内容容器不要写死高度，防止放大后文字被裁切 */
.card {
  min-height: 0;
}
```

## 检查清单

- 页面能否只用 Tab + Enter 完整操作？
- 所有交互元素在键盘聚焦时有可见指示？
- 正文对比度 ≥ 4.5:1，错误提示不只靠颜色区分？
- 浏览器放大到 200% 或只改字号后，内容不重叠、不裁切？
- 动效有 `prefers-reduced-motion` 降级？

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 无障碍是给残障人士的 | 临时受伤、老人、弱网、强光环境都受益 |
| 颜色对比"看着还行"就行 | 用工具测量（如 Lighthouse、axe）而非目测 |
| 只用颜色传达状态 | 状态必须叠加图标/文字等非颜色线索 |
| 焦点框很丑所以去掉 | 用 `:focus-visible` 兼顾美观与可用 |

## 小结

可访问性样式没有魔法，就是四条纪律：对比度达标、焦点可见、动效可降级、文字可缩放。
配合 [HTML 无障碍](/FANDEX/html5/004-Accessibility/) 的结构语义，就能覆盖绝大多数障碍场景。
