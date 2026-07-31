# SQL 锁机制 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 行级锁

**基本写法：共享锁（S 锁）**
`SELECT * FROM <表> WHERE <条件> LOCK IN SHARE MODE;`
```sql
-- MySQL 共享锁：允许其他事务读，不允许写
BEGIN;
SELECT * FROM accounts WHERE id = 1 LOCK IN SHARE MODE;
-- 其他事务可以读，但不能修改此行
COMMIT;
```

---

**基本写法：PostgreSQL 共享锁**
`SELECT * FROM <表> WHERE <条件> FOR SHARE;`
```sql
-- PostgreSQL 共享锁
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR SHARE;
-- 其他事务可加 SHARE 锁，不能加 EXCLUSIVE 锁
COMMIT;
```

---

**基本写法：排他锁（X 锁）**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE;`
```sql
-- 排他锁：阻止其他事务读写
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- 其他事务无法读取或修改此行
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

**基本写法：NOWAIT 不等待锁**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE NOWAIT;`
```sql
-- 获取不到锁立即报错，不等待
BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- 如果行被锁定，立即报错：ERROR: could not obtain lock
COMMIT;
```

---

**基本写法：SKIP LOCKED 跳过锁定行**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE SKIP LOCKED;`
```sql
-- 跳过被锁定的行（适合任务队列）
BEGIN;
SELECT id FROM task_queue WHERE status = 'pending'
FOR UPDATE SKIP LOCKED LIMIT 10;
-- 只返回未被锁定的行
COMMIT;
```

---

## 表级锁

**基本写法：MySQL 表锁**
`LOCK TABLES <表> [READ|WRITE];`
```sql
-- MySQL 表锁
LOCK TABLES employees WRITE;
-- 只有当前会话可读写
UNLOCK TABLES;

LOCK TABLES employees READ;
-- 所有会话只能读
UNLOCK TABLES;
```

---

**基本写法：PostgreSQL 表锁**
`LOCK TABLE <表> IN <模式> MODE;`
```sql
-- PostgreSQL 表级锁
LOCK TABLE employees IN SHARE MODE;
-- 允许并发读，阻止写

LOCK TABLE employees IN EXCLUSIVE MODE;
-- 只允许当前事务读写

LOCK TABLE employees IN ACCESS EXCLUSIVE MODE;
-- 最严格：阻止一切并发访问
```

---

**基本写法：锁模式层级**
`-- PostgreSQL 锁模式从弱到强`
```sql
-- ACCESS SHARE        SELECT 自动加（最弱）
-- ROW SHARE          SELECT FOR UPDATE/SHARE 自动加
-- ROW EXCLUSIVE      INSERT/UPDATE/DELETE 自动加
-- SHARE UPDATE       （预留）
-- SHARE              LOCK TABLE ... IN SHARE MODE
-- SHARE ROW EXCLUSIVE
-- EXCLUSIVE
-- ACCESS EXCLUSIVE   DROP/TRUNCATE/ALTER 自动加（最强）
```

---

## 间隙锁（MySQL InnoDB）

**基本写法：间隙锁防止幻读**
`SELECT * FROM <表> WHERE <范围条件> FOR UPDATE;`
```sql
-- REPEATABLE READ 下，范围查询加间隙锁
BEGIN;
SELECT * FROM accounts WHERE id BETWEEN 10 AND 20 FOR UPDATE;
-- 锁定 id=10 到 id=20 之间的间隙
-- 其他事务无法在此范围内插入数据
COMMIT;
```

---

**基本写法：临键锁（Next-Key Lock）**
`-- InnoDB 默认使用临键锁（行锁+间隙锁）`
```sql
-- 临键锁锁定的范围
-- 如果索引有 10, 15, 20
-- SELECT WHERE id > 10 AND id < 20 FOR UPDATE
-- 锁定：(10, 15], (15, 20)
-- 即锁住了 10 到 20 之间所有可能的位置
```

---

**基本写法：查看锁信息**
`SELECT * FROM information_schema.innodb_locks;`
```sql
-- MySQL 查看当前锁
SELECT * FROM performance_schema.data_locks;
SELECT * FROM performance_schema.data_lock_waits;

-- 查看锁等待
SELECT * FROM sys.innodb_lock_waits;
```

---

## 死锁

**基本写法：死锁产生场景**
`-- 两个事务互相等待对方释放锁`
```sql
-- 事务A
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;  -- 锁 id=1
UPDATE accounts SET balance = balance + 100 WHERE id = 2;  -- 等待 id=2 的锁

-- 事务B（同时执行）
BEGIN;
UPDATE accounts SET balance = balance - 200 WHERE id = 2;  -- 锁 id=2
UPDATE accounts SET balance = balance + 200 WHERE id = 1;  -- 等待 id=1 的锁
-- 死锁！
```

