# C++ 完美转发与引用折叠

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 转发引用

**基本写法：模板中的万能引用**
`template <typename <T>> void <函数名>(<T>&& <参数>);`
```cpp
// 既可接受左值也可接受右值
template <typename T>
void wrapper(T&& arg);
```

---

**基本写法：auto&& 也是万能引用**
`auto&& <变量> = <表达式>;`
```cpp
// auto 推导配合 && 形成转发引用
auto&& ref = some_expr();
```

---

## std::forward

**基本写法：完美转发参数**
`std::forward<<T>>(<参数>)`
```cpp
// 保持参数的左右值属性转发
template <typename T>
void wrapper(T&& arg) {
    target(std::forward<T>(arg));
}
```

---

**基本写法：转发给构造函数**
`: <成员>(std::forward<<T>>(<参数>)) { }`
```cpp
// 转发初始化成员
template <typename T>
struct Holder {
    T data;
    template <typename U>
    Holder(U&& u) : data(std::forward<U>(u)) {}
};
```

---

**基本写法：转发多个参数**
`target(std::forward<<Args>>(<args>)...);`
```cpp
// 转发可变参数包
template <typename... Args>
void emplace(Args&&... args) {
    construct(std::forward<Args>(args)...);
}
```

---

## std::move

**基本写法：强制转为右值**
`std::move(<对象>)`
```cpp
// 触发移动语义
std::string s = "hi";
vec.push_back(std::move(s));
```

---

**基本写法：移动成员**
`<成员> = std::move(<其他>.<成员>);`
```cpp
// 转移资源所有权
String(String&& o) noexcept : data_(std::move(o.data_)) {}
```

---

## std::move_if_noexcept

**基本写法：条件移动**
`std::move_if_noexcept(<对象>)`
```cpp
// 移动构造非异常安全时退化为拷贝
auto x = std::move_if_noexcept(obj);
```

---

## 引用折叠规则

**基本写法：折叠为左值引用**
`<类型>& &` → `<类型>&`
```cpp
// 左值引用遇到左值引用折叠为左值引用
using R = int& &;   // 折叠为 int&
```

---

**基本写法：右值与右值折叠**
`<类型>&& &&` → `<类型>&&`
```cpp
// 两个右值引用折叠为右值引用
using R = int&& &&;  // 折叠为 int&&
```

---

**基本写法：任意左值参与折叠为左值**
`<类型>& &&` 或 `<类型>&& &` → `<类型>&`
```cpp
// 只要有一个左值引用就折叠为左值引用
using R = int& &&;   // 折叠为 int&
```

---

## 转发工厂函数

**基本写法：make_unique 转发**
`std::make_unique<<类型>>(<参数>...)`
```cpp
// 标准库通过完美转发构造对象
auto p = std::make_unique<Widget>(arg1, arg2);
```

---

**基本写法：emplace 系列转发**
`<容器>.emplace_back(<参数>...);`
```cpp
// 容器原地构造避免临时对象
vec.emplace_back(42, "name");
```

---

## 完美转发包装器

**基本写法：通用函数包装**
`template <typename F, typename... Args> auto <函数名>(F&& <f>, Args&&... <args>) { return std::forward<F>(<f>)(std::forward<Args>(<args>)...); }`
```cpp
// 包装可调用对象与参数
template <typename F, typename... Args>
auto invoke_wrap(F&& f, Args&&... args) {
    return std::forward<F>(f)(std::forward<Args>(args)...);
}
```

---

## as_const 转发

**基本写法：添加 const 左值引用**
`std::as_const(<对象>)`
```cpp
// 将对象转为 const 引用避免被修改
for (auto& item : std::as_const(container)) {
    // 只读访问
}
```

---

## 注意事项

**基本写法：不要转发多次**
`auto& <别名> = std::forward<<T>>(<参数>);  // 后续使用别名而非再次 forward`
```cpp
// 转发后的对象状态可能已被移动
template <typename T>
void wrapper(T&& arg) {
    target(std::forward<T>(arg));
    // 不要再次使用 arg，可能已被移动
}
```
