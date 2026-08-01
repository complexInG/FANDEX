---
order: 41
title: 协程与asyncio
module: python
category: Python
difficulty: intermediate
description: 异步编程基础
author: fanquanpp
updated: '2026-08-01'
related:
  - python/并发编程
  - python/生成器与迭代器
  - python/Python与WebSocket
  - python/Python与FastAPI
prerequisites:
  - python/语法速查
---

# Python asyncio 异步编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事件循环

**基本写法：运行协程**
`asyncio.run(<协程>)`
```python
# 运行顶层协程并管理事件循环
async def main():
    print("hello")
asyncio.run(main())
```

**基本写法：获取当前事件循环**
`asyncio.get_event_loop()`
```python
# 获取当前运行的事件循环
loop = asyncio.get_event_loop()
```

**基本写法：获取运行中的事件循环**
`asyncio.get_running_loop()`
```python
# 在协程中获取当前运行的事件循环
loop = asyncio.get_running_loop()
```

**基本写法：设置事件循环策略**
`asyncio.set_event_loop_policy(<策略>)`
```python
# Windows 下使用 Selector 事件循环
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

---

### 异步上下文管理器

```python
import asyncio

class AsyncDatabaseConnection:
    """异步数据库连接"""

    async def __aenter__(self):
        print("连接数据库")
        await asyncio.sleep(0.1)  # 模拟异步连接
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        await asyncio.sleep(0.1)  # 模拟异步关闭

    async def query(self, sql):
        await asyncio.sleep(0.5)  # 模拟异步查询
        return f"查询结果: {sql}"

async def main():
    async with AsyncDatabaseConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(result)

asyncio.run(main())
```

### 异步迭代器

```python
import asyncio

class AsyncRange:
    """异步范围迭代器"""

    def __init__(self, count):
        self.count = count

    def __aiter__(self):
        self.current = 0
        return self

    async def __anext__(self):
        if self.current >= self.count:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)  # 模拟异步获取
        value = self.current
        self.current += 1
        return value

async def main():
    # 使用 async for 遍历异步迭代器
    async for i in AsyncRange(5):
        print(f"获取到: {i}")

asyncio.run(main())
```

## 什么是协程

协程是一种比线程更轻量的并发方式。线程由操作系统调度，切换开销大；协程由程序自身调度，切换开销极小。你可以创建成千上万个协程而不会耗尽系统资源。

Python 的 asyncio 模块提供了编写协程的基础设施。在 asyncio 中，你用 async def 定义协程函数，用 await 等待异步操作完成。当一个协程在等待（比如等待网络响应）时，事件循环会自动切换到其他协程执行，从而实现并发。

## 基础概念

### 同步与异步

同步代码是按顺序执行的：一行代码执行完才执行下一行。如果某行代码需要等待（如网络请求），整个程序都会停在那里。

异步代码在等待时会自动切换到其他任务。比如你发起一个网络请求，在等待响应的同时可以做其他事情，等响应到了再回来处理。这样就不会因为一个慢操作阻塞整个程序。

### async/await 语法

- async def：定义一个协程函数。调用协程函数不会立即执行，而是返回一个协程对象
- await：等待一个异步操作完成。await 只能在 async 函数中使用

### 协程与任务

- 协程（Coroutine）：async def 定义的函数的返回值，本身不会执行
- 任务（Task）：对协程的封装，由事件循环调度执行。使用 asyncio.create_task() 创建

## 快速上手

### 第一个协程

```python
import asyncio

# 定义协程函数
async def say_hello(name, delay):
    """延迟后打印问候"""
    print(f"开始等待 {name}...")
    # 异步等待（不会阻塞事件循环）
    await asyncio.sleep(delay)
    print(f"你好, {name}!")

# 运行协程
asyncio.run(say_hello("世界", 2))
```

### 并发执行多个协程

```python
import asyncio
import time

async def say_hello(name, delay):
    print(f"开始: {name}")
    await asyncio.sleep(delay)
    print(f"完成: {name}")
    return f"{name} 的结果"

async def main():
    start = time.time()

    # 并发执行三个协程
    results = await asyncio.gather(
        say_hello("任务A", 2),
        say_hello("任务B", 1),
        say_hello("任务C", 3),
    )

    duration = time.time() - start
    print(f"结果: {results}")
    print(f"总耗时: {duration:.1f} 秒")  # 约 3 秒，不是 6 秒

asyncio.run(main())
```

输出：

```
开始: 任务A
开始: 任务B
开始: 任务C
完成: 任务B
完成: 任务A
完成: 任务C
结果: ['任务A 的结果', '任务B 的结果', '任务C 的结果']
总耗时: 3.0 秒
```

三个任务并发执行，总耗时等于最慢的那个任务（3 秒），而不是所有任务时间之和（6 秒）。

## 详细用法

### 创建任务

```python
import asyncio

