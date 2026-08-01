---
order: 67
title: JOIN算法
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL JOIN算法：Nested Loop Join、Block Nested Loop、Hash Join的原理、适用场景与优化'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/派生表优化
  - 'mysql/GROUP-BY与ORDER-BY优化'
  - mysql/事务隔离级别底层实现
  - mysql/MVCC原理
prerequisites:
  - mysql/语法速查
---

# MySQL Join 多表连接

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. JOIN 算法概述

MySQL 支持多种 JOIN 算法，优化器根据表大小、索引和条件选择最优算法。

## 2. Nested Loop Join（NLJ）

### 2.1 原理

```
for each row in outer_table:
    for each row in inner_table:
        if match_condition:
            output combined row
```

```sql
-- 驱动表：departments，被驱动表：employees
SELECT * FROM departments d JOIN employees e ON d.id = e.dept_id;

-- 执行过程：
-- 1. 扫描 departments 表的每一行
-- 2. 对每行，使用 idx_employees_dept_id 索引查找 employees
-- 3. 如果有索引：Index Nested Loop Join
-- 4. 如果无索引：Block Nested Loop Join
```

### 2.2 Index Nested Loop Join

```sql
-- 被驱动表有索引时使用
-- 时间复杂度：O(M * log N)
-- M = 驱动表行数，N = 被驱动表行数

-- 确保 JOIN 列有索引
CREATE INDEX idx_employees_dept_id ON employees(dept_id);
```

## 3. Block Nested Loop Join（BNL）

### 3.1 原理

```
1. 将驱动表的数据块读入 join_buffer
2. 扫描被驱动表，与 join_buffer 中的数据匹配
3. 减少被驱动表的扫描次数
```

```sql
-- 被驱动表无索引时使用
-- join_buffer_size 控制缓冲区大小
SET join_buffer_size = 262144;  -- 256KB

-- EXPLAIN 中 Extra: Using join buffer (Block Nested Loop)
```

### 3.2 优化

```sql
-- 增大 join_buffer_size
SET join_buffer_size = 8388608;  -- 8MB

-- 为 JOIN 列创建索引（转为 Index NLJ）
CREATE INDEX idx_join_col ON table_name(join_col);

-- 小表做驱动表
-- 驱动表越小，join_buffer 效果越好
```

## 4. Hash Join

### 4.1 原理

MySQL 8.0.18 引入 Hash Join，替代无索引场景下的 BNL：

```
1. Build 阶段：扫描小表，构建哈希表
2. Probe 阶段：扫描大表，在哈希表中查找匹配
```

```sql
-- 等值连接无索引时自动使用
SELECT * FROM t1 JOIN t2 ON t1.col = t2.col;
-- Extra: Using join buffer (hash join)

-- Hash Join 优势：
-- 时间复杂度：O(M + N)，比 BNL 的 O(M * N) 好
-- 不需要索引
```

### 4.2 Hash Join 限制

```sql
-- 仅支持等值连接（=, <=>）
-- 不支持非等值连接（>, <, BETWEEN）

-- 非等值连接仍使用 BNL
SELECT * FROM t1 JOIN t2 ON t1.col > t2.col;
-- Extra: Using join buffer (Block Nested Loop)
```

## 5. JOIN 优化策略

```sql
-- 1. 确保 JOIN 列有索引
-- 2. 小表做驱动表
-- 3. 避免过多表连接（建议不超过5个）
-- 4. 使用 STRAIGHT_JOIN 控制连接顺序
SELECT /*+ STRAIGHT_JOIN */ *
FROM small_table s
JOIN large_table l ON s.id = l.small_id;

-- 5. 使用 BKA（Batched Key Access）
SET optimizer_switch = 'batched_key_access=on';
-- 将驱动表的行批量传递给被驱动表
```
## INNER JOIN 内连接

