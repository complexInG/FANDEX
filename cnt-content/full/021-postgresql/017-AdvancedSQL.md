---
order: 62
title: 高级SQL
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL高级SQL：窗口函数、CTE与递归CTE、横向连接、分组集与高级聚合
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/分区表
  - postgresql/分区裁剪与分区连接
  - postgresql/MERGE语句增强
  - postgresql/JSON表格函数
prerequisites:
  - postgresql/概述与安装配置
---
## 1. 窗口函数

```sql
-- 排名函数
SELECT name, dept_id, salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num
FROM employees;

-- 累计聚合
SELECT order_date, amount,
    SUM(amount) OVER (ORDER BY order_date) AS cumulative,
    AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM daily_sales;

-- LAG/LEAD
SELECT order_date, amount,
    amount - LAG(amount) OVER (ORDER BY order_date) AS day_over_day
FROM daily_sales;

-- FILTER 子句
SELECT dept_id,
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE salary > 50000) AS high_earners
FROM employees
GROUP BY dept_id;
```

## 2. CTE 与递归 CTE

```sql
-- CTE
WITH dept_stats AS (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees GROUP BY dept_id
)
SELECT e.name, e.salary, ds.avg_salary
FROM employees e JOIN dept_stats ds ON e.dept_id = ds.dept_id;

-- 递归 CTE
WITH RECURSIVE org_tree AS (
    SELECT emp_id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, ot.level + 1
    FROM employees e JOIN org_tree ot ON e.manager_id = ot.emp_id
)
SELECT * FROM org_tree;
```

## 3. 横向连接

```sql
-- LATERAL：每行执行子查询
SELECT d.dept_name, top3.name, top3.salary
FROM departments d,
LATERAL (
    SELECT name, salary FROM employees
    WHERE dept_id = d.id
    ORDER BY salary DESC LIMIT 3
) top3;
```

## 4. 分组集

```sql
-- ROLLUP
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY ROLLUP (dept_id, job_title);

-- CUBE
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY CUBE (dept_id, job_title);

-- GROUPING SETS
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY GROUPING SETS ((dept_id, job_title), (dept_id), ());
```
## 窗口函数

**换行写法：RANK 排名函数**
`RANK() OVER (PARTITION BY <列名> ORDER BY <列名> [ASC|DESC])`
```sql
-- 部门内薪资排名
SELECT name, dept_id, salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank
FROM employees;
```

**换行写法：DENSE_RANK 密集排名**
`DENSE_RANK() OVER (PARTITION BY <列名> ORDER BY <列名> [ASC|DESC])`
```sql
-- 部门内薪资密集排名
SELECT name, dept_id, salary,
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank
FROM employees;
```

**换行写法：ROW_NUMBER 行号**
`ROW_NUMBER() OVER (PARTITION BY <列名> ORDER BY <列名> [ASC|DESC])`
```sql
-- 部门内按薪资生成行号
SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num
FROM employees;
```

**换行写法：累计求和**
`SUM(<列名>) OVER (ORDER BY <列名>)`
```sql
-- 按日期累计求和
SELECT order_date, amount,
    SUM(amount) OVER (ORDER BY order_date) AS cumulative
FROM daily_sales;
```

**换行写法：移动平均**
`AVG(<列名>) OVER (ORDER BY <列名> ROWS BETWEEN <范围>)`
```sql
-- 7 日移动平均
SELECT order_date, amount,
    AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM daily_sales;
```

**换行写法：LAG 访问前一行**
`LAG(<列名>[, <偏移量>[, <默认值>]]) OVER (ORDER BY <列名>)`
```sql
-- 计算环比变化
SELECT order_date, amount,
    amount - LAG(amount) OVER (ORDER BY order_date) AS day_over_day
FROM daily_sales;
```

**换行写法：LEAD 访问后一行**
`LEAD(<列名>[, <偏移量>[, <默认值>]]) OVER (ORDER BY <列名>)`
```sql
-- 访问下一行的金额
SELECT order_date, amount,
    LEAD(amount) OVER (ORDER BY ORDER_DATE) AS next_day_amount
FROM daily_sales;
```

**换行写法：FILTER 条件聚合**
`<聚合函数>(*) FILTER (WHERE <条件>)`
```sql
-- 条件聚合统计高收入人数
SELECT dept_id,
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE salary > 50000) AS high_earners
FROM employees
GROUP BY dept_id;
```

---

## CTE 与递归 CTE

**换行写法：普通 CTE**
`WITH <CTE 名称> AS (<SELECT 语句>) SELECT ...`
```sql
-- 使用 CTE 简化复杂查询
WITH dept_stats AS (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees GROUP BY dept_id
)
SELECT e.name, e.salary, ds.avg_salary
FROM employees e JOIN dept_stats ds ON e.dept_id = ds.dept_id;
```

**换行写法：递归 CTE**
`WITH RECURSIVE <CTE 名称> AS (<基础查询> UNION ALL <递归查询>) SELECT ...`
```sql
-- 递归查询组织树
WITH RECURSIVE org_tree AS (
    SELECT emp_id, name, manager_id, 1 AS level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, ot.level + 1
    FROM employees e JOIN org_tree ot ON e.manager_id = ot.emp_id
)
SELECT * FROM org_tree;
```

---

## 横向连接

**换行写法：LATERAL 横向连接**
`SELECT <列名> FROM <表1>, LATERAL (<子查询>) AS <别名>`
```sql
-- 每行执行子查询获取前 3 名
SELECT d.dept_name, top3.name, top3.salary
FROM departments d,
LATERAL (
    SELECT name, salary FROM employees
    WHERE dept_id = d.id
    ORDER BY salary DESC LIMIT 3
) top3;
```

---

## 分组集

**换行写法：ROLLUP 层次汇总**
`GROUP BY ROLLUP (<列名>[, <列名>...])`
```sql
-- 按部门和职位层次汇总薪资
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY ROLLUP (dept_id, job_title);
```

**换行写法：CUBE 多维汇总**
`GROUP BY CUBE (<列名>[, <列名>...])`
```sql
-- 按部门和职位多维汇总薪资
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY CUBE (dept_id, job_title);
```

**换行写法：GROUPING SETS 自定义分组集**
`GROUP BY GROUPING SETS ((<列组合1>), (<列组合2>), ...)`
```sql
-- 自定义分组集汇总薪资
SELECT dept_id, job_title, SUM(salary)
FROM employees
GROUP BY GROUPING SETS ((dept_id, job_title), (dept_id), ());
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
| 高级SQL | 017-AdvancedSQL | 本文自身 |
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
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文的并列主题 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文的并列主题 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
