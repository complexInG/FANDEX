---
order: 720
title: Python functools 函数工具
module: python

category: '040-python'
difficulty: beginner
description: Python functools 函数工具 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## reduce 归约

**基本写法：reduce 归约**
`functools.reduce(<函数>, <可迭代>, [初始值])`
```python
# 累积应用函数到所有元素
from functools import reduce
import operator
result = reduce(operator.add, [1, 2, 3, 4], 0)  # 10
```

**基本写法：reduce 求最大值**
`functools.reduce(lambda a, b: a if a > b else b, <可迭代>)`
```python
# 找出最大值
from functools import reduce
nums = [3, 1, 4, 1, 5, 9]
m = reduce(lambda a, b: a if a > b else b, nums)  # 9
```

---

## 缓存装饰器

**基本写法：lru_cache LRU 缓存**
`@lru_cache(maxsize=<大小>)`
```python
# 基于最近最少使用策略的缓存
from functools import lru_cache
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

**基本写法：cache 无限缓存**
`@cache`
```python
# Python 3.9+ 无大小限制的缓存
from functools import cache
@cache
def slow_query(key):
    return database.get(key)
```

**基本写法：查看缓存信息**
`<函数>.cache_info()`
```python
# 查看缓存命中情况
fibonacci(50)
print(fibonacci.cache_info())
# CacheInfo(hits=49, misses=51, maxsize=128, currsize=51)
```

**基本写法：清除缓存**
`<函数>.cache_clear()`
```python
# 手动清空缓存
fibonacci.cache_clear()
```

**基本写法：Python 3.9+ typed 参数类型区分**
`@lru_cache(typed=True)`
```python
# 区分不同参数类型（1 和 1.0 分别缓存）
from functools import lru_cache
@lru_cache(typed=True)
def f(x):
    return x * 2
```

---

## partial 偏函数

**基本写法：创建偏函数**
`functools.partial(<函数>, *<参数>, **<关键字参数>)`
```python
# 固定部分参数生成新函数
from functools import partial
int2 = partial(int, base=2)
print(int2("1010"))  # 10
```

**基本写法：固定位置参数**
`functools.partial(<函数>, <值>)`
```python
# 固定第一个参数
from functools import partial
def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
print(square(5))  # 25
```

**基本写法：partial 对象属性**
`<偏函数>.args / .keywords`
```python
# 查看偏函数固定的参数
p = partial(int, base=2)
print(p.args)      # ()
print(p.keywords)  # {'base': 2}
```

---

## wraps 保留元信息

**基本写法：使用 @wraps**
`@wraps(<原函数>)`
```python
# 装饰器中保留原函数元信息
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## singledispatch 单分派

**基本写法： singledispatch 按类型分派**
`@singledispatch`
```python
# 根据第一个参数类型调用不同实现
from functools import singledispatch
@singledispatch
def process(data):
    raise TypeError(f"不支持类型: {type(data)}")

@process.register
def _(data: int):
    return f"整数: {data}"
```

**基本写法：注册分派函数**
`@<函数>.register`
```python
# 注册字符串类型处理
@process.register
def _(data: str):
    return f"字符串: {data}"
```

**基本写法：注册多个类型**
`@<函数>.register(<类型1>, <类型2>)`
```python
# 一个实现处理多种类型
@process.register(list)
@process.register(tuple)
def _(data):
    return f"序列: {len(data)} 项"
```

---

## singledispatchmethod 方法分派

**基本写法： singledispatchmethod 类方法分派**
`@singledispatchmethod`
```python
# Python 3.8+ 类方法按参数类型分派
from functools import singledispatchmethod
class Processor:
    @singledispatchmethod
    def process(self, data):
        raise TypeError("不支持")
    @process.register
    def _from_int(self, data: int):
        return data * 2
```

---

## total_ordering 自动补全比较方法

**换行写法：total_ordering 装饰类**
`@total_ordering`
`class <类名>:`
`    def __eq__(self, other): ...`
`    def __lt__(self, other): ...`

```python
# 定义一个比较方法后自动生成其余
from functools import total_ordering
@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __eq__(self, other):
        return self.grade == other.grade
    def __lt__(self, other):
        return self.grade < other.grade
```

---

## cached_property 缓存属性

**基本写法：cached_property**
`@cached_property`
```python
# 属性计算结果缓存，只计算一次
from functools import cached_property
class DataSet:
    def __init__(self, data):
        self.data = data
    @cached_property
    def mean(self):
        return sum(self.data) / len(self.data)
```

---

## cmp_to_key 比较函数转键

**基本写法：cmp_to_key 转换比较函数**
`functools.cmp_to_key(<比较函数>)`
```python
# 将旧式比较函数转为 key 函数
from functools import cmp_to_key
def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0
sorted([3, 1, 2], key=cmp_to_key(compare))
```

---

## Python 3.13+ functools 增强

**基本写法：Python 3.13+ lru_cache 不带参数**
`@lru_cache`
```python
# Python 3.13+ lru_cache 无参数时等同于 cache
from functools import lru_cache
@lru_cache
def compute(x):
    return x * x
```

**基本写法：Python 3.13+ singledispatch 泛型方法**
`@singledispatchmethod`
```python
# Python 3.13+ 支持联合类型注册
from functools import singledispatch
@singledispatch
def handle(data):
    pass
@handle.register(int | float)
def _(data):
    return data * 2
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
