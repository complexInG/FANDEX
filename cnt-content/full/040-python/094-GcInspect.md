---
order: 940
title: Python gc inspect dis
module: python

category: '040-python'
difficulty: beginner
description: Python gc inspect dis 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## gc 垃圾回收

**基本写法：手动回收**
`gc.collect()`
```python
# 触发垃圾回收
import gc

print(gc.collect())  # 返回回收对象数
```

**基本写法：分代回收**
`gc.collect(<代>)`
```python
# 只回收指定代（0/1/2）
gc.collect(0)
```

**基本写法：获取对象引用**
`gc.get_referrers(<对象>)`
```python
# 获取引用指定对象的对象
class Obj: pass
o = Obj()
lst = [o]
print(gc.get_referrers(o))
```

**基本写法：获取引用对象**
`gc.get_referents(<对象>)`
```python
# 获取对象引用的对象
print(gc.get_referents(lst))
```

**基本写法：获取阈值**
`gc.get_threshold()`
```python
# 获取分代回收阈值
print(gc.get_threshold())  # (700, 10, 10)
```

**基本写法：设置阈值**
`gc.set_threshold(<阈值0>, <阈值1>, <阈值2>)`
```python
# 调整回收阈值
gc.set_threshold(1000, 15, 15)
```

**基本写法：禁用/启用**
`gc.disable()` | `gc.enable()`
```python
# 禁用自动 GC
gc.disable()
gc.enable()
```

**基本写法：调试标志**
`gc.set_debug(<标志>)`
```python
# 设置调试输出
gc.set_debug(gc.DEBUG_LEAK)
```

**基本写法：跟踪对象**
`gc.callbacks.append(<回调>)`
```python
# 注册 GC 回调
def on_gc(phase, info):
    print(phase, info)
gc.callbacks.append(on_gc)
```

**基本写法：循环引用检测**
`gc.garbage`
```python
# 有 __del__ 的循环引用对象列表
print(gc.garbage)
```

---

## inspect 检查

**基本写法：获取源码**
`inspect.getsource(<对象>)`
```python
# 获取函数/类的源代码
import inspect

def foo():
    pass

print(inspect.getsource(foo))
```

**基本写法：获取文件**
`inspect.getfile(<对象>)`
```python
# 获取对象定义所在文件
print(inspect.getfile(foo))
```

**基本写法：获取模块**
`inspect.getmodule(<对象>)`
```python
# 获取对象所属模块
print(inspect.getmodule(foo))
```

**基本写法：签名信息**
`inspect.signature(<函数>)`
```python
# 获取函数签名
def add(a, b=10):
    return a + b

sig = inspect.signature(add)
print(sig.parameters)
```

**基本写法：参数详情**
`inspect.Parameter`
```python
# 检查参数
for name, p in sig.parameters.items():
    print(name, p.kind, p.default)
```

**基本写法：是否为函数/类**
`inspect.isfunction(<对象>)` | `inspect.isclass(<对象>)`
```python
# 类型判断
print(inspect.isfunction(foo))
print(inspect.isclass(int))
```

**基本写法：成员列表**
`inspect.getmembers(<对象>, <谓词>)`
```python
# 获取对象成员
class A:
    def method(self): pass

for name, member in inspect.getmembers(A, inspect.isfunction):
    print(name)
```

**基本写法：获取类层级**
`inspect.getmro(<类>)`
```python
# 获取方法解析顺序
print(inspect.getmro(int))
```

**基本写法：获取调用栈**
`inspect.stack()`
```python
# 获取调用栈帧
def outer():
    inner()

def inner():
    for frame in inspect.stack():
        print(frame.function)

outer()
```

**基本写法：当前帧**
`inspect.currentframe()`
```python
# 获取当前帧
frame = inspect.currentframe()
print(frame.f_code.co_name)
```

---

## dis 字节码反汇编

**基本写法：反汇编函数**
`dis.dis(<函数>)`
```python
# 反汇编为字节码
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

**基本写法：反汇编字符串代码**
`dis.dis(<代码字符串>)`
```python
# 反汇编代码字符串
dis.dis("a + b")
```

**基本写法：获取字节码**
`dis.Bytecode(<函数>)`
```python
# 获取 Bytecode 对象迭代
for instr in dis.Bytecode(add):
    print(instr.opname, instr.argval)
```

**基本写法：查看常量**
`dis.code_info(<函数>)`
```python
# 获取代码对象信息
print(dis.code_info(add))
```

**基本写法：show_code**
`dis.show_code(<函数>)`
```python
# 打印代码对象信息
dis.show_code(add)
```

---

## ast 抽象语法树

**基本写法：解析代码**
`ast.parse(<代码字符串>)`
```python
# 解析为 AST
import ast

tree = ast.parse("x = 1 + 2")
print(ast.dump(tree))
```

**基本写法：遍历节点**
`ast.walk(<树>)`
```python
# 遍历所有节点
for node in ast.walk(tree):
    print(type(node).__name__)
```

**基本写法：NodeVisitor 访问**
`class <类>(ast.NodeVisitor):\n    def visit_<节点>(self, node):`
```python
# 自定义访问器
class Counter(ast.NodeVisitor):
    def __init__(self):
        self.count = 0
    def visit_Call(self, node):
        self.count += 1
        self.generic_visit(node)

c = Counter()
c.visit(ast.parse("a(); b()"))
print(c.count)
```

**基本写法：NodeTransformer 修改**
`class <类>(ast.NodeTransformer):`
```python
# 修改 AST 节点
class Double(ast.NodeTransformer):
    def visit_Num(self, node):
        return ast.copy_location(ast.Num(n=node.n * 2), node)
```

**基本写法：unparse 反向生成**
`ast.unparse(<树>)`
```python
# AST 转回代码字符串（3.9+）
print(ast.unparse(tree))
```

**基本写法：literal_eval 安全求值**
`ast.literal_eval(<字符串>)`
```python
# 安全求值字面值
print(ast.literal_eval("[1, 2, 3]"))
print(ast.literal_eval("{'a': 1}"))
```

---

## sys.intern 字符串驻留

**基本写法：字符串驻留**
`sys.intern(<字符串>)`
```python
# 字符串驻留，节省内存
import sys

a = sys.intern("hello")
b = sys.intern("hello")
print(a is b)  # True
```

---

## sys.getsizeof 对象大小

**基本写法：获取对象大小**
`sys.getsizeof(<对象>)`
```python
# 获取对象字节大小
print(sys.getsizeof([1, 2, 3]))
print(sys.getsizeof("hello"))
```

**基本写法：递归大小**
`sys.getsizeof(<对象>, <默认>)`
```python
# 配合递归计算容器总大小
def total_size(obj):
    seen = set()
    def inner(o):
        if id(o) in seen:
            return 0
        seen.add(id(o))
        s = sys.getsizeof(o)
        if isinstance(o, (list, tuple, set)):
            s += sum(inner(i) for i in o)
        return s
    return inner(obj)
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
| Python gc inspect dis | 094-GcInspect | 本文自身 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
