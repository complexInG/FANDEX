---
order: 430
title: InnoDB-Cluster
module: 'mysql'
category: 数据库
difficulty: advanced
description: MySQL InnoDB Cluster与InnoDB ClusterSet：MySQL Shell、MGR、MySQL Router集成高可用方案
author: fanquanpp
updated: '2026-08-01'
related:
  - 'mysql/041-ParallelReplication'
  - 'mysql/042-GroupReplication'
  - 'mysql/044-PartitionedTable'
  - 'mysql/045-ShardingMiddleware'
prerequisites:
  - 'mysql/085-View'
---


## 1. InnoDB Cluster 概述

InnoDB Cluster 是 MySQL 官方的高可用方案，整合三个组件：

| 组件                             | 作用               |
| -------------------------------- | ------------------ |
| MySQL Server + Group Replication | 数据复制与一致性   |
| MySQL Router                     | 读写路由与故障转移 |
| MySQL Shell                      | 管理与配置工具     |

## 2. 部署

### 2.1 使用 MySQL Shell 创建集群

```javascript
// 连接主节点
mysqlsh root@node1:3306

// 创建集群
var cluster = dba.createCluster('myCluster');

// 添加实例
cluster.addInstance('root@node2:3306');
cluster.addInstance('root@node3:3306');

// 查看集群状态
cluster.status();
```

### 2.2 配置 MySQL Router

```bash
# 引导 Router
mysqlrouter --bootstrap root@node1:3306 --user=mysqlrouter

# 启动 Router
systemctl start mysqlrouter

# 应用连接 Router
# 读写端口：6446（指向主节点）
# 只读端口：6447（指向从节点）
mysql -h 127.0.0.1 -P 6446 -u root -p  # 读写
mysql -h 127.0.0.1 -P 6447 -u root -p  # 只读
```

## 3. InnoDB ClusterSet

### 3.1 概述

ClusterSet 将多个 InnoDB Cluster 连接起来，提供跨数据中心的高可用和灾难恢复。

```javascript
// 创建 ClusterSet
var clusterset = dba.createClusterSet('myClusterSet');

// 添加副本集群
clusterset.createReplicaCluster('root@replica-node1:3306', 'replicaCluster');

// 查看状态
clusterset.status();
```

### 3.2 故障切换

```javascript
// 强制切换到副本集群
clusterset.forcePrimaryCluster('replicaCluster');
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
