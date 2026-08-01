---
order: 80
title: 主从复制
module: mysql
category: MySQL
difficulty: advanced
description: MySQL主从复制：异步复制、半同步复制、全同步复制的原理、配置与切换
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/物理备份
  - mysql/基于时间点恢复
  - mysql/进阶查询与多表操作
  - mysql/全局事务标识
prerequisites:
  - mysql/语法速查
---
## 1. 复制概述

MySQL 复制基于 binlog，将主库的变更同步到从库。

### 1.1 复制模式

| 模式       | 主库等待            | 数据安全 | 性能 |
| ---------- | ------------------- | -------- | ---- |
| 异步复制   | 不等待从库          | 可能丢失 | 最高 |
| 半同步复制 | 等待至少1个从库确认 | 较安全   | 中等 |
| 全同步复制 | 等待所有从库确认    | 最安全   | 最低 |

## 2. 异步复制

### 2.1 原理

```
主库 → binlog → 从库 IO线程 → relay log → 从库 SQL线程 → 从库数据
```

### 2.2 配置

```ini
# 主库 my.cnf
[mysqld]
server-id = 1
log-bin = mysql-bin
binlog-format = ROW

# 从库 my.cnf
[mysqld]
server-id = 2
relay-log = relay-bin
read-only = ON
```

```sql
-- 主库创建复制用户
CREATE USER 'repl'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

-- 从库配置
CHANGE MASTER TO
    MASTER_HOST = 'master-ip',
    MASTER_USER = 'repl',
    MASTER_PASSWORD = 'password',
    MASTER_LOG_FILE = 'mysql-bin.000001',
    MASTER_LOG_POS = 154;

START SLAVE;
SHOW SLAVE STATUS\G
```

## 3. 半同步复制

```sql
-- 主库安装插件
INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
SET GLOBAL rpl_semi_sync_master_enabled = ON;
SET GLOBAL rpl_semi_sync_master_timeout = 5000;  -- 5秒超时降级为异步

-- 从库安装插件
INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';
SET GLOBAL rpl_semi_sync_slave_enabled = ON;
STOP SLAVE IO_THREAD; START SLAVE IO_THREAD;
```

## 4. 复制延迟监控

```sql
-- 查看从库延迟
SHOW SLAVE STATUS\G
-- Seconds_Behind_Master: 0

-- 使用 pt-heartbeat 更精确监控
pt-heartbeat -D test --update -h master
pt-heartbeat -D test --monitor -h slave
```
## 复制术语（8.4 SOURCE/REPLICA）

**基本写法：查看源库二进制日志状态**
`SHOW BINARY LOG STATUS;`

```sql
-- MySQL 8.4 新语法（替代旧版 SHOW MASTER STATUS）
SHOW BINARY LOG STATUS;
-- 输出: File=mysql-bin.000003, Position=1234, Binlog_Do_DB, Binlog_Ignore_DB
```

**基本写法：查看副本状态**
`SHOW REPLICA STATUS\G`

```sql
-- MySQL 8.4 新语法（替代旧版 SHOW SLAVE STATUS）
SHOW REPLICA STATUS\G
```

**基本写法：查看复制源**
`SHOW REPLICA STATUS FOR CHANNEL '<通道名>'\G`

```sql
-- 查看指定复制通道状态（多源复制）
SHOW REPLICA STATUS FOR CHANNEL 'source_1'\G
```

---

## 副本控制

**基本写法：启动复制**
`START REPLICA [FOR CHANNEL '<通道名>'];`

```sql
-- 启动所有复制线程
START REPLICA;
-- 启动指定通道
START REPLICA FOR CHANNEL 'source_1';
```

**基本写法：停止复制**
`STOP REPLICA [FOR CHANNEL '<通道名>'];`

```sql
-- 停止复制线程
STOP REPLICA;
-- 停止 IO 线程或 SQL 线程
STOP REPLICA IO_THREAD;
STOP REPLICA SQL_THREAD;
```

