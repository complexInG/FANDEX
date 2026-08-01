---
order: 78
title: 基于角色的权限管理
module: postgresql
category: PostgreSQL
difficulty: intermediate
description: PostgreSQL基于角色的权限管理：角色继承、组角色、默认权限与权限审计
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/订阅与发布
  - 'postgresql/SSL-TLS加密连接'
  - postgresql/行级安全策略
  - postgresql/数据加密存储
prerequisites:
  - postgresql/概述与安装配置
---

# PostgreSQL 基于角色的权限管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 角色体系

PostgreSQL 使用角色统一管理用户和组。

```sql
-- 创建登录角色（用户）
CREATE ROLE app_user LOGIN PASSWORD 'password';

-- 创建组角色（不能登录）
CREATE ROLE readonly NOLOGIN;
CREATE ROLE readwrite NOLOGIN;
CREATE ROLE admin NOLOGIN;

-- 授予权限给组角色
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO readwrite;
GRANT ALL PRIVILEGES ON SCHEMA public TO admin;

-- 将组角色授予用户
GRANT readonly TO app_read;
GRANT readwrite TO app_write;
```

## 2. 角色继承

```sql
-- 默认角色继承
SET ROLE readonly;  -- 切换到 readonly 角色
SELECT current_user;  -- readonly
RESET ROLE;  -- 恢复

-- 禁止继承
ALTER ROLE app_user NOINHERIT;
-- 需要显式 SET ROLE 才能获得组角色权限
```

## 3. 默认权限

```sql
-- 新建表的默认权限
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT SELECT ON TABLES TO readonly;

ALTER DEFAULT PRIVILEGES FOR ROLE admin
    GRANT SELECT ON TABLES TO readonly;
```

## 4. 查看权限

```sql
-- 查看表权限
SELECT grantee, privilege_type
FROM information_schema.table_privileges
WHERE table_name = 'employees';

-- 查看角色成员
SELECT r.rolname, m.rolname AS member
FROM pg_roles r
JOIN pg_auth_members am ON r.oid = am.roleid
JOIN pg_roles m ON am.member = m.oid;
```
## 用户管理

**单行写法：创建用户**
`CREATE USER <用户名> [WITH] PASSWORD '<密码>'`
```sql
-- 创建带密码的用户
CREATE USER app_user WITH PASSWORD 'StrongP@ss123';
```

**单行写法：创建带登录权限的用户**
`CREATE ROLE <角色名> WITH LOGIN PASSWORD '<密码>'`
```sql
-- 创建带登录权限的角色
CREATE ROLE app_role WITH LOGIN PASSWORD 'StrongP@ss123';
```

**单行写法：修改用户密码**
`ALTER USER <用户名> [WITH] PASSWORD '<新密码>'`
```sql
-- 修改用户密码
ALTER USER app_user WITH PASSWORD 'NewP@ss456';
```

**单行写法：删除用户**
`DROP USER [IF EXISTS] <用户名>`
```sql
-- 删除用户
DROP USER IF EXISTS app_user;
```

**单行写法：查看所有用户**
`SELECT <列名> FROM pg_user`
```sql
-- 查看所有用户列表
SELECT usename, usesuper FROM pg_user;
```

---

## 角色管理

**单行写法：创建角色**
`CREATE ROLE <角色名>`
```sql
-- 创建角色
CREATE ROLE readonly;
```

**单行写法：创建带属性的角色**
`CREATE ROLE <角色名> WITH <属性>`
```sql
-- 创建带登录和创建数据库属性的角色
CREATE ROLE admin WITH LOGIN CREATEDB CREATEROLE;
```

**单行写法：将角色分配给用户**
`GRANT <角色名> TO <用户名>`
```sql
-- 分配角色给用户
GRANT readonly TO app_user;
```

**单行写法：撤销用户角色**
`REVOKE <角色名> FROM <用户名>`
```sql
-- 撤销用户的角色
REVOKE readonly FROM app_user;
```

