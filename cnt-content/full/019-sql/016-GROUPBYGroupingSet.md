---
order: 55
title: 'GROUP BY与分组集'
module: sql
category: SQL
difficulty: advanced
description: 'SQL分组与分组集：GROUP BY子句、ROLLUP、CUBE、GROUPING SETS多维分析、GROUPING函数与报表生成'
author: fanquanpp
updated: '2026-08-01'
related:
  - sql/过滤条件
  - sql/聚合函数
  - sql/连接查询
  - sql/自然连接与USING
prerequisites:
  - sql/概述与标准
---
## 1. GROUP BY 基础

### 1.1 分组原理

GROUP BY 将结果集按指定列的值分组，每组生成一行汇总结果。

```sql
-- 单列分组
SELECT dept_id, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id;

-- 多列分组
SELECT dept_id, job_title, COUNT(*) AS emp_count
FROM employees
GROUP BY dept_id, job_title;
```

### 1.2 分组规则

- SELECT 中的非聚合列必须出现在 GROUP BY 中
- GROUP BY 列的 NULL 值被归为同一组
- GROUP BY 可以使用表达式

```sql
-- 按表达式分组
SELECT
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    COUNT(*) AS order_count
FROM orders
GROUP BY EXTRACT(YEAR FROM created_at), EXTRACT(MONTH FROM created_at);
```

## 2. GROUPING SETS

### 2.1 概念

GROUPING SETS 允许在一次查询中指定多个分组集，相当于多个 GROUP BY 查询的 UNION ALL。

```sql
-- 等价于两个 GROUP BY 的 UNION ALL
SELECT dept_id, job_title, COUNT(*) AS emp_count
FROM employees
GROUP BY GROUPING SETS (
    (dept_id),           -- 按部门分组
    (job_title)          -- 按职位分组
);
-- 等价于：
SELECT dept_id, NULL AS job_title, COUNT(*) AS emp_count
FROM employees GROUP BY dept_id
UNION ALL
SELECT NULL AS dept_id, job_title, COUNT(*) AS emp_count
FROM employees GROUP BY job_title;
```

### 2.2 多维分组集

```sql
-- 多个分组集组合
SELECT dept_id, job_title, COUNT(*) AS emp_count
FROM employees
GROUP BY GROUPING SETS (
    (dept_id, job_title),   -- 部门×职位交叉分组
    (dept_id),              -- 仅按部门
    (job_title),            -- 仅按职位
    ()                      -- 总计
);
```

## 3. ROLLUP

### 3.1 概念

ROLLUP 按层级递减生成分组集，用于生成小计和总计行。

```sql
-- ROLLUP(dept_id, job_title) 生成以下分组集：
-- 1. (dept_id, job_title)  -- 最细粒度
-- 2. (dept_id)             -- 部门小计
-- 3. ()                    -- 总计

SELECT
    dept_id,
    job_title,
    COUNT(*) AS emp_count,
    SUM(salary) AS total_salary
FROM employees
GROUP BY ROLLUP (dept_id, job_title);
```

**输出示例**：

| dept_id | job_title | emp_count | total_salary |
| ------- | --------- | --------- | ------------ | ---------- |
| 1 | Engineer | 10 | 1000000 |
| 1 | Manager | 3 | 450000 |
| 1 | NULL | 13 | 1450000 | ← 部门小计 |
| 2 | Engineer | 8 | 800000 |
| 2 | NULL | 8 | 800000 | ← 部门小计 |
| NULL | NULL | 21 | 2250000 | ← 总计 |

### 3.2 三级 ROLLUP

```sql
-- ROLLUP(year, quarter, month)
SELECT
    EXTRACT(YEAR FROM created_at) AS yr,
    EXTRACT(QUARTER FROM created_at) AS qtr,
    EXTRACT(MONTH FROM created_at) AS mon,
    SUM(amount) AS total
FROM orders
GROUP BY ROLLUP (
    EXTRACT(YEAR FROM created_at),
    EXTRACT(QUARTER FROM created_at),
    EXTRACT(MONTH FROM created_at)
);
-- 生成分组集：(yr,qtr,mon), (yr,qtr), (yr), ()
```

