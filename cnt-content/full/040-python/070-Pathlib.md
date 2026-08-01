---
order: 700
title: Python pathlib 路径操作
module: 040-python
category: '040-python'
difficulty: beginner
description: Python pathlib 路径操作 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Python pathlib 路径操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 路径创建

**基本写法：创建路径对象**
`Path(<路径字符串>)`
```python
# 创建 Path 对象
from pathlib import Path
p = Path("/usr/local/bin")
```

**基本写法：当前目录**
`Path.cwd()`
```python
# 获取当前工作目录
cwd = Path.cwd()
```

**基本写法：用户主目录**
`Path.home()`
```python
# 获取用户主目录
home = Path.home()
```

**基本写法：路径拼接**
`Path(<父路径>) / <子路径>`
```python
# 使用 / 运算符拼接路径
config = Path("/etc") / "nginx" / "nginx.conf"
```

**基本写法：joinpath 多级拼接**
`<路径>.joinpath(<子路径1>, <子路径2>)`
```python
# 拼接多个路径段
p = Path("/var").joinpath("log", "app.log")
```

---

## 路径属性

**基本写法：获取文件名**
`<路径>.name`
```python
# 返回最后一级路径名
p = Path("/a/b/c.txt")
print(p.name)  # c.txt
```

**基本写法：获取文件名（不含扩展名）**
`<路径>.stem`
```python
# 返回不含扩展名的文件名
p = Path("archive.tar.gz")
print(p.stem)  # archive.tar
```

**基本写法：获取扩展名**
`<路径>.suffix`
```python
# 返回最后一个扩展名
p = Path("file.tar.gz")
print(p.suffix)  # .gz
```

**基本写法：获取所有扩展名**
`<路径>.suffixes`
```python
# 返回所有扩展名列表
p = Path("file.tar.gz")
print(p.suffixes)  # ['.tar', '.gz']
```

**基本写法：获取父目录**
`<路径>.parent`
```python
# 返回上一级目录
p = Path("/a/b/c.txt")
print(p.parent)  # /a/b
```

**基本写法：获取所有父目录**
`<路径>.parents`
```python
# 返回所有上级目录的可迭代对象
p = Path("/a/b/c.txt")
for parent in p.parents:
    print(parent)
```

**基本写法：获取绝对路径**
`<路径>.resolve()`
```python
# 返回解析后的绝对路径
p = Path("./config").resolve()
```

**基本写法：获取路径各部分**
`<路径>.parts`
```python
# 返回路径各段组成的元组
p = Path("/usr/local/bin")
print(p.parts)  # ('/', 'usr', 'local', 'bin')
```

---

## 路径判断

**基本写法：判断文件是否存在**
`<路径>.exists()`
```python
# 检查路径是否存在
if Path("file.txt").exists():
    print("存在")
```

**基本写法：判断是否为文件**
`<路径>.is_file()`
```python
# 检查是否为普通文件
Path("file.txt").is_file()
```

**基本写法：判断是否为目录**
`<路径>.is_dir()`
```python
# 检查是否为目录
Path("/usr").is_dir()
```

**基本写法：判断是否为绝对路径**
`<路径>.is_absolute()`
```python
# 检查是否为绝对路径
Path("/usr").is_absolute()  # True
Path("usr").is_absolute()   # False
```

---

## 文件读写

**基本写法：读取文本文件**
`<路径>.read_text([encoding=<编码>])`
```python
# 一次性读取整个文本文件
content = Path("file.txt").read_text(encoding="utf-8")
```

**基本写法：写入文本文件**
`<路径>.write_text(<内容>, [encoding=<编码>])`
```python
# 一次性写入文本
Path("output.txt").write_text("hello", encoding="utf-8")
```

**基本写法：读取二进制文件**
`<路径>.read_bytes()`
```python
# 读取二进制内容
data = Path("image.png").read_bytes()
```

**基本写法：写入二进制文件**
`<路径>.write_bytes(<数据>)`
```python
# 写入二进制数据
Path("data.bin").write_bytes(b"\x00\x01")
```

