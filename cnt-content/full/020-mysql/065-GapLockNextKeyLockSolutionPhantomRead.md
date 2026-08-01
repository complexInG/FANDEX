---
order: 103
title: 间隙锁与临键锁解决幻读
module: mysql
category: database
difficulty: advanced
description: 'MySQL InnoDB 间隙锁（Gap Lock）与临键锁（Next-Key Lock）详解：锁结构、加锁规则、幻读解决方案与死锁分析。'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/Redo与Undo与Binlog写入时机
  - mysql/两阶段提交
  - mysql/主从复制延迟原因与解决
  - mysql/分库分表策略
prerequisites:
  - mysql/语法速查
---

## 1. 幻读问题

### 1.1 什么是幻读

同一事务内，两次相同的范围查询返回了不同的行集：

```sql
-- RR 隔离级别
BEGIN;
-- 第一次查询：2行
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
-- id=2, age=25 | id=5, age=28

-- 其他事务插入了一行
-- INSERT INTO users VALUES (8, 'new', 26);

-- 第二次查询：3行 ← 幻读！
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
-- id=2, age=25 | id=5, age=28 | id=8, age=26
```

### 1.2 快照读不会幻读

RR 隔离级别下，快照读通过 MVCC 的 ReadView 机制，始终读取事务开始时的数据快照，不会出现幻读。

### 1.3 当前读的幻读

当前读读取最新数据，不加间隙锁时会出现幻读：

```sql
BEGIN;
-- 当前读
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
-- 锁定 id=2 和 id=5 两行

-- 其他事务可以插入 age=26 的新行（行间间隙未被锁定）
INSERT INTO users VALUES (8, 'new', 26);  -- 成功！

-- 再次当前读
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
-- 多了一行！幻读！
```

## 2. 间隙锁（Gap Lock）

### 2.1 间隙锁概念

间隙锁锁定**索引记录之间的间隙**，阻止其他事务在间隙中插入新记录。

```
索引 age: ... | 20 | 25 | 28 | 30 | ...

间隙: (-∞, 20), (20, 25), (25, 28), (28, 30), (30, +∞)

Gap Lock 锁定 (20, 25) → 阻止插入 age=21,22,23,24
```

### 2.2 间隙锁的特性

- **纯抑制锁**：间隙锁之间不互斥，只阻止插入
- **不锁定记录本身**：只锁定记录间的间隙
- **仅在 RR 隔离级别生效**：RC 隔离级别下间隙锁失效
- **自动释放**：事务提交或回滚后释放

```sql
-- 两个事务可以同时持有同一间隙的 Gap Lock
-- 事务A: SELECT * FROM users WHERE age = 26 FOR UPDATE;  -- Gap Lock (25, 28)
-- 事务B: SELECT * FROM users WHERE age = 27 FOR UPDATE;  -- Gap Lock (25, 28) — 不冲突！
-- 但事务A或B都无法在 (25, 28) 间隙中插入数据
```

## 3. 临键锁（Next-Key Lock）

### 3.1 临键锁概念

临键锁 = **行锁（Record Lock） + 间隙锁（Gap Lock）**，锁定一条记录及其前面的间隙。

```
Next-Key Lock = Gap Lock (前间隙) + Record Lock (记录)

索引 age: ... | 20 | 25 | 28 | 30 | ...

Next-Key Lock 锁定 (20, 25]：
  - Gap Lock: (20, 25) — 阻止插入 age=21,22,23,24
  - Record Lock: 25 — 阻止修改/删除 age=25 的行
```

### 3.2 临键锁的加锁规则

InnoDB 的加锁规则（基于 MySQL 8.0）：

**规则1**：加锁的基本单位是 Next-Key Lock

**规则2**：查找过程中访问到的对象才会加锁

**规则3**：等值查询，唯一索引，Next-Key Lock 退化为行锁

**规则4**：等值查询，向右遍历到最后一个不满足条件的值时，Next-Key Lock 退化为 Gap Lock

**规则5**：范围查询，会对扫描到的范围加 Next-Key Lock

### 3.3 加锁示例