## 4. CUBE

### 4.1 概念

CUBE 生成所有可能的分组集组合，用于多维数据分析。

```sql
-- CUBE(dept_id, job_title) 生成以下分组集：
-- 1. (dept_id, job_title)  -- 交叉分组
-- 2. (dept_id)             -- 按部门
-- 3. (job_title)           -- 按职位
-- 4. ()                    -- 总计

SELECT
    dept_id,
    job_title,
    COUNT(*) AS emp_count
FROM employees
GROUP BY CUBE (dept_id, job_title);
```

### 4.2 CUBE 的分组集数量

$n$ 列的 CUBE 生成 $2^n$ 个分组集：

| 列数 | 分组集数量 | 说明                                            |
| ---- | ---------- | ----------------------------------------------- |
| 2    | 4          | (a,b), (a), (b), ()                             |
| 3    | 8          | (a,b,c), (a,b), (a,c), (b,c), (a), (b), (c), () |
| 4    | 16         | 注意性能影响                                    |

```sql
-- 三维 CUBE
SELECT region, dept_id, job_title, SUM(salary) AS total
FROM employees
GROUP BY CUBE (region, dept_id, job_title);
-- 生成 2^3 = 8 个分组集
```

## 5. GROUPING 函数

### 5.1 识别小计与总计行

GROUPING 函数返回 0 或 1，指示某列是否因分组集而被聚合为 NULL：

- `GROUPING(col) = 0`：该列有实际值
- `GROUPING(col) = 1`：该列因分组集而被聚合为 NULL

```sql
SELECT
    dept_id,
    job_title,
    COUNT(*) AS emp_count,
    GROUPING(dept_id) AS is_dept_subtotal,
    GROUPING(job_title) AS is_job_subtotal
FROM employees
GROUP BY ROLLUP (dept_id, job_title);
```

| dept_id | job_title | emp_count | is_dept_subtotal | is_job_subtotal |
| ------- | --------- | --------- | ---------------- | --------------- | ---------- |
| 1 | Engineer | 10 | 0 | 0 |
| 1 | NULL | 13 | 0 | 1 | ← 部门小计 |
| NULL | NULL | 21 | 1 | 1 | ← 总计 |

### 5.2 使用 GROUPING ID

```sql
-- GROUPING_ID：将所有 GROUPING 位组合为整数
-- GROUPING_ID(dept_id, job_title)
-- = GROUPING(dept_id) * 2 + GROUPING(job_title) * 1

SELECT
    dept_id,
    job_title,
    COUNT(*) AS emp_count,
    GROUPING_ID(dept_id, job_title) AS grouping_id
FROM employees
GROUP BY ROLLUP (dept_id, job_title);

-- grouping_id 含义：
-- 0 = (dept_id, job_title)  最细粒度
-- 1 = (dept_id)             部门小计
-- 3 = ()                    总计
```

### 5.3 格式化报表输出

```sql
SELECT
    CASE WHEN GROUPING(dept_id) = 1 THEN '【总计】'
         ELSE dept_id::TEXT END AS dept,
    CASE WHEN GROUPING(job_title) = 1 THEN '【小计】'
         ELSE job_title END AS job,
    COUNT(*) AS emp_count,
    SUM(salary) AS total_salary
FROM employees
GROUP BY ROLLUP (dept_id, job_title)
ORDER BY GROUPING(dept_id), dept_id, GROUPING(job_title), job_title;
```

## 6. 组合使用

### 6.1 混合 ROLLUP 和 CUBE

```sql
SELECT
    region,
    dept_id,
    job_title,
    SUM(salary) AS total
FROM employees
GROUP BY
    region,
    ROLLUP (dept_id, job_title);
-- 等价于 GROUPING SETS (
--     (region, dept_id, job_title),
--     (region, dept_id),
--     (region)
-- )
```

### 6.2 多个 ROLLUP/CUBE

```sql
SELECT
    region,
    dept_id,
    job_title,
    SUM(salary) AS total
FROM employees
GROUP BY
    ROLLUP (region),
    ROLLUP (dept_id, job_title);
-- 等价于两个 ROLLUP 的交叉积
```

