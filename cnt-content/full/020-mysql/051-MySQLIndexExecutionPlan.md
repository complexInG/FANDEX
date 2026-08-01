---
order: 90
tags:
  - mysql
  - database
difficulty: intermediate
title: 'MySQL 索引与执行计划'
module: mysql
category: 'MySQL Basics'
description: 'B+Tree 索引、EXPLAIN 分析与索引优化策略。'
author: Anonymous
related:
  - mysql/InnoDB体系架构
  - mysql/数据加密
  - mysql/MySQL9新特性与并行查询
  - mysql/VECTOR向量类型
prerequisites:
  - mysql/语法速查
updated: '2026-08-01'
---

# MySQL 索引与执行计划

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 索引是什么 (What is an Index)

索引是为了加速检索而构建的数据结构。对 InnoDB 来说，常见索引是 B+Tree。
索引带来的收益：

- 加速 `WHERE` 过滤、`JOIN`、`ORDER BY`、`GROUP BY`
  索引带来的成本：
- 写入变慢（INSERT/UPDATE/DELETE 需要维护索引）
- 占用更多空间
- 设计不当会让查询优化器选错计划或无法利用索引

## 2. InnoDB 索引要点 (InnoDB Basics)

### 2.1 聚簇索引与二级索引

- 主键索引（聚簇索引）：叶子节点存放整行数据
- 二级索引：叶子节点存放“索引列 + 主键值”
  因此：
- 用二级索引命中后，可能需要回表（根据主键再查一次聚簇索引）
- 覆盖索引可以避免回表（查询列都在索引里）

## 3. 组合索引与最左前缀 (Composite Index)

假设有索引 `(a, b, c)`：

- 能有效利用：`a`、`a,b`、`a,b,c` 的前缀过滤
- 不能跳过前缀：只用 `b` 或 `c` 往往无法走该索引
  实践建议：
- 把区分度更高、过滤更强的列放在前面（但也要结合排序/分组需求）
- 频繁按 `(tenant_id, created_at)` 查询，优先建立组合索引

## 4. 什么时候索引会失效 (When Index Isn’t Used)

常见原因：

- 对索引列做函数/表达式：`WHERE DATE(created_at) = ...`
- 隐式类型转换：字符串与数字混用导致无法利用索引
- 前缀缺失：组合索引没用到最左前缀
- `LIKE '%xxx'` 前置通配符无法利用普通 B+Tree 索引
- 返回行数过多：优化器认为全表扫描更便宜

## 5. EXPLAIN 怎么看 (How to Read EXPLAIN)

常用字段（MySQL 8）：

- `type`：访问类型（从好到差大致：`const`/`ref`/`range`/`index`/`ALL`）
- `key`：实际使用的索引
- `rows`：估算扫描行数
- `Extra`：额外信息（例如 `Using index`、`Using filesort`、`Using temporary`）
  示例：

```sql
 EXPLAIN
 SELECT id, email
 from user_account
 WHERE email = 'a@b.com';
```

解读目标：

- 是否使用了期望的索引（`key`）
- 扫描行数是否可控（`rows`）
- 是否出现 `Using filesort` / `Using temporary`（可能需要优化索引或 SQL）

## 6. 建索引的实用策略 (Practical Strategy)

- 先写出典型查询，再反推索引，而不是“先建一堆索引”
- 一张表的索引数量控制在合理范围，避免写放大
- 组合索引优先覆盖高频查询路径
- 长字符串字段用前缀索引需谨慎（会影响选择性与排序能力）
- 对时间范围查询：`(tenant_id, created_at)` 常见有效

## 7. 小结 (Summary)

- 索引是“以写换读”的典型优化手段
- 组合索引与最左前缀是 MySQL 索引设计的核心
- EXPLAIN 是验证索引是否生效的第一工具

---

## 索引创建

**单行写法：创建单列普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为用户名列创建普通索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为用户名和状态列创建复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建单列唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为邮箱列创建唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

**单行写法：创建复合唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为订单 ID 和产品 ID 创建复合唯一索引
CREATE UNIQUE INDEX idx_order_product ON order_items(order_id, product_id);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>))`
```sql
-- 为长字符串邮箱列创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
```

**单行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 为文章标题和内容创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_title_content (title, content);
```

