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