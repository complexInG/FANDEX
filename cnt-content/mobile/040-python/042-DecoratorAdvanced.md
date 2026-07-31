# Python 装饰器进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## functools.wraps 保留元信息

**基本写法：wraps 装饰器**
`@functools.wraps(<原函数>)`
```python
# 装饰器中使用 wraps 保留原函数元信息
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result
    return wrapper

@my_decorator
def greet(name):
    """打招呼"""
    return f"Hello, {name}"

print(greet.__name__, greet.__doc__)
```

---

## 带参数装饰器

**基本写法：三层嵌套装饰器**
`def <装饰器>(<参数>):\n    def wrapper(func): ...\n    return wrapper`
```python
# 带参数的装饰器需要三层嵌套
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)
```

**基本写法：带关键字参数**
`def <装饰器>(<参数>=<默认值>):`
```python
# 带默认参数的装饰器
def logged(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] 调用 {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@logged(level="DEBUG")
def process():
    pass
```

---

## 类装饰器

**基本写法：类作为装饰器**
`class <装饰器类>:\n    def __init__(self, func): ...\n    def __call__(self, *args):`
```python
# 类装饰器通过 __call__ 实现
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"第 {self.count} 次调用")
        return self.func(*args, **kwargs)

@Counter
def hello():
    print("hi")

hello(); hello()
```

**基本写法：带参数类装饰器**
`class <类>:\n    def __init__(self, <参数>): ...\n    def __call__(self, func):`
```python
# 带参数的类装饰器
class Retry:
    def __init__(self, times=3):
        self.times = times
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(self.times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == self.times - 1:
                        raise
        return wrapper

@Retry(times=5)
def fetch():
    pass
```

---

## 装饰器堆叠

**基本写法：多个装饰器堆叠**
`@<装饰器1>\n@<装饰器2>\ndef <函数>:`
```python
# 装饰器从下往上应用，从上往下执行
@decorator_a
@decorator_b
def func():
    pass
# 等价于 func = decorator_a(decorator_b(func))
```

---

## 装饰类方法

**基本写法：装饰实例方法**
`def <装饰器>(method):\n    @functools.wraps(method)\n    def wrapper(self, *args, **kwargs):`
```python
# 装饰类的实例方法
def log_call(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"调用 {method.__name__}")
        return method(self, *args, **kwargs)
    return wrapper

class Service:
    @log_call
    def run(self):
        return "done"
```

**基本写法：装饰 classmethod 与 staticmethod**
`@classmethod` | `@staticmethod`
```python
# 注意装饰器顺序：staticmethod 应在最外层
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def create(cls):
        return cls()
```

---

## 内置常用装饰器

**基本写法：functools.lru_cache**
`@functools.lru_cache(maxsize=<大小>)`
```python
# LRU 缓存装饰器
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))
```

**基本写法：functools.cache**
`@functools.cache`
```python
# 无限缓存（3.9+）
from functools import cache

@cache
def expensive(n):
    return sum(range(n))
```

**基本写法：functools.cached_property**
`@functools.cached_property`
```python
# 首次访问后缓存属性
from functools import cached_property

class Data:
    @cached_property
    def heavy(self):
        return list(range(1000000))
```

**基本写法：functools.singledispatch**
`@functools.singledispatch`
```python
# 单分派泛函数
from functools import singledispatch

@singledispatch
def process(data):
    raise TypeError("不支持的类型")

@process.register(int)
def _(data):
    return data * 2

@process.register(str)
def _(data):
    return data.upper()

print(process(5))
print(process("abc"))
```

**基本写法：functools.singledispatchmethod**
`@functools.singledispatchmethod`
```python
# 类方法单分派（3.8+）
from functools import singledispatchmethod

class Processor:
    @singledispatchmethod
    def process(self, data):
        raise TypeError

    @process.register
    def _(self, data: int):
        return data * 2
```

---

## dataclass 装饰器

**基本写法：dataclass 装饰器**
`@dataclasses.dataclass`
```python
# 自动生成 __init__/__repr__/__eq__
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

---

## 自定义属性访问装饰器

**基本写法：property**
`@property`
```python
# property 装饰器定义只读属性
class Circle:
    def __init__(self, r):
        self.r = r
    @property
    def area(self):
        return 3.14 * self.r ** 2
```

**基本写法：abstract 装饰器**
`@abc.abstractmethod`
```python
# 抽象方法装饰器
import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sound(self):
        pass
```

---

## warnings.deprecated（3.13+）

**基本写法：标记弃用**
`@warnings.deprecated(<消息>)`
```python
# Python 3.13 新增弃用装饰器
import warnings

@warnings.deprecated("使用 new_func 替代")
def old_func():
    pass
```
