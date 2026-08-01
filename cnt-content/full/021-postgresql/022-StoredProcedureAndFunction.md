---
order: 67
title: 存储过程与函数
module: postgresql
category: PostgreSQL
difficulty: advanced
description: PostgreSQL存储过程与函数：PL/pgSQL、PL/Python、PL/Perl与过程语言扩展
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/全文检索
  - postgresql/地理空间对象
  - postgresql/触发器与事件触发器
  - postgresql/扩展模块
prerequisites:
  - postgresql/概述与安装配置
---
## 1. PL/pgSQL

### 1.1 函数

```sql
CREATE OR REPLACE FUNCTION calculate_bonus(
    p_salary NUMERIC,
    p_performance INTEGER
) RETURNS NUMERIC AS $$
DECLARE
    v_bonus NUMERIC;
BEGIN
    v_bonus := p_salary * p_performance / 100.0;
    RETURN v_bonus;
END;
$$ LANGUAGE plpgsql;

-- 调用
SELECT calculate_bonus(50000, 15);
```

### 1.2 存储过程（PROCEDURE）

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    p_from INTEGER,
    p_to INTEGER,
    p_amount NUMERIC
) AS $$
BEGIN
    UPDATE accounts SET balance = balance - p_amount WHERE id = p_from;
    UPDATE accounts SET balance = balance + p_amount WHERE id = p_to;
    COMMIT;
END;
$$ LANGUAGE plpgsql;

-- 调用
CALL transfer_funds(1, 2, 1000);
```

### 1.3 控制流

```sql
CREATE OR REPLACE FUNCTION get_grade(p_score INTEGER)
RETURNS VARCHAR(10) AS $$
BEGIN
    IF p_score >= 90 THEN
        RETURN 'A';
    ELSIF p_score >= 80 THEN
        RETURN 'B';
    ELSIF p_score >= 70 THEN
        RETURN 'C';
    ELSE
        RETURN 'D';
    END IF;
END;
$$ LANGUAGE plpgsql;
```

### 1.4 游标与循环

```sql
CREATE OR REPLACE PROCEDURE process_orders() AS $$
DECLARE
    order_record RECORD;
BEGIN
    FOR order_record IN
        SELECT id, amount FROM orders WHERE status = 'pending'
    LOOP
        UPDATE orders SET status = 'processing' WHERE id = order_record.id;
        -- 处理逻辑
    END LOOP;
END;
$$ LANGUAGE plpgsql;
```

## 2. PL/Python

```sql
CREATE EXTENSION plpython3u;

CREATE OR REPLACE FUNCTION python_hash(p_text TEXT)
RETURNS TEXT AS $$
import hashlib
return hashlib.sha256(p_text.encode()).hexdigest()
$$ LANGUAGE plpython3u;
```

## 3. PL/Perl

```sql
CREATE EXTENSION plperl;

CREATE OR REPLACE FUNCTION perl_reverse(p_text TEXT)
RETURNS TEXT AS $$
return reverse($_[0]);
$$ LANGUAGE plperl;
```
## 存储过程基础

**换行写法：创建无参存储过程**
`CREATE PROCEDURE <过程名>() LANGUAGE plpgsql AS $$ BEGIN <过程体> END $$`
```sql
-- 创建查询所有用户的存储过程
CREATE PROCEDURE GetAllUsers()
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT id, username, email, created_at
    FROM users
    ORDER BY created_at DESC;
END $$;
```

**单行写法：调用存储过程**
`CALL <过程名>([<参数>...])`
```sql
-- 调用存储过程
CALL GetAllUsers();
```

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>([<参数类型>...])`
```sql
-- 删除存储过程
DROP PROCEDURE IF EXISTS GetAllUsers();
```

---

## PL/pgSQL 控制结构

**换行写法：IF 条件判断**
`IF <条件> THEN <语句> [ELSIF <条件> THEN <语句>] [ELSE <语句>] END IF`
```sql
-- 根据金额计算折扣率
CREATE FUNCTION GetDiscount(p_amount DECIMAL)
RETURNS DECIMAL
LANGUAGE plpgsql AS $$
DECLARE
    v_discount DECIMAL;
BEGIN
    IF p_amount >= 1000 THEN
        v_discount := 0.20;
    ELSIF p_amount >= 500 THEN
        v_discount := 0.10;
    ELSE
        v_discount := 0.00;
    END IF;
    RETURN v_discount;
END $$;
```

**换行写法：CASE 多分支**
`CASE WHEN <条件> THEN <值> [WHEN ...] [ELSE <值>] END`
```sql
-- 根据状态返回描述
CREATE FUNCTION GetStatusDesc(p_status INT)
RETURNS TEXT
LANGUAGE plpgsql AS $$
BEGIN
    RETURN CASE
        WHEN p_status = 1 THEN 'Active'
        WHEN p_status = 0 THEN 'Inactive'
        ELSE 'Unknown'
    END;
END $$;
```

**换行写法：WHILE 循环**
`WHILE <条件> LOOP <语句> END LOOP`
```sql
-- WHILE 循环累加
CREATE FUNCTION SumToN(p_n INT)
RETURNS INT
LANGUAGE plpgsql AS $$
DECLARE
    v_i INT := 1;
    v_sum INT := 0;
BEGIN
    WHILE v_i <= p_n LOOP
        v_sum := v_sum + v_i;
        v_i := v_i + 1;
    END LOOP;
    RETURN v_sum;
END $$;
```

