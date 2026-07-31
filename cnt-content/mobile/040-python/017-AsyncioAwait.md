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

## 异步上下文管理器

**换行写法：定义异步上下文管理器**
`class <类名>:`
`    async def __aenter__(self): <语句>`
`    async def __aexit__(self, *args): <语句>`

```python
# 异步上下文管理器
class AsyncDB:
    async def __aenter__(self):
        self.conn = await connect()
        return self
    async def __aexit__(self, *args):
        await self.conn.close()
```

**基本写法：使用异步上下文管理器**
`async with <对象> as <变量>:`
```python
# 使用 async with
async def main():
    async with AsyncDB() as db:
        await db.query("SELECT 1")
```

---

## 异步迭代器

**换行写法：定义异步迭代器**
`class <类名>:`
`    def __aiter__(self): return self`
`    async def __anext__(self): <语句>`

```python
# 实现异步迭代器协议
class AsyncCounter:
    def __init__(self, stop):
        self.i = 0
        self.stop = stop
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.i >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.i += 1
        return self.i
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
