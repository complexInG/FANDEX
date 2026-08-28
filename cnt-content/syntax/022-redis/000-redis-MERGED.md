---
order: 10
title: redis 模块文档合集
module: 'redis'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：022-redis/001-GeoSpatial.md ============ -->

# 地理空间

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本操作

**单成员写法：添加单个地理位置**
`GEOADD <key> <longitude> <latitude> <member>`
```bash
# 添加天安门的位置
GEOADD locations 116.3975 39.9087 "天安门"
```

**多成员写法：添加多个地理位置**
`GEOADD <key> <longitude> <latitude> <member> [longitude latitude member ...]`
```bash
# 添加天安门和外滩的位置
GEOADD locations 116.3975 39.9087 "天安门" 121.4737 31.2304 "外滩"
```

**单成员写法：获取单个成员坐标**
`GEOPOS <key> <member>`
```bash
# 获取天安门的坐标
GEOPOS locations "天安门"
```

**多成员写法：获取多个成员坐标**
`GEOPOS <key> <member> [member ...]`
```bash
# 获取天安门和外滩的坐标
GEOPOS locations "天安门" "外滩"
```

**基本写法：计算两点距离**
`GEODIST <key> <member1> <member2> [unit]`
```bash
# 计算天安门到外滩的距离（单位km）
GEODIST locations "天安门" "外滩" km
```

---

## 范围查询

**基本写法：按经纬度半径查询附近地点**
`GEOSEARCH <key> FROMLONLAT <lon> <lat> BYRADIUS <radius> <unit> [WITHCOORD] [WITHDIST] [COUNT N] [ASC|DESC]`
```bash
# 查找坐标(116.4, 39.9)附近3公里内的地点，按距离升序返回前10个
GEOSEARCH locations FROMLONLAT 116.4 39.9 BYRADIUS 3 km WITHDIST WITHCOORD COUNT 10 ASC
```

**基本写法：按矩形范围查询**
`GEOSEARCH <key> FROMLONLAT <lon> <lat> BYBOX <width> <height> <unit> [WITHCOORD] [WITHDIST]`
```bash
# 查找矩形范围内的地点（宽10km高10km）
GEOSEARCH locations FROMLONLAT 116.4 39.9 BYBOX 10 10 km WITHDIST
```

**基本写法：以成员为中心查询附近地点**
`GEOSEARCH <key> FROMMEMBER <member> BYRADIUS <radius> <unit> [WITHDIST]`
```bash
# 查找天安门附近5公里内的地点
GEOSEARCH locations FROMMEMBER "天安门" BYRADIUS 5 km WITHDIST
```

**基本写法：旧版按经纬度半径查询**
`GEORADIUS <key> <longitude> <latitude> <radius> <unit> [WITHCOORD] [WITHDIST] [COUNT N]`
```bash
# 旧版范围查询（已废弃，建议使用GEOSEARCH）
GEORADIUS locations 116.4 39.9 3 km WITHCOORD WITHDIST COUNT 10
```

---

## 应用场景

**基本写法：添加用户位置**
`GEOADD <nearby_key> <lon> <lat> <member>`
```bash
# 添加用户42的位置
GEOADD nearby:users 116.4 39.9 "user:42"
```

**基本写法：查找附近用户**
`GEOSEARCH <nearby_key> FROMMEMBER <member> BYRADIUS <radius> <unit> [COUNT N]`
```bash
# 查找用户42附近1km内的用户，最多返回20个
GEOSEARCH nearby:users FROMMEMBER "user:42" BYRADIUS 1 km COUNT 20
```

**多成员写法：添加多个门店位置**
`GEOADD <stores_key> <longitude> <latitude> <member> [longitude latitude member ...]`
```bash
# 添加门店1和门店2的位置
GEOADD stores 116.397 39.908 "store:1" 116.401 39.912 "store:2"
```

**基本写法：查找附近门店按距离升序**
`GEOSEARCH <stores_key> FROMLONLAT <lon> <lat> BYRADIUS <radius> <unit> [WITHDIST] [ASC]`
```bash
# 查找坐标(116.4, 39.9)附近2km内门店，按距离升序
GEOSEARCH stores FROMLONLAT 116.4 39.9 BYRADIUS 2 km WITHDIST ASC
```



<!-- ============ 文档分隔线：022-redis/002-PipeTransactionAtomic.md ============ -->

# 管道与事务原子性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Pipeline 管道

**基本写法：Python 批量发送命令减少 RTT**
`pipe = r.pipeline()`
```python
# Python redis-py 使用 Pipeline 批量发送命令
import redis
r = redis.Redis()

pipe = r.pipeline()
for i in range(10000):
    pipe.set(f'key:{i}', f'value:{i}')
pipe.execute()
```

---

## 事务基本用法

**基本写法：开启并提交事务**
`MULTI ... EXEC`
```bash
# 开启事务，命令入队后统一执行
MULTI
SET key1 val1
SET key2 val2
INCR counter
EXEC
```

**基本写法：取消事务**
`MULTI ... DISCARD`
```bash
# 取消事务，所有入队命令不执行
MULTI
SET key1 val1
DISCARD
```

---

## WATCH 乐观锁

**基本写法：CAS 乐观锁**
`WATCH <key> [key ...] ... MULTI ... EXEC`
```bash
# 监视 counter 键，读取后开启事务设置新值
WATCH counter
GET counter
MULTI
SET counter 6
EXEC
```

**基本写法：被监视键被修改时事务失败**
`WATCH <key> ... MULTI ... EXEC`
```bash
# 事务A监视counter，事务B修改counter后事务A的EXEC返回nil
WATCH counter
GET counter
MULTI
SET counter 6
EXEC
```

**基本写法：Python WATCH 秒杀乐观锁重试**
`r.watch(<key>)`
```python
# Python 乐观锁重试秒杀
import redis

def seckill(user_id, item_id):
    r = redis.Redis()
    key = f'stock:{item_id}'

    while True:
        try:
            r.watch(key)
            stock = int(r.get(key) or 0)
            if stock <= 0:
                r.unwatch()
                return False

            pipe = r.pipeline()
            pipe.multi()
            pipe.decr(key)
            pipe.sadd(f'users:{item_id}', user_id)
            pipe.execute()
            return True
        except redis.WatchError:
            continue
```

---

## Pipeline + 事务

**基本写法：Pipeline 中使用事务**
`pipe.multi()`
```python
# Pipeline 中开启事务，兼顾性能与原子性
pipe = r.pipeline()
pipe.multi()
pipe.set('key1', 'v1')
pipe.set('key2', 'v2')
pipe.incr('counter')
pipe.execute()
```

**基本写法：Pipeline 事务模式快捷方式**
`pipe = r.pipeline(True)`
```python
# transaction=True 等价于先 pipeline 再 multi
pipe = r.pipeline(True)
pipe.set('key1', 'v1')
pipe.set('key2', 'v2')
pipe.incr('counter')
pipe.execute()
```

---

## Lua 脚本替代方案

**基本写法：Lua 原子性秒杀**
`EVAL <script> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 使用 Lua 脚本保证秒杀操作的原子性
EVAL "local stock = tonumber(redis.call('GET', KEYS[1])) if stock and stock > 0 then redis.call('DECR', KEYS[1]) redis.call('SADD', KEYS[2], ARGV[1]) return 1 end return 0" 2 stock:item1 users:item1 user42
```



<!-- ============ 文档分隔线：022-redis/003-NumberStats.md ============ -->

# 基数统计

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本操作

**单元素写法：添加单个元素到 HyperLogLog**
`PFADD <key> <element>`
```bash
# 添加单个用户到UV统计
PFADD uv:2026-06-14 user1
```

**多元素写法：添加多个元素到 HyperLogLog**
`PFADD <key> <element> [element ...]`
```bash
# 添加多个用户，重复元素自动去重
PFADD uv:2026-06-14 user1 user2 user3 user1 user2
```

**基本写法：获取基数估算值**
`PFCOUNT <key>`
```bash
# 获取单天的UV数
PFCOUNT uv:2026-06-14
```

**多键写法：获取多个键的合并基数**
`PFCOUNT <key> [key ...]`
```bash
# 获取多天合并后的UV数
PFCOUNT uv:2026-06-13 uv:2026-06-14
```

**基本写法：合并多个 HyperLogLog**
`PFMERGE <destkey> <sourcekey> [sourcekey ...]`
```bash
# 合并多天UV到周UV
PFMERGE uv:2026-week uv:2026-06-08 uv:2026-06-09 uv:2026-06-10
```

---

## 应用场景

**基本写法：统计网站独立访客**
`PFADD <site_uv_key> <user_id>`
```bash
# 网站UV统计
PFADD site:uv:2026-06-14 user42
```

**基本写法：统计页面独立访客**
`PFADD <page_uv_key> <user_id>`
```bash
# 页面UV统计
PFADD page:uv:article:123:2026-06-14 user42
```

**基本写法：统计搜索关键词独立用户数**
`PFADD <search_uv_key> <user_id>`
```bash
# 搜索关键词UV统计
PFADD search:uv:keyword:redis:2026-06-14 user42
```

**换行写法：合并每日活跃用户计算周活跃**
`PFMERGE <wau_key> <dau_key> [dau_key ...]`
```bash
# 合并每日活跃用户数据计算周活跃用户
PFMERGE wau:2026-w24 dau:2026-06-09 dau:2026-06-10 dau:2026-06-11
```

**基本写法：获取周活跃用户数**
`PFCOUNT <wau_key>`
```bash
# 获取第24周的活跃用户数
PFCOUNT wau:2026-w24
```



<!-- ============ 文档分隔线：022-redis/004-Stream.md ============ -->

# 流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 添加消息

**基本写法：自动生成 ID 添加消息**
`XADD <key> * <field> <value>`
```bash
# 添加消息，* 表示自动生成ID
XADD mystream * field1 value1
```

**多字段写法：自动生成 ID 添加多字段消息**
`XADD <key> * <field> <value> [field value ...]`
```bash
# 添加包含多个字段的消息
XADD mystream * field1 value1 field2 value2
```

**基本写法：手动指定消息 ID**
`XADD <key> <id> <field> <value>`
```bash
# 指定ID格式添加消息
XADD mystream 1718334600000-0 field1 value1
```

**基本写法：添加消息并限制 Stream 长度**
`XADD <key> MAXLEN <count> * <field> <value> [field value ...]`
```bash
# 限制Stream长度为1000
XADD mystream MAXLEN 1000 * field1 value1
```

---

## 读取消息

**基本写法：从头读取指定数量消息**
`XREAD COUNT <count> STREAMS <key> <id>`
```bash
# 从头读取10条消息
XREAD COUNT 10 STREAMS mystream 0
```

**基本写法：阻塞读取新消息**
`XREAD BLOCK <ms> COUNT <count> STREAMS <key> $`
```bash
# 阻塞读取新消息，最多等待5000ms
XREAD BLOCK 5000 COUNT 10 STREAMS mystream $
```

**基本写法：范围读取所有消息**
`XRANGE <key> - + [COUNT <count>]`
```bash
# 读取所有消息，最多返回10条
XRANGE mystream - + COUNT 10
```

**基本写法：按 ID 范围读取消息**
`XRANGE <key> <start> <end> [COUNT <count>]`
```bash
# 按ID范围读取消息
XRANGE mystream 1718334600000-0 1718334700000-0
```

---

## 消费者组

**基本写法：从最新消息开始创建消费者组**
`XGROUP CREATE <key> <group> $`
```bash
# 从最新消息开始创建消费者组
XGROUP CREATE mystream mygroup $
```

**基本写法：从头开始创建消费者组**
`XGROUP CREATE <key> <group> 0`
```bash
# 从头开始创建消费者组
XGROUP CREATE mystream mygroup 0
```

**基本写法：消费者读取消息**
`XREADGROUP GROUP <group> <consumer> COUNT <count> STREAMS <key> >`
```bash
# 消费者consumer1读取1条消息
XREADGROUP GROUP mygroup consumer1 COUNT 1 STREAMS mystream >
```

**单消息写法：确认单条消息已处理**
`XACK <key> <group> <id>`
```bash
# 确认单条消息
XACK mystream mygroup 1718334600000-0
```

**多消息写法：确认多条消息已处理**
`XACK <key> <group> <id> [id ...]`
```bash
# 确认多条消息
XACK mystream mygroup 1718334600000-0 1718334600001-0
```

**基本写法：查看待处理消息**
`XPENDING <key> <group>`
```bash
# 查看待处理消息
XPENDING mystream mygroup
```

**单消息写法：认领单条超时消息**
`XCLAIM <key> <group> <consumer> <min-idle-time> <id>`
```bash
# 认领空闲超过3600000ms的单条消息
XCLAIM mystream mygroup consumer1 3600000 1718334600000-0
```

**多消息写法：认领多条超时消息**
`XCLAIM <key> <group> <consumer> <min-idle-time> <id> [id ...]`
```bash
# 认领空闲超过3600000ms的多条消息
XCLAIM mystream mygroup consumer1 3600000 1718334600000-0 1718334600001-0
```

---

## 消息积压处理

**基本写法：查看 Stream 信息**
`XINFO STREAM <key>`
```bash
# 查看 Stream 详细信息
XINFO STREAM mystream
```

**基本写法：按最大长度修剪 Stream**
`XTRIM <key> MAXLEN <count>`
```bash
# 按最大长度修剪Stream为10000条
XTRIM mystream MAXLEN 10000
```

**基本写法：按最小 ID 修剪 Stream**
`XTRIM <key> MINID <id>`
```bash
# 删除ID小于指定值的消息
XTRIM mystream MINID 1718334600000-0
```

**基本写法：查看所有消费者组**
`XINFO GROUPS <key>`
```bash
# 查看Stream的所有消费者组
XINFO GROUPS mystream
```