**单行写法：删除角色**
`DROP ROLE [IF EXISTS] <角色名>`
```sql
-- 删除角色
DROP ROLE IF EXISTS readonly;
```

**单行写法：查看所有角色**
`SELECT <列名> FROM pg_roles`
```sql
-- 查看所有角色
SELECT rolname, rolsuper, rolcreaterole FROM pg_roles;
```

---

## 权限管理

**单行写法：授予连接数据库权限**
`GRANT CONNECT ON DATABASE <库名> TO <角色名>`
```sql
-- 授予连接数据库权限
GRANT CONNECT ON DATABASE mydb TO readonly;
```

**单行写法：授予使用模式权限**
`GRANT USAGE ON SCHEMA <模式名> TO <角色名>`
```sql
-- 授予使用模式权限
GRANT USAGE ON SCHEMA public TO readonly;
```

**单行写法：授予表查询权限**
`GRANT SELECT ON <表名> TO <角色名>`
```sql
-- 授予表查询权限
GRANT SELECT ON users TO readonly;
```

**单行写法：授予表所有权限**
`GRANT ALL ON <表名> TO <角色名>`
```sql
-- 授予表所有权限
GRANT ALL ON users TO admin;
```

**单行写法：授予模式所有表查询权限**
`GRANT SELECT ON ALL TABLES IN SCHEMA <模式名> TO <角色名>`
```sql
-- 授予模式所有表查询权限
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```

**单行写法：授予模式所有表所有权限**
`GRANT ALL ON ALL TABLES IN SCHEMA <模式名> TO <角色名>`
```sql
-- 授予模式所有表所有权限
GRANT ALL ON ALL TABLES IN SCHEMA public TO admin;
```

**单行写法：授予序列使用权限**
`GRANT USAGE ON SEQUENCE <序列名> TO <角色名>`
```sql
-- 授予序列使用权限
GRANT USAGE ON SEQUENCE users_id_seq TO app_user;
```

**单行写法：撤销表查询权限**
`REVOKE SELECT ON <表名> FROM <角色名>`
```sql
-- 撤销表查询权限
REVOKE SELECT ON users FROM readonly;
```

**单行写法：撤销表所有权限**
`REVOKE ALL ON <表名> FROM <角色名>`
```sql
-- 撤销表所有权限
REVOKE ALL ON users FROM readonly;
```

**单行写法：修改默认权限**
`ALTER DEFAULT PRIVILEGES IN SCHEMA <模式名> GRANT SELECT ON TABLES TO <角色名>`
```sql
-- 设置未来创建表的默认权限
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;
```

---

## 默认角色

**单行写法：设置用户默认角色**
`SET ROLE <角色名>`
```sql
-- 切换当前会话角色
SET ROLE readonly;
```

**单行写法：重置为原始角色**
`RESET ROLE`
```sql
-- 重置为原始用户
RESET ROLE;
```

**单行写法：设置默认搜索路径**
`ALTER ROLE <角色名> SET search_path TO <模式名>`
```sql
-- 设置角色的默认搜索路径
ALTER ROLE app_user SET search_path TO myschema, public;
```

---

## 权限查看

**单行写法：查看表权限**
`\dp <表名>`
```sql
-- 查看表的权限信息
\dp users;
```

**单行写法：查看角色权限**
`SELECT <列名> FROM information_schema.role_table_grants WHERE <条件>`
```sql
-- 查看角色表权限
SELECT grantee, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE table_name = 'users';
```

**单行写法：查看用户权限**
`\du <用户名>`
```sql
-- 查看用户角色和属性
\du app_user;
```

**单行写法：查看数据库权限**
`SELECT <列名> FROM pg_database WHERE <条件>`
```sql
-- 查看数据库权限信息
SELECT datname, datacl FROM pg_database WHERE datname = 'mydb';
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
| 基于角色的权限管理 | 033-RoleBasedPermissionManagement | 本文自身 |
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
