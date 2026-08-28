# Go pprof 性能分析 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 工具型应用 runtime/pprof

**基本写法：启动 CPU 采样**
`pprof.StartCPUProfile(<writer>) error`
```go
// 将 CPU 采样数据写入文件
import "runtime/pprof"
f, _ := os.Create("cpu.prof")
pprof.StartCPUProfile(f)
defer pprof.StopCPUProfile()
```

**基本写法：停止 CPU 采样**
`pprof.StopCPUProfile()`
```go
// 停止采样并刷新数据到文件
defer pprof.StopCPUProfile()
```

**基本写法：写入堆内存采样**
`pprof.WriteHeapProfile(<writer>) error`
```go
// 采样当前堆内存分配
f, _ := os.Create("heap.prof")
pprof.WriteHeapProfile(f)
```

**基本写法：采样指定 profile**
`pprof.Lookup(<名称>).WriteTo(<writer>, <debug级别>)`
```go
// 采样 goroutine 信息，0 为压缩格式 1 为可读文本
pprof.Lookup("goroutine").WriteTo(os.Stdout, 1)
```

---

## 服务型应用 net/http/pprof

**基本写法：注册 pprof 路由**
`import _ "net/http/pprof"`
```go
// 使用默认 DefaultServeMux 时自动注册 /debug/pprof 端点
import _ "net/http/pprof"
go http.ListenAndServe("localhost:6060", nil)
```

**基本写法：自定义路由注册**
`pprof.Index / pprof.Cmdline / pprof.Profile`
```go
// 手动注册到自定义 mux
mux.HandleFunc("/debug/pprof/", pprof.Index)
mux.HandleFunc("/debug/pprof/profile", pprof.Profile)
```

**基本写法：HTTP 端点列表**
`/debug/pprof/<类型>`
```go
// 可用类型：
// profile  CPU 采样（默认 30s）
// heap     堆内存
// goroutine 协程栈
// block    阻塞事件（需先 SetBlockProfileRate）
// mutex    锁竞争（需先 SetMutexProfileFraction）
// allocs   历史内存分配
// threadcreate 线程创建
```

---

## go tool pprof 命令

**基本写法：分析采样文件**
`go tool pprof [<文件>]`
```go
// 进入交互式终端分析 cpu.prof
go tool pprof cpu.prof
```

**基本写法：从 HTTP 拉取采样**
`go tool pprof http://<地址>/debug/pprof/<类型>`
```go
// 拉取远端 CPU 采样，默认 30 秒
go tool pprof http://localhost:6060/debug/pprof/profile
```

**基本写法：启动 Web 界面**
`go tool pprof -http=<地址> [<源>]`
```go
// 打开浏览器查看火焰图与调用图
go tool pprof -http=:8080 cpu.prof
```

**基本写法：指定采样时长**
`go tool pprof http://<地址>/debug/pprof/profile?seconds=<秒>`
```go
// 拉取 60 秒 CPU 采样
go tool pprof http://localhost:6060/debug/pprof/profile?seconds=60
```

**基本写法：指定采样指标**
`go tool pprof -sample_index=<指标> [<源>]`
```go
// 堆内存可选：inuse_space inuse_objects alloc_space alloc_objects
go tool pprof -sample_index=alloc_space heap.prof
```

**基本写法：对比两个采样**
`go tool pprof -base=<基准> <对比文件>`
```go
// 对比两个时间点的内存增长
go tool pprof -base=heap1.prof heap2.prof
```

---

## 交互式命令

**基本写法：查看热点**
`top [<数量>]`
```go
// 列出消耗最多的函数，flat 为自身耗时 cum 为累计耗时
(pprof) top 10
```

**基本写法：查看源码标注**
`list <函数正则>`
```go
// 按行显示函数内的采样分布
(pprof) list doWork
```

**基本写法：调用树**
`tree`
```go
// 以树形展示调用关系与耗时占比
(pprof) tree
```

**基本写法：调用图**
`web`
```go
// 生成 SVG 调用图并用浏览器打开（需 graphviz）
(pprof) web
```

**基本写法：聚焦过滤**
`focus <正则>`
```go
// 仅显示匹配函数相关的采样
(pprof) focus HandleRequest
```

**基本写法：忽略函数**
`ignore <正则>`
```go
// 过滤掉指定函数的采样
(pprof) ignore fmt.*
```

**基本写法：输出文本报告**
`go tool pprof -text <源>`
```go
// 直接输出文本格式热点表，不进入交互
go tool pprof -text cpu.prof
```

**基本写法：输出 SVG**
`go tool pprof -svg <源> > <文件>`
```go
// 生成调用图 SVG 文件
go tool pprof -svg cpu.prof > cpu.svg
```

---

## 基准测试采样

**基本写法：基准测试生成 CPU profile**
`go test -bench=<正则> -cpuprofile=<文件>`
```go
// 运行基准测试并生成 CPU 采样文件
go test -bench=. -cpuprofile=cpu.prof
```

**基本写法：基准测试生成内存采样**
`go test -bench=<正则> -memprofile=<文件>`
```go
// 运行基准测试并生成堆内存采样文件
go test -bench=. -memprofile=mem.prof
```

**基本写法：运行时直接采样**
`go test -bench=. -cpuprofile=cpu.prof -memprofile=mem.prof`
```go
// 同时生成 CPU 与内存采样
go test -bench=. -cpuprofile=cpu.prof -memprofile=mem.prof
```

---

## 运行时采样配置

**基本写法：设置 CPU 采样频率**
`runtime.SetCPUProfileRate(<频率>)`
```go
// 设置每秒采样次数，默认 100Hz
runtime.SetCPUProfileRate(250)
```

**基本写法：设置内存采样比例**
`runtime.MemProfileRate = <字节>`
```go
// 每分配多少字节采样一次，默认 512KB
runtime.MemProfileRate = 4096
```

**基本写法：开启阻塞采样**
`runtime.SetBlockProfileRate(<纳秒>)`
```go
// 1 表示全部采样，大于 1 按该纳秒阈值采样
runtime.SetBlockProfileRate(1)
```

**基本写法：开启锁竞争采样**
`runtime.SetMutexProfileFraction(<比例>)`
```go
// 0 关闭，1 采样全部，N 采样 1/N
runtime.SetMutexProfileFraction(1)
```

---

## trace 执行跟踪

**基本写法：生成执行跟踪**
`go test -trace=<文件> [<包路径>]`
```go
// 生成运行时执行跟踪文件
go test -trace=trace.out ./...
```

**基本写法：查看跟踪**
`go tool trace <文件>`
```go
// 启动本地服务查看 goroutine 调度跟踪
go tool trace trace.out
```

**基本写法：程序内启用 trace**
`trace.Start(<writer>)`
```go
// 代码内启动执行跟踪
import "runtime/trace"
f, _ := os.Create("trace.out")
trace.Start(f)
defer trace.Stop()
```

---

## 常见指标说明

**基本写法：CPU profile 字段**
`flat / cum`
```go
// flat 函数自身消耗的 CPU 时间
// cum 函数及其调用链累计消耗的 CPU 时间
```

**基本写法：heap profile 指标**
`inuse / alloc`
```go
// inuse_space   当前使用中的内存
// inuse_objects 当前使用中的对象数
// alloc_space   累计分配的内存
// alloc_objects 累计分配的对象数
```