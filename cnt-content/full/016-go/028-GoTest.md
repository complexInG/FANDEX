---
order: 68
title: Go与测试
module: go
category: Go
difficulty: intermediate
description: Go测试框架与基准测试
author: fanquanpp
updated: '2026-08-01'
related:
  - go/Go与Redis
  - go/Go与消息队列
  - go/Go与Fuzzing
  - go/Go与性能分析
prerequisites:
  - go/概述与环境配置
---

# Go testing 包

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

### 表驱动测试

表驱动测试是 Go 中最推荐的测试模式，将测试用例组织为结构体切片，便于维护和扩展。

```go
func TestParse(t *testing.T) {
    // 定义测试用例表
    tests := []struct {
        name     string
        input    string
        expected string
    }{
        {"小写转大写", "hello", "HELLO"},
        {"空字符串", "", ""},
        {"已是大写", "WORLD", "WORLD"},
        {"混合大小写", "HeLLo", "HELLO"},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := strings.ToUpper(tt.input)
            if got != tt.expected {
                t.Errorf("ToUpper(%q) = %q, want %q", tt.input, got, tt.expected)
            }
        })
    }
}
```

### 并行测试

使用 `t.Parallel()` 标记可并行执行的测试：

```go
func TestParallel(t *testing.T) {
    tests := []struct {
        name  string
        input int
        want  int
    }{
        {"正数", 5, 25},
        {"负数", -3, 9},
        {"零", 0, 0},
    }

    for _, tt := range tests {
        tt := tt // 捕获变量
        t.Run(tt.name, func(t *testing.T) {
            t.Parallel() // 标记为并行
            got := tt.input * tt.input
            if got != tt.want {
                t.Errorf("got %d, want %d", got, tt.want)
            }
        })
    }
}
```

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

### 示例测试

示例测试既作为文档，也作为可执行的测试：

```go
// 示例会出现在 godoc 文档中
func ExampleGreet() {
    result := Greet("Alice")
    fmt.Println(result)
    // Output: Hello, Alice
}

// 带后缀的示例，对应具体方法
func ExampleUser_Name() {
    u := User{Name: "Bob"}
    fmt.Println(u.Name)
    // Output: Bob
}
```

## 概述

Go 语言内置了强大的测试框架，无需引入第三方库即可完成单元测试、基准测试和示例测试。testing 包配合 `go test` 命令，提供了完整的测试工作流。良好的测试习惯是保证代码质量的基础，Go 的测试哲学强调简洁和实用。

## 基础概念

### 测试文件命名规则

- 测试文件以 `_test.go` 结尾，与被测试文件放在同一包下
- 测试函数以 `Test` 开头，参数为 `*testing.T`
- 基准测试函数以 `Benchmark` 开头，参数为 `*testing.B`
- 示例函数以 `Example` 开头，无参数

### 测试函数签名

```go
// 单元测试
func TestXxx(t *testing.T) { ... }

// 基准测试
func BenchmarkXxx(b *testing.B) { ... }

// 示例测试
func ExampleXxx() { ... }
```

## 快速上手

### 第一个测试

```go
// math.go
package math

func Add(a, b int) int {
    return a + b
}
```

```go
// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(1, 2)
    if result != 3 {
        t.Errorf("Add(1, 2) = %d, want 3", result)
    }
}
```

运行测试：

```bash
go test ./...           # 运行所有测试
go test -v ./...        # 详细输出
go test -run TestAdd    # 运行指定测试
```

## 详细用法

### 子测试与 t.Run

`t.Run` 创建子测试，支持独立运行和并行执行：

```go
func TestUser(t *testing.T) {
    t.Run("创建用户", func(t *testing.T) {
        user := NewUser("Alice")
        if user.Name != "Alice" {
            t.Error("用户名不正确")
        }
    })

    t.Run("更新用户", func(t *testing.T) {
        user := NewUser("Alice")
        user.UpdateName("Bob")
        if user.Name != "Bob" {
            t.Error("更新失败")
        }
    })
}
```

运行指定子测试：

```bash
go test -run TestUser/创建用户
```

### TestMain 自定义初始化

当测试需要全局初始化或清理时，使用 TestMain：

```go
func TestMain(m *testing.M) {
    // 初始化：连接测试数据库
    db := setupTestDB()
    defer db.Close()

    // 运行所有测试
    code := m.Run()

    // 清理资源
    cleanup()

    os.Exit(code)
}
```

### 基准测试进阶

```go
// 带子基准的基准测试
func BenchmarkSort(b *testing.B) {
    sizes := []int{100, 1000, 10000}

    for _, size := range sizes {
        b.Run(fmt.Sprintf("size_%d", size), func(b *testing.B) {
            data := generateData(size)
            b.ResetTimer() // 重置计时器，排除数据生成时间

            for i := 0; i < b.N; i++ {
                sorted := make([]int, len(data))
                copy(sorted, data)
                sort.Ints(sorted)
            }
        })
    }
}

// 基准测试中控制计时
func BenchmarkExpensive(b *testing.B) {
    // 准备工作不计入基准时间
    setup()

    b.ResetTimer()  // 重置计时器
    for i := 0; i < b.N; i++ {
        expensiveOperation()
    }
    b.StopTimer()   // 停止计时

    // 清理工作不计入基准时间
    cleanup()
}
```

