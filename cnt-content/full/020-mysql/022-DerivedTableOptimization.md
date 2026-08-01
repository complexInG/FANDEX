---
order: 65
title: 派生表优化
module: mysql
category: MySQL
difficulty: advanced
description: MySQL派生表优化：合并策略、物化策略、LATERAL派生表与性能调优
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/优化器追踪
  - mysql/子查询优化
  - 'mysql/GROUP-BY与ORDER-BY优化'
  - mysql/JOIN算法
prerequisites:
  - mysql/语法速查
---

## 1. 派生表概述

派生表（Derived Table）是 FROM 子句中的子查询，MySQL 8.0 对派生表有多种优化策略。

## 2. 合并策略

### 2.1 条件合并

MySQL 8.0 默认将派生表合并到外查询中，避免物化临时表：

```sql
-- 原始查询
SELECT * FROM (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) dept_avg
WHERE avg_salary > 50000;

-- 优化器合并后等价于
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;
```

### 2.2 合并条件

- 派生表没有 LIMIT
- 派生表没有 GROUP BY（合并后外查询有 GROUP BY 除外）
- 派生表没有 DISTINCT
- 派生表没有窗口函数
- 派生表没有 UNION

```sql
-- 阻止合并（需要物化）
SELECT /*+ NO_MERGE(dept_avg) */ *
FROM (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) dept_avg
WHERE avg_salary > 50000;
```

## 3. 物化策略

### 3.1 何时物化

当无法合并时，MySQL 将派生表物化为临时表：

```sql
-- 包含 LIMIT 的派生表会被物化
SELECT * FROM (
    SELECT * FROM employees ORDER BY salary DESC LIMIT 10
) top_earners;

-- 包含 DISTINCT 的派生表会被物化
SELECT * FROM (
    SELECT DISTINCT dept_id FROM employees
) unique_depts;
```

## 4. LATERAL 派生表

```sql
-- MySQL 8.0.14+ 支持 LATERAL
-- 每个部门薪资最高的3名员工
SELECT d.dept_name, top3.name, top3.salary
FROM departments d,
LATERAL (
    SELECT name, salary
    FROM employees e
    WHERE e.dept_id = d.id
    ORDER BY salary DESC
    LIMIT 3
) top3;
```

## 参考文献

MySQL 官方文档：https://dev.mysql.com/doc/
MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/
High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/
Percona 博客：https://www.percona.com/blog/

## 延伸阅读

MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 InnoDB 日志与崩溃恢复

redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。
undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。
两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。
刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。

### 13.2 执行计划与优化器

EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。
优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。
排序与分组：filesort 优化为索引序；避免临时表。
慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。
