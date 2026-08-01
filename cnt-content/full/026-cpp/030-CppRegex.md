---
order: 72
title: C++正则表达式
module: cpp
category: C++
difficulty: intermediate
description: regex库与模式匹配
author: fanquanpp
updated: '2026-08-01'
related:
  - cpp/C++序列化
  - cpp/C++网络编程
  - cpp/C++23与C++26新特性
  - cpp/C++与Python交互
prerequisites:
  - cpp/概述与环境配置
---
### 替换

```cpp
void replaceDemo() {
    std::string text = "今天是 2026-06-14，明天是 2026-06-15";

    // 简单替换：将所有日期替换为 "XXXX-XX-XX"
    std::regex dateRegex(R"(\d{4}-\d{2}-\d{2})");
    std::string result1 = std::regex_replace(text, dateRegex, "XXXX-XX-XX");
    std::cout << result1 << std::endl;
    // 输出: 今天是 XXXX-XX-XX，明天是 XXXX-XX-XX

    // 使用捕获组替换：将日期格式从 YYYY-MM-DD 改为 DD/MM/YYYY
    std::regex dateRegex2(R"((\d{4})-(\d{2})-(\d{2}))");
    std::string result2 = std::regex_replace(text, dateRegex2, "$3/$2/$1");
    std::cout << result2 << std::endl;
    // 输出: 今天是 14/06/2026，明天是 15/06/2026

    // 只替换第一个匹配
    std::string result3 = std::regex_replace(text, dateRegex, "XXXX-XX-XX",
        std::regex_constants::format_first_only);
    std::cout << result3 << std::endl;
    // 输出: 今天是 XXXX-XX-XX，明天是 2026-06-15

    // 隐藏手机号中间四位
    std::string phoneText = "联系手机: 13800138000 和 13900139000";
    std::regex phoneRegex(R"((1\d{2})\d{4}(\d{4}))");
    std::string result4 = std::regex_replace(phoneText, phoneRegex, "$1****$2");
    std::cout << result4 << std::endl;
    // 输出: 联系手机: 138****8000 和 139****9000
}
```

## 概述

C++11 引入了 `<regex>` 标准库，提供了正则表达式的支持。正则表达式是一种描述字符串模式的语言，可以用来搜索、匹配、替换和验证文本。C++ 的 regex 库支持多种正则语法（ECMAScript、POSIX 等），提供了匹配、搜索和替换等操作。

为什么需要正则表达式？当你需要验证用户输入的格式（如邮箱、手机号）、从文本中提取特定模式的数据（如 URL、日期）、或者批量替换文本中的某些模式时，正则表达式是最简洁高效的工具。没有正则表达式，你需要手写复杂的字符串解析代码。

## 基础概念

**正则表达式语法**：用特殊字符描述匹配规则。例如 `\d+` 匹配一个或多个数字，`[a-z]+` 匹配一个或多个小写字母。

**匹配（regex_match）**：检查整个字符串是否完全匹配正则表达式。适合验证格式。

**搜索（regex_search）**：在字符串中搜索匹配正则表达式的子串。适合提取数据。

**替换（regex_replace）**：将匹配的子串替换为新的内容。适合文本处理。

**捕获组**：用括号 `()` 包围的部分，可以单独提取匹配到的内容。

**迭代器（regex_iterator）**：遍历字符串中所有匹配的子串。

## 快速上手

```cpp
#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string text = "我的邮箱是 test@example.com，电话是 13800138000";

    // 1. 创建正则表达式对象
    std::regex emailRegex(R"(\w+@\w+\.\w+)");  // 匹配邮箱
    std::regex phoneRegex(R"(1\d{10})");        // 匹配手机号

    // 2. 搜索匹配
    std::smatch match;
    if (std::regex_search(text, match, emailRegex)) {
        std::cout << "找到邮箱: " << match.str() << std::endl;
        // 输出: 找到邮箱: test@example.com
    }

    if (std::regex_search(text, match, phoneRegex)) {
        std::cout << "找到电话: " << match.str() << std::endl;
        // 输出: 找到电话: 13800138000
    }

    // 3. 验证格式
    std::string input = "user@domain.com";
    if (std::regex_match(input, emailRegex)) {
        std::cout << "邮箱格式正确" << std::endl;
    }

    return 0;
}
```

