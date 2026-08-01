---
order: 290
title: Redis 7.0+ 新特性命令速查手册
module: 022-redis
category: '022-redis'
difficulty: beginner
description: Redis 7.0+ 新特性命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Redis Functions（7.0+）

**基本写法：FUNCTION LOAD 加载函数库**
`FUNCTION LOAD [REPLACE] '#!lua name=<库名> ...'`
```redis
-- Redis 7.0 用 Function 替代 Lua 脚本，可持久化、可读
FUNCTION LOAD "#!lua name=mylib
redis.register_function('myset',
  function(keys, args)
    redis.call('SET', keys[1], args[1])
    redis.call('EXPIRE', keys[1], args[2])
    return redis.call('GET', keys[1])
  end
)"

-- REPLACE 覆盖同名库
FUNCTION LOAD REPLACE "#!lua name=mylib ..."

-- 调用函数
FCALL myset 1 mykey myvalue 60
-- 参数：函数名 key数量 key... arg...
```

---

**基本写法：FUNCTION 管理命令**
`FUNCTION LIST | DUMP | RESTORE | DELETE | STATS`
```redis
-- 列出所有函数库
FUNCTION LIST
FUNCTION LIST WITHCODE          -- 显示代码

-- 导出函数库（二进制）
FUNCTION DUMP

-- 恢复函数库
FUNCTION RESTORE <serialized> [FLUSH|APPEND|REPLACE]

-- 删除函数库
FUNCTION DELETE mylib

-- 查看函数执行统计
FUNCTION STATS
-- 返回：running_script, engines
```

---

**基本写法：FCALL vs EVAL 对比**
`FCALL <函数> <key数> ... | EVAL <脚本> <key数> ...`
```redis
-- 传统 Lua 脚本（每次传输脚本，重启缓存丢失）
EVAL 'return redis.call('GET', KEYS[1])' 1 mykey

-- Redis Function（持久化、可读、可管理）
FCALL my_get 1 mykey

-- 优势对比：
-- 持久化：Function 随 RDB/AOF 持久化，重启不丢；Lua 重启丢失需重新 LOAD
-- 主从复制：Function 定义复制到从库；Lua 脚本内容复制
-- 可读性：函数名 vs SHA1 哈希
-- RESP3：Function 可返回 Map/Set 类型
```

---

## Sharded Pub/Sub（7.0+）

**基本写法：SSUBSCRIBE / SPUBLISH**
`SSUBSCRIBE <频道> | SPUBLISH <频道> <消息>`
```redis
-- 分片发布订阅：消息只在频道所属分片传播，不广播全集群
-- 订阅分片频道（必须连接拥有该频道槽位的节点）
SSUBSCRIBE orders

-- 发布到分片频道
SPUBLISH orders '{"id":123}'

-- 返回收到消息的订阅者数
-- 优势：集群环境下线性扩展吞吐量
-- 限制：不支持 PSUBSCRIBE 模式订阅
```

---

**基本写法：Hash Tag 共址订阅**
`SSUBSCRIBE {user100}.events`
```redis
-- 用 Hash Tag 确保相关频道在同一分片
SSUBSCRIBE {user100}.events
SPUBLISH {user100}.events 'login'

-- 查看分片频道订阅（在所属节点执行）
PUBSUB SHARDCHANNELS orders*
PUBSUB SHARDNUMSUB orders
```

---

## Multi-Part AOF（7.0+）

**基本写法：AOF 多文件结构**
`appendonly yes`
```conf
# Redis 7.0 AOF 重构为多文件结构
appendonly yes
appenddirname "appendonlydir"

# 文件结构：
# appendonlydir/
#   appendonly.aof.manifest          -- 清单
#   appendonly.aof.1.base.rdb        -- Base：RDB 格式全量快照
#   appendonly.aof.1.incr.aof        -- 增量 AOF
#   appendonly.aof.2.incr.aof        -- 下一个增量

# 优势：
# - 重写时无需大内存缓冲区
# - 增量文件轮转，渐进清理
# - 可选择性恢复
```

---

