---
order: 58
title: 索引提示与强制索引
module: mysql
category: MySQL
difficulty: intermediate
description: 'MySQL索引提示：USE INDEX、FORCE INDEX、IGNORE INDEX的语法、场景与注意事项'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/全文索引
  - mysql/前缀索引
  - mysql/索引统计信息与直方图
  - mysql/SQL函数与高级查询
prerequisites:
  - mysql/语法速查
---

## 1. 索引提示概述

MySQL 提供索引提示（Index Hints）来影响优化器的索引选择。

## 2. 三种索引提示

### 2.1 USE INDEX

```sql
-- 建议优化器使用指定索引（优化器可能忽略）
SELECT * FROM employees USE INDEX (idx_dept) WHERE dept_id = 5;

-- 建议多个索引
SELECT * FROM employees USE INDEX (idx_dept, idx_name)
WHERE dept_id = 5 AND name = 'Alice';
```

### 2.2 FORCE INDEX

```sql
-- 强制使用指定索引（优化器必须使用）
SELECT * FROM employees FORCE INDEX (idx_dept) WHERE dept_id = 5;

-- 强制主键索引
SELECT * FROM employees FORCE INDEX (PRIMARY) WHERE id > 100;
```

### 2.3 IGNORE INDEX

```sql
-- 忽略指定索引
SELECT * FROM employees IGNORE INDEX (idx_dept) WHERE dept_id = 5;
-- 优化器不会考虑 idx_dept
```

## 3. 索引提示的作用范围

```sql
-- FOR JOIN：仅影响 JOIN 查找
SELECT * FROM employees e USE INDEX FOR JOIN (idx_dept)
JOIN departments d ON e.dept_id = d.id;

-- FOR ORDER BY：仅影响排序
SELECT * FROM employees USE INDEX FOR ORDER BY (idx_salary)
ORDER BY salary DESC;

-- FOR GROUP BY：仅影响分组
SELECT dept_id, COUNT(*) USE INDEX FOR GROUP BY (idx_dept)
FROM employees GROUP BY dept_id;
```

## 4. 使用场景

```sql
-- 场景1：优化器选择了错误的索引
-- 数据分布变化导致统计信息不准确
SELECT * FROM orders FORCE INDEX (idx_created_at)
WHERE created_at > '2026-01-01';

-- 场景2：避免全表扫描
SELECT * FROM large_table FORCE INDEX (idx_status)
WHERE status = 'rare_value';

-- 场景3：调试和性能对比
-- 对比不同索引的性能
SELECT * FROM t USE INDEX (idx_a) WHERE a = 1;
SELECT * FROM t USE INDEX (idx_b) WHERE a = 1;
```

## 5. 注意事项

```sql
-- 索引提示是临时方案，应优先解决根本问题
-- 1. 更新统计信息：ANALYZE TABLE
-- 2. 优化查询语句
-- 3. 调整索引设计

-- 索引提示在表结构变更后可能失效
-- 定期审查使用索引提示的查询
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
