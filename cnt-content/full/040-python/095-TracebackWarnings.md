---
order: 950
title: Python traceback 与 warnings
module: python

category: '040-python'
difficulty: beginner
description: Python traceback 与 warnings 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## traceback 打印异常

**基本写法：打印当前异常**
`traceback.print_exc()`
```python
# 打印当前异常栈到 stderr
import traceback

try:
    1 / 0
except Exception:
    traceback.print_exc()
```

**基本写法：格式化异常字符串**
`traceback.format_exc()`
```python
# 获取异常栈字符串
try:
    1 / 0
except Exception:
    msg = traceback.format_exc()
    print(msg)
```

**基本写法：打印指定异常**
`traceback.print_exception(<异常>)`
```python
# 打印指定异常对象
try:
    raise ValueError("test")
except ValueError as e:
    traceback.print_exception(e)
```

**基本写法：格式化指定异常**
`traceback.format_exception(<异常>)`
```python
# 返回异常信息行列表
try:
    raise ValueError("test")
except ValueError as e:
    lines = traceback.format_exception(e)
    print("".join(lines))
```

---

## traceback 提取栈帧

**基本写法：提取当前栈**
`traceback.extract_stack()`
```python
# 获取当前调用栈帧列表
frames = traceback.extract_stack()
for f in frames:
    print(f.filename, f.lineno, f.name)
```

**基本写法：提取指定栈**
`traceback.extract_tb(<tb>)`
```python
# 从 traceback 对象提取帧
try:
    1 / 0
except ZeroDivisionError as e:
    frames = traceback.extract_tb(e.__traceback__)
    for f in frames:
        print(f.filename, f.lineno, f.name, f.line)
```

**基本写法：StackSummary 对象**
`traceback.StackSummary.extract(<帧>)`
```python
# 3.5+ StackSummary 对象
summary = traceback.StackSummary.extract(traceback.walk_stack(None))
print(summary.format())
```

**基本写法：format_list 格式化帧**
`traceback.format_list(<帧列表>)`
```python
# 格式化帧列表
frames = traceback.extract_stack()
print("".join(traceback.format_list(frames)))
```

---

## traceback 装饰器

**基本写法：异常装饰器**
`def <装饰器>(func):\n    @functools.wraps(func)\n    def wrapper(*a, **k):`
```python
# 捕获异常并记录完整 traceback
import functools
import traceback
import logging

def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logging.error(traceback.format_exc())
            raise
    return wrapper
```

---

## warnings 警告控制

**基本写法：发出警告**
`warnings.warn(<消息>, <警告类>)`
```python
# 发出警告
import warnings

def deprecated_func():
    warnings.warn("该函数已弃用", DeprecationWarning)
    return "old"
```

**基本写法：警告类别**
`UserWarning` | `DeprecationWarning` | `RuntimeWarning`
```python
# 常用警告类别
warnings.warn("用户警告", UserWarning)
warnings.warn("弃用警告", DeprecationWarning)
warnings.warn("运行时警告", RuntimeWarning)
warnings.warn("资源警告", ResourceWarning)
```

**基本写法：过滤警告**
`warnings.filterwarnings(<动作>, <消息正则>, <类别>)`
```python
# 过滤警告
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("error", category=UserWarning)
```

**基本写法：simplefilter 简化过滤**
`warnings.simplefilter(<动作>, <类别>)`
```python
# 简化过滤
warnings.simplefilter("ignore")
warnings.simplefilter("always", UserWarning)
```

**基本写法：动作选项**
`"error"` | `"ignore"` | `"always"` | `"default"` | `"module"` | `"once"`
```python
# 警告动作
warnings.simplefilter("error")   # 警告转异常
warnings.simplefilter("ignore")  # 忽略
warnings.simplefilter("always")  # 总是显示
```

---

## warnings 上下文管理

**基本写法：catch_warnings 临时过滤**
`with warnings.catch_warnings():`
```python
# 临时修改警告过滤
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    deprecated_func()
```

**基本写法：捕获警告记录**
`with warnings.catch_warnings(record=True) as w:`
```python
# 捕获警告到列表
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    deprecated_func()
    for warning in w:
        print(warning.category.__name__, warning.message)
```

**基本写法：指定模块过滤**
`warnings.filterwarnings(<动作>, module=<模块正则>)`
```python
# 仅对特定模块过滤
warnings.filterwarnings("ignore", module="legacy_lib.*")
```

---

## warnings 子类化

