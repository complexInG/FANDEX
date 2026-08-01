---
order: 11
title: 设计文档规范
module: 'engineering-practices'
category: 'eng-infra'
difficulty: intermediate
description: RFC、ADR、技术方案文档的编写规范与最佳实践。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'engineering-practices/工程实践概述'
  - 'engineering-practices/代码审查清单'
  - 'engineering-practices/On-Call最佳实践'
prerequisites: []
---

## 1. RFC文档

### 1.1 RFC概述

RFC（Request for Comments）用于**提出和讨论技术方案**，在实施前获取团队反馈。

### 1.2 RFC模板

```markdown
# RFC: [标题]

## 元数据

- 作者:
- 状态: 草案 / 评审中 / 已批准 / 已拒绝
- 创建日期:
- 更新日期:

## 摘要

一段话描述本RFC的核心内容。

## 动机

为什么需要做这件事？解决什么问题？

## 详细设计

### 架构变更

### API设计

### 数据模型

### 关键算法

## 替代方案

列出考虑过的其他方案及选择理由。

## 兼容性

对现有系统的影响和迁移方案。

## 风险与缓解

| 风险 | 影响 | 缓解措施 |
| :--- | :--- | :------- |
|      |      |          |

## 时间线

里程碑和预期完成时间。

## 开放问题

待讨论的问题。
```

## 2. ADR文档

### 2.1 ADR概述

ADR（Architecture Decision Record）记录**重要的架构决策**及其上下文。

### 2.2 ADR模板

```markdown
# ADR-[编号]: [决策标题]

## 状态

[提议 | 已接受 | 已废弃 | 已替代]

## 上下文

描述促使做出此决策的背景和问题。

## 决策

我们决定采取的行动。

## 理由

为什么做出这个决策。

## 后果

### 正面

### 负面

### 风险
```

### 2.3 ADR示例

```markdown
# ADR-003: 选择PostgreSQL作为主数据库

## 状态

已接受

## 上下文

系统需要选择关系型数据库，需支持JSON查询、全文搜索和GIS。

## 决策

选择PostgreSQL而非MySQL。

## 理由

1. 原生JSON/JSONB支持更好
2. 扩展生态更丰富（PostGIS、pg_trgm）
3. 并发控制更成熟（MVCC）
4. 团队经验更丰富

## 后果

- 正面: 功能更强大，扩展性更好
- 负面: 运维经验需积累
- 风险: 部分云服务兼容性需验证
```

## 3. 技术方案文档

### 3.1 技术方案模板

```markdown
# [项目名] 技术方案

## 1. 背景与目标

### 1.1 业务背景

### 1.2 技术目标

### 1.3 非目标（明确排除的范围）

## 2. 现状分析

### 2.1 当前架构

### 2.2 存在的问题

## 3. 方案设计

### 3.1 总体架构

### 3.2 核心流程

### 3.3 数据模型

### 3.4 API设计

### 3.5 安全设计

## 4. 方案对比

| 维度   | 方案A | 方案B |
| :----- | :---- | :---- |
| 性能   |       |       |
| 成本   |       |       |
| 复杂度 |       |       |

## 5. 容量与性能

### 5.1 容量估算

### 5.2 性能目标

### 5.3 压测方案

## 6. 风险与应对

## 7. 实施计划

## 8. 监控与告警
```

## 4. 文档最佳实践

| 实践         | 说明               |
| :----------- | :----------------- |
| 与代码同仓库 | 文档和代码一起维护 |
| 自动化生成   | API文档自动生成    |
| 版本控制     | 文档变更可追溯     |
| 定期审查     | 季度审查文档时效性 |
| 简洁有效     | 只写有价值的文档   |

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
| 工程实践概述 | 001-EngineeringPracticeOverview | 本文的前置基础 |
| 设计文档规范 | 002-DesignDocumentStandard | 本文自身 |
| Code-Review-Checklist | 003-CodeReviewChecklist | 本文的并列主题 |
| On-Call最佳实践 | 004-OnCallPractice | 本文的并列主题 |
| 事故复盘方法论 | 005-IncidentRetrospectiveMethodology | 本文的并列主题 |
| 技术方案评审 | 006-TechnicalReview | 本文的并列主题 |
| 知识管理 | 007-KnowledgeManagement | 本文的并列主题 |
