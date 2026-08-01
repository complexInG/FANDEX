---
order: 420
title: C# .NET CLI 命令
module: 015-csharp
category: '015-csharp'
difficulty: beginner
description: C# .NET CLI 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# C# .NET CLI 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SDK 与环境

**基本写法：查看版本**
`dotnet --version`
```bash
// 查看当前 .NET SDK 版本
dotnet --version
```

---

**基本写法：列出已装 SDK**
`dotnet --list-sdks`
```bash
// 列出本机所有 .NET SDK
dotnet --list-sdks
```

---

**基本写法：列出已装运行时**
`dotnet --list-runtimes`
```bash
// 列出本机所有 .NET 运行时
dotnet --list-runtimes
```

---

**基本写法：查看信息**
`dotnet --info`
```bash
// 查看 SDK 与环境详细信息
dotnet --info
```

---

## 项目创建

**基本写法：创建控制台应用**
`dotnet new console -n <项目名>`
```bash
// 创建控制台项目
dotnet new console -n MyApp
```

---

**基本写法：创建类库**
`dotnet new classlib -n <库名>`
```bash
// 创建类库项目
dotnet new classlib -n MyLib
```

---

**基本写法：创建 Web API**
`dotnet new webapi -n <项目名>`
```bash
// 创建 ASP.NET Core Web API
dotnet new webapi -n MyApi
```

---

**基本写法：指定框架**
`dotnet new console -n <项目名> -f <框架>`
```bash
// 指定目标框架
dotnet new console -n MyApp -f net8.0
```

---

**基本写法：列出模板**
`dotnet new list`
```bash
// 列出所有可用项目模板
dotnet new list
```

---

## 构建与运行

**基本写法：构建项目**
`dotnet build [<项目>] [--configuration <配置>]`
```bash
// 编译项目
dotnet build
dotnet build -c Release
```

---

**基本写法：运行项目**
`dotnet run [--project <路径>]`
```bash
// 编译并运行
dotnet run --project src/MyApp
```

---

**基本写法：运行时传参**
`dotnet run -- <参数>`
```bash
// 双横线后的参数传给程序
dotnet run -- arg1 arg2
```

---

**基本写法：清理生成**
`dotnet clean [<项目>]`
```bash
// 清理编译输出
dotnet clean
```

---

**基本写法：构建指定目标**
`dotnet build -t:<目标>`
```bash
// 执行 MSBuild 目标
dotnet build -t:Publish
```

---

## 依赖管理

**基本写法：添加包**
`dotnet add <项目> package <包名> [--version <版本>]`
```bash
// 添加 NuGet 包
dotnet add package Newtonsoft.Json --version 13.0.1
```

---

**基本写法：移除包**
`dotnet remove <项目> package <包名>`
```bash
// 移除 NuGet 包
dotnet remove package Newtonsoft.Json
```

---

**基本写法：添加项目引用**
`dotnet add <项目> reference <引用项目>`
```bash
// 添加项目引用
dotnet add src/App reference src/Lib/Lib.csproj
```

---

**基本写法：移除项目引用**
`dotnet remove <项目> reference <引用项目>`
```bash
// 移除项目引用
dotnet remove src/App reference src/Lib/Lib.csproj
```

---

**基本写法：还原依赖**
`dotnet restore [<项目>]`
```bash
// 还原 NuGet 依赖
dotnet restore
```

---

**基本写法：列出包**
`dotnet list <项目> package [--outdated]`
```bash
// 列出依赖包及可升级版本
dotnet list package --outdated
```

---

## 发布与打包

**基本写法：发布应用**
`dotnet publish -c Release -o <输出目录>`
```bash
// 发布到指定目录
dotnet publish -c Release -o ./publish
```

---

**基本写法：独立部署**
`dotnet publish -c Release --self-contained true -r <RID>`
```bash
// 包含运行时，目标机器无需装 .NET
dotnet publish -c Release --self-contained true -r win-x64
```

---

