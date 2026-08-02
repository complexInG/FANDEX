---
order: 760
title: Python sys/os 平台接口
module: python

category: '040-python'
difficulty: beginner
description: Python sys/os 平台接口 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## sys 解释器接口

**基本写法：命令行参数**
`sys.argv`
```python
# 获取命令行参数列表
import sys
print(sys.argv)         # ['script.py', 'arg1', 'arg2']
print(sys.argv[1:])     # 用户传入的参数
```

**基本写法：退出程序**
`sys.exit([<状态码>])`
```python
# 退出并返回状态码
if len(sys.argv) < 2:
    sys.exit(1)  # 非零表示异常退出
```

**基本写法：标准输入输出**
`sys.stdin / sys.stdout / sys.stderr`
```python
# 重定向或直接使用标准流
sys.stdout.write("标准输出\n")
sys.stderr.write("错误信息\n")
name = sys.stdin.readline().strip()
```

**基本写法：递归深度**
`sys.getrecursionlimit() / sys.setrecursionlimit(<n>)`
```python
# 查询与设置递归深度上限
print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(2000)
```

**基本写法：版本信息**
`sys.version / sys.version_info`
```python
# 获取解释器版本
print(sys.version_info.major, sys.version_info.minor)  # 3 12
```

**基本写法：平台标识**
`sys.platform`
```python
# 获取操作系统平台标识
print(sys.platform)  # win32 / linux / darwin
```

**基本写法：最大整数值**
`sys.maxsize`
```python
# 获取平台最大整数
print(sys.maxsize)  # 64 位系统为 2**63 - 1
```

**基本写法：模块搜索路径**
`sys.path`
```python
# 查看与修改模块搜索路径
import sys
sys.path.append("/custom/libs")
```

**基本写法：递增打印进度**
`sys.stdout.write + \r`
```python
# 原地刷新输出进度条
for i in range(101):
    sys.stdout.write(f"\r进度: {i}%")
    sys.stdout.flush()
```

---

## os 目录与文件操作

**基本写法：当前工作目录**
`os.getcwd()`
```python
# 获取当前工作目录
import os
print(os.getcwd())
```

**基本写法：切换目录**
`os.chdir(<路径>)`
```python
# 改变当前工作目录
os.chdir("/tmp")
```

**基本写法：列出目录内容**
`os.listdir(<路径>)`
```python
# 列出目录下所有条目
for name in os.listdir("."):
    print(name)
```

**基本写法：创建目录**
`os.mkdir(<路径>) / os.makedirs(<路径>)`
```python
# 创建单层或多层目录
os.mkdir("newdir")
os.makedirs("a/b/c", exist_ok=True)
```

**基本写法：删除文件与目录**
`os.remove(<文件>) / os.rmdir(<空目录>)`
```python
# 删除文件或空目录
os.remove("data.txt")
os.rmdir("emptydir")
```

**基本写法：递归删除目录树**
`shutil.rmtree(<目录>)`
```python
# 递归删除非空目录
import shutil
shutil.rmtree("old_project")
```

**基本写法：重命名与移动**
`os.rename(<旧名>, <新名>)`
```python
# 重命名文件或目录
os.rename("old.txt", "new.txt")
```

**基本写法：递归遍历目录**
`os.walk(<路径>)`
```python
# 自顶向下遍历目录树
for root, dirs, files in os.walk("."):
    for f in files:
        print(os.path.join(root, f))
```

**基本写法：文件信息**
`os.stat(<路径>)`
```python
# 获取文件大小、修改时间等元信息
st = os.stat("data.txt")
print(st.st_size, st.st_mtime)
```

---

## os 环境与进程

**基本写法：环境变量**
`os.environ`
```python
# 读取与设置环境变量
print(os.environ.get("HOME"))
os.environ["MY_VAR"] = "value"
```

**基本写法：获取进程号**
`os.getpid() / os.getppid()`
```python
# 获取当前进程与父进程 ID
print(os.getpid(), os.getppid())
```

**基本写法：执行系统命令**
`os.system(<命令>)`
```python
# 执行 shell 命令并返回退出码
ret = os.system("echo hello")
```

**基本写法：CPU 核数**
`os.cpu_count()`
```python
# 获取系统 CPU 核心数
print(os.cpu_count())
```

**基本写法：获取系统随机字节**
`os.urandom(<字节数>)`
```python
# 生成密码学安全的随机字节
token = os.urandom(16)
```

---

## os.path 路径操作

**基本写法：拼接路径**
`os.path.join(<路径1>, <路径2>)`
```python
# 跨平台安全拼接路径
p = os.path.join("dir", "sub", "file.txt")
```

**基本写法：判断存在**
`os.path.exists(<路径>)`
```python
# 判断路径是否存在
print(os.path.exists("data.txt"))
```

**基本写法：判断文件与目录**
`os.path.isfile(<路径>) / os.path.isdir(<路径>)`
```python
# 区分文件与目录
print(os.path.isfile("a.txt"), os.path.isdir("d"))
```

**基本写法：取文件名与目录名**
`os.path.basename(<路径>) / os.path.dirname(<路径>)`
```python
# 拆分路径末尾与父目录
print(os.path.basename("/a/b/c.txt"))  # c.txt
print(os.path.dirname("/a/b/c.txt"))   # /a/b
```

**基本写法：扩展名拆分**
`os.path.splitext(<路径>)`
```python
# 分离文件名与扩展名
name, ext = os.path.splitext("archive.tar.gz")
print(name, ext)  # archive.tar .gz
```

**基本写法：绝对路径**
`os.path.abspath(<路径>) / os.path.realpath(<路径>)`
```python
# 转换为绝对路径并解析软链接
print(os.path.abspath("../a.txt"))
print(os.path.realpath("link.txt"))
```

**基本写法：路径大小与时间**
`os.path.getsize(<路径>) / os.path.getmtime(<路径>)`
```python
# 获取文件大小与修改时间
print(os.path.getsize("a.txt"))
```

---

## platform 平台信息

**基本写法：操作系统类型**
`platform.system()`
```python
# 获取操作系统名称
import platform
print(platform.system())  # Windows / Linux / Darwin
```

**基本写法：Python 版本**
`platform.python_version()`
```python
# 获取当前 Python 版本字符串
print(platform.python_version())  # 3.12.0
```

**基本写法：机器架构**
`platform.machine()`
```python
# 获取 CPU 架构
print(platform.machine())  # AMD64 / arm64
```

## 延伸阅读
Python 数据类型与内置容器，见 040-python 模块的基础文档。
Python 异步编程（asyncio/FastAPI），见 040-python 模块的异步与 Web 文档。
Python 数据分析（NumPy/Pandas），见 051-data-analysis 模块。
Python 与数据库交互（SQLAlchemy），见 019-sql 模块相关文档。
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
