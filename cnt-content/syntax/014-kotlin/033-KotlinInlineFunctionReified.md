# Kotlin 内联函数与 reified 语法速查手册

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
