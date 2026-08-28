---
order: 10
title: 020-mysql 模块文档合集
module: 'mysql'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：020-mysql/001-TriggerEvent.md ============ -->

# MySQL 触发器与事件

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 触发器基础

**换行写法：创建插入后触发器**
`CREATE TRIGGER <触发器名> AFTER INSERT ON <表名> FOR EACH ROW BEGIN <触发体> END`
```sql
-- 插入后记录审计日志
DELIMITER //
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_audit_log (user_id, action, action_time, details)
    VALUES (NEW.id, 'INSERT', NOW(), CONCAT('Created user: ', NEW.username));
END //
DELIMITER ;
```

**单行写法：删除触发器**
`DROP TRIGGER [IF EXISTS] <触发器名>`
```sql
-- 删除触发器
DROP TRIGGER IF EXISTS before_user_insert;
```

---

## NEW 与 OLD 关键字

**换行写法：NEW 关键字访问新数据**
`NEW.<列名>`
```sql
-- 更新前比较新旧值并记录变更
DELIMITER //
CREATE TRIGGER before_user_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.username != NEW.username THEN
        INSERT INTO user_change_log (user_id, field_name, old_value, new_value, changed_at)
        VALUES (OLD.id, 'username', OLD.username, NEW.username, NOW());
    END IF;
END //
DELIMITER ;
```

**换行写法：OLD 关键字访问旧数据**
`OLD.<列名>`
```sql
-- 删除后记录被删除的数据
DELIMITER //
CREATE TRIGGER after_user_delete
AFTER DELETE ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_delete_log (user_id, username, deleted_at)
    VALUES (OLD.id, OLD.username, NOW());
END //
DELIMITER ;
```

---

## BEFORE 触发器

**换行写法：BEFORE 触发器数据验证**
`SIGNAL SQLSTATE '<状态码>' SET MESSAGE_TEXT = '<错误信息>'`
```sql
-- 更新前验证薪资不能低于最低标准
DELIMITER //
CREATE TRIGGER before_salary_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 3000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '薪资不能低于最低标准3000元';
    END IF;
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器验证订单金额**
`SIGNAL SQLSTATE '<状态码>' SET MESSAGE_TEXT = '<错误信息>'`
```sql
-- 插入前验证订单金额必须大于 0
DELIMITER //
CREATE TRIGGER before_order_insert
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.total_amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '订单金额必须大于0';
    END IF;
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器自动计算字段**
`SET NEW.<列名> = <值>`
```sql
-- 插入前自动计算商品总价
DELIMITER //
CREATE TRIGGER before_order_item_insert
BEFORE INSERT ON order_items
FOR EACH ROW
BEGIN
    SET NEW.line_total = NEW.quantity * NEW.unit_price;
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器自动更新时间**
`SET NEW.<列名> = NOW()`
```sql
-- 更新前自动维护修改时间
DELIMITER //
CREATE TRIGGER before_product_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END //
DELIMITER ;
```

**换行写法：BEFORE 触发器自动生成编号**
`SET NEW.<列名> = <生成表达式>`
```sql
-- 插入前自动生成订单编号
DELIMITER //
CREATE TRIGGER before_order_insert2
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    IF NEW.order_no IS NULL THEN
        SET NEW.order_no = CONCAT('ORD', DATE_FORMAT(NOW(), '%Y%m%d'),
            LPAD((SELECT COUNT(*) FROM orders WHERE order_date = CURDATE()) + 1, 4, '0'));
    END IF;
END //
DELIMITER ;
```

---

## AFTER 触发器

**换行写法：AFTER 插入审计**
`INSERT INTO <日志表> VALUES (NEW.<列名>...)`
```sql
-- 插入后记录产品审计日志
DELIMITER //
CREATE TRIGGER after_product_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, new_data, action_time)
    VALUES ('products', NEW.id, 'INSERT',
            JSON_OBJECT('name', NEW.name, 'price', NEW.price, 'stock', NEW.stock),
            NOW());
END //
DELIMITER ;
```

**换行写法：AFTER 更新审计**
`INSERT INTO <日志表> VALUES (OLD.<列名>..., NEW.<列名>...)`
```sql
-- 更新后记录新旧数据审计日志
DELIMITER //
CREATE TRIGGER after_product_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_data, new_data, action_time)
    VALUES ('products', NEW.id, 'UPDATE',
            JSON_OBJECT('name', OLD.name, 'price', OLD.price, 'stock', OLD.stock),
            JSON_OBJECT('name', NEW.name, 'price', NEW.price, 'stock', NEW.stock),
            NOW());
END //
DELIMITER ;
```

**换行写法：AFTER 删除审计**
`INSERT INTO <日志表> VALUES (OLD.<列名>...)`
```sql
-- 删除后记录被删除数据审计日志
DELIMITER //
CREATE TRIGGER after_product_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (table_name, record_id, action, old_data, action_time)
    VALUES ('products', OLD.id, 'DELETE',
            JSON_OBJECT('name', OLD.name, 'price', OLD.price, 'stock', OLD.stock),
            NOW());
END //
DELIMITER ;
```

**换行写法：AFTER 触发器扣减库存**
`UPDATE <关联表> SET <列名> = <列名> - NEW.<列名> WHERE <条件>`
```sql
-- 订单项插入后扣减商品库存
DELIMITER //
CREATE TRIGGER after_order_item_insert
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock - NEW.quantity
    WHERE id = NEW.product_id;
END //
DELIMITER ;
```

**换行写法：AFTER 触发器恢复库存**
`UPDATE <关联表> SET <列名> = <列名> + OLD.<列名> WHERE <条件>`
```sql
-- 订单项删除后恢复商品库存
DELIMITER //
CREATE TRIGGER after_order_item_delete
AFTER DELETE ON order_items
FOR EACH ROW
BEGIN
    UPDATE products
    SET stock = stock + OLD.quantity
    WHERE id = OLD.product_id;
END //
DELIMITER ;
```

**换行写法：AFTER 触发器更新统计**
`UPDATE <统计表> SET <列名> = <列名> + NEW.<列名> WHERE <条件>`
```sql
-- 订单插入后更新客户统计信息
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customers
    SET total_orders = total_orders + 1,
        total_spent = total_spent + NEW.total_amount,
        last_order_date = NEW.order_date
    WHERE id = NEW.customer_id;
END //
DELIMITER ;
```

---

## 事件调度器

**单行写法：查看调度器状态**
`SHOW VARIABLES LIKE 'event_scheduler'`
```sql
-- 检查事件调度器状态
SHOW VARIABLES LIKE 'event_scheduler';
```

**单行写法：启用调度器**
`SET GLOBAL event_scheduler = ON`
```sql
-- 启用事件调度器
SET GLOBAL event_scheduler = ON;
```

**换行写法：创建每日定时事件**
`CREATE EVENT [IF NOT EXISTS] <事件名> ON SCHEDULE EVERY 1 DAY [STARTS <时间>] DO BEGIN <事件体> END`
```sql
-- 每天凌晨清理过期会话
DELIMITER //
CREATE EVENT IF NOT EXISTS cleanup_expired_sessions
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_DATE + INTERVAL 1 DAY + INTERVAL 2 HOUR
DO
BEGIN
    DELETE FROM sessions WHERE expires_at < NOW();
    INSERT INTO event_log (event_name, executed_at, rows_affected)
    VALUES ('cleanup_expired_sessions', NOW(), ROW_COUNT());
END //
DELIMITER ;
```

**换行写法：创建每小时定时事件**
`CREATE EVENT [IF NOT EXISTS] <事件名> ON SCHEDULE EVERY 1 HOUR DO BEGIN <事件体> END`
```sql
-- 每小时更新热门商品
DELIMITER //
CREATE EVENT IF NOT EXISTS update_hot_products
ON SCHEDULE EVERY 1 HOUR
DO
BEGIN
    TRUNCATE TABLE hot_products;
    INSERT INTO hot_products (product_id, view_count, sales_count)
    SELECT p.id, p.view_count, COALESCE(SUM(oi.quantity), 0)
    FROM products p
    LEFT JOIN order_items oi ON p.id = oi.product_id
    WHERE p.created_at >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    GROUP BY p.id
    ORDER BY p.view_count DESC, sales_count DESC
    LIMIT 100;
END //
DELIMITER ;
```

**换行写法：创建每月定时事件**
`CREATE EVENT [IF NOT EXISTS] <事件名> ON SCHEDULE EVERY 1 MONTH STARTS '<时间>' DO BEGIN <事件体> END`
```sql
-- 每月 1 号生成统计报表
DELIMITER //
CREATE EVENT IF NOT EXISTS monthly_report
ON SCHEDULE EVERY 1 MONTH
STARTS '2026-07-01 00:00:00'
DO
BEGIN
    INSERT INTO monthly_reports (report_month, total_orders, total_revenue, new_users)
    SELECT
        DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%Y-%m'),
        (SELECT COUNT(*) FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND order_date < CURDATE()),
        (SELECT COALESCE(SUM(total_amount), 0) FROM orders
         WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND order_date < CURDATE()),
        (SELECT COUNT(*) FROM users WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
         AND created_at < CURDATE());
END //
DELIMITER ;
```

**换行写法：创建一次性事件**
`CREATE EVENT <事件名> ON SCHEDULE AT <时间> DO BEGIN <事件体> END`
```sql
-- 5 分钟后执行一次性任务
DELIMITER //
CREATE EVENT IF NOT EXISTS one_time_task
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 5 MINUTE
DO
BEGIN
    UPDATE system_config SET value = 'initialized' WHERE key = 'status';
END //
DELIMITER ;
```

**单行写法：查看所有事件**
`SHOW EVENTS`
```sql
-- 查看所有事件
SHOW EVENTS;
```

**单行写法：查看事件详情**
`SHOW CREATE EVENT <事件名>`
```sql
-- 查看事件定义详情
SHOW CREATE EVENT cleanup_expired_sessions;
```

**单行写法：禁用事件**
`ALTER EVENT <事件名> DISABLE`
```sql
-- 禁用指定事件
ALTER EVENT cleanup_expired_sessions DISABLE;
```

**单行写法：启用事件**
`ALTER EVENT <事件名> ENABLE`
```sql
-- 启用指定事件
ALTER EVENT cleanup_expired_sessions ENABLE;
```

**单行写法：修改事件调度周期**
`ALTER EVENT <事件名> ON SCHEDULE EVERY <间隔>`
```sql
-- 修改事件的调度周期
ALTER EVENT cleanup_expired_sessions
ON SCHEDULE EVERY 2 DAY;
```

**单行写法：删除事件**
`DROP EVENT [IF EXISTS] <事件名>`
```sql
-- 删除事件
DROP EVENT IF EXISTS one_time_task;
```

**换行写法：查询事件信息**
`SELECT <列名> FROM information_schema.events WHERE <条件>`
```sql
-- 从 information_schema 查询事件信息
SELECT event_name, status, interval_value, interval_field, last_executed
FROM information_schema.events
WHERE event_schema = 'mydb';
```

---

## 条件触发器

**换行写法：使用标志变量控制触发器**
`IF @<变量名> IS NULL OR @<变量名> = 0 THEN <逻辑> END IF`
```sql
-- 批量操作时通过标志变量跳过触发器逻辑
DELIMITER //
CREATE TRIGGER conditional_trigger
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    IF @skip_trigger IS NULL OR @skip_trigger = 0 THEN
        SET NEW.updated_at = NOW();
    END IF;
END //
DELIMITER ;
```

**换行写法：批量操作时设置标志变量**
`SET @<变量名> = <值>`
```sql
-- 批量更新时设置标志变量跳过触发器
SET @skip_trigger = 1;
UPDATE products SET price = price * 1.1;
SET @skip_trigger = 0;
```


<!-- ============ 文档分隔线：020-mysql/002-StoredProcedureAndFunction.md ============ -->

# MySQL 存储过程与函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 存储过程基础

**换行写法：创建无参存储过程**
`CREATE PROCEDURE <过程名>() BEGIN <过程体> END`
```sql
-- 创建查询所有用户的存储过程
DELIMITER //
CREATE PROCEDURE GetAllUsers()
BEGIN
    SELECT id, username, email, created_at
    FROM users
    ORDER BY created_at DESC;
END //
DELIMITER ;
```

**单行写法：调用存储过程**
`CALL <过程名>([<参数>...])`
```sql
-- 调用存储过程
CALL GetAllUsers();
```

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS GetAllUsers;
```

**单行写法：查看存储过程定义**
`SHOW CREATE PROCEDURE <过程名>`
```sql
-- 查看存储过程定义
SHOW CREATE PROCEDURE GetAllUsers;
```

---

## 参数类型

**换行写法：IN 参数**
`IN <参数名> <类型>`
```sql
-- 创建带 IN 输入参数的存储过程
DELIMITER //
CREATE PROCEDURE GetUserById(IN p_user_id INT)
BEGIN
    SELECT id, username, email
    FROM users
    WHERE id = p_user_id;
END //
DELIMITER ;
```

**换行写法：OUT 参数**
`OUT <参数名> <类型>`
```sql
-- 创建带 OUT 输出参数的存储过程
DELIMITER //
CREATE PROCEDURE GetUserCount(OUT p_count INT)
BEGIN
    SELECT COUNT(*) INTO p_count FROM users;
END //
DELIMITER ;
```

**换行写法：INOUT 参数**
`INOUT <参数名> <类型>`
```sql
-- 创建带 INOUT 输入输出参数的存储过程
DELIMITER //
CREATE PROCEDURE DoubleValue(INOUT p_value INT)
BEGIN
    SET p_value = p_value * 2;
END //
DELIMITER ;
```

---

## 变量声明

**单行写法：声明局部变量**
`DECLARE <变量名> <类型> [DEFAULT <默认值>]`
```sql
-- 声明带默认值的局部变量
DECLARE v_name VARCHAR(100) DEFAULT 'Unknown';
```

**单行写法：SELECT INTO 赋值**
`SELECT <列名> INTO <变量名> FROM <表名> WHERE <条件>`
```sql
-- 查询结果赋值给变量
SELECT COUNT(*) INTO v_count FROM users;
```

**单行写法：SET 变量赋值**
`SET <变量名> = <值>`
```sql
-- 为局部变量赋值
SET v_total = v_count * 9.99;
```

**单行写法：设置用户变量**
`SET @<变量名> = <值>`
```sql
-- 设置会话级别的用户变量
SET @user_var = 'Hello';
```

---

## 条件判断

**换行写法：IF 多分支**
`IF <条件> THEN <语句> [ELSEIF <条件> THEN <语句>] [ELSE <语句>] END IF`
```sql
-- 根据金额计算折扣率
DELIMITER //
CREATE PROCEDURE GetDiscount(IN p_amount DECIMAL(10, 2))
BEGIN
    DECLARE v_discount DECIMAL(4, 2);

    IF p_amount >= 1000 THEN
        SET v_discount = 0.20;
    ELSEIF p_amount >= 500 THEN
        SET v_discount = 0.10;
    ELSEIF p_amount >= 100 THEN
        SET v_discount = 0.05;
    ELSE
        SET v_discount = 0.00;
    END IF;

    SELECT p_amount AS original,
           p_amount * (1 - v_discount) AS discounted,
           v_discount AS discount_rate;
END //
DELIMITER ;
```

**换行写法：CASE 多分支**
`CASE <表达式> WHEN <值> THEN <语句> [WHEN ...] [ELSE <语句>] END CASE`
```sql
-- 根据地区计算运费
DELIMITER //
CREATE PROCEDURE GetShippingCost(IN p_region VARCHAR(50))
BEGIN
    DECLARE v_cost DECIMAL(10, 2);

    CASE p_region
        WHEN 'North' THEN SET v_cost = 10.00;
        WHEN 'South' THEN SET v_cost = 15.00;
        WHEN 'East' THEN SET v_cost = 12.00;
        WHEN 'West' THEN SET v_cost = 12.00;
        ELSE SET v_cost = 20.00;
    END CASE;

    SELECT v_cost AS shipping_cost;
END //
DELIMITER ;
```

---

## 循环

**换行写法：WHILE 循环**
`[<标签>:] WHILE <条件> DO <语句> END WHILE [<标签>]`
```sql
-- WHILE 循环生成数字串
DELIMITER //
CREATE PROCEDURE GenerateNumbers(IN p_count INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE result VARCHAR(1000) DEFAULT '';

    WHILE i <= p_count DO
        SET result = CONCAT(result, IF(i > 1, ',', ''), i);
        SET i = i + 1;
    END WHILE;

    SELECT result AS numbers;
END //
DELIMITER ;
```

**换行写法：REPEAT 循环**
`[<标签>:] REPEAT <语句> UNTIL <条件> END REPEAT [<标签>]`
```sql
-- REPEAT 循环至少执行一次
DELIMITER //
CREATE PROCEDURE RepeatDemo(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE total INT DEFAULT 0;

    REPEAT
        SET total = total + i;
        SET i = i + 1;
    UNTIL i > p_limit
    END REPEAT;

    SELECT total AS sum_result;
END //
DELIMITER ;
```

**换行写法：LOOP 循环**
`[<标签>:] LOOP <语句> END LOOP [<标签>]`
```sql
-- LOOP 配合 LEAVE 跳出循环
DELIMITER //
CREATE PROCEDURE LoopDemo(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT DEFAULT 0;

    add_loop: LOOP
        SET i = i + 1;
        IF i > p_limit THEN
            LEAVE add_loop;
        END IF;
        SET total = total + i;
    END LOOP;

    SELECT total AS sum_result;
END //
DELIMITER ;
```

**单行写法：ITERATE 跳过当前循环**
`ITERATE <标签>`
```sql
-- ITERATE 跳过偶数只累加奇数
DELIMITER //
CREATE PROCEDURE OddSum(IN p_limit INT)
BEGIN
    DECLARE i INT DEFAULT 0;
    DECLARE total INT DEFAULT 0;

    odd_loop: LOOP
        SET i = i + 1;
        IF i > p_limit THEN
            LEAVE odd_loop;
        END IF;
        IF i % 2 = 0 THEN
            ITERATE odd_loop;
        END IF;
        SET total = total + i;
    END LOOP;

    SELECT total AS odd_sum;
END //
DELIMITER ;
```

---

## 游标

**换行写法：游标基本遍历**
`DECLARE <游标名> CURSOR FOR <SELECT 语句>`
```sql
-- 游标遍历用户并记录日志
DELIMITER //
CREATE PROCEDURE ProcessUsers()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE v_username VARCHAR(50);
    DECLARE v_email VARCHAR(100);

    DECLARE cur CURSOR FOR
        SELECT id, username, email FROM users WHERE status = 'active';

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO v_id, v_username, v_email;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO user_log (user_id, action, created_at)
        VALUES (v_id, CONCAT('Processed user: ', v_username), NOW());
    END LOOP;

    CLOSE cur;

    SELECT 'Processing complete' AS status;
END //
DELIMITER ;
```

**换行写法：游标配合临时表**
`DECLARE <游标名> CURSOR FOR <聚合查询>`
```sql
-- 游标遍历聚合结果写入临时表
DELIMITER //
CREATE PROCEDURE CategoryStats()
BEGIN
    DECLARE v_done INT DEFAULT FALSE;
    DECLARE v_category VARCHAR(50);
    DECLARE v_count INT;
    DECLARE v_avg_price DECIMAL(10, 2);

    DECLARE cur CURSOR FOR
        SELECT category, COUNT(*) AS cnt, AVG(price) AS avg_price
        FROM products
        GROUP BY category;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = TRUE;

    DROP TEMPORARY TABLE IF EXISTS temp_stats;
    CREATE TEMPORARY TABLE temp_stats (
        category VARCHAR(50),
        product_count INT,
        avg_price DECIMAL(10, 2)
    );

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO v_category, v_count, v_avg_price;
        IF v_done THEN
            LEAVE read_loop;
        END IF;

        INSERT INTO temp_stats VALUES (v_category, v_count, v_avg_price);
    END LOOP;

    CLOSE cur;

    SELECT * FROM temp_stats;
    DROP TEMPORARY TABLE IF EXISTS temp_stats;
END //
DELIMITER ;
```

---

## 异常处理

**换行写法：CONTINUE HANDLER**
`DECLARE CONTINUE HANDLER FOR <异常> BEGIN <处理> END`
```sql
-- 捕获异常后继续执行
DELIMITER //
CREATE PROCEDURE SafeInsertUser(
    IN p_username VARCHAR(50),
    IN p_email VARCHAR(100)
)
BEGIN
    DECLARE v_error VARCHAR(255) DEFAULT '';

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error = MESSAGE_TEXT;
        SELECT CONCAT('Error: ', v_error) AS error_message;
    END;

    INSERT INTO users (username, email, created_at)
    VALUES (p_username, p_email, NOW());

    IF v_error = '' THEN
        SELECT 'User inserted successfully' AS result;
    END IF;
END //
DELIMITER ;
```

**换行写法：EXIT HANDLER**
`DECLARE EXIT HANDLER FOR <异常> BEGIN <处理> END`
```sql
-- 捕获异常后退出并回滚
DELIMITER //
CREATE PROCEDURE SafeTransfer(
    IN p_from_id INT,
    IN p_to_id INT,
    IN p_amount DECIMAL(10, 2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Transfer failed, transaction rolled back' AS result;
    END;

    START TRANSACTION;

    UPDATE accounts SET balance = balance - p_amount WHERE id = p_from_id;
    UPDATE accounts SET balance = balance + p_amount WHERE id = p_to_id;

    COMMIT;
    SELECT 'Transfer completed' AS result;
END //
DELIMITER ;
```

---

## 自定义函数

