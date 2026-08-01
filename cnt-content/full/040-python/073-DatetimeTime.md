---
order: 730
title: Python datetime 与 time
module: 040-python
category: '040-python'
difficulty: beginner
description: Python datetime 与 time 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## datetime 基本创建

**基本写法：创建日期**
`datetime.date(<年>, <月>, <日>)`
```python
# 创建日期对象
from datetime import date
d = date(2024, 7, 31)
print(d)  # 2024-07-31
```

**基本写法：创建时间**
`datetime.time(<时>, <分>, [秒], [微秒])`
```python
# 创建时间对象
from datetime import time
t = time(14, 30, 0)
print(t)  # 14:30:00
```

**基本写法：创建日期时间**
`datetime.datetime(<年>, <月>, <日>, <时>, <分>, <秒>)`
```python
# 创建日期时间对象
from datetime import datetime
dt = datetime(2024, 7, 31, 14, 30, 0)
```

**基本写法：获取当前日期时间**
`datetime.now()`
```python
# 获取本地当前日期时间
now = datetime.now()
```

**基本写法：获取当前日期**
`date.today()`
```python
# 获取当前日期
today = date.today()
```

**基本写法：获取 UTC 当前时间**
`datetime.now(tz=timezone.utc)`
```python
# 获取 UTC 时区当前时间
from datetime import timezone
utc_now = datetime.now(tz=timezone.utc)
```

---

## datetime 从字符串解析

**基本写法：解析日期时间字符串**
`datetime.strptime(<字符串>, <格式>)`
```python
# 按格式解析字符串
from datetime import datetime
dt = datetime.strptime("2024-07-31 14:30", "%Y-%m-%d %H:%M")
```

**基本写法：格式化输出**
`<日期>.strftime(<格式>)`
```python
# 格式化为字符串
now = datetime.now()
s = now.strftime("%Y年%m月%d日 %H:%M:%S")
```

**常用格式化代码**
`%Y %m %d %H %M %S`
```python
# 常用格式化占位符
# %Y 年(4位)  %m 月(01-12)  %d 日(01-31)
# %H 时(00-23)  %M 分(00-59)  %S 秒(00-59)
# %A 星期名  %B 月名  %j 年内天数
```

**基本写法：ISO 格式解析**
`datetime.fromisoformat(<字符串>)`
```python
# 解析 ISO 8601 格式字符串
from datetime import datetime
dt = datetime.fromisoformat("2024-07-31T14:30:00")
```

**基本写法：输出 ISO 格式**
`<日期>.isoformat()`
```python
# 输出 ISO 8601 格式字符串
now = datetime.now()
print(now.isoformat())  # 2024-07-31T14:30:00
```

---

## timedelta 时间差

**基本写法：创建时间差**
`datetime.timedelta([days], [seconds], [microseconds])`
```python
# 创建时间间隔
from datetime import timedelta, date
delta = timedelta(days=7)
```

**基本写法：日期加减**
`<日期> + <时间差>`
```python
# 日期加减时间差
from datetime import date, timedelta
today = date.today()
next_week = today + timedelta(days=7)
```

**基本写法：两个日期相减**
`<日期1> - <日期2>`
```python
# 计算日期差
from datetime import date
d1 = date(2024, 12, 31)
d2 = date(2024, 1, 1)
diff = d1 - d2
print(diff.days)  # 365
```

**基本写法：时间差属性**
`<时间差>.days / .seconds / .total_seconds()`
```python
# 访问时间差的各部分
delta = timedelta(days=1, hours=2)
print(delta.days)             # 1
print(delta.seconds)          # 7200
print(delta.total_seconds())  # 93600.0
```

---

## 时区处理

**基本写法：设置时区**
`datetime.now(tz=<时区>)`
```python
# 获取带时区的当前时间
from datetime import datetime, timezone
utc_now = datetime.now(tz=timezone.utc)
```

