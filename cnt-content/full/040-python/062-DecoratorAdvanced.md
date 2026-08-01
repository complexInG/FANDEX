---
order: 111
title: 装饰器进阶
module: python
category: 'dev-lang'
difficulty: advanced
description: Python装饰器进阶详解：带参数装饰器、类装饰器、functools.wraps。
author: fanquanpp
updated: '2026-08-01'
related:
  - python/上下文管理器
  - python/描述符
  - python/元类与单例模式
  - python/生成器与协程
prerequisites:
  - python/语法速查
---
### functools.wraps 保留元信息

```python
import functools

def log(func):
    @functools.wraps(func)  # 保留原函数的 __name__、__doc__ 等
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name):
    """问候函数"""
    return f"Hello, {name}"

print(greet.__name__)  # greet（没有 @wraps 则是 wrapper）
print(greet.__doc__)   # 问候函数
```

## 类装饰器

**基本写法：类作为装饰器**
`class <装饰器类>:\n    def __init__(self, func): ...\n    def __call__(self, *args):`
```python
# 类装饰器通过 __call__ 实现
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"第 {self.count} 次调用")
        return self.func(*args, **kwargs)

@Counter
def hello():
    print("hi")

hello(); hello()
```

**基本写法：带参数类装饰器**
`class <类>:\n    def __init__(self, <参数>): ...\n    def __call__(self, func):`
```python
# 带参数的类装饰器
class Retry:
    def __init__(self, times=3):
        self.times = times
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(self.times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == self.times - 1:
                        raise
        return wrapper

@Retry(times=5)
def fetch():
    pass
```

---

### 装饰器堆叠

多个装饰器从下往上应用，执行时从上往下：

```python
@decorator_a  # 第二个应用
@decorator_b  # 第一个应用
def func():
    pass

# 等价于
func = decorator_a(decorator_b(func))
```

```python
import functools

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold      # 外层
@italic    # 内层
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # <b><i>Hello, Alice</i></b>
```

## 概述

装饰器是 Python 中强大的语法特性，用于在不修改原函数代码的情况下扩展其功能。进阶装饰器包括带参数的装饰器、类装饰器、装饰器堆叠和保留函数元信息等。掌握装饰器进阶技巧是编写优雅 Python 代码的关键。

## 基础概念

### 装饰器的本质

装饰器是一个接受函数作为参数并返回新函数的可调用对象。`@decorator` 语法只是语法糖：

```python
# 以下两种写法等价
@decorator
def func():
    pass

def func():
    pass
func = decorator(func)
```

### 闭包与装饰器

装饰器利用闭包捕获原函数的引用：

```python
def log(func):
    """简单的日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回")
        return result
    return wrapper

@log
def greet(name):
    return f"Hello, {name}"

greet("Alice")  # 调用 greet → Hello, Alice → greet 返回
```

## 快速上手

### 带参数的装饰器

```python
def retry(max_attempts=3, delay=1.0):
    """带参数的重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2.0)
def fetch_data(url):
    return requests.get(url).json()
```

## 详细用法

### 方法装饰器

```python
def validate_positive(func):
    """验证参数为正数"""
    @functools.wraps(func)
    def wrapper(self, value, *args, **kwargs):
        if value <= 0:
            raise ValueError("值必须为正数")
        return func(self, value, *args, **kwargs)
    return wrapper

class Account:
    def __init__(self):
        self._balance = 0

    @validate_positive
    def deposit(self, amount):
        """存款"""
        self._balance += amount
        return self._balance

    @validate_positive
    def withdraw(self, amount):
        """取款"""
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
        return self._balance
```

### 类方法装饰器

```python
def classmethod_decorator(func):
    @functools.wraps(func)
    def wrapper(cls, *args, **kwargs):
        print(f"在类 {cls.__name__} 上调用 {func.__name__}")
        return func(cls, *args, **kwargs)
    return wrapper

class Factory:
    @classmethod
    @classmethod_decorator
    def create(cls, name):
        return cls(name)
```

### 缓存装饰器

```python
import functools

def cache(ttl=60):
    """带过期时间的缓存装饰器"""
    def decorator(func):
        cache_store = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import time
            key = (args, frozenset(kwargs.items()))
            if key in cache_store:
                result, timestamp = cache_store[key]
                if time.time() - timestamp < ttl:
                    return result

            result = func(*args, **kwargs)
            cache_store[key] = (result, time.time())
            return result

        wrapper.cache_clear = lambda: cache_store.clear()
        return wrapper
    return decorator

@cache(ttl=30)
def expensive_query(sql):
    return db.execute(sql)
```

### 类型保留装饰器

```python
from typing import TypeVar, Callable, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def typed_decorator(func: Callable[P, R]) -> Callable[P, R]:
    """保留类型签名的装饰器"""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)
    return wrapper
```

## 常见场景

### 场景一：权限检查

```python
def require_role(role):
    """权限检查装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.current_user.role != role:
                raise PermissionError(f"需要 {role} 权限")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

class AdminPanel:
    def __init__(self, user):
        self.current_user = user

    @require_role("admin")
    def delete_user(self, user_id):
        return f"已删除用户 {user_id}"
```

### 场景二：速率限制

```python
import time
import threading

def rate_limit(calls_per_second=10):
    """速率限制装饰器"""
    min_interval = 1.0 / calls_per_second
    lock = threading.Lock()
    last_called = [0.0]

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                elapsed = time.time() - last_called[0]
                if elapsed < min_interval:
                    time.sleep(min_interval - elapsed)
                last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_per_second=5)
def api_call(endpoint):
    return requests.get(endpoint)
```

### 场景三：自动注册

