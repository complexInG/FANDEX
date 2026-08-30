---
order: 710
title: Deno KV 与队列
module: 'javascript'
category: 后端技术
difficulty: advanced
description: 内置零配置数据库：强一致 KV、原子事务与消息队列。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'javascript/070-DenoStdLibNpmCompatibility'
prerequisites:
  - 'javascript/070-DenoStdLibNpmCompatibility'
---

# Deno KV 与队列

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- openKv 基本读写与 key 前缀建模
- 原子操作与乐观并发
- kv.watch 实时监听
- enqueue/listenQueue 与失败重试
- 适用边界与 Postgres 对比
