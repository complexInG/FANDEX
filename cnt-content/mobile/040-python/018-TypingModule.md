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
