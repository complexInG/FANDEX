---
order: 10
title: csharp 模块文档合集
module: 'csharp'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：015-csharp/001-CGenericCollection.md ============ -->

# C# 泛型与集合

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型类与方法

**基本写法：泛型类定义**
`public class <类名><T> { ... }`
```csharp
// 定义类型参数化的泛型类
public class Repository<T>
{
    private readonly List<T> _items = [];
}
```

---

**基本写法：泛型类带约束**
`public class <类名><T> where T : <约束> { ... }`
```csharp
// 定义带约束的泛型类
public class Repository<T> where T : class
{
    public T? FindById(int id) => _items.FirstOrDefault();
}
```

---

**基本写法：泛型方法**
`public static <返回类型> <方法名><T>(<参数>)`
```csharp
// 方法定义类型参数
public static void Swap<T>(ref T a, ref T b)
{
    (a, b) = (b, a);
}
```

---

**基本写法：泛型方法带约束**
`public static <返回类型> <方法名><T>(<参数>) where T : <约束>`
```csharp
// 带约束的泛型方法
public static T Max<T>(T a, T b) where T : IComparable<T>
{
    return a.CompareTo(b) >= 0 ? a : b;
}
```

---

**基本写法：多类型参数泛型方法**
`public static <返回类型> <方法名><T1, T2>(<参数>)`
```csharp
// 多类型参数的泛型方法
public static TResult Convert<TInput, TResult>(
    TInput input, Func<TInput, TResult> converter)
{
    return converter(input);
}
```

---

## 泛型约束

**基本写法：class 引用类型约束**
`where T : class`
```csharp
// 限制泛型参数为引用类型
public class Repository<T> where T : class { }
```

---

**基本写法：struct 值类型约束**
`where T : struct`
```csharp
// 限制泛型参数为值类型
public class NumberProcessor<T> where T : struct { }
```

---

**基本写法：new 无参构造约束**
`where T : new()`
```csharp
// 限制泛型参数有无参公共构造函数
public class Factory<T> where T : new()
{
    public T Create() => new T();
}
```

---

**基本写法：基类约束**
`where T : <基类>`
```csharp
// 限制泛型参数继承自指定基类
public class AnimalProcessor<T> where T : Animal { }
```

---

**基本写法：接口约束**
`where T : <接口>`
```csharp
// 限制泛型参数实现指定接口
public class Comparer<T> where T : IComparable<T> { }
```

---

**基本写法：unmanaged 约束**
`where T : unmanaged`
```csharp
// 限制泛型参数为非托管类型
public class NativeBuffer<T> where T : unmanaged { }
```

---

**单行写法：多约束**
`where <参数> : <约束1>, <约束2>`
```csharp
// 单行声明多个约束
public class Service<T> where T : class, ICloneable { }
```

---

**换行写法：多类型参数多约束**
`where <参数1> : <约束> where <参数2> : <约束>`
```csharp
// 换行声明多类型参数的约束
public class Service<TInput, TOutput>
    where TInput : class, ICloneable
    where TOutput : new()
{
    public TOutput Process(TInput input) => new TOutput();
}
```

---

## 协变与逆变

**基本写法：协变接口**
`interface <接口名><out T> { T <方法>(); }`
```csharp
// 协变接口允许子类型到父类型转换
public interface IProducer<out T>
{
    T Produce();
}
```

---

**基本写法：协变接口转换**
`<父接口> <变量> = <实现类>;`
```csharp
// 协变允许 string producer 转换为 object producer
IProducer<object> producer = new StringProducer();
```

---

**基本写法：IEnumerable 协变**
`IEnumerable<<父类型>> <变量> = <子类型集合>;`
```csharp
// 内置 IEnumerable<out T> 协变
IEnumerable<string> strings = new List<string> { "a", "b" };
IEnumerable<object> objects = strings;
```

---

**基本写法：逆变接口**
`interface <接口名><in T> { void <方法>(T <参数>); }`
```csharp
// 逆变接口允许父类型到子类型转换
public interface IConsumer<in T>
{
    void Consume(T item);
}
```

---

**基本写法：逆变接口转换**
`<子接口> <变量> = <实现类>;`
```csharp
// 逆变允许 object consumer 转换为 string consumer
IConsumer<string> consumer = new ObjectConsumer();
```

---

## List\<T\>

**基本写法：List 初始化**
`var <变量> = new List<<类型>> { <元素>, ... };`
```csharp
// 初始化列表
var list = new List<int> { 1, 2, 3, 4, 5 };
```

---

**基本写法：List 添加元素**
`<列表>.Add(<元素>);`
```csharp
// 向列表末尾添加元素
list.Add(6);
```

---

**基本写法：List 批量添加**
`<列表>.AddRange(<集合>);`
```csharp
// 批量添加元素到列表
list.AddRange([7, 8, 9]);
```

---

**基本写法：List 指定位置插入**
`<列表>.Insert(<索引>, <元素>);`
```csharp
// 在指定索引位置插入元素
list.Insert(0, 0);
```

---

**基本写法：List 索引访问**
`<类型> <变量> = <列表>[<索引>];`
```csharp
// 通过索引访问列表元素
int first = list[0];
```

---

**基本写法：List 末尾访问**
`<类型> <变量> = <列表>[^1];`
```csharp
// 从末尾访问列表元素
int last = list[^1];
```

---

**基本写法：List Contains 检查**
`bool <结果> = <列表>.Contains(<元素>);`
```csharp
// 检查列表是否包含指定元素
bool has = list.Contains(3);
```

---

**基本写法：List IndexOf 定位**
`int <结果> = <列表>.IndexOf(<元素>);`
```csharp
// 获取元素首次出现的索引
int index = list.IndexOf(3);
```

---

**基本写法：List Find 查找**
`<类型> <结果> = <列表>.Find(<谓词>);`
```csharp
// 查找第一个匹配条件的元素
int found = list.Find(x => x > 5);
```

---

**基本写法：List FindAll 查找全部**
`List<<类型>> <结果> = <列表>.FindAll(<谓词>);`
```csharp
// 查找所有匹配条件的元素
List<int> allFound = list.FindAll(x => x > 3);
```

---

**基本写法：List Remove 删除**
`<列表>.Remove(<元素>);`
```csharp
// 删除第一个匹配元素
list.Remove(3);
```

---

**基本写法：List RemoveAt 索引删除**
`<列表>.RemoveAt(<索引>);`
```csharp
// 删除指定索引的元素
list.RemoveAt(0);
```

---

**基本写法：List RemoveAll 条件删除**
`<列表>.RemoveAll(<谓词>);`
```csharp
// 删除所有匹配条件的元素
list.RemoveAll(x => x > 5);
```

---

**基本写法：List 默认排序**
`<列表>.Sort();`
```csharp
// 使用默认比较器排序
list.Sort();
```

---

**基本写法：List 自定义排序**
`<列表>.Sort(<比较器>);`
```csharp
// 使用自定义比较器降序排序
list.Sort((a, b) => b.CompareTo(a));
```

---

**基本写法：List ForEach 遍历**
`<列表>.ForEach(<动作>);`
```csharp
// 对每个元素执行指定动作
list.ForEach(item => Console.WriteLine(item));
```

---

## Dictionary\<TKey, TValue\>

**基本写法：Dictionary 初始化**
`var <变量> = new Dictionary<<TKey>, <TValue>> { [<键>] = <值>, ... };`
```csharp
// 初始化字典
var dict = new Dictionary<string, int>
{
    ["apple"] = 5,
    ["banana"] = 3
};
```

---

**基本写法：Dictionary Add 添加**
`<字典>.Add(<键>, <值>);`
```csharp
// 添加键值对（键不存在时）
dict.Add("grape", 4);
```

---

**基本写法：Dictionary 索引赋值**
`<字典>[<键>] = <值>;`
```csharp
// 添加或更新键值对
dict["mango"] = 6;
```

---

**基本写法：Dictionary TryAdd 尝试添加**
`bool <结果> = <字典>.TryAdd(<键>, <值>);`
```csharp
// 尝试添加键值对
dict.TryAdd("pear", 2);
```

---

**基本写法：Dictionary 索引访问**
`<值类型> <变量> = <字典>[<键>];`
```csharp
// 通过键获取值（键不存在抛异常）
int count = dict["apple"];
```

---

**基本写法：Dictionary TryGetValue 安全访问**
`bool <结果> = <字典>.TryGetValue(<键>, out <输出变量>);`
```csharp
// 安全获取值，返回是否成功
if (dict.TryGetValue("banana", out int value))
{
    Console.WriteLine($"banana: {value}");
}
```

---

**基本写法：Dictionary 默认值访问**
`<值类型> <变量> = <字典>.GetValueOrDefault(<键>, <默认值>);`
```csharp
// 获取值或默认值
int safe = dict.GetValueOrDefault("kiwi", 0);
```

---

**基本写法：Dictionary 遍历**
`foreach (var (<键>, <值>) in <字典>)`
```csharp
// 遍历字典的键值对
foreach (var (key, val) in dict)
{
    Console.WriteLine($"{key}: {val}");
}
```

---

**基本写法：Dictionary ContainsKey 检查**
`bool <结果> = <字典>.ContainsKey(<键>);`
```csharp
// 检查字典是否包含指定键
bool hasKey = dict.ContainsKey("apple");
```

---

**基本写法：Dictionary Remove 删除**
`<字典>.Remove(<键>);`
```csharp
// 删除指定键的键值对
dict.Remove("apple");
```

---

## HashSet\<T\> 与其他集合

**基本写法：HashSet 交集**
`<集合1>.IntersectWith(<集合2>);`
```csharp
// 计算两个集合的交集
var set1 = new HashSet<int> { 1, 2, 3, 4, 5 };
var set2 = new HashSet<int> { 4, 5, 6, 7, 8 };
set1.IntersectWith(set2);
```

---

**基本写法：HashSet 并集**
`<集合1>.UnionWith(<集合2>);`
```csharp
// 计算两个集合的并集
set1.UnionWith(set2);
```

---

**基本写法：HashSet 差集**
`<集合1>.ExceptWith(<集合2>);`
```csharp
// 计算两个集合的差集
set1.ExceptWith(set2);
```

---

**基本写法：Queue 入队**
`<队列>.Enqueue(<元素>);`
```csharp
// 向队列末尾添加元素
var queue = new Queue<string>();
queue.Enqueue("第一个");
```

---

**基本写法：Queue 出队**
`<类型> <变量> = <队列>.Dequeue();`
```csharp
// 从队列头部移除并返回元素
string dequeued = queue.Dequeue();
```

---

**基本写法：Stack 压栈**
`<栈>.Push(<元素>);`
```csharp
// 向栈顶压入元素
var stack = new Stack<int>();
stack.Push(1);
```

---

**基本写法：Stack 出栈**
`<类型> <变量> = <栈>.Pop();`
```csharp
// 从栈顶弹出元素
int popped = stack.Pop();
```

---

**基本写法：PriorityQueue 入队**
`<队列>.Enqueue(<元素>, <优先级>);`
```csharp
// 按优先级入队
var pq = new PriorityQueue<string, int>();
pq.Enqueue("高优先级", 1);
```

---

**基本写法：PriorityQueue 出队**
`<类型> <变量> = <队列>.Dequeue();`
```csharp
// 取出优先级最高的元素
string highest = pq.Dequeue();
```

---

**基本写法：LinkedList 尾部添加**
`<链表>.AddLast(<元素>);`
```csharp
// 在链表末尾添加节点
var linked = new LinkedList<int>();
linked.AddLast(1);
```

---

**基本写法：LinkedList 头部添加**
`<链表>.AddFirst(<元素>);`
```csharp
// 在链表头部添加节点
linked.AddFirst(0);
```

---

## 不可变集合

**基本写法：ImmutableList 创建**
`var <变量> = ImmutableList.Create(<元素>, ...);`
```csharp
// 创建不可变列表
var list = ImmutableList.Create(1, 2, 3);
```

---

**基本写法：ImmutableList 添加**
`var <新列表> = <列表>.Add(<元素>);`
```csharp
// 添加元素返回新列表，原列表不变
var newList = list.Add(4);
```

---

**基本写法：Frozen 字典创建**
`var <变量> = <字典>.ToFrozenDictionary();`
```csharp
// 创建后不可修改，查询性能极快
var frozen = new Dictionary<string, int>
{
    ["a"] = 1, ["b"] = 2
}.ToFrozenDictionary();
```

---

## LINQ to Objects

**基本写法：Where 筛选**
`var <结果> = <集合>.Where(<谓词>);`
```csharp
// 筛选满足条件的元素
var expensive = products.Where(p => p.Price > 1000);
```

---

**基本写法：Select 投影**
`var <结果> = <集合>.Select(<选择器>);`
```csharp
// 将元素投影为新形式
var names = products.Select(p => p.Name);
```

---

**基本写法：Select 匿名类型投影**
`var <结果> = <集合>.Select(<选择器>);`
```csharp
// 投影为匿名类型
var projections = products.Select(p => new { p.Name, p.Price });
```

---

**基本写法：OrderBy 排序**
`var <结果> = <集合>.OrderBy(<键选择器>);`
```csharp
// 按指定键升序排序
var sorted = products.OrderBy(p => p.Price);
```

---

**基本写法：OrderByDescending 降序排序**
`var <结果> = <集合>.OrderByDescending(<键选择器>);`
```csharp
// 按指定键降序排序
var sortedDesc = products.OrderByDescending(p => p.Price);
```

---

**基本写法：ThenBy 多级排序**
`var <结果> = <集合>.OrderBy(<键1>).ThenBy(<键2>);`
```csharp
// 多级排序
var multiSort = products.OrderBy(p => p.Category).ThenBy(p => p.Price);
```

---

**基本写法：GroupBy 分组**
`var <结果> = <集合>.GroupBy(<键选择器>);`
```csharp
// 按指定键分组
var grouped = products.GroupBy(p => p.Category);
```

---

**基本写法：Sum 求和**
`<类型> <结果> = <集合>.Sum(<选择器>);`
```csharp
// 计算指定属性的总和
decimal total = products.Sum(p => p.Price);
```

---

**基本写法：Average 平均值**
`<类型> <结果> = <集合>.Average(<选择器>);`
```csharp
// 计算指定属性的平均值
decimal avg = products.Average(p => p.Price);
```

---

**基本写法：Count 条件计数**
`int <结果> = <集合>.Count(<谓词>);`
```csharp
// 统计满足条件的元素数量
int count = products.Count(p => p.Price > 500);
```

---

**基本写法：Skip Take 分页**
`var <结果> = <集合>.Skip(<数量>).Take(<数量>);`
```csharp
// 跳过指定数量后取指定数量
var page = products.OrderBy(p => p.Price).Skip(10).Take(5);
```

---

**基本写法：Distinct 去重**
`var <结果> = <集合>.Select(<选择器>).Distinct();`
```csharp
// 对指定属性去重
var categories = products.Select(p => p.Category).Distinct();
```

---

**基本写法：Intersect 交集**
`var <结果> = <集合1>.Intersect(<集合2>);`
```csharp
// 计算两个集合的交集
var intersect = allNames.Intersect(someNames);
```

---

**基本写法：Union 并集**
`var <结果> = <集合1>.Union(<集合2>);`
```csharp
// 计算两个集合的并集
var union = allNames.Union(someNames);
```

---

**基本写法：Except 差集**
`var <结果> = <集合1>.Except(<集合2>);`
```csharp
// 计算两个集合的差集
var except = allNames.Except(someNames);
```

---

**单行写法：查询语法**
`from <变量> in <集合> where <条件> select <结果>`
```csharp
// 单行 SQL 风格查询表达式
var query = from p in products where p.Price > 500 select p;
```

---

**换行写法：查询语法**
`from <变量> in <集合> where <条件> orderby <排序> select <结果>`
```csharp
// 换行 SQL 风格查询表达式
var query = from p in products
            where p.Price > 500
            orderby p.Price descending
            select new { p.Name, p.Price };
```

---

**基本写法：Join 连接查询**
`from <变量1> in <集合1> join <变量2> in <集合2> on <键1> equals <键2> select <结果>`
```csharp
// 连接两个集合查询
var result = from p in products
             join o in orders on p.Name equals o.ProductName
             select new { p.Name, o.Quantity };
```

---

## 迭代器 (yield)

**基本写法：yield return 惰性生成**
`yield return <值>;`
```csharp
// 惰性生成斐波那契数列
public static IEnumerable<int> Fibonacci(int count)
{
    int a = 0, b = 1;
    for (int i = 0; i < count; i++)
    {
        yield return a;
        (a, b) = (b, a + b);
    }
}
```

---

**基本写法：yield break 提前退出**
`yield break;`
```csharp
// 遇到负数时停止生成
public static IEnumerable<int> GetPositive(int[] numbers)
{
    foreach (var n in numbers)
    {
        if (n < 0) yield break;
        if (n > 0) yield return n;
    }
}
```

---

**基本写法：惰性读取文件**
`yield return <行>;`
```csharp
// 逐行惰性读取文件
public static IEnumerable<string> ReadLinesLazy(string path)
{
    using var reader = new StreamReader(path);
    while (reader.ReadLine() is string line)
    {
        yield return line;
    }
}
```

---

## 集合表达式 (C# 12)

**基本写法：数组集合表达式**
`<类型>[] <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化数组
int[] array = [1, 2, 3];
```

---

**基本写法：List 集合表达式**
`List<<类型>> <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化列表
List<string> list = ["a", "b", "c"];
```

---

**基本写法：Span 集合表达式**
`Span<<类型>> <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化 Span
Span<int> span = [1, 2, 3];
```

---

**基本写法：HashSet 集合表达式**
`HashSet<<类型>> <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化 HashSet
HashSet<string> set = ["x", "y", "z"];
```

---

**基本写法：展开运算符合并**
`<类型>[] <变量> = [..<集合1>, ..<集合2>, <元素>];`
```csharp
// 使用展开运算符合并多个集合
int[] a = [1, 2, 3];
int[] b = [4, 5, 6];
int[] combined = [..a, ..b, 7, 8];
```



<!-- ============ 文档分隔线：015-csharp/002-CAdvancedFeature.md ============ -->

# C# 高级特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Span\<T\> 与 Memory\<T\>

**基本写法：Span 从数组创建**
`Span<<类型>> <变量> = <数组>.AsSpan();`
```csharp
// 从数组创建 Span
int[] array = { 1, 2, 3, 4, 5 };
Span<int> span = array.AsSpan();
```

---

**基本写法：Span 切片**
`Span<<类型>> <变量> = <源Span>[<开始>..<结束>];`
```csharp
// 获取 Span 的切片
Span<int> slice = span[1..4];
```

---

**基本写法：Span 索引访问**
`<类型> <变量> = <Span>[<索引>];`
```csharp
// 通过索引访问 Span 元素
int first = span[0];
```

---

**基本写法：Span 修改元素**
`<Span>[<索引>] = <值>;`
```csharp
// 修改 Span 中的元素
span[0] = 100;
```

---

**基本写法：Span 遍历**
`foreach (var <变量> in <Span>)`
```csharp
// 遍历 Span 的元素
foreach (var item in span)
{
    Console.WriteLine(item);
}
```

---

**基本写法：stackalloc 栈分配**
`Span<<类型>> <变量> = stackalloc <类型>[<大小>];`
```csharp
// 在栈上分配内存
Span<int> buffer = stackalloc int[10];
```

