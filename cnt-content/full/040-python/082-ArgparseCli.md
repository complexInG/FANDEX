---
order: 820
title: Python argparse 命令行参数解析
module: python

category: '040-python'
difficulty: beginner
description: Python argparse 命令行参数解析 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ArgumentParser 创建解析器

**基本写法：创建解析器**
`argparse.ArgumentParser([description=<描述>])`
```python
# 创建参数解析器
import argparse
parser = argparse.ArgumentParser(description="数据处理工具")
args = parser.parse_args()
```

**基本写法：完整构造参数**
`ArgumentParser(prog=<名称>, description=<描述>, epilog=<结尾说明>)`
```python
# 自定义程序名、描述与结尾说明
parser = argparse.ArgumentParser(
    prog="myapp",
    description="图片处理 CLI",
    epilog="示例: myapp resize --size 100",
)
```

**基本写法：运行并获取参数**
`<解析器>.parse_args()`
```python
# 解析命令行参数为命名空间对象
args = parser.parse_args()
print(args.filename)
```

---

## add_argument 添加参数

**基本写法：位置参数**
`<解析器>.add_argument(<参数名>)`
```python
# 必填位置参数
parser.add_argument("filename")
# 运行：python app.py data.txt
args = parser.parse_args()
print(args.filename)  # data.txt
```

**基本写法：可选参数**
`<解析器>.add_argument("-<短>", "--<长>")`
```python
# 带 - 前缀的可选参数
parser.add_argument("-v", "--verbose", help="详细输出")
# 运行：python app.py --verbose yes
```

**基本写法：指定类型**
`<解析器>.add_argument(<名>, type=<类型>)`
```python
# 自动类型转换
parser.add_argument("--count", type=int, default=1)
parser.add_argument("--rate", type=float)
```

**基本写法：默认值**
`<解析器>.add_argument(<名>, default=<默认值>)`
```python
# 未提供时使用默认值
parser.add_argument("--mode", default="auto")
```

**基本写法：限定取值**
`<解析器>.add_argument(<名>, choices=<列表>)`
```python
# 限制参数取值范围
parser.add_argument("--log", choices=["debug", "info", "error"])
```

**基本写法：必填可选参数**
`<解析器>.add_argument(<名>, required=True)`
```python
# 标记可选参数为必填
parser.add_argument("--config", required=True)
```

**基本写法：帮助文本**
`<解析器>.add_argument(<名>, help=<说明>)`
```python
# 提供 --help 时显示的说明
parser.add_argument("path", help="目标文件路径")
```

---

## nargs 多值参数

**基本写法：接收多个值**
`<解析器>.add_argument(<名>, nargs=<数量>)`
```python
# 指定接收 N 个值
parser.add_argument("--coords", nargs=2, type=float)  # 接收 2 个
```

**基本写法：可变数量**
`nargs="?" / "*" / "+"`
```python
# ? 零或一，* 零或多，+ 一或多
parser.add_argument("files", nargs="+", help="至少一个文件")
parser.add_argument("--opt", nargs="?", const="x", default="y")
```

**基本写法：收集剩余所有参数**
`nargs=argparse.REMAINDER`
```python
# 收集剩余参数传给子命令
parser.add_argument("cmd", nargs=argparse.REMAINDER)
```

---

## action 参数行为

**基本写法：布尔开关**
`action="store_true" / "store_false"`
```python
# 标志位，出现即 True / False
parser.add_argument("--dry-run", action="store_true")
parser.add_argument("--no-cache", action="store_false", dest="cache")
```

**基本写法：计数**
`action="count"`
```python
# 统计出现次数（如 -vvv 表示级别 3）
parser.add_argument("-v", action="count", default=0)
```

**基本写法：追加到列表**
`action="append"`
```python
# 重复参数追加为列表
parser.add_argument("--tag", action="append")
# 运行 --tag a --tag b => ['a', 'b']
```

