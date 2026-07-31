# Kotlin 协程进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Job 与 Deferred

**基本写法：启动协程获取 Job**
`val <变量> = scope.launch { }`
```kotlin
// 启动协程返回 Job
val job = scope.launch { doWork() }
```

---

**基本写法：async 返回 Deferred**
`val <变量> = scope.async { <表达式> }`
```kotlin
// async 启动并返回结果
val deferred = scope.async { compute() }
val r = deferred.await()
```

---

**基本写法：等待多个 Deferred**
`awaitAll(<deferred1>, <deferred2>)`
```kotlin
// 并发等待多个结果
val (a, b) = listOf(d1, d2).awaitAll().let { it[0] to it[1] }
```

---

## Job 生命周期

**基本写法：判断活跃**
`<job>.isActive`
```kotlin
// 判断协程是否活跃
if (job.isActive) { }
```

---

**基本写法：判断完成**
`<job>.isCompleted`
```kotlin
// 判断协程是否完成
if (job.isCompleted) { }
```

---

**基本写法：判断取消**
`<job>.isCancelled`
```kotlin
// 判断协程是否被取消
if (job.isCancelled) { }
```

---

## 取消协程

**基本写法：取消协程**
`<job>.cancel()`
```kotlin
// 取消协程
job.cancel()
```

---

**基本写法：取消并等待**
`<job>.cancelAndJoin()`
```kotlin
// 取消并阻塞等待完成
job.cancelAndJoin()
```

---

**基本写法：响应取消**
`if (!isActive) return`
```kotlin
// 协程内主动检查取消
if (!isActive) return
```

---

**基本写法：确保取消检查**
`currentCoroutineContext().ensureActive()`
```kotlin
// 显式抛出取消异常
currentCoroutineContext().ensureActive()
```

---

## 超时控制

**基本写法：超时抛异常**
`withTimeout(<毫秒>) { }`
```kotlin
// 超时抛 TimeoutCancellationException
withTimeout(1000) { doWork() }
```

---

**基本写法：超时返回 null**
`withTimeoutOrNull(<毫秒>) { }`
```kotlin
// 超时返回 null 不抛异常
val r = withTimeoutOrNull(1000) { doWork() }
```

---

## 启动模式 CoroutineStart

**基本写法：默认立即调度**
`launch(start = CoroutineStart.DEFAULT) { }`
```kotlin
// 立即调度执行
launch(start = CoroutineStart.DEFAULT) { }
```

---

**基本写法：懒加载启动**
`launch(start = CoroutineStart.LAZY) { }`
```kotlin
// 调用 join 或 start 才执行
val job = scope.launch(start = CoroutineStart.LAZY) { }
job.start()
```

---

**基本写法：原子启动**
`launch(start = CoroutineStart.ATOMIC) { }`
```kotlin
// 不可在执行前取消
launch(start = CoroutineStart.ATOMIC) { }
```

---

**基本写法：不调度启动**
`launch(start = CoroutineStart.UNDISPATCHED) { }`
```kotlin
// 在当前线程执行直到第一个挂起点
launch(start = CoroutineStart.UNDISPATCHED) { }
```

---

## 协程作用域

**基本写法：创建作用域**
`CoroutineScope(<上下文>)`
```kotlin
// 创建独立作用域
val scope = CoroutineScope(Dispatchers.Default)
```

---

**基本写法：coroutineScope 子作用域**
`coroutineScope { }`
```kotlin
// 等待所有子协程完成
coroutineScope {
    launch { }
    launch { }
}
```

---

**基本写法：supervisorScope 容错**
`supervisorScope { }`
```kotlin
// 子协程异常不互相影响
supervisorScope {
    launch { }
    launch { }
}
```

---

## 挂起函数

**基本写法：定义挂起函数**
`suspend fun <方法名>() {}`
```kotlin
// 定义挂起函数
suspend fun fetch(): String {
    delay(100)
    return "data"
}
```

---

**基本写法：挂起函数调用**
`<挂起函数>()`
```kotlin
// 在协程中调用挂起函数
suspend fun work() { fetch() }
```

---

## 延迟与挂起

**基本写法：延迟**
`delay(<毫秒>)`
```kotlin
// 非阻塞延迟
delay(500)
```

---

**基本写法：按 Duration 延迟**
`delay(<时长>.<单位>)`
```kotlin
// 使用 Duration 字面量延迟
delay(500.milliseconds)
```

---

## 协程上下文操作

**基本写法：切换调度器**
`withContext(<dispatcher>) { }`
```kotlin
// 切换到 IO 调度器
withContext(Dispatchers.IO) { readFile() }
```

---

**基本写法：组合上下文元素**
`<job> + <dispatcher>`
```kotlin
// 组合 Job 与 Dispatcher
val ctx = Job() + Dispatchers.IO
```

---

## runBlocking 阻塞

**基本写法：阻塞启动协程**
`runBlocking { }`
```kotlin
// 阻塞主线程启动协程
runBlocking { doWork() }
```

---

**基本写法：带调度器**
`runBlocking(<dispatcher>) { }`
```kotlin
// 指定调度器阻塞
runBlocking(Dispatchers.Default) { }
```

---

## select 等待多路

**基本写法：select 多路复用**
`select<<返回类型>> { <分支> }`
```kotlin
// 等待首个就绪结果
val r = select<String> {
    deferred1.onAwait { "a" }
    deferred2.onAwait { "b" }
}
```

---

## SupervisorJob

**基本写法：创建 SupervisorJob**
`SupervisorJob()`
```kotlin
// 子协程失败不影响其他子协程
val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)
```

---

## 协程命名

**基本写法：命名协程**
`CoroutineName("<名称>")`
```kotlin
// 为协程命名便于调试
launch(CoroutineName("worker")) { }
```
