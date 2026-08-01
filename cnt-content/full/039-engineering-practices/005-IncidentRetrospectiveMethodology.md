---
order: 14
title: 事故复盘方法论
module: 'engineering-practices'
category: 'eng-infra'
difficulty: intermediate
description: 'Blameless Postmortem、5-Whys根因分析与复盘报告。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'engineering-practices/代码审查清单'
  - 'engineering-practices/On-Call最佳实践'
  - 'engineering-practices/技术方案评审'
  - 'engineering-practices/知识管理'
prerequisites: []
---

## 1. Blameless Postmortem

### 1.1 核心原则

> "Blame the process, not the person." — 无责复盘

| 原则     | 说明                   |
| :------- | :--------------------- |
| 无指责   | 关注系统和流程缺陷     |
| 全透明   | 复盘文档全员可见       |
| 学习导向 | 目标是改进而非追责     |
| 行动导向 | 每个发现都要有改进行动 |

### 1.2 为什么无指责

- 指责导致**隐瞒问题**
- 大多数事故是**系统性问题**而非个人失误
- 心理安全感是高效团队的基础

## 2. 5-Whys根因分析

### 2.1 方法

连续问5次"为什么"，从表象追溯到根本原因：

```
问题: 网站响应超时
为什么? → 数据库查询慢
为什么? → 缺少索引
为什么? → 新增查询未添加索引
为什么? → 代码审查未检查索引
为什么? → 缺少数据库查询审查清单
```

### 2.2 注意事项

| 注意           | 说明                   |
| :------------- | :--------------------- |
| 不要指向个人   | "因为张三忘了"不是根因 |
| 不要停在太浅层 | 至少追问3层            |
| 不要过度深挖   | 5层通常足够            |
| 多条路径       | 可能有多个根因         |

## 3. 复盘报告

### 3.1 报告模板

```markdown
# 事故复盘: [标题]

## 基本信息

- 事故时间:
- 持续时长:
- 影响范围:
- 严重级别:
- 值班工程师:

## 时间线

| 时间  | 事件     |
| :---- | :------- |
| HH:MM | 告警触发 |
| HH:MM | 开始排查 |
| HH:MM | 确认根因 |
| HH:MM | 实施修复 |
| HH:MM | 服务恢复 |

## 影响评估

- 受影响用户数:
- 业务损失:
- 数据影响:

## 根因分析

### 直接原因

### 根本原因

(5-Whys分析)

## 改进行动

| 编号 | 行动 | 负责人 | 截止日期 | 优先级 |
| :--- | :--- | :----- | :------- | :----- |
| 1    |      |        |          | P0     |
| 2    |      |        |          | P1     |

## 经验教训

### 做得好的

### 需要改进的

### 幸运的地方
```

### 3.2 复盘会议

```
1. 主持人介绍事故概况 (5min)
2. 值班工程师讲述时间线 (10min)
3. 集体讨论根因 (15min)
4. 制定改进行动 (10min)
5. 总结经验教训 (5min)
```

## 4. 复盘文化

| 要素     | 说明                   |
| :------- | :--------------------- |
| 及时性   | 事故后48小时内完成复盘 |
| 全员参与 | 相关人员都应参加       |
| 文档公开 | 复盘报告存档可查       |
| 跟踪闭环 | 改进行动必须落实       |
| 定期回顾 | 季度回顾复盘改进效果   |

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
| 设计文档规范 | 002-DesignDocumentStandard | 本文的并列主题 |
| Code-Review-Checklist | 003-CodeReviewChecklist | 本文的并列主题 |
| On-Call最佳实践 | 004-OnCallPractice | 本文的并列主题 |
| 事故复盘方法论 | 005-IncidentRetrospectiveMethodology | 本文自身 |
| 技术方案评审 | 006-TechnicalReview | 本文的并列主题 |
| 知识管理 | 007-KnowledgeManagement | 本文的并列主题 |