**基本写法：重置副本**
`RESET REPLICA [ALL] [FOR CHANNEL '<通道名>'];`

```sql
-- 清除副本元数据与中继日志（替换旧 RESET SLAVE）
RESET REPLICA;
-- 彻底删除通道（含元数据）
RESET REPLICA ALL FOR CHANNEL 'source_1';
```

**基本写法：配置复制源**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_PORT=<端口>, SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_LOG_FILE='<日志文件>', SOURCE_LOG_POS=<位置>;`

```sql
-- 配置主从复制源（8.4 新语法，替代 CHANGE MASTER TO）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_LOG_FILE='mysql-bin.000003',
  SOURCE_LOG_POS=1234,
  GET_SOURCE_PUBLIC_KEY=1;
```

---

## 二进制日志管理

**基本写法：查看二进制日志列表**
`SHOW BINARY LOGS;`

```sql
-- 查看所有 binlog 文件及大小
SHOW BINARY LOGS;
```

**基本写法：查看 binlog 事件**
`SHOW BINLOG EVENTS [IN '<日志文件>'] [FROM <位置>] [LIMIT <偏移>, <行数>];`

```sql
-- 查看指定 binlog 事件
SHOW BINLOG EVENTS IN 'mysql-bin.000003' FROM 1234 LIMIT 10;
```

**基本写法：查看 binlog 格式**
`SHOW VARIABLES LIKE 'binlog_format';`

```sql
-- 查看 binlog 格式（ROW/STATEMENT/MIXED）
SHOW VARIABLES LIKE 'binlog_format';
```

**基本写法：删除旧 binlog**
`PURGE BINARY LOGS TO '<保留文件>';`

```sql
-- 删除指定文件之前的所有 binlog
PURGE BINARY LOGS TO 'mysql-bin.000010';
```

**基本写法：按时间删除 binlog**
`PURGE BINARY LOGS BEFORE '<日期时间>';`

```sql
-- 删除指定时间之前的 binlog
PURGE BINARY LOGS BEFORE '2024-12-01 00:00:00';
```

**基本写法：自动过期配置**
`SET GLOBAL binlog_expire_logs_seconds = <秒数>;`

```sql
-- 设置 binlog 自动过期（默认 30 天）
SET GLOBAL binlog_expire_logs_seconds = 604800;  -- 7 天
```

---

## binlog 工具

**基本写法：mysqlbinlog 查看日志**
`mysqlbinlog <选项> <日志文件>`

```bash
# 查看二进制日志内容
mysqlbinlog mysql-bin.000003
# 指定时间范围
mysqlbinlog --start-datetime="2024-12-01 00:00:00" --stop-datetime="2024-12-02 00:00:00" mysql-bin.000003
```

**基本写法：mysqlbinlog 重放恢复**
`mysqlbinlog <日志文件> | mysql -u <用户名> -p <数据库名>`

```bash
# 基于位置恢复
mysqlbinlog --start-position=1234 --stop-position=5678 mysql-bin.000003 | mysql -u root -p mydb
```

**基本写法：基于 GTID 恢复**
`mysqlbinlog --exclude-gtids='<GTID集合>' <日志文件>`

```bash
# 排除指定 GTID 事务进行恢复
mysqlbinlog --exclude-gtids='3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5' mysql-bin.000003 | mysql -u root -p
```

---

## 复制过滤

**基本写法：配置复制过滤规则**
`CHANGE REPLICATION FILTER <过滤类型> = (<规则>);`

```sql
-- 仅复制指定库
CHANGE REPLICATION FILTER REPLICATE_DO_DB = (mydb);
-- 排除指定库
CHANGE REPLICATION FILTER REPLICATE_IGNORE_DB = (test, tmp);
-- 仅复制指定表
CHANGE REPLICATION FILTER REPLICATE_DO_TABLE = (mydb.users, mydb.orders);
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
| 主从复制 | 038-Replication | 本文自身 |
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
