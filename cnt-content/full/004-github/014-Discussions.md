---
order: 57
title: Discussions
module: github
category: GitHub
difficulty: beginner
description: 'GitHub Discussions详解：社区讨论、问答与公告管理。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/Projects看板
  - github/知识库
  - github/AI编程助手
  - github/依赖自动更新
prerequisites:
  - github/GitHub概述
---

## 1. Discussions 概述

### 1.1 什么是 Discussions

GitHub Discussions 是仓库的**社区论坛**，用于讨论、问答、公告和想法收集，与 Issue 互补。

### 1.2 Discussions vs Issues

| 特性               | Discussions      | Issues             |
| :----------------- | :--------------- | :----------------- |
| **用途**           | 讨论、问答、想法 | Bug 报告、功能请求 |
| **状态**           | 开放式           | 需要解决           |
| **分类**           | 分类标签         | 标签               |
| **可转换为 Issue** |                  | —                  |
| **协作**           | 社区驱动         | 维护者驱动         |

## 2. 启用 Discussions

1. 仓库 Settings → Features → Discussions → 勾选
2. 访问 `https://github.com/user/repo/discussions`

## 3. 讨论分类

### 3.1 默认分类

| 分类              | 用途     | 图标 |
| :---------------- | :------- | :--- |
| **Announcements** | 公告     |      |
| **General**       | 通用讨论 |      |
| **Ideas**         | 功能想法 |      |
| **Q&A**           | 问答     |      |
| **Show and Tell** | 展示     |      |

### 3.2 自定义分类

可以创建自定义分类，如：

- Documentation
- Architecture
- Community

## 4. 使用场景

### 4.1 问答

社区成员提问，其他成员或维护者回答。可标记最佳答案。

### 4.2 功能讨论

讨论新功能的可行性和设计方向，收集社区反馈。

### 4.3 公告

发布版本更新、重要变更等信息。

### 4.4 展示

社区成员展示使用项目的作品。

## 5. 与 Issue 的联动

### 5.1 Discussion → Issue

将讨论转化为 Issue 进行跟踪。

### 5.2 Issue → Discussion

将不适合作为 Issue 的讨论转移到 Discussions。

## 参考文献

GitHub 文档：https://docs.github.com/zh
GitHub Actions 文档：https://docs.github.com/zh/actions
GitHub REST API：https://docs.github.com/zh/rest
GitHub GraphQL API：https://docs.github.com/zh/graphql

## 延伸阅读

GitHub Actions CI/CD，见 004-github 模块 Actions 文档。
Git 协作基础，见 003-git 模块。
DevOps 自动化，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 GitHub 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 GitHub Actions 深入

事件驱动：push、pull_request、schedule、workflow_dispatch；on 支持过滤路径与分支。
上下文：github（事件数据）、env、secrets、needs（任务依赖）；表达式与函数。
安全：第三方 action 固定 SHA；权限默认最小；OIDC 换取云凭证。
缓存与性能：actions/cache、并发控制、矩阵并行。

### 13.2 开源协作治理

CONTRIBUTING 定义贡献路径；Issue 标签（good first issue）引导新手。
维护者时间管理：合并队列、自动化 triage、定期发布。
社区健康：行为准则执行、讨论区沉淀、感谢贡献。
安全披露：SECURITY.md + 私密漏洞报告流程。
