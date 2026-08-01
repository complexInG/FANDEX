---
title: 'Python 理论知识点'
module: python
category: 'Python Theory'
order: 160
tags:
  - python
  - theory
difficulty: intermediate
description: 'GIL 机制、内存管理、字节码与运行时模型。'
related:
  - python/文件IO与上下文管理器
  - 'python/项目示例-网页爬虫与数据分析'
prerequisites:
  - python/语法速查
updated: '2026-08-01'
---

1. 线程获取 GIL
2. 执行一定数量的字节码（check interval，默认 100 条）或达到时间片（5ms）
3. 线程释放 GIL
4. 其他线程竞争获取 GIL
5. 原线程可能重新获取 GIL（非公平竞争）

```python
import sys
sys.getcheckinterval()  # 默认 100（字节码指令数）
sys.setcheckinterval(200)  # 设置检查间隔
```

### GIL 对多线程的影响

| 场景       | GIL 影响                          | 推荐方案                      |
| ---------- | --------------------------------- | ----------------------------- |
| CPU 密集型 | 多线程无法并行，甚至比单线程慢    | 多进程（multiprocessing）     |
| I/O 密集型 | GIL 在 I/O 等待时释放，多线程有效 | 多线程（threading）或 asyncio |
| C 扩展     | 可手动释放 GIL                    | ctypes/Cython 中释放 GIL      |
| 混合型     | 部分并行                          | 线程池 + 进程池组合           |

CPU 密集型多线程反而更慢的原因：线程切换本身有开销，加上 GIL 的获取/释放竞争，增加了额外的时间消耗。

### 绕过 GIL 的策略

1. **multiprocessing** -- 每个进程有独立的 GIL

   ```python
   from multiprocessing import Pool
   with Pool(4) as p:
       results = p.map(cpu_bound_func, data)
   ```

2. **C 扩展释放 GIL** -- 在 C 代码中手动释放

   ```c
   Py_BEGIN_ALLOW_THREADS
   // C 代码，不操作 Python 对象
   Py_END_ALLOW_THREADS
   ```

3. **concurrent.futures** -- 高层抽象

   ```python
   from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
   # CPU 密集用 ProcessPoolExecutor
   # I/O 密集用 ThreadPoolExecutor
   ```

4. **numpy/numba** -- 内部释放 GIL 的数值计算库

### GIL 的未来

PEP 703 提议在 CPython 3.13+ 中提供可选的 free-threaded 模式（nogil），通过以下方式实现：

- 将引用计数改为偏向引用计数（biased reference counting）
- 对共享对象使用原子引用计数
- 引入内存安全机制替代 GIL 的保护作用

---

## Python 字节码

### 字节码执行模型

Python 代码的执行过程：

```
源代码(.py) --> 编译器 --> 字节码(.pyc) --> 虚拟机 --> 执行结果
```

CPython 虚拟机是一个基于栈的虚拟机，通过操作数栈（evaluation stack）执行计算。

### 查看字节码

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

输出：

