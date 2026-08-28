---
order: 170
title: select 语句详解
module: 'go'
category: 后端技术
difficulty: advanced
description: 多路复用：default 分支、超时控制与退出广播。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'go/015-ChannelPrinciple'
  - 'go/019-ContextDetailed'
prerequisites:
  - 'go/015-ChannelPrinciple'
---

# select 语句详解

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- select 语义与随机选择
- default 非阻塞模式
- time.After 超时控制
- context.Done 退出广播
- nil channel 与死锁排查
