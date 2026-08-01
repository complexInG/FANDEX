---
order: 72
title: 脏读不可重复读幻读
module: sql
category: SQL
difficulty: intermediate
description: SQL并发异常：脏读、不可重复读、幻读的定义、示例、区别与防护策略
author: fanquanpp
updated: '2026-08-01'
related:
  - sql/事务ACID特性
  - sql/隔离级别
  - sql/锁机制
  - sql/多版本并发控制
prerequisites:
  - sql/概述与标准
---

## 1. 并发异常概述

当多个事务并发执行时，可能产生三种数据不一致问题：

| 异常       | 英文                | 影响             | 严重程度 |
| ---------- | ------------------- | ---------------- | -------- |
| 脏读       | Dirty Read          | 读到未提交数据   | 高       |
| 不可重复读 | Non-Repeatable Read | 同一查询结果不同 | 中       |
| 幻读       | Phantom Read        | 行数变化         | 低       |

## 2. 脏读（Dirty Read）

### 2.1 定义

事务A读取了事务B**未提交**的修改，如果事务B回滚，事务A读到的就是无效数据。

### 2.2 场景示例

```sql
-- 初始状态：账户1余额 = 1000

-- 事务A（READ UNCOMMITTED）
BEGIN ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 返回 1000

-- 事务B
BEGIN;
UPDATE accounts SET balance = 5000 WHERE id = 1;
-- 未提交

-- 事务A
SELECT balance FROM accounts WHERE id = 1;
-- 返回 5000 ← 脏读！读到事务B未提交的修改

-- 事务B回滚
ROLLBACK;
-- balance 恢复为 1000

-- 事务A基于 5000 做出的决策是错误的
```

### 2.3 脏读的危害

```
场景：电商库存
T1: UPDATE stock SET count = 0 WHERE product_id = 100;  -- 库存清零
T2: SELECT count FROM stock WHERE product_id = 100;     -- 读到 0
T2: -- 判断库存不足，拒绝用户下单
T1: ROLLBACK;  -- 库存恢复为 10
-- 结果：用户被错误拒绝，实际有库存
```

### 2.4 防护

- 使用 READ COMMITTED 及以上隔离级别
- 几乎所有生产环境都不使用 READ UNCOMMITTED

## 3. 不可重复读（Non-Repeatable Read）

### 3.1 定义

事务A两次读取同一行数据，中间事务B修改并提交了该行，导致两次读取结果不同。

### 3.2 场景示例

```sql
-- 初始状态：账户1余额 = 1000

-- 事务A（READ COMMITTED）
BEGIN ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 返回 1000

-- 事务B
BEGIN;
UPDATE accounts SET balance = 2000 WHERE id = 1;
COMMIT;

-- 事务A再次读取同一行
SELECT balance FROM accounts WHERE id = 1;
-- 返回 2000 ← 不可重复读！同一事务内两次读取结果不同
```

### 3.3 不可重复读的危害

```
场景：审计对账
T1: SELECT SUM(balance) FROM accounts;       -- 总额 10000
T2: UPDATE accounts SET balance = balance + 1000 WHERE id = 1; COMMIT;
T1: SELECT SUM(balance) FROM accounts;       -- 总额 11000
-- 两次汇总结果不一致，审计报告不准确
```

### 3.4 防护

```sql
-- 方法1：使用 REPEATABLE READ 隔离级别
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT balance FROM accounts WHERE id = 1;  -- 1000
-- 事务B修改并提交
SELECT balance FROM accounts WHERE id = 1;  -- 仍然是 1000

-- 方法2：使用 SELECT FOR UPDATE 锁定行
BEGIN ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;  -- 加锁
-- 事务B无法修改该行（被锁阻塞）
SELECT balance FROM accounts WHERE id = 1;  -- 一致
COMMIT;
```

## 4. 幻读（Phantom Read）

### 4.1 定义

事务A两次执行相同的范围查询，中间事务B插入并提交了新行，导致第二次查询多出"幻影行"。

### 4.2 场景示例

