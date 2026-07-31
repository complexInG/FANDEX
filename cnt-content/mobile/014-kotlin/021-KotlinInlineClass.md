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
