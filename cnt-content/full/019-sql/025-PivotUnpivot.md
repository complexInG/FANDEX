---
order: 64
title: PIVOT与UNPIVOT
module: sql
category: SQL
difficulty: advanced
description: 'SQL PIVOT与UNPIVOT：行列转换的语法、条件聚合实现、跨数据库兼容方案与性能优化'
author: fanquanpp
updated: '2026-08-01'
related:
  - sql/公用表表达式
  - sql/递归CTE
  - sql/集合操作
  - sql/数据控制语言
prerequisites:
  - sql/概述与标准
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《PIVOT与UNPIVOT》，属于 SQL 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 SQL 的核心概念、语法与常用对象。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 SQL 的执行原理与优化机制。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写正确、高效的 SQL 语句与操作。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 SQL 相关方案在性能与一致性上的权衡。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据业务场景评价 SQL 技术选型。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 SQL 与其他技术设计数据架构。

通过本节学习，读者应当能够把《PIVOT与UNPIVOT》纳入自己的知识网络，并与 SQL 模块的其他主题（DDL/DML、查询、索引、事务）建立关联。

## 2. 历史动机与发展脉络

《PIVOT与UNPIVOT》是 SQL 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

SQL（结构化查询语言）源于 1970 年 Codd 的关系模型，1974 年由 Chamberlin 与 Boyce 设计（SEQUEL），1986 年成为 ANSI 标准；SQL:2023 是当前国际标准。
SQL 分为 DDL（建表）、DML（增删改）、DQL（查询）、DCL（权限）与 TCL（事务）；各大数据库在标准基础上扩展方言。
SQL 是声明式语言：描述“要什么”而非“怎么做”，优化器负责执行计划；这一设计让 SQL 具有跨数据库的表达一致性。

回到本文主题：PIVOT与UNPIVOT 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《PIVOT与UNPIVOT》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。
查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。
事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 8 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# SQL 行列转换（Pivot/Unpivot） 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. 行列转换概述

- **PIVOT（行转列）**：将行数据旋转为列，常用于交叉报表
- **UNPIVOT（列转行）**：将列数据旋转为行，常用于数据规范化

#### 2. PIVOT 行转列

##### 2.1 条件聚合实现（通用方法）

所有数据库都支持的条件聚合方法：

```sql
-- 原始数据：季度收入
-- | dept_id | quarter | revenue |
-- |---------|---------|---------|
-- | 1       | Q1      | 100     |
-- | 1       | Q2      | 150     |

-- 行转列：每个部门一行，季度为列
SELECT
    dept_id,
    SUM(CASE WHEN quarter = 'Q1' THEN revenue ELSE 0 END) AS q1,
    SUM(CASE WHEN quarter = 'Q2' THEN revenue ELSE 0 END) AS q2,
    SUM(CASE WHEN quarter = 'Q3' THEN revenue ELSE 0 END) AS q3,
    SUM(CASE WHEN quarter = 'Q4' THEN revenue ELSE 0 END) AS q4
FROM quarterly_revenue
GROUP BY dept_id;

-- 结果：
-- | dept_id | q1  | q2  | q3  | q4  |
-- |---------|-----|-----|-----|-----|
-- | 1       | 100 | 150 | 200 | 180 |
```

##### 2.2 SQL Server PIVOT 语法

```sql
-- SQL Server 专用 PIVOT 语法
SELECT dept_id, [Q1], [Q2], [Q3], [Q4]
FROM quarterly_revenue
PIVOT (
    SUM(revenue)
    FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS p;
```

##### 2.3 PostgreSQL crosstab

```sql
-- PostgreSQL: tablefunc 扩展
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT *
FROM crosstab(
    'SELECT dept_id, quarter, revenue
     FROM quarterly_revenue
     ORDER BY 1, 2'
) AS ct (dept_id INTEGER, q1 NUMERIC, q2 NUMERIC, q3 NUMERIC, q4 NUMERIC);
```

##### 2.4 动态 PIVOT