```sql
-- 初始状态：dept_id = 5 有3名员工

-- 事务A（REPEATABLE READ）
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT COUNT(*) FROM employees WHERE dept_id = 5;
-- 返回 3

-- 事务B
INSERT INTO employees (name, dept_id) VALUES ('新员工', 5);
COMMIT;

-- 事务A再次查询
SELECT COUNT(*) FROM employees WHERE dept_id = 5;
-- MVCC 下：返回 3（快照读无幻读）
-- 但当前读可能出现幻读：

-- 事务A执行更新
UPDATE employees SET salary = salary + 100 WHERE dept_id = 5;
-- 影响了4行！（包括事务B插入的行）

SELECT COUNT(*) FROM employees WHERE dept_id = 5;
-- 返回 4 ← 幻读！
```

### 4.3 幻读 vs 不可重复读

| 特性     | 不可重复读       | 幻读             |
| -------- | ---------------- | ---------------- |
| 影响对象 | 已存在的行被修改 | 新行被插入或删除 |
| 锁范围   | 行级锁           | 间隙锁/谓词锁    |
| SQL 语句 | UPDATE/DELETE    | INSERT           |
| 防护方式 | REPEATABLE READ  | SERIALIZABLE     |

### 4.4 防护

```sql
-- 方法1：使用 SERIALIZABLE 隔离级别
BEGIN ISOLATION LEVEL SERIALIZABLE;

-- 方法2：MySQL InnoDB 使用 Next-Key Lock
BEGIN;
SELECT * FROM employees WHERE dept_id = 5 FOR UPDATE;
-- 锁定 dept_id = 5 的所有行及间隙
-- 事务B无法插入 dept_id = 5 的新行

-- 方法3：应用层使用 advisory lock（PostgreSQL）
SELECT pg_advisory_lock(5);  -- 锁定部门5
-- 执行操作
SELECT pg_advisory_unlock(5);
```

## 5. 三种异常的完整对比

### 5.1 时间线对比

**脏读**：

```
T1: BEGIN;     UPDATE → value=200 (未提交)
T2:                    SELECT → 200 (脏读!)
T1: ROLLBACK;  (value 恢复为 100)
```

**不可重复读**：

```
T1: BEGIN;     SELECT → 100
T2:                    UPDATE → 200; COMMIT;
T1:             SELECT → 200 (不可重复读!)
```

**幻读**：

```
T1: BEGIN;     SELECT COUNT → 3
T2:                    INSERT; COMMIT;
T1:             SELECT COUNT → 4 (幻读!)
```

### 5.2 隔离级别与异常关系

$$
\begin{aligned}
\text{READ UNCOMMITTED} &\supseteq \{\text{脏读, 不可重复读, 幻读}\} \\
\text{READ COMMITTED} &\supseteq \{\text{不可重复读, 幻读}\} \\
\text{REPEATABLE READ} &\supseteq \{\text{幻读}\} \\
\text{SERIALIZABLE} &= \emptyset
\end{aligned}
$$

## 6. 实战防护策略

### 6.1 选择合适的隔离级别

```sql
-- 大多数 OLTP 场景：READ COMMITTED 足够
-- 需要一致性读取：REPEATABLE READ
-- 严格一致性：SERIALIZABLE（性能代价大）
```

### 6.2 乐观锁替代高隔离级别

```sql
-- 使用版本号实现乐观锁
UPDATE products
SET stock = stock - 1, version = version + 1
WHERE id = 100 AND version = 5 AND stock > 0;
-- 如果影响行数为0，说明并发冲突，重试
```

### 6.3 SELECT FOR UPDATE 精确加锁

