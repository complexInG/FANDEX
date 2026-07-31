# Python 多进程与多线程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## threading 线程创建

**基本写法：创建线程**
`threading.Thread(target=<函数>, args=<参数>)`
```python
# 创建并启动线程
import threading
def worker(name):
    print(f"线程 {name} 运行中")
t = threading.Thread(target=worker, args=("A",))
t.start()
t.join()
```

**换行写法：继承 Thread 类**
`class <类名>(threading.Thread):`
`    def run(self): <语句>`

```python
# 继承 Thread 自定义线程逻辑
import threading
class MyThread(threading.Thread):
    def __init__(self, task):
        super().__init__()
        self.task = task
    def run(self):
        print(f"执行: {self.task}")
t = MyThread("download")
t.start()
t.join()
```

**基本写法：获取当前线程**
`threading.current_thread()`
```python
# 获取当前线程对象
t = threading.current_thread()
print(t.name)
```

**基本写法：获取活跃线程数**
`threading.active_count()`
```python
# 返回当前活跃线程数
print(threading.active_count())
```

---

## threading 线程同步

**基本写法：Lock 互斥锁**
`threading.Lock()`
```python
# 互斥锁保护共享资源
import threading
lock = threading.Lock()
count = 0
def increment():
    global count
    with lock:
        count += 1
```

**基本写法：RLock 可重入锁**
`threading.RLock()`
```python
# 同一线程可多次获取的锁
lock = threading.RLock()
def recursive(n):
    with lock:
        if n > 0:
            recursive(n - 1)
```

**基本写法：Semaphore 信号量**
`threading.Semaphore(<数量>)`
```python
# 限制同时访问的线程数
sem = threading.Semaphore(3)
def limited_task():
    with sem:
        do_work()
```

**基本写法：Event 事件**
`threading.Event()`
```python
# 线程间事件通知
event = threading.Event()
def waiter():
    event.wait()
    print("收到信号")
event.set()
```

**基本写法：Condition 条件变量**
`threading.Condition()`
```python
# 生产者消费者模式
cond = threading.Condition()
def producer():
    with cond:
        cond.notify_all()
def consumer():
    with cond:
        cond.wait()
```

---

## ThreadPoolExecutor 线程池

**基本写法：使用线程池**
`ThreadPoolExecutor(max_workers=<数量>)`
```python
# 线程池执行任务
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(fetch_url, urls)
```

**基本写法：submit 提交单个任务**
`executor.submit(<函数>, <参数>)`
```python
# 提交任务并获取 Future
with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(fetch_url, "https://example.com")
    result = future.result()
```

**基本写法：as_completed 按完成顺序获取**
`concurrent.futures.as_completed(<future列表>)`
```python
# 哪个先完成先处理哪个
from concurrent.futures import ThreadPoolExecutor, as_completed
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(fetch_url, url) for url in urls]
    for future in as_completed(futures):
        print(future.result())
```

**基本写法：future 回调**
`future.add_done_callback(<函数>)`
```python
# 任务完成后自动调用回调
def on_complete(future):
    print("结果:", future.result())
future = executor.submit(fetch_url, url)
future.add_done_callback(on_complete)
```

---

## multiprocessing 进程创建

**基本写法：创建进程**
`multiprocessing.Process(target=<函数>, args=<参数>)`
```python
# 创建并启动进程
import multiprocessing
def worker(name):
    print(f"进程 {name} 运行中")
p = multiprocessing.Process(target=worker, args=("A",))
p.start()
p.join()
```

**换行写法：继承 Process 类**
`class <类名>(multiprocessing.Process):`
`    def run(self): <语句>`

```python
# 继承 Process 自定义进程逻辑
import multiprocessing
class MyProcess(multiprocessing.Process):
    def run(self):
        print("自定义进程运行中")
p = MyProcess()
p.start()
p.join()
```