---

**基本写法：Memory 创建**
`Memory<<类型>> <变量> = new <<类型>>[<大小>];`
```csharp
// 创建 Memory
Memory<int> memory = new int[10];
```

---

**基本写法：Memory 转 Span**
`Span<<类型>> <变量> = <Memory>.Span;`
```csharp
// 从 Memory 获取 Span
Span<int> span = memory.Span;
```

---

**基本写法：Memory 异步访问**
`async Task <方法>(Memory<<类型>> <参数>)`
```csharp
// 异步方法中使用 Memory
async Task ProcessAsync(Memory<int> memory)
{
    await Task.Delay(100);
    var span = memory.Span;
    for (int i = 0; i < span.Length; i++)
    {
        span[i] = i;
    }
}
```

---

## 反射

**基本写法：获取 Type 对象**
`Type <变量> = typeof(<类型>);`
```csharp
// 获取类型的 Type 对象
Type type = typeof(Person);
```

---

**基本写法：GetType 实例方法**
`Type <变量> = <对象>.GetType();`
```csharp
// 获取对象运行时类型
var person = new Person("张三", 25);
Type type = person.GetType();
```

---

**基本写法：获取所有属性**
`PropertyInfo[] <变量> = <Type>.GetProperties();`
```csharp
// 获取类型的所有公共属性
PropertyInfo[] properties = type.GetProperties();
```

---

**基本写法：获取所有方法**
`MethodInfo[] <变量> = <Type>.GetMethods();`
```csharp
// 获取类型的所有公共方法
MethodInfo[] methods = type.GetMethods();
```

---

**基本写法：动态创建实例**
`object <变量> = Activator.CreateInstance<<类型>>();`
```csharp
// 动态创建类型实例
object instance = Activator.CreateInstance<Person>();
```

---

**基本写法：动态获取属性值**
`object? <变量> = <属性>.GetValue(<对象>);`
```csharp
// 通过反射获取属性值
var prop = type.GetProperty("Name");
object? value = prop?.GetValue(person);
```

---

**基本写法：动态设置属性值**
`<属性>.SetValue(<对象>, <值>);`
```csharp
// 通过反射设置属性值
var prop = type.GetProperty("Name");
prop?.SetValue(person, "李四");
```

---

**基本写法：动态调用方法**
`object? <变量> = <方法>.Invoke(<对象>, <参数>);`
```csharp
// 通过反射调用方法
var method = type.GetMethod("Greet");
object? result = method?.Invoke(person, null);
```

---

## 特性 (Attribute)

**基本写法：定义特性**
`[AttributeUsage(AttributeTargets.<目标>)] public class <名称> : Attribute { ... }`
```csharp
// 定义自定义特性
[AttributeUsage(AttributeTargets.Class | AttributeTargets.Method)]
public class DescriptionAttribute : Attribute
{
    public string Text { get; }
    public DescriptionAttribute(string text) => Text = text;
}
```

---

**基本写法：应用特性**
`[<特性名>(<参数>)]`
```csharp
// 在类上应用特性
[Description("用户服务")]
public class UserService { }
```

---

**基本写法：方法应用特性**
`[<特性名>(<参数>)] public void <方法>() { ... }`
```csharp
// 在方法上应用特性
[Description("获取用户信息")]
public void GetUser() { }
```

---

**基本写法：获取特性**
`var <变量> = Attribute.GetCustomAttribute(<成员>, typeof(<特性>));`
```csharp
// 通过反射获取特性
var attr = Attribute.GetCustomAttribute(
    typeof(UserService),
    typeof(DescriptionAttribute));
```

---

**基本写法：特性带命名参数**
`[<特性名>(<位置参数>, <命名参数> = <值>)]`
```csharp
// 特性使用命名参数
[Description("用户服务", Priority = 1)]
public class UserService { }
```

---

## 表达式树

**基本写法：Lambda 表达式树**
`Expression<Func<<类型>, <返回类型>>> <变量> = <参数> => <表达式>;`
```csharp
// 创建表达式树
Expression<Func<int, int>> expr = x => x * 2;
```

---

**基本写法：编译并执行**
`Func<<类型>, <返回类型>> <变量> = <表达式>.Compile();`
```csharp
// 编译表达式树为委托
Func<int, int> func = expr.Compile();
int result = func(21);
```

---

**基本写法：参数表达式**
`ParameterExpression <变量> = Expression.Parameter(typeof(<类型>), "<名称>");`
```csharp
// 创建参数表达式
ParameterExpression param = Expression.Parameter(typeof(int), "x");
```

---

**基本写法：常量表达式**
`ConstantExpression <变量> = Expression.Constant(<值>);`
```csharp
// 创建常量表达式
ConstantExpression constant = Expression.Constant(2);
```

---

**基本写法：二元运算表达式**
`BinaryExpression <变量> = Expression.Multiply(<左>, <右>);`
```csharp
// 创建乘法表达式
BinaryExpression multiply = Expression.Multiply(param, constant);
```

---

**基本写法：构建 Lambda**
`Expression<Func<<类型>, <返回类型>>> <变量> = Expression.Lambda<<委托>>>(<主体>, <参数>);`
```csharp
// 组合表达式构建 Lambda
Expression<Func<int, int>> expr =
    Expression.Lambda<Func<int, int>>(multiply, param);
```

---

## 不安全代码与指针

**基本写法：unsafe 上下文**
`unsafe { ... }`
```csharp
// 启用不安全代码块
unsafe
{
    int x = 10;
    int* p = &x;
}
```

---

**基本写法：unsafe 方法**
`unsafe void <方法>() { ... }`
```csharp
// 声明不安全方法
unsafe void ProcessPointer(int* ptr)
{
    *ptr = 42;
}
```

---

**基本写法：指针声明**
`<类型>* <变量> = <对象>;`
```csharp
// 声明并初始化指针
int x = 10;
int* ptr = &x;
```

---

**基本写法：指针解引用**
`<类型> <变量> = *<指针>;`
```csharp
// 解引用指针获取值
int value = *ptr;
```

---

**基本写法：fixed 语句**
`fixed (<类型>* <变量> = &<字段>) { ... }`
```csharp
// 固定托管对象防止 GC 移动
int[] array = { 1, 2, 3, 4, 5 };
fixed (int* p = array)
{
    Console.WriteLine(*p);
}
```

---

**基本写法：sizeof 运算符**
`int <变量> = sizeof(<类型>);`
```csharp
// 获取类型大小
int size = sizeof(int);
```

---

## 委托与事件

**基本写法：自定义委托**
`public delegate <返回类型> <委托名>(<参数>);`
```csharp
// 定义自定义委托类型
public delegate void NotifyHandler(string message);
```

---

**基本写法：Action 委托**
`Action <变量> = () => <表达式>;`
```csharp
// 使用 Action 委托
Action action = () => Console.WriteLine("执行");
```

---

**基本写法：Action 带参数**
`Action<<类型>> <变量> = <参数> => <表达式>;`
```csharp
// 使用带参数的 Action
Action<string> log = msg => Console.WriteLine(msg);
```

---

**基本写法：Func 委托**
`Func<<类型>, <返回类型>> <变量> = <参数> => <表达式>;`
```csharp
// 使用 Func 委托
Func<int, int> square = x => x * x;
```

---

**基本写法：Predicate 委托**
`Predicate<<类型>> <变量> = <参数> => <布尔表达式>;`
```csharp
// 使用 Predicate 委托
Predicate<int> isPositive = x => x > 0;
```

---

**基本写法：事件声明**
`public event <委托类型>? <事件名>;`
```csharp
// 声明事件
public event NotifyHandler? OnNotify;
```

---

**基本写法：事件触发**
`<事件名>?.Invoke(<参数>);`
```csharp
// 触发事件
OnNotify?.Invoke("通知消息");
```

---

**基本写法：事件订阅**
`<对象>.<事件> += <处理方法>;`
```csharp
// 订阅事件
publisher.OnNotify += HandleNotify;
```

---

**基本写法：事件取消订阅**
`<对象>.<事件> -= <处理方法>;`
```csharp
// 取消订阅事件
publisher.OnNotify -= HandleNotify;
```

---

## 元组与解构

**基本写法：元组声明**
`(<类型1>, <类型2>) <变量> = (<值1>, <值2>);`
```csharp
// 创建元组
(int x, int y) point = (10, 20);
```

---

**基本写法：命名元组**
`var <变量> = (<名称1>: <值1>, <名称2>: <值2>);`
```csharp
// 创建带命名的元组
var person = (Name: "张三", Age: 25);
```

---

**基本写法：元组成员访问**
`<类型> <变量> = <元组>.<名称>;`
```csharp
// 访问元组成员
string name = person.Name;
```

---

**基本写法：元组解构**
`var (<变量1>, <变量2>) = <元组>;`
```csharp
// 解构元组
var (name, age) = person;
```

---

## 全局 using 与 Nullable

**基本写法：全局 using**
`global using <命名空间>;`
```csharp
// 全项目共享的命名空间引用
global using System;
```

---

**单行写法：全局 using 多命名空间**
`global using <命名空间1>; global using <命名空间2>;`
```csharp
// 单行声明多个全局 using
global using System; global using System.Linq;
```

---

**换行写法：全局 using 多命名空间**
`global using <命名空间1>; global using <命名空间2>;`
```csharp
// 换行声明多个全局 using
global using System;
global using System.Collections.Generic;
global using System.Linq;
global using System.Threading.Tasks;
```

---

**基本写法：启用可空引用类型**
`#nullable enable`
```csharp
// 启用可空引用类型警告
#nullable enable
string name = "张三";
```

---

**基本写法：可空引用类型变量**
`<类型>? <变量名>`
```csharp
// 标记引用类型允许为 null
string? nickname = null;
```

---

## 顶级语句与文件范围命名空间

**基本写法：顶级语句**
`<语句>;`
```csharp
// 无需 Main 方法的程序入口
var data = await FetchDataAsync();
Console.WriteLine($"获取到 {data.Length} 条记录");
```

---

**基本写法：文件范围命名空间**
`namespace <命名空间>;`
```csharp
// 单文件命名空间声明
namespace MyApp.Services;

public class UserService
{
    // 整个文件都在该命名空间下
}
```

---

## 集合表达式

**基本写法：数组集合表达式**
`<类型>[] <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化数组
int[] array = [1, 2, 3];
```

---

**基本写法：List 集合表达式**
`List<<类型>> <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化列表
List<string> list = ["a", "b", "c"];
```

---

**基本写法：展开运算符合并**
`<类型>[] <变量> = [..<集合1>, ..<集合2>, <元素>];`
```csharp
// 使用展开运算符合并多个集合
int[] a = [1, 2, 3];
int[] b = [4, 5, 6];
int[] combined = [..a, ..b, 7, 8];
```

---

## 源生成器

**基本写法：IIncrementalGenerator 接口**
`[Generator] public class <生成器名> : IIncrementalGenerator { ... }`
```csharp
// 定义增量源生成器
[Generator]
public class MyGenerator : IIncrementalGenerator
{
    public void Initialize(IncrementalGeneratorInitializationContext context)
    {
        // 生成器初始化
    }
}
```

---

**基本写法：ISourceGenerator 接口**
`[Generator] public class <生成器名> : ISourceGenerator { ... }`
```csharp
// 定义源生成器
[Generator]
public class MySourceGenerator : ISourceGenerator
{
    public void Execute(GeneratorExecutionContext context)
    {
        // 生成代码
    }
    public void Initialize(GeneratorInitializationContext context) { }
}
```

---

**基本写法：添加源代码**
`context.AddSource("<名称>", <代码>);`
```csharp
// 添加生成的源代码
context.AddSource("Generated.g.cs", """
    namespace Generated;
    public class Helper { }
    """);
```

---

## Native AOT 与互操作

**基本写法：LibraryImport 特性**
`[LibraryImport("<库>", EntryPoint = "<入口>")] public static partial <类型> <方法>(<参数>);`
```csharp
// 使用 LibraryImport 声明 P/Invoke
[LibraryImport("user32.dll", EntryPoint = "MessageBoxW")]
public static partial int MessageBox(IntPtr hWnd, string text, string caption, int options);
```

---

**基本写法：DllImport 特性**
`[DllImport("<库>")] public static extern <类型> <方法>(<参数>);`
```csharp
// 使用 DllImport 声明 P/Invoke
[DllImport("user32.dll")]
public static extern int MessageBox(IntPtr hWnd, string text, string caption, int options);
```

---

**基本写法：Marshal 字符串**
`[MarshalAs(UnmanagedType.<类型>)]`
```csharp
// 指定字符串封送方式
[DllImport("user32.dll", CharSet = CharSet.Unicode)]
public static extern int MessageBox(IntPtr hWnd, [MarshalAs(UnmanagedType.LPWStr)] string text, [MarshalAs(UnmanagedType.LPWStr)] string caption, int options);
```

---

## Span 高级操作

**基本写法：Span 转数组**
`<类型>[] <变量> = <Span>.ToArray();`
```csharp
// 将 Span 转换为数组
int[] array = span.ToArray();
```

---

**基本写法：Span Fill 填充**
`<Span>.Fill(<值>);`
```csharp
// 用指定值填充 Span
span.Fill(0);
```

---

**基本写法：Span CopyTo 复制**
`<Span>.CopyTo(<目标Span>);`
```csharp
// 将 Span 复制到目标 Span
var source = new int[] { 1, 2, 3 }.AsSpan();
var target = new int[3];
source.CopyTo(target);
```

---

**基本写法：MemoryMarshal 类型重解释**
`Span<<目标类型>> <变量> = MemoryMarshal.Cast<<源类型>, <目标类型>>(<源Span>);`
```csharp
// 零拷贝将字节数组重新解释为 int 数组
byte[] bytes = new byte[16];
Span<int> ints = MemoryMarshal.Cast<byte, int>(bytes.AsSpan());
ints[0] = 42;
```

---

## BitHelper 与位操作

**基本写法：BitConverter 转换**
`int <变量> = BitConverter.ToInt32(<字节数组>, <偏移>);`
```csharp
// 字节数组转整数
byte[] bytes = { 1, 0, 0, 0 };
int value = BitConverter.ToInt32(bytes, 0);
```

---

**基本写法：整数转字节**
`byte[] <变量> = BitConverter.GetBytes(<整数>);`
```csharp
// 整数转字节数组
byte[] bytes = BitConverter.GetBytes(42);
```

---

**基本写法：位运算**
`int <变量> = <值1> | <值2>;`
```csharp
// 位或运算
int flags = 0x01 | 0x02;
```

---

**基本写法：位与运算**
`int <变量> = <值1> & <值2>;`
```csharp
// 位与运算
int mask = flags & 0x01;
```

---

**基本写法：位移运算**
`int <变量> = <值> << <位数>;`
```csharp
// 左移运算
int shifted = 1 << 4;
```

---

## C# 13/14 新特性

**基本写法：C# 13 lock 类型**
`System.Threading.Lock`
```csharp
// C# 13 新增专用锁类型，性能优于传统 object 锁
System.Threading.Lock myLock = new();
// 使用 EnterScope 自动管理锁的进入与退出
using (myLock.EnterScope())
{
    // 临界区代码
    Console.WriteLine("已获取锁");
}
```

**基本写法：C# 13 params 集合**
`params <Collection> <参数>`
```csharp
// params 关键字支持 ReadOnlySpan、IEnumerable 等集合类型
void Process(params ReadOnlySpan<int> nums)
{
    foreach (var n in nums) Console.WriteLine(n);
}
// 也支持自定义集合类型
void Build(params List<string> items)
{
    items.ForEach(Console.WriteLine);
}
// 调用
Process(1, 2, 3);
Build(new List<string> { "a", "b" });
```

**基本写法：C# 13 escape 字符 \e**
`string <变量> = "\e";`
```csharp
// 新增 \e 转义字符表示 ESC (Unicode U+001B)
string escape = "\e";
// 用于终端控制序列
Console.WriteLine("\e[31m红色文本\e[0m");
```

**基本写法：C# 14 扩展成员**
`extension members for <类型> { }`
```csharp
// C# 14 引入扩展成员语法，统一扩展方法、属性等
extension members for string
{
    public static bool IsBlank(string s) => string.IsNullOrWhiteSpace(s);
    public string Reversed() => new string(this.Reverse().ToArray());
}
// 使用
string str = "hello";
bool blank = string.IsBlank(str);
string rev = str.Reversed();
```

**基本写法：C# 14 null 条件分配**
`<obj>?.<字段> = <值>;`
```csharp
// 仅当 obj 非空时才赋值字段
class User { public string? Name { get; set; } }
User? user = GetUser();
user?.Name = "Alice";
// 等价于 if (user != null) user.Name = "Alice";
```

**基本写法：C# 14 implicit span conversion**
`Span<<T>> <变量> = <数组>;`
```csharp
// 隐式转换：数组与 Span<T> 之间自动转换
int[] arr = { 1, 2, 3, 4, 5 };
// 数组隐式转换为 Span<T>，无需显式 AsSpan 调用
Span<int> span = arr;
ReadOnlySpan<int> ros = arr;
foreach (var v in span) Console.WriteLine(v);
```

**基本写法：C# 14 partial constructors**
`partial <类型>()`
```csharp
// partial 构造函数：将构造逻辑拆分到多个 partial 文件
partial class Service
{
    // 主文件声明 partial 构造函数
    public partial Service();
}
// 另一个文件实现
partial class Service
{
    public partial Service()
    {
        Console.WriteLine("partial 构造逻辑执行");
    }
}
```



<!-- ============ 文档分隔线：015-csharp/003-CBasicSyntax.md ============ -->

# C# 基础语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量声明

**基本写法：整数变量声明**
`int <变量名> = <整数值>;`
```csharp
// 声明整数类型变量
int age = 25;
```

---

**基本写法：字符串变量声明**
`string <变量名> = "<文本>";`
```csharp
// 声明字符串类型变量
string name = "张三";
```

---

**基本写法：浮点变量声明**
`double <变量名> = <浮点值>;`
```csharp
// 声明双精度浮点变量
double price = 99.99;
```

---

**基本写法：布尔变量声明**
`bool <变量名> = <true | false>;`
```csharp
// 声明布尔类型变量
bool isActive = true;
```

---

**基本写法：var 整数推断**
`var <变量名> = <整数值>;`
```csharp
// 编译期推断为 int
var count = 42;
```

---

**基本写法：var 字符串推断**
`var <变量名> = "<文本>";`
```csharp
// 编译期推断为 string
var message = "Hello";
```

---

**基本写法：var 数组推断**
`var <变量名> = new[] { <元素>, ... };`
```csharp
// 编译期推断为 int[]
var numbers = new[] { 1, 2, 3 };
```

---

**基本写法：var 泛型推断**
`var <变量名> = new Dictionary<<键类型>, <值类型>>();`
```csharp
// 编译期推断为 Dictionary<string, int>
var dict = new Dictionary<string, int>();
```

---

**基本写法：常量声明**
`const <类型> <常量名> = <值>;`
```csharp
// 声明编译期常量
const double Pi = 3.14159265358979;
```

---

**基本写法：字符串常量声明**
`const string <常量名> = "<文本>";`
```csharp
// 声明字符串常量
const string AppName = "FANDEX";
```

---

