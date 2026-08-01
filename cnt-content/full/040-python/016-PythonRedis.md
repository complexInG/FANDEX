---
order: 58
title: Python与Redis
module: python
category: Python
difficulty: intermediate
description: Redis缓存与数据结构
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与Celery
  - python/Python与Docker
  - python/Python与消息队列
  - python/Python与Django
prerequisites:
  - python/语法速查
---

## 什么是 Redis

Redis 是一个基于内存的高性能键值数据库。因为数据存储在内存中，读写速度极快，每秒可以处理数十万次操作。Redis 不仅仅是一个简单的键值存储，它还支持字符串、列表、哈希、集合、有序集合等多种数据结构，以及发布/订阅、事务、Lua 脚本等高级功能。

在 Python 项目中，Redis 最常用于缓存、会话存储、消息队列和排行榜等场景。它不是用来替代关系型数据库的，而是作为数据库前面的高速缓存层，或者用于存储临时性的、需要快速访问的数据。

## 基础概念

### 键值存储

Redis 中所有数据都以键值对的形式存储。键是字符串，值可以是多种数据类型。你可以把 Redis 想象成一个超级快的 Python 字典。

### 数据类型

Redis 支持五种基本数据类型：

- String（字符串）：最简单的类型，可以存储文本、数字、甚至二进制数据
- List（列表）：有序的字符串列表，支持从两端插入和弹出
- Hash（哈希）：键值对的集合，适合存储对象
- Set（集合）：不重复的字符串集合，支持交集、并集等操作
- Sorted Set（有序集合）：带分数的集合，按分数排序，适合排行榜

### 过期时间

Redis 可以为键设置过期时间（TTL），到期后自动删除。这个特性非常适合缓存和会话管理。

### 持久化

虽然 Redis 是内存数据库，但它支持将数据持久化到磁盘，防止重启后数据丢失。有两种持久化方式：RDB（快照）和 AOF（追加日志）。

## 快速上手

### 安装

```bash
# 安装 Redis Python 客户端
pip install redis

# 用 Docker 启动 Redis 服务
docker run -d --name redis -p 6379:6379 redis:7-alpine
```

### 连接 Redis

```python
import redis

# 创建连接
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# decode_responses=True 让返回值自动解码为字符串，而不是字节

# 测试连接
r.ping()  # 返回 True

# 也可以使用连接池
pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)
```

### 基本的键值操作

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 设置键值
r.set('name', '张三')

# 获取值
name = r.get('name')
print(name)  # 张三

# 设置带过期时间的键（10 秒后自动删除）
r.setex('session:abc', 10, 'user_data')

# 查看剩余过期时间
r.ttl('session:abc')  # 返回剩余秒数

# 删除键
r.delete('name')

# 检查键是否存在
r.exists('name')  # 0 表示不存在

# 设置键的过期时间
r.set('temp_key', 'value')
r.expire('temp_key', 60)  # 60 秒后过期
```

## 详细用法

### String 操作

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 基本操作
r.set('counter', '100')
r.get('counter')      # '100'

# 数值操作（值会被当作整数处理）
r.incr('counter')     # 101（自增 1）
r.incrby('counter', 5)  # 106（自增 5）
r.decr('counter')     # 105（自减 1）

# 批量操作
r.mset({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
r.mget('key1', 'key2', 'key3')  # ['value1', 'value2', 'value3']

# 只有键不存在时才设置（防止覆盖）
r.setnx('unique_id', '12345')  # 设置成功返回 True
r.setnx('unique_id', '67890')  # 键已存在，返回 False

# 追加字符串
r.set('msg', 'Hello')
r.append('msg', ', World!')
r.get('msg')  # 'Hello, World!'
```

### Hash 操作

Hash 适合存储对象，类似于 Python 的嵌套字典：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 设置 Hash 的字段
r.hset('user:1', mapping={
    'name': '张三',
    'age': '25',
    'email': 'zhangsan@example.com'
})

# 获取单个字段
r.hget('user:1', 'name')  # '张三'

# 获取所有字段
r.hgetall('user:1')  # {'name': '张三', 'age': '25', 'email': 'zhangsan@example.com'}

