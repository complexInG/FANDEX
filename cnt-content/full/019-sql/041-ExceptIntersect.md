---
order: 410
title: SQL EXCEPT / INTERSECT 集合操作语法速查手册
module: sql

category: '019-sql'
difficulty: beginner
description: SQL EXCEPT / INTERSECT 集合操作语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基本集合操作

**基本写法：UNION 并集**
`<查询1> UNION [ALL] <查询2>`
```sql
-- UNION 去重，UNION ALL 保留重复（更快）
SELECT name FROM teachers
UNION
SELECT name FROM students;

-- UNION ALL 不去重，性能更优
SELECT '2024' AS year, month, income FROM income_2024
UNION ALL
SELECT '2025' AS year, month, income FROM income_2025;
```

---

**基本写法：INTERSECT 交集**
`<查询1> INTERSECT [ALL] <查询2>`
```sql
-- 返回两个查询结果中都存在的行
-- 找出同时选修了数学和物理的学生
SELECT student_id FROM scores WHERE subject = '数学'
INTERSECT
SELECT student_id FROM scores WHERE subject = '物理';

-- INTERSECT ALL 保留重复行（SQL 标准，PostgreSQL 支持）
SELECT tag FROM article_tags WHERE article_id = 1
INTERSECT ALL
SELECT tag FROM article_tags WHERE article_id = 2;
```

---

**基本写法：EXCEPT 差集**
`<查询1> EXCEPT [ALL] <查询2>`
```sql
-- 返回在查询1中但不在查询2中的行
-- 找出未下单的用户
SELECT id FROM users
EXCEPT
SELECT user_id FROM orders;

-- MySQL 不支持 EXCEPT，用 NOT IN 或 LEFT JOIN 替代
SELECT id FROM users
WHERE id NOT IN (SELECT user_id FROM orders);

-- LEFT JOIN 替代
SELECT u.id FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.user_id IS NULL;
```

---

## 三集合组合

**基本写法：链式集合操作**
`<查询1> UNION <查询2> UNION <查询3>`
```sql
-- 多个查询组合，注意优先级
SELECT '员工' AS type, name FROM employees
UNION
SELECT '客户' AS type, name FROM customers
UNION
SELECT '供应商' AS type, name FROM suppliers
ORDER BY type, name;
```

---

**基本写法：括号控制优先级**
`(<查询1> UNION <查询2>) INTERSECT <查询3>`
```sql
-- 括号改变执行顺序（PostgreSQL/Oracle 支持，MySQL 8.0+ 支持）
(SELECT city FROM customers WHERE country = 'US'
 UNION
 SELECT city FROM suppliers WHERE country = 'US')
INTERSECT
SELECT city FROM offices WHERE country = 'US';
```

---

## 集合操作规则

**基本写法：列数与类型对齐**
`SELECT <同数量同类型列> ... UNION ...`
```sql
-- 规则：列数相同、类型兼容、顺序对应
-- 第一个查询决定列名
SELECT product_id, product_name, 'active' AS status
FROM products WHERE active = 1
UNION
SELECT product_id, product_name, 'discontinued' AS status
FROM products WHERE active = 0
ORDER BY product_id;
```

---

## 集合操作与 NULL

**基本写法：NULL 处理**
`SELECT ... UNION ... -- NULL 被视为相等`
```sql
-- 集合操作中 NULL 视为相等（与 WHERE 不同）
-- INTERSECT 会匹配 NULL
SELECT NULL AS val UNION SELECT NULL;  -- 返回 1 行 NULL
SELECT NULL INTERSECT SELECT NULL;     -- 返回 1 行 NULL

-- 注意：EXCEPT 中 NULL 也参与匹配
SELECT 1 WHERE 1 IN (SELECT NULL);     -- 无结果
SELECT 1 EXCEPT SELECT NULL;            -- 返回 1
```

---

## 实战场景

**基本写法：找差集（未完成 vs 已完成）**
`SELECT ... EXCEPT SELECT ...`
```sql
-- 找出有库存但从未售出的商品
SELECT product_id FROM inventory
EXCEPT
SELECT DISTINCT product_id FROM order_items;

-- MySQL 替代
SELECT i.product_id FROM inventory i
WHERE NOT EXISTS (
  SELECT 1 FROM order_items o WHERE o.product_id = i.product_id
);
```

---

**基本写法：对称差集（A XOR B）**
`(A EXCEPT B) UNION (B EXCEPT A)`
```sql
-- 对称差集：只在 A 或只在 B，不在两者交集
(SELECT id FROM table_a
 EXCEPT
 SELECT id FROM table_b)
UNION
(SELECT id FROM table_b
 EXCEPT
 SELECT id FROM table_a);
```

---

## ORDER BY 与 LIMIT

**基本写法：结果排序与限制**
`<集合操作> ORDER BY <列> [LIMIT <n>]`
```sql
-- ORDER BY 必须在最后，作用于整体结果
-- 列名用第一个查询的列名
SELECT name, score FROM team_a
UNION ALL
SELECT name, score FROM team_b
ORDER BY score DESC
LIMIT 10;

-- 对单个子查询限制需用括号（部分数据库支持）
(SELECT name FROM t1 ORDER BY score DESC LIMIT 5)
UNION
(SELECT name FROM t2 ORDER BY score DESC LIMIT 5);
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
| 脏读不可重复读幻读 | 033-DirtyReadNonRepeatablePhantom | 本文的并列主题 |
| 锁机制 | 034-LockMechanism | 本文的原理深化 |
| MVCC | 035-MVCC | 本文的并列主题 |
| 窗口函数框架 | 036-WindowFunctionFramework | 本文的并列主题 |
| 递归CTE遍历树结构 | 037-RecursiveCTETreeTraversal | 本文的并列主题 |
| 乐观锁与悲观锁 | 038-OptimisticPessimisticLock | 本文的并列主题 |
| 常见SQL反模式 | 039-SQLAntipattern | 本文的并列主题 |
| SQL MERGE / UPSERT 语句语法速查手册 | 040-MergeStatement | 本文的并列主题 |
| SQL EXCEPT / INTERSECT 集合操作语法速查手册 | 041-ExceptIntersect | 本文自身 |
| 类型转换 语法速查手册 | 042-TypeConversion | 本文的并列主题 |
