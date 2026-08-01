---
order: 57
title: Python与Django
module: python
category: Python
difficulty: intermediate
description: Django Web框架
author: fanquanpp
updated: '2026-08-01'
related:
  - python/Python与Docker
  - python/Python与Celery
  - python/Python与Redis
  - python/Python与数据库迁移
prerequisites:
  - python/语法速查
---

## 什么是 Django

Django 是一个全功能的 Python Web 框架，它遵循"内置电池"（batteries included）的理念，提供了开发 Web 应用所需的大部分功能：ORM、管理后台、表单处理、用户认证、URL 路由、模板引擎等。你不需要从零开始拼装各种组件，Django 开箱即用。

Django 特别适合内容管理系统、电商平台、社交网络等需要快速开发且功能丰富的 Web 应用。Instagram、Pinterest、Mozilla 等知名网站都使用 Django 构建。

## 基础概念

### MVT 架构

Django 采用 MVT（Model-View-Template）架构：

- Model（模型）：定义数据结构，与数据库交互。每个模型类对应一张数据库表
- View（视图）：处理业务逻辑，接收请求并返回响应
- Template（模板）：负责页面展示，生成 HTML

### ORM

Django 的 ORM（对象关系映射）让你用 Python 类来操作数据库，不需要手写 SQL。你定义模型类，Django 自动生成对应的数据库表，并提供查询接口。

### Admin 后台

Django 最强大的特性之一是自动生成的管理后台。只需定义模型，Django 就会自动创建一个功能完整的后台管理界面，支持增删改查、搜索、过滤等操作。

### App

Django 项目由多个 App 组成。每个 App 是一个独立的功能模块，包含自己的模型、视图、模板等。App 可以复用到不同项目中。

## 快速上手

### 安装 Django

```bash
pip install django
```

### 创建项目

```bash
# 创建 Django 项目
django-admin startproject mysite

# 进入项目目录
cd mysite

# 创建一个 App
python manage.py startapp blog
```

项目结构：

```
mysite/
  manage.py           # 管理脚本
  mysite/
    settings.py       # 项目配置
    urls.py           # 根 URL 路由
    wsgi.py           # 部署入口
  blog/
    models.py         # 数据模型
    views.py          # 视图函数
    urls.py           # App 的 URL 路由
    admin.py          # Admin 后台配置
```

### 定义模型

```python
# blog/models.py
from django.db import models

class Article(models.Model):
    """文章模型"""
    title = models.CharField('标题', max_length=200)
    content = models.TextField('内容')
    author = models.CharField('作者', max_length=100)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)
    is_published = models.BooleanField('是否发布', default=False)

    def __str__(self):
        return self.title
```

### 注册模型到 Admin

```python
# blog/admin.py
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ['title', 'author', 'created_at', 'is_published']
    # 可过滤的字段
    list_filter = ['is_published', 'created_at']
    # 可搜索的字段
    search_fields = ['title', 'content']
```

### 创建并执行迁移

```bash
# 生成迁移文件
python manage.py makemigrations

# 执行迁移（创建数据库表）
python manage.py migrate

# 创建管理员账号
python manage.py createsuperuser

# 启动开发服务器
python manage.py runserver
```

访问 http://127.0.0.1:8000/admin/ 即可使用管理后台。

## 详细用法

### 编写视图

Django 支持函数视图和类视图两种方式：

```python
# blog/views.py - 函数视图
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article

def article_list(request):
    """文章列表"""
    articles = Article.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    """文章详情"""
    article = get_object_or_404(Article, pk=pk, is_published=True)
    return render(request, 'blog/article_detail.html', {'article': article})

def article_api(request):
    """返回 JSON 格式的文章列表"""
    articles = Article.objects.filter(is_published=True).values('id', 'title', 'author')
    return JsonResponse(list(articles), safe=False)
```

```python
# blog/views.py - 类视图（更简洁，推荐）
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Article

class ArticleListView(ListView):
    """文章列表视图"""
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        # 只显示已发布的文章
        return Article.objects.filter(is_published=True).order_by('-created_at')

class ArticleDetailView(DetailView):
    """文章详情视图"""
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    """创建文章视图"""
    model = Article
    fields = ['title', 'content', 'author', 'is_published']
    template_name = 'blog/article_form.html'
    success_url = '/blog/'
```

### 配置 URL 路由

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('api/', views.article_api, name='article_api'),
]
```

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # 引入 blog 的路由
]
```

### 编写模板

```
<!-- blog/templates/blog/article_list.html -->
<html>
<head><title>文章列表</title></head>
<body>
  <h1>文章列表</h1>
  {% for article in articles %}
    <div>
      <h2><a href="{{ article.get_absolute_url }}">{{ article.title }}</a></h2>
      <p>作者: {{ article.author }} | 时间: {{ article.created_at|date:"Y-m-d" }}</p>
    </div>
  {% empty %}
    <p>暂无文章</p>
  {% endfor %}
</body>
</html>
```

