---
order: 63
title: 递归CTE
module: sql
category: SQL
difficulty: advanced
description: 'SQL递归公用表表达式：WITH RECURSIVE语法、层级遍历、图遍历、斐波那契数列与终止条件控制'
author: fanquanpp
updated: '2026-08-01'
related:
  - sql/子查询
  - sql/公用表表达式
  - sql/PIVOT与UNPIVOT
  - sql/集合操作
prerequisites:
  - sql/概述与标准
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《递归CTE》，属于 SQL 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 SQL 的核心概念、语法与常用对象。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 SQL 的执行原理与优化机制。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够编写正确、高效的 SQL 语句与操作。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 SQL 相关方案在性能与一致性上的权衡。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够根据业务场景评价 SQL 技术选型。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够组合 SQL 与其他技术设计数据架构。

通过本节学习，读者应当能够把《递归CTE》纳入自己的知识网络，并与 SQL 模块的其他主题（DDL/DML、查询、索引、事务）建立关联。

## 2. 历史动机与发展脉络

《递归CTE》是 SQL 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

SQL（结构化查询语言）源于 1970 年 Codd 的关系模型，1974 年由 Chamberlin 与 Boyce 设计（SEQUEL），1986 年成为 ANSI 标准；SQL:2023 是当前国际标准。
SQL 分为 DDL（建表）、DML（增删改）、DQL（查询）、DCL（权限）与 TCL（事务）；各大数据库在标准基础上扩展方言。
SQL 是声明式语言：描述“要什么”而非“怎么做”，优化器负责执行计划；这一设计让 SQL 具有跨数据库的表达一致性。

回到本文主题：递归CTE 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《递归CTE》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。
查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。
事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 13 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# SQL 递归 CTE 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. 递归 CTE 概述

递归 CTE（Recursive CTE）允许查询引用自身，用于处理层级数据、树形结构和图遍历等递归问题。

##### 1.1 基本语法

```sql
WITH RECURSIVE cte_name AS (
    -- 锚点查询（基础情况，非递归）
    SELECT ...

    UNION ALL

    -- 递归查询（引用自身）
    SELECT ... FROM cte_name WHERE ...
)
SELECT * FROM cte_name;
```

##### 1.2 执行流程

```
1. 执行锚点查询，生成初始结果集 R0
2. 将 R0 作为输入，执行递归查询，生成 R1
3. 将 R1 作为输入，执行递归查询，生成 R2
4. 重复直到递归查询返回空结果集
5. 最终结果 = R0 ∪ R1 ∪ R2 ∪ ...
```

#### 2. 层级数据遍历

##### 2.1 组织架构树

```sql
CREATE TABLE employees (
    emp_id    SERIAL PRIMARY KEY,
    name      VARCHAR(100),
    manager_id INTEGER REFERENCES employees(emp_id)
);

-- 从顶级经理开始，向下遍历所有层级
WITH RECURSIVE org_tree AS (
    -- 锚点：顶级经理（无上级）
    SELECT emp_id, name, manager_id, 1 AS level, name::TEXT AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- 递归：每个经理的下属
    SELECT e.emp_id, e.name, e.manager_id,
           ot.level + 1,
           ot.path || ' > ' || e.name
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.emp_id
)
SELECT * FROM org_tree ORDER BY level, path;
```

**输出示例**：

| emp_id | name | manager_id | level | path             |
| ------ | ---- | ---------- | ----- | ---------------- |
| 1      | CEO  | NULL       | 1     | CEO              |
| 2      | CTO  | 1          | 2     | CEO > CTO        |
| 3      | CFO  | 1          | 2     | CEO > CFO        |
| 4      | Dev1 | 2          | 3     | CEO > CTO > Dev1 |

##### 2.2 自底向上遍历

```sql
-- 从指定员工向上查找所有上级
WITH RECURSIVE manager_chain AS (
    -- 锚点：指定员工
    SELECT emp_id, name, manager_id, 0 AS distance
    FROM employees
    WHERE emp_id = 42

    UNION ALL

    -- 递归：向上查找上级
    SELECT e.emp_id, e.name, e.manager_id, mc.distance + 1
    FROM employees e
    JOIN manager_chain mc ON e.emp_id = mc.manager_id
)
SELECT * FROM manager_chain ORDER BY distance;
```

##### 2.3 计算每个节点的子树大小

