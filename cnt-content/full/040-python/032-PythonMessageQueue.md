---
order: 76
title: Python与消息队列
module: python
category: Python
difficulty: intermediate
description: RabbitMQ与Kafka
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与配置管理
  - python/装饰器
  - python/Python与gRPC
  - python/Python与WebSocket
prerequisites:
  - python/语法速查
---

## 什么是消息队列

消息队列是一种进程间通信方式。发送方把消息放入队列，接收方从队列中取出消息处理。发送方和接收方不需要同时在线，也不需要知道对方是谁，它们只需要关心消息本身。

消息队列解决的核心问题是"解耦"和"削峰"。解耦是指生产者和消费者互不依赖，可以独立开发和部署。削峰是指当瞬时请求量很大时，消息先在队列中排队，消费者按自己的速度处理，不会因为流量突增而崩溃。

## 基础概念

### 生产者、消费者与队列

- 生产者（Producer）：发送消息的程序
- 消费者（Consumer）：接收消息的程序
- 队列（Queue）：存储消息的缓冲区

### RabbitMQ 与 Kafka 的区别

RabbitMQ 是传统的消息代理，支持复杂的路由规则、消息确认、优先级队列等。适合任务分发、事件通知等场景。

Kafka 是分布式流处理平台，以高吞吐量著称，消息持久化到磁盘。适合日志收集、数据流处理、事件溯源等场景。

### Exchange 与路由（RabbitMQ）

RabbitMQ 中生产者不直接发送消息到队列，而是发送到 Exchange（交换机），由 Exchange 根据路由规则将消息投递到一个或多个队列。常见的 Exchange 类型有：

- Direct：精确匹配路由键
- Fanout：广播到所有绑定队列
- Topic：通配符匹配路由键

### Topic 与分区（Kafka）

Kafka 中消息按 Topic 分类，每个 Topic 可以分成多个 Partition（分区），分区是并行处理的基本单位。消息在分区中按顺序存储，每条消息有一个偏移量（Offset）。

## 快速上手

### 安装客户端库

```bash
# RabbitMQ 客户端
pip install pika

# Kafka 客户端
pip install kafka-python
```

### RabbitMQ 最简示例

先确保 RabbitMQ 服务已启动（可用 Docker 快速启动）：

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

发送消息：

```python
# rabbitmq_send.py - 发送消息
import pika

# 连接到 RabbitMQ 服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明一个队列（如果不存在会自动创建）
channel.queue_declare(queue='hello')

# 发送消息
channel.basic_publish(
    exchange='',
    routing_key='hello',      # 队列名称
    body='Hello, RabbitMQ!'   # 消息内容
)

print("消息已发送")
connection.close()
```

接收消息：

```python
# rabbitmq_receive.py - 接收消息
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明队列（确保队列存在）
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    """消息处理回调函数"""
    print(f"收到消息: {body.decode()}")

# 订阅队列，设置消息处理回调
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True  # 自动确认
)

print("等待消息中，按 Ctrl+C 退出")
channel.start_consuming()
```

### Kafka 最简示例

先启动 Kafka 服务（需要先启动 Zookeeper）：

```bash
docker run -d --name zookeeper -p 2181:2181 wurstmeister/zookeeper
docker run -d --name kafka -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=host.docker.internal:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  wurstmeister/kafka
```

生产者：

```python
# kafka_producer.py - Kafka 生产者
from kafka import KafkaProducer

# 创建生产者
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')  # 字符串编码
)

# 发送消息
producer.send('my-topic', 'Hello, Kafka!')
producer.flush()  # 确保消息已发送

print("消息已发送")
producer.close()
```

消费者：

```python
# kafka_consumer.py - Kafka 消费者
from kafka import KafkaConsumer

# 创建消费者
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    group_id='my-group',         # 消费者组
    auto_offset_reset='earliest' # 从最早的消息开始消费
)

# 持续消费消息
for message in consumer:
    print(f"收到消息: {message.value.decode('utf-8')}")
    print(f"  分区: {message.partition}, 偏移量: {message.offset}")
```

