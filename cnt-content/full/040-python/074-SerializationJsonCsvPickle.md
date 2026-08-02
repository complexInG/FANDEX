---
order: 740
title: Python 序列化 JSON/CSV/Pickle
module: 'python'
category: 后端技术
difficulty: beginner
description: Python 序列化 JSON/CSV/Pickle 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## json 序列化

**基本写法：对象转 JSON 字符串**
`json.dumps(<对象>)`
```python
# 将 Python 对象转为 JSON 字符串
import json
data = {"name": "Tom", "age": 18}
s = json.dumps(data)  # '{"name": "Tom", "age": 18}'
```

**基本写法：格式化输出**
`json.dumps(<对象>, indent=<缩进>, ensure_ascii=<布尔>)`
```python
# 缩进美化并保留中文字符
print(json.dumps(data, indent=2, ensure_ascii=False))
```

**基本写法：JSON 字符串转对象**
`json.loads(<字符串>)`
```python
# 将 JSON 字符串解析为 Python 对象
obj = json.loads('{"name": "Tom"}')
print(obj["name"])  # Tom
```

**基本写法：写入文件**
`json.dump(<对象>, <文件对象>)`
```python
# 将对象序列化写入文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

**基本写法：从文件读取**
`json.load(<文件对象>)`
```python
# 从文件读取并解析 JSON
with open("data.json", encoding="utf-8") as f:
    obj = json.load(f)
```

**基本写法：排序键输出**
`json.dumps(<对象>, sort_keys=True)`
```python
# 按键名排序输出
print(json.dumps({"b": 1, "a": 2}, sort_keys=True))
```

**基本写法：自定义序列化**
`json.dumps(<对象>, default=<函数>)`
```python
# 自定义非内置类型的序列化逻辑
from datetime import datetime
def default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError

print(json.dumps({"t": datetime.now()}, default=default))
```

**基本写法：自定义反序列化**
`json.loads(<字符串>, object_hook=<函数>)`
```python
# 解析时转换字典结构
def as_date(d):
    if "date" in d:
        return d["date"]
    return d

obj = json.loads('{"date": "2024-01-01"}', object_hook=as_date)
```

**基本写法：JSONEncoder 子类**
`class <类>(json.JSONEncoder):`
```python
# 通过子类化编码器统一处理类型
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return super().default(o)

print(json.dumps({1, 2}, cls=MyEncoder))
```

---

## csv 读写

**基本写法：写入 CSV**
`csv.writer(<文件对象>)`
```python
# 写入 CSV 文件
import csv
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["name", "age"])
    w.writerow(["Tom", 18])
```

**基本写法：读取 CSV**
`csv.reader(<文件对象>)`
```python
# 读取 CSV 文件内容
with open("data.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['name', 'age']
```

**基本写法：字典方式写入**
`csv.DictWriter(<文件对象>, fieldnames=<字段列表>)`
```python
# 按字典结构写入
fields = ["name", "age"]
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerow({"name": "Tom", "age": 18})
```

**基本写法：字典方式读取**
`csv.DictReader(<文件对象>)`
```python
# 按字典结构读取
with open("data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])  # Tom
```

**基本写法：指定分隔符与引号**
`csv.writer(<文件>, delimiter=<分隔符>, quotechar=<引号字符>)`
```python
# 自定义分隔符（如 TSV 制表符分隔）
with open("data.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["a", "b"])
```

**基本写法：处理空值与方言**
`csv.register_dialect(<名称>, **<参数>)`
```python
# 注册自定义方言复用配置
csv.register_dialect("pipes", delimiter="|")
with open("data.txt", "w", newline="") as f:
    w = csv.writer(f, dialect="pipes")
    w.writerow(["a", "b"])
```

---

## pickle 序列化

**基本写法：对象转字节串**
`pickle.dumps(<对象>)`
```python
# 将任意 Python 对象序列化为字节
import pickle
data = {"name": "Tom", "list": [1, 2, 3]}
b = pickle.dumps(data)
```

**基本写法：字节串转对象**
`pickle.loads(<字节串>)`
```python
# 从字节反序列化为 Python 对象
obj = pickle.loads(b)
print(obj["name"])  # Tom
```

**基本写法：写入文件**
`pickle.dump(<对象>, <文件对象>)`
```python
# 序列化对象到文件
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

**基本写法：从文件读取**
`pickle.load(<文件对象>)`
```python
# 从文件反序列化对象
with open("data.pkl", "rb") as f:
    obj = pickle.load(f)
```

**基本写法：指定协议版本**
`pickle.dump(<对象>, <文件>, protocol=<版本>)`
```python
# 使用高版本协议提升效率
with open("data.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
```

**基本写法：批量序列化**
`pickle.dump + 循环`
```python
# 多次调用 dump 可写入多个对象
with open("data.pkl", "wb") as f:
    for item in [obj1, obj2, obj3]:
        pickle.dump(item, f)

# 读取时循环 load 直到 EOFError
with open("data.pkl", "rb") as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break
```

---

## shelve 持久化字典

**基本写法：打开 shelve 数据库**
`shelve.open(<文件名>)`
```python
# 像字典一样持久化存储对象
import shelve
db = shelve.open("mydb")
db["user"] = {"name": "Tom", "age": 18}
print(db["user"]["name"])  # Tom
db.close()
```

**基本写法：上下文管理**
`with shelve.open(<文件名>) as <变量>:`
```python
# 使用 with 自动关闭
with shelve.open("mydb") as db:
    db["key"] = "value"
    for k in db:
        print(k, db[k])
```

**基本写法：写回模式**
`shelve.open(<文件名>, writeback=True)`
```python
# 启用写回，修改可变值时自动同步
with shelve.open("mydb", writeback=True) as db:
    db["list"].append("new")  # 直接修改生效
```

---

## msgpack 与 orjson（高性能扩展）

**基本写法：orjson 高速序列化**
`orjson.dumps(<对象>)`
```python
# orjson 性能远高于标准 json（返回字节）
import orjson
b = orjson.dumps(data, option=orjson.OPT_INDENT_2)
obj = orjson.loads(b)
```

**基本写法：orjson 保留中文**
`orjson.dumps(<对象>, option=orjson.OPT_NON_STR_KEYS)`
```python
# orjson 默认即返回 UTF-8 字节，无需 ensure_ascii
import orjson
print(orjson.dumps({"名": "Tom"}))  # b'{"name":"Tom"}'
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