```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

### 常见字节码指令

| 指令              | 说明               | 栈效果                     |
| ----------------- | ------------------ | -------------------------- |
| LOAD_CONST        | 加载常量到栈顶     | push                       |
| LOAD_FAST         | 加载局部变量到栈顶 | push                       |
| STORE_FAST        | 将栈顶存入局部变量 | pop                        |
| LOAD_GLOBAL       | 加载全局变量到栈顶 | push                       |
| LOAD_ATTR         | 加载对象属性到栈顶 | pop, push                  |
| BINARY_ADD        | 栈顶两元素相加     | pop x2, push               |
| BINARY_SUBSCR     | 下标访问 a[b]      | pop x2, push               |
| CALL_FUNCTION     | 调用函数           | pop args+func, push result |
| RETURN_VALUE      | 返回栈顶元素       | pop                        |
| COMPARE_OP        | 比较操作           | pop x2, push               |
| POP_JUMP_IF_FALSE | 条件跳转           | pop                        |
| FOR_ITER          | for 循环迭代       | push                       |

### 字节码与性能

Python 每条字节码的执行涉及：

1. 解码指令
2. 分发到对应的处理函数
3. 操作数栈的 push/pop
4. GIL 检查

这些开销使得 Python 比 C 慢约 50-100 倍。JIT 编译器（如 PyPy）通过将热点字节码编译为机器码来消除这些开销。

### .pyc 文件

Python 自动将编译后的字节码缓存到 `__pycache__` 目录下的 `.pyc` 文件中。缓存失效条件：

- 源文件的修改时间戳变化
- 源文件的大小变化
- Python 版本或魔法号（magic number）不匹配

---

## 描述符协议（Descriptor Protocol）

### 什么是描述符

描述符是实现了 `__get__`、`__set__` 或 `__delete__` 中任意一个方法的类。描述符允许自定义属性的访问、赋值和删除行为，是 Python 中最强大的特性之一。

### 描述符的分类

| 类型         | 实现方法              | 典型用途                        |
| ------------ | --------------------- | ------------------------------- |
| 数据描述符   | `__get__` + `__set__` | property、类属性验证            |
| 非数据描述符 | 仅 `__get__`          | 方法、classmethod、staticmethod |

### 描述符协议方法

```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        # obj 为 None 时表示通过类访问
        # obj 不为 None 时表示通过实例访问
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        # 仅数据描述符需要实现
        obj.__dict__[self.name] = value

    def __delete__(self, obj):
        # 可选实现
        del obj.__dict__[self.name]

    def __set_name__(self, owner, name):
        # Python 3.6+，自动获取属性名
        self.name = name
```

### 属性查找优先级

Python 属性查找的优先级顺序：

1. **数据描述符** -- 类中定义了 `__get__` 和 `__set__` 的描述符
2. **实例属性** -- `obj.__dict__` 中的属性
3. **非数据描述符** -- 类中仅定义了 `__get__` 的描述符
4. **`__getattr__`** -- 以上都未找到时调用

```python
class DataDescriptor:
    def __get__(self, obj, objtype=None):
        return "from data descriptor"
    def __set__(self, obj, value):
        pass

class NonDataDescriptor:
    def __get__(self, obj, objtype=None):
        return "from non-data descriptor"

class Example:
    data_desc = DataDescriptor()
    non_data_desc = NonDataDescriptor()

    def __init__(self):
        self.data_desc = "instance value"   # 被数据描述符拦截
        self.non_data_desc = "instance value" # 实例属性优先

e = Example()
print(e.data_desc)      # "from data descriptor"（数据描述符优先）
print(e.non_data_desc)  # "instance value"（实例属性优先于非数据描述符）
```

### property 的本质

property 是数据描述符的语法糖：

```python
# 使用 property
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

# 等价的手动描述符
class RadiusDescriptor:
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj._radius

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        obj._radius = value
```

### 描述符的实际应用

1. **类型验证** -- 在 `__set__` 中检查赋值类型
2. **延迟计算** -- 在 `__get__` 中按需计算并缓存
3. **ORM 字段** -- SQLAlchemy/ Django Model 的字段定义
4. **信号/事件** -- 属性变化时触发回调
5. **访问控制** -- 实现只读属性、受保护属性

---

## MRO（Method Resolution Order）

### 什么是 MRO

MRO 是 Python 在多重继承中确定方法查找顺序的算法。Python 使用 C3 线性化算法计算 MRO，保证：

- 子类优先于父类
- 多个父类按定义顺序查找
- 单调性：子类的 MRO 不违反父类的 MRO

### C3 线性化算法

C3 算法的递归定义：

```
L[C] = C + merge(L[B1], L[B2], ..., [B1, B2, ...])
```

merge 的规则：

1. 取第一个列表的头部（第一个元素）
2. 如果该头部不出现在任何其他列表的尾部，则将其加入结果，并从所有列表中移除
3. 否则，跳到下一个列表的头部，重复步骤 2
4. 如果所有列表都为空，则完成；如果无法选择任何头部，则报错（不一致的继承关系）

### 示例

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# MRO:
# L[A] = [A, object]
# L[B] = [B] + merge(L[A], [A]) = [B, A, object]
# L[C] = [C] + merge(L[A], [A]) = [C, A, object]
# L[D] = [D] + merge(L[B], L[C], [B, C])
#       = [D] + merge([B, A, object], [C, A, object], [B, C])
#       = [D, B] + merge([A, object], [C, A, object], [C])
#       = [D, B, C] + merge([A, object], [A, object])
#       = [D, B, C, A, object]

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### 钻石继承问题

```
    object
      |
      A
     / \
    B   C
     \ /
      D
