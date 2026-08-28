---
order: 10
title: go 模块文档合集
module: 'go'
category: 后端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：016-go/001-ConcurrentProgramming.md ============ -->

# Go 并发编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## goroutine

**基本写法：启动 goroutine**
`go <函数>(<参数>)`
```go
// 启动 goroutine 执行函数
go doWork("task1");
```

**基本写法：匿名函数 goroutine**
`go func(<参数> <类型>) { ... }(<值>)`
```go
// 启动匿名函数 goroutine
go func(msg string) {
    fmt.Println(msg);
}("hello");
```

---

## channel 创建

**基本写法：无缓冲通道**
`make(chan <类型>)`
```go
// 无缓冲通道，发送和接收同步
ch := make(chan int);
```

**基本写法：有缓冲通道**
`make(chan <类型>, <容量>)`
```go
// 有缓冲通道，容量为 10
ch := make(chan int, 10);
```

---

## channel 操作

**基本写法：发送数据**
`<通道> <- <值>`
```go
// 发送数据到通道
ch <- 42;
```

**基本写法：接收数据**
`<-<通道>`
```go
// 从通道接收数据
v := <-ch;
```

**基本写法：关闭通道**
`close(<通道>)`
```go
// 关闭通道，禁止再发送
close(ch);
```

**基本写法：遍历通道**
`for <值> := range <通道> { ... }`
```go
// 遍历通道直到关闭
for v := range ch {
    fmt.Println(v);
}
```

---

## select 语句

**基本写法：select 多路复用**
`select { case ... }`
```go
// 多路复用选择
select {
case v := <-ch1:
    fmt.Println("ch1:", v);
case v := <-ch2:
    fmt.Println("ch2:", v);
case <-time.After(time.Second):
    fmt.Println("timeout");
}
```

**基本写法：default 非阻塞**
`select { case ... default: }`
```go
// 非阻塞接收
select {
case v := <-ch:
    fmt.Println(v);
default:
    fmt.Println("no data");
}
```

---

## sync.WaitGroup

**基本写法：WaitGroup 等待**
`var <变量名> sync.WaitGroup`
```go
// 使用 WaitGroup 等待所有 goroutine 完成
var wg sync.WaitGroup;
for i := 0; i < 5; i++ {
    wg.Add(1);
    go func(n int) {
        defer wg.Done();
        doWork(n);
    }(i);
}
wg.Wait();
```

---

## sync.Mutex

**基本写法：互斥锁**
`var <变量名> sync.Mutex`
```go
// 互斥锁保护共享数据
var mu sync.Mutex;
var counter int;

func increment() {
    mu.Lock();
    defer mu.Unlock();
    counter++;
}
```

**基本写法：读写锁**
`var <变量名> sync.RWMutex`
```go
// 读写锁，读多写少场景
var rwmu sync.RWMutex;
var data map[string]string;

func read(key string) string {
    rwmu.RLock();
    defer rwmu.RUnlock();
    return data[key];
}

func write(key, value string) {
    rwmu.Lock();
    defer rwmu.Unlock();
    data[key] = value;
}
```

---

## sync.Once

**基本写法：单次执行**
`var <变量名> sync.Once`
```go
// sync.Once 确保初始化只执行一次
var (
    once sync.Once;
    instance *Config;
)

func GetConfig() *Config {
    once.Do(func() {
        instance = loadConfig();
    });
    return instance;
}
```

---

## sync.Cond

**基本写法：条件变量**
`sync.NewCond(&<互斥锁>)`
```go
// 条件变量等待通知
var mu sync.Mutex;
cond := sync.NewCond(&mu);

func waitForData() {
    mu.Lock();
    for !dataReady {
        cond.Wait();
    }
    mu.Unlock();
}

func notifyData() {
    mu.Lock();
    dataReady = true;
    cond.Signal();
    mu.Unlock();
}
```

---

## sync.Pool

**基本写法：对象池**
`sync.Pool{ New: func() any { ... } }`
```go
// 对象池复用对象
var bufPool = sync.Pool{
    New: func() any {
        return new(bytes.Buffer);
    },
}

func process(data []byte) {
    buf := bufPool.Get().(*bytes.Buffer);
    defer bufPool.Put(buf);
    buf.Reset();
    buf.Write(data);
}
```

---

## atomic 原子操作

**基本写法：原子加法**
`atomic.AddInt64(&<变量>, <值>)`
```go
// 原子加法
var counter int64;
atomic.AddInt64(&counter, 1);
```

**基本写法：原子加载**
`atomic.LoadInt64(&<变量>)`
```go
// 原子读取
val := atomic.LoadInt64(&counter);
```

**基本写法：原子存储**
`atomic.StoreInt64(&<变量>, <值>)`
```go
// 原子写入
atomic.StoreInt64(&counter, 100);
```

**基本写法：原子比较交换**
`atomic.CompareAndSwapInt64(&<变量>, <旧值>, <新值>)`
```go
// CAS 操作
ok := atomic.CompareAndSwapInt64(&counter, 100, 200);
```

---

## context

**基本写法：创建根 context**
`context.Background()`
```go
// 创建根 context
ctx := context.Background();
```

**基本写法：带超时的 context**
`context.WithTimeout(<父context>, <时长>)`
```go
// 创建 5 秒超时的 context
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second);
defer cancel();
```

**基本写法：带取消的 context**
`context.WithCancel(<父context>)`
```go
// 创建可取消的 context
ctx, cancel := context.WithCancel(context.Background());
defer cancel();
```

**基本写法：带值的 context**
`context.WithValue(<父context>, <键>, <值>)`
```go
// 创建带值的 context
ctx := context.WithValue(context.Background(), "userID", 123);
```

**基本写法：从 context 获取值**
`<ctx>.Value(<键>)`
```go
// 从 context 获取值
userID := ctx.Value("userID").(int);
```

**基本写法：检查 context 是否取消**
`<-<ctx>.Done()`
```go
// 检查 context 是否已取消
select {
case <-ctx.Done():
    return ctx.Err();
default:
    // 继续工作
}
```

---

## 并发模式

**基本写法：fan-out 扇出**
`go <函数>(<输入通道>, <输出通道>)`
```go
// 多个 goroutine 处理同一输入
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2;
    }
}

jobs := make(chan int, 100);
results := make(chan int, 100);
for w := 1; w <= 3; w++ {
    go worker(w, jobs, results);
}
```

**基本写法：fan-in 扇入**
`func <函数名>(<输出通道>, <输入通道1>, <输入通道2>)`
```go
// 合并多个通道的数据
func merge(out chan<- int, cs ...<-chan int) {
    var wg sync.WaitGroup;
    wg.Add(len(cs));
    for _, c := range cs {
        go func(ch <-chan int) {
            defer wg.Done();
            for v := range ch {
                out <- v;
            }
        }(c);
    }
    go func() {
        wg.Wait();
        close(out);
    }();
}
```

**基本写法：pipeline 管道**
`go func() { ... }()`
```go
// 管道模式
func generate(nums ...int) <-chan int {
    out := make(chan int);
    go func() {
        defer close(out);
        for _, n := range nums {
            out <- n;
        }
    }();
    return out;
}
```

---

## 并发安全

**基本写法：并发安全 map**
`sync.Map`
```go
// 并发安全的 map
var m sync.Map;
m.Store("key", "value");
v, ok := m.Load("key");
m.Delete("key");
```

**基本写法：遍历 sync.Map**
`<map>.Range(func(<键>, <值>) bool { ... })`
```go
// 遍历 sync.Map
m.Range(func(key, value any) bool {
    fmt.Printf("%v: %v\n", key, value);
    return true;
});
```



<!-- ============ 文档分隔线：016-go/002-GoErrorHandling.md ============ -->

# Go 错误处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本错误处理

**基本写法：函数返回错误**
`func <函数名>(<参数>) (<返回值>, error) { ... }`
```go
// 函数返回结果和错误
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero");
    }
    return a / b, nil;
}
```

**基本写法：调用方检查错误**
`if <错误> != nil { ... }`
```go
// 调用函数并检查错误
result, err := divide(10, 0);
if err != nil {
    fmt.Println("Error:", err);
    return;
}
```

---

## 错误创建

**基本写法：errors.New 创建错误**
`errors.New("<消息>")`
```go
// 创建简单错误
err := errors.New("file not found");
```

**基本写法：fmt.Errorf 创建错误**
`fmt.Errorf("<格式>", <参数>)`
```go
// 格式化错误消息
err := fmt.Errorf("user %d not found", userID);
```

---

## 自定义错误类型

**基本写法：自定义错误结构体**
`type <错误类型> struct { ... }`
```go
// 自定义错误类型
type ValidationError struct {
    Field   string;
    Message string;
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Message);
}
```

**基本写法：返回自定义错误**
`return &<错误类型>{ ... }`
```go
// 返回自定义错误
func validateEmail(email string) error {
    if !strings.Contains(email, "@") {
        return &ValidationError{
            Field:   "email",
            Message: "invalid email format",
        };
    }
    return nil;
}
```

---

## 错误包装与解包

**基本写法：错误包装**
`fmt.Errorf("<消息>: %w", <错误>)`
```go
// 包装错误保留原始错误链
err := fmt.Errorf("save user failed: %w", originalErr);
```

**基本写法：错误解包**
`errors.Unwrap(<错误>)`
```go
// 解包获取原始错误
originalErr := errors.Unwrap(wrappedErr);
```

**基本写法：错误链判断**
`errors.Is(<错误>, <目标错误>)`
```go
// 判断错误链中是否包含目标错误
if errors.Is(err, sql.ErrNoRows) {
    fmt.Println("record not found");
}
```

**基本写法：错误类型断言**
`errors.As(<错误>, &<目标变量>)`
```go
// 提取错误链中的特定类型
var valErr *ValidationError;
if errors.As(err, &valErr) {
    fmt.Println(valErr.Field);
}
```

---

## 错误处理模式

**基本写法：哨兵错误**
`var Err<名称> = errors.New("<消息>")`
```go
// 定义哨兵错误
var ErrNotFound = errors.New("not found");
var ErrUnauthorized = errors.New("unauthorized");

// 使用 errors.Is 判断
if errors.Is(err, ErrNotFound) {
    fmt.Println("resource not found");
}
```

**基本写法：错误变量组**
`var ( Err<名称1> = ...; Err<名称2> = ... )`
```go
// 批量定义错误变量
var (
    ErrInvalidInput = errors.New("invalid input");
    ErrTimeout      = errors.New("operation timed out");
);
```

---

## panic 与 recover

**基本写法：panic 触发**
`panic(<值>)`
```go
// 触发 panic
func mustInit() {
    panic("initialization failed");
}
```

**基本写法：recover 捕获**
`recover()`
```go
// 在 defer 中 recover
func safeRun() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered:", r);
        }
    }();
    panic("something went wrong");
}
```

**基本写法：安全调用包装**
`func <函数名>(<函数> func()) { ... }`
```go
// 安全调用包装函数
func safe(fn func()) (err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("panic: %v", r);
        }
    }();
    fn();
    return nil;
}
```

---

## 错误处理最佳实践

**基本写法：错误立即处理**
`if <错误> != nil { return <错误> }`
```go
// 错误立即返回，不忽略
data, err := readFile("config.json");
if err != nil {
    return err;
}
```

**基本写法：错误包装上下文**
`fmt.Errorf("<上下文>: %w", <错误>)`
```go
// 添加上下文信息
if err := saveUser(user); err != nil {
    return fmt.Errorf("create user: %w", err);
}
```

**基本写法：不重复处理错误**
`if <错误> != nil { return }`
```go
// 调用方处理错误，不重复处理
result, err := doSomething();
if err != nil {
    return;
}
```



<!-- ============ 文档分隔线：016-go/003-Reflection.md ============ -->

# Go 反射

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 反射基础

**基本写法：获取反射类型**
`reflect.TypeOf(<值>)`
```go
// 获取类型的反射对象
t := reflect.TypeOf(42);
fmt.Println(t); // int
```

**基本写法：获取反射值**
`reflect.ValueOf(<值>)`
```go
// 获取值的反射对象
v := reflect.ValueOf(42);
fmt.Println(v); // 42
```

**基本写法：获取值的类型**
`<反射值>.Type()`
```go
// 从 Value 获取 Type
t := v.Type();
```

---

## Kind 判断

**基本写法：获取 Kind**
`<反射类型>.Kind()`
```go
// 获取类型的 Kind
t := reflect.TypeOf("hello");
if t.Kind() == reflect.String {
    fmt.Println("string type");
}
```

**基本写法：Kind 常量**
`reflect.<Kind>`
```go
// Kind 常量判断
switch t.Kind() {
case reflect.Int, reflect.Int64:
    fmt.Println("integer");
case reflect.String:
    fmt.Println("string");
case reflect.Struct:
    fmt.Println("struct");
}
```

---

## 值修改

**基本写法：获取可设置值**
`reflect.ValueOf(&<变量>).Elem()`
```go
// 传入指针才能修改值
x := 42;
v := reflect.ValueOf(&x).Elem();
v.SetInt(100);
fmt.Println(x); // 100
```

**基本写法：检查可设置性**
`<反射值>.CanSet()`
```go
// 检查值是否可设置
if v.CanSet() {
    v.SetInt(100);
}
```

---

## Struct 反射

**基本写法：获取字段数量**
`<反射类型>.NumField()`
```go
// 获取结构体字段数量
t := reflect.TypeOf(User{});
count := t.NumField();
```

**基本写法：按索引获取字段**
`<反射类型>.Field(<索引>)`
```go
// 按索引获取字段信息
field := t.Field(0);
fmt.Println(field.Name, field.Type);
```

**基本写法：按名称获取字段**
`<反射类型>.FieldByName("<名称>")`
```go
// 按名称获取字段信息
field, ok := t.FieldByName("Name");
if ok {
    fmt.Println(field.Type);
}
```

**基本写法：获取字段标签**
`<字段>.Tag.Get("<标签名>")`
```go
// 获取字段的 json 标签
field, _ := t.FieldByName("Name");
tag := field.Tag.Get("json");
```

**基本写法：遍历结构体字段**
`for <索引> := 0; <索引> < <数量>; <索引>++ { ... }`
```go
// 遍历结构体所有字段
for i := 0; i < t.NumField(); i++ {
    field := t.Field(i);
    fmt.Printf("%s: %s\n", field.Name, field.Type);
}
```

**基本写法：设置字段值**
`<反射值>.Field(<索引>).Set(<值>)`
```go
// 通过反射设置字段值
v := reflect.ValueOf(&user).Elem();
v.FieldByName("Name").SetString("Alice");
```

---

## Method 反射

**基本写法：获取方法数量**
`<反射类型>.NumMethod()`
```go
// 获取类型的方法数量
t := reflect.TypeOf(User{});
count := t.NumMethod();
```

**基本写法：按索引获取方法**
`<反射类型>.Method(<索引>)`
```go
// 按索引获取方法
m := t.Method(0);
fmt.Println(m.Name);
```

**基本写法：按名称获取方法**
`<反射类型>.MethodByName("<名称>")`
```go
// 按名称获取方法
m, ok := t.MethodByName("String");
```

**基本写法：调用方法**
`<反射值>.Method(<索引>).Call(<参数>)`
```go
// 通过反射调用方法
v := reflect.ValueOf(user);
result := v.Method(0).Call(nil);
```

---

## 函数反射

**基本写法：调用函数**
`<反射值>.Call(<参数>)`
```go
// 通过反射调用函数
fn := func(a, b int) int { return a + b };
v := reflect.ValueOf(fn);
result := v.Call([]reflect.Value{
    reflect.ValueOf(1),
    reflect.ValueOf(2),
});
```

---

## Slice 与 Map 反射

**基本写法：创建切片**
`reflect.MakeSlice(<类型>, <长度>, <容量>)`
```go
// 通过反射创建切片
t := reflect.TypeOf([]int{});
s := reflect.MakeSlice(t, 0, 10);
```

