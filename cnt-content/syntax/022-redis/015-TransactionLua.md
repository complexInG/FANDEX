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
