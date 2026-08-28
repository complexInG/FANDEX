# C# 13 新特性 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## params 集合

**基本写法：params ReadOnlySpan**
`void <方法>(params ReadOnlySpan<<T>> <参数>)`
```csharp
// C# 13，params 不再限于数组，可使用 Span/ReadOnlySpan
void WriteBytes(params ReadOnlySpan<byte> bytes) { }
// 调用：编译器在栈上分配，避免堆分配
WriteBytes(1, 2, 3);
```

---

**基本写法：params Span**
`void <方法>(params Span<<T>> <参数>)`
```csharp
// 可写 span 参数
void Fill(params Span<int> values) {
    for (int i = 0; i < values.Length; i++) values[i] = i;
}
```

---

**基本写法：params 接口类型**
`void <方法>(params IEnumerable<<T>> <参数>)`
```csharp
// params 可声明为 IEnumerable<T> 等接口
void Log(params IEnumerable<string> items) {
    foreach (var s in items) Console.WriteLine(s);
}
Log("a", "b", "c");
```

---

**基本写法：集合表达式传参**
`<方法>([<元素>, ...])`
```csharp
// 用集合表达式调用 params
WriteBytes([1, 2, 3]);
byte[] extra = [4, 5];
WriteBytes([1, 2, 3, .. extra]);
```

---

## 新 lock 类型

**基本写法：System.Threading.Lock**
`private Lock <字段> = new();`
```csharp
// C# 13 新锁类型，性能优于传统 monitor
using System.Threading;
private Lock _lock = new();
void DoWork() {
    lock (_lock) {
        // 临界区
    }
}
```

---

**基本写法：Lock.EnterScope**
`ref Lock.Scope <变量> = <lock>.EnterScope()`
```csharp
// 显式作用域管理
ref Lock.Scope scope = ref _lock.EnterScope();
try {
    // 临界区
} finally {
    scope.Exit();
}
```

---

## 新转义序列

**基本写法：\e 转义**
`"<内容>\e<内容>"`
```csharp
// C# 13，\e 表示 ESC 字符（ASCII 27）
string esc = "\e[31mRed\e[0m";
// 等价于旧写法 "\x1B[31mRed\x1B[0m"
```

---

## 方法组自然类型

**基本写法：方法组类型推断**
`var <变量> = <方法名>;`
```csharp
// C# 13 改进方法组的自然类型推断
static int Parse(string s) => int.Parse(s);
var p = Parse;  // 推断为 Func<string, int>
```

---

**基本写法：方法组作泛型参数**
`Method<<T>>(<方法名>)`
```csharp
// 重载解析更精确
void Run<T>(Func<T> f) { }
int GetInt() => 42;
Run(GetInt);  // T 推断为 int
```

---

## 隐式索引访问

**基本写法：初始化器中用索引**
`new <类型> { [<索引>] = <值> }`
```csharp
// 对象初始化器中支持索引器
var list = new List<int>(10) {
    [0] = 1,
    [1] = 2
};
```

---

**基本写法：末尾索引（^）**
`new <类型> { [^1] = <值> }`
```csharp
// C# 13，初始化器支持 ^ 末尾索引
var buffer = new Buffer(5) {
    [^1] = 99  // 设置最后一个元素
};
```

---

## ref 与 unsafe 扩展

**基本写法：迭代器中的 ref 局部**
`yield return ref <字段>`
```csharp
// C# 13，迭代器方法允许 ref 局部变量
static IEnumerable ref Iterate(int[] arr) {
    for (int i = 0; i < arr.Length; i++) {
        yield return arr[i];
    }
}
```

---

**基本写法：async 方法中的 unsafe**
`async Task <方法>() { unsafe { ... } }`
```csharp
// async 方法内可使用 unsafe 上下文
async Task Process() {
    unsafe {
        int* p = stackalloc int[10];
        // 指针操作
    }
    await Task.Yield();
}
```

---

## ref struct 增强

**基本写法：ref struct 实现接口**
`ref struct <名称> : <接口>`
```csharp
// C# 13，ref struct 可实现接口
interface IProcessor { void Run(); }
ref struct SpanProcessor : IProcessor {
    public void Run() { }
}
```

---

**基本写法：泛型 allows ref struct**
`void <方法><T>() where T : allows ref struct`
```csharp
// 允许 ref struct 作为泛型类型参数
void Process<T>(T item) where T : allows ref struct {
    // T 可以是 Span<int> 等 ref struct
}
Span<int> s = stackalloc int[5];
Process(s);
```

---

## partial 成员扩展

**基本写法：partial 属性**
`public partial <类型> <属性名> { get; set; }`
```csharp
// C# 13，partial 类型中可声明 partial 属性
partial class Widget {
    public partial string Name { get; set; }
}
partial class Widget {
    private string _name = "";
    public partial string Name {
        get => _name;
        set => _name = value;
    }
}
```

---

**基本写法：partial 索引器**
`public partial <类型> this[<索引>] { get; set; }`
```csharp
// partial 索引器
partial class Map {
    public partial int this[int key] { get; set; }
}
```

---

## 重载解析优先级

**基本写法：OverloadResolutionPriority**
`[OverloadResolutionPriority(<优先级>)]`
```csharp
// C# 13，库作者指定重载优先级
using System.Runtime.CompilerServices;

class Parser {
    [OverloadResolutionPriority(1)]
    public void Parse(ReadOnlySpan<char> s) { }

    [OverloadResolutionPriority(0)]
    public void Parse(string s) { }
}
```

---

## field 上下文关键字（preview）

**基本写法：field 关键字**
`public <类型> <属性> { get => field; set => field = value; }`
```csharp
// C# 13 preview，自动生成后备字段
class Person {
    public string Name {
        get;
        set => field = value?.Trim() ?? "";
    }
}
```

---

**基本写法：field 初始化**
`public <类型> <属性> = <初始值>;`
```csharp
// 半自动属性带初始值
class Counter {
    public int Count { get; set; } = 0;
    public int Doubled => field * 2; // field 引用 Count
}
```

---

## 编译与版本

**基本写法：指定语言版本**
`<LangVersion>13</LangVersion>`
```xml
<!-- .csproj 中指定 C# 13 -->
<PropertyGroup>
    <TargetFramework>net9.0</TargetFramework>
    <LangVersion>13</LangVersion>
</PropertyGroup>
```

---

**基本写法：preview 启用**
`<Features>$(Features);field-keyword</Features>`
```xml
<!-- 启用 field preview 特性 -->
<PropertyGroup>
    <Features>$(Features);field-keyword</Features>
</PropertyGroup>
```
