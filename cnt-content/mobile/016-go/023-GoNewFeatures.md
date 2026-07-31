# Go 1.21-1.23 新特性 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Go 1.21 内置函数

**基本写法：内置 min/max**
`min(<a>, <b>[, ...]) / max(<a>, <b>[, ...])`
```go
// 返回多个值中的最小/最大值，支持任意有序类型
m := min(3, 1, 2)
x := max(1.5, 2.3)
```

**基本写法：清空 map/slice**
`clear(<map或slice>)`
```go
// 清空 map 所有键值，或将 slice 元素置零
clear(m)
clear(s)
```

**基本写法：内置 min 用于字符串**
`min(<字符串A>, <字符串B>)`
```go
// 字符串按字典序比较
s := min("go", "rust")
```

---

## Go 1.21 标准库新增

**基本写法：log/slog 结构化日志**
`slog.Info(<消息>, <键>, <值>)`
```go
// 结构化日志输出 JSON
import "log/slog"
slog.Info("user login", "uid", 42, "ip", "1.2.3.4")
```

**基本写法：slog 配置 handler**
`slog.NewJSONHandler(<writer>, &slog.HandlerOptions{...})`
```go
// 自定义 JSON handler 并设为默认 logger
logger := slog.New(slog.NewJSONHandler(os.Stdout, &slog.HandlerOptions{
    Level: slog.LevelDebug,
}))
slog.SetDefault(logger)
```

**基本写法：slog 分组属性**
`slog.With(<键>, <值>).<级别>(<消息>)`
```go
// 携带固定属性输出日志
log := slog.With("service", "api")
log.Info("started")
```

---

## Go 1.21 slices 包

**基本写法：切片排序**
`slices.Sort(<切片>)`
```go
// 原地升序排序
import "slices"
slices.Sort(nums)
```

**基本写法：切片二分查找**
`slices.BinarySearch(<切片>, <目标>) (int, bool)`
```go
// 在有序切片中查找，返回位置与是否命中
i, ok := slices.BinarySearch(nums, 5)
```

**基本写法：判断包含**
`slices.Contains(<切片>, <目标>) bool`
```go
// 切片是否包含某元素
if slices.Contains(nums, 3) { }
```

**基本写法：切片反转**
`slices.Reverse(<切片>)`
```go
// 原地反转切片元素顺序
slices.Reverse(s)
```

**基本写法：切片去重排序**
`slices.Compact(<切片>)`
```go
// 移除相邻重复元素，需先排序
s = slices.Compact(s)
```

**基本写法：泛型比较**
`cmp.Less(<a>, <b>) / cmp.Compare(<a>, <b>)`
```go
// cmp 包提供有序类型比较工具
import "cmp"
r := cmp.Compare(1, 2)  // -1 0 1
```

---

## Go 1.21 maps 包

**基本写法：克隆 map**
`maps.Clone(<map>) <map>`
```go
// 浅拷贝整个 map
copy := maps.Clone(m)
```

**基本写法：合并 map**
`maps.Copy(<目标map>, <源map>)`
```go
// 将 src 的键值合并到 dst，重复键覆盖
maps.Copy(dst, src)
```

**基本写法：判断 map 相等**
`maps.Equal(<a>, <b>) bool`
```go
// 判断两个 map 键值是否完全相同
if maps.Equal(m1, m2) { }
```

---

## Go 1.21 context 增强

**基本写法：派生可取消 context**
`context.WithoutCancel(<父context>) context.Context`
```go
// 继承父值但不受父取消影响（Go 1.21+）
ctx := context.WithoutCancel(parent)
```

**基本写法：派生无超时 context**
`context.WithoutDeadline(<父>) context.Context`
```go
// 继承父值但去掉父的 deadline
ctx := context.WithoutDeadline(parent)
```

**基本写法：合并多个 err**
`errors.Join(<err>...) error`
```go
// Go 1.20+ 将多个错误合并为一个
err := errors.Join(err1, err2)
```

---

## Go 1.21 sync 增强

**基本写法：单次求值 OnceFunc**
`sync.OnceFunc(<函数>) func()`
```go
// 返回只执行一次的函数封装
loadConfig := sync.OnceFunc(func() { /* init */ })
loadConfig()  // 多次调用只首次执行
```

**基本写法：带返回值 OnceValue**
`sync.OnceValue(<函数>) func() <T>`
```go
// 返回缓存结果的惰性求值（Go 1.21+）
getVal := sync.OnceValue(func() int { return compute() })
v := getVal()
```

**基本写法：多返回值 OnceValues**
`sync.OnceValues(<函数>) func() (<T>, <U>)`
```go
// 缓存两个返回值的惰性求值
getPair := sync.OnceValues(func() (int, string) { return 1, "ok" })
n, s := getPair()
```

---

## Go 1.21 工具链与兼容

**基本写法：toolchain 指令**
`// go.mod: toolchain go<版本>`
```go
// go.mod 声明所需工具链版本
// go 1.21.0
// toolchain go1.21.5
```

**基本写法：GODEBUG 向后兼容**
`GODEBUG=<键>=<值>`
```go
// 控制特定行为开关，如 panicnil
// GODEBUG=panicnil=1 允许 panic(nil)
```

**基本写法：go.mod 中声明 GODEBUG**
`godebug <键>=<值>`
```go
// go.mod 中声明程序级 GODEBUG（Go 1.23+）
// godebug (
//     default=go1.21
//     panicnil=1
// )
```

