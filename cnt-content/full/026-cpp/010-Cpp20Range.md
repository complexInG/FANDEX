---
order: 55
title: C++20范围
module: cpp
category: C++
difficulty: advanced
description: Ranges库与视图组合
author: fanquanpp
updated: '2026-08-01'
related:
  - cpp/Lambda表达式
  - cpp/模板元编程
  - cpp/C++20模块
  - cpp/C++23与C++26新特性
prerequisites:
  - cpp/概述与现代标准
---

# C++20 Ranges 速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 概述

C++20 引入的 Ranges 库为标准库算法带来了范式级的变革。它将算法与数据源解耦，通过视图（View）实现惰性求值的链式管道操作，使数据处理代码更加声明式和高效。传统 STL 算法依赖迭代器对，而 Ranges 以"范围"为基本抽象，配合管道操作符 `|` 实现数据流的组合变换，代码可读性显著提升。

Ranges 的核心设计理念是：算法不应关心数据的存储方式，数据变换应该像流水线一样可组合。视图是轻量级的范围适配器，不会复制底层数据，仅在迭代时按需计算。

## 基础概念

### 范围（Range）

范围是对可迭代数据的抽象，任何提供 `begin()` 和 `end()` 的类型都是范围。C++20 通过 `std::ranges::range` 概念约束范围类型，包括容器、数组、初始化列表等。

### 视图（View）

视图是惰性求值的范围适配器，具有以下特性：

- 不拥有数据，仅引用底层范围
- 复制、赋值和销毁的复杂度为 O(1)
- 惰性求值，仅在迭代时才执行计算
- 可通过管道操作符 `|` 链式组合

### 常用视图一览

| 视图        | 说明                      |
| ----------- | ------------------------- |
| `filter`    | 根据谓词过滤元素          |
| `transform` | 对每个元素应用转换函数    |
| `take`      | 取前 n 个元素             |
| `drop`      | 跳过前 n 个元素           |
| `reverse`   | 反转元素顺序              |
| `sort`      | 排序（C++20 ranges 算法） |
| `unique`    | 去除连续重复元素          |
| `join`      | 展平嵌套范围              |
| `zip`       | 合并多个范围（C++23）     |
| `enumerate` | 带索引遍历（C++23）       |
| `chunk`     | 分块（C++23）             |
| `slide`     | 滑动窗口（C++23）         |

## 快速上手

### 管道式数据变换

```cpp
#include <ranges>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // 链式管道：过滤偶数 -> 平方 -> 取前5个
    auto result = nums
        | std::views::filter([](int n) { return n % 2 == 0; })
        | std::views::transform([](int n) { return n * n; })
        | std::views::take(5);

    for (int n : result) {
        std::cout << n << " ";  // 输出: 4 16 36 64 100
    }
    return 0;
}
```

### 使用 iota 生成序列

```cpp
#include <ranges>

// 生成 1 到 99 的整数序列
auto nums = std::views::iota(1, 100);

// 过滤偶数并求平方，取前5个
auto even_squared = nums
    | std::views::filter([](int n) { return n % 2 == 0; })
    | std::views::transform([](int n) { return n * n; })
    | std::views::take(5);

for (int n : even_squared) {
    std::cout << n << " ";  // 输出: 4 16 36 64 100
}
```

## 详细用法

### filter -- 条件过滤

```cpp
#include <ranges>
#include <vector>
#include <string>

struct Student {
    std::string name;
    int score;
};

int main() {
    std::vector<Student> students = {
        {"张三", 85}, {"李四", 62}, {"王五", 91}, {"赵六", 58}
    };

    // 筛选成绩及格的学生
    auto passed = students
        | std::views::filter([](const Student& s) { return s.score >= 60; });

    for (const auto& s : passed) {
        std::cout << s.name << ": " << s.score << std::endl;
    }
    return 0;
}
```

### transform -- 元素转换

```cpp
#include <ranges>
#include <vector>

int main() {
    std::vector<std::string> words = {"hello", "world", "cpp20"};

    // 转换为大写（简化示例，实际需逐字符转换）
    auto lengths = words
        | std::views::transform([](const std::string& s) { return s.size(); });

    for (size_t len : lengths) {
        std::cout << len << " ";  // 输出: 5 5 4
    }
    return 0;
}
```

### take 和 drop -- 截取与跳过