**基本写法：查看消费者组内消费者**
`XINFO CONSUMERS <key> <group>`
```bash
# 查看消费者组mygroup内的消费者
XINFO CONSUMERS mystream mygroup
```



<!-- ============ 文档分隔线：022-redis/005-MemoryEvictionPolicy.md ============ -->

﻿# 内存淘汰策略

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 触发条件

**基本写法：设置最大内存**
`CONFIG SET maxmemory <bytes>`
```bash
# 设置 Redis 最大内存为 4GB
CONFIG SET maxmemory 4gb
```

**基本写法：查看内存使用**
`INFO memory`
```bash
# 查看当前内存使用情况
INFO memory
```

---

## 淘汰策略配置

**基本写法：不淘汰策略**
`CONFIG SET maxmemory-policy noeviction`
```bash
# 内存不足时拒绝写入，返回错误
CONFIG SET maxmemory-policy noeviction
```

**基本写法：所有键 LRU 策略**
`CONFIG SET maxmemory-policy allkeys-lru`
```bash
# 所有键中淘汰最久未访问的键
CONFIG SET maxmemory-policy allkeys-lru
```

**基本写法：所有键 LFU 策略**
`CONFIG SET maxmemory-policy allkeys-lfu`
```bash
# 所有键中淘汰访问频率最低的键
CONFIG SET maxmemory-policy allkeys-lfu
```

**基本写法：所有键随机策略**
`CONFIG SET maxmemory-policy allkeys-random`
```bash
# 所有键中随机淘汰
CONFIG SET maxmemory-policy allkeys-random
```

**基本写法：有 TTL 的键 LRU 策略**
`CONFIG SET maxmemory-policy volatile-lru`
```bash
# 有过期时间的键中淘汰最久未访问的键
CONFIG SET maxmemory-policy volatile-lru
```

**基本写法：有 TTL 的键 LFU 策略**
`CONFIG SET maxmemory-policy volatile-lfu`
```bash
# 有过期时间的键中淘汰访问频率最低的键
CONFIG SET maxmemory-policy volatile-lfu
```

**基本写法：有 TTL 的键随机策略**
`CONFIG SET maxmemory-policy volatile-random`
```bash
# 有过期时间的键中随机淘汰
CONFIG SET maxmemory-policy volatile-random
```

**基本写法：有 TTL 的键最短 TTL 优先策略**
`CONFIG SET maxmemory-policy volatile-ttl`
```bash
# 有过期时间的键中淘汰 TTL 最短的键
CONFIG SET maxmemory-policy volatile-ttl
```

---

## LRU 算法

**基本写法：设置 LRU 采样数**
`CONFIG SET maxmemory-samples <N>`
```bash
# 设置 LRU 采样数为 5（默认值）
CONFIG SET maxmemory-samples 5
```

**结构定义写法：redisObject LRU 时钟字段**
`struct redisObject { unsigned lru:24; }`
```c
// 每个 Redis 对象头包含一个 24 位的 LRU 时钟
typedef struct redisObject {
    unsigned type:4;
    unsigned encoding:4;
    unsigned lru:24;    // LRU 时间戳（精度约1.5分钟）
    int refcount;
    void *ptr;
} robj;
```

---

## LFU 算法

**基本写法：设置 LFU 衰减时间**
`CONFIG SET lfu-decay-time <minutes>`
```bash
# 设置 LFU 计数器衰减时间为 1 分钟
CONFIG SET lfu-decay-time 1
```

**基本写法：设置 LFU 计数器因子**
`CONFIG SET lfu-log-factor <factor>`
```bash
# 设置 LFU 计数器对数因子为 10
CONFIG SET lfu-log-factor 10
```

**函数源码写法：LFU 对数计数器更新**
`uint8_t LFULogIncr(uint8_t counter)`
```c
// LFU 对数计数器更新函数
uint8_t LFULogIncr(uint8_t counter) {
    if (counter == 255) return 255;
    double r = (double)rand() / RAND_MAX;
    double baseval = counter - LFU_INIT_VAL;  // LFU_INIT_VAL = 5
    if (baseval < 0) baseval = 0;
    double p = 1.0 / (baseval * 10 + 1);  // 概率递减
    if (r < p) counter++;
    return counter;
}
```

---

## 监控与调优

**基本写法：查看淘汰统计**
`INFO stats`
```bash
# 查看键淘汰统计信息
INFO stats
```



<!-- ============ 文档分隔线：022-redis/006-BitGraph.md ============ -->

# 位图

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：022-redis/007-StringSDSStructure.md ============ -->

﻿# 字符串 SDS 结构

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 结构定义

**结构定义写法：sdshdr8 头部**
`struct __attribute__((packed)) sdshdr8 { uint8_t len; uint8_t alloc; unsigned char flags; char buf[]; }`
```c
// 定义 sdshdr8 类型头部（用于短字符串）
struct __attribute__((packed)) sdshdr8 {
    uint8_t  len;         // 已使用长度（不含\0）
    uint8_t  alloc;       // 总分配容量（不含\0和header）
    unsigned char flags;   // 类型标识：SDS_TYPE_8
    char     buf[];       // 实际数据（柔性数组）
};
```

**结构定义写法：sdshdr16 头部**
`struct __attribute__((packed)) sdshdr16 { uint16_t len; uint16_t alloc; unsigned char flags; char buf[]; }`
```c
// 定义 sdshdr16 类型头部（用于中等长度字符串）
struct __attribute__((packed)) sdshdr16 {
    uint16_t len;
    uint16_t alloc;
    unsigned char flags;
    char buf[];
};
```

**结构定义写法：sdshdr32 头部**
`struct __attribute__((packed)) sdshdr32 { uint32_t len; uint32_t alloc; unsigned char flags; char buf[]; }`
```c
// 定义 sdshdr32 类型头部（用于较长字符串）
struct __attribute__((packed)) sdshdr32 {
    uint32_t len;
    uint32_t alloc;
    unsigned char flags;
    char buf[];
};
```

**结构定义写法：sdshdr64 头部**
`struct __attribute__((packed)) sdshdr64 { uint64_t len; uint64_t alloc; unsigned char flags; char buf[]; }`
```c
// 定义 sdshdr64 类型头部（用于超长字符串）
struct __attribute__((packed)) sdshdr64 {
    uint64_t len;
    uint64_t alloc;
    unsigned char flags;
    char buf[];
};
```

---

## 内存布局

**内存布局写法：sdshdr8 字节排列**
`[len][alloc][flags][buf[]][\0]`
```c
// sdshdr8 内存布局示例
// len = 5:   已使用5字节
// alloc = 10: 总容量10字节（不含header和\0）
// 剩余空间 = alloc - len = 5字节
```

---

## 预分配策略

**预分配规则写法：修改后 len 小于 1MB**
`if (newlen < SDS_MAX_PREALLOC) newlen *= 2;`
```c
// 规则1: 修改后 len < 1MB 时翻倍分配
// 示例: len=10 → 修改后 len=15 → alloc=30
```

**预分配规则写法：修改后 len 大于等于 1MB**
`else newlen += SDS_MAX_PREALLOC;`
```c
// 规则2: 修改后 len >= 1MB 时固定追加1MB
// 示例: len=3MB → 修改后 len=5MB → alloc=6MB
```

**函数源码写法：sdsMakeRoomFor 扩容核心函数**
`sds sdsMakeRoomFor(sds s, size_t addlen)`
```c
// sds.c - sdsMakeRoomFor 扩容核心函数
sds sdsMakeRoomFor(sds s, size_t addlen) {
    size_t free = sdsavail(s);  // 剩余空间
    if (free >= addlen) return s;  // 空间足够，直接返回

    size_t len = sdslen(s);
    size_t newlen = len + addlen;

    // 预分配策略
    if (newlen < SDS_MAX_PREALLOC)  // SDS_MAX_PREALLOC = 1MB
        newlen *= 2;               // 翻倍
    else
        newlen += SDS_MAX_PREALLOC; // +1MB

    return sds_realloc(s, newlen);
}
```

---

## 惰性删除

**函数源码写法：sdstrim 缩短字符串不释放内存**
`sds sdstrim(sds s, const char *cset)`
```c
// sds.c - sdstrim 删除首尾匹配字符但不调用 realloc
sds sdstrim(sds s, const char *cset) {
    // 删除首尾匹配字符
    // 不调用 realloc 释放内存
    // 仅更新 len 和 free
    sdssetlen(s, newlen);  // 更新 len
    return s;
}
```

**惰性删除示例写法：仅更新 len 不释放内存**
`sdstrim(s, "ld")`
```c
// SDS: "hello world" (len=11, alloc=11)
// 执行: sdstrim(s, "ld")  → 删除首尾的 'l' 和 'd'
// 结果: "hello wor" (len=9, alloc=11)
//       剩余空间 = 2 字节，未释放
```

**显式释放写法：sdsRemoveFreeSpace 回收内存**
`sdsRemoveFreeSpace(s)`
```c
// 显式调用 sdsRemoveFreeSpace 释放剩余空间
// 结果: "hello wor" (len=9, alloc=9)
```

**真正释放时机写法：触发内存回收的条件**
`sdsRemoveFreeSpace(s) | 键被删除 | 内存淘汰 | 对象重写`
```c
// 1. 显式调用 sdsRemoveFreeSpace
// 2. 键被删除时，整个 SDS 被释放
// 3. Redis 内存淘汰时
// 4. 使用 SDS 的对象被重写时
```

---

## 二进制安全

**函数源码写法：sdsnewlen 存储包含 \0 的二进制数据**
`sds sdsnewlen(const void *init, size_t initlen)`
```c
// SDS 可以存储任意二进制数据
sds s = sdsnewlen("hello\0world", 11);  // len=11
printf("%zu", sdslen(s));  // 输出: 11
```

**兼容 C 字符串函数写法：buf 末尾保留 \0**
`sdsnew("hello")`
```c
// SDS 的 buf 末尾始终保留 \0，可以直接使用 C 字符串函数
sds s = sdsnew("hello");
printf("%s", s);  // 直接传给 printf，兼容 C 字符串
strcmp(s, "hello");  // 可以使用 strcmp
```

---

## 类型选择

**函数源码写法：sdsReqType 根据字符串长度选择 SDS 类型**
`static inline char sdsReqType(size_t string_size)`
```c
// sds.c - sdsReqType 根据字符串长度选择 SDS 类型
static inline char sdsReqType(size_t string_size) {
    if (string_size < 1 << 5)  return SDS_TYPE_5;
    if (string_size < 1 << 8)  return SDS_TYPE_8;
    if (string_size < 1 << 16) return SDS_TYPE_16;
    if (string_size < 1ll << 32) return SDS_TYPE_32;
    return SDS_TYPE_64;
}
```



<!-- ============ 文档分隔线：022-redis/008-AOFLogPersistence.md ============ -->

# AOF 日志持久化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 工作流程

**函数源码写法：命令追加到 AOF 缓冲区**
`void feedAppendOnlyFile(struct redisCommand *cmd, int argc, robj **argv)`
```c
// 将命令转换为 RESP 协议格式并追加到 aof_buf
void feedAppendOnlyFile(struct redisCommand *cmd, int argc, robj **argv) {
    buf = catAppendOnlyGenericCommand(argc, argv);
    aof_buf = sdscatlen(aof_buf, buf, sdslen(buf));
}
```

**函数源码写法：写入文件并根据策略刷盘**
`void flushAppendOnlyFile(int force)`
```c
// 将 aof_buf 写入 AOF 文件并根据 appendfsync 策略决定是否 fsync
void flushAppendOnlyFile(int force) {
    nwritten = write(server.aof_fd, server.aof_buf, sdslen(server.aof_buf));
    if (server.aof_fsync == APPENDFSYNC_ALWAYS) {
        fsync(server.aof_fd);
    }
}
```

---

## appendfsync 策略

**基本写法：每条命令都 fsync**
`appendfsync always`
```bash
# 每条写命令执行后立即调用 fsync
appendfsync always
```

**基本写法：每秒 fsync（默认推荐）**
`appendfsync everysec`
```bash
# 每秒调用一次 fsync
appendfsync everysec
```

**基本写法：由操作系统决定刷盘**
`appendfsync no`
```bash
# 不主动 fsync，由操作系统决定刷盘时机
appendfsync no
```

---

## AOF 重写

**基本写法：手动触发 AOF 重写**
`BGREWRITEAOF`
```bash
# 手动触发 AOF 重写
BGREWRITEAOF
```

**基本写法：配置重写增长百分比阈值**
`auto-aof-rewrite-percentage <percentage>`
```bash
# AOF 文件大小比上次重写后增长 100% 时触发重写
auto-aof-rewrite-percentage 100
```

**基本写法：配置重写最小文件大小**
`auto-aof-rewrite-min-size <size>`
```bash
# AOF 文件最小 64MB 才触发重写
auto-aof-rewrite-min-size 64mb
```

**基本写法：重写时合并列表操作**
`RPUSH <key> <values>`
```bash
# 重写后将多次 RPUSH 和 LPOP 合并为一条命令
RPUSH list b c d e f
```

---

## AOF 文件格式

**基本写法：RESP 协议格式**
`*<count>\r\n$<len>\r\n<command>\r\n...`
```bash
# AOF 文件使用 RESP 协议格式存储命令
*2
$6
SELECT
$1
0
```

**基本写法：SET 命令的 RESP 格式**
`*3\r\n$3\r\nSET\r\n$<keylen>\r\n<key>\r\n$<vallen>\r\n<value>\r\n`
```bash
# SET key1 value1 的 RESP 格式
*3
$3
SET
$4
key1
$6
value1
```