**换行写法：创建函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS <返回类型> [DETERMINISTIC] BEGIN <函数体> RETURN <值> END`
```sql
-- 计算订单总金额的函数
DELIMITER //
CREATE FUNCTION CalculateOrderTotal(p_order_id INT)
RETURNS DECIMAL(12, 2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE v_total DECIMAL(12, 2);

    SELECT SUM(oi.quantity * oi.unit_price)
    INTO v_total
    FROM order_items oi
    WHERE oi.order_id = p_order_id;

    RETURN IFNULL(v_total, 0);
END //
DELIMITER ;
```

**换行写法：创建格式化函数**
`CREATE FUNCTION <函数名>(<参数>) RETURNS <返回类型> BEGIN RETURN <表达式> END`
```sql
-- 格式化金额显示的函数
DELIMITER //
CREATE FUNCTION FormatCurrency(
    p_amount DECIMAL(12, 2),
    p_currency VARCHAR(3)
)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    RETURN CONCAT(p_currency, ' ', FORMAT(p_amount, 2));
END //
DELIMITER ;
```

**单行写法：调用函数**
`SELECT <函数名>(<参数>)`
```sql
-- 使用自定义函数查询
SELECT CalculateOrderTotal(1001) AS total;
```

**单行写法：在查询中使用函数**
`SELECT <列名>, <函数名>(<列名>) AS <别名> FROM <表名>`
```sql
-- 在 SELECT 中使用函数计算年龄
SELECT name, CalculateAge(birthdate) AS age FROM employees;
```

---

## DELIMITER 使用

**单行写法：修改分隔符**
`DELIMITER <分隔符>`
```sql
-- 临时更改语句分隔符
DELIMITER //
```

**换行写法：DELIMITER 完整用法**
`DELIMITER <分隔符> <创建语句> <分隔符> DELIMITER ;`
```sql
-- 使用 DELIMITER 创建存储过程
DELIMITER //
CREATE PROCEDURE MyProc()
BEGIN
    SELECT * FROM users;
END //
DELIMITER ;
```


<!-- ============ 文档分隔线：020-mysql/003-TransactionLockMechanism.md ============ -->

# MySQL 事务与锁机制

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事务控制

**单行写法：开启事务**
`START TRANSACTION` / `BEGIN`
```sql
-- 开启事务
START TRANSACTION;
```

**换行写法：提交事务**
`COMMIT`
```sql
-- 提交事务并持久化变更
START TRANSACTION;
INSERT INTO users (username, email) VALUES ('张三', 'zhangsan@example.com');
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK`
```sql
-- 回滚事务撤销变更
ROLLBACK;
```

**换行写法：使用保存点**
`SAVEPOINT <保存点名>` / `ROLLBACK TO <保存点名>`
```sql
-- 使用保存点部分回滚
START TRANSACTION;
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

**单行写法：查看隔离级别**
`SELECT @@transaction_isolation`
```sql
-- 查看当前事务隔离级别
SELECT @@transaction_isolation;
```

**单行写法：查看旧变量名隔离级别**
`SELECT @@tx_isolation`
```sql
-- 查看旧版本隔离级别变量
SELECT @@tx_isolation;
```

**单行写法：设置会话隔离级别**
`SET SESSION TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**单行写法：设置全局隔离级别**
`SET GLOBAL TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置全局隔离级别为可序列化
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

**单行写法：通过变量设置全局隔离级别**
`SET GLOBAL transaction_isolation = '<级别>'`
```sql
-- 通过变量设置全局隔离级别
SET GLOBAL transaction_isolation = 'READ-COMMITTED';
```

**单行写法：通过变量设置会话隔离级别**
`SET SESSION transaction_isolation = '<级别>'`
```sql
-- 通过变量设置会话隔离级别
SET SESSION transaction_isolation = 'REPEATABLE-READ';
```

---

## 锁机制

**单行写法：加共享锁**
`SELECT ... LOCK IN SHARE MODE`
```sql
-- 查询时加共享锁
SELECT * FROM users WHERE id = 1 LOCK IN SHARE MODE;
```

**单行写法：加排他锁**
`SELECT ... FOR UPDATE`
```sql
-- 查询时加排他锁
SELECT * FROM users WHERE id = 1 FOR UPDATE;
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
`SELECT @@innodb_lock_wait_timeout`
```sql
-- 查看锁等待超时时间
SELECT @@innodb_lock_wait_timeout;
```

**单行写法：设置锁等待超时**
`SET SESSION innodb_lock_wait_timeout = <秒数>`
```sql
-- 设置锁等待超时为 30 秒
SET SESSION innodb_lock_wait_timeout = 30;
```

---

## 死锁检测

**单行写法：查看 InnoDB 状态**
`SHOW ENGINE INNODB STATUS`
```sql
-- 查看死锁日志
SHOW ENGINE INNODB STATUS;
```

**单行写法：开启死锁检测**
`SET GLOBAL innodb_deadlock_detect = ON`
```sql
-- 开启死锁检测
SET GLOBAL innodb_deadlock_detect = ON;
```

---

## 事务实战

**换行写法：转账事务**
`START TRANSACTION; <DML>; COMMIT;`
```sql
-- 转账事务保证原子性
START TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;
COMMIT;
```

**换行写法：条件提交**
`IF <条件> THEN COMMIT; ELSE ROLLBACK; END IF`
```sql
-- 检查余额后决定提交或回滚
START TRANSACTION;
UPDATE accounts SET balance = balance - 1000 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 1000 WHERE user_id = 2;

IF (SELECT balance FROM accounts WHERE user_id = 1) < 0 THEN
  ROLLBACK;
ELSE
  COMMIT;
END IF;
```

**换行写法：订单创建事务**
`START TRANSACTION; <DML>; SET @变量; <DML>; COMMIT;`
```sql
-- 订单创建事务包含订单和订单项
START TRANSACTION;
INSERT INTO orders (user_id, total_amount) VALUES (1, 500);
SET @order_id = LAST_INSERT_ID();
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
  (@order_id, 101, 2, 200),
  (@order_id, 102, 1, 100);
UPDATE products SET stock = stock - 3 WHERE id IN (101, 102);
COMMIT;
```

**换行写法：悲观锁查询**
`SELECT ... FOR UPDATE`
```sql
-- 先锁定再更新
SELECT * FROM users WHERE id = 1 FOR UPDATE;
UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
```

**换行写法：批量删除事务**
`START TRANSACTION; <DML>; COMMIT;`
```sql
-- 批量更新避免长事务
START TRANSACTION;
UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
UPDATE stats SET inactive_users = inactive_users + 1;
COMMIT;
```

**单行写法：分批删除**
`DELETE FROM <表名> WHERE <条件> LIMIT <N>`
```sql
-- 分批删除避免锁表
DELETE FROM logs WHERE created_at < '2023-01-01' LIMIT 1000;
```


<!-- ============ 文档分隔线：020-mysql/004-MySQLDataTypeConstraint.md ============ -->

# MySQL 数据类型与约束

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数值类型

**单行写法：定义 BIGINT 自增主键**
`<列名> BIGINT [UNSIGNED] [NOT NULL] [PRIMARY KEY] [AUTO_INCREMENT]`
```sql
-- 定义 BIGINT 无符号自增主键
id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT;
```

**单行写法：定义 TINYINT 状态枚举**
`<列名> TINYINT [UNSIGNED] [NOT NULL] [DEFAULT <默认值>]`
```sql
-- 定义 TINYINT 状态字段并设置默认值
status TINYINT NOT NULL DEFAULT 1;
```

**单行写法：定义 DECIMAL 金额字段**
`<列名> DECIMAL(<精度>, <小数位数>) [DEFAULT <默认值>]`
```sql
-- 定义金额字段避免浮点误差
balance DECIMAL(10, 2) DEFAULT 0.00;
```

**单行写法：定义 DOUBLE 浮点字段**
`<列名> <FLOAT|DOUBLE> [(<精度>, <小数位数>)]`
```sql
-- 定义测量数据浮点字段
temperature DOUBLE;
```

---

## 字符串类型

**单行写法：定义 CHAR 定长字符串**
`<列名> CHAR(<长度>) [NOT NULL]`
```sql
-- 定义国家码定长字段
country_code CHAR(2) NOT NULL;
```

**单行写法：定义 VARCHAR 变长字符串**
`<列名> VARCHAR(<最大长度>) [NOT NULL]`
```sql
-- 定义用户名变长字段
username VARCHAR(50) NOT NULL;
```

**单行写法：定义 TEXT 长文本**
`<列名> <TINYTEXT|TEXT|MEDIUMTEXT|LONGTEXT>`
```sql
-- 定义文章内容长文本字段
content TEXT;
```

---

## 日期与时间类型

**单行写法：定义 DATE 日期字段**
`<列名> DATE`
```sql
-- 定义仅保存日期的字段
birthday DATE;
```

**单行写法：定义 DATETIME 日期时间字段**
`<列名> DATETIME [NOT NULL] [DEFAULT CURRENT_TIMESTAMP]`
```sql
-- 定义业务发生时间字段
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;
```

**单行写法：定义 TIMESTAMP 自动更新字段**
`<列名> TIMESTAMP [DEFAULT CURRENT_TIMESTAMP] [ON UPDATE CURRENT_TIMESTAMP]`
```sql
-- 定义更新时间自动维护字段
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
```

---

## JSON 类型

**单行写法：定义 JSON 列**
`<列名> JSON`
```sql
-- 定义 JSON 扩展字段
profile JSON;
```

**换行写法：建表时包含 JSON 列**
`CREATE TABLE <表名> (<列定义>, <JSON 列名> JSON)`
```sql
-- 创建包含 JSON 字段的用户表
CREATE TABLE users (
  id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
  profile JSON
);
```

---

## 字符集与排序规则

**换行写法：创建数据库时指定字符集**
`CREATE DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>`
```sql
-- 创建数据库并指定 utf8mb4 字符集
CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

---

## 约束

**单行写法：非空约束**
`<列名> <类型> NOT NULL`
```sql
-- 定义必填字段
email VARCHAR(255) NOT NULL;
```

**单行写法：默认值约束**
`<列名> <类型> DEFAULT <默认值>`
```sql
-- 定义状态字段默认值为 1
status TINYINT NOT NULL DEFAULT 1;
```

**单行写法：默认值为当前时间**
`<列名> <时间类型> DEFAULT CURRENT_TIMESTAMP`
```sql
-- 定义创建时间默认值为当前时间
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;
```

**单行写法：单列唯一约束**
`UNIQUE [KEY <索引名>] (<列名>)`
```sql
-- 定义邮箱单列唯一约束
UNIQUE KEY uk_email (email);
```

**单行写法：组合唯一约束**
`UNIQUE [KEY <索引名>] (<列名1>, <列名2>[, ...])`
```sql
-- 定义租户与邮箱组合唯一约束
UNIQUE KEY uk_tenant_email (tenant_id, email);
```

**单行写法：单列主键约束**
`<列名> <类型> PRIMARY KEY`
```sql
-- 定义单列主键
id BIGINT UNSIGNED NOT NULL PRIMARY KEY;
```

**单行写法：复合主键约束**
`PRIMARY KEY (<列名1>, <列名2>[, ...])`
```sql
-- 定义复合主键
PRIMARY KEY (tenant_id, user_id);
```

**换行写法：外键约束**
`FOREIGN KEY (<列名>) REFERENCES <父表>(<父列>) [ON DELETE <行为>] [ON UPDATE <行为>]`
```sql
-- 定义外键关联并设置级联行为
FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
```

**单行写法：检查约束（非负）**
`CHECK (<条件表达式>)`
```sql
-- 定义金额必须非负的检查约束
CHECK (total_amount >= 0);
```

**单行写法：检查约束（枚举值）**
`CHECK (<列名> IN (<值1>, <值2>[, ...]))`
```sql
-- 定义状态值限定检查约束
CHECK (status IN (1, 2, 3, 4, 5));
```

**单行写法：自增约束**
`<列名> <整数类型> AUTO_INCREMENT`
```sql
-- 定义自增主键
id INT PRIMARY KEY AUTO_INCREMENT;
```

---

## 建表示例

**换行写法：完整建表语句**
`CREATE TABLE <表名> (<列定义>[, <约束定义>...])`
```sql
-- 创建用户账户表并包含唯一约束
CREATE TABLE user_account (
  id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  status TINYINT NOT NULL DEFAULT 1,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uk_email (email)
);
```


<!-- ============ 文档分隔线：020-mysql/005-MySQLIndexExecutionPlan.md ============ -->

# MySQL 索引与执行计划

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 索引创建

**单行写法：创建单列普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为用户名列创建普通索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为用户名和状态列创建复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建单列唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>)`
```sql
-- 为邮箱列创建唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

**单行写法：创建复合唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 为订单 ID 和产品 ID 创建复合唯一索引
CREATE UNIQUE INDEX idx_order_product ON order_items(order_id, product_id);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>))`
```sql
-- 为长字符串邮箱列创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
```

**单行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 为文章标题和内容创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_title_content (title, content);
```

**单行写法：通过 ALTER TABLE 添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 通过 ALTER TABLE 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：通过 ALTER TABLE 添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 通过 ALTER TABLE 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX idx_phone (phone);
```

**单行写法：通过 ALTER TABLE 添加复合索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名1>, <列名2>[, ...])`
```sql
-- 通过 ALTER TABLE 添加复合索引
ALTER TABLE users ADD INDEX idx_age_gender (age, gender);
```

---

## 索引查看与删除

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>`
```sql
-- 查看表的索引信息
SHOW INDEX FROM users;
```

**单行写法：竖向显示索引**
`SHOW INDEX FROM <表名>\G`
```sql
-- 竖向显示表索引信息
SHOW INDEX FROM users\G
```

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>`
```sql
-- 删除指定索引
DROP INDEX idx_username ON users;
```

**单行写法：删除主键索引**
`ALTER TABLE <表名> DROP PRIMARY KEY`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 复合索引与最左前缀

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>, <列3>)`
```sql
-- 为状态和创建时间创建复合索引
CREATE INDEX idx_status_created ON users(status, created_at);
```

**单行写法：使用前缀列查询（能利用索引）**
`SELECT * FROM <表名> WHERE <前缀列> <操作符> <值>`
```sql
-- 使用复合索引的第一列查询能利用索引
SELECT * FROM users WHERE status = 1;
```

**单行写法：使用前缀列组合查询（能利用索引）**
`SELECT * FROM <表名> WHERE <前缀列1> <操作符> <值> AND <前缀列2> <操作符> <值>`
```sql
-- 使用复合索引的前两列查询能利用索引
SELECT * FROM users WHERE status = 1 AND created_at > '2024-01-01';
```

**单行写法：跳过前缀列查询（不能利用索引）**
`SELECT * FROM <表名> WHERE <非前缀列> <操作符> <值>`
```sql
-- 跳过第一列查询不能利用索引
SELECT * FROM users WHERE created_at > '2024-01-01';
```

---

## EXPLAIN 执行计划

**换行写法：查看 SELECT 执行计划**
`EXPLAIN <SELECT 语句>`
```sql
-- 查看查询的执行计划
EXPLAIN
SELECT id, email
FROM user_account
WHERE email = 'a@b.com';
```

**单行写法：查看 UPDATE 执行计划**
`EXPLAIN <UPDATE 语句>`
```sql
-- 查看更新语句的执行计划
EXPLAIN UPDATE users SET status = 0 WHERE last_login_time < '2023-01-01';
```

---

## 覆盖索引

**单行写法：使用覆盖索引避免回表**
`SELECT <索引列> FROM <表名> WHERE <索引列> <操作符> <值>`
```sql
-- 查询列都在索引中避免回表
SELECT id, email FROM users WHERE email = 'test@example.com';
```

---

## 索引失效场景

**单行写法：函数导致索引失效**
`WHERE <函数>(<列名>) <操作符> <值>`
```sql
-- 对索引列使用函数导致索引失效
SELECT * FROM users WHERE DATE(created_at) = '2024-01-01';
```

**单行写法：改写为范围查询利用索引**
`WHERE <列名> >= '<起始>' AND <列名> < '<结束>'`
```sql
-- 改写为范围查询以利用索引
SELECT * FROM users WHERE created_at >= '2024-01-01' AND created_at < '2024-01-02';
```

**单行写法：隐式类型转换导致索引失效**
`WHERE <列名> = <不同类型值>`
```sql
-- 字符串列与数字比较导致索引失效
SELECT * FROM users WHERE phone = 13800138000;
```

**单行写法：使用正确类型利用索引**
`WHERE <列名> = '<字符串值>'`
```sql
-- 使用字符串值以利用索引
SELECT * FROM users WHERE phone = '13800138000';
```

**单行写法：LIKE 前置通配符导致索引失效**
`WHERE <列名> LIKE '%<模式>'`
```sql
-- 前置通配符导致索引失效
SELECT * FROM users WHERE username LIKE '%张';
```

**单行写法：LIKE 后置通配符利用索引**
`WHERE <列名> LIKE '<前缀>%'`
```sql
-- 后置通配符能利用索引
SELECT * FROM users WHERE username LIKE '张%';
```


<!-- ============ 文档分隔线：020-mysql/006-AccountPermissionManagement.md ============ -->

# MySQL 账户与权限管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 用户管理

**单行写法：创建用户允许任意主机连接**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>'`
```sql
-- 创建允许任意主机连接的用户
CREATE USER 'app_user'@'%' IDENTIFIED BY 'StrongP@ss123';
```

**单行写法：创建用户限制来源 IP 段**
`CREATE USER '<用户名>'@'<IP 段>' IDENTIFIED BY '<密码>'`
```sql
-- 创建限制来源 IP 段的用户
CREATE USER 'readonly'@'10.0.%' IDENTIFIED BY 'password';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>'`
```sql
-- 修改用户密码
ALTER USER 'app_user'@'%' IDENTIFIED BY 'NewP@ss456';
```

**单行写法：删除用户**
`DROP USER '<用户名>'@'<主机>'`
```sql
-- 删除指定用户
DROP USER 'app_user'@'%';
```

**单行写法：查看所有用户**
`SELECT user, host FROM mysql.user`
```sql
-- 查看所有用户列表
SELECT user, host FROM mysql.user;
```

---

## 权限管理

**单行写法：授予查询和插入权限**
`GRANT <权限列表> ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予查询和插入权限
GRANT SELECT, INSERT ON mydb.* TO 'app_user'@'%';
```

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>'`
```sql
-- 授予所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';
```

**单行写法：撤销权限**
`REVOKE <权限列表> ON <库>.<表> FROM '<用户名>'@'<主机>'`
```sql
-- 撤销插入权限
REVOKE INSERT ON mydb.* FROM 'app_user'@'%';
```

**单行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>'`
```sql
-- 查看用户权限
SHOW GRANTS FOR 'app_user'@'%';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES`
```sql
-- 刷新权限表
FLUSH PRIVILEGES;
```

---

## 角色管理

**单行写法：创建多个角色**
`CREATE ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 创建多个角色
CREATE ROLE 'app_read', 'app_write', 'app_admin';
```

**单行写法：授予只读角色权限**
`GRANT SELECT ON <库>.<表> TO '<角色名>'`
```sql
-- 授予只读角色权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：授予读写角色权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.<表> TO '<角色名>'`
```sql
-- 授予读写角色权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
```

**单行写法：授予管理员角色权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<角色名>'`
```sql
-- 授予管理员角色权限
GRANT ALL PRIVILEGES ON mydb.* TO 'app_admin';
```

**单行写法：将角色分配给用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>'`
```sql
-- 分配角色给用户
GRANT 'app_read' TO 'reporting_user'@'%';
```

**单行写法：设置用户默认角色**
`SET DEFAULT ROLE ALL TO '<用户名>'@'<主机>'`
```sql
-- 设置用户默认角色
SET DEFAULT ROLE ALL TO 'reporting_user'@'%';
```

**单行写法：撤销用户角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>'`
```sql
-- 撤销用户角色
REVOKE 'app_read' FROM 'reporting_user'@'%';
```

**单行写法：删除角色**
`DROP ROLE '<角色名>'[, '<角色名>'...]`
```sql
-- 删除多个角色
DROP ROLE 'app_read', 'app_write', 'app_admin';
```

---

## 密码策略

**单行写法：安装密码验证组件**
`INSTALL COMPONENT 'file://component_validate_password'`
```sql
-- 安装密码验证组件
INSTALL COMPONENT 'file://component_validate_password';
```

**单行写法：设置密码策略级别**
`SET GLOBAL validate_password.policy = <级别>`
```sql
-- 设置密码策略级别为 MEDIUM
SET GLOBAL validate_password.policy = MEDIUM;
```

**单行写法：设置密码最小长度**
`SET GLOBAL validate_password.length = <长度>`
```sql
-- 设置密码最小长度为 12
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置大小写字母数量**
`SET GLOBAL validate_password.mixed_case_count = <数量>`
```sql
-- 设置密码大小写字母数量为 1
SET GLOBAL validate_password.mixed_case_count = 1;
```

**单行写法：设置数字数量**
`SET GLOBAL validate_password.number_count = <数量>`
```sql
-- 设置密码数字数量为 1
SET GLOBAL validate_password.number_count = 1;
```

**单行写法：设置特殊字符数量**
`SET GLOBAL validate_password.special_char_count = <数量>`
```sql
-- 设置密码特殊字符数量为 1
SET GLOBAL validate_password.special_char_count = 1;
```

**单行写法：密码定期过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE INTERVAL <天数> DAY`
```sql
-- 设置密码 90 天过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
```

**单行写法：密码永不过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE NEVER`
```sql
-- 设置密码永不过期
ALTER USER 'app_user'@'%' PASSWORD EXPIRE NEVER;
```

---

## 连接限制

**单行写法：限制每小时最大连接数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_CONNECTIONS_PER_HOUR <数量>`
```sql
-- 限制每小时最大连接数为 100
ALTER USER 'app_user'@'%' WITH MAX_CONNECTIONS_PER_HOUR 100;
```

**单行写法：限制每小时最大查询数**
`ALTER USER '<用户名>'@'<主机>' WITH MAX_QUERIES_PER_HOUR <数量>`
```sql
-- 限制每小时最大查询数为 1000
ALTER USER 'app_user'@'%' WITH MAX_QUERIES_PER_HOUR 1000;
```

**单行写法：锁定账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK`
```sql
-- 锁定账户
ALTER USER 'app_user'@'%' ACCOUNT LOCK;
```

**单行写法：解锁账户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK`
```sql
-- 解锁账户
ALTER USER 'app_user'@'%' ACCOUNT UNLOCK;
```


<!-- ============ 文档分隔线：020-mysql/007-JSONTypeJSONTable.md ============ -->

# MySQL JSON 类型与 JSON_TABLE

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## JSON 数据类型

**换行写法：创建 JSON 类型列**
`CREATE TABLE <表名> (<列名> INT PRIMARY KEY, <JSON 列名> JSON)`
```sql
-- 创建包含原生 JSON 类型的表
CREATE TABLE users (
    id       INT PRIMARY KEY,
    profile  JSON
);
```

**单行写法：插入有效 JSON 对象**
`INSERT INTO <表名> VALUES (<值>, '<JSON 字符串>')`
```sql
-- 插入有效 JSON 对象数据
INSERT INTO users VALUES (1, '{"name": "Alice", "age": 30, "tags": ["dev", "go"]}');
```

**单行写法：插入 JSON 数组**
`INSERT INTO <表名> VALUES (<值>, '<JSON 数组>')`
```sql
-- 插入 JSON 数组数据
INSERT INTO users VALUES (3, '[1, 2, 3, "hello", null, true]');
```

**换行写法：插入嵌套 JSON**
`INSERT INTO <表名> VALUES (<值>, '<嵌套 JSON 字符串>')`
```sql
-- 插入嵌套结构的 JSON 数据
INSERT INTO users VALUES (4, '{
    "name": "Bob",
    "address": {
        "city": "Beijing",
        "zip": "100000"
    },
    "orders": [
        {"id": 1, "amount": 99.9},
        {"id": 2, "amount": 199.9}
    ]
}');
```

---

## JSON 提取函数

**单行写法：JSON_EXTRACT 提取值**
`JSON_EXTRACT(<JSON 列>, '<路径>')`
```sql
-- 提取 JSON 中的 name 字段值
SELECT JSON_EXTRACT(profile, '$.name') FROM users WHERE id = 1;
```

**单行写法：-> 运算符提取值**
`<JSON 列>->'<路径>'`
```sql
-- 使用 -> 运算符提取 name 字段
SELECT profile->'$.name' FROM users WHERE id = 1;
```

**单行写法：->> 运算符提取并取消引号**
`<JSON 列>->>'<路径>'`
```sql
-- 提取 name 字段并取消引号
SELECT profile->>'$.name' FROM users WHERE id = 1;
```

**单行写法：提取嵌套值**
`<JSON 列>->>'<嵌套路径>'`
```sql
-- 提取嵌套的 address.city 字段
SELECT profile->>'$.address.city' FROM users WHERE id = 4;
```

**单行写法：提取数组元素**
`<JSON 列>->'<数组路径>'`
```sql
-- 提取 orders 数组第一个元素的 amount
SELECT profile->'$.orders[0].amount' FROM users WHERE id = 4;
```

**单行写法：提取数组所有元素**
`<JSON 列>->'<数组路径>[*]'`
```sql
-- 提取 tags 数组的所有元素
SELECT profile->'$.tags[*]' FROM users WHERE id = 1;
```

---

## JSON 修改函数

**单行写法：JSON_SET 设置值**
`JSON_SET(<JSON 列>, '<路径>', <值>[, '<路径>', <值>...])`
```sql
-- 设置 age 字段值（存在则更新不存在则创建）
UPDATE users SET profile = JSON_SET(profile, '$.age', 31) WHERE id = 1;
```

**单行写法：JSON_INSERT 插入值**
`JSON_INSERT(<JSON 列>, '<路径>', <值>)`
```sql
-- 插入 email 字段（仅不存在时创建）
UPDATE users SET profile = JSON_INSERT(profile, '$.email', 'alice@example.com') WHERE id = 1;
```

**单行写法：JSON_REPLACE 替换值**
`JSON_REPLACE(<JSON 列>, '<路径>', <值>)`
```sql
-- 替换 age 字段值（仅存在时更新）
UPDATE users SET profile = JSON_REPLACE(profile, '$.age', 32) WHERE id = 1;
```

**单行写法：JSON_REMOVE 删除值**
`JSON_REMOVE(<JSON 列>, '<路径>')`
```sql
-- 删除 tags 字段
UPDATE users SET profile = JSON_REMOVE(profile, '$.tags') WHERE id = 1;
```

**单行写法：JSON_ARRAY_APPEND 追加数组元素**
`JSON_ARRAY_APPEND(<JSON 列>, '<路径>', <值>)`
```sql
-- 向 tags 数组追加元素
UPDATE users SET profile = JSON_ARRAY_APPEND(profile, '$.tags', 'java') WHERE id = 1;
```

**单行写法：JSON_MERGE_PATCH 合并对象**
`JSON_MERGE_PATCH(<JSON 列>, '<JSON 对象>')`
```sql
-- 合并 JSON 对象（覆盖同 key）
UPDATE users SET profile = JSON_MERGE_PATCH(profile, '{"age": 33, "level": "senior"}') WHERE id = 1;
```

---

## JSON 查询与搜索函数

**单行写法：JSON_CONTAINS 判断包含值**
`JSON_CONTAINS(<JSON 列>, '<JSON 值>'[, '<路径>'])`
```sql
-- 判断 tags 数组是否包含 dev
SELECT * FROM users WHERE JSON_CONTAINS(profile->'$.tags', '"dev"');
```

**单行写法：JSON_CONTAINS_PATH 判断包含路径**
`JSON_CONTAINS_PATH(<JSON 列>, 'one|all', '<路径>'[, '<路径>'...])`
```sql
-- 判断是否包含 email 路径
SELECT * FROM users WHERE JSON_CONTAINS_PATH(profile, 'one', '$.email');
```

**单行写法：JSON_SEARCH 搜索值返回路径**
`JSON_SEARCH(<JSON 列>, 'one|all', '<值>')`
```sql
-- 搜索 Alice 值并返回路径
SELECT JSON_SEARCH(profile, 'one', 'Alice') FROM users;
```

**单行写法：JSON_KEYS 获取所有 key**
`JSON_KEYS(<JSON 列>[, '<路径>'])`
```sql
-- 获取 JSON 对象的所有 key
SELECT JSON_KEYS(profile) FROM users WHERE id = 1;
```

**单行写法：JSON_LENGTH 获取长度**
`JSON_LENGTH(<JSON 列>[, '<路径>'])`
```sql
-- 获取 tags 数组的长度
SELECT JSON_LENGTH(profile->'$.tags') FROM users WHERE id = 1;
```

**单行写法：JSON_TYPE 获取类型**
`JSON_TYPE(<JSON 值>)`
```sql
-- 获取 name 字段的数据类型
SELECT JSON_TYPE(profile->'$.name') FROM users WHERE id = 1;
```

**单行写法：JSON_VALID 判断有效性**
`JSON_VALID('<JSON 字符串>')`
```sql
-- 判断字符串是否为有效 JSON
SELECT JSON_VALID('{"a":1}');
```

---

## JSON_TABLE

**换行写法：JSON_TABLE 基本语法**
`JSON_TABLE(<JSON 文档>, <路径> COLUMNS (<列定义>) ) [AS] <别名>`
```sql
-- 将 JSON 数组展开为关系表
SELECT
    o.id AS order_id,
    jt.product_id,
    jt.name,
    jt.qty,
    jt.price,
    jt.qty * jt.price AS subtotal
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        qty        INT PATH '$.qty',
        price      DECIMAL(10,2) PATH '$.price'
    )
) AS jt;
```

**换行写法：NESTED PATH 嵌套展开**
`NESTED PATH '<路径>' COLUMNS (<列定义>)`
```sql
-- 嵌套 JSON 结构展开
SELECT
    o.id,
    jt.product_id,
    jt.name,
    nt.color,
    nt.stock
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        product_id INT PATH '$.product_id',
        name       VARCHAR(50) PATH '$.name',
        NESTED PATH '$.variants[*]' COLUMNS (
            color VARCHAR(20) PATH '$.color',
            stock INT PATH '$.stock'
        )
    )
) AS jt;
```

**换行写法：ORDINALITY 列生成行号**
`<列名> FOR ORDINALITY`
```sql
-- 自动生成行号
SELECT
    jt.row_num,
    jt.name
FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        row_num FOR ORDINALITY,
        name VARCHAR(50) PATH '$.name'
    )
) AS jt
WHERE o.id = 1;
```

**换行写法：处理缺失值**
`<列名> <类型> PATH '<路径>' DEFAULT '<默认值>' ON EMPTY`
```sql
-- 缺失值使用默认值
SELECT * FROM orders o,
JSON_TABLE(
    o.items,
    '$[*]' COLUMNS (
        name VARCHAR(50) PATH '$.name',
        discount DECIMAL(5,2) PATH '$.discount' DEFAULT '0.00' ON EMPTY
    )
) AS jt;
```

---

## JSON 索引优化

**换行写法：虚拟列索引**
`ALTER TABLE <表名> ADD COLUMN <列名> <类型> GENERATED ALWAYS AS (<表达式>) VIRTUAL, ADD INDEX <索引名> (<列名>)`
```sql
-- 为 JSON 字段创建虚拟列加索引
ALTER TABLE users
ADD COLUMN name_virtual VARCHAR(50)
    GENERATED ALWAYS AS (JSON_UNQUOTE(profile->'$.name')) VIRTUAL,
ADD INDEX idx_name (name_virtual);
```

