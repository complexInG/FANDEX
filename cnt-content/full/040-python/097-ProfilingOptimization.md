---
order: 970
title: Python 性能分析与优化
module: 040-python
category: '040-python'
difficulty: beginner
description: Python 性能分析与优化 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## timeit 计时

**基本写法：timeit 计时**
`timeit.timeit(<代码>, number=<次数>)`
```python
# 测量代码执行时间
import timeit

t = timeit.timeit("sum(range(100))", number=10000)
print(t)
```

**基本写法：repeat 重复测量**
`timeit.repeat(<代码>, repeat=<次数>, number=<次数>)`
```python
# 多次重复测量
times = timeit.repeat("sum(range(100))", repeat=5, number=10000)
print(min(times))
```

**基本写法：命令行**
`python -m timeit -s <setup> <代码>`
```python
# 命令行计时
# python -m timeit -s "import json" "json.dumps({'a':1})"
```

**基本写法：Timer 对象**
`timeit.Timer(<代码>, setup=<准备>)`
```python
# Timer 对象
t = timeit.Timer("x.append(1)", setup="x = []")
print(t.timeit(number=100000))
```

---

## time 性能计数器

**基本写法：perf_counter 高精度**
`time.perf_counter()`
```python
# 高精度计时器
import time

start = time.perf_counter()
# 执行代码
time.sleep(0.1)
end = time.perf_counter()
print(f"耗时 {end - start:.4f}s")
```

**基本写法：perf_counter_ns 纳秒**
`time.perf_counter_ns()`
```python
# 纳秒级精度
start = time.perf_counter_ns()
# 执行代码
end = time.perf_counter_ns()
print(f"耗时 {end - start}ns")
```

**基本写法：process_time 进程时间**
`time.process_time()`
```python
# 进程 CPU 时间（不含睡眠）
start = time.process_time()
# 执行代码
end = time.process_time()
print(f"CPU 时间 {end - start}s")
```

---

## cProfile 性能分析

**基本写法：cProfile 运行**
`cProfile.run(<代码字符串>)`
```python
# 分析代码性能
import cProfile

cProfile.run("sum(range(1000000))")
```

**基本写法：Profile 对象**
`cProfile.Profile()`
```python
# Profile 对象精细控制
prof = cProfile.Profile()
prof.enable()
# 执行代码
sum(range(100000))
prof.disable()
prof.print_stats(sort="cumtime")
```

**基本写法：排序输出**
`prof.print_stats(sort=<排序>)`
```python
# 按累计时间排序
prof.print_stats(sort="cumulative")
prof.print_stats(sort="tottime")  # 按总时间
```

**基本写法：保存到文件**
`prof.dump_stats(<文件>)`
```python
# 保存分析数据
prof.dump_stats("profile.prof")
```

**基本写法：pstats 分析**
`pstats.Stats(<文件>)`
```python
# 加载并分析 profile 文件
import pstats

stats = pstats.Stats("profile.prof")
stats.sort_stats("cumulative").print_stats(10)
```

---

## memory_profiler 内存分析

**基本写法：profile 装饰器**
`@profile`
```python
# 需要安装 memory_profiler
# pip install memory_profiler
@profile
def my_func():
    a = [1] * 1000000
    return sum(a)

my_func()
# 运行：python -m memory_profiler script.py
```

**基本写法：memit 内存峰值**
`%memit <表达式>`
```python
# IPython 中测量内存峰值
# %memit sum(range(1000000))
```

---

## sys.getsizeof 内存占用

**基本写法：获取对象大小**
`sys.getsizeof(<对象>)`
```python
# 获取对象字节大小
import sys

print(sys.getsizeof([1, 2, 3]))
print(sys.getsizeof("hello"))
print(sys.getsizeof({}))
```

**基本写法：tracemalloc 跟踪分配**
`tracemalloc.start()`
```python
# 跟踪内存分配
import tracemalloc

tracemalloc.start()
# 执行代码
data = [i for i in range(100000)]
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:5]:
    print(stat)
```

**基本写法：比较快照**
`snapshot2.compare_to(snapshot1, "lineno")`
```python
# 比较两个内存快照
snap1 = tracemalloc.take_snapshot()
# 执行代码
snap2 = tracemalloc.take_snapshot()
for stat in snap2.compare_to(snap1, "lineno")[:5]:
    print(stat)
```

---

## dis 字节码分析

**基本写法：反汇编**
`dis.dis(<函数>)`
```python
# 查看函数字节码
import dis

def loop():
    total = 0
    for i in range(100):
        total += i
    return total

dis.dis(loop)
```

---

## 优化技巧

**基本写法：列表推导优于循环**
`[<表达式> for <变量> in <可迭代>]`
```python
# 列表推导比 append 循环快
squares = [x * x for x in range(1000)]
```

**基本写法：生成器节省内存**
`(<表达式> for <变量> in <可迭代>)`
```python
# 大数据用生成器
squares_gen = (x * x for x in range(1000000))
```

**基本写法：set 成员查找**
`<值> in <集合>`
```python
# set 查找 O(1)，list 查找 O(n)
valid = {"a", "b", "c"}  # 用 set 而非 list
if x in valid:
    pass
```

**基本写法：局部变量优化**
`def <函数>():\n    <局部变量>`
```python
# 局部变量比全局变量快
def compute():
    # 局部变量访问快
    total = sum
    return total(range(100))
```

**基本写法：__slots__ 节省内存**
`class <类>:\n    __slots__ = (<字段>,)`
```python
# __slots__ 减少内存与加速属性访问
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**基本写法：lru_cache 缓存**
`@functools.lru_cache(maxsize=<大小>)`
```python
# 缓存函数结果
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## sys.monitoring 监控（3.12+）

**基本写法：注册监控工具**
`sys.monitoring.use_tool_id(<ID>, <名称>)`
```python
# Python 3.12 低开销监控（PEP 669）
import sys.monitoring

sys.monitoring.use_tool_id(0, "my_profiler")
sys.monitoring.register_callback(
    sys.monitoring.events.PY_START,
    0,
    lambda code, offset: print("开始", code.co_name)
)
```

**基本写法：获取事件**
`sys.monitoring.events`
```python
# 监控事件类型
print(sys.monitoring.events.PY_START)
print(sys.monitoring.events.PY_RESUME)
print(sys.monitoring.events.CALL)
```

---

## 并行加速

**基本写法：多进程 CPU 密集**
`concurrent.futures.ProcessPoolExecutor()`
```python
# CPU 密集型用多进程
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(heavy, [1000000, 2000000, 3000000]))
```

**基本写法：多线程 IO 密集**
`concurrent.futures.ThreadPoolExecutor()`
```python
# IO 密集型用多线程或 asyncio
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.read()

with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(fetch, urls))
```

---

## 字符串拼接优化

**基本写法：join 优于 +**
`"<分隔>".join(<字符串列表>)`
```python
# join 比 + 拼接高效
parts = ["a", "b", "c"]
result = "".join(parts)  # 优于 result = parts[0] + parts[1] + ...
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
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文自身 |