**基本写法：AOF 相关命令**
`BGREWRITEAOF | CONFIG SET auto-aof-rewrite-percentage`
```redis
-- 手动触发 AOF 重写
BGREWRITEAOF

-- 自动重写触发条件
CONFIG SET auto-aof-rewrite-percentage 100
CONFIG SET auto-aof-rewrite-min-size 64mb

-- AOF 策略
CONFIG SET appendfsync everysec    -- always|everysec|no
```

---

## listpack 全面替代 ziplist（7.0+）

**基本写法：listpack 配置**
`hash-max-listpack-entries | zset-max-listpack-entries`
```conf
# Redis 7.0 用 listpack 替代 ziplist，消除连锁更新问题
hash-max-listpack-entries 512
hash-max-listpack-value 64
zset-max-listpack-entries 128
zset-max-listpack-value 64
list-max-listpack-size -2
stream-node-max-bytes 4096

# 旧的 ziplist 配置自动忽略
# hash-max-ziplist-entries (已废弃)
```

---

**基本写法：查看编码**
`OBJECT ENCODING <key>`
```redis
-- 小数据用 listpack 编码，大数据用 hashtable/skiplist
SET k v
OBJECT ENCODING k    -- listpack（小）或 skiplist（大）

-- listpack 优势：
-- 无 prevlen 字段，彻底消除连锁更新
-- 高并发写入下无延迟抖动
```

---

## ACL v2（7.0+）

**基本写法：Selector 选择器**
`ACL SETUSER <用户> on >pwd (<规则组1>) (<规则组2>)`
```redis
-- ACL v2 支持多组规则，根规则或任一 selector 匹配即允许
ACL SETUSER dev on >pwd \
  (~dev:* +@all) \
  (~prod:* +@read -@dangerous)

-- 频道权限独立控制
ACL SETUSER sub on >pwd &channel:* +@pubsub

-- 查看 selector
ACL GETUSER dev
-- 返回 selectors 字段列出所有选择器
```

---

## Redis 7.2 新特性

**基本写法：JSON.MERGE / JSON.MSET（RedisJSON 2.6+）**
`JSON.MERGE <key> <path> <value> | JSON.MSET <key> <path> <value> ...`
```redis
-- JSON.MERGE 合并值到匹配路径
JSON.SET doc $ {"a":1,"b":{"c":2}}
JSON.MERGE doc $.b {"d":3}
-- 结果：{"a":1,"b":{"c":2,"d":3}}

-- JSON.MSET 批量设置
JSON.MSET k1 $.a 1 k2 $.a 2 k3 $.a 3
```

---

**基本写法：地理多边形搜索（7.2）**
`GEOSEARCH <key> FROBMEMBER <成员> BYRADIUS ... | ...`
```redis
-- Redis 7.2 RedisSearch 支持多边形地理查询
-- 基础 GEOSEARCH（圆形）
GEOSEARCH stores FROMLONLAT 116.40 39.90 BYRADIUS 5 km ASC

-- 多边形搜索（需 RedisSearch 模块）
FT.SEARCH idx '@location:[POLYGON 116.38 39.88 116.42 39.88 116.42 39.92 116.38 39.92]'
```

---

**基本写法：sorted set 性能提升**
`ZADD | ZRANGE（7.2 优化）`
```redis
-- Redis 7.2 sorted set 性能提升 30%~100%
-- 命令语法不变，底层优化
ZADD leaderboard 100 'Alice' 200 'Bob'
ZRANGE leaderboard 0 9 WITHSCORES REV
```

---

## Redis 7.4 新特性预览

**基本写法：Hash 字段过期（7.4+）**
`HEXPIRE <key> <秒> FIELDS <n> <字段> | HTTL <key> FIELDS <n> <字段>`
```redis
-- Redis 7.4 支持 Hash 单字段过期
HEXPIRE user:1001 3600 FIELDS 1 session_token
HTTL user:1001 FIELDS 1 session_token
HPERSIST user:1001 FIELDS 1 session_token

-- 字段过期后自动删除，不影响其他字段
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
| 向量集 | 009-VectorSet | 本文的并列主题 |
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
| Redis 7.0+ 新特性命令速查手册 | 029-NewFeatures7 | 本文自身 |
