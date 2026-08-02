---
order: 870
title: Python http.client HTTP 客户端
module: python

category: '040-python'
difficulty: beginner
description: Python http.client HTTP 客户端 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## HTTPConnection

**基本写法：创建连接**
`http.client.HTTPConnection(<主机>, <端口>)`
```python
# 创建 HTTP 连接
import http.client

conn = http.client.HTTPConnection("example.com", 80)
```

**基本写法：HTTPS 连接**
`http.client.HTTPSConnection(<主机>, <端口>)`
```python
# 创建 HTTPS 连接
import ssl

ctx = ssl.create_default_context()
conn = http.client.HTTPSConnection("www.python.org", 443, context=ctx)
```

**基本写法：发起请求**
`conn.request(<方法>, <路径>, <数据>, <头>)`
```python
# 发起 GET 请求
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status, resp.reason)
print(resp.read().decode()[:100])
```

**基本写法：POST 请求**
`conn.request("POST", <路径>, <数据>, <头>)`
```python
# 发起 POST 请求
import json
body = json.dumps({"name": "Alice"}).encode()
headers = {"Content-Type": "application/json"}
conn.request("POST", "/api/users", body, headers)
resp = conn.getresponse()
```

---

## HTTPResponse 响应对象

**基本写法：获取响应**
`conn.getresponse()`
```python
# 获取响应对象
resp = conn.getresponse()
```

**基本写法：状态码**
`resp.status` | `resp.reason`
```python
# 状态码与原因短语
print(resp.status)    # 200
print(resp.reason)    # OK
```

**基本写法：读取响应体**
`resp.read()` | `resp.read(<长度>)`
```python
# 读取全部或部分响应体
data = resp.read()
chunk = resp.read(1024)
```

**基本写法：获取响应头**
`resp.getheader(<名称>)` | `resp.getheaders()`
```python
# 获取响应头
print(resp.getheader("Content-Type"))
print(resp.getheaders())
```

**基本写法：流式读取**
`for line in resp:`
```python
# 逐行迭代响应体
for line in resp:
    print(line)
```

---

## 请求方法

**基本写法：PUT/DELETE/PATCH**
`conn.request(<方法>, <路径>)`
```python
# 各种 HTTP 方法
conn.request("PUT", "/item/1", body)
conn.request("DELETE", "/item/1")
conn.request("PATCH", "/item/1", body)
```

**基本写法：HEAD 请求**
`conn.request("HEAD", <路径>)`
```python
# HEAD 只获取头
conn.request("HEAD", "/")
resp = conn.getresponse()
print(resp.getheader("Content-Length"))
```

---

## 请求头

**基本写法：自定义请求头**
`conn.request(<方法>, <路径>, <数据>, <头字典>)`
```python
# 携带自定义头
headers = {
    "User-Agent": "MyClient/1.0",
    "Authorization": "Bearer token123",
}
conn.request("GET", "/", headers=headers)
```

**基本写法：添加 Cookie**
`headers["Cookie"] = <字符串>`
```python
# 携带 Cookie
headers = {"Cookie": "session=abc123"}
conn.request("GET", "/", headers=headers)
```

---

## 连接管理

**基本写法：关闭连接**
`conn.close()`
```python
# 关闭连接
conn.close()
```

**基本写法：set_tunnel 代理隧道**
`conn.set_tunnel(<代理主机>, <代理端口>)`
```python
# 通过代理建立隧道
conn = http.client.HTTPSConnection("example.com")
conn.set_tunnel("proxy.local", 8080)
conn.request("GET", "/")
```

**基本写法：connect 手动连接**
`conn.connect()`
```python
# 手动建立连接
conn.connect()
```

---

## 超时与异常

**基本写法：设置超时**
`HTTPConnection(<主机>, <端口>, timeout=<秒>)`
```python
# 连接超时
conn = http.client.HTTPConnection("example.com", timeout=10)
```

**基本写法：捕获异常**
`except http.client.HTTPException:`
```python
# http.client 异常基类
try:
    conn.request("GET", "/")
except http.client.HTTPException as e:
    print("HTTP 异常:", e)
except ConnectionError as e:
    print("连接错误:", e)
```

**基本写法：常见异常类型**
`http.client.HTTPException`
```python
# 异常层级
# HTTPException
#   ├── ProtocolError
#   ├── ResponseNotReady
#   ├── BadStatusLine
#   ├── ImproperConnectionState
#   └── CannotSendRequest
```

---

## HTTPMessage 消息对象

**基本写法：响应头为 email.message.Message**
`type(resp.headers)`
```python
# headers 是 email.message.Message 子类
print(type(resp.headers))
print(resp.headers["Content-Type"])
```

**基本写法：items 遍历头**
`resp.headers.items()`
```python
# 遍历所有头
for key, value in resp.headers.items():
    print(key, value)
```

---

## 持续连接与流水线

**基本写法：复用连接**
`conn.request(...)` 多次
```python
# 同一连接发多个请求
conn = http.client.HTTPConnection("example.com")
conn.request("GET", "/a")
r1 = conn.getresponse()
r1.read()
conn.request("GET", "/b")
r2 = conn.getresponse()
r2.read()
conn.close()
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
