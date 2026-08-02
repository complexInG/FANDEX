---
order: 880
title: Python sqlite3 数据库
module: 'python'
category: 后端技术
difficulty: beginner
description: Python sqlite3 数据库 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 连接数据库

**基本写法：连接数据库**
`sqlite3.connect(<数据库文件>)`
```python
# 连接 SQLite 数据库
import sqlite3

conn = sqlite3.connect("example.db")
# 内存数据库
conn_mem = sqlite3.connect(":memory:")
```

**基本写法：关闭连接**
`conn.close()`
```python
# 关闭连接
conn.close()
```

**基本写法：with 自动提交**
`with conn:`
```python
# with 块结束自动提交事务
with conn:
    conn.execute("INSERT INTO users VALUES (1, 'Alice')")
```

---

## 游标操作

**基本写法：创建游标**
`conn.cursor()`
```python
# 创建游标对象
cur = conn.cursor()
```

**基本写法：执行 SQL**
`cur.execute(<SQL>, <参数>)`
```python
# 执行单条 SQL（参数化查询）
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Alice"))
conn.commit()
```

**基本写法：批量执行**
`cur.executemany(<SQL>, <参数序列>)`
```python
# 批量插入
data = [(2, "Bob"), (3, "Carol")]
cur.executemany("INSERT INTO users (id, name) VALUES (?, ?)", data)
conn.commit()
```

**基本写法：执行脚本**
`cur.executescript(<SQL 脚本>)`
```python
# 执行多语句脚本
cur.executescript("""
CREATE TABLE IF NOT EXISTS logs (msg TEXT);
INSERT INTO logs VALUES ('init');
""")
```

---

## 查询结果

**基本写法：fetchone 取一条**
`cur.fetchone()`
```python
# 获取一条结果
cur.execute("SELECT * FROM users")
print(cur.fetchone())
```

**基本写法：fetchall 取全部**
`cur.fetchall()`
```python
# 获取全部结果
cur.execute("SELECT * FROM users")
print(cur.fetchall())
```

**基本写法：fetchmany 取多条**
`cur.fetchmany(<数量>)`
```python
# 获取指定数量结果
cur.execute("SELECT * FROM users")
print(cur.fetchmany(2))
```

**基本写法：迭代查询结果**
`for row in cur:`
```python
# 迭代结果
cur.execute("SELECT * FROM users")
for row in cur:
    print(row)
```

---

## Row 行工厂

**基本写法：Row 对象访问**
`conn.row_factory = sqlite3.Row`
```python
# 使用 Row 工厂按列名访问
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT * FROM users")
row = cur.fetchone()
print(row["name"], row["id"])
```

---

## 事务与隔离级别

**基本写法：设置隔离级别**
`sqlite3.connect(<文件>, isolation_level=<级别>)`
```python
# 隔离级别：None/DEFERRED/IMMEDIATE/EXCLUSIVE
conn = sqlite3.connect("example.db", isolation_level="DEFERRED")
```

**基本写法：手动提交**
`conn.commit()`
```python
# 提交事务
conn.commit()
```

**基本写法：回滚**
`conn.rollback()`
```python
# 回滚事务
conn.rollback()
```

---

## 参数化查询

**基本写法：问号占位符**
`cur.execute(<SQL>, (<参数1>, <参数2>))`
```python
# 使用 ? 占位符（推荐）
cur.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
```

**基本写法：命名占位符**
`cur.execute(<SQL>, {<名>: <值>})`
```python
# 使用 :name 命名占位符
cur.execute("SELECT * FROM users WHERE name = :name", {"name": "Alice"})
```

---

## 类型转换

**基本写法：注册适配器**
`sqlite3.register_adapter(<Python 类型>, <函数>)`
```python
# 自定义类型适配
import sqlite3
from datetime import date

sqlite3.register_adapter(date, lambda d: d.isoformat())
```

**基本写法：注册转换器**
`sqlite3.register_converter(<类型名>, <函数>)`
```python
# 自定义类型转换
sqlite3.register_converter("DATE", lambda b: date.fromisoformat(b.decode()))

conn = sqlite3.connect("db", detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute("CREATE TABLE events (d DATE)")
cur.execute("INSERT INTO events VALUES (?)", (date(2024, 1, 1),))
cur.execute("SELECT d FROM events")
print(type(cur.fetchone()[0]))  # <class 'datetime.date'>
```

---

## 上下文管理

**基本写法：连接作为上下文管理器**
`with conn:`
```python
# 自动提交或回滚
with conn:
    conn.execute("INSERT INTO users VALUES (1, 'Alice')")
```

**基本写法：游标作为上下文管理器**
`with conn.cursor() as cur:`
```python
# 自动关闭游标
with conn.cursor() as cur:
    cur.execute("SELECT * FROM users")
    print(cur.fetchall())
```

---

## 命令行接口（3.12+）

**基本写法：CLI 执行**
`python -m sqlite3 <数据库> <SQL>`
```python
# 命令行执行 SQL
# python -m sqlite3 example.db "SELECT * FROM users"
```

---

## 元数据查询

**基本写法：lastrowid**
`cur.lastrowid`
```python
# 获取最后插入行的 ID
cur.execute("INSERT INTO users (name) VALUES (?)", ("Dave",))
print(cur.lastrowid)
```

**基本写法：rowcount**
`cur.rowcount`
```python
# 获取影响的行数
cur.execute("DELETE FROM users WHERE id = ?", (1,))
print(cur.rowcount)
```

**基本写法：表结构**
`cur.execute("PRAGMA table_info(<表名>)")`
```python
# 查询表结构
cur.execute("PRAGMA table_info(users)")
for col in cur.fetchall():
    print(col)
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
