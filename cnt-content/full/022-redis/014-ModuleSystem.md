---
order: 59
title: 模块系统
module: redis
category: Redis
difficulty: advanced
description: Redis模块系统：RedisJSON、RedisTimeSeries、RediSearch、RedisBloom等模块原理与使用
author: fanquanpp
updated: '2026-08-01'
related:
  - redis/混合持久化
  - redis/无盘复制
  - redis/字符串SDS结构
  - redis/跳表与有序集合
prerequisites:
  - redis/概述与核心数据结构
---

## 1. 模块系统概述

Redis 模块系统是 Redis 4.0 引入的扩展机制，允许开发者使用 C 语言编写自定义模块，为 Redis 添加新的数据类型和命令，而无需修改 Redis 核心代码。

**核心特性**：

- **自定义数据类型**：注册新的数据类型及编码方式
- **自定义命令**：添加新的 Redis 命令
- **钩子机制**：拦截 Redis 事件（如键过期、命令执行）
- **线程安全**：支持后台线程执行耗时操作
- **动态加载**：运行时加载/卸载模块，无需重启

### 1.1 模块加载方式

```redis
# redis.conf 配置
loadmodule /path/to/module.so

# 运行时加载
MODULE LOAD /path/to/module.so

# 查看已加载模块
MODULE LIST

# 卸载模块
MODULE UNLOAD module_name
```

## 2. RedisJSON

RedisJSON 是 Redis 的 JSON 数据类型模块，提供完整的 JSON 操作能力。

### 2.1 核心特性

- 原生 JSON 数据类型，支持嵌套结构
- JSONPath 语法查询和修改
- 原子性操作，无需读取-修改-写入
- 支持 JSON Schema 验证

### 2.2 基本操作

```redis
# 存储 JSON
JSON.SET user:1 $ '{"name":"张三","age":30,"address":{"city":"北京"},"tags":["dev","redis"]}'

# 获取整个 JSON
JSON.GET user:1

# 获取指定路径
JSON.GET user:1 $.name
JSON.GET user:1 $.address.city

# 修改字段
JSON.SET user:1 $.age 31

# 追加数组元素
JSON.ARRAPPEND user:1 $.tags '"python"'

# 数值递增
JSON.NUMINCRBY user:1 $.age 1

# 删除字段
JSON.DEL user:1 $.tags

# 查询类型
JSON.TYPE user:1 $.name
```

### 2.3 JSONPath 语法

```redis
# 根节点
JSON.GET user:1 $

# 子节点
JSON.GET user:1 $.name

# 递归下降
JSON.GET user:1 $..city

# 数组索引
JSON.GET user:1 $.tags[0]

# 数组切片
JSON.GET user:1 $.tags[0:2]

# 过滤表达式
JSON.GET users $[?(@.age>25)].name
```

### 2.4 性能优势

RedisJSON 相比传统 String 存储 JSON 的优势：

| 操作         | String + 序列化                | RedisJSON    |
| ------------ | ------------------------------ | ------------ |
| 修改单个字段 | 读取→反序列化→修改→序列化→写入 | 直接修改     |
| 网络传输     | 传输完整 JSON                  | 仅传输结果   |
| 原子性       | 需要事务/MULTI                 | 原生原子操作 |
| 内存效率     | 重复存储完整 JSON              | 共享不变部分 |

## 3. RediSearch

RediSearch 是 Redis 的全文搜索和二级索引模块。

### 3.1 创建索引

```redis
# 创建索引
FT.CREATE idx:products
  ON HASH
  PREFIX 1 product:
  SCHEMA
    title TEXT WEIGHT 5.0
    description TEXT
    price NUMERIC SORTABLE
    category TAG
    created_at NUMERIC SORTABLE

# 创建 JSON 索引
FT.CREATE idx:users
  ON JSON
  PREFIX 1 user:
  SCHEMA
    $.name AS name TEXT
    $.age AS age NUMERIC
    $.address.city AS city TAG
```

### 3.2 搜索操作

```redis
# 全文搜索
FT.SEARCH idx:products "redis search"

# 精确匹配
FT.SEARCH idx:products "@category:{electronics}"

# 数值范围
FT.SEARCH idx:products "@price:[100 500]"

# 组合查询
FT.SEARCH idx:products "redis @price:[0 100] @category:{book}"

# 模糊搜索
FT.SEARCH idx:products "%%redis%%"

# 前缀搜索
FT.SEARCH idx:products "redi*"
```

