---
order: 18
title: 'Kotlin DSL 与领域特定语言'
module: kotlin
category: Kotlin
difficulty: advanced
description: 'DSL 设计模式、带接收者的 Lambda、类型安全构建器与实际项目 DSL 设计。'
author: fanquanpp
updated: '2026-08-01'
related:
  - kotlin/协程进阶
  - kotlin/Kotlin多平台
  - kotlin/测试与最佳实践
  - kotlin/空安全详解
prerequisites: []
---

## 1. DSL 概述

DSL（Domain-Specific Language，领域特定语言）是为特定领域设计的专用语言。Kotlin 的语法特性使其非常适合构建内部 DSL：

- **带接收者的 Lambda**：改变 `this` 上下文
- **扩展函数**：为已有类型添加领域方法
- **中缀函数**：消除点号和括号
- **运算符重载**：自定义运算符语义
- **命名参数**：提升可读性

### 1.1 DSL vs 命令式 API

```kotlin
// 命令式 API
val button = Button()
button.text = "Click me"
button.textColor = Color.RED
button.onClick = { println("Clicked!") }
button.padding = Padding(16, 8, 16, 8)
layout.addView(button)

// DSL 风格
layout {
    button {
        text = "Click me"
        textColor = Color.RED
        onClick { println("Clicked!") }
        padding(16, 8, 16, 8)
    }
}
```

## 2. 带接收者的 Lambda

这是 Kotlin DSL 的核心机制，允许 Lambda 内部直接访问接收者对象的成员：

### 2.1 基本概念

```kotlin
// 普通 Lambda
val lambda: (StringBuilder) -> Unit = { sb ->
    sb.append("Hello")
    sb.append(" World")
}

// 带接收者的 Lambda
val lambdaWithReceiver: StringBuilder.() -> Unit = {
    // this 是 StringBuilder
    append("Hello")  // 等价于 this.append("Hello")
    append(" World")
}

// 使用
val sb = StringBuilder()
sb.lambdaWithReceiver()  // 将 sb 作为接收者传入
```

### 2.2 与 apply/run 的关系

```kotlin
// apply 的实现原理
inline fun <T> T.apply(block: T.() -> Unit): T {
    block()  // this 作为接收者
    return this
}

// run 的实现原理
inline fun <T, R> T.run(block: T.() -> R): R {
    return block()  // this 作为接收者，返回 Lambda 结果
}
```

### 2.3 嵌套接收者

```kotlin
class Table {
    val rows = mutableListOf<Row>()

    fun row(init: Row.() -> Unit) {
        val row = Row()
        row.init()  // 将 row 作为接收者
        rows.add(row)
    }
}

class Row {
    val cells = mutableListOf<Cell>()

    fun cell(text: String, init: Cell.() -> Unit = {}) {
        val cell = Cell(text)
        cell.init()
        cells.add(cell)
    }
}

class Cell(val text: String) {
    var align: Align = Align.LEFT
    var bold: Boolean = false
}

enum class Align { LEFT, CENTER, RIGHT }

// 使用 DSL
val table = Table().apply {
    row {
        cell("Name") { align = Align.CENTER; bold = true }
        cell("Age") { align = Align.CENTER; bold = true }
    }
    row {
        cell("Alice")
        cell("25") { align = Align.CENTER }
    }
}
```

## 3. 类型安全构建器

### 3.1 基础构建器模式

```kotlin
// HTML 构建器示例
class HtmlBuilder {
    private val children = mutableListOf<String>()

    fun head(init: HeadBuilder.() -> Unit) {
        val builder = HeadBuilder()
        builder.init()
        children.add(builder.build())
    }

    fun body(init: BodyBuilder.() -> Unit) {
        val builder = BodyBuilder()
        builder.init()
        children.add(builder.build())
    }

    fun build(): String = "<html>${children.joinToString("")}</html>"
}

class HeadBuilder {
    private val children = mutableListOf<String>()

    fun title(text: String) {
        children.add("<title>$text</title>")
    }

    fun build(): String = "<head>${children.joinToString("")}</head>"
}

class BodyBuilder {
    private val children = mutableListOf<String>()

    fun h1(text: String) {
        children.add("<h1>$text</h1>")
    }

    fun p(text: String) {
        children.add("<p>$text</p>")
    }

    fun div(init: DivBuilder.() -> Unit) {
        val builder = DivBuilder()
        builder.init()
        children.add(builder.build())
    }

    fun build(): String = "<body>${children.joinToString("")}</body>"
}

class DivBuilder {
    var className: String = ""
    private val children = mutableListOf<String>()

    fun p(text: String) {
        children.add("<p>$text</p>")
    }

    fun build(): String = """<div class="$className">${children.joinToString("")}</div>"""
}

// 使用
fun html(init: HtmlBuilder.() -> Unit): String {
    val builder = HtmlBuilder()
    builder.init()
    return builder.build()
}

val page = html {
    head {
        title("My Page")
    }
    body {
        h1("Welcome")
        div {
            className = "content"
            p("Hello, Kotlin DSL!")
        }
    }
}
```

