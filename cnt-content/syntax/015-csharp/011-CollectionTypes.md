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