**基本写法：if __name__ == "__main__" 保护**
`if __name__ == "__main__": <主逻辑>`
```python
# Windows 下必须使用入口保护
import multiprocessing
def worker():
    print("工作进程")
if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
```

---

## multiprocessing 进程通信

**基本写法：Queue 进程队列**
`multiprocessing.Queue()`
```python
# 进程间安全队列
import multiprocessing
q = multiprocessing.Queue()
def producer():
    q.put("data")
def consumer():
    print(q.get())
```

**基本写法：Pipe 管道**
`multiprocessing.Pipe()`
```python
# 双向管道通信
parent_conn, child_conn = multiprocessing.Pipe()
def child():
    child_conn.send("hello")
    print(child_conn.recv())
```

**基本写法：Value 共享内存**
`multiprocessing.Value(<类型>, <初始值>)`
```python
# 共享内存中的简单变量
count = multiprocessing.Value("i", 0)
count.value += 1
```

**基本写法：Array 共享数组**
`multiprocessing.Array(<类型>, <大小>)`
```python
# 共享内存中的数组
arr = multiprocessing.Array("i", [0, 1, 2, 3])
print(arr[2])
```

---

## multiprocessing 进程同步

**基本写法：进程锁**
`multiprocessing.Lock()`
```python
# 跨进程互斥锁
lock = multiprocessing.Lock()
def worker():
    with lock:
        print("安全操作")
```

**基本写法：进程信号量**
`multiprocessing.Semaphore(<数量>)`
```python
# 跨进程信号量
sem = multiprocessing.Semaphore(2)
```

---

## ProcessPoolExecutor 进程池

**基本写法：使用进程池**
`ProcessPoolExecutor(max_workers=<数量>)`
```python
# 进程池执行 CPU 密集型任务
from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(heavy_compute, data_list))
```

**基本写法：submit 提交进程任务**
`executor.submit(<函数>, <参数>)`
```python
# 提交任务到进程池
with ProcessPoolExecutor() as executor:
    future = executor.submit(compute, data)
    result = future.result()
```

---

## Pool 进程池（旧式）

**基本写法：创建进程池**
`multiprocessing.Pool(<进程数>)`
```python
# 使用 Pool 创建进程池
from multiprocessing import Pool
with Pool(4) as pool:
    results = pool.map(worker, range(10))
```

**基本写法：异步映射**
`pool.map_async(<函数>, <可迭代>)`
```python
# 非阻塞映射
with Pool(4) as pool:
    result = pool.map_async(worker, range(10))
    result.wait()
    print(result.get())
```

**基本写法：apply_async 异步执行单个任务**
`pool.apply_async(<函数>, (<参数>,))`
```python
# 异步执行单个任务
with Pool(4) as pool:
    future = pool.apply_async(worker, (42,))
    print(future.get(timeout=5))
```

---

## 共享状态 Manager

**基本写法：Manager 共享字典**
`manager.dict()`
```python
# 通过 Manager 创建共享字典
from multiprocessing import Manager
with Manager() as manager:
    shared_dict = manager.dict()
    shared_dict["key"] = "value"
```

**基本写法：Manager 共享列表**
`manager.list()`
```python
# 通过 Manager 创建共享列表
with Manager() as manager:
    shared_list = manager.list()
    shared_list.append(1)
```

---

## Python 3.13+ free-threading 自由线程

**基本写法：Python 3.13+ 自由线程构建**
`python3.13t`
```python
# Python 3.13+ 实验性无 GIL 构建
# 使用自由线程构建时多线程可真正并行
# 需安装 python3.13t 并设置 PYTHON_GIL=0
import sys
print(sys._is_gil_enabled())  # 检查 GIL 是否启用
```

**基本写法：禁用 GIL**
`PYTHON_GIL=0`
```python
# Python 3.13+ 自由线程模式下禁用 GIL
# 环境变量 PYTHON_GIL=0 启动解释器
# 或在代码中设置
import sys
if hasattr(sys, "_enable_gil_disabled"):
    sys._enable_gil_disabled()
```
