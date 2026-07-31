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
