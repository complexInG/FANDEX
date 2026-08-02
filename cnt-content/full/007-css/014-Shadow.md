---
order: 140
title: 阴影
module: 'css'
category: 前端技术
difficulty: beginner
description: box-shadow、text-shadow
author: fanquanpp
updated: '2026-08-02'
related:
  - 'css/012-StackingContext'
  - 'css/013-Gradient'
  - 'css/015-BackgroundEnhancement'
  - 'css/016-CSS3GridGridLayout'
prerequisites:
  - 'css/001-CSS3OverviewBasicSyntax'
---

## 0. 直觉：光从左上角来

阴影模拟“光从左上角照下来”：元素向右下投射影子。`box-shadow` 的六个参数依次是水平偏移、垂直偏移、模糊半径、扩散半径、颜色、`inset`（内阴影）。

最常用的写法是 `0 2px 8px rgba(0,0,0,0.1)` 这类“轻投影”；多层阴影叠加可以做出更真实的“材料高度”。

## 1. box-shadow

```css
box-shadow: offset-x offset-y blur-radius spread-radius color inset;
```

```css
.box {
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}
.box {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
.box {
  box-shadow:
    0 1px 2px rgba(0, 0, 0, 0.07),
    0 2px 4px rgba(0, 0, 0, 0.07),
    0 4px 8px rgba(0, 0, 0, 0.07);
}
```

**讲解：**

- 参数顺序：`offset-x offset-y blur spread color`；
- `inset` 让阴影向内，适合凹陷效果（按钮按下、输入框内阴影）；
- 多层阴影用逗号分隔，第一层在最上面；
- 多层同色小模糊阴影（如示例第三组）能模拟更柔和的“材料阴影”。

## 2. text-shadow

```css
.text {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
.neon {
  text-shadow:
    0 0 7px #fff,
    0 0 42px #0fa,
    0 0 82px #0fa;
}
```

**讲解：** `text-shadow` 与 `box-shadow` 参数相同，但作用于文字轮廓；多层叠加可做霓虹发光效果，颜色用亮色 + 大模糊半径。

## 3. 实战效果

```css
.card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.elevation-1 {
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.12),
    0 1px 2px rgba(0, 0, 0, 0.24);
}
.elevation-2 {
  box-shadow:
    0 3px 6px rgba(0, 0, 0, 0.16),
    0 3px 6px rgba(0, 0, 0, 0.23);
}
```

**讲解：** 卡片阴影配合 `transition` 在 hover 时“抬起”（阴影变大变散）；`elevation-1/2` 是 Material Design 的层级阴影体系，用两三层阴影模拟不同高度。

## 4. drop-shadow 滤镜

```css
.icon {
  filter: drop-shadow(2px 4px 6px rgba(0, 0, 0, 0.3));
}
```

box-shadow 沿盒子形状，drop-shadow 沿元素实际轮廓（适合 PNG 图标）。

**讲解：** `drop-shadow` 是 `filter` 滤镜函数，阴影跟随元素的实际形状（透明 PNG 的轮廓），而 `box-shadow` 只跟随矩形盒子；不规则图标用 `drop-shadow`，普通卡片用 `box-shadow`。

## 5. 进阶知识点

### 5.1 阴影变量

```css
:root {
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.12);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.16);
}
```

**讲解：** 把阴影定义为设计令牌（CSS 变量），全站统一层级；深色模式下可以覆盖 `--shadow-*` 的阴影颜色（用带白调的半透明色）。

### 5.2 内阴影

```css
.pressed {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}
```

**讲解：** `inset` 让阴影向内投射，适合按钮按下态、输入框凹陷感。

### 5.3 长阴影与霓虹

```css
.long-shadow {
  box-shadow: 10px 10px 0 0 #aaa, 20px 20px 0 0 #bbb;
}
.neon {
  text-shadow: 0 0 7px #fff, 0 0 42px #0fa;
}
```

**讲解：** 长阴影用多层位移阴影叠加；霓虹用文字阴影的多层发光（亮色 + 大模糊）。

## 6. 本章综合挑战（选做）

1. 用 CSS 变量定义 `--shadow-sm/md/lg` 三层阴影体系；
2. 做一张 hover 时“抬起”的卡片（阴影变大 + transition）；
3. 给 PNG 图标加 `drop-shadow`，对比 `box-shadow` 的差异；
4. 用 `inset` 做按钮按下态。

## 7. 核心知识点

> 一句话记住阴影：`box-shadow` 六参数（偏移/模糊/扩散/颜色/inset），多层逗号分隔；`text-shadow` 管文字，`drop-shadow` 跟形状。

- `box-shadow: offset-x offset-y blur spread color [inset]`；
- 多层阴影逗号分隔，第一层在最上；
- `inset` 内阴影适合按压/凹陷效果；
- `text-shadow` 作用于文字，可做发光；
- `drop-shadow`（filter）跟随元素形状；
- 阴影建议用变量统一管理，深色模式单独适配。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 阴影过重 | 页面显脏 | 用低透明度（0.08-0.16）小模糊 |
| 阴影不随主题 | 深色模式下刺眼 | 阴影颜色用变量并适配深色 |
| 大量元素阴影 | 绘制开销大 | 减少模糊半径与数量 |
| 用 box-shadow 做图标阴影 | 出现方框 | 用 drop-shadow |
| 忘记 transition | 阴影突变 | hover 变化加过渡 |

## 9. 扩展学习

- 滤镜体系：`css/057-CSSFilters`；
- 背景：`css/015-BackgroundEnhancement`；
- 动画：`css/017-CSSAnimationTransition`；
- 设计令牌：`css/023-CSSVariableCustomAttribute`。
