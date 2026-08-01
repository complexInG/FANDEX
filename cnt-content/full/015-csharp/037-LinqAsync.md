---
order: 370
title: C# LINQ 与异步速查
module: csharp

category: '015-csharp'
difficulty: beginner
description: C# LINQ 与异步速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## LINQ 查询

**基本写法：Where 过滤**
`<集合>.Where(<谓词>);`
```csharp
// 过滤出偶数
var evens = list.Where(x => x % 2 == 0);
```

---

**基本写法：Select 转换**
`<集合>.Select(<函数>);`
```csharp
// 转换为大写
var upper = list.Select(s => s.ToUpper());
```

---

**基本写法：OrderBy 排序**
`<集合>.OrderBy(<键选择器>);`
```csharp
// 按长度排序
var sorted = list.OrderBy(s => s.Length);
```

---

**基本写法：ThenBy 二级排序**
`<有序集合>.ThenBy(<键选择器>);`
```csharp
// 先按长度，再按字母
var sorted = list.OrderBy(s => s.Length).ThenBy(s => s);
```

---

**基本写法：GroupBy 分组**
`<集合>.GroupBy(<键选择器>);`
```csharp
// 按首字母分组
var groups = list.GroupBy(s => s[0]);
```

---

**基本写法：Distinct 去重**
`<集合>.Distinct();`
```csharp
// 去除重复元素
var unique = list.Distinct();
```

---

**基本写法：Take 取前 N 个**
`<集合>.Take(<数量>);`
```csharp
// 取前 5 个
var first5 = list.Take(5);
```

---

**基本写法：Skip 跳过**
`<集合>.Skip(<数量>);`
```csharp
// 跳过前 3 个
var rest = list.Skip(3);
```

---

**基本写法：First 第一个**
`<集合>.First([<谓词>]);`
```csharp
// 第一个大于 10 的
var item = list.First(x => x > 10);
```

---

**基本写法：FirstOrDefault 默认值**
`<集合>.FirstOrDefault([<谓词>]);`
```csharp
// 找不到返回默认值
var item = list.FirstOrDefault(x => x > 100) ?? 0;
```

---

**基本写法：Any 判断存在**
`<集合>.Any([<谓词>]);`
```csharp
// 是否存在匹配元素
bool has = list.Any(x => x > 10);
```

---

**基本写法：All 全部匹配**
`<集合>.All(<谓词>);`
```csharp
// 判断是否全部为正数
bool allPositive = list.All(x => x > 0);
```

---

**基本写法：Count 计数**
`<集合>.Count([<谓词>]);`
```csharp
// 统计偶数个数
int count = list.Count(x => x % 2 == 0);
```

---

**基本写法：Sum 求和**
`<集合>.Sum([<选择器>]);`
```csharp
// 求和
int total = list.Sum();
// 按字段求和
int totalAge = users.Sum(u => u.Age);
```

---

**基本写法：Aggregate 聚合**
`<集合>.Aggregate(<初始值>, <聚合函数>);`
```csharp
// 计算阶乘
int fact = Enumerable.Range(1, 5).Aggregate(1, (a, b) => a * b);
```

---

**基本写法：ToDictionary 转 Dictionary**
`<集合>.ToDictionary(<键选择器>, [<值选择器>]);`
```csharp
// 转换为字典
var dict = list.ToDictionary(x => x.Id, x => x.Name);
```

---

## async/await 异步

**基本写法：async 方法声明**
`async <Task<返回类型>> <方法名>() { ... }`
```csharp
// 异步方法
async Task<string> GetDataAsync() {
    await Task.Delay(1000);
    return "Data";
}
```

---

**基本写法：await 等待**
`await <Task>;`
```csharp
// 等待异步操作完成
string result = await GetDataAsync();
```

---

**基本写法：Task.Run 后台执行**
`Task.Run(() => <函数>);`
```csharp
// 在线程池执行
var result = await Task.Run(() => HeavyCompute());
```

---

**基本写法：Task.Delay 延迟**
`await Task.Delay(<毫秒>);`
```csharp
// 非阻塞延迟
await Task.Delay(1000);
```

---

