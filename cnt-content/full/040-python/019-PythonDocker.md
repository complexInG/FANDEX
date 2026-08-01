---
order: 62
title: Python与Docker
module: python
category: Python
difficulty: intermediate
description: Python容器化
author: fanquanpp
updated: '2026-08-01'
related:
  - python/控制流
  - python/Python与Celery
  - python/Python与Redis
  - python/Python与GraphQL
prerequisites:
  - python/语法速查
---

## 什么是 Docker

Docker 是一种容器化技术，它可以把你的应用和所有依赖打包到一个标准化的容器中。这个容器可以在任何安装了 Docker 的机器上一致地运行，不会出现"在我电脑上能跑"的问题。

对于 Python 开发者来说，Docker 解决了几个核心痛点：不同机器上 Python 版本不一致、系统依赖缺失、开发环境与生产环境差异导致的故障。通过 Docker，你可以确保代码在开发、测试、生产环境中以完全相同的方式运行。

## 基础概念

### 镜像（Image）

镜像是一个只读的模板，包含了运行应用所需的一切：操作系统、Python 解释器、第三方库、代码文件等。你可以把镜像理解为一份"安装光盘"，用它来创建容器。

### 容器（Container）

容器是镜像的运行实例。一个镜像可以创建多个容器，每个容器都是独立运行的、隔离的进程。容器启动很快，占用的资源也远少于虚拟机。

### Dockerfile

Dockerfile 是一个文本文件，包含了一系列指令，用来告诉 Docker 如何构建镜像。每一条指令都会在镜像中创建一个新的层。

### Docker Compose

Docker Compose 是一个用于定义和运行多容器应用的工具。通过一个 YAML 文件，你可以同时启动应用、数据库、缓存等多个服务，非常适合本地开发。

## 快速上手

### 安装 Docker

前往 Docker 官网下载并安装 Docker Desktop。安装完成后在终端验证：

```bash
# 验证 Docker 是否安装成功
docker --version

# 验证 Docker 是否正常运行
docker run hello-world
```

### 最简单的 Python 容器

创建一个文件名为 Dockerfile 的文件（没有扩展名）：

```dockerfile
# 使用官方 Python 镜像作为基础
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有文件到容器中
COPY . .

# 运行 Python 脚本
CMD ["python", "app.py"]
```

在同目录下创建 app.py：

```python
# 一个简单的 Python 脚本
print("Hello from Docker!")
```

构建并运行：

```bash
# 构建镜像，-t 参数给镜像起个名字
docker build -t my-python-app .

# 运行容器
docker run my-python-app
```

## 详细用法

### 编写规范的 Dockerfile

一个生产级别的 Python 项目 Dockerfile 通常包含以下步骤：

```dockerfile
# 第一阶段：构建阶段
FROM python:3.12-slim AS builder

# 设置工作目录
WORKDIR /app

# 先只复制依赖文件（利用 Docker 缓存层机制）
COPY requirements.txt .

# 安装依赖到指定目录
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# 第二阶段：运行阶段（最终镜像）
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 从构建阶段复制已安装的依赖
COPY --from=builder /install /usr/local

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 使用非 root 用户运行（安全最佳实践）
RUN useradd --create-home appuser
USER appuser

# 启动命令
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 理解 Docker 缓存层

Docker 构建镜像时，每一条指令都会生成一个层（layer）。如果某条指令的内容没有变化，Docker 会复用之前的缓存层，不会重新执行。这就是为什么要把 COPY requirements.txt 和 RUN pip install 放在 COPY . . 之前——只要依赖没变，安装依赖这一步就会使用缓存，大幅加快构建速度。

```dockerfile
# 正确的顺序：先复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 最后再复制代码（代码经常变动，放最后）
COPY . .
```

### 使用 .dockerignore

和 .gitignore 类似，.dockerignore 文件指定哪些文件不复制到镜像中：

```
# .dockerignore 文件内容
__pycache__
*.pyc
*.pyo
.git
.gitignore
.venv
venv
.env
*.md
.pytest_cache
.mypy_cache
.ruff_cache
```

这样可以避免把不必要的文件打包进镜像，减小镜像体积，也防止敏感信息泄露。

### 环境变量与配置

在 Dockerfile 中可以通过 ENV 指令设置环境变量：

```dockerfile
# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV APP_ENV=production

