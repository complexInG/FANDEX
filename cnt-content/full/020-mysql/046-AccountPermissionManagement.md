---
order: 87
title: 账户与权限管理
module: mysql
category: MySQL
difficulty: intermediate
description: MySQL账户与权限管理：用户创建、权限授予、角色、密码策略与审计
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/分区表
  - mysql/分库分表中间件
  - 'mysql/SSL-TLS加密'
  - mysql/防火墙插件
prerequisites:
  - mysql/语法速查
---
## 1. 用户管理

```sql
-- 创建用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';

-- 修改密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';

-- 删除用户
DROP USER 'app_user'@'%';

-- 查看用户
SELECT user, host FROM mysql.user;
```

## 2. 权限管理

```sql
-- 授予权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';

-- 撤销权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';

-- 查看权限
SHOW GRANTS FOR 'app_user'@'%';
```

## 3. 角色（MySQL 8.0+）

```sql
-- 创建角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';

-- 授予角色权限
GRANT SELECT ON mydb.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';

-- 将角色分配给用户
GRANT 'app_read' TO 'reporting_user'@'%';
GRANT 'app_write' TO 'application_user'@'%';

-- 激活角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

## 4. 密码策略

```sql
-- MySQL 8.0 密码验证插件
INSTALL COMPONENT 'file://component_validate_password';
SET GLOBAL validate_password.policy = MEDIUM;
SET GLOBAL validate_password.length = 12;
SET GLOBAL validate_password.mixed_case_count = 1;
SET GLOBAL validate_password.number_count = 1;
SET GLOBAL validate_password.special_char_count = 1;

-- 密码过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

## 5. 连接安全

```sql
-- 限制最大连接数
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;

-- 限制查询数
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;

-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
```
## 用户管理

**单行写法：创建用户允许任意主机连接**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>'`
```sql
-- 创建允许任意主机连接的用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
```

**单行写法：创建用户限制来源 IP 段**
`CREATE USER '<用户名>'@'<IP 段>' IDENTIFIED BY '<密码>'`
```sql
-- 创建限制来源 IP 段的用户
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>'`
```sql
-- 修改用户密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';
```

**单行写法：删除用户**
`DROP USER '<用户名>'@'<主机>'`
```sql
-- 删除指定用户
DROP USER 'app_user'@'%';
```

**单行写法：查看所有用户**
`SELECT user, host FROM mysql.user`
```sql
-- 查看所有用户列表
SELECT user, host FROM mysql.user;
```

---

## 权限管理

**单行写法：授予查询和插入权限**
`GRANT <权限列表> ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予查询和插入权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
```

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';
```

**单行写法：撤销权限**
`REVOKE <权限列表> ON <库>.<表> FROM '<用户名>'@'<主机>'`
```sql
-- 撤销插入权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';
```

**单行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>'`
```sql
-- 查看用户权限
SHOW GRANTS FOR 'app_user'@'%';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES`
```sql
-- 刷新权限表
FLUSH PRIVILEGES;
```

---

## 角色管理

**单行写法：创建多个角色**
`CREATE ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 创建多个角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';
```

**单行写法：授予只读角色权限**
`GRANT SELECT ON <库>.<表> TO '<角色名>'`
```sql
-- 授予只读角色权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：授予读写角色权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.<表> TO '<角色名>'`
```sql
-- 授予读写角色权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
```

**单行写法：授予管理员角色权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<角色名>'`
```sql
-- 授予管理员角色权限
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';
```

**单行写法：将角色分配给用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>'`
```sql
-- 分配角色给用户
GRANT 'app_read' TO 'reporting_user'@'%';
```

**单行写法：设置用户默认角色**
`SET DEFAULT ROLE ALL TO '<用户名>'@'<主机>'`
```sql
-- 设置用户默认角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

**单行写法：撤销用户角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>'`
```sql
-- 撤销用户角色
REVOKE 'app_read' FROM 'reporting_user'@'%';
```

**单行写法：删除角色**
`DROP ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 删除多个角色
DROP ROLE 'app_read', 'app_write', 'app_admin';
```

---

## 密码策略

**单行写法：安装密码验证组件**
`INSTALL COMPONENT 'file://component_validate_password'`
```sql
-- 安装密码验证组件
INSTALL COMPONENT 'file://component_validate_password';
```

**单行写法：设置密码策略级别**
`SET GLOBAL validate_password.policy = <级别>`
```sql
-- 设置密码策略级别为 MEDIUM
SET GLOBAL validate_password.policy = MEDIUM;
```

**单行写法：设置密码最小长度**
`SET GLOBAL validate_password.length = <长度>`
```sql
-- 设置密码最小长度为 12
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置大小写字母数量**
`SET GLOBAL validate_password.mixed_case_count = <数量>`
```sql
-- 设置密码大小写字母数量为 1
SET GLOBAL validate_password.mixed_case_count = 1;
```

**单行写法：设置数字数量**
`SET GLOBAL validate_password.number_count = <数量>`
```sql
-- 设置密码数字数量为 1
SET GLOBAL validate_password.number_count = 1;
```

**单行写法：设置特殊字符数量**
`SET GLOBAL validate_password.special_char_count = <数量>`
```sql
-- 设置密码特殊字符数量为 1
SET GLOBAL validate_password.special_char_count = 1;
```

**单行写法：密码定期过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE INTERVAL <天数> DAY`
```sql
-- 设置密码 90 天过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
```

**单行写法：密码永不过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE NEVER`
```sql
-- 设置密码永不过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

---

## 连接限制

**单行写法：限制每小时最大连接数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_CONNECTIONS_PER_HOUR <数量>`
```sql
-- 限制每小时最大连接数为 100
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;
```

**单行写法：限制每小时最大查询数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_QUERIES_PER_HOUR <数量>`
```sql
-- 限制每小时最大查询数为 1000
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;
```

**单行写法：锁定账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK`
```sql
-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
```

**单行写法：解锁账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK`
```sql
-- 解锁账户
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
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
| 账户与权限管理 | 046-AccountPermissionManagement | 本文自身 |
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
