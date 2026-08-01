---
order: 76
title: 日志系统
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL日志系统：错误日志、通用查询日志、慢查询日志的配置、查看与运维
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/重做日志
  - mysql/撤销日志
  - mysql/逻辑备份
  - mysql/物理备份
prerequisites:
  - mysql/语法速查
---
## 1. MySQL 日志体系

| 日志类型     | 用途               | 默认状态 |
| ------------ | ------------------ | -------- |
| 错误日志     | 启动/运行/关闭错误 | 开启     |
| 通用查询日志 | 所有SQL语句        | 关闭     |
| 慢查询日志   | 慢SQL语句          | 关闭     |
| 二进制日志   | 复制与恢复         | 关闭     |
| 中继日志     | 从库复制           | 从库开启 |

## 2. 错误日志

```sql
-- 查看错误日志位置
SHOW VARIABLES LIKE 'log_error';

-- 配置
SET GLOBAL log_error = '/var/log/mysql/error.log';
SET GLOBAL log_error_verbosity = 3;  -- 1=ERROR, 2=ERROR+WARNING, 3=ERROR+WARNING+NOTE

-- 查看错误日志
-- Linux: tail -f /var/log/mysql/error.log
-- MySQL 8.0:
SHOW VARIABLES LIKE 'log_error';
```

## 3. 通用查询日志

```sql
-- 记录所有SQL语句（性能影响大，通常关闭）
SET GLOBAL general_log = ON;
SET GLOBAL general_log_file = '/var/log/mysql/general.log';

-- 查看状态
SHOW VARIABLES LIKE 'general_log%';
```

## 4. 慢查询日志

```sql
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;
SET GLOBAL log_queries_not_using_indexes = ON;
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
```

## 5. 日志管理最佳实践

```sql
-- 1. 错误日志始终开启
-- 2. 通用查询日志仅在调试时开启
-- 3. 慢查询日志生产环境建议开启
-- 4. 使用 logrotate 管理日志文件大小
-- 5. 定期分析慢查询日志
```
## 系统变量查询

**基本写法：查看所有系统变量**
`SHOW VARIABLES [LIKE '<模式>'];`

```sql
-- 查看所有变量
SHOW VARIABLES;
-- 过滤查看 innodb 相关变量
SHOW VARIABLES LIKE 'innodb%';
```

**基本写法：查看单个变量**
`SHOW VARIABLES LIKE '<变量名>';`

```sql
-- 查看最大连接数
SHOW VARIABLES LIKE 'max_connections';
-- 查看默认存储引擎
SHOW VARIABLES LIKE 'default_storage_engine';
```

**基本写法：精确匹配变量**
`SELECT @@GLOBAL.<变量名>;` / `SELECT @@SESSION.<变量名>;`

```sql
-- 查看 GLOBAL 与 SESSION 作用域变量
SELECT @@GLOBAL.max_connections;
SELECT @@SESSION.autocommit;
-- 查看仅会话级变量
SELECT @@session.sql_mode;
```

**基本写法：information_schema 查询变量**
`SELECT * FROM performance_schema.global_variables WHERE variable_name LIKE '<模式>';`

```sql
-- 通过性能 schema 查询变量
SELECT variable_name, variable_value
FROM performance_schema.global_variables
WHERE variable_name LIKE 'innodb_buffer%';
```

---

## 系统变量设置

**基本写法：设置全局变量（运行时）**
`SET GLOBAL <变量名> = <值>;`

```sql
-- 动态调整最大连接数（重启失效）
SET GLOBAL max_connections = 500;
```

**基本写法：设置会话变量**
`SET SESSION <变量名> = <值>;`

```sql
-- 仅当前会话生效
SET SESSION sql_mode = 'STRICT_TRANS_TABLES';
SET autocommit = 0;
```

**基本写法：SET PERSIST 持久化（8.0+）**
`SET PERSIST <变量名> = <值>;`

```sql
-- 持久化到 mysqld-auto.cnf，重启仍生效
SET PERSIST max_connections = 500;
SET PERSIST_ONLY innodb_buffer_pool_size = 4294967296;  -- 仅重启生效
```

**基本写法：重置变量为默认值**
`SET PERSIST <变量名> = DEFAULT;`

