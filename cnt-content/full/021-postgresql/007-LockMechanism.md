---
order: 70
title: 锁机制
module: 'postgresql'
category: 数据库
difficulty: advanced
description: PostgreSQL锁机制：表级锁、行级锁、advisory锁的语法、兼容性与死锁处理
author: fanquanpp
updated: '2026-08-01'
related:
  - 'postgresql/006-SystemArchitecture'
  - 'postgresql/008-DeadlockDetectionHandling'
  - 'postgresql/009-VACUUMMechanism'
prerequisites:
  - 'postgresql/001-OverviewInstallConfig'
---


## 1. 表级锁

### 1.1 锁模式

| 锁模式                 | SQL 语句                | 冲突范围                                                                                                  |
| ---------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------- |
| ACCESS SHARE           | SELECT                  | ACCESS EXCLUSIVE                                                                                          |
| ROW SHARE              | SELECT FOR UPDATE/SHARE | EXCLUSIVE, ACCESS EXCLUSIVE                                                                               |
| ROW EXCLUSIVE          | UPDATE, DELETE, INSERT  | SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                                                   |
| SHARE UPDATE EXCLUSIVE | VACUUM, ALTER INDEX     | SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                           |
| SHARE                  | CREATE INDEX            | ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE                   |
| SHARE ROW EXCLUSIVE    | —                       | ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE            |
| EXCLUSIVE              | —                       | ROW SHARE, ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE |
| ACCESS EXCLUSIVE       | ALTER TABLE, DROP TABLE | 所有模式                                                                                                  |

```sql
-- 手动获取表锁
LOCK TABLE employees IN ACCESS EXCLUSIVE MODE;
```

## 2. 行级锁

### 2.1 行锁类型

| 锁类型            | 语法                         | 说明     |
| ----------------- | ---------------------------- | -------- |
| FOR UPDATE        | SELECT ... FOR UPDATE        | 排他行锁 |
| FOR NO KEY UPDATE | SELECT ... FOR NO KEY UPDATE | 弱排他锁 |
| FOR SHARE         | SELECT ... FOR SHARE         | 共享行锁 |
| FOR KEY SHARE     | SELECT ... FOR KEY SHARE     | 弱共享锁 |

### 2.2 行锁兼容性

|               | KEY SHARE | SHARE | NO KEY UPDATE | UPDATE |
| ------------- | --------- | ----- | ------------- | ------ |
| KEY SHARE     |           |       |               |        |
| SHARE         |           |       |               |        |
| NO KEY UPDATE |           |       |               |        |
| UPDATE        |           |       |               |        |

```sql
-- 行锁示例
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

## 3. Advisory 锁

```sql
-- 获取 advisory 锁
SELECT pg_advisory_lock(12345);          -- 阻塞式
SELECT pg_try_advisory_lock(12345);      -- 非阻塞式

-- 释放
SELECT pg_advisory_unlock(12345);

-- 会话级锁（连接断开自动释放）
SELECT pg_advisory_lock(1, 2);  -- 双int参数

-- 事务级锁（事务结束自动释放）
SELECT pg_advisory_xact_lock(12345);
```

## 4. 查看锁

```sql
SELECT locktype, relation::regclass, mode, pid, granted
FROM pg_locks
WHERE pid != pg_backend_pid();

-- 查看阻塞
SELECT blocked.pid, blocker.pid, blocked.query, blocker.query
FROM pg_locks blocked
JOIN pg_locks blocker ON blocked.locktype = blocker.locktype
    AND blocked.database IS NOT DISTINCT FROM blocker.database
    AND blocked.relation IS NOT DISTINCT FROM blocker.relation
    AND NOT blocked.granted AND blocker.granted
    AND blocked.pid != blocker.pid;
```

## 延伸阅读
PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 MVCC 与 vacuum 机制

行头存储 xmin（创建事务）与 xmax（删除事务）；可见性由快照比较决定。
更新 = 插入新版本 + 旧版本标记；旧版本对旧事务可见，vacuum 回收不再可见的死元组。
事务 ID 回卷：约 21 亿事务后需要冻结；autovacuum 与 vacuum freeze 防止。
监控：SELECT n_dead_tup, last_autovacuum FROM pg_stat_user_tables。

### 13.2 逻辑复制与高可用

发布（publication）定义表集，订阅（subscription）在目标端应用变更；支持过滤与列子集。
流复制：主库 WAL 发送到备库，同步/异步模式；级联复制扩展拓扑。
Patroni 使用分布式共识（etcd）选主，故障自动切换，配合虚拟 IP。
切换演练与数据校验（pg_checksums）是可用性工程必备。
