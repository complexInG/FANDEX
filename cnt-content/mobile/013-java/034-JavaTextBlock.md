# Java 文本块与字符串

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文本块基础

**基本写法：创建文本块**
`"""<换行><内容><换行>"""`
```java
// Java 15+ 多行字符串文本块
String json = """
    {
      "name": "Alice"
    }
    """;
```

---

**基本写法：文本块结尾控制**
`<内容>\n    """`
```java
// 末尾缩进决定去除前导空格
String s = """
    hello
    """;
```

---

**基本写法：保留末尾换行**
`"""<换行><内容>\n"""`
```java
// 行尾反斜杠表示不换行
String s = """
    hello \
    world
    """;
```

---

## 字符串模板（Java 21 预览）

**基本写法：字符串模板表达式**
`StringTemplate.STR."<文本>\{<表达式>}"`
```java
// Java 21 预览特性字符串模板
String name = "Alice";
String s = STR."Hello \{name}";
```

---

**基本写法：多变量插值**
`STR."<文本>\{<变量1>}\{<变量2>}"`
```java
// 模板中嵌入多个表达式
int x = 1, y = 2;
String s = STR."\{x} + \{y} = \{x + y}";
```

---

## 字符串常用操作

**基本写法：字符串格式化**
`String.format("<模板>", <参数>...)`
```java
// printf 风格格式化
String s = String.format("name=%s, age=%d", "Alice", 20);
```

---

**基本写法：formatted 方法**
`"<模板>".formatted(<参数>...)`
```java
// Java 15+ 实例方法格式化
String s = "name=%s".formatted("Alice");
```

---

**基本写法：拼接**
`String.join("<分隔符>", <元素>...)`
```java
// 用分隔符拼接字符串
String r = String.join(",", "a", "b", "c");
```

---

## 文本块与格式化结合

**基本写法：文本块格式化**
`"""<内容>""".formatted(<参数>...)`
```java
// 文本块配合 formatted 占位
String json = """
    {"name":"%s","age":%d}
    """.formatted("Alice", 20);
```

---

## 缩进控制

**基本写法：去除缩进**
`<字符串>.stripIndent();`
```java
// 去除最小公共缩进
String s = raw.stripIndent();
```

---

**基本写法：转义换行**
`<字符串>.translateEscapes();`
```java
// 将转义字符翻译为实际字符
String s = "a\\nb".translateEscapes();
```

---

## 字符串拼接

**基本写法：StringBuilder 拼接**
`StringBuilder sb = new StringBuilder(); sb.append(<值>);`
```java
// 可变字符串拼接
StringBuilder sb = new StringBuilder();
sb.append("a").append(1);
String r = sb.toString();
```

---

**基本写法：StringJoiner 拼接**
`new StringJoiner("<分隔符>", "[", "]").add(<值>);`
```java
// 带前后缀的拼接器
String r = new StringJoiner(",", "[", "]").add("a").add("b").toString();
```

---

## 字符串查找与判断

**基本写法：判断前后缀**
`<字符串>.startsWith("<前缀>");`
```java
// 判断是否以指定前缀开头
boolean b = "hello".startsWith("he");
```

---

**基本写法：包含子串**
`<字符串>.contains("<子串>");`
```java
// 判断是否包含子串
boolean b = "hello".contains("ell");
```

---

**基本写法：查找位置**
`<字符串>.indexOf("<子串>);`
```java
// 查找子串首次出现位置
int i = "hello".indexOf("l");
```

---

## 字符串转换

**基本写法：分割**
`<字符串>.split("<正则>);`
```java
// 按正则分割字符串
String[] parts = "a,b,c".split(",");
```

---

**基本写法：替换**
`<字符串>.replace("<旧>", "<新>");`
```java
// 替换所有匹配字面量
String s = "hello".replace("l", "L");
```

---

**基本写法：replaceAll 正则替换**
`<字符串>.replaceAll("<正则>", "<替换>");`
```java
// 使用正则替换
String s = "a1b2".replaceAll("\\d", "_");
```

---

**基本写法：去除空白**
`<字符串>.strip();`
```java
// 去除首尾 Unicode 空白
String s = "  hi  ".strip();
```

---

## 字符串与字节转换

**基本写法：编码为字节**
`<字符串>.getBytes(<字符集>);`
```java
// 使用 UTF-8 编码为字节
byte[] b = "hi".getBytes(StandardCharsets.UTF_8);
```

---

**基本写法：字节解码**
`new String(<字节数组>, <字符集>);`
```java
// 用指定字符集构造字符串
String s = new String(bytes, StandardCharsets.UTF_8);
```

---

## 重复与缩进

**基本写法：重复字符串**
`"<字符串>".repeat(<次数>);`
```java
// Java 11+ 字符串重复
String s = "ab".repeat(3);
```

---

**基本写法：添加缩进**
`<字符串>.indent(<空格数>);`
```java
// Java 12+ 给每行增加缩进
String s = "a\nb".indent(4);
```

---

## 字符串判空

**基本写法：判断空白**
`<字符串>.isBlank();`
```java
// Java 11+ 判断是否空白
boolean b = "   ".isBlank();
```

---

**基本写法：判断空**
`<字符串>.isEmpty();`
```java
// 判断长度是否为 0
boolean b = "".isEmpty();
```