**单行写法：查询虚拟列索引**
`SELECT * FROM <表名> WHERE <虚拟列名> = <值>`
```sql
-- 查询走虚拟列索引
SELECT * FROM users WHERE name_virtual = 'Alice';
```

**换行写法：函数索引**
`ALTER TABLE <表名> ADD INDEX <索引名> ((<表达式>))`
```sql
-- 直接创建函数索引（MySQL 8.0+）
ALTER TABLE users
ADD INDEX idx_json_name ((CAST(profile->>'$.name' AS CHAR(50))));
```

**换行写法：多值索引**
`ALTER TABLE <表名> ADD INDEX <索引名> ((CAST(<JSON 列> AS <类型> ARRAY)))`
```sql
-- 为 JSON 数组创建多值索引（MySQL 8.0.17+）
ALTER TABLE users
ADD INDEX idx_tags ((CAST(profile->'$.tags' AS CHAR(50) ARRAY)));
```

**单行写法：MEMBER OF 查询**
`<值> MEMBER OF(<JSON 列>)`
```sql
-- 使用 MEMBER OF 查询数组包含值
SELECT * FROM users WHERE 'dev' MEMBER OF(profile->'$.tags');
```

**单行写法：JSON_OVERLAPS 查询**
`JSON_OVERLAPS(<JSON 列>, '<JSON 数组>')`
```sql
-- 使用 JSON_OVERLAPS 查询数组交集
SELECT * FROM users WHERE JSON_OVERLAPS(profile->'$.tags', '["dev", "java"]');
```


<!-- ============ 文档分隔线：020-mysql/008-SQLFunctionAndAdvancedQuery.md ============ -->

# MySQL SQL 函数与高级查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 字符串函数

**单行写法：CONCAT 连接字符串**
`CONCAT(<字符串1>[, <字符串2>...])`
```sql
-- 连接用户名和邮箱
SELECT CONCAT(username, ' (', email, ')') AS user_info FROM users;
```

**单行写法：CONCAT_WS 带分隔符连接**
`CONCAT_WS('<分隔符>', <字符串1>[, <字符串2>...])`
```sql
-- 带分隔符连接地址字段
SELECT CONCAT_WS('-', province, city, district) AS full_address FROM addresses;
```

**单行写法：LENGTH 字节长度**
`LENGTH(<字符串>)`
```sql
-- 获取用户名的字节长度
SELECT LENGTH(username) AS name_bytes FROM users;
```

**单行写法：CHAR_LENGTH 字符长度**
`CHAR_LENGTH(<字符串>)`
```sql
-- 获取用户名的字符长度
SELECT CHAR_LENGTH(username) AS name_chars FROM users;
```

**单行写法：SUBSTRING 截取字符串**
`SUBSTRING(<字符串>, <起始位置>[, <长度>])`
```sql
-- 截取手机号前 3 位
SELECT SUBSTRING(phone, 1, 3) AS phone_prefix FROM users;
```

**单行写法：LEFT 从左截取**
`LEFT(<字符串>, <长度>)`
```sql
-- 从左截取用户名前 2 位
SELECT LEFT(username, 2) FROM users;
```

**单行写法：RIGHT 从右截取**
`RIGHT(<字符串>, <长度>)`
```sql
-- 从右截取用户名后 2 位
SELECT RIGHT(username, 2) FROM users;
```

**单行写法：TRIM 去除首尾空格**
`TRIM(<字符串>)`
```sql
-- 去除字符串首尾空格
SELECT TRIM(' Hello ');
```

**单行写法：LOWER 转小写**
`LOWER(<字符串>)`
```sql
-- 将邮箱转为小写
SELECT LOWER(email) AS email_lower FROM users;
```

**单行写法：UPPER 转大写**
`UPPER(<字符串>)`
```sql
-- 将用户名转为大写
SELECT UPPER(username) AS name_upper FROM users;
```

**单行写法：REPLACE 替换字符串**
`REPLACE(<字符串>, '<旧子串>', '<新子串>')`
```sql
-- 替换字符串中的字符
SELECT REPLACE('Hello', 'l', 'w');
```

**单行写法：REVERSE 反转字符串**
`REVERSE(<字符串>)`
```sql
-- 反转字符串
SELECT REVERSE('Hello');
```

**单行写法：LPAD 左填充**
`LPAD(<字符串>, <长度>, '<填充字符>')`
```sql
-- 左填充数字到 3 位
SELECT LPAD('5', 3, '0');
```

**单行写法：RPAD 右填充**
`RPAD(<字符串>, <长度>, '<填充字符>')`
```sql
-- 右填充字符串到 5 位
SELECT RPAD('5', 5, '0');
```

**单行写法：INSTR 查找子串位置**
`INSTR(<字符串>, '<子串>')`
```sql
-- 查找子串位置
SELECT INSTR('Hello', 'll');
```

---

## 日期时间函数

**单行写法：NOW 当前日期时间**
`NOW()`
```sql
-- 获取当前日期时间
SELECT NOW() AS now;
```

**单行写法：CURDATE 当前日期**
`CURDATE()`
```sql
-- 获取当前日期
SELECT CURDATE() AS today;
```

**单行写法：CURTIME 当前时间**
`CURTIME()`
```sql
-- 获取当前时间
SELECT CURTIME() AS current_time;
```

**单行写法：DATE 提取日期**
`DATE(<日期时间>)`
```sql
-- 提取日期部分
SELECT DATE('2024-01-15 10:30:00');
```

**单行写法：TIME 提取时间**
`TIME(<日期时间>)`
```sql
-- 提取时间部分
SELECT TIME('2024-01-15 10:30:00');
```

**单行写法：YEAR 提取年份**
`YEAR(<日期>)`
```sql
-- 提取当前年份
SELECT YEAR(NOW());
```

**单行写法：MONTH 提取月份**
`MONTH(<日期>)`
```sql
-- 提取当前月份
SELECT MONTH(NOW());
```

**单行写法：DAY 提取日**
`DAY(<日期>)`
```sql
-- 提取当前日
SELECT DAY(NOW());
```

**单行写法：HOUR 提取小时**
`HOUR(<时间>)`
```sql
-- 提取当前小时
SELECT HOUR(NOW());
```

**单行写法：MINUTE 提取分钟**
`MINUTE(<时间>)`
```sql
-- 提取当前分钟
SELECT MINUTE(NOW());
```

**单行写法：SECOND 提取秒**
`SECOND(<时间>)`
```sql
-- 提取当前秒
SELECT SECOND(NOW());
```

**单行写法：DATE_FORMAT 格式化日期**
`DATE_FORMAT(<日期>, '<格式>')`
```sql
-- 格式化日期显示
SELECT DATE_FORMAT(NOW(), '%Y年%m月%d日 %H:%i:%s') AS formatted;
```

**单行写法：DATE_ADD 日期加**
`DATE_ADD(<日期>, INTERVAL <值> <单位>)`
```sql
-- 日期加 7 天
SELECT DATE_ADD(NOW(), INTERVAL 7 DAY) AS next_week;
```

**单行写法：DATE_SUB 日期减**
`DATE_SUB(<日期>, INTERVAL <值> <单位>)`
```sql
-- 日期减 1 个月
SELECT DATE_SUB(NOW(), INTERVAL 1 MONTH) AS last_month;
```

**单行写法：DATEDIFF 日期差**
`DATEDIFF(<日期1>, <日期2>)`
```sql
-- 计算注册至今天数
SELECT DATEDIFF(NOW(), created_at) AS days_since_join FROM users;
```

**单行写法：TIMESTAMPDIFF 时间差**
`TIMESTAMPDIFF(<单位>, <开始>, <结束>)`
```sql
-- 计算注册至今年数
SELECT TIMESTAMPDIFF(YEAR, created_at, NOW()) AS years_since_join FROM users;
```

**单行写法：计算年龄**
`TIMESTAMPDIFF(YEAR, <生日列>, NOW())`
```sql
-- 根据生日计算年龄
SELECT TIMESTAMPDIFF(YEAR, birthday, NOW()) AS age FROM users;
```

**单行写法：DAYOFWEEK 星期几**
`DAYOFWEEK(<日期>)`
```sql
-- 获取星期几
SELECT DAYOFWEEK(NOW());
```

**单行写法：LAST_DAY 月份最后一天**
`LAST_DAY(<日期>)`
```sql
-- 获取月份最后一天
SELECT LAST_DAY('2024-01-15');
```

---

## 数值函数

**单行写法：ABS 绝对值**
`ABS(<数值>)`
```sql
-- 获取绝对值
SELECT ABS(-10);
```

**单行写法：ROUND 四舍五入**
`ROUND(<数值>[, <小数位>])`
```sql
-- 四舍五入保留 2 位小数
SELECT ROUND(price, 2) AS rounded FROM products;
```

**单行写法：CEIL 向上取整**
`CEIL(<数值>)`
```sql
-- 向上取整
SELECT CEIL(price) AS ceil_price FROM products;
```

**单行写法：FLOOR 向下取整**
`FLOOR(<数值>)`
```sql
-- 向下取整
SELECT FLOOR(price) AS floor_price FROM products;
```

**单行写法：MOD 取模**
`MOD(<数值1>, <数值2>)`
```sql
-- 取模运算
SELECT MOD(10, 3);
```

**单行写法：POW 幂运算**
`POW(<底数>, <指数>)`
```sql
-- 幂运算
SELECT POW(2, 3);
```

**单行写法：SQRT 平方根**
`SQRT(<数值>)`
```sql
-- 平方根
SELECT SQRT(16);
```

**单行写法：RAND 随机数**
`RAND()`
```sql
-- 随机排序取 5 行
SELECT * FROM users ORDER BY RAND() LIMIT 5;
```

**单行写法：TRUNCATE 截断**
`TRUNCATE(<数值>, <小数位>)`
```sql
-- 截断到 3 位小数
SELECT TRUNCATE(3.14159, 3);
```

**单行写法：SIGN 符号**
`SIGN(<数值>)`
```sql
-- 获取数值符号
SELECT SIGN(-10);
```

---

## 条件函数

**单行写法：IF 条件判断**
`IF(<条件>, <真值>, <假值>)`
```sql
-- 根据年龄判断成人或未成年
SELECT username, age, IF(age >= 18, '成人', '未成年') AS age_desc FROM users;
```

**单行写法：IFNULL NULL 替换**
`IFNULL(<值>, <默认值>)`
```sql
-- 替换 NULL 值为默认值
SELECT username, IFNULL(email, '未填写') AS email FROM users;
```

**单行写法：嵌套 IFNULL**
`IFNULL(<值>, IFNULL(<值2>, <默认值>))`
```sql
-- 嵌套 IFNULL 处理多个可能为空的字段
SELECT IFNULL(phone, IFNULL(telephone, '无')) AS contact FROM users;
```

**单行写法：NULLIF 相等返回 NULL**
`NULLIF(<值1>, <值2>)`
```sql
-- 两值相等返回 NULL
SELECT NULLIF(a, b);
```

**换行写法：CASE WHEN 多条件判断**
`CASE WHEN <条件> THEN <值> [WHEN ...] [ELSE <值>] END`
```sql
-- 多条件判断年龄分组
SELECT
  username,
  age,
  CASE
    WHEN age < 18 THEN '未成年'
    WHEN age < 30 THEN '青年'
    WHEN age < 60 THEN '中年'
    ELSE '老年'
  END AS age_group
FROM users;
```

**换行写法：CASE 表达式等值匹配**
`CASE <表达式> WHEN <值> THEN <结果> [WHEN ...] [ELSE <结果>] END`
```sql
-- 等值匹配状态值
SELECT
  username,
  CASE status
    WHEN 1 THEN '正常'
    WHEN 2 THEN '冻结'
    WHEN 0 THEN '禁用'
    ELSE '未知'
  END AS status_desc
FROM users;
```

**换行写法：CASE 聚合条件计数**
`SUM(CASE WHEN <条件> THEN 1 ELSE 0 END)`
```sql
-- 条件计数统计不同状态数量
SELECT
  SUM(CASE WHEN status = 1 THEN 1 ELSE 0 END) AS active_count,
  SUM(CASE WHEN status = 0 THEN 1 ELSE 0 END) AS inactive_count
FROM users;
```

---

## 类型转换与系统函数

**单行写法：CAST 类型转换**
`CAST(<值> AS <类型>)`
```sql
-- 将价格转换为字符类型
SELECT CAST(price AS CHAR) FROM products;
```

**单行写法：CONVERT 类型转换**
`CONVERT(<值>, <类型>)`
```sql
-- 将价格转换为 DECIMAL 类型
SELECT CONVERT(price, DECIMAL(10,2)) FROM products;
```

**单行写法：FORMAT 格式化数字**
`FORMAT(<数值>, <小数位>)`
```sql
-- 格式化数字带千位分隔符
SELECT FORMAT(price, 2) AS price_formatted FROM products;
```

**单行写法：MD5 哈希**
`MD5('<字符串>')`
```sql
-- 计算 MD5 哈希
SELECT MD5('password') AS md5_hash;
```

**单行写法：SHA1 哈希**
`SHA1('<字符串>')`
```sql
-- 计算 SHA1 哈希
SELECT SHA1('password') AS sha1_hash;
```

**单行写法：SHA2 哈希**
`SHA2('<字符串>', <长度>)`
```sql
-- 计算 SHA256 哈希
SELECT SHA2('password', 256) AS sha256_hash;
```

**单行写法：UUID 生成**
`UUID()`
```sql
-- 生成 UUID
SELECT UUID() AS uuid;
```

**单行写法：SET 用户变量**
`SET @<变量名> = <值>`
```sql
-- 设置用户变量
SET @total = 0;
```

**单行写法：SELECT 变量累加**
`SELECT @<变量名> := @<变量名> + <表达式>`
```sql
-- 用户变量累加
SELECT @total := @total + price FROM products;
```

---

## 子查询

**单行写法：标量子查询最大值**
`SELECT * FROM <表名> WHERE <列名> = (SELECT MAX(<列名>) FROM <表名>)`
```sql
-- 查询年龄最大的用户
SELECT * FROM users WHERE age = (SELECT MAX(age) FROM users);
```

**单行写法：标量子查询平均值**
`SELECT * FROM <表名> WHERE <列名> > (SELECT AVG(<列名>) FROM <表名>)`
```sql
-- 查询年龄大于平均年龄的用户
SELECT * FROM users WHERE age > (SELECT AVG(age) FROM users);
```

**单行写法：用子查询更新**
`UPDATE <表名> SET <列名> = (SELECT <聚合> FROM <表名>) WHERE <条件>`
```sql
-- 用子查询结果更新字段
UPDATE users SET age = (SELECT MAX(age) FROM users) + 1 WHERE id = 1;
```

**单行写法：IN 子查询**
`WHERE <列名> IN (SELECT <列名> FROM <表名>)`
```sql
-- 查询属于 VIP 用户表的用户
SELECT * FROM users WHERE id IN (SELECT user_id FROM vip_users);
```

**单行写法：NOT IN 子查询**
`WHERE <列名> NOT IN (SELECT <列名> FROM <表名>)`
```sql
-- 查询不在黑名单中的用户
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM blocked_users);
```

**单行写法：ANY 子查询**
`WHERE <列名> <操作符> ANY (SELECT ...)`
```sql
-- 满足子查询中任意一个值
SELECT * FROM products WHERE price > ANY (SELECT price FROM products WHERE category_id = 1);
```

**单行写法：ALL 子查询**
`WHERE <列名> <操作符> ALL (SELECT ...)`
```sql
-- 满足子查询中所有值
SELECT * FROM products WHERE price > ALL (SELECT price FROM products WHERE status = 0);
```

**换行写法：EXISTS 子查询**
`WHERE EXISTS (SELECT 1 FROM <表名> WHERE <条件>)`
```sql
-- 查询有订单的用户
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

**换行写法：NOT EXISTS 子查询**
`WHERE NOT EXISTS (SELECT 1 FROM <表名> WHERE <条件>)`
```sql
-- 查询没有订单的用户
SELECT * FROM users u WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

**换行写法：FROM 子查询作为临时表**
`SELECT * FROM (SELECT ...) AS <别名>`
```sql
-- 子查询作为临时表查询
SELECT * FROM (SELECT * FROM users WHERE status = 1) AS active_users;
```

**换行写法：分组统计子查询**
`SELECT * FROM (SELECT <列名>, <聚合> FROM <表名> GROUP BY <列名>) AS <别名>`
```sql
-- 分组统计子查询
SELECT * FROM (
  SELECT status, COUNT(*) AS count, AVG(age) AS avg_age
  FROM users
  GROUP BY status
) AS stats;
```

**换行写法：SELECT 列子查询**
`SELECT <列名>, (SELECT ...) AS <别名>`
```sql
-- 列子查询统计订单数
SELECT
  u.id,
  u.username,
  (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS order_count
FROM users u;
```

**换行写法：SELECT 列子查询最新时间**
`SELECT <列名>, (SELECT MAX(<列名>) FROM <表名> WHERE <条件>) AS <别名>`
```sql
-- 查询用户最新订单时间
SELECT
  u.id,
  u.username,
  (SELECT MAX(created_at) FROM orders WHERE user_id = u.id) AS last_order_time
FROM users u;
```

---

## 多表查询

**换行写法：两表内连接**
`SELECT <列名> FROM <表1> [AS <别名>] INNER JOIN <表2> [AS <别名>] ON <条件>`
```sql
-- 两表内连接查询
SELECT u.username, o.order_no, o.total_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

**换行写法：多表内连接**
`SELECT <列名> FROM <表1> JOIN <表2> ON <条件> JOIN <表3> ON <条件>`
```sql
-- 多表内连接查询
SELECT u.username, o.order_no, p.product_name, oi.quantity
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;
```

**换行写法：USING 简写内连接**
`SELECT <列名> FROM <表1> INNER JOIN <表2> USING (<列名>)`
```sql
-- 使用 USING 简写连接条件
SELECT u.username, o.order_no
FROM users u
INNER JOIN orders o USING (user_id);
```

**换行写法：左连接**
`SELECT <列名> FROM <表1> LEFT JOIN <表2> ON <条件>`
```sql
-- 左连接查询左表全部数据
SELECT u.username, o.order_no, o.total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

**换行写法：左连接分组统计**
`SELECT <列名>, COUNT(<列名>) FROM <表1> LEFT JOIN <表2> ON <条件> GROUP BY <列名>`
```sql
-- 左连接分组统计订单数
SELECT u.username, COUNT(o.id) AS order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;
```

**换行写法：左连接找出无关联数据**
`SELECT <列名> FROM <表1> LEFT JOIN <表2> ON <条件> WHERE <表2.列> IS NULL`
```sql
-- 找出没有订单的用户
SELECT u.*
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

**换行写法：右连接**
`SELECT <列名> FROM <表1> RIGHT JOIN <表2> ON <条件>`
```sql
-- 右连接查询右表全部数据
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

**换行写法：自连接**
`SELECT <列名> FROM <表> [AS <别名1>] JOIN <表> [AS <别名2>] ON <条件>`
```sql
-- 员工与经理自连接
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**换行写法：UNION 实现全连接**
`SELECT ... LEFT JOIN ... UNION SELECT ... RIGHT JOIN ...`
```sql
-- MySQL 用 UNION 实现 FULL OUTER JOIN
SELECT u.username, o.order_no
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT u.username, o.order_no
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

**换行写法：交叉连接**
`SELECT <列名> FROM <表1> CROSS JOIN <表2>`
```sql
-- 笛卡尔积交叉连接
SELECT u.username, p.product_name
FROM users u
CROSS JOIN products p;
```

---

## UNION 合并查询

**换行写法：UNION 去重合并**
`SELECT ... UNION SELECT ...`
```sql
-- 合并结果集并去重
SELECT username FROM users WHERE status = 1
UNION
SELECT username FROM users WHERE age > 30;
```

**换行写法：UNION ALL 保留重复合并**
`SELECT ... UNION ALL SELECT ...`
```sql
-- 合并结果集保留重复
SELECT username FROM users WHERE status = 1
UNION ALL
SELECT username FROM users WHERE age > 30;
```


<!-- ============ 文档分隔线：020-mysql/009-SQLDataOperationQuery.md ============ -->

# MySQL SQL 数据操作与查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 插入数据

**单行写法：指定列插入单行**
`INSERT INTO <表名> (<列名>[, <列名>...]) VALUES (<值>[, <值>...])`
```sql
-- 指定列插入单行数据
INSERT INTO users (id, username, email, password, age)
VALUES (1, '张三', 'zhangsan@example.com', 'encrypted_pass', 25);
```

**单行写法：省略自增列插入**
`INSERT INTO <表名> (<非自增列>[, ...]) VALUES (<值>[, ...])`
```sql
-- 省略自增主键列插入数据
INSERT INTO users (username, email, password, age)
VALUES ('张三', 'zhangsan@example.com', 'encrypted_pass', 25);
```

**换行写法：SET 语法插入**
`INSERT INTO <表名> SET <列名> = <值>[, <列名> = <值>...]`
```sql
-- 使用 SET 形式插入数据
INSERT INTO users SET
  username = '李四',
  email = 'lisi@example.com',
  password = 'encrypted_pass',
  age = 30;
```

**换行写法：批量插入多行**
`INSERT INTO <表名> (<列名>) VALUES (<值1>), (<值2>)[, ...]`
```sql
-- 批量插入多行数据
INSERT INTO users (username, email, password, age) VALUES
('王五', 'wangwu@example.com', 'pass1', 28),
('赵六', 'zhaoliu@example.com', 'pass2', 32),
('钱七', 'qianqi@example.com', 'pass3', 27);
```

**换行写法：插入查询结果**
`INSERT INTO <表名> (<列名>) SELECT <列名> FROM <源表> [WHERE <条件>]`
```sql
-- 从旧表迁移符合条件的数据
INSERT INTO users (username, email, password, age)
SELECT username, email, password, age FROM old_users WHERE status = 1;
```

**换行写法：插入或更新**
`INSERT INTO <表名> (<列名>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列名> = <值>`
```sql
-- 主键冲突时更新指定字段
INSERT INTO users (id, username, email) VALUES (1, '张三', 'new@example.com')
ON DUPLICATE KEY UPDATE email = 'new@example.com', updated_at = NOW();
```

**单行写法：忽略冲突插入**
`INSERT IGNORE INTO <表名> (<列名>) VALUES (<值>)`
```sql
-- 主键冲突时跳过插入
INSERT IGNORE INTO users (username, email) VALUES ('张三', 'test@example.com');
```

**单行写法：替换插入**
`REPLACE INTO <表名> (<列名>) VALUES (<值>)`
```sql
-- 主键冲突时删除原行再插入
REPLACE INTO users (id, username, email) VALUES (1, '张三', 'new@example.com');
```

**单行写法：获取自增 ID**
`SELECT LAST_INSERT_ID();`
```sql
-- 插入后获取自增主键值
SELECT LAST_INSERT_ID();
```

---

## 更新数据

**单行写法：更新单列**
`UPDATE <表名> SET <列名> = <值> WHERE <条件>`
```sql
-- 更新指定行的单列
UPDATE users SET age = 26 WHERE id = 1;
```

**单行写法：基于原值更新**
`UPDATE <表名> SET <列名> = <列名> <运算符> <值> WHERE <条件>`
```sql
-- 基于原值进行累加更新
UPDATE users SET age = age + 1 WHERE age < 30;
```

**换行写法：多列更新**
`UPDATE <表名> SET <列名> = <值>[, <列名> = <值>...] WHERE <条件>`
```sql
-- 同时更新多个字段
UPDATE users
SET age = 27, email = 'new@example.com', updated_at = NOW()
WHERE id = 1;
```

**换行写法：JOIN 关联更新**
`UPDATE <表1> [AS <别名>] JOIN <表2> [AS <别名>] ON <条件> SET <列名> = <值>`
```sql
-- 关联其他表更新数据
UPDATE users u
JOIN user_profiles p ON u.id = p.user_id
SET u.avatar = p.avatar_url, u.status = p.status
WHERE u.id = 1;
```

**换行写法：子查询更新**
`UPDATE <表名> SET <列名> = (SELECT <聚合> FROM <表> WHERE <条件>)`
```sql
-- 用子查询结果更新字段
UPDATE users
SET balance = (SELECT SUM(amount) FROM orders WHERE user_id = users.id)
WHERE id = 1;
```

---

## 删除数据

**单行写法：条件删除**
`DELETE FROM <表名> WHERE <条件>`
```sql
-- 删除符合条件的行
DELETE FROM users WHERE id = 1;
```

**单行写法：范围删除**
`DELETE FROM <表名> WHERE <条件1> AND <条件2>`
```sql
-- 删除符合多条件的行
DELETE FROM users WHERE status = 0 AND created_at < '2024-01-01';
```

**单行写法：排序后删除指定行数**
`DELETE FROM <表名> ORDER BY <列名> [ASC|DESC] LIMIT <行数>`
```sql
-- 按排序删除前 N 行
DELETE FROM users ORDER BY created_at DESC LIMIT 10;
```

**换行写法：JOIN 关联删除**
`DELETE <别名> FROM <表1> [AS <别名>] JOIN <表2> [AS <别名>] ON <条件> WHERE <条件>`
```sql
-- 关联其他表删除数据
DELETE u FROM users u
JOIN inactive_users i ON u.email = i.email
WHERE u.status = 0;
```

**换行写法：子查询删除**
`DELETE FROM <表名> WHERE <列名> IN (SELECT <列名> FROM <表> WHERE <条件>)`
```sql
-- 用子查询结果删除数据
DELETE FROM users WHERE id IN (SELECT user_id FROM old_users WHERE created_at < '2023-01-01');
```

**单行写法：清空表**
`TRUNCATE TABLE <表名>`
```sql
-- 清空表数据并重置自增值
TRUNCATE TABLE users;
```

---

## 基础查询

**单行写法：查询所有列**
`SELECT * FROM <表名>`
```sql
-- 查询表中所有字段
SELECT * FROM users;
```

**单行写法：查询指定列**
`SELECT <列名>[, <列名>...] FROM <表名>`
```sql
-- 查询指定列数据
SELECT id, username, email FROM users;
```

**单行写法：列别名**
`SELECT <列名> [AS] <别名>`
```sql
-- 使用别名查询字段
SELECT username AS name, email AS "邮箱地址" FROM users;
```

