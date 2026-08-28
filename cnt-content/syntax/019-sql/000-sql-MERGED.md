---
order: 10
title: sql 模块文档合集
module: 'sql'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：019-sql/001-WindowFunction.md ============ -->

# 窗口函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本语法

**换行写法：OVER 子句定义窗口框架**
`<窗口函数>() OVER ([PARTITION BY <列>] [ORDER BY <列>] [frame_clause])`
```sql
-- 使用 OVER 子句定义窗口
SELECT
  column1,
  column2,
  window_function() OVER (
    PARTITION BY partition_column
    ORDER BY sort_column
  ) AS alias
FROM table_name;
```

---

## ROW_NUMBER 行号

**换行写法：全局行号**
`ROW_NUMBER() OVER (ORDER BY <列>)`
```sql
-- 按薪资降序生成全局行号
SELECT
  name,
  salary,
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```

**换行写法：分部门行号**
`ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 按部门分组后按薪资降序生成行号
SELECT
  name,
  department,
  salary,
  ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

---

## RANK 排名

**换行写法：允许并列跳号排名**
`RANK() OVER (ORDER BY <列>)`
```sql
-- 按薪资降序排名（允许并列，跳号：1, 2, 2, 4, 5）
SELECT
  name,
  salary,
  RANK() OVER (ORDER BY salary DESC) AS rank_num
FROM employees;
```

---

## DENSE_RANK 密集排名

**换行写法：允许并列不跳号排名**
`DENSE_RANK() OVER (ORDER BY <列>)`
```sql
-- 按薪资降序密集排名（允许并列，不跳号：1, 2, 2, 3, 4）
SELECT
  name,
  salary,
  DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank_num
FROM employees;
```

---

## NTILE 分桶

**换行写法：将数据分为 N 个桶**
`NTILE(<N>) OVER (ORDER BY <列>)`
```sql
-- 按薪资降序分为 4 个桶（四分位数）
SELECT
  name,
  salary,
  NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

---

## SUM OVER 累计求和

