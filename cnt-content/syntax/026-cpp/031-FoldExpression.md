# C++ 折叠表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 一元右折叠

**基本写法：一元右折叠**
`(<参数包> <op> ...)`
```cpp
// 从右向左结合计算
template <typename... Args>
auto sum(Args... args) {
    return (args + ...);   // 等价 a1+(a2+(...+aN))
}
```

---

## 一元左折叠

**基本写法：一元左折叠**
`(... <op> <参数包>)`
```cpp
// 从左向右结合计算
template <typename... Args>
auto sum(Args... args) {
    return (... + args);   // 等价 ((a1+a2)+...)+aN
}
```

---

## 二元右折叠

**基本写法：带初值的右折叠**
`(<参数包> <op> ... <op> <初值>)`
```cpp
// 指定初值从右向左
template <typename... Args>
auto sum(Args... args) {
    return (args + ... + 0);   // 空包返回 0
}
```

---

## 二元左折叠

**基本写法：带初值的左折叠**
`(<初值> <op> ... <op> <参数包>)`
```cpp
// 指定初值从左向右
template <typename... Args>
auto sum(Args... args) {
    return (0 + ... + args);   // 空包返回 0
}
```

---

## 常用运算符

**基本写法：逻辑与**
`(... && <args>)`
```cpp
// 全部条件为真
template <typename... Args>
bool all_true(Args... args) {
    return (... && args);
}
```

---

**基本写法：逻辑或**
`(... || <args>)`
```cpp
// 任一条件为真
template <typename... Args>
bool any_true(Args... args) {
    return (args || ...);
}
```

---

**基本写法：逗号折叠**
`(<args>, ...)`
```cpp
// 按顺序执行每个表达式
template <typename... Args>
void print_all(Args... args) {
    ((std::cout << args << ' '), ...);
}
```

---

**基本写法：位运算折叠**
`(<args> | ...)`
```cpp
// 合并所有位标志
template <typename... Flags>
int combine(Flags... flags) {
    return (flags | ...);
}
```

---

## 类型包折叠

**基本写法：检查全部类型相同**
`((std::is_same_v<<T>, <Args>>) && ...)`
```cpp
// 编译期判断类型包是否全为 T
template <typename T, typename... Args>
constexpr bool all_same = (std::is_same_v<T, Args> && ...);
```

---

**基本写法：检查任意类型匹配**
`((std::is_same_v<<T>, <Args>>) || ...)`
```cpp
// 编译期判断类型包是否包含 T
template <typename T, typename... Args>
constexpr bool any_same = (std::is_same_v<T, Args> || ...);
```

---

## 继承链折叠

**基本写法：多继承折叠**
`class <派生> : public <Bases>... { };`
```cpp
// 通过折叠展开基类列表
template <typename... Bases>
struct Derived : Bases... {
    using Bases::operator()...;
};
```

---

## 数组与初始化折叠

**基本写法：数组初始化列表**
`{ <args>... }`
```cpp
// 展开为初始化列表
template <typename... Args>
auto make_array(Args... args) {
    return std::array<std::common_type_t<Args...>, sizeof...(Args)>{args...};
}
```

---

**基本写法：索引序列展开**
`<arr>[<seq>]...`
```cpp
// 配合 index_sequence 展开数组
template <size_t... I>
void print_indices(std::index_sequence<I...>) {
    ((std::cout << I << ' '), ...);
}
```

---

## 空包处理

**基本写法：空包与二元折叠**
`(<初值> <op> ... <op> <args>)`
```cpp
// 空参数包使用二元折叠返回初值
template <typename... Args>
auto count() {
    return (sizeof...(Args) + ... + 0);
}
```

---

**基本写法：空包一元折叠仅部分运算符合法**
`(... && <args>)` 空包返回 true
```cpp
// && 与 || 与 , 对空包有定义
template <typename... Args>
bool always_true() {
    return (... && Args::value);   // 空包为 true
}
```
