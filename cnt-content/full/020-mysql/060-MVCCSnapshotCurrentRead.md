---
order: 100
title: MVCC快照读与当前读
module: mysql
category: database
difficulty: advanced
description: 'MySQL InnoDB MVCC 机制详解：快照读与当前读的区别、ReadView 创建时机、Undo Log 版本链与一致性非锁定读原理。'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/函数索引
  - mysql/存储过程与函数
  - mysql/索引原理与性能优化
  - mysql/触发器与事件
prerequisites:
  - mysql/语法速查
---

## 1. MVCC 基础概念

### 1.1 什么是 MVCC

MVCC（Multi-Version Concurrency Control，多版本并发控制）是 InnoDB 实现高并发读写的核心机制。其核心思想是：**读不阻塞写，写不阻塞读**。

```
传统锁机制：读 → 加共享锁 → 阻塞写
MVCC机制：  读 → 访问历史版本 → 不阻塞写
```

### 1.2 MVCC 的核心组件

| 组件            | 作用                                             |
| --------------- | ------------------------------------------------ |
| 隐藏列          | `DB_TRX_ID`（事务ID）、`DB_ROLL_PTR`（回滚指针） |
| Undo Log 版本链 | 通过 `DB_ROLL_PTR` 串联的历史版本                |
| ReadView        | 决定当前事务能看到哪个版本                       |

### 1.3 隐藏列结构

每行数据包含两个隐藏列：

```mermaid
flowchart LR
    D[数据列 用户数据] --- T[DB_TRX_ID 6字节<br/>最后修改该行的事务ID]
    T --- R[DB_ROLL_PTR 7字节<br/>指向 Undo Log 中该行的上一个版本]
    R --- W[DB_ROW_ID 6字节<br/>隐藏自增ID 无主键时自动生成]
```

## 2. Undo Log 版本链

### 2.1 版本链构建

当一行数据被多次修改时，每次修改前的旧版本通过 `DB_ROLL_PTR` 串联成链表：

```
当前行: {data='C', trx_id=303, roll_ptr→undo_C}
                                         ↓
Undo版本: {data='B', trx_id=202, roll_ptr→undo_B}
                                         ↓
Undo版本: {data='A', trx_id=101, roll_ptr→NULL}
```

### 2.2 版本链遍历

当事务需要读取数据时，从当前行开始沿版本链向前遍历，找到第一个对当前事务可见的版本。

## 3. ReadView 机制

### 3.1 ReadView 结构

ReadView 是事务进行快照读时创建的"可见性判断规则"，包含四个关键字段：

```
ReadView {
    m_ids:        [201, 302]          -- 创建时所有活跃（未提交）事务ID列表
    min_trx_id:   201                 -- m_ids 中的最小值
    max_trx_id:   401                 -- 下一个将分配的事务ID（当前最大事务ID+1）
    creator_trx_id: 303               -- 创建该 ReadView 的事务ID
}
```

### 3.2 可见性判断规则

对于版本链中某个版本的 `trx_id`：

```
1. trx_id == creator_trx_id → 可见（自己修改的）
2. trx_id < min_trx_id      → 可见（该事务在 ReadView 创建前已提交）
3. trx_id >= max_trx_id     → 不可见（该事务在 ReadView 创建后才开始）
4. min_trx_id <= trx_id < max_trx_id:
   - trx_id 在 m_ids 中 → 不可见（该事务未提交）
   - trx_id 不在 m_ids 中 → 可见（该事务已提交）
```

### 3.3 可见性判断流程图

```
                    trx_id == creator_trx_id?
                    /                    \
                  YES                    NO
                  ↓                       ↓
               可见              trx_id < min_trx_id?
                                /                \
                              YES                NO
                              ↓                  ↓
                            可见        trx_id >= max_trx_id?
                                      /                \
                                    YES                NO
                                    ↓                  ↓
                                 不可见       trx_id ∈ m_ids?
                                            /          \
                                          YES          NO
                                          ↓            ↓
                                        不可见        可见
```