**基本写法：required 属性声明**
`public required <类型> <属性名> { get; init; }`
```csharp
// 声明必填的初始化属性
public required string Name { get; init; }
```

---

**单行写法：required 多属性类定义**
`public class <类名> { public required <类型1> <属性1> { get; init; } public required <类型2> <属性2> { get; init; } }`
```csharp
// 单行定义包含多个 required 属性的类
public class Person { public required string Name { get; init; } public required int Age { get; init; } }
```

---

**换行写法：required 多属性类定义**
`public class <类名> { public required <类型1> <属性1> { get; init; } public required <类型2> <属性2> { get; init; } }`
```csharp
// 换行定义包含多个 required 属性的类
public class Person
{
    public required string Name { get; init; }
    public required int Age { get; init; }
}
```

---

**基本写法：required 对象初始化**
`var <变量> = new <类名> { <属性1> = <值1>, <属性2> = <值2> };`
```csharp
// 初始化时必须为 required 属性赋值
var person = new Person { Name = "李四", Age = 30 };
```

---

## 类型转换

**基本写法：隐式转换 int 到 long**
`long <变量> = <int变量>;`
```csharp
// int 自动转换为 long
int num = 100;
long bigNum = num;
```

---

**基本写法：隐式转换 int 到 double**
`double <变量> = <int变量>;`
```csharp
// int 自动转换为 double
int num = 100;
double d = num;
```

---

**基本写法：显式转换 double 到 int**
`int <变量> = (int)<double变量>;`
```csharp
// 强制转换并截断小数部分
double pi = 3.14159;
int intPi = (int)pi;
```

---

**基本写法：Convert 字符串转整数**
`int <变量> = Convert.ToInt32(<字符串>);`
```csharp
// 使用 Convert 类将字符串转换为整数
string str = "123";
int parsed = Convert.ToInt32(str);
```

---

**基本写法：Convert 字符串转浮点**
`double <变量> = Convert.ToDouble(<字符串>);`
```csharp
// 使用 Convert 类将字符串转换为双精度浮点
double dbl = Convert.ToDouble("3.14");
```

---

**基本写法：Parse 字符串解析**
`int <变量> = int.Parse(<字符串>);`
```csharp
// 解析失败时抛出异常
int number = int.Parse("456");
```

---

**基本写法：TryParse 安全解析**
`bool <结果> = int.TryParse(<字符串>, out <输出变量>);`
```csharp
// 安全解析，返回是否成功
if (int.TryParse("789", out int result))
{
    Console.WriteLine($"解析成功: {result}");
}
```

---

**基本写法：is 类型检查并转换**
`if (<变量> is <类型> <变量名>)`
```csharp
// is 模式匹配进行类型转换
object obj = "Hello";
if (obj is string s)
{
    Console.WriteLine(s.Length);
}
```

---

**基本写法：as 引用类型转换**
`<接口>? <变量> = <对象> as <接口>;`
```csharp
// as 转换失败时返回 null
IAnimal? animal = dog as IAnimal;
```

---

## 字符串操作

**基本写法：字符串插值**
`$"文本 {<表达式>}"`
```csharp
// 基本字符串插值
var name = "世界";
Console.WriteLine($"你好, {name}!");
```

---

**基本写法：表达式插值**
`$"文本 {<表达式>}"`
```csharp
// 在插值中使用表达式
Console.WriteLine($"2 + 3 = {2 + 3}");
```

---

**基本写法：方法调用插值**
`$"文本 {<方法调用>}"`
```csharp
// 在插值中调用方法
var name = "world";
Console.WriteLine($"大写: {name.ToUpper()}");
```

---

**基本写法：格式化插值**
`$"文本 {<表达式>:<格式>}"`
```csharp
// 在插值中使用格式化
Console.WriteLine($"时间: {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
```

---

**基本写法：原始字符串字面量**
`"""<内容>"""`
```csharp
// 三引号保留原始格式
var json = """
    {
        "name": "张三",
        "age": 25
    }
    """;
```

---

**基本写法：插值原始字符串**
`$"""<内容 {<表达式>}>"""`
```csharp
// 在原始字符串中嵌入表达式
var id = 1001;
var query = $"""
    SELECT * FROM Users
    WHERE Id = {id}
    """;
```

---

**基本写法：Contains 子串检查**
`bool <结果> = <字符串>.Contains(<子串>);`
```csharp
// 检查字符串是否包含子串
string str = "Hello, C# World!";
bool contains = str.Contains("C#");
```

---

**基本写法：IndexOf 子串定位**
`int <结果> = <字符串>.IndexOf(<子串>);`
```csharp
// 获取子串首次出现的位置
string str = "Hello, C# World!";
int index = str.IndexOf("World");
```

---

**基本写法：StartsWith 前缀检查**
`bool <结果> = <字符串>.StartsWith(<前缀>);`
```csharp
// 检查字符串是否以指定前缀开头
string str = "Hello, C# World!";
bool startsWith = str.StartsWith("Hello");
```

---

**基本写法：Substring 截取子串**
`string <结果> = <字符串>.Substring(<起始>, <长度>);`
```csharp
// 从指定位置截取指定长度的子串
string str = "Hello, C# World!";
string sub = str.Substring(7, 2);
```

---

**基本写法：Split 分割字符串**
`string[] <结果> = <字符串>.Split(<分隔符>);`
```csharp
// 按分隔符拆分字符串为数组
string str = "Hello, C# World!";
string[] parts = str.Split(' ');
```

---

**基本写法：ToUpper 转大写**
`string <结果> = <字符串>.ToUpper();`
```csharp
// 将字符串转换为大写
string str = "Hello, C# World!";
string upper = str.ToUpper();
```

---

**基本写法：Trim 去空白**
`string <结果> = <字符串>.Trim();`
```csharp
// 去除字符串首尾空白
string trimmed = "  hello  ".Trim();
```

---

**基本写法：Replace 替换子串**
`string <结果> = <字符串>.Replace(<旧值>, <新值>);`
```csharp
// 替换字符串中的指定子串
string str = "Hello, C# World!";
string replaced = str.Replace("C#", "F#");
```

---

**单行写法：StringBuilder 链式构建**
`var <变量> = new StringBuilder().AppendLine(<内容>).AppendFormat(<格式>, <参数>);`
```csharp
// 单行链式调用构建字符串
var sb = new StringBuilder().AppendLine("第一行").AppendFormat("数字: {0:N2}", 1234.5678);
string result = sb.ToString();
```

---

**换行写法：StringBuilder 链式构建**
`var <变量> = new StringBuilder(); <变量>.AppendLine(<内容>); <变量>.AppendFormat(<格式>, <参数>);`
```csharp
// 换行链式调用构建字符串
var sb = new StringBuilder();
sb.AppendLine("第一行");
sb.AppendLine("第二行");
sb.AppendFormat("数字: {0:N2}", 1234.5678);
string result = sb.ToString();
```

---

## Nullable 引用类型

**基本写法：启用可空引用类型**
`#nullable enable`
```csharp
// 启用可空引用类型警告
#nullable enable
string name = "张三";
```

---

**基本写法：可空引用类型变量**
`<类型>? <变量名>`
```csharp
// 标记引用类型允许为 null
string? nickname = null;
```

---

**基本写法：空条件运算符访问属性**
`<变量>?.<属性>`
```csharp
// 当变量为 null 时返回 null
string? nickname = null;
int? length = nickname?.Length;
```

---

**基本写法：空条件运算符调用方法**
`<变量>?.<方法>()`
```csharp
// 当变量为 null 时返回 null
string? nickname = null;
string? upper = nickname?.ToUpper();
```

---

**基本写法：空合并运算符**
`<变量> ?? <默认值>`
```csharp
// 当变量为 null 时提供默认值
string? nickname = null;
string display = nickname ?? "匿名";
```

---

**基本写法：空合并赋值运算符**
`<变量> ??= <默认值>`
```csharp
// 当变量为 null 时赋值并返回
string? nickname = null;
string display2 = nickname ??= "匿名";
```

---

**基本写法：强制非空运算符**
`<变量>!`
```csharp
// 抑制 null 警告，慎用
string? nickname = null;
string forced = nickname!;
```

---

**基本写法：值类型可空声明**
`<值类型>? <变量名>`
```csharp
// 使值类型可以接受 null
int? age = null;
```

---

**基本写法：HasValue 检查**
`bool <结果> = <可空变量>.HasValue;`
```csharp
// 检查可空值类型是否有值
int? age = null;
bool hasValue = age.HasValue;
```

---

**基本写法：GetValueOrDefault 带默认值**
`int <结果> = <可空变量>.GetValueOrDefault(<默认值>);`
```csharp
// 获取值或指定默认值
int? age = null;
int value2 = age.GetValueOrDefault(18);
```

---

## 控制流

**基本写法：if-else 多分支**
`if (<条件>) <语句> else if (<条件>) <语句> else <语句>`
```csharp
// 多分支条件判断
int score = 85;
if (score >= 90)
    Console.WriteLine("优秀");
else if (score >= 80)
    Console.WriteLine("良好");
else
    Console.WriteLine("及格");
```

---

**基本写法：switch 语句**
`switch (<变量>) { case <值>: <语句>; break; default: <语句>; break; }`
```csharp
// 枚举多分支选择
var day = DayOfWeek.Monday;
switch (day)
{
    case DayOfWeek.Saturday:
    case DayOfWeek.Sunday:
        Console.WriteLine("周末");
        break;
    default:
        Console.WriteLine("工作日");
        break;
}
```

---

**基本写法：switch 表达式**
`<变量> switch { <模式> => <结果>, _ => <默认> }`
```csharp
// 基于值的表达式分支
var day = DayOfWeek.Monday;
string label = day switch
{
    DayOfWeek.Saturday or DayOfWeek.Sunday => "周末",
    _ => "工作日"
};
```

---

**基本写法：switch 类型模式**
`<变量> switch { <类型> => <结果>, _ => <默认> }`
```csharp
// 基于类型的表达式分支
object obj = 42;
string typeName = obj switch
{
    int => "整数",
    string => "字符串",
    _ => "其他"
};
```

---

**基本写法：for 循环**
`for (<初始化>; <条件>; <更新>) <循环体>`
```csharp
// 计数迭代循环
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(i);
}
```

---

**基本写法：foreach 循环**
`foreach (<类型> <变量> in <集合>) <循环体>`
```csharp
// 遍历可枚举集合
var fruits = new[] { "苹果", "香蕉", "橙子" };
foreach (var fruit in fruits)
{
    Console.WriteLine(fruit);
}
```

---

**基本写法：while 循环**
`while (<条件>) <循环体>`
```csharp
// 前置条件循环
int n = 10;
while (n > 0)
{
    Console.WriteLine(n--);
}
```

---

**基本写法：do-while 循环**
`do <循环体> while (<条件>);`
```csharp
// 至少执行一次的后置条件循环
string? input;
do
{
    Console.Write("请输入 (q 退出): ");
    input = Console.ReadLine();
} while (input != "q");
```

---

**基本写法：末尾索引**
`<数组>[^<索引>]`
```csharp
// 从末尾访问数组元素
var numbers = new[] { 10, 20, 30, 40, 50 };
int last = numbers[^1];
```

---

**基本写法：范围切片**
`<数组>[<开始>..<结束>]`
```csharp
// 获取数组的指定范围切片
var numbers = new[] { 10, 20, 30, 40, 50 };
var slice = numbers[1..4];
```

---

**基本写法：起始范围切片**
`<数组>[..<结束>]`
```csharp
// 从开头到指定位置的切片
var numbers = new[] { 10, 20, 30, 40, 50 };
var firstThree = numbers[..3];
```

---

## 模式匹配

**基本写法：is 类型与条件组合**
`if (<变量> is <类型> <变量名> and <条件>)`
```csharp
// 组合条件匹配
object value = 42;
if (value is int num and > 0 and < 100)
{
    Console.WriteLine($"0-100 之间的整数: {num}");
}
```

---

**基本写法：属性模式**
`<变量> switch { { <属性>: <值> } => <结果> }`
```csharp
// 基于对象属性值分支
public record Order(decimal Amount, string Status);
string GetDiscount(Order order) => order switch
{
    { Status: "VIP", Amount: > 1000m } => "8折",
    { Status: "VIP" } => "9折",
    _ => "无折扣"
};
```

---

**基本写法：列表模式空列表**
`<数组> switch { [] => <结果> }`
```csharp
// 匹配空列表
int[] numbers = [1, 2, 3];
string label = numbers switch
{
    [] => "空列表",
    _ => "非空列表"
};
```

---

**基本写法：列表模式单元素**
`<数组> switch { [single] => <结果> }`
```csharp
// 匹配仅含单个元素的列表
int[] numbers = [1];
string label = numbers switch
{
    [single] => $"单个元素: {single}",
    _ => "其他"
};
```

---

**基本写法：列表模式首尾匹配**
`<数组> switch { [first, .., last] => <结果> }`
```csharp
// 匹配列表的首尾元素
int[] numbers = [1, 2, 3];
string label = numbers switch
{
    [first, .., last] => $"首: {first}, 尾: {last}",
    _ => "其他"
};
```

---

**基本写法：when 守卫**
`<模式> when <条件>`
```csharp
// 为模式添加额外条件
string Classify(int[] arr) => arr switch
{
    [var a, .., var b] when a == b => "首尾相同",
    _ => "其他"
};
```

---

## 顶级语句与全局 Using

**基本写法：全局 using**
`global using <命名空间>;`
```csharp
// 全项目共享的命名空间引用
global using System;
```

---

**单行写法：全局 using 多命名空间**
`global using <命名空间1>; global using <命名空间2>;`
```csharp
// 单行声明多个全局 using
global using System; global using System.Linq;
```

---

**换行写法：全局 using 多命名空间**
`global using <命名空间1>; global using <命名空间2>;`
```csharp
// 换行声明多个全局 using
global using System;
global using System.Collections.Generic;
global using System.Linq;
global using System.Threading.Tasks;
global using System.IO;
```

---

**基本写法：文件范围命名空间**
`namespace <命名空间>;`
```csharp
// 单文件命名空间声明
namespace MyApp.Services;

public class UserService
{
    // 整个文件都在该命名空间下
}
```

---

**基本写法：顶级语句**
`<语句>;`
```csharp
// 无需 Main 方法的程序入口
var data = await FetchDataAsync();
Console.WriteLine($"获取到 {data.Length} 条记录");
```

---

## 运算符速查

**基本写法：空合并赋值**
`<变量> ??= <值>`
```csharp
// 当变量为 null 时赋值
string? name = null;
name ??= "赋值";
```

---

**基本写法：with 表达式**
`<记录> with { <属性> = <值> }`
```csharp
// 修改 record 创建副本
var original = new Point(1, 2);
var modified = original with { X = 10 };
```

---

**基本写法：集合表达式声明**
`List<<类型>> <变量> = [<元素>, ...];`
```csharp
// 使用集合表达式初始化列表
List<int> list = [1, 2, 3];
```

---

**基本写法：集合表达式展开合并**
`<类型>[] <变量> = [..<集合>, <元素>, ...];`
```csharp
// 使用展开运算符合并集合
List<int> list = [1, 2, 3];
int[] arr = [..list, 4, 5];
```



<!-- ============ 文档分隔线：015-csharp/004-CRecordType.md ============ -->

# C# 记录类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## record 定义

**基本写法：引用类型记录**
`public record <名称>(<参数列表>);`
```csharp
// 定义引用类型记录
public record Person(string Name, int Age);
```

---

**基本写法：值类型记录**
`public record struct <名称>(<参数列表>);`
```csharp
// 定义值类型记录
public record struct Point(double X, double Y);
```

---

**基本写法：不可变值类型记录**
`public readonly record struct <名称>(<参数列表>);`
```csharp
// 定义不可变值类型记录
public readonly record struct Money(decimal Amount, string Currency);
```

---

**单行写法：多参数记录定义**
`public record <名称>(<类型1> <参数1>, <类型2> <参数2>, <类型3> <参数3>);`
```csharp
// 单行定义包含多个参数的记录
public record User(string Name, int Age, string Email, string Phone);
```

---

**换行写法：多参数记录定义**
`public record <名称>(<类型1> <参数1>, <类型2> <参数2>, <类型3> <参数3>);`
```csharp
// 换行定义包含多个参数的记录
public record User(
    string Name,
    int Age,
    string Email,
    string Phone);
```

---

**基本写法：带主体的记录**
`public record <名称>(<参数列表>) { <成员> }`
```csharp
// 在记录中添加额外成员
public record Person(string Name, int Age)
{
    public bool IsAdult => Age >= 18;
}
```

---

## 值相等性

**基本写法：引用类型记录相等**
`bool <结果> = <记录1> == <记录2>;`
```csharp
// 引用类型记录基于值比较
var p1 = new Person("张三", 25);
var p2 = new Person("张三", 25);
Console.WriteLine(p1 == p2);
```

---

**基本写法：值类型记录相等**
`bool <结果> = <记录1> == <记录2>;`
```csharp
// 值类型记录基于值比较
var p1 = new Point(1.0, 2.0);
var p2 = new Point(1.0, 2.0);
Console.WriteLine(p1 == p2);
```

---

**基本写法：记录不等比较**
`bool <结果> = <记录1> != <记录2>;`
```csharp
// 记录不等比较
var p1 = new Person("张三", 25);
var p2 = new Person("李四", 30);
Console.WriteLine(p1 != p2);
```

---

**基本写法：Equals 方法**
`bool <结果> = <记录>.Equals(<其他记录>);`
```csharp
// 使用 Equals 方法比较
var p1 = new Person("张三", 25);
var p2 = new Person("张三", 25);
Console.WriteLine(p1.Equals(p2));
```

---

## with 表达式

**基本写法：with 修改单属性**
`var <变量> = <记录> with { <属性> = <值> };`
```csharp
// 非破坏性修改单个属性
var p1 = new Person("张三", 25);
var p2 = p1 with { Age = 26 };
```

---

**基本写法：with 修改多属性**
`var <变量> = <记录> with { <属性1> = <值1>, <属性2> = <值2> };`
```csharp
// 非破坏性修改多个属性
var p1 = new Person("张三", 25);
var p2 = p1 with { Name = "李四", Age = 26 };
```

---

**基本写法：with 嵌套修改**
`var <变量> = <记录> with { <属性> = <子记录> with { <子属性> = <值> } };`
```csharp
// 非破坏性修改嵌套记录
var order = new Order(new Customer("张三"), 100m);
var newOrder = order with { Customer = order.Customer with { Name = "李四" } };
```

---

## 记录继承

**基本写法：记录继承**
`public record <派生>(<参数>) : <基类>(<参数>);`
```csharp
// 记录类型支持继承
public record Student(string Name, int Age, string School) : Person(Name, Age);
```

---

**基本写法：多级记录继承**
`public record <派生>(<参数>) : <基类>(<参数>);`
```csharp
// 多级记录继承
public record GraduateStudent(string Name, int Age, string School, string Degree)
    : Student(Name, Age, School);
```

---

**基本写法：继承记录 with 表达式**
`var <变量> = <派生记录> with { <属性> = <值> };`
```csharp
// 派生记录使用 with 表达式
var student = new Student("张三", 20, "清华大学");
var olderStudent = student with { Age = 21 };
```

---

## 解构

