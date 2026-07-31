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
