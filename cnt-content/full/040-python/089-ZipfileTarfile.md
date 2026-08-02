---
order: 890
title: Python zipfile 与 tarfile
module: 'python'
category: 后端技术
difficulty: beginner
description: Python zipfile 与 tarfile 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## zipfile 读取

**基本写法：打开 ZIP**
`zipfile.ZipFile(<文件>, <模式>)`
```python
# 打开 zip 文件
import zipfile

with zipfile.ZipFile("archive.zip", "r") as zf:
    print(zf.namelist())
```

**基本写法：列出文件**
`zf.namelist()`
```python
# 列出 zip 内所有文件
with zipfile.ZipFile("archive.zip") as zf:
    for name in zf.namelist():
        print(name)
```

**基本写法：读取文件**
`zf.read(<文件名>)`
```python
# 读取 zip 内文件内容
with zipfile.ZipFile("archive.zip") as zf:
    data = zf.read("data.txt")
    print(data.decode())
```

**基本写法：提取文件**
`zf.extract(<文件名>, <目录>)`
```python
# 提取单个文件
with zipfile.ZipFile("archive.zip") as zf:
    zf.extract("data.txt", "output")
```

**基本写法：提取全部**
`zf.extractall(<目录>)`
```python
# 提取全部文件
with zipfile.ZipFile("archive.zip") as zf:
    zf.extractall("output")
```

---

## zipfile 写入

**基本写法：创建 ZIP**
`zipfile.ZipFile(<文件>, "w", <压缩>)`
```python
# 创建新 zip 文件
import zipfile

with zipfile.ZipFile("new.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("data.txt")
    zf.write("config.json")
```

**基本写法：追加文件**
`zipfile.ZipFile(<文件>, "a")`
```python
# 追加文件到已有 zip
with zipfile.ZipFile("new.zip", "a") as zf:
    zf.write("extra.txt")
```

**基本写法：writestr 写入字符串**
`zf.writestr(<文件名>, <数据>)`
```python
# 直接写入字符串/字节
with zipfile.ZipFile("new.zip", "w") as zf:
    zf.writestr("hello.txt", "Hello, World!")
    zf.writestr("data.json", '{"a": 1}')
```

---

## zipfile 信息

**基本写法：获取文件信息**
`zf.getinfo(<文件名>)`
```python
# 获取 ZipInfo 对象
with zipfile.ZipFile("archive.zip") as zf:
    info = zf.getinfo("data.txt")
    print(info.file_size, info.compress_size, info.date_time)
```

**基本写法：infolist 全部信息**
`zf.infolist()`
```python
# 获取所有文件信息
with zipfile.ZipFile("archive.zip") as zf:
    for info in zf.infolist():
        print(info.filename, info.file_size)
```

---

## ZIP 加密

**基本写法：密码解密**
`zf.setpassword(<密码>)`
```python
# 解密 zip
with zipfile.ZipFile("secret.zip") as zf:
    zf.setpassword(b"password")
    print(zf.read("data.txt"))
```

---

## tarfile 读取

**基本写法：打开 tar**
`tarfile.open(<文件>, <模式>)`
```python
# 打开 tar 文件
import tarfile

with tarfile.open("archive.tar.gz", "r:gz") as tf:
    print(tf.getnames())
```

**基本写法：列出成员**
`tf.getnames()` | `tf.getmembers()`
```python
# 列出 tar 内文件
with tarfile.open("archive.tar") as tf:
    for m in tf.getmembers():
        print(m.name, m.size, m.isfile())
```

**基本写法：提取文件**
`tf.extract(<成员>, <目录>)`
```python
# 提取单个文件
with tarfile.open("archive.tar") as tf:
    tf.extract("data.txt", "output")
```

**基本写法：提取全部**
`tf.extractall(<目录>)`
```python
# 提取全部
with tarfile.open("archive.tar") as tf:
    tf.extractall("output")
```

**基本写法：安全提取（3.12+）**
`tf.extractall(<目录>, filter="data")`
```python
# 3.12+ 推荐使用 filter 防止路径穿越
with tarfile.open("archive.tar") as tf:
    tf.extractall("output", filter="data")
```

---

## tarfile 写入

**基本写法：创建 tar**
`tarfile.open(<文件>, "w:<压缩>")`
```python
# 创建 tar.gz
with tarfile.open("new.tar.gz", "w:gz") as tf:
    tf.add("data.txt")
    tf.add("config.json")
```

**基本写法：添加文件**
`tf.add(<文件>, arcname=<归档名>)`
```python
# 指定归档内文件名
with tarfile.open("new.tar", "w") as tf:
    tf.add("data.txt", arcname="dir/data.txt")
```

**基本写法：addfile 写入**
`tf.addfile(<TarInfo>, <文件对象>)`
```python
# 手动构造 TarInfo 写入
import io

info = tarfile.TarInfo(name="hello.txt")
data = b"Hello, World!"
info.size = len(data)
with tarfile.open("new.tar", "w") as tf:
    tf.addfile(info, io.BytesIO(data))
```

---

## tarfile 模式

**基本写法：压缩模式**
`"w:gz"` | `"w:bz2"` | `"w:xz"`
```python
# 不同压缩格式
tarfile.open("a.tar.gz", "w:gz")
tarfile.open("a.tar.bz2", "w:bz2")
tarfile.open("a.tar.xz", "w:xz")
```

**基本写法：流式读取**
`"r|gz"`
```python
# 流式读取大文件
with tarfile.open("big.tar.gz", "r|gz") as tf:
    for member in tf:
        f = tf.extractfile(member)
        if f:
            print(f.read()[:50])
```

---

## TarInfo 对象

**基本写法：创建 TarInfo**
`tarfile.TarInfo(<名称>)`
```python
# 创建文件信息
info = tarfile.TarInfo("data.txt")
info.size = 100
info.mode = 0o644
```

**基本写法：从文件创建**
`tf.gettarinfo(<文件对象>)`
```python
# 从现有文件创建 TarInfo
with open("data.txt", "rb") as f:
    info = tf.gettarinfo(fileobj=f)
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