---

**基本写法：避免死锁**
`-- 按固定顺序访问资源`
```sql
-- 始终按 id 升序加锁，避免交叉等待
-- 事务A 和 事务B 都先锁 id=1 再锁 id=2
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

---

**基本写法：设置锁等待超时**
`SET innodb_lock_wait_timeout = <秒>;`
```sql
-- 设置锁等待超时（默认 50 秒）
SET innodb_lock_wait_timeout = 10;
-- 超时后报错并回滚当前语句
```

---

**基本写法：查看死锁日志**
`SHOW ENGINE INNODB STATUS\G`
```sql
-- 查看最近死锁信息
SHOW ENGINE INNODB STATUS\G
-- 查看 LATEST DETECTED DEADLOCK 部分
```

---

## 悲观锁

**基本写法：悲观锁模式**
`SELECT ... FOR UPDATE`
```sql
-- 先锁定再修改，确保安全
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
-- 应用层判断余额是否足够
-- 如果 balance >= 100
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

---

**基本写法：悲观锁实现库存扣减**
`SELECT stock FROM products WHERE id = 1 FOR UPDATE;`
```sql
-- 库存扣减使用悲观锁
BEGIN;
SELECT stock FROM products WHERE id = 1 FOR UPDATE;
-- 检查 stock >= order_qty
-- 如果足够
UPDATE products SET stock = stock - 1 WHERE id = 1;
INSERT INTO orders (product_id, qty) VALUES (1, 1);
COMMIT;
```

---

## 乐观锁

**基本写法：版本号实现乐观锁**
`UPDATE <表> SET <列>=<新值>, version=version+1 WHERE id=<ID> AND version=<版本>`
```sql
-- 乐观锁：先读后写，写入时检查版本
-- 1. 读取数据
SELECT id, balance, version FROM accounts WHERE id = 1;
-- 结果: id=1, balance=1000, version=3

-- 2. 写入时检查版本
UPDATE accounts
SET balance = 900, version = version + 1
WHERE id = 1 AND version = 3;
-- 如果受影响行数 = 0，说明已被其他人修改，需重试
```

---

**基本写法：时间戳实现乐观锁**
`UPDATE <表> SET <列>=<值>, updated_at=NOW() WHERE id=<ID> AND updated_at=<时间>`
```sql
-- 使用时间戳替代版本号
SELECT id, balance, updated_at FROM accounts WHERE id = 1;
-- 假设 updated_at = '2026-07-31 10:00:00'

UPDATE accounts
SET balance = 900, updated_at = NOW()
WHERE id = 1 AND updated_at = '2026-07-31 10:00:00';
```

---

**基本写法：CAS 模式**
`UPDATE <表> SET <列>=<新值> WHERE id=<ID> AND <列>=<旧值>`
```sql
-- Compare And Swap 模式
-- 扣减余额：条件是当前余额足够
UPDATE accounts
SET balance = balance - 100
WHERE id = 1 AND balance >= 100;
-- 如果受影响行数 = 0，说明余额不足或被修改
```

---

## 锁监控

**基本写法：MySQL 锁等待查询**
`SELECT * FROM performance_schema.data_lock_waits;`
```sql
-- 查看锁等待情况
SELECT
  r.trx_id AS waiting_trx,
  r.trx_mysql_thread_id AS waiting_thread,
  b.trx_id AS blocking_trx,
  b.trx_mysql_thread_id AS blocking_thread
FROM information_schema.innodb_trx r
JOIN information_schema.innodb_trx b
  ON r.trx_requested_lock_id = b.trx_lock_id;
```

---

**基本写法：PostgreSQL 锁查询**
`SELECT * FROM pg_locks;`
```sql
-- 查看当前所有锁
SELECT pid, locktype, relation::regclass, mode, granted
FROM pg_locks;

-- 查看阻塞的会话
SELECT
  blocked.pid AS blocked_pid,
  blocking.pid AS blocking_pid,
  query
FROM pg_stat_activity blocked
JOIN pg_locks bl ON bl.pid = blocked.pid AND NOT bl.granted
JOIN pg_locks ul ON ul.locktype = bl.locktype
  AND ul.relation = bl.relation AND ul.granted
JOIN pg_stat_activity blocking ON blocking.pid = ul.pid;
```

---

**基本写法：终止阻塞会话**
`SELECT pg_terminate_backend(<pid>);`
```sql
-- PostgreSQL 终止阻塞进程
SELECT pg_terminate_backend(12345);

-- MySQL 杀死会话
KILL 12345;
```
