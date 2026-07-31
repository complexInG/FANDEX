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
