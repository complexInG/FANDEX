---
order: 10
title: postgresql 模块文档合集
module: 'postgresql'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：021-postgresql/001-TriggerEventTrigger.md ============ -->

# PostgreSQL 触发器与事件触发器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 触发器基础

**换行写法：创建 BEFORE 触发器函数**
`CREATE FUNCTION <函数名>() RETURNS TRIGGER LANGUAGE plpgsql AS $$ BEGIN <逻辑> RETURN NEW END $$`
```sql
-- 创建插入前触发器函数
CREATE FUNCTION before_user_insert()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    NEW.created_at := NOW();
    NEW.updated_at := NOW();
    RETURN NEW;
END $$;
```

**换行写法：创建 BEFORE 触发器**
`CREATE TRIGGER <触发器名> BEFORE INSERT ON <表名> FOR EACH ROW EXECUTE FUNCTION <函数名>()`
```sql
-- 绑定插入前触发器
CREATE TRIGGER trg_before_user_insert
BEFORE INSERT ON users
FOR EACH ROW EXECUTE FUNCTION before_user_insert();
```

**换行写法：创建 AFTER 触发器**
`CREATE TRIGGER <触发器名> AFTER INSERT ON <表名> FOR EACH ROW EXECUTE FUNCTION <函数名>()`
```sql
-- 绑定插入后触发器
CREATE TRIGGER trg_after_user_insert
AFTER INSERT ON users
FOR EACH ROW EXECUTE FUNCTION after_user_insert();
```

**单行写法：删除触发器**
`DROP TRIGGER [IF EXISTS] <触发器名> ON <表名>`
```sql
-- 删除触发器
DROP TRIGGER IF EXISTS trg_before_user_insert ON users;
```

**单行写法：禁用触发器**
`ALTER TABLE <表名> DISABLE TRIGGER <触发器名>`
```sql
-- 禁用指定触发器
ALTER TABLE users DISABLE TRIGGER trg_before_user_insert;
```

**单行写法：启用触发器**
`ALTER TABLE <表名> ENABLE TRIGGER <触发器名>`
```sql
-- 启用指定触发器
ALTER TABLE users ENABLE TRIGGER trg_before_user_insert;
```

---

## BEFORE 触发器

**换行写法：BEFORE INSERT 数据验证**
`IF <条件> THEN RAISE EXCEPTION '<错误信息>' END IF`
```sql
-- 插入前验证薪资不能低于最低标准
CREATE FUNCTION validate_salary()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.salary < 3000 THEN
        RAISE EXCEPTION '薪资不能低于最低标准3000元';
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER trg_validate_salary
BEFORE INSERT OR UPDATE ON employees
FOR EACH ROW EXECUTE FUNCTION validate_salary();
```

**换行写法：BEFORE UPDATE 自动维护时间**
`NEW.<列名> := NOW()`
```sql
-- 更新前自动维护修改时间
CREATE FUNCTION update_modified_time()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    NEW.updated_at := NOW();
    RETURN NEW;
END $$;

CREATE TRIGGER trg_update_modified_time
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_modified_time();
```

**换行写法：BEFORE INSERT 自动生成编号**
`NEW.<列名> := <生成表达式>`
```sql
-- 插入前自动生成订单编号
CREATE FUNCTION generate_order_no()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.order_no IS NULL THEN
        NEW.order_no := 'ORD' || TO_CHAR(NOW(), 'YYYYMMDD') ||
            LPAD((SELECT COUNT(*) + 1 FROM orders WHERE order_date = CURRENT_DATE)::TEXT, 4, '0');
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER trg_generate_order_no
BEFORE INSERT ON orders
FOR EACH ROW EXECUTE FUNCTION generate_order_no();
```

---

## AFTER 触发器

**换行写法：AFTER INSERT 审计日志**
`INSERT INTO <日志表> VALUES (NEW.<列名>...)`
```sql
-- 插入后记录审计日志
CREATE FUNCTION log_user_insert()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO user_audit_log (user_id, action, action_time, details)
    VALUES (NEW.id, 'INSERT', NOW(), 'Created user: ' || NEW.username);
    RETURN NEW;
END $$;

CREATE TRIGGER trg_log_user_insert
AFTER INSERT ON users
FOR EACH ROW EXECUTE FUNCTION log_user_insert();
```

**换行写法：AFTER UPDATE 记录变更**
`IF OLD.<列名> IS DISTINCT FROM NEW.<列名> THEN INSERT INTO ... END IF`
```sql
-- 更新后记录字段变更
CREATE FUNCTION log_user_update()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    IF OLD.username IS DISTINCT FROM NEW.username THEN
        INSERT INTO user_change_log (user_id, field_name, old_value, new_value, changed_at)
        VALUES (OLD.id, 'username', OLD.username, NEW.username, NOW());
    END IF;
    RETURN NEW;
END $$;

CREATE TRIGGER trg_log_user_update
AFTER UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION log_user_update();
```

**换行写法：AFTER DELETE 记录删除**
`INSERT INTO <日志表> VALUES (OLD.<列名>...)`
```sql
-- 删除后记录被删除的数据
CREATE FUNCTION log_user_delete()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO user_delete_log (user_id, username, deleted_at)
    VALUES (OLD.id, OLD.username, NOW());
    RETURN OLD;
END $$;

CREATE TRIGGER trg_log_user_delete
AFTER DELETE ON users
FOR EACH ROW EXECUTE FUNCTION log_user_delete();
```

**换行写法：AFTER INSERT 扣减库存**
`UPDATE <关联表> SET <列名> = <列名> - NEW.<列名> WHERE <条件>`
```sql
-- 订单项插入后扣减商品库存
CREATE FUNCTION decrease_stock()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE id = NEW.product_id;
    RETURN NEW;
END $$;

CREATE TRIGGER trg_decrease_stock
AFTER INSERT ON order_items
FOR EACH ROW EXECUTE FUNCTION decrease_stock();
```

**换行写法：AFTER DELETE 恢复库存**
`UPDATE <关联表> SET <列名> = <列名> + OLD.<列名> WHERE <条件>`
```sql
-- 订单项删除后恢复商品库存
CREATE FUNCTION restore_stock()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE products
    SET stock = stock + OLD.quantity
    WHERE id = OLD.product_id;
    RETURN OLD;
END $$;

CREATE TRIGGER trg_restore_stock
AFTER DELETE ON order_items
FOR EACH ROW EXECUTE FUNCTION restore_stock();
```

---

## INSTEAD OF 触发器

**换行写法：INSTEAD OF 触发器用于视图**
`CREATE TRIGGER <触发器名> INSTEAD OF INSERT ON <视图名> FOR EACH ROW EXECUTE FUNCTION <函数名>()`
```sql
-- 视图插入时实际写入基础表
CREATE FUNCTION instead_of_insert_user_view()
RETURNS TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO users (username, email) VALUES (NEW.username, NEW.email);
    RETURN NEW;
END $$;

CREATE TRIGGER trg_instead_of_insert
INSTEAD OF INSERT ON user_view
FOR EACH ROW EXECUTE FUNCTION instead_of_insert_user_view();
```

---

## 事件触发器

**换行写法：创建事件触发器函数**
`CREATE FUNCTION <函数名>() RETURNS EVENT_TRIGGER LANGUAGE plpgsql AS $$ BEGIN <逻辑> END $$`
```sql
-- 创建 DDL 事件触发器函数
CREATE FUNCTION log_ddl_events()
RETURNS EVENT_TRIGGER
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO ddl_log (event_type, tag, user_name, action_time)
    VALUES (tg_event, tg_tag, current_user, NOW());
END $$;
```

**换行写法：创建 DDL 事件触发器**
`CREATE EVENT TRIGGER <触发器名> ON ddl_command_end EXECUTE FUNCTION <函数名>()`
```sql
-- 绑定 DDL 命令结束事件
CREATE EVENT TRIGGER trg_log_ddl
ON ddl_command_end
EXECUTE FUNCTION log_ddl_events();
```

**换行写法：过滤特定 TAG 的事件触发器**
`CREATE EVENT TRIGGER <触发器名> ON ddl_command_end WHEN tag IN ('<标签>') EXECUTE FUNCTION <函数名>()`
```sql
-- 仅对 CREATE TABLE 和 DROP TABLE 触发
CREATE EVENT TRIGGER trg_log_table_changes
ON ddl_command_end
WHEN tag IN ('CREATE TABLE', 'DROP TABLE', 'ALTER TABLE')
EXECUTE FUNCTION log_ddl_events();
```

**单行写法：删除事件触发器**
`DROP EVENT TRIGGER [IF EXISTS] <触发器名>`
```sql
-- 删除事件触发器
DROP EVENT TRIGGER IF EXISTS trg_log_ddl;
```

---

## 触发器管理

**单行写法：查看表触发器**
`SELECT <列名> FROM information_schema.triggers WHERE <条件>`
```sql
-- 查看表的触发器信息
SELECT trigger_name, event_manipulation, action_timing
FROM information_schema.triggers
WHERE event_object_table = 'users';
```

**单行写法：查看触发器函数**
`SELECT <列名> FROM pg_proc WHERE <条件>`
```sql
-- 查看触发器函数定义
SELECT proname, prosrc FROM pg_proc WHERE proname = 'before_user_insert';
```

**单行写法：重命名触发器**
`ALTER TRIGGER <触发器名> ON <表名> RENAME TO <新名>`
```sql
-- 重命名触发器
ALTER TRIGGER trg_before_user_insert ON users RENAME TO trg_before_insert;
```



<!-- ============ 文档分隔线：021-postgresql/002-StoredProcedureAndFunction.md ============ -->

# PostgreSQL 存储过程与函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 存储过程基础

**换行写法：创建无参存储过程**
`CREATE PROCEDURE <过程名>() LANGUAGE plpgsql AS $$ BEGIN <过程体> END $$`
```sql
-- 创建查询所有用户的存储过程
CREATE PROCEDURE GetAllUsers()
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT id, username, email, created_at
    FROM users
    ORDER BY created_at DESC;
END $$;
```

**单行写法：调用存储过程**
`CALL <过程名>([<参数>...])`
```sql
-- 调用存储过程
CALL GetAllUsers();
```

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>([<参数类型>...])`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS GetAllUsers();
```

---

## PL/pgSQL 控制结构

**换行写法：IF 条件判断**
`IF <条件> THEN <语句> [ELSIF <条件> THEN <语句>] [ELSE <语句>] END IF`
```sql
-- 根据金额计算折扣率
CREATE FUNCTION GetDiscount(p_amount DECIMAL)
RETURNS DECIMAL
LANGUAGE plpgsql AS $$
DECLARE
    v_discount DECIMAL;
BEGIN
    IF p_amount >= 1000 THEN
        v_discount := 0.20;
    ELSIF p_amount >= 500 THEN
        v_discount := 0.10;
    ELSE
        v_discount := 0.00;
    END IF;
    RETURN v_discount;
END $$;
```

**换行写法：CASE 多分支**
`CASE WHEN <条件> THEN <值> [WHEN ...] [ELSE <值>] END`
```sql
-- 根据状态返回描述
CREATE FUNCTION GetStatusDesc(p_status INT)
RETURNS TEXT
LANGUAGE plpgsql AS $$
BEGIN
    RETURN CASE
        WHEN p_status = 1 THEN 'Active'
        WHEN p_status = 0 THEN 'Inactive'
        ELSE 'Unknown'
    END;
END $$;
```

**换行写法：WHILE 循环**
`WHILE <条件> LOOP <语句> END LOOP`
```sql
-- WHILE 循环累加
CREATE FUNCTION SumToN(p_n INT)
RETURNS INT
LANGUAGE plpgsql AS $$
DECLARE
    v_i INT := 1;
    v_sum INT := 0;
BEGIN
    WHILE v_i <= p_n LOOP
        v_sum := v_sum + v_i;
        v_i := v_i + 1;
    END LOOP;
    RETURN v_sum;
END $$;
```

**换行写法：FOR 循环**
`FOR <变量> IN <起始>..<结束> LOOP <语句> END LOOP`
```sql
-- FOR 循环累加
CREATE FUNCTION SumRange(p_start INT, p_end INT)
RETURNS INT
LANGUAGE plpgsql AS $$
DECLARE
    v_sum INT := 0;
BEGIN
    FOR i IN p_start..p_end LOOP
        v_sum := v_sum + i;
    END LOOP;
    RETURN v_sum;
END $$;
```

**换行写法：FOR IN 查询循环**
`FOR <记录> IN <SELECT 语句> LOOP <语句> END LOOP`
```sql
-- 遍历查询结果
CREATE PROCEDURE ProcessUsers()
LANGUAGE plpgsql AS $$
DECLARE
    v_user RECORD;
BEGIN
    FOR v_user IN SELECT id, username FROM users WHERE status = 1 LOOP
        INSERT INTO user_log (user_id, action) VALUES (v_user.id, 'processed');
    END LOOP;
END $$;
```

**换行写法：LOOP 循环**
`LOOP <语句> EXIT WHEN <条件> END LOOP`
```sql
-- LOOP 循环配合 EXIT 跳出
CREATE FUNCTION LoopDemo(p_limit INT)
RETURNS INT
LANGUAGE plpgsql AS $$
DECLARE
    v_i INT := 0;
    v_sum INT := 0;
BEGIN
    LOOP
        v_i := v_i + 1;
        EXIT WHEN v_i > p_limit;
        v_sum := v_sum + v_i;
    END LOOP;
    RETURN v_sum;
END $$;
```

---

## 函数创建

**换行写法：创建标量函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS <类型> LANGUAGE plpgsql AS $$ BEGIN RETURN <值> END $$`
```sql
-- 计算订单总金额的函数
CREATE FUNCTION CalculateOrderTotal(p_order_id INT)
RETURNS DECIMAL(12, 2)
LANGUAGE plpgsql AS $$
DECLARE
    v_total DECIMAL(12, 2);
BEGIN
    SELECT SUM(quantity * unit_price)
    INTO v_total
    FROM order_items
    WHERE order_id = p_order_id;
    RETURN COALESCE(v_total, 0);
END $$;
```

**换行写法：创建返回表函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS TABLE(<列定义>) LANGUAGE plpgsql AS $$ BEGIN <查询> END $$`
```sql
-- 返回表结果集的函数
CREATE FUNCTION GetUsersByStatus(p_status INT)
RETURNS TABLE(id INT, username VARCHAR, email VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT id, username, email FROM users WHERE status = p_status;
END $$;
```

**换行写法：创建集合返回函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS SETOF <表名> LANGUAGE plpgsql AS $$ BEGIN <查询> END $$`
```sql
-- 返回整张表的函数
CREATE FUNCTION GetActiveUsers()
RETURNS SETOF users
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT * FROM users WHERE status = 1;
END $$;
```

---

## 函数调用

**单行写法：SELECT 调用函数**
`SELECT <函数名>(<参数>)`
```sql
-- 调用标量函数
SELECT CalculateOrderTotal(1001) AS total;
```

**换行写法：FROM 调用表函数**
`SELECT * FROM <函数名>(<参数>)`
```sql
-- 调用返回表函数
SELECT * FROM GetUsersByStatus(1);
```

**换行写法：在查询中使用函数**
`SELECT <列名>, <函数名>(<列名>) AS <别名> FROM <表名>`
```sql
-- 在 SELECT 中使用函数
SELECT name, CalculateAge(birthdate) AS age FROM employees;
```

---

## 存储过程调用

**换行写法：带参数的存储过程**
`CALL <过程名>(<参数值>[, ...])`
```sql
-- 调用带参数的存储过程
CALL UpdateUserStatus(1, 0);
```

**换行写法：带事务的存储过程**
`CREATE PROCEDURE <过程名>(<参数>) LANGUAGE plpgsql AS $$ BEGIN <事务> END $$`
```sql
-- 存储过程内使用事务
CREATE PROCEDURE TransferFunds(p_from INT, p_to INT, p_amount DECIMAL)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE accounts SET balance = balance - p_amount WHERE id = p_from;
    UPDATE accounts SET balance = balance + p_amount WHERE id = p_to;
    COMMIT;
END $$;
```

---

## 存储过程删除

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>([<参数类型>...])`
```sql
-- 删除带参数的存储过程
DROP PROCEDURE IF EXISTS TransferFunds(INT, INT, DECIMAL);
```

**单行写法：删除函数**
`DROP FUNCTION [IF EXISTS] <函数名>([<参数类型>...])`
```sql
-- 删除函数
DROP FUNCTION IF EXISTS CalculateOrderTotal(INT);
```

**单行写法：修改函数**
`ALTER FUNCTION <函数名>([<参数类型>...]) OWNER TO <用户>`
```sql
-- 修改函数所有者
ALTER FUNCTION CalculateOrderTotal(INT) OWNER TO admin;
```



<!-- ============ 文档分隔线：021-postgresql/003-PartitionedTable.md ============ -->

# PostgreSQL 分区表

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 范围分区

**换行写法：创建范围分区主表**
`CREATE TABLE <表名> (<列定义>) PARTITION BY RANGE (<列名>)`
```sql
-- 创建按日期范围分区的订单表
CREATE TABLE orders (
    id BIGSERIAL,
    order_date DATE NOT NULL,
    customer_id INT NOT NULL,
    amount DECIMAL(10, 2)
) PARTITION BY RANGE (order_date);
```

**换行写法：创建范围分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES FROM (<起始>) TO (<结束>)`
```sql
-- 创建 2024 年 1 月的分区
CREATE TABLE orders_2024_01 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

**换行写法：创建多个范围分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES FROM (<起始>) TO (<结束>)`
```sql
-- 创建 2024 年 2 月的分区
CREATE TABLE orders_2024_02 PARTITION OF orders
    FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

---

## 列表分区

**换行写法：创建列表分区主表**
`CREATE TABLE <表名> (<列定义>) PARTITION BY LIST (<列名>)`
```sql
-- 创建按地区列表分区的用户表
CREATE TABLE users (
    id BIGSERIAL,
    username VARCHAR(50),
    region VARCHAR(20)
) PARTITION BY LIST (region);
```

