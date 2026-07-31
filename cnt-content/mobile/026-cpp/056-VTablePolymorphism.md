# C++ 虚函数表与多态内存布局

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 虚函数表基础

**基本写法：含虚函数的对象布局**
`struct <类> { virtual void <方法>(); };`
```cpp
// 含虚函数的类，对象首部有虚表指针
struct Base {
    int x;
    virtual void f() {}
    virtual ~Base() = default;
};
// 内存布局（64 位）：
// [vptr][int x]
// vptr 指向虚函数表
```

---

**基本写法：虚表工作原理**
`<对象>.vptr → <虚表> → <函数地址>`
```cpp
// 虚函数调用过程
struct Base { virtual void f() { std::cout << "B"; } };
struct Derived : Base { void f() override { std::cout << "D"; } };

Base* p = new Derived;
p->f(); // 1. 取 p->vptr
        // 2. 查虚表 f 的槽位
        // 3. 调用 Derived::f
```

---

## 多继承虚表

**基本写法：多继承的虚表**
`struct <类> : <基类1>, <基类2> {}`
```cpp
// 多继承有多个 vptr
struct A { virtual void fa() {} };
struct B { virtual void fb() {} };
struct C : A, B {
    void fa() override {}
    void fb() override {}
};
// C 对象内存：[vptr_A][vptr_B]
// 两个虚表指针分别指向 A、B 的虚表
```

---

## 虚析构函数

**基本写法：虚析构保证正确释放**
`virtual ~<类>() = default;`
```cpp
// 基类析构必须是虚函数
struct Base {
    virtual ~Base() = default; // 关键
    virtual void f() = 0;
};
struct Derived : Base {
    ~Derived() override { /* 释放资源 */ }
};
Base* p = new Derived;
delete p; // 虚析构保证调用 Derived::~Derived
```

---

## RTTI 与 type_info

**基本写法：type_info 存储**
`typeid(<对象>)` 返回 type_info
```cpp
// 虚表相关联的 RTTI 信息
struct Base { virtual ~Base() = default; };
struct Derived : Base {};
Base* p = new Derived;
// typeid 通过 vptr 找到 RTTI
const std::type_info& ti = typeid(*p);
std::cout << ti.name(); // 类型名
```

---

## final 优化

**基本写法：final 去虚化**
`<方法> final` 或 `<类> final`
```cpp
// final 允许编译器去虚化
struct Base { virtual void f(); };
struct Derived final : Base {
    void f() override; // 可去虚化
};
Derived d;
d.f(); // 编译器可直接调用（非虚调用）
```

---

## 内存对齐

**基本写法：查看对象大小**
`sizeof(<类>)`
```cpp
// 含虚函数的类大小
struct NoVirtual { int x; };           // sizeof = 4
struct WithVirtual { int x; virtual void f(){} }; // sizeof = 16（vptr+int+padding）
// 64 位下 vptr 为 8 字节
```

---

**基本写法：alignas 指定对齐**
`struct alignas(<n>) <类> {};`
```cpp
// 自定义对齐
struct alignas(64) CacheLine {
    int data[16];
};
// 强制 64 字节对齐（缓存行大小）
```

---

## 纯虚函数调用

**基本写法：纯虚函数实现**
`<返回> <方法>() = 0;` 可有实现
```cpp
// 纯虚函数也可以有实现
struct Base {
    virtual void f() = 0; // 纯虚
};
void Base::f() { std::cout << "base impl"; } // 实现
struct Derived : Base {
    void f() override { Base::f(); } // 调用基类实现
};
```

---

## 构造与析构中的虚函数

**基本写法：构造时虚函数不生效**
`<构造函数> 中调用虚函数调用本类版本`
```cpp
// 构造/析构中虚函数退化为当前类版本
struct Base {
    Base() { f(); } // 调用 Base::f，非 Derived::f
    virtual void f() { std::cout << "B"; }
};
struct Derived : Base {
    void f() override { std::cout << "D"; }
};
Derived d; // 构造时打印 "B"（不是 "D"）
```

---

## 多态性能

**基本写法：虚调用开销**
`虚调用有间接寻址开销`
```cpp
// 虚函数调用：2 次内存访问 + 1 次间接调用
// 非虚函数：1 次直接调用
// 现代 CPU 分支预测可缓解
// 热点路径考虑 CRTP 或 final 去虚化
struct Base { virtual int compute() = 0; };
// CRTP 替代方案
template <typename D>
struct CRTPBase { int compute() { return static_cast<D*>(this)->computeImpl(); } };
```
