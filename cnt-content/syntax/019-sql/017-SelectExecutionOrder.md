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