**基本写法：MULTI/EXEC 合并格式（Redis 4.0+）**
`*1\r\n$5\r\nMULTI\r\n...*1\r\n$4\r\nEXEC\r\n`
```bash
# Redis 4.0+ 使用 MULTI/EXEC 包裹多条命令减少文件体积
*1
$5
MULTI
*3
$3
SET
$3
key
$5
value
*1
$4
EXEC
```

---

## AOF 文件恢复

**基本写法：开启 AOF 持久化**
`appendonly yes`
```bash
# 开启 AOF，Redis 启动时自动加载 AOF 文件
appendonly yes
```

**基本写法：检查 AOF 文件**
`redis-check-aof <file>`
```bash
# 检查 AOF 文件完整性
redis-check-aof appendonly.aof
```

**基本写法：修复 AOF 文件**
`redis-check-aof --fix <file>`
```bash
# 修复 AOF 文件，截断损坏部分
redis-check-aof --fix appendonly.aof
```

---

## 配置优化

**基本写法：开启 AOF**
`appendonly yes`
```bash
# 开启 AOF 持久化
appendonly yes
```

**基本写法：设置 AOF 文件名**
`appendfilename <name>`
```bash
# 设置 AOF 文件名
appendfilename "appendonly.aof"
```

**基本写法：设置刷盘策略**
`appendfsync <strategy>`
```bash
# 设置刷盘策略为每秒
appendfsync everysec
```

**基本写法：设置自动重写增长百分比**
`auto-aof-rewrite-percentage <percentage>`
```bash
# 设置自动重写增长百分比为 100
auto-aof-rewrite-percentage 100
```

**基本写法：设置自动重写最小文件大小**
`auto-aof-rewrite-min-size <size>`
```bash
# 设置自动重写最小文件大小为 64MB
auto-aof-rewrite-min-size 64mb
```

**基本写法：重写期间禁止 fsync**
`no-appendfsync-on-rewrite <yes|no>`
```bash
# AOF 重写期间不执行 fsync
no-appendfsync-on-rewrite yes
```

**基本写法：加载时忽略不完整命令**
`aof-load-truncated <yes|no>`
```bash
# 加载时忽略最后一条不完整命令
aof-load-truncated yes
```

**基本写法：设置 AOF 文件存储目录**
`dir <path>`
```bash
# 设置 AOF 文件存储目录
dir /var/lib/redis
```



<!-- ============ 文档分隔线：022-redis/009-LuaScriptAtomicExecution.md ============ -->

﻿# Lua 脚本原子执行

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## EVAL 命令

**基本写法：执行 Lua 脚本**
`EVAL <script> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 执行简单的 GET + SET 脚本
EVAL "redis.call('SET', KEYS[1], ARGV[1]); return 'OK'" 1 mykey myvalue
```

**基本写法：原子性限流器**
`EVAL <script> 1 <key> <expire> <limit>`
```bash
# 使用 Lua 脚本实现原子性限流器
EVAL "local count = redis.call('INCR', KEYS[1]) if count == 1 then redis.call('EXPIRE', KEYS[1], ARGV[1]) end if count > tonumber(ARGV[2]) then return 0 end return 1" 1 rate_limit:user1 60 100
```

---

## redis.call 与 redis.pcall

**基本写法：redis.call 错误时脚本终止**
`redis.call(<command>, <args>)`
```lua
-- redis.call 遇到错误时脚本终止
local val = redis.call('INCR', 'non_numeric_key')
```

**基本写法：redis.pcall 错误时返回错误表**
`redis.pcall(<command>, <args>)`
```lua
-- redis.pcall 遇到错误时返回错误表，脚本继续执行
local result = redis.pcall('INCR', 'non_numeric_key')
if type(result) == 'table' and result.err then
    redis.call('SET', 'error_log', result.err)
end
```

---

## EVALSHA 与脚本缓存

**基本写法：加载脚本到缓存**
`SCRIPT LOAD <script>`
```bash
# 加载脚本到缓存，返回 SHA1 校验和
SCRIPT LOAD "return redis.call('GET', KEYS[1])"
```

**基本写法：使用 SHA1 执行缓存脚本**
`EVALSHA <sha1> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 使用 SHA1 执行已缓存的脚本
EVALSHA a1b2c3d4e5f6 1 mykey
```

**单脚本写法：检查单个脚本是否在缓存中**
`SCRIPT EXISTS <sha1>`
```bash
# 检查单个脚本是否在缓存中
SCRIPT EXISTS a1b2c3d4e5f6
```

**多脚本写法：检查多个脚本是否在缓存中**
`SCRIPT EXISTS <sha1> [sha1 ...]`
```bash
# 检查多个脚本是否在缓存中
SCRIPT EXISTS a1b2c3d4e5f6 f7g8h9i0j1k2
```

**基本写法：清空脚本缓存**
`SCRIPT FLUSH`
```bash
# 清空所有脚本缓存
SCRIPT FLUSH
```

**基本写法：同步清空脚本缓存**
`SCRIPT FLUSH SYNC`
```bash
# 同步方式清空脚本缓存（Redis 7.0+）
SCRIPT FLUSH SYNC
```

**基本写法：异步清空脚本缓存**
`SCRIPT FLUSH ASYNC`
```bash
# 异步方式清空脚本缓存（Redis 7.0+）
SCRIPT FLUSH ASYNC
```

**基本写法：Python EVALSHA 自动降级**
`r.register_script(<script>)`
```python
# Python redis-py 自动处理 EVAL 到 EVALSHA 的降级
import redis
r = redis.Redis()

script = r.register_script("""
    local stock = tonumber(redis.call('GET', KEYS[1]))
    if stock and stock > 0 then
        redis.call('DECR', KEYS[1])
        return 1
    end
    return 0
""")
result = script(keys=['stock:item1'])
```

---

## Lua 沙箱限制

**基本写法：调用 Redis 命令**
`redis.call(<command>, <args>)`
```lua
-- 在 Lua 脚本中调用 Redis 命令
redis.call('SET', 'key', 'value')
```

**基本写法：安全模式调用 Redis 命令**
`redis.pcall(<command>, <args>)`
```lua
-- 安全模式调用 Redis 命令，错误时不终止脚本
redis.pcall('GET', 'key')
```

**基本写法：写日志**
`redis.log(<level>, <message>)`
```lua
-- 在 Lua 脚本中写日志
redis.log(redis.LOG_WARNING, 'something went wrong')
```

**基本写法：SHA1 计算**
`redis.sha1hex(<string>)`
```lua
-- 计算字符串的 SHA1 哈希值
local hash = redis.sha1hex('hello')
```

**基本写法：构造状态回复**
`redis.status_reply(<message>)`
```lua
-- 构造状态回复
return redis.status_reply('OK')
```

**基本写法：构造错误回复**
`redis.error_reply(<message>)`
```lua
-- 构造错误回复
return redis.error_reply('something went wrong')
```

**基本写法：JSON 编码**
`cjson.encode(<value>)`
```lua
-- 将 Lua 表编码为 JSON 字符串
local json_str = cjson.encode({name='redis', version=7})
```

**基本写法：JSON 解码**
`cjson.decode(<json_string>)`
```lua
-- 将 JSON 字符串解码为 Lua 表
local data = cjson.decode('{"name":"redis","version":7}')
```

**基本写法：MessagePack 编码**
`cmsgpack.pack(<value>)`
```lua
-- 将 Lua 表编码为 MessagePack 二进制
local packed = cmsgpack.pack({1, 2, 3})
```

**基本写法：MessagePack 解码**
`cmsgpack.unpack(<packed_string>)`
```lua
-- 将 MessagePack 二进制解码为 Lua 表
local data = cmsgpack.unpack(packed_string)
```

**禁止写法：系统调用**
`os.execute(<command>)`
```lua
-- 沙箱禁止系统调用
os.execute('rm -rf /')
```

**禁止写法：文件操作**
`io.open(<path>)`
```lua
-- 沙箱禁止文件操作
io.open('/etc/passwd')
```

**禁止写法：加载模块**
`require(<module>)`
```lua
-- 沙箱禁止加载外部模块
require('socket')
```

**基本写法：设置脚本最大执行时间**
`lua-time-limit <ms>`
```bash
# 配置 Lua 脚本最大执行时间为5000毫秒
lua-time-limit 5000
```

**基本写法：复制所有写命令（默认）**
`redis.set_repl(redis.REPL_ALL)`
```lua
-- 默认行为，复制所有写命令到从节点
redis.set_repl(redis.REPL_ALL)
```

**基本写法：不复制写命令**
`redis.set_repl(redis.REPL_NONE)`
```lua
-- 不复制写命令到从节点
redis.set_repl(redis.REPL_NONE)
```

---

## 实战模式

**基本写法：分布式锁释放**
`EVAL <script> 1 <lock_key> <lock_value>`
```bash
# 原子性检查并释放分布式锁
EVAL "if redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('DEL', KEYS[1]) end return 0" 1 lock:resource1 my_token
```

**基本写法：滑动窗口限流器**
`EVAL <script> 1 <key> <limit> <window> <now>`
```bash
# 基于 ZSET 实现滑动窗口限流
EVAL "local key = KEYS[1] local limit = tonumber(ARGV[1]) local window = tonumber(ARGV[2]) local now = tonumber(ARGV[3]) redis.call('ZREMRANGEBYSCORE', key, 0, now - window) local count = redis.call('ZCARD', key) if count < limit then redis.call('ZADD', key, now, now .. '-' .. math.random(1000000)) redis.call('PEXPIRE', key, window) return 1 end return 0" 1 rate_limit:user1 100 60000 1718334600000
```

**基本写法：库存扣减**
`EVAL <script> 2 <stock_key> <user_key> <user_id> <quantity>`
```bash
# 原子性检查库存并扣减
EVAL "local stock_key = KEYS[1] local user_key = KEYS[2] local user_id = ARGV[1] local quantity = tonumber(ARGV[2]) if redis.call('SISMEMBER', user_key, user_id) == 1 then return -1 end local stock = tonumber(redis.call('GET', stock_key)) if not stock or stock < quantity then return 0 end redis.call('DECRBY', stock_key, quantity) redis.call('SADD', user_key, user_id) return 1" 2 stock:item1 users:item1 user42 1
```



<!-- ============ 文档分隔线：022-redis/010-RDBSnapshotPersistence.md ============ -->

# RDB 快照持久化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## save 命令

**基本写法：阻塞方式生成 RDB 文件**
`SAVE`
```bash
# 阻塞方式生成 RDB 文件，主进程无法响应请求
SAVE
```

---

## bgsave 命令

**基本写法：后台子进程生成 RDB 文件**
`BGSAVE`
```bash
# 后台方式生成 RDB 文件（生产推荐）
BGSAVE
```

**基本写法：查看最近一次保存时间**
`LASTSAVE`
```bash
# 返回最近一次成功保存的 Unix 时间戳
LASTSAVE
```

**基本写法：查看 RDB 统计信息**
`INFO Persistence`
```bash
# 查看 rdb 相关统计信息
INFO Persistence
```

---

## 写时复制（COW）

**基本写法：fork 创建子进程共享内存**
`fork()`
```c
// fork() 创建子进程后，父子进程共享同一块物理内存页
// 父进程页表 → 物理页 A (只读)
// 子进程页表 → 物理页 A (只读)
```

**基本写法：父进程修改页时触发 COW**
`fork() → 父进程写入 → 复制页`
```c
// 父进程修改页 A 时，操作系统复制一份新页
// 父进程页表 → 物理页 A' (可写) ← 新副本
// 子进程页表 → 物理页 A  (只读) ← 原始数据
```

**基本写法：COW 额外内存估算**
`COW 额外内存 ≈ 修改页数 × 页大小`
```c
// Linux 默认页大小为 4KB
// 假设 bgsave 耗时 5 秒，每秒写入 10 万个 key，每个 key 平均 100 字节
// 修改页数 ≈ (5 × 100000 × 100) / 4096 ≈ 12207 页
// COW 额外内存 ≈ 12207 × 4KB ≈ 48MB
```

---

## 自动触发配置

**基本写法：配置自动触发条件**
`save <seconds> <changes>`
```bash
# 900秒内有至少1个key被修改时触发
save 900 1
```

**多条件写法：配置多个自动触发条件**
`save <seconds> <changes>`
```bash
# 配置多个触发条件，满足任意一个即触发 bgsave
save 900 1
save 300 10
save 60 10000
```

**基本写法：禁用自动 RDB**
`save ""`
```bash
# 禁用自动 RDB 快照
save ""
```

**基本写法：运行时修改 save 配置**
`CONFIG SET save "<config>"`
```bash
# 运行时修改 save 配置
CONFIG SET save "900 1 300 10 60 10000"
```

---

## RDB 文件格式

**基本写法：RDB 文件整体结构**
`[REDIS][version][databases][EOF][checksum]`
```c
// RDB 文件采用二进制格式
// 魔数 → 版本号 → 数据库数据 → 结束标记 → 校验和
```

**基本写法：数据库区域结构**
`[SELECTDB][key-value对(带过期时间)][key-value对(无过期时间)]`
```c
// 各数据库区域结构
// 数据库编号 → key-value对(带过期时间) → key-value对(无过期时间)
```

---

## RDB 文件恢复

**基本写法：配置 RDB 文件路径**
`dir <path>`
```bash
# 设置 RDB 文件存储目录
dir /var/lib/redis
```

**基本写法：配置 RDB 文件名**
`dbfilename <name>`
```bash
# 设置 RDB 文件名
dbfilename dump.rdb
```

**基本写法：校验 RDB 文件**
`redis-check-rdb <file>`
```bash
# 使用 redis-check-rdb 工具校验文件
redis-check-rdb dump.rdb
```

---

## 配置优化

