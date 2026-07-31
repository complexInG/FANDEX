# SQL 事务隔离级别 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 四种隔离级别

**基本写法：查看当前隔离级别**
`SELECT @@transaction_isolation;`
```sql
-- MySQL 查看隔离级别
SELECT @@transaction_isolation;
-- 或
SHOW VARIABLES LIKE 'transaction_isolation';
```

---

**基本写法：设置全局隔离级别**
`SET GLOBAL transaction_isolation = '<级别>';`
```sql
-- MySQL 设置全局隔离级别
SET GLOBAL transaction_isolation = 'READ-COMMITTED';
-- 可选值：
-- 'READ-UNCOMMITTED'
-- 'READ-COMMITTED'
-- 'REPEATABLE-READ'（MySQL 默认）
-- 'SERIALIZABLE'
```

---

**基本写法：设置会话隔离级别**
`SET SESSION transaction_isolation = '<级别>';`
```sql
-- 仅影响当前会话
SET SESSION transaction_isolation = 'READ-COMMITTED';
```

---

**基本写法：设置单事务隔离级别**
`SET TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- 仅影响下一个事务
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN;
SELECT * FROM employees;
COMMIT;
```

---

**基本写法：PostgreSQL 设置隔离级别**
`SET TRANSACTION ISOLATION LEVEL <级别>;`
```sql
-- PostgreSQL 在事务内设置
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT * FROM employees;
COMMIT;

-- 或在 BEGIN 时指定
BEGIN ISOLATION LEVEL READ COMMITTED;
```

---

## READ UNCOMMITTED（读未提交）

**基本写法：允许脏读**
`SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;`
```sql
-- 最低隔离级别：可读取未提交的数据（脏读）
-- 事务A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 未提交

-- 事务B（READ UNCOMMITTED）
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 可以看到事务A未提交的修改（脏数据）
```

---

## READ COMMITTED（读已提交）

**基本写法：避免脏读**
`SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`
```sql
-- 只能读取已提交的数据
-- 事务A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 未提交

-- 事务B（READ COMMITTED - PostgreSQL 默认）
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 读到的是修改前的值（避免脏读）
```

---

**基本写法：不可重复读现象**
`-- 同一事务内两次读取可能不同`
```sql
-- 事务B 先读取
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 余额 1000

-- 事务A 修改并提交
-- UPDATE accounts SET balance = 500 WHERE id = 1; COMMIT;

-- 事务B 再次读取
SELECT balance FROM accounts WHERE id = 1;  -- 余额 500（不可重复读）
COMMIT;
```

---

## REPEATABLE READ（可重复读）

**基本写法：避免不可重复读**
`SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;`
```sql
-- MySQL 默认隔离级别
-- 同一事务内多次读取结果一致
-- 事务B
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 余额 1000

-- 事务A 修改并提交
-- UPDATE accounts SET balance = 500 WHERE id = 1; COMMIT;

-- 事务B 再次读取
SELECT balance FROM accounts WHERE id = 1;  -- 余额仍为 1000（可重复读）
COMMIT;
```

---

**基本写法：MySQL 的幻读避免**
`-- MySQL InnoDB 通过 MVCC + 间隙锁避免幻读`
```sql
-- MySQL 的 REPEATABLE READ 已基本解决幻读
-- 事务B
BEGIN;
SELECT COUNT(*) FROM orders;  -- 10 条

-- 事务A 插入新订单并提交
-- INSERT INTO orders VALUES (...); COMMIT;

-- 事务B 再次查询
SELECT COUNT(*) FROM orders;  -- 仍为 10 条（无幻读）
COMMIT;
```

---

## SERIALIZABLE（串行化）

**基本写法：最高隔离级别**
`SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`
```sql
-- 所有事务串行执行，完全隔离
-- 性能最差，并发最低
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT * FROM accounts WHERE id = 1;
-- 其他事务对此行的修改会被阻塞
COMMIT;
```

