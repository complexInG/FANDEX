---
order: 10
title: python 模块文档合集
module: 'python'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：040-python/001-VariableConstant.md ============ -->

# 变量与常量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量赋值

**基本写法：动态类型赋值**
`<变量> = <值>`

```python
# 基本变量赋值
x = 10
name = "Alice"
is_valid = True
```

---

**基本写法：动态类型改变**
`<变量> = <新类型的值>`

```python
# 变量 x 从整数变为字符串
x = "Hello"
```

---

## 链式赋值

**基本写法：多个变量指向同一对象**
`<变量1> = <变量2> = <值>`

```python
# 链式赋值，a、b、c 指向同一对象
a = b = c = 100
```

---

## 多重赋值（解包）

**单行写法：同时为多个变量赋值**
`<变量1>, <变量2> = <值1>, <值2>`

```python
# 多重赋值（单行写法）
x, y = 1, 2
```

---

**单行写法：解包列表或元组**
`<变量1>, <变量2>, <变量3> = <序列>`

```python
# 解包列表到多个变量
values = [3, 4, 5]
x, y, z = values
```

---

**基本写法：使用星号收集剩余值**
`<变量1>, *<变量2> = <序列>`

```python
# 使用星号收集剩余值到列表
first, *rest = [1, 2, 3, 4, 5]
```

---

## 内存地址与引用

**基本写法：查看对象内存地址**
`id(<对象>)`

```python
# 查看变量的内存地址
x = 10
print(id(x))
```

---

## 变量作用域

**基本写法：局部作用域变量**
`def <函数>(): <局部变量> = <值>`

```python
# 函数内部定义的局部变量
def my_function():
    local_var = "local"
    print(local_var)
```

---

**基本写法：全局作用域变量**
`<全局变量> = <值>`

```python
# 模块级别定义的全局变量
global_var = "global"
```

---

**基本写法：使用 global 声明修改全局变量**
`global <变量名>`

```python
# 在函数内部声明并修改全局变量
count = 0

def increment():
    global count
    count += 1
```

---

**基本写法：使用 nonlocal 声明修改嵌套作用域变量**
`nonlocal <变量名>`

```python
# 在内部函数中修改外层函数的变量
def outer_function():
    count = 0
    def inner_function():
        nonlocal count
        count += 1
    inner_function()
```

---

## 引用计数

**基本写法：查看对象引用计数**
`sys.getrefcount(<对象>)`

```python
# 查看对象的引用计数
import sys
x = [1, 2, 3]
print(sys.getrefcount(x))
```

---

## 常量命名约定

**基本写法：常量使用全大写字母和下划线**
`<UPPER_CASE_NAME> = <值>`

```python
# 常量命名约定（全大写加下划线）
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159265359
```

---

## 实现真正的常量

**换行写法：使用类实现不可修改常量**
`class <常量类>:`
`    <常量1> = <值>`
`    <常量2> = <值>`
`    def __setattr__(self, name, value): raise AttributeError(...)`

```python
# 通过 __setattr__ 禁止修改的常量类
class Constants:
    MAX_CONNECTIONS = 100
    DEFAULT_TIMEOUT = 30

    def __setattr__(self, name, value):
        raise AttributeError("Constants cannot be modified")
```

---

## 枚举常量

**换行写法：使用 enum 模块定义枚举常量**
`class <枚举类>(Enum):`
`    <成员1> = <值>`
`    <成员2> = <值>`

```python
# 使用 Enum 定义一组相关常量
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

---

**换行写法：使用 auto() 自动赋值**
`class <枚举类>(Enum):`
`    <成员1> = auto()`
`    <成员2> = auto()`

```python
# 使用 auto() 自动生成枚举值
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
```

---

**基本写法：访问枚举成员**
`<枚举类>.<成员>`

```python
# 访问枚举成员及其值
print(Color.RED)
print(Color.RED.value)
```

---

**基本写法：遍历枚举**
`for <变量> in <枚举类>: <语句>`

```python
# 遍历枚举的所有成员
for color in Color:
    print(color.name, color.value)
```

---

## 变量交换

**单行写法：两个变量交换**
`<变量1>, <变量2> = <变量2>, <变量1>`

```python
# 使用元组解包交换两个变量
a, b = 1, 2
a, b = b, a
```

---

**单行写法：三个变量交换**
`<变量1>, <变量2>, <变量3> = <变量3>, <变量1>, <变量2>`

```python
# 三个变量循环交换
x, y, z = 1, 2, 3
x, y, z = z, x, y
```

---

**基本写法：列表元素交换**
`<列表>[<索引1>], <列表>[<索引2>] = <列表>[<索引2>], <列表>[<索引1>]`

```python
# 交换列表中两个位置的元素
lst = [1, 2, 3, 4]
lst[0], lst[1] = lst[1], lst[0]
```

---



<!-- ============ 文档分隔线：040-python/002-ProgramStructureBasicSyntax.md ============ -->

# 程序结构与基本语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块文档字符串

**基本写法：模块级文档字符串**
`"""<模块描述>"""`

```python
# 模块开头的文档字符串
"""用户管理模块，提供用户增删改查功能"""
```

---

## 导入语句

**单行写法：导入单个模块**
`import <模块>`

```python
# 导入 math 模块
import math
```

---

**单行写法：从模块导入指定对象**
`from <模块> import <对象>`

```python
# 从 datetime 模块导入 datetime 类
from datetime import datetime
```

---

**换行写法：从模块导入多个对象**
`from <模块> import (<对象1>, <对象2>, <对象3>)`

```python
# 从 typing 模块导入多个类型（换行书写）
from typing import (
    List,
    Dict,
    Optional,
    Union,
)
```

---

## 全局变量定义

**基本写法：模块级全局变量**
`<变量> = <值>`

```python
# 定义模块级全局常量
PI = math.pi
MAX_VALUE = 100
```

---

## 函数定义

**基本写法：定义函数**
`def <函数名>(<参数>): <语句>`

```python
# 定义计算圆面积的函数
def calculate_area(radius):
    return PI * (radius ** 2)
```

---

## 类定义

**单行写法：简单类定义**
`class <类名>: <类体>`

```python
# 定义空类作为占位符
class Placeholder: pass
```

---

**换行写法：包含属性和方法的类定义**
`class <类名>:`
`    def __init__(self, <参数>): <初始化>`
`    def <方法>(self): <语句>`

```python
# 定义 Circle 类，包含初始化方法和实例方法
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return calculate_area(self.radius)
```

---

## 主函数与入口点

**基本写法：定义主函数**
`def main(): <语句>`

```python
# 定义程序主函数
def main():
    circle = Circle(5)
    print(f"Area: {circle.area():.2f}")
```

---

**基本写法：标准入口点检查**
`if __name__ == "__main__": <主逻辑>`

```python
# 模块作为脚本运行时执行主函数
if __name__ == "__main__":
    main()
```

---

## 缩进规则

**基本写法：使用 4 个空格定义代码块**
`<语句>:`
`    <4 空格缩进的语句>`

```python
# 使用 4 个空格缩进定义代码块
def example():
    if True:
        print("Inside if")
        for i in range(3):
            print(f"Loop {i}")
    print("Outside if")
```

---

## 注释规范

**基本写法：单行注释**
`# <注释内容>`

```python
# 这是一个单行注释
age = 30  # 行尾注释
```

---

**基本写法：函数文档字符串**
`def <函数>(<参数>): """<文档内容>"""`

```python
# 为函数添加文档字符串
def calculate_area(radius):
    """计算圆的面积"""
    return math.pi * (radius ** 2)
```

---

**换行写法：多行文档字符串**
`def <函数>(<参数>):`
`    """`
`    <描述>`
`    Args: <参数说明>`
`    Returns: <返回值说明>`
`    """`

```python
# 多行文档字符串（换行书写）
def calculate_area(radius):
    """
    计算圆的面积
    Args:
        radius: 圆的半径
    Returns:
        圆的面积
    """
    return math.pi * (radius ** 2)
```

---

## 标识符规则

**基本写法：合法标识符命名**
`<标识符> = <值>`

```python
# 合法的标识符命名
user_name = "Alice"
_total = 100
PI = 3.14
```

---

## 命名规范

**基本写法：变量和函数使用 snake_case**
`<变量> = <snake_case>`

```python
# 变量使用 snake_case 命名
user_name = "Alice"
```

---

**基本写法：函数使用 snake_case**
`def <snake_case>(): <语句>`

```python
# 函数使用 snake_case 命名
def calculate_total():
    pass
```

---

**基本写法：常量使用 UPPER_SNAKE_CASE**
`<UPPER_CASE> = <值>`

```python
# 常量使用全大写加下划线
MAX_VALUE = 100
DEFAULT_TIMEOUT = 30
```

---

**基本写法：类名使用 PascalCase**
`class <PascalCase>: <类体>`

```python
# 类名使用 PascalCase 命名
class UserProfile:
    pass
```

---

**基本写法：私有属性使用下划线前缀**
`self._<属性> = <值>`

```python
# 私有属性使用单下划线前缀
class MyClass:
    def __init__(self):
        self._private_var = 0
```

---

## 语句换行

**单行写法：使用反斜杠显式换行**
`<语句> \`
`    <续行>`

```python
# 使用反斜杠实现显式换行
long_string = "This is a very long string that " \
    "spans multiple lines using backslash"
```

---

**换行写法：在括号内隐式换行**
`<表达式> (`
`    <内容>`
`)`

```python
# 在括号内隐式换行（推荐写法）
long_string = (
    "This is a very long string that "
    "spans multiple lines using parentheses"
)
```

---

**换行写法：列表多行书写**
`<列表> = [`
`    <元素1>,`
`    <元素2>,`
`]`

```python
# 列表换行书写
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9,
]
```

---

**换行写法：函数调用多行书写**
`<函数>(`
`    <参数1>=<值1>,`
`    <参数2>=<值2>,`
`)`

```python
# 函数调用换行书写
result = calculate(
    param1=value1,
    param2=value2,
    param3=value3,
)
```

---

## 分号与空语句

**基本写法：分号分隔多个语句**
`<语句1>; <语句2>`

```python
# 使用分号在一行分隔多个语句（不推荐）
x = 1; y = 2; print(x + y)
```

---

**基本写法：pass 空语句占位**
`pass`

```python
# 使用 pass 作为函数体占位符
def placeholder_function():
    pass
```

---

**基本写法：pass 用于类定义占位**
`class <类名>: pass`

```python
# 使用 pass 作为类体占位符
class PlaceholderClass:
    pass
```

---

**基本写法：pass 用于条件语句占位**
`if <条件>: pass`

```python
# 使用 pass 作为条件语句体占位符
if condition:
    pass
```

---

## 多行语句组合

**单行写法：元组解包多行赋值**
`(<变量1>, <变量2>, <变量3>) = (<值1>, <值2>, <值3>)`

```python
# 使用元组解包进行多变量赋值
(a, b, c) = (1, 2, 3)
```

---

**换行写法：多行字典定义**
`<字典> = {`
`    <键1>: <值1>,`
`    <键2>: <值2>,`
`}`

```python
# 字典换行书写
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
}
```

---

**换行写法：多行条件表达式**
`if (<条件1> and`
`    <条件2>):`
`    <语句>`

```python
# 多行条件表达式（换行书写）
if (condition1 and
    condition2):
    do_something()
```

---



<!-- ============ 文档分隔线：040-python/003-FunctionDetailed.md ============ -->

# 函数详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数定义

**基本写法：定义无参函数**
`def <函数名>(): <语句>`

```python
# 定义无参函数
def greet():
    print("Hello, World!")
```

---

**基本写法：定义带参函数**
`def <函数名>(<参数>): <语句>`

```python
# 定义带参函数
def greet(name):
    print(f"Hello, {name}!")
```

---

**单行写法：定义单行函数**
`def <函数名>(<参数>): return <表达式>`

```python
# 定义单行函数
def square(x): return x * x
```

---

**换行写法：定义多参数函数**
`def <函数名>(`
`    <参数1>,`
`    <参数2>,`
`    <参数3>,`
`): <语句>`

```python
# 定义多参数函数（换行书写）
def create_user(
    name,
    age,
    email,
):
    return {"name": name, "age": age, "email": email}
```

---

## 函数调用

**基本写法：调用无参函数**
`<函数名>()`

```python
# 调用无参函数
greet()
```

---

**基本写法：按位置传参调用**
`<函数名>(<参数1>, <参数2>)`

```python
# 按位置传参调用函数
greet("Alice")
```

---

**基本写法：按关键字传参调用**
`<函数名>(<参数名>=<值>)`

```python
# 按关键字传参调用函数
greet(name="Alice")
```

---

**换行写法：多参数函数调用**
`<函数名>(`
`    <参数1>=<值1>,`
`    <参数2>=<值2>,`
`)`

```python
# 多参数函数调用（换行书写）
create_user(
    name="Alice",
    age=30,
    email="alice@example.com",
)
```

---

## 返回值

**基本写法：返回单个值**
`return <值>`

```python
# 返回单个值
def add(a, b):
    return a + b
```

---

**单行写法：返回多个值（元组）**
`return <值1>, <值2>, <值3>`

```python
# 返回多个值（作为元组）
def get_user_info():
    return "Alice", 30, "alice@example.com"
```

---

**基本写法：无返回值（隐式返回 None）**
`def <函数名>(): <语句>`

```python
# 无返回值的函数（隐式返回 None）
def print_message(msg):
    print(msg)
```

---

**基本写法：显式返回 None**
`return None`

```python
# 显式返回 None
def process(data):
    if not data:
        return None
    return data
```

---

## 默认参数

**基本写法：定义带默认值的参数**
`def <函数名>(<参数>=<默认值>): <语句>`

```python
# 定义带默认值的参数
def greet(name="World"):
    print(f"Hello, {name}!")
```

---

**基本写法：混合必选和默认参数**
`def <函数名>(<必选参数>, <参数>=<默认值>): <语句>`

```python
# 混合必选参数和默认参数
def create_user(name, age=18, active=True):
    return {"name": name, "age": age, "active": active}
```

---

## 可变参数

**基本写法：使用 *args 收集位置参数**
`def <函数名>(*<args>): <语句>`

```python
# 使用 *args 收集位置参数
def sum_all(*args):
    return sum(args)
```

---

**基本写法：使用 **kwargs 收集关键字参数**
`def <函数名>(**<kwargs>): <语句>`

```python
# 使用 **kwargs 收集关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

---

**换行写法：组合使用必选、默认、可变参数**
`def <函数名>(`
`    <必选参数>,`
`    <参数>=<默认值>,`
`    *<args>,`
`    **<kwargs>,`
`): <语句>`

```python
# 组合使用各类参数
def create_profile(
    name,
    age=18,
    *hobbies,
    **metadata,
):
    profile = {"name": name, "age": age, "hobbies": hobbies}
    profile.update(metadata)
    return profile
```

---

## 参数解包

**基本写法：使用 * 解包列表或元组**
`<函数名>(*<序列>)`

```python
# 使用 * 解包列表作为位置参数
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))
```

---

**基本写法：使用 ** 解包字典**
`<函数名>(**<字典>)`

```python
# 使用 ** 解包字典作为关键字参数
def greet(name, greeting):
    print(f"{greeting}, {name}!")

params = {"name": "Alice", "greeting": "Hi"}
greet(**params)
```

---

## 仅关键字参数

**基本写法：使用 * 强制关键字参数**
`def <函数名>(*, <参数>): <语句>`

```python
# 使用 * 强制后面的参数为关键字参数
def connect(host, *, port, timeout):
    print(f"Connecting to {host}:{port}, timeout={timeout}")
```

---

**基本写法：在 *args 后定义关键字参数**
`def <函数名>(*<args>, <参数>=<默认值>): <语句>`

```python
# 在 *args 后定义仅关键字参数
def func(*args, debug=False):
    if debug:
        print(f"args: {args}")
    return sum(args)
```

---

## 仅位置参数

**基本写法：使用 / 强制位置参数**
`def <函数名>(<参数1>, <参数2>, /): <语句>`

```python
# 使用 / 强制前面的参数为位置参数
def divide(a, b, /):
    return a / b
```

---

**换行写法：组合位置参数和关键字参数**
`def <函数名>(`
`    <位置参数>, /,`
`    <普通参数>,`
`    *, <关键字参数>,`
`): <语句>`

```python
# 组合位置参数、普通参数和关键字参数
def process_data(
    data, /,
    transform=None,
    *,
    validate=False,
):
    if transform:
        data = transform(data)
    if validate:
        data = validate(data)
    return data
```

---

## Lambda 表达式

**单行写法：基本 lambda 表达式**
`lambda <参数>: <表达式>`

```python
# 基本 lambda 表达式
square = lambda x: x * x
print(square(5))
```

---

**单行写法：多参数 lambda 表达式**
`lambda <参数1>, <参数2>: <表达式>`

```python
# 多参数 lambda 表达式
add = lambda a, b: a + b
print(add(3, 5))
```

---

**单行写法：带默认值的 lambda 表达式**
`lambda <参数>=<默认值>: <表达式>`

```python
# 带默认值的 lambda 表达式
greet = lambda name="World": f"Hello, {name}!"
print(greet())
```

---

**基本写法：在 sorted() 中使用 lambda**
`sorted(<可迭代对象>, key=lambda <参数>: <表达式>)`

```python
# 在 sorted() 中使用 lambda 作为 key
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
```

---

**基本写法：在 map() 中使用 lambda**
`map(lambda <参数>: <表达式>, <可迭代对象>)`

```python
# 在 map() 中使用 lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
```

---

**基本写法：在 filter() 中使用 lambda**
`filter(lambda <参数>: <条件>, <可迭代对象>)`

```python
# 在 filter() 中使用 lambda
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

## 高阶函数

**基本写法：函数作为参数**
`def <函数名>(<函数参数>, <其他参数>): <语句>`

```python
# 函数作为参数传递
def apply(func, value):
    return func(value)

result = apply(lambda x: x * 2, 5)
```

---

**基本写法：函数作为返回值**
`def <函数名>(): return <函数>`

```python
# 函数作为返回值
def make_multiplier(factor):
    return lambda x: x * factor

double = make_multiplier(2)
print(double(5))
```

---

**基本写法：使用 map() 函数**
`map(<函数>, <可迭代对象>)`

```python
# 使用 map() 对可迭代对象应用函数
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
```

---

**基本写法：使用 filter() 函数**
`filter(<函数>, <可迭代对象>)`

```python
# 使用 filter() 过滤可迭代对象
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

**基本写法：使用 reduce() 函数**
`reduce(<函数>, <可迭代对象>)`

```python
# 使用 reduce() 累积计算
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
```

---

## 闭包

**换行写法：定义闭包**
`def <外部函数>(<参数>):`
`    def <内部函数>(<参数>): <语句>`
`    return <内部函数>`

```python
# 定义闭包
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
```

---

**基本写法：使用闭包**
`<变量> = <外部函数>()`

```python
# 使用闭包
counter = make_counter()
print(counter())
print(counter())
```

---

## 递归

**基本写法：递归函数**
`def <函数名>(<参数>): if <条件>: return <基线> else: return <递归调用>`

```python
# 递归计算阶乘
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

---

**基本写法：尾递归优化（Python 不支持，仅作示例）**
`def <函数名>(<参数>, <累加器>): if <条件>: return <累加器> else: return <递归调用>`

```python
# 尾递归形式的阶乘（Python 不优化）
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    else:
        return factorial_tail(n - 1, n * acc)
```

---

## 函数注解

**基本写法：参数类型注解**
`def <函数名>(<参数>: <类型>): <语句>`

```python
# 参数类型注解
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

---

**基本写法：返回值类型注解**
`def <函数名>(<参数>) -> <返回类型>: <语句>`

```python
# 返回值类型注解
def add(a: int, b: int) -> int:
    return a + b
```

---

**基本写法：使用 Optional 类型注解**
`def <函数名>(<参数>: Optional[<类型>]) -> <类型>: <语句>`

```python
# 使用 Optional 类型注解
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:
    if user_id == 1:
        return {"id": 1, "name": "Alice"}
    return None
```

---

**基本写法：使用 List 类型注解**
`def <函数名>(<参数>: List[<类型>]) -> <类型>: <语句>`

```python
# 使用 List 类型注解
from typing import List

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)
```

---

**基本写法：使用 Dict 类型注解**
`def <函数名>(<参数>: Dict[<键类型>, <值类型>]) -> <类型>: <语句>`

```python
# 使用 Dict 类型注解
from typing import Dict

def get_value(data: Dict[str, int], key: str) -> int:
    return data.get(key, 0)
```

---

**基本写法：使用 Union 类型注解**
`def <函数名>(<参数>: Union[<类型1>, <类型2>]) -> <类型>: <语句>`

```python
# 使用 Union 类型注解
from typing import Union

def process(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data
```

---

## 函数属性

**基本写法：访问函数注解**
`<函数>.__annotations__`

```python
# 访问函数的注解信息
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet.__annotations__)
```

---

**基本写法：访问函数文档字符串**
`<函数>.__doc__`

```python
# 访问函数的文档字符串
def greet(name):
    """向用户打招呼"""
    return f"Hello, {name}!"

print(greet.__doc__)
```

---

**基本写法：访问函数名**
`<函数>.__name__`

```python
# 访问函数的名称
def my_function():
    pass

print(my_function.__name__)
```

---

## 偏函数

**基本写法：使用 partial 创建偏函数**
`partial(<函数>, <固定参数>)`

```python
# 使用 partial 创建偏函数
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))
```

---

## 函数缓存

**基本写法：使用 lru_cache 缓存函数结果**
`@lru_cache(maxsize=<n>)`

```python
# 使用 lru_cache 缓存函数结果
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

**基本写法：使用 cache 无限缓存**
`@cache`

```python
# 使用 cache 无限缓存
from functools import cache

@cache
def expensive_computation(n):
    return sum(i * i for i in range(n))
```

---



<!-- ============ 文档分隔线：040-python/004-BasicDataType.md ============ -->

# 基础数据类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 整数类型

**基本写法：十进制整数**
`<十进制> = 123`

```python
# 十进制整数
x = 123
```

---

**基本写法：二进制整数**
`<二进制> = 0b<二进制串>`

```python
# 二进制整数（以 0b 开头）
y = 0b1010
```

---

**基本写法：八进制整数**
`<八进制> = 0o<八进制串>`

```python
# 八进制整数（以 0o 开头）
z = 0o123
```

---

**基本写法：十六进制整数**
`<十六进制> = 0x<十六进制串>`

```python
# 十六进制整数（以 0x 开头）
p = 0x1A
```

---

## 整数运算

**基本写法：加法运算**
`<操作数1> + <操作数2>`

```python
# 整数加法
addition = 10 + 5
```

---

**基本写法：整除运算**
`<操作数1> // <操作数2>`

```python
# 整除（向下取整）
floor_division = 10 // 3
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`

```python
# 取模（求余数）
modulo = 10 % 3
```

---

**基本写法：幂运算**
`<操作数1> ** <操作数2>`

```python
# 幂运算
power = 2 ** 3
```

---

**基本写法：复合赋值运算**
`<变量> <运算符>= <值>`

```python
# 复合赋值运算符
x = 10
x += 5
```

---

## 浮点数类型

**基本写法：普通浮点数**
`<浮点数> = <小数>`

```python
# 普通浮点数
pi = 3.14159
```

---

**基本写法：科学记数法**
`<科学记数法> = <尾数>e<指数>`

```python
# 科学记数法
avogadro = 6.022e23
```

---

## 复数类型

**基本写法：复数字面量**
`<复数> = <实部> + <虚部>j`

```python
# 复数定义
c1 = 3 + 4j
```

---

**基本写法：使用 complex() 函数**
`complex(<实部>, <虚部>)`

```python
# 使用 complex() 创建复数
c2 = complex(2, 5)
```

---

**基本写法：访问复数实部**
`<复数>.real`

```python
# 获取复数的实部
print(c1.real)
```

---

**基本写法：访问复数虚部**
`<复数>.imag`

```python
# 获取复数的虚部
print(c1.imag)
```

---

## 数学函数

**基本写法：导入 math 模块**
`import math`

```python
# 导入数学模块
import math
```

---

**基本写法：调用 math 函数**
`math.<函数>(<参数>)`

```python
# 计算平方根
print(math.sqrt(16))
```

---

**基本写法：向下取整**
`math.floor(<浮点数>)`

```python
# 向下取整
print(math.floor(3.9))
```

---

**基本写法：向上取整**
`math.ceil(<浮点数>)`

```python
# 向上取整
print(math.ceil(3.1))
```

---

## 字符串

**基本写法：单引号字符串**
`'<字符串>'`

```python
# 单引号字符串
s1 = 'Hello, World!'
```

---

**基本写法：双引号字符串**
`"<字符串>"`

```python
# 双引号字符串
s2 = "Hello, World!"
```

---

**换行写法：三引号多行字符串**
`'''<多行字符串>'''`

```python
# 三引号字符串（支持多行）
s3 = '''Hello,
World!'''
```

---

**基本写法：原始字符串**
`r'<字符串>'`

```python
# 原始字符串（不转义）
s4 = r'C:\path\to\file'
```

---

**基本写法：字节字符串**
`b'<字符串>'`

```python
# 字节字符串
s5 = b'Hello'
```

---

## 字符串拼接

**基本写法：使用 + 运算符拼接**
`<字符串1> + <字符串2>`

```python
# 使用 + 拼接字符串
full_name = "Alice" + " " + "Smith"
```

---

**基本写法：使用 * 运算符重复**
`<字符串> * <次数>`

```python
# 使用 * 重复字符串
print("Hello" * 3)
```

---

## 字符串切片

**基本写法：获取单个字符**
`<字符串>[<索引>]`

```python
# 获取指定位置的字符
print(s[0])
```

---

**基本写法：切片操作**
`<字符串>[<start>:<stop>:<step>]`

```python
# 切片获取子字符串
print(s[0:5])
```

---

**基本写法：反转字符串**
`<字符串>[::-1]`

```python
# 使用切片反转字符串
print(s[::-1])
```

---

## 字符串方法

**基本写法：转换为大写**
`<字符串>.upper()`

```python
# 转换为大写
print(s.upper())
```

---

**基本写法：查找子串位置**
`<字符串>.find(<子串>)`

```python
# 查找子串位置
print(s.find("World"))
```

---

**基本写法：替换子串**
`<字符串>.replace(<旧子串>, <新子串>)`

```python
# 替换字符串中的子串
print(s.replace("World", "Python"))
```

---

**基本写法：分割字符串**
`<字符串>.split(<分隔符>)`

```python
# 按分隔符分割字符串
print(s.split(", "))
```

---

**基本写法：连接字符串列表**
`<分隔符>.join(<字符串列表>)`

```python
# 使用分隔符连接字符串列表
print(", ".join(["Hello", "Python"]))
```

---

**基本写法：去除空白字符**
`<字符串>.strip()`

```python
# 去除两端空白字符
print(" Hello ".strip())
```

---

## 字符串格式化

**基本写法：f-string 格式化**
`f"<文本>{<表达式>}"`

```python
# f-string 基本用法
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

---

**基本写法：f-string 格式化选项**
`f"<文本>{<表达式>:<格式说明>}"`

```python
# f-string 浮点数格式化
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")
```

---

**基本写法：format() 方法**
`"<文本>{}".format(<参数>)`

```python
# 使用 format() 方法格式化
print("My name is {} and I am {} years old.".format("Alice", 30))
```

---

**基本写法：% 运算符格式化**
`"<格式>" % <值>`

```python
# C 风格 % 格式化
print("My name is %s and I am %d years old." % ("Alice", 30))
```

---

## 布尔类型

**基本写法：逻辑与运算**
`<表达式> and <表达式>`

```python
# 逻辑与运算
print(True and False)
```

---

**基本写法：逻辑或运算**
`<表达式> or <表达式>`

```python
# 逻辑或运算
print(True or False)
```

---

**基本写法：逻辑非运算**
`not <表达式>`

```python
# 逻辑非运算
print(not True)
```

---

**基本写法：布尔上下文判断**
`if <对象>: <语句>`

```python
# 在布尔上下文中判断对象真假
if "Hello":
    print("非空字符串为真")
```

---

## 空值 None

**基本写法：赋值为 None**
`<变量> = None`

```python
# 赋值为 None
x = None
```

---

**基本写法：使用 is 检查 None**
`<变量> is None`

```python
# 使用 is 运算符检查 None
x = None
print(x is None)
```

---

## 类型转换

**基本写法：转换为整数**
`int(<值>)`

```python
# 转换为整数
print(int("123"))
```

---

**基本写法：转换为浮点数**
`float(<值>)`

```python
# 转换为浮点数
print(float("3.14"))
```

---

**基本写法：转换为字符串**
`str(<值>)`

```python
# 转换为字符串
print(str(123))
```

---

**基本写法：转换为布尔值**
`bool(<值>)`

```python
# 转换为布尔值
print(bool(1))
```

---

**基本写法：转换为列表**
`list(<可迭代对象>)`

```python
# 转换为列表
print(list("Hello"))
```

---

**基本写法：转换为元组**
`tuple(<可迭代对象>)`

```python
# 转换为元组
print(tuple([1, 2, 3]))
```

---

**基本写法：转换为集合**
`set(<可迭代对象>)`

```python
# 转换为集合（去重）
print(set([1, 2, 3, 2, 1]))
```

---

**基本写法：转换为字典**
`dict(<键值对序列>)`

```python
# 转换为字典
print(dict([("a", 1), ("b", 2)]))
```

---

## 类型检查

**基本写法：获取对象类型**
`type(<对象>)`

```python
# 获取对象的类型
print(type(42))
```

---

**基本写法：检查对象是否为指定类型**
`isinstance(<对象>, <类型>)`

```python
# 检查对象是否为指定类型
print(isinstance(42, int))
```

---

**基本写法：检查是否为多种类型之一**
`isinstance(<对象>, (<类型1>, <类型2>))`

```python
# 检查对象是否为多种类型之一
print(isinstance(42, (int, float)))
```

---

## Python 3.13+ 新特性

**基本写法：type 参数支持复数形式**
`type(<对象>, complex)`

```python
# Python 3.13 type() 第三参数支持复数形式（用于复数类型判断）
x = 3 + 4j
print(type(x, complex))
```

---

**基本写法：Python 3.13 改进的错误消息**
`<表达式>  # 触发错误时高亮精确位置`

```python
# Python 3.13 改进的错误消息（更精确的错误定位）
# 字典键访问错误会精确高亮具体键名,而非整行
data = {"name": "Alice"}
# data["age"]  # 触发 KeyError 时错误消息高亮 "age" 字符串本身
```

---

**基本写法：Python 3.14 t-string 模板字符串**
`t"<文本>{<表达式>}"`

```python
# Python 3.14 t-string 模板字符串（返回 Template 对象,不立即求值）
name = "Alice"
template = t"Hello, {name}!"
```

---

**基本写法：Python 3.14 模板字符串渲染**
`<模板>.render(<上下文字典>)`

```python
# Python 3.14 模板字符串渲染（调用 render 方法执行求值）
template = t"Hello, {name}!"
result = template.render({"name": "Alice"})
print(result)
```

---

**基本写法：Python 3.13 自由线程模式**
`python -X gil=0 <脚本>`

```python
# Python 3.13 自由线程模式（禁用 GIL,允许多线程真正并行）
# 命令行执行：python -X gil=0 script.py
# 需使用启用 --disable-gil 编译选项的 Python 解释器
```

---

**基本写法：Python 3.13 实验性 JIT**
`python -X jit <脚本>`

```python
# Python 3.13 实验性 JIT 编译器（提升长运行任务性能）
# 命令行执行：python -X jit script.py
# 需使用启用 --enable-experimental-jit 编译选项的 Python 解释器
```



<!-- ============ 文档分隔线：040-python/005-ControlFlow.md ============ -->

# 控制流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## if 条件语句

**基本写法：基本 if 语句**
`if <条件>: <语句>`

```python
# 基本 if 语句
if x > 0:
    print("正数")
```

---

**基本写法：if-else 语句**
`if <条件>: <语句1> else: <语句2>`

```python
# if-else 语句
if age >= 18:
    print("成年")
else:
    print("未成年")
```

---

**基本写法：if-elif-else 语句**
`if <条件1>: <语句1> elif <条件2>: <语句2> else: <语句3>`

```python
# if-elif-else 语句
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

---

**换行写法：多条件 if 语句**
`if (<条件1> and`
`    <条件2>):`
`    <语句>`

```python
# 多条件 if 语句（换行书写）
if (age >= 18 and
    age <= 65 and
    has_id):
    print("符合条件")
```

---

## 三元条件表达式

**单行写法：三元条件表达式**
`<值1> if <条件> else <值2>`

```python
# 三元条件表达式
status = "成年" if age >= 18 else "未成年"
```

---

## match-case 语句

**基本写法：match-case 基本用法**
`match <对象>: case <模式>: <语句>`

```python
# match-case 基本用法
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")
```

---

**基本写法：match-case 字面量模式**
`match <对象>: case <字面量>: <语句>`

```python
# match-case 字面量模式匹配
match color:
    case "red":
        print("红色")
    case "green":
        print("绿色")
    case "blue":
        print("蓝色")
```

---

**基本写法：match-case 变量绑定**
`match <对象>: case <变量>: <语句>`

```python
# match-case 变量绑定模式
match point:
    case (0, 0):
        print("原点")
    case (0, y):
        print(f"y 轴上，y={y}")
    case (x, 0):
        print(f"x 轴上，x={x}")
    case (x, y):
        print(f"点 ({x}, {y})")
```

---

**基本写法：match-case 类模式匹配**
`match <对象>: case <类名>(<属性>): <语句>`

```python
# match-case 类模式匹配
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x=0, y=0):
        print("原点")
    case Point(x=x, y=0):
        print(f"x 轴上，x={x}")
    case Point(x=0, y=y):
        print(f"y 轴上，y={y}")
    case Point(x=x, y=y):
        print(f"点 ({x}, {y})")
```

---

**基本写法：match-case 序列模式**
`match <序列>: case [<元素1>, <元素2>]: <语句>`

```python
# match-case 序列模式匹配
match command:
    case [action]:
        print(f"单个命令: {action}")
    case [action, obj]:
        print(f"命令: {action} {obj}")
    case [action, *args]:
        print(f"命令: {action}，参数: {args}")
```

---

**基本写法：match-case 映射模式**
`match <字典>: case {"<键>": <值>}: <语句>`

```python
# match-case 映射模式匹配
match config:
    case {"host": str(host), "port": int(port)}:
        print(f"连接 {host}:{port}")
    case {"socket": str(path)}:
        print(f"Unix socket: {path}")
```

---

**基本写法：match-case 守卫条件**
`match <对象>: case <模式> if <条件>: <语句>`

```python
# match-case 守卫条件
match number:
    case n if n < 0:
        print("负数")
    case 0:
        print("零")
    case n if n > 0:
        print("正数")
```

---

**基本写法：match-case 或模式**
`match <对象>: case <模式1> | <模式2>: <语句>`

```python
# match-case 或模式匹配
match status:
    case 200 | 201:
        print("成功")
    case 400 | 404:
        print("客户端错误")
    case 500 | 502:
        print("服务器错误")
```

---

## while 循环

**基本写法：while 循环**
`while <条件>: <语句>`

```python
# while 循环
count = 0
while count < 5:
    print(count)
    count += 1
```

---

**基本写法：while-else 语句**
`while <条件>: <语句> else: <语句>`

```python
# while-else 语句（循环正常结束执行 else）
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环结束")
```

---

**基本写法：break 跳出循环**
`while <条件>: break`

```python
# 使用 break 跳出循环
while True:
    user_input = input("输入 quit 退出: ")
    if user_input == "quit":
        break
    print(f"你输入了: {user_input}")
```

---

**基本写法：continue 跳过本次迭代**
`while <条件>: continue`

```python
# 使用 continue 跳过本次迭代
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

---

## for 循环

**基本写法：遍历可迭代对象**
`for <变量> in <可迭代对象>: <语句>`

```python
# 遍历列表
for item in [1, 2, 3]:
    print(item)
```

---

**基本写法：遍历字符串**
`for <字符> in <字符串>: <语句>`

```python
# 遍历字符串
for char in "Hello":
    print(char)
```

---

**基本写法：遍历字典**
`for <键>, <值> in <字典>.items(): <语句>`

```python
# 遍历字典的键值对
for key, value in {"a": 1, "b": 2}.items():
    print(f"{key}: {value}")
```

---

**基本写法：遍历字典键**
`for <键> in <字典>: <语句>`

```python
# 遍历字典的键
for key in {"a": 1, "b": 2}:
    print(key)
```

---

**基本写法：遍历字典值**
`for <值> in <字典>.values(): <语句>`

```python
# 遍历字典的值
for value in {"a": 1, "b": 2}.values():
    print(value)
```

---

**基本写法：使用 range() 生成序列**
`for <变量> in range(<stop>): <语句>`

```python
# 使用 range() 遍历数字序列
for i in range(5):
    print(i)
```

---

**基本写法：使用 range() 指定起止**
`for <变量> in range(<start>, <stop>): <语句>`

```python
# 使用 range() 指定起始和结束
for i in range(1, 6):
    print(i)
```

---

**基本写法：使用 range() 指定步长**
`for <变量> in range(<start>, <stop>, <step>): <语句>`

```python
# 使用 range() 指定步长
for i in range(0, 10, 2):
    print(i)
```

---

**基本写法：使用 enumerate() 获取索引**
`for <索引>, <值> in enumerate(<可迭代对象>): <语句>`

```python
# 使用 enumerate() 获取索引和值
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")
```

---

**基本写法：enumerate() 指定起始索引**
`for <索引>, <值> in enumerate(<可迭代对象>, start=<n>): <语句>`

```python
# 使用 enumerate() 指定起始索引
for index, value in enumerate(["a", "b", "c"], start=1):
    print(f"{index}: {value}")
```

---

**基本写法：使用 zip() 并行遍历**
`for <变量1>, <变量2> in zip(<可迭代对象1>, <可迭代对象2>): <语句>`

```python
# 使用 zip() 并行遍历多个可迭代对象
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

---

**基本写法：for-else 语句**
`for <变量> in <可迭代对象>: <语句> else: <语句>`

```python
# for-else 语句（循环正常结束执行 else）
for item in [1, 2, 3]:
    print(item)
else:
    print("循环结束")
```

---

**基本写法：嵌套循环**
`for <变量1> in <可迭代对象1>: for <变量2> in <可迭代对象2>: <语句>`

```python
# 嵌套循环
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

---

## 循环控制语句

**基本写法：break 跳出 for 循环**
`for <变量> in <可迭代对象>: if <条件>: break`

```python
# 使用 break 跳出 for 循环
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        break
    print(item)
```

---

**基本写法：continue 跳过 for 循环迭代**
`for <变量> in <可迭代对象>: if <条件>: continue`

```python
# 使用 continue 跳过 for 循环的本次迭代
for item in [1, 2, 3, 4, 5]:
    if item % 2 == 0:
        continue
    print(item)
```

---

**基本写法：pass 空语句**
`for <变量> in <可迭代对象>: pass`

```python
# 使用 pass 作为循环体占位符
for item in items:
    pass
```

---

## 无限循环

**基本写法：while True 无限循环**
`while True: <语句>`

```python
# while True 无限循环
while True:
    response = get_input()
    if response == "exit":
        break
    process(response)
```

---

## 循环中的 else 与 break

**基本写法：循环 break 不执行 else**
`for <变量> in <可迭代对象>: if <条件>: break else: <语句>`

```python
# 循环中 break 时不执行 else 块
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        print("找到 3")
        break
else:
    print("未找到 3")
```

---

## 迭代器与可迭代对象

**基本写法：使用 iter() 获取迭代器**
`iter(<可迭代对象>)`

```python
# 获取迭代器
my_iter = iter([1, 2, 3])
```

---

**基本写法：使用 next() 获取下一个值**
`next(<迭代器>)`

```python
# 获取迭代器的下一个值
print(next(my_iter))
```

---

**基本写法：next() 指定默认值**
`next(<迭代器>, <默认值>)`

```python
# 获取迭代器的下一个值，指定默认值
print(next(my_iter, None))
```

---

**换行写法：自定义迭代器类**
`class <类名>:`
`    def __iter__(self): <语句>`
`    def __next__(self): <语句>`

```python
# 自定义迭代器类
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
```

---

**换行写法：可迭代对象（仅实现 __iter__）**
`class <类名>:`
`    def __iter__(self): yield <值>`

```python
# 可迭代对象（使用 yield 实现）
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
```

---

## 生成器表达式

**基本写法：生成器表达式**
`(<表达式> for <变量> in <可迭代对象>)`

```python
# 生成器表达式
squares = (x ** 2 for x in range(10))
print(next(squares))
```

---

**基本写法：带条件的生成器表达式**
`(<表达式> for <变量> in <可迭代对象> if <条件>)`

```python
# 带条件的生成器表达式
evens = (x for x in range(20) if x % 2 == 0)
print(list(evens))
```

---



<!-- ============ 文档分隔线：040-python/006-TypeAnnotationMypy.md ============ -->

# 类型注解与mypy

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本类型注解

**基本写法：变量类型注解**
`<变量>: <类型> = <值>`

```python
# 变量类型注解
name: str = "Alice"
age: int = 30
height: float = 1.75
is_active: bool = True
```

---

**基本写法：函数参数类型注解**
`def <函数名>(<参数>: <类型>): <语句>`

```python
# 函数参数类型注解
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

---

**基本写法：函数返回值类型注解**
`def <函数名>(<参数>) -> <返回类型>: <语句>`

```python
# 函数返回值类型注解
def add(a: int, b: int) -> int:
    return a + b
```

---

## 复合类型注解

**基本写法：列表类型注解**
`from typing import List`
`<变量>: List[<元素类型>] = <值>`

```python
# 列表类型注解
from typing import List
numbers: List[int] = [1, 2, 3]
names: List[str] = ["Alice", "Bob"]
```

---

**基本写法：字典类型注解**
`from typing import Dict`
`<变量>: Dict[<键类型>, <值类型>] = <值>`

```python
# 字典类型注解
from typing import Dict
user: Dict[str, int] = {"age": 30, "score": 95}
```

---

**基本写法：元组类型注解**
`from typing import Tuple`
`<变量>: Tuple[<类型1>, <类型2>] = <值>`

```python
# 元组类型注解
from typing import Tuple
point: Tuple[int, int] = (3, 4)
```

---

**基本写法：集合类型注解**
`from typing import Set`
`<变量>: Set[<元素类型>] = <值>`

```python
# 集合类型注解
from typing import Set
unique_numbers: Set[int] = {1, 2, 3}
```

---

## Optional 类型

**基本写法：使用 Optional 类型**
`from typing import Optional`
`<变量>: Optional[<类型>] = <值>`

```python
# Optional 类型注解（表示值可以为 None）
from typing import Optional
def find_user(user_id: int) -> Optional[dict]:
    if user_id == 1:
        return {"name": "Alice"}
    return None
```

---

## Union 类型

**基本写法：使用 Union 类型**
`from typing import Union`
`<变量>: Union[<类型1>, <类型2>] = <值>`

```python
# Union 类型注解（表示值可以是多种类型之一）
from typing import Union
def process(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data
```

---

**基本写法：使用管道符（Python 3.10+）**
`<变量>: <类型1> | <类型2> = <值>`

```python
# 使用管道符表示联合类型
def process(data: str | bytes) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data
```

---

## Any 类型

**基本写法：使用 Any 类型**
`from typing import Any`
`<变量>: Any = <值>`

```python
# Any 类型注解（表示任意类型）
from typing import Any
data: Any = "hello"
data = 123
```

---

## Callable 类型

**基本写法：使用 Callable 类型**
`from typing import Callable`
`<变量>: Callable[[<参数类型>], <返回类型>] = <函数>`

```python
# Callable 类型注解（表示可调用对象）
from typing import Callable
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)
```

---

**基本写法：Callable 无参数**
`<变量>: Callable[[], <返回类型>] = <函数>`

```python
# Callable 无参数类型注解
from typing import Callable
callback: Callable[[], None] = lambda: print("Hello")
```

---

## 泛型类型

**换行写法：定义泛型类**
`from typing import TypeVar, Generic`
`T = TypeVar("T")`
`class <类名>(Generic[T]):`
`    def <方法>(self, <参数>: T) -> T: <语句>`

```python
# 定义泛型类
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

---

**换行写法：定义泛型函数**
`from typing import TypeVar`
`T = TypeVar("T")`
`def <函数名>(<参数>: T) -> T: <语句>`

```python
# 定义泛型函数
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]
```

---

## TypeVar 约束

**基本写法：带约束的 TypeVar**
`T = TypeVar("T", <类型1>, <类型2>)`

```python
# 带约束的 TypeVar（限制为指定类型之一）
from typing import TypeVar

T = TypeVar("T", int, float)

def add(a: T, b: T) -> T:
    return a + b
```

---

**基本写法：带边界的 TypeVar**
`T = TypeVar("T", bound=<类型>)`

```python
# 带边界的 TypeVar（限制为指定类型及其子类）
from typing import TypeVar

class Animal:
    def speak(self) -> str:
        return "sound"

T = TypeVar("T", bound=Animal)

def make_speak(animal: T) -> str:
    return animal.speak()
```

---

## TypedDict

**换行写法：定义 TypedDict**
`from typing import TypedDict`
`class <TypedDict类>(TypedDict):`
`    <字段1>: <类型>`
`    <字段2>: <类型>`

```python
# 定义 TypedDict（类型安全的字典）
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str
```

---

**基本写法：使用 TypedDict**
`<变量>: <TypedDict类> = {<字段>: <值>}`

```python
# 使用 TypedDict
user: User = {"name": "Alice", "age": 30, "email": "alice@example.com"}
```

---

## Literal 类型

**基本写法：使用 Literal 类型**
`from typing import Literal`
`<变量>: Literal[<值1>, <值2>] = <值>`

```python
# Literal 类型注解（限制为特定字面量值）
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    print(f"模式: {mode}")
```

---

## Final 类型

**基本写法：使用 Final 类型**
`from typing import Final`
`<变量>: Final[<类型>] = <值>`

```python
# Final 类型注解（表示常量，不可重新赋值）
from typing import Final
MAX_SIZE: Final[int] = 100
```

---

## ClassVar 类型

**基本写法：使用 ClassVar 类型**
`from typing import ClassVar`
`<属性>: ClassVar[<类型>] = <值>`

```python
# ClassVar 类型注解（表示类变量而非实例变量）
from typing import ClassVar

class MyClass:
    count: ClassVar[int] = 0
    name: str = "default"
```

---

## Protocol 类型

**换行写法：定义 Protocol**
`from typing import Protocol`
`class <Protocol名>(Protocol):`
`    def <方法>(self, <参数>) -> <返回类型>: ...`

```python
# 定义 Protocol（结构化子类型）
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

def render(obj: Drawable) -> None:
    obj.draw()
```

---

## 类型别名

**基本写法：定义类型别名**
`<别名> = <类型>`

```python
# 定义类型别名
Vector = list[float]
Matrix = list[Vector]

def create_vector() -> Vector:
    return [1.0, 2.0, 3.0]
```

---

**基本写法：使用 TypeAlias**
`from typing import TypeAlias`
`<别名>: TypeAlias = <类型>`

```python
# 使用 TypeAlias 显式声明类型别名
from typing import TypeAlias
UserId: TypeAlias = int
UserName: TypeAlias = str
```

---

## NewType

**基本写法：使用 NewType 创建新类型**
`from typing import NewType`
`<新类型> = NewType("<新类型名>", <基础类型>)`

```python
# 使用 NewType 创建新类型
from typing import NewType
UserId = NewType("UserId", int)

def get_user(user_id: UserId) -> str:
    return f"User {user_id}"
```

---

## mypy 配置

**基本写法：创建 mypy.ini 配置文件**
`[mypy]`
`python_version = <版本>`
`strict = <布尔值>`

```python
# mypy.ini 配置文件
# [mypy]
# python_version = 3.11
# strict = True
# warn_return_any = True
# warn_unused_configs = True
```

---

**基本写法：使用 pyproject.toml 配置**
`[tool.mypy]`
`python_version = "<版本>"`

```python
# pyproject.toml 中的 mypy 配置
# [tool.mypy]
# python_version = "3.11"
# strict = true
# disallow_untyped_defs = true
```

---

## 运行 mypy

**基本写法：运行 mypy 检查**
`mypy <文件或目录>`

```python
# 运行 mypy 检查 Python 文件
# 命令行执行：mypy script.py
```

---

**基本写法：运行 mypy 严格模式**
`mypy --strict <文件>`

```python
# 运行 mypy 严格模式
# 命令行执行：mypy --strict script.py
```

---

**基本写法：忽略特定错误**
`# type: ignore`

```python
# 忽略类型检查错误
result = some_untyped_function()  # type: ignore
```

---

**基本写法：忽略特定错误码**
`# type: ignore[<错误码>]`

```python
# 忽略特定错误码
result = some_function()  # type: ignore[no-untyped-call]
```

---

## 类型注解进阶

**基本写法：使用 Type 获取类型**
`from typing import Type`
`def <函数>(<参数>: Type[<类>]) -> <语句>`

```python
# 使用 Type 注解表示类本身
from typing import Type

class Animal:
    @classmethod
    def create(cls) -> "Animal":
        return cls()

def factory(cls: Type[Animal]) -> Animal:
    return cls.create()
```

---

**基本写法：使用 TypeGuard**
`from typing import TypeGuard`
`def <函数>(<参数>: <类型>) -> TypeGuard[<目标类型>]: <语句>`

```python
# 使用 TypeGuard 定义类型守卫
from typing import TypeGuard

def is_string_list(items: list) -> TypeGuard[list[str]]:
    return all(isinstance(item, str) for item in items)
```

---

**基本写法：使用 ParamSpec**
`from typing import ParamSpec`
`P = ParamSpec("P")`

```python
# 使用 ParamSpec 传递参数签名
from typing import ParamSpec, TypeVar, Callable

P = ParamSpec("P")
R = TypeVar("R")

def decorator(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func(*args, **kwargs)
    return wrapper
```

---

**基本写法：使用 Concatenate**
`from typing import Concatenate`
`def <函数>(<参数>: Callable[Concatenate[<类型>, P], R]): <语句>`

```python
# 使用 Concatenate 在参数签名前添加参数
from typing import Concatenate, ParamSpec, TypeVar, Callable

P = ParamSpec("P")
R = TypeVar("R")

def with_context(func: Callable[Concatenate[str, P], R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return func("context", *args, **kwargs)
    return wrapper
```

---

## 类型注解与 dataclass

**换行写法：带类型注解的 dataclass**
`from dataclasses import dataclass`
`@dataclass`
`class <类名>:`
`    <字段1>: <类型>`
`    <字段2>: <类型> = <默认值>`

```python
# 带类型注解的 dataclass
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str = ""
    active: bool = True
```

---

## 类型注解与 Pydantic

**换行写法：使用 Pydantic 模型**
`from pydantic import BaseModel`
`class <模型名>(BaseModel):`
`    <字段1>: <类型>`
`    <字段2>: <类型>`

```python
# 使用 Pydantic 定义数据模型
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

---

**基本写法：使用 Pydantic 验证**
`<模型>(**<字典>)`

```python
# 使用 Pydantic 进行数据验证
data = {"name": "Alice", "age": 30, "email": "alice@example.com"}
user = User(**data)
```

---

## 异步类型注解

**换行写法：异步函数类型注解**
`from typing import Coroutine, Any`
`async def <函数>(<参数>: <类型>) -> <返回类型>: <语句>`

```python
# 异步函数类型注解
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)
    return f"Data from {url}"
```

---

**基本写法：Awaitable 类型注解**
`from typing import Awaitable`
`<变量>: Awaitable[<类型>] = <协程>`

```python
# Awaitable 类型注解
from typing import Awaitable

def get_fetcher() -> Awaitable[str]:
    return fetch_data("https://example.com")
```

---

**基本写法：AsyncIterator 类型注解**
`from typing import AsyncIterator`
`async def <函数>() -> AsyncIterator[<类型>]: <语句>`

```python
# AsyncIterator 类型注解
from typing import AsyncIterator

async def async_range(n: int) -> AsyncIterator[int]:
    for i in range(n):
        yield i
        await asyncio.sleep(0.1)
```

---

## 类型注解最佳实践

**基本写法：为所有函数添加类型注解**
`def <函数名>(<参数>: <类型>) -> <返回类型>: <语句>`

```python
# 为所有函数添加类型注解
def calculate_total(prices: list[float], tax_rate: float) -> float:
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)
```

---

**基本写法：使用 NoReturn 表示不返回**
`from typing import NoReturn`
`def <函数>(<参数>) -> NoReturn: <语句>`

```python
# 使用 NoReturn 表示函数不返回
from typing import NoReturn

def raise_error(message: str) -> NoReturn:
    raise ValueError(message)
```

---

**基本写法：使用 overload 重载**
`from typing import overload`
`@overload`
`def <函数>(<参数>: <类型1>) -> <返回类型1>: ...`

```python
# 使用 overload 定义函数重载
from typing import overload

@overload
def process(data: int) -> int: ...

@overload
def process(data: str) -> str: ...

def process(data):
    if isinstance(data, int):
        return data * 2
    return data.upper()
```

---

## Python 3.13+ 类型系统增强

**基本写法：TypeIs 缩窄类型（Python 3.13）**
`from typing import TypeIs`
`def <函数>(<参数>: <类型>) -> TypeIs[<目标类型>]: <语句>`

```python
# Python 3.13 TypeIs 类型缩窄（双向缩窄,比 TypeGuard 更严格）
from typing import TypeIs

def is_str_list(items: list) -> TypeIs[list[str]]:
    return all(isinstance(item, str) for item in items)
```

---

**基本写法：ReadOnly 类型限定符（Python 3.13）**
`from typing import ReadOnly`
`<属性>: ReadOnly[<类型>]`

```python
# Python 3.13 ReadOnly 类型限定符（标记 TypedDict 只读字段,禁止写入）
from typing import TypedDict, ReadOnly

class User(TypedDict):
    name: ReadOnly[str]
    age: int
```

---

**基本写法：deprecated 装饰器（Python 3.13）**
`from warnings import deprecated`
`@deprecated("<弃用说明>")`
`def <函数>() -> <返回类型>: <语句>`

```python
# Python 3.13 deprecated 装饰器（标记弃用函数,调用时触发 DeprecationWarning）
from warnings import deprecated

@deprecated("use new_function() instead")
def old_function() -> None:
    print("old")
```

---

**基本写法：PEP 695 类型别名语句**
`type <别名> = <类型>`

```python
# PEP 695 类型别名语句（原生语法,无需 typing.TypeAlias）
type Point = tuple[float, float]
type Vector = list[float]

def origin() -> Point:
    return (0.0, 0.0)
```

---

**基本写法：PEP 695 泛型类新语法**
`class <类名>[<类型参数>]:`
`    def <方法>(self, <参数>: <类型参数>) -> <类型参数>: <语句>`

```python
# PEP 695 泛型类新语法（无需显式声明 TypeVar 和 Generic）
class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

---

**基本写法：Python 3.14 deferred annotations 求值**
`<变量>: <前向引用类型> = <值>`
`class <类名>:`
`    <属性>: <前向引用类型> = <值>`

```python
# Python 3.14 deferred annotations 延迟求值（注解默认延迟,访问 __annotations__ 时才求值）
# 无需 from __future__ import annotations 即可使用前向引用
class Node:
    next: Node | None = None

def build() -> Node:
    return Node()
```



<!-- ============ 文档分隔线：040-python/007-ListComprehensionAdvanced.md ============ -->

# 列表推导式进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本列表推导式

**基本写法：基本列表推导式**
`[<表达式> for <变量> in <可迭代对象>]`

```python
# 基本列表推导式
squares = [x ** 2 for x in range(5)]
```

---

**基本写法：带条件的列表推导式**
`[<表达式> for <变量> in <可迭代对象> if <条件>]`

```python
# 带条件的列表推导式
evens = [x for x in range(10) if x % 2 == 0]
```

---

**基本写法：带 if-else 的列表推导式**
`[<表达式1> if <条件> else <表达式2> for <变量> in <可迭代对象>]`

```python
# 带 if-else 的列表推导式
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
```

---

## 嵌套循环推导式

**基本写法：嵌套 for 的列表推导式**
`[<表达式> for <变量1> in <可迭代对象1> for <变量2> in <可迭代对象2>]`

```python
# 嵌套 for 的列表推导式
pairs = [(x, y) for x in range(3) for y in range(3)]
```

---

**基本写法：带条件的嵌套推导式**
`[<表达式> for <变量1> in <可迭代对象1> for <变量2> in <可迭代对象2> if <条件>]`

```python
# 带条件的嵌套推导式
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
```

---

**换行写法：多行嵌套推导式**
`[<表达式>`
` for <变量1> in <可迭代对象1>`
` for <变量2> in <可迭代对象2>]`

```python
# 多行嵌套推导式
matrix = [
    [x * y for y in range(3)]
    for x in range(3)
]
```

---

## 字典推导式

**基本写法：基本字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象>}`

```python
# 基本字典推导式
squares = {x: x ** 2 for x in range(5)}
```

---

**基本写法：带条件的字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的字典推导式
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
```

---

**基本写法：反转字典键值**
`{<值>: <键> for <键>, <值> in <字典>.items()}`

```python
# 反转字典的键和值
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
```

---

## 集合推导式

**基本写法：基本集合推导式**
`{<表达式> for <变量> in <可迭代对象>}`

```python
# 基本集合推导式
squares = {x ** 2 for x in range(5)}
```

---

**基本写法：带条件的集合推导式**
`{<表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的集合推导式
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
```

---

## 生成器表达式

**基本写法：基本生成器表达式**
`(<表达式> for <变量> in <可迭代对象>)`

```python
# 基本生成器表达式
squares_gen = (x ** 2 for x in range(5))
print(next(squares_gen))
```

---

**基本写法：带条件的生成器表达式**
`(<表达式> for <变量> in <可迭代对象> if <条件>)`

```python
# 带条件的生成器表达式
evens_gen = (x for x in range(10) if x % 2 == 0)
print(list(evens_gen))
```

---

## 复杂表达式

**基本写法：函数调用在推导式中**
`[<函数>(<参数>) for <变量> in <可迭代对象>]`

```python
# 函数调用在推导式中
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
```

---

**基本写法：方法调用在推导式中**
`[<对象>.<方法>() for <对象> in <可迭代对象>]`

```python
# 方法调用在推导式中
strings = ["  hello  ", "  world  "]
cleaned = [s.strip() for s in strings]
```

---

**基本写法：条件表达式在推导式中**
`[<表达式1> if <条件> else <表达式2> for <变量> in <可迭代对象>]`

```python
# 条件表达式在推导式中
numbers = [1, -2, 3, -4, 5]
abs_values = [x if x >= 0 else -x for x in numbers]
```

---

## 使用 enumerate()

**基本写法：使用 enumerate() 获取索引**
`[(<索引>, <值>) for <索引>, <值> in enumerate(<可迭代对象>)]`

```python
# 使用 enumerate() 获取索引
fruits = ["apple", "banana", "cherry"]
indexed = [(i, fruit) for i, fruit in enumerate(fruits)]
```

---

**基本写法：enumerate() 指定起始索引**
`[(<索引>, <值>) for <索引>, <值> in enumerate(<可迭代对象>, start=<n>)]`

```python
# enumerate() 指定起始索引
indexed = [(i, fruit) for i, fruit in enumerate(fruits, start=1)]
```

---

## 使用 zip()

**基本写法：使用 zip() 并行遍历**
`[(<值1>, <值2>) for <值1>, <值2> in zip(<可迭代对象1>, <可迭代对象2>)]`

```python
# 使用 zip() 并行遍历
names = ["Alice", "Bob"]
ages = [25, 30]
pairs = [(name, age) for name, age in zip(names, ages)]
```

---

## 字符串处理

**基本写法：字符串分割与处理**
`[<表达式> for <变量> in <字符串>.split(<分隔符>)]`

```python
# 字符串分割与处理
sentence = "hello world python"
words = [word.upper() for word in sentence.split()]
```

---

**基本写法：过滤字符串列表**
`[<字符串> for <字符串> in <列表> if <条件>]`

```python
# 过滤字符串列表
words = ["apple", "banana", "cherry", "date"]
long_words = [word for word in words if len(word) > 5]
```

---

## 数学运算

**基本写法：数学运算在推导式中**
`[<表达式> for <变量> in <可迭代对象>]`

```python
# 数学运算在推导式中
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
```

---

**基本写法：使用数学函数**
`[<函数>(<参数>) for <变量> in <可迭代对象>]`

```python
# 使用数学函数
import math
numbers = [1, 4, 9, 16, 25]
roots = [math.sqrt(x) for x in numbers]
```

---

## 文件处理

**基本写法：读取文件行并处理**
`[<表达式> for <行> in <文件>]`

```python
# 读取文件行并处理
with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
```

---

**基本写法：过滤文件行**
`[<行> for <行> in <文件> if <条件>]`

```python
# 过滤文件中的非空行
with open("file.txt", "r") as f:
    non_empty = [line.strip() for line in f if line.strip()]
```

---

## 嵌套列表展平

**基本写法：展平嵌套列表**
`[<元素> for <子列表> in <嵌套列表> for <元素> in <子列表>]`

```python
# 展平嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
```

---

**基本写法：带条件的展平**
`[<元素> for <子列表> in <嵌套列表> for <元素> in <子列表> if <条件>]`

```python
# 带条件的展平
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
```

---

## 使用 itertools

**基本写法：使用 itertools.chain 展平**
`list(chain.from_iterable(<嵌套列表>))`

```python
# 使用 itertools.chain 展平嵌套列表
from itertools import chain
matrix = [[1, 2, 3], [4, 5, 6]]
flat = list(chain.from_iterable(matrix))
```

---

**基本写法：使用 itertools.product 生成笛卡尔积**
`[<表达式> for <变量1>, <变量2> in product(<可迭代对象1>, <可迭代对象2>)]`

```python
# 使用 itertools.product 生成笛卡尔积
from itertools import product
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combinations = [(c, s) for c, s in product(colors, sizes)]
```

---

## 性能对比

**基本写法：列表推导式 vs for 循环**
`[<表达式> for <变量> in <可迭代对象>]`

```python
# 列表推导式（比 for 循环更快）
squares = [x ** 2 for x in range(1000)]
```

---

**基本写法：使用 sum() 配合生成器**
`sum(<表达式> for <变量> in <可迭代对象>)`

```python
# 使用 sum() 配合生成器表达式
total = sum(x ** 2 for x in range(100))
```

---

## 多变量推导式

**基本写法：多变量列表推导式**
`[<表达式> for <变量1>, <变量2> in <可迭代对象>]`

```python
# 多变量列表推导式
pairs = [(a, b) for a, b in [(1, 2), (3, 4), (5, 6)]]
```

---

**基本写法：多变量带条件推导式**
`[<表达式> for <变量1>, <变量2> in <可迭代对象> if <条件>]`

```python
# 多变量带条件推导式
sums = [a + b for a, b in [(1, 2), (3, 4), (5, 6)] if a + b > 5]
```

---

## 字典转换为列表

**基本写法：字典键转换为列表**
`[<键> for <键> in <字典>]`

```python
# 字典键转换为列表
person = {"name": "Alice", "age": 30}
keys = [key for key in person]
```

---

**基本写法：字典值转换为列表**
`[<值> for <值> in <字典>.values()]`

```python
# 字典值转换为列表
values = [value for value in person.values()]
```

---

**基本写法：字典键值对转换为列表**
`[(<键>, <值>) for <键>, <值> in <字典>.items()]`

```python
# 字典键值对转换为列表
items = [(k, v) for k, v in person.items()]
```

---

**基本写法：带条件的字典过滤**
`[(<键>, <值>) for <键>, <值> in <字典>.items() if <条件>]`

```python
# 带条件的字典过滤
filtered = [(k, v) for k, v in person.items() if isinstance(v, str)]
```

---



<!-- ============ 文档分隔线：040-python/008-COOPBasics.md ============ -->

# Python 面向对象基础

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类定义

**基本写法：定义简单类**
`class <类名>: <类体>`

```python
# 定义简单类
class Dog:
    pass
```

---

**换行写法：定义带属性的类**
`class <类名>:`
`    def __init__(self, <参数>):`
`        self.<属性> = <值>`

```python
# 定义带初始化方法的类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

**基本写法：定义类属性**
`class <类名>: <类属性> = <值>`

```python
# 定义类属性
class Dog:
    species = "Canis lupus"
```

---

**基本写法：定义实例属性**
`self.<属性> = <值>`

```python
# 在 __init__ 中定义实例属性
class Dog:
    def __init__(self, name):
        self.name = name
```

---

## 实例化与访问

**基本写法：创建类实例**
`<对象> = <类名>(<参数>)`

```python
# 创建 Dog 类的实例
dog = Dog("Buddy", 3)
```

---

**基本写法：访问实例属性**
`<对象>.<属性>`

```python
# 访问实例属性
print(dog.name)
```

---

**基本写法：访问类属性**
`<类名>.<类属性>`

```python
# 访问类属性
print(Dog.species)
```

---

**基本写法：修改实例属性**
`<对象>.<属性> = <新值>`

```python
# 修改实例属性
dog.age = 4
```

---

## 实例方法

**基本写法：定义实例方法**
`def <方法名>(self, <参数>): <语句>`

```python
# 定义实例方法
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
```

---

**基本写法：调用实例方法**
`<对象>.<方法名>(<参数>)`

```python
# 调用实例方法
print(dog.bark())
```

---

**基本写法：定义带参数的实例方法**
`def <方法名>(self, <参数1>, <参数2>): <语句>`

```python
# 定义带参数的实例方法
class Dog:
    def fetch(self, item):
        return f"{self.name} fetches the {item}"
```

---

## 类方法

**基本写法：定义类方法**
`@classmethod`
`def <方法名>(cls, <参数>): <语句>`

```python
# 定义类方法
class Dog:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

---

**基本写法：使用类方法作为工厂**
`@classmethod`
`def <方法名>(cls, <参数>): return cls(<参数>)`

```python
# 使用类方法作为工厂函数
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split(",")
        return cls(name, int(age))
```

---

## 静态方法

**基本写法：定义静态方法**
`@staticmethod`
`def <方法名>(<参数>): <语句>`

```python
# 定义静态方法
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
```

---

**基本写法：调用静态方法**
`<类名>.<方法名>(<参数>)`

```python
# 调用静态方法
print(MathHelper.add(3, 5))
```

---

## 继承

**基本写法：单继承**
`class <子类>(<父类>): <类体>`

```python
# 单继承
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass
```

---

**基本写法：多继承**
`class <子类>(<父类1>, <父类2>): <类体>`

```python
# 多继承
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass
```

---

**基本写法：调用父类方法**
`super().<方法名>(<参数>)`

```python
# 调用父类的 __init__ 方法
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

---

**基本写法：方法重写**
`def <父类方法名>(self, <参数>): <新语句>`

```python
# 重写父类方法
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

---

**基本写法：使用 super() 调用重写方法**
`super().<方法名>(<参数>)`

```python
# 在重写方法中调用父类方法
class Dog(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} - Woof!"
```

---

## 多重继承与 MRO

**基本写法：查看方法解析顺序**
`<类名>.mro()`

```python
# 查看方法解析顺序
print(Dog.mro())
```

---

**基本写法：查看方法解析顺序（__mro__）**
`<类名>.__mro__`

```python
# 查看 MRO 元组
print(Dog.__mro__)
```

---

## 属性装饰器

**基本写法：使用 @property 定义属性**
`@property`
`def <属性名>(self): <语句>`

```python
# 使用 @property 定义只读属性
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
```

---

**基本写法：使用 @property 定义可写属性**
`@<属性名>.setter`
`def <属性名>(self, <值>): <语句>`

```python
# 使用 @property.setter 定义可写属性
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

---

**基本写法：使用 @property 定义删除器**
`@<属性名>.deleter`
`def <属性名>(self): <语句>`

```python
# 使用 @property.deleter 定义删除器
class Circle:
    @property
    def radius(self):
        return self._radius

    @radius.deleter
    def radius(self):
        del self._radius
```

---

## 特殊方法（魔术方法）

**基本写法：定义 __str__ 方法**
`def __str__(self): return <字符串>`

```python
# 定义 __str__ 方法（用户友好的字符串表示）
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog(name={self.name})"
```

---

**基本写法：定义 __repr__ 方法**
`def __repr__(self): return <字符串>`

```python
# 定义 __repr__ 方法（开发者友好的字符串表示）
class Dog:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Dog(name={self.name!r})"
```

---

**基本写法：定义 __len__ 方法**
`def __len__(self): return <整数>`

```python
# 定义 __len__ 方法（支持 len() 函数）
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)
```

---

**基本写法：定义 __eq__ 方法**
`def __eq__(self, other): return <布尔值>`

```python
# 定义 __eq__ 方法（支持 == 运算符）
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

**基本写法：定义 __lt__ 方法**
`def __lt__(self, other): return <布尔值>`

```python
# 定义 __lt__ 方法（支持 < 运算符）
class Student:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score
```

---

**基本写法：定义 __add__ 方法**
`def __add__(self, other): return <新对象>`

```python
# 定义 __add__ 方法（支持 + 运算符）
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

---

**基本写法：定义 __getitem__ 方法**
`def __getitem__(self, <键>): return <值>`

```python
# 定义 __getitem__ 方法（支持 [] 访问）
class Matrix:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]
```

---

**基本写法：定义 __setitem__ 方法**
`def __setitem__(self, <键>, <值>): <语句>`

```python
# 定义 __setitem__ 方法（支持 [] 赋值）
class Matrix:
    def __setitem__(self, key, value):
        self.data[key] = value
```

---

**基本写法：定义 __iter__ 方法**
`def __iter__(self): return <迭代器>`

```python
# 定义 __iter__ 方法（支持迭代）
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
```

---

**基本写法：定义 __contains__ 方法**
`def __contains__(self, <元素>): return <布尔值>`

```python
# 定义 __contains__ 方法（支持 in 运算符）
class Matrix:
    def __contains__(self, item):
        return any(item in row for row in self.data)
```

---

**基本写法：定义 __call__ 方法**
`def __call__(self, <参数>): <语句>`

```python
# 定义 __call__ 方法（使实例可调用）
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor
```



<!-- ============ 文档分隔线：040-python/009-COOPAdvanced.md ============ -->

# Python 面向对象进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：040-python/010-BuiltinDataStructure.md ============ -->

# 内置数据结构

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 列表

**基本写法：创建列表**
`[<元素1>, <元素2>, <元素3>]`

```python
# 创建列表
fruits = ["apple", "banana", "cherry"]
```

---

**基本写法：创建空列表**
`[]`

```python
# 创建空列表
empty_list = []
```

---

**基本写法：使用 list() 创建列表**
`list(<可迭代对象>)`

```python
# 使用 list() 创建列表
numbers = list(range(5))
```

---

**基本写法：访问列表元素**
`<列表>[<索引>]`

```python
# 访问列表元素
print(fruits[0])
```

---

**基本写法：负索引访问**
`<列表>[-<索引>]`

```python
# 使用负索引访问（从末尾开始）
print(fruits[-1])
```

---

**基本写法：列表切片**
`<列表>[<start>:<stop>:<step>]`

```python
# 列表切片
print(fruits[0:2])
```

---

**基本写法：修改列表元素**
`<列表>[<索引>] = <新值>`

```python
# 修改列表元素
fruits[0] = "orange"
```

---

## 列表方法

**基本写法：追加元素**
`<列表>.append(<元素>)`

```python
# 追加元素到列表末尾
fruits.append("grape")
```

---

**基本写法：插入元素**
`<列表>.insert(<索引>, <元素>)`

```python
# 在指定位置插入元素
fruits.insert(1, "kiwi")
```

---

**基本写法：扩展列表**
`<列表>.extend(<可迭代对象>)`

```python
# 使用另一个列表扩展当前列表
fruits.extend(["mango", "pear"])
```

---

**基本写法：删除指定元素**
`<列表>.remove(<元素>)`

```python
# 删除列表中第一个匹配的元素
fruits.remove("banana")
```

---

**基本写法：弹出元素**
`<列表>.pop([<索引>])`

```python
# 弹出指定位置的元素（默认末尾）
last = fruits.pop()
```

---

**基本写法：清空列表**
`<列表>.clear()`

```python
# 清空列表
fruits.clear()
```

---

**基本写法：查找元素索引**
`<列表>.index(<元素>)`

```python
# 查找元素的索引位置
index = fruits.index("cherry")
```

---

**基本写法：统计元素出现次数**
`<列表>.count(<元素>)`

```python
# 统计元素出现次数
count = fruits.count("apple")
```

---

**基本写法：排序列表**
`<列表>.sort()`

```python
# 原地排序列表
fruits.sort()
```

---

**基本写法：指定排序规则**
`<列表>.sort(key=<函数>, reverse=<布尔值>)`

```python
# 按字符串长度排序
fruits.sort(key=len, reverse=True)
```

---

**基本写法：反转列表**
`<列表>.reverse()`

```python
# 原地反转列表
fruits.reverse()
```

---

**基本写法：复制列表**
`<列表>.copy()`

```python
# 复制列表
fruits_copy = fruits.copy()
```

---

## 元组

**基本写法：创建元组**
`(<元素1>, <元素2>, <元素3>)`

```python
# 创建元组
point = (3, 4)
```

---

**基本写法：创建单元素元组**
`(<元素>,)`

```python
# 创建单元素元组（注意逗号）
single = (42,)
```

---

**基本写法：创建空元组**
`()`

```python
# 创建空元组
empty_tuple = ()
```

---

**基本写法：使用 tuple() 创建元组**
`tuple(<可迭代对象>)`

```python
# 使用 tuple() 创建元组
numbers = tuple([1, 2, 3])
```

---

**基本写法：访问元组元素**
`<元组>[<索引>]`

```python
# 访问元组元素
print(point[0])
```

---

**基本写法：元组解包**
`<变量1>, <变量2> = <元组>`

```python
# 元组解包
x, y = point
```

---

**基本写法：使用星号解包**
`<变量1>, *<变量2> = <元组>`

```python
# 使用星号收集剩余值
first, *rest = (1, 2, 3, 4, 5)
```

---

**基本写法：命名元组**
`namedtuple(<类名>, [<字段1>, <字段2>])`

```python
# 创建命名元组
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
```

---

## 字典

**基本写法：创建字典**
`{<键1>: <值1>, <键2>: <值2>}`

```python
# 创建字典
person = {"name": "Alice", "age": 30}
```

---

**基本写法：创建空字典**
`{}`

```python
# 创建空字典
empty_dict = {}
```

---

**基本写法：使用 dict() 创建字典**
`dict(<键1>=<值1>, <键2>=<值2>)`

```python
# 使用 dict() 创建字典
person = dict(name="Alice", age=30)
```

---

**基本写法：使用键值对序列创建字典**
`dict([(<键>, <值>), (<键>, <值>)])`

```python
# 使用键值对序列创建字典
person = dict([("name", "Alice"), ("age", 30)])
```

---

**基本写法：访问字典值**
`<字典>[<键>]`

```python
# 通过键访问值
print(person["name"])
```

---

**基本写法：使用 get() 安全访问**
`<字典>.get(<键>, <默认值>)`

```python
# 使用 get() 安全访问，键不存在时返回默认值
print(person.get("email", "N/A"))
```

---

**基本写法：修改或添加键值对**
`<字典>[<键>] = <值>`

```python
# 修改或添加键值对
person["email"] = "alice@example.com"
```

---

**基本写法：删除键值对**
`del <字典>[<键>]`

```python
# 删除指定键值对
del person["age"]
```

---

## 字典方法

**基本写法：获取所有键**
`<字典>.keys()`

```python
# 获取字典的所有键
print(person.keys())
```

---

**基本写法：获取所有值**
`<字典>.values()`

```python
# 获取字典的所有值
print(person.values())
```

---

**基本写法：获取所有键值对**
`<字典>.items()`

```python
# 获取字典的所有键值对
print(person.items())
```

---

**基本写法：弹出键值对**
`<字典>.pop(<键>, <默认值>)`

```python
# 弹出指定键的值
age = person.pop("age", None)
```

---

**基本写法：弹出最后一个键值对**
`<字典>.popitem()`

```python
# 弹出最后一个键值对
key, value = person.popitem()
```

---

**基本写法：更新字典**
`<字典>.update(<其他字典>)`

```python
# 使用另一个字典更新当前字典
person.update({"age": 31, "city": "New York"})
```

---

**基本写法：设置默认值**
`<字典>.setdefault(<键>, <默认值>)`

```python
# 设置键的默认值（键不存在时设置）
person.setdefault("country", "USA")
```

---

**基本写法：清空字典**
`<字典>.clear()`

```python
# 清空字典
person.clear()
```

---

**基本写法：复制字典**
`<字典>.copy()`

```python
# 复制字典
person_copy = person.copy()
```

---

## 字典推导式

**基本写法：基本字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象>}`

```python
# 基本字典推导式
squares = {x: x ** 2 for x in range(5)}
```

---

**基本写法：带条件的字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的字典推导式
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
```

---

## 集合

**基本写法：创建集合**
`{<元素1>, <元素2>, <元素3>}`

```python
# 创建集合
fruits = {"apple", "banana", "cherry"}
```

---

**基本写法：创建空集合**
`set()`

```python
# 创建空集合（注意：{} 创建的是空字典）
empty_set = set()
```

---

**基本写法：使用 set() 创建集合**
`set(<可迭代对象>)`

```python
# 使用 set() 从列表创建集合
numbers = set([1, 2, 3, 2, 1])
```

---

## 集合方法

**基本写法：添加元素**
`<集合>.add(<元素>)`

```python
# 添加元素到集合
fruits.add("orange")
```

---

**基本写法：删除元素**
`<集合>.remove(<元素>)`

```python
# 删除元素（元素不存在时抛出异常）
fruits.remove("banana")
```

---

**基本写法：安全删除元素**
`<集合>.discard(<元素>)`

```python
# 安全删除元素（元素不存在时不抛出异常）
fruits.discard("banana")
```

---

**基本写法：弹出元素**
`<集合>.pop()`

```python
# 弹出集合中的任意元素
element = fruits.pop()
```

---

**基本写法：清空集合**
`<集合>.clear()`

```python
# 清空集合
fruits.clear()
```

---

## 集合运算

**基本写法：并集运算**
`<集合1> | <集合2>`

```python
# 集合并集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
```

---

**基本写法：交集运算**
`<集合1> & <集合2>`

```python
# 集合交集
intersection = set1 & set2
```

---

**基本写法：差集运算**
`<集合1> - <集合2>`

```python
# 集合差集
difference = set1 - set2
```

---

**基本写法：对称差集运算**
`<集合1> ^ <集合2>`

```python
# 集合对称差集
symmetric_diff = set1 ^ set2
```

---

**基本写法：使用 union() 方法**
`<集合>.union(<其他集合>)`

```python
# 使用 union() 方法求并集
union = set1.union(set2)
```

---

**基本写法：使用 intersection() 方法**
`<集合>.intersection(<其他集合>)`

```python
# 使用 intersection() 方法求交集
intersection = set1.intersection(set2)
```

---

**基本写法：使用 difference() 方法**
`<集合>.difference(<其他集合>)`

```python
# 使用 difference() 方法求差集
difference = set1.difference(set2)
```

---

**基本写法：子集判断**
`<集合1>.issubset(<集合2>)`

```python
# 判断是否为子集
is_subset = {1, 2}.issubset({1, 2, 3})
```

---

**基本写法：超集判断**
`<集合1>.issuperset(<集合2>)`

```python
# 判断是否为超集
is_superset = {1, 2, 3}.issuperset({1, 2})
```

---

**基本写法：不相交判断**
`<集合1>.isdisjoint(<集合2>)`

```python
# 判断两个集合是否不相交
is_disjoint = {1, 2}.isdisjoint({3, 4})
```

---

## 集合推导式

**基本写法：基本集合推导式**
`{<表达式> for <变量> in <可迭代对象>}`

```python
# 基本集合推导式
squares = {x ** 2 for x in range(5)}
```

---

**基本写法：带条件的集合推导式**
`{<表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的集合推导式
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
```

---

## collections 模块

**基本写法：使用 Counter 计数**
`Counter(<可迭代对象>)`

```python
# 使用 Counter 统计元素出现次数
from collections import Counter
word_count = Counter("hello world")
```

---

**基本写法：使用 defaultdict**
`defaultdict(<默认工厂>)`

```python
# 使用 defaultdict 设置默认值
from collections import defaultdict
word_list = defaultdict(list)
word_list["fruits"].append("apple")
```

---

**基本写法：使用 OrderedDict**
`OrderedDict([(<键>, <值>), (<键>, <值>)])`

```python
# 使用 OrderedDict 保持插入顺序
from collections import OrderedDict
ordered = OrderedDict([("a", 1), ("b", 2)])
```

---

**基本写法：使用 deque 双端队列**
`deque(<可迭代对象>)`

```python
# 使用 deque 创建双端队列
from collections import deque
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
```

---

**基本写法：deque 弹出左侧元素**
`<deque>.popleft()`

```python
# 从左侧弹出元素
first = queue.popleft()
```

---

## 冻结集合

**基本写法：创建冻结集合**
`frozenset(<可迭代对象>)`

```python
# 创建不可变的冻结集合
frozen = frozenset([1, 2, 3])
```

---

## 数据结构嵌套

**换行写法：嵌套字典列表**
`[`
`    {<键1>: <值1>, <键2>: <值2>},`
`    {<键1>: <值1>, <键2>: <值2>},`
`]`

```python
# 嵌套字典列表
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
]
```

---

**换行写法：嵌套字典字典**
`{`
`    <键1>: {<子键1>: <值1>},`
`    <键2>: {<子键2>: <值2>},`
`}`

```python
# 嵌套字典字典
matrix = {
    "row1": {"col1": 1, "col2": 2},
    "row2": {"col1": 3, "col2": 4},
}
```

---



<!-- ============ 文档分隔线：040-python/011-ComprehensionGenerator.md ============ -->

# 推导式与生成器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 列表推导式

**基本写法：基本列表推导式**
`[<表达式> for <变量> in <可迭代对象>]`

```python
# 基本列表推导式
squares = [x ** 2 for x in range(5)]
```

---

**基本写法：带条件的列表推导式**
`[<表达式> for <变量> in <可迭代对象> if <条件>]`

```python
# 带条件的列表推导式
evens = [x for x in range(10) if x % 2 == 0]
```

---

**基本写法：带 if-else 的列表推导式**
`[<表达式1> if <条件> else <表达式2> for <变量> in <可迭代对象>]`

```python
# 带 if-else 的列表推导式
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
```

---

## 嵌套列表推导式

**基本写法：嵌套 for 的列表推导式**
`[<表达式> for <变量1> in <可迭代对象1> for <变量2> in <可迭代对象2>]`

```python
# 嵌套 for 的列表推导式
pairs = [(x, y) for x in range(3) for y in range(3)]
```

---

**基本写法：带条件的嵌套推导式**
`[<表达式> for <变量1> in <可迭代对象1> for <变量2> in <可迭代对象2> if <条件>]`

```python
# 带条件的嵌套推导式
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
```

---

**换行写法：多行嵌套推导式**
`[<表达式>`
` for <变量1> in <可迭代对象1>`
` for <变量2> in <可迭代对象2>]`

```python
# 多行嵌套推导式
matrix = [
    [x * y for y in range(3)]
    for x in range(3)
]
```

---

## 字典推导式

**基本写法：基本字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象>}`

```python
# 基本字典推导式
squares = {x: x ** 2 for x in range(5)}
```

---

**基本写法：带条件的字典推导式**
`{<键表达式>: <值表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的字典推导式
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
```

---

**基本写法：反转字典键值**
`{<值>: <键> for <键>, <值> in <字典>.items()}`

```python
# 反转字典的键和值
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
```

---

## 集合推导式

**基本写法：基本集合推导式**
`{<表达式> for <变量> in <可迭代对象>}`

```python
# 基本集合推导式
squares = {x ** 2 for x in range(5)}
```

---

**基本写法：带条件的集合推导式**
`{<表达式> for <变量> in <可迭代对象> if <条件>}`

```python
# 带条件的集合推导式
even_squares = {x ** 2 for x in range(10) if x % 2 == 0}
```

---

## 生成器表达式

**基本写法：基本生成器表达式**
`(<表达式> for <变量> in <可迭代对象>)`

```python
# 基本生成器表达式
squares_gen = (x ** 2 for x in range(5))
print(next(squares_gen))
```

---

**基本写法：带条件的生成器表达式**
`(<表达式> for <变量> in <可迭代对象> if <条件>)`

```python
# 带条件的生成器表达式
evens_gen = (x for x in range(10) if x % 2 == 0)
print(list(evens_gen))
```

---

**基本写法：生成器表达式作为函数参数**
`<函数>(<表达式> for <变量> in <可迭代对象>)`

```python
# 生成器表达式作为函数参数
total = sum(x ** 2 for x in range(10))
```

---

## 生成器函数

**换行写法：定义生成器函数**
`def <函数名>(<参数>):`
`    yield <值>`

```python
# 定义生成器函数
def count_up_to(max_value):
    count = 0
    while count < max_value:
        yield count
        count += 1
```

---

**基本写法：使用生成器**
`for <变量> in <生成器>: <语句>`

```python
# 使用生成器
for num in count_up_to(5):
    print(num)
```

---

**基本写法：使用 next() 获取值**
`next(<生成器>)`

```python
# 使用 next() 获取生成器的下一个值
gen = count_up_to(3)
print(next(gen))
```

---

**基本写法：使用 list() 转换生成器**
`list(<生成器>)`

```python
# 将生成器转换为列表
gen = count_up_to(5)
print(list(gen))
```

---

## yield 语句

**基本写法：使用 yield 生成值**
`yield <值>`

```python
# 使用 yield 生成值
def simple_generator():
    yield 1
    yield 2
    yield 3
```

---

**基本写法：使用 yield from 委托生成器**
`yield from <可迭代对象>`

```python
# 使用 yield from 委托给子生成器
def combined_generator():
    yield from [1, 2, 3]
    yield from [4, 5, 6]
```

---

**基本写法：yield from 委托给另一个生成器**
`yield from <生成器函数>()`

```python
# yield from 委托给另一个生成器
def sub_generator():
    yield "a"
    yield "b"

def main_generator():
    yield "start"
    yield from sub_generator()
    yield "end"
```

---

## 生成器方法

**基本写法：使用 send() 发送值**
`<生成器>.send(<值>)`

```python
# 使用 send() 向生成器发送值
def echo_generator():
    while True:
        received = yield
        print(f"收到: {received}")

gen = echo_generator()
next(gen)
gen.send("Hello")
```

---

**基本写法：使用 throw() 抛出异常**
`<生成器>.throw(<异常>)`

```python
# 使用 throw() 在生成器中抛出异常
def safe_generator():
    try:
        while True:
            yield "正常"
    except ValueError:
        yield "捕获到异常"

gen = safe_generator()
print(next(gen))
print(gen.throw(ValueError))
```

---

**基本写法：使用 close() 关闭生成器**
`<生成器>.close()`

```python
# 使用 close() 关闭生成器
gen = count_up_to(10)
print(next(gen))
gen.close()
```

---

## 无限生成器

**换行写法：定义无限生成器**
`def <函数名>():`
`    while True:`
`        yield <值>`

```python
# 定义无限生成器
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1
```

---

**基本写法：使用 itertools.islice 限制无限生成器**
`islice(<无限生成器>, <n>)`

```python
# 使用 islice 限制无限生成器的输出
from itertools import islice

gen = infinite_counter()
first_ten = list(islice(gen, 10))
```

---

## 生成器管道

**换行写法：生成器管道组合**
`gen1 = (<表达式> for <变量> in <可迭代对象>)`
`gen2 = (<表达式> for <变量> in gen1)`
`gen3 = (<表达式> for <变量> in gen2)`

```python
# 生成器管道组合
numbers = range(100)
squared = (x ** 2 for x in numbers)
evens = (x for x in squared if x % 2 == 0)
result = list(evens)
```

---

## itertools 模块

**基本写法：使用 itertools.chain 连接**
`chain(<可迭代对象1>, <可迭代对象2>)`

```python
# 使用 chain 连接多个可迭代对象
from itertools import chain
combined = chain([1, 2, 3], [4, 5, 6])
print(list(combined))
```

---

**基本写法：使用 itertools.chain.from_iterable 展平**
`chain.from_iterable(<嵌套可迭代对象>)`

```python
# 使用 chain.from_iterable 展平嵌套列表
from itertools import chain
nested = [[1, 2], [3, 4], [5, 6]]
flat = chain.from_iterable(nested)
print(list(flat))
```

---

**基本写法：使用 itertools.product 笛卡尔积**
`product(<可迭代对象1>, <可迭代对象2>)`

```python
# 使用 product 生成笛卡尔积
from itertools import product
colors = ["red", "blue"]
sizes = ["S", "M"]
combinations = list(product(colors, sizes))
```

---

**基本写法：使用 itertools.combinations 组合**
`combinations(<可迭代对象>, <r>)`

```python
# 使用 combinations 生成所有组合
from itertools import combinations
combos = list(combinations([1, 2, 3, 4], 2))
```

---

**基本写法：使用 itertools.permutations 排列**
`permutations(<可迭代对象>, <r>)`

```python
# 使用 permutations 生成所有排列
from itertools import permutations
perms = list(permutations([1, 2, 3], 2))
```

---

**基本写法：使用 itertools.cycle 循环**
`cycle(<可迭代对象>)`

```python
# 使用 cycle 无限循环可迭代对象
from itertools import cycle
cycler = cycle(["A", "B", "C"])
first_five = [next(cycler) for _ in range(5)]
```

---

**基本写法：使用 itertools.repeat 重复**
`repeat(<元素>, <次数>)`

```python
# 使用 repeat 重复元素
from itertools import repeat
repeated = list(repeat("Hello", 3))
```

---

**基本写法：使用 itertools.starmap 应用函数**
`starmap(<函数>, <可迭代对象>)`

```python
# 使用 starmap 将函数应用于解包的参数
from itertools import starmap
pairs = [(2, 3), (4, 5), (6, 7)]
results = list(starmap(lambda x, y: x + y, pairs))
```

---

**基本写法：使用 itertools.groupby 分组**
`groupby(<可迭代对象>, <键函数>)`

```python
# 使用 groupby 按键分组
from itertools import groupby
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(f"{key}: {list(group)}")
```

---

**基本写法：使用 itertools.accumulate 累积**
`accumulate(<可迭代对象>, <函数>)`

```python
# 使用 accumulate 累积计算
from itertools import accumulate
numbers = [1, 2, 3, 4, 5]
cumsum = list(accumulate(numbers))
```

---

## 生成器与协程

**换行写法：定义协程生成器**
`def <协程名>():`
`    while True:`
`        <值> = yield`
`        <处理>`

```python
# 定义协程生成器
def coroutine():
    print("启动协程")
    while True:
        value = yield
        print(f"处理: {value}")

coro = coroutine()
next(coro)
coro.send("数据")
```

---

## 生成器表达式与列表推导式对比

**基本写法：列表推导式（立即计算）**
`[<表达式> for <变量> in <可迭代对象>]`

```python
# 列表推导式（立即计算，占用内存）
squares_list = [x ** 2 for x in range(1000000)]
```

---

**基本写法：生成器表达式（惰性计算）**
`(<表达式> for <变量> in <可迭代对象>)`

```python
# 生成器表达式（惰性计算，节省内存）
squares_gen = (x ** 2 for x in range(1000000))
```

---

## 生成器与迭代器

**换行写法：自定义迭代器类**
`class <迭代器类>:`
`    def __iter__(self): return self`
`    def __next__(self): <语句>`

```python
# 自定义迭代器类
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
```

---

**换行写法：可迭代对象类**
`class <可迭代对象类>:`
`    def __iter__(self): yield <值>`

```python
# 可迭代对象类（使用 yield）
class NumberRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
```

---

## 生成器与内存优化

**基本写法：使用生成器处理大文件**
`def <函数名>(<文件路径>):`
`    with open(<文件路径>) as f:`
`        for line in f: yield <处理>`

```python
# 使用生成器逐行处理大文件
def read_large_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()
```

---

**基本写法：使用生成器过滤数据**
`(<表达式> for <变量> in <可迭代对象> if <条件>)`

```python
# 使用生成器表达式过滤数据
data = range(1000000)
filtered = (x for x in data if x % 2 == 0)
result = sum(filtered)
```

---

## 生成器与 send() 双向通信

**换行写法：带 send() 的生成器**
`def <生成器名>():`
`    <初始化>`
`    while True:`
`        <输入> = yield <输出>`
`        <处理>`

```python
# 带 send() 的双向通信生成器
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

gen = accumulator()
next(gen)
print(gen.send(10))
print(gen.send(20))
```

---

## 生成器与 yield from

**换行写法：使用 yield from 委托**
`def <主生成器>():`
`    yield <值1>`
`    yield from <子生成器>()`
`    yield <值2>`

```python
# 使用 yield from 委托子生成器
def sub_generator():
    yield "sub1"
    yield "sub2"

def main_generator():
    yield "start"
    yield from sub_generator()
    yield "end"
```

---

**基本写法：yield from 返回值**
`result = yield from <生成器>`

```python
# yield from 获取子生成器的返回值
def sub_generator():
    yield 1
    yield 2
    return "完成"

def main_generator():
    result = yield from sub_generator()
    print(f"子生成器返回: {result}")
```



<!-- ============ 文档分隔线：040-python/012-FileIOContextManager.md ============ -->

# 文件IO与上下文管理器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件打开与关闭

**基本写法：使用 open() 打开文件**
`open(<文件路径>, <模式>)`

```python
# 使用 open() 打开文件
file = open("test.txt", "r")
content = file.read()
file.close()
```

---

**基本写法：使用 with 语句自动关闭**
`with open(<文件路径>, <模式>) as <变量>: <语句>`

```python
# 使用 with 语句自动管理文件资源
with open("test.txt", "r") as f:
    content = f.read()
```

---

## 文件读取

**基本写法：读取整个文件**
`<文件>.read()`

```python
# 读取整个文件内容
with open("test.txt", "r") as f:
    content = f.read()
```

---

**基本写法：读取指定字节数**
`<文件>.read(<字节数>)`

```python
# 读取指定字节数
with open("test.txt", "r") as f:
    content = f.read(100)
```

---

**基本写法：逐行读取**
`for <行> in <文件>: <语句>`

```python
# 逐行读取文件
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

**基本写法：使用 readline() 读取一行**
`<文件>.readline()`

```python
# 使用 readline() 读取一行
with open("test.txt", "r") as f:
    first_line = f.readline()
```

---

**基本写法：使用 readlines() 读取所有行**
`<文件>.readlines()`

```python
# 使用 readlines() 读取所有行为列表
with open("test.txt", "r") as f:
    lines = f.readlines()
```

---

## 文件写入

**基本写法：写入字符串**
`<文件>.write(<字符串>)`

```python
# 写入字符串到文件
with open("test.txt", "w") as f:
    f.write("Hello, World!")
```

---

**基本写法：写入多行**
`<文件>.writelines(<字符串列表>)`

```python
# 写入多行到文件
lines = ["line1\n", "line2\n", "line3\n"]
with open("test.txt", "w") as f:
    f.writelines(lines)
```

---

**基本写法：追加写入**
`with open(<文件路径>, "a") as <变量>: <语句>`

```python
# 追加写入到文件
with open("test.txt", "a") as f:
    f.write("追加的内容\n")
```

---

## 文件模式

**基本写法：读取模式**
`open(<文件路径>, "r")`

```python
# 读取模式（默认）
with open("test.txt", "r") as f:
    content = f.read()
```

---

**基本写法：写入模式**
`open(<文件路径>, "w")`

```python
# 写入模式（覆盖原有内容）
with open("test.txt", "w") as f:
    f.write("新内容")
```

---

**基本写法：追加模式**
`open(<文件路径>, "a")`

```python
# 追加模式（在文件末尾添加）
with open("test.txt", "a") as f:
    f.write("追加内容")
```

---

**基本写法：二进制读取模式**
`open(<文件路径>, "rb")`

```python
# 二进制读取模式
with open("image.png", "rb") as f:
    data = f.read()
```

---

**基本写法：二进制写入模式**
`open(<文件路径>, "wb")`

```python
# 二进制写入模式
with open("data.bin", "wb") as f:
    f.write(b"\x00\x01\x02")
```

---

**基本写法：读写模式**
`open(<文件路径>, "r+")`

```python
# 读写模式
with open("test.txt", "r+") as f:
    content = f.read()
    f.write("新内容")
```

---

## 文件指针操作

**基本写法：移动文件指针**
`<文件>.seek(<偏移量>)`

```python
# 移动文件指针到指定位置
with open("test.txt", "r") as f:
    f.seek(10)
    content = f.read()
```

---

**基本写法：获取文件指针位置**
`<文件>.tell()`

```python
# 获取当前文件指针位置
with open("test.txt", "r") as f:
    f.read(10)
    position = f.tell()
```

---

## 文件与目录操作

**基本写法：检查文件是否存在**
`os.path.exists(<路径>)`

```python
# 检查文件是否存在
import os
if os.path.exists("test.txt"):
    print("文件存在")
```

---

**基本写法：创建目录**
`os.makedirs(<目录路径>)`

```python
# 创建目录（包括父目录）
import os
os.makedirs("path/to/directory")
```

---

**基本写法：删除文件**
`os.remove(<文件路径>)`

```python
# 删除文件
import os
os.remove("test.txt")
```

---

**基本写法：删除目录**
`os.rmdir(<目录路径>)`

```python
# 删除空目录
import os
os.rmdir("empty_directory")
```

---

**基本写法：重命名文件**
`os.rename(<旧路径>, <新路径>)`

```python
# 重命名文件
import os
os.rename("old.txt", "new.txt")
```

---

**基本写法：列出目录内容**
`os.listdir(<目录路径>)`

```python
# 列出目录内容
import os
files = os.listdir(".")
```

---

**基本写法：使用 pathlib 操作路径**
`Path(<路径>)`

```python
# 使用 pathlib 操作路径
from pathlib import Path
path = Path("test.txt")
if path.exists():
    print("文件存在")
```

---

**基本写法：使用 pathlib 读取文件**
`Path(<路径>).read_text()`

```python
# 使用 pathlib 读取文件内容
from pathlib import Path
content = Path("test.txt").read_text()
```

---

**基本写法：使用 pathlib 写入文件**
`Path(<路径>).write_text(<内容>)`

```python
# 使用 pathlib 写入文件内容
from pathlib import Path
Path("test.txt").write_text("Hello, World!")
```

---

## JSON 文件处理

**基本写法：读取 JSON 文件**
`json.load(<文件>)`

```python
# 读取 JSON 文件
import json
with open("data.json", "r") as f:
    data = json.load(f)
```

---

**基本写法：写入 JSON 文件**
`json.dump(<对象>, <文件>)`

```python
# 写入 JSON 文件
import json
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f)
```

---

**基本写法：JSON 字符串与对象转换**
`json.loads(<字符串>)`

```python
# JSON 字符串转换为 Python 对象
import json
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)
```

---

**基本写法：Python 对象转换为 JSON 字符串**
`json.dumps(<对象>)`

```python
# Python 对象转换为 JSON 字符串
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
```

---

**基本写法：格式化 JSON 输出**
`json.dumps(<对象>, indent=<n>)`

```python
# 格式化 JSON 输出
import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data, indent=2)
```

---

## CSV 文件处理

**基本写法：读取 CSV 文件**
`csv.reader(<文件>)`

```python
# 读取 CSV 文件
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

**基本写法：使用 DictReader 读取 CSV**
`csv.DictReader(<文件>)`

```python
# 使用 DictReader 读取 CSV 为字典
import csv
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

---

**基本写法：写入 CSV 文件**
`csv.writer(<文件>)`

```python
# 写入 CSV 文件
import csv
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 30])
```

---

**基本写法：使用 DictWriter 写入 CSV**
`csv.DictWriter(<文件>, fieldnames=[<字段>])`

```python
# 使用 DictWriter 写入 CSV
import csv
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})
```

---

## 上下文管理器

**换行写法：自定义上下文管理器类**
`class <上下文管理器>:`
`    def __enter__(self): <语句>`
`    def __exit__(self, exc_type, exc_val, exc_tb): <语句>`

```python
# 自定义上下文管理器类
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
```

---

**基本写法：使用自定义上下文管理器**
`with <上下文管理器>(<参数>) as <变量>: <语句>`

```python
# 使用自定义上下文管理器
with FileManager("test.txt", "r") as f:
    content = f.read()
```

---

**换行写法：使用 contextlib.contextmanager**
`@contextmanager`
`def <函数名>(<参数>):`
`    <前置处理>`
`    yield <值>`
`    <后置处理>`

```python
# 使用 contextlib.contextmanager 装饰器
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()
```

---

**基本写法：使用 contextmanager 创建的上下文**
`with <函数名>(<参数>) as <变量>: <语句>`

```python
# 使用 contextmanager 创建的上下文管理器
with open_file("test.txt", "r") as f:
    content = f.read()
```

---

## contextlib 模块工具

**基本写法：使用 suppress 抑制异常**
`with suppress(<异常>): <语句>`

```python
# 使用 suppress 抑制特定异常
from contextlib import suppress

with suppress(FileNotFoundError):
    with open("nonexistent.txt", "r") as f:
        content = f.read()
```

---

**基本写法：使用 redirect_stdout 重定向输出**
`with redirect_stdout(<目标>): <语句>`

```python
# 使用 redirect_stdout 重定向标准输出
from contextlib import redirect_stdout
import io

output = io.StringIO()
with redirect_stdout(output):
    print("这会被重定向")
print(output.getvalue())
```

---

**基本写法：使用 redirect_stderr 重定向错误**
`with redirect_stderr(<目标>): <语句>`

```python
# 使用 redirect_stderr 重定向标准错误
from contextlib import redirect_stderr
import io

error_output = io.StringIO()
with redirect_stderr(error_output):
    import sys
    sys.stderr.write("错误信息")
```

---

**基本写法：使用 closing 自动关闭**
`with closing(<对象>) as <变量>: <语句>`

```python
# 使用 closing 自动关闭对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("http://example.com")) as response:
    content = response.read()
```

---

## 临时文件与目录

**基本写法：创建临时文件**
`tempfile.NamedTemporaryFile()`

```python
# 创建临时文件
import tempfile
with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
    f.write("临时内容")
    print(f.name)
```

---

**基本写法：创建临时目录**
`tempfile.TemporaryDirectory()`

```python
# 创建临时目录
import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
    print(f"临时目录: {tmpdir}")
```

---

## 文件编码处理

**基本写法：指定编码打开文件**
`open(<文件路径>, <模式>, encoding=<编码>)`

```python
# 指定编码打开文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

---

**基本写法：处理编码错误**
`open(<文件路径>, <模式>, encoding=<编码>, errors=<策略>)`

```python
# 处理编码错误
with open("test.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()
```

---

## 二进制文件处理

**基本写法：读取二进制文件**
`open(<文件路径>, "rb")`

```python
# 读取二进制文件
with open("image.png", "rb") as f:
    data = f.read()
```

---

**基本写法：写入二进制文件**
`open(<文件路径>, "wb")`

```python
# 写入二进制文件
with open("data.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03")
```

---

**基本写法：使用 pickle 序列化对象**
`pickle.dump(<对象>, <文件>)`

```python
# 使用 pickle 序列化对象到文件
import pickle
data = {"name": "Alice", "age": 30}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

---

**基本写法：使用 pickle 反序列化**
`pickle.load(<文件>)`

```python
# 使用 pickle 从文件反序列化
import pickle
with open("data.pkl", "rb") as f:
    data = pickle.load(f)
```

---

## 文件路径处理

**基本写法：拼接路径**
`os.path.join(<路径1>, <路径2>)`

```python
# 拼接路径
import os
path = os.path.join("folder", "subfolder", "file.txt")
```

---

**基本写法：获取文件名**
`os.path.basename(<路径>)`

```python
# 获取文件名
import os
filename = os.path.basename("/path/to/file.txt")
```

---

**基本写法：获取目录名**
`os.path.dirname(<路径>)`

```python
# 获取目录名
import os
dirname = os.path.dirname("/path/to/file.txt")
```

---

**基本写法：分割文件名和扩展名**
`os.path.splitext(<路径>)`

```python
# 分割文件名和扩展名
import os
name, ext = os.path.splitext("file.txt")
```

---

**基本写法：使用 pathlib 拼接路径**
`Path(<路径>) / <子路径>`

```python
# 使用 pathlib 拼接路径
from pathlib import Path
path = Path("folder") / "subfolder" / "file.txt"
```

---

**基本写法：使用 pathlib 获取文件名**
`Path(<路径>).name`

```python
# 使用 pathlib 获取文件名
from pathlib import Path
filename = Path("/path/to/file.txt").name
```

---

**基本写法：使用 pathlib 获取文件后缀**
`Path(<路径>).suffix`

```python
# 使用 pathlib 获取文件后缀
from pathlib import Path
ext = Path("file.txt").suffix
```

---

## 文件遍历

**基本写法：使用 os.walk 遍历目录**
`for <根>, <目录>, <文件> in os.walk(<路径>): <语句>`

```python
# 使用 os.walk 遍历目录树
import os
for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))
```

---

**基本写法：使用 pathlib 遍历目录**
`Path(<路径>).rglob(<模式>)`

```python
# 使用 pathlib 递归遍历目录
from pathlib import Path
for file in Path(".").rglob("*.py"):
    print(file)
```

---

**基本写法：使用 glob 模块匹配文件**
`glob.glob(<模式>, recursive=True)`

```python
# 使用 glob 模块匹配文件
import glob
files = glob.glob("**/*.py", recursive=True)
```

---

## 异步文件IO

**换行写法：使用 aiofiles 异步读写**
`import aiofiles`
`async with aiofiles.open(<路径>, <模式>) as f: await f.read()`

```python
# 使用 aiofiles 异步读写文件
import asyncio
import aiofiles

async def read_file(path):
    async with aiofiles.open(path, "r") as f:
        content = await f.read()
    return content
```

---

**基本写法：异步写入文件**
`await f.write(<内容>)`

```python
# 异步写入文件
async def write_file(path, content):
    async with aiofiles.open(path, "w") as f:
        await f.write(content)
```



<!-- ============ 文档分隔线：040-python/013-ExceptionHandling.md ============ -->

# 异常处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## try-except 语句

**基本写法：基本 try-except**
`try: <语句> except <异常>: <处理>`

```python
# 基本 try-except 异常处理
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除零错误")
```

---

**基本写法：捕获异常信息**
`try: <语句> except <异常> as <变量>: <处理>`

```python
# 捕获异常信息到变量
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误: {e}")
```

---

**基本写法：捕获多种异常**
`try: <语句> except (<异常1>, <异常2>): <处理>`

```python
# 捕获多种异常类型
try:
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"转换错误: {e}")
```

---

**换行写法：多 except 块**
`try: <语句>`
`except <异常1>: <处理1>`
`except <异常2>: <处理2>`

```python
# 多个 except 块分别处理不同异常
try:
    value = int(input("请输入数字: "))
    result = 10 / value
except ValueError:
    print("输入不是有效数字")
except ZeroDivisionError:
    print("不能除以零")
```

---

## try-except-else 语句

**基本写法：try-except-else**
`try: <语句> except <异常>: <处理> else: <无异常时执行>`

```python
# try-except-else 语句
try:
    value = int("123")
except ValueError:
    print("转换失败")
else:
    print(f"转换成功: {value}")
```

---

## try-finally 语句

**基本写法：try-finally**
`try: <语句> finally: <无论是否异常都执行>`

```python
# try-finally 语句
try:
    file = open("test.txt", "r")
    content = file.read()
finally:
    file.close()
```

---

## try-except-finally 语句

**换行写法：完整的异常处理结构**
`try: <语句>`
`except <异常>: <处理>`
`else: <无异常时执行>`
`finally: <清理>`

```python
# 完整的 try-except-else-finally 结构
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("文件不存在")
    content = ""
else:
    print("文件读取成功")
finally:
    file.close()
```

---

## 抛出异常

**基本写法：使用 raise 抛出异常**
`raise <异常>(<消息>)`

```python
# 使用 raise 抛出异常
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    return age
```

---

**基本写法：重新抛出当前异常**
`raise`

```python
# 重新抛出当前捕获的异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("记录错误日志")
    raise
```

---

**基本写法：抛出异常链**
`raise <新异常> from <原异常>`

```python
# 抛出异常链（保留原始异常）
try:
    result = 10 / 0
except ZeroDivisionError as e:
    raise RuntimeError("计算失败") from e
```

---

## 自定义异常

**换行写法：定义自定义异常类**
`class <异常类>(Exception):`
`    def __init__(self, <参数>): <语句>`

```python
# 定义自定义异常类
class InvalidAgeError(Exception):
    def __init__(self, age, message="年龄无效"):
        self.age = age
        self.message = message
        super().__init__(self.message)
```

---

**换行写法：定义带额外属性的自定义异常**
`class <异常类>(Exception):`
`    def __init__(self, <参数>):`
`        self.<属性> = <值>`
`        super().__init__(<消息>)`

```python
# 定义带额外属性的自定义异常
class DatabaseError(Exception):
    def __init__(self, query, error_code):
        self.query = query
        self.error_code = error_code
        super().__init__(f"Database error {error_code}: {query}")
```

---

**基本写法：使用自定义异常**
`raise <自定义异常>(<参数>)`

```python
# 使用自定义异常
def set_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return age
```

---

**基本写法：捕获自定义异常**
`try: <语句> except <自定义异常> as <变量>: <处理>`

```python
# 捕获自定义异常
try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"错误: {e.message}, 年龄: {e.age}")
```

---

## 异常层次结构

**基本写法：捕获 Exception 基类**
`try: <语句> except Exception: <处理>`

```python
# 捕获 Exception 基类（捕获所有非系统退出异常）
try:
    result = 10 / 0
except Exception as e:
    print(f"发生异常: {e}")
```

---

**基本写法：捕获 BaseException**
`try: <语句> except BaseException: <处理>`

```python
# 捕获 BaseException（包括 KeyboardInterrupt 等）
try:
    result = 10 / 0
except BaseException as e:
    print(f"发生异常: {e}")
```

---

## 常见内置异常

**基本写法：ValueError 值错误**
`raise ValueError(<消息>)`

```python
# 抛出 ValueError
def parse_int(value):
    if not value.isdigit():
        raise ValueError(f"无法转换为整数: {value}")
    return int(value)
```

---

**基本写法：TypeError 类型错误**
`raise TypeError(<消息>)`

```python
# 抛出 TypeError
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须是数字")
    return a + b
```

---

**基本写法：KeyError 键错误**
`raise KeyError(<键>)`

```python
# 抛出 KeyError
def get_value(dictionary, key):
    if key not in dictionary:
        raise KeyError(f"键不存在: {key}")
    return dictionary[key]
```

---

**基本写法：IndexError 索引错误**
`raise IndexError(<消息>)`

```python
# 抛出 IndexError
def get_item(lst, index):
    if index >= len(lst):
        raise IndexError(f"索引超出范围: {index}")
    return lst[index]
```

---

**基本写法：AttributeError 属性错误**
`raise AttributeError(<消息>)`

```python
# 抛出 AttributeError
class MyClass:
    pass

obj = MyClass()
if not hasattr(obj, "name"):
    raise AttributeError("对象没有 name 属性")
```

---

**基本写法：FileNotFoundError 文件未找到错误**
`raise FileNotFoundError(<文件路径>)`

```python
# 抛出 FileNotFoundError
import os

def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"文件不存在: {path}")
    with open(path, "r") as f:
        return f.read()
```

---

## 异常处理最佳实践

**基本写法：捕获具体异常**
`try: <语句> except <具体异常>: <处理>`

```python
# 捕获具体异常而非通用异常
try:
    value = int("abc")
except ValueError:
    print("值错误")
```

---

**基本写法：使用上下文管理器替代 try-finally**
`with <资源> as <变量>: <语句>`

```python
# 使用 with 语句替代 try-finally
with open("test.txt", "r") as f:
    content = f.read()
```

---

## 异常断言

**基本写法：使用 assert 断言**
`assert <条件>, <消息>`

```python
# 使用 assert 断言条件
def calculate_average(numbers):
    assert len(numbers) > 0, "列表不能为空"
    return sum(numbers) / len(numbers)
```

---

**基本写法：禁用 assert 优化**
`python -O <脚本>`

```python
# 使用 -O 选项运行时，assert 语句会被忽略
# 命令行执行：python -O script.py
```

---

## 异常组（Python 3.11+）

**基本写法：使用 ExceptionGroup**
`raise ExceptionGroup(<消息>, [<异常1>, <异常2>])`

```python
# 抛出异常组
errors = [
    ValueError("第一个错误"),
    TypeError("第二个错误"),
]
raise ExceptionGroup("多个错误发生", errors)
```

---

**基本写法：使用 except* 捕获异常组**
`try: <语句> except* <异常>: <处理>`

```python
# 使用 except* 捕获异常组中的特定类型
try:
    raise ExceptionGroup("错误组", [ValueError("值错误"), TypeError("类型错误")])
except* ValueError:
    print("捕获到 ValueError")
except* TypeError:
    print("捕获到 TypeError")
```

---

## 异常上下文

**基本写法：访问异常上下文**
`<异常>.__context__`

```python
# 访问异常的上下文（隐式链）
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        raise RuntimeError("处理失败")
except RuntimeError as e:
    print(f"异常: {e}")
    print(f"上下文: {e.__context__}")
```

---

**基本写法：访问异常原因**
`<异常>.__cause__`

```python
# 访问异常的原因（显式链）
try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("处理失败") from e
except RuntimeError as e:
    print(f"异常: {e}")
    print(f"原因: {e.__cause__}")
```

---

## 自定义异常处理

**换行写法：定义带异常处理的基类**
`class <基类>:`
`    def <方法>(self):`
`        try: <语句>`
`        except <异常>: <处理>`

```python
# 定义带异常处理的基类
class Repository:
    def find_by_id(self, entity_id):
        try:
            return self._fetch(entity_id)
        except KeyError:
            return None
        except Exception as e:
            raise DatabaseError(f"查询失败: {e}")
```

---

**换行写法：定义异常处理装饰器**
`def <装饰器名>(func):`
`    def wrapper(*args, **kwargs):`
`        try: return func(*args, **kwargs)`
`        except <异常>: <处理>`
`    return wrapper`

```python
# 定义异常处理装饰器
def handle_errors(default=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"错误: {e}")
                return default
        return wrapper
    return decorator
```

---

## 异常日志记录

**基本写法：使用 logging 记录异常**
`import logging`
`logging.exception(<消息>)`

```python
# 使用 logging 记录异常
import logging

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("发生除零错误")
```

---

**基本写法：使用 traceback 记录异常**
`import traceback`
`traceback.print_exc()`

```python
# 使用 traceback 打印异常堆栈
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    traceback.print_exc()
```

---

## 上下文管理器异常处理

**换行写法：自定义上下文管理器处理异常**
`class <上下文管理器>:`
`    def __enter__(self): <语句>`
`    def __exit__(self, exc_type, exc_val, exc_tb): <处理>`

```python
# 自定义上下文管理器处理异常
class SafeOperation:
    def __enter__(self):
        print("开始操作")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"捕获异常: {exc_val}")
            return True
        print("操作完成")
        return False
```

---

**基本写法：使用 contextlib.suppress 抑制异常**
`with suppress(<异常>): <语句>`

```python
# 使用 contextlib.suppress 抑制特定异常
from contextlib import suppress

with suppress(FileNotFoundError):
    with open("nonexistent.txt", "r") as f:
        content = f.read()
```

---

## 异常重试机制

**换行写法：实现重试装饰器**
`def <装饰器>(retries=<n>):`
`    def decorator(func):`
`        def wrapper(*args, **kwargs):`
`            for i in range(retries):`
`                try: return func(*args, **kwargs)`
`                except <异常>: <处理>`
`        return wrapper`
`    return decorator`

```python
# 实现重试装饰器
import time

def retry(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
```



<!-- ============ 文档分隔线：040-python/014-OperatorExpression.md ============ -->

# 运算符与表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 算术运算符

**基本写法：加法运算**
`<操作数1> + <操作数2>`

```python
# 加法运算
result = 10 + 5
```

---

**基本写法：减法运算**
`<操作数1> - <操作数2>`

```python
# 减法运算
result = 10 - 5
```

---

**基本写法：乘法运算**
`<操作数1> * <操作数2>`

```python
# 乘法运算
result = 10 * 5
```

---

**基本写法：除法运算**
`<操作数1> / <操作数2>`

```python
# 除法运算（返回浮点数）
result = 10 / 3
```

---

**基本写法：整除运算**
`<操作数1> // <操作数2>`

```python
# 整除运算（向下取整）
result = 10 // 3
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`

```python
# 取模运算（求余数）
result = 10 % 3
```

---

**基本写法：幂运算**
`<操作数1> ** <操作数2>`

```python
# 幂运算
result = 2 ** 3
```

---

**基本写法：负号运算**
`-<操作数>`

```python
# 负号运算
result = -10
```

---

**基本写法：正号运算**
`+<操作数>`

```python
# 正号运算
result = +10
```

---

## 复合赋值运算符

**基本写法：加法赋值**
`<变量> += <值>`

```python
# 加法赋值运算
x = 10
x += 5
```

---

**基本写法：减法赋值**
`<变量> -= <值>`

```python
# 减法赋值运算
x = 10
x -= 5
```

---

**基本写法：乘法赋值**
`<变量> *= <值>`

```python
# 乘法赋值运算
x = 10
x *= 5
```

---

**基本写法：除法赋值**
`<变量> /= <值>`

```python
# 除法赋值运算
x = 10
x /= 5
```

---

**基本写法：整除赋值**
`<变量> //= <值>`

```python
# 整除赋值运算
x = 10
x //= 3
```

---

**基本写法：取模赋值**
`<变量> %= <值>`

```python
# 取模赋值运算
x = 10
x %= 3
```

---

**基本写法：幂运算赋值**
`<变量> **= <值>`

```python
# 幂运算赋值
x = 2
x **= 3
```

---

## 比较运算符

**基本写法：等于比较**
`<操作数1> == <操作数2>`

```python
# 等于比较
result = (5 == 5)
```

---

**基本写法：不等于比较**
`<操作数1> != <操作数2>`

```python
# 不等于比较
result = (5 != 3)
```

---

**基本写法：大于比较**
`<操作数1> > <操作数2>`

```python
# 大于比较
result = (5 > 3)
```

---

**基本写法：小于比较**
`<操作数1> < <操作数2>`

```python
# 小于比较
result = (5 < 10)
```

---

**基本写法：大于等于比较**
`<操作数1> >= <操作数2>`

```python
# 大于等于比较
result = (5 >= 5)
```

---

**基本写法：小于等于比较**
`<操作数1> <= <操作数2>`

```python
# 小于等于比较
result = (5 <= 10)
```

---

## 链式比较

**基本写法：链式比较运算**
`<值1> < <值2> < <值3>`

```python
# 链式比较（等价于 1 < 2 and 2 < 3）
result = 1 < 2 < 3
```

---

## 逻辑运算符

**基本写法：逻辑与运算**
`<表达式1> and <表达式2>`

```python
# 逻辑与运算
result = True and False
```

---

**基本写法：逻辑或运算**
`<表达式1> or <表达式2>`

```python
# 逻辑或运算
result = True or False
```

---

**基本写法：逻辑非运算**
`not <表达式>`

```python
# 逻辑非运算
result = not True
```

---

## 短路求值

**基本写法：and 短路返回**
`<表达式1> and <表达式2>`

```python
# and 短路求值，第一个为 False 时返回第一个值
result = False and expensive_operation()
```

---

**基本写法：or 短路返回**
`<表达式1> or <表达式2>`

```python
# or 短路求值，第一个为 True 时返回第一个值
result = True or expensive_operation()
```

---

## 身份运算符

**基本写法：is 身份比较**
`<对象1> is <对象2>`

```python
# is 身份比较（判断是否为同一对象）
a = [1, 2, 3]
b = a
result = (a is b)
```

---

**基本写法：is not 身份比较**
`<对象1> is not <对象2>`

```python
# is not 身份比较
a = [1, 2, 3]
b = [1, 2, 3]
result = (a is not b)
```

---

**基本写法：使用 is 检查 None**
`<变量> is None`

```python
# 使用 is 检查 None
x = None
result = (x is None)
```

---

## 成员运算符

**基本写法：in 成员判断**
`<元素> in <容器>`

```python
# in 成员判断
result = 3 in [1, 2, 3]
```

---

**基本写法：not in 成员判断**
`<元素> not in <容器>`

```python
# not in 成员判断
result = 4 not in [1, 2, 3]
```

---

**基本写法：字符串成员判断**
`<子串> in <字符串>`

```python
# 字符串子串判断
result = "World" in "Hello, World!"
```

---

**基本写法：字典键成员判断**
`<键> in <字典>`

```python
# 字典键成员判断
result = "name" in {"name": "Alice", "age": 30}
```

---

## 位运算符

**基本写法：按位与运算**
`<操作数1> & <操作数2>`

```python
# 按位与运算
result = 5 & 3
```

---

**基本写法：按位或运算**
`<操作数1> | <操作数2>`

```python
# 按位或运算
result = 5 | 3
```

---

**基本写法：按位异或运算**
`<操作数1> ^ <操作数2>`

```python
# 按位异或运算
result = 5 ^ 3
```

---

**基本写法：按位取反运算**
`~<操作数>`

```python
# 按位取反运算
result = ~5
```

---

**基本写法：左移运算**
`<操作数> << <位数>`

```python
# 左移运算
result = 5 << 2
```

---

**基本写法：右移运算**
`<操作数> >> <位数>`

```python
# 右移运算
result = 20 >> 2
```

---

## 三元条件运算符

**单行写法：三元条件表达式**
`<值1> if <条件> else <值2>`

```python
# 三元条件表达式
age = 20
status = "Adult" if age >= 18 else "Minor"
```

---

**单行写法：嵌套三元表达式**
`<值1> if <条件1> else (<值2> if <条件2> else <值3>)`

```python
# 嵌套三元表达式
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
```

---

## 运算符优先级

**基本写法：使用括号改变优先级**
`(<表达式>)`

```python
# 使用括号明确运算优先级
result = (2 + 3) * 4
```

---

## 海象运算符

**基本写法：赋值表达式**
`(<变量> := <值>)`

```python
# 海象运算符（赋值表达式）
if (n := len([1, 2, 3])) > 2:
    print(f"List has {n} elements")
```

---

**基本写法：在 while 循环中使用海象运算符**
`while (<变量> := <表达式>): <语句>`

```python
# 在 while 循环中使用海象运算符
while (line := input()) != "quit":
    print(line)
```

---

**基本写法：在列表推导式中使用海象运算符**
`[<变量> for <元素> in <可迭代对象> if (<变量> := <表达式>)]`

```python
# 在列表推导式中使用海象运算符
data = [1, 2, 3, 4, 5]
results = [y for x in data if (y := x * 2) > 4]
```

---

## 表达式求值

**基本写法：使用 eval() 求值**
`eval(<字符串表达式>)`

```python
# 使用 eval() 求值字符串表达式
result = eval("2 + 3 * 4")
```

---

## 运算符重载

**换行写法：通过魔术方法重载运算符**
`class <类名>:`
`    def __<运算符方法>__(self, <参数>): <语句>`

```python
# 通过 __add__ 方法重载加法运算符
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

---

**基本写法：重载等于运算符**
`def __eq__(self, other): <语句>`

```python
# 通过 __eq__ 方法重载等于运算符
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

**基本写法：重载小于运算符**
`def __lt__(self, other): <语句>`

```python
# 通过 __lt__ 方法重载小于运算符
class Student:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score
```

---

**基本写法：重载字符串表示**
`def __repr__(self): <语句>`

```python
# 通过 __repr__ 方法重载字符串表示
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name!r})"
```

---

**基本写法：重载长度运算**
`def __len__(self): <语句>`

```python
# 通过 __len__ 方法重载 len() 函数
class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
```

---

**基本写法：重载成员判断**
`def __contains__(self, item): <语句>`

```python
# 通过 __contains__ 方法重载 in 运算符
class Matrix:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return any(item in row for row in self.data)
```

---



<!-- ============ 文档分隔线：040-python/015-Regex.md ============ -->

# 正则表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## re 模块导入

**基本写法：导入 re 模块**
`import re`

```python
# 导入正则表达式模块
import re
```

---

## 基本匹配

**基本写法：使用 re.match 从开头匹配**
`re.match(<模式>, <字符串>)`

```python
# 从字符串开头匹配
result = re.match(r"Hello", "Hello, World!")
```

---

**基本写法：使用 re.search 搜索**
`re.search(<模式>, <字符串>)`

```python
# 在字符串中搜索第一个匹配
result = re.search(r"World", "Hello, World!")
```

---

**基本写法：使用 re.findall 查找所有匹配**
`re.findall(<模式>, <字符串>)`

```python
# 查找所有匹配项
results = re.findall(r"\d+", "abc123def456")
```

---

**基本写法：使用 re.finditer 迭代匹配**
`re.finditer(<模式>, <字符串>)`

```python
# 迭代所有匹配项
for match in re.finditer(r"\d+", "abc123def456"):
    print(match.group())
```

---

## 匹配对象操作

**基本写法：获取匹配的字符串**
`<匹配对象>.group()`

```python
# 获取匹配的字符串
match = re.search(r"\d+", "abc123def")
print(match.group())
```

---

**基本写法：获取匹配的起始位置**
`<匹配对象>.start()`

```python
# 获取匹配的起始位置
match = re.search(r"\d+", "abc123def")
print(match.start())
```

---

**基本写法：获取匹配的结束位置**
`<匹配对象>.end()`

```python
# 获取匹配的结束位置
match = re.search(r"\d+", "abc123def")
print(match.end())
```

---

**基本写法：获取匹配的 span**
`<匹配对象>.span()`

```python
# 获取匹配的起止位置元组
match = re.search(r"\d+", "abc123def")
print(match.span())
```

---

## 字符类

**基本写法：匹配数字**
`\d`

```python
# 匹配数字
result = re.findall(r"\d+", "abc123def456")
```

---

**基本写法：匹配非数字**
`\D`

```python
# 匹配非数字字符
result = re.findall(r"\D+", "abc123def456")
```

---

**基本写法：匹配单词字符**
`\w`

```python
# 匹配字母、数字、下划线
result = re.findall(r"\w+", "hello_world 123!")
```

---

**基本写法：匹配非单词字符**
`\W`

```python
# 匹配非单词字符
result = re.findall(r"\W+", "hello_world 123!")
```

---

**基本写法：匹配空白字符**
`\s`

```python
# 匹配空白字符
result = re.findall(r"\s+", "hello world\ttab")
```

---

**基本写法：匹配非空白字符**
`\S`

```python
# 匹配非空白字符
result = re.findall(r"\S+", "hello world")
```

---

**基本写法：使用字符集合**
`[<字符集合>]`

```python
# 匹配方括号内的任意字符
result = re.findall(r"[aeiou]", "hello world")
```

---

**基本写法：使用字符范围**
`[<起始>-<结束>]`

```python
# 匹配 a 到 z 的小写字母
result = re.findall(r"[a-z]+", "Hello World 123")
```

---

**基本写法：使用否定字符集合**
`[^<字符集合>]`

```python
# 匹配不在方括号内的字符
result = re.findall(r"[^aeiou]", "hello world")
```

---

## 量词

**基本写法：匹配 0 次或多次**
`<字符>*`

```python
# 匹配 0 次或多次
result = re.findall(r"ab*", "a ab abb abbb")
```

---

**基本写法：匹配 1 次或多次**
`<字符>+`

```python
# 匹配 1 次或多次
result = re.findall(r"ab+", "a ab abb abbb")
```

---

**基本写法：匹配 0 次或 1 次**
`<字符>?`

```python
# 匹配 0 次或 1 次
result = re.findall(r"ab?", "a ab abb")
```

---

**基本写法：匹配指定次数**
`<字符>{<次数>}`

```python
# 匹配恰好 3 次
result = re.findall(r"\d{3}", "12 123 1234")
```

---

**基本写法：匹配至少 n 次**
`<字符>{<次数>,}`

```python
# 匹配至少 2 次
result = re.findall(r"\d{2,}", "1 12 123 1234")
```

---

**基本写法：匹配 n 到 m 次**
`<字符>{<n>,<m>}`

```python
# 匹配 2 到 4 次
result = re.findall(r"\d{2,4}", "1 12 123 1234 12345")
```

---

## 锚点

**基本写法：匹配字符串开头**
`^<模式>`

```python
# 匹配字符串开头
result = re.match(r"^Hello", "Hello, World!")
```

---

**基本写法：匹配字符串结尾**
`<模式>$`

```python
# 匹配字符串结尾
result = re.search(r"World!$", "Hello, World!")
```

---

**基本写法：匹配单词边界**
`\b<模式>\b`

```python
# 匹配完整单词
result = re.findall(r"\bcat\b", "cat category cat")
```

---

## 分组与捕获

**基本写法：使用括号分组**
`(<模式>)`

```python
# 使用括号创建捕获组
match = re.search(r"(\d+)-(\d+)", "电话: 123-456")
print(match.group(1))
print(match.group(2))
```

---

**基本写法：获取所有分组**
`<匹配对象>.groups()`

```python
# 获取所有分组
match = re.search(r"(\d+)-(\d+)", "电话: 123-456")
print(match.groups())
```

---

**基本写法：命名分组**
`(?P<<名称><模式>)`

```python
# 使用命名分组
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "日期: 2024-01")
print(match.group("year"))
print(match.group("month"))
```

---

**基本写法：非捕获分组**
`(?:<模式>)`

```python
# 使用非捕获分组
result = re.findall(r"(?:ab)+", "ababab ab")
```

---

**基本写法：引用分组**
`\<分组号>`

```python
# 引用前面的分组
result = re.findall(r"(\w+)\s+\1", "hello hello world world")
```

---

## 替换操作

**基本写法：使用 re.sub 替换**
`re.sub(<模式>, <替换>, <字符串>)`

```python
# 替换所有匹配项
result = re.sub(r"\d+", "N", "abc123def456")
```

---

**基本写法：限制替换次数**
`re.sub(<模式>, <替换>, <字符串>, count=<n>)`

```python
# 只替换前 1 个匹配项
result = re.sub(r"\d+", "N", "abc123def456", count=1)
```

---

**基本写法：使用函数替换**
`re.sub(<模式>, <函数>, <字符串>)`

```python
# 使用函数进行替换
def double(match):
    return str(int(match.group()) * 2)

result = re.sub(r"\d+", double, "abc123def456")
```

---

**基本写法：使用反向引用替换**
`re.sub(r"<模式>", r"<替换>", <字符串>)`

```python
# 使用反向引用进行替换
result = re.sub(r"(\w+),(\w+)", r"\2,\1", "hello,world")
```

---

## 分割操作

**基本写法：使用 re.split 分割**
`re.split(<模式>, <字符串>)`

```python
# 按模式分割字符串
result = re.split(r"\s+", "hello   world   python")
```

---

**基本写法：限制分割次数**
`re.split(<模式>, <字符串>, maxsplit=<n>)`

```python
# 限制分割次数
result = re.split(r"\s+", "hello world python", maxsplit=1)
```

---

## 编译正则表达式

**基本写法：编译正则表达式**
`re.compile(<模式>)`

```python
# 编译正则表达式
pattern = re.compile(r"\d+")
result = pattern.findall("abc123def456")
```

---

**基本写法：使用编译后的模式匹配**
`<模式>.match(<字符串>)`

```python
# 使用编译后的模式
pattern = re.compile(r"\d+")
match = pattern.match("123abc")
```

---

**基本写法：使用编译后的模式搜索**
`<模式>.search(<字符串>)`

```python
# 使用编译后的模式搜索
pattern = re.compile(r"\d+")
match = pattern.search("abc123def")
```

---

**基本写法：使用编译后的模式查找所有**
`<模式>.findall(<字符串>)`

```python
# 使用编译后的模式查找所有
pattern = re.compile(r"\d+")
results = pattern.findall("abc123def456")
```

---

**基本写法：使用编译后的模式替换**
`<模式>.sub(<替换>, <字符串>)`

```python
# 使用编译后的模式替换
pattern = re.compile(r"\d+")
result = pattern.sub("N", "abc123def456")
```

---

## 标志位

**基本写法：忽略大小写**
`re.IGNORECASE`

```python
# 忽略大小写匹配
result = re.findall(r"hello", "Hello HELLO hello", re.IGNORECASE)
```

---

**基本写法：多行模式**
`re.MULTILINE`

```python
# 多行模式下 ^ 和 $ 匹配每行
result = re.findall(r"^\w+", "line1\nline2\nline3", re.MULTILINE)
```

---

**基本写法：点号匹配所有**
`re.DOTALL`

```python
# 点号匹配包括换行符
result = re.findall(r".+", "line1\nline2", re.DOTALL)
```

---

**基本写法：组合多个标志位**
`re.IGNORECASE | re.MULTILINE`

```python
# 组合多个标志位
result = re.findall(r"^hello", "Hello\nhello\nHELLO", re.IGNORECASE | re.MULTILINE)
```

---

**基本写法：使用内联标志**
`(?<标志><模式>)`

```python
# 使用内联标志
result = re.findall(r"(?i)hello", "Hello HELLO hello")
```

---

## 贪婪与非贪婪

**基本写法：贪婪匹配**
`<字符>*`

```python
# 贪婪匹配（尽可能多匹配）
result = re.findall(r"<.*>", "<a><b><c>")
```

---

**基本写法：非贪婪匹配**
`<字符>*?`

```python
# 非贪婪匹配（尽可能少匹配）
result = re.findall(r"<.*?>", "<a><b><c>")
```

---

**基本写法：非贪婪加号**
`<字符>+?`

```python
# 非贪婪加号
result = re.findall(r"\d+?", "12345")
```

---

## 前瞻与后顾

**基本写法：正向前瞻**
`<模式>(?=<前瞻模式>)`

```python
# 正向前瞻（匹配后面跟着的）
result = re.findall(r"\d+(?= dollars)", "100 dollars 200 euros")
```

---

**基本写法：负向前瞻**
`<模式>(?!<前瞻模式>)`

```python
# 负向前瞻（匹配后面不跟着的）
result = re.findall(r"\d+(?! dollars)", "100 dollars 200 euros")
```

---

**基本写法：正向后顾**
`(?<=<后顾模式>)<模式>`

```python
# 正向后顾（匹配前面是...的）
result = re.findall(r"(?<=\$)\d+", "$100 and $200")
```

---

**基本写法：负向后顾**
`(?<!<后顾模式>)<模式>`

```python
# 负向后顾（匹配前面不是...的）
result = re.findall(r"(?<!\$)\d+", "$100 and 200")
```

---

## 常用正则模式

**基本写法：匹配邮箱**
`r"[\w.+-]+@[\w-]+\.[\w.]+"`

```python
# 匹配邮箱地址
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", "联系: alice@example.com")
```

---

**基本写法：匹配 URL**
`r"https?://[\w./-]+"`

```python
# 匹配 URL
urls = re.findall(r"https?://[\w./-]+", "访问 https://example.com 或 http://test.org")
```

---

**基本写法：匹配手机号**
`r"1[3-9]\d{9}"`

```python
# 匹配中国大陆手机号
phones = re.findall(r"1[3-9]\d{9}", "电话: 13812345678")
```

---

**基本写法：匹配 IP 地址**
`r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"`

```python
# 匹配 IP 地址
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "IP: 192.168.1.1")
```

---

**基本写法：匹配日期**
`r"\d{4}-\d{2}-\d{2}"`

```python
# 匹配日期
dates = re.findall(r"\d{4}-\d{2}-\d{2}", "日期: 2024-01-15")
```

---

## 字符串方法与正则对比

**基本写法：使用字符串方法替换**
`<字符串>.replace(<旧>, <新>)`

```python
# 使用字符串方法替换
result = "hello world".replace("world", "python")
```

---

**基本写法：使用正则替换**
`re.sub(<模式>, <替换>, <字符串>)`

```python
# 使用正则替换
result = re.sub(r"\s+", "_", "hello   world")
```

---

## 验证与提取

**基本写法：验证邮箱格式**
`re.match(<模式>, <字符串>)`

```python
# 验证邮箱格式
def is_valid_email(email):
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.]+$"
    return bool(re.match(pattern, email))
```

---

**基本写法：提取数字**
`re.findall(r"\d+", <字符串>)`

```python
# 从字符串中提取所有数字
numbers = re.findall(r"\d+", "价格: 100元，数量: 5个")
```

---

**基本写法：提取 URL**
`re.findall(r"https?://[\w./-]+", <字符串>)`

```python
# 从文本中提取 URL
text = "访问 https://example.com 了解更多"
urls = re.findall(r"https?://[\w./-]+", text)
```



<!-- ============ 文档分隔线：040-python/016-Decorator.md ============ -->

# 装饰器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本装饰器

**换行写法：定义基本装饰器**
`def <装饰器名>(func):`
`    def wrapper(*args, **kwargs):`
`        <前置处理>`
`        result = func(*args, **kwargs)`
`        <后置处理>`
`        return result`
`    return wrapper`

```python
# 定义基本装饰器
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("函数执行前")
        result = func(*args, **kwargs)
        print("函数执行后")
        return result
    return wrapper
```

---

**基本写法：使用装饰器**
`@<装饰器名>`
`def <函数名>(<参数>): <语句>`

```python
# 使用装饰器装饰函数
@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")
```

---

**基本写法：手动应用装饰器**
`<函数> = <装饰器>(<函数>)`

```python
# 手动应用装饰器
def say_hello(name):
    print(f"Hello, {name}!")

say_hello = my_decorator(say_hello)
```

---

## 带参数的装饰器

**换行写法：定义带参数的装饰器**
`def <装饰器名>(<参数>):`
`    def decorator(func):`
`        def wrapper(*args, **kwargs): <语句>`
`        return wrapper`
`    return decorator`

```python
# 定义带参数的装饰器
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

---

**基本写法：使用带参数的装饰器**
`@<装饰器名>(<参数>)`
`def <函数名>(<参数>): <语句>`

```python
# 使用带参数的装饰器
@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")
```

---

## functools.wraps 保留元信息

**换行写法：使用 @wraps 保留元信息**
`from functools import wraps`
`def <装饰器名>(func):`
`    @wraps(func)`
`    def wrapper(*args, **kwargs): <语句>`
`    return wrapper`

```python
# 使用 @wraps 保留原函数的元信息
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## 类装饰器

**换行写法：使用类作为装饰器**
`class <装饰器类>:`
`    def __init__(self, func): self.func = func`
`    def __call__(self, *args, **kwargs): <语句>`

```python
# 使用类作为装饰器
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数: {self.count}")
        return self.func(*args, **kwargs)
```

---

**基本写法：使用类装饰器**
`@<装饰器类>`
`def <函数名>(<参数>): <语句>`

```python
# 使用类装饰器
@CountCalls
def say_hello():
    print("Hello!")
```

---

## 带参数的类装饰器

**换行写法：定义带参数的类装饰器**
`class <装饰器类>:`
`    def __init__(self, <参数>): <语句>`
`    def __call__(self, func): <返回包装函数>`

```python
# 定义带参数的类装饰器
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper
```

---

## 方法装饰器

**换行写法：装饰类的方法**
`class <类名>:`
`    @<装饰器名>`
`    def <方法名>(self, <参数>): <语句>`

```python
# 装饰类的方法
class MyClass:
    @my_decorator
    def my_method(self):
        print("方法执行")
```

---

## 属性装饰器

**基本写法：使用 @property 定义属性**
`@property`
`def <属性名>(self): return <值>`

```python
# 使用 @property 定义只读属性
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

---

**基本写法：使用 @staticmethod 定义静态方法**
`@staticmethod`
`def <方法名>(<参数>): <语句>`

```python
# 使用 @staticmethod 定义静态方法
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
```

---

**基本写法：使用 @classmethod 定义类方法**
`@classmethod`
`def <方法名>(cls, <参数>): <语句>`

```python
# 使用 @classmethod 定义类方法
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
        return cls.count
```

---

## 多个装饰器叠加

**换行写法：叠加多个装饰器**
`@<装饰器1>`
`@<装饰器2>`
`def <函数名>(<参数>): <语句>`

```python
# 叠加多个装饰器（从下往上执行）
@decorator1
@decorator2
def my_function():
    print("Hello")
```

---

## 常用内置装饰器

**基本写法：使用 @staticmethod**
`@staticmethod`
`def <方法名>(<参数>): <语句>`

```python
# 使用 @staticmethod
class MyClass:
    @staticmethod
    def static_method():
        return "静态方法"
```

---

**基本写法：使用 @classmethod**
`@classmethod`
`def <方法名>(cls, <参数>): <语句>`

```python
# 使用 @classmethod
class MyClass:
    @classmethod
    def class_method(cls):
        return "类方法"
```

---

**基本写法：使用 @property**
`@property`
`def <属性名>(self): <语句>`

```python
# 使用 @property
class MyClass:
    @property
    def value(self):
        return self._value
```

---

**基本写法：使用 @abstractmethod**
`@abstractmethod`
`def <方法名>(self): <语句>`

```python
# 使用 @abstractmethod 定义抽象方法
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

---

**基本写法：使用 @dataclass**
`@dataclass`
`class <类名>: <类体>`

```python
# 使用 @dataclass
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

---

**基本写法：使用 @lru_cache**
`@lru_cache(maxsize=<n>)`
`def <函数名>(<参数>): <语句>`

```python
# 使用 @lru_cache 缓存函数结果
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## 装饰器实战

**换行写法：计时装饰器**
`def <装饰器名>(func):`
`    @wraps(func)`
`    def wrapper(*args, **kwargs):`
`        start = time.time()`
`        result = func(*args, **kwargs)`
`        end = time.time()`
`        print(f"耗时: {end - start}")`
`        return result`
`    return wrapper`

```python
# 计时装饰器
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.4f} 秒")
        return result
    return wrapper
```

---

**换行写法：日志装饰器**
`def <装饰器名>(func):`
`    @wraps(func)`
`    def wrapper(*args, **kwargs):`
`        print(f"调用 {func.__name__}, 参数: {args}, {kwargs}")`
`        result = func(*args, **kwargs)`
`        print(f"返回: {result}")`
`        return result`
`    return wrapper`

```python
# 日志装饰器
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}, 参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"返回: {result}")
        return result
    return wrapper
```

---

**换行写法：权限验证装饰器**
`def <装饰器名>(<权限参数>):`
`    def decorator(func):`
`        @wraps(func)`
`        def wrapper(*args, **kwargs):`
`            if not <检查权限>: raise <异常>`
`            return func(*args, **kwargs)`
`        return wrapper`
`    return decorator`

```python
# 权限验证装饰器
from functools import wraps

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not has_role(role):
                raise PermissionError(f"需要 {role} 权限")
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

---

**换行写法：重试装饰器**
`def <装饰器名>(max_retries=<n>):`
`    def decorator(func):`
`        @wraps(func)`
`        def wrapper(*args, **kwargs):`
`            for attempt in range(max_retries):`
`                try: return func(*args, **kwargs)`
`                except <异常>: <处理>`
`        return wrapper`
`    return decorator`

```python
# 重试装饰器
import time
from functools import wraps

def retry(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
```

---

**换行写法：缓存装饰器**
`def <装饰器名>(func):`
`    cache = {}`
`    @wraps(func)`
`    def wrapper(*args):`
`        if args not in cache: cache[args] = func(*args)`
`        return cache[args]`
`    return wrapper`

```python
# 自定义缓存装饰器
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

---

## 装饰器类实战

**换行写法：使用类实现计数装饰器**
`class <装饰器类>:`
`    def __init__(self, func):`
`        self.func = func`
`        self.count = 0`
`    def __call__(self, *args, **kwargs):`
`        self.count += 1`
`        return self.func(*args, **kwargs)`

```python
# 使用类实现计数装饰器
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"调用次数: {self.count}")
        return self.func(*args, **kwargs)
```

---

## 装饰器堆栈

**换行写法：多个装饰器组合使用**
`@<装饰器1>`
`@<装饰器2>`
`@<装饰器3>`
`def <函数名>(<参数>): <语句>`

```python
# 多个装饰器组合使用
@timer
@logger
@retry(max_retries=3)
def fetch_data(url):
    print(f"从 {url} 获取数据")
    return "data"
```

---

## 装饰器与元信息

**基本写法：访问装饰后的函数名**
`<函数>.__name__`

```python
# 访问装饰后的函数名（使用 @wraps 保留原信息）
@my_decorator
def my_function():
    pass

print(my_function.__name__)
```

---

**基本写法：访问装饰后的函数文档**
`<函数>.__doc__`

```python
# 访问装饰后的函数文档
@my_decorator
def my_function():
    """这是函数文档"""
    pass

print(my_function.__doc__)
```

---

## functools 模块工具

**基本写法：使用 @wraps**
`@wraps(<原函数>)`

```python
# 使用 @wraps 保留原函数元信息
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

**基本写法：使用 @lru_cache**
`@lru_cache(maxsize=<n>)`

```python
# 使用 @lru_cache 实现缓存
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    return sum(i * i for i in range(n))
```

---

**基本写法：使用 @cache**
`@cache`

```python
# 使用 @cache 无限缓存
from functools import cache

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

**基本写法：使用 @cached_property**
`@cached_property`
`def <属性名>(self): <语句>`

```python
# 使用 @cached_property 缓存属性计算结果
from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14159 * self.radius ** 2
```

---

**基本写法：使用 @singledispatch**
`@singledispatch`
`def <函数名>(<参数>): <语句>`

```python
# 使用 @singledispatch 实现函数重载
from functools import singledispatch

@singledispatch
def process(data):
    raise TypeError(f"不支持的类型: {type(data)}")

@process.register
def _(data: int):
    return f"处理整数: {data}"
```

---

**基本写法：注册 singledispatch 处理器**
`@<函数>.register`
`def _(<参数>: <类型>): <语句>`

```python
# 注册 singledispatch 的字符串处理器
@process.register
def _(data: str):
    return f"处理字符串: {data}"
```

---

## 装饰器与类型注解

**换行写法：带类型注解的装饰器**
`from typing import Callable, TypeVar`
`T = TypeVar("T")`
`def <装饰器名>(func: Callable[..., T]) -> Callable[..., T]:`
`    def wrapper(*args, **kwargs) -> T: return func(*args, **kwargs)`
`    return wrapper`

```python
# 带类型注解的装饰器
from typing import Callable, TypeVar, Any
from functools import wraps

T = TypeVar("T")

def my_decorator(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        print("装饰器执行")
        return func(*args, **kwargs)
    return wrapper
```



<!-- ============ 文档分隔线：040-python/017-AsyncioAwait.md ============ -->

# Python asyncio 异步编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 事件循环

**基本写法：运行协程**
`asyncio.run(<协程>)`
```python
# 运行顶层协程并管理事件循环
async def main():
    print("hello")
asyncio.run(main())
```

**基本写法：获取当前事件循环**
`asyncio.get_event_loop()`
```python
# 获取当前运行的事件循环
loop = asyncio.get_event_loop()
```

**基本写法：获取运行中的事件循环**
`asyncio.get_running_loop()`
```python
# 在协程中获取当前运行的事件循环
loop = asyncio.get_running_loop()
```

**基本写法：设置事件循环策略**
`asyncio.set_event_loop_policy(<策略>)`
```python
# Windows 下使用 Selector 事件循环
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

---

## 协程定义与调用

**基本写法：定义协程函数**
`async def <函数名>(<参数>): <语句>`
```python
# 使用 async def 定义协程
async def fetch_data(url):
    await asyncio.sleep(1)
    return {"data": "result"}
```

**基本写法：await 等待协程**
`await <协程>`
```python
# 在协程中等待另一个协程完成
async def main():
    result = await fetch_data("https://example.com")
    print(result)
```

**基本写法：await 多个协程顺序执行**
`await <协程1>; await <协程2>`
```python
# 依次等待两个协程
async def main():
    r1 = await fetch("url1")
    r2 = await fetch("url2")
```

---

## 任务管理

**基本写法：创建任务**
`asyncio.create_task(<协程>)`
```python
# 将协程封装为 Task 并调度执行
async def main():
    task = asyncio.create_task(fetch_data("url"))
    result = await task
```

**基本写法：并发运行多个协程**
`asyncio.gather(<协程1>, <协程2>)`
```python
# 并发执行多个协程，按顺序返回结果
async def main():
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3"),
    )
```

**基本写法：gather 异常处理**
`asyncio.gather(<协程>, return_exceptions=True)`
```python
# 异常作为返回值而非抛出
async def main():
    results = await asyncio.gather(
        fetch("url1"),
        fetch("bad_url"),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print("失败:", r)
```

**基本写法：Go 1.0 风格任务组**
`async with asyncio.TaskGroup() as <组>:`
```python
# Python 3.11+ 结构化并发，任一任务异常则全部取消
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch("url1"))
        t2 = tg.create_task(fetch("url2"))
    # 退出 with 块时所有任务已完成
    print(t1.result(), t2.result())
```

---

## 等待与超时

**基本写法：等待第一个完成**
`asyncio.wait_for(<协程>, <超时>)`
```python
# 设置超时，超时抛出 TimeoutError
async def main():
    try:
        result = await asyncio.wait_for(fetch("url"), timeout=5.0)
    except asyncio.TimeoutError:
        print("超时")
```

**基本写法：Python 3.11+ asyncio.timeout**
`async with asyncio.timeout(<秒>):`
```python
# Python 3.11+ 超时上下文管理器
async def main():
    try:
        async with asyncio.timeout(5.0):
            result = await fetch("url")
    except TimeoutError:
        print("超时")
```

**基本写法：等待首个完成**
`asyncio.as_completed(<协程列表>)`
```python
# 按完成顺序获取结果
async def main():
    tasks = [fetch(f"url{i}") for i in range(3)]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print("完成:", result)
```

**基本写法：wait 返回两组任务**
`done, pending = await asyncio.wait(<任务集>)`
```python
# 返回已完成和未完成两组任务
async def main():
    tasks = [asyncio.create_task(fetch(f"url{i}")) for i in range(3)]
    done, pending = await asyncio.wait(
        tasks, return_when=asyncio.FIRST_COMPLETED
    )
```

---

## 休眠

**基本写法：异步休眠**
`await asyncio.sleep(<秒>)`
```python
# 非阻塞休眠，让出控制权
async def main():
    await asyncio.sleep(1.0)
    print("1秒后")
```

---

## 队列

**基本写法：异步队列**
`asyncio.Queue()`
```python
# 协程间安全传递数据
async def producer(q):
    await q.put("item")
async def consumer(q):
    item = await q.get()
async def main():
    q = asyncio.Queue(maxsize=10)
    await asyncio.gather(producer(q), consumer(q))
```

**基本写法：带缓冲的队列**
`asyncio.Queue(maxsize=<大小>)`
```python
# 设置最大容量，满时 put 阻塞
q = asyncio.Queue(maxsize=5)
await q.put("data")
item = await q.get()
q.task_done()
await q.join()
```

---

## 锁与信号量

**基本写法：异步锁**
`asyncio.Lock()`
```python
# 协程间互斥锁
lock = asyncio.Lock()
async def safe_update():
    async with lock:
        shared_resource += 1
```

**基本写法：信号量**
`asyncio.Semaphore(<数量>)`
```python
# 限制并发数量
sem = asyncio.Semaphore(5)
async def limited_fetch(url):
    async with sem:
        return await fetch(url)
```

**基本写法：事件**
`asyncio.Event()`
```python
# 协程间事件通知
event = asyncio.Event()
async def waiter():
    await event.wait()
    print("收到信号")
async def setter():
    await asyncio.sleep(1)
    event.set()
```

---

## 异步生成器

**基本写法：定义异步生成器**
`async def <函数名>(): yield <值>`
```python
# 异步生成器函数
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i
```

**基本写法：遍历异步生成器**
`async for <变量> in <异步可迭代>:`
```python
# 异步迭代
async def main():
    async for num in async_range(5):
        print(num)
```

---

## 异步上下文管理器

**换行写法：定义异步上下文管理器**
`class <类名>:`
`    async def __aenter__(self): <语句>`
`    async def __aexit__(self, *args): <语句>`

```python
# 异步上下文管理器
class AsyncDB:
    async def __aenter__(self):
        self.conn = await connect()
        return self
    async def __aexit__(self, *args):
        await self.conn.close()
```

**基本写法：使用异步上下文管理器**
`async with <对象> as <变量>:`
```python
# 使用 async with
async def main():
    async with AsyncDB() as db:
        await db.query("SELECT 1")
```

---

## 异步迭代器

**换行写法：定义异步迭代器**
`class <类名>:`
`    def __aiter__(self): return self`
`    async def __anext__(self): <语句>`

```python
# 实现异步迭代器协议
class AsyncCounter:
    def __init__(self, stop):
        self.i = 0
        self.stop = stop
    def __aiter__(self):
        return self
    async def __anext__(self):
        if self.i >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.i += 1
        return self.i
```

---

## Python 3.13+ asyncio 增强

**基本写法：Python 3.13+ asyncio.Runner**
`asyncio.Runner()`
```python
# Python 3.13+ Runner 上下文管理复用事件循环
with asyncio.Runner() as runner:
    r1 = runner.run(fetch("url1"))
    r2 = runner.run(fetch("url2"))
```

**基本写法：Python 3.13+ eager_task_factory**
`loop.set_task_factory(asyncio.eager_task_factory)`
```python
# Python 3.13+ 协程立即开始执行而非延迟调度
async def main():
    loop = asyncio.get_running_loop()
    loop.set_task_factory(asyncio.eager_task_factory)
```



<!-- ============ 文档分隔线：040-python/018-TypingModule.md ============ -->

# Python typing 模块

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本类型别名

**基本写法：类型别名**
`<别名> = <类型>`
```python
# 为类型定义别名
Vector = list[float]
Matrix = list[list[float]]
def scale(v: Vector, n: float) -> Vector:
    return [x * n for x in v]
```

**基本写法：Python 3.12+ type 语句**
`type <别名> = <类型>`
```python
# Python 3.12+ 使用 type 关键字定义类型别名
type Vector = list[float]
type Callback = Callable[[int], str]
```

---

## 泛型

**基本写法：泛型函数**
`def <函数名>(<参数>: <类型>[T]) -> <类型>[T]`
```python
# 使用 TypeVar 声明泛型
from typing import TypeVar
T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]
```

**基本写法：Python 3.12+ 泛型语法**
`def <函数名>[T](<参数>: list[T]) -> T`
```python
# Python 3.12+ 内联泛型参数声明
def first[T](items: list[T]) -> T:
    return items[0]
```

**换行写法：泛型类**
`class <类名>(Generic[T]):`
```python
# 继承 Generic 实现泛型类
from typing import Generic, TypeVar
T = TypeVar("T")
class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
```

**基本写法：Python 3.12+ 泛型类新语法**
`class <类名>[T]:`
```python
# Python 3.12+ 直接在类名后声明类型参数
class Stack[T]:
    def __init__(self):
        self._items: list[T] = []
    def push(self, item: T) -> None:
        self._items.append(item)
```

---

## Optional 与 Union

**基本写法：Optional 可选类型**
`Optional[<类型>]`
```python
# 表示值可以为 None
from typing import Optional
def find(name: str) -> Optional[int]:
    if name in data:
        return data[name]
    return None
```

**基本写法：Union 联合类型**
`Union[<类型1>, <类型2>]`
```python
# 多种可能的类型
from typing import Union
def process(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data
```

**基本写法：Python 3.10+ 联合类型语法**
`<类型1> | <类型2>`
```python
# 使用管道符表示联合类型
def process(data: str | bytes) -> str:
    if isinstance(data, bytes):
        return data.decode()
    return data
```

**基本写法：Python 3.10+ 可空语法**
`<类型> | None`
```python
# 使用管道符表示可选
def find(name: str) -> int | None:
    return data.get(name)
```

---

## Callable 可调用类型

**基本写法：Callable 类型**
`Callable[[<参数类型>], <返回类型>]`
```python
# 标注函数类型
from typing import Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

**基本写法：无参数 Callable**
`Callable[[], <返回类型>]`
```python
# 无参数可调用对象
def run(fn: Callable[[], str]) -> str:
    return fn()
```

**基本写法：任意签名 Callable**
`Callable[..., <返回类型>]`
```python
# 不指定参数签名的可调用对象
Handler = Callable[..., None]
```

---

## 容器类型

**基本写法：List 类型**
`list[<元素类型>]`
```python
# 列表类型标注
names: list[str] = ["Alice", "Bob"]
```

**基本写法：Dict 类型**
`dict[<键类型>, <值类型>]`
```python
# 字典类型标注
scores: dict[str, int] = {"Alice": 90}
```

**基本写法：Tuple 类型**
`tuple[<类型1>, <类型2>]`
```python
# 固定长度元组
point: tuple[float, float] = (1.0, 2.0)
```

**基本写法：可变长元组**
`tuple[<类型>, ...]`
```python
# 任意长度的同类型元组
nums: tuple[int, ...] = (1, 2, 3)
```

**基本写法：Set 类型**
`set[<元素类型>]`
```python
# 集合类型标注
tags: set[str] = {"a", "b"}
```

---

## TypedDict

**换行写法：定义 TypedDict**
`class <类名>(TypedDict):`
`    <字段>: <类型>`

```python
# 为字典提供固定键值类型
from typing import TypedDict
class UserDict(TypedDict):
    name: str
    age: int
user: UserDict = {"name": "Alice", "age": 30}
```

**基本写法：Python 3.12+ TypedDict 用于 kwargs**
`def <函数名>(**kwargs: <TypedDict类>)`
```python
# Python 3.12+ PEP 692 使用 TypedDict 标注 kwargs
class Options(TypedDict, total=False):
    timeout: int
    retry: bool
def fetch(url: str, **kwargs: Options) -> None:
    pass
```

---

## Literal 字面量类型

**基本写法：Literal 字面量**
`Literal[<值1>, <值2>]`
```python
# 限定值为特定字面量
from typing import Literal
def set_mode(mode: Literal["read", "write", "append"]) -> None:
    pass
```

---

## Protocol 结构化子类型

**换行写法：定义 Protocol**
`class <协议名>(Protocol):`
`    def <方法>(self, ...) -> ...: ...`

```python
# 鸭子类型协议
from typing import Protocol
class Comparable(Protocol):
    def __lt__(self, other: "Comparable") -> bool: ...
def sort(items: list[Comparable]) -> None:
    pass
```

**基本写法：runtime_checkable 运行时检查**
`@runtime_checkable`
```python
# 允许 isinstance 检查 Protocol
from typing import Protocol, runtime_checkable
@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...
isinstance(obj, Drawable)
```

---

## Any 与 TypeGuard

**基本写法：Any 类型**
`Any`
```python
# 任意类型，跳过类型检查
from typing import Any
data: Any = json.loads(raw)
```

**基本写法：TypeGuard 类型守卫**
`TypeGuard[<类型>]`
```python
# 缩小类型范围的谓词函数
from typing import TypeGuard
def is_str_list(val: list) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in val)
```

**基本写法：Python 3.13+ TypeIs**
`TypeIs[<类型>]`
```python
# Python 3.13+ 更严格的类型守卫
from typing import TypeIs
def is_positive(n: int) -> TypeIs[int]:
    return n > 0
```

---

## TypeVar 高级用法

**基本写法：带约束的 TypeVar**
`TypeVar("<名称>", <类型1>, <类型2>)`
```python
# 限定类型只能是某几种
from typing import TypeVar
T = TypeVar("T", int, float)
def add(a: T, b: T) -> T:
    return a + b
```

**基本写法：带上界的 TypeVar**
`TypeVar("<名称>", bound=<类型>)`
```python
# 限定类型必须是指定类的子类
from typing import TypeVar
T = TypeVar("T", bound=str)
def process(value: T) -> T:
    return value
```

**基本写法：Python 3.13+ TypeVar 默认值**
`T = TypeVar("T", default=<类型>)`
```python
# Python 3.13+ PEP 696 类型参数默认值
from typing import TypeVar
T = TypeVar("T", default=int)
def get_value() -> T:
    return 42
```

---

## ParamSpec 与 TypeVarTuple

**基本写法：ParamSpec 参数规格**
`P = ParamSpec("P")`
```python
# 捕获函数的参数签名
from typing import ParamSpec, Callable, TypeVar
P = ParamSpec("P")
R = TypeVar("R")
def log(fn: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return fn(*args, **kwargs)
    return wrapper
```

**基本写法：TypeVarTuple 可变泛型**
`Ts = TypeVarTuple("Ts")`
```python
# 可变数量的类型参数
from typing import TypeVarTuple, Unpack
Ts = TypeVarTuple("Ts")
def merge(*args: Unpack[Ts]) -> tuple[Unpack[Ts]]:
    return args
```

---

## 常用工具类型

**基本写法：Final 不可变**
`Final[<类型>]`
```python
# 标注不应被重新赋值
from typing import Final
MAX_SIZE: Final[int] = 100
```

**基本写法：ClassVar 类变量**
`ClassVar[<类型>]`
```python
# 标注类级别变量而非实例变量
from typing import ClassVar
class Config:
    default: ClassVar[str] = "production"
```

**基本写法：Python 3.13+ @deprecated**
`@deprecated("<消息>")`
```python
# Python 3.13+ PEP 702 标记弃用
from warnings import deprecated  # typing.deprecated
@deprecated("使用 new_func 替代")
def old_func():
    pass
```

**基本写法：@override 重写标记**
`@override`
```python
# Python 3.12+ PEP 698 标记方法重写
from typing import override
class Child(Parent):
    @override
    def method(self):
        pass
```



<!-- ============ 文档分隔线：040-python/019-Pathlib.md ============ -->

# Python pathlib 路径操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 路径创建

**基本写法：创建路径对象**
`Path(<路径字符串>)`
```python
# 创建 Path 对象
from pathlib import Path
p = Path("/usr/local/bin")
```

**基本写法：当前目录**
`Path.cwd()`
```python
# 获取当前工作目录
cwd = Path.cwd()
```

**基本写法：用户主目录**
`Path.home()`
```python
# 获取用户主目录
home = Path.home()
```

**基本写法：路径拼接**
`Path(<父路径>) / <子路径>`
```python
# 使用 / 运算符拼接路径
config = Path("/etc") / "nginx" / "nginx.conf"
```

**基本写法：joinpath 多级拼接**
`<路径>.joinpath(<子路径1>, <子路径2>)`
```python
# 拼接多个路径段
p = Path("/var").joinpath("log", "app.log")
```

---

## 路径属性

**基本写法：获取文件名**
`<路径>.name`
```python
# 返回最后一级路径名
p = Path("/a/b/c.txt")
print(p.name)  # c.txt
```

**基本写法：获取文件名（不含扩展名）**
`<路径>.stem`
```python
# 返回不含扩展名的文件名
p = Path("archive.tar.gz")
print(p.stem)  # archive.tar
```

**基本写法：获取扩展名**
`<路径>.suffix`
```python
# 返回最后一个扩展名
p = Path("file.tar.gz")
print(p.suffix)  # .gz
```

**基本写法：获取所有扩展名**
`<路径>.suffixes`
```python
# 返回所有扩展名列表
p = Path("file.tar.gz")
print(p.suffixes)  # ['.tar', '.gz']
```

**基本写法：获取父目录**
`<路径>.parent`
```python
# 返回上一级目录
p = Path("/a/b/c.txt")
print(p.parent)  # /a/b
```

**基本写法：获取所有父目录**
`<路径>.parents`
```python
# 返回所有上级目录的可迭代对象
p = Path("/a/b/c.txt")
for parent in p.parents:
    print(parent)
```

**基本写法：获取绝对路径**
`<路径>.resolve()`
```python
# 返回解析后的绝对路径
p = Path("./config").resolve()
```

**基本写法：获取路径各部分**
`<路径>.parts`
```python
# 返回路径各段组成的元组
p = Path("/usr/local/bin")
print(p.parts)  # ('/', 'usr', 'local', 'bin')
```

---

## 路径判断

**基本写法：判断文件是否存在**
`<路径>.exists()`
```python
# 检查路径是否存在
if Path("file.txt").exists():
    print("存在")
```

**基本写法：判断是否为文件**
`<路径>.is_file()`
```python
# 检查是否为普通文件
Path("file.txt").is_file()
```

**基本写法：判断是否为目录**
`<路径>.is_dir()`
```python
# 检查是否为目录
Path("/usr").is_dir()
```

**基本写法：判断是否为绝对路径**
`<路径>.is_absolute()`
```python
# 检查是否为绝对路径
Path("/usr").is_absolute()  # True
Path("usr").is_absolute()   # False
```

---

## 文件读写

**基本写法：读取文本文件**
`<路径>.read_text([encoding=<编码>])`
```python
# 一次性读取整个文本文件
content = Path("file.txt").read_text(encoding="utf-8")
```

**基本写法：写入文本文件**
`<路径>.write_text(<内容>, [encoding=<编码>])`
```python
# 一次性写入文本
Path("output.txt").write_text("hello", encoding="utf-8")
```

**基本写法：读取二进制文件**
`<路径>.read_bytes()`
```python
# 读取二进制内容
data = Path("image.png").read_bytes()
```

**基本写法：写入二进制文件**
`<路径>.write_bytes(<数据>)`
```python
# 写入二进制数据
Path("data.bin").write_bytes(b"\x00\x01")
```

**换行写法：打开文件上下文管理**
`with <路径>.open([mode], [encoding]) as <变量>:`
```python
# 使用 open 方法逐行读取
with Path("file.txt").open("r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## 目录操作

**基本写法：创建目录**
`<路径>.mkdir([parents=True], [exist_ok=True])`
```python
# 递归创建目录，已存在不报错
Path("a/b/c").mkdir(parents=True, exist_ok=True)
```

**基本写法：删除空目录**
`<路径>.rmdir()`
```python
# 删除空目录
Path("empty_dir").rmdir()
```

**基本写法：删除文件**
`<路径>.unlink()`
```python
# 删除单个文件
Path("file.txt").unlink()
```

**基本写法：删除文件（不存在不报错）**
`<路径>.unlink(missing_ok=True)`
```python
# Python 3.8+ 文件不存在时不抛出异常
Path("file.txt").unlink(missing_ok=True)
```

**基本写法：重命名或移动**
`<路径>.rename(<目标路径>)`
```python
# 移动文件或重命名
Path("old.txt").rename("new.txt")
```

**基本写法：Python 3.13+ replace 兼容性**
`<路径>.replace(<目标路径>)`
```python
# 覆盖目标路径并替换
Path("temp.txt").replace("final.txt")
```

---

## 遍历目录

**基本写法：列出目录内容**
`<路径>.iterdir()`
```python
# 遍历目录下的直接子项
for item in Path(".").iterdir():
    print(item.name)
```

**基本写法：glob 模式匹配**
`<路径>.glob(<模式>)`
```python
# 递归匹配文件
for p in Path(".").glob("**/*.py"):
    print(p)
```

**基本写法：rglob 递归匹配**
`<路径>.rglob(<模式>)`
```python
# 递归搜索所有子目录
for p in Path(".").rglob("*.py"):
    print(p)
```

**基本写法：Python 3.12+ 模式参数**
`<路径>.glob(<模式>, case_sensitive=<布尔>)`
```python
# Python 3.12+ 支持大小写敏感控制
for p in Path(".").glob("*.PY", case_sensitive=False):
    print(p)
```

---

## 文件信息

**基本写法：获取文件状态**
`<路径>.stat()`
```python
# 获取文件元数据
info = Path("file.txt").stat()
print(info.st_size, info.st_mtime)
```

**基本写法：获取文件大小**
`<路径>.stat().st_size`
```python
# 返回文件字节数
size = Path("file.txt").stat().st_size
```

**基本写法：获取修改时间**
`<路径>.stat().st_mtime`
```python
# 返回最后修改时间戳
import time
mtime = Path("file.txt").stat().st_mtime
print(time.ctime(mtime))
```

---

## 路径匹配与变换

**基本写法：路径模式匹配**
`<路径>.match(<模式>)`
```python
# 判断路径是否匹配模式
Path("a/b/c.txt").match("*.txt")  # True
Path("a/b/c.txt").match("a/*.txt")  # False
```

**基本写法：修改文件名**
`<路径>.with_name(<新名称>)`
```python
# 返回替换文件名后的新路径
p = Path("/a/b/c.txt")
new_p = p.with_name("d.txt")  # /a/b/d.txt
```

**基本写法：修改扩展名**
`<路径>.with_suffix(<新扩展名>)`
```python
# 返回替换扩展名后的新路径
p = Path("file.txt")
new_p = p.with_suffix(".md")
```

**基本写法：修改父目录**
`<路径>.with_parent(<新父目录>)`
```python
# Python 3.12+ 替换父目录
p = Path("/old/file.txt")
new_p = p.with_parent("/new")  # /new/file.txt
```

**基本写法：相对路径**
`<路径>.relative_to(<基准路径>)`
```python
# 计算相对路径
p = Path("/usr/local/bin")
rel = p.relative_to("/usr")  # local/bin
```

---

## Python 3.13+ pathlib 增强

**基本写法：Python 3.13+ from_uri**
`Path.from_uri(<URI>)`
```python
# Python 3.13+ 从 URI 创建路径
p = Path.from_uri("file:///usr/local/bin")
```

**基本写法：Python 3.13+ as_uri**
`<路径>.as_uri()`
```python
# 将绝对路径转为 file URI
uri = Path("/usr/local").as_uri()
```

**基本写法：Python 3.13+ full_match**
`<路径>.full_match(<模式>)`
```python
# Python 3.13+ 完整路径匹配
Path("/a/b/c.txt").full_match("/a/**/*.txt")
```



<!-- ============ 文档分隔线：040-python/020-CollectionsModule.md ============ -->

# Python collections 模块

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Counter 计数器

**基本写法：创建计数器**
`Counter(<可迭代对象>)`
```python
# 统计元素出现次数
from collections import Counter
c = Counter("abracadabra")
print(c)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

**基本写法：获取元素计数**
`<计数器>[<元素>]`
```python
# 获取指定元素的计数
c = Counter(["a", "b", "a"])
print(c["a"])  # 2
```

**基本写法：获取前 N 个高频元素**
`<计数器>.most_common([n])`
```python
# 返回计数最多的 n 个元素
c = Counter("abracadabra")
print(c.most_common(2))  # [('a', 5), ('b', 2)]
```

**基本写法：计数器加法**
`<计数器1> + <计数器2>`
```python
# 合并计数
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)  # Counter({'a': 4, 'b': 3})
```

**基本写法：计数器减法**
`<计数器1> - <计数器2>`
```python
# 计数相减（结果保留正数）
c1 = Counter(a=5, b=2)
c2 = Counter(a=1, b=4)
print(c1 - c2)  # Counter({'a': 4})
```

**基本写法：获取所有元素**
`<计数器>.elements()`
```python
# 返回所有元素的迭代器
c = Counter(a=2, b=3)
print(list(c.elements()))  # ['a', 'a', 'b', 'b', 'b']
```

**基本写法：更新计数**
`<计数器>.update(<可迭代对象>)`
```python
# 增加元素计数
c = Counter(a=1)
c.update("aab")
print(c)  # Counter({'a': 3, 'b': 1})
```

---

## defaultdict 默认字典

**基本写法：创建默认字典**
`defaultdict(<工厂函数>)`
```python
# 键不存在时自动创建默认值
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(d["a"])  # [1, 2]
```

**基本写法：int 默认值**
`defaultdict(int)`
```python
# 默认值为 0
counts = defaultdict(int)
for word in words:
    counts[word] += 1
```

**基本写法：set 默认值**
`defaultdict(set)`
```python
# 默认值为空集合
groups = defaultdict(set)
groups["fruit"].add("apple")
groups["fruit"].add("banana")
```

**基本写法：自定义默认值**
`defaultdict(lambda: <默认值>)`
```python
# 自定义默认值
d = defaultdict(lambda: "N/A")
print(d["missing"])  # N/A
```

---

## namedtuple 命名元组

**基本写法：创建命名元组**
`namedtuple("<类名>", [<字段1>, <字段2>])`
```python
# 创建具名元组类型
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)  # 1 2
```

**基本写法：字段名为字符串**
`namedtuple("<类名>", "<字段1> <字段2>")`
```python
# 空格分隔的字段名
Point = namedtuple("Point", "x y")
p = Point(3, 4)
```

**基本写法：通过键创建**
`<类型>._make(<可迭代对象>)`
```python
# 从可迭代对象创建
data = [10, 20]
p = Point._make(data)
```

**基本写法：转换为字典**
`<实例>._asdict()`
```python
# 转为字典
p = Point(1, 2)
d = p._asdict()
print(d)  # {'x': 1, 'y': 2}
```

**基本写法：替换字段值**
`<实例>._replace(<字段>=<新值>)`
```python
# 返回替换指定字段后的新实例
p = Point(1, 2)
p2 = p._replace(x=10)
print(p2)  # Point(x=10, y=2)
```

**基本写法：默认值字段**
`namedtuple("<类名>", <字段>, defaults=[<默认值>])`
```python
# 从右往左设置默认值
Point = namedtuple("Point", ["x", "y", "z"], defaults=[0])
p = Point(1, 2)  # z 默认为 0
```

---

## OrderedDict 有序字典

**基本写法：创建有序字典**
`OrderedDict([<键值对列表>])`
```python
# 保持插入顺序的字典（Python 3.7+ 普通 dict 也保序）
from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2)])
```

**基本写法：移到末尾**
`<有序字典>.move_to_end(<键>)`
```python
# 将指定键移到末尾
od = OrderedDict(a=1, b=2, c=3)
od.move_to_end("a")
print(list(od.keys()))  # ['b', 'c', 'a']
```

**基本写法：弹出首尾**
`<有序字典>.popitem(last=<布尔>)`
```python
# 弹出首部或尾部元素
od = OrderedDict(a=1, b=2)
key, val = od.popitem(last=False)  # 弹出 a
```

---

## deque 双端队列

**基本写法：创建双端队列**
`deque([<可迭代对象>], [maxlen=<最大长度>])`
```python
# 创建双端队列
from collections import deque
dq = deque([1, 2, 3], maxlen=5)
```

**基本写法：左端添加**
`<队列>.appendleft(<元素>)`
```python
# 在左端添加元素
dq = deque([1, 2])
dq.appendleft(0)  # deque([0, 1, 2])
```

**基本写法：右端添加**
`<队列>.append(<元素>)`
```python
# 在右端添加元素
dq = deque([1, 2])
dq.append(3)  # deque([1, 2, 3])
```

**基本写法：左端弹出**
`<队列>.popleft()`
```python
# 从左端弹出元素
dq = deque([1, 2, 3])
x = dq.popleft()  # 1
```

**基本写法：批量扩展**
`<队列>.extendleft(<可迭代对象>)`
```python
# 左端批量添加
dq = deque([1])
dq.extendleft([2, 3])  # deque([3, 2, 1])
```

**基本写法：旋转**
`<队列>.rotate(<步数>)`
```python
# 向右旋转 n 步（负数向左）
dq = deque([1, 2, 3, 4])
dq.rotate(1)  # deque([4, 1, 2, 3])
```

---

## ChainMap 链式映射

**基本写法：创建链式映射**
`ChainMap(<字典1>, <字典2>)`
```python
# 合并多个字典按顺序查找
from collections import ChainMap
defaults = {"color": "red", "size": 10}
user = {"color": "blue"}
config = ChainMap(user, defaults)
print(config["color"])  # blue
print(config["size"])   # 10
```

**基本写法：添加新映射**
`<链式映射>.new_child(<字典>)`
```python
# 在链首添加新字典
config = ChainMap(user, defaults)
new_config = config.new_child({"size": 20})
print(new_config["size"])  # 20
```

---

## UserDict 自定义字典

**换行写法：继承 UserDict**
`class <类名>(UserDict):`
`    def __setitem__(self, key, value): <语句>`

```python
# 继承 UserDict 自定义字典行为
from collections import UserDict
class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    def __getitem__(self, key):
        return super().__getitem__(key.lower())
```



<!-- ============ 文档分隔线：040-python/021-Itertools.md ============ -->

# Python itertools 迭代工具

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 无限迭代器

**基本写法：count 无限计数**
`itertools.count([start], [step])`
```python
# 从 start 开始每次加 step 无限计数
from itertools import count
for i in count(10, 2):
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20
```

**基本写法：cycle 循环重复**
`itertools.cycle(<可迭代对象>)`
```python
# 无限循环遍历可迭代对象
from itertools import cycle
colors = cycle(["red", "green", "blue"])
for i, c in enumerate(colors):
    if i >= 5:
        break
    print(c)
```

**基本写法：repeat 重复元素**
`itertools.repeat(<元素>, [times])`
```python
# 重复元素指定次数
from itertools import repeat
for x in repeat("hi", 3):
    print(x)  # hi hi hi
```

---

## 串联与切分

**基本写法：chain 串联迭代器**
`itertools.chain(<可迭代1>, <可迭代2>)`
```python
# 将多个可迭代对象串联
from itertools import chain
for x in chain([1, 2], [3, 4]):
    print(x)  # 1 2 3 4
```

**基本写法：chain.from_iterable 串联嵌套**
`itertools.chain.from_iterable(<嵌套可迭代>)`
```python
# 串联可迭代对象的可迭代对象
nested = [[1, 2], [3, 4], [5]]
for x in chain.from_iterable(nested):
    print(x)  # 1 2 3 4 5
```

**基本写法：islice 切片**
`itertools.islice(<可迭代>, [start], stop, [step])`
```python
# 对迭代器进行切片
from itertools import islice
for x in islice(range(100), 5, 10, 2):
    print(x)  # 5 7 9
```

**基本写法：tee 分裂迭代器**
`itertools.tee(<可迭代>, n)`
```python
# 复制迭代器为 n 个独立迭代器
from itertools import tee
it1, it2 = tee(range(3), 2)
print(list(it1))  # [0, 1, 2]
print(list(it2))  # [0, 1, 2]
```

---

## 过滤

**基本写法：filterfalse 反向过滤**
`itertools.filterfalse(<函数>, <可迭代>)`
```python
# 保留使函数返回 False 的元素
from itertools import filterfalse
for x in filterfalse(lambda n: n % 2, range(6)):
    print(x)  # 0 2 4
```

**基本写法：takewhile 取到条件不满足**
`itertools.takewhile(<函数>, <可迭代>)`
```python
# 依次取元素直到函数返回 False
from itertools import takewhile
for x in takewhile(lambda n: n < 5, [1, 3, 5, 2]):
    print(x)  # 1 3
```

**基本写法：dropwhile 丢弃到条件不满足**
`itertools.dropwhile(<函数>, <可迭代>)`
```python
# 跳过元素直到函数返回 False，然后取剩余
from itertools import dropwhile
for x in dropwhile(lambda n: n < 5, [1, 3, 5, 2, 7]):
    print(x)  # 5 2 7
```

**基本写法：compress 按选择器过滤**
`itertools.compress(<数据>, <选择器>)`
```python
# 按布尔选择器提取元素
from itertools import compress
for x in compress("ABCDEF", [1, 0, 1, 0, 1, 1]):
    print(x)  # A C E F
```

---

## 映射

**基本写法：starmap 展开映射**
`itertools.starmap(<函数>, <可迭代>)`
```python
# 将每项作为参数展开传给函数
from itertools import starmap
for result in starmap(pow, [(2, 3), (3, 2)]):
    print(result)  # 8 9
```

**基本写法：accumulate 累积**
`itertools.accumulate(<可迭代>, [func])`
```python
# 累积求和或自定义累积函数
from itertools import accumulate
for x in accumulate([1, 2, 3, 4]):
    print(x)  # 1 3 6 10
```

**基本写法：累积求积**
`itertools.accumulate(<可迭代>, operator.mul)`
```python
# 累积乘法
import operator
for x in accumulate([1, 2, 3, 4], operator.mul):
    print(x)  # 1 2 6 24
```

---

## 分组

**基本写法：groupby 分组**
`itertools.groupby(<可迭代>, [key=<函数>])`
```python
# 按键函数分组（需先排序）
from itertools import groupby
data = [("a", 1), ("a", 2), ("b", 3)]
for key, group in groupby(data, lambda x: x[0]):
    print(key, list(group))
# a [('a', 1), ('a', 2)]
# b [('b', 3)]
```

**基本写法：按值分组**
`itertools.groupby(sorted(<可迭代>), key=<函数>)`
```python
# 先排序再分组确保连续
words = ["apple", "bat", "ant", "bear"]
for first, group in groupby(sorted(words), lambda w: w[0]):
    print(first, list(group))
# a ['apple', 'ant']
# b ['bat', 'bear']
```

---

## 排列组合

**基本写法：product 笛卡尔积**
`itertools.product(<可迭代1>, <可迭代2>, [repeat=<次数>])`
```python
# 多个可迭代对象的笛卡尔积
from itertools import product
for combo in product("AB", "12"):
    print(combo)
# ('A','1') ('A','2') ('B','1') ('B','2')
```

**基本写法：product 重复**
`itertools.product(<可迭代>, repeat=<次数>)`
```python
# 与自身做笛卡尔积
for combo in product("AB", repeat=2):
    print(combo)
# AA AB BA BB
```

**基本写法：permutations 排列**
`itertools.permutations(<可迭代>, [r])`
```python
# 全排列
from itertools import permutations
for p in permutations("ABC", 2):
    print(p)
# AB AC BA BC CA CB
```

**基本写法：combinations 组合**
`itertools.combinations(<可迭代>, r)`
```python
# 无放回组合
from itertools import combinations
for c in combinations("ABC", 2):
    print(c)
# AB AC BC
```

**基本写法：combinations_with_replacement 可重复组合**
`itertools.combinations_with_replacement(<可迭代>, r)`
```python
# 有放回组合
from itertools import combinations_with_replacement
for c in combinations_with_replacement("AB", 2):
    print(c)
# AA AB BB
```

---

## 配对与分块

**基本写法：Python 3.10+ pairwise 配对**
`itertools.pairwise(<可迭代>)`
```python
# 相邻元素两两配对
from itertools import pairwise
for a, b in pairwise([1, 2, 3, 4]):
    print(a, b)  # 1 2 / 2 3 / 3 4
```

**基本写法：Python 3.12+ batched 分批**
`itertools.batched(<可迭代>, n)`
```python
# Python 3.12+ 按固定大小分批
from itertools import batched
for batch in batched(range(7), 3):
    print(batch)
# (0, 1, 2) (3, 4, 5) (6,)
```

---

## zip_longest

**基本写法：zip_longest 不等长配对**
`itertools.zip_longest(<可迭代1>, <可迭代2>, [fillvalue=<填充值>])`
```python
# 不等长可迭代对象配对，短端填充
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], ["a", "b"], fillvalue="?"):
    print(a, b)
# 1 a / 2 b / 3 ?
```



<!-- ============ 文档分隔线：040-python/022-Functools.md ============ -->

# Python functools 函数工具

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：040-python/023-DatetimeTime.md ============ -->

# Python datetime 与 time

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## datetime 基本创建

**基本写法：创建日期**
`datetime.date(<年>, <月>, <日>)`
```python
# 创建日期对象
from datetime import date
d = date(2024, 7, 31)
print(d)  # 2024-07-31
```

**基本写法：创建时间**
`datetime.time(<时>, <分>, [秒], [微秒])`
```python
# 创建时间对象
from datetime import time
t = time(14, 30, 0)
print(t)  # 14:30:00
```

**基本写法：创建日期时间**
`datetime.datetime(<年>, <月>, <日>, <时>, <分>, <秒>)`
```python
# 创建日期时间对象
from datetime import datetime
dt = datetime(2024, 7, 31, 14, 30, 0)
```

**基本写法：获取当前日期时间**
`datetime.now()`
```python
# 获取本地当前日期时间
now = datetime.now()
```

**基本写法：获取当前日期**
`date.today()`
```python
# 获取当前日期
today = date.today()
```

**基本写法：获取 UTC 当前时间**
`datetime.now(tz=timezone.utc)`
```python
# 获取 UTC 时区当前时间
from datetime import timezone
utc_now = datetime.now(tz=timezone.utc)
```

---

## datetime 从字符串解析

**基本写法：解析日期时间字符串**
`datetime.strptime(<字符串>, <格式>)`
```python
# 按格式解析字符串
from datetime import datetime
dt = datetime.strptime("2024-07-31 14:30", "%Y-%m-%d %H:%M")
```

**基本写法：格式化输出**
`<日期>.strftime(<格式>)`
```python
# 格式化为字符串
now = datetime.now()
s = now.strftime("%Y年%m月%d日 %H:%M:%S")
```

**常用格式化代码**
`%Y %m %d %H %M %S`
```python
# 常用格式化占位符
# %Y 年(4位)  %m 月(01-12)  %d 日(01-31)
# %H 时(00-23)  %M 分(00-59)  %S 秒(00-59)
# %A 星期名  %B 月名  %j 年内天数
```

**基本写法：ISO 格式解析**
`datetime.fromisoformat(<字符串>)`
```python
# 解析 ISO 8601 格式字符串
from datetime import datetime
dt = datetime.fromisoformat("2024-07-31T14:30:00")
```

**基本写法：输出 ISO 格式**
`<日期>.isoformat()`
```python
# 输出 ISO 8601 格式字符串
now = datetime.now()
print(now.isoformat())  # 2024-07-31T14:30:00
```

---

## timedelta 时间差

**基本写法：创建时间差**
`datetime.timedelta([days], [seconds], [microseconds])`
```python
# 创建时间间隔
from datetime import timedelta, date
delta = timedelta(days=7)
```

**基本写法：日期加减**
`<日期> + <时间差>`
```python
# 日期加减时间差
from datetime import date, timedelta
today = date.today()
next_week = today + timedelta(days=7)
```

**基本写法：两个日期相减**
`<日期1> - <日期2>`
```python
# 计算日期差
from datetime import date
d1 = date(2024, 12, 31)
d2 = date(2024, 1, 1)
diff = d1 - d2
print(diff.days)  # 365
```

**基本写法：时间差属性**
`<时间差>.days / .seconds / .total_seconds()`
```python
# 访问时间差的各部分
delta = timedelta(days=1, hours=2)
print(delta.days)             # 1
print(delta.seconds)          # 7200
print(delta.total_seconds())  # 93600.0
```

---

## 时区处理

**基本写法：设置时区**
`datetime.now(tz=<时区>)`
```python
# 获取带时区的当前时间
from datetime import datetime, timezone
utc_now = datetime.now(tz=timezone.utc)
```

**基本写法：时区转换**
`<时间>.astimezone(<目标时区>)`
```python
# UTC 转本地时区
from datetime import datetime, timezone
utc_dt = datetime.now(tz=timezone.utc)
local_dt = utc_dt.astimezone()
```

**基本写法：Python 3.9+ zoneinfo 时区**
`ZoneInfo("<时区名>")`
```python
# Python 3.9+ 使用 IANA 时区数据库
from zoneinfo import ZoneInfo
from datetime import datetime
tz_shanghai = ZoneInfo("Asia/Shanghai")
dt = datetime(2024, 7, 31, 14, 0, tzinfo=tz_shanghai)
```

**基本写法：时区转换**
`<时间>.astimezone(ZoneInfo("<时区>"))`
```python
# 上海时间转纽约时间
from zoneinfo import ZoneInfo
shanghai_time = datetime.now(tz=ZoneInfo("Asia/Shanghai"))
ny_time = shanghai_time.astimezone(ZoneInfo("America/New_York"))
```

**基本写法：Python 3.12+ fromisoformat 解析时区**
`datetime.fromisoformat(<带时区字符串>)`
```python
# Python 3.11+ 支持解析带时区的 ISO 字符串
dt = datetime.fromisoformat("2024-07-31T14:30:00+08:00")
```

---

## time 模块

**基本写法：获取时间戳**
`time.time()`
```python
# 返回当前时间的 Unix 时间戳（秒）
import time
ts = time.time()
```

**基本写法：时间戳转结构化时间**
`time.localtime([<时间戳>])`
```python
# 转为本地时间 struct_time
t = time.localtime()
print(t.tm_year, t.tm_mon, t.tm_mday)
```

**基本写法：格式化时间**
`time.strftime(<格式>, <结构化时间>)`
```python
# 按格式输出字符串
import time
s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
```

**基本写法：解析时间字符串**
`time.strptime(<字符串>, <格式>)`
```python
# 解析字符串为 struct_time
t = time.strptime("2024-07-31", "%Y-%m-%d")
```

**基本写法：程序休眠**
`time.sleep(<秒>)`
```python
# 阻塞当前线程指定秒数
time.sleep(1.5)
```

**基本写法：计时**
`time.perf_counter()`
```python
# 高精度计时器
start = time.perf_counter()
do_work()
elapsed = time.perf_counter() - start
```

**基本写法：单调时钟**
`time.monotonic()`
```python
# 不受系统时间调整影响的单调时钟
start = time.monotonic()
time.sleep(1)
print(time.monotonic() - start)
```

**基本写法：Python 3.11+ monotonic_ns**
`time.monotonic_ns()`
```python
# 纳秒精度单调时钟
ns = time.monotonic_ns()
```

---

## time 性能计时

**基本写法：测量代码执行时间**
`time.perf_counter()`
```python
# 使用 perf_counter 测量耗时
import time
start = time.perf_counter()
result = sum(range(10**6))
elapsed = time.perf_counter() - start
print(f"耗时: {elapsed:.4f} 秒")
```

**基本写法：纳秒精度时间戳**
`time.time_ns()`
```python
# 返回纳秒精度时间戳
ns = time.time_ns()
```

**基本写法：process_time 进程时间**
`time.process_time()`
```python
# 返回进程实际 CPU 时间（不含休眠）
start = time.process_time()
do_work()
cpu_time = time.process_time() - start
```

---

## calendar 日历

**基本写法：获取月历**
`calendar.month(<年>, <月>)`
```python
# 输出文本格式月历
import calendar
print(calendar.month(2024, 7))
```

**基本写法：判断闰年**
`calendar.isleap(<年>)`
```python
# 判断是否为闰年
import calendar
print(calendar.isleap(2024))  # True
```

**基本写法：获取某月天数**
`calendar.monthrange(<年>, <月>)`
```python
# 返回 (该月首日星期几, 该月天数)
import calendar
print(calendar.monthrange(2024, 2))  # (3, 29)
```



<!-- ============ 文档分隔线：040-python/024-MultiprocessingThreading.md ============ -->

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



<!-- ============ 文档分隔线：040-python/028-SerializationJsonCsvPickle.md ============ -->

# Python 序列化 JSON/CSV/Pickle

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## json 序列化

**基本写法：对象转 JSON 字符串**
`json.dumps(<对象>)`
```python
# 将 Python 对象转为 JSON 字符串
import json
data = {"name": "Tom", "age": 18}
s = json.dumps(data)  # '{"name": "Tom", "age": 18}'
```

**基本写法：格式化输出**
`json.dumps(<对象>, indent=<缩进>, ensure_ascii=<布尔>)`
```python
# 缩进美化并保留中文字符
print(json.dumps(data, indent=2, ensure_ascii=False))
```

**基本写法：JSON 字符串转对象**
`json.loads(<字符串>)`
```python
# 将 JSON 字符串解析为 Python 对象
obj = json.loads('{"name": "Tom"}')
print(obj["name"])  # Tom
```

**基本写法：写入文件**
`json.dump(<对象>, <文件对象>)`
```python
# 将对象序列化写入文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

**基本写法：从文件读取**
`json.load(<文件对象>)`
```python
# 从文件读取并解析 JSON
with open("data.json", encoding="utf-8") as f:
    obj = json.load(f)
```

**基本写法：排序键输出**
`json.dumps(<对象>, sort_keys=True)`
```python
# 按键名排序输出
print(json.dumps({"b": 1, "a": 2}, sort_keys=True))
```

**基本写法：自定义序列化**
`json.dumps(<对象>, default=<函数>)`
```python
# 自定义非内置类型的序列化逻辑
from datetime import datetime
def default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError

print(json.dumps({"t": datetime.now()}, default=default))
```

**基本写法：自定义反序列化**
`json.loads(<字符串>, object_hook=<函数>)`
```python
# 解析时转换字典结构
def as_date(d):
    if "date" in d:
        return d["date"]
    return d

obj = json.loads('{"date": "2024-01-01"}', object_hook=as_date)
```

**基本写法：JSONEncoder 子类**
`class <类>(json.JSONEncoder):`
```python
# 通过子类化编码器统一处理类型
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return super().default(o)

print(json.dumps({1, 2}, cls=MyEncoder))
```

---

## csv 读写

**基本写法：写入 CSV**
`csv.writer(<文件对象>)`
```python
# 写入 CSV 文件
import csv
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["name", "age"])
    w.writerow(["Tom", 18])
```

**基本写法：读取 CSV**
`csv.reader(<文件对象>)`
```python
# 读取 CSV 文件内容
with open("data.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['name', 'age']
```

**基本写法：字典方式写入**
`csv.DictWriter(<文件对象>, fieldnames=<字段列表>)`
```python
# 按字典结构写入
fields = ["name", "age"]
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerow({"name": "Tom", "age": 18})
```

**基本写法：字典方式读取**
`csv.DictReader(<文件对象>)`
```python
# 按字典结构读取
with open("data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])  # Tom
```

**基本写法：指定分隔符与引号**
`csv.writer(<文件>, delimiter=<分隔符>, quotechar=<引号字符>)`
```python
# 自定义分隔符（如 TSV 制表符分隔）
with open("data.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["a", "b"])
```

**基本写法：处理空值与方言**
`csv.register_dialect(<名称>, **<参数>)`
```python
# 注册自定义方言复用配置
csv.register_dialect("pipes", delimiter="|")
with open("data.txt", "w", newline="") as f:
    w = csv.writer(f, dialect="pipes")
    w.writerow(["a", "b"])
```

---

## pickle 序列化

**基本写法：对象转字节串**
`pickle.dumps(<对象>)`
```python
# 将任意 Python 对象序列化为字节
import pickle
data = {"name": "Tom", "list": [1, 2, 3]}
b = pickle.dumps(data)
```

**基本写法：字节串转对象**
`pickle.loads(<字节串>)`
```python
# 从字节反序列化为 Python 对象
obj = pickle.loads(b)
print(obj["name"])  # Tom
```

**基本写法：写入文件**
`pickle.dump(<对象>, <文件对象>)`
```python
# 序列化对象到文件
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

**基本写法：从文件读取**
`pickle.load(<文件对象>)`
```python
# 从文件反序列化对象
with open("data.pkl", "rb") as f:
    obj = pickle.load(f)
```

**基本写法：指定协议版本**
`pickle.dump(<对象>, <文件>, protocol=<版本>)`
```python
# 使用高版本协议提升效率
with open("data.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
```

**基本写法：批量序列化**
`pickle.dump + 循环`
```python
# 多次调用 dump 可写入多个对象
with open("data.pkl", "wb") as f:
    for item in [obj1, obj2, obj3]:
        pickle.dump(item, f)

# 读取时循环 load 直到 EOFError
with open("data.pkl", "rb") as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
```

---

## shelve 持久化字典

**基本写法：打开 shelve 数据库**
`shelve.open(<文件名>)`
```python
# 像字典一样持久化存储对象
import shelve
db = shelve.open("mydb")
db["user"] = {"name": "Tom", "age": 18}
print(db["user"]["name"])  # Tom
db.close()
```

**基本写法：上下文管理**
`with shelve.open(<文件名>) as <变量>:`
```python
# 使用 with 自动关闭
with shelve.open("mydb") as db:
    db["key"] = "value"
    for k in db:
        print(k, db[k])
```

**基本写法：写回模式**
`shelve.open(<文件名>, writeback=True)`
```python
# 启用写回，修改可变值时自动同步
with shelve.open("mydb", writeback=True) as db:
    db["list"].append("new")  # 直接修改生效
```

---

## msgpack 与 orjson（高性能扩展）

**基本写法：orjson 高速序列化**
`orjson.dumps(<对象>)`
```python
# orjson 性能远高于标准 json（返回字节）
import orjson
b = orjson.dumps(data, option=orjson.OPT_INDENT_2)
obj = orjson.loads(b)
```

**基本写法：orjson 保留中文**
`orjson.dumps(<对象>, option=orjson.OPT_NON_STR_KEYS)`
```python
# orjson 默认即返回 UTF-8 字节，无需 ensure_ascii
import orjson
print(orjson.dumps({"名": "Tom"}))  # b'{"name":"Tom"}'
```



<!-- ============ 文档分隔线：040-python/029-NetworkSocketHttp.md ============ -->

# Python 网络编程 socket/http

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## socket TCP 服务端

**基本写法：创建 TCP 服务端**
`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
```python
# 创建 IPv4 TCP 套接字并监听
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8080))
s.listen(5)
conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall(b"hello")
conn.close()
```

**基本写法：设置地址复用**
`<套接字>.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
```python
# 避免端口释放等待，立即重启绑定
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 8080))
```

**基本写法：并发接收连接**
`while True: <套接字>.accept()`
```python
# 循环接受多个客户端连接
while True:
    conn, addr = s.accept()
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # 回显
    finally:
        conn.close()
```

**基本写法：设置超时**
`<套接字>.settimeout(<秒数>)`
```python
# 设置阻塞操作的超时时间
s.settimeout(5.0)
try:
    conn, addr = s.accept()
except socket.timeout:
    print("接受连接超时")
```

---

## socket TCP 客户端

**基本写法：创建 TCP 客户端**
`<套接字>.connect((<主机>, <端口>))`
```python
# 连接服务端并发送数据
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
s.sendall(b"ping")
response = s.recv(1024)
s.close()
```

**基本写法：发送字符串数据**
`<字符串>.encode(<编码>)`
```python
# 字符串转字节后发送
s.sendall("你好".encode("utf-8"))
response = s.recv(1024).decode("utf-8")
```

---

## socket UDP 通信

**基本写法：UDP 服务端**
`socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
```python
# UDP 无连接，直接接收数据报
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 8080))
data, addr = s.recvfrom(1024)
s.sendto(b"ack", addr)
```

**基本写法：UDP 客户端**
`<套接字>.sendto(<数据>, (<主机>, <端口>))`
```python
# UDP 发送无需建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"hello", ("127.0.0.1", 8080))
data, addr = s.recvfrom(1024)
```

---

## socketserver 模块

**基本写法：TCP 请求处理类**
`class <类>(socketserver.BaseRequestHandler):`
```python
# 继承 BaseRequestHandler 简化服务端
import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.request.sendall(data)

server = socketserver.TCPServer(("127.0.0.1", 8080), Handler)
server.serve_forever()
```

**基本写法：多线程服务端**
`socketserver.ThreadingTCPServer(<地址>, <处理器>)`
```python
# 每个连接独立线程处理
server = socketserver.ThreadingTCPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()
```

**基本写法：UDP 服务端**
`socketserver.UDPServer(<地址>, <处理器>)`
```python
# UDP 请求处理
class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, sock = self.request
        sock.sendto(b"ack", self.client_address)

server = socketserver.UDPServer(("127.0.0.1", 8080), UDPHandler)
```

---

## http.client 标准库客户端

**基本写法：HTTP GET 请求**
`http.client.HTTPSConnection(<主机>)`
```python
# 发起 HTTPS GET 请求
import http.client
conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status, resp.read().decode())
conn.close()
```

**基本写法：带请求头**
`conn.request(<方法>, <路径>, <请求体>, <头字典>)`
```python
# 携带自定义请求头
headers = {"Authorization": "Bearer token123"}
conn.request("GET", "/api", headers=headers)
```

**基本写法：HTTP POST 请求**
`conn.request("POST", <路径>, <请求体>)`
```python
# 发送 POST 请求体
import json
body = json.dumps({"name": "Tom"})
conn.request("POST", "/api", body, {"Content-Type": "application/json"})
```

---

## urllib.request 请求

**基本写法：发起 GET 请求**
`urllib.request.urlopen(<URL>)`
```python
# 最简方式打开 URL
from urllib.request import urlopen
resp = urlopen("https://www.example.com")
html = resp.read().decode("utf-8")
```

**基本写法：构造 Request 对象**
`urllib.request.Request(<URL>, headers=<头>)`
```python
# 自定义请求头
from urllib.request import Request, urlopen
req = Request("https://example.com", headers={"User-Agent": "MyApp"})
resp = urlopen(req)
```

**基本写法：POST 请求**
`urlopen(<Request>, data=<字节串>)`
```python
# 发送表单数据
from urllib.parse import urlencode
data = urlencode({"q": "python"}).encode()
resp = urlopen(Request("https://example.com", data=data))
```

---

## urllib.parse URL 处理

**基本写法：URL 编码**
`urllib.parse.urlencode(<字典>)`
```python
# 字典转查询字符串
from urllib.parse import urlencode
print(urlencode({"a": 1, "b": "中文"}))  # a=1&b=%E4%B8%AD%E6%96%87
```

**基本写法：解析 URL**
`urllib.parse.urlparse(<URL>)`
```python
# 拆解 URL 各部分
from urllib.parse import urlparse
r = urlparse("https://a.com/path?q=1#frag")
print(r.scheme, r.netloc, r.path)  # https a.com /path
```

**基本写法：拼接 URL**
`urllib.parse.urljoin(<基础URL>, <相对路径>)`
```python
# 基于基础 URL 拼接相对路径
from urllib.parse import urljoin
print(urljoin("https://a.com/dir/", "page.html"))  # https://a.com/dir/page.html
```

**基本写法：解析查询字符串**
`urllib.parse.parse_qs(<查询串>)`
```python
# 查询字符串转字典
from urllib.parse import parse_qs
print(parse_qs("a=1&b=2&b=3"))  # {'a': ['1'], 'b': ['2', '3']}
```

---

## urllib.error 异常处理

**基本写法：捕获 HTTP 错误**
`urllib.error.HTTPError`
```python
# 处理 HTTP 状态码错误
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
try:
    resp = urlopen("https://example.com/404")
except HTTPError as e:
    print(e.code, e.reason)  # 404 Not Found
except URLError as e:
    print(e.reason)
```



<!-- ============ 文档分隔线：040-python/030-SysOsPlatform.md ============ -->

# Python sys/os 平台接口

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## sys 解释器接口

**基本写法：命令行参数**
`sys.argv`
```python
# 获取命令行参数列表
import sys
print(sys.argv)         # ['script.py', 'arg1', 'arg2']
print(sys.argv[1:])     # 用户传入的参数
```

**基本写法：退出程序**
`sys.exit([<状态码>])`
```python
# 退出并返回状态码
if len(sys.argv) < 2:
    sys.exit(1)  # 非零表示异常退出
```

**基本写法：标准输入输出**
`sys.stdin / sys.stdout / sys.stderr`
```python
# 重定向或直接使用标准流
sys.stdout.write("标准输出\n")
sys.stderr.write("错误信息\n")
name = sys.stdin.readline().strip()
```

**基本写法：递归深度**
`sys.getrecursionlimit() / sys.setrecursionlimit(<n>)`
```python
# 查询与设置递归深度上限
print(sys.getrecursionlimit())  # 1000
sys.setrecursionlimit(2000)
```

**基本写法：版本信息**
`sys.version / sys.version_info`
```python
# 获取解释器版本
print(sys.version_info.major, sys.version_info.minor)  # 3 12
```

**基本写法：平台标识**
`sys.platform`
```python
# 获取操作系统平台标识
print(sys.platform)  # win32 / linux / darwin
```

**基本写法：最大整数值**
`sys.maxsize`
```python
# 获取平台最大整数
print(sys.maxsize)  # 64 位系统为 2**63 - 1
```

**基本写法：模块搜索路径**
`sys.path`
```python
# 查看与修改模块搜索路径
import sys
sys.path.append("/custom/libs")
```

**基本写法：递增打印进度**
`sys.stdout.write + \r`
```python
# 原地刷新输出进度条
for i in range(101):
    sys.stdout.write(f"\r进度: {i}%")
    sys.stdout.flush()
```

---

## os 目录与文件操作

**基本写法：当前工作目录**
`os.getcwd()`
```python
# 获取当前工作目录
import os
print(os.getcwd())
```

**基本写法：切换目录**
`os.chdir(<路径>)`
```python
# 改变当前工作目录
os.chdir("/tmp")
```

**基本写法：列出目录内容**
`os.listdir(<路径>)`
```python
# 列出目录下所有条目
for name in os.listdir("."):
    print(name)
```

**基本写法：创建目录**
`os.mkdir(<路径>) / os.makedirs(<路径>)`
```python
# 创建单层或多层目录
os.mkdir("newdir")
os.makedirs("a/b/c", exist_ok=True)
```

**基本写法：删除文件与目录**
`os.remove(<文件>) / os.rmdir(<空目录>)`
```python
# 删除文件或空目录
os.remove("data.txt")
os.rmdir("emptydir")
```

**基本写法：递归删除目录树**
`shutil.rmtree(<目录>)`
```python
# 递归删除非空目录
import shutil
shutil.rmtree("old_project")
```

**基本写法：重命名与移动**
`os.rename(<旧名>, <新名>)`
```python
# 重命名文件或目录
os.rename("old.txt", "new.txt")
```

**基本写法：递归遍历目录**
`os.walk(<路径>)`
```python
# 自顶向下遍历目录树
for root, dirs, files in os.walk("."):
    for f in files:
        print(os.path.join(root, f))
```

**基本写法：文件信息**
`os.stat(<路径>)`
```python
# 获取文件大小、修改时间等元信息
st = os.stat("data.txt")
print(st.st_size, st.st_mtime)
```

---

## os 环境与进程

**基本写法：环境变量**
`os.environ`
```python
# 读取与设置环境变量
print(os.environ.get("HOME"))
os.environ["MY_VAR"] = "value"
```

**基本写法：获取进程号**
`os.getpid() / os.getppid()`
```python
# 获取当前进程与父进程 ID
print(os.getpid(), os.getppid())
```

**基本写法：执行系统命令**
`os.system(<命令>)`
```python
# 执行 shell 命令并返回退出码
ret = os.system("echo hello")
```

**基本写法：CPU 核数**
`os.cpu_count()`
```python
# 获取系统 CPU 核心数
print(os.cpu_count())
```

**基本写法：获取系统随机字节**
`os.urandom(<字节数>)`
```python
# 生成密码学安全的随机字节
token = os.urandom(16)
```

---

## os.path 路径操作

**基本写法：拼接路径**
`os.path.join(<路径1>, <路径2>)`
```python
# 跨平台安全拼接路径
p = os.path.join("dir", "sub", "file.txt")
```

**基本写法：判断存在**
`os.path.exists(<路径>)`
```python
# 判断路径是否存在
print(os.path.exists("data.txt"))
```

**基本写法：判断文件与目录**
`os.path.isfile(<路径>) / os.path.isdir(<路径>)`
```python
# 区分文件与目录
print(os.path.isfile("a.txt"), os.path.isdir("d"))
```

**基本写法：取文件名与目录名**
`os.path.basename(<路径>) / os.path.dirname(<路径>)`
```python
# 拆分路径末尾与父目录
print(os.path.basename("/a/b/c.txt"))  # c.txt
print(os.path.dirname("/a/b/c.txt"))   # /a/b
```

**基本写法：扩展名拆分**
`os.path.splitext(<路径>)`
```python
# 分离文件名与扩展名
name, ext = os.path.splitext("archive.tar.gz")
print(name, ext)  # archive.tar .gz
```

**基本写法：绝对路径**
`os.path.abspath(<路径>) / os.path.realpath(<路径>)`
```python
# 转换为绝对路径并解析软链接
print(os.path.abspath("../a.txt"))
print(os.path.realpath("link.txt"))
```

**基本写法：路径大小与时间**
`os.path.getsize(<路径>) / os.path.getmtime(<路径>)`
```python
# 获取文件大小与修改时间
print(os.path.getsize("a.txt"))
```

---

## platform 平台信息

**基本写法：操作系统类型**
`platform.system()`
```python
# 获取操作系统名称
import platform
print(platform.system())  # Windows / Linux / Darwin
```

**基本写法：Python 版本**
`platform.python_version()`
```python
# 获取当前 Python 版本字符串
print(platform.python_version())  # 3.12.0
```

**基本写法：机器架构**
`platform.machine()`
```python
# 获取 CPU 架构
print(platform.machine())  # AMD64 / arm64
```



<!-- ============ 文档分隔线：040-python/031-MathRandomStatistics.md ============ -->

# Python math/random/statistics

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## math 数学函数

**基本写法：平方根与幂**
`math.sqrt(<数>) / math.pow(<底>, <指数>)`
```python
# 开方与幂运算
import math
print(math.sqrt(16))      # 4.0
print(math.pow(2, 10))    # 1024.0
```

**基本写法：数学常量**
`math.pi / math.e / math.inf / math.nan`
```python
# 内置数学常量
print(math.pi)     # 3.141592653589793
print(math.e)      # 2.718281828459045
print(math.inf)    # 正无穷
```

**基本写法：向上向下取整**
`math.ceil(<数>) / math.floor(<数>)`
```python
# 取整运算
print(math.ceil(3.2))    # 4
print(math.floor(3.8))   # 3
```

**基本写法：绝对值与符号**
`math.fabs(<数>) / math.copysign(<数1>, <数2>)`
```python
# 取绝对值与复制符号
print(math.fabs(-5))         # 5.0
print(math.copysign(3, -1))  # -3.0
```

**基本写法：阶乘**
`math.factorial(<整数>)`
```python
# 计算阶乘
print(math.factorial(5))  # 120
```

**基本写法：最大公约数与最小公倍数**
`math.gcd(<a>, <b>) / math.lcm(<a>, <b>)`
```python
# Python 3.9+ lcm 计算最小公倍数
print(math.gcd(12, 18))  # 6
print(math.lcm(4, 6))    # 12
```

**基本写法：对数运算**
`math.log(<数>[, <底>]) / math.log2 / math.log10`
```python
# 各类对数
print(math.log(8, 2))    # 3.0
print(math.log10(1000))  # 3.0
```

**基本写法：三角函数**
`math.sin(<弧度>) / math.cos / math.tan`
```python
# 角度需先转弧度
print(math.sin(math.pi / 2))  # 1.0
print(math.degrees(math.pi))  # 180.0
```

**基本写法：浮点判断**
`math.isfinite(<数>) / math.isnan(<数>)`
```python
# 判断有限与 NaN
print(math.isfinite(1.0))  # True
print(math.isnan(math.nan))  # True
```

**基本写法：精确求和**
`math.fsum(<可迭代>)`
```python
# 避免浮点累计误差
print(math.fsum([0.1] * 10))  # 1.0
```

**基本写法：融合乘加（Python 3.13+）**
`math.fma(<a>, <b>, <c>)`
```python
# 单次舍入的 a*b+c，精度更高
print(math.fma(2.0, 3.0, 1.0))  # 7.0
```

---

## random 随机数

**基本写法：设置随机种子**
`random.seed(<种子>)`
```python
# 固定种子保证结果可复现
import random
random.seed(42)
print(random.random())
```

**基本写法：0 到 1 随机浮点**
`random.random()`
```python
# 生成 [0.0, 1.0) 随机浮点数
x = random.random()
```

**基本写法：指定范围随机整数**
`random.randint(<起>, <止>)`
```python
# 生成 [a, b] 闭区间整数
print(random.randint(1, 100))
```

**基本写法：随机选择元素**
`random.choice(<序列>)`
```python
# 从非空序列随机选一个
print(random.choice(["a", "b", "c"]))
```

**基本写法：加权随机选择**
`random.choices(<序列>, weights=<权重>, k=<数量>)`
```python
# 按权重有放回抽样
result = random.choices(["红", "蓝"], weights=[1, 3], k=5)
```

**基本写法：打乱序列**
`random.shuffle(<列表>)`
```python
# 原地打乱列表顺序
cards = list(range(1, 11))
random.shuffle(cards)
```

**基本写法：无放回抽样**
`random.sample(<序列>, k=<数量>)`
```python
# 不重复抽取 k 个元素
print(random.sample(range(1, 50), 6))  # 随机 6 个不重复
```

**基本写法：区间随机浮点**
`random.uniform(<起>, <止>)`
```python
# 生成 [a, b] 随机浮点数
print(random.uniform(1.5, 3.5))
```

**基本写法：高斯分布**
`random.gauss(<均值>, <标准差>)`
```python
# 生成正态分布随机数
print(random.gauss(0, 1))
```

**基本写法：随机字节**
`random.randbytes(<字节数>)`
```python
# Python 3.9+ 生成随机字节
print(random.randbytes(8))
```

**基本写法：命令行生成随机数**
`python -m random`
```python
# Python 3.13+ 可通过命令行生成随机数
# 命令行执行：python -m random
```

---

## statistics 统计函数

**基本写法：平均值**
`statistics.mean(<数据>)`
```python
# 计算算术平均数
import statistics
print(statistics.mean([1, 2, 3, 4]))  # 2.5
```

**基本写法：中位数**
`statistics.median(<数据>)`
```python
# 计算中位数
print(statistics.median([1, 3, 2, 4]))  # 2.5
```

**基本写法：众数**
`statistics.mode(<数据>) / statistics.multimode(<数据>)`
```python
# 计算众数，multimode 返回所有众数
print(statistics.mode([1, 2, 2, 3]))      # 2
print(statistics.multimode([1, 1, 2, 2]))  # [1, 2]
```

**基本写法：标准差**
`statistics.stdev(<数据>) / statistics.pstdev(<数据>)`
```python
# 样本标准差与总体标准差
data = [1, 2, 3, 4, 5]
print(statistics.stdev(data))   # 1.5811...
print(statistics.pstdev(data))  # 1.4142...
```

**基本写法：方差**
`statistics.variance(<数据>) / statistics.pvariance(<数据>)`
```python
# 样本方差与总体方差
print(statistics.variance(data))
```

**基本写法：分位数**
`statistics.quantiles(<数据>, n=<份数>)`
```python
# 将数据分为 n 份返回分位点
print(statistics.quantiles([1, 2, 3, 4, 5, 6], n=4))  # 四分位数
```

**基本写法：相关系数与线性回归**
`statistics.linear_regression(<x>, <y>)`
```python
# 计算线性回归斜率与截距
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
slope, intercept = statistics.linear_regression(x, y)
print(slope, intercept)  # 2.0 0.0
```

**基本写法：几何平均与调和平均**
`statistics.geometric_mean(<数据>) / statistics.harmonic_mean(<数据>)`
```python
# 几何平均与调和平均
print(statistics.geometric_mean([1, 2, 4]))  # 2.0
print(statistics.harmonic_mean([1, 2, 4]))   # 1.714...
```



<!-- ============ 文档分隔线：040-python/032-Subprocess.md ============ -->

# Python subprocess 子进程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## subprocess.run 推荐用法

**基本写法：执行命令**
`subprocess.run([<命令>, <参数1>, <参数2>])`
```python
# 以列表形式执行命令（推荐，避免注入）
import subprocess
result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result.stdout)  # hello
```

**基本写法：捕获输出**
`subprocess.run(<命令>, capture_output=True, text=True)`
```python
# 捕获标准输出与错误输出
r = subprocess.run(["python", "-V"], capture_output=True, text=True)
print(r.stdout, r.stderr)
```

**基本写法：字符串命令（shell 模式）**
`subprocess.run(<命令字符串>, shell=True)`
```python
# 使用 shell 解析管道与通配符
r = subprocess.run("dir | findstr py", shell=True, capture_output=True, text=True)
```

**基本写法：检查返回码**
`subprocess.run(<命令>, check=True)`
```python
# 非零返回码抛出 CalledProcessError
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print(f"命令失败: {e.returncode}")
```

**基本写法：设置工作目录**
`subprocess.run(<命令>, cwd=<目录>)`
```python
# 指定子进程工作目录
subprocess.run(["ls"], cwd="/tmp", capture_output=True, text=True)
```

**基本写法：设置环境变量**
`subprocess.run(<命令>, env=<环境字典>)`
```python
# 自定义子进程环境变量
import os
env = {**os.environ, "DEBUG": "1"}
subprocess.run(["python", "main.py"], env=env)
```

**基本写法：设置超时**
`subprocess.run(<命令>, timeout=<秒数>)`
```python
# 超时抛出 TimeoutExpired
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("执行超时")
```

**基本写法：传入输入**
`subprocess.run(<命令>, input=<字符串>, text=True)`
```python
# 通过 stdin 传入输入
r = subprocess.run(["python", "-c", "print(input()*2)"], input="ab", text=True, capture_output=True)
print(r.stdout)  # abab
```

**基本写法：输入输出编码**
`subprocess.run(<命令>, encoding=<编码>)`
```python
# 指定编码替代 text=True
r = subprocess.run(["echo", "中文"], encoding="utf-8", capture_output=True)
```

---

## Popen 进程对象

**基本写法：创建子进程**
`subprocess.Popen([<命令>, <参数>])`
```python
# 获取进程对象进行交互
p = subprocess.Popen(["python", "-u", "task.py"], stdout=subprocess.PIPE, text=True)
out = p.communicate()[0]
print(out)
```

**基本写法：管道通信**
`<进程>.communicate([input=<输入>])`
```python
# 一次性读取全部输出并等待结束
p = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
out, err = p.communicate(input="hello")
print(out)  # hello
```

**基本写法：等待进程结束**
`<进程>.wait([timeout=<秒>])`
```python
# 阻塞等待子进程退出
p = subprocess.Popen(["sleep", "2"])
p.wait()
print("进程已结束")
```

**基本写法：轮询状态**
`<进程>.poll()`
```python
# 非阻塞检查是否结束
p = subprocess.Popen(["sleep", "2"])
while p.poll() is None:
    print("运行中")
```

**基本写法：终止进程**
`<进程>.terminate() / <进程>.kill()`
```python
# terminate 发送 SIGTERM，kill 发送 SIGKILL
p = subprocess.Popen(["sleep", "100"])
p.terminate()
```

**基本写法：获取进程号**
`<进程>.pid`
```python
# 获取子进程 PID
p = subprocess.Popen(["sleep", "1"])
print(p.pid)
```

---

## 管道串联

**基本写法：命令管道串联**
`Popen(stdout=Popen.stdin)`
```python
# 模拟 shell 管道：ps | grep python
p1 = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(["grep", "python"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()
out = p2.communicate()[0]
print(out)
```

---

## check_output / call / check_call

**基本写法：获取标准输出**
`subprocess.check_output(<命令>)`
```python
# 直接返回标准输出，失败抛异常
out = subprocess.check_output(["python", "-V"], text=True, stderr=subprocess.STDOUT)
print(out)
```

**基本写法：仅执行并取返回码**
`subprocess.call(<命令>)`
```python
# 返回退出码，不抛异常
code = subprocess.call(["ls", "-l"])
```

**基本写法：执行并校验**
`subprocess.check_call(<命令>)`
```python
# 返回码非零抛 CalledProcessError
subprocess.check_call(["echo", "ok"])
```

---

## 输入输出重定向

**基本写法：输出重定向到文件**
`subprocess.run(<命令>, stdout=<文件对象>)`
```python
# 将输出写入文件
with open("out.log", "w", encoding="utf-8") as f:
    subprocess.run(["python", "-V"], stdout=f)
```

**基本写法：合并标准错误到标准输出**
`subprocess.run(<命令>, stderr=subprocess.STDOUT)`
```python
# 合并 stderr 到 stdout 一起捕获
r = subprocess.run(["python", "err.py"], capture_output=True, stderr=subprocess.STDOUT, text=True)
print(r.stdout)
```

**基本写法：从文件输入**
`subprocess.run(<命令>, stdin=<文件对象>)`
```python
# 从文件读取 stdin
with open("input.txt", encoding="utf-8") as f:
    subprocess.run(["python", "process.py"], stdin=f)
```



<!-- ============ 文档分隔线：040-python/033-Logging.md ============ -->

# Python logging 日志配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础配置

**基本写法：快速配置**
`logging.basicConfig(level=<级别>)`
```python
# 一行配置根 logger 输出级别
import logging
logging.basicConfig(level=logging.DEBUG)
logging.info("启动服务")
```

**基本写法：带格式与文件**
`logging.basicConfig(filename=<文件>, format=<格式>, level=<级别>)`
```python
# 输出到文件并定义格式
logging.basicConfig(
    filename="app.log",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
```

**基本写法：获取命名 logger**
`logging.getLogger(<名称>)`
```python
# 每个模块使用独立 logger 便于追踪
logger = logging.getLogger(__name__)
logger.warning("模块警告")
```

---

## 日志级别

**基本写法：各级别日志**
`logger.<级别>(<消息>)`
```python
# 从低到高五个级别
logger.debug("调试详情")
logger.info("一般信息")
logger.warning("警告")
logger.error("错误")
logger.critical("严重错误")
```

**基本写法：自定义级别**
`logging.addLevelName(<数值>, <名称>)`
```python
# 注册自定义日志级别
TRACE = 5
logging.addLevelName(TRACE, "TRACE")
logger.log(TRACE, "追踪信息")
```

**基本写法：按级别输出**
`logger.log(<级别>, <消息>)`
```python
# 动态指定级别
logger.log(logging.ERROR, "动态级别错误")
```

---

## Handler 输出目标

**基本写法：控制台输出**
`logging.StreamHandler()`
```python
# 添加控制台处理器
import sys
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
logger.addHandler(console)
```

**基本写法：文件输出**
`logging.FileHandler(<文件>)`
```python
# 日志写入指定文件
fh = logging.FileHandler("app.log", encoding="utf-8")
fh.setLevel(logging.INFO)
logger.addHandler(fh)
```

**基本写法：按大小滚动**
`logging.handlers.RotatingFileHandler(<文件>, maxBytes=<字节>, backupCount=<份数>)`
```python
# 单文件超限后自动轮转
from logging.handlers import RotatingFileHandler
rh = RotatingFileHandler("app.log", maxBytes=10 * 1024 * 1024, backupCount=5)
logger.addHandler(rh)
```

**基本写法：按时间滚动**
`logging.handlers.TimedRotatingFileHandler(<文件>, when=<周期>, backupCount=<份数>)`
```python
# 按时间周期切割日志
from logging.handlers import TimedRotatingFileHandler
th = TimedRotatingFileHandler("app.log", when="midnight", backupCount=7)
logger.addHandler(th)
```

---

## Formatter 格式化

**基本写法：定义格式器**
`logging.Formatter(<格式字符串>)`
```python
# 设置日志显示格式
fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
fh.setFormatter(fmt)
logger.addHandler(fh)
```

**基本写法：常用字段**
`%(asctime)s %(name)s %(levelname)s %(message)s`
```python
# 常用格式字段说明
# asctime 时间 | name logger 名 | levelname 级别
# filename 文件名 | lineno 行号 | funcName 函数名
fmt = logging.Formatter("%(filename)s:%(lineno)d %(message)s")
```

---

## 异常日志

**基本写法：记录异常堆栈**
`logger.exception(<消息>)`
```python
# 在 except 中输出完整堆栈
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("除零异常")
```

**基本写法：exc_info 参数**
`logger.error(<消息>, exc_info=True)`
```python
# 任意级别附加异常信息
try:
    open("missing.txt")
except FileNotFoundError:
    logger.error("文件不存在", exc_info=True)
```

---

## dictConfig 字典配置

**换行写法：字典配置**
`logging.config.dictConfig(<配置字典>)`
```python
# 集中化配置多 handler 与 logger
import logging.config
config = {
    "version": 1,
    "formatters": {"simple": {"format": "%(asctime)s %(message)s"}},
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
logging.config.dictConfig(config)
```

---

## 禁用与过滤

**基本写法：禁用日志**
`logging.disable(<级别>)`
```python
# 禁用指定级别及以下日志
logging.disable(logging.DEBUG)  # 关闭 DEBUG
```

**基本写法：按级别过滤**
`logging.Filter`
```python
# 自定义过滤器
class LevelFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING

logger.addFilter(LevelFilter())
```

---

## 模块化 logger 最佳实践

**基本写法：模块级 logger**
`logger = logging.getLogger(__name__)`
```python
# 每个 Python 文件顶部声明 logger
# mymodule.py
import logging
logger = logging.getLogger(__name__)

def do_work():
    logger.info("开始处理")
```

**基本写法：设置第三方库日志级别**
`logging.getLogger(<库名>).setLevel(<级别>)`
```python
# 抑制第三方库的过多日志
logging.getLogger("urllib3").setLevel(logging.WARNING)
```

**基本写法：禁止传播**
`logger.propagate = False`
```python
# 防止日志向父 logger 重复输出
logger.propagate = False
```



<!-- ============ 文档分隔线：040-python/034-UnittestPytest.md ============ -->

# Python 测试 unittest/pytest

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## unittest 基础

**基本写法：编写测试类**
`class <类>(unittest.TestCase):`
```python
# 继承 TestCase 编写单元测试
import unittest

class TestString(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("abc".upper(), "ABC")
```

**基本写法：运行测试**
`python -m unittest <模块>`
```python
# 命令行运行 unittest 测试
# 执行：python -m unittest test_my module
# 自动发现：python -m unittest discover
```

---

## unittest 断言

**基本写法：相等断言**
`self.assertEqual(<实际>, <期望>)`
```python
# 验证两值相等
self.assertEqual(sum([1, 2]), 3)
```

**基本写法：不等与布尔**
`self.assertNotEqual / self.assertTrue / self.assertFalse`
```python
# 不等与布尔断言
self.assertNotEqual(1, 2)
self.assertTrue("a" in "abc")
self.assertFalse([])
```

**基本写法：判断异常**
`self.assertRaises(<异常类>)`
```python
# 验证代码抛出指定异常
with self.assertRaises(ZeroDivisionError):
    1 / 0
```

**基本写法：异常匹配**
`self.assertRaisesRegex(<异常>, <正则>)`
```python
# 验证异常消息匹配
with self.assertRaisesRegex(ValueError, "invalid"):
    int("abc")
```

**基本写法：近似比较**
`self.assertAlmostEqual(<实际>, <期望>, places=<小数位>)`
```python
# 浮点数近似相等比较
self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
```

**基本写法：包含判断**
`self.assertIn / self.assertNotIn`
```python
# 判断成员关系
self.assertIn(2, [1, 2, 3])
self.assertNotIn("x", "abc")
```

**基本写法：None 判断**
`self.assertIsNone / self.assertIsNotNone`
```python
# 判断是否为 None
self.assertIsNone(None)
self.assertIsNotNone(0)
```

---

## unittest 前后置

**基本写法：每个用例前后置**
`def setUp(self) / def tearDown(self)`
```python
# 每个测试方法前后执行
class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = create_conn()

    def tearDown(self):
        self.conn.close()

    def test_query(self):
        self.assertTrue(self.conn.query())
```

**基本写法：类级前后置**
`@classmethod def setUpClass / tearDownClass`
```python
# 整个测试类只执行一次
class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_fixture()

    @classmethod
    def tearDownClass(cls):
        cls.data = None
```

---

## pytest 基础

**基本写法：函数式测试**
`def test_<函数名>():`
```python
# pytest 无需继承，直接写函数
def test_addition():
    assert 1 + 1 == 2
```

**基本写法：运行 pytest**
`pytest [<选项>]`
```python
# 常用命令行运行方式
# pytest                       运行所有测试
# pytest test_x.py             运行指定文件
# pytest -k "add"              按名称匹配运行
# pytest -v                    详细输出
# pytest --tb=short            简短回溯
```

**基本写法：异常断言**
`pytest.raises(<异常类>)`
```python
# 验证抛出异常
import pytest
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

**基本写法：近似断言**
`pytest.approx(<期望>)`
```python
# 浮点近似比较
def test_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

---

## pytest fixture

**基本写法：定义 fixture**
`@pytest.fixture`
```python
# 通过 fixture 注入测试数据
@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_len(sample_list):
    assert len(sample_list) == 3
```

**基本写法：yield 前后置**
`@pytest.fixture`
`def <名>(): yield <值>`
```python
# yield 前为准备，后为清理
@pytest.fixture
def db_conn():
    conn = create_conn()
    yield conn
    conn.close()
```

**基本写法：fixture 作用域**
`@pytest.fixture(scope="<作用域>")`
```python
# 控制 fixture 生命周期
@pytest.fixture(scope="session")
def config():
    return load_config()  # 整个会话只执行一次
```

**基本写法：自动使用**
`@pytest.fixture(autouse=True)`
```python
# 自动应用到所有测试，无需参数
@pytest.fixture(autouse=True)
def reset_state():
    yield
    clear_cache()
```

---

## pytest 参数化

**基本写法：参数化测试**
`@pytest.mark.parametrize("<参数>", [(<值1>,), (<值2>,)])`
```python
# 一组数据生成多个用例
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (4, 5, 9),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

---

## pytest 标记

**基本写法：自定义标记**
`@pytest.mark.<标记名>`
```python
# 标记测试分类运行
@pytest.mark.slow
def test_big_data():
    ...

# 运行：pytest -m slow
```

**基本写法：跳过测试**
`@pytest.mark.skip(reason="<原因>")`
```python
# 无条件跳过
@pytest.mark.skip(reason="暂不支持")
def test_future():
    pass
```

**基本写法：条件跳过**
`@pytest.mark.skipif(<条件>, reason="<原因>")`
```python
# 满足条件时跳过
import sys
@pytest.mark.skipif(sys.platform == "win32", reason="仅 Linux")
def test_unix_only():
    pass
```

**基本写法：预期失败**
`@pytest.mark.xfail`
```python
# 标记为预期失败，失败不报错
@pytest.mark.xfail(reason="已知 bug")
def test_known_issue():
    assert 1 == 2
```

---

## mock 模拟

**基本写法：patch 替换对象**
`unittest.mock.patch("<目标>")`
```python
# 临时替换函数或对象
from unittest.mock import patch

@patch("mymodule.requests.get")
def test_api(mock_get):
    mock_get.return_value.status_code = 200
    assert mymodule.fetch() == 200
```

**基本写法：配置 mock 行为**
`mock.return_value / mock.side_effect`
```python
# 设置返回值或副作用
mock_get.return_value.json.return_value = {"ok": True}
mock_get.side_effect = ConnectionError("超时")  # 抛异常
```

**基本写法：断言调用**
`mock.assert_called_once_with(<参数>)`
```python
# 验证 mock 被调用情况
mock_get.assert_called_once_with("https://api.com")
mock_get.assert_not_called()
```

**基本写法：MagicMock**
`MagicMock()`
```python
# 创建支持魔法方法的模拟对象
from unittest.mock import MagicMock
m = MagicMock()
m.__len__.return_value = 5
print(len(m))  # 5
```



<!-- ============ 文档分隔线：040-python/035-MetaclassDescriptor.md ============ -->

# Python 元类与描述符

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## type 动态创建类

**基本写法：type 三参数创建类**
`type(<类名>, <父类元组>, <属性字典>)`
```python
# 动态创建一个类
MyClass = type("MyClass", (), {"x": 10, "greet": lambda self: "hi"})
obj = MyClass()
print(obj.x, obj.greet())  # 10 hi
```

**基本写法：带父类动态创建**
`type(<类名>, (<父类>,), <属性>)`
```python
# 继承父类动态创建
class Base:
    def show(self):
        return "base"

Derived = type("Derived", (Base,), {"y": 20})
print(Derived().show())  # base
```

---

## 自定义元类

**换行写法：定义元类**
`class <元类>(type):`
`    def __new__(mcs, name, bases, ns): <语句>`
```python
# 通过元类统一改造类创建过程
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        namespace["created_by"] = "Meta"
        return super().__new__(mcs, name, bases, namespace)

class Foo(metaclass=Meta):
    pass

print(Foo.created_by)  # Meta
```

**基本写法：使用元类**
`class <类>(metaclass=<元类>):`
```python
# 指定类创建时使用的元类
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DB(metaclass=SingletonMeta):
    pass

a, b = DB(), DB()
print(a is b)  # True
```

**基本写法：元类拦截属性**
`def __init_subclass__(cls, **<参数>):`
```python
# 子类创建时触发，无需自定义元类
class Plugin:
    registry = []
    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if name:
            Plugin.registry.append(name)

class Foo(Plugin, name="foo"):
    pass

print(Plugin.registry)  # ['foo']
```

**基本写法：类参数化**
`def __class_getitem__(cls, <参数>):`
```python
# 支持 SomeClass[int] 形式
class Container:
    def __class_getitem__(cls, item):
        return f"Container[{item.__name__}]"

print(Container[int])  # Container[int]
```

---

## 描述符协议

**基本写法：定义描述符**
`class <描述符>:`
`    def __get__(self, obj, owner): <语句>`
```python
# 实现描述符协议的对象作为类属性时被特殊处理
class TypedField:
    def __init__(self, expected_type):
        self.expected_type = expected_type
    def __get__(self, obj, owner):
        return obj.__dict__.get(self.name)
    def __set_name__(self, owner, name):
        self.name = name
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} 需要 {self.expected_type}")
        obj.__dict__[self.name] = value

class User:
    age = TypedField(int)

u = User()
u.age = 18
# u.age = "x"  # 抛出 TypeError
```

**基本写法：数据描述符**
`__get__ + __set__`
```python
# 同时定义 __get__ 和 __set__ 为数据描述符
# 优先级高于实例字典
class Validator:
    def __get__(self, obj, owner):
        return obj.__dict__.get("_val")
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("不能为负")
        obj.__dict__["_val"] = value
```

**基本写法：非数据描述符**
`仅 __get__`
```python
# 只定义 __get__ 为非数据描述符
# 实例字典优先级高于它
class Const:
    def __init__(self, value):
        self.value = value
    def __get__(self, obj, owner):
        return self.value

class Config:
    version = Const("1.0.0")

print(Config().version)  # 1.0.0
```

**基本写法：删除描述符**
`def __delete__(self, obj):`
```python
# 实现删除拦截
class Protected:
    def __get__(self, obj, owner):
        return obj._data
    def __delete__(self, obj):
        raise PermissionError("禁止删除")
```

**基本写法：__set_name__ 自动命名**
`def __set_name__(self, owner, <属性名>):`
```python
# 类创建时自动获取属性名
class Field:
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, obj, owner):
        return obj.__dict__.get(self.name)
```

---

## property 内置描述符

**基本写法：property 定义**
`property(<fget>, [fset], [fdel], [doc])`
```python
# property 本质是数据描述符
class Temperature:
    def __init__(self):
        self._c = 0
    @property
    def celsius(self):
        return self._c
    @celsius.setter
    def celsius(self, value):
        self._c = value

t = Temperature()
t.celsius = 25
```

---

## 元类与描述符组合

**换行写法：元类收集描述符**
`class <元类>(type):`
`    def __new__(mcs, name, bases, ns): <收集描述符>`
```python
# ORM 风格字段收集
class Field:
    def __set_name__(self, owner, name):
        self.name = name

class ModelMeta(type):
    def __new__(mcs, name, bases, ns):
        fields = {k: v for k, v in ns.items() if isinstance(v, Field)}
        ns["_fields"] = fields
        return super().__new__(mcs, name, bases, ns)

class Model(metaclass=ModelMeta):
    pass

class User(Model):
    id = Field()
    name = Field()

print(User._fields.keys())  # dict_keys(['id', 'name'])
```

---

## abstractmethod 抽象方法

**基本写法：抽象基类**
`from abc import ABC, abstractmethod`
```python
# 强制子类实现抽象方法
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):
    def sound(self):
        return "汪"

# Animal()  # 抛出 TypeError
print(Dog().sound())  # 汪
```

**基本写法：抽象属性**
`@property @abstractmethod`
```python
# 强制子类实现属性
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...
```



<!-- ============ 文档分隔线：040-python/036-Python312313NewFeatures.md ============ -->

# Python 3.12/3.13 新特性语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Python 3.12 类型形参语法（PEP 695）

**基本写法：泛型函数**
`def <函数名>[<类型变量>](<参数>: <类型变量>) -> <类型变量>:`
```python
# 无需先声明 TypeVar，直接在函数签名定义
def identity[T](x: T) -> T:
    return x

def first[T](items: list[T]) -> T:
    return items[0]
```

**基本写法：泛型类**
`class <类名>[<类型变量>]:`
```python
# 类级别类型参数
class Box[T]:
    def __init__(self, value: T):
        self.value = value
    def get(self) -> T:
        return self.value
```

**基本写法：带约束的泛型**
`def <函数>[<T>: <边界>](<参数>: <T>) -> <T>:`
```python
# 使用冒号指定上界 bound
from collections.abc import Hashable
def lookup[T: Hashable](key: T, mapping: dict[T, int]) -> int:
    return mapping[key]
```

**基本写法：类型别名语句**
`type <别名>[<类型变量>] = <表达式>`
```python
# type 语句定义类型别名，支持递归引用
type Point = tuple[float, float]
type ListOrSet[T] = list[T] | set[T]

def f(p: Point) -> None: ...
```

**基本写法：多个类型变量**
`def <函数>[T, U](<参数>) -> <类型>:`
```python
# 多类型参数
def map_fn[T, U](items: list[T], fn: callable) -> list[U]:
    return [fn(x) for x in items]
```

---

## Python 3.12 f-string 改进（PEP 701）

**基本写法：嵌套引号**
`f"{f"{<表达式>}"}"`
```python
# 同类引号嵌套不再冲突
names = ["a", "b"]
print(f"{", ".join(names)}")  # a, b
```

**基本写法：表达式含反斜杠**
`f"{<含反斜杠表达式>}"`
```python
# f-string 表达式部分可使用反斜杠
print(f"{'a\nb'.upper()}")  # A\nB
```

**基本写法：多行 f-string 表达式**
`f"{<换行表达式>}"`
```python
# 表达式可跨行书写
key = "name"
value = "Tom"
msg = f"{
    {key: value}
}"
```

**基本写法：注释与换行**
`f"{<表达式>  # 注释}"`
```python
# f-string 表达式内可含注释
print(f"{1 + 1  # 相加
}")
```

---

## Python 3.12 其他新特性

**基本写法：override 装饰器（PEP 698）**
`@typing.override`
```python
# 显式标记覆盖父类方法，便于静态检查
import typing

class Base:
    def run(self): ...

class Child(Base):
    @typing.override
    def run(self):
        print("子类实现")
```

**基本写法：TypedDict 标注 kwargs（PEP 692）**
`def f(**<kwargs>: <TypedDict>)`
```python
# 精确标注 **kwargs 的键类型
from typing import TypedDict, Unpack

class Options(TypedDict):
    timeout: int
    retry: int

def fetch(url: str, **opts: Unpack[Options]) -> None: ...
```

**基本写法：推导式内联（PEP 709）**
`[<表达式> for <变量> in <可迭代>]`
```python
# 推导式改为内联实现，性能提升且不再泄漏变量
x = [i for i in range(10)]
print("i" in dir())  # False（不再泄漏）
```

---

## Python 3.13 TypeVar 默认值（PEP 696）

**基本写法：TypeVar 默认值**
`def <函数>[<T> = <默认类型>]()`
```python
# 不指定类型参数时使用默认类型
def get_items[T = str]() -> list[T]:
    return []

# 不带类型参数等价于 list[str]
result = get_items()
```

**基本写法：泛型类默认值**
`class <类>[T = <默认>]:`
```python
# 泛型类同样支持默认类型参数
from dataclasses import dataclass

@dataclass
class Box[T = int]:
    value: T | None = None

b = Box()         # 默认为 Box[int]
b = Box("x")      # 推断为 Box[str]
```

**基本写法：Generator 默认参数**
`def <函数>() -> Generator[T]:`
```python
# 简化生成器返回类型
from collections.abc import Generator

def f() -> Generator[int]:
    yield 42
```

---

## Python 3.13 deprecated 装饰器（PEP 702）

**基本写法：标记弃用**
`@warnings.deprecated("<说明>")`
```python
# 静态类型检查器与运行时双重弃用警告
import warnings

@warnings.deprecated("改用 new_func")
def old_func():
    return "old"

# 调用时触发 DeprecationWarning
```

**基本写法：弃用类方法**
`@warnings.deprecated("<说明>")`
```python
# 装饰类的方法
class API:
    @warnings.deprecated("使用 v2 接口")
    def query(self):
        pass
```

---

## Python 3.13 TypeIs（PEP 742）

**基本写法：TypeIs 类型收窄**
`def <函数>(<参数>: <类型>) -> TypeIs[<子类型>]:`
```python
# 比 TypeGuard 更精确，收窄后互补类型也确定
from typing import TypeIs

def is_str(x: int | str) -> TypeIs[str]:
    return isinstance(x, str)

def f(x: int | str):
    if is_str(x):
        print(x.upper())  # 推断为 str
    else:
        print(x + 1)       # 推断为 int
```

---

## Python 3.13 ReadOnly（PEP 705）

**基本写法：只读 TypedDict 字段**
`class <TypedDict>: <字段>: ReadOnly[<类型>]`
```python
# 标记字段为只读，不可重新赋值
from typing import TypedDict, ReadOnly

class Movie(TypedDict):
    title: ReadOnly[str]
    year: int

m: Movie = {"title": "A", "year": 2024}
# m["title"] = "B"  # 类型检查报错
```

---

## Python 3.13 运行时改进

**基本写法：locals() 语义明确化（PEP 667）**
`locals()`
```python
# locals() 返回的快照与实际局部变量同步
def f():
    x = 1
    d = locals()
    d["x"] = 99  # 现在会反映到局部变量
```

**基本写法：彩色 traceback**
`PYTHON_COLORS=1`
```python
# 默认彩色输出错误回溯，可通过环境变量控制
# 启用：set PYTHON_COLORS=1
# 禁用：set PYTHON_COLORS=0
```

**基本写法：math.fma 融合乘加**
`math.fma(<a>, <b>, <c>)`
```python
# 单次舍入的 a * b + c，精度更高
import math
print(math.fma(2.0, 3.0, 1.0))  # 7.0
```

**基本写法：Path.from_uri**
`Path.from_uri(<file URI>)`
```python
# 从 file:// URI 创建路径对象
from pathlib import Path
p = Path.from_uri("file:///home/user/file.txt")
print(p)
```

**基本写法：process_cpu_count**
`os.process_cpu_count()`
```python
# 获取进程可用的 CPU 核心数（考虑 cgroup 限制）
import os
print(os.process_cpu_count())
```

---

## Python 3.13 实验性特性

**基本写法：自由线程（PEP 703）**
`python -X gil=0`
```python
# 实验性禁用 GIL 的自由线程构建
# 启动：python -X gil=0 script.py
# 多线程可真正并行执行 Python 字节码
```

**基本写法：JIT 编译器（PEP 744）**
`python -X jit`
```python
# 实验性 JIT 编译器，默认关闭
# 启用：python -X jit script.py
```

---

## Python 3.13 移除内容（PEP 594）

**基本写法：移除的旧模块**
`# 以下模块在 3.13 移除`
```python
# 已移除的旧标准库模块（建议替代）
# aifc -> wave / stdaudio
# cgi -> multipart
# imghdr -> filetype
# mailcap -> 标准库外
# nntplib -> pynntp
# ossaudiodev -> 第三方
# pipes -> shlex
# sndhdr -> filetype
# sunau -> wave
# telnetlib -> telnetlib3 / Exscript
# uu -> base64
# xdrlib -> xdr 庫
# 2to3 工具也已移除
```



<!-- ============ 文档分隔线：040-python/037-StringFormattingMethods.md ============ -->

# Python 字符串格式化与方法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## f-string 格式化

**基本写法：基础 f-string**
`f"<前缀>{<表达式>}<后缀>"`
```python
# 变量直接嵌入字符串
name = "Tom"
age = 18
print(f"姓名: {name}, 年龄: {age}")
```

**基本写法：表达式与运算**
`f"{<表达式计算>}"`
```python
# 大括号内支持任意表达式
print(f"总价: {10 * 2.5:.2f}")
print(f"长度: {len(name)}")
```

**基本写法：浮点精度**
`f"{<值>:.<小数位>f}"`
```python
# 控制小数位数
pi = 3.14159
print(f"{pi:.2f}")  # 3.14
```

**基本写法：宽度与对齐**
`f"{<值>:<填充><对齐><宽度>}"`
```python
# < 左对齐 | > 右对齐 | ^ 居中
print(f"{name:>10}")   # 右对齐宽 10
print(f"{name:<10}")   # 左对齐
print(f"{name:^10}")   # 居中
print(f"{name:0>10}")  # 用 0 填充
```

**基本写法：千分位分隔**
`f"{<值>:,}"`
```python
# 数字千分位逗号
print(f"{1000000:,}")    # 1,000,000
print(f"{1000000:,.2f}") # 1,000,000.00
```

**基本写法：百分比与科学计数**
`f"{<值>:%} / f"{<值>:e}"`
```python
# 百分比与科学计数法
ratio = 0.85
print(f"{ratio:.1%}")   # 85.0%
print(f"{1234567:.2e}") # 1.23e+06
```

**基本写法：进制转换**
`f"{<值>:b/o/x/X}"`
```python
# 二进制 八进制 十六进制
n = 255
print(f"{n:b}")  # 11111111
print(f"{n:o}")  # 377
print(f"{n:x}")  # ff
print(f"{n:#x}") # 0xff（带前缀）
```

**基本写法：调试输出**
`f"{<变量>=}"`
```python
# Python 3.8+ 自动显示变量名与值
x = 42
print(f"{x=}")        # x=42
print(f"{x=:>10}")    # x=        42
```

**基本写法：转换标志**
`f"{<值>!r/!s/!a}"`
```python
# 强制使用 repr / str / ascii
s = "中文"
print(f"{s!r}")  # '中文'
print(f"{s!s}")  # 中文
```

**基本写法：日期格式化**
`f"{<日期>:%Y-%m-%d}"`
```python
# 直接用 strftime 格式说明符
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
```

---

## format 方法

**基本写法：位置参数**
`"<{}>".format(<值>)`
```python
# 按位置填充占位符
print("{}, {}".format("a", "b"))
print("{0} - {1}".format("a", "b"))
```

**基本写法：命名参数**
`"{<名称>}".format(<名称>=<值>)`
```python
# 按名称填充
print("{name} {age}".format(name="Tom", age=18))
```

**基本写法：format_map**
`"<{name}>".format_map(<字典>)`
```python
# 直接从字典读取键值
data = {"name": "Tom", "age": 18}
print("{name}-{age}".format_map(data))
```

---

## % 旧式格式化

**基本写法：% 格式化**
`"<格式串>" % (<值1>, <值2>)`
```python
# 旧式百分号格式化
print("name=%s, age=%d" % ("Tom", 18))
print("pi=%.2f" % 3.14159)
```

---

## Template 模板字符串

**基本写法：Template 替换**
`Template("<$名称>").substitute(<字典>)`
```python
# 安全的字符串模板替换
from string import Template
t = Template("$name 的成绩是 $score")
print(t.substitute(name="Tom", score=90))
print(t.safe_substitute({"name": "Tom"}))  # 缺失键保留原样
```

---

## 字符串拆分与拼接

**基本写法：split 拆分**
`<字符串>.split([<分隔符>[, <最大次数>]])`
```python
# 按分隔符拆分为列表
print("a,b,c".split(","))      # ['a', 'b', 'c']
print("a-b-c".split("-", 1))   # ['a', 'b-c']
```

**基本写法：rsplit 从右拆分**
`<字符串>.rsplit([<分隔符>[, <最大次数>]])`
```python
# 从右侧开始拆分
print("a.b.c".rsplit(".", 1))  # ['a.b', 'c']
```

**基本写法：splitlines 按行拆分**
`<字符串>.splitlines([keepends=<布尔>])`
```python
# 按换行符拆分为行列表
print("a\nb\nc".splitlines())
print("a\nb".splitlines(keepends=True))  # ['a\n', 'b']
```

**基本写法：join 拼接**
`<分隔符>.join(<可迭代>)`
```python
# 将可迭代对象拼接为字符串
print(",".join(["a", "b", "c"]))  # a,b,c
print("-".join(str(i) for i in range(5)))
```

**基本写法：partition 分段**
`<字符串>.partition(<分隔符>)`
```python
# 分成三段元组（前、分隔符、后）
print("a=b=c".partition("="))  # ('a', '=', 'b=c')
print("a=b".rpartition("="))   # ('a', '=', 'b')
```

---

## 字符串查找与替换

**基本写法：find 查找位置**
`<字符串>.find(<子串>[, <起>[, <止>]])`
```python
# 返回首次出现位置，找不到返回 -1
print("hello".find("l"))     # 2
print("hello".find("x"))     # -1
```

**基本写法：index 查找**
`<字符串>.index(<子串>)`
```python
# 与 find 类似，找不到抛 ValueError
print("hello".index("l"))
```

**基本写法：count 计数**
`<字符串>.count(<子串>)`
```python
# 统计子串出现次数
print("banana".count("a"))  # 3
```

**基本写法：replace 替换**
`<字符串>.replace(<旧>, <新>[, <次数>])`
```python
# 替换子串，可限制次数
print("a-b-c".replace("-", "+"))      # a+b+c
print("a-b-c".replace("-", "+", 1))   # a+b-c
```

**基本写法：前后缀判断**
`<字符串>.startswith(<前缀>) / .endswith(<后缀>)`
```python
# 判断开头或结尾
print("abc.py".endswith(".py"))   # True
print("abc".startswith("a"))      # True
```

---

## 字符串修剪与对齐

**基本写法：strip 去空白**
`<字符串>.strip([<字符集>])`
```python
# 去除两端空白或指定字符
print("  hi  ".strip())   # hi
print("##hi##".strip("#")) # hi
```

**基本写法：单侧去除**
`lstrip / rstrip`
```python
# 仅去除左侧或右侧
print("  hi  ".lstrip())  # "hi  "
print("  hi  ".rstrip())  # "  hi"
```

**基本写法：对齐填充**
`ljust / rjust / center`
```python
# 指定宽度对齐并填充
print("ab".ljust(5, "-"))   # ab---
print("ab".rjust(5, "-"))   # ---ab
print("ab".center(5, "-"))  # -ab--
```

**基本写法：补零**
`<字符串>.zfill(<宽度>)`
```python
# 左侧补零到指定宽度
print("42".zfill(5))  # 00042
```

---

## 大小写转换

**基本写法：大小写转换**
`upper / lower / title / swapcase`
```python
# 各类大小写转换
print("Hello".upper())      # HELLO
print("Hello".lower())      # hello
print("hello world".title()) # Hello World
print("aBc".swapcase())     # AbC
```

**基本写法：casefold 强制折叠**
`<字符串>.casefold()`
```python
# 更激进的小写转换，适合国际化比较
print("STRASSE".casefold())  # strasse
```

**基本写法：首字母大写**
`<字符串>.capitalize()`
```python
# 仅首字符大写其余小写
print("hELLO".capitalize())  # Hello
```

---

## 字符串判断

**基本写法：字符类型判断**
`isalpha / isdigit / isalnum / isspace`
```python
# 判断字符串组成类型
print("abc".isalpha())    # True
print("123".isdigit())    # True
print("  ".isspace())     # True
print("a1".isalnum())     # True
```

---

## 字符串转换

**基本写法：编码与解码**
`<字符串>.encode(<编码>) / <字节>.decode(<编码>)`
```python
# 字符串与字节互转
b = "中文".encode("utf-8")
print(b)                    # b'\xe4\xb8\xad...'
print(b.decode("utf-8"))    # 中文
```

**基本写法：translate 映射**
`<字符串>.translate(<映射表>)`
```python
# 按映射表批量替换字符
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))  # h2ll4
```

**基本写法：删除指定字符**
`str.maketrans("", "", <要删除字符>)`
```python
# 第三参数指定要删除的字符
table = str.maketrans("", "", "0123456789")
print("a1b2c".translate(table))  # abc
```



<!-- ============ 文档分隔线：040-python/038-ArgparseCli.md ============ -->

# Python argparse 命令行参数解析

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ArgumentParser 创建解析器

**基本写法：创建解析器**
`argparse.ArgumentParser([description=<描述>])`
```python
# 创建参数解析器
import argparse
parser = argparse.ArgumentParser(description="数据处理工具")
args = parser.parse_args()
```

**基本写法：完整构造参数**
`ArgumentParser(prog=<名称>, description=<描述>, epilog=<结尾说明>)`
```python
# 自定义程序名、描述与结尾说明
parser = argparse.ArgumentParser(
    prog="myapp",
    description="图片处理 CLI",
    epilog="示例: myapp resize --size 100",
)
```

**基本写法：运行并获取参数**
`<解析器>.parse_args()`
```python
# 解析命令行参数为命名空间对象
args = parser.parse_args()
print(args.filename)
```

---

## add_argument 添加参数

**基本写法：位置参数**
`<解析器>.add_argument(<参数名>)`
```python
# 必填位置参数
parser.add_argument("filename")
# 运行：python app.py data.txt
args = parser.parse_args()
print(args.filename)  # data.txt
```

**基本写法：可选参数**
`<解析器>.add_argument("-<短>", "--<长>")`
```python
# 带 - 前缀的可选参数
parser.add_argument("-v", "--verbose", help="详细输出")
# 运行：python app.py --verbose yes
```

**基本写法：指定类型**
`<解析器>.add_argument(<名>, type=<类型>)`
```python
# 自动类型转换
parser.add_argument("--count", type=int, default=1)
parser.add_argument("--rate", type=float)
```

**基本写法：默认值**
`<解析器>.add_argument(<名>, default=<默认值>)`
```python
# 未提供时使用默认值
parser.add_argument("--mode", default="auto")
```

**基本写法：限定取值**
`<解析器>.add_argument(<名>, choices=<列表>)`
```python
# 限制参数取值范围
parser.add_argument("--log", choices=["debug", "info", "error"])
```

**基本写法：必填可选参数**
`<解析器>.add_argument(<名>, required=True)`
```python
# 标记可选参数为必填
parser.add_argument("--config", required=True)
```

**基本写法：帮助文本**
`<解析器>.add_argument(<名>, help=<说明>)`
```python
# 提供 --help 时显示的说明
parser.add_argument("path", help="目标文件路径")
```

---

## nargs 多值参数

**基本写法：接收多个值**
`<解析器>.add_argument(<名>, nargs=<数量>)`
```python
# 指定接收 N 个值
parser.add_argument("--coords", nargs=2, type=float)  # 接收 2 个
```

**基本写法：可变数量**
`nargs="?" / "*" / "+"`
```python
# ? 零或一，* 零或多，+ 一或多
parser.add_argument("files", nargs="+", help="至少一个文件")
parser.add_argument("--opt", nargs="?", const="x", default="y")
```

**基本写法：收集剩余所有参数**
`nargs=argparse.REMAINDER`
```python
# 收集剩余参数传给子命令
parser.add_argument("cmd", nargs=argparse.REMAINDER)
```

---

## action 参数行为

**基本写法：布尔开关**
`action="store_true" / "store_false"`
```python
# 标志位，出现即 True / False
parser.add_argument("--dry-run", action="store_true")
parser.add_argument("--no-cache", action="store_false", dest="cache")
```

**基本写法：计数**
`action="count"`
```python
# 统计出现次数（如 -vvv 表示级别 3）
parser.add_argument("-v", action="count", default=0)
```

**基本写法：追加到列表**
`action="append"`
```python
# 重复参数追加为列表
parser.add_argument("--tag", action="append")
# 运行 --tag a --tag b => ['a', 'b']
```

**基本写法：追加字面值**
`action="append_const"`
```python
# 追加常量值到列表
parser.add_argument("--debug", action="append_const", const="debug")
```

---

## 子命令 subparsers

**换行写法：定义子命令**
`<解析器>.add_subparsers(dest=<字段>, required=True)`
```python
# 实现 git 风格子命令
sub = parser.add_subparsers(dest="cmd", required=True)

commit = sub.add_parser("commit", help="提交")
commit.add_argument("-m", "--message", required=True)

push = sub.add_parser("push", help="推送")
push.add_argument("--force", action="store_true")
```

**基本写法：绑定子命令处理函数**
`<子解析器>.set_defaults(func=<函数>)`
```python
# 为每个子命令绑定处理函数
def do_commit(args):
    print(f"提交: {args.message}")

commit.set_defaults(func=do_commit)

args = parser.parse_args()
args.func(args)
```

---

## 互斥参数组

**基本写法：互斥组**
`<解析器>.add_mutually_exclusive_group()`
```python
# 组内参数不能同时出现
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", action="store_true")
group.add_argument("--quiet", action="store_true")
```

**基本写法：必填互斥组**
`add_mutually_exclusive_group(required=True)`
```python
# 必须从互斥组中选一个
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--input")
group.add_argument("--from-stdin", action="store_true")
```

---

## 参数组与元信息

**基本写法：参数分组**
`<解析器>.add_argument_group(<组标题>)`
```python
# 在帮助信息中分组显示
db_group = parser.add_argument_group("数据库选项")
db_group.add_argument("--host")
db_group.add_argument("--port", type=int)
```

**基本写法：自定义参数显示名**
`<解析器>.add_argument(<名>, metavar=<显示名>)`
```python
# 在帮助信息中显示为自定义名
parser.add_argument("--input", metavar="FILE")
```

**基本写法：指定存储属性名**
`<解析器>.add_argument(<名>, dest=<属性名>)`
```python
# 将参数值绑定到自定义属性名
parser.add_argument("--rate", dest="speed")
print(args.speed)
```

---

## 文件类型参数

**基本写法：文件参数**
`type=argparse.FileType(<模式>)`
```python
# 自动打开文件并传入文件对象
parser.add_argument("--out", type=argparse.FileType("w"))
parser.add_argument("infile", type=argparse.FileType("r", encoding="utf-8"))
args = parser.parse_args()
args.out.write("done")
args.infile.close()
```

---

## 自定义类型转换

**基本写法：自定义 type 函数**
`type=<转换函数>`
```python
# 通过函数实现自定义转换
def hex_int(s):
    return int(s, 16)

parser.add_argument("--color", type=hex_int)
# 运行：--color ff => 255
```

**基本写法：正则校验**
`type=<校验函数>`
```python
# 校验失败抛 argparse.ArgumentTypeError
import re
def email(s):
    if not re.match(r"^[\w.]+@[\w.]+$", s):
        raise argparse.ArgumentTypeError("非法邮箱")
    return s

parser.add_argument("--email", type=email)
```

---

## 自定义动作

**换行写法：自定义 Action**
`class <动作>(argparse.Action):`
```python
# 通过子类化实现复杂参数处理
class UpperAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.upper())

parser.add_argument("--name", action=UpperAction)
```

---

## 错误处理与帮助

**基本写法：自定义错误处理**
`<解析器>.error(<消息>)`
```python
# 触发错误并退出
args = parser.parse_args()
if args.port < 0:
    parser.error("端口不能为负数")
```

**基本写法：禁止缩写匹配**
`ArgumentParser(allow_abbrev=False)`
```python
# 禁止 --ver 自动匹配 --verbose
parser = argparse.ArgumentParser(allow_abbrev=False)
```

**基本写法：formatter_class 控制帮助格式**
`ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)`
```python
# 保留 description 中的原始格式
parser = argparse.ArgumentParser(
    description="多行说明\n第二行",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
```



<!-- ============ 文档分隔线：040-python/039-FunctionalProgramming.md ============ -->

# Python 函数式编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## lambda 表达式

**基本写法：匿名函数**
`lambda <参数>: <表达式>`
```python
# 定义返回参数平方的匿名函数
square = lambda x: x * x
print(square(5))
```

**基本写法：多参数 lambda**
`lambda <参数1>, <参数2>: <表达式>`
```python
# 多参数匿名函数
add = lambda x, y: x + y
print(add(3, 4))
```

**基本写法：作为排序 key**
`sorted(<可迭代>, key=lambda <参数>: <表达式>)`
```python
# 按元组第二元素排序
data = [("a", 3), ("b", 1), ("c", 2)]
print(sorted(data, key=lambda x: x[1]))
```

---

## map 映射

**基本写法：对每个元素应用函数**
`map(<函数>, <可迭代>)`
```python
# 将列表每个元素平方
nums = [1, 2, 3, 4]
result = list(map(lambda x: x ** 2, nums))
```

**基本写法：多可迭代对象**
`map(<函数>, <可迭代1>, <可迭代2>)`
```python
# 对应位置元素相加
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
```

**基本写法：转换类型**
`map(<类型>, <可迭代>)`
```python
# 字符串列表转整数
nums = list(map(int, ["1", "2", "3"]))
```

---

## filter 过滤

**基本写法：按条件过滤**
`filter(<函数>, <可迭代>)`
```python
# 过滤出偶数
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
```

**基本写法：过滤 falsy 值**
`filter(None, <可迭代>)`
```python
# 移除所有 falsy 值
data = [0, 1, None, "", "a", False, 2]
result = list(filter(None, data))
```

---

## reduce 归约

**基本写法：累积归约**
`functools.reduce(<函数>, <可迭代>)`
```python
# 累加求和
from functools import reduce
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
```

**基本写法：带初始值**
`functools.reduce(<函数>, <可迭代>, <初始值>)`
```python
# 带初始值的累加
total = reduce(lambda x, y: x + y, nums, 100)
```

**基本写法：归约成字典**
`functools.reduce(<函数>, <可迭代>)`
```python
# 将键值对列表合并为字典
pairs = [("a", 1), ("b", 2), ("c", 3)]
result = reduce(lambda d, kv: {**d, kv[0]: kv[1]}, pairs, {})
```

---

## partial 偏函数

**基本写法：固定部分参数**
`functools.partial(<函数>, <参数>)`
```python
# 固定 base 参数
from functools import partial
int2 = partial(int, base=2)
print(int2("1010"))
```

**基本写法：固定关键字参数**
`functools.partial(<函数>, <键>=<值>)`
```python
# 固定关键字参数
def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
```

**基本写法：partial 对象属性**
`partial.func` | `partial.args` | `partial.keywords`
```python
# 查看偏函数的原始信息
p = partial(int, base=2)
print(p.func, p.keywords)
```

---

## 高阶函数

**基本写法：函数作为参数**
`def <函数>(<参数>, <函数参数>):`
```python
# 接收函数作为参数的高阶函数
def apply(func, value):
    return func(value)
print(apply(str.upper, "hello"))
```

**基本写法：返回函数**
`def <函数>(): return <内嵌函数>`
```python
# 工厂模式返回函数
def multiplier(n):
    return lambda x: x * n
times3 = multiplier(3)
print(times3(5))
```

---

## operator 运算符函数

**基本写法：算术运算函数**
`operator.add` | `operator.sub` | `operator.mul`
```python
# operator 模块提供运算符对应的函数
import operator
print(operator.add(3, 4))
print(operator.mul(3, 4))
```

**基本写法：取元素函数**
`operator.itemgetter(<索引>)`
```python
# itemgetter 创建取元素函数
f = operator.itemgetter(1)
print(f(("a", "b", "c")))
```

**基本写法：取属性函数**
`operator.attrgetter(<属性名>)`
```python
# attrgetter 创建取属性函数
class User:
    def __init__(self, name):
        self.name = name
f = operator.attrgetter("name")
print(f(User("Alice")))
```

**基本写法：方法调用函数**
`operator.methodcaller(<方法名>)`
```python
# methodcaller 创建调用方法的函数
f = operator.methodcaller("upper")
print(f("hello"))
```

---

## itertools 函数式工具

**基本写法：starmap 解包应用**
`itertools.starmap(<函数>, <可迭代>)`
```python
# starmap 解包元组作为参数
from itertools import starmap
pairs = [(1, 2), (3, 4)]
result = list(starmap(lambda x, y: x + y, pairs))
```

**基本写法：accumulate 累积**
`itertools.accumulate(<可迭代>, <函数>)`
```python
# 累积运算
from itertools import accumulate
nums = [1, 2, 3, 4]
print(list(accumulate(nums, lambda x, y: x + y)))
```

---

## 闭包

**基本写法：闭包捕获变量**
`def <外层>():\n    <变量> = <值>\n    def <内层>(): return <变量>`
```python
# 闭包捕获外层变量
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
c = make_counter()
print(c(), c(), c())
```

**基本写法：nonlocal 修改闭包变量**
`nonlocal <变量名>`
```python
# 在内层函数中修改外层变量
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)
```



<!-- ============ 文档分隔线：040-python/040-IteratorGeneratorAdvanced.md ============ -->

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



<!-- ============ 文档分隔线：040-python/041-ContextManagerAdvanced.md ============ -->

# Python 上下文管理器进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 自定义上下文管理器

**基本写法：实现 __enter__/__exit__**
`class <类>:\n    def __enter__(self): ...\n    def __exit__(self, exc_type, exc, tb):`
```python
# 经典上下文管理器实现
class FileOpener:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        self.f = open(self.path, "r")
        return self.f
    def __exit__(self, exc_type, exc, tb):
        self.f.close()
        return False

with FileOpener("data.txt") as f:
    print(f.read())
```

**基本写法：抑制异常**
`def __exit__(self, exc_type, exc, tb): return True`
```python
# 返回 True 抑制 with 块内的异常
class Suppressor:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type is ValueError:
            return True
        return False

with Suppressor():
    raise ValueError("被抑制")
```

---

## contextlib.contextmanager

**基本写法：装饰器生成上下文管理器**
`@contextlib.contextmanager`
```python
# 用生成器函数简化上下文管理器
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("标题")
```

**基本写法：带返回值**
`yield <值>`
```python
# yield 的值会绑定到 as 变量
@contextmanager
def open_db(url):
    conn = connect(url)
    try:
        yield conn
    finally:
        conn.close()

with open_db("sqlite://") as db:
    db.execute("SELECT 1")
```

**基本写法：处理异常**
`try: yield\nexcept <异常> as e:`
```python
# 在生成器中捕获异常
@contextmanager
def safe_op():
    try:
        yield
    except ValueError as e:
        print(f"捕获 {e}")
```

---

## contextlib 工具

**基本写法：closing 包装关闭**
`contextlib.closing(<对象>)`
```python
# 为只有 close 方法的对象提供上下文
from contextlib import closing
import urllib.request

with closing(urllib.request.urlopen("http://example.com")) as r:
    print(r.read()[:50])
```

**基本写法：suppress 抑制异常**
`contextlib.suppress(<异常类>)`
```python
# 抑制指定异常
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("nonexistent.txt")
```

**基本写法：redirect_stdout 重定向**
`contextlib.redirect_stdout(<目标>)`
```python
# 重定向标准输出
from contextlib import redirect_stdout
import io

buf = io.StringIO()
with redirect_stdout(buf):
    print("捕获这行")
print(buf.getvalue())
```

**基本写法：redirect_stderr 重定向**
`contextlib.redirect_stderr(<目标>)`
```python
# 重定向标准错误
import io
buf = io.StringIO()
with redirect_stderr(buf):
    import warnings
    warnings.warn("警告")
```

---

## ExitStack 动态管理

**基本写法：ExitStack 动态管理**
`contextlib.ExitStack()`
```python
# 动态管理多个上下文
from contextlib import ExitStack

files = []
with ExitStack() as stack:
    for name in ["a.txt", "b.txt"]:
        files.append(stack.enter_context(open(name)))
```

**基本写法：enter_context 进入上下文**
`stack.enter_context(<上下文管理器>)`
```python
# 动态添加上下文管理器
with ExitStack() as stack:
    f1 = stack.enter_context(open("a.txt"))
    f2 = stack.enter_context(open("b.txt"))
    stack.callback(lambda: print("清理"))
```

**基本写法：callback 注册清理回调**
`stack.callback(<函数>, *<参数>)`
```python
# 注册退出时回调
with ExitStack() as stack:
    stack.callback(print, "退出时调用")
    print("执行中")
```

**基本写法：push 推入清理函数**
`stack.push(<退出函数>)`
```python
# 推入任意退出函数
def cleanup():
    print("清理完成")
with ExitStack() as stack:
    stack.push(cleanup)
```

---

## 异步上下文管理器

**基本写法：实现 __aenter__/__aexit__**
`class <类>:\n    async def __aenter__(self): ...\n    async def __aexit__(self, exc_type, exc, tb):`
```python
# 异步上下文管理器
class AsyncConn:
    async def __aenter__(self):
        await self.connect()
        return self
    async def __aexit__(self, exc_type, exc, tb):
        await self.close()
        return False
    async def connect(self): pass
    async def close(self): pass

async def main():
    async with AsyncConn() as conn:
        pass
```

**基本写法：asynccontextmanager 装饰器**
`@contextlib.asynccontextmanager`
```python
# 异步上下文管理器装饰器
from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def timer():
    start = asyncio.get_event_loop().time()
    yield
    print(f"耗时 {asyncio.get_event_loop().time() - start}")

async def main():
    async with timer():
        await asyncio.sleep(0.5)
```

---

## AsyncExitStack

**基本写法：异步动态管理**
`contextlib.AsyncExitStack()`
```python
# 异步动态管理多个上下文
from contextlib import AsyncExitStack

async def main():
    async with AsyncExitStack() as stack:
        c1 = await stack.enter_async_context(AsyncConn())
        c2 = await stack.enter_async_context(AsyncConn())
```

**基本写法：push_async_callback**
`stack.push_async_callback(<协程函数>)`
```python
# 注册异步清理回调
async def main():
    async with AsyncExitStack() as stack:
        stack.push_async_callback(asyncio.sleep, 0)
```

---

## 多上下文嵌套

**基本写法：多上下文嵌套**
`with <ctx1> as <a>, <ctx2> as <b>:`
```python
# 多上下文同时管理
with open("a") as fa, open("b") as fb:
    pass
```

**基本写法：括号换行**
`with (<ctx1> as <a>,\n      <ctx2> as <b>):`
```python
# 3.10+ 支持括号内换行
with (
    open("a") as fa,
    open("b") as fb,
):
    pass
```



<!-- ============ 文档分隔线：040-python/042-DecoratorAdvanced.md ============ -->

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



<!-- ============ 文档分隔线：040-python/043-TypingAdvanced.md ============ -->

# Python typing 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：040-python/044-Enum.md ============ -->

# Python enum 枚举

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：040-python/045-ConcurrentFutures.md ============ -->

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



<!-- ============ 文档分隔线：040-python/046-HashlibHmac.md ============ -->

# Python hashlib 与 hmac

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## hashlib 哈希

**基本写法：创建哈希对象**
`hashlib.<算法名>()`
```python
# 创建 SHA256 哈希对象
import hashlib

h = hashlib.sha256()
h.update(b"hello")
print(h.hexdigest())
```

**基本写法：直接计算哈希**
`hashlib.<算法名>(<字节>)`
```python
# 一步计算哈希值
h = hashlib.sha256(b"hello")
print(h.hexdigest())
```

**基本写法：update 分块更新**
`h.update(<字节>)`
```python
# 分块更新大文件哈希
h = hashlib.sha256()
with open("big.bin", "rb") as f:
    while chunk := f.read(8192):
        h.update(chunk)
print(h.hexdigest())
```

**基本写法：hexdigest 十六进制**
`h.hexdigest()`
```python
# 返回十六进制字符串
print(hashlib.sha256(b"x").hexdigest())
```

**基本写法：digest 字节**
`h.digest()`
```python
# 返回原始字节摘要
print(hashlib.sha256(b"x").digest())
```

---

## 常用算法

**基本写法：md5**
`hashlib.md5(<字节>)`
```python
# MD5（不推荐用于安全场景）
print(hashlib.md5(b"hello").hexdigest())
```

**基本写法：sha1**
`hashlib.sha1(<字节>)`
```python
# SHA1
print(hashlib.sha1(b"hello").hexdigest())
```

**基本写法：sha256 / sha512**
`hashlib.sha256(<字节>)` | `hashlib.sha512(<字节>)`
```python
# SHA256 与 SHA512
print(hashlib.sha256(b"hello").hexdigest())
print(hashlib.sha512(b"hello").hexdigest())
```

**基本写法：sha3_256（3.6+）**
`hashlib.sha3_256(<字节>)`
```python
# SHA3 系列
print(hashlib.sha3_256(b"hello").hexdigest())
```

**基本写法：blake2**
`hashlib.blake2b(<字节>)` | `hashlib.blake2s(<字节>)`
```python
# BLAKE2 哈希
print(hashlib.blake2b(b"hello").hexdigest())
print(hashlib.blake2s(b"hello").hexdigest())
```

**基本写法：查询可用算法**
`hashlib.algorithms_available`
```python
# 当前实现可用的算法集合
print(hashlib.algorithms_available)
```

**基本写法：保证可用算法**
`hashlib.algorithms_guaranteed`
```python
# 所有平台保证可用的算法
print(hashlib.algorithms_guaranteed)
```

---

## HMAC 消息认证

**基本写法：创建 HMAC**
`hmac.new(<密钥>, <消息>, <哈希算法>)`
```python
# 创建 HMAC
import hmac
import hashlib

m = hmac.new(b"secret_key", b"hello", hashlib.sha256)
print(m.hexdigest())
```

**基本写法：update 更新消息**
`m.update(<字节>)`
```python
# 分块更新 HMAC
m = hmac.new(b"key", b"", hashlib.sha256)
m.update(b"hello")
m.update(b"world")
print(m.hexdigest())
```

**基本写法：compare_digest 安全比较**
`hmac.compare_digest(<a>, <b>)`
```python
# 常量时间比较，防止时序攻击
a = hmac.new(b"key", b"msg", hashlib.sha256).digest()
b = hmac.new(b"key", b"msg", hashlib.sha256).digest()
print(hmac.compare_digest(a, b))
```

**基本写法：digest 字节**
`m.digest()`
```python
# 返回字节摘要
print(m.digest())
```

---

## secrets 安全随机

**基本写法：生成安全随机字节**
`secrets.token_bytes(<长度>)`
```python
# 生成加密安全的随机字节
import secrets

print(secrets.token_bytes(16))
```

**基本写法：生成安全随机字符串**
`secrets.token_hex(<长度>)`
```python
# 生成十六进制随机字符串
print(secrets.token_hex(16))
```

**基本写法：生成 URL 安全字符串**
`secrets.token_urlsafe(<长度>)`
```python
# 生成 URL 安全的随机字符串
print(secrets.token_urlsafe(16))
```

**基本写法：安全随机整数**
`secrets.randbelow(<上界>)`
```python
# 生成 0 到 n-1 的安全随机整数
print(secrets.randbelow(100))
```

**基本写法：安全选择**
`secrets.choice(<序列>)`
```python
# 从序列中安全随机选择
print(secrets.choice("abcdef"))
```

**基本写法：生成口令**
`secrets.choice` 配合 string
```python
# 生成 16 位随机口令
import string
alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for _ in range(16))
print(password)
```

---

## 文件哈希校验

**基本写法：文件 SHA256**
`def <函数>(<路径>):`
```python
# 计算文件 SHA256
def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()
```

---

## 密码哈希（推荐）

**基本写法：pbkdf2_hmac**
`hashlib.pbkdf2_hmac(<算法>, <密码>, <盐>, <迭代次数>)`
```python
# PBKDF2 密码哈希
salt = os.urandom(16)
key = hashlib.pbkdf2_hmac("sha256", b"password", salt, 100000)
print(key.hex())
```

**基本写法：scrypt（3.6+）**
`hashlib.scrypt(<密码>, salt=<盐>, n=<参数>, r=<参数>, p=<参数>)`
```python
# scrypt 密码哈希
salt = os.urandom(16)
key = hashlib.scrypt(b"password", salt=salt, n=16384, r=8, p=1)
print(key.hex())
```



<!-- ============ 文档分隔线：040-python/047-SslCrypto.md ============ -->

# Python ssl 安全套接字

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SSLContext 上下文

**基本写法：创建默认上下文**
`ssl.create_default_context(<用途>)`
```python
# 创建默认 SSL 上下文
import ssl

ctx = ssl.create_default_context()  # 服务端验证
ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)  # 服务端
```

**基本写法：创建基础上下文**
`ssl.SSLContext(<协议>)`
```python
# 手动创建上下文
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
```

**基本写法：加载证书**
`ctx.load_cert_chain(<证书>, keyfile=<密钥>)`
```python
# 加载服务器证书与私钥
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("server.crt", keyfile="server.key")
```

**基本写法：加载 CA 证书**
`ctx.load_verify_locations(<CA 文件>)`
```python
# 加载 CA 证书用于验证
ctx = ssl.create_default_context()
ctx.load_verify_locations("ca-bundle.crt")
```

---

## 客户端配置

**基本写法：禁用主机名检查**
`ctx.check_hostname = False`
```python
# 关闭主机名校验（不推荐）
ctx = ssl.create_default_context()
ctx.check_hostname = False
```

**基本写法：调整验证模式**
`ctx.verify_mode = ssl.CERT_NONE`
```python
# 关闭证书验证（不推荐）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
```

**基本写法：设置最低 TLS 版本**
`ctx.minimum_version = ssl.TLSVersion.TLSv1_2`
```python
# 设置最低 TLS 版本
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
```

---

## 包装套接字

**基本写法：包装客户端套接字**
`ctx.wrap_socket(<套接字>, server_hostname=<主机>)`
```python
# 客户端包装 socket
import socket
import ssl

ctx = ssl.create_default_context()
sock = socket.create_connection(("www.python.org", 443))
ssock = ctx.wrap_socket(sock, server_hostname="www.python.org")
ssock.send(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
print(ssock.recv(1024)[:50])
ssock.close()
```

**基本写法：包装服务端套接字**
`ctx.wrap_socket(<套接字>, server_side=True)`
```python
# 服务端包装 socket
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain("server.crt", keyfile="server.key")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 8443))
sock.listen()
ssock, addr = ctx.wrap_socket(sock, server_side=True)
```

---

## 证书信息

**基本写法：获取对端证书**
`ssock.getpeercert()`
```python
# 获取对端证书字典
cert = ssock.getpeercert()
print(cert["subject"])
```

**基本写法：获取证书二进制**
`ssock.getpeercert(binary_form=True)`
```python
# 获取 DER 编码的证书
der = ssock.getpeercert(binary_form=True)
print(len(der))
```

**基本写法：cipher 信息**
`ssock.cipher()`
```python
# 获取当前使用的加密套件
print(ssock.cipher())
```

**基本写法：协议版本**
`ssock.version()`
```python
# 获取协商的 TLS 版本
print(ssock.version())
```

---

## 证书校验回调

**基本写法：设置回调**
`ctx.set_servername_callback(<函数>)`
```python
# 服务端根据 SNI 选择证书
def sni_callback(sslsocket, sni_name, ssl_context):
    if sni_name == "example.com":
        ssl_context.load_cert_chain("example.crt", "example.key")

ctx.set_servername_callback(sni_callback)
```

---

## 证书与 PKCS

**基本写法：DER 转 PEM**
`ssl.DER_cert_to_PEM_cert(<DER 字节>)`
```python
# DER 转 PEM 字符串
pem = ssl.DER_cert_to_PEM_cert(der_bytes)
```

**基本写法：PEM 转 DER**
`ssl.PEM_cert_to_DER_cert(<PEM 字符串>)`
```python
# PEM 转 DER 字节
der = ssl.PEM_cert_to_DER_cert(pem_string)
```

---

## OCSP 与 CRL

**基本写法：加载 CRL**
`ctx.load_verify_locations(cafile=<文件>)`
```python
# 加载证书吊销列表
ctx = ssl.create_default_context()
ctx.load_verify_locations(cafile="crl.pem")
ctx.verify_flags |= ssl.VERIFY_CRL_CHECK_LEAF
```

**基本写法：3.13 默认严格标志**
`ctx.verify_flags`
```python
# Python 3.13 默认启用 VERIFY_X509_STRICT 等
ctx = ssl.create_default_context()
print(ctx.verify_flags)
```

---

## 常量与枚举

**基本写法：TLSVersion**
`ssl.TLSVersion.TLSv1_2` | `ssl.TLSVersion.TLSv1_3`
```python
# TLS 版本常量
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
ctx.maximum_version = ssl.TLSVersion.TLSv1_3
```

**基本写法：CERT_* 验证模式**
`ssl.CERT_NONE` | `ssl.CERT_OPTIONAL` | `ssl.CERT_REQUIRED`
```python
# 证书验证模式
ctx.verify_mode = ssl.CERT_REQUIRED
```



<!-- ============ 文档分隔线：040-python/048-HttpClient.md ============ -->

# Python http.client HTTP 客户端

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## HTTPConnection

**基本写法：创建连接**
`http.client.HTTPConnection(<主机>, <端口>)`
```python
# 创建 HTTP 连接
import http.client

conn = http.client.HTTPConnection("example.com", 80)
```

**基本写法：HTTPS 连接**
`http.client.HTTPSConnection(<主机>, <端口>)`
```python
# 创建 HTTPS 连接
import ssl

ctx = ssl.create_default_context()
conn = http.client.HTTPSConnection("www.python.org", 443, context=ctx)
```

**基本写法：发起请求**
`conn.request(<方法>, <路径>, <数据>, <头>)`
```python
# 发起 GET 请求
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status, resp.reason)
print(resp.read().decode()[:100])
```

**基本写法：POST 请求**
`conn.request("POST", <路径>, <数据>, <头>)`
```python
# 发起 POST 请求
import json
body = json.dumps({"name": "Alice"}).encode()
headers = {"Content-Type": "application/json"}
conn.request("POST", "/api/users", body, headers)
resp = conn.getresponse()
```

---

## HTTPResponse 响应对象

**基本写法：获取响应**
`conn.getresponse()`
```python
# 获取响应对象
resp = conn.getresponse()
```

**基本写法：状态码**
`resp.status` | `resp.reason`
```python
# 状态码与原因短语
print(resp.status)    # 200
print(resp.reason)    # OK
```

**基本写法：读取响应体**
`resp.read()` | `resp.read(<长度>)`
```python
# 读取全部或部分响应体
data = resp.read()
chunk = resp.read(1024)
```

**基本写法：获取响应头**
`resp.getheader(<名称>)` | `resp.getheaders()`
```python
# 获取响应头
print(resp.getheader("Content-Type"))
print(resp.getheaders())
```

**基本写法：流式读取**
`for line in resp:`
```python
# 逐行迭代响应体
for line in resp:
    print(line)
```

---

## 请求方法

**基本写法：PUT/DELETE/PATCH**
`conn.request(<方法>, <路径>)`
```python
# 各种 HTTP 方法
conn.request("PUT", "/item/1", body)
conn.request("DELETE", "/item/1")
conn.request("PATCH", "/item/1", body)
```

**基本写法：HEAD 请求**
`conn.request("HEAD", <路径>)`
```python
# HEAD 只获取头
conn.request("HEAD", "/")
resp = conn.getresponse()
print(resp.getheader("Content-Length"))
```

---

## 请求头

**基本写法：自定义请求头**
`conn.request(<方法>, <路径>, <数据>, <头字典>)`
```python
# 携带自定义头
headers = {
    "User-Agent": "MyClient/1.0",
    "Authorization": "Bearer token123",
}
conn.request("GET", "/", headers=headers)
```

**基本写法：添加 Cookie**
`headers["Cookie"] = <字符串>`
```python
# 携带 Cookie
headers = {"Cookie": "session=abc123"}
conn.request("GET", "/", headers=headers)
```

---

## 连接管理

**基本写法：关闭连接**
`conn.close()`
```python
# 关闭连接
conn.close()
```

**基本写法：set_tunnel 代理隧道**
`conn.set_tunnel(<代理主机>, <代理端口>)`
```python
# 通过代理建立隧道
conn = http.client.HTTPSConnection("example.com")
conn.set_tunnel("proxy.local", 8080)
conn.request("GET", "/")
```

**基本写法：connect 手动连接**
`conn.connect()`
```python
# 手动建立连接
conn.connect()
```

---

## 超时与异常

**基本写法：设置超时**
`HTTPConnection(<主机>, <端口>, timeout=<秒>)`
```python
# 连接超时
conn = http.client.HTTPConnection("example.com", timeout=10)
```

**基本写法：捕获异常**
`except http.client.HTTPException:`
```python
# http.client 异常基类
try:
    conn.request("GET", "/")
except http.client.HTTPException as e:
    print("HTTP 异常:", e)
except ConnectionError as e:
    print("连接错误:", e)
```

**基本写法：常见异常类型**
`http.client.HTTPException`
```python
# 异常层级
# HTTPException
#   ├── ProtocolError
#   ├── ResponseNotReady
#   ├── BadStatusLine
#   ├── ImproperConnectionState
#   └── CannotSendRequest
```

---

## HTTPMessage 消息对象

**基本写法：响应头为 email.message.Message**
`type(resp.headers)`
```python
# headers 是 email.message.Message 子类
print(type(resp.headers))
print(resp.headers["Content-Type"])
```

**基本写法：items 遍历头**
`resp.headers.items()`
```python
# 遍历所有头
for key, value in resp.headers.items():
    print(key, value)
```

---

## 持续连接与流水线

**基本写法：复用连接**
`conn.request(...)` 多次
```python
# 同一连接发多个请求
conn = http.client.HTTPConnection("example.com")
conn.request("GET", "/a")
r1 = conn.getresponse()
r1.read()
conn.request("GET", "/b")
r2 = conn.getresponse()
r2.read()
conn.close()
```



<!-- ============ 文档分隔线：040-python/049-UrllibModule.md ============ -->

# Python urllib 标准库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## urllib.request 请求

**基本写法：urlopen 打开 URL**
`urllib.request.urlopen(<URL>)`
```python
# 打开 URL 并读取
from urllib.request import urlopen

with urlopen("https://www.python.org") as resp:
    print(resp.read()[:100])
```

**基本写法：带超时**
`urlopen(<URL>, timeout=<秒>)`
```python
# 设置超时
with urlopen("https://www.python.org", timeout=10) as resp:
    print(resp.status)
```

**基本写法：Request 自定义请求**
`urllib.request.Request(<URL>, data=<数据>, headers=<头>)`
```python
# 自定义请求对象
from urllib.request import Request, urlopen

req = Request(
    "https://httpbin.org/post",
    data=b"key=value",
    headers={"User-Agent": "MyClient/1.0"},
    method="POST",
)
with urlopen(req) as resp:
    print(resp.read().decode()[:100])
```

**基本写法：携带 User-Agent**
`req.add_header(<键>, <值>)`
```python
# 添加请求头
req = Request("https://www.python.org")
req.add_header("User-Agent", "MyClient/1.0")
with urlopen(req) as resp:
    print(resp.status)
```

---

## urllib.parse URL 解析

**基本写法：urlparse 拆分 URL**
`urllib.parse.urlparse(<URL>)`
```python
# 拆分 URL 各部分
from urllib.parse import urlparse

r = urlparse("https://user:pass@host.com:8080/path?q=1#frag")
print(r.scheme, r.netloc, r.path, r.query, r.fragment)
```

**基本写法：urlunparse 组合**
`urllib.parse.urlunparse(<六元组>)`
```python
# 组合 URL
parts = ("https", "host.com", "/path", "", "q=1", "")
print(urlunparse(parts))
```

**基本写法：urljoin 拼接**
`urllib.parse.urljoin(<基础>, <相对>)`
```python
# 拼接基础与相对 URL
print(urljoin("https://host.com/a/b/", "../c"))
# https://host.com/a/c
```

**基本写法：urlencode 编码查询**
`urllib.parse.urlencode(<字典>)`
```python
# 字典转查询字符串
from urllib.parse import urlencode

print(urlencode({"name": "Alice", "age": 18}))
# name=Alice&age=18
```

**基本写法：urlencode 多值**
`urlencode(<字典>, doseq=True)`
```python
# 多值参数
print(urlencode({"tag": ["a", "b"]}, doseq=True))
# tag=a&tag=b
```

**基本写法：parse_qs 解析查询**
`urllib.parse.parse_qs(<查询串>)`
```python
# 解析查询字符串为字典
from urllib.parse import parse_qs

print(parse_qs("name=Alice&tag=a&tag=b"))
# {"name": ["Alice"], "tag": ["a", "b"]}
```

**基本写法：parse_qsl 列表形式**
`urllib.parse.parse_qsl(<查询串>)`
```python
# 解析为键值对列表
print(parse_qsl("name=Alice&age=18"))
# [("name", "Alice"), ("age", "18")]
```

**基本写法：quote URL 编码**
`urllib.parse.quote(<字符串>)`
```python
# 编码特殊字符
from urllib.parse import quote

print(quote("hello world&test"))
# hello%20world%26test
```

**基本写法：quote_plus 空格转加号**
`urllib.parse.quote_plus(<字符串>)`
```python
# 空格编码为 +
print(quote_plus("hello world"))
# hello+world
```

**基本写法：unquote 解码**
`urllib.parse.unquote(<字符串>)`
```python
# 解码 URL 编码
from urllib.parse import unquote

print(unquote("hello%20world"))
# hello world
```

**基本写法：urlsplit**
`urllib.parse.urlsplit(<URL>)`
```python
# 拆分为五元组（不拆 params）
r = urlsplit("https://host.com/path?q=1")
print(r)
```

---

## urllib.error 异常

**基本写法：URLError**
`except urllib.error.URLError:`
```python
# 捕获 URL 错误
from urllib.error import URLError, HTTPError

try:
    urlopen("https://invalid.invalid")
except URLError as e:
    print("URL 错误:", e.reason)
```

**基本写法：HTTPError**
`except urllib.error.HTTPError:`
```python
# 捕获 HTTP 错误（含状态码）
try:
    urlopen("https://httpbin.org/status/404")
except HTTPError as e:
    print(e.code, e.reason)
```

---

## urllib.request 高级

**基本写法：BaseHandler 与 Opener**
`urllib.request.build_opener(<处理器>)`
```python
# 自定义 opener
from urllib.request import build_opener, HTTPCookieProcessor, HTTPHandler

opener = build_opener(HTTPCookieProcessor(), HTTPHandler())
resp = opener.open("https://www.python.org")
```

**基本写法：HTTPBasicAuthHandler 认证**
`urllib.request.HTTPPasswordMgrWithDefaultRealm()`
```python
# HTTP 基本认证
import urllib.request

pwd_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
pwd_mgr.add_password(None, "https://host.com", "user", "pass")
auth = urllib.request.HTTPBasicAuthHandler(pwd_mgr)
opener = urllib.request.build_opener(auth)
resp = opener.open("https://host.com/protected")
```

**基本写法：ProxyHandler 代理**
`urllib.request.ProxyHandler(<代理字典>)`
```python
# 设置代理
proxy = urllib.request.ProxyHandler({"http": "http://proxy:8080"})
opener = urllib.request.build_opener(proxy)
```

**基本写法：HTTPCookieProcessor Cookie**
`http.cookiejar.CookieJar()`
```python
# 自动管理 Cookie
import http.cookiejar

jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
resp = opener.open("https://httpbin.org/cookies/set?name=Alice")
```

---

## 下载文件

**基本写法：urlretrieve 下载**
`urllib.request.urlretrieve(<URL>, <文件路径>)`
```python
# 下载到本地文件
from urllib.request import urlretrieve

filename, headers = urlretrieve("https://www.python.org/static/img/python-logo.png", "logo.png")
print(filename)
```



<!-- ============ 文档分隔线：040-python/050-Sqlite3.md ============ -->

# Python sqlite3 数据库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 连接数据库

**基本写法：连接数据库**
`sqlite3.connect(<数据库文件>)`
```python
# 连接 SQLite 数据库
import sqlite3

conn = sqlite3.connect("example.db")
# 内存数据库
conn_mem = sqlite3.connect(":memory:")
```

**基本写法：关闭连接**
`conn.close()`
```python
# 关闭连接
conn.close()
```

**基本写法：with 自动提交**
`with conn:`
```python
# with 块结束自动提交事务
with conn:
    conn.execute("INSERT INTO users VALUES (1, 'Alice')")
```

---

## 游标操作

**基本写法：创建游标**
`conn.cursor()`
```python
# 创建游标对象
cur = conn.cursor()
```

**基本写法：执行 SQL**
`cur.execute(<SQL>, <参数>)`
```python
# 执行单条 SQL（参数化查询）
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Alice"))
conn.commit()
```

**基本写法：批量执行**
`cur.executemany(<SQL>, <参数序列>)`
```python
# 批量插入
data = [(2, "Bob"), (3, "Carol")]
cur.executemany("INSERT INTO users (id, name) VALUES (?, ?)", data)
conn.commit()
```

**基本写法：执行脚本**
`cur.executescript(<SQL 脚本>)`
```python
# 执行多语句脚本
cur.executescript("""
CREATE TABLE IF NOT EXISTS logs (msg TEXT);
INSERT INTO logs VALUES ('init');
""")
```

---

## 查询结果

**基本写法：fetchone 取一条**
`cur.fetchone()`
```python
# 获取一条结果
cur.execute("SELECT * FROM users")
print(cur.fetchone())
```

**基本写法：fetchall 取全部**
`cur.fetchall()`
```python
# 获取全部结果
cur.execute("SELECT * FROM users")
print(cur.fetchall())
```

**基本写法：fetchmany 取多条**
`cur.fetchmany(<数量>)`
```python
# 获取指定数量结果
cur.execute("SELECT * FROM users")
print(cur.fetchmany(2))
```

**基本写法：迭代查询结果**
`for row in cur:`
```python
# 迭代结果
cur.execute("SELECT * FROM users")
for row in cur:
    print(row)
```

---

## Row 行工厂

**基本写法：Row 对象访问**
`conn.row_factory = sqlite3.Row`
```python
# 使用 Row 工厂按列名访问
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT * FROM users")
row = cur.fetchone()
print(row["name"], row["id"])
```

---

## 事务与隔离级别

**基本写法：设置隔离级别**
`sqlite3.connect(<文件>, isolation_level=<级别>)`
```python
# 隔离级别：None/DEFERRED/IMMEDIATE/EXCLUSIVE
conn = sqlite3.connect("example.db", isolation_level="DEFERRED")
```

**基本写法：手动提交**
`conn.commit()`
```python
# 提交事务
conn.commit()
```

**基本写法：回滚**
`conn.rollback()`
```python
# 回滚事务
conn.rollback()
```

---

## 参数化查询

**基本写法：问号占位符**
`cur.execute(<SQL>, (<参数1>, <参数2>))`
```python
# 使用 ? 占位符（推荐）
cur.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
```

**基本写法：命名占位符**
`cur.execute(<SQL>, {<名>: <值>})`
```python
# 使用 :name 命名占位符
cur.execute("SELECT * FROM users WHERE name = :name", {"name": "Alice"})
```

---

## 类型转换

**基本写法：注册适配器**
`sqlite3.register_adapter(<Python 类型>, <函数>)`
```python
# 自定义类型适配
import sqlite3
from datetime import date

sqlite3.register_adapter(date, lambda d: d.isoformat())
```

**基本写法：注册转换器**
`sqlite3.register_converter(<类型名>, <函数>)`
```python
# 自定义类型转换
sqlite3.register_converter("DATE", lambda b: date.fromisoformat(b.decode()))

conn = sqlite3.connect("db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute("CREATE TABLE events (d DATE)")
cur.execute("INSERT INTO events VALUES (?)", (date(2024, 1, 1),))
cur.execute("SELECT d FROM events")
print(type(cur.fetchone()[0]))  # <class 'datetime.date'>
```

---

## 上下文管理

**基本写法：连接作为上下文管理器**
`with conn:`
```python
# 自动提交或回滚
with conn:
    conn.execute("INSERT INTO users VALUES (1, 'Alice')")
```

**基本写法：游标作为上下文管理器**
`with conn.cursor() as cur:`
```python
# 自动关闭游标
with conn.cursor() as cur:
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
```

---

## 命令行接口（3.12+）

**基本写法：CLI 执行**
`python -m sqlite3 <数据库> <SQL>`
```python
# 命令行执行 SQL
# python -m sqlite3 example.db "SELECT * FROM users"
```

---

## 元数据查询

**基本写法：lastrowid**
`cur.lastrowid`
```python
# 获取最后插入行的 ID
cur.execute("INSERT INTO users (name) VALUES (?)", ("Dave",))
print(cur.lastrowid)
```

**基本写法：rowcount**
`cur.rowcount`
```python
# 获取影响的行数
cur.execute("DELETE FROM users WHERE id = ?", (1,))
print(cur.rowcount)
```

**基本写法：表结构**
`cur.execute("PRAGMA table_info(<表名>)")`
```python
# 查询表结构
cur.execute("PRAGMA table_info(users)")
for col in cur.fetchall():
    print(col)
```



<!-- ============ 文档分隔线：040-python/051-ZipfileTarfile.md ============ -->

# Python zipfile 与 tarfile

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## zipfile 读取

**基本写法：打开 ZIP**
`zipfile.ZipFile(<文件>, <模式>)`
```python
# 打开 zip 文件
import zipfile

with zipfile.ZipFile("archive.zip", "r") as zf:
    print(zf.namelist())
```

**基本写法：列出文件**
`zf.namelist()`
```python
# 列出 zip 内所有文件
with zipfile.ZipFile("archive.zip") as zf:
    for name in zf.namelist():
        print(name)
```

**基本写法：读取文件**
`zf.read(<文件名>)`
```python
# 读取 zip 内文件内容
with zipfile.ZipFile("archive.zip") as zf:
    data = zf.read("data.txt")
    print(data.decode())
```

**基本写法：提取文件**
`zf.extract(<文件名>, <目录>)`
```python
# 提取单个文件
with zipfile.ZipFile("archive.zip") as zf:
    zf.extract("data.txt", "output")
```

**基本写法：提取全部**
`zf.extractall(<目录>)`
```python
# 提取全部文件
with zipfile.ZipFile("archive.zip") as zf:
    zf.extractall("output")
```

---

## zipfile 写入

**基本写法：创建 ZIP**
`zipfile.ZipFile(<文件>, "w", <压缩>)`
```python
# 创建新 zip 文件
import zipfile

with zipfile.ZipFile("new.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("data.txt")
    zf.write("config.json")
```

**基本写法：追加文件**
`zipfile.ZipFile(<文件>, "a")`
```python
# 追加文件到已有 zip
with zipfile.ZipFile("new.zip", "a") as zf:
    zf.write("extra.txt")
```

**基本写法：writestr 写入字符串**
`zf.writestr(<文件名>, <数据>)`
```python
# 直接写入字符串/字节
with zipfile.ZipFile("new.zip", "w") as zf:
    zf.writestr("hello.txt", "Hello, World!")
    zf.writestr("data.json", '{"a": 1}')
```

---

## zipfile 信息

**基本写法：获取文件信息**
`zf.getinfo(<文件名>)`
```python
# 获取 ZipInfo 对象
with zipfile.ZipFile("archive.zip") as zf:
    info = zf.getinfo("data.txt")
    print(info.file_size, info.compress_size, info.date_time)
```

**基本写法：infolist 全部信息**
`zf.infolist()`
```python
# 获取所有文件信息
with zipfile.ZipFile("archive.zip") as zf:
    for info in zf.infolist():
        print(info.filename, info.file_size)
```

---

## ZIP 加密

**基本写法：密码解密**
`zf.setpassword(<密码>)`
```python
# 解密 zip
with zipfile.ZipFile("secret.zip") as zf:
    zf.setpassword(b"password")
    print(zf.read("data.txt"))
```

---

## tarfile 读取

**基本写法：打开 tar**
`tarfile.open(<文件>, <模式>)`
```python
# 打开 tar 文件
import tarfile

with tarfile.open("archive.tar.gz", "r:gz") as tf:
    print(tf.getnames())
```

**基本写法：列出成员**
`tf.getnames()` | `tf.getmembers()`
```python
# 列出 tar 内文件
with tarfile.open("archive.tar") as tf:
    for m in tf.getmembers():
        print(m.name, m.size, m.isfile())
```

**基本写法：提取文件**
`tf.extract(<成员>, <目录>)`
```python
# 提取单个文件
with tarfile.open("archive.tar") as tf:
    tf.extract("data.txt", "output")
```

**基本写法：提取全部**
`tf.extractall(<目录>)`
```python
# 提取全部
with tarfile.open("archive.tar") as tf:
    tf.extractall("output")
```

**基本写法：安全提取（3.12+）**
`tf.extractall(<目录>, filter="data")`
```python
# 3.12+ 推荐使用 filter 防止路径穿越
with tarfile.open("archive.tar") as tf:
    tf.extractall("output", filter="data")
```

---

## tarfile 写入

**基本写法：创建 tar**
`tarfile.open(<文件>, "w:<压缩>")`
```python
# 创建 tar.gz
with tarfile.open("new.tar.gz", "w:gz") as tf:
    tf.add("data.txt")
    tf.add("config.json")
```

**基本写法：添加文件**
`tf.add(<文件>, arcname=<归档名>)`
```python
# 指定归档内文件名
with tarfile.open("new.tar", "w") as tf:
    tf.add("data.txt", arcname="dir/data.txt")
```

**基本写法：addfile 写入**
`tf.addfile(<TarInfo>, <文件对象>)`
```python
# 手动构造 TarInfo 写入
import io

info = tarfile.TarInfo(name="hello.txt")
data = b"Hello, World!"
info.size = len(data)
with tarfile.open("new.tar", "w") as tf:
    tf.addfile(info, io.BytesIO(data))
```

---

## tarfile 模式

**基本写法：压缩模式**
`"w:gz"` | `"w:bz2"` | `"w:xz"`
```python
# 不同压缩格式
tarfile.open("a.tar.gz", "w:gz")
tarfile.open("a.tar.bz2", "w:bz2")
tarfile.open("a.tar.xz", "w:xz")
```

**基本写法：流式读取**
`"r|gz"`
```python
# 流式读取大文件
with tarfile.open("big.tar.gz", "r|gz") as tf:
    for member in tf:
        f = tf.extractfile(member)
        if f:
            print(f.read()[:50])
```

---

## TarInfo 对象

**基本写法：创建 TarInfo**
`tarfile.TarInfo(<名称>)`
```python
# 创建文件信息
info = tarfile.TarInfo("data.txt")
info.size = 100
info.mode = 0o644
```

**基本写法：从文件创建**
`tf.gettarinfo(<文件对象>)`
```python
# 从现有文件创建 TarInfo
with open("data.txt", "rb") as f:
    info = tf.gettarinfo(fileobj=f)
```



<!-- ============ 文档分隔线：040-python/052-Weakref.md ============ -->

# Python weakref 弱引用

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 弱引用基础

**基本写法：创建弱引用**
`weakref.ref(<对象>)`
```python
# 创建弱引用
import weakref

class Obj:
    pass

obj = Obj()
r = weakref.ref(obj)
print(r())        # 引用对象
print(r() is obj) # True
```

**基本写法：访问引用对象**
`r()`
```python
# 调用弱引用获取对象
obj_ref = r()
if obj_ref is not None:
    print("对象存在")
else:
    print("对象已回收")
```

**基本写法：对象回收后**
`del <对象>`
```python
# 删除强引用后弱引用返回 None
del obj
print(r())  # None
```

---

## WeakValueDictionary

**基本写法：值弱引用字典**
`weakref.WeakValueDictionary()`
```python
# 字典值为弱引用，对象可被回收
d = weakref.WeakValueDictionary()
o = Obj()
d["key"] = o
print(d["key"] is o)  # True
del o
print("key" in d)     # False，对象回收后自动移除
```

---

## WeakKeyDictionary

**基本写法：键弱引用字典**
`weakref.WeakKeyDictionary()`
```python
# 字典键为弱引用
d = weakref.WeakKeyDictionary()
o = Obj()
d[o] = "value"
print(d.get(o))  # value
del o
print(len(d))    # 0
```

---

## WeakSet

**基本写法：弱引用集合**
`weakref.WeakSet()`
```python
# 集合中元素为弱引用
s = weakref.WeakSet()
o = Obj()
s.add(o)
print(o in s)  # True
del o
print(len(s))  # 0
```

---

## finalize 终结回调

**基本写法：注册终结回调**
`weakref.finalize(<对象>, <函数>, *<参数>)`
```python
# 对象回收时调用回调
def cleanup(name):
    print(f"{name} 被回收")

o = Obj()
f = weakref.finalize(o, cleanup, "myobj")
del o  # 打印 "myobj 被回收"
```

**基本写法：取消终结**
`f.detach()`
```python
# 取消终结器
f = weakref.finalize(o, cleanup, "myobj")
f.detach()  # 取消回调
```

**基本写法：检查是否存活**
`f.alive`
```python
# 检查终结器是否仍存活
print(f.alive)
```

---

## WeakMethod 方法弱引用

**基本写法：方法弱引用**
`weakref.WeakMethod(<绑定方法>)`
```python
# 对绑定方法创建弱引用
class Service:
    def run(self):
        pass

s = Service()
m = weakref.WeakMethod(s.run)
print(m() is s.run)
```

---

## proxy 代理

**基本写法：创建代理**
`weakref.proxy(<对象>)`
```python
# 代理对象自动解引用
obj = Obj()
p = weakref.proxy(obj)
print(p is obj)  # False，但行为像 obj
del obj
# 访问 p 现在会抛出 ReferenceError
```

**基本写法：代理回调**
`weakref.proxy(<对象>, <回调>)`
```python
# 代理对象回收时回调
def on_unref(ref):
    print("代理对象被回收")

p = weakref.proxy(obj, on_unref)
```

---

## 支持弱引用的对象

**基本写法：检查是否支持弱引用**
`weakref.ref(<对象>)`
```python
# 内置类型如 list/dict 不支持弱引用
try:
    weakref.ref([1, 2, 3])
except TypeError as e:
    print(e)
```

**基本写法：子类化获得支持**
`class <类>(dict): __slots__ = ("__weakref__",)`
```python
# 通过 __slots__ 让对象支持弱引用
class MyDict(dict):
    __slots__ = ("__weakref__",)
```

---

## 应用场景

**基本写法：缓存弱引用**
`WeakValueDictionary`
```python
# 缓存大对象，不阻止回收
class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get(self, key, factory):
        obj = self._cache.get(key)
        if obj is None:
            obj = factory()
            self._cache[key] = obj
        return obj
```

**基本写法：观察者模式弱引用**
`WeakSet`
```python
# 观察者列表使用弱引用，避免内存泄漏
class Subject:
    def __init__(self):
        self._observers = weakref.WeakSet()
    def subscribe(self, obs):
        self._observers.add(obs)
    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)
```

---

## getweakrefcount

**基本写法：统计弱引用数**
`weakref.getweakrefcount(<对象>)`
```python
# 返回指向对象的弱引用数
print(weakref.getweakrefcount(obj))
```

**基本写法：获取所有弱引用**
`weakref.getweakrefs(<对象>)`
```python
# 返回所有弱引用列表
print(weakref.getweakrefs(obj))
```



<!-- ============ 文档分隔线：040-python/053-ArrayBisect.md ============ -->

# Python array 与 bisect

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：040-python/054-DataStructureAdvanced.md ============ -->

# Python 数据结构进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## deque 双端队列

**基本写法：创建 deque**
`collections.deque(<可迭代>, maxlen=<最大长度>)`
```python
# 创建双端队列
from collections import deque

d = deque([1, 2, 3])
d_bounded = deque(maxlen=5)  # 固定长度，溢出自动丢弃
```

**基本写法：两端追加**
`d.append(<值>)` | `d.appendleft(<值>)`
```python
# 右侧与左侧追加
d.append(4)
d.appendleft(0)
```

**基本写法：两端弹出**
`d.pop()` | `d.popleft()`
```python
# 两端弹出元素
print(d.pop())       # 4
print(d.popleft())   # 0
```

**基本写法：extend 批量追加**
`d.extend(<可迭代>)` | `d.extendleft(<可迭代>)`
```python
# 批量追加
d.extend([5, 6])
d.extendleft([-1, -2])  # 注意左侧追加顺序反转
```

**基本写法：rotate 旋转**
`d.rotate(<步数>)`
```python
# 正数右旋，负数左旋
d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # deque([4, 5, 1, 2, 3])
d.rotate(-1)  # deque([5, 1, 2, 3, 4])
```

**基本写法：固定长度滑动窗口**
`deque(maxlen=<大小>)`
```python
# 自动维护滑动窗口
window = deque(maxlen=3)
for i in range(5):
    window.append(i)
    print(window)  # 最后只剩 [2, 3, 4]
```

---

## heapq 堆队列

**基本写法：创建堆**
`heapq.heapify(<列表>)`
```python
# 原地转换为最小堆
import heapq

data = [3, 1, 4, 1, 5, 9]
heapq.heapify(data)
print(data[0])  # 1（最小值）
```

**基本写法：压入元素**
`heapq.heappush(<堆>, <值>)`
```python
# 维持堆性质压入
heapq.heappush(data, 0)
```

**基本写法：弹出最小**
`heapq.heappop(<堆>)`
```python
# 弹出堆顶最小值
print(heapq.heappop(data))
```

**基本写法：push 后 pop**
`heapq.heappushpop(<堆>, <值>)`
```python
# 压入后立即弹出，比分别调用更高效
print(heapq.heappushpop(data, 2))
```

**基本写法：pop 后 Push**
`heapq.heapreplace(<堆>, <值>)`
```python
# 先弹出再压入
print(heapq.heapreplace(data, 6))
```

**基本写法：nsmallest 取最小 N**
`heapq.nsmallest(<n>, <可迭代>, key=<函数>)`
```python
# 取最小的 N 个元素
print(heapq.nsmallest(3, [5, 1, 8, 2, 9]))
```

**基本写法：nlargest 取最大 N**
`heapq.nlargest(<n>, <可迭代>, key=<函数>)`
```python
# 取最大的 N 个元素
print(heapq.nlargest(3, [5, 1, 8, 2, 9]))
```

**基本写法：最大堆**
`heapq` 配合负值
```python
# Python heapq 只支持最小堆，用负值模拟最大堆
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  # 5
```

**基本写法：合并有序序列**
`heapq.merge(*<有序可迭代>)`
```python
# 合并多个有序序列
a = [1, 3, 5]
b = [2, 4, 6]
print(list(heapq.merge(a, b)))
```

**基本写法：自定义优先级**
`heapq` 配合元组
```python
# 元组比较实现优先队列
pq = []
heapq.heappush(pq, (1, "low"))
heapq.heappush(pq, (0, "high"))
print(heapq.heappop(pq))  # (0, "high")
```

---

## OrderedDict 有序字典

**基本写法：创建 OrderedDict**
`collections.OrderedDict()`
```python
# 有序字典（3.7+ 普通 dict 也保持插入顺序）
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
```

**基本写法：move_to_end 移动到末尾**
`od.move_to_end(<键>, last=<bool>)`
```python
# 移动元素到末尾或开头
od.move_to_end("a")           # 移到末尾
od.move_to_end("a", last=False)  # 移到开头
```

**基本写法：popitem 弹出**
`od.popitem(last=<bool>)`
```python
# 弹出末尾或开头元素
print(od.popitem())           # 弹出末尾
print(od.popitem(last=False)) # 弹出开头
```

**基本写法：按插入顺序迭代**
`for <键>, <值> in od.items():`
```python
# 迭代有序字典
for k, v in od.items():
    print(k, v)
```

**基本写法：LRU 缓存**
`OrderedDict` 实现 LRU
```python
# LRU 缓存实现
class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## ChainMap 链式字典

**基本写法：创建 ChainMap**
`collections.ChainMap(*<字典>)`
```python
# 链接多个字典，按顺序查找
from collections import ChainMap

defaults = {"host": "localhost", "port": 8080}
override = {"port": 9000}
config = ChainMap(override, defaults)
print(config["host"], config["port"])  # localhost 9000
```

**基本写法：新增映射**
`cm.new_child(<字典>)`
```python
# 添加新字典到链首
cm = config.new_child({"host": "remote"})
print(cm["host"])  # remote
```

**基本写法：parents 父链**
`cm.parents`
```python
# 返回除第一个之外的所有映射
print(config.parents)
```

**基本写法：写入只影响首映射**
`cm[<键>] = <值>`
```python
# 赋值只修改第一个字典
config["host"] = "changed"
print(override)  # {"port": 9000, "host": "changed"}
```

---

## UserDict 自定义字典

**基本写法：继承 UserDict**
`class <类>(collections.UserDict):`
```python
# UserDict 比继承 dict 更易自定义
import collections

class CaseInsensitiveDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    def __getitem__(self, key):
        return super().__getitem__(key.lower())
```



<!-- ============ 文档分隔线：040-python/055-StringText.md ============ -->

# Python 字符串与文本处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## string 模块

**基本写法：常量字符串**
`string.ascii_letters` | `string.digits`
```python
# 字符常量
import string

print(string.ascii_letters)  # a-zA-Z
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)         # 0-9
print(string.punctuation)    # 标点符号
```

**基本写法：Template 模板替换**
`string.Template(<模板>)`
```python
# 使用 $ 占位符的模板
from string import Template

t = Template("Hello, $name! You are $age.")
print(t.substitute(name="Alice", age=18))
```

**基本写法：safe_substitute 安全替换**
`t.safe_substitute(<字典>)`
```python
# 缺少占位符不报错
print(t.safe_substitute(name="Alice"))  # age 占位符保留
```

**基本写法：自定义分隔符**
`Template(<模板>, delimiter=<字符>)`
```python
# 自定义分隔符（如用 #）
class HashTemplate(Template):
    delimiter = "#"

t = HashTemplate("Hello, #name!")
print(t.substitute(name="Alice"))
```

---

## textwrap 文本换行

**基本写法：wrap 换行**
`textwrap.wrap(<文本>, width=<宽度>)`
```python
# 按指定宽度换行返回列表
import textwrap

lines = textwrap.wrap("Hello, World! This is a long text.", width=10)
print(lines)
```

**基本写法：fill 填充换行**
`textwrap.fill(<文本>, width=<宽度>)`
```python
# 返回换行后的字符串
print(textwrap.fill("Hello World!", width=5))
```

**基本写法：shorten 截断**
`textwrap.shorten(<文本>, width=<宽度>, placeholder=<占位>)`
```python
# 截断文本并添加占位符
print(textwrap.shorten("Hello World Hello Python", width=15, placeholder="..."))
```

**基本写法：dedent 去除缩进**
`textwrap.dedent(<文本>)`
```python
# 去除多行文本的公共缩进
text = """
    first
    second
    """
print(textwrap.dedent(text))
```

**基本写法：indent 添加缩进**
`textwrap.indent(<文本>, <前缀>)`
```python
# 给每行添加前缀
print(textwrap.indent("a\nb", "    "))
```

**基本写法：TextWrapper 对象**
`textwrap.TextWrapper(width=<宽度>)`
```python
# 复用配置
wrapper = textwrap.TextWrapper(width=70, initial_indent="> ", subsequent_indent="  ")
print(wrapper.fill("long text..."))
```

---

## unicodedata Unicode 数据

**基本写法：字符名称**
`unicodedata.name(<字符>)`
```python
# 获取 Unicode 字符名
import unicodedata

print(unicodedata.name("A"))  # LATIN CAPITAL LETTER A
print(unicodedata.name("中"))  # CJK UNIFIED IDEOGRAPH-4E2D
```

**基本写法：按名称查找字符**
`unicodedata.lookup(<名称>)`
```python
# 按名称查找字符
print(unicodedata.lookup("HEAVY BLACK HEART"))  # ❤
```

**基本写法：分类**
`unicodedata.category(<字符>)`
```python
# 获取 Unicode 分类
print(unicodedata.category("A"))  # Lu（大写字母）
print(unicodedata.category("1"))  # Nd（数字）
```

**基本写法：数值**
`unicodedata.decimal(<字符>)` | `unicodedata.numeric(<字符>)`
```python
# 获取字符数值
print(unicodedata.decimal("5"))  # 5
print(unicodedata.numeric("½"))  # 0.5
```

**基本写法：标准化**
`unicodedata.normalize(<形式>, <字符串>)`
```python
# Unicode 标准化
s = "café"
print(unicodedata.normalize("NFC", s))  # 组合形式
print(unicodedata.normalize("NFD", s))  # 分解形式
```

**基本写法：字符镜像**
`unicodedata.mirrored(<字符>)`
```python
# 是否为镜像字符
print(unicodedata.mirrored("("))  # 1
```

---

## codecs 编解码

**基本写法：获取编码器**
`codecs.lookup(<编码>)`
```python
# 查询编码信息
import codecs

enc = codecs.lookup("utf-8")
print(enc.name)
```

**基本写法：open 编码打开**
`codecs.open(<文件>, <模式>, <编码>)`
```python
# 指定编码打开文件
with codecs.open("file.txt", "r", "utf-8") as f:
    print(f.read())
```

**基本写法：编码与解码**
`codecs.encode(<字符串>, <编码>)` | `codecs.decode(<字节>, <编码>)`
```python
# 编码转换
b = codecs.encode("hello", "utf-8")
s = codecs.decode(b, "utf-8")
```

**基本写法：转码**
`codecs.encode(<字符串>, "rot_13")`
```python
# 特殊编码如 rot13
print(codecs.encode("hello", "rot_13"))
```

---

## 字符串方法扩展

**基本写法：str.translate 翻译表**
`str.maketrans(<字典>)`
```python
# 批量字符替换/删除
table = str.maketrans("aeiou", "12345")
print("hello".translate(table))  # h2ll4

# 删除字符
del_table = str.maketrans("", "", "aeiou")
print("hello".translate(del_table))  # hll
```

**基本写法：str.partition 分区**
`<字符串>.partition(<分隔符>)`
```python
# 三元组返回
print("a=b".partition("="))  # ("a", "=", "b")
```

**基本写法：str.format_map**
`<字符串>.format_map(<字典>)`
```python
# 用字典格式化
d = {"name": "Alice", "age": 18}
print("{name} is {age}".format_map(d))
```

---

## binascii 二进制文本

**基本写法：base64 编码**
`base64.b64encode(<字节>)`
```python
# Base64 编解码
import base64

print(base64.b64encode(b"hello"))
print(base64.b64decode(b"aGVsbG8="))
```

**基本写法：hex 编码**
`<字节>.hex()` | `bytes.fromhex(<字符串>)`
```python
# 十六进制编解码
print(b"hello".hex())
print(bytes.fromhex("68656c6c6f"))
```

**基本写法：URL 安全 base64**
`base64.urlsafe_b64encode(<字节>)`
```python
# URL 安全的 base64
print(base64.urlsafe_b64encode(b"ab?cd"))
```



<!-- ============ 文档分隔线：040-python/056-DecimalFractions.md ============ -->

# Python decimal 与 fractions

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：040-python/057-ShutilTempfile.md ============ -->

# Python shutil 与 tempfile

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## shutil 文件操作

**基本写法：复制文件**
`shutil.copy(<源>, <目标>)`
```python
# 复制文件（保留权限）
import shutil

shutil.copy("src.txt", "dst.txt")
shutil.copy2("src.txt", "dst.txt")  # 保留元数据
```

**基本写法：复制文件内容**
`shutil.copyfile(<源>, <目标>)`
```python
# 仅复制内容，不保留权限
shutil.copyfile("src.txt", "dst.txt")
```

**基本写法：复制目录树**
`shutil.copytree(<源目录>, <目标目录>)`
```python
# 递归复制目录
shutil.copytree("src_dir", "dst_dir")
```

**基本写法：复制目录（忽略）**
`shutil.copytree(<源>, <目标>, ignore=shutil.ignore_patterns(*<模式>))`
```python
# 复制时忽略指定模式
shutil.copytree("src", "dst", ignore=shutil.ignore_patterns("*.tmp", "*.log"))
```

**基本写法：删除目录树**
`shutil.rmtree(<目录>)`
```python
# 递归删除目录
shutil.rmtree("dst_dir")
```

**基本写法：移动文件**
`shutil.move(<源>, <目标>)`
```python
# 移动文件或目录
shutil.move("src.txt", "subdir/dst.txt")
```

---

## shutil 元数据与权限

**基本写法：复制模式**
`shutil.copymode(<源>, <目标>)`
```python
# 仅复制权限位
shutil.copymode("src.txt", "dst.txt")
```

**基本写法：复制元数据**
`shutil.copystat(<源>, <目标>)`
```python
# 复制权限、时间、扩展属性
shutil.copystat("src.txt", "dst.txt")
```

**基本写法：chown 改属主**
`shutil.chown(<路径>, user=<用户>, group=<组>)`
```python
# 修改所有者（Unix）
shutil.chown("file", user="alice", group="staff")
```

---

## shutil 压缩归档

**基本写法：创建归档**
`shutil.make_archive(<基础名>, <格式>, <根目录>)`
```python
# 创建 zip/tar 归档
shutil.make_archive("backup", "zip", "src_dir")
shutil.make_archive("backup", "gztar", "src_dir")
```

**基本写法：解包归档**
`shutil.unpack_archive(<文件>, <目录>)`
```python
# 解压归档
shutil.unpack_archive("backup.zip", "output")
```

**基本写法：查看支持的格式**
`shutil.get_archive_formats()`
```python
# 列出支持的归档格式
print(shutil.get_archive_formats())
```

---

## shutil 磁盘信息

**基本写法：磁盘使用情况**
`shutil.disk_usage(<路径>)`
```python
# 获取磁盘使用情况
usage = shutil.disk_usage("/")
print(usage.total, usage.used, usage.free)
```

**基本写法：获取终端大小**
`shutil.get_terminal_size()`
```python
# 获取终端列数行数
size = shutil.get_terminal_size()
print(size.columns, size.lines)
```

**基本写法：which 查找可执行文件**
`shutil.which(<命令>)`
```python
# 查找命令路径
print(shutil.which("python"))
```

---

## tempfile 临时文件

**基本写法：临时文件**
`tempfile.TemporaryFile()`
```python
# 创建临时文件，关闭自动删除
import tempfile

with tempfile.TemporaryFile() as f:
    f.write(b"hello")
    f.seek(0)
    print(f.read())
```

**基本写法：命名临时文件**
`tempfile.NamedTemporaryFile()`
```python
# 可访问文件名的临时文件
with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
    f.write(b"hello")
    print(f.name)
```

**基本写法：临时目录**
`tempfile.TemporaryDirectory()`
```python
# 临时目录，退出自动删除
with tempfile.TemporaryDirectory() as d:
    print(d)
    # 在 d 下创建文件
```

**基本写法：mkstemp 创建临时文件**
`tempfile.mkstemp(suffix=<后缀>, prefix=<前缀>, dir=<目录>)`
```python
# 低层创建，返回 fd 与路径
fd, path = tempfile.mkstemp(suffix=".log")
os.close(fd)
```

**基本写法：mkdtemp 创建临时目录**
`tempfile.mkdtemp(prefix=<前缀>)`
```python
# 创建临时目录（需手动删除）
d = tempfile.mkdtemp(prefix="myapp_")
```

**基本写法：gettempdir 临时目录**
`tempfile.gettempdir()`
```python
# 获取系统临时目录
print(tempfile.gettempdir())
```

**基本写法：gettempdirb 字节路径**
`tempfile.gettempdirb()`
```python
# 字节形式临时目录
print(tempfile.gettempdirb())
```

---

## fileinput 文件输入

**基本写法：迭代多文件**
`fileinput.input(<文件列表>)`
```python
# 串联读取多个文件
import fileinput

for line in fileinput.input(["a.txt", "b.txt"]):
    print(fileinput.filename(), fileinput.lineno(), line.rstrip())
```

**基本写法：原地编辑**
`fileinput.input(<文件>, inplace=True)`
```python
# 原地修改文件（stdout 重定向到文件）
for line in fileinput.input("data.txt", inplace=True):
    print(line.rstrip().upper())
```

**基本写法：备份数据**
`fileinput.input(<文件>, backup=".bak")`
```python
# 编辑前创建备份
for line in fileinput.input("data.txt", backup=".bak", inplace=True):
    print(line.rstrip())
```

**基本写法：files 与 filelineno**
`fileinput.filename()` | `fileinput.filelineno()`
```python
# 当前文件名与文件内行号
for line in fileinput.input(["a.txt", "b.txt"]):
    print(fileinput.filename(), fileinput.filelineno())
```

**基本写法：isfirstline 判断首行**
`fileinput.isfirstline()`
```python
# 判断是否为当前文件首行
for line in fileinput.input(files):
    if fileinput.isfirstline():
        print("新文件:", fileinput.filename())
```

---

## fnmatch 文件名匹配

**基本写法：匹配文件名**
`fnmatch.fnmatch(<文件名>, <模式>)`
```python
# shell 风格通配符匹配
import fnmatch

print(fnmatch.fnmatch("data.txt", "*.txt"))
print(fnmatch.fnmatch("file.PY", "*.py"))  # 大小写不敏感（Windows）
```

**基本写法：大小写敏感**
`fnmatch.fnmatchcase(<文件名>, <模式>)`
```python
# 严格大小写匹配
print(fnmatch.fnmatchcase("file.PY", "*.py"))  # False
```

**基本写法：filter 过滤**
`fnmatch.filter(<名称列表>, <模式>)`
```python
# 过滤匹配的名称
files = ["a.txt", "b.py", "c.txt"]
print(fnmatch.filter(files, "*.txt"))
```

**基本写法：translate 转正则**
`fnmatch.translate(<模式>)`
```python
# 通配符转正则表达式
print(fnmatch.translate("*.txt"))
```



<!-- ============ 文档分隔线：040-python/058-GcInspect.md ============ -->

# Python gc inspect dis

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## gc 垃圾回收

**基本写法：手动回收**
`gc.collect()`
```python
# 触发垃圾回收
import gc

print(gc.collect())  # 返回回收对象数
```

**基本写法：分代回收**
`gc.collect(<代>)`
```python
# 只回收指定代（0/1/2）
gc.collect(0)
```

**基本写法：获取对象引用**
`gc.get_referrers(<对象>)`
```python
# 获取引用指定对象的对象
class Obj: pass
o = Obj()
lst = [o]
print(gc.get_referrers(o))
```

**基本写法：获取引用对象**
`gc.get_referents(<对象>)`
```python
# 获取对象引用的对象
print(gc.get_referents(lst))
```

**基本写法：获取阈值**
`gc.get_threshold()`
```python
# 获取分代回收阈值
print(gc.get_threshold())  # (700, 10, 10)
```

**基本写法：设置阈值**
`gc.set_threshold(<阈值0>, <阈值1>, <阈值2>)`
```python
# 调整回收阈值
gc.set_threshold(1000, 15, 15)
```

**基本写法：禁用/启用**
`gc.disable()` | `gc.enable()`
```python
# 禁用自动 GC
gc.disable()
gc.enable()
```

**基本写法：调试标志**
`gc.set_debug(<标志>)`
```python
# 设置调试输出
gc.set_debug(gc.DEBUG_LEAK)
```

**基本写法：跟踪对象**
`gc.callbacks.append(<回调>)`
```python
# 注册 GC 回调
def on_gc(phase, info):
    print(phase, info)
gc.callbacks.append(on_gc)
```

**基本写法：循环引用检测**
`gc.garbage`
```python
# 有 __del__ 的循环引用对象列表
print(gc.garbage)
```

---

## inspect 检查

**基本写法：获取源码**
`inspect.getsource(<对象>)`
```python
# 获取函数/类的源代码
import inspect

def foo():
    pass

print(inspect.getsource(foo))
```

**基本写法：获取文件**
`inspect.getfile(<对象>)`
```python
# 获取对象定义所在文件
print(inspect.getfile(foo))
```

**基本写法：获取模块**
`inspect.getmodule(<对象>)`
```python
# 获取对象所属模块
print(inspect.getmodule(foo))
```

**基本写法：签名信息**
`inspect.signature(<函数>)`
```python
# 获取函数签名
def add(a, b=10):
    return a + b

sig = inspect.signature(add)
print(sig.parameters)
```

**基本写法：参数详情**
`inspect.Parameter`
```python
# 检查参数
for name, p in sig.parameters.items():
    print(name, p.kind, p.default)
```

**基本写法：是否为函数/类**
`inspect.isfunction(<对象>)` | `inspect.isclass(<对象>)`
```python
# 类型判断
print(inspect.isfunction(foo))
print(inspect.isclass(int))
```

**基本写法：成员列表**
`inspect.getmembers(<对象>, <谓词>)`
```python
# 获取对象成员
class A:
    def method(self): pass

for name, member in inspect.getmembers(A, inspect.isfunction):
    print(name)
```

**基本写法：获取类层级**
`inspect.getmro(<类>)`
```python
# 获取方法解析顺序
print(inspect.getmro(int))
```

**基本写法：获取调用栈**
`inspect.stack()`
```python
# 获取调用栈帧
def outer():
    inner()

def inner():
    for frame in inspect.stack():
        print(frame.function)

outer()
```

**基本写法：当前帧**
`inspect.currentframe()`
```python
# 获取当前帧
frame = inspect.currentframe()
print(frame.f_code.co_name)
```

---

## dis 字节码反汇编

**基本写法：反汇编函数**
`dis.dis(<函数>)`
```python
# 反汇编为字节码
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

**基本写法：反汇编字符串代码**
`dis.dis(<代码字符串>)`
```python
# 反汇编代码字符串
dis.dis("a + b")
```

**基本写法：获取字节码**
`dis.Bytecode(<函数>)`
```python
# 获取 Bytecode 对象迭代
for instr in dis.Bytecode(add):
    print(instr.opname, instr.argval)
```

**基本写法：查看常量**
`dis.code_info(<函数>)`
```python
# 获取代码对象信息
print(dis.code_info(add))
```

**基本写法：show_code**
`dis.show_code(<函数>)`
```python
# 打印代码对象信息
dis.show_code(add)
```

---

## ast 抽象语法树

**基本写法：解析代码**
`ast.parse(<代码字符串>)`
```python
# 解析为 AST
import ast

tree = ast.parse("x = 1 + 2")
print(ast.dump(tree))
```

**基本写法：遍历节点**
`ast.walk(<树>)`
```python
# 遍历所有节点
for node in ast.walk(tree):
    print(type(node).__name__)
```

**基本写法：NodeVisitor 访问**
`class <类>(ast.NodeVisitor):\n    def visit_<节点>(self, node):`
```python
# 自定义访问器
class Counter(ast.NodeVisitor):
    def __init__(self):
        self.count = 0
    def visit_Call(self, node):
        self.count += 1
        self.generic_visit(node)

c = Counter()
c.visit(ast.parse("a(); b()"))
print(c.count)
```

**基本写法：NodeTransformer 修改**
`class <类>(ast.NodeTransformer):`
```python
# 修改 AST 节点
class Double(ast.NodeTransformer):
    def visit_Num(self, node):
        return ast.copy_location(ast.Num(n=node.n * 2), node)
```

**基本写法：unparse 反向生成**
`ast.unparse(<树>)`
```python
# AST 转回代码字符串（3.9+）
print(ast.unparse(tree))
```

**基本写法：literal_eval 安全求值**
`ast.literal_eval(<字符串>)`
```python
# 安全求值字面值
print(ast.literal_eval("[1, 2, 3]"))
print(ast.literal_eval("{'a': 1}"))
```

---

## sys.intern 字符串驻留

**基本写法：字符串驻留**
`sys.intern(<字符串>)`
```python
# 字符串驻留，节省内存
import sys

a = sys.intern("hello")
b = sys.intern("hello")
print(a is b)  # True
```

---

## sys.getsizeof 对象大小

**基本写法：获取对象大小**
`sys.getsizeof(<对象>)`
```python
# 获取对象字节大小
print(sys.getsizeof([1, 2, 3]))
print(sys.getsizeof("hello"))
```

**基本写法：递归大小**
`sys.getsizeof(<对象>, <默认>)`
```python
# 配合递归计算容器总大小
def total_size(obj):
    seen = set()
    def inner(o):
        if id(o) in seen:
            return 0
        seen.add(id(o))
        s = sys.getsizeof(o)
        if isinstance(o, (list, tuple, set)):
            s += sum(inner(i) for i in o)
        return s
    return inner(obj)
```



<!-- ============ 文档分隔线：040-python/059-TracebackWarnings.md ============ -->

# Python traceback 与 warnings

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## traceback 打印异常

**基本写法：打印当前异常**
`traceback.print_exc()`
```python
# 打印当前异常栈到 stderr
import traceback

try:
    1 / 0
except Exception:
    traceback.print_exc()
```

**基本写法：格式化异常字符串**
`traceback.format_exc()`
```python
# 获取异常栈字符串
try:
    1 / 0
except Exception:
    msg = traceback.format_exc()
    print(msg)
```

**基本写法：打印指定异常**
`traceback.print_exception(<异常>)`
```python
# 打印指定异常对象
try:
    raise ValueError("test")
except ValueError as e:
    traceback.print_exception(e)
```

**基本写法：格式化指定异常**
`traceback.format_exception(<异常>)`
```python
# 返回异常信息行列表
try:
    raise ValueError("test")
except ValueError as e:
    lines = traceback.format_exception(e)
    print("".join(lines))
```

---

## traceback 提取栈帧

**基本写法：提取当前栈**
`traceback.extract_stack()`
```python
# 获取当前调用栈帧列表
frames = traceback.extract_stack()
for f in frames:
    print(f.filename, f.lineno, f.name)
```

**基本写法：提取指定栈**
`traceback.extract_tb(<tb>)`
```python
# 从 traceback 对象提取帧
try:
    1 / 0
except ZeroDivisionError as e:
    frames = traceback.extract_tb(e.__traceback__)
    for f in frames:
        print(f.filename, f.lineno, f.name, f.line)
```

**基本写法：StackSummary 对象**
`traceback.StackSummary.extract(<帧>)`
```python
# 3.5+ StackSummary 对象
summary = traceback.StackSummary.extract(traceback.walk_stack(None))
print(summary.format())
```

**基本写法：format_list 格式化帧**
`traceback.format_list(<帧列表>)`
```python
# 格式化帧列表
frames = traceback.extract_stack()
print("".join(traceback.format_list(frames)))
```

---

## traceback 装饰器

**基本写法：异常装饰器**
`def <装饰器>(func):\n    @functools.wraps(func)\n    def wrapper(*a, **k):`
```python
# 捕获异常并记录完整 traceback
import functools
import traceback
import logging

def log_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logging.error(traceback.format_exc())
            raise
    return wrapper
```

---

## warnings 警告控制

**基本写法：发出警告**
`warnings.warn(<消息>, <警告类>)`
```python
# 发出警告
import warnings

def deprecated_func():
    warnings.warn("该函数已弃用", DeprecationWarning)
    return "old"
```

**基本写法：警告类别**
`UserWarning` | `DeprecationWarning` | `RuntimeWarning`
```python
# 常用警告类别
warnings.warn("用户警告", UserWarning)
warnings.warn("弃用警告", DeprecationWarning)
warnings.warn("运行时警告", RuntimeWarning)
warnings.warn("资源警告", ResourceWarning)
```

**基本写法：过滤警告**
`warnings.filterwarnings(<动作>, <消息正则>, <类别>)`
```python
# 过滤警告
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("error", category=UserWarning)
```

**基本写法：simplefilter 简化过滤**
`warnings.simplefilter(<动作>, <类别>)`
```python
# 简化过滤
warnings.simplefilter("ignore")
warnings.simplefilter("always", UserWarning)
```

**基本写法：动作选项**
`"error"` | `"ignore"` | `"always"` | `"default"` | `"module"` | `"once"`
```python
# 警告动作
warnings.simplefilter("error")   # 警告转异常
warnings.simplefilter("ignore")  # 忽略
warnings.simplefilter("always")  # 总是显示
```

---

## warnings 上下文管理

**基本写法：catch_warnings 临时过滤**
`with warnings.catch_warnings():`
```python
# 临时修改警告过滤
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    deprecated_func()
```

**基本写法：捕获警告记录**
`with warnings.catch_warnings(record=True) as w:`
```python
# 捕获警告到列表
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    deprecated_func()
    for warning in w:
        print(warning.category.__name__, warning.message)
```

**基本写法：指定模块过滤**
`warnings.filterwarnings(<动作>, module=<模块正则>)`
```python
# 仅对特定模块过滤
warnings.filterwarnings("ignore", module="legacy_lib.*")
```

---

## warnings 子类化

**基本写法：自定义警告类**
`class <警告类>(Warning):`
```python
# 自定义警告类别
class ConfigWarning(UserWarning):
    pass

warnings.warn("配置问题", ConfigWarning)
```

**基本写法：deprecated 装饰器（3.13+）**
`@warnings.deprecated(<消息>)`
```python
# Python 3.13 内置弃用装饰器
@warnings.deprecated("使用 new_func 替代")
def old_func():
    pass
```

---

## 命令行控制警告

**基本写法：命令行参数**
`python -W <动作>:<消息>:<类别>:<模块>:<行号>`
```python
# 命令行控制警告
# python -W ignore::DeprecationWarning main.py
# python -W error::UserWarning main.py
```

**基本写法：环境变量**
`PYTHONWARNINGS=<过滤>`
```python
# 通过环境变量设置
# set PYTHONWARNINGS=ignore::DeprecationWarning
```

---

## sys 异常信息

**基本写法：sys.exc_info**
`sys.exc_info()`
```python
# 获取当前异常信息三元组
import sys

try:
    1 / 0
except ZeroDivisionError:
    exc_type, exc, tb = sys.exc_info()
    print(exc_type, exc)
```

**基本写法：异常链**
`raise <异常> from <原异常>`
```python
# 异常链
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("处理失败") from e
```

**基本写法：suppress 上下文**
`raise <异常> from None`
```python
# 抑制异常上下文
raise RuntimeError("独立错误") from None
```

**基本写法：__cause__ 与 __context__**
`exc.__cause__` | `exc.__context__`
```python
# 访问异常链
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise RuntimeError("wrap") from e
except RuntimeError as e:
    print(e.__cause__)
```



<!-- ============ 文档分隔线：040-python/060-ThreadingSync.md ============ -->

# Python threading 同步原语

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Lock 互斥锁

**基本写法：创建锁**
`threading.Lock()`
```python
# 互斥锁
import threading

lock = threading.Lock()
```

**基本写法：acquire 与 release**
`lock.acquire()` | `lock.release()`
```python
# 手动加锁解锁
lock.acquire()
try:
    pass
finally:
    lock.release()
```

**基本写法：with 自动管理**
`with lock:`
```python
# 推荐：with 自动加锁解锁
with lock:
    pass
```

**基本写法：非阻塞获取**
`lock.acquire(blocking=False)`
```python
# 非阻塞尝试获取
if lock.acquire(blocking=False):
    try:
        pass
    finally:
        lock.release()
else:
    print("锁被占用")
```

**基本写法：带超时获取**
`lock.acquire(timeout=<秒>)`
```python
# 超时获取
if lock.acquire(timeout=5):
    try:
        pass
    finally:
        lock.release()
```

---

## RLock 可重入锁

**基本写法：创建 RLock**
`threading.RLock()`
```python
# 同一线程可多次获取
rlock = threading.RLock()

def recursive(n):
    with rlock:
        if n > 0:
            recursive(n - 1)
```

---

## Condition 条件变量

**基本写法：创建 Condition**
`threading.Condition(<锁>)`
```python
# 条件变量
cond = threading.Condition()
```

**基本写法：wait 等待**
`with cond:\n    cond.wait()`
```python
# 等待条件满足
with cond:
    cond.wait()
```

**基本写法：notify 通知**
`cond.notify(<数量>)` | `cond.notify_all()`
```python
# 通知等待线程
with cond:
    cond.notify()
    cond.notify_all()
```

**基本写法：生产者消费者**
`Condition` 配合 wait/notify
```python
queue = []
MAX = 5
cond = threading.Condition()

def producer():
    with cond:
        while len(queue) >= MAX:
            cond.wait()
        queue.append("item")
        cond.notify_all()

def consumer():
    with cond:
        while not queue:
            cond.wait()
        item = queue.pop(0)
        cond.notify_all()
```

**基本写法：wait_for 条件谓词**
`cond.wait_for(<谓词函数>, timeout=<秒>)`
```python
# 等待条件成立
with cond:
    cond.wait_for(lambda: len(queue) > 0)
    item = queue.pop(0)
```

---

## Event 事件

**基本写法：创建 Event**
`threading.Event()`
```python
# 事件标志
event = threading.Event()
```

**基本写法：set 与 clear**
`event.set()` | `event.clear()`
```python
# 设置与清除标志
event.set()
event.clear()
```

**基本写法：wait 等待**
`event.wait(timeout=<秒>)`
```python
# 等待事件被 set
event.wait()
event.wait(timeout=5)
```

**基本写法：is_set 检查**
`event.is_set()`
```python
# 检查标志状态
print(event.is_set())
```

---

## Semaphore 信号量

**基本写法：创建信号量**
`threading.Semaphore(<数量>)`
```python
# 限制并发数
sem = threading.Semaphore(3)

def worker():
    with sem:
        pass
```

**基本写法：BoundedSemaphore**
`threading.BoundedSemaphore(<数量>)`
```python
# 有界信号量
sem = threading.BoundedSemaphore(3)
```

---

## Barrier 栅栏

**基本写法：创建 Barrier**
`threading.Barrier(<数量>)`
```python
# 等待指定数量线程到达后一起继续
barrier = threading.Barrier(4)

def worker():
    barrier.wait()
```

**基本写法：带超时**
`barrier.wait(timeout=<秒>)`
```python
# 超时则抛出 BrokenBarrierError
barrier.wait(timeout=10)
```

**基本写法：abort 中断**
`barrier.abort()`
```python
# 中断栅栏
barrier.abort()
```

---

## local 线程局部存储

**基本写法：创建 local**
`threading.local()`
```python
# 线程局部数据
local_data = threading.local()
local_data.value = 0
```

---

## GIL 与自由线程

**基本写法：Python GIL**
`threading` 适用于 IO 密集型
```python
# GIL 限制：同一时刻只有一个线程执行 Python 字节码
# CPU 密集型任务请用 multiprocessing
```

**基本写法：3.13 自由线程模式**
`python -X gil=0`
```python
# Python 3.13 实验性无 GIL 模式（PEP 703）
# python -X gil=0 main.py
```

---

## 线程枚举

**基本写法：活跃线程数**
`threading.active_count()`
```python
# 当前活跃线程数
print(threading.active_count())
```

**基本写法：枚举线程**
`threading.enumerate()`
```python
# 获取所有活跃线程列表
for t in threading.enumerate():
    print(t.name)
```

**基本写法：主线程**
`threading.main_thread()`
```python
# 获取主线程对象
print(threading.main_thread().name)
```

---

## Timer 定时线程

**基本写法：创建 Timer**
`threading.Timer(<秒>, <函数>)`
```python
# 定时执行函数
def hello():
    print("hello")

t = threading.Timer(5.0, hello)
t.start()
```

**基本写法：取消 Timer**
`t.cancel()`
```python
# 取消未执行的定时器
t.cancel()
```

---

## 线程间通信 queue

**基本写法：Queue**
`queue.Queue(<最大长度>)`
```python
# 线程安全队列
import queue

q = queue.Queue(maxsize=10)
q.put("item")
print(q.get())
```

**基本写法：非阻塞操作**
`q.put(<值>, block=False)` | `q.get(block=False)`
```python
# 非阻塞
try:
    q.put("x", block=False)
except queue.Full:
    pass

try:
    q.get(block=False)
except queue.Empty:
    pass
```

**基本写法：LifoQueue 与 PriorityQueue**
`queue.LifoQueue()` | `queue.PriorityQueue()`
```python
# 后进先出与优先队列
lifo = queue.LifoQueue()
pq = queue.PriorityQueue()
pq.put((1, "high"))
pq.put((3, "low"))
```

**基本写法：task_done 与 join**
`q.task_done()` | `q.join()`
```python
# 任务完成标记与等待全部处理
q.put("task1")
q.get()
q.task_done()
q.join()
```

**基本写法：SimpleQueue（3.7+）**
`queue.SimpleQueue()`
```python
# 无界的简单队列，性能更好
sq = queue.SimpleQueue()
sq.put("x")
print(sq.get())
```



<!-- ============ 文档分隔线：040-python/061-AsyncioAdvanced.md ============ -->

# Python asyncio 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Task 任务

**基本写法：创建 Task**
`asyncio.create_task(<协程>)`
```python
# 调度协程为 Task
import asyncio

async def fetch(url):
    await asyncio.sleep(1)
    return f"data from {url}"

async def main():
    task = asyncio.create_task(fetch("https://x"))
    result = await task
    print(result)

asyncio.run(main())
```

**基本写法：TaskGroup（3.11+）**
`async with asyncio.TaskGroup() as tg:`
```python
# 结构化并发
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(fetch("a"))
        t2 = tg.create_task(fetch("b"))
    print(t1.result(), t2.result())
```

**基本写法：gather 并发**
`asyncio.gather(*<协程>)`
```python
# 并发运行多个协程
async def main():
    results = await asyncio.gather(
        fetch("a"), fetch("b"), fetch("c")
    )
    print(results)
```

**基本写法：gather 异常处理**
`asyncio.gather(*<协程>, return_exceptions=True)`
```python
# 异常作为结果返回
results = await asyncio.gather(
    fetch("a"), fetch("b"), return_exceptions=True
)
for r in results:
    if isinstance(r, Exception):
        print("错误:", r)
```

---

## wait 等待

**基本写法：wait 等待**
`asyncio.wait(<Task 集合>)`
```python
# 等待任务完成
tasks = [asyncio.create_task(fetch(i)) for i in range(3)]
done, pending = await asyncio.wait(tasks)
```

**基本写法：指定 return_when**
`asyncio.wait(<集合>, return_when=<常量>)`
```python
# 首个完成即返回
from asyncio import FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED

done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)
```

**基本写法：wait_for 超时**
`asyncio.wait_for(<协程>, timeout=<秒>)`
```python
# 等待协程完成，超时取消
try:
    result = await asyncio.wait_for(fetch("a"), timeout=2.0)
except asyncio.TimeoutError:
    print("超时")
```

**基本写法：as_completed 按完成迭代**
`asyncio.as_completed(<协程列表>)`
```python
# 按完成顺序迭代
coros = [fetch(i) for i in range(3)]
for coro in asyncio.as_completed(coros):
    result = await coro
    print(result)
```

---

## Queue 队列

**基本写法：asyncio.Queue**
`asyncio.Queue(maxsize=<大小>)`
```python
# 异步队列
q = asyncio.Queue(maxsize=10)

async def producer():
    await q.put("item")

async def consumer():
    item = await q.get()
    q.task_done()
```

**基本写法：get 与 put**
`await q.put(<值>)` | `await q.get()`
```python
# 异步入队出队
await q.put("x")
item = await q.get()
```

**基本写法：join 等待全部处理**
`await q.join()`
```python
# 等待所有 item 被 task_done
await q.join()
```

**基本写法：PriorityQueue 与 LifoQueue**
`asyncio.PriorityQueue()` | `asyncio.LifoQueue()`
```python
# 优先队列与栈
pq = asyncio.PriorityQueue()
pq.put_nowait((1, "high"))
```

---

## Lock 锁

**基本写法：asyncio.Lock**
`asyncio.Lock()`
```python
# 异步锁
lock = asyncio.Lock()

async def safe_update():
    async with lock:
        pass
```

**基本写法：acquire 与 release**
`await lock.acquire()` | `lock.release()`
```python
# 手动加锁
await lock.acquire()
try:
    pass
finally:
    lock.release()
```

---

## Event 与 Condition

**基本写法：asyncio.Event**
`asyncio.Event()`
```python
# 异步事件
event = asyncio.Event()

async def waiter():
    await event.wait()

async def setter():
    event.set()
```

**基本写法：asyncio.Condition**
`asyncio.Condition()`
```python
# 异步条件变量
cond = asyncio.Condition()

async def consumer():
    async with cond:
        await cond.wait_for(lambda: data_ready)
```

---

## Semaphore 信号量

**基本写法：asyncio.Semaphore**
`asyncio.Semaphore(<数量>)`
```python
# 限制并发数
sem = asyncio.Semaphore(5)

async def fetch_limited(url):
    async with sem:
        return await fetch(url)
```

**基本写法：BoundedSemaphore**
`asyncio.BoundedSemaphore(<数量>)`
```python
# 有界信号量
sem = asyncio.BoundedSemaphore(3)
```

---

## Stream 流

**基本写法：open_connection 客户端**
`asyncio.open_connection(<主机>, <端口>)`
```python
# 异步 TCP 客户端
async def tcp_client():
    reader, writer = await asyncio.open_connection("example.com", 80)
    writer.write(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    data = await reader.read(1024)
    writer.close()
    await writer.wait_closed()
```

**基本写法：start_server 服务端**
`asyncio.start_server(<回调>, <主机>, <端口>)`
```python
# 异步 TCP 服务端
async def handle(reader, writer):
    data = await reader.read(100)
    writer.write(data)
    await writer.drain()
    writer.close()

server = await asyncio.start_server(handle, "0.0.0.0", 8888)
async with server:
    await server.serve_forever()
```

**基本写法：读写流**
`writer.write(<字节>)` | `await reader.read(<长度>)`
```python
# 流读写
writer.write(b"hello")
await writer.drain()
data = await reader.read(1024)
```

**基本写法：readline 与 readexactly**
`await reader.readline()` | `await reader.readexactly(<字节>)`
```python
# 按行读取与精确读取
line = await reader.readline()
data = await reader.readexactly(8)
```

---

## 取消与超时

**基本写法：cancel 取消任务**
`task.cancel()`
```python
# 取消任务
task = asyncio.create_task(fetch("a"))
task.cancel()
try:
    await task
except asyncio.CancelledError:
    print("任务已取消")
```

**基本写法：CancelledError 处理**
`try: await task\nexcept asyncio.CancelledError:`
```python
# 协程内处理取消
async def work():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("清理资源")
        raise
```

**基本写法：shield 屏蔽取消**
`asyncio.shield(<协程>)`
```python
# 保护协程不被取消
result = await asyncio.shield(fetch("a"))
```

---

## 事件循环

**基本写法：run 运行**
`asyncio.run(<协程>)`
```python
# 运行顶层协程
asyncio.run(main())
```

**基本写法：get_running_loop**
`asyncio.get_running_loop()`
```python
# 在协程中获取当前循环
loop = asyncio.get_running_loop()
```

**基本写法：run_in_executor 阻塞任务**
`loop.run_in_executor(<执行器>, <函数>, *<参数>)`
```python
# 在线程池运行阻塞函数
import time

async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, time.sleep, 1)
```

**基本写法：to_thread（3.9+）**
`asyncio.to_thread(<函数>, *<参数>)`
```python
# 简化版 run_in_executor
result = await asyncio.to_thread(time.sleep, 1)
```

**基本写法：call_later 延迟调用**
`loop.call_later(<秒>, <回调>)`
```python
# 延迟执行回调
loop = asyncio.get_running_loop()
loop.call_later(5, lambda: print("5 秒后"))
```

---

## sleep 与时间

**基本写法：sleep**
`await asyncio.sleep(<秒>)`
```python
# 异步等待
await asyncio.sleep(1.0)
```

**基本写法：get_event_loop 时间**
`loop.time()`
```python
# 事件循环单调时钟
loop = asyncio.get_running_loop()
start = loop.time()
```



<!-- ============ 文档分隔线：040-python/062-Pydantic.md ============ -->

# Python pydantic 数据验证

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## BaseModel 基础

**基本写法：定义模型**
`class <模型>(pydantic.BaseModel):\n    <字段>: <类型>`
```python
# pydantic v2 模型定义
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str = ""
```

**基本写法：从字典创建**
`<模型>(**<字典>)` | `<模型>.model_validate(<字典>)`
```python
# 从字典创建并验证
u = User(id=1, name="Alice")
u2 = User.model_validate({"id": 2, "name": "Bob"})
```

**基本写法：转换为字典**
`<实例>.model_dump()`
```python
# 模型转字典
print(u.model_dump())
```

**基本写法：转换为 JSON**
`<实例>.model_dump_json()`
```python
# 模型转 JSON 字符串
print(u.model_dump_json())
```

**基本写法：从 JSON 创建**
`<模型>.model_validate_json(<字符串>)`
```python
# 从 JSON 字符串创建
u = User.model_validate_json('{"id": 1, "name": "Alice"}')
```

---

## 字段验证

**基本写法：Field 字段配置**
`<字段>: <类型> = pydantic.Field(...)`
```python
# 字段元数据
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    price: float = Field(gt=0, description="价格")
    qty: int = Field(default=0, ge=0)
```

**基本写法：默认值与默认工厂**
`<字段>: <类型> = Field(default=<值>)` | `Field(default_factory=<函数>)`
```python
# 默认值
class Config(BaseModel):
    timeout: int = Field(default=30)
    tags: list = Field(default_factory=list)
```

**基本写法：Optional 与可空**
`<字段>: <类型> | None = None`
```python
# 可空字段
class User(BaseModel):
    email: str | None = None
```

---

## 验证器

**基本写法：field_validator**
`@pydantic.field_validator(<字段>)`
```python
# 字段级验证器
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("名称不能为空")
        return v
```

**基本写法：model_validator 模型级**
`@pydantic.model_validator(mode=<模式>)`
```python
# 模型级验证
from pydantic import BaseModel, model_validator

class DateRange(BaseModel):
    start: int
    end: int
    @model_validator(mode="after")
    def check_range(self):
        if self.start > self.end:
            raise ValueError("起始大于结束")
        return self
```

**基本写法：before 验证器**
`@field_validator(<字段>, mode="before")`
```python
# 在类型转换前验证
class Item(BaseModel):
    qty: int
    @field_validator("qty", mode="before")
    @classmethod
    def parse_qty(cls, v):
        if isinstance(v, str):
            return int(v)
        return v
```

---

## 类型注解

**基本写法：约束类型**
`Annotated[<类型>, <约束>]`
```python
# 使用 Annotated 添加约束
from typing import Annotated
from pydantic import BaseModel, Field

PosInt = Annotated[int, Field(gt=0)]
class Model(BaseModel):
    n: PosInt
```

**基本写法：Literal 枚举**
`<字段>: Literal[<值1>, <值2>]`
```python
# 字面值类型
from typing import Literal

class Config(BaseModel):
    mode: Literal["r", "w", "a"]
```

**基本写法：EmailStr 邮箱**
`<字段>: pydantic.EmailStr`
```python
# 邮箱字段（需安装 email-validator）
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
```

---

## 嵌套模型

**基本写法：嵌套模型**
`<字段>: <另一个模型>`
```python
# 模型嵌套
class Address(BaseModel):
    city: str
    zip: str

class User(BaseModel):
    name: str
    addr: Address

u = User(name="Alice", addr={"city": "Shanghai", "zip": "200000"})
```

**基本写法：列表模型**
`<字段>: list[<模型>]`
```python
# 模型列表
class Group(BaseModel):
    name: str
    users: list[User]
```

---

## 配置

**基本写法：model_config**
`model_config = pydantic.ConfigDict(...)`
```python
# 模型配置
class User(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        frozen=True,
        extra="forbid",
    )
    name: str
```

**基本写法：禁止额外字段**
`model_config = ConfigDict(extra="forbid")`
```python
# 拒绝未定义字段
class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")
    x: int
```

**基本写法：str_strip_whitespace**
`model_config = ConfigDict(str_strip_whitespace=True)`
```python
# 自动去除字符串空白
class User(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    name: str
```

---

## 序列化

**基本写法：自定义序列化**
`@pydantic.field_serializer(<字段>)`
```python
# 自定义字段序列化
from pydantic import BaseModel, field_serializer

class User(BaseModel):
    created_at: int
    @field_serializer("created_at")
    def ser_time(self, v):
        from datetime import datetime
        return datetime.fromtimestamp(v).isoformat()
```

**基本写法：排除字段**
`<实例>.model_dump(exclude=<键集>)`
```python
# 序列化排除字段
print(u.model_dump(exclude={"email"}))
```

**基本写法：include 包含**
`<实例>.model_dump(include=<键集>)`
```python
# 只包含指定字段
print(u.model_dump(include={"id", "name"}))
```

---

## 不可变模型

**基本写法：frozen 不可变**
`model_config = ConfigDict(frozen=True)`
```python
# 不可变模型
class Config(BaseModel):
    model_config = ConfigDict(frozen=True)
    host: str

c = Config(host="localhost")
# c.host = "other"  # 抛出 ValidationError
```

---

## 类型转换

**基本写法：严格模式**
`model_config = ConfigDict(strict=True)`
```python
# 严格模式，不自动转换类型
class M(BaseModel):
    model_config = ConfigDict(strict=True)
    x: int

# M(x="1")  # 抛出 ValidationError
M(x=1)
```

**基本写法：自动转换**
`pydantic` 默认行为
```python
# 默认会自动转换兼容类型
class M(BaseModel):
    x: int

m = M(x="123")
print(m.x)
```

---

## 错误处理

**基本写法：捕获 ValidationError**
`except pydantic.ValidationError:`
```python
# 捕获验证错误
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int

try:
    User(id="abc")
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], err["msg"])
```

**基本写法：errors 错误列表**
`e.errors()`
```python
# 获取所有错误
for err in e.errors():
    print(err)
```



<!-- ============ 文档分隔线：040-python/063-HttpxRequests.md ============ -->

# Python httpx 与 requests

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## httpx 客户端

**基本写法：创建客户端**
`httpx.Client()`
```python
# 同步客户端
import httpx

with httpx.Client() as client:
    resp = client.get("https://www.python.org")
```

**基本写法：AsyncClient**
`httpx.AsyncClient()`
```python
# 异步客户端
async with httpx.AsyncClient() as client:
    resp = await client.get("https://www.python.org")
```

**基本写法：get 请求**
`client.get(<URL>)`
```python
# GET 请求
resp = httpx.get("https://www.python.org")
print(resp.status_code)
```

**基本写法：post 请求**
`client.post(<URL>, json=<数据>)`
```python
# POST JSON
resp = httpx.post("https://httpbin.org/post", json={"name": "Alice"})
```

---

## httpx 响应

**基本写法：状态码**
`resp.status_code`
```python
# 状态码
print(resp.status_code)
```

**基本写法：响应文本**
`resp.text`
```python
# 文本内容
print(resp.text[:100])
```

**基本写法：响应 JSON**
`resp.json()`
```python
# JSON 内容
data = resp.json()
```

**基本写法：响应字节**
`resp.content`
```python
# 字节内容
print(resp.content[:50])
```

**基本写法：响应头**
`resp.headers`
```python
# 响应头
print(resp.headers["content-type"])
```

---

## httpx 请求配置

**基本写法：超时**
`httpx.Timeout(<秒>)` | `timeout=<秒>`
```python
# 超时配置
client = httpx.Client(timeout=10.0)
client = httpx.Client(timeout=httpx.Timeout(5.0, connect=2.0))
```

**基本写法：headers**
`client.headers[<键>] = <值>`
```python
# 默认请求头
client = httpx.Client(headers={"User-Agent": "MyClient/1.0"})
```

**基本写法：auth 认证**
`httpx.BasicAuth(<用户>, <密码>)`
```python
# 基本认证
client = httpx.Client(auth=httpx.BasicAuth("user", "pass"))
```

**基本写法：proxy 代理**
`httpx.Client(proxy=<URL>)`
```python
# 代理设置
client = httpx.Client(proxy="http://proxy:8080")
```

**基本写法：params 查询参数**
`client.get(<URL>, params=<字典>)`
```python
# 查询参数
resp = client.get("https://httpbin.org/get", params={"q": "python", "page": 1})
```

---

## httpx 会话管理

**基本写法：with 自动关闭**
`with httpx.Client() as client:`
```python
# 自动管理连接
with httpx.Client(base_url="https://api.example.com") as client:
    r1 = client.get("/users")
    r2 = client.get("/posts")
```

**基本写法：base_url 基础 URL**
`httpx.Client(base_url=<URL>)`
```python
# 基础 URL
client = httpx.Client(base_url="https://api.example.com")
r = client.get("/users")
```

---

## httpx 流式响应

**基本写法：stream 流式读取**
`with client.stream("GET", <URL>) as resp:`
```python
# 流式响应
with httpx.stream("GET", "https://example.com/big") as resp:
    for chunk in resp.iter_bytes(chunk_size=1024):
        print(len(chunk))
```

**基本写法：iter_lines**
`for line in resp.iter_lines():`
```python
# 按行迭代
with client.stream("GET", url) as resp:
    for line in resp.iter_lines():
        print(line)
```

---

## requests 库

**基本写法：get 请求**
`requests.get(<URL>, params=<字典>)`
```python
# requests GET
import requests

resp = requests.get("https://www.python.org", params={"q": "python"})
print(resp.status_code)
```

**基本写法：post 请求**
`requests.post(<URL>, data=<数据>, json=<JSON>)`
```python
# POST 表单与 JSON
r = requests.post(url, data={"key": "value"})
r = requests.post(url, json={"name": "Alice"})
```

**基本写法：自定义 headers**
`requests.get(<URL>, headers=<字典>)`
```python
# 自定义头
r = requests.get(url, headers={"User-Agent": "MyClient/1.0"})
```

**基本写法：timeout 超时**
`requests.get(<URL>, timeout=<秒>)`
```python
# 超时设置
r = requests.get(url, timeout=10)
```

---

## requests Session 会话

**基本写法：Session 复用连接**
`requests.Session()`
```python
# Session 保持 Cookie 与连接
s = requests.Session()
s.headers.update({"Authorization": "Bearer token"})
r1 = s.get(url)
r2 = s.get(url)
s.close()
```

**基本写法：with 自动关闭**
`with requests.Session() as s:`
```python
# 自动关闭会话
with requests.Session() as s:
    r = s.get(url)
```

---

## requests 响应

**基本写法：响应内容**
`r.text` | `r.json()` | `r.content`
```python
# 响应内容
print(r.text)
print(r.json())
print(r.content)
```

**基本写法：状态检查**
`r.raise_for_status()`
```python
# 状态码非 2xx 抛出异常
r = requests.get(url)
r.raise_for_status()
```

**基本写法：响应头**
`r.headers`
```python
# 响应头
print(r.headers["Content-Type"])
```

**基本写法：cookies**
`r.cookies`
```python
# 响应 Cookie
print(r.cookies.get("session"))
```

---

## requests 认证

**基本写法：basic auth**
`requests.auth.HTTPBasicAuth(<用户>, <密码>)`
```python
# 基本认证
from requests.auth import HTTPBasicAuth

r = requests.get(url, auth=HTTPBasicAuth("user", "pass"))
```

**基本写法：bearer token**
`headers={"Authorization": "Bearer <token>"}`
```python
# Bearer Token
r = requests.get(url, headers={"Authorization": "Bearer abc123"})
```

---

## requests 异常处理

**基本写法：捕获异常**
`except requests.RequestException:`
```python
# requests 异常基类
try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
except requests.Timeout:
    print("超时")
except requests.HTTPError as e:
    print("HTTP 错误:", e)
except requests.RequestException as e:
    print("请求异常:", e)
```

---

## 文件上传与下载

**基本写法：上传文件**
`requests.post(<URL>, files={<字段>: <文件>})`
```python
# multipart 上传
with open("data.txt", "rb") as f:
    r = requests.post(url, files={"file": f})
```

**基本写法：下载文件**
`with open(<路径>, "wb") as f:\n    f.write(r.content)`
```python
# 下载二进制
r = requests.get(url)
with open("image.png", "wb") as f:
    f.write(r.content)
```

**基本写法：流式下载**
`requests.get(<URL>, stream=True)`
```python
# 大文件流式下载
r = requests.get(url, stream=True)
with open("big.zip", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
```



<!-- ============ 文档分隔线：040-python/064-PackagingPublish.md ============ -->

# Python 打包与发布

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## setuptools 项目配置

**基本写法：pyproject.toml 元数据**
`[project]`
```toml
# 项目基本元数据
[project]
name = "mypackage"
version = "0.1.0"
description = "示例包"
readme = "README.md"
requires-python = ">=3.12"
license = {text = "MIT"}
authors = [{name = "Alice", email = "alice@example.com"}]
```

**基本写法：依赖声明**
`dependencies = [...]`
```toml
# 运行时依赖
dependencies = [
    "requests>=2.31",
    "pydantic>=2.0",
]
```

**基本写法：可选依赖**
`[project.optional-dependencies]`
```toml
# 可选依赖分组
[project.optional-dependencies]
dev = ["pytest>=8.0", "ruff>=0.4"]
docs = ["sphinx>=7.0"]
```

**基本写法：构建系统**
`[build-system]`
```toml
# 声明构建后端
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

**基本写法：包发现配置**
`[tool.setuptools.packages.find]`
```toml
# 自动发现包
[tool.setuptools.packages.find]
where = ["src"]
```

---

## 版本号管理

**基本写法：静态版本**
`version = "<版本>"`
```toml
# 直接写版本号
version = "1.2.3"
```

**基本写法：动态版本**
`dynamic = ["version"]`
```toml
# 动态读取版本
[project]
dynamic = ["version"]
[tool.setuptools.dynamic]
version = {attr = "mypackage.__version__"}
```

---

## 构建包

**基本写法：安装 build**
`pip install build`
```python
# 安装构建工具
pip install build
```

**基本写法：构建 sdist 与 wheel**
`python -m build`
```python
# 构建源码分发包与 wheel
python -m build
```

**基本写法：仅构建 wheel**
`python -m build --wheel`
```python
# 仅构建 wheel 包
python -m build --wheel
```

**基本写法：仅构建 sdist**
`python -m build --sdist`
```python
# 仅构建源码分发
python -m build --sdist
```

---

## wheel 包结构

**基本写法：查看 wheel 内容**
`python -m zipfile -l <wheel>`
```python
# 查看 wheel 内文件
python -m zipfile -l mypackage-0.1.0-py3-none-any.whl
```

**基本写法：纯 Python wheel**
`py3-none-any.whl`
```python
# 命名约定：{包名}-{版本}-{python}-{abi}-{平台}.whl
# py3-none-any：纯 Python，所有平台
```

**基本写法：平台 wheel**
`cp312-cp312-win_amd64.whl`
```python
# CPython 3.12，Windows x64 平台特定 wheel
```

---

## 发布到 PyPI

**基本写法：安装 twine**
`pip install twine`
```python
# 安装发布工具
pip install twine
```

**基本写法：检查包**
`twine check dist/*`
```python
# 检查包元数据
twine check dist/*
```

**基本写法：上传到 TestPyPI**
`twine upload --repository testpypi dist/*`
```python
# 上传到测试仓库
twine upload --repository testpypi dist/*
```

**基本写法：上传到 PyPI**
`twine upload dist/*`
```python
# 上传到正式 PyPI
twine upload dist/*
```

**基本写法：配置 API Token**
`~/.pypirc`
```ini
# 配置 PyPI 凭据
[pypi]
username = __token__
password = pypi-xxxxxxxxxxxx
```

---

## entry_points 入口点

**基本写法：命令行脚本**
`[project.scripts]`
```toml
# 注册命令行入口
[project.scripts]
mycli = "mypackage.cli:main"
```

**基本写法：GUI 入口**
`[project.gui-scripts]`
```toml
# GUI 应用入口
[project.gui-scripts]
mygui = "mypackage.gui:main"
```

---

## 包内资源

**基本写法：include-package-data**
`[tool.setuptools]`
```toml
# 包含所有版本控制文件
[tool.setuptools]
include-package-data = true
```

**基本写法：MANIFEST.in**
`include <文件模式>`
```
# 显式声明包含文件
include README.md LICENSE
recursive-include mypackage/data *.json *.txt
```

**基本写法：package-data**
`[tool.setuptools.package-data]`
```toml
# 指定包数据
[tool.setuptools.package-data]
mypackage = ["data/*.json"]
```

---

## 可编辑安装

**基本写法：开发模式安装**
`pip install -e <项目>`
```python
# 可编辑安装，源码修改即时生效
pip install -e .
```

**基本写法：PEP 660 可编辑安装**
`pip install -e . --config-settings editable_mode=compat`
```python
# 标准化可编辑安装
pip install -e .
```

---

## 依赖锁定

**基本写法：pip-tools 锁定**
`pip-compile <文件>`
```python
# 锁定依赖到 requirements.txt
pip install pip-tools
pip-compile pyproject.toml
```

**基本写法：pip-sync 同步**
`pip-sync <文件>`
```python
# 精确同步环境依赖
pip-sync requirements.txt
```

---

## uv 打包

**基本写法：uv build**
`uv build`
```python
# uv 构建包
uv build
```

**基本写法：uv publish**
`uv publish`
```python
# uv 发布到 PyPI
uv publish
```

---

## Poetry 打包

**基本写法：poetry build**
`poetry build`
```python
# poetry 构建包
poetry build
```

**基本写法：poetry publish**
`poetry publish`
```python
# poetry 发布到 PyPI
poetry publish
```

---

## ruff 配置

**基本写法：ruff 配置**
`[tool.ruff]`
```toml
# ruff 代码检查配置
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]
```



<!-- ============ 文档分隔线：040-python/065-DesignPattern.md ============ -->

# Python 设计模式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 单例模式

**基本写法：模块级单例**
`<模块>.py`
```python
# 模块本身就是单例
# config.py
class Config:
    def __init__(self):
        self.settings = {}

config = Config()  # 模块变量

# 使用：from config import config
```

**基本写法：__new__ 实现**
`class <类>:\n    _instance = None\n    def __new__(cls):`
```python
# 通过 __new__ 控制实例化
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True
```

**基本写法：元类单例**
`class <元类>(type):\n    def __call__(cls):`
```python
# 元类实现单例
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DB(metaclass=SingletonMeta):
    pass
```

**基本写法：装饰器单例**
`def singleton(cls):`
```python
# 装饰器实现单例
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Service:
    pass
```

---

## 工厂模式

**基本写法：简单工厂**
`def create(<类型>):`
```python
# 工厂函数
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

def create_animal(kind):
    if kind == "dog":
        return Dog()
    if kind == "cat":
        return Cat()
    raise ValueError("未知类型")
```

**基本写法：工厂方法**
`class <类>:\n    def create(self):`
```python
# 工厂方法模式
class AnimalFactory:
    def create(self):
        raise NotImplementedError

class DogFactory(AnimalFactory):
    def create(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create(self):
        return Cat()
```

**基本写法：抽象工厂**
`class <抽象工厂>(abc.ABCMeta):`
```python
# 抽象工厂
import abc

class GUIFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self): pass
    @abc.abstractmethod
    def create_input(self): pass

class WinFactory(GUIFactory):
    def create_button(self): return WinButton()
    def create_input(self): return WinInput()
```

---

## 观察者模式

**基本写法：观察者模式**
`class <主题>:\n    def attach(self, obs):`
```python
# 观察者模式
class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, obs):
        self._observers.append(obs)
    def detach(self, obs):
        self._observers.remove(obs)
    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)

class Observer:
    def update(self, msg):
        print(f"收到: {msg}")
```

**基本写法：弱引用观察者**
`weakref.WeakSet`
```python
# 使用弱引用避免内存泄漏
import weakref

class Subject:
    def __init__(self):
        self._observers = weakref.WeakSet()
    def attach(self, obs):
        self._observers.add(obs)
    def notify(self, msg):
        for obs in self._observers:
            obs.update(msg)
```

---

## 策略模式

**基本写法：策略模式**
`class <上下文>:\n    def __init__(self, strategy):`
```python
# 策略模式
from typing import Callable

class Sorter:
    def __init__(self, strategy: Callable):
        self.strategy = strategy
    def sort(self, data):
        return self.strategy(data)

asc = lambda x: sorted(x)
desc = lambda x: sorted(x, reverse=True)

s = Sorter(asc)
print(s.sort([3, 1, 2]))
```

---

## 装饰器模式

**基本写法：装饰器模式**
`def <装饰器>(<对象>):`
```python
# 装饰器模式（不修改原对象）
class Coffee:
    def cost(self): return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost() + 1

c = SugarDecorator(MilkDecorator(Coffee()))
print(c.cost())  # 8
```

---

## 适配器模式

**基本写法：适配器模式**
`class <适配器>:\n    def __init__(self, adaptee):`
```python
# 适配器模式
class OldPrinter:
    def print_old(self, msg):
        print(f"[OLD] {msg}")

class PrinterAdapter:
    def __init__(self, old):
        self.old = old
    def print(self, msg):
        self.old.print_old(msg)

p = PrinterAdapter(OldPrinter())
p.print("hello")
```

---

## 命令模式

**基本写法：命令模式**
`class <命令>:\n    def execute(self):`
```python
# 命令模式
class Command:
    def execute(self):
        raise NotImplementedError

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.on()

class Light:
    def on(self): print("灯亮")
    def off(self): print("灯灭")

class Remote:
    def __init__(self):
        self._cmd = None
    def set_command(self, cmd):
        self._cmd = cmd
    def press(self):
        self._cmd.execute()
```

---

## 模板方法模式

**基本写法：模板方法**
`class <抽象类>:\n    def template_method(self):`
```python
# 模板方法模式
import abc

class DataProcessor(abc.ABC):
    def process(self):
        data = self.read()
        result = self.transform(data)
        self.write(result)

    @abc.abstractmethod
    def read(self): pass
    @abc.abstractmethod
    def transform(self, data): pass
    @abc.abstractmethod
    def write(self, data): pass

class CSVProcessor(DataProcessor):
    def read(self): return []
    def transform(self, data): return data
    def write(self, data): print(data)
```

---

## 责任链模式

**基本写法：责任链**
`class <处理器>:\n    def set_next(self, h):`
```python
# 责任链模式
class Handler:
    def __init__(self):
        self._next = None
    def set_next(self, handler):
        self._next = handler
        return handler
    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        return None

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("token"):
            return "未认证"
        return super().handle(request)

class LogHandler(Handler):
    def handle(self, request):
        print(f"记录请求")
        return super().handle(request)
```

---

## 上下文管理器模式

**基本写法：with 语句模式**
`class <类>:\n    def __enter__(self): ...\n    def __exit__(self, *a):`
```python
# 上下文管理器模式
class Transaction:
    def __enter__(self):
        print("开始事务")
        return self
    def __exit__(self, *exc):
        if exc[0] is None:
            print("提交")
        else:
            print("回滚")
        return False

with Transaction():
    pass
```



<!-- ============ 文档分隔线：040-python/066-ProfilingOptimization.md ============ -->

# Python 性能分析与优化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## timeit 计时

**基本写法：timeit 计时**
`timeit.timeit(<代码>, number=<次数>)`
```python
# 测量代码执行时间
import timeit

t = timeit.timeit("sum(range(100))", number=10000)
print(t)
```

**基本写法：repeat 重复测量**
`timeit.repeat(<代码>, repeat=<次数>, number=<次数>)`
```python
# 多次重复测量
times = timeit.repeat("sum(range(100))", repeat=5, number=10000)
print(min(times))
```

**基本写法：命令行**
`python -m timeit -s <setup> <代码>`
```python
# 命令行计时
# python -m timeit -s "import json" "json.dumps({'a':1})"
```

**基本写法：Timer 对象**
`timeit.Timer(<代码>, setup=<准备>)`
```python
# Timer 对象
t = timeit.Timer("x.append(1)", setup="x = []")
print(t.timeit(number=100000))
```

---

## time 性能计数器

**基本写法：perf_counter 高精度**
`time.perf_counter()`
```python
# 高精度计时器
import time

start = time.perf_counter()
# 执行代码
time.sleep(0.1)
end = time.perf_counter()
print(f"耗时 {end - start:.4f}s")
```

**基本写法：perf_counter_ns 纳秒**
`time.perf_counter_ns()`
```python
# 纳秒级精度
start = time.perf_counter_ns()
# 执行代码
end = time.perf_counter_ns()
print(f"耗时 {end - start}ns")
```

**基本写法：process_time 进程时间**
`time.process_time()`
```python
# 进程 CPU 时间（不含睡眠）
start = time.process_time()
# 执行代码
end = time.process_time()
print(f"CPU 时间 {end - start}s")
```

---

## cProfile 性能分析

**基本写法：cProfile 运行**
`cProfile.run(<代码字符串>)`
```python
# 分析代码性能
import cProfile

cProfile.run("sum(range(1000000))")
```

**基本写法：Profile 对象**
`cProfile.Profile()`
```python
# Profile 对象精细控制
prof = cProfile.Profile()
prof.enable()
# 执行代码
sum(range(100000))
prof.disable()
prof.print_stats(sort="cumtime")
```

**基本写法：排序输出**
`prof.print_stats(sort=<排序>)`
```python
# 按累计时间排序
prof.print_stats(sort="cumulative")
prof.print_stats(sort="tottime")  # 按总时间
```

**基本写法：保存到文件**
`prof.dump_stats(<文件>)`
```python
# 保存分析数据
prof.dump_stats("profile.prof")
```

**基本写法：pstats 分析**
`pstats.Stats(<文件>)`
```python
# 加载并分析 profile 文件
import pstats

stats = pstats.Stats("profile.prof")
stats.sort_stats("cumulative").print_stats(10)
```

---

## memory_profiler 内存分析

**基本写法：profile 装饰器**
`@profile`
```python
# 需要安装 memory_profiler
# pip install memory_profiler
@profile
def my_func():
    a = [1] * 1000000
    return sum(a)

my_func()
# 运行：python -m memory_profiler script.py
```

**基本写法：memit 内存峰值**
`%memit <表达式>`
```python
# IPython 中测量内存峰值
# %memit sum(range(1000000))
```

---

## sys.getsizeof 内存占用

**基本写法：获取对象大小**
`sys.getsizeof(<对象>)`
```python
# 获取对象字节大小
import sys

print(sys.getsizeof([1, 2, 3]))
print(sys.getsizeof("hello"))
print(sys.getsizeof({}))
```

**基本写法：tracemalloc 跟踪分配**
`tracemalloc.start()`
```python
# 跟踪内存分配
import tracemalloc

tracemalloc.start()
# 执行代码
data = [i for i in range(100000)]
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics("lineno")[:5]:
    print(stat)
```

**基本写法：比较快照**
`snapshot2.compare_to(snapshot1, "lineno")`
```python
# 比较两个内存快照
snap1 = tracemalloc.take_snapshot()
# 执行代码
snap2 = tracemalloc.take_snapshot()
for stat in snap2.compare_to(snap1, "lineno")[:5]:
    print(stat)
```

---

## dis 字节码分析

**基本写法：反汇编**
`dis.dis(<函数>)`
```python
# 查看函数字节码
import dis

def loop():
    total = 0
    for i in range(100):
        total += i
    return total

dis.dis(loop)
```

---

## 优化技巧

**基本写法：列表推导优于循环**
`[<表达式> for <变量> in <可迭代>]`
```python
# 列表推导比 append 循环快
squares = [x * x for x in range(1000)]
```

**基本写法：生成器节省内存**
`(<表达式> for <变量> in <可迭代>)`
```python
# 大数据用生成器
squares_gen = (x * x for x in range(1000000))
```

**基本写法：set 成员查找**
`<值> in <集合>`
```python
# set 查找 O(1)，list 查找 O(n)
valid = {"a", "b", "c"}  # 用 set 而非 list
if x in valid:
    pass
```

**基本写法：局部变量优化**
`def <函数>():\n    <局部变量>`
```python
# 局部变量比全局变量快
def compute():
    # 局部变量访问快
    total = sum
    return total(range(100))
```

**基本写法：__slots__ 节省内存**
`class <类>:\n    __slots__ = (<字段>,)`
```python
# __slots__ 减少内存与加速属性访问
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**基本写法：lru_cache 缓存**
`@functools.lru_cache(maxsize=<大小>)`
```python
# 缓存函数结果
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## sys.monitoring 监控（3.12+）

**基本写法：注册监控工具**
`sys.monitoring.use_tool_id(<ID>, <名称>)`
```python
# Python 3.12 低开销监控（PEP 669）
import sys.monitoring

sys.monitoring.use_tool_id(0, "my_profiler")
sys.monitoring.register_callback(
    sys.monitoring.events.PY_START,
    0,
    lambda code, offset: print("开始", code.co_name)
)
```

**基本写法：获取事件**
`sys.monitoring.events`
```python
# 监控事件类型
print(sys.monitoring.events.PY_START)
print(sys.monitoring.events.PY_RESUME)
print(sys.monitoring.events.CALL)
```

---

## 并行加速

**基本写法：多进程 CPU 密集**
`concurrent.futures.ProcessPoolExecutor()`
```python
# CPU 密集型用多进程
from concurrent.futures import ProcessPoolExecutor

def heavy(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor() as ex:
        results = list(ex.map(heavy, [1000000, 2000000, 3000000]))
```

**基本写法：多线程 IO 密集**
`concurrent.futures.ThreadPoolExecutor()`
```python
# IO 密集型用多线程或 asyncio
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as r:
        return r.read()

with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(fetch, urls))
```

---

## 字符串拼接优化

**基本写法：join 优于 +**
`"<分隔>".join(<字符串列表>)`
```python
# join 比 + 拼接高效
parts = ["a", "b", "c"]
result = "".join(parts)  # 优于 result = parts[0] + parts[1] + ...
```



<!-- ============ 文档分隔线：040-python/067-VirtualEnvPackageManagement.md ============ -->

# Python 虚拟环境与包管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## venv 标准库

**基本写法：创建虚拟环境**
`python -m venv <目录>`
```python
# 在当前目录创建 .venv 虚拟环境
# python -m venv .venv
```

---

**基本写法：激活虚拟环境（Windows）**
`.venv\Scripts\Activate.ps1`
```python
# PowerShell 激活脚本，激活后提示符前缀显示 (.venv)
# .venv\Scripts\Activate.ps1
```

---

**基本写法：激活虚拟环境（Linux/macOS）**
`source <目录>/bin/activate`
```python
# bash/zsh 下激活
# source .venv/bin/activate
```

---

**基本写法：退出虚拟环境**
`deactivate`
```python
# 在已激活环境中退出
# deactivate
```

---

**基本写法：指定不安装 pip**
`python -m venv <目录> --without-pip`
```python
# 创建不含 pip 的轻量环境
# python -m venv myenv --without-pip
```

---

**基本写法：升级环境内部组件**
`python -m venv <目录> --upgrade`
```python
# 升级已有环境的 Python 内部组件，保留已装包
# python -m venv myenv --upgrade
```

---

## pip 包管理

**基本写法：安装包**
`pip install <包名>`
```python
# 安装最新版本的 requests
# pip install requests
```

---

**基本写法：安装指定版本**
`pip install <包名>==<版本>`
```python
# 安装指定版本
# pip install requests==2.32.3
```

---

**基本写法：从需求文件安装**
`pip install -r <需求文件>`
```python
# 按 requirements.txt 批量安装
# pip install -r requirements.txt
```

---

**基本写法：卸载包**
`pip uninstall <包名>`
```python
# 卸载指定包
# pip uninstall requests
```

---

**基本写法：导出依赖列表**
`pip freeze > <文件>`
```python
# 将当前已安装包导出为 requirements
# pip freeze > requirements.txt
```

---

**基本写法：查看已安装包**
`pip list`
```python
# 列出所有已安装包及版本
# pip list
```

---

**基本写法：升级包**
`pip install --upgrade <包名>`
```python
# 升级到最新版本
# pip install --upgrade requests
```

---

**基本写法：查看包详情**
`pip show <包名>`
```python
# 显示包元信息与依赖
# pip show requests
```

---

## poetry 项目管理

**基本写法：初始化项目**
`poetry init`
```python
# 交互式生成 pyproject.toml
# poetry init
```

---

**基本写法：新建项目**
`poetry new <项目名>`
```python
# 创建标准目录结构
# poetry new mypkg
```

---

**基本写法：添加依赖**
`poetry add <包名>`
```python
# 安装并写入 pyproject.toml
# poetry add fastapi
```

---

**基本写法：添加开发依赖**
`poetry add <包名> --group dev`
```python
# 添加到 dev 依赖组
# poetry add pytest --group dev
```

---

**基本写法：安装全部依赖**
`poetry install`
```python
# 按 pyproject.toml 安装并锁定
# poetry install
```

---

**基本写法：指定解释器创建环境**
`poetry env use <python版本>`
```python
# 使用指定解释器创建虚拟环境
# poetry env use python3.12
```

---

**基本写法：运行命令**
`poetry run <命令>`
```python
# 在项目环境中执行
# poetry run python main.py
```

---

**基本写法：打包构建**
`poetry build`
```python
# 生成 sdist 与 wheel 包
# poetry build
```

---

**基本写法：发布到 PyPI**
`poetry publish`
```python
# 发布构建产物到 PyPI
# poetry publish
```

---

## uv 极速管理

**基本写法：创建虚拟环境**
`uv venv [目录]`
```python
# 默认在 .venv 创建环境
# uv venv
```

---

**基本写法：指定 Python 版本**
`uv venv --python <版本>`
```python
# 自动下载并使用指定版本
# uv venv --python 3.13
```

---

**基本写法：pip 兼容安装**
`uv pip install <包名>`
```python
# 兼容 pip 语法但更快
# uv pip install requests
```

---

**基本写法：按需求文件安装**
`uv pip install -r <需求文件>`
```python
# 批量安装依赖
# uv pip install -r requirements.txt
```

---

**基本写法：导出依赖**
`uv pip freeze > <文件>`
```python
# 导出当前环境依赖
# uv pip freeze > requirements.txt
```

---

**基本写法：添加项目依赖**
`uv add <包名>`
```python
# 写入 pyproject.toml 并安装
# uv add fastapi
```

---

**基本写法：移除依赖**
`uv remove <包名>`
```python
# 从项目中移除
# uv remove fastapi
```

---

**基本写法：同步依赖**
`uv sync`
```python
# 按锁文件精确重建环境
# uv sync
```

---

**基本写法：运行脚本**
`uv run <脚本>`
```python
# 自动加载环境运行
# uv run python main.py
```

---

**基本写法：临时依赖运行**
`uv run --with <包名> <命令>`
```python
# 隔离环境临时安装并执行
# uv run --with httpx python -c "import httpx"
```

---

**基本写法：初始化项目**
`uv init <项目名>`
```python
# 生成标准项目结构
# uv init myproject
```

---

**基本写法：安装指定 Python**
`uv python install <版本>`
```python
# 下载安装指定解释器
# uv python install 3.13
```

---

**基本写法：列出可用 Python**
`uv python list`
```python
# 查看本地及可下载版本
# uv python list
```

---



<!-- ============ 文档分隔线：040-python/068-Dataclass.md ============ -->

# Python dataclass 数据类

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本数据类

**基本写法：定义数据类**
`@dataclass` 装饰器应用于类
```python
from dataclasses import dataclass

# 自动生成 __init__/__repr__/__eq__
@dataclass
class Point:
    x: float
    y: float
```

---

**基本写法：带默认值字段**
`<字段名>: <类型> = <默认值>`
```python
# 提供默认值的字段必须放在无默认值字段之后
@dataclass
class User:
    name: str
    age: int = 0
    active: bool = True
```

---

## field 字段配置

**基本写法：可变默认值**
`field(default_factory=<工厂函数>)`
```python
from dataclasses import dataclass, field

# 列表/字典等可变默认值必须用 default_factory
@dataclass
class Config:
    tags: list = field(default_factory=list)
    meta: dict = field(default_factory=dict)
```

---

**基本写法：忽略字段比较**
`field(compare=False)`
```python
# 不参与 __eq__ 与 __hash__ 比较
@dataclass
class Task:
    id: int
    cache: list = field(default_factory=list, compare=False)
```

---

**基本写法：字段不参与初始化**
`field(init=False)`
```python
# 字段不进 __init__，常用于派生属性
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = self.width * self.height
```

---

**基本写法：字段默认值与 repr 控制**
`field(default=<值>, repr=<布尔>)`
```python
# repr=False 隐藏敏感字段
@dataclass
class Account:
    username: str
    token: str = field(default="", repr=False)
```

---

## 冻结与哈希

**基本写法：不可变数据类**
`@dataclass(frozen=True)`
```python
# frozen 后实例不可修改，且可哈希，可作为字典键或集合元素
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lng: float
```

---

**基本写法：自定义哈希**
`@dataclass(unsafe_hash=True)`
```python
# 即便有非哈希字段也强制生成 __hash__
@dataclass(unsafe_hash=True)
class Key:
    name: str
```

---

## slots 优化

**基本写法：启用 slots**
`@dataclass(slots=True)`
```python
# 生成 __slots__，禁止动态属性，节省内存
@dataclass(slots=True)
class Pixel:
    r: int
    g: int
    b: int
```

---

**基本写法：冻结与 slots 同时启用**
`@dataclass(frozen=True, slots=True)`
```python
# 不可变且内存优化的数据类
@dataclass(frozen=True, slots=True)
class Color:
    value: int
```

---

## InitVar 与 __post_init__

**基本写法：仅初始化参数**
`<字段名>: <类型> = dataclasses.InitVar`
```python
from dataclasses import dataclass, field, InitVar

# InitVar 仅传参用，不成为实例字段
@dataclass
class DbConfig:
    host: str
    port: int
    url: InitVar[str] = ""

    def __post_init__(self, url: str):
        # url 不存为字段，仅用于初始化逻辑
        if url:
            print("init from url:", url)
```

---

**基本写法：post_init 后处理**
`def __post_init__(self):`
```python
# __init__ 执行后自动调用，用于校验或派生字段
@dataclass
class Range:
    start: int
    end: int

    def __post_init__(self):
        if self.start > self.end:
            raise ValueError("start 不能大于 end")
```

---

## 类方法生成

**基本写法：生成排序方法**
`@dataclass(order=True)`
```python
# 生成 __lt__/__le__/__gt__/__ge__，可排序
@dataclass(order=True)
class Version:
    major: int
    minor: int
```

---

## 转换工具

**基本写法：实例转字典**
`dataclasses.asdict(<实例>)`
```python
import dataclasses

# 深度转换为字典，便于序列化
@dataclass
class Point:
    x: int
    y: int

d = dataclasses.asdict(Point(1, 2))  # {'x': 1, 'y': 2}
```

---

**基本写法：实例转元组**
`dataclasses.astuple(<实例>)`
```python
# 转换为字段值元组
@dataclass
class Point:
    x: int
    y: int

t = dataclasses.astuple(Point(1, 2))  # (1, 2)
```

---

**基本写法：从字典构造**
`<类>(**<字典>)`
```python
# 利用解包从字典重建实例
@dataclass
class Point:
    x: int
    y: int

data = {"x": 3, "y": 4}
p = Point(**data)
```

---

**基本写法：替换字段生成新实例**
`dataclasses.replace(<实例>, <字段>=<新值>)`
```python
# 基于已有实例生成仅部分字段不同的新实例
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p2 = dataclasses.replace(p, y=5)  # Point(x=1, y=5)
```

---

**基本写法：查询字段信息**
`dataclasses.fields(<类或实例>)`
```python
# 返回 Field 对象元组，含 name/type/default
@dataclass
class Point:
    x: int
    y: int

for f in dataclasses.fields(Point):
    print(f.name, f.type)
```

---

## KW_ONLY 参数

**基本写法：仅关键字参数**
`@dataclass(kw_only=True)`
```python
# 所有字段只能以关键字形式传入
@dataclass(kw_only=True)
class Server:
    host: str
    port: int
```

---

**基本写法：部分仅关键字**
`<字段>: <类型> = field(kw_only=True)`
```python
# 单个字段标记为仅关键字
@dataclass
class Connection:
    url: str
    timeout: int = field(default=30, kw_only=True)
```

---



<!-- ============ 文档分隔线：040-python/069-ModulePackageImport.md ============ -->

# Python 模块包导入

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本导入

**基本写法：导入模块**
`import <模块名>`
```python
# 导入整个模块，通过模块名访问成员
import os
path = os.getcwd()
```

---

**基本写法：导入特定成员**
`from <模块> import <名称>`
```python
# 仅导入需要的函数或类
from pathlib import Path
p = Path(".")
```

---

**基本写法：导入并设置别名**
`import <模块> as <别名>`
```python
# 用别名简化长模块名
import numpy as np
arr = np.array([1, 2, 3])
```

---

**基本写法：导入多个成员**
`from <模块> import <名称1>, <名称2>`
```python
# 一次导入多个符号
from collections import deque, defaultdict
```

---

**基本写法：导入全部公开成员**
`from <模块> import *`
```python
# 导入 __all__ 列出的名称，无 __all__ 则导入所有非下划线开头名称
# 不推荐在生产代码使用，易造成命名冲突
```

---

## 包与 __init__.py

**基本写法：定义包**
`<目录>/__init__.py`
```python
# 含 __init__.py 的目录即为包（Python 3.3+ 普通目录也支持命名空间包）
# mypackage/__init__.py
__all__ = ["core", "utils"]
```

---

**基本写法：包内模块导入**
`from <包> import <模块>`
```python
# mypackage/core.py 中定义函数
# 外部调用
from mypackage import core
core.run()
```

---

## __all__ 公开接口

**基本写法：声明公开名称**
`__all__ = [<名称列表>]`
```python
# 模块顶部声明，控制 from module import * 的导出范围
# utils.py
__all__ = ["helper", "format_text"]

def helper():
    pass

def _internal():
    # 以 _ 开头默认为私有，不会被 import * 导入
    pass
```

---

## 相对导入

**基本写法：当前包内导入**
`from . import <模块>`
```python
# 一个点表示当前包目录
# mypackage/core.py
from . import utils
```

---

**基本写法：上级包导入**
`from .. import <模块>`
```python
# 两个点表示上一级包
# mypackage/sub/child.py
from .. import core
```

---

**基本写法：指定相对层级**
`from .<模块> import <名称>`
```python
# 从当前包的指定模块导入
# mypackage/core.py
from .utils import format_text
```

---

## sys.path 路径管理

**基本写法：查看搜索路径**
`sys.path`
```python
import sys
# 列出模块搜索路径，首项常为当前脚本目录
print(sys.path)
```

---

**基本写法：临时添加搜索路径**
`sys.path.append(<路径>)`
```python
import sys
# 运行时动态加入目录，重启后失效
sys.path.append("/home/user/libs")
import mylib
```

---

**基本写法：插入到路径最前**
`sys.path.insert(0, <路径>)`
```python
import sys
# 0 表示最高优先级
sys.path.insert(0, "/opt/custom")
```

---

## importlib 动态导入

**基本写法：按字符串导入模块**
`importlib.import_module(<模块名>)`
```python
import importlib
# 运行时根据字符串动态加载模块
mod = importlib.import_module("json")
print(mod.dumps({"a": 1}))
```

---

**基本写法：导入子模块**
`importlib.import_module("<包>.<模块>")`
```python
import importlib
# 动态加载包内子模块
core = importlib.import_module("mypackage.core")
```

---

**基本写法：按名称获取函数**
`getattr(<模块>, <名称>)`
```python
import importlib
mod = importlib.import_module("collections")
# 再用 getattr 取出具体成员
Deque = getattr(mod, "deque")
```

---

## 模块属性

**基本写法：模块名**
`__name__`
```python
# 模块自身为 "__main__"，被导入时为模块全名
if __name__ == "__main__":
    main()
```

---

**基本写法：模块文件路径**
`__file__`
```python
# 获取模块所在文件路径
print(__file__)
```

---

**基本写法：模块文档字符串**
`__doc__`
```python
"""模块顶部文档字符串。"""
# 通过 __doc__ 访问
print(__doc__)
```

---

**基本写法：包路径**
`__path__`
```python
# 仅包拥有 __path__，表示包目录列表
# 子模块导入时会基于 __path__ 查找
```

---

## 模块缓存

**基本写法：查看已加载模块**
`sys.modules`
```python
import sys
# 字典缓存所有已导入模块，键为模块全名
print("json" in sys.modules)
```

---

**基本写法：重载模块**
`importlib.reload(<模块>)`
```python
import importlib, mymod
# 开发期修改源码后重新加载
importlib.reload(mymod)
```

---

## 条件与延迟导入

**基本写法：函数内导入**
`def <函数>(): import <模块>`
```python
# 延迟到调用时导入，常用于避免循环依赖或加速启动
def parse(path):
    import json
    with open(path) as f:
        return json.load(f)
```

---

**基本写法：try 容错导入**
`try: import <模块>`
```python
# 优先使用 C 加速版本，失败回退纯 Python
try:
    import cjson as json
except ImportError:
    import json
```

---
