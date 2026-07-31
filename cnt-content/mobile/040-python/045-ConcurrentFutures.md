# Python concurrent.futures

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ThreadPoolExecutor 线程池

**基本写法：创建线程池**
`concurrent.futures.ThreadPoolExecutor(max_workers=<数量>)`
```python
# 创建线程池
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    pass
```

**基本写法：submit 提交任务**
`executor.submit(<函数>, *<参数>)`
```python
# 提交单个任务并返回 Future
with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(pow, 2, 8)
    print(future.result())
```

**基本写法：map 批量提交**
`executor.map(<函数>, <可迭代>)`
```python
# 批量提交并按顺序返回结果
def square(x):
    return x * x

with ThreadPoolExecutor() as executor:
    results = list(executor.map(square, [1, 2, 3, 4]))
    print(results)
```

---

## ProcessPoolExecutor 进程池

**基本写法：创建进程池**
`concurrent.futures.ProcessPoolExecutor(max_workers=<数量>)`
```python
# 创建进程池
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as executor:
    future = executor.submit(pow, 2, 8)
    print(future.result())
```

**基本写法：进程池 map**
`executor.map(<函数>, <可迭代>)`
```python
# 进程池批量处理 CPU 密集任务
def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy, [100000, 200000, 300000]))
```

---

## Future 对象

**基本写法：result 获取结果**
`future.result(timeout=<秒>)`
```python
# 阻塞等待结果
future = executor.submit(pow, 2, 8)
print(future.result(timeout=5))
```

**基本写法：exception 获取异常**
`future.exception()`
```python
# 获取任务抛出的异常
future = executor.submit(lambda: 1 / 0)
try:
    future.result()
except ZeroDivisionError:
    print(future.exception())
```

**基本写法：done 判断完成**
`future.done()`
```python
# 判断任务是否完成
print(future.done())
```

**基本写法：cancelled 判断取消**
`future.cancelled()`
```python
# 判断任务是否被取消
print(future.cancelled())
```

**基本写法：cancel 取消任务**
`future.cancel()`
```python
# 尝试取消未开始的任务
future = executor.submit(pow, 2, 8)
future.cancel()
```

**基本写法：add_done_callback 回调**
`future.add_done_callback(<函数>)`
```python
# 任务完成时回调
def on_done(fut):
    print("结果:", fut.result())

future = executor.submit(pow, 2, 8)
future.add_done_callback(on_done)
```

---

## wait 等待多个 Future

**基本写法：wait 等待**
`concurrent.futures.wait(<Future 列表>)`
```python
# 等待所有任务完成
from concurrent.futures import wait

futures = [executor.submit(pow, 2, i) for i in range(5)]
done, not_done = wait(futures)
print([f.result() for f in done])
```

**基本写法：指定 return_when**
`wait(<列表>, return_when=<常量>)`
```python
# FIRST_COMPLETED 首个完成即返回
from concurrent.futures import wait, FIRST_COMPLETED

done, not_done = wait(futures, return_when=FIRST_COMPLETED)
```

**基本写法：指定 timeout**
`wait(<列表>, timeout=<秒>)`
```python
# 超时返回
done, not_done = wait(futures, timeout=2.0)
```

---

## as_completed 按完成顺序

**基本写法：as_completed 迭代**
`concurrent.futures.as_completed(<Future 列表>)`
```python
# 按完成顺序迭代结果
from concurrent.futures import as_completed

futures = [executor.submit(pow, 2, i) for i in range(5)]
for future in as_completed(futures):
    print(future.result())
```

**基本写法：带超时**
`as_completed(<列表>, timeout=<秒>)`
```python
# 带超时迭代
for future in as_completed(futures, timeout=5):
    try:
        print(future.result())
    except TimeoutError:
        break
```

---

## 异常处理

**基本写法：捕获任务异常**
`try: future.result()\nexcept <异常>:`
```python
# 任务异常会通过 result() 重新抛出
futures = [executor.submit(lambda: 1 / 0)]
for future in as_completed(futures):
    try:
        future.result()
    except ZeroDivisionError as e:
        print("任务异常:", e)
```

---

## Executor 上下文管理

**基本写法：with 自动关闭**
`with ThreadPoolExecutor() as executor:`
```python
# with 块结束时会调用 executor.shutdown(wait=True)
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(task)
```

**基本写法：shutdown 手动关闭**
`executor.shutdown(wait=<bool>, cancel_futures=<bool>)`
```python
# 手动关闭执行器
executor = ThreadPoolExecutor()
executor.submit(task)
executor.shutdown(wait=True, cancel_futures=True)
```