---

**基本写法：PostgreSQL SERIALIZABLE**
`-- PostgreSQL 的 SSI 实现真正可串行化`
```sql
-- PostgreSQL 串行化隔离级别使用 SSI（Serializable Snapshot Isolation）
BEGIN ISOLATION LEVEL SERIALIZABLE;
SELECT balance FROM accounts WHERE id = 1;
-- 如果检测到冲突，提交时报错
COMMIT;
-- 可能报错：could not serialize access due to read/write dependencies
```

---

## 隔离级别对比

**基本写法：各级别对比**
`-- 四种隔离级别的现象对比`
```sql
-- 隔离级别          脏读   不可重复读  幻读
-- READ UNCOMMITTED  可能    可能        可能
-- READ COMMITTED    避免    可能        可能
-- REPEATABLE READ   避免    避免        MySQL避免/标准可能
-- SERIALIZABLE      避免    避免        避免
```

---

**基本写法：PostgreSQL 默认隔离级别**
`-- PostgreSQL 默认 READ COMMITTED`
```sql
-- 查看 PostgreSQL 默认隔离级别
SHOW default_transaction_isolation;
-- 默认值：read committed

-- 修改默认隔离级别
ALTER DATABASE mydb SET default_transaction_isolation = 'repeatable read';
```

---

**基本写法：MySQL 默认隔离级别**
`-- MySQL InnoDB 默认 REPEATABLE READ`
```sql
-- 查看 MySQL 默认隔离级别
SELECT @@global.transaction_isolation;
-- 默认值：REPEATABLE-READ
```

---

## 并发问题演示

**基本写法：脏读演示**
`-- READ UNCOMMITTED 下出现脏读`
```sql
-- 会话1
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
BEGIN;
UPDATE accounts SET balance = 0 WHERE id = 1;
-- 不提交

-- 会话2
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT balance FROM accounts WHERE id = 1;
-- 读到 balance=0（脏读：读到未提交的数据）

-- 会话1 回滚
ROLLBACK;
-- 会话2 读到的是无效数据
```

---

**基本写法：不可重复读演示**
`-- READ COMMITTED 下出现不可重复读`
```sql
-- 会话1
BEGIN;
SELECT salary FROM employees WHERE id = 1;  -- 5000

-- 会话2 修改并提交
-- UPDATE employees SET salary = 6000 WHERE id = 1; COMMIT;

-- 会话1 再次查询
SELECT salary FROM employees WHERE id = 1;  -- 6000（不可重复读）
COMMIT;
```

---

**基本写法：幻读演示**
`-- 标准 REPEATABLE READ 下可能出现幻读`
```sql
-- 会话1
BEGIN;
SELECT COUNT(*) FROM employees WHERE dept = 'IT';  -- 5 行

-- 会话2 插入新行并提交
-- INSERT INTO employees VALUES (..., 'IT'); COMMIT;

-- 会话1 再次查询
SELECT COUNT(*) FROM employees WHERE dept = 'IT';  -- 6 行（幻读）
COMMIT;
```

---

**基本写法：加锁避免幻读**
`SELECT ... FOR UPDATE 加锁`
```sql
-- 使用锁避免幻读
BEGIN;
SELECT * FROM employees WHERE dept = 'IT' FOR UPDATE;
-- 此时其他事务无法在此范围插入数据
-- INSERT INTO employees VALUES (..., 'IT') 会被阻塞
COMMIT;
```

---

## 隔离级别选择建议

**基本写法：选择建议**
`-- 根据业务场景选择合适的隔离级别`
```sql
-- 场景与建议：
-- 高并发读、少写    READ COMMITTED
-- 需要一致性读      REPEATABLE READ（MySQL 默认）
-- 金融/关键业务     SERIALIZABLE 或 REPEATABLE READ + 行锁
-- 报表/统计分析     REPEATABLE READ 或 READ ONLY
```
