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