---
order: 10
title: kotlin 模块文档合集
module: 'kotlin'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：014-kotlin/001-KotlinGenericTypeSystem.md ============ -->

# Kotlin 泛型与类型系统速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型基础

**基本写法：泛型类**
`class <Name><T>(val <prop>: T) { <body> }`
```kotlin
// 泛型类定义
class Box<T>(val value: T) {
    fun unwrap(): T = value;
}
```

**基本写法：泛型接口**
`interface <Name><T> { fun <method>(<param>): T }`
```kotlin
// 泛型接口定义
interface Repository<T> {
    fun findById(id: String): T?;
    fun save(entity: T): T;
}
```

**基本写法：泛型函数**
`fun <T> <name>(<params>): <ReturnType>`
```kotlin
// 泛型函数定义
fun <T> List<T>.secondOrNull(): T? =
    if (this.size >= 2) this[1] else null;
```

**基本写法：带约束的泛型函数**
`fun <T : <Bound>> <name>(<params>): <ReturnType>`
```kotlin
// T 必须实现 Comparable<T>
fun <T : Comparable<T>> maxOf(a: T, b: T): T = if (a > b) a else b;
```

**单行写法：多类型参数泛型类**
`class <Name><A, B>(val <prop1>: A, val <prop2>: B)`
```kotlin
// 单行多类型参数泛型类
class Pair<A, B>(val first: A, val second: B);
```

**换行写法：多类型参数泛型函数**
`fun <K, V> <name>(<param>): <ReturnType> { <body> }`
```kotlin
// 换行声明多类型参数泛型函数
fun <K, V> buildMap(builder: MutableMap<K, V>.() -> Unit): Map<K, V> {
    val map = mutableMapOf<K, V>();
    map.builder();
    return map;
}
```

---

## 型变

**基本写法：协变（out）**
`interface <Name><out T> { fun <method>(): T }`
```kotlin
// 协变：T 只能作为返回类型
interface Producer<out T> {
    fun produce(): T;
}
```

**基本写法：逆变（in）**
`interface <Name><in T> { fun <method>(<param>: T) }`
```kotlin
// 逆变：T 只能作为参数类型
interface Consumer<in T> {
    fun consume(item: T);
}
```

**基本写法：使用处协变投影**
`fun <name>(<param>: Array<out <Type>>)`
```kotlin
// 使用处协变投影
fun copy(from: Array<out Any>, to: Array<Any>) {
    for (i in from.indices) {
        to[i] = from[i];
    }
}
```

**基本写法：使用处逆变投影**
`fun <name>(<param>: Array<in <Type>>)`
```kotlin
// 使用处逆变投影
fun fill(array: Array<in String>, value: String) {
    for (i in array.indices) {
        array[i] = value;
    }
}
```

---

## 星投影

**基本写法：Array 星投影**
`fun <name>(<param>: Array<*>)`
```kotlin
// Array<*> 等价于 Array<out Any?>
fun printArray(array: Array<*>) {
    for (item in array) {
        println(item);
    }
}
```

**基本写法：Map 星投影**
`fun <name>(<param>: Map<*, *>)`
```kotlin
// Map<*, *> 两个类型参数都未知
fun printMap(map: Map<*, *>) {
    for ((key, value) in map) {
        println("$key: $value");
    }
}
```

---

## 泛型约束

**基本写法：上界约束**
`fun <T : <Bound>> <name>(<params>): <ReturnType>`
```kotlin
// T 必须实现 Comparable<T>
fun <T : Comparable<T>> sort(list: List<T>): List<T> {
    return list.sorted();
}
```

**换行写法：多重约束（where 子句）**
`fun <T> <name>(<params>): <ReturnType> where T : <Bound1>, T : <Bound2>`
```kotlin
// 多重约束
fun <T> process(value: T): String where T : CharSequence, T : Comparable<T> {
    return if (value > "threshold") value.toString() else "default";
}
```

**基本写法：非空上界约束**
`fun <T : Any> <name>(<param>: T)`
```kotlin
// 显式非空上界
fun <T : Any> nonNullExample(value: T) {
    // T 的上界是 Any，value 不为 null
}
```

---

## reified 类型参数

**基本写法：reified 类型参数**
`inline fun <reified T> <name>(<param>): <ReturnType>`
```kotlin
// reified 保留类型信息
inline fun <reified T> isType(value: Any): Boolean = value is T;
```

**基本写法：reified 类型安全 JSON 解析**
`inline fun <reified T> <name>(): T`
```kotlin
// 类型安全的 JSON 解析
inline fun <reified T> HttpClient.parseResponse(): T {
    val response = execute();
    return Json.decodeFromString<T>(response.body);
}
```

---

## 空安全

**基本写法：非空类型**
`var <name>: <Type> = <value>`
```kotlin
// 非空类型，不能赋 null
var name: String = "Kotlin";
```

**基本写法：可空类型**
`var <name>: <Type>? = <value>`
```kotlin
// 可空类型，允许 null
var nickname: String? = "Kt";
nickname = null;
```

**基本写法：安全调用操作符 ?.**
`<obj>?.<prop>`
```kotlin
// 安全调用，为 null 时返回 null
val length: Int? = nickname?.length;
```

**基本写法：非空断言 !!**
`<obj>!!.<prop>`
```kotlin
// 非空断言，为 null 时抛出 NPE
val length: Int = nickname!!.length;
```

**基本写法：Elvis 操作符 ?:**
`<expr> ?: <default>`
```kotlin
// Elvis 运算符提供默认值
val length: Int = nickname?.length ?: 0;
```

**基本写法：Elvis 与 throw 结合**
`<expr> ?: throw <Exception>`
```kotlin
// 为 null 时抛出异常
val value = nullableValue ?: throw IllegalArgumentException("Required value is null");
```

**基本写法：let 安全调用**
`<obj>?.let { <body with it> }`
```kotlin
// let 安全调用非空值
nickname?.let {
    println("Length: ${it.length}");
}
```

**基本写法：安全类型转换 as?**
`<obj> as? <Type>`
```kotlin
// 安全转换，失败返回 null
val number: Int? = value as? Int;
```

**基本写法：filterNotNull 过滤 null**
`<list>.filterNotNull()`
```kotlin
// 过滤集合中的 null 值
val list: List<String?> = listOf("a", null, "b");
val nonNull: List<String> = list.filterNotNull();
```

**基本写法：mapNotNull 映射并过滤 null**
`<list>.mapNotNull { <transform> }`
```kotlin
// 映射并过滤 null
val lengths: List<Int> = list.mapNotNull { it?.length };
```

---

## 智能转换

**基本写法：is 检查后智能转换**
`if (<obj> is <Type>) { <body with obj as Type> }`
```kotlin
// is 检查后自动智能转换
if (input is String) {
    println(input.length);
}
```

**基本写法：when 中的智能转换**
`fun <name>(<param>: Any) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// when 中 is 检查后智能转换
fun describe(x: Any) = when (x) {
    is Int -> "Int: ${x + 1}";
    is String -> "String: ${x.length}";
    else -> "Unknown";
}
```

**基本写法：null 检查后智能转换**
`if (<obj> != null) { <body with obj as non-null> }`
```kotlin
// null 检查后智能转换为非空
fun greet(name: String?) {
    if (name != null) {
        println(name.length);
    }
}
```

**基本写法：智能转换的限制**
`val <local> = <prop>; if (<local> != null) { <body> }`
```kotlin
// var 属性需使用局部变量避免智能转换限制
val v = value;
if (v != null) {
    println(v.length);
}
```

---

## 类型系统特殊类型

**基本写法：Nothing 类型**
`fun <name>(<params>): Nothing`
```kotlin
// Nothing 表示永远不会正常返回
fun fail(message: String): Nothing {
    throw IllegalArgumentException(message);
}
```

**基本写法：Nothing 用于类型推断**
`val <name>: <Type> = if (<cond>) <expr> else fail(<msg>)`
```kotlin
// Nothing 是所有类型的子类型
val result: String = if (condition) "success" else fail("error");
```

**基本写法：Unit 类型**
`fun <name>(<params>): Unit { <body> }`
```kotlin
// Unit 表示无返回值
fun printHello(): Unit {
    println("Hello");
}
```

**基本写法：Unit 作为泛型参数**
`val <name>: List<() -> Unit> = listOf(<lambdas>)`
```kotlin
// Unit 作为泛型参数
val actions: List<() -> Unit> = listOf(
    { println("Action 1"); },
    { println("Action 2"); }
);
```

**基本写法：Any 类型**
`val <name>: Any = <value>`
```kotlin
// Any 是所有非空类型的根
val value: Any = "Hello";
```

**基本写法：Any? 类型**
`val <name>: Any? = null`
```kotlin
// Any? 是所有类型的根（包括可空类型）
val nullable: Any? = null;
```



<!-- ============ 文档分隔线：014-kotlin/002-KotlinFunctionAndLambda.md ============ -->

# Kotlin 函数与 Lambda 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数定义

**基本写法：标准函数**
`fun <name>(<params>): <ReturnType> { <body> }`
```kotlin
// 标准函数定义
fun add(a: Int, b: Int): Int {
    return a + b;
}
```

**基本写法：表达式函数体**
`fun <name>(<params>): <ReturnType> = <expr>`
```kotlin
// 表达式函数体
fun add(a: Int, b: Int): Int = a + b;
```

**基本写法：表达式函数体类型推断**
`fun <name>(<params>) = <expr>`
```kotlin
// 返回类型推断为 Int
fun add(a: Int, b: Int) = a + b;
```

**基本写法：Unit 无返回值函数**
`fun <name>(<params>): Unit { <body> }`
```kotlin
// 无返回值（Unit）
fun greet(name: String): Unit {
    println("Hello, $name!");
}
```

**基本写法：省略 Unit 的无返回值函数**
`fun <name>(<params>) { <body> }`
```kotlin
// Unit 可省略
fun greet(name: String) {
    println("Hello, $name!");
}
```

**单行写法：默认参数函数**
`fun <name>(<param1>: <Type>, <param2>: <Type> = <default>): <ReturnType>`
```kotlin
// 单行声明带默认参数的函数
fun connect(host: String, port: Int = 8080): String = "$host:$port";
```

**换行写法：多默认参数函数**
`fun <name>(<param1>: <Type>, <param2>: <Type> = <default>, <param3>: <Type> = <default>): <ReturnType>`
```kotlin
// 换行声明多个默认参数
fun connect(
    host: String,
    port: Int = 8080,
    timeout: Int = 5000
): String {
    return "$host:$port (timeout: ${timeout}ms)";
}
```

**基本写法：命名参数调用**
`<name>(<arg> = <value>)`
```kotlin
// 使用命名参数跳过中间参数
createUser("Alice", email = "alice@example.com");
```

**基本写法：可变参数函数**
`fun <name>(vararg <params>: <Type>): <ReturnType>`
```kotlin
// 可变参数函数
fun sum(vararg numbers: Int): Int {
    return numbers.sum();
}
```

**基本写法：展开数组调用可变参数**
`<name>(*<array>)`
```kotlin
// 使用 * 展开运算符
val array = intArrayOf(1, 2, 3);
sum(*array);
```

**基本写法：尾递归函数**
`tailrec fun <name>(<params>): <ReturnType>`
```kotlin
// 尾递归函数，避免栈溢出
tailrec fun factorial(n: Long, acc: Long = 1): Long {
    return if (n <= 1) acc else factorial(n - 1, acc * n);
}
```

---

## 扩展函数

**基本写法：为类添加扩展函数**
`fun <ReceiverType>.<name>(<params>): <ReturnType>`
```kotlin
// 为 String 添加扩展函数
fun String.addExclamation(): String = this + "!";
```

**基本写法：为 Int 添加扩展函数**
`fun Int.<name>(): <ReturnType>`
```kotlin
// 为 Int 添加扩展
fun Int.isEven(): Boolean = this % 2 == 0;
```

**基本写法：可空接收者扩展**
`fun <ReceiverType>?.<name>(<params>): <ReturnType>`
```kotlin
// 可空接收者，在函数内部处理 null
fun String?.isNullOrEmpty(): Boolean = this == null || this.isEmpty();
```

**基本写法：只读扩展属性**
`val <ReceiverType>.<name>: <Type> get() = <expr>`
```kotlin
// 为 String 添加只读扩展属性
val String.halfLength: Int
    get() = this.length / 2;
```

**换行写法：可变扩展属性**
`var <ReceiverType>.<name>: <Type> [get() = <expr>] [set(value) { <body> }]`
```kotlin
// 为 StringBuilder 添加可变扩展属性
var StringBuilder.lastChar: Char
    get() = this[this.length - 1]
    set(value) { this.append(value); }
```

**基本写法：扩展函数静态解析**
`fun <BaseType>.<name>() = <expr>`
```kotlin
// 扩展函数静态解析，由声明类型决定
open class Animal;
class Dog : Animal();
fun Animal.sound() = "Generic sound";
fun Dog.sound() = "Woof";
val animal: Animal = Dog();
animal.sound();  // "Generic sound"
```

---

## Lambda 表达式

**基本写法：完整语法 Lambda**
`val <name>: (<ParamTypes>) -> <ReturnType> = { <params> -> <body> }`
```kotlin
// 完整语法
val sum: (Int, Int) -> Int = { a: Int, b: Int -> a + b };
```

**基本写法：类型推断 Lambda**
`val <name> = { <params> -> <body> }`
```kotlin
// 类型推断
val sum = { a: Int, b: Int -> a + b };
```

**基本写法：指定类型省略参数类型**
`val <name>: (<ParamTypes>) -> <ReturnType> = { <params> -> <body> }`
```kotlin
// 指定函数类型，省略参数类型
val sum: (Int, Int) -> Int = { a, b -> a + b };
```

**基本写法：it 隐式参数**
`{ <body using it> }`
```kotlin
// 单参数 Lambda 用 it 代替
val square: (Int) -> Int = { it * it };
```

**基本写法：filter 过滤**
`<collection>.filter { <predicate> }`
```kotlin
// filter 过滤集合
val numbers = listOf(1, 2, 3, 4, 5);
numbers.filter { it > 3 };
```

**基本写法：map 映射**
`<collection>.map { <transform> }`
```kotlin
// map 映射集合元素
numbers.map { it * 2 };
```

**基本写法：forEach 遍历**
`<collection>.forEach { <body> }`
```kotlin
// forEach 遍历集合
numbers.forEach { println(it); }
```

**基本写法：fold 累积**
`<collection>.fold(<init>) { <acc>, <item> -> <body> }`
```kotlin
// fold 带初始值累积
val sum = numbers.fold(0) { acc, num -> acc + num };
```

**基本写法：groupBy 分组**
`<collection>.groupBy { <keySelector> }`
```kotlin
// groupBy 按条件分组
val grouped = numbers.groupBy { if (it % 2 == 0) "even" else "odd" };
```

---

## 高阶函数

**基本写法：函数作为参数**
`fun <name>(<param>: (<Type>) -> <ReturnType>): <ReturnType>`
```kotlin
// 接受函数作为参数
fun <T> List<T>.customFilter(predicate: (T) -> Boolean): List<T> {
    val result = mutableListOf<T>();
    for (item in this) {
        if (predicate(item)) result.add(item);
    }
    return result;
}
```

**基本写法：函数作为返回值**
`fun <name>(<params>): (<Type>) -> <ReturnType>`
```kotlin
// 返回函数
fun multiplier(factor: Int): (Int) -> Int = { number -> number * factor };
```

**基本写法：无参函数类型**
`val <name>: () -> <ReturnType> = { <body> }`
```kotlin
// 无参函数类型
val f1: () -> Unit = { println("No params"); };
```

**基本写法：带参函数类型**
`val <name>: (<Type>) -> <ReturnType> = { <body> }`
```kotlin
// 带参函数类型
val f2: (Int) -> String = { "Number: $it" };
```

**基本写法：带接收者的函数类型**
`val <name>: <ReceiverType>.(<Type>) -> <ReturnType> = { <body> }`
```kotlin
// 带接收者的函数类型
val f4: String.(Int) -> String = { this.repeat(it) };
```

**基本写法：匿名函数**
`val <name> = fun(<params>): <ReturnType> = <expr>`
```kotlin
// 匿名函数
val f5 = fun(a: Int, b: Int): Int = a + b;
```

**基本写法：also 执行附加操作**
`<obj>.also { <body with it> }`
```kotlin
// also 返回原对象
val user = User("Alice", 25).also {
    println("Created: $it");
};
```

**基本写法：apply 配置对象**
`<obj>.apply { <body with this> }`
```kotlin
// apply 返回原对象
val builder = StringBuilder().apply {
    append("Hello");
    append(", Kotlin");
};
```

**基本写法：let 转换对象**
`<obj>.let { <body with it> }`
```kotlin
// let 返回 Lambda 结果
val length = "Kotlin".let { it.length };
```

**基本写法：run 执行代码块**
`<obj>.run { <body with this> }`
```kotlin
// run 返回 Lambda 结果
val result = "Kotlin".run { length };
```

**基本写法：with 执行多个操作**
`with(<obj>) { <body with this> }`
```kotlin
// with 非扩展版本
val greeting = with(StringBuilder()) {
    append("Hello");
    append(", Kotlin");
    toString();
};
```

---

## 内联函数

**基本写法：inline 内联函数**
`inline fun <name>(<params>): <ReturnType>`
```kotlin
// inline 关键字内联函数
inline fun <T> measureTime(block: () -> T): T {
    val start = System.currentTimeMillis();
    val result = block();
    val end = System.currentTimeMillis();
    println("Execution time: ${end - start}ms");
    return result;
}
```

**换行写法：noinline 与 crossinline**
`inline fun <name>(<param1>: () -> Unit, noinline <param2>: () -> Unit)`
```kotlin
// noinline 禁止内联，crossinline 禁止非局部返回
inline fun process(
    inlineBlock: () -> Unit,
    noinline notInlined: () -> Unit
) {
    inlineBlock();
    notInlined();
}
```

**基本写法：crossinline 禁止非局部返回**
`inline fun <name>(crossinline <param>: () -> Unit)`
```kotlin
// crossinline 允许内联但禁止非局部返回
inline fun runInThread(crossinline action: () -> Unit) {
    Thread { action(); }.start();
}
```

**基本写法：非局部返回**
`<collection>.forEach { if (<cond>) return; <body> }`
```kotlin
// 非局部返回，退出外层函数
fun processElements(elements: List<Int>) {
    elements.forEach {
        if (it == 0) return;
        println(it);
    }
}
```

---

## SAM 转换

**基本写法：Java SAM 接口转换**
`<obj>.setListener { <param> -> <body> }`
```kotlin
// SAM 转换简化 Java 接口实现
button.setOnClickListener { view ->
    println("Clicked: $view");
}
```

**基本写法：Kotlin 函数式接口**
`fun interface <Name> { fun <method>(<params>): <ReturnType> }`
```kotlin
// fun interface 声明
fun interface Producer<T> {
    fun produce(): T;
}
```

**基本写法：函数式接口实例化**
`val <name> = <Interface> { <body> }`
```kotlin
// 函数式接口实例化
val producer = Producer { "Hello" };
```

**单行写法：多类型参数函数式接口**
`fun interface <Name><<T1>, <T2>> { fun <method>(<param>: <T1>): <T2> }`
```kotlin
// 多类型参数函数式接口
fun interface Transformer<T, R> {
    fun transform(input: T): R;
}
```

---

## 作用域函数对比

**基本写法：apply 配置并返回对象**
`<obj>.apply { <body with this> }`
```kotlin
// apply 典型场景：配置对象
val person = Person().apply {
    name = "Alice";
    age = 25;
};
```

**基本写法：also 附加操作并返回对象**
`<obj>.also { <body with it> }`
```kotlin
// also 典型场景：日志记录
val logged = person.also {
    println("Created person: $it");
};
```

**基本写法：let 转换并返回结果**
`<obj>.let { <body with it> }`
```kotlin
// let 典型场景：转换
val nameLength = person.let { it.name.length };
```



<!-- ============ 文档分隔线：014-kotlin/003-KotlinBasicSyntax.md ============ -->

# Kotlin 基础语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量声明

**基本写法：val 声明显式类型只读变量**
`val <name>: <Type> = <value>`
```kotlin
// 声明显式类型的只读变量
val name: String = "Kotlin";
```

**基本写法：val 类型推断只读变量**
`val <name> = <value>`
```kotlin
// 类型推断为 Double
val version = 2.2;
// 类型推断为 Int
val year = 2011;
```

**基本写法：var 声明显式类型可变变量**
`var <name>: <Type> = <value>`
```kotlin
// 声明可变变量并修改
var count: Int = 0;
count = 1;
count += 10;
```

**基本写法：var 类型推断可变变量**
`var <name> = <value>`
```kotlin
// 声明可变字符串变量
var message = "Hello";
message = "World";
```

**基本写法：lateinit 延迟初始化可变变量**
`lateinit var <name>: <Type>`
```kotlin
// 用于 var，延迟初始化引用类型
lateinit var service: UserService;
fun setup() {
    service = UserService();
}
```

**基本写法：by lazy 首次访问时初始化只读变量**
`val <name>: <Type> by lazy { <init> }`
```kotlin
// 用于 val，首次访问时初始化
val heavyObject: ExpensiveClass by lazy {
    println("Initializing...");
    ExpensiveClass();
}
```

**基本写法：const val 编译期常量**
`const val <name> = <value>`
```kotlin
// 编译期常量（顶层或伴生对象中）
const val MAX_SIZE = 100;
```

**单行写法：const val 多常量声明**
`const val <name1> = <value1>; const val <name2> = <value2>`
```kotlin
// 单行声明多个编译期常量
const val APP_NAME = "FANDEX"; const val VERSION = "1.0";
```

---

## 基本类型

**基本写法：Int 整数字面量**
`val <name> = <int>`
```kotlin
// Int 类型字面量
val intVal = 42;
```

**基本写法：Long 长整数字面量**
`val <name> = <int>L`
```kotlin
// Long 类型字面量（后缀 L）
val longVal = 42L;
```

**基本写法：Double 双精度浮点字面量**
`val <name> = <float>`
```kotlin
// Double 类型字面量
val doubleVal = 3.14;
```

**基本写法：Float 单精度浮点字面量**
`val <name> = <float>f`
```kotlin
// Float 类型字面量（后缀 f）
val floatVal = 3.14f;
```

**基本写法：十六进制字面量**
`val <name> = 0x<hex>`
```kotlin
// 十六进制 Int 字面量
val hexVal = 0xFF;
```

**基本写法：二进制字面量**
`val <name> = 0b<binary>`
```kotlin
// 二进制 Int 字面量
val binaryVal = 0b1010;
```

**基本写法：下划线分隔字面量**
`val <name> = <int_with_underscores>`
```kotlin
// 下划线提升可读性
val underscored = 1_000_000;
```

**基本写法：数值显式转换**
`<value>.to<Type>()`
```kotlin
// Kotlin 不支持隐式转换，必须显式调用转换函数
val intVal: Int = 100;
val longVal: Long = intVal.toLong();
```

**基本写法：Boolean 布尔类型**
`val <name>: Boolean = <bool>`
```kotlin
// 声明布尔变量
val isActive: Boolean = true;
```

**基本写法：短路求值**
`val <name> = <bool> && <expr>`
```kotlin
// 短路求值，expensiveCheck 在 isActive 为 false 时不执行
val result = isActive && expensiveCheck();
```

**基本写法：Char 字符类型**
`val <name>: Char = '<char>'`
```kotlin
// Char 用单引号
val letter: Char = 'A';
```

**基本写法：Char Unicode 字符**
`val <name>: Char = '\u<hex>'`
```kotlin
// Unicode 字符
val unicode: Char = '\u0041';
```

**基本写法：String 字符串类型**
`val <name>: String = "<text>"`
```kotlin
// String 用双引号
val text: String = "Hello, Kotlin";
```

**单行写法：trimMargin 原始字符串**
`"""<content>""".trimMargin()`
```kotlin
// trimMargin 去除 | 前缀
val rawText = """
    |Hello,
    |Kotlin!
""".trimMargin();
```

**单行写法：trimIndent 原始字符串**
`"""<content>""".trimIndent()`
```kotlin
// trimIndent 去除公共缩进
val rawText2 = """
    Hello,
    Kotlin!
""".trimIndent();
```

**单行写法：arrayOf 创建对象数组**
`arrayOf(<elements>)`
```kotlin
// 对象数组
val numbers = arrayOf(1, 2, 3, 4, 5);
```

**单行写法：intArrayOf 创建原始类型数组**
`<type>ArrayOf(<elements>)`
```kotlin
// 原始类型数组（无装箱开销）
val intArray = intArrayOf(1, 2, 3);
```

**换行写法：Array 构造函数创建数组**
`Array(<size>) { <index> -> <expr> }`
```kotlin
// 构造函数创建数组，按索引计算元素
val squares = Array(5) { i -> i * i };
```

**换行写法：IntArray 构造函数创建数组**
`<Type>Array(<size>) { <init> }`
```kotlin
// 构造函数创建原始类型数组并初始化
val ones = IntArray(5) { 1 };
```

---

## 字符串模板

**基本写法：简单变量模板**
`"...$<name>..."`
```kotlin
// 简单模板：直接插入变量
val name = "Kotlin";
println("Language: $name");
```

**基本写法：表达式模板**
`"...${<expression>}..."`
```kotlin
// 表达式模板：插入计算结果
val version = 2.2;
println("Version: ${version + 0.1}");
```

**基本写法：嵌套表达式模板**
`"...${<obj>.<prop>}..."`
```kotlin
// 嵌套表达式：访问属性
val list = listOf("a", "b", "c");
println("Size: ${list.size}, First: ${list[0]}");
```

**单行写法：原始字符串中使用模板**
`"""...$<name>..."""`
```kotlin
// 原始字符串中使用模板
val name = "Kotlin";
val json = """
    {
        "name": "$name"
    }
""".trimIndent();
```

---

## 包与导入

**基本写法：包声明**
`package <package.name>`
```kotlin
// 声明包名
package com.example.kotlinbasics;
```

**基本写法：显式导入**
`import <package>.<name>`
```kotlin
// 显式导入单个类或函数
import com.example.utils.Logger;
```

**基本写法：导入并重命名**
`import <package>.<name> as <alias>`
```kotlin
// 导入并重命名解决冲突
import com.example.utils.formatDate as formatDateUtil;
```

**基本写法：导入整个包**
`import <package>.*`
```kotlin
// 导入整个包的所有内容
import com.example.utils.*;
```

**基本写法：导入伴生对象成员**
`import <package>.<Class>.<member>`
```kotlin
// 导入伴生对象成员
import com.example.Config.DEFAULT_TIMEOUT;
```

---

## 控制流

**基本写法：if 表达式**
`val <name> = if (<cond>) <exprA> else <exprB>`
```kotlin
// if 作为表达式赋值
val max = if (a > b) a else b;
```

**换行写法：多分支 if 表达式**
`val <name> = if (<cond>) { <body> } else if (<cond>) { <body> } else { <body> }`
```kotlin
// 多行 if 表达式
val result = if (score >= 90) {
    println("Excellent");
    "A";
} else if (score >= 80) {
    println("Good");
    "B";
} else {
    println("Keep going");
    "C";
}
```

**基本写法：when 表达式**
`when (<subject>) { <branches> }`
```kotlin
// 基本 when 分支匹配
when (x) {
    1 -> println("One");
    2, 3 -> println("Two or Three");
    else -> println("Unknown");
}
```

**基本写法：when 区间匹配**
`when (<subject>) { in <range> -> <expr> }`
```kotlin
// 区间匹配
when (x) {
    in 4..10 -> println("Four to Ten");
    !in 11..20 -> println("Not in 11-20");
}
```

**基本写法：when 类型匹配**
`when (<subject>) { is <Type> -> <expr> }`
```kotlin
// 类型匹配
when (x) {
    is String -> println("It's a String");
}
```

**基本写法：when 作为表达式赋值**
`val <name> = when (<subject>) { <branches> }`
```kotlin
// when 表达式返回值
val description = when (x) {
    0 -> "Zero";
    1, 2, 3 -> "Small";
    in 4..100 -> "Medium";
    else -> "Large";
}
```

**基本写法：无参 when**
`when { <branches> }`
```kotlin
// 无参 when 替代 if-else 链
when {
    x > 0 -> println("Positive");
    x < 0 -> println("Negative");
    else -> println("Zero");
}
```

**基本写法：when 捕获变量智能转换**
`fun <name>(<param>: Any) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// when 中 is 检查后智能转换
fun process(input: Any) = when (input) {
    is Int -> "Integer: ${input * 2}";
    is String -> "String of length ${input.length}";
    else -> "Unknown type";
}
```

**基本写法：for 遍历闭区间**
`for (<item> in <start>..<end>) { <body> }`
```kotlin
// 遍历闭区间
for (i in 1..5) print("$i ");
```

**基本写法：for 遍历半开区间**
`for (<item> in <start> until <end>) { <body> }`
```kotlin
// 遍历半开区间（排除末尾）
for (i in 1 until 5) print("$i ");
```

**基本写法：for 递减遍历**
`for (<item> in <start> downTo <end>) { <body> }`
```kotlin
// 递减遍历
for (i in 5 downTo 1) print("$i ");
```

**基本写法：for 带步长遍历**
`for (<item> in <range> step <n>) { <body> }`
```kotlin
// 带步长遍历
for (i in 1..10 step 2) print("$i ");
```

**基本写法：for 遍历集合**
`for (<item> in <iterable>) { <body> }`
```kotlin
// 遍历集合元素
val items = listOf("apple", "banana", "cherry");
for (item in items) println(item);
```

**基本写法：带索引遍历**
`for ((<index>, <value>) in <collection>.withIndex()) { <body> }`
```kotlin
// 带索引遍历集合
for ((index, value) in items.withIndex()) {
    println("$index: $value");
}
```

**基本写法：遍历 Map**
`for ((<key>, <value>) in <map>) { <body> }`
```kotlin
// 遍历 Map 键值对
val map = mapOf("a" to 1, "b" to 2);
for ((key, value) in map) {
    println("$key = $value");
}
```

**基本写法：while 循环**
`while (<cond>) { <body> }`
```kotlin
// while 循环
var i = 0;
while (i < 5) {
    println(i);
    i++;
}
```

**基本写法：do-while 循环**
`do { <body> } while (<cond>)`
```kotlin
// do-while 循环（至少执行一次）
var input: String;
do {
    input = readLine() ?: "";
} while (input.isEmpty());
```

**基本写法：break 跳出循环**
`break`
```kotlin
// break 跳出循环
for (i in 1..10) {
    if (i == 7) break;
    println(i);
}
```

**基本写法：continue 跳过本次**
`continue`
```kotlin
// continue 跳过当前迭代
for (i in 1..10) {
    if (i == 3) continue;
    println(i);
}
```

**基本写法：标签 break**
`break@<label>`
```kotlin
// 标签 break 跳出外层循环
loop@ for (i in 1..5) {
    for (j in 1..5) {
        if (i * j == 6) break@loop;
        println("$i * $j = ${i * j}");
    }
}
```

---

## 区间与数列

**基本写法：闭区间**
`<start>..<end>`
```kotlin
// 闭区间：包含 end
val range1 = 1..10;
```

**基本写法：字符区间**
`'<char>'..'<char>'`
```kotlin
// 字符区间
val range2 = 'a'..'z';
```

**基本写法：半开区间**
`<start> until <end>`
```kotlin
// 半开区间：不包含 end
val range3 = 1 until 10;
```

**基本写法：递减区间**
`<start> downTo <end>`
```kotlin
// 递减区间
val range4 = 10 downTo 1;
```

**基本写法：带步长区间**
`<range> step <n>`
```kotlin
// 带步长的区间
val range5 = 1..10 step 2;
```

**基本写法：递减带步长区间**
`<start> downTo <end> step <n>`
```kotlin
// 递减且带步长
val range6 = 10 downTo 1 step 3;
```

**基本写法：in 包含检查**
`<value> in <range>`
```kotlin
// 检查值是否在区间内
val range = 1..100;
3 in range;
```

