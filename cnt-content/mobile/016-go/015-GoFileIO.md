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