```sql
-- 列值不固定时，需要动态 SQL
-- PostgreSQL 示例
DO $$
DECLARE
    pivot_cols TEXT;
    query TEXT;
BEGIN
    SELECT STRING_AGG(DISTINCT quote_ident(quarter), ', ')
    INTO pivot_cols
    FROM quarterly_revenue;

    query := format('
        SELECT dept_id, %s
        FROM quarterly_revenue
        PIVOT (SUM(revenue) FOR quarter IN (%s)) AS p
    ', pivot_cols, pivot_cols);

    EXECUTE query;
END $$;
```

##### 2.5 多值 PIVOT

```sql
-- 同时转换多个度量
SELECT
    dept_id,
    SUM(CASE WHEN quarter = 'Q1' THEN revenue ELSE 0 END) AS q1_revenue,
    SUM(CASE WHEN quarter = 'Q1' THEN cost ELSE 0 END) AS q1_cost,
    SUM(CASE WHEN quarter = 'Q2' THEN revenue ELSE 0 END) AS q2_revenue,
    SUM(CASE WHEN quarter = 'Q2' THEN cost ELSE 0 END) AS q2_cost
FROM quarterly_data
GROUP BY dept_id;
```

#### 3. UNPIVOT 列转行

##### 3.1 UNION ALL 实现（通用方法）

```sql
-- 原始数据：
-- | dept_id | q1  | q2  | q3  | q4  |
-- |---------|-----|-----|-----|-----|
-- | 1       | 100 | 150 | 200 | 180 |

-- 列转行
SELECT dept_id, 'Q1' AS quarter, q1 AS revenue FROM wide_data
UNION ALL
SELECT dept_id, 'Q2', q2 FROM wide_data
UNION ALL
SELECT dept_id, 'Q3', q3 FROM wide_data
UNION ALL
SELECT dept_id, 'Q4', q4 FROM wide_data;

-- 结果：
-- | dept_id | quarter | revenue |
-- |---------|---------|---------|
-- | 1       | Q1      | 100     |
-- | 1       | Q2      | 150     |
-- | 1       | Q3      | 200     |
-- | 1       | Q4      | 180     |
```

##### 3.2 SQL Server UNPIVOT 语法

```sql
SELECT dept_id, quarter, revenue
FROM wide_data
UNPIVOT (
    revenue FOR quarter IN (q1, q2, q3, q4)
) AS u;
```

##### 3.3 PostgreSQL 使用 VALUES + LATERAL

```sql
SELECT t.dept_id, v.quarter, v.revenue
FROM wide_data t,
LATERAL (VALUES
    ('Q1', t.q1),
    ('Q2', t.q2),
    ('Q3', t.q3),
    ('Q4', t.q4)
) AS v(quarter, revenue)
WHERE v.revenue IS NOT NULL;  -- 排除 NULL 值
```

##### 3.4 UNPIVOT 与 NULL 处理

```sql
-- UNION ALL 保留 NULL
SELECT dept_id, 'Q1' AS quarter, q1 AS revenue FROM wide_data
UNION ALL
SELECT dept_id, 'Q2', q2 FROM wide_data;

-- SQL Server UNPIVOT 自动排除 NULL
SELECT dept_id, quarter, revenue
FROM wide_data
UNPIVOT (revenue FOR quarter IN (q1, q2, q3, q4)) AS u;
-- NULL 值的行不会出现在结果中

-- 如需保留 NULL，使用 CROSS APPLY
SELECT t.dept_id, v.quarter, v.revenue
FROM wide_data t
CROSS APPLY (VALUES
    ('Q1', t.q1), ('Q2', t.q2), ('Q3', t.q3), ('Q4', t.q4)
) v(quarter, revenue);
```

#### 4. 实际应用场景

##### 4.1 月度报表

```sql
-- 按月展示销售数据
SELECT
    product_name,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 1  THEN amount ELSE 0 END) AS jan,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 2  THEN amount ELSE 0 END) AS feb,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 3  THEN amount ELSE 0 END) AS mar,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 4  THEN amount ELSE 0 END) AS apr,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 5  THEN amount ELSE 0 END) AS may,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 6  THEN amount ELSE 0 END) AS jun
FROM sales
WHERE EXTRACT(YEAR FROM order_date) = 2026
GROUP BY product_name;
```

##### 4.2 用户属性宽表

