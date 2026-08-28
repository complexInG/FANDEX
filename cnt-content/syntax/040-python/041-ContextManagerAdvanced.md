# Python 上下文管理器进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 自定义上下文管理器

**基本写法：实现 __enter__/__exit__**
`class <类>:\n    def __enter__(self): ...\n    def __exit__(self, exc_type, exc, tb):`
```python
# 经典上下文管理器实现
class FileOpener:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        self.f = open(self.path, "r")
        return self.f
    def __exit__(self, exc_type, exc, tb):
        self.f.close()
        return False

with FileOpener("data.txt") as f:
    print(f.read())
```

**基本写法：抑制异常**
`def __exit__(self, exc_type, exc, tb): return True`
```python
# 返回 True 抑制 with 块内的异常
class Suppressor:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type is ValueError:
            return True
        return False

with Suppressor():
    raise ValueError("被抑制")
```

---

## contextlib.contextmanager

**基本写法：装饰器生成上下文管理器**
`@contextlib.contextmanager`
```python
# 用生成器函数简化上下文管理器
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("标题")
```

**基本写法：带返回值**
`yield <值>`
```python
# yield 的值会绑定到 as 变量
@contextmanager
def open_db(url):
    conn = connect(url)
    try:
        yield conn
    finally:
        conn.close()

with open_db("sqlite://") as db:
    db.execute("SELECT 1")
```

**基本写法：处理异常**
`try: yield\nexcept <异常> as e:`
```python
# 在生成器中捕获异常
@contextmanager
def safe_op():
    try:
        yield
    except ValueError as e:
        print(f"捕获 {e}")
```

---

## contextlib 工具

**基本写法：closing 包装关闭**
`contextlib.closing(<对象>)`
```python
# 为只有 close 方法的对象提供上下文
from contextlib import closing
import urllib.request

with closing(urllib.request.urlopen("http://example.com")) as r:
    print(r.read()[:50])
```

**基本写法：suppress 抑制异常**
`contextlib.suppress(<异常类>)`
```python
# 抑制指定异常
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("nonexistent.txt")
```

**基本写法：redirect_stdout 重定向**
`contextlib.redirect_stdout(<目标>)`
```python
# 重定向标准输出
from contextlib import redirect_stdout
import io

buf = io.StringIO()
with redirect_stdout(buf):
    print("捕获这行")
print(buf.getvalue())
```

**基本写法：redirect_stderr 重定向**
`contextlib.redirect_stderr(<目标>)`
```python
# 重定向标准错误
import io
buf = io.StringIO()
with redirect_stderr(buf):
    import warnings
    warnings.warn("警告")
```

---

## ExitStack 动态管理

**基本写法：ExitStack 动态管理**
`contextlib.ExitStack()`
```python
# 动态管理多个上下文
from contextlib import ExitStack

files = []
with ExitStack() as stack:
    for name in ["a.txt", "b.txt"]:
        files.append(stack.enter_context(open(name)))
```

**基本写法：enter_context 进入上下文**
`stack.enter_context(<上下文管理器>)`
```python
# 动态添加上下文管理器
with ExitStack() as stack:
    f1 = stack.enter_context(open("a.txt"))
    f2 = stack.enter_context(open("b.txt"))
    stack.callback(lambda: print("清理"))
```

**基本写法：callback 注册清理回调**
`stack.callback(<函数>, *<参数>)`
```python
# 注册退出时回调
with ExitStack() as stack:
    stack.callback(print, "退出时调用")
    print("执行中")
```

**基本写法：push 推入清理函数**
`stack.push(<退出函数>)`
```python
# 推入任意退出函数
def cleanup():
    print("清理完成")
with ExitStack() as stack:
    stack.push(cleanup)
```

---

## 异步上下文管理器

**基本写法：实现 __aenter__/__aexit__**
`class <类>:\n    async def __aenter__(self): ...\n    async def __aexit__(self, exc_type, exc, tb):`
```python
# 异步上下文管理器
class AsyncConn:
    async def __aenter__(self):
        await self.connect()
        return self
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()
        return False
    async def connect(self): pass
    async def close(self): pass

async def main():
    async with AsyncConn() as conn:
        pass
```

**基本写法：asynccontextmanager 装饰器**
`@contextlib.asynccontextmanager`
```python
# 异步上下文管理器装饰器
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def timer():
    start = asyncio.get_event_loop().time()
    yield
    print(f"耗时 {asyncio.get_event_loop().time() - start}")

async def main():
    async with timer():
        await asyncio.sleep(0.5)
```

---

## AsyncExitStack

**基本写法：异步动态管理**
`contextlib.AsyncExitStack()`
```python
# 异步动态管理多个上下文
from contextlib import AsyncExitStack

async def main():
    async with AsyncExitStack() as stack:
        c1 = await stack.enter_async_context(AsyncConn())
        c2 = await stack.enter_async_context(AsyncConn())
```

**基本写法：push_async_callback**
`stack.push_async_callback(<协程函数>)`
```python
# 注册异步清理回调
async def main():
    async with AsyncExitStack() as stack:
        stack.push_async_callback(asyncio.sleep, 0)
```

---

## 多上下文嵌套

**基本写法：多上下文嵌套**
`with <ctx1> as <a>, <ctx2> as <b>:`
```python
# 多上下文同时管理
with open("a") as fa, open("b") as fb:
    pass
```

**基本写法：括号换行**
`with (<ctx1> as <a>,\n      <ctx2> as <b>):`
```python
# 3.10+ 支持括号内换行
with (
    open("a") as fa,
    open("b") as fb,
):
    pass
```
