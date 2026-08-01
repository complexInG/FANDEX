---
order: 420
title: 类型转换 语法速查手册
module: 019-sql
category: '019-sql'
difficulty: beginner
description: 类型转换 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 类型转换 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## CAST 标准转换

**基本写法：CAST 函数**
`CAST(<表达式> AS <目标类型>)`

```sql
-- 字符串转数值
SELECT CAST('123.45' AS DECIMAL(10,2)) AS price;
-- 数值转字符串
SELECT CAST(20240101 AS CHAR(8)) AS date_str;
-- 字符串转日期
SELECT CAST('2024-03-15' AS DATE) AS order_date;
```

**基本写法：CAST 常见目标类型**
`CAST(<表达式> AS <类型> [(<精度>[,<标度>])])`

```sql
-- 常用目标类型转换
SELECT
  CAST(3.14159 AS DECIMAL(5,2))     AS rounded,   -- 3.14
  CAST(100 AS CHAR(10))             AS str_val,   -- '100'
  CAST('2024-03-15 10:30:00' AS DATETIME) AS dt,  -- 日期时间
  CAST(1 AS BOOLEAN)                AS flag;      -- true（PG/MySQL8）
```

---

## CONVERT 函数

**基本写法：CONVERT 类型转换**
`CONVERT(<表达式>, <目标类型>)`

```sql
-- SQL Server 风格 CONVERT
SELECT CONVERT(VARCHAR(10), GETDATE(), 120) AS date_str;
-- MySQL 风格 CONVERT
SELECT CONVERT('2024-03-15', DATE) AS order_date;
```

**基本写法：CONVERT 字符集转换（MySQL）**
`CONVERT(<表达式> USING <字符集名>)`

```sql
-- 字符集转换
SELECT CONVERT('中文' USING utf8mb4) AS utf8_text;
SELECT CONVERT(name USING utf8mb4) FROM users;
```

---

## 隐式转换

**基本写法：运算中隐式转换**
`<数值列> <算术运算符> <字符串数值>`

```sql
-- 字符串与数值运算时自动转换
SELECT '100' + 50 AS result;          -- 150
SELECT order_id + 0 FROM orders;      -- 字符串 ID 转数值
SELECT '2024-03-15' + INTERVAL 1 DAY; -- 字符串日期参与运算
```

**基本写法：比较时隐式转换**
`WHERE <数值列> = '<字符串数值>'`

```sql
-- 比较时字符串自动转数值（不推荐，可能导致索引失效）
SELECT * FROM products WHERE price = '99.9';
-- 推荐显式转换以利用索引
SELECT * FROM products WHERE price = CAST('99.9' AS DECIMAL(10,2));
```

---

## 专用转换函数

**基本写法：TO_NUMBER 字符串转数值（Oracle/PG）**
`TO_NUMBER(<字符串> [, <格式>])`

```sql
-- 带格式字符串转数值
SELECT TO_NUMBER('1,234.56', '9,999.99') AS amount;
-- PostgreSQL 简化用法
SELECT TO_NUMBER('123.45', '999.99') AS price;
```

**基本写法：TO_CHAR 数值/日期转字符串**
`TO_CHAR(<数值或日期> [, <格式>])`

```sql
-- 日期格式化为字符串
SELECT TO_CHAR(CURRENT_DATE, 'YYYY-MM-DD') AS today;
-- 数值格式化
SELECT TO_CHAR(12345.678, '999,999.99') AS formatted;
```

**基本写法：TO_DATE 字符串转日期**
`TO_DATE(<字符串> [, <格式>])`

```sql
-- 字符串解析为日期
SELECT TO_DATE('2024-03-15', 'YYYY-MM-DD') AS order_date;
SELECT TO_DATE('15/03/2024', 'DD/MM/YYYY') AS eu_date;
```

---

## NULL 与安全转换

**基本写法：COALESCE 处理转换后 NULL**
`COALESCE(CAST(<表达式> AS <类型>), <默认值>)`

```sql
-- 转换失败时返回默认值
SELECT
  user_id,
  COALESCE(CAST(score_text AS INT), 0) AS score
FROM user_scores;
```

**基本写法：TRY_CAST 安全转换（SQL Server/PG14+）**
`TRY_CAST(<表达式> AS <目标类型>)`

```sql
-- 转换失败返回 NULL 而非报错
SELECT
  TRY_CAST('abc' AS INT) AS num1,    -- NULL
  TRY_CAST('123' AS INT) AS num2;    -- 123
```

**基本写法：NULLIF 避免除零**
`NULLIF(<表达式>, 0)`

```sql
-- 分母为 0 时返回 NULL 避免报错
SELECT
  total_amount / NULLIF(item_count, 0) AS avg_price
FROM orders;
```

---

## 数组与 JSON 转换

**基本写法：数组转字符串（PostgreSQL）**
`<数组列>::text` 或 `ARRAY_TO_STRING(<数组>, <分隔符>)`

```sql
-- 数组拼接为字符串
SELECT ARRAY_TO_STRING(ARRAY['a','b','c'], ',') AS joined; -- 'a,b,c'
-- 字符串转数组
SELECT STRING_TO_ARRAY('a,b,c', ',') AS arr;               -- {a,b,c}
```

**基本写法：JSON 与文本互转**
`<表达式>::jsonb` 或 `CAST(<表达式> AS JSON)`

```sql
-- 文本转 JSONB（PostgreSQL）
SELECT '{"name":"张三"}'::jsonb AS data;
-- JSON 提取为文本
SELECT data->>'name' AS name FROM users WHERE id = 1;
-- MySQL JSON 转文本
SELECT CAST(JSON_EXTRACT(config, '$.name') AS CHAR) AS name;
```

---

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
| SQL EXCEPT / INTERSECT 集合操作语法速查手册 | 041-ExceptIntersect | 本文的并列主题 |
| 类型转换 语法速查手册 | 042-TypeConversion | 本文自身 |