```cpp
#include <ranges>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> data = {10, 20, 30, 40, 50, 60, 70};

    // 取前3个
    auto first3 = data | std::views::take(3);
    for (int n : first3) std::cout << n << " ";  // 10 20 30
    std::cout << std::endl;

    // 跳过前3个
    auto skip3 = data | std::views::drop(3);
    for (int n : skip3) std::cout << n << " ";  // 40 50 60 70
    std::cout << std::endl;

    // 组合使用：取中间部分
    auto middle = data | std::views::drop(2) | std::views::take(3);
    for (int n : middle) std::cout << n << " ";  // 30 40 50
    return 0;
}
```

### reverse 和 keys/values

```cpp
#include <ranges>
#include <map>
#include <iostream>

int main() {
    std::map<std::string, int> scores = {
        {"语文", 90}, {"数学", 85}, {"英语", 92}
    };

    // 遍历键
    for (const auto& key : std::views::keys(scores)) {
        std::cout << key << " ";  // 数学 英语 语文（按字典序）
    }
    std::cout << std::endl;

    // 遍历值并反转
    auto reversed_values = std::views::values(scores) | std::views::reverse;
    for (int v : reversed_values) {
        std::cout << v << " ";  // 92 85 90
    }
    return 0;
}
```

### join -- 展平嵌套范围

```cpp
#include <ranges>
#include <vector>
#include <iostream>

int main() {
    std::vector<std::vector<int>> nested = {{1, 2}, {3, 4, 5}, {6}};

    // 展平为一维
    auto flat = nested | std::views::join;

    for (int n : flat) {
        std::cout << n << " ";  // 输出: 1 2 3 4 5 6
    }
    return 0;
}
```

## 常见场景

### 数据清洗管道

```cpp
#include <ranges>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> raw_data = {0, -3, 5, 0, 8, -1, 12, 0, 7};

    // 清洗流程：去除零值 -> 过滤负数 -> 排序 -> 去重
    auto cleaned = raw_data
        | std::views::filter([](int n) { return n != 0; })
        | std::views::filter([](int n) { return n > 0; });

    // 排序和去重需要复制到容器（sort 会修改原数据）
    std::vector<int> result(cleaned.begin(), cleaned.end());
    std::ranges::sort(result);
    result.erase(std::ranges::unique(result).begin(), result.end());

    for (int n : result) {
        std::cout << n << " ";  // 输出: 5 7 8 12
    }
    return 0;
}
```

### 字符串分割与处理

```cpp
#include <ranges>
#include <string>
#include <iostream>

int main() {
    std::string text = "hello world from cpp20 ranges";

    // 按空格分割字符串（C++20 lazy split）
    auto words = std::views::split(text, ' ');

    for (const auto& word : words) {
        // word 是一个子范围，需要构造为 string
        std::string s(word.begin(), word.end());
        std::cout << s << std::endl;
    }
    return 0;
}
```

## 注意事项

- 视图是惰性求值的，每次迭代都会重新计算，如果需要多次遍历结果，应将视图复制到容器中
- 视图不拥有数据，底层容器被销毁后视图将变为悬空引用，使用时需确保底层容器的生命周期
- `std::views::filter` 和 `std::views::transform` 返回的视图不满足 `common_range`，其 `end()` 返回哨兵而非迭代器，某些需要双向迭代的场景需注意
- 部分视图（如 `filter`）的迭代器性能略低于原生循环，在对性能极其敏感的热路径中应进行基准测试
- `std::views::split` 在 C++20 中返回的子范围类型使用不便，C++23 的 `std::views::split` 改进了接口
- Ranges 算法（如 `std::ranges::sort`）会直接修改原容器，与视图的惰性语义不同，使用时需区分

## 进阶用法

### 自定义视图适配器

