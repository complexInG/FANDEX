---
order: 590
title: 前端性能指标与 Core Web Vitals
module: 'javascript'
category: 前端技术
difficulty: intermediate
description: '用 LCP、INP、CLS 三个核心指标学会量化"页面快不快"，并给出浏览器端采集与上报的完整示例。'
author: fanquanpp
updated: '2026-08-02'
related:
  - 'javascript/047-DebugPerformanceOptimization'
  - 'css/042-CSSPerformanceOptimizationDetailed'
prerequisites:
  - 'javascript/047-DebugPerformanceOptimization'
---


## 一句话理解

性能不能靠"感觉"，Core Web Vitals 用三个数字回答：
**加载快不快（LCP）、响应快不快（INP）、稳不稳（CLS）**。

## 三个核心指标

| 指标 | 全称 | 衡量什么 | 良好阈值 |
| --- | --- | --- | --- |
| LCP | Largest Contentful Paint | 最大内容（图片/标题块）渲染时间 | ≤ 2.5s |
| INP | Interaction to Next Paint | 交互（点击/输入）到界面响应 | ≤ 200ms |
| CLS | Cumulative Layout Shift | 布局意外跳动的累计程度 | ≤ 0.1 |

辅助指标：TTFB（首字节）、FCP（首次内容绘制）、TBT（主线程阻塞时间），
用于定位 LCP/INP 的具体瓶颈。

## 怎么测量

两个层面缺一不可：

- **实验室**：Lighthouse 在固定条件下跑分，适合开发期回归。
- **真实用户（RUM）**：用 PerformanceObserver 在生产环境采集，代表真实网络与设备。

```javascript
// 用 web-vitals 库采集并上报（推荐方式）
import { onLCP, onINP, onCLS } from 'web-vitals';

function report(metric) {
  // 示例：把指标发到你的监控接口
  navigator.sendBeacon('/api/metrics', JSON.stringify({
    name: metric.name,
    value: metric.value,
    rating: metric.rating, // good / needs-improvement / poor
  }));
}

onLCP(report);
onINP(report);
onCLS(report);
```

```javascript
// 不引库的原生写法：监听 LCP 元素变化
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log('LCP candidate:', entry.startTime, entry.element);
  }
}).observe({ type: 'largest-contentful-paint', buffered: true });
```

## 定位与优化思路

| 指标差 | 先看什么 | 常见手段 |
| --- | --- | --- |
| LCP | 首屏最大图/文本是否被阻塞 | 压缩图片、preload 关键资源、内联关键 CSS、减少长任务 |
| INP | 主线程长任务、事件处理函数 | 拆分长任务、减少渲染阻塞、节流高频事件 |
| CLS | 无尺寸图片、动态插入内容 | 给图片/广告预留尺寸、字体 `size-adjust`、动画用 transform |

## 常见误区

| 误区 | 真相 |
| --- | --- |
| 只看 Lighthouse 分数 | 实验室结果不能代表真实用户，必须配合 RUM |
| INP 就是 FID | FID 只看首次输入，INP 看整个会话的最差交互 |
| CLS 只跟图片有关 | 字体加载、iframe、动态内容都会造成布局偏移 |
| 指标达标就完事 | 指标是结果，还要监控"指标变差"的版本回归 |

## 小结

先立指标，再谈优化。接入 web-vitals 采集真实数据，配合 Lighthouse 做开发期回归，
优化动作按"LCP → INP → CLS"优先级推进，最后用线上数据验证效果。
