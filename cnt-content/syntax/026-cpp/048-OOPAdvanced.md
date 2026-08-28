# C++ OOP 进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 虚函数与多态

**基本写法：虚函数与 override**
`virtual <返回> <方法>() [const] [override];`
```cpp
// 动态多态基础
struct Animal {
    virtual void speak() const { std::cout << "..."; }
    virtual ~Animal() = default; // 虚析构
};
struct Dog : Animal {
    void speak() const override { std::cout << "woof"; }
};
Animal* a = new Dog;
a->speak(); // 调用 Dog::speak
```

---

**基本写法：纯虚函数与抽象类**
`virtual <返回> <方法>() = 0;`
```cpp
// 含纯虚函数的类不可实例化
struct Shape {
    virtual double area() const = 0; // 纯虚
    virtual ~Shape() = default;
};
// Shape s; // 错误：抽象类
struct Circle : Shape {
    double r;
    double area() const override { return 3.14 * r * r; }
};
```

---

**基本写法：final 禁止覆盖/继承**
`<类> final` 或 `<方法> final`
```cpp
// 禁止进一步继承
struct Base final {};
// struct Derived : Base {}; // 错误

struct A {
    virtual void f() final; // 禁止子类覆盖
};
```

---

## 多重继承

**基本写法：多继承**
`struct <类> : <访问> <基类1>, <访问> <基类2> ...`
```cpp
// 一个类继承多个基类
struct Drawable { virtual void draw() = 0; virtual ~Drawable() = default; };
struct Clickable { virtual void click() = 0; virtual ~Clickable() = default; };
struct Button : Drawable, Clickable {
    void draw() override {}
    void click() override {}
};
```

---

**基本写法：虚继承解决菱形**
`virtual <访问> <基类>`
```cpp
// 菱形继承：虚继承避免二义性
struct Base { int value; };
struct A : virtual Base {};
struct B : virtual Base {};
struct C : A, B {
    // 只有一份 Base::value
};
```

---

## CRTP 静态多态

**基本写法：CRTP 模式**
`template <typename <派生>> struct <基类> { ... };`
```cpp
// 奇异递归模板模式（编译期多态）
template <typename Derived>
struct Shape {
    double area() { return static_cast<Derived*>(this)->areaImpl(); }
};
struct Circle : Shape<Circle> {
    double areaImpl() { return 3.14 * r * r; }
    double r;
};
Circle c; c.r = 2;
c.area(); // 编译期分发，无虚函数开销
```

---

## 对象生命周期

**基本写法：构造/析构顺序**
`基类构造 → 成员构造 → 派生类构造 → 派生类析构 → 成员析构 → 基类析构`
```cpp
struct Base { Base(){ log("B+"); } ~Base(){ log("B-"); } };
struct Member { Member(){ log("M+"); } ~Member(){ log("M-"); } };
struct Derived : Base {
    Member m;
    Derived(){ log("D+"); }
    ~Derived(){ log("D-"); }
};
// 构造 Derived 时输出：B+ M+ D+
// 析构时输出：D- M- B-
```

---

**基本写法：委托构造**
`<类>(<参数>) : <类>(<其他参数>) {}`
```cpp
// 构造函数调用另一构造函数
struct Point {
    int x, y;
    Point() : Point(0, 0) {}          // 委托
    Point(int a) : Point(a, 0) {}     // 委托
    Point(int a, int b) : x(a), y(b) {}
};
```

---

**基本写法：继承构造**
`using <基类>::<基类>;`
```cpp
// C++11 继承基类构造函数
struct Base {
    Base(int);
    Base(int, int);
};
struct Derived : Base {
    using Base::Base; // 继承所有构造函数
};
```

---

## 拷贝与移动控制

**基本写法：Rule of Five**
`<类>(const <类>&); <类>(<类>&&); operator=; ~<类>();`
```cpp
// 自定义资源管理时需定义五个
struct Buffer {
    int* data; size_t size;
    Buffer(size_t n) : data(new int[n]), size(n) {}
    ~Buffer() { delete[] data; }
    Buffer(const Buffer& o) : data(new int[o.size]), size(o.size) {
        std::copy(o.data, o.data+size, data);
    }
    Buffer& operator=(const Buffer& o) {
        Buffer tmp(o); swap(tmp); return *this;
    }
    Buffer(Buffer&& o) noexcept : data(o.data), size(o.size) {
        o.data = nullptr; o.size = 0;
    }
    Buffer& operator=(Buffer&& o) noexcept {
        swap(o); return *this;
    }
    void swap(Buffer& o) noexcept {
        std::swap(data, o.data); std::swap(size, o.size);
    }
};
```

---

**基本写法：Rule of Zero**
`<类>() = default;`
```cpp
// 让编译器自动生成，最简
struct Widget {
    std::vector<int> v;
    std::string name;
    std::unique_ptr<int> p;
    // 无需定义任何特殊成员函数
};
```

---

## 运行时类型信息

**基本写法：typeid 与 dynamic_cast**
`typeid(<对象>)` `dynamic_cast<<派生>*>(<基类*>)`
```cpp
// RTTI 需要虚函数支持
struct Base { virtual ~Base() = default; };
struct Derived : Base { void special() {} };

Base* p = new Derived;
if (typeid(*p) == typeid(Derived)) { /* 类型匹配 */ }
if (Derived* d = dynamic_cast<Derived*>(p)) { d->special(); }
```

---

## 接口设计

**基本写法：NVI 非虚接口**
`public: <接口方法> final { <调用私有虚函数>; }`
```cpp
// 公开非虚方法，私有虚函数实现
struct Widget {
    void work() final {     // 公开接口固定
        beforeWork();
        doWork();            // 私有可覆盖
        afterWork();
    }
    virtual ~Widget() = default;
private:
    virtual void doWork() = 0;
    void beforeWork() {}
    void afterWork() {}
};
```
