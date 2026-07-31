# Kotlin 协程调度器与上下文

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 内置调度器

**基本写法：默认调度器**
`Dispatchers.Default`
```kotlin
// CPU 密集任务调度器
launch(Dispatchers.Default) { compute() }
```

---

**基本写法：IO 调度器**
`Dispatchers.IO`
```kotlin
// 阻塞 IO 任务调度器
launch(Dispatchers.IO) { readFile() }
```

---

**基本写法：主线程调度器**
`Dispatchers.Main`
```kotlin
// UI 主线程调度器（需平台依赖）
launch(Dispatchers.Main) { updateUI() }
```

---

**基本写法：不受限调度器**
`Dispatchers.Unconfined`
```kotlin
// 在调用线程执行直到挂起
launch(Dispatchers.Unconfined) { }
```

---

## 自定义调度器

**基本写法：单线程调度器**
`newSingleThreadContext("<名称>")`
```kotlin
// 创建单线程调度器
val dispatcher = newSingleThreadContext("worker")
```

---

**基本写法：固定线程池调度器**
`newFixedThreadPoolContext(<线程数>, "<名称>")`
```kotlin
// 创建固定大小线程池调度器
val dispatcher = newFixedThreadPoolContext(4, "pool")
```

---

**基本写法：基于 Executor**
`<executor>.asCoroutineDispatcher()`
```kotlin
// 复用现有 Executor 作为调度器
val d = Executors.newFixedThreadPool(4).asCoroutineDispatcher()
```

---

## 切换调度器

**基本写法：withContext 切换**
`withContext(<dispatcher>) { }`
```kotlin
// 临时切换调度器
withContext(Dispatchers.IO) { fetchData() }
```

---

**基本写法：launch 指定调度器**
`launch(<dispatcher>) { }`
```kotlin
// 启动时指定调度器
launch(Dispatchers.Default) { heavy() }
```

---

**基本写法：async 指定调度器**
`async(<dispatcher>) { }`
```kotlin
// async 启动并指定调度器
async(Dispatchers.IO) { fetch() }
```

---

## 限流调度器

**基本写法：限制并发数**
`<dispatcher>.limitedParallelism(<并发数>)`
```kotlin
// 限制调度器并发数
val limited = Dispatchers.IO.limitedParallelism(8)
```

---

## CoroutineContext 元素

**基本写法：获取当前上下文**
`currentCoroutineContext()`
```kotlin
// 获取当前协程上下文
val ctx = currentCoroutineContext()
```

---

**基本写法：从上下文取元素**
`<context>[<Key>]`
```kotlin
// 获取当前调度器
val d = currentCoroutineContext()[CoroutineDispatcher]
```

---

**基本写法：获取 Job**
`coroutineContext[Job]`
```kotlin
// 获取当前协程 Job
val job = coroutineContext[Job]
```

---

**基本写法：获取名称**
`coroutineContext[CoroutineName]`
```kotlin
// 获取协程名称
val name = coroutineContext[CoroutineName]?.name
```

---

## 上下文组合与传递

**基本写法：组合上下文元素**
`<ctx1> + <ctx2>`
```kotlin
// Job 与 Dispatcher 组合
val ctx = Job() + Dispatchers.IO + CoroutineName("worker")
```

---

**基本写法：移除上下文元素**
`<ctx>.minusKey(<Key>)`
```kotlin
// 移除 Job 元素
val newCtx = ctx.minusKey(Job)
```

---

**基本写法：fold 遍历**
`<ctx>.fold(<初始>) { <累加>, <元素> -> }`
```kotlin
// 遍历上下文所有元素
ctx.fold(emptyList()) { acc, e -> acc + e }
```

---

## 自定义上下文元素

**基本写法：实现 CoroutineContext.Element**
`class <类>(val <值>) : CoroutineContext.Element { companion object Key }`
```kotlin
// 自定义请求 ID 上下文
class RequestId(val id: String) : CoroutineContext.Element {
    companion object Key : CoroutineContext.Key<RequestId>
    override val key = Key
}
```

---

**基本写法：注入自定义元素**
`launch(<dispatcher> + <元素>) { }`
```kotlin
// 启动时注入请求 ID
launch(Dispatchers.Default + RequestId("r-1")) { }
```

---

## 线程局部变量

**基本写法：CoroutineContext 存 ThreadLocal**
`<threadLocal>.asContextElement(<值>)`
```kotlin
// ThreadLocal 跨挂起传递
val tl = ThreadLocal<String>()
launch(tl.asContextElement("ctx") + Dispatchers.IO) {
    println(tl.get())
}
```

---

## 调度器异常处理

**基本写法：CoroutineExceptionHandler**
`CoroutineExceptionHandler { <ctx>, <异常> -> }`
```kotlin
// 自定义协程异常处理器
val handler = CoroutineExceptionHandler { _, e ->
    println("caught: $e")
}
launch(Dispatchers.Default + handler) { }
```

---

## 阻塞与挂起桥接

**基本写法：阻塞调用转挂起**
`<dispatcher>.runIsolated { }`
```kotlin
// 在调度器上运行可阻塞代码
runBlocking(Dispatchers.IO) { blockingCall() }
```

---

**基本写法：runInterruptible 阻塞转可取消**
`runInterruptible { <阻塞调用> }`
```kotlin
// 将阻塞代码包装为可取消挂起
suspend fun read(): String = runInterruptible { Files.readString(path) }
```

---

## 调度器关闭

**基本写法：关闭自定义调度器**
`<dispatcher>.close()`
```kotlin
// 关闭单线程调度器释放线程
val dispatcher = newSingleThreadContext("w")
dispatcher.close()
```

---

## 父子上下文继承

**基本写法：复制父上下文**
`<parentCtx> + <新元素>`
```kotlin
// 子协程继承父上下文并覆盖
val childCtx = coroutineContext + Dispatchers.IO
launch(childCtx) { }
```