**基本写法：追加元素**
`<反射值>.Set(reflect.Append(<切片>, <值>))`
```go
// 通过反射追加元素
v := reflect.ValueOf(&s).Elem();
v.Set(reflect.Append(v, reflect.ValueOf(42)));
```

**基本写法：创建 Map**
`reflect.MakeMap(<类型>)`
```go
// 通过反射创建 map
t := reflect.TypeOf(map[string]int{});
m := reflect.MakeMap(t);
```

**基本写法：设置 Map 键值**
`<反射值>.SetMapIndex(<键>, <值>)`
```go
// 通过反射设置 map 键值
m.SetMapIndex(reflect.ValueOf("key"), reflect.ValueOf(42));
```

---

## 接口转换

**基本写法：获取接口值**
`<反射值>.Interface()`
```go
// 从反射值获取接口值
v := reflect.ValueOf(42);
i := v.Interface();
n := i.(int);
```

---

## 类型判断

**基本写法：判断是否实现接口**
`<反射类型>.Implements(<接口类型>)`
```go
// 检查类型是否实现 Stringer 接口
t := reflect.TypeOf(User{});
stringerType := reflect.TypeOf((*fmt.Stringer)(nil)).Elem();
if t.Implements(stringerType) {
    fmt.Println("implements Stringer");
}
```

**基本写法：判断可赋值性**
`<反射类型>.AssignableTo(<目标类型>)`
```go
// 检查类型是否可赋值
t1 := reflect.TypeOf(int(0));
t2 := reflect.TypeOf(int64(0));
ok := t1.AssignableTo(t2);
```



<!-- ============ 文档分隔线：016-go/004-GoGeneric.md ============ -->

# Go 泛型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 泛型函数

**基本写法：泛型函数声明**
`func <函数名>[<类型参数> <约束>](<参数> <类型参数>) <返回值>`
```go
// 泛型函数，T 必须满足 Ordered 约束
func Min[T constraints.Ordered](a, b T) T {
    if a < b {
        return a;
    }
    return b;
}
```

**基本写法：调用泛型函数**
`<函数名>[<类型>](<参数>)`
```go
// 显式指定类型参数
minInt := Min[int](3, 5);
```

**基本写法：类型推断调用**
`<函数名>(<参数>)`
```go
// 编译器自动推断类型
minFloat := Min(3.14, 2.71);
```

---

## 类型约束

**基本写法：接口约束**
`type <约束名> interface { ~<类型1> | ~<类型2> }`
```go
// 自定义类型约束
type Number interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
    ~float32 | ~float64;
}
```

**基本写法：使用自定义约束**
`func <函数名>[<类型参数> <约束>](<参数>) <返回值>`
```go
// 使用自定义 Number 约束
func Sum[T Number](nums []T) T {
    var total T;
    for _, n := range nums {
        total += n;
    }
    return total;
}
```

**基本写法：comparable 约束**
`func <函数名>[<类型参数> comparable](<参数>) <返回值>`
```go
// comparable 约束允许 == 和 != 比较
func Contains[T comparable](slice []T, target T) bool {
    for _, v := range slice {
        if v == target {
            return true;
        }
    }
    return false;
}
```

**基本写法：any 约束**
`func <函数名>[<类型参数> any](<参数>) <返回值>`
```go
// any 约束接受任意类型
func Print[T any](v T) {
    fmt.Println(v);
}
```

---

## 多类型参数

**基本写法：多类型参数泛型**
`func <函数名>[<类型1> <约束1>, <类型2> <约束2>](<参数>) <返回值>`
```go
// 多类型参数泛型函数
func Map[T, U any](slice []T, fn func(T) U) []U {
    result := make([]U, len(slice));
    for i, v := range slice {
        result[i] = fn(v);
    }
    return result;
}
```

---

## 泛型类型

**基本写法：泛型切片类型**
`type <类型名>[<类型参数> <约束>] []<类型参数>`
```go
// 泛型切片类型
type Stack[T any] []T;
```

**基本写法：泛型结构体**
`type <类型名>[<类型参数> <约束>] struct { ... }`
```go
// 泛型结构体
type Pair[T, U any] struct {
    First  T;
    Second U;
}
```

**基本写法：泛型 map 类型**
`type <类型名>[<类型参数1> <约束1>, <类型参数2> <约束2>] map[<类型参数1>]<类型参数2>`
```go
// 泛型 map 类型
type Map[K comparable, V any] map[K]V;
```

---

## 泛型方法

**基本写法：泛型类型方法**
`func (<接收者> <类型名>[<类型参数>]) <方法名>(<参数>) <返回值>`
```go
// 泛型类型的方法
func (s *Stack[T]) Push(v T) {
    *s = append(*s, v);
}

func (s *Stack[T]) Pop() (T, bool) {
    var zero T;
    if len(*s) == 0 {
        return zero, false;
    }
    v := (*s)[len(*s)-1];
    *s = (*s)[:len(*s)-1];
    return v, true;
}
```

---

## 泛型接口

**基本写法：泛型接口**
`type <接口名>[<类型参数> <约束>] interface { ... }`
```go
// 泛型接口
type Container[T any] interface {
    Add(v T);
    Get() T;
    Len() int;
}
```

---

## 约束包

**基本写法：constraints.Ordered**
`[T constraints.Ordered]`
```go
// Ordered 约束支持 < > <= >=
func Max[T constraints.Ordered](a, b T) T {
    if a > b {
        return a;
    }
    return b;
}
```

---

## 类型近似

**基本写法：近似类型约束**
`~<底层类型>`
```go
// ~ 表示包含底层类型的自定义类型
type Number interface {
    ~int | ~float64;
}

type MyInt int; // MyInt 满足 Number 约束
```

---

## 泛型实例化

**基本写法：实例化泛型类型**
`<类型名>[<具体类型>]`
```go
// 实例化泛型类型
intStack := Stack[int]{};
strStack := Stack[string]{};
```

---

## 泛型算法

**基本写法：泛型过滤**
`func <函数名>[<类型> <约束>](<参数>) <返回值>`
```go
// 泛型过滤函数
func Filter[T any](slice []T, fn func(T) bool) []T {
    result := []T{};
    for _, v := range slice {
        if fn(v) {
            result = append(result, v);
        }
    }
    return result;
}
```

**基本写法：泛型归约**
`func <函数名>[<类型> <约束>](<参数>) <返回值>`
```go
// 泛型归约函数
func Reduce[T, U any](slice []T, initial U, fn func(U, T) U) U {
    result := initial;
    for _, v := range slice {
        result = fn(result, v);
    }
    return result;
}
```



<!-- ============ 文档分隔线：016-go/005-GoFunctionMethod.md ============ -->

# Go 函数与方法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数定义

**基本写法：标准函数声明**
`func <函数名>(<参数列表>) <返回值> { ... }`
```go
// 声明加法函数
func add(a int, b int) int {
    return a + b;
}
```

**基本写法：合并类型参数**
`func <函数名>(<参数1>, <参数2> <类型>) <返回值>`
```go
// a 和 b 都是 int 类型
func add(a, b int) int {
    return a + b;
}
```

---

## 多返回值

**基本写法：多返回值函数**
`func <函数名>(<参数>) (<返回值1>, <返回值2>) { ... }`
```go
// 返回结果和错误
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero");
    }
    return a / b, nil;
}
```

---

## 命名返回值

**基本写法：命名返回值**
`func <函数名>(<参数>) (<名称1>, <名称2> <类型>) { ... }`
```go
// 命名返回值，裸 return 自动返回命名变量
func rectangleProps(w, h float64) (area, perimeter float64) {
    area = w * h;
    perimeter = 2 * (w + h);
    return;
}
```

---

## 可变参数

**基本写法：可变参数函数**
`func <函数名>(<参数> ...<类型>) <返回值>`
```go
// 可变参数在函数内被视为切片
func sum(nums ...int) int {
    total := 0;
    for _, n := range nums {
        total += n;
    }
    return total;
}
```

**基本写法：展开切片**
`<函数名>(<切片>...)`
```go
// 展开切片传入可变参数函数
numbers := []int{10, 20, 30};
fmt.Println(sum(numbers...));
```

---

## 函数作为一等公民

**基本写法：函数变量**
`<变量名> := func(<参数>) <返回值> { ... }`
```go
// 匿名函数赋值给变量
add := func(a, b int) int {
    return a + b;
};
```

**基本写法：高阶函数（参数）**
`func <函数名>(<参数> <类型>, fn func(<类型>) <返回值>) <返回值>`
```go
// 函数作为参数
func apply(nums []int, fn func(int) int) []int {
    result := make([]int, len(nums));
    for i, n := range nums {
        result[i] = fn(n);
    }
    return result;
}
```

**基本写法：高阶函数（返回值）**
`func <函数名>(<参数>) func(<类型>) <返回值>`
```go
// 返回闭包函数
func multiplier(factor int) func(int) int {
    return func(n int) int {
        return n * factor;
    };
}
```

---

## 闭包

**基本写法：闭包定义**
`func() <返回值> { ... }`
```go
// 闭包捕获并修改外部变量
func counter() func() int {
    count := 0;
    return func() int {
        count++;
        return count;
    };
}
```

**基本写法：闭包参数传递**
`go func(<参数> <类型>) { ... }(<值>)`
```go
// 通过参数传递避免闭包陷阱
for i := 0; i < 3; i++ {
    go func(n int) {
        fmt.Println(n);
    }(i);
}
```

---

## init 函数

**基本写法：init 函数**
`func init() { ... }`
```go
// init 函数自动执行，无法被调用
func init() {
    version = "1.0.0";
    loadConfig();
}
```

---

## 方法定义

**基本写法：值接收者方法**
`func (<接收者> <类型>) <方法名>(<参数>) <返回值> { ... }`
```go
// 值接收者方法
type Circle struct {
    Radius float64;
}

func (c Circle) Area() float64 {
    return math.Pi * c.Radius * c.Radius;
}
```

**基本写法：指针接收者方法**
`func (<接收者> *<类型>) <方法名>(<参数>) <返回值> { ... }`
```go
// 指针接收者方法，可修改原始值
func (c *Circle) Scale(factor float64) {
    c.Radius *= factor;
}
```

---

## 自定义类型方法

**基本写法：自定义类型方法**
`func (<接收者> <类型>) <方法名>() <返回值> { ... }`
```go
// 为自定义类型添加方法
type Celsius float64;

func (c Celsius) ToFahrenheit() float64 {
    return float64(c)*9/5 + 32;
}
```

**基本写法：实现 Stringer 接口**
`func (<接收者> <类型>) String() string { ... }`
```go
// 实现 String 方法
func (c Celsius) String() string {
    return fmt.Sprintf("%.1f°C", c);
}
```

---

## 方法值与方法表达式

**基本写法：方法值**
`<变量> := <实例>.<方法名>`
```go
// 方法值绑定接收者
r := Rect{W: 3, H: 4};
area := r.Area;
fmt.Println(area());
```

**基本写法：方法表达式**
`<变量> := <类型>.<方法名>`
```go
// 方法表达式需要传入接收者
areaFn := Rect.Area;
fmt.Println(areaFn(r));
```

---

## 接口定义与实现

**基本写法：接口定义**
`type <接口名> interface { ... }`
```go
// 定义接口
type Speaker interface {
    Speak() string;
}
```

**基本写法：隐式实现**
`func (<接收者> <类型>) <方法名>() <返回值> { ... }`
```go
// Dog 隐式实现了 Speaker 接口
type Dog struct{ Name string };

func (d Dog) Speak() string {
    return d.Name + " says: Woof!";
}
```

---

## 接口组合

**基本写法：接口组合**
`type <接口名> interface { <接口1>; <接口2> }`
```go
// 组合 Reader 和 Writer
type ReadWriter interface {
    Reader;
    Writer;
}
```

---

## 空接口

**基本写法：空接口**
`any` / `interface{}`
```go
// any 接受任意类型
func printAny(v any) {
    fmt.Println(v);
}
```

---

## 类型断言与类型开关

**基本写法：类型断言**
`<值>.(<类型>)`
```go
// 带检查的类型断言
dog, ok := s.(Dog);
if ok {
    fmt.Println(dog.Name);
}
```

**基本写法：类型开关**
`switch <变量> := <值>.(type) { case ... }`
```go
// 类型开关判断类型
switch v := v.(type) {
case int:
    return fmt.Sprintf("int: %d", v);
case string:
    return fmt.Sprintf("string: %s", v);
default:
    return fmt.Sprintf("unknown: %T", v);
}
```

---

## 函数选项模式

**基本写法：函数选项模式**
`type Option func(*<类型>)`
```go
// 函数选项模式
type Server struct {
    host    string;
    port    int;
    timeout time.Duration;
}

type Option func(*Server);

func WithHost(host string) Option {
    return func(s *Server) { s.host = host };
}

func NewServer(opts ...Option) *Server {
    s := &Server{host: "localhost", port: 8080};
    for _, opt := range opts {
        opt(s);
    }
    return s;
}
```

---

## 中间件模式

**基本写法：中间件模式**
`type <类型> func(<类型>) <类型>`
```go
// 中间件模式
type Handler func(msg string);

func LoggingMiddleware(next Handler) Handler {
    return func(msg string) {
        log.Printf("Before: %s", msg);
        next(msg);
        log.Printf("After: %s", msg);
    };
}
```



<!-- ============ 文档分隔线：016-go/006-GoBasicSyntax.md ============ -->

# Go 基础语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量声明

**基本写法：显式声明变量类型和初始值**
`var <变量名> <类型> = <值>`
```go
// 显式声明变量类型和初始值
var name string = "Go";
```

**基本写法：类型推断声明**
`var <变量名> = <值>`
```go
// 自动推断类型
var age = 15;
```

**单行写法：批量声明多个变量**
`var ( <变量1> <类型1> = <值1>; <变量2> <类型2> = <值2> )`
```go
// 单行批量声明多个变量
var ( x int = 10; y float64 = 3.14; flag bool = true );
```

**换行写法：批量声明多个变量**
`var ( ... )`
```go
// 换行书写批量声明
var (
    x    int     = 10
    y    float64 = 3.14
    flag bool    = true
);
```

**基本写法：短变量声明**
`<变量名> := <值>`
```go
// 仅限函数内使用，自动推断类型
city := "Beijing";
```

**基本写法：零值声明**
`var <变量名> <类型>`
```go
// 未初始化的变量使用零值
var score int; // 0
```

---

## 常量

**基本写法：常量声明**
`const <名称> = <值>`
```go
// 声明常量
const Pi = 3.14159;
```

**单行写法：批量声明常量**
`const ( <名称1> = <值1>; <名称2> = <值2> )`
```go
// 单行批量声明常量
const ( StatusOK = 200; StatusError = 500 );
```

**换行写法：批量声明常量**
`const ( ... )`
```go
// 换行书写批量声明
const (
    StatusOK    = 200
    StatusError = 500
);
```

**基本写法：iota 常量生成器**
`const ( <名称> = iota ... )`
```go
// iota 从 0 开始自动递增
const (
    Sunday    = iota // 0
    Monday           // 1
    Tuesday          // 2
);
```

**基本写法：iota 位运算标志**
`const ( <名称> = 1 << iota ... )`
```go
// 位运算生成权限标志
const (
    ReadPermission   = 1 << iota // 1  (001)
    WritePermission              // 2  (010)
    ExecutePermission            // 4  (100)
);
```

**基本写法：iota 跳过值**
`_ = iota`
```go
// 跳过 0，从 1024 开始
const (
    _  = iota
    KB = 1 << (10 * iota) // 1024
    MB                    // 1048576
);
```

---

## 类型转换

**基本写法：显式类型转换**
`<目标类型>(<值>)`
```go
// int 转 float64
var i int = 42;
var f float64 = float64(i);
```

**基本写法：int 转 string**
`strconv.Itoa(<整数>)`
```go
// int 转 string
s := strconv.Itoa(42);
```

