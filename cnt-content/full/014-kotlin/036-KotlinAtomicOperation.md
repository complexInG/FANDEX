---
order: 76
title: Kotlin与原子操作
module: kotlin
category: Kotlin
difficulty: intermediate
description: kotlinx.atomicfu
author: fanquanpp
updated: '2026-08-01'
related:
  - kotlin/Kotlin与编译器插件
  - kotlin/Kotlin与DSL
  - kotlin/Kotlin与Benchmark
  - kotlin/Kotlin与IO
prerequisites:
  - kotlin/概述与环境配置
---

## 概述

原子操作（Atomic Operation）是不可被中断的操作。在多线程环境中，多个线程可能同时读写同一个变量，导致数据竞争和不确定的结果。原子操作通过硬件级别的指令保证操作的原子性，不需要加锁就能实现线程安全。

Kotlin 提供的 kotlinx.atomicfu 库是对原子操作的封装，API 简洁，且通过编译器插件在编译期将原子变量转换为 Java 的 AtomicInteger、AtomicReference 等，运行时零额外开销。

## 基础概念

- **原子变量**：使用 `atomic()` 创建的变量，所有读写操作都是线程安全的
- **CAS（Compare-And-Swap）**：原子操作的核心原理，先比较当前值是否等于预期值，如果相等则更新为新值，整个过程不可中断
- **lock-free**：无锁编程，通过原子操作而非锁来实现并发安全，性能更好
- **atomicfu 插件**：编译器插件，将 `atomic()` 调用转换为 Java 原子类，消除运行时开销

## 快速上手

添加依赖和插件：

```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "2.0.0"
    id("org.jetbrains.kotlinx.atomicfu") version "0.24.0"
}

dependencies {
    implementation("org.jetbrains.kotlinx:atomicfu:0.24.0")
}
```

最简单的原子计数器：

```kotlin
import kotlinx.atomicfu.atomic

class Counter {
    // 创建原子整数，初始值为 0
    private val count = atomic(0)

    // 原子递增
    fun increment(): Int = count.incrementAndGet()

    // 获取当前值
    fun get(): Int = count.value
}

fun main() {
    val counter = Counter()
    // 多线程安全递增
    val threads = (1..10).map {
        Thread {
            repeat(1000) { counter.increment() }
        }
    }
    threads.forEach { it.start() }
    threads.forEach { it.join() }
    // 结果一定是 10000，不会丢失更新
    println("最终计数: ${counter.get()}")
}
```

## 详细用法

### 原子整数操作

```kotlin
import kotlinx.atomicfu.atomic

class AtomicIntDemo {
    private val value = atomic(0)

    fun demo() {
        // 基本读写
        val current = value.value          // 读取当前值
        value.value = 10                   // 设置新值

        // 原子递增/递减
        value.incrementAndGet()            // 先加1，再返回新值
        value.getAndIncrement()            // 先返回当前值，再加1
        value.decrementAndGet()            // 先减1，再返回新值
        value.getAndDecrement()            // 先返回当前值，再减1

        // 原子加减
        value.addAndGet(5)                 // 加5，返回新值
        value.getAndAdd(5)                 // 先返回当前值，再加5

        // CAS 操作：如果当前值等于预期值，则更新
        value.compareAndSet(10, 20)        // 如果当前值是10，则设为20，返回是否成功
    }
}
```

### 原子布尔操作

```kotlin
import kotlinx.atomicfu.atomic

class AtomicBoolDemo {
    // 原子布尔值，常用于标志位
    private val running = atomic(false)

    fun start() {
        // 如果当前是 false，则设为 true（防止重复启动）
        if (running.compareAndSet(false, true)) {
            println("启动成功")
        } else {
            println("已经在运行中")
        }
    }

    fun stop() {
        running.value = false
    }

    fun isRunning(): Boolean = running.value
}
```

### 原子引用操作

```kotlin
import kotlinx.atomicfu.atomic
import kotlinx.atomicfu.update
import kotlinx.atomicfu.getAndUpdate

class AtomicRefDemo {
    // 原子引用，可以指向任何对象
    private val state = atomic("INITIAL")

    fun demo() {
        // 读取当前值
        val current = state.value

        // CAS 更新
        state.compareAndSet("INITIAL", "RUNNING")

        // 无条件更新（基于 CAS 循环实现）
        state.update { it.lowercase() }

        // 先获取旧值，再更新
        val oldValue = state.getAndUpdate { it.uppercase() }
        println("旧值: $oldValue, 新值: ${state.value}")
    }
}
```

### 原子更新复杂数据

```kotlin
import kotlinx.atomicfu.atomic
import kotlinx.atomicfu.update

data class Config(val host: String, val port: Int, val timeout: Int)

class ConfigManager {
    // 原子引用持有不可变配置对象
    private val config = atomic(Config("localhost", 8080, 30000))

    fun getConfig(): Config = config.value

    // 原子更新配置（创建新对象替换旧对象）
    fun updateHost(newHost: String) {
        config.update { it.copy(host = newHost) }
    }

    fun updatePort(newPort: Int) {
        config.update { it.copy(port = newPort) }
    }

    fun updateTimeout(newTimeout: Int) {
        config.update { it.copy(timeout = newTimeout) }
    }
}

fun main() {
    val manager = ConfigManager()
    manager.updateHost("example.com")
    manager.updatePort(9090)
    println(manager.getConfig())  // Config(host=example.com, port=9090, timeout=30000)
}
```

