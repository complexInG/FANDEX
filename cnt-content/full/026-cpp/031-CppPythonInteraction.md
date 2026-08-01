---
order: 73
title: C++与Python交互
module: cpp
category: C++
difficulty: intermediate
description: pybind11与C API
author: fanquanpp
updated: '2026-08-01'
related:
  - cpp/C++序列化
  - cpp/C++网络编程
  - cpp/C++与Rust对比
  - cpp/C++23与C++26新特性
prerequisites:
  - cpp/概述与环境配置
---

## 概述

C++ 与 Python 交互是指在两种语言之间互相调用代码。Python 有丰富的生态和简洁的语法，但运行速度较慢；C++ 性能强大但开发效率较低。将两者结合，可以用 Python 快速编写业务逻辑，用 C++ 实现性能关键的部分。主要的交互方式有 Python C API（底层但灵活）和 pybind11（现代且易用）。

为什么需要 C++ 与 Python 交互？深度学习框架（PyTorch、TensorFlow）用 C++ 实现核心计算，用 Python 提供易用的接口；科学计算库（NumPy、SciPy）用 C/C++ 加速数值运算；游戏引擎用 C++ 处理渲染，用 Python 编写脚本逻辑。如果你需要在 Python 中调用 C++ 的高性能代码，或者需要在 C++ 中使用 Python 的库，就需要掌握两者之间的交互技术。

## 基础概念

**Python C API**：Python 提供的 C 语言接口，是最低层的交互方式。所有引用计数、类型检查都需要手动处理，容易出错但最灵活。

**pybind11**：基于 C++11 的轻量级头文件库，简化了 C++ 与 Python 的绑定。自动处理引用计数、类型转换和异常传递，是当前最推荐的方式。

**引用计数**：Python 使用引用计数管理内存。C API 中每次增加 Python 对象的引用时必须调用 `Py_INCREF`，减少时调用 `Py_DECREF`，否则会导致内存泄漏或崩溃。

**GIL（全局解释器锁）**：Python 的全局解释器锁，同一时刻只允许一个线程执行 Python 代码。C++ 代码在调用 Python API 时必须持有 GIL，纯 C++ 计算可以释放 GIL 以实现并行。

## 快速上手

### 使用 pybind11

安装 pybind11：

```bash
pip install pybind11
```

编写 C++ 模块：

```cpp
// mymodule.cpp - 一个简单的 Python 扩展模块
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // 支持 STL 容器自动转换
#include <string>

namespace py = pybind11;

// 普通函数
int add(int a, int b) {
    return a + b;
}

// 带字符串参数的函数
std::string greet(const std::string& name) {
    return "你好, " + name + "!";
}

// 定义 Python 模块
PYBIND11_MODULE(mymodule, m) {
    m.doc() = "示例 Python 扩展模块";

    // 绑定函数
    m.def("add", &add, "两个数相加",
          py::arg("a"), py::arg("b"));

    m.def("greet", &greet, "问候函数",
          py::arg("name"));

    // 绑定带默认参数的函数
    m.def("multiply", [](int a, int b = 2) { return a * b; },
          "乘法运算", py::arg("a"), py::arg("b") = 2);
}
```

编译为 Python 模块：

```bash
# 使用 pybind11 提供的编译工具
c++ -O3 -Wall -shared -std=c++17 -fPIC $(python3 -m pybind11 --includes) mymodule.cpp -o mymodule$(python3-config --extension-suffix)
```

或者使用 CMake：

```cmake
cmake_minimum_required(VERSION 3.14)
project(mymodule)

find_package(pybind11 REQUIRED)

pybind11_add_module(mymodule mymodule.cpp)
```

在 Python 中使用：

```python
import mymodule

result = mymodule.add(3, 5)
print(result)  # 8

greeting = mymodule.greet("世界")
print(greeting)  # 你好, 世界!

product = mymodule.multiply(4)     # 使用默认参数 b=2
print(product)  # 8
```

## 详细用法

### 绑定类

