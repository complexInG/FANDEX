---
order: 90
title: 'Python 进阶与最新特性'
module: python
category: 'Python Advanced'
difficulty: advanced
description: 'Python 3.12-3.14 新特性、dataclass/attrs、asyncio 进阶、类型系统、Pydantic v2、FastAPI 与现代工具链。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'python/Python与WebSocket-2'
  - python/Python与向量数据库
  - python/推导式与生成器
  - 'python/模块-包与工程化'
prerequisites:
  - python/语法速查
---

## 1. Python 3.12-3.14 新特性

Python 近年来的版本迭代显著提升了语言表达力、运行性能和类型安全。

### 1.1 Python 3.12 关键特性

**改进的错误消息**：Python 3.12 提供了更精确的错误提示，尤其在导入错误和拼写错误方面：

```python
# 之前
# ImportError: cannot import name 'datacalss' from 'dataclasses'

# Python 3.12
# ImportError: cannot import name 'datacalss' from 'dataclasses';
# did you mean: 'dataclass'?

import datacalss  # ModuleNotFoundError: No module named 'datacalss';
                   # did you mean: 'dataclasses'?
```

**Type Parameter 语法（PEP 695）**：全新的泛型类型参数声明语法：

```python
# Python 3.12 之前 —— 需要手动声明 TypeVar
from typing import TypeVar, Generic

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Python 3.12 —— 使用 type 语法
class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# 类型别名也简化了
type Point = tuple[float, float]
type Matrix = list[list[float]]

# 泛型函数
def first[T](items: list[T]) -> T:
    return items[0]

# 带约束的类型参数
class Numeric[T: (int, float)]:
    value: T
```

**f-string 改进（PEP 701）**：f-string 不再有限制，可以嵌套引号、注释和多行表达式：

```python
# 嵌套相同引号
greeting = f"Hello, {f"world {name}"}!"

# f-string 中使用注释
result = f"""
    计算结果: {
        x + y  # 这是注释
    }
"""

# f-string 中使用反斜杠
paths = f"路径: {'\\'.join(['home', 'user', 'docs'])}"
```

### 1.2 Python 3.13 关键特性

**Faster CPython 项目**：Python 3.13 继续推进性能优化，包括：

- 优化了 `int` 的实现，大整数运算更快
- `comprehension` 内联优化
- 实验性的 JIT 编译器（copy-and-patch JIT）

```python
# JIT 编译器需要显式启用
# python -X jit myscript.py

# 或通过环境变量
# PYTHON_JIT=1 python myscript.py
```

**自由线程模式（Free-threaded / No-GIL）**：Python 3.13 引入了实验性的自由线程构建，允许禁用 GIL：

```bash
# 安装自由线程版本
# Windows: 官方安装包选择 "free-threaded" 选项
# Linux: sudo apt install python3.13-nogil

# 验证是否为自由线程版本
python -c "import sys; print(sys._is_gil_enabled())"  # False

# 运行自由线程 Python
python3.13t myscript.py
```

```python
# 自由线程下的真正并行
import threading
import time

def cpu_work(n: int) -> int:
    """CPU 密集型计算"""
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    start = time.perf_counter()

    threads = []
    for _ in range(4):
        t = threading.Thread(target=cpu_work, args=(5_000_000,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"并行耗时: {time.perf_counter() - start:.2f}s")
    # GIL 模式: ~4s (串行执行)
    # 自由线程: ~1.2s (真正并行)
```

**改进的交互式解释器**：基于 PyREPL 的新 REPL，支持多行编辑、语法高亮和历史浏览。

**弃用和移除**：移除了大量已弃用的标准库模块（如 `aifc`、`cgi`、`imghdr` 等）。

### 1.3 Python 3.14 前瞻

Python 3.14 预计在 2025 年 10 月发布，关键特性包括：

- **延迟求值的注解（PEP 649）**：`annotations` 默认延迟求值，解决前向引用问题
- **Template Strings（PEP 750）**：新的字符串模板机制
- **改进的 `ast` 模块**：更高效的 AST 操作
- **C API 改进**：更多稳定 API，便于 C 扩展开发

