# C++ 反射与元编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类型信息

**基本写法：typeid**
`typeid(<类型或表达式>)`
```cpp
#include <typeinfo>
// 运行时类型信息
int x = 42;
const std::type_info& ti = typeid(x);
std::cout << ti.name();      // 类型名（编译器相关）
if (typeid(x) == typeid(int)) { /* 类型匹配 */ }
```

---

**基本写法：dynamic_cast**
`dynamic_cast<<派生>*>(<基类*>)`
```cpp
// 运行时类型转换
Base* p = getBase();
if (Derived* d = dynamic_cast<Derived*>(p)) {
    d->specificMethod();
}
```

---

## 编译期类型操作

**基本写法：type_traits 类型特征**
`std::is_<特征><<类型>>::value`
```cpp
#include <type_traits>
// 类型判断
static_assert(std::is_integral_v<int>);          // 是否整数
static_assert(std::is_pointer_v<int*>);          // 是否指针
static_assert(std::is_class_v<std::string>);     // 是否类
static_assert(std::is_base_of_v<Base, Derived>); // 继承关系
static_assert(std::is_convertible_v<int, double>); // 可转换
```

---

**基本写法：类型变换**
`std::remove_const<...>::type` 等
```cpp
// 类型变换（C++14 起有 _t 别名）
using T1 = std::remove_const_t<const int>;        // int
using T2 = std::remove_pointer_t<int*>;           // int
using T3 = std::add_const_t<int>;                 // const int
using T4 = std::decay_t<const int&>;              // int
using T5 = std::conditional_t<sizeof(int)==4, int, long>; // int
```

---

**基本写法：decay 与 common_type**
`std::decay_t<T>` `std::common_type_t<T...>`
```cpp
// 类型退化（值传递语义）
template <typename T>
void func(T x) {
    using D = std::decay_t<T>; // 去除引用、cv、数组退化
}
// 公共类型
using C = std::common_type_t<int, double>; // double
using C2 = std::common_type_t<char, short, int>; // int
```

---

## SFINAE

**基本写法：enable_if**
`std::enable_if_t<<条件>, <类型>>`
```cpp
#include <type_traits>
// SFINAE 条件启用
template <typename T,
          typename = std::enable_if_t<std::is_integral_v<T>>>
T addOne(T x) { return x + 1; }
addOne(42);     // OK
// addOne(3.14); // 错误：float 非整数
```

---

**基本写法：void_t 技巧**
`std::void_t<<表达式>...>`
```cpp
// 检测类型是否有某成员
template <typename T, typename = void>
struct has_size : std::false_type {};
template <typename T>
struct has_size<T, std::void_t<decltype(std::declval<T>().size())>>
    : std::true_type {};
static_assert(has_size<std::vector<int>>::value);  // true
static_assert(!has_size<int>::value);              // true
```

---

## Concepts（C++20）

**基本写法：requires 表达式**
`requires(<参数>) { <表达式>; }`
```cpp
// 编译期约束
template <typename T>
concept Iterable = requires(T t) {
    t.begin();
    t.end();
    { t.size() } -> std::convertible_to<size_t>;
};
template <Iterable T>
void printAll(const T& container) { /* ... */ }
```

---

**基本写法：requires 子句**
`requires <概念>`
```cpp
// 函数模板约束
template <typename T>
requires std::integral<T>
T gcd(T a, T b) {
    while (b) { T t = b; b = a % b; a = t; }
    return a;
}
```

---

## 编译期反射技巧

**基本写法：聚合体反射**
`struct <数据> { ... };` + 模板
```cpp
// 利用结构化绑定做字段遍历（技巧）
struct Point { int x; int y; };
template <typename T>
void printFields(const T& obj) {
    // C++17 结构化绑定
    const auto& [a, b] = obj;
    std::cout << a << "," << b;
}
Point p{3, 4};
printFields(p);
```

---

**基本写法：magic_get / Boost.PFR**
`boost::pfr::for_each_field`
```cpp
#include <boost/pfr.hpp>
// 无宏反射聚合体
struct Person { std::string name; int age; };
Person p{"Alice", 30};
boost::pfr::for_each_field(p, [](const auto& field) {
    std::cout << field << " ";
});
// 输出 Alice 30
```

---

## 编译期字符串

**基本写法：consteval 字符串处理**
`consteval <返回> <函数>()`
```cpp
// 编译期字符串操作
consteval size_t strLen(const char* s) {
    size_t n = 0;
    while (s[n]) ++n;
    return n;
}
constexpr size_t len = strLen("hello"); // 5，编译期
```

---

## 元编程工具

**基本写法：integral_constant**
`std::integral_constant<<类型>, <值>>`
```cpp
// 编译期常量类型
using Two = std::integral_constant<int, 2>;
static_assert(Two::value == 2);
// bool 特化
using True = std::true_type;
using False = std::false_type;
static_assert(True::value);
```

---

**基本写法：编译期循环展开**
`template <size_t... I>`
```cpp
// 编译期整数序列
template <size_t... I>
void printIndices(std::index_sequence<I...>) {
    ((std::cout << I << " "), ...); // 折叠表达式
}
printIndices(std::make_index_sequence<5>{});
// 输出 0 1 2 3 4
```
