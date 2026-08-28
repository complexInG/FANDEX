# Kotlin IO API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件读取

**基本写法：读取全部文本**
`File("<路径>").readText()`
```kotlin
// 一次性读取文本文件
val text = File("a.txt").readText()
```

---

**基本写法：按行读取**
`File("<路径>").readLines()`
```kotlin
// 按行读取为 List
val lines = File("a.txt").readLines()
```

---

**基本写法：读取全部字节**
`File("<路径>").readBytes()`
```kotlin
// 读取为字节数组
val bytes = File("a.txt").readBytes()
```

---

**基本写法：逐行流式读取**
`File("<路径>").useLines { }`
```kotlin
// 流式逐行处理自动关闭
File("a.txt").useLines { lines -> lines.forEach { } }
```

---

## 文件写入

**基本写法：写入文本**
`File("<路径>").writeText("<内容>")`
```kotlin
// 覆盖写入文本
File("out.txt").writeText("hello")
```

---

**基本写法：写入字节**
`File("<路径>").writeBytes(<字节数组>)`
```kotlin
// 覆盖写入字节
File("out.bin").writeBytes(bytes)
```

---

**基本写法：追加写入**
`File("<路径>").appendText("<内容>")`
```kotlin
// 追加文本到文件
File("log.txt").appendText("new line\n")
```

---

**基本写法：追加字节**
`File("<路径>").appendBytes(<字节数组>)`
```kotlin
// 追加字节数组
File("log.bin").appendBytes(bytes)
```

---

## 文件流操作

**基本写法：写入流**
`File("<路径>").outputStream()`
```kotlin
// 获取文件输出流
File("out.txt").outputStream().use { it.write(bytes) }
```

---

**基本写法：读取流**
`File("<路径>").inputStream()`
```kotlin
// 获取文件输入流
File("a.txt").inputStream().use { it.readBytes() }
```

---

**基本写法：BufferedWriter**
`File("<路径>").bufferedWriter()`
```kotlin
// 缓冲写入器
File("out.txt").bufferedWriter().use { w -> w.write("hi") }
```

---

**基本写法：BufferedReader**
`File("<路径>").bufferedReader()`
```kotlin
// 缓冲读取器
File("a.txt").bufferedReader().use { r -> r.readLine() }
```

---

## 文件与目录操作

**基本写法：创建文件**
`File("<路径>").createNewFile()`
```kotlin
// 创建新文件
File("a.txt").createNewFile()
```

---

**基本写法：创建目录**
`File("<路径>").mkdirs()`
```kotlin
// 递归创建目录
File("a/b/c").mkdirs()
```

---

**基本写法：删除文件**
`File("<路径>").delete()`
```kotlin
// 删除文件或空目录
File("a.txt").delete()
```

---

**基本写法：删除递归**
`File("<路径>").deleteRecursively()`
```kotlin
// 递归删除目录及内容
File("dir").deleteRecursively()
```

---

**基本写法：判断存在**
`File("<路径>").exists()`
```kotlin
// 判断文件是否存在
if (File("a.txt").exists()) { }
```

---

**基本写法：判断文件/目录**
`File("<路径>").isFile | isDirectory`
```kotlin
// 判断是文件还是目录
if (File("p").isDirectory) { }
```

---

**基本写法：列出文件**
`File("<路径>").listFiles()`
```kotlin
// 列出目录下文件
val files = File("dir").listFiles()
```

---

**基本写法：按扩展名过滤**
`File("<路径>").listFiles { _, name -> name.endsWith(".txt") }`
```kotlin
// 过滤特定扩展名
val txts = File("dir").listFiles { _, n -> n.endsWith(".txt") }
```

---

**基本写法：遍历目录树**
`File("<路径>").walk()`
```kotlin
// 深度遍历目录树
File("dir").walk().forEach { println(it) }
```

---

## 文件复制与移动

**基本写法：复制到**
`File("<源>").copyTo(File("<目标>"))`
```kotlin
// 复制文件
File("a.txt").copyTo(File("b.txt"))
```

---

**基本写法：递归复制**
`File("<源>").copyRecursively(File("<目标>"))`
```kotlin
// 递归复制目录
File("src").copyRecursively(File("dst"))
```

---

**基本写法：移动**
`File("<源>").renameTo(File("<目标>"))`
```kotlin
// 重命名或移动文件
File("a.txt").renameTo(File("b.txt"))
```

---

## 文件属性

**基本写法：文件大小**
`File("<路径>").length()`
```kotlin
// 获取文件字节数
val size = File("a.txt").length()
```

---

**基本写法：最后修改时间**
`File("<路径>").lastModified()`
```kotlin
// 获取最后修改时间戳
val t = File("a.txt").lastModified()
```

---

**基本写法：绝对路径**
`File("<路径>").absolutePath`
```kotlin
// 获取绝对路径
val abs = File("a.txt").absolutePath
```

---

## Path（kotlin.io.path）

**基本写法：创建 Path**
`Path("<路径>")`
```kotlin
// 创建 Path 对象
val p = Path("a/b.txt")
```

---

**基本写法：读写 Path**
`<path>.readText() | <path>.writeText()`
```kotlin
// Path 扩展读写
val text = Path("a.txt").readText()
Path("out.txt").writeText("hi")
```

---

**基本写法：递归创建**
`<path>.createDirectories()`
```kotlin
// 递归创建目录
Path("a/b/c").createDirectories()
```

---

**基本写法：复制 Path**
`<path>.copyTo(<目标>)`
```kotlin
// Path 复制
Path("a.txt").copyTo(Path("b.txt"))
```

---

## 标准流

**基本写法：标准输入**
`readLine()`
```kotlin
// 读取一行标准输入
val line = readLine()
```

---

**基本写法：标准输出**
`print(<值>) | println(<值>)`
```kotlin
// 标准输出
println("hello")
```

---

**基本写法：System.err**
`System.err.println(<值>)`
```kotlin
// 标准错误输出
System.err.println("error")
```

---

## 跨平台 IO

**基本写法：KMP 使用 okio**
`FileSystem.SYSTEM.read(<path>) { }`
```kotlin
// okio 跨平台文件读取
FileSystem.SYSTEM.read(Path("a.txt")) {
    readUtf8()
}
```

---

**基本写法：KMP 写入**
`FileSystem.SYSTEM.write(<path>) { }`
```kotlin
// okio 跨平台文件写入
FileSystem.SYSTEM.write(Path("out.txt")) {
    writeUtf8("hi")
}
```
