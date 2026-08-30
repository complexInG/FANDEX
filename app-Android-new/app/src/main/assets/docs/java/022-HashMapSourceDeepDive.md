---
order: 220
title: HashMap 源码详解
module: 'java'
category: 后端技术
difficulty: advanced
description: 数组+链表+红黑树：扩容、扰动与树化的源码级解析。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'java/021-CollectionFrameworkDetailed'
  - 'java/023-JavaIteratorIterable'
prerequisites:
  - 'java/021-CollectionFrameworkDetailed'
---

# HashMap 源码详解

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 核心字段与容量/负载因子
- hash 扰动与索引计算
- putVal 流程与链表树化
- resize 扩容与高低位拆分
- 1.7 与 1.8 实现差异与线程问题
