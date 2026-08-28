# C# 12 新特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 主构造函数

**基本写法：类的主构造函数**
`public class <类名>(<参数>) { }`
```csharp
// 任意 class 都可声明主构造函数，参数在类体内可用
public class UserService(ILogger logger)
{
    public void Run() => logger.Log("running");
}
```

---

**基本写法：结构体主构造函数**
`public struct <结构名>(<参数>) { }`
```csharp
// struct 也支持主构造函数
public readonly struct Point(double x, double y)
{
    public double X => x;
    public double Y => y;
}
```

---

**基本写法：主构造函数存为字段**
`<字段> = <参数>;`
```csharp
// 需要可变状态时显式存入字段
public class Counter(int initial)
{
    private int _count = initial;
    public void Increment() => _count++;
}
```

---

**基本写法：显式构造函数调用主构造函数**
`public <类名>(<参数>) : this(<主参数>) { }`
```csharp
// 显式构造函数必须调用主构造函数
public class User(string name)
{
    public User() : this("anonymous") { }
}
```

---

## 集合表达式

**基本写法：数组初始化**
`<类型>[] <变量> = [<元素>];`
```csharp
// 统一的集合语法
int[] nums = [1, 2, 3];
string[] names = ["Alice", "Bob"];
```

---

**基本写法：List 初始化**
`List<<类型>> <变量> = [<元素>];`
```csharp
// List 也可用集合表达式
List<int> list = [1, 2, 3];
```

---

**基本写法：展开元素**
`[..<集合1>, <元素>, ..<集合2>]`
```csharp
// 用 .. 展开其他集合
int[] a = [1, 2];
int[] b = [.. a, 3, 4]; // [1,2,3,4]
```

---

**基本写法：空集合**
`<类型>[] <变量> = [];`
```csharp
// 表示空集合
int[] empty = [];
```

---

**基本写法：Span 初始化**
`Span<<类型>> <变量> = [<元素>];`
```csharp
// 直接生成 Span，零分配
Span<int> span = [1, 2, 3];
```

---

## using 别名任意类型

**基本写法：别名元组类型**
`using <别名> = (<类型>, <类型>);`
```csharp
// 为元组取别名
using Point = (double X, double Y);
Point p = (1.0, 2.0);
```

---

**基本写法：别名数组与可空**
`using <别名> = <类型>[];`
```csharp
// 为数组、可空类型取别名
using Matrix = int[][];
using Name = string?;
```

---

**基本写法：别名泛型委托**
`using <别名> = <泛型类型>;`
```csharp
// 为复杂泛型类型取别名
using Handler = Action<string, int>;
Handler h = (s, n) => { };
```

---

## 默认 Lambda 参数

**基本写法：Lambda 默认参数**
`(<参数> = <默认值>) => <表达式>`
```csharp
// Lambda 支持默认参数
var greet = (string name, string greeting = "Hello") => $"{greeting}, {name}";
greet("Alice");          // Hello, Alice
greet("Bob", "Hi");      // Hi, Bob
```

---

**基本写法：Lambda params 参数**
`(params <类型>[] <参数>) => <表达式>`
```csharp
// Lambda 支持 params
var sum = (params int[] nums) => nums.Sum();
sum(1, 2, 3); // 6
```

---

## ref readonly 参数

**基本写法：ref readonly 参数**
`void <方法>(ref readonly <类型> <参数>)`
```csharp
// 按引用传递但不可修改，避免拷贝
public static double Magnitude(ref readonly Point p) => p.X + p.Y;
```

---

## 内联数组

**基本写法：声明内联数组**
`[InlineArray(<大小>)] public struct <结构名> { <字段> }`
```csharp
// 固定大小数组作为 struct 字段，无堆分配
[InlineArray(4)]
public struct Vector4
{
    private float _element;
}
```

---

**基本写法：访问内联数组**
`<变量>[<索引>]`
```csharp
// 像数组一样索引访问
var v = new Vector4();
v[0] = 1.0f;
v[1] = 2.0f;
```

---

## Experimental 实验特性

**基本写法：标记实验性 API**
`[Experimental("<诊断ID>")]`
```csharp
// 标记为实验性，使用时会发出警告
[Experimental("DIAG001")]
public class PreviewFeature { }
```

---

**基本写法：抑制实验警告**
`#pragma warning disable <诊断ID>`
```csharp
// 显式抑制实验性警告
#pragma warning disable DIAG001
var f = new PreviewFeature();
#pragma warning restore DIAG001
```

---

## 拦截器（预览）

**基本写法：声明拦截器**
`[InterceptsLocation(<文件>, <行>, <列>)]`
```csharp
// 预览特性：源生成器在编译期替换方法调用
[InterceptsLocation("Program.cs", line: 10, character: 5)]
public static void Intercept(this void m) { }
```

---

## 其他改进

**基本写法：ref 局部变量重新赋值**
`ref <类型> <变量> = ref <其他>;`
```csharp
// ref 局部变量可重新指向
ref int r = ref a;
r = ref b; // 重新指向 b
```

---

**基本写法：循环迭代器改进**
`foreach (var <项> in <集合>)`
```csharp
// 编译器对 foreach 的 span 与 SIMD 优化更好
foreach (var item in span) { }
```

---

**基本写法：设置语言版本**
`<LangVersion>12</LangVersion>`
```xml
<!-- 在 csproj 中指定 C# 12 -->
<PropertyGroup>
  <LangVersion>12</LangVersion>
  <TargetFramework>net8.0</TargetFramework>
</PropertyGroup>
```
