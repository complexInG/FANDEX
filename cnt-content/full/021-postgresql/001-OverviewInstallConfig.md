---
order: 1
title: 概述与安装配置
module: postgresql
category: PostgreSQL
difficulty: beginner
description: 'PostgreSQL 17概述、安装与配置、pg_hba.conf认证、postgresql.conf核心参数、连接管理、角色与权限。'
author: fanquanpp
updated: '2026-08-01'
related:
  - postgresql/事务与并发控制
  - postgresql/索引与查询优化
prerequisites: []
---
## 0. 零基础入门（从零开始）

### 0.1 零基础起点

本模块讲解 PostgreSQL 数据库。零基础可学，建议先完成 019-sql 模块掌握通用 SQL，再安装 PostgreSQL 16+（官网下载安装包，记住安装时设置的 postgres 用户密码）。
启动 psql 命令行（Windows: 开始菜单里的 SQL Shell，macOS/Linux: psql -U postgres），输入密码后看到 postgres=# 提示符即连接成功。

### 0.2 第一个 PostgreSQL 操作：建表、插入、查询

```sql
-- 创建一张书籍表
CREATE TABLE books (
  id SERIAL PRIMARY KEY,     -- SERIAL: 自动递增整数
  title TEXT NOT NULL,       -- 书名
  price NUMERIC(8,2)         -- 价格：最多 8 位，2 位小数
);

INSERT INTO books (title, price) VALUES ('深入理解计算机系统', 139.00);

SELECT title, price FROM books;
```

CREATE TABLE 定义表结构；SERIAL 是 PostgreSQL 的特色写法，等价于“自动递增整数”，每插入一行自动编号，无需手动指定 id。
NUMERIC(8,2) 表示最多 8 位有效数字、其中 2 位小数，适合存储金额，避免浮点误差。
INSERT 语句的写法与标准 SQL 一致：字符串用单引号，数值直接写。
SELECT title, price FROM books 查询全部书籍的书名与价格，执行后看到一行结果。
这套“建表-插入-查询”流程是所有 PostgreSQL 应用的起点；后续的约束、索引、视图都在此基础上增强。

### 0.3 学习路径

完成上面的第一步后，按以下顺序继续学习：

- 002-安装与配置：连接参数、客户端工具与权限。
- 003-数据类型：TEXT、NUMERIC、TIMESTAMPTZ 的选择。
- 004-查询进阶：窗口函数与 CTE。


## 1. PostgreSQL 17 概述

### 1.1 PostgreSQL 简介

PostgreSQL 是全球最先进的**开源对象-关系型数据库管理系统**，以可靠性、功能丰富和可扩展性著称。PostgreSQL 17 于 2024 年发布，带来多项重要改进。

### 1.2 核心特性

| 特性     | 说明                                   |
| :------- | :------------------------------------- |
| SQL 标准 | 高度兼容 SQL:2023 标准                 |
| 数据类型 | JSON/JSONB、数组、范围、几何、UUID 等  |
| 索引     | B-tree、Hash、GiST、GIN、SP-GiST、BRIN |
| 并发控制 | MVCC 多版本并发控制                    |
| 扩展性   | 自定义类型、函数、操作符、索引方法     |
| 全文检索 | 内置 tsvector/tsquery 全文搜索         |
| 外部数据 | FDW 外部数据包装器                     |
| 逻辑复制 | 发布/订阅模式                          |

### 1.3 PostgreSQL 17 新特性

```
- SQL/JSON 标准化: JSON_TABLE、JSON_QUERY 等
- MERGE 语句增强: 支持 RETURNING 子句
- 增量备份: pg_basebackup 支持增量备份
- VACUUM 改进: tid store 内存优化
- 逻辑复制增强: 故障转移改进
- 性能提升: 并行查询优化、I/O 并发改进
```

## 2. 安装与配置

### 2.1 Linux 安装

```bash
# Ubuntu/Debian
sudo apt install -y postgresql-17 postgresql-contrib-17

# CentOS/Rocky (使用 PGDG 仓库)
sudo dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-9-x86_64/pgdg-redhat-repo-latest.noarch.rpm
sudo dnf install -y postgresql17-server postgresql17-contrib

# 初始化数据目录
sudo /usr/pgsql-17/bin/postgresql-17-setup initdb

# 启动服务
sudo systemctl enable --now postgresql-17
```

