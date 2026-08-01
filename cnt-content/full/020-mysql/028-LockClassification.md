---
order: 70
title: 锁分类
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL InnoDB锁分类：全局锁、表级锁、元数据锁、意向锁、行锁、间隙锁、临键锁、插入意向锁'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/MVCC原理
  - mysql/多表联查详解
  - mysql/死锁检测与处理
  - mysql/分布式事务
prerequisites:
  - mysql/语法速查
---

## 1. 锁分类总览

```mermaid
flowchart TD
    T0["MySQL 锁"]
    T1["全局锁"]
    T2["表级锁"]
    T3["表锁（READ/WRITE）"]
    T4["元数据锁（MDL）"]
    T5["意向锁（IS/IX）"]
    T6["行级锁"]
    T7["记录锁（Record Lock）"]
    T8["间隙锁（Gap Lock）"]
    T9["临键锁（Next-Key Lock）"]
    T10["插入意向锁（Insert Intention Lock）"]
    T11["自增锁（AUTO-INC Lock）"]
    T0 --> T1
    T0 --> T2
    T5 --> T6
    T10 --> T11
```

## 2. 全局锁

```sql
-- 全局读锁（用于备份）
FLUSH TABLES WITH READ LOCK;

-- 备份
mysqldump --single-transaction mydb > backup.sql

-- 释放
UNLOCK TABLES;
```

## 3. 表级锁

### 3.1 表锁

```sql
LOCK TABLES employees READ;       -- 读锁
LOCK TABLES employees WRITE;      -- 写锁
UNLOCK TABLES;
```

### 3.2 元数据锁（MDL）

```sql
-- MDL 自动获取，防止 DDL 与 DML 冲突
-- SELECT → MDL 读锁
-- ALTER → MDL 写锁

-- 长事务阻塞 DDL
-- 事务A: BEGIN; SELECT * FROM t;  -- 持有 MDL 读锁
-- 事务B: ALTER TABLE t ADD COLUMN ...;  -- 等待 MDL 写锁
-- 事务C: SELECT * FROM t;  -- 等待事务B的 MDL 写锁！

-- 查看MDL等待
SELECT * FROM performance_schema.metadata_locks;
```

### 3.3 意向锁

```sql
-- 行级锁的前置声明，快速检测表级锁冲突
-- IS：打算加行级S锁
-- IX：打算加行级X锁

-- 兼容性：
-- IS-IS , IS-IX , IS-S , IS-X
-- IX-IX , IX-S , IX-X
```

## 4. 行级锁

### 4.1 记录锁（Record Lock）

```sql
-- 锁定索引记录
SELECT * FROM t WHERE id = 5 FOR UPDATE;
-- 锁定 id=5 的索引记录
```

### 4.2 间隙锁（Gap Lock）

```sql
-- 锁定索引记录之间的间隙
SELECT * FROM t WHERE id BETWEEN 5 AND 10 FOR UPDATE;
-- 锁定 (5, 10) 间隙，阻止插入 id=6,7,8,9

-- 间隙锁之间不冲突
-- 间隙锁与插入意向锁冲突
```

### 4.3 临键锁（Next-Key Lock）

```sql
-- 记录锁 + 间隙锁
-- InnoDB 在 REPEATABLE READ 下的默认行锁算法

-- 退化为记录锁：唯一索引等值查询且记录存在
SELECT * FROM t WHERE id = 5 FOR UPDATE;  -- id 是主键，存在
-- 只锁 id=5 行

-- 退化为间隙锁：唯一索引等值查询但记录不存在
SELECT * FROM t WHERE id = 5 FOR UPDATE;  -- id=5 不存在
-- 锁 (prev, next) 间隙
```

### 4.4 插入意向锁

```sql
-- INSERT 操作在插入前获取插入意向锁
-- 是一种特殊的间隙锁，不阻止其他插入意向锁
-- 只与间隙锁冲突

-- 多个事务向同一间隙的不同位置插入不冲突
INSERT INTO t VALUES (6, ...);  -- 事务A
INSERT INTO t VALUES (7, ...);  -- 事务B
-- 不冲突
```

## 5. 自增锁

```sql
-- AUTO-INC 锁模式
-- innodb_autoinc_lock_mode = 0：传统模式（每次INSERT加表级锁）
-- innodb_autoinc_lock_mode = 1：连续模式（批量INSERT加锁，单行轻量锁）
-- innodb_autoinc_lock_mode = 2：交叉模式（无锁，最高并发，主从不安全）

SET GLOBAL innodb_autoinc_lock_mode = 2;
```

## 6. 查看锁信息

```sql
-- MySQL 8.0+
SELECT * FROM performance_schema.data_locks;
SELECT * FROM performance_schema.data_lock_waits;

-- 查看锁等待
SELECT
    waiting.pid AS waiting_pid,
    blocking.pid AS blocking_pid,
    waiting.sql_text AS waiting_query,
    blocking.sql_text AS blocking_query
FROM performance_schema.data_lock_waits w
JOIN performance_schema.events_statements_current waiting
    ON w.THREAD_ID = waiting.THREAD_ID
JOIN performance_schema.events_statements_current blocking
    ON w.BLOCKING_THREAD_ID = blocking.THREAD_ID;
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