**基本写法：!in 不包含检查**
`<value> !in <range>`
```kotlin
// 检查值是否不在区间内
50 !in range;
```

**基本写法：区间随机数**
`<range>.random()`
```kotlin
// 从区间获取随机数
(1..10).random();
```

**基本写法：区间首尾属性**
`<range>.[first|last]`
```kotlin
// 获取区间首尾元素
(1..10).first;
(1..10).last;
```

**基本写法：数列自定义步长**
`IntProgression.fromClosedRange(<start>, <end>, <step>)`
```kotlin
// 自定义步长的数列
val progression = IntProgression.fromClosedRange(1, 10, 3);
```

**基本写法：区间转列表**
`<range>.toList()`
```kotlin
// 区间转换为列表
val list = (1..10 step 2).toList();
```

---

## 类型检查与转换

**基本写法：is 类型检查**
`if (<obj> is <Type>) { <body> }`
```kotlin
// is 检查后智能转换
if (obj is String) {
    println(obj.length);
}
```

**基本写法：!is 类型检查**
`if (<obj> !is <Type>) { <body> }`
```kotlin
// !is 检查类型不匹配
if (obj !is String) {
    println("Not a String");
}
```

**基本写法：as 不安全类型转换**
`<obj> as <Type>`
```kotlin
// 不安全转换，可能抛出 ClassCastException
val x: Any = "Hello";
val s1: String = x as String;
```

**基本写法：as? 安全类型转换**
`<obj> as? <Type>`
```kotlin
// 安全转换，失败返回 null
val s2: String? = x as? String;
```

---

## Kotlin 2.x 新特性

**基本写法：Kotlin 2.0 K2 编译器前端**
`// 默认启用 K2 编译器`
```kotlin
// Kotlin 2.0 起默认启用 K2 编译器前端
// 无需额外配置，编译速度与稳定性显著提升
// 旧版本手动启用：在 gradle.properties 中设置 kotlin.language.version=2.0
fun main() {
    // K2 编译器对类型推断、内联函数处理更精确
    val list = listOf(1, 2, 3).map { it * 2 }
    println(list)
}
```

**基本写法：Kotlin 2.1 guard 条件 in when**
`when (<x>) { <条件> && guard -> <语句> }`
```kotlin
// when 分支支持 guard 条件，使用 if 关键字附加布尔守卫
fun classify(x: Any): String = when (x) {
    is Int if x > 0 -> "正整数"
    is Int if x < 0 -> "负整数"
    is Int -> "零"
    is String if x.isNotEmpty() -> "非空字符串"
    else -> "其他"
}
// 调用示例
println(classify(42))       // 正整数
println(classify("hello")) // 非空字符串
```

**基本写法：Kotlin 2.1 多重赋值**
`val (<a>, <b>) = <pair>`
```kotlin
// 多重赋值：解构 Pair/Triple 到多个变量
val pair = "Alice" to 30
val (name, age) = pair
println("$name $age") // Alice 30
// 用于函数返回多值场景
fun userInfo(): Pair<String, Int> = "Bob" to 25
val (n, a) = userInfo()
// 也支持 List 解构
val (first, second) = listOf(10, 20)
```

**基本写法：Kotlin 2.2 context receivers**
`context(<receiver>) fun <name>() { }`
```kotlin
// 上下文接收者：声明函数依赖的接收者上下文
class Logger { fun log(msg: String) { println(msg) } }
class Config { val env = "prod" }
// 函数同时依赖 Logger 和 Config 两个上下文
context(Logger, Config)
fun printEnv() {
    log("当前环境: $env")
}
// 调用时需在对应接收者作用域内
with(Logger()) {
    with(Config()) {
        printEnv()
    }
}
```

**基本写法：Kotlin 2.3 Java 25 互操作增强**
`// Kotlin 2.3 增强 Java 25 互操作`
```kotlin
// Kotlin 2.3 改进与 Java 25 新特性的互操作
// 支持 Java 25 模式匹配、记录类、密封类等特性的更优调用
// Java 25 密封类可在 Kotlin 中直接 when 穷尽匹配
sealed interface JShape permits JCircle, JSquare {}
// Kotlin 中无 else 分支也能穷尽匹配
fun area(s: JShape): Double = when (s) {
    is JCircle -> Math.PI * s.r * s.r
    is JSquare -> s.side * s.side
}
```



<!-- ============ 文档分隔线：014-kotlin/004-NullSafetyDetailed.md ============ -->

# Kotlin 空安全详解速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 可空类型声明

**基本写法：非空类型**
`var <name>: <Type> = <value>`
```kotlin
// 非空类型，不能赋 null
var name: String = "Kotlin";
```

**基本写法：可空类型**
`var <name>: <Type>? = <value>`
```kotlin
// 可空类型，允许 null
var nickname: String? = "Kt";
nickname = null;
```

**基本写法：可空集合元素**
`List<<Type>?>`
```kotlin
// 集合元素可为 null
val list: List<String?> = listOf("a", null, "b");
```

**基本写法：可空集合**
`List<<Type>>?`
```kotlin
// 集合本身可为 null
val nullableList: List<String>? = null;
```

**基本写法：可空泛型参数**
`class <Name><T : Any?> { val <prop>: T? }`
```kotlin
// 泛型参数默认可空
class Container<T>(val value: T?);
```

---

## 安全调用操作符

**基本写法：安全调用 ?.**
`<obj>?.<prop>`
```kotlin
// 安全调用，为 null 时返回 null
val length: Int? = nickname?.length;
```

**基本写法：链式安全调用**
`<obj>?.<prop1>?.<prop2>`
```kotlin
// 链式安全调用
val city: String? = user?.address?.city;
```

**基本写法：安全调用方法**
`<obj>?.<method>()`
```kotlin
// 安全调用方法
nickname?.let { println(it); }
```

**基本写法：安全调用集合操作**
`<list>?.<method>()`
```kotlin
// 安全调用集合方法
val size: Int? = list?.size;
```

---

## Elvis 操作符

**基本写法：Elvis 提供默认值**
`<expr> ?: <default>`
```kotlin
// Elvis 运算符提供默认值
val length: Int = nickname?.length ?: 0;
```

**基本写法：Elvis 与 throw**
`<expr> ?: throw <Exception>`
```kotlin
// 为 null 时抛出异常
val value = nullableValue ?: throw IllegalArgumentException("Required value is null");
```

**基本写法：Elvis 与 return**
`<expr> ?: return`
```kotlin
// 为 null 时提前返回
fun process(input: String?) {
    val text = input ?: return;
    println(text);
}
```

**基本写法：Elvis 嵌套**
`<expr1> ?: <expr2> ?: <default>`
```kotlin
// 嵌套 Elvis
val name = primaryName ?: secondaryName ?: "Unknown";
```

---

## 非空断言

**基本写法：非空断言 !!**
`<obj>!!`
```kotlin
// 非空断言，为 null 时抛出 NPE
val length: Int = nickname!!.length;
```

**基本写法：链式非空断言**
`<obj>!!.<prop>!!`
```kotlin
// 链式非空断言（不推荐）
val city: String = user!!.address!!.city!!;
```

---

## 安全类型转换

**基本写法：as? 安全转换**
`<obj> as? <Type>`
```kotlin
// 安全转换，失败返回 null
val number: Int? = value as? Int;
```

**基本写法：as? 与 Elvis 结合**
`(<obj> as? <Type>) ?: <default>`
```kotlin
// 安全转换并提供默认值
val length: Int = (value as? String)?.length ?: 0;
```

---

## let 安全调用

**基本写法：let 安全调用**
`<obj>?.let { <body with it> }`
```kotlin
// let 安全调用非空值
nickname?.let {
    println("Length: ${it.length}");
}
```

**基本写法：let 转换可空值**
`val <name> = <obj>?.let { <transform> }`
```kotlin
// let 转换可空值
val upperName: String? = nickname?.let { it.uppercase() };
```

**基本写法：let 与 Elvis 结合**
`<obj>?.let { <transform> } ?: <default>`
```kotlin
// let 与 Elvis 结合
val length: Int = nickname?.let { it.length } ?: 0;
```

---

## 集合空安全操作

**基本写法：filterNotNull 过滤 null**
`<list>.filterNotNull()`
```kotlin
// 过滤集合中的 null 值
val list: List<String?> = listOf("a", null, "b");
val nonNull: List<String> = list.filterNotNull();
```

**基本写法：mapNotNull 映射并过滤 null**
`<list>.mapNotNull { <transform> }`
```kotlin
// 映射并过滤 null
val lengths: List<Int> = list.mapNotNull { it?.length };
```

**基本写法：firstOrNull 获取第一个非空元素**
`<list>.firstOrNull { <predicate> }`
```kotlin
// 获取第一个满足条件的元素，没有则返回 null
val first = list.firstOrNull { it != null };
```

**基本写法：firstOrNull 获取第一个元素**
`<list>.firstOrNull()`
```kotlin
// 获取第一个元素，空列表返回 null
val first: String? = list.firstOrNull();
```

**基本写法：orEmpty 提供空集合**
`<list>?.orEmpty()`
```kotlin
// 为 null 时返回空集合
val safeList: List<String> = nullableList.orEmpty();
```

**基本写法：orEmpty 提供空字符串**
`<string>?.orEmpty()`
```kotlin
// 为 null 时返回空字符串
val safeString: String = nullableString.orEmpty();
```

---

## 智能转换

**基本写法：null 检查后智能转换**
`if (<obj> != null) { <body with obj as non-null> }`
```kotlin
// null 检查后智能转换为非空
fun greet(name: String?) {
    if (name != null) {
        println(name.length);
    }
}
```

**基本写法：is 检查后智能转换**
`if (<obj> is <Type>) { <body with obj as Type> }`
```kotlin
// is 检查后自动智能转换
if (input is String) {
    println(input.length);
}
```

**基本写法：when 中的智能转换**
`fun <name>(<param>: Any) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// when 中 is 检查后智能转换
fun describe(x: Any) = when (x) {
    is Int -> "Int: ${x + 1}";
    is String -> "String: ${x.length}";
    else -> "Unknown";
}
```

**基本写法：智能转换的限制**
`val <local> = <prop>; if (<local> != null) { <body> }`
```kotlin
// var 属性需使用局部变量避免智能转换限制
val v = value;
if (v != null) {
    println(v.length);
}
```

---

## 平台类型

**基本写法：Java 互操作返回类型**
`val <name> = <JavaObject>.<method>()`
```kotlin
// Java 方法返回类型在 Kotlin 中为平台类型
val name = javaObject.getName();
name.length;  // 可能 NPE
```

**基本写法：显式声明可空类型**
`val <name>: <Type>? = <JavaObject>.<method>()`
```kotlin
// 显式声明为可空类型
val name: String? = javaObject.getName();
name?.length;
```

**基本写法：显式声明非空类型**
`val <name>: <Type> = <JavaObject>.<method>()`
```kotlin
// 显式声明为非空类型（需确保不为 null）
val name: String = javaObject.getName();
```

---

## lateinit 与可空类型

**基本写法：lateinit 延迟初始化**
`lateinit var <name>: <Type>`
```kotlin
// lateinit 延迟初始化
class Service {
    lateinit var repository: Repository;
    fun init() {
        repository = Repository();
    }
}
```

**基本写法：检查 lateinit 是否初始化**
`::<name>.isInitialized`
```kotlin
// 检查 lateinit 属性是否已初始化
if (::repository.isInitialized) {
    repository.query();
}
```

**基本写法：lateinit 与可空类型对比**
`lateinit var <name>: <Type> // vs var <name>: <Type>? = null`
```kotlin
// lateinit 用于非空类型延迟初始化
lateinit var service: Service;  // 不能为 null
// 可空类型用于可能为 null 的场景
var service2: Service? = null;
```

---

## 可空类型扩展函数

**基本写法：为可空类型添加扩展**
`fun <ReceiverType>?.<name>(<params>): <ReturnType>`
```kotlin
// 为可空 String 添加扩展
fun String?.isNullOrBlank(): Boolean = this == null || this.isBlank();
```

**基本写法：可空类型提供默认值**
`fun <ReceiverType>?.<name>(<default>): <ReturnType>`
```kotlin
// 可空类型提供默认值
fun String?.orElse(default: String): String = this ?: default;
```

**基本写法：可空类型安全操作**
`fun <ReceiverType>?.<name>(): <ReturnType>`
```kotlin
// 可空类型安全操作
fun String?.safeLength(): Int = this?.length ?: 0;
```

---

## Contracts（契约）

**基本写法：contract 契约**
`fun <name>(<param>: <Type>?) { contract { returns() implies (<param> != null) } }`
```kotlin
// contract 契约帮助编译器进行智能转换
fun requireNotNull(value: String?) {
    contract { returns() implies (value != null) }
    if (value == null) throw IllegalArgumentException();
}
```

**基本写法：自定义契约函数**
`fun <name>(<param>: <Type>?): Boolean { contract { returns(true) implies (<param> != null) } }`
```kotlin
// 自定义契约函数
fun isValid(value: String?): Boolean {
    contract { returns(true) implies (value != null) }
    return value != null && value.length > 0;
}
```

---

## 空安全最佳实践

**基本写法：优先使用安全调用**
`<obj>?.<method>()`
```kotlin
// 优先使用安全调用而非非空断言
val length = nickname?.length;
```

**基本写法：使用 Elvis 提供默认值**
`<expr> ?: <default>`
```kotlin
// 使用 Elvis 提供默认值
val name = nickname ?: "Unknown";
```

**基本写法：使用 require 检查非空**
`require(<obj> != null) { <message> }`
```kotlin
// 使用 require 检查非空
fun process(input: String?) {
    require(input != null) { "Input cannot be null" };
    println(input.length);
}
```

**基本写法：使用 check 检查状态**
`check(<obj> != null) { <message> }`
```kotlin
// 使用 check 检查状态
fun process() {
    check(state != null) { "State must be initialized" };
    state.execute();
}
```



<!-- ============ 文档分隔线：014-kotlin/005-ExtensionFunction.md ============ -->

# Kotlin 扩展函数速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 扩展函数基础

**基本写法：为 String 添加扩展函数**
`fun String.<name>(): <ReturnType>`
```kotlin
// 为 String 添加扩展函数
fun String.addExclamation(): String = this + "!";
```

**基本写法：为 Int 添加扩展函数**
`fun Int.<name>(): <ReturnType>`
```kotlin
// 为 Int 添加扩展函数
fun Int.isEven(): Boolean = this % 2 == 0;
```

**换行写法：带逻辑的扩展函数**
`fun <ReceiverType>.<name>(<params>): <ReturnType> { <body> }`
```kotlin
// 为 List 添加带逻辑的扩展函数
fun <T> List<T>.second(): T {
    if (this.size < 2) throw NoSuchElementException("列表没有第二个元素");
    return this[1];
}
```

**基本写法：为可空类型添加扩展函数**
`fun <ReceiverType>?.<name>(<params>): <ReturnType>`
```kotlin
// 为可空类型添加扩展函数
fun String?.isNullOrBlank(): Boolean = this == null || this.isBlank();
```

---

## 扩展属性

**基本写法：只读扩展属性**
`val <ReceiverType>.<name>: <Type> get() = <expr>`
```kotlin
// 为 String 添加只读扩展属性
val String.firstChar: Char
    get() = this.first();
```

**基本写法：Boolean 扩展属性**
`val <ReceiverType>.<name>: Boolean get() = <expr>`
```kotlin
// 为 String 添加 Boolean 扩展属性
val String.hasContent: Boolean
    get() = this.isNotBlank();
```

**换行写法：可变扩展属性**
`var <ReceiverType>.<name>: <Type> [get() = <expr>] [set(value) { <body> }]`
```kotlin
// 为 StringBuilder 添加可变扩展属性
var StringBuilder.lastChar: Char
    get() = this[this.length - 1]
    set(value) { this.append(value); }
```

---

## 扩展函数与可空类型

**基本写法：为非空类型添加扩展**
`fun <ReceiverType>.<name>(<params>): <ReturnType>`
```kotlin
// 为非空 String 添加扩展
fun String.trimToLength(maxLength: Int): String {
    return if (this.length <= maxLength) this
    else this.substring(0, maxLength) + "...";
}
```

**基本写法：为可空类型添加扩展**
`fun <ReceiverType>?.<name>(<params>): <ReturnType>`
```kotlin
// 为可空 String 添加扩展
fun String?.safeLength(): Int = this?.length ?: 0;
```

**基本写法：可空类型提供默认值**
`fun <ReceiverType>?.<name>(<default>): <ReturnType>`
```kotlin
// 可空类型提供默认值
fun String?.orElse(default: String): String = this ?: default;
```

---

## 扩展函数中的 this

**基本写法：this 引用接收者对象**
`fun <ReceiverType>.<name>(): <ReturnType>`
```kotlin
// this 指向接收者对象
fun String.describe(): String {
    return "字符串 '$this' 的长度是 ${this.length}";
}
```

**基本写法：省略 this**
`fun <ReceiverType>.<name>(): <ReturnType>`
```kotlin
// 省略 this 调用方法
fun String.shout(): String = uppercase() + "!!!";
```

---

## 泛型扩展函数

**基本写法：为任意类型添加扩展**
`fun <T> T.<name>(): <ReturnType>`
```kotlin
// 为任意类型添加扩展
fun <T> T.printSelf(): T {
    println(this);
    return this;
}
```

**基本写法：带约束的泛型扩展**
`fun <T : <Bound>> T.<name>(<params>): <ReturnType>`
```kotlin
// 带约束的泛型扩展
fun <T : Comparable<T>> T.isBetween(min: T, max: T): Boolean {
    return this >= min && this <= max;
}
```

**换行写法：为集合添加泛型扩展**
`fun <T> List<T>.<name>(<param>: List<T>): <ReturnType>`
```kotlin
// 为 List 添加泛型扩展
fun <T> List<T>.interleave(other: List<T>): List<T> {
    val result = mutableListOf<T>();
    val maxSize = maxOf(this.size, other.size);
    for (i in 0 until maxSize) {
        if (i < this.size) result.add(this[i]);
        if (i < other.size) result.add(other[i]);
    }
    return result;
}
```

---

## 扩展函数的解析规则

**基本写法：静态解析**
`fun <BaseType>.<name>() = <expr>`
```kotlin
// 扩展函数静态解析，由声明类型决定
open class Animal;
class Dog : Animal();
fun Animal.sound() = "动物叫声";
fun Dog.sound() = "汪汪汪";
val animal: Animal = Dog();
animal.sound();  // 动物叫声（调用 Animal 的扩展）
```

---

## 扩展函数的作用域

**基本写法：顶层扩展函数**
`package <pkg>; fun <ReceiverType>.<name>(): <ReturnType>`
```kotlin
// 顶层扩展函数，使用时需要 import
package com.example.utils;
fun String.isEmail(): Boolean = this.contains("@") && this.contains(".");
```

**基本写法：成员扩展函数**
`class <Name> { fun <ReceiverType>.<name>(): <ReturnType> }`
```kotlin
// 成员扩展函数，只在类内部可用
class Parser {
    private fun String.parseToInt(): Int? = this.toIntOrNull();
    fun parse(input: String): Int? {
        return input.parseToInt();
    }
}
```

---

## 工具函数扩展

**基本写法：日期格式化扩展**
`fun <Type>.<name>(): <ReturnType>`
```kotlin
// 为 LocalDateTime 添加格式化扩展
fun java.time.LocalDateTime.formatChinese(): String {
    return "${this.year}年${this.monthValue}月${this.dayOfMonth}日";
}
```

**基本写法：集合随机元素扩展**
`fun <T> List<T>.<name>(): <ReturnType>`
```kotlin
// 为 List 添加随机元素扩展
fun <T> List<T>.randomItemOrNull(): T? = if (this.isEmpty()) null else this.random();
```

**基本写法：数值四舍五入扩展**
`fun <Number>.<name>(<params>): <ReturnType>`
```kotlin
// 为 Double 添加四舍五入扩展
fun Double.roundTo(decimals: Int): Double {
    var multiplier = 1.0;
    repeat(decimals) { multiplier *= 10 };
    return kotlin.math.round(this * multiplier) / multiplier;
}
```

---

## 防御性编程扩展

**基本写法：安全的类型转换扩展**
`inline fun <reified T> Any.safeCast(): T?`
```kotlin
// 安全的类型转换扩展
inline fun <reified T> Any.safeCast(): T? = this as? T;
```

**基本写法：安全的列表访问扩展**
`fun <T> List<T>.safeGet(<index>: Int): T?`
```kotlin
// 安全的列表访问扩展
fun <T> List<T>.safeGet(index: Int): T? {
    return if (index in indices) this[index] else null;
}
```

**基本写法：非空检查扩展**
`fun <T : Any> T?.requireNonNull(<lazyMessage>): T`
```kotlin
// 非空检查扩展
fun <T : Any> T?.requireNonNull(lazyMessage: () -> String = { "值不能为空" }): T {
    return this ?: throw IllegalArgumentException(lazyMessage());
}
```

---

## 流式 API 扩展

**基本写法：applyIf 条件执行扩展**
`fun <T> T.<name>(<condition>, <block>): T`
```kotlin
// 条件执行扩展
fun <T> T.applyIf(condition: Boolean, block: T.() -> Unit): T {
    if (condition) block();
    return this;
}
```

**基本写法：alsoIf 条件执行扩展**
`fun <T> T.<name>(<condition>, <block>): T`
```kotlin
// 条件执行扩展
fun <T> T.alsoIf(condition: Boolean, block: (T) -> Unit): T {
    if (condition) block(this);
    return this;
}
```

---

## 中缀扩展函数

**基本写法：infix 扩展函数**
`infix fun <ReceiverType>.<name>(<param>): <ReturnType>`
```kotlin
// 中缀扩展函数
infix fun String.times(n: Int): String {
    return this.repeat(n);
}
```

**基本写法：infix 集合扩展函数**
`infix fun <T> List<T>.<name>(<param>): <ReturnType>`
```kotlin
// 中缀集合扩展函数
infix fun <T> List<T>.intersect(other: List<T>): List<T> {
    return this.filter { it in other };
}
```

---

## 扩展函数与运算符重载

**基本写法：operator 扩展函数**
`operator fun <ReceiverType>.<name>(<params>): <ReturnType>`
```kotlin
// operator 重载 step 运算符
operator fun ClosedRange<Int>.step(step: Int): Iterable<Int> {
    return object : Iterable<Int> {
        override fun iterator(): Iterator<Int> {
            var current = start;
            return object : Iterator<Int> {
                override fun hasNext() = current <= endInclusive;
                override fun next(): Int {
                    val result = current;
                    current += step;
                    return result;
                }
            };
        }
    };
}
```

---

## 带接收者的函数类型

**基本写法：带接收者的函数类型**
`fun <name>(<param>: <ReceiverType>.() -> <ReturnType>): <ReturnType>`
```kotlin
// 带接收者的函数类型
fun buildString(builderAction: StringBuilder.() -> Unit): String {
    val builder = StringBuilder();
    builder.builderAction();
    return builder.toString();
}
```



<!-- ============ 文档分隔线：014-kotlin/006-KotlinClassObject.md ============ -->

# Kotlin 类与对象速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类定义

**基本写法：基本类定义**
`class <Name> { <body> }`
```kotlin
// 基本类定义
class Person {
    var name: String = "";
    var age: Int = 0;
}
```

**基本写法：可变属性与自定义 getter**
`var <name>: <Type> = <init> get() = <expr>`
```kotlin
// 可变属性自定义 getter
class User {
    var name: String = "Unknown"
        get() = field.uppercase();
}
```

**基本写法：可变属性与自定义 setter**
`var <name>: <Type> = <init> set(value) { field = <expr> }`
```kotlin
// 可变属性自定义 setter
class User {
    var name: String = "Unknown"
        set(value) { field = value.trim(); }
}
```

**基本写法：只读属性**
`val <name>: <Type> = <init>`
```kotlin
// 只读属性
class User {
    val createdAt: Long = System.currentTimeMillis();
}
```

**基本写法：幕后字段**
`set(value) { field = <expr> }`
```kotlin
// field 引用幕后字段，避免递归调用 setter
class Temperature {
    var celsius: Double = 0.0
        set(value) {
            field = value;
        }
}
```

**基本写法：lateinit 延迟初始化属性**
`lateinit var <name>: <Type>`
```kotlin
// lateinit 延迟初始化
class Service {
    lateinit var repository: Repository;
    fun init() {
        repository = Repository();
    }
}
```

**基本写法：检查 lateinit 是否初始化**
`::<name>.isInitialized`
```kotlin
// 检查 lateinit 属性是否已初始化
if (::repository.isInitialized) {
    repository.query();
}
```

---

## 构造函数

**单行写法：主构造函数**
`class <Name>(val <prop>: <Type>, val <prop2>: <Type>)`
```kotlin
// 单行主构造函数声明属性
class Person(val name: String, val age: Int);
```

**单行写法：constructor 关键字主构造函数**
`class <Name> constructor(val <prop>: <Type>)`
```kotlin
// 显式 constructor 关键字
class Person constructor(val name: String, val age: Int);
```

**换行写法：多参数主构造函数**
`class <Name>(val <prop1>: <Type>, val <prop2>: <Type>, val <prop3>: <Type>)`
```kotlin
// 换行声明多参数主构造函数
class Person(
    val name: String,
    val age: Int,
    val email: String
);
```

**基本写法：init 块**
`init { <body> }`
```kotlin
// init 块执行初始化逻辑
class Person(val name: String, val age: Int) {
    init {
        require(age >= 0) { "Age cannot be negative" };
    }
}
```

**基本写法：次构造函数**
`constructor(<params>) : this(<args>)`
```kotlin
// 次构造函数委托给主构造函数
class Person(val name: String, val age: Int) {
    constructor(name: String) : this(name, 0);
}
```

**基本写法：私有主构造函数**
`class <Name> private constructor() { <body> }`
```kotlin
// 私有主构造函数实现单例
class Singleton private constructor() {
    companion object {
        val instance: Singleton by lazy { Singleton(); }
    }
}
```

---

## 继承

**基本写法：open 类继承**
`open class <Name>(<params>) { open fun <name>(): <ReturnType> }`
```kotlin
// open 修饰类允许继承
open class Animal(val name: String) {
    open fun sound() = "Some sound";
}
```

**基本写法：子类继承**
`class <SubName>(<params>) : <BaseName>(<args>) { override fun <name>(): <ReturnType> }`
```kotlin
// 子类重写方法
class Dog(name: String) : Animal(name) {
    override fun sound() = "Woof";
}
```

**基本写法：属性重写**
`override val <name>: <Type> = <value>`
```kotlin
// 重写父类属性
open class Base {
    open val value: Int = 0;
}
class Derived : Base() {
    override val value: Int = 42;
}
```

**基本写法：主构造函数属性重写**
`class <SubName>(override val <prop>: <Type>) : <BaseName>()`
```kotlin
// 主构造函数中重写属性
class Derived2(override val value: Int) : Base();
```

**基本写法：调用父类实现**
`super.<method>()`
```kotlin
// 调用父类方法
class Button : View() {
    override fun draw() {
        super.draw();
        println("Drawing button");
    }
}
```

---

## 抽象类

**基本写法：抽象类定义**
`abstract class <Name> { abstract fun <name>(): <ReturnType> }`
```kotlin
// 抽象类定义抽象方法
abstract class Shape {
    abstract fun perimeter(): Double;
}
```

**基本写法：抽象属性**
`abstract class <Name> { abstract val <prop>: <Type> }`
```kotlin
// 抽象类定义抽象属性
abstract class Shape {
    abstract val area: Double;
}
```

**基本写法：抽象类实现**
`class <SubName>(<params>) : <BaseName>() { override val <prop>: <Type> = <value> }`
```kotlin
// 实现抽象类
class Circle(val radius: Double) : Shape() {
    override val area: Double = Math.PI * radius * radius;
    override fun perimeter(): Double = 2 * Math.PI * radius;
}
```

---

## 接口

**基本写法：接口定义**
`interface <Name> { fun <method>(<params>): <ReturnType> }`
```kotlin
// 接口定义抽象方法
interface Clickable {
    fun click();
}
```

**基本写法：接口默认实现**
`interface <Name> { fun <method>(): <ReturnType> = <expr> }`
```kotlin
// 接口方法默认实现
interface Clickable {
    fun showOff() = "Clickable!";
}
```

**换行写法：实现多个接口**
`class <Name> : <Interface1>, <Interface2> { override fun <method> }`
```kotlin
// 实现多个接口并解决冲突
class Button : Clickable, Focusable {
    override fun click() = println("Button clicked");
    override fun showOff(): String {
        return super<Clickable>.showOff() + " & " + super<Focusable>.showOff();
    }
}
```

**基本写法：接口中的属性**
`interface <Name> { val <prop>: <Type> }`
```kotlin
// 接口定义抽象属性
interface Config {
    val host: String;
    val port: Int;
}
```

**基本写法：接口属性默认 getter**
`interface <Name> { val <prop>: <Type> get() = <expr> }`
```kotlin
// 接口属性提供默认 getter
interface Config {
    val url: String
        get() = "$host:$port";
}
```

---

## 数据类

**单行写法：data class**
`data class <Name>(val <prop>: <Type>, val <prop2>: <Type>)`
```kotlin
// 单行数据类
data class User(val name: String, val age: Int);
```

**换行写法：多参数 data class**
`data class <Name>(val <prop1>: <Type>, val <prop2>: <Type>, val <prop3>: <Type>)`
```kotlin
// 换行声明多参数数据类
data class User(
    val name: String,
    val age: Int,
    val email: String
);
```

**基本写法：copy 复制并修改**
`<obj>.copy(<prop> = <value>)`
```kotlin
// copy 创建副本并修改部分属性
val user3 = user1.copy(age = 26);
```

**基本写法：解构声明**
`val (<a>, <b>, <c>) = <obj>`
```kotlin
// 解构声明提取属性
val (name, age, email) = user1;
```

---

## 密封类

**基本写法：密封类定义**
`sealed class <Name> { <subclasses> }`
```kotlin
// 密封类定义子类
sealed class Result<out T> {
    data class Success<T>(val value: T) : Result<T>();
    object Loading : Result<Nothing>();
}
```

**基本写法：when 穷举密封类**
`fun <name>(<param>: <SealedClass>) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// when 穷举所有子类，无需 else
fun handle(result: Result<Int>) = when (result) {
    is Result.Success -> println("Success: ${result.value}");
    Result.Loading -> println("Loading...");
}
```

**基本写法：密封接口定义**
`sealed interface <Name>`
```kotlin
// 密封接口定义
sealed interface Action {
    data class Click(val x: Int, val y: Int) : Action;
    object Idle : Action;
}
```

**基本写法：密封接口组合**
`sealed interface <Name> : <Other>`
```kotlin
// 密封接口继承其他密封接口
sealed interface Drawable {
    fun draw();
}
```

---

## 枚举类

**单行写法：枚举定义**
`enum class <Name> { <VALUES> }`
```kotlin
// 单行枚举定义
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```

**换行写法：带属性的枚举**
`enum class <Name>(val <prop>: <Type>) { <VALUE>(<args>), ... }`
```kotlin
// 换行声明带属性的枚举
enum class Planet(val mass: Double, val radius: Double) {
    EARTH(5.97e24, 6371.0),
    MARS(6.42e23, 3390.0),
    JUPITER(1.90e27, 69911.0)
}
```

**基本写法：枚举实现接口**
`enum class <Name> : <Interface> { <VALUE> { override fun <method>() } }`
```kotlin
// 枚举实现接口
enum class Format : Runnable {
    JSON {
        override fun run() = println("Formatting as JSON");
    }
}
```

**基本写法：枚举 values 获取所有值**
`<EnumClass>.values()`
```kotlin
// 获取所有枚举值
Direction.values();
```

**基本写法：枚举 valueOf 根据名称获取**
`<EnumClass>.valueOf("<name>")`
```kotlin
// 根据名称获取枚举值
Direction.valueOf("NORTH");
```

**基本写法：枚举 name 属性**
`<EnumValue>.name`
```kotlin
// 获取枚举值名称
Direction.NORTH.name;
```

