# C++ 模板编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数模板

**基本写法：定义函数模板**
`template <typename <T>> <返回类型> <函数名>(<参数>) { }`
```cpp
// 泛型加法函数
template <typename T>
T add(T a, T b) { return a + b; }
```

---

**基本写法：多类型参数**
`template <typename <T1>, typename <T2>>`
```cpp
// 两个不同类型的参数
template <typename T1, typename T2>
auto mul(T1 a, T2 b) { return a * b; }
```

---

**基本写法：非类型模板参数**
`template <typename <T>, <类型> <N>>`
```cpp
// 编译期常量参数
template <typename T, int N>
T scale(T x) { return x * N; }
```

---

**基本写法：调用函数模板**
`<函数名><<类型>>(<参数>);`
```cpp
// 显式指定模板参数
int r = add<int>(3, 4);
```

---

## 类模板

**基本写法：定义类模板**
`template <typename <T>> class <类名> { };`
```cpp
// 泛型栈容器
template <typename T>
class Stack {
    std::vector<T> data;
public:
    void push(T v) { data.push_back(v); }
};
```

---

**基本写法：实例化类模板**
`<类名><<类型>> <变量>;`
```cpp
// 创建 int 类型栈
Stack<int> s;
```

---

**基本写法：类外定义成员**
`template <typename <T>> <返回类型> <类名><<T>>::<方法名>(<参数>) { }`
```cpp
// 类外定义成员函数
template <typename T>
void Stack<T>::push(T v) { data.push_back(v); }
```

---

## 模板特化

**基本写法：全特化**
`template <> class <类名><<具体类型>> { };`
```cpp
// 针对 bool 类型的特化实现
template <>
class Stack<bool> {
    std::vector<bool> data;
public:
    void push(bool v) { data.push_back(v); }
};
```

---

**基本写法：函数模板全特化**
`template <> <返回类型> <函数名><<具体类型>>(<参数>) { }`
```cpp
// 针对指针类型的特化
template <>
int max_ptr<int>(int* a, int* b) { return *a > *b ? *a : *b; }
```

---

**基本写法：偏特化**
`template <typename <T>> class <类名><<T>*> { };`
```cpp
// 针对指针类型的偏特化
template <typename T>
class Stack<T*> {
    std::vector<T*> data;
};
```

---

## 可变参数模板

**基本写法：参数包**
`template <typename... <Args>>`
```cpp
// 接收任意数量类型
template <typename... Args>
void print(Args... args);
```

---

**基本写法：sizeof 计算参数数量**
`sizeof...(<参数包>)`
```cpp
// 获取包中元素个数
constexpr size_t n = sizeof...(Args);
```

---

## 模板元编程

**基本写法：编译期递归**
`template <int <N>> struct <名称> { static const int value = <N> * <名称><<N-1>>::value; };`
```cpp
// 编译期阶乘
template <int N>
struct Factorial {
    static const int value = N * Factorial<N - 1>::value;
};
```

---

**基本写法：递归终止特化**
`template <> struct <名称><0> { static const int value = 1; };`
```cpp
// 0 的阶乘为 1
template <>
struct Factorial<0> {
    static const int value = 1;
};
```

---

## 别名模板

**基本写法：类型别名**
`template <typename <T>> using <别名> = <类型><<T>>;`
```cpp
// 简化容器类型书写
template <typename T>
using Vec = std::vector<T>;
```

---

## 变量模板

**基本写法：变量模板**
`template <typename <T>> constexpr <类型> <名> = <值>;`
```cpp
// 编译期常量模板
template <typename T>
constexpr T pi = T(3.14159265358979);
```

---

## if constexpr

**基本写法：编译期条件分支**
`if constexpr (<条件>) { } else { }`
```cpp
// 编译期选择分支避免非法代码
if constexpr (std::is_integral_v<T>) {
    return x + 1;
} else {
    return x;
}
```