async def process_data(data):
    """处理数据"""
    await asyncio.sleep(1)
    return f"处理完成: {data}"

async def main():
    # 方式一：create_task 创建任务并立即开始执行
    task = asyncio.create_task(process_data("测试数据"))

    # 在任务执行的同时可以做其他事情
    print("任务已创建，可以做其他事...")

    # 等待任务完成并获取结果
    result = await task
    print(result)

    # 方式二：gather 同时等待多个任务
    results = await asyncio.gather(
        process_data("数据1"),
        process_data("数据2"),
        process_data("数据3"),
    )
    print(results)

asyncio.run(main())
```

### 任务取消

```python
import asyncio

async def long_task():
    """长时间运行的任务"""
    try:
        for i in range(10):
            print(f"进度: {i}/10")
            await asyncio.sleep(1)
        return "完成"
    except asyncio.CancelledError:
        print("任务被取消了")
        raise  # 重新抛出，让调用者知道任务被取消

async def main():
    task = asyncio.create_task(long_task())

    # 等 3 秒后取消任务
    await asyncio.sleep(3)
    task.cancel()

    try:
        result = await task
    except asyncio.CancelledError:
        print("主函数得知任务被取消")

asyncio.run(main())
```

### 超时控制

```python
import asyncio

async def slow_operation():
    """模拟慢操作"""
    await asyncio.sleep(10)
    return "完成"

async def main():
    # 方式一：wait_for 设置超时
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("操作超时")

    # 方式二：asyncio.timeout（Python 3.11+）
    async with asyncio.timeout(3):
        try:
            result = await slow_operation()
            print(result)
        except asyncio.TimeoutError:
            print("操作超时")

asyncio.run(main())
```

### 异步 HTTP 请求

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    """异步获取 URL 内容"""
    async with session.get(url) as response:
        return await response.text()

async def main():
    # 使用 aiohttp 进行异步 HTTP 请求
    async with aiohttp.ClientSession() as session:
        # 并发请求多个 URL
        urls = [
            "https://httpbin.org/get",
            "https://httpbin.org/ip",
            "https://httpbin.org/headers",
        ]
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for url, result in zip(urls, results):
            print(f"{url}: {len(result)} 字符")

# 需要先安装 aiohttp: pip install aiohttp
asyncio.run(main())
```

### 异步文件操作

```python
import asyncio
import aiofiles

async def read_file(path):
    """异步读取文件"""
    async with aiofiles.open(path, 'r', encoding='utf-8') as f:
        content = await f.read()
    return content

async def write_file(path, content):
    """异步写入文件"""
    async with aiofiles.open(path, 'w', encoding='utf-8') as f:
        await f.write(content)

# 需要先安装 aiofiles: pip install aiofiles
```

### asyncio.Queue

asyncio.Queue 是协程间通信的安全方式：

```python
import asyncio
import random

async def producer(queue, producer_id):
    """生产者：向队列中添加数据"""
    for i in range(5):
        item = f"产品-{producer_id}-{i}"
        await queue.put(item)
        print(f"生产者 {producer_id} 添加: {item}")
        await asyncio.sleep(random.uniform(0.1, 0.5))

async def consumer(queue, consumer_id):
    """消费者：从队列中取出数据"""
    while True:
        item = await queue.get()
        print(f"消费者 {consumer_id} 处理: {item}")
        await asyncio.sleep(random.uniform(0.2, 0.8))
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=10)

    # 启动生产者和消费者
    producers = [producer(queue, i) for i in range(2)]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(3)]

    # 等待所有生产者完成
    await asyncio.gather(*producers)

    # 等待队列中所有项目被处理
    await queue.join()

    # 取消消费者（它们在无限循环中）
    for c in consumers:
        c.cancel()

asyncio.run(main())
```

## 常见场景

### 异步 Web 爬虫

```python
import asyncio
import aiohttp
from time import time

async def fetch(session, url):
    """异步获取单个 URL"""
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
            return await resp.text()
    except Exception as e:
        return f"错误: {e}"

async def crawl(urls):
    """并发爬取多个 URL"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    urls = [f"https://httpbin.org/get?id={i}" for i in range(10)]

    start = time()
    results = await crawl(urls)
    duration = time() - start

    print(f"爬取 {len(urls)} 个页面，耗时 {duration:.2f} 秒")

asyncio.run(main())
```

### 异步数据库操作

