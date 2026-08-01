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

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《GROUP BY与分组集》，属于 SQL 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 SQL 的核心概念、语法与常用对象。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 SQL 的执行原理与优化机制。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写正确、高效的 SQL 语句与操作。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 SQL 相关方案在性能与一致性上的权衡。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据业务场景评价 SQL 技术选型。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 SQL 与其他技术设计数据架构。

通过本节学习，读者应当能够把《GROUP BY与分组集》纳入自己的知识网络，并与 SQL 模块的其他主题（DDL/DML、查询、索引、事务）建立关联。

## 2. 历史动机与发展脉络

《GROUP BY与分组集》是 SQL 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

SQL（结构化查询语言）源于 1970 年 Codd 的关系模型，1974 年由 Chamberlin 与 Boyce 设计（SEQUEL），1986 年成为 ANSI 标准；SQL:2023 是当前国际标准。
SQL 分为 DDL（建表）、DML（增删改）、DQL（查询）、DCL（权限）与 TCL（事务）；各大数据库在标准基础上扩展方言。
SQL 是声明式语言：描述“要什么”而非“怎么做”，优化器负责执行计划；这一设计让 SQL 具有跨数据库的表达一致性。

回到本文主题：GROUP BY与分组集 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《GROUP BY与分组集》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。
查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。
事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 15 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# SQL GROUP BY 与分组集合 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. GROUP BY 基础

##### 1.1 分组原理

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

##### 1.2 分组规则

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

#### 2. GROUPING SETS

##### 2.1 概念

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

##### 2.2 多维分组集

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

#### 3. ROLLUP

##### 3.1 概念

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

##### 3.2 三级 ROLLUP

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

#### 4. CUBE

##### 4.1 概念

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

##### 4.2 CUBE 的分组集数量

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

#### 5. GROUPING 函数

##### 5.1 识别小计与总计行

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

##### 5.2 使用 GROUPING ID

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

##### 5.3 格式化报表输出

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

#### 6. 组合使用

##### 6.1 混合 ROLLUP 和 CUBE

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

##### 6.2 多个 ROLLUP/CUBE

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

#### 7. 性能考量

##### 7.1 分组集数量控制

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

##### 7.2 物化视图与预聚合

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
#### 基本分组

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

#### ROLLUP 上卷汇总

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

#### CUBE 立方体汇总

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

#### GROUPING SETS 分组集合

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

#### GROUPING 函数

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

#### 聚合函数组合

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

#### 条件聚合

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