**单行写法：计算列别名**
`SELECT <表达式> AS <别名>`
```sql
-- 计算列并设置别名
SELECT price, quantity, price * quantity AS total FROM order_items;
```

**单行写法：单列去重**
`SELECT DISTINCT <列名> FROM <表名>`
```sql
-- 查询单列去重结果
SELECT DISTINCT status FROM users;
```

**单行写法：多列去重**
`SELECT DISTINCT <列名1>, <列名2>[, ...] FROM <表名>`
```sql
-- 查询多列组合去重结果
SELECT DISTINCT province, city FROM addresses;
```

---

## 条件查询

**单行写法：大于比较**
`WHERE <列名> > <值>`
```sql
-- 查询年龄大于 25 的用户
SELECT * FROM users WHERE age > 25;
```

**单行写法：大于等于比较**
`WHERE <列名> >= <值>`
```sql
-- 查询年龄大于等于 25 的用户
SELECT * FROM users WHERE age >= 25;
```

**单行写法：小于比较**
`WHERE <列名> < <值>`
```sql
-- 查询年龄小于 30 的用户
SELECT * FROM users WHERE age < 30;
```

**单行写法：不等于比较**
`WHERE <列名> <!=|<>> <值>`
```sql
-- 查询年龄不等于 25 的用户
SELECT * FROM users WHERE age != 25;
```

**单行写法：AND 逻辑与**
`WHERE <条件1> AND <条件2>`
```sql
-- 查询同时满足多条件的用户
SELECT * FROM users WHERE age > 25 AND status = 1;
```

**单行写法：OR 逻辑或**
`WHERE <条件1> OR <条件2>`
```sql
-- 查询满足任一条件的用户
SELECT * FROM users WHERE status = 1 OR status = 2;
```

**单行写法：NOT 逻辑非**
`WHERE NOT <条件>`
```sql
-- 查询不满足条件的用户
SELECT * FROM users WHERE NOT status = 0;
```

**换行写法：括号组合条件**
`WHERE (<条件1> AND <条件2>) OR (<条件3> AND <条件4>)`
```sql
-- 使用括号组合复杂条件
SELECT * FROM users
WHERE (age > 25 AND status = 1) OR (age < 20 AND status = 2);
```

**单行写法：数值范围查询**
`WHERE <列名> [NOT] BETWEEN <起始> AND <结束>`
```sql
-- 查询年龄在 20 到 30 之间的用户
SELECT * FROM users WHERE age BETWEEN 20 AND 30;
```

**单行写法：日期范围查询**
`WHERE <日期列> BETWEEN '<起始日期>' AND '<结束日期>'`
```sql
-- 查询指定日期范围内的用户
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

**单行写法：IN 多值匹配**
`WHERE <列名> [NOT] IN (<值1>, <值2>[, ...])`
```sql
-- 查询状态为指定值的用户
SELECT * FROM users WHERE status IN (1, 2, 3);
```

**单行写法：IN 子查询**
`WHERE <列名> IN (SELECT <列名> FROM <表名>)`
```sql
-- 查询属于 VIP 用户表的用户
SELECT * FROM users WHERE id IN (SELECT user_id FROM vip_users);
```

**单行写法：前缀模糊查询**
`WHERE <列名> [NOT] LIKE '<前缀>%'`
```sql
-- 查询以指定字符开头的用户名
SELECT * FROM users WHERE username LIKE '张%';
```

**单行写法：包含模糊查询**
`WHERE <列名> LIKE '%<子串>%'`
```sql
-- 查询包含指定字符的用户名
SELECT * FROM users WHERE username LIKE '%张%';
```

**单行写法：单字符匹配模糊查询**
`WHERE <列名> LIKE '<前缀>_'`
```sql
-- 查询指定前缀加单字符的用户名
SELECT * FROM users WHERE username LIKE '张_';
```

**单行写法：指定转义符模糊查询**
`WHERE <列名> LIKE '<模式>' ESCAPE '<转义符>'`
```sql
-- 使用指定转义符查询包含百分号的数据
SELECT * FROM users WHERE username LIKE '%100\%%' ESCAPE '\';
```

**单行写法：查询空值**
`WHERE <列名> IS NULL`
```sql
-- 查询邮箱为空的用户
SELECT * FROM users WHERE email IS NULL;
```

**单行写法：查询非空值**
`WHERE <列名> IS NOT NULL`
```sql
-- 查询已删除的用户
SELECT * FROM users WHERE deleted_at IS NOT NULL;
```

---

## 排序与分页

**单行写法：升序排序**
`ORDER BY <列名> ASC`
```sql
-- 按年龄升序排序
SELECT * FROM users ORDER BY age ASC;
```

**单行写法：降序排序**
`ORDER BY <列名> DESC`
```sql
-- 按创建时间降序排序
SELECT * FROM users ORDER BY created_at DESC;
```

**单行写法：多列排序**
`ORDER BY <列名1> [ASC|DESC], <列名2> [ASC|DESC]`
```sql
-- 先按状态升序再按年龄降序排序
SELECT * FROM users ORDER BY status ASC, age DESC;
```

**单行写法：按列位置排序**
`ORDER BY <列位置序号>`
```sql
-- 按查询列的位置序号排序
SELECT id, username, email FROM users ORDER BY 3;
```

**单行写法：取前 N 行**
`LIMIT <行数>`
```sql
-- 取前 10 行数据
SELECT * FROM users LIMIT 10;
```

**单行写法：分页查询**
`LIMIT <行数> OFFSET <偏移>`
```sql
-- 查询第 2 页数据（每页 10 行）
SELECT * FROM users LIMIT 10 OFFSET 10;
```

**单行写法：分页简写形式**
`LIMIT <偏移>, <行数>`
```sql
-- 使用简写形式分页查询
SELECT * FROM users LIMIT 10, 10;
```

**单行写法：排序后取前 N 行**
`SELECT * FROM <表名> ORDER BY <列名> [DESC] LIMIT <行数>`
```sql
-- 按降序排序后取前 5 行
SELECT * FROM users ORDER BY id DESC LIMIT 5;
```

---

## 分组查询

**换行写法：单列分组统计**
`SELECT <分组列>, <聚合函数>(<列名>) FROM <表名> GROUP BY <分组列>`
```sql
-- 按状态分组统计用户数量
SELECT status, COUNT(*) AS count FROM users GROUP BY status;
```

**换行写法：多列分组统计**
`SELECT <列名1>, <列名2>, <聚合函数>(<列名>) FROM <表名> GROUP BY <列名1>, <列名2>`
```sql
-- 按省份和城市分组统计用户数量
SELECT province, city, COUNT(*) AS count FROM users GROUP BY province, city;
```

**换行写法：分组求平均值**
`SELECT <分组列>, AVG(<列名>) FROM <表名> GROUP BY <分组列>`
```sql
-- 按状态分组求平均年龄
SELECT status, AVG(age) AS avg_age FROM users GROUP BY status;
```

**换行写法：分组过滤**
`SELECT <列名> FROM <表名> GROUP BY <列名> HAVING <过滤条件>`
```sql
-- 过滤分组结果只保留数量大于 10 的组
SELECT status, COUNT(*) AS count
FROM users
GROUP BY status
HAVING count > 10;
```

**换行写法：WHERE 与 HAVING 组合**
`SELECT <列名> FROM <表名> WHERE <条件> GROUP BY <列名> HAVING <过滤条件>`
```sql
-- 先过滤行再分组最后过滤分组
SELECT status, AVG(age) AS avg_age, COUNT(*) AS count
FROM users
WHERE age > 0
GROUP BY status
HAVING count > 5 AND avg_age > 25;
```

---

## 聚合函数

**单行写法：总行数计数**
`COUNT(*)`
```sql
-- 统计表的总行数
SELECT COUNT(*) FROM users;
```

**单行写法：非空计数**
`COUNT(<列名>)`
```sql
-- 统计邮箱非空的行数
SELECT COUNT(email) FROM users;
```

**单行写法：去重计数**
`COUNT(DISTINCT <列名>)`
```sql
-- 统计状态去重后的数量
SELECT COUNT(DISTINCT status) FROM users;
```

**单行写法：求和**
`SUM(<列名>)`
```sql
-- 统计所有用户余额总和
SELECT SUM(balance) AS total_balance FROM users;
```

**单行写法：求平均值**
`AVG(<列名>)`
```sql
-- 统计用户平均年龄
SELECT AVG(age) AS avg_age FROM users;
```

**单行写法：求最大值**
`MAX(<列名>)`
```sql
-- 查询商品最高价格
SELECT MAX(price) AS max_price FROM products;
```

**单行写法：求最小值**
`MIN(<列名>)`
```sql
-- 查询商品最低价格
SELECT MIN(price) AS min_price FROM products;
```

**换行写法：分组拼接字符串**
`GROUP_CONCAT(<列名> [SEPARATOR '<分隔符>'])`
```sql
-- 按状态分组拼接用户名
SELECT status, GROUP_CONCAT(username SEPARATOR ',') AS names
FROM users GROUP BY status;
```


<!-- ============ 文档分隔线：020-mysql/010-SQLDataDefinitionAdvanced.md ============ -->

# MySQL SQL 数据定义与高级对象

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数据库操作

**单行写法：创建数据库**
`CREATE DATABASE <库名>`
```sql
-- 创建数据库
CREATE DATABASE mydb;
```

**换行写法：创建数据库并指定字符集**
`CREATE DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>`
```sql
-- 创建数据库并指定字符集与排序规则
CREATE DATABASE mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

**换行写法：不存在时创建数据库**
`CREATE DATABASE IF NOT EXISTS <库名> [CHARACTER SET <字符集>] [COLLATE <排序规则>]`
```sql
-- 数据库不存在时才创建
CREATE DATABASE IF NOT EXISTS mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

**单行写法：查看所有数据库**
`SHOW DATABASES`
```sql
-- 查看所有数据库
SHOW DATABASES;
```

**单行写法：查看建库语句**
`SHOW CREATE DATABASE <库名>`
```sql
-- 查看数据库的建库语句
SHOW CREATE DATABASE mydb;
```

**单行写法：查看当前数据库**
`SELECT DATABASE()`
```sql
-- 查看当前使用的数据库
SELECT DATABASE();
```

**单行写法：选择数据库**
`USE <库名>`
```sql
-- 切换到指定数据库
USE mydb;
```

**单行写法：删除数据库**
`DROP DATABASE <库名>`
```sql
-- 删除数据库
DROP DATABASE mydb;
```

**单行写法：存在时删除数据库**
`DROP DATABASE IF EXISTS <库名>`
```sql
-- 数据库存在时才删除
DROP DATABASE IF EXISTS mydb;
```

**单行写法：修改数据库字符集**
`ALTER DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>`
```sql
-- 修改数据库的字符集与排序规则
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

## 表操作

**换行写法：创建表**
`CREATE TABLE [IF NOT EXISTS] <表名> (<列定义>[, <表约束>...])`
```sql
-- 创建用户表并包含索引
CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL COMMENT '邮箱',
  password VARCHAR(255) NOT NULL COMMENT '密码',
  phone VARCHAR(20) COMMENT '手机号',
  age INT UNSIGNED COMMENT '年龄',
  gender ENUM('男', '女', '保密') DEFAULT '保密' COMMENT '性别',
  status TINYINT DEFAULT 1 COMMENT '状态',
  balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '账户余额',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  INDEX idx_username (username),
  INDEX idx_email (email),
  INDEX idx_status (status)
);
```

**单行写法：查看表字段**
`DESC <表名>`
```sql
-- 查看表字段信息
DESC users;
```

**单行写法：查看列信息**
`SHOW COLUMNS FROM <表名>`
```sql
-- 查看表的列详细信息
SHOW COLUMNS FROM users;
```

**单行写法：查看建表语句**
`SHOW CREATE TABLE <表名>`
```sql
-- 查看表的建表语句
SHOW CREATE TABLE users;
```

**单行写法：查看所有表**
`SHOW TABLES`
```sql
-- 查看当前数据库的所有表
SHOW TABLES;
```

**单行写法：模糊查表**
`SHOW TABLES LIKE '<模式>'`
```sql
-- 模糊查询表名
SHOW TABLES LIKE '%user%';
```

**单行写法：添加列**
`ALTER TABLE <表名> ADD COLUMN <列定义> [AFTER <列名>]`
```sql
-- 在指定列后添加新列
ALTER TABLE users ADD COLUMN address VARCHAR(255) AFTER email;
```

**单行写法：修改列类型**
`ALTER TABLE <表名> MODIFY COLUMN <列名> <新类型> [<约束>]`
```sql
-- 修改列的定义
ALTER TABLE users MODIFY COLUMN phone VARCHAR(20) NOT NULL;
```

**单行写法：重命名列**
`ALTER TABLE <表名> CHANGE COLUMN <旧列名> <新列名> <类型> [<约束>]`
```sql
-- 重命名列并保留类型
ALTER TABLE users CHANGE COLUMN phone telephone VARCHAR(20) NOT NULL;
```

**单行写法：删除列**
`ALTER TABLE <表名> DROP COLUMN <列名>`
```sql
-- 删除指定列
ALTER TABLE users DROP COLUMN address;
```

**单行写法：添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX idx_phone (phone);
```

**单行写法：添加复合索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名1>, <列名2>[, ...])`
```sql
-- 添加复合索引
ALTER TABLE users ADD INDEX idx_age_gender (age, gender);
```

**单行写法：添加外键**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> FOREIGN KEY (<列名>) REFERENCES <父表>(<父列>)`
```sql
-- 添加外键约束
ALTER TABLE orders ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);
```

**单行写法：删除外键**
`ALTER TABLE <表名> DROP FOREIGN KEY <约束名>`
```sql
-- 删除外键约束
ALTER TABLE orders DROP FOREIGN KEY fk_user_id;
```

**单行写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>`
```sql
-- 重命名表
ALTER TABLE users RENAME TO user_info;
```

**单行写法：多表重命名**
`RENAME TABLE <旧表名1> TO <新表名1>, <旧表名2> TO <新表名2>`
```sql
-- 同时重命名多个表
RENAME TABLE users TO user_info, orders TO order_info;
```

**单行写法：删除表**
`DROP TABLE <表名>`
```sql
-- 删除表
DROP TABLE users;
```

**单行写法：存在时删除表**
`DROP TABLE IF EXISTS <表名>`
```sql
-- 表存在时才删除
DROP TABLE IF EXISTS users;
```

**单行写法：删除多表**
`DROP TABLE IF EXISTS <表名1>, <表名2>[, ...]`
```sql
-- 同时删除多个表
DROP TABLE IF EXISTS users, orders, products;
```

**单行写法：清空表**
`TRUNCATE TABLE <表名>`
```sql
-- 清空表数据
TRUNCATE TABLE users;
```

**单行写法：仅复制表结构**
`CREATE TABLE <新表> LIKE <源表>`
```sql
-- 仅复制表结构不复制数据
CREATE TABLE users_copy LIKE users;
```

**单行写法：复制结构和数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表>`
```sql
-- 复制表结构和全部数据
CREATE TABLE users_copy AS SELECT * FROM users;
```

**单行写法：复制部分数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表> WHERE <条件>`
```sql
-- 复制表结构并复制符合条件的数据
CREATE TABLE users_copy AS SELECT * FROM users WHERE status = 1;
```

---

## 索引操作

**单行写法：创建普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>[, <列名>...])`
```sql
-- 创建单列普通索引
CREATE INDEX idx_username ON users(username);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 创建多列复合索引
CREATE INDEX idx_name_status ON users(username, status);
```

**单行写法：创建唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>[, <列名>...])`
```sql
-- 创建单列唯一索引
CREATE UNIQUE INDEX idx_email ON users(email);
```

**单行写法：创建复合唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名1>, <列名2>[, ...])`
```sql
-- 创建多列复合唯一索引
CREATE UNIQUE INDEX idx_order_product ON order_items(order_id, product_id);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>))`
```sql
-- 为长字符串创建前缀索引
CREATE INDEX idx_email_prefix ON users(email(10));
```

**单行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, <列名>...])`
```sql
-- 为文本列创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_title_content (title, content);
```

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>`
```sql
-- 查看表的索引信息
SHOW INDEX FROM users;
```

**单行写法：删除索引**
`DROP INDEX <索引名> ON <表名>`
```sql
-- 删除指定索引
DROP INDEX idx_username ON users;
```

**单行写法：删除主键**
`ALTER TABLE <表名> DROP PRIMARY KEY`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 约束

**换行写法：综合约束建表**
`CREATE TABLE <表名> (<列定义>, <约束定义>...)`
```sql
-- 创建包含多种约束的订单表
CREATE TABLE orders (
  id INT PRIMARY KEY AUTO_INCREMENT,
  order_no VARCHAR(32) NOT NULL UNIQUE COMMENT '订单编号',
  user_id INT NOT NULL COMMENT '用户ID',
  total_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00 COMMENT '订单总额',
  status TINYINT NOT NULL DEFAULT 1 COMMENT '状态',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CHECK (total_amount >= 0),
  CHECK (status IN (1, 2, 3, 4, 5))
);
```

---

## 事务

**单行写法：开启事务**
`START TRANSACTION` / `BEGIN`
```sql
-- 开启事务
START TRANSACTION;
```

**换行写法：提交事务**
`COMMIT`
```sql
-- 提交事务并持久化变更
START TRANSACTION;
INSERT INTO users (username, email) VALUES ('张三', 'zhangsan@example.com');
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK`
```sql
-- 回滚事务撤销变更
ROLLBACK;
```

**换行写法：使用保存点**
`SAVEPOINT <保存点名>` / `ROLLBACK TO <保存点名>`
```sql
-- 使用保存点部分回滚
START TRANSACTION;
INSERT INTO users (username) VALUES ('张三');
SAVEPOINT sp1;
INSERT INTO users (username) VALUES ('李四');
ROLLBACK TO sp1;
COMMIT;
```

**单行写法：查看隔离级别**
`SELECT @@transaction_isolation`
```sql
-- 查看当前事务隔离级别
SELECT @@transaction_isolation;
```

**单行写法：设置会话隔离级别**
`SET SESSION TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**单行写法：设置全局隔离级别**
`SET GLOBAL TRANSACTION ISOLATION LEVEL <级别>`
```sql
-- 设置全局隔离级别为可序列化
SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

---

## 视图

**换行写法：创建简单视图**
`CREATE VIEW <视图名> AS <SELECT 语句>`
```sql
-- 创建只读视图
CREATE VIEW active_users AS
SELECT id, username, email, status
FROM users
WHERE status = 1;
```

**换行写法：创建多表视图**
`CREATE VIEW <视图名> AS <多表 JOIN 查询>`
```sql
-- 创建多表关联视图
CREATE VIEW order_details AS
SELECT
  o.id AS order_id,
  o.order_no,
  u.username,
  u.email,
  o.total_amount,
  o.status
FROM orders o
INNER JOIN users u ON o.user_id = u.id;
```

**单行写法：查询视图**
`SELECT <列名> FROM <视图名> [WHERE <条件>]`
```sql
-- 查询视图数据
SELECT * FROM active_users WHERE username LIKE '张%';
```

**换行写法：替换视图定义**
`CREATE OR REPLACE VIEW <视图名> AS <SELECT 语句>`
```sql
-- 替换已有视图的定义
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email, status, created_at
FROM users
WHERE status = 1;
```

**单行写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名>`
```sql
-- 删除视图
DROP VIEW IF EXISTS active_users;
```

**单行写法：查看视图定义**
`SHOW CREATE VIEW <视图名>`
```sql
-- 查看视图的建语句
SHOW CREATE VIEW order_details;
```

---

## 存储过程

**换行写法：创建带 IN 参数的存储过程**
`CREATE PROCEDURE <过程名>(IN <参数名> <类型>[, ...]) BEGIN <过程体> END`
```sql
-- 创建带输入参数的存储过程
DELIMITER //
CREATE PROCEDURE get_user_by_age(IN min_age INT, IN max_age INT)
BEGIN
  SELECT * FROM users
  WHERE age BETWEEN min_age AND max_age
  ORDER BY age;
END //
DELIMITER ;
```

**换行写法：创建带 OUT 参数的存储过程**
`CREATE PROCEDURE <过程名>(OUT <参数名> <类型>[, ...]) BEGIN <过程体> END`
```sql
-- 创建带输出参数的存储过程
DELIMITER //
CREATE PROCEDURE count_users_by_status(OUT active_count INT, OUT inactive_count INT)
BEGIN
  SELECT COUNT(*) INTO active_count FROM users WHERE status = 1;
  SELECT COUNT(*) INTO inactive_count FROM users WHERE status = 0;
END //
DELIMITER ;
```

**单行写法：调用无参存储过程**
`CALL <过程名>()`
```sql
-- 调用无参存储过程
CALL get_all_users();
```

**单行写法：调用带 IN 参数的存储过程**
`CALL <过程名>(<参数值>[, ...])`
```sql
-- 调用带输入参数的存储过程
CALL get_user_by_age(20, 30);
```

**换行写法：调用带 OUT 参数的存储过程**
`CALL <过程名>(@<变量名>[, ...])`
```sql
-- 调用带输出参数的存储过程并查看结果
CALL count_users_by_status(@active, @inactive);
SELECT @active AS active_users, @inactive AS inactive_users;
```

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS get_user_by_age;
```

---

## 触发器

**换行写法：创建插入前触发器**
`CREATE TRIGGER <触发器名> BEFORE INSERT ON <表名> FOR EACH ROW BEGIN <触发体> END`
```sql
-- 插入前自动填充时间字段
DELIMITER //
CREATE TRIGGER before_user_insert
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
  SET NEW.created_at = NOW();
  SET NEW.updated_at = NOW();
  IF NEW.status IS NULL THEN
    SET NEW.status = 1;
  END IF;
END //
DELIMITER ;
```

**换行写法：创建更新后触发器**
`CREATE TRIGGER <触发器名> AFTER UPDATE ON <表名> FOR EACH ROW BEGIN <触发体> END`
```sql
-- 更新后记录状态变更日志
DELIMITER //
CREATE TRIGGER after_order_update
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
  IF OLD.status != NEW.status THEN
    INSERT INTO order_status_log (order_id, old_status, new_status, changed_at)
    VALUES (OLD.id, OLD.status, NEW.status, NOW());
  END IF;
END //
DELIMITER ;
```

**单行写法：删除触发器**
`DROP TRIGGER [IF EXISTS] <触发器名>`
```sql
-- 删除触发器
DROP TRIGGER IF EXISTS before_user_insert;
```


<!-- ============ 文档分隔线：020-mysql/011-DDL.md ============ -->

# MySQL DDL 数据定义

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

> **新手必读：DDL 会自动提交，无法回滚**
> DDL 语句执行后立即生效，MySQL 会对其隐式提交，**不能像 DML 那样用 `ROLLBACK` 撤销**。
> 执行 `DROP` / `TRUNCATE` / `ALTER` 前务必再三确认作用对象与影响范围，删表、清表操作没有后悔药。

---

## 数据库操作

**单行写法：创建数据库**
`CREATE DATABASE [IF NOT EXISTS] <库名> [CHARACTER SET <字符集>] [COLLATE <排序规则>]`
```sql
-- 创建数据库并指定 utf8mb4 字符集
CREATE DATABASE IF NOT EXISTS mydb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;
```

**单行写法：查看所有数据库**
`SHOW DATABASES;`
```sql
-- 列出所有数据库
SHOW DATABASES;
```

**单行写法：查看建库语句**
`SHOW CREATE DATABASE <库名>;`
```sql
-- 查看 mydb 的建库语句
SHOW CREATE DATABASE mydb;
```

**单行写法：切换数据库**
`USE <库名>;`
```sql
-- 切换到 mydb
USE mydb;
```

**单行写法：修改数据库字符集**
`ALTER DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>;`
```sql
-- 修改数据库字符集与排序规则
ALTER DATABASE mydb CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

**单行写法：删除数据库**
`DROP DATABASE [IF EXISTS] <库名>;`
```sql
-- 存在时才删除
DROP DATABASE IF EXISTS mydb;
```

---

## 创建表

**换行写法：创建完整表结构**
`CREATE TABLE [IF NOT EXISTS] <表名> (<列定义>[, <表约束>...]) [ENGINE=<引擎>] [DEFAULT CHARSET=<字符集>];`
```sql
-- 创建用户表并指定存储引擎与字符集
CREATE TABLE IF NOT EXISTS users (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY COMMENT '用户ID',
  username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名',
  email VARCHAR(100) NOT NULL COMMENT '邮箱',
  age INT UNSIGNED COMMENT '年龄',
  balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '余额',
  status TINYINT DEFAULT 1 COMMENT '状态',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**单行写法：仅复制表结构**
`CREATE TABLE <新表> LIKE <源表>;`
```sql
-- 复制表结构不复制数据
CREATE TABLE users_copy LIKE users;
```

**单行写法：复制结构和数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表>;`
```sql
-- 复制表结构和全部数据
CREATE TABLE users_backup AS SELECT * FROM users;
```

**单行写法：复制部分数据**
`CREATE TABLE <新表> AS SELECT * FROM <源表> WHERE <条件>;`
```sql
-- 仅复制符合条件的数据
CREATE TABLE active_users AS SELECT * FROM users WHERE status = 1;
```

---

## 查看表结构

**单行写法：查看表字段**
`DESC <表名>;`
```sql
-- 查看表字段信息
DESC users;
```

**单行写法：查看列详细信息**
`SHOW COLUMNS FROM <表名>;`
```sql
-- 查看列的详细定义
SHOW COLUMNS FROM users;
```

**单行写法：查看建表语句**
`SHOW CREATE TABLE <表名>;`
```sql
-- 查看完整建表语句
SHOW CREATE TABLE users;
```

**单行写法：查看当前库所有表**
`SHOW TABLES;`
```sql
-- 列出当前数据库的所有表
SHOW TABLES;
```

**单行写法：模糊查表**
`SHOW TABLES LIKE '<模式>';`
```sql
-- 模糊查询表名
SHOW TABLES LIKE '%user%';
```

---

## 修改表 ALTER TABLE

**单行写法：添加列**
`ALTER TABLE <表名> ADD COLUMN <列定义> [AFTER <列名>];`
```sql
-- 在 email 列后添加新列
ALTER TABLE users ADD COLUMN phone VARCHAR(20) AFTER email;
```

**单行写法：快速添加列（8.0.12+ INSTANT）**
`ALTER TABLE <表名> ADD COLUMN <列定义>, ALGORITHM=INSTANT;`
```sql
-- 即时添加列，不修改数据行
ALTER TABLE users ADD COLUMN nickname VARCHAR(50), ALGORITHM=INSTANT;
```

