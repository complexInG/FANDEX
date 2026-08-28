# Kotlin Select 表达式 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## select 基础

**基本写法：引入 select**
`import kotlinx.coroutines.selects.select`
```kotlin
// 协程 select 让多个挂起操作竞争，先就绪者胜出
import kotlinx.coroutines.selects.select
import kotlinx.coroutines.*
```

---

**基本写法：select 表达式**
`select { <子句1>; <子句2> }`
```kotlin
// 等待多个 Deferred，先返回者被处理
suspend fun fetchBoth(a: Deferred<String>, b: Deferred<String>): String =
    select {
        a.onAwait { "from A: $it" }
        b.onAwait { "from B: $it" }
    }
```

---

## Deferred onAwait

**基本写法：等待首个完成**
`<Deferred>.onAwait { <处理> }`
```kotlin
// 多个异步任务竞争
val a = async { delay(100); "A" }
val b = async { delay(50);  "B" }
val r = select<String> {
    a.onAwait { "got $it" }
    b.onAwait { "got $it" }
}
```

---

**基本写法：select 返回值**
`select { <子句> }`
```kotlin
// select 是表达式，最后一行决定返回类型
val result: String = select {
    deferred1.onAwait { it }
    deferred2.onAwait { it }
}
```

---

## Channel onReceive / onSend

**基本写法：接收首个可用消息**
`<Channel>.onReceive { <处理> }`
```kotlin
// 从两个 Channel 中接收先就绪的
val r = select<String> {
    chan1.onReceive { "c1: $it" }
    chan2.onReceive { "c2: $it" }
}
```

---

**基本写法：发送到首个可写 Channel**
`<Channel>.onSend(<值>) { <处理> }`
```kotlin
// 选择第一个能接收元素的 Channel
select<Unit> {
    chan1.onSend(item) { println("sent to c1") }
    chan2.onSend(item) { println("sent to c2") }
}
```

---

**基本写法：onReceiveCatching**
`<Channel>.onReceiveCatching { <Result> }`
```kotlin
// 处理 Channel 关闭情况
val r = select<String> {
    chan.onReceiveCatching { result ->
        result.getOrNull() ?: "closed"
    }
}
```

---

## 超时与默认值

**基本写法：配合超时**
`withTimeout(<时间>) { select { ... } }`
```kotlin
// 给 select 加超时上限
val r = withTimeoutOrNull(500) {
    select<String> {
        chan1.onReceive { it }
        chan2.onReceive { it }
    }
} ?: "timeout"
```

---

**基本写法：onTimeout 子句**
`select { onTimeout(<时间>) { <默认> } }`
```kotlin
// 直接在 select 内处理超时
val r = select<String> {
    chan.onReceive { it }
    onTimeout(300) { "default" }
}
```

---

## select 偏好与公平性

**基本写法：默认公平选择**
`select { <子句1>; <子句2> }`
```kotlin
// select 随机选择同时就绪的子句，避免饥饿
val r = select<String> {
    c1.onReceive { "c1" }
    c2.onReceive { "c2" }
}
```

---

**基本写法：优先级子句**
`select { <优先>.onReceive {}; <普通>.onReceive {} }`
```kotlin
// 利用 selectClause 顺序实现弱优先级
val r = select<String> {
    highPriChan.onReceive { "high" }
    lowPriChan.onReceive  { "low" }
}
```

---

## SelectBuilder 进阶

**基本写法：动态子句**
`select { if (<条件>) <子句A> else <子句B> }`
```kotlin
// 按条件加入不同子句
val r = select<String> {
    if (useFirst) c1.onReceive { it }
    else          c2.onReceive { it }
}
```

---

**基本写法：循环 select**
`while (true) select { ... }`
```kotlin
// 持续多路复用
while (isActive) {
    select<Unit> {
        chan1.onReceive { handle1(it) }
        chan2.onReceive { handle2(it) }
    }
}
```

---

## 自定义 SelectClause

**基本写法：实现 onReceive 风格子句**
`fun <R> registerSelectClause(<scope>, <块>)`
```kotlin
// 自定义可被 select 的对象
class MyEvent {
    private val listeners = mutableListOf<(String) -> Unit>()
    fun consume(block: (String) -> Unit) { listeners.add(block) }

    suspend fun selectConsume(): String = select {
        consume { it }
    }
}
```

---

**基本写法：SelectClause1 协议**
`val onEvent: SelectClause1<String>`
```kotlin
// 暴露 SelectClause1 供外部 select
import kotlinx.coroutines.selects.SelectClause1

class Stream {
    val onData: SelectClause1<String> get() = TODO()
}

select<String> {
    stream.onData.onAwait { it }
}
```

---

## 典型场景

**基本写法：负载均衡**
`select { <c1>.onReceive {}; <c2>.onReceive {} }`
```kotlin
// 多个 worker Channel 均衡消费
suspend fun worker(chans: List<Channel<Job>>) {
    while (true) {
        val job = select<Job> {
            chans.forEach { c -> c.onReceive { it } }
        }
        job.run()
    }
}
```

---

**基本写法：扇出（fan-out）**
`select { <input>.onReceive {}; <control>.onReceive {} }`
```kotlin
// 同时处理数据流与控制信号
while (isActive) {
    select<Unit> {
        dataChan.onReceive { process(it) }
        controlChan.onReceive { if (it == "stop") cancel() }
    }
}
```
