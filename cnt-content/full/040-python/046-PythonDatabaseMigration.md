---
order: 86
title: Python与数据库迁移
module: python
category: Python
difficulty: intermediate
description: Alembic与数据库迁移
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与代码质量
  - python/并发编程
  - python/Python与OAuth2
  - 'python/Python与WebSocket-2'
prerequisites:
  - python/语法速查
---

## 什么是数据库迁移

数据库迁移是指对数据库结构进行版本化管理的过程。当你修改了数据表的结构（比如新增一列、删除一张表、修改字段类型），你需要一种可靠的方式把这些变更记录下来，并能在不同环境（开发、测试、生产）中重复执行。

如果没有迁移工具，你可能会手动去数据库里执行 SQL 语句来改表结构。但这样做有几个严重问题：你无法追踪改了什么、无法回滚、无法在团队之间同步变更。数据库迁移工具就是为了解决这些问题而诞生的。

在 Python 生态中，Alembic 是最主流的数据库迁移工具，它与 SQLAlchemy ORM 紧密配合，是 Python Web 开发中不可或缺的一环。

## 基础概念

### 迁移版本链

Alembic 把每一次数据库结构变更称为一个"迁移"（migration）。每个迁移都有一个唯一的版本标识，多个迁移按顺序组成一条版本链。数据库中会有一张特殊的表（默认叫 alembic_version）来记录当前数据库处于哪个版本。

### 自动生成与手写迁移

Alembic 支持两种方式创建迁移：

- 自动生成（autogenerate）：Alembic 对比你的 SQLAlchemy 模型定义和数据库实际结构，自动生成迁移脚本
- 手写迁移：你手动编写迁移脚本中的 upgrade 和 downgrade 函数

自动生成非常方便，但并非万能。复杂变更（如数据迁移、列重命名）仍需手动调整。

### upgrade 与 downgrade

每个迁移脚本都包含两个函数：

- upgrade()：执行升级操作，把数据库结构从上一个版本变更为当前版本
- downgrade()：执行回退操作，把数据库结构从当前版本恢复为上一个版本

这两个函数必须互为逆操作，否则回滚会出问题。

## 快速上手

### 安装 Alembic

```bash
# 安装 alembic 和 sqlalchemy
pip install alembic sqlalchemy
```

### 初始化 Alembic

在你的项目根目录下执行初始化命令：

```bash
# 创建 alembic 配置目录和文件
alembic init migrations
```

执行后会在当前目录生成以下文件结构：

```
alembic.ini          # Alembic 配置文件
migrations/
  env.py             # 迁移运行环境配置
  script.py.mako     # 迁移脚本模板
  versions/          # 存放迁移脚本的目录（初始为空）
```

### 配置数据库连接

打开 alembic.ini，修改 sqlalchemy.url 为你的数据库连接地址：

```ini
# 修改这一行为你的数据库地址
sqlalchemy.url = sqlite:///myapp.db
```

如果你使用 PostgreSQL，连接字符串类似：

```ini
sqlalchemy.url = postgresql://user:password@localhost:5432/mydb
```

### 创建第一个迁移

```bash
# 根据模型自动生成迁移脚本
alembic revision --autogenerate -m "add users table"
```

这会在 migrations/versions/ 目录下生成一个 Python 文件，文件名类似 `a1b2c3d4e5f6_add_users_table.py`。

### 执行迁移

```bash
# 升级到最新版本
alembic upgrade head
```

### 回退迁移

```bash
# 回退一个版本
alembic downgrade -1

# 回退到指定版本
alembic downgrade a1b2c3d4e5f6

# 回退所有迁移（回到空白数据库状态）
alembic downgrade base
```

## 详细用法

### 配置 env.py 关联 SQLAlchemy 模型

要让 autogenerate 功能正常工作，需要在 env.py 中告诉 Alembic 你的模型定义在哪里。打开 migrations/env.py，找到 target_metadata 变量，修改为：

```python
# 导入你的 SQLAlchemy Base
from myapp.models import Base

# 将 target_metadata 指向你的模型元数据
target_metadata = Base.metadata
```

