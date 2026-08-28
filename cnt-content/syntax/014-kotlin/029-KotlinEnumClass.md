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