```sql
-- 表结构
CREATE TABLE t (id INT PRIMARY KEY, c INT, KEY(c));
INSERT INTO t VALUES (5,5), (10,10), (15,15), (20,20);

-- 示例1：等值查询唯一索引
SELECT * FROM t WHERE id = 10 FOR UPDATE;
-- 加锁: 行锁 id=10（规则3：唯一索引退化为行锁）

-- 示例2：等值查询普通索引
SELECT * FROM t WHERE c = 10 FOR UPDATE;
-- 加锁: Next-Key Lock (5, 10] + Gap Lock (10, 15)
-- (5,10]: c=10 的 Next-Key Lock
-- (10,15): 规则4，向右遍历到15不满足，退化为 Gap Lock

-- 示例3：范围查询
SELECT * FROM t WHERE c >= 10 AND c < 15 FOR UPDATE;
-- 加锁: Next-Key Lock (5, 10] + Next-Key Lock (10, 15]
-- 扫描到 c=10 和 c=15

-- 示例4：无匹配的等值查询
SELECT * FROM t WHERE c = 12 FOR UPDATE;
-- 加锁: Gap Lock (10, 15)
-- 规则4：c=12不存在，向右遍历到15，退化为 Gap Lock
```

## 4. 幻读解决方案

### 4.1 当前读 + 临键锁

```sql
BEGIN;
-- 当前读加临键锁
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;

-- 加锁范围:
-- 假设索引 age 有值: 20, 25, 28, 30
-- Next-Key Lock: (20, 25], (25, 28], (28, 30]
-- Gap Lock: (30, +∞) 如果扫描到30之后

-- 其他事务无法在锁定范围内插入
INSERT INTO users VALUES (8, 'new', 26);  -- 阻塞！被 (25, 28] 阻止
INSERT INTO users VALUES (9, 'new', 22);  -- 阻塞！被 (20, 25] 阻止

-- 再次查询结果一致
SELECT * FROM users WHERE age BETWEEN 20 AND 30 FOR UPDATE;
COMMIT;
```

### 4.2 不同索引的加锁差异

```sql
-- 无索引：锁全表
SELECT * FROM users WHERE name = 'Alice' FOR UPDATE;
-- 所有行和间隙都被锁定

-- 主键索引：只锁行
SELECT * FROM users WHERE id = 5 FOR UPDATE;
-- 只锁 id=5 这一行

-- 唯一索引：锁索引行 + 主键行
SELECT * FROM users WHERE email = 'a@b.com' FOR UPDATE;
-- 唯一索引上的行锁 + 主键上的行锁

-- 普通索引：临键锁 + 主键行锁
SELECT * FROM users WHERE age = 25 FOR UPDATE;
-- age 索引: Next-Key Lock + Gap Lock
-- 主键索引: 行锁
```

## 5. 死锁场景分析

### 5.1 间隙锁导致的死锁

```sql
-- 初始数据: id=5(c=5), id=10(c=10)

-- 事务A
BEGIN;
SELECT * FROM t WHERE c = 7 FOR UPDATE;
-- Gap Lock (5, 10)

-- 事务B
BEGIN;
SELECT * FROM t WHERE c = 8 FOR UPDATE;
-- Gap Lock (5, 10) — 间隙锁不互斥

-- 事务A
INSERT INTO t VALUES (7, 7);
-- 等待事务B的 Gap Lock 释放

-- 事务B
INSERT INTO t VALUES (8, 8);
-- 等待事务A的 Gap Lock 释放
-- 死锁！
```

### 5.2 避免死锁的策略

1. **按固定顺序访问**：避免交叉锁定
2. **缩小锁定范围**：使用索引减少锁定行数
3. **降低隔离级别**：RC 下无间隙锁
4. **缩短事务**：减少持锁时间
5. **使用乐观锁**：避免使用 FOR UPDATE

```sql
-- 查看死锁日志
SHOW ENGINE INNODB STATUS;

-- 设置死锁超时（秒）
SET GLOBAL innodb_lock_wait_timeout = 50;
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
| 间隙锁与临键锁解决幻读 | 065-GapLockNextKeyLockSolutionPhantomRead | 本文自身 |
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
