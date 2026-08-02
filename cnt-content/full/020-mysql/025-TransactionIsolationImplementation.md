---
order: 68
title: 事务隔离级别底层实现
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL InnoDB事务隔离级别底层实现：锁机制、MVCC、Read View与各隔离级别的实现细节'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'mysql/GROUP-BY与ORDER-BY优化'
  - mysql/JOIN算法
  - mysql/MVCC原理
  - mysql/多表联查详解
prerequisites:
  - mysql/语法速查
---

## 1. InnoDB 隔离级别实现概述

InnoDB 通过 MVCC + 锁机制实现不同隔离级别。

| 隔离级别        | 快照读实现                   | 当前读实现    |
| --------------- | ---------------------------- | ------------- |
| READ COMMITTED  | 每次 SELECT 新 Read View     | 行级记录锁    |
| REPEATABLE READ | 事务首次 SELECT 的 Read View | Next-Key Lock |
| SERIALIZABLE    | 所有 SELECT 加共享锁         | Next-Key Lock |

## 2. READ COMMITTED 实现

### 2.1 快照读

```sql
-- 每次 SELECT 生成新的 Read View
BEGIN;
SELECT * FROM t WHERE id = 1;  -- Read View 1
-- 其他事务修改并提交
SELECT * FROM t WHERE id = 1;  -- Read View 2（新快照，能看到已提交修改）
COMMIT;
```

### 2.2 当前读

```sql
-- 当前读使用记录锁，不加间隙锁
BEGIN;
SELECT * FROM t WHERE id > 5 FOR UPDATE;
-- 只锁定 id > 5 的已有记录
-- 其他事务可以插入 id = 6 的新行
```

## 3. REPEATABLE READ 实现

### 3.1 快照读

```sql
-- 事务首次 SELECT 生成 Read View，后续复用
BEGIN;
SELECT * FROM t WHERE id = 1;  -- 生成 Read View
-- 其他事务修改并提交
SELECT * FROM t WHERE id = 1;  -- 复用 Read View，看不到修改
COMMIT;
```

### 3.2 当前读

```sql
-- 当前读使用 Next-Key Lock（记录锁 + 间隙锁）
BEGIN;
SELECT * FROM t WHERE id > 5 FOR UPDATE;
-- 锁定 id > 5 的所有记录和间隙
-- 其他事务不能插入 id > 5 的新行
```

## 4. SERIALIZABLE 实现

```sql
-- 所有 SELECT 自动加共享锁
-- 等价于 SELECT ... LOCK IN SHARE MODE
BEGIN;
SELECT * FROM t WHERE id = 1;  -- 自动加 S 锁
-- 其他事务无法修改 id = 1
COMMIT;
```

## 5. Read View 详解

### 5.1 核心字段

```
m_ids：创建时所有活跃事务ID列表
min_trx_id：m_ids 中最小值
max_trx_id：下一个将分配的事务ID
creator_trx_id：创建者事务ID
```

### 5.2 可见性判断

```
对于版本链中 trx_id：
1. trx_id < min_trx_id → 可见（事务已提交）
2. trx_id >= max_trx_id → 不可见（Read View 后开始的事务）
3. trx_id 在 m_ids 中 → 不可见（事务未提交）
4. trx_id 不在 m_ids 中 → 可见（事务已提交）
```

## 延伸阅读
MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
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