## 7. 性能考量

### 7.1 分组集数量控制

```sql
-- CUBE(5列) = 32个分组集，数据量大时性能堪忧
-- 优化：拆分为多个查询或使用 GROUPING SETS 精确指定

-- 替代 CUBE(a, b, c, d, e)
GROUP BY GROUPING SETS (
    (a, b, c),     -- 只需这三个关键分组
    (a, b),
    (a, c),
    (b, c),
    ()
)
```

### 7.2 物化视图与预聚合

```sql
-- PostgreSQL 物化视图
CREATE MATERIALIZED VIEW sales_summary AS
SELECT
    region, dept_id,
    DATE_TRUNC('month', created_at) AS month,
    SUM(amount) AS total,
    COUNT(*) AS cnt
FROM sales
GROUP BY region, dept_id, DATE_TRUNC('month', created_at);

-- 刷新物化视图
REFRESH MATERIALIZED VIEW CONCURRENTLY sales_summary;
```
## 基本分组

**基本写法：单列分组**
`GROUP BY <列>`
```sql
-- 按部门分组统计人数
SELECT dept, COUNT(*) AS emp_count
FROM employees
GROUP BY dept;
```

---

**基本写法：多列分组**
`GROUP BY <列1>, <列2>`
```sql
-- 按部门和职位分组
SELECT dept, job_title, COUNT(*) AS cnt, AVG(salary) AS avg_sal
FROM employees
GROUP BY dept, job_title;
```

---

**基本写法：HAVING 过滤分组**
`GROUP BY <列> HAVING <聚合条件>`
```sql
-- 只显示人数大于 5 的部门
SELECT dept, COUNT(*) AS cnt
FROM employees
GROUP BY dept
HAVING COUNT(*) > 5;
```

---

## ROLLUP 上卷汇总

**基本写法：ROLLUP 多级汇总**
`GROUP BY ROLLUP(<列1>, <列2>)`
```sql
-- 按部门、职位汇总，并生成各级小计与总计
SELECT dept, job_title, COUNT(*) AS cnt, SUM(salary) AS total
FROM employees
GROUP BY ROLLUP(dept, job_title);
-- 结果包含：
--   每个 (dept, job_title) 组合的统计
--   每个 dept 的小计（job_title 为 NULL）
--   总计（dept 和 job_title 均为 NULL）
```

---

**基本写法：单列 ROLLUP**
`GROUP BY ROLLUP(<列>)`
```sql
-- 单列 ROLLUP 等价于分组 + 总计行
SELECT dept, SUM(salary) AS total
FROM employees
GROUP BY ROLLUP(dept);
```

---

## CUBE 立方体汇总

**基本写法：CUBE 全组合汇总**
`GROUP BY CUBE(<列1>, <列2>)`
```sql
-- 生成所有维度的交叉汇总
SELECT dept, job_title, COUNT(*) AS cnt
FROM employees
GROUP BY CUBE(dept, job_title);
-- 结果包含：
--   (dept, job_title) 组合统计
--   每个 dept 的小计
--   每个 job_title 的小计
--   总计
```

---

**基本写法：三列 CUBE**
`GROUP BY CUBE(<列1>, <列2>, <列3>)`
```sql
-- 三维交叉汇总
SELECT year, quarter, region, SUM(sales) AS total
FROM sales_data
GROUP BY CUBE(year, quarter, region);
```

---

## GROUPING SETS 分组集合

**基本写法：指定分组集合**
`GROUP BY GROUPING SETS((<列组合1>), (<列组合2>))`
```sql
-- 分别按部门和按职位分组统计
SELECT dept, job_title, COUNT(*) AS cnt
FROM employees
GROUP BY GROUPING SETS(
  (dept),
  (job_title)
);
-- 等价于 UNION ALL 两条查询
```

---

**基本写法：包含空集（总计行）**
`GROUP BY GROUPING SETS((<列>), ())`
```sql
-- 分组统计 + 总计行
SELECT dept, COUNT(*) AS cnt
FROM employees
GROUP BY GROUPING SETS((dept), ());
```

