---
order: 72
title: Python与日志
module: python
category: Python
difficulty: beginner
description: logging模块与日志配置
author: fanquanpp
updated: '2026-08-01'
related:
  - python/函数详解
  - python/Python与测试
  - python/Python与加密
  - python/Python与CLI
prerequisites:
  - python/语法速查
---

## 什么是日志

日志是程序运行时输出的记录信息。当程序出现问题时，日志是你排查错误的主要依据。没有日志的程序就像黑盒，出了问题完全无从下手。

Python 标准库中的 logging 模块提供了完整的日志功能，不需要安装第三方库。它支持多种日志级别、灵活的输出格式、文件轮转等特性，能满足从简单脚本到大型项目的各种需求。

## 基础概念

### 日志级别

日志级别从低到高分为五级，不同级别表示信息的重要程度不同：

- DEBUG：调试信息，最详细的日志，只在开发时使用
- INFO：普通信息，确认程序按预期运行
- WARNING：警告信息，表示有潜在问题，但程序仍能正常工作
- ERROR：错误信息，某些功能无法正常执行
- CRITICAL：严重错误，程序可能无法继续运行

设置日志级别后，只有等于或高于该级别的日志才会被输出。例如设置为 INFO，则 DEBUG 级别的日志不会显示。

### Logger、Handler 与 Formatter

- Logger：日志记录器，是代码中直接使用的接口。每个 Logger 有一个名称，通常用模块名命名
- Handler：日志处理器，决定日志输出到哪里（控制台、文件、网络等）
- Formatter：日志格式器，决定日志的输出格式

一个 Logger 可以有多个 Handler，每个 Handler 可以有自己的 Formatter。

## 快速上手

### 最简单的日志

```python
import logging

# 配置基本日志（只需一行）
logging.basicConfig(level=logging.INFO)

# 输出不同级别的日志
logging.debug("这是调试信息")      # 不会显示（级别低于 INFO）
logging.info("程序启动成功")       # 会显示
logging.warning("磁盘空间不足")    # 会显示
logging.error("文件读取失败")      # 会显示
logging.critical("数据库连接断开") # 会显示
```

### 自定义日志格式

```python
import logging

# 配置日志格式
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

logger.info("处理开始")
logger.error("出错了")
```

输出示例：

```
2026-01-15 10:30:00 [INFO] __main__: 处理开始
2026-01-15 10:30:01 [ERROR] __main__: 出错了
```

### 输出到文件

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename='app.log',      # 日志输出到文件
    filemode='a'             # 追加模式（默认），'w' 为覆盖模式
)

logging.info("这条日志会写入 app.log 文件")
```

## 详细用法

### 使用 Logger 对象

在大型项目中，应该为每个模块创建独立的 Logger，而不是直接使用 logging.info：

```python
import logging

# 为不同模块创建不同的 Logger
db_logger = logging.getLogger('app.database')
api_logger = logging.getLogger('app.api')

# 配置根 Logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

# 不同模块的日志会带上不同的 Logger 名称
db_logger.info("数据库连接成功")   # 显示 app.database
api_logger.info("API 请求处理中")  # 显示 app.api
db_logger.error("查询超时")       # 显示 app.database
```

### 同时输出到控制台和文件

```python
import logging

# 创建 Logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# 创建控制台 Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 控制台只显示 INFO 及以上

# 创建文件 Handler
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # 文件记录所有级别

# 创建格式器
formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
)

# 给 Handler 设置格式
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 给 Logger 添加 Handler
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 使用
logger.debug("这条只写入文件")     # 控制台不显示
logger.info("这条同时显示和写入")   # 控制台和文件都有
logger.error("错误信息")
```

### 日志文件轮转

长期运行的应用如果一直写入同一个日志文件，文件会越来越大。使用 RotatingFileHandler 可以按文件大小轮转：

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)

# 创建轮转文件 Handler
# maxBytes：单个文件最大字节数（这里设为 10MB）
# backupCount：保留的备份文件数量
handler = RotatingFileHandler(
    'app.log',
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5,
    encoding='utf-8'
)

handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s'
))
logger.addHandler(handler)

# 当 app.log 达到 10MB 时，会自动重命名为 app.log.1
# 然后创建新的 app.log 继续写入
# 最多保留 5 个备份文件（app.log.1 到 app.log.5）
```

### 按时间轮转日志

```python
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)

# 创建按时间轮转的 Handler
handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',    # 每天午夜轮转
    interval=1,         # 间隔
    backupCount=30,     # 保留 30 天的日志
    encoding='utf-8'
)

# when 参数可选值：
# 'S' - 秒, 'M' - 分, 'H' - 小时, 'D' - 天
# 'midnight' - 每天午夜, 'W0'-'W6' - 每周几（W0=周一）

handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s'
))
logger.addHandler(handler)
```

### 记录异常信息

当捕获异常时，使用 exc_info=True 可以把完整的堆栈跟踪写入日志：

```python
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

try:
    result = 1 / 0
except ZeroDivisionError:
    # exc_info=True 会记录完整的异常堆栈
    logging.error("计算出错", exc_info=True)

# 也可以用 logging.exception()，它自动设置 exc_info=True
try:
    result = 1 / 0
except ZeroDivisionError:
    logging.exception("计算出错")
```

### 使用字典配置

对于复杂项目，可以使用字典来配置日志，比代码配置更清晰：

```python
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(name)s %(funcName)s:%(lineno)d: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'myapp': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
        },
        'myapp.database': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': False,  # 不向父 Logger 传播
        },
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
}

# 应用配置
logging.config.dictConfig(LOGGING_CONFIG)

# 使用
logger = logging.getLogger('myapp')
logger.info("应用启动")
```