这样 Alembic 在自动生成迁移时，就能发现你定义的所有模型类，并与数据库实际结构进行对比。

### 编写 SQLAlchemy 模型

```python
# myapp/models.py
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# 声明基类
class Base(DeclarativeBase):
    pass

# 定义用户模型
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    age: Mapped[int] = mapped_column(Integer, nullable=True)
```

### 自动生成迁移脚本

当你修改了模型后（比如新增了字段或新增了模型类），运行：

```bash
alembic revision --autogenerate -m "add age column to users"
```

生成的迁移脚本大致如下：

```python
"""add age column to users

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2026-01-15 10:30:00.000000
"""
from alembic import op
import sqlalchemy as sa

# 版本标识
revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # 升级操作：添加 age 列
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))

def downgrade() -> None:
    # 回退操作：删除 age 列
    op.drop_column('users', 'age')
```

### 手动编写迁移脚本

有时自动生成无法满足需求，你需要手动创建迁移：

```bash
# 创建空白的迁移脚本
alembic revision -m "rename column name to full_name"
```

然后手动编辑生成的文件：

```python
"""rename column name to full_name

Revision ID: c3d4e5f6a7b8
Revises: b2c3d4e5f6a7
Create Date: 2026-01-15 11:00:00.000000
"""
from alembic import op

revision = 'c3d4e5f6a7b8'
down_revision = 'b2c3d4e5f6a7'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # 重命名列（alembic 的 batch 模式兼容 SQLite）
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('name', new_column_name='full_name')

def downgrade() -> None:
    # 回退：把列名改回去
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('full_name', new_column_name='name')
```

### 常用的 op 操作

Alembic 通过 op 对象提供了丰富的数据库操作方法：

```python
# 创建新表
def upgrade() -> None:
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('content', sa.Text()),
        sa.Column('author_id', sa.Integer(), sa.ForeignKey('users.id')),
    )

# 添加列
op.add_column('users', sa.Column('phone', sa.String(20)))

# 删除列
op.drop_column('users', 'phone')

# 修改列类型
op.alter_column('users', 'age',
                existing_type=sa.Integer(),
                type_=sa.String(10))

# 添加唯一约束
op.create_unique_constraint('uq_users_email', 'users', ['email'])

# 添加外键
op.create_foreign_key('fk_articles_author', 'articles', 'users', ['author_id'], ['id'])

# 创建索引
op.create_index('ix_users_name', 'users', ['name'])

# 删除表
op.drop_table('articles')
```

### 查看迁移状态

```bash
# 查看当前数据库的迁移版本
alembic current

# 查看迁移历史
alembic history

# 查看详细历史（显示每个迁移的具体信息）
alembic history --verbose
```

### 升级和降级的多种方式

```bash
# 升级到最新版本
alembic upgrade head

# 升级到指定版本
alembic upgrade a1b2c3d4e5f6

# 相对升级（向前推进2个版本）
alembic upgrade +2

# 降级一个版本
alembic downgrade -1

# 降级到指定版本
alembic downgrade a1b2c3d4e5f6

# 降级到最初状态
alembic downgrade base

# 升级到某个相对位置
alembic upgrade head+1
```

### 数据迁移

有时候你不仅需要修改表结构，还需要迁移数据。这必须在迁移脚本中手动完成：

```python
from alembic import op
import sqlalchemy as sa

def upgrade() -> None:
    # 先添加新列
    op.add_column('users', sa.Column('full_name', sa.String(200)))

    # 创建临时连接来执行数据迁移
    user_table = sa.table('users',
        sa.column('name', sa.String),
        sa.column('full_name', sa.String),
    )

    # 把 name 列的值复制到 full_name 列
    op.execute(
        user_table.update().values(full_name=user_table.c.name)
    )

    # 最后删除旧列
    op.drop_column('users', 'name')

def downgrade() -> None:
    # 回退操作
    op.add_column('users', sa.Column('name', sa.String(200)))
    # 反向复制数据
    user_table = sa.table('users',
        sa.column('name', sa.String),
        sa.column('full_name', sa.String),
    )
    op.execute(
        user_table.update().values(name=user_table.c.full_name)
    )
    op.drop_column('users', 'full_name')
```