# 修改单个字段
r.hset('user:1', 'age', '26')

# 删除字段
r.hdel('user:1', 'email')

# 检查字段是否存在
r.hexists('user:1', 'name')  # True

# 字段值自增
r.hincrby('user:1', 'age', 1)  # 27
```

### List 操作

List 是有序的字符串列表，支持从两端操作：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 从右端插入
r.rpush('tasks', '任务1', '任务2', '任务3')

# 从左端插入
r.lpush('tasks', '紧急任务')

# 获取列表长度
r.llen('tasks')  # 4

# 获取指定范围的元素
r.lrange('tasks', 0, -1)  # ['紧急任务', '任务1', '任务2', '任务3']

# 从左端弹出
r.lpop('tasks')  # '紧急任务'

# 从右端弹出
r.rpop('tasks')  # '任务3'

# 阻塞式弹出（适合实现队列，等待直到有数据）
# r.blpop('tasks', timeout=30)  # 最多等 30 秒
```

### Set 操作

Set 是不重复的字符串集合：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 添加元素
r.sadd('tags:article1', 'Python', 'Web', 'FastAPI')
r.sadd('tags:article2', 'Python', '数据库', 'SQL')

# 获取所有元素
r.smembers('tags:article1')  # {'Python', 'Web', 'FastAPI'}

# 检查元素是否存在
r.sismember('tags:article1', 'Python')  # True

# 集合运算
r.sinter('tags:article1', 'tags:article2')  # 交集: {'Python'}
r.sunion('tags:article1', 'tags:article2')  # 并集: {'Python', 'Web', 'FastAPI', '数据库', 'SQL'}
r.sdiff('tags:article1', 'tags:article2')   # 差集: {'Web', 'FastAPI'}

# 随机弹出一个元素
r.spop('tags:article1')

# 获取集合大小
r.scard('tags:article1')
```

### Sorted Set 操作

Sorted Set 是带分数的有序集合，非常适合排行榜：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 添加带分数的元素
r.zadd('leaderboard', {
    '张三': 100,
    '李四': 200,
    '王五': 150,
    '赵六': 300,
})

# 按分数从低到高获取排名
r.zrange('leaderboard', 0, -1, withscores=True)
# [('张三', 100.0), ('王五', 150.0), ('李四', 200.0), ('赵六', 300.0)]

# 按分数从高到低获取排名（排行榜常用）
r.zrevrange('leaderboard', 0, -1, withscores=True)
# [('赵六', 300.0), ('李四', 200.0), ('王五', 150.0), ('张三', 100.0)]

# 获取前 3 名
r.zrevrange('leaderboard', 0, 2, withscores=True)
# [('赵六', 300.0), ('李四', 200.0), ('王五', 150.0)]

# 增加分数
r.zincrby('leaderboard', 50, '张三')  # 张三的分数变为 150

# 获取某个成员的排名（从 0 开始）
r.zrevrank('leaderboard', '赵六')  # 0（第一名）

# 获取某个成员的分数
r.zscore('leaderboard', '赵六')  # 300.0
```

## 常见场景

### 缓存

```python
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_user(user_id: int):
    """获取用户信息（先查缓存，再查数据库）"""
    cache_key = f'user:{user_id}'

    # 第一步：查缓存
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    # 第二步：缓存未命中，查数据库
    user = query_user_from_db(user_id)
    if user:
        # 写入缓存，设置 5 分钟过期
        r.setex(cache_key, 300, json.dumps(user, ensure_ascii=False))

    return user

def invalidate_user_cache(user_id: int):
    """用户信息更新后，清除缓存"""
    r.delete(f'user:{user_id}')
```

### 会话存储

```python
import redis
import json
import uuid

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def create_session(user_id: int) -> str:
    """创建会话，返回 session_id"""
    session_id = str(uuid.uuid4())
    session_data = json.dumps({'user_id': user_id, 'role': 'user'})
    # 会话 24 小时后过期
    r.setex(f'session:{session_id}', 86400, session_data)
    return session_id

def get_session(session_id: str) -> dict:
    """获取会话数据"""
    data = r.get(f'session:{session_id}')
    return json.loads(data) if data else None

def delete_session(session_id: str):
    """删除会话（登出）"""
    r.delete(f'session:{session_id}')
```

