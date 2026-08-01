---
order: 81
title: Python与设计模式
module: python
category: Python
difficulty: intermediate
description: Python实现设计模式
author: fanquanpp
updated: '2026-08-01'
related:
  - python/内置数据结构
  - python/正则表达式
  - python/Python与打包发布
  - python/Python与Jupyter
prerequisites:
  - python/语法速查
---

# Python 设计模式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 单例模式

**基本写法：模块级单例**
`<模块>.py`
```python
# 模块本身就是单例
# config.py
class Config:
    def __init__(self):
        self.settings = {}

config = Config()  # 模块变量

# 使用：from config import config
```

**基本写法：__new__ 实现**
`class <类>:\n    _instance = None\n    def __new__(cls):`
```python
# 通过 __new__ 控制实例化
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True
```

**基本写法：元类单例**
`class <元类>(type):\n    def __call__(cls):`
```python
# 元类实现单例
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DB(metaclass=SingletonMeta):
    pass
```

**基本写法：装饰器单例**
`def singleton(cls):`
```python
# 装饰器实现单例
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Service:
    pass
```

---

## 工厂模式

**基本写法：简单工厂**
`def create(<类型>):`
```python
# 工厂函数
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

def create_animal(kind):
    if kind == "dog":
        return Dog()
    if kind == "cat":
        return Cat()
    raise ValueError("未知类型")
```

**基本写法：工厂方法**
`class <类>:\n    def create(self):`
```python
# 工厂方法模式
class AnimalFactory:
    def create(self):
        raise NotImplementedError

class DogFactory(AnimalFactory):
    def create(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create(self):
        return Cat()
```

**基本写法：抽象工厂**
`class <抽象工厂>(abc.ABCMeta):`
```python
# 抽象工厂
import abc

class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self): pass
    @abc.abstractmethod
    def create_input(self): pass

class WinFactory(GUIFactory):
    def create_button(self): return WinButton()
    def create_input(self): return WinInput()
```

---

### 观察者模式

```python
class Observable:
    """可观察对象"""
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        """订阅事件"""
        self._observers.append(observer)

    def unsubscribe(self, observer):
        """取消订阅"""
        self._observers.remove(observer)

    def notify(self, event):
        """通知所有观察者"""
        for observer in self._observers:
            observer(event)

# 使用
class EventBus:
    """事件总线：观察者模式的应用"""
    def __init__(self):
        self._handlers = {}

    def on(self, event_type, handler):
        """注册事件处理器"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def emit(self, event_type, data=None):
        """触发事件"""
        for handler in self._handlers.get(event_type, []):
            handler(data)

# 使用示例
bus = EventBus()
bus.on("user_created", lambda data: print(f"欢迎新用户: {data}"))
bus.on("order_placed", lambda data: print(f"新订单: {data}"))
bus.emit("user_created", "Alice")
```

### 策略模式

策略模式允许在运行时选择算法。Python 中可以用函数代替策略类：

```python
# 传统类实现
class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy(data)

# Pythonic 实现：直接使用函数
def bubble_sort(data):
    """冒泡排序"""
    result = data[:]
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def quick_sort(data):
    """快速排序"""
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 使用
data = [3, 1, 4, 1, 5, 9]
sorted_data = quick_sort(data)  # 直接选择排序策略
```

### 装饰器模式

Python 的装饰器语法天然实现了装饰器模式：

```python
import functools
import time

def retry(max_attempts=3, delay=1):
    """重试装饰器"""
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

def timer(func):
    """计时装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} 耗时: {elapsed:.3f}s")
        return result
    return wrapper

# 组合使用多个装饰器
@timer
@retry(max_attempts=3, delay=2)
def fetch_data(url):
    """获取数据"""
    import requests
    return requests.get(url).json()
```

### 适配器模式

```python
class OldAPI:
    """旧版 API"""
    def get_user_info(self, user_id):
        return {"name": "Alice", "age": 30}

class NewAPI:
    """新版 API"""
    def fetch_user(self, user_id):
        return {"full_name": "Alice", "user_age": 30}

class UserAdapter:
    """适配器：统一新旧 API 的接口"""
    def __init__(self, api):
        self.api = api

    def get_name(self, user_id):
        data = self.api.fetch_user(user_id) if hasattr(self.api, 'fetch_user') \
            else self.api.get_user_info(user_id)
        return data.get("full_name") or data.get("name")

    def get_age(self, user_id):
        data = self.api.fetch_user(user_id) if hasattr(self.api, 'fetch_user') \
            else self.api.get_user_info(user_id)
        return data.get("user_age") or data.get("age")
```

