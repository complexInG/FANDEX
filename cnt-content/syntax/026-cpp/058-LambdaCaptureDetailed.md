# C++ Lambda 捕获详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 捕获方式

**基本写法：值捕获**
`[<变量>] { ... }`
```cpp
// 值捕获：拷贝一份
int x = 10;
auto f = [x] { return x; }; // 捕获 x 的副本
// f 中 x 为 10，与外部 x 解耦
```

---

**基本写法：引用捕获**
`[&<变量>] { ... }`
```cpp
// 引用捕获：共享同一变量
int x = 10;
auto f = [&x] { x = 20; };
f();
std::cout << x; // 20，外部被修改
```

---

**基本写法：全部值捕获**
`[=] { ... }`
```cpp
// 捕获所有用到的变量（值）
int a = 1, b = 2;
auto f = [=] { return a + b; }; // 3
// 所有变量拷贝
```

---

**基本写法：全部引用捕获**
`[&] { ... }`
```cpp
// 捕获所有用到的变量（引用）
int a = 1, b = 2;
auto f = [&] { a = 10; b = 20; };
f();
// a=10, b=20
```

---

## 混合捕获

**基本写法：混合捕获**
`[=, &<变量>]` 或 `[&, <变量>]`
```cpp
// 默认值捕获，特定变量引用
int a = 1, b = 2, c = 3;
auto f = [=, &c] {
    // a, b 值捕获
    c = a + b; // c 引用捕获
};
```

---

**基本写法：this 捕获**
`[this] { ... }`
```cpp
// 捕获 this 指针
struct Widget {
    int x = 42;
    auto getCallback() {
        return [this] { return x; }; // 访问成员
    }
};
```

---

**基本写法：捕获初始化（C++14）**
`[<名> = <表达式>]`
```cpp
// 在捕获中初始化新变量
auto f = [p = std::make_unique<int>(42)] {
    return *p;
};
// p 是 lambda 内的 unique_ptr
```

---

**基本写法：捕获移动（C++14）**
`[<名> = std::move(<变量>)]`
```cpp
// 移动捕获
auto ptr = std::make_unique<int>(42);
auto f = [p = std::move(ptr)] {
    return *p;
};
// ptr 已被移动，p 持有资源
```

---

## 泛型 Lambda

**基本写法：auto 参数（C++14）**
`[](auto <参数>) { ... }`
```cpp
// 泛型 lambda
auto add = [](auto a, auto b) { return a + b; };
add(1, 2);       // int
add(1.0, 2.0);   // double
add(std::string("a"), std::string("b")); // string
```

---

**基本写法：模板参数（C++20）**
`[]<typename T>(T <参数>) { ... }`
```cpp
// C++20 显式模板参数
auto f = []<typename T>(std::vector<T> const& v) {
    return v.size();
};
std::vector<int> vi{1,2,3};
f(vi); // 3
```

---

## 可变 Lambda

**基本写法：mutable**
`[<捕获>] (<参数>) mutable { ... }`
```cpp
// 允许修改值捕获的副本
int x = 10;
auto f = [x]() mutable {
    return ++x; // 修改副本
};
f(); // 11
f(); // 12
std::cout << x; // 10（外部不变）
```

---

## 递归 Lambda

**基本写法：std::function 递归**
`std::function<<签名>> <名> = ...;`
```cpp
// 用 std::function 实现递归
std::function<int(int)> fact = [&](int n) {
    return n <= 1 ? 1 : n * fact(n - 1);
};
fact(5); // 120
```

---

**基本写法：泛型 lambda 递归（C++14）**
`auto <名> = [](auto& self, ...) { ... };`
```cpp
// 传递自身实现递归
auto fact = [](auto& self, int n) -> int {
    return n <= 1 ? 1 : n * self(self, n - 1);
};
fact(fact, 5); // 120
```

---

## Lambda 与返回类型

**基本写法：尾随返回类型**
`[](...) -> <类型> { ... }`
```cpp
// 显式指定返回类型
auto f = [](int x) -> double {
    if (x < 0) return 0.0;
    return std::sqrt(x);
};
```

---

**基本写法：无返回值**
`[](...) -> void { ... }`
```cpp
// 显式 void 返回
auto log = [](const std::string& msg) -> void {
    std::cout << msg << "\n";
};
```

---

## 存储与传递

**基本写法：存入 std::function**
`std::function<<签名>> <变量> = <lambda>;`
```cpp
// 持有 lambda
std::function<int(int, int)> op = [](int a, int b){ return a + b; };
op(2, 3); // 5
```

---

**基本写法：模板参数传递（零开销）**
`template <typename F> void <函数>(F <回调>)`
```cpp
// 模板参数避免 std::function 开销
template <typename F>
void forEach(std::vector<int>& v, F callback) {
    for (auto& x : v) callback(x);
}
forEach(v, [](int& x){ x *= 2; });
```
