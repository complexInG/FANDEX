---
order: 78
title: Python与WebSocket
module: python
category: Python
difficulty: intermediate
description: WebSocket实时通信
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与消息队列
  - python/Python与gRPC
  - 'python/Python与CI-CD'
  - python/Python与性能优化
prerequisites:
  - python/语法速查
---

## 什么是 WebSocket

WebSocket 是一种在客户端和服务器之间建立持久双向通信的协议。传统的 HTTP 请求是单向的：客户端发请求，服务器返回响应，然后连接就断开了。如果服务器想主动给客户端推送数据，HTTP 做不到。

WebSocket 解决了这个问题。客户端和服务器通过一次 HTTP 握手建立连接后，双方可以随时互相发送数据，连接会一直保持，直到某一方主动关闭。这使得 WebSocket 特别适合实时聊天、在线协作、实时数据推送等场景。

## 基础概念

### 与 HTTP 的区别

HTTP 是请求-响应模式，每次通信都需要客户端先发起请求。WebSocket 在建立连接后，服务器可以主动向客户端推送数据，不需要客户端反复轮询。

### 连接生命周期

WebSocket 连接经历三个阶段：

- 握手：客户端发送 HTTP 请求，携带 Upgrade: websocket 头，服务器同意后升级协议
- 通信：双方通过连接自由发送文本或二进制消息
- 关闭：任一方发送关闭帧，连接断开

### 消息类型

WebSocket 支持两种消息类型：

- 文本消息：UTF-8 编码的字符串，常用于 JSON 数据
- 二进制消息：原始字节数据，常用于图片、音频等

## 快速上手

### 安装依赖

```bash
# 安装 FastAPI 和 uvicorn
pip install fastapi uvicorn

# 安装 WebSocket 客户端库（用于测试）
pip install websockets
```

### 最简单的 WebSocket 服务端

```python
# server.py - 最简单的 WebSocket 服务端
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 接受客户端连接
    await websocket.accept()
    try:
        while True:
            # 接收客户端发来的文本消息
            data = await websocket.receive_text()
            # 把消息原样发回（Echo 服务）
            await websocket.send_text(f"Echo: {data}")
    except Exception:
        # 客户端断开连接时退出循环
        pass
```

运行服务：

```bash
uvicorn server:app --reload
```

### 最简单的 WebSocket 客户端

```python
# client.py - 最简单的 WebSocket 客户端
import asyncio
import websockets

async def main():
    # 连接到 WebSocket 服务端
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        # 发送消息
        await ws.send("Hello, WebSocket!")
        # 接收回复
        response = await ws.recv()
        print(f"收到回复: {response}")

asyncio.run(main())
```

## 详细用法

### 处理连接和断开事件

在实际应用中，你需要知道客户端何时连接、何时断开，以便做相应的处理（如更新在线用户列表）：

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# 保存所有已连接的客户端
connected_clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 接受连接
    await websocket.accept()
    # 将新客户端加入列表
    connected_clients.append(websocket)
    print(f"客户端已连接，当前在线: {len(connected_clients)}")

    try:
        while True:
            data = await websocket.receive_text()
            # 处理收到的消息
            await websocket.send_text(f"你发送了: {data}")
    except WebSocketDisconnect:
        # 客户端断开连接
        connected_clients.remove(websocket)
        print(f"客户端已断开，当前在线: {len(connected_clients)}")
```

### 广播消息

广播是指将一条消息发送给所有已连接的客户端，这是聊天室等场景的核心功能：

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# 在线客户端列表
clients = []

async def broadcast(message: str):
    """向所有客户端广播消息"""
    for client in clients:
        try:
            await client.send_text(message)
        except Exception:
            # 发送失败说明客户端已断开
            clients.remove(client)

@app.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            # 将消息广播给所有人
            await broadcast(data)
    except WebSocketDisconnect:
        clients.remove(websocket)
        await broadcast("有人离开了聊天室")
```

### 发送和接收 JSON 数据

大多数实际应用中，WebSocket 传输的是结构化的 JSON 数据：

```python
import json
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            # 接收文本消息
            raw_data = await websocket.receive_text()
            # 解析 JSON
            data = json.loads(raw_data)

            # 根据消息类型做不同处理
            msg_type = data.get("type")

            if msg_type == "greeting":
                response = {
                    "type": "greeting_reply",
                    "message": f"你好, {data.get('name', '匿名')}!"
                }
            elif msg_type == "ping":
                response = {"type": "pong", "timestamp": data.get("timestamp")}
            else:
                response = {"type": "error", "message": "未知的消息类型"}

            # 发送 JSON 响应
            await websocket.send_text(json.dumps(response))
    except Exception:
        pass
```

