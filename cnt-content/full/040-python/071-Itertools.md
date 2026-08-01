---
order: 710
title: Python itertools 迭代工具
module: 040-python
category: '040-python'
difficulty: beginner
description: Python itertools 迭代工具 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 无限迭代器

**基本写法：count 无限计数**
`itertools.count([start], [step])`
```python
# 从 start 开始每次加 step 无限计数
from itertools import count
for i in count(10, 2):
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20
```

**基本写法：cycle 循环重复**
`itertools.cycle(<可迭代对象>)`
```python
# 无限循环遍历可迭代对象
from itertools import cycle
colors = cycle(["red", "green", "blue"])
for i, c in enumerate(colors):
    if i >= 5:
        break
    print(c)
```

**基本写法：repeat 重复元素**
`itertools.repeat(<元素>, [times])`
```python
# 重复元素指定次数
from itertools import repeat
for x in repeat("hi", 3):
    print(x)  # hi hi hi
```

---

## 串联与切分

**基本写法：chain 串联迭代器**
`itertools.chain(<可迭代1>, <可迭代2>)`
```python
# 将多个可迭代对象串联
from itertools import chain
for x in chain([1, 2], [3, 4]):
    print(x)  # 1 2 3 4
```

**基本写法：chain.from_iterable 串联嵌套**
`itertools.chain.from_iterable(<嵌套可迭代>)`
```python
# 串联可迭代对象的可迭代对象
nested = [[1, 2], [3, 4], [5]]
for x in chain.from_iterable(nested):
    print(x)  # 1 2 3 4 5
```

**基本写法：islice 切片**
`itertools.islice(<可迭代>, [start], stop, [step])`
```python
# 对迭代器进行切片
from itertools import islice
for x in islice(range(100), 5, 10, 2):
    print(x)  # 5 7 9
```

**基本写法：tee 分裂迭代器**
`itertools.tee(<可迭代>, n)`
```python
# 复制迭代器为 n 个独立迭代器
from itertools import tee
it1, it2 = tee(range(3), 2)
print(list(it1))  # [0, 1, 2]
print(list(it2))  # [0, 1, 2]
```

---

## 过滤

**基本写法：filterfalse 反向过滤**
`itertools.filterfalse(<函数>, <可迭代>)`
```python
# 保留使函数返回 False 的元素
from itertools import filterfalse
for x in filterfalse(lambda n: n % 2, range(6)):
    print(x)  # 0 2 4
```

**基本写法：takewhile 取到条件不满足**
`itertools.takewhile(<函数>, <可迭代>)`
```python
# 依次取元素直到函数返回 False
from itertools import takewhile
for x in takewhile(lambda n: n < 5, [1, 3, 5, 2]):
    print(x)  # 1 3
```

**基本写法：dropwhile 丢弃到条件不满足**
`itertools.dropwhile(<函数>, <可迭代>)`
```python
# 跳过元素直到函数返回 False，然后取剩余
from itertools import dropwhile
for x in dropwhile(lambda n: n < 5, [1, 3, 5, 2, 7]):
    print(x)  # 5 2 7
```

**基本写法：compress 按选择器过滤**
`itertools.compress(<数据>, <选择器>)`
```python
# 按布尔选择器提取元素
from itertools import compress
for x in compress("ABCDEF", [1, 0, 1, 0, 1, 1]):
    print(x)  # A C E F
```

---

## 映射

**基本写法：starmap 展开映射**
`itertools.starmap(<函数>, <可迭代>)`
```python
# 将每项作为参数展开传给函数
from itertools import starmap
for result in starmap(pow, [(2, 3), (3, 2)]):
    print(result)  # 8 9
```

**基本写法：accumulate 累积**
`itertools.accumulate(<可迭代>, [func])`
```python
# 累积求和或自定义累积函数
from itertools import accumulate
for x in accumulate([1, 2, 3, 4]):
    print(x)  # 1 3 6 10
```

**基本写法：累积求积**
`itertools.accumulate(<可迭代>, operator.mul)`
```python
# 累积乘法
import operator
for x in accumulate([1, 2, 3, 4], operator.mul):
    print(x)  # 1 2 6 24
```

---

## 分组

**基本写法：groupby 分组**
`itertools.groupby(<可迭代>, [key=<函数>])`
```python
# 按键函数分组（需先排序）
from itertools import groupby
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in groupby(data, lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3)]
```

**基本写法：按值分组**
`itertools.groupby(sorted(<可迭代>), key=<函数>)`
```python
# 先排序再分组确保连续
words = ["apple", "bat", "ant", "bear"]
for first, group in groupby(sorted(words), lambda w: w[0]):
    print(first, list(group))
# a ['apple', 'ant']
# b ['bat', 'bear']
```

---

## 排列组合

**基本写法：product 笛卡尔积**
`itertools.product(<可迭代1>, <可迭代2>, [repeat=<次数>])`
```python
# 多个可迭代对象的笛卡尔积
from itertools import product
for combo in product("AB", "12"):
    print(combo)
# ('A','1') ('A','2') ('B','1') ('B','2')
```

**基本写法：product 重复**
`itertools.product(<可迭代>, repeat=<次数>)`
```python
# 与自身做笛卡尔积
for combo in product("AB", repeat=2):
    print(combo)
# AA AB BA BB
```

**基本写法：permutations 排列**
`itertools.permutations(<可迭代>, [r])`
```python
# 全排列
from itertools import permutations
for p in permutations("ABC", 2):
    print(p)
# AB AC BA BC CA CB
```

**基本写法：combinations 组合**
`itertools.combinations(<可迭代>, r)`
```python
# 无放回组合
from itertools import combinations
for c in combinations("ABC", 2):
    print(c)
# AB AC BC
```

**基本写法：combinations_with_replacement 可重复组合**
`itertools.combinations_with_replacement(<可迭代>, r)`
```python
# 有放回组合
from itertools import combinations_with_replacement
for c in combinations_with_replacement("AB", 2):
    print(c)
# AA AB BB
```

---

## 配对与分块

**基本写法：Python 3.10+ pairwise 配对**
`itertools.pairwise(<可迭代>)`
```python
# 相邻元素两两配对
from itertools import pairwise
for a, b in pairwise([1, 2, 3, 4]):
    print(a, b)  # 1 2 / 2 3 / 3 4
```

**基本写法：Python 3.12+ batched 分批**
`itertools.batched(<可迭代>, n)`
```python
# Python 3.12+ 按固定大小分批
from itertools import batched
for batch in batched(range(7), 3):
    print(batch)
# (0, 1, 2) (3, 4, 5) (6,)
```

---

## zip_longest

**基本写法：zip_longest 不等长配对**
`itertools.zip_longest(<可迭代1>, <可迭代2>, [fillvalue=<填充值>])`
```python
# 不等长可迭代对象配对，短端填充
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], ["a", "b"], fillvalue="?"):
    print(a, b)
# 1 a / 2 b / 3 ?
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
| Python itertools 迭代工具 | 071-Itertools | 本文自身 |
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
