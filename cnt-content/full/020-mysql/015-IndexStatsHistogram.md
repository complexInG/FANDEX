---
order: 59
title: 索引统计信息与直方图
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL索引统计信息与直方图：ANALYZE TABLE、统计信息存储、直方图类型与优化器利用'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/前缀索引
  - mysql/索引提示与强制索引
  - mysql/SQL函数与高级查询
  - mysql/索引失效场景
prerequisites:
  - mysql/语法速查
---

## 1. 索引统计信息

### 1.1 统计信息内容

InnoDB 通过随机采样估算索引的基数（Cardinality）：

```sql
-- 查看索引统计信息
SHOW INDEX FROM employees;

-- 关键字段：
-- Cardinality：索引中不同值的估算数量
-- Sub_part：前缀索引长度
-- Null：是否允许 NULL
```

### 1.2 ANALYZE TABLE

```sql
-- 手动更新统计信息
ANALYZE TABLE employees;

-- 查看统计信息更新时间
SELECT table_name, last_update
FROM mysql.innodb_table_stats
WHERE database_name = 'mydb';

-- 控制采样页数
SET GLOBAL innodb_stats_persistent_sample_pages = 20;  -- 默认20
SET GLOBAL innodb_stats_transient_sample_pages = 8;     -- 非持久化统计
```

### 1.3 持久化统计信息

```sql
-- 默认开启持久化统计信息
SET GLOBAL innodb_stats_persistent = ON;

-- 统计信息存储在 mysql.innodb_table_stats 和 mysql.innodb_index_stats
SELECT * FROM mysql.innodb_table_stats WHERE table_name = 'employees';
SELECT * FROM mysql.innodb_index_stats WHERE table_name = 'employees';
```

## 2. 直方图统计

### 2.1 概述

MySQL 8.0 引入直方图（Histogram）统计，提供列值分布的详细信息，帮助优化器做出更好的执行计划选择。

### 2.2 直方图类型

| 类型        | 适用场景 | 说明                     |
| ----------- | -------- | ------------------------ |
| Singleton   | 低基数列 | 每个值一个桶             |
| Equi-Height | 高基数列 | 等高直方图，每桶行数相近 |

### 2.3 创建直方图

```sql
-- 创建直方图
ANALYZE TABLE employees UPDATE HISTOGRAM ON salary WITH 100 BUCKETS;
ANALYZE TABLE employees UPDATE HISTOGRAM ON dept_id, status WITH 50 BUCKETS;

-- 查看直方图
SELECT * FROM information_schema.column_statistics
WHERE table_name = 'employees';

-- 删除直方图
ANALYZE TABLE employees DROP HISTOGRAM ON salary;
```

### 2.4 直方图的作用

```sql
-- 直方图帮助优化器估算 WHERE 条件的选择性
-- 例如：salary > 100000 的比例
-- 无直方图：优化器只能基于索引统计估算
-- 有直方图：优化器可以精确知道分布

-- 对没有索引的列特别有用
-- WHERE status = 'rare_value'
-- 直方图告诉优化器这个值很少，选择索引扫描而非全表扫描
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