**换行写法：FOR 循环**
`FOR <变量> IN <起始>..<结束> LOOP <语句> END LOOP`
```sql
-- FOR 循环累加
CREATE FUNCTION SumRange(p_start INT, p_end INT)
RETURNS INT
LANGUAGE plpgsql AS $$
DECLARE
    v_sum INT := 0;
BEGIN
    FOR i IN p_start..p_end LOOP
        v_sum := v_sum + i;
    END LOOP;
    RETURN v_sum;
END $$;
```

**换行写法：FOR IN 查询循环**
`FOR <记录> IN <SELECT 语句> LOOP <语句> END LOOP`
```sql
-- 遍历查询结果
CREATE PROCEDURE ProcessUsers()
LANGUAGE plpgsql AS $$
DECLARE
    v_user RECORD;
BEGIN
    FOR v_user IN SELECT id, username FROM users WHERE status = 1 LOOP
        INSERT INTO user_log (user_id, action) VALUES (v_user.id, 'processed');
    END LOOP;
END $$;
```

**换行写法：LOOP 循环**
`LOOP <语句> EXIT WHEN <条件> END LOOP`
```sql
-- LOOP 循环配合 EXIT 跳出
CREATE FUNCTION LoopDemo(p_limit INT)
RETURNS INT
LANGUAGE plpgsql AS $$
DECLARE
    v_i INT := 0;
    v_sum INT := 0;
BEGIN
    LOOP
        v_i := v_i + 1;
        EXIT WHEN v_i > p_limit;
        v_sum := v_sum + v_i;
    END LOOP;
    RETURN v_sum;
END $$;
```

---

## 函数创建

**换行写法：创建标量函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS <类型> LANGUAGE plpgsql AS $$ BEGIN RETURN <值> END $$`
```sql
-- 计算订单总金额的函数
CREATE FUNCTION CalculateOrderTotal(p_order_id INT)
RETURNS DECIMAL(12, 2)
LANGUAGE plpgsql AS $$
DECLARE
    v_total DECIMAL(12, 2);
BEGIN
    SELECT SUM(quantity * unit_price)
    INTO v_total
    FROM order_items
    WHERE order_id = p_order_id;
    RETURN COALESCE(v_total, 0);
END $$;
```

**换行写法：创建返回表函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS TABLE(<列定义>) LANGUAGE plpgsql AS $$ BEGIN <查询> END $$`
```sql
-- 返回表结果集的函数
CREATE FUNCTION GetUsersByStatus(p_status INT)
RETURNS TABLE(id INT, username VARCHAR, email VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT id, username, email FROM users WHERE status = p_status;
END $$;
```

**换行写法：创建集合返回函数**
`CREATE FUNCTION <函数名>([<参数>]) RETURNS SETOF <表名> LANGUAGE plpgsql AS $$ BEGIN <查询> END $$`
```sql
-- 返回整张表的函数
CREATE FUNCTION GetActiveUsers()
RETURNS SETOF users
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY SELECT * FROM users WHERE status = 1;
END $$;
```

---

## 函数调用

**单行写法：SELECT 调用函数**
`SELECT <函数名>(<参数>)`
```sql
-- 调用标量函数
SELECT CalculateOrderTotal(1001) AS total;
```

**换行写法：FROM 调用表函数**
`SELECT * FROM <函数名>(<参数>)`
```sql
-- 调用返回表函数
SELECT * FROM GetUsersByStatus(1);
```

**换行写法：在查询中使用函数**
`SELECT <列名>, <函数名>(<列名>) AS <别名> FROM <表名>`
```sql
-- 在 SELECT 中使用函数
SELECT name, CalculateAge(birthdate) AS age FROM employees;
```

---

## 存储过程调用

**换行写法：带参数的存储过程**
`CALL <过程名>(<参数值>[, ...])`
```sql
-- 调用带参数的存储过程
CALL UpdateUserStatus(1, 0);
```

**换行写法：带事务的存储过程**
`CREATE PROCEDURE <过程名>(<参数>) LANGUAGE plpgsql AS $$ BEGIN <事务> END $$`
```sql
-- 存储过程内使用事务
CREATE PROCEDURE TransferFunds(p_from INT, p_to INT, p_amount DECIMAL)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE accounts SET balance = balance - p_amount WHERE id = p_from;
    UPDATE accounts SET balance = balance + p_amount WHERE id = p_to;
    COMMIT;
END $$;
```

---

## 存储过程删除

**单行写法：删除存储过程**
`DROP PROCEDURE [IF EXISTS] <过程名>([<参数类型>...])`
```sql
-- 删除带参数的存储过程
DROP PROCEDURE IF EXISTS TransferFunds(INT, INT, DECIMAL);
```

**单行写法：删除函数**
`DROP FUNCTION [IF EXISTS] <函数名>([<参数类型>...])`
```sql
-- 删除函数
DROP FUNCTION IF EXISTS CalculateOrderTotal(INT);
```

**单行写法：修改函数**
`ALTER FUNCTION <函数名>([<参数类型>...]) OWNER TO <用户>`
```sql
-- 修改函数所有者
ALTER FUNCTION CalculateOrderTotal(INT) OWNER TO admin;
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
| 存储过程与函数 | 022-StoredProcedureAndFunction | 本文自身 |
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