```sql
-- 将 EAV 模型转为宽表
-- 原始：user_id | attribute | value
-- 目标：user_id | age | gender | city

SELECT
    user_id,
    MAX(CASE WHEN attribute = 'age' THEN value END)::INTEGER AS age,
    MAX(CASE WHEN attribute = 'gender' THEN value END) AS gender,
    MAX(CASE WHEN attribute = 'city' THEN value END) AS city
FROM user_attributes
GROUP BY user_id;
```

##### 4.3 数据清洗：宽表转长表

```sql
-- 将1月-12月列转为行，便于分析
WITH monthly_data AS (
    SELECT id, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec_val
    from annual_data
)
SELECT
    id,
    month,
    value
FROM monthly_data
UNPIVOT (
    value FOR month IN (jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec_val)
) u;
```
#### 行转列（Pivot）

**基本写法：CASE WHEN 实现行转列**
`SELECT <分组列>, SUM(CASE WHEN <条件> THEN <值> ELSE 0 END) AS <别名> FROM <表> GROUP BY <分组列>`
```sql
-- 将行数据转为列（通用方式）
SELECT
  dept,
  SUM(CASE WHEN quarter = 'Q1' THEN sales ELSE 0 END) AS q1,
  SUM(CASE WHEN quarter = 'Q2' THEN sales ELSE 0 END) AS q2,
  SUM(CASE WHEN quarter = 'Q3' THEN sales ELSE 0 END) AS q3,
  SUM(CASE WHEN quarter = 'Q4' THEN sales ELSE 0 END) AS q4
FROM quarterly_sales
GROUP BY dept;
```

---

**基本写法：MySQL 行转列（MAX + CASE）**
`SELECT <分组列>, MAX(CASE WHEN <条件> THEN <值> END) AS <别名> FROM <表> GROUP BY <分组列>`
```sql
-- 使用 MAX 替代 SUM（适合非数值去重场景）
SELECT
  user_id,
  MAX(CASE WHEN attr = 'name' THEN value END) AS name,
  MAX(CASE WHEN attr = 'email' THEN value END) AS email,
  MAX(CASE WHEN attr = 'phone' THEN value END) AS phone
FROM user_attributes
GROUP BY user_id;
```

---

**基本写法：SQL Server PIVOT**
`SELECT * FROM (SELECT <列> FROM <表>) <别名> PIVOT (<聚合函数>(<值列>) FOR <转列> IN ([<值1>], [<值2>])) <别名>`
```sql
-- SQL Server 专用 PIVOT 语法
SELECT dept, [Q1], [Q2], [Q3], [Q4]
FROM (
  SELECT dept, quarter, sales FROM quarterly_sales
) AS src
PIVOT (
  SUM(sales) FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS pvt;
```

---

**基本写法：PostgreSQL crosstab**
`SELECT * FROM crosstab('SELECT <分组列>, <转列>, <值列> FROM <表> ORDER BY 1,2') AS <结果>(<列定义>)`
```sql
-- PostgreSQL tablefunc 扩展
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT * FROM crosstab(
  'SELECT dept, quarter, sales FROM quarterly_sales ORDER BY 1,2'
) AS result(
  dept VARCHAR,
  q1 INTEGER,
  q2 INTEGER,
  q3 INTEGER,
  q4 INTEGER
);
```

---

**基本写法：MySQL GROUP_CONCAT 行转列**
`SELECT <分组列>, GROUP_CONCAT(<列> SEPARATOR '<分隔>') FROM <表> GROUP BY <分组列>`
```sql
-- 将多行值合并为一个字符串
SELECT
  dept,
  GROUP_CONCAT(name SEPARATOR ', ') AS all_names
FROM employees
GROUP BY dept;
```

---

**基本写法：PostgreSQL STRING_AGG**
`SELECT <分组列>, STRING_AGG(<列>, '<分隔>') FROM <表> GROUP BY <分组列>`
```sql
-- PostgreSQL 字符串聚合
SELECT
  dept,
  STRING_AGG(name, ', ' ORDER BY name) AS all_names
FROM employees
GROUP BY dept;
```

---

#### 列转行（Unpivot）

