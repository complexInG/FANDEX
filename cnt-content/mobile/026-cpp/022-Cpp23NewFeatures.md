# C++23 新特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Deducing this

**基本写法：显式对象参数**
`<返回类型> <方法名>(this <Self> <self>, <参数>);`
```cpp
// 一个方法同时支持 const 与非 const 调用
template <typename Self>
auto& get(this Self& self) {
    return self.value;
}
```

---

**基本写法：完美转发 self**
`auto&& <方法名>(this auto&& <self>) { return std::forward<decltype(<self>)>(<self>).<成员>; }`
```cpp
// 保留值类别以支持移动语义
template <typename Self>
auto&& data(this Self&& self) {
    return std::forward<Self>(self).data_;
}
```

---

**基本写法：CRTP 简化**
`void <方法名>(this auto&& <self>) { <self>.<实现>(); }`
```cpp
// 无需模板参数即可实现静态多态
struct Base {
    template <typename Self>
    void interface(this Self&& self) {
        self.impl();
    }
};
```

---

**基本写法：递归 lambda**
`auto <名> = [](this auto <self>, <参数>) { <body> };`
```cpp
// lambda 自身递归调用
auto factorial = [](this auto self, int n) -> int {
    return n <= 1 ? 1 : n * self(n - 1);
};
```

---

## std::expected

**基本写法：创建 expected**
`std::expected<<值类型>, <错误类型>> <变量>;`
```cpp
// 表示可能成功或失败的结果
std::expected<int, std::string> result = 42;
```

---

**基本写法：返回失败**
`return std::unexpected(<错误>);`
```cpp
// 返回错误对象
return std::unexpected("parse error");
```

---

**基本写法：检查是否有值**
`<result>.has_value()` 或 `static_cast<bool>(<result>)`
```cpp
// 判断 expected 是否持有成功值
if (result) { /* 使用 *result */ }
```

---

**基本写法：获取值**
`*<result>` 或 `<result>.value()`
```cpp
// 取出成功值
int v = *result;
```

---

**基本写法：获取错误**
`<result>.error()`
```cpp
// 取出错误对象
std::string err = result.error();
```

---

**基本写法：单子转换 transform**
`<result>.transform(<函数>)`
```cpp
// 成功时对值应用函数
auto doubled = result.transform([](int x) { return x * 2; });
```

---

**基本写法：失败处理 or_else**
`<result>.or_else(<函数>)`
```cpp
// 失败时应用函数
auto recovered = result.or_else([](std::string e) {
    return std::expected<int, std::string>(0);
});
```

---

## std::print

**基本写法：格式化输出**
`std::print(<格式串>, <参数>...);`
```cpp
// 不换行的格式化输出
std::print("x = {}", x);
```

---

**基本写法：换行输出**
`std::println(<格式串>, <参数>...);`
```cpp
// 自动换行的格式化输出
std::println("sum = {}", sum);
```

---

**基本写法：输出到文件流**
`std::print(<文件流>, <格式串>, <参数>...);`
```cpp
// 输出到指定流
std::print(std::cerr, "error: {}", msg);
```

---

## std::flat_map / std::flat_set

**基本写法：创建 flat_map**
`std::flat_map<<键>, <值>> <变量>;`
```cpp
// 基于连续存储的有序映射
std::flat_map<int, std::string> m;
```

---

**基本写法：插入元素**
`<map>.insert({<键>, <值>});`
```cpp
// 插入键值对
m.insert({1, "one"});
```

---

## 其他常用特性

**基本写法：if consteval**
`if consteval { <编译时分支> } else { <运行时分支> }`
```cpp
// 判断是否在常量求值上下文
if consteval {
    return compile_impl();
} else {
    return runtime_impl();
}
```

---

**基本写法：多维下标运算符**
`<返回类型> operator[](<索引1>, <索引2>);`
```cpp
// 支持多维索引
int& operator[](size_t i, size_t j);
```

---

**基本写法：不可达声明**
`std::unreachable();`
```cpp
// 标记程序不应到达此处
throw std::logic_error("unreachable");
```

---

**基本写法：枚举底层值**
`std::to_underlying(<枚举值>)`
```cpp
// 获取枚举的底层整数值
int n = std::to_underlying(Color::Red);
```

---

**基本写法：字节序交换**
`std::byteswap(<整数>)`
```cpp
// 交换字节序用于端序转换
uint32_t be = std::byteswap(host_val);
```

---

**基本写法：assume 属性**
`[[assume(<条件>)]];`
```cpp
// 给编译器提供假设以辅助优化
[[assume(n > 0)]];
```
