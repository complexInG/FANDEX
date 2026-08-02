---
order: 450
title: 分库分表中间件
module: 'mysql'
category: 数据库
difficulty: advanced
description: MySQL分库分表中间件：ShardingSphere、Vitess、MyCat的架构、分片策略与适用场景
author: fanquanpp
updated: '2026-08-01'
related:
  - 'mysql/044-PartitionedTable'
  - 'mysql/046-AccountPermissionManagement'
  - 'mysql/047-SSLEncryption'
prerequisites:
  - 'mysql/085-View'
---


## 1. 分库分表概述

当单表数据量超过千万级，单库性能瓶颈时，需要分库分表。

### 1.1 拆分策略

| 策略     | 说明                       | 适用场景     |
| -------- | -------------------------- | ------------ |
| 垂直分库 | 按业务拆分到不同数据库     | 微服务架构   |
| 垂直分表 | 将大表拆分为多张小表       | 列数过多的表 |
| 水平分库 | 同一表数据分布到多个数据库 | 数据量大的表 |
| 水平分表 | 同一库中将表拆分为多张子表 | 数据量大的表 |

## 2. 分片键设计

```sql
-- 分片键选择原则：
-- 1. 高选择性（避免数据倾斜）
-- 2. 查询高频使用
-- 3. 尽量避免跨分片查询

-- 常见分片策略：
-- user_id % 4 → 4个分片
-- HASH(order_id) → 均匀分布
-- RANGE(created_at) → 按时间分片
```

## 3. ShardingSphere

### 3.1 架构

```
ShardingSphere-JDBC：轻量级Java框架，应用内嵌入
ShardingSphere-Proxy：独立代理服务
ShardingSphere-Sidecar：云原生方案
```

### 3.2 分片配置

```yaml
rules:
  - !SHARDING
    tables:
      orders:
        actualDataNodes: ds_${0..3}.orders_${0..7}
        tableStrategy:
          standard:
            shardingColumn: user_id
            shardingAlgorithmName: orders_mod
        keyGenerateStrategy:
          column: id
            keyGeneratorName: snowflake
    shardingAlgorithms:
      orders_mod:
        type: MOD
        props:
          sharding-count: 8
```

## 4. Vitess

```sql
-- Vitess：YouTube 开源的 MySQL 集群管理工具
-- 基于 VReplication 实现分片迁移
-- 支持在线分片拆分和合并

-- 创建分片
vtctlclient CreateShard -keyspace commerce -shard '-'
vtctlclient CreateShard -keyspace commerce -shard '-80'
vtctlclient CreateShard -keyspace commerce -shard '80-'
```

## 5. 跨分片查询

```sql
-- 尽量避免跨分片 JOIN 和聚合
-- 使用冗余字段减少跨分片查询
-- 使用全局表（广播表）存储维度数据
-- 使用 ER 分片将关联表放在同一分片
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
