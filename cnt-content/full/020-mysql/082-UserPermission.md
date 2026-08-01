---
order: 820
title: MySQL 用户与权限管理
module: mysql

category: '020-mysql'
difficulty: beginner
description: MySQL 用户与权限管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 用户管理

**单行写法：创建用户**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED BY '<密码>';`
```sql
-- 创建本地用户
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'StrongPass123!';
```

**单行写法：创建远程用户**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>';`
```sql
-- 允许从任意主机连接
CREATE USER 'appuser'@'%' IDENTIFIED BY 'StrongPass123!';
```

**换行写法：指定认证插件（8.0+ 默认）**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED WITH caching_sha2_password BY '<密码>';`
```sql
-- 使用默认 caching_sha2_password 认证插件
CREATE USER 'secure_user'@'%' IDENTIFIED WITH caching_sha2_password BY 'StrongPass123!';
```

**换行写法：使用 mysql_native_password 认证**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED WITH mysql_native_password BY '<密码>';`
```sql
-- 兼容旧客户端的认证方式
CREATE USER 'legacy_user'@'%' IDENTIFIED WITH mysql_native_password BY 'StrongPass123!';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>';`
```sql
-- 修改用户密码
ALTER USER 'appuser'@'localhost' IDENTIFIED BY 'NewPass456!';
```

**单行写法：修改当前用户密码**
`ALTER USER USER() IDENTIFIED BY '<新密码>';`
```sql
-- 修改当前登录用户密码
ALTER USER USER() IDENTIFIED BY 'NewPass456!';
```

**单行写法：锁定用户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK;`
```sql
-- 锁定用户禁止登录
ALTER USER 'appuser'@'localhost' ACCOUNT LOCK;
```

**单行写法：解锁用户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK;`
```sql
-- 解锁用户
ALTER USER 'appuser'@'localhost' ACCOUNT UNLOCK;
```

**单行写法：设置密码过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE;`
```sql
-- 强制用户下次登录修改密码
ALTER USER 'appuser'@'localhost' PASSWORD EXPIRE;
```

**单行写法：删除用户**
`DROP USER [IF EXISTS] '<用户名>'@'<主机>';`
```sql
-- 删除用户
DROP USER IF EXISTS 'appuser'@'localhost';
```

**单行写法：重命名用户**
`RENAME USER '<旧名>'@'<主机>' TO '<新名>'@'<主机>';`
```sql
-- 重命名用户
RENAME USER 'appuser'@'localhost' TO 'webapp'@'localhost';
```

---

## 查看用户

**单行写法：查看所有用户**
`SELECT User, Host FROM mysql.user;`
```sql
-- 列出所有用户
SELECT User, Host FROM mysql.user;
```

**单行写法：查看当前用户**
`SELECT CURRENT_USER();`
```sql
-- 查看当前登录用户
SELECT CURRENT_USER();
```

**换行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>';`
```sql
-- 查看指定用户权限
SHOW GRANTS FOR 'appuser'@'localhost';
```

**单行写法：查看当前用户权限**
`SHOW GRANTS;`
```sql
-- 查看当前登录用户权限
SHOW GRANTS;
```

---

## 权限授予与回收

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予某库所有表的所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';
```

**单行写法：授予指定权限**
`GRANT SELECT, INSERT, UPDATE ON <库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予增删改查权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.users TO 'appuser'@'localhost';
```

**单行写法：授予全局权限**
`GRANT <权限> ON *.* TO '<用户名>'@'<主机>';`
```sql
-- 授予全局 CREATE 权限
GRANT CREATE ON *.* TO 'appuser'@'localhost';
```

**单行写法：授予并允许授权**
`GRANT <权限> ON <库>.<表> TO '<用户>'@'<主机>' WITH GRANT OPTION;`
```sql
-- 授予权限并允许该用户授权给他人
GRANT SELECT ON mydb.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

**单行写法：回收权限**
`REVOKE <权限> ON <库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 回收删除权限
REVOKE DELETE ON mydb.users FROM 'appuser'@'localhost';
```

**单行写法：回收所有权限**
`REVOKE ALL PRIVILEGES ON <库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 回收某库所有权限
REVOKE ALL PRIVILEGES ON mydb.* FROM 'appuser'@'localhost';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES;`
```sql
-- 直接修改 user 表后刷新权限
FLUSH PRIVILEGES;
```

---

## 常用权限列表

**单行写法：授予 DML 权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予数据操作权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'appuser'@'%';
```

**单行写法：授予 DDL 权限**
`GRANT CREATE, ALTER, DROP, INDEX ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予数据定义权限
GRANT CREATE, ALTER, DROP, INDEX ON mydb.* TO 'devuser'@'%';
```

**单行写法：授予只读权限**
`GRANT SELECT ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予只读权限
GRANT SELECT ON mydb.* TO 'readonly'@'%';
```

**单行写法：授予备份权限**
`GRANT SELECT, LOCK TABLES, RELOAD, REPLICATION CLIENT ON *.* TO '<用户>'@'<主机>';`
```sql
-- 授予 mysqldump 所需权限
GRANT SELECT, LOCK TABLES, RELOAD, REPLICATION CLIENT ON *.* TO 'backup'@'localhost';
```

---

## 角色管理（8.0+）

**单行写法：创建角色**
`CREATE ROLE '<角色名>';`
```sql
-- 创建角色
CREATE ROLE 'app_read';
```

**单行写法：给角色授权**
`GRANT SELECT ON <库>.* TO '<角色名>';`
```sql
-- 给角色授予只读权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：将角色授予用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 把角色分配给用户
GRANT 'app_read' TO 'appuser'@'localhost';
```

**单行写法：设置默认角色**
`SET DEFAULT ROLE '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 设置用户登录后默认激活的角色
SET DEFAULT ROLE 'app_read' TO 'appuser'@'localhost';
```

**单行写法：激活当前角色**
`SET ROLE '<角色名>';`
```sql
-- 当前会话激活指定角色
SET ROLE 'app_read';
```

**单行写法：查看当前角色**
`SELECT CURRENT_ROLE();`
```sql
-- 查看当前激活的角色
SELECT CURRENT_ROLE();
```

**单行写法：回收角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>';`
```sql
-- 从用户回收角色
REVOKE 'app_read' FROM 'appuser'@'localhost';
```

**单行写法：删除角色**
`DROP ROLE [IF EXISTS] '<角色名>';`
```sql
-- 删除角色
DROP ROLE IF EXISTS 'app_read';
```

---

## 密码策略

**单行写法：查看密码策略**
`SHOW VARIABLES LIKE 'validate_password%';`
```sql
-- 查看密码验证插件配置
SHOW VARIABLES LIKE 'validate_password%';
```

**单行写法：设置密码长度**
`SET GLOBAL validate_password.length = <数值>;`
```sql
-- 设置最小密码长度
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置密码复杂度**
`SET GLOBAL validate_password.policy = <级别>;`
```sql
-- 设置密码策略为中等
SET GLOBAL validate_password.policy = 'MEDIUM';
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
| MySQL 用户与权限管理 | 082-UserPermission | 本文自身 |
| MySQL CLI 命令 | 083-CLI | 本文的并列主题 |
| mysqladmin 管理命令 语法速查手册 | 084-Mysqladmin | 本文的并列主题 |
| 视图 语法速查手册 | 085-View | 本文的并列主题 |
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文的并列主题 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
