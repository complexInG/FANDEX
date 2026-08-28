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