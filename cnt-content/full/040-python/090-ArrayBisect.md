---
order: 900
title: Python array 与 bisect
module: python

category: '040-python'
difficulty: beginner
description: Python array 与 bisect 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## array 数组

**基本写法：创建数组**
`array.array(<类型码>, <可迭代>)`
```python
# 创建紧凑类型数组
import array

a = array.array("i", [1, 2, 3, 4])  # 有符号整数
b = array.array("f", [1.5, 2.5])     # 单精度浮点
d = array.array("d", [3.14])         # 双精度浮点
```

**基本写法：类型码**
`"i"` | `"f"` | `"d"` | `"b"` | `"B"` | `"u"`
```python
# 常用类型码
# b: signed char  B: unsigned char
# i: signed int   I: unsigned int
# f: float        d: double
# u: unicode char（已弃用）
a = array.array("i")
print(a.typecode)
```

**基本写法：追加元素**
`a.append(<值>)` | `a.extend(<可迭代>)`
```python
# 追加元素
a = array.array("i", [1, 2])
a.append(3)
a.extend([4, 5])
```

**基本写法：插入元素**
`a.insert(<索引>, <值>)`
```python
# 在指定位置插入
a.insert(0, 0)
```

**基本写法：从文件读取**
`a.fromfile(<文件>, <数量>)`
```python
# 从二进制文件读取到数组
with open("data.bin", "rb") as f:
    a.fromfile(f, 100)
```

**基本写法：写入文件**
`a.tofile(<文件>)`
```python
# 数组写入二进制文件
with open("data.bin", "wb") as f:
    a.tofile(f)
```

**基本写法：转换为列表**
`a.tolist()`
```python
# 数组转列表
print(a.tolist())
```

**基本写法：bytes 与 frombytes**
`a.tobytes()` | `a.frombytes(<字节>)`
```python
# 数组与字节转换
data = a.tobytes()
a2 = array.array("i")
a2.frombytes(data)
```

**基本写法：反转与缓冲**
`a.reverse()` | `a.buffer_info()`
```python
# 反转数组与获取内存信息
a.reverse()
print(a.buffer_info())  # (地址, 长度)
```

---

## bisect 有序列表

**基本写法：bisect 查找插入位置**
`bisect.bisect(<有序列表>, <值>)`
```python
# 查找保持有序的插入位置
import bisect

a = [1, 3, 5, 7, 9]
print(bisect.bisect(a, 4))  # 2
```

**基本写法：bisect_left 左侧插入**
`bisect.bisect_left(<列表>, <值>)`
```python
# 返回左侧插入点
print(bisect.bisect_left(a, 5))  # 2
```

**基本写法：bisect_right 右侧插入**
`bisect.bisect_right(<列表>, <值>)`
```python
# 返回右侧插入点
print(bisect.bisect_right(a, 5))  # 3
```

**基本写法：insort 插入保持有序**
`bisect.insort(<列表>, <值>)`
```python
# 插入元素并保持有序
bisect.insort(a, 4)
print(a)  # [1, 3, 4, 5, 7, 9]
```

**基本写法：insort_left 左侧插入**
`bisect.insort_left(<列表>, <值>)`
```python
# 插入到左侧
bisect.insort_left(a, 5)
```

**基本写法：insort_right 右侧插入**
`bisect.insort_right(<列表>, <值>)`
```python
# 插入到右侧（默认）
bisect.insort_right(a, 5)
```

**基本写法：限定范围查找**
`bisect.bisect(<列表>, <值>, lo=<起>, hi=<止>)`
```python
# 限定查找范围
print(bisect.bisect(a, 4, lo=1, hi=4))
```

---

## bisect 应用

**基本写法：分级映射**
`bisect.bisect` 配合列表
```python
# 按分数定级
def grade(score):
    breakpoints = [60, 70, 80, 90]
    grades = "FDCBA"
    i = bisect.bisect(breakpoints, score)
    return grades[i]

print(grade(85))  # B
```

**基本写法：优先队列（有序插入）**
`bisect.insort`
```python
# 用 bisect 维护有序队列
class SortedQueue:
    def __init__(self):
        self._data = []
    def push(self, x):
        bisect.insort(self._data, x)
    def pop(self):
        return self._data.pop(0)
```

---

## array 与 list 区别

**基本写法：内存占用对比**
`sys.getsizeof(<对象>)`
```python
# array 比 list 节省内存
import sys
lst = list(range(1000))
arr = array.array("i", range(1000))
print(sys.getsizeof(lst))  # 较大
print(sys.getsizeof(arr))  # 较小
```

---

## array 切片与迭代

**基本写法：切片**
`a[<起>:<止>]`
```python
# 数组切片返回新数组
sub = a[1:3]
print(type(sub))  # <class 'array.array'>
```

**基本写法：迭代**
`for <元素> in a:`
```python
# 迭代数组元素
for x in a:
    print(x)
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
