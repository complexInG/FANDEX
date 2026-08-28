# C# 泛型协变与逆变

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 协变 out

**基本写法：声明协变接口**
`interface I<<out T>> { }`
```csharp
// out 表示 T 只能作为返回类型
public interface IProducer<out T> { T Get(); }
```

---

**基本写法：协变赋值**
`I<<基类>> <变量> = <派生类实现>;`
```csharp
// 派生类集合可赋给基类集合
IProducer<string> sp = new StringProducer();
IProducer<object> op = sp;
```

---

**基本写法：IEnumerable 协变**
`IEnumerable<<基类>> <变量> = <派生类列表>;`
```csharp
// 内置 IEnumerable<out T> 已是协变
List<string> strs = new() { "a" };
IEnumerable<object> objs = strs;
```

---

## 逆变 in

**基本写法：声明逆变接口**
`interface I<<in T>> { }`
```csharp
// in 表示 T 只能作为参数类型
public interface IConsumer<in T> { void Process(T item); }
```

---

**基本写法：逆变赋值**
`I<<派生类>> <变量> = <基类实现>;`
```csharp
// 基类消费者可处理派生类
IConsumer<object> co = new ObjectConsumer();
IConsumer<string> cs = co;
```

---

**基本写法：Action 逆变**
`Action<<基类>> <变量> = <方法>;`
```csharp
// 内置 Action<in T> 已是逆变
Action<object> print = o => Console.WriteLine(o);
Action<string> printStr = print;
```

---

## Func 协变逆变

**基本写法：Func 的协变与逆变**
`Func<<in T, out TResult>>`
```csharp
// 输入参数逆变，返回值协变
Func<object, string> f = o => o.ToString();
Func<string, object> g = f;
```

---

## 协变限制

**基本写法：类不支持协变**
`// class 不支持 out/in`
```csharp
// 泛型类不能声明协变逆变
// 只有接口和委托可以
public class Box<T> { } // 不能加 out
```

---

**基本写法：协变类型不能作参数**
`// out T 不能作为方法参数`
```csharp
// 协变接口内 T 仅能用于返回
public interface IProducer<out T>
{
    T Get();           // 合法
    // void Set(T x);  // 非法
}
```

---

**基本写法：逆变类型不能作返回**
`// in T 不能作为返回类型`
```csharp
// 逆变接口内 T 仅能用于参数
public interface IConsumer<in T>
{
    void Process(T x); // 合法
    // T Get();         // 非法
}
```

---

## 数组协变陷阱

**基本写法：数组协变**
`<基类>[] <变量> = <派生类数组>;`
```csharp
// 数组支持协变但有运行时风险
string[] strs = new[] { "a" };
object[] objs = strs;
// objs[0] = 1; // 运行时抛 ArrayTypeMismatchException
```

---

## 自定义协变示例

**基本写法：协变栈只读视图**
`interface I<out T> IReadOnlyStack<T> { T Peek(); }`
```csharp
// 只读接口声明协变
public interface IReadOnlyStack<out T>
{
    T Peek();
}
public class Stack<T> : IReadOnlyStack<T>
{
    public T Peek() => default!;
}
```

---

## 委托协变逆变

**基本写法：自定义委托协变**
`public delegate T <委托名><out T>();`
```csharp
// 返回类型协变委托
public delegate T Producer<out T>();
Producer<string> sp = () => "hi";
Producer<object> op = sp;
```

---

**基本写法：自定义委托逆变**
`public delegate void <委托名><in T>(T <参数>);`
```csharp
// 参数类型逆变委托
public delegate void Consumer<in T>(T item);
Consumer<object> co = o => { };
Consumer<string> cs = co;
```

---

## 协变与多态场景

**基本写法：返回协变集合**
`IEnumerable<<基类>> <方法>()`
```csharp
// 方法返回基类型接口，实际返回派生集合
public IEnumerable<Animal> GetAnimals() => new List<Dog>();
```

---

**基本写法：接受逆变回调**
`void <方法>(Action<<基类>> <回调>)`
```csharp
// 接受基类型回调，传入时传派生类型处理器
public void ForEach(Action<object> action) { }
ForEach(o => Print(o));
```

---

## 协变判定

**基本写法：判断是否可赋值**
`typeof(I<<基类>>).IsAssignableFrom(typeof(I<<派生类>>));`
```csharp
// 运行时判断协变兼容性
bool ok = typeof(IEnumerable<object>).IsAssignableFrom(typeof(IEnumerable<string>));
```

---

## 常用协变逆变接口

**基本写法：内置协变接口**
`<接口><<out T>>`
```csharp
// .NET 内置协变接口
// IEnumerable<out T>
// IEnumerator<out T>
// IQueryable<out T>
// IComparable<in T>      逆变
// IEqualityComparer<in T> 逆变
```

---

**基本写法：内置逆变比较器**
`IComparer<<in T>>`
```csharp
// 基类比较器可用于派生类
IComparer<object> objComp = Comparer<object>.Default;
IComparer<string> strComp = objComp;
```
