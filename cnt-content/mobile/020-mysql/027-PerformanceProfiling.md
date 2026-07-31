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