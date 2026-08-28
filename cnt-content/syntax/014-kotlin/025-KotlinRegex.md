# Kotlin 正则表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建正则

**基本写法：创建 Regex**
`Regex("<模式>")`
```kotlin
// 从字符串创建正则对象
val re = Regex("\\d+")
```

---

**基本写法：toRegex 转换**
`"<模式>".toRegex()`
```kotlin
// 字符串扩展转换为正则
val re = "[a-z]+".toRegex()
```

---

**基本写法：带选项创建**
`Regex("<模式>", setOf(<选项>))`
```kotlin
// 创建忽略大小写的正则
val re = Regex("hello", setOf(RegexOption.IGNORE_CASE))
```

---

**基本写法：原始字符串模式**
`Regex("""<模式>""")`
```kotlin
// 使用原始字符串避免转义
val re = Regex("""\d{3}-\d{4}""")
```

---

## 匹配判断

**基本写法：完整匹配**
`<re>.matches(<字符串>)`
```kotlin
// 判断整个字符串是否匹配
val ok = re.matches("123")
```

---

**基本写法：包含匹配**
`<re>.containsMatchIn(<字符串>)`
```kotlin
// 判断是否包含匹配
val has = re.containsMatchIn("abc123")
```

---

**基本写法：matches 中缀操作**
`<字符串> matches <re>`
```kotlin
// 中缀形式匹配
val ok = "123" matches re
```

---

## 查找与提取

**基本写法：查找首个**
`<re>.find(<字符串>)`
```kotlin
// 查找首个匹配
val m = re.find("a1b2")
val v = m?.value
```

---

**基本写法：查找所有**
`<re>.findAll(<字符串>)`
```kotlin
// 查找所有匹配
val all = re.findAll("a1b2c3").map { it.value }.toList()
```

---

**基本写法：获取捕获组**
`<match>?.groupValues`
```kotlin
// 获取捕获组列表
val groups = m?.groupValues
val g1 = groups?.get(1)
```

---

**基本写法：命名捕获组**
`<match>?.groups["<名称>"]?.value`
```kotlin
// 按名称获取捕获组
val re = Regex("""(?<year>\d{4})""")
val year = re.find("2025")?.groups?.get("year")?.value
```

---

## 替换操作

**基本写法：替换全部**
`<re>.replace(<字符串>, "<替换>")`
```kotlin
// 替换所有匹配
val r = re.replace("a1b2", "X")
```

---

**基本写法：函数替换**
`<re>.replace(<字符串>) { <替换> }`
```kotlin
// 使用函数生成替换值
val r = re.replace("a1b2") { m -> "[${m.value}]" }
```

---

**基本写法：替换首个**
`<re>.replaceFirst(<字符串>, "<替换>")`
```kotlin
// 仅替换首个匹配
val r = re.replaceFirst("a1b2", "X")
```

---

## 分割字符串

**基本写法：按正则分割**
`<re>.split(<字符串>)`
```kotlin
// 按正则分割字符串
val parts = Regex("[,;]").split("a,b;c")
```

---

## MatchResult 操作

**基本写法：next 下一个匹配**
`<match>?.next()`
```kotlin
// 链式获取下一个匹配
var cur = re.find("a1b2")
while (cur != null) { println(cur.value); cur = cur.next() }
```

---

**基本写法：获取匹配范围**
`<match>?.range`
```kotlin
// 获取匹配在原串中的范围
val range = m?.range
```

---

## 分组引用

**基本写法：替换中引用捕获组**
`<re>.replace(<字符串>, "$<组名>")`
```kotlin
// 引用命名捕获组进行替换
val r = Regex("(?<d>\\d)").replace("a1", "<${'$'}{d}>")
```

---

## RegexOption 选项

**基本写法：忽略大小写**
`RegexOption.IGNORE_CASE`
```kotlin
// 忽略大小写匹配
val re = Regex("hello", RegexOption.IGNORE_CASE)
```

---

**基本写法：多行模式**
`RegexOption.MULTILINE`
```kotlin
// ^ $ 匹配每行
val re = Regex("^a", RegexOption.MULTILINE)
```

---

**基本写法：单行模式**
`RegexOption.DOT_MATCHES_ALL`
```kotlin
// . 匹配包括换行符
val re = Regex("a.b", RegexOption.DOT_MATCHES_ALL)
```

---

## 常用模式示例

**基本写法：邮箱校验**
`Regex("^[\\w.]+@[\\w.]+$")`
```kotlin
// 简单邮箱正则
val email = Regex("""^[\w.]+@[\w.]+$""")
val ok = email.matches("a@b.com")
```

---

**基本写法：手机号校验**
`Regex("^1[3-9]\\d{9}$")`
```kotlin
// 中国大陆手机号校验
val phone = Regex("^1[3-9]\\d{9}$")
```

---

**基本写法：IPv4 校验**
`Regex("^\\d{1,3}(\\.\\d{1,3}){3}$")`
```kotlin
// IPv4 地址格式校验
val ip = Regex("""^\d{1,3}(\.\d{1,3}){3}$""")
```

---

## 字符串便捷方法

**基本写法：startsWith 正则**
`<字符串>.startsWith(Regex("<模式>"))`
```kotlin
// 判断是否以正则匹配开头
val ok = "abc".startsWith(Regex("[a-z]"))
```

---

**基本写法：trim 按 Regex**
`<字符串>.trim(<re>, <re>)`
```kotlin
// 按正则裁剪首尾
val r = "##abc##".trim(Regex("#+"))
```

---

## 性能优化

**基本写法：复用 Regex 实例**
`private val <re> = Regex("<模式>")`
```kotlin
// 编译一次复用避免重复解析
private val EMAIL_RE = Regex("""^[\w.]+@[\w.]+$""")
fun check(s: String) = EMAIL_RE.matches(s)
```
