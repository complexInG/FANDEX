---
order: 750
title: Python 网络编程 socket/http
module: 'python'
category: 后端技术
difficulty: beginner
description: Python 网络编程 socket/http 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## socket TCP 服务端

**基本写法：创建 TCP 服务端**
`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
```python
# 创建 IPv4 TCP 套接字并监听
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8080))
s.listen(5)
conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall(b"hello")
conn.close()
```

**基本写法：设置地址复用**
`<套接字>.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
```python
# 避免端口释放等待，立即重启绑定
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 8080))
```

**基本写法：并发接收连接**
`while True: <套接字>.accept()`
```python
# 循环接受多个客户端连接
while True:
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # 回显
    finally:
        conn.close()
```

**基本写法：设置超时**
`<套接字>.settimeout(<秒数>)`
```python
# 设置阻塞操作的超时时间
s.settimeout(5.0)
try:
    conn, addr = s.accept()
except socket.timeout:
    print("接受连接超时")
```

---

## socket TCP 客户端

**基本写法：创建 TCP 客户端**
`<套接字>.connect((<主机>, <端口>))`
```python
# 连接服务端并发送数据
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
s.sendall(b"ping")
response = s.recv(1024)
s.close()
```

**基本写法：发送字符串数据**
`<字符串>.encode(<编码>)`
```python
# 字符串转字节后发送
s.sendall("你好".encode("utf-8"))
response = s.recv(1024).decode("utf-8")
```

---

## socket UDP 通信

**基本写法：UDP 服务端**
`socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
```python
# UDP 无连接，直接接收数据报
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 8080))
data, addr = s.recvfrom(1024)
s.sendto(b"ack", addr)
```

**基本写法：UDP 客户端**
`<套接字>.sendto(<数据>, (<主机>, <端口>))`
```python
# UDP 发送无需建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"hello", ("127.0.0.1", 8080))
data, addr = s.recvfrom(1024)
```

---

## socketserver 模块

**基本写法：TCP 请求处理类**
`class <类>(socketserver.BaseRequestHandler):`
```python
# 继承 BaseRequestHandler 简化服务端
import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.request.sendall(data)

server = socketserver.TCPServer(("127.0.0.1", 8080), Handler)
server.serve_forever()
```

**基本写法：多线程服务端**
`socketserver.ThreadingTCPServer(<地址>, <处理器>)`
```python
# 每个连接独立线程处理
server = socketserver.ThreadingTCPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()
```

**基本写法：UDP 服务端**
`socketserver.UDPServer(<地址>, <处理器>)`
```python
# UDP 请求处理
class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        sock.sendto(b"ack", self.client_address)

server = socketserver.UDPServer(("127.0.0.1", 8080), UDPHandler)
```

---

## http.client 标准库客户端

**基本写法：HTTP GET 请求**
`http.client.HTTPSConnection(<主机>)`
```python
# 发起 HTTPS GET 请求
import http.client
conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status, resp.read().decode())
conn.close()
```

**基本写法：带请求头**
`conn.request(<方法>, <路径>, <请求体>, <头字典>)`
```python
# 携带自定义请求头
headers = {"Authorization": "Bearer token123"}
conn.request("GET", "/api", headers=headers)
```

**基本写法：HTTP POST 请求**
`conn.request("POST", <路径>, <请求体>)`
```python
# 发送 POST 请求体
import json
body = json.dumps({"name": "Tom"})
conn.request("POST", "/api", body, {"Content-Type": "application/json"})
```

---

## urllib.request 请求

**基本写法：发起 GET 请求**
`urllib.request.urlopen(<URL>)`
```python
# 最简方式打开 URL
from urllib.request import urlopen
resp = urlopen("https://www.example.com")
html = resp.read().decode("utf-8")
```

**基本写法：构造 Request 对象**
`urllib.request.Request(<URL>, headers=<头>)`
```python
# 自定义请求头
from urllib.request import Request, urlopen
req = Request("https://example.com", headers={"User-Agent": "MyApp"})
resp = urlopen(req)
```

**基本写法：POST 请求**
`urlopen(<Request>, data=<字节串>)`
```python
# 发送表单数据
from urllib.parse import urlencode
data = urlencode({"q": "python"}).encode()
resp = urlopen(Request("https://example.com", data=data))
```

---

## urllib.parse URL 处理

**基本写法：URL 编码**
`urllib.parse.urlencode(<字典>)`
```python
# 字典转查询字符串
from urllib.parse import urlencode
print(urlencode({"a": 1, "b": "中文"}))  # a=1&b=%E4%B8%AD%E6%96%87
```

**基本写法：解析 URL**
`urllib.parse.urlparse(<URL>)`
```python
# 拆解 URL 各部分
from urllib.parse import urlparse
r = urlparse("https://a.com/path?q=1#frag")
print(r.scheme, r.netloc, r.path)  # https a.com /path
```

**基本写法：拼接 URL**
`urllib.parse.urljoin(<基础URL>, <相对路径>)`
```python
# 基于基础 URL 拼接相对路径
from urllib.parse import urljoin
print(urljoin("https://a.com/dir/", "page.html"))  # https://a.com/dir/page.html
```

**基本写法：解析查询字符串**
`urllib.parse.parse_qs(<查询串>)`
```python
# 查询字符串转字典
from urllib.parse import parse_qs
print(parse_qs("a=1&b=2&b=3"))  # {'a': ['1'], 'b': ['2', '3']}
```

---

## urllib.error 异常处理

**基本写法：捕获 HTTP 错误**
`urllib.error.HTTPError`
```python
# 处理 HTTP 状态码错误
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
try:
    resp = urlopen("https://example.com/404")
except HTTPError as e:
    print(e.code, e.reason)  # 404 Not Found
except URLError as e:
    print(e.reason)
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