**基本写法：枚举 ordinal 属性**
`<EnumValue>.ordinal`
```kotlin
// 获取枚举值序号
Direction.NORTH.ordinal;
```

---

## 伴生对象

**基本写法：companion object**
`class <Name> { companion object { <members> } }`
```kotlin
// 伴生对象定义静态成员
class MyClass {
    companion object {
        const val CONSTANT = "Hello";
        fun create(): MyClass = MyClass();
    }
}
```

**基本写法：伴生对象实现接口**
`companion object : <Interface> { override fun <method>(): <ReturnType> }`
```kotlin
// 伴生对象实现工厂接口
class Product(val name: String) {
    companion object : Factory<Product> {
        override fun create(): Product = Product("Default");
    }
}
```

**基本写法：伴生对象扩展**
`fun <Class>.Companion.<name>(<params>): <ReturnType>`
```kotlin
// 为伴生对象添加扩展函数
fun Product.Companion.fromJson(json: String): Product {
    return Product(json);
}
```

---

## 对象表达式与声明

**基本写法：对象表达式**
`object : <Class>(), <Interface> { <overrides> }`
```kotlin
// 对象表达式替代匿名内部类
window.addMouseListener(object : MouseAdapter() {
    override fun mouseClicked(e: MouseEvent) {
        println("Clicked at ${e.point}");
    }
})
```

**基本写法：简单对象表达式**
`val <name> = object { <members> }`
```kotlin
// 无继承的简单对象表达式
val config = object {
    val host = "localhost";
    val port = 8080;
}
```

**基本写法：对象声明（单例）**
`object <Name> { <body> }`
```kotlin
// 对象声明实现单例
object Database {
    fun getSchema(name: String): String? = tables[name];
}
```

**基本写法：嵌套对象**
`class <Outer> { object <Nested> { <body> } }`
```kotlin
// 嵌套对象（静态内部类）
class Outer {
    object Nested {
        fun greet() = "Hello from Nested";
    }
}
```

**基本写法：内部类**
`class <Outer> { inner class <Inner> { <body> } }`
```kotlin
// inner class 内部类（持有外部类引用）
class Outer {
    inner class Inner {
        fun greet() = "Hello from Inner";
    }
}
```

---

## 委托

**基本写法：类委托**
`class <Name>(<val delegate>: <Interface>) : <Interface> by <delegate>`
```kotlin
// 类委托实现装饰器模式
class LoggingRepository(private val repo: Repository) : Repository by repo {
    override fun findAll(): List<String> {
        println("Finding all items...");
        return repo.findAll();
    }
}
```

**基本写法：observable 属性委托**
`var <name>: <Type> by Delegates.observable(<init>) { _, old, new -> <body> }`
```kotlin
// observable 属性变化时回调
class Config {
    var name: String by Delegates.observable("initial") { _, old, new ->
        println("Name changed from $old to $new");
    }
}
```

**基本写法：vetoable 属性委托**
`var <name>: <Type> by Delegates.vetoable(<init>) { _, _, new -> <cond> }`
```kotlin
// vetoable 可否决属性变化
class Config {
    var age: Int by Delegates.vetoable(0) { _, _, new ->
        new >= 0;
    }
}
```

**基本写法：lazy 属性委托**
`val <name>: <Type> by lazy { <init> }`
```kotlin
// lazy 延迟初始化
class Config {
    val heavyData: List<String> by lazy {
        (1..1000).map { "Item $it" };
    }
}
```

**换行写法：自定义属性委托**
`class <Delegate><T> { operator fun getValue(...) / setValue(...) }`
```kotlin
// 自定义属性委托实现
class Preference<T>(private val key: String, private val default: T) {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T {
        return prefs[key] as? T ?: default;
    }
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        prefs[key] = value;
    }
}
```



<!-- ============ 文档分隔线：014-kotlin/007-SealedClassSealedInterface.md ============ -->

# Kotlin 密封类与密封接口速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 密封类基础

**基本写法：密封类定义**
`sealed class <Name>`
```kotlin
// 密封类定义，子类必须在同一文件或同一包
sealed class Result;
```

**基本写法：密封类带泛型**
`sealed class <Name><T>`
```kotlin
// 带泛型的密封类
sealed class Result<out T>;
```

**基本写法：密封类带抽象成员**
`sealed class <Name> { abstract fun <method>(): <ReturnType> }`
```kotlin
// 密封类定义抽象成员
sealed class Shape {
    abstract fun area(): Double;
}
```

---

## 密封类子类

**基本写法：data class 子类**
`data class <SubName>(val <prop>: <Type>) : <SealedClass>()`
```kotlin
// data class 作为密封类子类
data class Success(val value: Int) : Result<Int>();
```

**基本写法：object 子类**
`object <SubName> : <SealedClass>()`
```kotlin
// object 作为密封类子类
object Loading : Result<Nothing>();
```

**基本写法：普通 class 子类**
`class <SubName>(<params>) : <SealedClass>()`
```kotlin
// 普通 class 作为密封类子类
class Error(val message: String) : Result<Nothing>();
```

**单行写法：多子类密封类**
`sealed class <Name> { data class <A>(...); object <B>; class <C>(...) }`
```kotlin
// 单行定义多个子类
sealed class Result {
    data class Success<T>(val value: T) : Result<T>();
    object Loading : Result<Nothing>();
    class Error(val message: String) : Result<Nothing>();
}
```

**换行写法：多子类密封类**
`sealed class <Name> { <subclasses on separate lines> }`
```kotlin
// 换行定义多个子类
sealed class Result<out T> {
    data class Success<T>(val value: T) : Result<T>();
    object Loading : Result<Nothing>();
    data class Error(val message: String) : Result<Nothing>();
}
```

---

## 嵌套密封类子类

**基本写法：嵌套子类**
`sealed class <Name> { class <SubName> : <Name>() }`
```kotlin
// 嵌套子类定义
sealed class State {
    class Loading : State();
    class Loaded(val data: String) : State();
    class Error(val message: String) : State();
}
```

**基本写法：object 嵌套子类**
`sealed class <Name> { object <SubName> : <Name>() }`
```kotlin
// object 嵌套子类
sealed class Permission {
    object Granted : Permission();
    object Denied : Permission();
}
```

---

## when 表达式穷举

**基本写法：when 穷举密封类**
`fun <name>(<param>: <SealedClass>) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// when 穷举所有子类，无需 else
fun handleResult(result: Result<Int>): String = when (result) {
    is Result.Success -> "成功: ${result.value}";
    Result.Loading -> "加载中";
    is Result.Error -> "错误: ${result.message}";
}
```

**基本写法：when 穷举 object 子类**
`fun <name>(<param>: <SealedClass>) = when (<param>) { <ObjectName> -> <expr> }`
```kotlin
// when 中直接匹配 object（无需 is）
fun checkPermission(permission: Permission): String = when (permission) {
    Permission.Granted -> "已授权";
    Permission.Denied -> "已拒绝";
}
```

**基本写法：when 穷举带返回值**
`val <name> = when (<param>) { <branches> }`
```kotlin
// when 表达式返回值
val stateText: String = when (state) {
    is State.Loading -> "正在加载";
    is State.Loaded -> "已加载: ${state.data}";
    is State.Error -> "错误: ${state.message}";
}
```

---

## 密封接口

**基本写法：密封接口定义**
`sealed interface <Name>`
```kotlin
// 密封接口定义
sealed interface Action;
```

**基本写法：密封接口带泛型**
`sealed interface <Name><T>`
```kotlin
// 带泛型的密封接口
sealed interface Event<out T>;
```

**基本写法：密封接口带方法**
`sealed interface <Name> { fun <method>(): <ReturnType> }`
```kotlin
// 密封接口定义方法
sealed interface Drawable {
    fun draw(): String;
}
```

---

## 密封接口实现

**基本写法：data class 实现密封接口**
`data class <Name>(val <prop>: <Type>) : <SealedInterface>`
```kotlin
// data class 实现密封接口
data class Click(val x: Int, val y: Int) : Action;
```

**基本写法：object 实现密封接口**
`object <Name> : <SealedInterface>`
```kotlin
// object 实现密封接口
object Idle : Action;
```

**基本写法：class 实现密封接口**
`class <Name>(<params>) : <SealedInterface>`
```kotlin
// 普通 class 实现密封接口
class Scroll(val delta: Int) : Action;
```

**换行写法：多实现密封接口**
`sealed interface <Name> { <implementations on separate lines> }`
```kotlin
// 换行定义多个实现
sealed interface Action {
    data class Click(val x: Int, val y: Int) : Action;
    data class LongPress(val duration: Long) : Action;
    object Idle : Action;
}
```

---

## 密封接口组合

**基本写法：密封接口继承**
`sealed interface <Name> : <Other>`
```kotlin
// 密封接口继承其他接口
sealed interface Clickable : Drawable {
    fun click();
}
```

**基本写法：密封接口多重继承**
`sealed interface <Name> : <Interface1>, <Interface2>`
```kotlin
// 密封接口多重继承
sealed interface UIEvent : Clickable, Focusable;
```

**基本写法：类实现多个密封接口**
`class <Name> : <SealedInterface1>, <SealedInterface2>`
```kotlin
// 类实现多个密封接口
class Button : Clickable, Focusable {
    override fun draw() = "Drawing button";
    override fun click() = println("Clicked");
}
```

---

## 密封类与密封接口结合

**基本写法：密封类实现密封接口**
`sealed class <Name> : <SealedInterface>`
```kotlin
// 密封类实现密封接口
sealed class UIComponent : Drawable {
    data class Button(val text: String) : UIComponent() {
        override fun draw() = "Button: $text";
    }
    data class TextField(val text: String) : UIComponent() {
        override fun draw() = "TextField: $text";
    }
}
```

**基本写法：when 穷举密封类与密封接口**
`fun <name>(<param>: <SealedClass>) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// when 穷举密封类实现
fun render(component: UIComponent): String = when (component) {
    is UIComponent.Button -> component.draw();
    is UIComponent.TextField -> component.draw();
}
```

---

## 密封类递归类型

**基本写法：递归密封类**
`sealed class <Name><T> { data class <SubName><T>(val <prop>: <Name><T>) : <Name><T>() }`
```kotlin
// 递归密封类（链表结构）
sealed class List<out T> {
    object Nil : List<Nothing>();
    data class Cons<T>(val head: T, val tail: List<T>) : List<T>();
}
```

**基本写法：递归 when 处理**
`fun <name>(<param>: <SealedClass>): <ReturnType> = when (<param>) { is <Type> -> <expr> }`
```kotlin
// 递归处理密封类
fun <T> sum(list: List<T>): Int where T : Number = when (list) {
    List.Nil -> 0;
    is List.Cons -> list.head.toInt() + sum(list.tail);
}
```

---

## 密封类实战

**基本写法：状态机密封类**
`sealed class <State> { <subclasses> }`
```kotlin
// 状态机密封类
sealed class ViewState {
    object Loading : ViewState();
    data class Success(val data: List<String>) : ViewState();
    data class Error(val message: String, val retry: () -> Unit) : ViewState();
}
```

**基本写法：状态机 when 处理**
`fun <name>(<param>: <State>) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// 状态机 when 处理
fun renderView(state: ViewState): String = when (state) {
    ViewState.Loading -> "显示加载动画";
    is ViewState.Success -> "显示数据: ${state.data}";
    is ViewState.Error -> "显示错误: ${state.message}";
}
```

**基本写法：网络请求结果密封类**
`sealed class <Result><T> { <subclasses> }`
```kotlin
// 网络请求结果密封类
sealed class NetworkResult<out T> {
    data class Success<T>(val data: T) : NetworkResult<T>();
    data class Failure(val error: Throwable) : NetworkResult<Nothing>();
    object NetworkError : NetworkResult<Nothing>();
}
```

**基本写法：网络请求结果处理**
`fun <name>(<param>: <NetworkResult>) = when (<param>) { is <Type> -> <expr> }`
```kotlin
// 网络请求结果处理
fun <T> handleResult(result: NetworkResult<T>): String = when (result) {
    is NetworkResult.Success -> "成功: ${result.data}";
    is NetworkResult.Failure -> "失败: ${result.error.message}";
    NetworkResult.NetworkError -> "网络错误";
}
```



<!-- ============ 文档分隔线：014-kotlin/008-DelegateProperty.md ============ -->

# Kotlin 委托属性速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 标准委托

**基本写法：lazy 延迟初始化**
`val <name>: <Type> by lazy { <init> }`
```kotlin
// lazy 首次访问时初始化
val database: Database by lazy { Database.connect("localhost"); }
```

**基本写法：lazy 同步模式**
`val <name>: <Type> by lazy(LazyThreadSafetyMode.<mode>) { <init> }`
```kotlin
// 指定 lazy 的线程安全模式
val cache: Map<String, String> by lazy(LazyThreadSafetyMode.PUBLICATION) {
    loadCache();
}
```

**基本写法：observable 属性变化监听**
`var <name>: <Type> by Delegates.observable(<init>) { <prop>, <old>, <new> -> <body> }`
```kotlin
// observable 属性变化时回调
var name: String by Delegates.observable("initial") { prop, old, new ->
    println("${prop.name} changed from $old to $new");
}
```

**基本写法：vetoable 可否决属性变化**
`var <name>: <Type> by Delegates.vetoable(<init>) { <prop>, <old>, <new> -> <cond> }`
```kotlin
// vetoable 返回 false 时拒绝修改
var age: Int by Delegates.vetoable(0) { _, _, new -> new >= 0 };
```

**基本写法：.notNull 非空委托**
`var <name>: <Type> by Delegates.notNull()`
```kotlin
// notNull 委托，未初始化前访问抛出异常
var config: Config by Delegates.notNull();
fun init() {
    config = Config.load();
}
```

---

## Map 委托

**基本写法：只读 Map 委托**
`val <name>: <Type> by <map>`
```kotlin
// 从只读 Map 中读取属性
val map = mapOf("name" to "Alice", "age" to 25);
val name: String by map;
val age: Int by map;
```

**基本写法：可变 Map 委托**
`var <name>: <Type> by <mutableMap>`
```kotlin
// 从可变 Map 中读写属性
val mutableMap = mutableMapOf("name" to "Alice");
var name: String by mutableMap;
name = "Bob";  // 修改会同步到 map
```

---

## 自定义属性委托

**基本写法：只读属性委托**
`class <Delegate><T> { operator fun getValue(thisRef: Any?, property: KProperty<*>): T }`
```kotlin
// 只读属性委托实现
class StringDelegate(private val value: String) {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): String {
        return "[$property] = $value";
    }
}
val greeting by StringDelegate("Hello");
```

**换行写法：可读写属性委托**
`class <Delegate><T> { operator fun getValue(...); operator fun setValue(...) }`
```kotlin
// 可读写属性委托实现
class Preference<T>(private val key: String, private val default: T) {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T {
        return preferences.get(key) as? T ?: default;
    }
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        preferences.put(key, value);
    }
}
```

**基本写法：ReadOnlyProperty 接口实现**
`class <Delegate><T> : ReadOnlyProperty<Any?, T> { override fun getValue(...): T }`
```kotlin
// 实现 ReadOnlyProperty 接口
class ConstProperty<T>(private val value: T) : ReadOnlyProperty<Any?, T> {
    override fun getValue(thisRef: Any?, property: KProperty<*>): T = value;
}
```

**基本写法：ReadWriteProperty 接口实现**
`class <Delegate><T> : ReadWriteProperty<Any?, T> { override fun getValue(...); override fun setValue(...) }`
```kotlin
// 实现 ReadWriteProperty 接口
class LoggingProperty<T>(private var value: T) : ReadWriteProperty<Any?, T> {
    override fun getValue(thisRef: Any?, property: KProperty<*>): T {
        println("Getting ${property.name}");
        return value;
    }
    override fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        println("Setting ${property.name} to $value");
        this.value = value;
    }
}
```

---

## 委托提供者

**基本写法：提供委托（provideDelegate）**
`operator fun <name>.provideDelegate(thisRef: Any?, property: KProperty<*>): <Delegate>`
```kotlin
// provideDelegate 在属性初始化时拦截
class ConfigDelegate<T>(private val default: T) {
    operator fun provideDelegate(thisRef: Any?, property: KProperty<*>): ReadWriteProperty<Any?, T> {
        return Preference(property.name, default);
    }
}
```

**基本写法：使用提供委托**
`val <name>: <Type> by <DelegateProvider>(<default>)`
```kotlin
// 使用提供委托
val host: String by ConfigDelegate("localhost");
val port: Int by ConfigDelegate(8080);
```

---

## 局部委托属性

**基本写法：局部变量 lazy 委托**
`val <name> by lazy { <init> }`
```kotlin
// 局部变量使用 lazy 委托
fun process(input: String) {
    val parsed by lazy { parseInput(input); }
    if (shouldProcess) {
        println(parsed);
    }
}
```

**基本写法：局部变量自定义委托**
`val <name> by <delegate>`
```kotlin
// 局部变量使用自定义委托
fun example() {
    val value by LoggingProperty("initial");
    println(value);
}
```

---

## 委托属性实战

**基本写法：SharedPreferences 委托**
`val <name>: <Type> by <Preference>(<key>, <default>)`
```kotlin
// SharedPreferences 委托
class Preference<T>(private val key: String, private val default: T) {
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T {
        val prefs = context.getSharedPreferences("app", Context.MODE_PRIVATE);
        return when (default) {
            is String -> prefs.getString(key, default) as T;
            is Int -> prefs.getInt(key, default) as T;
            is Boolean -> prefs.getBoolean(key, default) as T;
            else -> default;
        }
    }
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        val prefs = context.getSharedPreferences("app", Context.MODE_PRIVATE);
        val editor = prefs.edit();
        when (value) {
            is String -> editor.putString(key, value);
            is Int -> editor.putInt(key, value);
            is Boolean -> editor.putBoolean(key, value);
        }
        editor.apply();
    }
}
```

**基本写法：ObservableList 委托**
`val <name>: List<<T>> by <ObservableList>(<init>)`
```kotlin
// 可观察列表委托
class ObservableList<T>(initial: List<T>) {
    private val items = initial.toMutableList();
    var onChange: ((List<T>) -> Unit)? = null;
    operator fun getValue(thisRef: Any?, property: KProperty<*>): List<T> = items.toList();
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: List<T>) {
        items.clear();
        items.addAll(value);
        onChange?.invoke(items.toList());
    }
}
```

---

## 委托属性与验证

**基本写法：带验证的属性委托**
`var <name>: <Type> by <ValidatedDelegate>(<init>, <validator>)`
```kotlin
// 带验证的属性委托
class ValidatedDelegate<T>(
    initialValue: T,
    private val validator: (T) -> Boolean
) {
    private var value = initialValue;
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T = value;
    operator fun setValue(thisRef: Any?, property: KProperty<*>, value: T) {
        require(validator(value)) { "验证失败: $value" };
        this.value = value;
    }
}
```

---

## 委托属性与缓存

**基本写法：带过期时间的缓存委托**
`val <name>: <Type> by <CacheDelegate>(<ttl>) { <init> }`
```kotlin
// 带过期时间的缓存委托
class CacheDelegate<T>(private val ttlMillis: Long, private val loader: () -> T) {
    private var value: T? = null;
    private var lastLoadTime: Long = 0;
    operator fun getValue(thisRef: Any?, property: KProperty<*>): T {
        val now = System.currentTimeMillis();
        if (value == null || now - lastLoadTime > ttlMillis) {
            value = loader();
            lastLoadTime = now;
        }
        return value!!;
    }
}
```



<!-- ============ 文档分隔线：014-kotlin/009-CoroutineBasics.md ============ -->

# Kotlin 协程基础速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 协程基础

**基本写法：launch 启动协程**
`GlobalScope.launch { <body> }`
```kotlin
// 启动新协程（不阻塞当前线程）
GlobalScope.launch {
    delay(1000);
    println("Hello, Coroutines!");
}
```

**基本写法：runBlocking 阻塞启动**
`runBlocking { <body> }`
```kotlin
// 阻塞当前线程直到协程完成
runBlocking {
    delay(1000);
    println("Hello, Coroutines!");
}
```

**基本写法：async 启动异步任务**
`async { <body> }`
```kotlin
// 启动异步任务并返回 Deferred
val deferred = async {
    delay(1000);
    42;
}
```

**基本写法：await 等待结果**
`<deferred>.await()`
```kotlin
// 等待异步任务完成并获取结果
val result = deferred.await();
```

**基本写法：awaitAll 等待多个任务**
`awaitAll(<deferred1>, <deferred2>)`
```kotlin
// 等待多个异步任务完成
val d1 = async { 1 };
val d2 = async { 2 };
val results = awaitAll(d1, d2);
```

---

## 作用域构建器

**基本写法：coroutineScope 协程作用域**
`coroutineScope { <body> }`
```kotlin
// 创建协程作用域，等待所有子协程完成
coroutineScope {
    launch {
        delay(1000);
        println("Task 1");
    }
    launch {
        delay(500);
        println("Task 2");
    }
}
```

**基本写法：supervisorScope 监督作用域**
`supervisorScope { <body> }`
```kotlin
// 子协程异常不会取消其他子协程
supervisorScope {
    launch {
        delay(100);
        throw Exception("Failed");
    }
    launch {
        delay(200);
        println("Still running");
    }
}
```

**基本写法：withContext 切换上下文**
`withContext(<dispatcher>) { <body> }`
```kotlin
// 切换协程上下文
suspend fun fetchData(): String = withContext(Dispatchers.IO) {
    networkRequest();
}
```

---

## 调度器

**基本写法：Dispatchers.Main 主线程**
`launch(Dispatchers.Main) { <body> }`
```kotlin
// 在主线程执行（UI 操作）
launch(Dispatchers.Main) {
    updateUI();
}
```

**基本写法：Dispatchers.IO IO 线程**
`launch(Dispatchers.IO) { <body> }`
```kotlin
// 在 IO 线程执行（网络、文件操作）
launch(Dispatchers.IO) {
    val data = readFile();
}
```

**基本写法：Dispatchers.Default 默认线程**
`launch(Dispatchers.Default) { <body> }`
```kotlin
// 在默认线程执行（CPU 密集型）
launch(Dispatchers.Default) {
    val result = heavyComputation();
}
```

**基本写法：Dispatchers.Unconfined 不限制**
`launch(Dispatchers.Unconfined) { <body> }`
```kotlin
// 不限制线程
launch(Dispatchers.Unconfined) {
    println("Running in ${Thread.currentThread().name}");
}
```

---

## 挂起函数

**基本写法：suspend 挂起函数**
`suspend fun <name>(<params>): <ReturnType>`
```kotlin
// 挂起函数，可在协程中调用
suspend fun fetchData(): String {
    delay(1000);
    return "Data";
}
```

**基本写法：挂起函数调用网络请求**
`suspend fun <name>(<params>): <ReturnType> = withContext(Dispatchers.IO) { <body> }`
```kotlin
// 挂起函数执行网络请求
suspend fun fetchUser(id: String): User = withContext(Dispatchers.IO) {
    api.getUser(id);
}
```

**基本写法：delay 延迟**
`delay(<milliseconds>)`
```kotlin
// 延迟指定毫秒（不阻塞线程）
delay(1000);
```

---

## Job 控制

**基本写法：Job 取消**
`<job>.cancel()`
```kotlin
// 取消协程
val job = launch {
    repeat(1000) { i ->
        println(i);
        delay(500);
    }
}
delay(1300);
job.cancel();
```

**基本写法：Job 等待完成**
`<job>.join()`
```kotlin
// 等待协程完成
val job = launch { /* ... */ };
job.join();
```

**基本写法：cancelAndJoin 取消并等待**
`<job>.cancelAndJoin()`
```kotlin
// 取消并等待协程完成
job.cancelAndJoin();
```

**基本写法：isActive 检查活跃状态**
`if (isActive) { <body> }`
```kotlin
// 检查协程是否活跃
while (isActive) {
    println("Working...");
    delay(500);
}
```

**基本写法：ensureActive 确保活跃**
`ensureActive()`
```kotlin
// 确保协程活跃，否则抛出 CancellationException
ensureActive();
```

**基本写法：yield 让出执行权**
`yield()`
```kotlin
// 让出执行权给其他协程
yield();
```

---

## 超时控制

**基本写法：withTimeout 超时**
`withTimeout(<milliseconds>) { <body> }`
```kotlin
// 设置超时，超时抛出 TimeoutCancellationException
withTimeout(1000) {
    repeat(1000) { i ->
        println(i);
        delay(100);
    }
}
```

**基本写法：withTimeoutOrNull 安全超时**
`withTimeoutOrNull(<milliseconds>) { <body> }`
```kotlin
// 超时返回 null，不抛出异常
val result = withTimeoutOrNull(1000) {
    repeat(1000) { i ->
        println(i);
        delay(100);
    }
    "Done";
}
```

---

## Channel 通道

**基本写法：Channel 创建通道**
`Channel<<Type>>()`
```kotlin
// 创建通道
val channel = Channel<String>();
```

**基本写法：send 发送数据**
`<channel>.send(<value>)`
```kotlin
// 发送数据到通道
launch {
    channel.send("Hello");
}
```

**基本写法：receive 接收数据**
`<channel>.receive()`
```kotlin
// 从通道接收数据
val value = channel.receive();
```

**基本写法：close 关闭通道**
`<channel>.close()`
```kotlin
// 关闭通道
channel.close();
```

**基本写法：for 遍历通道**
`for (<item> in <channel>) { <body> }`
```kotlin
// 遍历通道接收数据
for (msg in channel) {
    println(msg);
}
```

**基本写法：produce 生产者**
`produce { send(<value>) }`
```kotlin
// 创建生产者协程
val producer = produce {
    for (i in 1..5) {
        send(i);
    }
}
```

---

## Flow 流

**基本写法：flow 创建流**
`flow { emit(<value>) }`
```kotlin
// 创建冷流
val flow = flow {
    for (i in 1..5) {
        emit(i);
    }
}
```

**基本写法：collect 收集流**
`<flow>.collect { <body> }`
```kotlin
// 收集流中的值
flow.collect { value ->
    println(value);
}
```

**基本写法：flowOf 创建流**
`flowOf(<values>)`
```kotlin
// 创建固定值的流
val flow = flowOf(1, 2, 3, 4, 5);
```

**基本写法：asFlow 集合转流**
`<collection>.asFlow()`
```kotlin
// 集合转换为流
val flow = listOf(1, 2, 3).asFlow();
```

**基本写法：map 转换流**
`<flow>.map { <transform> }`
```kotlin
// 转换流中的值
val doubled = flow.map { it * 2 };
```

**基本写法：filter 过滤流**
`<flow>.filter { <predicate> }`
```kotlin
// 过滤流中的值
val evens = flow.filter { it % 2 == 0 };
```

**基本写法：flowOn 切换调度器**
`<flow>.flowOn(<dispatcher>)`
```kotlin
// 切换流执行的调度器
val flow = flow { /* IO 操作 */ }.flowOn(Dispatchers.IO);
```

**基本写法：buffer 缓冲流**
`<flow>.buffer()`
```kotlin
// 缓冲流，提高并发性能
flow.buffer().collect { /* ... */ }
```

**基本写法：conflate 合并流**
`<flow>.conflate()`
```kotlin
// 合并流，只保留最新值
flow.conflate().collect { /* ... */ }
```

**基本写法：zip 合并流**
`<flow1>.zip(<flow2>) { <a>, <b> -> <transform> }`
```kotlin
// 合并两个流
val combined = flow1.zip(flow2) { a, b -> "$a-$b" };
```

**基本写法：combine 合并流**
`<flow1>.combine(<flow2>) { <a>, <b> -> <transform> }`
```kotlin
// 合并两个流，任一流发射时触发
val combined = flow1.combine(flow2) { a, b -> a + b };
```

**基本写法：flatMapConcat 顺序展平**
`<flow>.flatMapConcat { <transform> }`
```kotlin
// 顺序展平流
flow.flatMapConcat { flowOf(it, it * 2) };
```

**基本写法：flatMapMerge 并发展平**
`<flow>.flatMapMerge { <transform> }`
```kotlin
// 并发展平流
flow.flatMapMerge { flowOf(it, it * 2) };
```

**基本写法：catch 捕获异常**
`<flow>.catch { <body> }`
```kotlin
// 捕获流中的异常
flow.catch { e ->
    println("Error: $e");
}.collect { /* ... */ }
```

**基本写法：onCompletion 完成回调**
`<flow>.onCompletion { <body> }`
```kotlin
// 流完成时回调
flow.onCompletion {
    println("Completed");
}.collect { /* ... */ }
```

**基本写法：StateFlow 状态流**
`MutableStateFlow(<initial>)`
```kotlin
// 创建状态流
val state = MutableStateFlow(0);
```

**基本写法：SharedFlow 共享流**
`MutableSharedFlow<<Type>>()`
```kotlin
// 创建共享流
val shared = MutableSharedFlow<String>();
```

---

## 异常处理

**基本写法：try-catch 捕获异常**
`try { <body> } catch (e: <Exception>) { <body> }`
```kotlin
// 捕获协程中的异常
try {
    delay(1000);
} catch (e: CancellationException) {
    println("Cancelled");
}
```

**基本写法：CoroutineExceptionHandler 异常处理器**
`val <handler> = CoroutineExceptionHandler { <ctx>, <e> -> <body> }`
```kotlin
// 创建协程异常处理器
val handler = CoroutineExceptionHandler { _, e ->
    println("Caught: $e");
};
launch(handler) {
    throw RuntimeException("Error");
}
```

**基本写法：SupervisorJob 监督作业**
`launch(SupervisorJob()) { <body> }`
```kotlin
// 使用 SupervisorJob，子协程异常不影响其他子协程
val supervisor = SupervisorJob();
launch(supervisor) { /* ... */ }
```

---

## 并发工具

**基本写法：Mutex 互斥锁**
`val <mutex> = Mutex(); <mutex>.withLock { <body> }`
```kotlin
// 使用互斥锁保护共享资源
val mutex = Mutex();
var counter = 0;
launch {
    mutex.withLock {
        counter++;
    }
}
```

**基本写法：Semaphore 信号量**
`val <semaphore> = Semaphore(<permits>); <semaphore>.withPermit { <body> }`
```kotlin
// 使用信号量限制并发数
val semaphore = Semaphore(3);
launch {
    semaphore.withPermit {
        networkRequest();
    }
}
```

**换行写法：async 并发请求**
`coroutineScope { val <d1> = async { <body> }; val <d2> = async { <body> }; <d1>.await() + <d2>.await() }`
```kotlin
// 并发执行多个异步任务
suspend fun fetchAll(): Pair<String, Int> = coroutineScope {
    val name = async { fetchName() };
    val age = async { fetchAge() };
    name.await() to age.await();
}
```



<!-- ============ 文档分隔线：014-kotlin/010-KotlinCollectionOperation.md ============ -->

# Kotlin 集合操作速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 集合创建

**基本写法：listOf 创建只读列表**
`listOf(<elements>)`
```kotlin
// 创建只读列表
val numbers = listOf(1, 2, 3, 4, 5);
```

**基本写法：mutableListOf 创建可变列表**
`mutableListOf(<elements>)`
```kotlin
// 创建可变列表
val mutableList = mutableListOf(1, 2, 3);
mutableList.add(4);
```

**基本写法：setOf 创建只读集合**
`setOf(<elements>)`
```kotlin
// 创建只读集合（去重）
val set = setOf(1, 2, 3, 3);  // {1, 2, 3}
```

**基本写法：mutableSetOf 创建可变集合**
`mutableSetOf(<elements>)`
```kotlin
// 创建可变集合
val mutableSet = mutableSetOf(1, 2, 3);
mutableSet.add(4);
```

**基本写法：mapOf 创建只读映射**
`mapOf(<key1> to <value1>, <key2> to <value2>)`
```kotlin
// 创建只读映射
val map = mapOf("a" to 1, "b" to 2);
```

**基本写法：mutableMapOf 创建可变映射**
`mutableMapOf(<key1> to <value1>)`
```kotlin
// 创建可变映射
val mutableMap = mutableMapOf("a" to 1);
mutableMap["b"] = 2;
```

