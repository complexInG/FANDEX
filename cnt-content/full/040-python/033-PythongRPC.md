---
order: 77
title: Python与gRPC
module: python
category: Python
difficulty: intermediate
description: gRPC与Protocol Buffers
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与消息队列
  - python/Python与WebSocket
  - 'python/Python与CI-CD'
  - python/Python与性能优化
prerequisites:
  - python/语法速查
---

## 什么是 gRPC

gRPC 是 Google 开发的高性能远程过程调用（RPC）框架。它让客户端像调用本地函数一样调用服务器上的函数，不需要关心底层的网络通信细节。

gRPC 使用 Protocol Buffers（简称 protobuf）作为接口定义语言和序列化格式，默认基于 HTTP/2 协议传输，支持双向流、连接多路复用等特性。与 REST API 相比，gRPC 的数据传输更紧凑、速度更快，特别适合微服务之间的高效通信。

## 基础概念

### Protocol Buffers

Protocol Buffers 是一种结构化数据序列化格式，类似于 JSON，但更小、更快。你在一个 .proto 文件中定义数据结构，protobuf 编译器会自动生成 Python 代码。

### 服务定义

在 .proto 文件中定义服务接口，包括方法名、请求参数和响应参数。gRPC 支持四种通信模式：

- 一元调用（Unary）：客户端发一个请求，服务器回一个响应，类似普通函数调用
- 服务端流：客户端发一个请求，服务器回一个流式响应
- 客户端流：客户端发一个流式请求，服务器回一个响应
- 双向流：双方都可以流式发送消息

### 存根（Stub）

客户端通过存根调用服务端的方法。存根是 protobuf 编译器根据 .proto 文件自动生成的客户端代码，它把方法调用转换为网络请求。

## 快速上手

### 安装依赖

```bash
# 安装 gRPC 和 protobuf 工具
pip install grpcio grpcio-tools
```

### 定义 Protobuf 文件

创建文件 `greeter.proto`：

```protobuf
// 指定 protobuf 语法版本
syntax = "proto3";

// 包名
package greeter;

// 定义请求消息
message HelloRequest {
  string name = 1;
}

// 定义响应消息
message HelloReply {
  string message = 1;
}

// 定义服务
service Greeter {
  // 一元调用：发送名字，返回问候
  rpc SayHello (HelloRequest) returns (HelloReply);
}
```

### 生成 Python 代码

```bash
# 从 proto 文件生成 Python 代码
python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  greeter.proto
```

这会生成两个文件：`greeter_pb2.py`（消息类）和 `greeter_pb2_grpc.py`（服务存根）。

### 编写服务端

```python
# server.py
import grpc
from concurrent import futures
import greeter_pb2
import greeter_pb2_grpc

# 实现服务接口
class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        """处理 SayHello 请求"""
        # request.name 就是客户端传来的名字
        reply = greeter_pb2.HelloReply(message=f"你好, {request.name}!")
        return reply

# 启动服务器
def serve():
    # 创建 gRPC 服务器，使用线程池处理并发
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 注册服务
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    # 监听端口
    server.add_insecure_port('[::]:50051')
    server.start()
    print("服务器已启动，监听端口 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

### 编写客户端

```python
# client.py
import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    # 连接到 gRPC 服务器
    with grpc.insecure_channel('localhost:50051') as channel:
        # 创建存根
        stub = greeter_pb2_grpc.GreeterStub(channel)
        # 调用远程方法
        response = stub.SayHello(greeter_pb2.HelloRequest(name='世界'))
        print(f"收到响应: {response.message}")

if __name__ == '__main__':
    run()
```

## 详细用法

### 定义复杂消息类型

```protobuf
syntax = "proto3";
package ecommerce;

// 商品消息
message Product {
  int32 id = 1;
  string name = 2;
  float price = 3;
  repeated string tags = 4;  // 列表类型
}

// 订单消息
message Order {
  int32 id = 1;
  string user_id = 2;
  repeated Product items = 3;  // 嵌套消息的列表
  double total = 4;
}

// 请求和响应
message GetOrderRequest {
  int32 order_id = 1;
}

message ListOrdersRequest {
  string user_id = 1;
  int32 page_size = 2;
}

message ListOrdersResponse {
  repeated Order orders = 1;
}

// 订单服务
service OrderService {
  rpc GetOrder(GetOrderRequest) returns (Order);
  rpc ListOrders(ListOrdersRequest) returns (ListOrdersResponse);
}
```

### 服务端流式响应

```protobuf
// 服务端流：服务器持续推送数据
message SubscribeRequest {
  string topic = 1;
}

message Notification {
  string message = 1;
  int64 timestamp = 2;
}

service NotificationService {
  // returns 前面加 stream 表示服务端流
  rpc Subscribe(SubscribeRequest) returns (stream Notification);
}
```

```python
# 服务端实现
import time
import grpc
import notification_pb2
import notification_pb2_grpc

class NotificationServicer(notification_pb2_grpc.NotificationServiceServicer):
    def Subscribe(self, request, context):
        """持续推送通知"""
        count = 0
        while context.is_active():  # 客户端还在线
            count += 1
            yield notification_pb2.Notification(
                message=f"[{request.topic}] 通知 #{count}",
                timestamp=int(time.time())
            )
            time.sleep(2)  # 每 2 秒推送一条