**换行写法：创建列表分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES IN (<值>[, <值>...])`
```sql
-- 创建华北地区的分区
CREATE TABLE users_north PARTITION OF users
    FOR VALUES IN ('北京', '天津', '河北');
```

**换行写法：创建多个列表分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES IN (<值>[, <值>...])`
```sql
-- 创建华南地区的分区
CREATE TABLE users_south PARTITION OF users
    FOR VALUES IN ('广东', '广西', '海南');
```

---

## 哈希分区

**换行写法：创建哈希分区主表**
`CREATE TABLE <表名> (<列定义>) PARTITION BY HASH (<列名>)`
```sql
-- 创建按用户 ID 哈希分区的用户表
CREATE TABLE users (
    id BIGSERIAL,
    username VARCHAR(50),
    email VARCHAR(100)
) PARTITION BY HASH (id);
```

**换行写法：创建哈希分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES WITH (MODULUS <模数>, REMAINDER <余数>)`
```sql
-- 创建哈希余数为 0 的分区
CREATE TABLE users_0 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
```

**换行写法：创建多个哈希分区子表**
`CREATE TABLE <子表名> PARTITION OF <父表> FOR VALUES WITH (MODULUS <模数>, REMAINDER <余数>)`
```sql
-- 创建哈希余数为 1 的分区
CREATE TABLE users_1 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);
```

---

## 分区管理

**单行写法：查看分区表信息**
`SELECT <列名> FROM pg_inherits WHERE <条件>`
```sql
-- 查看分区表的子表
SELECT inhrelid::regclass AS child_table
FROM pg_inherits
WHERE inhparent = 'orders'::regclass;
```

**单行写法：查看分区表结构**
`SELECT <列名> FROM pg_partitioned_table WHERE <条件>`
```sql
-- 查看分区表的结构信息
SELECT partrelid::regclass AS table_name, partstrat AS strategy
FROM pg_partitioned_table;
```

**单行写法：分离分区**
`ALTER TABLE <父表> DETACH PARTITION <子表名>`
```sql
-- 分离分区使其成为独立表
ALTER TABLE orders DETACH PARTITION orders_2024_01;
```

**单行写法：附加分区**
`ALTER TABLE <父表> ATTACH PARTITION <子表名> FOR VALUES FROM (<起始>) TO (<结束>)`
```sql
-- 附加分区到父表
ALTER TABLE orders ATTACH PARTITION orders_2024_01
    FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

**单行写法：删除分区子表**
`DROP TABLE <子表名>`
```sql
-- 删除分区子表
DROP TABLE orders_2024_01;
```

**换行写法：创建默认分区**
`CREATE TABLE <子表名> PARTITION OF <父表> DEFAULT`
```sql
-- 创建默认分区存放不匹配的数据
CREATE TABLE users_default PARTITION OF users DEFAULT;
```

---

## 分区索引

**单行写法：在父表创建索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 在父表创建索引自动应用到所有分区
CREATE INDEX idx_orders_date ON orders(order_date);
```

**单行写法：在子表创建索引**
`CREATE INDEX <索引名> ON <子表名>(<列名>)`
```sql
-- 在单个分区子表创建索引
CREATE INDEX idx_orders_2024_01_date ON orders_2024_01(order_date);
```

---

## 分区裁剪

**单行写法：查询触发分区裁剪**
`SELECT * FROM <分区表> WHERE <分区列> <操作符> <值>`
```sql
-- 查询条件触发分区裁剪只扫描匹配分区
SELECT * FROM orders WHERE order_date = '2024-01-15';
```

**单行写法：范围查询触发分区裁剪**
`SELECT * FROM <分区表> WHERE <分区列> BETWEEN <值1> AND <值2>`
```sql
-- 范围查询触发分区裁剪
SELECT * FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';
```

**单行写法：查看查询计划**
`EXPLAIN SELECT * FROM <分区表> WHERE <条件>`
```sql
-- 查看查询是否触发分区裁剪
EXPLAIN SELECT * FROM orders WHERE order_date = '2024-01-15';
```



<!-- ============ 文档分隔线：021-postgresql/004-AdvancedSQL.md ============ -->

# PostgreSQL 高级 SQL

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 窗口函数

**换行写法：RANK 排名函数**
`RANK() OVER (PARTITION BY <列名> ORDER BY <列名> [ASC|DESC])`
```sql
-- 部门内薪资排名
SELECT name, dept_id, salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank
FROM employees;
```

**换行写法：DENSE_RANK 密集排名**
`DENSE_RANK() OVER (PARTITION BY <列名> ORDER BY <列名> [ASC|DESC])`
```sql
-- 部门内薪资密集排名
SELECT name, dept_id, salary,
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank
FROM employees;
```

**换行写法：ROW_NUMBER 行号**
`ROW_NUMBER() OVER (PARTITION BY <列名> ORDER BY <列名> [ASC|DESC])`
```sql
-- 部门内按薪资生成行号
SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num
FROM employees;
```

**换行写法：累计求和**
`SUM(<列名>) OVER (ORDER BY <列名>)`
```sql
-- 按日期累计求和
SELECT order_date, amount,
    SUM(amount) OVER (ORDER BY order_date) AS cumulative
FROM daily_sales;
```

**换行写法：移动平均**
`AVG(<列名>) OVER (ORDER BY <列名> ROWS BETWEEN <范围>)`
```sql
-- 7 日移动平均
SELECT order_date, amount,
    AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM daily_sales;
```

**换行写法：LAG 访问前一行**
`LAG(<列名>[, <偏移量>[, <默认值>]]) OVER (ORDER BY <列名>)`
```sql
-- 计算环比变化
SELECT order_date, amount,
    amount - LAG(amount) OVER (ORDER BY order_date) AS day_over_day
FROM daily_sales;
```

**换行写法：LEAD 访问后一行**
`LEAD(<列名>[, <偏移量>[, <默认值>]]) OVER (ORDER BY <列名>)`
```sql
-- 访问下一行的金额
SELECT order_date, amount,
    LEAD(amount) OVER (ORDER BY ORDER_DATE) AS next_day_amount
FROM daily_sales;
```

**换行写法：FILTER 条件聚合**
`<聚合函数>(*) FILTER (WHERE <条件>)`
```sql
-- 条件聚合统计高收入人数
SELECT dept_id,
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE salary > 50000) AS high_earners
FROM employees
GROUP BY dept_id;
```

---

## CTE 与递归 CTE

**换行写法：普通 CTE**
`WITH <CTE 名称> AS (<SELECT 语句>) SELECT ...`
```sql
-- 使用 CTE 简化复杂查询
WITH dept_stats AS (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees GROUP BY dept_id
)
SELECT e.name, e.salary, ds.avg_salary
FROM employees e JOIN dept_stats ds ON e.dept_id = ds.dept_id;
```

**换行写法：递归 CTE**
`WITH RECURSIVE <CTE 名称> AS (<基础查询> UNION ALL <递归查询>) SELECT ...`
```sql
-- 递归查询组织树
WITH RECURSIVE org_tree AS (
    SELECT emp_id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, ot.level + 1
    FROM employees e JOIN org_tree ot ON e.manager_id = ot.emp_id
)
SELECT * FROM org_tree;
```

---

## 横向连接

**换行写法：LATERAL 横向连接**
`SELECT <列名> FROM <表1>, LATERAL (<子查询>) AS <别名>`
```sql
-- 每行执行子查询获取前 3 名
SELECT d.dept_name, top3.name, top3.salary
FROM departments d,
LATERAL (
    SELECT name, salary FROM employees
    WHERE dept_id = d.id
    ORDER BY salary DESC LIMIT 3
) top3;
```

---

## 分组集

**换行写法：ROLLUP 层次汇总**
`GROUP BY ROLLUP (<列名>[, <列名>...])`
```sql
-- 按部门和职位层次汇总薪资
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY ROLLUP (dept_id, job_title);
```

**换行写法：CUBE 多维汇总**
`GROUP BY CUBE (<列名>[, <列名>...])`
```sql
-- 按部门和职位多维汇总薪资
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY CUBE (dept_id, job_title);
```

**换行写法：GROUPING SETS 自定义分组集**
`GROUP BY GROUPING SETS ((<列组合1>), (<列组合2>), ...)`
```sql
-- 自定义分组集汇总薪资
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY GROUPING SETS ((dept_id, job_title), (dept_id), ());
```



<!-- ============ 文档分隔线：021-postgresql/005-RoleBasedPermissionManagement.md ============ -->

# PostgreSQL 基于角色的权限管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 用户管理

**单行写法：创建用户**
`CREATE USER <用户名> [WITH] PASSWORD '<密码>'`
```sql
-- 创建带密码的用户
CREATE USER app_user WITH PASSWORD 'StrongP@ss123';
```

**单行写法：创建带登录权限的用户**
`CREATE ROLE <角色名> WITH LOGIN PASSWORD '<密码>'`
```sql
-- 创建带登录权限的角色
CREATE ROLE app_role WITH LOGIN PASSWORD 'StrongP@ss123';
```

**单行写法：修改用户密码**
`ALTER USER <用户名> [WITH] PASSWORD '<新密码>'`
```sql
-- 修改用户密码
ALTER USER app_user WITH PASSWORD 'NewP@ss456';
```

**单行写法：删除用户**
`DROP USER [IF EXISTS] <用户名>`
```sql
-- 删除用户
DROP USER IF EXISTS app_user;
```

**单行写法：查看所有用户**
`SELECT <列名> FROM pg_user`
```sql
-- 查看所有用户列表
SELECT usename, usesuper FROM pg_user;
```

---

## 角色管理

**单行写法：创建角色**
`CREATE ROLE <角色名>`
```sql
-- 创建角色
CREATE ROLE readonly;
```

**单行写法：创建带属性的角色**
`CREATE ROLE <角色名> WITH <属性>`
```sql
-- 创建带登录和创建数据库属性的角色
CREATE ROLE admin WITH LOGIN CREATEDB CREATEROLE;
```

**单行写法：将角色分配给用户**
`GRANT <角色名> TO <用户名>`
```sql
-- 分配角色给用户
GRANT readonly TO app_user;
```

**单行写法：撤销用户角色**
`REVOKE <角色名> FROM <用户名>`
```sql
-- 撤销用户的角色
REVOKE readonly FROM app_user;
```

**单行写法：删除角色**
`DROP ROLE [IF EXISTS] <角色名>`
```sql
-- 删除角色
DROP ROLE IF EXISTS readonly;
```

**单行写法：查看所有角色**
`SELECT <列名> FROM pg_roles`
```sql
-- 查看所有角色
SELECT rolname, rolsuper, rolcreaterole FROM pg_roles;
```

---

## 权限管理

**单行写法：授予连接数据库权限**
`GRANT CONNECT ON DATABASE <库名> TO <角色名>`
```sql
-- 授予连接数据库权限
GRANT CONNECT ON DATABASE mydb TO readonly;
```

**单行写法：授予使用模式权限**
`GRANT USAGE ON SCHEMA <模式名> TO <角色名>`
```sql
-- 授予使用模式权限
GRANT USAGE ON SCHEMA public TO readonly;
```

**单行写法：授予表查询权限**
`GRANT SELECT ON <表名> TO <角色名>`
```sql
-- 授予表查询权限
GRANT SELECT ON users TO readonly;
```

**单行写法：授予表所有权限**
`GRANT ALL ON <表名> TO <角色名>`
```sql
-- 授予表所有权限
GRANT ALL ON users TO admin;
```

**单行写法：授予模式所有表查询权限**
`GRANT SELECT ON ALL TABLES IN SCHEMA <模式名> TO <角色名>`
```sql
-- 授予模式所有表查询权限
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```

**单行写法：授予模式所有表所有权限**
`GRANT ALL ON ALL TABLES IN SCHEMA <模式名> TO <角色名>`
```sql
-- 授予模式所有表所有权限
GRANT ALL ON ALL TABLES IN SCHEMA public TO admin;
```

**单行写法：授予序列使用权限**
`GRANT USAGE ON SEQUENCE <序列名> TO <角色名>`
```sql
-- 授予序列使用权限
GRANT USAGE ON SEQUENCE users_id_seq TO app_user;
```

**单行写法：撤销表查询权限**
`REVOKE SELECT ON <表名> FROM <角色名>`
```sql
-- 撤销表查询权限
REVOKE SELECT ON users FROM readonly;
```

**单行写法：撤销表所有权限**
`REVOKE ALL ON <表名> FROM <角色名>`
```sql
-- 撤销表所有权限
REVOKE ALL ON users FROM readonly;
```

**单行写法：修改默认权限**
`ALTER DEFAULT PRIVILEGES IN SCHEMA <模式名> GRANT SELECT ON TABLES TO <角色名>`
```sql
-- 设置未来创建表的默认权限
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;
```

---

## 默认角色

**单行写法：设置用户默认角色**
`SET ROLE <角色名>`
```sql
-- 切换当前会话角色
SET ROLE readonly;
```

**单行写法：重置为原始角色**
`RESET ROLE`
```sql
-- 重置为原始用户
RESET ROLE;
```

**单行写法：设置默认搜索路径**
`ALTER ROLE <角色名> SET search_path TO <模式名>`
```sql
-- 设置角色的默认搜索路径
ALTER ROLE app_user SET search_path TO myschema, public;
```

---

## 权限查看

**单行写法：查看表权限**
`\dp <表名>`
```sql
-- 查看表的权限信息
\dp users;
```

**单行写法：查看角色权限**
`SELECT <列名> FROM information_schema.role_table_grants WHERE <条件>`
```sql
-- 查看角色表权限
SELECT grantee, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE table_name = 'users';
```

**单行写法：查看用户权限**
`\du <用户名>`
```sql
-- 查看用户角色和属性
\du app_user;
```

**单行写法：查看数据库权限**
`SELECT <列名> FROM pg_database WHERE <条件>`
```sql
-- 查看数据库权限信息
SELECT datname, datacl FROM pg_database WHERE datname = 'mydb';
```



<!-- ============ 文档分隔线：021-postgresql/006-TransactionConcurrencyControl.md ============ -->

# PostgreSQL 事务与并发控制

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事务控制

**单行写法：开启事务**
`BEGIN` / `BEGIN TRANSACTION`
```sql
-- 开启事务
BEGIN;
```

**换行写法：提交事务**
`COMMIT` / `END`
```sql
-- 提交事务并持久化变更
BEGIN;
INSERT INTO users (username, email) VALUES ('张三', 'zhangsan@example.com');
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK` / `ABORT`
```sql
-- 回滚事务撤销变更
ROLLBACK;
```

**换行写法：使用保存点**
`SAVEPOINT <保存点名>` / `ROLLBACK TO <保存点名>`
```sql
-- 使用保存点部分回滚
BEGIN;
INSERT INTO users (username) VALUES ('张三');
SAVEPOINT sp1;
INSERT INTO users (username) VALUES ('李四');
ROLLBACK TO sp1;
COMMIT;
```

**单行写法：释放保存点**
`RELEASE SAVEPOINT <保存点名>`
```sql
-- 释放指定保存点
RELEASE SAVEPOINT sp1;
```

---

## 隔离级别

**单行写法：查看当前隔离级别**
`SHOW transaction_isolation`
```sql
-- 查看当前事务隔离级别
SHOW transaction_isolation;
```

**换行写法：设置会话隔离级别**
`SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**换行写法：设置事务隔离级别**
`SET TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置当前事务隔离级别为可序列化
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM users;
COMMIT;
```

**单行写法：设置默认隔离级别**
`ALTER DATABASE <库名> SET default_transaction_isolation TO '<级别>'`
```sql
-- 设置数据库默认隔离级别
ALTER DATABASE mydb SET default_transaction_isolation TO 'read committed';
```

---

## 锁机制

**单行写法：加共享锁**
`SELECT ... FOR SHARE`
```sql
-- 查询时加共享锁
SELECT * FROM users WHERE id = 1 FOR SHARE;
```

**单行写法：加排他锁**
`SELECT ... FOR UPDATE`
```sql
-- 查询时加排他锁
SELECT * FROM users WHERE id = 1 FOR UPDATE;
```

**单行写法：加无等待排他锁**
`SELECT ... FOR UPDATE NOWAIT`
```sql
-- 查询时加排他锁不等待
SELECT * FROM users WHERE id = 1 FOR UPDATE NOWAIT;
```

**换行写法：加跳过锁定排他锁**
`SELECT ... FOR UPDATE SKIP LOCKED`
```sql
-- 查询时加排他锁并跳过已锁定行
SELECT * FROM job_queue WHERE status = 'pending'
    FOR UPDATE SKIP LOCKED LIMIT 10;
```

**单行写法：INSERT 自动加排他锁**
`INSERT INTO <表名> (<列名>) VALUES (<值>)`
```sql
-- 插入操作自动加排他锁
INSERT INTO users (name) VALUES ('John');
```

**单行写法：UPDATE 自动加排他锁**
`UPDATE <表名> SET <列名> = <值> WHERE <条件>`
```sql
-- 更新操作自动加排他锁
UPDATE users SET name = 'John' WHERE id = 1;
```

**单行写法：DELETE 自动加排他锁**
`DELETE FROM <表名> WHERE <条件>`
```sql
-- 删除操作自动加排他锁
DELETE FROM users WHERE id = 1;
```

---

## 锁等待与超时

**单行写法：查看锁等待超时**
`SHOW lock_timeout`
```sql
-- 查看锁等待超时时间
SHOW lock_timeout;
```

**单行写法：设置锁等待超时**
`SET lock_timeout = '<时间>'`
```sql
-- 设置锁等待超时为 5 秒
SET lock_timeout = '5s';
```

**单行写法：查看死锁超时**
`SHOW deadlock_timeout`
```sql
-- 查看死锁检测超时
SHOW deadlock_timeout;
```

**单行写法：设置死锁超时**
`SET deadlock_timeout = '<时间>'`
```sql
-- 设置死锁检测超时为 100 毫秒
SET deadlock_timeout = '100ms';
```