## 详细用法

### RabbitMQ 工作队列

工作队列用于在多个消费者之间分配任务：

```python
# rabbitmq_task.py - 发送任务
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明持久化队列
channel.queue_declare(queue='tasks', durable=True)

# 发送多个任务
for i in range(10):
    message = f"任务 {i}"
    channel.basic_publish(
        exchange='',
        routing_key='tasks',
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # 持久化消息
    )
    print(f"已发送: {message}")

connection.close()
```

```python
# rabbitmq_worker.py - 工作进程
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks', durable=True)

def callback(ch, method, properties, body):
    """处理任务"""
    print(f"开始处理: {body.decode()}")
    time.sleep(1)  # 模拟耗时操作
    print(f"处理完成: {body.decode()}")
    # 手动确认消息已处理
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 每次只取一条消息（公平分发）
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='tasks', on_message_callback=callback)

print("工作进程已启动，等待任务...")
channel.start_consuming()
```

### RabbitMQ 发布/订阅

使用 Fanout Exchange 广播消息给所有订阅者：

```python
# rabbitmq_publish.py - 发布消息
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明 fanout 类型的交换机
channel.exchange_declare(exchange='notifications', exchange_type='fanout')

# 发布消息（fanout 模式不需要 routing_key）
channel.basic_publish(exchange='notifications', routing_key='', body='系统维护通知')

print("通知已发布")
connection.close()
```

```python
# rabbitmq_subscribe.py - 订阅消息
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='notifications', exchange_type='fanout')

# 创建临时队列（断开连接后自动删除）
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 将临时队列绑定到交换机
channel.queue_bind(exchange='notifications', queue=queue_name)

def callback(ch, method, properties, body):
    print(f"收到通知: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("等待通知...")
channel.start_consuming()
```

### RabbitMQ 主题路由

使用 Topic Exchange 根据路由键的通配符匹配来分发消息：

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明 topic 类型的交换机
channel.exchange_declare(exchange='logs', exchange_type='topic')

# 发送不同类型的日志
channel.basic_publish(exchange='logs', routing_key='sys.error', body='系统错误日志')
channel.basic_publish(exchange='logs', routing_key='sys.info', body='系统信息日志')
channel.basic_publish(exchange='logs', routing_key='app.error', body='应用错误日志')
channel.basic_publish(exchange='logs', routing_key='app.info', body='应用信息日志')

print("日志已发送")
connection.close()
```

```python
# 只接收所有 error 日志
channel.queue_bind(exchange='logs', queue=queue_name, routing_key='*.error')

# 接收 sys 下的所有日志
channel.queue_bind(exchange='logs', queue=queue_name, routing_key='sys.*')

# 接收所有日志
channel.queue_bind(exchange='logs', queue=queue_name, routing_key='#')
```

### Kafka 消费者组

消费者组是 Kafka 实现负载均衡的方式。同一个组内的消费者共同分担一个 Topic 的消息，每条消息只会被组内一个消费者处理：

```python
from kafka import KafkaConsumer

# 消费者 1
consumer1 = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='order-processors',  # 同一个消费者组
    auto_offset_reset='earliest'
)

# 消费者 2（另一个进程）
consumer2 = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    group_id='order-processors',  # 同一个消费者组
    auto_offset_reset='earliest'
)

# 两个消费者会各自处理一部分消息，不会重复
```

### Kafka 发送带键的消息

键（Key）用于控制消息分配到哪个分区，相同键的消息会进入同一个分区：

```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 发送带键的消息（相同用户 ID 的订单进入同一分区，保证顺序）
producer.send('orders', key='user-123', value={'item': '笔记本', 'price': 5999})
producer.send('orders', key='user-456', value={'item': '手机', 'price': 3999})
producer.send('orders', key='user-123', value={'item': '鼠标', 'price': 199})

producer.flush()
producer.close()
```

## 常见场景

### 异步任务处理

用户注册后发送欢迎邮件，不需要等邮件发完才返回响应：

```python
import pika
import json