## 4. 快照读与当前读

### 4.1 快照读（Snapshot Read）

快照读读取的是数据的**历史版本**，不加锁，通过 MVCC 实现：

```sql
-- 普通 SELECT 都是快照读
SELECT * FROM users WHERE id = 1;
```

**RC 隔离级别**：每次 SELECT 都创建新的 ReadView

```
事务A (trx_id=300):
  SELECT * FROM users WHERE id=1;  -- 创建 ReadView_1
  -- 此时事务B修改了 id=1 并提交
  SELECT * FROM users WHERE id=1;  -- 创建 ReadView_2，能看到事务B的修改
```

**RR 隔离级别**：只在第一次 SELECT 时创建 ReadView，后续复用

```
事务A (trx_id=300):
  SELECT * FROM users WHERE id=1;  -- 创建 ReadView_1
  -- 此时事务B修改了 id=1 并提交
  SELECT * FROM users WHERE id=1;  -- 复用 ReadView_1，看不到事务B的修改
```

### 4.2 当前读（Current Read）

当前读读取的是数据的**最新版本**，并加锁：

```sql
-- 当前读语句
SELECT * FROM users WHERE id = 1 FOR UPDATE;      -- 排他锁
SELECT * FROM users WHERE id = 1 LOCK IN SHARE MODE; -- 共享锁
UPDATE users SET name = 'new' WHERE id = 1;        -- 排他锁
DELETE FROM users WHERE id = 1;                     -- 排他锁
INSERT INTO users VALUES (1, 'new');                -- 插入锁
```

### 4.3 快照读与当前读对比

| 维度     | 快照读      | 当前读           |
| -------- | ----------- | ---------------- |
| 读取版本 | 历史版本    | 最新版本         |
| 加锁     | 不加锁      | 加行锁/间隙锁    |
| ReadView | 创建/复用   | 不使用           |
| 语句     | 普通 SELECT | FOR UPDATE / DML |
| 一致性   | 一致性视图  | 实时数据         |

### 4.4 快照读与当前读混合的陷阱

```sql
-- RR 隔离级别下的经典问题
BEGIN;
-- 快照读：读取 stock=10
SELECT stock FROM products WHERE id=1;  -- stock=10

-- 当前读：读取最新 stock
SELECT stock FROM products WHERE id=1 FOR UPDATE;  -- stock=8（已被其他事务修改）

-- 快照读：仍然读取旧值
SELECT stock FROM products WHERE id=1;  -- stock=10（ReadView 未更新）

-- UPDATE 是当前读，基于最新版本
UPDATE products SET stock = stock - 1 WHERE id=1;  -- 基于 stock=8

COMMIT;
```

## 5. 不同隔离级别的 MVCC 行为

### 5.1 READ UNCOMMITTED

不使用 MVCC，直接读取最新数据（可能读到未提交数据）。

### 5.2 READ COMMITTED

每次 SELECT 创建新 ReadView：

```
时间线:  T1        T2        T3        T4
事务A:   BEGIN     SELECT→RV1           SELECT→RV2
事务B:             BEGIN     UPDATE    COMMIT

T2: SELECT 创建 RV1，看到事务B修改前的数据
T4: SELECT 创建 RV2，看到事务B已提交的修改
```

### 5.3 REPEATABLE READ

只在第一次 SELECT 创建 ReadView，后续复用：

```
时间线:  T1        T2        T3        T4
事务A:   BEGIN     SELECT→RV1           SELECT(复用RV1)
事务B:             BEGIN     UPDATE    COMMIT

T2: SELECT 创建 RV1
T4: SELECT 复用 RV1，仍然看到事务B修改前的数据
```

### 5.4 SERIALIZABLE

所有 SELECT 自动加共享锁，退化为当前读，不存在快照读。

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
| MVCC快照读与当前读 | 060-MVCCSnapshotCurrentRead | 本文自身 |
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
