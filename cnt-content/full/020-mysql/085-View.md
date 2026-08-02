---
order: 850
title: 视图 语法速查手册
module: 'mysql'
category: 数据库
difficulty: beginner
description: 视图 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 延伸阅读
MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 InnoDB 日志与崩溃恢复

redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。
undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。
两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。
刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。

### 13.2 执行计划与优化器

EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。
优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。
排序与分组：filesort 优化为索引序；避免临时表。
慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。