**基本写法：记录解构**
`var (<变量1>, <变量2>) = <记录>;`
```csharp
// 解构记录的所有位置参数
var person = new Person("张三", 25);
var (name, age) = person;
```

---

**基本写法：部分解构**
`var (<变量1>, _) = <记录>;`
```csharp
// 仅解构需要的部分参数
var person = new Person("张三", 25);
var (name, _) = person;
```

---

**基本写法：解构带类型**
`(<类型1> <变量1>, <类型2> <变量2>) = <记录>;`
```csharp
// 解构时指定变量类型
var person = new Person("张三", 25);
(string name, int age) = person;
```

---

## 自定义成员

**基本写法：添加计算属性**
`public <类型> <属性名> => <表达式>;`
```csharp
// 在记录中添加计算属性
public record Circle(double Radius)
{
    public double Area => Math.PI * Radius * Radius;
}
```

---

**基本写法：添加方法**
`public <返回类型> <方法名>(<参数>) => <表达式>;`
```csharp
// 在记录中添加方法
public record Money(decimal Amount, string Currency)
{
    public Money ConvertTo(string newCurrency, decimal rate) =>
        new(Amount * rate, newCurrency);
}
```

---

**基本写法：添加验证**
`public <类型> <属性名> { get; init; }`
```csharp
// 在 init 访问器中添加验证
public record Person
{
    private string _name = string.Empty;
    public string Name
    {
        get => _name;
        init => _name = string.IsNullOrEmpty(value)
            ? throw new ArgumentException("Name 不能为空")
            : value;
    }
}
```

---

## ToString 与 PrintMembers

**基本写法：默认 ToString**
`string <结果> = <记录>.ToString();`
```csharp
// 记录默认生成可读的 ToString
var person = new Person("张三", 25);
Console.WriteLine(person.ToString());
```

---

**基本写法：重写 PrintMembers**
`protected virtual bool PrintMembers(StringBuilder builder)`
```csharp
// 自定义 ToString 输出的成员
public record Person(string Name, int Age)
{
    protected virtual bool PrintMembers(StringBuilder builder)
    {
        builder.Append($"姓名 = {Name}, 年龄 = {Age}");
        return true;
    }
}
```

---

## 记录与模式匹配

**基本写法：位置模式匹配**
`<变量> switch { <类型>(<模式1>, <模式2>) => <结果> }`
```csharp
// 记录位置模式匹配
public record Point(int X, int Y);
Point p = new(10, 20);
string label = p switch
{
    Point(0, 0) => "原点",
    Point(> 0, > 0) => "第一象限",
    _ => "其他"
};
```

---

**基本写法：属性模式匹配**
`<变量> switch { <类型> { <属性>: <值> } => <结果> }`
```csharp
// 记录属性模式匹配
var person = new Person("张三", 25);
string label = person switch
{
    { Age: > 18 } => "成年",
    { Age: <= 18 } => "未成年",
    _ => "未知"
};
```

---

## 记录与集合

**基本写法：记录列表**
`List<<记录类型>> <变量> = [ <记录>, ... ];`
```csharp
// 使用集合表达式初始化记录列表
List<Person> people = [
    new("张三", 25),
    new("李四", 30)
];
```

---

**基本写法：LINQ 查询记录**
`var <结果> = <记录集合>.Where(<谓词>);`
```csharp
// 使用 LINQ 查询记录集合
var adults = people.Where(p => p.Age >= 18);
```

---

**基本写法：记录分组**
`var <结果> = <记录集合>.GroupBy(<键选择器>);`
```csharp
// 按属性分组记录
var grouped = people.GroupBy(p => p.Age >= 18 ? "成年" : "未成年");
```

---

## 记录与 JSON 序列化

**基本写法：JsonSerializer 序列化**
`string <结果> = JsonSerializer.Serialize(<记录>);`
```csharp
// 序列化记录为 JSON 字符串
var person = new Person("张三", 25);
string json = JsonSerializer.Serialize(person);
```

---

**基本写法：JsonSerializer 反序列化**
`<记录类型> <变量> = JsonSerializer.Deserialize<<记录类型>>(<字符串>);`
```csharp
// 从 JSON 字符串反序列化为记录
string json = """{"Name":"张三","Age":25}""";
var person = JsonSerializer.Deserialize<Person>(json);
```

---

**基本写法：JsonSerializerOptions 配置**
`var <变量> = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };`
```csharp
// 配置 JSON 序列化选项
var options = new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true
};
var person = JsonSerializer.Deserialize<Person>(json, options);
```

---

## Primary Constructor 与记录

**基本写法：主构造函数捕获**
`public record <名称>(<参数>) { public <类型> <属性> => <参数>; }`
```csharp
// 主构造函数参数在记录主体中使用
public record Service(string ConnectionString)
{
    public bool IsValid => !string.IsNullOrEmpty(ConnectionString);
}
```

---

**基本写法：主构造函数与成员**
`public record <名称>(<参数>) { public void <方法>() { ... } }`
```csharp
// 主构造函数参数在方法中使用
public record DatabaseService(string ConnectionString)
{
    public void Connect()
    {
        Console.WriteLine($"连接到: {ConnectionString}");
    }
}
```



<!-- ============ 文档分隔线：015-csharp/005-OOP.md ============ -->

# C# 面向对象编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类的定义

**基本写法：私有字段声明**
`private <类型> <字段名>;`
```csharp
// 声明类内部私有字段
private string _name;
private int _age;
```

---

**基本写法：带验证的属性**
`public <类型> <属性名> { get => <字段>; set => <赋值表达式>; }`
```csharp
// 属性设置时进行参数验证
public string Name
{
    get => _name;
    set => _name = value ?? throw new ArgumentNullException(nameof(value));
}
```

---

**基本写法：自动属性**
`public <类型> <属性名> { get; set; } = <默认值>;`
```csharp
// 自动实现的属性带默认值
public string Email { get; set; } = string.Empty;
```

---

**基本写法：init 属性**
`public <类型> <属性名> { get; init; } = <默认值>;`
```csharp
// 仅初始化时赋值的属性
public string Address { get; init; } = string.Empty;
```

---

**基本写法：计算属性**
`public <类型> <属性名> => <表达式>;`
```csharp
// 基于其他属性计算的只读属性
public bool IsAdult => Age >= 18;
```

---

**基本写法：构造函数**
`public <类名>(<参数>) { <赋值语句>; }`
```csharp
// 类的构造函数初始化字段
public Person(string name, int age)
{
    _name = name;
    _age = age;
}
```

---

**基本写法：方法重载**
`public <返回类型> <方法名>() => <表达式>;`
```csharp
// 无参数的方法重载
public string Greet() => $"你好，我是{Name}";
```

---

**基本写法：带参数方法重载**
`public <返回类型> <方法名>(<参数>) => <表达式>;`
```csharp
// 带参数的方法重载
public string Greet(string greeting) => $"{greeting}，我是{Name}";
```

---

**单行写法：对象初始化器**
`var <变量> = new <类型>(<参数>) { <属性> = <值> };`
```csharp
// 单行使用构造函数和对象初始化器
var person = new Person("张三", 25) { Email = "zhangsan@example.com" };
```

---

**换行写法：对象初始化器**
`var <变量> = new <类型>(<参数>) { <属性1> = <值1>, <属性2> = <值2> };`
```csharp
// 换行使用构造函数和对象初始化器
var person = new Person("张三", 25)
{
    Email = "zhangsan@example.com",
    Address = "北京市"
};
```

---

**基本写法：目标类型 new**
`<类型> <变量> = new(<参数>);`
```csharp
// C# 9+ 目标类型 new 表达式
Person p = new("王五", 28);
```

---

**基本写法：静态字段属性**
`public static <类型> <属性名> { get; private set; }`
```csharp
// 类级别共享的静态属性
public static int InstanceCount { get; private set; }
```

---

**基本写法：静态构造函数**
`static <类名>() { <语句>; }`
```csharp
// 类首次访问时执行的静态构造函数
static MathHelper()
{
    InstanceCount = 0;
}
```

---

**基本写法：静态方法**
`public static <返回类型> <方法名>(<参数>) => <表达式>;`
```csharp
// 类级别的静态方法
public static double CircleArea(double radius) => Math.PI * radius * radius;
```

---

**基本写法：静态类**
`public static class <类名> { ... }`
```csharp
// 静态类只能包含静态成员
public static class StringExtensions { }
```

---

**基本写法：扩展方法**
`public static <返回类型> <方法名>(this <类型> <参数>) => <表达式>;`
```csharp
// 为现有类型添加扩展方法
public static bool IsNullOrEmpty(this string? str) =>
    string.IsNullOrEmpty(str);
```

---

## 构造函数

**基本写法：构造函数链**
`public <类名>(<参数>) : this(<参数>) { ... }`
```csharp
// 调用其他构造函数
public Product(string name, decimal price, string category) : this(name, price)
{
    Category = category;
}
```

---

**基本写法：主构造函数**
`public class <类名>(<参数>) { ... }`
```csharp
// C# 12 主构造函数简化构造函数定义
public class Service(ILogger logger, IConfiguration config)
{
    public void DoWork() => logger.LogInformation("执行工作...");
}
```

---

## 继承

**基本写法：基类定义**
`public class <基类> { public virtual <返回类型> <方法>() => <表达式>; }`
```csharp
// 基类定义虚方法供子类重写
public class Animal
{
    public virtual string Speak() => $"{Name}发出了声音";
}
```

---

**基本写法：派生类继承**
`public class <派生类> : <基类> { public <派生类>(<参数>) : base(<参数>) { ... } }`
```csharp
// 派生类继承基类并调用基类构造函数
public class Dog : Animal
{
    public Dog(string name, int age) : base(name, age) { }
}
```

---

**基本写法：override 重写虚方法**
`public override <返回类型> <方法>() => <表达式>;`
```csharp
// 重写基类的虚方法
public override string Speak() => $"{Name}汪汪叫！";
```

---

**基本写法：sealed 密封方法**
`public sealed <返回类型> <方法>() => <表达式>;`
```csharp
// 阻止子类进一步重写
public sealed string GetInfo() => $"{Name}, {Age}岁";
```

---

**基本写法：new 方法隐藏**
`public new <返回类型> <方法>() => <表达式>;`
```csharp
// 隐藏基类方法（不推荐使用）
public new string GetInfo() => $"{Name} ({Breed}), {Age}岁";
```

---

**基本写法：多态调用**
`<基类> <变量> = new <派生类>(<参数>);`
```csharp
// 运行时根据实际类型调用方法
Animal animal = new Dog("旺财", 3, "金毛");
Console.WriteLine(animal.Speak());
```

---

## 抽象类与接口

**基本写法：抽象类定义**
`public abstract class <类名> { public abstract <返回类型> <方法>(); }`
```csharp
// 定义包含抽象方法的抽象类
public abstract class Shape
{
    public abstract double Area();
}
```

---

**基本写法：抽象类虚方法**
`public virtual <返回类型> <方法>() => <表达式>;`
```csharp
// 抽象类中定义可选重写的虚方法
public virtual string Describe() =>
    $"{GetType().Name} (颜色: {Color}, 面积: {Area():F2})";
```

---

**基本写法：实现抽象类**
`public class <派生类> : <抽象类> { public override <返回类型> <方法>() => <表达式>; }`
```csharp
// 派生类实现抽象方法
public class Circle : Shape
{
    public override double Area() => Math.PI * Radius * Radius;
}
```

---

**基本写法：接口定义**
`public interface <接口名> { <返回类型> <方法>(); }`
```csharp
// 定义接口契约
public interface IReadable
{
    string Read();
}
```

---

**基本写法：接口默认实现**
`public interface <接口名> { void <方法>(); void <默认方法>() => <表达式>; }`
```csharp
// C# 8+ 接口默认方法实现
public interface ILogger
{
    void Log(string message);
    void LogWarning(string message) => Log($"[WARN] {message}");
}
```

---

**单行写法：多接口实现**
`public class <类名> : <接口1>, <接口2>, <接口3> { ... }`
```csharp
// 单行声明实现多个接口
public class FileStorage : IReadable, IWritable, ILogger { }
```

---

**换行写法：多接口实现**
`public class <类名> : <接口1>, <接口2>, <接口3> { ... }`
```csharp
// 换行声明实现多个接口
public class FileStorage
    : IReadable, IWritable, ILogger
{
    public string Read() => File.ReadAllText(_path);
}
```

---

## 属性与索引器

**基本写法：派生属性 get/set**
`public <类型> <属性名> { get => <表达式>; set => <赋值表达式>; }`
```csharp
// 基于其他属性计算的派生属性
public double Fahrenheit
{
    get => _celsius * 9 / 5 + 32;
    set => _celsius = (value - 32) * 5 / 9;
}
```

---

**基本写法：索引器定义**
`public <类型> this[<参数>] { get; set; }`
```csharp
// 通过索引访问对象成员
public double this[int row, int col]
{
    get => _data[row, col];
    set => _data[row, col] = value;
}
```

---

**基本写法：索引器赋值**
`<对象>[<索引>] = <值>;`
```csharp
// 使用索引器设置值
var matrix = new Matrix(3, 3);
matrix[0, 0] = 1.0;
```

---

**基本写法：索引器取值**
`<类型> <变量> = <对象>[<索引>];`
```csharp
// 使用索引器获取值
var value = matrix[2, 2];
```

---

## 运算符重载

**基本写法：二元加法运算符重载**
`public static <类型> operator +(<类型> <参数1>, <类型> <参数2>)`
```csharp
// 重载加法运算符
public static Vector operator +(Vector a, Vector b) =>
    new(a.X + b.X, a.Y + b.Y);
```

---

**基本写法：二元减法运算符重载**
`public static <类型> operator -(<类型> <参数1>, <类型> <参数2>)`
```csharp
// 重载减法运算符
public static Vector operator -(Vector a, Vector b) =>
    new(a.X - b.X, a.Y - b.Y);
```

---

**基本写法：标量乘法运算符重载**
`public static <类型> operator *(<类型> <参数>, <标量类型> <标量>)`
```csharp
// 重载与标量的乘法运算符
public static Vector operator *(Vector v, double scalar) =>
    new(v.X * scalar, v.Y * scalar);
```

---

**基本写法：相等运算符重载**
`public static bool operator ==(<类型> a, <类型> b)`
```csharp
// 重载相等比较运算符
public static bool operator ==(Vector a, Vector b) =>
    a.X == b.X && a.Y == b.Y;
```

---

**基本写法：不等运算符重载**
`public static bool operator !=(<类型> a, <类型> b)`
```csharp
// 重载不等比较运算符（需与 == 成对重载）
public static bool operator !=(Vector a, Vector b) => !(a == b);
```

---

**基本写法：Equals 重写**
`public override bool Equals(object? <参数>)`
```csharp
// 重写 Equals 方法
public override bool Equals(object? obj) =>
    obj is Vector v && this == v;
```

---

**基本写法：GetHashCode 重写**
`public override int GetHashCode()`
```csharp
// 重写 GetHashCode 方法
public override int GetHashCode() => HashCode.Combine(X, Y);
```

---

**基本写法：隐式转换运算符**
`public static implicit operator <目标类型>(<源类型> <参数>)`
```csharp
// 定义类型的隐式转换
public static implicit operator Vector((double x, double y) tuple) =>
    new(tuple.x, tuple.y);
```

---

## 记录类型 (Record)

**基本写法：位置记录**
`public record <名称>(<参数列表>);`
```csharp
// 简洁的不可变数据类型定义
public record Person(string Name, int Age);
```

---

**基本写法：记录继承**
`public record <派生>(<参数>) : <基类>(<参数>);`
```csharp
// 记录类型支持继承
public record Student(string Name, int Age, string School) : Person(Name, Age);
```

---

**基本写法：record struct**
`public record struct <名称>(<参数列表>);`
```csharp
// 值类型记录
public record struct Point(double X, double Y);
```

---

**基本写法：readonly record struct**
`public readonly record struct <名称>(<参数列表>);`
```csharp
// 不可变值类型记录
public readonly record struct Money(decimal Amount, string Currency);
```

---

**基本写法：记录值相等性**
`bool <结果> = <记录1> == <记录2>;`
```csharp
// 记录类型基于值比较相等性
var p1 = new Person("张三", 25);
var p2 = new Person("张三", 25);
Console.WriteLine(p1 == p2);
```

---

**基本写法：记录 with 表达式**
`var <变量> = <记录> with { <属性> = <值> };`
```csharp
// 非破坏性修改记录
var p3 = p1 with { Age = 26 };
```

---

**基本写法：记录解构**
`var (<变量1>, <变量2>) = <记录>;`
```csharp
// 解构记录的属性
var (name, age) = p1;
Console.WriteLine($"{name}, {age}");
```



<!-- ============ 文档分隔线：015-csharp/006-PatternMatching.md ============ -->

# C# 模式匹配

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类型模式

**基本写法：is 类型检查**
`if (<变量> is <类型>)`
```csharp
// 检查对象是否为指定类型
object obj = "Hello";
if (obj is string)
{
    Console.WriteLine("是字符串");
}
```

---

**基本写法：is 类型声明**
`if (<变量> is <类型> <变量名>)`
```csharp
// 类型检查并赋值给新变量
object obj = "Hello";
if (obj is string s)
{
    Console.WriteLine($"长度: {s.Length}");
}
```

---

**基本写法：switch 类型分支**
`switch (<变量>) { case <类型> <变量名>: <语句>; break; }`
```csharp
// switch 语句中的类型模式
object obj = 42;
switch (obj)
{
    case int i:
        Console.WriteLine($"整数: {i}");
        break;
    case string s:
        Console.WriteLine($"字符串: {s}");
        break;
}
```

---

**基本写法：switch 表达式类型分支**
`<变量> switch { <类型> <变量名> => <结果>, _ => <默认> }`
```csharp
// switch 表达式中的类型模式
object obj = 42;
string label = obj switch
{
    int i => $"整数 {i}",
    string s => $"字符串 {s}",
    _ => "未知类型"
};
```

---

## 常量模式

**基本写法：null 检查**
`if (<变量> is null)`
```csharp
// 检查变量是否为 null
string? name = null;
if (name is null)
{
    Console.WriteLine("未设置");
}
```

---

**基本写法：not null 检查**
`if (<变量> is not null)`
```csharp
// 检查变量是否非 null
string? name = "张三";
if (name is not null)
{
    Console.WriteLine(name);
}
```

---

**基本写法：常量值匹配**
`<变量> switch { <常量> => <结果>, _ => <默认> }`
```csharp
// 匹配常量值
int statusCode = 404;
string label = statusCode switch
{
    200 => "OK",
    404 => "Not Found",
    500 => "Server Error",
    _ => "Unknown"
};
```

---

## 关系模式

**基本写法：大于关系**
`<变量> switch { > <值> => <结果> }`
```csharp
// 匹配大于指定值
int score = 85;
string grade = score switch
{
    > 90 => "A",
    > 80 => "B",
    > 70 => "C",
    _ => "F"
};
```

---

**基本写法：小于关系**
`<变量> switch { < <值> => <结果> }`
```csharp
// 匹配小于指定值
int temperature = -5;
string label = temperature switch
{
    < 0 => "冰冻",
    < 20 => "寒冷",
    _ => "温暖"
};
```

---