---

**基本写法：多组合分组**
`GROUP BY GROUPING SETS((<列1>, <列2>), (<列1>), (<列2>), ())`
```sql
-- 灵活指定多级分组
SELECT dept, job_title, COUNT(*) AS cnt
FROM employees
GROUP BY GROUPING SETS(
  (dept, job_title),
  (dept),
  (job_title),
  ()
);
```

---

## GROUPING 函数

**基本写法：区分 NULL 与汇总行**
`GROUPING(<列>)`
```sql
-- GROUPING 返回 1 表示该 NULL 是汇总行，0 表示实际 NULL
SELECT
  dept,
  CASE WHEN GROUPING(dept) = 1 THEN '总计' ELSE dept END AS dept_name,
  COUNT(*) AS cnt
FROM employees
GROUP BY ROLLUP(dept);
```

---

**基本写法：多列 GROUPING**
`GROUPING(<列1>), GROUPING(<列2>)`
```sql
-- 区分各级汇总
SELECT
  CASE WHEN GROUPING(dept) = 1 THEN '全部部门' ELSE dept END AS dept,
  CASE WHEN GROUPING(job_title) = 1 THEN '全部职位' ELSE job_title END AS job,
  COUNT(*) AS cnt
FROM employees
GROUP BY ROLLUP(dept, job_title);
```

---

## 聚合函数组合

**基本写法：多聚合函数**
`SELECT <列>, COUNT(*), SUM(<列>), AVG(<列>), MIN(<列>), MAX(<列>)`
```sql
-- 常用聚合函数组合
SELECT dept,
  COUNT(*) AS emp_count,
  SUM(salary) AS total_salary,
  AVG(salary) AS avg_salary,
  MIN(salary) AS min_salary,
  MAX(salary) AS max_salary
FROM employees
GROUP BY dept;
```

---

**基本写法：COUNT 不同值**
`COUNT(DISTINCT <列>)`
```sql
-- 统计每个部门的不同职位数
SELECT dept, COUNT(DISTINCT job_title) AS job_count
FROM employees
GROUP BY dept;
```

---

**基本写法：字符串聚合**
`GROUP_CONCAT(<列> [SEPARATOR '<分隔>'])`
```sql
-- MySQL：将分组中的字符串拼接
SELECT dept, GROUP_CONCAT(name SEPARATOR ', ') AS all_names
FROM employees
GROUP BY dept;
```

---

**基本写法：PostgreSQL 字符串聚合**
`STRING_AGG(<列>, '<分隔>')`
```sql
-- PostgreSQL：字符串拼接
SELECT dept, STRING_AGG(name, ', ' ORDER BY name) AS all_names
FROM employees
GROUP BY dept;
```

---

## 条件聚合

**基本写法：CASE WHEN 与聚合**
`SUM(CASE WHEN <条件> THEN 1 ELSE 0 END)`
```sql
-- 按条件统计不同类别
SELECT dept,
  SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_count,
  SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count
FROM employees
GROUP BY dept;
```

---

**基本写法：条件平均值**
`AVG(CASE WHEN <条件> THEN <列> END)`
```sql
-- 计算不同条件的平均值
SELECT dept,
  AVG(CASE WHEN job_title = 'Engineer' THEN salary END) AS eng_avg,
  AVG(CASE WHEN job_title = 'Manager' THEN salary END) AS mgr_avg
FROM employees
GROUP BY dept;
```

---

## FILTER 子句（PostgreSQL）

**基本写法：FILTER 条件聚合**
`<聚合函数>(<列>) FILTER (WHERE <条件>)`
```sql
-- PostgreSQL/SQL Standard 条件聚合
SELECT dept,
  COUNT(*) AS total,
  COUNT(*) FILTER (WHERE salary > 50000) AS high_paid,
  AVG(salary) FILTER (WHERE status = 'active') AS active_avg
FROM employees
GROUP BY dept;
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
| GROUP BY与分组集 | 016-GROUPBYGroupingSet | 本文自身 |
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
| 类型转换 语法速查手册 | 042-TypeConversion | 本文的并列主题 |