**基本写法：单文件发布**
`dotnet publish -c Release -p:PublishSingleFile=true`
```bash
// 打包为单可执行文件
dotnet publish -c Release -r linux-x64 -p:PublishSingleFile=true
```

---

**基本写法：AOT 原生编译**
`dotnet publish -p:PublishAot=true -r <RID>`
```bash
// .NET 8+ 原生 AOT 编译
dotnet publish -p:PublishAot=true -r win-x64
```

---

**基本写法：修剪未用代码**
`dotnet publish -p:PublishTrimmed=true`
```bash
// 裁剪未使用程序集以减小体积
dotnet publish -c Release -p:PublishTrimmed=true
```

---

## 测试

**基本写法：运行测试**
`dotnet test [<项目>]`
```bash
// 运行所有单元测试
dotnet test
```

---

**基本写法：过滤测试**
`dotnet test --filter <表达式>`
```bash
// 按名称过滤运行
dotnet test --filter "FullyQualifiedName~UserService"
```

---

**基本写法：生成覆盖率**
`dotnet test --collect:"XPlat Code Coverage"`
```bash
// 收集代码覆盖率（coverlet）
dotnet test --collect:"XPlat Code Coverage"
```

---

**基本写法：详细日志**
`dotnet test --logger <日志器>`
```bash
// 输出测试结果到 trx 文件
dotnet test --logger "trx;LogFileName=test.trx"
```

---

## 解决方案管理

**基本写法：创建解决方案**
`dotnet new sln -n <方案名>`
```bash
// 创建 sln 解决方案
dotnet new sln -n MySolution
```

---

**基本写法：添加项目到方案**
`dotnet sln <方案> add <项目>`
```bash
// 把项目加入解决方案
dotnet sln MySolution.sln add src/App/App.csproj
```

---

**基本写法：列出方案项目**
`dotnet sln <方案> list`
```bash
// 列出解决方案中所有项目
dotnet sln list
```

---

## 工具与缓存

**基本写法：安装全局工具**
`dotnet tool install -g <工具>`
```bash
// 全局安装 dotnet 工具
dotnet tool install -g dotnet-ef
```

---

**基本写法：更新工具**
`dotnet tool update -g <工具>`
```bash
// 更新全局工具
dotnet tool update -g dotnet-ef
```

---

**基本写法：列出工具**
`dotnet tool list -g`
```bash
// 列出已安装的全局工具
dotnet tool list -g
```

---

**基本写法：清理 NuGet 缓存**
`dotnet nuget locals all --clear`
```bash
// 清空本地 NuGet 缓存
dotnet nuget locals all --clear
```

---

## EF Core 工具

**基本写法：生成迁移**
`dotnet ef migrations add <迁移名>`
```bash
// 添加 EF Core 迁移
dotnet ef migrations add InitCreate
```

---

**基本写法：更新数据库**
`dotnet ef database update`
```bash
// 应用迁移到数据库
dotnet ef database update
```

---

**基本写法：根据数据库反向生成**
`dotnet ef dbcontext scaffold "<连接串>" <提供程序>`
```bash
// 数据库优先生成模型
dotnet ef dbcontext scaffold "Server=.;Db=App" Microsoft.EntityFrameworkCore.SqlServer
```

---

## 其他常用

**基本写法：查看帮助**
`dotnet <命令> --help`
```bash
// 查看命令帮助
dotnet run --help
```

---

**基本写法：格式化代码**
`dotnet format [<项目>]`
```bash
// 按.editorconfig 格式化代码
dotnet format
```

---

**基本写法：生成强名称密钥**
`dotnet sn -k <文件>`
```bash
// 生成强名称签名密钥对
dotnet sn -k key.snk
```

## 参考文献



Microsoft Learn C# 文档：https://learn.microsoft.com/zh-cn/dotnet/csharp/
.NET 官方文档：https://learn.microsoft.com/zh-cn/dotnet/
ASP.NET Core 文档：https://learn.microsoft.com/zh-cn/aspnet/core/
C# 语言规范：https://learn.microsoft.com/zh-cn/dotnet/csharp/language-reference/

