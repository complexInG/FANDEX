---
order: 530
title: Kotlin Flow 进阶
module: kotlin

category: '014-kotlin'
difficulty: beginner
description: Kotlin Flow 进阶 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 延伸阅读
Kotlin 基础语法精讲，见 014-kotlin/002-KotlinBasicSyntax 文档。
协程与 Flow，见 014-kotlin 模块协程文档。
Android 与 HarmonyOS 应用开发，见 018-harmonyos 模块。
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
