# Java 正则表达式 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Pattern 编译

**基本写法：编译正则**
`Pattern.compile("<regex>"[, <flags>]): Pattern`
```java
// 编译正则表达式
Pattern p = Pattern.compile("\\d+");
Pattern pi = Pattern.compile("abc", Pattern.CASE_INSENSITIVE);
Pattern pm = Pattern.compile("a.b", Pattern.DOTALL);
```

---

**基本写法：标志位组合**
`Pattern.compile("<regex>", Pattern.<flag1> | Pattern.<flag2>);`
```java
// 多个标志位用按位或组合
Pattern p = Pattern.compile("hello", Pattern.CASE_INSENSITIVE | Pattern.MULTILINE);
```

---

## Matcher 匹配

**基本写法：创建匹配器**
`<pattern>.matcher(<input>): Matcher`
```java
// 创建 Matcher 对象
Matcher m = p.matcher("123 456");
```

---

**基本写法：完整匹配**
`<matcher>.matches(): boolean`
```java
// 整个字符串是否匹配
boolean ok = p.matcher("123").matches();
```

---

**基本写法：查找下一个**
`<matcher>.find(): boolean`
```java
// 查找下一个匹配
while (m.find()) {
    System.out.println(m.group());
}
```

---

**基本写法：匹配位置**
`<matcher>.start(): int` / `<matcher>.end(): int`
```java
// 获取匹配起止索引
if (m.find()) {
    int start = m.start();
    int end = m.end();
}
```

---

## 分组捕获

**基本写法：捕获组**
`(<pattern>)`
```java
// 圆括号定义捕获组
Pattern p = Pattern.compile("(\\d+)-(\\d+)");
Matcher m = p.matcher("12-34");
if (m.matches()) {
    m.group(0); // "12-34" 整个匹配
    m.group(1); // "12" 第一组
    m.group(2); // "34" 第二组
}
```

---

**基本写法：命名捕获组**
`(?<<name><pattern>)`
```java
// 命名捕获组（Java 7+）
Pattern p = Pattern.compile("(?<year>\\d{4})-(?<month>\\d{2})");
Matcher m = p.matcher("2024-03");
if (m.matches()) {
    m.group("year");   // "2024"
    m.group("month");  // "03"
}
```

---

**基本写法：组总数**
`<matcher>.groupCount(): int`
```java
// 获取捕获组数量（不含 group(0)）
int count = m.groupCount();
```

---

## 替换操作

**基本写法：替换全部**
`<matcher>.replaceAll("<replacement>"): String`
```java
// 替换所有匹配
String r = p.matcher("a1b2").replaceAll("X");
```

---

**基本写法：替换首个**
`<matcher>.replaceFirst("<replacement>"): String`
```java
// 仅替换第一个匹配
String r = p.matcher("a1b2").replaceFirst("X");
```

---

**基本写法：引用捕获组替换**
`<matcher>.replaceAll("$<groupName>");` 或 `$<n>`
```java
// 引用命名组
Pattern p = Pattern.compile("(?<word>\\w+)");
String r = p.matcher("hello").replaceAll("${word}!");
// 引用编号组
String r2 = Pattern.compile("(\\w)(\\w)").matcher("ab").replaceAll("$2$1");
```

---

## 常用预定义字符

**基本写法：字符类**
```java
// .   任意字符（默认不含换行）
// \d  数字 [0-9]
// \D  非数字
// \w  单词字符 [a-zA-Z0-9_]
// \W  非单词字符
// \s  空白字符
// \S  非空白字符
```

---

**基本写法：量词**
```java
// ?     0 或 1 次
// *     0 次或多次
// +     1 次或多次
// {n}   恰好 n 次
// {n,}  至少 n 次
// {n,m} n 到 m 次
```

---

**基本写法：边界匹配**
```java
// ^   行开头
// $   行结尾
// \b  单词边界
// \B  非单词边界
// \A  输入开头
// \z  输入结尾
```

---

## 断言

**基本写法：正向先行断言**
`(?=<pattern>)`
```java
// 匹配后面跟着数字的字母
Pattern p = Pattern.compile("[a-z]+(?=\\d)");
```

---

**基本写法：负向先行断言**
`(?!<pattern>)`
```java
// 匹配后面不跟数字的字母
Pattern p = Pattern.compile("[a-z]+(?!\\d)");
```

---

## String 正则方法

**基本写法：分割**
`<string>.split("<regex>"[, <limit>]): String[]`
```java
// 按正则分割字符串
String[] parts = "a,b,,c".split(",");
String[] parts2 = "a1b2c".split("\\d", 2);
```

---

**基本写法：替换全部**
`<string>.replaceAll("<regex>", "<replacement>): String`
```java
// 字符串直接替换
String r = "2024-03".replaceAll("\\d", "*");
```

---

**基本写法：匹配判断**
`<string>.matches("<regex>"): boolean`
```java
// 整串是否匹配
boolean ok = "123".matches("\\d+");
```

---

## 标志位常量

**基本写法：常用标志**
```java
// Pattern.CASE_INSENSITIVE  忽略大小写
// Pattern.MULTILINE         ^ $ 匹配每行
// Pattern.DOTALL            . 匹配换行
// Pattern.UNICODE_CASE      Unicode 大小写
// Pattern.COMMENTS          忽略空白与注释
// Pattern.LITERAL           字面量模式
```

---