```cpp
#include <ranges>
#include <concepts>

// 自定义视图：每 N 个元素取一个（采样）
template<std::ranges::view V>
struct SampleView : std::ranges::view_interface<SampleView<V>> {
    V base_;
    std::size_t step_;

    // 迭代器实现（简化版）
    class iterator {
        std::ranges::iterator_t<V> current_;
        std::ranges::sentinel_t<V> end_;
        std::size_t step_;
    public:
        iterator(std::ranges::iterator_t<V> cur,
                 std::ranges::sentinel_t<V> end,
                 std::size_t step)
            : current_(cur), end_(end), step_(step) {}

        auto operator*() const { return *current_; }

        iterator& operator++() {
            // 前进 step 步
            for (std::size_t i = 0; i < step_ && current_ != end_; ++i) {
                ++current_;
            }
            return *this;
        }
    };

    auto begin() { return iterator{base_.begin(), base_.end(), step_}; }
    auto end() { return std::default_sentinel; }
};

// 适配器闭包对象（支持管道语法）
struct SampleFn {
    std::size_t step;
    template<std::ranges::viewable_range R>
    auto operator()(R&& r) const {
        return SampleView<std::views::all_t<R>>{
            std::views::all(std::forward<R>(r)), step
        };
    }
};

// 使用方式
// auto sampled = data | SampleFn{3};  // 每3个取1个
```

### C++23 新增视图

```cpp
#include <ranges>

// enumerate: 带索引遍历
std::vector<std::string> items = {"apple", "banana", "cherry"};
for (auto [index, value] : std::views::enumerate(items)) {
    std::cout << index << ": " << value << std::endl;
}

// zip: 合并多个范围
std::vector<int> ids = {1, 2, 3};
std::vector<std::string> names = {"张三", "李四", "王五"};
for (auto [id, name] : std::views::zip(ids, names)) {
    std::cout << id << " - " << name << std::endl;
}

// chunk: 分块处理
std::vector<int> data = {1, 2, 3, 4, 5, 6, 7};
for (auto chunk : std::views::chunk(data, 3)) {
    // 第一轮: {1, 2, 3}，第二轮: {4, 5, 6}，第三轮: {7}
    for (int n : chunk) std::cout << n << " ";
    std::cout << std::endl;
}

// slide: 滑动窗口
for (auto window : std::views::slide(data, 3)) {
    // {1,2,3}, {2,3,4}, {3,4,5}, {4,5,6}, {5,6,7}
    for (int n : window) std::cout << n << " ";
    std::cout << std::endl;
}
```

### Ranges 与投影（Projection）

Ranges 算法支持投影参数，避免编写简单的 lambda：

```cpp
#include <ranges>
#include <algorithm>
#include <vector>

struct Employee {
    std::string name;
    int age;
    double salary;
};

int main() {
    std::vector<Employee> employees = {
        {"张三", 28, 15000.0},
        {"李四", 35, 22000.0},
        {"王五", 24, 12000.0}
    };

    // 按年龄排序，使用投影替代 lambda
    std::ranges::sort(employees, {}, &Employee::age);

    // 按薪资降序排序
    std::ranges::sort(employees, std::greater{}, &Employee::salary);

    // 查找薪资最高的员工
    auto it = std::ranges::max_element(employees, {}, &Employee::salary);
    std::cout << "最高薪资: " << it->name << std::endl;
    return 0;
}
```
## 视图基础

**基本写法：filter 过滤**
`<range> | std::views::filter(<谓词>);`
```cpp
// 过滤出偶数
auto evens = v | std::views::filter([](int x) { return x % 2 == 0; });
```

---

**基本写法：transform 转换**
`<range> | std::views::transform(<函数>);`
```cpp
// 每个元素乘以 2
auto doubled = v | std::views::transform([](int x) { return x * 2; });
```

---

**基本写法：take 取前 N 个**
`<range> | std::views::take(<数量>);`
```cpp
// 取前 5 个元素
auto first5 = v | std::views::take(5);
```

---

**基本写法：drop 跳过前 N 个**
`<range> | std::views::drop(<数量>);`
```cpp
// 跳过前 3 个元素
auto rest = v | std::views::drop(3);
```

---

**基本写法：reverse 反转**
`<range> | std::views::reverse;`
```cpp
// 反转顺序
auto reversed = v | std::views::reverse;
```

---

## 链式组合

**基本写法：管道操作符组合**
`<range> | std::views::filter(<谓词>) | std::views::transform(<函数>);`
```cpp
// 过滤偶数并乘以 10
auto result = v
    | std::views::filter([](int x) { return x % 2 == 0; })
    | std::views::transform([](int x) { return x * 10; });
```

---

**基本写法：取前 N 个并反转**
`<range> | std::views::take(<数量>) | std::views::reverse;`
```cpp
// 取前 3 个并反转
auto result = v | std::views::take(3) | std::views::reverse;
```

---

## 生成视图