**基本写法：Task.WhenAll 等待全部**
`await Task.WhenAll(<task1>, <task2>);`
```csharp
// 并行执行多个任务
var t1 = GetData1Async();
var t2 = GetData2Async();
await Task.WhenAll(t1, t2);
```

---

**基本写法：Task.WhenAny 任一完成**
`await Task.WhenAny(<task1>, <task2>);`
```csharp
// 任一任务完成即返回
var completed = await Task.WhenAny(t1, t2);
```

---

## CancellationToken

**基本写法：创建 Token**
`CancellationTokenSource <变量> = new CancellationTokenSource();`
```csharp
// 创建取消源
var cts = new CancellationTokenSource();
var token = cts.Token;
```

---

**基本写法：传递 Token**
`<方法>(<参数>, <token>);`
```csharp
// 传递给异步方法
await Task.Delay(5000, token);
```

---

**基本写法：取消操作**
`<cts>.Cancel();`
```csharp
// 触发取消
cts.Cancel();
```

---

**基本写法：响应取消**
`<token>.ThrowIfCancellationRequested();`
```csharp
// 检查并抛出异常
for (int i = 0; i < 100; i++) {
    token.ThrowIfCancellationRequested();
    // 工作
}
```

---

## 并行编程

**基本写法：Parallel.For 并行循环**
`Parallel.For(<起始>, <结束>, <循环体>);`
```csharp
// 并行执行循环
Parallel.For(0, 100, i => {
    Process(i);
});
```

---

**基本写法：Parallel.ForEach 并行遍历**
`Parallel.ForEach(<集合>, <循环体>);`
```csharp
// 并行处理每个元素
Parallel.ForEach(list, item => {
    Process(item);
});
```

---

**基本写法：Parallel.Invoke 并行调用**
`Parallel.Invoke(<action1>, <action2>);`
```csharp
// 并行执行多个操作
Parallel.Invoke(
    () => DoTask1(),
    () => DoTask2()
);
```

---

## ConcurrentBag 并发集合

**基本写法：ConcurrentBag 创建**
`ConcurrentBag<<类型>> <变量> = new ConcurrentBag<<类型>>();`
```csharp
// 线程安全集合
var bag = new ConcurrentBag<int>();
bag.Add(1);
```

---

**基本写法：ConcurrentDictionary 并发字典**
`ConcurrentDictionary<<键类型>, <值类型>> <变量>;`
```csharp
// 线程安全字典
var dict = new ConcurrentDictionary<string, int>();
dict.TryAdd("a", 1);
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

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 async/await 状态机原理

async 方法被编译器转换为状态机结构：方法开始同步执行到第一个 await，之后挂起；续体在 Task 完成时调度恢复。
SynchronizationContext 决定恢复线程：UI 上下文恢复主线程，ASP.NET Core 默认无上下文（因此无需 ConfigureAwait(false)）。
Task 组合：WhenAll 并行等待，WhenAny 竞速；ValueTask 避免无等待场景的分配。
调试技巧：TaskScheduler.UnobservedTaskException 观察未处理异常；用 AsyncDiagnostics 追踪。

### 13.2 LINQ 与表达式树

LINQ 两类实现：Enumerable（委托，内存执行）与 Queryable（表达式树，可翻译）。EF Core 把表达式树翻译为 SQL。
延迟执行：Select/Where 不立即执行，foreach/ToList/Count 触发；链式查询组合灵活但注意重复枚举。
表达式树可以动态构建查询条件（组合筛选），是高级查询库的基础。
性能：复杂 LINQ 先用 EF 生成的 SQL 分析，必要时手写 SQL 或投影优化。

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
| C# LINQ 与异步速查 | 037-LinqAsync | 本文自身 |
| C# LINQ 进阶操作 | 038-LinqAdvanced | 本文的并列主题 |
| C# 文件与流操作 | 039-FileAndStream | 本文的并列主题 |
| C# JSON 序列化 | 040-JsonSerialization | 本文的并列主题 |
| C# 正则表达式 | 041-RegularExpression | 本文的并列主题 |
| C# .NET CLI 命令 | 042-DotnetCli | 本文的并列主题 |
| C# HttpClient 网络请求 | 043-NetworkingHttp | 本文的并列主题 |