```

```python
# 客户端接收流式响应
def subscribe():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = notification_pb2_grpc.NotificationServiceStub(channel)
        # 迭代接收流式响应
        for notification in stub.Subscribe(
            notification_pb2.SubscribeRequest(topic='news')
        ):
            print(f"收到通知: {notification.message}")
```

### 客户端流式请求

```protobuf
// 客户端流：客户端持续发送数据
message UploadChunk {
  string filename = 1;
  bytes data = 2;
}

message UploadResponse {
  bool success = 1;
  int32 size = 2;
}

service FileService {
  // 请求前面加 stream 表示客户端流
  rpc Upload(stream UploadChunk) returns (UploadResponse);
}
```

```python
# 服务端实现
class FileServicer(file_pb2_grpc.FileServiceServicer):
    def Upload(self, request_iterator, context):
        """接收客户端流式上传"""
        total_size = 0
        for chunk in request_iterator:
            total_size += len(chunk.data)
            # 在这里处理每个数据块（如写入文件）
        return file_pb2.UploadResponse(success=True, size=total_size)
```

### 错误处理

```python
import grpc
from grpc import StatusCode

class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        if not request.name:
            # 返回错误状态码
            context.set_code(StatusCode.INVALID_ARGUMENT)
            context.set_details("名字不能为空")
            return greeter_pb2.HelloReply()

        return greeter_pb2.HelloReply(message=f"你好, {request.name}!")
```

客户端处理错误：

```python
try:
    response = stub.SayHello(greeter_pb2.HelloRequest(name=''))
except grpc.RpcError as e:
    print(f"错误码: {e.code()}")     # INVALID_ARGUMENT
    print(f"错误详情: {e.details()}")  # 名字不能为空
```

### 添加超时

```python
# 客户端设置超时（5 秒）
try:
    response = stub.SayHello(
        greeter_pb2.HelloRequest(name='测试'),
        timeout=5
    )
except grpc.RpcError as e:
    if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
        print("请求超时")
```

## 常见场景

### 微服务间通信

在微服务架构中，gRPC 常用于服务间的内部通信。相比 REST API，gRPC 更快、更节省带宽：

```python
# 用户服务客户端
class UserClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('user-service:50051')
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    def get_user(self, user_id: int):
        try:
            return self.stub.GetUser(user_pb2.GetUserRequest(id=user_id), timeout=3)
        except grpc.RpcError:
            return None

    def close(self):
        self.channel.close()
```

### 在 FastAPI 中集成 gRPC

```python
from fastapi import FastAPI, HTTPException
import grpc
import user_pb2
import user_pb2_grpc

app = FastAPI()

# 创建 gRPC 客户端连接
channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserServiceStub(channel)

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    try:
        response = stub.GetUser(
            user_pb2.GetUserRequest(id=user_id),
            timeout=5
        )
        return {"id": response.id, "name": response.name}
    except grpc.RpcError as e:
        raise HTTPException(status_code=404, detail="用户不存在")
```

## 注意事项与常见错误

### protobuf 字段编号不能修改

.proto 文件中每个字段后面的编号（如 `string name = 1;` 中的 1）一旦确定就不能修改。修改编号会导致旧数据无法正确反序列化。新增字段应该使用新的编号。

### 默认值与字段存在性

protobuf3 中所有字段都有默认值（字符串为空串、数字为 0、布尔为 false）。你无法区分一个字段是未设置还是被设置为默认值。如果需要区分，可以使用 `optional` 关键字：

```protobuf
message Example {
  optional string name = 1;  // 可以区分未设置和空串
}
```

### 连接管理

gRPC 连接是长连接，应该复用而不是每次请求都创建新连接。在应用启动时创建连接，在关闭时释放：

```python
# 好的做法：复用连接
channel = grpc.insecure_channel('localhost:50051')
stub = MyServiceStub(channel)
# 多次使用 stub...
# 应用关闭时
channel.close()
```

### 不要在 gRPC 中传输大文件

gRPC 默认最大消息大小为 4MB。如果需要传输大文件，应该使用流式传输分块发送，或者使用对象存储（如 S3）只传输文件 URL。

## 进阶用法

### 使用 TLS 加密

```python
# 安全连接（TLS）
import grpc

# 读取证书
with open('server.crt', 'rb') as f:
    credentials = grpc.ssl_channel_credentials(f.read())

channel = grpc.secure_channel('localhost:50051', credentials)
```

### 拦截器

拦截器类似于中间件，可以在请求前后添加通用逻辑（如日志、认证）：

```python
import grpc
import time

class LoggingInterceptor(grpc.ServerInterceptor):
    """日志拦截器"""
    def intercept_service(self, continuation, handler_call_details):
        start = time.time()
        method = handler_call_details.method
        print(f"收到请求: {method}")

        handler = continuation(handler_call_details)

        duration = time.time() - start
        print(f"请求完成: {method}, 耗时: {duration:.3f}s")
        return handler

# 使用拦截器
server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10),
    interceptors=[LoggingInterceptor()]
)
```

### 健康检查

gRPC 内置了健康检查协议：

```python
from grpc_health.v1 import health, health_pb2, health_pb2_grpc

# 创建健康检查服务
health_servicer = health.HealthServicer()
health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

# 设置服务状态为健康
health_servicer.set('', health_pb2.HealthCheckResponse.SERVING)
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
| Python与gRPC | 033-PythongRPC | 本文自身 |
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