## 延伸阅读



C# 与 .NET 生态，见 015-csharp 模块基础文档。
异步编程与 Task，见 015-csharp 模块异步文档。
SQL 与 EF Core，见 019-sql 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 .NET 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C# 概述与环境配置 | 001-COverviewEnvSetup | 本文的前置基础 |
| C# 基础语法 | 002-CBasicSyntax | 本文的前置基础 |
| C# 面向对象编程 | 003-COOP | 本文的并列主题 |
| C# 泛型与集合 | 004-CGenericCollection | 本文的并列主题 |
| C# 异步编程 | 005-CAsyncProgramming | 本文的并列主题 |
| C# LINQ与函数式编程 | 006-CLINQFunctionalProgramming | 本文的并列主题 |
| C# 高级特性 | 007-CAdvancedFeature | 本文的并列主题 |
| C# .NET 平台与生态 | 008-CNET | 本文的并列主题 |
| C# 测试与工程化 | 009-CTestEngineering | 本文的并列主题 |
| C# 游戏开发与Unity | 010-CGameDevUnity | 本文的并列主题 |
| LINQ深度解析 | 011-LINQDeep | 本文的并列主题 |
| 异步编程详解 | 012-AsyncProgrammingDetailed | 本文的并列主题 |
| 模式匹配 | 013-PatternMatching | 本文的并列主题 |
| C# 记录类型 | 014-CRecordType | 本文的并列主题 |
| 泛型与协变逆变 | 015-GenericCovarianceContravariance | 本文的并列主题 |
| Span与Memory | 016-SpanMemory | 本文的并列主题 |
| 源生成器 | 017-SourceGenerator | 本文的并列主题 |
| C#与Unity游戏开发 | 018-CUnityGameDev | 本文的并列主题 |
| C#与Blazor | 019-CBlazor | 本文的并列主题 |
| C#与MAUI | 020-CMAUI | 本文的并列主题 |
| C#与EF Core | 021-CEFCore | 本文的并列主题 |
| C#与依赖注入 | 022-CDependencyInjection | 本文的并列主题 |
| C#与最小API | 023-CAPI | 本文的并列主题 |
| C#12与C#13新特性 | 024-C12C13NewFeatures | 本文的并列主题 |
| C#与反射 | 025-CSharpReflection | 本文的并列主题 |
| LINQ延迟与立即执行 | 026-LINQDeferredImmediate | 本文的并列主题 |
| async-await状态机 | 027-AsyncAwaitStateMachine | 本文的并列主题 |
| 委托与事件底层原理 | 028-DelegateEventUnderlying | 本文的原理深化 |
| 反射与特性应用 | 029-ReflectionAndFeatureApplication | 本文的并列主题 |
| Entity-Framework-Core迁移与优化 | 030-EFCoreMigrationOptimization | 本文的性能延伸 |
| ASP-NET-Core中间件管道 | 031-AspNetCoreMiddlewarePipeline | 本文的并列主题 |
| 依赖注入生命周期 | 032-DILifecycle | 本文的并列主题 |
| GC代机制 | 033-GCGeneration | 本文的原理深化 |
| 值类型与引用类型 | 034-ValueTypeReferenceType | 本文的并列主题 |
| 记录类型与不可变性 | 035-RecordTypeImmutability | 本文的并列主题 |
| C# 面向对象编程 | 036-OOP | 本文的并列主题 |
| C# LINQ 与异步速查 | 037-LinqAsync | 本文的并列主题 |
| C# LINQ 进阶操作 | 038-LinqAdvanced | 本文的并列主题 |
| C# 文件与流操作 | 039-FileAndStream | 本文的并列主题 |
| C# JSON 序列化 | 040-JsonSerialization | 本文的并列主题 |
| C# 正则表达式 | 041-RegularExpression | 本文的并列主题 |
| C# .NET CLI 命令 | 042-DotnetCli | 本文自身 |
| C# HttpClient 网络请求 | 043-NetworkingHttp | 本文的并列主题 |
