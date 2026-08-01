---
order: 94
title: 函数索引
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL函数索引：基于表达式的索引、虚拟列索引与函数索引优化
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/不可见索引
  - mysql/性能调优与安全
  - mysql/存储过程与函数
  - mysql/MVCC快照读与当前读
prerequisites:
  - mysql/语法速查
---

## 1. 函数索引概述

MySQL 8.0 支持函数索引（Functional Index），可以对表达式创建索引，解决索引列使用函数导致索引失效的问题。

## 2. 创建函数索引

```sql
-- 方式1：直接创建函数索引
CREATE INDEX idx_year ON orders ((YEAR(created_at)));

-- 方式2：通过虚拟列创建
ALTER TABLE orders ADD COLUMN order_year INT
    GENERATED ALWAYS AS (YEAR(created_at)) VIRTUAL;
CREATE INDEX idx_order_year ON orders(order_year);
```

## 3. 使用场景

### 3.1 日期函数索引

```sql
-- 优化：WHERE YEAR(created_at) = 2026
CREATE INDEX idx_year ON orders ((YEAR(created_at)));

SELECT * FROM orders WHERE YEAR(created_at) = 2026;
-- 现在可以使用索引
```

### 3.2 字符串函数索引

```sql
-- 优化：WHERE LOWER(email) = 'test@example.com'
CREATE INDEX idx_email_lower ON users ((LOWER(email)));

SELECT * FROM users WHERE LOWER(email) = 'test@example.com';
-- 使用索引
```

### 3.3 JSON 路径索引

```sql
-- 优化：WHERE data->>'$.status' = 'active'
CREATE INDEX idx_data_status ON orders ((CAST(data->>'$.status' AS CHAR(20))));

SELECT * FROM orders WHERE data->>'$.status' = 'active';
-- 使用索引
```

### 3.4 计算列索引

```sql
-- 优化：WHERE price * quantity > 1000
CREATE INDEX idx_total ON order_items ((price * quantity));

SELECT * FROM order_items WHERE price * quantity > 1000;
-- 使用索引
```

## 4. 限制

```sql
-- 函数索引不支持前缀索引
-- 函数索引中的表达式必须用括号包裹
-- 子查询不允许出现在函数索引中
-- 函数索引占用存储空间（虚拟列索引不占数据空间）
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