**基本写法：设置 RDB 文件名**
`dbfilename <name>`
```bash
# 设置 RDB 文件名
dbfilename dump.rdb
```

**基本写法：设置存储目录**
`dir <path>`
```bash
# 设置 RDB 文件存储目录
dir /var/lib/redis
```

**基本写法：开启 LZF 压缩**
`rdbcompression <yes|no>`
```bash
# 开启 RDB 文件 LZF 压缩
rdbcompression yes
```

**基本写法：开启 CRC64 校验**
`rdbchecksum <yes|no>`
```bash
# 开启 RDB 文件 CRC64 校验
rdbchecksum yes
```

**基本写法：bgsave 失败时停止写入**
`stop-writes-on-bgsave-error <yes|no>`
```bash
# bgsave 失败时停止接受写入
stop-writes-on-bgsave-error yes
```



<!-- ============ 文档分隔线：022-redis/011-StringCommand.md ============ -->

# Redis String 命令速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本读写

**基本写法：SET 设置键值**
`SET <key> <value> [EX <秒>] [PX <毫秒>] [NX|XX]`
```bash
# 设置键值并设置 60 秒过期
SET user:name zhangsan EX 60
```

**基本写法：SET NX 仅键不存在时设置**
`SET <key> <value> NX`
```bash
# 仅当键不存在时设置（分布式锁基础）
SET lock:resource my_token NX EX 30
```

**基本写法：SET XX 仅键存在时设置**
`SET <key> <value> XX`
```bash
# 仅当键已存在时更新值
SET counter 100 XX
```

**基本写法：GET 获取值**
`GET <key>`
```bash
# 获取键的值
GET user:name
```

**基本写法：GETSET 获取并设置新值**
`GETSET <key> <value>`
```bash
# 返回旧值并设置新值
GETSET counter 200
```

**基本写法：GETDEL 获取并删除**
`GETDEL <key>`
```bash
# 返回值并删除键
GETDEL temp:key
```

**基本写法：GETEX 获取并设置过期**
`GETEX <key> [EX <秒> | PX <毫秒> | PERSIST]`
```bash
# 获取值并设置 60 秒过期
GETEX session:token EX 60
```

---

## 批量操作

**基本写法：MSET 批量设置**
`MSET <key1> <value1> <key2> <value2> [key value ...]`
```bash
# 原子批量设置多个键值
MSET user:1:name zhangsan user:1:age 25
```

**基本写法：MGET 批量获取**
`MGET <key1> <key2> [key ...]`
```bash
# 批量获取多个键的值
MGET user:1:name user:1:age
```

**基本写法：MSETNX 批量不存在时设置**
`MSETNX <key1> <value1> <key2> <value2> [key value ...]`
```bash
# 所有键都不存在时才批量设置
MSETNX user:2:name lisi user:2:age 30
```

---

## 计数操作

**基本写法：INCR 自增 1**
`INCR <key>`
```bash
# 键值自增 1
INCR page:views
```

**基本写法：DECR 自减 1**
`DECR <key>`
```bash
# 键值自减 1
DECR stock:item:1001
```

**基本写法：INCRBY 指定步长自增**
`INCRBY <key> <增量>`
```bash
# 增加指定数值
INCRBY score 10
```

**基本写法：DECRBY 指定步长自减**
`DECRBY <key> <减量>`
```bash
# 减少指定数值
DECRBY stock:item:1001 5
```

**基本写法：INCRBYFLOAT 浮点自增**
`INCRBYFLOAT <key> <增量>`
```bash
# 浮点数自增
INCRBYFLOAT price:gold 0.05
```

---

## 字符串操作

**基本写法：APPEND 追加字符串**
`APPEND <key> <value>`
```bash
# 在原值后追加内容
APPEND log:today " new entry"
```

**基本写法：STRLEN 获取长度**
`STRLEN <key>`
```bash
# 获取值的字节长度
STRLEN user:name
```

**基本写法：GETRANGE 获取子串**
`GETRANGE <key> <起始> <结束>`
```bash
# 获取指定范围的子串
GETRANGE user:name 0 4
```

**基本写法：SETRANGE 覆盖子串**
`SETRANGE <key> <偏移> <值>`
```bash
# 从指定偏移覆盖字符串
SETRANGE user:name 0 "Hello"
```

---

## 过期时间

**基本写法：SETEX 设置带过期的值**
`SETEX <key> <秒> <value>`
```bash
# 设置键值并指定秒级过期
SETEX code:sms 300 123456
```

**基本写法：PSETEX 毫秒级过期**
`PSETEX <key> <毫秒> <value>`
```bash
# 设置键值并指定毫秒级过期
PSETEX token:temp 60000 abc123
```

**基本写法：EXPIRE 设置过期**
`EXPIRE <key> <秒>`
```bash
# 给已有键设置过期时间
EXPIRE user:session 1800
```

**基本写法：PEXPIRE 毫秒过期**
`PEXPIRE <key> <毫秒>`
```bash
# 毫秒级过期时间
PEXPIRE user:session 1800000
```

**基本写法：EXPIREAT 指定过期时间戳**
`EXPIREAT <key> <Unix时间戳>`
```bash
# 设置键在指定时间戳过期
EXPIREAT coupon:123 1735689600
```

**基本写法：TTL 查看剩余秒数**
`TTL <key>`
```bash
# 查看键剩余存活秒数（-1 永久 -2 已过期）
TTL user:session
```

**基本写法：PTTL 查看剩余毫秒**
`PTTL <key>`
```bash
# 查看键剩余存活毫秒数
PTTL user:session
```

**基本写法：PERSIST 移除过期**
`PERSIST <key>`
```bash
# 移除过期时间使键永久有效
PERSIST user:session
```

---

## 位操作

**基本写法：SETBIT 设置位**
`SETBIT <key> <偏移> <0|1>`
```bash
# 设置指定偏移的位
SETBIT user:online 100 1
```

**基本写法：GETBIT 获取位**
`GETBIT <key> <偏移>`
```bash
# 获取指定偏移的位
GETBIT user:online 100
```

**基本写法：BITCOUNT 统计位数**
`BITCOUNT <key> [start end]`
```bash
# 统计值为 1 的位数
BITCOUNT user:online
```

**基本写法：BITOP 位运算**
`BITOP <AND|OR|XOR|NOT> <destkey> <key> [key ...]`
```bash
# 对多个键执行位运算存入目标键
BITOP AND result:online today:yesterday today:now
```

**基本写法：BITPOS 查找位**
`BITPOS <key> <0|1> [start end]`
```bash
# 查找第一个 0 或 1 的位置
BITPOS user:online 1
```

---

## 实用模式

**基本写法：分布式锁**
`SET <lock_key> <token> NX PX <毫秒>`
```bash
# 原子性获取分布式锁
SET lock:order:1001 my_token NX PX 30000
```

**基本写法：限流计数器**
`INCR <rate_limit:用户> 配合 EXPIRE`
```bash
# 简单限流器（每分钟最多 100 次）
INCR rate_limit:user1
# 若返回 1 则设置过期
EXPIRE rate_limit:user1 60
```

**基本写法：序列号生成器**
`INCR <seq:订单>`
```bash
# 生成自增订单号
INCR seq:order:20240101
```

**基本写法：缓存穿透防护**
`SET <cache_null_key> "" EX <短过期>`
```bash
# 缓存空值防止缓存穿透
SET cache:user:null "" EX 60
```



<!-- ============ 文档分隔线：022-redis/012-HashCommand.md ============ -->

# Redis Hash 命令速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：022-redis/013-ListSetZSetCommand.md ============ -->

# Redis List/Set/ZSet 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## List 列表

**基本写法：LPUSH 左侧插入**
`LPUSH <key> <value1> [value2 ...]`
```bash
# 在列表头部插入元素
LPUSH messages "hello" "world"
```

**基本写法：RPUSH 右侧插入**
`RPUSH <key> <value1> [value2 ...]`
```bash
# 在列表尾部插入元素
RPUSH queue:tasks task1 task2
```

**基本写法：LPOP 左侧弹出**
`LPOP <key> [count]`
```bash
# 从列表头部弹出元素
LPOP queue:tasks
```

**基本写法：RPOP 右侧弹出**
`RPOP <key> [count]`
```bash
# 从列表尾部弹出元素
RPOP queue:tasks
```

**基本写法：LRANGE 获取范围**
`LRANGE <key> <start> <stop>`
```bash
# 获取列表指定范围元素（0 到 -1 为全部）
LRANGE messages 0 -1
```

**基本写法：LINDEX 按索引获取**
`LINDEX <key> <索引>`
```bash
# 获取指定索引位置的元素
LINDEX messages 0
```

**基本写法：LLEN 获取长度**
`LLEN <key>`
```bash
# 获取列表长度
LLEN messages
```

**基本写法：LINSERT 插入元素**
`LINSERT <key> BEFORE|AFTER <pivot> <value>`
```bash
# 在指定元素前或后插入
LINSERT messages BEFORE "world" "new"
```

**基本写法：LREM 删除指定元素**
`LREM <key> <count> <value>`
```bash
# 删除指定数量的匹配元素
LREM messages 2 "hello"
```

**基本写法：LTRIM 修剪列表**
`LTRIM <key> <start> <stop>`
```bash
# 仅保留指定范围元素
LTRIM messages 0 99
```

**基本写法：LSET 修改元素**
`LSET <key> <索引> <value>`
```bash
# 修改指定索引位置的元素
LSET messages 0 "updated"
```

**基本写法：RPOPLPUSH 转移元素**
`RPOPLPUSH <源> <目标>`
```bash
# 从源列表尾部弹出并插入目标列表头部
RPOPLPUSH queue:pending queue:processing
```

**基本写法：LMOVE 转移元素（替代 RPOPLPUSH）**
`LMOVE <源> <目标> <LEFT|RIGHT> <LEFT|RIGHT>`
```bash
# 灵活指定源和目标的弹出插入方向
LMOVE queue:pending queue:processing LEFT RIGHT
```

**基本写法：BLPOP 阻塞弹出**
`BLPOP <key> [key ...] <超时>`
```bash
# 阻塞式左侧弹出（0 表示永久阻塞）
BLPOP queue:tasks 30
```

**基本写法：BRPOP 阻塞弹出**
`BRPOP <key> [key ...] <超时>`
```bash
# 阻塞式右侧弹出
BRPOP queue:tasks 30
```

---

## Set 集合

**基本写法：SADD 添加元素**
`SADD <key> <member1> [member2 ...]`
```bash
# 向集合添加元素
SADD tags:article:1 redis mysql postgresql
```

**基本写法：SREM 删除元素**
`SREM <key> <member1> [member2 ...]`
```bash
# 从集合删除元素
SREM tags:article:1 mysql
```

**基本写法：SMEMBERS 获取所有元素**
`SMEMBERS <key>`
```bash
# 获取集合所有元素
SMEMBERS tags:article:1
```

**基本写法：SISMEMBER 判断成员存在**
`SISMEMBER <key> <member>`
```bash
# 判断元素是否在集合中
SISMEMBER tags:article:1 redis
```

**基本写法：SMISMEMBER 批量判断**
`SMISMEMBER <key> <member1> [member2 ...]`
```bash
# 批量判断多个元素是否存在
SMISMEMBER tags:article:1 redis mysql mongodb
```

**基本写法：SCARD 获取集合大小**
`SCARD <key>`
```bash
# 获取集合元素数量
SCARD tags:article:1
```

**基本写法：SRANDMEMBER 随机获取**
`SRANDMEMBER <key> [count]`
```bash
# 随机获取元素不删除
SRANDMEMBER tags:article:1 2
```

**基本写法：SPOP 随机弹出**
`SPOP <key> [count]`
```bash
# 随机弹出元素并删除
SPOP lucky:draw 1
```

**基本写法：SMOVE 转移元素**
`SMOVE <源> <目标> <member>`
```bash
# 将元素从一个集合转移到另一个
SMOVE set:old set:new member1
```

---

## Set 集合运算

**基本写法：SINTER 交集**
`SINTER <key1> [key2 ...]`
```bash
# 获取多个集合的交集
SINTER tags:article:1 tags:article:2
```

**基本写法：SUNION 并集**
`SUNION <key1> [key2 ...]`
```bash
# 获取多个集合的并集
SUNION tags:article:1 tags:article:2
```

**基本写法：SDIFF 差集**
`SDIFF <key1> [key2 ...]`
```bash
# 获取第一个集合与其他集合的差集
SDIFF tags:article:1 tags:article:2
```

**基本写法：SINTERSTORE 交集存储**
`SINTERSTORE <目标> <key1> [key2 ...]`
```bash
# 将交集结果存储到新集合
SINTERSTORE common:tags tags:article:1 tags:article:2
```

**基本写法：SUNIONSTORE 并集存储**
`SUNIONSTORE <目标> <key1> [key2 ...]`
```bash
# 将并集结果存储到新集合
SUNIONSTORE all:tags tags:article:1 tags:article:2
```

**基本写法：SDIFFSTORE 差集存储**
`SDIFFSTORE <目标> <key1> [key2 ...]`
```bash
# 将差集结果存储到新集合
SDIFFSTORE diff:tags tags:article:1 tags:article:2
```

**基本写法：SINTERCARD 交集数量（7.0+）**
`SINTERCARD <numkeys> <key1> [key2 ...] [LIMIT <数量>]`
```bash
# 仅返回交集元素数量不返回具体元素
SINTERCARD 2 tags:article:1 tags:article:2
```

---

## Sorted Set 有序集合

**基本写法：ZADD 添加元素**
`ZADD <key> [NX|XX] [GT|LT] [CH] [INCR] <score1> <member1> [score2 member2 ...]`
```bash
# 添加带分数的元素
ZADD leaderboard 100 user:1 90 user:2 80 user:3
```