客户端发送 JSON：

```python
import asyncio
import json
import websockets

async def main():
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        # 发送 JSON 格式的消息
        message = {"type": "greeting", "name": "小明"}
        await ws.send(json.dumps(message))

        # 接收并解析 JSON 响应
        response = json.loads(await ws.recv())
        print(f"收到: {response}")

asyncio.run(main())
```

### 发送二进制数据

WebSocket 也支持发送二进制数据，适合传输图片、文件等：

```python
@app.websocket("/ws/binary")
async def binary_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            # 接收二进制数据
            data = await websocket.receive_bytes()

            # 处理二进制数据（例如图片缩略图）
            # 这里简单地把数据原样返回
            await websocket.send_bytes(data)
    except Exception:
        pass
```

### 使用 WebSocket 路径参数

你可以像普通路由一样在 WebSocket 路径中使用参数：

```python
@app.websocket("/ws/room/{room_id}")
async def room_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            # 消息属于哪个房间
            await websocket.send_text(f"[房间 {room_id}] {data}")
    except WebSocketDisconnect:
        pass
```

### 使用查询参数

客户端连接时可以通过查询参数传递信息（如用户名、token）：

```python
@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...)  # 从查询参数获取 token
):
    # 先验证 token
    user = verify_token(token)
    if not user:
        await websocket.close(code=4001, reason="认证失败")
        return

    await websocket.accept()
    # 正常通信...
```

客户端连接时带上查询参数：

```python
# 连接时在 URL 中带上 token
async with websockets.connect("ws://localhost:8000/ws?token=abc123") as ws:
    await ws.send("Hello")
```

## 常见场景

### 实时聊天应用

```python
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# 按房间分组的客户端字典
rooms: dict[str, list] = {}

@app.websocket("/ws/chat/{room_id}")
async def chat_room(websocket: WebSocket, room_id: str):
    await websocket.accept()

    # 初始化房间
    if room_id not in rooms:
        rooms[room_id] = []
    rooms[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)

            # 构建广播消息
            broadcast_msg = json.dumps({
                "user": msg.get("user", "匿名"),
                "text": msg.get("text", ""),
                "room": room_id
            })

            # 向房间内所有人广播
            for client in rooms[room_id]:
                try:
                    await client.send_text(broadcast_msg)
                except Exception:
                    rooms[room_id].remove(client)
    except WebSocketDisconnect:
        rooms[room_id].remove(websocket)
        # 通知房间内其他人
        leave_msg = json.dumps({"system": True, "text": "有人离开了房间"})
        for client in rooms[room_id]:
            await client.send_text(leave_msg)
```

### 实时数据推送

服务器定时向客户端推送数据（如股票行情、系统监控）：

```python
import asyncio
import json
import random
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws/stock/{symbol}")
async def stock_price(websocket: WebSocket, symbol: str):
    await websocket.accept()

    try:
        while True:
            # 模拟实时股票价格
            price = round(random.uniform(100, 200), 2)
            change = round(random.uniform(-5, 5), 2)

            data = json.dumps({
                "symbol": symbol,
                "price": price,
                "change": change
            })

            await websocket.send_text(data)
            # 每秒推送一次
            await asyncio.sleep(1)
    except Exception:
        pass
```

### 进度通知

长时间运行的任务通过 WebSocket 实时报告进度：

```python
import asyncio
from fastapi import FastAPI, WebSocket

app = FastAPI()

async def long_running_task(websocket: WebSocket, task_id: str):
    """模拟一个耗时任务，逐步报告进度"""
    total_steps = 10
    for step in range(1, total_steps + 1):
        # 执行一步任务
        await asyncio.sleep(1)

        # 报告进度
        progress = int(step / total_steps * 100)
        await websocket.send_json({
            "task_id": task_id,
            "progress": progress,
            "status": "running" if progress < 100 else "completed"
        })

@app.websocket("/ws/task/{task_id}")
async def task_progress(websocket: WebSocket, task_id: str):
    await websocket.accept()
    try:
        await long_running_task(websocket, task_id)
    except Exception:
        pass
```

## 注意事项与常见错误

