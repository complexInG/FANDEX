---
order: 51
title: 锁机制
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL锁机制：表级锁、行级锁、advisory锁的语法、兼容性与死锁处理
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/语法速查
  - postgresql/体系架构
  - postgresql/死锁检测与处理
  - postgresql/VACUUM机制
prerequisites:
  - postgresql/概述与安装配置
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

## 参考文献

PostgreSQL 官方文档：https://www.postgresql.org/docs/
PostgreSQL 中文文档：https://www.postgresql.org/docs/current/index.html
PGXN 扩展仓库：https://pgxn.org/
PostGIS：https://postgis.net/
pgvector：https://github.com/pgvector/pgvector

## 延伸阅读

PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 PostgreSQL 课程。

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与安装配置 | 001-OverviewInstallConfig | 本文的前置基础 |
| 事务与并发控制 | 002-TransactionConcurrencyControl | 本文的并列主题 |
| 索引与查询优化 | 003-IndexQueryOptimization | 本文的性能延伸 |
| 高级SQL与扩展 | 004-AdvancedSQLExtension | 本文的并列主题 |
| 复制与高可用 | 005-ReplicationHA | 本文的并列主题 |
| 体系架构 | 006-SystemArchitecture | 本文的原理深化 |
| 锁机制 | 007-LockMechanism | 本文自身 |
| 死锁检测与处理 | 008-DeadlockDetectionHandling | 本文的并列主题 |
| VACUUM机制 | 009-VACUUMMechanism | 本文的原理深化 |
| 事务ID回卷预防 | 010-TransactionIDWraparoundPrevention | 本文的并列主题 |
| 索引类型 | 011-IndexType | 本文的并列主题 |
| 覆盖索引与部分索引 | 012-CoveringIndexPartialIndex | 本文的并列主题 |
| KNN向量索引 | 013-KNNVectorIndex | 本文的并列主题 |
| 查询优化 | 014-QueryOptimization | 本文的性能延伸 |
| 分区表 | 015-PartitionedTable | 本文的并列主题 |
| 分区裁剪与分区连接 | 016-PartitionPruningPartitionJoin | 本文的并列主题 |
| 高级SQL | 017-AdvancedSQL | 本文的并列主题 |
| MERGE语句增强 | 018-MERGEStatementEnhancement | 本文的并列主题 |
| JSON-TABLE | 019-JSONTABLE | 本文的并列主题 |
| 全文检索 | 020-FullTextSearch | 本文的并列主题 |
| 地理空间对象 | 021-GeoSpatialObject | 本文的并列主题 |
| 存储过程与函数 | 022-StoredProcedureAndFunction | 本文的并列主题 |
| 触发器与事件触发器 | 023-TriggerEventTrigger | 本文的并列主题 |
| 扩展模块 | 024-ExtensionModule | 本文的并列主题 |
| FDW外部数据包装器 | 025-FDWFDW | 本文的并列主题 |
| 流复制 | 026-StreamingReplication | 本文的并列主题 |
| 级联复制 | 027-CascadingReplication | 本文的并列主题 |
| 物理复制槽 | 028-PhysicalReplicationSlot | 本文的并列主题 |
| 逻辑解码与输出插件 | 029-LogicalDecodingOutputPlugin | 本文的并列主题 |
| 增量备份 | 030-IncrementalBackup | 本文的并列主题 |
| 订阅与发布 | 031-SubscribePublish | 本文的并列主题 |
| SSL-TLS加密连接 | 032-SSLEncryptionConnection | 本文的安全延伸 |
| 基于角色的权限管理 | 033-RoleBasedPermissionManagement | 本文的安全延伸 |
| 行级安全策略 | 034-RowLevelSecurity | 本文的安全延伸 |
| 数据加密存储 | 035-DataEncryptionStorage | 本文的安全延伸 |
| 审计日志 | 036-AuditLog | 本文的并列主题 |
| 序列与自增列 | 037-SequenceAutoIncrement | 本文的并列主题 |
| 生成列 | 038-GeneratedColumn | 本文的并列主题 |
| 可更新视图 | 039-UpdatableView | 本文的并列主题 |
| 并行查询 | 040-ParallelQuery | 本文的并列主题 |
| 逻辑复制与物理复制对比 | 041-LogicalPhysicalReplicationCompare | 本文的并列主题 |
| JSONB与JSON差异 | 042-JSONBJSONDifference | 本文的并列主题 |
| 扩展模块详解 | 043-ExtensionModuleDetailed | 本文的并列主题 |
| PostgreSQL DDL 数据定义 | 044-DDL | 本文的并列主题 |
| PostgreSQL DML 数据操作 | 045-DML | 本文的并列主题 |
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文的并列主题 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文的并列主题 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