**换行写法：全局累计求和**
`SUM(<列>) OVER (ORDER BY <列>)`
```sql
-- 按日期累计求和
SELECT
  order_date,
  amount,
  SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

**换行写法：分组累计求和**
`SUM(<列>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 按部门分组后按入职日期累计求和
SELECT
  department,
  name,
  salary,
  SUM(salary) OVER (PARTITION BY department ORDER BY hire_date) AS dept_running_total
FROM employees;
```

---

## AVG OVER 移动平均

**换行写法：3 天移动平均**
`AVG(<列>) OVER (ORDER BY <列> ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)`
```sql
-- 计算 3 天移动平均价格
SELECT
  date,
  price,
  AVG(price) OVER (
    ORDER BY date
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS moving_avg_3day
FROM stock_prices;
```

---

## LAG 偏移函数

**换行写法：访问前 1 行的值**
`LAG(<列>, 1) OVER (ORDER BY <列>)`
```sql
-- 查询前一天的价格及价格变化
SELECT
  date,
  price,
  LAG(price, 1) OVER (ORDER BY date) AS prev_price,
  price - LAG(price, 1) OVER (ORDER BY date) AS price_change
FROM stock_prices;
```

**换行写法：指定偏移量和默认值**
`LAG(<列>, <offset>, <default>) OVER (ORDER BY <列>)`
```sql
-- 查询 7 天前的价格，无值时返回 0
SELECT
  date,
  price,
  LAG(price, 7, 0) OVER (ORDER BY date) AS price_7_days_ago
FROM stock_prices;
```

---

## LEAD 偏移函数

**换行写法：访问后 1 行的值**
`LEAD(<列>, 1) OVER (ORDER BY <列>)`
```sql
-- 查询后一天的价格
SELECT
  date,
  price,
  LEAD(price, 1) OVER (ORDER BY date) AS next_price
FROM stock_prices;
```

---

## FIRST_VALUE / LAST_VALUE

**换行写法：窗口首值**
`FIRST_VALUE(<列>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 查询每个部门薪资最高的员工
SELECT
  name,
  department,
  salary,
  FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) AS highest_paid
FROM employees;
```

**换行写法：窗口尾值**
`LAST_VALUE(<列>) OVER (PARTITION BY <列> ORDER BY <列> ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)`
```sql
-- 查询每个部门薪资最低的员工
SELECT
  name,
  department,
  salary,
  LAST_VALUE(name) OVER (
    PARTITION BY department
    ORDER BY salary DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS lowest_paid
FROM employees;
```

---

## CUME_DIST 累积分布

**换行写法：累积分布（0 到 1）**
`CUME_DIST() OVER (ORDER BY <列>)`
```sql
-- 计算薪资的累积分布
SELECT
  name,
  salary,
  CUME_DIST() OVER (ORDER BY salary) AS cume_dist
FROM employees;
```

---

## PERCENT_RANK 百分位排名

**换行写法：百分位排名（0 到 1）**
`PERCENT_RANK() OVER (ORDER BY <列>)`
```sql
-- 计算薪资的百分位排名
SELECT
  name,
  salary,
  PERCENT_RANK() OVER (ORDER BY salary) AS percent_rank
FROM employees;
```

---

## ROWS BETWEEN 行范围

**换行写法：从第一行到当前行**
`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
```sql
-- 累计求和（从第一行到当前行）
SUM(amount) OVER (
  ORDER BY date
  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

**换行写法：前 2 行到后 2 行**
`ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING`
```sql
-- 计算 5 天移动平均（前 2 行到后 2 行）
AVG(price) OVER (
  ORDER BY date
  ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
)
```

---

## RANGE BETWEEN 值范围

**换行写法：按逻辑值范围累计求和**
`RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
```sql
-- 同一薪资值的行被视为一组进行累计求和
SELECT
  name,
  salary,
  SUM(salary) OVER (
    ORDER BY salary
    RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total
FROM employees;
```

---

## NTH_VALUE

**换行写法：窗口第 N 行的值**
`NTH_VALUE(<列>, <N>) OVER (...)`
```sql
-- 查询每个部门薪资第 3 高的员工
SELECT
  name,
  department,
  salary,
  NTH_VALUE(salary, 3) OVER (
    PARTITION BY department
    ORDER BY salary DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS third_highest
FROM employees;
```

---

## Top-N 查询

**换行写法：ROW_NUMBER 实现 Top-N**
`ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 查询每个部门薪资前 3 名
SELECT * FROM (
  SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
  FROM employees
) ranked
WHERE rn <= 3;
```

---

## 去重

**换行写法：DISTINCT 与窗口函数去重**
`SELECT DISTINCT ... FROM (SELECT ... ROW_NUMBER() OVER (...))`
```sql
-- 去重保留每个用户的最新记录
SELECT DISTINCT user_id, latest_action
FROM (
  SELECT
    user_id,
    action AS latest_action,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at DESC) AS rn
  FROM user_actions
) t
WHERE rn = 1;
```



<!-- ============ 文档分隔线：019-sql/002-MultiTableQuery.md ============ -->

# 多表查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## INNER JOIN

**换行写法：基本内连接**
`FROM <表 1> INNER JOIN <表 2> ON <条件>`
```sql
-- 查询员工及其部门名称
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;
```

**换行写法：省略 INNER 的内连接**
`FROM <表 1> JOIN <表 2> ON <条件>`
```sql
-- 省略 INNER 关键字
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

**换行写法：多表连接**
`FROM <表 1> JOIN <表 2> ON ... JOIN <表 3> ON ...`
```sql
-- 连接订单、客户、订单项、商品四张表
SELECT o.order_id, c.name, p.product_name, oi.quantity
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

**换行写法：复合连接条件**
`FROM <表 1> JOIN <表 2> ON <条件 1> AND <条件 2>`
```sql
-- 使用复合条件连接员工和活跃部门
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id AND d.is_active = true;
```

---

## LEFT JOIN

**换行写法：左外连接返回左表全部行**
`FROM <表 1> LEFT JOIN <表 2> ON <条件>`
```sql
-- 查询所有员工及其部门（包括没有部门的员工）
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id;
```

**换行写法：左连接查找无匹配行**
`FROM <表 1> LEFT JOIN <表 2> ON <条件> WHERE <表 2>.<列> IS NULL`
```sql
-- 找出没有部门的员工
SELECT e.name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
WHERE d.id IS NULL;
```

**换行写法：多层左连接**
`FROM <表 1> LEFT JOIN <表 2> ON ... LEFT JOIN <表 3> ON ...`
```sql
-- 链式左连接用户、订单、订单项、商品
SELECT
  u.name,
  o.order_id,
  p.product_name
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
LEFT JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.id;
```

---

## RIGHT JOIN

**换行写法：右外连接返回右表全部行**
`FROM <表 1> RIGHT JOIN <表 2> ON <条件>`
```sql
-- 查询所有部门及其员工（包括没有员工的部门）
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;
```

---

## FULL JOIN

**换行写法：全外连接返回两表所有行**
`FROM <表 1> FULL JOIN <表 2> ON <条件>`
```sql
-- 返回员工和部门的所有行
SELECT e.name, d.department_name
FROM employees e
FULL JOIN departments d ON e.dept_id = d.id;
```

**换行写法：全外连接查找不匹配行**
`FROM <表 1> FULL JOIN <表 2> ON <条件> WHERE <表 1>.<id> IS NULL OR <表 2>.<id> IS NULL`
```sql
-- 查找两表不匹配的行
SELECT e.name, d.department_name
FROM employees e
FULL JOIN departments d ON e.dept_id = d.id
WHERE e.id IS NULL OR d.id IS NULL;
```

**换行写法：MySQL 用 UNION 模拟全外连接**
`LEFT JOIN ... UNION RIGHT JOIN ...`
```sql
-- MySQL 不支持 FULL JOIN，用 UNION 模拟
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
UNION
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;
```

---

## CROSS JOIN

**换行写法：显式交叉连接**
`FROM <表 1> CROSS JOIN <表 2>`
```sql
-- 生成部门和职级的笛卡尔积
SELECT d.department_name, j.job_level
FROM departments d
CROSS JOIN job_levels j;
```

**换行写法：隐式交叉连接**
`FROM <表 1>, <表 2>`
```sql
-- 使用逗号分隔的隐式交叉连接
SELECT d.department_name, j.job_level
FROM departments d, job_levels j;
```

---

## 自连接

**换行写法：员工与经理关系**
`FROM <表> AS <别名 1> LEFT JOIN <表> AS <别名 2> ON <条件>`
```sql
-- 查询员工及其经理
SELECT
  e.name AS employee,
  m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：组织层级查询（固定层级）**
`FROM <表> AS <别名 1> LEFT JOIN <表> AS <别名 2> ON ... LEFT JOIN <表> AS <别名 3> ON ...`
```sql
-- 查询三级组织层级
SELECT
  e3.name AS level3,
  e2.name AS level2,
  e1.name AS level1
FROM employees e1
LEFT JOIN employees e2 ON e2.manager_id = e1.id
LEFT JOIN employees e3 ON e3.manager_id = e2.id
WHERE e1.manager_id IS NULL;
```

---

## 标量子查询

**换行写法：WHERE 中的标量子查询**
`WHERE <列> <运算符> (SELECT ...)`
```sql
-- 查询薪资高于平均值的员工
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**换行写法：SELECT 中的标量子查询**
`SELECT <列>, (SELECT ...) AS <别名> FROM <表名>`
```sql
-- 查询员工薪资与平均薪资的差值
SELECT
  name,
  salary,
  (SELECT AVG(salary) FROM employees) AS avg_salary,
  salary - (SELECT AVG(salary) FROM employees) AS diff
FROM employees;
```

---

## 列子查询

**换行写法：ANY 与子查询任一值比较**
`WHERE <列> <运算符> ANY (SELECT ...)`
```sql
-- 查询薪资高于部门 5 中任一员工的员工
SELECT name, salary FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = 5);
```

**换行写法：= ANY 等价于 IN**
`WHERE <列> = ANY (SELECT ...)`
```sql
-- 查询东部地区部门的员工
SELECT name, salary FROM employees
WHERE dept_id = ANY (SELECT id FROM departments WHERE region = 'East');
```

**换行写法：ALL 与子查询所有值比较**
`WHERE <列> <运算符> ALL (SELECT ...)`
```sql
-- 查询薪资高于部门 5 中所有员工的员工
SELECT name, salary FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE dept_id = 5);
```

---

## 表子查询

**换行写法：FROM 中的派生表**
`FROM (SELECT ...) AS <别名>`
```sql
-- 查询平均薪资大于 50000 的部门
SELECT dept_name, avg_salary
FROM (
  SELECT department AS dept_name, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) AS dept_stats
WHERE avg_salary > 50000;
```

**换行写法：多列 IN 子查询**
`WHERE (<列 1>, <列 2>) IN (SELECT ...)`
```sql
-- 查询每个客户最新订单
SELECT * FROM orders
WHERE (customer_id, order_date) IN (
  SELECT customer_id, MAX(order_date)
  FROM orders
  GROUP BY customer_id
);
```

---

## 相关子查询

**换行写法：相关子查询引用外层查询列**
`WHERE <列> = (SELECT ... FROM ... WHERE ... = <外层列>)`
```sql
-- 查询每个部门薪资最高的员工
SELECT name, department, salary
FROM employees e
WHERE salary = (
  SELECT MAX(salary)
  FROM employees e2
  WHERE e2.department = e.department
);
```

---

## EXISTS 与 IN

**换行写法：EXISTS 检查子查询是否返回行**
`WHERE EXISTS (SELECT 1 FROM ... WHERE ...)`
```sql
-- 查询有薪资超过 100000 员工的部门
SELECT d.department_name
FROM departments d
WHERE EXISTS (
  SELECT 1 FROM employees e
  WHERE e.dept_id = d.id AND e.salary > 100000
);
```

**换行写法：IN 检查值是否在子查询结果中**
`WHERE <列> IN (SELECT ...)`
```sql
-- 查询有薪资超过 100000 员工的部门
SELECT d.department_name
FROM departments d
WHERE d.id IN (
  SELECT dept_id FROM employees WHERE salary > 100000
);
```

**换行写法：NOT EXISTS 避免 NULL 陷阱**
`WHERE NOT EXISTS (SELECT 1 FROM ... WHERE ...)`
```sql
-- 查询部门中没有薪资超过 100000 员工的部门
SELECT name FROM employees e
WHERE NOT EXISTS (
  SELECT 1 FROM employees e2
  WHERE e2.dept_id = e.dept_id AND e2.salary > 100000
);
```

---

## JOIN 性能建议

**换行写法：小表驱动大表**
`FROM <小表> JOIN <大表> ON ...`
```sql
-- 小表在左驱动大表
SELECT * FROM small_table s JOIN big_table b ON s.id = b.small_id;
```

**单行写法：连接列上建索引**
`CREATE INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在订单表的 customer_id 上建索引
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
```

**换行写法：避免在 JOIN 条件上使用函数**
`FROM <表 1> JOIN <表 2> ON <表 1>.<列> = <表 2>.<列>`
```sql
-- 直接使用列值连接（推荐）
SELECT * FROM users u JOIN orders o ON u.email = o.email;
```



<!-- ============ 文档分隔线：019-sql/003-CTE.md ============ -->

# 公用表表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本 CTE

**换行写法：定义基本 CTE**
`WITH <CTE 名> AS (SELECT ...) SELECT ... FROM <CTE 名>`
```sql
-- 定义 CTE 查询高薪员工
WITH high_paid AS (
  SELECT id, name, salary FROM employees WHERE salary > 80000
)
SELECT * FROM high_paid ORDER BY salary DESC;
```

**换行写法：定义多个 CTE**
`WITH <CTE 1> AS (...), <CTE 2> AS (...) SELECT ...`
```sql
-- 定义多个 CTE 并联合查询
WITH
  high_paid AS (
    SELECT id, name, salary FROM employees WHERE salary > 80000
  ),
  dept_count AS (
    SELECT dept_id, COUNT(*) AS cnt FROM employees GROUP BY dept_id
  )
SELECT h.name, h.salary, d.cnt
FROM high_paid h
JOIN dept_count d ON h.dept_id = d.dept_id;
```

**换行写法：CTE 中引用前一个 CTE**
`WITH <CTE 1> AS (...), <CTE 2> AS (... FROM <CTE 1>) SELECT ...`
```sql
-- 后一个 CTE 引用前一个 CTE
WITH
  active_users AS (
    SELECT id, name FROM users WHERE status = 'active'
  ),
  active_orders AS (
    SELECT o.* FROM orders o
    JOIN active_users au ON o.user_id = au.id
  )
SELECT * FROM active_orders;
```

---

## 递归 CTE

**换行写法：递归 CTE 基本结构**
`WITH RECURSIVE <CTE 名> AS (非递归部分 UNION ALL 递归部分) SELECT ...`
```sql
-- 递归 CTE 基本结构
WITH RECURSIVE counter(n) AS (
  SELECT 1          -- 非递归部分（锚点）
  UNION ALL
  SELECT n + 1     -- 递归部分
  FROM counter
  WHERE n < 10
)
SELECT * FROM counter;
```

**换行写法：组织树形结构查询**
`WITH RECURSIVE <CTE 名> AS (锚点 UNION ALL 递归) SELECT ...`
```sql
-- 查询员工及其所有下属（组织树）
WITH RECURSIVE org_tree AS (
  -- 锚点：顶层管理者
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  -- 递归：下属员工
  SELECT e.id, e.name, e.manager_id, ot.level + 1
  FROM employees e
  JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT * FROM org_tree ORDER BY level, name;
```

**换行写法：路径字符串拼接**
`WITH RECURSIVE <CTE 名> AS (... <路径列> ...) SELECT ...`
```sql
-- 查询组织树并拼接路径
WITH RECURSIVE org_tree AS (
  SELECT id, name, manager_id, CAST(name AS VARCHAR(1000)) AS path
  FROM employees
  WHERE manager_id IS NULL

  UNION ALL

  SELECT e.id, e.name, e.manager_id, ot.path || ' > ' || e.name
  FROM employees e
  JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT id, path FROM org_tree;
```

**换行写法：分类树形结构查询**
`WITH RECURSIVE <CTE 名> AS (锚点 UNION ALL 递归) SELECT ...`
```sql
-- 查询商品分类树
WITH RECURSIVE category_tree AS (
  SELECT id, name, parent_id, 1 AS level
  FROM categories
  WHERE parent_id IS NULL

  UNION ALL

  SELECT c.id, c.name, c.parent_id, ct.level + 1
  FROM categories c
  JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree ORDER BY level, name;
```

---

## CTE 与子查询对比

**换行写法：子查询写法**
`SELECT ... FROM (SELECT ...) AS <别名>`
```sql
-- 使用子查询查询高薪员工
SELECT * FROM (
  SELECT id, name, salary FROM employees WHERE salary > 80000
) AS high_paid
ORDER BY salary DESC;
```

**换行写法：CTE 写法（可读性更好）**
`WITH <CTE 名> AS (SELECT ...) SELECT ... FROM <CTE 名>`
```sql
-- 使用 CTE 改写子查询
WITH high_paid AS (
  SELECT id, name, salary FROM employees WHERE salary > 80000
)
SELECT * FROM high_paid ORDER BY salary DESC;
```

---

## CTE 与窗口函数

**换行写法：CTE 中使用窗口函数**
`WITH <CTE 名> AS (SELECT ... <窗口函数> OVER (...)) SELECT ...`
```sql
-- 使用 CTE 和窗口函数查询每个部门薪资前 3 名
WITH ranked_employees AS (
  SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
  FROM employees
)
SELECT name, department, salary
FROM ranked_employees
WHERE rn <= 3;
```

---

## CTE 在 DML 中使用

**换行写法：CTE 用于 INSERT**
`WITH <CTE 名> AS (...) INSERT INTO <表名> SELECT ... FROM <CTE 名>`
```sql
-- 使用 CTE 批量插入高薪员工到奖金表
WITH high_paid AS (
  SELECT id, name, salary FROM employees WHERE salary > 80000
)
INSERT INTO bonus (employee_id, bonus_amount)
SELECT id, salary * 0.1 FROM high_paid;
```

**换行写法：CTE 用于 UPDATE**
`WITH <CTE 名> AS (...) UPDATE <表名> SET ... FROM <CTE 名>`
```sql
-- 使用 CTE 更新员工薪资
WITH dept_avg AS (
  SELECT dept_id, AVG(salary) AS avg_sal
  FROM employees
  GROUP BY dept_id
)
UPDATE employees e
SET salary = da.avg_sal
FROM dept_avg da
WHERE e.dept_id = da.dept_id AND e.salary < da.avg_sal;
```

**换行写法：CTE 用于 DELETE**
`WITH <CTE 名> AS (...) DELETE FROM <表名> WHERE <列> IN (SELECT ... FROM <CTE 名>)`
```sql
-- 使用 CTE 删除没有订单的客户
WITH inactive_customers AS (
  SELECT c.id FROM customers c
  LEFT JOIN orders o ON c.id = o.customer_id
  WHERE o.id IS NULL
)
DELETE FROM customers
WHERE id IN (SELECT id FROM inactive_customers);
```



<!-- ============ 文档分隔线：019-sql/004-FilterCondition.md ============ -->

# 过滤条件

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## WHERE 基本语法

**换行写法：WHERE 子句过滤行**
`SELECT <select_list> FROM <table_source> WHERE <search_condition>;`
```sql
-- 使用 WHERE 子句过滤满足条件的行
SELECT select_list
FROM table_source
WHERE search_condition;
```

---

## 比较运算符

**单行写法：等于比较**
`WHERE <列> = <值>;`
```sql
-- 查询年龄等于 25 的记录
SELECT * FROM users WHERE age = 25;
```

**单行写法：不等于比较**
`WHERE <列> <> <值>;`
```sql
-- 查询状态不为 closed 的订单
SELECT * FROM orders WHERE status <> 'closed';
```

**单行写法：小于比较**
`WHERE <列> < <值>;`
```sql
-- 查询价格小于 100 的商品
SELECT * FROM products WHERE price < 100;
```

**单行写法：大于比较**
`WHERE <列> > <值>;`
```sql
-- 查询薪资大于 50000 的员工
SELECT * FROM employees WHERE salary > 50000;
```

**单行写法：小于等于比较**
`WHERE <列> <= <值>;`
```sql
-- 查询库存小于等于 0 的商品
SELECT * FROM products WHERE quantity <= 0;
```

**单行写法：大于等于比较**
`WHERE <列> >= <值>;`
```sql
-- 查询成绩大于等于 60 的记录
SELECT * FROM exams WHERE score >= 60;
```

---

## 安全等于运算符

**单行写法：MySQL NULL 安全等于**
`WHERE <列> <=> <值>;`
```sql
-- 查询手机号为 NULL 的用户（等价于 IS NULL）
SELECT * FROM users WHERE phone <=> NULL;
```

**单行写法：IS DISTINCT FROM**
`WHERE <列> IS DISTINCT FROM <值>;`
```sql
-- 查询手机号不为 NULL 的用户（等价于 IS NOT NULL）
SELECT * FROM users WHERE phone IS DISTINCT FROM NULL;
```

**单行写法：IS NOT DISTINCT FROM**
`WHERE <列> IS NOT DISTINCT FROM <值>;`
```sql
-- 查询手机号为 NULL 的用户（等价于 IS NULL）
SELECT * FROM users WHERE phone IS NOT DISTINCT FROM NULL;
```

---

## 逻辑运算符

**单行写法：AND 组合条件**
`WHERE <条件 1> AND <条件 2>;`
```sql
-- 查询部门 ID 为 5 且薪资大于 50000 的员工
SELECT * FROM employees
WHERE dept_id = 5 AND salary > 50000;
```

**单行写法：OR 组合条件**
`WHERE <条件 1> OR <条件 2>;`
```sql
-- 查询部门 ID 为 5 或 10 的员工
SELECT * FROM employees
WHERE dept_id = 5 OR dept_id = 10;
```

**单行写法：NOT 取反条件**
`WHERE NOT (<条件>);`
```sql
-- 查询部门 ID 不为 5 且不为 10 的员工
SELECT * FROM employees
WHERE NOT (dept_id = 5 OR dept_id = 10);
```

**换行写法：运算符优先级（AND 优先于 OR）**
`WHERE <条件 1> OR <条件 2> AND <条件 3>;`
```sql
-- AND 优先于 OR，等价于 category = 'A' OR (category = 'B' AND price > 100)
SELECT * FROM products
WHERE category = 'A' OR category = 'B' AND price > 100;
```

**换行写法：括号改变优先级**
`WHERE (<条件 1> OR <条件 2>) AND <条件 3>;`
```sql
-- 使用括号改变优先级
SELECT * FROM products
WHERE (category = 'A' OR category = 'B') AND price > 100;
```

---

## IN 运算符

**单行写法：离散值匹配**
`WHERE <列> IN (<值 1>, <值 2>, ...);`
```sql
-- 查询状态为待处理、处理中、已发货的订单
SELECT * FROM orders
WHERE status IN ('pending', 'processing', 'shipped');
```

**单行写法：排除离散值**
`WHERE <列> NOT IN (<值 1>, <值 2>, ...);`
```sql
-- 查询状态不为已取消、已退货的订单
SELECT * FROM orders
WHERE status NOT IN ('cancelled', 'returned');
```

**换行写法：子查询中的 IN**
`WHERE <列> IN (SELECT ...);`
```sql
-- 查询 VIP 等级大于等于 3 的用户的订单
SELECT * FROM orders
WHERE user_id IN (
    SELECT id FROM users WHERE vip_level >= 3
);
```

---

## BETWEEN 运算符

**单行写法：范围查询（包含边界）**
`WHERE <列> BETWEEN <下界> AND <上界>;`
```sql
-- 查询价格在 100 到 500 之间的商品
SELECT * FROM products
WHERE price BETWEEN 100 AND 500;
```

**单行写法：排除范围**
`WHERE <列> NOT BETWEEN <下界> AND <上界>;`
```sql
-- 查询价格不在 100 到 500 之间的商品
SELECT * FROM products
WHERE price NOT BETWEEN 100 AND 500;
```

**单行写法：日期范围查询**
`WHERE <列> BETWEEN DATE '<开始>' AND DATE '<结束>';`
```sql
-- 查询 2026 年上半年的订单
SELECT * FROM orders
WHERE created_at BETWEEN DATE '2026-01-01' AND DATE '2026-06-30';
```

**换行写法：时间戳范围查询（避免精度问题）**
`WHERE <列> >= <开始> AND <列> < <结束>;`
```sql
-- 查询 2026-06-14 全天的日志（避免 BETWEEN 精度问题）
SELECT * FROM logs
WHERE created_at >= '2026-06-14 00:00:00'
  AND created_at < '2026-06-15 00:00:00';
```

---

## LIKE 运算符

**单行写法：前缀匹配**
`WHERE <列> LIKE '<前缀>%';`
```sql
-- 查询姓"张"的用户（可利用索引）
SELECT * FROM users WHERE name LIKE '张%';
```

**单行写法：后缀匹配**
`WHERE <列> LIKE '%<后缀>';`
```sql
-- 查询名字以"明"结尾的用户（无法利用普通索引）
SELECT * FROM users WHERE name LIKE '%明';
```

**单行写法：包含匹配**
`WHERE <列> LIKE '%<关键字>%';`
```sql
-- 查询名字包含"华"的用户
SELECT * FROM users WHERE name LIKE '%华%';
```

**单行写法：单字符匹配**
`WHERE <列> LIKE '<前缀>_<后缀>';`
```sql
-- 查询"张三"、"张四"等两字姓名
SELECT * FROM users WHERE name LIKE '张_';
```

**单行写法：ESCAPE 转义特殊字符**
`WHERE <列> LIKE '<模式>' ESCAPE '<转义字符>';`
```sql
-- 查找文件名为"100%"的记录
SELECT * FROM files WHERE filename LIKE '100\%' ESCAPE '\';
```

---

## 正则表达式匹配

**单行写法：PostgreSQL 正则匹配**
`WHERE <列> ~ '<正则>';`
```sql
-- 查询姓张、三、四、五的用户
SELECT * FROM users WHERE name ~ '^张[三四五]$';
```

**单行写法：MySQL 正则匹配**
`WHERE <列> REGEXP '<正则>';`
```sql
-- 查询姓张、三、四、五的用户
SELECT * FROM users WHERE name REGEXP '^张[三四五]$';
```

**单行写法：SQL 标准模式匹配**
`WHERE <列> SIMILAR TO '<模式>';`
```sql
-- 查询姓张、三、四、五的用户
SELECT * FROM users WHERE name SIMILAR TO '张(三|四|五)';
```

---

## IS NULL / IS NOT NULL

**单行写法：检查 NULL 值**
`WHERE <列> IS NULL;`
```sql
-- 查询没有手机号的用户
SELECT * FROM users WHERE phone IS NULL;
```

**单行写法：检查非 NULL 值**
`WHERE <列> IS NOT NULL;`
```sql
-- 查询有手机号的用户
SELECT * FROM users WHERE phone IS NOT NULL;
```

**换行写法：多列 NULL 检查**
`WHERE <列 1> IS NULL AND <列 2> IS NOT NULL;`
```sql
-- 查询已付款但未发货的订单
SELECT * FROM orders
WHERE shipping_date IS NULL AND payment_date IS NOT NULL;
```

---

## NULL 相关函数

**单行写法：COALESCE 返回第一个非 NULL 参数**
`SELECT COALESCE(<列 1>, <列 2>, <默认值>) FROM <表名>;`
```sql
-- 查询用户联系方式，优先手机号，其次邮箱，最后显示 N/A
SELECT COALESCE(phone, email, 'N/A') AS contact FROM users;
```

**单行写法：NULLIF 相等返回 NULL**
`SELECT NULLIF(<列 1>, <列 2>) FROM <表名>;`
```sql
-- 查询成绩，为 0 时返回 NULL 避免除零
SELECT NULLIF(score, 0) AS safe_score FROM exams;
```

**单行写法：MySQL IFNULL**
`SELECT IFNULL(<列>, <默认值>) FROM <表名>;`
```sql
-- 查询用户手机号，未填写则显示 N/A
SELECT IFNULL(phone, 'N/A') FROM users;
```

---

## SARGable 条件

**单行写法：非 SARGable 条件（无法利用索引）**
`WHERE <函数>(<列>) = <值>;`
```sql
-- 对列使用函数导致无法利用索引
SELECT * FROM orders WHERE YEAR(created_at) = 2026;
```

**换行写法：SARGable 条件改写（可利用索引）**
`WHERE <列> >= <开始> AND <列> < <结束>;`
```sql
-- 改写为范围查询以利用索引
SELECT * FROM orders WHERE created_at >= '2026-01-01' AND created_at < '2027-01-01';
```



<!-- ============ 文档分隔线：019-sql/005-SetOperation.md ============ -->

# 集合操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## UNION

**换行写法：UNION 合并去重**
`<查询 1> UNION <查询 2>`
```sql
-- 合并 2025 年和 2026 年的客户（自动去重）
SELECT customer_id FROM orders_2025
UNION
SELECT customer_id FROM orders_2026;
```

**换行写法：UNION 合并多表**
`<查询 1> UNION <查询 2> UNION <查询 3>`
```sql
-- 合并三年的客户
SELECT customer_id FROM orders_2024
UNION
SELECT customer_id FROM orders_2025
UNION
SELECT customer_id FROM orders_2026;
```

---

## UNION ALL

**换行写法：UNION ALL 合并不去重**
`<查询 1> UNION ALL <查询 2>`
```sql
-- 合并 2025 年和 2026 年的客户（保留重复）
SELECT customer_id FROM orders_2025
UNION ALL
SELECT customer_id FROM orders_2026;
```

**换行写法：UNION ALL 合并不同表**
`<查询 1> UNION ALL <查询 2>`
```sql
-- 合并活跃用户和归档用户
SELECT id, name, email FROM active_users
UNION ALL
SELECT id, name, email FROM archived_users;
```

---

## INTERSECT

**换行写法：INTERSECT 交集**
`<查询 1> INTERSECT <查询 2>`
```sql
-- 查询两年都下单的客户
SELECT customer_id FROM orders_2025
INTERSECT
SELECT customer_id FROM orders_2026;
```

**换行写法：INTERSECT 多查询交集**
`<查询 1> INTERSECT <查询 2> INTERSECT <查询 3>`
```sql
-- 查询三年都下单的客户
SELECT customer_id FROM orders_2024
INTERSECT
SELECT customer_id FROM orders_2025
INTERSECT
SELECT customer_id FROM orders_2026;
```

---

## EXCEPT

**换行写法：EXCEPT 差集**
`<查询 1> EXCEPT <查询 2>`
```sql
-- 查询 2025 年下单但 2026 年未下单的客户
SELECT customer_id FROM orders_2025
EXCEPT
SELECT customer_id FROM orders_2026;
```

**换行写法：MySQL 用 LEFT JOIN 模拟 EXCEPT**
`SELECT ... FROM <表 1> LEFT JOIN <表 2> ON ... WHERE <表 2>.<列> IS NULL`
```sql
-- MySQL 不支持 EXCEPT，使用 LEFT JOIN 模拟
SELECT a.customer_id
FROM orders_2025 a
LEFT JOIN orders_2026 b ON a.customer_id = b.customer_id
WHERE b.customer_id IS NULL;
```

---

## 集合操作排序

**换行写法：UNION 结果排序**
`<查询 1> UNION <查询 2> ORDER BY <列>`
```sql
-- 合并结果后按 customer_id 排序
SELECT customer_id FROM orders_2025
UNION
SELECT customer_id FROM orders_2026
ORDER BY customer_id;
```

**换行写法：UNION ALL 结果带来源标记排序**
`SELECT ..., '<来源>' AS source FROM ... UNION ALL ... ORDER BY <列>`
```sql
-- 合并结果并标记来源，按 customer_id 排序
SELECT customer_id, '2025' AS year FROM orders_2025
UNION ALL
SELECT customer_id, '2026' AS year FROM orders_2026
ORDER BY customer_id, year;
```

---

## 集合操作规则

**换行写法：列数和类型必须一致**
`SELECT <列 1>, <列 2> UNION SELECT <列 1>, <列 2>`
```sql
-- 两个查询的列数和数据类型必须一致
SELECT name, email FROM active_users
UNION
SELECT name, email FROM archived_users;
```

**换行写法：使用 NULL 占位对齐列数**
`SELECT <列 1>, NULL AS <列 2> UNION SELECT <列 1>, <列 2>`
```sql
-- 使用 NULL 占位使列数一致
SELECT name, email, phone FROM users
UNION
SELECT name, email, NULL FROM archived_users;
```

---

## 集合操作优先级

**换行写法：INTERSECT 优先于 UNION**
`<查询 1> UNION <查询 2> INTERSECT <查询 3>`
```sql
-- INTERSECT 先执行，再执行 UNION
-- 等价于：查询 1 UNION (查询 2 INTERSECT 查询 3)
SELECT customer_id FROM orders_2024
UNION
SELECT customer_id FROM orders_2025
INTERSECT
SELECT customer_id FROM orders_2026;
```

**换行写法：括号改变优先级**
`(<查询 1> UNION <查询 2>) INTERSECT <查询 3>`
```sql
-- 使用括号改变优先级
(SELECT customer_id FROM orders_2024
 UNION
 SELECT customer_id FROM orders_2025)
INTERSECT
SELECT customer_id FROM orders_2026;
```



<!-- ============ 文档分隔线：019-sql/006-AggregateFunction.md ============ -->

# 聚合函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## COUNT 统计

**单行写法：统计所有行（包括 NULL）**
`SELECT COUNT(*) FROM <表名>;`
```sql
-- 统计员工总数
SELECT COUNT(*) FROM employees;
```

**单行写法：统计非 NULL 行数**
`SELECT COUNT(<列>) FROM <表名>;`
```sql
-- 统计有手机号的员工数
SELECT COUNT(phone) FROM employees;
```

**单行写法：统计去重后的行数**
`SELECT COUNT(DISTINCT <列>) FROM <表名>;`
```sql
-- 统计不同部门的数量
SELECT COUNT(DISTINCT department) FROM employees;
```

---

## SUM 求和

**单行写法：求和（自动忽略 NULL）**
`SELECT SUM(<列>) AS <别名> FROM <表名>;`
```sql
-- 计算所有员工薪资总和
SELECT SUM(salary) AS total_salary FROM employees;
```

**单行写法：去重后求和**
`SELECT SUM(DISTINCT <列>) FROM <表名>;`
```sql
-- 去重后计算薪资总和
SELECT SUM(DISTINCT salary) FROM employees;
```

---

## AVG 平均值

**单行写法：平均值（自动忽略 NULL）**
`SELECT AVG(<列>) AS <别名> FROM <表名>;`
```sql
-- 计算员工平均薪资
SELECT AVG(salary) AS avg_salary FROM employees;
```

**单行写法：去重后求平均**
`SELECT AVG(DISTINCT <列>) FROM <表名>;`
```sql
-- 去重后计算平均薪资
SELECT AVG(DISTINCT salary) FROM employees;
```

---

## MAX / MIN 最值

**单行写法：最大值与最小值**
`SELECT MAX(<列>) AS <别名 1>, MIN(<列>) AS <别名 2> FROM <表名>;`
```sql
-- 查询最高薪资和最低薪资
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary
FROM employees;
```

**单行写法：日期最值**
`SELECT MAX(<日期列>) AS <别名 1>, MIN(<日期列>) AS <别名 2> FROM <表名>;`
```sql
-- 查询最新入职日期和最早入职日期
SELECT MAX(hire_date) AS latest_hire, MIN(hire_date) AS earliest_hire
FROM employees;
```

---

## GROUP BY 分组

**换行写法：按单列分组聚合**
`SELECT <分组列>, <聚合函数> FROM <表名> GROUP BY <分组列>;`
```sql
-- 按部门分组统计员工数和平均薪资
SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

**换行写法：按多列分组聚合**
`SELECT <列 1>, <列 2>, <聚合函数> FROM <表名> GROUP BY <列 1>, <列 2>;`
```sql
-- 按部门和职位分组统计
SELECT department, job_title, COUNT(*) AS cnt, AVG(salary) AS avg_salary
FROM employees
GROUP BY department, job_title;
```

**换行写法：GROUP BY 与 ORDER BY**
`SELECT <列>, <聚合函数> FROM <表名> GROUP BY <列> ORDER BY <聚合函数> DESC;`
```sql
-- 按部门分组并按平均薪资降序排列
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

---

## HAVING 分组过滤

**换行写法：分组后过滤**
`HAVING <分组条件>;`
```sql
-- 查询员工数大于 5 且平均薪资大于 50000 的部门
SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 5 AND AVG(salary) > 50000;
```

**换行写法：WHERE 与 HAVING 区别**
`WHERE <行条件> ... GROUP BY ... HAVING <组条件>;`
```sql
-- 先过滤 2024 年后入职的员工，再按部门分组过滤
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE hire_date >= '2024-01-01'
GROUP BY department
HAVING COUNT(*) > 3;
```

---

## GROUP_CONCAT 字符串聚合

**换行写法：MySQL 分组拼接字符串**
`GROUP_CONCAT([DISTINCT] <列> [ORDER BY <列>] SEPARATOR '<分隔符>')`
```sql
-- 按部门分组拼接员工姓名
SELECT
  department,
  GROUP_CONCAT(name SEPARATOR ', ') AS employees
FROM employees
GROUP BY department;
```

**换行写法：去重拼接**
`GROUP_CONCAT(DISTINCT <列> ORDER BY <列> SEPARATOR '<分隔符>')`
```sql
-- 按部门分组去重拼接职位
SELECT
  department,
  GROUP_CONCAT(DISTINCT job_title ORDER BY job_title SEPARATOR ', ') AS titles
FROM employees
GROUP BY department;
```

---

## STRING_AGG 字符串聚合

**换行写法：PostgreSQL/SQL Server 字符串聚合**
`STRING_AGG(<列>, '<分隔符>')`
```sql
-- 按部门分组拼接员工姓名
SELECT
  department,
  STRING_AGG(name, ', ') AS employees
FROM employees
GROUP BY department;
```

**换行写法：带排序的拼接**
`STRING_AGG(<列>, '<分隔符>' ORDER BY <列> DESC)`
```sql
-- 按部门分组按薪资降序拼接员工姓名
SELECT
  department,
  STRING_AGG(name, ', ' ORDER BY salary DESC) AS employees
FROM employees
GROUP BY department;
```

---

## 统计聚合函数

**单行写法：样本标准差**
`SELECT STDDEV(<列>) AS <别名> FROM <表名>;`
```sql
-- 计算薪资的样本标准差
SELECT STDDEV(salary) AS salary_std FROM employees;
```

**单行写法：总体标准差**
`SELECT STDDEV_POP(<列>) AS <别名> FROM <表名>;`
```sql
-- 计算薪资的总体标准差
SELECT STDDEV_POP(salary) AS salary_std_pop FROM employees;
```

**单行写法：样本方差**
`SELECT VARIANCE(<列>) AS <别名> FROM <表名>;`
```sql
-- 计算薪资的样本方差
SELECT VARIANCE(salary) AS salary_var FROM employees;
```

**单行写法：总体方差**
`SELECT VAR_POP(<列>) AS <别名> FROM <表名>;`
```sql
-- 计算薪资的总体方差
SELECT VAR_POP(salary) AS salary_var_pop FROM employees;
```

---

## 布尔聚合

**换行写法：PostgreSQL 布尔聚合**
`BOOL_AND(<表达式>) | BOOL_OR(<表达式>)`
```sql
-- 按部门统计是否全部高薪及是否存在超高薪
SELECT
  department,
  BOOL_AND(salary > 50000) AS all_high_paid,
  BOOL_OR(salary > 100000) AS any_high_paid
FROM employees
GROUP BY department;
```

**换行写法：MySQL 等价写法**
`MIN(<表达式>) | MAX(<表达式>)`
```sql
-- MySQL 使用 MIN/MAX 模拟 BOOL_AND/BOOL_OR
SELECT
  department,
  MIN(salary > 50000) AS all_high_paid,
  MAX(salary > 100000) AS any_high_paid
FROM employees
GROUP BY department;
```

---

## JSON 聚合

**换行写法：聚合为 JSON 数组**
`JSON_ARRAYAGG(<列|表达式>)`
```sql
-- 按部门分组将员工姓名聚合为 JSON 数组
SELECT
  department,
  JSON_ARRAYAGG(name) AS employee_names
FROM employees
GROUP BY department;
```

**换行写法：聚合为 JSON 对象**
`JSON_OBJECTAGG(<键列>, <值列>)`
```sql
-- 按部门分组将姓名和薪资聚合为 JSON 对象
SELECT
  department,
  JSON_OBJECTAGG(name, salary) AS name_salary_map
FROM employees
GROUP BY department;
```



<!-- ============ 文档分隔线：019-sql/007-JoinQuery.md ============ -->

# 连接查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## INNER JOIN

**换行写法：内连接返回两表匹配行**
`FROM <左表> INNER JOIN <右表> ON <条件>`
```sql
-- 查询员工及其所属部门名称
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.id;
```

**换行写法：省略 INNER 的内连接**
`FROM <左表> JOIN <右表> ON <条件>`
```sql
-- 省略 INNER 关键字的内连接
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

**换行写法：非等值连接**
`FROM <左表> JOIN <右表> ON <非等值条件>`
```sql
-- 根据薪资范围匹配薪资等级
SELECT e.name, g.grade
FROM employees e
JOIN salary_grades g ON e.salary BETWEEN g.min_salary AND g.max_salary;
```

**换行写法：多表连接**
`FROM <表 1> JOIN <表 2> ON ... JOIN <表 3> ON ...`
```sql
-- 连接员工表、部门表和职位表
SELECT e.name, d.dept_name, j.job_title
FROM employees e
JOIN departments d ON e.dept_id = d.id
JOIN jobs j ON e.job_id = j.id
WHERE d.region = 'East';
```

---

## LEFT JOIN

**换行写法：左外连接返回左表全部行**
`FROM <左表> LEFT JOIN <右表> ON <条件>`
```sql
-- 查询所有部门及其员工（包括没有员工的部门）
SELECT d.dept_name, e.name
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id;
```

**换行写法：左连接查找无匹配行**
`FROM <左表> LEFT JOIN <右表> ON <条件> WHERE <右表>.<列> IS NULL`
```sql
-- 查找没有员工的部门
SELECT d.dept_name
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id
WHERE e.id IS NULL;
```

**换行写法：左连接统计含零值分组**
`FROM <左表> LEFT JOIN <右表> ON <条件> GROUP BY ...`
```sql
-- 统计每个部门的员工数（包括 0 人部门）
SELECT d.dept_name, COUNT(e.id) AS emp_count
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id
GROUP BY d.id, d.dept_name;
```

**换行写法：左连接右表过滤条件放 ON 子句**
`FROM <左表> LEFT JOIN <右表> ON <条件> AND <右表过滤>`
```sql
-- 查询所有部门及活跃状态的员工（右表过滤条件放 ON 子句）
SELECT d.dept_name, e.name
FROM departments d
LEFT JOIN employees e ON d.id = e.dept_id AND e.status = 'active';
```

---

## RIGHT JOIN

**换行写法：右外连接返回右表全部行**
`FROM <左表> RIGHT JOIN <右表> ON <条件>`
```sql
-- 查询所有部门及其员工（包括没有员工的部门）
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id;
```

---

## FULL JOIN

**换行写法：全外连接返回两表所有行**
`FROM <左表> FULL JOIN <右表> ON <条件>`
```sql
-- 返回员工和部门的所有行，不匹配时填 NULL
SELECT e.name, d.dept_name
FROM employees e
FULL JOIN departments d ON e.dept_id = d.id;
```

**换行写法：全外连接查找不匹配行**
`FROM <左表> FULL JOIN <右表> ON <条件> WHERE <左表>.<id> IS NULL OR <右表>.<id> IS NULL`
```sql
-- 查找两表不匹配的行
SELECT e.name, d.dept_name
FROM employees e
FULL JOIN departments d ON e.dept_id = d.id
WHERE e.id IS NULL OR d.id IS NULL;
```

**换行写法：MySQL 用 UNION ALL 模拟全外连接**
`LEFT JOIN ... UNION ALL RIGHT JOIN ... WHERE IS NULL`
```sql
-- MySQL 不支持 FULL JOIN，使用 UNION ALL 替代
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.id
UNION ALL
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.id
WHERE e.id IS NULL;
```

---

## CROSS JOIN

**换行写法：显式交叉连接（笛卡尔积）**
`FROM <左表> CROSS JOIN <右表>`
```sql
-- 生成部门和职位的笛卡尔积
SELECT d.dept_name, j.job_title
FROM departments d
CROSS JOIN jobs j;
```

**换行写法：隐式交叉连接**
`FROM <表 1>, <表 2>`
```sql
-- 使用逗号分隔的隐式交叉连接
SELECT d.dept_name, j.job_title
FROM departments d, jobs j;
```

---

## 自连接

**换行写法：表与自身连接**
`FROM <表> AS <别名 1> JOIN <表> AS <别名 2> ON <条件>`
```sql
-- 查询员工及其经理
SELECT
  e.name AS employee,
  m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：自连接查找同组数据**
`FROM <表> AS <别名 1> JOIN <表> AS <别名 2> ON <条件>`
```sql
-- 查找同一部门中薪资相同的员工
SELECT a.name, b.name, a.salary
FROM employees a
JOIN employees b ON a.dept_id = b.dept_id AND a.salary = b.salary AND a.id < b.id;
```

---

## USING 子句

**换行写法：USING 指定同名列连接**
`FROM <左表> JOIN <右表> USING (<列>)`
```sql
-- 使用 USING 指定同名列连接
SELECT e.name, department_id
FROM employees e
JOIN departments d USING (department_id);
```

**换行写法：NATURAL JOIN 自动按同名列连接**
`FROM <左表> NATURAL JOIN <右表>`
```sql
-- 自动按同名列连接（不推荐，不可控）
SELECT * FROM employees NATURAL JOIN departments;
```



<!-- ============ 文档分隔线：019-sql/008-TCL.md ============ -->

# 事务控制语言

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## BEGIN

**单行写法：开启事务**
`BEGIN;`
```sql
-- 开启一个事务
BEGIN;
```

**单行写法：MySQL 开启事务**
`START TRANSACTION;`
```sql
-- MySQL 开启事务
START TRANSACTION;
```

**单行写法：开启只读事务**
`BEGIN READ ONLY;`
```sql
-- 开启只读事务（PostgreSQL）
BEGIN READ ONLY;
```

---

## COMMIT

**单行写法：提交事务**
`COMMIT;`
```sql
-- 提交当前事务
COMMIT;
```

**换行写法：完整事务流程**
`BEGIN; ... COMMIT;`
```sql
-- 转账事务流程
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

---

## ROLLBACK

**单行写法：回滚事务**
`ROLLBACK;`
```sql
-- 回滚当前事务
ROLLBACK;
```

**换行写法：事务回滚示例**
`BEGIN; ... ROLLBACK;`
```sql
-- 转账失败时回滚
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
ROLLBACK;
```

---

## SAVEPOINT

**单行写法：设置保存点**
`SAVEPOINT <保存点名>;`
```sql
-- 在事务中设置保存点
SAVEPOINT sp1;
```

**单行写法：回滚到保存点**
`ROLLBACK TO SAVEPOINT <保存点名>;`
```sql
-- 回滚到指定保存点（不回滚整个事务）
ROLLBACK TO SAVEPOINT sp1;
```

**单行写法：释放保存点**
`RELEASE SAVEPOINT <保存点名>;`
```sql
-- 释放保存点（保存点之后不能再回滚到该点）
RELEASE SAVEPOINT sp1;
```

**换行写法：保存点完整示例**
`BEGIN; ... SAVEPOINT ...; ... ROLLBACK TO ...; COMMIT;`
```sql
-- 使用保存点实现部分回滚
BEGIN;
INSERT INTO orders (id, amount) VALUES (1, 100);
SAVEPOINT sp1;
INSERT INTO orders (id, amount) VALUES (2, 200);
ROLLBACK TO SAVEPOINT sp1;
INSERT INTO orders (id, amount) VALUES (3, 300);
COMMIT;
```

---

## SET TRANSACTION

**单行写法：设置事务隔离级别**
`SET TRANSACTION ISOLATION LEVEL <隔离级别>;`
```sql
-- 设置事务隔离级别为可重复读
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

**换行写法：开启事务时指定隔离级别**
`BEGIN ISOLATION LEVEL <隔离级别>;`
```sql
-- PostgreSQL 开启事务并指定隔离级别
BEGIN ISOLATION LEVEL SERIALIZABLE;
```

**单行写法：设置只读事务**
`SET TRANSACTION READ ONLY;`
```sql
-- 设置当前事务为只读
SET TRANSACTION READ ONLY;
```

---

## 隔离级别

**单行写法：读未提交**
`SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;`
```sql
-- 设置隔离级别为读未提交（允许脏读）
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
```

**单行写法：读已提交**
`SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`
```sql
-- 设置隔离级别为读已提交（防止脏读）
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**单行写法：可重复读**
`SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;`
```sql
-- 设置隔离级别为可重复读（防止脏读和不可重复读）
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

**单行写法：可串行化**
`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`
```sql
-- 设置隔离级别为可串行化（最高隔离级别）
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

## MySQL 自动提交

**单行写法：查看自动提交状态**
`SELECT @@autocommit;`
```sql
-- 查看当前自动提交状态
SELECT @@autocommit;
```

**单行写法：关闭自动提交**
`SET autocommit = 0;`
```sql
-- 关闭自动提交，需手动 COMMIT
SET autocommit = 0;
```

**单行写法：开启自动提交**
`SET autocommit = 1;`
```sql
-- 开启自动提交（默认）
SET autocommit = 1;
```

---

## 锁

**单行写法：共享锁**
`SELECT ... LOCK IN SHARE MODE;`
```sql
-- 加共享锁读取数据
SELECT * FROM accounts WHERE id = 1 LOCK IN SHARE MODE;
```

**单行写法：排他锁**
`SELECT ... FOR UPDATE;`
```sql
-- 加排他锁读取数据
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
```

**单行写法：PostgreSQL 跳过已锁行**
`SELECT ... FOR UPDATE SKIP LOCKED;`
```sql
-- 跳过已被锁定的行（用于任务队列）
SELECT * FROM task_queue WHERE status = 'pending' FOR UPDATE SKIP LOCKED LIMIT 1;
```

**单行写法：PostgreSQL 锁定指定列**
`SELECT ... FOR UPDATE OF <表别名>`
```sql
-- 仅锁定指定表的行
SELECT * FROM orders o JOIN users u ON o.user_id = u.id WHERE u.id = 1 FOR UPDATE OF o;
```

---

## 死锁处理

**换行写法：死锁示例**
`BEGIN; ... BEGIN; ...`
```sql
-- 事务 A 锁定行 1，事务 B 锁定行 2，互相等待导致死锁
-- 事务 A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;

-- 事务 B
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 2;

-- 事务 A 请求锁定行 2（被 B 持有）
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- 事务 B 请求锁定行 1（被 A 持有）→ 死锁
UPDATE accounts SET balance = balance + 100 WHERE id = 1;
```

**单行写法：设置锁超时**
`SET lock_timeout = '<时间>';`
```sql
-- 设置锁等待超时为 5 秒
SET lock_timeout = '5s';
```

**单行写法：MySQL 查看锁信息**
`SELECT * FROM information_schema.INNODB_LOCKS;`
```sql
-- 查看 InnoDB 锁信息
SELECT * FROM information_schema.INNODB_LOCKS;
```



<!-- ============ 文档分隔线：019-sql/009-DML.md ============ -->

# 数据操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## INSERT

**单行写法：插入单行指定列**
`INSERT INTO <表名> (<列 1>, <列 2>) VALUES (<值 1>, <值 2>);`
```sql
-- 向用户表插入一条记录
INSERT INTO users (name, email) VALUES ('张三', 'zhangsan@example.com');
```

**单行写法：插入单行所有列**
`INSERT INTO <表名> VALUES (<值 1>, <值 2>, ...);`
```sql
-- 向用户表插入一条记录（按列顺序提供所有值）
INSERT INTO users VALUES (1, '张三', 'zhangsan@example.com');
```

**换行写法：插入多行**
`INSERT INTO <表名> (<列>) VALUES (<值 1>), (<值 2>), (<值 3>);`
```sql
-- 向用户表插入多条记录
INSERT INTO users (name, email) VALUES
  ('张三', 'zhangsan@example.com'),
  ('李四', 'lisi@example.com'),
  ('王五', 'wangwu@example.com');
```

**换行写法：INSERT ... SELECT 从查询结果插入**
`INSERT INTO <表名> (<列>) SELECT ...`
```sql
-- 从临时表批量插入数据
INSERT INTO users (name, email)
SELECT name, email FROM temp_users WHERE status = 'active';
```

---

## UPDATE

**单行写法：更新单列**
`UPDATE <表名> SET <列> = <值> WHERE <条件>;`
```sql
-- 更新用户 1 的邮箱
UPDATE users SET email = 'new@example.com' WHERE id = 1;
```

**换行写法：更新多列**
`UPDATE <表名> SET <列 1> = <值 1>, <列 2> = <值 2> WHERE <条件>;`
```sql
-- 更新用户 1 的邮箱和姓名
UPDATE users
SET email = 'new@example.com', name = '张三丰'
WHERE id = 1;
```

**换行写法：基于子查询更新**
`UPDATE <表名> SET <列> = (SELECT ...) WHERE <条件>;`
```sql
-- 将员工薪资更新为部门平均薪资的 1.1 倍
UPDATE employees e
SET salary = (
  SELECT AVG(salary) * 1.1 FROM employees e2 WHERE e2.dept_id = e.dept_id
)
WHERE e.performance = 'A';
```

**换行写法：基于 JOIN 更新**
`UPDATE <表 1> JOIN <表 2> ON ... SET ...`
```sql
-- 根据部门表更新员工表的部门名称
UPDATE employees e
JOIN departments d ON e.dept_id = d.id
SET e.dept_name = d.dept_name;
```

---

## DELETE

**单行写法：删除指定行**
`DELETE FROM <表名> WHERE <条件>;`
```sql
-- 删除 ID 为 1 的用户
DELETE FROM users WHERE id = 1;
```

**换行写法：基于子查询删除**
`DELETE FROM <表名> WHERE <列> IN (SELECT ...);`
```sql
-- 删除没有订单的客户
DELETE FROM customers
WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders);
```

**换行写法：基于 JOIN 删除**
`DELETE <表 1> FROM <表 1> JOIN <表 2> ON ...`
```sql
-- 删除没有订单的客户
DELETE c FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;
```

---

## MERGE / UPSERT

**换行写法：MySQL ON DUPLICATE KEY UPDATE**
`INSERT INTO ... ON DUPLICATE KEY UPDATE <列> = VALUES(<列>)`
```sql
-- 插入数据，主键冲突时更新
INSERT INTO users (id, name, email) VALUES (1, '张三', 'zhangsan@example.com')
ON DUPLICATE KEY UPDATE name = VALUES(name), email = VALUES(email);
```

**换行写法：PostgreSQL ON CONFLICT**
`INSERT INTO ... ON CONFLICT (<列>) DO UPDATE SET ...`
```sql
-- 插入数据，冲突时更新
INSERT INTO users (id, name, email) VALUES (1, '张三', 'zhangsan@example.com')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;
```

**换行写法：PostgreSQL ON CONFLICT DO NOTHING**
`INSERT INTO ... ON CONFLICT (<列>) DO NOTHING`
```sql
-- 插入数据，冲突时忽略
INSERT INTO users (id, name, email) VALUES (1, '张三', 'zhangsan@example.com')
ON CONFLICT (id) DO NOTHING;
```

**换行写法：SQL Server MERGE**
`MERGE INTO <目标表> USING <源表> ON <条件> WHEN MATCHED THEN UPDATE ... WHEN NOT MATCHED THEN INSERT ...`
```sql
-- SQL Server MERGE 实现 UPSERT
MERGE INTO users AS target
USING (VALUES (1, '张三', 'zhangsan@example.com')) AS source (id, name, email)
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET name = source.name, email = source.email
WHEN NOT MATCHED THEN INSERT (id, name, email) VALUES (source.id, source.name, source.email);
```

---

## RETURNING

**换行写法：PostgreSQL RETURNING 返回插入的行**
`INSERT INTO ... RETURNING <列>`
```sql
-- 插入数据并返回自增 ID
INSERT INTO users (name, email) VALUES ('张三', 'zhangsan@example.com')
RETURNING id;
```

**换行写法：RETURNING 返回更新的行**
`UPDATE ... SET ... RETURNING <列>`
```sql
-- 更新数据并返回更新后的行
UPDATE users SET status = 'inactive' WHERE last_login < '2025-01-01'
RETURNING id, name;
```

**换行写法：RETURNING 返回删除的行**
`DELETE FROM ... WHERE ... RETURNING <列>`
```sql
-- 删除数据并返回被删除的行
DELETE FROM users WHERE status = 'inactive'
RETURNING id, name;
```

---

## TRUNCATE

**单行写法：清空表数据**
`TRUNCATE TABLE <表名>;`
```sql
-- 清空用户表数据（保留表结构）
TRUNCATE TABLE users;
```

**换行写法：清空表并重置自增 ID**
`TRUNCATE TABLE <表名> RESTART IDENTITY;`
```sql
-- 清空用户表并重置自增 ID
TRUNCATE TABLE users RESTART IDENTITY;
```

**换行写法：级联清空关联表**
`TRUNCATE TABLE <表 1>, <表 2> CASCADE;`
```sql
-- 级联清空用户表和订单表
TRUNCATE TABLE users, orders CASCADE;
```



<!-- ============ 文档分隔线：019-sql/010-DataQueryBasics.md ============ -->

# 数据查询基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SELECT 查询

**单行写法：查询所有列**
`SELECT * FROM <表名>;`
```sql
-- 查询员工表中的所有字段
SELECT * FROM employees;
```

**单行写法：查询指定列**
`SELECT <列名 1>, <列名 2> FROM <表名>;`
```sql
-- 查询员工表中的姓名和薪资字段
SELECT first_name, salary FROM employees;
```

**换行写法：查询多列并计算**
`SELECT <列名 1>, <列名 2>, <表达式> AS <别名> FROM <表名>;`
```sql
-- 查询姓名、薪资并计算年薪
SELECT
  first_name,
  salary,
  salary * 12 AS annual_salary
FROM employees;
```

---

## WHERE 条件

**单行写法：AND 组合条件**
`WHERE <条件 1> AND <条件 2>;`
```sql
-- 查询 IT 部门且薪资大于 80000 的员工
SELECT * FROM employees WHERE department = 'IT' AND salary > 80000;
```

**单行写法：OR 组合条件**
`WHERE <条件 1> OR <条件 2>;`
```sql
-- 查询 IT 或 HR 部门的员工
SELECT * FROM employees WHERE department = 'IT' OR department = 'HR';
```

**单行写法：NOT 取反条件**
`WHERE NOT <条件>;`
```sql
-- 查询非 IT 部门的员工
SELECT * FROM employees WHERE NOT department = 'IT';
```

**换行写法：括号组合条件**
`WHERE (<条件 1> OR <条件 2>) AND <条件 3>;`
```sql
-- 查询 IT 或 HR 部门且薪资大于 50000 的员工
SELECT * FROM employees
WHERE (department = 'IT' OR department = 'HR') AND salary > 50000;
```

---

## BETWEEN 范围查询

**单行写法：范围查询（包含边界）**
`WHERE <列> BETWEEN <下界> AND <上界>;`
```sql
-- 查询价格在 100 到 500 之间的商品
SELECT * FROM products WHERE price BETWEEN 100 AND 500;
```

**单行写法：排除范围**
`WHERE <列> NOT BETWEEN <下界> AND <上界>;`
```sql
-- 查询价格不在 100 到 500 之间的商品
SELECT * FROM products WHERE price NOT BETWEEN 100 AND 500;
```

---

## IN 集合匹配

**单行写法：集合匹配**
`WHERE <列> IN (<值 1>, <值 2>, ...);`
```sql
-- 查询 IT、HR、Finance 部门的员工
SELECT * FROM employees WHERE department IN ('IT', 'HR', 'Finance');
```

**单行写法：排除集合**
`WHERE <列> NOT IN (<值 1>, <值 2>, ...);`
```sql
-- 查询非 IT、HR 部门的员工
SELECT * FROM employees WHERE department NOT IN ('IT', 'HR');
```

**换行写法：子查询形式的 IN**
`WHERE <列> IN (SELECT ...);`
```sql
-- 查询来自中国的客户的订单
SELECT * FROM orders
WHERE customer_id IN (
  SELECT id FROM customers WHERE country = 'China'
);
```

---

## LIKE 模式匹配

**单行写法：前缀匹配**
`WHERE <列> LIKE '<前缀>%';`
```sql
-- 查询姓"张"的用户
SELECT * FROM users WHERE name LIKE '张%';
```

**单行写法：后缀匹配**
`WHERE <列> LIKE '%<后缀>';`
```sql
-- 查询 Gmail 邮箱用户
SELECT * FROM users WHERE email LIKE '%@gmail.com';
```

**单行写法：包含匹配**
`WHERE <列> LIKE '%<关键字>%';`
```sql
-- 查询名字包含"华"的用户
SELECT * FROM users WHERE name LIKE '%华%';
```

**单行写法：单字符匹配**
`WHERE <列> LIKE '<前缀>_<后缀>';`
```sql
-- 查询 138 开头 1234 结尾的 11 位手机号
SELECT * FROM users WHERE phone LIKE '138____1234';
```

**单行写法：排除模式**
`WHERE <列> NOT LIKE '<模式>';`
```sql
-- 查询名字不以 admin 开头的用户
SELECT * FROM users WHERE name NOT LIKE 'admin%';
```

---

## NULL 处理

**单行写法：检查 NULL 值**
`WHERE <列> IS NULL;`
```sql
-- 查询没有手机号的用户
SELECT * FROM users WHERE phone IS NULL;
```

**单行写法：检查非 NULL 值**
`WHERE <列> IS NOT NULL;`
```sql
-- 查询有手机号的用户
SELECT * FROM users WHERE phone IS NOT NULL;
```

**单行写法：COALESCE 返回第一个非 NULL 值**
`SELECT COALESCE(<列>, <默认值>) AS <别名> FROM <表名>;`
```sql
-- 查询用户手机号，未填写则显示"未填写"
SELECT name, COALESCE(phone, '未填写') AS phone_display FROM users;
```

**单行写法：NULLIF 相等返回 NULL**
`SELECT NULLIF(<列>, <值>) AS <别名> FROM <表名>;`
```sql
-- 查询成绩，为 0 时返回 NULL 避免除零
SELECT NULLIF(score, 0) AS safe_score FROM results;
```

---

## ORDER BY 排序

**单行写法：升序排序**
`ORDER BY <列> ASC;`
```sql
-- 按薪资升序排列员工
SELECT * FROM employees ORDER BY salary ASC;
```

**单行写法：降序排序**
`ORDER BY <列> DESC;`
```sql
-- 按薪资降序排列员工
SELECT * FROM employees ORDER BY salary DESC;
```

**换行写法：多列排序**
`ORDER BY <列 1> ASC, <列 2> DESC;`
```sql
-- 按部门升序、薪资降序排列员工
SELECT * FROM employees ORDER BY department ASC, salary DESC;
```

**单行写法：按表达式排序**
`ORDER BY <表达式> DESC;`
```sql
-- 按折扣后价格降序排列商品
SELECT * FROM products ORDER BY price * discount DESC;
```

---

## LIMIT / OFFSET 分页

**单行写法：限制返回行数**
`LIMIT <数量>;`
```sql
-- 查询前 10 条员工记录
SELECT * FROM employees ORDER BY id LIMIT 10;
```

**单行写法：偏移分页**
`LIMIT <数量> OFFSET <偏移>;`
```sql
-- 查询第 21 到 30 条员工记录
SELECT * FROM employees ORDER BY id LIMIT 10 OFFSET 20;
```

**换行写法：SQL Server 分页**
`OFFSET <偏移> ROWS FETCH NEXT <数量> ROWS ONLY;`
```sql
-- SQL Server 2012+ 分页查询
SELECT * FROM employees
ORDER BY id
OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;
```

**单行写法：游标分页（深分页优化）**
`WHERE <列> > <值> ORDER BY <列> LIMIT <数量>;`
```sql
-- 利用索引进行游标分页，避免 OFFSET 性能问题
SELECT * FROM orders WHERE id > 1000000 ORDER BY id LIMIT 10;
```

---

## DISTINCT 去重

**单行写法：单列去重**
`SELECT DISTINCT <列> FROM <表名>;`
```sql
-- 查询所有不重复的部门
SELECT DISTINCT department FROM employees;
```

**单行写法：多列组合去重**
`SELECT DISTINCT <列 1>, <列 2> FROM <表名>;`
```sql
-- 查询所有不重复的部门和职位组合
SELECT DISTINCT department, job_title FROM employees;
```

**单行写法：COUNT DISTINCT 统计**
`SELECT COUNT(DISTINCT <列>) AS <别名> FROM <表名>;`
```sql
-- 统计不同部门的数量
SELECT COUNT(DISTINCT department) AS dept_count FROM employees;
```

---

## 别名

**单行写法：列别名**
`SELECT <列> AS <别名> FROM <表名>;`
```sql
-- 为列设置中文别名
SELECT first_name AS 名, salary AS 薪资 FROM employees;
```

**单行写法：省略 AS 的列别名**
`SELECT <列> <别名> FROM <表名>;`
```sql
-- 省略 AS 关键字设置列别名
SELECT first_name 名, salary 薪资 FROM employees;
```

**换行写法：表别名**
`FROM <表名> AS <别名>`
```sql
-- 为表设置别名后进行连接查询
SELECT e.first_name, d.department_name
FROM employees e
JOIN departments d ON e.dept_id = d.id;
```

**换行写法：别名在 ORDER BY 中使用**
`SELECT <表达式> AS <别名> ... ORDER BY <别名> DESC;`
```sql
-- 计算年薪并按年薪降序排列
SELECT salary * 12 AS annual_salary
FROM employees
ORDER BY annual_salary DESC;
```

---

## CASE WHEN 条件表达式

**换行写法：简单 CASE 等值匹配**
`CASE <列> WHEN <值> THEN <结果> [ELSE <结果>] END`
```sql
-- 将部门代码转换为中文名称
SELECT
  department,
  CASE department
    WHEN 'IT' THEN '技术部'
    WHEN 'HR' THEN '人力资源部'
    WHEN 'Finance' THEN '财务部'
    ELSE '其他部门'
  END AS dept_name_cn
FROM employees;
```

**换行写法：搜索 CASE 条件判断**
`CASE WHEN <条件> THEN <结果> [ELSE <结果>] END`
```sql
-- 根据薪资划分等级
SELECT
  name,
  salary,
  CASE
    WHEN salary >= 100000 THEN '高薪'
    WHEN salary >= 60000 THEN '中薪'
    WHEN salary >= 30000 THEN '低薪'
    ELSE '实习'
  END AS salary_level
FROM employees;
```

**换行写法：CASE WHEN 在聚合中使用**
`COUNT(CASE WHEN <条件> THEN 1 END) AS <别名>`
```sql
-- 统计男女员工数量及高薪总额
SELECT
  COUNT(*) AS total,
  COUNT(CASE WHEN gender = 'M' THEN 1 END) AS male_count,
  COUNT(CASE WHEN gender = 'F' THEN 1 END) AS female_count,
  SUM(CASE WHEN salary > 50000 THEN salary ELSE 0 END) AS high_salary_total
FROM employees;
```

---

## GROUP BY 分组

**换行写法：按单列分组聚合**
`SELECT <分组列>, <聚合函数> FROM <表名> GROUP BY <分组列>;`
```sql
-- 按部门分组统计员工数和平均薪资
SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

**换行写法：按多列分组聚合**
`SELECT <列 1>, <列 2>, <聚合函数> FROM <表名> GROUP BY <列 1>, <列 2>;`
```sql
-- 按部门和职位分组统计员工数和平均薪资
SELECT department, job_title, COUNT(*) AS cnt, AVG(salary) AS avg_salary
FROM employees
GROUP BY department, job_title;
```

**换行写法：GROUP BY 与 ORDER BY**
`SELECT <列>, <聚合函数> FROM <表名> GROUP BY <列> ORDER BY <聚合函数> DESC;`
```sql
-- 按部门分组并按平均薪资降序排列
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

---

## HAVING 分组过滤

**换行写法：分组后过滤**
`HAVING <分组条件>;`
```sql
-- 查询员工数大于 5 且平均薪资大于 50000 的部门
SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 5 AND AVG(salary) > 50000;
```

**换行写法：WHERE 与 HAVING 区别**
`WHERE <行条件> ... GROUP BY ... HAVING <组条件>;`
```sql
-- 先过滤 2024 年后入职的员工，再按部门分组过滤人数大于 3 的部门
SELECT department, COUNT(*) AS cnt
FROM employees
WHERE hire_date >= '2024-01-01'
GROUP BY department
HAVING COUNT(*) > 3;
```



<!-- ============ 文档分隔线：019-sql/011-DDL.md ============ -->

# 数据定义

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## CREATE DATABASE

**单行写法：创建数据库**
`CREATE DATABASE <数据库名>;`
```sql
-- 创建名为 mydb 的数据库
CREATE DATABASE mydb;
```

**单行写法：创建数据库时指定字符集**
`CREATE DATABASE <数据库名> CHARACTER SET <字符集> COLLATE <排序规则>;`
```sql
-- 创建数据库并指定字符集为 utf8mb4
CREATE DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**单行写法：创建数据库时判断是否已存在**
`CREATE DATABASE IF NOT EXISTS <数据库名>;`
```sql
-- 仅在数据库不存在时创建
CREATE DATABASE IF NOT EXISTS mydb;
```

---

## CREATE TABLE

**换行写法：创建表**
`CREATE TABLE <表名> (<列定义>);`
```sql
-- 创建用户表
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**换行写法：创建表时判断是否已存在**
`CREATE TABLE IF NOT EXISTS <表名> (<列定义>);`
```sql
-- 仅在表不存在时创建
CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY,
  name VARCHAR(100)
);
```

**换行写法：创建表时指定存储引擎和字符集**
`CREATE TABLE <表名> (<列定义>) ENGINE=<引擎> DEFAULT CHARSET=<字符集>;`
```sql
-- 创建表并指定存储引擎和字符集
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

---

## 列定义

**单行写法：定义自增主键列**
`<列名> INT AUTO_INCREMENT PRIMARY KEY`
```sql
-- 定义自增主键列
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);
```

**单行写法：定义带默认值的列**
`<列名> <数据类型> DEFAULT <默认值>`
```sql
-- 定义带默认值的列
CREATE TABLE users (
  id INT PRIMARY KEY,
  status VARCHAR(20) DEFAULT 'active'
);
```

**单行写法：定义非空列**
`<列名> <数据类型> NOT NULL`
```sql
-- 定义非空列
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);
```

**单行写法：定义唯一约束列**
`<列名> <数据类型> UNIQUE`
```sql
-- 定义唯一约束列
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255) UNIQUE
);
```

---

## ALTER TABLE

**单行写法：添加列**
`ALTER TABLE <表名> ADD COLUMN <列名> <数据类型>;`
```sql
-- 向用户表添加年龄列
ALTER TABLE users ADD COLUMN age INT;
```

**单行写法：删除列**
`ALTER TABLE <表名> DROP COLUMN <列名>;`
```sql
-- 从用户表删除年龄列
ALTER TABLE users DROP COLUMN age;
```

**单行写法：修改列类型**
`ALTER TABLE <表名> ALTER COLUMN <列名> TYPE <新类型>;`
```sql
-- 修改 name 列类型为 VARCHAR(200)
ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(200);
```

**单行写法：MySQL 修改列类型**
`ALTER TABLE <表名> MODIFY COLUMN <列名> <新类型>;`
```sql
-- MySQL 修改 name 列类型为 VARCHAR(200)
ALTER TABLE users MODIFY COLUMN name VARCHAR(200);
```

**单行写法：重命名列**
`ALTER TABLE <表名> RENAME COLUMN <旧名> TO <新名>;`
```sql
-- 将 name 列重命名为 username
ALTER TABLE users RENAME COLUMN name TO username;
```

**单行写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>;`
```sql
-- 将 users 表重命名为 accounts
ALTER TABLE users RENAME TO accounts;
```

**换行写法：添加多列**
`ALTER TABLE <表名> ADD COLUMN <列 1> <类型>, ADD COLUMN <列 2> <类型>;`
```sql
-- 向用户表添加多列
ALTER TABLE users
  ADD COLUMN age INT,
  ADD COLUMN phone VARCHAR(20);
```

---

## DROP TABLE

**单行写法：删除表**
`DROP TABLE <表名>;`
```sql
-- 删除用户表
DROP TABLE users;
```

**单行写法：删除表时判断是否存在**
`DROP TABLE IF EXISTS <表名>;`
```sql
-- 仅在表存在时删除
DROP TABLE IF EXISTS users;
```

**换行写法：删除多表**
`DROP TABLE <表 1>, <表 2>;`
```sql
-- 同时删除多个表
DROP TABLE users, orders;
```

---

## TRUNCATE TABLE

**单行写法：清空表数据**
`TRUNCATE TABLE <表名>;`
```sql
-- 清空用户表数据（保留表结构）
TRUNCATE TABLE users;
```

---

## CREATE INDEX

**单行写法：创建单列索引**
`CREATE INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在用户表的 email 列上创建索引
CREATE INDEX idx_email ON users(email);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列 1>, <列 2>);`
```sql
-- 在用户表的姓和名列上创建复合索引
CREATE INDEX idx_name ON users(last_name, first_name);
```

**单行写法：创建唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在用户表的 email 列上创建唯一索引
CREATE UNIQUE INDEX idx_unique_email ON users(email);
```

