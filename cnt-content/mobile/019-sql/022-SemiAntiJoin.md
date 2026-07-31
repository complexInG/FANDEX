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
