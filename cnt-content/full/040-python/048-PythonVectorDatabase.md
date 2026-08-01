---
order: 89
title: Python与向量数据库
module: python
category: Python
difficulty: advanced
description: 向量搜索与RAG
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与OAuth2
  - 'python/Python与WebSocket-2'
  - python/Python进阶与最新特性
  - python/推导式与生成器
prerequisites:
  - python/语法速查
---

## 什么是向量数据库

向量数据库是专门用来存储和检索向量（一组浮点数）的数据库。在大语言模型和 AI 应用中，文本、图片等数据会被转换成高维向量（比如 1536 维的浮点数组），向量数据库能快速找到与某个向量最相似的其他向量。

这种"相似性搜索"是 RAG（检索增强生成）技术的核心。当你向 AI 提问时，系统先把你的问题转成向量，在向量数据库中找到最相关的文档片段，再把这些片段提供给大语言模型来生成回答。

## 基础概念

### 向量嵌入（Embedding）

向量嵌入是把非结构化数据（文本、图片、音频）转换成数值向量的过程。例如，一句话"今天天气很好"经过嵌入模型处理后，可能变成一个 1536 维的浮点数组。语义相近的文本，其向量在空间中的距离也相近。

### 相似度计算

向量数据库通过计算向量之间的距离来判断相似度。常用的距离度量有：

- 余弦相似度：计算两个向量夹角的余弦值，范围 -1 到 1，值越大越相似
- 欧氏距离：两个向量在空间中的直线距离，值越小越相似
- 内积（点积）：两个向量对应位置相乘再求和

### RAG（检索增强生成）

RAG 的工作流程：用户提问 -> 问题转成向量 -> 在向量数据库中检索相关文档 -> 将文档和问题一起交给大语言模型 -> 生成回答。这样大语言模型就能基于你自己的数据来回答问题，而不仅限于训练数据。

### 常见的向量数据库

- ChromaDB：轻量级，适合本地开发和原型验证
- Pinecone：全托管云服务，适合生产环境
- Milvus：高性能分布式向量数据库，适合大规模数据
- Qdrant：用 Rust 编写的高性能向量搜索引擎
- Weaviate：支持混合搜索（向量+关键词）

## 快速上手

### 安装 ChromaDB

```bash
# 安装 ChromaDB
pip install chromadb

# 安装 OpenAI SDK（用于生成嵌入向量）
pip install openai
```

### 最简单的向量存储和检索

```python
import chromadb

# 创建内存模式的客户端（数据不持久化）
client = chromadb.Client()

# 创建或获取一个集合（类似数据库中的表）
collection = client.get_or_create_collection("my_docs")

# 添加文档（ChromaDB 会自动使用默认嵌入模型）
collection.add(
    documents=["Python 是一种编程语言", "Java 也是一种编程语言", "今天天气很好"],
    ids=["doc1", "doc2", "doc3"]
)

# 查询与"编程"最相关的文档
results = collection.query(
    query_texts=["编程语言有哪些"],
    n_results=2  # 返回最相似的 2 个结果
)

print(results["documents"])
# 输出: [['Python 是一种编程语言', 'Java 也是一种编程语言']]
```

### 使用持久化存储

上面的例子数据只存在于内存中，程序关闭后就丢失了。使用持久化客户端可以将数据保存到磁盘：

```python
import chromadb

# 创建持久化客户端（数据保存到指定目录）
client = chromadb.PersistentClient(path="./chroma_data")

# 创建集合
collection = client.get_or_create_collection("my_docs")

# 添加文档
collection.add(
    documents=["第一篇文档的内容", "第二篇文档的内容"],
    ids=["1", "2"]
)

# 下次启动程序时，数据依然存在
```

## 详细用法

### 手动指定嵌入向量

如果你有自己的嵌入模型，可以手动计算向量并存入 ChromaDB：

```python
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("custom_embeddings")

# 手动提供嵌入向量（这里用模拟数据，实际应使用嵌入模型生成）
# 假设每个文档对应一个 3 维向量
collection.add(
    documents=["苹果是一种水果", "香蕉也是一种水果", "汽车是交通工具"],
    embeddings=[
        [0.9, 0.1, 0.0],  # 苹果的向量
        [0.85, 0.15, 0.0],  # 香蕉的向量（和苹果相近）
        [0.0, 0.1, 0.9],  # 汽车的向量（和水果相远）
    ],
    ids=["1", "2", "3"]
)

# 用向量进行查询
results = collection.query(
    query_embeddings=[[0.9, 0.1, 0.0]],  # 查询和苹果相近的文档
    n_results=2
)

print(results["documents"])
# 输出: [['苹果是一种水果', '香蕉也是一种水果']]
```

### 添加元数据

元数据是附加在文档上的额外信息，可以用来过滤搜索结果：

