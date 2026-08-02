---
order: 75
title: 撤销日志
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL InnoDB撤销日志undo log：版本链、回滚段、MVCC支持与Purge机制'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/二进制日志
  - mysql/重做日志
  - mysql/日志系统
  - mysql/逻辑备份
prerequisites:
  - mysql/语法速查
---

## 1. undo log 概述

撤销日志（Undo Log）记录数据修改前的旧值，用于事务回滚和 MVCC 快照读。

### 1.1 两大功能

| 功能     | 说明                    |
| -------- | ----------------------- |
| 事务回滚 | ROLLBACK 时恢复原始数据 |
| MVCC     | 提供历史版本供快照读    |

## 2. 版本链

```
当前行：{data='Alice', trx_id=300, roll_ptr → undo_2}
                                           ↓
undo_2：{data='Bob', trx_id=200, roll_ptr → undo_1}
                                           ↓
undo_1：{data='Charlie', trx_id=100, roll_ptr → NULL}
```

```sql
-- INSERT：生成 INSERT undo log（事务提交后可立即清理）
-- UPDATE：生成 UPDATE undo log（需要保留给 MVCC）
-- DELETE：生成 DELETE undo log（标记删除，需要保留给 MVCC）
```

## 3. 回滚段

```sql
-- InnoDB 使用回滚段（Rollback Segment）管理 undo log
-- 每个回滚段包含 1024 个 undo slot

-- MySQL 8.0 默认 128 个回滚段
SET GLOBAL innodb_rollback_segments = 128;

-- undo log 表空间
-- MySQL 8.0 默认使用独立 undo 表空间
SET GLOBAL innodb_undo_tablespaces = 2;
SET GLOBAL innodb_max_undo_log_size = 1073741824;  -- 1GB
```

## 4. Purge 机制

```
Purge 线程负责清理不再需要的 undo log：
1. 检查 undo log 是否对所有活跃事务都不可见
2. 如果是，可以安全清理
3. 同时清理标记为删除的行

长事务会阻止 Purge，导致 undo log 膨胀
```

```sql
-- 查看 undo log 状态
SHOW ENGINE INNODB STATUS;

-- 查看历史版本长度
SELECT COUNT(*) FROM information_schema.innodb_trx;
-- 如果 History list length 持续增长，说明 Purge 跟不上
```

## 5. 性能调优

```sql
-- 加速 Purge
SET GLOBAL innodb_purge_batch_size = 300;  -- 每次 Purge 批量大小

-- 独立 undo 表空间（在线收缩）
SET GLOBAL innodb_undo_log_truncate = ON;
SET GLOBAL innodb_max_undo_log_size = 1073741824;
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