## 详细用法

### 常用正则语法

```cpp
// 字符类
std::regex digit(R"(\d)");       // 匹配数字 [0-9]
std::regex word(R"(\w)");        // 匹配单词字符 [a-zA-Z0-9_]
std::regex space(R"(\s)");       // 匹配空白字符（空格、制表符、换行等）
std::regex letter(R"([a-z])");   // 匹配小写字母
std::regex hex(R"([0-9a-fA-F])");// 匹配十六进制字符

// 量词
std::regex oneOrMore(R"(\d+)");    // 一个或多个数字
std::regex zeroOrMore(R"(\d*)");   // 零个或多个数字
std::regex zeroOrOne(R"(\d?)");    // 零个或一个数字
std::regex exact(R"(\d{3})");      // 恰好3个数字
std::regex range(R"(\d{2,4})");    // 2到4个数字
std::regex atLeast(R"(\d{2,})");   // 至少2个数字

// 锚点
std::regex startOfLine(R"(^\d+)");  // 行首的数字
std::regex endOfLine(R"(\d+$)");    // 行尾的数字
std::regex wholeString(R"(^\d+$)"); // 整个字符串都是数字

// 分组和选择
std::regex group(R"((\d+)-(\d+))");       // 捕获组：匹配 "123-456"
std::regex choice(R"((cat|dog))");         // 选择：匹配 "cat" 或 "dog"
std::regex nonCapture(R"((?:\d+)-(\d+))"); // 非捕获组
```

### 捕获组

```cpp
#include <iostream>
#include <regex>
#include <string>

void captureGroupDemo() {
    std::string text = "日期: 2026-06-14";
    // 用括号定义捕获组
    std::regex dateRegex(R"((\d{4})-(\d{2})-(\d{2}))");

    std::smatch match;
    if (std::regex_search(text, match, dateRegex)) {
        // match[0] 是整个匹配
        std::cout << "完整匹配: " << match[0].str() << std::endl;  // 2026-06-14

        // match[1], match[2], ... 是各个捕获组
        std::cout << "年: " << match[1].str() << std::endl;  // 2026
        std::cout << "月: " << match[2].str() << std::endl;  // 06
        std::cout << "日: " << match[3].str() << std::endl;  // 14

        // 也可以获取匹配的位置
        std::cout << "位置: " << match[1].first - text.begin() << std::endl;
    }
}
```

### 搜索所有匹配

```cpp
void searchAllDemo() {
    std::string text = "价格: 99元, 199元, 299元";
    std::regex priceRegex(R"(\d+)元");

    // 方法一：使用迭代器
    auto begin = std::sregex_iterator(text.begin(), text.end(), priceRegex);
    auto end = std::sregex_iterator();

    for (auto it = begin; it != end; ++it) {
        std::smatch match = *it;
        std::cout << "找到价格: " << match.str() << std::endl;
    }
    // 输出:
    // 找到价格: 99元
    // 找到价格: 199元
    // 找到价格: 299元

    // 方法二：使用 regex_token_iterator 只获取捕获组
    std::regex numRegex(R"((\d+)元)");
    auto tokenBegin = std::sregex_token_iterator(text.begin(), text.end(), numRegex, 1);
    auto tokenEnd = std::sregex_token_iterator();

    for (auto it = tokenBegin; it != tokenEnd; ++it) {
        std::cout << "数字: " << *it << std::endl;
    }
    // 输出: 数字: 99, 数字: 199, 数字: 299
}
```

### 验证格式