**基本写法：string 转 int**
`strconv.Atoi(<字符串>)`
```go
// string 转 int
n, err := strconv.Atoi("42");
```

**基本写法：string 转 []byte**
`[]byte(<字符串>)`
```go
// string 转 []byte
bytes := []byte("hello");
```

**基本写法：[]byte 转 string**
`string(<字节切片>)`
```go
// []byte 转 string
str := string(bytes);
```

---

## 字符串操作

**基本写法：字符串字节长度**
`len(<字符串>)`
```go
// 字节数（UTF-8 编码）
fmt.Println(len("Hello, 世界")); // 13
```

**基本写法：字符串字符数**
`utf8.RuneCountInString(<字符串>)`
```go
// 字符数（正确处理 Unicode）
fmt.Println(utf8.RuneCountInString("Hello, 世界")); // 9
```

**基本写法：按 rune 遍历字符串**
`for i, r := range <字符串>`
```go
// 按 rune 遍历，正确处理 Unicode
for i, r := range "Hello" {
    fmt.Printf("%d:%c ", i, r);
}
```

**基本写法：判断子串是否存在**
`strings.Contains(<字符串>, <子串>)`
```go
// 查找子串
strings.Contains("Hello, World", "World"); // true
```

**基本写法：判断前缀**
`strings.HasPrefix(<字符串>, <前缀>)`
```go
// 判断前缀
strings.HasPrefix("Hello, World", "Hello"); // true
```

**基本写法：判断后缀**
`strings.HasSuffix(<字符串>, <后缀>)`
```go
// 判断后缀
strings.HasSuffix("Hello, World", "World"); // true
```

**基本写法：查找子串位置**
`strings.Index(<字符串>, <子串>)`
```go
// 查找子串位置
strings.Index("Hello, World", "World"); // 7
```

**基本写法：转大写**
`strings.ToUpper(<字符串>)`
```go
// 转大写
strings.ToUpper("Hello"); // "HELLO"
```

**基本写法：转小写**
`strings.ToLower(<字符串>)`
```go
// 转小写
strings.ToLower("Hello"); // "hello"
```

**基本写法：去除首尾空白**
`strings.TrimSpace(<字符串>)`
```go
// 去除首尾空白
strings.TrimSpace("  hi  "); // "hi"
```

**基本写法：替换字符串**
`strings.Replace(<字符串>, <旧>, <新>, <次数>)`
```go
// 替换字符串
strings.Replace("Hello", "l", "L", 1); // "HeLlo"
```

**基本写法：拆分字符串**
`strings.Split(<字符串>, <分隔符>)`
```go
// 拆分字符串
parts := strings.Split("a,b,c", ",");
```

**基本写法：合并字符串**
`strings.Join(<切片>, <分隔符>)`
```go
// 合并字符串
joined := strings.Join(parts, "-");
```

**基本写法：字符串构建**
`strings.Builder`
```go
// 使用 Builder 高效构建字符串
var b strings.Builder;
b.WriteString("Hello");
b.WriteString(", World");
result := b.String();
```

**基本写法：原始字符串**
`` `<内容> ``
```go
// 反引号包围的原始字符串
raw := `C:\Users\name\file.txt`;
```

---

## 指针

**基本写法：取地址**
`&<变量>`
```go
// 取地址
x := 42;
p := &x; // p 是 *int 类型
```

**基本写法：解引用**
`*<指针>`
```go
// 解引用获取值
fmt.Println(*p); // 42
```

**基本写法：通过指针修改值**
`*<指针> = <值>`
```go
// 通过指针修改值
*p = 100;
```

**基本写法：nil 指针检查**
`if <指针> != nil`
```go
// nil 指针检查
var p *int;
if p != nil {
    fmt.Println(*p);
}
```

**基本写法：指针传递**
`func <函数名>(<参数> *<类型>)`
```go
// 指针传递修改外部变量
func doublePtr(n *int) {
    *n *= 2;
}
```

**基本写法：new 函数**
`new(<类型>)`
```go
// new 分配零值内存
p := new(int);
*p = 42;
```

---

## if 语句

**基本写法：基本 if 语句**
`if <条件> { ... }`
```go
// 基本条件判断
if x > 0 {
    fmt.Println("positive");
} else if x < 0 {
    fmt.Println("negative");
} else {
    fmt.Println("zero");
}
```

**基本写法：带初始化的 if**
`if <初始化>; <条件> { ... }`
```go
// 初始化语句中的变量仅在此块可见
if err := doSomething(); err != nil {
    fmt.Println("Error:", err);
}
```

---

## for 循环

**基本写法：经典三段式**
`for <初始化>; <条件>; <后置> { ... }`
```go
// 经典 for 循环
for i := 0; i < 10; i++ {
    fmt.Println(i);
}
```

**基本写法：while 风格**
`for <条件> { ... }`
```go
// while 风格循环
n := 1;
for n < 100 {
    n *= 2;
}
```

**基本写法：无限循环**
`for { ... }`
```go
// 无限循环
for {
    if shouldBreak() {
        break;
    }
}
```

**基本写法：for-range 遍历**
`for <索引>, <值> := range <集合> { ... }`
```go
// 遍历切片
nums := []int{1, 2, 3};
for i, v := range nums {
    fmt.Printf("index=%d value=%d\n", i, v);
}
```

**基本写法：Go 1.22+ for-range 整数**
`for i := range <整数> { ... }`
```go
// 遍历 0 到 4
for i := range 5 {
    fmt.Println(i);
}
```

---

## switch 语句

**基本写法：基本 switch**
`switch <表达式> { case ... }`
```go
// 基本 switch 语句
switch day {
case "Monday":
    fmt.Println("周一");
case "Tuesday":
    fmt.Println("周二");
default:
    fmt.Println("其他");
}
```

**基本写法：多值匹配**
`case <值1>, <值2>, <值3>:`
```go
// 多值匹配
switch color {
case "red", "green", "blue":
    fmt.Println("基础颜色");
}
```

**基本写法：fallthrough 穿透**
`fallthrough`
```go
// fallthrough 继续执行下一个 case
switch n := 2; n {
case 1:
    fmt.Println("一");
    fallthrough;
case 2:
    fmt.Println("二");
    fallthrough;
case 3:
    fmt.Println("三");
}
```

**基本写法：无条件 switch**
`switch { case <条件>: ... }`
```go
// 无条件 switch
score := 85;
switch {
case score >= 90:
    fmt.Println("A");
case score >= 80:
    fmt.Println("B");
default:
    fmt.Println("D");
}
```

---

## break 与 continue

**基本写法：continue 跳过**
`continue`
```go
// 跳过当前迭代
for i := 0; i < 10; i++ {
    if i == 3 {
        continue;
    }
    fmt.Println(i);
}
```

**基本写法：break 退出**
`break`
```go
// 退出循环
for i := 0; i < 10; i++ {
    if i == 7 {
        break;
    }
    fmt.Println(i);
}
```

**基本写法：标签跳转**
`break <标签>`
```go
// 标签跳转跳出外层循环
outer:
for i := 0; i < 3; i++ {
    for j := 0; j < 3; j++ {
        if i == 1 && j == 1 {
            break outer;
        }
    }
}
```

---

## defer 语句

**基本写法：基本 defer**
`defer <函数调用>`
```go
// 确保文件关闭
func readFile(path string) {
    file, err := os.Open(path);
    if err != nil {
        return;
    }
    defer file.Close();
}
```

**基本写法：defer 执行顺序**
`defer <函数调用>`
```go
// 多个 defer 按后进先出执行
defer fmt.Println("第一");  // 最后执行
defer fmt.Println("第二");  // 第二执行
defer fmt.Println("第三");  // 最先执行
```

**基本写法：defer 参数求值**
`defer <函数>(<参数>)`
```go
// 参数在声明时求值
x := 10;
defer fmt.Println(x); // 输出 10
x = 20;
```

**基本写法：defer 修改命名返回值**
`defer func() { ... }()`
```go
// defer 修改命名返回值
func double() (result int) {
    defer func() {
        result *= 2;
    }();
    return 5;
}
```

---

## Go 1.24+ 新特性

**基本写法：Go 1.24 generic type aliases**
`type <别名>[T] = <类型>[T]`
```go
// 泛型类型别名：为泛型类型定义简短别名
type List[T] = []T
type Map[K, V] = map[K]V
type Set[T comparable] = map[T]struct{}
// 使用别名声明变量
var names List[string] = []string{"Go", "Rust"}
var ages Map[string, int] = map[string]int{"Alice": 30}
```

**基本写法：Go 1.24 range-over-func**
`for <x> := range <func> { }`
```go
// range 遍历函数：迭代器函数签名为 func(yield func(T) bool)
func gen(yield func(int) bool) {
    for i := 0; i < 3; i++ {
        if !yield(i * 10) {
            return
        }
    }
}
// 使用 range-over-func 直接遍历函数
for v := range gen {
    fmt.Println(v) // 依次输出 0 10 20
}
```

**基本写法：Go 1.24 weak pointer**
`runtime.AddCleanup(<obj>, <cleanup>, <arg>)`
```go
// 通过 runtime.AddCleanup 注册清理回调，实现弱引用语义
type Big struct{ data [1024]byte }
obj := &Big{}
obj.data[0] = 42
// 当 obj 被 GC 回收时执行清理函数，arg 作为参数传入
runtime.AddCleanup(obj, func(arg int) {
    fmt.Println("对象被回收，传入参数 =", arg)
}, 100)
// 主动解除引用，等待 GC 触发清理
obj = nil
runtime.GC()
```

**基本写法：Go 1.24 toolchain 指令**
`//go:toolchain <版本>`
```go
// 在 go.mod 文件头部指定工具链版本
// go 1.24.0
// toolchain go1.24.3
//go:toolchain go1.24.3

module example.com/myapp

go 1.24.0
```

**基本写法：Go 1.26 new(expr) 内置函数**
`new(<expr>)`
```go
// Go 1.26：new 支持任意表达式，返回指向表达式结果的指针
x := 42
// 直接对表达式结果取地址
p := new(x*2 + 1) // *int，指向值为 85 的内存
fmt.Println(*p)   // 输出 85
// 等价于传统写法
// v := x*2 + 1; p := &v
```



<!-- ============ 文档分隔线：016-go/007-InterfaceTypeAssertion.md ============ -->

# Go 接口与类型断言

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 接口定义

**基本写法：基本接口**
`type <接口名> interface { <方法签名> }`
```go
// 定义接口
type Speaker interface {
    Speak() string;
}
```

**基本写法：组合接口**
`type <接口名> interface { <接口1>; <接口2> }`
```go
// 组合接口
type ReadWriter interface {
    Reader;
    Writer;
}
```

**基本写法：空接口**
`any` / `interface{}`
```go
// any 接受任意类型
func printAny(v any) {
    fmt.Println(v);
}
```

---

## 接口实现

**基本写法：隐式实现**
`func (<接收者> <类型>) <方法名>() <返回值> { ... }`
```go
// Dog 隐式实现 Speaker
type Dog struct{ Name string };

func (d Dog) Speak() string {
    return d.Name + " says: Woof!";
}
```

**基本写法：接口赋值**
`var <接口变量> <接口名> = <实例>`
```go
// 接口变量持有具体类型实例
var s Speaker = Dog{Name: "Rex"};
fmt.Println(s.Speak());
```

---

## 类型断言

**基本写法：基本类型断言**
`<值>.(<类型>)`
```go
// 直接断言（失败会 panic）
var i any = "hello";
s := i.(string);
```

**基本写法：带检查的类型断言**
`<值>, <ok> := <接口值>.(<类型>)`
```go
// 带检查的断言
s, ok := i.(string);
if ok {
    fmt.Println(s);
}
```

---

## 类型开关

**基本写法：类型开关**
`switch <变量> := <值>.(type) { case ... }`
```go
// 类型开关判断类型
switch v := i.(type) {
case int:
    fmt.Printf("int: %d\n", v);
case string:
    fmt.Printf("string: %s\n", v);
case []byte:
    fmt.Printf("bytes: %v\n", v);
default:
    fmt.Printf("unknown: %T\n", v);
}
```

**基本写法：多个类型同一分支**
`case <类型1>, <类型2>:`
```go
// 多个类型同一处理
switch v := i.(type) {
case int, int64, float64:
    fmt.Printf("number: %v\n", v);
case string:
    fmt.Printf("string: %s\n", v);
}
```

---

## 接口嵌套

**基本写法：接口嵌套**
`type <接口名> interface { <接口1>; <接口2>; <方法> }`
```go
// 接口嵌套
type Reader interface {
    Read(p []byte) (n int, err error);
}

type Writer interface {
    Write(p []byte) (n int, err error);
}

type ReadWriter interface {
    Reader;
    Writer;
}
```

---

## 空接口应用

**基本写法：空接口作为参数**
`func <函数名>(<参数> any) { ... }`
```go
// 接受任意类型参数
func printAny(v any) {
    fmt.Println(v);
}
```

**基本写法：空接口切片**
`[]any`
```go
// 存储任意类型的切片
mixed := []any{42, "hello", 3.14, true};
for _, v := range mixed {
    fmt.Printf("%T: %v\n", v, v);
}
```

---

## 接口组合模式

**基本写法：接口隔离原则**
`type <接口名> interface { ... }`
```go
// 小接口组合
type Sizer interface {
    Size() int;
}

type Stringer interface {
    String() string;
}

// 组合使用
type SizableStringer interface {
    Sizer;
    Stringer;
}
```

---

## 鸭子类型检查

**基本写法：编译期接口检查**
`var _ <接口名> = <类型>{}`
```go
// 编译期检查 Dog 是否实现 Speaker
var _ Speaker = Dog{};
```

---

## 接口零值

**基本写法：nil 接口**
`var <变量> <接口名>`
```go
// nil 接口调用方法会 panic
var s Speaker;
if s != nil {
    s.Speak();
}
```

**基本写法：nil 指针接收者**
`var <接口变量> <接口名> = (<类型>)(nil)`
```go
// 接口持有 nil 指针
type MyError struct{ Msg string };

func (e *MyError) Error() string {
    if e == nil {
        return "nil error";
    }
    return e.Msg;
}

var err error = (*MyError)(nil);
fmt.Println(err.Error()); // "nil error"
```

---

## 类型别名与类型定义

**基本写法：类型定义**
`type <新类型> <底层类型>`
```go
// 类型定义，Celsius 是新类型
type Celsius float64;
```

**基本写法：类型别名**
`type <别名> = <原类型>`
```go
// 类型别名，与原类型完全相同
type Text = string;
```

---

## 可比较接口

**基本写法：可比较类型作为 map 键**
`map[<接口>]<值类型>`
```go
// 接口作为 map 键（仅限可比较类型）
type Key interface{};

m := map[Key]string{};
m[1] = "one";
m["two"] = "two";
```



<!-- ============ 文档分隔线：016-go/008-MemoryAlignment.md ============ -->

# Go 内存对齐

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本类型大小

**基本写法：获取基本类型大小**
`unsafe.Sizeof(<变量>)`
```go
// 基本类型大小
fmt.Println(unsafe.Sizeof(bool(false)));     // 1
fmt.Println(unsafe.Sizeof(int8(0)));         // 1
fmt.Println(unsafe.Sizeof(int16(0)));        // 2
fmt.Println(unsafe.Sizeof(int32(0)));        // 4
fmt.Println(unsafe.Sizeof(int64(0)));        // 8
fmt.Println(unsafe.Sizeof(float64(0)));      // 8
fmt.Println(unsafe.Sizeof(string("")));     // 16
fmt.Println(unsafe.Sizeof(int(0)));          // 8
```

---

## 对齐边界

