---
order: 410
title: C# 正则表达式
module: 015-csharp
category: '015-csharp'
difficulty: beginner
description: C# 正则表达式 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基本匹配

**基本写法：静态匹配**
`Regex.IsMatch(<输入>, "<模式>" [, <选项>]);`
```csharp
// 判断是否匹配
bool ok = Regex.IsMatch("abc123", @"\d+");
```

---

**基本写法：提取匹配**
`Regex.Match(<输入>, "<模式>");`
```csharp
// 获取第一个匹配
Match m = Regex.Match("phone: 13800001234", @"\d+");
if (m.Success) Console.WriteLine(m.Value);
```

---

**基本写法：提取所有匹配**
`Regex.Matches(<输入>, "<模式>");`
```csharp
// 获取所有匹配
foreach (Match m in Regex.Matches("a1 b2 c3", @"\d"))
{
    Console.WriteLine(m.Value);
}
```

---

**基本写法：编译正则**
`Regex.<变量> = new Regex("<模式>", RegexOptions.Compiled);`
```csharp
// 编译为 IL，多次使用更快
var re = new Regex(@"\d+", RegexOptions.Compiled);
```

---

## 替换与分割

**基本写法：替换匹配**
`Regex.Replace(<输入>, "<模式>", "<替换>");`
```csharp
// 替换所有匹配
string result = Regex.Replace("hello 123", @"\d", "*");
```

---

**基本写法：替换回调**
`Regex.Replace(<输入>, "<模式>", <MatchEvaluator>);`
```csharp
// 用函数动态生成替换值
string result = Regex.Replace("a1 b2", @"\d", m => (int.Parse(m.Value) + 1).ToString());
```

---

**基本写法：分割字符串**
`Regex.Split(<输入>, "<模式>");`
```csharp
// 按模式分割
string[] parts = Regex.Split("a,b;c", @"[,;]");
```

---

## 分组捕获

**基本写法：捕获组**
`Regex.Match(<输入>, "(<分组>)");`
```csharp
// 用括号定义捕获组
Match m = Regex.Match("2024-01-01", @"(\d+)-(\d+)-(\d+)");
string year = m.Groups[1].Value;
```

---

**基本写法：命名分组**
`(?<<名称>><模式>)`
```csharp
// 命名捕获组
Match m = Regex.Match("Alice:30", @"(?<name>\w+):(?<age>\d+)");
string name = m.Groups["name"].Value;
```

---

**基本写法：替换引用分组**
`Regex.Replace(<输入>, "<模式>", "<$组名>");`
```csharp
// 在替换中引用命名组
string result = Regex.Replace("2024-01", @"(\d+)-(\d+)", "$2/$1");
```

---

**基本写法：非捕获组**
`(?:<模式>)`
```csharp
// 仅分组不捕获
Match m = Regex.Match("abc", @"(?:ab)+c");
```

---

## 选项标志

**基本写法：忽略大小写**
`RegexOptions.IgnoreCase`
```csharp
// 忽略大小写匹配
bool ok = Regex.IsMatch("Hello", "hello", RegexOptions.IgnoreCase);
```

---

**基本写法：多行模式**
`RegexOptions.Multiline`
```csharp
// ^ $ 匹配每行开头结尾
var re = new Regex(@"^\w+", RegexOptions.Multiline);
```

---

**基本写法：单行模式**
`RegexOptions.Singleline`
```csharp
// . 匹配换行符
var re = new Regex(@"<div>.*?</div>", RegexOptions.Singleline);
```

---

**基本写法：忽略空白**
`RegexOptions.IgnorePatternWhitespace`
```csharp
// 模式中的空白被忽略，可写注释
var re = new Regex(@"
    \d+      # 数字部分
    -        # 分隔符
    \d+      # 数字部分
", RegexOptions.IgnorePatternWhitespace);
```

---

## 常用模式

**基本写法：匹配邮箱**
`@"[\w.+-]+@[\w-]+\.[\w.]+"`
```csharp
// 简易邮箱匹配
bool ok = Regex.IsMatch("a@b.com", @"[\w.+-]+@[\w-]+\.[\w.]+");
```

---

**基本写法：匹配 URL**
`@"https?://[\w./?-]+"`
```csharp
// 简易 URL 匹配
Match m = Regex.Match(text, @"https?://[\w./?-]+");
```

---

**基本写法：匹配 IPv4**
`@"\d{1,3}(\.\d{1,3}){3}"`
```csharp
// 简易 IPv4 匹配
bool ok = Regex.IsMatch("192.168.1.1", @"\d{1,3}(\.\d{1,3}){3}");
```

---

**基本写法：匹配中文**
`@"[\u4e00-\u9fa5]+"`
```csharp
// 匹配连续中文字符
Match m = Regex.Match("hello 世界", @"[\u4e00-\u9fa5]+");
```

---

## 超时与安全

**基本写法：设置超时**
`new Regex("<模式>", <选项>, <超时>);`
```csharp
// 防止 ReDoS 拒绝服务
var re = new Regex(@"^(a+)+$", RegexOptions.None, TimeSpan.FromSeconds(1));
```

---

**基本写法：try-catch 超时**
`try { } catch (RegexMatchTimeoutException) { }`
```csharp
// 捕获正则匹配超时
try { var m = re.Match(input); }
catch (RegexMatchTimeoutException) { }
```

---

## 生成器源生成

**基本写法：GeneratedRegex 源生成**
`[GeneratedRegex("<模式>", <选项>)]`
```csharp
// .NET 7+ 编译时生成正则实现
public partial class MyRegex
{
    [GeneratedRegex(@"\d+")]
    public static partial Regex Numbers();
}
// 使用：MyRegex.Numbers().Match(input)
```

---

## 字符类速查

**基本写法：常用字符类**
`<字符类>`
```csharp
// \d 数字 \D 非数字
// \w 字母数字下划线 \W 非
// \s 空白 \S 非空白
// . 任意字符（除换行）
// [a-z] 字符区间 [^a-z] 取反
```

---

**基本写法：量词**
`<量词>`
```csharp
// * 0 次或多次
// + 1 次或多次
// ? 0 次或 1 次
// {n} 恰好 n 次
// {n,} 至少 n 次
// {n,m} n 到 m 次
// *? +? ?? 惰性匹配
```

---

**基本写法：锚点**
`<锚点>`
```csharp
// ^ 字符串/行首
// $ 字符串/行尾
// \b 单词边界
// \B 非单词边界
// \A 输入开头 \z 输入结尾
```

---

**基本写法：零宽断言**
`(?=<模式>) | (?<=<模式>)`
```csharp
// 先行断言：(?=...)  后行断言：(?<=...)
// 负向先行：(?!...)  负向后行：(?<!...)
Match m = Regex.Match("a1", @"\d(?=[a-z])"); // 数字后跟字母
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
| C# LINQ 与异步速查 | 037-LinqAsync | 本文的并列主题 |
| C# LINQ 进阶操作 | 038-LinqAdvanced | 本文的并列主题 |
| C# 文件与流操作 | 039-FileAndStream | 本文的并列主题 |
| C# JSON 序列化 | 040-JsonSerialization | 本文的并列主题 |
| C# 正则表达式 | 041-RegularExpression | 本文自身 |
| C# .NET CLI 命令 | 042-DotnetCli | 本文的并列主题 |
| C# HttpClient 网络请求 | 043-NetworkingHttp | 本文的并列主题 |