**基本写法：自定义警告类**
`class <警告类>(Warning):`
```python
# 自定义警告类别
class ConfigWarning(UserWarning):
    pass

warnings.warn("配置问题", ConfigWarning)
```

**基本写法：deprecated 装饰器（3.13+）**
`@warnings.deprecated(<消息>)`
```python
# Python 3.13 内置弃用装饰器
@warnings.deprecated("使用 new_func 替代")
def old_func():
    pass
```

---

## 命令行控制警告

**基本写法：命令行参数**
`python -W <动作>:<消息>:<类别>:<模块>:<行号>`
```python
# 命令行控制警告
# python -W ignore::DeprecationWarning main.py
# python -W error::UserWarning main.py
```

**基本写法：环境变量**
`PYTHONWARNINGS=<过滤>`
```python
# 通过环境变量设置
# set PYTHONWARNINGS=ignore::DeprecationWarning
```

---

## sys 异常信息

**基本写法：sys.exc_info**
`sys.exc_info()`
```python
# 获取当前异常信息三元组
import sys

try:
    1 / 0
except ZeroDivisionError:
    exc_type, exc, tb = sys.exc_info()
    print(exc_type, exc)
```

**基本写法：异常链**
`raise <异常> from <原异常>`
```python
# 异常链
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("处理失败") from e
```

**基本写法：suppress 上下文**
`raise <异常> from None`
```python
# 抑制异常上下文
raise RuntimeError("独立错误") from None
```

**基本写法：__cause__ 与 __context__**
`exc.__cause__` | `exc.__context__`
```python
# 访问异常链
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("wrap") from e
except RuntimeError as e:
    print(e.__cause__)
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

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Python 对象模型与魔术方法

Python 的对象模型以“特殊方法”（dunder methods）为协议载体。`__init__` 负责初始化，`__new__` 负责创建；`__repr__` 与 `__str__` 控制展示；`__eq__` 与 `__hash__` 控制相等性与哈希。
运算符重载同样基于协议：`__add__` 对应 +，`__lt__` 对应 <，`__getitem__` 对应下标访问。实现这些方法时，应保持与内置类型行为一致，例如 `__eq__` 返回布尔值、`__hash__` 与 `__eq__` 同步定义。
上下文管理器协议（`__enter__/__exit__`）让自定义资源支持 with 语句；迭代器协议（`__iter__/__next__`）让自定义容器支持 for。掌握协议思维，就能写出与标准库无缝协作的类。
属性协议（`__getattr__/__setattr__/__getattribute__`）与 `property` 装饰器提供属性访问控制；`__slots__` 声明固定属性，减少实例内存并提升属性访问速度。
工程建议：优先使用 `dataclasses` 声明数据类，仅在需要深度定制时才手写特殊方法；每个特殊方法都应有明确的文档与测试。

### 13.2 装饰器与闭包的原理

闭包是携带自由变量的函数：内层函数引用外层函数的变量，外层返回内层函数时，变量随函数一起保存。Python 用 `nonlocal` 声明需要修改的外层变量。
装饰器是“接收函数并返回函数”的高阶函数，`@decorator` 语法等价于 `func = decorator(func)`。装饰器常用于日志、计时、鉴权、缓存。
带参数的装饰器需要三层嵌套：最外层接收参数，中间层接收函数，内层包裹原函数。`functools.wraps` 复制原函数元信息，避免调试信息丢失。
常见陷阱：装饰器只在导入时执行一次，若缓存结果会导致状态过期；装饰器堆叠顺序从下往上应用，从下往上执行。
工程建议：装饰器保持薄层，复杂逻辑拆分为独立函数；使用 `functools.singledispatch` 实现单分派泛型，避免大量 isinstance 分支。

### 13.3 生成器与内存优化

生成器函数使用 `yield` 逐次产出值，保存执行状态，下次调用从断点继续。与列表相比，生成器不一次性占用内存，适合大文件、无限序列与流式处理。
生成器表达式 `(x * x for x in range(10))` 是惰性求值的列表推导变体；`yield from` 委托子生成器，简化递归生成。
协程与生成器同源：`send()` 向生成器传入值，`throw()` 注入异常，`close()` 终止。asyncio 的事件循环正是基于这一机制实现异步任务调度。
流水线模式：多个生成器串联（如读取行、过滤、转换、输出），每个环节独立可测，内存占用恒定。
工程建议：不确定数据量时默认用生成器；需要随机访问或多遍遍历时改用列表；用 `itertools` 组合生成器避免重复造轮子。

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
| Python traceback 与 warnings | 095-TracebackWarnings | 本文自身 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