### 限流

```python
import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def rate_limit(user_id: str, max_requests: int = 10, window: int = 60) -> bool:
    """限流：每个用户在 window 秒内最多 max_requests 次请求"""
    key = f'rate_limit:{user_id}'
    current = r.get(key)

    if current is None:
        # 第一次请求，设置计数器
        r.setex(key, window, 1)
        return True

    current = int(current)
    if current >= max_requests:
        return False  # 超过限制

    r.incr(key)
    return True

# 使用
if rate_limit('user:123'):
    print("请求允许")
else:
    print("请求过于频繁，请稍后再试")
```

## 注意事项与常见错误

### 内存有限

Redis 数据存储在内存中，内存是有限的资源。不要把所有数据都放进 Redis，只存放需要快速访问的热数据。为键设置合理的过期时间，避免数据无限增长。

### 大键问题

一个键对应的值不要太大（如一个列表包含百万个元素），这会阻塞 Redis 的其他操作。如果需要存储大量数据，应该拆分成多个小键。

### 数据持久化

默认情况下 Redis 不保证数据不丢失。如果你的数据很重要，需要配置持久化策略（RDB 或 AOF），或者只把 Redis 用作缓存，数据可以从数据库重建。

### 连接管理

每次创建 Redis 连接都有开销，应该使用连接池复用连接。redis-py 默认使用连接池，但如果你手动创建多个 Redis 实例，应该共享同一个连接池。

### 键命名规范

使用冒号分隔的命名规范，方便管理和查找：

```python
# 推荐的键命名方式
'user:1001'           # 用户 ID 为 1001 的数据
'session:abc123'      # 会话 ID 为 abc123 的数据
'cache:article:567'   # 文章 ID 为 567 的缓存
'rate_limit:api:1001' # API 限流，用户 ID 为 1001
```

## 进阶用法

### 发布/订阅

Redis 的发布/订阅模式可以实现简单的消息通知：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 发布消息
r.publish('notifications', '系统维护通知')

# 订阅消息（在另一个进程或线程中）
pubsub = r.pubsub()
pubsub.subscribe('notifications')

for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"收到消息: {message['data']}")
```

### Pipeline 批量操作

Pipeline 可以将多个命令一次性发送给 Redis，减少网络往返时间：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 使用 Pipeline 批量执行
with r.pipeline() as pipe:
    pipe.set('key1', 'value1')
    pipe.set('key2', 'value2')
    pipe.set('key3', 'value3')
    pipe.get('key1')
    results = pipe.execute()

print(results)  # [True, True, True, 'value1']
```

### 使用 redis-py 的异步客户端

```python
import asyncio
import redis.asyncio as redis

async def main():
    # 创建异步连接
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    # 异步操作
    await r.set('key', 'value')
    value = await r.get('key')
    print(value)

    await r.close()

asyncio.run(main())
```

### Lua 脚本

Lua 脚本在 Redis 服务端原子执行，适合需要原子性的复杂操作：

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 定义 Lua 脚本：限流脚本
rate_limit_script = """
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local current = tonumber(redis.call('get', key) or '0')

if current >= limit then
    return 0
end

redis.call('incr', key)
if current == 0 then
    redis.call('expire', key, window)
end
return 1
"""

