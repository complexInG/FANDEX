# SQL 性能优化 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 索引优化

**基本写法：创建合适索引**
`CREATE INDEX <索引名> ON <表>(<列>)`
```sql
-- 为 WHERE 条件列创建索引
CREATE INDEX idx_user_id ON orders(user_id);
-- 为 JOIN 条件列创建索引
CREATE INDEX idx_dept_id ON employees(dept_id);
```

---

**基本写法：复合索引**
`CREATE INDEX <索引名> ON <表>(<列1>, <列2>)`
```sql
-- 多条件查询使用复合索引
CREATE INDEX idx_user_status_date ON orders(user_id, status, create_date);
-- 查询：WHERE user_id=1 AND status='paid'
-- 查询：WHERE user_id=1 AND status='paid' AND create_date > '2026-01-01'
-- 都能命中索引
```

---

**基本写法：覆盖索引**
`-- 索引包含查询所需的所有列`
```sql
-- 查询只需要索引列时，无需回表
CREATE INDEX idx_cover ON employees(dept_id, name, salary);

SELECT name, salary FROM employees WHERE dept_id = 5;
-- Extra: Using index（覆盖索引，性能最优）
```

---

**基本写法：前缀索引**
`CREATE INDEX <索引名> ON <表>(<列>(<前缀长度>))`
```sql
-- 长字符串列使用前缀索引节省空间
CREATE INDEX idx_email ON users(email(10));
-- 仅索引前 10 个字符
```

---

**基本写法：函数索引（MySQL 5.7+）**
`CREATE INDEX <索引名> ON <表>((<表达式>))`
```sql
-- 为函数表达式创建索引
CREATE INDEX idx_lower_email ON users((LOWER(email)));
-- 查询 WHERE LOWER(email) = 'test@example.com' 可用索引

-- PostgreSQL
CREATE INDEX idx_upper_name ON employees(UPPER(name));
```

---

**基本写法：删除无用索引**
`DROP INDEX <索引名> ON <表>`
```sql
-- 索引会降低写入性能，删除不使用的索引
DROP INDEX idx_unused ON users;
```

---

## 查询优化

**基本写法：只查询需要的列**
`SELECT <列1>, <列2> FROM <表>`
```sql
-- 避免 SELECT *
SELECT id, name, email FROM users WHERE active = 1;
```

---

**基本写法：LIMIT 分页**
`SELECT * FROM <表> LIMIT <数量> OFFSET <偏移>`
```sql
-- 深度分页优化：避免大 OFFSET
-- 反模式：OFFSET 1000000（扫描 100 万行）
-- SELECT * FROM orders ORDER BY id LIMIT 10 OFFSET 1000000;

-- 正确：使用游标分页
SELECT * FROM orders
WHERE id > 1000000
ORDER BY id
LIMIT 10;
```

---

**基本写法：JOIN 优化小表驱动大表**
`SELECT * FROM <小表> JOIN <大表> ON <条件>`
```sql
-- 小表驱动大表（小表在外层）
SELECT * FROM small_table s
JOIN large_table l ON l.small_id = s.id
WHERE s.status = 'active';
```

---

**基本写法：子查询优化为 JOIN**
`SELECT ... FROM <表1> JOIN <表2> ON <条件>`
```sql
-- IN 子查询改为 JOIN
-- 反模式
-- SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE vip=1);

-- 优化为 JOIN
SELECT o.* FROM orders o
JOIN users u ON o.user_id = u.id
WHERE u.vip = 1;
```

---

**基本写法：批量插入**
`INSERT INTO <表> (<列>) VALUES (<值1>), (<值2>), ...`
```sql
-- 批量插入比逐条快
INSERT INTO users (name, email) VALUES
  ('Alice', 'a@test.com'),
  ('Bob', 'b@test.com'),
  ('Charlie', 'c@test.com');
```

---

**基本写法：INSERT ... ON DUPLICATE KEY UPDATE**
`INSERT INTO <表> (<列>) VALUES (<值>) ON DUPLICATE KEY UPDATE <列>=<值>`
```sql
-- MySQL UPSERT 避免先查后插
INSERT INTO counters (id, count) VALUES (1, 1)
ON DUPLICATE KEY UPDATE count = count + 1;
```

---

**基本写法：PostgreSQL UPSERT**
`INSERT INTO <表> (<列>) VALUES (<值>) ON CONFLICT (<列>) DO UPDATE SET <列>=<值>`
```sql
-- PostgreSQL UPSERT
INSERT INTO counters (id, count) VALUES (1, 1)
ON CONFLICT (id) DO UPDATE SET count = counters.count + 1;
```

---

## 执行计划分析