**基本写法：向前兼容下载**
`go get go@<版本>`
```go
// 自动下载并切换到所需工具链
go get go@1.23.0
```

---

## Go 1.22 整数 range

**基本写法：range 整数**
`for i := range <整数> { }`
```go
// 遍历 0 到 n-1
for i := range 10 {
    fmt.Println(i)
}
```

**基本写法：range 整数省略变量**
`for range <整数> { }`
```go
// 仅循环指定次数，不使用索引
for range 3 {
    doWork()
}
```

---

## Go 1.22 循环变量作用域

**基本写法：每次迭代独立变量**
`for i, v := range <集合> { }`
```go
// Go 1.22+ 循环变量每次迭代独立，闭包捕获安全
for _, x := range items {
    go func() { fmt.Println(x) }()  // 各自捕获独立值
}
```

**基本写法：模块级控制 loopvar**
`// go.mod: go 1.22`
```go
// go 指令为 1.22 及以上时自动启用新作用域语义
// 旧代码可通过 go 1.21 保持旧行为
```

---

## Go 1.22 增强路由

**基本写法：方法匹配路由**
`mux.HandleFunc("<方法> <路径>", <handler>)`
```go
// Go 1.22 ServeMux 支持方法与路径模式
mux.HandleFunc("GET /users/{id}", getUser)
```

**基本写法：路径通配符**
`mux.HandleFunc("<路径>/{<名称>}", <handler>)`
```go
// 捕获路径参数
mux.HandleFunc("GET /files/{path...}", serveFile)
```

**基本写法：读取路径参数**
`<request>.PathValue(<名称>) string`
```go
// 取出路由中 {id} 的实际值
id := r.PathValue("id")
```

**基本写法：方法冲突检测**
`mux.Handle("<方法A> <路径>", ...)`
```go
// 注册冲突方法会 panic，注册 "/" 兜底其余方法
mux.HandleFunc("GET /", fallback)
```

---

## Go 1.22 math/rand/v2

**基本写法：生成随机数**
`rand.IntN(<上限>) int`
```go
// 返回 [0, n) 随机整数，无需手动 Seed
import "math/rand/v2"
n := rand.IntN(100)
```

**基本写法：浮点随机**
`rand.Float64() float64`
```go
// 返回 [0.0, 1.0) 随机浮点
f := rand.Float64()
```

**基本写法：从切片随机取值**
`func(<切片>) <元素> { return <切片>[rand.IntN(len(<切片>))] }`
```go
// 简易随机选择元素
pick := items[rand.IntN(len(items))]
```

---

## Go 1.23 迭代器

**基本写法：range 函数迭代器**
`for v := range <迭代函数> { }`
```go
// for-range 支持 iterator 函数类型
// 类型为 func(func(V) bool)
for v := range seq {
    fmt.Println(v)
}
```

**基本写法：iter.Seq 类型**
`iter.Seq[V] / iter.Seq2[K, V]`
```go
// 标准迭代器类型定义
import "iter"
type Seq[V any] func(yield func(V) bool)
```

**基本写法：自定义迭代器**
`func(yield func(V) bool)`
```go
// 返回遍历切片的迭代器
func SliceIter[T any](s []T) iter.Seq[T] {
    return func(yield func(T) bool) {
        for _, v := range s {
            if !yield(v) {
                return
            }
        }
    }
}
```

**基本写法：键值迭代器**
`func(yield func(K, V) bool)`
```go
// iter.Seq2 用于键值对遍历
for k, v := range m2.Seq2 {
}
```

---

## Go 1.23 标准库新增

**基本写法：unique 包去重**
`unique.Make[T](<值>) unique.Handle[T]`
```go
// 字符串等值的全局去重，节省内存
import "unique"
h := unique.Make("longstring")
s := h.Value()
```

**基本写法：structs 包字段对齐**
`structs.HostLayout`
```go
// 保证结构体内存布局与宿主机一致
import "structs"
var s structs.HostLayout
```

**基本写法：slices 收集迭代器**
`slices.Collect(<iter.Seq>) []<T>`
```go
// 将迭代器收集为切片
s := slices.Collect(SliceIter(items))
```

**基本写法：slices 排序迭代器**
`slices.Sorted(<iter.Seq>) []<T>`
```go
// 排序并收集迭代器结果
s := slices.Sorted(seq)
```

---

## Go 1.23 命令与工具

**基本写法：查看变更配置**
`go env -changed`
```go
// 仅显示与默认值不同的环境变量
go env -changed
```

**基本写法：tidy 差异预览**
`go mod tidy -diff`
```go
// 预览 go.mod 所需修改而不写回
go mod tidy -diff
```

**基本写法：运行时生成 profile**
`go run -cpuprofile=<文件>`
```go
// go run 直接支持 CPU 采样（Go 1.23+）
go run -cpuprofile=cpu.prof main.go
```

**基本写法：vet 版本检查**
`go vet ./...`
```go
// Go 1.23 vet 含 stdversion 分析器
// 标记使用了过高版本 API 的符号引用
go vet ./...
```

---

## Go 1.23 运行时改进

**基本写法：Timer 行为统一**
`<timer>.Stop() / <timer>.Reset()`
```go
// Go 1.23 统一 Timer 停止与重置语义
// 未触发即 Stop 会回收资源，不再阻塞
timer.Stop()
```

**基本写法：泛型类型别名预览**
`GOEXPERIMENT=aliastypeparams`
```go
// 预览特性，启用后允许泛型类型别名
// GOEXPERIMENT=aliastypeparams go build
type Set[T comparable] = map[T]struct{}
```