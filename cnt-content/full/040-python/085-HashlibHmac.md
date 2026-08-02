---
order: 850
title: Python hashlib 与 hmac
module: 'python'
category: 后端技术
difficulty: beginner
description: Python hashlib 与 hmac 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## hashlib 哈希

**基本写法：创建哈希对象**
`hashlib.<算法名>()`
```python
# 创建 SHA256 哈希对象
import hashlib

h = hashlib.sha256()
h.update(b"hello")
print(h.hexdigest())
```

**基本写法：直接计算哈希**
`hashlib.<算法名>(<字节>)`
```python
# 一步计算哈希值
h = hashlib.sha256(b"hello")
print(h.hexdigest())
```

**基本写法：update 分块更新**
`h.update(<字节>)`
```python
# 分块更新大文件哈希
h = hashlib.sha256()
with open("big.bin", "rb") as f:
    while chunk := f.read(8192):
        h.update(chunk)
print(h.hexdigest())
```

**基本写法：hexdigest 十六进制**
`h.hexdigest()`
```python
# 返回十六进制字符串
print(hashlib.sha256(b"x").hexdigest())
```

**基本写法：digest 字节**
`h.digest()`
```python
# 返回原始字节摘要
print(hashlib.sha256(b"x").digest())
```

---

## 常用算法

**基本写法：md5**
`hashlib.md5(<字节>)`
```python
# MD5（不推荐用于安全场景）
print(hashlib.md5(b"hello").hexdigest())
```

**基本写法：sha1**
`hashlib.sha1(<字节>)`
```python
# SHA1
print(hashlib.sha1(b"hello").hexdigest())
```

**基本写法：sha256 / sha512**
`hashlib.sha256(<字节>)` | `hashlib.sha512(<字节>)`
```python
# SHA256 与 SHA512
print(hashlib.sha256(b"hello").hexdigest())
print(hashlib.sha512(b"hello").hexdigest())
```

**基本写法：sha3_256（3.6+）**
`hashlib.sha3_256(<字节>)`
```python
# SHA3 系列
print(hashlib.sha3_256(b"hello").hexdigest())
```

**基本写法：blake2**
`hashlib.blake2b(<字节>)` | `hashlib.blake2s(<字节>)`
```python
# BLAKE2 哈希
print(hashlib.blake2b(b"hello").hexdigest())
print(hashlib.blake2s(b"hello").hexdigest())
```

**基本写法：查询可用算法**
`hashlib.algorithms_available`
```python
# 当前实现可用的算法集合
print(hashlib.algorithms_available)
```

**基本写法：保证可用算法**
`hashlib.algorithms_guaranteed`
```python
# 所有平台保证可用的算法
print(hashlib.algorithms_guaranteed)
```

---

## HMAC 消息认证

**基本写法：创建 HMAC**
`hmac.new(<密钥>, <消息>, <哈希算法>)`
```python
# 创建 HMAC
import hmac
import hashlib

m = hmac.new(b"secret_key", b"hello", hashlib.sha256)
print(m.hexdigest())
```

**基本写法：update 更新消息**
`m.update(<字节>)`
```python
# 分块更新 HMAC
m = hmac.new(b"key", b"", hashlib.sha256)
m.update(b"hello")
m.update(b"world")
print(m.hexdigest())
```

**基本写法：compare_digest 安全比较**
`hmac.compare_digest(<a>, <b>)`
```python
# 常量时间比较，防止时序攻击
a = hmac.new(b"key", b"msg", hashlib.sha256).digest()
b = hmac.new(b"key", b"msg", hashlib.sha256).digest()
print(hmac.compare_digest(a, b))
```

**基本写法：digest 字节**
`m.digest()`
```python
# 返回字节摘要
print(m.digest())
```

---

## secrets 安全随机

**基本写法：生成安全随机字节**
`secrets.token_bytes(<长度>)`
```python
# 生成加密安全的随机字节
import secrets

print(secrets.token_bytes(16))
```

**基本写法：生成安全随机字符串**
`secrets.token_hex(<长度>)`
```python
# 生成十六进制随机字符串
print(secrets.token_hex(16))
```

**基本写法：生成 URL 安全字符串**
`secrets.token_urlsafe(<长度>)`
```python
# 生成 URL 安全的随机字符串
print(secrets.token_urlsafe(16))
```

**基本写法：安全随机整数**
`secrets.randbelow(<上界>)`
```python
# 生成 0 到 n-1 的安全随机整数
print(secrets.randbelow(100))
```

**基本写法：安全选择**
`secrets.choice(<序列>)`
```python
# 从序列中安全随机选择
print(secrets.choice("abcdef"))
```

**基本写法：生成口令**
`secrets.choice` 配合 string
```python
# 生成 16 位随机口令
import string
alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for _ in range(16))
print(password)
```

---

## 文件哈希校验

**基本写法：文件 SHA256**
`def <函数>(<路径>):`
```python
# 计算文件 SHA256
def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()
```

---

## 密码哈希（推荐）

**基本写法：pbkdf2_hmac**
`hashlib.pbkdf2_hmac(<算法>, <密码>, <盐>, <迭代次数>)`
```python
# PBKDF2 密码哈希
salt = os.urandom(16)
key = hashlib.pbkdf2_hmac("sha256", b"password", salt, 100000)
print(key.hex())
```

**基本写法：scrypt（3.6+）**
`hashlib.scrypt(<密码>, salt=<盐>, n=<参数>, r=<参数>, p=<参数>)`
```python
# scrypt 密码哈希
salt = os.urandom(16)
key = hashlib.scrypt(b"password", salt=salt, n=16384, r=8, p=1)
print(key.hex())
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