**基本写法：获取对齐边界**
`unsafe.Alignof(<变量>)`
```go
// 基本类型的对齐边界
fmt.Println(unsafe.Alignof(bool(false)));    // 1
fmt.Println(unsafe.Alignof(int8(0)));       // 1
fmt.Println(unsafe.Alignof(int16(0)));      // 2
fmt.Println(unsafe.Alignof(int32(0)));      // 4
fmt.Println(unsafe.Alignof(int64(0)));      // 8
fmt.Println(unsafe.Alignof(float64(0)));    // 8
```

---

## 结构体对齐

**基本写法：未优化布局**
`type <类型名> struct { ... }`
```go
// 优化前：24 字节
type Bad struct {
    A bool;    // 1 + 7 padding
    B int64;   // 8
    C int32;   // 4 + 4 padding
}
```

**基本写法：优化后布局**
`type <类型名> struct { ... }`
```go
// 优化后：16 字节
type Optimized struct {
    B int64;   // 8
    C int32;   // 4
    A bool;    // 1 + 3 padding
}
```

**基本写法：查看结构体大小**
`unsafe.Sizeof(<结构体>{})`
```go
// 查看结构体大小
fmt.Println(unsafe.Sizeof(Bad{}));       // 24
fmt.Println(unsafe.Sizeof(Optimized{})); // 16
```

---

## 字段偏移量

**基本写法：获取字段偏移量**
`unsafe.Offsetof(<结构体>.<字段>)`
```go
// 获取字段偏移量
type User struct {
    ID   int;
    Name string;
}
fmt.Println(unsafe.Offsetof(User{}.ID));   // 0
fmt.Println(unsafe.Offsetof(User{}.Name)); // 8
```

---

## 对齐计算

**基本写法：计算对齐填充**
`(<偏移> + <对齐> - 1) &^ (<对齐> - 1)`
```go
// 计算对齐后的偏移量
offset := 3;
align := 8;
aligned := (offset + align - 1) &^ (align - 1);
fmt.Println(aligned); // 8
```

---

## 空结构体

**基本写法：空结构体大小**
`unsafe.Sizeof(struct{}{})`
```go
// 空结构体大小为 0
fmt.Println(unsafe.Sizeof(struct{}{})); // 0
```

**基本写法：空结构体作为字段**
`type <类型名> struct { ... }`
```go
// 空结构体作为最后一个字段
type S struct {
    A int;
    _ struct{};
}
```

---

## 结构体嵌入对齐

**基本写法：嵌入结构体对齐**
`type <类型名> struct { <嵌入类型>; ... }`
```go
// 嵌入结构体的对齐
type Inner struct {
    X int64;
}

type Outer struct {
    A bool;
    Inner;
    B int32;
}
```

---

## 切片与字符串对齐

**基本写法：切片大小**
`unsafe.Sizeof(<切片>)`
```go
// 切片大小为 24（指针+len+cap）
s := []int{1, 2, 3};
fmt.Println(unsafe.Sizeof(s)); // 24
```

**基本写法：字符串大小**
`unsafe.Sizeof(<字符串>)`
```go
// 字符串大小为 16（指针+len）
str := "hello";
fmt.Println(unsafe.Sizeof(str)); // 16
```

---

## 指针大小

**基本写法：指针大小**
`unsafe.Sizeof(&<变量>)`
```go
// 64 位系统指针大小为 8
x := 42;
fmt.Println(unsafe.Sizeof(&x)); // 8
```

**基本写法：map 大小**
`unsafe.Sizeof(<map>)`
```go
// map 是指针类型，大小为 8
m := map[string]int{};
fmt.Println(unsafe.Sizeof(m)); // 8
```

---

## 64 位原子操作对齐

**基本写法：原子操作对齐要求**
`type <类型名> struct { ... }`
```go
// 64 位原子操作要求 8 字节对齐
type Counter struct {
    _ [56]byte; // padding 确保 64 位对齐
    n int64;
}
```

**基本写法：使用 atomic.Int64**
`type <类型名> struct { ... }`
```go
// Go 1.19+ 使用 atomic 类型自动对齐
type Counter struct {
    n atomic.Int64;
}
```

---

## 内存对齐优化

**基本写法：按大小降序排列**
`type <类型名> struct { ... }`
```go
// 按字段大小降序排列减少 padding
type Optimized struct {
    B int64;   // 8
    C int32;   // 4
    A bool;    // 1 + 3 padding
}
```

**基本写法：手动 padding**
`type <类型名> struct { ... }`
```go
// 手动添加 padding
type Padded struct {
    A bool;
    _ [7]byte; // 显式 padding
    B int64;
}
```

---

## 内存对齐验证

**基本写法：验证对齐**
`unsafe.Alignof(<结构体>{})`
```go
// 验证结构体对齐
type S struct {
    A bool;
    B int64;
}
fmt.Println(unsafe.Alignof(S{})); // 8
```

**基本写法：验证偏移**
`unsafe.Offsetof(<结构体>.<字段>)`
```go
// 验证字段偏移
type S struct {
    A bool;
    B int64;
}
fmt.Println(unsafe.Offsetof(S{}.B)); // 8
```



<!-- ============ 文档分隔线：016-go/009-GoDataStructure.md ============ -->

# Go 数据结构

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 数组声明

**基本写法：固定长度数组**
`var <变量名> [<长度>]<类型>`
```go
// 声明长度为 5 的 int 数组
var a [5]int;
```

**基本写法：字面量初始化数组**
`[<长度>]<类型>{ ... }`
```go
// 字面量初始化
b := [3]string{"Go", "Rust", "C"};
```

**基本写法：自动推断长度数组**
`[...]<类型>{ ... }`
```go
// 编译器推断长度为 4
c := [...]int{1, 2, 3, 4};
```

**基本写法：指定索引初始化**
`[<长度>]<类型>{ <索引>: <值> }`
```go
// 索引 1 和 3 赋值，其余为零值
d := [5]int{1: 10, 3: 30};
```

---

## 数组操作

**基本写法：访问数组元素**
`<数组>[<索引>]`
```go
// 访问数组元素
arr := [5]int{10, 20, 30, 40, 50};
fmt.Println(arr[0]);
```

**基本写法：修改数组元素**
`<数组>[<索引>] = <值>`
```go
// 修改数组元素
arr[0] = 100;
```

**基本写法：遍历数组**
`for <索引>, <值> := range <数组> { ... }`
```go
// 遍历数组
for i, v := range arr {
    fmt.Printf("arr[%d] = %d\n", i, v);
}
```

---

## 切片创建

**基本写法：nil 切片**
`var <变量名> []<类型>`
```go
// nil 切片
var s []int;
```

**基本写法：字面量切片**
`[]<类型>{ ... }`
```go
// 切片字面量
s1 := []int{1, 2, 3};
```

**基本写法：make 创建切片（指定长度）**
`make([]<类型>, <长度>)`
```go
// 长度 5，容量 5
s2 := make([]int, 5);
```

**基本写法：make 创建切片（指定长度和容量）**
`make([]<类型>, <长度>, <容量>)`
```go
// 长度 0，容量 10
s3 := make([]int, 0, 10);
```

**基本写法：从数组切片**
`<数组>[<起始>:<结束>]`
```go
// 左闭右开区间
arr := [5]int{10, 20, 30, 40, 50};
s4 := arr[1:4]; // [20 30 40]
```

**基本写法：从数组头部切片**
`<数组>[:<结束>]`
```go
// 从头到索引 3
s5 := arr[:3]; // [10 20 30]
```

**基本写法：从数组尾部切片**
`<数组>[<起始>:]`
```go
// 从索引 2 到末尾
s6 := arr[2:]; // [30 40 50]
```

---

## 切片操作

**基本写法：追加单个元素**
`append(<切片>, <元素>)`
```go
// 追加单个元素
s = append(s, 6);
```

**基本写法：追加多个元素**
`append(<切片>, <元素1>, <元素2>, <元素3>)`
```go
// 追加多个元素
s = append(s, 7, 8, 9);
```

**基本写法：追加切片**
`append(<切片>, <另一切片>...)`
```go
// 追加另一个切片
other := []int{10, 11};
s = append(s, other...);
```

**基本写法：复制切片**
`copy(<目标>, <源>)`
```go
// 复制切片内容
src := []int{1, 2, 3};
dst := make([]int, len(src));
copy(dst, src);
```

**基本写法：删除元素（不保序）**
`<切片>[<索引>] = <切片>[len(<切片>)-1]`
```go
// 删除索引 2，不保序
s := []int{1, 2, 3, 4, 5};
s[2] = s[len(s)-1];
s = s[:len(s)-1];
```

**基本写法：删除元素（保序）**
`append(<切片>[:<索引>], <切片>[<索引>+1:]...)`
```go
// 删除索引 2，保序
s = append(s[:2], s[3:]...);
```

**基本写法：三索引切片**
`<切片>[<起始>:<结束>:<容量>]`
```go
// 限制容量，append 触发扩容不影响原切片
b := a[1:3:3];
```

---

## Map 创建

**基本写法：make 创建 Map**
`make(map[<键类型>]<值类型>)`
```go
// 创建空 map
m1 := make(map[string]int);
```

**单行写法：字面量创建 Map**
`map[<键类型>]<值类型>{ <键1>: <值1>, <键2>: <值2> }`
```go
// 单行字面量初始化
m2 := map[string]int{ "apple": 5, "banana": 3 };
```

**换行写法：字面量创建 Map**
`map[<键类型>]<值类型>{ ... }`
```go
// 换行书写字面量初始化
m2 := map[string]int{
    "apple":  5,
    "banana": 3,
};
```

**基本写法：预分配容量 Map**
`make(map[<键类型>]<值类型>, <容量>)`
```go
// 预分配约 1000 个键的空间
m := make(map[string]int, 1000);
```

---

## Map 操作

**基本写法：添加/修改**
`<map>[<键>] = <值>`
```go
// 添加或修改
m1["one"] = 1;
```

**基本写法：获取值**
`<值> := <map>[<键>]`
```go
// 获取值（不存在返回零值）
v := m1["one"];
```

**基本写法：检查键是否存在**
`<值>, <ok> := <map>[<键>]`
```go
// 检查键是否存在
v, ok := m2["orange"];
if !ok {
    fmt.Println("orange 不存在");
}
```

**基本写法：删除键**
`delete(<map>, <键>)`
```go
// 删除键
delete(m1, "one");
```

**基本写法：遍历 Map**
`for <键>, <值> := range <map> { ... }`
```go
// 遍历 map
for k, v := range m2 {
    fmt.Printf("%s: %d\n", k, v);
}
```

---

## 结构体定义

**基本写法：结构体声明**
`type <类型名> struct { ... }`
```go
// 定义结构体
type User struct {
    ID    int;
    Name  string;
    Email string;
    Age   int;
}
```

**基本写法：按字段名初始化**
`<类型>{ <字段>: <值> }`
```go
// 按字段名初始化
u1 := User{ID: 1, Name: "Alice", Email: "alice@example.com", Age: 30};
```

**基本写法：部分初始化**
`<类型>{ <字段>: <值> }`
```go
// 部分初始化，其余为零值
u3 := User{Name: "Charlie"};
```

**基本写法：指针结构体**
`&<类型>{ ... }`
```go
// 创建结构体指针
p := &User{Name: "Dave"};
fmt.Println(p.Name);
```

---

## 结构体嵌入与组合

**基本写法：匿名嵌入**
`type <类型> struct { <嵌入类型>; ... }`
```go
// 匿名嵌入实现组合
type Employee struct {
    User;              // 字段提升
    Address;           // 字段提升
    Department string;
}
```

**基本写法：访问嵌入字段**
`<实例>.<字段>`
```go
// 直接访问嵌入字段
e := Employee{User: User{Name: "Alice"}, Department: "Engineering"};
fmt.Println(e.Name);
```

---

## 结构体标签

**基本写法：字段标签**
`` <字段> <类型> `<标签>: "<值>"` ``
```go
// 使用 json 和 validate 标签
type User struct {
    ID    int    `json:"id" db:"user_id"`;
    Name  string `json:"name" validate:"required,min=2"`;
    Pass  string `json:"-" validate:"min=8"`;
}
```

**基本写法：读取标签**
`<字段>.Tag.Get("<标签名>")`
```go
// 通过反射读取标签
t := reflect.TypeOf(User{});
field, _ := t.FieldByName("Name");
fmt.Println(field.Tag.Get("json"));
```

---

## JSON 序列化

**基本写法：序列化**
`json.Marshal(<结构体>)`
```go
// 结构体转 JSON
r := Response{Code: 200, Message: "OK"};
bytes, err := json.Marshal(r);
```

**基本写法：格式化序列化**
`json.MarshalIndent(<结构体>, "", "  ")`
```go
// 格式化输出 JSON
pretty, _ := json.MarshalIndent(r, "", "  ");
```

**基本写法：反序列化**
`json.Unmarshal(<字节>, &<结构体>)`
```go
// JSON 转结构体
jsonStr := `{"code":404,"message":"Not Found"}`;
var resp Response;
err := json.Unmarshal([]byte(jsonStr), &resp);
```

---

## 结构体比较

**基本写法：可比较结构体**
`<结构体1> == <结构体2>`
```go
// 所有字段可比较的结构体
type Point struct{ X, Y int };
p1 := Point{1, 2};
p2 := Point{1, 2};
fmt.Println(p1 == p2); // true
```

---

## 结构体内存布局

**基本写法：未优化布局**
`type <类型> struct { ... }`
```go
// 优化前：24 字节
type Bad struct {
    A bool;    // 1 + 7 padding
    B int64;   // 8
    C int32;   // 4 + 4 padding
}
```

**基本写法：优化后布局**
`type <类型> struct { ... }`
```go
// 优化后：16 字节
type Optimized struct {
    B int64;   // 8
    C int32;   // 4
    A bool;    // 1 + 3 padding
}
```

**基本写法：查看结构体大小**
`unsafe.Sizeof(<结构体>{})`
```go
// 查看结构体大小
fmt.Println(unsafe.Sizeof(Bad{}));       // 24
fmt.Println(unsafe.Sizeof(Optimized{})); // 16
```



<!-- ============ 文档分隔线：016-go/010-UnsafePointer.md ============ -->

# Go unsafe 与指针

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## unsafe.Pointer

**基本写法：获取指针**
`unsafe.Pointer(&<变量>)`
```go
// 获取变量的 unsafe.Pointer
x := 42;
p := unsafe.Pointer(&x);
```

**基本写法：指针转换回普通指针**
`(*<类型>)(unsafe.Pointer(&<变量>))`
```go
// 转换回 *int
pInt := (*int)(p);
```

---

## 指针类型转换

**基本写法：int 转 float64**
`*(*<目标类型>)(unsafe.Pointer(&<变量>))`
```go
// 将 int 的位模式解释为 float64
var i int64 = 0x400921FB54442D18;
f := *(*float64)(unsafe.Pointer(&i));
fmt.Println(f); // 3.141592653589793
```

**基本写法：float64 转 int**
`*(*<目标类型>)(unsafe.Pointer(&<变量>))`
```go
// 将 float64 的位模式解释为 int64
var f = 3.14;
i := *(*int64)(unsafe.Pointer(&f));
```

**基本写法：[]byte 转 string**
`*(*string)(unsafe.Pointer(&<切片>))`
```go
// 零拷贝将 []byte 转为 string
b := []byte("hello");
s := *(*string)(unsafe.Pointer(&b));
```

---

## unsafe.Sizeof

**基本写法：获取变量大小**
`unsafe.Sizeof(<变量>)`
```go
// 获取 int 类型大小
fmt.Println(unsafe.Sizeof(int(0))); // 8
```

**基本写法：获取结构体大小**
`unsafe.Sizeof(<结构体>{})`
```go
// 获取结构体大小
type Point struct{ X, Y int };
fmt.Println(unsafe.Sizeof(Point{})); // 16
```

---

## unsafe.Offsetof

**基本写法：获取字段偏移量**
`unsafe.Offsetof(<结构体>.<字段>)`
```go
// 获取字段在结构体中的偏移量
type User struct {
    ID   int;
    Name string;
}
fmt.Println(unsafe.Offsetof(User{}.ID));   // 0
fmt.Println(unsafe.Offsetof(User{}.Name)); // 8
```

