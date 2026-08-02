---
order: 950
title: Python traceback 与 warnings
module: 'python'
category: 后端技术
difficulty: beginner
description: Python traceback 与 warnings 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
