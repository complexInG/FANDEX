---
order: 780
title: Python subprocess 子进程
module: 'python'
category: 后端技术
difficulty: beginner
description: Python subprocess 子进程 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## subprocess.run 推荐用法

**基本写法：执行命令**
`subprocess.run([<命令>, <参数1>, <参数2>])`
```python
# 以列表形式执行命令（推荐，避免注入）
import subprocess
result = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result.stdout)  # hello
```

**基本写法：捕获输出**
`subprocess.run(<命令>, capture_output=True, text=True)`
```python
# 捕获标准输出与错误输出
r = subprocess.run(["python", "-V"], capture_output=True, text=True)
print(r.stdout, r.stderr)
```

**基本写法：字符串命令（shell 模式）**
`subprocess.run(<命令字符串>, shell=True)`
```python
# 使用 shell 解析管道与通配符
r = subprocess.run("dir | findstr py", shell=True, capture_output=True, text=True)
```

**基本写法：检查返回码**
`subprocess.run(<命令>, check=True)`
```python
# 非零返回码抛出 CalledProcessError
try:
    subprocess.run(["false"], check=True)
except subprocess.CalledProcessError as e:
    print(f"命令失败: {e.returncode}")
```

**基本写法：设置工作目录**
`subprocess.run(<命令>, cwd=<目录>)`
```python
# 指定子进程工作目录
subprocess.run(["ls"], cwd="/tmp", capture_output=True, text=True)
```

**基本写法：设置环境变量**
`subprocess.run(<命令>, env=<环境字典>)`
```python
# 自定义子进程环境变量
import os
env = {**os.environ, "DEBUG": "1"}
subprocess.run(["python", "main.py"], env=env)
```

**基本写法：设置超时**
`subprocess.run(<命令>, timeout=<秒数>)`
```python
# 超时抛出 TimeoutExpired
try:
    subprocess.run(["sleep", "10"], timeout=3)
except subprocess.TimeoutExpired:
    print("执行超时")
```

**基本写法：传入输入**
`subprocess.run(<命令>, input=<字符串>, text=True)`
```python
# 通过 stdin 传入输入
r = subprocess.run(["python", "-c", "print(input()*2)"], input="ab", text=True, capture_output=True)
print(r.stdout)  # abab
```

**基本写法：输入输出编码**
`subprocess.run(<命令>, encoding=<编码>)`
```python
# 指定编码替代 text=True
r = subprocess.run(["echo", "中文"], encoding="utf-8", capture_output=True)
```

---

## Popen 进程对象

**基本写法：创建子进程**
`subprocess.Popen([<命令>, <参数>])`
```python
# 获取进程对象进行交互
p = subprocess.Popen(["python", "-u", "task.py"], stdout=subprocess.PIPE, text=True)
out = p.communicate()[0]
print(out)
```

**基本写法：管道通信**
`<进程>.communicate([input=<输入>])`
```python
# 一次性读取全部输出并等待结束
p = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
out, err = p.communicate(input="hello")
print(out)  # hello
```

**基本写法：等待进程结束**
`<进程>.wait([timeout=<秒>])`
```python
# 阻塞等待子进程退出
p = subprocess.Popen(["sleep", "2"])
p.wait()
print("进程已结束")
```

**基本写法：轮询状态**
`<进程>.poll()`
```python
# 非阻塞检查是否结束
p = subprocess.Popen(["sleep", "2"])
while p.poll() is None:
    print("运行中")
```

**基本写法：终止进程**
`<进程>.terminate() / <进程>.kill()`
```python
# terminate 发送 SIGTERM，kill 发送 SIGKILL
p = subprocess.Popen(["sleep", "100"])
p.terminate()
```

**基本写法：获取进程号**
`<进程>.pid`
```python
# 获取子进程 PID
p = subprocess.Popen(["sleep", "1"])
print(p.pid)
```

---

## 管道串联

**基本写法：命令管道串联**
`Popen(stdout=Popen.stdin)`
```python
# 模拟 shell 管道：ps | grep python
p1 = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(["grep", "python"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()
out = p2.communicate()[0]
print(out)
```

---

## check_output / call / check_call

**基本写法：获取标准输出**
`subprocess.check_output(<命令>)`
```python
# 直接返回标准输出，失败抛异常
out = subprocess.check_output(["python", "-V"], text=True, stderr=subprocess.STDOUT)
print(out)
```

**基本写法：仅执行并取返回码**
`subprocess.call(<命令>)`
```python
# 返回退出码，不抛异常
code = subprocess.call(["ls", "-l"])
```

**基本写法：执行并校验**
`subprocess.check_call(<命令>)`
```python
# 返回码非零抛 CalledProcessError
subprocess.check_call(["echo", "ok"])
```

---

## 输入输出重定向

**基本写法：输出重定向到文件**
`subprocess.run(<命令>, stdout=<文件对象>)`
```python
# 将输出写入文件
with open("out.log", "w", encoding="utf-8") as f:
    subprocess.run(["python", "-V"], stdout=f)
```

**基本写法：合并标准错误到标准输出**
`subprocess.run(<命令>, stderr=subprocess.STDOUT)`
```python
# 合并 stderr 到 stdout 一起捕获
r = subprocess.run(["python", "err.py"], capture_output=True, stderr=subprocess.STDOUT, text=True)
print(r.stdout)
```

**基本写法：从文件输入**
`subprocess.run(<命令>, stdin=<文件对象>)`
```python
# 从文件读取 stdin
with open("input.txt", encoding="utf-8") as f:
    subprocess.run(["python", "process.py"], stdin=f)
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