```python
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("articles")

# 添加带元数据的文档
collection.add(
    documents=["Python 入门教程", "Java 高级编程", "Python 数据分析"],
    metadatas=[
        {"category": "tutorial", "language": "python", "level": "beginner"},
        {"category": "book", "language": "java", "level": "advanced"},
        {"category": "tutorial", "language": "python", "level": "intermediate"},
    ],
    ids=["1", "2", "3"]
)

# 查询时通过元数据过滤：只搜索 Python 相关的文档
results = collection.query(
    query_texts=["学习编程"],
    n_results=10,
    where={"language": "python"}  # 过滤条件
)

print(results["documents"])
# 输出: [['Python 入门教程', 'Python 数据分析']]
```

### 更新和删除文档

```python
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("my_docs")

# 先添加文档
collection.add(
    documents=["原始内容"],
    ids=["1"]
)

# 更新文档（id 不变，内容替换）
collection.update(
    documents=["更新后的内容"],
    ids=["1"]
)

# 也可以用 upsert（存在则更新，不存在则添加）
collection.upsert(
    documents=["再次更新的内容"],
    ids=["1"]
)

# 删除文档
collection.delete(ids=["1"])

# 删除整个集合
client.delete_collection("my_docs")
```

### 使用 OpenAI 嵌入模型

在实际项目中，通常使用 OpenAI 的嵌入模型来生成向量：

```python
import chromadb
from openai import OpenAI

# 初始化 OpenAI 客户端
openai_client = OpenAI()

def get_embedding(text: str) -> list[float]:
    """使用 OpenAI 的嵌入模型将文本转换为向量"""
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# 创建 ChromaDB 集合
chroma_client = chromadb.PersistentClient(path="./chroma_data")
collection = chroma_client.get_or_create_collection("knowledge_base")

# 添加文档
docs = [
    "Python 是一种解释型编程语言",
    "FastAPI 是一个高性能的 Python Web 框架",
    "Docker 可以将应用容器化部署",
]

for i, doc in enumerate(docs):
    embedding = get_embedding(doc)
    collection.upsert(
        documents=[doc],
        embeddings=[embedding],
        ids=[str(i)]
    )

# 查询
query = "Python Web 开发"
query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

print(results["documents"])
```

### 构建简单的 RAG 系统

下面是一个完整的 RAG 系统示例，包含文档入库、检索和生成回答：

```python
import chromadb
from openai import OpenAI

openai_client = OpenAI()
chroma_client = chromadb.PersistentClient(path="./rag_data")
collection = chroma_client.get_or_create_collection("rag_docs")

def get_embedding(text: str) -> list[float]:
    """生成文本的嵌入向量"""
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def add_documents(texts: list[str]):
    """将文档添加到向量数据库"""
    for i, text in enumerate(texts):
        embedding = get_embedding(text)
        collection.upsert(
            documents=[text],
            embeddings=[embedding],
            ids=[f"doc_{i}"],
            metadatas=[{"source": "user_input"}]
        )

def search_documents(query: str, n_results: int = 3) -> list[str]:
    """检索与查询最相关的文档"""
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results["documents"][0]

def ask_question(question: str) -> str:
    """RAG 问答：检索相关文档，然后让大模型生成回答"""
    # 第一步：检索相关文档
    relevant_docs = search_documents(question)

    # 第二步：构建提示词
    context = "\n".join(relevant_docs)
    prompt = f"""请根据以下参考资料回答问题。如果参考资料中没有相关信息，请说明。

参考资料：
{context}

问题：{question}

回答："""

    # 第三步：调用大语言模型生成回答
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# 使用示例
# 先添加知识库文档
add_documents([
    "Python 的 GIL（全局解释器锁）使得同一时刻只有一个线程执行 Python 字节码。",
    "FastAPI 支持 async/await 异步编程，可以高效处理并发请求。",
    "Celery 是 Python 的分布式任务队列，常用于处理耗时操作如发送邮件、生成报表。",
])

# 然后提问
answer = ask_question("Python 如何处理异步任务？")
print(answer)
```

## 常见场景

### 文档问答系统

将公司内部文档（PDF、Word、Wiki）分块后存入向量数据库，员工可以通过自然语言提问，系统自动检索相关内容并生成回答。

```python
# 将长文档切分成小块
def split_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """将长文本切分成重叠的小块"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap  # 重叠部分确保不丢失上下文
    return chunks

# 处理长文档
long_text = "这是一篇很长的文档..."  # 你的文档内容
chunks = split_text(long_text)

# 将每个块存入向量数据库
for i, chunk in enumerate(chunks):
    embedding = get_embedding(chunk)
    collection.upsert(
        documents=[chunk],
        embeddings=[embedding],
        ids=[f"chunk_{i}"],
        metadatas=[{"chunk_index": i}]
    )
```

### 语义搜索

传统的关键词搜索只能匹配包含相同词的文档，语义搜索能理解用户意图，找到意思相近但不包含相同关键词的文档：