---

## unsafe.Alignof

**基本写法：获取对齐边界**
`unsafe.Alignof(<变量>)`
```go
// 获取类型的对齐边界
fmt.Println(unsafe.Alignof(int64(0))); // 8
```

**基本写法：获取结构体对齐**
`unsafe.Alignof(<结构体>{})`
```go
// 获取结构体的对齐边界
type S struct {
    A bool;
    B int64;
}
fmt.Println(unsafe.Alignof(S{})); // 8
```

---

## 指针运算

**基本写法：指针加法**
`unsafe.Pointer(uintptr(<指针>) + <偏移>)`
```go
// 指针偏移访问数组元素
arr := [3]int{10, 20, 30};
p := unsafe.Pointer(&arr[0]);
p2 := unsafe.Pointer(uintptr(p) + unsafe.Sizeof(arr[0]));
fmt.Println(*(*int)(p2)); // 20
```

**基本写法：uintptr 转换**
`uintptr(unsafe.Pointer(&<变量>))`
```go
// 转换为 uintptr 用于指针运算
addr := uintptr(unsafe.Pointer(&x));
```

---

## SliceHeader

**基本写法：获取 SliceHeader**
`(*reflect.SliceHeader)(unsafe.Pointer(&<切片>))`
```go
// 获取切片的底层结构
s := []int{1, 2, 3};
header := (*reflect.SliceHeader)(unsafe.Pointer(&s));
fmt.Println(header.Len);    // 3
fmt.Println(header.Cap);    // 3
```

---

## StringHeader

**基本写法：获取 StringHeader**
`(*reflect.StringHeader)(unsafe.Pointer(&<字符串>))`
```go
// 获取字符串的底层结构
s := "hello";
header := (*reflect.StringHeader)(unsafe.Pointer(&s));
fmt.Println(header.Len); // 5
```

---

## 零拷贝转换

**基本写法：string 转 []byte**
`*(*[]byte)(unsafe.Pointer(&<字符串变量>))`
```go
// 零拷贝 string 转 []byte
s := "hello";
b := *(*[]byte)(unsafe.Pointer(&s));
```

**基本写法：[]byte 转 string**
`*(*string)(unsafe.Pointer(&<切片变量>))`
```go
// 零拷贝 []byte 转 string
b := []byte("hello");
s := *(*string)(unsafe.Pointer(&b));
```

---

## 内存操作

**基本写法：内存拷贝**
`unsafe.Pointer(<目标>)`
```go
// 指针内存拷贝
src := [4]byte{1, 2, 3, 4};
var dst [4]byte;
copy(dst[:], src[:]);
```

---

## unsafe.Add

**基本写法：指针加法（Go 1.17+）**
`unsafe.Add(<指针>, <偏移>)`
```go
// Go 1.17+ 指针加法
arr := [3]int{10, 20, 30};
p := unsafe.Pointer(&arr[0]);
p2 := unsafe.Add(p, unsafe.Sizeof(arr[0]));
fmt.Println(*(*int)(p2)); // 20
```

---

## unsafe.Slice

**基本写法：从指针创建切片（Go 1.17+）**
`unsafe.Slice(<指针>, <长度>)`
```go
// Go 1.17+ 从指针创建切片
arr := [3]int{10, 20, 30};
p := &arr[0];
s := unsafe.Slice(p, 3);
fmt.Println(s); // [10 20 30]
```

---

## 注意事项

**基本写法：uintptr 不能作为指针存储**
`uintptr(unsafe.Pointer(&<变量>))`
```go
// uintptr 只是一个数值，GC 不视为指针
// 仅用于临时指针运算
addr := uintptr(unsafe.Pointer(&x));
```



<!-- ============ 文档分隔线：016-go/011-GoGoroutineChannel.md ============ -->

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



<!-- ============ 文档分隔线：016-go/012-GoContext.md ============ -->

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



<!-- ============ 文档分隔线：016-go/013-GoTesting.md ============ -->

# Go testing 包

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本测试

**基本写法：测试函数**
`func Test<名称>(t *testing.T)`
```go
// 测试函数名必须以 Test 开头
func TestAdd(t *testing.T) {
    got := Add(1, 2)
    if got != 3 {
        t.Errorf("Add(1,2) = %d, want 3", got)
    }
}
```

**基本写法：报告失败**
`t.Error(<消息>)`
```go
// 报告失败并继续执行
t.Error("结果不匹配")
```

**基本写法：报告失败并停止**
`t.Fatal(<消息>)`
```go
// 报告失败并立即停止当前测试
t.Fatal("致命错误")
```

**基本写法：格式化报告失败**
`t.Errorf(<格式>, <参数>)`
```go
// 格式化输出失败信息
t.Errorf("got %d, want %d", got, want)
```

**基本写法：标记失败**
`t.Fail()`
```go
// 标记失败但继续执行
t.Fail()
```

**基本写法：跳过测试**
`t.Skip(<原因>)`
```go
// 跳过当前测试
if testing.Short() {
    t.Skip("跳过长测试")
}
```

---

## 断言辅助

**换行写法：手动断言相等**
`if got != want { t.Errorf(...) }`
```go
// 手动比较并报告
func TestEqual(t *testing.T) {
    got, want := Add(1, 2), 3
    if got != want {
        t.Errorf("got %d, want %d", got, want)
    }
}
```

**换行写法：使用 testify 断言**
`assert.Equal(t, <期望>, <实际>)`
```go
// 使用第三方库 testify 断言
import "github.com/stretchr/testify/assert"
assert.Equal(t, 3, Add(1, 2))
assert.NoError(t, err)
```

**换行写法：require 强制断言**
`require.NoError(t, err)`
```go
// 失败时立即停止测试
import "github.com/stretchr/testify/require"
require.NoError(t, err)
require.Equal(t, 3, result)
```

---

## 表驱动测试

**换行写法：表驱动测试**
`tests := []struct{ ... }{ ... }`
```go
// 表驱动测试模式
func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"正数", 1, 2, 3},
        {"负数", -1, -2, -3},
        {"零", 0, 0, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.expected {
                t.Errorf("got %d, want %d", got, tt.expected)
            }
        })
    }
}
```

---

## 子测试

**基本写法：运行子测试**
`t.Run(<名称>, func(t *testing.T) { ... })`
```go
// 子测试可单独运行
t.Run("正常情况", func(t *testing.T) {
    // 测试逻辑
})
t.Run("边界情况", func(t *testing.T) {
    // 测试逻辑
})
```

**基本写法：并行子测试**
`t.Parallel()`
```go
// 在子测试中调用 Parallel 实现并行
t.Run("并发测试", func(t *testing.T) {
    t.Parallel()
    // 测试逻辑
})
```

---

## 并行测试

**基本写法：标记并行测试**
`t.Parallel()`
```go
// 在测试函数开头调用
func TestParallel(t *testing.T) {
    t.Parallel()
    // 测试逻辑
}
```

**基本写法：控制并行数量**
`-parallel <数量>`
```go
// 运行时指定并行数
// go test -parallel 4
```

---

## 基准测试

**基本写法：基准测试函数**
`func Benchmark<名称>(b *testing.B)`
```go
// 基准测试函数以 Benchmark 开头
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(1, 2)
    }
}
```

**基本写法：Go 1.24+ b.Loop**
`for b.Loop() { ... }`
```go
// Go 1.24+ 推荐写法，自动管理迭代
func BenchmarkAdd(b *testing.B) {
    for b.Loop() {
        Add(1, 2)
    }
}
```

**基本写法：基准测试计时控制**
`b.ResetTimer()`
```go
// 重置计时器，排除初始化耗时
func BenchmarkProcess(b *testing.B) {
    data := setupData()
    b.ResetTimer()
    for b.Loop() {
        process(data)
    }
}
```

**基本写法：报告内存分配**
`b.ReportAllocs()`
```go
// 报告每次操作的内存分配
func BenchmarkAlloc(b *testing.B) {
    b.ReportAllocs()
    for b.Loop() {
        _ = make([]int, 100)
    }
}
```

**基本写法：自定义指标**
`b.ReportMetric(<值>, <名称>)`
```go
// 报告自定义指标
func BenchmarkCustom(b *testing.B) {
    for b.Loop() {
        result := doWork()
        b.ReportMetric(float64(result.Items), "items/op")
    }
}
```

**基本写法：运行基准测试**
`go test -bench=<模式>`
```go
// 运行所有基准测试
// go test -bench=.
// go test -bench=BenchmarkAdd -benchmem
```

---

## 示例测试

**基本写法：示例函数**
`func Example<名称>()`
```go
// 以 Example 开头，Output 注释声明期望输出
func ExampleAdd() {
    fmt.Println(Add(1, 2))
    // Output: 3
}
```

**基本写法：无输出示例**
`func Example<名称>()`
```go
// 不检查输出的示例
func ExampleUsage() {
    result := Process(data)
    fmt.Println(result)
    // Unordered output:
    // some line
}
```

---

## 测试辅助

**基本写法：临时目录**
`t.TempDir()`
```go
// 自动创建并在测试结束后清理的临时目录
func TestFileWrite(t *testing.T) {
    dir := t.TempDir()
    path := filepath.Join(dir, "test.txt")
    os.WriteFile(path, []byte("hi"), 0644)
}
```

**基本写法：Go 1.24+ 切换工作目录**
`t.Chdir(<目录>)`
```go
// Go 1.24+ 测试期间切换工作目录，测试结束自动恢复
func TestCwd(t *testing.T) {
    t.Chdir("/tmp")
    // 当前工作目录为 /tmp
}
```

**基本写法：helper 函数标记**
`t.Helper()`
```go
// 标记为辅助函数，报错时定位到调用方
func assertEqual(t *testing.T, got, want int) {
    t.Helper()
    if got != want {
        t.Errorf("got %d, want %d", got, want)
    }
}
```

**基本写法：清理函数**
`t.Cleanup(func() { ... })`
```go
// 注册清理函数，测试结束后按 LIFO 执行
t.Cleanup(func() {
    os.Remove(tempFile)
})
```

**基本写法：设置超时**
`t.SetDeadline(<时间>)`
```go
// Go 1.24+ 为测试设置截止时间
t.SetDeadline(time.Now().Add(30 * time.Second))
```

---

## 测试覆盖率

**基本写法：生成覆盖率报告**
`go test -cover`
```go
// 运行测试并显示覆盖率百分比
// go test -cover
```

**基本写法：生成覆盖率文件**
`go test -coverprofile=<文件>`
```go
// 输出覆盖率到文件
// go test -coverprofile=coverage.out
// go tool cover -html=coverage.out
```

**基本写法：按包覆盖率**
`go test -coverpkg=<包路径>`
```go
// 跨包覆盖率统计
// go test -coverpkg=./... ./...
```

---

## Go 1.24+ 测试新特性

**基本写法：testing/synctest 并发测试**
`synctest.Run(func() { ... })`
```go
// Go 1.24+ 实验性并发测试，模拟时间无需真实等待
import "testing/synctest"
func TestTimeout(t *testing.T) {
    synctest.Run(func() {
        ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
        defer cancel()
        synctest.Wait()
        <-ctx.Done()
    })
}
```

**基本写法：Go 1.24+ 测试日志 JSON 输出**
`go test -json`
```go
// Go 1.24+ 构建输出也以 JSON 格式报告
// go test -json ./...
```



<!-- ============ 文档分隔线：016-go/014-GoStandardLibrary.md ============ -->

# Go 标准库速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## fmt 格式化

**基本写法：格式化输出**
`fmt.Printf(<格式串>, <参数>)`
```go
// 格式化输出到标准输出
fmt.Printf("name=%s age=%d\n", "Go", 15)
```

**基本写法：格式化为字符串**
`fmt.Sprintf(<格式串>, <参数>)`
```go
// 返回格式化字符串
s := fmt.Sprintf("x=%d", 42)
```

**基本写法：格式化到 Writer**
`fmt.Fprintf(<writer>, <格式串>, <参数>)`
```go
// 输出到实现了 io.Writer 的对象
fmt.Fprintf(os.Stdout, "count=%d\n", 10)
```

**基本写法：打印值**
`fmt.Println(<参数>)`
```go
// 打印并换行
fmt.Println("hello", "world")
```

**基本写法：扫描输入**
`fmt.Scan(&<变量>)`
```go
// 从标准输入读取
var name string
fmt.Scan(&name)
```

**基本写法：扫描格式化输入**
`fmt.Sscanf(<字符串>, <格式串>, &<变量>)`
```go
// 从字符串按格式读取
var name string
var age int
fmt.Sscanf("Go 15", "%s %d", &name, &age)
```

---

## fmt 格式化动词

**基本写法：通用格式化动词**
`%v / %+v / %#v`
```go
// 通用格式化
type User struct{ Name string; Age int }
u := User{"Go", 15}
fmt.Printf("%v\n", u)   // {Go 15}
fmt.Printf("%+v\n", u)  // {Name:Go Age:15}
fmt.Printf("%#v\n", u)  // main.User{Name:"Go", Age:15}
```

**基本写法：类型格式化**
`%T`
```go
// 输出值的 Go 类型
fmt.Printf("%T\n", 42) // int
```

**基本写法：整数格式化**
`%d / %b / %o / %x / %X`
```go
// 整数各种进制
fmt.Printf("%d\n", 255)  // 255
fmt.Printf("%b\n", 255)  // 11111111
fmt.Printf("%o\n", 255)  // 377
fmt.Printf("%x\n", 255)  // ff
```

**基本写法：浮点数格式化**
`%f / %e / %g`
```go
// 浮点数格式
fmt.Printf("%f\n", 3.14)   // 3.140000
fmt.Printf("%.2f\n", 3.14) // 3.14
fmt.Printf("%e\n", 3.14)   // 3.140000e+00
```

**基本写法：字符串格式化**
`%s / %q / %x`
```go
// 字符串格式
fmt.Printf("%s\n", "Go")   // Go
fmt.Printf("%q\n", "Go")   // "Go"
fmt.Printf("%x\n", "Go")   // 476f
```

**基本写法：宽度与对齐**
`%[宽度].[精度]<动词>`
```go
// 指定宽度和精度
fmt.Printf("|%5d|\n", 42)   // |   42|
fmt.Printf("|%-5d|\n", 42)  // |42   |
fmt.Printf("|%5.2f|\n", 3.14159) // | 3.14|
```

---

## strings 字符串操作

**基本写法：拼接字符串**
`strings.Join(<切片>, <分隔符>)`
```go
// 用分隔符拼接字符串切片
parts := []string{"a", "b", "c"}
s := strings.Join(parts, "-") // "a-b-c"
```

**基本写法：拆分字符串**
`strings.Split(<字符串>, <分隔符>)`
```go
// 按分隔符拆分
parts := strings.Split("a,b,c", ",")
```

**基本写法：拆分为字段**
`strings.Fields(<字符串>)`
```go
// 按空白拆分
fields := strings.Fields("  hello  world  ")
```

**基本写法：替换**
`strings.ReplaceAll(<字符串>, <旧>, <新>)`
```go
// 全部替换
s := strings.ReplaceAll("a-b-c", "-", "+")
```

**基本写法：替换指定次数**
`strings.Replace(<字符串>, <旧>, <新>, <次数>)`
```go
// 替换前 n 次
s := strings.Replace("aaa", "a", "b", 2) // "bba"
```

**基本写法：去除首尾字符**
`strings.Trim(<字符串>, <字符集>)`
```go
// 去除首尾指定字符
s := strings.Trim("##hello##", "#")
```

**基本写法：去除空白**
`strings.TrimSpace(<字符串>)`
```go
// 去除首尾空白
s := strings.TrimSpace("  hi  ")
```

**基本写法：查找子串**
`strings.Index(<字符串>, <子串>)`
```go
// 返回子串首次位置，未找到返回 -1
i := strings.Index("hello", "ll") // 2
```

