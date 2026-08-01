---
order: 81
title: GTID
module: mysql
category: MySQL
difficulty: advanced
description: MySQL全局事务标识符GTID：原理、配置、基于GTID的复制与故障切换
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/主从复制
  - mysql/进阶查询与多表操作
  - mysql/并行复制
  - mysql/组复制
prerequisites:
  - mysql/语法速查
---

# GTID 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. GTID 概述

全局事务标识符（Global Transaction Identifier，GTID）为每个事务分配唯一标识，简化复制管理。

### 1.1 GTID 格式

$$
\text{GTID} = \text{server\_uuid}:\text{transaction\_id}
$$

```
3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
```

## 2. 配置

```ini
[mysqld]
gtid-mode = ON
enforce-gtid-consistency = ON
log-bin = mysql-bin
binlog-format = ROW
server-id = 1
```

## 3. 基于GTID的复制

```sql
-- 从库配置（无需指定 binlog 位置）
CHANGE MASTER TO
    MASTER_HOST = 'master-ip',
    MASTER_USER = 'repl',
    MASTER_PASSWORD = 'password',
    MASTER_AUTO_POSITION = 1;  -- 使用 GTID 自动定位

START SLAVE;
```

## 4. GTID 运维

```sql
-- 查看已执行的 GTID
SHOW MASTER STATUS;
-- Executed_Gtid_Set: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100

-- 查看从库已执行的 GTID
SHOW SLAVE STATUS\G
-- Retrieved_Gtid_Set: ...
-- Executed_Gtid_Set: ...

-- 跳过有问题的 GTID 事务
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN;
COMMIT;
SET GTID_NEXT = AUTOMATIC;
START SLAVE;
```

## 5. GTID 优势

- 无需手动定位 binlog 位置
- 故障切换更简单
- 可验证主从数据一致性
- 支持多源复制
## GTID 概念与格式

**基本写法：标准 GTID 格式**
`<server_uuid>:<事务序号>`

```sql
-- 标准 GTID 格式示例
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
-- 表示该 UUID 的事务 1 到 5

-- 8.4 Tagged GTID 格式（带标签）
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5:delete_logs
```

**基本写法：查看服务器 UUID**
`SHOW VARIABLES LIKE 'server_uuid';`

```sql
-- 查看当前服务器 UUID
SHOW VARIABLES LIKE 'server_uuid';
```

---

## GTID 开启与配置

**基本写法：查看 GTID 状态**
`SHOW VARIABLES LIKE 'gtid_mode';`

```sql
-- 查看 GTID 是否启用
SHOW VARIABLES LIKE 'gtid_mode';
SHOW VARIABLES LIKE 'enforce_gtid_consistency';
```

**基本写法：在线开启 GTID（分步）**
`SET GLOBAL enforce_gtid_consistency = WARN;`

```sql
-- 第一步：开启一致性警告，观察业务无警告后继续
SET GLOBAL enforce_gtid_consistency = WARN;
-- 第二步：开启一致性强制
SET GLOBAL enforce_gtid_consistency = ON;
-- 第三步：GTID 模式 OFF_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = OFF_PERMISSIVE;
-- 第四步：ON_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = ON_PERMISSIVE;
-- 等待所有匿名事务消费完毕
SHOW STATUS LIKE 'Ongoing_anonymous_transaction_count';
-- 第五步：正式开启
SET GLOBAL gtid_mode = ON;
```

**基本写法：配置文件持久开启**
`gtid_mode = ON`

```ini
# my.cnf 持久配置
[mysqld]
gtid_mode = ON
enforce_gtid_consistency = ON
log_slave_updates = ON        # 8.0.10+ 默认 ON，副本需记录更新到 binlog
log_bin = mysql-bin
```

---

## GTID 查询

**基本写法：查看已执行 GTID**
`SELECT @@GLOBAL.gtid_executed;`