**基本写法：UNION ALL 实现列转行**
`SELECT <分组列>, '<列名1>' AS <类型列>, <列1> AS <值列> FROM <表> UNION ALL SELECT <分组列>, '<列名2>', <列2> FROM <表>`
```sql
-- 将列数据转为行（通用方式）
SELECT dept, 'Q1' AS quarter, q1 AS sales FROM wide_sales
UNION ALL
SELECT dept, 'Q2' AS quarter, q2 AS sales FROM wide_sales
UNION ALL
SELECT dept, 'Q3' AS quarter, q3 AS sales FROM wide_sales
UNION ALL
SELECT dept, 'Q4' AS quarter, q4 AS sales FROM wide_sales
ORDER BY dept, quarter;
```

---

**基本写法：SQL Server UNPIVOT**
`SELECT <分组列>, <类型列>, <值列> FROM <表> UNPIVOT (<值列> FOR <类型列> IN (<列1>, <列2>)) <别名>`
```sql
-- SQL Server 专用 UNPIVOT 语法
SELECT dept, quarter, sales
FROM wide_sales
UNPIVOT (
  sales FOR quarter IN (q1, q2, q3, q4)
) AS unpvt;
```

---

**基本写法：PostgreSQL UNNEST**
`SELECT <分组列>, <类型列>, <值列> FROM <表>, UNNEST(ARRAY[<值>], ARRAY[<标签>]) AS t(<值>, <标签>)`
```sql
-- PostgreSQL 使用 UNNEST 展开数组
SELECT dept, quarter, sales
FROM wide_sales,
  UNNEST(
    ARRAY[q1, q2, q3, q4],
    ARRAY['Q1', 'Q2', 'Q3', 'Q4']
  ) AS t(sales, quarter);
```

---

#### 动态行列转换

**基本写法：动态 SQL 行转列**
`SET @sql = CONCAT('SELECT dept, ', <动态列>, ' FROM ...')`
```sql
-- MySQL 动态生成 PIVOT 查询
SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT('SUM(CASE WHEN quarter = ''', quarter,
      ''' THEN sales ELSE 0 END) AS `', quarter, '`')
  ) INTO @sql
FROM quarterly_sales;

SET @sql = CONCAT('SELECT dept, ', @sql,
  ' FROM quarterly_sales GROUP BY dept');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

---

**基本写法：PostgreSQL 动态列**
`-- 使用 JSON 聚合实现动态行转列`
```sql
-- PostgreSQL 使用 JSON 构建动态结构
SELECT
  dept,
  json_object_agg(quarter, sales) AS sales_json
FROM quarterly_sales
GROUP BY dept;
-- 结果：{"Q1": 1000, "Q2": 1500, ...}
```

---

#### 常见应用场景

**基本写法：成绩表行转列**
`SELECT student, MAX(CASE WHEN subject='数学' THEN score END) AS math, ...`
```sql
-- 学生成绩行转列
SELECT
  student,
  MAX(CASE WHEN subject = '语文' THEN score END) AS chinese,
  MAX(CASE WHEN subject = '数学' THEN score END) AS math,
  MAX(CASE WHEN subject = '英语' THEN score END) AS english
FROM scores
GROUP BY student;
```

---

**基本写法：月度统计行转列**
`SELECT year, SUM(CASE WHEN month=1 THEN amount END) AS jan, ...`
```sql
-- 月度金额统计行转列
SELECT
  year,
  SUM(CASE WHEN month = 1 THEN amount ELSE 0 END) AS jan,
  SUM(CASE WHEN month = 2 THEN amount ELSE 0 END) AS feb,
  SUM(CASE WHEN month = 3 THEN amount ELSE 0 END) AS mar,
  SUM(CASE WHEN month = 4 THEN amount ELSE 0 END) AS apr,
  SUM(CASE WHEN month = 5 THEN amount ELSE 0 END) AS may,
  SUM(CASE WHEN month = 6 THEN amount ELSE 0 END) AS jun
