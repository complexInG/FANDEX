# MySQL Join 多表连接

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## INNER JOIN 内连接

**换行写法：内连接查询**
`SELECT <列> FROM <表1> INNER JOIN <表2> ON <连接条件>;`
```sql
-- 查询用户及其订单
SELECT u.username, o.order_no, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

**换行写法：多表内连接**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件> JOIN <表3> ON <条件>;`
```sql
-- 三表关联查询
SELECT u.username, o.order_no, p.product_name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

**换行写法：使用 USING 简化连接**
`SELECT <列> FROM <表1> JOIN <表2> USING (<同名列>);`
```sql
-- 两表同名列时使用 USING
SELECT * FROM users JOIN user_profiles USING (user_id);
```

---

## LEFT JOIN 左连接

**换行写法：左连接查询**
`SELECT <列> FROM <表1> LEFT JOIN <表2> ON <连接条件>;`
```sql
-- 查询所有用户及其订单（含无订单用户）
SELECT u.username, o.order_no
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**换行写法：左连接筛选无匹配记录**
`SELECT <列> FROM <表1> LEFT JOIN <表2> ON <条件> WHERE <表2.列> IS NULL;`
```sql
-- 查询没有订单的用户
SELECT u.username
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

---

## RIGHT JOIN 右连接

**换行写法：右连接查询**
`SELECT <列> FROM <表1> RIGHT JOIN <表2> ON <连接条件>;`
```sql
-- 查询所有订单及其用户（含无用户订单）
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

---

## CROSS JOIN 交叉连接

**单行写法：笛卡尔积**
`SELECT * FROM <表1> CROSS JOIN <表2>;`
```sql
-- 生成两表的笛卡尔积
SELECT * FROM colors CROSS JOIN sizes;
```

**单行写法：逗号连接等价写法**
`SELECT * FROM <表1>, <表2>;`
```sql
-- 逗号分隔等价于 CROSS JOIN
SELECT * FROM colors, sizes;
```

---

## 自连接

**换行写法：员工与上级自连接**
`SELECT <别名1.列>, <别名2.列> FROM <表> <别名1> JOIN <表> <别名2> ON <条件>;`
```sql
-- 查询员工姓名及其直接上级
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：同级分类自连接**
`SELECT <别名1.列>, <别名2.列> FROM <表> <别名1> JOIN <表> <别名2> ON <条件>;`
```sql
-- 查询分类及其父分类名称
SELECT c.name AS category, p.name AS parent
FROM categories c
LEFT JOIN categories p ON c.parent_id = p.id;
```

---

## 自然连接与 USING

**换行写法：NATURAL JOIN 自然连接**
`SELECT * FROM <表1> NATURAL JOIN <表2>;`
```sql
-- 自动按同名列连接
SELECT * FROM users NATURAL JOIN user_profiles;
```

---

## 复合条件连接

**换行写法：多条件连接**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件1> AND <条件2>;`
```sql
-- 多条件关联
SELECT u.username, o.order_no
FROM users u
JOIN orders o ON u.id = o.user_id AND o.status = 1;
```

**换行写法：连接加过滤条件**
`SELECT <列> FROM <表1> JOIN <表2> ON <条件> WHERE <过滤条件>;`
```sql
-- 连接后再过滤
SELECT u.username, o.order_no
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.status = 1 AND o.created_at > '2024-01-01';
```

---

## 聚合与连接

**换行写法：连接加分组聚合**
`SELECT <列>, <聚合函数> FROM <表1> JOIN <表2> ON <条件> GROUP BY <列>;`
```sql
-- 查询每个用户的订单总数和总金额
SELECT u.username, COUNT(o.id) AS order_count, IFNULL(SUM(o.total_amount), 0) AS total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**换行写法：连接加 HAVING 过滤**
`SELECT <列>, <聚合> FROM <表1> JOIN <表2> ON <条件> GROUP BY <列> HAVING <条件>;`
```sql
-- 查询订单金额超过 1000 的用户
SELECT u.username, SUM(o.total_amount) AS total
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username
HAVING total > 1000;
```

---

## 8.0+ 高级连接特性

**换行写法：NOWAIT 不等待锁**
`SELECT * FROM <表1> JOIN <表2> ON <条件> FOR UPDATE NOWAIT;`
```sql
-- 行被锁时立即报错不等待
SELECT * FROM users u JOIN orders o ON u.id = o.user_id FOR UPDATE NOWAIT;
```

**换行写法：SKIP LOCKED 跳过锁定行**
`SELECT * FROM <表1> JOIN <表2> ON <条件> FOR UPDATE SKIP LOCKED;`
```sql
-- 跳过被其他事务锁定的行
SELECT * FROM users u JOIN orders o ON u.id = o.user_id FOR UPDATE SKIP LOCKED;
```

**换行写法：LATERAL 派生表（8.0.14+）**
`SELECT * FROM <表1>, LATERAL (SELECT * FROM <表2> WHERE <条件> LIMIT <数量>) <别名>;`
```sql
-- 关联派生表查询每个用户最近 3 笔订单
SELECT u.username, o.order_no
FROM users u,
LATERAL (
  SELECT order_no, total_amount
  FROM orders
  WHERE user_id = u.id
  ORDER BY created_at DESC
  LIMIT 3
) o;
```
