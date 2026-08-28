# Python 迭代器与生成器进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 迭代器协议

**基本写法：自定义迭代器**
`class <迭代器>:\n    def __iter__(self): return self\n    def __next__(self):`
```python
# 实现 __iter__ 与 __next__ 的迭代器
class Counter:
    def __init__(self, low, high):
        self.cur = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.cur >= self.high:
            raise StopIteration
        v = self.cur
        self.cur += 1
        return v

for x in Counter(1, 4):
    print(x)
```

**基本写法：可迭代对象**
`class <可迭代>:\n    def __iter__(self):`
```python
# 可迭代对象返回独立迭代器
class Range:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        for i in range(self.n):
            yield i
```

---

## 生成器函数

**基本写法：yield 生成值**
`def <生成器>():\n    yield <值>`
```python
# 生成器函数惰性产出值
def counter(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(list(counter(3)))
```

**基本写法：yield from 委托**
`yield from <可迭代>`
```python
# 委托给子生成器
def chained(*iters):
    for it in iters:
        yield from it

print(list(chained([1, 2], [3, 4])))
```

**基本写法：无限生成器**
`def <生成器>():\n    while True: yield <值>`
```python
# 无限序列生成器
def naturals(start=1):
    n = start
    while True:
        yield n
        n += 1

from itertools import islice
print(list(islice(naturals(), 5)))
```

---

## 生成器高级方法

**基本写法：send 发送值**
`gen.send(<值>)`
```python
# send 向生成器注入值
def echo():
    while True:
        received = yield
        print(f"收到: {received}")

g = echo()
next(g)            # 预激到第一个 yield
g.send("hello")
```

**基本写法：throw 抛异常**
`gen.throw(<异常类>, <消息>)`
```python
# 在 yield 处抛出异常
def handler():
    try:
        while True:
            try:
                x = yield
                print(f"处理 {x}")
            except ValueError as e:
                print(f"捕获 {e}")
    except GeneratorExit:
        print("生成器关闭")

g = handler()
next(g)
g.send(1)
g.throw(ValueError, "无效值")
```

**基本写法：close 关闭生成器**
`gen.close()`
```python
# 关闭生成器，触发 GeneratorExit
g = counter(10)
next(g)
g.close()
```

**基本写法：return 终止生成器**
`return <值>`
```python
# return 触发 StopIteration 携带返回值
def worker():
    yield 1
    yield 2
    return "done"

g = worker()
try:
    while True:
        print(next(g))
except StopIteration as e:
    print("返回值:", e.value)
```

---

## 生成器表达式

**基本写法：生成器表达式**
`(<表达式> for <变量> in <可迭代>)`
```python
# 惰性求值的生成器表达式
gen = (x * 2 for x in range(1000000))
print(next(gen))
```

**基本写法：带条件**
`(<表达式> for <变量> in <可迭代> if <条件>)`
```python
# 带过滤的生成器表达式
evens = (x for x in range(20) if x % 2 == 0)
print(list(evens))
```

**基本写法：链式生成器**
`(<表达式> for <变量1> in <可迭代1> for <变量2> in <可迭代2>)`
```python
# 笛卡尔积
pairs = ((x, y) for x in "ab" for y in "12")
print(list(pairs))
```

---

## 协程生成器

**基本写法：yield 接收返回**
`x = yield`
```python
# 双向通信的协程生成器
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            return total
        total += value

acc = accumulator()
next(acc)
print(acc.send(10))
print(acc.send(20))
print(acc.send(None))
```

---

## 异步生成器

**基本写法：async 生成器**
`async def <异步生成器>():\n    yield <值>`
```python
# 异步生成器 yield 之间可 await
import asyncio

async def async_counter(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for x in async_counter(3):
        print(x)

asyncio.run(main())
```

**基本写法：async for 迭代**
`async for <变量> in <异步生成器>:`
```python
# 异步迭代
async def main():
    async for x in async_counter(3):
        print(x)
```

---

## 内置迭代工具

**基本写法：iter 双参形式**
`iter(<可调用>, <哨兵>)`
```python
# 调用可调用直到返回哨兵值
import random
data = iter(lambda: random.randint(1, 10), 5)
print(list(data))
```

**基本写法：next 取下一值**
`next(<迭代器>, <默认值>)`
```python
# 带默认值的 next
g = iter([])
print(next(g, "empty"))
```

**基本写法：zip 并行**
`zip(*<可迭代>, strict=<bool>)`
```python
# strict=True 要求长度一致（3.10+）
for a, b in zip([1, 2, 3], ["a", "b", "c"], strict=True):
    print(a, b)
```

**基本写法：enumerate 索引**
`enumerate(<可迭代>, start=<起>)`
```python
# 带索引迭代
for i, v in enumerate(["a", "b"], start=1):
    print(i, v)
```
