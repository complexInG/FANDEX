# C++ 正则表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 正则对象

**基本写法：构造正则**
`std::regex <变量>(<模式>);`
```cpp
// 编译正则模式
std::regex re("\\d+");
```

---

**基本写法：忽略大小写**
`std::regex <变量>(<模式>, std::regex::icase);`
```cpp
// 匹配时忽略大小写
std::regex re("hello", std::regex::icase);
```

---

**基本写法：扩展语法**
`std::regex <变量>(<模式>, std::regex::extended);`
```cpp
// 使用 POSIX 扩展正则语法
std::regex re("a+", std::regex::extended);
```

---

## 匹配

**基本写法：整串匹配**
`std::regex_match(<字符串>, <正则>);`
```cpp
// 整个字符串是否匹配
bool b = std::regex_match("12345", re);
```

---

**基本写法：匹配并捕获**
`std::regex_match(<字符串>, <smatch>, <正则>);`
```cpp
// 提取捕获组
std::smatch m;
if (std::regex_match(str, m, re)) {
    std::string g1 = m[1];
}
```

---

**基本写法：搜索子串**
`std::regex_search(<字符串>, <正则>);`
```cpp
// 查找第一个匹配子串
bool b = std::regex_search("abc123def", re);
```

---

**基本写法：搜索并捕获**
`std::regex_search(<字符串>, <smatch>, <正则>);`
```cpp
// 提取匹配子串与捕获组
std::smatch m;
if (std::regex_search(str, m, re)) {
    std::string matched = m[0];
}
```

---

## 迭代匹配

**基本写法：遍历所有匹配**
`std::sregex_iterator(<起始>, <结束>, <正则>);`
```cpp
// 遍历所有匹配结果
auto begin = std::sregex_iterator(str.begin(), str.end(), re);
auto end = std::sregex_iterator();
for (auto it = begin; it != end; ++it) {
    std::cout << it->str() << '\n';
}
```

---

**基本写法：分词迭代**
`std::sregex_token_iterator(<起始>, <结束>, <正则>, [-1]);`
```cpp
// 按分隔符切分字符串
std::regex sep("[,\\s]+");
auto it = std::sregex_token_iterator(str.begin(), str.end(), sep, -1);
```

---

## 替换

**基本写法：替换全部**
`std::regex_replace(<字符串>, <正则>, <替换串>);`
```cpp
// 替换所有匹配子串
std::string r = std::regex_replace(s, re, "NUM");
```

---

**基本写法：只替换第一个**
`std::regex_replace(<字符串>, <正则>, <替换串>, std::format_first_only);`
```cpp
// 仅替换首次匹配
std::string r = std::regex_replace(s, re, "X", std::format_first_only);
```

---

**基本写法：使用反向引用**
`std::regex_replace(<字符串>, <正则>, "$1")`
```cpp
// 引用捕获组内容
std::regex re("(\\w+)@(\\w+)");
std::string r = std::regex_replace(s, re, "$2.$1");
```

---

## match 结果

**基本写法：获取匹配前缀**
`<m>.prefix()`
```cpp
// 匹配子串之前的内容
auto pre = m.prefix();
```

---

**基本写法：获取匹配后缀**
`<m>.suffix()`
```cpp
// 匹配子串之后的内容
auto suf = m.suffix();
```

---

**基本写法：获取捕获组数量**
`<m>.size()`
```cpp
// 包含完整匹配的捕获组数
size_t n = m.size();
```

---

## 常用元字符

**基本写法：字符类**
`[<字符集>]`
```cpp
// 匹配数字字母
std::regex re("[0-9a-zA-Z]+");
```

---

**基本写法：预定义字符类**
`\\d` `\\w` `\\s`
```cpp
// 数字字母空白
std::regex re("\\w+\\s\\d+");
```

---

**基本写法：量词**
`*` `+` `?` `{n,m}`
```cpp
// 重复次数
std::regex re("a{2,4}");
```

---

**基本写法：锚点**
`^` `$`
```cpp
// 行首行尾
std::regex re("^start.*end$");
```

---

**基本写法：分组与非捕获**
`(...)` `(?:...)`
```cpp
// 捕获组与非捕获组
std::regex re("(\\d+)(?:\\.\\d+)?");
```