```

Python 的 C3 线性化保证 D 的 MRO 为 D -> B -> C -> A -> object，避免了经典 MRO 中 A 被优先于 C 访问的问题。

### 不合法的继承

```python
class X: pass
class Y(X): pass

class A(X, Y): pass  # TypeError: Cannot create a consistent MRO
# 因为 X 必须在 Y 之前（X 是 Y 的父类），但 A 的定义中 X 在 Y 之前
# 这违反了 Y 的 MRO 中 X 在 Y 之后的约束
```

---

## 元类（Metaclass）

### 什么是元类

元类是创建类的类。正如实例由类创建，类由元类创建。默认元类是 `type`。

```python
class MyClass:
    pass

# 等价于
MyClass = type("MyClass", (), {})
```

### type 的三参数形式

```python
type(name, bases, dict)
# name: 类名
# bases: 基类元组
# dict: 类属性字典

MyClass = type(
    "MyClass",
    (BaseClass,),
    {"x": 10, "method": lambda self: self.x}
)
```

### 自定义元类

```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        # 在类创建之前修改类定义
        print(f"Creating class {name}")
        namespace["class_id"] = id(mcs)
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

    def __init__(cls, name, bases, namespace):
        # 在类创建之后初始化
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        # 控制实例创建过程（类似单例模式）
        print(f"Creating instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=Meta):
    def __init__(self):
        self.value = 42
```

### 元类的执行顺序

当 Python 遇到 `class MyClass(metaclass=Meta):` 时：

1. 收集基类和类属性到 namespace
2. 调用 `Meta.__prepare__()` 创建 namespace（可选，返回自定义映射）
3. 调用 `Meta.__new__(mcs, name, bases, namespace)` 创建类对象
4. 调用 `Meta.__init__(cls, name, bases, namespace)` 初始化类对象
5. 类创建完成

### 元类的实际应用

1. **单例模式**

   ```python
   class SingletonMeta(type):
       _instances = {}
       def __call__(cls, *args, **kwargs):
           if cls not in cls._instances:
               cls._instances[cls] = super().__call__(*args, **kwargs)
           return cls._instances[cls]

   class Database(metaclass=SingletonMeta):
       pass
   ```

2. **注册模式** -- 自动注册子类

   ```python
   class PluginMeta(type):
       registry = {}
       def __init__(cls, name, bases, namespace):
           super().__init__(name, bases, namespace)
           if name != "Plugin":
               PluginMeta.registry[name] = cls

   class Plugin(metaclass=PluginMeta):
       pass
   ```

3. **接口验证** -- 检查子类是否实现了所有抽象方法
4. **ORM 映射** -- Django Model 的元类将字段定义转换为数据库映射
5. **API 框架** -- 自动收集路由和视图函数

### 元类 vs 类装饰器

| 特性     | 元类             | 类装饰器         |
| -------- | ---------------- | ---------------- |
| 作用时机 | 类创建时         | 类创建后         |
| 继承性   | 子类自动继承元类 | 子类不继承装饰器 |
| 复杂度   | 高               | 低               |
| 适用场景 | 框架级抽象       | 简单的类修改     |

优先使用类装饰器，仅在需要继承行为时使用元类。

---

## 理论速查表

| 概念     | 核心要点                                     | 关键细节                              |
| -------- | -------------------------------------------- | ------------------------------------- |
| GIL      | 全局解释器锁，同一时刻只有一个线程执行字节码 | CPU 密集用多进程，I/O 密集用多线程    |
| 字节码   | CPython 基于栈的虚拟机指令                   | `dis.dis()` 查看，`.pyc` 缓存         |
| 描述符   | `__get__`/`__set__`/`__delete__` 协议        | 数据描述符优先于实例属性              |
| MRO      | C3 线性化算法确定方法查找顺序                | `ClassName.__mro__` 查看              |
| 元类     | 创建类的类，默认为 `type`                    | `__new__` -> `__init__` -> `__call__` |
| 引用计数 | CPython 的主要 GC 机制                       | 循环引用由分代 GC 处理                |
| 名称修饰 | `__attr` 变为 `_ClassName__attr`             | 仅双下划线前缀触发，防止子类覆盖      |
| 协程     | async/await 基于生成器实现                   | 事件循环调度，非抢占式                |

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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Python 概述与环境配置 | 001-PythonOverviewEnvSetup | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 变量与常量 | 003-VariableConstant | 本文的并列主题 |
| Python 描述符协议：属性访问的底层机制与工程实践 | 004-PythonDescriptorProtocol | 本文的原理深化 |
| Python 基础数据类型：从对象模型到工程实践的深度解析 | 005-PythonBasicsDataTypeObjectModelPracticeDeepAnalysis | 本文的前置基础 |
| 协程与asyncio | 006-CoroutineAsyncio | 本文的并列主题 |
| 列表推导式进阶 | 007-ListComprehensionAdvanced | 本文的并列主题 |
| 运算符与表达式 | 008-OperatorExpression | 本文的并列主题 |
| Python与虚拟环境 | 009-PythonVirtualEnv | 本文的前置基础 |
| 元类 | 010-Metaclass | 本文的并列主题 |
| Python与SQLAlchemy | 011-PythonSQLAlchemy | 本文的并列主题 |
| 多进程与多线程 | 012-MultiprocessingMultithreading | 本文的并列主题 |
| Python与FastAPI | 013-PythonFastAPI | 本文的并列主题 |
| Python与Django | 014-PythonDjango | 本文的并列主题 |
| 数据类与Pydantic | 015-DataClassPydantic | 本文的并列主题 |
| Python与Redis | 016-PythonRedis | 本文的并列主题 |
| Python 与 Celery：分布式任务队列的设计、实现与工程实践 | 017-PythonCeleryDistributedTaskQueue | 本文的并列主题 |
| 控制流 | 018-ControlFlow | 本文的并列主题 |
| Python与Docker | 019-PythonDocker | 本文的并列主题 |
| Python与机器学习 | 020-PythonMachineLearning | 本文的并列主题 |
| Python与深度学习 | 021-PythonDeepLearning | 本文的并列主题 |
| Python与NLP | 022-PythonAndNLP | 本文的并列主题 |
| Python与计算机视觉 | 023-PythonComputerVision | 本文的并列主题 |
| Python与Web爬虫 | 024-WebScrapingWithPython | 本文的并列主题 |
| Python与自动化 | 025-PythonAutomationCookbook | 本文的并列主题 |
| 函数详解 | 026-FunctionDetailed | 本文的并列主题 |
| Python与日志 | 027-PythonLog | 本文的并列主题 |
| Python与加密 | 028-PythonAndCryptography | 本文的安全延伸 |
| Python与测试 | 029-PythonTest | 本文的并列主题 |
| Python 与配置管理：从环境变量到云原生动态配置的工程实践 | 030-Python | 本文的前置基础 |
| 装饰器 | 031-Decorator | 本文的并列主题 |
| Python与消息队列 | 032-PythonMessageQueue | 本文的并列主题 |
| Python与gRPC | 033-PythongRPC | 本文的并列主题 |
| Python与WebSocket | 034-PythonWebSocket | 本文的并列主题 |
| Python与CI-CD | 035-PythonCICD | 本文的并列主题 |
| Python与性能优化 | 036-PythonPerformance | 本文的性能延伸 |
| 内置数据结构 | 037-BuiltinDataStructure | 本文的并列主题 |
| 正则表达式 | 038-Regex | 本文的并列主题 |
| Python与CLI | 039-PythonCLI | 本文的并列主题 |
| Python与设计模式 | 040-PythonDesignPattern | 本文的并列主题 |
| Python与打包发布 | 041-ASurveyOfPythonPackagingPastPresentAndFuture | 本文的并列主题 |
| Python 与 Jupyter：交互式计算、数据分析与可复现研究 | 042-PythonJupyter | 本文的并列主题 |
| Python与GraphQL | 043-PythonGraphQL | 本文的并列主题 |
| Python与代码质量 | 044-PythonCodeQuality | 本文的并列主题 |
| 并发编程 | 045-ConcurrentProgramming | 本文的并列主题 |
| Python与数据库迁移 | 046-PythonDatabaseMigration | 本文的并列主题 |
| Python与OAuth2 | 047-PythonOAuth2 | 本文的并列主题 |
| Python与向量数据库 | 048-PythonVectorDatabase | 本文的并列主题 |
| Python 进阶与最新特性 | 049-PythonAdvancedLatestFeature | 本文的并列主题 |
| 推导式与生成器 | 050-ComprehensionGenerator | 本文的并列主题 |
| 模块、包与工程化 | 051-ModulePackageEngineering | 本文的并列主题 |
| 上下文管理器 | 052-ContextManager | 本文的并列主题 |
| 元类与单例模式 | 053-MetaclassSingleton | 本文的并列主题 |
| 异步编程详解 | 054-AsyncProgrammingDetailed | 本文的并列主题 |
| 弱引用 | 055-WeakReference | 本文的并列主题 |
| 打包与发布 | 056-PackagePublish | 本文的并列主题 |
| 描述符 | 057-Descriptor | 本文的并列主题 |
| 数据类与字段默认值 | 058-DataClassFieldDefault | 本文的并列主题 |
| 生成器与协程 | 059-GeneratorCoroutine | 本文的并列主题 |
| 类型注解与mypy | 060-TypeAnnotationMypy | 本文的并列主题 |
| 面向对象编程 | 061-OOP | 本文的并列主题 |
| 装饰器进阶 | 062-DecoratorAdvanced | 本文的并列主题 |
| 异常处理 | 063-ExceptionHandling | 本文的并列主题 |
| 文件 I/O 与上下文管理器 | 064-FileIOContextManager | 本文的并列主题 |
| Python 项目示例：网页爬虫与数据分析 | 065-PythonProjectExampleWebCrawlerDataAnalysis | 本文的综合应用 |
| Python 理论知识点 | 066-PythonTheoryKnowledge | 本文自身 |
| 基础数据类型 | 067-BasicDataType | 本文的前置基础 |
| Python 面向对象基础 | 068-COOPBasics | 本文的前置基础 |
| Python 面向对象进阶 | 069-COOPAdvanced | 本文的并列主题 |
| Python pathlib 路径操作 | 070-Pathlib | 本文的并列主题 |
| Python itertools 迭代工具 | 071-Itertools | 本文的并列主题 |
| Python functools 函数工具 | 072-Functools | 本文的并列主题 |
| Python datetime 与 time | 073-DatetimeTime | 本文的并列主题 |
| Python 序列化 JSON/CSV/Pickle | 074-SerializationJsonCsvPickle | 本文的并列主题 |
| Python 网络编程 socket/http | 075-NetworkSocketHttp | 本文的并列主题 |
| Python sys/os 平台接口 | 076-SysOsPlatform | 本文的并列主题 |
| Python math/random/statistics | 077-MathRandomStatistics | 本文的并列主题 |
| Python subprocess 子进程 | 078-Subprocess | 本文的并列主题 |
| Python logging 日志配置 | 079-Logging | 本文的并列主题 |
| Python 测试 unittest/pytest | 080-UnittestPytest | 本文的并列主题 |
| Python 字符串格式化与方法 | 081-StringFormattingMethods | 本文的并列主题 |
| Python argparse 命令行参数解析 | 082-ArgparseCli | 本文的并列主题 |
| Python typing 进阶 | 083-TypingAdvanced | 本文的并列主题 |
| Python enum 枚举 | 084-Enum | 本文的并列主题 |
| Python hashlib 与 hmac | 085-HashlibHmac | 本文的并列主题 |
| Python ssl 安全套接字 | 086-SslCrypto | 本文的安全延伸 |
| Python http.client HTTP 客户端 | 087-HttpClient | 本文的并列主题 |
| Python sqlite3 数据库 | 088-Sqlite3 | 本文的并列主题 |
| Python zipfile 与 tarfile | 089-ZipfileTarfile | 本文的并列主题 |
| Python array 与 bisect | 090-ArrayBisect | 本文的并列主题 |
| Python 字符串与文本处理 | 091-StringText | 本文的并列主题 |
| Python decimal 与 fractions | 092-DecimalFractions | 本文的并列主题 |
| Python shutil 与 tempfile | 093-ShutilTempfile | 本文的并列主题 |
| Python gc inspect dis | 094-GcInspect | 本文的并列主题 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