**基本写法：iota 递增序列**
`std::views::iota(<起始> [, <结束>]);`
```cpp
// 生成 0 到 9
auto nums = std::views::iota(0, 10);

// 生成无限序列（配合 take）
auto infinite = std::views::iota(0) | std::views::take(100);
```

---

**基本写法：repeat 重复**
`std::views::repeat(<值> [, <次数>]);`
```cpp
// 重复 5 五次（无限需配合 take）
auto fives = std::views::repeat(5, 3);
```

---

**基本写法：empty 单元素视图**
`std::views::single(<值>);`
```cpp
// 包含单个元素的视图
auto one = std::views::single(42);
```

---

## 元素访问

**基本写法：遍历 range**
`for (auto&& <元素> : <range>) { ... }`
```cpp
// 遍历过滤后的视图
for (int x : v | std::views::filter([](int n) { return n > 0; })) {
    std::cout << x;
}
```

---

## 常用算法

**基本写法：ranges::sort 排序**
`std::ranges::sort(<range> [, <比较器>]);`
```cpp
// 对容器排序
std::ranges::sort(v);
// 降序
std::ranges::sort(v, std::greater<int>());
```

---

**基本写法：ranges::find 查找**
`std::ranges::find(<range>, <值>);`
```cpp
// 查找值为 5 的元素
auto it = std::ranges::find(v, 5);
```

---

**基本写法：ranges::min_element 最小值**
`std::ranges::min_element(<range>);`
```cpp
// 查找最小元素
auto it = std::ranges::min_element(v);
```

---

**基本写法：ranges::count 计数**
`std::ranges::count(<range>, <值>);`
```cpp
// 统计值为 3 的个数
auto n = std::ranges::count(v, 3);
```

---

**基本写法：ranges::transform 转换**
`std::ranges::transform(<range>, <输出迭代器>, <函数>);`
```cpp
// 转换并存入另一容器
std::ranges::transform(v, std::back_inserter(dest), [](int x) { return x * 2; });
```

## 参考文献



cppreference C++ 文档：https://zh.cppreference.com/w/cpp
C++ 核心指南：https://isocpp.github.io/CppCoreGuidelines/
C++ 标准草案（WG21）：https://isocpp.org/std/the-standard
CMake 官方文档：https://cmake.org/documentation/
Compiler Explorer：https://godbolt.org/

## 延伸阅读