```sql
-- 清除持久化配置恢复默认
SET PERSIST max_connections = DEFAULT;
```

---

## 状态查询

**基本写法：查看服务器状态**
`SHOW STATUS [LIKE '<模式>'];`

```sql
-- 查看所有状态变量
SHOW STATUS;
-- 查看连接相关状态
SHOW STATUS LIKE 'Threads%';
```

**基本写法：查看会话级状态**
`SHOW SESSION STATUS LIKE '<模式>';`

```sql
-- 仅查看当前会话状态
SHOW SESSION STATUS LIKE 'Bytes%';
```

**基本写法：查看全局状态**
`SHOW GLOBAL STATUS LIKE '<模式>';`

```sql
-- 查看全局累计状态
SHOW GLOBAL STATUS LIKE 'Uptime';
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool%';
```

**基本写法：性能 schema 查询状态**
`SELECT * FROM performance_schema.global_status WHERE variable_name LIKE '<模式>';`

```sql
-- 通过性能 schema 查询状态
SELECT variable_name, variable_value
FROM performance_schema.global_status
WHERE variable_name LIKE 'Threads_%';
```

---

## 常用监控查询

**基本写法：查看当前连接数**
`SHOW STATUS LIKE 'Threads_connected';`

```sql
-- 当前活跃连接数
SHOW STATUS LIKE 'Threads_connected';
-- 历史最大连接数
SHOW STATUS LIKE 'Max_used_connections';
```

**基本写法：查看缓冲池命中率**
`SHOW STATUS LIKE 'Innodb_buffer_pool_reads';`

```sql
-- 计算缓冲池命中率（reads 为磁盘读，read_requests 为总请求）
SHOW STATUS LIKE 'Innodb_buffer_pool_read_requests';
SHOW STATUS LIKE 'Innodb_buffer_pool_reads';
-- 命中率 = 1 - reads / read_requests
```

**基本写法：查看 QPS 与 TPS**
`SHOW STATUS LIKE 'Questions';`

```sql
-- Questions 为查询总数，Uptime 为运行秒数，QPS = Questions/Uptime
SHOW STATUS LIKE 'Questions';
SHOW STATUS LIKE 'Uptime';
-- Com_开头的为各命令执行次数
SHOW STATUS LIKE 'Com_select';
SHOW STATUS LIKE 'Com_insert';
```

---

## 字符集与时区

**基本写法：查看字符集变量**
`SHOW VARIABLES LIKE 'character_set%';`

```sql
-- 查看各环节字符集
SHOW VARIABLES LIKE 'character_set%';
-- 查看排序规则
SHOW VARIABLES LIKE 'collation%';
```

**基本写法：查看时区**
`SELECT @@global.time_zone, @@session.time_zone;`

```sql
-- 查看全局与会话时区
SELECT @@global.time_zone, @@session.time_zone;
-- 查看当前时间
SELECT NOW(), UTC_TIMESTAMP();
```

**基本写法：设置时区**
`SET GLOBAL time_zone = '<时区>';`

```sql
-- 设置全局时区
SET GLOBAL time_zone = '+08:00';
SET SESSION time_zone = '+08:00';
```

---

## 查看进程与锁

**基本写法：查看进程列表**
`SHOW PROCESSLIST;`

```sql
-- 查看当前所有连接与正在执行的 SQL
SHOW PROCESSLIST;
-- 完整查看（含完整 SQL 文本）
SHOW FULL PROCESSLIST;
```

**基本写法：查看 InnoDB 锁信息**
`SELECT * FROM performance_schema.data_locks;`

```sql
-- 8.0+ 通过 performance_schema 查看锁（替代旧版 information_schema.INNODB_LOCKS）
SELECT * FROM performance_schema.data_locks;
-- 查看锁等待
SELECT * FROM performance_schema.data_lock_waits;
```

**基本写法：查看 InnoDB 事务**
`SELECT * FROM information_schema.INNODB_TRX;`

```sql
-- 查看当前活跃事务
SELECT trx_id, trx_state, trx_started, trx_mysql_thread_id
FROM information_schema.INNODB_TRX;
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
| 日志系统 | 034-LogSystem | 本文自身 |
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
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文的并列主题 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