# 执行脚本
result = r.eval(rate_limit_script, 1, 'rate_limit:user:123', 10, 60)
print(f"请求是否允许: {bool(result)}")
```

## 参考文献



Python 官方文档：https://docs.python.org/zh-cn/3/
PEP 8 样式指南：https://peps.python.org/pep-0008/
Python 之禅（PEP 20）：https://peps.python.org/pep-0020/
Python 类型注解指南（PEP 484）：https://peps.python.org/pep-0484/
Python 打包用户指南：https://packaging.python.org/
Real Python 教程站：https://realpython.com/

## 延伸阅读



Python 数据类型与内置容器，见 040-python 模块的基础文档。
Python 异步编程（asyncio/FastAPI），见 040-python 模块的异步与 Web 文档。
Python 数据分析（NumPy/Pandas），见 051-data-analysis 模块。
Python 与数据库交互（SQLAlchemy），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Python 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Python 后端课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Python 概述与环境配置 | 001-PythonOverviewEnvSetup | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 变量与常量 | 003-VariableConstant | 本文的并列主题 |
| Python 描述符协议：属性访问的底层机制与工程实践 | 004-PythonDescriptorProtocol | 本文的原理深化 |
| Python 基础数据类型：从对象模型到工程实践的深度解析 | 005-PythonBasicsDataTypeObjectModelPracticeDeepAnalysis | 本文的前置基础 |
| 协程与asyncio | 006-CoroutineAsyncio | 本文的并列主题 |
| 列表推导式进阶 | 007-ListComprehensionAdvanced | 本文的并列主题 |
| 运算符与表达式 | 008-OperatorExpression | 本文的并列主题 |
| Python与虚拟环境 | 009-PythonVirtualEnv | 本文的前置基础 |
| 元类 | 010-Metaclass | 本文的并列主题 |
| Python与SQLAlchemy | 011-PythonSQLAlchemy | 本文的并列主题 |
| 多进程与多线程 | 012-MultiprocessingMultithreading | 本文的并列主题 |
| Python与FastAPI | 013-PythonFastAPI | 本文的并列主题 |
| Python与Django | 014-PythonDjango | 本文的并列主题 |
| 数据类与Pydantic | 015-DataClassPydantic | 本文的并列主题 |
| Python与Redis | 016-PythonRedis | 本文自身 |
| Python 与 Celery：分布式任务队列的设计、实现与工程实践 | 017-PythonCeleryDistributedTaskQueue | 本文的并列主题 |
| 控制流 | 018-ControlFlow | 本文的并列主题 |
| Python与Docker | 019-PythonDocker | 本文的并列主题 |
| Python与机器学习 | 020-PythonMachineLearning | 本文的并列主题 |
| Python与深度学习 | 021-PythonDeepLearning | 本文的并列主题 |
| Python与NLP | 022-PythonAndNLP | 本文的并列主题 |
| Python与计算机视觉 | 023-PythonComputerVision | 本文的并列主题 |
| Python与Web爬虫 | 024-WebScrapingWithPython | 本文的并列主题 |
| Python与自动化 | 025-PythonAutomationCookbook | 本文的并列主题 |
| 函数详解 | 026-FunctionDetailed | 本文的并列主题 |
| Python与日志 | 027-PythonLog | 本文的并列主题 |
| Python与加密 | 028-PythonAndCryptography | 本文的安全延伸 |
| Python与测试 | 029-PythonTest | 本文的并列主题 |
| Python 与配置管理：从环境变量到云原生动态配置的工程实践 | 030-Python | 本文的前置基础 |
| 装饰器 | 031-Decorator | 本文的并列主题 |
| Python与消息队列 | 032-PythonMessageQueue | 本文的并列主题 |
| Python与gRPC | 033-PythongRPC | 本文的并列主题 |
| Python与WebSocket | 034-PythonWebSocket | 本文的并列主题 |
| Python与CI-CD | 035-PythonCICD | 本文的并列主题 |
| Python与性能优化 | 036-PythonPerformance | 本文的性能延伸 |
| 内置数据结构 | 037-BuiltinDataStructure | 本文的并列主题 |
| 正则表达式 | 038-Regex | 本文的并列主题 |
| Python与CLI | 039-PythonCLI | 本文的并列主题 |
| Python与设计模式 | 040-PythonDesignPattern | 本文的并列主题 |
| Python与打包发布 | 041-ASurveyOfPythonPackagingPastPresentAndFuture | 本文的并列主题 |
| Python 与 Jupyter：交互式计算、数据分析与可复现研究 | 042-PythonJupyter | 本文的并列主题 |
| Python与GraphQL | 043-PythonGraphQL | 本文的并列主题 |
| Python与代码质量 | 044-PythonCodeQuality | 本文的并列主题 |
| 并发编程 | 045-ConcurrentProgramming | 本文的并列主题 |
| Python与数据库迁移 | 046-PythonDatabaseMigration | 本文的并列主题 |
| Python与OAuth2 | 047-PythonOAuth2 | 本文的并列主题 |
| Python与向量数据库 | 048-PythonVectorDatabase | 本文的并列主题 |
| Python 进阶与最新特性 | 049-PythonAdvancedLatestFeature | 本文的并列主题 |
| 推导式与生成器 | 050-ComprehensionGenerator | 本文的并列主题 |
| 模块、包与工程化 | 051-ModulePackageEngineering | 本文的并列主题 |
| 上下文管理器 | 052-ContextManager | 本文的并列主题 |
| 元类与单例模式 | 053-MetaclassSingleton | 本文的并列主题 |
| 异步编程详解 | 054-AsyncProgrammingDetailed | 本文的并列主题 |
| 弱引用 | 055-WeakReference | 本文的并列主题 |
| 打包与发布 | 056-PackagePublish | 本文的并列主题 |
| 描述符 | 057-Descriptor | 本文的并列主题 |
| 数据类与字段默认值 | 058-DataClassFieldDefault | 本文的并列主题 |
| 生成器与协程 | 059-GeneratorCoroutine | 本文的并列主题 |
| 类型注解与mypy | 060-TypeAnnotationMypy | 本文的并列主题 |
| 面向对象编程 | 061-OOP | 本文的并列主题 |
| 装饰器进阶 | 062-DecoratorAdvanced | 本文的并列主题 |
| 异常处理 | 063-ExceptionHandling | 本文的并列主题 |
| 文件 I/O 与上下文管理器 | 064-FileIOContextManager | 本文的并列主题 |
| Python 项目示例：网页爬虫与数据分析 | 065-PythonProjectExampleWebCrawlerDataAnalysis | 本文的综合应用 |
| Python 理论知识点 | 066-PythonTheoryKnowledge | 本文的并列主题 |
| 基础数据类型 | 067-BasicDataType | 本文的前置基础 |
| Python 面向对象基础 | 068-COOPBasics | 本文的前置基础 |
| Python 面向对象进阶 | 069-COOPAdvanced | 本文的并列主题 |
| Python pathlib 路径操作 | 070-Pathlib | 本文的并列主题 |
| Python itertools 迭代工具 | 071-Itertools | 本文的并列主题 |
| Python functools 函数工具 | 072-Functools | 本文的并列主题 |
| Python datetime 与 time | 073-DatetimeTime | 本文的并列主题 |
| Python 序列化 JSON/CSV/Pickle | 074-SerializationJsonCsvPickle | 本文的并列主题 |
| Python 网络编程 socket/http | 075-NetworkSocketHttp | 本文的并列主题 |
| Python sys/os 平台接口 | 076-SysOsPlatform | 本文的并列主题 |
| Python math/random/statistics | 077-MathRandomStatistics | 本文的并列主题 |
| Python subprocess 子进程 | 078-Subprocess | 本文的并列主题 |
| Python logging 日志配置 | 079-Logging | 本文的并列主题 |
| Python 测试 unittest/pytest | 080-UnittestPytest | 本文的并列主题 |
| Python 字符串格式化与方法 | 081-StringFormattingMethods | 本文的并列主题 |
| Python argparse 命令行参数解析 | 082-ArgparseCli | 本文的并列主题 |
| Python typing 进阶 | 083-TypingAdvanced | 本文的并列主题 |
| Python enum 枚举 | 084-Enum | 本文的并列主题 |
| Python hashlib 与 hmac | 085-HashlibHmac | 本文的并列主题 |
| Python ssl 安全套接字 | 086-SslCrypto | 本文的安全延伸 |
| Python http.client HTTP 客户端 | 087-HttpClient | 本文的并列主题 |
| Python sqlite3 数据库 | 088-Sqlite3 | 本文的并列主题 |
| Python zipfile 与 tarfile | 089-ZipfileTarfile | 本文的并列主题 |
| Python array 与 bisect | 090-ArrayBisect | 本文的并列主题 |
| Python 字符串与文本处理 | 091-StringText | 本文的并列主题 |
| Python decimal 与 fractions | 092-DecimalFractions | 本文的并列主题 |
| Python shutil 与 tempfile | 093-ShutilTempfile | 本文的并列主题 |
| Python gc inspect dis | 094-GcInspect | 本文的并列主题 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