```sql
WITH RECURSIVE subtree AS (
    -- 锚点：每个员工自身
    SELECT emp_id AS root_id, emp_id
    FROM employees

    UNION ALL

    -- 递归：向下扩展子树
    SELECT s.root_id, e.emp_id
    FROM subtree s
    JOIN employees e ON e.manager_id = s.emp_id
)
SELECT root_id AS emp_id, COUNT(*) AS subtree_size
FROM subtree
GROUP BY root_id
ORDER BY subtree_size DESC;
```

#### 3. 图遍历

##### 3.1 最短路径

```sql
CREATE TABLE edges (
    from_node VARCHAR(10),
    to_node   VARCHAR(10),
    weight    INTEGER
);

-- BFS 查找最短路径
WITH RECURSIVE bfs AS (
    -- 锚点：起始节点
    SELECT
        from_node AS current,
        to_node AS next_node,
        weight AS total_weight,
        from_node::TEXT AS path,
        1 AS depth

    FROM edges
    WHERE from_node = 'A'

    UNION ALL

    -- 递归：扩展到下一层
    SELECT
        e.from_node,
        e.to_node,
        b.total_weight + e.weight,
        b.path || ' -> ' || e.to_node,
        b.depth + 1
    FROM edges e
    JOIN bfs b ON e.from_node = b.next_node
    WHERE b.path NOT LIKE '%' || e.to_node || '%'  -- 避免环路
)
SELECT path, total_weight, depth
FROM bfs
WHERE next_node = 'D'
ORDER BY total_weight
LIMIT 1;
```

##### 3.2 航班路线搜索

```sql
CREATE TABLE flights (
    flight_id  VARCHAR(10),
    from_city  VARCHAR(50),
    to_city    VARCHAR(50),
    price      DECIMAL(10, 2)
);

-- 查找从北京到上海的所有路线（最多2次中转）
WITH RECURSIVE routes AS (
    -- 锚点：直飞航班
    SELECT
        from_city,
        to_city,
        price,
        from_city || ' -> ' || to_city AS route,
        1 AS stops
    FROM flights
    WHERE from_city = '北京'

    UNION ALL

    -- 递归：中转航班
    SELECT
        r.from_city,
        f.to_city,
        r.price + f.price,
        r.route || ' -> ' || f.to_city,
        r.stops + 1
    FROM routes r
    JOIN flights f ON r.to_city = f.from_city
    WHERE r.stops < 3  -- 最多2次中转
      AND r.route NOT LIKE '%' || f.to_city || '%'  -- 避免环路
)
SELECT route, price, stops
FROM routes
WHERE to_city = '上海'
ORDER BY price
LIMIT 5;
```

#### 4. 数列生成

##### 4.1 斐波那契数列

```sql
WITH RECURSIVE fib AS (
    -- 锚点：前两个数
    SELECT 1 AS n, 0 AS fib_n, 1 AS fib_n_plus_1

    UNION ALL

    -- 递归：下一个数
    SELECT n + 1, fib_n_plus_1, fib_n + fib_n_plus_1
    FROM fib
    WHERE n < 20
)
SELECT n, fib_n AS fibonacci_number FROM fib;
```

##### 4.2 日期序列

```sql
-- 生成2026年所有日期
WITH RECURSIVE dates AS (
    SELECT DATE '2026-01-01' AS dt

    UNION ALL

    SELECT dt + INTERVAL '1 day'
    FROM dates
    WHERE dt < DATE '2026-12-31'
)
SELECT dt FROM dates;
```

##### 4.3 数字序列

```sql
-- 生成1到1000的数字序列
WITH RECURSIVE nums AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT n FROM nums;
```

#### 5. 终止条件与安全控制

##### 5.1 终止条件

递归 CTE 在以下情况终止：

1. 递归查询返回空结果集
2. 达到数据库的递归深度限制

```sql
-- PostgreSQL：设置递归深度限制
SET max_recursion_depth = 100;  -- 默认无限制

-- MySQL：在查询中指定
WITH RECURSIVE cte AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM cte WHERE n < 1000  -- WHERE 条件控制终止
)
SELECT * FROM cte;

-- SQL Server：OPTION 提示
SELECT * FROM cte OPTION (MAXRECURSION 100);
```

##### 5.2 防止无限递归