## 常见场景

### 线程安全的单例

```kotlin
import kotlinx.atomicfu.atomic
import kotlinx.atomicfu.locks.ReentrantLock

class ConnectionPool private constructor() {
    companion object {
        private val instance = atomic<ConnectionPool?>(null)

        fun getInstance(): ConnectionPool {
            // 双重检查锁定模式
            var pool = instance.value
            if (pool == null) {
                instance.compareAndSet(null, ConnectionPool())
                pool = instance.value!!
            }
            return pool
        }
    }
}
```

### 限流器

```kotlin
import kotlinx.atomicfu.atomic

class RateLimiter(private val maxRequests: Int, private val windowMs: Long) {
    private val count = atomic(0)
    private val windowStart = atomic(System.currentTimeMillis())

    fun tryAcquire(): Boolean {
        val now = System.currentTimeMillis()
        // 如果时间窗口过期，重置计数
        if (now - windowStart.value >= windowMs) {
            windowStart.compareAndSet(windowStart.value, now)
            count.value = 0
        }
        // 尝试增加计数
        while (true) {
            val current = count.value
            if (current >= maxRequests) return false
            if (count.compareAndSet(current, current + 1)) return true
        }
    }
}

fun main() {
    // 每秒最多允许 5 个请求
    val limiter = RateLimiter(maxRequests = 5, windowMs = 1000)
    repeat(10) {
        println("请求 $it: ${if (limiter.tryAcquire()) "通过" else "拒绝"}")
    }
}
```

### 线程安全的栈

```kotlin
import kotlinx.atomicfu.atomic

class LockFreeStack<T> {
    private val top = atomic<Node<T>?>(null)

    private class Node<T>(val value: T, val next: Node<T>?)

    // 原子压栈
    fun push(value: T) {
        while (true) {
            val currentTop = top.value
            val newNode = Node(value, currentTop)
            if (top.compareAndSet(currentTop, newNode)) return
        }
    }

    // 原子弹栈
    fun pop(): T? {
        while (true) {
            val currentTop = top.value ?: return null
            if (top.compareAndSet(currentTop, currentTop.next)) {
                return currentTop.value
            }
        }
    }

    fun isEmpty(): Boolean = top.value == null
}
```

## 注意事项

- **必须使用 atomicfu 编译器插件**：没有插件，原子变量在运行时会有额外包装开销
- **不要在原子操作中做耗时操作**：CAS 循环在竞争激烈时可能自旋很久，不要在其中做 IO 或长时间计算
- **value 属性 vs get()**：在 atomicfu 中，使用 `.value` 读写原子变量，这是 Kotlin 风格的 API
- **ABA 问题**：简单的 CAS 可能遇到 ABA 问题（值从 A 变成 B 又变回 A），如果需要解决，考虑使用版本号
- **原子引用更新不可变对象**：更新原子引用时，应该创建新对象（如 data class 的 copy），而不是修改对象内部状态

## 进阶用法

### 原子数组

```kotlin
import kotlinx.atomicfu.atomic

class AtomicArrayDemo {
    // 原子数组
    private val array = atomicArrayOfNulls<String>(10)

    fun demo() {
        // 设置指定位置的值
        array[0].value = "Hello"
        array[1].value = "World"

        // 读取
        println(array[0].value)  // Hello

        // CAS 更新指定位置
        array[0].compareAndSet("Hello", "Hi")
    }
}
```

### 与协程配合

```kotlin
import kotlinx.atomicfu.atomic
import kotlinx.coroutines.*

class CoroutineCounter {
    private val count = atomic(0)

    suspend fun incrementConcurrently() = coroutineScope {
        val jobs = List(100) {
            launch(Dispatchers.Default) {
                repeat(1000) {
                    count.incrementAndGet()
                }
            }
        }
        jobs.forEach { it.join() }
        println("最终计数: ${count.value}")  // 一定是 100000
    }
}
```

### 自旋锁

```kotlin
import kotlinx.atomicfu.atomic

class SpinLock {
    private val locked = atomic(false)

    fun lock() {
        // 自旋等待，直到获取锁
        while (!locked.compareAndSet(false, true)) {
            // 可以加入 yield 让出 CPU
            Thread.yield()
        }
    }

    fun unlock() {
        locked.value = false
    }
}

// 使用方式
fun main() {
    val lock = SpinLock()
    lock.lock()
    try {
        // 临界区代码
        println("执行受保护的操作")
    } finally {
        lock.unlock()
    }
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
| Kotlin与原子操作 | 036-KotlinAtomicOperation | 本文自身 |
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
