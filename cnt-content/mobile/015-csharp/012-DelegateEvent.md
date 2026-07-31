# C# 委托与事件

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 委托声明

**基本写法：自定义委托**
`public delegate <返回类型> <委托名>(<参数>);`
```csharp
// 声明一个委托类型
public delegate int MathOp(int a, int b);
```

---

**基本写法：实例化委托**
`<委托类型> <变量> = <方法>;`
```csharp
// 用方法初始化委托
MathOp op = Add;
int result = op(3, 4);
```

---

**基本写法：泛型委托 Func**
`Func<<T1>, <T2>, <TResult>> <变量> = <方法>;`
```csharp
// Func 最后一个参数为返回类型
Func<int, int, int> add = (a, b) => a + b;
```

---

**基本写法：泛型委托 Action**
`Action<<T1>, <T2>> <变量> = <方法>;`
```csharp
// Action 无返回值
Action<string> log = msg => Console.WriteLine(msg);
```

---

**基本写法：Predicate 谓词委托**
`Predicate<<T>> <变量> = <方法>;`
```csharp
// 返回 bool 的委托
Predicate<int> isEven = n => n % 2 == 0;
```

---

## 多播委托

**基本写法：委托合并**
`<委托1> + <委托2>;`
```csharp
// 使用 + 合并多个委托
Action<string> handler = Log;
handler += Notify;
```

---

**基本写法：委托移除**
`<委托> - <方法>;`
```csharp
// 使用 - 移除一个委托
handler -= Log;
```

---

**基本写法：获取调用列表**
`<委托>.GetInvocationList();`
```csharp
// 获取委托链中所有委托
var delegates = handler.GetInvocationList();
```

---

**基本写法：遍历逐个调用**
`foreach (var <项> in <委托>.GetInvocationList()) { }`
```csharp
// 逐个调用并捕获异常
foreach (Action<string> h in handler.GetInvocationList())
{
    try { h("msg"); } catch { }
}
```

---

## 事件声明

**基本写法：声明事件**
`public event <委托类型> <事件名>;`
```csharp
// 基于委托声明事件
public event EventHandler<EventArgs> Clicked;
```

---

**基本写法：触发事件**
`<事件名>?.Invoke(<发送者>, <参数>);`
```csharp
// 安全触发事件（无订阅者时不抛异常）
Clicked?.Invoke(this, EventArgs.Empty);
```

---

**基本写法：订阅事件**
`<对象>.<事件> += <处理函数>;`
```csharp
// 注册事件处理方法
button.Clicked += OnClicked;
```

---

**基本写法：取消订阅**
`<对象>.<事件> -= <处理函数>;`
```csharp
// 注销事件处理方法，避免内存泄漏
button.Clicked -= OnClicked;
```

---

## 自定义事件参数

**基本写法：派生 EventArgs**
`public class <类名> : EventArgs { }`
```csharp
// 自定义事件参数类
public class ValueChangedEventArgs : EventArgs
{
    public int OldValue { get; init; }
    public int NewValue { get; init; }
}
```

---

**基本写法：泛型事件委托**
`public event EventHandler<<EventArgs类型>> <事件名>;`
```csharp
// 使用泛型 EventHandler
public event EventHandler<ValueChangedEventArgs> ValueChanged;
```

---

## 事件访问器

**基本写法：自定义 add/remove**
`public event <委托类型> <事件名> { add { } remove { } }`
```csharp
// 显式实现事件访问器
private EventHandler _field;
public event EventHandler Clicked
{
    add => _field += value;
    remove => _field -= value;
}
```

---

**基本写法：线程安全加锁**
`lock (<锁对象>) { <委托> += value; }`
```csharp
// 加锁保证订阅线程安全
lock (_lock) { _field = (EventHandler)Delegate.Combine(_field, value); }
```

---

## 匿名方法与 Lambda

**基本写法：匿名方法**
`delegate(<参数>) { <语句> };`
```csharp
// 使用 delegate 关键字
Func<int, int> square = delegate(int x) { return x * x; };
```

---

**基本写法：Lambda 表达式**
`(<参数>) => <表达式>`
```csharp
// 简洁的内联函数
Func<int, int> square = x => x * x;
```

---

**基本写法：语句 Lambda**
`(<参数>) => { <语句> };`
```csharp
// 多语句 Lambda
Action<string> log = msg =>
{
    var time = DateTime.Now;
    Console.WriteLine($"{time}: {msg}");
};
```

---

**基本写法：无参数 Lambda**
`() => <表达式>`
```csharp
// 无参 Lambda
Func<int> getCount = () => items.Count;
```

---

## 闭包与捕获

**基本写法：捕获局部变量**
`Func<int> <变量> = () => <外部变量>;`
```csharp
// Lambda 捕获外部变量
int counter = 0;
Func<int> increment = () => ++counter;
```

---

**基本写法：foreach 捕获**
`foreach (var <项> in <集合>) { <委托> = () => <项>; }`
```csharp
// C# 5+ 每次循环捕获独立变量
var actions = new List<Func<int>>();
foreach (var i in new[] { 1, 2, 3 })
    actions.Add(() => i);
```

---

## 内置委托类型

**基本写法：Comparison 比较委托**
`Comparison<<T>> <变量> = (<a>, <b>) => <int>;`
```csharp
// 用于 Sort 方法的比较委托
Comparison<int> desc = (a, b) => b.CompareTo(a);
list.Sort(desc);
```

---

**基本写法：Converter 转换委托**
`Converter<<TInput>, <TOutput>> <变量> = <方法>;`
```csharp
// 用于 ConvertAll 的转换委托
Converter<string, int> parser = int.Parse;
var nums = list.ConvertAll(parser);
```

---

## 委托与异步

**基本写法：BeginInvoke 旧式异步**
`<委托>.BeginInvoke(<参数>, <回调>, <状态>);`
```csharp
// .NET Core 不支持，仅 .NET Framework
// 推荐改用 Task.Run
```

---

**基本写法：异步 Lambda**
`async (<参数>) => await <异步操作>`
```csharp
// 异步 Lambda 表达式
Func<string, Task<string>> fetch = async url => await httpClient.GetStringAsync(url);
```
