# Go HTTP 服务端

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本服务

**基本写法：启动 HTTP 服务**
`http.ListenAndServe(<地址>, <handler>)`
```go
// 启动 HTTP 服务
http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "hello")
})
http.ListenAndServe(":8080", nil)
```

**基本写法：注册路由**
`http.HandleFunc(<路径>, <处理函数>)`
```go
// 注册路由处理函数
http.HandleFunc("/api", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "API response")
})
```

**基本写法：使用 Handler 对象**
`http.Handle(<路径>, <handler>)`
```go
// 注册实现了 http.Handler 的对象
http.Handle("/static", http.FileServer(http.Dir("./public")))
```

**基本写法：带 TLS 启动**
`http.ListenAndServeTLS(<地址>, <证书>, <密钥>, <handler>)`
```go
// 启动 HTTPS 服务
http.ListenAndServeTLS(":443", "cert.pem", "key.pem", nil)
```

---

## 请求处理

**基本写法：获取请求方法**
`r.Method`
```go
// 获取 HTTP 方法
if r.Method == "GET" {
    // 处理 GET 请求
}
```

**基本写法：获取查询参数**
`r.URL.Query().Get(<参数名>)`
```go
// 获取 URL 查询参数
name := r.URL.Query().Get("name")
```

**基本写法：获取所有同名参数**
`r.URL.Query()[<参数名>]`
```go
// 获取同名参数列表
ids := r.URL.Query()["id"]
```

**基本写法：获取请求头**
`r.Header.Get(<头部名>)`
```go
// 获取请求头
ua := r.Header.Get("User-Agent")
```

**基本写法：获取路径参数**
`r.PathValue(<参数名>)`
```go
// Go 1.22+ 路径参数
http.HandleFunc("/user/{id}", func(w http.ResponseWriter, r *http.Request) {
    id := r.PathValue("id")
    fmt.Fprintln(w, id)
})
```

**基本写法：读取请求体**
`io.ReadAll(r.Body)`
```go
// 读取请求体内容
body, _ := io.ReadAll(r.Body)
defer r.Body.Close()
```

---

## 响应处理

**基本写法：写入文本响应**
`fmt.Fprintln(<writer>, <内容>)`
```go
// 写入纯文本响应
fmt.Fprintln(w, "hello world")
```

**基本写法：写入字节数据**
`w.Write(<字节>)`
```go
// 写入字节数据
w.Write([]byte("raw bytes"))
```

**基本写法：设置响应头**
`w.Header().Set(<名称>, <值>)`
```go
// 设置响应头
w.Header().Set("Content-Type", "application/json")
```

**基本写法：设置状态码**
`w.WriteHeader(<状态码>)`
```go
// 设置 HTTP 状态码
w.WriteHeader(http.StatusNotFound)
```

**基本写法：写入 JSON 响应**
`json.NewEncoder(w).Encode(<数据>)`
```go
// 返回 JSON 数据
w.Header().Set("Content-Type", "application/json")
json.NewEncoder(w).Encode(map[string]string{"msg": "ok"})
```

---

## Go 1.22+ 路由增强

**基本写法：方法路由**
`mux.HandleFunc("<方法> <路径>", <处理函数>)`
```go
// Go 1.22+ 支持方法前缀
mux := http.NewServeMux()
mux.HandleFunc("GET /users", listUsers)
mux.HandleFunc("POST /users", createUser)
```

**基本写法：路径通配符**
`mux.HandleFunc("/static/{path...}", <处理函数>)`
```go
// Go 1.22+ 捕获多级路径
mux.HandleFunc("/files/{path...}", func(w http.ResponseWriter, r *http.Request) {
    p := r.PathValue("path")
    fmt.Fprintln(w, p)
})
```

**基本写法：路由优先级**
`mux.HandleFunc("/api/v1/", <处理函数>)`
```go
// Go 1.22+ 更精确的路由匹配优先
mux.HandleFunc("/api/", apiHandler)
mux.HandleFunc("/api/users/", usersHandler)
```

---

## ServeMux

