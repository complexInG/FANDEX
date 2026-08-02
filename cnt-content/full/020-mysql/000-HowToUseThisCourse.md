---
order: 10
title: 本课程使用指南（先读这里）
module: 'mysql'
category: 数据库
difficulty: beginner
description: 零基础学习 MySQL 的正确姿势：必读/选读/进阶分层、学习路线与预期时间。
author: fanquanpp
updated: '2026-08-03'
related:
  - 'mysql/000-Roadmap'
  - 'mysql/000-Glossary'
  - 'mysql/000-SQL-Playground'
prerequisites: []
---

## 0. 这份资料怎么用

本模块有 87 篇文档，**不要按编号顺序读完**。它分为三类：

**必读（第一周，约 3-4 小时）**

- `000-SQL-Playground`：在线沙箱，先动手跑 SQL；
- `001-MySQLOverviewDatabaseDesign` 的第 0 节：五分钟写出第一句 SQL；
- `002-MySQLEnvSetup`：装好 MySQL 环境；
- `080-DQL` 的前 5 个动作：SELECT、WHERE、ORDER BY、LIMIT、COUNT。

**选读（第二周起，按需）**

- `003-MySQLDataTypeConstraint`、`078-DDL`、`079-DML`：建表与增删改；
- `027-MultiTableJoinDetailed`、`024-JOINAlgorithm`：多表查询；
- `071-MySQLQuickLookup`：随时查阅的速查手册。

**进阶（有基础后再读）**

- 索引原理（009-015、051、061）、事务与锁（025-030、065、069）、日志与备份（031-037）、复制与高可用（038-043、055）、分库分表（045、067）、性能调优（018-023、057）。

**三条原则**

1. 先动手再理解：先在沙箱里跑通，再回来读原理；
2. 术语不认识先查 `000-Glossary`，不要卡住；
3. 每条 SQL 都要自己敲一遍，复制粘贴记不住。

## 1. 学习路线图

详细时间线见 `000-Roadmap`。一句话版：

```text
第 1 周：沙箱 + SELECT 五动作 + 环境搭建
第 2 周：建表 + 增删改 + 常用函数
第 3 周：多表查询 + 索引入门
第 4 周：事务与锁
之后：按项目需要查对应专题
```

## 2. 预期时间与验收标准

| 阶段 | 预期时间 | 验收标准 |
| --- | --- | --- |
| 第一周 | 3-4 小时 | 能在沙箱里独立写出五条基础查询 |
| 第二周 | 4-6 小时 | 能建一张带主键的表并完成增删改 |
| 第三周 | 4-6 小时 | 能解释 INNER JOIN 与 LEFT JOIN 的区别 |
| 第四周 | 3-4 小时 | 能说出事务 ACID 与常用隔离级别 |

## 3. 常见误区

| 误区 | 真相 |
| --- | --- |
| 背语法 | 语法随用随查，重点是理解“查什么、怎么查” |
| 一上来读索引原理 | 先会写查询，再学优化 |
| 跳过环境搭建 | 沙箱能跑通就过关，本地环境第二周再装也行 |
| 用 MySQL 与 SQL 标准混学 | 先掌握通用 SQL，再学 MySQL 特有语法 |

> 一句话记住：先跑通、再理解、最后优化；看不懂的术语查 `000-Glossary`。

## 扩展学习

- 路线图：`mysql/000-Roadmap`；
- 术语表：`mysql/000-Glossary`；
- 沙箱练习：`mysql/000-SQL-Playground`；
- 第一课：`mysql/001-MySQLOverviewDatabaseDesign`。