**基本写法：emptyList 创建空列表**
`emptyList<<Type>>()`
```kotlin
// 创建空列表
val empty: List<String> = emptyList();
```

**基本写法：arrayListOf 创建 ArrayList**
`arrayListOf(<elements>)`
```kotlin
// 创建 ArrayList
val arrayList = arrayListOf(1, 2, 3);
```

**基本写法：linkedMapOf 创建 LinkedHashMap**
`linkedMapOf(<key1> to <value1>)`
```kotlin
// 创建 LinkedHashMap（保持插入顺序）
val linkedMap = linkedMapOf("a" to 1, "b" to 2);
```

---

## 集合基本操作

**基本写法：size 获取大小**
`<collection>.size`
```kotlin
// 获取集合大小
val size = numbers.size;
```

**基本写法：contains 检查包含**
`<collection>.contains(<element>)`
```kotlin
// 检查是否包含元素
numbers.contains(3);
```

**基本写法：in 检查包含**
`<element> in <collection>`
```kotlin
// 使用 in 检查包含
3 in numbers;
```

**基本写法：!in 检查不包含**
`<element> !in <collection>`
```kotlin
// 使用 !in 检查不包含
6 !in numbers;
```

**基本写法：isEmpty 检查空集合**
`<collection>.isEmpty()`
```kotlin
// 检查集合是否为空
numbers.isEmpty();
```

**基本写法：isNotEmpty 检查非空集合**
`<collection>.isNotEmpty()`
```kotlin
// 检查集合是否非空
numbers.isNotEmpty();
```

**基本写法：get 获取元素**
`<list>[<index>]`
```kotlin
// 通过索引获取元素
val first = numbers[0];
```

**基本写法：get 获取 Map 值**
`<map>[<key>]`
```kotlin
// 通过键获取值
val value = map["a"];
```

---

## 过滤操作

**基本写法：filter 过滤元素**
`<collection>.filter { <predicate> }`
```kotlin
// 过滤满足条件的元素
val evens = numbers.filter { it % 2 == 0 };
```

**基本写法：filterNot 反向过滤**
`<collection>.filterNot { <predicate> }`
```kotlin
// 过滤不满足条件的元素
val odds = numbers.filterNot { it % 2 == 0 };
```

**基本写法：filterNotNull 过滤 null**
`<collection>.filterNotNull()`
```kotlin
// 过滤 null 值
val list: List<String?> = listOf("a", null, "b");
val nonNull = list.filterNotNull();
```

**基本写法：filterIndexed 带索引过滤**
`<collection>.filterIndexed { <index>, <item> -> <predicate> }`
```kotlin
// 带索引过滤
val filtered = numbers.filterIndexed { index, _ -> index % 2 == 0 };
```

**基本写法：filterIsInstance 过滤类型**
`<collection>.filterIsInstance<<Type>>()`
```kotlin
// 过滤指定类型
val mixed: List<Any> = listOf(1, "a", 2, "b");
val strings = mixed.filterIsInstance<String>();
```

**基本写法：take 获取前 n 个**
`<collection>.take(<n>)`
```kotlin
// 获取前 n 个元素
val first3 = numbers.take(3);
```

**基本写法：takeLast 获取后 n 个**
`<collection>.takeLast(<n>)`
```kotlin
// 获取后 n 个元素
val last3 = numbers.takeLast(3);
```

**基本写法：drop 丢弃前 n 个**
`<collection>.drop(<n>)`
```kotlin
// 丢弃前 n 个元素
val remaining = numbers.drop(2);
```

**基本写法：dropLast 丢弃后 n 个**
`<collection>.dropLast(<n>)`
```kotlin
// 丢弃后 n 个元素
val remaining = numbers.dropLast(2);
```

**基本写法：takeWhile 条件获取**
`<collection>.takeWhile { <predicate> }`
```kotlin
// 满足条件时获取，遇到不满足时停止
val result = numbers.takeWhile { it < 4 };
```

**基本写法：dropWhile 条件丢弃**
`<collection>.dropWhile { <predicate> }`
```kotlin
// 满足条件时丢弃，遇到不满足时停止
val result = numbers.dropWhile { it < 4 };
```

**基本写法：distinct 去重**
`<collection>.distinct()`
```kotlin
// 去重
val unique = listOf(1, 2, 2, 3, 3).distinct();
```

**基本写法：distinctBy 按条件去重**
`<collection>.distinctBy { <selector> }`
```kotlin
// 按条件去重
val people = listOf(Person("Alice", 25), Person("Bob", 25));
val uniqueAges = people.distinctBy { it.age };
```

---

## 映射操作

**基本写法：map 映射元素**
`<collection>.map { <transform> }`
```kotlin
// 映射元素
val doubled = numbers.map { it * 2 };
```

**基本写法：mapIndexed 带索引映射**
`<collection>.mapIndexed { <index>, <item> -> <transform> }`
```kotlin
// 带索引映射
val indexed = numbers.mapIndexed { index, value -> "$index: $value" };
```

**基本写法：mapNotNull 映射并过滤 null**
`<collection>.mapNotNull { <transform> }`
```kotlin
// 映射并过滤 null
val lengths = listOf("a", null, "bb").mapNotNull { it?.length };
```

**基本写法：flatMap 扁平映射**
`<collection>.flatMap { <transform> }`
```kotlin
// 扁平映射
val nested = listOf(listOf(1, 2), listOf(3, 4));
val flat = nested.flatMap { it };
```

**基本写法：flatten 扁平化**
`<collection>.flatten()`
```kotlin
// 扁平化嵌套集合
val flat = nested.flatten();
```

**基本写法：groupBy 分组**
`<collection>.groupBy { <keySelector> }`
```kotlin
// 按条件分组
val grouped = numbers.groupBy { if (it % 2 == 0) "even" else "odd" };
```

**基本写法：groupBy 带值转换**
`<collection>.groupBy({ <keySelector> }, { <valueTransform> })`
```kotlin
// 分组并转换值
val grouped = people.groupBy({ it.age }, { it.name });
```

**基本写法：chunked 分块**
`<collection>.chunked(<size>)`
```kotlin
// 分块处理
val chunks = numbers.chunked(2);
```

**基本写法：windowed 滑动窗口**
`<collection>.windowed(<size>, <step>, <partialWindows>)`
```kotlin
// 滑动窗口
val windows = numbers.windowed(3, 1, false);
```

**基本写法：zip 合并集合**
`<list1>.zip(<list2>)`
```kotlin
// 合并两个集合
val names = listOf("Alice", "Bob");
val ages = listOf(25, 30);
val pairs = names.zip(ages);
```

**基本写法：zip 合并并转换**
`<list1>.zip(<list2>) { <a>, <b> -> <transform> }`
```kotlin
// 合并并转换
val combined = names.zip(ages) { name, age -> "$name: $age" };
```

**基本写法：unzip 拆分**
`<list>.unzip()`
```kotlin
// 拆分 Pair 列表
val pairs = listOf("a" to 1, "b" to 2);
val (keys, values) = pairs.unzip();
```

**基本写法：partition 分区**
`<collection>.partition { <predicate> }`
```kotlin
// 按条件分区为两个列表
val (evens, odds) = numbers.partition { it % 2 == 0 };
```

---

## 查找操作

**基本写法：find 查找第一个匹配**
`<collection>.find { <predicate> }`
```kotlin
// 查找第一个匹配元素
val first = numbers.find { it > 3 };
```

**基本写法：findLast 查找最后一个匹配**
`<collection>.findLast { <predicate> }`
```kotlin
// 查找最后一个匹配元素
val last = numbers.findLast { it > 3 };
```

**基本写法：firstOrNull 获取第一个元素**
`<collection>.firstOrNull()`
```kotlin
// 获取第一个元素，空列表返回 null
val first = numbers.firstOrNull();
```

**基本写法：firstOrNull 条件查找**
`<collection>.firstOrNull { <predicate> }`
```kotlin
// 查找第一个满足条件的元素
val first = numbers.firstOrNull { it > 3 };
```

**基本写法：lastOrNull 获取最后一个元素**
`<collection>.lastOrNull()`
```kotlin
// 获取最后一个元素，空列表返回 null
val last = numbers.lastOrNull();
```

**基本写法：lastOrNull 条件查找**
`<collection>.lastOrNull { <predicate> }`
```kotlin
// 查找最后一个满足条件的元素
val last = numbers.lastOrNull { it > 3 };
```

**基本写法：indexOf 查找索引**
`<list>.indexOf(<element>)`
```kotlin
// 查找元素索引
val index = numbers.indexOf(3);
```

**基本写法：binarySearch 二分查找**
`<list>.binarySearch(<element>)`
```kotlin
// 二分查找（列表需有序）
val index = sortedList.binarySearch(5);
```

**基本写法：elementAtOrNull 安全获取**
`<list>.elementAtOrNull(<index>)`
```kotlin
// 安全获取指定索引元素
val element = numbers.elementAtOrNull(10);
```

**基本写法：elementAtOrElse 条件获取**
`<list>.elementAtOrElse(<index>) { <default> }`
```kotlin
// 获取指定索引元素，越界返回默认值
val element = numbers.elementAtOrElse(10) { -1 };
```

---

## 排序操作

**基本写法：sorted 升序排序**
`<collection>.sorted()`
```kotlin
// 升序排序
val sorted = numbers.sorted();
```

**基本写法：sortedDescending 降序排序**
`<collection>.sortedDescending()`
```kotlin
// 降序排序
val sorted = numbers.sortedDescending();
```

**基本写法：sortedBy 按条件升序**
`<collection>.sortedBy { <selector> }`
```kotlin
// 按条件升序排序
val sorted = people.sortedBy { it.age };
```

**基本写法：sortedByDescending 按条件降序**
`<collection>.sortedByDescending { <selector> }`
```kotlin
// 按条件降序排序
val sorted = people.sortedByDescending { it.age };
```

**基本写法：sortedWith 自定义排序**
`<collection>.sortedWith(<comparator>)`
```kotlin
// 自定义比较器排序
val sorted = people.sortedWith(compareBy({ it.age }, { it.name }));
```

**基本写法：reversed 反转**
`<collection>.reversed()`
```kotlin
// 反转集合
val reversed = numbers.reversed();
```

**基本写法：shuffled 随机打乱**
`<collection>.shuffled()`
```kotlin
// 随机打乱集合
val shuffled = numbers.shuffled();
```



<!-- ============ 文档分隔线：014-kotlin/011-KotlinCollectionAdvanced.md ============ -->

# Kotlin 集合进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 聚合操作

**基本写法：sum 求和**
`<collection>.sum()`
```kotlin
// 求和
val sum = numbers.sum();
```

**基本写法：sumBy 条件求和**
`<collection>.sumOf { <selector> }`
```kotlin
// 按条件求和
val totalAge = people.sumOf { it.age };
```

**基本写法：maxOrNull 最大值**
`<collection>.maxOrNull()`
```kotlin
// 获取最大值（空集合返回 null）
val max = numbers.maxOrNull();
```

**基本写法：maxByOrNull 条件最大值**
`<collection>.maxByOrNull { <selector> }`
```kotlin
// 按条件获取最大元素
val oldest = people.maxByOrNull { it.age };
```

**基本写法：minOrNull 最小值**
`<collection>.minOrNull()`
```kotlin
// 获取最小值（空集合返回 null）
val min = numbers.minOrNull();
```

**基本写法：minByOrNull 条件最小值**
`<collection>.minByOrNull { <selector> }`
```kotlin
// 按条件获取最小元素
val youngest = people.minByOrNull { it.age };
```

**基本写法：average 平均值**
`<collection>.average()`
```kotlin
// 计算平均值
val avg = numbers.average();
```

**基本写法：count 计数**
`<collection>.count()`
```kotlin
// 计算元素数量
val count = numbers.count();
```

**基本写法：count 条件计数**
`<collection>.count { <predicate> }`
```kotlin
// 计算满足条件的元素数量
val count = numbers.count { it > 3 };
```

**基本写法：fold 累积**
`<collection>.fold(<initial>) { <acc>, <item> -> <body> }`
```kotlin
// 从左到右累积
val sum = numbers.fold(0) { acc, num -> acc + num };
```

**基本写法：reduce 累积**
`<collection>.reduce { <acc>, <item> -> <body> }`
```kotlin
// 从左到右累积（无初始值）
val sum = numbers.reduce { acc, num -> acc + num };
```

**基本写法：reduceOrNull 安全累积**
`<collection>.reduceOrNull { <acc>, <item> -> <body> }`
```kotlin
// 安全累积（空集合返回 null）
val sum = numbers.reduceOrNull { acc, num -> acc + num };
```

**基本写法：joinToString 连接字符串**
`<collection>.joinToString(<separator>)`
```kotlin
// 连接为字符串
val str = numbers.joinToString(", ");
```

**换行写法：joinToString 带前缀后缀**
`<collection>.joinToString(<separator>, <prefix>, <postfix>)`
```kotlin
// 连接为字符串带前缀后缀
val str = numbers.joinToString(
    separator = ", ",
    prefix = "[",
    postfix = "]"
);
```

---

## 判断操作

**基本写法：any 判断是否有元素**
`<collection>.any()`
```kotlin
// 判断集合是否有元素
val hasElements = numbers.any();
```

**基本写法：any 条件判断**
`<collection>.any { <predicate> }`
```kotlin
// 判断是否有满足条件的元素
val hasEven = numbers.any { it % 2 == 0 };
```

**基本写法：all 全部满足**
`<collection>.all { <predicate> }`
```kotlin
// 判断是否全部满足条件
val allPositive = numbers.all { it > 0 };
```

**基本写法：none 全不满足**
`<collection>.none { <predicate> }`
```kotlin
// 判断是否全不满足条件
val noneNegative = numbers.none { it < 0 };
```

**基本写法：contains 检查包含**
`<collection>.contains(<element>)`
```kotlin
// 检查是否包含元素
numbers.contains(5);
```

---

## 序列（Sequence）

**基本写法：asSequence 转换为序列**
`<collection>.asSequence()`
```kotlin
// 转换为序列（惰性求值）
val sequence = numbers.asSequence();
```

**基本写法：sequenceOf 创建序列**
`sequenceOf(<elements>)`
```kotlin
// 创建序列
val seq = sequenceOf(1, 2, 3);
```

**换行写法：generateSequence 生成序列**
`generateSequence(<seed>) { <next> }`
```kotlin
// 生成序列
val naturals = generateSequence(1) { it + 1 };
```

**换行写法：yield 构建序列**
`sequence { yield(<value>); yieldAll(<collection>) }`
```kotlin
// 使用 yield 构建序列
val seq = sequence {
    yield(1);
    yield(2);
    yieldAll(listOf(3, 4, 5));
}
```

**基本写法：序列操作链**
`<sequence>.filter { <predicate> }.map { <transform> }.toList()`
```kotlin
// 序列操作链（惰性求值）
val result = numbers.asSequence()
    .filter { it > 2 }
    .map { it * 2 }
    .toList();
```

**基本写法：take 限制序列**
`<sequence>.take(<n>)`
```kotlin
// 限制序列元素数量
val first5 = naturals.take(5).toList();
```

---

## 集合转换

**基本写法：toSet 转换为 Set**
`<collection>.toSet()`
```kotlin
// 转换为 Set（去重）
val set = numbers.toSet();
```

**基本写法：toList 转换为 List**
`<collection>.toList()`
```kotlin
// 转换为 List
val list = set.toList();
```

**基本写法：toMap 转换为 Map**
`<list>.toMap()`
```kotlin
// Pair 列表转换为 Map
val map = listOf("a" to 1, "b" to 2).toMap();
```

**基本写法：toMutableList 转换为可变列表**
`<collection>.toMutableList()`
```kotlin
// 转换为可变列表
val mutable = numbers.toMutableList();
```

**基本写法：associate 转换为 Map**
`<collection>.associate { <transform> }`
```kotlin
// 转换为 Map
val map = people.associate { it.name to it.age };
```

**基本写法：associateBy 按 key 转换**
`<collection>.associateBy { <keySelector> }`
```kotlin
// 按 key 转换为 Map
val map = people.associateBy { it.name };
```

**基本写法：associateWith 按 value 转换**
`<collection>.associateWith { <valueSelector> }`
```kotlin
// 按 value 转换为 Map
val map = numbers.associateWith { it * 2 };
```

---

## 集合遍历

**基本写法：forEach 遍历**
`<collection>.forEach { <body> }`
```kotlin
// 遍历集合
numbers.forEach { println(it); }
```

**基本写法：forEachIndexed 带索引遍历**
`<collection>.forEachIndexed { <index>, <item> -> <body> }`
```kotlin
// 带索引遍历
numbers.forEachIndexed { index, value ->
    println("$index: $value");
}
```

**基本写法：for-in 遍历**
`for (<item> in <collection>) { <body> }`
```kotlin
// for-in 遍历
for (item in numbers) {
    println(item);
}
```

**基本写法：遍历 Map**
`for ((<key>, <value>) in <map>) { <body> }`
```kotlin
// 遍历 Map 键值对
for ((key, value) in map) {
    println("$key = $value");
}
```

**基本写法：遍历 List 索引**
`for (<index> in <list>.indices) { <body> }`
```kotlin
// 遍历 List 索引
for (i in numbers.indices) {
    println("Index $i: ${numbers[i]}");
}
```

**基本写法：iterator 迭代器**
`val <iterator> = <collection>.iterator(); while (<iterator>.hasNext()) { <body> }`
```kotlin
// 使用迭代器遍历
val iterator = numbers.iterator();
while (iterator.hasNext()) {
    println(iterator.next());
}
```

---

## 集合修改

**基本写法：add 添加元素**
`<mutableList>.add(<element>)`
```kotlin
// 添加元素到末尾
mutableList.add(4);
```

**基本写法：add 指定位置添加**
`<mutableList>.add(<index>, <element>)`
```kotlin
// 在指定位置添加元素
mutableList.add(0, 0);
```

**基本写法：addAll 添加多个元素**
`<mutableList>.addAll(<collection>)`
```kotlin
// 添加多个元素
mutableList.addAll(listOf(5, 6, 7));
```

**基本写法：remove 移除元素**
`<mutableList>.remove(<element>)`
```kotlin
// 移除指定元素
mutableList.remove(3);
```

**基本写法：removeAt 移除指定位置**
`<mutableList>.removeAt(<index>)`
```kotlin
// 移除指定位置的元素
mutableList.removeAt(0);
```

**基本写法：clear 清空集合**
`<mutableList>.clear()`
```kotlin
// 清空集合
mutableList.clear();
```

**基本写法：set 修改元素**
`<mutableList>[<index>] = <value>`
```kotlin
// 修改指定位置的元素
mutableList[0] = 10;
```

**基本写法：Map 修改**
`<mutableMap>[<key>] = <value>`
```kotlin
// 修改 Map 值
mutableMap["a"] = 10;
```

**基本写法：putIfAbsent 条件添加**
`<mutableMap>.putIfAbsent(<key>, <value>)`
```kotlin
// 键不存在时添加
mutableMap.putIfAbsent("c", 3);
```

**基本写法：remove 移除 Map 条目**
`<mutableMap>.remove(<key>)`
```kotlin
// 移除 Map 条目
mutableMap.remove("a");
```



<!-- ============ 文档分隔线：014-kotlin/012-KotlinSerialization.md ============ -->

# Kotlin 序列化速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 序列化基础

**基本写法：@Serializable 注解**
`@Serializable data class <Name>(val <prop>: <Type>)`
```kotlin
// 标记类为可序列化
@Serializable
data class User(val name: String, val age: Int);
```

**基本写法：encodeToString 序列化为字符串**
`Json.encodeToString(<obj>)`
```kotlin
// 序列化对象为 JSON 字符串
val json = Json.encodeToString(User("Alice", 25));
```

**基本写法：decodeFromString 反序列化**
`Json.decodeFromString<<Type>>(<json>)`
```kotlin
// 从 JSON 字符串反序列化
val user = Json.decodeFromString<User>("""{"name":"Alice","age":25}""");
```

**基本写法：Json 配置**
`Json { <options> }`
```kotlin
// 自定义 Json 配置
val json = Json {
    ignoreUnknownKeys = true;
    prettyPrint = true;
}
```

---

## 字段配置

**基本写法：@SerialName 自定义字段名**
`@SerialName("<name>") val <prop>: <Type>`
```kotlin
// 自定义 JSON 字段名
@Serializable
data class User(
    @SerialName("user_name") val name: String,
    @SerialName("user_age") val age: Int
);
```

**基本写法：@Transient 忽略字段**
`@Transient val <prop>: <Type> = <default>`
```kotlin
// 忽略字段不参与序列化
@Serializable
data class User(
    val name: String,
    @Transient val temp: String = ""
);
```

**基本写法：@Optional 可选字段**
`@Optional val <prop>: <Type> = <default>`
```kotlin
// 可选字段，缺失时使用默认值
@Serializable
data class User(
    val name: String,
    val email: String? = null
);
```

**基本写法：默认值字段**
`val <prop>: <Type> = <default>`
```kotlin
// 带默认值的字段
@Serializable
data class Config(
    val host: String = "localhost",
    val port: Int = 8080
);
```

---

## 多态序列化

**基本写法：@Polymorphic 多态标记**
`@Polymorphic open class <Name>`
```kotlin
// 标记类支持多态序列化
@Serializable
@Polymorphic
open class Animal;
```

**基本写法：@SerialName 子类注册**
`@Serializable @SerialName("<name>") class <SubName> : <BaseName>()`
```kotlin
// 子类使用 @SerialName 注册
@Serializable
@SerialName("dog")
class Dog : Animal();
```

**换行写法：SerializersModule 序列化模块**
`SerializersModule { polymorphic(<Base>::class) { subclass(<Sub>::class) } }`
```kotlin
// 注册多态子类
val module = SerializersModule {
    polymorphic(Animal::class) {
        subclass(Dog::class);
        subclass(Cat::class);
    }
}
```

**基本写法：使用多态模块**
`Json { serializersModule = <module> }`
```kotlin
// 使用多态模块
val json = Json {
    serializersModule = module;
}
```

---

## 集合序列化

**基本写法：List 序列化**
`@Serializable data class <Name>(val <prop>: List<<Type>>)`
```kotlin
// 序列化包含 List 的对象
@Serializable
data class UserList(val users: List<User>);
```

**基本写法：Map 序列化**
`@Serializable data class <Name>(val <prop>: Map<<KeyType>, <ValueType>>)`
```kotlin
// 序列化包含 Map 的对象
@Serializable
data class Config(val settings: Map<String, String>);
```

**基本写法：嵌套对象序列化**
`@Serializable data class <Outer>(val <inner>: <Inner>)`
```kotlin
// 序列化嵌套对象
@Serializable
data class Order(val id: String, val user: User);
```

**基本写法：可空字段序列化**
`@Serializable data class <Name>(val <prop>: <Type>?)`
```kotlin
// 序列化可空字段
@Serializable
data class User(val name: String, val email: String? = null);
```

---

## 自定义序列化器

**基本写法：KSerializer 自定义序列化器**
`object <Name>Serializer : KSerializer<<Type>> { override fun serialize(...); override fun deserialize(...) }`
```kotlin
// 自定义序列化器
object DateSerializer : KSerializer<Date> {
    override val descriptor = PrimitiveSerialDescriptor("Date", PrimitiveKind.STRING);
    override fun serialize(encoder: Encoder, value: Date) {
        encoder.encodeString(value.toString());
    }
    override fun deserialize(decoder: Decoder): Date {
        return Date(decoder.decodeString());
    }
}
```

**基本写法：@Serializable with 自定义序列化器**
`@Serializable(with = <Serializer>::class) val <prop>: <Type>`
```kotlin
// 使用自定义序列化器
@Serializable
data class Event(
    @Serializable(with = DateSerializer::class) val date: Date
);
```

**基本写法：@Serializer 文件级注册**
`@file:UseSerializers(<Serializer>::class)`
```kotlin
// 文件级注册序列化器
@file:UseSerializers(DateSerializer::class);
```

---

## 编码器与解码器

**基本写法：encode 编码**
`<encoder>.encode<<Type>>(<value>)`
```kotlin
// 使用编码器编码值
encoder.encodeInt(42);
encoder.encodeString("Hello");
```

**基本写法：decode 解码**
`<decoder>.decode<<Type>>()`
```kotlin
// 使用解码器解码值
val num = decoder.decodeInt();
val text = decoder.decodeString();
```

**基本写法：encodeNullable 编码可空值**
`<encoder>.encodeNullableValue(<value>)`
```kotlin
// 编码可空值
encoder.encodeNullableSerializableElement(descriptor, 0, value);
```

**基本写法：CompositeEncoder 复合编码**
`<encoder>.beginStructure(<descriptor>)`
```kotlin
// 复合编码器
val composite = encoder.beginStructure(descriptor);
composite.encodeStringElement(descriptor, 0, value.name);
composite.endStructure();
```

---

## JSON 配置选项

**基本写法：ignoreUnknownKeys 忽略未知键**
`Json { ignoreUnknownKeys = true }`
```kotlin
// 忽略 JSON 中未知的键
val json = Json { ignoreUnknownKeys = true };
```

**基本写法：prettyPrint 美化输出**
`Json { prettyPrint = true }`
```kotlin
// 美化 JSON 输出
val json = Json { prettyPrint = true };
```

**基本写法：encodeDefaults 编码默认值**
`Json { encodeDefaults = true }`
```kotlin
// 编码默认值字段
val json = Json { encodeDefaults = true };
```

**基本写法：explicitNulls 显式 null**
`Json { explicitNulls = false }`
```kotlin
// 不编码 null 值
val json = Json { explicitNulls = false };
```

**基本写法：coerceInputValues 强制输入值**
`Json { coerceInputValues = true }`
```kotlin
// 强制输入值（无效值使用默认值）
val json = Json { coerceInputValues = true };
```

**基本写法：classDiscriminator 类标识符**
`Json { classDiscriminator = "<name>" }`
```kotlin
// 自定义多态类标识符
val json = Json { classDiscriminator = "type" };
```

---

## 流式序列化

**基本写法：encodeToStream 编码到流**
`<format>.encodeToStream(<obj>, <stream>)`
```kotlin
// 编码到输出流
val stream = ByteArrayOutputStream();
Json.encodeToStream(User("Alice", 25), stream);
```

**基本写法：decodeFromStream 从流解码**
`<format>.decodeFromStream<<Type>>(<stream>)`
```kotlin
// 从输入流解码
val stream = ByteArrayInputStream(json.toByteArray());
val user = Json.decodeFromStream<User>(stream);
```

---

## 其他格式

**基本写法：ProtoBuf 序列化**
`ProtoBuf.encodeToString(<obj>)`
```kotlin
// ProtoBuf 序列化
val proto = ProtoBuf.encodeToString(User("Alice", 25));
```

**基本写法：ProtoBuf 反序列化**
`ProtoBuf.decodeFromString<<Type>>(<proto>)`
```kotlin
// ProtoBuf 反序列化
val user = ProtoBuf.decodeFromString<User>(proto);
```

**基本写法：@ProtoNumber 自定义字段编号**
`@ProtoNumber(<n>) val <prop>: <Type>`
```kotlin
// 自定义 ProtoBuf 字段编号
@Serializable
data class User(
    @ProtoNumber(1) val name: String,
    @ProtoNumber(2) val age: Int
);
```

**基本写法：CBOR 序列化**
`Cbor.encodeToByteArray(<obj>)`
```kotlin
// CBOR 序列化
val cbor = Cbor.encodeToByteArray(User("Alice", 25));
```

**基本写法：CBOR 反序列化**
`Cbor.decodeFromByteArray<<Type>>(<cbor>)`
```kotlin
// CBOR 反序列化
val user = Cbor.decodeFromByteArray<User>(cbor);
```

---

## 实战应用

**基本写法：网络请求响应解析**
`suspend fun <name>(<params>): <ReturnType> = withContext(Dispatchers.IO) { Json.decodeFromString<<Type>>(<response>) }`
```kotlin
// 解析网络请求响应
suspend fun fetchUser(id: String): User = withContext(Dispatchers.IO) {
    val response = api.getUser(id);
    Json.decodeFromString<User>(response);
}
```

**基本写法：列表数据解析**
`Json.decodeFromString<List<<Type>>>(<json>)`
```kotlin
// 解析 JSON 数组
val users = Json.decodeFromString<List<User>>(jsonArray);
```

**换行写法：复杂嵌套对象解析**
`@Serializable data class <Response>(val <data>: <Data>); @Serializable data class <Data>(<fields>)`
```kotlin
// 解析复杂嵌套 JSON
@Serializable
data class ApiResponse(
    val code: Int,
    val message: String,
    val data: User
);
val response = Json.decodeFromString<ApiResponse>(json);
```



<!-- ============ 文档分隔线：014-kotlin/013-KotlinScopeFunction.md ============ -->

# Kotlin 作用域函数速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## let 函数

**基本写法：let 转换对象**
`<obj>.let { <body with it> }`
```kotlin
// let 返回 Lambda 结果
val length = "Kotlin".let { it.length };
```

**基本写法：let 处理可空值**
`<obj>?.let { <body with it> }`
```kotlin
// let 安全调用非空值
nickname?.let {
    println("Length: ${it.length}");
}
```

**基本写法：let 链式调用**
`<obj>.let { <transform> }.let { <transform> }`
```kotlin
// let 链式转换
val result = "Hello".let { it.uppercase() }.let { it + "!" };
```

**基本写法：let 与 Elvis 结合**
`<obj>?.let { <transform> } ?: <default>`
```kotlin
// let 与 Elvis 结合提供默认值
val length: Int = nickname?.let { it.length } ?: 0;
```

---

## run 函数

**基本写法：run 执行代码块**
`<obj>.run { <body with this> }`
```kotlin
// run 返回 Lambda 结果，this 指向对象
val length = "Kotlin".run { length };
```

**基本写法：run 配置对象**
`<obj>.run { <body with this> }`
```kotlin
// run 配置对象并返回结果
val result = StringBuilder().run {
    append("Hello");
    append(", Kotlin");
    toString();
}
```

**基本写法：run 作为顶层函数**
`run { <body> }`
```kotlin
// run 作为顶层函数执行代码块
val value = run {
    val a = 10;
    val b = 20;
    a + b;
}
```

---

## with 函数

**基本写法：with 执行多个操作**
`with(<obj>) { <body with this> }`
```kotlin
// with 非扩展版本，对同一对象执行多个操作
val greeting = with(StringBuilder()) {
    append("Hello");
    append(", Kotlin");
    toString();
}
```

**基本写法：with 配置对象**
`with(<obj>) { <body with this> }`
```kotlin
// with 配置对象
val person = Person();
with(person) {
    name = "Alice";
    age = 25;
}
```

**基本写法：with 返回结果**
`val <name> = with(<obj>) { <body with this> }`
```kotlin
// with 返回结果
val description = with(person) {
    "$name, $age years old";
}
```

---

## apply 函数

**基本写法：apply 配置对象**
`<obj>.apply { <body with this> }`
```kotlin
// apply 返回原对象，this 指向对象
val person = Person().apply {
    name = "Alice";
    age = 25;
}
```

**基本写法：apply 配置 Builder**
`<obj>.apply { <body with this> }`
```kotlin
// apply 配置 Builder 对象
val builder = AlertDialog.Builder(context).apply {
    setTitle("Title");
    setMessage("Message");
    setPositiveButton("OK") { _, _ -> };
}
```

**基本写法：apply 链式调用**
`<obj>.apply { <body> }.apply { <body> }`
```kotlin
// apply 链式配置
val list = mutableListOf<String>().apply {
    add("a");
    add("b");
}.apply {
    add("c");
}
```

---

## also 函数

**基本写法：also 执行附加操作**
`<obj>.also { <body with it> }`
```kotlin
// also 返回原对象，it 指向对象
val person = Person("Alice", 25).also {
    println("Created: $it");
}
```

**基本写法：also 日志记录**
`<obj>.also { <body with it> }`
```kotlin
// also 用于日志记录
val result = compute().also {
    println("Computed: $it");
}
```

