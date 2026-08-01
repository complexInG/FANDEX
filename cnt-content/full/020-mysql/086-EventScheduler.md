---
order: 860
title: 事件调度器 语法速查手册
module: 020-mysql
category: '020-mysql'
difficulty: beginner
description: 事件调度器 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 事件调度器 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 调度器开关

**基本写法：查看事件调度器状态**
`SHOW VARIABLES LIKE 'event_scheduler';`

```sql
-- 查看事件调度器是否开启
SHOW VARIABLES LIKE 'event_scheduler';
-- 输出: event_scheduler | ON / OFF
```

**基本写法：开启事件调度器**
`SET GLOBAL event_scheduler = ON;`

```sql
-- 全局开启事件调度器（运行时生效，重启失效）
SET GLOBAL event_scheduler = ON;
```

**基本写法：配置文件持久开启**
`event_scheduler = ON`

```ini
# my.cnf 中配置，重启后持久生效
[mysqld]
event_scheduler = ON
```

---

## 创建事件

**基本写法：一次性事件**
`CREATE EVENT <事件名> ON SCHEDULE AT <时间点> DO <SQL 语句>;`

```sql
-- 在指定时间执行一次
CREATE EVENT e_clean_logs
ON SCHEDULE AT '2024-12-31 23:59:59'
DO DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：当前时间延迟执行**
`CREATE EVENT <事件名> ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL <数值> <单位> DO <SQL>;`

```sql
-- 1 小时后执行一次
CREATE EVENT e_notify
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
DO UPDATE users SET notified = 1 WHERE last_login < NOW() - INTERVAL 7 DAY;
```

**基本写法：周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <数值> <单位> DO <SQL 语句>;`

```sql
-- 每天执行一次清理
CREATE EVENT e_daily_clean
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：指定起止时间的周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <间隔> STARTS <开始> ENDS <结束> DO <SQL>;`

```sql
-- 每小时执行，限定起止时间
CREATE EVENT e_hourly_stat
ON SCHEDULE EVERY 1 HOUR
STARTS '2024-01-01 00:00:00'
ENDS '2024-12-31 23:59:59'
DO CALL sp_calc_hourly_stats();
```

**基本写法：复合语句事件**
`CREATE EVENT <事件名> ON SCHEDULE <调度> DO BEGIN <语句1>; <语句2>; END`

```sql
-- 执行多条语句需用 BEGIN...END 包裹并重置分隔符
DELIMITER //
CREATE EVENT e_multi ON SCHEDULE EVERY 1 DAY
DO BEGIN
  DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
  UPDATE stats SET count = 0 WHERE stat_date = CURDATE();
END //
DELIMITER ;
```

---

## 事件管理

**基本写法：查看事件**
`SHOW EVENTS [FROM <数据库名>] [LIKE '<模式>'];`

```sql
-- 查看当前库所有事件
SHOW EVENTS;
-- 查看指定库事件
SHOW EVENTS FROM mydb LIKE 'e_%';
```

**基本写法：查看事件定义**
`SHOW CREATE EVENT <事件名>;`

```sql
-- 查看事件创建语句
SHOW CREATE EVENT e_daily_clean\G
```

**基本写法：查看事件元数据**
`SELECT * FROM information_schema.EVENTS WHERE event_name = '<事件名>';`

```sql
-- 查询事件状态与调度信息
SELECT event_name, last_executed, status, interval_value, interval_field
FROM information_schema.EVENTS
WHERE event_schema = 'mydb';
```

---

## 修改与删除

**基本写法：禁用/启用事件**
`ALTER EVENT <事件名> {DISABLE|ENABLE};`

```sql
-- 临时禁用事件
ALTER EVENT e_daily_clean DISABLE;
-- 重新启用
ALTER EVENT e_daily_clean ENABLE;
```

**基本写法：修改事件调度**
`ALTER EVENT <事件名> ON SCHEDULE <新调度> DO <SQL>;`

```sql
-- 修改执行周期为每周一次
ALTER EVENT e_daily_clean
ON SCHEDULE EVERY 1 WEEK STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：重命名事件**
`ALTER EVENT <旧事件名> RENAME TO <新事件名>;`

```sql
-- 重命名事件
ALTER EVENT e_daily_clean RENAME TO e_weekly_clean;
```

**基本写法：删除事件**
`DROP EVENT [IF EXISTS] <事件名>;`

```sql
-- 安全删除事件
DROP EVENT IF EXISTS e_weekly_clean;
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
| GTID | 040-GTID | 本文的并列主题 |
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
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文自身 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
