---
order: 83
title: 组复制
module: mysql
category: MySQL
difficulty: advanced
description: 'MySQL组复制Group Replication：单主/多主模式、Paxos协议、故障检测与自动切换'
author: fanquanpp
updated: '2026-08-01'
related:
  - mysql/全局事务标识
  - mysql/并行复制
  - mysql/InnoDB集群
  - mysql/分区表
prerequisites:
  - mysql/语法速查
---

## 1. 组复制概述

MySQL Group Replication（MGR）基于 Paxos 协议实现多主一致性复制，提供自动故障检测和切换。

### 1.1 模式

| 模式     | 写入点   | 适用场景   |
| -------- | -------- | ---------- |
| 单主模式 | 仅主节点 | 大多数场景 |
| 多主模式 | 所有节点 | 写分散场景 |

## 2. 配置

```ini
[mysqld]
server-id = 1
gtid-mode = ON
enforce-gtid-consistency = ON
log-bin = mysql-bin
binlog-format = ROW
master-info-repository = TABLE
relay-log-info-repository = TABLE

# 组复制配置
plugin_load_add = 'group_replication.so'
group_replication_group_name = '3E11FA47-71CA-11E1-9E33-C80AA9429562'
group_replication_start_on_boot = OFF
group_replication_local_address = 'node1:33061'
group_replication_group_seeds = 'node1:33061,node2:33061,node3:33061'
group_replication_single_primary_mode = ON
```

## 3. 启动组复制

```sql
-- 首个节点（引导组）
SET SQL_LOG_BIN = 0;
CREATE USER 'repl'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
SET SQL_LOG_BIN = 1;
CHANGE MASTER TO MASTER_USER='repl', MASTER_PASSWORD='password' FOR CHANNEL 'group_replication_recovery';

SET GLOBAL group_replication_bootstrap_group = ON;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group = OFF;

-- 其他节点加入
START GROUP_REPLICATION;

-- 查看成员
SELECT * FROM performance_schema.replication_group_members;
```

## 4. 故障检测

```sql
-- 自动检测故障节点
-- 多数节点同意后剔除故障节点
-- 单主模式下自动选举新主

-- 查看当前主节点
SELECT * FROM performance_schema.replication_group_members
WHERE MEMBER_ROLE = 'PRIMARY';
```

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