C++ 模板深入，见 026-cpp/062-CppTemplate 文档。
STL 容器与算法，见 026-cpp 模块 STL 文档。
并发与原子，见 026-cpp 模块并发文档。
Rust 内存安全对比，见 053-rust 模块（若已加入）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 C++ 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C++ 概述与现代标准 | 001-CppOverviewAndModernStandard | 本文的前置基础 |
| C++ 基础语法 | 002-CppBasicSyntax | 本文的前置基础 |
| C++ 类型系统 | 003-CppTypeSystem | 本文的并列主题 |
| C++ 引用 | 004-CppReference | 本文的并列主题 |
| 右值引用与移动语义 | 005-RvalueReferenceMoveSemantics | 本文的并列主题 |
| C++ 指针 | 006-PointersCppreferenceCom | 本文的并列主题 |
| 智能指针详解 | 007-N4089DeletingSafeBoolInFavorOfExplicitBool | 本文的并列主题 |
| Lambda表达式 | 008-LambdaExpression | 本文的并列主题 |
| 模板元编程 | 009-ATourOfC3rdEditionOnlineExcerpts | 本文的并列主题 |
| C++20范围 | 010-Cpp20Range | 本文自身 |
| C++20模块 | 011-Cpp20Module | 本文的并列主题 |
| 设计模式与C++ | 012-DesignPatternCpp | 本文的并列主题 |
| RAII与资源管理 | 013-RAIIResourceManagement | 本文的并列主题 |
| 运算符重载 | 014-OperatorOverloading | 本文的并列主题 |
| C++ 面向对象基础 | 015-COOPBasics | 本文的前置基础 |
| C++ STL 算法详解 | 016-CSTL | 本文的并列主题 |
| 字符串处理 | 017-StringProcessing | 本文的并列主题 |
| 文件IO与文件系统 | 018-FileIOFileSystem | 本文的并列主题 |
| 异常安全 | 019-ExceptionSecurity | 本文的安全延伸 |
| 多线程与并发 | 020-MultithreadingConcurrency | 本文的并列主题 |
| 类型特征与SFINAE | 021-TypeTraitsSFINAE | 本文的并列主题 |
| 变参模板 | 022-VariadicTemplate | 本文的并列主题 |
| constexpr与编译期计算 | 023-ConstexprCompileTime | 本文的并列主题 |
| 命名空间与链接 | 024-NamespaceLinkage | 本文的并列主题 |
| C++网络编程 | 025-CppNetworkProgramming | 本文的并列主题 |
| C++ 面向对象进阶 | 026-COOPAdvanced | 本文的并列主题 |
| C++内存模型 | 027-CppMemoryModel | 本文的并列主题 |
| C++图形编程 | 028-CppGraphicsProgramming | 本文的并列主题 |
| C++工具链 | 029-CppToolchain | 本文的并列主题 |
| C++正则表达式 | 030-CppRegex | 本文的并列主题 |
| C++与Python交互 | 031-CppPythonInteraction | 本文的并列主题 |
| C++测试框架 | 032-CppTestFramework | 本文的并列主题 |
| C++与Rust对比 | 033-CppRustComparison | 本文的并列主题 |
| C++23与C++26新特性 | 034-Cpp23Cpp26NewFeatures | 本文的并列主题 |
| C++性能优化 | 035-CppPerformance | 本文的性能延伸 |
| C++序列化 | 036-CppSerialization | 本文的并列主题 |
| C++游戏开发 | 037-CppGameDev | 本文的并列主题 |
| C++嵌入式开发 | 038-CppEmbedded | 本文的并列主题 |
| C++ 内存管理 | 039-CppMemoryManagement | 本文的并列主题 |
| C++代码规范 | 040-CppCodeStyle | 本文的并列主题 |
| C++与WebAssembly | 041-CppWebAssembly | 本文的并列主题 |
| C++反射与元编程 | 042-CppReflectionMetaprogramming | 本文的并列主题 |
| C++数学库 | 043-CppMathLibrary | 本文的并列主题 |
| 智能指针 | 044-SmartPointer | 本文的并列主题 |
| C++ 日期时间 | 045-CppDateTime | 本文的并列主题 |
| C++格式化输出 | 046-CppFormatOutput | 本文的并列主题 |
| C++26 与最新标准 | 047-Cpp26AndLatestStandard | 本文的并列主题 |
| C++ STL 容器与迭代器 | 048-CSTL | 本文的并列主题 |
| 并发编程 | 049-ConcurrentProgramming | 本文的并列主题 |
| RAII资源管理 | 050-CCoreGuidelinesResourceManagement | 本文的并列主题 |
| C++ STL 算法与函数对象 | 051-CSTLAlgorithmAndFunctionObject | 本文的并列主题 |
| 移动语义详解 | 052-MoveSemanticsDetailed | 本文的并列主题 |
| 完美转发与引用折叠 | 053-PerfectForwardingReferenceCollapse | 本文的并列主题 |
| 虚函数表与多态内存布局 | 054-VTablePolymorphismMemoryLayout | 本文的并列主题 |
| 智能指针循环引用 | 055-SmartPointerCircularReference | 本文的并列主题 |
| Lambda捕获详解 | 056-LambdaCaptureDetailed | 本文的并列主题 |
| 类型萃取与SFINAE | 057-TypeExtractionSFINAE | 本文的并列主题 |
| 可变参数模板与折叠表达式 | 058-VariadicTemplateFoldExpression | 本文的并列主题 |
| C++20协程 | 059-Cpp20Coroutine | 本文的并列主题 |
| C++20概念 | 060-Cpp20Concept | 本文的并列主题 |
| C++23新特性 | 061-Cpp23NewFeatures | 本文的并列主题 |
| C++ 模板 | 062-CppTemplate | 本文的并列主题 |
| 内存序与无锁编程 | 063-MemoryOrderLockFree | 本文的并列主题 |
| C++ 异常处理与性能优化 | 064-CppExceptionAndPerformance | 本文的性能延伸 |
| C++ 调试与性能分析 | 065-CDebugPerformanceAnalysis | 本文的性能延伸 |
| C++ 项目实战 | 066-CppProjectPractice | 本文的综合应用 |
| C++ STL 容器使用速查 | 067-STLContainerUsage | 本文的并列主题 |
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文的并列主题 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
