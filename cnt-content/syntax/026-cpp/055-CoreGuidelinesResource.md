# C++ 核心指南资源管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## RAII 原则

**基本写法：RAII 资源获取即初始化**
`struct <类> { <资源> res; ~<类>() { <释放>; } };`
```cpp
// 构造获取，析构释放
struct FileRAII {
    FILE* fp;
    explicit FileRAII(const char* path) : fp(std::fopen(path, "r")) {
        if (!fp) throw std::runtime_error("open failed");
    }
    ~FileRAII() { if (fp) std::fclose(fp); }
    FileRAII(const FileRAII&) = delete;
    FileRAII& operator=(const FileRAII&) = delete;
};
```

---

**基本写法：make_unique 工厂**
`std::make_unique<<类型>>(<参数>...)`
```cpp
// 推荐用工厂函数创建智能指针
auto p = std::make_unique<Widget>(42);
// 异常安全：避免裸 new
// std::unique_ptr<Widget> p(new Widget(42)); // 不推荐
```

---

## 智能指针选择

**基本写法：unique_ptr 独占**
`std::unique_ptr<<类型>>`
```cpp
// 默认首选 unique_ptr
std::unique_ptr<Widget> p = std::make_unique<Widget>();
// 转移所有权
std::unique_ptr<Widget> q = std::move(p);
// 自定义删除器
auto deleter = [](FILE* f){ if (f) fclose(f); };
std::unique_ptr<FILE, decltype(deleter)> fp(fopen("a", "r"), deleter);
```

---

**基本写法：shared_ptr 共享**
`std::shared_ptr<<类型>>`
```cpp
// 多个所有者共享
auto p = std::make_shared<Widget>();
std::shared_ptr<Widget> q = p; // 引用计数 +1
// 注意：有原子操作开销
```

---

**基本写法：weak_ptr 打破循环**
`std::weak_ptr<<类型>>`
```cpp
// 观察但不拥有
auto sp = std::make_shared<Widget>();
std::weak_ptr<Widget> wp = sp;
// 使用前提升
if (auto locked = wp.lock()) {
    locked->doWork();
}
```

---

## 资源管理规则

**基本写法：R.1 自动管理**
`用 RAII 自动管理资源`
```cpp
// R.1: 不要手动管理资源
// 错误：裸 new/delete
// Widget* w = new Widget; ... delete w;
// 正确：智能指针
auto w = std::make_unique<Widget>();
```

---

**基本写法：R.11 避免显式 new/delete**
`std::make_unique` / `std::make_shared`
```cpp
// R.11: 避免显式调用 new 和 delete
auto p = std::make_unique<int[]>(100); // 数组
auto s = std::make_shared<Widget>();
// 容器自动管理
std::vector<Widget> v(100);
```

---

**基本写法：R.23 sort 自定义**
`sort 用 lambda 比自定义类型更简单`
```cpp
// R.23: 用 lambda 而非函数对象
std::sort(v.begin(), v.end(),
    [](const auto& a, const auto& b){ return a.x < b.x; });
```

---

## 容器与所有权

**基本写法：容器持有对象**
`std::vector<<类型>>`
```cpp
// 容器自动管理元素生命周期
std::vector<Widget> widgets;
widgets.emplace_back(42); // 自动构造存储
// 容器销毁时元素自动销毁
```

---

**基本写法：容器持有指针**
`std::vector<std::unique_ptr<Widget>>`
```cpp
// 多态容器用智能指针
std::vector<std::unique_ptr<Animal>> zoo;
zoo.push_back(std::make_unique<Dog>());
zoo.push_back(std::make_unique<Cat>());
```

---

## 传递参数规则

**基本写法：F.15 排序规则**
`<类型> | const& | && | const*`
```cpp
// 参数传递指导
void inParam(const Widget& w);      // 输入：const 引用
void inParam(Widget w);             // 小类型或要拷贝：值传递
void outParam(Widget& w);           // 输出：引用
void ownParam(std::unique_ptr<Widget> w); // 转移所有权
void shareParam(std::shared_ptr<Widget> w); // 共享所有权
```

---

**基本写法：返回值规则**
`值返回 | unique_ptr | &`
```cpp
// 返回值指导
Widget makeWidget();                 // 返回值（RVO）
std::unique_ptr<Widget> makePtr();   // 返回多态对象
const std::vector<int>& getVec();    // 返回成员引用
std::string_view getName();          // 返回视图
```

---

## 异常安全

**基本写法：RAII 保证异常安全**
`auto <指针> = std::make_unique<...>();`
```cpp
// 即使抛异常，RAII 也会正确释放
void work() {
    auto file = std::make_unique<FileRAII>("a.txt");
    auto buf  = std::make_unique<char[]>(1024);
    riskyOp(); // 抛异常时 file、buf 自动释放
}
```

---

## GSL 指导库

**基本写法：gsl::owner 标注**
`gsl::owner<T*>`
```cpp
// 标注所有权
#include <gsl/gsl>
gsl::owner<int*> p = new int(42); // 标注拥有
delete p;
// gsl::not_null 确保非空
void f(gsl::not_null<Widget*> w);
```