---

## DROP INDEX

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>;`
```sql
-- 删除用户表上的 idx_email 索引
DROP INDEX idx_email ON users;
```

**单行写法：PostgreSQL 删除索引**
`DROP INDEX <索引名>;`
```sql
-- PostgreSQL 删除索引
DROP INDEX idx_email;
```

**单行写法：删除索引时判断是否存在**
`DROP INDEX IF EXISTS <索引名>;`
```sql
-- 仅在索引存在时删除
DROP INDEX IF EXISTS idx_email;
```

---

## CREATE VIEW

**换行写法：创建视图**
`CREATE VIEW <视图名> AS <SELECT 语句>;`
```sql
-- 创建高薪员工视图
CREATE VIEW high_salary_employees AS
SELECT id, name, salary
FROM employees
WHERE salary > 80000;
```

**换行写法：创建或替换视图**
`CREATE OR REPLACE VIEW <视图名> AS <SELECT 语句>;`
```sql
-- 创建或替换高薪员工视图
CREATE OR REPLACE VIEW high_salary_employees AS
SELECT id, name, salary, department
FROM employees
WHERE salary > 80000;
```

---

## DROP VIEW

**单行写法：删除视图**
`DROP VIEW <视图名>;`
```sql
-- 删除高薪员工视图
DROP VIEW high_salary_employees;
```

**单行写法：删除视图时判断是否存在**
`DROP VIEW IF EXISTS <视图名>;`
```sql
-- 仅在视图存在时删除
DROP VIEW IF EXISTS high_salary_employees;
```



<!-- ============ 文档分隔线：019-sql/012-DataType.md ============ -->

# 数据类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 整数类型

**单行写法：定义 TINYINT 列**
`<列名> TINYINT`
```sql
-- 定义 TINYINT 类型列（1 字节，-128 到 127）
CREATE TABLE products (id INT, stock TINYINT);
```

**单行写法：定义 SMALLINT 列**
`<列名> SMALLINT`
```sql
-- 定义 SMALLINT 类型列（2 字节，-32768 到 32767）
CREATE TABLE products (id INT, quantity SMALLINT);
```

**单行写法：定义 INT 列**
`<列名> INT`
```sql
-- 定义 INT 类型列（4 字节，-2147483648 到 2147483647）
CREATE TABLE users (id INT, age INT);
```

**单行写法：定义 BIGINT 列**
`<列名> BIGINT`
```sql
-- 定义 BIGINT 类型列（8 字节，大范围整数）
CREATE TABLE orders (id BIGINT, user_id BIGINT);
```

**单行写法：定义无符号整数**
`<列名> INT UNSIGNED`
```sql
-- 定义无符号 INT 列（MySQL，0 到 4294967295）
CREATE TABLE products (id INT UNSIGNED, price INT UNSIGNED);
```

---

## 定点数与浮点数

**单行写法：定义 DECIMAL 列**
`<列名> DECIMAL(<精度>, <标度>)`
```sql
-- 定义 DECIMAL 类型列（精确小数，推荐用于金额）
CREATE TABLE products (id INT, price DECIMAL(10, 2));
```

**单行写法：定义 NUMERIC 列**
`<列名> NUMERIC(<精度>, <标度>)`
```sql
-- 定义 NUMERIC 类型列（等价于 DECIMAL）
CREATE TABLE accounts (id INT, balance NUMERIC(15, 2));
```

**单行写法：定义 FLOAT 列**
`<列名> FLOAT`
```sql
-- 定义 FLOAT 类型列（单精度浮点数，4 字节）
CREATE TABLE sensors (id INT, temperature FLOAT);
```

**单行写法：定义 DOUBLE 列**
`<列名> DOUBLE`
```sql
-- 定义 DOUBLE 类型列（双精度浮点数，8 字节）
CREATE TABLE measurements (id INT, value DOUBLE);
```

**单行写法：定义 REAL 列**
`<列名> REAL`
```sql
-- 定义 REAL 类型列（单精度浮点数）
CREATE TABLE sensors (id INT, temperature REAL);
```

---

## 字符串类型

**单行写法：定义 CHAR 列**
`<列名> CHAR(<长度>)`
```sql
-- 定义 CHAR 类型列（固定长度字符串）
CREATE TABLE users (id INT, gender CHAR(1));
```

**单行写法：定义 VARCHAR 列**
`<列名> VARCHAR(<最大长度>)`
```sql
-- 定义 VARCHAR 类型列（可变长度字符串）
CREATE TABLE users (id INT, name VARCHAR(100));
```

**单行写法：定义 TEXT 列**
`<列名> TEXT`
```sql
-- 定义 TEXT 类型列（大文本数据）
CREATE TABLE articles (id INT, content TEXT);
```

**单行写法：定义 PostgreSQL TEXT 列**
`<列名> TEXT`
```sql
-- PostgreSQL 中 TEXT 无长度限制
CREATE TABLE articles (id INT, content TEXT);
```

---

## 日期时间类型

**单行写法：定义 DATE 列**
`<列名> DATE`
```sql
-- 定义 DATE 类型列（仅日期，YYYY-MM-DD）
CREATE TABLE users (id INT, birth_date DATE);
```

**单行写法：定义 TIME 列**
`<列名> TIME`
```sql
-- 定义 TIME 类型列（仅时间，HH:MM:SS）
CREATE TABLE events (id INT, start_time TIME);
```

**单行写法：定义 DATETIME 列**
`<列名> DATETIME`
```sql
-- 定义 DATETIME 类型列（日期时间，MySQL）
CREATE TABLE orders (id INT, created_at DATETIME);
```

**单行写法：定义 TIMESTAMP 列**
`<列名> TIMESTAMP`
```sql
-- 定义 TIMESTAMP 类型列（时间戳）
CREATE TABLE logs (id INT, log_time TIMESTAMP);
```

**单行写法：定义带时区的 TIMESTAMP 列**
`<列名> TIMESTAMP WITH TIME ZONE`
```sql
-- 定义带时区的 TIMESTAMP 列（PostgreSQL）
CREATE TABLE events (id INT, event_time TIMESTAMP WITH TIME ZONE);
```

---

## 布尔类型

**单行写法：定义 BOOLEAN 列**
`<列名> BOOLEAN`
```sql
-- 定义 BOOLEAN 类型列（PostgreSQL）
CREATE TABLE users (id INT, is_active BOOLEAN);
```

**单行写法：MySQL 用 TINYINT 模拟 BOOLEAN**
`<列名> TINYINT(1)`
```sql
-- MySQL 用 TINYINT(1) 模拟布尔类型
CREATE TABLE users (id INT, is_active TINYINT(1));
```

---

## 二进制类型

**单行写法：定义 BLOB 列**
`<列名> BLOB`
```sql
-- 定义 BLOB 类型列（二进制大对象）
CREATE TABLE files (id INT, file_data BLOB);
```

**单行写法：定义 BYTEA 列**
`<列名> BYTEA`
```sql
-- 定义 BYTEA 类型列（PostgreSQL 二进制数据）
CREATE TABLE files (id INT, file_data BYTEA);
```

**单行写法：定义 VARBINARY 列**
`<列名> VARBINARY(<最大长度>)`
```sql
-- 定义 VARBINARY 类型列（可变长度二进制）
CREATE TABLE images (id INT, thumbnail VARBINARY(1024));
```

---

## JSON 类型

**单行写法：定义 JSON 列**
`<列名> JSON`
```sql
-- 定义 JSON 类型列（MySQL 5.7+/PostgreSQL）
CREATE TABLE users (id INT, preferences JSON);
```

**单行写法：定义 JSONB 列**
`<列名> JSONB`
```sql
-- 定义 JSONB 类型列（PostgreSQL，二进制 JSON，支持索引）
CREATE TABLE users (id INT, preferences JSONB);
```

---

## 枚举类型

**换行写法：PostgreSQL 创建枚举类型**
`CREATE TYPE <类型名> AS ENUM (<值 1>, <值 2>, ...)`
```sql
-- 创建订单状态枚举类型
CREATE TYPE order_status AS ENUM ('pending', 'processing', 'shipped', 'delivered');
```

**单行写法：使用枚举类型**
`<列名> <枚举类型名>`
```sql
-- 使用枚举类型定义列
CREATE TABLE orders (id INT, status order_status);
```

**单行写法：MySQL ENUM 类型**
`<列名> ENUM(<值 1>, <值 2>, ...)`
```sql
-- MySQL 直接在列定义中使用 ENUM
CREATE TABLE orders (id INT, status ENUM('pending', 'processing', 'shipped', 'delivered'));
```

---

## 数组类型

**单行写法：PostgreSQL 数组类型**
`<列名> <类型>[]`
```sql
-- 定义整数数组列
CREATE TABLE teams (id INT, member_ids INT[]);
```

**单行写法：定义字符串数组列**
`<列名> VARCHAR[]`
```sql
-- 定义字符串数组列
CREATE TABLE articles (id INT, tags VARCHAR[]);
```

---

## UUID 类型

**单行写法：定义 UUID 列**
`<列名> UUID`
```sql
-- 定义 UUID 类型列（PostgreSQL）
CREATE TABLE users (id UUID PRIMARY KEY, name VARCHAR(100));
```

**单行写法：定义默认 UUID 列**
`<列名> UUID DEFAULT gen_random_uuid()`
```sql
-- 定义默认生成 UUID 的列
CREATE TABLE users (id UUID DEFAULT gen_random_uuid() PRIMARY KEY, name VARCHAR(100));
```

---

## 自增类型

**单行写法：MySQL AUTO_INCREMENT**
`<列名> INT AUTO_INCREMENT PRIMARY KEY`
```sql
-- MySQL 自增主键
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));
```

**单行写法：PostgreSQL SERIAL**
`<列名> SERIAL PRIMARY KEY`
```sql
-- PostgreSQL 自增主键
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));
```

**单行写法：PostgreSQL BIGSERIAL**
`<列名> BIGSERIAL PRIMARY KEY`
```sql
-- PostgreSQL 大范围自增主键
CREATE TABLE orders (id BIGSERIAL PRIMARY KEY, user_id BIGINT);
```

**单行写法：SQL Server IDENTITY**
`<列名> INT IDENTITY(1, 1) PRIMARY KEY`
```sql
-- SQL Server 自增主键
CREATE TABLE users (id INT IDENTITY(1, 1) PRIMARY KEY, name VARCHAR(100));
```

---

## 货币类型

**单行写法：定义 MONEY 列**
`<列名> MONEY`
```sql
-- 定义 MONEY 类型列（PostgreSQL）
CREATE TABLE products (id INT, price MONEY);
```

**单行写法：推荐用 DECIMAL 存储金额**
`<列名> DECIMAL(<精度>, 2)`
```sql
-- 推荐使用 DECIMAL 存储金额
CREATE TABLE products (id INT, price DECIMAL(10, 2));
```



<!-- ============ 文档分隔线：019-sql/013-Index.md ============ -->

# 索引

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## CREATE INDEX

**单行写法：创建单列索引**
`CREATE INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在用户表的 email 列上创建索引
CREATE INDEX idx_email ON users(email);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列 1>, <列 2>);`
```sql
-- 在用户表的姓和名列上创建复合索引
CREATE INDEX idx_name ON users(last_name, first_name);
```

**单行写法：创建唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在用户表的 email 列上创建唯一索引
CREATE UNIQUE INDEX idx_unique_email ON users(email);
```

**单行写法：创建表时定义索引**
`INDEX <索引名> (<列>)`
```sql
-- 创建表时同时创建索引
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255),
  INDEX idx_email (email)
);
```

---

## DROP INDEX

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>;`
```sql
-- 删除用户表上的索引
DROP INDEX idx_email ON users;
```

**单行写法：PostgreSQL 删除索引**
`DROP INDEX <索引名>;`
```sql
-- PostgreSQL 删除索引
DROP INDEX idx_email;
```

**单行写法：删除索引时判断是否存在**
`DROP INDEX IF EXISTS <索引名>;`
```sql
-- 仅在索引存在时删除
DROP INDEX IF EXISTS idx_email;
```

---

## 复合索引

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列 1>, <列 2>, <列 3>);`
```sql
-- 创建三列复合索引
CREATE INDEX idx_dept_status_salary ON employees(dept_id, status, salary);
```

