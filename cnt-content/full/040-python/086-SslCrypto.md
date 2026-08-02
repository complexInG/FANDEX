---
order: 860
title: Python ssl 安全套接字
module: 'python'
category: 后端技术
difficulty: beginner
description: Python ssl 安全套接字 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## SSLContext 上下文

**基本写法：创建默认上下文**
`ssl.create_default_context(<用途>)`
```python
# 创建默认 SSL 上下文
import ssl

ctx = ssl.create_default_context()  # 服务端验证
ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)  # 服务端
```

**基本写法：创建基础上下文**
`ssl.SSLContext(<协议>)`
```python
# 手动创建上下文
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
```

**基本写法：加载证书**
`ctx.load_cert_chain(<证书>, keyfile=<密钥>)`
```python
# 加载服务器证书与私钥
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("server.crt", keyfile="server.key")
```

**基本写法：加载 CA 证书**
`ctx.load_verify_locations(<CA 文件>)`
```python
# 加载 CA 证书用于验证
ctx = ssl.create_default_context()
ctx.load_verify_locations("ca-bundle.crt")
```

---

## 客户端配置

**基本写法：禁用主机名检查**
`ctx.check_hostname = False`
```python
# 关闭主机名校验（不推荐）
ctx = ssl.create_default_context()
ctx.check_hostname = False
```

**基本写法：调整验证模式**
`ctx.verify_mode = ssl.CERT_NONE`
```python
# 关闭证书验证（不推荐）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
```

**基本写法：设置最低 TLS 版本**
`ctx.minimum_version = ssl.TLSVersion.TLSv1_2`
```python
# 设置最低 TLS 版本
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
```

---

## 包装套接字

**基本写法：包装客户端套接字**
`ctx.wrap_socket(<套接字>, server_hostname=<主机>)`
```python
# 客户端包装 socket
import socket
import ssl

ctx = ssl.create_default_context()
sock = socket.create_connection(("www.python.org", 443))
ssock = ctx.wrap_socket(sock, server_hostname="www.python.org")
ssock.send(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
print(ssock.recv(1024)[:50])
ssock.close()
```

**基本写法：包装服务端套接字**
`ctx.wrap_socket(<套接字>, server_side=True)`
```python
# 服务端包装 socket
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("server.crt", keyfile="server.key")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 8443))
sock.listen()
ssock, addr = ctx.wrap_socket(sock, server_side=True)
```

---

## 证书信息

**基本写法：获取对端证书**
`ssock.getpeercert()`
```python
# 获取对端证书字典
cert = ssock.getpeercert()
print(cert["subject"])
```

**基本写法：获取证书二进制**
`ssock.getpeercert(binary_form=True)`
```python
# 获取 DER 编码的证书
der = ssock.getpeercert(binary_form=True)
print(len(der))
```

**基本写法：cipher 信息**
`ssock.cipher()`
```python
# 获取当前使用的加密套件
print(ssock.cipher())
```

**基本写法：协议版本**
`ssock.version()`
```python
# 获取协商的 TLS 版本
print(ssock.version())
```

---

## 证书校验回调

**基本写法：设置回调**
`ctx.set_servername_callback(<函数>)`
```python
# 服务端根据 SNI 选择证书
def sni_callback(sslsocket, sni_name, ssl_context):
    if sni_name == "example.com":
        ssl_context.load_cert_chain("example.crt", "example.key")

ctx.set_servername_callback(sni_callback)
```

---

## 证书与 PKCS

**基本写法：DER 转 PEM**
`ssl.DER_cert_to_PEM_cert(<DER 字节>)`
```python
# DER 转 PEM 字符串
pem = ssl.DER_cert_to_PEM_cert(der_bytes)
```

**基本写法：PEM 转 DER**
`ssl.PEM_cert_to_DER_cert(<PEM 字符串>)`
```python
# PEM 转 DER 字节
der = ssl.PEM_cert_to_DER_cert(pem_string)
```

---

## OCSP 与 CRL

**基本写法：加载 CRL**
`ctx.load_verify_locations(cafile=<文件>)`
```python
# 加载证书吊销列表
ctx = ssl.create_default_context()
ctx.load_verify_locations(cafile="crl.pem")
ctx.verify_flags |= ssl.VERIFY_CRL_CHECK_LEAF
```

**基本写法：3.13 默认严格标志**
`ctx.verify_flags`
```python
# Python 3.13 默认启用 VERIFY_X509_STRICT 等
ctx = ssl.create_default_context()
print(ctx.verify_flags)
```

---

## 常量与枚举

**基本写法：TLSVersion**
`ssl.TLSVersion.TLSv1_2` | `ssl.TLSVersion.TLSv1_3`
```python
# TLS 版本常量
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
ctx.maximum_version = ssl.TLSVersion.TLSv1_3
```

**基本写法：CERT_* 验证模式**
`ssl.CERT_NONE` | `ssl.CERT_OPTIONAL` | `ssl.CERT_REQUIRED`
```python
# 证书验证模式
ctx.verify_mode = ssl.CERT_REQUIRED
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