**单行写法：修改列定义**
`ALTER TABLE <表名> MODIFY COLUMN <列名> <新类型> [<约束>];`
```sql
-- 修改列类型并加约束
ALTER TABLE users MODIFY COLUMN phone VARCHAR(20) NOT NULL;
```

**单行写法：重命名列**
`ALTER TABLE <表名> CHANGE COLUMN <旧列名> <新列名> <类型> [<约束>];`
```sql
-- 重命名列并保留类型
ALTER TABLE users CHANGE COLUMN phone telephone VARCHAR(20) NOT NULL;
```

**单行写法：删除列**
`ALTER TABLE <表名> DROP COLUMN <列名>;`
```sql
-- 删除指定列
ALTER TABLE users DROP COLUMN nickname;
```

**单行写法：重命名表**
`ALTER TABLE <旧表名> RENAME TO <新表名>;`
```sql
-- 重命名表
ALTER TABLE users RENAME TO user_info;
```

**单行写法：多表重命名**
`RENAME TABLE <旧1> TO <新1>, <旧2> TO <新2>;`
```sql
-- 同时重命名多个表
RENAME TABLE users TO user_info, orders TO order_info;
```

---

## 约束管理

**单行写法：添加主键**
`ALTER TABLE <表名> ADD PRIMARY KEY (<列名>);`
```sql
-- 添加主键约束
ALTER TABLE users ADD PRIMARY KEY (id);
```

**单行写法：添加唯一约束**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>);`
```sql
-- 添加唯一约束
ALTER TABLE users ADD UNIQUE INDEX uk_email (email);
```

**单行写法：添加外键**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> FOREIGN KEY (<列名>) REFERENCES <父表>(<父列>) [ON DELETE <动作>] [ON UPDATE <动作>];`
```sql
-- 添加外键并设置级联更新
ALTER TABLE orders ADD CONSTRAINT fk_user_id
  FOREIGN KEY (user_id) REFERENCES users(id)
  ON DELETE RESTRICT ON UPDATE CASCADE;
```

**单行写法：添加 CHECK 约束（8.0.16+）**
`ALTER TABLE <表名> ADD CONSTRAINT <约束名> CHECK (<条件>);`
```sql
-- 添加检查约束
ALTER TABLE users ADD CONSTRAINT chk_age CHECK (age >= 0 AND age < 150);
```

**单行写法：删除外键**
`ALTER TABLE <表名> DROP FOREIGN KEY <约束名>;`
```sql
-- 删除外键约束
ALTER TABLE orders DROP FOREIGN KEY fk_user_id;
```

**单行写法：删除主键**
`ALTER TABLE <表名> DROP PRIMARY KEY;`
```sql
-- 删除主键约束
ALTER TABLE users DROP PRIMARY KEY;
```

---

## 删除表与清空

**单行写法：删除表**
`DROP TABLE [IF EXISTS] <表名>[, <表名>...];`
```sql
-- 同时删除多个表
DROP TABLE IF EXISTS users, orders, products;
```

**单行写法：清空表数据**
`TRUNCATE TABLE <表名>;`
```sql
-- 清空表数据并重置自增ID
TRUNCATE TABLE users;
```

---

## 视图

**换行写法：创建视图**
`CREATE [OR REPLACE] VIEW <视图名> AS <SELECT 语句>;`
```sql
-- 创建或替换活跃用户视图
CREATE OR REPLACE VIEW active_users AS
SELECT id, username, email FROM users WHERE status = 1;
```

**单行写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名>;`
```sql
-- 删除视图
DROP VIEW IF EXISTS active_users;
```


<!-- ============ 文档分隔线：020-mysql/012-DML.md ============ -->

# MySQL DML 数据操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## INSERT 插入

**单行写法：插入单行**
`INSERT INTO <表名> (<列1>, <列2>) VALUES (<值1>, <值2>);`
```sql
-- 插入一条用户记录
INSERT INTO users (username, email, age) VALUES ('zhangsan', 'zs@example.com', 25);
```

**单行写法：插入所有列**
`INSERT INTO <表名> VALUES (<值1>, <值2>, ...);`
```sql
-- 按列顺序插入所有列
INSERT INTO users VALUES (NULL, 'lisi', 'ls@example.com', 30, 0.00, 1, NOW(), NOW());
```

**换行写法：插入多行**
`INSERT INTO <表名> (<列>) VALUES (<值1>), (<值2>), (<值3>);`
```sql
-- 批量插入多行数据
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

**换行写法：插入时使用 ON DUPLICATE KEY UPDATE**
`INSERT INTO <表名> (<列>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列>=<值>;`
```sql
-- 主键或唯一键冲突时更新
INSERT INTO users (id, username, email) VALUES (1, 'zhangsan', 'new@example.com')
ON DUPLICATE KEY UPDATE email = VALUES(email), updated_at = NOW();
```

**换行写法：INSERT ... IGNORE 忽略冲突**
`INSERT IGNORE INTO <表名> (<列>) VALUES (<值>);`
```sql
-- 主键冲突时忽略不报错
INSERT IGNORE INTO users (id, username) VALUES (1, 'zhangsan');
```

**单行写法：REPLACE 替换插入**
`REPLACE INTO <表名> (<列>) VALUES (<值>);`
```sql
-- 冲突时先删除旧行再插入新行
REPLACE INTO users (id, username, email) VALUES (1, 'zhangsan', 'new@example.com');
```

---

## UPDATE 更新

**单行写法：更新单列**
`UPDATE <表名> SET <列>=<值> WHERE <条件>;`
```sql
-- 更新指定用户的年龄
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

**换行写法：基于 JOIN 更新**
`UPDATE <表1> JOIN <表2> ON <条件> SET <列>=<值>;`
```sql
-- 关联订单表更新用户总消费
UPDATE users u
JOIN (SELECT user_id, SUM(total_amount) AS total FROM orders GROUP BY user_id) o
  ON u.id = o.user_id
SET u.balance = u.balance - o.total;
```

**单行写法：使用 LIMIT 限制更新行数**
`UPDATE <表名> SET <列>=<值> WHERE <条件> LIMIT <数量>;`
```sql
-- 仅更新前 100 条匹配记录
UPDATE users SET status = 0 WHERE last_login < '2024-01-01' LIMIT 100;
```

**单行写法：使用 CASE 条件更新**
`UPDATE <表名> SET <列> = CASE <条件列> WHEN <值1> THEN <结果1> ELSE <结果2> END WHERE <条件>;`
```sql
-- 根据不同状态批量更新
UPDATE users SET status = CASE age
  WHEN 18 THEN 1
  WHEN 30 THEN 2
  ELSE status
END WHERE age IN (18, 30);
```

---

## DELETE 删除

**单行写法：按条件删除**
`DELETE FROM <表名> WHERE <条件>;`
```sql
-- 删除指定用户
DELETE FROM users WHERE id = 1;
```

**单行写法：限制删除行数**
`DELETE FROM <表名> WHERE <条件> LIMIT <数量>;`
```sql
-- 仅删除前 100 条匹配记录
DELETE FROM logs WHERE created_at < '2024-01-01' LIMIT 100;
```

**换行写法：基于 JOIN 删除**
`DELETE <别名> FROM <表1> <别名> JOIN <表2> ON <条件> WHERE <条件>;`
```sql
-- 删除没有订单的用户
DELETE u FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

**换行写法：多表关联删除**
`DELETE <表1>, <表2> FROM <表1> JOIN <表2> ON <条件> WHERE <条件>;`
```sql
-- 同时删除用户和其订单
DELETE u, o FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.id = 1;
```

**单行写法：删除所有数据**
`DELETE FROM <表名>;`
```sql
-- 删除全表数据（保留自增ID计数）
DELETE FROM users;
```

---

## UPSERT 与冲突处理

**换行写法：VALUES() 函数引用插入值**
`INSERT INTO <表> (<列>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列>=VALUES(<列>);`
```sql
-- 冲突时引用待插入值更新
INSERT INTO counters (id, count) VALUES (1, 1)
ON DUPLICATE KEY UPDATE count = count + VALUES(count);
```

**换行写法：MySQL 8.0.20+ 使用别名引用**
`INSERT INTO <表> (<列>) VALUES (<值>) AS <别名> ON DUPLICATE KEY UPDATE <列>=<别名>.<列>;`
```sql
-- 8.0.20+ 使用别名替代 VALUES()
INSERT INTO counters (id, count) VALUES (1, 1) AS new
ON DUPLICATE KEY UPDATE count = counters.count + new.count;
```

---

## 事务控制

**单行写法：开启事务**
`START TRANSACTION;` 或 `BEGIN;`
```sql
-- 开启事务
START TRANSACTION;
```

**换行写法：提交事务**
`COMMIT;`
```sql
-- 提交事务持久化变更
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;
COMMIT;
```

**单行写法：回滚事务**
`ROLLBACK;`
```sql
-- 回滚撤销事务变更
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
`SELECT @@transaction_isolation;`
```sql
-- 查看当前事务隔离级别
SELECT @@transaction_isolation;
```

**单行写法：设置隔离级别**
`SET SESSION TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- 设置会话隔离级别为读已提交
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```


<!-- ============ 文档分隔线：020-mysql/013-DQL.md ============ -->

# MySQL DQL 查询速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SELECT 基础

**单行写法：查询所有列**
`SELECT * FROM <表名>;`
```sql
-- 查询所有用户
SELECT * FROM users;
```

**单行写法：查询指定列**
`SELECT <列1>, <列2> FROM <表名>;`
```sql
-- 查询用户名和邮箱
SELECT username, email FROM users;
```

**单行写法：列别名**
`SELECT <列> AS <别名> FROM <表名>;`
```sql
-- 给列起别名
SELECT username AS 用户名, email AS 邮箱 FROM users;
```

**单行写法：去重查询**
`SELECT DISTINCT <列> FROM <表名>;`
```sql
-- 查询不重复的城市
SELECT DISTINCT city FROM users;
```

**单行写法：限制列数预览**
`SELECT * FROM <表名> LIMIT <数量>;`
```sql
-- 仅查看前 5 行
SELECT * FROM users LIMIT 5;
```

---

## WHERE 条件

**单行写法：等值条件**
`SELECT * FROM <表名> WHERE <列>=<值>;`
```sql
-- 查询状态为 1 的用户
SELECT * FROM users WHERE status = 1;
```

**单行写法：多条件 AND**
`SELECT * FROM <表名> WHERE <条件1> AND <条件2>;`
```sql
-- 查询活跃且成年的用户
SELECT * FROM users WHERE status = 1 AND age >= 18;
```

**单行写法：多条件 OR**
`SELECT * FROM <表名> WHERE <条件1> OR <条件2>;`
```sql
-- 查询北京或上海的用户
SELECT * FROM users WHERE city = '北京' OR city = '上海';
```

**单行写法：IN 范围查询**
`SELECT * FROM <表名> WHERE <列> IN (<值1>, <值2>);`
```sql
-- 查询指定状态的用户
SELECT * FROM users WHERE status IN (1, 2, 3);
```

**单行写法：BETWEEN 范围查询**
`SELECT * FROM <表名> WHERE <列> BETWEEN <起> AND <止>;`
```sql
-- 查询年龄在 18 到 30 之间的用户
SELECT * FROM users WHERE age BETWEEN 18 AND 30;
```

**单行写法：LIKE 模糊查询**
`SELECT * FROM <表名> WHERE <列> LIKE '<模式>';`
```sql
-- 查询姓张的用户
SELECT * FROM users WHERE username LIKE '张%';
```

**单行写法：IS NULL 空值查询**
`SELECT * FROM <表名> WHERE <列> IS NULL;`
```sql
-- 查询手机号为空的用户
SELECT * FROM users WHERE phone IS NULL;
```

**单行写法：IS NOT NULL 非空查询**
`SELECT * FROM <表名> WHERE <列> IS NOT NULL;`
```sql
-- 查询已填写邮箱的用户
SELECT * FROM users WHERE email IS NOT NULL;
```

**单行写法：NOT IN 反向查询**
`SELECT * FROM <表名> WHERE <列> NOT IN (<值1>, <值2>);`
```sql
-- 查询非指定状态的用户
SELECT * FROM users WHERE status NOT IN (0, 9);
```

---

## ORDER BY 排序

**单行写法：升序排序**
`SELECT * FROM <表名> ORDER BY <列> ASC;`
```sql
-- 按年龄升序排列
SELECT * FROM users ORDER BY age ASC;
```

**单行写法：降序排序**
`SELECT * FROM <表名> ORDER BY <列> DESC;`
```sql
-- 按创建时间降序排列
SELECT * FROM users ORDER BY created_at DESC;
```

**单行写法：多列排序**
`SELECT * FROM <表名> ORDER BY <列1> DESC, <列2> ASC;`
```sql
-- 先按状态降序，再按年龄升序
SELECT * FROM users ORDER BY status DESC, age ASC;
```

**单行写法：按表达式排序**
`SELECT * FROM <表名> ORDER BY <表达式>;`
```sql
-- 按余额绝对值排序
SELECT * FROM accounts ORDER BY ABS(balance);
```

---

## LIMIT 分页

**单行写法：限制返回行数**
`SELECT * FROM <表名> LIMIT <数量>;`
```sql
-- 仅返回前 10 条
SELECT * FROM users LIMIT 10;
```

**单行写法：分页查询**
`SELECT * FROM <表名> LIMIT <偏移量>, <数量>;`
```sql
-- 查询第 3 页每页 10 条
SELECT * FROM users LIMIT 20, 10;
```

**单行写法：OFFSET 写法**
`SELECT * FROM <表名> LIMIT <数量> OFFSET <偏移量>;`
```sql
-- 使用 OFFSET 关键字分页
SELECT * FROM users LIMIT 10 OFFSET 20;
```

**换行写法：深度分页优化**
`SELECT * FROM <表名> WHERE <主键> > <上次最大值> ORDER BY <主键> LIMIT <数量>;`
```sql
-- 基于主键游标分页避免深度分页性能问题
SELECT id, username FROM users WHERE id > 10000 ORDER BY id LIMIT 10;
```

---

## 运算符与函数

**单行写法：算术运算**
`SELECT <列1> + <列2> AS <别名> FROM <表名>;`
```sql
-- 计算总价
SELECT price * quantity AS total FROM order_items;
```

**单行写法：日期比较**
`SELECT * FROM <表名> WHERE <日期列> > <日期值>;`
```sql
-- 查询 2024 年后的订单
SELECT * FROM orders WHERE created_at > '2024-01-01';
```

**单行写法：字符串拼接**
`SELECT CONCAT(<列1>, <列2>) AS <别名> FROM <表名>;`
```sql
-- 拼接用户姓名
SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;
```

**单行写法：使用 IF 函数**
`SELECT IF(<条件>, <真值>, <假值>) FROM <表名>;`
```sql
-- 根据状态返回文本
SELECT username, IF(status = 1, '活跃', '禁用') AS state FROM users;
```

**换行写法：CASE 表达式**
`CASE WHEN <条件> THEN <结果> ELSE <默认> END`
```sql
-- 多条件分支判断
SELECT username,
  CASE
    WHEN age < 18 THEN '未成年'
    WHEN age < 60 THEN '成年'
    ELSE '老年'
  END AS age_group
FROM users;
```

---

## 子查询

**单行写法：标量子查询**
`SELECT * FROM <表名> WHERE <列> = (SELECT <列> FROM <表名> WHERE <条件>);`
```sql
-- 查询年龄大于平均年龄的用户
SELECT * FROM users WHERE age > (SELECT AVG(age) FROM users);
```

**单行写法：IN 子查询**
`SELECT * FROM <表名> WHERE <列> IN (SELECT <列> FROM <表名>);`
```sql
-- 查询有订单的用户
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);
```

**单行写法：EXISTS 子查询**
`SELECT * FROM <表1> WHERE EXISTS (SELECT 1 FROM <表2> WHERE <条件>);`
```sql
-- 查询存在订单的用户
SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

**换行写法：NOT EXISTS 子查询**
`SELECT * FROM <表1> WHERE NOT EXISTS (SELECT 1 FROM <表2> WHERE <条件>);`
```sql
-- 查询没有订单的用户
SELECT * FROM users u WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```


<!-- ============ 文档分隔线：020-mysql/014-Join.md ============ -->

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


<!-- ============ 文档分隔线：020-mysql/015-AggregateGroup.md ============ -->

# MySQL 聚合与分组

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 聚合函数

**单行写法：COUNT 计数**
`SELECT COUNT(<列>) FROM <表名>;`
```sql
-- 统计用户总数
SELECT COUNT(*) AS total FROM users;
```

**单行写法：COUNT 去重计数**
`SELECT COUNT(DISTINCT <列>) FROM <表名>;`
```sql
-- 统计不重复的城市数量
SELECT COUNT(DISTINCT city) FROM users;
```

**单行写法：SUM 求和**
`SELECT SUM(<列>) FROM <表名>;`
```sql
-- 统计所有订单总金额
SELECT SUM(total_amount) AS total FROM orders;
```

**单行写法：AVG 平均值**
`SELECT AVG(<列>) FROM <表名>;`
```sql
-- 计算用户平均年龄
SELECT AVG(age) AS avg_age FROM users;
```

**单行写法：MAX 最大值**
`SELECT MAX(<列>) FROM <表名>;`
```sql
-- 查询最高订单金额
SELECT MAX(total_amount) AS max_amount FROM orders;
```

**单行写法：MIN 最小值**
`SELECT MIN(<列>) FROM <表名>;`
```sql
-- 查询最低订单金额
SELECT MIN(total_amount) AS min_amount FROM orders;
```

**单行写法：GROUP_CONCAT 分组拼接**
`SELECT GROUP_CONCAT(<列> SEPARATOR '<分隔符>') FROM <表名>;`
```sql
-- 拼接用户名用逗号分隔
SELECT GROUP_CONCAT(username SEPARATOR ',') FROM users;
```

**单行写法：BIT_COUNT 位计数**
`SELECT BIT_COUNT(<列>) FROM <表名>;`
```sql
-- 统计二进制位中 1 的个数
SELECT BIT_COUNT(flags) FROM users;
```

---

## GROUP BY 分组

**换行写法：单列分组**
`SELECT <列>, <聚合函数> FROM <表名> GROUP BY <列>;`
```sql
-- 按状态分组统计用户数
SELECT status, COUNT(*) AS count FROM users GROUP BY status;
```

**换行写法：多列分组**
`SELECT <列1>, <列2>, <聚合> FROM <表名> GROUP BY <列1>, <列2>;`
```sql
-- 按城市和性别分组统计
SELECT city, gender, COUNT(*) AS count FROM users GROUP BY city, gender;
```

**换行写法：按表达式分组**
`SELECT <表达式>, <聚合> FROM <表名> GROUP BY <表达式>;`
```sql
-- 按月份分组统计订单
SELECT DATE_FORMAT(created_at, '%Y-%m') AS month, COUNT(*) AS orders
FROM orders
GROUP BY month;
```

**换行写法：按日期分组**
`SELECT DATE(<列>), <聚合> FROM <表名> GROUP BY DATE(<列>);`
```sql
-- 按天统计订单数量
SELECT DATE(created_at) AS day, COUNT(*) AS cnt
FROM orders
GROUP BY DATE(created_at);
```

---

## HAVING 过滤分组

**换行写法：HAVING 过滤聚合结果**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> HAVING <条件>;`
```sql
-- 查询订单数超过 5 的用户
SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id HAVING cnt > 5;
```

**换行写法：HAVING 多条件**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> HAVING <条件1> AND <条件2>;`
```sql
-- 查询订单数大于 5 且总金额大于 1000 的用户
SELECT user_id, COUNT(*) AS cnt, SUM(total_amount) AS total
FROM orders
GROUP BY user_id
HAVING cnt > 5 AND total > 1000;
```

**换行写法：WHERE 与 HAVING 组合**
`SELECT <列>, <聚合> FROM <表名> WHERE <过滤条件> GROUP BY <列> HAVING <聚合条件>;`
```sql
-- 先过滤再分组再筛选
SELECT user_id, COUNT(*) AS cnt
FROM orders
WHERE status = 1
GROUP BY user_id
HAVING cnt >= 3;
```

---

## WITH ROLLUP 汇总

**换行写法：分组小计与合计**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> WITH ROLLUP;`
```sql
-- 按城市分组统计并显示总计
SELECT IFNULL(city, '总计') AS city, COUNT(*) AS cnt
FROM users
GROUP BY city WITH ROLLUP;
```

**换行写法：多列 ROLLUP 分层汇总**
`SELECT <列1>, <列2>, <聚合> FROM <表名> GROUP BY <列1>, <列2> WITH ROLLUP;`
```sql
-- 按城市和性别分层汇总
SELECT IFNULL(city, '总计') AS city, IFNULL(gender, '小计') AS gender, COUNT(*) AS cnt
FROM users
GROUP BY city, gender WITH ROLLUP;
```

---

## GROUP BY 排序与限制

**换行写法：分组后排序**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> ORDER BY <聚合> DESC;`
```sql
-- 按订单数降序排列用户
SELECT user_id, COUNT(*) AS cnt FROM orders GROUP BY user_id ORDER BY cnt DESC;
```

**换行写法：分组排序并限制**
`SELECT <列>, <聚合> FROM <表名> GROUP BY <列> ORDER BY <聚合> DESC LIMIT <数量>;`
```sql
-- 查询订单数前 10 的用户
SELECT user_id, COUNT(*) AS cnt
FROM orders
GROUP BY user_id
ORDER BY cnt DESC
LIMIT 10;
```

---

## 窗口函数聚合（8.0+）

**换行写法：累计求和**
`SELECT <列>, SUM(<列>) OVER (ORDER BY <列>) FROM <表名>;`
```sql
-- 按日期累计求和销售额
SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date) AS cumulative
FROM daily_sales;
```

**换行写法：分组排名**
`SELECT <列>, ROW_NUMBER() OVER (PARTITION BY <列> ORDER BY <列>) FROM <表名>;`
```sql
-- 每个部门按薪资排名
SELECT name, dept_id, salary,
  ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
FROM employees;
```

**换行写法：分组占比**
`SELECT <列>, <列> / SUM(<列>) OVER (PARTITION BY <列>) FROM <表名>;`
```sql
-- 计算每个用户订单金额占该用户总金额的比例
SELECT user_id, order_no, total_amount,
  total_amount / SUM(total_amount) OVER (PARTITION BY user_id) AS ratio
FROM orders;
```


<!-- ============ 文档分隔线：020-mysql/016-IndexManagement.md ============ -->

# MySQL 索引管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建索引

**单行写法：创建普通索引**
`CREATE INDEX <索引名> ON <表名>(<列名>[, <列名>...]);`
```sql
-- 在 email 列上创建索引
CREATE INDEX idx_email ON users(email);
```

**单行写法：创建复合索引**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>[, ...]);`
```sql
-- 创建多列复合索引
CREATE INDEX idx_status_created ON orders(status, created_at);
```

**单行写法：创建唯一索引**
`CREATE UNIQUE INDEX <索引名> ON <表名>(<列名>);`
```sql
-- 创建唯一索引
CREATE UNIQUE INDEX uk_email ON users(email);
```

**单行写法：创建前缀索引**
`CREATE INDEX <索引名> ON <表名>(<列名>(<长度>));`
```sql
-- 为长字符串列创建前缀索引
CREATE INDEX idx_name_prefix ON users(username(10));
```

**换行写法：创建全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名> (<列名>[, ...]);`
```sql
-- 为文章标题和内容创建全文索引
ALTER TABLE articles ADD FULLTEXT INDEX ft_content (title, content);
```

**换行写法：创建函数索引（8.0.13+）**
`CREATE INDEX <索引名> ON <表名>((<表达式>));`
```sql
-- 为列的小写形式创建函数索引
CREATE INDEX idx_lower_email ON users((LOWER(email)));
```

**换行写法：创建降序索引（8.0+）**
`CREATE INDEX <索引名> ON <表名>(<列> DESC);`
```sql
-- 创建降序索引优化倒序查询
CREATE INDEX idx_created_desc ON orders(created_at DESC);
```

---

## ALTER TABLE 管理索引

**单行写法：添加普通索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列名>);`
```sql
-- 添加普通索引
ALTER TABLE users ADD INDEX idx_age (age);
```

**单行写法：添加唯一索引**
`ALTER TABLE <表名> ADD UNIQUE INDEX <索引名> (<列名>);`
```sql
-- 添加唯一索引
ALTER TABLE users ADD UNIQUE INDEX uk_phone (phone);
```

**单行写法：添加主键**
`ALTER TABLE <表名> ADD PRIMARY KEY (<列名>);`
```sql
-- 添加主键
ALTER TABLE users ADD PRIMARY KEY (id);
```

**单行写法：设置不可见索引（8.0+）**
`ALTER TABLE <表名> ALTER INDEX <索引名> INVISIBLE;`
```sql
-- 隐藏索引用于测试删除影响
ALTER TABLE users ALTER INDEX idx_age INVISIBLE;
```

**单行写法：恢复可见索引**
`ALTER TABLE <表名> ALTER INDEX <索引名> VISIBLE;`
```sql
-- 恢复索引可见
ALTER TABLE users ALTER INDEX idx_age VISIBLE;
```

---

## 查看索引

**单行写法：查看表索引**
`SHOW INDEX FROM <表名>;`
```sql
-- 查看 users 表的索引
SHOW INDEX FROM users;
```

**单行写法：查看表索引带库名**
`SHOW INDEX FROM <表名> FROM <库名>;`
```sql
-- 查看指定库的表索引
SHOW INDEX FROM users FROM mydb;
```

**单行写法：查看建表语句含索引**
`SHOW CREATE TABLE <表名>;`
```sql
-- 查看建表语句中包含的索引定义
SHOW CREATE TABLE users;
```

---

## 删除索引

**单行写法：DROP INDEX 删除**
`DROP INDEX <索引名> ON <表名>;`
```sql
-- 删除指定索引
DROP INDEX idx_email ON users;
```

**单行写法：ALTER 删除索引**
`ALTER TABLE <表名> DROP INDEX <索引名>;`
```sql
-- 通过 ALTER 删除索引
ALTER TABLE users DROP INDEX idx_age;
```

**单行写法：删除主键**
`ALTER TABLE <表名> DROP PRIMARY KEY;`
```sql
-- 删除主键索引
ALTER TABLE users DROP PRIMARY KEY;
```

**单行写法：删除全文索引**
`ALTER TABLE <表名> DROP INDEX <索引名>;`
```sql
-- 删除全文索引
ALTER TABLE articles DROP INDEX ft_content;
```

---

## 索引分析

**单行写法：查看执行计划**
`EXPLAIN SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

