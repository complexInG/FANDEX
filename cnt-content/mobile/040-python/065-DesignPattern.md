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
