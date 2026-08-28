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