```cpp
// 验证邮箱格式
bool isValidEmail(const std::string& email) {
    std::regex emailRegex(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
    return std::regex_match(email, emailRegex);
}

// 验证中国手机号
bool isValidPhone(const std::string& phone) {
    std::regex phoneRegex(R"(^1[3-9]\d{9}$)");
    return std::regex_match(phone, phoneRegex);
}

// 验证身份证号（18位）
bool isValidIdCard(const std::string& id) {
    std::regex idRegex(R"(^\d{17}[\dXx]$)");
    return std::regex_match(id, idRegex);
}

// 验证 URL
bool isValidUrl(const std::string& url) {
    std::regex urlRegex(R"(https?://[^\s]+)");
    return std::regex_match(url, urlRegex);
}

// 验证 IP 地址
bool isValidIP(const std::string& ip) {
    std::regex ipRegex(R"((\d{1,3}\.){3}\d{1,3})");
    if (!std::regex_match(ip, ipRegex)) return false;

    // 进一步验证每段范围
    int a, b, c, d;
    char dot;
    std::istringstream iss(ip);
    iss >> a >> dot >> b >> dot >> c >> dot >> d;
    return a >= 0 && a <= 255 && b >= 0 && b <= 255
        && c >= 0 && c <= 255 && d >= 0 && d <= 255;
}
```

### 正则标志

```cpp
// 忽略大小写
std::regex caseInsensitive("hello", std::regex_constants::icase);
std::cout << std::regex_match("HELLO", caseInsensitive) << std::endl;  // 1 (true)

// 选择语法类型
std::regex ecmascript(R"(\d+)", std::regex_constants::ECMAScript);   // 默认
std::regex basic(R"(\d+)", std::regex_constants::basic);             // POSIX 基本正则
std::regex extended(R"(\d+)", std::regex_constants::extended);       // POSIX 扩展正则

// 优化匹配速度（但增加编译时间）
std::regex optimized(R"(\d+)", std::regex_constants::optimize);
```

## 常见场景

### 解析配置文件

```cpp
#include <map>
#include <regex>

// 解析 key=value 格式的配置
std::map<std::string, std::string> parseConfig(const std::string& content) {
    std::map<std::string, std::string> config;
    std::regex lineRegex(R"((\w+)\s*=\s*(.+))");

    auto begin = std::sregex_iterator(content.begin(), content.end(), lineRegex);
    auto end = std::sregex_iterator();

    for (auto it = begin; it != end; ++it) {
        std::string key = (*it)[1].str();
        std::string value = (*it)[2].str();

        // 去除值两端的空格和引号
        if (value.front() == '"' && value.back() == '"') {
            value = value.substr(1, value.size() - 2);
        }

        config[key] = value;
    }

    return config;
}

// 使用
std::string configText = R"(
    host = "localhost"
    port = 8080
    debug = true
)";
auto config = parseConfig(configText);
// config["host"] = "localhost"
// config["port"] = "8080"
```

### 日志分析

```cpp
// 解析 Nginx 访问日志
void parseAccessLog(const std::string& log) {
    // 格式: 192.168.1.1 - - [14/Jun/2026:10:30:00 +0800] "GET /index.html HTTP/1.1" 200 1234
    std::regex logRegex(
        R"((\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) \S+" (\d+) (\d+))"
    );

    std::smatch match;
    if (std::regex_search(log, match, logRegex)) {
        std::cout << "IP: " << match[1].str() << std::endl;
        std::cout << "时间: " << match[2].str() << std::endl;
        std::cout << "方法: " << match[3].str() << std::endl;
        std::cout << "路径: " << match[4].str() << std::endl;
        std::cout << "状态码: " << match[5].str() << std::endl;
        std::cout << "大小: " << match[6].str() << std::endl;
    }
}
```

## 注意事项

**性能问题**：`std::regex` 在某些编译器（特别是 GCC）上的性能较差。如果性能敏感，考虑使用 Boost.Regex 或 PCRE 库。

**原始字符串**：正则表达式中大量使用反斜杠，建议使用 C++11 的原始字符串 `R"(...)"` 来避免双重转义。`R"(\d+)"` 比 `"\\d+"` 更清晰。

**贪婪匹配**：默认情况下量词是贪婪的（匹配尽可能多的字符）。使用 `?` 使其变为懒惰的：`\d+?` 匹配尽可能少的数字。

**正则编译开销**：创建 `std::regex` 对象时会编译正则表达式，这是相对耗时的操作。如果同一个正则在循环中使用，应该在循环外创建 regex 对象。

**异常安全**：如果正则表达式语法有误，构造 `std::regex` 会抛出 `std::regex_error` 异常。在生产代码中应该捕获此异常。

