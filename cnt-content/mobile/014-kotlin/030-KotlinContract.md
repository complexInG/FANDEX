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