## 概述

设计模式是面向对象编程中经过验证的解决方案模板，用于解决常见的软件设计问题。Python 的动态特性使得许多设计模式的实现比传统静态语言更简洁。本文介绍 Python 中常用的设计模式及其惯用实现方式，重点在于利用 Python 语言特性（如装饰器、元类、描述符等）实现更优雅的方案。

## 基础概念

### 设计模式分类

- 创建型：关注对象的创建机制，如单例、工厂、建造者
- 结构型：关注对象的组合方式，如适配器、装饰器、代理
- 行为型：关注对象间的通信，如策略、观察者、命令

### Python 的特殊之处

Python 的动态特性使得一些传统设计模式可以更简洁地实现：

- 不需要接口定义，鸭子类型天然支持多态
- 装饰器模式可以直接用 Python 装饰器实现
- 单例模式可以用模块级别变量实现
- 策略模式可以用函数代替类

## 快速上手

## 详细用法

### 建造者模式

```python
class QueryBuilder:
    """SQL 查询建造者"""
    def __init__(self):
        self._table = ""
        self._columns = []
        self._conditions = []
        self._order_by = ""
        self._limit = None

    def select(self, *columns):
        self._columns = columns or ["*"]
        return self

    def from_table(self, table):
        self._table = table
        return self

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def order_by(self, column):
        self._order_by = column
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        """构建 SQL 语句"""
        cols = ", ".join(self._columns)
        sql = f"SELECT {cols} FROM {self._table}"
        if self._conditions:
            sql += " WHERE " + " AND ".join(self._conditions)
        if self._order_by:
            sql += f" ORDER BY {self._order_by}"
        if self._limit:
            sql += f" LIMIT {self._limit}"
        return sql

# 使用
query = QueryBuilder() \
    .select("name", "age") \
    .from_table("users") \
    .where("age > 18") \
    .where("status = 'active'") \
    .order_by("name") \
    .limit(10) \
    .build()
# SELECT name, age FROM users WHERE age > 18 AND status = 'active' ORDER BY name LIMIT 10
```

## 常见场景

### 场景一：插件系统

```python
class PluginRegistry:
    """插件注册表"""
    _plugins = {}

    @classmethod
    def register(cls, name):
        """注册插件装饰器"""
        def decorator(plugin_class):
            cls._plugins[name] = plugin_class
            return plugin_class
        return decorator

    @classmethod
    def get(cls, name):
        return cls._plugins.get(name)

# 注册插件
@PluginRegistry.register("mysql")
class MySQLPlugin:
    def connect(self):
        return "MySQL 连接"

@PluginRegistry.register("postgres")
class PostgresPlugin:
    def connect(self):
        return "PostgreSQL 连接"

# 使用
plugin = PluginRegistry.get("mysql")()
print(plugin.connect())  # MySQL 连接
```

### 场景二：责任链模式

```python
class Handler:
    """处理器基类"""
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        return None

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("token"):
            return "认证失败"
        return super().handle(request)

class RoleHandler(Handler):
    def handle(self, request):
        if request.get("role") != "admin":
            return "权限不足"
        return super().handle(request)

class LogHandler(Handler):
    def handle(self, request):
        print(f"记录日志: {request}")
        return super().handle(request)

# 构建责任链
auth = AuthHandler()
role = RoleHandler()
log = LogHandler()
auth.set_next(role).set_next(log)

# 使用
result = auth.handle({"token": "abc", "role": "admin"})
```

### 场景三：模板方法模式

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """数据处理器模板"""
    def process(self, data):
        """模板方法：定义处理流程"""
        data = self.read(data)
        data = self.validate(data)
        data = self.transform(data)
        self.output(data)

    @abstractmethod
    def read(self, data):
        pass

    def validate(self, data):
        """默认验证逻辑，子类可覆盖"""
        if not data:
            raise ValueError("数据为空")
        return data

    @abstractmethod
    def transform(self, data):
        pass

    def output(self, data):
        """默认输出逻辑"""
        print(f"处理结果: {data}")

class CSVProcessor(DataProcessor):
    def read(self, data):
        return data.split(",")

    def transform(self, data):
        return [item.strip().upper() for item in data]

