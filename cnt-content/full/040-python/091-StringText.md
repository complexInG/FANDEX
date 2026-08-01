---
order: 910
title: Python 字符串与文本处理
module: python

category: '040-python'
difficulty: beginner
description: Python 字符串与文本处理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## string 模块

**基本写法：常量字符串**
`string.ascii_letters` | `string.digits`
```python
# 字符常量
import string

print(string.ascii_letters)  # a-zA-Z
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)         # 0-9
print(string.punctuation)    # 标点符号
```

**基本写法：Template 模板替换**
`string.Template(<模板>)`
```python
# 使用 $ 占位符的模板
from string import Template

t = Template("Hello, $name! You are $age.")
print(t.substitute(name="Alice", age=18))
```

**基本写法：safe_substitute 安全替换**
`t.safe_substitute(<字典>)`
```python
# 缺少占位符不报错
print(t.safe_substitute(name="Alice"))  # age 占位符保留
```

**基本写法：自定义分隔符**
`Template(<模板>, delimiter=<字符>)`
```python
# 自定义分隔符（如用 #）
class HashTemplate(Template):
    delimiter = "#"

t = HashTemplate("Hello, #name!")
print(t.substitute(name="Alice"))
```

---

## textwrap 文本换行

**基本写法：wrap 换行**
`textwrap.wrap(<文本>, width=<宽度>)`
```python
# 按指定宽度换行返回列表
import textwrap

lines = textwrap.wrap("Hello, World! This is a long text.", width=10)
print(lines)
```

**基本写法：fill 填充换行**
`textwrap.fill(<文本>, width=<宽度>)`
```python
# 返回换行后的字符串
print(textwrap.fill("Hello World!", width=5))
```

**基本写法：shorten 截断**
`textwrap.shorten(<文本>, width=<宽度>, placeholder=<占位>)`
```python
# 截断文本并添加占位符
print(textwrap.shorten("Hello World Hello Python", width=15, placeholder="..."))
```

**基本写法：dedent 去除缩进**
`textwrap.dedent(<文本>)`
```python
# 去除多行文本的公共缩进
text = """
    first
    second
    """
print(textwrap.dedent(text))
```

**基本写法：indent 添加缩进**
`textwrap.indent(<文本>, <前缀>)`
```python
# 给每行添加前缀
print(textwrap.indent("a\nb", "    "))
```

**基本写法：TextWrapper 对象**
`textwrap.TextWrapper(width=<宽度>)`
```python
# 复用配置
wrapper = textwrap.TextWrapper(width=70, initial_indent="> ", subsequent_indent="  ")
print(wrapper.fill("long text..."))
```

---

## unicodedata Unicode 数据

**基本写法：字符名称**
`unicodedata.name(<字符>)`
```python
# 获取 Unicode 字符名
import unicodedata

print(unicodedata.name("A"))  # LATIN CAPITAL LETTER A
print(unicodedata.name("中"))  # CJK UNIFIED IDEOGRAPH-4E2D
```

**基本写法：按名称查找字符**
`unicodedata.lookup(<名称>)`
```python
# 按名称查找字符
print(unicodedata.lookup("HEAVY BLACK HEART"))  # 心
```

**基本写法：分类**
`unicodedata.category(<字符>)`
```python
# 获取 Unicode 分类
print(unicodedata.category("A"))  # Lu（大写字母）
print(unicodedata.category("1"))  # Nd（数字）
```

**基本写法：数值**
`unicodedata.decimal(<字符>)` | `unicodedata.numeric(<字符>)`
```python
# 获取字符数值
print(unicodedata.decimal("5"))  # 5
print(unicodedata.numeric("½"))  # 0.5
```

**基本写法：标准化**
`unicodedata.normalize(<形式>, <字符串>)`
```python
# Unicode 标准化
s = "café"
print(unicodedata.normalize("NFC", s))  # 组合形式
print(unicodedata.normalize("NFD", s))  # 分解形式
```

**基本写法：字符镜像**
`unicodedata.mirrored(<字符>)`
```python
# 是否为镜像字符
print(unicodedata.mirrored("("))  # 1
```

---

## codecs 编解码

**基本写法：获取编码器**
`codecs.lookup(<编码>)`
```python
# 查询编码信息
import codecs

enc = codecs.lookup("utf-8")
print(enc.name)
```

**基本写法：open 编码打开**
`codecs.open(<文件>, <模式>, <编码>)`
```python
# 指定编码打开文件
with codecs.open("file.txt", "r", "utf-8") as f:
    print(f.read())
```

**基本写法：编码与解码**
`codecs.encode(<字符串>, <编码>)` | `codecs.decode(<字节>, <编码>)`
```python
# 编码转换
b = codecs.encode("hello", "utf-8")
s = codecs.decode(b, "utf-8")
```

**基本写法：转码**
`codecs.encode(<字符串>, "rot_13")`
```python
# 特殊编码如 rot13
print(codecs.encode("hello", "rot_13"))
```

---

## 字符串方法扩展

**基本写法：str.translate 翻译表**
`str.maketrans(<字典>)`
```python
# 批量字符替换/删除
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))  # h2ll4

# 删除字符
del_table = str.maketrans("", "", "aeiou")
print("hello".translate(del_table))  # hll
```

**基本写法：str.partition 分区**
`<字符串>.partition(<分隔符>)`
```python
# 三元组返回
print("a=b".partition("="))  # ("a", "=", "b")
```

**基本写法：str.format_map**
`<字符串>.format_map(<字典>)`
```python
# 用字典格式化
d = {"name": "Alice", "age": 18}
print("{name} is {age}".format_map(d))
```

---

## binascii 二进制文本

**基本写法：base64 编码**
`base64.b64encode(<字节>)`
```python
# Base64 编解码
import base64

print(base64.b64encode(b"hello"))
print(base64.b64decode(b"aGVsbG8="))
```

**基本写法：hex 编码**
`<字节>.hex()` | `bytes.fromhex(<字符串>)`
```python
# 十六进制编解码
print(b"hello".hex())
print(bytes.fromhex("68656c6c6f"))
```

**基本写法：URL 安全 base64**
`base64.urlsafe_b64encode(<字节>)`
```python
# URL 安全的 base64
print(base64.urlsafe_b64encode(b"ab?cd"))
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
| Python 字符串与文本处理 | 091-StringText | 本文自身 |
| Python decimal 与 fractions | 092-DecimalFractions | 本文的并列主题 |
| Python shutil 与 tempfile | 093-ShutilTempfile | 本文的并列主题 |
| Python gc inspect dis | 094-GcInspect | 本文的并列主题 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