**基本写法：范围匹配**
`<变量> switch { >= <最小> and <= <最大> => <结果> }`
```csharp
// 匹配指定范围
int age = 25;
string category = age switch
{
    >= 0 and < 18 => "未成年",
    >= 18 and < 60 => "成年",
    >= 60 => "老年",
    _ => "无效"
};
```

---

## 逻辑模式

**基本写法：and 组合模式**
`<模式1> and <模式2>`
```csharp
// 同时满足两个模式
object value = 42;
if (value is int and > 0)
{
    Console.WriteLine("正整数");
}
```

---

**基本写法：or 选择模式**
`<模式1> or <模式2>`
```csharp
// 满足任一模式
DayOfWeek day = DayOfWeek.Saturday;
if (day is DayOfWeek.Saturday or DayOfWeek.Sunday)
{
    Console.WriteLine("周末");
}
```

---

**基本写法：not 否定模式**
`not <模式>`
```csharp
// 不满足指定模式
object value = "Hello";
if (value is not null)
{
    Console.WriteLine("非 null");
}
```

---

**基本写法：复杂逻辑组合**
`<模式1> and (<模式2> or <模式3>)`
```csharp
// 复杂逻辑组合
int score = 85;
if (score is > 60 and (< 80 or > 90))
{
    Console.WriteLine("特殊分数段");
}
```

---

## 属性模式

**基本写法：单属性匹配**
`<变量> switch { { <属性>: <值> } => <结果> }`
```csharp
// 匹配对象单个属性值
var user = new User("张三", 25);
string label = user switch
{
    { Age: 25 } => "25岁用户",
    _ => "其他"
};
```

---

**基本写法：多属性匹配**
`<变量> switch { { <属性1>: <值1>, <属性2>: <值2> } => <结果> }`
```csharp
// 匹配对象多个属性值
var user = new User("张三", 25);
string label = user switch
{
    { Name: "张三", Age: 25 } => "匹配张三",
    _ => "不匹配"
};
```

---

**基本写法：嵌套属性匹配**
`<变量> switch { { <属性>.<子属性>: <值> } => <结果> }`
```csharp
// 匹配嵌套对象的属性
var order = new Order(new Customer("VIP"), 1500m);
string discount = order switch
{
    { Customer.Level: "VIP" } => "8折",
    _ => "无折扣"
};
```

---

**基本写法：属性带关系匹配**
`<变量> switch { { <属性>: > <值> } => <结果> }`
```csharp
// 属性值与关系运算符组合
var order = new Order(1500m);
string label = order switch
{
    { Amount: > 1000m } => "大额订单",
    { Amount: > 100m } => "中额订单",
    _ => "小额订单"
};
```

---

## 位置模式

**基本写法：元组位置匹配**
`(<变量1>, <变量2>) switch { (<值1>, <值2>) => <结果> }`
```csharp
// 匹配元组的值
var point = (10, 20);
string quadrant = point switch
{
    (0, 0) => "原点",
    (> 0, > 0) => "第一象限",
    (< 0, > 0) => "第二象限",
    _ => "其他象限"
};
```

---

**基本写法：记录位置匹配**
`<变量> switch { <类型>(<值1>, <值2>) => <结果> }`
```csharp
// 匹配记录的位置参数
public record Point(int X, int Y);
Point p = new(10, 20);
string label = p switch
{
    Point(0, 0) => "原点",
    Point(_, 0) => "X 轴",
    Point(0, _) => "Y 轴",
    _ => "其他"
};
```

---

**基本写法：位置模式带类型**
`<变量> switch { <类型>(<模式1>, <模式2>) => <结果> }`
```csharp
// 位置模式与类型组合
public record Point(int X, int Y);
Point p = new(10, 20);
string label = p switch
{
    Point(> 0, > 0) => "第一象限",
    Point(< 0, > 0) => "第二象限",
    _ => "其他"
};
```

---

## 列表模式

**基本写法：空列表匹配**
`<数组> switch { [] => <结果> }`
```csharp
// 匹配空列表
int[] numbers = [];
string label = numbers switch
{
    [] => "空列表",
    _ => "非空列表"
};
```

---

**基本写法：单元素列表匹配**
`<数组> switch { [<元素>] => <结果> }`
```csharp
// 匹配仅含单个元素的列表
int[] numbers = [42];
string label = numbers switch
{
    [single] => $"单元素: {single}",
    _ => "其他"
};
```

---

**基本写法：双元素列表匹配**
`<数组> switch { [<元素1>, <元素2>] => <结果> }`
```csharp
// 匹配包含两个元素的列表
int[] numbers = [1, 2];
string label = numbers switch
{
    [first, second] => $"两元素: {first}, {second}",
    _ => "其他"
};
```

---

**基本写法：首尾元素匹配**
`<数组> switch { [first, .., last] => <结果> }`
```csharp
// 匹配列表的首尾元素
int[] numbers = [1, 2, 3, 4, 5];
string label = numbers switch
{
    [first, .., last] => $"首: {first}, 尾: {last}",
    _ => "其他"
};
```

---

**基本写法：特定值列表匹配**
`<数组> switch { [1, 2, ..] => <结果> }`
```csharp
// 匹配以特定值开头的列表
int[] numbers = [1, 2, 3, 4];
string label = numbers switch
{
    [1, 2, ..] => "以 1, 2 开头",
    _ => "其他"
};
```

---

**基本写法：列表模式带条件**
`<数组> switch { [var x, ..] when <条件> => <结果> }`
```csharp
// 列表模式与 when 守卫组合
int[] numbers = [10, 20, 30];
string label = numbers switch
{
    [var first, ..] when first > 5 => "首元素大于 5",
    _ => "其他"
};
```

---

## when 守卫

**基本写法：when 条件守卫**
`case <模式> when <条件>:`
```csharp
// switch 语句中的 when 守卫
int score = 85;
switch (score)
{
    case int s when s >= 90:
        Console.WriteLine("优秀");
        break;
    case int s when s >= 80:
        Console.WriteLine("良好");
        break;
}
```

---

**基本写法：switch 表达式 when 守卫**
`<模式> when <条件> => <结果>`
```csharp
// switch 表达式中的 when 守卫
var user = new User("张三", 25);
string label = user switch
{
    { Age: var age } when age < 18 => "未成年",
    { Age: var age } when age >= 18 => "成年",
    _ => "未知"
};
```

---

## 模式组合

**基本写法：类型与属性组合**
`<类型> { <属性>: <值> }`
```csharp
// 类型模式与属性模式组合
object obj = new User("张三", 25);
string label = obj switch
{
    User { Age: > 18 } u => $"成年用户: {u.Name}",
    User u => $"未成年用户: {u.Name}",
    _ => "非用户"
};
```

---

**基本写法：类型与位置组合**
`<类型>(<模式1>, <模式2>)`
```csharp
// 类型模式与位置模式组合
public record Point(int X, int Y);
object obj = new Point(10, 20);
string label = obj switch
{
    Point(0, 0) => "原点",
    Point(_, _) => "非原点",
    _ => "非点"
};
```

---

**基本写法：复杂模式组合**
`<类型> { <属性>: <模式> } when <条件>`
```csharp
// 多种模式组合使用
public record Order(decimal Amount, string Status);
var order = new Order(1500m, "VIP");
string label = order switch
{
    Order { Amount: > 1000m, Status: "VIP" } when order.Amount < 2000m => "中额 VIP",
    _ => "其他"
};
```

---

## 解构模式

**基本写法：Deconstruct 解构**
`var (<变量1>, <变量2>) = <对象>;`
```csharp
// 使用 Deconstruct 方法解构对象
public record Point(int X, int Y);
Point p = new(10, 20);
var (x, y) = p;
Console.WriteLine($"X: {x}, Y: {y}");
```

---

**基本写法：自定义 Deconstruct**
`public void Deconstruct(out <类型1> <变量1>, out <类型2> <变量2>)`
```csharp
// 为类型添加解构方法
public class Rectangle
{
    public double Width { get; init; }
    public double Height { get; init; }
    public void Deconstruct(out double width, out double height)
    {
        width = Width;
        height = Height;
    }
}
```

---

**基本写法：解构与模式匹配**
`if (<对象> is (<模式1>, <模式2>))`
```csharp
// 解构后进行模式匹配
var rect = new Rectangle { Width = 10, Height = 20 };
if (rect is ( > 5, > 5))
{
    Console.WriteLine("宽高都大于 5");
}
```



<!-- ============ 文档分隔线：015-csharp/007-AsyncProgramming.md ============ -->

# C# 异步编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## async 与 await 基础

**基本写法：async 方法声明**
`public async Task <方法名>() { ... }`
```csharp
// 声明异步方法返回 Task
public async Task DoWorkAsync()
{
    await Task.Delay(1000);
    Console.WriteLine("工作完成");
}
```

---

**基本写法：async Task\<T\> 方法**
`public async Task<<返回类型>> <方法名>() { ... }`
```csharp
// 声明异步方法返回带值 Task
public async Task<int> GetCountAsync()
{
    await Task.Delay(500);
    return 42;
}
```

---

**基本写法：async ValueTask 方法**
`public async ValueTask<<返回类型>> <方法名>() { ... }`
```csharp
// 声明返回 ValueTask 的异步方法
public async ValueTask<int> GetCachedCountAsync()
{
    await Task.Delay(100);
    return 100;
}
```

---

**基本写法：await Task.Delay**
`await Task.Delay(<毫秒>);`
```csharp
// 异步等待指定毫秒
await Task.Delay(1000);
```

---

**基本写法：await 调用异步方法**
`await <异步方法>();`
```csharp
// 等待异步方法完成
await DoWorkAsync();
```

---

**基本写法：await 获取结果**
`<类型> <变量> = await <异步方法>();`
```csharp
// 等待异步方法并获取返回值
int count = await GetCountAsync();
```

---

## Task 创建与组合

**基本写法：Task.Run 委托**
`Task <变量> = Task.Run(() => <表达式>);`
```csharp
// 在线程池上运行委托
Task task = Task.Run(() =>
{
    Console.WriteLine("在线程池执行");
});
```

---

**基本写法：Task.Run 带返回值**
`Task<<类型>> <变量> = Task.Run(() => <表达式>);`
```csharp
// 在线程池上运行带返回值的委托
Task<int> task = Task.Run(() => 42 + 100);
```

---

**基本写法：Task.FromResult 同步结果**
`Task<<类型>> <变量> = Task.FromResult(<值>);`
```csharp
// 创建已完成的 Task
Task<int> completed = Task.FromResult(42);
```

---

**基本写法：Task.CompletedTask**
`Task <变量> = Task.CompletedTask;`
```csharp
// 获取已完成的 Task
return Task.CompletedTask;
```

---

**基本写法：Task.WhenAll 等待全部**
`await Task.WhenAll(<任务1>, <任务2>);`
```csharp
// 等待多个任务全部完成
var task1 = Task.Delay(1000);
var task2 = Task.Delay(2000);
await Task.WhenAll(task1, task2);
```

---

**基本写法：Task.WhenAll 带返回值**
`<类型>[] <变量> = await Task.WhenAll(<任务1>, <任务2>);`
```csharp
// 等待多个带返回值的任务并获取结果
var t1 = Task.FromResult(1);
var t2 = Task.FromResult(2);
int[] results = await Task.WhenAll(t1, t2);
```

---

**基本写法：Task.WhenAny 等待任一**
`Task <变量> = await Task.WhenAny(<任务1>, <任务2>);`
```csharp
// 等待任一任务完成
var t1 = Task.Delay(1000);
var t2 = Task.Delay(2000);
Task first = await Task.WhenAny(t1, t2);
```

---

**基本写法：Task.WhenAny 带超时**
`Task <变量> = await Task.WhenAny(<任务>, Task.Delay(<超时>));`
```csharp
// 等待任务完成或超时
var task = DoWorkAsync();
var timeout = Task.Delay(5000);
if (await Task.WhenAny(task, timeout) == timeout)
{
    Console.WriteLine("超时");
}
```

---

## CancellationToken

**基本写法：CancellationTokenSource 创建**
`using var <变量> = new CancellationTokenSource();`
```csharp
// 创建取消令牌源
using var cts = new CancellationTokenSource();
```

---

**基本写法：传递 CancellationToken**
`public async Task <方法>(CancellationToken <参数>) { ... }`
```csharp
// 异步方法接受取消令牌
public async Task DoWorkAsync(CancellationToken cancellationToken)
{
    await Task.Delay(1000, cancellationToken);
}
```

---

**基本写法：Task.Delay 带取消**
`await Task.Delay(<毫秒>, <取消令牌>);`
```csharp
// 可取消的延迟
using var cts = new CancellationTokenSource();
await Task.Delay(1000, cts.Token);
```

---

**基本写法：触发取消**
`<取消源>.Cancel();`
```csharp
// 触发取消请求
using var cts = new CancellationTokenSource();
cts.Cancel();
```

---

**基本写法：超时自动取消**
`<取消源>.CancelAfter(<毫秒>);`
```csharp
// 指定时间后自动取消
using var cts = new CancellationTokenSource();
cts.CancelAfter(5000);
```

---

**基本写法：检查取消请求**
`<取消令牌>.ThrowIfCancellationRequested();`
```csharp
// 主动检查并抛出取消异常
cancellationToken.ThrowIfCancellationRequested();
```

---

**基本写法：循环中检查取消**
`for (...) { <取消令牌>.ThrowIfCancellationRequested(); ... }`
```csharp
// 在循环中检查取消请求
for (int i = 0; i < 1000; i++)
{
    cancellationToken.ThrowIfCancellationRequested();
    await Task.Delay(10, cancellationToken);
}
```

---

## IAsyncEnumerable

**基本写法：异步迭代器声明**
`public async IAsyncEnumerable<<类型>> <方法>() { ... }`
```csharp
// 声明异步流方法
public async IAsyncEnumerable<int> GenerateAsync()
{
    for (int i = 0; i < 5; i++)
    {
        await Task.Delay(100);
        yield return i;
    }
}
```

---

**基本写法：异步迭代器带取消**
`public async IAsyncEnumerable<<类型>> <方法>(CancellationToken <参数>) { ... }`
```csharp
// 带取消令牌的异步流
public async IAsyncEnumerable<int> GenerateAsync(
    [EnumeratorCancellation] CancellationToken cancellationToken)
{
    for (int i = 0; i < 5; i++)
    {
        await Task.Delay(100, cancellationToken);
        yield return i;
    }
}
```

---

**基本写法：await foreach 消费**
`await foreach (var <变量> in <异步流>)`
```csharp
// 异步遍历异步流
await foreach (var item in GenerateAsync())
{
    Console.WriteLine(item);
}
```

---

**基本写法：await foreach 带取消**
`await foreach (var <变量> in <异步流>.WithCancellation(<令牌>))`
```csharp
// 带取消令牌的异步遍历
using var cts = new CancellationTokenSource();
await foreach (var item in GenerateAsync().WithCancellation(cts.Token))
{
    Console.WriteLine(item);
}
```

---

## ConfigureAwait

**基本写法：ConfigureAwait(false)**
`await <任务>.ConfigureAwait(false);`
```csharp
// 库代码中避免捕获同步上下文
await Task.Delay(1000).ConfigureAwait(false);
```

---

**基本写法：ConfigureAwait(true)**
`await <任务>.ConfigureAwait(true);`
```csharp
// 捕获同步上下文（UI 应用默认行为）
await Task.Delay(1000).ConfigureAwait(true);
```

---

## 异步流操作

**基本写法：异步流 LINQ**
`await foreach (var <变量> in <异步流>.Where(<谓词>))`
```csharp
// 对异步流应用 LINQ 操作
await foreach (var item in GenerateAsync().Where(x => x > 2))
{
    Console.WriteLine(item);
}
```

---

**基本写法：ToListAsync 异步收集**
`List<<类型>> <变量> = await <异步流>.ToListAsync();`
```csharp
// 将异步流收集为列表
List<int> list = await GenerateAsync().ToListAsync();
```

---

## Channel 异步通信

**基本写法：Channel 创建**
`var <变量> = Channel.CreateUnbounded<<类型>>();`
```csharp
// 创建无界通道
var channel = Channel.CreateUnbounded<int>();
```

---

**基本写法：Channel 有界创建**
`var <变量> = Channel.CreateBounded<<类型>>(<容量>);`
```csharp
// 创建有界通道
var channel = Channel.CreateBounded<int>(100);
```

---

**基本写法：写入 Channel**
`await <通道>.Writer.WriteAsync(<值>);`
```csharp
// 异步写入通道
await channel.Writer.WriteAsync(42);
```

---

**基本写法：读取 Channel**
`<类型> <变量> = await <通道>.Reader.ReadAsync();`
```csharp
// 异步读取通道
int value = await channel.Reader.ReadAsync();
```

---

**基本写法：完成写入**
`<通道>.Writer.Complete();`
```csharp
// 标记通道写入完成
channel.Writer.Complete();
```

---

**基本写法：await foreach 消费 Channel**
`await foreach (var <变量> in <通道>.Reader.ReadAllAsync())`
```csharp
// 异步遍历通道所有数据
await foreach (var item in channel.Reader.ReadAllAsync())
{
    Console.WriteLine(item);
}
```

---

## Parallel 并行

**基本写法：Parallel.ForEach**
`Parallel.ForEach(<集合>, <动作>);`
```csharp
// 并行遍历集合
var items = Enumerable.Range(0, 100);
Parallel.ForEach(items, item =>
{
    Console.WriteLine($"处理: {item}");
});
```

---

**基本写法：Parallel.For**
`Parallel.For(<起始>, <结束>, <动作>);`
```csharp
// 并行执行循环
Parallel.For(0, 100, i =>
{
    Console.WriteLine($"索引: {i}");
});
```

---

**基本写法：ParallelOptions 带取消**
`Parallel.ForEach(<集合>, new ParallelOptions { CancellationToken = <令牌> }, <动作>);`
```csharp
// 并行遍历带取消支持
using var cts = new CancellationTokenSource();
Parallel.ForEach(items, new ParallelOptions
{
    CancellationToken = cts.Token,
    MaxDegreeOfParallelism = 4
}, item => Process(item));
```

---

## TaskCompletionSource

**基本写法：TaskCompletionSource 创建**
`var <变量> = new TaskCompletionSource<<类型>>();`
```csharp
// 创建可手动控制的 Task 源
var tcs = new TaskCompletionSource<int>();
```

---

**基本写法：SetResult 完成任务**
`<源>.SetResult(<值>);`
```csharp
// 手动完成 Task
var tcs = new TaskCompletionSource<int>();
tcs.SetResult(42);
```

---

**基本写法：SetException 异常完成**
`<源>.SetException(<异常>);`
```csharp
// 手动让 Task 失败
var tcs = new TaskCompletionSource<int>();
tcs.SetException(new InvalidOperationException("失败"));
```

---

**基本写法：await TaskCompletionSource**
`<类型> <变量> = await <源>.Task;`
```csharp
// 等待手动控制的 Task
var tcs = new TaskCompletionSource<int>();
int result = await tcs.Task;
```

---

## 异步锁与并发

**基本写法：SemaphoreSlim 异步锁**
`await <信号量>.WaitAsync();`
```csharp
// 异步等待信号量
var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();
try
{
    // 临界区
}
finally
{
    semaphore.Release();
}
```

---

**基本写法：SemaphoreSlim 释放**
`<信号量>.Release();`
```csharp
// 释放信号量
semaphore.Release();
```

---

