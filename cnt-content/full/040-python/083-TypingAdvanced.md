---
order: 830
title: Python typing 进阶
module: python

category: '040-python'
difficulty: beginner
description: Python typing 进阶 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Literal 字面量类型

**基本写法：限定具体值**
`Literal[<值1>, <值2>]`
```python
# 限定参数只能取特定字面值
from typing import Literal

def set_mode(mode: Literal["r", "w", "a"]) -> None:
    pass

set_mode("r")
```

---

## TypedDict 结构化字典

**基本写法：定义 TypedDict**
`class <名称>(TypedDict):\n    <字段>: <类型>`
```python
# 类型化字典
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    active: bool

u: User = {"id": 1, "name": "Alice", "active": True}
```

**基本写法：total=False 全可选**
`class <名称>(TypedDict, total=False):`
```python
# 所有字段可选
class Point(TypedDict, total=False):
    x: int
    y: int
```

**基本写法：Required 与 NotRequired（3.11+）**
`Required[<类型>]` | `NotRequired[<类型>]`
```python
# 单字段控制可选性
from typing import TypedDict, Required, NotRequired

class Config(TypedDict):
    host: Required[str]
    port: NotRequired[int]
```

**基本写法：ReadOnly 只读（3.13+）**
`ReadOnly[<类型>]`
```python
# 标记字段只读
from typing import TypedDict, ReadOnly

class Item(TypedDict):
    id: ReadOnly[int]
    name: str
```

---

## Final 不可变注解

**基本写法：声明 Final**
`<变量>: Final[<类型>] = <值>`
```python
# Final 表示变量不应被重新赋值
from typing import Final

MAX_SIZE: Final[int] = 100
```

**基本写法：类属性 Final**
`<属性>: Final[<类型>]`
```python
# 类属性标记为 Final
class Config:
    VERSION: Final[str] = "1.0.0"
```

---

## Protocol 结构子类型

**基本写法：定义 Protocol**
`class <名称>(Protocol):\n    def <方法>(self): ...`
```python
# 鸭子类型的静态检查支持
from typing import Protocol

class Closeable(Protocol):
    def close(self) -> None: ...

def close_all(items: list[Closeable]) -> None:
    for item in items:
        item.close()
```

**基本写法：runtime_checkable**
`@runtime_checkable`
```python
# 允许 isinstance 检查
from typing import Protocol, runtime_checkable

@runtime_checkable
class Iterable2(Protocol):
    def __iter__(self): ...

print(isinstance([1, 2], Iterable2))
```

---

## TypeVar 类型变量

**基本写法：定义 TypeVar**
`T = TypeVar("<名称>")`
```python
# 泛型类型变量
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]
```

**基本写法：带约束**
`TypeVar("<名称>", <类型1>, <类型2>)`
```python
# 限定类型取值范围
T = TypeVar("T", int, float)

def add(a: T, b: T) -> T:
    return a + b
```

**基本写法：bound 上界**
`TypeVar("<名称>", bound=<类型>)`
```python
# 上界约束
T = TypeVar("T", bound=str)

def upper(x: T) -> T:
    return x.upper()
```

**基本写法：TypeVar 默认值（3.13+）**
`TypeVar("<名称>", default=<类型>)`
```python
# 类型参数默认值
T = TypeVar("T", default=int)

def value(x: T = 0) -> T:
    return x
```

---

## ParamSpec 参数规格

**基本写法：定义 ParamSpec**
`P = ParamSpec("<名称>")`
```python
# 捕获可调用对象的参数规格
from typing import ParamSpec, TypeVar, Callable

P = ParamSpec("P")
R = TypeVar("R")

def logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)
    return wrapper
```

---

## TypeVarTuple 可变泛型

**基本写法：定义 TypeVarTuple**
`Ts = TypeVarTuple("<名称>")`
```python
# 可变长度类型变量元组
from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple("Ts")

def first(x: tuple[*Ts]) -> tuple[*Ts]:
    return x
```

---

## TypeAlias 类型别名

**基本写法：类型别名**
`type <别名> = <类型>`
```python
# Python 3.12 新语法
type Vector = list[float]

def norm(v: Vector) -> float:
    return sum(x * x for x in v) ** 0.5
```

**基本写法：泛型别名**
`type <别名>[<参数>] = <类型>`
```python
# 带类型参数的别名
type Pair[T] = tuple[T, T]

def make(x: int) -> Pair[int]:
    return (x, x)
```

---

## TypeGuard 与 TypeIs 类型 narrowing

**基本写法：TypeGuard**
`TypeGuard[<类型>]`
```python
# 自定义类型守卫
from typing import TypeGuard

def is_str_list(val: list) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)

def process(val: list):
    if is_str_list(val):
        return [x.upper() for x in val]
```

**基本写法：TypeIs（3.13+）**
`TypeIs[<类型>]`
```python
# TypeIs 提供更直观的双向 narrowing
from typing import TypeIs

def is_int(x: object) -> TypeIs[int]:
    return isinstance(x, int)
```

---

## overload 函数重载

**基本写法：overload 装饰器**
`@overload`
```python
# 函数重载签名
from typing import overload

@overload
def parse(x: int) -> str: ...
@overload
def parse(x: str) -> int: ...
def parse(x):
    if isinstance(x, int):
        return str(x)
    return int(x)
```

---

## Generic 泛型类

**基本写法：Generic 类**
`class <类>(Generic[T]):`
```python
# 泛型容器
from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
    def pop(self) -> T:
        return self._items.pop()
```

**基本写法：PEP 695 泛型语法（3.12+）**
`class <类>[T]:`
```python
# 新语法无需 TypeVar
class Stack[T]:
    def __init__(self):
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
```

---

## Never 与 NoReturn

**基本写法：NoReturn**
`def <函数>() -> NoReturn:`
```python
# 表示函数永不返回
from typing import NoReturn

def fatal() -> NoReturn:
    raise SystemExit(1)
```

**基本写法：Never**
`def <函数>() -> Never:`
```python
# Never 表示永不产生值（3.11+）
from typing import Never

def unreachable() -> Never:
    raise RuntimeError
```

---

## override 装饰器（3.12+）

**基本写法：标记覆盖**
`@typing.override`
```python
# 标记方法覆盖父类方法
from typing import override

class Base:
    def run(self): pass

class Sub(Base):
    @override
    def run(self):
        print("子类实现")
```

## 延伸阅读
Python 数据类型与内置容器，见 040-python 模块的基础文档。
Python 异步编程（asyncio/FastAPI），见 040-python 模块的异步与 Web 文档。
Python 数据分析（NumPy/Pandas），见 051-data-analysis 模块。
Python 与数据库交互（SQLAlchemy），见 019-sql 模块相关文档。
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