**单行写法：分析执行计划**
`EXPLAIN ANALYZE SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 8.0.18+ 显示实际执行耗时
EXPLAIN ANALYZE SELECT * FROM users WHERE status = 1;
```

**单行写法：查看索引使用情况**
`SELECT * FROM sys.schema_index_statistics WHERE table_schema = '<库名>';`
```sql
-- 查看索引的读写统计
SELECT * FROM sys.schema_index_statistics
WHERE table_schema = 'mydb' AND table_name = 'users';
```

**单行写法：查看未使用的索引**
`SELECT * FROM sys.schema_unused_indexes WHERE object_schema = '<库名>';`
```sql
-- 查找从未被使用的索引
SELECT * FROM sys.schema_unused_indexes WHERE object_schema = 'mydb';
```

---

## 索引维护

**单行写法：分析表更新统计**
`ANALYZE TABLE <表名>;`
```sql
-- 重新分析表统计信息
ANALYZE TABLE users;
```

**单行写法：检查表**
`CHECK TABLE <表名>;`
```sql
-- 检查表是否有错误
CHECK TABLE users;
```

**单行写法：优化表**
`OPTIMIZE TABLE <表名>;`
```sql
-- 优化表回收空间
OPTIMIZE TABLE users;
```

**单行写法：在线添加索引**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列>), ALGORITHM=INPLACE, LOCK=NONE;`
```sql
-- 在线添加索引不阻塞读写
ALTER TABLE users ADD INDEX idx_nickname (nickname), ALGORITHM=INPLACE, LOCK=NONE;
```

**单行写法：即时添加列索引（8.0.12+）**
`ALTER TABLE <表名> ADD INDEX <索引名> (<列>), ALGORITHM=INSTANT;`
```sql
-- 即时操作不影响数据
ALTER TABLE users ADD INDEX idx_status (status), ALGORITHM=INSTANT;
```

---

## 索引设计原则

**单行写法：复合索引最左前缀**
`CREATE INDEX <索引名> ON <表名>(<高频列>, <范围列>);`
```sql
-- 高频等值列在前，范围列在后
CREATE INDEX idx_status_age ON users(status, age);
```

**单行写法：覆盖索引避免回表**
`CREATE INDEX <索引名> ON <表名>(<列1>, <列2>);`
```sql
-- 索引包含查询所需所有列
CREATE INDEX idx_cover ON orders(user_id, status, total_amount);
```

**单行写法：使用 EXPLAIN 验证类型**
`EXPLAIN SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 检查 type 列是否为 ref 或 eq_ref
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```


<!-- ============ 文档分隔线：020-mysql/017-UserPermission.md ============ -->

# MySQL 用户与权限管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 用户管理

**单行写法：创建用户**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED BY '<密码>';`
```sql
-- 创建本地用户
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'StrongPass123!';
```

**单行写法：创建远程用户**
`CREATE USER '<用户名>'@'%' IDENTIFIED BY '<密码>';`
```sql
-- 允许从任意主机连接
CREATE USER 'appuser'@'%' IDENTIFIED BY 'StrongPass123!';
```

**换行写法：指定认证插件（8.0+ 默认）**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED WITH caching_sha2_password BY '<密码>';`
```sql
-- 使用默认 caching_sha2_password 认证插件
CREATE USER 'secure_user'@'%' IDENTIFIED WITH caching_sha2_password BY 'StrongPass123!';
```

**换行写法：使用 mysql_native_password 认证**
`CREATE USER '<用户名>'@'<主机>' IDENTIFIED WITH mysql_native_password BY '<密码>';`
```sql
-- 兼容旧客户端的认证方式
CREATE USER 'legacy_user'@'%' IDENTIFIED WITH mysql_native_password BY 'StrongPass123!';
```

**单行写法：修改用户密码**
`ALTER USER '<用户名>'@'<主机>' IDENTIFIED BY '<新密码>';`
```sql
-- 修改用户密码
ALTER USER 'appuser'@'localhost' IDENTIFIED BY 'NewPass456!';
```

**单行写法：修改当前用户密码**
`ALTER USER USER() IDENTIFIED BY '<新密码>';`
```sql
-- 修改当前登录用户密码
ALTER USER USER() IDENTIFIED BY 'NewPass456!';
```

**单行写法：锁定用户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT LOCK;`
```sql
-- 锁定用户禁止登录
ALTER USER 'appuser'@'localhost' ACCOUNT LOCK;
```

**单行写法：解锁用户**
`ALTER USER '<用户名>'@'<主机>' ACCOUNT UNLOCK;`
```sql
-- 解锁用户
ALTER USER 'appuser'@'localhost' ACCOUNT UNLOCK;
```

**单行写法：设置密码过期**
`ALTER USER '<用户名>'@'<主机>' PASSWORD EXPIRE;`
```sql
-- 强制用户下次登录修改密码
ALTER USER 'appuser'@'localhost' PASSWORD EXPIRE;
```

**单行写法：删除用户**
`DROP USER [IF EXISTS] '<用户名>'@'<主机>';`
```sql
-- 删除用户
DROP USER IF EXISTS 'appuser'@'localhost';
```

**单行写法：重命名用户**
`RENAME USER '<旧名>'@'<主机>' TO '<新名>'@'<主机>';`
```sql
-- 重命名用户
RENAME USER 'appuser'@'localhost' TO 'webapp'@'localhost';
```

---

## 查看用户

**单行写法：查看所有用户**
`SELECT User, Host FROM mysql.user;`
```sql
-- 列出所有用户
SELECT User, Host FROM mysql.user;
```

**单行写法：查看当前用户**
`SELECT CURRENT_USER();`
```sql
-- 查看当前登录用户
SELECT CURRENT_USER();
```

**换行写法：查看用户权限**
`SHOW GRANTS FOR '<用户名>'@'<主机>';`
```sql
-- 查看指定用户权限
SHOW GRANTS FOR 'appuser'@'localhost';
```

**单行写法：查看当前用户权限**
`SHOW GRANTS;`
```sql
-- 查看当前登录用户权限
SHOW GRANTS;
```

---

## 权限授予与回收

**单行写法：授予所有权限**
`GRANT ALL PRIVILEGES ON <库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予某库所有表的所有权限
GRANT ALL PRIVILEGES ON mydb.* TO 'appuser'@'localhost';
```

**单行写法：授予指定权限**
`GRANT SELECT, INSERT, UPDATE ON <库>.<表> TO '<用户名>'@'<主机>';`
```sql
-- 授予增删改查权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.users TO 'appuser'@'localhost';
```

**单行写法：授予全局权限**
`GRANT <权限> ON *.* TO '<用户名>'@'<主机>';`
```sql
-- 授予全局 CREATE 权限
GRANT CREATE ON *.* TO 'appuser'@'localhost';
```

**单行写法：授予并允许授权**
`GRANT <权限> ON <库>.<表> TO '<用户>'@'<主机>' WITH GRANT OPTION;`
```sql
-- 授予权限并允许该用户授权给他人
GRANT SELECT ON mydb.* TO 'admin'@'localhost' WITH GRANT OPTION;
```

**单行写法：回收权限**
`REVOKE <权限> ON <库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 回收删除权限
REVOKE DELETE ON mydb.users FROM 'appuser'@'localhost';
```

**单行写法：回收所有权限**
`REVOKE ALL PRIVILEGES ON <库>.<表> FROM '<用户名>'@'<主机>';`
```sql
-- 回收某库所有权限
REVOKE ALL PRIVILEGES ON mydb.* FROM 'appuser'@'localhost';
```

**单行写法：刷新权限**
`FLUSH PRIVILEGES;`
```sql
-- 直接修改 user 表后刷新权限
FLUSH PRIVILEGES;
```

---

## 常用权限列表

**单行写法：授予 DML 权限**
`GRANT SELECT, INSERT, UPDATE, DELETE ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予数据操作权限
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'appuser'@'%';
```

**单行写法：授予 DDL 权限**
`GRANT CREATE, ALTER, DROP, INDEX ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予数据定义权限
GRANT CREATE, ALTER, DROP, INDEX ON mydb.* TO 'devuser'@'%';
```

**单行写法：授予只读权限**
`GRANT SELECT ON <库>.* TO '<用户>'@'<主机>';`
```sql
-- 授予只读权限
GRANT SELECT ON mydb.* TO 'readonly'@'%';
```

**单行写法：授予备份权限**
`GRANT SELECT, LOCK TABLES, RELOAD, REPLICATION CLIENT ON *.* TO '<用户>'@'<主机>';`
```sql
-- 授予 mysqldump 所需权限
GRANT SELECT, LOCK TABLES, RELOAD, REPLICATION CLIENT ON *.* TO 'backup'@'localhost';
```

---

## 角色管理（8.0+）

**单行写法：创建角色**
`CREATE ROLE '<角色名>';`
```sql
-- 创建角色
CREATE ROLE 'app_read';
```

**单行写法：给角色授权**
`GRANT SELECT ON <库>.* TO '<角色名>';`
```sql
-- 给角色授予只读权限
GRANT SELECT ON mydb.* TO 'app_read';
```

**单行写法：将角色授予用户**
`GRANT '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 把角色分配给用户
GRANT 'app_read' TO 'appuser'@'localhost';
```

**单行写法：设置默认角色**
`SET DEFAULT ROLE '<角色名>' TO '<用户名>'@'<主机>';`
```sql
-- 设置用户登录后默认激活的角色
SET DEFAULT ROLE 'app_read' TO 'appuser'@'localhost';
```

**单行写法：激活当前角色**
`SET ROLE '<角色名>';`
```sql
-- 当前会话激活指定角色
SET ROLE 'app_read';
```

**单行写法：查看当前角色**
`SELECT CURRENT_ROLE();`
```sql
-- 查看当前激活的角色
SELECT CURRENT_ROLE();
```

**单行写法：回收角色**
`REVOKE '<角色名>' FROM '<用户名>'@'<主机>';`
```sql
-- 从用户回收角色
REVOKE 'app_read' FROM 'appuser'@'localhost';
```

**单行写法：删除角色**
`DROP ROLE [IF EXISTS] '<角色名>';`
```sql
-- 删除角色
DROP ROLE IF EXISTS 'app_read';
```

---

## 密码策略

**单行写法：查看密码策略**
`SHOW VARIABLES LIKE 'validate_password%';`
```sql
-- 查看密码验证插件配置
SHOW VARIABLES LIKE 'validate_password%';
```

**单行写法：设置密码长度**
`SET GLOBAL validate_password.length = <数值>;`
```sql
-- 设置最小密码长度
SET GLOBAL validate_password.length = 12;
```

**单行写法：设置密码复杂度**
`SET GLOBAL validate_password.policy = <级别>;`
```sql
-- 设置密码策略为中等
SET GLOBAL validate_password.policy = 'MEDIUM';
```


<!-- ============ 文档分隔线：020-mysql/018-CLI.md ============ -->

# MySQL CLI 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 连接登录

**单行写法：本地连接**
`mysql -u <用户名> -p`
```bash
# 交互式输入密码登录
mysql -u root -p
```

**单行写法：指定密码连接**
`mysql -u <用户名> -p<密码>`
```bash
# 直接在命令中带密码（不推荐，会泄露）
mysql -u root -pStrongPass123!
```

**单行写法：连接远程主机**
`mysql -h <主机> -P <端口> -u <用户名> -p`
```bash
# 连接远程 MySQL 服务器
mysql -h 192.168.1.100 -P 3306 -u appuser -p
```

**单行写法：指定数据库连接**
`mysql -u <用户名> -p <数据库名>`
```bash
# 登录后直接使用指定数据库
mysql -u root -p mydb
```

**单行写法：通过 socket 连接**
`mysql -u <用户名> -p --socket=<socket路径>`
```bash
# 指定 socket 文件连接
mysql -u root -p --socket=/tmp/mysql.sock
```

**单行写法：使用配置文件连接**
`mysql --defaults-file=<配置文件>`
```bash
# 使用配置文件中的连接信息
mysql --defaults-file=/etc/mysql/my.cnf
```

---

## 客户端命令

**单行写法：查看帮助**
`mysql --help`
```bash
# 查看 mysql 客户端帮助
mysql --help
```

**单行写法：查看版本**
`mysql --version`
```bash
# 查看 MySQL 客户端版本
mysql --version
```

**单行写法：执行 SQL 后退出**
`mysql -u <用户> -p -e "<SQL语句>"`
```bash
# 执行单条 SQL 并返回
mysql -u root -p -e "SELECT VERSION();"
```

**单行写法：执行 SQL 文件**
`mysql -u <用户> -p <数据库> < <SQL文件>`
```bash
# 执行脚本文件
mysql -u root -p mydb < /path/to/script.sql
```

**单行写法：垂直显示结果**
`mysql -u <用户> -p -e "<SQL>" --vertical`
```bash
# 以垂直方式显示宽结果
mysql -u root -p -e "SELECT * FROM users" --vertical
```

**单行写法：表格输出**
`mysql -u <用户> -p -e "<SQL>" --table`
```bash
# 表格形式输出结果
mysql -u root -p -e "SELECT id, name FROM users" --table
```

**单行写法：批处理静默模式**
`mysql -u <用户> -p -s -N -e "<SQL>"`
```bash
# 静默模式去除表格边框和列名
mysql -u root -p -s -N -e "SELECT username FROM users"
```

---

## 交互式命令

**单行写法：查看所有数据库**
`SHOW DATABASES;`
```sql
-- 列出所有数据库
SHOW DATABASES;
```

**单行写法：选择数据库**
`USE <数据库名>;`
```sql
-- 切换数据库
USE mydb;
```

**单行写法：查看所有表**
`SHOW TABLES;`
```sql
-- 列出当前库所有表
SHOW TABLES;
```

**单行写法：查看表结构**
`DESC <表名>;`
```sql
-- 查看表字段
DESC users;
```

**单行写法：查看状态**
`STATUS;`
```sql
-- 查看服务器状态
STATUS;
```

**单行写法：清除当前输入**
`\c`
```sql
-- 取消当前未完成的 SQL 输入
SELECT * FROM users\c
```

**单行写法：退出客户端**
`exit;` 或 `quit;`
```sql
-- 退出 mysql 客户端
exit;
```

**单行写法：切换数据库快捷命令**
`\u <数据库名>`
```sql
-- 快速切换数据库
\u mydb
```

**单行写法：执行系统命令**
`\! <系统命令>`
```sql
-- 在 mysql 客户端中执行系统命令
\! ls -la
```

**单行写法：执行 SQL 文件**
`source <文件路径>;` 或 `\. <文件路径>`
```sql
-- 在客户端中执行 SQL 文件
source /path/to/script.sql;
```

---

## 备份恢复

**单行写法：导出数据库**
`mysqldump -u <用户> -p <数据库> > <文件>`
```bash
# 导出整个数据库
mysqldump -u root -p mydb > mydb_backup.sql
```

**单行写法：导出单张表**
`mysqldump -u <用户> -p <数据库> <表名> > <文件>`
```bash
# 仅导出 users 表
mysqldump -u root -p mydb users > users_backup.sql
```

**单行写法：导出多张表**
`mysqldump -u <用户> -p <数据库> <表1> <表2> > <文件>`
```bash
# 导出多个表
mysqldump -u root -p mydb users orders > backup.sql
```

**单行写法：导出所有数据库**
`mysqldump -u <用户> -p --all-databases > <文件>`
```bash
# 导出全部数据库
mysqldump -u root -p --all-databases > all_backup.sql
```

**单行写法：仅导出表结构**
`mysqldump -u <用户> -p --no-data <数据库> > <文件>`
```bash
# 仅导出表结构不导出数据
mysqldump -u root -p --no-data mydb > schema.sql
```

**单行写法：仅导出数据**
`mysqldump -u <用户> -p --no-create-info <数据库> > <文件>`
```bash
# 仅导出数据不导出表结构
mysqldump -u root -p --no-create-info mydb > data.sql
```

**单行写法：导入数据**
`mysql -u <用户> -p <数据库> < <文件>`
```bash
# 从备份文件恢复数据
mysql -u root -p mydb < mydb_backup.sql
```

---

## 服务管理

**单行写法：查看 MySQL 服务状态**
`systemctl status mysql`
```bash
# 查看 MySQL 服务状态
systemctl status mysql
```

**单行写法：启动 MySQL 服务**
`systemctl start mysql`
```bash
# 启动 MySQL 服务
systemctl start mysql
```

**单行写法：停止 MySQL 服务**
`systemctl stop mysql`
```bash
# 停止 MySQL 服务
systemctl stop mysql
```

**单行写法：重启 MySQL 服务**
`systemctl restart mysql`
```bash
# 重启 MySQL 服务
systemctl restart mysql
```

**单行写法：查看 MySQL 进程**
`mysqladmin -u <用户> -p processlist`
```bash
# 查看当前 MySQL 进程列表
mysqladmin -u root -p processlist
```

**单行写法：查看服务器状态**
`mysqladmin -u <用户> -p status`
```bash
# 查看 MySQL 服务器状态
mysqladmin -u root -p status
```

---

## 配置与变量

**单行写法：查看系统变量**
`SHOW VARIABLES LIKE '<模式>';`
```sql
-- 查看字符集相关变量
SHOW VARIABLES LIKE 'character%';
```

**单行写法：查看全局变量**
`SELECT @@global.<变量名>;`
```sql
-- 查看全局最大连接数
SELECT @@global.max_connections;
```

**单行写法：设置全局变量**
`SET GLOBAL <变量名> = <值>;`
```sql
-- 设置最大连接数
SET GLOBAL max_connections = 500;
```

**单行写法：查看会话变量**
`SELECT @@session.<变量名>;`
```sql
-- 查看当前会话时区
SELECT @@session.time_zone;
```

**单行写法：设置会话变量**
`SET SESSION <变量名> = <值>;`
```sql
-- 设置会话时区
SET SESSION time_zone = '+08:00';
```

**单行写法：查看状态信息**
`SHOW STATUS LIKE '<模式>';`
```sql
-- 查看连接数
SHOW STATUS LIKE 'Threads%';
```

---

## 工具命令

**单行写法：检查表**
`mysqlcheck -u <用户> -p --check <数据库>`
```bash
# 检查数据库所有表
mysqlcheck -u root -p --check mydb
```

**单行写法：修复表**
`mysqlcheck -u <用户> -p --repair <数据库>`
```bash
# 修复数据库表
mysqlcheck -u root -p --repair mydb
```

**单行写法：优化表**
`mysqlcheck -u <用户> -p --optimize <数据库>`
```bash
# 优化数据库表
mysqlcheck -u root -p --optimize mydb
```

**单行写法：分析表**
`mysqlcheck -u <用户> -p --analyze <数据库>`
```bash
# 分析表更新统计信息
mysqlcheck -u root -p --analyze mydb
```

**单行写法：查看慢查询日志**
`mysqldumpslow -s t -t <数量> <日志文件>`
```bash
# 按耗时排序查看前 10 条慢查询
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
```


<!-- ============ 文档分隔线：020-mysql/019-MysqldumpBackup.md ============ -->

# mysqldump 备份命令 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基本备份

**基本写法：备份单个数据库**
`mysqldump -u <用户名> -p <数据库名> > <输出文件>.sql`

```bash
# 备份 mydb 数据库到文件
mysqldump -u root -p mydb > mydb_backup.sql
```

**基本写法：备份多个数据库**
`mysqldump -u <用户名> -p --databases <库1> <库2> [库...] > <输出文件>`

```bash
# 同时备份多个数据库（含 CREATE DATABASE 语句）
mysqldump -u root -p --databases db1 db2 db3 > multi_db.sql
```

**基本写法：备份所有数据库**
`mysqldump -u <用户名> -p --all-databases > <输出文件>`

```bash
# 全库备份
mysqldump -u root -p --all-databases > all_db_backup.sql
```

**基本写法：仅备份结构**
`mysqldump -u <用户名> -p --no-data <数据库名> > <输出文件>`

```bash
# 仅导出表结构（不包含数据）
mysqldump -u root -p --no-data mydb > mydb_schema.sql
```

**基本写法：仅备份数据**
`mysqldump -u <用户名> -p --no-create-info <数据库名> > <输出文件>`

```bash
# 仅导出数据（不含建表语句）
mysqldump -u root -p --no-create-info mydb > mydb_data.sql
```

---

## 指定表与条件

**基本写法：备份指定表**
`mysqldump -u <用户名> -p <数据库名> <表1> [表2...] > <输出文件>`

```bash
# 仅备份 users 和 orders 两张表
mysqldump -u root -p mydb users orders > tables_backup.sql
```

**基本写法：按条件备份（WHERE）**
`mysqldump -u <用户名> -p <数据库名> <表名> --where="<条件>" > <输出文件>`

```bash
# 仅备份 id 小于 1000 的记录
mysqldump -u root -p mydb users --where="id < 1000" > users_partial.sql
```

---

## 远程与压缩

**基本写法：备份远程数据库**
`mysqldump -h <主机> -P <端口> -u <用户名> -p <数据库名> > <输出文件>`

```bash
# 备份远程 MySQL 服务器
mysqldump -h 192.168.1.100 -P 3306 -u admin -p mydb > remote_backup.sql
```

**基本写法：管道压缩备份**
`mysqldump -u <用户名> -p <数据库名> | gzip > <输出文件>.sql.gz`

```bash
# 压缩备份减少磁盘占用
mysqldump -u root -p mydb | gzip > mydb_backup.sql.gz
```

**基本写法：解压恢复**
`gunzip -c <压缩文件>.sql.gz | mysql -u <用户名> -p <数据库名>`

```bash
# 解压并恢复数据库
gunzip -c mydb_backup.sql.gz | mysql -u root -p mydb
```

---

## 关键选项

**基本写法：兼容版本输出（8.4 新增 --output-as-version）**
`mysqldump -u <用户名> -p --output-as-version=<版本标识> <数据库名> > <输出文件>`

```bash
# 输出兼容 8.0.23 之前版本的语法
mysqldump -u root -p --output-as-version=BEFORE_8_0_23 mydb > compat.sql
```

**基本写法：事务一致性备份**
`mysqldump -u <用户名> -p --single-transaction --quick --routines --triggers <数据库名> > <输出文件>`

```bash
# InnoDB 一致性快照备份（推荐，不锁表）
mysqldump -u root -p --single-transaction --quick --routines --triggers mydb > consistent.sql
```

**基本写法：包含存储过程与事件**
`mysqldump -u <用户名> -p --routines --events --triggers <数据库名> > <输出文件>`

```bash
# 完整备份含存储过程、函数、事件、触发器
mysqldump -u root -p --routines --events --triggers --single-transaction mydb > full.sql
```

---

## 恢复数据

**基本写法：从文件恢复**
`mysql -u <用户名> -p <数据库名> < <备份文件>.sql`

```bash
# 恢复备份到指定数据库
mysql -u root -p mydb < mydb_backup.sql
```

**基本写法：源命令恢复**
`SOURCE <备份文件路径>`

```sql
-- 在 mysql 客户端内执行
SOURCE /backup/mydb_backup.sql;
```

---


<!-- ============ 文档分隔线：020-mysql/020-Mysqladmin.md ============ -->

# mysqladmin 管理命令 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 服务状态检查

**基本写法：检查服务器存活**
`mysqladmin -u <用户名> -p ping`

```bash
# 检测 MySQL 服务是否运行（返回 mysqld is alive）
mysqladmin -u root -p ping
```

**基本写法：查看服务器状态**
`mysqladmin -u <用户名> -p status`

```bash
# 查看连接数、运行时间等概览
mysqladmin -u root -p status
# 输出: Uptime: 3600  Threads: 5  Questions: 1234  Slow queries: 0  Opens: 100
```

**基本写法：查看扩展状态**
`mysqladmin -u <用户名> -p extended-status`

```bash
# 查看所有状态变量
mysqladmin -u root -p extended-status
# 查看特定状态变量
mysqladmin -u root -p extended-status | grep -i thread
```

**基本写法：查看版本信息**
`mysqladmin -u <用户名> -p version`

```bash
# 查看 MySQL 版本与协议信息
mysqladmin -u root -p version
```

---

## 进程与连接管理

**基本写法：查看进程列表**
`mysqladmin -u <用户名> -p processlist`

```bash
# 查看当前所有连接与执行的 SQL
mysqladmin -u root -p processlist
```

**基本写法：杀掉指定连接**
`mysqladmin -u <用户名> -p kill <连接ID> [<连接ID2> ...]`

```bash
# 终止指定会话（ID 来自 processlist）
mysqladmin -u root -p kill 1234 5678
```

**基本写法：杀掉某用户所有连接**
`mysqladmin -u <用户名> -p kill $(mysqladmin -u root -p processlist | grep <用户名> | awk '{print $2}')`

```bash
# 终止某用户的所有连接
mysqladmin -u root -p kill $(mysqladmin -u root -ppass processlist | grep appuser | awk '{print $2}')
```

---

## 服务控制

**基本写法：关闭服务器**
`mysqladmin -u <用户名> -p shutdown`

```bash
# 安全关闭 MySQL 服务
mysqladmin -u root -p shutdown
```

**基本写法：刷新权限**
`mysqladmin -u <用户名> -p flush-privileges`

```bash
# 重新加载授权表（8.4 需 FLUSH_PRIVILEGES 权限）
mysqladmin -u root -p flush-privileges
```

**基本写法：刷新日志**
`mysqladmin -u <用户名> -p flush-logs`

```bash
# 关闭并重新打开日志文件（轮转二进制日志）
mysqladmin -u root -p flush-logs
```

**基本写法：刷新主机缓存**
`mysqladmin -u <用户名> -p flush-hosts`

```bash
# 清空主机缓存（8.4 FLUSH HOSTS 已移除，等价于 TRUNCATE host_cache）
mysqladmin -u root -p flush-hosts
```

**基本写法：刷新表**
`mysqladmin -u <用户名> -p flush-tables`

```bash
# 关闭所有打开的表并刷新缓存
mysqladmin -u root -p flush-tables
```

**基本写法：刷新状态变量**
`mysqladmin -u <用户名> -p flush-status`

```bash
# 重置大多数状态变量为 0
mysqladmin -u root -p flush-status
```

---

## 密码与变量

**基本写法：修改用户密码**
`mysqladmin -u <用户名> -p password "<新密码>"`

```bash
# 修改当前用户密码
mysqladmin -u root -p password "NewStrongPass123!"
```

**基本写法：查看/设置变量**
`mysqladmin -u <用户名> -p variables`

