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

## 延伸阅读
Redis 数据结构详解，见 022-redis 模块文档。
Redis 持久化与集群，见 022-redis 模块相关文档。
MySQL 与 Redis 缓存架构，见 020-mysql 模块。
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