```sql
-- 方法1：深度限制
WITH RECURSIVE tree AS (
    SELECT id, parent_id, 1 AS depth
    FROM nodes WHERE parent_id IS NULL

    UNION ALL

    SELECT n.id, n.parent_id, t.depth + 1
    FROM nodes n JOIN tree t ON n.parent_id = t.id
    WHERE t.depth < 10  -- 限制最大深度
)

-- 方法2：路径去重（防止环路）
WITH RECURSIVE tree AS (
    SELECT id, parent_id, ARRAY[id] AS visited
    FROM nodes WHERE parent_id IS NULL

    UNION ALL

    SELECT n.id, n.parent_id, t.visited || n.id
    FROM nodes n JOIN tree t ON n.parent_id = t.id
    WHERE n.id <> ALL(t.visited)  -- 排除已访问节点
)
```

#### 6. 性能优化

##### 6.1 索引支持

```sql
-- 递归查询的连接列需要索引
CREATE INDEX idx_employees_manager_id ON employees(manager_id);

-- 递归查询通常使用 Nested Loop，索引至关重要
```

##### 6.2 减少递归层数

```sql
-- 优化前：逐层递归
WITH RECURSIVE tree AS (...)

-- 优化后：使用物化路径或嵌套集模型
-- 物化路径：存储完整路径 "1/3/7/12"
-- 嵌套集：存储左值右值 (lft, rgt)
-- 这些非递归模型查询效率更高
```

##### 6.3 递归 CTE vs 递归函数

| 特性     | 递归 CTE           | 递归函数     |
| -------- | ------------------ | ------------ |
| 语言     | 纯 SQL             | PL/pgSQL 等  |
| 灵活性   | 有限               | 高           |
| 调试     | 困难               | 较容易       |
| 性能     | 单次查询，减少往返 | 可能多次查询 |
| 适用场景 | 简单层级遍历       | 复杂递归逻辑 |
#### 递归 CTE 基本结构

**基本写法：递归 CTE 框架**
`WITH RECURSIVE <CTE名> AS (<基础查询> UNION [ALL] <递归查询>) SELECT * FROM <CTE名>`
```sql
-- 递归 CTE 由基础查询 + 递归查询组成
WITH RECURSIVE counter(n) AS (
  -- 基础查询：起点
  SELECT 1
  UNION ALL
  -- 递归查询：基于上一次结果迭代
  SELECT n + 1 FROM counter WHERE n < 10
)
SELECT * FROM counter;
-- 结果：1 到 10
```

---

