# C++ 智能指针进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## unique_ptr 进阶

**基本写法：自定义删除器**
`std::unique_ptr<<类型>, <删除器类型>>`
```cpp
// 函数指针删除器
auto fileDeleter = [](FILE* f){ if (f) fclose(f); };
std::unique_ptr<FILE, decltype(fileDeleter)> fp(fopen("a.txt", "r"), fileDeleter);

// 仿函数删除器
struct FreeDeleter {
    void operator()(void* p) const { std::free(p); }
};
std::unique_ptr<int, FreeDeleter> up((int*)std::malloc(4));
```

---

**基本写法：数组特化**
`std::unique_ptr<<类型>[]>`
```cpp
// 动态数组
std::unique_ptr<int[]> arr(new int[100]);
arr[0] = 42; // 支持 operator[]
// 推荐：用 std::vector 替代
std::vector<int> v(100);
```

---

**基本写法：make_unique**
`std::make_unique<<类型>>(<参数>...)`
```cpp
// 工厂函数创建
auto p = std::make_unique<Widget>(42);
auto arr = std::make_unique<int[]>(100); // 数组
// 异常安全：避免裸 new
```

---

**基本写法：release 释放所有权**
`<ptr>.release()`
```cpp
// 释放并返回裸指针
auto p = std::make_unique<Widget>();
Widget* raw = p.release(); // p 变空，调用者负责删除
delete raw;
```

---

**基本写法：reset 重置**
`<ptr>.reset(<新指针>)`
```cpp
// 替换管理的对象
auto p = std::make_unique<Widget>();
p.reset(new Widget()); // 删除旧对象，管理新对象
p.reset();             // 删除对象，变空
```

---

## shared_ptr 进阶

**基本写法：make_shared 优势**
`std::make_shared<<类型>>(<参数>...)`
```cpp
// make_shared 一次分配（对象+控制块）
auto p = std::make_shared<Widget>(42);
// shared_ptr<Widget>(new Widget) 两次分配，且非异常安全
```

---

**基本写法：控制块**
`<ptr>.use_count()` `<ptr>.unique()`
```cpp
// 引用计数查询
auto p = std::make_shared<Widget>();
auto q = p;
std::cout << p.use_count(); // 2
// C++17 起 unique() 已弃用
```

---

**基本写法：自定义删除器（shared）**
`std::shared_ptr<<类型>>(<裸指针>, <删除器>)`
```cpp
// shared_ptr 自定义删除器（运行时开销）
std::shared_ptr<FILE> fp(fopen("a.txt", "r"),
    [](FILE* f){ if (f) fclose(f); });
// 删除器存储在控制块，类型不影响 shared_ptr 类型
```

---

**基本写法：enable_shared_from_this**
`std::enable_shared_from_this<<类型>>`
```cpp
// 在成员函数中安全获取 shared_ptr
struct Node : std::enable_shared_from_this<Node> {
    std::shared_ptr<Node> getSelf() {
        return shared_from_this(); // 安全共享
        // return std::shared_ptr<Node>(this); // 错误：双重管理
    }
};
```

---

**基本写法：aliasing 构造**
`std::shared_ptr<<类型>>(<其他shared>, <裸指针>)`
```cpp
// 共享所有权但指向不同对象
auto pair = std::make_shared<std::pair<int,int>>(1, 2);
std::shared_ptr<int> first(pair, &pair->first);
// first 共享 pair 的计数，但指向 first 成员
```

---

## weak_ptr 进阶

**基本写法：构造与提升**
`std::weak_ptr<<类型>> <变量>(<shared>)`
```cpp
// 弱引用
auto sp = std::make_shared<Widget>(42);
std::weak_ptr<Widget> wp = sp;
// 提升为 shared_ptr
if (auto p = wp.lock()) {
    use(*p); // 对象仍存活
}
// 直接构造可能抛异常
// std::shared_ptr<Widget> p(wp); // 若失效抛 bad_weak_ptr
```

---

**基本写法：owner_before**
`<weak>.owner_before(<其他>)`
```cpp
// 比较所有权（用于排序/关联容器键）
auto sp1 = std::make_shared<int>(1);
auto sp2 = std::make_shared<int>(2);
std::weak_ptr<int> w1 = sp1, w2 = sp1; // 同一控制块
bool same = !w1.owner_before(w2) && !w2.owner_before(w1); // true
```

---

## 分配器与智能指针

**基本写法：allocate_shared**
`std::allocate_shared<<类型>>(<分配器>, <参数>...)`
```cpp
// 使用自定义分配器
std::allocator<Widget> alloc;
auto p = std::allocate_shared<Widget>(alloc, 42);
```

---

## 类型转换

**基本写法：static_pointer_cast**
`std::static_pointer_cast<<目标>>(<智能指针>)`
```cpp
// 智能指针类型转换
auto derived = std::make_shared<Derived>();
std::shared_ptr<Base> base = std::static_pointer_cast<Base>(derived);
// 动态转换
std::shared_ptr<Derived> d = std::dynamic_pointer_cast<Derived>(base);
// const 转换
std::shared_ptr<Widget> p = std::const_pointer_cast<Widget>(constPtr);
```

---

## 内存布局

**基本写法：make_shared 内存优化**
`对象与控制块同一次分配`
```cpp
// make_shared：1 次分配
auto p = std::make_shared<Widget>();
// [控制块][Widget] 连续内存
// shared_ptr(new Widget)：2 次分配
std::shared_ptr<Widget> q(new Widget);
// 缺点：make_shared 的内存在 weak_ptr 存活时不释放
```

---

## 最佳实践

**基本写法：选用决策**
`unique_ptr > shared_ptr > weak_ptr`
```cpp
// 1. 默认用 unique_ptr
auto p = std::make_unique<Widget>();
// 2. 需要共享所有权时用 shared_ptr
auto sp = std::make_shared<Widget>();
// 3. 观察不拥有用 weak_ptr
std::weak_ptr<Widget> wp = sp;
// 4. 函数参数传 const& 或值
void use(const std::shared_ptr<Widget>& p); // 不增计数
void take(std::unique_ptr<Widget> p);       // 转移所有权
```