### ORM 查询

```python
from .models import Article

# 基本查询
articles = Article.objects.all()                          # 查询所有
article = Article.objects.get(pk=1)                       # 按 ID 查询
articles = Article.objects.filter(is_published=True)      # 条件过滤
articles = Article.objects.exclude(author='admin')        # 排除条件

# 链式查询
articles = Article.objects.filter(
    is_published=True
).exclude(
    title__contains='测试'
).order_by('-created_at')[:10]

# 常用查询条件
Article.objects.filter(title__contains='Python')          # 标题包含
Article.objects.filter(title__startswith='Python')        # 标题以...开头
Article.objects.filter(created_at__year=2026)             # 按年份过滤
Article.objects.filter(author__in=['张三', '李四'])        # 在列表中
Article.objects.filter(content__isnull=True)              # 内容为空

# 聚合查询
from django.db.models import Count, Avg
Article.objects.aggregate(total=Count('id'))              # 总数
Article.objects.values('author').annotate(count=Count('id'))  # 按作者分组统计

# 创建和更新
article = Article.objects.create(title='新文章', content='内容', author='张三')
article.title = '修改后的标题'
article.save()

# 删除
article.delete()
Article.objects.filter(is_published=False).delete()
```

### 表单处理

```python
# blog/forms.py
from django import forms
from .models import Article

# 基于 Model 的表单
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

# 自定义表单
class ContactForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=100)
    email = forms.EmailField(label='邮箱')
    message = forms.CharField(label='留言', widget=forms.Textarea)
```

```python
# blog/views.py - 表单处理视图
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # 处理表单数据（如发送邮件）
            return render(request, 'blog/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})
```

### 用户认证

Django 内置了完整的用户认证系统：

```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def login_view(request):
    """用户登录"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')

def logout_view(request):
    """用户登出"""
    logout(request)
    return redirect('home')

# 使用装饰器保护视图
@login_required
def profile(request):
    """用户资料（需要登录才能访问）"""
    return render(request, 'profile.html')
```

## 常见场景

### Django REST Framework 构建 API

```bash
pip install djangorestframework
```

```python
# blog/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_at', 'is_published']
```

```python
# blog/api_views.py
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """文章 API 视图集（自动提供增删改查接口）"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

```python
# blog/urls.py - 添加 API 路由
from rest_framework.routers import DefaultRouter
from .api_views import ArticleViewSet

router = DefaultRouter()
router.register('api/articles', ArticleViewSet)

urlpatterns = [
    # ... 其他路由
    path('', include(router.urls)),
]
```

## 注意事项与常见错误

### settings.py 中的 DEBUG 模式

生产环境必须设置 DEBUG=False，否则会暴露敏感信息。同时需要配置 ALLOWED_HOSTS：

```python
# 生产环境配置
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

### 静态文件收集

开发时 Django 自动处理静态文件，但生产环境需要运行 collectstatic：

```bash
python manage.py collectstatic
```

### N+1 查询问题

在模板中遍历关联对象时，可能会产生大量额外查询。使用 select_related 或 prefetch_related 优化：

```python
# 不好的做法：每个文章都会额外查询一次作者信息
articles = Article.objects.all()

# 好的做法：一次性关联查询
articles = Article.objects.select_related('author').all()

# 多对多关系用 prefetch_related
articles = Article.objects.prefetch_related('tags').all()
```

### 不要在视图中写复杂逻辑

视图应该保持简洁，复杂的业务逻辑应该放在模型的方法或单独的服务层中。

## 进阶用法

### 自定义中间件

```python
# middleware.py
class SimpleLogMiddleware:
    """简单的请求日志中间件"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 请求前的处理
        print(f"请求: {request.method} {request.path}")
        response = self.get_response(request)
        # 响应后的处理
        print(f"响应状态: {response.status_code}")
        return response
```

在 settings.py 中注册：

```python
MIDDLEWARE = [
    # ...
    'myapp.middleware.SimpleLogMiddleware',
]
```

### 信号

Django 信号允许你在某些动作发生时自动执行代码：

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article

@receiver(post_save, sender=Article)
def on_article_created(sender, instance, created, **kwargs):
    """文章创建后自动执行"""
    if created:
        print(f"新文章已创建: {instance.title}")
        # 可以在这里发送通知等
```

### 使用 Django 配合 Celery

```python
# tasks.py
from celery import shared_task

@shared_task
def send_notification_email(article_id):
    """异步发送通知邮件"""
    from .models import Article
    article = Article.objects.get(pk=article_id)
    # 发送邮件的逻辑
    print(f"已发送通知: {article.title}")
```

在模型中触发异步任务：

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article
from .tasks import send_notification_email

@receiver(post_save, sender=Article)
def notify_subscribers(sender, instance, created, **kwargs):
    if created and instance.is_published:
        send_notification_email.delay(instance.id)
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
| Python与Django | 014-PythonDjango | 本文自身 |
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
