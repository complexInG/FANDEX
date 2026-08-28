# Python asyncio 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Task 任务

**基本写法：创建 Task**
`asyncio.create_task(<协程>)`
```python
# 调度协程为 Task
import asyncio

async def fetch(url):
    await asyncio.sleep(1)
    return f"data from {url}"

async def main():
    task = asyncio.create_task(fetch("https://x"))
    result = await task
    print(result)

asyncio.run(main())
```

**基本写法：TaskGroup（3.11+）**
`async with asyncio.TaskGroup() as tg:`
```python
# 结构化并发
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch("a"))
        t2 = tg.create_task(fetch("b"))
    print(t1.result(), t2.result())
```

**基本写法：gather 并发**
`asyncio.gather(*<协程>)`
```python
# 并发运行多个协程
async def main():
    results = await asyncio.gather(
        fetch("a"), fetch("b"), fetch("c")
    )
    print(results)
```

**基本写法：gather 异常处理**
`asyncio.gather(*<协程>, return_exceptions=True)`
```python
# 异常作为结果返回
results = await asyncio.gather(
    fetch("a"), fetch("b"), return_exceptions=True
)
for r in results:
    if isinstance(r, Exception):
        print("错误:", r)
```

---

## wait 等待

**基本写法：wait 等待**
`asyncio.wait(<Task 集合>)`
```python
# 等待任务完成
tasks = [asyncio.create_task(fetch(i)) for i in range(3)]
done, pending = await asyncio.wait(tasks)
```

**基本写法：指定 return_when**
`asyncio.wait(<集合>, return_when=<常量>)`
```python
# 首个完成即返回
from asyncio import FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED

done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)
```

**基本写法：wait_for 超时**
`asyncio.wait_for(<协程>, timeout=<秒>)`
```python
# 等待协程完成，超时取消
try:
    result = await asyncio.wait_for(fetch("a"), timeout=2.0)
except asyncio.TimeoutError:
    print("超时")
```

**基本写法：as_completed 按完成迭代**
`asyncio.as_completed(<协程列表>)`
```python
# 按完成顺序迭代
coros = [fetch(i) for i in range(3)]
for coro in asyncio.as_completed(coros):
    result = await coro
    print(result)
```

---

## Queue 队列

**基本写法：asyncio.Queue**
`asyncio.Queue(maxsize=<大小>)`
```python
# 异步队列
q = asyncio.Queue(maxsize=10)

async def producer():
    await q.put("item")

async def consumer():
    item = await q.get()
    q.task_done()
```

**基本写法：get 与 put**
`await q.put(<值>)` | `await q.get()`
```python
# 异步入队出队
await q.put("x")
item = await q.get()
```

**基本写法：join 等待全部处理**
`await q.join()`
```python
# 等待所有 item 被 task_done
await q.join()
```

**基本写法：PriorityQueue 与 LifoQueue**
`asyncio.PriorityQueue()` | `asyncio.LifoQueue()`
```python
# 优先队列与栈
pq = asyncio.PriorityQueue()
pq.put_nowait((1, "high"))
```

---

## Lock 锁

**基本写法：asyncio.Lock**
`asyncio.Lock()`
```python
# 异步锁
lock = asyncio.Lock()

async def safe_update():
    async with lock:
        pass
```

**基本写法：acquire 与 release**
`await lock.acquire()` | `lock.release()`
```python
# 手动加锁
await lock.acquire()
try:
    pass
finally:
    lock.release()
```

---

## Event 与 Condition

**基本写法：asyncio.Event**
`asyncio.Event()`
```python
# 异步事件
event = asyncio.Event()

async def waiter():
    await event.wait()

async def setter():
    event.set()
```

**基本写法：asyncio.Condition**
`asyncio.Condition()`
```python
# 异步条件变量
cond = asyncio.Condition()

async def consumer():
    async with cond:
        await cond.wait_for(lambda: data_ready)
```

---

## Semaphore 信号量

**基本写法：asyncio.Semaphore**
`asyncio.Semaphore(<数量>)`
```python
# 限制并发数
sem = asyncio.Semaphore(5)

async def fetch_limited(url):
    async with sem:
        return await fetch(url)
```

**基本写法：BoundedSemaphore**
`asyncio.BoundedSemaphore(<数量>)`
```python
# 有界信号量
sem = asyncio.BoundedSemaphore(3)
```

---

## Stream 流

**基本写法：open_connection 客户端**
`asyncio.open_connection(<主机>, <端口>)`
```python
# 异步 TCP 客户端
async def tcp_client():
    reader, writer = await asyncio.open_connection("example.com", 80)
    writer.write(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    data = await reader.read(1024)
    writer.close()
    await writer.wait_closed()
```

**基本写法：start_server 服务端**
`asyncio.start_server(<回调>, <主机>, <端口>)`
```python
# 异步 TCP 服务端
async def handle(reader, writer):
    data = await reader.read(100)
    writer.write(data)
    await writer.drain()
    writer.close()

server = await asyncio.start_server(handle, "0.0.0.0", 8888)
async with server:
    await server.serve_forever()
```

**基本写法：读写流**
`writer.write(<字节>)` | `await reader.read(<长度>)`
```python
# 流读写
writer.write(b"hello")
await writer.drain()
data = await reader.read(1024)
```

**基本写法：readline 与 readexactly**
`await reader.readline()` | `await reader.readexactly(<字节>)`
```python
# 按行读取与精确读取
line = await reader.readline()
data = await reader.readexactly(8)
```

---

## 取消与超时

**基本写法：cancel 取消任务**
`task.cancel()`
```python
# 取消任务
task = asyncio.create_task(fetch("a"))
task.cancel()
try:
    await task
except asyncio.CancelledError:
    print("任务已取消")
```

**基本写法：CancelledError 处理**
`try: await task\nexcept asyncio.CancelledError:`
```python
# 协程内处理取消
async def work():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("清理资源")
        raise
```

**基本写法：shield 屏蔽取消**
`asyncio.shield(<协程>)`
```python
# 保护协程不被取消
result = await asyncio.shield(fetch("a"))
```

---

## 事件循环

**基本写法：run 运行**
`asyncio.run(<协程>)`
```python
# 运行顶层协程
asyncio.run(main())
```

**基本写法：get_running_loop**
`asyncio.get_running_loop()`
```python
# 在协程中获取当前循环
loop = asyncio.get_running_loop()
```

**基本写法：run_in_executor 阻塞任务**
`loop.run_in_executor(<执行器>, <函数>, *<参数>)`
```python
# 在线程池运行阻塞函数
import time

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, time.sleep, 1)
```

**基本写法：to_thread（3.9+）**
`asyncio.to_thread(<函数>, *<参数>)`
```python
# 简化版 run_in_executor
result = await asyncio.to_thread(time.sleep, 1)
```

**基本写法：call_later 延迟调用**
`loop.call_later(<秒>, <回调>)`
```python
# 延迟执行回调
loop = asyncio.get_running_loop()
loop.call_later(5, lambda: print("5 秒后"))
```

---

## sleep 与时间

**基本写法：sleep**
`await asyncio.sleep(<秒>)`
```python
# 异步等待
await asyncio.sleep(1.0)
```

**基本写法：get_event_loop 时间**
`loop.time()`
```python
# 事件循环单调时钟
loop = asyncio.get_running_loop()
start = loop.time()
```