**基本写法：追加字面值**
`action="append_const"`
```python
# 追加常量值到列表
parser.add_argument("--debug", action="append_const", const="debug")
```

---

## 子命令 subparsers

**换行写法：定义子命令**
`<解析器>.add_subparsers(dest=<字段>, required=True)`
```python
# 实现 git 风格子命令
sub = parser.add_subparsers(dest="cmd", required=True)

commit = sub.add_parser("commit", help="提交")
commit.add_argument("-m", "--message", required=True)

push = sub.add_parser("push", help="推送")
push.add_argument("--force", action="store_true")
```

**基本写法：绑定子命令处理函数**
`<子解析器>.set_defaults(func=<函数>)`
```python
# 为每个子命令绑定处理函数
def do_commit(args):
    print(f"提交: {args.message}")

commit.set_defaults(func=do_commit)

args = parser.parse_args()
args.func(args)
```

---

## 互斥参数组

**基本写法：互斥组**
`<解析器>.add_mutually_exclusive_group()`
```python
# 组内参数不能同时出现
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", action="store_true")
group.add_argument("--quiet", action="store_true")
```

**基本写法：必填互斥组**
`add_mutually_exclusive_group(required=True)`
```python
# 必须从互斥组中选一个
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--input")
group.add_argument("--from-stdin", action="store_true")
```

---

## 参数组与元信息

**基本写法：参数分组**
`<解析器>.add_argument_group(<组标题>)`
```python
# 在帮助信息中分组显示
db_group = parser.add_argument_group("数据库选项")
db_group.add_argument("--host")
db_group.add_argument("--port", type=int)
```

**基本写法：自定义参数显示名**
`<解析器>.add_argument(<名>, metavar=<显示名>)`
```python
# 在帮助信息中显示为自定义名
parser.add_argument("--input", metavar="FILE")
```

**基本写法：指定存储属性名**
`<解析器>.add_argument(<名>, dest=<属性名>)`
```python
# 将参数值绑定到自定义属性名
parser.add_argument("--rate", dest="speed")
print(args.speed)
```

---

## 文件类型参数

**基本写法：文件参数**
`type=argparse.FileType(<模式>)`
```python
# 自动打开文件并传入文件对象
parser.add_argument("--out", type=argparse.FileType("w"))
parser.add_argument("infile", type=argparse.FileType("r", encoding="utf-8"))
args = parser.parse_args()
args.out.write("done")
args.infile.close()
```

---

## 自定义类型转换

**基本写法：自定义 type 函数**
`type=<转换函数>`
```python
# 通过函数实现自定义转换
def hex_int(s):
    return int(s, 16)

parser.add_argument("--color", type=hex_int)
# 运行：--color ff => 255
```

**基本写法：正则校验**
`type=<校验函数>`
```python
# 校验失败抛 argparse.ArgumentTypeError
import re
def email(s):
    if not re.match(r"^[\w.]+@[\w.]+$", s):
        raise argparse.ArgumentTypeError("非法邮箱")
    return s

parser.add_argument("--email", type=email)
```

---

## 自定义动作

**换行写法：自定义 Action**
`class <动作>(argparse.Action):`
```python
# 通过子类化实现复杂参数处理
class UpperAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.upper())

parser.add_argument("--name", action=UpperAction)
```

---

## 错误处理与帮助

**基本写法：自定义错误处理**
`<解析器>.error(<消息>)`
```python
# 触发错误并退出
args = parser.parse_args()
if args.port < 0:
    parser.error("端口不能为负数")
```

**基本写法：禁止缩写匹配**
`ArgumentParser(allow_abbrev=False)`
```python
# 禁止 --ver 自动匹配 --verbose
parser = argparse.ArgumentParser(allow_abbrev=False)
```

**基本写法：formatter_class 控制帮助格式**
`ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)`
```python
# 保留 description 中的原始格式
parser = argparse.ArgumentParser(
    description="多行说明\n第二行",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
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