```python
# PEP 649 —— 延迟注解求值
class Node:
    def __init__(self, value: int, children: list[Node]):  # 无需引号
        self.value = value
        self.children = children

    def append(self, child: Node) -> None:  # 直接引用自身类型
        self.children.append(child)
```

## 2. dataclass 与 attrs

### 2.1 dataclass 进阶

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar

@dataclass
class Employee:
    name: str
    age: int
    department: str = "Engineering"
    salary: float = field(default=0.0, repr=False)  # 不在 repr 中显示
    skills: list[str] = field(default_factory=list)  # 可变默认值
    _id: int = field(init=False, repr=False)
    counter: ClassVar[int] = 0  # 类变量，不参与实例化

    def __post_init__(self) -> None:
        Employee.counter += 1
        self._id = Employee.counter

# frozen —— 不可变数据类
@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other: Point) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# 继承
@dataclass
class Manager(Employee):
    team_size: int = 0
    reports: list[str] = field(default_factory=list)
```

### 2.2 attrs 库

`attrs` 是 `dataclass` 的超集，提供更丰富的功能：

```python
import attrs
from attrs import define, field, asdict

@define
class User:
    name: str
    email: str = field(validator=attrs.validators.matches_re(r'^[^@]+@[^@]+\.[^@]+$'))
    age: int = field(validator=attrs.validators.ge(0))
    tags: list[str] = field(factory=list)
    is_active: bool = True

    @email.validator
    def _check_email_domain(self, attribute, value):
        if not value.endswith(('.com', '.org', '.net')):
            raise ValueError("不支持的邮箱域名")

# 转换器
@define
class Config:
    port: int = field(converter=int, default=8080)
    debug: bool = field(converter=lambda x: x.lower() == 'true', default=False)

# 不可变版本
@define(frozen=True)
class ImmutablePoint:
    x: float
    y: float
```

## 3. asyncio 进阶

### 3.1 TaskGroup 与结构化并发

Python 3.11 引入的 `TaskGroup` 提供了更安全的结构化并发：

```python
import asyncio
from typing import Any

async def fetch_url(url: str) -> dict[str, Any]:
    await asyncio.sleep(1)  # 模拟网络请求
    return {"url": url, "status": 200}

async def fetch_all() -> None:
    results: list[dict[str, Any]] = []

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_url("https://api.example.com/users"))
        task2 = tg.create_task(fetch_url("https://api.example.com/posts"))
        task3 = tg.create_task(fetch_url("https://api.example.com/comments"))

    # TaskGroup 退出时所有任务已完成
    results = [task1.result(), task2.result(), task3.result()]
    print(f"获取 {len(results)} 个资源")

asyncio.run(fetch_all())
```

### 3.2 异步上下文管理器与迭代器

```python
import asyncio
from contextlib import asynccontextmanager

class AsyncDBPool:
    def __init__(self, max_connections: int = 10):
        self.max_connections = max_connections
        self._pool: list[asyncio.Queue] = []

    @asynccontextmanager
    async def connection(self):
        """异步上下文管理器获取连接"""
        conn = await self._acquire()
        try:
            yield conn
        finally:
            await self._release(conn)

    async def _acquire(self):
        await asyncio.sleep(0.01)
        return "db_connection"

    async def _release(self, conn: str):
        await asyncio.sleep(0.01)

async def main():
    pool = AsyncDBPool()
    async with pool.connection() as conn:
        print(f"使用连接: {conn}")

# 异步生成器
async def stream_events():
    """模拟事件流"""
    for i in range(5):
        await asyncio.sleep(0.5)
        yield {"event_id": i, "data": f"事件 {i}"}

async def consume_events():
    async for event in stream_events():
        print(f"收到: {event}")
```

### 3.3 asyncio 调度器与超时

```python
import asyncio

async def with_timeout():
    try:
        result = await asyncio.wait_for(
            slow_operation(),
            timeout=2.0
        )
    except asyncio.TimeoutError:
        print("操作超时")

async def slow_operation():
    await asyncio.sleep(5)