### 3.2 使用 @DslMarker 限制作用域

默认情况下，嵌套 Lambda 可以访问外层接收者的方法，可能导致意外调用：

```kotlin
@DslMarker
annotation class HtmlDsl

@HtmlDsl
class TableBuilder {
    fun tr(init: TrBuilder.() -> Unit) { /* ... */ }
}

@HtmlDsl
class TrBuilder {
    fun td(text: String) { /* ... */ }
    // 有了 @HtmlDsl，在 tr 块中不能调用外层 TableBuilder 的方法
}

// 编译器会阻止跨层调用
table {
    tr {
        // td()  // OK
        // tr()  // 编译错误！不能调用外层 TableBuilder 的 tr
    }
}
```

## 4. 中缀函数

中缀函数让 DSL 更接近自然语言：

```kotlin
infix fun String.should(equal: String) = this == equal
infix fun String.should(contain: String) = this.contains(contain)
infix fun String.should(startWith: String) = this.startsWith(startWith)

// 使用
"hello" should equal "hello"
"hello world" should contain "world"
"hello" should startWith "he"

// 更复杂的例子
infix fun Int.times(action: () -> Unit) {
    repeat(this) { action() }
}

5 times { print("Hello ") }  // Hello Hello Hello Hello Hello
```

## 5. 运算符重载

```kotlin
// 向量运算
data class Vector(val x: Double, val y: Double) {
    operator fun plus(other: Vector) = Vector(x + other.x, y + other.y)
    operator fun minus(other: Vector) = Vector(x - other.x, y - other.y)
    operator fun times(scalar: Double) = Vector(x * scalar, y * scalar)
    operator fun div(scalar: Double) = Vector(x / scalar, y / scalar)
    operator fun unaryMinus() = Vector(-x, -y)
}

val v1 = Vector(1.0, 2.0)
val v2 = Vector(3.0, 4.0)
val result = v1 + v2 * 2.0 - Vector(0.5, 0.5)
```

## 6. Gradle Kotlin DSL

Gradle Kotlin DSL 是 Kotlin DSL 最广泛的应用之一：

```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "2.2.0"
    `java-library`
    `maven-publish`
}

dependencies {
    implementation(kotlin("stdlib"))
    implementation("io.ktor:ktor-client-core:3.0.0")

    testImplementation(kotlin("test"))
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(17)
}

publishing {
    publications {
        create<MavenPublication>("maven") {
            from(components["java"])
            groupId = "com.example"
            artifactId = "my-library"
            version = "1.0.0"
        }
    }
}
```

## 7. kotlinx.html DSL

kotlinx.html 是 Kotlin 的类型安全 HTML 构建库：

```kotlin
import kotlinx.html.*
import kotlinx.html.stream.createHTML

val html = createHTML().html {
    head {
        meta(charset = "utf-8")
        title("My Page")
        style {
            unsafe {
                +"""
                body { font-family: sans-serif; }
                .container { max-width: 800px; margin: 0 auto; }
                """
            }
        }
    }
    body {
        div(classes = "container") {
            h1 { +"Welcome" }
            p { +"This is a Kotlin HTML DSL example." }
            ul {
                for (i in 1..5) {
                    li { +"Item $i" }
                }
            }
            form(action = "/submit", method = FormMethod.post) {
                label { +"Name: " }
                input(type = InputType.text, name = "name") {
                    placeholder = "Enter your name"
                }
                br
                button(type = ButtonType.submit) { +"Submit" }
            }
        }
    }
}
```

## 8. 实际项目 DSL 设计

### 8.1 API 路由 DSL

```kotlin
// 路由 DSL 设计
class RouteBuilder {
    private val routes = mutableListOf<Route>()

    fun get(path: String, handler: suspend (Context) -> Unit) {
        routes.add(Route(HttpMethod.Get, path, handler))
    }

    fun post(path: String, handler: suspend (Context) -> Unit) {
        routes.add(Route(HttpMethod.Post, path, handler))
    }

    fun group(path: String, init: RouteBuilder.() -> Unit) {
        val builder = RouteBuilder()
        builder.init()
        builder.routes.forEach { route ->
            routes.add(route.copy(path = path + route.path))
        }
    }

    fun build(): List<Route> = routes.toList()
}

fun routes(init: RouteBuilder.() -> Unit): List<Route> {
    return RouteBuilder().apply(init).build()
}

// 使用
val appRoutes = routes {
    get("/") { ctx -> ctx.respond("Welcome") }
    get("/users") { ctx -> ctx.respond(userService.findAll()) }

    group("/api") {
        get("/status") { ctx -> ctx.respond("OK") }

        group("/v1") {
            get("/users") { ctx -> ctx.respond(userService.findAll()) }
            post("/users") { ctx -> ctx.respond(userService.create(ctx.body())) }
        }
    }
}
```