---

## 死锁检测

**单行写法：查看锁信息**
`SELECT <列名> FROM pg_locks WHERE <条件>`
```sql
-- 查看当前锁信息
SELECT locktype, relation::regclass, mode, pid
FROM pg_locks WHERE granted = false;
```

**单行写法：查看阻塞进程**
`SELECT <列名> FROM pg_stat_activity WHERE <条件>`
```sql
-- 查看阻塞的进程
SELECT pid, usename, query, state, wait_event
FROM pg_stat_activity WHERE state = 'active';
```

**单行写法：终止进程**
`SELECT pg_terminate_backend(<PID>)`
```sql
-- 终止指定进程
SELECT pg_terminate_backend(12345);
```

**单行写法：取消进程查询**
`SELECT pg_cancel_backend(<PID>)`
```sql
-- 取消指定进程的查询
SELECT pg_cancel_backend(12345);
```

---

## 事务实战

**换行写法：转账事务**
`BEGIN; <DML>; COMMIT;`
```sql
-- 转账事务保证原子性
BEGIN;
UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;
COMMIT;
```

**换行写法：条件提交**
`IF <条件> THEN COMMIT; ELSE ROLLBACK; END IF`
```sql
-- 检查余额后决定提交或回滚
BEGIN;
UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;
DO $$
BEGIN
    IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
        RAISE EXCEPTION '余额不足';
    END IF;
END $$;
COMMIT;
```

**换行写法：订单创建事务**
`BEGIN; <DML>; COMMIT;`
```sql
-- 订单创建事务包含订单和订单项
BEGIN;
INSERT INTO orders (user_id, total_amount) VALUES (1, 500) RETURNING id;
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
    (1, 101, 2, 200),
    (1, 102, 1, 100);
UPDATE products SET stock = stock - 3 WHERE id IN (101, 102);
COMMIT;
```

**换行写法：悲观锁查询**
`SELECT ... FOR UPDATE`
```sql
-- 先锁定再更新
BEGIN;
SELECT * FROM users WHERE id = 1 FOR UPDATE;
UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
COMMIT;
```

**换行写法：批量删除事务**
`BEGIN; <DML>; COMMIT;`
```sql
-- 批量更新避免长事务
BEGIN;
UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
UPDATE stats SET inactive_users = inactive_users + 1;
COMMIT;
```

**换行写法：分批删除**
`DELETE FROM <表名> WHERE id IN (SELECT id FROM <表名> WHERE <条件> LIMIT <N>)`
```sql
-- 分批删除避免锁表
DELETE FROM logs WHERE id IN (
    SELECT id FROM logs WHERE created_at < '2023-01-01' LIMIT 1000
);
```

---

## 并发问题

**换行写法：使用 SELECT FOR UPDATE 防止丢失更新**
`SELECT ... FOR UPDATE`
```sql
-- 先锁定行再更新防止丢失更新
BEGIN;
SELECT balance FROM accounts WHERE user_id = 1 FOR UPDATE;
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
COMMIT;
```

**换行写法：使用乐观锁防止丢失更新**
`UPDATE <表名> SET <列名> = <值>, version = version + 1 WHERE id = <值> AND version = <版本>`
```sql
-- 使用版本号实现乐观锁
UPDATE products SET stock = stock - 1, version = version + 1
WHERE id = 1 AND version = 10;
```

**换行写法：使用 SERIALIZABLE 防止幻读**
`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE`
```sql
-- 使用可序列化隔离级别防止幻读
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT COUNT(*) FROM orders WHERE user_id = 1;
INSERT INTO orders (user_id, amount) VALUES (1, 100);
COMMIT;
```



<!-- ============ 文档分隔线：021-postgresql/007-IndexType.md ============ -->

# PostgreSQL 索引类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## B-Tree 索引

**单行写法：创建单列 B-Tree 索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为用户名列创建 B-Tree 索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合 B-Tree 索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为用户名和状态列创建复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建唯一 B-Tree 索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为邮箱列创建唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

---

## Hash 索引

**单行写法：创建 Hash 索引**
`CREATE INDEX <索引名> ON <表名> USING HASH (<列名>)`
```sql
-- 为用户 ID 创建 Hash 索引
CREATE INDEX idx_user_id_hash ON users USING HASH (user_id);
```

---

## GiST 索引

**单行写法：创建 GiST 索引**
`CREATE INDEX <索引名> ON <表名> USING GIST (<列名>)`
```sql
-- 为地理位置列创建 GiST 索引
CREATE INDEX idx_location ON places USING GIST (location);
```

**单行写法：创建 GiST 范围索引**
`CREATE INDEX <索引名> ON <表名> USING GIST (<范围列>)`
```sql
-- 为时间范围列创建 GiST 索引
CREATE INDEX idx_time_range ON schedules USING GIST (time_range);
```

---

## GIN 索引

**单行写法：创建 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<列名>)`
```sql
-- 为 JSONB 列创建 GIN 索引
CREATE INDEX idx_tags ON articles USING GIN (tags);
```

**单行写法：创建 JSONB 路径 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<列名> jsonb_path_ops)`
```sql
-- 为 JSONB 列创建路径操作符 GIN 索引
CREATE INDEX idx_profile ON users USING GIN (profile jsonb_path_ops);
```

