---
order: 510
title: 排版与网格系统
module: css
category: '007-css'
difficulty: intermediate
description: 用字号阶梯、行高、8pt 间距与 CSS 变量搭一套可复用的排版网格，让页面看起来专业而不是"随手排的"。
author: fanquanpp
created: '2026-08-02'
updated: '2026-08-02'
related:
  - 'css/023-CSSVariableCustomAttribute'
  - 'css/030-ResponsiveDesign'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
quiz:
  - type: choice
    question: 排版系统中"垂直节奏"主要指什么？
    options:
      - 所有元素等宽
      - 行高与间距遵循同一数值体系，视觉间隔稳定
      - 每行文字长度一致
      - 使用网格布局
    answer: 1
    explanation: 垂直节奏让标题、正文、列表的行距在同一个"节奏"上，滚动阅读更舒适。
  - type: fill
    question: 用 CSS 函数____可以写出随视口平滑变化、又有上下限的字号。
    answer: clamp()
    hint: '如 font-size: clamp(1rem, 0.9rem + 0.5vw, 1.5rem)。'
references:
  - type: website
    authors:
      - web.dev Team
    year: 2026
    title: Learn CSS：排版与网格
    venue: web.dev
    url: https://web.dev/learn/css
    accessedDate: '2026-08-02'
  - type: documentation
    authors:
      - MDN Contributors
    year: 2026
    title: CSS clamp() 函数
    venue: MDN
    url: https://developer.mozilla.org/zh-CN/docs/Web/CSS/clamp
    accessedDate: '2026-08-02'
etymology:
  - term: 排版
    english: Typography
    origin: 源自活字印刷时代，type 指铅字，graphy 指书写与规则，即"字的排布法则"。
estimatedReadingTime: 7
lastReviewed: '2026-08-02'
reviewer: fanquanpp
---

## 一句话理解

排版系统 = 一套**有规律的数值**：字号阶梯（type scale）、行高、间距与网格。
它让不同页面看起来同属一个产品，而不是每个页面各自"发挥"。

## 为什么需要

- 随手选的字号与间距，在滚动阅读时会显得杂乱。
- 设计令牌（CSS 变量）让全局改字号、改间距只需改一处。
- 响应式页面里，字号阶梯配合 `clamp()` 能平滑过渡。

## 核心概念

**1. 字号阶梯（Type Scale）**

以正文为基准，按固定比例放大/缩小：

```css
:root {
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px 基准 */
  --text-lg: 1.25rem;   /* 20px */
  --text-xl: 1.5rem;    /* 24px */
  --text-2xl: 2rem;     /* 32px */
}
```

**2. 行高与垂直节奏**

行高也走同一套数字，让相邻文本块的间距看起来稳定：

```css
:root {
  --leading-tight: 1.25;
  --leading-normal: 1.6;
  --leading-loose: 1.8;
  --space-1: 4px;
  --space-2: 8px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
}
```

**3. 8pt 间距体系**

间距只取 4 或 8 的倍数（`4/8/16/24/32/48`），
元素之间的缝隙在视觉上有明确的层级，不会出现"3px 还是 5px"的选择困难。

## 落地示例

```css
/* 响应式字号：随视口平滑变化，且不超出上下限 */
.page-title {
  font-size: clamp(1.5rem, 1.2rem + 1.6vw, 2.5rem);
  line-height: var(--leading-tight);
}

.page-body {
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  /* 段落间距与 8pt 体系对齐 */
  margin-block: var(--space-4);
}

.card {
  padding: var(--space-4);
  gap: var(--space-3);
}
```

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 标题越大越好 | 字号阶梯保证层级关系，标题与正文的比例比绝对大小更重要 |
| 行高越宽松越好 | 正文 1.5-1.7 合适，标题用紧凑行高，避免留白失衡 |
| 间距随手填 | 间距来自同一数值体系，视觉才统一 |
| 只用 px 固定字号 | 用 rem 基准 + clamp() 兼顾可访问性与响应式 |

## 小结

排版系统的本质是"约束"：字号、行高、间距都从有限的数值集合里取值。
先用 CSS 变量把阶梯定义出来，再让所有组件消费变量，页面自然会整齐。
下一步可结合 [CSS 变量与自定义属性](/FANDEX/css/023-CSSVariableCustomAttribute/) 做主题化扩展。
