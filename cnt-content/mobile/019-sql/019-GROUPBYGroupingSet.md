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