```python
registry = {}

def register(name):
    """自动注册装饰器"""
    def decorator(cls):
        registry[name] = cls
        return cls
    return decorator

@register("mysql")
class MySQLHandler:
    pass

@register("redis")
class RedisHandler:
    pass

print(registry)  # {'mysql': <class 'MySQLHandler'>, 'redis': <class 'RedisHandler'>}
```

## 注意事项

- 始终使用 `@functools.wraps(func)` 保留原函数的元信息
- 装饰器返回的 wrapper 函数签名与原函数不同，可能影响文档和调试
- 带参数的装饰器需要三层嵌套函数，注意闭包变量的捕获
- 类装饰器中 `__call__` 方法会替代原函数，注意保留属性
- 装饰器在模块加载时执行，不是在函数调用时执行
- 过度使用装饰器会降低代码可读性，保持装饰器职责单一

## 进阶用法

### 使用 **wrapped** 访问原函数

```python
@log
def greet(name):
    return f"Hello, {name}"

# functools.wraps 自动设置 __wrapped__
original = greet.__wrapped__
print(original("Alice"))  # Hello, Alice（不经过装饰器）
```

### 装饰器与描述符结合

```python
class cached_property:
    """缓存属性描述符装饰器"""
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.func.__name__, value)  # 替换为实例属性
        return value

class DataLoader:
    def __init__(self, path):
        self.path = path

    @cached_property
    def data(self):
        print("加载数据...")
        with open(self.path) as f:
            return f.read()

loader = DataLoader("data.txt")
print(loader.data)  # 加载数据... + 内容
print(loader.data)  # 直接返回缓存
```

### 装饰器工厂模式

```python
class DecoratorFactory:
    """可配置的装饰器工厂"""
    def __init__(self, *, log_args=False, log_result=False, log_time=False):
        self.log_args = log_args
        self.log_result = log_result
        self.log_time = log_time

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.log_args:
                print(f"参数: {args}, {kwargs}")
            start = time.perf_counter()
            result = func(*args, **kwargs)
            if self.log_time:
                print(f"耗时: {time.perf_counter() - start:.3f}s")
            if self.log_result:
                print(f"返回: {result}")
            return result
        return wrapper

# 使用
debug = DecoratorFactory(log_args=True, log_result=True, log_time=True)

@debug
def compute(n):
    return sum(range(n))
```

### 异步装饰器

```python
import functools

def async_retry(max_attempts=3, delay=1.0):
    """异步重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    await asyncio.sleep(delay)
        return wrapper
    return decorator

@async_retry(max_attempts=3, delay=2.0)
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```
## 带参数装饰器

**基本写法：三层嵌套装饰器**
`def <装饰器>(<参数>):\n    def wrapper(func): ...\n    return wrapper`
```python
# 带参数的装饰器需要三层嵌套
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)
```

**基本写法：带关键字参数**
`def <装饰器>(<参数>=<默认值>):`
```python
# 带默认参数的装饰器
def logged(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] 调用 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@logged(level="DEBUG")
def process():
    pass
```

---

## 装饰类方法

**基本写法：装饰实例方法**
`def <装饰器>(method):\n    @functools.wraps(method)\n    def wrapper(self, *args, **kwargs):`
```python
# 装饰类的实例方法
def log_call(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"调用 {method.__name__}")
        return method(self, *args, **kwargs)
    return wrapper

class Service:
    @log_call
    def run(self):
        return "done"
```

**基本写法：装饰 classmethod 与 staticmethod**
`@classmethod` | `@staticmethod`
```python
# 注意装饰器顺序：staticmethod 应在最外层
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create(cls):
        return cls()
```

---

## 内置常用装饰器

**基本写法：functools.lru_cache**
`@functools.lru_cache(maxsize=<大小>)`
```python
# LRU 缓存装饰器
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))
```

**基本写法：functools.cache**
`@functools.cache`
```python
# 无限缓存（3.9+）
from functools import cache

@cache
def expensive(n):
    return sum(range(n))
```

**基本写法：functools.cached_property**
`@functools.cached_property`
```python
# 首次访问后缓存属性
from functools import cached_property

class Data:
    @cached_property
    def heavy(self):
        return list(range(1000000))
```

**基本写法：functools.singledispatch**
`@functools.singledispatch`
```python
# 单分派泛函数
from functools import singledispatch

@singledispatch
def process(data):
    raise TypeError("不支持的类型")

@process.register(int)
def _(data):
    return data * 2

@process.register(str)
def _(data):
    return data.upper()

print(process(5))
print(process("abc"))
```

**基本写法：functools.singledispatchmethod**
`@functools.singledispatchmethod`
```python
# 类方法单分派（3.8+）
from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    def process(self, data):
        raise TypeError

    @process.register
    def _(self, data: int):
        return data * 2
```

---

## dataclass 装饰器

**基本写法：dataclass 装饰器**
`@dataclasses.dataclass`
```python
# 自动生成 __init__/__repr__/__eq__
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

---

## 自定义属性访问装饰器

**基本写法：property**
`@property`
```python
# property 装饰器定义只读属性
class Circle:
    def __init__(self, r):
        self.r = r
    @property
    def area(self):
        return 3.14 * self.r ** 2
```

**基本写法：abstract 装饰器**
`@abc.abstractmethod`
```python
# 抽象方法装饰器
import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sound(self):
        pass
```

---

## warnings.deprecated（3.13+）

**基本写法：标记弃用**
`@warnings.deprecated(<消息>)`
```python
# Python 3.13 新增弃用装饰器
import warnings

@warnings.deprecated("使用 new_func 替代")
def old_func():
    pass
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
| 装饰器进阶 | 062-DecoratorAdvanced | 本文自身 |
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