**基本写法：ZADD 仅更新已存在元素**
`ZADD <key> XX <score> <member>`
```bash
# 仅更新已存在成员的分数
ZADD leaderboard XX 95 user:2
```

**基本写法：ZADD 仅新增不更新**
`ZADD <key> NX <score> <member>`
```bash
# 仅添加新成员不更新已有成员
ZADD leaderboard NX 85 user:4
```

**基本写法：ZSCORE 获取分数**
`ZSCORE <key> <member>`
```bash
# 获取成员的分数
ZSCORE leaderboard user:1
```

**基本写法：ZMSCORE 批量获取分数**
`ZMSCORE <key> <member1> [member2 ...]`
```bash
# 批量获取多个成员分数
ZMSCORE leaderboard user:1 user:2 user:3
```

**基本写法：ZRANK 升序排名**
`ZRANK <key> <member>`
```bash
# 获取成员升序排名（0 为最小）
ZRANK leaderboard user:1
```

**基本写法：ZREVRANK 降序排名**
`ZREVRANK <key> <member>`
```bash
# 获取成员降序排名（0 为最大）
ZREVRANK leaderboard user:1
```

**基本写法：ZRANGE 按索引范围获取**
`ZRANGE <key> <start> <stop> [WITHSCORES]`
```bash
# 按升序获取索引范围元素
ZRANGE leaderboard 0 9 WITHSCORES
```

**基本写法：ZREVRANGE 降序范围获取**
`ZREVRANGE <key> <start> <stop> [WITHSCORES]`
```bash
# 按降序获取索引范围元素
ZREVRANGE leaderboard 0 9 WITHSCORES
```

**基本写法：ZRANGEBYSCORE 按分数范围获取**
`ZRANGEBYSCORE <key> <min> <max> [WITHSCORES] [LIMIT offset count]`
```bash
# 获取分数范围内的元素
ZRANGEBYSCORE leaderboard 80 100 WITHSCORES LIMIT 0 10
```

**基本写法：ZREVRANGEBYSCORE 降序按分数获取**
`ZREVRANGEBYSCORE <key> <max> <min> [WITHSCORES] [LIMIT offset count]`
```bash
# 降序获取分数范围内的元素
ZREVRANGEBYSCORE leaderboard 100 80 WITHSCORES LIMIT 0 10
```

**基本写法：ZRANGEBYSCORE 使用无穷大**
`ZRANGEBYSCORE <key> -inf +inf [WITHSCORES]`
```bash
# 获取全部元素
ZRANGEBYSCORE leaderboard -inf +inf WITHSCORES
```

**基本写法：ZINCRBY 增加分数**
`ZINCRBY <key> <增量> <member>`
```bash
# 增加成员分数
ZINCRBY leaderboard 5 user:1
```

**基本写法：ZREM 删除元素**
`ZREM <key> <member1> [member2 ...]`
```bash
# 删除有序集合元素
ZREM leaderboard user:3
```

**基本写法：ZREMRANGEBYRANK 按排名删除**
`ZREMRANGEBYRANK <key> <start> <stop>`
```bash
# 按排名范围删除元素
ZREMRANGEBYRANK leaderboard 0 9
```

**基本写法：ZREMRANGEBYSCORE 按分数删除**
`ZREMRANGEBYSCORE <key> <min> <max>`
```bash
# 按分数范围删除元素
ZREMRANGEBYSCORE leaderboard 0 60
```

**基本写法：ZCARD 获取元素数量**
`ZCARD <key>`
```bash
# 获取有序集合元素总数
ZCARD leaderboard
```

**基本写法：ZCOUNT 按分数统计数量**
`ZCOUNT <key> <min> <max>`
```bash
# 统计指定分数范围内的元素数量
ZCOUNT leaderboard 80 100
```

---

## ZSet 集合运算

**基本写法：ZUNIONSTORE 并集存储**
`ZUNIONSTORE <目标> <numkeys> <key> [key ...] [WEIGHTS <权重>...] [AGGREGATE SUM|MIN|MAX]`
```bash
# 多个有序集合并集并按 SUM 聚合分数
ZUNIONSTORE total:score 2 score:week1 score:week2 AGGREGATE SUM
```

**基本写法：ZINTERSTORE 交集存储**
`ZINTERSTORE <目标> <numkeys> <key> [key ...] [WEIGHTS <权重>...] [AGGREGATE SUM|MIN|MAX]`
```bash
# 多个有序集合交集并按 MAX 聚合分数
ZINTERSTORE common:high 2 set1 set2 AGGREGATE MAX
```

**基本写法：ZDIFFSTORE 差集存储**
`ZDIFFSTORE <目标> <numkeys> <key> [key ...]`
```bash
# 多个有序集合差集存储
ZDIFFSTORE diff:set 2 set1 set2
```

**基本写法：ZUNION 并集返回（7.0+）**
`ZUNION <numkeys> <key> [key ...] [WITHSCORES]`
```bash
# 直接返回并集结果不存储
ZUNION 2 set1 set2 WITHSCORES
```

**基本写法：ZINTER 交集返回（7.0+）**
`ZINTER <numkeys> <key> [key ...] [WITHSCORES]`
```bash
# 直接返回交集结果不存储
ZINTER 2 set1 set2 WITHSCORES
```

---

## 实用模式

**基本写法：消息队列（List）**
`LPUSH <queue> <message> 配合 BRPOP`
```bash
# 生产者推送消息
LPUSH queue:email "send to user1"
# 消费者阻塞获取消息
BRPOP queue:email 30
```

**基本写法：排行榜（ZSet）**
`ZADD <rank> <score> <member> 配合 ZREVRANGE`
```bash
# 更新用户积分
ZADD rank:game 1500 user:1
# 获取前 10 名
ZREVRANGE rank:game 0 9 WITHSCORES
```

**基本写法：共同关注（Set）**
`SINTER <user1:follow> <user2:follow>`
```bash
# 获取两个用户的共同关注
SINTER user:1:follow user:2:follow
```

**基本写法：延迟队列（ZSet）**
`ZADD <delay:queue> <执行时间戳> <任务>`
```bash
# 添加延迟任务到队列
ZADD delay:queue 1718334600000 task:1001
# 扫描到期任务
ZRANGEBYSCORE delay:queue 0 1718334600000 LIMIT 0 100
```

**基本写法：滑动窗口限流（ZSet）**
`ZADD <rate:key> <时间戳> <唯一标识> 配合 ZREMRANGEBYSCORE`
```bash
# 滑动窗口限流记录请求
ZADD rate:user1 1718334600000 req-1
# 清理窗口外的记录
ZREMRANGEBYSCORE rate:user1 0 1718334540000
# 获取窗口内请求数
ZCARD rate:user1
```



<!-- ============ 文档分隔线：022-redis/014-PubSubCommand.md ============ -->

# Redis 发布订阅命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 订阅命令

**基本写法：SUBSCRIBE 订阅频道**
`SUBSCRIBE <channel> [channel ...]`
```bash
# 订阅指定频道（阻塞式）
SUBSCRIBE news:tech news:sports
```

**基本写法：UNSUBSCRIBE 取消订阅**
`UNSUBSCRIBE [channel ...]`
```bash
# 取消订阅指定频道（不指定则取消全部）
UNSUBSCRIBE news:tech
```

**基本写法：PSUBSCRIBE 模式订阅**
`PSUBSCRIBE <pattern> [pattern ...]`
```bash
# 按模式订阅频道
PSUBSCRIBE news:*
```

**基本写法：PUNSUBSCRIBE 取消模式订阅**
`PUNSUBSCRIBE [pattern ...]`
```bash
# 取消模式订阅
PUNSUBSCRIBE news:*
```

---

## 发布命令

**基本写法：PUBLISH 发布消息**
`PUBLISH <channel> <message>`
```bash
# 向指定频道发布消息
PUBLISH news:tech "Redis 7.4 released"
```

---

## 查询命令

**基本写法：PUBSUB CHANNELS 查看活跃频道**
`PUBSUB CHANNELS [pattern]`
```bash
# 查看当前有订阅者的频道
PUBSUB CHANNELS news:*
```

**基本写法：PUBSUB NUMSUB 查看频道订阅数**
`PUBSUB NUMSUB [channel ...]`
```bash
# 查看指定频道的订阅者数量
PUBSUB NUMSUB news:tech news:sports
```

**基本写法：PUBSUB NUMPAT 查看模式订阅数**
`PUBSUB NUMPAT`
```bash
# 查看所有模式订阅的总数
PUBSUB NUMPAT
```

**基本写法：PUBSUB SHARDCHANNELS 查看分片频道（7.0+）**
`PUBSUB SHARDCHANNELS [pattern]`
```bash
# 查看集群分片频道
PUBSUB SHARDCHANNELS
```

**基本写法：PUBSUB SHARDNUMSUB 查看分片频道订阅数（7.0+）**
`PUBSUB SHARDNUMSUB [channel ...]`
```bash
# 查看分片频道的订阅者数量
PUBSUB SHARDNUMSUB shard:channel1
```

---

## Stream 消息队列

**基本写法：XADD 添加消息**
`XADD <key> [NOMKSTREAM] [MAXLEN|MINID [=|~] <阈值>] <ID> <field> <value> [field value ...]`
```bash
# 添加消息到流（* 表示自动生成 ID）
XADD stream:orders * order_id 1001 user_id 1 amount 99.9
```

**基本写法：XADD 限制流长度**
`XADD <key> MAXLEN <数量> * <field> <value>`
```bash
# 仅保留最近 1000 条消息
XADD stream:logs MAXLEN 1000 * level ERROR msg "something wrong"
```

**基本写法：XADD 近似限制长度**
`XADD <key> MAXLEN ~ <数量> * <field> <value>`
```bash
# 近似限制长度性能更好
XADD stream:logs MAXLEN ~ 1000 * level INFO msg "ok"
```

**基本写法：XLEN 获取流长度**
`XLEN <key>`
```bash
# 获取流中消息数量
XLEN stream:orders
```

**基本写法：XRANGE 按范围查询**
`XRANGE <key> <start> <end> [COUNT <数量>]`
```bash
# 查询全部消息（- 到 +）
XRANGE stream:orders - + COUNT 10
```

**基本写法：XREVRANGE 反向查询**
`XREVRANGE <key> <end> <start> [COUNT <数量>]`
```bash
# 倒序查询最新 10 条
XREVRANGE stream:orders + - COUNT 10
```

**基本写法：XREAD 读取消息**
`XREAD [COUNT <数量>] [BLOCK <毫秒>] STREAMS <key> [key ...] <ID> [ID ...]`
```bash
# 读取大于指定 ID 的新消息
XREAD COUNT 10 STREAMS stream:orders 0
```

**基本写法：XREAD 阻塞读取**
`XREAD BLOCK <毫秒> STREAMS <key> <ID>`
```bash
# 阻塞式等待新消息（0 永久阻塞）
XREAD BLOCK 0 STREAMS stream:orders $
```

---

## 消费者组

**基本写法：XGROUP CREATE 创建消费者组**
`XGROUP CREATE <key> <group> <ID> [MKSTREAM]`
```bash
# 创建消费者组从头部开始消费
XGROUP CREATE stream:orders group1 0 MKSTREAM
```

**基本写法：XGROUP CREATE 从最新开始**
`XGROUP CREATE <key> <group> $`
```bash
# 创建消费者组仅消费新消息
XGROUP CREATE stream:orders group2 $
```

**基本写法：XREADGROUP 消费组读取**
`XREADGROUP GROUP <group> <consumer> [COUNT <数量>] [BLOCK <毫秒>] STREAMS <key> <ID>`
```bash
# 消费者读取消息（> 表示未投递过的新消息）
XREADGROUP GROUP group1 consumer1 COUNT 10 STREAMS stream:orders >
```

**基本写法：XACK 确认消息**
`XACK <key> <group> <ID> [ID ...]`
```bash
# 确认消息已处理
XACK stream:orders group1 1718334600000-0
```

**基本写法：XPENDING 查看待处理消息**
`XPENDING <key> <group> [start end count] [consumer]`
```bash
# 查看待确认的消息列表
XPENDING stream:orders group1 - + 10
```

**基本写法：XCLAIM 转移消息归属**
`XCLAIM <key> <group> <consumer> <min-idle-time> <ID> [ID ...]`
```bash
# 转移超时未确认的消息给其他消费者
XCLAIM stream:orders group1 consumer2 60000 1718334600000-0
```

**基本写法：XAUTOCLAIM 自动转移（6.2+）**
`XAUTOCLAIM <key> <group> <consumer> <min-idle-time> <start> [COUNT <数量>]`
```bash
# 自动扫描并转移超时消息
XAUTOCLAIM stream:orders group1 consumer2 60000 0 COUNT 10
```

**基本写法：XINFO 查看流信息**
`XINFO STREAM <key> [FULL [COUNT <数量>]]`
```bash
# 查看流详细信息
XINFO STREAM stream:orders FULL
```

**基本写法：XINFO 查看消费者组**
`XINFO GROUPS <key>`
```bash
# 查看流的所有消费者组
XINFO GROUPS stream:orders
```

**基本写法：XINFO 查看消费者**
`XINFO CONSUMERS <key> <group>`
```bash
# 查看消费者组中的消费者
XINFO CONSUMERS stream:orders group1
```

**基本写法：XTRIM 修剪流**
`XTRIM <key> <MAXLEN|MINID> [=|~] <阈值>`
```bash
# 修剪流仅保留最近 1000 条
XTRIM stream:logs MAXLEN 1000
```

**基本写法：XDEL 删除消息**
`XDEL <key> <ID> [ID ...]`
```bash
# 删除指定 ID 的消息
XDEL stream:orders 1718334600000-0
```