#### FILTER 子句（PostgreSQL）

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


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["GROUP BY与分组集"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《GROUP BY与分组集》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。
查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。
事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。
集合语义：SELECT 返回结果集；JOIN 组合关系，GROUP BY 聚合，子查询与 CTE 表达复杂逻辑。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1.1 分组原理

该示例来自原文《1.1 分组原理》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：1.2 分组规则

该示例来自原文《1.2 分组规则》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 按表达式分组
SELECT
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    COUNT(*) AS order_count
FROM orders
GROUP BY EXTRACT(YEAR FROM created_at), EXTRACT(MONTH FROM created_at);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：2.1 概念

该示例来自原文《2.1 概念》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：2.2 多维分组集

该示例来自原文《2.2 多维分组集》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：3.1 概念

该示例来自原文《3.1 概念》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：3.2 三级 ROLLUP

该示例来自原文《3.2 三级 ROLLUP》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：4.1 概念

该示例来自原文《4.1 概念》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：4.2 CUBE 的分组集数量

该示例来自原文《4.2 CUBE 的分组集数量》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 三维 CUBE
SELECT region, dept_id, job_title, SUM(salary) AS total
FROM employees
GROUP BY CUBE (region, dept_id, job_title);
-- 生成 2^3 = 8 个分组集
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：5.1 识别小计与总计行

该示例来自原文《5.1 识别小计与总计行》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：5.2 使用 GROUPING ID

该示例来自原文《5.2 使用 GROUPING ID》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：5.3 格式化报表输出

该示例来自原文《5.3 格式化报表输出》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：6.1 混合 ROLLUP 和 CUBE

该示例来自原文《6.1 混合 ROLLUP 和 CUBE》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：6.2 多个 ROLLUP/CUBE

该示例来自原文《6.2 多个 ROLLUP/CUBE》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：7.1 分组集数量控制

该示例来自原文《7.1 分组集数量控制》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：7.2 物化视图与预聚合

该示例来自原文《7.2 物化视图与预聚合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：基本分组

该示例来自原文《基本分组》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 按部门分组统计人数
SELECT dept, COUNT(*) AS emp_count
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：基本分组

该示例来自原文《基本分组》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 按部门和职位分组
SELECT dept, job_title, COUNT(*) AS cnt, AVG(salary) AS avg_sal
FROM employees
GROUP BY dept, job_title;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：基本分组

该示例来自原文《基本分组》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 只显示人数大于 5 的部门
SELECT dept, COUNT(*) AS cnt
FROM employees
GROUP BY dept
HAVING COUNT(*) > 5;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：ROLLUP 上卷汇总

该示例来自原文《ROLLUP 上卷汇总》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：ROLLUP 上卷汇总

该示例来自原文《ROLLUP 上卷汇总》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 单列 ROLLUP 等价于分组 + 总计行
SELECT dept, SUM(salary) AS total
FROM employees
GROUP BY ROLLUP(dept);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：CUBE 立方体汇总

该示例来自原文《CUBE 立方体汇总》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：CUBE 立方体汇总

该示例来自原文《CUBE 立方体汇总》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 三维交叉汇总
SELECT year, quarter, region, SUM(sales) AS total
FROM sales_data
GROUP BY CUBE(year, quarter, region);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：GROUPING SETS 分组集合

该示例来自原文《GROUPING SETS 分组集合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：GROUPING SETS 分组集合

该示例来自原文《GROUPING SETS 分组集合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 分组统计 + 总计行
SELECT dept, COUNT(*) AS cnt
FROM employees
GROUP BY GROUPING SETS((dept), ());
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：GROUPING SETS 分组集合

该示例来自原文《GROUPING SETS 分组集合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：GROUPING 函数

该示例来自原文《GROUPING 函数》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- GROUPING 返回 1 表示该 NULL 是汇总行，0 表示实际 NULL
SELECT
  dept,
  CASE WHEN GROUPING(dept) = 1 THEN '总计' ELSE dept END AS dept_name,
  COUNT(*) AS cnt
FROM employees
GROUP BY ROLLUP(dept);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：GROUPING 函数

该示例来自原文《GROUPING 函数》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 区分各级汇总
SELECT
  CASE WHEN GROUPING(dept) = 1 THEN '全部部门' ELSE dept END AS dept,
  CASE WHEN GROUPING(job_title) = 1 THEN '全部职位' ELSE job_title END AS job,
  COUNT(*) AS cnt
FROM employees
GROUP BY ROLLUP(dept, job_title);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：聚合函数组合

该示例来自原文《聚合函数组合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.29 示例：聚合函数组合

该示例来自原文《聚合函数组合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 统计每个部门的不同职位数
SELECT dept, COUNT(DISTINCT job_title) AS job_count
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.30 示例：聚合函数组合

该示例来自原文《聚合函数组合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- MySQL：将分组中的字符串拼接
SELECT dept, GROUP_CONCAT(name SEPARATOR ', ') AS all_names
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.31 示例：聚合函数组合

该示例来自原文《聚合函数组合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL：字符串拼接
SELECT dept, STRING_AGG(name, ', ' ORDER BY name) AS all_names
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.32 示例：条件聚合

该示例来自原文《条件聚合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 按条件统计不同类别
SELECT dept,
  SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_count,
  SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.33 示例：条件聚合

该示例来自原文《条件聚合》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 计算不同条件的平均值
SELECT dept,
  AVG(CASE WHEN job_title = 'Engineer' THEN salary END) AS eng_avg,
  AVG(CASE WHEN job_title = 'Manager' THEN salary END) AS mgr_avg
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.34 示例：FILTER 子句（PostgreSQL）

该示例来自原文《FILTER 子句（PostgreSQL）》小节，用于演示GROUP BY与分组集相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL/SQL Standard 条件聚合
SELECT dept,
  COUNT(*) AS total,
  COUNT(*) FILTER (WHERE salary > 50000) AS high_paid,
  AVG(salary) FILTER (WHERE status = 'active') AS active_avg
FROM employees
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《GROUP BY与分组集》定位的最快路径。下面从多个维度与相邻方案进行对比。

SQL 与 NoSQL：SQL 适合关系与事务，NoSQL（文档/键值/宽表）适合弹性扩展与特定模型；混合架构常见。
MySQL 与 PostgreSQL：MySQL 生态普及、复制成熟；PostgreSQL 功能全面（窗口、JSON、扩展）。
存储过程与业务代码：复杂逻辑放应用层更可测试；存储过程适合强封装场景。

对比的目的不是分出绝对优劣，而是建立选择依据：不同约束条件下，最优解不同。读者应把每个对比维度转化为决策检查清单。

## 7. 常见陷阱与最佳实践

本节整理该主题的高频错误与推荐做法。每个陷阱先描述现象，再解释原因，最后给出最佳实践。

### 7.1 SELECT * 滥用

返回多余列浪费带宽且破坏视图依赖。显式列出所需列。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，SELECT * 滥用 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，SELECT * 滥用 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理SELECT * 滥用的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.2 隐式类型转换

字符串与数字比较走转换，索引失效。保持类型一致。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，隐式类型转换 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，隐式类型转换 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理隐式类型转换的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.3 函数包裹索引列

WHERE DATE(ts)=... 无法用索引。使用范围条件。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，函数包裹索引列 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，函数包裹索引列 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理函数包裹索引列的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.4 分页偏移过大

OFFSET 大时扫描大量行。使用游标或键集分页。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，分页偏移过大 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，分页偏移过大 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理分页偏移过大的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.5 事务内做慢查询

长事务锁资源。事务保持短小。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，事务内做慢查询 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，事务内做慢查询 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理事务内做慢查询的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.6 N+1 查询

循环查库。使用 JOIN 或批量查询。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，N+1 查询 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，N+1 查询 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理N+1 查询的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.7 不设外键约束

应用层维护引用完整性易漏。关键关系使用外键。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，不设外键约束 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，不设外键约束 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理不设外键约束的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.8 忽略执行计划

凭直觉优化。用 EXPLAIN 验证。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，忽略执行计划 一般源于对 SQL 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，忽略执行计划 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理忽略执行计划的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.0 最佳实践总览

1. 命名规范：表名复数或单数统一，列名小写下划线，主键 id。
2. 每个表必须有主键，时间戳列记录变更。
3. 查询先 WHERE 缩小数据量，再 JOIN 与聚合。
4. 迁移脚本版本化，变更可回滚。
5. 生产查询全部过 EXPLAIN 与慢日志检查。

把这些最佳实践固化为团队规范与代码评审检查项，是避免同类问题反复出现的关键。

## 8. 工程实践

本节把《GROUP BY与分组集》放入真实工程场景，给出可复用的模式与组织方法。

连接池管理数据库连接；迁移工具（Flyway/Alembic）版本化 schema。
读写分离与分库分表按量级引入；缓存（Redis）承担热数据。
监控：慢查询日志、连接数、QPS、复制延迟。

### 8.1 工程实践的原则拆解

以上工程实践可以归纳为四条原则。第一，配置与代码分离：SQL 项目中环境差异应通过配置注入，而不是散落在代码分支中；这保证同一份代码可以在开发、测试、生产环境一致运行。

第二，接口稳定优先：对外接口（函数签名、协议、数据格式）一旦被消费方依赖，变更成本极高；设计时应预留扩展点并保持向后兼容。

第三，可观测性内置：日志、指标与追踪应该在功能开发时同步设计，而不是故障发生后补救；没有观测手段的模块等于黑盒。

第四，变更可回滚：任何发布都应有对应的回滚方案；数据库迁移、配置变更与代码发布一样需要版本管理与逆向路径。

### 8.2 实践落地的检查清单

- [ ] 实践 1：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 实践 2：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 监控：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。

工程实践的共性原则：配置与代码分离、接口稳定优先、可观测性内置、变更可回滚。这些原则适用于本主题的所有实现。

## 9. 案例研究

本节通过一个完整案例把《GROUP BY与分组集》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

需求：为订单系统设计表结构与核心查询。
方案：订单主表 + 明细表 + 用户表；事务保证一致；索引覆盖高频查询。
要点：金额用 decimal；状态用枚举；时间用 UTC；分页用键集。
验证：EXPLAIN 检查索引；并发插入测试唯一约束；压测查询延迟。

### 9.1 案例的扩展讨论

把案例中的方案放大到真实规模，需要额外考虑三个问题：

第一，规模：当数据量或并发量上升一个数量级时，原方案中的数据结构、缓存策略与任务调度是否仍然成立？通常需要引入分层与异步。

第二，团队：多人协作时，模块边界、接口契约与代码所有权必须明确；案例中的实现应拆分为可独立测试的单元，并配合文档说明设计意图。

第三，演进：上线后的需求变化不可避免；方案设计时应预留扩展点（配置化、插件化、事件化），并定期用真实指标验证假设。


案例研究的学习方法：先独立阅读需求，尝试在脑中形成方案，再对照实现与讲解，最后思考“如果约束变化（数据量、并发、团队规模），方案应如何调整”。

## 10. 知识要点总结与深入讲解

本节以讲解形式汇总全文要点，替代传统的习题与自测，读者不需要答题，只需跟随解释建立完整的认知框架。

关于《GROUP BY与分组集》的核心结论：

SQL 的声明式表达力建立在关系代数之上，理解集合思维是进阶关键。
索引、执行计划与事务是三大实战主题。
工程化：迁移、连接池、监控与慢查询治理缺一不可。

原文档各小节的要点回顾：

- 1. GROUP BY 基础：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. GROUPING SETS：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. ROLLUP：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. CUBE：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. GROUPING 函数：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 组合使用：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 7. 性能考量：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 基本分组：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- ROLLUP 上卷汇总：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- CUBE 立方体汇总：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- GROUPING SETS 分组集合：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- GROUPING 函数：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 聚合函数组合：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 条件聚合：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- FILTER 子句（PostgreSQL）：该小节围绕GROUP BY与分组集展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

把以上要点与第 3-9 节的内容对照复习，即可完成对本文主题的闭环学习。

## 11. 参考文献


SQL 标准（ISO/IEC 9075）：https://www.iso.org/standard/76583.html
PostgreSQL 文档（SQL 章节）：https://www.postgresql.org/docs/current/sql.html
MySQL 文档：https://dev.mysql.com/doc/
SQLite 文档：https://www.sqlite.org/docs.html
Use The Index, Luke：https://use-the-index-luke.com/

## 12. 延伸阅读


SQL 连接与子查询，见 019-sql 模块文档。
SQL 自连接与递归，见 019-sql/019-SelfJoin 文档。
MySQL 深入，见 020-mysql 模块。
PostgreSQL 深入，见 021-postgresql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 课程。

## 14. 模块知识图谱与学习路径

本文属于 SQL 模块。为了把《GROUP BY与分组集》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["GROUP BY与分组集"]
    N0["概述与标准"]
    N1["数据查询基础"]
    N0 --> N1
    N2["多表查询"]
    N1 --> N2
    N3["数据操作"]
    N2 --> N3
    N4["数据定义"]
    N3 --> N4
    N5["窗口函数"]
    N4 --> N5
    N6["高级查询"]
    N5 --> N6
    N7["性能优化"]
    N6 --> N7
    N8["PL-SQL与存储过程"]
    N7 --> N8
    N9["SQL实战与面试"]
    N8 --> N9
    N10["数据类型"]
    N9 --> N10
    N11["约束"]
    N10 --> N11
    N12["SELECT执行顺序"]
    N11 --> N12
    N13["过滤条件"]
    N12 --> N13
```

上图为模块主题的推荐学习顺序示意图（仅展示前若干主题）。各主题之间存在三类关联：

第一，前置依赖关系：早期主题是后期主题的基础，例如环境与语法先行、进阶主题随后；

第二，横向并列关系：同一层级主题从不同角度覆盖模块能力，学习顺序可以按兴趣调整；

第三，工程组合关系：多个主题在真实项目中组合使用，例如配置、性能与安全主题往往出现在同一系统的不同层面。

### 14.1 模块主题速查表

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

速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。

## 15. 术语表

下表整理《GROUP BY与分组集》及 SQL 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

| 术语 | 释义 |
| --- | --- |
| 关系模型 | 表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。 |
| 查询执行 | 解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。 |
| 事务 ACID | 原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。 |
| 集合语义 | SELECT 返回结果集；JOIN 组合关系，GROUP BY 聚合，子查询与 CTE 表达复杂逻辑。 |
| SELECT * 滥用（易错点） | 参见常见陷阱章节的详细讲解 |
| 隐式类型转换（易错点） | 参见常见陷阱章节的详细讲解 |
| 函数包裹索引列（易错点） | 参见常见陷阱章节的详细讲解 |
| 分页偏移过大（易错点） | 参见常见陷阱章节的详细讲解 |
| 事务内做慢查询（易错点） | 参见常见陷阱章节的详细讲解 |
| N+1 查询（易错点） | 参见常见陷阱章节的详细讲解 |

术语表与正文配合使用：先通读正文，遇到模糊术语回查本表；长期使用后术语会自然进入工作记忆。