## 常见场景

### 在 FastAPI 项目中集成 Alembic

一个典型的 FastAPI 项目结构如下：

```
myapp/
  main.py           # FastAPI 应用入口
  models.py         # SQLAlchemy 模型定义
  database.py       # 数据库连接配置
  alembic.ini       # Alembic 配置
  migrations/
    env.py
    versions/
```

在 database.py 中定义数据库连接：

```python
# myapp/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./myapp.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
```

在 env.py 中引入 Base：

```python
# 修改 migrations/env.py 中的关键部分
from myapp.database import Base
from myapp.models import *  # 确保所有模型都被导入

target_metadata = Base.metadata
```

### 在生产环境中安全执行迁移

```bash
# 先查看当前状态
alembic current

# 检查是否有待执行的迁移（不实际执行）
alembic upgrade head --sql > migration.sql

# 确认 SQL 无误后再实际执行
alembic upgrade head
```

### 多分支迁移合并

当多个开发者同时创建迁移时，可能会产生分支。Alembic 提供了合并功能：

```bash
# 合并多个分支
alembic merge -m "merge branches" a1b2c3d4 e5f6a7b8

# 查看是否有分支
alembic heads
```

## 注意事项与常见错误

### autogenerate 不是万能的

Alembic 的自动生成功能无法检测以下变更：

- 列的重命名（会被识别为删除旧列并添加新列，导致数据丢失）
- 表的重命名
- 数据迁移
- 约束的修改

遇到这些情况，必须手动编写迁移脚本。

### SQLite 的限制

SQLite 不支持直接修改列定义和删除列。Alembic 提供了 batch 模式来兼容 SQLite：

```python
# 在 env.py 中启用 batch 模式
def run_migrations_online():
    connectable = engine
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,  # 启用 batch 模式
        )
        with context.begin_transaction():
            context.run_migrations()
```

在迁移脚本中使用 batch_alter_table：

```python
def upgrade() -> None:
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('name', nullable=False)
```

### 不要修改已执行的迁移脚本

一旦某个迁移脚本已经在数据库中执行过，就不要再修改它。否则会导致版本链不一致。如果发现迁移有错误，应该创建一个新的迁移来修正。

### 始终检查自动生成的迁移

自动生成的迁移脚本不一定完全正确，在执行前务必检查 upgrade 和 downgrade 函数的内容，确认操作符合预期。

### downgrade 必须是 upgrade 的逆操作

如果 downgrade 函数不能正确回退 upgrade 的操作，那么回滚时数据库结构就会出错。编写迁移时一定要确保两者互为逆操作。

## 进阶用法

### 自定义迁移模板

你可以修改 migrations/script.py.mako 来自定义迁移脚本的生成模板：

```mako
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

def upgrade() -> None:
    ${upgrades if upgrades else "pass"}

def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
```

### 在代码中执行迁移

有时候你需要在应用启动时自动执行迁移，而不是手动运行命令：

```python
from alembic.config import Config
from alembic import command

def run_migrations():
    # 创建 Alembic 配置
    alembic_cfg = Config("alembic.ini")
    # 执行升级
    command.upgrade(alembic_cfg, "head")

# 在应用启动时调用
if __name__ == "__main__":
    run_migrations()
```

### 使用环境变量管理数据库连接

不要把数据库密码硬编码在 alembic.ini 中，应该通过环境变量读取：

```python
# 在 env.py 中动态设置数据库连接
import os

# 从环境变量获取数据库连接字符串
database_url = os.getenv("DATABASE_URL", "sqlite:///default.db")

def run_migrations_online():
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = database_url
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    # ... 后续代码不变
```

### 离线模式生成 SQL

在不连接数据库的情况下生成 SQL 脚本，适合交给 DBA 审核：

```bash
# 生成 SQL 而不实际执行
alembic upgrade head --sql

# 生成从某个版本到另一个版本的 SQL
alembic upgrade a1b2c3:e5f6a7b --sql
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
| Python与数据库迁移 | 046-PythonDatabaseMigration | 本文自身 |
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
