---
order: 54
title: 向量集
module: redis
category: Redis
difficulty: advanced
description: 'Redis向量集Vector Set：高维向量存储、近似最近邻搜索与AI嵌入应用'
author: fanquanpp
updated: '2026-08-01'
related:
  - redis/地理空间
  - redis/流
  - redis/RDB快照持久化
  - redis/AOF日志持久化
prerequisites:
  - redis/概述与核心数据结构
---

## 1. Vector Set 概述

Redis 8.0 引入 Vector Set 数据类型，支持高维向量的存储和近似最近邻（ANN）搜索。

## 2. 基本操作

```redis
-- 创建向量集并添加向量
VADD myvectors VALUES 3 0.1 0.2 0.3 element1
VADD myvectors VALUES 3 0.4 0.5 0.6 element2
VADD myvectors VALUES 3 0.7 0.8 0.9 element3

-- 设置向量属性
VADD myvectors VALUES 3 0.1 0.2 0.3 element1 SET name "Alice" age 30

-- 获取向量
VEMB myvectors element1

-- 获取向量维度
VDIM myvectors
```

## 3. 近似最近邻搜索

```redis
-- 搜索最相似的向量
VSEARCH myvectors VALUES 3 0.15 0.25 0.35 COUNT 5

-- 基于元素搜索相似元素
VSIM myvectors element1 COUNT 5

-- 带过滤条件搜索
VSEARCH myvectors VALUES 3 0.15 0.25 0.35 FILTER "age >= 25" COUNT 5

-- 返回属性
VSIM myvectors element1 WITHATTRIBUTES COUNT 5
```

## 4. 配置

```redis
-- 设置量化方式
VADD myvectors VALUES 3 0.1 0.2 0.3 element1 QUANTIZATION NO  -- 不量化
VADD myvectors VALUES 3 0.1 0.2 0.3 element1 QUANTIZATION Q8  -- 8位量化

-- 设置链接数（HNSW参数）
VADD myvectors VALUES 3 0.1 0.2 0.3 element1 M 64

-- 设置EF运行时参数
VSEARCH myvectors VALUES 3 0.15 0.25 0.35 EF 200 COUNT 5
```

## 5. 应用场景

```redis
-- 语义搜索
VADD docs VALUES 1536 <embedding> doc:1 SET title "Redis Guide"
VSEARCH docs VALUES 1536 <query_embedding> COUNT 10

-- 推荐系统
VADD products VALUES 128 <embedding> product:1 SET category "electronics"
VSIM products product:42 COUNT 10 FILTER "category == 'electronics'"
```

## 参考文献

Redis 官方文档：https://redis.io/docs/latest/
Redis 命令参考：https://redis.io/docs/latest/commands/
Redis 中文资料：https://redis.com.cn/
Redisson 文档：https://redisson.org/

## 延伸阅读

Redis 数据结构详解，见 022-redis 模块文档。
Redis 持久化与集群，见 022-redis 模块相关文档。
MySQL 与 Redis 缓存架构，见 020-mysql 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Redis 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 缓存一致性深度

Cache Aside：读未命中查 DB 回填；写先 DB 后删缓存；删除失败用消息队列补偿。
延迟双删：更新 DB 后删缓存，等待短暂延迟再删一次，处理并发读写窗口。
读写锁与版本号：缓存携带版本，更新时比较版本，失败重试。
强一致场景：不要依赖缓存，直接读 DB；缓存用于可容忍最终一致的数据。

### 13.2 Redis Cluster 原理

16384 个槽分布在主节点，键经 CRC16 % 16384 定位；客户端 MOVED/ASK 重定向。
主从复制：每个主节点挂从节点；主故障由从节点提升（cluster 自动 failover）。
多键操作：同一事务/管道中的键必须同槽（hash tag {user1001}）。
扩缩容：槽迁移在线进行，客户端感知重定向；规划容量避免热点槽。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与核心数据结构 | 001-OverviewCoreDataStructure | 本文的前置基础 |
| 持久化与模块 | 002-PersistenceModule | 本文的并列主题 |
| 集群与高可用 | 003-ClusterHA | 本文的并列主题 |
| 缓存策略与高级特性 | 004-CacheStrategyAdvancedFeature | 本文的并列主题 |
| 位图 | 005-BitGraph | 本文的并列主题 |
| 基数统计 | 006-NumberStats | 本文的并列主题 |
| 地理空间 | 007-GeoSpatial | 本文的并列主题 |
| 流 | 008-Stream | 本文的并列主题 |
| 向量集 | 009-VectorSet | 本文自身 |
| RDB快照持久化 | 010-RDBSnapshotPersistence | 本文的并列主题 |
| AOF日志持久化 | 011-AOFLogPersistence | 本文的并列主题 |
| 混合持久化 | 012-MixedPersistence | 本文的并列主题 |
| 无盘复制 | 013-DisklessReplication | 本文的并列主题 |
| 模块系统 | 014-ModuleSystem | 本文的并列主题 |
| 字符串SDS结构 | 015-StringSDSStructure | 本文的并列主题 |
| 跳表与有序集合 | 016-SkipListAndSortedSet | 本文的并列主题 |
| 主从复制缓冲区 | 017-ReplicationBuffer | 本文的并列主题 |
| 哨兵选举 | 018-SentinelElection | 本文的并列主题 |
| Redis-Cluster哈希槽 | 019-RedisClusterHashSlot | 本文的并列主题 |
| 管道与事务原子性 | 020-PipeTransactionAtomic | 本文的并列主题 |
| Lua脚本原子执行 | 021-LuaScriptAtomicExecution | 本文的并列主题 |
| 缓存穿透击穿雪崩 | 022-CachePenetrationBreakdownAvalanche | 本文的并列主题 |
| 内存淘汰策略 | 023-MemoryEvictionPolicy | 本文的并列主题 |
| Redis Hash 命令速查 | 024-HashCommand | 本文的并列主题 |
| Redis List/Set/ZSet 命令 | 025-ListSetZSetCommand | 本文的并列主题 |
| Redis 发布订阅命令 | 026-PubSubCommand | 本文的并列主题 |
| Redis Key 管理与过期命令速查手册 | 027-KeyManagement | 本文的并列主题 |
| Redis 安全与 ACL 命令速查手册 | 028-ACL | 本文的安全延伸 |
| Redis 7.0+ 新特性命令速查手册 | 029-NewFeatures7 | 本文的并列主题 |