```sql
-- 查看当前服务器已执行的 GTID 集合
SELECT @@GLOBAL.gtid_executed;
-- 示例输出: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100
```

**基本写法：查看已清除 GTID**
`SELECT @@GLOBAL.gtid_purged;`

```sql
-- 查看已被清除（不可用）的 GTID 集合
SELECT @@GLOBAL.gtid_purged;
```

**基本写法：查看 GTID 执行状态**
`SHOW MASTER STATUS;`

```sql
-- 查看当前二进制日志位置与已执行 GTID（8.4 用 SHOW BINARY LOG STATUS）
SHOW BINARY LOG STATUS\G
-- 输出包含 Executed_Gtid_Set 字段
```

**基本写法：performance_schema 查询 GTID**
`SELECT * FROM performance_schema.replication_connection_status;`

```sql
-- 查看复制连接接收到的 GTID
SELECT thread_id, service_state, received_transaction_set
FROM performance_schema.replication_connection_status;
```

---

## GTID 复制配置

**基本写法：基于 GTID 建立复制**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_AUTO_POSITION = 1;`

```sql
-- GTID 自动定位复制（无需指定日志文件和位置）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_AUTO_POSITION = 1,
  GET_SOURCE_PUBLIC_KEY = 1;
START REPLICA;
```

**基本写法：跳过指定 GTID 事务**
`SET GTID_NEXT = '<GTID>';`

```sql
-- 跳过单个 GTID 事务（解决复制错误）
STOP REPLICA;
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN; COMMIT;
SET GTID_NEXT = AUTOMATIC;
START REPLICA;
```

**基本写法：设置已清除 GTID（空库初始化）**
`SET GLOBAL gtid_purged = '<GTID集合>';`

```sql
-- 从备份恢复空库时设置已清除的 GTID
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100';
```

---

## 8.4 Tagged GTID

**基本写法：为事务打标签**
`SET TRANSACTION GTID_TAG = '<标签名>';`

```sql
-- MySQL 8.4 新特性：为事务分配标签（最多 33 字符）
-- 需 TRANSACTION_GTID_TAG 权限
SET TRANSACTION GTID_TAG = 'delete_logs';
DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：会话级设置标签**
`SET SESSION gtid_next_tag = '<标签名>';`

```sql
-- 当前会话所有事务都打上标签
SET SESSION gtid_next_tag = 'batch_import';
INSERT INTO sales VALUES (...);
```

**基本写法：跳过指定标签的事务**
`SET GLOBAL gtid_purged = '<UUID>:<区间>:<标签>';`

```sql
-- 副本端跳过带标签的事务（8.4 新增三参数 gtid_purged）
-- 格式: SET GLOBAL gtid_purged=<group_name>, <gtid_set>, <tag>
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100:delete_logs';
```

**基本写法：查看带标签的 GTID**
`SELECT * FROM performance_schema.replication_applier_status_by_worker;`

```sql
-- 查看副本应用事务时是否包含标签信息
SELECT worker_id, last_applied_transaction, last_applied_transaction_original_seqno
FROM performance_schema.replication_applier_status_by_worker;
```

---

## GTID 复制错误处理

**基本写法：查看复制错误**
`SHOW REPLICA STATUS\G`

```sql
-- 查看复制错误信息
SHOW REPLICA STATUS\G
-- 关注 Last_Error 与 Last_SQL_Error 字段
```

**基本写法：基于 GTID 自动跳过错误**
`SET GLOBAL slave_skip_errors = '<错误码>';`

```sql
-- 不推荐：跳过指定错误码（破坏一致性）
-- 推荐：使用 GTID_NEXT 手动跳过或 sql_slave_skip_counter（仅非 GTID）
```

**基本写法：重置 GTID 执行状态**
`RESET MASTER;`

```sql
-- 清空所有 binlog 并重置 gtid_executed（危险！仅初始化时使用）
RESET MASTER;
```

