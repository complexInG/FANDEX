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
