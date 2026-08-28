# C++ RAII 资源管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## RAII 基本模式

**基本写法：构造函数获取资源**
`<类名>(<参数>) : <资源>{ <初始化> } { }`
```cpp
// 构造时获取资源
class FileGuard {
    FILE* fp;
public:
    FileGuard(const char* path) : fp(std::fopen(path, "r")) {}
};
```

---

**基本写法：析构函数释放资源**
`~<类名>() { <释放代码> }`
```cpp
// 析构时自动释放
~FileGuard() {
    if (fp) std::fclose(fp);
}
```

---

**基本写法：禁用拷贝**
`<类名>(const <类名>&) = delete;`
```cpp
// 防止资源被多次释放
FileGuard(const FileGuard&) = delete;
FileGuard& operator=(const FileGuard&) = delete;
```

---

**基本写法：支持移动**
`<类名>(<类名>&& <o>) noexcept : <成员>{<o>.<成员>} { <o>.<成员> = nullptr; }`
```cpp
// 转移资源所有权
FileGuard(FileGuard&& o) noexcept : fp(o.fp) {
    o.fp = nullptr;
}
```

---

**基本写法：移动赋值**
`<类名>& operator=(<类名>&& <o>) noexcept { }`
```cpp
// 释放旧资源再转移新资源
FileGuard& operator=(FileGuard&& o) noexcept {
    if (this != &o) {
        if (fp) std::fclose(fp);
        fp = o.fp;
        o.fp = nullptr;
    }
    return *this;
}
```

---

## lock_guard

**基本写法：作用域锁**
`std::lock_guard<<锁类型>> <变量>(<锁>);`
```cpp
// 进入作用域加锁离开解锁
std::mutex m;
std::lock_guard<std::mutex> lk(m);
```

---

**基本写法：带额外锁的 lock_guard**
`std::lock_guard<<锁类型>> <变量>(<锁>, std::adopt_lock);`
```cpp
// 假设锁已被持有仅管理析构解锁
std::lock(m1, m2);
std::lock_guard<std::mutex> lk1(m1, std::adopt_lock);
std::lock_guard<std::mutex> lk2(m2, std::adopt_lock);
```

---

## unique_lock

**基本写法：可灵活管理锁**
`std::unique_lock<<锁类型>> <变量>(<锁>);`
```cpp
// 支持延迟加锁与手动解锁
std::unique_lock<std::mutex> lk(m);
```

---

**基本写法：延迟加锁**
`std::unique_lock<<锁类型>> <变量>(<锁>, std::defer_lock);`
```cpp
// 构造时不加锁
std::unique_lock<std::mutex> lk(m, std::defer_lock);
lk.lock();
```

---

**基本写法：手动解锁**
`<锁变量>.unlock();`
```cpp
// 主动释放锁
lk.unlock();
```

---

**基本写法：转移锁所有权**
`std::move(<锁变量>);`
```cpp
// 转移 unique_lock 给另一变量
std::unique_lock<std::mutex> lk2 = std::move(lk1);
```

---

## scoped_lock

**基本写法：多锁同时加锁**
`std::scoped_lock <变量>(<锁1>, <锁2>);`
```cpp
// C++17 一次锁住多个互斥避免死锁
std::scoped_lock lk(m1, m2);
```

---

## 资源封装类模板

**基本写法：std::unique_ptr 管理**
`std::unique_ptr<<类型>> <变量>(new <类型>(<参数>));`
```cpp
// 独占所有权智能指针
std::unique_ptr<Widget> p(new Widget());
```

---

**基本写法：自定义删除器**
`std::unique_ptr<<类型>, <删除器类型>> <变量>(<指针>, <删除器>);`
```cpp
// 自定义资源释放逻辑
auto deleter = [](FILE* f) { if (f) std::fclose(f); };
std::unique_ptr<FILE, decltype(deleter)> fp(std::fopen("a.txt", "r"), deleter);
```

---

## 常见 RAII 容器

**基本写法：vector 自动管理**
`std::vector<<类型>> <变量>;`
```cpp
// 动态数组自动释放内存
std::vector<int> v(100);
```

---

**基本写法：string 自动管理**
`std::string <变量>;`
```cpp
// 字符串自动管理字符缓冲
std::string s = "hello";
```

---

**基本写法：fstream 自动管理**
`std::ifstream <变量>(<文件名>);`
```cpp
// 文件流析构自动关闭
std::ifstream in("data.txt");
```
