---
order: 960
title: Python httpx 与 requests
module: python

category: '040-python'
difficulty: beginner
description: Python httpx 与 requests 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## httpx 客户端

**基本写法：创建客户端**
`httpx.Client()`
```python
# 同步客户端
import httpx

with httpx.Client() as client:
    resp = client.get("https://www.python.org")
```

**基本写法：AsyncClient**
`httpx.AsyncClient()`
```python
# 异步客户端
async with httpx.AsyncClient() as client:
    resp = await client.get("https://www.python.org")
```

**基本写法：get 请求**
`client.get(<URL>)`
```python
# GET 请求
resp = httpx.get("https://www.python.org")
print(resp.status_code)
```

**基本写法：post 请求**
`client.post(<URL>, json=<数据>)`
```python
# POST JSON
resp = httpx.post("https://httpbin.org/post", json={"name": "Alice"})
```

---

## httpx 响应

**基本写法：状态码**
`resp.status_code`
```python
# 状态码
print(resp.status_code)
```

**基本写法：响应文本**
`resp.text`
```python
# 文本内容
print(resp.text[:100])
```

**基本写法：响应 JSON**
`resp.json()`
```python
# JSON 内容
data = resp.json()
```

**基本写法：响应字节**
`resp.content`
```python
# 字节内容
print(resp.content[:50])
```

**基本写法：响应头**
`resp.headers`
```python
# 响应头
print(resp.headers["content-type"])
```

---

## httpx 请求配置

**基本写法：超时**
`httpx.Timeout(<秒>)` | `timeout=<秒>`
```python
# 超时配置
client = httpx.Client(timeout=10.0)
client = httpx.Client(timeout=httpx.Timeout(5.0, connect=2.0))
```

**基本写法：headers**
`client.headers[<键>] = <值>`
```python
# 默认请求头
client = httpx.Client(headers={"User-Agent": "MyClient/1.0"})
```

**基本写法：auth 认证**
`httpx.BasicAuth(<用户>, <密码>)`
```python
# 基本认证
client = httpx.Client(auth=httpx.BasicAuth("user", "pass"))
```

**基本写法：proxy 代理**
`httpx.Client(proxy=<URL>)`
```python
# 代理设置
client = httpx.Client(proxy="http://proxy:8080")
```

**基本写法：params 查询参数**
`client.get(<URL>, params=<字典>)`
```python
# 查询参数
resp = client.get("https://httpbin.org/get", params={"q": "python", "page": 1})
```

---

## httpx 会话管理

**基本写法：with 自动关闭**
`with httpx.Client() as client:`
```python
# 自动管理连接
with httpx.Client(base_url="https://api.example.com") as client:
    r1 = client.get("/users")
    r2 = client.get("/posts")
```

**基本写法：base_url 基础 URL**
`httpx.Client(base_url=<URL>)`
```python
# 基础 URL
client = httpx.Client(base_url="https://api.example.com")
r = client.get("/users")
```

---

## httpx 流式响应

**基本写法：stream 流式读取**
`with client.stream("GET", <URL>) as resp:`
```python
# 流式响应
with httpx.stream("GET", "https://example.com/big") as resp:
    for chunk in resp.iter_bytes(chunk_size=1024):
        print(len(chunk))
```

**基本写法：iter_lines**
`for line in resp.iter_lines():`
```python
# 按行迭代
with client.stream("GET", url) as resp:
    for line in resp.iter_lines():
        print(line)
```

---

## requests 库

**基本写法：get 请求**
`requests.get(<URL>, params=<字典>)`
```python
# requests GET
import requests

resp = requests.get("https://www.python.org", params={"q": "python"})
print(resp.status_code)
```

**基本写法：post 请求**
`requests.post(<URL>, data=<数据>, json=<JSON>)`
```python
# POST 表单与 JSON
r = requests.post(url, data={"key": "value"})
r = requests.post(url, json={"name": "Alice"})
```

**基本写法：自定义 headers**
`requests.get(<URL>, headers=<字典>)`
```python
# 自定义头
r = requests.get(url, headers={"User-Agent": "MyClient/1.0"})
```

**基本写法：timeout 超时**
`requests.get(<URL>, timeout=<秒>)`
```python
# 超时设置
r = requests.get(url, timeout=10)
```

---

## requests Session 会话

**基本写法：Session 复用连接**
`requests.Session()`
```python
# Session 保持 Cookie 与连接
s = requests.Session()
s.headers.update({"Authorization": "Bearer token"})
r1 = s.get(url)
r2 = s.get(url)
s.close()
```

**基本写法：with 自动关闭**
`with requests.Session() as s:`
```python
# 自动关闭会话
with requests.Session() as s:
    r = s.get(url)
```

---

## requests 响应

**基本写法：响应内容**
`r.text` | `r.json()` | `r.content`
```python
# 响应内容
print(r.text)
print(r.json())
print(r.content)
```

**基本写法：状态检查**
`r.raise_for_status()`
```python
# 状态码非 2xx 抛出异常
r = requests.get(url)
r.raise_for_status()
```

**基本写法：响应头**
`r.headers`
```python
# 响应头
print(r.headers["Content-Type"])
```

**基本写法：cookies**
`r.cookies`
```python
# 响应 Cookie
print(r.cookies.get("session"))
```

---

## requests 认证

**基本写法：basic auth**
`requests.auth.HTTPBasicAuth(<用户>, <密码>)`
```python
# 基本认证
from requests.auth import HTTPBasicAuth

r = requests.get(url, auth=HTTPBasicAuth("user", "pass"))
```

**基本写法：bearer token**
`headers={"Authorization": "Bearer <token>"}`
```python
# Bearer Token
r = requests.get(url, headers={"Authorization": "Bearer abc123"})
```

---

## requests 异常处理

**基本写法：捕获异常**
`except requests.RequestException:`
```python
# requests 异常基类
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
except requests.Timeout:
    print("超时")
except requests.HTTPError as e:
    print("HTTP 错误:", e)
except requests.RequestException as e:
    print("请求异常:", e)
```

---

## 文件上传与下载

**基本写法：上传文件**
`requests.post(<URL>, files={<字段>: <文件>})`
```python
# multipart 上传
with open("data.txt", "rb") as f:
    r = requests.post(url, files={"file": f})
```

**基本写法：下载文件**
`with open(<路径>, "wb") as f:\n    f.write(r.content)`
```python
# 下载二进制
r = requests.get(url)
with open("image.png", "wb") as f:
    f.write(r.content)
```

**基本写法：流式下载**
`requests.get(<URL>, stream=True)`
```python
# 大文件流式下载
r = requests.get(url, stream=True)
with open("big.zip", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
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
