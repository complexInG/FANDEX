---
order: 810
title: Python 字符串格式化与方法
module: 040-python
category: '040-python'
difficulty: beginner
description: Python 字符串格式化与方法 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## f-string 格式化

**基本写法：基础 f-string**
`f"<前缀>{<表达式>}<后缀>"`
```python
# 变量直接嵌入字符串
name = "Tom"
age = 18
print(f"姓名: {name}, 年龄: {age}")
```

**基本写法：表达式与运算**
`f"{<表达式计算>}"`
```python
# 大括号内支持任意表达式
print(f"总价: {10 * 2.5:.2f}")
print(f"长度: {len(name)}")
```

**基本写法：浮点精度**
`f"{<值>:.<小数位>f}"`
```python
# 控制小数位数
pi = 3.14159
print(f"{pi:.2f}")  # 3.14
```

**基本写法：宽度与对齐**
`f"{<值>:<填充><对齐><宽度>}"`
```python
# < 左对齐 | > 右对齐 | ^ 居中
print(f"{name:>10}")   # 右对齐宽 10
print(f"{name:<10}")   # 左对齐
print(f"{name:^10}")   # 居中
print(f"{name:0>10}")  # 用 0 填充
```

**基本写法：千分位分隔**
`f"{<值>:,}"`
```python
# 数字千分位逗号
print(f"{1000000:,}")    # 1,000,000
print(f"{1000000:,.2f}") # 1,000,000.00
```

**基本写法：百分比与科学计数**
`f"{<值>:%} / f"{<值>:e}"`
```python
# 百分比与科学计数法
ratio = 0.85
print(f"{ratio:.1%}")   # 85.0%
print(f"{1234567:.2e}") # 1.23e+06
```

**基本写法：进制转换**
`f"{<值>:b/o/x/X}"`
```python
# 二进制 八进制 十六进制
n = 255
print(f"{n:b}")  # 11111111
print(f"{n:o}")  # 377
print(f"{n:x}")  # ff
print(f"{n:#x}") # 0xff（带前缀）
```

**基本写法：调试输出**
`f"{<变量>=}"`
```python
# Python 3.8+ 自动显示变量名与值
x = 42
print(f"{x=}")        # x=42
print(f"{x=:>10}")    # x=        42
```

**基本写法：转换标志**
`f"{<值>!r/!s/!a}"`
```python
# 强制使用 repr / str / ascii
s = "中文"
print(f"{s!r}")  # '中文'
print(f"{s!s}")  # 中文
```

**基本写法：日期格式化**
`f"{<日期>:%Y-%m-%d}"`
```python
# 直接用 strftime 格式说明符
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
```

---

## format 方法

**基本写法：位置参数**
`"<{}>".format(<值>)`
```python
# 按位置填充占位符
print("{}, {}".format("a", "b"))
print("{0} - {1}".format("a", "b"))
```

**基本写法：命名参数**
`"{<名称>}".format(<名称>=<值>)`
```python
# 按名称填充
print("{name} {age}".format(name="Tom", age=18))
```

**基本写法：format_map**
`"<{name}>".format_map(<字典>)`
```python
# 直接从字典读取键值
data = {"name": "Tom", "age": 18}
print("{name}-{age}".format_map(data))
```

---

## % 旧式格式化

**基本写法：% 格式化**
`"<格式串>" % (<值1>, <值2>)`
```python
# 旧式百分号格式化
print("name=%s, age=%d" % ("Tom", 18))
print("pi=%.2f" % 3.14159)
```

---

## Template 模板字符串

**基本写法：Template 替换**
`Template("<$名称>").substitute(<字典>)`
```python
# 安全的字符串模板替换
from string import Template
t = Template("$name 的成绩是 $score")
print(t.substitute(name="Tom", score=90))
print(t.safe_substitute({"name": "Tom"}))  # 缺失键保留原样
```

---

## 字符串拆分与拼接

**基本写法：split 拆分**
`<字符串>.split([<分隔符>[, <最大次数>]])`
```python
# 按分隔符拆分为列表
print("a,b,c".split(","))      # ['a', 'b', 'c']
print("a-b-c".split("-", 1))   # ['a', 'b-c']
```

**基本写法：rsplit 从右拆分**
`<字符串>.rsplit([<分隔符>[, <最大次数>]])`
```python
# 从右侧开始拆分
print("a.b.c".rsplit(".", 1))  # ['a.b', 'c']
```

