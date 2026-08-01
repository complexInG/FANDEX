---
order: 670
title: 基础数据类型
module: python

category: '040-python'
difficulty: beginner
description: 基础数据类型 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 整数类型

**基本写法：十进制整数**
`<十进制> = 123`

```python
# 十进制整数
x = 123
```

---

**基本写法：二进制整数**
`<二进制> = 0b<二进制串>`

```python
# 二进制整数（以 0b 开头）
y = 0b1010
```

---

**基本写法：八进制整数**
`<八进制> = 0o<八进制串>`

```python
# 八进制整数（以 0o 开头）
z = 0o123
```

---

**基本写法：十六进制整数**
`<十六进制> = 0x<十六进制串>`

```python
# 十六进制整数（以 0x 开头）
p = 0x1A
```

---

## 整数运算

**基本写法：加法运算**
`<操作数1> + <操作数2>`

```python
# 整数加法
addition = 10 + 5
```

---

**基本写法：整除运算**
`<操作数1> // <操作数2>`

```python
# 整除（向下取整）
floor_division = 10 // 3
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`

```python
# 取模（求余数）
modulo = 10 % 3
```

---

**基本写法：幂运算**
`<操作数1> ** <操作数2>`

```python
# 幂运算
power = 2 ** 3
```

---

**基本写法：复合赋值运算**
`<变量> <运算符>= <值>`

```python
# 复合赋值运算符
x = 10
x += 5
```

---

## 浮点数类型

**基本写法：普通浮点数**
`<浮点数> = <小数>`

```python
# 普通浮点数
pi = 3.14159
```

---

**基本写法：科学记数法**
`<科学记数法> = <尾数>e<指数>`

```python
# 科学记数法
avogadro = 6.022e23
```

---

## 复数类型

**基本写法：复数字面量**
`<复数> = <实部> + <虚部>j`

```python
# 复数定义
c1 = 3 + 4j
```

---

**基本写法：使用 complex() 函数**
`complex(<实部>, <虚部>)`

```python
# 使用 complex() 创建复数
c2 = complex(2, 5)
```

---

**基本写法：访问复数实部**
`<复数>.real`

```python
# 获取复数的实部
print(c1.real)
```

---

**基本写法：访问复数虚部**
`<复数>.imag`

```python
# 获取复数的虚部
print(c1.imag)
```

---

## 数学函数

**基本写法：导入 math 模块**
`import math`

```python
# 导入数学模块
import math
```

---

**基本写法：调用 math 函数**
`math.<函数>(<参数>)`

```python
# 计算平方根
print(math.sqrt(16))
```

---

**基本写法：向下取整**
`math.floor(<浮点数>)`

```python
# 向下取整
print(math.floor(3.9))
```

---

**基本写法：向上取整**
`math.ceil(<浮点数>)`

```python
# 向上取整
print(math.ceil(3.1))
```

---

## 字符串

**基本写法：单引号字符串**
`'<字符串>'`

```python
# 单引号字符串
s1 = 'Hello, World!'
```

---

**基本写法：双引号字符串**
`"<字符串>"`

```python
# 双引号字符串
s2 = "Hello, World!"
```

---

**换行写法：三引号多行字符串**
`'''<多行字符串>'''`

```python
# 三引号字符串（支持多行）
s3 = '''Hello,
World!'''
```

---

**基本写法：原始字符串**
`r'<字符串>'`

```python
# 原始字符串（不转义）
s4 = r'C:\path\to\file'
```

---

**基本写法：字节字符串**
`b'<字符串>'`

```python
# 字节字符串
s5 = b'Hello'
```

---

## 字符串拼接

**基本写法：使用 + 运算符拼接**
`<字符串1> + <字符串2>`

```python
# 使用 + 拼接字符串
full_name = "Alice" + " " + "Smith"
```

---

**基本写法：使用 * 运算符重复**
`<字符串> * <次数>`

```python
# 使用 * 重复字符串
print("Hello" * 3)
```

---

## 字符串切片

**基本写法：获取单个字符**
`<字符串>[<索引>]`

```python
# 获取指定位置的字符
print(s[0])
```

---

**基本写法：切片操作**
`<字符串>[<start>:<stop>:<step>]`

```python
# 切片获取子字符串
print(s[0:5])
```

---

**基本写法：反转字符串**
`<字符串>[::-1]`

```python
# 使用切片反转字符串
print(s[::-1])
```

---

## 字符串方法

**基本写法：转换为大写**
`<字符串>.upper()`

```python
# 转换为大写
print(s.upper())
```

---

**基本写法：查找子串位置**
`<字符串>.find(<子串>)`

```python
# 查找子串位置
print(s.find("World"))
```

---

**基本写法：替换子串**
`<字符串>.replace(<旧子串>, <新子串>)`

```python
# 替换字符串中的子串
print(s.replace("World", "Python"))
```

---

**基本写法：分割字符串**
`<字符串>.split(<分隔符>)`

```python
# 按分隔符分割字符串
print(s.split(", "))
```

---

**基本写法：连接字符串列表**
`<分隔符>.join(<字符串列表>)`

```python
# 使用分隔符连接字符串列表
print(", ".join(["Hello", "Python"]))
```