# Web 请求处理中：把任务放入队列
def register_user(username, email):
    # 保存用户到数据库...
    # 将发送邮件的任务放入队列
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_tasks')
    channel.basic_publish(
        exchange='',
        routing_key='email_tasks',
        body=json.dumps({'type': 'welcome', 'email': email, 'username': username})
    )
    connection.close()
    return "注册成功"

# 邮件发送 Worker：从队列取出任务并发送
def email_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_tasks')

    def callback(ch, method, properties, body):
        task = json.loads(body)
        # 发送邮件的逻辑
        print(f"发送{task['type']}邮件给 {task['email']}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='email_tasks', on_message_callback=callback)
    channel.start_consuming()
```

### 日志收集

使用 Kafka 收集多个服务的日志：

```python
# 各个服务中的日志生产者
from kafka import KafkaProducer
import json
import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def log(level, service, message):
    """发送日志到 Kafka"""
    producer.send('app-logs', {
        'timestamp': datetime.datetime.now().isoformat(),
        'level': level,
        'service': service,
        'message': message
    })

# 使用
log('ERROR', 'payment-service', '支付超时')
log('INFO', 'user-service', '用户登录成功')
```

## 注意事项与常见错误

### 消息确认机制

RabbitMQ 中如果 auto_ack=True，消息一旦投递就从队列中删除。如果消费者处理失败，消息就丢失了。生产环境应该使用手动确认：

```python
# 关闭自动确认
channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=False)

def callback(ch, method, properties, body):
    try:
        # 处理消息
        process_message(body)
        # 处理成功，确认消息
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception:
        # 处理失败，拒绝消息并重新入队
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
```

### 消息持久化

默认情况下 RabbitMQ 重启后消息会丢失。需要同时设置队列持久化和消息持久化：

```python
# 队列持久化
channel.queue_declare(queue='tasks', durable=True)

# 消息持久化
channel.basic_publish(
    exchange='',
    routing_key='tasks',
    body=message,
    properties=pika.BasicProperties(delivery_mode=2)  # 2 表示持久化
)
```

### Kafka 消费者偏移量

Kafka 消费者需要管理偏移量。如果 auto_offset_reset 设置不当，可能重复消费或丢失消息：

- earliest：从最早的消息开始消费（适合首次启动）
- latest：只消费启动后的新消息（默认值）

### 连接断开处理

消息队列的连接可能因为网络问题断开，生产环境需要处理重连：

```python
import pika

def create_connection():
    """创建带自动重连的连接"""
    while True:
        try:
            connection = pika.BlockingConnection(
                pika.ConnectionParameters('localhost')
            )
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("连接失败，5 秒后重试...")
            time.sleep(5)
```

## 进阶用法

### RabbitMQ 延迟消息

通过 TTL（存活时间）和死信队列实现延迟消息：

```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明延迟队列（消息过期后转到目标队列）
channel.queue_declare(
    queue='delay_queue',
    arguments={
        'x-message-ttl': 60000,              # 消息存活 60 秒
        'x-dead-letter-exchange': '',         # 过期后转到默认交换机
        'x-dead-letter-routing-key': 'target' # 转到目标队列
    }
)

# 目标队列
channel.queue_declare(queue='target')

# 发送延迟消息（60 秒后才会出现在 target 队列）
channel.basic_publish(exchange='', routing_key='delay_queue', body='延迟消息')

connection.close()
```

### Kafka 批量消费

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'events',
    bootstrap_servers='localhost:9092',
    group_id='batch-processor',
    auto_offset_reset='earliest'
)

batch = []
batch_size = 100

for message in consumer:
    batch.append(message.value.decode('utf-8'))

    if len(batch) >= batch_size:
        # 批量处理
        process_batch(batch)
        # 手动提交偏移量
        consumer.commit()
        batch = []
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
| Python与Redis | 016-PythonRedis | 本文的并列主题 |
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
| Python与消息队列 | 032-PythonMessageQueue | 本文自身 |
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