### 必须调用 accept()

在 FastAPI 中，WebSocket 处理函数的第一步必须是调用 `await websocket.accept()`，否则客户端无法建立连接。

### 处理断开连接

客户端可能随时断开连接（网络中断、用户关闭页面等），你的代码必须能正确处理这种情况。使用 try-except 捕获 WebSocketDisconnect 异常，清理资源。

### 不要在 WebSocket 中执行阻塞操作

WebSocket 处理函数是异步的，不要在其中执行阻塞的同步操作（如 time.sleep、同步数据库查询），否则会阻塞整个事件循环。使用 asyncio.sleep 替代 time.sleep。

### 连接数限制

每个 WebSocket 连接都会占用服务器资源。如果你的应用需要支持大量并发连接，需要注意：

- 使用负载均衡分散连接
- 设置心跳机制及时清理断开的连接
- 考虑使用专业的 WebSocket 服务（如 Redis Pub/Sub 做消息分发）

### 心跳保活

某些网络环境（如反向代理、防火墙）会自动关闭长时间空闲的连接。通过定期发送心跳消息来保持连接：

```python
import asyncio
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # 启动心跳任务
    async def heartbeat():
        while True:
            await asyncio.sleep(30)  # 每 30 秒发送一次心跳
            try:
                await websocket.send_json({"type": "ping"})
            except Exception:
                break

    heartbeat_task = asyncio.create_task(heartbeat())

    try:
        while True:
            data = await websocket.receive_text()
            # 处理消息...
    except Exception:
        pass
    finally:
        heartbeat_task.cancel()
```

## 进阶用法

### 使用连接管理器封装

对于复杂的应用，建议把连接管理逻辑封装到一个类中：

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict, List

class ConnectionManager:
    """WebSocket 连接管理器"""

    def __init__(self):
        # 按组管理的连接字典
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, group: str):
        """接受新连接并加入指定组"""
        await websocket.accept()
        if group not in self.active_connections:
            self.active_connections[group] = []
        self.active_connections[group].append(websocket)

    def disconnect(self, websocket: WebSocket, group: str):
        """断开连接并从组中移除"""
        if group in self.active_connections:
            self.active_connections[group].remove(websocket)
            if not self.active_connections[group]:
                del self.active_connections[group]

    async def broadcast(self, message: str, group: str):
        """向指定组的所有连接广播消息"""
        if group not in self.active_connections:
            return
        for connection in self.active_connections[group]:
            try:
                await connection.send_text(message)
            except Exception:
                self.disconnect(connection, group)

    async def send_personal(self, message: str, websocket: WebSocket):
        """向单个连接发送消息"""
        try:
            await websocket.send_text(message)
        except Exception:
            pass

# 使用连接管理器
manager = ConnectionManager()
app = FastAPI()

@app.websocket("/ws/{group}")
async def websocket_endpoint(websocket: WebSocket, group: str):
    await manager.connect(websocket, group)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data, group)
    except WebSocketDisconnect:
        manager.disconnect(websocket, group)
```

### 配合 Redis 实现跨进程通信

当你的应用运行多个进程时，不同进程的 WebSocket 连接无法直接通信。通过 Redis 的发布/订阅功能可以实现跨进程消息传递：

```python
import asyncio
import json
import redis.asyncio as redis
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

# Redis 客户端
redis_client = redis.from_url("redis://localhost:6379")

# 本进程的连接管理
local_connections: list[WebSocket] = []

async def redis_subscriber():
    """订阅 Redis 频道，接收其他进程的消息"""
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("chat_channel")
    async for message in pubsub.listen():
        if message["type"] == "message":
            data = message["data"].decode()
            # 向本进程的所有连接广播
            for ws in local_connections[:]:
                try:
                    await ws.send_text(data)
                except Exception:
                    local_connections.remove(ws)

# 应用启动时启动 Redis 订阅
@app.on_event("startup")
async def startup():
    asyncio.create_task(redis_subscriber())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    local_connections.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            # 发布到 Redis，让所有进程都能收到
            await redis_client.publish("chat_channel", data)
    except WebSocketDisconnect:
        local_connections.remove(websocket)
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
| Python与消息队列 | 032-PythonMessageQueue | 本文的并列主题 |
| Python与gRPC | 033-PythongRPC | 本文的并列主题 |
| Python与WebSocket | 034-PythonWebSocket | 本文自身 |
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