**单行写法：最左前缀匹配查询**
`WHERE <列 1> = <值> AND <列 2> = <值>`
```sql
-- 使用复合索引的前两列（可利用索引）
SELECT * FROM employees WHERE dept_id = 5 AND status = 'active';
```

**单行写法：跳过中间列无法利用索引**
`WHERE <列 1> = <值> AND <列 3> = <值>`
```sql
-- 跳过 status 列，仅 dept_id 可利用索引
SELECT * FROM employees WHERE dept_id = 5 AND salary > 50000;
```

---

## 覆盖索引

**换行写法：索引包含查询所需所有列**
`CREATE INDEX <索引名> ON <表名>(<列 1>, <列 2>, <列 3>)`
```sql
-- 创建覆盖索引，避免回表查询
CREATE INDEX idx_covering ON orders(user_id, status, amount);
```

**换行写法：覆盖索引查询**
`SELECT <索引列> FROM <表名> WHERE <索引列条件>`
```sql
-- 查询列都在索引中，无需回表
SELECT user_id, status, amount FROM orders WHERE user_id = 100;
```

---

## 函数索引

**单行写法：PostgreSQL 函数索引**
`CREATE INDEX <索引名> ON <表名>(<函数>(<列>));`
```sql
-- 在 email 列的小写形式上创建索引
CREATE INDEX idx_lower_email ON users(LOWER(email));
```

**单行写法：MySQL 函数索引**
`CREATE INDEX <索引名> ON <表名>((<表达式>));`
```sql
-- MySQL 8.0+ 函数索引
CREATE INDEX idx_lower_email ON users((LOWER(email)));
```

---

## 前缀索引

**单行写法：MySQL 前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列>(<前缀长度>));`
```sql
-- 在 email 列前 10 个字符上创建索引
CREATE INDEX idx_email_prefix ON users(email(10));
```

---

## 全文索引

**单行写法：MySQL 全文索引**
`CREATE FULLTEXT INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在文章内容列上创建全文索引
CREATE FULLTEXT INDEX idx_content ON articles(content);
```

**换行写法：创建表时定义全文索引**
`FULLTEXT INDEX <索引名> (<列>)`
```sql
-- 创建表时同时创建全文索引
CREATE TABLE articles (
  id INT PRIMARY KEY,
  title VARCHAR(200),
  content TEXT,
  FULLTEXT INDEX idx_content (content)
);
```

**单行写法：PostgreSQL GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN(to_tsvector(<配置>, <列>));`
```sql
-- 在文章内容列上创建 GIN 全文索引
CREATE INDEX idx_content ON articles USING GIN(to_tsvector('english', content));
```

---

## 空间索引

**单行写法：MySQL 空间索引**
`CREATE SPATIAL INDEX <索引名> ON <表名>(<列>);`
```sql
-- 在地理位置列上创建空间索引
CREATE SPATIAL INDEX idx_location ON stores(location);
```

---

## 索引查看

**单行写法：MySQL 查看索引**
`SHOW INDEX FROM <表名>;`
```sql
-- 查看用户表上的所有索引
SHOW INDEX FROM users;
```

**换行写法：PostgreSQL 查看索引**
`SELECT * FROM pg_indexes WHERE tablename = '<表名>';`
```sql
-- 查看用户表上的所有索引
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'users';
```

**单行写法：SQL Server 查看索引**
`EXEC sp_helpindex '<表名>';`
```sql
-- 查看用户表上的所有索引
EXEC sp_helpindex 'users';
```

---

## 索引重建

**单行写法：MySQL 重建索引**
`ALTER TABLE <表名> REBUILD INDEX <索引名>;`
```sql
-- 重建用户表上的索引
ALTER TABLE users REBUILD INDEX idx_email;
```

**单行写法：PostgreSQL 重建索引**
`REINDEX INDEX <索引名>;`
```sql
-- 重建指定索引
REINDEX INDEX idx_email;
```

**单行写法：PostgreSQL 并发重建索引**
`REINDEX INDEX CONCURRENTLY <索引名>;`
```sql
-- 并发重建索引（不阻塞写入）
REINDEX INDEX CONCURRENTLY idx_email;
```

---

## 索引分析

**单行写法：MySQL 分析执行计划**
`EXPLAIN <SQL 语句>;`
```sql
-- 分析查询是否使用索引
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

**换行写法：PostgreSQL 分析执行计划**
`EXPLAIN ANALYZE <SQL 语句>;`
```sql
-- 分析查询执行计划并实际执行
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';
```



<!-- ============ 文档分隔线：019-sql/014-Constraint.md ============ -->

# 约束

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## PRIMARY KEY 主键

**单行写法：列级主键约束**
`<列名> <类型> PRIMARY KEY`
```sql
-- 在列定义时直接指定主键
CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100));
```

**换行写法：表级单列主键约束**
`CONSTRAINT <约束名> PRIMARY KEY (<列>)`
```sql
-- 在表级定义主键并命名
CREATE TABLE users (
  id INT,
  name VARCHAR(100),
  CONSTRAINT pk_users PRIMARY KEY (id)
);
```

**换行写法：表级复合主键约束**
`CONSTRAINT <约束名> PRIMARY KEY (<列 1>, <列 2>)`
```sql
-- 定义复合主键
CREATE TABLE order_items (
  order_id INT,
  product_id INT,
  quantity INT,
  CONSTRAINT pk_order_items PRIMARY KEY (order_id, product_id)
);
```

---

## FOREIGN KEY 外键

**换行写法：列级外键约束**
`<列名> <类型> REFERENCES <引用表>(<引用列>)`
```sql
-- 在列定义时直接指定外键
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT REFERENCES users(id),
  amount DECIMAL(10, 2)
);
```

**换行写法：表级外键约束**
`CONSTRAINT <约束名> FOREIGN KEY (<列>) REFERENCES <引用表>(<引用列>)`
```sql
-- 在表级定义外键并命名
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  amount DECIMAL(10, 2),
  CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**换行写法：外键级联删除**
`FOREIGN KEY (<列>) REFERENCES <引用表>(<引用列>) ON DELETE CASCADE`
```sql
-- 父记录删除时级联删除子记录
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

**换行写法：外键级联更新**
`FOREIGN KEY (<列>) REFERENCES <引用表>(<引用列>) ON UPDATE CASCADE`
```sql
-- 父记录主键更新时级联更新子记录外键
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE
);
```

**换行写法：外键 SET NULL**
`FOREIGN KEY (<列>) REFERENCES <引用表>(<引用列>) ON DELETE SET NULL`
```sql
-- 父记录删除时子记录外键设为 NULL
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  CONSTRAINT fk_orders_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);
```

---

## UNIQUE 唯一约束

**单行写法：列级唯一约束**
`<列名> <类型> UNIQUE`
```sql
-- 在列定义时直接指定唯一约束
CREATE TABLE users (id INT PRIMARY KEY, email VARCHAR(255) UNIQUE);
```

**换行写法：表级唯一约束**
`CONSTRAINT <约束名> UNIQUE (<列>)`
```sql
-- 在表级定义唯一约束并命名
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255),
  CONSTRAINT uk_users_email UNIQUE (email)
);
```

**换行写法：复合唯一约束**
`CONSTRAINT <约束名> UNIQUE (<列 1>, <列 2>)`
```sql
-- 定义复合唯一约束
CREATE TABLE user_roles (
  user_id INT,
  role_id INT,
  CONSTRAINT uk_user_role UNIQUE (user_id, role_id)
);
```

---

## NOT NULL 非空约束

**单行写法：列级非空约束**
`<列名> <类型> NOT NULL`
```sql
-- 在列定义时指定非空约束
CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(100) NOT NULL);
```

---

## DEFAULT 默认值

**单行写法：列级默认值**
`<列名> <类型> DEFAULT <默认值>`
```sql
-- 在列定义时指定默认值
CREATE TABLE users (id INT PRIMARY KEY, status VARCHAR(20) DEFAULT 'active');
```

**单行写法：使用函数作为默认值**
`<列名> <类型> DEFAULT <函数>()`
```sql
-- 使用 CURRENT_TIMESTAMP 作为默认值
CREATE TABLE users (id INT PRIMARY KEY, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```

---

## CHECK 检查约束

**单行写法：列级 CHECK 约束**
`<列名> <类型> CHECK (<条件>)`
```sql
-- 在列定义时指定检查约束
CREATE TABLE products (id INT PRIMARY KEY, price DECIMAL(10, 2) CHECK (price >= 0));
```

**换行写法：表级 CHECK 约束**
`CONSTRAINT <约束名> CHECK (<条件>)`
```sql
-- 在表级定义检查约束并命名
CREATE TABLE employees (
  id INT PRIMARY KEY,
  salary DECIMAL(10, 2),
  CONSTRAINT chk_salary CHECK (salary > 0 AND salary < 1000000)
);
```

**换行写法：多列 CHECK 约束**
`CONSTRAINT <约束名> CHECK (<列 1> <运算符> <列 2>)`
```sql
-- 检查结束日期大于开始日期
CREATE TABLE events (
  id INT PRIMARY KEY,
  start_date DATE,
  end_date DATE,
  CONSTRAINT chk_dates CHECK (end_date > start_date)
);
```

---

## AUTO_INCREMENT 自增

**单行写法：MySQL 自增主键**
`<列名> INT AUTO_INCREMENT PRIMARY KEY`
```sql
-- MySQL 自增主键
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100));
```

---

## 约束管理

**单行写法：添加约束**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> <约束定义>;`
```sql
-- 向现有表添加唯一约束
ALTER TABLE users ADD CONSTRAINT uk_email UNIQUE (email);
```

**单行写法：删除约束**
`ALTER TABLE <表名> DROP CONSTRAINT <约束名>;`
```sql
-- 删除表上的约束
ALTER TABLE users DROP CONSTRAINT uk_email;
```

**单行写法：MySQL 删除外键**
`ALTER TABLE <表名> DROP FOREIGN KEY <外键名>;`
```sql
-- MySQL 删除外键约束
ALTER TABLE orders DROP FOREIGN KEY fk_orders_user;
```

**单行写法：禁用约束**
`ALTER TABLE <表名> DISABLE CONSTRAINT <约束名>;`
```sql
-- 临时禁用约束（Oracle/PostgreSQL）
ALTER TABLE users DISABLE CONSTRAINT uk_email;
```

**单行写法：启用约束**
`ALTER TABLE <表名> ENABLE CONSTRAINT <约束名>;`
```sql
-- 重新启用约束
ALTER TABLE users ENABLE CONSTRAINT uk_email;
```



<!-- ============ 文档分隔线：019-sql/015-Subquery.md ============ -->

# 子查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 标量子查询

**换行写法：WHERE 中的标量子查询**
`WHERE <列> <运算符> (SELECT ...)`
```sql
-- 查询薪资高于平均值的员工
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**换行写法：SELECT 中的标量子查询**
`SELECT <列>, (SELECT ...) AS <别名> FROM <表名>`
```sql
-- 查询员工薪资及公司平均薪资
SELECT
  name,
  salary,
  (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;
```

---

## 列子查询

**换行写法：ANY 与子查询任一值比较**
`WHERE <列> <运算符> ANY (SELECT ...)`
```sql
-- 查询薪资高于部门 5 中任一员工的员工
SELECT name, salary FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept_id = 5);
```

**换行写法：= ANY 等价于 IN**
`WHERE <列> = ANY (SELECT ...)`
```sql
-- 查询东部地区部门的员工
SELECT name, salary FROM employees
WHERE dept_id = ANY (SELECT id FROM departments WHERE region = 'East');
```

**换行写法：ALL 与子查询所有值比较**
`WHERE <列> <运算符> ALL (SELECT ...)`
```sql
-- 查询薪资高于部门 5 中所有员工的员工
SELECT name, salary FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE dept_id = 5);
```

**换行写法：<> ALL 等价于 NOT IN**
`WHERE <列> <> ALL (SELECT ...)`
```sql
-- 查询不在东部地区部门的员工
SELECT name, salary FROM employees
WHERE dept_id <> ALL (SELECT id FROM departments WHERE region = 'East');
```

---

## 行子查询

**换行写法：行子查询返回单行多列**
`WHERE (<列 1>, <列 2>) = (SELECT ...)`
```sql
-- 查询部门 5 中薪资最高的员工
SELECT * FROM employees
WHERE (dept_id, salary) = (
  SELECT dept_id, MAX(salary)
  FROM employees
  GROUP BY dept_id
  HAVING dept_id = 5
);
```

**换行写法：多列 IN 子查询**
`WHERE (<列 1>, <列 2>) IN (SELECT ...)`
```sql
-- 查询每个客户最新订单
SELECT * FROM orders
WHERE (customer_id, order_date) IN (
  SELECT customer_id, MAX(order_date)
  FROM orders
  GROUP BY customer_id
);
```

---

## 表子查询

**换行写法：FROM 中的派生表**
`FROM (SELECT ...) AS <别名>`
```sql
-- 查询平均薪资大于 50000 的部门
SELECT dept_name, avg_salary
FROM (
  SELECT department AS dept_name, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) AS dept_stats
WHERE avg_salary > 50000;
```

---

## 相关子查询

**换行写法：相关子查询引用外层查询列**
`WHERE <列> = (SELECT ... FROM ... WHERE ... = <外层列>)`
```sql
-- 查询每个部门薪资最高的员工
SELECT name, department, salary
FROM employees e
WHERE salary = (
  SELECT MAX(salary)
  FROM employees e2
  WHERE e2.department = e.department
);
```

---

## EXISTS 与 NOT EXISTS

**换行写法：EXISTS 检查子查询是否返回行**
`WHERE EXISTS (SELECT 1 FROM ... WHERE ...)`
```sql
-- 查询有薪资超过 100000 员工的部门
SELECT d.department_name
FROM departments d
WHERE EXISTS (
  SELECT 1 FROM employees e
  WHERE e.dept_id = d.id AND e.salary > 100000
);
```

**换行写法：NOT EXISTS 避免 NULL 陷阱**
`WHERE NOT EXISTS (SELECT 1 FROM ... WHERE ...)`
```sql
-- 查询部门中没有薪资超过 100000 员工的部门
SELECT name FROM employees e
WHERE NOT EXISTS (
  SELECT 1 FROM employees e2
  WHERE e2.dept_id = e.dept_id AND e2.salary > 100000
);
```

---

## IN 与 NOT IN

**换行写法：IN 检查值在子查询结果中**
`WHERE <列> IN (SELECT ...)`
```sql
-- 查询有高薪员工的部门
SELECT d.department_name
FROM departments d
WHERE d.id IN (
  SELECT dept_id FROM employees WHERE salary > 100000
);
```

**换行写法：NOT IN 的 NULL 陷阱**
`WHERE <列> NOT IN (SELECT ...)`
```sql
-- NOT IN 如果子查询包含 NULL，整个查询返回空
SELECT name FROM employees
WHERE dept_id NOT IN (SELECT id FROM departments WHERE region = 'East');
```

**换行写法：NOT EXISTS 替代 NOT IN**
`WHERE NOT EXISTS (SELECT 1 FROM ... WHERE ...)`
```sql
-- 推荐使用 NOT EXISTS 替代 NOT IN
SELECT name FROM employees e
WHERE NOT EXISTS (
  SELECT 1 FROM departments d
  WHERE d.id = e.dept_id AND d.region = 'East'
);
```

---

## 子查询位置

**换行写法：SELECT 中的标量子查询**
`SELECT <列>, (SELECT ...) AS <别名>`
```sql
-- 查询员工薪资与平均薪资的差值
SELECT
  name,
  salary,
  (SELECT AVG(salary) FROM employees) AS avg_salary,
  salary - (SELECT AVG(salary) FROM employees) AS diff
FROM employees;
```

**换行写法：WHERE 中的子查询**
`WHERE <列> <运算符> (SELECT ...)`
```sql
-- 查询薪资高于平均值的员工
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**换行写法：HAVING 中的子查询**
`HAVING <聚合> <运算符> (SELECT ...)`
```sql
-- 查询平均薪资高于公司平均薪资的部门
SELECT department, AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

---

## 子查询与 JOIN 对比

**换行写法：子查询写法**
`WHERE <列> IN (SELECT ...)`
```sql
-- 使用子查询查询东部地区部门的员工
SELECT name
FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE region = 'East');
```

**换行写法：JOIN 写法（通常更高效）**
`FROM <表 1> JOIN <表 2> ON ...`
```sql
-- 使用 JOIN 改写子查询
SELECT e.name
FROM employees e
JOIN departments d ON e.dept_id = d.id
WHERE d.region = 'East';
```



<!-- ============ 文档分隔线：019-sql/016-SQLAdvancedQueryWindowFunction.md ============ -->

# SQL 高级查询与窗口函数速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 窗口函数

**基本写法：ROW_NUMBER 行号**
`ROW_NUMBER() OVER ([PARTITION BY <列>] ORDER BY <列>)`
```sql
-- 按部门分组并按薪资降序编号
SELECT name, dept, salary,
       ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn
FROM employees;
```

---

**基本写法：RANK 排名**
`RANK() OVER ([PARTITION BY <列>] ORDER BY <列>)`
```sql
-- 排名（并列时跳号）
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;
```

---

**基本写法：DENSE_RANK 密集排名**
`DENSE_RANK() OVER ([PARTITION BY <列>] ORDER BY <列>)`
```sql
-- 排名（并列时不跳号）
SELECT name, salary,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```

---

**基本写法：LAG 取前 N 行**
`LAG(<列>, [<偏移>], [<默认值>]) OVER (ORDER BY <列>)`
```sql
-- 取上一行的薪资
SELECT name, salary,
       LAG(salary, 1, 0) OVER (ORDER BY salary) AS prev_salary
FROM employees;
```

---

**基本写法：LEAD 取后 N 行**
`LEAD(<列>, [<偏移>], [<默认值>]) OVER (ORDER BY <列>)`
```sql
-- 取下一行的薪资
SELECT name, salary,
       LEAD(salary, 1, 0) OVER (ORDER BY salary) AS next_salary
