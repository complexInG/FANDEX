# Kotlin Channel 通道

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Channel

**基本写法：创建无缓冲通道**
`Channel<<类型>>()`
```kotlin
// 创建无缓冲 rendezvous 通道
val ch = Channel<Int>()
```

---

**基本写法：创建带缓冲通道**
`Channel<<类型>>(<容量>)`
```kotlin
// 创建容量为 10 的缓冲通道
val ch = Channel<Int>(10)
```

---

**基本写法：创建无限缓冲通道**
`Channel<<类型>>(Channel.UNLIMITED)`
```kotlin
// 容量无上限的链表缓冲
val ch = Channel<Int>(Channel.UNLIMITED)
```

---

**基本写法：创建带满策略通道**
`Channel<<类型>>(<容量>, <溢出策略>)`
```kotlin
// 满时丢弃最新值
val ch = Channel<Int>(10, BufferOverflow.DROP_LATEST)
```

---

## 发送与接收

**基本写法：发送值**
`<channel>.send(<值>)`
```kotlin
// 挂起发送值到通道
ch.send(1)
```

---

**基本写法：非阻塞发送**
`<channel>.trySend(<值>)`
```kotlin
// 尝试发送不挂起
val r = ch.trySend(1)
```

---

**基本写法：接收值**
`<channel>.receive()`
```kotlin
// 挂起接收通道值
val v = ch.receive()
```

---

**基本写法：非阻塞接收**
`<channel>.tryReceive()`
```kotlin
// 尝试接收不挂起
val r = ch.tryReceive()
```

---

## 关闭通道

**基本写法：关闭通道**
`<channel>.close()`
```kotlin
// 关闭通道不再接收新值
ch.close()
```

---

**基本写法：判断关闭**
`<channel>.isClosedForSend | <channel>.isClosedForReceive`
```kotlin
// 判断发送或接收侧是否关闭
if (ch.isClosedForSend) { }
```

---

## 遍历接收

**基本写法：for 循环接收**
`for (<变量> in <channel>) { }`
```kotlin
// 持续接收直到关闭
for (v in ch) { println(v) }
```

---

**基本写法：consumeEach 接收**
`<channel>.consumeEach { }`
```kotlin
// 消费全部并关闭通道
ch.consumeEach { println(it) }
```

---

## produce 生产者

**基本写法：创建生产者**
`produce { <send> }`
```kotlin
// 启动协程生产并返回 ReceiveChannel
val ch = GlobalScope.produce {
    for (i in 1..5) send(i)
}
```

---

**基本写法：指定调度器**
`produce(<dispatcher>) { }`
```kotlin
// 生产者在 IO 调度器
val ch = scope.produce(Dispatchers.IO) { send(read()) }
```

---

## actor 消费者

**基本写法：创建 actor**
`actor<<类型>> { for (<变量> in channel) { } }`
```kotlin
// 启动协程消费 SendChannel
val a = scope.actor<Int> {
    for (v in channel) println(v)
}
a.send(1)
```

---

## Channel 与 Flow

**基本写法：Channel 转 Flow**
`<channel>.receiveAsFlow()`
```kotlin
// 将 Channel 转为 Flow 便于操作
val flow = ch.receiveAsFlow()
```

---

**基本写法：Flow 转 Channel**
`<flow>.produceIn(<scope>)`
```kotlin
// 将 Flow 转为 ReceiveChannel
val rc = flow.produceIn(scope)
```

---

## BufferOverflow 溢出策略

**基本写法：挂起等待**
`BufferOverflow.SUSPEND`
```kotlin
// 满时挂起发送者
val ch = Channel<Int>(2, BufferOverflow.SUSPEND)
```

---

**基本写法：丢弃最旧**
`BufferOverflow.DROP_OLDEST`
```kotlin
// 满时丢弃队列最旧值
val ch = Channel<Int>(2, BufferOverflow.DROP_OLDEST)
```

---

**基本写法：丢弃最新**
`BufferOverflow.DROP_LATEST`
```kotlin
// 满时丢弃新发送的值
val ch = Channel<Int>(2, BufferOverflow.DROP_LATEST)
```

---

## select 多路接收

**基本写法：select 等待多通道**
`select<<类型>> { <channel>.onReceive { } }`
```kotlin
// 从多个通道获取首个就绪值
val r = select<Int> {
    ch1.onReceive { "from ch1: $it" }
    ch2.onReceive { "from ch2: $it" }
}
```

---

**基本写法：select 发送**
`select<<类型>> { <channel>.onSend(<值>) { } }`
```kotlin
// 向多个通道首个就绪者发送
select<Unit> {
    ch1.onSend(1) { }
    ch2.onSend(1) { }
}
```

---

## BroadcastChannel（已弃用改用 SharedFlow）

**基本写法：Channel 转 SharedFlow**
`<channel>.broadcast(<容量>)`
```kotlin
// 旧版广播通道
val bc = ch.broadcast(10)
```

---

## Channel 容量常量

**基本写法：无缓冲**
`Channel.RENDEZVOUS`
```kotlin
// 发送接收同步会合
val ch = Channel<Int>(Channel.RENDEZVOUS)
```

---

**基本写法：合并缓冲**
`Channel.CONFLATED`
```kotlin
// 仅保留最新值
val ch = Channel<Int>(Channel.CONFLATED)
```

---

## Channel 取消

**基本写法：取消通道**
`<channel>.cancel()`
```kotlin
// 取消通道并关闭
ch.cancel()
```

---

**基本写法：带原因取消**
`<channel>.cancel(<异常>)`
```kotlin
// 携带异常取消通道
ch.cancel(CancellationException("done"))
```

---

## fan-out 多消费者

**基本写法：多个消费者分摊**
`for (i in 1..N) launch { for (v in <channel>) { } }`
```kotlin
// 多个协程分摊通道元素
repeat(3) {
    launch { for (v in ch) process(v) }
}
```

---

## fan-in 多生产者

**基本写法：多协程向同一通道发送**
`launch { <channel>.send(<值>) }`
```kotlin
// 多协程合并到同一通道
val ch = Channel<Int>()
launch { ch.send(1) }
launch { ch.send(2) }
```
