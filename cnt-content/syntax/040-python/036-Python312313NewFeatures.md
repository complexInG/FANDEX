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