---

**基本写法：去除空白字符**
`<字符串>.strip()`

```python
# 去除两端空白字符
print(" Hello ".strip())
```

---

## 字符串格式化

**基本写法：f-string 格式化**
`f"<文本>{<表达式>}"`

```python
# f-string 基本用法
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

---

**基本写法：f-string 格式化选项**
`f"<文本>{<表达式>:<格式说明>}"`

```python
# f-string 浮点数格式化
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")
```

---

**基本写法：format() 方法**
`"<文本>{}".format(<参数>)`

```python
# 使用 format() 方法格式化
print("My name is {} and I am {} years old.".format("Alice", 30))
```

---

**基本写法：% 运算符格式化**
`"<格式>" % <值>`

```python
# C 风格 % 格式化
print("My name is %s and I am %d years old." % ("Alice", 30))
```

---

## 布尔类型

**基本写法：逻辑与运算**
`<表达式> and <表达式>`

```python
# 逻辑与运算
print(True and False)
```

---

**基本写法：逻辑或运算**
`<表达式> or <表达式>`

```python
# 逻辑或运算
print(True or False)
```

---

**基本写法：逻辑非运算**
`not <表达式>`

```python
# 逻辑非运算
print(not True)
```

---

**基本写法：布尔上下文判断**
`if <对象>: <语句>`

```python
# 在布尔上下文中判断对象真假
if "Hello":
    print("非空字符串为真")
```

---

## 空值 None

**基本写法：赋值为 None**
`<变量> = None`

```python
# 赋值为 None
x = None
```

---

**基本写法：使用 is 检查 None**
`<变量> is None`

```python
# 使用 is 运算符检查 None
x = None
print(x is None)
```

---

## 类型转换

**基本写法：转换为整数**
`int(<值>)`

```python
# 转换为整数
print(int("123"))
```

---

**基本写法：转换为浮点数**
`float(<值>)`

```python
# 转换为浮点数
print(float("3.14"))
```

---

**基本写法：转换为字符串**
`str(<值>)`

```python
# 转换为字符串
print(str(123))
```

---

**基本写法：转换为布尔值**
`bool(<值>)`

```python
# 转换为布尔值
print(bool(1))
```

---

**基本写法：转换为列表**
`list(<可迭代对象>)`

```python
# 转换为列表
print(list("Hello"))
```

---

**基本写法：转换为元组**
`tuple(<可迭代对象>)`

```python
# 转换为元组
print(tuple([1, 2, 3]))
```

---

**基本写法：转换为集合**
`set(<可迭代对象>)`

```python
# 转换为集合（去重）
print(set([1, 2, 3, 2, 1]))
```

---

**基本写法：转换为字典**
`dict(<键值对序列>)`

```python
# 转换为字典
print(dict([("a", 1), ("b", 2)]))
```

---

## 类型检查

**基本写法：获取对象类型**
`type(<对象>)`

```python
# 获取对象的类型
print(type(42))
```

---

**基本写法：检查对象是否为指定类型**
`isinstance(<对象>, <类型>)`

```python
# 检查对象是否为指定类型
print(isinstance(42, int))
```

---

**基本写法：检查是否为多种类型之一**
`isinstance(<对象>, (<类型1>, <类型2>))`

```python
# 检查对象是否为多种类型之一
print(isinstance(42, (int, float)))
```

---

## Python 3.13+ 新特性

**基本写法：type 参数支持复数形式**
`type(<对象>, complex)`

```python
# Python 3.13 type() 第三参数支持复数形式（用于复数类型判断）
x = 3 + 4j
print(type(x, complex))
```

---

**基本写法：Python 3.13 改进的错误消息**
`<表达式>  # 触发错误时高亮精确位置`

```python
# Python 3.13 改进的错误消息（更精确的错误定位）
# 字典键访问错误会精确高亮具体键名,而非整行
data = {"name": "Alice"}
# data["age"]  # 触发 KeyError 时错误消息高亮 "age" 字符串本身
```

---

**基本写法：Python 3.14 t-string 模板字符串**
`t"<文本>{<表达式>}"`

```python
# Python 3.14 t-string 模板字符串（返回 Template 对象,不立即求值）
name = "Alice"
template = t"Hello, {name}!"
```

---

**基本写法：Python 3.14 模板字符串渲染**
`<模板>.render(<上下文字典>)`

```python
# Python 3.14 模板字符串渲染（调用 render 方法执行求值）
template = t"Hello, {name}!"
result = template.render({"name": "Alice"})
print(result)
```

---

**基本写法：Python 3.13 自由线程模式**
`python -X gil=0 <脚本>`

```python
# Python 3.13 自由线程模式（禁用 GIL,允许多线程真正并行）
# 命令行执行：python -X gil=0 script.py
# 需使用启用 --disable-gil 编译选项的 Python 解释器
```

---

**基本写法：Python 3.13 实验性 JIT**
`python -X jit <脚本>`

```python
# Python 3.13 实验性 JIT 编译器（提升长运行任务性能）
# 命令行执行：python -X jit script.py
# 需使用启用 --enable-experimental-jit 编译选项的 Python 解释器
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
| 基础数据类型 | 067-BasicDataType | 本文自身 |
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