---

## 实用模式

**基本写法：实时聊天室**
`PUBLISH <room:频道> <消息>`
```bash
# 发布聊天消息
PUBLISH room:1001 "user1: 你好"
# 订阅房间
SUBSCRIBE room:1001
```

**基本写法：事件通知**
`PUBLISH <event:类型> <JSON数据>`
```bash
# 发布事件通知
PUBLISH event:order.created '{"order_id":1001,"amount":99.9}'
```

**基本写法：可靠消息队列（Stream）**
`XADD <stream> * <field> <value> 配合 XREADGROUP 与 XACK`
```bash
# 生产者发送可靠消息
XADD stream:tasks * task_id 1001 payload "do something"
# 消费者组消费并确认
XREADGROUP GROUP workers worker1 COUNT 1 STREAMS stream:tasks >
XACK stream:tasks workers 1718334600000-0
```

**基本写法：多播通知**
`PUBLISH <broadcast:全局> <消息>`
```bash
# 全局广播消息
PUBLISH broadcast:all "system maintenance at 22:00"
PSUBSCRIBE broadcast:*
```



<!-- ============ 文档分隔线：022-redis/015-TransactionLua.md ============ -->

# Redis 事务与 Lua 脚本

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事务基础

**基本写法：MULTI 开启事务**
`MULTI`
```bash
# 开启事务标记后续命令入队
MULTI
```

**基本写法：EXEC 执行事务**
`EXEC`
```bash
# 顺序执行队列中的所有命令
EXEC
```

**基本写法：DISCARD 取消事务**
`DISCARD`
```bash
# 取消事务清空命令队列
DISCARD
```

**换行写法：完整事务流程**
`MULTI > <命令> > EXEC`
```bash
# 事务内执行多条命令
MULTI
SET user:1:name zhangsan
INCR seq:user
SET user:1:age 25
EXEC
```

---

## WATCH 乐观锁

**基本写法：WATCH 监视键**
`WATCH <key> [key ...]`
```bash
# 监视键，若被修改则事务执行失败
WATCH balance:user1
```

**基本写法：UNWATCH 取消监视**
`UNWATCH`
```bash
# 取消所有键的监视
UNWATCH
```

**换行写法：WATCH 实现乐观锁**
`WATCH <key> > MULTI > EXEC`
```bash
# 乐观锁扣减余额
WATCH balance:user1
val = GET balance:user1
MULTI
SET balance:user1 (val - 100)
EXEC
# 若 EXEC 返回 nil 表示键被修改需重试
```

**换行写法：WATCH 多个键**
`WATCH <key1> <key2> > MULTI > EXEC`
```bash
# 监视多个键的转账事务
WATCH balance:user1 balance:user2
MULTI
DECRBY balance:user1 100
INCRBY balance:user2 100
EXEC
```

---

## 事务注意点

**基本写法：命令语法错误整个事务失败**
`MULTI > <错误命令> > EXEC`
```bash
# 队列中存在语法错误时 EXEC 整体失败
MULTI
SET key value WRONGSYNTAX
EXEC
```

**基本写法：运行时错误部分失败**
`MULTI > <类型错误命令> > EXEC`
```bash
# 运行时类型错误仅该条失败其他仍执行
MULTI
SET str:key "hello"
INCR str:key
EXEC
```

---

## EVAL 执行 Lua 脚本

**基本写法：EVAL 执行脚本**
`EVAL <script> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 执行简单 Lua 脚本
EVAL "return redis.call('SET', KEYS[1], ARGV[1])" 1 mykey myvalue
```

**基本写法：EVAL 访问键与参数**
`EVAL <script> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 在脚本中使用 KEYS 和 ARGV
EVAL "return {KEYS[1], ARGV[1], ARGV[2]}" 1 key1 arg1 arg2
```

**换行写法：原子性 GETSET**
`EVAL "<script>" 1 <key> <value>`
```bash
# 原子性获取旧值并设置新值
EVAL "local old = redis.call('GET', KEYS[1]) redis.call('SET', KEYS[1], ARGV[1]) return old" 1 mykey newvalue
```

---

## redis.call 与 redis.pcall

**基本写法：redis.call 错误终止**
`redis.call(<command>, <args>)`
```lua
-- 错误时脚本立即终止并返回错误
local val = redis.call('GET', 'missing_key')
```

**基本写法：redis.pcall 错误返回表**
`redis.pcall(<command>, <args>)`
```lua
-- 错误时返回错误表脚本继续执行
local result = redis.pcall('INCR', 'non_numeric_key')
if type(result) == 'table' and result.err then
    redis.call('SET', 'error_log', result.err)
end
```

---

## EVALSHA 与脚本缓存

**基本写法：SCRIPT LOAD 加载脚本**
`SCRIPT LOAD <script>`
```bash
# 加载脚本到缓存返回 SHA1 校验和
SCRIPT LOAD "return redis.call('GET', KEYS[1])"
```

**基本写法：EVALSHA 执行缓存脚本**
`EVALSHA <sha1> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 使用 SHA1 执行已缓存脚本节省带宽
EVALSHA a1b2c3d4e5f6g7h8 1 mykey
```

**基本写法：SCRIPT EXISTS 检查缓存**
`SCRIPT EXISTS <sha1> [sha1 ...]`
```bash
# 检查脚本是否在缓存中
SCRIPT EXISTS a1b2c3d4e5f6g7h8
```

**基本写法：SCRIPT FLUSH 清空缓存**
`SCRIPT FLUSH [ASYNC|SYNC]`
```bash
# 清空所有脚本缓存（Redis 7.0+ 支持异步）
SCRIPT FLUSH ASYNC
```

**基本写法：SCRIPT KILL 终止脚本**
`SCRIPT KILL`
```bash
# 终止正在执行的脚本（仅未执行写命令时有效）
SCRIPT KILL
```

---

## FUNCTION 函数（7.0+）

**基本写法：FUNCTION LOAD 加载函数库**
`FUNCTION LOAD [REPLACE] <code>`
```bash
# 加载 Lua 函数库
FUNCTION LOAD "#!lua name=mylib
redis.register_function('myfunc', function(keys, args)
    return redis.call('GET', keys[1])
end)"
```

**基本写法：FCALL 调用函数**
`FCALL <function> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 调用已注册的函数
FCALL myfunc 1 mykey
```

**基本写法：FCALL_RO 只读调用**
`FCALL_RO <function> <numkeys> <key> [key ...] <arg> [arg ...]`
```bash
# 只读模式调用函数（禁止写命令）
FCALL_RO myfunc 1 mykey
```

**基本写法：FUNCTION LIST 查看函数库**
`FUNCTION LIST [LIBRARYNAME <pattern>]`
```bash
# 列出所有函数库
FUNCTION LIST
```

**基本写法：FUNCTION DELETE 删除函数库**
`FUNCTION DELETE <库名>`
```bash
# 删除指定函数库
FUNCTION DELETE mylib
```

**基本写法：FUNCTION FLUSH 清空所有函数**
`FUNCTION FLUSH [ASYNC|SYNC]`
```bash
# 清空所有函数库
FUNCTION FLUSH
```

---

## Lua 数据类型转换

**基本写法：Lua 到 Redis 类型映射**
`return <value>`
```lua
-- Lua 类型到 Redis 回复的映射
-- Lua number -> Redis integer reply
return 42
-- Lua string -> Redis bulk string reply
return "hello"
-- Lua table (array) -> Redis multi-bulk reply
return {1, 2, 3}
-- Lua boolean true -> Redis integer 1
return true
-- Lua boolean false -> Redis nil reply
return false
-- Lua nil -> Redis nil reply
return nil
```

**基本写法：false 作为 nil 处理（7.0+ 变化）**
`return false`
```lua
-- Redis 7.0+ false 与 nil 都返回 nil
return false
```

---

## Lua 内置库

**基本写法：cjson 编码**
`cjson.encode(<value>)`
```lua
-- 将 Lua 表编码为 JSON 字符串
local json = cjson.encode({name='redis', version=7})
```

**基本写法：cjson 解码**
`cjson.decode(<json>)`
```lua
-- 将 JSON 字符串解码为 Lua 表
local data = cjson.decode('{"name":"redis","version":7}')
```

**基本写法：cmsgpack 编码**
`cmsgpack.pack(<value>)`
```lua
-- 将 Lua 表编码为 MessagePack 二进制
local packed = cmsgpack.pack({1, 2, 3})
```

**基本写法：cmsgpack 解码**
`cmsgpack.unpack(<packed>)`
```lua
-- 将 MessagePack 二进制解码为 Lua 表
local data = cmsgpack.unpack(packed)
```

**基本写法：redis.sha1hex 计算 SHA1**
`redis.sha1hex(<string>)`
```lua
-- 计算字符串的 SHA1 哈希值
local hash = redis.sha1hex('hello')
```

**基本写法：redis.log 写日志**
`redis.log(<level>, <message>)`
```lua
-- 在 Lua 脚本中写日志
redis.log(redis.LOG_WARNING, 'something went wrong')
```

**基本写法：构造状态回复**
`redis.status_reply(<message>)`
```lua
-- 构造状态回复
return redis.status_reply('OK')
```

**基本写法：构造错误回复**
`redis.error_reply(<message>)`
```lua
-- 构造错误回复
return redis.error_reply('something went wrong')
```

---

## 实战模式

**换行写法：原子性分布式锁释放**
`EVAL <script> 1 <lock_key> <lock_value>`
```bash
# 检查 token 后再释放锁避免误删
EVAL "if redis.call('GET', KEYS[1]) == ARGV[1] then return redis.call('DEL', KEYS[1]) else return 0 end" 1 lock:resource1 my_token
```

**换行写法：滑动窗口限流器**
`EVAL <script> 1 <key> <limit> <window> <now>`
```bash
# 基于 ZSET 实现原子性滑动窗口限流
EVAL "local key=KEYS[1] local limit=tonumber(ARGV[1]) local window=tonumber(ARGV[2]) local now=tonumber(ARGV[3]) redis.call('ZREMRANGEBYSCORE', key, 0, now-window) local count=redis.call('ZCARD', key) if count<limit then redis.call('ZADD', key, now, now) redis.call('PEXPIRE', key, window) return 1 end return 0" 1 rate:user1 100 60000 1718334600000
```

**换行写法：库存原子扣减**
`EVAL <script> 1 <stock_key> <quantity>`
```bash
# 检查库存足够后原子扣减
EVAL "local stock=tonumber(redis.call('GET', KEYS[1])) local qty=tonumber(ARGV[1]) if not stock or stock<qty then return 0 end redis.call('DECRBY', KEYS[1], qty) return 1" 1 stock:item1 1
```

**换行写法：计数器限流**
`EVAL <script> 1 <key> <limit> <expire>`
```bash
# 简单计数器限流
EVAL "local count=redis.call('INCR', KEYS[1]) if count==1 then redis.call('EXPIRE', KEYS[1], ARGV[2]) end if count>tonumber(ARGV[1]) then return 0 end return 1" 1 rate:user1 100 60
```

**换行写法：原子转账**
`EVAL <script> 2 <from> <to> <amount>`
```bash
# 原子性余额转账
EVAL "local from=KEYS[1] local to=KEYS[2] local amt=tonumber(ARGV[1]) local bal1=tonumber(redis.call('GET', from)) if not bal1 or bal1<amt then return 0 end redis.call('DECRBY', from, amt) redis.call('INCRBY', to, amt) return 1" 2 balance:user1 balance:user2 100
```



<!-- ============ 文档分隔线：022-redis/016-KeyManagement.md ============ -->

# Redis Key 管理与过期命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 过期时间设置

**基本写法：EXPIRE / PEXPIRE**
`EXPIRE <key> <秒> | PEXPIRE <key> <毫秒>`
```redis
-- 设置过期时间（秒）
SET session:1001 'user_data'
EXPIRE session:1001 1800

-- 毫秒级过期
PEXPIRE token:abc 90000

-- SET 时直接带过期（推荐，原子操作）
SET session:1001 'data' EX 1800
SET token:abc 'v' PX 90000

-- 设置绝对过期时间点
EXPIREAT cache:img 1735689600      -- Unix 时间戳（秒）
PEXPIREAT cache:img 1735689600000  -- 毫秒
```

---

**基本写法：TTL / PTTL 查看剩余时间**
`TTL <key> | PTTL <key>`
```redis
-- 返回剩余秒数；-1=永不过期；-2=键不存在
TTL session:1001
-- 返回剩余毫秒
PTTL token:abc
```

---

## 过期移除与持久化

**基本写法：PERSIST 移除过期**
`PERSIST <key>`
```redis
-- 将带过期的 key 变为永久 key
SET k1 v1 EX 60
PERSIST k1
TTL k1   -- 返回 -1（永不过期）
```

---

## Key 基本操作

**基本写法：TYPE 查看类型**
`TYPE <key>`
```redis
-- 返回 key 的数据类型：string/list/hash/set/zset/stream/none
TYPE user:1001
TYPE mylist
```

---

**基本写法：DEL / UNLINK 删除**
`DEL <key> [<key>...] | UNLINK <key> [<key>...]`
```redis
-- DEL 同步删除（阻塞，大 key 慎用）
DEL k1 k2 k3

-- UNLINK 异步删除（后台释放内存，适合大 key）
UNLINK biglist:1
```

---

**基本写法：RENAME / RENAMENX**
`RENAME <old> <new> | RENAMENX <old> <new>`
```redis
-- 重命名（new 已存在会被覆盖）
RENAME k1 k2
-- 仅在 new 不存在时重命名
RENAMENX k1 k2
```

---

