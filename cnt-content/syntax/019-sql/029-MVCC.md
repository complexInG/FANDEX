# SQL 多版本并发控制（MVCC） 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## MVCC 基本概念

**基本写法：MVCC 原理**
`-- 每行保存多个版本，读操作不加锁`
```sql
-- MVCC（Multi-Version Concurrency Control）
-- 每行数据隐藏两个字段：
--   trx_id   最后修改该行的事务 ID
--   roll_ptr 指向 undo log 中该行的上一个版本
-- 读操作根据 Read View 选择合适的版本，不加锁
```

---

**基本写法：查看隐藏字段**
`-- InnoDB 每行隐藏字段`
```sql
-- MySQL InnoDB 每行记录的隐藏列
-- DB_TRX_ID    事务 ID（6 字节）
-- DB_ROLL_PTR  回滚指针（7 字节）
-- DB_ROW_ID     行 ID（6 字节，无主键时自动生成）
```

---

## Read View（读视图）

**基本写法：Read View 创建时机**
`-- 在 READ COMMITTED 下每次 SELECT 创建新 Read View`
```sql
-- READ COMMITTED 隔离级别
-- 每次 SELECT 都创建新的 Read View
-- 因此能看到其他事务已提交的最新数据

-- REPEATABLE READ 隔离级别
-- 事务第一次 SELECT 时创建 Read View
-- 整个事务使用同一个 Read View
-- 因此看到的是事务开始时的快照
```

---

**基本写法：可见性判断规则**
`-- 行版本对当前事务可见的条件`
```sql
-- Read View 包含：
--   m_ids       活跃事务 ID 列表
--   min_trx_id  最小活跃事务 ID
--   max_trx_id  下一个事务 ID
--   creator_trx_id 当前事务 ID

-- 判断规则：
-- 1. trx_id == creator_trx_id → 可见（自己修改的）
-- 2. trx_id < min_trx_id      → 可见（已提交）
-- 3. trx_id >= max_trx_id     → 不可见（未来事务）
-- 4. min_trx_id <= trx_id < max_trx_id 且不在 m_ids → 可见
--    在 m_ids 中 → 不可见，沿 roll_ptr 找历史版本
```

---

## 快照读

**基本写法：普通 SELECT 是快照读**
`SELECT * FROM <表> WHERE <条件>`
```sql
-- 快照读：读取 MVCC 版本链中的可见版本，不加锁
-- READ COMMITTED 下读到最新已提交版本
-- REPEATABLE READ 下读到事务开始时的快照

SELECT * FROM accounts WHERE id = 1;
-- 不加锁，读的是快照
```

---

**基本写法：不同隔离级别的快照读**
`-- 同一查询在不同隔离级别下结果不同`
```sql
-- 会话A（REPEATABLE READ）
BEGIN;
SELECT balance FROM accounts WHERE id = 1;  -- 1000

-- 会话B 修改并提交
-- UPDATE accounts SET balance = 500 WHERE id = 1; COMMIT;

-- 会话A 再次查询（快照读）
SELECT balance FROM accounts WHERE id = 1;  -- 仍为 1000（使用旧快照）
COMMIT;
```

---

## 当前读

**基本写法：加锁查询是当前读**
`SELECT * FROM <表> WHERE <条件> FOR UPDATE`
```sql
-- 当前读：读取最新版本并加锁
-- FOR UPDATE / LOCK IN SHARE MODE / UPDATE / DELETE 都是当前读

BEGIN;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
-- 读取最新版本（即使其他事务已提交），并加排他锁
COMMIT;
```

---

**基本写法：UPDATE 是当前读**
`UPDATE <表> SET <列>=<值> WHERE <条件>`
```sql
-- UPDATE/DELETE 操作需要读取最新版本（当前读）
BEGIN;
-- 快照读（读旧版本）
SELECT balance FROM accounts WHERE id = 1;  -- 1000

-- 当前读（读最新版本）
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
-- 此处读到的是最新余额（可能是 2000），更新后为 1900
COMMIT;
```

---

## undo log 版本链

**基本写法：版本链结构**
`-- 每次修改生成 undo log，形成版本链`
```sql
-- 版本链示例
-- 当前行:  trx_id=200, balance=300
--          ↓ roll_ptr
-- undo1:  trx_id=150, balance=500
--          ↓ roll_ptr
-- undo2:  trx_id=100, balance=1000

-- 事务 trx_id=120 的 Read View：
-- 200 不可见（活跃），150 不可见（活跃），100 可见 → 读到 balance=1000
```

