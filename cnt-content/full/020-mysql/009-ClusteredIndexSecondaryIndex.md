---
order: 53
title: 聚簇索引与二级索引
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL InnoDB聚簇索引与二级索引：B+树结构、回表查询、覆盖索引与索引优化策略'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/Memory存储引擎
  - mysql/NDB集群
  - mysql/联合索引与最左前缀原则
  - mysql/索引下推
prerequisites:
  - mysql/语法速查
---

## 1. 聚簇索引

### 1.1 概念

聚簇索引将数据行与主键索引存储在同一棵 B+树中，叶子节点直接包含完整的行数据。InnoDB 每张表只有一个聚簇索引。

```
聚簇索引 B+树结构：
            [30|60]
           /   |    \
    [10|20|30] [40|50|60] [70|80|90]
        ↓         ↓         ↓
    → [行1][行2][行3] → [行4][行5][行6] → [行7][行8][行9] →
        叶子节点（包含完整行数据）
```

### 1.2 聚簇索引的选择

InnoDB 按以下优先级选择聚簇索引：

1. 显式定义的 PRIMARY KEY
2. 第一个 NOT NULL 的 UNIQUE KEY
3. 系统自动生成的隐藏 ROW_ID（6字节）

```sql
-- 推荐使用自增主键
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,  -- 聚簇索引
    name VARCHAR(100),
    email VARCHAR(200) UNIQUE
);

-- 避免使用 UUID 作为主键
-- UUID 无序，插入导致页分裂，索引碎片化
```

### 1.3 自增主键 vs UUID 主键

| 特性       | 自增主键 | UUID 主键             |
| ---------- | -------- | --------------------- |
| 插入顺序   | 顺序追加 | 随机插入              |
| 页分裂     | 极少     | 频繁                  |
| 索引碎片   | 少       | 多                    |
| 空间利用率 | 高       | 低（36字节 vs 8字节） |
| 全局唯一   | 否       | 是                    |
| 安全性     | 可预测   | 不可预测              |

## 2. 二级索引

### 2.1 概念

二级索引（非聚簇索引）的叶子节点存储主键值而非行数据。通过二级索引查找行数据需要两步：先查二级索引获取主键，再查聚簇索引获取行数据。

```
二级索引 B+树结构：
            [M|S]
           /     \
    [A|D|M]      [S|Z]
      ↓            ↓
    → [1][3][5] → [7][9] →
      叶子节点（存储主键值）
```

### 2.2 回表查询

```sql
-- 二级索引：idx_employees_name (name)
SELECT * FROM employees WHERE name = 'Alice';

-- 执行过程：
-- 1. 在 name 索引 B+树中查找 'Alice'，获取主键 id = 5
-- 2. 在聚簇索引 B+树中查找 id = 5，获取完整行数据
-- 这就是"回表"操作
```

### 2.3 回表的代价

```sql
-- 如果查询返回大量行，回表代价很高
-- 假设 name 索引选择性低，返回 10000 行
SELECT * FROM employees WHERE name = 'Alice';  -- 10000次回表

-- 优化器可能选择全表扫描而非索引 + 回表
-- 当回表代价 > 全表扫描代价时
```

## 3. 覆盖索引

### 3.1 概念

覆盖索引是指索引包含了查询所需的所有列，无需回表。

```sql
-- 创建覆盖索引
CREATE INDEX idx_employees_dept_name_salary
ON employees(dept_id, name, salary);

-- 覆盖索引查询：不需要回表
SELECT name, salary FROM employees WHERE dept_id = 5;
-- EXPLAIN 中 Extra: Using index

-- 非覆盖索引查询：需要回表
SELECT name, salary, email FROM employees WHERE dept_id = 5;
-- email 不在索引中，需要回表
```

### 3.2 覆盖索引优化场景

```sql
-- 场景1：避免回表
-- 无覆盖索引
SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;
-- 需要回表获取 user_id

-- 有覆盖索引
CREATE INDEX idx_orders_user_id ON orders(user_id);
SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;
-- Using index，无需回表

-- 场景2：分页查询优化
SELECT id, title FROM articles ORDER BY created_at DESC LIMIT 10000, 10;
-- 使用覆盖索引避免大量回表
CREATE INDEX idx_articles_created_id_title ON articles(created_at DESC, id, title);
```

## 4. 索引下推（ICP）

### 4.1 概念

索引条件下推（Index Condition Pushdown，ICP）将 WHERE 条件中可以在索引上评估的部分下推到存储引擎层，减少回表次数。

```sql
-- 索引 (name, age)
SELECT * FROM employees WHERE name LIKE '张%' AND age > 30;

-- 无 ICP：
-- 1. 存储引擎通过 name LIKE '张%' 找到所有主键
-- 2. 回表获取完整行
-- 3. Server 层评估 age > 30

-- 有 ICP：
-- 1. 存储引擎通过 name LIKE '张%' 找到索引项
-- 2. 在索引中直接评估 age > 30（age 在索引中）
-- 3. 只对满足条件的行回表
-- 减少回表次数！
```

### 4.2 ICP 开启

```sql
-- 默认开启
SET optimizer_switch = 'index_condition_pushdown=on';

-- EXPLAIN 中 Extra: Using index condition
```

## 5. 索引优化策略

### 5.1 减少回表

```sql
-- 方法1：使用覆盖索引
CREATE INDEX idx_cover ON employees(dept_id, name, salary);
SELECT name, salary FROM employees WHERE dept_id = 5;

-- 方法2：延迟关联
-- 先通过二级索引获取主键，再通过主键获取行
SELECT e.* FROM employees e
JOIN (
    SELECT id FROM employees WHERE name LIKE '张%' LIMIT 10000, 10
) tmp ON e.id = tmp.id;
```

### 5.2 避免不必要的列

```sql
-- 不推荐：SELECT *
SELECT * FROM employees WHERE dept_id = 5;

-- 推荐：只查需要的列
SELECT name, salary FROM employees WHERE dept_id = 5;
-- 可能命中覆盖索引
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
| 聚簇索引与二级索引 | 009-ClusteredIndexSecondaryIndex | 本文自身 |
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
| 事件调度器 语法速查手册 | 086-EventScheduler | 本文的并列主题 |
| 字符集与排序规则 语法速查手册 | 087-CharsetCollation | 本文的并列主题 |