FROM monthly_revenue
GROUP BY year;
```

---

**基本写法：EAV 模型行转列**
`SELECT entity_id, MAX(CASE WHEN attr_name='name' THEN attr_value END) AS name, ...`
```sql
-- Entity-Attribute-Value 模型行转列
SELECT
  entity_id,
  MAX(CASE WHEN attr_name = 'name' THEN attr_value END) AS name,
  MAX(CASE WHEN attr_name = 'age' THEN attr_value END) AS age,
  MAX(CASE WHEN attr_name = 'city' THEN attr_value END) AS city
FROM eav_table
GROUP BY entity_id;
```

---

**基本写法：NULL 值处理**
`COALESCE(SUM(CASE WHEN ...), 0)`
```sql
-- 用 COALESCE 替换 NULL 为 0
SELECT
  dept,
  COALESCE(SUM(CASE WHEN quarter = 'Q1' THEN sales END), 0) AS q1,
  COALESCE(SUM(CASE WHEN quarter = 'Q2' THEN sales END), 0) AS q2
FROM quarterly_sales
GROUP BY dept;
```


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["PIVOT与UNPIVOT"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《PIVOT与UNPIVOT》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。
查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。
事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。
集合语义：SELECT 返回结果集；JOIN 组合关系，GROUP BY 聚合，子查询与 CTE 表达复杂逻辑。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：2.1 条件聚合实现（通用方法）

该示例来自原文《2.1 条件聚合实现（通用方法）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 原始数据：季度收入
-- | dept_id | quarter | revenue |
-- |---------|---------|---------|
-- | 1       | Q1      | 100     |
-- | 1       | Q2      | 150     |

-- 行转列：每个部门一行，季度为列
SELECT
    dept_id,
    SUM(CASE WHEN quarter = 'Q1' THEN revenue ELSE 0 END) AS q1,
    SUM(CASE WHEN quarter = 'Q2' THEN revenue ELSE 0 END) AS q2,
    SUM(CASE WHEN quarter = 'Q3' THEN revenue ELSE 0 END) AS q3,
    SUM(CASE WHEN quarter = 'Q4' THEN revenue ELSE 0 END) AS q4
FROM quarterly_revenue
GROUP BY dept_id;

-- 结果：
-- | dept_id | q1  | q2  | q3  | q4  |
-- |---------|-----|-----|-----|-----|
-- | 1       | 100 | 150 | 200 | 180 |
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：2.2 SQL Server PIVOT 语法

该示例来自原文《2.2 SQL Server PIVOT 语法》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- SQL Server 专用 PIVOT 语法
SELECT dept_id, [Q1], [Q2], [Q3], [Q4]
FROM quarterly_revenue
PIVOT (
    SUM(revenue)
    FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS p;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：2.3 PostgreSQL crosstab

该示例来自原文《2.3 PostgreSQL crosstab》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL: tablefunc 扩展
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT *
FROM crosstab(
    'SELECT dept_id, quarter, revenue
     FROM quarterly_revenue
     ORDER BY 1, 2'
) AS ct (dept_id INTEGER, q1 NUMERIC, q2 NUMERIC, q3 NUMERIC, q4 NUMERIC);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 4 类关键结构（func、SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：2.4 动态 PIVOT

该示例来自原文《2.4 动态 PIVOT》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 列值不固定时，需要动态 SQL
-- PostgreSQL 示例
DO $$
DECLARE
    pivot_cols TEXT;
    query TEXT;
BEGIN
    SELECT STRING_AGG(DISTINCT quote_ident(quarter), ', ')
    INTO pivot_cols
    FROM quarterly_revenue;

    query := format('
        SELECT dept_id, %s
        FROM quarterly_revenue
        PIVOT (SUM(revenue) FOR quarter IN (%s)) AS p
    ', pivot_cols, pivot_cols);

    EXECUTE query;
END $$;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 17 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：2.5 多值 PIVOT

该示例来自原文《2.5 多值 PIVOT》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 同时转换多个度量
SELECT
    dept_id,
    SUM(CASE WHEN quarter = 'Q1' THEN revenue ELSE 0 END) AS q1_revenue,
    SUM(CASE WHEN quarter = 'Q1' THEN cost ELSE 0 END) AS q1_cost,
    SUM(CASE WHEN quarter = 'Q2' THEN revenue ELSE 0 END) AS q2_revenue,
    SUM(CASE WHEN quarter = 'Q2' THEN cost ELSE 0 END) AS q2_cost
FROM quarterly_data
GROUP BY dept_id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：3.1 UNION ALL 实现（通用方法）

该示例来自原文《3.1 UNION ALL 实现（通用方法）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 原始数据：
-- | dept_id | q1  | q2  | q3  | q4  |
-- |---------|-----|-----|-----|-----|
-- | 1       | 100 | 150 | 200 | 180 |

-- 列转行
SELECT dept_id, 'Q1' AS quarter, q1 AS revenue FROM wide_data
UNION ALL
SELECT dept_id, 'Q2', q2 FROM wide_data
UNION ALL
SELECT dept_id, 'Q3', q3 FROM wide_data
UNION ALL
SELECT dept_id, 'Q4', q4 FROM wide_data;

-- 结果：
-- | dept_id | quarter | revenue |
-- |---------|---------|---------|
-- | 1       | Q1      | 100     |
-- | 1       | Q2      | 150     |
-- | 1       | Q3      | 200     |
-- | 1       | Q4      | 180     |
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 19 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：3.2 SQL Server UNPIVOT 语法

该示例来自原文《3.2 SQL Server UNPIVOT 语法》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
SELECT dept_id, quarter, revenue
FROM wide_data
UNPIVOT (
    revenue FOR quarter IN (q1, q2, q3, q4)
) AS u;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：3.3 PostgreSQL 使用 VALUES + LATERAL

该示例来自原文《3.3 PostgreSQL 使用 VALUES + LATERAL》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
SELECT t.dept_id, v.quarter, v.revenue
FROM wide_data t,
LATERAL (VALUES
    ('Q1', t.q1),
    ('Q2', t.q2),
    ('Q3', t.q3),
    ('Q4', t.q4)
) AS v(quarter, revenue)
WHERE v.revenue IS NOT NULL;  -- 排除 NULL 值
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：3.4 UNPIVOT 与 NULL 处理

该示例来自原文《3.4 UNPIVOT 与 NULL 处理》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- UNION ALL 保留 NULL
SELECT dept_id, 'Q1' AS quarter, q1 AS revenue FROM wide_data
UNION ALL
SELECT dept_id, 'Q2', q2 FROM wide_data;

-- SQL Server UNPIVOT 自动排除 NULL
SELECT dept_id, quarter, revenue
FROM wide_data
UNPIVOT (revenue FOR quarter IN (q1, q2, q3, q4)) AS u;
-- NULL 值的行不会出现在结果中

-- 如需保留 NULL，使用 CROSS APPLY
SELECT t.dept_id, v.quarter, v.revenue
FROM wide_data t
CROSS APPLY (VALUES
    ('Q1', t.q1), ('Q2', t.q2), ('Q3', t.q3), ('Q4', t.q4)
) v(quarter, revenue);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 15 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：4.1 月度报表

该示例来自原文《4.1 月度报表》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 按月展示销售数据
SELECT
    product_name,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 1  THEN amount ELSE 0 END) AS jan,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 2  THEN amount ELSE 0 END) AS feb,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 3  THEN amount ELSE 0 END) AS mar,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 4  THEN amount ELSE 0 END) AS apr,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 5  THEN amount ELSE 0 END) AS may,
    SUM(CASE WHEN EXTRACT(MONTH FROM order_date) = 6  THEN amount ELSE 0 END) AS jun
FROM sales
WHERE EXTRACT(YEAR FROM order_date) = 2026
GROUP BY product_name;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：4.2 用户属性宽表

该示例来自原文《4.2 用户属性宽表》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 将 EAV 模型转为宽表
-- 原始：user_id | attribute | value
-- 目标：user_id | age | gender | city

SELECT
    user_id,
    MAX(CASE WHEN attribute = 'age' THEN value END)::INTEGER AS age,
    MAX(CASE WHEN attribute = 'gender' THEN value END) AS gender,
    MAX(CASE WHEN attribute = 'city' THEN value END) AS city
FROM user_attributes
GROUP BY user_id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：4.3 数据清洗：宽表转长表

该示例来自原文《4.3 数据清洗：宽表转长表》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 将1月-12月列转为行，便于分析
WITH monthly_data AS (
    SELECT id, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec_val
    from annual_data
)
SELECT
    id,
    month,
    value
FROM monthly_data
UNPIVOT (
    value FOR month IN (jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec_val)
) u;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 3 类关键结构（from、SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：行转列（Pivot）

该示例来自原文《行转列（Pivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 将行数据转为列（通用方式）
SELECT
  dept,
  SUM(CASE WHEN quarter = 'Q1' THEN sales ELSE 0 END) AS q1,
  SUM(CASE WHEN quarter = 'Q2' THEN sales ELSE 0 END) AS q2,
  SUM(CASE WHEN quarter = 'Q3' THEN sales ELSE 0 END) AS q3,
  SUM(CASE WHEN quarter = 'Q4' THEN sales ELSE 0 END) AS q4
FROM quarterly_sales
GROUP BY dept;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：行转列（Pivot）

该示例来自原文《行转列（Pivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 使用 MAX 替代 SUM（适合非数值去重场景）
SELECT
  user_id,
  MAX(CASE WHEN attr = 'name' THEN value END) AS name,
  MAX(CASE WHEN attr = 'email' THEN value END) AS email,
  MAX(CASE WHEN attr = 'phone' THEN value END) AS phone
FROM user_attributes
GROUP BY user_id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：行转列（Pivot）

该示例来自原文《行转列（Pivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- SQL Server 专用 PIVOT 语法
SELECT dept, [Q1], [Q2], [Q3], [Q4]
FROM (
  SELECT dept, quarter, sales FROM quarterly_sales
) AS src
PIVOT (
  SUM(sales) FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS pvt;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：行转列（Pivot）

该示例来自原文《行转列（Pivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL tablefunc 扩展
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT * FROM crosstab(
  'SELECT dept, quarter, sales FROM quarterly_sales ORDER BY 1,2'
) AS result(
  dept VARCHAR,
  q1 INTEGER,
  q2 INTEGER,
  q3 INTEGER,
  q4 INTEGER
);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 4 类关键结构（func、SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：行转列（Pivot）

该示例来自原文《行转列（Pivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 将多行值合并为一个字符串
SELECT
  dept,
  GROUP_CONCAT(name SEPARATOR ', ') AS all_names
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

### 5.18 示例：行转列（Pivot）

该示例来自原文《行转列（Pivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL 字符串聚合
SELECT
  dept,
  STRING_AGG(name, ', ' ORDER BY name) AS all_names
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

### 5.19 示例：列转行（Unpivot）

该示例来自原文《列转行（Unpivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 将列数据转为行（通用方式）
SELECT dept, 'Q1' AS quarter, q1 AS sales FROM wide_sales
UNION ALL
SELECT dept, 'Q2' AS quarter, q2 AS sales FROM wide_sales
UNION ALL
SELECT dept, 'Q3' AS quarter, q3 AS sales FROM wide_sales
UNION ALL
SELECT dept, 'Q4' AS quarter, q4 AS sales FROM wide_sales
ORDER BY dept, quarter;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：列转行（Unpivot）

该示例来自原文《列转行（Unpivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- SQL Server 专用 UNPIVOT 语法
SELECT dept, quarter, sales
FROM wide_sales
UNPIVOT (
  sales FOR quarter IN (q1, q2, q3, q4)
) AS unpvt;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：列转行（Unpivot）

该示例来自原文《列转行（Unpivot）》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL 使用 UNNEST 展开数组
SELECT dept, quarter, sales
FROM wide_sales,
  UNNEST(
    ARRAY[q1, q2, q3, q4],
    ARRAY['Q1', 'Q2', 'Q3', 'Q4']
  ) AS t(sales, quarter);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：动态行列转换

该示例来自原文《动态行列转换》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- MySQL 动态生成 PIVOT 查询
SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT('SUM(CASE WHEN quarter = ''', quarter,
      ''' THEN sales ELSE 0 END) AS `', quarter, '`')
  ) INTO @sql
FROM quarterly_sales;

SET @sql = CONCAT('SELECT dept, ', @sql,
  ' FROM quarterly_sales GROUP BY dept');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：动态行列转换

该示例来自原文《动态行列转换》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL 使用 JSON 构建动态结构
SELECT
  dept,
  json_object_agg(quarter, sales) AS sales_json
FROM quarterly_sales
GROUP BY dept;
-- 结果：{"Q1": 1000, "Q2": 1500, ...}
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：常见应用场景

该示例来自原文《常见应用场景》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 学生成绩行转列
SELECT
  student,
  MAX(CASE WHEN subject = '语文' THEN score END) AS chinese,
  MAX(CASE WHEN subject = '数学' THEN score END) AS math,
  MAX(CASE WHEN subject = '英语' THEN score END) AS english
FROM scores
GROUP BY student;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：常见应用场景

该示例来自原文《常见应用场景》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 月度金额统计行转列
SELECT
  year,
  SUM(CASE WHEN month = 1 THEN amount ELSE 0 END) AS jan,
  SUM(CASE WHEN month = 2 THEN amount ELSE 0 END) AS feb,
  SUM(CASE WHEN month = 3 THEN amount ELSE 0 END) AS mar,
  SUM(CASE WHEN month = 4 THEN amount ELSE 0 END) AS apr,
  SUM(CASE WHEN month = 5 THEN amount ELSE 0 END) AS may,
  SUM(CASE WHEN month = 6 THEN amount ELSE 0 END) AS jun
FROM monthly_revenue
GROUP BY year;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：常见应用场景

该示例来自原文《常见应用场景》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- Entity-Attribute-Value 模型行转列
SELECT
  entity_id,
  MAX(CASE WHEN attr_name = 'name' THEN attr_value END) AS name,
  MAX(CASE WHEN attr_name = 'age' THEN attr_value END) AS age,
  MAX(CASE WHEN attr_name = 'city' THEN attr_value END) AS city
FROM eav_table
GROUP BY entity_id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：常见应用场景

该示例来自原文《常见应用场景》小节，用于演示PIVOT与UNPIVOT相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 用 COALESCE 替换 NULL 为 0
SELECT
  dept,
  COALESCE(SUM(CASE WHEN quarter = 'Q1' THEN sales END), 0) AS q1,
  COALESCE(SUM(CASE WHEN quarter = 'Q2' THEN sales END), 0) AS q2
FROM quarterly_sales
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

对比是理解《PIVOT与UNPIVOT》定位的最快路径。下面从多个维度与相邻方案进行对比。

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

本节把《PIVOT与UNPIVOT》放入真实工程场景，给出可复用的模式与组织方法。

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

本节通过一个完整案例把《PIVOT与UNPIVOT》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

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

关于《PIVOT与UNPIVOT》的核心结论：

SQL 的声明式表达力建立在关系代数之上，理解集合思维是进阶关键。
索引、执行计划与事务是三大实战主题。
工程化：迁移、连接池、监控与慢查询治理缺一不可。

原文档各小节的要点回顾：

- 1. 行列转换概述：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. PIVOT 行转列：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. UNPIVOT 列转行：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. 实际应用场景：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 行转列（Pivot）：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 列转行（Unpivot）：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 动态行列转换：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 常见应用场景：该小节围绕PIVOT与UNPIVOT展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

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

本文属于 SQL 模块。为了把《PIVOT与UNPIVOT》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["PIVOT与UNPIVOT"]
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
| GROUP BY与分组集 | 016-GROUPBYGroupingSet | 本文的并列主题 |
| 连接查询 | 017-JoinQuery | 本文的并列主题 |
| 自然连接与USING | 018-NaturalJoinUsing | 本文的并列主题 |
| 自连接 | 019-SelfJoin | 本文的并列主题 |
| 半连接与反半连接 | 020-SemiAntiJoin | 本文的并列主题 |
| LATERAL派生表 | 021-LateralDerivedTable | 本文的并列主题 |
| 子查询 | 022-Subquery | 本文的并列主题 |
| CTE | 023-CTE | 本文的并列主题 |
| 递归CTE | 024-RecursiveCTE | 本文的并列主题 |
| PIVOT与UNPIVOT | 025-PivotUnpivot | 本文自身 |
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

下表整理《PIVOT与UNPIVOT》及 SQL 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

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
