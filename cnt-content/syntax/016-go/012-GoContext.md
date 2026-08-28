# Go Context 上下文

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Context 基础

**基本写法：创建根 Context**
`context.Background()`
```go
// 根 Context，通常在 main 函数或顶层使用
ctx := context.Background()
```

**基本写法：创建 TODO Context**
`context.TODO()`
```go
// 占位 Context，尚未确定使用何种策略时使用
ctx := context.TODO()
```

---

## 派生 Context

**基本写法：带取消的 Context**
`context.WithCancel(<父Context>)`
```go
// 创建可手动取消的 Context
ctx, cancel := context.WithCancel(context.Background())
defer cancel()
go func() {
    select {
    case <-ctx.Done():
        fmt.Println("已取消")
    }
}()
cancel()
```

**基本写法：带超时的 Context**
`context.WithTimeout(<父Context>, <时长>)`
```go
// 超时后自动取消
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
```

**基本写法：带截止时间的 Context**
`context.WithDeadline(<父Context>, <时间点>)`
```go
// 到达指定时间点自动取消
deadline := time.Now().Add(10 * time.Second)
ctx, cancel := context.WithDeadline(context.Background(), deadline)
defer cancel()
```

**基本写法：带值的 Context**
`context.WithValue(<父Context>, <键>, <值>)`
```go
// 在 Context 中传递请求作用域数据
type key string
ctx := context.WithValue(context.Background(), key("userID"), 42)
```

---

## Context 取值

**基本写法：从 Context 获取值**
`<ctx>.Value(<键>)`
```go
// 获取 Context 中存储的值
v := ctx.Value(key("userID"))
if id, ok := v.(int); ok {
    fmt.Println(id)
}
```

---

## Context 检查

**基本写法：检查是否已取消**
`<-<ctx>.Done()`
```go
// 阻塞等待取消或超时
select {
case <-ctx.Done():
    fmt.Println(ctx.Err())
case result := <-doWork():
    fmt.Println(result)
}
```

**基本写法：获取取消错误**
`<ctx>.Err()`
```go
// 返回取消原因
err := ctx.Err()
if err == context.Canceled {
    fmt.Println("被手动取消")
} else if err == context.DeadlineExceeded {
    fmt.Println("超时取消")
}
```

**基本写法：获取截止时间**
`<ctx>.Deadline()`
```go
// 返回截止时间和是否设置了截止时间
deadline, ok := ctx.Deadline()
if ok {
    fmt.Println("截止时间:", deadline)
}
```

---

## Context 使用模式

**换行写法：HTTP 请求传递 Context**
`func handler(w http.ResponseWriter, r *http.Request)`
```go
// 从 HTTP 请求中获取 Context
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    select {
    case <-ctx.Done():
        fmt.Println("请求被取消")
    case result := <-doWork():
        fmt.Fprintln(w, result)
    }
}
```

**换行写法：函数参数传递 Context**
`func doWork(ctx context.Context, ...) <返回值>`
```go
// Context 作为第一个参数传递
func queryDB(ctx context.Context, sql string) (Result, error) {
    select {
    case <-ctx.Done():
        return Result{}, ctx.Err()
    default:
        return execute(sql), nil
    }
}
```

**换行写法：超时控制数据库查询**
`ctx, cancel := context.WithTimeout(parent, <时长>)`
```go
// 为数据库操作设置超时
func fetchUser(ctx context.Context, db *sql.DB, id int) (*User, error) {
    ctx, cancel := context.WithTimeout(ctx, 3*time.Second)
    defer cancel()
    return db.QueryRowContext(ctx, "SELECT ... WHERE id=?", id), nil
}
```

**换行写法：级联取消**
`child, cancel := context.WithCancel(parent)`
```go
// 子 Context 随父 Context 取消而取消
parent, parentCancel := context.WithCancel(context.Background())
child, childCancel := context.WithCancel(parent)
// 父取消时，子也会取消
parentCancel()
<-child.Done()
```

---

## Go 1.21+ Context 增强

**基本写法：WithoutCancel 移除取消**
`context.WithoutCancel(<ctx>)`
```go
// 返回不继承取消信号的 Context
ctx, cancel := context.WithCancel(context.Background())
bg := context.WithoutCancel(ctx)
cancel()
// ctx 已取消，bg 仍未取消
```

**基本写法：WithDeadlineCause 指定取消原因**
`context.WithDeadlineCause(<ctx>, <时间>, <原因>)`
```go
// 在截止时间到达时附带自定义错误
ctx, cancel := context.WithDeadlineCause(
    context.Background(),
    time.Now().Add(time.Second),
    errors.New("自定义超时原因"),
)
defer cancel()
<-ctx.Done()
fmt.Println(ctx.Err()) // 自定义超时原因
```

**基本写法：WithTimeoutCause 指定超时原因**
`context.WithTimeoutCause(<ctx>, <时长>, <原因>)`
```go
// 超时时附带自定义错误
ctx, cancel := context.WithTimeoutCause(
    context.Background(),
    5*time.Second,
    errors.New("请求超时"),
)
defer cancel()
```

**基本写法：AfterFunc 注册取消回调**
`stop := context.AfterFunc(<ctx>, <回调>)`
```go
// Context 取消时执行回调
ctx, cancel := context.WithCancel(context.Background())
stop := context.AfterFunc(ctx, func() {
    fmt.Println("Context 被取消")
})
cancel()
// stop() 可在取消前撤销回调
```

---

## Go 1.24+ 测试 Context

**基本写法：testing.T.Context**
`t.Context()`
```go
// Go 1.24+ 测试自带 Context，测试结束自动取消
func TestExample(t *testing.T) {
    ctx := t.Context()
    go func() {
        <-ctx.Done()
    }()
}
```

**基本写法：benchmark.B.Context**
`b.Context()`
```go
// 基准测试自带的 Context
func BenchmarkExample(b *testing.B) {
    ctx := b.Context()
    for b.Loop() {
        doWork(ctx)
    }
}
```