**基本写法：also 链式调用**
`<obj>.also { <body> }.also { <body> }`
```kotlin
// also 链式附加操作
val list = mutableListOf(1, 2, 3).also {
    println("Initial: $it");
}.also {
    it.add(4);
    println("After add: $it");
}
```

---

## 作用域函数对比

**基本写法：let 与 also 对比**
`<obj>.let { <transform> } // vs <obj>.also { <body> }`
```kotlin
// let 返回 Lambda 结果，also 返回原对象
val length = "Kotlin".let { it.length };  // 返回 Int
val str = "Kotlin".also { println(it); };  // 返回 String
```

**基本写法：apply 与 run 对比**
`<obj>.apply { <body> } // vs <obj>.run { <body> }`
```kotlin
// apply 返回原对象，run 返回 Lambda 结果
val builder = StringBuilder().apply { append("a"); };  // 返回 StringBuilder
val text = StringBuilder().run { append("a"); toString(); };  // 返回 String
```

**基本写法：with 与 run 对比**
`with(<obj>) { <body> } // vs <obj>.run { <body> }`
```kotlin
// with 是非扩展函数，run 是扩展函数
val result1 = with(StringBuilder()) { toString(); };
val result2 = StringBuilder().run { toString(); };
```

---

## 作用域函数选择

**基本写法：let 用于转换**
`<obj>?.let { <transform> }`
```kotlin
// let 典型场景：转换可空值
val length: Int? = nickname?.let { it.length };
```

**基本写法：run 用于计算**
`<obj>.run { <body with this> }`
```kotlin
// run 典型场景：对象上执行计算
val isValid = userInput.run {
    trim().isNotEmpty() && length >= 3;
}
```

**基本写法：with 用于多操作**
`with(<obj>) { <body with this> }`
```kotlin
// with 典型场景：对同一对象执行多个操作
with(person) {
    name = "Alice";
    age = 25;
    email = "alice@example.com";
}
```

**基本写法：apply 用于配置**
`<obj>.apply { <body with this> }`
```kotlin
// apply 典型场景：配置对象
val intent = Intent().apply {
    action = "ACTION_VIEW";
    data = Uri.parse("https://example.com");
}
```

**基本写法：also 用于附加操作**
`<obj>.also { <body with it> }`
```kotlin
// also 典型场景：附加操作（日志、调试）
val list = mutableListOf(1, 2, 3).also {
    println("List created: $it");
}
```

---

## 作用域函数实战

**基本写法：let 处理可空值**
`<obj>?.let { <body with it> } ?: <default>`
```kotlin
// let 处理可空值并提供默认值
val name = nullableName?.let { it.trim() } ?: "Unknown";
```

**基本写法：apply 配置并返回**
`<obj>.apply { <body with this> }`
```kotlin
// apply 配置对象并返回
val person = Person().apply {
    name = "Alice";
    age = 25;
    email = "alice@example.com";
}
```

**基本写法：also 链式调试**
`<obj>.also { <body> }.<method>()`
```kotlin
// also 链式调试
val result = listOf(1, 2, 3)
    .also { println("Original: $it"); }
    .map { it * 2 }
    .also { println("Mapped: $it"); }
    .filter { it > 2 };
```

**基本写法：run 计算并返回**
`<obj>.run { <body with this> }`
```kotlin
// run 计算并返回结果
val summary = data.run {
    val total = sum();
    val avg = average();
    "Total: $total, Avg: $avg";
}
```

**基本写法：with 多操作返回**
`val <name> = with(<obj>) { <body with this> }`
```kotlin
// with 多操作并返回结果
val report = with(database) {
    val count = queryCount();
    val max = queryMax();
    "Count: $count, Max: $max";
}
```

---

## 作用域函数与可空类型

**基本写法：let 处理可空值**
`<obj>?.let { <body with it> }`
```kotlin
// let 安全调用非空值
nullableValue?.let {
    println(it);
}
```

**基本写法：apply 配置可空对象**
`<obj>?.apply { <body with this> }`
```kotlin
// apply 安全配置可空对象
nullableBuilder?.apply {
    append("Hello");
    append(", Kotlin");
}
```

**基本写法：run 处理可空对象**
`<obj>?.run { <body with this> }`
```kotlin
// run 安全执行可空对象
nullableString?.run {
    println(length);
}
```

**基本写法：also 处理可空对象**
`<obj>?.also { <body with it> }`
```kotlin
// also 安全附加操作
nullableValue?.also {
    println("Value: $it");
}
```

---

## 作用域函数与集合

**基本写法：let 转换集合**
`<list>.let { <transform> }`
```kotlin
// let 转换集合
val size = list.let { it.size };
```

**基本写法：apply 配置集合**
`<list>.apply { <body with this> }`
```kotlin
// apply 配置可变集合
val list = mutableListOf<Int>().apply {
    add(1);
    add(2);
    add(3);
}
```

**基本写法：also 调试集合**
`<list>.also { <body with it> }`
```kotlin
// also 调试集合
val filtered = list
    .filter { it > 0 }
    .also { println("Filtered: $it"); }
```

**基本写法：run 计算集合**
`<list>.run { <body with this> }`
```kotlin
// run 计算集合
val result = list.run {
    filter { it > 0 }.sum();
}
```

**基本写法：with 多操作集合**
`with(<list>) { <body with this> }`
```kotlin
// with 对集合执行多个操作
val info = with(list) {
    "Size: $size, First: ${firstOrNull()}, Last: ${lastOrNull()}";
}
```



<!-- ============ 文档分隔线：014-kotlin/014-CoroutineFlow.md ============ -->

# Kotlin 协程与 Flow 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 协程基础

**基本写法：launch 启动协程**
`GlobalScope.launch { <代码> }`
```kotlin
// 启动新协程（不阻塞）
GlobalScope.launch {
    delay(1000)
    println("Hello")
}
```

---

**基本写法：async 异步返回**
`GlobalScope.async { <返回值> }`
```kotlin
// 异步计算结果
val deferred = GlobalScope.async {
    delay(1000)
    42
}
val result = deferred.await()
```

---

**基本写法：runBlocking 阻塞启动**
`runBlocking { <代码> }`
```kotlin
// 阻塞主线程启动协程
runBlocking {
    launch { println("Hello") }
}
```

---

**基本写法：suspend 挂起函数**
`suspend fun <函数名>(<参数>): <返回类型> { ... }`
```kotlin
// 声明挂起函数
suspend fun fetchData(): String {
    delay(1000)
    return "Data"
}
```

---

**基本写法：CoroutineScope 自定义作用域**
`CoroutineScope(<上下文>).launch { <代码> }`
```kotlin
// 创建作用域
val scope = CoroutineScope(Dispatchers.Main)
scope.launch { /* UI 操作 */ }
```

---

## 调度器

**基本写法：Dispatchers.Main 主线程**
`withContext(Dispatchers.Main) { <代码> }`
```kotlin
// 切换到主线程
withContext(Dispatchers.Main) {
    updateUI()
}
```

---

**基本写法：Dispatchers.IO IO 线程**
`withContext(Dispatchers.IO) { <代码> }`
```kotlin
// 切换到 IO 线程
withContext(Dispatchers.IO) {
    val data = readFromFile()
}
```

---

**基本写法：Dispatchers.Default 计算线程**
`withContext(Dispatchers.Default) { <代码> }`
```kotlin
// CPU 密集型任务
withContext(Dispatchers.Default) {
    val result = heavyCompute()
}
```

---

## Job 控制

**基本写法：cancel 取消**
`<job>.cancel();`
```kotlin
// 取消协程
val job = launch { repeat(100) { delay(100) } }
job.cancel()
```

---

**基本写法：join 等待完成**
`<job>.join();`
```kotlin
// 等待协程完成
job.join()
```

---

**基本写法：cancelAndJoin 取消并等待**
`<job>.cancelAndJoin();`
```kotlin
// 取消并等待完成
job.cancelAndJoin()
```

---

**基本写法：isActive 检查活跃**
`<coroutineScope>.isActive`
```kotlin
// 检查协程是否仍活跃
while (isActive) {
    // 执行工作
}
```

---

## Flow 流

**基本写法：flow 构建流**
`flow { <emit 调用> }`
```kotlin
// 创建 Flow
val flow = flow {
    for (i in 1..3) {
        emit(i)
    }
}
```

---

**基本写法：collect 收集**
`<flow>.collect { <处理> }`
```kotlin
// 收集 Flow 数据
flow.collect { value ->
    println(value)
}
```

---

**基本写法：map 转换**
`<flow>.map { <转换> }`
```kotlin
// 转换数据
flow.map { it * 2 }
```

---

**基本写法：filter 过滤**
`<flow>.filter { <条件> }`
```kotlin
// 过滤数据
flow.filter { it > 1 }
```

---

**基本写法：flatMapConcat 串联**
`<flow>.flatMapConcat { <新 Flow> }`
```kotlin
// 串联多个流
flow.flatMapConcat { value -> flowOf(value, value * 2) }
```

---

**基本写法：flowOf 固定流**
`flowOf(<元素1>, <元素2>);`
```kotlin
// 创建固定元素流
flowOf(1, 2, 3).collect { println(it) }
```

---

**基本写法：asFlow 集合转流**
`<集合>.asFlow()`
```kotlin
// List 转 Flow
listOf(1, 2, 3).asFlow().collect { println(it) }
```

---

## Channel 通道

**基本写法：Channel 创建**
`Channel<<类型>>()`
```kotlin
// 创建通道
val channel = Channel<Int>()
launch {
    channel.send(1)
}
val value = channel.receive()
```

---

**基本写法：produce 生产者**
`produce { <send 调用> }`
```kotlin
// 创建生产者
val producer = produce {
    for (i in 1..5) send(i)
}
producer.consumeEach { println(it) }
```

---

## 异常处理

**基本写法：try-catch 捕获异常**
`try { <代码> } catch (e: <异常类型>) { }`
```kotlin
// 捕获协程异常
try {
    deferred.await()
} catch (e: Exception) {
    println("Error: ${e.message}")
}
```

---

**基本写法：CoroutineExceptionHandler**
`CoroutineExceptionHandler { <ctx>, <throwable> -> }`
```kotlin
// 全局异常处理器
val handler = CoroutineExceptionHandler { _, e ->
    println("Caught: $e")
}
scope.launch(handler) { throw RuntimeException("fail") }
```

---

## 超时控制

**基本写法：withTimeout 超时**
`withTimeout(<毫秒>) { <代码> }`
```kotlin
// 设置超时
withTimeout(2000) {
    delay(3000) // 抛出 TimeoutCancellationException
}
```

---

**基本写法：withTimeoutOrNull 超时返回 null**
`withTimeoutOrNull(<毫秒>) { <代码> }`
```kotlin
// 超时返回 null
val result = withTimeoutOrNull(1000) {
    delay(2000)
    "Done"
}  // null
```



<!-- ============ 文档分隔线：014-kotlin/015-KotlinDSLBuilder.md ============ -->

# Kotlin DSL 构建器速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## DSL 基础

**基本写法：带接收者的 Lambda**
`fun <函数名>(<参数>, <块>: <接收者类型>.() -> Unit)`
```kotlin
// 定义 DSL 入口函数
fun html(block: Html.() -> Unit): Html {
    return Html().apply(block)
}
```

---

**基本写法：构建器类**
`class <类名> { fun <方法>(<参数>, <块>: <类型>.() -> Unit) }`
```kotlin
// 构建器模式
class Html {
    private val elements = mutableListOf<String>()
    fun body(block: Body.() -> Unit) {
        elements.add(Body().apply(block).toString())
    }
}
```

---

**基本写法：@DslMarker 限制作用域**
`@DslMarker annotation class <名称>`
```kotlin
// 防止外部接收者访问
@DslMarker
annotation class HtmlDsl
@HtmlDsl
class Body { fun p(text: String) { } }
```

---

**基本写法：invoke 约定**
`operator fun <函数名>.invoke(<参数>): <返回类型>`
```kotlin
// 让对象像函数一样调用
class Config {
    operator fun invoke(name: String, value: String) {
        /* 设置配置 */
    }
}
```

---

## 类型安全构建器

**基本写法：HTML DSL**
```kotlin
html {
    body {
        p("Hello")
        p("World")
    }
}
```
```kotlin
// 类型安全构建器实现
class Html {
    private val children = mutableListOf<Body>()
    fun body(block: Body.() -> Unit) { children.add(Body().apply(block)) }
}
class Body {
    private val paragraphs = mutableListOf<String>()
    fun p(text: String) { paragraphs.add(text) }
}
```

---

**基本写法：Gradle 风格依赖 DSL**
```kotlin
dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib")
    testImplementation("junit:junit:4.13")
}
```
```kotlin
// 实现依赖 DSL
class Dependencies {
    private val list = mutableListOf<String>()
    fun implementation(dep: String) { list.add(dep) }
    fun testImplementation(dep: String) { list.add("test: $dep") }
}
fun dependencies(block: Dependencies.() -> Unit) = Dependencies().apply(block)
```

---

## 中缀调用

**基本写法：infix 中缀函数**
`infix fun <函数名>(<参数>): <返回类型>`
```kotlin
// 定义中缀函数
infix fun Int.toPower(exp: Int): Int = Math.pow(this.toDouble(), exp.toDouble()).toInt()
val result = 2 toPower 10
```

---

**基本写法：to 配对**
`<值1> to <值2>`
```kotlin
// 创建 Pair
val pair = "key" to "value"
```

---

**基本写法：区间操作**
`<开始> .. <结束>`
```kotlin
// 创建区间
for (i in 1..10) { }
val range = 1 until 100
```

---

## 属性委托

**基本写法：lazy 懒加载**
`val <变量>: <类型> by lazy { <初始化> }`
```kotlin
// 懒加载属性
val expensive by lazy { computeExpensive() }
```

---

**基本写法：observable 可观察**
`var <变量>: <类型> by Delegates.observable(<初始值>) { <属性>, <旧值>, <新值> -> }`
```kotlin
// 监听属性变化
var name by Delegates.observable("") { _, old, new ->
    println("$old -> $new")
}
```

---

**基本写法：vetoable 可否决**
`var <变量>: <类型> by Delegates.vetoable(<初始值>) { <属性>, <旧值>, <新值> -> <是否允许> }`
```kotlin
// 可否决属性变化
var age by Delegates.vetoable(0) { _, _, new -> new >= 0 }
```

---

**基本写法：map 委托**
`val <变量>: <类型> by <map>`
```kotlin
// 从 Map 委托属性
class User(map: Map<String, Any?>) {
    val name: String by map
    val age: Int by map
}
```

---

## 自定义委托

**基本写法：ReadOnlyProperty 只读委托**
`class <类名> : ReadOnlyProperty<<所有者>, <类型>> { override fun getValue(...) }`
```kotlin
// 自定义只读委托
class TrimDelegate : ReadOnlyProperty<Any?, String> {
    override fun getValue(thisRef: Any?, property: KProperty<*>): String {
        return property.name.trim()
    }
}
```

---

**基本写法：ReadWriteProperty 读写委托**
`class <类名> : ReadWriteProperty<<所有者>, <类型>> { ... }`
```kotlin
// 自定义读写委托
class Counter : ReadWriteProperty<Any?, Int> {
    private var value = 0
    override fun getValue(thisRef: Any?, property: KProperty<*>): Int = value
    override fun setValue(thisRef: Any?, property: KProperty<*>, value: Int) {
        this.value = value
    }
}
```



<!-- ============ 文档分隔线：014-kotlin/016-KotlinCoroutineAdvanced.md ============ -->

# Kotlin 协程进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Job 与 Deferred

**基本写法：启动协程获取 Job**
`val <变量> = scope.launch { }`
```kotlin
// 启动协程返回 Job
val job = scope.launch { doWork() }
```

---

**基本写法：async 返回 Deferred**
`val <变量> = scope.async { <表达式> }`
```kotlin
// async 启动并返回结果
val deferred = scope.async { compute() }
val r = deferred.await()
```

---

**基本写法：等待多个 Deferred**
`awaitAll(<deferred1>, <deferred2>)`
```kotlin
// 并发等待多个结果
val (a, b) = listOf(d1, d2).awaitAll().let { it[0] to it[1] }
```

---

## Job 生命周期

**基本写法：判断活跃**
`<job>.isActive`
```kotlin
// 判断协程是否活跃
if (job.isActive) { }
```

---

**基本写法：判断完成**
`<job>.isCompleted`
```kotlin
// 判断协程是否完成
if (job.isCompleted) { }
```

---

**基本写法：判断取消**
`<job>.isCancelled`
```kotlin
// 判断协程是否被取消
if (job.isCancelled) { }
```

---

## 取消协程

**基本写法：取消协程**
`<job>.cancel()`
```kotlin
// 取消协程
job.cancel()
```

---

**基本写法：取消并等待**
`<job>.cancelAndJoin()`
```kotlin
// 取消并阻塞等待完成
job.cancelAndJoin()
```

---

**基本写法：响应取消**
`if (!isActive) return`
```kotlin
// 协程内主动检查取消
if (!isActive) return
```

---

**基本写法：确保取消检查**
`currentCoroutineContext().ensureActive()`
```kotlin
// 显式抛出取消异常
currentCoroutineContext().ensureActive()
```

---

## 超时控制

**基本写法：超时抛异常**
`withTimeout(<毫秒>) { }`
```kotlin
// 超时抛 TimeoutCancellationException
withTimeout(1000) { doWork() }
```

---

**基本写法：超时返回 null**
`withTimeoutOrNull(<毫秒>) { }`
```kotlin
// 超时返回 null 不抛异常
val r = withTimeoutOrNull(1000) { doWork() }
```

---

## 启动模式 CoroutineStart

**基本写法：默认立即调度**
`launch(start = CoroutineStart.DEFAULT) { }`
```kotlin
// 立即调度执行
launch(start = CoroutineStart.DEFAULT) { }
```

---

**基本写法：懒加载启动**
`launch(start = CoroutineStart.LAZY) { }`
```kotlin
// 调用 join 或 start 才执行
val job = scope.launch(start = CoroutineStart.LAZY) { }
job.start()
```

---

**基本写法：原子启动**
`launch(start = CoroutineStart.ATOMIC) { }`
```kotlin
// 不可在执行前取消
launch(start = CoroutineStart.ATOMIC) { }
```

---

**基本写法：不调度启动**
`launch(start = CoroutineStart.UNDISPATCHED) { }`
```kotlin
// 在当前线程执行直到第一个挂起点
launch(start = CoroutineStart.UNDISPATCHED) { }
```

---

## 协程作用域

**基本写法：创建作用域**
`CoroutineScope(<上下文>)`
```kotlin
// 创建独立作用域
val scope = CoroutineScope(Dispatchers.Default)
```

---

**基本写法：coroutineScope 子作用域**
`coroutineScope { }`
```kotlin
// 等待所有子协程完成
coroutineScope {
    launch { }
    launch { }
}
```

---

**基本写法：supervisorScope 容错**
`supervisorScope { }`
```kotlin
// 子协程异常不互相影响
supervisorScope {
    launch { }
    launch { }
}
```

---

## 挂起函数

**基本写法：定义挂起函数**
`suspend fun <方法名>() {}`
```kotlin
// 定义挂起函数
suspend fun fetch(): String {
    delay(100)
    return "data"
}
```

---

**基本写法：挂起函数调用**
`<挂起函数>()`
```kotlin
// 在协程中调用挂起函数
suspend fun work() { fetch() }
```

---

## 延迟与挂起

**基本写法：延迟**
`delay(<毫秒>)`
```kotlin
// 非阻塞延迟
delay(500)
```

---

**基本写法：按 Duration 延迟**
`delay(<时长>.<单位>)`
```kotlin
// 使用 Duration 字面量延迟
delay(500.milliseconds)
```

---

## 协程上下文操作

**基本写法：切换调度器**
`withContext(<dispatcher>) { }`
```kotlin
// 切换到 IO 调度器
withContext(Dispatchers.IO) { readFile() }
```

---

**基本写法：组合上下文元素**
`<job> + <dispatcher>`
```kotlin
// 组合 Job 与 Dispatcher
val ctx = Job() + Dispatchers.IO
```

---

## runBlocking 阻塞

**基本写法：阻塞启动协程**
`runBlocking { }`
```kotlin
// 阻塞主线程启动协程
runBlocking { doWork() }
```

---

**基本写法：带调度器**
`runBlocking(<dispatcher>) { }`
```kotlin
// 指定调度器阻塞
runBlocking(Dispatchers.Default) { }
```

---

## select 等待多路

**基本写法：select 多路复用**
`select<<返回类型>> { <分支> }`
```kotlin
// 等待首个就绪结果
val r = select<String> {
    deferred1.onAwait { "a" }
    deferred2.onAwait { "b" }
}
```

---

## SupervisorJob

**基本写法：创建 SupervisorJob**
`SupervisorJob()`
```kotlin
// 子协程失败不影响其他子协程
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
```

---

## 协程命名

**基本写法：命名协程**
`CoroutineName("<名称>")`
```kotlin
// 为协程命名便于调试
launch(CoroutineName("worker")) { }
```



<!-- ============ 文档分隔线：014-kotlin/017-CoroutineDispatcherContext.md ============ -->

# Kotlin 协程调度器与上下文

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 内置调度器

**基本写法：默认调度器**
`Dispatchers.Default`
```kotlin
// CPU 密集任务调度器
launch(Dispatchers.Default) { compute() }
```

---

**基本写法：IO 调度器**
`Dispatchers.IO`
```kotlin
// 阻塞 IO 任务调度器
launch(Dispatchers.IO) { readFile() }
```

---

**基本写法：主线程调度器**
`Dispatchers.Main`
```kotlin
// UI 主线程调度器（需平台依赖）
launch(Dispatchers.Main) { updateUI() }
```

---

**基本写法：不受限调度器**
`Dispatchers.Unconfined`
```kotlin
// 在调用线程执行直到挂起
launch(Dispatchers.Unconfined) { }
```

---

## 自定义调度器

**基本写法：单线程调度器**
`newSingleThreadContext("<名称>")`
```kotlin
// 创建单线程调度器
val dispatcher = newSingleThreadContext("worker")
```

---

**基本写法：固定线程池调度器**
`newFixedThreadPoolContext(<线程数>, "<名称>")`
```kotlin
// 创建固定大小线程池调度器
val dispatcher = newFixedThreadPoolContext(4, "pool")
```

---

**基本写法：基于 Executor**
`<executor>.asCoroutineDispatcher()`
```kotlin
// 复用现有 Executor 作为调度器
val d = Executors.newFixedThreadPool(4).asCoroutineDispatcher()
```

---

## 切换调度器

**基本写法：withContext 切换**
`withContext(<dispatcher>) { }`
```kotlin
// 临时切换调度器
withContext(Dispatchers.IO) { fetchData() }
```

---

**基本写法：launch 指定调度器**
`launch(<dispatcher>) { }`
```kotlin
// 启动时指定调度器
launch(Dispatchers.Default) { heavy() }
```

---

**基本写法：async 指定调度器**
`async(<dispatcher>) { }`
```kotlin
// async 启动并指定调度器
async(Dispatchers.IO) { fetch() }
```

---

## 限流调度器

**基本写法：限制并发数**
`<dispatcher>.limitedParallelism(<并发数>)`
```kotlin
// 限制调度器并发数
val limited = Dispatchers.IO.limitedParallelism(8)
```

---

## CoroutineContext 元素

**基本写法：获取当前上下文**
`currentCoroutineContext()`
```kotlin
// 获取当前协程上下文
val ctx = currentCoroutineContext()
```

---

**基本写法：从上下文取元素**
`<context>[<Key>]`
```kotlin
// 获取当前调度器
val d = currentCoroutineContext()[CoroutineDispatcher]
```

---

**基本写法：获取 Job**
`coroutineContext[Job]`
```kotlin
// 获取当前协程 Job
val job = coroutineContext[Job]
```

---

**基本写法：获取名称**
`coroutineContext[CoroutineName]`
```kotlin
// 获取协程名称
val name = coroutineContext[CoroutineName]?.name
```

---

## 上下文组合与传递

**基本写法：组合上下文元素**
`<ctx1> + <ctx2>`
```kotlin
// Job 与 Dispatcher 组合
val ctx = Job() + Dispatchers.IO + CoroutineName("worker")
```

---

**基本写法：移除上下文元素**
`<ctx>.minusKey(<Key>)`
```kotlin
// 移除 Job 元素
val newCtx = ctx.minusKey(Job)
```

---

**基本写法：fold 遍历**
`<ctx>.fold(<初始>) { <累加>, <元素> -> }`
```kotlin
// 遍历上下文所有元素
ctx.fold(emptyList()) { acc, e -> acc + e }
```

---

## 自定义上下文元素

**基本写法：实现 CoroutineContext.Element**
`class <类>(val <值>) : CoroutineContext.Element { companion object Key }`
```kotlin
// 自定义请求 ID 上下文
class RequestId(val id: String) : CoroutineContext.Element {
    companion object Key : CoroutineContext.Key<RequestId>
    override val key = Key
}
```

---

**基本写法：注入自定义元素**
`launch(<dispatcher> + <元素>) { }`
```kotlin
// 启动时注入请求 ID
launch(Dispatchers.Default + RequestId("r-1")) { }
```

---

## 线程局部变量

**基本写法：CoroutineContext 存 ThreadLocal**
`<threadLocal>.asContextElement(<值>)`
```kotlin
// ThreadLocal 跨挂起传递
val tl = ThreadLocal<String>()
launch(tl.asContextElement("ctx") + Dispatchers.IO) {
    println(tl.get())
}
```

---

## 调度器异常处理

**基本写法：CoroutineExceptionHandler**
`CoroutineExceptionHandler { <ctx>, <异常> -> }`
```kotlin
// 自定义协程异常处理器
val handler = CoroutineExceptionHandler { _, e ->
    println("caught: $e")
}
launch(Dispatchers.Default + handler) { }
```

---

## 阻塞与挂起桥接

**基本写法：阻塞调用转挂起**
`<dispatcher>.runIsolated { }`
```kotlin
// 在调度器上运行可阻塞代码
runBlocking(Dispatchers.IO) { blockingCall() }
```

---

**基本写法：runInterruptible 阻塞转可取消**
`runInterruptible { <阻塞调用> }`
```kotlin
// 将阻塞代码包装为可取消挂起
suspend fun read(): String = runInterruptible { Files.readString(path) }
```

---

## 调度器关闭

**基本写法：关闭自定义调度器**
`<dispatcher>.close()`
```kotlin
// 关闭单线程调度器释放线程
val dispatcher = newSingleThreadContext("w")
dispatcher.close()
```

---

## 父子上下文继承

**基本写法：复制父上下文**
`<parentCtx> + <新元素>`
```kotlin
// 子协程继承父上下文并覆盖
val childCtx = coroutineContext + Dispatchers.IO
launch(childCtx) { }
```



<!-- ============ 文档分隔线：014-kotlin/018-CoroutineExceptionHandling.md ============ -->

# Kotlin 协程异常处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 异常传播机制

**基本写法：launch 异常向上抛**
`launch { throw <异常> }`
```kotlin
// launch 异常传播到父协程
scope.launch { throw RuntimeException("fail") }
```

---

**基本写法：async 异常不立即抛**
`async { throw <异常> }`
```kotlin
// async 在 await 时才抛异常
val d = scope.async { throw RuntimeException("fail") }
d.await() // 此处抛出
```

---

## try-catch 捕获

**基本写法：捕获挂起函数异常**
`try { <挂起调用> } catch (<异常>) { }`
```kotlin
// 捕获协程内异常
try {
    deferred.await()
} catch (e: Exception) {
    println(e)
}
```

---

**基本写法：捕获 launch 异常需 ExceptionHandler**
`launch(<handler>) { }`
```kotlin
// launch 异常不能直接 try-catch
val handler = CoroutineExceptionHandler { _, e -> println(e) }
scope.launch(handler) { throw RuntimeException("fail") }
```

---

## CoroutineExceptionHandler

**基本写法：定义异常处理器**
`val <变量> = CoroutineExceptionHandler { <ctx>, <异常> -> }`
```kotlin
// 创建异常处理器
val handler = CoroutineExceptionHandler { ctx, e ->
    println("ctx=${ctx[CoroutineName]} err=$e")
}
```

---

**基本写法：应用于根协程**
`launch(<dispatcher> + <handler>) { }`
```kotlin
// 仅根协程生效
scope.launch(Dispatchers.Default + handler) { }
```

---

## SupervisorJob 容错

**基本写法：SupervisorJob 隔离子协程**
`CoroutineScope(SupervisorJob()) { }`
```kotlin
// 子协程失败不影响兄弟
val scope = CoroutineScope(SupervisorJob())
scope.launch { throw RuntimeException() }
scope.launch { /* 仍会执行 */ }
```

---

**基本写法：supervisorScope**
`supervisorScope { }`
```kotlin
// 作用域内子协程互不影响
supervisorScope {
    launch { throw RuntimeException() }
    launch { /* 正常执行 */ }
}
```

---

## CancellationException

**基本写法：取消异常需重新抛出**
`catch (e: CancellationException) { throw e }`
```kotlin
// 捕获取消异常必须重抛
try { doWork() }
catch (e: CancellationException) { throw e }
catch (e: Exception) { handle(e) }
```

---

**基本写法：自定义取消消息**
`throw CancellationException("<消息>")`
```kotlin
// 主动抛出取消异常
throw CancellationException("manual cancel")
```

---

## finally 资源清理

**基本写法：finally 清理**
`try { } finally { <清理> }`
```kotlin
// 协程取消时清理资源
try { doWork() }
finally { closeResource() }
```

---

**基本写法：NonCancellable 中执行清理**
`withContext(NonCancellable) { <清理> }`
```kotlin
// 不可取消上下文中执行挂起清理
try { doWork() }
finally {
    withContext(NonCancellable) { delay(100); close() }
}
```

---

## 异常聚合

**基本写法：await 抛出首个异常**
`try { <deferred>.await() } catch (<异常>) { }`
```kotlin
// async 等待异常抛出
try { deferred.await() } catch (e: Exception) { }
```

---

**基本写法：多个 async 异常聚合**
`awaitAll(<d1>, <d2>)`
```kotlin
// 抛出 CompositeException
supervisorScope {
    val d1 = async { throw IOException() }
    val d2 = async { throw RuntimeException() }
    try { listOf(d1, d2).awaitAll() } catch (e: Exception) { }
}
```

---

## 恢复协程

**基本写法：恢复挂起协程值**
`runCatching { <挂起调用> }.getOrDefault(<默认>)`
```kotlin
// 异常时返回默认值
val r = runCatching { deferred.await() }.getOrDefault("fallback")
```

---

## recover 异常恢复

**基本写法：recoverCatching 恢复**
`runCatching { }.recoverCatching { }`
```kotlin
// 捕获后转换结果
val r = runCatching { fetch() }
    .recoverCatching { e -> "default" }
    .getOrThrow()
```

---

## 检查与断言

**基本写法：抛出 IllegalStateException**
`check(<条件>) { "<消息>" }`
```kotlin
// 条件不满足抛异常
check(state == READY) { "not ready" }
```

---

**基本写法：参数校验**
`require(<条件>) { "<消息>" }`
```kotlin
// 参数不合法抛 IllegalArgumentException
require(id > 0) { "invalid id" }
```

---

## 异常处理器优先级

**基本写法：父协程优先于 handler**
`launch(<handler>) { launch { throw <异常> } }`
```kotlin
// 子协程异常先传播到父，父失败才走 handler
scope.launch(handler) {
    launch { throw RuntimeException() }
}
```

---

## 取消与异常关系

**基本写法：取消触发 CancellationException**
`<job>.cancel("<原因>")`
```kotlin
// 带原因的取消
job.cancel("timeout")
```

---

**基本写法：getCancellationCause 获取原因**
`<job>.getCancellationCause()`
```kotlin
// 获取取消异常原因
val cause = job.getCancellationCause()
```

---

## 异常日志记录

**基本写法：记录协程异常**
`<handler> = CoroutineExceptionHandler { _, e -> log.error("", e) }`
```kotlin
// 处理器中记录日志
val handler = CoroutineExceptionHandler { ctx, e ->
    log.error("coroutine ${ctx[CoroutineName]} failed", e)
}
```