---

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| MySQL 概述与数据库设计 | 001-MySQLOverviewDatabaseDesign | 本文的前置基础 |
| MySQL 环境搭建 | 002-MySQLEnvSetup | 本文的前置基础 |
| MySQL 数据类型与约束 | 003-MySQLDataTypeConstraint | 本文的并列主题 |
| SQL 数据定义与高级对象 | 004-SQLDataDefinitionAdvanced | 本文的并列主题 |
| MyISAM存储引擎 | 005-MyISAMStorageEngine | 本文的并列主题 |
| SQL 数据操作与查询 | 006-SQLDataOperationQuery | 本文的并列主题 |
| Memory存储引擎 | 007-MemoryStorageEngine | 本文的并列主题 |
| NDB-Cluster | 008-NDBCluster | 本文的并列主题 |
| 聚簇索引与二级索引 | 009-ClusteredIndexSecondaryIndex | 本文的并列主题 |
| 联合索引与最左前缀原则 | 010-CompositeIndexLeftmostPrefixPrinciple | 本文的并列主题 |
| 索引下推 | 011-IndexConditionPushdown | 本文的并列主题 |
| 全文索引 | 012-FullTextIndex | 本文的并列主题 |
| 前缀索引 | 013-PrefixIndex | 本文的并列主题 |
| 索引提示与强制索引 | 014-IndexHintForceIndex | 本文的并列主题 |
| 索引统计信息与直方图 | 015-IndexStatsHistogram | 本文的并列主题 |
| SQL 函数与高级查询 | 016-SQLFunctionAndAdvancedQuery | 本文的并列主题 |
| 索引失效场景 | 017-IndexFailureScene | 本文的并列主题 |
| EXPLAIN输出详解 | 018-EXPLAINDetailed | 本文的并列主题 |
| 慢查询日志 | 019-SlowQueryLog | 本文的并列主题 |
| 优化器追踪 | 020-OptimizerTrace | 本文的性能延伸 |
| 子查询优化 | 021-SubqueryOptimization | 本文的性能延伸 |
| 派生表优化 | 022-DerivedTableOptimization | 本文的性能延伸 |
| GROUP-BY与ORDER-BY优化 | 023-GroupByOrderByOptimization | 本文的性能延伸 |
| JOIN算法 | 024-JOINAlgorithm | 本文的并列主题 |
| 事务隔离级别底层实现 | 025-TransactionIsolationImplementation | 本文的并列主题 |
| MVCC原理 | 026-MVCCPrinciple | 本文的原理深化 |
| 多表联查详解 | 027-MultiTableJoinDetailed | 本文的并列主题 |
| 锁分类 | 028-LockClassification | 本文的并列主题 |
| 死锁检测与处理 | 029-DeadlockDetectionHandling | 本文的并列主题 |
| 分布式事务 | 030-DistributedTransaction | 本文的并列主题 |
| 二进制日志 | 031-Binlog | 本文的并列主题 |
| 重做日志 | 032-RedoLog | 本文的并列主题 |
| 撤销日志 | 033-UndoLog | 本文的并列主题 |
| 日志系统 | 034-LogSystem | 本文的并列主题 |
| 逻辑备份 | 035-LogicalBackup | 本文的并列主题 |
| 物理备份 | 036-PhysicalBackup | 本文的并列主题 |
| 基于时间点恢复 | 037-PITR | 本文的并列主题 |
| 主从复制 | 038-Replication | 本文的并列主题 |
| 进阶查询与多表操作 | 039-AdvancedQueryMultiTableOperation | 本文的并列主题 |
| GTID | 040-GTID | 本文自身 |
| 并行复制 | 041-ParallelReplication | 本文的并列主题 |
| 组复制 | 042-GroupReplication | 本文的并列主题 |
| InnoDB-Cluster | 043-InnoDBCluster | 本文的并列主题 |
| 分区表 | 044-PartitionedTable | 本文的并列主题 |
| 分库分表中间件 | 045-ShardingMiddleware | 本文的并列主题 |
| 账户与权限管理 | 046-AccountPermissionManagement | 本文的安全延伸 |
| SSL-TLS加密 | 047-SSLEncryption | 本文的安全延伸 |
| 防火墙插件 | 048-FirewallPlugin | 本文的并列主题 |
| InnoDB体系架构 | 049-InnoDBSystemArchitecture | 本文的原理深化 |
| 数据加密 | 050-DataEncryption | 本文的安全延伸 |
| MySQL 索引与执行计划 | 051-MySQLIndexExecutionPlan | 本文的并列主题 |
| MySQL9新特性与并行查询 | 052-MySQL9NewFeaturesParallelQuery | 本文的并列主题 |
| VECTOR向量类型 | 053-VectorType | 本文的并列主题 |
| JSON模式验证与聚合函数 | 054-JSONSchemaValidationAggregate | 本文的并列主题 |
| 复制与高可用 | 055-ReplicationHA | 本文的并列主题 |
| 不可见索引 | 056-InvisibleIndex | 本文的并列主题 |
| 性能调优与安全 | 057-PerformanceTuningSecurity | 本文的性能延伸 |
| 函数索引 | 058-FunctionalIndex | 本文的并列主题 |
| 存储过程与函数 | 059-StoredProcedureAndFunction | 本文的并列主题 |
| MVCC快照读与当前读 | 060-MVCCSnapshotCurrentRead | 本文的并列主题 |
| 索引原理与性能优化 | 061-IndexPrinciplePerformanceOptimization | 本文的性能延伸 |
| 触发器与事件 | 062-TriggerEvent | 本文的并列主题 |
| Redo与Undo与Binlog写入时机 | 063-RedoUndoBinlogWriteTiming | 本文的并列主题 |
| 两阶段提交 | 064-TwoPhaseCommit | 本文的并列主题 |
| 间隙锁与临键锁解决幻读 | 065-GapLockNextKeyLockSolutionPhantomRead | 本文的并列主题 |
| 主从复制延迟原因与解决 | 066-ReplicationDelayCauseSolution | 本文的并列主题 |
| 分库分表策略 | 067-ShardingStrategy | 本文的并列主题 |
| JSON类型与JSON-TABLE | 068-JSONTypeJSONTable | 本文的并列主题 |
| 事务与锁机制 | 069-TransactionLockMechanism | 本文的原理深化 |
| MySQL 配置与运维 | 070-MySQLConfigOps | 本文的并列主题 |
| MySQL 快速查阅 | 071-MySQLQuickLookup | 本文的并列主题 |
| MySQL 控制器与应用 | 072-MySQLControlApplication | 本文的并列主题 |
| SQL 注入基础与检测 | 073-SQLInjectionBasicsDetection | 本文的前置基础 |
| SQL 注入攻击类型与实战 | 074-SQLInjectionAttackTypePractice | 本文的综合应用 |
| SQL 注入防御策略 | 075-SQLInjectionDefenseStrategy | 本文的并列主题 |
| MySQL 项目示例：电商数据库设计 | 076-MySQLProjectExampleDatabaseDesign | 本文的综合应用 |
| MySQL 理论知识点 | 077-MySQLTheoryKnowledge | 本文的并列主题 |
| MySQL DDL 数据定义 | 078-DDL | 本文的并列主题 |
| MySQL DML 数据操作 | 079-DML | 本文的并列主题 |
| MySQL DQL 查询速查 | 080-DQL | 本文的并列主题 |
| MySQL 索引管理 | 081-IndexManagement | 本文的并列主题 |
| MySQL 用户与权限管理 | 082-UserPermission | 本文的安全延伸 |
| MySQL CLI 命令 | 083-CLI | 本文的并列主题 |
| mysqladmin 管理命令 语法速查手册 | 084-Mysqladmin | 本文的并列主题 |
| 视图 语法速查手册 | 085-View | 本文的并列主题 |
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文的并列主题 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