**基本写法：AsyncLock 模式**
`public class <类名> { public async Task<<锁句柄>> LockAsync() { ... } }`
```csharp
// 自定义异步锁模式
public class AsyncLock
{
    private readonly SemaphoreSlim _semaphore = new(1, 1);
    public async Task<IDisposable> LockAsync()
    {
        await _semaphore.WaitAsync();
        return new Releaser(_semaphore);
    }
    private class Releaser : IDisposable
    {
        private readonly SemaphoreSlim _sem;
        public Releaser(SemaphoreSlim sem) => _sem = sem;
        public void Dispose() => _sem.Release();
    }
}
```

---

## 异步异常处理

**基本写法：try-catch 异步异常**
`try { await <任务>; } catch (<异常类型> <变量>) { ... }`
```csharp
// 捕获异步方法抛出的异常
try
{
    await DoWorkAsync();
}
catch (OperationCanceledException ex)
{
    Console.WriteLine($"已取消: {ex.Message}");
}
```

---

**基本写法：AggregateException 多任务异常**
`catch (AggregateException <变量>)`
```csharp
// 捕获多个任务的聚合异常
try
{
    var tasks = new[] { Task.Run(() => throw new Exception("错误1")) };
    Task.WaitAll(tasks);
}
catch (AggregateException ex)
{
    foreach (var inner in ex.InnerExceptions)
    {
        Console.WriteLine(inner.Message);
    }
}
```

---

**基本写法：WhenAll 异常处理**
`try { await Task.WhenAll(<任务1>, <任务2>); } catch (<异常>) { ... }`
```csharp
// WhenAll 抛出第一个异常
try
{
    await Task.WhenAll(FailAsync(), FailAsync());
}
catch (Exception ex)
{
    Console.WriteLine($"捕获: {ex.Message}");
}
```



<!-- ============ 文档分隔线：015-csharp/008-ValueTypeReferenceType.md ============ -->

# C# 值类型与引用类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 赋值行为差异

**基本写法：值类型赋值**
`<值类型> <变量B> = <变量A>;`
```csharp
// struct 赋值复制值，两个变量相互独立
var p1 = new Point(1, 2);
var p2 = p1;
p2.X = 10;
```

---

**基本写法：引用类型赋值**
`<引用类型> <变量B> = <变量A>;`
```csharp
// class 赋值复制引用，两个变量指向同一对象
var u1 = new User("张三");
var u2 = u1;
u2.Name = "李四";
```

---

## 装箱与拆箱

**基本写法：装箱操作**
`object <变量> = <值类型变量>;`
```csharp
// 值类型转换为堆上的引用类型
int x = 42;
object obj = x;
```

---

**基本写法：拆箱操作**
`<值类型> <变量> = (<值类型>)<object变量>;`
```csharp
// 引用类型转换回值类型
object obj = 42;
int y = (int)obj;
```

---

**基本写法：泛型列表避免装箱**
`List<<值类型>> <变量> = new();`
```csharp
// 使用泛型列表存储值类型，避免装箱开销
var list = new List<int>();
list.Add(42);
```

---

## struct 定义

**单行写法：readonly struct 单字段定义**
`public readonly struct <名称> { public <类型> <属性> { get; } }`
```csharp
// 单行定义不可变值类型
public readonly struct Point { public double X { get; } public double Y { get; } public Point(double x, double y) => (X, Y) = (x, y); }
```

---

**换行写法：readonly struct 多字段定义**
`public readonly struct <名称> { public <类型> <属性> { get; } public <类型> <属性> { get; } }`
```csharp
// 换行定义包含多个属性的不可变值类型
public readonly struct Point
{
    public double X { get; }
    public double Y { get; }
    public Point(double x, double y) => (X, Y) = (x, y);
}
```

---

**基本写法：readonly struct 含方法**
`public double <方法>(<参数>) => <表达式>;`
```csharp
// 在 readonly struct 中定义计算方法
public double DistanceTo(Point other) =>
    Math.Sqrt(Math.Pow(X - other.X, 2) + Math.Pow(Y - other.Y, 2));
```

---

**基本写法：ref struct 定义**
`public ref struct <名称> { ... }`
```csharp
// 定义只能存在于栈上的结构体
public ref struct StackBuffer
{
    private readonly Span<byte> _buffer;
    public StackBuffer(int size) => _buffer = stackalloc byte[size];
}
```

---

**基本写法：ref struct 写方法**
`public void <方法>(<参数>) => <表达式>;`
```csharp
// 在 ref struct 中定义写入方法
public void Write(int offset, byte value) => _buffer[offset] = value;
```

---

## record struct

**基本写法：record struct 定义**
`public record struct <名称>(<参数列表>);`
```csharp
// 定义值类型记录，自动生成相等性比较
public record struct Point(double X, double Y);
```

---

**基本写法：record struct 值相等**
`bool <结果> = <记录1> == <记录2>;`
```csharp
// 值类型记录基于值比较相等性
var p1 = new Point(1, 2);
var p2 = new Point(1, 2);
Console.WriteLine(p1 == p2);
```

---

**基本写法：record class 定义**
`public record <名称>(<参数列表>);`
```csharp
// 定义引用类型记录
public record User(string Name, int Age);
```

---

**基本写法：record class with 表达式**
`var <变量> = <记录> with { <属性> = <值> };`
```csharp
// 使用 with 创建引用类型记录的修改副本
var u1 = new User("张三", 25);
var u2 = u1 with { Age = 26 };
```

---

## 接口与装箱

**基本写法：值类型实现接口**
`struct <名称> : <接口> { public void <方法>() { ... } }`
```csharp
// 值类型实现接口
struct MyProcessor : IProcessor
{
    public void Process() { }
}
```

---

**基本写法：直接调用无装箱**
`<值类型变量>.<方法>();`
```csharp
// 直接调用值类型方法，无装箱开销
MyProcessor processor = new();
processor.Process();
```

---

**基本写法：接口调用导致装箱**
`<接口> <变量> = <值类型实例>;`
```csharp
// 通过接口调用值类型会装箱
MyProcessor processor = new();
IProcessor boxed = processor;
```

---

**基本写法：泛型约束避免装箱**
`void <方法><T>(T <参数>) where T : <接口>`
```csharp
// 使用泛型约束避免接口调用装箱
void Process<T>(T processor) where T : IProcessor
{
    processor.Process();
}
```

---

## 参数传递优化

**基本写法：ref 引用传递**
`void <方法>(ref <类型> <参数>)`
```csharp
// 通过引用传递参数，避免大 struct 复制
void ProcessLargeStruct(ref LargeData data)
{
    data.Value = 42;
}
```

---

**基本写法：in 只读引用传递**
`void <方法>(in <类型> <参数>)`
```csharp
// 通过只读引用传递参数
void ReadLargeStruct(in LargeData data)
{
    Console.WriteLine(data.Value);
}
```

---

**基本写法：ref 返回**
`ref <类型> <方法>(<参数>)`
```csharp
// 返回引用，调用者可直接修改原数据
ref int FindMax(int[] array)
{
    int maxIndex = 0;
    for (int i = 1; i < array.Length; i++)
    {
        if (array[i] > array[maxIndex]) maxIndex = i;
    }
    return ref array[maxIndex];
}
```

---

## 结构体内存布局

**基本写法：StructLayout 顺序布局**
`[StructLayout(LayoutKind.Sequential)] public struct <名称> { ... }`
```csharp
// 控制结构体内存布局用于互操作
[StructLayout(LayoutKind.Sequential)]
public struct NativeHeader
{
    public int Magic;
    public short Version;
    public short Flags;
    public int DataLength;
}
```

---

**基本写法：StructLayout 显式布局**
`[StructLayout(LayoutKind.Explicit)] public struct <名称> { [FieldOffset(<偏移>)] public <类型> <字段>; }`
```csharp
// 精确控制字段偏移实现联合体效果
[StructLayout(LayoutKind.Explicit)]
public struct UnionValue
{
    [FieldOffset(0)] public int IntValue;
    [FieldOffset(0)] public float FloatValue;
}
```

---

## MemoryMarshal 高级操作

**基本写法：类型重解释**
`MemoryMarshal.Cast<<源类型>, <目标类型>>(<Span>)`
```csharp
// 零拷贝将字节数组重新解释为 int 数组
byte[] bytes = new byte[16];
Span<int> ints = MemoryMarshal.Cast<byte, int>(bytes.AsSpan());
ints[0] = 42;
```

---

**基本写法：结构体转字节**
`MemoryMarshal.AsBytes(MemoryMarshal.CreateReadOnlySpan(ref <结构体>, 1))`
```csharp
// 将结构体转换为只读字节跨度
var header = new NativeHeader { Magic = 0x4D42, Version = 1 };
ReadOnlySpan<byte> headerBytes = MemoryMarshal.AsBytes(
    MemoryMarshal.CreateReadOnlySpan(ref header, 1));
```



<!-- ============ 文档分隔线：015-csharp/009-LinqAsync.md ============ -->

# C# LINQ 与异步速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：015-csharp/010-LinqAdvanced.md ============ -->

# C# LINQ 进阶操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 投影与展开

**基本写法：SelectMany 展平嵌套集合**
`<集合>.SelectMany(<子集合选择器>);`
```csharp
// 把每个用户的订单列表展开成一个订单序列
var allOrders = users.SelectMany(u => u.Orders);
```

---

**基本写法：Select 带索引投影**
`<集合>.Select((<元素>, <索引>) => <结果>);`
```csharp
// 带索引生成编号
var indexed = items.Select((item, i) => $"{i + 1}. {item}");
```

---

**基本写法：SelectMany 带结果收集器**
`<集合>.SelectMany(<子集合选择器>, (<外元素>, <内元素>) => <结果>);`
```csharp
// 笛卡尔积：用户与角色的组合
var pairs = users.SelectMany(u => roles, (u, r) => $"{u.Name}-{r.Name}");
```

---

## 连接操作

**基本写法：Join 内连接**
`<外集合>.Join(<内集合>, <外键>, <内键>, <结果选择器>);`
```csharp
// 按部门 Id 连接员工与部门
var result = employees.Join(
    departments,
    e => e.DepartmentId,
    d => d.Id,
    (e, d) => new { e.Name, d.Name });
```

---

**基本写法：GroupJoin 分组连接**
`<外集合>.GroupJoin(<内集合>, <外键>, <内键>, <结果选择器>);`
```csharp
// 每个部门及其下属员工列表（左连接风格）
var grouped = departments.GroupJoin(
    employees,
    d => d.Id,
    e => e.DepartmentId,
    (d, emps) => new { Department = d.Name, Employees = emps });
```

---

**基本写法：Zip 按位置合并**
`<集合1>.Zip(<集合2>, (<元素1>, <元素2>) => <结果>);`
```csharp
// 按下标配对姓名与分数
var pairs = names.Zip(scores, (n, s) => new { Name = n, Score = s });
```

---

## 集合运算

**基本写法：Concat 串联**
`<集合1>.Concat(<集合2>);`
```csharp
// 拼接两个序列（不去重）
var combined = list1.Concat(list2);
```

---

**基本写法：Union 并集去重**
`<集合1>.Union(<集合2>);`
```csharp
// 合并去重
var unique = list1.Union(list2);
```

---

**基本写法：Except 差集**
`<集合1>.Except(<集合2>);`
```csharp
// 返回在 list1 但不在 list2 的元素
var diff = list1.Except(list2);
```

---

**基本写法：Intersect 交集**
`<集合1>.Intersect(<集合2>);`
```csharp
// 返回两个序列共有的元素
var common = list1.Intersect(list2);
```

---

**基本写法：DistinctBy 按键去重**
`<集合>.DistinctBy(<键选择器>);`
```csharp
// .NET 6+ 按字段去重
var uniqueById = items.DistinctBy(x => x.Id);
```

---

**基本写法：SequenceEqual 序列相等**
`<集合1>.SequenceEqual(<集合2>);`
```csharp
// 逐元素比较是否完全相同
bool same = list1.SequenceEqual(list2);
```

---

## 分组与查找

**基本写法：GroupBy 多值投影**
`<集合>.GroupBy(<键选择器>, <元素选择器>);`
```csharp
// 按班级分组，只保留姓名
var groups = students.GroupBy(s => s.Class, s => s.Name);
```

---

**基本写法：GroupBy 带结果投影**
`<集合>.GroupBy(<键选择器>, (<键>, <组>) => <结果>);`
```csharp
// 按部门分组并统计人数
var stats = employees.GroupBy(e => e.Dept, (k, g) => new { Dept = k, Count = g.Count() });
```

---

**基本写法：ToLookup 一对多字典**
`<集合>.ToLookup(<键选择器>, [<值选择器>]);`
```csharp
// 创建可重复键的查找结构
var lookup = items.ToLookup(x => x.Category, x => x.Name);
var values = lookup["Books"]; // 该分类下所有名称
```

---

## 类型筛选与转换

**基本写法：OfType 类型过滤**
`<集合>.OfType<<目标类型>>();`
```csharp
// 只保留字符串类型的元素
var strings = mixed.OfType<string>();
```

---

**基本写法：Cast 类型转换**
`<集合>.Cast<<目标类型>>();`
```csharp
// 将 ArrayList 强转为 IEnumerable<string>
var list = arrayList.Cast<string>();
```

---

**基本写法：Chunk 分块**
`<集合>.Chunk(<大小>);`
```csharp
// .NET 6+ 按每 3 个元素分块
var chunks = items.Chunk(3);
```

---

## 聚合与统计

**基本写法：Min/Max 极值**
`<集合>.Min([<选择器>]);`
```csharp
// 取最小年龄
int minAge = users.Min(u => u.Age);
// 取最大年龄
int maxAge = users.Max(u => u.Age);
```

---

**基本写法：Average 平均值**
`<集合>.Average([<选择器>]);`
```csharp
// 计算平均分
double avg = scores.Average();
double avgAge = users.Average(u => u.Age);
```

---

**基本写法：Aggregate 带种子聚合**
`<集合>.Aggregate(<种子>, (<累计>, <当前>) => <结果>, <结果选择器>);`
```csharp
// 计算总和并格式化
string result = nums.Aggregate(0, (acc, n) => acc + n, sum => $"Total: {sum}");
```

---

## 排序与分区

**基本写法：OrderByDescending 降序**
`<集合>.OrderByDescending(<键选择器>);`
```csharp
// 按分数降序排序
var sorted = students.OrderByDescending(s => s.Score);
```

---

**基本写法：Reverse 反转**
`<集合>.Reverse();`
```csharp
// 反转序列顺序
var reversed = list.Reverse();
```

---

**基本写法：TakeLast 取末尾**
`<集合>.TakeLast(<数量>);`
```csharp
// 取最后 3 个元素
var last3 = list.TakeLast(3);
```

---

**基本写法：SkipLast 跳过末尾**
`<集合>.SkipLast(<数量>);`
```csharp
// 跳过最后 2 个元素
var rest = list.SkipLast(2);
```

---

**基本写法：TakeWhile 条件取**
`<集合>.TakeWhile(<谓词>);`
```csharp
// 一直取直到不满足条件为止
var head = list.TakeWhile(x => x > 0);
```

---

**基本写法：SkipWhile 条件跳**
`<集合>.SkipWhile(<谓词>);`
```csharp
// 一直跳过直到不满足条件为止
var tail = list.SkipWhile(x => x < 0);
```

---

## 生成与空序列

**基本写法：Range 生成范围**
`Enumerable.Range(<起始>, <数量>);`
```csharp
// 生成 1 到 10
var nums = Enumerable.Range(1, 10);
```

---

**基本写法：Repeat 重复生成**
`Enumerable.Repeat(<值>, <次数>);`
```csharp
// 生成 5 个 0
var zeros = Enumerable.Repeat(0, 5);
```

---

**基本写法：Empty 空序列**
`Enumerable.Empty<<类型>>();`
```csharp
// 创建类型化的空序列
var empty = Enumerable.Empty<int>();
```

---

**基本写法：DefaultIfEmpty 默认值**
`<集合>.DefaultIfEmpty([<默认值>]);`
```csharp
// 序列为空时返回单个默认值
var safe = list.DefaultIfEmpty(0);
```

---

## 查询表达式语法

**基本写法：from-where-select 查询**
`from <变量> in <集合> where <条件> select <结果>`
```csharp
// 查询表达式风格
var result = from u in users
             where u.Age > 18
             select u.Name;
```

---

**基本写法：join-on-equals 查询连接**
`from <a> in <集合1> join <b> in <集合2> on <a键> equals <b键>`
```csharp
// 查询表达式风格的内连接
var result = from e in employees
             join d in departments on e.DeptId equals d.Id
             select new { e.Name, d.Name };
```

---

**基本写法：group-by 查询分组**
`group <元素> by <键> into <组>`
```csharp
// 查询表达式风格的分组
var result = from s in students
             group s by s.Class into g
             select new { Class = g.Key, Count = g.Count() };
```

---

## 立即执行与延迟执行

**基本写法：ToList 立即求值**
`<集合>.ToList();`
```csharp
// 立即执行查询并缓存结果
var list = query.ToList();
```

---

**基本写法：ToArray 转数组**
`<集合>.ToArray();`
```csharp
// 立即执行并返回数组
var arr = query.ToArray();
```

---

**基本写法：ToDictionary 转字典**
`<集合>.ToDictionary(<键选择器>);`
```csharp
// 立即转为字典（键不可重复）
var dict = items.ToDictionary(x => x.Id);
```

---

**基本写法：FirstOrDefault 带默认值**
`<集合>.FirstOrDefault(<谓词>, <默认值>);`
```csharp
// .NET 6+ 找不到时返回指定默认值
var item = list.FirstOrDefault(x => x.Id == 5, fallback);
```



<!-- ============ 文档分隔线：015-csharp/011-CollectionTypes.md ============ -->

# C# 集合类型详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Dictionary 字典

**基本写法：创建 Dictionary**
`Dictionary<<键类型>, <值类型>> <变量> = new();`
```csharp
// 创建键值对集合
var dict = new Dictionary<string, int>();
```

---

**基本写法：添加键值对**
`<dict>[<键>] = <值>;`
```csharp
// 添加或覆盖键值对
dict["Alice"] = 25;
```

---

**基本写法：TryGetValue 安全获取**
`<dict>.TryGetValue(<键>, out <值>);`
```csharp
// 不存在不抛异常，返回是否找到
if (dict.TryGetValue("Alice", out int age)) { }
```

---

**基本写法：Add 显式添加**
`<dict>.Add(<键>, <值>);`
```csharp
// 键已存在会抛异常
dict.Add("Bob", 30);
```

---

**基本写法：遍历键值对**
`foreach (var <项> in <dict>) { }`
```csharp
// 遍历 KeyValuePair
foreach (var kv in dict)
{
    Console.WriteLine($"{kv.Key}: {kv.Value}");
}
```

---

**基本写法：初始化器**
`new Dictionary<<K>, <V>> { { <键>, <值> } };`
```csharp
// 集合初始化器
var dict = new Dictionary<string, int> { ["A"] = 1, ["B"] = 2 };
```

---

## HashSet 去重集合

**基本写法：创建 HashSet**
`HashSet<<类型>> <变量> = new();`
```csharp
// 创建无序去重集合
var set = new HashSet<int>();
```

---

**基本写法：添加元素**
`<set>.Add(<元素>);`
```csharp
// 添加元素，已存在返回 false
bool added = set.Add(1);
```