**基本写法：统计子串**
`strings.Count(<字符串>, <子串>)`
```go
// 统计子串出现次数
n := strings.Count("aaa", "a") // 3
```

**基本写法：重复字符串**
`strings.Repeat(<字符串>, <次数>)`
```go
// 重复 n 次拼接
s := strings.Repeat("ab", 3) // "ababab"
```

**基本写法：高效构建字符串**
`var b strings.Builder`
```go
// 使用 Builder 高效拼接
var b strings.Builder
for i := 0; i < 1000; i++ {
    b.WriteString("item")
}
result := b.String()
```

---

## strconv 类型转换

**基本写法：int 转 string**
`strconv.Itoa(<整数>)`
```go
// 整数转字符串
s := strconv.Itoa(42)
```

**基本写法：string 转 int**
`strconv.Atoi(<字符串>)`
```go
// 字符串转整数
n, err := strconv.Atoi("42")
```

**基本写法：格式化整数**
`strconv.FormatInt(<值>, <进制>)`
```go
// 将整数转为指定进制字符串
s := strconv.FormatInt(255, 16) // "ff"
```

**基本写法：解析整数**
`strconv.ParseInt(<字符串>, <进制>, <位数>)`
```go
// 解析指定进制整数
n, err := strconv.ParseInt("ff", 16, 64)
```

**基本写法：格式化浮点数**
`strconv.FormatFloat(<值>, <格式>, <精度>, <位数>)`
```go
// 浮点数转字符串
s := strconv.FormatFloat(3.14, 'f', 2, 64) // "3.14"
```

**基本写法：解析浮点数**
`strconv.ParseFloat(<字符串>, <位数>)`
```go
// 字符串转浮点数
f, err := strconv.ParseFloat("3.14", 64)
```

**基本写法：解析布尔值**
`strconv.ParseBool(<字符串>)`
```go
// 字符串转布尔值
b, err := strconv.ParseBool("true")
```

**基本写法：追加格式化值**
`strconv.AppendInt(<切片>, <值>, <进制>)`
```go
// 追加格式化值到字节切片
buf := []byte("val=")
buf = strconv.AppendInt(buf, 42, 10)
```

---

## io 读写接口

**基本写法：Reader 接口**
`io.Reader`
```go
// 实现了 Read(p []byte) (n int, err error)
var r io.Reader = strings.NewReader("hello")
```

**基本写法：Writer 接口**
`io.Writer`
```go
// 实现了 Write(p []byte) (n int, err error)
var w io.Writer = os.Stdout
```

**基本写法：从 Reader 拷贝到 Writer**
`io.Copy(<writer>, <reader>)`
```go
// 数据流拷贝
n, err := io.Copy(os.Stdout, strings.NewReader("hello"))
```

**基本写法：读取全部**
`io.ReadAll(<reader>)`
```go
// 读取 Reader 全部内容
data, err := io.ReadAll(strings.NewReader("hello"))
```

**基本写法：写入字符串**
`io.WriteString(<writer>, <字符串>)`
```go
// 向 Writer 写入字符串
n, err := io.WriteString(os.Stdout, "hello\n")
```

**基本写法：组合读写**
`io.ReadWriter`
```go
// 同时实现 Read 和 Write 接口
var rw io.ReadWriter = os.Stdin
```

**基本写法：多 Reader 串联**
`io.MultiReader(<reader1>, <reader2>)`
```go
// 串联多个 Reader 依次读取
r := io.MultiReader(
    strings.NewReader("hello "),
    strings.NewReader("world"),
)
data, _ := io.ReadAll(r)
```

**基本写法：多 Writer 并联**
`io.MultiWriter(<writer1>, <writer2>)`
```go
// 并联多个 Writer 同时写入
w := io.MultiWriter(os.Stdout, os.Stderr)
io.WriteString(w, "hello")
```

**基本写法：限制读取量**
`io.LimitReader(<reader>, <字节数>)`
```go
// 限制最多读取 N 字节
r := io.LimitReader(file, 1024)
```

**基本写法：丢弃数据**
`io.Discard`
```go
// 丢弃所有写入数据的 Writer
io.Copy(io.Discard, largeReader)
```

**基本写法：EOF 判断**
`errors.Is(err, io.EOF)`
```go
// 判断是否读到末尾
_, err := r.Read(buf)
if errors.Is(err, io.EOF) {
    fmt.Println("已到末尾")
}
```

---

## bytes 字节操作

**基本写法：字节缓冲区**
`var buf bytes.Buffer`
```go
// 可变长字节缓冲区
var buf bytes.Buffer
buf.WriteString("hello")
buf.WriteByte('!')
result := buf.String()
```

**基本写法：字节切片拼接**
`bytes.Join(<切片>, <分隔符>)`
```go
// 拼接多个字节切片
parts := [][]byte{[]byte("a"), []byte("b")}
joined := bytes.Join(parts, []byte("-"))
```

**基本写法：字节切片比较**
`bytes.Equal(<a>, <b>)`
```go
// 比较两个字节切片是否相等
ok := bytes.Equal([]byte("a"), []byte("a"))
```

**基本写法：字节切片包含**
`bytes.Contains(<切片>, <子切片>)`
```go
// 判断是否包含子切片
ok := bytes.Contains([]byte("hello"), []byte("ell"))
```



<!-- ============ 文档分隔线：016-go/015-GoFileIO.md ============ -->

# Go 文件 I/O 操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件读写

**基本写法：打开文件**
`os.Open(<路径>)`
```go
// 以只读方式打开文件
file, err := os.Open("input.txt")
if err != nil {
    log.Fatal(err)
}
defer file.Close()
```

**基本写法：创建文件**
`os.Create(<路径>)`
```go
// 创建或截断文件，以读写方式打开
file, err := os.Create("output.txt")
defer file.Close()
```

**基本写法：以指定权限创建文件**
`os.OpenFile(<路径>, <标志>, <权限>)`
```go
// 追加模式打开
file, err := os.OpenFile("app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
defer file.Close()
```

**基本写法：读取整个文件**
`os.ReadFile(<路径>)`
```go
// 一次性读取文件全部内容
data, err := os.ReadFile("input.txt")
fmt.Println(string(data))
```

**基本写法：写入文件**
`os.WriteFile(<路径>, <数据>, <权限>)`
```go
// 一次性写入数据到文件
err := os.WriteFile("output.txt", []byte("hello"), 0644)
```

---

## 缓冲读写

**基本写法：缓冲写入**
`bufio.NewWriter(<writer>)`
```go
// 使用缓冲写入提高性能
file, _ := os.Create("output.txt")
defer file.Close()
writer := bufio.NewWriter(file)
writer.WriteString("hello\n")
writer.Flush()
```

**基本写法：缓冲读取**
`bufio.NewReader(<reader>)`
```go
// 使用缓冲读取
file, _ := os.Open("input.txt")
defer file.Close()
reader := bufio.NewReader(file)
line, _ := reader.ReadString('\n')
```

**基本写法：逐行扫描**
`bufio.NewScanner(<reader>)`
```go
// 逐行读取文件
file, _ := os.Open("input.txt")
defer file.Close()
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    line := scanner.Text()
    fmt.Println(line)
}
```

**基本写法：按单词扫描**
`scanner.Split(bufio.ScanWords)`
```go
// 按单词而非按行扫描
scanner := bufio.NewScanner(file)
scanner.Split(bufio.ScanWords)
for scanner.Scan() {
    word := scanner.Text()
}
```

**基本写法：逐行读取带错误检查**
`scanner.Err()`
```go
// 扫描结束后检查错误
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    process(scanner.Text())
}
if err := scanner.Err(); err != nil {
    log.Fatal(err)
}
```

---

## 文件信息

**基本写法：获取文件信息**
`os.Stat(<路径>)`
```go
// 获取文件元数据
info, err := os.Stat("file.txt")
if err != nil {
    if os.IsNotExist(err) {
        fmt.Println("文件不存在")
    }
}
```

**基本写法：判断文件是否存在**
`os.IsNotExist(err)`
```go
// 判断文件是否不存在
if _, err := os.Stat("file.txt"); os.IsNotExist(err) {
    fmt.Println("文件不存在")
}
```

**基本写法：获取文件大小**
`info.Size()`
```go
// 返回文件字节数
info, _ := os.Stat("file.txt")
size := info.Size()
```

**基本写法：判断是否为目录**
`info.IsDir()`
```go
// 判断是否为目录
info, _ := os.Stat("path")
if info.IsDir() {
    fmt.Println("是目录")
}
```

**基本写法：获取修改时间**
`info.ModTime()`
```go
// 返回文件最后修改时间
info, _ := os.Stat("file.txt")
modTime := info.ModTime()
```

---

## 目录操作

**基本写法：创建目录**
`os.Mkdir(<路径>, <权限>)`
```go
// 创建单个目录
os.Mkdir("newdir", 0755)
```

**基本写法：递归创建目录**
`os.MkdirAll(<路径>, <权限>)`
```go
// 递归创建多层目录
os.MkdirAll("a/b/c", 0755)
```

**基本写法：读取目录内容**
`os.ReadDir(<路径>)`
```go
// 读取目录下的所有条目
entries, err := os.ReadDir(".")
for _, entry := range entries {
    fmt.Println(entry.Name())
}
```

**基本写法：遍历目录树**
`filepath.WalkDir(<路径>, <函数>)`
```go
// 递归遍历目录树
filepath.WalkDir(".", func(path string, d fs.DirEntry, err error) error {
    if !d.IsDir() {
        fmt.Println(path)
    }
    return nil
})
```

**基本写法：删除文件**
`os.Remove(<路径>)`
```go
// 删除文件或空目录
os.Remove("file.txt")
```

**基本写法：递归删除**
`os.RemoveAll(<路径>)`
```go
// 递归删除目录及内容
os.RemoveAll("tempdir")
```

---

## 文件路径操作

**基本写法：拼接路径**
`filepath.Join(<路径1>, <路径2>)`
```go
// 跨平台路径拼接
path := filepath.Join("dir", "subdir", "file.txt")
```

**基本写法：获取文件扩展名**
`filepath.Ext(<路径>)`
```go
// 返回文件扩展名（含点）
ext := filepath.Ext("file.txt") // ".txt"
```

**基本写法：获取文件名**
`filepath.Base(<路径>)`
```go
// 返回路径最后一级
name := filepath.Base("/a/b/c.txt") // "c.txt"
```

**基本写法：获取目录**
`filepath.Dir(<路径>)`
```go
// 返回路径的目录部分
dir := filepath.Dir("/a/b/c.txt") // "/a/b"
```

**基本写法：绝对路径**
`filepath.Abs(<路径>)`
```go
// 转为绝对路径
abs, _ := filepath.Abs("file.txt")
```

**基本写法：通配匹配**
`filepath.Glob(<模式>)`
```go
// 匹配文件模式
matches, _ := filepath.Glob("*.go")
```

**基本写法：Go 1.24+ 目录受限文件系统**
`os.Root`
```go
// Go 1.24+ 限制在指定目录内操作
root, _ := os.OpenRoot("./data")
f, _ := root.Open("file.txt")
defer f.Close()
```

---

## 文件读写位置

**基本写法：设置读写偏移**
`file.Seek(<偏移>, <起始位置>)`
```go
// 移动文件指针到指定位置
file.Seek(10, io.SeekStart) // 从开头偏移 10
file.Seek(-5, io.SeekEnd)   // 从末尾回退 5
```

**基本写法：当前偏移量**
`file.Seek(0, io.SeekCurrent)`
```go
// 获取当前偏移量
pos, _ := file.Seek(0, io.SeekCurrent)
```

**基本写法：按位置读取**
`file.ReadAt(<缓冲>, <偏移>)`
```go
// 从指定位置读取
buf := make([]byte, 10)
n, _ := file.ReadAt(buf, 20)
```

**基本写法：按位置写入**
`file.WriteAt(<数据>, <偏移>)`
```go
// 在指定位置写入
file.WriteAt([]byte("hello"), 5)
```

---

## 临时文件

**基本写法：创建临时文件**
`os.CreateTemp(<目录>, <前缀>)`
```go
// 创建临时文件
f, _ := os.CreateTemp("", "prefix-*.txt")
defer f.Close()
defer os.Remove(f.Name())
```

**基本写法：创建临时目录**
`os.MkdirTemp(<目录>, <前缀>)`
```go
// 创建临时目录
dir, _ := os.MkdirTemp("", "mydir-")
defer os.RemoveAll(dir)
```



<!-- ============ 文档分隔线：016-go/016-GoHTTPServer.md ============ -->

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



<!-- ============ 文档分隔线：016-go/017-GoJSON.md ============ -->

# Go JSON 编解码

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 编码与解码

**基本写法：序列化为 JSON**
`json.Marshal(<值>)`
```go
// 将 Go 数据结构序列化为 JSON
data, err := json.Marshal(map[string]int{"a": 1, "b": 2})
fmt.Println(string(data))
```

**基本写法：带缩进序列化**
`json.MarshalIndent(<值>, <前缀>, <缩进>)`
```go
// 生成格式化的 JSON
data, _ := json.MarshalIndent(user, "", "  ")
fmt.Println(string(data))
```

**基本写法：反序列化 JSON**
`json.Unmarshal(<数据>, &<变量>)`
```go
// 将 JSON 解析为 Go 数据结构
var u User
err := json.Unmarshal([]byte(`{"name":"Go"}`), &u)
```

**基本写法：编码到 Writer**
`json.NewEncoder(<writer>).Encode(<值>)`
```go
// 直接编码输出到 Writer
json.NewEncoder(os.Stdout).Encode(user)
```

**基本写法：从 Reader 解码**
`json.NewDecoder(<reader>).Decode(&<变量>)`
```go
// 从 Reader 直接解码
var u User
json.NewDecoder(strings.NewReader(jsonStr)).Decode(&u)
```

---

## 结构体标签

**基本写法：字段映射标签**
`` `json:"<字段名>"` ``
```go
// 使用标签控制 JSON 字段名
type User struct {
    Name string `json:"name"`
    Age  int    `json:"age"`
}
```

**基本写法：忽略字段**
`` `json:"-"` ``
```go
// 序列化时忽略该字段
type User struct {
    Password string `json:"-"`
    Name     string `json:"name"`
}
```

**基本写法：omitempty 省略空值**
`` `json:"<字段名>,omitempty"` ``
```go
// 字段为零值时不输出
type User struct {
    Name  string `json:"name"`
    Email string `json:"email,omitempty"`
}
```

**基本写法：字符串化字段**
`` `json:"<字段名>,string"` ``
```go
// 将数值序列化为字符串
type Config struct {
    Port int `json:"port,string"`
}
```

---

## 流式处理

**基本写法：流式编码多对象**
`enc := json.NewEncoder(<writer>)`
```go
// 连续编码多个 JSON 对象
enc := json.NewEncoder(os.Stdout)
enc.Encode(obj1)
enc.Encode(obj2)
```

**基本写法：流式解码多对象**
`dec := json.NewDecoder(<reader>)`
```go
// 循环解码多个 JSON 对象
dec := json.NewDecoder(file)
for dec.More() {
    var u User
    dec.Decode(&u)
    fmt.Println(u)
}
```

**基本写法：解码 JSON 数组流**
`dec.Token()`
```go
// 逐个解码数组元素
dec := json.NewDecoder(file)
dec.Token() // 读取开始的 [
for dec.More() {
    var item Item
    dec.Decode(&item)
}
dec.Token() // 读取结束的 ]
```

---

## 动态 JSON

**基本写法：解析到 map**
`var m map[string]interface{}`
```go
// 不确定结构时解析到 map
var m map[string]interface{}
json.Unmarshal(data, &m)
name := m["name"].(string)
```

**基本写法：解析到 interface{}**
`var v interface{}`
```go
// 完全动态解析
var v interface{}
json.Unmarshal(data, &v)
m := v.(map[string]interface{})
```