# Python 3.11+ 的 TaskGroup + timeout 组合
async def resilient_fetch():
    try:
        async with asyncio.timeout(3.0):
            async with asyncio.TaskGroup() as tg:
                tg.create_task(fetch_url("https://api1.example.com"))
                tg.create_task(fetch_url("https://api2.example.com"))
    except TimeoutError:
        print("部分请求超时，已取消所有任务")
```

## 4. 类型系统完善

### 4.1 TypeAlias 与高级类型

```python
from typing import TypeAlias, ParamSpec, Concatenate, override, Protocol

# TypeAlias —— 显式类型别名
Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[Vector]
Handler: TypeAlias = Callable[[dict[str, Any]], Awaitable[None]]

# ParamSpec —— 参数规格类型
P = ParamSpec('P')
R = TypeVar('R')

def retry(
    max_attempts: int = 3,
    delay: float = 1.0
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """通用重试装饰器，保留原始函数签名"""
    def decorator(fn: Callable[P, R]) -> Callable[P, R]:
        @wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            last_error: Exception | None = None
            for attempt in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    time.sleep(delay * (2 ** attempt))
            raise last_error  # type: ignore
        return wrapper
    return decorator

# Concatenate —— 在函数签名前/后追加参数
def with_logging(
    fn: Callable[Concatenate[str, P], R]
) -> Callable[P, R]:
    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        logger = "app.logger"
        return fn(logger, *args, **kwargs)
    return wrapper
```

### 4.2 Protocol 与结构化子类型

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None: ...

@runtime_checkable
class AsyncCloseable(Protocol):
    async def close(self) -> None: ...

class DatabaseConnection:
    def close(self) -> None:
        print("关闭数据库连接")

def safe_close(resource: Closeable) -> None:
    resource.close()

db = DatabaseConnection()
assert isinstance(db, Closeable)  # 运行时检查
safe_close(db)
```

### 4.3 override 装饰器

```python
from typing import override

class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    @override
    def speak(self) -> str:
        return "汪汪"

    @override
    def fetch(self) -> str:  # 类型检查器报错：父类没有 fetch 方法
        return "捡球"
```

## 5. Pydantic v2 数据验证

Pydantic v2 基于 Rust 重写核心，性能提升 5-50 倍。

### 5.1 基础模型

```python
from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class User(BaseModel):
    id: int = Field(gt=0, description="用户ID")
    name: str = Field(min_length=2, max_length=50)
    email: str = Field(pattern=r'^[^@]+@[^@]+\.[^@]+$')
    role: UserRole = UserRole.USER
    created_at: datetime = Field(default_factory=datetime.now)
    tags: list[str] = Field(default_factory=list, max_length=10)

    @field_validator('name')
    @classmethod
    def name_must_not_contain_spaces(cls, v: str) -> str:
        if ' ' in v.strip():
            raise ValueError('姓名不能包含空格')
        return v.strip()

    @model_validator(mode='after')
    def validate_model(self) -> 'User':
        if self.role == UserRole.ADMIN and 'admin' not in self.tags:
            self.tags.append('admin')
        return self

# 使用
user = User(id=1, name="张三", email="zhang@example.com")
print(user.model_dump())          # 字典输出
print(user.model_dump_json())     # JSON 输出
print(user.model_json_schema())   # JSON Schema
```

### 5.2 配置与序列化

```python
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class APIResponse(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,      # 自动生成驼峰别名
        populate_by_name=True,          # 允许原始字段名
        from_attributes=True,           # 支持从 ORM 对象创建
        str_strip_whitespace=True,      # 自动去除空白
        json_schema_extra={
            "examples": [{"id": 1, "name": "示例"}]
        }
    )

    user_id: int
    user_name: str
    is_active: bool = True

# JSON 中使用驼峰
json_data = '{"userId": 1, "userName": "test", "isActive": true}'
resp = APIResponse.model_validate_json(json_data)
print(resp.user_name)  # test
```

## 6. FastAPI Web 框架

FastAPI 基于 Starlette 和 Pydantic，是构建现代 API 的首选框架。

### 6.1 路由与依赖注入

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI(title="My API", version="2.0.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="无效的认证凭据")
    return user

@app.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(
    item: ItemCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncDB = Depends(get_db)
) -> ItemResponse:
    db_item = await db.create_item(item, owner_id=current_user.id)
    return db_item
```

### 6.2 中间件与后台任务

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time

app = FastAPI()

# CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 自定义中间件
@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.perf_counter() - start)
    return response

# 后台任务
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    """发送邮件（后台执行）"""
    print(f"发送邮件到 {email}: {message}")

@app.post("/register")
async def register(
    user: UserCreate,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, user.email, "欢迎注册")
    return {"message": "注册成功，确认邮件已发送"}
```

## 7. Ruff 与 uv 工具链

### 7.1 Ruff —— 极速 Python Linter & Formatter

Ruff 用 Rust 编写，替代 flake8、isort、black 等多个工具：

```toml
# pyproject.toml
[tool.ruff]
target-version = "py312"
line-length = 88

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort
    "N",    # pep8-naming
    "UP",   # pyupgrade
    "B",    # flake8-bugbear
    "SIM",  # flake8-simplify
    "TCH",  # flake8-type-checking
    "RUF",  # ruff-specific rules
]
ignore = ["E501"]  # 行长度由 formatter 处理

[tool.ruff.lint.isort]
known-first-party = ["myapp"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

```bash
# 常用命令
ruff check .                    # 检查代码
ruff check --fix .              # 自动修复
ruff format .                   # 格式化代码
ruff check --select I --fix .   # 仅整理导入
```

### 7.2 uv —— 极速 Python 包管理

uv 由 Astral（Ruff 同一团队）开发，替代 pip、pip-tools、virtualenv、pyenv：

```bash
# 安装 Python 版本
uv python install 3.12 3.13

# 创建虚拟环境
uv venv --python 3.12

# 安装包（比 pip 快 10-100 倍）
uv pip install fastapi uvicorn pydantic

# 从 requirements.txt 安装
uv pip install -r requirements.txt

# 项目管理（uv 的项目管理模式）
uv init my-project
cd my-project
uv add fastapi pydantic        # 添加依赖到 pyproject.toml
uv add --dev pytest ruff       # 添加开发依赖
uv remove requests             # 移除依赖
uv run python main.py          # 在项目环境中运行
uv run pytest                  # 在项目环境中运行测试

# 工具运行（无需安装到项目）
uvx ruff check .
uvx black --check .
uvx mypy src/
```

```toml
# pyproject.toml (uv 项目)
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.110.0",
    "pydantic>=2.6.0",
    "uvicorn[standard]>=0.29.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8.0",
    "ruff>=0.4.0",
    "mypy>=1.10",
]
```

## 8. 小结

Python 3.12-3.14 的演进方向清晰：

- **性能**：Faster CPython 和自由线程模式正在消除 Python 的性能瓶颈
- **类型安全**：Type Parameter 语法、Protocol、override 等让 Python 的类型系统日趋完善
- **开发体验**：更好的错误消息、改进的 REPL、更简洁的语法
- **生态工具**：Ruff 和 uv 代表了 Python 工具链的现代化方向
- **数据验证**：Pydantic v2 和 FastAPI 构建了类型安全的 Web 开发范式

这些进步使得 Python 在保持简洁易用的同时，越来越适合构建大型、高性能、类型安全的生产级应用。

## 参考文献

Python 官方文档：https://docs.python.org/zh-cn/3/
PEP 8 样式指南：https://peps.python.org/pep-0008/
Python 之禅（PEP 20）：https://peps.python.org/pep-0020/
Python 类型注解指南（PEP 484）：https://peps.python.org/pep-0484/
Python 打包用户指南：https://packaging.python.org/
Real Python 教程站：https://realpython.com/

## 延伸阅读

Python 数据类型与内置容器，见 040-python 模块的基础文档。
Python 异步编程（asyncio/FastAPI），见 040-python 模块的异步与 Web 文档。
Python 数据分析（NumPy/Pandas），见 051-data-analysis 模块。
Python 与数据库交互（SQLAlchemy），见 019-sql 模块相关文档。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Python 全栈课程；尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Python 后端课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Python 概述与环境配置 | 001-PythonOverviewEnvSetup | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 变量与常量 | 003-VariableConstant | 本文的并列主题 |
| Python 描述符协议：属性访问的底层机制与工程实践 | 004-PythonDescriptorProtocol | 本文的原理深化 |
| Python 基础数据类型：从对象模型到工程实践的深度解析 | 005-PythonBasicsDataTypeObjectModelPracticeDeepAnalysis | 本文的前置基础 |
| 协程与asyncio | 006-CoroutineAsyncio | 本文的并列主题 |
| 列表推导式进阶 | 007-ListComprehensionAdvanced | 本文的并列主题 |
| 运算符与表达式 | 008-OperatorExpression | 本文的并列主题 |
| Python与虚拟环境 | 009-PythonVirtualEnv | 本文的前置基础 |
| 元类 | 010-Metaclass | 本文的并列主题 |
| Python与SQLAlchemy | 011-PythonSQLAlchemy | 本文的并列主题 |
| 多进程与多线程 | 012-MultiprocessingMultithreading | 本文的并列主题 |
| Python与FastAPI | 013-PythonFastAPI | 本文的并列主题 |
| Python与Django | 014-PythonDjango | 本文的并列主题 |
| 数据类与Pydantic | 015-DataClassPydantic | 本文的并列主题 |
| Python与Redis | 016-PythonRedis | 本文的并列主题 |
| Python 与 Celery：分布式任务队列的设计、实现与工程实践 | 017-PythonCeleryDistributedTaskQueue | 本文的并列主题 |
| 控制流 | 018-ControlFlow | 本文的并列主题 |
| Python与Docker | 019-PythonDocker | 本文的并列主题 |
| Python与机器学习 | 020-PythonMachineLearning | 本文的并列主题 |
| Python与深度学习 | 021-PythonDeepLearning | 本文的并列主题 |
| Python与NLP | 022-PythonAndNLP | 本文的并列主题 |
| Python与计算机视觉 | 023-PythonComputerVision | 本文的并列主题 |
| Python与Web爬虫 | 024-WebScrapingWithPython | 本文的并列主题 |
| Python与自动化 | 025-PythonAutomationCookbook | 本文的并列主题 |
| 函数详解 | 026-FunctionDetailed | 本文的并列主题 |
| Python与日志 | 027-PythonLog | 本文的并列主题 |
| Python与加密 | 028-PythonAndCryptography | 本文的安全延伸 |
| Python与测试 | 029-PythonTest | 本文的并列主题 |
| Python 与配置管理：从环境变量到云原生动态配置的工程实践 | 030-Python | 本文的前置基础 |
| 装饰器 | 031-Decorator | 本文的并列主题 |
| Python与消息队列 | 032-PythonMessageQueue | 本文的并列主题 |
| Python与gRPC | 033-PythongRPC | 本文的并列主题 |
| Python与WebSocket | 034-PythonWebSocket | 本文的并列主题 |
| Python与CI-CD | 035-PythonCICD | 本文的并列主题 |
| Python与性能优化 | 036-PythonPerformance | 本文的性能延伸 |
| 内置数据结构 | 037-BuiltinDataStructure | 本文的并列主题 |
| 正则表达式 | 038-Regex | 本文的并列主题 |
| Python与CLI | 039-PythonCLI | 本文的并列主题 |
| Python与设计模式 | 040-PythonDesignPattern | 本文的并列主题 |
| Python与打包发布 | 041-ASurveyOfPythonPackagingPastPresentAndFuture | 本文的并列主题 |
| Python 与 Jupyter：交互式计算、数据分析与可复现研究 | 042-PythonJupyter | 本文的并列主题 |
| Python与GraphQL | 043-PythonGraphQL | 本文的并列主题 |
| Python与代码质量 | 044-PythonCodeQuality | 本文的并列主题 |
| 并发编程 | 045-ConcurrentProgramming | 本文的并列主题 |
| Python与数据库迁移 | 046-PythonDatabaseMigration | 本文的并列主题 |
| Python与OAuth2 | 047-PythonOAuth2 | 本文的并列主题 |
| Python与向量数据库 | 048-PythonVectorDatabase | 本文的并列主题 |
| Python 进阶与最新特性 | 049-PythonAdvancedLatestFeature | 本文自身 |
| 推导式与生成器 | 050-ComprehensionGenerator | 本文的并列主题 |
| 模块、包与工程化 | 051-ModulePackageEngineering | 本文的并列主题 |
| 上下文管理器 | 052-ContextManager | 本文的并列主题 |
| 元类与单例模式 | 053-MetaclassSingleton | 本文的并列主题 |
| 异步编程详解 | 054-AsyncProgrammingDetailed | 本文的并列主题 |
| 弱引用 | 055-WeakReference | 本文的并列主题 |
| 打包与发布 | 056-PackagePublish | 本文的并列主题 |
| 描述符 | 057-Descriptor | 本文的并列主题 |
| 数据类与字段默认值 | 058-DataClassFieldDefault | 本文的并列主题 |
| 生成器与协程 | 059-GeneratorCoroutine | 本文的并列主题 |
| 类型注解与mypy | 060-TypeAnnotationMypy | 本文的并列主题 |
| 面向对象编程 | 061-OOP | 本文的并列主题 |
| 装饰器进阶 | 062-DecoratorAdvanced | 本文的并列主题 |
| 异常处理 | 063-ExceptionHandling | 本文的并列主题 |
| 文件 I/O 与上下文管理器 | 064-FileIOContextManager | 本文的并列主题 |
| Python 项目示例：网页爬虫与数据分析 | 065-PythonProjectExampleWebCrawlerDataAnalysis | 本文的综合应用 |
| Python 理论知识点 | 066-PythonTheoryKnowledge | 本文的并列主题 |
| 基础数据类型 | 067-BasicDataType | 本文的前置基础 |
| Python 面向对象基础 | 068-COOPBasics | 本文的前置基础 |
| Python 面向对象进阶 | 069-COOPAdvanced | 本文的并列主题 |
| Python pathlib 路径操作 | 070-Pathlib | 本文的并列主题 |
| Python itertools 迭代工具 | 071-Itertools | 本文的并列主题 |
| Python functools 函数工具 | 072-Functools | 本文的并列主题 |
| Python datetime 与 time | 073-DatetimeTime | 本文的并列主题 |
| Python 序列化 JSON/CSV/Pickle | 074-SerializationJsonCsvPickle | 本文的并列主题 |
| Python 网络编程 socket/http | 075-NetworkSocketHttp | 本文的并列主题 |
| Python sys/os 平台接口 | 076-SysOsPlatform | 本文的并列主题 |
| Python math/random/statistics | 077-MathRandomStatistics | 本文的并列主题 |
| Python subprocess 子进程 | 078-Subprocess | 本文的并列主题 |
| Python logging 日志配置 | 079-Logging | 本文的并列主题 |
| Python 测试 unittest/pytest | 080-UnittestPytest | 本文的并列主题 |
| Python 字符串格式化与方法 | 081-StringFormattingMethods | 本文的并列主题 |
| Python argparse 命令行参数解析 | 082-ArgparseCli | 本文的并列主题 |
| Python typing 进阶 | 083-TypingAdvanced | 本文的并列主题 |
| Python enum 枚举 | 084-Enum | 本文的并列主题 |
| Python hashlib 与 hmac | 085-HashlibHmac | 本文的并列主题 |
| Python ssl 安全套接字 | 086-SslCrypto | 本文的安全延伸 |
| Python http.client HTTP 客户端 | 087-HttpClient | 本文的并列主题 |
| Python sqlite3 数据库 | 088-Sqlite3 | 本文的并列主题 |
| Python zipfile 与 tarfile | 089-ZipfileTarfile | 本文的并列主题 |
| Python array 与 bisect | 090-ArrayBisect | 本文的并列主题 |
| Python 字符串与文本处理 | 091-StringText | 本文的并列主题 |
| Python decimal 与 fractions | 092-DecimalFractions | 本文的并列主题 |
| Python shutil 与 tempfile | 093-ShutilTempfile | 本文的并列主题 |
| Python gc inspect dis | 094-GcInspect | 本文的并列主题 |
| Python traceback 与 warnings | 095-TracebackWarnings | 本文的并列主题 |
| Python httpx 与 requests | 096-HttpxRequests | 本文的并列主题 |
| Python 性能分析与优化 | 097-ProfilingOptimization | 本文的性能延伸 |