### 2.2 Docker 安装

```bash
# 运行 PostgreSQL 容器
docker run -d \
  --name postgres17 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=SecurePass123 \
  -e POSTGRES_DB=fandex \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:17

# 连接数据库
docker exec -it postgres17 psql -U admin -d fandex
```

### 2.3 Windows 安装

```powershell
# 使用 EDB 安装器
# 下载: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

# 或使用 chocolatey
choco install postgresql17

# 配置环境变量
$env:PATH += ";C:\Program Files\PostgreSQL\17\bin"
```

## 3. pg_hba.conf 认证配置

### 3.1 配置文件位置

```
Linux:  /etc/postgresql/17/main/pg_hba.conf
Docker: /var/lib/postgresql/data/pg_hba.conf
Windows: C:\Program Files\PostgreSQL\17\data\pg_hba.conf
```

### 3.2 认证规则格式

```
# TYPE  DATABASE  USER    ADDRESS         METHOD
local   all       all                     peer
host    all       all     127.0.0.1/32    scram-sha-256
host    all       all     ::1/128         scram-sha-256
host    all       admin   192.168.1.0/24  scram-sha-256
host    replication replicator 192.168.1.0/24 scram-sha-256
```

### 3.3 认证方法

| 方法          | 安全级别 | 说明                          |
| :------------ | :------- | :---------------------------- |
| trust         | 无       | 无需密码，仅限开发环境        |
| reject        | -        | 拒绝连接                      |
| md5           | 中       | MD5 加密密码（旧版）          |
| scram-sha-256 | 高       | SCRAM-SHA-256 认证（推荐）    |
| peer          | 高       | 操作系统用户名匹配（仅local） |
| ident         | 中       | ident 协议认证                |
| cert          | 极高     | SSL 客户端证书认证            |
| gss/sspi      | 高       | Kerberos 认证                 |

### 3.4 安全配置示例

```
# 生产环境推荐配置
# TYPE  DATABASE  USER      ADDRESS          METHOD
local   all       postgres                   peer
host    all       postgres  127.0.0.1/32     reject
host    all       app_user  10.0.0.0/8       scram-sha-256
hostssl all       app_user  0.0.0.0/0        cert scram-sha-256
host    replication repl    192.168.1.0/24   scram-sha-256
```

## 4. postgresql.conf 核心参数

### 4.1 连接参数

```ini
# 基本连接
listen_addresses = '*'          # 监听地址（* = 所有）
port = 5432                     # 监听端口
max_connections = 200           # 最大连接数
superuser_reserved_connections = 3  # 超级用户保留连接数

# TCP 配置
tcp_keepalives_idle = 60        # 空闲探测间隔(秒)
tcp_keepalives_interval = 10    # 探测重试间隔
tcp_keepalives_count = 10       # 探测失败次数
```

### 4.2 内存参数

```ini
# 内存配置（以 16GB 内存服务器为例）
shared_buffers = 4GB            # 共享缓冲区（建议 25% 内存）
effective_cache_size = 12GB     # 查询规划器缓存估计（75% 内存）
work_mem = 64MB                 # 排序/哈希操作内存
maintenance_work_mem = 512MB    # 维护操作内存(VACUUM/CREATE INDEX)
huge_pages = try                # 启用大页内存

# WAL 配置
wal_buffers = 64MB              # WAL 缓冲区
checkpoint_completion_target = 0.9
max_wal_size = 2GB
min_wal_size = 512MB
```

### 4.3 查询优化参数

```ini
# 查询规划
random_page_cost = 1.1          # SSD 设为 1.1，HDD 默认 4.0
effective_io_concurrency = 200  # SSD 设为 200，HDD 默认 1
max_worker_processes = 8        # 最大后台工作进程
max_parallel_workers_per_gather = 4  # 每个查询最大并行工作进程
max_parallel_workers = 8        # 最大并行工作进程总数
jit = on                        # 启用 JIT 编译
```