**基本写法：检查 type 字段**
`EXPLAIN SELECT ...`
```sql
-- type 从好到差：
-- const > eq_ref > ref > range > index > ALL
-- ALL 表示全表扫描，必须优化
EXPLAIN SELECT * FROM users WHERE email = 'test@test.com';
-- 确保 type 为 ref 或更好
```

---

**基本写法：检查 Extra 字段**
`-- 关注 Using filesort 和 Using temporary`
```sql
-- Using filesort: 额外排序，考虑加索引
-- Using temporary: 使用临时表，需优化
-- Using index: 覆盖索引，性能好

EXPLAIN SELECT dept, COUNT(*) FROM employees GROUP BY dept;
-- 如果出现 Using temporary; Using filesort
-- 考虑为 dept 加索引
```

---

## 表结构优化

**基本写法：选择合适数据类型**
`-- 使用最小够用的类型`
```sql
-- 优先使用精确类型
-- TINYINT(1)  代替  INT      节省 3 字节
-- SMALLINT    代替  INT      节省 2 字节
-- VARCHAR(N)  代替  CHAR(N) 变长节省空间
-- DATETIME    代替  VARCHAR 存日期

CREATE TABLE users (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  status TINYINT DEFAULT 0,       -- 而非 INT
  name VARCHAR(50),                -- 而非 CHAR(255)
  email VARCHAR(100)
);
```

---

**基本写法：避免过度规范化**
`-- 高频关联的表可适当冗余`
```sql
-- 订单表冗余商品名称（减少 JOIN）
CREATE TABLE orders (
  id INT PRIMARY KEY,
  product_id INT,
  product_name VARCHAR(100),  -- 冗余字段
  qty INT,
  price DECIMAL(10,2)
);
-- 查询时无需 JOIN products 表
```

---

**基本写法：分区表**
`PARTITION BY <方式>(<列>)`
```sql
-- MySQL 按范围分区
CREATE TABLE logs (
  id BIGINT AUTO_INCREMENT,
  create_time DATETIME,
  level VARCHAR(10),
  message TEXT,
  PRIMARY KEY (id, create_time)
)
PARTITION BY RANGE (TO_DAYS(create_time)) (
  PARTITION p202601 VALUES LESS THAN (TO_DAYS('2026-02-01')),
  PARTITION p202602 VALUES LESS THAN (TO_DAYS('2026-03-01')),
  PARTITION pmax VALUES LESS THAN MAXVALUE
);
```

---

## 缓存优化

**基本写法：使用 SQL_CACHE**
`SELECT SQL_CACHE * FROM <表>`
```sql
-- MySQL 查询缓存（8.0 已移除，仅旧版本）
SELECT SQL_CACHE * FROM users WHERE id = 1;
```

---

**基本写法：应用层缓存**
`-- 高频查询结果缓存到 Redis`
```sql
-- 数据库层面：减少重复查询
-- 对于不变的配置数据，应用层缓存
-- SELECT * FROM config;  -- 每次启动加载一次，缓存到内存
```

---

## 配置优化

**基本写法：InnoDB 缓冲池**
`SET GLOBAL innodb_buffer_pool_size = <字节>`
```sql
-- 设置 InnoDB 缓冲池大小（建议物理内存的 70-80%）
SET GLOBAL innodb_buffer_pool_size = 4294967296;  -- 4GB
```

---

**基本写法：连接池配置**
`SET GLOBAL max_connections = <数量>`
```sql
-- MySQL 最大连接数
SET GLOBAL max_connections = 200;
-- 查看当前连接数
SHOW STATUS LIKE 'Threads_connected';
```

---

**基本写法：PostgreSQL 配置**
`-- 修改 postgresql.conf`
```ini
# postgresql.conf 关键参数
shared_buffers = 2GB          # 内存 25%
effective_cache_size = 6GB     # 内存 75%
work_mem = 16MB
maintenance_work_mem = 256MB
max_connections = 100
```

---

## 慢查询排查

**基本写法：开启慢查询日志**
`SET GLOBAL slow_query_log = ON;`
```sql
-- 开启慢查询日志
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 1;  -- 超过 1 秒
```

---

**基本写法：分析慢查询日志**
`-- 使用 mysqldumpslow 分析`
```bash
# 统计慢查询 Top 10
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# 按返回行数排序
mysqldumpslow -s r -t 10 /var/log/mysql/slow.log
```

---

**基本写法：实时查看正在执行的查询**
`SHOW PROCESSLIST;`
```sql
-- 查看当前正在执行的查询
SHOW FULL PROCESSLIST;

-- PostgreSQL
SELECT * FROM pg_stat_activity
WHERE state = 'active';
```
