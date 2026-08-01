---
order: 480
title: PostgreSQL psql CLI 命令
module: 021-postgresql
category: '021-postgresql'
difficulty: beginner
description: PostgreSQL psql CLI 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# PostgreSQL psql CLI 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 连接登录

**单行写法：本地连接**
`psql -U <用户名> -d <数据库名>`
```bash
# 连接本地数据库
psql -U postgres -d mydb
```

**单行写法：指定主机端口连接**
`psql -h <主机> -p <端口> -U <用户名> -d <数据库>`
```bash
# 连接远程 PostgreSQL 服务器
psql -h 192.168.1.100 -p 5432 -U appuser -d mydb
```

**单行写法：使用连接字符串**
`psql "postgresql://<用户>:<密码>@<主机>:<端口>/<数据库>"`
```bash
# 使用 URI 连接字符串
psql "postgresql://appuser:password@192.168.1.100:5432/mydb"
```

**单行写法：交互式输入密码**
`psql -U <用户名> -d <数据库> -W`
```bash
# 强制提示输入密码
psql -U postgres -d mydb -W
```

**单行写法：指定角色连接**
`psql -U <角色名> -d <数据库>`
```bash
# 指定角色登录
psql -U appuser -d mydb
```

**单行写法：使用环境变量连接**
`PGPASSWORD=<密码> psql -h <主机> -U <用户> -d <数据库>`
```bash
# 通过环境变量传递密码
PGPASSWORD=StrongPass psql -h 192.168.1.100 -U postgres -d mydb
```

---

## 执行命令

**单行写法：执行单条 SQL**
`psql -U <用户> -d <数据库> -c "<SQL>"`
```bash
# 执行单条 SQL 后退出
psql -U postgres -d mydb -c "SELECT version();"
```

**单行写法：执行多条 SQL**
`psql -U <用户> -d <数据库> -c "<SQL1>" -c "<SQL2>"`
```bash
# 执行多条 SQL
psql -U postgres -d mydb -c "SELECT 1;" -c "SELECT 2;"
```

**单行写法：执行 SQL 文件**
`psql -U <用户> -d <数据库> -f <文件路径>`
```bash
# 执行 SQL 脚本文件
psql -U postgres -d mydb -f /path/to/script.sql
```

**单行写法：从标准输入读取**
`psql -U <用户> -d <数据库> < <文件>`
```bash
# 从文件重定向输入
psql -U postgres -d mydb < script.sql
```

**单行写法：执行并输出到文件**
`psql -U <用户> -d <数据库> -c "<SQL>" -o <输出文件>`
```bash
# 将查询结果输出到文件
psql -U postgres -d mydb -c "SELECT * FROM users;" -o users.txt
```

---

## 输出格式

**单行写法：表格输出（默认）**
`psql -U <用户> -d <数据库> -c "<SQL>" --format=aligned`
```bash
# 默认表格对齐输出
psql -U postgres -d mydb -c "SELECT * FROM users LIMIT 3;"
```

**单行写法：HTML 输出**
`psql -U <用户> -d <数据库> -c "<SQL>" -H`
```bash
# 输出 HTML 表格
psql -U postgres -d mydb -c "SELECT * FROM users;" -H
```

**单行写法：逗号分隔输出**
`psql -U <用户> -d <数据库> -c "<SQL>" -A -F ','`
```bash
# 无对齐逗号分隔输出
psql -U postgres -d mydb -c "SELECT * FROM users;" -A -F ','
```

**单行写法：制表符分隔输出**
`psql -U <用户> -d <数据库> -c "<SQL>" -A -F $'\t'`
```bash
# 制表符分隔便于复制到 Excel
psql -U postgres -d mydb -c "SELECT * FROM users;" -A -F $'\t'
```

**单行写法：静默输出无表头**
`psql -U <用户> -d <数据库> -c "<SQL>" -t -A`
```bash
# 仅输出数据无表头无对齐
psql -U postgres -d mydb -c "SELECT username FROM users;" -t -A
```

**单行写法：扩展显示**
`psql -U <用户> -d <数据库> -c "<SQL>" -x`
```bash
# 垂直显示每列一行
psql -U postgres -d mydb -c "SELECT * FROM users WHERE id = 1;" -x
```

---

## 交互式元命令

**单行写法：查看帮助**
`\?`
```sql
-- 查看 psql 元命令帮助
\?
```

**单行写法：查看 SQL 帮助**
`\h <命令>`
```sql
-- 查看指定 SQL 命令帮助
\h CREATE TABLE
```