FROM employees;
```

---

**基本写法：FIRST_VALUE 首值**
`FIRST_VALUE(<列>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 取分组内第一行的值
SELECT name, dept, salary,
       FIRST_VALUE(salary) OVER (PARTITION BY dept ORDER BY salary DESC) AS max_in_dept
FROM employees;
```

---

**基本写法：NTILE 分桶**
`NTILE(<桶数>) OVER (ORDER BY <列>)`
```sql
-- 将数据分为 4 桶
SELECT name, salary,
       NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

---

**基本写法：窗口范围**
`<函数>() OVER (ORDER BY <列> ROWS BETWEEN <起点> AND <终点>)`
```sql
-- 计算移动平均（当前行与前 2 行）
SELECT date, sales,
       AVG(sales) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM daily_sales;
```

---

## CTE 通用表表达式

**基本写法：WITH 子句**
`WITH <名称> AS (SELECT ...) SELECT ...`
```sql
-- 定义 CTE
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 100000
)
SELECT dept, COUNT(*) FROM high_earners GROUP BY dept;
```

---

**基本写法：多个 CTE**
`WITH <cte1> AS (...), <cte2> AS (...) SELECT ...`
```sql
-- 多个 CTE 串联
WITH dept_avg AS (
    SELECT dept, AVG(salary) AS avg_sal FROM employees GROUP BY dept
),
above_avg AS (
    SELECT e.* FROM employees e
    JOIN dept_avg d ON e.dept = d.dept AND e.salary > d.avg_sal
)
SELECT * FROM above_avg;
```

---

**基本写法：递归 CTE**
`WITH RECURSIVE <名称> AS (...) SELECT ...`
```sql
-- 递归查询层级
WITH RECURSIVE org_tree AS (
    SELECT id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, t.level + 1
    FROM employees e
    JOIN org_tree t ON e.manager_id = t.id
)
SELECT * FROM org_tree;
```

---

## 集合操作

**基本写法：UNION 合并去重**
`<查询1> UNION <查询2>`
```sql
-- 合并两个查询结果（去重）
SELECT name FROM employees
UNION
SELECT name FROM contractors;
```

---

**基本写法：UNION ALL 合并不去重**
`<查询1> UNION ALL <查询2>`
```sql
-- 合并两个查询结果（保留重复）
SELECT 'emp' AS type, name FROM employees
UNION ALL
SELECT 'contractor' AS type, name FROM contractors;
```

---

**基本写法：INTERSECT 交集**
`<查询1> INTERSECT <查询2>`
```sql
-- 取交集
SELECT product_id FROM sales_2023
INTERSECT
SELECT product_id FROM sales_2024;
```

---

**基本写法：EXCEPT 差集**
`<查询1> EXCEPT <查询2>`
```sql
-- 取差集（仅 2023 有而 2024 没有）
SELECT product_id FROM sales_2023
EXCEPT
SELECT product_id FROM sales_2024;
```

---

## CASE 表达式

**基本写法：简单 CASE**
`CASE <列> WHEN <值> THEN <结果> [ELSE <默认>] END`
```sql
-- 简单 CASE
SELECT name,
    CASE dept
        WHEN 'IT' THEN 'Technology'
        WHEN 'HR' THEN 'Human Resources'
        ELSE 'Other'
    END AS dept_name
FROM employees;
```

---

**基本写法：搜索 CASE**
`CASE WHEN <条件> THEN <结果> [ELSE <默认>] END`
```sql
-- 条件 CASE
SELECT name, salary,
    CASE
        WHEN salary > 100000 THEN 'High'
        WHEN salary > 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employees;
```

---

## 子查询

**基本写法：标量子查询**
`SELECT <列>, (SELECT ...) FROM <表>`
```sql
-- 子查询作为列
SELECT name, salary,
       (SELECT AVG(salary) FROM employees) AS company_avg
FROM employees;
```

---

**基本写法：EXISTS 存在判断**
`WHERE EXISTS (SELECT ...)`
```sql
-- 判断是否存在相关记录
SELECT name FROM employees e
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.emp_id = e.id
);
```

---

**基本写法：IN 子查询**
`WHERE <列> IN (SELECT ...)`
```sql
-- 使用 IN 子查询
SELECT name FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE active = 1);
```

---

## 字符串函数

**基本写法：CONCAT 拼接**
`CONCAT(<字符串1>, <字符串2>, ...)`
```sql
-- 拼接字符串
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;
```

---

**基本写法：SUBSTRING 截取**
`SUBSTRING(<字符串>, <起始>, [<长度>])`
```sql
-- 截取子串
SELECT SUBSTRING('Hello World', 1, 5);
```

---

**基本写法：REPLACE 替换**
`REPLACE(<字符串>, <旧>, <新>)`
```sql
-- 替换字符串
SELECT REPLACE('Hello', 'l', 'L');
```

---

**基本写法：LOWER/UPPER 大小写**
`LOWER(<字符串>)` 或 `UPPER(<字符串>)`
```sql
-- 转换大小写
SELECT LOWER('HELLO');
SELECT UPPER('hello');
```

---

**基本写法：TRIM 去空格**
`TRIM([<位置>] [<字符>] FROM <字符串>)`
```sql
-- 去除两端空格
SELECT TRIM('  Hello  ');
-- 去除指定字符
SELECT TRIM(BOTH 'x' FROM 'xxxHelloxxx');
```

---

## 日期函数

**基本写法：CURRENT_DATE 当前日期**
`CURRENT_DATE`
```sql
-- 获取当前日期
SELECT CURRENT_DATE;
```

---

**基本写法：CURRENT_TIMESTAMP 当前时间戳**
`CURRENT_TIMESTAMP`
```sql
-- 获取当前时间戳
SELECT CURRENT_TIMESTAMP;
```

---

**基本写法：EXTRACT 提取部分**
`EXTRACT(<部分> FROM <日期>)`
```sql
-- 提取年份
SELECT EXTRACT(YEAR FROM birth_date) AS year FROM users;
```

---

**基本写法：DATE_ADD 日期加**
`DATE_ADD(<日期>, INTERVAL <值> <单位>)`
```sql
-- 日期加 7 天
SELECT DATE_ADD(CURRENT_DATE, INTERVAL 7 DAY);
```

---

**基本写法：DATEDIFF 日期差**
`DATEDIFF(<日期1>, <日期2>)`
```sql
-- 计算两个日期相差天数
SELECT DATEDIFF('2024-12-31', '2024-01-01');
```

---

## 数值函数

**基本写法：ROUND 四舍五入**
`ROUND(<数值>, [<小数位>])`
```sql
-- 保留 2 位小数
SELECT ROUND(3.14159, 2);
```

---

**基本写法：CEIL/FLOOR 取整**
`CEIL(<数值>)` 或 `FLOOR(<数值>)`
```sql
-- 向上取整
SELECT CEIL(3.2);
-- 向下取整
SELECT FLOOR(3.8);
```

---

**基本写法：MOD 取模**
`MOD(<被除数>, <除数>)`
```sql
-- 取余数
SELECT MOD(10, 3);
```

---

## NULL 处理

**基本写法：COALESCE 取首个非空**
`COALESCE(<值1>, <值2>, ...)`
```sql
-- 返回第一个非 NULL 值
SELECT COALESCE(nickname, real_name, 'Anonymous') FROM users;
```

---

**基本写法：NULLIF 相等返回 NULL**
`NULLIF(<值1>, <值2>)`
```sql
-- 两值相等时返回 NULL
SELECT NULLIF(salary, 0) FROM employees;
```

---

## 聚合与分组

**基本写法：GROUP BY 分组**
`SELECT <列>, <聚合> FROM <表> GROUP BY <列>`
```sql
-- 按部门统计薪资
SELECT dept, COUNT(*), AVG(salary)
FROM employees
GROUP BY dept;
```

---

**基本写法：HAVING 分组后过滤**
`SELECT ... GROUP BY <列> HAVING <条件>`
```sql
-- 筛选薪资总和大于 100000 的部门
SELECT dept, SUM(salary)
FROM employees
GROUP BY dept
HAVING SUM(salary) > 100000;
```

---

**基本写法：DISTINCT 去重**
`SELECT DISTINCT <列> FROM <表>`
```sql
-- 查询不重复的部门
SELECT DISTINCT dept FROM employees;
```



<!-- ============ 文档分隔线：019-sql/017-SelectExecutionOrder.md ============ -->

# SQL SELECT 执行顺序 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SQL 逻辑执行顺序

**基本写法：完整执行顺序**
`FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`
```sql
-- SQL 子句逻辑执行顺序（非书写顺序）
-- 1. FROM      确定数据源表
-- 2. JOIN      执行连接
-- 3. WHERE     行级过滤
-- 4. GROUP BY  分组
-- 5. HAVING    组级过滤
-- 6. SELECT    选择列与聚合
-- 7. DISTINCT  去重
-- 8. ORDER BY  排序
-- 9. LIMIT     限制行数
```

---

**基本写法：FROM 与 JOIN 先执行**
`FROM <表1> JOIN <表2> ON <条件>`
```sql
-- 先确定数据源再过滤
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.id
WHERE e.salary > 5000;
```

---

**基本写法：WHERE 在 GROUP BY 前执行**
`WHERE <行条件> GROUP BY <列>`
```sql
-- WHERE 过滤行，再对结果分组
SELECT dept, COUNT(*) AS cnt
FROM employees
WHERE status = 'active'
GROUP BY dept;
```

---

**基本写法：HAVING 在 GROUP BY 后执行**
`GROUP BY <列> HAVING <组条件>`
```sql
-- HAVING 过滤分组后的结果
SELECT dept, AVG(salary) AS avg_sal
FROM employees
GROUP BY dept
HAVING AVG(salary) > 50000;
```

---

**基本写法：SELECT 列别名在 ORDER BY 可用**
`SELECT <列> AS <别名> ORDER BY <别名>`
```sql
-- 别名在 ORDER BY 中可用，在 WHERE 中不可用
SELECT name, salary * 12 AS annual_salary
FROM employees
ORDER BY annual_salary DESC;
-- 以下会报错：WHERE 中不能使用别名
-- WHERE annual_salary > 100000
```

---

**基本写法：WHERE 中不能用聚合函数**
`-- 聚合函数过滤必须用 HAVING`
```sql
-- 错误：WHERE 中不能用 COUNT/SUM 等
-- SELECT dept FROM employees WHERE COUNT(*) > 5 GROUP BY dept;

-- 正确：使用 HAVING
SELECT dept FROM employees
GROUP BY dept
HAVING COUNT(*) > 5;
```

---

## 各阶段说明

**基本写法：FROM 阶段**
`FROM <表> [AS <别名>]`
```sql
-- 表别名在 FROM 阶段生效，后续均可使用
SELECT e.name, e.salary
FROM employees AS e
WHERE e.salary > 5000;
```

---

**基本写法：WHERE 阶段行过滤**
`WHERE <条件表达式>`
```sql
-- WHERE 不支持聚合函数，支持普通函数
SELECT name, UPPER(name) AS upper_name
FROM employees
WHERE YEAR(hire_date) = 2024;
```

---

**基本写法：GROUP BY 分组**
`GROUP BY <列1>, <列2>`
```sql
-- 多列分组
SELECT dept, job_title, COUNT(*) AS cnt
FROM employees
GROUP BY dept, job_title;
```

---

**基本写法：SELECT 表达式计算**
`SELECT <列|表达式|聚合函数>`
```sql
-- SELECT 阶段计算列值
SELECT
  name,
  salary,
  salary * 1.1 AS new_salary,
  CASE WHEN salary > 50000 THEN '高' ELSE '低' END AS level
FROM employees;
```

---

**基本写法：DISTINCT 去重**
`SELECT DISTINCT <列>`
```sql
-- DISTINCT 在 SELECT 之后执行
SELECT DISTINCT dept FROM employees;
```

---

**基本写法：ORDER BY 排序**
`ORDER BY <列> [ASC|DESC]`
```sql
-- ORDER BY 可使用列名、别名或列序号
SELECT name, salary FROM employees
ORDER BY 2 DESC;
-- 等价于 ORDER BY salary DESC
```

---

**基本写法：LIMIT 分页**
`LIMIT <行数> [OFFSET <偏移>]`
```sql
-- 分页查询
SELECT name, salary FROM employees
ORDER BY salary DESC
LIMIT 10 OFFSET 20;
-- 或 MySQL 简写
LIMIT 20, 10;
```

---

## 子查询执行顺序

**基本写法：子查询先于外查询执行**
`SELECT * FROM <表> WHERE <列> IN (SELECT <列> FROM <表>)`
```sql
-- 子查询先执行，结果传给外查询
SELECT name FROM employees
WHERE dept_id IN (
  SELECT id FROM departments WHERE location = '北京'
);
```

---

**基本写法：相关子查询逐行执行**
`SELECT * FROM <表> t1 WHERE <列> > (SELECT AVG(<列>) FROM <表> t2 WHERE t2.<列> = t1.<列>)`
```sql
-- 相关子查询：外查询每行都触发一次子查询
SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary > (
  SELECT AVG(e2.salary)
  FROM employees e2
  WHERE e2.dept_id = e1.dept_id
);
```



<!-- ============ 文档分隔线：019-sql/018-DCL.md ============ -->

# SQL 数据控制语言（DCL） 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 用户管理

**基本写法：创建用户**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED BY '<密码>';`
```sql
-- 创建用户（MySQL 语法）
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'SecurePass123!';
-- 允许从任意主机连接
CREATE USER 'appuser'@'%' IDENTIFIED BY 'SecurePass123!';
```

---

**基本写法：修改密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>';`
```sql
-- 修改用户密码
ALTER USER 'appuser'@'localhost' IDENTIFIED BY 'NewPass456!';
```

---

**基本写法：删除用户**
`DROP USER '<用户名>'@'<主机>';`
```sql
-- 删除用户
DROP USER 'appuser'@'localhost';
```

---

**基本写法：查看用户列表**
`SELECT user, host FROM mysql.user;`
```sql
-- 查看所有用户
SELECT user, host FROM mysql.user;
```

---

## 权限授予

**基本写法：授予权限**
`GRANT <权限> ON <数据库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予查询权限
GRANT SELECT ON mydb.* TO 'appuser'@'localhost';
-- 授予全部权限
GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';
-- 授予特定表权限
GRANT SELECT, INSERT, UPDATE ON mydb.users TO 'appuser'@'localhost';
```

---

**基本写法：授予权限并可传递**
`GRANT <权限> ON <数据库>.<表> TO '<用户>'@'<主机>' WITH GRANT OPTION;`
```sql
-- 允许该用户将权限授予他人
GRANT SELECT ON mydb.* TO 'appuser'@'localhost' WITH GRANT OPTION;
```

---

**基本写法：常见权限列表**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <表> TO '<用户>';`
```sql
-- 常用权限
-- SELECT  查询
-- INSERT  插入
-- UPDATE  更新
-- DELETE  删除
-- CREATE  创建表/数据库
-- DROP    删除表/数据库
-- ALTER   修改表结构
-- INDEX   创建/删除索引
-- ALL PRIVILEGES  所有权限
```

---

**基本写法：授予数据库级别权限**
`GRANT <权限> ON <数据库>.* TO '<用户>';`
```sql
-- 授予整个数据库的权限
GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';
```

---

**基本写法：授予全局权限**
`GRANT <权限> ON *.* TO '<用户>';`
```sql
-- 授予所有数据库的权限
GRANT SELECT ON *.* TO 'readonly'@'localhost';
```

---

## 权限撤销

**基本写法：撤销权限**
`REVOKE <权限> ON <数据库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 撤销查询权限
REVOKE SELECT ON mydb.* FROM 'appuser'@'localhost';
-- 撤销全部权限
REVOKE ALL PRIVILEGES ON mydb.* FROM 'appuser'@'localhost';
```

---

**基本写法：撤销 GRANT OPTION**
`REVOKE GRANT OPTION ON <数据库>.<表> FROM '<用户>';`
```sql
-- 撤销授权能力
REVOKE GRANT OPTION ON mydb.* FROM 'appuser'@'localhost';
```

---

## 查看权限

**基本写法：查看当前用户权限**
`SHOW GRANTS;`
```sql
-- 查看当前登录用户的权限
SHOW GRANTS;
```

---

**基本写法：查看指定用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>';`
```sql
-- 查看指定用户的权限
SHOW GRANTS FOR 'appuser'@'localhost';
```

---

## 角色管理

**基本写法：创建角色**
`CREATE ROLE '<角色名>';`
```sql
-- 创建角色
CREATE ROLE 'read_only';
CREATE ROLE 'read_write';
```

---

**基本写法：给角色授权**
`GRANT <权限> ON <表> TO '<角色名>';`
```sql
-- 给角色授予权限
GRANT SELECT ON mydb.* TO 'read_only';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'read_write';
```

---

**基本写法：给用户授予角色**
`GRANT '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 将角色分配给用户
GRANT 'read_only' TO 'appuser'@'localhost';
GRANT 'read_write' TO 'admin'@'localhost';
```

---

**基本写法：撤销角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>';`
```sql
-- 撤销用户的角色
REVOKE 'read_only' FROM 'appuser'@'localhost';
```

---

**基本写法：设置默认角色**
`SET DEFAULT ROLE '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 用户登录后自动激活的角色
SET DEFAULT ROLE 'read_only' TO 'appuser'@'localhost';
SET DEFAULT ROLE ALL TO 'appuser'@'localhost';
```

---

**基本写法：删除角色**
`DROP ROLE '<角色名>';`
```sql
-- 删除角色
DROP ROLE 'read_only';
```

---

## 刷新权限

**基本写法：刷新权限表**
`FLUSH PRIVILEGES;`
```sql
-- 直接修改 mysql.user 表后需刷新
FLUSH PRIVILEGES;
```

---

## PostgreSQL 用户管理

**基本写法：创建用户**
`CREATE USER <用户名> WITH PASSWORD '<密码>';`
```sql
-- PostgreSQL 创建用户
CREATE USER appuser WITH PASSWORD 'SecurePass123!';
-- 创建超级用户
CREATE USER admin WITH PASSWORD 'pass' SUPERUSER;
```

---

**基本写法：PostgreSQL 授权**
`GRANT <权限> ON <表> TO <用户名>;`
```sql
-- PostgreSQL 授权语法
GRANT SELECT, INSERT ON users TO appuser;
GRANT ALL PRIVILEGES ON DATABASE mydb TO appuser;
-- 授予序列权限
GRANT USAGE, SELECT ON SEQUENCE users_id_seq TO appuser;
```

---

**基本写法：PostgreSQL 撤权**
`REVOKE <权限> ON <表> FROM <用户名>;`
```sql
-- PostgreSQL 撤销权限
REVOKE INSERT ON users FROM appuser;
```



<!-- ============ 文档分隔线：019-sql/019-GROUPBYGroupingSet.md ============ -->

# SQL GROUP BY 与分组集合 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：019-sql/020-NaturalJoinUsing.md ============ -->

# SQL 自然连接与 USING 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## NATURAL JOIN 自然连接

**基本写法：自然连接**
`SELECT * FROM <表1> NATURAL JOIN <表2>;`
```sql
-- 自动按同名列连接
SELECT * FROM employees NATURAL JOIN departments;
-- 等价于
SELECT * FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
  AND e.location = d.location;
```

---

**基本写法：自然左连接**
`SELECT * FROM <表1> NATURAL LEFT JOIN <表2>;`
```sql
-- 自然左连接保留左表所有行
SELECT * FROM employees NATURAL LEFT JOIN departments;
```

---

**基本写法：自然右连接**
`SELECT * FROM <表1> NATURAL RIGHT JOIN <表2>;`
```sql
-- 自然右连接保留右表所有行
SELECT * FROM employees NATURAL RIGHT JOIN departments;
```

---

## USING 子句

**基本写法：USING 指定连接列**
`SELECT * FROM <表1> JOIN <表2> USING(<列>);`
```sql
-- 两表中同名的列用 USING 连接
SELECT * FROM employees e
JOIN departments d USING(dept_id);
-- 等价于 ON e.dept_id = d.dept_id
```

---

**基本写法：多列 USING**
`JOIN <表2> USING(<列1>, <列2>)`
```sql
-- 多个同名列同时连接
SELECT * FROM employees e
JOIN departments d USING(dept_id, location_id);
```

---

**基本写法：USING 与 ON 的区别**
`-- USING 合并同名列，ON 可使用不同列名`
```sql
-- USING：结果中 dept_id 只出现一次
SELECT * FROM employees e
JOIN departments d USING(dept_id);
-- 结果列: emp_id, name, dept_id, dept_name

-- ON：结果中两表各有一个 dept_id
SELECT * FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
-- 结果列: emp_id, name, dept_id, dept_id, dept_name
```

---

## JOIN ON 进阶

**基本写法：不等值连接**
`JOIN <表2> ON <非等值条件>`
```sql
-- 连接条件不一定是等号
SELECT e.name, e.salary, g.grade
FROM employees e
JOIN salary_grades g ON e.salary BETWEEN g.min_sal AND g.max_sal;
```

---

**基本写法：多条件连接**
`JOIN <表2> ON <条件1> AND <条件2>`
```sql
-- 连接时附加额外条件
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
  AND e.status = 'active'
  AND d.active = 1;
```

---

**基本写法：CROSS JOIN 笛卡尔积**
`SELECT * FROM <表1> CROSS JOIN <表2>;`
```sql
-- 笛卡尔积：两表所有行组合
SELECT * FROM colors CROSS JOIN sizes;
-- 3 种颜色 x 4 种尺寸 = 12 行
```

---

## 连接类型对比

**基本写法：INNER JOIN**
`SELECT * FROM <表1> INNER JOIN <表2> ON <条件>`
```sql
-- 内连接：只返回匹配的行
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;
```

---

**基本写法：LEFT JOIN**
`SELECT * FROM <表1> LEFT [OUTER] JOIN <表2> ON <条件>`
```sql
-- 左连接：保留左表所有行，右表无匹配为 NULL
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;
```

---

**基本写法：RIGHT JOIN**
`SELECT * FROM <表1> RIGHT [OUTER] JOIN <表2> ON <条件>`
```sql
-- 右连接：保留右表所有行
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;
```

---

**基本写法：FULL OUTER JOIN**
`SELECT * FROM <表1> FULL [OUTER] JOIN <表2> ON <条件>`
```sql
-- 全外连接：保留两表所有行
SELECT e.name, d.dept_name
FROM employees e
FULL JOIN departments d ON e.dept_id = d.dept_id;
```

---

## 多表连接

**基本写法：三表连接**
`SELECT * FROM <表1> JOIN <表2> ON <条件> JOIN <表3> ON <条件>`
```sql
-- 连续连接多张表
SELECT e.name, d.dept_name, p.project_name
FROM employees e
JOIN departments d ON e.dept_id = d.id
JOIN projects p ON e.emp_id = p.lead_id;
```

---

**基本写法：使用 USING 多表连接**
`JOIN <表2> USING(<列>) JOIN <表3> USING(<列>)`
```sql
-- 多表 USING 连接
SELECT * FROM employees e
JOIN departments d USING(dept_id)
JOIN locations l USING(location_id);
```



<!-- ============ 文档分隔线：019-sql/021-SelfJoin.md ============ -->

# SQL 自连接 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 自连接基础

**基本写法：表自连接**
`SELECT a.<列>, b.<列> FROM <表> a JOIN <表> b ON <条件>`
```sql
-- 同一张表连接自身，必须使用别名
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
JOIN employees e2 ON e1.manager_id = e2.emp_id;
```

---

**基本写法：自连接查找上下级**
`SELECT a.<列>, b.<列> FROM <表> a JOIN <表> b ON a.<父列> = b.<子列>`
```sql
-- 查找每个员工的直接上级
SELECT
  e.name AS employee_name,
  m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

---

## 组织架构查询

**基本写法：查找同级同事**
`SELECT b.<列> FROM <表> a JOIN <表> b ON a.<列> = b.<列> AND a.<主键> <> b.<主键>`
```sql
-- 查找同部门的同事
SELECT a.name, b.name AS colleague
FROM employees a
JOIN employees b ON a.dept_id = b.dept_id
WHERE a.emp_id <> b.emp_id;
```

---

**基本写法：查找下属**
`SELECT b.* FROM <表> a JOIN <表> b ON b.<上级列> = a.<主键>`
```sql
-- 查找某经理的所有直接下属
SELECT m.name AS manager, e.name AS subordinate
FROM employees m
JOIN employees e ON e.manager_id = m.id
WHERE m.name = '张三';
```

---

## 对比查询

**基本写法：同表数据对比**
`SELECT a.* FROM <表> a JOIN <表> b ON <关联条件> WHERE <对比条件>`
```sql
-- 查找工资高于自己经理的员工
SELECT e.name, e.salary, m.name AS manager, m.salary AS mgr_salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

---

**基本写法：查找重复数据**
`SELECT a.* FROM <表> a JOIN <表> b ON a.<列> = b.<列> WHERE a.<主键> <> b.<主键>`
```sql
-- 查找重复邮箱的用户
SELECT a.id, a.name, a.email
FROM users a
JOIN users b ON a.email = b.email
WHERE a.id < b.id;
```

---

## 路径与层级查询

**基本写法：查找两级层级路径**
`SELECT a.<列> AS level1, b.<列> AS level2 FROM <表> a JOIN <表> b ON b.<父列> = a.<主键>`
```sql
-- 查找祖孙两级关系
SELECT p.name AS parent, c.name AS child
FROM categories p
JOIN categories c ON c.parent_id = p.id;
```

---

**基本写法：查找三级层级路径**
`SELECT a.<列>, b.<列>, c.<列> FROM <表> a JOIN <表> b ON ... JOIN <表> c ON ...`
```sql
-- 三级层级关系
SELECT
  l1.name AS level1,
  l2.name AS level2,
  l3.name AS level3
FROM categories l1
JOIN categories l2 ON l2.parent_id = l1.id
JOIN categories l3 ON l3.parent_id = l2.id;
```

---

## 日期与序列对比

**基本写法：查找连续事件**
`SELECT a.* FROM <表> a JOIN <表> b ON a.<日期> = b.<日期> - INTERVAL 1 DAY`
```sql
-- 查找连续登录的用户
SELECT a.user_id, a.login_date
FROM login_log a
JOIN login_log b ON a.user_id = b.user_id
  AND a.login_date = DATE_SUB(b.login_date, INTERVAL 1 DAY);
```

---

**基本写法：查找相邻行差值**
`SELECT a.<列>, b.<列>, (b.<列> - a.<列>) AS diff FROM <表> a JOIN <表> b ON <序列条件>`
```sql
-- 查找价格变动
SELECT a.date, a.price, b.date AS next_date, b.price AS next_price,
  b.price - a.price AS price_change
FROM stock_prices a
JOIN stock_prices b ON a.stock_id = b.stock_id
  AND b.date = DATE_ADD(a.date, INTERVAL 1 DAY);
```

---

## 自连接去重

**基本写法：自连接排除重复对**
`SELECT DISTINCT LEAST(a.<列>, b.<列>), GREATEST(a.<列>, b.<列>) FROM <表> a JOIN <表> b ON <条件>`
```sql
-- 查找所有不同的用户对
SELECT DISTINCT
  LEAST(a.user_id, b.user_id) AS user1,
  GREATEST(a.user_id, b.user_id) AS user2
FROM orders a
JOIN orders b ON a.product_id = b.product_id
WHERE a.user_id < b.user_id;
```

---

## 自连接性能优化

**基本写法：自连接加索引提示**
`-- 确保 JOIN 条件列有索引`
```sql
-- 在 manager_id 列上创建索引
CREATE INDEX idx_emp_manager ON employees(manager_id);

-- 查询使用索引
SELECT e.name, m.name AS manager
FROM employees e FORCE INDEX(idx_emp_manager)
JOIN employees m ON e.manager_id = m.id;
```

---

**基本写法：使用子查询替代自连接**
`SELECT * FROM <表> WHERE <列> = (SELECT MAX(<列>) FROM <表>)`
```sql
-- 某些场景子查询比自连接更高效
SELECT name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```



<!-- ============ 文档分隔线：019-sql/022-SemiAntiJoin.md ============ -->

# SQL 半连接与反连接 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 半连接（Semi Join）

**基本写法：IN 实现半连接**
`SELECT * FROM <表1> WHERE <列> IN (SELECT <列> FROM <表2>)`
```sql
-- 查找有订单的客户（半连接：只返回左表匹配行）
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders);
```

---

**基本写法：EXISTS 实现半连接**
`SELECT * FROM <表1> t1 WHERE EXISTS (SELECT 1 FROM <表2> t2 WHERE t2.<列> = t1.<列>)`
```sql
-- EXISTS 半连接：存在即返回
SELECT * FROM customers c
WHERE EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.id
);
```

---

**基本写法：ANY 实现半连接**
`SELECT * FROM <表1> WHERE <列> = ANY (SELECT <列> FROM <表2>)`
```sql
-- = ANY 等价于 IN
SELECT * FROM employees
WHERE dept_id = ANY (SELECT id FROM departments WHERE active = 1);
```

---

## 反连接（Anti Join）

**基本写法：NOT IN 实现反连接**
`SELECT * FROM <表1> WHERE <列> NOT IN (SELECT <列> FROM <表2>)`
```sql
-- 查找没有订单的客户（反连接：只返回左表不匹配行）
SELECT * FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders);
```

---

**基本写法：NOT EXISTS 实现反连接**
`SELECT * FROM <表1> t1 WHERE NOT EXISTS (SELECT 1 FROM <表2> t2 WHERE t2.<列> = t1.<列>)`
```sql
-- NOT EXISTS 反连接：不存在才返回
SELECT * FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.id
);
```

---

**基本写法：LEFT JOIN + IS NULL 实现反连接**
`SELECT * FROM <表1> t1 LEFT JOIN <表2> t2 ON <条件> WHERE t2.<列> IS NULL`
```sql
-- 左连接反连接：连接结果为 NULL 的行
SELECT c.*
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
```

---

## IN 与 EXISTS 对比

**基本写法：IN 适合子查询结果小**
`WHERE <列> IN (SELECT <列> FROM <表>)`
```sql
-- 子查询结果集较小时 IN 更快
SELECT * FROM orders
WHERE customer_id IN (SELECT id FROM customers WHERE vip = 1);
```

---

**基本写法：EXISTS 适合外查询表大**
`WHERE EXISTS (SELECT 1 FROM <表> WHERE <条件>)`
```sql
-- 外查询表大、子查询表小时 EXISTS 更快
SELECT * FROM large_orders lo
WHERE EXISTS (
  SELECT 1 FROM customers c
  WHERE c.id = lo.customer_id AND c.vip = 1
);
```

---

**基本写法：NOT IN 的 NULL 陷阱**
`-- NOT IN 子查询中有 NULL 时不返回任何行`
```sql
-- 危险：子查询含 NULL 时 NOT IN 返回空集
SELECT * FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders WHERE status IS NOT NULL);
-- 如果 orders.customer_id 有 NULL，整个查询返回空

-- 正确做法：排除 NULL
SELECT * FROM customers
WHERE id NOT IN (
  SELECT customer_id FROM orders WHERE customer_id IS NOT NULL
);
```

---

**基本写法：NOT EXISTS 不受 NULL 影响**
`WHERE NOT EXISTS (SELECT 1 FROM <表> WHERE <条件>)`
```sql
-- NOT EXISTS 不受 NULL 影响，更安全
SELECT * FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.id
);
```

---

## 半连接/反连接应用场景

**基本写法：查找已购买特定商品的用户**
`SELECT * FROM <表> WHERE <列> IN (SELECT <列> FROM <表> WHERE <条件>)`
```sql
-- 查找买过商品 A 的用户
SELECT * FROM users
WHERE id IN (
  SELECT user_id FROM orders
  WHERE product_id = (SELECT id FROM products WHERE name = '商品A')
);
```

---

**基本写法：查找未完成任务的项目**
`SELECT * FROM <表1> WHERE NOT EXISTS (SELECT 1 FROM <表2> WHERE <条件>)`
```sql
-- 查找没有已完成任务的项目
SELECT * FROM projects p
WHERE NOT EXISTS (
  SELECT 1 FROM tasks t
  WHERE t.project_id = p.id AND t.status = 'done'
);
```

---

**基本写法：查找部门中所有员工都有奖金**
`SELECT * FROM <表1> t1 WHERE NOT EXISTS (SELECT 1 FROM <表2> t2 WHERE <条件1> AND <反向条件>)`
```sql
-- 查找所有员工都有奖金的部门
SELECT d.dept_name
FROM departments d
WHERE NOT EXISTS (
  SELECT 1 FROM employees e
  WHERE e.dept_id = d.id
  AND NOT EXISTS (
    SELECT 1 FROM bonuses b WHERE b.emp_id = e.id
  )
);
```

---

## 性能优化

**基本写法：半连接提示**
`-- MySQL 半连接优化参数`
```sql
-- 查看半连接策略
SHOW VARIABLES LIKE 'optimizer_switch';
-- 确保 semijoin=on

-- MySQL 半连接策略
-- FIRSTMATCH   匹配第一行即返回
-- LOOSESCAN    使用索引去重
-- MATERIALIZATION 物化子查询
-- DUPLICATEWEEDOUT 去重
```

---

**基本写法：使用 JOIN 替代半连接**
`SELECT DISTINCT t1.* FROM <表1> t1 JOIN <表2> t2 ON <条件>`
```sql
-- 用 JOIN + DISTINCT 替代 IN/EXISTS
SELECT DISTINCT c.*
FROM customers c
JOIN orders o ON o.customer_id = c.id;
```



<!-- ============ 文档分隔线：019-sql/023-RecursiveCTE.md ============ -->

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



<!-- ============ 文档分隔线：019-sql/024-PivotUnpivot.md ============ -->

# SQL 行列转换（Pivot/Unpivot） 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 行转列（Pivot）

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

## 列转行（Unpivot）

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

## 动态行列转换

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

## 常见应用场景

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



<!-- ============ 文档分隔线：019-sql/025-ExecutionPlan.md ============ -->

# SQL 执行计划 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## EXPLAIN 基本用法

**基本写法：MySQL EXPLAIN**
`EXPLAIN <SQL语句>`
```sql
-- 查看 SELECT 执行计划
EXPLAIN SELECT * FROM employees WHERE dept_id = 5;

-- 查看 UPDATE/DELETE 执行计划
EXPLAIN UPDATE employees SET salary = salary * 1.1 WHERE dept_id = 5;
```

---

**基本写法：EXPLAIN ANALYZE 实际执行**
`EXPLAIN ANALYZE <SQL语句>`
```sql
-- PostgreSQL：实际执行并返回耗时统计
EXPLAIN ANALYZE
SELECT * FROM employees WHERE dept_id = 5;

-- MySQL 8.0+ 也支持
EXPLAIN ANALYZE
SELECT * FROM employees e JOIN departments d ON e.dept_id = d.id;
```

---

**基本写法：EXPLAIN FORMAT**
`EXPLAIN FORMAT=JSON <SQL语句>`
```sql
-- MySQL JSON 格式输出更详细信息
EXPLAIN FORMAT=JSON
SELECT * FROM employees WHERE salary > 50000;
```

---

**基本写法：PostgreSQL 详细格式**
`EXPLAIN (FORMAT <格式>) <SQL语句>`
```sql
-- PostgreSQL 输出格式选项
EXPLAIN (FORMAT TEXT) SELECT * FROM employees;
EXPLAIN (FORMAT JSON) SELECT * FROM employees;
EXPLAIN (FORMAT YAML) SELECT * FROM employees;
```

---

**基本写法：查看开销估算**
`EXPLAIN (COSTS ON) <SQL语句>`
```sql
-- PostgreSQL 显示成本估算
EXPLAIN (COSTS ON, ANALYZE ON, BUFFERS ON)
SELECT * FROM employees WHERE salary > 50000;
-- 输出含 cost=0.00..35.50 rows=100 width=256
-- buffers: shared hit=5 read=2
```

---

## MySQL 执行计划字段

**基本写法：type 字段（访问类型）**
`-- type 表示 MySQL 访问数据的方式`
```sql
-- type 性能从好到差：
-- system   表仅一行
-- const    主键/唯一索引等值查询
-- eq_ref   JOIN 时主键/唯一索引等值匹配
-- ref       非唯一索引等值匹配
-- range    索引范围扫描
-- index    全索引扫描
-- ALL      全表扫描（最差）
```

---

**基本写法：key 字段（实际使用的索引）**
`-- key 显示 MySQL 实际使用的索引名`
```sql
-- 查看是否走了索引
EXPLAIN SELECT * FROM employees WHERE emp_id = 100;
-- key: PRIMARY（走了主键索引）

EXPLAIN SELECT * FROM employees WHERE name = 'Alice';
-- key: NULL（未走索引，全表扫描）
```

---

**基本写法：rows 字段（扫描行数估算）**
`-- rows 表示预估需要扫描的行数`
```sql
-- rows 越小越好
EXPLAIN SELECT * FROM employees WHERE emp_id = 100;
-- rows: 1（高效）

EXPLAIN SELECT * FROM employees WHERE salary > 1000;
-- rows: 5000（较差，可能需要优化）
```

---

**基本写法：Extra 字段（额外信息）**
`-- Extra 显示额外的执行信息`
```sql
-- 常见 Extra 信息：
-- Using index        覆盖索引，无需回表
-- Using where        使用 WHERE 过滤
-- Using temporary    使用临时表（需优化）
-- Using filesort     使用文件排序（需优化）
-- Using join buffer   使用连接缓冲（需优化）
-- Impossible WHERE   WHERE 条件恒假
```

---

**基本写法：possible_keys 字段**
`-- possible_keys 显示可能使用的索引`
```sql
EXPLAIN SELECT * FROM employees WHERE dept_id = 5;
-- possible_keys: idx_dept_id
-- key: idx_dept_id  ← 实际用了
```

---

## PostgreSQL 执行计划节点

**基本写法：常见扫描节点**
`-- EXPLAIN 输出的节点类型`
```sql
-- Seq Scan        全表顺序扫描
-- Index Scan      索引扫描（回表）
-- Index Only Scan  仅索引扫描（覆盖索引）
-- Bitmap Index Scan + Bitmap Heap Scan 位图扫描
-- Tid Scan        按 CTID 扫描

EXPLAIN SELECT * FROM employees WHERE id = 100;
-- Index Scan using employees_pkey on employees
```

---

**基本写法：连接节点**
`-- JOIN 操作的执行节点`
```sql
-- Nested Loop    嵌套循环（适合小表）
-- Hash Join      哈希连接（适合大表等值连接）
-- Merge Join     合并连接（有序数据）

EXPLAIN SELECT * FROM employees e
JOIN departments d ON e.dept_id = d.id;
-- Hash Join
```

---

**基本写法：聚合与排序节点**
`-- 聚合和排序的执行方式`
```sql
-- HashAggregate    哈希聚合
-- GroupAggregate   分组聚合
-- Sort             排序
-- Limit            限制行数
-- Unique           去重

EXPLAIN SELECT dept, COUNT(*) FROM employees GROUP BY dept;
-- HashAggregate
```

---

## 索引使用分析

**基本写法：检查索引是否命中**
`EXPLAIN SELECT * FROM <表> WHERE <索引列> = <值>`
```sql
-- 验证索引是否被使用
EXPLAIN SELECT * FROM employees WHERE email = 'test@example.com';
-- key: idx_email ← 索引命中

EXPLAIN SELECT * FROM employees WHERE LEFT(email, 5) = 'test@';
-- key: NULL ← 索引失效（函数操作导致）
```

---

**基本写法：覆盖索引验证**
`EXPLAIN SELECT <索引列> FROM <表> WHERE <条件>`
```sql
-- Extra 显示 Using index 表示覆盖索引
EXPLAIN SELECT emp_id, name FROM employees WHERE dept_id = 5;
-- Extra: Using index ← 覆盖索引，无需回表
```

---

**基本写法：复合索引最左前缀**
`EXPLAIN SELECT * FROM <表> WHERE <复合索引第二列> = <值>`
```sql
-- 验证复合索引是否遵循最左前缀
CREATE INDEX idx_dept_name ON employees(dept_id, name);

-- 能用索引（从 dept_id 开始）
EXPLAIN SELECT * FROM employees WHERE dept_id = 5 AND name = 'Alice';
-- key: idx_dept_name

-- 不能用索引（跳过 dept_id）
EXPLAIN SELECT * FROM employees WHERE name = 'Alice';
-- key: NULL ← 索引失效
```

---

## 慢查询分析

**基本写法：开启慢查询日志**
`SET GLOBAL slow_query_log = ON;`
```sql
-- MySQL 开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过 1 秒记录
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';
```

---

**基本写法：查看慢查询**
`-- 分析慢查询日志`
```bash
# 使用 mysqldumpslow 分析慢日志
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
# -s t 按总时间排序
# -t 10 显示前 10 条
```

---

**基本写法：PostgreSQL 慢查询**
`-- 修改 postgresql.conf`
```ini
# postgresql.conf 配置
log_min_duration_statement = 1000  # 记录超过 1 秒的查询
log_statement = 'none'
log_duration = off
```

---

## 优化器提示

**基本写法：MySQL 索引提示**
`SELECT * FROM <表> FORCE INDEX(<索引名>) WHERE <条件>`
```sql
-- 强制使用指定索引
SELECT * FROM employees FORCE INDEX(idx_dept)
WHERE dept_id = 5;

-- 忽略指定索引
SELECT * FROM employees IGNORE INDEX(idx_name)
WHERE dept_id = 5;
```

---

**基本写法：PostgreSQL 优化器开关**
`SET enable_seqscan = off;`
```sql
-- 临时关闭顺序扫描强制使用索引
SET enable_seqscan = off;
EXPLAIN SELECT * FROM employees WHERE dept_id = 5;
-- 恢复
SET enable_seqscan = on;
```

---

**基本写法：PostgreSQL JOIN 方法控制**
`SET enable_hashjoin = off;`
```sql
-- 强制使用 Nested Loop 而非 Hash Join
SET enable_hashjoin = off;
SET enable_mergejoin = off;
EXPLAIN SELECT * FROM employees e JOIN departments d ON e.dept_id = d.id;
```



<!-- ============ 文档分隔线：019-sql/026-TransactionACIDProperty.md ============ -->

# SQL 事务 ACID 属性 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事务基本操作

**基本写法：开启事务**
`BEGIN [TRANSACTION] [ISOLATION LEVEL <级别>]`
```sql
-- 显式开启事务
BEGIN;
-- 或
START TRANSACTION;
-- 指定隔离级别
BEGIN ISOLATION LEVEL READ COMMITTED;
```

---

**基本写法：提交事务**
`COMMIT [TRANSACTION]`
```sql
-- 提交当前事务
COMMIT;
-- 所有修改永久保存
```

---

**基本写法：回滚事务**
`ROLLBACK [TRANSACTION] [TO <保存点>]`
```sql
-- 回滚整个事务
ROLLBACK;
-- 回滚到指定保存点
ROLLBACK TO SAVEPOINT sp1;
```

---

**基本写法：设置保存点**
`SAVEPOINT <保存点名>`
```sql
-- 在事务中创建保存点
BEGIN;
INSERT INTO orders (id, amount) VALUES (1, 100);
SAVEPOINT after_insert;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 如果出错回滚到插入之后
ROLLBACK TO SAVEPOINT after_insert;
COMMIT;
```

---

**基本写法：释放保存点**
`RELEASE SAVEPOINT <保存点名>`
```sql
-- 释放保存点（不可再回滚到该点）
RELEASE SAVEPOINT sp1;
```

---

**基本写法：自动提交模式**
`SET autocommit = <0|1>`
```sql
-- MySQL 关闭自动提交
SET autocommit = 0;
-- 每条 SQL 需手动 COMMIT 才生效

-- 开启自动提交（默认）
SET autocommit = 1;
```

---

## ACID 属性

**基本写法：A - 原子性（Atomicity）**
`-- 事务内所有操作要么全部成功，要么全部回滚`
```sql
-- 转账示例：扣款和加款必须同时成功或同时失败
BEGIN;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
-- 如果任一步失败，整个事务回滚
COMMIT;
-- 或出错时 ROLLBACK;
```

---

**基本写法：C - 一致性（Consistency）**
`-- 事务前后数据满足完整性约束`
```sql
-- 转账前后总金额不变
-- 转账前：A=1000, B=1000, 总计=2000
-- 转账后：A=500, B=1500, 总计=2000（一致）
-- 约束检查：balance >= 0
ALTER TABLE accounts ADD CONSTRAINT chk_balance CHECK (balance >= 0);
```

---

**基本写法：I - 隔离性（Isolation）**
`-- 并发事务之间互不干扰`
```sql
-- 设置事务隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- 隔离级别从低到高：
-- READ UNCOMMITTED  读未提交（脏读）
-- READ COMMITTED    读已提交（不可重复读）
-- REPEATABLE READ    可重复读（幻读）
-- SERIALIZABLE       串行化（最高隔离）
```

---

**基本写法：D - 持久性（Durability）**
`-- 事务提交后数据永久保存，即使系统崩溃`
```sql
-- COMMIT 后数据写入磁盘
-- MySQL 通过 redo log 保证持久性
-- innodb_flush_log_at_trx_commit = 1（默认）确保每次提交都刷盘
SET GLOBAL innodb_flush_log_at_trx_commit = 1;
```

---

## 事务嵌套

**基本写法：MySQL 不支持真正嵌套**
`-- 通过 SAVEPOINT 模拟嵌套`
```sql
-- MySQL 无嵌套事务，用保存点模拟
BEGIN;
  INSERT INTO t1 VALUES (1);
  SAVEPOINT sp1;
    INSERT INTO t2 VALUES (2);
    -- 模拟内层回滚
    ROLLBACK TO SAVEPOINT sp1;
  INSERT INTO t3 VALUES (3);
COMMIT;
-- t1 和 t3 提交，t2 被回滚
```

---

**基本写法：PostgreSQL 嵌套**
`-- PostgreSQL 也用保存点实现`
```sql
-- PostgreSQL 保存点实现嵌套效果
BEGIN;
  INSERT INTO users (name) VALUES ('Alice');
  SAVEPOINT sp_user;
    INSERT INTO profiles (user_id, bio) VALUES (1, 'Hello');
    -- 如果 profile 插入失败
    ROLLBACK TO sp_user;
    -- 用户仍然存在，可以继续
  INSERT INTO logs (action) VALUES ('user_created');
COMMIT;
```

---

## 隐式提交

**基本写法：DDL 语句隐式提交**
`-- DDL 语句（CREATE/ALTER/DROP/TRUNCATE）自动触发 COMMIT`
```sql
-- 以下语句会自动提交之前的事务
BEGIN;
INSERT INTO t1 VALUES (1);
-- 以下 DDL 会隐式提交
CREATE TABLE t2 (id INT);
-- 此处 INSERT 已经被提交，无法回滚
ROLLBACK;  -- 只能回滚 DDL 之后的操作
```

---

**基本写法：隐式提交的语句**
`-- 会触发隐式提交的语句`
```sql
-- 以下操作会隐式 COMMIT：
-- CREATE / ALTER / DROP TABLE
-- CREATE / DROP INDEX
-- CREATE / DROP DATABASE
-- TRUNCATE TABLE
-- GRANT / REVOKE
-- LOCK TABLES / UNLOCK TABLES
```

---

## 事务超时与锁等待

**基本写法：设置锁等待超时**
`SET innodb_lock_wait_timeout = <秒>`
```sql
-- MySQL 设置行锁等待超时（秒）
SET innodb_lock_wait_timeout = 10;
-- 10 秒内获取不到锁则报错回滚

-- PostgreSQL 设置语句超时
SET statement_timeout = 10000;  -- 毫秒
```

---

**基本写法：死锁检测**
`SET innodb_deadlock_detect = ON;`
```sql
-- MySQL 开启死锁检测（默认开启）
SET GLOBAL innodb_deadlock_detect = ON;
-- 发生死锁时自动回滚代价较小的事务

-- 查看最近一次死锁信息
SHOW ENGINE INNODB STATUS\G
-- 查看 LATEST DETECTED DEADLOCK 部分
```

---

## 分布式事务

**基本写法：XA 事务**
`XA START '<xid>'; ... XA END '<xid>'; XA PREPARE '<xid>'; XA COMMIT '<xid>'`
```sql
-- MySQL XA 分布式事务
XA START 'tx1';
INSERT INTO db1.orders VALUES (1, 100);
XA END 'tx1';
XA PREPARE 'tx1';
-- 所有参与者 PREPARE 成功后
XA COMMIT 'tx1';
-- 或放弃
-- XA ROLLBACK 'tx1';
```

---

**基本写法：查看 XA 事务**
`XA RECOVER;`
```sql
-- 查看所有未完成的 XA 事务
XA RECOVER;
```

---

## 事务最佳实践

**基本写法：事务尽量短小**
`-- 减少锁持有时间，避免长事务`
```sql
-- 不推荐：事务中包含耗时操作
BEGIN;
SELECT * FROM users WHERE id = 1;  -- 查询
-- ... 执行业务逻辑（耗时操作）
UPDATE users SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- 推荐：先准备好数据，事务中只做必要的写操作
SELECT * FROM users WHERE id = 1;  -- 事务外查询
-- ... 业务逻辑
BEGIN;
UPDATE users SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

**基本写法：设置只读事务**
`SET TRANSACTION READ ONLY;`
```sql
-- 声明只读事务，优化器可优化
BEGIN READ ONLY;
SELECT * FROM employees WHERE dept_id = 5;
COMMIT;
```



<!-- ============ 文档分隔线：019-sql/027-IsolationLevel.md ============ -->

# SQL 事务隔离级别 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 四种隔离级别

**基本写法：查看当前隔离级别**
`SELECT @@transaction_isolation;`
```sql
-- MySQL 查看隔离级别
SELECT @@transaction_isolation;
-- 或
SHOW VARIABLES LIKE 'transaction_isolation';
```

---

**基本写法：设置全局隔离级别**
`SET GLOBAL transaction_isolation = '<级别>';`
```sql
-- MySQL 设置全局隔离级别
SET GLOBAL transaction_isolation = 'READ-COMMITTED';
-- 可选值：
-- 'READ-UNCOMMITTED'
-- 'READ-COMMITTED'
-- 'REPEATABLE-READ'（MySQL 默认）
-- 'SERIALIZABLE'
```

---

**基本写法：设置会话隔离级别**
`SET SESSION transaction_isolation = '<级别>';`
```sql
-- 仅影响当前会话
SET SESSION transaction_isolation = 'READ-COMMITTED';
```

---

**基本写法：设置单事务隔离级别**
`SET TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- 仅影响下一个事务
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
SELECT * FROM employees;
COMMIT;
```

---

**基本写法：PostgreSQL 设置隔离级别**
`SET TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- PostgreSQL 在事务内设置
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM employees;
COMMIT;

-- 或在 BEGIN 时指定
BEGIN ISOLATION LEVEL READ COMMITTED;
```

---

## READ UNCOMMITTED（读未提交）

**基本写法：允许脏读**
`SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;`
```sql
-- 最低隔离级别：可读取未提交的数据（脏读）
-- 事务A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 未提交

-- 事务B（READ UNCOMMITTED）
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 可以看到事务A未提交的修改（脏数据）
```

---

## READ COMMITTED（读已提交）

**基本写法：避免脏读**
`SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`
```sql
-- 只能读取已提交的数据
-- 事务A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 未提交

-- 事务B（READ COMMITTED - PostgreSQL 默认）
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 读到的是修改前的值（避免脏读）
```

---

**基本写法：不可重复读现象**
`-- 同一事务内两次读取可能不同`
```sql
-- 事务B 先读取
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 余额 1000

-- 事务A 修改并提交
-- UPDATE accounts SET balance = 500 WHERE id = 1; COMMIT;

-- 事务B 再次读取
SELECT balance FROM accounts WHERE id = 1;  -- 余额 500（不可重复读）
COMMIT;
```

---

## REPEATABLE READ（可重复读）

**基本写法：避免不可重复读**
`SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;`
```sql
-- MySQL 默认隔离级别
-- 同一事务内多次读取结果一致
-- 事务B
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 余额 1000

-- 事务A 修改并提交
-- UPDATE accounts SET balance = 500 WHERE id = 1; COMMIT;

-- 事务B 再次读取
SELECT balance FROM accounts WHERE id = 1;  -- 余额仍为 1000（可重复读）
COMMIT;
```

---

**基本写法：MySQL 的幻读避免**
`-- MySQL InnoDB 通过 MVCC + 间隙锁避免幻读`
```sql
-- MySQL 的 REPEATABLE READ 已基本解决幻读
-- 事务B
BEGIN;
SELECT COUNT(*) FROM orders;  -- 10 条

-- 事务A 插入新订单并提交
-- INSERT INTO orders VALUES (...); COMMIT;

-- 事务B 再次查询
SELECT COUNT(*) FROM orders;  -- 仍为 10 条（无幻读）
COMMIT;
```

---

## SERIALIZABLE（串行化）

**基本写法：最高隔离级别**
`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`
```sql
-- 所有事务串行执行，完全隔离
-- 性能最差，并发最低
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT * FROM accounts WHERE id = 1;
-- 其他事务对此行的修改会被阻塞
COMMIT;
```

---

**基本写法：PostgreSQL SERIALIZABLE**
`-- PostgreSQL 的 SSI 实现真正可串行化`
```sql
-- PostgreSQL 串行化隔离级别使用 SSI（Serializable Snapshot Isolation）
BEGIN ISOLATION LEVEL SERIALIZABLE;
SELECT balance FROM accounts WHERE id = 1;
-- 如果检测到冲突，提交时报错
COMMIT;
-- 可能报错：could not serialize access due to read/write dependencies
```

---

## 隔离级别对比

**基本写法：各级别对比**
`-- 四种隔离级别的现象对比`
```sql
-- 隔离级别          脏读   不可重复读  幻读
-- READ UNCOMMITTED  可能    可能        可能
-- READ COMMITTED    避免    可能        可能
-- REPEATABLE READ   避免    避免        MySQL避免/标准可能
-- SERIALIZABLE      避免    避免        避免
```

---

**基本写法：PostgreSQL 默认隔离级别**
`-- PostgreSQL 默认 READ COMMITTED`
```sql
-- 查看 PostgreSQL 默认隔离级别
SHOW default_transaction_isolation;
-- 默认值：read committed

-- 修改默认隔离级别
ALTER DATABASE mydb SET default_transaction_isolation = 'repeatable read';
```

---

**基本写法：MySQL 默认隔离级别**
`-- MySQL InnoDB 默认 REPEATABLE READ`
```sql
-- 查看 MySQL 默认隔离级别
SELECT @@global.transaction_isolation;
-- 默认值：REPEATABLE-READ
```

---

## 并发问题演示

**基本写法：脏读演示**
`-- READ UNCOMMITTED 下出现脏读`
```sql
-- 会话1
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
BEGIN;
UPDATE accounts SET balance = 0 WHERE id = 1;
-- 不提交

-- 会话2
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 读到 balance=0（脏读：读到未提交的数据）

-- 会话1 回滚
ROLLBACK;
-- 会话2 读到的是无效数据
```

---

**基本写法：不可重复读演示**
`-- READ COMMITTED 下出现不可重复读`
```sql
-- 会话1
BEGIN;
SELECT salary FROM employees WHERE id = 1;  -- 5000

-- 会话2 修改并提交
-- UPDATE employees SET salary = 6000 WHERE id = 1; COMMIT;

-- 会话1 再次查询
SELECT salary FROM employees WHERE id = 1;  -- 6000（不可重复读）
COMMIT;
```

---

**基本写法：幻读演示**
`-- 标准 REPEATABLE READ 下可能出现幻读`
```sql
-- 会话1
BEGIN;
SELECT COUNT(*) FROM employees WHERE dept = 'IT';  -- 5 行

-- 会话2 插入新行并提交
-- INSERT INTO employees VALUES (..., 'IT'); COMMIT;

-- 会话1 再次查询
SELECT COUNT(*) FROM employees WHERE dept = 'IT';  -- 6 行（幻读）
COMMIT;
```

---

**基本写法：加锁避免幻读**
`SELECT ... FOR UPDATE 加锁`
```sql
-- 使用锁避免幻读
BEGIN;
SELECT * FROM employees WHERE dept = 'IT' FOR UPDATE;
-- 此时其他事务无法在此范围插入数据
-- INSERT INTO employees VALUES (..., 'IT') 会被阻塞
COMMIT;
```

---

## 隔离级别选择建议

**基本写法：选择建议**
`-- 根据业务场景选择合适的隔离级别`
```sql
-- 场景与建议：
-- 高并发读、少写    READ COMMITTED
-- 需要一致性读      REPEATABLE READ（MySQL 默认）
-- 金融/关键业务     SERIALIZABLE 或 REPEATABLE READ + 行锁
-- 报表/统计分析     REPEATABLE READ 或 READ ONLY
```



<!-- ============ 文档分隔线：019-sql/028-LockMechanism.md ============ -->

# SQL 锁机制 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 行级锁

**基本写法：共享锁（S 锁）**
`SELECT * FROM <表> WHERE <条件> LOCK IN SHARE MODE;`
```sql
-- MySQL 共享锁：允许其他事务读，不允许写
BEGIN;
SELECT * FROM accounts WHERE id = 1 LOCK IN SHARE MODE;
-- 其他事务可以读，但不能修改此行
COMMIT;
```

---

**基本写法：PostgreSQL 共享锁**
`SELECT * FROM <表> WHERE <条件> FOR SHARE;`
```sql
-- PostgreSQL 共享锁
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR SHARE;
-- 其他事务可加 SHARE 锁，不能加 EXCLUSIVE 锁
COMMIT;
```

---

**基本写法：排他锁（X 锁）**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE;`
```sql
-- 排他锁：阻止其他事务读写
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- 其他事务无法读取或修改此行
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

**基本写法：NOWAIT 不等待锁**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE NOWAIT;`
```sql
-- 获取不到锁立即报错，不等待
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- 如果行被锁定，立即报错：ERROR: could not obtain lock
COMMIT;
```

---

**基本写法：SKIP LOCKED 跳过锁定行**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE SKIP LOCKED;`
```sql
-- 跳过被锁定的行（适合任务队列）
BEGIN;
SELECT id FROM task_queue WHERE status = 'pending'
FOR UPDATE SKIP LOCKED LIMIT 10;
-- 只返回未被锁定的行
COMMIT;
```

---

## 表级锁

**基本写法：MySQL 表锁**
`LOCK TABLES <表> [READ|WRITE];`
```sql
-- MySQL 表锁
LOCK TABLES employees WRITE;
-- 只有当前会话可读写
UNLOCK TABLES;

LOCK TABLES employees READ;
-- 所有会话只能读
UNLOCK TABLES;
```

---

**基本写法：PostgreSQL 表锁**
`LOCK TABLE <表> IN <模式> MODE;`
```sql
-- PostgreSQL 表级锁
LOCK TABLE employees IN SHARE MODE;
-- 允许并发读，阻止写

LOCK TABLE employees IN EXCLUSIVE MODE;
-- 只允许当前事务读写

LOCK TABLE employees IN ACCESS EXCLUSIVE MODE;
-- 最严格：阻止一切并发访问
```

---

**基本写法：锁模式层级**
`-- PostgreSQL 锁模式从弱到强`
```sql
-- ACCESS SHARE        SELECT 自动加（最弱）
-- ROW SHARE          SELECT FOR UPDATE/SHARE 自动加
-- ROW EXCLUSIVE      INSERT/UPDATE/DELETE 自动加
-- SHARE UPDATE       （预留）
-- SHARE              LOCK TABLE ... IN SHARE MODE
-- SHARE ROW EXCLUSIVE
-- EXCLUSIVE
-- ACCESS EXCLUSIVE   DROP/TRUNCATE/ALTER 自动加（最强）
```

---

## 间隙锁（MySQL InnoDB）

**基本写法：间隙锁防止幻读**
`SELECT * FROM <表> WHERE <范围条件> FOR UPDATE;`
```sql
-- REPEATABLE READ 下，范围查询加间隙锁
BEGIN;
SELECT * FROM accounts WHERE id BETWEEN 10 AND 20 FOR UPDATE;
-- 锁定 id=10 到 id=20 之间的间隙
-- 其他事务无法在此范围内插入数据
COMMIT;
```

---

**基本写法：临键锁（Next-Key Lock）**
`-- InnoDB 默认使用临键锁（行锁+间隙锁）`
```sql
-- 临键锁锁定的范围
-- 如果索引有 10, 15, 20
-- SELECT WHERE id > 10 AND id < 20 FOR UPDATE
-- 锁定：(10, 15], (15, 20)
-- 即锁住了 10 到 20 之间所有可能的位置
```

---

**基本写法：查看锁信息**
`SELECT * FROM information_schema.innodb_locks;`
```sql
-- MySQL 查看当前锁
SELECT * FROM performance_schema.data_locks;
SELECT * FROM performance_schema.data_lock_waits;

-- 查看锁等待
SELECT * FROM sys.innodb_lock_waits;
```

---

## 死锁

**基本写法：死锁产生场景**
`-- 两个事务互相等待对方释放锁`
```sql
-- 事务A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;  -- 锁 id=1
UPDATE accounts SET balance = balance + 100 WHERE id = 2;  -- 等待 id=2 的锁

-- 事务B（同时执行）
BEGIN;
UPDATE accounts SET balance = balance - 200 WHERE id = 2;  -- 锁 id=2
UPDATE accounts SET balance = balance + 200 WHERE id = 1;  -- 等待 id=1 的锁
-- 死锁！
```

---

**基本写法：避免死锁**
`-- 按固定顺序访问资源`
```sql
-- 始终按 id 升序加锁，避免交叉等待
-- 事务A 和 事务B 都先锁 id=1 再锁 id=2
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

---

**基本写法：设置锁等待超时**
`SET innodb_lock_wait_timeout = <秒>;`
```sql
-- 设置锁等待超时（默认 50 秒）
SET innodb_lock_wait_timeout = 10;
-- 超时后报错并回滚当前语句
```

---

**基本写法：查看死锁日志**
`SHOW ENGINE INNODB STATUS\G`
```sql
-- 查看最近死锁信息
SHOW ENGINE INNODB STATUS\G
-- 查看 LATEST DETECTED DEADLOCK 部分
```

---

## 悲观锁

**基本写法：悲观锁模式**
`SELECT ... FOR UPDATE`
```sql
-- 先锁定再修改，确保安全
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
-- 应用层判断余额是否足够
-- 如果 balance >= 100
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

**基本写法：悲观锁实现库存扣减**
`SELECT stock FROM products WHERE id = 1 FOR UPDATE;`
```sql
-- 库存扣减使用悲观锁
BEGIN;
SELECT stock FROM products WHERE id = 1 FOR UPDATE;
-- 检查 stock >= order_qty
-- 如果足够
UPDATE products SET stock = stock - 1 WHERE id = 1;
INSERT INTO orders (product_id, qty) VALUES (1, 1);
COMMIT;
```

---

## 乐观锁

**基本写法：版本号实现乐观锁**
`UPDATE <表> SET <列>=<新值>, version=version+1 WHERE id=<ID> AND version=<版本>`
```sql
-- 乐观锁：先读后写，写入时检查版本
-- 1. 读取数据
SELECT id, balance, version FROM accounts WHERE id = 1;
-- 结果: id=1, balance=1000, version=3

-- 2. 写入时检查版本
UPDATE accounts
SET balance = 900, version = version + 1
WHERE id = 1 AND version = 3;
-- 如果受影响行数 = 0，说明已被其他人修改，需重试
```

---

**基本写法：时间戳实现乐观锁**
`UPDATE <表> SET <列>=<值>, updated_at=NOW() WHERE id=<ID> AND updated_at=<时间>`
```sql
-- 使用时间戳替代版本号
SELECT id, balance, updated_at FROM accounts WHERE id = 1;
-- 假设 updated_at = '2026-07-31 10:00:00'

UPDATE accounts
SET balance = 900, updated_at = NOW()
WHERE id = 1 AND updated_at = '2026-07-31 10:00:00';
```

---

**基本写法：CAS 模式**
`UPDATE <表> SET <列>=<新值> WHERE id=<ID> AND <列>=<旧值>`
```sql
-- Compare And Swap 模式
-- 扣减余额：条件是当前余额足够
UPDATE accounts
SET balance = balance - 100
WHERE id = 1 AND balance >= 100;
-- 如果受影响行数 = 0，说明余额不足或被修改
```

---

## 锁监控

**基本写法：MySQL 锁等待查询**
`SELECT * FROM performance_schema.data_lock_waits;`
```sql
-- 查看锁等待情况
SELECT
  r.trx_id AS waiting_trx,
  r.trx_mysql_thread_id AS waiting_thread,
  b.trx_id AS blocking_trx,
  b.trx_mysql_thread_id AS blocking_thread
FROM information_schema.innodb_trx r
JOIN information_schema.innodb_trx b
  ON r.trx_requested_lock_id = b.trx_lock_id;
```

---

**基本写法：PostgreSQL 锁查询**
`SELECT * FROM pg_locks;`
```sql
-- 查看当前所有锁
SELECT pid, locktype, relation::regclass, mode, granted
FROM pg_locks;

-- 查看阻塞的会话
SELECT
  blocked.pid AS blocked_pid,
  blocking.pid AS blocking_pid,
  query
FROM pg_stat_activity blocked
JOIN pg_locks bl ON bl.pid = blocked.pid AND NOT bl.granted
JOIN pg_locks ul ON ul.locktype = bl.locktype
  AND ul.relation = bl.relation AND ul.granted
JOIN pg_stat_activity blocking ON blocking.pid = ul.pid;
```

---

**基本写法：终止阻塞会话**
`SELECT pg_terminate_backend(<pid>);`
```sql
-- PostgreSQL 终止阻塞进程
SELECT pg_terminate_backend(12345);

-- MySQL 杀死会话
KILL 12345;
```



<!-- ============ 文档分隔线：019-sql/029-MVCC.md ============ -->

# SQL 多版本并发控制（MVCC） 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## MVCC 基本概念

**基本写法：MVCC 原理**
`-- 每行保存多个版本，读操作不加锁`
```sql
-- MVCC（Multi-Version Concurrency Control）
-- 每行数据隐藏两个字段：
--   trx_id   最后修改该行的事务 ID
--   roll_ptr 指向 undo log 中该行的上一个版本
-- 读操作根据 Read View 选择合适的版本，不加锁
```

---

**基本写法：查看隐藏字段**
`-- InnoDB 每行隐藏字段`
```sql
-- MySQL InnoDB 每行记录的隐藏列
-- DB_TRX_ID    事务 ID（6 字节）
-- DB_ROLL_PTR  回滚指针（7 字节）
-- DB_ROW_ID     行 ID（6 字节，无主键时自动生成）
```

---

## Read View（读视图）

**基本写法：Read View 创建时机**
`-- 在 READ COMMITTED 下每次 SELECT 创建新 Read View`
```sql
-- READ COMMITTED 隔离级别
-- 每次 SELECT 都创建新的 Read View
-- 因此能看到其他事务已提交的最新数据

-- REPEATABLE READ 隔离级别
-- 事务第一次 SELECT 时创建 Read View
-- 整个事务使用同一个 Read View
-- 因此看到的是事务开始时的快照
```

---

**基本写法：可见性判断规则**
`-- 行版本对当前事务可见的条件`
```sql
-- Read View 包含：
--   m_ids       活跃事务 ID 列表
--   min_trx_id  最小活跃事务 ID
--   max_trx_id  下一个事务 ID
--   creator_trx_id 当前事务 ID

-- 判断规则：
-- 1. trx_id == creator_trx_id → 可见（自己修改的）
-- 2. trx_id < min_trx_id      → 可见（已提交）
-- 3. trx_id >= max_trx_id     → 不可见（未来事务）
-- 4. min_trx_id <= trx_id < max_trx_id 且不在 m_ids → 可见
--    在 m_ids 中 → 不可见，沿 roll_ptr 找历史版本
```

---

## 快照读

**基本写法：普通 SELECT 是快照读**
`SELECT * FROM <表> WHERE <条件>`
```sql
-- 快照读：读取 MVCC 版本链中的可见版本，不加锁
-- READ COMMITTED 下读到最新已提交版本
-- REPEATABLE READ 下读到事务开始时的快照

SELECT * FROM accounts WHERE id = 1;
-- 不加锁，读的是快照
```

---

**基本写法：不同隔离级别的快照读**
`-- 同一查询在不同隔离级别下结果不同`
```sql
-- 会话A（REPEATABLE READ）
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 1000

-- 会话B 修改并提交
-- UPDATE accounts SET balance = 500 WHERE id = 1; COMMIT;

-- 会话A 再次查询（快照读）
SELECT balance FROM accounts WHERE id = 1;  -- 仍为 1000（使用旧快照）
COMMIT;
```

---

## 当前读

**基本写法：加锁查询是当前读**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE`
```sql
-- 当前读：读取最新版本并加锁
-- FOR UPDATE / LOCK IN SHARE MODE / UPDATE / DELETE 都是当前读

BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- 读取最新版本（即使其他事务已提交），并加排他锁
COMMIT;
```

---

**基本写法：UPDATE 是当前读**
`UPDATE <表> SET <列>=<值> WHERE <条件>`
```sql
-- UPDATE/DELETE 操作需要读取最新版本（当前读）
BEGIN;
-- 快照读（读旧版本）
SELECT balance FROM accounts WHERE id = 1;  -- 1000

-- 当前读（读最新版本）
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 此处读到的是最新余额（可能是 2000），更新后为 1900
COMMIT;
```

---

## undo log 版本链

**基本写法：版本链结构**
`-- 每次修改生成 undo log，形成版本链`
```sql
-- 版本链示例
-- 当前行:  trx_id=200, balance=300
--          ↓ roll_ptr
-- undo1:  trx_id=150, balance=500
--          ↓ roll_ptr
-- undo2:  trx_id=100, balance=1000

-- 事务 trx_id=120 的 Read View：
-- 200 不可见（活跃），150 不可见（活跃），100 可见 → 读到 balance=1000
```

---

**基本写法：purge 清理 undo log**
`-- 没有活跃事务引用的旧版本会被清理`
```sql
-- MySQL InnoDB 后台 purge 线程清理 undo log
-- 当 Read View 不再需要某个旧版本时，purge 线程删除它

-- 查看 purge 状态
SHOW ENGINE INNODB STATUS\G
-- 查看 purge 相关信息
```

---

## MVCC 与隔离级别

**基本写法：READ COMMITTED 下的 MVCC**
`-- 每次查询创建新 Read View`
```sql
-- READ COMMITTED 隔离级别
BEGIN;
SELECT * FROM accounts WHERE id = 1;  -- Read View 1，读到余额 1000

-- 其他事务提交修改

SELECT * FROM accounts WHERE id = 1;  -- Read View 2，读到新余额 500
-- 因为每次 SELECT 都创建新的 Read View
COMMIT;
```

---

**基本写法：REPEATABLE READ 下的 MVCC**
`-- 事务内使用同一个 Read View`
```sql
-- REPEATABLE READ 隔离级别
BEGIN;
SELECT * FROM accounts WHERE id = 1;  -- Read View 创建，读到余额 1000

-- 其他事务提交修改

SELECT * FROM accounts WHERE id = 1;  -- 仍为 1000（使用同一 Read View）
COMMIT;
```

---

## MVCC 相关参数

**基本写法：查看 undo 相关参数**
`SHOW VARIABLES LIKE 'innodb_undo%';`
```sql
-- 查看 undo 表空间配置
SHOW VARIABLES LIKE 'innodb_undo%';
-- innodb_undo_directory: undo log 目录
-- innodb_undo_log_truncate: 是否自动截断
-- innodb_undo_tablespaces: undo 表空间数量
```

---

**基本写法：查看隔离级别**
`SELECT @@transaction_isolation;`
```sql
-- 当前隔离级别决定了 MVCC 的行为
SELECT @@transaction_isolation;
-- REPEATABLE-READ（MySQL 默认，MVCC 效果最佳）
```

---

## MVCC 优势

**基本写法：读不加锁**
`-- 读操作不阻塞写，写不阻塞读`
```sql
-- 传统锁机制：
--   读加共享锁 → 阻塞写
--   写加排他锁 → 阻塞读

-- MVCC：
--   快照读不加锁 → 不阻塞写
--   写加排他锁 → 不阻塞快照读
--   大幅提升读多写少场景的并发性能
```

---

## MVCC 局限性

**基本写法：长事务导致 undo 膨胀**
`-- 长事务持有旧 Read View，旧版本无法清理`
```sql
-- 长事务问题
BEGIN;
SELECT * FROM accounts;  -- 创建 Read View

-- ... 长时间不提交
-- 其他事务大量更新
-- undo log 持续增长，无法 purge
-- 导致 ibdata 或 undo 表空间膨胀

COMMIT;  -- 提交后 purge 才能清理旧版本
```

---

**基本写法：更新频繁的表性能下降**
`-- 版本链过长时，查找可见版本需要遍历`
```sql
-- 高频更新场景下，版本链可能很长
-- 读操作需要遍历版本链找到可见版本
-- 导致读性能下降

-- 建议：
-- 1. 避免长事务
-- 2. 高频更新表考虑降低隔离级别
-- 3. 定期 COMMIT 释放 Read View
```

---

## PostgreSQL MVCC

**基本写法：PostgreSQL MVCC 实现**
`-- 每行存储 xmin（创建事务）和 xmax（删除事务）`
```sql
-- PostgreSQL MVCC 使用 xmin/xmax 标记
-- xmin   插入/更新该行的事务 ID
-- xmax   删除/更新该行的事务 ID（0 表示未删除）

-- 查看行的事务信息（需要超级用户）
SELECT xmin, xmax, * FROM accounts WHERE id = 1;
```

---

**基本写法：PostgreSQL 表膨胀**
`-- 更新产生死元组，需要 VACUUM 清理`
```sql
-- PostgreSQL 更新 = 删除旧行 + 插入新行
-- 旧行标记为 dead tuple

-- 手动清理
VACUUM accounts;

-- 分析并清理
VACUUM ANALYZE accounts;

-- 完全清理（锁表）
VACUUM FULL accounts;

-- 自动清理配置
SHOW autovacuum;
```



<!-- ============ 文档分隔线：019-sql/030-SQLAntipattern.md ============ -->

# SQL 反模式 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SELECT * 滥用

**基本写法：避免 SELECT ***
`SELECT <明确列名> FROM <表>`
```sql
-- 反模式：SELECT * 性能差且不安全
-- SELECT * FROM employees;

-- 正确：明确指定列
SELECT id, name, dept_id FROM employees;

-- 使用覆盖索引时更需明确列
SELECT id, name FROM employees WHERE dept_id = 5;
```

---

## 不使用 LIMIT 的查询

**基本写法：查询必须限制行数**
`SELECT * FROM <表> LIMIT <数量>`
```sql
-- 反模式：可能返回百万行
-- SELECT * FROM large_table;

-- 正确：加 LIMIT 或分页
SELECT * FROM large_table LIMIT 100;
-- 分页
SELECT * FROM large_table LIMIT 100 OFFSET 200;
```

---

## 索引列使用函数

**基本写法：避免对索引列使用函数**
`WHERE <列> = <值>`
```sql
-- 反模式：函数导致索引失效
-- SELECT * FROM orders WHERE YEAR(create_time) = 2026;

-- 正确：范围查询使用索引
SELECT * FROM orders
WHERE create_time >= '2026-01-01'
  AND create_time < '2027-01-01';
```

---

**基本写法：避免隐式类型转换**
`WHERE <列> = <同类型值>`
```sql
-- 反模式：字符串列用数字查询（隐式转换，索引失效）
-- SELECT * FROM users WHERE phone = 13800138000;

-- 正确：用引号
SELECT * FROM users WHERE phone = '13800138000';
```

---

## 前导通配符

**基本写法：避免 LIKE 前导通配符**
`WHERE <列> LIKE '<前缀>%'`
```sql
-- 反模式：前导 % 导致全表扫描
-- SELECT * FROM users WHERE name LIKE '%abc';

-- 正确：前缀匹配可使用索引
SELECT * FROM users WHERE name LIKE 'abc%';

-- 需要全文搜索时用全文索引
-- MySQL
ALTER TABLE users ADD FULLTEXT INDEX ft_name(name);
SELECT * FROM users WHERE MATCH(name) AGAINST('abc');
```

---

## N+1 查询问题

**基本写法：使用 JOIN 替代循环查询**
`SELECT ... FROM <表1> JOIN <表2> ON <条件>`
```sql
-- 反模式：循环中逐条查询（N+1 查询）
-- 代码中：
-- for user in users:
--   SELECT * FROM orders WHERE user_id = user.id

-- 正确：一次性 JOIN 查询
SELECT u.name, o.order_id, o.amount
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.id IN (1, 2, 3, 4, 5);
```

---

**基本写法：使用 IN 批量查询**
`WHERE <列> IN (<值1>, <值2>, ...)`
```sql
-- 反模式：逐条查询
-- SELECT * FROM users WHERE id = 1;
-- SELECT * FROM users WHERE id = 2;
-- SELECT * FROM users WHERE id = 3;

-- 正确：批量查询
SELECT * FROM users WHERE id IN (1, 2, 3);
```

---

## 事务过大

**基本写法：事务应短小**
`-- 事务中只包含必要的数据库操作`
```sql
-- 反模式：事务中包含网络请求或大量计算
BEGIN;
SELECT * FROM accounts WHERE id = 1;
-- ... HTTP 请求外部服务（耗时 5 秒）
-- ... 大量计算
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- 正确：先准备数据，事务中只做写操作
SELECT * FROM accounts WHERE id = 1;  -- 事务外
-- ... 外部请求和计算
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

## 过度使用子查询

**基本写法：用 JOIN 替代子查询**
`SELECT ... FROM <表1> JOIN <表2> ON <条件>`
```sql
-- 反模式：相关子查询性能差
-- SELECT name,
--   (SELECT dept_name FROM departments WHERE id = e.dept_id) AS dept
-- FROM employees e;

-- 正确：使用 JOIN
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON d.id = e.dept_id;
```

---

## 缺少索引

**基本写法：WHERE 和 JOIN 条件列建索引**
`CREATE INDEX <索引名> ON <表>(<列>)`
```sql
-- 反模式：高频查询条件无索引
-- SELECT * FROM orders WHERE user_id = 100 AND status = 'paid';

-- 正确：创建复合索引
CREATE INDEX idx_user_status ON orders(user_id, status);
-- 遵循最左前缀原则
```

---

## 复合索引顺序错误

**基本写法：高选择性列放前面**
`CREATE INDEX <索引名> ON <表>(<高选择性列>, <低选择性列>)`
```sql
-- 反模式：低选择性列在前
-- CREATE INDEX idx_status_user ON orders(status, user_id);

-- 正确：高选择性列在前（user_id 区分度高）
CREATE INDEX idx_user_status ON orders(user_id, status);
```

---

## 存储 JSON 大对象

**基本写法：避免在 SQL 中存储大 JSON**
`-- 关系数据使用规范表结构`
```sql
-- 反模式：单列存储大量 JSON
-- CREATE TABLE config (id INT, data JSON);
-- INSERT INTO config VALUES (1, '{"a":1,"b":2,"c":3,...}');

-- 正确：拆分为关系表
CREATE TABLE config_items (
  config_id INT,
  key_name VARCHAR(100),
  value TEXT
);

-- 如果必须用 JSON，建函数索引（MySQL 5.7+）
ALTER TABLE config ADD COLUMN a INT
  GENERATED ALWAYS AS (JSON_EXTRACT(data, '$.a')) STORED;
CREATE INDEX idx_a ON config(a);
```

---

## 使用 COUNT(*) 判断是否存在

**基本写法：用 EXISTS 替代 COUNT(*)**
`SELECT EXISTS(SELECT 1 FROM <表> WHERE <条件>)`
```sql
-- 反模式：COUNT(*) 需要扫描所有匹配行
-- SELECT COUNT(*) FROM orders WHERE user_id = 1;

-- 正确：EXISTS 找到一行即返回
SELECT EXISTS(
  SELECT 1 FROM orders WHERE user_id = 1
);
```

---

## 日期存储为字符串

**基本写法：使用 DATE/TIMESTAMP 类型**
`CREATE TABLE <表> (<日期列> DATE)`
```sql
-- 反模式：用 VARCHAR 存日期
-- CREATE TABLE events (event_date VARCHAR(20));

-- 正确：使用原生日期类型
CREATE TABLE events (
  event_date DATE,
  create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- 可用日期函数比较和计算
SELECT * FROM events WHERE event_date BETWEEN '2026-01-01' AND '2026-12-31';
```

---

## 忽略外键约束

**基本写法：声明外键保证数据完整性**
`FOREIGN KEY (<列>) REFERENCES <父表>(<列>)`
```sql
-- 反模式：应用层维护关系，可能产生孤儿数据
-- CREATE TABLE orders (id INT, user_id INT);  -- 无外键

-- 正确：数据库层约束
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
```

---

## 过度使用 ORM 生成的 SQL

**基本写法：关键查询手写优化**
`-- ORM 适用于简单 CRUD，复杂查询需手写`
```sql
-- 反模式：ORM 生成的 N+1 查询或低效 SQL
-- ORM: user.orders.filter(status='paid')  -- 可能生成多条查询

-- 正确：复杂查询手写 SQL 或使用 ORM 的 JOIN 预加载
SELECT u.*, o.*
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.status = 'paid';
```

---

## 不使用 EXPLAIN 验证

**基本写法：上线前用 EXPLAIN 检查**
`EXPLAIN <关键查询>`
```sql
-- 反模式：直接上线未经执行计划检查的查询

-- 正确：检查执行计划
EXPLAIN SELECT * FROM orders
WHERE user_id = 100 AND status = 'paid';
-- 确认 type 不是 ALL（全表扫描）
-- 确认 key 使用了正确的索引
-- 确认 rows 不过大
```



<!-- ============ 文档分隔线：019-sql/031-PerformanceOptimization.md ============ -->

# SQL 性能优化 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 索引优化

**基本写法：创建合适索引**
`CREATE INDEX <索引名> ON <表>(<列>)`
```sql
-- 为 WHERE 条件列创建索引
CREATE INDEX idx_user_id ON orders(user_id);
-- 为 JOIN 条件列创建索引
CREATE INDEX idx_dept_id ON employees(dept_id);
```

---

**基本写法：复合索引**
`CREATE INDEX <索引名> ON <表>(<列1>, <列2>)`
```sql
-- 多条件查询使用复合索引
CREATE INDEX idx_user_status_date ON orders(user_id, status, create_date);
-- 查询：WHERE user_id=1 AND status='paid'
-- 查询：WHERE user_id=1 AND status='paid' AND create_date > '2026-01-01'
-- 都能命中索引
```

---

**基本写法：覆盖索引**
`-- 索引包含查询所需的所有列`
```sql
-- 查询只需要索引列时，无需回表
CREATE INDEX idx_cover ON employees(dept_id, name, salary);

SELECT name, salary FROM employees WHERE dept_id = 5;
-- Extra: Using index（覆盖索引，性能最优）
```

---

**基本写法：前缀索引**
`CREATE INDEX <索引名> ON <表>(<列>(<前缀长度>))`
```sql
-- 长字符串列使用前缀索引节省空间
CREATE INDEX idx_email ON users(email(10));
-- 仅索引前 10 个字符
```

---

**基本写法：函数索引（MySQL 5.7+）**
`CREATE INDEX <索引名> ON <表>((<表达式>))`
```sql
-- 为函数表达式创建索引
CREATE INDEX idx_lower_email ON users((LOWER(email)));
-- 查询 WHERE LOWER(email) = 'test@example.com' 可用索引

-- PostgreSQL
CREATE INDEX idx_upper_name ON employees(UPPER(name));
```

---

**基本写法：删除无用索引**
`DROP INDEX <索引名> ON <表>`
```sql
-- 索引会降低写入性能，删除不使用的索引
DROP INDEX idx_unused ON users;
```

---

## 查询优化

**基本写法：只查询需要的列**
`SELECT <列1>, <列2> FROM <表>`
```sql
-- 避免 SELECT *
SELECT id, name, email FROM users WHERE active = 1;
```

---

**基本写法：LIMIT 分页**
`SELECT * FROM <表> LIMIT <数量> OFFSET <偏移>`
```sql
-- 深度分页优化：避免大 OFFSET
-- 反模式：OFFSET 1000000（扫描 100 万行）
-- SELECT * FROM orders ORDER BY id LIMIT 10 OFFSET 1000000;

-- 正确：使用游标分页
SELECT * FROM orders
WHERE id > 1000000
ORDER BY id
LIMIT 10;
```

---

**基本写法：JOIN 优化小表驱动大表**
`SELECT * FROM <小表> JOIN <大表> ON <条件>`
```sql
-- 小表驱动大表（小表在外层）
SELECT * FROM small_table s
JOIN large_table l ON l.small_id = s.id
WHERE s.status = 'active';
```

---

**基本写法：子查询优化为 JOIN**
`SELECT ... FROM <表1> JOIN <表2> ON <条件>`
```sql
-- IN 子查询改为 JOIN
-- 反模式
-- SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE vip=1);

-- 优化为 JOIN
SELECT o.* FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.vip = 1;
```

---

**基本写法：批量插入**
`INSERT INTO <表> (<列>) VALUES (<值1>), (<值2>), ...`
```sql
-- 批量插入比逐条快
INSERT INTO users (name, email) VALUES
  ('Alice', 'a@test.com'),
  ('Bob', 'b@test.com'),
  ('Charlie', 'c@test.com');
```

---

**基本写法：INSERT ... ON DUPLICATE KEY UPDATE**
`INSERT INTO <表> (<列>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列>=<值>`
```sql
-- MySQL UPSERT 避免先查后插
INSERT INTO counters (id, count) VALUES (1, 1)
ON DUPLICATE KEY UPDATE count = count + 1;
```

---

**基本写法：PostgreSQL UPSERT**
`INSERT INTO <表> (<列>) VALUES (<值>) ON CONFLICT (<列>) DO UPDATE SET <列>=<值>`
```sql
-- PostgreSQL UPSERT
INSERT INTO counters (id, count) VALUES (1, 1)
ON CONFLICT (id) DO UPDATE SET count = counters.count + 1;
```

---

## 执行计划分析

**基本写法：检查 type 字段**
`EXPLAIN SELECT ...`
```sql
-- type 从好到差：
-- const > eq_ref > ref > range > index > ALL
-- ALL 表示全表扫描，必须优化
EXPLAIN SELECT * FROM users WHERE email = 'test@test.com';
-- 确保 type 为 ref 或更好
```

---

**基本写法：检查 Extra 字段**
`-- 关注 Using filesort 和 Using temporary`
```sql
-- Using filesort: 额外排序，考虑加索引
-- Using temporary: 使用临时表，需优化
-- Using index: 覆盖索引，性能好

EXPLAIN SELECT dept, COUNT(*) FROM employees GROUP BY dept;
-- 如果出现 Using temporary; Using filesort
-- 考虑为 dept 加索引
```

---

## 表结构优化

**基本写法：选择合适数据类型**
`-- 使用最小够用的类型`
```sql
-- 优先使用精确类型
-- TINYINT(1)  代替  INT      节省 3 字节
-- SMALLINT    代替  INT      节省 2 字节
-- VARCHAR(N)  代替  CHAR(N) 变长节省空间
-- DATETIME    代替  VARCHAR 存日期

CREATE TABLE users (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  status TINYINT DEFAULT 0,       -- 而非 INT
  name VARCHAR(50),                -- 而非 CHAR(255)
  email VARCHAR(100)
);
```

---

**基本写法：避免过度规范化**
`-- 高频关联的表可适当冗余`
```sql
-- 订单表冗余商品名称（减少 JOIN）
CREATE TABLE orders (
  id INT PRIMARY KEY,
  product_id INT,
  product_name VARCHAR(100),  -- 冗余字段
  qty INT,
  price DECIMAL(10,2)
);
-- 查询时无需 JOIN products 表
```

---

**基本写法：分区表**
`PARTITION BY <方式>(<列>)`
```sql
-- MySQL 按范围分区
CREATE TABLE logs (
  id BIGINT AUTO_INCREMENT,
  create_time DATETIME,
  level VARCHAR(10),
  message TEXT,
  PRIMARY KEY (id, create_time)
)
PARTITION BY RANGE (TO_DAYS(create_time)) (
  PARTITION p202601 VALUES LESS THAN (TO_DAYS('2026-02-01')),
  PARTITION p202602 VALUES LESS THAN (TO_DAYS('2026-03-01')),
  PARTITION pmax VALUES LESS THAN MAXVALUE
);
```

---

## 缓存优化

**基本写法：使用 SQL_CACHE**
`SELECT SQL_CACHE * FROM <表>`
```sql
-- MySQL 查询缓存（8.0 已移除，仅旧版本）
SELECT SQL_CACHE * FROM users WHERE id = 1;
```

---

**基本写法：应用层缓存**
`-- 高频查询结果缓存到 Redis`
```sql
-- 数据库层面：减少重复查询
-- 对于不变的配置数据，应用层缓存
-- SELECT * FROM config;  -- 每次启动加载一次，缓存到内存
```

---

## 配置优化

**基本写法：InnoDB 缓冲池**
`SET GLOBAL innodb_buffer_pool_size = <字节>`
```sql
-- 设置 InnoDB 缓冲池大小（建议物理内存的 70-80%）
SET GLOBAL innodb_buffer_pool_size = 4294967296;  -- 4GB
```

---

**基本写法：连接池配置**
`SET GLOBAL max_connections = <数量>`
```sql
-- MySQL 最大连接数
SET GLOBAL max_connections = 200;
-- 查看当前连接数
SHOW STATUS LIKE 'Threads_connected';
```

---

**基本写法：PostgreSQL 配置**
`-- 修改 postgresql.conf`
```ini
# postgresql.conf 关键参数
shared_buffers = 2GB          # 内存 25%
effective_cache_size = 6GB     # 内存 75%
work_mem = 16MB
maintenance_work_mem = 256MB
max_connections = 100
```

---

## 慢查询排查

**基本写法：开启慢查询日志**
`SET GLOBAL slow_query_log = ON;`
```sql
-- 开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过 1 秒
```

---

**基本写法：分析慢查询日志**
`-- 使用 mysqldumpslow 分析`
```bash
# 统计慢查询 Top 10
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# 按返回行数排序
mysqldumpslow -s r -t 10 /var/log/mysql/slow.log
```

---

**基本写法：实时查看正在执行的查询**
`SHOW PROCESSLIST;`
```sql
-- 查看当前正在执行的查询
SHOW FULL PROCESSLIST;

-- PostgreSQL
SELECT * FROM pg_stat_activity
WHERE state = 'active';
```



<!-- ============ 文档分隔线：019-sql/032-PLSQLStoredProcedure.md ============ -->

# SQL 存储过程与 PL/SQL 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 存储过程创建

**基本写法：MySQL 存储过程**
`CREATE PROCEDURE <名称>([<参数>]) BEGIN <SQL语句> END`
```sql
-- MySQL 创建存储过程
DELIMITER //
CREATE PROCEDURE get_employee_count(OUT count INT)
BEGIN
  SELECT COUNT(*) INTO count FROM employees;
END //
DELIMITER ;

-- 调用
CALL get_employee_count(@total);
SELECT @total;
```

---

**基本写法：PostgreSQL 函数**
`CREATE OR REPLACE FUNCTION <名称>(<参数>) RETURNS <类型> AS $$ BEGIN <SQL> END; $$ LANGUAGE plpgsql`
```sql
-- PostgreSQL PL/pgSQL 函数
CREATE OR REPLACE FUNCTION get_dept_count(p_dept VARCHAR)
RETURNS INTEGER AS $$
DECLARE
  v_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO v_count FROM employees WHERE dept = p_dept;
  RETURN v_count;
END;
$$ LANGUAGE plpgsql;

-- 调用
SELECT get_dept_count('IT');
```

---

**基本写法：带 IN 参数**
`CREATE PROCEDURE <名>(IN <参数> <类型>)`
```sql
-- MySQL 带输入参数
DELIMITER //
CREATE PROCEDURE get_by_salary(IN min_sal DECIMAL(10,2))
BEGIN
  SELECT name, salary FROM employees WHERE salary >= min_sal;
END //
DELIMITER ;

CALL get_by_salary(50000);
```

---

**基本写法：带 OUT 参数**
`CREATE PROCEDURE <名>(OUT <参数> <类型>)`
```sql
-- MySQL 带输出参数
DELIMITER //
CREATE PROCEDURE get_avg_salary(OUT avg_sal DECIMAL(10,2))
BEGIN
  SELECT AVG(salary) INTO avg_sal FROM employees;
END //
DELIMITER ;

CALL get_avg_salary(@avg);
SELECT @avg;
```

---

**基本写法：带 INOUT 参数**
`CREATE PROCEDURE <名>(INOUT <参数> <类型>)`
```sql
-- INOUT 参数可读可写
DELIMITER //
CREATE PROCEDURE double_value(INOUT val INT)
BEGIN
  SET val = val * 2;
END //
DELIMITER ;

SET @x = 10;
CALL double_value(@x);
SELECT @x;  -- 20
```

---

## 变量与控制流

**基本写法：声明变量**
`DECLARE <变量名> <类型> [DEFAULT <默认值>];`
```sql
-- MySQL 存储过程中声明变量
DELIMITER //
CREATE PROCEDURE demo_vars()
BEGIN
  DECLARE v_name VARCHAR(50) DEFAULT 'unknown';
  DECLARE v_count INT DEFAULT 0;
  DECLARE v_active BOOLEAN DEFAULT TRUE;
  
  SET v_name = 'Alice';
  SELECT COUNT(*) INTO v_count FROM employees;
  
  SELECT v_name, v_count, v_active;
END //
DELIMITER ;
```

---

**基本写法：IF 条件**
`IF <条件> THEN <语句> ELSEIF <条件> THEN <语句> ELSE <语句> END IF`
```sql
-- IF/ELSEIF/ELSE
DELIMITER //
CREATE PROCEDURE get_salary_level(IN sal DECIMAL(10,2), OUT level VARCHAR(20))
BEGIN
  IF sal >= 100000 THEN
    SET level = '高薪';
  ELSEIF sal >= 50000 THEN
    SET level = '中薪';
  ELSE
    SET level = '普通';
  END IF;
END //
DELIMITER ;
```

---

**基本写法：CASE 语句**
`CASE WHEN <条件> THEN <值> ... ELSE <值> END CASE`
```sql
-- CASE WHEN 控制流
DELIMITER //
CREATE PROCEDURE get_grade(IN score INT, OUT grade CHAR(1))
BEGIN
  CASE
    WHEN score >= 90 THEN SET grade = 'A';
    WHEN score >= 80 THEN SET grade = 'B';
    WHEN score >= 70 THEN SET grade = 'C';
    WHEN score >= 60 THEN SET grade = 'D';
    ELSE SET grade = 'F';
  END CASE;
END //
DELIMITER ;
```

---

**基本写法：WHILE 循环**
`WHILE <条件> DO <语句> END WHILE`
```sql
-- WHILE 循环
DELIMITER //
CREATE PROCEDURE fill_numbers(IN max_n INT)
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= max_n DO
    INSERT INTO numbers (value) VALUES (i);
    SET i = i + 1;
  END WHILE;
END //
DELIMITER ;
```

---

**基本写法：LOOP 循环**
`<标签>: LOOP <语句> IF <条件> THEN LEAVE <标签>; END IF; END LOOP`
```sql
-- LOOP + LEAVE
DELIMITER //
CREATE PROCEDURE process_loop(IN max_count INT)
BEGIN
  DECLARE i INT DEFAULT 0;
  loop1: LOOP
    SET i = i + 1;
    IF i > max_count THEN
      LEAVE loop1;
    END IF;
    -- 处理逻辑
  END LOOP loop1;
END //
DELIMITER ;
```

---

**基本写法：REPEAT 循环**
`REPEAT <语句> UNTIL <条件> END REPEAT`
```sql
-- REPEAT UNTIL（先执行后判断）
DELIMITER //
CREATE PROCEDURE repeat_demo(IN max_n INT)
BEGIN
  DECLARE i INT DEFAULT 0;
  REPEAT
    SET i = i + 1;
  UNTIL i >= max_n
  END REPEAT;
END //
DELIMITER ;
```

---

## 游标

**基本写法：声明游标**
`DECLARE <游标名> CURSOR FOR <SELECT语句>`
```sql
-- MySQL 游标
DELIMITER //
CREATE PROCEDURE process_employees()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE v_name VARCHAR(50);
  DECLARE v_salary DECIMAL(10,2);
  
  DECLARE emp_cursor CURSOR FOR
    SELECT name, salary FROM employees WHERE active = 1;
  
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  
  OPEN emp_cursor;
  read_loop: LOOP
    FETCH emp_cursor INTO v_name, v_salary;
    IF done THEN LEAVE read_loop;
    END IF;
    -- 处理每行数据
    INSERT INTO salary_log (name, salary) VALUES (v_name, v_salary);
  END LOOP;
  CLOSE emp_cursor;
END //
DELIMITER ;
```

---

**基本写法：PostgreSQL 游标**
`FOR <变量> IN SELECT <语句> LOOP <处理> END LOOP`
```sql
-- PostgreSQL FOR-IN 循环游标
CREATE OR REPLACE FUNCTION log_salaries()
RETURNS VOID AS $$
DECLARE
  emp_record RECORD;
BEGIN
  FOR emp_record IN SELECT name, salary FROM employees LOOP
    INSERT INTO salary_log (name, salary)
    VALUES (emp_record.name, emp_record.salary);
  END LOOP;
END;
$$ LANGUAGE plpgsql;
```

---

## 异常处理

**基本写法：MySQL 异常处理**
`DECLARE <CONTINUE|EXIT> HANDLER FOR <条件> <处理语句>`
```sql
-- 异常处理
DELIMITER //
CREATE PROCEDURE safe_insert(IN p_name VARCHAR(50))
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    SELECT '插入失败' AS result;
  END;
  
  START TRANSACTION;
  INSERT INTO users (name) VALUES (p_name);
  INSERT INTO logs (action) VALUES (CONCAT('user_created: ', p_name));
  COMMIT;
END //
DELIMITER ;
```

---

**基本写法：PostgreSQL 异常处理**
`BEGIN <语句> EXCEPTION WHEN <异常> THEN <处理> END`
```sql
-- PostgreSQL 异常处理
CREATE OR REPLACE FUNCTION safe_divide(a NUMERIC, b NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
  RETURN a / b;
EXCEPTION
  WHEN division_by_zero THEN
    RETURN NULL;
  WHEN OTHERS THEN
    RAISE NOTICE '未知错误: %', SQLERRM;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

---

## 触发器

**基本写法：创建触发器**
`CREATE TRIGGER <名称> <BEFORE|AFTER> <INSERT|UPDATE|DELETE> ON <表> FOR EACH ROW <动作>`
```sql
-- MySQL 触发器
DELIMITER //
CREATE TRIGGER before_insert_employee
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  IF NEW.salary IS NULL THEN
    SET NEW.salary = 0;
  END IF;
END //
DELIMITER ;
```

---

**基本写法：PostgreSQL 触发器函数**
`CREATE FUNCTION <名>() RETURNS TRIGGER AS $$ BEGIN <动作>; RETURN NEW; END; $$ LANGUAGE plpgsql`
```sql
-- PostgreSQL 触发器（需要先创建函数）
CREATE OR REPLACE FUNCTION update_modified_time()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_time
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION update_modified_time();
```

---

## 删除与查看

**基本写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <名称>`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS get_employee_count;
```

---

**基本写法：查看存储过程**
`SHOW CREATE PROCEDURE <名称>`
```sql
-- MySQL 查看存储过程定义
SHOW CREATE PROCEDURE get_employee_count;

-- 查看所有存储过程
SELECT routine_name, routine_type
FROM information_schema.routines
WHERE routine_schema = 'mydb';
```

---

**基本写法：PostgreSQL 查看函数**
`SELECT proname FROM pg_proc WHERE proname LIKE '<模式>';`
```sql
-- PostgreSQL 查看函数
SELECT proname, prosrc FROM pg_proc
WHERE proname = 'get_dept_count';
```



<!-- ============ 文档分隔线：019-sql/033-LateralDerivedTable.md ============ -->

# SQL LATERAL 与派生表 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 派生表（子查询）

**基本写法：FROM 子句中的派生表**
`SELECT * FROM (SELECT <列> FROM <表>) AS <别名>`
```sql
-- 将子查询结果作为临时表
SELECT t.dept, t.avg_sal
FROM (
  SELECT dept, AVG(salary) AS avg_sal
  FROM employees
  GROUP BY dept
) AS t
WHERE t.avg_sal > 50000;
```

---

**基本写法：多派生表 JOIN**
`SELECT * FROM (SELECT ...) AS t1 JOIN (SELECT ...) AS t2 ON <条件>`
```sql
-- 两个派生表连接
SELECT d.dept_name, a.avg_sal, b.max_sal
FROM (
  SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id
) AS a
JOIN (
  SELECT dept_id, MAX(salary) AS max_sal FROM employees GROUP BY dept_id
) AS b ON a.dept_id = b.dept_id
JOIN departments d ON d.id = a.dept_id;
```

---

**基本写法：派生表必须命名**
`-- 每个派生表必须有别名`
```sql
-- 正确：派生表有别名 t
SELECT * FROM (SELECT 1 AS val) AS t;

-- 错误：缺少别名
-- SELECT * FROM (SELECT 1 AS val);
```

---

## CTE 替代派生表

**基本写法：CTE 提升可读性**
`WITH <CTE名> AS (SELECT ...) SELECT * FROM <CTE名>`
```sql
-- CTE 替代派生表，可读性更好
WITH dept_stats AS (
  SELECT dept_id, AVG(salary) AS avg_sal, MAX(salary) AS max_sal
  FROM employees
  GROUP BY dept_id
)
SELECT d.dept_name, ds.avg_sal, ds.max_sal
FROM dept_stats ds
JOIN departments d ON d.id = ds.dept_id
WHERE ds.avg_sal > 50000;
```

---

**基本写法：多个 CTE**
`WITH <CTE1> AS (...), <CTE2> AS (...) SELECT ...`
```sql
-- 多个 CTE 串联
WITH
  active_emp AS (
    SELECT * FROM employees WHERE status = 'active'
  ),
  dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_sal FROM active_emp GROUP BY dept_id
  )
SELECT e.name, e.salary, da.avg_sal
FROM active_emp e
JOIN dept_avg da ON da.dept_id = e.dept_id
WHERE e.salary > da.avg_sal;
```

---

## LATERAL 子查询

**基本写法：LATERAL 关联子查询**
`SELECT * FROM <表1> t1, LATERAL (SELECT ... WHERE <条件引用t1>) t2`
```sql
-- LATERAL 允许子查询引用前面的表
-- PostgreSQL / MySQL 8.0+
SELECT e.name, t.recent_orders
FROM employees e,
LATERAL (
  SELECT COUNT(*) AS recent_orders
  FROM orders o
  WHERE o.emp_id = e.id
    AND o.create_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
) AS t;
```

---

**基本写法：LATERAL 获取 Top N**
`SELECT * FROM <表1> t1, LATERAL (SELECT ... ORDER BY ... LIMIT N) t2`
```sql
-- 获取每个部门薪资最高的 3 名员工
SELECT d.dept_name, t.emp_name, t.salary
FROM departments d,
LATERAL (
  SELECT e.name AS emp_name, e.salary
  FROM employees e
  WHERE e.dept_id = d.id
  ORDER BY e.salary DESC
  LIMIT 3
) AS t;
```

---

**基本写法：LATERAL 替代窗口函数**
`-- 某些场景 LATERAL 比窗口函数更直观`
```sql
-- 每个客户最近的 3 笔订单
SELECT c.name, t.order_date, t.amount
FROM customers c,
LATERAL (
  SELECT order_date, amount
  FROM orders o
  WHERE o.customer_id = c.id
  ORDER BY order_date DESC
  LIMIT 3
) AS t
ORDER BY c.name, t.order_date DESC;
```

---

**基本写法：MySQL LATERAL**
`-- MySQL 8.0.14+ 支持 LATERAL`
```sql
-- MySQL LATERAL 派生表
SELECT e.name, latest.amount
FROM employees e
LEFT JOIN LATERAL (
  SELECT amount FROM orders
  WHERE orders.emp_id = e.id
  ORDER BY order_date DESC
  LIMIT 1
) AS latest ON TRUE;
```

---

## LATERAL JOIN

**基本写法：LATERAL 与 JOIN 结合**
`SELECT * FROM <表1> JOIN LATERAL (<子查询>) <别名> ON TRUE`
```sql
-- LATERAL JOIN
SELECT d.dept_name, t.total
FROM departments d
JOIN LATERAL (
  SELECT SUM(salary) AS total
  FROM employees e
  WHERE e.dept_id = d.id
) AS t ON TRUE
ORDER BY t.total DESC;
```

---

**基本写法：LEFT JOIN LATERAL**
`SELECT * FROM <表1> LEFT JOIN LATERAL (...) <别名> ON TRUE`
```sql
-- LEFT JOIN LATERAL 保留左表所有行
SELECT c.name, t.latest_order
FROM customers c
LEFT JOIN LATERAL (
  SELECT MAX(order_date) AS latest_order
  FROM orders o
  WHERE o.customer_id = c.id
) AS t ON TRUE;
-- 无订单的客户 latest_order 为 NULL
```

---

## CROSS APPLY / OUTER APPLY（SQL Server）

**基本写法：SQL Server CROSS APPLY**
`SELECT * FROM <表1> CROSS APPLY (<子查询>) <别名>`
```sql
-- SQL Server 的 CROSS APPLY 等价于 LATERAL JOIN
SELECT d.dept_name, t.emp_name, t.salary
FROM departments d
CROSS APPLY (
  SELECT TOP 3 e.name AS emp_name, e.salary
  FROM employees e
  WHERE e.dept_id = d.id
  ORDER BY e.salary DESC
) AS t;
```

---

**基本写法：SQL Server OUTER APPLY**
`SELECT * FROM <表1> OUTER APPLY (<子查询>) <别名>`
```sql
-- OUTER APPLY 等价于 LEFT JOIN LATERAL
SELECT c.name, t.latest_order
FROM customers c
OUTER APPLY (
  SELECT TOP 1 order_date AS latest_order
  FROM orders o
  WHERE o.customer_id = c.id
  ORDER BY order_date DESC
) AS t;
```

---

## 应用场景

**基本写法：每组 Top N**
`SELECT ... FROM <分组表>, LATERAL (SELECT ... LIMIT N)`
```sql
-- 每个分类下销量最高的 3 个商品
SELECT cat.name AS category, t.product_name, t.sales
FROM categories cat,
LATERAL (
  SELECT p.name AS product_name, p.sales
  FROM products p
  WHERE p.category_id = cat.id
  ORDER BY p.sales DESC
  LIMIT 3
) AS t;
```

---

**基本写法：关联聚合**
`SELECT ... FROM <表1>, LATERAL (SELECT <聚合> FROM <表2> WHERE ...)`
```sql
-- 每个用户的订单统计
SELECT u.name, t.order_count, t.total_amount
FROM users u,
LATERAL (
  SELECT COUNT(*) AS order_count, SUM(amount) AS total_amount
  FROM orders o
  WHERE o.user_id = u.id
) AS t
WHERE t.order_count > 0;
```

---

**基本写法：层级查询**
`SELECT ... FROM <表1>, LATERAL (SELECT ... FROM <表2> WHERE <关联>)`
```sql
-- 每个部门及其经理信息
SELECT d.dept_name, m.name AS manager_name, m.salary AS mgr_salary
FROM departments d,
LATERAL (
  SELECT e.name, e.salary
  FROM employees e
  WHERE e.id = d.manager_id
) AS m;
```

---

## LATERAL 性能注意

**基本写法：LATERAL 可能导致嵌套循环**
`-- LATERAL 对每行外查询执行一次子查询`
```sql
-- 如果外查询表很大，LATERAL 可能很慢
-- 确保子查询有索引
-- 或改用 JOIN + 窗口函数

-- LATERAL 方式（每行执行子查询）
SELECT u.name, t.cnt
FROM users u,
LATERAL (SELECT COUNT(*) AS cnt FROM orders WHERE user_id = u.id) AS t;

-- 等价 JOIN 方式（通常更快）
SELECT u.name, o.cnt
FROM users u
LEFT JOIN (
  SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id
) AS o ON o.user_id = u.id;
```

---

**基本写法：索引支持 LATERAL**
`-- 确保 LATERAL 子查询的关联条件列有索引`
```sql
-- 为关联列创建索引
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_orders_emp ON orders(emp_id);

-- LATERAL 子查询使用索引后性能提升
SELECT e.name, t.cnt
FROM employees e,
LATERAL (
  SELECT COUNT(*) AS cnt
  FROM orders o
  WHERE o.emp_id = e.id  -- 此条件使用 idx_orders_emp
) AS t;
```



<!-- ============ 文档分隔线：019-sql/035-RecursiveCTEAdvanced.md ============ -->

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



<!-- ============ 文档分隔线：019-sql/036-MergeStatement.md ============ -->

# SQL MERGE / UPSERT 语句语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## MERGE 标准语法

**基本写法：SQL 标准 MERGE**
`MERGE INTO <目标表> USING <源> ON <条件> WHEN MATCHED THEN ... WHEN NOT MATCHED THEN ...`
```sql
-- SQL:2003 标准，PostgreSQL 15+/Oracle/SQL Server 支持
MERGE INTO target t
USING source s
ON t.id = s.id
WHEN MATCHED THEN
  UPDATE SET t.name = s.name, t.salary = s.salary
WHEN NOT MATCHED THEN
  INSERT (id, name, salary) VALUES (s.id, s.name, s.salary);
```

---

**基本写法：带条件分支**
`WHEN MATCHED AND <条件> THEN ...`
```sql
-- 仅更新满足额外条件的行
MERGE INTO products p
USING staging s
ON p.id = s.id
WHEN MATCHED AND s.price <> p.price THEN
  UPDATE SET p.price = s.price, p.updated_at = NOW()
WHEN MATCHED AND s.deleted = 1 THEN
  DELETE
WHEN NOT MATCHED THEN
  INSERT (id, name, price) VALUES (s.id, s.name, s.price);
```

---

## MySQL UPSERT

**基本写法：INSERT ... ON DUPLICATE KEY UPDATE**
`INSERT INTO <表> VALUES (...) ON DUPLICATE KEY UPDATE <列>=VALUES(<列>)`
```sql
-- MySQL 经典 UPSERT，依赖主键/唯一索引判断冲突
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'a@x.com')
ON DUPLICATE KEY UPDATE
  name = VALUES(name),
  email = VALUES(email),
  updated_at = NOW();

-- MySQL 8.0+ 可用别名引用行
INSERT INTO users (id, name) VALUES (1, 'Bob') AS new
ON DUPLICATE KEY UPDATE name = new.name;
```

---

**基本写法：INSERT IGNORE**
`INSERT IGNORE INTO <表> ...`
```sql
-- 冲突时忽略错误，不插入也不更新
INSERT IGNORE INTO users (id, name) VALUES (1, 'Alice');
-- 若 id=1 已存在，产生 warning 而非 error，跳过该行
```

---

**基本写法：REPLACE INTO**
`REPLACE INTO <表> VALUES (...)`
```sql
-- 冲突时先 DELETE 旧行再 INSERT 新行（注意触发器、自增ID变化）
REPLACE INTO users (id, name, email)
VALUES (1, 'Alice', 'new@x.com');
```

---

## PostgreSQL UPSERT

**基本写法：INSERT ... ON CONFLICT**
`INSERT INTO <表> VALUES (...) ON CONFLICT (<列>) DO UPDATE SET ...`
```sql
-- PostgreSQL 9.5+ 原生 UPSERT
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'a@x.com')
ON CONFLICT (id)
DO UPDATE SET
  name = EXCLUDED.name,
  email = EXCLUDED.email,
  updated_at = NOW();

-- 冲突时什么都不做
INSERT INTO users (id, name) VALUES (1, 'Bob')
ON CONFLICT (id) DO NOTHING;
```

---

**基本写法：基于约束名冲突**
`ON CONFLICT ON CONSTRAINT <约束名> DO ...`
```sql
-- 指定约束名处理冲突
INSERT INTO users (id, email)
VALUES (1, 'a@x.com')
ON CONFLICT ON CONSTRAINT users_email_key
DO UPDATE SET email = EXCLUDED.email;
```

---

**基本写法：条件 UPSERT**
`ON CONFLICT DO UPDATE SET ... WHERE <条件>`
```sql
-- 仅在满足条件时更新
INSERT INTO inventory (product_id, qty)
VALUES (100, 50)
ON CONFLICT (product_id)
DO UPDATE SET qty = inventory.qty + EXCLUDED.qty
WHERE inventory.warehouse = 'A';
```

---

## SQL Server UPSERT

**基本写法：MERGE 语法**
`MERGE INTO <表> AS <别名> USING (VALUES ...) AS <源>(<列>) ON ...`
```sql
-- SQL Server 推荐 MERGE
MERGE INTO users AS t
USING (VALUES (1, 'Alice', 'a@x.com')) AS s(id, name, email)
ON t.id = s.id
WHEN MATCHED THEN
  UPDATE SET t.name = s.name, t.email = s.email
WHEN NOT MATCHED THEN
  INSERT (id, name, email) VALUES (s.id, s.name, s.email);
```

---

**基本写法：IF EXISTS 模式**
`IF EXISTS (SELECT ...) UPDATE ... ELSE INSERT ...`
```sql
-- 兼容性最好的写法
IF EXISTS (SELECT 1 FROM users WHERE id = 1)
  UPDATE users SET name = 'Alice' WHERE id = 1;
ELSE
  INSERT INTO users (id, name) VALUES (1, 'Alice');
```

---

## SQLite UPSERT

**基本写法：ON CONFLICT（SQLite 3.24+）**
`INSERT INTO <表> VALUES (...) ON CONFLICT(<列>) DO UPDATE SET ...`
```sql
-- SQLite 语法与 PostgreSQL 类似
INSERT INTO users (id, name, email)
VALUES (1, 'Alice', 'a@x.com')
ON CONFLICT(id) DO UPDATE SET
  name = excluded.name,
  email = excluded.email;
```

---

**基本写法：REPLACE（SQLite）**
`REPLACE INTO <表> VALUES (...)`
```sql
-- SQLite REPLACE 与 MySQL 一致，先删后插
REPLACE INTO users (id, name) VALUES (1, 'Alice');
```

---

## 批量 UPSERT

**基本写法：多行 UPSERT**
`INSERT INTO <表> VALUES (...),(...),(...) ON CONFLICT ...`
```sql
-- PostgreSQL 批量
INSERT INTO products (id, name, price)
VALUES
  (1, 'A1', 10.0),
  (2, 'A2', 20.0),
  (3, 'A3', 30.0)
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  price = EXCLUDED.price;

-- MySQL 批量
INSERT INTO products (id, name, price)
VALUES (1, 'A1', 10.0), (2, 'A2', 20.0)
ON DUPLICATE KEY UPDATE
  name = VALUES(name), price = VALUES(price);
```



<!-- ============ 文档分隔线：019-sql/037-ExceptIntersect.md ============ -->

# SQL EXCEPT / INTERSECT 集合操作语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：019-sql/038-GroupingSetsCubeRollup.md ============ -->

# SQL GROUPING SETS / CUBE / ROLLUP 多维分组语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## GROUPING SETS 自定义分组

**基本写法：指定多个分组集**
`GROUP BY GROUPING SETS ((<列1>,<列2>), (<列1>), (<列2>), ())`
```sql
-- 一次性输出多种分组聚合结果，等价于多个 UNION ALL
SELECT
  COALESCE(region, '所有地区') AS region,
  COALESCE(product, '所有产品') AS product,
  SUM(amount) AS total
FROM sales
GROUP BY GROUPING SETS (
  (region, product),   -- 按地区+产品
  (region),            -- 仅按地区
  (product),           -- 仅按产品
  ()                   -- 总计
)
ORDER BY region, product;
```

---

**基本写法：单列分组集**
`GROUP BY GROUPING SETS ((<列1>), (<列2>))`
```sql
-- 对不同列分别分组聚合
SELECT dept, NULL AS job, COUNT(*) AS cnt FROM emp GROUP BY GROUPING SETS ((dept),(job));
-- 等价于
SELECT dept, NULL AS job, COUNT(*) FROM emp GROUP BY dept
UNION ALL
SELECT NULL, job, COUNT(*) FROM emp GROUP BY job;
```

---

## ROLLUP 层级汇总

**基本写法：ROLLUP 递减分组**
`GROUP BY ROLLUP (<列1>, <列2>, <列3>)`
```sql
-- ROLLUP(a,b,c) 等价于 GROUPING SETS ((a,b,c),(a,b),(a),())
-- 按列顺序从右到左递减，生成层级小计与总计
SELECT
  COALESCE(year, '总计') AS year,
  COALESCE(region, '小计') AS region,
  COALESCE(product, '-') AS product,
  SUM(amount) AS total
FROM sales
GROUP BY ROLLUP (year, region, product)
ORDER BY year, region, product;
-- 输出：(2024,East,A) (2024,East,小计) (2024,总计,-) (总计,小计,-)
```

---

**基本写法：ROLLUP 部分列**
`GROUP BY <列1>, ROLLUP(<列2>, <列3>)`
```sql
-- 不对第一列做汇总，仅对后续列 ROLLUP
SELECT dept, job, SUM(salary) AS total
FROM employees
GROUP BY dept, ROLLUP(job, level);
-- 等价于 GROUPING SETS ((dept,job,level),(dept,job),(dept))
```

---

## CUBE 全组合汇总

**基本写法：CUBE 全维度组合**
`GROUP BY CUBE (<列1>, <列2>, <列3>)`
```sql
-- CUBE(a,b,c) 生成 2^3=8 种分组：
-- (a,b,c)(a,b)(a,c)(b,c)(a)(b)(c)()
-- 适合多维交叉分析
SELECT
  COALESCE(year, '全部') AS yr,
  COALESCE(region, '全部') AS reg,
  COALESCE(product, '全部') AS prod,
  SUM(amount) AS total,
  COUNT(*) AS cnt
FROM sales
GROUP BY CUBE (year, region, product)
ORDER BY year, region, product;
```

---

**基本写法：CUBE 部分列**
`GROUP BY <列1>, CUBE(<列2>, <列3>)`
```sql
-- dept 固定分组，job 与 level 交叉
SELECT dept, job, level, SUM(salary)
FROM employees
GROUP BY dept, CUBE (job, level);
-- 4 种组合：(dept,job,level)(dept,job)(dept,level)(dept)
```

---

## GROUPING 函数识别小计行

**基本写法：GROUPING 标记**
`GROUPING(<列>) -- 返回 1 表示该列在此行被聚合（NULL 为汇总标记）`
```sql
-- 区分原始 NULL 与汇总产生的 NULL
SELECT
  year,
  region,
  SUM(amount) AS total,
  GROUPING(year) AS gy,       -- 1=年汇总行
  GROUPING(region) AS gr      -- 1=地区汇总行
FROM sales
GROUP BY ROLLUP(year, region);

-- 用 CASE 生成可读标签
SELECT
  CASE WHEN GROUPING(year)=1 THEN '年总计' ELSE year::text END AS yr,
  CASE WHEN GROUPING(region)=1 THEN '地区小计' ELSE region END AS reg,
  SUM(amount) AS total
FROM sales
GROUP BY ROLLUP(year, region);
```

---

**基本写法：GROUPING_ID 组合标记**
`GROUPING_ID(<列1>, <列2>, ...)`
```sql
-- 返回位掩码，标识当前行对应哪个分组集
SELECT year, region, product,
  GROUPING_ID(year, region, product) AS gid,
  SUM(amount) AS total
FROM sales
GROUP BY ROLLUP(year, region, product);
-- gid=0: 明细 (year,region,product)
-- gid=1: year+region 小计（product 被 rollup）
-- gid=3: year 小计
-- gid=7: 总计
```

---

## 三者对比

**基本写法：对比总结**
`GROUP BY <ROLLUP|CUBE|GROUPING SETS> (...)`
```sql
-- ROLLUP(a,b): 3 组 = (a,b)(a)()
-- CUBE(a,b):   4 组 = (a,b)(a)(b)()
-- GROUPING SETS((a,b),(a),(b),()): 等价于 CUBE(a,b)

-- ROLLUP 适合层级维度（年>月>日）
-- CUBE 适合独立维度交叉分析
-- GROUPING SETS 适合自定义任意分组组合
```

---

## MySQL 兼容写法

**基本写法：MySQL 8.0+ 支持**
`GROUP BY <列> WITH ROLLUP`
```sql
-- MySQL 8.0 之前用 WITH ROLLUP，不支持 CUBE/GROUPING SETS
SELECT year, region, SUM(amount) AS total
FROM sales
GROUP BY year, region WITH ROLLUP;

-- MySQL 8.0+ 完整支持 GROUPING SETS/CUBE/ROLLUP
SELECT year, region, SUM(amount)
FROM sales
GROUP BY ROLLUP(year, region);
```



<!-- ============ 文档分隔线：019-sql/039-PivotUnpivotAdvanced.md ============ -->

# SQL PIVOT / UNPIVOT 进阶语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## PIVOT 行转列

**基本写法：SQL Server / Oracle PIVOT**
`SELECT * FROM (<源查询>) AS <别名> PIVOT (<聚合>(<值列>) FOR <列> IN ([<值1>],[<值2>])) AS <别名>`
```sql
-- SQL Server / Oracle 原生 PIVOT
SELECT *
FROM (
  SELECT dept, month, amount FROM sales
) AS src
PIVOT (
  SUM(amount) FOR month IN (
    [Jan], [Feb], [Mar], [Apr], [May], [Jun]
  )
) AS pvt
ORDER BY dept;
-- 输出：dept | Jan | Feb | Mar | Apr | May | Jun
```

---

**基本写法：动态列名 PIVOT（动态 SQL）**
`EXEC('SELECT ... PIVOT ... IN (' + @cols + ')')`
```sql
-- SQL Server 动态生成列名
DECLARE @cols AS NVARCHAR(MAX);
SELECT @cols = STRING_AGG(QUOTENAME(month), ',')
  FROM (SELECT DISTINCT month FROM sales) t;

DECLARE @sql AS NVARCHAR(MAX) = '
SELECT * FROM (SELECT dept, month, amount FROM sales) src
PIVOT (SUM(amount) FOR month IN (' + @cols + ')) pvt';

EXEC sp_executesql @sql;
```

---

## CASE 表达式实现 PIVOT（通用）

**基本写法：CASE WHEN 交叉表**
`SUM(CASE WHEN <条件> THEN <值> ELSE 0 END) AS <列名>`
```sql
-- 所有数据库通用的行转列方案
SELECT
  dept,
  SUM(CASE WHEN month = 'Jan' THEN amount ELSE 0 END) AS Jan,
  SUM(CASE WHEN month = 'Feb' THEN amount ELSE 0 END) AS Feb,
  SUM(CASE WHEN month = 'Mar' THEN amount ELSE 0 END) AS Mar,
  SUM(amount) AS total
FROM sales
GROUP BY dept
ORDER BY dept;
```

---

**基本写法：FILTER 子句（PostgreSQL）**
`SUM(<值>) FILTER (WHERE <条件>) AS <列名>`
```sql
-- PostgreSQL 简洁写法
SELECT
  dept,
  SUM(amount) FILTER (WHERE month = 'Jan') AS Jan,
  SUM(amount) FILTER (WHERE month = 'Feb') AS Feb,
  SUM(amount) FILTER (WHERE month = 'Mar') AS Mar
FROM sales
GROUP BY dept;
```

---

## crosstab（PostgreSQL）

**基本写法：tablefunc 扩展**
`SELECT * FROM crosstab('<源查询>') AS <结果表结构>(<行键> <类型>, <列1> <类型>, ...)`
```sql
-- PostgreSQL tablefunc 扩展
CREATE EXTENSION IF NOT EXISTS tablefunc;

SELECT *
FROM crosstab(
  'SELECT dept, month, amount FROM sales ORDER BY 1,2'
) AS ct(
  dept text,
  Jan numeric, Feb numeric, Mar numeric,
  Apr numeric, May numeric, Jun numeric
);
```

---

## JSONB 实现动态 PIVOT（PostgreSQL）

**基本写法：jsonb_pivot 自定义聚合**
`SELECT <行键>, jsonb_object_agg(<列>, <值>) FROM <表> GROUP BY <行键>`
```sql
-- PostgreSQL 用 JSONB 动态生成列
SELECT
  dept,
  jsonb_object_agg(month, amount) AS 月份金额
FROM sales
GROUP BY dept;
-- 输出：dept | {"Jan":100, "Feb":200, "Mar":150}

-- 展开为行查看
SELECT dept, kv.key AS month, kv.value::numeric AS amount
FROM (
  SELECT dept, jsonb_object_agg(month, amount) AS data FROM sales GROUP BY dept
) t, jsonb_each_text(t.data) AS kv(key, value);
```

---

## UNPIVOT 列转行

**基本写法：SQL Server / Oracle UNPIVOT**
`SELECT * FROM <表> UNPIVOT (<值列> FOR <列名列> IN ([<列1>],[<列2>])) AS <别名>`
```sql
-- 列转行
SELECT dept, month, amount
FROM monthly_sales
UNPIVOT (
  amount FOR month IN ([Jan], [Feb], [Mar], [Apr], [May], [Jun])
) AS upvt;
-- 输入：dept | Jan | Feb | Mar ...
-- 输出：dept | Jan | 100 / dept | Feb | 200 ...
```

---

**基本写法：UNION ALL 通用列转行**
`SELECT <键>, '列名1' AS <列>, <列1> AS <值> UNION ALL ...`
```sql
-- 所有数据库通用
SELECT dept, 'Jan' AS month, Jan AS amount FROM monthly_sales WHERE Jan IS NOT NULL
UNION ALL
SELECT dept, 'Feb' AS month, Feb AS amount FROM monthly_sales WHERE Feb IS NOT NULL
UNION ALL
SELECT dept, 'Mar' AS month, Mar AS amount FROM monthly_sales WHERE Mar IS NOT NULL;
```

---

## VALUES 子句列转行

**基本写法：PostgreSQL/标准 VALUES**
`SELECT <键>, m.month, m.amount FROM <表> CROSS JOIN LATERAL (VALUES ...) AS m(...)`
```sql
-- PostgreSQL 用 LATERAL + VALUES
SELECT dept, m.month, m.amount
FROM monthly_sales ms
CROSS JOIN LATERAL (
  VALUES
    ('Jan', ms.Jan),
    ('Feb', ms.Feb),
    ('Mar', ms.Mar)
) AS m(month, amount)
WHERE m.amount IS NOT NULL;
```

---

## 实战：交叉报表

**基本写法：季度+产品交叉报表**
`SUM(CASE WHEN <产品> THEN <值> END) FILTER ...`
```sql
-- 年度产品季度销售交叉表
SELECT
  product,
  SUM(CASE WHEN quarter = 1 THEN amount ELSE 0 END) AS Q1,
  SUM(CASE WHEN quarter = 2 THEN amount ELSE 0 END) AS Q2,
  SUM(CASE WHEN quarter = 3 THEN amount ELSE 0 END) AS Q3,
  SUM(CASE WHEN quarter = 4 THEN amount ELSE 0 END) AS Q4,
  SUM(amount) AS 全年
FROM sales
WHERE year = 2024
GROUP BY product
ORDER BY product;

-- PostgreSQL FILTER 简写
SELECT product,
  SUM(amount) FILTER (WHERE quarter=1) AS Q1,
  SUM(amount) FILTER (WHERE quarter=2) AS Q2,
  SUM(amount) FILTER (WHERE quarter=3) AS Q3,
  SUM(amount) FILTER (WHERE quarter=4) AS Q4
FROM sales WHERE year = 2024 GROUP BY product;
```



<!-- ============ 文档分隔线：019-sql/040-TypeConversion.md ============ -->

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
