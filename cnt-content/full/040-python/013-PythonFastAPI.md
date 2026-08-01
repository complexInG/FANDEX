---
order: 56
title: Python与FastAPI
module: python
category: Python
difficulty: intermediate
description: FastAPI框架
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与Docker
  - python/Python与OAuth2
  - python/Python与Redis
  - python/Python与Celery
prerequisites:
  - python/语法速查
---

## 什么是 FastAPI

FastAPI 是一个现代、高性能的 Python Web 框架，用于构建 API。它基于 Starlette（处理网络请求）和 Pydantic（数据验证），利用 Python 的类型注解实现自动的数据验证、序列化和 API 文档生成。

FastAPI 的性能接近 Go 和 Node.js，是 Python 中最快的 Web 框架之一。它的设计理念是让开发者在写代码的同时就完成数据验证和文档编写，减少重复劳动。

## 基础概念

### 路径操作装饰器

FastAPI 使用装饰器来定义路由，如 @app.get、@app.post 等。每个装饰器对应一个 HTTP 方法。

### 路径参数与查询参数

路径参数是 URL 的一部分（如 /users/{user_id} 中的 user_id），查询参数是 URL 中 ? 后面的部分（如 ?page=1）。

### 请求体

POST 和 PUT 请求通常携带请求体（Request Body），FastAPI 使用 Pydantic 模型来验证请求体的数据结构和类型。

### 依赖注入

FastAPI 的依赖注入系统允许你声明代码所需的依赖，框架会自动解析和提供。常用于数据库连接、认证等场景。

### 自动文档

FastAPI 自动生成 OpenAPI 文档和交互式 API 文档（Swagger UI 和 ReDoc），访问 /docs 和 /redoc 即可查看。

## 快速上手

### 安装

```bash
pip install fastapi uvicorn
```

### 最简单的 API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}
```

运行：

```bash
uvicorn main:app --reload
```

访问 http://127.0.0.1:8000/ 即可看到返回的 JSON。访问 http://127.0.0.1:8000/docs 可以看到自动生成的交互式 API 文档。

## 详细用法

### 路径参数

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """路径参数：user_id 会自动转换为整数"""
    return {"user_id": user_id}

# 枚举类型的路径参数
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model": model_name.value}
```

### 查询参数

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items")
async def list_items(
    skip: int = 0,              # 有默认值的查询参数
    limit: int = 10,            # 有默认值的查询参数
    q: Optional[str] = None,    # 可选的查询参数
):
    return {"skip": skip, "limit": limit, "q": q}

# 请求示例：/items?skip=10&limit=20&q=python
```

### 请求体（Pydantic 模型）

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

app = FastAPI()

# 定义请求体模型
class UserCreate(BaseModel):
    username: str
    email: EmailStr          # 自动验证邮箱格式
    password: str
    age: Optional[int] = None  # 可选字段

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    """创建用户，自动验证请求体"""
    # user.username、user.email 等已经过验证
    # 模拟创建用户
    return {
        "id": 1,
        "username": user.username,
        "email": user.email,
        "created_at": datetime.now()
    }
```

### 表单数据与文件上传

```python
from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()

@app.post("/login")
async def login(username: str = Form(), password: str = Form()):
    """处理表单数据"""
    return {"username": username}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """处理文件上传"""
    content = await file.read()
    return {
        "filename": file.filename,
        "size": len(content),
        "content_type": file.content_type,
    }

@app.post("/upload-with-data")
async def upload_with_data(
    file: UploadFile = File(...),
    description: str = Form(...),
):
    """同时上传文件和表单数据"""
    return {
        "filename": file.filename,
        "description": description,
    }
```

### 依赖注入

```python
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Annotated

app = FastAPI()

# 模拟数据库
fake_items_db = {"item1": "苹果", "item2": "香蕉"}

# 定义依赖
def get_item_or_404(item_id: str):
    """根据 ID 获取项目，不存在则返回 404"""
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="项目不存在")
    return fake_items_db[item_id]

def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    """通用查询参数"""
    return {"q": q, "skip": skip, "limit": limit}

# 使用依赖
@app.get("/items/{item_id}")
async def read_item(item: str = Depends(get_item_or_404)):
    return {"item": item}

@app.get("/search")
async def search(params: dict = Depends(common_parameters)):
    return params

# 使用 Annotated 简化依赖声明
CommonParams = Annotated[dict, Depends(common_parameters)]

@app.get("/products")
async def list_products(params: CommonParams):
    return params
```

### 中间件

```python
from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """添加处理时间头的中间件"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# CORS 中间件
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 允许的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 异常处理

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"item1": "苹果", "item2": "香蕉"}

@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in items:
        # 抛出 HTTP 异常
        raise HTTPException(
            status_code=404,
            detail=f"项目 {item_id} 不存在"
        )
    return {"item": items[item_id]}
```

### 后台任务

```python
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def send_email(email: str, message: str):
    """模拟发送邮件（后台执行）"""
    print(f"发送邮件到 {email}: {message}")

@app.post("/send-notification")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks,
):
    """在后台发送邮件，不阻塞响应"""
    background_tasks.add_task(send_email, email, "欢迎注册")
    return {"message": "通知已加入后台队列"}
```

## 常见场景

### 完整的 CRUD API

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# 数据模型
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# 模拟数据库
db: dict[int, dict] = {}
next_id = 1

@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate):
    global next_id
    db[next_id] = {"id": next_id, **item.model_dump()}
    result = db[next_id]
    next_id += 1
    return result

@app.get("/items", response_model=List[ItemResponse])
async def list_items(skip: int = 0, limit: int = 10):
    return list(db.values())[skip:skip + limit]

@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="项目不存在")
    return db[item_id]

@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemCreate):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="项目不存在")
    db[item_id] = {"id": item_id, **item.model_dump()}
    return db[item_id]

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="项目不存在")
    del db[item_id]
    return {"message": "已删除"}
```

## 注意事项与常见错误

### async 与同步函数

如果你的函数中调用了同步的阻塞操作（如同步数据库查询、requests 库），应该使用 def 而不是 async def。在 async def 中调用阻塞操作会阻塞整个事件循环。

### Pydantic v2 变化

FastAPI 0.100+ 使用 Pydantic v2，一些 API 有变化：

- model.dict() 改为 model.model_dump()
- model.parse_obj() 改为 model.model_validate()
- Config 类改为 model_config

### 路由顺序

路由的匹配是按定义顺序的。如果两个路由可能冲突，更具体的路由应该放在前面：

```python
# 正确：具体的路径在前
@app.get("/users/me")
async def get_current_user(): ...

@app.get("/users/{user_id}")
async def get_user(user_id: int): ...

# 错误：{user_id} 会匹配 "me"，导致 get_current_user 永远不会被调用
```

## 进阶用法

### 数据库集成

```python
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

# 创建表
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
async def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

### 生命周期事件

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动时执行
    print("应用启动")
    yield
    # 应用关闭时执行
    print("应用关闭")

app = FastAPI(lifespan=lifespan)
```

### APIRouter 分模块

```python
# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def list_users():
    return [{"id": 1, "name": "张三"}]

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "张三"}
```

```python
# main.py
from fastapi import FastAPI
from routers.users import router as users_router

app = FastAPI()
app.include_router(users_router)
```

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
| Python与FastAPI | 013-PythonFastAPI | 本文自身 |
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
| Python 进阶与最新特性 | 049-PythonAdvancedLatestFeature | 本文的并列主题 |
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