### 4.4 日志参数

```ini
# 日志配置
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d.log'
log_rotation_age = 1d
log_rotation_size = 100MB
log_min_duration_statement = 1000  # 记录超过 1 秒的慢查询
log_checkpoints = on
log_connections = on
log_disconnections = on
log_lock_waits = on
log_temp_files = 0
log_line_prefix = '%t [%p]: db=%d,user=%u,app=%a,client=%h '
```

## 5. 连接管理

### 5.1 连接方式

```bash
# 命令行连接
psql -h 192.168.1.10 -p 5432 -U admin -d fandex

# 使用连接字符串
psql "postgresql://admin:password@192.168.1.10:5432/fandex?sslmode=require"

# 使用 .pgpass 免密
cat > ~/.pgpass << 'EOF'
192.168.1.10:5432:fandex:admin:SecurePass123
EOF
chmod 600 ~/.pgpass
```

### 5.2 连接池（PgBouncer）

```ini
# pgbouncer.ini
[databases]
fandex = host=127.0.0.1 port=5432 dbname=fandex

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction          # 事务级连接池
max_client_conn = 1000
default_pool_size = 25
reserve_pool_size = 5
reserve_pool_timeout = 3
server_idle_timeout = 300
```

### 5.3 活动连接查询

```sql
-- 查看当前连接
SELECT pid, usename, datname, client_addr, state, query, query_start
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY query_start;

-- 终止空闲连接
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND query_start < now() - interval '30 minutes'
  AND pid != pg_backend_pid();

-- 连接数统计
SELECT usename, count(*)
FROM pg_stat_activity
GROUP BY usename
ORDER BY count DESC;
```

## 6. 角色与权限

### 6.1 角色管理

```sql
-- 创建角色（角色 = 用户，可登录角色即用户）
CREATE ROLE app_user WITH LOGIN PASSWORD 'SecurePass123';
CREATE ROLE app_admin WITH LOGIN PASSWORD 'AdminPass456' SUPERUSER;
CREATE ROLE readonly WITH LOGIN PASSWORD 'ReadOnly789';

-- 修改角色属性
ALTER ROLE app_user CONNECTION LIMIT 50;
ALTER ROLE app_user VALID UNTIL '2026-12-31';
ALTER ROLE app_user SET work_mem = '128MB';

-- 创建组角色（不可登录）
CREATE ROLE dev_team NOLOGIN;
GRANT dev_team TO app_user, app_admin;

-- 删除角色
DROP ROLE IF EXISTS old_user;
```

### 6.2 权限管理

```sql
-- 数据库权限
GRANT CONNECT ON DATABASE fandex TO app_user;
GRANT ALL ON DATABASE fandex TO app_admin;

-- Schema 权限
GRANT USAGE ON SCHEMA public TO app_user;
GRANT CREATE ON SCHEMA public TO app_admin;

-- 表权限
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO app_user;
GRANT ALL ON ALL TABLES IN SCHEMA public TO app_admin;

-- 序列权限
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- 默认权限（自动应用于未来创建的对象）
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO readonly;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT, INSERT, UPDATE ON TABLES TO app_user;

-- 撤销权限
REVOKE DELETE ON ALL TABLES IN SCHEMA public FROM app_user;

-- 查看权限
\dp                           # psql 命令
SELECT grantee, table_name, privilege_type
FROM information_schema.table_privileges
WHERE table_schema = 'public'
ORDER BY grantee, table_name;
```

### 6.3 行级安全策略（RLS）

```sql
-- 启用 RLS
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

-- 创建策略：用户只能看到自己的订单
CREATE POLICY user_orders ON orders
  FOR ALL
  TO app_user
  USING (user_id = current_user_id());

-- 管理员可看所有
CREATE POLICY admin_all ON orders
  FOR ALL
  TO app_admin
  USING (true)
  WITH CHECK (true);

-- 查看策略
SELECT * FROM pg_policies WHERE tablename = 'orders';
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
| 概述与安装配置 | 001-OverviewInstallConfig | 本文自身 |
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
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文的并列主题 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文的并列主题 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