**基本写法：类型断言访问**
`v.(<类型>)`
```go
// 动态访问 JSON 字段
m := v.(map[string]interface{})
for key, val := range m {
    switch t := val.(type) {
    case string:
        fmt.Println(key, "is string:", t)
    case float64:
        fmt.Println(key, "is number:", t)
    }
}
```

---

## json.RawMessage

**基本写法：延迟解码**
`json.RawMessage`
```go
// 保留原始 JSON 字节，延迟解析
type Envelope struct {
    Type string          `json:"type"`
    Data json.RawMessage `json:"data"`
}
var env Envelope
json.Unmarshal(data, &env)
// 根据 Type 决定如何解析 Data
```

**基本写法：合并 RawMessage**
`json.RawMessage(<字节>)`
```go
// 构造原始 JSON 片段
raw := json.RawMessage(`{"key":"value"}`)
result, _ := json.Marshal(struct {
    Wrap json.RawMessage `json:"wrap"`
}{Wrap: raw})
```

---

## 自定义序列化

**换行写法：实现 MarshalJSON**
`func (<类型>) MarshalJSON() ([]byte, error)`
```go
// 自定义序列化逻辑
type Temperature float64
func (t Temperature) MarshalJSON() ([]byte, error) {
    return json.Marshal(fmt.Sprintf("%.1fC", t))
}
```

**换行写法：实现 UnmarshalJSON**
`func (<接收者>) UnmarshalJSON([]byte) error`
```go
// 自定义反序列化逻辑
func (t *Temperature) UnmarshalJSON(data []byte) error {
    var s string
    if err := json.Unmarshal(data, &s); err != nil {
        return err
    }
    val, _ := strconv.ParseFloat(strings.TrimSuffix(s, "C"), 64)
    *t = Temperature(val)
    return nil
}
```

---

## 错误处理

**基本写法：获取字段错误**
`json.UnmarshalTypeError`
```go
// 捕获类型不匹配错误
var u User
err := json.Unmarshal(data, &u)
if typeErr, ok := err.(*json.UnmarshalTypeError); ok {
    fmt.Printf("字段 %s 类型错误\n", typeErr.Field)
}
```

**基本写法：UnknownFields 检测**
`dec.DisallowUnknownFields()`
```go
// 禁止 JSON 中出现未知字段
dec := json.NewDecoder(r)
dec.DisallowUnknownFields()
var u User
err := dec.Decode(&u)
```

---

## Go 1.24+ JSON 增强

**基本写法：jsontext 严格 JSON 处理**
`import "encoding/json/v2"`
```go
// Go 1.24+ 实验性 JSON v2 API（需启用实验特性）
// 提供更严格的类型系统和更高效的编解码
var js jsonv2.Value
js.Unmarshal(data)
```

**基本写法：json v2 序列化**
`jsonv2.Marshal(<值>)`
```go
// Go 1.24+ 实验性 v2 序列化
// data, err := jsonv2.Marshal(user)
```



<!-- ============ 文档分隔线：016-go/018-GoModule.md ============ -->

# Go Modules

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块初始化

**基本写法：初始化模块**
`go mod init <模块路径>`
```go
// 创建 go.mod 文件
// go mod init github.com/myname/myproject
```

**基本写法：go.mod 文件结构**
`module <路径>`
```go
// go.mod 文件基本结构
// module github.com/myname/myproject
// go 1.22
// require (
//     github.com/gin-gonic/gin v1.9.1
// )
```

---

## 依赖管理

**基本写法：添加依赖**
`go get <包路径>`
```go
// 下载并添加依赖
// go get github.com/gin-gonic/gin
```

**基本写法：添加指定版本**
`go get <包路径>@<版本>`
```go
// 指定版本添加依赖
// go get github.com/gin-gonic/gin@v1.9.1
```

**基本写法：更新依赖**
`go get -u <包路径>`
```go
// 更新到最新版本
// go get -u github.com/gin-gonic/gin
```

**基本写法：更新所有依赖**
`go get -u ./...`
```go
// 更新项目中所有依赖
// go get -u ./...
```

**基本写法：移除未使用依赖**
`go mod tidy`
```go
// 清理 go.mod 中未使用的依赖
// go mod tidy
```

**基本写法：降级依赖**
`go get <包路径>@<较低版本>`
```go
// 降级到指定版本
// go get github.com/gin-gonic/gin@v1.8.0
```

**基本写法：查看可用版本**
`go list -m -versions <包路径>`
```go
// 列出模块所有可用版本
// go list -m -versions github.com/gin-gonic/gin
```

**基本写法：查看依赖图**
`go mod graph`
```go
// 输出依赖关系图
// go mod graph
```

---

## 依赖下载与缓存

**基本写法：下载依赖到本地**
`go mod download`
```go
// 下载所有依赖到本地缓存
// go mod download
```

**基本写法：下载指定依赖**
`go mod download <包路径>`
```go
// 下载指定模块
// go mod download github.com/gin-gonic/gin
```

**基本写法：将依赖复制到 vendor**
`go mod vendor`
```go
// 创建 vendor 目录存放依赖
// go mod vendor
```

**基本写法：使用 vendor 构建**
`go build -mod=vendor`
```go
// 使用 vendor 目录中的依赖
// go build -mod=vendor
```

---

## 模块查询

**基本写法：列出所有依赖**
`go list -m all`
```go
// 列出当前模块所有依赖
// go list -m all
```

**基本写法：查看依赖信息**
`go list -m -json <包路径>`
```go
// 以 JSON 格式查看模块信息
// go list -m -json github.com/gin-gonic/gin
```

**基本写法：查看模块路径**
`go list -m`
```go
// 输出当前模块路径
// go list -m
```

**基本写法：查看已更改的配置**
`go env -changed`
```go
// Go 1.23+ 仅显示与默认值不同的环境变量
// go env -changed
```

---

## 模块替换与排除

**基本写法：替换依赖**
`replace <原路径> => <新路径>`
```go
// 在 go.mod 中替换依赖源
// replace github.com/old/lib => github.com/new/lib v1.2.0
```

**基本写法：替换为本地路径**
`replace <路径> => <本地目录>`
```go
// 替换为本地开发版本
// replace github.com/myname/lib => ../lib
```

**基本写法：排除特定版本**
`exclude <包路径> <版本>`
```go
// 排除有问题的版本
// exclude github.com/some/pkg v1.5.0
```

**基本写法：撤回版本**
`retract <版本>`
```go
// 在 go.mod 中声明撤回有问题的版本
// retract v1.2.0
// retract [v1.1.0, v1.1.5]
```

---

## Go 1.24+ 工具依赖

**基本写法：添加工具依赖**
`go get -tool <工具路径>`
```go
// Go 1.24+ 使用 tool 指令管理工具
// go get -tool golang.org/x/tools/cmd/stringer
```

**基本写法：go.mod 中的 tool 指令**
`tool ( <工具路径> )`
```go
// go.mod 中声明工具依赖
// tool (
//     github.com/golangci/golangci-lint/cmd/golangci-lint
//     golang.org/x/tools/cmd/stringer
// )
```

**基本写法：运行工具**
`go tool <工具名>`
```go
// 运行声明的工具
// go tool stringer -type=Color
```

**基本写法：安装所有工具**
`go install tool`
```go
// 安装 go.mod 中所有工具到 GOBIN
// go install tool
```

**基本写法：更新所有工具**
`go get tool`
```go
// 更新所有工具到最新版本
// go get tool
```

---

## 版本控制与构建

**基本写法：嵌入版本信息**
`go build -buildvcs`
```go
// Go 1.24+ 默认嵌入 VCS 版本信息
// go build 默认将版本控制信息嵌入二进制
```

**基本写法：禁用版本信息**
`go build -buildvcs=false`
```go
// 不嵌入版本控制信息
// go build -buildvcs=false
```

**基本写法：JSON 构建输出**
`go build -json`
```go
// Go 1.24+ 以 JSON 格式输出构建结果
// go build -json
```

---

## 工具链管理

**基本写法：指定工具链版本**
`//go:toolchain <版本>`
```go
// 在 go.mod 中指定工具链
// go 1.24.0
// toolchain go1.24.3
```

**基本写法：切换工具链**
`go toolchain <命令>`
```go
// 切换 Go 工具链版本
// go toolchain go1.24.0
```

**基本写法：设置工具链策略**
`GOTOOLCHAIN=<值>`
```go
// 环境变量控制工具链行为
// GOTOOLCHAIN=auto  // 自动选择（默认）
// GOTOOLCHAIN=local // 强制使用本地版本
```

---

## 私有模块

**基本写法：设置私有仓库**
`GOPRIVATE=<域名>`
```go
// 跳过代理和校验的私有模块
// GOPRIVATE=git.mycorp.com,*.mycorp.com
```

**基本写法：Go 1.24+ GOAUTH 认证**
`GOAUTH=<认证方式>`
```go
// Go 1.24+ 灵活的私有模块认证
// GOAUTH=netrc:~/.netrc
```

**基本写法：设置模块代理**
`GOPROXY=<代理地址>`
```go
// 设置模块代理服务器
// GOPROXY=https://goproxy.cn,direct
```

**基本写法：设置校验和服务器**
`GOSUMDB=<地址>`
```go
// 设置校验和数据库
// GOSUMDB=sum.golang.org
```

---

## Workspace 工作区

**基本写法：初始化工作区**
`go work init <模块路径>`
```go
// 创建 go.work 文件管理多模块
// go work init ./module1 ./module2
```

**基本写法：添加模块到工作区**
`go work use <模块路径>`
```go
// 将模块添加到工作区
// go work use ./newmodule
```

**基本写法：工作区中同步依赖**
`go work sync`
```go
// 同步工作区依赖到各模块
// go work sync
```



<!-- ============ 文档分隔线：016-go/020-GoTime.md ============ -->

# Go time 包 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 当前时间

**基本写法：获取当前时间**
`time.Now() time.Time`
```go
// 返回当前本地时间
now := time.Now()
```

**基本写法：获取当前 Unix 时间戳**
`time.Now().Unix() int64`
```go
// 返回自 1970-01-01 起的秒数
sec := time.Now().Unix()
```

**基本写法：获取纳秒时间戳**
`time.Now().UnixNano() int64`
```go
// 返回纳秒级时间戳，用于高精度计时
nano := time.Now().UnixNano()
```

**基本写法：获取 Unix 毫秒**
`time.Now().UnixMilli() int64`
```go
// 返回毫秒时间戳（Go 1.17+）
ms := time.Now().UnixMilli()
```

---

## 时间创建

**基本写法：构造指定时间**
`time.Date(<年>, <月>, <日>, <时>, <分>, <秒>, <纳秒>, <时区>) time.Time`
```go
// 构造 2024 年 1 月 1 日 0 点 UTC 时间
t := time.Date(2024, time.January, 1, 0, 0, 0, 0, time.UTC)
```

**基本写法：从 Unix 秒创建**
`time.Unix(<秒>, <纳秒>) time.Time`
```go
// 从时间戳还原时间
t := time.Unix(1700000000, 0)
```

**基本写法：解析字符串为时间**
`time.Parse(<布局>, <字符串>) (time.Time, error)`
```go
// 按 RFC3339 布局解析
t, err := time.Parse("2006-01-02 15:04:05", "2024-01-01 12:00:00")
```

**基本写法：按本地时区解析**
`time.ParseInLocation(<布局>, <字符串>, <时区>) (time.Time, error)`
```go
// 按上海时区解析字符串
loc, _ := time.LoadLocation("Asia/Shanghai")
t, _ := time.ParseInLocation("2006-01-02 15:04:05", "2024-01-01 12:00:00", loc)
```

---

## 格式化布局

**基本写法：格式化为字符串**
`<时间>.Format(<布局>) string`
```go
// Go 使用参考时间 2006-01-02 15:04:05 作为布局
s := time.Now().Format("2006-01-02 15:04:05")
```

**基本写法：RFC3339 格式**
`<时间>.Format(time.RFC3339) string`
```go
// 输出 2024-01-01T12:00:00Z 格式
s := time.Now().Format(time.RFC3339)
```

**基本写法：自定义布局**
`<时间>.Format("<布局串>") string`
```go
// 常用占位：年 2006 月 01 日 02 时 15 分 04 秒 05
s := time.Now().Format("2006/01/02 15:04")
```

**基本写法：格式化为 RFC3339Nano**
`<时间>.Format(time.RFC3339Nano) string`
```go
// 带纳秒精度的 ISO 格式
s := time.Now().Format(time.RFC3339Nano)
```

---

## 时间运算

**基本写法：增加时间**
`<时间>.Add(<时长>) time.Time`
```go
// 当前时间加 2 小时
later := time.Now().Add(2 * time.Hour)
```

**基本写法：增加年月日**
`<时间>.AddDate(<年>, <月>, <日>) time.Time`
```go
// 当前时间加 1 年 2 个月 3 天
t := time.Now().AddDate(1, 2, 3)
```

**基本写法：计算时间差**
`<时间>.Sub(<另一时间>) time.Duration`
```go
// 计算两个时间间隔
diff := end.Sub(start)
```

**基本写法：比较时间先后**
`<时间>.Before(<另一时间>) bool`
```go
// 判断 t1 是否早于 t2
if t1.Before(t2) { }
```

**基本写法：比较时间相等**
`<时间>.Equal(<另一时间>) bool`
```go
// 判断两时间是否相等（推荐用 Equal 而非 ==）
if t1.Equal(t2) { }
```

**基本写法：判断之后**
`<时间>.After(<另一时间>) bool`
```go
// 判断 t1 是否晚于 t2
if t1.After(t2) { }
```

---

## 时长 Duration

**基本写法：定义时长**
`<数值> * time.<单位>`
```go
// 常见单位：ns、us、ms、s、m、h
d := 500 * time.Millisecond
```

**基本写法：时长转秒**
`<时长>.Seconds() float64`
```go
// 将时长转为浮点秒
sec := d.Seconds()
```

**基本写法：时长转字符串**
`<时长>.String() string`
```go
// 输出如 500ms、2h30m 的可读形式
s := d.String()
```

**基本写法：解析时长字符串**
`time.ParseDuration(<字符串>) (time.Duration, error)`
```go
// 解析 1h30m 形式时长
d, err := time.ParseDuration("1h30m")
```

---

## 定时器

**基本写法：一次性定时器**
`time.NewTimer(<时长>) *time.Timer`
```go
// 2 秒后触发
timer := time.NewTimer(2 * time.Second)
<-timer.C
```

**基本写法：重置定时器**
`<timer>.Reset(<时长>) bool`
```go
// 重新计时（Go 1.23+ 仅在未停止且未触发时返回 true）
timer.Reset(3 * time.Second)
```

**基本写法：停止定时器**
`<timer>.Stop() bool`
```go
// 停止定时器，返回是否成功停止
timer.Stop()
```

**基本写法：周期触发**
`time.NewTicker(<时长>) *time.Ticker`
```go
// 每 1 秒触发一次
ticker := time.NewTicker(time.Second)
defer ticker.Stop()
for t := range ticker.C {
    fmt.Println(t)
}
```

**基本写法：阻塞等待**
`time.Sleep(<时长>)`
```go
// 暂停当前 goroutine 100 毫秒
time.Sleep(100 * time.Millisecond)
```

**基本写法：After 延迟通道**
`time.After(<时长>) <-chan time.Time`
```go
// 返回到时发送一次的通道
select {
case <-time.After(time.Second):
}
```

---

## 时区

**基本写法：获取时区**
`time.LoadLocation(<名称>) (*time.Location, error)`
```go
// 加载上海时区
loc, err := time.LoadLocation("Asia/Shanghai")
```

**基本写法：UTC 时区**
`time.UTC *time.Location`
```go
// 使用 UTC 时区
t := time.Now().In(time.UTC)
```