<!-- ============ 文档分隔线：014-kotlin/019-FlowAdvanced.md ============ -->

# Kotlin Flow 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Flow 创建

**基本写法：flow 构建器**
`flow { <emit 值> }`
```kotlin
// 手动发射值的冷流
fun nums() = flow {
    for (i in 1..3) emit(i)
}
```

---

**基本写法：flowOf 固定值**
`flowOf(<值1>, <值2>)`
```kotlin
// 创建固定值 Flow
val f = flowOf(1, 2, 3)
```

---

**基本写法：asFlow 转换**
`<集合>.asFlow()`
```kotlin
// 集合转 Flow
val f = listOf(1, 2, 3).asFlow()
```

---

**基本写法：区间转 Flow**
`(<区间>).asFlow()`
```kotlin
// 区间转 Flow
val f = (1..10).asFlow()
```

---

## 中间操作符

**基本写法：map 转换**
`<flow>.map { <转换> }`
```kotlin
// 元素映射
nums().map { it * 2 }
```

---

**基本写法：filter 过滤**
`<flow>.filter { <条件> }`
```kotlin
// 过滤元素
nums().filter { it > 1 }
```

---

**基本写法：transform 自定义**
`<flow>.transform { <emit> }`
```kotlin
// 一个输入可发射多个输出
nums().transform { emit(it); emit(it * 10) }
```

---

**基本写法：take 取前 N**
`<flow>.take(<数量>)`
```kotlin
// 取前 N 个元素
nums().take(2)
```

---

**基本写法：distinctUntilChanged 去重**
`<flow>.distinctUntilChanged()`
```kotlin
// 连续重复值去重
nums().distinctUntilChanged()
```

---

## 末端操作符

**基本写法：collect 收集**
`<flow>.collect { <处理> }`
```kotlin
// 收集流元素
nums().collect { println(it) }
```

---

**基本写法：collectLatest 取消旧**
`<flow>.collectLatest { }`
```kotlin
// 新值到来取消旧处理
nums().collectLatest { process(it) }
```

---

**基本写法：toList 收集为列表**
`<flow>.toList()`
```kotlin
// 转换为 List
val list = nums().toList()
```

---

**基本写法：first 取首个**
`<flow>.first()`
```kotlin
// 取第一个元素
val v = nums().first()
```

---

**基本写法：single 取唯一**
`<flow>.single()`
```kotlin
// 流必须只有一个元素
val v = nums().single()
```

---

## 错误处理

**基本写法：catch 捕获上游异常**
`<flow>.catch { <emit 兜底> }`
```kotlin
// 上游异常时发射兜底值
nums().catch { emit(-1) }.collect { }
```

---

**基本写法：onEach 中 try-catch**
`<flow>.onEach { try { } catch (<异常>) { } }`
```kotlin
// 元素处理时捕获异常
nums().onEach { runCatching { } }.collect { }
```

---

**基本写法：retry 重试**
`<flow>.retry(<次数>) { }`
```kotlin
// 失败重试 3 次
nums().retry(3).collect { }
```

---

**基本写法：retryWhen 条件重试**
`<flow>.retryWhen { <异常>, <次数> -> <条件> }`
```kotlin
// 按条件重试
nums().retryWhen { e, n -> n < 3 }.collect { }
```

---

## 完成回调

**基本写法：onCompletion**
`<flow>.onCompletion { <异常> -> }`
```kotlin
// 流结束时回调
nums().onCompletion { e -> println("done $e") }.collect { }
```

---

**基本写法：finally 清理**
`try { <flow>.collect { } } finally { }`
```kotlin
// finally 中清理资源
try { nums().collect { } }
finally { close() }
```

---

## 线程调度

**基本写法：flowOn 切换上游**
`<flow>.flowOn(<dispatcher>)`
```kotlin
// 上游切换到 IO
nums().flowOn(Dispatchers.IO).collect { }
```

---

**基本写法：withContext 切换下游**
`<flow>.collect { withContext(<dispatcher>) { } }`
```kotlin
// 下游 collect 切换线程
nums().collect { withContext(Dispatchers.Main) { update(it) } }
```

---

## 背压处理

**基本写法：buffer 缓冲**
`<flow>.buffer(<容量>)`
```kotlin
// 缓冲解决生产消费速度不匹配
nums().buffer().collect { }
```

---

**基本写法：conflate 合并**
`<flow>.conflate()`
```kotlin
// 跳过中间值只处理最新
nums().conflate().collect { }
```

---

**基本写法：collectLatest 取消旧处理**
`<flow>.collectLatest { }`
```kotlin
// 处理慢时新值到来取消旧
nums().collectLatest { process(it) }
```

---

## 冷流与热流

**基本写法：冷流每次 collect 重新执行**
`fun <冷流>() = flow { }`
```kotlin
// 每个 collector 触发独立执行
fun cold() = flow { emit(System.currentTimeMillis()) }
```

---

## SharedFlow 热流

**基本写法：创建 SharedFlow**
`MutableSharedFlow<<类型>>()`
```kotlin
// 创建可变 SharedFlow
val sf = MutableSharedFlow<Int>()
```

---

**基本写法：发射值**
`<sharedFlow>.emit(<值>)` 或 `<sharedFlow>.tryEmit(<值>)`
```kotlin
// 发射值到所有订阅者
sf.emit(1)
```

---

**基本写法：配置 replay 缓存**
`MutableSharedFlow<Int>(replay = <数量>)`
```kotlin
// 新订阅者收到最近 2 个值
val sf = MutableSharedFlow<Int>(replay = 2)
```

---

**基本写法：转换为只读**
`<sharedFlow>.asSharedFlow()`
```kotlin
// 暴露只读 SharedFlow
val shared: SharedFlow<Int> = sf.asSharedFlow()
```

---

## StateFlow 状态流

**基本写法：创建 StateFlow**
`MutableStateFlow(<初始值>)`
```kotlin
// 创建状态流带初始值
val state = MutableStateFlow(0)
```

---

**基本写法：更新值**
`<stateFlow>.value = <新值>`
```kotlin
// 直接赋值更新状态
state.value = 1
```

---

**基本写法：原子更新**
`<stateFlow>.update { <新值> }`
```kotlin
// 原子更新当前值
state.update { it + 1 }
```

---

**基本写法：转只读 StateFlow**
`<stateFlow>.asStateFlow()`
```kotlin
// 暴露只读 StateFlow
val s: StateFlow<Int> = state.asStateFlow()
```

---

## Flow 转 StateFlow

**基本写法：冷流转 StateFlow**
`<flow>.stateIn(<scope>, <启动策略>, <初始值>)`
```kotlin
// 冷流共享化为 StateFlow
val s = flow.stateIn(
    scope, SharingStarted.WhileSubscribed(5000), 0
)
```

---

## 组合操作符

**基本写法：combine 合并**
`combine(<flow1>, <flow2>) { a, b -> <合并> }`
```kotlin
// 任一流变化都合并最新值
combine(f1, f2) { a, b -> a + b }.collect { }
```

---

**基本写法：zip 配对**
`<flow1>.zip(<flow2>) { a, b -> <合并> }`
```kotlin
// 严格配对两流元素
f1.zip(f2) { a, b -> a to b }.collect { }
```

---

**基本写法：flattenMerge 展平合并**
`<flow>.map { <内流> }.flattenMerge()`
```kotlin
// 展平多个内部 Flow 并发收集
flows.flattenMerge().collect { }
```

---

## 启动收集

**基本写法：launchIn 启动收集**
`<flow>.launchIn(<scope>)`
```kotlin
// 在指定作用域启动收集
nums().onEach { }.launchIn(scope)
```



<!-- ============ 文档分隔线：014-kotlin/020-KotlinChannel.md ============ -->

# Kotlin Channel 通道

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Channel

**基本写法：创建无缓冲通道**
`Channel<<类型>>()`
```kotlin
// 创建无缓冲 rendezvous 通道
val ch = Channel<Int>()
```

---

**基本写法：创建带缓冲通道**
`Channel<<类型>>(<容量>)`
```kotlin
// 创建容量为 10 的缓冲通道
val ch = Channel<Int>(10)
```

---

**基本写法：创建无限缓冲通道**
`Channel<<类型>>(Channel.UNLIMITED)`
```kotlin
// 容量无上限的链表缓冲
val ch = Channel<Int>(Channel.UNLIMITED)
```

---

**基本写法：创建带满策略通道**
`Channel<<类型>>(<容量>, <溢出策略>)`
```kotlin
// 满时丢弃最新值
val ch = Channel<Int>(10, BufferOverflow.DROP_LATEST)
```

---

## 发送与接收

**基本写法：发送值**
`<channel>.send(<值>)`
```kotlin
// 挂起发送值到通道
ch.send(1)
```

---

**基本写法：非阻塞发送**
`<channel>.trySend(<值>)`
```kotlin
// 尝试发送不挂起
val r = ch.trySend(1)
```

---

**基本写法：接收值**
`<channel>.receive()`
```kotlin
// 挂起接收通道值
val v = ch.receive()
```

---

**基本写法：非阻塞接收**
`<channel>.tryReceive()`
```kotlin
// 尝试接收不挂起
val r = ch.tryReceive()
```

---

## 关闭通道

**基本写法：关闭通道**
`<channel>.close()`
```kotlin
// 关闭通道不再接收新值
ch.close()
```

---

**基本写法：判断关闭**
`<channel>.isClosedForSend | <channel>.isClosedForReceive`
```kotlin
// 判断发送或接收侧是否关闭
if (ch.isClosedForSend) { }
```

---

## 遍历接收

**基本写法：for 循环接收**
`for (<变量> in <channel>) { }`
```kotlin
// 持续接收直到关闭
for (v in ch) { println(v) }
```

---

**基本写法：consumeEach 接收**
`<channel>.consumeEach { }`
```kotlin
// 消费全部并关闭通道
ch.consumeEach { println(it) }
```

---

## produce 生产者

**基本写法：创建生产者**
`produce { <send> }`
```kotlin
// 启动协程生产并返回 ReceiveChannel
val ch = GlobalScope.produce {
    for (i in 1..5) send(i)
}
```

---

**基本写法：指定调度器**
`produce(<dispatcher>) { }`
```kotlin
// 生产者在 IO 调度器
val ch = scope.produce(Dispatchers.IO) { send(read()) }
```

---

## actor 消费者

**基本写法：创建 actor**
`actor<<类型>> { for (<变量> in channel) { } }`
```kotlin
// 启动协程消费 SendChannel
val a = scope.actor<Int> {
    for (v in channel) println(v)
}
a.send(1)
```

---

## Channel 与 Flow

**基本写法：Channel 转 Flow**
`<channel>.receiveAsFlow()`
```kotlin
// 将 Channel 转为 Flow 便于操作
val flow = ch.receiveAsFlow()
```

---

**基本写法：Flow 转 Channel**
`<flow>.produceIn(<scope>)`
```kotlin
// 将 Flow 转为 ReceiveChannel
val rc = flow.produceIn(scope)
```

---

## BufferOverflow 溢出策略

**基本写法：挂起等待**
`BufferOverflow.SUSPEND`
```kotlin
// 满时挂起发送者
val ch = Channel<Int>(2, BufferOverflow.SUSPEND)
```

---

**基本写法：丢弃最旧**
`BufferOverflow.DROP_OLDEST`
```kotlin
// 满时丢弃队列最旧值
val ch = Channel<Int>(2, BufferOverflow.DROP_OLDEST)
```

---

**基本写法：丢弃最新**
`BufferOverflow.DROP_LATEST`
```kotlin
// 满时丢弃新发送的值
val ch = Channel<Int>(2, BufferOverflow.DROP_LATEST)
```

---

## select 多路接收

**基本写法：select 等待多通道**
`select<<类型>> { <channel>.onReceive { } }`
```kotlin
// 从多个通道获取首个就绪值
val r = select<Int> {
    ch1.onReceive { "from ch1: $it" }
    ch2.onReceive { "from ch2: $it" }
}
```

---

**基本写法：select 发送**
`select<<类型>> { <channel>.onSend(<值>) { } }`
```kotlin
// 向多个通道首个就绪者发送
select<Unit> {
    ch1.onSend(1) { }
    ch2.onSend(1) { }
}
```

---

## BroadcastChannel（已弃用改用 SharedFlow）

**基本写法：Channel 转 SharedFlow**
`<channel>.broadcast(<容量>)`
```kotlin
// 旧版广播通道
val bc = ch.broadcast(10)
```

---

## Channel 容量常量

**基本写法：无缓冲**
`Channel.RENDEZVOUS`
```kotlin
// 发送接收同步会合
val ch = Channel<Int>(Channel.RENDEZVOUS)
```

---

**基本写法：合并缓冲**
`Channel.CONFLATED`
```kotlin
// 仅保留最新值
val ch = Channel<Int>(Channel.CONFLATED)
```

---

## Channel 取消

**基本写法：取消通道**
`<channel>.cancel()`
```kotlin
// 取消通道并关闭
ch.cancel()
```

---

**基本写法：带原因取消**
`<channel>.cancel(<异常>)`
```kotlin
// 携带异常取消通道
ch.cancel(CancellationException("done"))
```

---

## fan-out 多消费者

**基本写法：多个消费者分摊**
`for (i in 1..N) launch { for (v in <channel>) { } }`
```kotlin
// 多个协程分摊通道元素
repeat(3) {
    launch { for (v in ch) process(v) }
}
```

---

## fan-in 多生产者

**基本写法：多协程向同一通道发送**
`launch { <channel>.send(<值>) }`
```kotlin
// 多协程合并到同一通道
val ch = Channel<Int>()
launch { ch.send(1) }
launch { ch.send(2) }
```



<!-- ============ 文档分隔线：014-kotlin/021-KotlinInlineClass.md ============ -->

# Kotlin 内联类与 Value Class

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 定义内联类

**基本写法：定义 value class**
`@JvmInline value class <类名>(val <属性>: <类型>)`
```kotlin
// 定义内联值类避免装箱开销
@JvmInline
value class UserId(val value: Long)
```

---

**基本写法：字符串包装类**
`@JvmInline value class <类名>(val <属性>: String)`
```kotlin
// 包装字符串为强类型
@JvmInline
value class Email(val value: String)
```

---

## 使用内联类

**基本写法：创建实例**
`<类名>(<值>)`
```kotlin
// 创建内联类实例
val id = UserId(42L)
```

---

**基本写法：访问底层值**
`<实例>.<属性>`
```kotlin
// 取出底层值
val raw: Long = id.value
```

---

**基本写法：作为参数**
`fun <方法>(<参数>: <内联类>) {}`
```kotlin
// 函数签名使用强类型
fun find(id: UserId) = repo.findById(id.value)
```

---

## 内联类方法

**基本写法：定义方法**
`@JvmInline value class <类>(val v: <类型>) { fun <方法>() {} }`
```kotlin
// 内联类可定义方法
@JvmInline
value class Meter(val value: Double) {
    fun toKm() = Kilometer(value / 1000)
}
```

---

**基本写法：扩展函数**
`fun <内联类>.<方法>() {}`
```kotlin
// 为内联类添加扩展
fun Meter.toCm() = value * 100
```

---

## 内联类与接口

**基本写法：实现接口**
`@JvmInline value class <类>(val v: <类型>) : <接口> {}`
```kotlin
// 内联类实现接口
interface Printable { fun print() }
@JvmInline
value class Name(val value: String) : Printable {
    override fun print() = println(value)
}
```

---

## 泛型与内联类

**基本写法：泛型内联类**
`@JvmInline value class <类><<T>>(val v: <T>)`
```kotlin
// 泛型内联类
@JvmInline
value class Box<T>(val value: T)
```

---

## nullable 内联类

**基本写法：可空类型字段**
`@JvmInline value class <类>(val v: <类型>?)`
```kotlin
// 内部可空时装箱为包装类
@JvmInline
value class Phone(val value: String?)
```

---

## underlying 字段类型

**基本写法：数字底层类型**
`@JvmInline value class <类>(val v: <数字类型>)`
```kotlin
// 底层为 Int 编译期不装箱
@JvmInline
value class Age(val value: Int)
```

---

## 与 Java 互操作

**基本写法：Java 调用需传底层类型**
`<Java 方法>(<底层值>);`
```kotlin
// Java 中调用需传 Long 而非 UserId
// Kotlin 端添加 @JvmName 避免签名冲突
@JvmInline
value class UserId(val value: Long) {
    @JvmName("of") companion object { fun of(v: Long) = UserId(v) }
}
```

---

## value class 与 data class 区别

**基本写法：何时用 value class**
`@JvmInline value class <类>(val v: <单字段>)`
```kotlin
// 单字段且无需 equals 时使用 value class
@JvmInline value class Token(val value: String)
```

---

**基本写法：何时用 data class**
`data class <类>(val <字段1>, val <字段2>)`
```kotlin
// 多字段或需 equals 时使用 data class
data class Point(val x: Int, val y: Int)
```

---

## 内联类集合

**基本写法：内联类作为 Map 键**
`Map<<内联类>, <值>>`
```kotlin
// 内联类作为 Map 键避免装箱
val map: Map<UserId, String> = mapOf(UserId(1) to "Alice")
```

---

## Sealed 结合内联类

**基本写法：内联类配合密封类**
`sealed class <基> | @JvmInline value class <子>: <基>`
```kotlin
// 内联类作为密封类子类
sealed interface Id
@JvmInline value class LongId(val v: Long) : Id
@JvmInline value class Uuid(val v: String) : Id
```

---

## 验证构造

**基本写法：init 校验**
`@JvmInline value class <类>(val v: <类型>) { init { require(<条件>) } }`
```kotlin
// 构造时校验合法性
@JvmInline
value class NonBlank(val value: String) {
    init { require(value.isNotBlank()) { "blank" } }
}
```

---

## 性能优化场景

**基本写法：ID 类型避免装箱**
`@JvmInline value class <Id>(val v: <Long>)`
```kotlin
// 大量 ID 时用内联类避免 Long 装箱
@JvmInline value class OrderId(val v: Long)
val ids = listOf(OrderId(1), OrderId(2)) // 数组无装箱
```

---

## toString 与 equals

**基本写法：自定义 toString**
`override fun toString() = "<格式>"`
```kotlin
// 自定义字符串表示
@JvmInline
value class UserId(val value: Long) {
    override fun toString() = "User($value)"
}
```

---

## 内联类限制

**基本写法：只能有单构造属性**
`@JvmInline value class <类>(val <属性>: <类型>)`
```kotlin
// 仅支持单个 val 属性作为底层值
@JvmInline value class Score(val value: Int)
```

---

**基本写法：内部不能有可变状态**
`@JvmInline value class <类>(val v: <类型>) { var <变量> } // 禁止`
```kotlin
// 内联类不能有可变 var 属性
@JvmInline value class Score(val value: Int)
```



<!-- ============ 文档分隔线：014-kotlin/022-KotlinMultiplatform.md ============ -->

# Kotlin Multiplatform

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 项目结构

**基本写法：build.gradle.kts 配置**
`kotlin { androidTarget(); jvm(); iosX64(); iosArm64() }`
```kotlin
// 声明多平台目标
kotlin {
    androidTarget()
    jvm()
    iosX64(); iosArm64(); iosSimulatorArm64()
}
```

---

**基本写法：层级 sourceSets**
`val commonMain by getting; val androidMain by getting`
```kotlin
// 公共代码与平台代码目录
kotlin {
    sourceSets {
        val commonMain by getting
        val androidMain by getting
        val iosMain by creating { dependsOn(commonMain) }
    }
}
```

---

## expect/actual 机制

**基本写法：声明 expect**
`expect fun <方法>(): <类型>`
```kotlin
// commonMain 中声明平台差异函数
expect fun currentTimeMillis(): Long
```

---

**基本写法：实现 actual**
`actual fun <方法>(): <类型> { }`
```kotlin
// androidMain 中实现
actual fun currentTimeMillis(): Long = System.currentTimeMillis()
```

---

**基本写法：expect 类**
`expect class <类名>()`
```kotlin
// common 声明平台类
expect class DateFormatter() {
    fun format(millis: Long): String
}
```

---

**基本写法：actual 类**
`actual class <类名> { }`
```kotlin
// 平台实现具体类
actual class DateFormatter {
    actual fun format(millis: Long): String = java.text.SimpleDateFormat().format(Date(millis))
}
```

---

**基本写法：expect 属性**
`expect val <属性>: <类型>`
```kotlin
// 声明平台相关常量
expect val platformName: String
```

---

## 跨平台依赖

**基本写法：commonMain 依赖**
`commonMain { dependencies { implementation("<坐标>") } }`
```kotlin
// 公共代码使用跨平台库
commonMain.dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.0")
}
```

---

**基本写法：平台专属依赖**
`androidMain { dependencies { implementation("<坐标>") } }`
```kotlin
// 仅 Android 平台依赖
androidMain.dependencies {
    implementation("androidx.core:core-ktx:1.13.0")
}
```

---

## 平台特定调用

**基本写法：Android 调用**
`import android.util.Log; Log.d(...)`
```kotlin
// androidMain 中调用 Android API
android.util.Log.d("tag", "msg")
```

---

**基本写法：iOS 调用**
`import platform.Foundation.NSDate`
```kotlin
// iosMain 中调用 Objective-C API
import platform.Foundation.NSDate
val now = NSDate()
```

---

**基本写法：JVM 调用**
`import java.io.File`
```kotlin
// jvmMain 中调用 JVM API
import java.io.File
val f = File("a.txt")
```

---

## 跨平台 IO

**基本写法：使用 okio 跨平台 IO**
`okio.FileSystem.SYSTEM.read(<path>) { }`
```kotlin
// okio 提供跨平台文件 IO
import okio.FileSystem
FileSystem.SYSTEM.read(path) { readUtf8() }
```

---

## kotlinx 库

**基本写法：kotlinx-datetime**
`Clock.System.now()`
```kotlin
// 跨平台日期时间
import kotlinx.datetime.Clock
val now = Clock.System.now()
```

---

**基本写法：kotlinx.coroutines 协程**
`runBlocking { }`
```kotlin
// 跨平台协程
import kotlinx.coroutines.runBlocking
runBlocking { doWork() }
```

---

**基本写法：kotlinx-serialization**
`@Serializable class <类>`
```kotlin
// 跨平台序列化
import kotlinx.serialization.Serializable
@Serializable
data class User(val name: String)
```

---

## expect/actual 扩展函数

**基本写法：扩展 expect**
`expect fun <<T>> <类型>.<方法>(): <返回>`
```kotlin
// 声明跨平台扩展函数
expect fun Long.toDateString(): String
```

---

## 共享业务逻辑

**基本写法：commonMain 编写业务**
`class <仓库> { suspend fun <方法>() = <实现> }`
```kotlin
// 共享业务代码不依赖平台
class UserRepository {
    suspend fun load(): User = api.fetch()
}
```

---

## 构建与运行

**基本写法：构建所有目标**
`./gradlew build`
```bash
# 编译所有平台目标
./gradlew build
```

---

**基本写法：构建特定目标**
`./gradlew :shared:assembleAndroid`
```bash
# 仅构建 Android 目标
./gradlew :shared:assembleAndroid
```

---

**基本写法：发布 iOS Framework**
`./gradlew :shared:linkDebugFrameworkIosArm64`
```bash
# 生成 iOS Framework
./gradlew :shared:linkDebugFrameworkIosArm64
```

---

## CocoaPods 集成

**基本写法：cocoapods 配置**
`cocoapods { summary = "<描述>"; version = "1.0" }`
```kotlin
// 配置 iOS CocoaPods 集成
kotlin {
    cocoapods {
        summary = "Shared Library"
        version = "1.0"
        ios.deploymentTarget = "14.0"
    }
}
```

---

## 目标简写

**基本写法：iOS 目标简写**
`ios() // 等价 iosX64 + iosArm64 + iosSimulatorArm64`
```kotlin
// 一行配置所有 iOS 目标
kotlin { ios() }
```

---

**基本写法：macos 目标**
`macosX64(); macosArm64()`
```kotlin
// macOS 目标
kotlin { macosX64(); macosArm64() }
```

---

## 中间层 sourceSet

**基本写法：iOS 共享代码**
`val iosMain by creating { dependsOn(commonMain) }`
```kotlin
// iOS 多架构共享代码
val iosMain by creating { dependsOn(commonMain) }
val iosX64Main by getting { dependsOn(iosMain) }
val iosArm64Main by getting { dependsOn(iosMain) }
```



<!-- ============ 文档分隔线：014-kotlin/023-KotlinKtor.md ============ -->

# Kotlin Ktor 服务端

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建服务器

**基本写法：embeddedServer 启动**
`embeddedServer(Netty, port = <端口>) { }.start(wait = true)`
```kotlin
// 启动 Ktor Netty 服务器
embeddedServer(Netty, port = 8080) {
    routing { get("/") { call.respondText("hello") } }
}.start(wait = true)
```

---

**基本写法：指定 host**
`embeddedServer(Netty, port = <端口>, host = "<主机>") { }`
```kotlin
// 指定监听主机
embeddedServer(Netty, port = 8080, host = "0.0.0.0") { }
```

---

## 路由配置

**基本写法：定义 GET 路由**
`get("<路径>") { }`
```kotlin
// 注册 GET 请求处理
get("/users") { call.respond(users) }
```

---

**基本写法：POST 路由**
`post("<路径>") { }`
```kotlin
// 注册 POST 请求处理
post("/users") { call.respond(create()) }
```

---

**基本写法：路径参数**
`get("<路径>/{<参数>}") { }`
```kotlin
// 获取路径参数
get("/users/{id}") {
    val id = call.parameters["id"]
}
```

---

**基本写法：route 分组**
`route("<前缀>") { }`
```kotlin
// 路由分组
routing {
    route("/api") {
        get("/v1") { }
        post("/v2") { }
    }
}
```

---

## 请求处理

**基本写法：接收 JSON**
`call.receive<<类型>>()`
```kotlin
// 反序列化请求体
val user = call.receive<User>()
```

---

**基本写法：响应 JSON**
`call.respond(<对象>)`
```kotlin
// 序列化对象为 JSON 响应
call.respond(User("Alice"))
```

---

**基本写法：响应纯文本**
`call.respondText("<文本>")`
```kotlin
// 返回纯文本响应
call.respondText("hello", ContentType.Text.Plain)
```

---

**基本写法：查询参数**
`call.request.queryParameters["<名称>"]`
```kotlin
// 获取查询字符串参数
val q = call.request.queryParameters["q"]
```

---

## ContentNegotiation 插件

**基本写法：安装 JSON 插件**
`install(ContentNegotiation) { json() }`
```kotlin
// 启用 JSON 序列化
install(ContentNegotiation) {
    json(Json { ignoreUnknownKeys = true })
}
```

---

## StatusPages 异常处理

**基本写法：异常映射**
`install(StatusPages) { exception<异常> { } }`
```kotlin
// 异常转换为 HTTP 状态码
install(StatusPages) {
    exception<NotFoundException> { call, _ ->
        call.respond(HttpStatusCode.NotFound)
    }
}
```

---

## Authentication 认证

**基本写法：Basic 认证**
`install(Authentication) { basic { } }`
```kotlin
// 启用 Basic 认证
install(Authentication) {
    basic("auth") {
        realm = "api"
        validate { cred -> if (check(cred)) UserIdPrincipal(cred.name) else null }
    }
}
```

---

**基本写法：路由应用认证**
`authenticate("<名称>") { }`
```kotlin
// 路由级应用认证
authenticate("auth") {
    get("/me") { call.respond(user) }
}
```

---

**基本写法：JWT 认证**
`install(Authentication) { jwt { } }`
```kotlin
// JWT 认证配置
install(Authentication) {
    jwt("jwt") {
        verifier(jwk)
        realm = "api"
        validate { cred -> UserIdPrincipal(cred.payload.subject) }
    }
}
```

---

## Sessions 会话

**基本写法：启用会话**
`install(Sessions) { cookie<<类型>>("<名称>") }`
```kotlin
// Cookie 会话
install(Sessions) {
    cookie<UserSession>("SESSION")
}
```

---

**基本写法：设置会话**
`call.sessions.set(<实例>)`
```kotlin
// 写入会话数据
call.sessions.set(UserSession(id = "1"))
```

---

**基本写法：获取会话**
`call.sessions.get<<类型>>()`
```kotlin
// 读取会话数据
val s = call.sessions.get<UserSession>()
```

---

## 静态资源

**基本写法：静态文件**
`staticFiles("<路径>", <文件对象>)`
```kotlin
// 提供静态文件服务
staticFiles("/static", File("public"))
```

---

**基本写法：静态默认资源**
`defaultResource("<文件>")`
```kotlin
// 从资源目录提供静态文件
staticResources("/static") {
    defaultResource("index.html")
}
```

---

## WebSockets

**基本写法：启用 WebSocket**
`install(WebSockets)`
```kotlin
// 安装 WebSocket 插件
install(WebSockets)
```

---

**基本写法：定义 WebSocket 路由**
`webSocket("<路径>") { }`
```kotlin
// WebSocket 端点
webSocket("/chat") {
    for (frame in incoming) {
        val text = frame as Frame.Text
        send(Frame.Text(text.readText()))
    }
}
```

---

**基本写法：发送消息**
`send(Frame.Text("<消息>"))`
```kotlin
// 发送文本帧
send(Frame.Text("hello"))
```

---

**基本写法：接收消息**
`incoming.receive() as Frame.Text`
```kotlin
// 接收文本帧
val text = (incoming.receive() as Frame.Text).readText()
```

---

## CORS 跨域

**基本写法：启用 CORS**
`install(CORS) { anyHost() }`
```kotlin
// 配置跨域
install(CORS) {
    anyHost()
    allowHeader(HttpHeaders.ContentType)
}
```

---

## 部署命令

**基本写法：构建 FatJar**
`./gradlew buildFatJar`
```bash
# 构建包含所有依赖的 FatJar
./gradlew :app:buildFatJar
```

---

**基本写法：运行应用**
`java -jar <jar>`
```bash
# 运行打包后的应用
java -jar build/libs/app-all.jar
```

---

**基本写法：Docker 运行**
`docker build -t <名称> .`
```bash
# 构建 Docker 镜像
docker build -t ktor-app .
docker run -p 8080:8080 ktor-app
```



<!-- ============ 文档分隔线：014-kotlin/024-KotlinKtorClient.md ============ -->

# Kotlin Ktor 客户端

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建客户端

**基本写法：创建 HttpClient**
`HttpClient(<引擎>)`
```kotlin
// 创建 HttpClient
val client = HttpClient(CIO)
```

---

**基本写法：带配置创建**
`HttpClient(<引擎>) { }`
```kotlin
// 配置引擎参数
val client = HttpClient(CIO) {
    engine { requestTimeout = 5000 }
}
```

---

**基本写法：OkHttp 引擎**
`HttpClient(OkHttp)`
```kotlin
// 使用 OkHttp 引擎
val client = HttpClient(OkHttp)
```

---

## 请求方法

**基本写法：GET 请求**
`client.get("<url>")`
```kotlin
// 发送 GET 请求
val resp = client.get("https://api.example.com/users")
```

---

**基本写法：POST 请求**
`client.post("<url>") { }`
```kotlin
// 发送 POST 请求
client.post("https://api.example.com/users") {
    setBody(User("Alice"))
}
```

---

**基本写法：PUT 请求**
`client.put("<url>") { }`
```kotlin
// 发送 PUT 请求
client.put("https://api.example.com/users/1") { setBody(data) }
```

---

**基本写法：DELETE 请求**
`client.delete("<url>")`
```kotlin
// 发送 DELETE 请求
client.delete("https://api.example.com/users/1")
```

---

## 请求配置

**基本写法：设置请求头**
`headers { append("<名称>", "<值>") }`
```kotlin
// 添加请求头
client.get("...") {
    header("Authorization", "Bearer token")
}
```

---

**基本写法：URL 参数**
`url { parameters.append("<名>", "<值>") }`
```kotlin
// 添加查询参数
client.get("...") {
    url { parameters.append("page", "1") }
}
```

---