**基本写法：splitlines 按行拆分**
`<字符串>.splitlines([keepends=<布尔>])`
```python
# 按换行符拆分为行列表
print("a\nb\nc".splitlines())
print("a\nb".splitlines(keepends=True))  # ['a\n', 'b']
```

**基本写法：join 拼接**
`<分隔符>.join(<可迭代>)`
```python
# 将可迭代对象拼接为字符串
print(",".join(["a", "b", "c"]))  # a,b,c
print("-".join(str(i) for i in range(5)))
```

**基本写法：partition 分段**
`<字符串>.partition(<分隔符>)`
```python
# 分成三段元组（前、分隔符、后）
print("a=b=c".partition("="))  # ('a', '=', 'b=c')
print("a=b".rpartition("="))   # ('a', '=', 'b')
```

---

## 字符串查找与替换

**基本写法：find 查找位置**
`<字符串>.find(<子串>[, <起>[, <止>]])`
```python
# 返回首次出现位置，找不到返回 -1
print("hello".find("l"))     # 2
print("hello".find("x"))     # -1
```

**基本写法：index 查找**
`<字符串>.index(<子串>)`
```python
# 与 find 类似，找不到抛 ValueError
print("hello".index("l"))
```

**基本写法：count 计数**
`<字符串>.count(<子串>)`
```python
# 统计子串出现次数
print("banana".count("a"))  # 3
```

**基本写法：replace 替换**
`<字符串>.replace(<旧>, <新>[, <次数>])`
```python
# 替换子串，可限制次数
print("a-b-c".replace("-", "+"))      # a+b+c
print("a-b-c".replace("-", "+", 1))   # a+b-c
```

**基本写法：前后缀判断**
`<字符串>.startswith(<前缀>) / .endswith(<后缀>)`
```python
# 判断开头或结尾
print("abc.py".endswith(".py"))   # True
print("abc".startswith("a"))      # True
```

---

## 字符串修剪与对齐

**基本写法：strip 去空白**
`<字符串>.strip([<字符集>])`
```python
# 去除两端空白或指定字符
print("  hi  ".strip())   # hi
print("##hi##".strip("#")) # hi
```

**基本写法：单侧去除**
`lstrip / rstrip`
```python
# 仅去除左侧或右侧
print("  hi  ".lstrip())  # "hi  "
print("  hi  ".rstrip())  # "  hi"
```

**基本写法：对齐填充**
`ljust / rjust / center`
```python
# 指定宽度对齐并填充
print("ab".ljust(5, "-"))   # ab---
print("ab".rjust(5, "-"))   # ---ab
print("ab".center(5, "-"))  # -ab--
```

**基本写法：补零**
`<字符串>.zfill(<宽度>)`
```python
# 左侧补零到指定宽度
print("42".zfill(5))  # 00042
```

---

## 大小写转换

**基本写法：大小写转换**
`upper / lower / title / swapcase`
```python
# 各类大小写转换
print("Hello".upper())      # HELLO
print("Hello".lower())      # hello
print("hello world".title()) # Hello World
print("aBc".swapcase())     # AbC
```

**基本写法：casefold 强制折叠**
`<字符串>.casefold()`
```python
# 更激进的小写转换，适合国际化比较
print("STRASSE".casefold())  # strasse
```

**基本写法：首字母大写**
`<字符串>.capitalize()`
```python
# 仅首字符大写其余小写
print("hELLO".capitalize())  # Hello
```

---

## 字符串判断

**基本写法：字符类型判断**
`isalpha / isdigit / isalnum / isspace`
```python
# 判断字符串组成类型
print("abc".isalpha())    # True
print("123".isdigit())    # True
print("  ".isspace())     # True
print("a1".isalnum())     # True
```

---

## 字符串转换

**基本写法：编码与解码**
`<字符串>.encode(<编码>) / <字节>.decode(<编码>)`
```python
# 字符串与字节互转
b = "中文".encode("utf-8")
print(b)                    # b'\xe4\xb8\xad...'
print(b.decode("utf-8"))    # 中文
```

**基本写法：translate 映射**
`<字符串>.translate(<映射表>)`
```python
# 按映射表批量替换字符
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))  # h2ll4
```

**基本写法：删除指定字符**
`str.maketrans("", "", <要删除字符>)`
```python
# 第三参数指定要删除的字符
table = str.maketrans("", "", "0123456789")
print("a1b2c".translate(table))  # abc
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
| Python 字符串格式化与方法 | 081-StringFormattingMethods | 本文自身 |
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