---

**基本写法：purge 清理 undo log**
`-- 没有活跃事务引用的旧版本会被清理`
```sql
-- MySQL InnoDB 后台 purge 线程清理 undo log
-- 当 Read View 不再需要某个旧版本时，purge 线程删除它

-- 查看 purge 状态
SHOW ENGINE INNODB STATUS\G
-- 查看 purge 相关信息
```

---

## MVCC 与隔离级别

**基本写法：READ COMMITTED 下的 MVCC**
`-- 每次查询创建新 Read View`
```sql
-- READ COMMITTED 隔离级别
BEGIN;
SELECT * FROM accounts WHERE id = 1;  -- Read View 1，读到余额 1000

-- 其他事务提交修改

SELECT * FROM accounts WHERE id = 1;  -- Read View 2，读到新余额 500
-- 因为每次 SELECT 都创建新的 Read View
COMMIT;
```

---

**基本写法：REPEATABLE READ 下的 MVCC**
`-- 事务内使用同一个 Read View`
```sql
-- REPEATABLE READ 隔离级别
BEGIN;
SELECT * FROM accounts WHERE id = 1;  -- Read View 创建，读到余额 1000

-- 其他事务提交修改

SELECT * FROM accounts WHERE id = 1;  -- 仍为 1000（使用同一 Read View）
COMMIT;
```

---

## MVCC 相关参数

**基本写法：查看 undo 相关参数**
`SHOW VARIABLES LIKE 'innodb_undo%';`
```sql
-- 查看 undo 表空间配置
SHOW VARIABLES LIKE 'innodb_undo%';
-- innodb_undo_directory: undo log 目录
-- innodb_undo_log_truncate: 是否自动截断
-- innodb_undo_tablespaces: undo 表空间数量
```

---

**基本写法：查看隔离级别**
`SELECT @@transaction_isolation;`
```sql
-- 当前隔离级别决定了 MVCC 的行为
SELECT @@transaction_isolation;
-- REPEATABLE-READ（MySQL 默认，MVCC 效果最佳）
```

---

## MVCC 优势

**基本写法：读不加锁**
`-- 读操作不阻塞写，写不阻塞读`
```sql
-- 传统锁机制：
--   读加共享锁 → 阻塞写
--   写加排他锁 → 阻塞读

-- MVCC：
--   快照读不加锁 → 不阻塞写
--   写加排他锁 → 不阻塞快照读
--   大幅提升读多写少场景的并发性能
```

---

## MVCC 局限性

**基本写法：长事务导致 undo 膨胀**
`-- 长事务持有旧 Read View，旧版本无法清理`
```sql
-- 长事务问题
BEGIN;
SELECT * FROM accounts;  -- 创建 Read View

-- ... 长时间不提交
-- 其他事务大量更新
-- undo log 持续增长，无法 purge
-- 导致 ibdata 或 undo 表空间膨胀

COMMIT;  -- 提交后 purge 才能清理旧版本
```

---

**基本写法：更新频繁的表性能下降**
`-- 版本链过长时，查找可见版本需要遍历`
```sql
-- 高频更新场景下，版本链可能很长
-- 读操作需要遍历版本链找到可见版本
-- 导致读性能下降

-- 建议：
-- 1. 避免长事务
-- 2. 高频更新表考虑降低隔离级别
-- 3. 定期 COMMIT 释放 Read View
```

---

## PostgreSQL MVCC

**基本写法：PostgreSQL MVCC 实现**
`-- 每行存储 xmin（创建事务）和 xmax（删除事务）`
```sql
-- PostgreSQL MVCC 使用 xmin/xmax 标记
-- xmin   插入/更新该行的事务 ID
-- xmax   删除/更新该行的事务 ID（0 表示未删除）

-- 查看行的事务信息（需要超级用户）
SELECT xmin, xmax, * FROM accounts WHERE id = 1;
```

---

**基本写法：PostgreSQL 表膨胀**
`-- 更新产生死元组，需要 VACUUM 清理`
```sql
-- PostgreSQL 更新 = 删除旧行 + 插入新行
-- 旧行标记为 dead tuple

-- 手动清理
VACUUM accounts;

-- 分析并清理
VACUUM ANALYZE accounts;

-- 完全清理（锁表）
VACUUM FULL accounts;

-- 自动清理配置
SHOW autovacuum;
```
