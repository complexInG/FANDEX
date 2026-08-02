---
order: 310
title: 关键渲染路径与资源加载
module: 'html5'
category: 前端技术
difficulty: advanced
description: 从 HTML 解析到首屏像素，讲清关键渲染路径的每一步，以及 async、defer、preload、prefetch 的正确用法。
author: fanquanpp
updated: '2026-08-02'
related:
  - 'css/035-CriticalRenderPathOptimization'
  - 'javascript/059-CoreWebVitalsAndPerformanceMetrics'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---


## 一句话理解

关键渲染路径 = 浏览器把 HTML/CSS 变成首屏像素的必经流水线；
资源加载策略就是"决定哪些资源在这条流水线上排队、哪些走旁路"。

## 流水线五步

1. **HTML 解析**：构建 DOM 树。
2. **CSS 解析**：构建 CSSOM 树（CSS 默认是渲染阻塞资源）。
3. **合并**：DOM + CSSOM 生成渲染树。
4. **布局**：计算每个节点的几何位置。
5. **绘制**：把像素画到屏幕上。

其中任何一步被阻塞，首屏就晚一点。普通 `<script>` 会阻塞第 1 步，
未内联的 CSS 会阻塞第 2 步。

## 脚本加载：async 与 defer

| 属性 | 下载时机 | 执行时机 | 适用 |
| --- | --- | --- | --- |
| 无 | 遇到即下载 | 下载完立即执行，阻塞解析 | 极少使用 |
| `async` | 异步下载 | 下载完立即执行（不保证顺序） | 独立统计/广告脚本 |
| `defer` | 异步下载 | HTML 解析完成后按顺序执行 | 大多数业务脚本 |

```html
<script defer src="/js/main.js"></script>
<script async src="/js/analytics.js"></script>
```

**讲解：**

- 普通 `<script>` 遇到即下载并立即执行，HTML 解析被暂停；
- `async` 下载不阻塞，但执行时机不可控，适合相互独立的脚本；
- `defer` 下载不阻塞，HTML 解析完成后按文档顺序执行，是业务脚本的首选。

## 资源提示：preload / prefetch / preconnect

```html
<!-- 首屏关键资源：提前下载，不改变优先级 -->
<link rel="preload" href="/fonts/body.woff2" as="font" type="font/woff2" crossorigin>

<!-- 下一屏可能用到的资源：空闲时下载 -->
<link rel="prefetch" href="/page-next.html">

<!-- 提前建立跨域连接：节省 DNS/TCP/TLS 时间 -->
<link rel="preconnect" href="https://api.example.com">
```

**讲解：**

- `preload` 提前下载首屏确定要用的资源，`as` 必须与资源类型一致；
- `prefetch` 在空闲时下载“未来可能用”的资源，优先级低；
- `preconnect` 提前完成 DNS/TCP/TLS 握手，节省第三方接口的首字节时间。

| 提示 | 时机 | 注意 |
| --- | --- | --- |
| preload | 立即、高优先级 | 只用于首屏确定会用到的资源，滥用会挤占带宽 |
| prefetch | 空闲时、低优先级 | 用于用户下一步可能访问的页面 |
| preconnect | 立即建连 | 只对确实要请求的域名使用 |

## 优化清单

- 关键 CSS 尽量内联或少量拆分，首屏样式不依赖额外请求。
- 业务脚本全部 `defer`，把 HTML 解析让给首屏。
- 字体用 `preload` + `font-display: swap`，避免不可见文字期。
- 图片给宽高或 `aspect-ratio`，防止布局抖动。
- 首屏外组件用懒加载，配合 `prefetch` 预取下一步。

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 所有资源都 preload | preload 会抬高请求优先级，滥用反而拖慢关键资源 |
| async 比 defer 快 | async 执行时机不可控，业务脚本顺序敏感时必须用 defer |
| prefetch 会加速当前页 | prefetch 针对"未来页面"，对当前页没有帮助 |
| CSS 只影响样式不影响性能 | CSSOM 阻塞渲染，大 CSS 会直接推迟首屏 |

## 动手试试

先复制下面这个最小示例到本地 `load.html`，用来做加载实验：

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>资源加载实验</title>
    <script src="slow.js"></script>
  </head>
  <body>
    <h1>首屏内容</h1>
  </body>
</html>
```

另建一个 `slow.js`，内容随意（如 `console.log('loaded')`），把上面 `<script>` 依次改成 `<script defer>` 与 `<script async>` 对比。

1. 打开任意网站，按 F12 进入 Network 面板，勾选“禁用缓存”后刷新；
2. 观察瀑布图：找出阻塞首屏的脚本（普通 `<script>` 会让后续资源排队）；
3. 把脚本改成 `defer` 或 `async` 再对比，确认首屏时间变化；
4. 在 Performance 面板录制刷新过程，找到 HTML 解析、布局、绘制的分段时间；
5. 进阶挑战：给字体加 `preload` + `font-display: swap`，对比文字渲染时间。

> 回到你写的第一个页面（001 的 `index.html`），试着把其中的 `<script>` 标签加上 `defer`，对比加与不加的加载速度差异。

## 核心知识点

> 一句话记住关键渲染路径：HTML 建 DOM，CSS 建 CSSOM，合并成渲染树再布局绘制；脚本用 `defer`，关键资源用 `preload`，未来资源用 `prefetch`。

- 关键渲染路径五步：解析 HTML → 解析 CSS → 生成渲染树 → 布局 → 绘制；
- 普通脚本阻塞解析，业务脚本一律 `defer`；
- CSS 是渲染阻塞资源，首屏 CSS 应内联或精简；
- `preload` 抢首屏、`prefetch` 备未来、`preconnect` 省握手；
- 优化效果用 Performance 面板与 Lighthouse 验证。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 滥用 preload | 抬高优先级挤占带宽 | 只 preload 首屏确定资源 |
| 业务脚本用 async | 执行顺序不可控 | 顺序敏感用 defer |
| 大 CSS 外链 | CSSOM 延迟首屏 | 关键样式内联、非关键异步加载 |
| 忽略字体加载 | FOIT 不可见文字 | preload + font-display: swap |
| 图片无尺寸 | 布局抖动（CLS） | 设置宽高或 aspect-ratio |

## 扩展学习

- CSS 侧：`css/035-CriticalRenderPathOptimization` 的渲染路径优化清单；
- 指标验证：`javascript/059-CoreWebVitalsAndPerformanceMetrics` 中 LCP/CLS/TBT 的测量；
- 资源加载：`html5/013-ImageResponsiveImage` 中图片的优先级与懒加载；
- 工程实践：构建工具的资源拆分与预加载清单生成。

## 小结

把资源分三类：**首屏必须的**（内联/高优先级）、**当前页次要的**（defer/lazy）、
**未来可能用的**（prefetch/preconnect）。配合
`css/035-CriticalRenderPathOptimization` 与 `javascript/059-CoreWebVitalsAndPerformanceMetrics` 形成闭环验证。