**基本写法：自定义 ServeMux**
`mux := http.NewServeMux()`
```go
// 使用自定义路由器
mux := http.NewServeMux()
mux.HandleFunc("/", rootHandler)
http.ListenAndServe(":8080", mux)
```

**基本写法：注册子路径**
`mux.Handle("/api/", <handler>)`
```go
// 注册带尾部斜杠的子路径
mux.Handle("/api/", http.StripPrefix("/api/", apiHandler))
```

---

## 中间件

**换行写法：编写中间件**
`func <中间件名>(next http.Handler) http.Handler`
```go
// 中间件包装 Handler
func logging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r)
        fmt.Printf("%s %s %v\n", r.Method, r.URL.Path, time.Since(start))
    })
}
```

**基本写法：应用中间件**
`mux.Use(<中间件>)`
```go
// Go 1.22+ ServeMux 支持 Use 方法链式中间件
mux := http.NewServeMux()
mux.HandleFunc("/", handler)
mux.Use(logging)
```

**换行写法：手动链式中间件**
`handler = middleware1(middleware2(handler))`
```go
// 手动组合多个中间件
handler := logging(auth(rateLimit(finalHandler)))
http.ListenAndServe(":8080", handler)
```

---

## 静态文件服务

**基本写法：文件服务器**
`http.FileServer(http.Dir(<目录>))`
```go
// 提供静态文件服务
fs := http.FileServer(http.Dir("./static"))
http.Handle("/static/", http.StripPrefix("/static/", fs))
```

**基本写法：嵌入静态文件**
`//go:embed <目录>`
```go
// Go 1.16+ 嵌入文件到二进制
//go:embed static/*
var staticFiles embed.FS
fs := http.FileServer(http.FS(staticFiles))
http.Handle("/assets/", fs)
```

---

## 服务端高级配置

**换行写法：自定义 Server**
`srv := &http.Server{ ... }`
```go
// 自定义超时等参数
srv := &http.Server{
    Addr:         ":8080",
    Handler:      mux,
    ReadTimeout:  5 * time.Second,
    WriteTimeout: 10 * time.Second,
    IdleTimeout:  120 * time.Second,
}
srv.ListenAndServe()
```

**换行写法：优雅关闭**
`srv.Shutdown(ctx)`
```go
// 接收信号后优雅关闭
go func() {
    if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
        log.Fatal(err)
    }
}()
quit := make(chan os.Signal, 1)
signal.Notify(quit, os.Interrupt)
<-quit
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
srv.Shutdown(ctx)
```

**基本写法：注入 Context**
`r.Context()`
```go
// 请求自带的 Context，客户端断开时自动取消
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    select {
    case <-ctx.Done():
        return
    case result := <-slowQuery():
        fmt.Fprintln(w, result)
    }
}
```

---

## HTTP 客户端

**基本写法：简单 GET 请求**
`http.Get(<URL>)`
```go
// 发送 GET 请求
resp, err := http.Get("https://example.com")
defer resp.Body.Close()
body, _ := io.ReadAll(resp.Body)
```

**基本写法：自定义请求**
`http.NewRequest(<方法>, <URL>, <body>)`
```go
// 创建自定义请求
req, _ := http.NewRequest("POST", "https://api.example.com", strings.NewReader(`{"k":"v"}`))
req.Header.Set("Content-Type", "application/json")
resp, _ := http.DefaultClient.Do(req)
defer resp.Body.Close()
```

**换行写法：自定义客户端**
`client := &http.Client{ ... }`
```go
// 自定义超时的 HTTP 客户端
client := &http.Client{
    Timeout: 30 * time.Second,
}
resp, _ := client.Get("https://example.com")
defer resp.Body.Close()
```

**基本写法：带 Context 的请求**
`http.NewRequestWithContext(<ctx>, <方法>, <URL>, <body>)`
```go
// 请求可被 Context 取消
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
req, _ := http.NewRequestWithContext(ctx, "GET", "https://example.com", nil)
resp, _ := http.DefaultClient.Do(req)
```
