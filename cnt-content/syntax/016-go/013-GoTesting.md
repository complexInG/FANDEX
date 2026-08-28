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
