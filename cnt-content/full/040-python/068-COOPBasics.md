---
order: 680
title: Python 面向对象基础
module: python

category: '040-python'
difficulty: beginner
description: Python 面向对象基础 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 类定义

**基本写法：定义简单类**
`class <类名>: <类体>`

```python
# 定义简单类
class Dog:
    pass
```

---

**换行写法：定义带属性的类**
`class <类名>:`
`    def __init__(self, <参数>):`
`        self.<属性> = <值>`

```python
# 定义带初始化方法的类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

**基本写法：定义类属性**
`class <类名>: <类属性> = <值>`

```python
# 定义类属性
class Dog:
    species = "Canis lupus"
```

---

**基本写法：定义实例属性**
`self.<属性> = <值>`

```python
# 在 __init__ 中定义实例属性
class Dog:
    def __init__(self, name):
        self.name = name
```

---

## 实例化与访问

**基本写法：创建类实例**
`<对象> = <类名>(<参数>)`

```python
# 创建 Dog 类的实例
dog = Dog("Buddy", 3)
```

---

**基本写法：访问实例属性**
`<对象>.<属性>`

```python
# 访问实例属性
print(dog.name)
```

---

**基本写法：访问类属性**
`<类名>.<类属性>`

```python
# 访问类属性
print(Dog.species)
```

---

**基本写法：修改实例属性**
`<对象>.<属性> = <新值>`

```python
# 修改实例属性
dog.age = 4
```

---

## 实例方法

**基本写法：定义实例方法**
`def <方法名>(self, <参数>): <语句>`

```python
# 定义实例方法
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
```

---

**基本写法：调用实例方法**
`<对象>.<方法名>(<参数>)`

```python
# 调用实例方法
print(dog.bark())
```

---

**基本写法：定义带参数的实例方法**
`def <方法名>(self, <参数1>, <参数2>): <语句>`

```python
# 定义带参数的实例方法
class Dog:
    def fetch(self, item):
        return f"{self.name} fetches the {item}"
```

---

## 类方法

**基本写法：定义类方法**
`@classmethod`
`def <方法名>(cls, <参数>): <语句>`

```python
# 定义类方法
class Dog:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

---

**基本写法：使用类方法作为工厂**
`@classmethod`
`def <方法名>(cls, <参数>): return cls(<参数>)`

```python
# 使用类方法作为工厂函数
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split(",")
        return cls(name, int(age))
```

---

## 静态方法

**基本写法：定义静态方法**
`@staticmethod`
`def <方法名>(<参数>): <语句>`

```python
# 定义静态方法
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
```

---

**基本写法：调用静态方法**
`<类名>.<方法名>(<参数>)`

```python
# 调用静态方法
print(MathHelper.add(3, 5))
```

---

## 继承

**基本写法：单继承**
`class <子类>(<父类>): <类体>`

```python
# 单继承
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass
```

---

**基本写法：多继承**
`class <子类>(<父类1>, <父类2>): <类体>`

```python
# 多继承
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass
```

---

**基本写法：调用父类方法**
`super().<方法名>(<参数>)`

```python
# 调用父类的 __init__ 方法
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

**基本写法：方法重写**
`def <父类方法名>(self, <参数>): <新语句>`

```python
# 重写父类方法
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

---

**基本写法：使用 super() 调用重写方法**
`super().<方法名>(<参数>)`

```python
# 在重写方法中调用父类方法
class Dog(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} - Woof!"
```

---

## 多重继承与 MRO

**基本写法：查看方法解析顺序**
`<类名>.mro()`

```python
# 查看方法解析顺序
print(Dog.mro())
```

---

**基本写法：查看方法解析顺序（__mro__）**
`<类名>.__mro__`

```python
# 查看 MRO 元组
print(Dog.__mro__)
```

---

## 属性装饰器

**基本写法：使用 @property 定义属性**
`@property`
`def <属性名>(self): <语句>`

```python
# 使用 @property 定义只读属性
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```

---

**基本写法：使用 @property 定义可写属性**
`@<属性名>.setter`
`def <属性名>(self, <值>): <语句>`

```python
# 使用 @property.setter 定义可写属性
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

---

**基本写法：使用 @property 定义删除器**
`@<属性名>.deleter`
`def <属性名>(self): <语句>`

```python
# 使用 @property.deleter 定义删除器
class Circle:
    @property
    def radius(self):
        return self._radius

    @radius.deleter
    def radius(self):
        del self._radius
```

---

## 特殊方法（魔术方法）

**基本写法：定义 __str__ 方法**
`def __str__(self): return <字符串>`

```python
# 定义 __str__ 方法（用户友好的字符串表示）
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog(name={self.name})"
```

---

**基本写法：定义 __repr__ 方法**
`def __repr__(self): return <字符串>`

```python
# 定义 __repr__ 方法（开发者友好的字符串表示）
class Dog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Dog(name={self.name!r})"
```

---

**基本写法：定义 __len__ 方法**
`def __len__(self): return <整数>`

```python
# 定义 __len__ 方法（支持 len() 函数）
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)
```

---

**基本写法：定义 __eq__ 方法**
`def __eq__(self, other): return <布尔值>`

```python
# 定义 __eq__ 方法（支持 == 运算符）
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

**基本写法：定义 __lt__ 方法**
`def __lt__(self, other): return <布尔值>`

```python
# 定义 __lt__ 方法（支持 < 运算符）
class Student:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score
```

---

**基本写法：定义 __add__ 方法**
`def __add__(self, other): return <新对象>`

```python
# 定义 __add__ 方法（支持 + 运算符）
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

---

**基本写法：定义 __getitem__ 方法**
`def __getitem__(self, <键>): return <值>`

```python
# 定义 __getitem__ 方法（支持 [] 访问）
class Matrix:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]
```

---

**基本写法：定义 __setitem__ 方法**
`def __setitem__(self, <键>, <值>): <语句>`

```python
# 定义 __setitem__ 方法（支持 [] 赋值）
class Matrix:
    def __setitem__(self, key, value):
        self.data[key] = value
```

---

**基本写法：定义 __iter__ 方法**
`def __iter__(self): return <迭代器>`

```python
# 定义 __iter__ 方法（支持迭代）
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
```

---

**基本写法：定义 __contains__ 方法**
`def __contains__(self, <元素>): return <布尔值>`

```python
# 定义 __contains__ 方法（支持 in 运算符）
class Matrix:
    def __contains__(self, item):
        return any(item in row for row in self.data)
```

---

**基本写法：定义 __call__ 方法**
`def __call__(self, <参数>): <语句>`

```python
# 定义 __call__ 方法（使实例可调用）
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
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
| 装饰器进阶 | 062-DecoratorAdvanced | 本文的并列主题 |
| 异常处理 | 063-ExceptionHandling | 本文的并列主题 |
| 文件 I/O 与上下文管理器 | 064-FileIOContextManager | 本文的并列主题 |
| Python 项目示例：网页爬虫与数据分析 | 065-PythonProjectExampleWebCrawlerDataAnalysis | 本文的综合应用 |
| Python 理论知识点 | 066-PythonTheoryKnowledge | 本文的并列主题 |
| 基础数据类型 | 067-BasicDataType | 本文的前置基础 |
| Python 面向对象基础 | 068-COOPBasics | 本文自身 |
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