**基本写法：转换时区**
`<时间>.In(<时区>) time.Time`
```go
// 将时间转换为指定时区表示
t := time.Now().In(loc)
```

**基本写法：固定偏移时区**
`time.FixedZone(<名称>, <秒偏移>) *time.Location`
```go
// 东八区固定偏移
loc := time.FixedZone("CST", 8*3600)
```

---

## 时间戳与组件

**基本写法：获取年月日**
`<时间>.Date() (<年>, <月>, <日>)`
```go
// 返回年月日三个值
y, m, d := time.Now().Date()
```

**基本写法：获取时分秒**
`<时间>.Clock() (<时>, <分>, <秒>)`
```go
// 返回时分秒三个值
h, mi, s := time.Now().Clock()
```

**基本写法：获取星期几**
`<时间>.Weekday() time.Weekday`
```go
// 返回星期，0 是 Sunday
w := time.Now().Weekday()
```

**基本写法：获取年内天数**
`<时间>.YearDay() int`
```go
// 返回当年第几天（1-366）
day := time.Now().YearDay()
```

---

## 性能计时

**基本写法：高精度计时**
`time.Since(<起始时间>) time.Duration`
```go
// 测量代码执行耗时
start := time.Now()
doWork()
fmt.Println(time.Since(start))
```

**基本写法：单调时钟计时**
`time.Now() time.Time`
```go
// Now 内含单调时钟读数，Sub/Before/After 仅比较单调部分
// 不受系统时间回拨影响
```



<!-- ============ 文档分隔线：016-go/021-GoRegexp.md ============ -->

# Go regexp 包 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 编译正则

**基本写法：编译正则**
`regexp.Compile(<表达式>) (*regexp.Regexp, error)`
```go
// 编译正则，错误时返回 error
re, err := regexp.Compile(`\d+`)
```

**基本写法：编译或 panic**
`regexp.MustCompile(<表达式>) *regexp.Regexp`
```go
// 表达式确定合法时使用，错误直接 panic
re := regexp.MustCompile(`^[a-z]+$`)
```

**基本写法：POSIX 最左最长匹配**
`regexp.CompilePOSIX(<表达式>) (*regexp.Regexp, error)`
```go
// 使用 POSIX 语义，匹配最左最长子串
re, _ := regexp.CompilePOSIX(`a|ab`)
```

**基本写法：编译并校验 UTF-8**
`regexp.Compile(<表达式>)`
```go
// regexp 默认要求表达式与目标均为合法 UTF-8
// 语法：. * + ? () [] {} ^ $ | \d \w \s
```

---

## 正则语法速查

**基本写法：常用字符类**
`\d \w \s \D \W \S`
```go
// \d 数字 \w 单词字符 \s 空白
// 大写为取反：\D 非数字
re := regexp.MustCompile(`\w+@\w+`)
```

**基本写法：重复次数**
`<字符>{<n>,<m>} 或 <字符>* + ?`
```go
// * 0 次或多次  + 1 次或多次  ? 0 或 1 次
// {3} 恰好 3 次  {2,5} 2 到 5 次
re := regexp.MustCompile(`\d{2,4}`)
```

**基本写法：分组与捕获**
`(<子表达式>)`
```go
// 捕获分组，后续可用索引引用
re := regexp.MustCompile(`(\d+)-(\d+)`)
```

**基本写法：非捕获分组**
`(?:<子表达式>)`
```go
// 仅分组不捕获
re := regexp.MustCompile(`(?:ab)+`)
```

**基本写法：命名捕获**
`(?P<名称><子表达式>)`
```go
// 命名捕获组，Go 采用 RE2 的 (?P<name>) 语法
re := regexp.MustCompile(`(?P<year>\d{4})-(?P<month>\d{2})`)
```

**基本写法：字符集合**
`[<字符集>] [^<字符集>]`
```go
// [a-z] 小写字母  [^0-9] 非数字
re := regexp.MustCompile(`[A-Za-z0-9_]+`)
```

---

## 匹配判断

**基本写法：判断是否匹配**
`<re>.MatchString(<字符串>) bool`
```go
// 返回是否包含匹配子串
if re.MatchString("abc123") { }
```

**基本写法：匹配字节切片**
`<re>.Match(<字节>) bool`
```go
// 对 []byte 进行匹配
if re.Match([]byte("abc123")) { }
```

**基本写法：匹配 Reader**
`<re>.MatchReader(<reader>) bool`
```go
// 对 io.RuneReader 进行匹配
if re.MatchReader(strings.NewReader("abc123")) { }
```

---

## 查找结果

**基本写法：查找首个匹配**
`<re>.FindString(<字符串>) string`
```go
// 返回第一个匹配子串，无匹配返回空串
s := re.FindString("phone: 13800000000")
```

**基本写法：查找首个匹配及位置**
`<re>.FindStringIndex(<字符串>) []int`
```go
// 返回 [起始, 结束] 索引，无匹配返回 nil
loc := re.FindStringIndex("a1b2")
```

**基本写法：查找所有匹配**
`<re>.FindAllString(<字符串>, <数量>) []string`
```go
// 返回所有匹配，-1 表示全部
list := re.FindAllString("a1b2c3", -1)
```

**基本写法：查找所有位置**
`<re>.FindAllStringIndex(<字符串>, <数量>) [][]int`
```go
// 返回所有匹配的 [起, 止] 索引切片
locs := re.FindAllStringIndex("a1b2c3", -1)
```

**基本写法：查找所有子匹配**
`<re>.FindAllStringSubmatch(<字符串>, <数量>) [][]string`
```go
// 返回每条匹配的分组切片
subs := re.FindAllStringSubmatch("2024-01 2025-02", -1)
```

---

## 子匹配与分组

**基本写法：查找首个子匹配**
`<re>.FindStringSubmatch(<字符串>) []string`
```go
// 返回 [全匹配, 分组1, 分组2, ...]
sub := re.FindStringSubmatch("2024-01")
// sub[0]="2024-01" sub[1]="2024" sub[2]="01"
```

**基本写法：命名捕获取值**
`<re>.SubexpNames() []string`
```go
// 返回分组名列表，结合 Submatch 使用
re := regexp.MustCompile(`(?P<y>\d{4})`)
names := re.SubexpNames()
m := re.FindStringSubmatch("2024")
val := m[1]
```

---

## 替换

**基本写法：替换首个匹配**
`<re>.ReplaceAllString(<源串>, <替换串>) string`
```go
// 将所有匹配替换为指定字符串
out := re.ReplaceAllString("a1b2", "X")
```

**基本写法：引用捕获分组**
`<re>.ReplaceAllString(<源串>, "${<名称>}")`
```go
// 用命名分组内容替换
re := regexp.MustCompile(`(\d+)-(\d+)`)
out := re.ReplaceAllString("2024-01", "${2}/${1}")
```

**基本写法：函数替换**
`<re>.ReplaceAllStringFunc(<源串>, <函数>) string`
```go
// 对每个匹配调用函数决定替换值
out := re.ReplaceAllStringFunc("a1b2", func(s string) string {
    return "[" + s + "]"
})
```

**基本写法：替换字节切片**
`<re>.ReplaceAll(<源字节>, <替换字节>) []byte`
```go
// 对 []byte 进行替换
out := re.ReplaceAll([]byte("a1b2"), []byte("X"))
```

---

## 分割与拆分

**基本写法：按正则分割**
`<re>.Split(<字符串>, <数量>) []string`
```go
// 按匹配分割字符串，-1 表示全部分割
parts := re.Split("a,b;c:d", -1)
```

**基本写法：限定分割次数**
`<re>.Split(<字符串>, <n>) []string`
```go
// n>0 时最多分割 n 次，返回最多 n+1 段
parts := regexp.MustCompile(`,`).Split("a,b,c,d", 2)
```

---

## 字符串提取辅助

**基本写法：提取数字**
`regexp.MustCompile(`\d+`).FindString(<字符串>)`
```go
// 提取字符串中第一段数字
num := regexp.MustCompile(`\d+`).FindString("id: 42, ok")
```

**基本写法：提取邮箱**
`regexp.MustCompile(`[\w.]+@[\w.]+`).FindString(<字符串>)`
```go
// 简易邮箱提取
email := regexp.MustCompile(`[\w.]+@[\w.]+`).FindString("contact: a@b.com")
```

---

## 高级用法

**基本写法：转义元字符**
`regexp.QuoteMeta(<字符串>) string`
```go
// 将字符串中的正则元字符转义，用于字面匹配
lit := regexp.QuoteMeta("1+1=2")
```

**基本写法：展开捕获变量**
`<re>.ExpandString(<dst>, <模板>, <源串>, <匹配>) []byte`
```go
// 按 $name 或 ${name} 模板展开捕获内容
re := regexp.MustCompile(`(?P<x>\d+)`)
m := re.FindStringSubmatchIndex("42")
out := re.ExpandString(nil, "$x", "42", m)
```

**基本写法：字面量前缀**
`<re>.LiteralPrefix() (前缀 string, 完整 bool)`
```go
// 返回正则的固定字面前缀，用于优化预过滤
re := regexp.MustCompile(`/api/v\d+/user`)
prefix, complete := re.LiteralPrefix()
```

---

## RE2 限制说明

**基本写法：不支持回溯**
`regexp 使用 RE2 引擎`
```go
// RE2 不支持反向引用 \1、不支持环视 (?=...)
// 保证线性时间，避免灾难性回溯
// 需要回溯特性请使用第三方库 regexp2
```

**基本写法：贪婪与懒惰**
`<量词>? 切换为懒惰匹配`
```go
// 默认贪婪，加 ? 变懒惰
greedy := regexp.MustCompile(`a.*b`)    // 贪婪
lazy := regexp.MustCompile(`a.*?b`)     // 懒惰
```



<!-- ============ 文档分隔线：016-go/022-GoPprof.md ============ -->

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



<!-- ============ 文档分隔线：016-go/023-GoNewFeatures.md ============ -->

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



<!-- ============ 文档分隔线：016-go/024-GoCommandToolchain.md ============ -->

# Go 命令工具链

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础命令

**基本写法：查看版本**
`go version`
```go
// 输出 Go 版本与平台信息
// go version
```

---

**基本写法：查看环境变量**
`go env [变量名]`
```go
// 查看全部或指定环境变量
// go env GOPATH
// go env GOOS GOARCH
```

---

**基本写法：设置环境变量**
`go env -w <变量>=<值>`
```go
// 持久化写入 GOENV 配置文件
// go env -w GOPROXY=https://goproxy.cn,direct
// go env -w GO111MODULE=on
```

---

## 构建与运行

**基本写法：运行程序**
`go run <文件或包>`
```go
// 直接编译并执行，不产生可执行文件
// go run main.go
// go run .
```

---

**基本写法：编译二进制**
`go build [包路径]`
```go
// 编译生成可执行文件
// go build
// go build -o myapp
// go build ./cmd/server
```

---

**基本写法：指定输出名编译**
`go build -o <输出名> <包>`
```go
// 自定义输出文件名
// go build -o bin/app ./cmd/app
```

---

**基本写法：指定目标平台交叉编译**
`GOOS=<系统> GOARCH=<架构> go build`
```go
// 交叉编译，无需额外工具链
// GOOS=linux GOARCH=amd64 go build -o app_linux
// GOOS=windows GOARCH=arm64 go build
```

---

**基本写法：编译并嵌入版本信息**
`go build -ldflags "<参数>"`
```go
// 通过 -ldflags 注入变量值
// go build -ldflags "-X main.Version=1.0.0 -s -w"
// -s -w 去除调试符号与 DWARF 信息减小体积
```

---

**基本写法：安装到 GOBIN**
`go install <包>`
```go
// 编译并安装到 GOBIN/GOPATH/bin
// go install
// go install golang.org/x/tools/cmd/goimports@latest
```

---

## 测试

**基本写法：运行测试**
`go test [包路径]`
```go
// 运行当前包测试
// go test
// go test ./...
```

---

**基本写法：递归测试所有包**
`go test ./...`
```go
// 测试当前模块下所有包
// go test ./...
```

---

**基本写法：显示详细输出**
`go test -v`
```go
// 打印每个用例的执行详情
// go test -v ./...
```

---

**基本写法：运行指定测试**
`go test -run <正则>`
```go
// 按正则匹配用例名执行
// go test -run TestSum
// go test -run TestUser/Delete
```

---

**基本写法：生成覆盖率报告**
`go test -cover`
```go
// 输出覆盖率百分比
// go test -cover ./...
```

---

**基本写法：生成覆盖率详情文件**
`go test -coverprofile=<文件>`
```go
// 生成覆盖率文件，配合 go tool cover 查看
// go test -coverprofile=cover.out ./...
// go tool cover -html=cover.out -o cover.html
```

---

**基本写法：基准测试**
`go test -bench=<正则>`
```go
// 运行 Benchmark 前缀函数
// go test -bench=. -benchmem
```

---

**基本写法：竞态检测**
`go test -race`
```go
// 启用竞态检测器
// go test -race ./...
```

---

## 模块管理

**基本写法：初始化模块**
`go mod init <模块路径>`
```go
// 创建 go.mod 文件
// go mod init github.com/myname/myproject
```

---

**基本写法：整理依赖**
`go mod tidy`
```go
// 添加缺失依赖、移除未用依赖
// go mod tidy
```

---

**基本写法：下载依赖到本地缓存**
`go mod download`
```go
// 下载依赖到 GOMODCACHE，不安装
// go mod download
```

---

**基本写法：添加依赖**
`go get <包路径>`
```go
// 下载并添加到 go.mod
// go get github.com/gin-gonic/gin
```

---

**基本写法：添加指定版本**
`go get <包路径>@<版本>`
```go
// 指定版本、提交或标签
// go get github.com/gin-gonic/gin@v1.9.1
// go get github.com/x/y@latest
```

---

**基本写法：升级依赖**
`go get -u <包路径>`
```go
// 升级到最新次版本及依赖
// go get -u github.com/gin-gonic/gin
```

---

**基本写法：移除依赖**
`go get <包路径>@none`
```go
// 移除指定依赖
// go get github.com/old/pkg@none
```

---

**基本写法：查看依赖图**
`go mod graph`
```go
// 打印模块依赖关系图
// go mod graph
```

---

**基本写法：将依赖复制到 vendor**
`go mod vendor`
```go
// 创建 vendor 目录存放依赖源码
// go mod vendor
```

---

**基本写法：校验依赖完整性**
`go mod verify`
```go
// 校验下载依赖的哈希
// go mod verify
```

---

## 代码质量

**基本写法：格式化代码**
`go fmt [包路径]`
```go
// 按标准格式重写源码
// go fmt ./...
```

---

**基本写法：gofmt 检查差异**
`gofmt -l <目录>`
```go
// 列出格式不符的文件，不修改
// gofmt -l .
```

---

**基本写法：静态检查**
`go vet [包路径]`
```go
// 运行内置可疑构造检查
// go vet ./...
```

---

**基本写法：清理构建缓存**
`go clean`
```go
// 清理构建产生的对象文件
// go clean
```

---

**基本写法：清理缓存目录**
`go clean -cache`
```go
// 清理 go build 缓存
// go clean -cache
// go clean -modcache  // 清理模块下载缓存
// go clean -testcache  // 清理测试结果缓存
```

---

## 文档与依赖查看

**基本写法：查看文档**
`go doc [包路径]`
```go
// 在终端查看包文档
// go doc fmt.Println
// go doc github.com/gin-gonic/gin
```

---

**基本写法：列出包及其依赖**
`go list [包路径]`
```go
// 列出当前模块的包
// go list ./...
// go list -m all  // 列出所有依赖模块
```

---

**基本写法：查看包导入路径**
`go list -f <模板> <包>`
```go
// 自定义输出格式
// go list -f "{{.ImportPath}} {{.Imports}}" ./...
```

---

**基本写法：启动本地文档服务**
`go doc -all`
```go
// 浏览器查看完整文档
// godoc -http=:6060
```

---
