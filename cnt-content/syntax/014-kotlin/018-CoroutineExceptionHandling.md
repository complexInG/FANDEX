# Kotlin 协程异常处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 异常传播机制

**基本写法：launch 异常向上抛**
`launch { throw <异常> }`
```kotlin
// launch 异常传播到父协程
scope.launch { throw RuntimeException("fail") }
```

---

**基本写法：async 异常不立即抛**
`async { throw <异常> }`
```kotlin
// async 在 await 时才抛异常
val d = scope.async { throw RuntimeException("fail") }
d.await() // 此处抛出
```

---

## try-catch 捕获

**基本写法：捕获挂起函数异常**
`try { <挂起调用> } catch (<异常>) { }`
```kotlin
// 捕获协程内异常
try {
    deferred.await()
} catch (e: Exception) {
    println(e)
}
```

---

**基本写法：捕获 launch 异常需 ExceptionHandler**
`launch(<handler>) { }`
```kotlin
// launch 异常不能直接 try-catch
val handler = CoroutineExceptionHandler { _, e -> println(e) }
scope.launch(handler) { throw RuntimeException("fail") }
```

---

## CoroutineExceptionHandler

**基本写法：定义异常处理器**
`val <变量> = CoroutineExceptionHandler { <ctx>, <异常> -> }`
```kotlin
// 创建异常处理器
val handler = CoroutineExceptionHandler { ctx, e ->
    println("ctx=${ctx[CoroutineName]} err=$e")
}
```

---

**基本写法：应用于根协程**
`launch(<dispatcher> + <handler>) { }`
```kotlin
// 仅根协程生效
scope.launch(Dispatchers.Default + handler) { }
```

---

## SupervisorJob 容错

**基本写法：SupervisorJob 隔离子协程**
`CoroutineScope(SupervisorJob()) { }`
```kotlin
// 子协程失败不影响兄弟
val scope = CoroutineScope(SupervisorJob())
scope.launch { throw RuntimeException() }
scope.launch { /* 仍会执行 */ }
```

---

**基本写法：supervisorScope**
`supervisorScope { }`
```kotlin
// 作用域内子协程互不影响
supervisorScope {
    launch { throw RuntimeException() }
    launch { /* 正常执行 */ }
}
```

---

## CancellationException

**基本写法：取消异常需重新抛出**
`catch (e: CancellationException) { throw e }`
```kotlin
// 捕获取消异常必须重抛
try { doWork() }
catch (e: CancellationException) { throw e }
catch (e: Exception) { handle(e) }
```

---

**基本写法：自定义取消消息**
`throw CancellationException("<消息>")`
```kotlin
// 主动抛出取消异常
throw CancellationException("manual cancel")
```

---

## finally 资源清理

**基本写法：finally 清理**
`try { } finally { <清理> }`
```kotlin
// 协程取消时清理资源
try { doWork() }
finally { closeResource() }
```

---

**基本写法：NonCancellable 中执行清理**
`withContext(NonCancellable) { <清理> }`
```kotlin
// 不可取消上下文中执行挂起清理
try { doWork() }
finally {
    withContext(NonCancellable) { delay(100); close() }
}
```

---

## 异常聚合

**基本写法：await 抛出首个异常**
`try { <deferred>.await() } catch (<异常>) { }`
```kotlin
// async 等待异常抛出
try { deferred.await() } catch (e: Exception) { }
```

---

**基本写法：多个 async 异常聚合**
`awaitAll(<d1>, <d2>)`
```kotlin
// 抛出 CompositeException
supervisorScope {
    val d1 = async { throw IOException() }
    val d2 = async { throw RuntimeException() }
    try { listOf(d1, d2).awaitAll() } catch (e: Exception) { }
}
```

---

## 恢复协程

**基本写法：恢复挂起协程值**
`runCatching { <挂起调用> }.getOrDefault(<默认>)`
```kotlin
// 异常时返回默认值
val r = runCatching { deferred.await() }.getOrDefault("fallback")
```

---

## recover 异常恢复

**基本写法：recoverCatching 恢复**
`runCatching { }.recoverCatching { }`
```kotlin
// 捕获后转换结果
val r = runCatching { fetch() }
    .recoverCatching { e -> "default" }
    .getOrThrow()
```

---

## 检查与断言

**基本写法：抛出 IllegalStateException**
`check(<条件>) { "<消息>" }`
```kotlin
// 条件不满足抛异常
check(state == READY) { "not ready" }
```

---

**基本写法：参数校验**
`require(<条件>) { "<消息>" }`
```kotlin
// 参数不合法抛 IllegalArgumentException
require(id > 0) { "invalid id" }
```

---

## 异常处理器优先级

**基本写法：父协程优先于 handler**
`launch(<handler>) { launch { throw <异常> } }`
```kotlin
// 子协程异常先传播到父，父失败才走 handler
scope.launch(handler) {
    launch { throw RuntimeException() }
}
```

---

## 取消与异常关系

**基本写法：取消触发 CancellationException**
`<job>.cancel("<原因>")`
```kotlin
// 带原因的取消
job.cancel("timeout")
```

---

**基本写法：getCancellationCause 获取原因**
`<job>.getCancellationCause()`
```kotlin
// 获取取消异常原因
val cause = job.getCancellationCause()
```

---

## 异常日志记录

**基本写法：记录协程异常**
`<handler> = CoroutineExceptionHandler { _, e -> log.error("", e) }`
```kotlin
// 处理器中记录日志
val handler = CoroutineExceptionHandler { ctx, e ->
    log.error("coroutine ${ctx[CoroutineName]} failed", e)
}
```
