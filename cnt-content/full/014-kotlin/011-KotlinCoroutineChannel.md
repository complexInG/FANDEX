---
order: 42
title: Kotlin与协程Channel
module: kotlin
category: Kotlin
difficulty: intermediate
description: Channel热数据流
author: fanquanpp
updated: '2026-08-01'
related:
  - kotlin/协程基础
  - kotlin/Flow冷流与SharedFlow和StateFlow
  - kotlin/协程调度器与上下文
  - kotlin/Kotlin与WebSocket
prerequisites:
  - kotlin/概述与环境配置
---

## 概述

Channel 是 Kotlin 协程中用于协程之间传递数据的并发原语。与 Flow 的冷流不同，Channel 是热通道：发送方发送的数据会立刻传递给接收方，如果没有接收方，发送方会挂起等待。Channel 类似于阻塞队列（BlockingQueue），但所有操作都是非阻塞的挂起函数。

Channel 适用于生产者-消费者模式、协程间通信、事件总线等场景。

## 基础概念

- **Channel**：协程间传递数据的管道，支持多个发送方和接收方
- **SendChannel**：发送端的接口，提供 send 和 trySend 方法
- **ReceiveChannel**：接收端的接口，提供 receive 和 tryReceive 方法
- **Buffer**：Channel 的缓冲区大小，决定了发送方何时挂起
- **Rendezvous**：默认模式，缓冲区为 0，发送方和接收方必须"会合"才能完成传输

## 快速上手

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun main() = runBlocking {
    // 创建一个 Channel
    val channel = Channel<String>()

    // 启动发送协程
    launch {
        channel.send("消息1")
        channel.send("消息2")
        channel.send("消息3")
        channel.close()  // 关闭通道，表示不再发送
    }

    // 接收所有消息
    for (msg in channel) {
        println("收到: $msg")
    }
    println("通道已关闭")
}
```

## 详细用法

### Channel 的不同类型

```kotlin
import kotlinx.coroutines.channels.*

fun channelTypes() = runBlocking {
    // 1. RendezvousChannel（默认）：缓冲区为0，发送和接收必须同时就绪
    val rendezvous = Channel<Int>()  // 等价于 Channel<Int>(0)

    // 2. UnlimitedChannel：缓冲区无限大，send 永远不会挂起
    val unlimited = Channel<Int>(Channel.UNLIMITED)

    // 3. BufferedChannel：指定缓冲区大小
    val buffered = Channel<Int>(10)  // 缓冲区大小为10

    // 4. ConflatedChannel：只保留最新值，旧值会被覆盖
    val conflated = Channel<Int>(Channel.CONFLATED)

    // 演示 ConflatedChannel
    launch {
        conflated.send(1)
        conflated.send(2)
        conflated.send(3)  // 只有3会被保留
    }
    delay(100)
    println(conflated.tryReceive().getOrNull())  // 3
}
```

### 发送和接收

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun sendReceiveDemo() = runBlocking {
    val channel = Channel<Int>()

    launch {
        // send：挂起函数，缓冲区满时挂起
        channel.send(1)
        channel.send(2)
        channel.send(3)
        channel.close()
    }

    // receive：挂起函数，没有数据时挂起
    println(channel.receive())  // 1
    println(channel.receive())  // 2
    println(channel.receive())  // 3

    // tryReceive：非挂起函数，立即返回结果
    val result = channel.tryReceive()
    println(result.isClosed)  // true（通道已关闭）

    // 使用 for 循环接收
    val channel2 = Channel<String>()
    launch {
        channel2.send("A")
        channel2.send("B")
        channel2.close()
    }
    for (item in channel2) {
        println(item)
    }
}
```

### produce 和 consumeEach

Kotlin 提供了便捷的构建器来创建生产者协程：

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun produceDemo() = runBlocking {
    // produce：创建一个生产者协程，返回 ReceiveChannel
    val numbers = produce {
        for (i in 1..5) {
            send(i)
        }
    }

    // consumeEach：消费所有接收到的元素
    numbers.consumeEach { num ->
        println("收到: $num")
    }
}

// 带过滤的生产者
fun CoroutineScope.produceEvens() = produce {
    for (i in 1..10) {
        if (i % 2 == 0) send(i)
    }
}

fun main() = runBlocking {
    val evens = produceEvens()
    evens.consumeEach { println(it) }
    // 输出: 2, 4, 6, 8, 10
}
```

### 管道模式

多个 Channel 可以串联形成管道：

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun CoroutineScope.produceNumbers() = produce {
    var x = 1
    while (true) {
        send(x++)
        delay(100)
    }
}

fun CoroutineScope.squareNumbers(channel: ReceiveChannel<Int>) = produce {
    for (x in channel) {
        send(x * x)
    }
}

fun main() = runBlocking {
    val numbers = produceNumbers()
    val squares = squareNumbers(numbers)

    // 只取前5个结果
    repeat(5) {
        println(squares.receive())
    }
    println("完成")

    // 取消所有协程
    coroutineContext.cancelChildren()
}
```

