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
