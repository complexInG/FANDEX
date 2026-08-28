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