**基本写法：PostgreSQL 递归**
`WITH RECURSIVE <CTE名>(<列>) AS (...) SELECT * FROM <CTE名>`
```sql
-- PostgreSQL 递归 CTE
WITH RECURSIVE fibonacci(n, a, b) AS (
  SELECT 1, 0, 1
  UNION ALL
  SELECT n + 1, b, a + b FROM fibonacci WHERE n < 10
)
SELECT n, a AS fib_value FROM fibonacci;
-- 结果：0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

---

#### 组织架构递归

**基本写法：向下查询所有下属**
`WITH RECURSIVE <CTE> AS (<根查询> UNION ALL <递归查询>) SELECT * FROM <CTE>`
```sql
-- 查找某经理的所有下属（含间接下属）
WITH RECURSIVE subordinates AS (
  -- 基础查询：直接下属
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE id = 100  -- 起始节点
  UNION ALL
  -- 递归查询：下一级
  SELECT e.id, e.name, e.manager_id, s.level + 1
  FROM employees e
  JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates ORDER BY level;
```

---

**基本写法：向上查询所有上级**
`WITH RECURSIVE <CTE> AS (<根查询> UNION ALL <递归查询>) SELECT * FROM <CTE>`
```sql
-- 查找某员工的所有上级（含间接上级）
WITH RECURSIVE managers AS (
  -- 基础查询：直接上级
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE id = 105  -- 起始节点
  UNION ALL
  -- 递归查询：上一级
  SELECT e.id, e.name, e.manager_id, m.level + 1
  FROM employees e
  JOIN managers m ON e.id = m.manager_id
)
SELECT * FROM managers ORDER BY level DESC;
```

---

**基本写法：拼接层级路径**
`WITH RECURSIVE <CTE> AS (SELECT ..., CAST(<列> AS VARCHAR(1000)) AS path ...)`
```sql
-- 生成完整层级路径
WITH RECURSIVE org_path AS (
  SELECT id, name, manager_id, 1 AS level,
    CAST(name AS VARCHAR(1000)) AS path
  FROM employees
  WHERE manager_id IS NULL  -- 顶级节点
  UNION ALL
  SELECT e.id, e.name, e.manager_id, o.level + 1,
    CONCAT(o.path, ' > ', e.name)
  FROM employees e
  JOIN org_path o ON e.manager_id = o.id
)
SELECT id, name, level, path FROM org_path;
-- 结果示例：1, CEO, 1, CEO > VP > Manager > Engineer
```

---

#### 树形结构遍历

**基本写法：分类树遍历**
`WITH RECURSIVE <CTE> AS (SELECT * FROM <表> WHERE <根条件> UNION ALL SELECT ... FROM <表> JOIN <CTE> ON ...)`
```sql
-- 遍历分类树
WITH RECURSIVE category_tree AS (
  SELECT id, name, parent_id, 0 AS depth, CAST(name AS VARCHAR(255)) AS tree_path
  FROM categories
  WHERE parent_id IS NULL  -- 根分类
  UNION ALL
  SELECT c.id, c.name, c.parent_id, ct.depth + 1,
    CONCAT(ct.tree_path, ' / ', c.name)
  FROM categories c
  JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT id, name, depth, tree_path
FROM category_tree
ORDER BY tree_path;
```

---

**基本写法：计算子节点数量**
`WITH RECURSIVE <CTE> AS (...) SELECT <父节点>, COUNT(*) FROM <CTE> GROUP BY <父节点>`
```sql
-- 统计每个分类下的子分类数
WITH RECURSIVE child_count AS (
  SELECT id, parent_id FROM categories WHERE parent_id IS NOT NULL
  UNION ALL
  SELECT c.id, c.parent_id FROM categories c
  JOIN child_count cc ON c.parent_id = cc.id
)
SELECT parent_id, COUNT(*) AS total_children
FROM child_count
GROUP BY parent_id;
```

---

#### 数字序列生成

**基本写法：生成连续数字**
`WITH RECURSIVE <CTE>(<列>) AS (SELECT 1 UNION ALL SELECT <列> + 1 FROM <CTE> WHERE <列> < <上限>)`
```sql
-- 生成 1 到 100 的序列
WITH RECURSIVE nums(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM nums WHERE n < 100
)
SELECT n FROM nums;
```

---

**基本写法：生成日期序列**
`WITH RECURSIVE <CTE> AS (SELECT <起始日期> AS dt UNION ALL SELECT dt + INTERVAL 1 DAY FROM <CTE> WHERE dt < <结束日期>)`
```sql
-- 生成日期范围内的每一天
WITH RECURSIVE date_range(dt) AS (
  SELECT DATE('2026-01-01')
  UNION ALL
  SELECT DATE_ADD(dt, INTERVAL 1 DAY) FROM date_range
  WHERE dt < DATE('2026-01-31')
)
SELECT dt FROM date_range;
```

---

#### 分层数据聚合

**基本写法：递归统计层级汇总**
`WITH RECURSIVE <CTE> AS (...) SELECT <层级>, SUM(<值>) FROM <CTE> GROUP BY <层级>`
```sql
-- 统计每个层级的总金额
WITH RECURSIVE org_sales AS (
  -- 基础：直接销售人员
  SELECT emp_id, emp_name, manager_id, 1 AS level, sales_amount
  FROM sales
  UNION ALL
  -- 递归：上级汇总下级
  SELECT s.emp_id, s.emp_name, s.manager_id, os.level + 1,
    os.sales_amount
  FROM sales s
  JOIN org_sales os ON s.emp_id = os.manager_id
)
SELECT level, SUM(sales_amount) AS total_sales
FROM org_sales
GROUP BY level
ORDER BY level;
```

---

#### 递归终止与防环

**基本写法：限制递归深度**
`WHERE <列> < <最大深度>`
```sql
-- MySQL 限制递归次数
SET @@cte_max_recursion_depth = 1000;

-- 在递归查询中加深度限制
WITH RECURSIVE tree AS (
  SELECT id, parent_id, 1 AS depth FROM nodes WHERE id = 1
  UNION ALL
  SELECT n.id, n.parent_id, t.depth + 1
  FROM nodes n JOIN tree t ON n.parent_id = t.id
  WHERE t.depth < 10  -- 限制 10 层
)
SELECT * FROM tree;
```

---

**基本写法：防止循环引用**
`WHERE FIND_IN_SET(<列>, <path>) = 0`
```sql
-- 使用路径防止循环
WITH RECURSIVE safe_tree AS (
  SELECT id, parent_id, CAST(id AS CHAR(1000)) AS path
  FROM nodes WHERE id = 1
  UNION ALL
  SELECT n.id, n.parent_id, CONCAT(st.path, ',', n.id)
  FROM nodes n
  JOIN safe_tree st ON n.parent_id = st.id
  WHERE FIND_IN_SET(n.id, st.path) = 0  -- 已访问过的节点跳过
)
SELECT * FROM safe_tree;
```

---

#### PostgreSQL WITH CYCLE 检测

**基本写法：CYCLE 检测（PostgreSQL 14+）**
`WITH RECURSIVE <CTE> AS (...) CYCLE <列> SET <标记> TO true DEFAULT false USING <路径>`
```sql
-- PostgreSQL 自动检测循环
WITH RECURSIVE tree AS (
  SELECT id, parent_id FROM nodes WHERE id = 1
  UNION ALL
  SELECT n.id, n.parent_id FROM nodes n
  JOIN tree t ON n.parent_id = t.id
)
CYCLE id SET is_cycle TO true DEFAULT false USING path
SELECT * FROM tree WHERE NOT is_cycle;
```


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["递归CTE"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《递归CTE》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。
查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。
事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。
集合语义：SELECT 返回结果集；JOIN 组合关系，GROUP BY 聚合，子查询与 CTE 表达复杂逻辑。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1.1 基本语法

该示例来自原文《1.1 基本语法》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
WITH RECURSIVE cte_name AS (
    -- 锚点查询（基础情况，非递归）
    SELECT ...

    UNION ALL

    -- 递归查询（引用自身）
    SELECT ... FROM cte_name WHERE ...
)
SELECT * FROM cte_name;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：1.2 执行流程

该示例来自原文《1.2 执行流程》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```text
1. 执行锚点查询，生成初始结果集 R0
2. 将 R0 作为输入，执行递归查询，生成 R1
3. 将 R1 作为输入，执行递归查询，生成 R2
4. 重复直到递归查询返回空结果集
5. 最终结果 = R0 ∪ R1 ∪ R2 ∪ ...
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 5 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：2.1 组织架构树

该示例来自原文《2.1 组织架构树》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
CREATE TABLE employees (
    emp_id    SERIAL PRIMARY KEY,
    name      VARCHAR(100),
    manager_id INTEGER REFERENCES employees(emp_id)
);

-- 从顶级经理开始，向下遍历所有层级
WITH RECURSIVE org_tree AS (
    -- 锚点：顶级经理（无上级）
    SELECT emp_id, name, manager_id, 1 AS level, name::TEXT AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- 递归：每个经理的下属
    SELECT e.emp_id, e.name, e.manager_id,
           ot.level + 1,
           ot.path || ' > ' || e.name
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.emp_id
)
SELECT * FROM org_tree ORDER BY level, path;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：2.2 自底向上遍历

该示例来自原文《2.2 自底向上遍历》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 从指定员工向上查找所有上级
WITH RECURSIVE manager_chain AS (
    -- 锚点：指定员工
    SELECT emp_id, name, manager_id, 0 AS distance
    FROM employees
    WHERE emp_id = 42

    UNION ALL

    -- 递归：向上查找上级
    SELECT e.emp_id, e.name, e.manager_id, mc.distance + 1
    FROM employees e
    JOIN manager_chain mc ON e.emp_id = mc.manager_id
)
SELECT * FROM manager_chain ORDER BY distance;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：2.3 计算每个节点的子树大小

该示例来自原文《2.3 计算每个节点的子树大小》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
WITH RECURSIVE subtree AS (
    -- 锚点：每个员工自身
    SELECT emp_id AS root_id, emp_id
    FROM employees

    UNION ALL

    -- 递归：向下扩展子树
    SELECT s.root_id, e.emp_id
    FROM subtree s
    JOIN employees e ON e.manager_id = s.emp_id
)
SELECT root_id AS emp_id, COUNT(*) AS subtree_size
FROM subtree
GROUP BY root_id
ORDER BY subtree_size DESC;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：3.1 最短路径

该示例来自原文《3.1 最短路径》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
CREATE TABLE edges (
    from_node VARCHAR(10),
    to_node   VARCHAR(10),
    weight    INTEGER
);

-- BFS 查找最短路径
WITH RECURSIVE bfs AS (
    -- 锚点：起始节点
    SELECT
        from_node AS current,
        to_node AS next_node,
        weight AS total_weight,
        from_node::TEXT AS path,
        1 AS depth

    FROM edges
    WHERE from_node = 'A'

    UNION ALL

    -- 递归：扩展到下一层
    SELECT
        e.from_node,
        e.to_node,
        b.total_weight + e.weight,
        b.path || ' -> ' || e.to_node,
        b.depth + 1
    FROM edges e
    JOIN bfs b ON e.from_node = b.next_node
    WHERE b.path NOT LIKE '%' || e.to_node || '%'  -- 避免环路
)
SELECT path, total_weight, depth
FROM bfs
WHERE next_node = 'D'
ORDER BY total_weight
LIMIT 1;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 33 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：3.2 航班路线搜索

该示例来自原文《3.2 航班路线搜索》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
CREATE TABLE flights (
    flight_id  VARCHAR(10),
    from_city  VARCHAR(50),
    to_city    VARCHAR(50),
    price      DECIMAL(10, 2)
);

-- 查找从北京到上海的所有路线（最多2次中转）
WITH RECURSIVE routes AS (
    -- 锚点：直飞航班
    SELECT
        from_city,
        to_city,
        price,
        from_city || ' -> ' || to_city AS route,
        1 AS stops
    FROM flights
    WHERE from_city = '北京'

    UNION ALL

    -- 递归：中转航班
    SELECT
        r.from_city,
        f.to_city,
        r.price + f.price,
        r.route || ' -> ' || f.to_city,
        r.stops + 1
    FROM routes r
    JOIN flights f ON r.to_city = f.from_city
    WHERE r.stops < 3  -- 最多2次中转
      AND r.route NOT LIKE '%' || f.to_city || '%'  -- 避免环路
)
SELECT route, price, stops
FROM routes
WHERE to_city = '上海'
ORDER BY price
LIMIT 5;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 35 行有效代码，包含 3 类关键结构（SELECT、CREATE、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：4.1 斐波那契数列

该示例来自原文《4.1 斐波那契数列》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
WITH RECURSIVE fib AS (
    -- 锚点：前两个数
    SELECT 1 AS n, 0 AS fib_n, 1 AS fib_n_plus_1

    UNION ALL

    -- 递归：下一个数
    SELECT n + 1, fib_n_plus_1, fib_n + fib_n_plus_1
    FROM fib
    WHERE n < 20
)
SELECT n, fib_n AS fibonacci_number FROM fib;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：4.2 日期序列

该示例来自原文《4.2 日期序列》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 生成2026年所有日期
WITH RECURSIVE dates AS (
    SELECT DATE '2026-01-01' AS dt

    UNION ALL

    SELECT dt + INTERVAL '1 day'
    FROM dates
    WHERE dt < DATE '2026-12-31'
)
SELECT dt FROM dates;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：4.3 数字序列

该示例来自原文《4.3 数字序列》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 生成1到1000的数字序列
WITH RECURSIVE nums AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1 FROM nums WHERE n < 1000
)
SELECT n FROM nums;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：5.1 终止条件

该示例来自原文《5.1 终止条件》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL：设置递归深度限制
SET max_recursion_depth = 100;  -- 默认无限制

-- MySQL：在查询中指定
WITH RECURSIVE cte AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM cte WHERE n < 1000  -- WHERE 条件控制终止
)
SELECT * FROM cte;

