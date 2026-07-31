# C++ string_view 字符串视图

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础用法

**基本写法：创建 string_view**
`std::string_view <变量>(<字符串>);`
```cpp
#include <string_view>
// 从字符串字面量
std::string_view sv1 = "hello";
// 从 std::string
std::string s = "world";
std::string_view sv2 = s;
// 从指针和长度
std::string_view sv3(s.data(), 3);
// 默认构造（空）
std::string_view sv4;
```

---

**基本写法：make_string_view**
`std::string_view(<指针>, <长度>)`
```cpp
// 显式构造
const char* data = "hello world";
std::string_view sv(data, 5); // "hello"
// 从 C 字符串
std::string_view sv2(data);   // "hello world"
```

---

## 访问元素

**基本写法：下标访问**
`<sv>[<索引>]` `<sv>.at(<索引>)`
```cpp
// 字符访问
std::string_view sv = "hello";
char c = sv[0];        // 'h'
char c2 = sv.at(1);    // 'e'（越界抛异常）
char front = sv.front(); // 'h'
char back = sv.back();   // 'o'
```

---

**基本写法：data 与 size**
`<sv>.data()` `<sv>.size()` `<sv>.length()`
```cpp
// 底层数据与大小
std::string_view sv = "hello";
const char* p = sv.data(); // 指向底层字符
size_t n = sv.size();      // 5
size_t n2 = sv.length();   // 5（同 size）
bool empty = sv.empty();   // false
```

---

## 子串与查找

**基本写法：substr**
`<sv>.substr(<位置> [, <长度>])`
```cpp
// 取子串视图（不拷贝）
std::string_view sv = "hello world";
std::string_view sub = sv.substr(0, 5);  // "hello"
std::string_view sub2 = sv.substr(6);    // "world"
// O(1) 操作，返回新视图
```

---

**基本写法：find 查找**
`<sv>.find(<子串> [, <位置>])`
```cpp
// 查找子串
std::string_view sv = "hello world";
size_t pos = sv.find("world"); // 6
size_t pos2 = sv.find("xyz");  // npos
// 反向查找
size_t rpos = sv.rfind("o");   // 7
// 查找字符集
size_t f = sv.find_first_of("aeiou"); // 1（e）
size_t l = sv.find_last_of("aeiou");  // 7（o）
size_t fn = sv.find_first_not_of("helo"); // 6
```

---

**基本写法：contains（C++23）**
`<sv>.contains(<子串>)`
```cpp
// C++23 包含检查
std::string_view sv = "hello world";
bool has = sv.contains("world"); // true
bool has2 = sv.contains("xyz");  // false
bool has3 = sv.contains('w');    // true
```

---

**基本写法：starts_with/ends_with（C++20）**
`<sv>.starts_with(<前缀>)`
```cpp
// 前缀后缀检查
std::string_view sv = "hello.cpp";
bool isCpp = sv.ends_with(".cpp");    // true
bool startsHello = sv.starts_with("hello"); // true
sv.starts_with('h'); // true（字符）
```

---

## 比较

**基本写法：比较运算**
`<sv> == <sv2>` `<sv> < <sv2>`
```cpp
// 字典序比较
std::string_view a = "apple", b = "banana";
bool eq = (a == b);    // false
bool less = (a < b);   // true
// compare 返回值
int r = a.compare(b);  // 负数（a < b）
```

---

## 修改视图

**基本写法：remove_prefix**
`<sv>.remove_prefix(<长度>)`
```cpp
// 移除前缀（修改视图，不修改数据）
std::string_view sv = "  hello";
sv.remove_prefix(2); // sv = "hello"
```

---

**基本写法：remove_suffix**
`<sv>.remove_suffix(<长度>)`
```cpp
// 移除后缀
std::string_view sv = "hello.cpp";
sv.remove_suffix(4); // sv = "hello"
```

---

**基本写法：swap**
`<sv>.swap(<其他sv>)`
```cpp
// 交换两个视图
std::string_view a = "hello", b = "world";
a.swap(b);
// a = "world", b = "hello"
```

---

## 转换为 string

**基本写法：转 std::string**
`std::string(<sv>)`
```cpp
// 转换为 string（拷贝）
std::string_view sv = "hello";
std::string s(sv);          // 构造
std::string s2 = sv;        // 拷贝构造
std::string s3 = std::string(sv); // 显式
```

---

## 函数参数

**基本写法：用 string_view 作参数**
`void func(std::string_view <参数>)`
```cpp
// 接受多种字符串类型
void print(std::string_view sv) {
    std::cout << sv << "\n";
}
print("hello");              // C 字符串
print(std::string("world")); // std::string
print(someStringView);       // string_view
// 避免重载爆炸
```

---

## 注意事项

**基本写法：悬垂引用**
`std::string_view` 不拥有数据
```cpp
// 危险：临时 string 销毁后 view 失效
std::string_view bad = std::string("temp"); // 销毁后失效
// 安全：保持源数据存活
std::string s = "safe";
std::string_view sv = s; // s 存活期间有效
// 不可用 string_view 接收需要持有的数据
```

---

## 迭代

**基本写法：遍历**
`for (char c : <sv>)`
```cpp
// 范围 for 循环
std::string_view sv = "hello";
for (char c : sv) {
    std::cout << c;
}
// 迭代器
for (auto it = sv.begin(); it != sv.end(); ++it) {
    std::cout << *it;
}
```
