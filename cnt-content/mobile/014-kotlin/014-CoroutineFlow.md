# Kotlin 协程与 Flow 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 协程基础

**基本写法：launch 启动协程**
`GlobalScope.launch { <代码> }`
```kotlin
// 启动新协程（不阻塞）
GlobalScope.launch {
    delay(1000)
    println("Hello")
}
```

---

**基本写法：async 异步返回**
`GlobalScope.async { <返回值> }`
```kotlin
// 异步计算结果
val deferred = GlobalScope.async {
    delay(1000)
    42
}
val result = deferred.await()
```

---

**基本写法：runBlocking 阻塞启动**
`runBlocking { <代码> }`
```kotlin
// 阻塞主线程启动协程
runBlocking {
    launch { println("Hello") }
}
```

---

**基本写法：suspend 挂起函数**
`suspend fun <函数名>(<参数>): <返回类型> { ... }`
```kotlin
// 声明挂起函数
suspend fun fetchData(): String {
    delay(1000)
    return "Data"
}
```

---

**基本写法：CoroutineScope 自定义作用域**
`CoroutineScope(<上下文>).launch { <代码> }`
```kotlin
// 创建作用域
val scope = CoroutineScope(Dispatchers.Main)
scope.launch { /* UI 操作 */ }
```

---

## 调度器

**基本写法：Dispatchers.Main 主线程**
`withContext(Dispatchers.Main) { <代码> }`
```kotlin
// 切换到主线程
withContext(Dispatchers.Main) {
    updateUI()
}
```

---

**基本写法：Dispatchers.IO IO 线程**
`withContext(Dispatchers.IO) { <代码> }`
```kotlin
// 切换到 IO 线程
withContext(Dispatchers.IO) {
    val data = readFromFile()
}
```

---

**基本写法：Dispatchers.Default 计算线程**
`withContext(Dispatchers.Default) { <代码> }`
```kotlin
// CPU 密集型任务
withContext(Dispatchers.Default) {
    val result = heavyCompute()
}
```

---

## Job 控制

**基本写法：cancel 取消**
`<job>.cancel();`
```kotlin
// 取消协程
val job = launch { repeat(100) { delay(100) } }
job.cancel()
```

---

**基本写法：join 等待完成**
`<job>.join();`
```kotlin
// 等待协程完成
job.join()
```

---

**基本写法：cancelAndJoin 取消并等待**
`<job>.cancelAndJoin();`
```kotlin
// 取消并等待完成
job.cancelAndJoin()
```

---

**基本写法：isActive 检查活跃**
`<coroutineScope>.isActive`
```kotlin
// 检查协程是否仍活跃
while (isActive) {
    // 执行工作
}
```

---

## Flow 流

**基本写法：flow 构建流**
`flow { <emit 调用> }`
```kotlin
// 创建 Flow
val flow = flow {
    for (i in 1..3) {
        emit(i)
    }
}
```

---

**基本写法：collect 收集**
`<flow>.collect { <处理> }`
```kotlin
// 收集 Flow 数据
flow.collect { value ->
    println(value)
}
```

---

**基本写法：map 转换**
`<flow>.map { <转换> }`
```kotlin
// 转换数据
flow.map { it * 2 }
```

---

**基本写法：filter 过滤**
`<flow>.filter { <条件> }`
```kotlin
// 过滤数据
flow.filter { it > 1 }
```

---

**基本写法：flatMapConcat 串联**
`<flow>.flatMapConcat { <新 Flow> }`
```kotlin
// 串联多个流
flow.flatMapConcat { value -> flowOf(value, value * 2) }
```

---

**基本写法：flowOf 固定流**
`flowOf(<元素1>, <元素2>);`
```kotlin
// 创建固定元素流
flowOf(1, 2, 3).collect { println(it) }
```

---

**基本写法：asFlow 集合转流**
`<集合>.asFlow()`
```kotlin
// List 转 Flow
listOf(1, 2, 3).asFlow().collect { println(it) }
```

---

## Channel 通道

**基本写法：Channel 创建**
`Channel<<类型>>()`
```kotlin
// 创建通道
val channel = Channel<Int>()
launch {
    channel.send(1)
}
val value = channel.receive()
```

---

**基本写法：produce 生产者**
`produce { <send 调用> }`
```kotlin
// 创建生产者
val producer = produce {
    for (i in 1..5) send(i)
}
producer.consumeEach { println(it) }
```

---

## 异常处理

**基本写法：try-catch 捕获异常**
`try { <代码> } catch (e: <异常类型>) { }`
```kotlin
// 捕获协程异常
try {
    deferred.await()
} catch (e: Exception) {
    println("Error: ${e.message}")
}
```

---

**基本写法：CoroutineExceptionHandler**
`CoroutineExceptionHandler { <ctx>, <throwable> -> }`
```kotlin
// 全局异常处理器
val handler = CoroutineExceptionHandler { _, e ->
    println("Caught: $e")
}
scope.launch(handler) { throw RuntimeException("fail") }
```

---

## 超时控制

**基本写法：withTimeout 超时**
`withTimeout(<毫秒>) { <代码> }`
```kotlin
// 设置超时
withTimeout(2000) {
    delay(3000) // 抛出 TimeoutCancellationException
}
```

---

**基本写法：withTimeoutOrNull 超时返回 null**
`withTimeoutOrNull(<毫秒>) { <代码> }`
```kotlin
// 超时返回 null
val result = withTimeoutOrNull(1000) {
    delay(2000)
    "Done"
}  // null
```
