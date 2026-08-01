---
order: 920
title: Python decimal 与 fractions
module: python

category: '040-python'
difficulty: beginner
description: Python decimal 与 fractions 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## decimal Decimal

**基本写法：创建 Decimal**
`decimal.Decimal(<数值>)`
```python
# 精确十进制运算
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)  # 0.3，精确
```

**基本写法：从整数创建**
`Decimal(<整数>)`
```python
# 从整数创建
d = Decimal(100)
```

**基本写法：从浮点创建（谨慎）**
`Decimal.from_float(<浮点>)`
```python
# 从 float 创建会保留浮点误差
print(Decimal.from_float(0.1))  # 0.1000000000000000055...
```

**基本写法：算术运算**
`Decimal + - * /`
```python
# 支持所有算术运算
x = Decimal("1.5")
y = Decimal("2.5")
print(x + y, x * y, x / y)
```

**基本写法：比较**
`Decimal < > ==`
```python
# 精确比较
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True
```

---

## Context 上下文

**基本写法：getcontext 获取上下文**
`decimal.getcontext()`
```python
# 获取当前十进制上下文
from decimal import getcontext

ctx = getcontext()
print(ctx.prec)  # 28 位精度
```

**基本写法：设置精度**
`getcontext().prec = <位数>`
```python
# 设置全局精度
getcontext().prec = 6
print(Decimal(1) / Decimal(7))  # 0.142857
```

**基本写法：设置舍入**
`getcontext().rounding = <常量>`
```python
# 舍入模式
from decimal import ROUND_HALF_UP, ROUND_DOWN

getcontext().rounding = ROUND_HALF_UP
```

**基本写法：localcontext 局部上下文**
`with decimal.localcontext() as ctx:`
```python
# 临时上下文
import decimal

with decimal.localcontext() as ctx:
    ctx.prec = 10
    print(Decimal(1) / Decimal(7))
```

**基本写法：舍入方法**
`<Decimal>.quantize(<模式>, rounding=<舍入>)`
```python
# 量化到指定小数位
d = Decimal("3.14159")
print(d.quantize(Decimal("0.01")))  # 3.14
```

---

## Decimal 特殊值

**基本写法：Infinity 与 NaN**
`Decimal("Infinity")` | `Decimal("NaN")`
```python
# 无穷与 NaN
print(Decimal("Infinity"))
print(Decimal("NaN"))
print(Decimal("-Infinity"))
```

**基本写法：signed 零**
`Decimal("-0")`
```python
# 带符号零
print(Decimal("-0") + Decimal("0"))  # 0
```

---

## fractions Fraction

**基本写法：创建分数**
`fractions.Fraction(<分子>, <分母>)`
```python
# 精确分数运算
from fractions import Fraction

f = Fraction(1, 3)
print(f)  # 1/3
```

**基本写法：从字符串创建**
`Fraction(<字符串>)`
```python
# 从字符串创建
f = Fraction("3/7")
f2 = Fraction("1.5")  # 3/2
```

**基本写法：从 Decimal 创建**
`Fraction(<Decimal>)`
```python
# 从 Decimal 创建
f = Fraction(Decimal("0.1"))  # 1/10
```

**基本写法：算术运算**
`Fraction + - * /`
```python
# 分数运算自动约分
a = Fraction(1, 2)
b = Fraction(1, 3)
print(a + b)  # 5/6
print(a * b)  # 1/6
```

**基本写法：约分**
`Fraction(<分子>, <分母>)`
```python
# 自动约分
print(Fraction(4, 6))  # 2/3
```

---

## Fraction 属性与方法

**基本写法：分子分母**
`f.numerator` | `f.denominator`
```python
# 获取分子分母
f = Fraction(3, 4)
print(f.numerator, f.denominator)  # 3 4
```

**基本写法：转 float**
`float(f)`
```python
# 转换为浮点
print(float(Fraction(1, 3)))  # 0.333...
```

**基本写法：limit_denominator 限制分母**
`f.limit_denominator(<最大分母>)`
```python
# 限制分母上限，常用浮点转分数
print(Fraction(0.5).limit_denominator(100))  # 1/2
print(Fraction(3.14159).limit_denominator(10))  # 22/7
```

---

## 应用场景

**基本写法：货币计算**
`Decimal` 用于货币
```python
# 货币精确计算
price = Decimal("19.99")
qty = Decimal("3")
total = price * qty
print(total.quantize(Decimal("0.00")))  # 59.97
```

**基本写法：百分比计算**
`Fraction` 用于比例
```python
# 比例运算保持精度
tax_rate = Fraction(5, 100)
amount = Decimal("100.00")
tax = amount * Decimal(tax_rate.numerator) / Decimal(tax_rate.denominator)
print(tax)
```

---

## 数值类型转换

**基本写法：Decimal 转 int**
`int(<Decimal>)`
```python
# 取整数部分
print(int(Decimal("3.99")))  # 3
```

**基本写法：Fraction 转 Decimal**
`Decimal(<Fraction>)`
```python
# 转换可能损失精度，建议先转字符串
f = Fraction(1, 3)
print(Decimal(f.numerator) / Decimal(f.denominator))
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
