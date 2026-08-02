---
order: 82
title: 并行复制
module: mysql
category: MySQL
difficulty: advanced
description: MySQL并行复制：逻辑时钟、写集并行、多线程回放与复制延迟优化
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/进阶查询与多表操作
  - mysql/全局事务标识
  - mysql/组复制
  - mysql/InnoDB集群
prerequisites:
  - mysql/语法速查
---

## 1. 并行复制概述

MySQL 从库默认单线程回放 relay log，高并发写入时容易产生延迟。并行复制允许多线程同时回放事务。

## 2. 并行复制策略

### 2.1 库级并行（MySQL 5.6）

```sql
-- 按数据库并行回放
SET GLOBAL slave_parallel_type = DATABASE;
SET GLOBAL slave_parallel_workers = 4;
-- 不同数据库的事务可以并行回放
-- 单库场景无效果
```

### 2.2 逻辑时钟（MySQL 5.7）

```sql
-- 基于组提交的并行回放
SET GLOBAL slave_parallel_type = LOGICAL_CLOCK;
SET GLOBAL slave_parallel_workers = 4;

-- 同一组提交的事务可以并行回放
-- 主库 binlog_group_commit_sync_delay 影响分组
SET GLOBAL binlog_group_commit_sync_delay = 1000;  -- 1ms延迟增加组大小
SET GLOBAL binlog_group_commit_sync_no_delay_count = 10;
```

### 2.3 写集并行（MySQL 8.0）

```sql
-- 基于写集（writeset）的更细粒度并行
SET GLOBAL transaction_write_set_extraction = XXHASH64;
SET GLOBAL binlog_transaction_dependency_tracking = WRITESET;
SET GLOBAL slave_parallel_workers = 8;

-- 不修改同一行的事务可以并行回放
-- 粒度最细，效果最好
```

## 3. 监控

```sql
-- 查看并行复制状态
SHOW SLAVE STATUS\G
-- Slave_SQL_Running_State: System lock

-- 查看工作线程状态
SELECT * FROM performance_schema.replication_applier_status_by_worker;
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
