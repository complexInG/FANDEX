---
order: 840
title: Python enum 枚举
module: python

category: '040-python'
difficulty: beginner
description: Python enum 枚举 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Enum 基础

**基本写法：定义枚举**
`class <名称>(enum.Enum):`
```python
# 定义枚举类型
import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)           # Color.RED
print(Color.RED.value)     # 1
print(Color.RED.name)      # RED
```

**基本写法：按值获取成员**
`<枚举>(<值>)`
```python
# 通过值获取枚举成员
c = Color(1)
print(c is Color.RED)
```

**基本写法：按名获取成员**
`<枚举>[<名称>]`
```python
# 通过名称字符串获取成员
c = Color["RED"]
print(c is Color.RED)
```

**基本写法：遍历枚举**
`for <成员> in <枚举>:`
```python
# 遍历所有枚举成员
for c in Color:
    print(c.name, c.value)
```

---

## IntEnum 与 IntFlag

**基本写法：IntEnum**
`class <名称>(enum.IntEnum):`
```python
# IntEnum 支持整数比较与运算
class Priority(enum.IntEnum):
    LOW = 1
    NORMAL = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)
```

**基本写法：IntFlag 位标志**
`class <名称>(enum.IntFlag):`
```python
# IntFlag 支持位运算
class Perm(enum.IntFlag):
    R = 4
    W = 2
    X = 1

p = Perm.R | Perm.W
print(Perm.R in p)
```

---

## StrEnum（3.11+）

**基本写法：StrEnum**
`class <名称>(enum.StrEnum):`
```python
# StrEnum 成员的 str() 返回成员名
class Status(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

print(str(Status.ACTIVE))    # active
print(Status.ACTIVE.upper()) # ACTIVE
```

---

## auto 自动赋值

**基本写法：auto 自动赋值**
`<成员> = enum.auto()`
```python
# 使用 auto 自动生成值
class Color(enum.Enum):
    RED = enum.auto()
    GREEN = enum.auto()
    BLUE = enum.auto()
```

**基本写法：自定义 auto 生成器**
`enum.auto()` 配合 `_generate_next_value_`
```python
# 自定义 auto 生成逻辑
class Color(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    RED = enum.auto()
    GREEN = enum.auto()
```

---

## 唯一值与别名

**基本写法：@unique 强制唯一**
`@enum.unique`
```python
# 强制枚举值唯一
@enum.unique
class Color(enum.Enum):
    RED = 1
    GREEN = 2
```

**基本写法：别名**
`<别名> = <成员>`
```python
# 同值成员成为别名
class Color(enum.Enum):
    RED = 1
    CRIMSON = 1  # 别名指向 RED

print(Color.CRIMSON is Color.RED)
```

---

## Flag 与 auto 位运算

**基本写法：Flag**
`class <名称>(enum.Flag):`
```python
# Flag 支持位运算
class Permission(enum.Flag):
    R = enum.auto()
    W = enum.auto()
    X = enum.auto()

p = Permission.R | Permission.W
print(Permission.R in p)
```

**基本写法：组合成员**
`<成员1> | <成员2>`
```python
# 组合权限
RW = Permission.R | Permission.W
print(RW.value)
```

---

## 枚举方法

**基本写法：枚举自定义方法**
`class <枚举>(enum.Enum):\n    def <方法>(self):`
```python
# 枚举成员可定义方法
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    def is_primary(self):
        return self in (Color.RED, Color.GREEN, Color.BLUE)
```

**基本写法：__str__ 自定义**
`def __str__(self):`
```python
# 自定义枚举字符串表示
class Color(enum.Enum):
    RED = 1
    def __str__(self):
        return f"Color({self.name})"
```

---

## 枚举与 dataclass

**基本写法：Enum 结合 dataclass（3.12+）**
`class <类>(enum.Enum):`
```python
# 使用 dataclass 装饰枚举
from dataclasses import dataclass

@dataclass
class ItemData:
    name: str
    price: float

class Item(ItemData, enum.Enum):
    APPLE = ("apple", 1.5)
    BANANA = ("banana", 0.8)
```

---

## enum 成员属性

**基本写法：_value_ 与 _name_**
`<成员>._value_` | `<成员>._name_`
```python
# 访问成员的值与名称
print(Color.RED._value_)
print(Color.RED._name_)
```

**基本写法：__members__ 字典**
`<枚举>.__members__`
```python
# 获取所有成员的有序字典
for name, member in Color.__members__.items():
    print(name, member)
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
