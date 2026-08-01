---
order: 460
title: PostgreSQL 窗口函数
module: postgresql

category: '021-postgresql'
difficulty: beginner
description: PostgreSQL 窗口函数 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 参考文献

PostgreSQL 官方文档：https://www.postgresql.org/docs/
PostgreSQL 中文文档：https://www.postgresql.org/docs/current/index.html
PGXN 扩展仓库：https://pgxn.org/
PostGIS：https://postgis.net/
pgvector：https://github.com/pgvector/pgvector

## 延伸阅读

PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 PostgreSQL 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 MVCC 与 vacuum 机制

行头存储 xmin（创建事务）与 xmax（删除事务）；可见性由快照比较决定。
更新 = 插入新版本 + 旧版本标记；旧版本对旧事务可见，vacuum 回收不再可见的死元组。
事务 ID 回卷：约 21 亿事务后需要冻结；autovacuum 与 vacuum freeze 防止。
监控：SELECT n_dead_tup, last_autovacuum FROM pg_stat_user_tables。

### 13.2 逻辑复制与高可用

发布（publication）定义表集，订阅（subscription）在目标端应用变更；支持过滤与列子集。
流复制：主库 WAL 发送到备库，同步/异步模式；级联复制扩展拓扑。
Patroni 使用分布式共识（etcd）选主，故障自动切换，配合虚拟 IP。
切换演练与数据校验（pg_checksums）是可用性工程必备。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与安装配置 | 001-OverviewInstallConfig | 本文的前置基础 |
| 事务与并发控制 | 002-TransactionConcurrencyControl | 本文的并列主题 |
| 索引与查询优化 | 003-IndexQueryOptimization | 本文的性能延伸 |
| 高级SQL与扩展 | 004-AdvancedSQLExtension | 本文的并列主题 |
| 复制与高可用 | 005-ReplicationHA | 本文的并列主题 |
| 体系架构 | 006-SystemArchitecture | 本文的原理深化 |
| 锁机制 | 007-LockMechanism | 本文的原理深化 |
| 死锁检测与处理 | 008-DeadlockDetectionHandling | 本文的并列主题 |
| VACUUM机制 | 009-VACUUMMechanism | 本文的原理深化 |
| 事务ID回卷预防 | 010-TransactionIDWraparoundPrevention | 本文的并列主题 |
| 索引类型 | 011-IndexType | 本文的并列主题 |
| 覆盖索引与部分索引 | 012-CoveringIndexPartialIndex | 本文的并列主题 |
| KNN向量索引 | 013-KNNVectorIndex | 本文的并列主题 |
| 查询优化 | 014-QueryOptimization | 本文的性能延伸 |
| 分区表 | 015-PartitionedTable | 本文的并列主题 |
| 分区裁剪与分区连接 | 016-PartitionPruningPartitionJoin | 本文的并列主题 |
| 高级SQL | 017-AdvancedSQL | 本文的并列主题 |
| MERGE语句增强 | 018-MERGEStatementEnhancement | 本文的并列主题 |
| JSON-TABLE | 019-JSONTABLE | 本文的并列主题 |
| 全文检索 | 020-FullTextSearch | 本文的并列主题 |
| 地理空间对象 | 021-GeoSpatialObject | 本文的并列主题 |
| 存储过程与函数 | 022-StoredProcedureAndFunction | 本文的并列主题 |
| 触发器与事件触发器 | 023-TriggerEventTrigger | 本文的并列主题 |
| 扩展模块 | 024-ExtensionModule | 本文的并列主题 |
| FDW外部数据包装器 | 025-FDWFDW | 本文的并列主题 |
| 流复制 | 026-StreamingReplication | 本文的并列主题 |
| 级联复制 | 027-CascadingReplication | 本文的并列主题 |
| 物理复制槽 | 028-PhysicalReplicationSlot | 本文的并列主题 |
| 逻辑解码与输出插件 | 029-LogicalDecodingOutputPlugin | 本文的并列主题 |
| 增量备份 | 030-IncrementalBackup | 本文的并列主题 |
| 订阅与发布 | 031-SubscribePublish | 本文的并列主题 |
| SSL-TLS加密连接 | 032-SSLEncryptionConnection | 本文的安全延伸 |
| 基于角色的权限管理 | 033-RoleBasedPermissionManagement | 本文的安全延伸 |
| 行级安全策略 | 034-RowLevelSecurity | 本文的安全延伸 |
| 数据加密存储 | 035-DataEncryptionStorage | 本文的安全延伸 |
| 审计日志 | 036-AuditLog | 本文的并列主题 |
| 序列与自增列 | 037-SequenceAutoIncrement | 本文的并列主题 |
| 生成列 | 038-GeneratedColumn | 本文的并列主题 |
| 可更新视图 | 039-UpdatableView | 本文的并列主题 |
| 并行查询 | 040-ParallelQuery | 本文的并列主题 |
| 逻辑复制与物理复制对比 | 041-LogicalPhysicalReplicationCompare | 本文的并列主题 |
| JSONB与JSON差异 | 042-JSONBJSONDifference | 本文的并列主题 |
| 扩展模块详解 | 043-ExtensionModuleDetailed | 本文的并列主题 |
| PostgreSQL DDL 数据定义 | 044-DDL | 本文的并列主题 |
| PostgreSQL DML 数据操作 | 045-DML | 本文的并列主题 |
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文自身 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文的并列主题 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
