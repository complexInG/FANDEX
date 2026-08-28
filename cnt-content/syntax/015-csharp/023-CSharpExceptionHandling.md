# C# 异常处理 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## try-catch-finally

**基本写法：基本捕获**
`try { <代码> } catch (<异常类型> <变量>) { <处理> }`
```csharp
// 捕获指定类型异常
try {
    File.ReadAllText(path);
} catch (FileNotFoundException ex) {
    Console.WriteLine($"缺失: {ex.FileName}");
}
```

---

**基本写法：多类型捕获**
`catch (<类型A>) {} catch (<类型B>) {}`
```csharp
// 按顺序匹配，先具体后通用
try {
    DoWork();
} catch (IOException ex) {
    Console.WriteLine("IO 错误");
} catch (UnauthorizedAccessException) {
    Console.WriteLine("无权限");
}
```

---

**基本写法：不带变量捕获**
`catch (<异常类型>)`
```csharp
// 不需要异常对象时省略变量名
try { } catch (OperationCanceledException) { }
```

---

**基本写法：通用捕获**
`catch`
```csharp
// 捕获所有异常（不推荐，CLR 非异常不应捕获）
try { } catch { }
```

---

**基本写法：带 finally**
`try { } catch { } finally { <清理> }`
```csharp
// finally 必定执行（即使 return）
FileStream fs = null;
try {
    fs = File.OpenRead(path);
    return fs.ReadByte();
} finally {
    fs?.Dispose();
}
```

---

## when 异常过滤器

**基本写法：when 条件过滤**
`catch (<异常类型> <变量>) when (<条件>)`
```csharp
// 仅当条件成立才进入该 catch
try {
    DoRequest();
} catch (HttpRequestException ex) when (ex.StatusCode == 503) {
    Console.WriteLine("服务暂不可用");
} catch (HttpRequestException ex) when ((int)ex.StatusCode >= 500) {
    Console.WriteLine("其他 5xx");
}
```

---

**基本写法：基于内省的过滤**
`catch (<类型> <变量>) when (<日志判断>)`
```csharp
// 过滤器内不展开堆栈，便于诊断
catch (Exception ex) when (Log(ex)) {
    throw;
}
static bool Log(Exception ex) { /* 写日志 */ return false; }
```

---

## 主动抛出

**基本写法：抛出新异常**
`throw new <异常类型>(<消息>);`
```csharp
// 参数校验抛出
if (value < 0)
    throw new ArgumentOutOfRangeException(nameof(value));
```

---

**基本写法：重新抛出**
`throw;`
```csharp
// 保留原始堆栈
catch (Exception ex) {
    Logger.Error(ex);
    throw;
}
```

---

**基本写法：包装异常**
`throw new <异常>(<消息>, <内部异常>);`
```csharp
// 包装为业务异常，保留原始原因
catch (SqlException ex) {
    throw new DataAccessException("用户查询失败", ex);
}
```

---

**基本写法：null 参数检查**
`throw new ArgumentNullException(nameof(<参数>));`
```csharp
// .NET 6+ 简写 ArgumentNullException.ThrowIfNull
void Process(string input) {
    ArgumentNullException.ThrowIfNull(input);
}
```

---

## 自定义异常

**基本写法：定义异常类**
`class <名称> : Exception { }`
```csharp
// 自定义异常应继承 Exception 并标记可序列化
[Serializable]
public class BusinessException : Exception {
    public string Code { get; }
    public BusinessException(string code, string message)
        : base(message) => Code = code;
    public BusinessException(string code, string message, Exception inner)
        : base(message, inner) => Code = code;
}
```

---

**基本写法：含额外属性**
`class <名称> : Exception { public <类型> <属性> { get; } }`
```csharp
public class ValidationError : Exception {
    public string Field { get; }
    public ValidationError(string field, string msg)
        : base(msg) => Field = field;
}
```

---

## 常用异常类型

**基本写法：参数异常**
`throw new ArgumentException(<消息>, <参数名>);`
```csharp
// 参数不合法
if (string.IsNullOrWhiteSpace(name))
    throw new ArgumentException("名称不能为空", nameof(name));
```

---

**基本写法：索引越界**
`throw new IndexOutOfRangeException();`
```csharp
// 数组/集合索引越界
if (i >= arr.Length) throw new IndexOutOfRangeException();
```

---

**基本写法：不支持操作**
`throw new NotSupportedException(<消息>);`
```csharp
// 接口方法在本实现中不支持
public void Delete() => throw new NotSupportedException();
```

---

**基本写法：无效操作**
`throw new InvalidOperationException(<消息>);`
```csharp
// 对象状态不允许该操作
if (_closed) throw new InvalidOperationException("已关闭");
```

---

## 异步异常

**基本写法：async 方法抛出**
`async Task <方法>() { throw new <异常>(); }`
```csharp
// 异步方法抛出的异常封装在 Task 内
async Task<int> ReadAsync() {
    throw new IOException("读取失败");
}
```

---

**基本写法：await 时捕获**
`try { await <任务> } catch (<类型>) {}`
```csharp
// 在 await 处解包异常
try {
    await ReadAsync();
} catch (IOException ex) {
    Console.WriteLine(ex.Message);
}
```

---

**基本写法：AggregateException 展平**
`<Aggregate>.Flatten()`
```csharp
// 多任务异常合并
try {
    Task.WaitAll(t1, t2);
} catch (AggregateException ae) {
    foreach (var ex in ae.Flatten().InnerExceptions) {
        Console.WriteLine(ex.Message);
    }
}
```

---

**基本写法：仅观察第一个异常**
`<Task>.Exception.GetBaseException()`
```csharp
// 取根因
var root = task.Exception?.GetBaseException();
```

---

## 异常处理模式

**基本写法：try-when 过滤重试**
`catch (<类型> <变量>) when (<重试条件>)`
```csharp
// 基于 when 实现重试
int retry = 0;
while (true) {
    try { CallApi(); break; }
    catch (HttpRequestException ex) when (retry++ < 3) {
        await Task.Delay(1000 * retry);
    }
}
```

---

**基本写法：全局未处理异常**
`AppDomain.CurrentDomain.UnhandledException`
```csharp
// 注册全局兜底处理
AppDomain.CurrentDomain.UnhandledException += (s, e) => {
    var ex = e.ExceptionObject as Exception;
    Logger.Crash(ex);
};
```

---

**基本写法：Task 未观察异常**
`TaskScheduler.UnobservedTaskException`
```csharp
// 处理未被 await 的 Task 异常
TaskScheduler.UnobservedTaskException += (s, e) => {
    Logger.Error(e.Exception);
    e.SetObserved();
};
```

---

## 异常与 IDisposable

**基本写法：using 自动释放**
`using var <变量> = <资源>;`
```csharp
// 异常发生时仍保证 Dispose 调用
using var fs = new FileStream(path, FileMode.Open);
using var sr = new StreamReader(fs);
return sr.ReadToEnd();
```

---

**基本写法：try-finally 手动释放**
`try { } finally { <资源>?.Dispose(); }`
```csharp
// 无法使用 using 时手动清理
IDisposable resource = Acquire();
try { Use(resource); }
finally { resource?.Dispose(); }
```