**单行写法：创建数组 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<数组列>)`
```sql
-- 为数组列创建 GIN 索引
CREATE INDEX idx_tags_array ON posts USING GIN (tags);
```

---

## BRIN 索引

**单行写法：创建 BRIN 索引**
`CREATE INDEX <索引名> ON <表名> USING BRIN (<列名>)`
```sql
-- 为时间戳列创建 BRIN 索引
CREATE INDEX idx_created ON logs USING BRIN (created_at);
```

**单行写法：指定 BRIN 块大小**
`CREATE INDEX <索引名> ON <表名> USING BRIN (<列名>) WITH (pages_per_range = <数量>)`
```sql
-- 指定 BRIN 块范围大小
CREATE INDEX idx_created ON logs USING BRIN (created_at) WITH (pages_per_range = 128);
```

---

## 部分索引

**换行写法：创建部分索引**
`CREATE INDEX <索引名> ON <表名>(<列名>) WHERE <条件>`
```sql
-- 仅为活跃用户创建索引
CREATE INDEX idx_active_users ON users(username) WHERE status = 1;
```

---

## 表达式索引

**换行写法：创建表达式索引**
`CREATE INDEX <索引名> ON <表名>(<表达式>)`
```sql
-- 为小写邮箱创建表达式索引
CREATE INDEX idx_email_lower ON users(LOWER(email));
```

**换行写法：创建函数表达式索引**
`CREATE INDEX <索引名> ON <表名>(<函数>(<列名>))`
```sql
-- 为日期提取创建表达式索引
CREATE INDEX idx_created_date ON orders(DATE(created_at));
```

---

## 索引管理

**单行写法：查看表索引**
`SELECT <列名> FROM pg_indexes WHERE <条件>`
```sql
-- 查看表的索引信息
SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'users';
```

**单行写法：查看索引大小**
`SELECT pg_size_pretty(pg_relation_size('<索引名>'))`
```sql
-- 查看索引占用空间
SELECT pg_size_pretty(pg_relation_size('idx_username'));
```

**单行写法：删除索引**
`DROP INDEX [IF EXISTS] <索引名>`
```sql
-- 删除索引
DROP INDEX IF EXISTS idx_username;
```

**单行写法：CONCURRENTLY 创建索引**
`CREATE INDEX CONCURRENTLY <索引名> ON <表名>(<列名>)`
```sql
-- 并发创建索引不阻塞写入
CREATE INDEX CONCURRENTLY idx_email ON users(email);
```

**单行写法：CONCURRENTLY 删除索引**
`DROP INDEX CONCURRENTLY <索引名>`
```sql
-- 并发删除索引不阻塞写入
DROP INDEX CONCURRENTLY idx_email;
```

**单行写法：重建索引**
`REINDEX INDEX <索引名>`
```sql
-- 重建索引
REINDEX INDEX idx_username;
```

**单行写法：重建表所有索引**
`REINDEX TABLE <表名>`
```sql
-- 重建表的所有索引
REINDEX TABLE users;
```

**单行写法：查看索引使用情况**
`SELECT <列名> FROM pg_stat_user_indexes WHERE <条件>`
```sql
-- 查看索引使用统计
SELECT indexrelname, idx_scan, idx_tup_read
FROM pg_stat_user_indexes
WHERE relname = 'users';
```



<!-- ============ 文档分隔线：021-postgresql/008-SequenceAutoIncrement.md ============ -->

# PostgreSQL 序列与自增列

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SERIAL 与 IDENTITY

**换行写法：使用 SERIAL 创建自增列**
`<列名> SERIAL [PRIMARY KEY]`
```sql
-- 使用 SERIAL 创建自增主键
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);
```

**换行写法：使用 BIGSERIAL 创建自增列**
`<列名> BIGSERIAL [PRIMARY KEY]`
```sql
-- 使用 BIGSERIAL 创建大范围自增主键
CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    order_no VARCHAR(32) NOT NULL
);
```

**换行写法：使用 IDENTITY 创建自增列**
`<列名> INT GENERATED ALWAYS AS IDENTITY [PRIMARY KEY]`
```sql
-- 使用 IDENTITY 创建自增主键
CREATE TABLE products (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

**换行写法：使用 BY DEFAULT IDENTITY**
`<列名> INT GENERATED BY DEFAULT AS IDENTITY`
```sql
-- 使用 BY DEFAULT 允许手动指定值
CREATE TABLE products (
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

---

## 序列创建与使用

**换行写法：创建序列**
`CREATE SEQUENCE <序列名> [START WITH <起始值>] [INCREMENT BY <步长>]`
```sql
-- 创建从 1000 开始的序列
CREATE SEQUENCE order_seq START WITH 1000 INCREMENT BY 1;
```

**单行写法：获取序列当前值**
`SELECT currval('<序列名>')`
```sql
-- 获取当前会话的序列当前值
SELECT currval('order_seq');
```

**单行写法：获取序列下一个值**
`SELECT nextval('<序列名>')`
```sql
-- 获取并递增序列值
SELECT nextval('order_seq');
```

**单行写法：设置序列值**
`SELECT setval('<序列名>', <值>)`
```sql
-- 设置序列的当前值
SELECT setval('order_seq', 2000);
```

**单行写法：设置序列值且不允许递增**
`SELECT setval('<序列名>', <值>, false)`
```sql
-- 设置序列值且下一次调用会递增
SELECT setval('order_seq', 2000, false);
```

**换行写法：INSERT 中使用序列**
`INSERT INTO <表名> (<列名>) VALUES (nextval('<序列名>'))`
```sql
-- 插入时使用序列生成值
INSERT INTO orders (id, order_no) VALUES (nextval('order_seq'), 'ORD001');
```

---

## 序列操作函数

**单行写法：lastval 获取最后值**
`SELECT lastval()`
```sql
-- 获取当前会话最后使用的序列值
SELECT lastval();
```

---

## 序列修改

**单行写法：修改序列起始值**
`ALTER SEQUENCE <序列名> START WITH <值>`
```sql
-- 修改序列起始值
ALTER SEQUENCE order_seq START WITH 100;
```

**单行写法：修改序列步长**
`ALTER SEQUENCE <序列名> INCREMENT BY <步长>`
```sql
-- 修改序列步长为 2
ALTER SEQUENCE order_seq INCREMENT BY 2;
```

**单行写法：修改序列最小值**
`ALTER SEQUENCE <序列名> MINVALUE <值>`
```sql
-- 修改序列最小值
ALTER SEQUENCE order_seq MINVALUE 1;
```

**单行写法：修改序列最大值**
`ALTER SEQUENCE <序列名> MAXVALUE <值>`
```sql
-- 修改序列最大值
ALTER SEQUENCE order_seq MAXVALUE 999999;
```

**单行写法：设置序列循环**
`ALTER SEQUENCE <序列名> CYCLE`
```sql
-- 设置序列循环
ALTER SEQUENCE order_seq CYCLE;
```

**单行写法：设置序列不循环**
`ALTER SEQUENCE <序列名> NO CYCLE`
```sql
-- 设置序列不循环
ALTER SEQUENCE order_seq NO CYCLE;
```

**单行写法：重置序列当前值**
`ALTER SEQUENCE <序列名> RESTART WITH <值>`
```sql
-- 重置序列从 1 开始
ALTER SEQUENCE order_seq RESTART WITH 1;
```

**单行写法：重置序列归属**
`ALTER SEQUENCE <序列名> OWNED BY <表名>.<列名>`
```sql
-- 将序列绑定到表的列
ALTER SEQUENCE order_seq OWNED BY orders.id;
```

---

## 序列删除

**单行写法：删除序列**
`DROP SEQUENCE [IF EXISTS] <序列名>`
```sql
-- 删除序列
DROP SEQUENCE IF EXISTS order_seq;
```

**单行写法：查看序列信息**
`SELECT <列名> FROM information_schema.sequences WHERE <条件>`
```sql
-- 查看序列的详细信息
SELECT sequence_name, start_value, increment, minimum_value, maximum_value
FROM information_schema.sequences
WHERE sequence_name = 'order_seq';
```

**单行写法：查看序列当前值**
`SELECT * FROM <序列名>`
```sql
-- 查看序列的参数
SELECT * FROM order_seq;
```



<!-- ============ 文档分隔线：021-postgresql/009-DDL.md ============ -->

# PostgreSQL DDL 数据定义

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数据库操作

**单行写法：创建数据库**
`CREATE DATABASE <库名>;`
```sql
-- 创建数据库
CREATE DATABASE mydb;
```

**换行写法：指定所有者与编码**
`CREATE DATABASE <库名> [OWNER <所有者>] [ENCODING '<编码>'] [LC_COLLATE '<排序>'] [LC_CTYPE '<类型>'] [TEMPLATE <模板>];`
```sql
-- 创建指定编码与所有者的数据库
CREATE DATABASE mydb
  OWNER appuser
  ENCODING 'UTF8'
  LC_COLLATE 'en_US.UTF-8'
  LC_CTYPE 'en_US.UTF-8'
  TEMPLATE template0;
```

**单行写法：删除数据库**
`DROP DATABASE [IF EXISTS] <库名>;`
```sql
-- 存在时才删除
DROP DATABASE IF EXISTS mydb;
```

**单行写法：切换数据库**
`\c <库名>`
```sql
-- 在 psql 中切换数据库
\c mydb
```

---

## Schema 模式

**单行写法：创建模式**
`CREATE SCHEMA [IF NOT EXISTS] <模式名> [AUTHORIZATION <用户>];`
```sql
-- 创建模式并指定所有者
CREATE SCHEMA IF NOT EXISTS app_schema AUTHORIZATION appuser;
```

**单行写法：删除模式**
`DROP SCHEMA [IF EXISTS] <模式名> [CASCADE];`
```sql
-- 级联删除模式及其所有对象
DROP SCHEMA IF EXISTS app_schema CASCADE;
```

**单行写法：设置搜索路径**
`SET search_path TO <模式1>, <模式2>, public;`
```sql
-- 设置模式搜索路径
SET search_path TO app_schema, public;
```

**单行写法：查看当前搜索路径**
`SHOW search_path;`
```sql
-- 查看当前搜索路径
SHOW search_path;
```

---

## 创建表

**换行写法：创建表（SERIAL 自增）**
`CREATE TABLE [IF NOT EXISTS] <表名> (<列定义>[, <表约束>...]);`
```sql
-- 创建用户表使用 SERIAL 自增
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL,
  age INT CHECK (age >= 0 AND age < 150),
  balance NUMERIC(10,2) DEFAULT 0.00,
  status SMALLINT DEFAULT 1,
  metadata JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

**换行写法：使用 IDENTITY 列（PG10+）**
`<列名> INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY`
```sql
-- 使用标准 IDENTITY 列替代 SERIAL
CREATE TABLE users (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  username TEXT NOT NULL
);
```

**换行写法：创建带外键的表**
`CREATE TABLE <表名> (<列定义>, FOREIGN KEY (<列>) REFERENCES <父表>(<列>) [ON DELETE <动作>]);`
```sql
-- 创建订单表带外键
CREATE TABLE orders (
  id BIGSERIAL PRIMARY KEY,
  order_no VARCHAR(32) UNIQUE NOT NULL,
  user_id INT NOT NULL,
  total_amount NUMERIC(10,2) NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE RESTRICT ON UPDATE CASCADE
);
```

**单行写法：创建临时表**
`CREATE TEMP TABLE <表名> AS SELECT * FROM <源表> WHERE <条件>;`
```sql
-- 创建会话级临时表
CREATE TEMP TABLE temp_users AS SELECT * FROM users WHERE status = 1;
```

**单行写法：复制表结构**
`CREATE TABLE <新表> (LIKE <源表> [INCLUDING DEFAULTS] [INCLUDING CONSTRAINTS]);`
```sql
-- 完整复制表结构包含约束
CREATE TABLE users_copy (LIKE users INCLUDING ALL);
```

---

## 修改表

**单行写法：添加列**
`ALTER TABLE <表名> ADD COLUMN [IF NOT EXISTS] <列名> <类型> [<约束>];`
```sql
-- 添加新列
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
```

**单行写法：删除列**
`ALTER TABLE <表名> DROP COLUMN [IF EXISTS] <列名> [CASCADE];`
```sql
-- 级联删除列及其依赖对象
ALTER TABLE users DROP COLUMN IF EXISTS phone CASCADE;
```

**单行写法：修改列类型**
`ALTER TABLE <表名> ALTER COLUMN <列名> TYPE <新类型> [USING <转换表达式>];`
```sql
-- 修改列类型并指定转换
ALTER TABLE users ALTER COLUMN phone TYPE BIGINT USING phone::BIGINT;
```

**单行写法：设置列默认值**
`ALTER TABLE <表名> ALTER COLUMN <列名> SET DEFAULT <默认值>;`
```sql
-- 设置列默认值
ALTER TABLE users ALTER COLUMN status SET DEFAULT 1;
```

**单行写法：删除列默认值**
`ALTER TABLE <表名> ALTER COLUMN <列名> DROP DEFAULT;`
```sql
-- 删除列默认值
ALTER TABLE users ALTER COLUMN status DROP DEFAULT;
```

**单行写法：设置非空**
`ALTER TABLE <表名> ALTER COLUMN <列名> SET NOT NULL;`
```sql
-- 设置列为非空
ALTER TABLE users ALTER COLUMN email SET NOT NULL;
```

**单行写法：删除非空约束**
`ALTER TABLE <表名> ALTER COLUMN <列名> DROP NOT NULL;`
```sql
-- 取消非空约束
ALTER TABLE users ALTER COLUMN email DROP NOT NULL;
```

**单行写法：重命名列**
`ALTER TABLE <表名> RENAME COLUMN <旧名> TO <新名>;`
```sql
-- 重命名列
ALTER TABLE users RENAME COLUMN phone TO telephone;
```

**单行写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>;`
```sql
-- 重命名表
ALTER TABLE users RENAME TO user_info;
```

---

## 约束管理

**单行写法：添加主键**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> PRIMARY KEY (<列>);`
```sql
-- 添加主键约束
ALTER TABLE users ADD CONSTRAINT pk_users PRIMARY KEY (id);
```

**单行写法：添加唯一约束**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> UNIQUE (<列>);`
```sql
-- 添加唯一约束
ALTER TABLE users ADD CONSTRAINT uk_email UNIQUE (email);
```

**单行写法：添加 CHECK 约束**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> CHECK (<条件>);`
```sql
-- 添加检查约束
ALTER TABLE users ADD CONSTRAINT chk_age CHECK (age >= 0);
```

**单行写法：添加外键**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> FOREIGN KEY (<列>) REFERENCES <父表>(<列>) ON DELETE <动作>;`
```sql
-- 添加外键约束
ALTER TABLE orders ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
```

**单行写法：删除约束**
`ALTER TABLE <表名> DROP CONSTRAINT [IF EXISTS] <约束名> [CASCADE];`
```sql
-- 删除约束
ALTER TABLE users DROP CONSTRAINT IF EXISTS uk_email;
```

---

## 删除与清空

**单行写法：删除表**
`DROP TABLE [IF EXISTS] <表名>[, <表名>...] [CASCADE];`
```sql
-- 级联删除多个表
DROP TABLE IF EXISTS users, orders CASCADE;
```

**单行写法：清空表数据**
`TRUNCATE [TABLE] <表名>[, <表名>...] [RESTART IDENTITY] [CASCADE];`
```sql
-- 清空表并重置自增序列
TRUNCATE TABLE users RESTART IDENTITY CASCADE;
```

**单行写法：清空并级联**
`TRUNCATE <表1>, <表2> CASCADE;`
```sql
-- 同时清空有外键关联的表
TRUNCATE users, orders CASCADE;
```

---

## 视图

**换行写法：创建视图**
`CREATE [OR REPLACE] VIEW <视图名> AS <SELECT 语句>;`
```sql
-- 创建或替换视图
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email FROM users WHERE status = 1;
```

**换行写法：创建物化视图**
`CREATE MATERIALIZED VIEW <视图名> AS <SELECT 语句> [WITH DATA | WITH NO DATA];`
```sql
-- 创建物化视图缓存结果
CREATE MATERIALIZED VIEW user_stats AS
SELECT user_id, COUNT(*) AS order_count FROM orders GROUP BY user_id;
```

**单行写法：刷新物化视图**
`REFRESH MATERIALIZED VIEW [CONCURRENTLY] <视图名>;`
```sql
-- 并发刷新物化视图不阻塞查询
REFRESH MATERIALIZED VIEW CONCURRENTLY user_stats;
```

**单行写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名> [CASCADE];`
```sql
-- 删除视图
DROP VIEW IF EXISTS active_users;
```

**单行写法：删除物化视图**
`DROP MATERIALIZED VIEW [IF EXISTS] <视图名>;`
```sql
-- 删除物化视图
DROP MATERIALIZED VIEW IF EXISTS user_stats;
```

---

## 序列

**单行写法：创建序列**
`CREATE SEQUENCE [IF NOT EXISTS] <序列名> [START WITH <起始>] [INCREMENT BY <步长>] [MINVALUE <最小>] [MAXVALUE <最大>] [CACHE <缓存>] [CYCLE | NO CYCLE];`
```sql
-- 创建自定义序列
CREATE SEQUENCE seq_order_no START 1000 INCREMENT 1 CACHE 10;
```

**单行写法：获取下一个值**
`SELECT nextval('<序列名>');`
```sql
-- 获取序列下一个值
SELECT nextval('seq_order_no');
```

**单行写法：查看当前值**
`SELECT currval('<序列名>');`
```sql
-- 查看当前会话最近获取的值
SELECT currval('seq_order_no');
```

**单行写法：查看最后值**
`SELECT last_value FROM <序列名>;`
```sql
-- 查看序列当前最后值
SELECT last_value FROM seq_order_no;
```

**单行写法：重置序列**
`ALTER SEQUENCE <序列名> RESTART WITH <值>;`
```sql
-- 重置序列从指定值开始
ALTER SEQUENCE seq_order_no RESTART WITH 1;
```

**单行写法：删除序列**
`DROP SEQUENCE [IF EXISTS] <序列名>;`
```sql
-- 删除序列
DROP SEQUENCE IF EXISTS seq_order_no;
```



<!-- ============ 文档分隔线：021-postgresql/010-DML.md ============ -->

# PostgreSQL DML 数据操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## INSERT 插入

**单行写法：插入单行**
`INSERT INTO <表名> (<列1>, <列2>) VALUES (<值1>, <值2>);`
```sql
-- 插入一条用户记录
INSERT INTO users (username, email, age) VALUES ('zhangsan', 'zs@example.com', 25);
```

**换行写法：插入多行**
`INSERT INTO <表名> (<列>) VALUES (<值1>), (<值2>), (<值3>);`
```sql
-- 批量插入多行
INSERT INTO users (username, email) VALUES
  ('user1', 'u1@example.com'),
  ('user2', 'u2@example.com'),
  ('user3', 'u3@example.com');
```

**单行写法：插入查询结果**
`INSERT INTO <目标表> SELECT * FROM <源表> [WHERE <条件>];`
```sql
-- 将活跃用户插入备份表
INSERT INTO active_users_backup SELECT * FROM users WHERE status = 1;
```

**换行写法：ON CONFLICT 冲突处理（upsert）**
`INSERT INTO <表名> (<列>) VALUES (<值>) ON CONFLICT (<列>) DO UPDATE SET <列>=<值>;`
```sql
-- 冲突时更新
INSERT INTO users (id, username, email) VALUES (1, 'zhangsan', 'new@example.com')
ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, updated_at = NOW();
```

**单行写法：冲突时什么都不做**
`INSERT INTO <表名> (<列>) VALUES (<值>) ON CONFLICT (<列>) DO NOTHING;`
```sql
-- 冲突时忽略
INSERT INTO users (id, username) VALUES (1, 'zhangsan') ON CONFLICT (id) DO NOTHING;
```

**换行写法：RETURNING 返回数据**
`INSERT INTO <表名> (<列>) VALUES (<值>) RETURNING <列>;`
```sql
-- 插入并返回自增ID
INSERT INTO users (username, email) VALUES ('zhangsan', 'zs@example.com')
RETURNING id, username;
```

**换行写法：RETURNING 返回所有列**
`INSERT INTO <表名> (<列>) VALUES (<值>) RETURNING *;`
```sql
-- 插入并返回所有列
INSERT INTO users (username, email) VALUES ('zhangsan', 'zs@example.com')
RETURNING *;
```

---

## UPDATE 更新

**单行写法：更新单列**
`UPDATE <表名> SET <列>=<值> WHERE <条件>;`
```sql
-- 更新指定用户年龄
UPDATE users SET age = 26 WHERE id = 1;
```

**单行写法：更新多列**
`UPDATE <表名> SET <列1>=<值1>, <列2>=<值2> WHERE <条件>;`
```sql
-- 同时更新多个字段
UPDATE users SET age = 26, status = 2 WHERE id = 1;
```

**单行写法：基于表达式更新**
`UPDATE <表名> SET <列>=<表达式> WHERE <条件>;`
```sql
-- 所有用户余额增加 10%
UPDATE users SET balance = balance * 1.10 WHERE status = 1;
```

**换行写法：基于 FROM 关联更新**
`UPDATE <表1> SET <列>=<值> FROM <表2> WHERE <连接条件>;`
```sql
-- 关联订单汇总表更新用户余额
UPDATE users SET balance = balance - o.total
FROM (SELECT user_id, SUM(total_amount) AS total FROM orders GROUP BY user_id) o
WHERE users.id = o.user_id;
```

**换行写法：RETURNING 返回更新后数据**
`UPDATE <表名> SET <列>=<值> WHERE <条件> RETURNING <列>;`
```sql
-- 更新并返回更新后的数据
UPDATE users SET status = 0 WHERE last_login < '2024-01-01'
RETURNING id, username, status;
```

**换行写法：使用 CASE 条件更新**
`UPDATE <表名> SET <列> = CASE WHEN <条件> THEN <值> ELSE <默认> END WHERE <条件>;`
```sql
-- 根据不同状态批量更新
UPDATE users SET status = CASE
  WHEN age < 18 THEN 1
  WHEN age >= 60 THEN 3
  ELSE 2
END WHERE age IS NOT NULL;
```

---

## DELETE 删除

**单行写法：按条件删除**
`DELETE FROM <表名> WHERE <条件>;`
```sql
-- 删除指定用户
DELETE FROM users WHERE id = 1;
```

**换行写法：基于 USING 关联删除**
`DELETE FROM <表1> USING <表2> WHERE <连接条件>;`
```sql
-- 删除没有订单的用户
DELETE FROM users
USING orders
WHERE users.id = orders.user_id;
```

**换行写法：基于子查询删除**
`DELETE FROM <表名> WHERE <列> IN (SELECT <列> FROM <表名> WHERE <条件>);`
```sql
-- 删除符合条件的关联数据
DELETE FROM orders WHERE user_id IN (SELECT id FROM users WHERE status = 0);
```

**换行写法：RETURNING 返回删除数据**
`DELETE FROM <表名> WHERE <条件> RETURNING <列>;`
```sql
-- 删除并返回被删除的记录
DELETE FROM users WHERE status = 0 RETURNING id, username;
```

**单行写法：删除所有数据**
`DELETE FROM <表名>;`
```sql
-- 删除全表数据
DELETE FROM logs;
```

---

## UPSERT 操作

**换行写法：基于主键冲突更新**
`INSERT INTO <表> (<列>) VALUES (<值>) ON CONFLICT ON CONSTRAINT <约束名> DO UPDATE SET <列>=EXCLUDED.<列>;`
```sql
-- 基于约束名冲突更新
INSERT INTO users (id, username) VALUES (1, 'newname')
ON CONFLICT ON CONSTRAINT users_pkey DO UPDATE SET username = EXCLUDED.username;
```

**换行写法：基于多列冲突更新**
`INSERT INTO <表> (<列>) VALUES (<值>) ON CONFLICT (<列1>, <列2>) DO UPDATE SET <列>=<值>;`
```sql
-- 复合唯一键冲突时更新
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (1, 100, 5)
ON CONFLICT (order_id, product_id) DO UPDATE SET quantity = order_items.quantity + EXCLUDED.quantity;
```

---

## MERGE 命令（PG15+）

**换行写法：MERGE 条件合并**
`MERGE INTO <目标表> USING <源> ON <条件> WHEN MATCHED THEN UPDATE SET ... WHEN NOT MATCHED THEN INSERT ...;`
```sql
-- 条件插入或更新
MERGE INTO users AS target
USING (SELECT 1 AS id, 'zhangsan' AS username, 'zs@example.com' AS email) AS source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET email = source.email
WHEN NOT MATCHED THEN INSERT (id, username, email) VALUES (source.id, source.username, source.email);
```

**换行写法：MERGE 带删除（PG17+）**
`MERGE INTO <目标表> USING <源> ON <条件> WHEN MATCHED AND <条件> THEN DELETE;`
```sql
-- 匹配且满足条件时删除
MERGE INTO users AS t USING inactive_users AS s ON t.id = s.id
WHEN MATCHED AND t.status = 0 THEN DELETE;
```

---

## 事务控制

**单行写法：开启事务**
`BEGIN;` 或 `START TRANSACTION;`
```sql
-- 开启事务
BEGIN;
```

**换行写法：提交事务**
`COMMIT;`
```sql
-- 提交事务
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK;`
```sql
-- 回滚事务
ROLLBACK;
```

**单行写法：设置保存点**
`SAVEPOINT <保存点名>;`
```sql
-- 设置保存点
SAVEPOINT sp1;
```

**单行写法：回滚到保存点**
`ROLLBACK TO <保存点名>;`
```sql
-- 回滚到指定保存点
ROLLBACK TO sp1;
```

**单行写法：查看隔离级别**
`SHOW transaction_isolation;`
```sql
-- 查看当前事务隔离级别
SHOW transaction_isolation;
```

**单行写法：设置隔离级别**
`SET TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- 设置事务隔离级别为可重复读
BEGIN;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```



<!-- ============ 文档分隔线：021-postgresql/011-JSON.md ============ -->

# PostgreSQL JSON/JSONB 操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建与插入

**单行写法：创建 JSONB 列**
`<列名> JSONB`
```sql
-- 创建带 JSONB 列的表
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  attributes JSONB
);
```

**单行写法：插入 JSON 数据**
`INSERT INTO <表名> (<列>) VALUES ('<JSON字符串>'::jsonb);`
```sql
-- 插入 JSONB 数据
INSERT INTO products (name, attributes)
VALUES ('手机', '{"品牌": "Xiaomi", "价格": 2999, "颜色": "黑色"}'::jsonb);
```

**单行写法：使用 JSON 构造函数（PG17+）**
`INSERT INTO <表名> (<列>) VALUES (JSON_OBJECT('key', 'value'));`
```sql
-- 使用 SQL 标准 JSON 构造函数
INSERT INTO products (name, attributes)
VALUES ('手机', JSON_OBJECT('品牌', 'Xiaomi', '价格', 2999));
```

**单行写法：插入 JSON 数组**
`INSERT INTO <表名> (<列>) VALUES ('[1, 2, 3]'::jsonb);`
```sql
-- 插入 JSON 数组
INSERT INTO logs (tags) VALUES ('["redis", "mysql", "pg"]'::jsonb);
```

---

## 查询操作

**单行写法：使用 -> 获取 JSON 对象字段**
`SELECT <列>->'<键>' FROM <表名>;`
```sql
-- 获取 JSON 对象字段（返回 JSONB）
SELECT attributes->'品牌' AS brand FROM products;
```

**单行写法：使用 ->> 获取文本值**
`SELECT <列>->>'<键>' FROM <表名>;`
```sql
-- 获取 JSON 字段文本值（返回 TEXT）
SELECT attributes->>'品牌' AS brand FROM products;
```

**单行写法：路径访问嵌套字段**
`SELECT <列>#>'{<路径1>, <路径2>}' FROM <表名>;`
```sql
-- 按路径获取嵌套 JSONB 值
SELECT attributes#>'{地址, 城市}' AS city FROM users;
```

**单行写法：路径访问文本**
`SELECT <列>#>>'{<路径1>, <路径2>}' FROM <表名>;`
```sql
-- 按路径获取嵌套字段文本值
SELECT attributes#>>'{地址, 城市}' AS city FROM users;
```

**单行写法：获取数组元素**
`SELECT <列>-><索引> FROM <表名>;`
```sql
-- 获取 JSON 数组指定索引元素
SELECT tags->0 AS first_tag FROM logs;
```

---

## 条件查询

**单行写法：按 JSON 字段过滤**
`SELECT * FROM <表名> WHERE <列>->>'<键>' = '<值>';`
```sql
-- 查询品牌为 Xiaomi 的商品
SELECT * FROM products WHERE attributes->>'品牌' = 'Xiaomi';
```

**单行写法：使用 @> 包含操作符**
`SELECT * FROM <表名> WHERE <列> @> '<JSON对象>';`
```sql
-- 查询包含指定键值对的记录
SELECT * FROM products WHERE attributes @> '{"品牌": "Xiaomi"}';
```

**单行写法：使用 ? 键存在判断**
`SELECT * FROM <表名> WHERE <列> ? '<键>';`
```sql
-- 查询存在指定键的记录
SELECT * FROM products WHERE attributes ? '价格';
```

**单行写法：使用 ?| 任一键存在**
`SELECT * FROM <表名> WHERE <列> ?| ARRAY['<键1>', '<键2>'];`
```sql
-- 查询存在任一键的记录
SELECT * FROM products WHERE attributes ?| ARRAY['价格', '库存'];
```

**单行写法：使用 ?& 所有关键存在**
`SELECT * FROM <表名> WHERE <列> ?& ARRAY['<键1>', '<键2>'];`
```sql
-- 查询同时存在多个键的记录
SELECT * FROM products WHERE attributes ?& ARRAY['价格', '库存'];
```

---

## 修改操作

**单行写法：合并 JSON 对象**
`SELECT <列> || '<JSON对象>' FROM <表名>;`
```sql
-- 合并两个 JSON 对象（后者覆盖前者）
UPDATE products SET attributes = attributes || '{"库存": 100}'::jsonb WHERE id = 1;
```

**单行写法：删除键**
`SELECT <列> - '<键>' FROM <表名>;`
```sql
-- 删除 JSON 对象指定键
UPDATE products SET attributes = attributes - '颜色' WHERE id = 1;
```

**单行写法：删除多个键**
`SELECT <列> - '<键1>' - '<键2>' FROM <表名>;`
```sql
-- 删除多个键
UPDATE products SET attributes = attributes - '颜色' - '库存' WHERE id = 1;
```

**单行写法：按路径删除**
`SELECT <列> #- '{<路径>}' FROM <表名>;`
```sql
-- 按路径删除嵌套字段
UPDATE users SET attributes = attributes #- '{地址, 城市}' WHERE id = 1;
```

**单行写法：更新指定路径值**
`SELECT jsonb_set(<列>, '{<路径>}', '<新值>');`
```sql
-- 更新嵌套字段值
UPDATE users SET attributes = jsonb_set(attributes, '{地址, 城市}', '"北京"'::jsonb) WHERE id = 1;
```

**单行写法：设置值不存在时才插入**
`SELECT jsonb_set(<列>, '{<路径>}', '<新值>', true);`
```sql
-- 仅当键不存在时插入新值
UPDATE products SET attributes = jsonb_set(attributes, '{折扣}', '"0.9"'::jsonb, true) WHERE id = 1;
```

---

## 聚合与展开

**单行写法：JSON 聚合**
`SELECT json_agg(<列>) FROM <表名>;`
```sql
-- 将多行数据聚合成 JSON 数组
SELECT json_agg(username) AS usernames FROM users;
```

**单行写法：JSONB 聚合**
`SELECT jsonb_agg(<列>) FROM <表名>;`
```sql
-- 将多行聚合成 JSONB 数组
SELECT jsonb_agg(row_to_json(u)) AS users FROM users u;
```

**单行写法：构建 JSON 对象**
`SELECT json_build_object('<键>', <值>[, ...]);`
```sql
-- 构建键值对 JSON 对象
SELECT json_build_object('id', id, 'name', username) FROM users;
```

**单行写法：行转 JSON 对象**
`SELECT row_to_json(<表别名>) FROM <表名> <别名>;`
```sql
-- 将整行转为 JSON 对象
SELECT row_to_json(u) FROM users u WHERE id = 1;
```

**换行写法：展开 JSON 数组**
`SELECT * FROM jsonb_array_elements(<列>) AS <别名>;`
```sql
-- 将 JSON 数组展开为多行
SELECT * FROM jsonb_array_elements('["a", "b", "c"]'::jsonb) AS elem;
```

**换行写法：展开 JSON 对象**
`SELECT * FROM jsonb_each(<列>) AS <别名>(键, 值);`
```sql
-- 将 JSON 对象展开为键值对多行
SELECT * FROM jsonb_each('{"a": 1, "b": 2}'::jsonb) AS x(key, value);
```

---

## 索引与性能

**单行写法：创建 GIN 索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (<列>);`
```sql
-- 为 JSONB 列创建 GIN 索引
CREATE INDEX idx_products_attr ON products USING GIN (attributes);
```

**单行写法：创建表达式索引**
`CREATE INDEX <索引名> ON <表名> ((<列>->>'<键>'));`
```sql
-- 为 JSONB 某字段创建表达式索引
CREATE INDEX idx_products_brand ON products ((attributes->>'品牌'));
```

**单行写法：查看 JSONB 键**
`SELECT jsonb_object_keys(<列>) FROM <表名>;`
```sql
-- 获取 JSONB 对象所有键
SELECT jsonb_object_keys(attributes) FROM products WHERE id = 1;
```

---

## JSON_TABLE（PG17+）

**换行写法：JSON 数据转关系表**
`SELECT * FROM JSON_TABLE(<JSON>, '<路径>' COLUMNS (<列定义>));`
```sql
-- 将 JSON 数组转为关系表行
SELECT * FROM JSON_TABLE(
  '[{"name": "张三", "age": 25}, {"name": "李四", "age": 30}]'::jsonb,
  '$[*]' COLUMNS (
    name TEXT PATH '$.name',
    age INT PATH '$.age'
  )
);
```

**单行写法：JSON_EXISTS 判断路径存在**
`SELECT JSON_EXISTS(<JSON>, '<路径>');`
```sql
-- 判断 JSON 路径是否存在
SELECT JSON_EXISTS(attributes, '$.品牌') FROM products WHERE id = 1;
```

**单行写法：JSON_VALUE 提取标量**
`SELECT JSON_VALUE(<JSON>, '<路径>');`
```sql
-- 提取 JSON 标量值
SELECT JSON_VALUE(attributes, '$.价格') FROM products WHERE id = 1;
```

**单行写法：JSON_QUERY 提取对象**
`SELECT JSON_QUERY(<JSON>, '<路径>');`
```sql
-- 提取 JSON 对象或数组
SELECT JSON_QUERY(attributes, '$.地址') FROM users WHERE id = 1;
```



<!-- ============ 文档分隔线：021-postgresql/012-WindowFunction.md ============ -->

# PostgreSQL 窗口函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 排名函数

**换行写法：ROW_NUMBER 行号**
`ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列> [ASC|DESC])`
```sql
-- 部门内按薪资生成行号
SELECT name, dept_id, salary,
  ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num