### 8.2 配置 DSL

```kotlin
class AppConfig {
    var name: String = "MyApp"
    var debug: Boolean = false
    private val servers = mutableListOf<ServerConfig>()

    fun server(init: ServerConfig.() -> Unit) {
        servers.add(ServerConfig().apply(init))
    }

    internal fun build() = ConfigData(name, debug, servers.toList())
}

class ServerConfig {
    var host: String = "localhost"
    var port: Int = 8080
    var ssl: Boolean = false
}

fun config(init: AppConfig.() -> Unit): ConfigData {
    return AppConfig().apply(init).build()
}

// 使用
val appConfig = config {
    name = "Production App"
    debug = false

    server {
        host = "0.0.0.0"
        port = 443
        ssl = true
    }

    server {
        host = "127.0.0.1"
        port = 8080
    }
}
```

### 8.3 测试 DSL

```kotlin
class TestContext {
    private val givenSteps = mutableListOf<String>()
    private val whenSteps = mutableListOf<String>()
    private val thenSteps = mutableListOf<String>()

    fun given(description: String, action: () -> Unit) {
        givenSteps.add(description)
        action()
    }

    fun `when`(description: String, action: () -> Unit) {
        whenSteps.add(description)
        action()
    }

    fun then(description: String, assertion: () -> Boolean) {
        thenSteps.add(description)
        check(assertion()) { "Assertion failed: $description" }
    }
}

fun test(init: TestContext.() -> Unit) = TestContext().apply(init)

// 使用
test {
    given("a user with admin role") {
        user = User(role = Role.ADMIN)
    }
    `when`("user accesses admin panel") {
        result = accessPanel(user)
    }
    then("access is granted") {
        result == Access.GRANTED
    }
}
```

## 9. DSL 设计原则

1. **最小化嵌套**：避免过深的嵌套层级，3 层以内为佳
2. **使用 @DslMarker**：防止作用域泄漏，确保类型安全
3. **提供合理默认值**：减少必填参数，降低使用门槛
4. **保持不可变性**：构建器内部可变，构建结果不可变
5. **命名清晰**：DSL 方法名应接近领域语言，避免技术术语
6. **文档和示例**：DSL 的正确用法需要清晰的文档和示例

## 参考文献



Kotlin 官方文档：https://kotlinlang.org/docs/home.html
Kotlin 协程指南：https://kotlinlang.org/docs/coroutines-guide.html
Compose Multiplatform：https://www.jetbrains.com/compose-multiplatform/
Ktor 框架：https://ktor.io/
Android 开发者文档：https://developer.android.com/kotlin

## 延伸阅读



Kotlin 基础语法精讲，见 014-kotlin/002-KotlinBasicSyntax 文档。
协程与 Flow，见 014-kotlin 模块协程文档。
Android 与 HarmonyOS 应用开发，见 018-harmonyos 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Kotlin 课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 协程调度与 Flow 背压

协程调度器决定线程切换：Dispatchers.Main 走 Android 主线程，IO 用于阻塞 I/O，Default 用于 CPU 密集；withContext 切换上下文而不阻塞调用方。
Flow 是冷流：每次收集重新执行；`flowOn` 切换上游上下文，`buffer` 缓冲背压，`conflate` 丢弃中间值。
StateFlow 持有最新值并去重，适合 UI 状态；SharedFlow 支持多订阅与事件广播。
取消协作：挂起点检查取消状态并抛出 CancellationException；耗时计算需周期调用 ensureActive。

### 13.2 KMP 多平台架构

