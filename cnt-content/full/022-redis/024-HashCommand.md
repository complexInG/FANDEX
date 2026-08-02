---
order: 240
title: Redis Hash 命令速查
module: redis

category: '022-redis'
difficulty: beginner
description: Redis Hash 命令速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基本读写

**基本写法：HSET 设置单个字段**
`HSET <key> <field> <value>`
```bash
# 设置哈希表字段值
HSET user:1 name zhangsan
```

**基本写法：HSET 设置多个字段**
`HSET <key> <field1> <value1> <field2> <value2> [field value ...]`
```bash
# 一次性设置多个字段
HSET user:1 name zhangsan age 25 email zs@example.com
```

**基本写法：HGET 获取字段值**
`HGET <key> <field>`
```bash
# 获取哈希表指定字段值
HGET user:1 name
```

**基本写法：HMGET 批量获取字段**
`HMGET <key> <field1> <field2> [field ...]`
```bash
# 批量获取多个字段值
HMGET user:1 name age email
```

**基本写法：HGETALL 获取所有字段**
`HGETALL <key>`
```bash
# 获取哈希表所有字段和值
HGETALL user:1
```

**基本写法：HSETNX 字段不存在时设置**
`HSETNX <key> <field> <value>`
```bash
# 仅当字段不存在时设置
HSETNX user:1 status active
```

---

## 字段删除与判断

**基本写法：HDEL 删除字段**
`HDEL <key> <field1> [field2 ...]`
```bash
# 删除一个或多个字段
HDEL user:1 email
```

**基本写法：HEXISTS 判断字段是否存在**
`HEXISTS <key> <field>`
```bash
# 判断字段是否存在
HEXISTS user:1 name
```

**基本写法：HLEN 获取字段数量**
`HLEN <key>`
```bash
# 获取哈希表字段总数
HLEN user:1
```

---

## 获取字段与值

**基本写法：HKEYS 获取所有字段名**
`HKEYS <key>`
```bash
# 获取哈希表所有字段名
HKEYS user:1
```

**基本写法：HVALS 获取所有值**
`HVALS <key>`
```bash
# 获取哈希表所有字段值
HVALS user:1
```

**基本写法：HSTRLEN 获取字段值长度**
`HSTRLEN <key> <field>`
```bash
# 获取指定字段值的字节长度
HSTRLEN user:1 name
```

---

## 计数操作

**基本写法：HINCRBY 字段自增**
`HINCRBY <key> <field> <增量>`
```bash
# 哈希字段整数值自增
HINCRBY user:1 age 1
```

**基本写法：HINCRBYFLOAT 字段浮点自增**
`HINCRBYFLOAT <key> <field> <增量>`
```bash
# 哈希字段浮点数值自增
HINCRBYFLOAT product:1 price 9.9
```

---

## 批量与扫描

**基本写法：HMSET 批量设置（已弃用，推荐 HSET）**
`HMSET <key> <field1> <value1> <field2> <value2> [field value ...]`
```bash
# 批量设置多个字段（建议改用 HSET）
HMSET user:1 name zhangsan age 25
```

**基本写法：HSCAN 增量扫描**
`HSCAN <key> <游标> [MATCH <模式>] [COUNT <数量>]`
```bash
# 增量扫描哈希字段
HSCAN user:1 0 MATCH "na*" COUNT 10
```

---

## 字段过期（7.4+）

**基本写法：HEXPIRE 设置字段过期秒数**
`HEXPIRE <key> <秒> [NX|XX|GT|LT] FIELDS <数量> <field> [field ...]`
```bash
# 设置哈希字段 60 秒后过期（Redis 7.4+）
HEXPIRE user:1 60 FIELDS 1 session_token
```

**基本写法：HPEXPIRE 设置字段过期毫秒**
`HPEXPIRE <key> <毫秒> [NX|XX|GT|LT] FIELDS <数量> <field> [field ...]`
```bash
# 毫秒级字段过期（Redis 7.4+）
HPEXPIRE user:1 60000 FIELDS 1 session_token
```

**基本写法：HEXPIREAT 设置字段过期时间戳**
`HEXPIREAT <key> <Unix时间戳> [NX|XX|GT|LT] FIELDS <数量> <field> [field ...]`
```bash
# 指定时间戳过期（Redis 7.4+）
HEXPIREAT user:1 1735689600 FIELDS 1 session_token
```

**基本写法：HTTL 查看字段剩余秒数**
`HTTL <key> FIELDS <数量> <field> [field ...]`
```bash
# 查看字段剩余存活秒数（Redis 7.4+）
HTTL user:1 FIELDS 1 session_token
```

**基本写法：HPERSIST 移除字段过期**
`HPERSIST <key> FIELDS <数量> <field> [field ...]`
```bash
# 移除字段过期时间（Redis 7.4+）
HPERSIST user:1 FIELDS 1 session_token
```

---

## 实用模式

**基本写法：存储对象信息**
`HSET <对象key> <字段> <值> <字段> <值>`
```bash
# 用哈希表存储用户对象
HSET user:1001 name 张三 age 25 email zs@example.com city 北京
```

**基本写法：购物车实现**
`HINCRBY <cart:用户> <商品ID> <数量>`
```bash
# 购物车添加商品
HINCRBY cart:user1 product:1001 2
```

**基本写法：商品库存**
`HSET <stock:商品> <规格> <库存数>`
```bash
# 按规格管理库存
HSET stock:item:1001 red 50 blue 30 green 20
```

**基本写法：点赞计数**
`HINCRBY <like:文章> <用户ID> 1`
```bash
# 文章点赞计数
HINCRBY like:article:100 user:1 1
```

**基本写法：部分更新对象**
`HSET <key> <字段> <新值>`
```bash
# 仅更新对象的某个字段
HSET user:1001 email new@example.com
```

---

## 性能建议

**基本写法：避免 HGETALL 大哈希**
`HSCAN <key> <游标> [COUNT <数量>]`
```bash
# 大哈希表使用 HSCAN 避免阻塞
HSCAN big:hash 0 COUNT 100
```

**基本写法：使用 HGET 替代 HGETALL**
`HGET <key> <field>`
```bash
# 仅获取需要的字段而非全部
HGET user:1 name
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
