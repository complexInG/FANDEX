---
order: 50
title: 位图
module: redis
category: Redis
difficulty: intermediate
description: Redis位图Bitmap：位操作、统计、用户标签、在线状态与布隆过滤器
author: fanquanpp
updated: '2026-08-01'
related:
  - redis/缓存策略与高级特性
  - redis/语法速查
  - redis/基数统计
  - redis/地理空间
prerequisites:
  - redis/概述与核心数据结构
---
## 1. 位图概述

位图（Bitmap）不是独立数据类型，而是基于 String 类型的位操作，每个 String 键最多存储 $2^{32}$ 个位。

## 2. 基本操作

```redis
SETBIT key offset value    -- 设置指定位
GETBIT key offset          -- 获取指定位
BITCOUNT key [start end]   -- 统计1的个数
BITPOS key bit [start end] -- 查找第一个0/1的位置
BITOP op destkey key [key ...] -- 位运算
```

```redis
-- 设置用户42在第100天登录
SETBIT user:login:2026 42 1

-- 检查用户42是否在第100天登录
GETBIT user:login:2026 42  -- 返回1

-- 统计2026年登录用户数
BITCOUNT user:login:2026
```

## 3. 应用场景

### 3.1 用户在线状态

```redis
-- 用户上线
SETBIT online:users 42 1
-- 用户下线
SETBIT online:users 42 0
-- 检查在线
GETBIT online:users 42
-- 在线人数
BITCOUNT online:users
```

### 3.2 用户标签

```redis
-- 用户42有标签0和标签3
SETBIT user:42:tags 0 1
SETBIT user:42:tags 3 1
-- 统计标签数
BITCOUNT user:42:tags
```

### 3.3 活跃用户统计

```redis
-- 每日活跃用户位图
SETBIT dau:2026-06-14 42 1

-- 计算月活跃用户（OR运算）
BITOP OR mau:2026-06 dau:2026-06-01 dau:2026-06-02 ... dau:2026-06-30
BITCOUNT mau:2026-06
```

## 4. 位运算

```redis
-- AND：交集
BITOP AND result key1 key2
-- OR：并集
BITOP OR result key1 key2
-- XOR：异或
BITOP XOR result key1 key2
-- NOT：取反
BITOP NOT result key1
```
## 基本操作

**基本写法：设置指定位的值**
`SETBIT <key> <offset> <value>`
```bash
# 设置用户42在第100天登录
SETBIT user:login:2026 42 1
```

**基本写法：获取指定位的值**
`GETBIT <key> <offset>`
```bash
# 检查用户42是否在第100天登录
GETBIT user:login:2026 42
```

**基本写法：统计为 1 的位数**
`BITCOUNT <key> [start end]`
```bash
# 统计2026年登录用户数
BITCOUNT user:login:2026
```

**基本写法：查找第一个 0/1 的位置**
`BITPOS <key> <bit> [start end]`
```bash
# 查找第一个为1的位置
BITPOS user:login:2026 1
```

---

## 位运算操作

**基本写法：AND 交集运算**
`BITOP AND <destkey> <key> [key ...]`
```bash
# 对 key1 和 key2 执行 AND 交集运算
BITOP AND result key1 key2
```

**基本写法：OR 并集运算**
`BITOP OR <destkey> <key> [key ...]`
```bash
# 对 key1 和 key2 执行 OR 并集运算
BITOP OR result key1 key2
```

**基本写法：XOR 异或运算**
`BITOP XOR <destkey> <key> [key ...]`
```bash
# 对 key1 和 key2 执行 XOR 异或运算
BITOP XOR result key1 key2
```

**基本写法：NOT 取反运算**
`BITOP NOT <destkey> <key>`
```bash
# 对 key1 执行 NOT 取反运算
BITOP NOT result key1
```

---

## 用户在线状态

**基本写法：标记用户上线**
`SETBIT <online_key> <user_id> 1`
```bash
# 用户42上线
SETBIT online:users 42 1
```

**基本写法：标记用户下线**
`SETBIT <online_key> <user_id> 0`
```bash
# 用户42下线
SETBIT online:users 42 0
```

**基本写法：检查用户是否在线**
`GETBIT <online_key> <user_id>`
```bash
# 检查用户42是否在线
GETBIT online:users 42
```

**基本写法：统计在线人数**
`BITCOUNT <online_key>`
```bash
# 统计当前在线人数
BITCOUNT online:users
```

---

## 用户标签

**基本写法：为用户打标签**
`SETBIT <user_tags_key> <tag_id> 1`
```bash
# 用户42拥有标签0
SETBIT user:42:tags 0 1
```

**多标签写法：为用户打多个标签**
`SETBIT <user_tags_key> <tag_id> 1`
```bash
# 用户42拥有标签0和标签3
SETBIT user:42:tags 0 1
SETBIT user:42:tags 3 1
```

**基本写法：统计用户标签数**
`BITCOUNT <user_tags_key>`
```bash
# 统计用户42的标签数量
BITCOUNT user:42:tags
```

---

## 活跃用户统计

**基本写法：记录每日活跃用户**
`SETBIT <dau_key> <user_id> 1`
```bash
# 记录用户42在2026-06-14活跃
SETBIT dau:2026-06-14 42 1
```

**换行写法：计算月活跃用户（OR 运算合并）**
`BITOP OR <destkey> <key> [key ...]`
```bash
# 计算月活跃用户（OR运算合并每日数据）
BITOP OR mau:2026-06 dau:2026-06-01 dau:2026-06-02 dau:2026-06-03
```

**基本写法：获取月活跃用户数**
`BITCOUNT <mau_key>`
```bash
# 获取2026年6月的月活跃用户数
BITCOUNT mau:2026-06
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
