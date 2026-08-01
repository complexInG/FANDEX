---
order: 10
title: 工程实践概述
module: 'engineering-practices'
category: 'eng-infra'
difficulty: beginner
description: 工程化思维、实践体系与工程师素养。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'engineering-practices/设计文档规范'
  - 'engineering-practices/代码审查清单'
prerequisites: []
---
## 1. 工程化思维

### 1.1 什么是工程化思维

工程化思维是将**系统性、规范性、可度量**的方法应用于软件开发全过程。

| 思维     | 说明               |
| :------- | :----------------- |
| 系统思维 | 关注整体而非局部   |
| 权衡思维 | 没有银弹，只有取舍 |
| 度量思维 | 数据驱动决策       |
| 迭代思维 | 小步快跑，持续改进 |
| 防御思维 | 假设一切可能出错   |

### 1.2 工程师素养

| 素养     | 说明               |
| :------- | :----------------- |
| 技术深度 | 至少一个领域的专家 |
| 技术广度 | 跨领域的技术视野   |
| 沟通能力 | 清晰表达技术方案   |
| 协作能力 | 团队协作完成目标   |
| 学习能力 | 持续学习新技术     |
| 工匠精神 | 追求代码和设计质量 |

## 2. 工程实践体系

### 2.1 实践维度

| 维度 | 实践                    |
| :--- | :---------------------- |
| 设计 | RFC、ADR、技术方案      |
| 编码 | 编码规范、Code Review   |
| 测试 | 单元测试、集成测试、E2E |
| 构建 | CI流水线、自动化构建    |
| 部署 | CD流水线、蓝绿部署      |
| 运维 | 监控告警、On-Call       |
| 协作 | 站会、回顾、知识分享    |

### 2.2 实践成熟度

| 级别      | 特征                 |
| :-------- | :------------------- |
| L1 初始   | 依赖个人能力，无规范 |
| L2 可重复 | 基本流程可重复       |
| L3 已定义 | 流程标准化和文档化   |
| L4 已管理 | 量化度量和控制       |
| L5 优化   | 持续改进和创新       |

## 3. 核心实践原则

| 原则       | 说明               |
| :--------- | :----------------- |
| 自动化优先 | 能自动化的不手动   |
| 文档即代码 | 文档与代码同步维护 |
| 左移       | 尽早发现问题       |
| 反馈闭环   | 快速反馈、持续改进 |
| 渐进式推进 | 小步验证、逐步推广 |

## 参考文献

Google 工程实践文档：https://google.github.io/eng-practices/
12 因素应用：https://12factor.net/zh_cn/
SemVer：https://semver.org/lang/zh-CN/
Conventional Commits：https://www.conventionalcommits.org/zh-hans/

## 延伸阅读

工程实践总览，见 039-engineering-practices 模块文档。
Git 协作规范，见 003-git 模块。
CI/CD 与 DevOps，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供工程化课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Monorepo 工程化

pnpm workspace：catalog 统一版本、隔离依赖、高效安装。
原子提交：跨包变更一次提交，版本联动。
构建缓存：turbo/nx 增量构建；依赖图驱动并行。
边界治理：包间依赖显式声明，禁止隐式引用。

### 13.2 代码评审与质量门禁

门禁矩阵：lint、格式、类型、单测、构建、覆盖率阈值。
评审自动化：机器人摘要、安全扫描、依赖检查。
人工聚焦：设计、边界、测试质量与可读性。
度量：评审周期、缺陷逃逸率、门禁通过率。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 工程实践概述 | 001-EngineeringPracticeOverview | 本文自身 |
| 设计文档规范 | 002-DesignDocumentStandard | 本文的并列主题 |
| Code-Review-Checklist | 003-CodeReviewChecklist | 本文的并列主题 |
| On-Call最佳实践 | 004-OnCallPractice | 本文的并列主题 |
| 事故复盘方法论 | 005-IncidentRetrospectiveMethodology | 本文的并列主题 |
| 技术方案评审 | 006-TechnicalReview | 本文的并列主题 |
| 知识管理 | 007-KnowledgeManagement | 本文的并列主题 |