```python
# 添加文档
collection.add(
    documents=[
        "如何提高代码质量",
        "代码审查的最佳实践",
        "数据库性能优化方法",
    ],
    ids=["1", "2", "3"]
)

# 语义搜索：即使用词不同，也能找到相关文档
results = collection.query(
    query_texts=["怎样写出更好的程序"],  # 没有用"代码质量"这个词
    n_results=2
)
# 仍然能找到"如何提高代码质量"和"代码审查的最佳实践"
```

### 推荐系统

通过向量相似度为用户推荐内容：

```python
# 假设用户喜欢某篇文章，找到相似的文章推荐
liked_article = "Python 异步编程入门"
results = collection.query(
    query_texts=[liked_article],
    n_results=5
)

# 返回与用户喜欢的文章最相似的内容
for doc in results["documents"][0]:
    print(f"推荐: {doc}")
```

## 注意事项与常见错误

### 嵌入模型的选择

嵌入模型的质量直接决定搜索效果。不同的嵌入模型生成的向量维度和语义空间不同，不能混用。一旦选定了嵌入模型，整个项目都应该使用同一个模型。

### 文档分块策略

文档太大时需要切分成小块再存入向量数据库。分块太小会丢失上下文，太大会导致检索不精确。一般建议每块 300-1000 个字符，相邻块之间有 50-100 个字符的重叠。

### 向量维度必须一致

同一个集合中所有向量的维度必须相同。如果你使用的嵌入模型输出 1536 维向量，那么所有文档和查询的向量都必须是 1536 维。

### ChromaDB 不适合大规模生产环境

ChromaDB 适合开发和小规模应用。如果数据量超过百万级别或需要高可用性，应该考虑 Milvus、Pinecone 等专业向量数据库。

### 搜索结果需要验证

向量搜索返回的是"语义相似"的结果，但不一定是"正确"的结果。在 RAG 系统中，应该让大语言模型判断检索到的内容是否真的与问题相关。

## 进阶用法

### 使用 Qdrant 向量数据库

Qdrant 是一个高性能的开源向量数据库，适合生产环境：

```bash
# 安装 Qdrant 客户端
pip install qdrant-client
```

```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# 连接 Qdrant（本地模式）
client = QdrantClient(":memory:")

# 也可以连接远程服务器
# client = QdrantClient(url="http://localhost:6333")

# 创建集合
client.create_collection(
    collection_name="my_docs",
    vectors_config=VectorParams(size=3, distance=Distance.COSINE),
)

# 插入向量
client.upsert(
    collection_name="my_docs",
    points=[
        PointStruct(id=1, vector=[0.9, 0.1, 0.0], payload={"text": "苹果是一种水果"}),
        PointStruct(id=2, vector=[0.85, 0.15, 0.0], payload={"text": "香蕉也是一种水果"}),
        PointStruct(id=3, vector=[0.0, 0.1, 0.9], payload={"text": "汽车是交通工具"}),
    ]
)

# 搜索
results = client.search(
    collection_name="my_docs",
    query_vector=[0.9, 0.1, 0.0],
    limit=2
)

for result in results:
    print(f"相似度: {result.score:.4f}, 内容: {result.payload['text']}")
```

### 混合搜索

混合搜索结合了向量搜索和关键词搜索的优点，既能理解语义，又能精确匹配关键词：

```python
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("hybrid_search")

# 添加文档
collection.add(
    documents=[
        "Python 3.12 发布于 2023 年 10 月",
        "Python 是最流行的编程语言之一",
        "Java 21 也发布了新特性",
    ],
    ids=["1", "2", "3"]
)

# 向量搜索（语义匹配）
vector_results = collection.query(
    query_texts=["Python 最新版本"],
    n_results=2
)

# 结合关键词过滤
filtered_results = collection.query(
    query_texts=["编程语言"],
    n_results=10,
    where_document={"$contains": "Python"}  # 文档必须包含"Python"
)
```

### 使用 LangChain 集成向量数据库

LangChain 是一个流行的 LLM 应用开发框架，提供了向量数据库的统一接口：

```bash
pip install langchain langchain-chroma langchain-openai
```

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# 创建嵌入模型
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# 创建向量数据库
vectorstore = Chroma.from_texts(
    texts=[
        "Python 的列表推导式是一种简洁的创建列表的方式",
        "字典是 Python 中最常用的数据结构之一",
        "装饰器可以在不修改函数代码的情况下扩展函数功能",
    ],
    embedding=embeddings,
    collection_name="python_knowledge"
)

# 创建检索器
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 创建问答链
llm = ChatOpenAI(model="gpt-4o-mini")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 提问
result = qa_chain.invoke({"query": "Python 中如何扩展函数功能？"})
print(result["result"])
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
| Python与数据库迁移 | 046-PythonDatabaseMigration | 本文的并列主题 |
| Python与OAuth2 | 047-PythonOAuth2 | 本文的并列主题 |
| Python与向量数据库 | 048-PythonVectorDatabase | 本文自身 |
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