### 3.3 聚合查询

```redis
# 按类别分组统计
FT.AGGREGATE idx:products "*"
  GROUPBY 1 @category
  REDUCE COUNT 0 AS count
  SORTBY 2 @count DESC

# 价格统计
FT.AGGREGATE idx:products "@category:{electronics}"
  GROUPBY 1 @category
  REDUCE AVG 1 @price AS avg_price
  REDUCE MIN 1 @price AS min_price
  REDUCE MAX 1 @price AS max_price
```

### 3.4 中文搜索

```redis
# 创建支持中文的索引
FT.CREATE idx:articles
  ON HASH
  PREFIX 1 article:
  SCHEMA
    title TEXT PHONETIC zh
    content TEXT PHONETIC zh

# 中文搜索
FT.SEARCH idx:articles "分布式系统"
```

## 4. RedisTimeSeries

RedisTimeSeries 是 Redis 的时间序列数据模块，专为 IoT 监控和指标收集设计。

### 4.1 基本操作

```redis
# 创建时间序列
TS.CREATE temperature:device1 RETENTION 86400000 LABELS device_id 1 location beijing

# 添加数据点
TS.ADD temperature:device1 * 25.5
TS.ADD temperature:device1 1640995200000 23.1

# 批量添加
TS.MADD temperature:device1 1640995200000 23.1 temperature:device1 1640995260000 24.5 temperature:device1 1640995320000 25.0

# 查询范围
TS.RANGE temperature:device1 - + AGGREGATION avg 60000

# 按标签查询
TS.MRANGE - + WITHLABELS FILTER device_id=1
```

### 4.2 降采样规则

```redis
# 创建降采样规则：每分钟平均值，保留 30 天
TS.CREATE temperature:device1:1min RETENTION 2592000000
TS.CREATERULE temperature:device1 temperature:device1:1min AGGREGATION avg 60000

# 支持的聚合函数
# avg, sum, min, max, range, count, first, last, std.p, std.s, var.p, var.s, twa
```

### 4.3 标签与过滤

```redis
# 创建带标签的时间序列
TS.CREATE cpu:host1 RETENTION 86400000 LABELS hostname host1 region us-east metric cpu
TS.CREATE cpu:host2 RETENTION 86400000 LABELS hostname host2 region us-west metric cpu

# 按标签过滤查询
TS.MRANGE - + FILTER metric=cpu
TS.MRANGE - + FILTER region=us-east metric=cpu

# 标签过滤支持
# = 等于, != 不等于, () 属于, ~= 正则匹配
```

## 5. RedisBloom

RedisBloom 提供概率数据结构：布隆过滤器、布谷鸟过滤器、计数-最小草图、Top-K。

### 5.1 布隆过滤器（Bloom Filter）

```redis
# 创建布隆过滤器
BF.CREATE emails FILTER 0.01 ERROR RATE 1000000 CAPACITY

# 添加元素
BF.ADD emails "user@example.com"

# 批量添加
BF.MADD emails "a@test.com" "b@test.com" "c@test.com"

# 检查是否存在
BF.EXISTS emails "user@example.com"    # 返回 1（可能存在）
BF.EXISTS emails "unknown@test.com"    # 返回 0（一定不存在）

# 误判率计算
# 误判率 p ≈ (1 - e^(-kn/m))^k
# 其中 n=元素数, m=位数组大小, k=哈希函数数
```

### 5.2 布谷鸟过滤器（Cuckoo Filter）

```redis
# 创建布谷鸟过滤器
CF.CREATE usernames CAPACITY 1000000

# 添加元素
CF.ADD usernames "alice"

# 检查存在
CF.EXISTS usernames "alice"

# 删除元素（布隆过滤器不支持，布谷鸟支持）
CF.DEL usernames "alice"
```

### 5.3 Count-Min Sketch

```redis
# 创建
CMS.CREATE pageviews 2000 7

# 增加计数
CMS.INCRBY pageviews homepage 5 about 3

# 查询计数
CMS.QUERY pageviews homepage
```

### 5.4 Top-K