KMP 项目以 kotlin-multiplatform 插件定义 targets（jvm、iosArm64、js 等）；commonMain 中 expect 声明，平台源集 actual 实现。
依赖管理：commonMain 使用 kotlinx 库（coroutines、serialization、datetime），平台差异库放对应源集。
与 Compose Multiplatform 组合时，UI 逻辑共享、平台能力通过 expect/actual 隔离。
构建产物：Android 输出 AAR，iOS 输出 framework；通过 CocoaPods 或 Swift Package 集成。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Kotlin 概述与环境配置 | 001-KotlinOverviewEnvSetup | 本文的前置基础 |
| Kotlin 基础语法 | 002-KotlinBasicSyntax | 本文的前置基础 |
| Kotlin 函数与 Lambda | 003-KotlinFunctionAndLambda | 本文的并列主题 |
| Kotlin 类与对象 | 004-KotlinClassObject | 本文的并列主题 |
| Kotlin 泛型与类型系统 | 005-KotlinGenericTypeSystem | 本文的并列主题 |
| Kotlin 集合与协程 | 006-KotlinCollectionCoroutine | 本文的并列主题 |
| Kotlin 协程进阶 | 007-KotlinCoroutineAdvanced | 本文的并列主题 |
| Kotlin 多平台 | 008-KotlinMultiplatform | 本文的并列主题 |
| Kotlin DSL 与领域特定语言 | 009-KotlinDSLDomainSpecificLanguage | 本文自身 |
| Kotlin 测试与最佳实践 | 010-KotlinTestBestPractice | 本文的并列主题 |
| Kotlin与协程Channel | 011-KotlinCoroutineChannel | 本文的并列主题 |
| 空安全详解 | 012-NullSafetyDetailed | 本文的安全延伸 |
| 密封类与代数数据类型 | 013-SealedClassAlgebraicDataType | 本文的并列主题 |
| 委托属性 | 014-DelegateProperty | 本文的并列主题 |
| 扩展函数 | 015-ExtensionFunction | 本文的并列主题 |
| 协程基础 | 016-CoroutineBasics | 本文的前置基础 |
| Flow与响应式流 | 017-FlowReactiveStream | 本文的并列主题 |
| Kotlin作用域函数 | 018-KotlinScopeFunction | 本文的并列主题 |
| Kotlin集合操作 | 019-KotlinCollectionOperation | 本文的并列主题 |
| Kotlin内联类 | 020-KotlinInlineClass | 本文的并列主题 |
| Kotlin 契约（Contracts） | 021-KotlinContractContracts | 本文的并列主题 |
| Kotlin与DSL | 022-KotlinDSL | 本文的并列主题 |
| Kotlin序列化 | 023-KotlinSerialization | 本文的并列主题 |
| Kotlin与Android | 024-KotlinAndroid | 本文的并列主题 |
| Kotlin与Spring | 025-KotlinSpring | 本文的并列主题 |
| Kotlin类型系统 | 026-KotlinTypeSystem | 本文的并列主题 |
| Kotlin与Compose | 027-KotlinCompose | 本文的并列主题 |
| Kotlin与Arrow | 028-KotlinArrow | 本文的并列主题 |
| Kotlin与Ktor | 029-KotlinKtor | 本文的并列主题 |
| Kotlin与Exposed | 030-KotlinExposed | 本文的并列主题 |
| Kotlin与Koin | 031-KotlinKoin | 本文的并列主题 |
| Kotlin与ktor-client | 032-KotlinKtorClient | 本文的并列主题 |
| Kotlin与测试 | 033-KotlinTest | 本文的并列主题 |
| Kotlin与编译器插件 | 034-KotlinCompilerPlugin | 本文的并列主题 |
| Kotlin与Gradle | 035-KotlinGradle | 本文的并列主题 |
| Kotlin与原子操作 | 036-KotlinAtomicOperation | 本文的并列主题 |
| Kotlin与Benchmark | 037-KotlinBenchmark | 本文的并列主题 |
| Kotlin与IO | 038-KotlinIO | 本文的并列主题 |
| Kotlin 与正则表达式 | 039-KotlinRegex | 本文的并列主题 |
| Kotlin与时间 | 040-KotlinTime | 本文的并列主题 |
| Kotlin与并发安全 | 041-KotlinConcurrencySafety | 本文的安全延伸 |
| Kotlin与WebSocket | 042-KotlinWebSocket | 本文的并列主题 |
| Kotlin与安全 | 043-KotlinSecurity | 本文的安全延伸 |
| 协程调度器与上下文 | 044-CoroutineDispatcherContext | 本文的并列主题 |
| Flow冷流与SharedFlow和StateFlow | 045-FlowColdSharedState | 本文的并列主题 |
| Channel与BroadcastChannel | 046-ChannelBroadcastChannel | 本文的并列主题 |
| 密封类与密封接口 | 047-SealedClassSealedInterface | 本文的并列主题 |
| 内联类 | 048-InlineClass | 本文的并列主题 |
| 扩展函数的编译原理 | 049-ExtensionFunctionCompilePrinciple | 本文的原理深化 |
| 作用域函数区别 | 050-ScopeFunctionDifference | 本文的并列主题 |
| 协程异常处理 | 051-CoroutineExceptionHandling | 本文的并列主题 |
| Kotlin跨平台 | 052-KotlinCrossPlatform | 本文的并列主题 |
| Kotlin Flow 进阶 | 053-FlowAdvanced | 本文的并列主题 |