# PYTHONUNBUFFERED=1 让 Python 日志实时输出（不缓冲）
# PYTHONDONTWRITEBYTECODE=1 不生成 .pyc 文件
```

运行容器时也可以通过 -e 参数传入环境变量：

```bash
# 通过 -e 参数设置环境变量
docker run -e DATABASE_URL=postgresql://db:5432/mydb my-app

# 通过 --env-file 从文件加载环境变量
docker run --env-file .env my-app
```

### 端口映射与数据卷

```bash
# 端口映射：将容器内的 8000 端口映射到主机的 8000 端口
docker run -p 8000:8000 my-app

# 数据卷：将主机目录挂载到容器内（代码修改实时生效）
docker run -v $(pwd):/app my-app

# 组合使用
docker run -p 8000:8000 -v $(pwd):/app my-app
```

### Docker Compose 管理多服务

实际项目中，你的应用通常需要数据库、缓存等服务。Docker Compose 可以用一个配置文件定义所有服务。

创建 docker-compose.yml：

```yaml
# Docker Compose 配置文件
version: '3.8'

services:
  # Web 应用服务
  web:
    build: .
    ports:
      - '8000:8000'
    volumes:
      - .:/app
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydb
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

  # PostgreSQL 数据库服务
  db:
    image: postgres:16
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - '5432:5432'

  # Redis 缓存服务
  redis:
    image: redis:7-alpine
    ports:
      - '6379:6379'

# 命名数据卷
volumes:
  postgres_data:
```

使用 Docker Compose 的常用命令：

```bash
# 构建并启动所有服务（后台运行）
docker compose up -d

# 查看运行中的服务
docker compose ps

# 查看服务日志
docker compose logs web

# 进入容器内部执行命令
docker compose exec web bash

# 停止所有服务
docker compose down

# 停止并删除数据卷（重置数据库）
docker compose down -v
```

### 开发环境与生产环境的 Dockerfile

开发环境需要支持热重载、调试，生产环境需要更小的镜像和更高的安全性。

开发用 Dockerfile：

```dockerfile
# 开发环境 Dockerfile
FROM python:3.12-slim

WORKDIR /app

# 安装开发依赖
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

# 使用热重载模式启动
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

生产用 Dockerfile（多阶段构建）：

```dockerfile
# 生产环境 Dockerfile - 多阶段构建
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

## 常见场景

### FastAPI 项目容器化

项目结构：

```
myproject/
  app/
    __init__.py
    main.py
    models.py
  requirements.txt
  Dockerfile
  docker-compose.yml
```

Dockerfile：

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Celery Worker 容器化

如果你的项目使用 Celery 处理异步任务，需要为 Worker 单独创建容器。可以在 docker-compose.yml 中添加：

```yaml
# Celery Worker 服务
worker:
  build: .
  command: celery -A app.celery worker --loglevel=info
  volumes:
    - .:/app
  environment:
    - DATABASE_URL=postgresql://postgres:password@db:5432/mydb
    - REDIS_URL=redis://redis:6379/0
  depends_on:
    - db
    - redis

# Celery Beat 定时任务服务
beat:
  build: .
  command: celery -A app.celery beat --loglevel=info
  volumes:
    - .:/app
  environment:
    - DATABASE_URL=postgresql://postgres:password@db:5432/mydb
    - REDIS_URL=redis://redis:6379/0
  depends_on:
    - db
    - redis
```

### 数据科学项目容器化

```dockerfile
# 数据科学项目的 Dockerfile
FROM python:3.12-slim

WORKDIR /app

# 安装系统依赖（某些数据科学库需要）
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Jupyter Notebook
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

