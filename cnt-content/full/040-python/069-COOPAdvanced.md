---
order: 690
title: Python 面向对象进阶
module: python

category: '040-python'
difficulty: beginner
description: Python 面向对象进阶 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 抽象基类

**换行写法：定义抽象基类**
`from abc import ABC, abstractmethod`
`class <类名>(ABC):`
`    @abstractmethod`
`    def <方法名>(self): <语句>`

```python
# 定义抽象基类
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

---

**基本写法：实现抽象基类**
`class <子类>(<抽象基类>): def <抽象方法>(self): <语句>`

```python
# 实现抽象基类
class Dog(Animal):
    def speak(self):
        return "Woof!"
```

---

## 数据类

**换行写法：使用 dataclass**
`from dataclasses import dataclass`
`@dataclass`
`class <类名>:`
`    <字段1>: <类型>`
`    <字段2>: <类型>`

```python
# 使用 dataclass 装饰器
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

---

**换行写法：带默认值的 dataclass**
`@dataclass`
`class <类名>:`
`    <字段1>: <类型>`
`    <字段2>: <类型> = <默认值>`

```python
# 带默认值的 dataclass
@dataclass
class User:
    name: str
    age: int = 18
    active: bool = True
```

---

**换行写法：使用 field() 设置默认值**
`from dataclasses import dataclass, field`
`@dataclass`
`class <类名>:`
`    <字段>: <类型> = field(default_factory=<工厂>)`

```python
# 使用 field() 设置可变默认值
from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)
```

---

## 封装与访问控制

**基本写法：使用单下划线表示受保护**
`self._<属性> = <值>`

```python
# 使用单下划线表示受保护属性
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
```

---

**基本写法：使用双下划线表示私有**
`self.__<属性> = <值>`

```python
# 使用双下划线表示私有属性（名称重整）
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
```

---

**基本写法：提供公共访问方法**
`def get_<属性>(self): return self.__<属性>`

```python
# 提供公共方法访问私有属性
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

---

**基本写法：提供公共修改方法**
`def set_<属性>(self, <值>): self.__<属性> = <值>`

```python
# 提供公共方法修改私有属性
class BankAccount:
    def set_balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance
```

---

## 组合与聚合

**换行写法：使用组合**
`class <类名>:`
`    def __init__(self):`
`        self.<组件> = <其他类>()`

```python
# 使用组合关系
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()
```

---

## 多态

**基本写法：多态实现**
`def <函数>(<参数>: <类型>): <参数>.<方法>()`

```python
# 多态实现（不同类调用相同方法）
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    return animal.speak()
```

---

## 元类

**换行写法：使用 type() 动态创建类**
`<类名> = type("<类名>", (<父类>,), {<属性>: <值>})`

```python
# 使用 type() 动态创建类
Dog = type("Dog", (), {"bark": lambda self: "Woof!"})
dog = Dog()
```

---

**换行写法：自定义元类**
`class <元类名>(type):`
`    def __new__(mcs, name, bases, namespace): <语句>`

```python
# 自定义元类
class MyMeta(type):
    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class MyClass(metaclass=MyMeta):
    pass
```

---

## 描述符

**换行写法：自定义描述符**
`class <描述符类>:`
`    def __get__(self, obj, objtype): <语句>`
`    def __set__(self, obj, value): <语句>`

```python
# 自定义描述符
class ValidatedAttribute:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Must be integer")
        obj.__dict__[self.name] = value
```

---

## 类装饰器

**换行写法：使用类装饰器**
`def <装饰器名>(cls): <修改类> return <类>`

```python
# 使用类装饰器添加方法
def add_method(cls):
    cls.new_method = lambda self: "New method"
    return cls

@add_method
class MyClass:
    pass
```

---

## __slots__ 优化

**基本写法：使用 __slots__ 限制属性**
`class <类名>: __slots__ = [<属性1>, <属性2>]`

```python
# 使用 __slots__ 限制实例属性
class Point:
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 枚举类

**换行写法：定义枚举类**
`from enum import Enum`
`class <枚举类>(Enum):`
`    <成员1> = <值>`
`    <成员2> = <值>`

```python
# 定义枚举类
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

---

**基本写法：访问枚举成员**
`<枚举类>.<成员>`

```python
# 访问枚举成员
print(Color.RED)
print(Color.RED.value)
```

---

**基本写法：通过值获取枚举成员**
`<枚举类>(<值>)`

```python
# 通过值获取枚举成员
print(Color(1))
```

---

**基本写法：遍历枚举**
`for <变量> in <枚举类>: <语句>`

```python
# 遍历枚举的所有成员
for color in Color:
    print(color.name, color.value)
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