### 结构化日志（JSON 格式）

在微服务和日志分析平台（如 ELK）中，JSON 格式的日志更容易被机器解析：

```python
import logging
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    """自定义 JSON 格式化器"""
    def format(self, record):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'line': record.lineno,
        }
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_entry, ensure_ascii=False)

# 使用 JSON 格式化器
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())

logger = logging.getLogger('myapp')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info("用户登录", extra={'user_id': 123})
```

## 常见场景

### FastAPI 项目中的日志配置

```python
import logging
from logging.handlers import RotatingFileHandler
from fastapi import FastAPI, Request
import time

app = FastAPI()

# 配置日志
logger = logging.getLogger('api')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    'api.log', maxBytes=10*1024*1024, backupCount=5, encoding='utf-8'
)
handler.setFormatter(logging.Formatter(
    '%(asctime)s [%(levelname)s] %(message)s'
))
logger.addHandler(handler)

# 请求日志中间件
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(
        f"{request.method} {request.url.path} "
        f"status={response.status_code} duration={duration:.3f}s"
    )
    return response

@app.get("/users")
async def get_users():
    logger.info("获取用户列表")
    return {"users": []}
```

### 在类中使用日志

```python
import logging

class UserService:
    """在类中使用日志的推荐方式"""
    def __init__(self):
        # 用类名作为 Logger 名称
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_user(self, user_id: int):
        self.logger.info(f"查询用户: user_id={user_id}")
        try:
            user = self._fetch_user(user_id)
            self.logger.debug(f"查询成功: {user}")
            return user
        except Exception as e:
            self.logger.error(f"查询失败: user_id={user_id}", exc_info=True)
            raise

    def _fetch_user(self, user_id):
        # 模拟数据库查询
        return {"id": user_id, "name": "张三"}
```

## 注意事项与常见错误

### 不要用 print 代替 logging

print 输出的信息无法控制级别、无法关闭、无法写入文件、无法添加时间戳。在正式项目中，始终使用 logging 而不是 print。

### 日志中的敏感信息

不要在日志中记录密码、Token、身份证号等敏感信息。如果必须记录，应该脱敏处理：

```python
# 错误：记录了明文密码
# logger.info(f"用户登录: password={password}")

# 正确：脱敏处理
logger.info(f"用户登录: password=***")
```

### 避免在日志中使用 f-string 的性能陷阱

当日志级别被过滤时，f-string 仍然会被求值。使用 % 格式化或延迟格式化可以避免这个问题：

```python
# 不推荐：即使 DEBUG 级别被过滤，f-string 仍然会执行
# logger.debug(f"处理数据: {expensive_function()}")

# 推荐：使用 % 格式化，只在日志实际输出时才求值
logger.debug("处理数据: %s", expensive_function)

# 或者用 logger.isEnabledFor 检查
if logger.isEnabledFor(logging.DEBUG):
    logger.debug(f"处理数据: {expensive_function()}")
```

### Logger 的传播机制

默认情况下，子 Logger 的日志会向上传播给父 Logger。如果你给子 Logger 添加了 Handler，又没有设置 propagate=False，日志可能会被重复输出：

```python
# 设置不向父 Logger 传播
child_logger = logging.getLogger('myapp.child')
child_logger.propagate = False  # 防止日志重复输出
```

### basicConfig 只在第一次调用时生效

logging.basicConfig() 只在第一次调用时生效。如果之前已经调用过（或者其他库已经配置过日志），再次调用不会有效果。建议在程序入口处尽早调用 basicConfig。

## 进阶用法

### 自定义 Handler 发送日志到远程服务

```python
import logging
import json
import urllib.request

class WebhookHandler(logging.Handler):
    """将日志发送到 Webhook（如飞书、钉钉、Slack）"""

    def __init__(self, webhook_url: str):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        try:
            # 只发送 ERROR 及以上级别的日志
            if record.levelno < logging.ERROR:
                return

            log_entry = {
                'level': record.levelname,
                'message': record.getMessage(),
                'logger': record.name,
                'timestamp': record.created,
            }

            data = json.dumps(log_entry).encode('utf-8')
            req = urllib.request.Request(
                self.webhook_url,
                data=data,
                headers={'Content-Type': 'application/json'}
            )
            urllib.request.urlopen(req)
        except Exception:
            # 日志发送失败不应该影响程序运行
            self.handleError(record)

# 使用
logger = logging.getLogger('myapp')
logger.addHandler(WebhookHandler('https://your-webhook-url'))
```

### 使用 structlog 库

structlog 是一个更现代的日志库，提供更好的结构化日志支持：

```bash
pip install structlog
```

```python
import structlog

# 配置 structlog
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer(),  # 开发环境用彩色控制台输出
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
)

logger = structlog.get_logger()

# 使用关键字参数记录结构化日志
logger.info("用户登录", user_id=123, ip="192.168.1.1")
logger.error("支付失败", order_id="ORD-001", reason="余额不足")
```

### 使用 loguru 库

loguru 是一个更简洁的日志库，开箱即用，不需要复杂配置：

```bash
pip install loguru
```

```python
from loguru import logger

# 默认输出到控制台，带颜色
logger.info("程序启动")

# 添加文件输出
logger.add("app.log", rotation="10 MB", retention="30 days", encoding="utf-8")

# 不同级别
logger.debug("调试信息")
logger.info("普通信息")
logger.warning("警告信息")
logger.error("错误信息")

# 记录异常
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("计算出错")

# 结构化日志
logger.info("用户登录", user_id=123, ip="192.168.1.1")
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
| Python与日志 | 027-PythonLog | 本文自身 |
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
