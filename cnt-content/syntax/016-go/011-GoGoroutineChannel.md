# Go goroutine 与 channel

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## goroutine 创建

**基本写法：启动 goroutine**
`go <函数调用>`
```go
// 使用 go 关键字启动并发协程
go doWork()
```

**基本写法：匿名函数 goroutine**
`go func() { ... }()`
```go
// 立即执行的匿名 goroutine
go func(msg string) {
    fmt.Println(msg)
}("hello")
```

**基本写法：WaitGroup 等待协程**
`var wg sync.WaitGroup`
```go
// 使用 WaitGroup 等待一组协程完成
var wg sync.WaitGroup
for i := 0; i < 3; i++ {
    wg.Add(1)
    go func(n int) {
        defer wg.Done()
        fmt.Println(n)
    }(i)
}
wg.Wait()
```

**基本写法：Go 1.22+ 循环变量安全**
`for i := range <n> { go func() { ... }() }`
```go
// Go 1.22+ 每次迭代变量地址独立，无需手动拷贝
var wg sync.WaitGroup
for i := range 3 {
    wg.Add(1)
    go func() {
        defer wg.Done()
        fmt.Println(i)
    }()
}
wg.Wait()
```

---

## channel 创建

**基本写法：无缓冲通道**
`make(chan <类型>)`
```go
// 无缓冲通道：发送和接收同步
ch := make(chan int)
```

**基本写法：带缓冲通道**
`make(chan <类型>, <容量>)`
```go
// 带缓冲通道：缓冲区满前发送不阻塞
ch := make(chan string, 3)
```

**基本写法：单向发送通道**
`chan<- <类型>`
```go
// 只能发送的通道类型
var sendOnly chan<- int = make(chan int)
```

**基本写法：单向接收通道**
`<-chan <类型>`
```go
// 只能接收的通道类型
var recvOnly <-chan int = make(chan int)
```

**基本写法：关闭通道**
`close(<通道>)`
```go
// 关闭通道，通知接收方不再有数据
ch := make(chan int, 2)
ch <- 1
ch <- 2
close(ch)
```

---

## channel 收发

**基本写法：发送数据**
`<通道> <- <值>`
```go
// 向通道发送数据
ch := make(chan int, 1)
ch <- 42
```

**基本写法：接收数据**
`<-<通道>`
```go
// 从通道接收数据
v := <-ch
```

**基本写法：接收数据并判断是否关闭**
`v, ok := <-<通道>`
```go
// ok 为 false 表示通道已关闭且无数据
v, ok := <-ch
if !ok {
    fmt.Println("通道已关闭")
}
```

**基本写法：range 遍历通道**
`for v := range <通道> { ... }`
```go
// 持续接收直到通道关闭
for v := range ch {
    fmt.Println(v)
}
```

**基本写法：select 多路复用**
`select { case ... : }`
```go
// select 随机选择一个就绪的 case 执行
select {
case v := <-ch1:
    fmt.Println("ch1:", v)
case v := <-ch2:
    fmt.Println("ch2:", v)
}
```

**基本写法：select 超时控制**
`select { case ... : case <-time.After(<时长>): }`
```go
// 使用 time.After 实现超时
select {
case v := <-ch:
    fmt.Println(v)
case <-time.After(2 * time.Second):
    fmt.Println("超时")
}
```

**基本写法：select 非阻塞**
`select { case ...: default: }`
```go
// default 使 select 非阻塞
select {
case v := <-ch:
    fmt.Println(v)
default:
    fmt.Println("无数据")
}
```

---

## 通道容量与长度

**基本写法：获取通道缓冲区容量**
`cap(<通道>)`
```go
// 返回通道缓冲区大小
ch := make(chan int, 5)
fmt.Println(cap(ch)) // 5
```

**基本写法：获取通道中元素个数**
`len(<通道>)`
```go
// 返回通道中当前排队元素数
ch := make(chan int, 3)
ch <- 1
ch <- 2
fmt.Println(len(ch)) // 2
```

---

## 常用并发模式

**换行写法：Worker Pool 工作池**
`func worker(id int, jobs <-chan int, results chan<- int)`
```go
// 固定数量 worker 消费任务队列
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2
    }
}
jobs := make(chan int, 10)
results := make(chan int, 10)
for w := 1; w <= 3; w++ {
    go worker(w, jobs, results)
}
for j := 1; j <= 5; j++ {
    jobs <- j
}
close(jobs)
```