**基本写法：JSON 请求体**
`setBody(<对象>)`
```kotlin
// 发送 JSON 请求体
client.post("...") {
    contentType(ContentType.Application.Json)
    setBody(user)
}
```

---

## 响应处理

**基本写法：获取响应体文本**
`<resp>.bodyAsText()`
```kotlin
// 获取响应文本
val text = client.get("...").bodyAsText()
```

---

**基本写法：反序列化为对象**
`<resp>.body<<类型>>()`
```kotlin
// 反序列化响应体
val user = client.get("...").body<User>()
```

---

**基本写法：获取状态码**
`<resp>.status`
```kotlin
// 获取 HTTP 状态码
val status = resp.status
```

---

**基本写法：获取响应头**
`<resp>.headers["<名称>"]`
```kotlin
// 获取响应头
val ct = resp.headers[HttpHeaders.ContentType]
```

---

## ContentNegotiation 插件

**基本写法：安装 JSON 插件**
`install(ContentNegotiation) { json() }`
```kotlin
// 启用自动 JSON 序列化
val client = HttpClient(CIO) {
    install(ContentNegotiation) {
        json(Json { ignoreUnknownKeys = true })
    }
}
```

---

## HttpRequestBuilder 风格

**基本写法：配置请求构建器**
`HttpRequestBuilder().apply { }`
```kotlin
// 复用请求配置
val builder = HttpRequestBuilder().apply {
    url("https://api.example.com")
    header("X-Key", "abc")
}
client.request(builder)
```

---

## 超时配置

**基本写法：设置超时**
`install(HttpTimeout) { }`
```kotlin
// 配置请求超时
install(HttpTimeout) {
    requestTimeoutMillis = 5000
    connectTimeoutMillis = 3000
    socketTimeoutMillis = 10000
}
```

---

## 鉴权插件

**基本写法：Bearer 鉴权**
`install(Auth) { bearer { } }`
```kotlin
// Bearer Token 自动加载
install(Auth) {
    bearer {
        loadTokens { BearerTokens(accessToken, refreshToken) }
    }
}
```

---

**基本写法：Basic 鉴权**
`install(Auth) { basic { } }`
```kotlin
// Basic 认证
install(Auth) {
    basic {
        username = "user"
        password = "pwd"
    }
}
```

---

## 日志插件

**基本写法：启用日志**
`install(Logging) { }`
```kotlin
// 请求响应日志
install(Logging) {
    level = LogLevel.HEADERS
    logger = Logger.DEFAULT
}
```

---

## 重试插件

**基本写法：失败重试**
`install(HttpRequestRetry) { }`
```kotlin
// 配置重试策略
install(HttpRequestRetry) {
    retryOnServerErrors(maxRetries = 3)
    exponentialDelay()
}
```

---

## UserAgent 插件

**基本写法：设置 UA**
`install(UserAgent) { agent = "<ua>" }`
```kotlin
// 设置全局 User-Agent
install(UserAgent) { agent = "MyApp/1.0" }
```

---

## HttpCookies Cookie 管理

**基本写法：启用 Cookie**
`install(HttpCookies)`
```kotlin
// 自动管理 Cookie
install(HttpCookies)
```

---

**基本写法：设置 Cookie 存储**
`install(HttpCookies) { storage = <存储> }`
```kotlin
// 自定义 Cookie 存储
install(HttpCookies) {
    storage = AcceptAllCookiesStorage()
}
```

---

## WebSocket 客户端

**基本写法：建立 WebSocket**
`client.webSocket("<url>") { }`
```kotlin
// 建立 WebSocket 连接
client.webSocket("wss://echo.example.com") {
    send(Frame.Text("hello"))
}
```

---

**基本写法：发送 WebSocket 消息**
`send(Frame.Text("<消息>"))`
```kotlin
// 发送文本帧
send(Frame.Text("ping"))
```

---

**基本写法：接收 WebSocket 消息**
`incoming.receive() as Frame.Text`
```kotlin
// 接收文本帧
val msg = (incoming.receive() as Frame.Text).readText()
```

---

## SSE Server-Sent Events

**基本写法：SSE 接收**
`client.config { }.sseSession { }`
```kotlin
// 处理 SSE 事件流
client.sseSession("https://events.example.com") {
    incoming.collect { event -> println(event.data) }
}
```

---

## 资源关闭

**基本写法：关闭客户端**
`<client>.close()`
```kotlin
// 关闭释放连接池
client.close()
```

---

**基本写法：use 自动关闭**
`HttpClient(<引擎>).use { }`
```kotlin
// use 块自动关闭
HttpClient(CIO).use { c -> c.get("...") }
```

---

## 跨平台使用

**基本写法：KMP 共享客户端**
`val client = HttpClient()`
```kotlin
// KMP 跨平台默认引擎
val client = HttpClient()
```



<!-- ============ 文档分隔线：014-kotlin/025-KotlinRegex.md ============ -->

# Kotlin 正则表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建正则

**基本写法：创建 Regex**
`Regex("<模式>")`
```kotlin
// 从字符串创建正则对象
val re = Regex("\\d+")
```

---

**基本写法：toRegex 转换**
`"<模式>".toRegex()`
```kotlin
// 字符串扩展转换为正则
val re = "[a-z]+".toRegex()
```

---

**基本写法：带选项创建**
`Regex("<模式>", setOf(<选项>))`
```kotlin
// 创建忽略大小写的正则
val re = Regex("hello", setOf(RegexOption.IGNORE_CASE))
```

---

**基本写法：原始字符串模式**
`Regex("""<模式>""")`
```kotlin
// 使用原始字符串避免转义
val re = Regex("""\d{3}-\d{4}""")
```

---

## 匹配判断

**基本写法：完整匹配**
`<re>.matches(<字符串>)`
```kotlin
// 判断整个字符串是否匹配
val ok = re.matches("123")
```

---

**基本写法：包含匹配**
`<re>.containsMatchIn(<字符串>)`
```kotlin
// 判断是否包含匹配
val has = re.containsMatchIn("abc123")
```

---

**基本写法：matches 中缀操作**
`<字符串> matches <re>`
```kotlin
// 中缀形式匹配
val ok = "123" matches re
```

---

## 查找与提取

**基本写法：查找首个**
`<re>.find(<字符串>)`
```kotlin
// 查找首个匹配
val m = re.find("a1b2")
val v = m?.value
```

---

**基本写法：查找所有**
`<re>.findAll(<字符串>)`
```kotlin
// 查找所有匹配
val all = re.findAll("a1b2c3").map { it.value }.toList()
```

---

**基本写法：获取捕获组**
`<match>?.groupValues`
```kotlin
// 获取捕获组列表
val groups = m?.groupValues
val g1 = groups?.get(1)
```

---

**基本写法：命名捕获组**
`<match>?.groups["<名称>"]?.value`
```kotlin
// 按名称获取捕获组
val re = Regex("""(?<year>\d{4})""")
val year = re.find("2025")?.groups?.get("year")?.value
```

---

## 替换操作

**基本写法：替换全部**
`<re>.replace(<字符串>, "<替换>")`
```kotlin
// 替换所有匹配
val r = re.replace("a1b2", "X")
```

---

**基本写法：函数替换**
`<re>.replace(<字符串>) { <替换> }`
```kotlin
// 使用函数生成替换值
val r = re.replace("a1b2") { m -> "[${m.value}]" }
```

---

**基本写法：替换首个**
`<re>.replaceFirst(<字符串>, "<替换>")`
```kotlin
// 仅替换首个匹配
val r = re.replaceFirst("a1b2", "X")
```

---

## 分割字符串

**基本写法：按正则分割**
`<re>.split(<字符串>)`
```kotlin
// 按正则分割字符串
val parts = Regex("[,;]").split("a,b;c")
```

---

## MatchResult 操作

**基本写法：next 下一个匹配**
`<match>?.next()`
```kotlin
// 链式获取下一个匹配
var cur = re.find("a1b2")
while (cur != null) { println(cur.value); cur = cur.next() }
```

---

**基本写法：获取匹配范围**
`<match>?.range`
```kotlin
// 获取匹配在原串中的范围
val range = m?.range
```

---

## 分组引用

**基本写法：替换中引用捕获组**
`<re>.replace(<字符串>, "$<组名>")`
```kotlin
// 引用命名捕获组进行替换
val r = Regex("(?<d>\\d)").replace("a1", "<${'$'}{d}>")
```

---

## RegexOption 选项

**基本写法：忽略大小写**
`RegexOption.IGNORE_CASE`
```kotlin
// 忽略大小写匹配
val re = Regex("hello", RegexOption.IGNORE_CASE)
```

---

**基本写法：多行模式**
`RegexOption.MULTILINE`
```kotlin
// ^ $ 匹配每行
val re = Regex("^a", RegexOption.MULTILINE)
```

---

**基本写法：单行模式**
`RegexOption.DOT_MATCHES_ALL`
```kotlin
// . 匹配包括换行符
val re = Regex("a.b", RegexOption.DOT_MATCHES_ALL)
```

---

## 常用模式示例

**基本写法：邮箱校验**
`Regex("^[\\w.]+@[\\w.]+$")`
```kotlin
// 简单邮箱正则
val email = Regex("""^[\w.]+@[\w.]+$""")
val ok = email.matches("a@b.com")
```

---

**基本写法：手机号校验**
`Regex("^1[3-9]\\d{9}$")`
```kotlin
// 中国大陆手机号校验
val phone = Regex("^1[3-9]\\d{9}$")
```

---

**基本写法：IPv4 校验**
`Regex("^\\d{1,3}(\\.\\d{1,3}){3}$")`
```kotlin
// IPv4 地址格式校验
val ip = Regex("""^\d{1,3}(\.\d{1,3}){3}$""")
```

---

## 字符串便捷方法

**基本写法：startsWith 正则**
`<字符串>.startsWith(Regex("<模式>"))`
```kotlin
// 判断是否以正则匹配开头
val ok = "abc".startsWith(Regex("[a-z]"))
```

---

**基本写法：trim 按 Regex**
`<字符串>.trim(<re>, <re>)`
```kotlin
// 按正则裁剪首尾
val r = "##abc##".trim(Regex("#+"))
```

---

## 性能优化

**基本写法：复用 Regex 实例**
`private val <re> = Regex("<模式>")`
```kotlin
// 编译一次复用避免重复解析
private val EMAIL_RE = Regex("""^[\w.]+@[\w.]+$""")
fun check(s: String) = EMAIL_RE.matches(s)
```



<!-- ============ 文档分隔线：014-kotlin/026-KotlinTime.md ============ -->

# Kotlin 时间 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Duration 时长

**基本写法：创建时长**
`<数字>.<单位>()`
```kotlin
// 不同单位创建 Duration
val d1 = 5.seconds
val d2 = 100.milliseconds
val d3 = 2.hours
```

---

**基本写法：字面量时长**
`<数字>.<单位>`
```kotlin
// Duration 字面量扩展属性
val d = 30.minutes
```

---

**基本写法：时长运算**
`<时长> + <时长> | <时长> * <倍数>`
```kotlin
// 时长加减乘除
val sum = 1.hours + 30.minutes
val half = 1.hours / 2
```

---

**基本写法：转换为单位**
`<duration>.inWholeSeconds | inWholeMilliseconds`
```kotlin
// 转换为整型单位
val s = (1.5.hours).inWholeSeconds
val ms = (1.minutes).inWholeMilliseconds
```

---

**基本写法：比较时长**
`<d1> > <d2> | <d>.compareTo(<d2>)`
```kotlin
// 比较时长大小
if (d1 > d2) { }
```

---

## TimeMark 与测量

**基本写法：获取时间标记**
`TimeSource.Monotonic.markNow()`
```kotlin
// 获取单调时钟标记
val mark = TimeSource.Monotonic.markNow()
```

---

**基本写法：测量经过时长**
`<mark>.elapsedNow()`
```kotlin
// 测量自标记以来的时长
val dur = mark.elapsedNow()
```

---

**基本写法：measureTime 测量代码**
`measureTime { <代码> }`
```kotlin
// 测量代码块耗时
val t = measureTime { doWork() }
println(t)
```

---

**基本写法：测量并返回结果**
`measureTimedValue { <代码> }`
```kotlin
// 同时返回结果与耗时
val (result, time) = measureTimedValue { compute() }
```

---

## kotlinx-datetime 跨平台

**基本写法：获取当前时刻**
`Clock.System.now()`
```kotlin
// 获取当前 Instant
val now = Clock.System.now()
```

---

**基本写法：当前本地日期**
`Clock.System.todayIn(<时区>)`
```kotlin
// 获取指定时区当前日期
val today = Clock.System.todayIn(TimeZone.currentSystemDefault())
```

---

**基本写法：创建 LocalDate**
`LocalDate(<年>, <月>, <日>)`
```kotlin
// 创建指定日期
val d = LocalDate(2025, 7, 31)
```

---

**基本写法：创建 LocalDateTime**
`LocalDateTime(<日期>, <时间>)`
```kotlin
// 创建本地日期时间
val dt = LocalDateTime(LocalDate(2025,7,31), LocalTime(10,30))
```

---

**基本写法：解析日期**
`LocalDate.parse("<字符串>")`
```kotlin
// 解析 ISO 日期字符串
val d = LocalDate.parse("2025-07-31")
```

---

## Instant 操作

**基本写法：加时长**
`<instant>.plus(<duration>)`
```kotlin
// Instant 加时长
val later = now.plus(1.hours)
```

---

**基本写法：计算差值**
`<i1>.minus(<i2>)`
```kotlin
// 两个 Instant 的时长差
val dur = i1.minus(i2)
```

---

**基本写法：转换为时区**
`<instant>.toLocalDateTime(<时区>)`
```kotlin
// 转为指定时区本地时间
val ldt = now.toLocalDateTime(TimeZone.of("Asia/Shanghai"))
```

---

## Instant 与 epoch

**基本写法：从 epoch 秒创建**
`Instant.fromEpochSeconds(<秒>)`
```kotlin
// Unix 秒转 Instant
val i = Instant.fromEpochSeconds(1700000000)
```

---

**基本写法：获取 epoch 秒**
`<instant>.epochSeconds`
```kotlin
// 获取 Unix 秒数
val s = now.epochSeconds
```

---

## DateTimePeriod 日期段

**基本写法：创建日期段**
`DateTimePeriod(years = <年>, months = <月>)`
```kotlin
// 创建年月日时段
val p = DateTimePeriod(years = 1, months = 2)
```

---

**基本写法：加日期段**
`<localDate>.plus(<period>, <时区>)`
```kotlin
// 日期加日期段
val next = d.plus(p, TimeZone.UTC)
```

---

## TimeZone 时区

**基本写法：系统默认时区**
`TimeZone.currentSystemDefault()`
```kotlin
// 获取系统默认时区
val tz = TimeZone.currentSystemDefault()
```

---

**基本写法：指定时区**
`TimeZone.of("<时区ID>")`
```kotlin
// 按名称获取时区
val tz = TimeZone.of("Asia/Shanghai")
```

---

**基本写法：UTC 时区**
`TimeZone.UTC`
```kotlin
// 直接引用 UTC 时区
val utc = TimeZone.UTC
```

---

## 格式化与解析

**基本写法：自定义格式化**
`LocalDate.Format { <配置> }`
```kotlin
// 自定义日期格式
val fmt = LocalDate.Format {
    year(); chars("-"); monthNumber(); chars("-"); dayOfMonth()
}
```

---

**基本写法：按格式解析**
`LocalDate.parse("<字符串>", <format>)`
```kotlin
// 按自定义格式解析
val d = LocalDate.parse("2025/07/31", fmt)
```

---

## DayOfWeek 与 Month

**基本写法：获取星期**
`<localDate>.dayOfWeek`
```kotlin
// 获取星期枚举值
val dow = d.dayOfWeek
```

---

**基本写法：获取月份**
`<localDate>.month`
```kotlin
// 获取月份枚举值
val m = d.month
```

---

## 协程中的延迟

**基本写法：Duration 延迟**
`delay(<duration>)`
```kotlin
// 协程中使用 Duration 延迟
delay(500.milliseconds)
```

---

## 日期比较

**基本写法：判断前/后**
`<d1> < <d2> | <d1>.until(<d2>)`
```kotlin
// 日期前后判断
if (d1 < d2) { }
val until = d1.until(d2)
```



<!-- ============ 文档分隔线：014-kotlin/027-KotlinIO.md ============ -->

# Kotlin IO API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件读取

**基本写法：读取全部文本**
`File("<路径>").readText()`
```kotlin
// 一次性读取文本文件
val text = File("a.txt").readText()
```

---

**基本写法：按行读取**
`File("<路径>").readLines()`
```kotlin
// 按行读取为 List
val lines = File("a.txt").readLines()
```

---

**基本写法：读取全部字节**
`File("<路径>").readBytes()`
```kotlin
// 读取为字节数组
val bytes = File("a.txt").readBytes()
```

---

**基本写法：逐行流式读取**
`File("<路径>").useLines { }`
```kotlin
// 流式逐行处理自动关闭
File("a.txt").useLines { lines -> lines.forEach { } }
```

---

## 文件写入

**基本写法：写入文本**
`File("<路径>").writeText("<内容>")`
```kotlin
// 覆盖写入文本
File("out.txt").writeText("hello")
```

---

**基本写法：写入字节**
`File("<路径>").writeBytes(<字节数组>)`
```kotlin
// 覆盖写入字节
File("out.bin").writeBytes(bytes)
```

---

**基本写法：追加写入**
`File("<路径>").appendText("<内容>")`
```kotlin
// 追加文本到文件
File("log.txt").appendText("new line\n")
```

---

**基本写法：追加字节**
`File("<路径>").appendBytes(<字节数组>)`
```kotlin
// 追加字节数组
File("log.bin").appendBytes(bytes)
```

---

## 文件流操作

**基本写法：写入流**
`File("<路径>").outputStream()`
```kotlin
// 获取文件输出流
File("out.txt").outputStream().use { it.write(bytes) }
```

---

**基本写法：读取流**
`File("<路径>").inputStream()`
```kotlin
// 获取文件输入流
File("a.txt").inputStream().use { it.readBytes() }
```

---

**基本写法：BufferedWriter**
`File("<路径>").bufferedWriter()`
```kotlin
// 缓冲写入器
File("out.txt").bufferedWriter().use { w -> w.write("hi") }
```

---

**基本写法：BufferedReader**
`File("<路径>").bufferedReader()`
```kotlin
// 缓冲读取器
File("a.txt").bufferedReader().use { r -> r.readLine() }
```

---

## 文件与目录操作

**基本写法：创建文件**
`File("<路径>").createNewFile()`
```kotlin
// 创建新文件
File("a.txt").createNewFile()
```

---

**基本写法：创建目录**
`File("<路径>").mkdirs()`
```kotlin
// 递归创建目录
File("a/b/c").mkdirs()
```

---

**基本写法：删除文件**
`File("<路径>").delete()`
```kotlin
// 删除文件或空目录
File("a.txt").delete()
```

---

**基本写法：删除递归**
`File("<路径>").deleteRecursively()`
```kotlin
// 递归删除目录及内容
File("dir").deleteRecursively()
```

---

**基本写法：判断存在**
`File("<路径>").exists()`
```kotlin
// 判断文件是否存在
if (File("a.txt").exists()) { }
```

---

**基本写法：判断文件/目录**
`File("<路径>").isFile | isDirectory`
```kotlin
// 判断是文件还是目录
if (File("p").isDirectory) { }
```

---

**基本写法：列出文件**
`File("<路径>").listFiles()`
```kotlin
// 列出目录下文件
val files = File("dir").listFiles()
```

---

**基本写法：按扩展名过滤**
`File("<路径>").listFiles { _, name -> name.endsWith(".txt") }`
```kotlin
// 过滤特定扩展名
val txts = File("dir").listFiles { _, n -> n.endsWith(".txt") }
```

---

**基本写法：遍历目录树**
`File("<路径>").walk()`
```kotlin
// 深度遍历目录树
File("dir").walk().forEach { println(it) }
```

---

## 文件复制与移动

**基本写法：复制到**
`File("<源>").copyTo(File("<目标>"))`
```kotlin
// 复制文件
File("a.txt").copyTo(File("b.txt"))
```

---

**基本写法：递归复制**
`File("<源>").copyRecursively(File("<目标>"))`
```kotlin
// 递归复制目录
File("src").copyRecursively(File("dst"))
```

---

**基本写法：移动**
`File("<源>").renameTo(File("<目标>"))`
```kotlin
// 重命名或移动文件
File("a.txt").renameTo(File("b.txt"))
```

---

## 文件属性

**基本写法：文件大小**
`File("<路径>").length()`
```kotlin
// 获取文件字节数
val size = File("a.txt").length()
```

---

**基本写法：最后修改时间**
`File("<路径>").lastModified()`
```kotlin
// 获取最后修改时间戳
val t = File("a.txt").lastModified()
```

---

**基本写法：绝对路径**
`File("<路径>").absolutePath`
```kotlin
// 获取绝对路径
val abs = File("a.txt").absolutePath
```

---

## Path（kotlin.io.path）

**基本写法：创建 Path**
`Path("<路径>")`
```kotlin
// 创建 Path 对象
val p = Path("a/b.txt")
```

---

**基本写法：读写 Path**
`<path>.readText() | <path>.writeText()`
```kotlin
// Path 扩展读写
val text = Path("a.txt").readText()
Path("out.txt").writeText("hi")
```

---

**基本写法：递归创建**
`<path>.createDirectories()`
```kotlin
// 递归创建目录
Path("a/b/c").createDirectories()
```

---

**基本写法：复制 Path**
`<path>.copyTo(<目标>)`
```kotlin
// Path 复制
Path("a.txt").copyTo(Path("b.txt"))
```

---

## 标准流

**基本写法：标准输入**
`readLine()`
```kotlin
// 读取一行标准输入
val line = readLine()
```

---

**基本写法：标准输出**
`print(<值>) | println(<值>)`
```kotlin
// 标准输出
println("hello")
```

---

**基本写法：System.err**
`System.err.println(<值>)`
```kotlin
// 标准错误输出
System.err.println("error")
```

---

## 跨平台 IO

**基本写法：KMP 使用 okio**
`FileSystem.SYSTEM.read(<path>) { }`
```kotlin
// okio 跨平台文件读取
FileSystem.SYSTEM.read(Path("a.txt")) {
    readUtf8()
}
```

---

**基本写法：KMP 写入**
`FileSystem.SYSTEM.write(<path>) { }`
```kotlin
// okio 跨平台文件写入
FileSystem.SYSTEM.write(Path("out.txt")) {
    writeUtf8("hi")
}
```



<!-- ============ 文档分隔线：014-kotlin/028-KotlinTest.md ============ -->

# Kotlin 测试

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## kotlin.test 基础

**基本写法：简单测试**
`@Test fun <方法名>() { }`
```kotlin
// 使用 @Test 注解标记测试
class MyTest {
    @Test fun sumWorks() = assertEquals(4, 2 + 2)
}
```

---

**基本写法：断言相等**
`assertEquals(<期望>, <实际>)`
```kotlin
// 断言两值相等
assertEquals(10, calc())
```

---

**基本写法：断言不相等**
`assertNotEquals(<值1>, <值2>)`
```kotlin
// 断言两值不等
assertNotEquals(0, count)
```

---

**基本写法：断言为真**
`assertTrue(<条件>)`
```kotlin
// 断言条件为真
assertTrue(list.isEmpty())
```

---

**基本写法：断言为假**
`assertFalse(<条件>)`
```kotlin
// 断言条件为假
assertFalse(list.isNotEmpty())
```

---

**基本写法：断言为 null**
`assertNull(<值>)`
```kotlin
// 断言值为 null
assertNull(findUser(-1))
```

---

**基本写法：断言非 null**
`assertNotNull(<值>)`
```kotlin
// 断言值非 null
assertNotNull(findUser(1))
```

---

**基本写法：断言抛异常**
`assertFailsWith<<异常类型>> { }`
```kotlin
// 断言代码块抛指定异常
assertFailsWith<IllegalArgumentException> { parse("") }
```

---

## kotlin.test 框架适配

**基本写法：Test 注解导入**
`import kotlin.test.Test`
```kotlin
// 跨平台测试注解
import kotlin.test.Test
import kotlin.test.assertEquals
```

---

## JUnit 5 注解

**基本写法：BeforeEach 初始化**
`@BeforeEach fun <方法>() { }`
```kotlin
// 每个测试前执行
class DbTest {
    @BeforeEach fun setup() { db = open() }
}
```

---

**基本写法：AfterEach 清理**
`@AfterEach fun <方法>() { }`
```kotlin
// 每个测试后执行
@AfterEach fun teardown() { db.close() }
```

---

**基本写法：BeforeAll 一次性初始化**
`@BeforeAll fun <方法>() { }`
```kotlin
// 所有测试前执行一次
companion object {
    @BeforeAll @JvmStatic fun init() { }
}
```

---

**基本写法：Disabled 禁用**
`@Disabled("<原因>") @Test fun <方法>() { }`
```kotlin
// 禁用测试用例
@Disabled("待实现")
@Test fun todo() { }
```

---

**基本写法：DisplayName**
`@DisplayName("<名称>") @Test fun <方法>() { }`
```kotlin
// 自定义测试显示名
@DisplayName("用户登录成功")
@Test fun login() { }
```

---

## 参数化测试

**基本写法：ValueSource**
`@ParameterizedTest @ValueSource(strings = ["a", "b"])`
```kotlin
// 多组参数运行测试
@ParameterizedTest
@ValueSource(strings = ["a", "b"])
fun test(s: String) { }
```

---

**基本写法：CsvSource**
`@ParameterizedTest @CsvSource(["1,2,3"])`
```kotlin
// CSV 多参数
@ParameterizedTest
@CsvSource(["1,2,3", "4,5,9"])
fun sum(a: Int, b: Int, expected: Int) { assertEquals(expected, a + b) }
```

---

**基本写法：MethodSource**
`@ParameterizedTest @MethodSource("<方法>")`
```kotlin
// 从静态方法获取参数
@ParameterizedTest
@MethodSource("cases")
fun test(c: Case) { }
companion object {
    @JvmStatic fun cases() = listOf(Case(1, 2))
}
```

---

## 协程测试

**基本写法：runTest 测试协程**
`runTest { }`
```kotlin
// 协程测试运行器
@Test fun test() = runTest {
    val r = fetch()
    assertEquals("ok", r)
}
```

---

**基本写法：测试延迟跳过**
`runTest { delay(1000) }`
```kotlin
// 虚拟时间跳过延迟
runTest {
    delay(1000) // 不实际等待
    launch { }
}
```

---

**基本写法：Turbine 测试 Flow**
`<flow>.test { }`
```kotlin
// 使用 Turbine 测试 Flow
nums().test {
    assertEquals(1, awaitItem())
    awaitComplete()
}
```

---

## MockK 模拟

**基本写法：mockk 模拟对象**
`mockk<<类型>>()`
```kotlin
// 创建 mock 对象
val repo = mockk<UserRepository>()
```

---

**基本写法：mockk relax**
`mockk<<类型>>(relaxed = true)`
```kotlin
// 宽松 mock 自动返回默认值
val repo = mockk<UserRepository>(relaxed = true)
```

---

**基本写法：every 打桩**
`every { <调用> } returns <值>`
```kotlin
// 配置 mock 返回值
every { repo.find(1) } returns User("Alice")
```

---

**基本写法：verify 验证**
`verify { <调用> }`
```kotlin
// 验证方法被调用
verify { repo.find(1) }
```

---

**基本写法：验证调用次数**
`verify(exactly = <次数>) { }`
```kotlin
// 验证调用次数
verify(exactly = 2) { repo.find(any()) }
```

---

**基本写法：coEvery 协程打桩**
`coEvery { <挂起调用> } returns <值>`
```kotlin
// 协程方法打桩
coEvery { repo.fetch() } returns "ok"
```

---

**基本写法：coVerify 协程验证**
`coVerify { <挂起调用> }`
```kotlin
// 验证协程方法调用
coVerify { repo.fetch() }
```

---

## kotest 风格

**基本写法：StringSpec**
`class <类> : StringSpec({ })`
```kotlin
// kotest 字符串风格
class MyTest : StringSpec({
    "sum should work" { 2 + 2 shouldBe 4 }
})
```

---

**基本写法：shouldBe 断言**
`<值> shouldBe <期望>`
```kotlin
// kotest 断言
result shouldBe "hello"
```

---

**基本写法：shouldThrow**
`shouldThrow<<异常>> { }`
```kotlin
// 断言抛异常
shouldThrow<IllegalArgumentException> { parse("") }
```

---

## Gradle 配置

**基本写法：测试依赖**
`testImplementation("<坐标>")`
```kotlin
// build.gradle.kts 测试依赖
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("io.mockk:mockk:1.13.12")
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.9.0")
}
```

---

**基本写法：运行测试**
`./gradlew test`
```bash
# 运行所有测试
./gradlew test
```

---

**基本写法：运行特定测试**
`./gradlew test --tests "<类>.<方法>"`
```bash
# 运行指定测试方法
./gradlew test --tests "com.example.MyTest.sumWorks"
```



<!-- ============ 文档分隔线：014-kotlin/029-KotlinEnumClass.md ============ -->

# Kotlin 枚举类

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 定义枚举

**基本写法：简单枚举**
`enum class <名称> { <枚举项1>, <枚举项2> }`
```kotlin
// 定义无参枚举
enum class Color { RED, GREEN, BLUE }
```

---

**基本写法：带参枚举**
`enum class <名称>(val <属性>: <类型>) { }`
```kotlin
// 枚举项带属性
enum class Color(val rgb: Int) {
    RED(0xFF0000), GREEN(0x00FF00), BLUE(0x0000FF)
}
```

---

**基本写法：多项属性**
`enum class <名称>(val <属性1>: <类型>, val <属性2>: <类型>) { }`
```kotlin
// 多属性枚举
enum class User(val id: Int, val role: String) {
    ADMIN(1, "admin"), GUEST(2, "guest")
}
```

---

## 枚举方法

**基本写法：定义方法**
`enum class <名称> { ; fun <方法>() {} }`
```kotlin
// 枚举类定义方法
enum class Ops {
    ADD, SUB;
    fun apply(a: Int, b: Int) = when (this) {
        ADD -> a + b
        SUB -> a - b
    }
}
```

---

**基本写法：抽象方法**
`enum class <名称> { ; abstract fun <方法>(): <类型> }`
```kotlin
// 枚举项重写抽象方法
enum class Op {
    ADD { override fun apply(a: Int, b: Int) = a + b },
    SUB { override fun apply(a: Int, b: Int) = a - b };
    abstract fun apply(a: Int, b: Int): Int
}
```

---

## 枚举使用

**基本写法：访问枚举值**
`<枚举>.<项>`
```kotlin
// 访问枚举常量
val c = Color.RED
```

---

**基本写法：获取所有值**
`<枚举>.values()`
```kotlin
// 获取所有枚举项
val all = Color.values()
```

---

**基本写法：entries（1.9+）**
`<枚举>.entries`
```kotlin
// 获取枚举项 List
val all = Color.entries
```

---

**基本写法：按名称转换**
`<枚举>.valueOf("<名称>")`
```kotlin
// 按字符串获取枚举值
val c = Color.valueOf("RED")
```

---

**基本写法：valueOfOrNull**
`runCatching { <枚举>.valueOf("<名称>") }.getOrNull()`
```kotlin
// 安全转换避免异常
val c = runCatching { Color.valueOf("X") }.getOrNull()
```

---

## 枚举属性

**基本写法：获取名称**
`<枚举值>.name`
```kotlin
// 获取枚举项名称
val n = Color.RED.name
```

---

**基本写法：获取序号**
`<枚举值>.ordinal`
```kotlin
// 获取枚举项序号
val o = Color.RED.ordinal
```

---

## when 分支

**基本写法：when 匹配枚举**
`when (<枚举值>) { <项1> -> ; <项2> -> }`
```kotlin
// when 表达式匹配枚举
when (c) {
    Color.RED -> println("r")
    Color.GREEN -> println("g")
    Color.BLUE -> println("b")
}
```

---