## 进阶用法

### 自定义替换函数

```cpp
// 使用回调函数进行替换
template<typename Callback>
std::string regexReplaceCallback(const std::string& text,
    const std::regex& pattern, Callback callback)
{
    std::string result;
    auto begin = std::sregex_iterator(text.begin(), text.end(), pattern);
    auto end = std::sregex_iterator();

    size_t lastPos = 0;
    for (auto it = begin; it != end; ++it) {
        // 添加匹配前的文本
        result += text.substr(lastPos, it->position() - lastPos);
        // 调用回调函数获取替换文本
        result += callback(*it);
        lastPos = it->position() + it->length();
    }
    // 添加最后一个匹配后的文本
    result += text.substr(lastPos);

    return result;
}

// 使用：将所有数字乘以2
std::string text = "价格: 100元, 200元, 300元";
std::regex numRegex(R"(\d+)");
std::string result = regexReplaceCallback(text, numRegex,
    [](const std::smatch& m) -> std::string {
        int num = std::stoi(m.str());
        return std::to_string(num * 2);
    });
// result: "价格: 200元, 400元, 600元"
```

### 使用 Boost.Regex 提升性能

```cpp
#include <boost/regex.hpp>

// Boost.Regex 的 API 与 std::regex 几乎相同
// 但性能通常更好，特别是在 GCC 上

boost::regex pattern(R"(\d{4}-\d{2}-\d{2})");
boost::smatch match;
if (boost::regex_search(text, match, pattern)) {
    std::cout << match.str() << std::endl;
}

std::string result = boost::regex_replace(text, pattern, "DATE");
```
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

## 参考文献

cppreference C++ 文档：https://zh.cppreference.com/w/cpp
C++ 核心指南：https://isocpp.github.io/CppCoreGuidelines/
C++ 标准草案（WG21）：https://isocpp.org/std/the-standard
CMake 官方文档：https://cmake.org/documentation/
Compiler Explorer：https://godbolt.org/

## 延伸阅读