**换行写法：内连接查询**
`SELECT <列> FROM <表1> INNER JOIN <表2> ON <连接条件>;`
```sql
-- 查询用户及其订单
SELECT u.username, o.order_no, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

**换行写法：多表内连接**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件> JOIN <表3> ON <条件>;`
```sql
-- 三表关联查询
SELECT u.username, o.order_no, p.product_name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

**换行写法：使用 USING 简化连接**
`SELECT <列> FROM <表1> JOIN <表2> USING (<同名列>);`
```sql
-- 两表同名列时使用 USING
SELECT * FROM users JOIN user_profiles USING (user_id);
```

---

## LEFT JOIN 左连接

**换行写法：左连接查询**
`SELECT <列> FROM <表1> LEFT JOIN <表2> ON <连接条件>;`
```sql
-- 查询所有用户及其订单（含无订单用户）
SELECT u.username, o.order_no
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**换行写法：左连接筛选无匹配记录**
`SELECT <列> FROM <表1> LEFT JOIN <表2> ON <条件> WHERE <表2.列> IS NULL;`
```sql
-- 查询没有订单的用户
SELECT u.username
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

---

## RIGHT JOIN 右连接

**换行写法：右连接查询**
`SELECT <列> FROM <表1> RIGHT JOIN <表2> ON <连接条件>;`
```sql
-- 查询所有订单及其用户（含无用户订单）
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## CROSS JOIN 交叉连接

**单行写法：笛卡尔积**
`SELECT * FROM <表1> CROSS JOIN <表2>;`
```sql
-- 生成两表的笛卡尔积
SELECT * FROM colors CROSS JOIN sizes;
```

**单行写法：逗号连接等价写法**
`SELECT * FROM <表1>, <表2>;`
```sql
-- 逗号分隔等价于 CROSS JOIN
SELECT * FROM colors, sizes;
```

---

## 自连接

**换行写法：员工与上级自连接**
`SELECT <别名1.列>, <别名2.列> FROM <表> <别名1> JOIN <表> <别名2> ON <条件>;`
```sql
-- 查询员工姓名及其直接上级
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：同级分类自连接**
`SELECT <别名1.列>, <别名2.列> FROM <表> <别名1> JOIN <表> <别名2> ON <条件>;`
```sql
-- 查询分类及其父分类名称
SELECT c.name AS category, p.name AS parent
FROM categories c
LEFT JOIN categories p ON c.parent_id = p.id;
```

---

## 自然连接与 USING

**换行写法：NATURAL JOIN 自然连接**
`SELECT * FROM <表1> NATURAL JOIN <表2>;`
```sql
-- 自动按同名列连接
SELECT * FROM users NATURAL JOIN user_profiles;
```

---

## 复合条件连接

**换行写法：多条件连接**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件1> AND <条件2>;`
```sql
-- 多条件关联
SELECT u.username, o.order_no
FROM users u
JOIN orders o ON u.id = o.user_id AND o.status = 1;
```

**换行写法：连接加过滤条件**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件> WHERE <过滤条件>;`
```sql
-- 连接后再过滤
SELECT u.username, o.order_no
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.status = 1 AND o.created_at > '2024-01-01';
```

---

## 聚合与连接

**换行写法：连接加分组聚合**
`SELECT <列>, <聚合函数> FROM <表1> JOIN <表2> ON <条件> GROUP BY <列>;`
```sql
-- 查询每个用户的订单总数和总金额
SELECT u.username, COUNT(o.id) AS order_count, IFNULL(SUM(o.total_amount), 0) AS total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**换行写法：连接加 HAVING 过滤**
`SELECT <列>, <聚合> FROM <表1> JOIN <表2> ON <条件> GROUP BY <列> HAVING <条件>;`
```sql
-- 查询订单金额超过 1000 的用户
SELECT u.username, SUM(o.total_amount) AS total
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username
HAVING total > 1000;
```

---

## 8.0+ 高级连接特性

**换行写法：NOWAIT 不等待锁**
`SELECT * FROM <表1> JOIN <表2> ON <条件> FOR UPDATE NOWAIT;`
```sql
-- 行被锁时立即报错不等待
SELECT * FROM users u JOIN orders o ON u.id = o.user_id FOR UPDATE NOWAIT;
```

**换行写法：SKIP LOCKED 跳过锁定行**
`SELECT * FROM <表1> JOIN <表2> ON <条件> FOR UPDATE SKIP LOCKED;`
```sql
-- 跳过被其他事务锁定的行
SELECT * FROM users u JOIN orders o ON u.id = o.user_id FOR UPDATE SKIP LOCKED;
```

**换行写法：LATERAL 派生表（8.0.14+）**
`SELECT * FROM <表1>, LATERAL (SELECT * FROM <表2> WHERE <条件> LIMIT <数量>) <别名>;`
```sql
-- 关联派生表查询每个用户最近 3 笔订单
SELECT u.username, o.order_no
FROM users u,
LATERAL (
  SELECT order_no, total_amount
  FROM orders
  WHERE user_id = u.id
  ORDER BY created_at DESC
  LIMIT 3
) o;
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
| JOIN算法 | 024-JOINAlgorithm | 本文自身 |
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