**单行写法：退出**
`\q`
```sql
-- 退出 psql
\q
```

**单行写法：切换数据库**
`\c <数据库名>`
```sql
-- 切换到其他数据库
\c mydb
```

**单行写法：查看当前连接**
`\conninfo`
```sql
-- 查看当前连接信息
\conninfo
```

---

## 对象查看元命令

**单行写法：查看所有数据库**
`\l`
```sql
-- 列出所有数据库
\l
```

**单行写法：查看所有表**
`\dt`
```sql
-- 列出当前数据库所有表
\dt
```

**单行写法：查看指定模式表**
`\dt <模式名>.*`
```sql
-- 列出指定模式的所有表
\dt public.*
```

**单行写法：查看表结构**
`\d <表名>`
```sql
-- 查看表结构含列、索引、约束
\d users
```

**单行写法：查看表详细信息**
`\d+ <表名>`
```sql
-- 查看表详细信息含描述和存储
\d+ users
```

**单行写法：查看索引**
`\di`
```sql
-- 列出所有索引
\di
```

**单行写法：查看视图**
`\dv`
```sql
-- 列出所有视图
\dv
```

**单行写法：查看函数**
`\df`
```sql
-- 列出所有函数
\df
```

**单行写法：查看序列**
`\ds`
```sql
-- 列出所有序列
\ds
```

**单行写法：查看用户角色**
`\du`
```sql
-- 列出所有用户和角色
\du
```

**单行写法：查看模式**
`\dn`
```sql
-- 列出所有模式
\dn
```

**单行写法：查看扩展**
`\dx`
```sql
-- 列出已安装扩展
\dx
```

---

## 文件操作元命令

**单行写法：执行 SQL 文件**
`\i <文件路径>`
```sql
-- 执行外部 SQL 文件
\i /path/to/script.sql
```

**单行写法：输出到文件**
`\o <文件路径>`
```sql
-- 将后续查询结果输出到文件
\o /tmp/result.txt
```

**单行写法：停止输出到文件**
`\o`
```sql
-- 恢复标准输出
\o
```

**单行写法：编辑查询缓冲区**
`\e`
```sql
-- 使用编辑器编辑当前查询
\e
```

**单行写法：编辑指定文件**
`\e <文件路径>`
```sql
-- 编辑指定文件并执行
\e /tmp/query.sql
```

**单行写法：保存查询到文件**
`\w <文件路径>`
```sql
-- 将当前查询缓冲区保存到文件
\w /tmp/query.sql
```

---

## 交互式实用命令

**单行写法：清除屏幕**
`\! clear`
```sql
-- 清除终端屏幕
\! clear
```

**单行写法：执行系统命令**
`\! <系统命令>`
```sql
-- 执行系统 shell 命令
\! ls -la
```

**单行写法：设置变量**
`\set <变量名> <值>`
```sql
-- 设置 psql 变量
\set limit 10
```

**单行写法：使用变量**
`SELECT * FROM users LIMIT :limit;`
```sql
-- 在 SQL 中使用变量
SELECT * FROM users LIMIT :limit;
```

**单行写法：取消当前输入**
`\r`
```sql
-- 重置当前查询缓冲区
\r
```

**单行写法：查看执行时间**
`\timing`
```sql
-- 开启/关闭查询执行时间统计
\timing
```

---

## 备份恢复工具

**单行写法：导出数据库**
`pg_dump -U <用户> -d <数据库> > <文件>`
```bash
# 导出整个数据库
pg_dump -U postgres -d mydb > mydb_backup.sql
```

**单行写法：导出为自定义格式**
`pg_dump -U <用户> -d <数据库> -F c -f <文件>`
```bash
# 导出为自定义压缩格式
pg_dump -U postgres -d mydb -F c -f mydb.dump
```

**单行写法：仅导出表结构**
`pg_dump -U <用户> -d <数据库> -s > <文件>`
```bash
# 仅导出表结构不导出数据
pg_dump -U postgres -d mydb -s > schema.sql
```

**单行写法：仅导出数据**
`pg_dump -U <用户> -d <数据库> -a > <文件>`
```bash
# 仅导出数据不导出表结构
pg_dump -U postgres -d mydb -a > data.sql
```

**单行写法：导出指定表**
`pg_dump -U <用户> -d <数据库> -t <表名> > <文件>`
```bash
# 仅导出指定表
pg_dump -U postgres -d mydb -t users > users_backup.sql
```

