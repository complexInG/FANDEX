# Kotlin Ktor 服务端

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建服务器

**基本写法：embeddedServer 启动**
`embeddedServer(Netty, port = <端口>) { }.start(wait = true)`
```kotlin
// 启动 Ktor Netty 服务器
embeddedServer(Netty, port = 8080) {
    routing { get("/") { call.respondText("hello") } }
}.start(wait = true)
```

---

**基本写法：指定 host**
`embeddedServer(Netty, port = <端口>, host = "<主机>") { }`
```kotlin
// 指定监听主机
embeddedServer(Netty, port = 8080, host = "0.0.0.0") { }
```

---

## 路由配置

**基本写法：定义 GET 路由**
`get("<路径>") { }`
```kotlin
// 注册 GET 请求处理
get("/users") { call.respond(users) }
```

---

**基本写法：POST 路由**
`post("<路径>") { }`
```kotlin
// 注册 POST 请求处理
post("/users") { call.respond(create()) }
```

---

**基本写法：路径参数**
`get("<路径>/{<参数>}") { }`
```kotlin
// 获取路径参数
get("/users/{id}") {
    val id = call.parameters["id"]
}
```

---

**基本写法：route 分组**
`route("<前缀>") { }`
```kotlin
// 路由分组
routing {
    route("/api") {
        get("/v1") { }
        post("/v2") { }
    }
}
```

---

## 请求处理

**基本写法：接收 JSON**
`call.receive<<类型>>()`
```kotlin
// 反序列化请求体
val user = call.receive<User>()
```

---

**基本写法：响应 JSON**
`call.respond(<对象>)`
```kotlin
// 序列化对象为 JSON 响应
call.respond(User("Alice"))
```

---

**基本写法：响应纯文本**
`call.respondText("<文本>")`
```kotlin
// 返回纯文本响应
call.respondText("hello", ContentType.Text.Plain)
```

---

**基本写法：查询参数**
`call.request.queryParameters["<名称>"]`
```kotlin
// 获取查询字符串参数
val q = call.request.queryParameters["q"]
```

---

## ContentNegotiation 插件

**基本写法：安装 JSON 插件**
`install(ContentNegotiation) { json() }`
```kotlin
// 启用 JSON 序列化
install(ContentNegotiation) {
    json(Json { ignoreUnknownKeys = true })
}
```

---

## StatusPages 异常处理

**基本写法：异常映射**
`install(StatusPages) { exception<异常> { } }`
```kotlin
// 异常转换为 HTTP 状态码
install(StatusPages) {
    exception<NotFoundException> { call, _ ->
        call.respond(HttpStatusCode.NotFound)
    }
}
```

---

## Authentication 认证

**基本写法：Basic 认证**
`install(Authentication) { basic { } }`
```kotlin
// 启用 Basic 认证
install(Authentication) {
    basic("auth") {
        realm = "api"
        validate { cred -> if (check(cred)) UserIdPrincipal(cred.name) else null }
    }
}
```

---

**基本写法：路由应用认证**
`authenticate("<名称>") { }`
```kotlin
// 路由级应用认证
authenticate("auth") {
    get("/me") { call.respond(user) }
}
```

---

**基本写法：JWT 认证**
`install(Authentication) { jwt { } }`
```kotlin
// JWT 认证配置
install(Authentication) {
    jwt("jwt") {
        verifier(jwk)
        realm = "api"
        validate { cred -> UserIdPrincipal(cred.payload.subject) }
    }
}
```

---

## Sessions 会话

**基本写法：启用会话**
`install(Sessions) { cookie<<类型>>("<名称>") }`
```kotlin
// Cookie 会话
install(Sessions) {
    cookie<UserSession>("SESSION")
}
```

---

**基本写法：设置会话**
`call.sessions.set(<实例>)`
```kotlin
// 写入会话数据
call.sessions.set(UserSession(id = "1"))
```

---

**基本写法：获取会话**
`call.sessions.get<<类型>>()`
```kotlin
// 读取会话数据
val s = call.sessions.get<UserSession>()
```

---

## 静态资源

**基本写法：静态文件**
`staticFiles("<路径>", <文件对象>)`
```kotlin
// 提供静态文件服务
staticFiles("/static", File("public"))
```

---

**基本写法：静态默认资源**
`defaultResource("<文件>")`
```kotlin
// 从资源目录提供静态文件
staticResources("/static") {
    defaultResource("index.html")
}
```

---

## WebSockets

**基本写法：启用 WebSocket**
`install(WebSockets)`
```kotlin
// 安装 WebSocket 插件
install(WebSockets)
```

---

**基本写法：定义 WebSocket 路由**
`webSocket("<路径>") { }`
```kotlin
// WebSocket 端点
webSocket("/chat") {
    for (frame in incoming) {
        val text = frame as Frame.Text
        send(Frame.Text(text.readText()))
    }
}
```

---

**基本写法：发送消息**
`send(Frame.Text("<消息>"))`
```kotlin
// 发送文本帧
send(Frame.Text("hello"))
```

---

**基本写法：接收消息**
`incoming.receive() as Frame.Text`
```kotlin
// 接收文本帧
val text = (incoming.receive() as Frame.Text).readText()
```

---

## CORS 跨域

**基本写法：启用 CORS**
`install(CORS) { anyHost() }`
```kotlin
// 配置跨域
install(CORS) {
    anyHost()
    allowHeader(HttpHeaders.ContentType)
}
```

---

## 部署命令

**基本写法：构建 FatJar**
`./gradlew buildFatJar`
```bash
# 构建包含所有依赖的 FatJar
./gradlew :app:buildFatJar
```

---

**基本写法：运行应用**
`java -jar <jar>`
```bash
# 运行打包后的应用
java -jar build/libs/app-all.jar
```

---

**基本写法：Docker 运行**
`docker build -t <名称> .`
```bash
# 构建 Docker 镜像
docker build -t ktor-app .
docker run -p 8080:8080 ktor-app
```
