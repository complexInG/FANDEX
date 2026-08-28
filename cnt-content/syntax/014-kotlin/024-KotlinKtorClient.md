# Kotlin Ktor 客户端

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建客户端

**基本写法：创建 HttpClient**
`HttpClient(<引擎>)`
```kotlin
// 创建 HttpClient
val client = HttpClient(CIO)
```

---

**基本写法：带配置创建**
`HttpClient(<引擎>) { }`
```kotlin
// 配置引擎参数
val client = HttpClient(CIO) {
    engine { requestTimeout = 5000 }
}
```

---

**基本写法：OkHttp 引擎**
`HttpClient(OkHttp)`
```kotlin
// 使用 OkHttp 引擎
val client = HttpClient(OkHttp)
```

---

## 请求方法

**基本写法：GET 请求**
`client.get("<url>")`
```kotlin
// 发送 GET 请求
val resp = client.get("https://api.example.com/users")
```

---

**基本写法：POST 请求**
`client.post("<url>") { }`
```kotlin
// 发送 POST 请求
client.post("https://api.example.com/users") {
    setBody(User("Alice"))
}
```

---

**基本写法：PUT 请求**
`client.put("<url>") { }`
```kotlin
// 发送 PUT 请求
client.put("https://api.example.com/users/1") { setBody(data) }
```

---

**基本写法：DELETE 请求**
`client.delete("<url>")`
```kotlin
// 发送 DELETE 请求
client.delete("https://api.example.com/users/1")
```

---

## 请求配置

**基本写法：设置请求头**
`headers { append("<名称>", "<值>") }`
```kotlin
// 添加请求头
client.get("...") {
    header("Authorization", "Bearer token")
}
```

---

**基本写法：URL 参数**
`url { parameters.append("<名>", "<值>") }`
```kotlin
// 添加查询参数
client.get("...") {
    url { parameters.append("page", "1") }
}
```

---

**基本写法：JSON 请求体**
`setBody(<对象>)`
```kotlin
// 发送 JSON 请求体
client.post("...") {
    contentType(ContentType.Application.Json)
    setBody(user)
}
```

---

## 响应处理

**基本写法：获取响应体文本**
`<resp>.bodyAsText()`
```kotlin
// 获取响应文本
val text = client.get("...").bodyAsText()
```

---

**基本写法：反序列化为对象**
`<resp>.body<<类型>>()`
```kotlin
// 反序列化响应体
val user = client.get("...").body<User>()
```

---

**基本写法：获取状态码**
`<resp>.status`
```kotlin
// 获取 HTTP 状态码
val status = resp.status
```

---

**基本写法：获取响应头**
`<resp>.headers["<名称>"]`
```kotlin
// 获取响应头
val ct = resp.headers[HttpHeaders.ContentType]
```

---

## ContentNegotiation 插件

**基本写法：安装 JSON 插件**
`install(ContentNegotiation) { json() }`
```kotlin
// 启用自动 JSON 序列化
val client = HttpClient(CIO) {
    install(ContentNegotiation) {
        json(Json { ignoreUnknownKeys = true })
    }
}
```

---

## HttpRequestBuilder 风格

**基本写法：配置请求构建器**
`HttpRequestBuilder().apply { }`
```kotlin
// 复用请求配置
val builder = HttpRequestBuilder().apply {
    url("https://api.example.com")
    header("X-Key", "abc")
}
client.request(builder)
```

---

## 超时配置

**基本写法：设置超时**
`install(HttpTimeout) { }`
```kotlin
// 配置请求超时
install(HttpTimeout) {
    requestTimeoutMillis = 5000
    connectTimeoutMillis = 3000
    socketTimeoutMillis = 10000
}
```

---

## 鉴权插件

**基本写法：Bearer 鉴权**
`install(Auth) { bearer { } }`
```kotlin
// Bearer Token 自动加载
install(Auth) {
    bearer {
        loadTokens { BearerTokens(accessToken, refreshToken) }
    }
}
```

---

**基本写法：Basic 鉴权**
`install(Auth) { basic { } }`
```kotlin
// Basic 认证
install(Auth) {
    basic {
        username = "user"
        password = "pwd"
    }
}
```

---

## 日志插件

**基本写法：启用日志**
`install(Logging) { }`
```kotlin
// 请求响应日志
install(Logging) {
    level = LogLevel.HEADERS
    logger = Logger.DEFAULT
}
```

---

## 重试插件

**基本写法：失败重试**
`install(HttpRequestRetry) { }`
```kotlin
// 配置重试策略
install(HttpRequestRetry) {
    retryOnServerErrors(maxRetries = 3)
    exponentialDelay()
}
```

---

## UserAgent 插件

**基本写法：设置 UA**
`install(UserAgent) { agent = "<ua>" }`
```kotlin
// 设置全局 User-Agent
install(UserAgent) { agent = "MyApp/1.0" }
```

---

## HttpCookies Cookie 管理

**基本写法：启用 Cookie**
`install(HttpCookies)`
```kotlin
// 自动管理 Cookie
install(HttpCookies)
```

---

**基本写法：设置 Cookie 存储**
`install(HttpCookies) { storage = <存储> }`
```kotlin
// 自定义 Cookie 存储
install(HttpCookies) {
    storage = AcceptAllCookiesStorage()
}
```

---

## WebSocket 客户端

**基本写法：建立 WebSocket**
`client.webSocket("<url>") { }`
```kotlin
// 建立 WebSocket 连接
client.webSocket("wss://echo.example.com") {
    send(Frame.Text("hello"))
}
```

---

**基本写法：发送 WebSocket 消息**
`send(Frame.Text("<消息>"))`
```kotlin
// 发送文本帧
send(Frame.Text("ping"))
```

---

**基本写法：接收 WebSocket 消息**
`incoming.receive() as Frame.Text`
```kotlin
// 接收文本帧
val msg = (incoming.receive() as Frame.Text).readText()
```

---

## SSE Server-Sent Events

**基本写法：SSE 接收**
`client.config { }.sseSession { }`
```kotlin
// 处理 SSE 事件流
client.sseSession("https://events.example.com") {
    incoming.collect { event -> println(event.data) }
}
```

---

## 资源关闭

**基本写法：关闭客户端**
`<client>.close()`
```kotlin
// 关闭释放连接池
client.close()
```

---

**基本写法：use 自动关闭**
`HttpClient(<引擎>).use { }`
```kotlin
// use 块自动关闭
HttpClient(CIO).use { c -> c.get("...") }
```

---

## 跨平台使用

**基本写法：KMP 共享客户端**
`val client = HttpClient()`
```kotlin
// KMP 跨平台默认引擎
val client = HttpClient()
```
