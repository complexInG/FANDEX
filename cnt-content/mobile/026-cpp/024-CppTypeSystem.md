# C++ 类型系统

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## auto 与 decltype

**基本写法：自动类型推导**
`auto <变量> = <表达式>;`
```cpp
// 编译器推导变量类型
auto x = 42;       // int
auto y = 3.14;     // double
```

---

**基本写法：推导表达式类型**
`decltype(<表达式>) <变量> = <值>;`
```cpp
// 获取表达式的精确类型
int a = 0;
decltype(a) b = 1;
```

---

**基本写法：decltype(auto)**
`decltype(auto) <变量> = <表达式>;`
```cpp
// 保留引用与 cv 限定
decltype(auto) r = foo();
```

---

**基本写法：尾置返回类型**
`auto <函数名>(<参数>) -> <返回类型> { }`
```cpp
// 后置返回类型用于模板
auto f(int x) -> double { return x; }
```

---

## 引用类型

**基本写法：左值引用**
`<类型>& <变量> = <对象>;`
```cpp
// 绑定到左值
int a = 10;
int& ref = a;
```

---

**基本写法：右值引用**
`<类型>&& <变量> = <右值>;`
```cpp
// 绑定到右值支持移动语义
int&& rref = 42;
```

---

**基本写法：const 引用**
`const <类型>& <变量> = <值>;`
```cpp
// 可绑定到右值的常量引用
const int& cref = 100;
```

---

**基本写法：转发引用**
`template <typename <T>> void <函数名>(<T>&& <参数>);`
```cpp
// 模板中的万能引用
template <typename T>
void wrapper(T&& arg);
```

---

## 类型转换

**基本写法：static_cast**
`static_cast<<目标类型>>(<表达式>)`
```cpp
// 编译期安全转换
double d = static_cast<double>(3);
```

---

**基本写法：dynamic_cast**
`dynamic_cast<<目标指针>>(<基类指针>)`
```cpp
// 运行时多态向下转换
Derived* p = dynamic_cast<Derived*>(base_ptr);
```

---

**基本写法：const_cast**
`const_cast<<目标类型>>(<表达式>)`
```cpp
// 移除或添加 const 限定
int& r = const_cast<int&>(cref);
```

---

**基本写法：reinterpret_cast**
`reinterpret_cast<<目标类型>>(<表达式>)`
```cpp
// 位模式重解释
long n = reinterpret_cast<long>(ptr);
```

---

## cv 限定符

**基本写法：const 变量**
`const <类型> <变量> = <值>;`
```cpp
// 不可修改的常量
const int max_size = 100;
```

---

**基本写法：const 成员函数**
`<返回类型> <方法名>() const;`
```cpp
// 承诺不修改对象状态
int size() const { return n; }
```

---

**基本写法：constexpr 变量**
`constexpr <类型> <变量> = <常量表达式>;`
```cpp
// 编译期常量
constexpr int size = 10;
```

---

**基本写法：constexpr 函数**
`constexpr <返回类型> <函数名>(<参数>) { }`
```cpp
// 可在编译期求值的函数
constexpr int square(int x) { return x * x; }
```

---

## 类型别名

**基本写法：using 别名**
`using <别名> = <类型>;`
```cpp
// 现代类型别名语法
using String = std::string;
```

---

**基本写法：typedef 别名**
`typedef <类型> <别名>;`
```cpp
// 传统类型别名
typedef unsigned long ulong;
```

---

## 类型推断辅助

**基本写法：auto 与引用结合**
`auto& <变量> = <对象>;`
```cpp
// 推导为左值引用避免拷贝
auto& ref = container;
```

---

**基本写法：auto 与 const 结合**
`const auto& <变量> = <表达式>;`
```cpp
// 只读引用避免拷贝
const auto& item = vec[i];
```

---

## 强类型枚举

**基本写法：枚举类**
`enum class <名称> { <枚举值> };`
```cpp
// 作用域安全枚举
enum class Color { Red, Green, Blue };
```

---

**基本写法：指定底层类型**
`enum class <名称> : <整数类型> { };`
```cpp
// 指定底层类型为 uint8_t
enum class Flag : unsigned char { None = 0, All = 0xFF };
```

---

**基本写法：访问枚举值**
`<枚举名>::<枚举值>`
```cpp
// 使用作用域访问
Color c = Color::Red;
```