## 常见场景

### 场景一：HTTP Handler 测试

```go
func TestHandler(t *testing.T) {
    // 创建测试请求
    req := httptest.NewRequest("GET", "/api/users", nil)
    w := httptest.NewRecorder()

    // 调用 handler
    handler := UserHandler{DB: mockDB}
    handler.ServeHTTP(w, req)

    // 验证响应
    if w.Code != http.StatusOK {
        t.Errorf("状态码 = %d, want %d", w.Code, http.StatusOK)
    }

    var users []User
    json.NewDecoder(w.Body).Decode(&users)
    if len(users) == 0 {
        t.Error("返回用户列表为空")
    }
}
```

### 场景二：接口 Mock 测试

```go
// 定义接口
type UserRepository interface {
    GetByID(id int) (*User, error)
}

// Mock 实现
type MockUserRepo struct {
    users map[int]*User
    err   error
}

func (m *MockUserRepo) GetByID(id int) (*User, error) {
    if m.err != nil {
        return nil, m.err
    }
    return m.users[id], nil
}

func TestGetUser(t *testing.T) {
    mock := &MockUserRepo{
        users: map[int]*User{1: {Name: "Alice"}},
    }

    service := NewUserService(mock)
    user, err := service.GetUser(1)

    if err != nil {
        t.Fatalf("意外错误: %v", err)
    }
    if user.Name != "Alice" {
        t.Errorf("用户名 = %s, want Alice", user.Name)
    }
}
```

### 场景三：测试覆盖率

```bash
# 生成覆盖率报告
go test -cover ./...

# 生成详细覆盖率文件
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out -o coverage.html

# 查看每个函数的覆盖率
go tool cover -func=coverage.out
```

## 注意事项

- 测试文件中不要使用 `init()` 函数，它会在所有测试之前执行，影响测试隔离性
- `t.Error` / `t.Errorf` 报告失败但继续执行，`t.Fatal` / `t.Fatalf` 报告失败并立即停止当前测试
- 基准测试中避免编译器优化消除代码，可以使用 `_ = result` 或 `runtime.KeepAlive(result)`
- 并行测试中必须捕获循环变量（Go 1.22 之前），否则闭包会引用最后一个值
- 测试代码也应保持简洁，避免过度抽象测试辅助函数
- 使用 `-count=1` 禁用测试缓存，确保每次都重新运行

## 进阶用法

### Fuzzing 模糊测试

Go 1.18 引入的原生模糊测试支持：

```go
func FuzzReverse(f *testing.F) {
    // 添加种子语料
    f.Add("hello")
    f.Add("世界")

    f.Fuzz(func(t *testing.T, original string) {
        reversed := Reverse(original)
        doubleReversed := Reverse(reversed)
        if doubleReversed != original {
            t.Errorf("Reverse(Reverse(%q)) = %q, want %q", original, doubleReversed, original)
        }
    })
}
```

```bash
go test -fuzz=FuzzReverse -fuzztime=30s
```

### 测试辅助函数

```go
// 使用 t.Helper() 标记辅助函数，错误信息指向调用方
func assertEqual(t *testing.T, got, want int) {
    t.Helper() // 标记为辅助函数
    if got != want {
        t.Errorf("got %d, want %d", got, want)
    }
}

func TestCalculation(t *testing.T) {
    assertEqual(t, Add(1, 2), 3)    // 错误行号指向这里，而非 assertEqual 内部
    assertEqual(t, Add(10, 20), 30)
}
```

### 构建标签控制测试

```go
// +build integration

package main

import "testing"

func TestDatabaseIntegration(t *testing.T) {
    // 仅在集成测试时运行
    db := connectRealDatabase()
    defer db.Close()
    // ...
}
```

```bash
# 运行集成测试
go test -tags=integration ./...

# 默认跳过集成测试
go test ./...
```

### 使用 testing.TB 统一测试接口

```go
// testing.TB 是 testing.T 和 testing.B 的共同接口
// 可以编写同时适用于单元测试和基准测试的辅助函数
func checkResult(t testing.TB, got, want int) {
    t.Helper()
    if got != want {
        t.Errorf("got %d, want %d", got, want)
    }
}
```
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

## 参考文献



Go 官方文档：https://go.dev/doc/
Go 内存模型：https://go.dev/ref/mem
Effective Go：https://go.dev/doc/effective_go
Go 标准库：https://pkg.go.dev/std
Go 官方博客：https://go.dev/blog/

## 延伸阅读



