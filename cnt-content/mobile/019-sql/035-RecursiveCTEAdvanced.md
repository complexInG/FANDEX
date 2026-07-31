# SQL 递归 CTE 进阶语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 递归 CTE 基本结构

**基本写法：WITH RECURSIVE**
`WITH RECURSIVE <cte名>(<列>) AS (<锚点成员> UNION [ALL] <递归成员>) SELECT ... FROM <cte名>`
```sql
-- 锚点成员：起始行；递归成员：引用 CTE 自身逐层展开
WITH RECURSIVE num_seq(n) AS (
  SELECT 1              -- 锚点：从 1 开始
  UNION ALL
  SELECT n + 1          -- 递归：每次 +1
  FROM num_seq
  WHERE n < 10          -- 终止条件
)
SELECT n FROM num_seq;
-- 结果：1~10
```

---

## 树形结构遍历

**基本写法：向下查所有子孙**
`WITH RECURSIVE <cte> AS (SELECT ... FROM <表> WHERE <根条件> UNION ALL SELECT ... FROM <表> JOIN <cte>)`
```sql
-- 经典组织架构向下遍历
WITH RECURSIVE org_tree(id, name, manager_id, lvl, path) AS (
  -- 锚点：顶层节点
  SELECT id, name, manager_id, 1 AS lvl,
         CAST(name AS VARCHAR(1000)) AS path
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  -- 递归：下级节点
  SELECT e.id, e.name, e.manager_id, o.lvl + 1,
         CAST(o.path || ' > ' || e.name AS VARCHAR(1000))
  FROM employees e
  JOIN org_tree o ON e.manager_id = o.id
)
SELECT id, name, lvl, path FROM org_tree ORDER BY path;
```

---

**基本写法：向上查所有祖先**
`WITH RECURSIVE <cte> AS (SELECT ... WHERE <起始> UNION ALL SELECT ... JOIN <cte> ON <父条件>)`
```sql
-- 从指定节点向上遍历到根
WITH RECURSIVE ancestors(id, name, manager_id, lvl) AS (
  SELECT id, name, manager_id, 0
  FROM employees
  WHERE id = 1001              -- 起始节点
  UNION ALL
  SELECT e.id, e.name, e.manager_id, a.lvl + 1
  FROM employees e
  JOIN ancestors a ON e.id = a.manager_id
)
SELECT id, name, lvl FROM ancestors ORDER BY lvl;
```

---

## 层级路径与排序

**基本写法：构造层级路径字符串**
`CAST(<父路径> || <分隔符> || <当前> AS <类型>)`
```sql
-- 用路径字符串保持树形排序
WITH RECURSIVE tree(id, name, parent_id, sort_path, depth) AS (
  SELECT id, name, parent_id,
         CAST(LPAD(id::text, 5, '0') AS text), 1
  FROM categories
  WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, c.parent_id,
         CAST(t.sort_path || '.' || LPAD(c.id::text, 5, '0') AS text),
         t.depth + 1
  FROM categories c
  JOIN tree t ON c.parent_id = t.id
)
SELECT depth, name, sort_path FROM tree ORDER BY sort_path;
```

---

## 防止无限循环

**基本写法：CYCLE 检测（PostgreSQL/标准）**
`<cte名>(<列>) AS (...) CYCLE <列> SET <标记列> TO <真值> DEFAULT <假值>`
```sql
-- PostgreSQL 14+ 原生环路检测
WITH RECURSIVE graph_traverse(node, path) AS (
  SELECT start_node, ARRAY[start_node]
  FROM graph WHERE start_node = 1
  UNION ALL
  SELECT g.target, gt.path || g.target
  FROM graph g
  JOIN graph_traverse gt ON g.source = gt.node
  WHERE NOT g.target = ANY(gt.path)
)
CYCLE node SET is_cycle TO true DEFAULT false USING path
SELECT node, is_cycle FROM graph_traverse;
```

---

**基本写法：路径数组防环路（通用）**
`WHERE <节点> NOT IN (<路径集合>)`
```sql
-- 通用环路防护：记录已访问节点
WITH RECURSIVE safe_traverse(node, visited) AS (
  SELECT 1, ARRAY[1]
  UNION ALL
  SELECT g.target, st.visited || g.target
  FROM graph g
  JOIN safe_traverse st ON g.source = st.node
  WHERE NOT g.target = ANY(st.visited)
)
SELECT node FROM safe_traverse;
```

---

## 多层聚合统计

**基本写法：每个节点包含子树聚合**
`WITH RECURSIVE <cte> AS (... UNION ALL SELECT <聚合> ...)`
```sql
-- 计算每个分类及其所有子分类的商品总数
WITH RECURSIVE cat_tree(id, name, parent_id, root_id) AS (
  SELECT id, name, parent_id, id AS root_id
  FROM categories
  UNION ALL
  SELECT c.id, c.name, c.parent_id, ct.root_id
  FROM categories c
  JOIN cat_tree ct ON c.parent_id = ct.id
)
SELECT ct.root_id, c.name AS 根分类, COUNT(p.id) AS 商品总数
FROM cat_tree ct
JOIN categories c ON c.id = ct.root_id
LEFT JOIN products p ON p.category_id = ct.id
GROUP BY ct.root_id, c.name;
```

---

## 图遍历（最短路径）

**基本写法：BFS 广度优先搜索**
`WITH RECURSIVE <cte>(node, dist) AS (... UNION ALL SELECT ..., dist+1 ...)`
```sql
-- 查找两点间最短跳数
WITH RECURSIVE bfs(node, distance, path) AS (
  SELECT 1, 0, ARRAY[1]              -- 起点
  UNION ALL
  SELECT e.target, b.distance + 1, b.path || e.target
  FROM edges e
  JOIN bfs b ON e.source = b.node
  WHERE NOT e.target = ANY(b.path)   -- 防环路
)
SELECT node, distance, path
FROM bfs
WHERE node = 6                       -- 终点
ORDER BY distance
LIMIT 1;                             -- 最短路径
```

---

## 递归 CTE 性能与限制

**基本写法：限制递归深度**
`<递归成员> WHERE <层级列> < <最大值>`
```sql
-- MySQL 通过 WHERE 控制；PostgreSQL 可设 max_recursive_cycles
-- MySQL: SET cte_max_recursion_depth = 1000;
-- PostgreSQL: SET max_worker_processes 不影响；用 WHERE 限制
WITH RECURSIVE limited(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM limited WHERE n < 100
)
SELECT COUNT(*) FROM limited;

-- MySQL 会话变量设置递归深度上限
SET SESSION cte_max_recursion_depth = 500;
```

---

**基本写法：UNION 与 UNION ALL 选择**
`<锚点> UNION [ALL] <递归>`
```sql
-- UNION ALL：保留所有行（含重复），速度快，适合无环路 DAG
-- UNION：去重，速度慢，适合可能产生重复路径的图
-- 树形结构（每个节点唯一父节点）用 UNION ALL 即可
-- 通用图遍历建议 UNION ALL + 路径数组防环路
```
