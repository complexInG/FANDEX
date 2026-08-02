---
order: 81
title: GTID
module: mysql
category: MySQL
difficulty: advanced
description: MySQL全局事务标识符GTID：原理、配置、基于GTID的复制与故障切换
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/主从复制
  - mysql/进阶查询与多表操作
  - mysql/并行复制
  - mysql/组复制
prerequisites:
  - mysql/语法速查
---
## 1. GTID 概述

全局事务标识符（Global Transaction Identifier，GTID）为每个事务分配唯一标识，简化复制管理。

### 1.1 GTID 格式

$$
\text{GTID} = \text{server\_uuid}:\text{transaction\_id}
$$

```
3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
```

## 2. 配置

```ini
[mysqld]
gtid-mode = ON
enforce-gtid-consistency = ON
log-bin = mysql-bin
binlog-format = ROW
server-id = 1
```

## 3. 基于GTID的复制

```sql
-- 从库配置（无需指定 binlog 位置）
CHANGE MASTER TO
    MASTER_HOST = 'master-ip',
    MASTER_USER = 'repl',
    MASTER_PASSWORD = 'password',
    MASTER_AUTO_POSITION = 1;  -- 使用 GTID 自动定位

START SLAVE;
```

## 4. GTID 运维

```sql
-- 查看已执行的 GTID
SHOW MASTER STATUS;
-- Executed_Gtid_Set: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100

-- 查看从库已执行的 GTID
SHOW SLAVE STATUS\G
-- Retrieved_Gtid_Set: ...
-- Executed_Gtid_Set: ...

-- 跳过有问题的 GTID 事务
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN;
COMMIT;
SET GTID_NEXT = AUTOMATIC;
START SLAVE;
```

## 5. GTID 优势

- 无需手动定位 binlog 位置
- 故障切换更简单
- 可验证主从数据一致性
- 支持多源复制
## GTID 概念与格式

**基本写法：标准 GTID 格式**
`<server_uuid>:<事务序号>`

```sql
-- 标准 GTID 格式示例
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5
-- 表示该 UUID 的事务 1 到 5

-- 8.4 Tagged GTID 格式（带标签）
-- 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-5:delete_logs
```

**基本写法：查看服务器 UUID**
`SHOW VARIABLES LIKE 'server_uuid';`

```sql
-- 查看当前服务器 UUID
SHOW VARIABLES LIKE 'server_uuid';
```

---

## GTID 开启与配置

**基本写法：查看 GTID 状态**
`SHOW VARIABLES LIKE 'gtid_mode';`

```sql
-- 查看 GTID 是否启用
SHOW VARIABLES LIKE 'gtid_mode';
SHOW VARIABLES LIKE 'enforce_gtid_consistency';
```

**基本写法：在线开启 GTID（分步）**
`SET GLOBAL enforce_gtid_consistency = WARN;`

```sql
-- 第一步：开启一致性警告，观察业务无警告后继续
SET GLOBAL enforce_gtid_consistency = WARN;
-- 第二步：开启一致性强制
SET GLOBAL enforce_gtid_consistency = ON;
-- 第三步：GTID 模式 OFF_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = OFF_PERMISSIVE;
-- 第四步：ON_PERMISSIVE（允许混合）
SET GLOBAL gtid_mode = ON_PERMISSIVE;
-- 等待所有匿名事务消费完毕
SHOW STATUS LIKE 'Ongoing_anonymous_transaction_count';
-- 第五步：正式开启
SET GLOBAL gtid_mode = ON;
```

**基本写法：配置文件持久开启**
`gtid_mode = ON`

```ini
# my.cnf 持久配置
[mysqld]
gtid_mode = ON
enforce_gtid_consistency = ON
log_slave_updates = ON        # 8.0.10+ 默认 ON，副本需记录更新到 binlog
log_bin = mysql-bin
```

---

## GTID 查询

**基本写法：查看已执行 GTID**
`SELECT @@GLOBAL.gtid_executed;`

```sql
-- 查看当前服务器已执行的 GTID 集合
SELECT @@GLOBAL.gtid_executed;
-- 示例输出: 3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100
```

**基本写法：查看已清除 GTID**
`SELECT @@GLOBAL.gtid_purged;`