FROM employees;
```

**换行写法：RANK 排名（带跳跃）**
`RANK() OVER (PARTITION BY <列> ORDER BY <列> [ASC|DESC])`
```sql
-- 部门内薪资排名（同值跳号）
SELECT name, dept_id, salary,
  RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank
FROM employees;
```

**换行写法：DENSE_RANK 密集排名**
`DENSE_RANK() OVER (PARTITION BY <列> ORDER BY <列> [ASC|DESC])`
```sql
-- 部门内薪资密集排名（同值不跳号）
SELECT name, dept_id, salary,
  DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank
FROM employees;
```

**换行写法：PERCENT_RANK 百分比排名**
`PERCENT_RANK() OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 计算百分比排名（0 到 1）
SELECT name, salary,
  PERCENT_RANK() OVER (ORDER BY salary DESC) AS pct_rank
FROM employees;
```

**换行写法：CUME_DIST 累积分布**
`CUME_DISTRIB() OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 计算累积分布比例
SELECT name, salary,
  CUME_DIST() OVER (ORDER BY salary ASC) AS cume_dist
FROM employees;
```

**换行写法：NTILE 分桶**
`NTILE(<桶数>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 将数据等分为 4 个桶
SELECT name, salary,
  NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

---

## 偏移函数

**换行写法：LAG 访问前一行**
`LAG(<列>[, <偏移量>[, <默认值>]]) OVER (ORDER BY <列>)`
```sql
-- 计算环比变化
SELECT order_date, amount,
  amount - LAG(amount) OVER (ORDER BY order_date) AS day_over_day
FROM daily_sales;
```

**换行写法：LEAD 访问后一行**
`LEAD(<列>[, <偏移量>[, <默认值>]]) OVER (ORDER BY <列>)`
```sql
-- 访问下一行金额
SELECT order_date, amount,
  LEAD(amount) OVER (ORDER BY order_date) AS next_day_amount
FROM daily_sales;
```

**换行写法：FIRST_VALUE 第一行值**
`FIRST_VALUE(<列>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 获取每个部门最低薪资
SELECT name, dept_id, salary,
  FIRST_VALUE(salary) OVER (PARTITION BY dept_id ORDER BY salary ASC) AS min_salary
FROM employees;
```

**换行写法：LAST_VALUE 末尾值**
`LAST_VALUE(<列>) OVER (PARTITION BY <列> ORDER BY <列> ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)`
```sql
-- 获取每个部门最高薪资
SELECT name, dept_id, salary,
  LAST_VALUE(salary) OVER (
    PARTITION BY dept_id ORDER BY salary
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS max_salary
FROM employees;
```

**换行写法：NTH_VALUE 第 N 行值**
`NTH_VALUE(<列>, <N>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 获取部门内第 2 高薪资
SELECT name, dept_id, salary,
  NTH_VALUE(salary, 2) OVER (PARTITION BY dept_id ORDER BY salary DESC) AS second_salary
FROM employees;
```

---

## 聚合窗口函数

**换行写法：累计求和**
`SUM(<列>) OVER (ORDER BY <列> ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`
```sql
-- 按日期累计求和
SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date) AS cumulative
FROM daily_sales;
```

**换行写法：移动平均**
`AVG(<列>) OVER (ORDER BY <列> ROWS BETWEEN <N> PRECEDING AND CURRENT ROW)`
```sql
-- 7 日移动平均
SELECT order_date, amount,
  AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM daily_sales;
```

**换行写法：分组累计求和**
`SUM(<列>) OVER (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 每个用户订单金额累计
SELECT user_id, order_date, amount,
  SUM(amount) OVER (PARTITION BY user_id ORDER BY order_date) AS cumulative
FROM orders;
```

**换行写法：分组占比**
`SELECT <列>, <列> / SUM(<列>) OVER (PARTITION BY <列>) AS ratio`
```sql
-- 计算每个用户订单金额占该用户总金额的比例
SELECT user_id, order_no, amount,
  amount / SUM(amount) OVER (PARTITION BY user_id) AS ratio
FROM orders;
```

**换行写法：累计计数**
`COUNT(<列>) OVER (ORDER BY <列>)`
```sql
-- 按日期累计计数
SELECT order_date,
  COUNT(*) OVER (ORDER BY order_date) AS cumulative_count
FROM orders;
```

---

## 窗口范围控制

**换行写法：ROWS 范围**
`<函数>() OVER (ORDER BY <列> ROWS BETWEEN <起> AND <止>)`
```sql
-- 指定行范围窗口
SELECT order_date, amount,
  AVG(amount) OVER (
    ORDER BY order_date
    ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
  ) AS window_avg
FROM daily_sales;
```

**换行写法：RANGE 范围**
`<函数>() OVER (ORDER BY <列> RANGE BETWEEN <起> AND <止>)`
```sql
-- 按值范围窗口
SELECT order_date, amount,
  SUM(amount) OVER (
    ORDER BY order_date
    RANGE BETWEEN INTERVAL '7' DAY PRECEDING AND CURRENT ROW
  ) AS weekly_sum
FROM daily_sales;
```

**换行写法：UNBOUNDED 无界限**
`<函数>() OVER (ORDER BY <列> ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)`
```sql
-- 整个分区作为窗口
SELECT name, salary,
  AVG(salary) OVER (
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) AS overall_avg
FROM employees;
```

---

## FILTER 条件聚合

**换行写法：FILTER 条件聚合**
`<聚合函数>(<列>) FILTER (WHERE <条件>) OVER (...)`
```sql
-- 条件聚合统计高收入人数
SELECT dept_id,
  COUNT(*) AS total,
  COUNT(*) FILTER (WHERE salary > 50000) AS high_earners,
  AVG(salary) FILTER (WHERE gender = 'M') AS male_avg
FROM employees
GROUP BY dept_id;
```

**换行写法：FILTER 窗口函数组合**
`SUM(<列>) FILTER (WHERE <条件>) OVER (PARTITION BY <列>)`
```sql
-- 每个部门高薪累计
SELECT name, dept_id, salary,
  SUM(salary) FILTER (WHERE salary > 50000) OVER (PARTITION BY dept_id) AS high_salary_sum
FROM employees;
```

---

## 命名窗口

**换行写法：WINDOW 子句定义命名窗口**
`SELECT <列>, <函数>() OVER <窗口名> FROM <表> WINDOW <窗口名> AS (PARTITION BY <列> ORDER BY <列>)`
```sql
-- 复用窗口定义
SELECT name, dept_id, salary,
  RANK() OVER w AS rank,
  DENSE_RANK() OVER w AS dense_rank,
  ROW_NUMBER() OVER w AS row_num
FROM employees
WINDOW w AS (PARTITION BY dept_id ORDER BY salary DESC);
```

---

## 常见应用场景

**换行写法：取每组前 N 行**
`SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>) AS rn FROM <表>) WHERE rn <= <N>`
```sql
-- 取每个部门薪资前 3 的员工
SELECT * FROM (
  SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
  FROM employees
) ranked
WHERE rn <= 3;
```

**换行写法：去除重复行保留最新**
`SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <时间> DESC) AS rn FROM <表>) WHERE rn = 1`
```sql
-- 每个用户保留最新一条登录记录
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_time DESC) AS rn
  FROM user_logins
) latest
WHERE rn = 1;
```



<!-- ============ 文档分隔线：021-postgresql/013-CTE.md ============ -->

# PostgreSQL CTE 递归查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本 CTE

**换行写法：WITH 简单 CTE**
`WITH <CTE名> AS (SELECT ...) SELECT * FROM <CTE名>;`
```sql
-- 使用 CTE 简化查询
WITH active_users AS (
  SELECT id, username, email FROM users WHERE status = 1
)
SELECT * FROM active_users ORDER BY username;
```

**换行写法：多个 CTE**
`WITH <CTE1> AS (...), <CTE2> AS (...) SELECT ... FROM <CTE1> JOIN <CTE2>`
```sql
-- 多个 CTE 组合查询
WITH user_counts AS (
  SELECT user_id, COUNT(*) AS order_count FROM orders GROUP BY user_id
),
user_totals AS (
  SELECT user_id, SUM(total_amount) AS total FROM orders GROUP BY user_id
)
SELECT u.username, uc.order_count, ut.total
FROM users u
LEFT JOIN user_counts uc ON u.id = uc.user_id
LEFT JOIN user_totals ut ON u.id = ut.user_id;
```

**换行写法：CTE 引用前一个 CTE**
`WITH <CTE1> AS (...), <CTE2> AS (SELECT ... FROM <CTE1>) SELECT * FROM <CTE2>`
```sql
-- 后一个 CTE 引用前一个
WITH order_stats AS (
  SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id
),
heavy_users AS (
  SELECT user_id FROM order_stats WHERE cnt > 10
)
SELECT u.username FROM users u JOIN heavy_users h ON u.id = h.user_id;
```

---

## CTE 数据操作

**换行写法：WITH 配合 INSERT**
`WITH <CTE> AS (SELECT ...) INSERT INTO <表> SELECT * FROM <CTE>;`
```sql
-- 将查询结果插入新表
WITH active AS (SELECT * FROM users WHERE status = 1)
INSERT INTO active_users_backup SELECT * FROM active;
```

**换行写法：WITH 配合 UPDATE**
`WITH <CTE> AS (SELECT ...) UPDATE <表> SET ... FROM <CTE> WHERE ...`
```sql
-- 基于 CTE 更新
WITH user_totals AS (
  SELECT user_id, SUM(total_amount) AS total FROM orders GROUP BY user_id
)
UPDATE users SET balance = balance - ut.total
FROM user_totals ut
WHERE users.id = ut.user_id;
```

**换行写法：WITH 配合 DELETE**
`WITH <CTE> AS (SELECT ...) DELETE FROM <表> WHERE <列> IN (SELECT ... FROM <CTE>)`
```sql
-- 基于 CTE 删除
WITH inactive AS (SELECT id FROM users WHERE status = 0)
DELETE FROM orders WHERE user_id IN (SELECT id FROM inactive);
```

**换行写法：WITH RETURNING 返回**
`WITH <CTE> AS (INSERT ... RETURNING ...) SELECT * FROM <CTE>`
```sql
-- 插入并返回结果供后续使用
WITH inserted AS (
  INSERT INTO users (username, email) VALUES ('zhangsan', 'zs@example.com')
  RETURNING id, username
)
SELECT * FROM inserted;
```

---

## 递归 CTE 基础

**换行写法：WITH RECURSIVE 基本结构**
`WITH RECURSIVE <CTE名> AS (<基础查询> UNION [ALL] <递归查询>) SELECT * FROM <CTE名>`
```sql
-- 生成 1 到 10 的序列
WITH RECURSIVE counter(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM counter WHERE n < 10
)
SELECT n FROM counter;
```

**换行写法：UNION 去重递归**
`WITH RECURSIVE <CTE名> AS (<基础> UNION <递归>) SELECT * FROM <CTE名>`
```sql
-- 使用 UNION 去重递归
WITH RECURSIVE numbers AS (
  SELECT 1 AS n
  UNION
  SELECT n + 1 FROM numbers WHERE n < 10
)
SELECT n FROM numbers;
```

---

## 层级数据递归

**换行写法：组织架构树查询**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 查询员工层级关系
WITH RECURSIVE employee_tree AS (
  -- 基础查询：顶层员工
  SELECT id, name, manager_id, 1 AS level, name::TEXT AS path
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  -- 递归查询：下属员工
  SELECT e.id, e.name, e.manager_id, et.level + 1, et.path || ' -> ' || e.name
  FROM employees e
  JOIN employee_tree et ON e.manager_id = et.id
)
SELECT id, name, level, path FROM employee_tree ORDER BY path;
```

**换行写法：分类树查询**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 查询分类及其所有子分类
WITH RECURSIVE category_tree AS (
  SELECT id, name, parent_id, 0 AS depth, name::TEXT AS full_path
  FROM categories
  WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, c.parent_id, ct.depth + 1, ct.full_path || ' > ' || c.name
  FROM categories c
  JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT id, name, depth, full_path FROM category_tree ORDER BY full_path;
```

**换行写法：从指定节点向下查询**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 查询指定部门的所有子部门
WITH RECURSIVE sub_departments AS (
  SELECT id, name, parent_id FROM departments WHERE id = 5
  UNION ALL
  SELECT d.id, d.name, d.parent_id
  FROM departments d
  JOIN sub_departments sd ON d.parent_id = sd.id
)
SELECT * FROM sub_departments;
```

**换行写法：从指定节点向上查询祖先**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 查询指定员工的所有上级
WITH RECURSIVE managers AS (
  SELECT id, name, manager_id FROM employees WHERE id = 100
  UNION ALL
  SELECT e.id, e.name, e.manager_id
  FROM employees e
  JOIN managers m ON e.id = m.manager_id
)
SELECT * FROM managers;
```

---

## 图遍历递归

**换行写法：好友关系传递查询**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 查询某人的所有间接好友
WITH RECURSIVE friend_chain AS (
  SELECT user_id, friend_id, 1 AS distance
  FROM friendships
  WHERE user_id = 1
  UNION ALL
  SELECT fc.user_id, f.friend_id, fc.distance + 1
  FROM friendships f
  JOIN friend_chain fc ON f.user_id = fc.friend_id
  WHERE fc.distance < 5
)
SELECT DISTINCT friend_id, MIN(distance) AS min_distance
FROM friend_chain
GROUP BY friend_id;
```

**换行写法：路径图遍历**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 查询两点间所有路径
WITH RECURSIVE paths AS (
  SELECT start_node, end_node, cost, start_node::TEXT AS route
  FROM edges
  WHERE start_node = 'A'
  UNION ALL
  SELECT p.start_node, e.end_node, p.cost + e.cost, p.route || '->' || e.end_node
  FROM edges e
  JOIN paths p ON e.start_node = p.end_node
  WHERE p.route NOT LIKE '%' || e.end_node || '%'
)
SELECT route, cost FROM paths WHERE end_node = 'D' ORDER BY cost;
```

---

## 物化 CTE（PG12+）

**换行写法：MATERIALIZED 强制物化**
`WITH <CTE名> AS MATERIALIZED (SELECT ...) SELECT * FROM <CTE名>`
```sql
-- 强制物化 CTE 提高重复引用性能
WITH expensive_query AS MATERIALIZED (
  SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id
)
SELECT u.username, eq.cnt FROM users u JOIN expensive_query eq ON u.id = eq.user_id
UNION ALL
SELECT 'total', SUM(cnt) FROM expensive_query;
```

**换行写法：NOT MATERIALIZED 内联展开**
`WITH <CTE名> AS NOT MATERIALIZED (SELECT ...) SELECT * FROM <CTE名>`
```sql
-- 强制内联展开让优化器自由下推条件
WITH active_users AS NOT MATERIALIZED (
  SELECT * FROM users WHERE status = 1
)
SELECT * FROM active_users WHERE created_at > '2024-01-01';
```

---

## 递归 CTE 注意事项

**换行写法：使用 LIMIT 防止无限递归**
`WITH RECURSIVE <CTE名> AS (...) SELECT * FROM <CTE名> LIMIT <数量>`
```sql
-- 限制递归结果数量
WITH RECURSIVE counter(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM counter WHERE n < 1000000
)
SELECT n FROM counter LIMIT 100;
```

**单行写法：设置递归深度限制**
`SET statement_timeout = '<时长>';`
```sql
-- 设置语句超时防止递归死循环
SET statement_timeout = '30s';
```

**单行写法：设置递归迭代上限**
`SET max_recursive_workers = <数值>;`
```sql
-- 控制递归工作进程数
SET max_recursive_workers = 4;
```

---

## 常见应用场景

**换行写法：日期序列生成**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 生成连续日期序列
WITH RECURSIVE date_range AS (
  SELECT DATE '2024-01-01' AS day
  UNION ALL
  SELECT day + INTERVAL '1 day' FROM date_range WHERE day < DATE '2024-01-31'
)
SELECT day FROM date_range;
```

**换行写法：generate_series 替代方案**
`SELECT generate_series(<起>, <止>, <步长>);`
```sql
-- 使用内置函数生成序列
SELECT generate_series(1, 10) AS n;
SELECT generate_series(DATE '2024-01-01', DATE '2024-01-31', INTERVAL '1 day') AS day;
```

**换行写法：层级汇总**
`WITH RECURSIVE <CTE名> AS (基础 UNION ALL 递归) SELECT * FROM <CTE名>`
```sql
-- 计算每个部门及其子部门的员工总数
WITH RECURSIVE dept_tree AS (
  SELECT id, parent_id FROM departments WHERE parent_id IS NULL
  UNION ALL
  SELECT d.id, d.parent_id FROM departments d JOIN dept_tree dt ON d.parent_id = dt.id
)
SELECT dt.id, d.name, COUNT(e.id) AS employee_count
FROM dept_tree dt
JOIN departments d ON dt.id = d.id
LEFT JOIN employees e ON e.dept_id = dt.id
GROUP BY dt.id, d.name;
```



<!-- ============ 文档分隔线：021-postgresql/014-psqlCLI.md ============ -->

# PostgreSQL psql CLI 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 连接登录

**单行写法：本地连接**
`psql -U <用户名> -d <数据库名>`
```bash
# 连接本地数据库
psql -U postgres -d mydb
```

**单行写法：指定主机端口连接**
`psql -h <主机> -p <端口> -U <用户名> -d <数据库>`
```bash
# 连接远程 PostgreSQL 服务器
psql -h 192.168.1.100 -p 5432 -U appuser -d mydb
```

**单行写法：使用连接字符串**
`psql "postgresql://<用户>:<密码>@<主机>:<端口>/<数据库>"`
```bash
# 使用 URI 连接字符串
psql "postgresql://appuser:password@192.168.1.100:5432/mydb"
```

**单行写法：交互式输入密码**
`psql -U <用户名> -d <数据库> -W`
```bash
# 强制提示输入密码
psql -U postgres -d mydb -W
```

**单行写法：指定角色连接**
`psql -U <角色名> -d <数据库>`
```bash
# 指定角色登录
psql -U appuser -d mydb
```

**单行写法：使用环境变量连接**
`PGPASSWORD=<密码> psql -h <主机> -U <用户> -d <数据库>`
```bash
# 通过环境变量传递密码
PGPASSWORD=StrongPass psql -h 192.168.1.100 -U postgres -d mydb
```

---

## 执行命令

**单行写法：执行单条 SQL**
`psql -U <用户> -d <数据库> -c "<SQL>"`
```bash
# 执行单条 SQL 后退出
psql -U postgres -d mydb -c "SELECT version();"
```

**单行写法：执行多条 SQL**
`psql -U <用户> -d <数据库> -c "<SQL1>" -c "<SQL2>"`
```bash
# 执行多条 SQL
psql -U postgres -d mydb -c "SELECT 1;" -c "SELECT 2;"
```

**单行写法：执行 SQL 文件**
`psql -U <用户> -d <数据库> -f <文件路径>`
```bash
# 执行 SQL 脚本文件
psql -U postgres -d mydb -f /path/to/script.sql
```

**单行写法：从标准输入读取**
`psql -U <用户> -d <数据库> < <文件>`
```bash
# 从文件重定向输入
psql -U postgres -d mydb < script.sql
```

**单行写法：执行并输出到文件**
`psql -U <用户> -d <数据库> -c "<SQL>" -o <输出文件>`
```bash
# 将查询结果输出到文件
psql -U postgres -d mydb -c "SELECT * FROM users;" -o users.txt
```

---

## 输出格式

**单行写法：表格输出（默认）**
`psql -U <用户> -d <数据库> -c "<SQL>" --format=aligned`
```bash
# 默认表格对齐输出
psql -U postgres -d mydb -c "SELECT * FROM users LIMIT 3;"
```

**单行写法：HTML 输出**
`psql -U <用户> -d <数据库> -c "<SQL>" -H`
```bash
# 输出 HTML 表格
psql -U postgres -d mydb -c "SELECT * FROM users;" -H
```

**单行写法：逗号分隔输出**
`psql -U <用户> -d <数据库> -c "<SQL>" -A -F ','`
```bash
# 无对齐逗号分隔输出
psql -U postgres -d mydb -c "SELECT * FROM users;" -A -F ','
```

**单行写法：制表符分隔输出**
`psql -U <用户> -d <数据库> -c "<SQL>" -A -F $'\t'`
```bash
# 制表符分隔便于复制到 Excel
psql -U postgres -d mydb -c "SELECT * FROM users;" -A -F $'\t'
```

**单行写法：静默输出无表头**
`psql -U <用户> -d <数据库> -c "<SQL>" -t -A`
```bash
# 仅输出数据无表头无对齐
psql -U postgres -d mydb -c "SELECT username FROM users;" -t -A
```

**单行写法：扩展显示**
`psql -U <用户> -d <数据库> -c "<SQL>" -x`
```bash
# 垂直显示每列一行
psql -U postgres -d mydb -c "SELECT * FROM users WHERE id = 1;" -x
```

---

## 交互式元命令

**单行写法：查看帮助**
`\?`
```sql
-- 查看 psql 元命令帮助
\?
```

**单行写法：查看 SQL 帮助**
`\h <命令>`
```sql
-- 查看指定 SQL 命令帮助
\h CREATE TABLE
```

**单行写法：退出**
`\q`
```sql
-- 退出 psql
\q
```

**单行写法：切换数据库**
`\c <数据库名>`
```sql
-- 切换到其他数据库
\c mydb
```

**单行写法：查看当前连接**
`\conninfo`
```sql
-- 查看当前连接信息
\conninfo
```

---

## 对象查看元命令

**单行写法：查看所有数据库**
`\l`
```sql
-- 列出所有数据库
\l
```

**单行写法：查看所有表**
`\dt`
```sql
-- 列出当前数据库所有表
\dt
```

**单行写法：查看指定模式表**
`\dt <模式名>.*`
```sql
-- 列出指定模式的所有表
\dt public.*
```

**单行写法：查看表结构**
`\d <表名>`
```sql
-- 查看表结构含列、索引、约束
\d users
```

**单行写法：查看表详细信息**
`\d+ <表名>`
```sql
-- 查看表详细信息含描述和存储
\d+ users
```

**单行写法：查看索引**
`\di`
```sql
-- 列出所有索引
\di
```

**单行写法：查看视图**
`\dv`
```sql
-- 列出所有视图
\dv
```

**单行写法：查看函数**
`\df`
```sql
-- 列出所有函数
\df
```

**单行写法：查看序列**
`\ds`
```sql
-- 列出所有序列
\ds
```

**单行写法：查看用户角色**
`\du`
```sql
-- 列出所有用户和角色
\du
```

**单行写法：查看模式**
`\dn`
```sql
-- 列出所有模式
\dn
```

**单行写法：查看扩展**
`\dx`
```sql
-- 列出已安装扩展
\dx
```

---

## 文件操作元命令

**单行写法：执行 SQL 文件**
`\i <文件路径>`
```sql
-- 执行外部 SQL 文件
\i /path/to/script.sql
```

**单行写法：输出到文件**
`\o <文件路径>`
```sql
-- 将后续查询结果输出到文件
\o /tmp/result.txt
```

**单行写法：停止输出到文件**
`\o`
```sql
-- 恢复标准输出
\o
```

**单行写法：编辑查询缓冲区**
`\e`
```sql
-- 使用编辑器编辑当前查询
\e
```

**单行写法：编辑指定文件**
`\e <文件路径>`
```sql
-- 编辑指定文件并执行
\e /tmp/query.sql
```

**单行写法：保存查询到文件**
`\w <文件路径>`
```sql
-- 将当前查询缓冲区保存到文件
\w /tmp/query.sql
```

---

## 交互式实用命令

**单行写法：清除屏幕**
`\! clear`
```sql
-- 清除终端屏幕
\! clear
```

**单行写法：执行系统命令**
`\! <系统命令>`
```sql
-- 执行系统 shell 命令
\! ls -la
```

**单行写法：设置变量**
`\set <变量名> <值>`
```sql
-- 设置 psql 变量
\set limit 10
```

**单行写法：使用变量**
`SELECT * FROM users LIMIT :limit;`
```sql
-- 在 SQL 中使用变量
SELECT * FROM users LIMIT :limit;
```

**单行写法：取消当前输入**
`\r`
```sql
-- 重置当前查询缓冲区
\r
```

**单行写法：查看执行时间**
`\timing`
```sql
-- 开启/关闭查询执行时间统计
\timing
```

---

## 备份恢复工具

**单行写法：导出数据库**
`pg_dump -U <用户> -d <数据库> > <文件>`
```bash
# 导出整个数据库
pg_dump -U postgres -d mydb > mydb_backup.sql
```

**单行写法：导出为自定义格式**
`pg_dump -U <用户> -d <数据库> -F c -f <文件>`
```bash
# 导出为自定义压缩格式
pg_dump -U postgres -d mydb -F c -f mydb.dump
```

**单行写法：仅导出表结构**
`pg_dump -U <用户> -d <数据库> -s > <文件>`
```bash
# 仅导出表结构不导出数据
pg_dump -U postgres -d mydb -s > schema.sql
```

**单行写法：仅导出数据**
`pg_dump -U <用户> -d <数据库> -a > <文件>`
```bash
# 仅导出数据不导出表结构
pg_dump -U postgres -d mydb -a > data.sql
```

**单行写法：导出指定表**
`pg_dump -U <用户> -d <数据库> -t <表名> > <文件>`
```bash
# 仅导出指定表
pg_dump -U postgres -d mydb -t users > users_backup.sql
```

**单行写法：从 SQL 文件恢复**
`psql -U <用户> -d <数据库> < <文件>`
```bash
# 从 SQL 文本文件恢复
psql -U postgres -d mydb < mydb_backup.sql
```

**单行写法：从自定义格式恢复**
`pg_restore -U <用户> -d <数据库> <文件>`
```bash
# 从自定义压缩格式恢复
pg_restore -U postgres -d mydb mydb.dump
```

**单行写法：导出所有数据库**
`pg_dumpall -U <用户> > <文件>`
```bash
# 导出所有数据库及全局对象
pg_dumpall -U postgres > all_backup.sql
```

---

## 服务管理工具

**单行写法：初始化数据库集群**
`initdb -D <数据目录>`
```bash
# 初始化新的数据库集群
initdb -D /var/lib/postgresql/data
```

**单行写法：启动服务**
`pg_ctl -D <数据目录> start`
```bash
# 启动 PostgreSQL 服务
pg_ctl -D /var/lib/postgresql/data start
```

**单行写法：停止服务**
`pg_ctl -D <数据目录> stop`
```bash
# 停止 PostgreSQL 服务
pg_ctl -D /var/lib/postgresql/data stop
```

**单行写法：重启服务**
`pg_ctl -D <数据目录> restart`
```bash
# 重启 PostgreSQL 服务
pg_ctl -D /var/lib/postgresql/data restart
```

**单行写法：查看服务状态**
`pg_ctl -D <数据目录> status`
```bash
# 查看服务运行状态
pg_ctl -D /var/lib/postgresql/data status
```

**单行写法：重载配置**
`pg_ctl -D <数据目录> reload`
```bash
# 重载配置文件不重启
pg_ctl -D /var/lib/postgresql/data reload
```

**单行写法：创建用户**
`createuser -U <管理员> <新用户名>`
```bash
# 创建新数据库用户
createuser -U postgres appuser
```

**单行写法：创建数据库**
`createdb -U <管理员> -O <所有者> <数据库名>`
```bash
# 创建数据库并指定所有者
createdb -U postgres -O appuser mydb
```

**单行写法：删除用户**
`dropuser -U <管理员> <用户名>`
```bash
# 删除数据库用户
dropuser -U postgres appuser
```

**单行写法：删除数据库**
`dropdb -U <管理员> <数据库名>`
```bash
# 删除数据库
dropdb -U postgres mydb
```

---

## 性能分析

**单行写法：分析查询计划**
`EXPLAIN SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

**单行写法：分析并执行**
`EXPLAIN ANALYZE SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 执行查询并显示实际耗时
EXPLAIN ANALYZE SELECT * FROM users WHERE status = 1;
```

**单行写法：分析含缓冲区**
`EXPLAIN (ANALYZE, BUFFERS) SELECT <列> FROM <表名>;`
```sql
-- 显示缓冲区使用情况
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE id = 1;
```

**单行写法：查看活动连接**
`SELECT * FROM pg_stat_activity;`
```sql
-- 查看当前所有活动连接
SELECT pid, usename, datname, state, query FROM pg_stat_activity;
```

**单行写法：查看数据库大小**
`SELECT pg_size_pretty(pg_database_size('<库名>'));`
```sql
-- 查看数据库大小
SELECT pg_size_pretty(pg_database_size('mydb'));
```

**单行写法：查看表大小**
`SELECT pg_size_pretty(pg_total_relation_size('<表名>'));`
```sql
-- 查看表及其索引总大小
SELECT pg_size_pretty(pg_total_relation_size('users'));
```



<!-- ============ 文档分隔线：021-postgresql/015-PgDumpRestore.md ============ -->

# pg_dump 与 pg_restore 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## pg_dump 基本备份

**基本写法：备份单个数据库**
`pg_dump -U <用户名> -d <数据库名> -f <输出文件>`

```bash
# 备份 mydb 数据库到文件
pg_dump -U postgres -d mydb -f mydb_backup.sql
```

**基本写法：自定义压缩格式备份**
`pg_dump -U <用户名> -Fc -d <数据库名> -f <输出文件>.dump`

```bash
# 使用自定义压缩格式（支持选择性恢复，推荐）
pg_dump -U postgres -Fc -d mydb -f mydb.dump
```

**基本写法：目录格式备份（支持并行）**
`pg_dump -U <用户名> -Fd -d <数据库名> -f <输出目录>`

```bash
# 目录格式（每个表一个文件，支持并行恢复）
pg_dump -U postgres -Fd -d mydb -f mydb_dir/
```

**基本写法：并行备份**
`pg_dump -U <用户名> -Fd -j <并行数> -d <数据库名> -f <输出目录>`

```bash
# 4 个并行进程加速备份
pg_dump -U postgres -Fd -j 4 -d mydb -f mydb_dir/
```

---

## 选择性备份

**基本写法：仅备份指定表**
`pg_dump -U <用户名> -d <库名> -t <表名> [-t <表2>] -f <输出文件>`

```bash
# 仅备份 users 和 orders 表
pg_dump -U postgres -d mydb -t users -t orders -f tables_backup.sql
```

**基本写法：排除指定表**
`pg_dump -U <用户名> -d <库名> -T <表名> -f <输出文件>`

```bash
# 备份除 logs 表外的所有表
pg_dump -U postgres -d mydb -T logs -f mydb_no_logs.sql
```

**基本写法：仅备份数据/仅结构**
`pg_dump -U <用户名> -d <库名> --data-only -f <输出文件>`

```bash
# 仅备份数据（不含结构）
pg_dump -U postgres -d mydb --data-only -f mydb_data.sql
# 仅备份结构（不含数据）
pg_dump -U postgres -d mydb --schema-only -f mydb_schema.sql
```

---

## 全库与模式备份

**基本写法：备份所有数据库**
`pg_dumpall -U <用户名> -f <输出文件>`

```bash
# 备份所有数据库（含角色与表空间定义）
pg_dumpall -U postgres -f all_db_backup.sql
# 仅备份全局对象（角色、表空间）
pg_dumpall -U postgres --globals-only -f globals.sql
```

**基本写法：备份指定模式**
`pg_dump -U <用户名> -d <库名> -n <模式名> -f <输出文件>`

```bash
# 仅备份 business 模式
pg_dump -U postgres -d mydb -n business -f business_schema.sql
```

---

## pg_restore 恢复

**基本写法：从自定义格式恢复**
`pg_restore -U <用户名> -d <数据库名> <备份文件>.dump`

```bash
# 恢复自定义格式备份到指定数据库
pg_restore -U postgres -d mydb mydb.dump
```

**基本写法：从 SQL 文本恢复**
`psql -U <用户名> -d <数据库名> -f <备份文件>.sql`

```bash
# 恢复纯文本 SQL 备份
psql -U postgres -d mydb -f mydb_backup.sql
```

**基本写法：并行恢复**
`pg_restore -U <用户名> -d <库名> -j <并行数> <备份文件>.dump`

```bash
# 4 个并行进程加速恢复
pg_restore -U postgres -d mydb -j 4 mydb.dump
```

**基本写法：仅恢复结构/数据**
`pg_restore -U <用户名> -d <库名> --schema-only <备份文件>.dump`

```bash
# 仅恢复结构
pg_restore -U postgres -d mydb --schema-only mydb.dump
# 仅恢复数据
pg_restore -U postgres -d mydb --data-only mydb.dump
```

---

## 增量备份（17 新特性）

**基本写法：pg_basebackup 增量备份**
`pg_basebackup -U <用户名> -D <目录> -Fp -Xs -P --incremental <基础备份manifest路径>`

```bash
# PostgreSQL 17 増量基础备份
pg_basebackup -U postgres -D /backup/incr -Fp -Xs -P -c fast
```

**基本写法：pg_combinebackup 合并备份**
`pg_combinebackup <基础备份目录> <增量备份目录> -o <合并输出目录>`

```bash
# PostgreSQL 17 合并基础与增量备份
pg_combinebackup /backup/base /backup/incr -o /backup/combined
```

---

## 选项速查

**基本写法：连接选项**
`pg_dump -h <主机> -p <端口> -U <用户> -d <数据库>`

```bash
# 远程数据库备份
pg_dump -h 192.168.1.100 -p 5432 -U admin -d mydb -f remote.sql
```

**基本写法：压缩级别**
`pg_dump -U <用户> -Fc -Z <级别> -d <库名> -f <输出文件>`

```bash
# 指定压缩级别 0-9（9 最高压缩率）
pg_dump -U postgres -Fc -Z 6 -d mydb -f mydb.dump
```

---



<!-- ============ 文档分隔线：021-postgresql/016-ArrayType.md ============ -->

# 数组类型操作 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 数组定义与构造

**基本写法：建表定义数组列**
`<列名> <元素类型>[]`

```sql
-- 定义整型数组和文本数组列
CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  tags TEXT[],
  member_ids BIGINT[],
  scores INTEGER[]
);
```

**基本写法：数组字面量构造**
`ARRAY[<值1>, <值2>, ...]` 或 `'{<值1>,<值2>,...}'`

```sql
-- 使用 ARRAY 构造器（推荐）
INSERT INTO projects (tags) VALUES (ARRAY['java','spring','web']);
-- 使用字符串字面量
INSERT INTO projects (tags) VALUES ('{java,spring,web}');
```

**基本写法：从子查询构造数组**
`ARRAY(SELECT <列> FROM <表> WHERE <条件>)`

```sql
-- 将查询结果转为数组
SELECT id, ARRAY(SELECT name FROM users WHERE dept_id = 1) AS dept_members;
```

**基本写法：多维数组**
`<元素类型>[][]`

```sql
-- 二维数组
CREATE TABLE matrix (data INTEGER[][]);
INSERT INTO matrix VALUES (ARRAY[[1,2],[3,4]]);
```

---

## 数组访问

**基本写法：按下标访问元素**
`<数组列>[<下标>]`

```sql
-- PostgreSQL 数组下标从 1 开始
SELECT tags[1] AS first_tag FROM projects WHERE id = 1;
SELECT member_ids[1:3] AS first_three FROM projects WHERE id = 1;  -- 切片
```

**基本写法：获取数组长度**
`array_length(<数组列>, <维度>)`

```sql
-- 获取第一维长度
SELECT array_length(tags, 1) AS tag_count FROM projects;
-- 获取多维数组各维长度
SELECT array_length(data, 1), array_length(data, 2) FROM matrix;
```

**基本写法：数组展开为行**
`unnest(<数组列>)`

```sql
-- 将数组展开为多行（常用于关联查询）
SELECT id, unnest(tags) AS tag FROM projects;
-- 多数组同步展开
SELECT id, tag, score
FROM projects
CROSS JOIN unnest(tags, scores) AS t(tag, score);
```

---

## 数组包含与匹配

**基本写法：包含元素判断**
`<值> = ANY(<数组>)` / `<数组> @> <数组>`

```sql
-- 是否包含任一等于该值的元素
SELECT * FROM projects WHERE 'java' = ANY(tags);
-- 是否包含指定子集（@> 包含）
SELECT * FROM projects WHERE tags @> ARRAY['java','spring'];
-- 是否被包含（<@）
SELECT * FROM projects WHERE ARRAY['java'] <@ tags;
```

**基本写法：重叠判断**
`<数组> && <数组>`

```sql
-- 两个数组是否有公共元素（存在交集）
SELECT * FROM projects WHERE tags && ARRAY['java','python'];
```

**基本写法：查找元素位置**
`array_position(<数组>, <值>)`

```sql
-- 返回元素首次出现的下标（从 1 开始）
SELECT array_position(tags, 'spring') FROM projects WHERE id = 1;
-- 所有出现位置
SELECT array_positions(tags, 'java') FROM projects;
```

---

## 数组修改

**基本写法：连接数组**
`<数组1> || <数组2>`

```sql
-- 数组连接
SELECT ARRAY[1,2] || ARRAY[3,4] AS result;  -- {1,2,3,4}
-- 追加元素
SELECT tags || 'new_tag' FROM projects WHERE id = 1;
```

**基本写法：追加元素**
`array_append(<数组>, <值>)`

```sql
-- 在末尾追加元素
UPDATE projects SET tags = array_append(tags, 'microservice') WHERE id = 1;
```

**基本写法：删除元素**
`array_remove(<数组>, <值>)`

```sql
-- 删除所有匹配元素
UPDATE projects SET tags = array_remove(tags, 'deprecated') WHERE id = 1;
```

**基本写法：替换元素**
`array_replace(<数组>, <旧值>, <新值>)`

```sql
-- 替换所有匹配元素
UPDATE projects SET tags = array_replace(tags, 'old', 'new') WHERE id = 1;
```

**基本写法：数组去重**
`ARRAY(SELECT DISTINCT unnest(<数组>))`

```sql
-- 数组去重
SELECT id, ARRAY(SELECT DISTINCT unnest(tags)) AS unique_tags FROM projects;
```

---

## 数组函数

**基本写法：数组转字符串**
`array_to_string(<数组>, <分隔符> [, <NULL替代>])`

```sql
-- 拼接为逗号分隔字符串
SELECT array_to_string(tags, ', ') AS tag_str FROM projects;
-- NULL 用占位符替代
SELECT array_to_string(scores, ',', 'N/A') FROM projects;
```

**基本写法：字符串转数组**
`string_to_array(<字符串>, <分隔符>)`

```sql
-- 按分隔符拆分为数组
SELECT string_to_array('a,b,c', ',') AS arr;  -- {a,b,c}
```

**基本写法：数组聚合**
`array_agg(<列>)`

```sql
-- 将分组内的值聚合为数组
SELECT dept_id, array_agg(user_name) AS members
FROM users GROUP BY dept_id;
```

**基本写法：数组与集合运算**
`array_cat / array_intersect / array_union`

```sql
-- 数组并集
SELECT ARRAY(SELECT unnest(ARRAY[1,2,3]) UNION SELECT unnest(ARRAY[3,4,5]));
-- 数组交集
SELECT ARRAY(SELECT unnest(ARRAY[1,2,3]) INTERSECT SELECT unnest(ARRAY[2,3,4]));
```

---

## 数组索引

**基本写法：创建 GIN 索引加速数组查询**
`CREATE INDEX <索引名> ON <表名> USING GIN (<数组列>);`

```sql
-- 为数组列建 GIN 索引（支持 @>、&& 等操作符）
CREATE INDEX idx_projects_tags ON projects USING GIN (tags);
-- 使用索引加速包含查询
SELECT * FROM projects WHERE tags @> ARRAY['java'];
```

---



<!-- ============ 文档分隔线：021-postgresql/017-SchemaManagement.md ============ -->

# 模式（Schema）管理 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建与删除模式

**基本写法：创建模式**
`CREATE SCHEMA [IF NOT EXISTS] <模式名> [AUTHORIZATION <用户>];`

```sql
-- 创建业务模式
CREATE SCHEMA IF NOT EXISTS business;
-- 创建模式并指定属主
CREATE SCHEMA sales AUTHORIZATION sales_user;
```

**基本写法：在模式中创建对象**
`CREATE TABLE <模式名>.<表名> (...)`

```sql
-- 在指定模式下建表（使用模式限定名）
CREATE TABLE business.orders (
  id BIGSERIAL PRIMARY KEY,
  amount NUMERIC(10,2)
);
```

**基本写法：删除模式**
`DROP SCHEMA [IF EXISTS] <模式名> [CASCADE|RESTRICT];`

```sql
-- 仅删除空模式
DROP SCHEMA IF EXISTS old_app;
-- 级联删除模式及其所有对象
DROP SCHEMA IF EXISTS test_app CASCADE;
```

---

## 模式搜索路径

**基本写法：查看搜索路径**
`SHOW search_path;`

```sql
-- 查看当前模式搜索路径
SHOW search_path;  -- 默认 "$user", public
```

**基本写法：设置搜索路径**
`SET search_path TO <模式1>[, <模式2>...];`

```sql
-- 临时设置搜索路径（影响对象解析顺序）
SET search_path TO business, public;
-- 在函数内设置（仅函数执行期间生效）
SET search_path TO business, public;
SELECT * FROM orders;  -- 解析为 business.orders
```

**基本写法：持久设置搜索路径**
`ALTER DATABASE <库名> SET search_path TO <模式>;`

```sql
-- 数据库级持久设置
ALTER DATABASE mydb SET search_path TO business, public;
-- 用户级设置
ALTER ROLE app_user SET search_path TO business, public;
```

**基本写法：查看当前模式**
`SELECT current_schema();`

```sql
-- 查看当前生效模式
SELECT current_schema();
-- 查看当前用户名同名模式是否存在
SELECT current_schemas(true);
```

---

## 模式权限

**基本写法：授予模式使用权限**
`GRANT USAGE ON SCHEMA <模式名> TO <角色>;`

```sql
-- 授予角色访问模式的权限
GRANT USAGE ON SCHEMA business TO app_user;
```

**基本写法：授予模式内对象权限**
`GRANT <权限> ON ALL TABLES IN SCHEMA <模式名> TO <角色>;`

```sql
-- 授予模式内所有表的查询权限
GRANT SELECT ON ALL TABLES IN SCHEMA business TO readonly_role;
-- 授予所有序列使用权限
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA business TO app_user;
```

**基本写法：设置默认权限（新对象自动授权）**
`ALTER DEFAULT PRIVILEGES IN SCHEMA <模式名> GRANT <权限> ON TABLES TO <角色>;`

```sql
-- 后续在该模式新建的表自动授予查询权限
ALTER DEFAULT PRIVILEGES IN SCHEMA business
GRANT SELECT ON TABLES TO readonly_role;
```

---

## 模式查询与迁移

**基本写法：查看所有模式**
`SELECT schema_name FROM information_schema.schemata;`

```sql
-- 查看数据库中所有模式
SELECT schema_name, schema_owner
FROM information_schema.schemata
WHERE schema_name NOT LIKE 'pg_%' AND schema_name <> 'information_schema';
```

**基本写法：查看模式内对象**
`SELECT * FROM information_schema.tables WHERE table_schema = '<模式名>';`

```sql
-- 查看 business 模式下的所有表
SELECT table_name, table_type
FROM information_schema.tables
WHERE table_schema = 'business';
```

**基本写法：将表迁移到另一模式**
`ALTER TABLE <旧模式>.<表名> SET SCHEMA <新模式>;`

```sql
-- 将表迁移到另一模式（索引、约束自动跟随）
ALTER TABLE public.old_orders SET SCHEMA archive;
```

**基本写法：重命名模式**
`ALTER SCHEMA <旧名> RENAME TO <新名>;`

```sql
-- 重命名模式
ALTER SCHEMA old_app RENAME TO legacy_app;
```

**基本写法：修改模式属主**
`ALTER SCHEMA <模式名> OWNER TO <新属主>;`

```sql
-- 修改模式属主
ALTER SCHEMA business OWNER TO dba;
```

---

## 公共模式与扩展模式

**基本写法：public 模式（默认共享模式）**
`CREATE TABLE public.<表名> (...)`

```sql
-- public 是默认共享模式，所有用户默认有访问权
CREATE TABLE public.shared_config (key TEXT PRIMARY KEY, value TEXT);
```

**基本写法：扩展自带模式**
`CREATE EXTENSION <扩展名> SCHEMA <模式名>;`

```sql
-- 将扩展对象放到指定模式
CREATE EXTENSION IF NOT EXISTS postgis SCHEMA geo;
-- pg_catalog 系统模式（不可删除，存放内置对象）
SELECT * FROM pg_catalog.pg_class LIMIT 1;
```

---



<!-- ============ 文档分隔线：021-postgresql/018-Extension.md ============ -->

# 扩展（CREATE EXTENSION）语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 扩展管理

**基本写法：安装扩展**
`CREATE EXTENSION [IF NOT EXISTS] <扩展名> [WITH] [SCHEMA <模式>] [VERSION <版本>];`

```sql
-- 安装常用扩展
CREATE EXTENSION IF NOT EXISTS pgcrypto;          -- 加密函数
CREATE EXTENSION IF NOT EXISTS pg_trgm;            -- 模糊匹配与相似度
CREATE EXTENSION IF NOT EXISTS btree_gin;          -- GIN 索引支持 btree 类型
CREATE EXTENSION IF NOT EXISTS hstore SCHEMA public;  -- 键值对类型
-- 指定版本
CREATE EXTENSION IF NOT EXISTS postgis VERSION '3.4.0';
```

**基本写法：查看已安装扩展**
`SELECT * FROM pg_available_extensions;`

```sql
-- 查看所有可用扩展及安装状态
SELECT name, default_version, installed_version
FROM pg_available_extensions
WHERE installed_version IS NOT NULL;
-- 查看所有可用扩展（含未安装）
SELECT name, default_version FROM pg_available_extensions ORDER BY name;
```

**基本写法：查看扩展详细信息**
`\dx+`

```bash
# psql 元命令查看已安装扩展及对象
\dx
# 查看扩展包含的对象
\dx+ pg_trgm
```

**基本写法：更新扩展版本**
`ALTER EXTENSION <扩展名> UPDATE [TO <新版本>];`

```sql
-- 升级扩展到新版本
ALTER EXTENSION postgis UPDATE TO '3.5.0';
```

**基本写法：删除扩展**
`DROP EXTENSION [IF EXISTS] <扩展名> [, <扩展2>] [CASCADE|RESTRICT];`

```sql
-- 删除扩展（默认 RESTRICT，依赖对象存在则失败）
DROP EXTENSION IF EXISTS pg_trgm;
-- 级联删除扩展及其依赖对象
DROP EXTENSION IF EXISTS postgis CASCADE;
```

---

## 常用扩展速查

**基本写法：uuid-OSSP 生成 UUID**
`CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

```sql
-- 生成 UUID（uuid-ossp 扩展）
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();  -- 随机 UUID
SELECT uuid_generate_v1();  -- 基于时间
-- PG 13+ 内置 gen_random_uuid()，无需扩展
SELECT gen_random_uuid();
```

**基本写法：pg_trgm 模糊匹配**
`CREATE EXTENSION IF NOT EXISTS pg_trgm;`

```sql
-- 三元组相似度匹配
CREATE EXTENSION IF NOT EXISTS pg_trgm;
-- 相似度查询
SELECT name, similarity(name, '张三') AS sim
FROM users WHERE name % '张三' ORDER BY sim DESC;
-- 创建 GIN trigram 索引加速 LIKE
CREATE INDEX idx_users_name ON users USING GIN (name gin_trgm_ops);
```

**基本写法：pgcrypto 加密**
`CREATE EXTENSION IF NOT EXISTS pgcrypto;`

```sql
-- 加密解密函数
CREATE EXTENSION IF NOT EXISTS pgcrypto;
SELECT digest('password', 'sha256');            -- 哈希
SELECT encrypt('data', 'key', 'aes');           -- 对称加密
SELECT pgp_sym_encrypt('secret', 'password');   -- PGP 对称加密
```

**基本写法：hstore 键值对**
`CREATE EXTENSION IF NOT EXISTS hstore;`

```sql
-- 键值对存储
CREATE EXTENSION IF NOT EXISTS hstore;
CREATE TABLE kv (id INT, data hstore);
INSERT INTO kv VALUES (1, 'name=>张三, age=>25');
SELECT data->'name' FROM kv WHERE id = 1;
```

**基本写法：postgis 空间数据**
`CREATE EXTENSION IF NOT EXISTS postgis;`

```sql
-- PostGIS 空间扩展
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE TABLE geo_points (id SERIAL PRIMARY KEY, geom geometry(Point, 4326));
INSERT INTO geo_points (geom) VALUES (ST_SetSRID(ST_MakePoint(116.4, 39.9), 4326));
-- 距离查询
SELECT id FROM geo_points WHERE ST_DWithin(geom, ST_MakePoint(116.4,39.9)::geography, 1000);
```

---

## 扩展开发相关

**基本写法：查看扩展包含的对象**
`SELECT * FROM pg_extension;`

```sql
-- 查看已安装扩展的详细信息
SELECT extname, extversion, extnamespace::regnamespace
FROM pg_extension;
```

**基本写法：查看扩展依赖对象**
`SELECT * FROM pg_depend WHERE refobjid = '<扩展名>'::regclass;`

```sql
-- 查看扩展提供的函数
SELECT proname, oidvectortypes(proargtypes)
FROM pg_proc p JOIN pg_extension e ON p.proextnamespace = e.extnamespace
WHERE e.extname = 'pg_trgm';
```

**基本写法：控制扩展可用性**
`shared_preload_libraries = '<扩展名>'`

```ini
# postgresql.conf 配置需预加载的扩展（如 pg_stat_statements）
shared_preload_libraries = 'pg_stat_statements, auto_explain'
```

**基本写法：pg_stat_statements 性能统计**
`CREATE EXTENSION IF NOT EXISTS pg_stat_statements;`

```sql
-- 安装并查看 SQL 执行统计
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
-- 查看最慢的 10 条 SQL
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;
```

---



<!-- ============ 文档分隔线：021-postgresql/019-ViewMaterializedView.md ============ -->

# 视图与物化视图 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 普通视图

**基本写法：创建视图**
`CREATE [OR REPLACE] VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 创建用户概览视图
CREATE OR REPLACE VIEW v_user_summary AS
SELECT user_id, user_name, email, last_login
FROM users
WHERE status = 'active';
```

**基本写法：递归视图列名指定**
`CREATE VIEW <视图名> (<列1>, <列2>) AS <SELECT 语句>;`

```sql
-- 显式指定视图列名
CREATE VIEW v_orders (订单号, 客户, 金额) AS
SELECT order_id, customer_name, amount FROM orders;
```

**基本写法：可更新视图**
`CREATE VIEW <视图名> AS SELECT <列> FROM <表>;`

```sql
-- 简单视图可直接 INSERT/UPDATE/DELETE（需包含基表所有非空列）
CREATE VIEW v_active_users AS
SELECT id, name, email FROM users WHERE status = 'active';
-- 通过视图插入
INSERT INTO v_active_users (id, name, email) VALUES (100, '张三', 'z@e.com');
```

**基本写法：带安全屏障视图**
`CREATE VIEW <视图名> WITH (security_barrier) AS <SELECT>;`

```sql
-- 防止通过视图泄露 WHERE 条件数据（行安全增强）
CREATE VIEW v_user_data WITH (security_barrier) AS
SELECT id, name FROM users WHERE deleted_at IS NULL;
```

---

## 视图管理

**基本写法：查看视图定义**
`SELECT pg_get_viewdef('<视图名>'::regclass, true);`

```sql
-- 查看视图完整定义
SELECT pg_get_viewdef('v_user_summary'::regclass, true);
-- psql 元命令
\d+ v_user_summary
```

**基本写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名> [, <视图2>] [CASCADE|RESTRICT];`

```sql
-- 安全删除视图
DROP VIEW IF EXISTS v_user_summary;
-- 级联删除依赖此视图的对象
DROP VIEW IF EXISTS v_orders CASCADE;
```

**基本写法：修改视图属主与模式**
`ALTER VIEW <视图名> OWNER TO <新属主>;`

```sql
-- 修改视图属主
ALTER VIEW v_user_summary OWNER TO app_user;
-- 修改视图所属模式
ALTER VIEW v_user_summary SET SCHEMA reporting;
```

---

## 物化视图创建

**基本写法：创建物化视图**
`CREATE MATERIALIZED VIEW <视图名> AS <SELECT 语句> [WITH [NO] DATA];`

```sql
-- 创建物化视图（预先计算并存储结果）
CREATE MATERIALIZED VIEW mv_daily_sales AS
SELECT date_trunc('day', order_time) AS day,
       SUM(amount) AS total,
       COUNT(*) AS order_count
FROM orders
GROUP BY 1;
-- 仅建结构不填充数据
CREATE MATERIALIZED VIEW mv_daily_sales AS
SELECT date_trunc('day', order_time), SUM(amount) FROM orders GROUP BY 1
WITH NO DATA;
```

**基本写法：指定存储参数与表空间**
`CREATE MATERIALIZED VIEW <视图名> WITH (<参数>) TABLESPACE <表空间> AS <SELECT>;`

```sql
-- 指定填充因子与表空间
CREATE MATERIALIZED VIEW mv_report WITH (fillfactor=80) TABLESPACE ssd
AS SELECT * FROM large_table WHERE year = 2024;
```

---

## 物化视图刷新

**基本写法：全量刷新**
`REFRESH MATERIALIZED VIEW <视图名>;`

```sql
-- 全量刷新（刷新期间阻塞查询）
REFRESH MATERIALIZED VIEW mv_daily_sales;
```

**基本写法：并发刷新（不阻塞）**
`REFRESH MATERIALIZED VIEW CONCURRENTLY <视图名>;`

```sql
-- 并发刷新（需物化视图有唯一索引）
CREATE UNIQUE INDEX idx_mv_daily_sales_day ON mv_daily_sales(day);
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_daily_sales;
```

**基本写法：定时刷新物化视图**
`SELECT cron.schedule('<任务名>', '<cron 表达式>', 'REFRESH MATERIALIZED VIEW <视图>');`

```sql
-- 使用 pg_cron 扩展定时刷新（每小时）
SELECT cron.schedule('refresh_sales', '0 * * * *',
  'REFRESH MATERIALIZED VIEW CONCURRENTLY mv_daily_sales');
```

---

## 物化视图管理

**基本写法：查看物化视图信息**
`SELECT * FROM pg_matviews;`

```sql
-- 查看所有物化视图
SELECT matviewname, schemaname, ispopulated
FROM pg_matviews;
-- 查看是否已填充数据（ispopulated）
```

**基本写法：删除物化视图**
`DROP MATERIALIZED VIEW [IF EXISTS] <视图名> [CASCADE];`

```sql
-- 删除物化视图（数据与结构一起删除）
DROP MATERIALIZED VIEW IF EXISTS mv_daily_sales;
```

**基本写法：修改物化视图（受限）**
`ALTER MATERIALIZED VIEW <视图名> <选项>;`

```sql
-- 修改属主与存储参数（不能直接修改查询定义，需重建）
ALTER MATERIALIZED VIEW mv_daily_sales OWNER TO report_user;
ALTER MATERIALIZED VIEW mv_daily_sales SET (fillfactor = 90);
-- 重命名列
ALTER MATERIALIZED VIEW mv_daily_sales RENAME COLUMN total TO total_amount;
```

**基本写法：重建物化视图定义**
`DROP MATERIALIZED VIEW <旧视图>; CREATE MATERIALIZED VIEW <新视图> AS <新查询>;`

```sql
-- 修改查询定义需重建（推荐先建新视图再删旧）
CREATE MATERIALIZED VIEW mv_daily_sales_v2 AS
SELECT date_trunc('day', order_time), SUM(amount), MAX(amount)
FROM orders GROUP BY 1;
DROP MATERIALIZED VIEW mv_daily_sales;
ALTER MATERIALIZED VIEW mv_daily_sales_v2 RENAME TO mv_daily_sales;
```

---



<!-- ============ 文档分隔线：021-postgresql/020-ListenNotify.md ============ -->

# LISTEN/NOTIFY 监听通知 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## NOTIFY 发送通知

**基本写法：发送通知**
`NOTIFY <通道名>[, '<载荷>'];`

```sql
-- 发送通道通知（无载荷）
NOTIFY user_update;
-- 发送带载荷的通知（载荷必须是字符串）
NOTIFY order_event, '{"order_id":1001,"action":"created"}';
```

**基本写法：pg_notify 函数发送通知**
`SELECT pg_notify('<通道名>', '<载荷>');`

```sql
-- 使用函数形式发送（载荷支持任意字符串）
SELECT pg_notify('task_queue', '{"task":"send_email","to":"user@example.com"}');
```

**基本写法：事务提交时触发通知**
`NOTIFY <通道> -- 在事务中`

```sql
-- 通知在事务提交时才真正发送（事务回滚则不发）
BEGIN;
UPDATE orders SET status = 'paid' WHERE id = 1001;
NOTIFY order_event, '{"order_id":1001,"status":"paid"}';
COMMIT;
```

---

## LISTEN 监听通道

**基本写法：监听通道**
`LISTEN <通道名>;`

```sql
-- 当前会话开始监听指定通道
LISTEN order_event;
-- 监听后该通道的通知会被异步推送到此会话
```

**基本写法：取消监听**
`UNLISTEN <通道名>;`

```sql
-- 停止监听指定通道
UNLISTEN order_event;
-- 停止所有通道监听
UNLISTEN *;
```

---

## 接收通知

**基本写法：psql 接收通知**
`LISTEN <通道>;`

```sql
-- 在 psql 中监听后，通知会自动显示
LISTEN order_event;
-- 当其他会话执行 NOTIFY 时，本会话显示:
-- Asynchronous notification "order_event" with payload "..." received from server process PID xxx.
```

**基本写法：应用轮询接收**
`SELECT 1; -- 触发通知接收`

```sql
-- 驱动通常需执行任意查询才能拉取排队中的通知
-- libpq 使用 PQnotifies 获取通知
-- JDBC 使用 PGNotification 接口
LISTEN order_event;
-- 定期执行轻量查询拉取通知
SELECT pg_notification_queue_usage();  -- 查看队列使用率
```

**基本写法：查看监听状态**
`SELECT * FROM pg_listening_channels();`

```sql
-- 查看当前会话监听的所有通道
SELECT pg_listening_channels();
-- 查看所有会话的监听（需超级用户）
SELECT pid, channel FROM pg_stat_activity
WHERE query LIKE 'LISTEN%';
```

---

## 实战模式

**基本写法：触发器配合 NOTIFY**
`CREATE TRIGGER ... AFTER ... DO NOTIFY <通道>, '<载荷>';`

```sql
-- 表变更时自动通知（监听方据载荷处理）
CREATE OR REPLACE FUNCTION notify_order_change()
RETURNS trigger AS $$
BEGIN
  PERFORM pg_notify('order_event',
    json_build_object('id', NEW.id, 'action', TG_OP)::text);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_order_notify
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH ROW EXECUTE FUNCTION notify_order_change();
```

**基本写法：队列模式（任务分发）**
`NOTIFY <通道>, '<任务JSON>'`

```sql
-- 生产者插入任务并通知
INSERT INTO task_queue (task_type, payload)
VALUES ('email', '{"to":"u@e.com"}');
NOTIFY task_available;
-- 消费者监听并拉取处理
LISTEN task_available;
-- 收到通知后查询并锁定任务
SELECT id, payload FROM task_queue
WHERE status = 'pending'
FOR UPDATE SKIP LOCKED LIMIT 1;
```

---

## 注意事项

**基本写法：载荷大小限制**
`NOTIFY <通道>, '<载荷>' -- 载荷不超过 8000 字节`

```sql
-- 载荷字符串需小于 8000 字节
-- 大数据建议只传 ID，监听方再查表
NOTIFY large_change, '{"id": 1001}';  -- 仅传 ID
-- 监听方接收后再查表
-- SELECT * FROM changes WHERE id = 1001;
```

**基本写法：查看通知队列使用率**
`SELECT pg_notification_queue_usage();`

```sql
-- 查看通知队列使用率（0-1，超过 0.5 需注意消费速度）
SELECT pg_notification_queue_usage();
```

**基本写法：清理堆积通知**
`UNLISTEN <通道>; LISTEN <通道>;`

```sql
-- 重新监听可清空当前会话已排队但未消费的通知
UNLISTEN order_event;
LISTEN order_event;
```

---



<!-- ============ 文档分隔线：021-postgresql/021-FullTextSearch.md ============ -->

# 全文搜索 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## tsvector 与 tsquery

**基本写法：创建 tsvector 文档**
`to_tsvector([<配置>,] <文本>)`

```sql
-- 将文本转换为标准化词素（分词、去停用词、词干化）
SELECT to_tsvector('english', 'The quick brown fox jumps');
-- 输出: 'brown':3 'fox':4 'jump':5 'quick':2
-- 中文需 zhparser 扩展
SELECT to_tsvector('chinese', '数据库性能优化');
```

**基本写法：创建 tsquery 查询**
`to_tsquery([<配置>,] <查询表达式>)` / `plainto_tsquery(<文本>)`

```sql
-- to_tsquery 支持运算符 & | ! <->（与/或/非/相邻）
SELECT to_tsquery('english', 'quick & brown');
-- plainto_tsquery 自动处理（不支持运算符，全部 AND）
SELECT plainto_tsquery('english', 'quick brown fox');
-- phraseto_tsquery 短语匹配（词序敏感）
SELECT phraseto_tsquery('english', 'quick brown fox');
-- websearch_to_tsquery 类似搜索引擎语法
SELECT websearch_to_tsquery('english', 'quick OR brown -slow');
```

**基本写法：手动构造 tsvector**
`'<词1>:<位置> <词2>:<位置>'::tsvector`

```sql
-- 手动指定词与位置
SELECT '数据库:1 性能:2 优化:3'::tsvector;
-- 含权重（A 最高，D 默认）
SELECT setweight('数据库:1 性能:2'::tsvector, 'A');
```

---

## 搜索查询

**基本写法：全文匹配**
`WHERE to_tsvector(<列>) @@ to_tsquery(<查询>)`

```sql
-- 使用 @@ 操作符匹配
SELECT id, title
FROM articles
WHERE to_tsvector(title) @@ to_tsquery('database & performance');
```

**基本写法：返回相关性排序**
`ts_rank(<tsvector>, <tsquery>)`

```sql
-- 按相关性分数排序
SELECT id, title,
  ts_rank(to_tsvector(title), to_tsquery('database')) AS rank
FROM articles
WHERE to_tsvector(title) @@ to_tsquery('database')
ORDER BY rank DESC;
-- ts_rank_cd 考虑词距（覆盖密度）
SELECT id, ts_rank_cd(to_tsvector(body), query) FROM articles;
```

**基本写法：高亮显示**
`ts_headline([<配置>,] <原文>, <tsquery> [, <选项>])`

```sql
-- 返回带高亮标记的摘要
SELECT ts_headline('english', body, to_tsquery('database & performance'),
  'StartSel=<b>, StopSel=</b>, MaxWords=35, MinWords=15')
FROM articles
WHERE to_tsvector(body) @@ to_tsquery('database & performance');
```

---

## GIN 索引

**基本写法：创建 GIN 全文索引**
`CREATE INDEX <索引名> ON <表名> USING GIN (to_tsvector(<配置>, <列>));`

```sql
-- 为表达式创建 GIN 索引加速全文搜索
CREATE INDEX idx_articles_body_fts
ON articles USING GIN (to_tsvector('english', body));
```

**基本写法：生成列加速索引**
`<列> tsvector GENERATED ALWAYS AS (to_tsvector(...)) STORED`

```sql
-- 使用生成列避免重复计算
CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  body TEXT,
  body_tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', body)) STORED
);
-- 为生成列建索引
CREATE INDEX idx_articles_body_tsv ON articles USING GIN (body_tsv);
-- 直接查询生成列
SELECT * FROM articles WHERE body_tsv @@ to_tsquery('database');
```

---

## 搜索配置

**基本写法：查看搜索配置**
`SELECT * FROM pg_ts_config;`

```sql
-- 查看可用的文本搜索配置
SELECT cfgname FROM pg_ts_config;
-- 默认配置（通常为 simple 或 english）
SHOW default_text_search_config;
-- 设置默认配置
SET default_text_search_config = 'english';
```

**基本写法：中文搜索配置**
`CREATE TEXT SEARCH CONFIGURATION <配置名> (...)`

```sql
-- 使用 zhparser 扩展配置中文搜索
CREATE EXTENSION IF NOT EXISTS zhparser;
CREATE TEXT SEARCH CONFIGURATION chinese (PARSER = zhparser);
ALTER TEXT SEARCH CONFIGURATION chinese
  ADD MAPPING FOR n,v,a,i,e,l WITH simple;
-- 使用配置
SELECT to_tsvector('chinese', '数据库性能优化');
```

---

## 复合搜索

**基本写法：多列加权搜索**
`setweight(to_tsvector(<列1>), 'A') || setweight(to_tsvector(<列2>), 'B')`

```sql
-- 标题权重 A（最高），正文权重 D（默认）
SELECT id,
  setweight(to_tsvector(title), 'A') ||
  setweight(to_tsvector(body), 'D') AS document
FROM articles;
-- 加权相关性排序（标题匹配分数更高）
SELECT id, title,
  ts_rank(setweight(to_tsvector(title), 'A') ||
          setweight(to_tsvector(body), 'D'),
          to_tsquery('database')) AS rank
FROM articles
WHERE to_tsvector(title) || to_tsvector(body) @@ to_tsquery('database')
ORDER BY rank DESC;
```

**基本写法：词组相邻搜索**
`phraseto_tsquery(<配置>, '<短语>')` 或 `<词1> <-> <词2>`

```sql
-- 精确短语匹配（词序相邻）
SELECT * FROM articles
WHERE to_tsvector(body) @@ phraseto_tsquery('database performance');
-- 指定相邻距离
SELECT * FROM articles
WHERE to_tsvector(body) @@ to_tsquery('database <3> performance');
```

---

## 字典与停用词

**基本写法：查看字典**
`SELECT * FROM pg_ts_dict;`

```sql
-- 查看可用字典
SELECT dictname, dictinit FROM pg_ts_dict;
```

**基本写法：自定义停用词**
`CREATE TEXT SEARCH DICTIONARY <名称> (TEMPLATE = pg_catalog.simple, STOPWORDS = <停用词集>);`

```sql
-- 创建自定义停用词字典
CREATE TEXT SEARCH DICTIONARY my_simple (
  TEMPLATE = pg_catalog.simple,
  STOPWORDS = my_stopwords
);
```

---