## 注意事项与常见错误

### 不要把敏感信息写进镜像

密码、API Key、数据库连接字符串等敏感信息绝对不能写在 Dockerfile 中。应该通过环境变量在运行时传入：

```bash
# 正确做法：运行时传入敏感信息
docker run -e SECRET_KEY=mysecret -e DB_PASSWORD=mypassword my-app
```

### 镜像体积过大

常见原因和解决方法：

- 使用了完整版基础镜像（python:3.12 而不是 python:3.12-slim），换成 slim 版本
- 没有使用 .dockerignore，把不必要的文件打包进去了
- 没有使用多阶段构建，构建工具也被包含在最终镜像中
- pip 缓存没有清理，使用 --no-cache-dir 参数

### 容器内时区问题

默认情况下容器使用 UTC 时区，如果你的应用依赖时区，需要设置：

```dockerfile
# 设置时区为上海
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
```

### 文件权限问题

容器内默认以 root 用户运行，这可能导致挂载卷时文件权限混乱。建议创建专用用户：

```dockerfile
# 创建非 root 用户
RUN useradd --create-home appuser
# 确保用户对工作目录有权限
RUN chown -R appuser:appuser /app
USER appuser
```

### 容器间通信

在 Docker Compose 中，服务之间通过服务名访问，而不是 localhost。例如 web 服务访问 db 服务，应该用 db:5432 而不是 localhost:5432：

```python
# 正确：使用 Docker Compose 中的服务名
DATABASE_URL = "postgresql://postgres:password@db:5432/mydb"

# 错误：不能用 localhost
# DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"
```

### Windows 下的路径问题

在 Windows 上使用 Docker 时，路径分隔符和换行符可能有问题。建议：

- Dockerfile 使用 LF 换行符（不要用 CRLF）
- 挂载卷时使用正斜杠或 ${pwd} 代替 $(pwd)

## 进阶用法

### 多阶段构建减小镜像体积

多阶段构建是减小镜像体积的最有效手段。核心思路是：在构建阶段安装编译工具和依赖，在运行阶段只复制编译好的结果：

```dockerfile
# 阶段一：构建
FROM python:3.12 AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# 阶段二：运行
FROM python:3.12-slim

WORKDIR /app
# 只复制安装好的依赖，不包含构建工具
COPY --from=builder /install /usr/local
COPY . .

CMD ["python", "app.py"]
```

### 健康检查

Docker 支持在 Dockerfile 中定义健康检查，让 Docker 自动判断容器是否正常运行：

```dockerfile
# 定义健康检查：每 30 秒检查一次
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
```

也可以在 docker-compose.yml 中定义：

```yaml
services:
  web:
    build: .
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:8000/health']
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
```

### 使用 uv 加速依赖安装

uv 是一个极速的 Python 包管理器，可以替代 pip：

```dockerfile
FROM python:3.12-slim

# 安装 uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# 使用 uv 安装依赖（比 pip 快 10-100 倍）
COPY pyproject.toml .
RUN uv pip install --system --no-cache -r pyproject.toml

COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker 多平台构建

如果你的镜像需要在不同 CPU 架构上运行（比如 Intel 和 Apple Silicon），可以使用多平台构建：

```bash
# 创建多平台构建器
docker buildx create --name mybuilder --use

# 构建多平台镜像
docker buildx build --platform linux/amd64,linux/arm64 -t my-app .
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
| Python与FastAPI | 013-PythonFastAPI | 本文的并列主题 |
| Python与Django | 014-PythonDjango | 本文的并列主题 |
| 数据类与Pydantic | 015-DataClassPydantic | 本文的并列主题 |
| Python与Redis | 016-PythonRedis | 本文的并列主题 |
| Python 与 Celery：分布式任务队列的设计、实现与工程实践 | 017-PythonCeleryDistributedTaskQueue | 本文的并列主题 |
| 控制流 | 018-ControlFlow | 本文的并列主题 |
| Python与Docker | 019-PythonDocker | 本文自身 |
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