-- SQL Server：OPTION 提示
SELECT * FROM cte OPTION (MAXRECURSION 100);
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：5.2 防止无限递归

该示例来自原文《5.2 防止无限递归》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 方法1：深度限制
WITH RECURSIVE tree AS (
    SELECT id, parent_id, 1 AS depth
    FROM nodes WHERE parent_id IS NULL

    UNION ALL

    SELECT n.id, n.parent_id, t.depth + 1
    FROM nodes n JOIN tree t ON n.parent_id = t.id
    WHERE t.depth < 10  -- 限制最大深度
)

-- 方法2：路径去重（防止环路）
WITH RECURSIVE tree AS (
    SELECT id, parent_id, ARRAY[id] AS visited
    FROM nodes WHERE parent_id IS NULL

    UNION ALL

    SELECT n.id, n.parent_id, t.visited || n.id
    FROM nodes n JOIN tree t ON n.parent_id = t.id
    WHERE n.id <> ALL(t.visited)  -- 排除已访问节点
)
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 18 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：6.1 索引支持

该示例来自原文《6.1 索引支持》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 递归查询的连接列需要索引
CREATE INDEX idx_employees_manager_id ON employees(manager_id);

-- 递归查询通常使用 Nested Loop，索引至关重要
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 3 行有效代码，包含 1 类关键结构（CREATE）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：6.2 减少递归层数