**换行写法：扇入合并多通道**
`func fanIn(<通道1>, <通道2> <-chan <类型>) <-chan <类型>`
```go
// 将多个通道合并为一个
func fanIn(ch1, ch2 <-chan int) <-chan int {
    out := make(chan int)
    go func() { for v := range ch1 { out <- v } }()
    go func() { for v := range ch2 { out <- v } }()
    return out
}
```

**换行写法：信号量限制并发数**
`sem := make(chan struct{}, <最大并发>)`
```go
// 使用带缓冲通道作为信号量控制并发
sem := make(chan struct{}, 3)
var wg sync.WaitGroup
for i := 0; i < 10; i++ {
    wg.Add(1)
    sem <- struct{}{}
    go func(n int) {
        defer wg.Done()
        defer func() { <-sem }()
        doWork(n)
    }(i)
}
wg.Wait()
```

**换行写法：通知退出信号**
`quit := make(chan struct{})`
```go
// 使用空结构体通道作为退出信号
quit := make(chan struct{})
go func() {
    for {
        select {
        case <-quit:
            return
        default:
            doWork()
        }
    }
}()
close(quit)
```

---

## Mutex 互斥锁

**基本写法：互斥锁**
`var mu sync.Mutex`
```go
// 互斥锁保护共享资源
var mu sync.Mutex
count := 0
mu.Lock()
count++
mu.Unlock()
```

**基本写法：读写锁**
`var rw sync.RWMutex`
```go
// 读写锁：允许多读单写
var rw sync.RWMutex
rw.RLock()
v := readData()
rw.RUnlock()
```

**换行写法：使用 defer 解锁**
`mu.Lock(); defer mu.Unlock()`
```go
// defer 确保锁一定被释放
func update() {
    mu.Lock()
    defer mu.Unlock()
    doUpdate()
}
```

**基本写法：tryLock 非阻塞加锁**
`mu.TryLock()`
```go
// 尝试加锁，失败返回 false
if mu.TryLock() {
    defer mu.Unlock()
    doWork()
} else {
    fmt.Println("加锁失败")
}
```

---

## Once 单次执行

**基本写法：sync.Once 确保只执行一次**
`var once sync.Once`
```go
// 单例模式初始化
var (
    instance *Config
    once     sync.Once
)
func GetConfig() *Config {
    once.Do(func() {
        instance = loadConfig()
    })
    return instance
}
```

---

## atomic 原子操作

**基本写法：原子加法**
`atomic.AddInt64(&<变量>, <值>)`
```go
// 原子整数加法
var count int64
atomic.AddInt64(&count, 1)
```

**基本写法：原子读取**
`atomic.LoadInt64(&<变量>)`
```go
// 原子读取值
v := atomic.LoadInt64(&count)
```

**基本写法：原子存储**
`atomic.StoreInt64(&<变量>, <值>)`
```go
// 原子存储值
atomic.StoreInt64(&count, 100)
```

**基本写法：原子比较交换**
`atomic.CompareAndSwapInt64(&<变量>, <旧值>, <新值>)`
```go
// CAS 操作：值匹配旧值才更新
ok := atomic.CompareAndSwapInt64(&count, 10, 20)
```

**基本写法：Go 1.19+ 原子类型**
`var <变量> atomic.Int64`
```go
// 使用类型安全的原子类型
var n atomic.Int64
n.Add(1)
n.Store(100)
fmt.Println(n.Load())
```

**基本写法：原子指针**
`atomic.Pointer[<类型>]`
```go
// Go 1.19+ 泛型原子指针
var p atomic.Pointer[Config]
p.Store(&Config{Name: "default"})
cfg := p.Load()
```

---

## Go 1.23+ Timer 通道变更

**基本写法：Go 1.23+ Timer 可被 GC 回收**
`t := time.NewTimer(<时长>)`
```go
// Go 1.23+ 未 Stop 的 Timer 可被垃圾回收
t := time.NewTimer(time.Second)
// 即使不调用 t.Stop()，失去引用后也会被 GC 回收
```

**基本写法：Go 1.23+ Timer 通道无缓冲**
`cap(t.C) == 0`
```go
// Go 1.23+ Timer 通道容量为 0，使用非阻塞 select 轮询
t := time.NewTimer(time.Second)
select {
case <-t.C:
    fmt.Println("超时")
default:
    fmt.Println("未超时")
}
```