**基本写法：RANDOMKEY / EXISTS**
`RANDOMKEY | EXISTS <key> [<key>...]`
```redis
-- 随机返回一个 key
RANDOMKEY

-- 检查 key 是否存在，返回存在的数量
EXISTS user:1 user:2 user:3
```

---

## SCAN 遍历

**基本写法：SCAN 游标遍历**
`SCAN <cursor> [MATCH <pattern>] [COUNT <n>] [TYPE <类型>]`
```redis
-- 增量式遍历，不阻塞，适合生产环境
SCAN 0 MATCH user:* COUNT 100

-- 下一页用上一次返回的游标
SCAN 16384 MATCH user:* COUNT 100

-- 按类型过滤（Redis 6.0+）
SCAN 0 TYPE hash

-- 返回格式：1) 下一个游标  2) 匹配的 key 列表
-- 游标返回 0 表示遍历结束
```

---

**基本写法：集合类型 HSCAN/SSCAN/ZSCAN**
`<HSCAN|SSCAN|ZSCAN> <key> <cursor> [MATCH <pattern>] [COUNT <n>]`
```redis
-- 遍历 Hash 字段
HSCAN user:1001 0 MATCH name* COUNT 100

-- 遍历 Set 成员
SSCAN tags 0 MATCH tech* COUNT 100

-- 遍历 ZSet 成员
ZSCAN leaderboard 0 MATCH user:* COUNT 100
```

---

## Key 通配模式

**基本写法：KEYS（生产禁用）**
`KEYS <pattern>`
```redis
-- KEYS 会阻塞，仅限调试；生产用 SCAN 替代
KEYS *              -- 所有 key
KEYS user:*         -- user: 开头
KEYS ?ser:100?      -- ? 匹配单字符
KEYS [au]ser:*      -- 字符集匹配
```

---

**基本写法：OBJECT ENCODING 查看内部编码**
`OBJECT ENCODING <key>`
```redis
-- 查看底层编码（int/embstr/raw/listpack/hashtable/skiplist/intset...）
OBJECT ENCODING k1
-- 查看引用计数
OBJECT REFCOUNT k1
-- 查看空闲时间（秒）
OBJECT IDLETIME k1
```

---

## 批量操作

**基本写法：MSET / MGET**
`MSET <k1> <v1> [<k2> <v2>...] | MGET <k1> [<k2>...]`
```redis
-- 批量设置（原子操作）
MSET k1 v1 k2 v2 k3 v3
-- 批量获取
MGET k1 k2 k3

-- MSETNX：仅当所有 key 都不存在时设置
MSETNX k1 v1 k2 v2
```

---

**基本写法：DBSIZE / FLUSHDB**
`DBSIZE | FLUSHDB [ASYNC]`
```redis
-- 当前库 key 数量
DBSIZE
-- 清空当前库（慎用）
FLUSHDB
-- 异步清空（不阻塞）
FLUSHDB ASYNC
-- 清空所有库
FLUSHALL ASYNC
```

---

## 过期键通知

**基本写法：键空间通知**
`CONFIG SET notify-keyspace-events <参数>`
```redis
-- 启用过期事件通知（K=键空间，E=键事件，x=过期事件）
CONFIG SET notify-keyspace-events Ex

-- 订阅过期事件
SUBSCRIBE __keyevent@0__:expired

-- 通知参数组合：
-- K 键空间通知  E 键事件通知
-- g 通用命令   $ 字符串  l 列表  s 集合  h 哈希  z 有序集合
-- x 过期事件   e 驱逐事件  t TTL  d 新 key
-- A 所有事件（g$lshzxe 的别名）
```



<!-- ============ 文档分隔线：022-redis/017-Replication.md ============ -->

# Redis 主从复制命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 主从配置

**基本写法：REPLICAOF 设置从库**
`REPLICAOF <host> <port>`
```redis
-- Redis 5.0+ 用 REPLICAOF（替代旧版 SLAVEOF）
REPLICAOF 192.168.1.10 6379

-- 取消从库身份，升级为主库
REPLICAOF NO ONE

-- 旧版写法（仍兼容但建议用 REPLICAOF）
SLAVEOF 192.168.1.10 6379
SLAVEOF NO ONE
```

---

**基本写法：配置文件持久化**
`replicaof <host> <port>`
```conf
# redis.conf 主从配置
replicaof 192.168.1.10 6379
masterauth <主库密码>          -- 主库有密码时设置
replica-auth-password <密码>   -- Redis 7.0+ 推荐写法

# 只读从库（默认 yes）
replica-read-only yes

# 复制缓冲区大小（应对断线重连）
repl-backlog-size 256mb
repl-backlog-ttl 3600
```

---

## 复制状态查询

**基本写法：INFO replication**
`INFO replication`
```redis
-- 查看复制信息
INFO replication
-- 关键字段：
-- role:master|slave
-- connected_slaves: 从库数量
-- slave0:ip=...,port=...,state=online,offset=...,lag=0
-- master_repl_offset: 主库复制偏移量
-- repl_backlog_size / repl_backlog_first_byte_offset
```

---

**基本写法：ROLE 查看角色**
`ROLE`
```redis
-- 返回当前节点角色信息
ROLE
-- 主库返回：master <offset> <从库列表>
-- 从库返回：slave <主IP> <主端口> <状态> <已复制偏移量>
```

---

## PSYNC 同步机制

**基本写法：PSYNC 部分重同步**
`PSYNC <replicationid> <offset>`
```redis
-- 从库内部调用，通常无需手动执行
-- 首次同步：PSYNC ? -1  触发全量 RDB 同步
-- 断线重连：PSYNC <runid> <offset>  尝试部分重同步

-- 全量同步流程：
-- 1. 从库发送 PSYNC ? -1
-- 2. 主库 BGSAVE 生成 RDB 并发送
-- 3. 主库同时缓存写命令到 backlog
-- 4. RDB 发送完，主库发送缓存的写命令
-- 5. 后续主库写命令实时复制

-- 部分重同步条件：offset 在 backlog 范围内
```

---

## 复制缓冲区

**基本写法：调整 backlog 大小**
`CONFIG SET repl-backlog-size <大小>`
```redis
-- backlog 越大，断线重连时部分重同步成功率越高
CONFIG SET repl-backlog-size 512mb

-- 主库无从库时 backlog 释放时间（秒），0=永不释放
CONFIG SET repl-backlog-ttl 3600

-- 客户端输出缓冲区（从库连接）
CONFIG SET client-output-buffer-limit 'replica 256mb 64mb 60'
```

---

## 级联复制

**基本写法：链式复制**
`REPLICAOF <中间从库> <port>`
```redis
-- 一主多从的级联结构，减轻主库压力
-- master <- slave1 <- slave2
-- slave2 指向 slave1
REPLICAOF 192.168.1.11 6379   -- slave1 的地址

-- slave1 配置允许级联复制（默认允许）
-- replica-serve-stale-data yes
```

---

## 读写分离与一致性

**基本写法：WAIT 等待复制**
`WAIT <numreplicas> <timeout毫秒>`
```redis
-- 等待 N 个从库确认写入，返回确认的从库数
SET key1 value1
WAIT 1 1000    -- 等待 1 个从库确认，最多等 1000ms

-- 注意：WAIT 只等待当前命令的复制，不保证持久化
-- 不影响后续命令，仅返回已确认从库数量
```

---

**基本写法：只读从库配置**
`CONFIG SET replica-read-only yes`
```redis
-- 从库默认只读，禁止写入
CONFIG SET replica-read-only yes

-- 主从延迟导致读到旧数据的应对：
-- 1. 关键读走主库
-- 2. 使用 WAIT 等待复制
-- 3. 读从库后校验 offset
```

---

## 复制故障排查

**基本写法：排查复制中断**
`INFO replication | LATENCY`
```redis
-- 1. 检查从库连接状态
INFO replication
-- state 不为 online 时检查网络/密码

-- 2. 检查 master_link_status
-- master_link_status:down 表示连接断开

-- 3. 检查复制偏移量差距
-- master_repl_offset - slave_repl_offset = 滞后字节数

-- 4. 查看日志
LOG GET 100

-- 5. 强制全量重同步
REPLICAOF NO ONE
REPLICAOF <master_ip> <master_port>
```

---

## 复制过滤

**基本写法：选择性复制**
`replica-serve-stale-data | replica-priority`
```conf
# redis.conf 配置
# 从库与主库断开后是否继续提供旧数据服务
replica-serve-stale-data yes

# 从库优先级（哨兵选主用，0=永不被选为主）
replica-priority 100

# 忽略某些 key 的复制（Redis 7.0+ 已移除，改用 ACL）
# 旧版：replica-ignore-maxmemory no
```



<!-- ============ 文档分隔线：022-redis/018-Sentinel.md ============ -->

# Redis Sentinel 哨兵命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 哨兵配置

**基本写法：sentinel.conf 配置**
`sentinel monitor <主库别名> <host> <port> <quorum>`
```conf
# sentinel.conf 配置文件
port 26379
sentinel monitor mymaster 192.168.1.10 6379 2
sentinel auth-pass mymaster <主库密码>
sentinel down-after-milliseconds mymaster 30000
sentinel parallel-syncs mymaster 1
sentinel failover-timeout mymaster 180000

# quorum=2：2 个哨兵同意才判定主观下线转客观下线
# down-after-milliseconds：30s 无响应判定下线
# parallel-syncs：故障转移时并行同步的从库数
# failover-timeout：故障转移超时
```

---

**基本写法：启动哨兵**
`redis-sentinel <配置文件> | redis-server <配置文件> --sentinel`
```bash
# 方式一：redis-sentinel 专用命令
redis-sentinel /etc/redis/sentinel.conf

# 方式二：redis-server 加 --sentinel 参数
redis-server /etc/redis/sentinel.conf --sentinel

# 集群部署：至少 3 个哨兵节点，分散部署
```

---

## 哨兵查询命令

**基本写法：SENTINEL masters**
`SENTINEL masters | SENTINEL master <主库别名>`
```redis
-- 查看所有被监控的主库
SENTINEL masters

-- 查看指定主库详情
SENTINEL master mymaster
-- 返回：name, ip, port, runid, role-reported, slaves, sentinels,
--       quorum, flags(master), down-after-milliseconds, etc.
```

---

**基本写法：查看从库与哨兵**
`SENTINEL slaves <主库别名> | SENTINEL sentinels <主库别名>`
```redis
-- 查看主库下的从库列表
SENTINEL slaves mymaster

-- 查看监控同一主库的其他哨兵
SENTINEL sentinels mymaster
```

---

**基本写法：获取主库地址**
`SENTINEL get-master-addr-by-name <主库别名>`
```redis
-- 客户端连接哨兵查询当前主库地址
SENTINEL get-master-addr-by-name mymaster
-- 返回：1) "192.168.1.11"  2) "6379"（故障转移后地址会变）
```

---

## 故障转移

**基本写法：手动故障转移**
`SENTINEL failover <主库别名>`
```redis
-- 手动触发故障转移，将从库提升为主库
SENTINEL failover mymaster

-- 故障转移流程：
-- 1. 哨兵标记主库下线
-- 2. 选举领头哨兵
-- 3. 选择最优从库（优先级>偏移量>runid）
-- 4. 从库执行 SLAVEOF NO ONE 升主
-- 5. 其他从库指向新主库
-- 6. 旧主恢复后变为从库
```

---

**基本写法：强制重置**
`SENTINEL reset <pattern>`
```redis
-- 重置匹配 pattern 的主库监控（清空状态重新发现）
SENTINEL reset my*
-- 重置所有
SENTINEL reset *

-- 重置后哨兵会重新发现主从拓扑
```

---

**基本写法：检查仲裁**
`SENTINEL ckquorum <主库别名>`
```redis
-- 检查当前哨兵数是否足够达成仲裁
SENTINEL ckquorum mymaster
-- 返回 OK 表示可用；返回 error 表示哨兵不足
```

---

## 故障转移原理

**基本写法：下线判定与选举**
`<主观下线> -> <客观下线> -> <_leader 选举> -> <选从升主>`
```redis
-- 1. 主观下线（SDOWN）：单个哨兵判定 down
--    条件：down-after-milliseconds 内无响应

-- 2. 客观下线（ODOWN）：quorum 个哨兵同意
--    通过 SENTINEL is-master-down-by-addr 投票

-- 3. Leader 选举：Raft 协议选领头哨兵执行转移

-- 4. 从库选举优先级：
--    a. replica-priority 值小的优先（0 永不升主）
--    b. 复制偏移量大的优先（数据更新）
--    c. runid 字典序小的优先
```

---

## 客户端连接哨兵

**基本写法：客户端订阅切换事件**
`SUBSCRIBE +switch-master | +sdown`
```redis
-- 客户端订阅哨兵频道感知主库切换
SUBSCRIBE +switch-master
-- 故障转移后收到：mymaster 192.168.1.10 6379 192.168.1.11 6379

-- 订阅下线事件
PSUBSCRIBE *

-- 常见事件频道：
-- +switch-master：主库切换
-- +sdown：主观下线
-- +odown：客观下线
-- +failover-state-*：故障转移各阶段
-- +slave-reconf-sent：从库重配置
```

---

## 哨兵运维

**基本写法：动态修改配置**
`SENTINEL set <主库别名> <参数> <值>`
```redis
-- 动态修改哨兵配置（运行时生效）
SENTINEL set mymaster down-after-milliseconds 5000
SENTINEL set mymaster parallel-syncs 3
SENTINEL set mymaster failover-timeout 300000
SENTINEL set mymaster quorum 3

-- 动态添加监控主库
SENTINEL monitor newmaster 192.168.2.10 6379 2
-- 移除监控
SENTINEL remove newmaster
```

---

**基本写法：flushconfig 持久化**
`SENTINEL flushconfig`
```redis
-- 将当前哨兵状态写入配置文件（持久化）
SENTINEL flushconfig
-- 哨兵状态变更（发现新从库/哨兵）后建议执行
```



