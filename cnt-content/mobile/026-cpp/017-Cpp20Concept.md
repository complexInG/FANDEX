# C++20 Concepts 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 定义 Concept

**基本写法：requires 表达式**
`template <<类型参数>> concept <名称> = requires(<参数>) { <要求>; };`
```cpp
// 定义数值类型 Concept
template <typename T>
concept Numeric = requires(T a, T b) {
    { a + b } -> std::same_as<T>;
    { a < b } -> std::convertible_to<bool>;
};
```

---

**基本写法：基于已有 Concept**
`template <<类型参数>> concept <名称> = <Concept表达式>;`
```cpp
// 组合已有 Concept
template <typename T>
concept Integer = std::integral<T> && !std::same_as<T, bool>;
```

---

## 使用 Concept

**基本写法：约束模板参数**
`template <<Concept> <参数>>`
```cpp
// 约束 T 必须为 Numeric
template <Numeric T>
T add(T a, T b) { return a + b; }
```

---

**基本写法：简写模板语法**
`<Concept> <参数>`
```cpp
// 使用 Concept 简写
Numeric auto add(Numeric auto a, Numeric auto b) { return a + b; }
```

---

**基本写法：requires 子句**
`template <<类型参数>> requires <Concept> <函数声明>`
```cpp
// 使用 requires 子句
template <typename T>
requires std::integral<T>
T factorial(T n) { return n <= 1 ? 1 : n * factorial(n - 1); }
```

---

## 标准 Concept

**基本写法：std::integral 整数类型**
`std::integral<<类型>>`
```cpp
// 约束为整数类型
template <std::integral T>
T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
```

---

**基本写法：std::floating_point 浮点类型**
`std::floating_point<<类型>>`
```cpp
// 约束为浮点类型
template <std::floating_point T>
T sqrt(T x) { return std::sqrt(x); }
```

---

**基本写法：std::same_as 相同类型**
`std::same_as<<目标类型>>`
```cpp
// 约束为 int 类型
template <typename T>
requires std::same_as<T, int>
void process(T value) { }
```

---

**基本写法：std::convertible_to 可转换**
`std::convertible_to<<目标类型>>`
```cpp
// 可转换为 bool
template <typename T>
requires std::convertible_to<T, bool>
bool to_bool(T value) { return static_cast<bool>(value); }
```

---

**基本写法：std::derived_from 派生关系**
`std::derived_from<<基类>>`
```cpp
// 必须派生自 Base
class Base { };
template <std::derived_from<Base> T>
void process(T& obj) { }
```

---

**基本写法：std::default_initializable 默认可构造**
`std::default_initializable<<类型>>`
```cpp
// 必须可以默认构造
template <std::default_initializable T>
T create() { return T{}; }
```

---

## 迭代器 Concept

**基本写法：std::input_iterator 输入迭代器**
`std::input_iterator<<迭代器类型>>`
```cpp
// 约束为输入迭代器
template <std::input_iterator It>
void process(It first, It last) { }
```

---

**基本写法：std::random_access_iterator 随机访问迭代器**
`std::random_access_iterator<<迭代器类型>>`
```cpp
// 约束为随机访问迭代器
template <std::random_access_iterator It>
void sort(It first, It last) { }
```

---

## 可调用 Concept

**基本写法：std::invocable 可调用**
`std::invocable<<函数类型>>`
```cpp
// 约束 F 为可调用对象
template <std::invocable F>
void run(F func) { func(); }
```

---

**基本写法：std::predicate 谓词**
`std::predicate<<函数类型>>`
```cpp
// 约束 F 为返回 bool 的谓词
template <std::predicate<int> F>
bool test(F func, int x) { return func(x); }
```