### 多个协程共享 Channel

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun main() = runBlocking {
    val channel = Channel<String>()

    // 多个发送方
    val senders = List(3) { senderId ->
        launch {
            repeat(3) {
                channel.send("发送方$senderId - 消息$it")
                delay(100)
            }
        }
    }

    // 多个接收方
    val receivers = List(2) { receiverId ->
        launch {
            for (msg in channel) {
                println("接收方$receiverId 收到: $msg")
            }
        }
    }

    // 等待所有发送完成
    senders.forEach { it.join() }
    channel.close()
    delay(500)
    coroutineContext.cancelChildren()
}
```

### BroadcastChannel（已废弃，使用 SharedFlow 替代）

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.flow.*

// 现在推荐使用 SharedFlow 替代 BroadcastChannel
fun sharedFlowDemo() = runBlocking {
    // 创建 SharedFlow，类似广播
    val sharedFlow = MutableSharedFlow<String>()

    // 多个收集者
    val collector1 = launch {
        sharedFlow.collect { println("收集者1: $it") }
    }
    val collector2 = launch {
        sharedFlow.collect { println("收集者2: $it") }
    }

    delay(100)

    // 发送事件，所有收集者都会收到
    sharedFlow.emit("事件1")
    sharedFlow.emit("事件2")

    delay(100)
    collector1.cancel()
    collector2.cancel()
}
```

## 常见场景

### 生产者-消费者模式

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun main() = runBlocking {
    val channel = Channel<Order>()

    // 生产者：接收订单
    launch {
        repeat(10) { i ->
            val order = Order(id = i, item = "商品$i")
            channel.send(order)
            println("下单: $order")
            delay(200)
        }
        channel.close()
    }

    // 消费者：处理订单
    launch {
        for (order in channel) {
            println("处理: $order")
            delay(500)  // 处理比下单慢
        }
        println("所有订单处理完成")
    }
}

data class Order(val id: Int, val item: String)
```

### 事件总线

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

class EventBus {
    private val channel = Channel<Event>(Channel.UNLIMITED)

    // 发布事件
    suspend fun publish(event: Event) {
        channel.send(event)
    }

    // 订阅事件
    fun subscribe(): ReceiveChannel<Event> = channel

    // 关闭
    fun close() = channel.close()
}

data class Event(val type: String, val data: String)

fun main() = runBlocking {
    val bus = EventBus()

    // 订阅者
    launch {
        bus.subscribe().consumeEach { event ->
            println("收到事件: ${event.type} - ${event.data}")
        }
    }

    // 发布事件
    bus.publish(Event("click", "按钮A"))
    bus.publish(Event("scroll", "页面1"))
    delay(500)
    bus.close()
}
```

### 限流器

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

class RateLimiter(private val maxRequests: Int, private val windowMs: Long) {
    private val channel = Channel<Unit>(maxRequests)

    suspend fun acquire() {
        channel.send(Unit)
    }

    fun release() {
        channel.tryReceive()
    }
}

fun main() = runBlocking {
    val limiter = RateLimiter(3, 1000)

    val jobs = List(10) { i ->
        async {
            limiter.acquire()
            println("请求 $i 开始处理")
            delay(500)
            println("请求 $i 完成")
            limiter.release()
        }
    }
    jobs.awaitAll()
}
```

## 注意事项

- **Channel 是热的**：发送的数据如果没有接收者，发送方会挂起（除非有缓冲区）
- **必须关闭 Channel**：不关闭 Channel 会导致接收方永远等待，使用 `close()` 或取消协程
- **Channel 是有损的**：ConflatedChannel 会丢弃旧值，RendezvousChannel 在没有接收者时发送会挂起
- **异常处理**：Channel 的发送和接收都可能抛出异常，需要妥善处理
- **Channel vs Flow**：Channel 适合协程间通信，Flow 适合数据流的转换和收集。大多数场景优先使用 Flow

## 进阶用法

### select 表达式

select 可以同时等待多个 Channel 的结果：

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*
import kotlinx.coroutines.selects.select

fun main() = runBlocking {
    val channel1 = Channel<String>()
    val channel2 = Channel<String>()

    launch {
        delay(100)
        channel1.send("来自通道1")
    }
    launch {
        delay(50)
        channel2.send("来自通道2")
    }

    // select：哪个通道先有数据就处理哪个
    val result = select<String> {
        channel1.onReceive { it }
        channel2.onReceive { it }
    }
    println("最快收到: $result")  // 来自通道2

    channel1.cancel()
    channel2.cancel()
}
```

### Channel 与 Flow 互转

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*
import kotlinx.coroutines.flow.*

fun main() = runBlocking {
    // Channel 转 Flow
    val channel = Channel<Int>()
    val flow = channel.receiveAsFlow()

    launch {
        flow.collect { println("Flow收到: $it") }
    }

    channel.send(1)
    channel.send(2)
    channel.close()
    delay(100)

    // Flow 转 Channel
    val flow2 = flowOf(10, 20, 30)
    val channel2 = flow2.produceIn(this)

    channel2.consumeEach { println("Channel收到: $it") }
}
```

### Ticker Channel

```kotlin
import kotlinx.coroutines.*
import kotlinx.coroutines.channels.*

fun main() = runBlocking {
    // 创建定时通道，每秒发送一次
    val ticker = ticker(1000)

    var count = 0
    for (tick in ticker) {
        println("第${++count}次触发: ${System.currentTimeMillis()}")
        if (count >= 5) break
    }
    ticker.cancel()
}
```

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
| Kotlin DSL 与领域特定语言 | 009-KotlinDSLDomainSpecificLanguage | 本文的并列主题 |
| Kotlin 测试与最佳实践 | 010-KotlinTestBestPractice | 本文的并列主题 |
| Kotlin与协程Channel | 011-KotlinCoroutineChannel | 本文自身 |
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