<!-- ============ 文档分隔线：022-redis/019-Cluster.md ============ -->

# Redis Cluster 集群命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 集群创建

**基本写法：redis-cli 创建集群**
`redis-cli --cluster create <节点1> <节点2> ... --cluster-replicas <每主几个从>`
```bash
# 创建 3 主 3 从集群
redis-cli --cluster create \
  192.168.1.1:7000 192.168.1.2:7000 192.168.1.3:7000 \
  192.168.1.1:7001 192.168.1.2:7001 192.168.1.3:7001 \
  --cluster-replicas 1

# cluster-replicas 1 表示每个主库配 1 个从库
```

---

**基本写法：节点配置文件**
`cluster-enabled yes`
```conf
# 每个节点的 redis.conf
port 7000
cluster-enabled yes
cluster-config-file nodes-7000.conf
cluster-node-timeout 15000
cluster-announce-ip 192.168.1.1
cluster-announce-port 7000
cluster-announce-bus-port 17000

# 集群总线端口 = 数据端口 + 10000
# 节点间通信用总线端口，客户端用数据端口
```

---

## CLUSTER 节点管理

**基本写法：CLUSTER MEET 加入节点**
`CLUSTER MEET <ip> <port>`
```redis
-- 向集群添加新节点
CLUSTER MEET 192.168.1.4 7000

-- 查看集群节点列表
CLUSTER NODES
-- 返回格式：id ip:port@bus flags master ping pong epoch link slots
-- flags: master/slave/fail/myself/handshake/noaddr
```

---

**基本写法：CLUSTER INFO 集群状态**
`CLUSTER INFO`
```redis
-- 查看集群信息
CLUSTER INFO
-- 关键字段：
-- cluster_state:ok
-- cluster_slots_assigned:16384
-- cluster_slots_ok:16384
-- cluster_known_nodes:6
-- cluster_size:3
```

---

## 槽位管理

**基本写法：CLUSTER SLOTS 槽位分布**
`CLUSTER SLOTS`
```redis
-- 查看槽位分配
CLUSTER SLOTS
-- 返回：起始槽-结束槽-主节点信息-从节点信息
-- 如：0-5460 [ip,port,id] [从ip,从port,从id]
```

---

**基本写法：CLUSTER COUNTKEYSINSLOT**
`CLUSTER COUNTKEYSINSLOT <slot>`
```redis
-- 统计某槽位的 key 数量
CLUSTER COUNTKEYSINSLOT 5500

-- 计算 key 的槽位
CLUSTER KEYSLOT mykey
-- Redis 用 CRC16(key) % 16384 计算槽位
```

---

**基本写法：分配槽位**
`CLUSTER ADDSLOTS <slot> [<slot>...]`
```redis
-- 给当前节点分配槽位
CLUSTER ADDSLOTS 0 1 2 3 4 5

-- 删除槽位
CLUSTER DELSLOTS 0 1 2

-- 批量分配（创建集群时用 bash 循环）
# for i in {0..5460}; do redis-cli -p 7000 CLUSTER ADDSLOTS $i; done
```

---

**基本写法：迁移槽位**
`CLUSTER SETSLOT <slot> MIGRATING <目标nodeid> | IMPORTING <源nodeid>`
```redis
-- 槽位迁移流程（手动迁移 slot 100 从 A 到 B）
-- 1. B 准备接收
CLUSTER SETSLOT 100 IMPORTING <A的nodeid>

-- 2. A 准备迁出
CLUSTER SETSLOT 100 MIGRATING <B的nodeid>

-- 3. 迁移 key
MIGRATE <B_ip> <B_port> '' 0 5000 KEYS key1 key2

-- 4. 两端都确认新归属
CLUSTER SETSLOT 100 NODE <B的nodeid>

-- 推荐：用 redis-cli --cluster reshard 自动迁移
```

---

## redis-cli 集群工具

**基本写法：集群重平衡**
`redis-cli --cluster reshard <任意节点>`
```bash
# 交互式迁移槽位
redis-cli --cluster reshard 192.168.1.1:7000
# 输入：迁移多少槽位、目标节点id、源节点（all 或 id 列表）

# 自动平衡槽位分布
redis-cli --cluster rebalance 192.168.1.1:7000

# 检查集群健康
redis-cli --cluster check 192.168.1.1:7000

# 修复槽位异常
redis-cli --cluster fix 192.168.1.1:7000
```

---

**基本写法：添加/移除节点**
`redis-cli --cluster add-node <新节点> <集群任意节点>`
```bash
# 添加主节点
redis-cli --cluster add-node 192.168.1.4:7000 192.168.1.1:7000

# 添加从节点（指定主库 id）
redis-cli --cluster add-node 192.168.1.4:7001 192.168.1.1:7000 \
  --cluster-slave --cluster-master-id <主库nodeid>

# 移除节点（先迁移槽位）
redis-cli --cluster del-node 192.168.1.1:7000 <待移除nodeid>
```

---

## 客户端集群操作

**基本写法：-c 启用集群模式**
`redis-cli -c -h <host> -p <port>`
```bash
# -c 自动跟随 MOVED/ASK 重定向
redis-cli -c -h 192.168.1.1 -p 7000

# 不加 -c 时遇到跨槽 key 会报错并返回 MOVED
# MOVED 5474 192.168.1.2:7000 表示去 2 号节点查
```

---

**基本写法：Hash Tag 保证同槽**
`SET {tag}key1 v1 | SET {tag}key2 v2`
```redis
-- 用 {} 指定 hash tag，大括号内内容参与槽位计算
SET {user100}.name 'Alice'
SET {user100}.age '30'
SET {user100}.email 'a@x.com'

-- 三个 key 槽位相同，可在同节点执行 MGET/事务
MGET {user100}.name {user100}.age {user100}.email

-- 适用于多 key 操作（事务/聚合）必须在同节点
```

---

## 集群限制

**基本写法：跨槽操作限制**
`<多key命令> 仅当所有 key 同槽时可用`
```redis
-- 以下命令要求所有 key 在同一槽位，否则报 CROSSSLOT 错误
MGET k1 k2 k3          -- 若槽位不同则失败
MULTI / EXEC            -- 事务中跨槽 key 失败
SINTER s1 s2            -- 集合运算跨槽失败
ZUNIONSTORE dst 2 s1 s2

-- 解决方案：用 Hash Tag {tag} 强制同槽
MGET {tag}k1 {tag}k2 {tag}k3
```

---

## 故障转移

**基本写法：手动故障转移**
`CLUSTER FAILOVER [FORCE|TAKEOVER]`
```redis
-- 从库执行，请求升主（需主库同意）
CLUSTER FAILOVER

-- FORCE：不等主库确认，直接升主（主库不可达时）
CLUSTER FAILOVER FORCE

-- TAKEOVER：跳过集群协商，强制升主（危险，可能脑裂）
CLUSTER FAILOVER TAKEOVER

-- 流程：从库停止复制 -> 通知主库 -> 主库停止处理 -> 从库升主
```

---

**基本写法：故障节点处理**
`CLUSTER FORGET <nodeid>`
```redis
-- 从集群中移除故障节点（需对所有存活节点执行）
CLUSTER FORGET <故障nodeid>

-- 重置当前节点集群状态
CLUSTER RESET [HARD|SOFT]
-- SOFT：保留数据，重置集群信息
-- HARD：清空数据 + 重置集群（重新加入用）
```



<!-- ============ 文档分隔线：022-redis/020-ACL.md ============ -->

# Redis 安全与 ACL 命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 认证基础

**基本写法：AUTH 密码认证**
`AUTH <password> | AUTH <username> <password>`
```redis
-- 旧版单密码认证（Redis 6 之前）
AUTH mypassword

-- ACL 用户认证（Redis 6.0+）
AUTH alice mypassword

-- 配置文件设置密码
# redis.conf
requirepass mypassword
```

---

**基本写法：配置文件启用 ACL**
`aclfile <路径>`
```conf
# redis.conf 启用 ACL 文件
aclfile /etc/redis/users.acl

# 默认用户配置
user default on >password ~* +@all

# users.acl 文件示例
user default on nopass ~* +@all
user app_user on >secret123 ~app:* +@read -@write
user admin on >admin_pwd ~* +@all
```

---

## ACL 用户管理

**基本写法：ACL SETUSER 创建用户**
`ACL SETUSER <用户名> [规则...]`
```redis
-- 创建用户并设置权限
ACL SETUSER alice on >password123 ~user:* +@read +@hash -@write

-- 规则说明：
-- on/off           启用/禁用用户
-- >password        设置密码
-- <password        删除密码
-- #hash            设置密码哈希（SHA256）
-- ~pattern         允许访问的 key 模式
-- allkeys          允许访问所有 key（等价 ~*）
-- resetkeys        清除 key 模式
-- +command         允许某命令
-- -command         禁止某命令
-- +@category       允许命令类别（read/write/admin/dangerous...）
-- -@category       禁止命令类别
-- allcommands/+@all  允许所有命令
-- nocommands/-@all   禁止所有命令
-- reset            重置所有规则
```

---

**基本写法：ACL GETUSER 查看用户**
`ACL GETUSER <用户名>`
```redis
-- 查看用户详细权限
ACL GETUSER alice
-- 返回：flags, passwords, commands, keys, channels, selectors

-- 查看所有用户名
ACL WHOAMI          -- 当前用户
ACL USERS           -- 所有用户列表
```

---

**基本写法：ACL DELUSER 删除用户**
`ACL DELUSER <用户名> [<用户名>...]`
```redis
-- 删除用户（不能删除 default 用户）
ACL DELUSER alice bob

-- 禁用而非删除（保留用户定义）
ACL SETUSER alice off
```

---

## 命令类别

**基本写法：ACL CAT 查看类别**
`ACL CAT [<类别>]`
```redis
-- 查看所有命令类别
ACL CAT
-- 返回：keyspace, read, write, set, sortedset, list, hash,
--       string, bitmap, hyperloglog, geo, stream, pubsub,
--       admin, fast, slow, blocking, dangerous, connection...

-- 查看某类别下的命令
ACL CAT read
ACL CAT dangerous
```

---

**基本写法：常用类别组合**
`+@read -@write +@dangerous`
```redis
-- 只读用户
ACL SETUSER reader on >pwd ~* +@read -@write

-- 管理员
ACL SETUSER admin on >pwd ~* +@all

-- 受限用户：只能读 app: 前缀
ACL SETUSER app_read on >pwd ~app:* +@read +@connection

-- 禁止危险命令
ACL SETUSER safe_user on >pwd ~* +@all -@dangerous
```

---

## Selector 选择器（Redis 7.0+）

**基本写法：多组规则组合**
`ACL SETUSER <用户> (<规则组>)`
```redis
-- ACL v2 Selector：根规则 + 多个选择器，任一匹配即允许
ACL SETUSER power_user on >pwd \
  (~app:* +@all) \
  (~cache:* +@read)

-- 根规则：对 app:* 有全部权限
-- 选择器1：对 cache:* 只有读权限
-- 执行命令时：根规则或任一 selector 匹配即允许

-- 设置频道权限（Pub/Sub）
ACL SETUSER subscriber on >pwd &channel:*
-- &pattern 限制可订阅频道
```

---

## ACL 持久化

**基本写法：ACL SAVE 保存**
`ACL SAVE | ACL LOAD`
```redis
-- 保存当前 ACL 到 aclfile
ACL SAVE

-- 从 aclfile 重新加载
ACL LOAD

-- 注意：ACL 变更后需 ACL SAVE 持久化，否则重启丢失
```

---

## ACL 日志

**基本写法：ACL LOG 审计**
`ACL LOG [<count>|RESET]`
```redis
-- 查看被拒绝的命令日志（最近 128 条）
ACL LOG 10

-- 日志字段：reason, context, object, username, age...
-- reason: auth|command|key|channel

-- 清空日志
ACL LOG RESET
```

---

## TLS 加密连接

**基本写法：配置 TLS**
`tls-port <端口>`
```conf
# redis.conf TLS 配置（Redis 6.0+）
tls-port 6380
port 0                          -- 关闭明文端口

tls-cert-file /etc/redis/redis.crt
tls-key-file /etc/redis/redis.key
tls-ca-cert-file /etc/redis/ca.crt

tls-auth-clients yes            -- 要求客户端证书
tls-auth-clients no             -- 不要求客户端证书
tls-protocols "TLSv1.2 TLSv1.3"
```

---

**基本写法：客户端 TLS 连接**
`redis-cli --tls --cert <证书> --key <私钥> --cacert <CA>`
```bash
# 启用 TLS 连接
redis-cli --tls \
  --cert /etc/redis/client.crt \
  --key /etc/redis/client.key \
  --cacert /etc/redis/ca.crt \
  -h 192.168.1.1 -p 6380
```

---

## 安全加固清单

**基本写法：生产安全配置**
`CONFIG SET <参数> <值>`
```redis
-- 1. 禁用危险命令
CONFIG SET rename-command FLUSHALL ''
CONFIG SET rename-command FLUSHDB ''
CONFIG SET rename-command CONFIG ''

-- 2. 绑定内网地址（配置文件）
# bind 192.168.1.10 127.0.0.1
# protected-mode yes

-- 3. 设置密码/ACL
# requirepass 或 aclfile

-- 4. 限制最大内存与淘汰策略
CONFIG SET maxmemory 4gb
CONFIG SET maxmemory-policy allkeys-lru

-- 5. 禁用 KEYS（用 SCAN 替代）
```



<!-- ============ 文档分隔线：022-redis/021-NewFeatures7.md ============ -->

# Redis 7.0+ 新特性命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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