Go 并发与 channel，见 016-go 模块并发文档。
Go 原子操作与竞争检测，见 016-go/058-RaceDetectionAtomic 文档。
云原生与 Kubernetes，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Go 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Go 概述与环境配置 | 001-GoOverviewEnvSetup | 本文的前置基础 |
| Go 基础语法 | 002-GoBasicSyntax | 本文的前置基础 |
| Go 函数与方法 | 003-GoFunctionMethod | 本文的并列主题 |
| Go 数据结构 | 004-GoDataStructure | 本文的并列主题 |
| Go 接口与组合 | 005-GoInterfaceComposition | 本文的并列主题 |
| Go 并发编程 | 006-GoConcurrentProgramming | 本文的并列主题 |
| Go 错误处理 | 007-GoErrorHandling | 本文的并列主题 |
| Go 泛型 | 008-GoGeneric | 本文的并列主题 |
| Go 标准库与工具链 | 009-GoStandardLibraryToolchain | 本文的并列主题 |
| Go Web 开发与微服务 | 010-GoWebDevelopmentMicroservice | 本文的并列主题 |
| 切片原理 | 011-SlicePrinciple | 本文的原理深化 |
| Map原理 | 012-MapPrinciple | 本文的原理深化 |
| unsafe与指针 | 013-UnsafePointer | 本文的并列主题 |
| Channel原理 | 014-ChannelPrinciple | 本文的原理深化 |
| 反射 | 015-Reflection | 本文的并列主题 |
| 内存对齐 | 016-MemoryAlignment | 本文的并列主题 |
| Context详解 | 017-ContextDetailed | 本文的并列主题 |
| Goroutine调度 | 018-GoroutineSchedule | 本文的并列主题 |
| 接口与类型断言 | 019-InterfaceTypeAssertion | 本文的并列主题 |
| 错误处理进阶 | 020-ErrorHandlingAdvanced | 本文的并列主题 |
| Go与GraphQL | 021-GoGraphQL | 本文的并列主题 |
| Go与gRPC | 022-GoGRPC | 本文的并列主题 |
| Go与Kubernetes | 023-GoKubernetes | 本文的并列主题 |
| Go与Docker | 024-GoDocker | 本文的并列主题 |
| Go与Redis | 025-GoRedis | 本文的并列主题 |
| Go与消息队列 | 026-GoMessageQueue | 本文的并列主题 |
| Go与数据库 | 027-GoDatabase | 本文的并列主题 |
| Go与测试 | 028-GoTest | 本文自身 |
| Go与JSON | 029-GoJSON | 本文的并列主题 |
| Go与Fuzzing | 030-GoFuzzing | 本文的并列主题 |
| Go与CGO | 031-GoCGO | 本文的并列主题 |
| Go与Wasm | 032-GoWasm | 本文的并列主题 |
| Go与代码生成 | 033-GoCodeGeneration | 本文的并列主题 |
| Go与依赖注入 | 034-GoDependencyInjection | 本文的并列主题 |
| Go与配置管理 | 035-GoConfigManagement | 本文的并列主题 |
| Go与日志 | 036-GoLog | 本文的并列主题 |
| Go与模板 | 037-GoTemplate | 本文的并列主题 |
| Go与加密 | 038-GoEncryption | 本文的安全延伸 |
| Go与文件监控 | 039-GoFileMonitor | 本文的并列主题 |
| Go与时间 | 040-GoTime | 本文的并列主题 |
| Go与正则表达式 | 041-GoRegex | 本文的并列主题 |
| Go与信号处理 | 042-GoSignalHandling | 本文的并列主题 |
| Go与性能分析 | 043-GoPerformanceAnalysis | 本文的性能延伸 |
| Go与HTTP客户端 | 044-GoHTTPClient | 本文的并列主题 |
| Go与HTTP服务器 | 045-GoHTTP | 本文的并列主题 |
| Go与OAuth2 | 046-GoOAuth2 | 本文的并列主题 |
| Go与中间件 | 047-GoMiddleware | 本文的并列主题 |
| Go与分布式追踪 | 048-GoDistributedTracing | 本文的并列主题 |
| Go与限流 | 049-Go | 本文的并列主题 |
| goroutine与channel通信原理 | 050-GoroutineChannelPrinciple | 本文的原理深化 |
| GMP调度模型 | 051-GMPModel | 本文的并列主题 |
| 并发模式 | 052-ConcurrencyPattern | 本文的并列主题 |
| 反射实现通用函数 | 053-ReflectionGenericFunction | 本文的并列主题 |
| 内存逃逸分析 | 054-MemoryEscapeAnalysis | 本文的并列主题 |
| 垃圾回收与GC调优 | 055-GCAndTuning | 本文的性能延伸 |
| 泛型详解 | 056-GenericDetailed | 本文的并列主题 |
| 单元测试与基准测试 | 057-UnitTestBenchmark | 本文的并列主题 |
| 竞态检测与原子操作 | 058-RaceDetectionAtomic | 本文的并列主题 |
| 包管理详解 | 059-PackageManagementDetailed | 本文的并列主题 |
