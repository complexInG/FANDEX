# C++ 智能指针循环引用

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 循环引用问题

**基本写法：shared_ptr 循环引用**
`a->b, b->a 导致内存泄漏`
```cpp
// 循环引用导致无法释放
struct Node {
    std::shared_ptr<Node> next;
    ~Node() { std::cout << "destroyed"; }
};
auto a = std::make_shared<Node>();
auto b = std::make_shared<Node>();
a->next = b; // a 引用 b
b->next = a; // b 引用 a
// 离开作用域后：a 引用计数 1（b 持有），b 引用计数 1（a 持有）
// 析构函数不会被调用！内存泄漏
```

---

## weak_ptr 解决方案

**基本写法：用 weak_ptr 打破循环**
`std::weak_ptr<<类型>> <变量>`
```cpp
// 用 weak_ptr 持有不拥有
struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;     // 弱引用，不增加计数
    ~Node() { std::cout << "destroyed"; }
};
auto a = std::make_shared<Node>();
auto b = std::make_shared<Node>();
a->next = b;      // b 引用计数 +1
b->prev = a;      // a 引用计数不变
// 离开作用域后正常析构
```

---

## weak_ptr 使用

**基本写法：lock 提升**
`<weak>.lock()` 返回 shared_ptr 或空
```cpp
// 使用前检查有效性
std::weak_ptr<Widget> wp = sp;
if (auto p = wp.lock()) {
    // 提升成功，对象仍存活
    p->doWork();
} else {
    // 对象已被释放
}
```

---

**基本写法：expired 检查**
`<weak>.expired()` 判断是否失效
```cpp
// 检查是否过期
std::weak_ptr<Widget> wp = sp;
sp.reset(); // 释放
if (wp.expired()) {
    std::cout << "对象已销毁";
}
```

---

**基本写法：use_count 查看计数**
`<weak>.use_count()`
```cpp
// 查看引用计数
auto sp = std::make_shared<Widget>();
std::weak_ptr<Widget> wp = sp;
std::cout << wp.use_count(); // 1
auto sp2 = sp;
std::cout << wp.use_count(); // 2
```

---

## 常见循环场景

**基本写法：父子关系**
`父持 shared_ptr 子，子持 weak_ptr 父`
```cpp
// 父子结构：父拥有子，子弱引用父
struct Parent;
struct Child {
    std::weak_ptr<Parent> parent; // 弱引用
    void useParent() {
        if (auto p = parent.lock()) { /* 安全使用 */ }
    }
};
struct Parent {
    std::vector<std::shared_ptr<Child>> children; // 强引用
};
```

---

**基本写法：观察者模式**
`被观察者持 shared_ptr，观察者持 weak_ptr`
```cpp
// 事件订阅避免延长生命周期
struct Event;
struct Listener {
    std::weak_ptr<Event> event; // 不阻止 event 释放
};
struct Event {
    std::vector<std::shared_ptr<Listener>> listeners;
};
```

---

**基本写法：双向链表**
`一方向 shared_ptr，另一方向 weak_ptr`
```cpp
// 双向链表：next 用 shared，prev 用 weak
struct Node {
    std::shared_ptr<Node> next;
    std::weak_ptr<Node> prev;
};
```

---

## enable_shared_from_this

**基本写法：安全获取自身 shared_ptr**
`std::enable_shared_from_this<<类型>>`
```cpp
// 在类内安全获取指向自己的 shared_ptr
struct Widget : std::enable_shared_from_this<Widget> {
    std::shared_ptr<Widget> getPtr() {
        return shared_from_this(); // 安全
        // return std::shared_ptr<Widget>(this); // 错误：双重释放
    }
};
auto w = std::make_shared<Widget>();
auto w2 = w->getPtr(); // 与 w 共享计数
```

---

**基本写法：weak_from_this**
`weak_from_this()`
```cpp
// C++17 获取 weak_ptr，避免增加计数
struct Widget : std::enable_shared_from_this<Widget> {
    std::weak_ptr<Widget> getWeak() {
        return weak_from_this();
    }
};
```

---

## 检测与调试

**基本写法：检查泄漏**
`use_count 长期不归零`
```cpp
// 调试循环引用
// 1. 析构函数加日志，检查是否调用
struct Watched {
    ~Watched() { std::cout << "freed"; }
};
// 2. 用 valgrind 检测泄漏
// valgrind --leak-check=full ./app
// 3. 用 AddressSanitizer
// g++ -fsanitize=address
```
