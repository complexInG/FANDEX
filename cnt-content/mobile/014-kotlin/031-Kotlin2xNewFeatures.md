# Kotlin 2.x 新特性 语法速查手册

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