```python
import asyncio

async def batch_insert(records):
    """批量异步插入数据"""
    tasks = [insert_record(record) for record in records]
    results = await asyncio.gather(*tasks)
    return results

async def insert_record(record):
    """异步插入单条记录"""
    # 模拟异步数据库操作
    await asyncio.sleep(0.01)
    return f"已插入: {record}"

async def main():
    records = [f"记录_{i}" for i in range(100)]
    results = await batch_insert(records)
    print(f"共插入 {len(results)} 条记录")

asyncio.run(main())
```

## 注意事项与常见错误

### 不要在协程中调用阻塞函数

在 async 函数中调用 time.sleep()、requests.get() 等同步阻塞函数会阻塞整个事件循环，其他协程都无法执行。应该使用对应的异步版本：

```python
import asyncio
import time

# 错误：使用同步的 time.sleep
async def bad_example():
    time.sleep(5)  # 阻塞整个事件循环 5 秒

# 正确：使用异步的 asyncio.sleep
async def good_example():
    await asyncio.sleep(5)  # 不阻塞事件循环
```

如果必须调用阻塞函数，使用 asyncio.to_thread 在线程中执行：

```python
import asyncio
import time

async def main():
    # 在线程中执行阻塞操作
    result = await asyncio.to_thread(time.sleep, 5)
```

### 忘记 await

调用协程函数时如果不加 await，协程不会执行：

```python
import asyncio

async def my_coroutine():
    print("这行会执行吗？")

async def main():
    # 错误：没有 await，协程不会执行
    my_coroutine()

    # 正确：使用 await
    await my_coroutine()

asyncio.run(main())
```

### asyncio.run 只能调用一次

asyncio.run() 会创建新的事件循环并运行。在已有事件循环运行时（如在 FastAPI 中），不能再调用 asyncio.run()。应该直接 await 协程或使用 asyncio.create_task()。

### gather 的错误处理

asyncio.gather 中某个任务抛出异常时，默认会取消其他任务。如果需要获取所有结果（包括异常），使用 return_exceptions=True：

```python
results = await asyncio.gather(
    task1(),
    task2(),
    task3(),
    return_exceptions=True  # 异常作为返回值，不会取消其他任务
)
```

## 进阶用法

### 使用 Semaphore 限制并发数

```python
import asyncio
import aiohttp

async def fetch_with_limit(session, url, semaphore):
    """带并发限制的请求"""
    async with semaphore:  # 获取信号量，超过限制则等待
        async with session.get(url) as resp:
            return await resp.text()

async def main():
    # 最多同时 5 个请求
    semaphore = asyncio.Semaphore(5)

    async with aiohttp.ClientSession() as session:
        urls = [f"https://httpbin.org/get?id={i}" for i in range(50)]
        tasks = [
            fetch_with_limit(session, url, semaphore)
            for url in urls
        ]
        results = await asyncio.gather(*tasks)
        print(f"完成 {len(results)} 个请求")

asyncio.run(main())
```

### 使用 as_completed 按完成顺序获取结果

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} 完成（耗时 {delay} 秒）"

async def main():
    tasks = [
        asyncio.create_task(task("A", 3)),
        asyncio.create_task(task("B", 1)),
        asyncio.create_task(task("C", 2)),
    ]

    # 按完成顺序获取结果（而不是按创建顺序）
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(result)

# 输出顺序：B -> C -> A

asyncio.run(main())
```

### 子进程管理

```python
import asyncio

async def run_command(cmd):
    """异步运行命令行命令"""
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await process.communicate()
    return {
        "returncode": process.returncode,
        "stdout": stdout.decode(),
        "stderr": stderr.decode(),
    }

async def main():
    result = await run_command(["python", "-c", "print('Hello')"])
    print(result["stdout"])  # Hello

asyncio.run(main())
```

### 在 FastAPI 中使用异步

FastAPI 原生支持 async/await，你可以直接在路由处理函数中使用：

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/slow")
async def slow_endpoint():
    """异步端点：等待时可以处理其他请求"""
    await asyncio.sleep(2)
    return {"message": "完成"}

@app.get("/fast")
async def fast_endpoint():
    return {"message": "立即返回"}
```
## 协程定义与调用

**基本写法：定义协程函数**
`async def <函数名>(<参数>): <语句>`
```python
# 使用 async def 定义协程
async def fetch_data(url):
    await asyncio.sleep(1)
    return {"data": "result"}
```

**基本写法：await 等待协程**
`await <协程>`
```python
# 在协程中等待另一个协程完成
async def main():
    result = await fetch_data("https://example.com")
    print(result)
```

**基本写法：await 多个协程顺序执行**
`await <协程1>; await <协程2>`
```python
# 依次等待两个协程
async def main():
    r1 = await fetch("url1")
    r2 = await fetch("url2")
```

---

## 任务管理