class JSONProcessor(DataProcessor):
    def read(self, data):
        import json
        return json.loads(data)

    def transform(self, data):
        return {k: v.upper() if isinstance(v, str) else v for k, v in data.items()}
```

## 注意事项

- 不要过度使用设计模式。Python 的简洁性意味着很多问题不需要设计模式就能解决
- 优先使用 Python 内置特性（装饰器、上下文管理器、生成器等）而非传统设计模式
- 单例模式在 Python 中最简单的实现是模块级别变量，不需要复杂的元类或 **new**
- 策略模式在 Python 中通常用函数即可实现，不必定义策略类
- 注意设计模式可能增加代码复杂度，在团队中应确保所有成员理解使用的模式
- Python 的鸭子类型减少了对接口和抽象类的需求

## 进阶用法

### 使用 dataclass 简化模式实现

```python
from dataclasses import dataclass

# 值对象模式
@dataclass(frozen=True)
class Money:
    """不可变的值对象"""
    amount: float
    currency: str

    def add(self, other):
        if self.currency != other.currency:
            raise ValueError("货币类型不同")
        return Money(self.amount + other.amount, self.currency)

# 使用
price = Money(99.9, "CNY")
shipping = Money(10.0, "CNY")
total = price.add(shipping)
```

### 使用 Protocol 实现接口

```python
from typing import Protocol

class Sortable(Protocol):
    """定义排序协议（类似接口）"""
    def sort(self, data: list) -> list: ...

class TimSorter:
    """自动满足 Sortable 协议"""
    def sort(self, data: list) -> list:
        return sorted(data)

def process_with_sorter(sorter: Sortable, data: list) -> list:
    """接受任何满足 Sortable 协议的对象"""
    return sorter.sort(data)
```

### 组合模式

```python
class Component:
    """组件基类"""
    def render(self, indent=0):
        raise NotImplementedError

class Leaf(Component):
    """叶子节点"""
    def __init__(self, name):
        self.name = name

    def render(self, indent=0):
        print(" " * indent + f"- {self.name}")

class Composite(Component):
    """组合节点"""
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self, indent=0):
        print(" " * indent + f"+ {self.name}")
        for child in self.children:
            child.render(indent + 2)

# 使用：构建树形结构
root = Composite("项目")
src = Composite("src")
src.add(Leaf("main.py"))
src.add(Leaf("utils.py"))
tests = Composite("tests")
tests.add(Leaf("test_main.py"))
root.add(src)
root.add(tests)
root.render()
```
## 命令模式

**基本写法：命令模式**
`class <命令>:\n    def execute(self):`
```python
# 命令模式
class Command:
    def execute(self):
        raise NotImplementedError

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()

class Light:
    def on(self): print("灯亮")
    def off(self): print("灯灭")

class Remote:
    def __init__(self):
        self._cmd = None
    def set_command(self, cmd):
        self._cmd = cmd
    def press(self):
        self._cmd.execute()
```

---

## 模板方法模式

**基本写法：模板方法**
`class <抽象类>:\n    def template_method(self):`
```python
# 模板方法模式
import abc

class DataProcessor(abc.ABC):
    def process(self):
        data = self.read()
        result = self.transform(data)
        self.write(result)

    @abc.abstractmethod
    def read(self): pass
    @abc.abstractmethod
    def transform(self, data): pass
    @abc.abstractmethod
    def write(self, data): pass

class CSVProcessor(DataProcessor):
    def read(self): return []
    def transform(self, data): return data
    def write(self, data): print(data)
```

---

## 责任链模式

**基本写法：责任链**
`class <处理器>:\n    def set_next(self, h):`
```python
# 责任链模式
class Handler:
    def __init__(self):
        self._next = None
    def set_next(self, handler):
        self._next = handler
        return handler
    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        return None

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("token"):
            return "未认证"
        return super().handle(request)

class LogHandler(Handler):
    def handle(self, request):
        print(f"记录请求")
        return super().handle(request)
```

---

## 上下文管理器模式

**基本写法：with 语句模式**
`class <类>:\n    def __enter__(self): ...\n    def __exit__(self, *a):`
```python
# 上下文管理器模式
class Transaction:
    def __enter__(self):
        print("开始事务")
        return self
    def __exit__(self, *exc):
        if exc[0] is None:
            print("提交")
        else:
            print("回滚")
        return False

with Transaction():
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
| Python与设计模式 | 040-PythonDesignPattern | 本文自身 |
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
