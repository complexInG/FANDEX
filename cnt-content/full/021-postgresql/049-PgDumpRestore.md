---
order: 490
title: pg_dump 与 pg_restore 语法速查手册
module: postgresql

category: '021-postgresql'
difficulty: beginner
description: pg_dump 与 pg_restore 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## pg_dump 基本备份

**基本写法：备份单个数据库**
`pg_dump -U <用户名> -d <数据库名> -f <输出文件>`

```bash
# 备份 mydb 数据库到文件
pg_dump -U postgres -d mydb -f mydb_backup.sql
```

**基本写法：自定义压缩格式备份**
`pg_dump -U <用户名> -Fc -d <数据库名> -f <输出文件>.dump`

```bash
# 使用自定义压缩格式（支持选择性恢复，推荐）
pg_dump -U postgres -Fc -d mydb -f mydb.dump
```

**基本写法：目录格式备份（支持并行）**
`pg_dump -U <用户名> -Fd -d <数据库名> -f <输出目录>`

```bash
# 目录格式（每个表一个文件，支持并行恢复）
pg_dump -U postgres -Fd -d mydb -f mydb_dir/
```

**基本写法：并行备份**
`pg_dump -U <用户名> -Fd -j <并行数> -d <数据库名> -f <输出目录>`

```bash
# 4 个并行进程加速备份
pg_dump -U postgres -Fd -j 4 -d mydb -f mydb_dir/
```

---

## 选择性备份

**基本写法：仅备份指定表**
`pg_dump -U <用户名> -d <库名> -t <表名> [-t <表2>] -f <输出文件>`

```bash
# 仅备份 users 和 orders 表
pg_dump -U postgres -d mydb -t users -t orders -f tables_backup.sql
```

**基本写法：排除指定表**
`pg_dump -U <用户名> -d <库名> -T <表名> -f <输出文件>`

```bash
# 备份除 logs 表外的所有表
pg_dump -U postgres -d mydb -T logs -f mydb_no_logs.sql
```

**基本写法：仅备份数据/仅结构**
`pg_dump -U <用户名> -d <库名> --data-only -f <输出文件>`

```bash
# 仅备份数据（不含结构）
pg_dump -U postgres -d mydb --data-only -f mydb_data.sql
# 仅备份结构（不含数据）
pg_dump -U postgres -d mydb --schema-only -f mydb_schema.sql
```

---

## 全库与模式备份

**基本写法：备份所有数据库**
`pg_dumpall -U <用户名> -f <输出文件>`

```bash
# 备份所有数据库（含角色与表空间定义）
pg_dumpall -U postgres -f all_db_backup.sql
# 仅备份全局对象（角色、表空间）
pg_dumpall -U postgres --globals-only -f globals.sql
```

**基本写法：备份指定模式**
`pg_dump -U <用户名> -d <库名> -n <模式名> -f <输出文件>`

```bash
# 仅备份 business 模式
pg_dump -U postgres -d mydb -n business -f business_schema.sql
```

---

## pg_restore 恢复

**基本写法：从自定义格式恢复**
`pg_restore -U <用户名> -d <数据库名> <备份文件>.dump`

```bash
# 恢复自定义格式备份到指定数据库
pg_restore -U postgres -d mydb mydb.dump
```

**基本写法：从 SQL 文本恢复**
`psql -U <用户名> -d <数据库名> -f <备份文件>.sql`

```bash
# 恢复纯文本 SQL 备份
psql -U postgres -d mydb -f mydb_backup.sql
```

**基本写法：并行恢复**
`pg_restore -U <用户名> -d <库名> -j <并行数> <备份文件>.dump`

```bash
# 4 个并行进程加速恢复
pg_restore -U postgres -d mydb -j 4 mydb.dump
```

**基本写法：仅恢复结构/数据**
`pg_restore -U <用户名> -d <库名> --schema-only <备份文件>.dump`

```bash
# 仅恢复结构
pg_restore -U postgres -d mydb --schema-only mydb.dump
# 仅恢复数据
pg_restore -U postgres -d mydb --data-only mydb.dump
```

---

## 增量备份（17 新特性）

**基本写法：pg_basebackup 增量备份**
`pg_basebackup -U <用户名> -D <目录> -Fp -Xs -P --incremental <基础备份manifest路径>`

```bash
# PostgreSQL 17 増量基础备份
pg_basebackup -U postgres -D /backup/incr -Fp -Xs -P -c fast
```

**基本写法：pg_combinebackup 合并备份**
`pg_combinebackup <基础备份目录> <增量备份目录> -o <合并输出目录>`

```bash
# PostgreSQL 17 合并基础与增量备份
pg_combinebackup /backup/base /backup/incr -o /backup/combined
```

---

## 选项速查

**基本写法：连接选项**
`pg_dump -h <主机> -p <端口> -U <用户> -d <数据库>`

```bash
# 远程数据库备份
pg_dump -h 192.168.1.100 -p 5432 -U admin -d mydb -f remote.sql
```

**基本写法：压缩级别**
`pg_dump -U <用户> -Fc -Z <级别> -d <库名> -f <输出文件>`

```bash
# 指定压缩级别 0-9（9 最高压缩率）
pg_dump -U postgres -Fc -Z 6 -d mydb -f mydb.dump
```

---

## 延伸阅读
PostgreSQL 窗口函数，见 021-postgresql 模块文档。
PostgreSQL 递归查询，见 021-postgresql 模块相关文档。
SQL 基础，见 019-sql 模块。
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
