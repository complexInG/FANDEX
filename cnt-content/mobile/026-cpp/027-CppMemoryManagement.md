# C++ 内存管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## new 与 delete

**基本写法：堆上分配对象**
`<类型>* <指针> = new <类型>(<参数>);`
```cpp
// 动态创建单个对象
int* p = new int(42);
```

---

**基本写法：释放单个对象**
`delete <指针>;`
```cpp
// 释放堆内存
delete p;
```

---

**基本写法：分配数组**
`<类型>* <指针> = new <类型>[<数量>];`
```cpp
// 动态创建对象数组
int* arr = new int[10];
```

---

**基本写法：释放数组**
`delete[] <指针>;`
```cpp
// 释放数组内存
delete[] arr;
```

---

**基本写法：placement new**
`new (<地址>) <类型>(<参数>);`
```cpp
// 在指定内存构造对象
char buf[sizeof(Widget)];
new (buf) Widget();
```

---

**基本写法：手动调用析构**
`<指针>->~<类型>();`
```cpp
// 析构但不释放内存
w->~Widget();
```

---

## 内存分配器

**基本写法：使用 allocator**
`std::allocator<<类型>> <变量>;`
```cpp
// 标准分配器
std::allocator<int> alloc;
```

---

**基本写法：分配未构造内存**
`<alloc>.allocate(<数量>);`
```cpp
// 仅分配内存不构造对象
int* mem = alloc.allocate(5);
```

---

**基本写法：构造对象**
`std::construct_at(<地址>, <参数>);`
```cpp
// 在内存上构造对象
std::construct_at(mem, 42);
```

---

**基本写法：销毁对象**
`std::destroy_at(<指针>);`
```cpp
// 调用析构不释放内存
std::destroy_at(mem);
```

---

**基本写法：释放内存**
`<alloc>.deallocate(<指针>, <数量>);`
```cpp
// 释放分配的内存
alloc.deallocate(mem, 5);
```

---

## 智能指针

**基本写法：独占指针**
`std::unique_ptr<<类型>> <变量> = std::make_unique<<类型>>(<参数>);`
```cpp
// 独占所有权
auto p = std::make_unique<Widget>(args);
```

---

**基本写法：共享指针**
`std::shared_ptr<<类型>> <变量> = std::make_shared<<类型>>(<参数>);`
```cpp
// 引用计数共享所有权
auto sp = std::make_shared<Widget>(args);
```

---

**基本写法：弱引用**
`std::weak_ptr<<类型>> <变量> = <shared_ptr>;`
```cpp
// 不影响引用计数的弱引用
std::weak_ptr<Widget> wp = sp;
```

---

**基本写法：从 weak 提升为 shared**
`<weak_ptr>.lock();`
```cpp
// 提升为 shared_ptr 检查有效性
if (auto p = wp.lock()) { /* 使用 p */ }
```

---

**基本写法：自定义删除器**
`std::shared_ptr<<类型>> <变量>(<指针>, <删除器>);`
```cpp
// 数组与自定义释放
std::shared_ptr<int> sp(new int[10], std::default_delete<int[]>());
```

---

## 内存对齐

**基本写法：指定对齐**
`alignas(<对齐值>) <类型> <变量>;`
```cpp
// 指定变量对齐到 16 字节
alignas(16) float data[4];
```

---

**基本写法：查询对齐**
`alignof(<类型>)`
```cpp
// 获取类型的对齐要求
size_t a = alignof(double);
```

---

**基本写法：对齐分配**
`std::aligned_alloc(<对齐>, <大小>);`
```cpp
// 分配对齐内存 C11
void* p = std::aligned_alloc(64, 1024);
```

---

## 低级内存操作

**基本写法：复制内存**
`std::memcpy(<目标>, <源>, <字节数>);`
```cpp
// 复制字节块
std::memcpy(dst, src, n * sizeof(int));
```

---

**基本写法：移动内存**
`std::memmove(<目标>, <源>, <字节数>);`
```cpp
// 支持重叠区域的复制
std::memmove(dst, src, n);
```

---

**基本写法：填充内存**
`std::memset(<目标>, <值>, <字节数>);`
```cpp
// 将内存清零
std::memset(buf, 0, sizeof(buf));
```

---

## 自定义 operator new

**基本写法：类专属 new**
`static void* operator new(size_t <大小>);`
```cpp
// 为类定制内存分配
static void* operator new(size_t sz) {
    return std::malloc(sz);
}
```

---

**基本写法：类专属 delete**
`static void operator delete(void* <指针>);`
```cpp
// 配套的释放函数
static void operator delete(void* p) {
    std::free(p);
}
```
