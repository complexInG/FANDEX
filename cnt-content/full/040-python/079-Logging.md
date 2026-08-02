---
order: 790
title: Python logging 日志配置
module: 'python'
category: 后端技术
difficulty: beginner
description: Python logging 日志配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## 基础配置

**基本写法：快速配置**
`logging.basicConfig(level=<级别>)`
```python
# 一行配置根 logger 输出级别
import logging
logging.basicConfig(level=logging.DEBUG)
logging.info("启动服务")
```

**基本写法：带格式与文件**
`logging.basicConfig(filename=<文件>, format=<格式>, level=<级别>)`
```python
# 输出到文件并定义格式
logging.basicConfig(
    filename="app.log",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
```

**基本写法：获取命名 logger**
`logging.getLogger(<名称>)`
```python
# 每个模块使用独立 logger 便于追踪
logger = logging.getLogger(__name__)
logger.warning("模块警告")
```

---

## 日志级别

**基本写法：各级别日志**
`logger.<级别>(<消息>)`
```python
# 从低到高五个级别
logger.debug("调试详情")
logger.info("一般信息")
logger.warning("警告")
logger.error("错误")
logger.critical("严重错误")
```

**基本写法：自定义级别**
`logging.addLevelName(<数值>, <名称>)`
```python
# 注册自定义日志级别
TRACE = 5
logging.addLevelName(TRACE, "TRACE")
logger.log(TRACE, "追踪信息")
```

**基本写法：按级别输出**
`logger.log(<级别>, <消息>)`
```python
# 动态指定级别
logger.log(logging.ERROR, "动态级别错误")
```

---

## Handler 输出目标

**基本写法：控制台输出**
`logging.StreamHandler()`
```python
# 添加控制台处理器
import sys
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
logger.addHandler(console)
```

**基本写法：文件输出**
`logging.FileHandler(<文件>)`
```python
# 日志写入指定文件
fh = logging.FileHandler("app.log", encoding="utf-8")
fh.setLevel(logging.INFO)
logger.addHandler(fh)
```

**基本写法：按大小滚动**
`logging.handlers.RotatingFileHandler(<文件>, maxBytes=<字节>, backupCount=<份数>)`
```python
# 单文件超限后自动轮转
from logging.handlers import RotatingFileHandler
rh = RotatingFileHandler("app.log", maxBytes=10 * 1024 * 1024, backupCount=5)
logger.addHandler(rh)
```

**基本写法：按时间滚动**
`logging.handlers.TimedRotatingFileHandler(<文件>, when=<周期>, backupCount=<份数>)`
```python
# 按时间周期切割日志
from logging.handlers import TimedRotatingFileHandler
th = TimedRotatingFileHandler("app.log", when="midnight", backupCount=7)
logger.addHandler(th)
```

---

## Formatter 格式化

**基本写法：定义格式器**
`logging.Formatter(<格式字符串>)`
```python
# 设置日志显示格式
fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
fh.setFormatter(fmt)
logger.addHandler(fh)
```

**基本写法：常用字段**
`%(asctime)s %(name)s %(levelname)s %(message)s`
```python
# 常用格式字段说明
# asctime 时间 | name logger 名 | levelname 级别
# filename 文件名 | lineno 行号 | funcName 函数名
fmt = logging.Formatter("%(filename)s:%(lineno)d %(message)s")
```

---

## 异常日志

**基本写法：记录异常堆栈**
`logger.exception(<消息>)`
```python
# 在 except 中输出完整堆栈
try:
    1 / 0
except ZeroDivisionError:
    logger.exception("除零异常")
```

**基本写法：exc_info 参数**
`logger.error(<消息>, exc_info=True)`
```python
# 任意级别附加异常信息
try:
    open("missing.txt")
except FileNotFoundError:
    logger.error("文件不存在", exc_info=True)
```

---

## dictConfig 字典配置

**换行写法：字典配置**
`logging.config.dictConfig(<配置字典>)`
```python
# 集中化配置多 handler 与 logger
import logging.config
config = {
    "version": 1,
    "formatters": {"simple": {"format": "%(asctime)s %(message)s"}},
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
logging.config.dictConfig(config)
```

---

## 禁用与过滤

**基本写法：禁用日志**
`logging.disable(<级别>)`
```python
# 禁用指定级别及以下日志
logging.disable(logging.DEBUG)  # 关闭 DEBUG
```

**基本写法：按级别过滤**
`logging.Filter`
```python
# 自定义过滤器
class LevelFilter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.WARNING

logger.addFilter(LevelFilter())
```

---

## 模块化 logger 最佳实践

**基本写法：模块级 logger**
`logger = logging.getLogger(__name__)`
```python
# 每个 Python 文件顶部声明 logger
# mymodule.py
import logging
logger = logging.getLogger(__name__)

def do_work():
    logger.info("开始处理")
```

**基本写法：设置第三方库日志级别**
`logging.getLogger(<库名>).setLevel(<级别>)`
```python
# 抑制第三方库的过多日志
logging.getLogger("urllib3").setLevel(logging.WARNING)
```

**基本写法：禁止传播**
`logger.propagate = False`
```python
# 防止日志向父 logger 重复输出
logger.propagate = False
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