```sql
-- 只锁定需要的行，避免提升隔离级别
BEGIN ISOLATION LEVEL READ COMMITTED;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- 检查余额
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

## 参考文献



SQL 标准（ISO/IEC 9075）：https://www.iso.org/standard/76583.html
PostgreSQL 文档（SQL 章节）：https://www.postgresql.org/docs/current/sql.html
MySQL 文档：https://dev.mysql.com/doc/
SQLite 文档：https://www.sqlite.org/docs.html
Use The Index, Luke：https://use-the-index-luke.com/

## 延伸阅读



SQL 连接与子查询，见 019-sql 模块文档。
SQL 自连接与递归，见 019-sql/019-SelfJoin 文档。
MySQL 深入，见 020-mysql 模块。
PostgreSQL 深入，见 021-postgresql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 索引原理与 B+ 树

B+ 树：非叶节点存索引键，叶节点存数据指针并链表相连；高度低（3-4 层）支撑千万级数据。
聚集索引（主键）决定数据物理顺序；二级索引存主键值，回表取行；覆盖索引避免回表。
最左前缀：复合索引按定义顺序匹配；范围查询后列失效。
选择率：区分度高的列放前面；低基数列（性别）单列索引收益低。

### 13.2 事务隔离与 MVCC

四种隔离级别：读未提交、读已提交、可重复读、可串行化；各自解决脏读、不可重复读、幻读。
MVCC（多版本并发控制）：快照读不加锁，写通过版本链与回滚段实现；读写互不阻塞。
PostgreSQL 默认读已提交，MySQL InnoDB 默认可重复读；理解差异避免跨库移植踩坑。
死锁处理：锁顺序一致、超时检测、重试策略。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与标准 | 001-OverviewStandard | 本文的前置基础 |
| 数据查询基础 | 002-DataQueryBasics | 本文的前置基础 |
| 多表查询 | 003-MultiTableQuery | 本文的并列主题 |
| 数据操作 | 004-DML | 本文的并列主题 |
| 数据定义 | 005-DDL | 本文的并列主题 |
| 窗口函数 | 006-WindowFunction | 本文的并列主题 |
| 高级查询 | 007-AdvancedQuery | 本文的并列主题 |
| 性能优化 | 008-PerformanceOptimization | 本文的性能延伸 |
| PL-SQL与存储过程 | 009-PLSQLStoredProcedure | 本文的并列主题 |
| SQL实战与面试 | 010-SQLPracticeInterview | 本文的综合应用 |
| 数据类型 | 011-DataType | 本文的并列主题 |
| 约束 | 012-Constraint | 本文的并列主题 |
| SELECT执行顺序 | 013-SelectExecutionOrder | 本文的并列主题 |
| 过滤条件 | 014-FilterCondition | 本文的并列主题 |
| 聚合函数 | 015-AggregateFunction | 本文的并列主题 |
| GROUP BY与分组集 | 016-GROUPBYGroupingSet | 本文的并列主题 |
| 连接查询 | 017-JoinQuery | 本文的并列主题 |
| 自然连接与USING | 018-NaturalJoinUsing | 本文的并列主题 |
| 自连接 | 019-SelfJoin | 本文的并列主题 |
| 半连接与反半连接 | 020-SemiAntiJoin | 本文的并列主题 |
| LATERAL派生表 | 021-LateralDerivedTable | 本文的并列主题 |
| 子查询 | 022-Subquery | 本文的并列主题 |
| CTE | 023-CTE | 本文的并列主题 |
| 递归CTE | 024-RecursiveCTE | 本文的并列主题 |
| PIVOT与UNPIVOT | 025-PivotUnpivot | 本文的并列主题 |
| 集合操作 | 026-SetOperation | 本文的并列主题 |
| DCL | 027-DCL | 本文的并列主题 |
| TCL | 028-TCL | 本文的并列主题 |
| 索引 | 029-Index | 本文的并列主题 |
| 执行计划 | 030-ExecutionPlan | 本文的并列主题 |
| 事务ACID特性 | 031-TransactionACIDProperty | 本文的并列主题 |
| 隔离级别 | 032-IsolationLevel | 本文的并列主题 |
| 脏读不可重复读幻读 | 033-DirtyReadNonRepeatablePhantom | 本文自身 |
| 锁机制 | 034-LockMechanism | 本文的原理深化 |
| MVCC | 035-MVCC | 本文的并列主题 |
| 窗口函数框架 | 036-WindowFunctionFramework | 本文的并列主题 |
| 递归CTE遍历树结构 | 037-RecursiveCTETreeTraversal | 本文的并列主题 |
| 乐观锁与悲观锁 | 038-OptimisticPessimisticLock | 本文的并列主题 |
| 常见SQL反模式 | 039-SQLAntipattern | 本文的并列主题 |
| SQL MERGE / UPSERT 语句语法速查手册 | 040-MergeStatement | 本文的并列主题 |
| SQL EXCEPT / INTERSECT 集合操作语法速查手册 | 041-ExceptIntersect | 本文的并列主题 |
| 类型转换 语法速查手册 | 042-TypeConversion | 本文的并列主题 |