```sql
-- 查看已被清除（不可用）的 GTID 集合
SELECT @@GLOBAL.gtid_purged;
```

**基本写法：查看 GTID 执行状态**
`SHOW MASTER STATUS;`

```sql
-- 查看当前二进制日志位置与已执行 GTID（8.4 用 SHOW BINARY LOG STATUS）
SHOW BINARY LOG STATUS\G
-- 输出包含 Executed_Gtid_Set 字段
```

**基本写法：performance_schema 查询 GTID**
`SELECT * FROM performance_schema.replication_connection_status;`

```sql
-- 查看复制连接接收到的 GTID
SELECT thread_id, service_state, received_transaction_set
FROM performance_schema.replication_connection_status;
```

---

## GTID 复制配置

**基本写法：基于 GTID 建立复制**
`CHANGE REPLICATION SOURCE TO SOURCE_HOST='<主机>', SOURCE_USER='<用户>', SOURCE_PASSWORD='<密码>', SOURCE_AUTO_POSITION = 1;`

```sql
-- GTID 自动定位复制（无需指定日志文件和位置）
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='192.168.1.100',
  SOURCE_PORT=3306,
  SOURCE_USER='repl',
  SOURCE_PASSWORD='ReplPass123!',
  SOURCE_AUTO_POSITION = 1,
  GET_SOURCE_PUBLIC_KEY = 1;
START REPLICA;
```

**基本写法：跳过指定 GTID 事务**
`SET GTID_NEXT = '<GTID>';`

```sql
-- 跳过单个 GTID 事务（解决复制错误）
STOP REPLICA;
SET GTID_NEXT = '3E11FA47-71CA-11E1-9E33-C80AA9429562:101';
BEGIN; COMMIT;
SET GTID_NEXT = AUTOMATIC;
START REPLICA;
```

**基本写法：设置已清除 GTID（空库初始化）**
`SET GLOBAL gtid_purged = '<GTID集合>';`

```sql
-- 从备份恢复空库时设置已清除的 GTID
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100';
```

---

## 8.4 Tagged GTID

**基本写法：为事务打标签**
`SET TRANSACTION GTID_TAG = '<标签名>';`

```sql
-- MySQL 8.4 新特性：为事务分配标签（最多 33 字符）
-- 需 TRANSACTION_GTID_TAG 权限
SET TRANSACTION GTID_TAG = 'delete_logs';
DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：会话级设置标签**
`SET SESSION gtid_next_tag = '<标签名>';`

```sql
-- 当前会话所有事务都打上标签
SET SESSION gtid_next_tag = 'batch_import';
INSERT INTO sales VALUES (...);
```

**基本写法：跳过指定标签的事务**
`SET GLOBAL gtid_purged = '<UUID>:<区间>:<标签>';`

```sql
-- 副本端跳过带标签的事务（8.4 新增三参数 gtid_purged）
-- 格式: SET GLOBAL gtid_purged=<group_name>, <gtid_set>, <tag>
SET GLOBAL gtid_purged = '3E11FA47-71CA-11E1-9E33-C80AA9429562:1-100:delete_logs';
```

**基本写法：查看带标签的 GTID**
`SELECT * FROM performance_schema.replication_applier_status_by_worker;`

```sql
-- 查看副本应用事务时是否包含标签信息
SELECT worker_id, last_applied_transaction, last_applied_transaction_original_seqno
FROM performance_schema.replication_applier_status_by_worker;
```

---

## GTID 复制错误处理

**基本写法：查看复制错误**
`SHOW REPLICA STATUS\G`

```sql
-- 查看复制错误信息
SHOW REPLICA STATUS\G
-- 关注 Last_Error 与 Last_SQL_Error 字段
```

**基本写法：基于 GTID 自动跳过错误**
`SET GLOBAL slave_skip_errors = '<错误码>';`

```sql
-- 不推荐：跳过指定错误码（破坏一致性）
-- 推荐：使用 GTID_NEXT 手动跳过或 sql_slave_skip_counter（仅非 GTID）
```

**基本写法：重置 GTID 执行状态**
`RESET MASTER;`

```sql
-- 清空所有 binlog 并重置 gtid_executed（危险！仅初始化时使用）
RESET MASTER;
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