该示例来自原文《6.2 减少递归层数》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 优化前：逐层递归
WITH RECURSIVE tree AS (...)

-- 优化后：使用物化路径或嵌套集模型
-- 物化路径：存储完整路径 "1/3/7/12"
-- 嵌套集：存储左值右值 (lft, rgt)
-- 这些非递归模型查询效率更高
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 6 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：递归 CTE 基本结构

该示例来自原文《递归 CTE 基本结构》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 递归 CTE 由基础查询 + 递归查询组成
WITH RECURSIVE counter(n) AS (
  -- 基础查询：起点
  SELECT 1
  UNION ALL
  -- 递归查询：基于上一次结果迭代
  SELECT n + 1 FROM counter WHERE n < 10
)
SELECT * FROM counter;
-- 结果：1 到 10
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：递归 CTE 基本结构

该示例来自原文《递归 CTE 基本结构》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL 递归 CTE
WITH RECURSIVE fibonacci(n, a, b) AS (
  SELECT 1, 0, 1
  UNION ALL
  SELECT n + 1, b, a + b FROM fibonacci WHERE n < 10
)
SELECT n, a AS fib_value FROM fibonacci;
-- 结果：0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：组织架构递归

该示例来自原文《组织架构递归》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查找某经理的所有下属（含间接下属）
WITH RECURSIVE subordinates AS (
  -- 基础查询：直接下属
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE id = 100  -- 起始节点
  UNION ALL
  -- 递归查询：下一级
  SELECT e.id, e.name, e.manager_id, s.level + 1
  FROM employees e
  JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates ORDER BY level;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：组织架构递归

该示例来自原文《组织架构递归》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 查找某员工的所有上级（含间接上级）
WITH RECURSIVE managers AS (
  -- 基础查询：直接上级
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE id = 105  -- 起始节点
  UNION ALL
  -- 递归查询：上一级
  SELECT e.id, e.name, e.manager_id, m.level + 1
  FROM employees e
  JOIN managers m ON e.id = m.manager_id
)
SELECT * FROM managers ORDER BY level DESC;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：组织架构递归

该示例来自原文《组织架构递归》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 生成完整层级路径
WITH RECURSIVE org_path AS (
  SELECT id, name, manager_id, 1 AS level,
    CAST(name AS VARCHAR(1000)) AS path
  FROM employees
  WHERE manager_id IS NULL  -- 顶级节点
  UNION ALL
  SELECT e.id, e.name, e.manager_id, o.level + 1,
    CONCAT(o.path, ' > ', e.name)
  FROM employees e
  JOIN org_path o ON e.manager_id = o.id
)
SELECT id, name, level, path FROM org_path;
-- 结果示例：1, CEO, 1, CEO > VP > Manager > Engineer
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：树形结构遍历

该示例来自原文《树形结构遍历》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 遍历分类树
WITH RECURSIVE category_tree AS (
  SELECT id, name, parent_id, 0 AS depth, CAST(name AS VARCHAR(255)) AS tree_path
  FROM categories
  WHERE parent_id IS NULL  -- 根分类
  UNION ALL
  SELECT c.id, c.name, c.parent_id, ct.depth + 1,
    CONCAT(ct.tree_path, ' / ', c.name)
  FROM categories c
  JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT id, name, depth, tree_path
FROM category_tree
ORDER BY tree_path;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：树形结构遍历

该示例来自原文《树形结构遍历》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 统计每个分类下的子分类数
WITH RECURSIVE child_count AS (
  SELECT id, parent_id FROM categories WHERE parent_id IS NOT NULL
  UNION ALL
  SELECT c.id, c.parent_id FROM categories c
  JOIN child_count cc ON c.parent_id = cc.id
)
SELECT parent_id, COUNT(*) AS total_children
FROM child_count
GROUP BY parent_id;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：数字序列生成

该示例来自原文《数字序列生成》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 生成 1 到 100 的序列
WITH RECURSIVE nums(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM nums WHERE n < 100
)
SELECT n FROM nums;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 7 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：数字序列生成

该示例来自原文《数字序列生成》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 生成日期范围内的每一天
WITH RECURSIVE date_range(dt) AS (
  SELECT DATE('2026-01-01')
  UNION ALL
  SELECT DATE_ADD(dt, INTERVAL 1 DAY) FROM date_range
  WHERE dt < DATE('2026-01-31')
)
SELECT dt FROM date_range;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：分层数据聚合

该示例来自原文《分层数据聚合》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 统计每个层级的总金额
WITH RECURSIVE org_sales AS (
  -- 基础：直接销售人员
  SELECT emp_id, emp_name, manager_id, 1 AS level, sales_amount
  FROM sales
  UNION ALL
  -- 递归：上级汇总下级
  SELECT s.emp_id, s.emp_name, s.manager_id, os.level + 1,
    os.sales_amount
  FROM sales s
  JOIN org_sales os ON s.emp_id = os.manager_id
)
SELECT level, SUM(sales_amount) AS total_sales
FROM org_sales
GROUP BY level
ORDER BY level;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：递归终止与防环

该示例来自原文《递归终止与防环》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- MySQL 限制递归次数
SET @@cte_max_recursion_depth = 1000;

-- 在递归查询中加深度限制
WITH RECURSIVE tree AS (
  SELECT id, parent_id, 1 AS depth FROM nodes WHERE id = 1
  UNION ALL
  SELECT n.id, n.parent_id, t.depth + 1
  FROM nodes n JOIN tree t ON n.parent_id = t.id
  WHERE t.depth < 10  -- 限制 10 层
)
SELECT * FROM tree;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：递归终止与防环

该示例来自原文《递归终止与防环》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- 使用路径防止循环
WITH RECURSIVE safe_tree AS (
  SELECT id, parent_id, CAST(id AS CHAR(1000)) AS path
  FROM nodes WHERE id = 1
  UNION ALL
  SELECT n.id, n.parent_id, CONCAT(st.path, ',', n.id)
  FROM nodes n
  JOIN safe_tree st ON n.parent_id = st.id
  WHERE FIND_IN_SET(n.id, st.path) = 0  -- 已访问过的节点跳过
)
SELECT * FROM safe_tree;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：PostgreSQL WITH CYCLE 检测

该示例来自原文《PostgreSQL WITH CYCLE 检测》小节，用于演示递归CTE相关操作。阅读时请先看代码结构，再看其后的讲解。

```sql
-- PostgreSQL 自动检测循环
WITH RECURSIVE tree AS (
  SELECT id, parent_id FROM nodes WHERE id = 1
  UNION ALL
  SELECT n.id, n.parent_id FROM nodes n
  JOIN tree t ON n.parent_id = t.id
)
CYCLE id SET is_cycle TO true DEFAULT false USING path
SELECT * FROM tree WHERE NOT is_cycle;
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，包含 2 类关键结构（SELECT、FROM）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《递归CTE》定位的最快路径。下面从多个维度与相邻方案进行对比。

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

本节把《递归CTE》放入真实工程场景，给出可复用的模式与组织方法。

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

本节通过一个完整案例把《递归CTE》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

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

关于《递归CTE》的核心结论：

SQL 的声明式表达力建立在关系代数之上，理解集合思维是进阶关键。
索引、执行计划与事务是三大实战主题。
工程化：迁移、连接池、监控与慢查询治理缺一不可。

原文档各小节的要点回顾：

- 1. 递归 CTE 概述：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. 层级数据遍历：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. 图遍历：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. 数列生成：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. 终止条件与安全控制：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 性能优化：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 递归 CTE 基本结构：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 组织架构递归：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 树形结构遍历：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 数字序列生成：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 分层数据聚合：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 递归终止与防环：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- PostgreSQL WITH CYCLE 检测：该小节围绕递归CTE展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

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

本文属于 SQL 模块。为了把《递归CTE》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["递归CTE"]
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
| 递归CTE | 024-RecursiveCTE | 本文自身 |
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

下表整理《递归CTE》及 SQL 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

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
