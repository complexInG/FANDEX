---
order: 90
title: defer、panic 与 recover 详解
module: 'go'
category: 后端技术
difficulty: intermediate
description: 延迟调用的执行时机、panic 传播与 recover 的正确姿势。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'go/008-GoErrorHandling'
  - 'go/003-GoBasicSyntax'
prerequisites:
  - 'go/008-GoErrorHandling'
---

# defer、panic 与 recover 详解

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- defer 执行顺序与参数求值
- defer 与返回值命名
- panic 传播机制
- recover 恢复与中间件模式
- 性能与常见误用