**基本写法：when 穷举**
`when (<枚举值>) { <所有项> -> } // else 可省`
```kotlin
// 穷举所有项可省略 else
fun label(c: Color) = when (c) {
    Color.RED -> "R"
    Color.GREEN -> "G"
    Color.BLUE -> "B"
}
```

---

## 实现接口

**基本写法：枚举实现接口**
`enum class <名称> : <接口> { }`
```kotlin
// 枚举实现接口
interface Describable { fun desc(): String }
enum class Mode : Describable {
    FAST { override fun desc() = "fast" },
    SLOW { override fun desc() = "slow" }
}
```

---

## 枚举与扩展函数

**基本写法：扩展枚举**
`fun <枚举>.<方法>() { }`
```kotlin
// 为枚举添加扩展函数
fun Color.isPrimary() = this == Color.RED
```

---

## 枚举集合

**基本写法：EnumSet**
`enumSetOf<<枚举>>(<项>...)`
```kotlin
// 高效枚举集合
import java.util.EnumSet
val set: EnumSet<Color> = EnumSet.of(Color.RED, Color.GREEN)
```

---

**基本写法：EnumMap**
`enumMapOf<<键>, <值>>()`
```kotlin
// 以枚举为键的高效 Map
import java.util.EnumMap
val m: EnumMap<Color, Int> = EnumMap(Color::class.java)
m[Color.RED] = 1
```

---

## 枚举比较

**基本写法：按序号比较**
`<值1>.compareTo(<值2>)`
```kotlin
// 比较 ordinal 大小
val cmp = Color.RED.compareTo(Color.BLUE)
```

---

**基本写法：范围**
`<枚举>.<项1>..<枚举>.<项2>`
```kotlin
// 枚举区间
val range = Color.RED..Color.GREEN
```

---

## 枚举委托属性

**基本写法：枚举作为状态**
`var <变量> by <委托>`
```kotlin
// 枚举常用于状态机
var state: State by Delegates.observable(State.IDLE) { _, _, new -> }
```

---

## 枚举序列化

**基本写法：按名称序列化**
`@Serializable` 配合 `@SerialName`
```kotlin
// kotlinx-serialization 枚举
import kotlinx.serialization.*
@Serializable
enum class Status {
    @SerialName("active") ACTIVE,
    @SerialName("inactive") INACTIVE
}
```

---

## 枚举与 sealed 比较

**基本写法：枚举固定项**
`enum class <名称> { <固定项> }`
```kotlin
// 枚举用于固定项常量
enum class Direction { UP, DOWN, LEFT, RIGHT }
```

---

**基本写法：密封类扩展项**
`sealed class <名称> { data class <子类> }`
```kotlin
// 密封类用于带状态的变体
sealed class Result {
    data class Ok<T>(val v: T): Result()
    data class Err(val e: Throwable): Result()
}
```

---

## 反射枚举

**基本写法：判断是否枚举**
`<类>.kotlin.isEnum`
```kotlin
// 判断 KClass 是否为枚举
val isEnum = Color::class.isEnum
```

---

**基本写法：获取枚举 KClass**
`<枚举>::class`
```kotlin
// 获取枚举类对象
val kc = Color::class
```



<!-- ============ 文档分隔线：014-kotlin/030-KotlinContract.md ============ -->

# Kotlin 契约 Contracts

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 契约基础

**基本写法：定义契约**
`contract { <效果> }`
```kotlin
// 在函数开头声明契约
fun requireNonZero(x: Int) {
    contract { returns() implies (x != 0) }
    require(x != 0)
}
```

---

## returns 契约

**基本写法：返回真则条件成立**
`returns(true) implies (<条件>)`
```kotlin
// 函数返回 true 时条件成立
fun isValid(s: String?): Boolean {
    contract { returns(true) implies (s != null) }
    return s != null && s.isNotEmpty()
}
```

---

**基本写法：返回即条件成立**
`returns() implies (<条件>)`
```kotlin
// 函数正常返回时条件成立
fun requireNotNull(x: Int?) {
    contract { returns() implies (x != null) }
    if (x == null) throw IllegalArgumentException()
}
```

---

**基本写法：returns(false) 契约**
`returns(false) implies (<条件>)`
```kotlin
// 返回 false 时的条件
fun isBlank(s: String?): Boolean {
    contract { returns(false) implies (s != null) }
    return s == null || s.isEmpty()
}
```

---

## callInplace 契约

**基本写法：内联调用契约**
`callsInPlace(<lambda>, <次数>)`
```kotlin
// lambda 仅被调用一次
inline fun compute(block: () -> Int) {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }
    block()
}
```

---

**基本写法：至少一次调用**
`callsInPlace(<lambda>, InvocationKind.AT_LEAST_ONCE)`
```kotlin
// lambda 至少调用一次
inline fun run(block: () -> Unit) {
    contract { callsInPlace(block, InvocationKind.AT_LEAST_ONCE) }
    block()
}
```

---

**基本写法：至多一次调用**
`callsInPlace(<lambda>, InvocationKind.AT_MOST_ONCE)`
```kotlin
// lambda 至多调用一次
inline fun lazyInit(block: () -> T) {
    contract { callsInPlace(block, InvocationKind.AT_MOST_ONCE) }
    block()
}
```

---

**基本写法：未知次数**
`callsInPlace(<lambda>, InvocationKind.UNKNOWN)`
```kotlin
// 调用次数未知
inline fun repeat(n: Int, block: () -> Unit) {
    contract { callsInPlace(block, InvocationKind.UNKNOWN) }
    for (i in 0 until n) block()
}
```

---

## 内联函数契约

**基本写法：内联函数中声明**
`inline fun <方法>(<参数>): <返回> { contract { } }`
```kotlin
// 内联函数必须用契约
inline fun checkFlag(flag: Boolean) {
    contract { returns() implies flag }
    if (!flag) throw IllegalStateException()
}
```

---

## 标准库契约示例

**基本写法：requireNotNull**
`requireNotNull(<值>) { <返回非空> }`
```kotlin
// 标准库已声明契约
val n: Int = requireNotNull(nullable) // 编译器知道非空
```

---

**基本写法：check**
`check(<条件>) { <条件成立> }`
```kotlin
// 标准库 check 契约
check(state == READY)
// 此处编译器知道 state == READY
```

---

**基本写法：assert**
`assert(<条件>)`
```kotlin
// 断言契约
assert(x > 0)
// 此处编译器知道 x > 0
```

---

## 自定义智能转换

**基本写法：辅助 is 智能转换**
`fun <方法>(x: Any?) { contract { returns() implies (x is <类型>) } }`
```kotlin
// 帮助编译器进行类型智能转换
fun requireString(x: Any?) {
    contract { returns() implies (x is String) }
    require(x is String)
}
```

---

**基本写法：非空智能转换**
`contract { returns() implies (<值> != null) }`
```kotlin
// 函数返回即值非空
fun ensureNonZero(x: Int?) {
    contract { returns() implies (x != null) }
    require(x != null && x != 0)
}
```

---

## 契约与 when

**基本写法：when 分支契约**
`contract { returns(true) implies (<条件>) }`
```kotlin
// 配合 when 使用智能转换
fun isList(x: Any): Boolean {
    contract { returns(true) implies (x is List<*>) }
    return x is List<*>
}
```

---

## 递归契约

**基本写法：契约避免递归警告**
`contract { callsInPlace(<lambda>, EXACTLY_ONCE) }`
```kotlin
// 让编译器知道递归 lambda 调用次数
inline fun recursion(block: (Int) -> Int) {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }
    block(0)
}
```

---

## 契约与可变变量

**基本写法：契约修改 var**
`contract { returns() implies (<变量> == <值>) }`
```kotlin
// 契约约束变量状态
var initialized = false
fun init() {
    contract { returns() implies (initialized) }
    initialized = true
}
```

---

## 契约限制

**基本写法：契约仅在内联函数**
`inline fun <方法>() { contract { } }`
```kotlin
// 契约必须在内联函数中声明
inline fun doCheck(x: Int) {
    contract { returns() implies (x > 0) }
    require(x > 0)
}
```

---

**基本写法：契约须为函数首条语句**
`fun <方法>() { contract { }; <其他> }`
```kotlin
// 契约声明必须位于函数体最前
inline fun f(x: Int) {
    contract { returns() implies (x > 0) }
    require(x > 0)
    doWork()
}
```

---

## 契约实验性标记

**基本写法：启用实验性契约**
`@OptIn(ExperimentalContracts::class)`
```kotlin
// 启用契约实验特性
@OptIn(ExperimentalContracts::class)
fun custom(x: Int?) {
    contract { returns() implies (x != null) }
    require(x != null)
}
```

---

## 契约与 lambda 返回类型

**基本写法：捕获 lambda 返回类型**
`contract { callsInPlace(<lambda>) }`
```kotlin
// 帮助推断 lambda 内 val 类型
inline fun <T> compute(block: () -> T) {
    contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }
    block()
}
fun main() {
    val x: Int  // 类型可被推断
    compute { x = 10 }
    println(x)
}
```



<!-- ============ 文档分隔线：014-kotlin/031-Kotlin2xNewFeatures.md ============ -->

﻿# Kotlin 2.x 新特性 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## K2 编译器

**基本写法：启用 K2 编译器**
`kotlin { compilerOptions { ... } }`
```kotlin
// Kotlin 2.0+ 默认使用 K2 编译器
// build.gradle.kts 中显式声明
kotlin {
    compilerOptions {
        languageVersion.set(org.jetbrains.kotlin.gradle.dsl.KotlinVersion.KOTLIN_2_0)
    }
}
```

---

**基本写法：降级到旧版本**
`languageVersion.set(KotlinVersion.KOTLIN_1_9)`
```kotlin
// 临时回退到 K1 行为
kotlin {
    compilerOptions {
        languageVersion.set(org.jetbrains.kotlin.gradle.dsl.KotlinVersion.KOTLIN_1_9)
    }
}
```

---

## when 守卫条件（2.1 stable）

**基本写法：when 守卫条件**
`case <模式> if <条件> -> <结果>`
```kotlin
// Kotlin 2.1 stable，when 分支后追加 if 条件
sealed interface Order
data class Pending(val amount: Int) : Order
data class Paid(val amount: Int, val txId: String) : Order

fun handle(order: Order) = when (order) {
    is Pending if order.amount > 10_000 -> "high-value pending"
    is Pending -> "pending"
    is Paid -> "paid: ${order.txId}"
}
```

---

**基本写法：多守卫分支**
`is <类型> if <条件> -> ...`
```kotlin
// 同一类型可配多个守卫分支
fun classify(n: Number) = when (n) {
    is Int if n > 0 -> "positive int"
    is Int if n < 0 -> "negative int"
    is Int -> "zero"
    is Double -> "double"
}
```

---

## 多美元字符串插值（2.1 stable）

**基本写法：多美元插值**
`$$"<内容>"`
```kotlin
// Kotlin 2.1 stable，$$ 内单 $ 视为字面量
val name = "Kotlin"
val template = $$"""
    Hello, $$name!
    Your balance is $1000 (USD).
    JSON: {"value": "$$value"}
"""
```

---

**基本写法：更多美元符号**
`$$$"<内容>"`
```kotlin
// $$$ 内 $$ 视为字面量，仅 $$$ 触发插值
val v = "x"
val s = $$$"raw $$ and $ chars, value: $$$v"
```

---

## 非局部 break/continue（2.1 preview → 2.2 stable）

**基本写法：在 inline lambda 中 break**
`<外层循环> { <inline函数> { break@<标签> } }`
```kotlin
// Kotlin 2.1+，从内联 lambda 中跳出外层循环
fun find(matrix: List<List<Int>>, target: Int) {
    outer@ for (row in matrix) {
        row.forEach {
            if (it == target) break@outer
        }
    }
}
```

---

**基本写法：非局部 continue**
`continue@<标签>`
```kotlin
// 跳过外层循环当前迭代
outer@ for (i in 1..10) {
    (1..10).forEach {
        if (it == 5) continue@outer
        println("$i-$it")
    }
}
```

---

## 上下文参数（2.2 preview）

**基本写法：声明上下文参数**
`context(<参数>) fun <函数名>()`
```kotlin
// Kotlin 2.2 preview，隐式依赖注入（替代 context receivers）
class Logger { fun info(msg: String) {} }

context(logger: Logger)
fun calculate(x: Int, y: Int): Int {
    logger.info("calc $x + $y")
    return x + y
}

fun main() {
    val log = Logger()
    with(log) {
        calculate(1, 2)
    }
}
```

---

**基本写法：多上下文参数**
`context(<参数1>, <参数2>) fun <函数名>()`
```kotlin
// 多个隐式依赖
context(logger: Logger, config: Config)
fun load() {
    logger.info("loading with ${config.timeout}")
}
```

---

**基本写法：上下文参数链式传递**
`context(<参数>) fun <函数A>() fun <函数B>()`
```kotlin
// 上下文参数自动向内层传递
context(db: Database)
fun query(sql: String) = db.exec(sql)

context(db: Database)
fun allUsers() = query("SELECT * FROM users")
```

---

## 上下文敏感解析（2.2 preview）

**基本写法：基于接收者的作用域解析**
`fun <接收者>.<方法>()`
```kotlin
// 根据调用位置上下文自动选择重载
class Builder { fun text(s: String) {} }

context(builder: Builder)
fun line(s: String) {
    builder.text(s)
}
```

---

## Base64 与 HexFormat（2.2 stable）

**基本写法：Base64 编解码**
`<字节>.encodeToBase64()`
```kotlin
// Kotlin 2.2 stable API
val bytes = "hello".encodeToByteArray()
val encoded = bytes.encodeToBase64()
val decoded = encoded.decodeFromBase64()
```

---

**基本写法：HexFormat 十六进制**
`HexFormat { ... }`
```kotlin
// 十六进制格式化
val fmt = HexFormat {
    upperCase = true
    bytes.byteSeparator = " "
}
val hex = byteArrayOf(1, 2, 3).toHexString(fmt)
val back = hex.hexToByteArray(fmt)
```

---

## 编译器警告统一管理

**基本写法：统一警告策略**
`allWarningsAsErrors = true`
```kotlin
// build.gradle.kts 中统一配置
kotlin {
    compilerOptions {
        allWarningsAsErrors.set(true)
    }
}
```

---

**基本写法：按需抑制警告**
`@Suppress("<警告ID>")`
```kotlin
// 精确抑制特定警告
@Suppress("UNUSED_PARAMETER")
fun process(unused: String) {}
```

---

## 接口默认方法生成

**基本写法：JVM 默认方法**
`kotlin { jvmToolchain(<版本>) }`
```kotlin
// Kotlin 2.2 改变接口默认方法生成策略
// 通过编译选项控制
kotlin {
    compilerOptions {
        jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_21)
    }
}
```

---

## Kotlin/Native 改进

**基本写法：内存追踪**
`kotlin.native.cacheKind=<模式>`
```properties
# gradle.properties 中配置 Native 内存模式
kotlin.native.cacheKind=static
kotlin.native.memory.metric.reclamation.enable=true
```

---

## Kotlin/Wasm 独立目标

**基本写法：启用 Wasm 目标**
`kotlin { wasmJs { } }`
```kotlin
// build.gradle.kts 中独立配置 Wasm
kotlin {
    wasmJs {
        browser()
        binaries.executable()
    }
}
```



<!-- ============ 文档分隔线：014-kotlin/032-KotlinCompilerCommand.md ============ -->

﻿# Kotlin kotlinc 编译命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本编译

**基本写法：编译单文件**
`kotlinc <源文件> -include-runtime -d <输出jar>`
```bash
# 编译并打包为可执行 jar，附带运行时
kotlinc Main.kt -include-runtime -d app.jar
```

---

**基本写法：运行 jar**
`java -jar <jar文件>`
```bash
# 运行上一步生成的 jar
java -jar app.jar
```

---

**基本写法：编译模块**
`kotlinc <模块名> -include-runtime -d <输出>`
```bash
# 编译整个模块目录
kotlinc src/main/kotlin -include-runtime -d app.jar
```

---

**基本写法：仅编译不打包**
`kotlinc <源> -d <输出目录>`
```bash
# 输出 .class 文件到目录
kotlinc Main.kt -d out
```

---

## 输出目标

**基本写法：指定 JVM 版本**
`kotlinc -jvm-target <版本> -d <输出>`
```bash
# 指定生成的字节码版本
kotlinc Main.kt -jvm-target 21 -d app.jar
```

---

**基本写法：编译为 JavaScript**
`kotlinc -js <源文件> -output <输出js>`
```bash
# 编译为 JavaScript 文件
kotlinc -js Main.kt -output app.js
```

---

**基本写法：编译为 Native 二进制**
`kotlinc-native <源文件> -o <输出名>`
```bash
# 编译为 Kotlin/Native 可执行文件
kotlinc-native Main.kt -o app
```

---

**基本写法：生成 IR**
`kotlinc -js -ir <源> -output <输出>`
```bash
# 使用新 IR 编译器后端
kotlinc -js -ir Main.kt -output app.js
```

---

## 脚本与 REPL

**基本写法：启动 REPL**
`kotlinc`
```bash
# 进入 Kotlin 交互式 REPL
kotlinc
```

---

**基本写法：执行脚本**
`kotlinc -script <脚本.kts> [参数]`
```bash
# 执行 .kts 脚本文件
kotlinc -script build.kts release
```

---

**基本写法：交互式求值**
`kotlinc -e "<代码>"`
```bash
# 直接执行单段代码
kotlinc -e "println(1 + 2)"
```

---

## 依赖与类路径

**基本写法：指定类路径**
`kotlinc -cp <类路径> <源> -d <输出>`
```bash
# 引入 jar 依赖
kotlinc -cp "lib/*" Main.kt -d app.jar
```

---

**基本写法：模块路径**
`kotlinc -module-path <路径> <源>`
```bash
# Java 模块系统支持
kotlinc -module-path mods Main.kt -d out
```

---

**基本写法：生成 Java 模块**
`kotlinc --java-module-path <路径> -d <输出>`
```bash
# 输出 JPMS 兼容模块
kotlinc -module-path mods -java-module-name com.example -d out
```

---

## 编译选项

**基本写法：开启严格可空性**
`kotlinc -Xjsr305=strict <源>`
```bash
# 严格 JSR-305 可空检查
kotlinc -Xjsr305=strict Main.kt -d out
```

---

**基本写法：启用 expect/actual**
`kotlinc -Xmulti-platform <源>`
```bash
# 多平台项目编译
kotlinc -Xmulti-platform commonMain -d out
```

---

**基本写法：开启进阶优化**
`kotlinc -Xopt=kotlin.classes.aligned <源>`
```bash
# 启用特定优化
kotlinc -Xopt=kotlin.classes.aligned Main.kt -d out
```

---

**基本写法：禁用内联**
`kotlinc -Xinline-classes=<模式>`
```bash
# 控制内联类生成
kotlinc -Xinline-classes=true Main.kt -d out
```

---

## 反编译与文档

**基本写法：生成 Kotlin 文档**
`kotlinx-javadoc <源>`
```bash
# 使用 Dokka 生成文档（推荐）
./gradlew dokkaHtml
```

---

**基本写法：反编译查看字节码**
`javap -p -c <class文件>`
```bash
# 查看编译产物字节码
javap -p -c out/Main.class
```

---

## Gradle Kotlin 编译任务

**基本写法：编译命令**
`./gradlew compileKotlin`
```bash
# 触发 Kotlin 编译任务
./gradlew compileKotlin
```

---

**基本写法：编译多平台**
`./gradlew compileKotlinJvm compileKotlinJs`
```bash
# 编译指定目标
./gradlew compileKotlinJvm
./gradlew compileKotlinWasmJs
```

---

**基本写法：增量编译**
`./gradlew compileKotlin -Pkotlin.incremental=true`
```bash
# 启用增量编译（默认开启）
./gradlew compileKotlin --info
```

---

**基本写法：守护进程编译**
`./gradlew compileKotlin --daemon`
```bash
# 使用 Gradle 守护进程加速
./gradlew compileKotlin --daemon
```

---

## Maven Kotlin 编译

**基本写法：Maven 编译**
`mvn compile`
```bash
# 通过 kotlin-maven-plugin 编译
mvn compile
```

---

**基本写法：指定 Kotlin 版本**
`mvn -Dkotlin.version=2.1.0 compile`
```bash
# 覆盖 Kotlin 版本
mvn -Dkotlin.version=2.1.0 compile
```

---

## 调试与诊断

**基本写法：输出编译时间**
`kotlinc --verbose <源>`
```bash
# 详细编译信息
kotlinc --verbose Main.kt -d out
```

---

**基本写法：输出 K2 警告**
`kotlinc -Xrender-internal-diagnostic-names <源>`
```bash
# 显示诊断内部名称
kotlinc -Xrender-internal-diagnostic-names Main.kt -d out
```

---

**基本写法：生成 .kotlin 缓存**
`-Pkotlin.incremental.useClasspathSnapshot=true`
```bash
# 启用类路径快照加速编译
./gradlew compileKotlin -Pkotlin.incremental.useClasspathSnapshot=true
```



<!-- ============ 文档分隔线：014-kotlin/033-KotlinInlineFunctionReified.md ============ -->

﻿# Kotlin 内联函数与 reified 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## inline 内联函数

**基本写法：声明内联函数**
`inline fun <函数名>(<参数>): <返回类型>`
```kotlin
// 函数体在调用处展开，消除 lambda 对象开销
inline fun measure(block: () -> Unit) {
    val start = System.nanoTime()
    block()
    println("cost: ${System.nanoTime() - start}")
}
```

---

**基本写法：内联带返回值**
`inline fun <函数名>(<参数>): <返回类型> = <表达式>`
```kotlin
// 内联函数返回表达式
inline fun twice(x: Int): Int = x * 2
```

---

**基本写法：内联扩展函数**
`inline fun <接收者>.<方法>()`
```kotlin
// 扩展函数内联
inline fun String.shout() = this.uppercase()
```

---

## noinline 与 crossinline

**基本写法：禁止内联的 lambda**
`noinline <参数名>: () -> <返回>`
```kotlin
// 某些 lambda 不想被内联
inline fun run(block1: () -> Unit, noinline block2: () -> Unit) {
    block1()
    block2()
}
```

---

**基本写法：非局部返回控制**
`crossinline <参数名>: () -> Unit`
```kotlin
// 禁止 lambda 非局部返回，常用于嵌套调用
inline fun runInThread(crossinline block: () -> Unit) {
    Thread { block() }.start()
}
```

---

**基本写法：组合使用**
`inline fun f(noinline a, crossinline b)`
```kotlin
// 同时使用 noinline 与 crossinline
inline fun compute(
    noinline log: () -> Unit,
    crossinline task: () -> Unit
) {
    log()
    Thread { task() }.start()
}
```

---

## reified 泛型实化

**基本写法：reified 类型参数**
`inline fun <reified T> <函数名>(): ...`
```kotlin
// 内联函数中可访问泛型类型 T 的 Class
inline fun <reified T> typeOf(): Class<T> = T::class.java
```

---

**基本写法：类型判断**
`inline fun <reified T> isA(<值>: Any): Boolean`
```kotlin
// 运行时判断类型
inline fun <reified T> isA(value: Any): Boolean = value is T
```

---

**基本写法：类型转换**
`inline fun <reified T> cast(<值>): T`
```kotlin
// 安全类型转换
inline fun <reified T> cast(value: Any?): T? = value as? T
```

---

**基本写法：过滤指定类型**
`inline fun <reified T> List<*>.filterIsInstance()`
```kotlin
// 标准库实现原理
inline fun <reified T> List<*>.filterByType(): List<T> =
    filter { it is T }.map { it as T }
```

---

## reified 反射与序列化

**基本写法：Gson 反序列化**
`inline fun <reified T> fromJson(<json>): T`
```kotlin
// reified 让泛型类型在运行时可用
inline fun <reified T> Gson.fromJson(json: String): T =
    fromJson(json, object : TypeToken<T>() {}.type)
```

---

**基本写法：kotlinx.serialization**
`inline fun <reified T> decode(<字符串>)`
```kotlin
// 协程序列化框架通用用法
inline fun <reified T> Json.decodeFromStringCompat(s: String): T =
    decodeFromString(s)
```

---

**基本写法：获取 KClass**
`inline fun <reified T> kClass(): KClass<T>`
```kotlin
// 拿到 KClass 进行反射
inline fun <reified T> kClass(): KClass<T> = T::class
```

---

## 多个 reified 参数

**基本写法：多个实化类型**
`inline fun <reified A, reified B> <函数名>()`
```kotlin
// 多个泛型类型都可实化
inline fun <reified A, reified B> sameType(): Boolean =
    A::class == B::class
```

---

**基本写法：reified 与默认参数**
`inline fun <reified T> <函数>(<参数> = <默认值>)`
```kotlin
// 实化函数可带默认参数
inline fun <reified T> parse(json: String, default: T? = null): T? =
    try { Json.decodeFromString<T>(json) } catch (e: Exception) { default }
```

---

## 内联高阶函数

**基本写法：带接收者的内联**
`inline fun <T> with(<接收者>: T, <块>: T.() -> R): R`
```kotlin
// 类似标准库 with
inline fun <T, R> myWith(receiver: T, block: T.() -> R): R =
    receiver.block()
```

---

**基本写法：let 风格**
`inline fun <T, R> T.myLet(<块>: (T) -> R): R`
```kotlin
// 类似标准库 let
inline fun <T, R> T.myLet(block: (T) -> R): R = block(this)
```

---

## 内联类（value class）

**基本写法：声明内联类**
`@JvmInline value class <名称>(<属性>: <类型>)`
```kotlin
// Java 19+ / Kotlin 1.5+，运行时零分配
@JvmInline
value class UserId(val raw: Long)

fun find(id: UserId) = id.raw
```

---

**基本写法：内联类方法**
`@JvmInline value class <名称>(val <字段>) { fun <方法>() }`
```kotlin
// 内联类可定义方法
@JvmInline
value class Email(val value: String) {
    fun domain() = value.substringAfter("@")
}
```

---

**基本写法：内联类实现接口**
`@JvmInline value class <名称>(...) : <接口>`
```kotlin
// 内联类可实现接口但不能继承类
interface Measurable { fun measure(): Int }

@JvmInline
value class Text(val s: String) : Measurable {
    override fun measure() = s.length
}
```

---

## 内联限制

**基本写法：不可内联的场景**
`// 非内联函数中不能使用 reified`
```kotlin
// reified 必须在内联函数中
// 以下为非法写法：
// fun <T> wrong(): Class<T> = T::class.java

// 必须改写为内联
inline fun <reified T> right(): Class<T> = T::class.java
```

---

**基本写法：public API 内联**
`public inline fun <reified T> api()`
```kotlin
// public 内联函数不能访问 private 成员
class Container {
    private val secret = 42
    // public inline fun leak() = secret  // 编译错误
}
```



<!-- ============ 文档分隔线：014-kotlin/034-KotlinSelectExpression.md ============ -->

﻿# Kotlin Select 表达式 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## select 基础

**基本写法：引入 select**
`import kotlinx.coroutines.selects.select`
```kotlin
// 协程 select 让多个挂起操作竞争，先就绪者胜出
import kotlinx.coroutines.selects.select
import kotlinx.coroutines.*
```

---

**基本写法：select 表达式**
`select { <子句1>; <子句2> }`
```kotlin
// 等待多个 Deferred，先返回者被处理
suspend fun fetchBoth(a: Deferred<String>, b: Deferred<String>): String =
    select {
        a.onAwait { "from A: $it" }
        b.onAwait { "from B: $it" }
    }
```

---

## Deferred onAwait

**基本写法：等待首个完成**
`<Deferred>.onAwait { <处理> }`
```kotlin
// 多个异步任务竞争
val a = async { delay(100); "A" }
val b = async { delay(50);  "B" }
val r = select<String> {
    a.onAwait { "got $it" }
    b.onAwait { "got $it" }
}
```

---

**基本写法：select 返回值**
`select { <子句> }`
```kotlin
// select 是表达式，最后一行决定返回类型
val result: String = select {
    deferred1.onAwait { it }
    deferred2.onAwait { it }
}
```

---

## Channel onReceive / onSend

**基本写法：接收首个可用消息**
`<Channel>.onReceive { <处理> }`
```kotlin
// 从两个 Channel 中接收先就绪的
val r = select<String> {
    chan1.onReceive { "c1: $it" }
    chan2.onReceive { "c2: $it" }
}
```

---

**基本写法：发送到首个可写 Channel**
`<Channel>.onSend(<值>) { <处理> }`
```kotlin
// 选择第一个能接收元素的 Channel
select<Unit> {
    chan1.onSend(item) { println("sent to c1") }
    chan2.onSend(item) { println("sent to c2") }
}
```

---

**基本写法：onReceiveCatching**
`<Channel>.onReceiveCatching { <Result> }`
```kotlin
// 处理 Channel 关闭情况
val r = select<String> {
    chan.onReceiveCatching { result ->
        result.getOrNull() ?: "closed"
    }
}
```

---

## 超时与默认值

**基本写法：配合超时**
`withTimeout(<时间>) { select { ... } }`
```kotlin
// 给 select 加超时上限
val r = withTimeoutOrNull(500) {
    select<String> {
        chan1.onReceive { it }
        chan2.onReceive { it }
    }
} ?: "timeout"
```

---

**基本写法：onTimeout 子句**
`select { onTimeout(<时间>) { <默认> } }`
```kotlin
// 直接在 select 内处理超时
val r = select<String> {
    chan.onReceive { it }
    onTimeout(300) { "default" }
}
```

---

## select 偏好与公平性

**基本写法：默认公平选择**
`select { <子句1>; <子句2> }`
```kotlin
// select 随机选择同时就绪的子句，避免饥饿
val r = select<String> {
    c1.onReceive { "c1" }
    c2.onReceive { "c2" }
}
```

---

**基本写法：优先级子句**
`select { <优先>.onReceive {}; <普通>.onReceive {} }`
```kotlin
// 利用 selectClause 顺序实现弱优先级
val r = select<String> {
    highPriChan.onReceive { "high" }
    lowPriChan.onReceive  { "low" }
}
```

---

## SelectBuilder 进阶

**基本写法：动态子句**
`select { if (<条件>) <子句A> else <子句B> }`
```kotlin
// 按条件加入不同子句
val r = select<String> {
    if (useFirst) c1.onReceive { it }
    else          c2.onReceive { it }
}
```

---

**基本写法：循环 select**
`while (true) select { ... }`
```kotlin
// 持续多路复用
while (isActive) {
    select<Unit> {
        chan1.onReceive { handle1(it) }
        chan2.onReceive { handle2(it) }
    }
}
```

---

## 自定义 SelectClause

**基本写法：实现 onReceive 风格子句**
`fun <R> registerSelectClause(<scope>, <块>)`
```kotlin
// 自定义可被 select 的对象
class MyEvent {
    private val listeners = mutableListOf<(String) -> Unit>()
    fun consume(block: (String) -> Unit) { listeners.add(block) }

    suspend fun selectConsume(): String = select {
        consume { it }
    }
}
```

---

**基本写法：SelectClause1 协议**
`val onEvent: SelectClause1<String>`
```kotlin
// 暴露 SelectClause1 供外部 select
import kotlinx.coroutines.selects.SelectClause1

class Stream {
    val onData: SelectClause1<String> get() = TODO()
}

select<String> {
    stream.onData.onAwait { it }
}
```

---

## 典型场景

**基本写法：负载均衡**
`select { <c1>.onReceive {}; <c2>.onReceive {} }`
```kotlin
// 多个 worker Channel 均衡消费
suspend fun worker(chans: List<Channel<Job>>) {
    while (true) {
        val job = select<Job> {
            chans.forEach { c -> c.onReceive { it } }
        }
        job.run()
    }
}
```

---

**基本写法：扇出（fan-out）**
`select { <input>.onReceive {}; <control>.onReceive {} }`
```kotlin
// 同时处理数据流与控制信号
while (isActive) {
    select<Unit> {
        dataChan.onReceive { process(it) }
        controlChan.onReceive { if (it == "stop") cancel() }
    }
}
```