```cpp
#include <pybind11/pybind11.h>
#include <string>
#include <vector>

namespace py = pybind11;

class Pet {
public:
    Pet(const std::string& name, int age)
        : name_(name), age_(age) {}

    std::string getName() const { return name_; }
    void setName(const std::string& name) { name_ = name; }

    int getAge() const { return age_; }
    void setAge(int age) { age_ = age; }

    std::string info() const {
        return name_ + ", " + std::to_string(age_) + "岁";
    }

private:
    std::string name_;
    int age_;
};

PYBIND11_MODULE(petmodule, m) {
    // 绑定类
    py::class_<Pet>(m, "Pet")
        // 构造函数
        .def(py::init<const std::string&, int>(),
             py::arg("name"), py::arg("age"))

        // 绑定方法
        .def("info", &Pet::info, "获取宠物信息")

        // 绑定属性（通过 getter/setter）
        .def_property("name", &Pet::getName, &Pet::setName)
        .def_property("age", &Pet::getAge, &Pet::setAge)

        // 只读属性
        .def_property_readonly("description", &Pet::info)

        // 设置文档字符串
        .doc() = "宠物类";
}
```

Python 中使用：

```python
import petmodule

pet = petmodule.Pet("旺财", 3)
print(pet.info())       # 旺财, 3岁
print(pet.name)         # 旺财
pet.name = "小花"
print(pet.name)         # 小花
pet.age = 4
print(pet.age)          # 4
```

### 继承与多态

```cpp
class Animal {
public:
    virtual ~Animal() = default;
    virtual std::string speak() const = 0;
};

class Dog : public Animal {
public:
    std::string speak() const override { return "汪汪!"; }
};

class Cat : public Animal {
public:
    std::string speak() const override { return "喵喵!"; }
};

// 工厂函数
std::unique_ptr<Animal> createAnimal(const std::string& type) {
    if (type == "dog") return std::make_unique<Dog>();
    if (type == "cat") return std::make_unique<Cat>();
    throw std::runtime_error("未知动物类型: " + type);
}

PYBIND11_MODULE(animals, m) {
    // 绑定基类（注意要指定持有人类型以支持多态）
    py::class_<Animal>(m, "Animal")
        .def("speak", &Animal::speak);

    // 绑定派生类，指定基类
    py::class_<Dog, Animal>(m, "Dog")
        .def(py::init<>());

    py::class_<Cat, Animal>(m, "Cat")
        .def(py::init<>());

    // 绑定工厂函数
    m.def("create_animal", &createAnimal,
          py::return_value_policy::take_ownership);
}
```

### STL 容器转换

```cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // 必须包含此头文件
#include <vector>
#include <map>

namespace py = pybind11;

// 使用 vector 的函数
double average(const std::vector<double>& numbers) {
    if (numbers.empty()) return 0.0;
    double sum = 0;
    for (double n : numbers) sum += n;
    return sum / numbers.size();
}

// 使用 map 的函数
std::map<std::string, int> wordCount(const std::vector<std::string>& words) {
    std::map<std::string, int> counts;
    for (const auto& word : words) {
        counts[word]++;
    }
    return counts;
}

PYBIND11_MODULE(stlmodule, m) {
    m.def("average", &average);
    m.def("word_count", &wordCount);
}
```

Python 中使用：

```python
import stlmodule

# Python list 自动转换为 std::vector
avg = stlmodule.average([1.0, 2.0, 3.0, 4.0])
print(avg)  # 2.5

# 返回的 std::map 自动转换为 Python dict
counts = stlmodule.word_count(["hello", "world", "hello"])
print(counts)  # {'hello': 2, 'world': 1}
```

### NumPy 交互

```cpp
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>  // NumPy 支持
#include <vector>

namespace py = pybind11;

// 从 NumPy 数组读取数据
double sumArray(py::array_t<double> arr) {
    auto buf = arr.request();  // 获取缓冲区信息
    double* ptr = static_cast<double*>(buf.ptr);

    double sum = 0;
    for (ssize_t i = 0; i < buf.size; i++) {
        sum += ptr[i];
    }
    return sum;
}

// 创建 NumPy 数组返回给 Python
py::array_t<double> createArray(int size) {
    auto result = py::array_t<double>(size);
    auto buf = result.request();
    double* ptr = static_cast<double*>(buf.ptr);

    for (int i = 0; i < size; i++) {
        ptr[i] = static_cast<double>(i) * i;
    }

    return result;
}

// 不复制地操作 NumPy 数组（零拷贝）
void scaleArray(py::array_t<double> arr, double factor) {
    auto buf = arr.request();
    double* ptr = static_cast<double*>(buf.ptr);

    for (ssize_t i = 0; i < buf.size; i++) {
        ptr[i] *= factor;
    }
    // 直接修改原数组，无需返回
}

PYBIND11_MODULE(numpymodule, m) {
    m.def("sum_array", &sumArray);
    m.def("create_array", &createArray);
    m.def("scale_array", &scaleArray);
}
```

### 释放 GIL 进行并行计算

```cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <algorithm>

namespace py = pybind11;

// 释放 GIL 的纯计算函数
std::vector<double> heavyComputation(int size) {
    // 释放 GIL，允许其他 Python 线程运行
    py::gil_scoped_release release;

    std::vector<double> result(size);
    for (int i = 0; i < size; i++) {
        result[i] = std::sqrt(static_cast<double>(i)) * std::sin(i);
    }

    // release 对象析构时自动恢复 GIL
    return result;
}

// 在 C++ 中调用 Python 代码
void callPythonFromCpp() {
    // 获取 GIL
    py::gil_scoped_acquire acquire;

    py::module_ json = py::module_::import("json");
    py::object result = json.attr("dumps")(py::dict("name"_a = "张三", "age"_a = 25));
    std::string jsonStr = result.cast<std::string>();
    // jsonStr = '{"name": "张三", "age": 25}'
}

PYBIND11_MODULE(parallelmodule, m) {
    m.def("heavy_computation", &heavyComputation);
    m.def("call_python", &callPythonFromCpp);
}
```

### 异常处理

```cpp
#include <pybind11/pybind11.h>
#include <stdexcept>

namespace py = pybind11;

// C++ 异常自动转换为 Python 异常
double divide(double a, double b) {
    if (b == 0) {
        throw std::runtime_error("除数不能为零");
    }
    return a / b;
}

// 注册自定义异常类型
class MyError : public std::runtime_error {
public:
    MyError(const std::string& msg) : std::runtime_error(msg) {}
};

PYBIND11_MODULE(errormodule, m) {
    // 注册 C++ 异常到 Python 异常的映射
    py::register_exception<MyError>(m, "MyError");

    // std::runtime_error 自动映射为 Python RuntimeError
    m.def("divide", &divide);

    // 抛出自定义异常
    m.def("throw_error", []() { throw MyError("自定义错误"); });
}
```

## 常见场景

### 性能加速 Python 代码

```cpp
// 用 C++ 加速 Python 中的排序算法
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <algorithm>

namespace py = pybind11;

// C++ 实现的快速排序
void quickSort(std::vector<int>& arr, int left, int right) {
    if (left >= right) return;

    int pivot = arr[(left + right) / 2];
    int i = left, j = right;

    while (i <= j) {
        while (arr[i] < pivot) i++;
        while (arr[j] > pivot) j--;
        if (i <= j) {
            std::swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }

    quickSort(arr, left, j);
    quickSort(arr, i, right);
}

std::vector<int> cppSort(std::vector<int> arr) {
    quickSort(arr, 0, static_cast<int>(arr.size()) - 1);
    return arr;
}

PYBIND11_MODULE(sortmodule, m) {
    m.def("cpp_sort", &cppSort, "C++ 快速排序");
}
```

## 注意事项

**GIL 管理**：C++ 代码调用 Python API 时必须持有 GIL。长时间纯 C++ 计算应释放 GIL，否则会阻塞所有 Python 线程。

**内存管理**：pybind11 自动管理 Python 对象的引用计数，但如果你直接使用 Python C API，必须手动管理。

**编译兼容性**：扩展模块必须用与 Python 解释器相同的编译器和 ABI 编译。不同版本的 Python 可能不兼容。

**STL 头文件**：使用 STL 容器转换时必须包含 `<pybind11/stl.h>`，否则编译会报错。

**返回值策略**：pybind11 有多种返回值策略（reference、copy、move、take_ownership 等），选择不当会导致悬垂指针或内存泄漏。

## 进阶用法

### 使用 Python C API

```cpp
#include <Python.h>

// 不使用 pybind11，直接使用 C API
PyObject* cApiAdd(PyObject* self, PyObject* args) {
    int a, b;
    // 解析参数
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return nullptr;  // 解析失败，抛出 TypeError
    }
    // 返回结果
    return PyLong_FromLong(a + b);
}

// 方法定义表
static PyMethodDef methods[] = {
    {"add", cApiAdd, METH_VARARGS, "两个数相加"},
    {nullptr, nullptr, 0, nullptr}  // 哨兵
};

// 模块定义
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "capi_module",     // 模块名
    "C API 示例模块",   // 文档
    -1,
    methods
};

// 模块初始化
PyMODINIT_FUNC PyInit_capi_module(void) {
    return PyModule_Create(&module);
}
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
| C++20范围 | 010-Cpp20Range | 本文的并列主题 |
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
| C++与Python交互 | 031-CppPythonInteraction | 本文自身 |
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
