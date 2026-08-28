# C++ 类型萃取与 SFINAE

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 类型萃取基础

**基本写法：判断整型**
`std::is_integral_v<<类型>>`
```cpp
// 检查类型是否为整型
bool b = std::is_integral_v<int>;
```

---

**基本写法：判断浮点型**
`std::is_floating_point_v<<类型>>`
```cpp
// 检查类型是否为浮点型
bool b = std::is_floating_point_v<double>;
```

---

**基本写法：判断指针**
`std::is_pointer_v<<类型>>`
```cpp
// 检查类型是否为指针
bool b = std::is_pointer_v<int*>;
```

---

**基本写法：判断引用**
`std::is_lvalue_reference_v<<类型>>` / `std::is_rvalue_reference_v<<类型>>`
```cpp
// 区分左值与右值引用
bool l = std::is_lvalue_reference_v<T>;
```

---

**基本写法：判断相同类型**
`std::is_same_v<<T1>, <T2>>`
```cpp
// 判断两个类型是否相同
bool b = std::is_same_v<int, int32_t>;
```

---

## 类型变换

**基本写法：移除 const**
`std::remove_const_t<<类型>>`
```cpp
// 去掉 const 限定
using T = std::remove_const_t<const int>;  // int
```

---

**基本写法：移除引用**
`std::remove_reference_t<<类型>>`
```cpp
// 去掉引用
using T = std::remove_reference_t<int&>;  // int
```

---

**基本写法：移除指针**
`std::remove_pointer_t<<类型>>`
```cpp
// 去掉指针
using T = std::remove_pointer_t<int*>;  // int
```

---

**基本写法：添加 const**
`std::add_const_t<<类型>>`
```cpp
// 添加 const 限定
using T = std::add_const_t<int>;  // const int
```

---

**基本写法：decay**
`std::decay_t<<类型>>`
```cpp
// 模拟按值传参的退化
using T = std::decay_t<const int&>;  // int
```

---

## 条件类型选择

**基本写法：编译期选择类型**
`std::conditional_t<<条件>, <真类型>, <假类型>>`
```cpp
// 根据条件选择类型
using T = std::conditional_t<sizeof(int) == 4, int, long>;
```

---

**基本写法：enable_if 启用模板**
`std::enable_if_t<<条件>, [<类型>]>`
```cpp
// 条件满足时类型有效
template <typename T,
          typename = std::enable_if_t<std::is_integral_v<T>>>
void f(T x);
```

---

**基本写法：enable_if 用于返回类型**
`template <typename T> std::enable_if_t<<条件>, <返回类型>> <函数名>(T);`
```cpp
// 通过返回类型 SFINAE
template <typename T>
std::enable_if_t<std::is_integral_v<T>, int> to_int(T x) {
    return static_cast<int>(x);
}
```

---

## SFINAE 技巧

**基本写法：函数模板 SFINAE**
`template <typename T> auto <函数名>(T x) -> decltype(<表达式>);`
```cpp
// 表达式有效才匹配
template <typename T>
auto size(T& c) -> decltype(c.size()) {
    return c.size();
}
```

---

**基本写法：void_t 检测成员**
`template <typename T, typename = void> struct <名称> { };`
```cpp
// 检测类型是否有 size 成员
template <typename T, typename = void>
struct has_size : std::false_type {};

template <typename T>
struct has_size<T, std::void_t<decltype(std::declval<T>().size())>>
    : std::true_type {};
```

---

**基本写法：declval 生成假想值**
`std::declval<<类型>>()`
```cpp
// 在不求值上下文生成右值引用
decltype(std::declval<T>().foo()) ret;
```

---

## Concepts 替代 SFINAE

**基本写法：用 concept 替代 enable_if**
`template <typename T> requires <概念> <返回类型> <函数名>(T);`
```cpp
// C++20 更清晰的约束
template <typename T>
requires std::integral<T>
T add(T a, T b) { return a + b; }
```

---

## 编译期断言

**基本写法：static_assert**
`static_assert(<条件>, "[<消息>]");`
```cpp
// 编译期检查条件
static_assert(sizeof(int) == 4, "int must be 4 bytes");
```

---

**基本写法：断言类型属性**
`static_assert(std::is_integral_v<<类型>>);`
```cpp
// 编译期验证类型特征
static_assert(std::is_default_constructible_v<Widget>);
```

---

## 类型推断辅助

**基本写法：common_type**
`std::common_type_t<<T1>, <T2>>`
```cpp
// 取多个类型的公共类型
using T = std::common_type_t<int, double>;  // double
```

---

**基本写法：underlying_type**
`std::underlying_type_t<<枚举类型>>`
```cpp
// 获取枚举底层类型
using U = std::underlying_type_t<Color>;
```
