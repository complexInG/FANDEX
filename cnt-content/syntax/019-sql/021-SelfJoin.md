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
