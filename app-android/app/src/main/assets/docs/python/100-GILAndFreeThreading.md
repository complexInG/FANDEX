---
order: 1000
title: GIL 与自由线程
module: 'python'
category: 后端技术
difficulty: advanced
description: 全局解释器锁的来龙去脉与 free-threading 时代的并发选型。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'python/012-MultiprocessingMultithreading'
  - 'python/047-ConcurrentProgramming'
prerequisites:
  - 'python/012-MultiprocessingMultithreading'
---

# GIL 与自由线程

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- GIL 为什么存在
- CPU 密集与 IO 密集的正确姿势
- multiprocessing 与进程池
- free-threading 构建（PEP 703 方向）与现状
- 迁移建议与基准方法