```bash
# 查看所有系统变量
mysqladmin -u root -p variables
# 过滤查看字符集相关变量
mysqladmin -u root -p variables | grep -i character
```

**基本写法：动态设置变量**
`mysqladmin -u <用户名> -p variable-set "<变量名>=<值>"`

```bash
# 在线调整最大连接数
mysqladmin -u root -p variable-set max_connections=500
```

---

## 其他常用

**基本写法：重新加载授权表并刷新**
`mysqladmin -u <用户名> -p reload`

```bash
# 重新加载授权表（等同 flush-privileges）
mysqladmin -u root -p reload
```

**基本写法：刷新线程缓存**
`mysqladmin -u <用户名> -p flush-threads`

```bash
# 清空线程缓存
mysqladmin -u root -p flush-threads
```

**基本写法：刷新查询缓存（8.0 前可用）**
`mysqladmin -u <用户名> -p refresh`

```bash
# 刷新表并刷新日志
mysqladmin -u root -p refresh
```

---


<!-- ============ 文档分隔线：020-mysql/021-StorageEngine.md ============ -->

# 存储引擎 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 引擎查看

**基本写法：查看服务器支持的引擎**
`SHOW ENGINES;`

```sql
-- 查看所有存储引擎及默认引擎
SHOW ENGINES;
```

**基本写法：查看当前默认引擎**
`SHOW VARIABLES LIKE 'default_storage_engine';`

```sql
-- 查看默认存储引擎（MySQL 8.0+ 默认 InnoDB）
SHOW VARIABLES LIKE 'default_storage_engine';
```

**基本写法：查看表使用的引擎**
`SHOW TABLE STATUS FROM <数据库名> [LIKE '<表名>'];`

```sql
-- 查看 mydb 库所有表的引擎
SHOW TABLE STATUS FROM mydb;
-- 查看指定表引擎
SHOW TABLE STATUS FROM mydb LIKE 'users';
```

---

## 引擎指定与修改

**基本写法：建表时指定引擎**
`CREATE TABLE <表名> (...) ENGINE = <引擎名>;`

```sql
-- 创建 InnoDB 表（默认）
CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  amount DECIMAL(10,2)
) ENGINE = InnoDB;

-- 创建 MyISAM 表（只读分析场景）
CREATE TABLE logs (
  id BIGINT PRIMARY KEY,
  msg TEXT
) ENGINE = MyISAM;
```

**基本写法：修改表引擎**
`ALTER TABLE <表名> ENGINE = <新引擎>;`

```sql
-- 将 MyISAM 表转为 InnoDB（支持事务）
ALTER TABLE logs ENGINE = InnoDB;
```

---

## InnoDB 配置

**基本写法：查看 InnoDB 状态**
`SHOW ENGINE INNODB STATUS;`

```sql
-- 查看 InnoDB 内部状态（锁、死锁、缓冲池等）
SHOW ENGINE INNODB STATUS\G
```

**基本写法：查看 InnoDB 缓冲池状态**
`SELECT * FROM information_schema.INNODB_BUFFER_POOL_STATS;`

```sql
-- 查看缓冲池命中率与页信息
SELECT
  pool_id, pool_size, free_buffers, database_pages,
  hit_rate FROM information_schema.INNODB_BUFFER_POOL_STATS;
```

**基本写法：查看 InnoDB 数据字典**
`SELECT * FROM information_schema.INNODB_TABLES WHERE name LIKE '<库>/<表>';`

```sql
-- 查看 InnoDB 内部表元数据
SELECT * FROM information_schema.INNODB_TABLES WHERE name LIKE 'mydb/users';
```

---

## 引擎特性对比命令

**基本写法：查看表行格式与特性**
`SHOW TABLE STATUS FROM <库> LIKE '<表>'\G`

```sql
-- 查看 orders 表的行格式、数据长度、索引长度等
SHOW TABLE STATUS FROM mydb LIKE 'orders'\G
```

**基本写法：查看 InnoDB 页大小**
`SHOW VARIABLES LIKE 'innodb_page_size';`

```sql
-- 查看 InnoDB 页大小（默认 16K）
SHOW VARIABLES LIKE 'innodb_page_size';
```

---

## MyISAM 与 MEMORY 操作

**基本写法：MyISAM 表检查**
`CHECK TABLE <表名> [QUICK|FAST|MEDIUM|EXTENDED];`

```sql
-- 检查 MyISAM 表完整性
CHECK TABLE logs MEDIUM;
```

**基本写法：MyISAM 表修复**
`REPAIR TABLE <表名> [QUICK|EXTENDED];`

```sql
-- 修复损坏的 MyISAM 表
REPAIR TABLE logs EXTENDED;
```

**基本写法：优化表（回收空间）**
`OPTIMIZE TABLE <表名> [, <表2> ...];`

```sql
-- 优化表回收碎片空间（8.4 需 OPTIMIZE_LOCAL_TABLE 权限才可免 binlog）
OPTIMIZE TABLE users, orders;
```

**基本写法：MEMORY 引擎建表**
`CREATE TABLE <表名> (...) ENGINE = MEMORY [MAX_ROWS = <行数>];`

```sql
-- 创建内存表（数据不持久化，重启丢失）
CREATE TABLE session_cache (
  sid VARCHAR(64) PRIMARY KEY,
  data TEXT
) ENGINE = MEMORY MAX_ROWS = 10000;
```

---


<!-- ============ 文档分隔线：020-mysql/022-View.md ============ -->

# 视图 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建视图

**基本写法：创建视图**
`CREATE VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 创建用户概览视图
CREATE VIEW v_user_summary AS
SELECT
  user_id,
  user_name,
  email,
  created_at
FROM users
WHERE status = 'active';
```

**基本写法：创建或替换视图**
`CREATE OR REPLACE VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 已存在则替换，避免 DROP 再建
CREATE OR REPLACE VIEW v_user_summary AS
SELECT user_id, user_name, email, last_login
FROM users;
```

**基本写法：指定列名创建视图**
`CREATE VIEW <视图名> (<列1>, <列2>, ...) AS <SELECT 语句>;`

```sql
-- 显式指定视图列名
CREATE VIEW v_orders (订单号, 客户, 金额) AS
SELECT order_id, customer_name, amount FROM orders;
```

**基本写法：带检查选项创建视图**
`CREATE VIEW <视图名> AS <SELECT 语句> [WITH CHECK OPTION];`

```sql
-- 通过视图插入的数据必须满足视图 WHERE 条件
CREATE VIEW v_active_users AS
SELECT * FROM users WHERE status = 'active'
WITH CHECK OPTION;
```

**基本写法：级联/本地检查选项**
`CREATE VIEW <视图名> AS <SELECT> WITH [CASCADED|LOCAL] CHECK OPTION;`

```sql
-- CASCADED 检查所有依赖视图（默认），LOCAL 仅检查当前视图
CREATE VIEW v_vip AS
SELECT * FROM v_active_users WHERE vip_level > 3
WITH CASCADED CHECK OPTION;
```

---

## 查询视图

**基本写法：查询视图**
`SELECT <列> FROM <视图名> [WHERE <条件>];`

```sql
-- 像普通表一样查询视图
SELECT user_name, email FROM v_user_summary WHERE user_id = 100;
```

**基本写法：查看视图定义**
`SHOW CREATE VIEW <视图名>;`

```sql
-- 查看视图创建语句
SHOW CREATE VIEW v_user_summary\G
```

**基本写法：查看视图元数据**
`SELECT * FROM information_schema.VIEWS WHERE table_name = '<视图名>';`

```sql
-- 查询视图定义与检查选项
SELECT table_schema, table_name, view_definition, check_option
FROM information_schema.VIEWS
WHERE table_name = 'v_user_summary';
```

---

## 修改视图

**基本写法：ALTER 修改视图**
`ALTER VIEW <视图名> AS <SELECT 语句>;`

```sql
-- 修改视图定义
ALTER VIEW v_user_summary AS
SELECT user_id, user_name, phone, last_login
FROM users
WHERE status = 'active';
```

**基本写法：修改视图 SQL 安全上下文**
`ALTER VIEW <视图名> SQL SECURITY {DEFINER|INVOKER} AS <SELECT 语句>;`

```sql
-- 以调用者权限执行（8.4 需 SET_ANY_DEFINER 权限指定他人 DEFINER）
ALTER VIEW v_user_summary
SQL SECURITY INVOKER
AS SELECT user_id, user_name FROM users;
```

---

## 删除视图

**基本写法：删除视图**
`DROP VIEW [IF EXISTS] <视图名> [, <视图2> ...];`

```sql
-- 安全删除视图
DROP VIEW IF EXISTS v_user_summary, v_orders;
```

---

## 可更新视图

**基本写法：通过视图插入数据**
`INSERT INTO <视图名> (<列>) VALUES (<值>);`

```sql
-- 通过视图插入（视图需包含基表所有非空列）
INSERT INTO v_active_users (user_name, email, status)
VALUES ('张三', 'zhangsan@example.com', 'active');
```

**基本写法：通过视图更新数据**
`UPDATE <视图名> SET <列> = <值> WHERE <条件>;`

```sql
-- 通过视图更新基表数据
UPDATE v_user_summary SET email = 'new@example.com' WHERE user_id = 100;
```

**基本写法：通过视图删除数据**
`DELETE FROM <视图名> WHERE <条件>;`

```sql
-- 通过视图删除基表数据
DELETE FROM v_active_users WHERE user_id = 100;
```

---


<!-- ============ 文档分隔线：020-mysql/023-EventScheduler.md ============ -->

# 事件调度器 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 调度器开关

**基本写法：查看事件调度器状态**
`SHOW VARIABLES LIKE 'event_scheduler';`

```sql
-- 查看事件调度器是否开启
SHOW VARIABLES LIKE 'event_scheduler';
-- 输出: event_scheduler | ON / OFF
```

**基本写法：开启事件调度器**
`SET GLOBAL event_scheduler = ON;`

```sql
-- 全局开启事件调度器（运行时生效，重启失效）
SET GLOBAL event_scheduler = ON;
```

**基本写法：配置文件持久开启**
`event_scheduler = ON`

```ini
# my.cnf 中配置，重启后持久生效
[mysqld]
event_scheduler = ON
```

---

## 创建事件

**基本写法：一次性事件**
`CREATE EVENT <事件名> ON SCHEDULE AT <时间点> DO <SQL 语句>;`

```sql
-- 在指定时间执行一次
CREATE EVENT e_clean_logs
ON SCHEDULE AT '2024-12-31 23:59:59'
DO DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：当前时间延迟执行**
`CREATE EVENT <事件名> ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL <数值> <单位> DO <SQL>;`

```sql
-- 1 小时后执行一次
CREATE EVENT e_notify
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
DO UPDATE users SET notified = 1 WHERE last_login < NOW() - INTERVAL 7 DAY;
```

**基本写法：周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <数值> <单位> DO <SQL 语句>;`

```sql
-- 每天执行一次清理
CREATE EVENT e_daily_clean
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：指定起止时间的周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <间隔> STARTS <开始> ENDS <结束> DO <SQL>;`

```sql
-- 每小时执行，限定起止时间
CREATE EVENT e_hourly_stat
ON SCHEDULE EVERY 1 HOUR
STARTS '2024-01-01 00:00:00'
ENDS '2024-12-31 23:59:59'
DO CALL sp_calc_hourly_stats();
```

**基本写法：复合语句事件**
`CREATE EVENT <事件名> ON SCHEDULE <调度> DO BEGIN <语句1>; <语句2>; END`

```sql
-- 执行多条语句需用 BEGIN...END 包裹并重置分隔符
DELIMITER //
CREATE EVENT e_multi ON SCHEDULE EVERY 1 DAY
DO BEGIN
  DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
  UPDATE stats SET count = 0 WHERE stat_date = CURDATE();
END //
DELIMITER ;
```

---

## 事件管理

**基本写法：查看事件**
`SHOW EVENTS [FROM <数据库名>] [LIKE '<模式>'];`

```sql
-- 查看当前库所有事件
SHOW EVENTS;
-- 查看指定库事件
SHOW EVENTS FROM mydb LIKE 'e_%';
```

**基本写法：查看事件定义**
`SHOW CREATE EVENT <事件名>;`

```sql
-- 查看事件创建语句
SHOW CREATE EVENT e_daily_clean\G
```

**基本写法：查看事件元数据**
`SELECT * FROM information_schema.EVENTS WHERE event_name = '<事件名>';`

```sql
-- 查询事件状态与调度信息
SELECT event_name, last_executed, status, interval_value, interval_field
FROM information_schema.EVENTS
WHERE event_schema = 'mydb';
```

---

## 修改与删除

**基本写法：禁用/启用事件**
`ALTER EVENT <事件名> {DISABLE|ENABLE};`

```sql
-- 临时禁用事件
ALTER EVENT e_daily_clean DISABLE;
-- 重新启用
ALTER EVENT e_daily_clean ENABLE;
```

**基本写法：修改事件调度**
`ALTER EVENT <事件名> ON SCHEDULE <新调度> DO <SQL>;`