C++ 模板深入，见 026-cpp/062-CppTemplate 文档。
STL 容器与算法，见 026-cpp 模块 STL 文档。
并发与原子，见 026-cpp 模块并发文档。
Rust 内存安全对比，见 053-rust 模块（若已加入）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 C++ 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C++ 概述与现代标准 | 001-CppOverviewAndModernStandard | 本文的前置基础 |
| C++ 基础语法 | 002-CppBasicSyntax | 本文的前置基础 |
| C++ 类型系统 | 003-CppTypeSystem | 本文的并列主题 |
| C++ 引用 | 004-CppReference | 本文的并列主题 |
| 右值引用与移动语义 | 005-RvalueReferenceMoveSemantics | 本文的并列主题 |
| C++ 指针 | 006-PointersCppreferenceCom | 本文的并列主题 |
| 智能指针详解 | 007-N4089DeletingSafeBoolInFavorOfExplicitBool | 本文的并列主题 |
| Lambda表达式 | 008-LambdaExpression | 本文的并列主题 |
| 模板元编程 | 009-ATourOfC3rdEditionOnlineExcerpts | 本文的并列主题 |
| C++20范围 | 010-Cpp20Range | 本文的并列主题 |
| C++20模块 | 011-Cpp20Module | 本文的并列主题 |
| 设计模式与C++ | 012-DesignPatternCpp | 本文的并列主题 |
| RAII与资源管理 | 013-RAIIResourceManagement | 本文的并列主题 |
| 运算符重载 | 014-OperatorOverloading | 本文的并列主题 |
| C++ 面向对象基础 | 015-COOPBasics | 本文的前置基础 |
| C++ STL 算法详解 | 016-CSTL | 本文的并列主题 |
| 字符串处理 | 017-StringProcessing | 本文的并列主题 |
| 文件IO与文件系统 | 018-FileIOFileSystem | 本文的并列主题 |
| 异常安全 | 019-ExceptionSecurity | 本文的安全延伸 |
| 多线程与并发 | 020-MultithreadingConcurrency | 本文的并列主题 |
| 类型特征与SFINAE | 021-TypeTraitsSFINAE | 本文的并列主题 |
| 变参模板 | 022-VariadicTemplate | 本文的并列主题 |
| constexpr与编译期计算 | 023-ConstexprCompileTime | 本文的并列主题 |
| 命名空间与链接 | 024-NamespaceLinkage | 本文的并列主题 |
| C++网络编程 | 025-CppNetworkProgramming | 本文的并列主题 |
| C++ 面向对象进阶 | 026-COOPAdvanced | 本文的并列主题 |
| C++内存模型 | 027-CppMemoryModel | 本文的并列主题 |
| C++图形编程 | 028-CppGraphicsProgramming | 本文的并列主题 |
| C++工具链 | 029-CppToolchain | 本文的并列主题 |
| C++正则表达式 | 030-CppRegex | 本文自身 |
| C++与Python交互 | 031-CppPythonInteraction | 本文的并列主题 |
| C++测试框架 | 032-CppTestFramework | 本文的并列主题 |
| C++与Rust对比 | 033-CppRustComparison | 本文的并列主题 |
| C++23与C++26新特性 | 034-Cpp23Cpp26NewFeatures | 本文的并列主题 |
| C++性能优化 | 035-CppPerformance | 本文的性能延伸 |
| C++序列化 | 036-CppSerialization | 本文的并列主题 |
| C++游戏开发 | 037-CppGameDev | 本文的并列主题 |
| C++嵌入式开发 | 038-CppEmbedded | 本文的并列主题 |
| C++ 内存管理 | 039-CppMemoryManagement | 本文的并列主题 |
| C++代码规范 | 040-CppCodeStyle | 本文的并列主题 |
| C++与WebAssembly | 041-CppWebAssembly | 本文的并列主题 |
| C++反射与元编程 | 042-CppReflectionMetaprogramming | 本文的并列主题 |
| C++数学库 | 043-CppMathLibrary | 本文的并列主题 |
| 智能指针 | 044-SmartPointer | 本文的并列主题 |
| C++ 日期时间 | 045-CppDateTime | 本文的并列主题 |
| C++格式化输出 | 046-CppFormatOutput | 本文的并列主题 |
| C++26 与最新标准 | 047-Cpp26AndLatestStandard | 本文的并列主题 |
| C++ STL 容器与迭代器 | 048-CSTL | 本文的并列主题 |
| 并发编程 | 049-ConcurrentProgramming | 本文的并列主题 |
| RAII资源管理 | 050-CCoreGuidelinesResourceManagement | 本文的并列主题 |
| C++ STL 算法与函数对象 | 051-CSTLAlgorithmAndFunctionObject | 本文的并列主题 |
| 移动语义详解 | 052-MoveSemanticsDetailed | 本文的并列主题 |
| 完美转发与引用折叠 | 053-PerfectForwardingReferenceCollapse | 本文的并列主题 |
| 虚函数表与多态内存布局 | 054-VTablePolymorphismMemoryLayout | 本文的并列主题 |
| 智能指针循环引用 | 055-SmartPointerCircularReference | 本文的并列主题 |
| Lambda捕获详解 | 056-LambdaCaptureDetailed | 本文的并列主题 |
| 类型萃取与SFINAE | 057-TypeExtractionSFINAE | 本文的并列主题 |
| 可变参数模板与折叠表达式 | 058-VariadicTemplateFoldExpression | 本文的并列主题 |
| C++20协程 | 059-Cpp20Coroutine | 本文的并列主题 |
| C++20概念 | 060-Cpp20Concept | 本文的并列主题 |
| C++23新特性 | 061-Cpp23NewFeatures | 本文的并列主题 |
| C++ 模板 | 062-CppTemplate | 本文的并列主题 |
| 内存序与无锁编程 | 063-MemoryOrderLockFree | 本文的并列主题 |
| C++ 异常处理与性能优化 | 064-CppExceptionAndPerformance | 本文的性能延伸 |
| C++ 调试与性能分析 | 065-CDebugPerformanceAnalysis | 本文的性能延伸 |
| C++ 项目实战 | 066-CppProjectPractice | 本文的综合应用 |
| C++ STL 容器使用速查 | 067-STLContainerUsage | 本文的并列主题 |
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文的并列主题 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