**基本写法：创建任务**
`asyncio.create_task(<协程>)`
```python
# 将协程封装为 Task 并调度执行
async def main():
    task = asyncio.create_task(fetch_data("url"))
    result = await task
```

**基本写法：并发运行多个协程**
`asyncio.gather(<协程1>, <协程2>)`
```python
# 并发执行多个协程，按顺序返回结果
async def main():
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
    )
```

**基本写法：gather 异常处理**
`asyncio.gather(<协程>, return_exceptions=True)`
```python
# 异常作为返回值而非抛出
async def main():
    results = await asyncio.gather(
        fetch("url1"),
        fetch("bad_url"),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print("失败:", r)
```

**基本写法：Go 1.0 风格任务组**
`async with asyncio.TaskGroup() as <组>:`
```python
# Python 3.11+ 结构化并发，任一任务异常则全部取消
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch("url1"))
        t2 = tg.create_task(fetch("url2"))
    # 退出 with 块时所有任务已完成
    print(t1.result(), t2.result())
```

---

## 等待与超时

**基本写法：等待第一个完成**
`asyncio.wait_for(<协程>, <超时>)`
```python
# 设置超时，超时抛出 TimeoutError
async def main():
    try:
        result = await asyncio.wait_for(fetch("url"), timeout=5.0)
    except asyncio.TimeoutError:
        print("超时")
```

**基本写法：Python 3.11+ asyncio.timeout**
`async with asyncio.timeout(<秒>):`
```python
# Python 3.11+ 超时上下文管理器
async def main():
    try:
        async with asyncio.timeout(5.0):
            result = await fetch("url")
    except TimeoutError:
        print("超时")
```

**基本写法：等待首个完成**
`asyncio.as_completed(<协程列表>)`
```python
# 按完成顺序获取结果
async def main():
    tasks = [fetch(f"url{i}") for i in range(3)]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print("完成:", result)
```

**基本写法：wait 返回两组任务**
`done, pending = await asyncio.wait(<任务集>)`
```python
# 返回已完成和未完成两组任务
async def main():
    tasks = [asyncio.create_task(fetch(f"url{i}")) for i in range(3)]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )
```

---

## 休眠

**基本写法：异步休眠**
`await asyncio.sleep(<秒>)`
```python
# 非阻塞休眠，让出控制权
async def main():
    await asyncio.sleep(1.0)
    print("1秒后")
```

---

## 队列

**基本写法：异步队列**
`asyncio.Queue()`
```python
# 协程间安全传递数据
async def producer(q):
    await q.put("item")
async def consumer(q):
    item = await q.get()
async def main():
    q = asyncio.Queue(maxsize=10)
    await asyncio.gather(producer(q), consumer(q))
```

**基本写法：带缓冲的队列**
`asyncio.Queue(maxsize=<大小>)`
```python
# 设置最大容量，满时 put 阻塞
q = asyncio.Queue(maxsize=5)
await q.put("data")
item = await q.get()
q.task_done()
await q.join()
```

---

## 锁与信号量

**基本写法：异步锁**
`asyncio.Lock()`
```python
# 协程间互斥锁
lock = asyncio.Lock()
async def safe_update():
    async with lock:
        shared_resource += 1
```

**基本写法：信号量**
`asyncio.Semaphore(<数量>)`
```python
# 限制并发数量
sem = asyncio.Semaphore(5)
async def limited_fetch(url):
    async with sem:
        return await fetch(url)
```

**基本写法：事件**
`asyncio.Event()`
```python
# 协程间事件通知
event = asyncio.Event()
async def waiter():
    await event.wait()
    print("收到信号")
async def setter():
    await asyncio.sleep(1)
    event.set()
```

---

## 异步生成器

**基本写法：定义异步生成器**
`async def <函数名>(): yield <值>`
```python
# 异步生成器函数
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i
```

**基本写法：遍历异步生成器**
`async for <变量> in <异步可迭代>:`
```python
# 异步迭代
async def main():
    async for num in async_range(5):
        print(num)
```

---

## Python 3.13+ asyncio 增强

**基本写法：Python 3.13+ asyncio.Runner**
`asyncio.Runner()`
```python
# Python 3.13+ Runner 上下文管理复用事件循环
with asyncio.Runner() as runner:
    r1 = runner.run(fetch("url1"))
    r2 = runner.run(fetch("url2"))
```

**基本写法：Python 3.13+ eager_task_factory**
`loop.set_task_factory(asyncio.eager_task_factory)`
```python
# Python 3.13+ 协程立即开始执行而非延迟调度
async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(asyncio.eager_task_factory)
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
| 协程与asyncio | 006-CoroutineAsyncio | 本文自身 |
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
| Python gc inspect dis | 094-GcInspect | 本文的并列主题 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
