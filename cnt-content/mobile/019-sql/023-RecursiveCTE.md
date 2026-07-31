# SQL 递归 CTE 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 递归 CTE 基本结构

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

## 组织架构递归

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

## 树形结构遍历

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

## 数字序列生成

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

## 分层数据聚合

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

## 递归终止与防环

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

## PostgreSQL WITH CYCLE 检测

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