```redis
# 创建
TOPK.CREATE trending 10

# 增加计数
TOPK.INCRBY trending redis 5 python 3 java 2 go 4

# 查询 Top-K
TOPK.LIST trending

# 查询元素排名
TOPK.QUERY trending redis
```

## 6. RedisCell

RedisCell 提供分布式限流功能，基于令牌桶算法：

```redis
# 限流：每秒最多 10 次请求
CL.THROTTLE api:limit 10 10 1

# 返回值
# 1) 0          # 是否被限流（0=允许，1=限流）
# 2) 11         # 令牌桶容量
# 3) 10         # 剩余令牌数
# 4) -1         # 需要等待的毫秒数（-1 表示无需等待）
# 5) 0          # 下次补充令牌的毫秒数
```

## 7. 其他常用模块

### 7.1 RedisGraph（已弃用）

Redis Graph 模块已在 Redis 7.2 中弃用，建议使用 Redis + 外部图数据库方案。

### 7.2 RedisAI

```redis
# 加载模型
AI.MODELSET my_model TF CPU INPUTS 2 input1 input2 OUTPUTS 1 output BLOB <model_data>

# 执行推理
AI.TENSORSET input1 FLOAT 1 2 VALUES 1.0 2.0
AI.TENSORSET input2 FLOAT 1 2 VALUES 3.0 4.0
AI.MODELEXECUTE my_model INPUTS 2 input1 input2 OUTPUTS 1 output
AI.TENSORGET output VALUES
```

### 7.3 redis-cell

基于滑动窗口的限流模块：

```redis
CL.THROTTLE my_limit 100 400 60 1
# 参数：key, max_burst, count_per_period, period, quantity
```

## 8. 模块开发基础

### 8.1 最简模块示例

```c
#include "redismodule.h"

int HelloCommand(RedisModuleCtx *ctx, RedisModuleString **argv, int argc) {
    RedisModule_ReplyWithSimpleString(ctx, "Hello, Module!");
    return REDISMODULE_OK;
}

int RedisModule_OnLoad(RedisModuleCtx *ctx) {
    if (RedisModule_Init(ctx, "mymodule", 1, REDISMODULE_APIVER_1) == REDISMODULE_ERR)
        return REDISMODULE_ERR;

    if (RedisModule_CreateCommand(ctx, "mymodule.hello", HelloCommand,
        "readonly", 0, 0, 0) == REDISMODULE_ERR)
        return REDISMODULE_ERR;

    return REDISMODULE_OK;
}
```

### 8.2 编译与加载

```bash
# 编译
gcc -shared -fPIC -o mymodule.so mymodule.c -I/path/to/redis/src

# 加载
redis-server --loadmodule ./mymodule.so
```

### 8.3 注册自定义数据类型

```c
// 注册数据类型
RedisModuleType *MyType = RedisModule_CreateDataType(
    ctx, "mytype_", 0, &typemethods);
```

## 9. 模块生态与选型

| 模块            | 功能         | 适用场景           | 维护状态 |
| --------------- | ------------ | ------------------ | -------- |
| RedisJSON       | JSON 操作    | 用户配置、商品信息 | 活跃     |
| RediSearch      | 全文搜索     | 搜索引擎、自动补全 | 活跃     |
| RedisTimeSeries | 时间序列     | IoT、监控指标      | 活跃     |
| RedisBloom      | 概率数据结构 | 去重、限流、统计   | 活跃     |
| RedisCell       | 限流         | API 限流           | 活跃     |
| RedisAI         | ML 推理      | 实时推理           | 活跃     |

**Redis Stack**：Redis 官方将常用模块打包为 Redis Stack，包含 RedisJSON、RediSearch、RedisTimeSeries、RedisBloom 等模块，开箱即用。

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
| 向量集 | 009-VectorSet | 本文的并列主题 |
| RDB快照持久化 | 010-RDBSnapshotPersistence | 本文的并列主题 |
| AOF日志持久化 | 011-AOFLogPersistence | 本文的并列主题 |
| 混合持久化 | 012-MixedPersistence | 本文的并列主题 |
| 无盘复制 | 013-DisklessReplication | 本文的并列主题 |
| 模块系统 | 014-ModuleSystem | 本文自身 |
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
