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