```sql
-- 修改执行周期为每周一次
ALTER EVENT e_daily_clean
ON SCHEDULE EVERY 1 WEEK STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：重命名事件**
`ALTER EVENT <旧事件名> RENAME TO <新事件名>;`

```sql
-- 重命名事件
ALTER EVENT e_daily_clean RENAME TO e_weekly_clean;
```

**基本写法：删除事件**
`DROP EVENT [IF EXISTS] <事件名>;`

```sql
-- 安全删除事件
DROP EVENT IF EXISTS e_weekly_clean;
```

---


<!-- ============ 文档分隔线：020-mysql/024-CharsetCollation.md ============ -->

# 字符集与排序规则 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看字符集

**基本写法：查看可用字符集**
`SHOW CHARACTER SET [LIKE '<模式>'];`

```sql
-- 查看所有字符集
SHOW CHARACTER SET;
-- 过滤查看 utf8mb4 相关
SHOW CHARACTER SET LIKE 'utf8%';
```

**基本写法：查看可用排序规则**
`SHOW COLLATION [LIKE '<模式>'];`

```sql
-- 查看 utf8mb4 的所有排序规则
SHOW COLLATION LIKE 'utf8mb4%';
```

**基本写法：查看当前字符集变量**
`SHOW VARIABLES LIKE 'character_set%';`

```sql
-- 查看连接、服务、数据库等字符集设置
SHOW VARIABLES LIKE 'character_set%';
```

**基本写法：查看排序规则变量**
`SHOW VARIABLES LIKE 'collation%';`

```sql
-- 查看连接与服务排序规则
SHOW VARIABLES LIKE 'collation%';
```

---

## 数据库级设置

**基本写法：建库时指定字符集**
`CREATE DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 创建 utf8mb4 库（推荐，支持完整 emoji）
CREATE DATABASE mydb
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
```

**基本写法：修改库字符集**
`ALTER DATABASE <库名> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 将库转为 utf8mb4
ALTER DATABASE mydb
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
```

---

## 表级设置

**基本写法：建表时指定字符集**
`CREATE TABLE <表名> (...) CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 建表指定字符集与排序规则
CREATE TABLE users (
  id BIGINT PRIMARY KEY,
  name VARCHAR(50)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

**基本写法：修改表字符集**
`ALTER TABLE <表名> CONVERT TO CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 转换表字符集（同时转换已有数据编码）
ALTER TABLE users
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;
```

**基本写法：仅修改表默认字符集（不转换数据）**
`ALTER TABLE <表名> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 只改默认字符集，不影响已有列数据
ALTER TABLE users CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

---

## 列级设置

**基本写法：列指定字符集**
`<列名> <字符类型>(<长度>) CHARACTER SET <字符集> COLLATE <排序规则>`

```sql
-- 指定列使用 utf8mb4 与区分大小写排序规则
CREATE TABLE articles (
  id BIGINT PRIMARY KEY,
  title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs,
  content TEXT CHARACTER SET utf8mb4
);
```

**基本写法：修改列字符集**
`ALTER TABLE <表名> MODIFY <列名> <类型> CHARACTER SET <字符集> COLLATE <排序规则>;`

```sql
-- 修改列字符集
ALTER TABLE articles
MODIFY title VARCHAR(200)
CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

---

## 连接级设置

**基本写法：设置连接字符集**
`SET NAMES <字符集> [COLLATE <排序规则>];`

```sql
-- 设置客户端、连接、结果字符集（最常用）
SET NAMES utf8mb4;
```

**基本写法：设置单个字符集变量**
`SET <变量名> = <字符集>;`

```sql
-- 分别设置各环节字符集
SET character_set_client = utf8mb4;
SET character_set_connection = utf8mb4;
SET character_set_results = utf8mb4;
```

---

## 排序规则后缀说明

**基本写法：排序规则后缀含义**
`<字符集>_<版本>_<强弱>_<重音>_<大小写>`

```sql
-- utf8mb4_0900_ai_ci 含义：
-- 0900: Unicode 9.0 标准
-- ai:    accent-insensitive 不区分重音
-- cs:    case-sensitive 区分大小写（_as 区分重音）
-- _bin:  二进制比较
-- 区分大小写排序规则示例
SELECT * FROM users ORDER BY name COLLATE utf8mb4_0900_as_cs;
```

**基本写法：查询时指定排序规则**
`ORDER BY <列> COLLATE <排序规则>`

```sql
-- 临时使用区分大小写的排序
SELECT * FROM users ORDER BY name COLLATE utf8mb4_0900_as_cs;
```

**基本写法：比较时强制排序规则**
`<表达式> COLLATE <排序规则> = <表达式>`

```sql
-- 跨排序规则比较时需统一
SELECT * FROM a JOIN b ON a.name COLLATE utf8mb4_0900_ai_ci = b.name;
```

---


<!-- ============ 文档分隔线：020-mysql/025-PartitionTable.md ============ -->

# 分区表 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## RANGE 分区

**基本写法：RANGE 分区建表**
`CREATE TABLE <表名> (...) PARTITION BY RANGE (<表达式>) (PARTITION <分区名> VALUES LESS THAN (<值>), ...)`

```sql
-- 按年份范围分区
CREATE TABLE orders (
  id BIGINT PRIMARY KEY,
  order_date DATE,
  amount DECIMAL(10,2)
)
PARTITION BY RANGE (YEAR(order_date)) (
  PARTITION p2022 VALUES LESS THAN (2023),
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION p2024 VALUES LESS THAN (2025),
  PARTITION pmax VALUES LESS THAN MAXVALUE
);
```

**基本写法：RANGE COLUMNS 多列分区**
`PARTITION BY RANGE COLUMNS(<列1>, <列2>) (PARTITION <名> VALUES LESS THAN (<值1>, <值2>), ...)`

```sql
-- 按多列组合范围分区
CREATE TABLE sales (
  id BIGINT,
  region VARCHAR(20),
  sale_date DATE
)
PARTITION BY RANGE COLUMNS(region, sale_date) (
  PARTITION p_east_2024 VALUES LESS THAN ('EAST', '2025-01-01'),
  PARTITION p_west_2024 VALUES LESS THAN ('WEST', '2025-01-01'),
  PARTITION p_other VALUES LESS THAN (MAXVALUE, MAXVALUE)
);
```

---

## LIST 分区

**基本写法：LIST 分区建表**
`CREATE TABLE <表名> (...) PARTITION BY LIST (<表达式>) (PARTITION <分区名> VALUES IN (<值列表>), ...)`

```sql
-- 按地区枚举分区
CREATE TABLE customers (
  id BIGINT PRIMARY KEY,
  region_code INT
)
PARTITION BY LIST (region_code) (
  PARTITION p_north VALUES IN (1, 2, 3),
  PARTITION p_south VALUES IN (4, 5, 6),
  PARTITION p_east VALUES IN (7, 8),
  PARTITION p_west VALUES IN (9, 10)
);
```

**基本写法：LIST COLUMNS 多列分区**
`PARTITION BY LIST COLUMNS(<列>) (PARTITION <名> VALUES IN (<值列表>), ...)`

```sql
-- 按字符串列分区
CREATE TABLE users (
  id BIGINT,
  country VARCHAR(10)
)
PARTITION BY LIST COLUMNS(country) (
  PARTITION p_cn VALUES IN ('CN', 'HK', 'TW'),
  PARTITION p_us VALUES IN ('US', 'CA'),
  PARTITION p_other VALUES IN ('UK', 'FR', 'DE')
);
```

---

## HASH 与 KEY 分区

**基本写法：HASH 分区**
`CREATE TABLE <表名> (...) PARTITION BY HASH(<表达式>) PARTITIONS <分区数>;`

```sql
-- 按用户 ID 哈希分 8 个区
CREATE TABLE user_logs (
  id BIGINT,
  user_id BIGINT,
  log_text TEXT
)
PARTITION BY HASH(user_id)
PARTITIONS 8;
```

**基本写法：LINEAR HASH 分区**
`PARTITION BY LINEAR HASH(<表达式>) PARTITIONS <分区数>;`

```sql
-- 线性哈希，增删分区更快但分布可能不均
CREATE TABLE t_logs (id BIGINT)
PARTITION BY LINEAR HASH(id)
PARTITIONS 16;
```

**基本写法：KEY 分区**
`PARTITION BY KEY(<列>) PARTITIONS <分区数>;`

```sql
-- KEY 分区由 MySQL 内部哈希，类似主键哈希
CREATE TABLE user_events (
  id BIGINT PRIMARY KEY,
  event VARCHAR(50)
)
PARTITION BY KEY()
PARTITIONS 4;
```

---

## 分区管理

**基本写法：添加分区**
`ALTER TABLE <表名> ADD PARTITION (PARTITION <分区名> VALUES LESS THAN (<值>));`

```sql
-- 为 RANGE 分区表添加新分区
ALTER TABLE orders
ADD PARTITION (
  PARTITION p2025 VALUES LESS THAN (2026)
);
```

**基本写法：删除分区**
`ALTER TABLE <表名> DROP PARTITION <分区名>;`

```sql
-- 删除分区（连同数据一起删除）
ALTER TABLE orders DROP PARTITION p2022;
```

**基本写法：重组分区**
`ALTER TABLE <表名> REORGANIZE PARTITION <分区名> INTO (PARTITION <新分区> ...);`

```sql
-- 将 p2024 拆分为 p2024_h1 和 p2024_h2
ALTER TABLE orders
REORGANIZE PARTITION p2024 INTO (
  PARTITION p2024_h1 VALUES LESS THAN ('2024-07-01'),
  PARTITION p2024_h2 VALUES LESS THAN (2025)
);
```

**基本写法：合并分区**
`ALTER TABLE <表名> REORGANIZE PARTITION <分区1>, <分区2> INTO (PARTITION <新分区> ...);`

```sql
-- 合并两个相邻分区
ALTER TABLE orders
REORGANIZE PARTITION p2024_h1, p2024_h2 INTO (
  PARTITION p2024 VALUES LESS THAN (2025)
);
```

---

## 分区维护

**基本写法：查看分区信息**
`SELECT * FROM information_schema.PARTITIONS WHERE table_name = '<表名>';`

```sql
-- 查看表分区、行数、数据长度
SELECT partition_name, partition_method, table_rows, data_length
FROM information_schema.PARTITIONS
WHERE table_name = 'orders';
```

**基本写法：检查分区**
`ALTER TABLE <表名> CHECK PARTITION <分区名>;`

```sql
-- 检查指定分区数据完整性
ALTER TABLE orders CHECK PARTITION p2024;
```

**基本写法：重建分区**
`ALTER TABLE <表名> REBUILD PARTITION <分区名>;`

```sql
-- 重建分区回收碎片
ALTER TABLE orders REBUILD PARTITION p2023;
```

**基本写法：分析分区**
`ALTER TABLE <表名> ANALYZE PARTITION <分区名>;`

```sql
-- 重新收集分区统计信息
ALTER TABLE orders ANALYZE PARTITION p2024;
```

**基本写法：移除分区（保留数据）**
`ALTER TABLE <表名> REMOVE PARTITIONING;`

```sql
-- 移除分区结构但保留数据为普通表
ALTER TABLE orders REMOVE PARTITIONING;
```

---


<!-- ============ 文档分隔线：020-mysql/026-ReplicationBinlog.md ============ -->

# 复制与 binlog 命令 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 复制术语（8.4 SOURCE/REPLICA）

**基本写法：查看源库二进制日志状态**
`SHOW BINARY LOG STATUS;`

```sql
-- MySQL 8.4 新语法（替代旧版 SHOW MASTER STATUS）
SHOW BINARY LOG STATUS;
-- 输出: File=mysql-bin.000003, Position=1234, Binlog_Do_DB, Binlog_Ignore_DB
```

**基本写法：查看副本状态**
`SHOW REPLICA STATUS\G`

```sql
-- MySQL 8.4 新语法（替代旧版 SHOW SLAVE STATUS）
SHOW REPLICA STATUS\G
```

**基本写法：查看复制源**
`SHOW REPLICA STATUS FOR CHANNEL '<通道名>'\G`

```sql
-- 查看指定复制通道状态（多源复制）
SHOW REPLICA STATUS FOR CHANNEL 'source_1'\G
```

---

## 副本控制

**基本写法：启动复制**
`START REPLICA [FOR CHANNEL '<通道名>'];`

```sql
-- 启动所有复制线程
START REPLICA;
-- 启动指定通道
START REPLICA FOR CHANNEL 'source_1';
```

**基本写法：停止复制**
`STOP REPLICA [FOR CHANNEL '<通道名>'];`

```sql
-- 停止复制线程
STOP REPLICA;
-- 停止 IO 线程或 SQL 线程
STOP REPLICA IO_THREAD;
STOP REPLICA SQL_THREAD;
```

**基本写法：重置副本**
`RESET REPLICA [ALL] [FOR CHANNEL '<通道名>'];`

```sql
-- 清除副本元数据与中继日志（替换旧 RESET SLAVE）
RESET REPLICA;
-- 彻底删除通道（含元数据）
RESET REPLICA ALL FOR CHANNEL 'source_1';
```

**基本写法：配置复制源**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_PORT=<端口>, SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_LOG_FILE='<日志文件>', SOURCE_LOG_POS=<位置>;`

```sql
-- 配置主从复制源（8.4 新语法，替代 CHANGE MASTER TO）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_LOG_FILE='mysql-bin.000003',
  SOURCE_LOG_POS=1234,
  GET_SOURCE_PUBLIC_KEY=1;
```

---

## 二进制日志管理

**基本写法：查看二进制日志列表**
`SHOW BINARY LOGS;`

```sql
-- 查看所有 binlog 文件及大小
SHOW BINARY LOGS;
```

**基本写法：查看 binlog 事件**
`SHOW BINLOG EVENTS [IN '<日志文件>'] [FROM <位置>] [LIMIT <偏移>, <行数>];`

```sql
-- 查看指定 binlog 事件
SHOW BINLOG EVENTS IN 'mysql-bin.000003' FROM 1234 LIMIT 10;
```

**基本写法：查看 binlog 格式**
`SHOW VARIABLES LIKE 'binlog_format';`

```sql
-- 查看 binlog 格式（ROW/STATEMENT/MIXED）
SHOW VARIABLES LIKE 'binlog_format';
```

**基本写法：删除旧 binlog**
`PURGE BINARY LOGS TO '<保留文件>';`

```sql
-- 删除指定文件之前的所有 binlog
PURGE BINARY LOGS TO 'mysql-bin.000010';
```

**基本写法：按时间删除 binlog**
`PURGE BINARY LOGS BEFORE '<日期时间>';`

```sql
-- 删除指定时间之前的 binlog
PURGE BINARY LOGS BEFORE '2024-12-01 00:00:00';
```

**基本写法：自动过期配置**
`SET GLOBAL binlog_expire_logs_seconds = <秒数>;`

```sql
-- 设置 binlog 自动过期（默认 30 天）
SET GLOBAL binlog_expire_logs_seconds = 604800;  -- 7 天
```

---

## binlog 工具

**基本写法：mysqlbinlog 查看日志**
`mysqlbinlog <选项> <日志文件>`

```bash
# 查看二进制日志内容
mysqlbinlog mysql-bin.000003
# 指定时间范围
mysqlbinlog --start-datetime="2024-12-01 00:00:00" --stop-datetime="2024-12-02 00:00:00" mysql-bin.000003
```

**基本写法：mysqlbinlog 重放恢复**
`mysqlbinlog <日志文件> | mysql -u <用户名> -p <数据库名>`

```bash
# 基于位置恢复
mysqlbinlog --start-position=1234 --stop-position=5678 mysql-bin.000003 | mysql -u root -p mydb
```

**基本写法：基于 GTID 恢复**
`mysqlbinlog --exclude-gtids='<GTID集合>' <日志文件>`

```bash
# 排除指定 GTID 事务进行恢复
mysqlbinlog --exclude-gtids='3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5' mysql-bin.000003 | mysql -u root -p
```

---

## 复制过滤

**基本写法：配置复制过滤规则**
`CHANGE REPLICATION FILTER <过滤类型> = (<规则>);`

```sql
-- 仅复制指定库
CHANGE REPLICATION FILTER REPLICATE_DO_DB = (mydb);
-- 排除指定库
CHANGE REPLICATION FILTER REPLICATE_IGNORE_DB = (test, tmp);
-- 仅复制指定表
CHANGE REPLICATION FILTER REPLICATE_DO_TABLE = (mydb.users, mydb.orders);
```

---


<!-- ============ 文档分隔线：020-mysql/027-PerformanceProfiling.md ============ -->

# 性能分析 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## EXPLAIN 执行计划

**基本写法：查看执行计划**
`EXPLAIN <SELECT 语句>;`

```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE age > 18;
```

**基本写法：EXPLAIN 输出连接信息**
`EXPLAIN FORMAT=TREE <SELECT 语句>;`

```sql
-- MySQL 8.0+ 树形输出，显示 join 顺序与成本
EXPLAIN FORMAT=TREE
SELECT u.user_name, o.amount
FROM users u JOIN orders o ON u.id = o.user_id;
```

**基本写法：EXPLAIN ANALYZE 实际执行**
`EXPLAIN ANALYZE <SELECT 语句>;`

```sql
-- MySQL 8.0.18+ 实际执行并统计耗时（注意会真实执行 DML）
EXPLAIN ANALYZE
SELECT COUNT(*) FROM orders WHERE create_time > '2024-01-01';
```

**基本写法：EXPLAIN 语句类型**
`EXPLAIN <语句类型> <SQL 语句>`

```sql
-- 查看 INSERT/UPDATE/DELETE 执行计划
EXPLAIN UPDATE users SET status = 0 WHERE last_login < NOW() - INTERVAL 90 DAY;
EXPLAIN DELETE FROM logs WHERE created_at < '2023-01-01';
```

---

## EXPLAIN 关键列

**基本写法：分析 type 访问类型**
`EXPLAIN SELECT ... -- 关注 type 列`

```sql
-- type 取值从优到差：system > const > eq_ref > ref > range > index > ALL
-- const: 主键或唯一索引等值查询
EXPLAIN SELECT * FROM users WHERE id = 100;
-- range: 索引范围扫描
EXPLAIN SELECT * FROM orders WHERE id BETWEEN 1 AND 100;
```

**基本写法：分析 Extra 额外信息**
`EXPLAIN SELECT ... -- 关注 Extra 列`

```sql
-- Using index: 覆盖索引，无需回表（最优）
EXPLAIN SELECT id, name FROM users WHERE name = '张三';
-- Using filesort: 额外排序（需优化）
EXPLAIN SELECT * FROM users ORDER BY age;
-- Using temporary: 使用临时表（需优化）
EXPLAIN SELECT DISTINCT dept FROM users;
```

---

## SHOW PROFILE

**基本写法：开启 profile**
`SET profiling = 1;`

```sql
-- 启用查询性能分析
SET profiling = 1;
```

**基本写法：查看 profile 列表**
`SHOW PROFILES;`

```sql
-- 查看最近执行的查询及 Query_ID
SHOW PROFILES;
```

**基本写法：查看单条查询详情**
`SHOW PROFILE [CPU|BLOCK IO|ALL] FOR QUERY <Query_ID>;`

```sql
-- 查看指定查询各阶段耗时
SHOW PROFILE CPU FOR QUERY 1;
-- 查看所有资源使用
SHOW PROFILE ALL FOR QUERY 1;
```

---

## 慢查询日志

**基本写法：查看慢查询配置**
`SHOW VARIABLES LIKE 'slow_query_log%';`

```sql
-- 查看慢查询日志开关与路径
SHOW VARIABLES LIKE 'slow_query_log%';
```

**基本写法：开启慢查询日志**
`SET GLOBAL slow_query_log = ON;`

```sql
-- 临时开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过 1 秒记录
```

**基本写法：配置文件持久开启**
`slow_query_log = 1`

```ini
# my.cnf 持久配置
[mysqld]
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = 1
```

**基本写法：mysqldumpslow 分析慢日志**
`mysqldumpslow -s <排序字段> -t <行数> <慢日志文件>`

```bash
# 按总耗时排序取前 10 条
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
# 按次数排序
mysqldumpslow -s c -t 10 /var/log/mysql/slow.log
```

---

## Performance Schema

**基本写法：查看性能 schema 开关**
`SELECT * FROM performance_schema.setup_instruments;`

```sql
-- 查看可用的性能采集器
SELECT name, enabled, timed
FROM performance_schema.setup_instruments
WHERE name LIKE 'statement/%';
```

**基本写法：启用采集器**
`UPDATE performance_schema.setup_instruments SET enabled = 'YES', timed = 'YES' WHERE name LIKE '<模式>';`

```sql
-- 启用语句采集
UPDATE performance_schema.setup_instruments
SET enabled = 'YES', timed = 'YES'
WHERE name LIKE 'statement/%';
```

**基本写法：查看 SQL 执行统计**
`SELECT * FROM performance_schema.events_statements_summary_by_digest ORDER BY COUNT_STAR DESC LIMIT 10;`

```sql
-- 查看执行最频繁的 SQL 模式
SELECT digest_text, count_star, avg_timer_wait/1000000000 AS avg_ms
FROM performance_schema.events_statements_summary_by_digest
ORDER BY count_star DESC LIMIT 10;
```

**基本写法：查看等待事件**
`SELECT * FROM performance_schema.events_waits_summary_global_by_event_name ORDER BY SUM_TIMER_WAIT DESC LIMIT 10;`

```sql
-- 查看最耗时的等待事件
SELECT event_name, count_star, sum_timer_wait/1000000000 AS sum_ms
FROM performance_schema.events_waits_summary_global_by_event_name
ORDER BY sum_timer_wait DESC LIMIT 10;
```

---

## 优化器追踪

**基本写法：开启 optimizer trace**
`SET optimizer_trace = 'enabled=on';`

```sql
-- 启用优化器追踪
SET optimizer_trace = 'enabled=on';
SET optimizer_trace_max_mem_size = 65536;
```

**基本写法：查看追踪结果**
`SELECT * FROM information_schema.OPTIMIZER_TRACE;`

```sql
-- 执行查询后查看优化器决策过程
SELECT id FROM users WHERE email = 'test@example.com';
SELECT trace FROM information_schema.OPTIMIZER_TRACE\G
```

---


<!-- ============ 文档分隔线：020-mysql/028-SystemVariableStatus.md ============ -->

# 系统变量与状态查询 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 系统变量查询

**基本写法：查看所有系统变量**
`SHOW VARIABLES [LIKE '<模式>'];`

```sql
-- 查看所有变量
SHOW VARIABLES;
-- 过滤查看 innodb 相关变量
SHOW VARIABLES LIKE 'innodb%';
```

**基本写法：查看单个变量**
`SHOW VARIABLES LIKE '<变量名>';`

```sql
-- 查看最大连接数
SHOW VARIABLES LIKE 'max_connections';
-- 查看默认存储引擎
SHOW VARIABLES LIKE 'default_storage_engine';
```

**基本写法：精确匹配变量**
`SELECT @@GLOBAL.<变量名>;` / `SELECT @@SESSION.<变量名>;`

```sql
-- 查看 GLOBAL 与 SESSION 作用域变量
SELECT @@GLOBAL.max_connections;
SELECT @@SESSION.autocommit;
-- 查看仅会话级变量
SELECT @@session.sql_mode;
```

**基本写法：information_schema 查询变量**
`SELECT * FROM performance_schema.global_variables WHERE variable_name LIKE '<模式>';`

```sql
-- 通过性能 schema 查询变量
SELECT variable_name, variable_value
FROM performance_schema.global_variables
WHERE variable_name LIKE 'innodb_buffer%';
```

---

## 系统变量设置

**基本写法：设置全局变量（运行时）**
`SET GLOBAL <变量名> = <值>;`

```sql
-- 动态调整最大连接数（重启失效）
SET GLOBAL max_connections = 500;
```

**基本写法：设置会话变量**
`SET SESSION <变量名> = <值>;`

```sql
-- 仅当前会话生效
SET SESSION sql_mode = 'STRICT_TRANS_TABLES';
SET autocommit = 0;
```

**基本写法：SET PERSIST 持久化（8.0+）**
`SET PERSIST <变量名> = <值>;`

```sql
-- 持久化到 mysqld-auto.cnf，重启仍生效
SET PERSIST max_connections = 500;
SET PERSIST_ONLY innodb_buffer_pool_size = 4294967296;  -- 仅重启生效
```

**基本写法：重置变量为默认值**
`SET PERSIST <变量名> = DEFAULT;`

```sql
-- 清除持久化配置恢复默认
SET PERSIST max_connections = DEFAULT;
```

---

## 状态查询

**基本写法：查看服务器状态**
`SHOW STATUS [LIKE '<模式>'];`

```sql
-- 查看所有状态变量
SHOW STATUS;
-- 查看连接相关状态
SHOW STATUS LIKE 'Threads%';
```

**基本写法：查看会话级状态**
`SHOW SESSION STATUS LIKE '<模式>';`

```sql
-- 仅查看当前会话状态
SHOW SESSION STATUS LIKE 'Bytes%';
```

**基本写法：查看全局状态**
`SHOW GLOBAL STATUS LIKE '<模式>';`

```sql
-- 查看全局累计状态
SHOW GLOBAL STATUS LIKE 'Uptime';
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool%';
```

**基本写法：性能 schema 查询状态**
`SELECT * FROM performance_schema.global_status WHERE variable_name LIKE '<模式>';`

```sql
-- 通过性能 schema 查询状态
SELECT variable_name, variable_value
FROM performance_schema.global_status
WHERE variable_name LIKE 'Threads_%';
```

---

## 常用监控查询

**基本写法：查看当前连接数**
`SHOW STATUS LIKE 'Threads_connected';`

```sql
-- 当前活跃连接数
SHOW STATUS LIKE 'Threads_connected';
-- 历史最大连接数
SHOW STATUS LIKE 'Max_used_connections';
```

**基本写法：查看缓冲池命中率**
`SHOW STATUS LIKE 'Innodb_buffer_pool_reads';`

```sql
-- 计算缓冲池命中率（reads 为磁盘读，read_requests 为总请求）
SHOW STATUS LIKE 'Innodb_buffer_pool_read_requests';
SHOW STATUS LIKE 'Innodb_buffer_pool_reads';
-- 命中率 = 1 - reads / read_requests
```

**基本写法：查看 QPS 与 TPS**
`SHOW STATUS LIKE 'Questions';`

```sql
-- Questions 为查询总数，Uptime 为运行秒数，QPS = Questions/Uptime
SHOW STATUS LIKE 'Questions';
SHOW STATUS LIKE 'Uptime';
-- Com_开头的为各命令执行次数
SHOW STATUS LIKE 'Com_select';
SHOW STATUS LIKE 'Com_insert';
```

---

## 字符集与时区

**基本写法：查看字符集变量**
`SHOW VARIABLES LIKE 'character_set%';`

```sql
-- 查看各环节字符集
SHOW VARIABLES LIKE 'character_set%';
-- 查看排序规则
SHOW VARIABLES LIKE 'collation%';
```

**基本写法：查看时区**
`SELECT @@global.time_zone, @@session.time_zone;`

```sql
-- 查看全局与会话时区
SELECT @@global.time_zone, @@session.time_zone;
-- 查看当前时间
SELECT NOW(), UTC_TIMESTAMP();
```

**基本写法：设置时区**
`SET GLOBAL time_zone = '<时区>';`

```sql
-- 设置全局时区
SET GLOBAL time_zone = '+08:00';
SET SESSION time_zone = '+08:00';
```

---

## 查看进程与锁

**基本写法：查看进程列表**
`SHOW PROCESSLIST;`

```sql
-- 查看当前所有连接与正在执行的 SQL
SHOW PROCESSLIST;
-- 完整查看（含完整 SQL 文本）
SHOW FULL PROCESSLIST;
```

**基本写法：查看 InnoDB 锁信息**
`SELECT * FROM performance_schema.data_locks;`

```sql
-- 8.0+ 通过 performance_schema 查看锁（替代旧版 information_schema.INNODB_LOCKS）
SELECT * FROM performance_schema.data_locks;
-- 查看锁等待
SELECT * FROM performance_schema.data_lock_waits;
```

**基本写法：查看 InnoDB 事务**
`SELECT * FROM information_schema.INNODB_TRX;`

```sql
-- 查看当前活跃事务
SELECT trx_id, trx_state, trx_started, trx_mysql_thread_id
FROM information_schema.INNODB_TRX;
```

---


<!-- ============ 文档分隔线：020-mysql/029-FullTextSearch.md ============ -->

# 全文搜索 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 全文索引创建

**基本写法：建表时创建全文索引**
`CREATE TABLE <表名> (... FULLTEXT KEY <索引名>(<列1>[, <列2>...])) [WITH PARSER <解析器>];`

```sql
-- 创建带中文全文索引的文章表（需 ngram 解析器支持中文）
CREATE TABLE articles (
  id BIGINT PRIMARY KEY,
  title VARCHAR(200),
  body TEXT,
  FULLTEXT KEY ft_title_body (title, body) WITH PARSER ngram
) ENGINE = InnoDB;
```

**基本写法：为已有表添加全文索引**
`CREATE FULLTEXT INDEX <索引名> ON <表名>(<列>[, <列>...]) [WITH PARSER <解析器>];`

```sql
-- 为 body 列添加全文索引
CREATE FULLTEXT INDEX ft_body ON articles(body) WITH PARSER ngram;
```

**基本写法：ALTER 添加全文索引**
`ALTER TABLE <表名> ADD FULLTEXT INDEX <索引名>(<列>[, <列>...]) [WITH PARSER <解析器>];`

```sql
-- 通过 ALTER 添加复合全文索引
ALTER TABLE articles
ADD FULLTEXT INDEX ft_title_body (title, body) WITH PARSER ngram;
```

---

## 全文搜索查询

**基本写法：MATCH ... AGAINST 自然语言搜索**
`SELECT ... WHERE MATCH(<列>) AGAINST('<关键词>')`

```sql
-- 自然语言模式搜索（默认）
SELECT id, title, MATCH(title, body) AGAINST('数据库') AS relevance
FROM articles
WHERE MATCH(title, body) AGAINST('数据库')
ORDER BY relevance DESC;
```

**基本写法：布尔模式搜索**
`SELECT ... WHERE MATCH(<列>) AGAINST('<表达式>' IN BOOLEAN MODE)`

```sql
-- 布尔模式：+必须包含，-排除，*通配
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('+MySQL -Oracle' IN BOOLEAN MODE);
-- 包含任意一个词
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('MySQL PostgreSQL' IN BOOLEAN MODE);
-- 前缀匹配
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('data*' IN BOOLEAN MODE);
```

**基本写法：查询扩展模式**
`SELECT ... WHERE MATCH(<列>) AGAINST('<关键词>' WITH QUERY EXPANSION)`

```sql
-- 查询扩展：自动扩展相关词进行二次搜索（召回率高但精度低）
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('database' WITH QUERY EXPANSION);
```

---

## ngram 中文解析器

**基本写法：ngram 分词配置**
`SET GLOBAL ngram_token_size = <数值>;`

```sql
-- 查看 ngram 分词长度（默认 2，需在配置文件设置）
SHOW VARIABLES LIKE 'ngram_token_size';
```

**基本写法：配置文件设置 ngram**
`ngram_token_size = 2`

```ini
# my.cnf 中设置 ngram 分词长度（重启生效）
[mysqld]
ngram_token_size = 2
```

**基本写法：ngram 布尔搜索中文**
`SELECT ... WHERE MATCH(<列>) AGAINST('<中文词>' IN BOOLEAN MODE)`

```sql
-- ngram 模式下中文搜索（"数据库"会被切分为"数据""据库"）
SELECT id, title FROM articles
WHERE MATCH(title, body) AGAINST('+数据 +据库' IN BOOLEAN MODE);
```

---

## 索引维护

**基本写法：查看全文索引**
`SHOW INDEX FROM <表名> WHERE Index_type = 'FULLTEXT';`

```sql
-- 查看表的全文索引
SHOW INDEX FROM articles WHERE Index_type = 'FULLTEXT';
```

**基本写法：删除全文索引**
`ALTER TABLE <表名> DROP INDEX <索引名>;`

```sql
-- 删除全文索引
ALTER TABLE articles DROP INDEX ft_title_body;
-- 或使用 DROP INDEX
DROP INDEX ft_body ON articles;
```

**基本写法：重建全文索引**
`ALTER TABLE <表名> DROP INDEX <索引名>, ADD FULLTEXT INDEX <索引名>(<列>) WITH PARSER <解析器>;`

```sql
-- 重建全文索引（数据变更后统计信息更新）
ALTER TABLE articles
DROP INDEX ft_body,
ADD FULLTEXT INDEX ft_body (body) WITH PARSER ngram;
```

---

## 布尔模式运算符

**基本写法：运算符速查**
`AGAINST('<+包含> <-排除> <可选> "<短语>" <前缀>*' IN BOOLEAN MODE)`

```sql
-- + 包含该词
MATCH(body) AGAINST('+MySQL' IN BOOLEAN MODE)
-- - 排除该词
MATCH(body) AGAINST('-Oracle' IN BOOLEAN MODE)
-- 无符号：该词可选，相关性更高
MATCH(body) AGAINST('MySQL 性能' IN BOOLEAN MODE)
-- "短语"：完整匹配短语
MATCH(body) AGAINST('"full text search"' IN BOOLEAN MODE)
-- * 前缀通配（必须 3 字符以上）
MATCH(body) AGAINST('opti*' IN BOOLEAN MODE)
-- () 分组
MATCH(body) AGAINST('+MySQL +(优化 调优)' IN BOOLEAN MODE)
-- ~ 词之间距离（接近度）
MATCH(body) AGAINST('MySQL~性能' IN BOOLEAN MODE)
```

**基本写法：相关性排序**
`SELECT MATCH(<列>) AGAINST('<词>') AS <相关度> FROM <表> ORDER BY <相关度> DESC`

```sql
-- 返回相关性分数并排序
SELECT
  id,
  title,
  MATCH(title, body) AGAINST('数据库 优化') AS score
FROM articles
WHERE MATCH(title, body) AGAINST('数据库 优化' IN BOOLEAN MODE)
ORDER BY score DESC
LIMIT 20;
```

---


<!-- ============ 文档分隔线：020-mysql/030-GTID.md ============ -->

# GTID 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## GTID 概念与格式

**基本写法：标准 GTID 格式**
`<server_uuid>:<事务序号>`

```sql
-- 标准 GTID 格式示例
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
-- 表示该 UUID 的事务 1 到 5

-- 8.4 Tagged GTID 格式（带标签）
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5:delete_logs
```

**基本写法：查看服务器 UUID**
`SHOW VARIABLES LIKE 'server_uuid';`

```sql
-- 查看当前服务器 UUID
SHOW VARIABLES LIKE 'server_uuid';
```

---

## GTID 开启与配置

**基本写法：查看 GTID 状态**
`SHOW VARIABLES LIKE 'gtid_mode';`

```sql
-- 查看 GTID 是否启用
SHOW VARIABLES LIKE 'gtid_mode';
SHOW VARIABLES LIKE 'enforce_gtid_consistency';
```

**基本写法：在线开启 GTID（分步）**
`SET GLOBAL enforce_gtid_consistency = WARN;`

```sql
-- 第一步：开启一致性警告，观察业务无警告后继续
SET GLOBAL enforce_gtid_consistency = WARN;
-- 第二步：开启一致性强制
SET GLOBAL enforce_gtid_consistency = ON;
-- 第三步：GTID 模式 OFF_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = OFF_PERMISSIVE;
-- 第四步：ON_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = ON_PERMISSIVE;
-- 等待所有匿名事务消费完毕
SHOW STATUS LIKE 'Ongoing_anonymous_transaction_count';
-- 第五步：正式开启
SET GLOBAL gtid_mode = ON;
```

**基本写法：配置文件持久开启**
`gtid_mode = ON`

```ini
# my.cnf 持久配置
[mysqld]
gtid_mode = ON
enforce_gtid_consistency = ON
log_slave_updates = ON        # 8.0.10+ 默认 ON，副本需记录更新到 binlog
log_bin = mysql-bin
```

---

## GTID 查询

**基本写法：查看已执行 GTID**
`SELECT @@GLOBAL.gtid_executed;`

```sql
-- 查看当前服务器已执行的 GTID 集合
SELECT @@GLOBAL.gtid_executed;
-- 示例输出: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100
```

**基本写法：查看已清除 GTID**
`SELECT @@GLOBAL.gtid_purged;`

```sql
-- 查看已被清除（不可用）的 GTID 集合
SELECT @@GLOBAL.gtid_purged;
```

**基本写法：查看 GTID 执行状态**
`SHOW MASTER STATUS;`

```sql
-- 查看当前二进制日志位置与已执行 GTID（8.4 用 SHOW BINARY LOG STATUS）
SHOW BINARY LOG STATUS\G
-- 输出包含 Executed_Gtid_Set 字段
```

**基本写法：performance_schema 查询 GTID**
`SELECT * FROM performance_schema.replication_connection_status;`

```sql
-- 查看复制连接接收到的 GTID
SELECT thread_id, service_state, received_transaction_set
FROM performance_schema.replication_connection_status;
```

---

## GTID 复制配置

**基本写法：基于 GTID 建立复制**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_AUTO_POSITION = 1;`

```sql
-- GTID 自动定位复制（无需指定日志文件和位置）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_AUTO_POSITION = 1,
  GET_SOURCE_PUBLIC_KEY = 1;
START REPLICA;
```

**基本写法：跳过指定 GTID 事务**
`SET GTID_NEXT = '<GTID>';`

```sql
-- 跳过单个 GTID 事务（解决复制错误）
STOP REPLICA;
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN; COMMIT;
SET GTID_NEXT = AUTOMATIC;
START REPLICA;
```

**基本写法：设置已清除 GTID（空库初始化）**
`SET GLOBAL gtid_purged = '<GTID集合>';`

```sql
-- 从备份恢复空库时设置已清除的 GTID
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100';
```

---

## 8.4 Tagged GTID

**基本写法：为事务打标签**
`SET TRANSACTION GTID_TAG = '<标签名>';`

```sql
-- MySQL 8.4 新特性：为事务分配标签（最多 33 字符）
-- 需 TRANSACTION_GTID_TAG 权限
SET TRANSACTION GTID_TAG = 'delete_logs';
DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：会话级设置标签**
`SET SESSION gtid_next_tag = '<标签名>';`

```sql
-- 当前会话所有事务都打上标签
SET SESSION gtid_next_tag = 'batch_import';
INSERT INTO sales VALUES (...);
```

**基本写法：跳过指定标签的事务**
`SET GLOBAL gtid_purged = '<UUID>:<区间>:<标签>';`

```sql
-- 副本端跳过带标签的事务（8.4 新增三参数 gtid_purged）
-- 格式: SET GLOBAL gtid_purged=<group_name>, <gtid_set>, <tag>
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100:delete_logs';
```

**基本写法：查看带标签的 GTID**
`SELECT * FROM performance_schema.replication_applier_status_by_worker;`

```sql
-- 查看副本应用事务时是否包含标签信息
SELECT worker_id, last_applied_transaction, last_applied_transaction_original_seqno
FROM performance_schema.replication_applier_status_by_worker;
```

---

## GTID 复制错误处理

**基本写法：查看复制错误**
`SHOW REPLICA STATUS\G`

```sql
-- 查看复制错误信息
SHOW REPLICA STATUS\G
-- 关注 Last_Error 与 Last_SQL_Error 字段
```

**基本写法：基于 GTID 自动跳过错误**
`SET GLOBAL slave_skip_errors = '<错误码>';`

```sql
-- 不推荐：跳过指定错误码（破坏一致性）
-- 推荐：使用 GTID_NEXT 手动跳过或 sql_slave_skip_counter（仅非 GTID）
```

**基本写法：重置 GTID 执行状态**
`RESET MASTER;`

```sql
-- 清空所有 binlog 并重置 gtid_executed（危险！仅初始化时使用）
RESET MASTER;
```

---

