# C# Span 与 Memory

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Span 基础

**基本写法：从数组创建 Span**
`Span<<类型>> <变量> = <数组>;`
```csharp
// 数组隐式转换为 Span，零拷贝
int[] arr = { 1, 2, 3 };
Span<int> span = arr;
```

---

**基本写法：切片 Slice**
`<span>.Slice(<起始> [, <长度>]);`
```csharp
// 取子段，不分配内存
Span<int> sub = span.Slice(1, 2);
```

---

**基本写法：索引访问与修改**
`<span>[<索引>] = <值>;`
```csharp
// 直接修改底层内存
span[0] = 10;
```

---

**基本写法：从字符串创建**
`ReadOnlySpan<<类型>> <变量> = <字符串>.AsSpan();`
```csharp
// 字符串切片零分配
ReadOnlySpan<char> s = "hello".AsSpan();
ReadOnlySpan<char> sub = s.Slice(1, 3); // "ell"
```

---

**基本写法：栈分配数组**
`Span<<类型>> <变量> = stackalloc <类型>[<大小>];`
```csharp
// 栈上分配，方法结束自动释放
Span<int> buf = stackalloc int[16];
```

---

## Span 遍历与操作

**基本写法：遍历 Span**
`foreach (var <项> in <span>) { }`
```csharp
// 高效遍历
foreach (int v in span) { }
```

---

**基本写法：填充 Fill**
`<span>.Fill(<值>);`
```csharp
// 全部填充为指定值
span.Fill(0);
```

---

**基本写法：复制 CopyTo**
`<span>.CopyTo(<目标>);`
```csharp
// 复制到另一 Span
span.CopyTo(dest);
```

---

**基本写法：清空 Clear**
`<span>.Clear();`
```csharp
// 清空所有元素为默认值
span.Clear();
```

---

**基本写法：反转 Reverse**
`<span>.Reverse();`
```csharp
// 原地反转
span.Reverse();
```

---

**基本写法：转换为数组**
`<span>.ToArray();`
```csharp
// 拷贝为新数组
int[] copy = span.ToArray();
```

---

## ReadOnlySpan 只读

**基本写法：声明只读 Span**
`ReadOnlySpan<<类型>> <变量> = <源>;`
```csharp
// 不可修改的视图
ReadOnlySpan<int> r = arr;
```

---

**基本写法：字面量直接赋值**
`ReadOnlySpan<<类型>> <变量> = [<元素>];`
```csharp
// C# 12 集合表达式直接生成
ReadOnlySpan<int> s = [1, 2, 3];
```

---

## Memory 与堆存储

**基本写法：创建 Memory**
`Memory<<类型>> <变量> = <数组>;`
```csharp
// Memory 可存储在堆上，可跨 await
Memory<int> mem = arr;
```

---

**基本写法：Memory 转 Span**
`<memory>.Span`
```csharp
// 通过属性获取 Span
Span<int> span = mem.Span;
```

---

**基本写法：Memory 切片**
`<memory>.Slice(<起始> [, <长度>]);`
```csharp
// 取子段
Memory<int> sub = mem.Slice(0, 2);
```

---

**基本写法：跨异步传递**
`async Task <方法>(Memory<<类型>> <参数>)`
```csharp
// Memory 可安全跨 await 使用
async Task ProcessAsync(Memory<byte> buf)
{
    await Task.Delay(10);
    Span<byte> s = buf.Span;
}
```

---

## 与字符串操作

**基本写法：字符串切片避免分配**
`<字符串>.AsSpan().Slice(<起始>, <长度>)`
```csharp
// 替代 Substring 避免分配
ReadOnlySpan<char> sub = "abcdef".AsSpan(1, 3); // "bcd"
```

---

**基本写法：解析数字**
`int.TryParse(<span>, out <值>);`
```csharp
// 直接从 Span 解析，无中间字符串
if (int.TryParse("42".AsSpan(), out int n)) { }
```

---

**基本写法：比较字符串**
`<span1>.SequenceEqual(<span2>);`
```csharp
// 逐字符比较
bool same = "abc".AsSpan().SequenceEqual("abc".AsSpan());
```

---

## 二进制与流

**基本写法：从 byte 数组读取结构**
`BinaryPrimitives.ReadInt32LittleEndian(<span>);`
```csharp
// 按小端序读取 4 字节整数
int value = BinaryPrimitives.ReadInt32LittleEndian(bytes);
```

---

**基本写法：写入结构**
`BinaryPrimitives.WriteInt32BigEndian(<span>, <值>);`
```csharp
// 按大端序写入
BinaryPrimitives.WriteInt32BigEndian(bytes, 42);
```

---

**基本写法：流读取到 Span**
`<流>.Read(<span>);`
```csharp
// 直接读入 Span 缓冲区
int read = stream.Read(buf);
```

---

**基本写法：流写入 Span**
`<流>.Write(<只读span>);`
```csharp
// 从只读 Span 写入流
stream.Write(data);
```

---

## Span 与 ref 结构

**基本写法：ref struct 声明**
`public ref struct <结构名> { }`
```csharp
// ref struct 只能存在于栈上
public ref struct Scanner
{
    public ReadOnlySpan<char> Buffer;
}
```

---

**基本写法：ref struct 限制**
`// 不能装箱、不能作为字段、不能跨 await`
```csharp
// ref struct 不能被装箱为 object
// 不能作为 class 的字段
// 不能在 async 方法中跨 await 使用
```

---

## 高性能模式

**基本写法：Unsafe 操作**
`Unsafe.As<<源类型>, <目标类型>>(ref <变量>);`
```csharp
// 类型重解释，零拷贝
ref int asInt = ref Unsafe.As<byte, int>(ref bytes[0]);
```

---

**基本写法：ref 返回**
`public ref <类型> <方法>()`
```csharp
// 返回引用避免拷贝
public ref int Get(int[] arr) => ref arr[0];
```

---

**基本写法：CollectionsMarshal 访问 List 内部**
`CollectionsMarshal.AsSpan(<list>);`
```csharp
// .NET 6+ 直接获取 List 内部 Span
Span<int> s = CollectionsMarshal.AsSpan(list);
```

---

**基本写法：MemoryMarshal 转换**
`MemoryMarshal.Cast<<源>, <目标>>(<span>);`
```csharp
// 字节与结构体互转
Span<int> ints = MemoryMarshal.Cast<byte, int>(bytes);
```