**单行写法：从 SQL 文件恢复**
`psql -U <用户> -d <数据库> < <文件>`
```bash
# 从 SQL 文本文件恢复
psql -U postgres -d mydb < mydb_backup.sql
```

**单行写法：从自定义格式恢复**
`pg_restore -U <用户> -d <数据库> <文件>`
```bash
# 从自定义压缩格式恢复
pg_restore -U postgres -d mydb mydb.dump
```

**单行写法：导出所有数据库**
`pg_dumpall -U <用户> > <文件>`
```bash
# 导出所有数据库及全局对象
pg_dumpall -U postgres > all_backup.sql
```

---

## 服务管理工具

**单行写法：初始化数据库集群**
`initdb -D <数据目录>`
```bash
# 初始化新的数据库集群
initdb -D /var/lib/postgresql/data
```

**单行写法：启动服务**
`pg_ctl -D <数据目录> start`
```bash
# 启动 PostgreSQL 服务
pg_ctl -D /var/lib/postgresql/data start
```

**单行写法：停止服务**
`pg_ctl -D <数据目录> stop`
```bash
# 停止 PostgreSQL 服务
pg_ctl -D /var/lib/postgresql/data stop
```

**单行写法：重启服务**
`pg_ctl -D <数据目录> restart`
```bash
# 重启 PostgreSQL 服务
pg_ctl -D /var/lib/postgresql/data restart
```

**单行写法：查看服务状态**
`pg_ctl -D <数据目录> status`
```bash
# 查看服务运行状态
pg_ctl -D /var/lib/postgresql/data status
```

**单行写法：重载配置**
`pg_ctl -D <数据目录> reload`
```bash
# 重载配置文件不重启
pg_ctl -D /var/lib/postgresql/data reload
```

**单行写法：创建用户**
`createuser -U <管理员> <新用户名>`
```bash
# 创建新数据库用户
createuser -U postgres appuser
```

**单行写法：创建数据库**
`createdb -U <管理员> -O <所有者> <数据库名>`
```bash
# 创建数据库并指定所有者
createdb -U postgres -O appuser mydb
```

**单行写法：删除用户**
`dropuser -U <管理员> <用户名>`
```bash
# 删除数据库用户
dropuser -U postgres appuser
```

**单行写法：删除数据库**
`dropdb -U <管理员> <数据库名>`
```bash
# 删除数据库
dropdb -U postgres mydb
```

---

## 性能分析

**单行写法：分析查询计划**
`EXPLAIN SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 查看查询执行计划
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

**单行写法：分析并执行**
`EXPLAIN ANALYZE SELECT <列> FROM <表名> WHERE <条件>;`
```sql
-- 执行查询并显示实际耗时
EXPLAIN ANALYZE SELECT * FROM users WHERE status = 1;
```

**单行写法：分析含缓冲区**
`EXPLAIN (ANALYZE, BUFFERS) SELECT <列> FROM <表名>;`
```sql
-- 显示缓冲区使用情况
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM users WHERE id = 1;
```

**单行写法：查看活动连接**
`SELECT * FROM pg_stat_activity;`
```sql
-- 查看当前所有活动连接
SELECT pid, usename, datname, state, query FROM pg_stat_activity;
```

**单行写法：查看数据库大小**
`SELECT pg_size_pretty(pg_database_size('<库名>'));`
```sql
-- 查看数据库大小
SELECT pg_size_pretty(pg_database_size('mydb'));
```

**单行写法：查看表大小**
`SELECT pg_size_pretty(pg_total_relation_size('<表名>'));`
```sql
-- 查看表及其索引总大小
SELECT pg_size_pretty(pg_total_relation_size('users'));
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
| PostgreSQL 窗口函数 | 046-WindowFunction | 本文的并列主题 |
| PostgreSQL CTE 递归查询 | 047-CTE | 本文的并列主题 |
| PostgreSQL psql CLI 命令 | 048-PsqlCLI | 本文自身 |
| pg_dump 与 pg_restore 语法速查手册 | 049-PgDumpRestore | 本文的并列主题 |
| 数组类型操作 语法速查手册 | 050-ArrayType | 本文的并列主题 |
| 模式（Schema）管理 语法速查手册 | 051-SchemaManagement | 本文的并列主题 |
| 视图与物化视图 语法速查手册 | 052-ViewMaterializedView | 本文的并列主题 |
| LISTEN/NOTIFY 监听通知 语法速查手册 | 053-ListenNotify | 本文的并列主题 |
