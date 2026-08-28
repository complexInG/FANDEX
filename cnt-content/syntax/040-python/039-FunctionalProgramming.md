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