**换行写法：打开文件上下文管理**
`with <路径>.open([mode], [encoding]) as <变量>:`
```python
# 使用 open 方法逐行读取
with Path("file.txt").open("r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## 目录操作

**基本写法：创建目录**
`<路径>.mkdir([parents=True], [exist_ok=True])`
```python
# 递归创建目录，已存在不报错
Path("a/b/c").mkdir(parents=True, exist_ok=True)
```

**基本写法：删除空目录**
`<路径>.rmdir()`
```python
# 删除空目录
Path("empty_dir").rmdir()
```

**基本写法：删除文件**
`<路径>.unlink()`
```python
# 删除单个文件
Path("file.txt").unlink()
```

**基本写法：删除文件（不存在不报错）**
`<路径>.unlink(missing_ok=True)`
```python
# Python 3.8+ 文件不存在时不抛出异常
Path("file.txt").unlink(missing_ok=True)
```

**基本写法：重命名或移动**
`<路径>.rename(<目标路径>)`
```python
# 移动文件或重命名
Path("old.txt").rename("new.txt")
```

**基本写法：Python 3.13+ replace 兼容性**
`<路径>.replace(<目标路径>)`
```python
# 覆盖目标路径并替换
Path("temp.txt").replace("final.txt")
```

---

## 遍历目录

**基本写法：列出目录内容**
`<路径>.iterdir()`
```python
# 遍历目录下的直接子项
for item in Path(".").iterdir():
    print(item.name)
```

**基本写法：glob 模式匹配**
`<路径>.glob(<模式>)`
```python
# 递归匹配文件
for p in Path(".").glob("**/*.py"):
    print(p)
```

**基本写法：rglob 递归匹配**
`<路径>.rglob(<模式>)`
```python
# 递归搜索所有子目录
for p in Path(".").rglob("*.py"):
    print(p)
```

**基本写法：Python 3.12+ 模式参数**
`<路径>.glob(<模式>, case_sensitive=<布尔>)`
```python
# Python 3.12+ 支持大小写敏感控制
for p in Path(".").glob("*.PY", case_sensitive=False):
    print(p)
```

---

## 文件信息

**基本写法：获取文件状态**
`<路径>.stat()`
```python
# 获取文件元数据
info = Path("file.txt").stat()
print(info.st_size, info.st_mtime)
```

**基本写法：获取文件大小**
`<路径>.stat().st_size`
```python
# 返回文件字节数
size = Path("file.txt").stat().st_size
```

**基本写法：获取修改时间**
`<路径>.stat().st_mtime`
```python
# 返回最后修改时间戳
import time
mtime = Path("file.txt").stat().st_mtime
print(time.ctime(mtime))
```

---

## 路径匹配与变换

**基本写法：路径模式匹配**
`<路径>.match(<模式>)`
```python
# 判断路径是否匹配模式
Path("a/b/c.txt").match("*.txt")  # True
Path("a/b/c.txt").match("a/*.txt")  # False
```

**基本写法：修改文件名**
`<路径>.with_name(<新名称>)`
```python
# 返回替换文件名后的新路径
p = Path("/a/b/c.txt")
new_p = p.with_name("d.txt")  # /a/b/d.txt
```

**基本写法：修改扩展名**
`<路径>.with_suffix(<新扩展名>)`
```python
# 返回替换扩展名后的新路径
p = Path("file.txt")
new_p = p.with_suffix(".md")
```

**基本写法：修改父目录**
`<路径>.with_parent(<新父目录>)`
```python
# Python 3.12+ 替换父目录
p = Path("/old/file.txt")
new_p = p.with_parent("/new")  # /new/file.txt
```

**基本写法：相对路径**
`<路径>.relative_to(<基准路径>)`
```python
# 计算相对路径
p = Path("/usr/local/bin")
rel = p.relative_to("/usr")  # local/bin
```

---

## Python 3.13+ pathlib 增强

**基本写法：Python 3.13+ from_uri**
`Path.from_uri(<URI>)`
```python
# Python 3.13+ 从 URI 创建路径
p = Path.from_uri("file:///usr/local/bin")
```

**基本写法：Python 3.13+ as_uri**
`<路径>.as_uri()`
```python
# 将绝对路径转为 file URI
uri = Path("/usr/local").as_uri()
```

**基本写法：Python 3.13+ full_match**
`<路径>.full_match(<模式>)`
```python
# Python 3.13+ 完整路径匹配
Path("/a/b/c.txt").full_match("/a/**/*.txt")
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
| Python pathlib 路径操作 | 070-Pathlib | 本文自身 |
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