---

**基本写法：集合交并差**
`<set1>.UnionWith(<set2>);`
```csharp
// 并集（合并到 set1）
set1.UnionWith(set2);
// 交集
set1.IntersectWith(set2);
// 差集
set1.ExceptWith(set2);
// 对称差（仅存在于其中一个集合）
set1.SymmetricExceptWith(set2);
```

---

**基本写法：判断子集**
`<set1>.IsSubsetOf(<set2>);`
```csharp
// 判断 set1 是否为 set2 的子集
bool isSub = set1.IsSubsetOf(set2);
// 判断 set1 是否为 set2 的超集
bool isSuper = set1.IsSupersetOf(set2);
```

---

## Queue 队列

**基本写法：创建队列**
`Queue<<类型>> <变量> = new();`
```csharp
// 创建先进先出队列
var queue = new Queue<string>();
```

---

**基本写法：入队 Enqueue**
`<queue>.Enqueue(<元素>);`
```csharp
// 在队尾添加元素
queue.Enqueue("Task1");
```

---

**基本写法：出队 Dequeue**
`<queue>.Dequeue();`
```csharp
// 取出并移除队首元素
string item = queue.Dequeue();
```

---

**基本写法：查看队首 Peek**
`<queue>.Peek();`
```csharp
// 查看但不移除队首元素
string head = queue.Peek();
```

---

**基本写法：TryDequeue 安全出队**
`<queue>.TryDequeue(out <元素>);`
```csharp
// .NET 6+ 队列为空不抛异常
if (queue.TryDequeue(out string item)) { }
```

---

## Stack 栈

**基本写法：创建栈**
`Stack<<类型>> <变量> = new();`
```csharp
// 创建后进先出栈
var stack = new Stack<int>();
```

---

**基本写法：入栈 Push**
`<stack>.Push(<元素>);`
```csharp
// 在栈顶压入元素
stack.Push(1);
```

---

**基本写法：出栈 Pop**
`<stack>.Pop();`
```csharp
// 取出并移除栈顶元素
int top = stack.Pop();
```

---

**基本写法：查看栈顶 Peek**
`<stack>.Peek();`
```csharp
// 查看但不移除栈顶元素
int top = stack.Peek();
```

---

## SortedList 排序列表

**基本写法：创建 SortedList**
`SortedList<<键类型>, <值类型>> <变量> = new();`
```csharp
// 创建按键排序的键值对
var sorted = new SortedList<string, int>();
```

---

**基本写法：按键访问**
`<sorted>[<键>]`
```csharp
// 键按升序存储
sorted["Apple"] = 1;
sorted["Banana"] = 2;
```

---

**基本写法：获取键索引**
`<sorted>.IndexOfKey(<键>);`
```csharp
// 获取键的序号
int idx = sorted.IndexOfKey("Apple");
```

---

## SortedDictionary 有序字典

**基本写法：创建 SortedDictionary**
`SortedDictionary<<键类型>, <值类型>> <变量> = new();`
```csharp
// 基于红黑树的有序字典，插入删除更快
var dict = new SortedDictionary<string, int>();
```

---

**基本写法：自定义排序**
`new SortedDictionary<<K>, <V>>(<比较器>);`
```csharp
// 使用自定义比较器
var dict = new SortedDictionary<string, int>(Comparer<string>.Create((a, b) => b.CompareTo(a)));
```

---

## ConcurrentDictionary 并发字典

**基本写法：创建并发字典**
`ConcurrentDictionary<<键类型>, <值类型>> <变量> = new();`
```csharp
// 线程安全的字典
var dict = new ConcurrentDictionary<string, int>();
```

---

**基本写法：TryAdd 原子添加**
`<dict>.TryAdd(<键>, <值>);`
```csharp
// 原子性添加，已存在返回 false
bool ok = dict.TryAdd("A", 1);
```

---

**基本写法：AddOrUpdate 添加或更新**
`<dict>.AddOrUpdate(<键>, <添加值>, (<键>, <旧值>) => <新值>);`
```csharp
// 不存在则添加，存在则按函数更新
dict.AddOrUpdate("A", 1, (k, old) => old + 1);
```

---

**基本写法：GetOrAdd 获取或添加**
`<dict>.GetOrAdd(<键>, <值工厂>);`
```csharp
// 不存在则用工厂生成值并加入
var val = dict.GetOrAdd("A", k => Compute(k));
```

---

## 只读集合

**基本写法：ImmutableList 不可变列表**
`ImmutableList<<类型>> <变量> = ImmutableList.Create<<类型>>();`
```csharp
// 创建不可变列表
var list = ImmutableList.Create(1, 2, 3);
```

---

**基本写法：不可变列表添加**
`<list>.Add(<元素>);`
```csharp
// 返回新列表，原列表不变
var newList = list.Add(4);
```

---

**基本写法：FrozenSet 冻结集合**
`<集合>.ToFrozenSet();`
```csharp
// .NET 8+ 构建后只读，查询极快
var frozen = set.ToFrozenSet();
```

---

**基本写法：FrozenDictionary 冻结字典**
`<集合>.ToFrozenDictionary(<键选择器>, <值选择器>);`
```csharp
// .NET 8+ 构建后只读字典
var frozen = list.ToFrozenDictionary(x => x.Id, x => x.Name);
```

---

## 集合容量与性能

**基本写法：预分配容量**
`new List<<类型>>(<容量>);`
```csharp
// 预分配容量避免频繁扩容
var list = new List<int>(1000);
```

---

**基本写法：TrimExcess 收缩**
`<list>.TrimExcess();`
```csharp
// 释放未使用的容量
list.TrimExcess();
```

---

**基本写法：EnsureCapacity 确保容量**
`<list>.EnsureCapacity(<最小容量>);`
```csharp
// 一次性确保至少容量
list.EnsureCapacity(500);
```



<!-- ============ 文档分隔线：015-csharp/012-DelegateEvent.md ============ -->

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



<!-- ============ 文档分隔线：015-csharp/013-ReflectionAttribute.md ============ -->

# C# 反射与特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 获取类型信息

**基本写法：获取 Type 对象**
`<对象>.GetType();`
```csharp
// 运行时获取类型信息
Type type = obj.GetType();
```

---

**基本写法：typeof 运算符**
`typeof(<类型>)`
```csharp
// 编译时获取类型信息
Type type = typeof(string);
```

---

**基本写法：按名称获取类型**
`Type.GetType("<完全限定名>");`
```csharp
// 通过字符串名称获取类型
Type type = Type.GetType("System.String, mscorlib");
```

---

**基本写法：判断类型继承**
`<类型>.IsAssignableFrom(<另一个类型>);`
```csharp
// 判断赋值兼容性
bool ok = typeof(IComparable).IsAssignableFrom(typeof(int));
```

---

**基本写法：判断实例类型**
`<对象> is <类型>`
```csharp
// 运行时类型检查
bool isString = obj is string;
```

---

## 成员反射

**基本写法：获取公共属性**
`<类型>.GetProperties();`
```csharp
// 获取所有公共属性
PropertyInfo[] props = type.GetProperties();
```

---

**基本写法：获取公共方法**
`<类型>.GetMethods();`
```csharp
// 获取所有公共方法
MethodInfo[] methods = type.GetMethods();
```

---

**基本写法：获取字段**
`<类型>.GetFields([<绑定标志>]);`
```csharp
// 获取私有字段需指定 BindingFlags
var fields = type.GetFields(BindingFlags.NonPublic | BindingFlags.Instance);
```

---

**基本写法：获取构造函数**
`<类型>.GetConstructors();`
```csharp
// 获取所有公共构造函数
ConstructorInfo[] ctors = type.GetConstructors();
```

---

**基本写法：获取特性**
`<成员>.GetCustomAttributes([<特性类型>], [<继承>]);`
```csharp
// 获取成员上的所有特性
var attrs = type.GetCustomAttributes(false);
```

---

## 动态创建实例

**基本写法：Activator 创建实例**
`Activator.CreateInstance(<类型>, [<参数>]);`
```csharp
// 动态创建对象
object obj = Activator.CreateInstance(typeof(StringBuilder));
```

---

**基本写法：泛型 Activator**
`Activator.CreateInstance<<类型>>();`
```csharp
// 泛型方式创建实例
var instance = Activator.CreateInstance<StringBuilder>();
```

---

**基本写法：调用构造函数反射**
`<构造函数>.Invoke(<参数>);`
```csharp
// 通过 ConstructorInfo 创建实例
var obj = ctor.Invoke(new object[] { "arg" });
```

---

## 动态调用成员

**基本写法：调用方法**
`<方法信息>.Invoke(<实例>, <参数数组>);`
```csharp
// 反射调用方法
var method = type.GetMethod("Substring");
var result = method.Invoke("hello", new object[] { 1, 3 });
```

---

**基本写法：获取属性值**
`<属性信息>.GetValue(<实例>);`
```csharp
// 读取属性值
var prop = type.GetProperty("Length");
var len = prop.GetValue("hello");
```

---

**基本写法：设置属性值**
`<属性信息>.SetValue(<实例>, <值>);`
```csharp
// 写入属性值
prop.SetValue(obj, newValue);
```

---

**基本写法：获取字段值**
`<字段信息>.GetValue(<实例>);`
```csharp
// 读取字段值
var field = type.GetField("_count", BindingFlags.NonPublic | BindingFlags.Instance);
var val = field.GetValue(obj);
```

---

**基本写法：泛型方法反射**
`<方法>.MakeGenericMethod(<类型参数>);`
```csharp
// 构造泛型方法再调用
var method = typeof(Enumerable).GetMethod("ToArray").MakeGenericMethod(typeof(int));
var arr = method.Invoke(null, new object[] { new[] { 1, 2 } });
```

---

## 内置特性

**基本写法：Obsolete 标记废弃**
`[Obsolete("<消息>" [, <是否报错>])]`
```csharp
// 标记方法已废弃
[Obsolete("请使用 NewMethod 代替", false)]
public void OldMethod() { }
```

---

**基本写法：Conditional 条件编译**
`[Conditional("<符号>")]`
```csharp
// 仅在定义符号时编译调用
[Conditional("DEBUG")]
public void DebugLog(string msg) { }
```

---

**基本写法：Serializable 标记可序列化**
`[Serializable]`
```csharp
// 标记类型可被二进制序列化
[Serializable]
public class MyData { }
```

---

**基本写法：AttributeUsage 限定用途**
`[AttributeUsage(<目标>, AllowMultiple = <bool>, Inherited = <bool>)]`
```csharp
// 限定特性只能用于类且不可重复
[AttributeUsage(AttributeTargets.Class, AllowMultiple = false)]
public class MyAttribute : Attribute { }
```

---

## 自定义特性

**基本写法：定义特性类**
`public class <名称> : Attribute { }`
```csharp
// 自定义特性必须继承 Attribute
public class TableAttribute : Attribute
{
    public string Name { get; set; }
    public TableAttribute(string name) { Name = name; }
}
```

---

**基本写法：应用特性**
`[<特性名>(<参数>)]`
```csharp
// 在类上应用特性
[Table("Users")]
public class User { }
```

---

**基本写法：读取命名特性**
`<成员>.GetCustomAttribute<<特性类型>>();`
```csharp
// 读取指定特性实例
var attr = type.GetCustomAttribute<TableAttribute>();
var name = attr?.Name;
```

---

## 动态类型与 dynamic

**基本写法：dynamic 声明**
`dynamic <变量> = <值>;`
```csharp
// 运行时绑定成员
dynamic d = "hello";
var len = d.Length; // 运行时解析
```

---

**基本写法：ExpandoObject 动态对象**
`dynamic <变量> = new ExpandoObject();`
```csharp
// 动态添加成员
dynamic obj = new ExpandoObject();
obj.Name = "Alice";
obj.Age = 30;
```

---

## 程序集加载

**基本写法：加载程序集**
`Assembly.Load("<程序集名>");`
```csharp
// 按名称加载程序集
var asm = Assembly.Load("MyLibrary");
```

---

**基本写法：从文件加载**
`Assembly.LoadFrom("<路径>");`
```csharp
// 从 DLL 文件加载程序集
var asm = Assembly.LoadFrom("MyLibrary.dll");
```

---

**基本写法：获取所有类型**
`<程序集>.GetTypes();`
```csharp
// 获取程序集中所有类型
Type[] types = asm.GetTypes();
```



<!-- ============ 文档分隔线：015-csharp/014-FileAndStream.md ============ -->

# C# 文件与流操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件路径

**基本写法：路径拼接**
`Path.Combine(<路径1>, <路径2>);`
```csharp
// 跨平台拼接路径
string path = Path.Combine("dir", "sub", "file.txt");
```

---

**基本写法：获取文件名**
`Path.GetFileName(<路径>);`
```csharp
// 获取含扩展名的文件名
string name = Path.GetFileName("/a/b/c.txt");
```

---

**基本写法：获取扩展名**
`Path.GetExtension(<路径>);`
```csharp
// 获取扩展名（含点）
string ext = Path.GetExtension("file.txt");
```

---

**基本写法：获取目录**
`Path.GetDirectoryName(<路径>);`
```csharp
// 获取所在目录路径
string dir = Path.GetDirectoryName("/a/b/c.txt");
```

---

**基本写法：临时文件路径**
`Path.GetTempFileName();`
```csharp
// 创建并返回临时文件路径
string tmp = Path.GetTempFileName();
```

---

**基本写法：获取特殊目录**
`Environment.GetFolderPath(<枚举>);`
```csharp
// 获取系统特殊目录
string desktop = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
```

---

## 文件读写

**基本写法：读取全部文本**
`File.ReadAllText(<路径>);`
```csharp
// 一次性读取整个文件
string content = File.ReadAllText("data.txt");
```

---

**基本写法：写入全部文本**
`File.WriteAllText(<路径>, <内容>);`
```csharp
// 覆盖写入文本
File.WriteAllText("out.txt", "Hello");
```

---

**基本写法：追加文本**
`File.AppendAllText(<路径>, <内容>);`
```csharp
// 在文件末尾追加
File.AppendAllText("log.txt", "new line\n");
```

---

**基本写法：读取所有行**
`File.ReadAllLines(<路径>);`
```csharp
// 按行读取为数组
string[] lines = File.ReadAllLines("data.txt");
```

---

**基本写法：异步读取全部文本**
`await File.ReadAllTextAsync(<路径>);`
```csharp
// 异步读取大文件
string content = await File.ReadAllTextAsync("big.txt");
```

---

**基本写法：异步写入**
`await File.WriteAllTextAsync(<路径>, <内容>);`
```csharp
// 异步写入
await File.WriteAllTextAsync("out.txt", content);
```

---

**基本写法：读取字节**
`File.ReadAllBytes(<路径>);`
```csharp
// 读取二进制内容
byte[] bytes = File.ReadAllBytes("img.png");
```

---

## 按行流式读取

**基本写法：逐行读取**
`File.ReadLines(<路径>);`
```csharp
// 惰性枚举，适合大文件
foreach (string line in File.ReadLines("big.log"))
{
}
```

---

**基本写法：异步逐行读取**
`using var <流> = File.OpenText(<路径>);`
```csharp
// 使用 StreamReader 流式读取
using var reader = new StreamReader("big.txt");
string? line;
while ((line = await reader.ReadLineAsync()) != null) { }
```

---

## FileStream 文件流

**基本写法：创建文件流**
`new FileStream(<路径>, <模式>, [<访问>]);`
```csharp
// 创建可读写文件流
using var fs = new FileStream("data.bin", FileMode.Create, FileAccess.ReadWrite);
```

---

**基本写法：Open 简便打开**
`File.Open(<路径>, <模式>);`
```csharp
// 简便方式打开文件
using var fs = File.Open("data.txt", FileMode.OpenOrCreate);
```

---

**基本写法：写入字节**
`<流>.Write(<字节数组>, <偏移>, <长度>);`
```csharp
// 写入字节数据
fs.Write(buffer, 0, buffer.Length);
```

---

**基本写法：读取字节**
`<流>.Read(<字节数组>, <偏移>, <长度>);`
```csharp
// 读取到缓冲区
int read = fs.Read(buffer, 0, buffer.Length);
```

---

**基本写法：定位 Seek**
`<流>.Seek(<偏移>, <起点>);`
```csharp
// 移动读写位置
fs.Seek(0, SeekOrigin.Begin);
```

---

## StreamWriter / StreamReader

**基本写法：StreamWriter 写文本**
`using var <写流> = new StreamWriter(<路径>);`
```csharp
// 文本写入流
using var writer = new StreamWriter("out.txt");
writer.WriteLine("第一行");
writer.Write("不换行");
```

---

**基本写法：StreamReader 读文本**
`using var <读流> = new StreamReader(<路径>);`
```csharp
// 文本读取流
using var reader = new StreamReader("in.txt");
string content = reader.ReadToEnd();
```

---

**基本写法：自动刷新**
`new StreamWriter(<路径>, <append>, <编码>, <缓冲>);`
```csharp
// 指定编码与缓冲大小
using var writer = new StreamWriter("out.txt", append: true, Encoding.UTF8, 1024);
```

---

## BinaryReader / BinaryWriter

**基本写法：BinaryWriter 写二进制**
`using var <写流> = new BinaryWriter(<流>);`
```csharp
// 写入基础类型二进制
using var writer = new BinaryWriter(File.Open("d.bin", FileMode.Create));
writer.Write(42);
writer.Write("hello");
```

---

**基本写法：BinaryReader 读二进制**
`using var <读流> = new BinaryReader(<流>);`
```csharp
// 按写入顺序读取基础类型
using var reader = new BinaryReader(File.Open("d.bin", FileMode.Open));
int n = reader.ReadInt32();
string s = reader.ReadString();
```

---

## MemoryStream 内存流

**基本写法：创建内存流**
`using var <流> = new MemoryStream();`
```csharp
// 内存中操作字节
using var ms = new MemoryStream();
ms.Write(buffer, 0, buffer.Length);
```

---

**基本写法：转字节数组**
`<流>.ToArray();`
```csharp
// 获取流中所有字节
byte[] bytes = ms.ToArray();
```

---

## 文件与目录管理

**基本写法：判断文件存在**
`File.Exists(<路径>);`
```csharp
// 判断文件是否存在
bool exists = File.Exists("data.txt");
```

---

**基本写法：复制文件**
`File.Copy(<源>, <目标>, [<覆盖>]);`
```csharp
// 复制文件，true 表示覆盖
File.Copy("a.txt", "b.txt", overwrite: true);
```

---

**基本写法：移动文件**
`File.Move(<源>, <目标>);`
```csharp
// 移动或重命名文件
File.Move("a.txt", "dir/a.txt");
```

---

**基本写法：删除文件**
`File.Delete(<路径>);`
```csharp
// 删除文件（不存在不抛异常）
File.Delete("a.txt");
```

---

**基本写法：获取文件信息**
`new FileInfo(<路径>);`
```csharp
// 获取文件大小与时间
var fi = new FileInfo("data.txt");
long size = fi.Length;
DateTime time = fi.LastWriteTime;
```

---

## 目录操作

**基本写法：创建目录**
`Directory.CreateDirectory(<路径>);`
```csharp
// 递归创建目录
Directory.CreateDirectory("a/b/c");
```

---