**单行写法：通过 ALTER TABLE 添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 通过 ALTER TABLE 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：通过 ALTER TABLE 添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 通过 ALTER TABLE 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX idx_phone (phone);
```

**单行写法：通过 ALTER TABLE 添加复合索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名1>, <列名2>[, ...])`
```sql
-- 通过 ALTER TABLE 添加复合索引
ALTER TABLE users ADD INDEX idx_age_gender (age, gender);
```

---

## 索引查看与删除

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>`
```sql
-- 查看表的索引信息
SHOW INDEX FROM users;
```

**单行写法：竖向显示索引**
`SHOW INDEX FROM <表名>\G`
```sql
-- 竖向显示表索引信息
SHOW INDEX FROM users\G
```

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>`
```sql
-- 删除指定索引
DROP INDEX idx_username ON users;
```

**单行写法：删除主键索引**
`ALTER TABLE <表名> DROP PRIMARY KEY`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 复合索引与最左前缀

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>, <列3>)`
```sql
-- 为状态和创建时间创建复合索引
CREATE INDEX idx_status_created ON users(status, created_at);
```

**单行写法：使用前缀列查询（能利用索引）**
`SELECT * FROM <表名> WHERE <前缀列> <操作符> <值>`
```sql
-- 使用复合索引的第一列查询能利用索引
SELECT * FROM users WHERE status = 1;
```

**单行写法：使用前缀列组合查询（能利用索引）**
`SELECT * FROM <表名> WHERE <前缀列1> <操作符> <值> AND <前缀列2> <操作符> <值>`
```sql
-- 使用复合索引的前两列查询能利用索引
SELECT * FROM users WHERE status = 1 AND created_at > '2024-01-01';
```

**单行写法：跳过前缀列查询（不能利用索引）**
`SELECT * FROM <表名> WHERE <非前缀列> <操作符> <值>`
```sql
-- 跳过第一列查询不能利用索引
SELECT * FROM users WHERE created_at > '2024-01-01';
```

---

## EXPLAIN 执行计划

**换行写法：查看 SELECT 执行计划**
`EXPLAIN <SELECT 语句>`
```sql
-- 查看查询的执行计划
EXPLAIN
SELECT id, email
FROM user_account
WHERE email = 'a@b.com';
```

**单行写法：查看 UPDATE 执行计划**
`EXPLAIN <UPDATE 语句>`
```sql
-- 查看更新语句的执行计划
EXPLAIN UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
```

---

## 覆盖索引

**单行写法：使用覆盖索引避免回表**
`SELECT <索引列> FROM <表名> WHERE <索引列> <操作符> <值>`
```sql
-- 查询列都在索引中避免回表
SELECT id, email FROM users WHERE email = 'test@example.com';
```

---

## 索引失效场景

**单行写法：函数导致索引失效**
`WHERE <函数>(<列名>) <操作符> <值>`
```sql
-- 对索引列使用函数导致索引失效
SELECT * FROM users WHERE DATE(created_at) = '2024-01-01';
```

**单行写法：改写为范围查询利用索引**
`WHERE <列名> >= '<起始>' AND <列名> < '<结束>'`
```sql
-- 改写为范围查询以利用索引
SELECT * FROM users WHERE created_at >= '2024-01-01' AND created_at < '2024-01-02';
```

**单行写法：隐式类型转换导致索引失效**
`WHERE <列名> = <不同类型值>`
```sql
-- 字符串列与数字比较导致索引失效
SELECT * FROM users WHERE phone = 13800138000;
```

**单行写法：使用正确类型利用索引**
`WHERE <列名> = '<字符串值>'`
```sql
-- 使用字符串值以利用索引
SELECT * FROM users WHERE phone = '13800138000';
```

**单行写法：LIKE 前置通配符导致索引失效**
`WHERE <列名> LIKE '%<模式>'`
```sql
-- 前置通配符导致索引失效
SELECT * FROM users WHERE username LIKE '%张';
```

**单行写法：LIKE 后置通配符利用索引**
`WHERE <列名> LIKE '<前缀>%'`
```sql
-- 后置通配符能利用索引
SELECT * FROM users WHERE username LIKE '张%';
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
| MySQL 索引与执行计划 | 051-MySQLIndexExecutionPlan | 本文自身 |
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
