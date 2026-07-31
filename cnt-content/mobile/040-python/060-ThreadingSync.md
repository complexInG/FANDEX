# Python threading 同步原语

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Lock 互斥锁

**基本写法：创建锁**
`threading.Lock()`
```python
# 互斥锁
import threading

lock = threading.Lock()
```

**基本写法：acquire 与 release**
`lock.acquire()` | `lock.release()`
```python
# 手动加锁解锁
lock.acquire()
try:
    pass
finally:
    lock.release()
```

**基本写法：with 自动管理**
`with lock:`
```python
# 推荐：with 自动加锁解锁
with lock:
    pass
```

**基本写法：非阻塞获取**
`lock.acquire(blocking=False)`
```python
# 非阻塞尝试获取
if lock.acquire(blocking=False):
    try:
        pass
    finally:
        lock.release()
else:
    print("锁被占用")
```

**基本写法：带超时获取**
`lock.acquire(timeout=<秒>)`
```python
# 超时获取
if lock.acquire(timeout=5):
    try:
        pass
    finally:
        lock.release()
```

---

## RLock 可重入锁

**基本写法：创建 RLock**
`threading.RLock()`
```python
# 同一线程可多次获取
rlock = threading.RLock()

def recursive(n):
    with rlock:
        if n > 0:
            recursive(n - 1)
```

---

## Condition 条件变量

**基本写法：创建 Condition**
`threading.Condition(<锁>)`
```python
# 条件变量
cond = threading.Condition()
```

**基本写法：wait 等待**
`with cond:\n    cond.wait()`
```python
# 等待条件满足
with cond:
    cond.wait()
```

**基本写法：notify 通知**
`cond.notify(<数量>)` | `cond.notify_all()`
```python
# 通知等待线程
with cond:
    cond.notify()
    cond.notify_all()
```

**基本写法：生产者消费者**
`Condition` 配合 wait/notify
```python
queue = []
MAX = 5
cond = threading.Condition()

def producer():
    with cond:
        while len(queue) >= MAX:
            cond.wait()
        queue.append("item")
        cond.notify_all()

def consumer():
    with cond:
        while not queue:
            cond.wait()
        item = queue.pop(0)
        cond.notify_all()
```

**基本写法：wait_for 条件谓词**
`cond.wait_for(<谓词函数>, timeout=<秒>)`
```python
# 等待条件成立
with cond:
    cond.wait_for(lambda: len(queue) > 0)
    item = queue.pop(0)
```

---

## Event 事件

**基本写法：创建 Event**
`threading.Event()`
```python
# 事件标志
event = threading.Event()
```

**基本写法：set 与 clear**
`event.set()` | `event.clear()`
```python
# 设置与清除标志
event.set()
event.clear()
```

**基本写法：wait 等待**
`event.wait(timeout=<秒>)`
```python
# 等待事件被 set
event.wait()
event.wait(timeout=5)
```

**基本写法：is_set 检查**
`event.is_set()`
```python
# 检查标志状态
print(event.is_set())
```

---

## Semaphore 信号量

**基本写法：创建信号量**
`threading.Semaphore(<数量>)`
```python
# 限制并发数
sem = threading.Semaphore(3)

def worker():
    with sem:
        pass
```

**基本写法：BoundedSemaphore**
`threading.BoundedSemaphore(<数量>)`
```python
# 有界信号量
sem = threading.BoundedSemaphore(3)
```

---

## Barrier 栅栏

**基本写法：创建 Barrier**
`threading.Barrier(<数量>)`
```python
# 等待指定数量线程到达后一起继续
barrier = threading.Barrier(4)

def worker():
    barrier.wait()
```

**基本写法：带超时**
`barrier.wait(timeout=<秒>)`
```python
# 超时则抛出 BrokenBarrierError
barrier.wait(timeout=10)
```

**基本写法：abort 中断**
`barrier.abort()`
```python
# 中断栅栏
barrier.abort()
```

---

## local 线程局部存储

**基本写法：创建 local**
`threading.local()`
```python
# 线程局部数据
local_data = threading.local()
local_data.value = 0
```

---

## GIL 与自由线程

**基本写法：Python GIL**
`threading` 适用于 IO 密集型
```python
# GIL 限制：同一时刻只有一个线程执行 Python 字节码
# CPU 密集型任务请用 multiprocessing
```

**基本写法：3.13 自由线程模式**
`python -X gil=0`
```python
# Python 3.13 实验性无 GIL 模式（PEP 703）
# python -X gil=0 main.py
```

---

## 线程枚举

**基本写法：活跃线程数**
`threading.active_count()`
```python
# 当前活跃线程数
print(threading.active_count())
```

**基本写法：枚举线程**
`threading.enumerate()`
```python
# 获取所有活跃线程列表
for t in threading.enumerate():
    print(t.name)
```

**基本写法：主线程**
`threading.main_thread()`
```python
# 获取主线程对象
print(threading.main_thread().name)
```

---

## Timer 定时线程

**基本写法：创建 Timer**
`threading.Timer(<秒>, <函数>)`
```python
# 定时执行函数
def hello():
    print("hello")

t = threading.Timer(5.0, hello)
t.start()
```

**基本写法：取消 Timer**
`t.cancel()`
```python
# 取消未执行的定时器
t.cancel()
```

---

## 线程间通信 queue

**基本写法：Queue**
`queue.Queue(<最大长度>)`
```python
# 线程安全队列
import queue

q = queue.Queue(maxsize=10)
q.put("item")
print(q.get())
```

**基本写法：非阻塞操作**
`q.put(<值>, block=False)` | `q.get(block=False)`
```python
# 非阻塞
try:
    q.put("x", block=False)
except queue.Full:
    pass

try:
    q.get(block=False)
except queue.Empty:
    pass
```

**基本写法：LifoQueue 与 PriorityQueue**
`queue.LifoQueue()` | `queue.PriorityQueue()`
```python
# 后进先出与优先队列
lifo = queue.LifoQueue()
pq = queue.PriorityQueue()
pq.put((1, "high"))
pq.put((3, "low"))
```

**基本写法：task_done 与 join**
`q.task_done()` | `q.join()`
```python
# 任务完成标记与等待全部处理
q.put("task1")
q.get()
q.task_done()
q.join()
```

**基本写法：SimpleQueue（3.7+）**
`queue.SimpleQueue()`
```python
# 无界的简单队列，性能更好
sq = queue.SimpleQueue()
sq.put("x")
print(sq.get())
```
