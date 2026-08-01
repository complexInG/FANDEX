---
order: 770
title: Python math/random/statistics
module: python

category: '040-python'
difficulty: beginner
description: Python math/random/statistics 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
