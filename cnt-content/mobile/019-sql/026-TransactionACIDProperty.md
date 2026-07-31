# SQL 事务 ACID 属性 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事务基本操作

**基本写法：开启事务**
`BEGIN [TRANSACTION] [ISOLATION LEVEL <级别>]`
```sql
-- 显式开启事务
BEGIN;
-- 或
START TRANSACTION;
-- 指定隔离级别
BEGIN ISOLATION LEVEL READ COMMITTED;
```

---

**基本写法：提交事务**
`COMMIT [TRANSACTION]`
```sql
-- 提交当前事务
COMMIT;
-- 所有修改永久保存
```

---

**基本写法：回滚事务**
`ROLLBACK [TRANSACTION] [TO <保存点>]`
```sql
-- 回滚整个事务
ROLLBACK;
-- 回滚到指定保存点
ROLLBACK TO SAVEPOINT sp1;
```

---

**基本写法：设置保存点**
`SAVEPOINT <保存点名>`
```sql
-- 在事务中创建保存点
BEGIN;
INSERT INTO orders (id, amount) VALUES (1, 100);
SAVEPOINT after_insert;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 如果出错回滚到插入之后
ROLLBACK TO SAVEPOINT after_insert;
COMMIT;
```

---

**基本写法：释放保存点**
`RELEASE SAVEPOINT <保存点名>`
```sql
-- 释放保存点（不可再回滚到该点）
RELEASE SAVEPOINT sp1;
```

---

**基本写法：自动提交模式**
`SET autocommit = <0|1>`
```sql
-- MySQL 关闭自动提交
SET autocommit = 0;
-- 每条 SQL 需手动 COMMIT 才生效

-- 开启自动提交（默认）
SET autocommit = 1;
```

---

## ACID 属性

**基本写法：A - 原子性（Atomicity）**
`-- 事务内所有操作要么全部成功，要么全部回滚`
```sql
-- 转账示例：扣款和加款必须同时成功或同时失败
BEGIN;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
-- 如果任一步失败，整个事务回滚
COMMIT;
-- 或出错时 ROLLBACK;
```

---

**基本写法：C - 一致性（Consistency）**
`-- 事务前后数据满足完整性约束`
```sql
-- 转账前后总金额不变
-- 转账前：A=1000, B=1000, 总计=2000
-- 转账后：A=500, B=1500, 总计=2000（一致）
-- 约束检查：balance >= 0
ALTER TABLE accounts ADD CONSTRAINT chk_balance CHECK (balance >= 0);
```

---

**基本写法：I - 隔离性（Isolation）**
`-- 并发事务之间互不干扰`
```sql
-- 设置事务隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
-- 隔离级别从低到高：
-- READ UNCOMMITTED  读未提交（脏读）
-- READ COMMITTED    读已提交（不可重复读）
-- REPEATABLE READ    可重复读（幻读）
-- SERIALIZABLE       串行化（最高隔离）
```

---

**基本写法：D - 持久性（Durability）**
`-- 事务提交后数据永久保存，即使系统崩溃`
```sql
-- COMMIT 后数据写入磁盘
-- MySQL 通过 redo log 保证持久性
-- innodb_flush_log_at_trx_commit = 1（默认）确保每次提交都刷盘
SET GLOBAL innodb_flush_log_at_trx_commit = 1;
```

---

## 事务嵌套

**基本写法：MySQL 不支持真正嵌套**
`-- 通过 SAVEPOINT 模拟嵌套`
```sql
-- MySQL 无嵌套事务，用保存点模拟
BEGIN;
  INSERT INTO t1 VALUES (1);
  SAVEPOINT sp1;
    INSERT INTO t2 VALUES (2);
    -- 模拟内层回滚
    ROLLBACK TO SAVEPOINT sp1;
  INSERT INTO t3 VALUES (3);
COMMIT;
-- t1 和 t3 提交，t2 被回滚
```

---

**基本写法：PostgreSQL 嵌套**
`-- PostgreSQL 也用保存点实现`
```sql
-- PostgreSQL 保存点实现嵌套效果
BEGIN;
  INSERT INTO users (name) VALUES ('Alice');
  SAVEPOINT sp_user;
    INSERT INTO profiles (user_id, bio) VALUES (1, 'Hello');
    -- 如果 profile 插入失败
    ROLLBACK TO sp_user;
    -- 用户仍然存在，可以继续
  INSERT INTO logs (action) VALUES ('user_created');
COMMIT;
```

---

## 隐式提交

**基本写法：DDL 语句隐式提交**
`-- DDL 语句（CREATE/ALTER/DROP/TRUNCATE）自动触发 COMMIT`
```sql
-- 以下语句会自动提交之前的事务
BEGIN;
INSERT INTO t1 VALUES (1);
-- 以下 DDL 会隐式提交
CREATE TABLE t2 (id INT);
-- 此处 INSERT 已经被提交，无法回滚
ROLLBACK;  -- 只能回滚 DDL 之后的操作
```

---

**基本写法：隐式提交的语句**
`-- 会触发隐式提交的语句`
```sql
-- 以下操作会隐式 COMMIT：
-- CREATE / ALTER / DROP TABLE
-- CREATE / DROP INDEX
-- CREATE / DROP DATABASE
-- TRUNCATE TABLE
-- GRANT / REVOKE
-- LOCK TABLES / UNLOCK TABLES
```

---

## 事务超时与锁等待

**基本写法：设置锁等待超时**
`SET innodb_lock_wait_timeout = <秒>`
```sql
-- MySQL 设置行锁等待超时（秒）
SET innodb_lock_wait_timeout = 10;
-- 10 秒内获取不到锁则报错回滚

-- PostgreSQL 设置语句超时
SET statement_timeout = 10000;  -- 毫秒
```

---

**基本写法：死锁检测**
`SET innodb_deadlock_detect = ON;`
```sql
-- MySQL 开启死锁检测（默认开启）
SET GLOBAL innodb_deadlock_detect = ON;
-- 发生死锁时自动回滚代价较小的事务

-- 查看最近一次死锁信息
SHOW ENGINE INNODB STATUS\G
-- 查看 LATEST DETECTED DEADLOCK 部分
```

---

## 分布式事务

**基本写法：XA 事务**
`XA START '<xid>'; ... XA END '<xid>'; XA PREPARE '<xid>'; XA COMMIT '<xid>'`
```sql
-- MySQL XA 分布式事务
XA START 'tx1';
INSERT INTO db1.orders VALUES (1, 100);
XA END 'tx1';
XA PREPARE 'tx1';
-- 所有参与者 PREPARE 成功后
XA COMMIT 'tx1';
-- 或放弃
-- XA ROLLBACK 'tx1';
```

---

**基本写法：查看 XA 事务**
`XA RECOVER;`
```sql
-- 查看所有未完成的 XA 事务
XA RECOVER;
```

---

## 事务最佳实践

**基本写法：事务尽量短小**
`-- 减少锁持有时间，避免长事务`
```sql
-- 不推荐：事务中包含耗时操作
BEGIN;
SELECT * FROM users WHERE id = 1;  -- 查询
-- ... 执行业务逻辑（耗时操作）
UPDATE users SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- 推荐：先准备好数据，事务中只做必要的写操作
SELECT * FROM users WHERE id = 1;  -- 事务外查询
-- ... 业务逻辑
BEGIN;
UPDATE users SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

**基本写法：设置只读事务**
`SET TRANSACTION READ ONLY;`
```sql
-- 声明只读事务，优化器可优化
BEGIN READ ONLY;
SELECT * FROM employees WHERE dept_id = 5;
COMMIT;
```