**基本写法：列出文件**
`Directory.GetFiles(<路径>, [<模式>]);`
```csharp
// 列出目录下所有 txt 文件
string[] files = Directory.GetFiles("dir", "*.txt");
```

---

**基本写法：递归列出**
`Directory.GetFiles(<路径>, <模式>, SearchOption.AllDirectories);`
```csharp
// 递归列出所有子目录文件
var files = Directory.GetFiles("dir", "*.*", SearchOption.AllDirectories);
```

---

**基本写法：枚举文件（惰性）**
`Directory.EnumerateFiles(<路径>);`
```csharp
// 惰性枚举，适合大目录
foreach (var f in Directory.EnumerateFiles("dir")) { }
```

---

**基本写法：删除目录**
`Directory.Delete(<路径>, [<递归>]);`
```csharp
// 递归删除目录
Directory.Delete("dir", recursive: true);
```

---

## using 与资源释放

**基本写法：using 声明**
`using var <流> = new FileStream(...);`
```csharp
// 作用域结束自动 Dispose
using var fs = new FileStream("a.txt", FileMode.Open);
```

---

**基本写法：using 语句**
`using (<流>) { }`
```csharp
// 显式作用域
using (var fs = new FileStream("a.txt", FileMode.Open))
{
}
```

---

**基本写法：await using 异步释放**
`await using var <流> = <异步流>;`
```csharp
// 异步释放 IAsyncDisposable
await using var fs = new FileStream("a.txt", FileMode.Open);
```



<!-- ============ 文档分隔线：015-csharp/015-JsonSerialization.md ============ -->

# C# JSON 序列化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本序列化

**基本写法：序列化为 JSON**
`JsonSerializer.Serialize(<对象>, [<选项>]);`
```csharp
// 对象转 JSON 字符串
string json = JsonSerializer.Serialize(user);
```

---

**基本写法：泛型序列化**
`JsonSerializer.Serialize<<类型>>(<对象>);`
```csharp
// 显式指定类型序列化
string json = JsonSerializer.Serialize<User>(user);
```

---

**基本写法：反序列化**
`JsonSerializer.Deserialize<<类型>>(<json>);`
```csharp
// JSON 字符串转对象
var user = JsonSerializer.Deserialize<User>(json);
```

---

**基本写法：异步序列化到流**
`await JsonSerializer.SerializeAsync(<流>, <对象>);`
```csharp
// 异步写入流，适合大对象
using var fs = File.Create("out.json");
await JsonSerializer.SerializeAsync(fs, users);
```

---

**基本写法：异步反序列化**
`await JsonSerializer.DeserializeAsync<<类型>>(<流>);`
```csharp
// 从流异步读取并反序列化
using var fs = File.OpenRead("in.json");
var data = await JsonSerializer.DeserializeAsync<List<User>>(fs);
```

---

## 序列化选项

**基本写法：缩进格式化**
`JsonSerializerOptions <变量> = new() { WriteIndented = true };`
```csharp
// 输出带缩进的可读 JSON
var opts = new JsonSerializerOptions { WriteIndented = true };
string json = JsonSerializer.Serialize(user, opts);
```

---

**基本写法：驼峰命名**
`<选项>.PropertyNamingPolicy = JsonNamingPolicy.CamelCase;`
```csharp
// 属性名转为 camelCase
var opts = new JsonSerializerOptions { PropertyNamingPolicy = JsonNamingPolicy.CamelCase };
```

---

**基本写法：忽略 null 值**
`<选项>.DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull;`
```csharp
// 值为 null 的属性不输出
var opts = new JsonSerializerOptions
{
    DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull
};
```

---

**基本写法：允许尾随逗号与注释**
`<选项>.ReadCommentHandling = JsonCommentHandling.Skip;`
```csharp
// 容忍注释与尾随逗号
var opts = new JsonSerializerOptions
{
    ReadCommentHandling = JsonCommentHandling.Skip,
    AllowTrailingCommas = true
};
```

---

**基本写法：大小写不敏感**
`<选项>.PropertyNameCaseInsensitive = true;`
```csharp
// 反序列化时属性名大小写不敏感
var opts = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
```

---

## 属性控制

**基本写法：自定义属性名**
`[JsonPropertyName("<名称>")]`
```csharp
// 指定 JSON 中的属性名
public class User
{
    [JsonPropertyName("user_name")]
    public string Name { get; set; }
}
```

---

**基本写法：忽略属性**
`[JsonIgnore]`
```csharp
// 序列化时忽略该属性
public class User
{
    public string Name { get; set; }
    [JsonIgnore]
    public string Password { get; set; }
}
```

---

**基本写法：条件忽略**
`[JsonIgnore(Condition = <条件>)]`
```csharp
// 仅在值为 null 时忽略
[JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingNull)]
public string? Nick { get; set; }
```

---

**基本写法：属性顺序**
`[JsonPropertyOrder(<序号>)]`
```csharp
// 控制属性输出顺序
public class User
{
    [JsonPropertyOrder(0)]
    public int Id { get; set; }
    [JsonPropertyOrder(1)]
    public string Name { get; set; }
}
```

---

## 集合与字典

**基本写法：序列化集合**
`JsonSerializer.Serialize(<集合>);`
```csharp
// 列表转 JSON 数组
string json = JsonSerializer.Serialize(new List<int> { 1, 2, 3 });
```

---

**基本写法：字典序列化**
`JsonSerializer.Serialize<<字典类型>>(<字典>);`
```csharp
// 字典转 JSON 对象
var dict = new Dictionary<string, int> { ["a"] = 1 };
string json = JsonSerializer.Serialize(dict);
```

---

**基本写法：非字符串键字典**
`JsonSerializerOptions <变量> = new() { DictionaryKeyPolicy = <策略> };`
```csharp
// 非字符串键需要键策略或自定义转换器
var opts = new JsonSerializerOptions { DictionaryKeyPolicy = JsonNamingPolicy.CamelCase };
```

---

## 自定义转换器

**基本写法：实现 JsonConverter**
`public class <类名> : JsonConverter<<类型>> { }`
```csharp
// 自定义类型转换器
public class DateTimeConverter : JsonConverter<DateTime>
{
    public override DateTime Read(ref Utf8JsonReader reader, Type t, JsonSerializerOptions o)
        => DateTime.Parse(reader.GetString()!);
    public override void Write(Utf8JsonWriter writer, DateTime v, JsonSerializerOptions o)
        => writer.WriteStringValue(v.ToString("yyyy-MM-dd"));
}
```

---

**基本写法：应用转换器**
`<选项>.Converters.Add(new <转换器>());`
```csharp
// 全局注册转换器
var opts = new JsonSerializerOptions();
opts.Converters.Add(new DateTimeConverter());
```

---

**基本写法：特性应用转换器**
`[JsonConverter(typeof(<转换器>))]`
```csharp
// 单属性应用转换器
public class Order
{
    [JsonConverter(typeof(DateTimeConverter))]
    public DateTime CreatedAt { get; set; }
}
```

---

## 多态序列化

**基本写法：声明派生类**
`[JsonDerivedType(typeof(<派生类>), "<鉴别名>")]`
```csharp
// 基类声明所有派生类型
[JsonDerivedType(typeof(Circle), "circle")]
[JsonDerivedType(typeof(Square), "square")]
public abstract class Shape { }
```

---

**基本写法：多态反序列化**
`JsonSerializer.Deserialize<<基类>>(<json>);`
```csharp
// JSON 含 $type 字段自动识别类型
Shape shape = JsonSerializer.Deserialize<Shape>(json);
```

---

## 流式读写 Utf8JsonReader/Writer

**基本写法：Utf8JsonWriter 写入**
`using var <写流> = new Utf8JsonWriter(<输出>);`
```csharp
// 手动生成 JSON，性能最高
using var writer = new Utf8JsonWriter(File.Create("out.json"));
writer.WriteStartObject();
writer.WriteString("name", "Alice");
writer.WriteNumber("age", 30);
writer.WriteEndObject();
```

---

**基本写法：Utf8JsonReader 读取**
`ref Utf8JsonReader <变量> = ...;`
```csharp
// 手动解析 JSON 字节，零分配
var reader = new Utf8JsonReader(jsonBytes);
while (reader.Read())
{
    if (reader.TokenType == JsonTokenType.PropertyName) { }
}
```

---

## 节点模型 JsonDocument/JsonNode

**基本写法：JsonDocument 只读解析**
`using var <文档> = JsonDocument.Parse(<json>);`
```csharp
// DOM 风格只读访问
using var doc = JsonDocument.Parse(json);
string name = doc.RootElement.GetProperty("name").GetString()!;
```

---

**基本写法：JsonNode 可读写 DOM**
`JsonNode <变量> = JsonNode.Parse(<json>);`
```csharp
// 可读写的 DOM
JsonNode node = JsonNode.Parse(json)!;
node["age"] = 31;
string json2 = node.ToJsonString();
```

---

**基本写法：创建 JsonObject**
`JsonObject <变量> = new() { ["<键>"] = <值> };`
```csharp
// 直接构造 JSON 对象
var obj = new JsonObject { ["name"] = "Alice", ["age"] = 30 };
string json = obj.ToJsonString();
```

---

## 源生成器

**基本写法：JsonSerializerContext 源生成**
`[JsonSerializable(typeof(<类型>))]`
```csharp
// 编译时生成序列化代码，AOT 友好
[JsonSourceGenerationOptions(WriteIndented = true)]
[JsonSerializable(typeof(User))]
public partial class MyContext : JsonSerializerContext { }
```

---

**基本写法：使用源生成上下文**
`JsonSerializer.Serialize(<对象>, <Context>.Default.<类型>);`
```csharp
// 使用生成的元数据序列化
string json = JsonSerializer.Serialize(user, MyContext.Default.User);
```



<!-- ============ 文档分隔线：015-csharp/016-RegularExpression.md ============ -->

# C# 正则表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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



<!-- ============ 文档分隔线：015-csharp/017-CSharp12NewFeatures.md ============ -->

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



<!-- ============ 文档分隔线：015-csharp/018-DotnetCli.md ============ -->

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



<!-- ============ 文档分隔线：015-csharp/019-SpanMemory.md ============ -->

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



<!-- ============ 文档分隔线：015-csharp/020-GenericVariance.md ============ -->

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



<!-- ============ 文档分隔线：015-csharp/021-NetworkingHttp.md ============ -->

# C# HttpClient 网络请求

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## HttpClient 基础

**基本写法：创建 HttpClient**
`HttpClient <变量> = new();`
```csharp
// 单例复用，避免套接字耗尽
private static readonly HttpClient _client = new();
```

---

**基本写法：GET 字符串**
`await <client>.GetStringAsync(<url>);`
```csharp
// 直接获取响应文本
string body = await _client.GetStringAsync("https://api.example.com/users");
```

---

**基本写法：GET 字节数组**
`await <client>.GetByteArrayAsync(<url>);`
```csharp
// 获取二进制内容
byte[] bytes = await _client.GetByteArrayAsync("https://a.com/img.png");
```

---

**基本写法：GET 流**
`await <client>.GetStreamAsync(<url>);`
```csharp
// 获取响应流，适合大文件
using Stream s = await _client.GetStreamAsync(url);
```

---

**基本写法：HttpClientFactory 注册**
`services.AddHttpClient();`
```csharp
// ASP.NET Core 中使用工厂管理生命周期
builder.Services.AddHttpClient();
```

---

## 基本请求响应

**基本写法：发送 GET 请求**
`await <client>.GetAsync(<url>);`
```csharp
// 获取完整响应对象
using var resp = await _client.GetAsync(url);
resp.EnsureSuccessStatusCode();
```

---

**基本写法：读取响应内容**
`await <响应>.Content.ReadAsStringAsync();`
```csharp
// 读取响应体字符串
var resp = await _client.GetAsync(url);
string body = await resp.Content.ReadAsStringAsync();
```

---

**基本写法：POST 字符串**
`await <client>.PostAsync(<url>, <内容>);`
```csharp
// 提交字符串内容
var content = new StringContent("raw body", Encoding.UTF8, "text/plain");
await _client.PostAsync(url, content);
```

---

**基本写法：POST JSON**
`JsonContent.Create(<对象>);`
```csharp
// .NET 5+ 直接创建 JSON 内容
var json = JsonContent.Create(user);
await _client.PostAsync(url, json);
```

---

**基本写法：POST 表单**
`new FormUrlEncodedContent(<字典>);`
```csharp
// 提交 application/x-www-form-urlencoded
var form = new FormUrlEncodedContent(new[]
{
    new KeyValuePair<string, string>("name", "Alice")
});
await _client.PostAsync(url, form);
```

---

## HttpRequestMessage 自定义

**基本写法：构造请求消息**
`new HttpRequestMessage(<方法>, <url>);`
```csharp
// 完全自定义请求
var req = new HttpRequestMessage(HttpMethod.Post, url);
req.Content = json;
var resp = await _client.SendAsync(req);
```

---

**基本写法：自定义方法**
`new HttpMethod("<方法名>")`
```csharp
// 使用 PATCH 等非标准方法
var req = new HttpRequestMessage(new HttpMethod("PATCH"), url);
```

---

**基本写法：添加请求头**
`<请求>.Headers.Add("<名称>", "<值>");`
```csharp
// 设置请求头
req.Headers.Add("Authorization", "Bearer token123");
req.Headers.Add("X-Request-Id", Guid.NewGuid().ToString());
```

---

**基本写法：默认请求头**
`<client>.DefaultRequestHeaders.Add("<名称>", "<值>");`
```csharp
// 所有请求都带上的头
_client.DefaultRequestHeaders.Add("User-Agent", "MyApp/1.0");
```

---

**基本写法：超时设置**
`<client>.Timeout = <时间>;`
```csharp
// 设置全局超时
_client.Timeout = TimeSpan.FromSeconds(30);
```

---

## 响应处理

**基本写法：读取响应头**
`<响应>.Headers.<名称>`
```csharp
// 获取响应头
foreach (var h in resp.Headers)
{
    Console.WriteLine($"{h.Key}: {string.Join(",", h.Value)}");
}
```

---

**基本写法：获取状态码**
`<响应>.StatusCode`
```csharp
// 读取 HTTP 状态码
HttpStatusCode code = resp.StatusCode;
if (code == HttpStatusCode.OK) { }
```

---

**基本写法：反序列化 JSON 响应**
`await JsonSerializer.DeserializeAsync<<类型>>(<流>);`
```csharp
// 流式反序列化响应
var resp = await _client.GetAsync(url);
var user = await JsonSerializer.DeserializeAsync<User>(
    await resp.Content.ReadAsStreamAsync());
```

---

## 取消与进度

**基本写法：取消请求**
`await <client>.GetAsync(<url>, <token>);`
```csharp
// 传入取消令牌
using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(10));
var resp = await _client.GetAsync(url, cts.Token);
```

---

**基本写法：HttpCompletionOption**
`await <client>.GetAsync(<url>, HttpCompletionOption.ResponseHeadersRead);`
```csharp
// 收到响应头即返回，不等读完体
var resp = await _client.GetAsync(url, HttpCompletionOption.ResponseHeadersRead);
```

---

**基本写法：上传进度**
`<流>.ReadAsync(<缓冲>, <token>)`
```csharp
// 自定义 HttpContent 实现上传进度
public class ProgressContent : HttpContent { /* 重写 SerializeToStreamAsync */ }
```

---

## 上传文件

**基本写法：Multipart 表单**
`MultipartFormDataContent <变量> = new();`
```csharp
// multipart/form-data 上传文件
using var form = new MultipartFormDataContent();
var fileContent = new ByteArrayContent(File.ReadAllBytes(path));
fileContent.Headers.ContentType = new MediaTypeHeaderValue("image/png");
form.Add(fileContent, "file", "photo.png");
await _client.PostAsync(url, form);
```

---

**基本写法：流式上传**
`new StreamContent(<流>);`
```csharp
// 大文件用流避免全加载到内存
using var fs = File.OpenRead("big.zip");
var form = new MultipartFormDataContent();
form.Add(new StreamContent(fs), "file", "big.zip");
await _client.PostAsync(url, form);
```

---

## 复用与命名客户端

**基本写法：命名客户端**
`services.AddHttpClient("<名称>", <配置>);`
```csharp
// 注册预配置的命名 HttpClient
builder.Services.AddHttpClient("github", c =>
{
    c.BaseAddress = new Uri("https://api.github.com/");
    c.DefaultRequestHeaders.Add("Accept", "application/vnd.github.v3+json");
});
```

---

**基本写法：注入命名客户端**
`IHttpClientFactory <变量>`
```csharp
// 通过工厂获取命名客户端
public class Service(IHttpClientFactory factory)
{
    public async Task DoAsync()
    {
        var client = factory.CreateClient("github");
        var json = await client.GetStringAsync("users/octocat");
    }
}
```

---

**基本写法：类型化客户端**
`services.AddHttpClient<<类型>>();`
```csharp
// 直接绑定到某服务类
builder.Services.AddHttpClient<GitHubService>(c => c.BaseAddress = new Uri("https://api.github.com/"));
```

---

## BaseAddress 与相对路径

**基本写法：设置基地址**
`<client>.BaseAddress = new Uri(<url>);`
```csharp
// 设置基地址后用相对路径
_client.BaseAddress = new Uri("https://api.example.com/");
var json = await _client.GetStringAsync("users/1");
```

---

## 重试与弹性

**基本写法：Polly 重试**
`services.AddHttpClient("<名称>").AddTransientHttpErrorPolicy(...)`
```csharp
// 使用 Polly 实现重试
builder.Services.AddHttpClient("api")
    .AddTransientHttpErrorPolicy(p =>
        p.WaitAndRetryAsync(3, i => TimeSpan.FromSeconds(i)));
```

---

**基本写法：超时策略**
`.AddPolicyHandler(Policy.TimeoutAsync<<HttpResponseMessage>>(<秒>))`
```csharp
// 每个请求的超时策略
.AddPolicyHandler(Policy.TimeoutAsync<HttpResponseMessage>(TimeSpan.FromSeconds(20)));
```

---

## Cookie 与代理

**基本写法：处理 Cookie**
`new HttpClient(new HttpClientHandler { UseCookies = true })`
```csharp
// 启用 Cookie 容器
var handler = new HttpClientHandler { UseCookies = true, CookieContainer = new CookieContainer() };
var client = new HttpClient(handler);
```

---

**基本写法：设置代理**
`new HttpClientHandler { Proxy = <代理> }`
```csharp
// 通过代理访问
var handler = new HttpClientHandler
{
    Proxy = new WebProxy("http://proxy:8080", true)
};
var client = new HttpClient(handler);
```

---

## SocketsHttpHandler 配置

**基本写法：自定义连接池**
`new SocketsHttpHandler { PooledConnectionLifetime = <时间> }`
```csharp
// .NET Core 2.1+ 默认使用 SocketsHttpHandler
var handler = new SocketsHttpHandler
{
    PooledConnectionLifetime = TimeSpan.FromMinutes(2),
    MaxConnectionsPerServer = 100
};
var client = new HttpClient(handler);
```



<!-- ============ 文档分隔线：015-csharp/022-CSharp13NewFeatures.md ============ -->

﻿# C# 13 新特性 语法速查手册

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



<!-- ============ 文档分隔线：015-csharp/023-CSharpExceptionHandling.md ============ -->

﻿# C# 异常处理 语法速查手册

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