**基本写法：时区转换**
`<时间>.astimezone(<目标时区>)`
```python
# UTC 转本地时区
from datetime import datetime, timezone
utc_dt = datetime.now(tz=timezone.utc)
local_dt = utc_dt.astimezone()
```

**基本写法：Python 3.9+ zoneinfo 时区**
`ZoneInfo("<时区名>")`
```python
# Python 3.9+ 使用 IANA 时区数据库
from zoneinfo import ZoneInfo
from datetime import datetime
tz_shanghai = ZoneInfo("Asia/Shanghai")
dt = datetime(2024, 7, 31, 14, 0, tzinfo=tz_shanghai)
```

**基本写法：时区转换**
`<时间>.astimezone(ZoneInfo("<时区>"))`
```python
# 上海时间转纽约时间
from zoneinfo import ZoneInfo
shanghai_time = datetime.now(tz=ZoneInfo("Asia/Shanghai"))
ny_time = shanghai_time.astimezone(ZoneInfo("America/New_York"))
```

**基本写法：Python 3.12+ fromisoformat 解析时区**
`datetime.fromisoformat(<带时区字符串>)`
```python
# Python 3.11+ 支持解析带时区的 ISO 字符串
dt = datetime.fromisoformat("2024-07-31T14:30:00+08:00")
```

---

## time 模块

**基本写法：获取时间戳**
`time.time()`
```python
# 返回当前时间的 Unix 时间戳（秒）
import time
ts = time.time()
```

**基本写法：时间戳转结构化时间**
`time.localtime([<时间戳>])`
```python
# 转为本地时间 struct_time
t = time.localtime()
print(t.tm_year, t.tm_mon, t.tm_mday)
```

**基本写法：格式化时间**
`time.strftime(<格式>, <结构化时间>)`
```python
# 按格式输出字符串
import time
s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```

**基本写法：解析时间字符串**
`time.strptime(<字符串>, <格式>)`
```python
# 解析字符串为 struct_time
t = time.strptime("2024-07-31", "%Y-%m-%d")
```

**基本写法：程序休眠**
`time.sleep(<秒>)`
```python
# 阻塞当前线程指定秒数
time.sleep(1.5)
```

**基本写法：计时**
`time.perf_counter()`
```python
# 高精度计时器
start = time.perf_counter()
do_work()
elapsed = time.perf_counter() - start
```

**基本写法：单调时钟**
`time.monotonic()`
```python
# 不受系统时间调整影响的单调时钟
start = time.monotonic()
time.sleep(1)
print(time.monotonic() - start)
```

**基本写法：Python 3.11+ monotonic_ns**
`time.monotonic_ns()`
```python
# 纳秒精度单调时钟
ns = time.monotonic_ns()
```

---

## time 性能计时

**基本写法：测量代码执行时间**
`time.perf_counter()`
```python
# 使用 perf_counter 测量耗时
import time
start = time.perf_counter()
result = sum(range(10**6))
elapsed = time.perf_counter() - start
print(f"耗时: {elapsed:.4f} 秒")
```

**基本写法：纳秒精度时间戳**
`time.time_ns()`
```python
# 返回纳秒精度时间戳
ns = time.time_ns()
```

**基本写法：process_time 进程时间**
`time.process_time()`
```python
# 返回进程实际 CPU 时间（不含休眠）
start = time.process_time()
do_work()
cpu_time = time.process_time() - start
```

---

## calendar 日历

**基本写法：获取月历**
`calendar.month(<年>, <月>)`
```python
# 输出文本格式月历
import calendar
print(calendar.month(2024, 7))
```

**基本写法：判断闰年**
`calendar.isleap(<年>)`
```python
# 判断是否为闰年
import calendar
print(calendar.isleap(2024))  # True
```

**基本写法：获取某月天数**
`calendar.monthrange(<年>, <月>)`
```python
# 返回 (该月首日星期几, 该月天数)
import calendar
print(calendar.monthrange(2024, 2))  # (3, 29)
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
| Python datetime 与 time | 073-DatetimeTime | 本文自身 |
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
