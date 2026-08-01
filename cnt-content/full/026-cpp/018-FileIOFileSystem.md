---
order: 63
title: 文件IO与文件系统
module: cpp
category: C++
difficulty: intermediate
description: '文件操作与std::filesystem'
author: fanquanpp
updated: '2026-08-01'
related:
  - cpp/STL算法详解
  - cpp/字符串处理
  - cpp/异常安全
  - cpp/多线程与并发
prerequisites:
  - cpp/概述与现代标准
---

# 文件IO与文件系统

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

### 目录遍历

```cpp
#include <filesystem>
#include <iostream>
#include <vector>

namespace fs = std::filesystem;

// 遍历目录中的所有文件
void listFiles(const std::string& dir) {
    for (const auto& entry : fs::directory_iterator(dir)) {
        if (entry.is_regular_file()) {
            std::cout << "文件: " << entry.path() << std::endl;
        } else if (entry.is_directory()) {
            std::cout << "目录: " << entry.path() << std::endl;
        }
    }
}

// 递归遍历（包含子目录）
void listAllFiles(const std::string& dir) {
    for (const auto& entry : fs::recursive_directory_iterator(dir)) {
        if (entry.is_regular_file()) {
            std::cout << entry.path() << " (" << entry.file_size() << " bytes)" << std::endl;
        }
    }
}

// 查找特定扩展名的文件
std::vector<fs::path> findByExtension(const fs::path& dir, const std::string& ext) {
    std::vector<fs::path> result;
    for (const auto& entry : fs::recursive_directory_iterator(dir)) {
        if (entry.is_regular_file() && entry.path().extension() == ext) {
            result.push_back(entry.path());
        }
    }
    return result;
}
```

## 概述

C++ 标准库提供了两套文件操作接口：传统的文件流（`std::ifstream`/`std::ofstream`）用于文本和二进制文件的读写，C++17 引入的 `std::filesystem` 用于路径操作和文件系统查询。文件流基于流的抽象，支持格式化读写和随机访问；filesystem 提供了跨平台的文件系统操作能力，包括路径拼接、目录遍历和文件属性查询。

## 基础概念

### 文件流类型

| 类型            | 说明                 |
| --------------- | -------------------- |
| `std::ifstream` | 输入文件流，只读     |
| `std::ofstream` | 输出文件流，只写     |
| `std::fstream`  | 输入输出文件流，读写 |

### 打开模式

| 模式               | 说明             |
| ------------------ | ---------------- |
| `std::ios::in`     | 读模式打开       |
| `std::ios::out`    | 写模式打开       |
| `std::ios::app`    | 追加模式         |
| `std::ios::binary` | 二进制模式       |
| `std::ios::trunc`  | 截断文件（默认） |
| `std::ios::ate`    | 打开后定位到末尾 |

## 快速上手

### 文本文件读写

```cpp
#include <fstream>
#include <string>
#include <iostream>

int main() {
    // 写入文件
    std::ofstream out("output.txt");
    out << "第一行" << std::endl;
    out << "第二行" << std::endl;
    out.close();  // 可以显式关闭，析构时也会自动关闭

    // 读取文件
    std::ifstream in("output.txt");
    std::string line;
    while (std::getline(in, line)) {
        std::cout << line << std::endl;
    }
    return 0;
}
```

### std::filesystem 基础（C++17）

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

int main() {
    fs::path p = "/usr/local/bin";

    // 路径操作
    p / "app";                          // 路径拼接: /usr/local/bin/app
    p.filename();                        // "bin"
    p.parent_path();                     // "/usr/local"
    p.extension();                       // ""（无扩展名）

    // 文件系统查询
    fs::exists(p);                       // 是否存在
    fs::is_directory(p);                 // 是否目录
    fs::is_regular_file(p);             // 是否普通文件
    fs::file_size(p);                    // 文件大小

    // 目录操作
    fs::create_directories("a/b/c");    // 递归创建目录
    fs::copy("src", "dst", fs::copy_options::recursive);  // 递归复制
    fs::remove("temp.txt");             // 删除文件
    fs::rename("old.txt", "new.txt");   // 重命名
    return 0;
}
```

## 详细用法

### 二进制文件读写

```cpp
#include <fstream>
#include <vector>

struct Record {
    int id;
    double value;
    char name[32];
};

void writeRecords(const std::string& filename, const std::vector<Record>& records) {
    std::ofstream out(filename, std::ios::binary);
    for (const auto& r : records) {
        out.write(reinterpret_cast<const char*>(&r), sizeof(Record));
    }
}

std::vector<Record> readRecords(const std::string& filename) {
    std::ifstream in(filename, std::ios::binary);
    std::vector<Record> records;
    Record r;
    while (in.read(reinterpret_cast<char*>(&r), sizeof(Record))) {
        records.push_back(r);
    }
    return records;
}
```

### 随机访问文件

```cpp
#include <fstream>
#include <string>

class IndexedFile {
    std::fstream file_;
public:
    explicit IndexedFile(const std::string& path) {
        file_.open(path, std::ios::in | std::ios::out | std::ios::binary);
        if (!file_) {
            // 文件不存在则创建
            file_.open(path, std::ios::out | std::ios::binary);
            file_.close();
            file_.open(path, std::ios::in | std::ios::out | std::ios::binary);
        }
    }

    // 在指定位置写入数据
    void writeAt(size_t offset, const std::string& data) {
        file_.seekp(offset);  // 定位写位置
        auto size = static_cast<uint32_t>(data.size());
        file_.write(reinterpret_cast<const char*>(&size), sizeof(size));
        file_.write(data.data(), size);
    }

    // 从指定位置读取数据
    std::string readAt(size_t offset) {
        file_.seekg(offset);  // 定位读位置
        uint32_t size;
        file_.read(reinterpret_cast<char*>(&size), sizeof(size));
        std::string result(size, '\0');
        file_.read(&result[0], size);
        return result;
    }
};
```

### 路径操作详解

```cpp
#include <filesystem>
#include <iostream>

namespace fs = std::filesystem;

void pathOperations() {
    fs::path p = "/home/user/docs/report.txt";

    // 路径分解
    p.root_name();      // ""（POSIX）或 "C:"（Windows）
    p.root_directory(); // "/"
    p.parent_path();    // "/home/user/docs"
    p.filename();       // "report.txt"
    p.stem();           // "report"（不含扩展名）
    p.extension();      // ".txt"

    // 路径拼接
    fs::path base = "/home/user";
    fs::path full = base / "docs" / "report.txt";  // /home/user/docs/report.txt

    // 路径转换
    p.string();         // 转为 std::string
    p.u8string();       // 转为 UTF-8 字符串

    // 相对路径
    fs::path a = "/home/user/docs";
    fs::path b = "/home/user/images/photo.jpg";
    auto rel = fs::relative(b, a);  // "../images/photo.jpg"
}
```

## 常见场景

### 文件监控

```cpp
#include <filesystem>
#include <chrono>
#include <unordered_map>

namespace fs = std::filesystem;

class FileWatcher {
    std::unordered_map<std::string, fs::file_time_type> lastModified_;
    fs::path watchDir_;

public:
    explicit FileWatcher(fs::path dir) : watchDir_(std::move(dir)) {
        // 记录初始状态
        for (const auto& entry : fs::recursive_directory_iterator(watchDir_)) {
            if (entry.is_regular_file()) {
                lastModified_[entry.path().string()] = entry.last_write_time();
            }
        }
    }

    // 检查是否有文件被修改
    std::vector<std::string> checkChanges() {
        std::vector<std::string> changed;
        for (const auto& entry : fs::recursive_directory_iterator(watchDir_)) {
            if (entry.is_regular_file()) {
                auto path = entry.path().string();
                auto mtime = entry.last_write_time();
                if (lastModified_.count(path) && lastModified_[path] != mtime) {
                    changed.push_back(path);
                }
                lastModified_[path] = mtime;
            }
        }
        return changed;
    }
};
```

### 配置文件管理

```cpp
#include <filesystem>
#include <fstream>
#include <string>

namespace fs = std::filesystem;

class ConfigManager {
    fs::path configDir_;
public:
    explicit ConfigManager(const std::string& appName) {
        // 获取平台特定的配置目录
#ifdef _WIN32
        configDir_ = fs::path(getenv("APPDATA")) / appName;
#else
        configDir_ = fs::path(getenv("HOME")) / ".config" / appName;
#endif
        fs::create_directories(configDir_);
    }

    std::string readConfig(const std::string& name) {
        auto path = configDir_ / name;
        if (!fs::exists(path)) return "";
        std::ifstream in(path);
        std::string content((std::istreambuf_iterator<char>(in)),
                            std::istreambuf_iterator<char>());
        return content;
    }

    void writeConfig(const std::string& name, const std::string& content) {
        auto path = configDir_ / name;
        std::ofstream out(path);
        out << content;
    }
};
```

## 注意事项

- 文件流在析构时自动关闭文件，但显式关闭可以在文件被复用前释放资源
- `std::filesystem` 操作可能抛出 `std::filesystem::filesystem_error` 异常
- 路径中的中文和空格需要正确处理，`fs::path` 内部使用宽字符存储
- 二进制模式下 `std::endl` 不会进行换行转换，文本模式下 Windows 会将 `\n` 转为 `\r\n`
- 目录遍历操作不是原子性的，遍历过程中文件可能被创建或删除
- `fs::file_size` 对目录返回的结果未定义，应先检查 `is_regular_file`

## 进阶用法

### 内存映射文件

```cpp
#include <fstream>
#include <iostream>

// 简化的内存映射文件读取（使用标准库）
std::string readFileToString(const fs::path& path) {
    // 打开文件并定位到末尾获取大小
    std::ifstream in(path, std::ios::binary | std::ios::ate);
    if (!in) throw std::runtime_error("无法打开文件");

    auto size = in.tellg();
    in.seekg(0);

    std::string content;
    content.resize(size);
    in.read(&content[0], size);
    return content;
}

// 高性能行读取
std::vector<std::string> readLines(const fs::path& path) {
    std::ifstream in(path);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(in, line)) {
        lines.push_back(std::move(line));
    }
    return lines;
}
```

### 文件系统权限（C++20）

```cpp
#include <filesystem>

namespace fs = std::filesystem;

// C++20: 更精细的权限控制
void setPermissions(const fs::path& file) {
    // 设置读写权限
    fs::perms p = fs::perms::owner_read | fs::perms::owner_write;
    fs::permissions(file, p, fs::perm_options::replace);

    // 添加执行权限
    fs::permissions(file, fs::perms::owner_exec, fs::perm_options::add);
}
```
## 文件流基础

**包含头文件写法**
`#include <fstream>`
```cpp
// 包含文件流头文件
#include <fstream>
```

---

## 文件打开与关闭

**输出流写法：打开输出文件流**
`std::ofstream <ofs>("<filename>");`
```cpp
#include <fstream>
// 打开输出文件流
std::ofstream ofs("output.txt");
```

---

**输入流写法：打开输入文件流**
`std::ifstream <ifs>("<filename>");`
```cpp
#include <fstream>
// 打开输入文件流
std::ifstream ifs("input.txt");
```

---

**打开模式写法：指定打开模式**
`std::ofstream <ofs>("<filename>", <mode>);`
```cpp
#include <fstream>
// 以追加模式打开文件
std::ofstream ofs("log.txt", std::ios::app);
```

---

**检查写法：检查文件是否打开成功**
`if (!<stream>) { ... }` 或 `if (<stream>.is_open()) { ... }`
```cpp
// 检查文件是否成功打开
std::ifstream ifs("data.txt");
if (!ifs) {
    std::cerr << "Failed to open file" << std::endl;
}
```

---

**关闭写法：关闭文件流**
`<stream>.close();`
```cpp
// 关闭文件流
ofs.close();
```

---

## 写入文件

**基本写法：使用 << 写入**
`<ofs> << <value>;`
```cpp
// 使用 << 写入数据
std::ofstream ofs("output.txt");
ofs << "Hello World" << std::endl;
ofs << 42 << std::endl;
```

---

**write 写法：二进制写入**
`<ofs>.write(<buffer>, <size>);`
```cpp
// 二进制写入
std::ofstream ofs("data.bin", std::ios::binary);
int data = 42;
ofs.write(reinterpret_cast<const char*>(&data), sizeof(data));
```

---

## 读取文件

**基本写法：使用 >> 读取**
`<ifs> >> <var>;`
```cpp
// 使用 >> 读取数据
std::ifstream ifs("input.txt");
int value;
ifs >> value;
```

---

**getline 写法：读取一行**
`std::getline(<ifs>, <line>);`
```cpp
#include <string>
// 读取一行
std::ifstream ifs("input.txt");
std::string line;
std::getline(ifs, line);
```

---

**read 写法：二进制读取**
`<ifs>.read(<buffer>, <size>);`
```cpp
// 二进制读取
std::ifstream ifs("data.bin", std::ios::binary);
int data;
ifs.read(reinterpret_cast<char*>(&data), sizeof(data));
```

---

## 遍历文件

**按行遍历写法：逐行读取文件**
`while (std::getline(<ifs>, <line>)) { ... }`
```cpp
#include <fstream>
#include <string>
// 逐行读取文件
std::ifstream ifs("input.txt");
std::string line;
while (std::getline(ifs, line)) {
    std::cout << line << std::endl;
}
```

---

**按字符遍历写法：逐字符读取**
`while (<ifs>.get(<ch>)) { ... }`
```cpp
// 逐字符读取文件
std::ifstream ifs("input.txt");
char ch;
while (ifs.get(ch)) {
    std::cout << ch;
}
```

---

## 文件定位

**seekg 写法：设置读取位置**
`<ifs>.seekg(<offset>, <origin>);`
```cpp
// 设置读取位置到文件开头
ifs.seekg(0, std::ios::beg);
```

---

**tellg 写法：获取读取位置**
`std::streampos <pos> = <ifs>.tellg();`
```cpp
// 获取当前读取位置
std::streampos pos = ifs.tellg();
```

---

**seekp 写法：设置写入位置**
`<ofs>.seekp(<offset>, <origin>);`
```cpp
// 设置写入位置到文件末尾
ofs.seekp(0, std::ios::end);
```

---

## 文件状态检查

**eof 写法：检查文件结束**
`<ifs>.eof()`
```cpp
// 检查是否到达文件末尾
if (ifs.eof()) {
    std::cout << "End of file" << std::endl;
}
```

---

**fail 写法：检查文件错误**
`<ifs>.fail()`
```cpp
// 检查文件操作是否失败
if (ifs.fail()) {
    std::cerr << "File operation failed" << std::endl;
}
```

---

**clear 写法：清除错误状态**
`<ifs>.clear();`
```cpp
// 清除文件错误状态
ifs.clear();
```

---

## 字符串流

**istringstream 写法：字符串输入流**
`std::istringstream <iss>(<str>);`
```cpp
#include <sstream>
// 从字符串读取
std::string str = "10 20 30";
std::istringstream iss(str);
int a, b, c;
iss >> a >> b >> c;
```

---

**ostringstream 写法：字符串输出流**
`std::ostringstream <oss>;`
```cpp
#include <sstream>
// 写入到字符串
std::ostringstream oss;
oss << "Value: " << 42;
std::string result = oss.str();
```

---

**stringstream 写法：双向字符串流**
`std::stringstream <ss>;`
```cpp
#include <sstream>
// 双向字符串流
std::stringstream ss;
ss << "Hello";
std::string result;
ss >> result;
```

---

## 文件系统（C++17）

**包含头文件写法**
`#include <filesystem>`
```cpp
// 包含文件系统头文件
#include <filesystem>
namespace fs = std::filesystem;
```

---

**创建目录写法**
`fs::create_directory(<path>);`
```cpp
#include <filesystem>
// 创建目录
fs::create_directory("mydir");
```

---

**创建多级目录写法**
`fs::create_directories(<path>);`
```cpp
#include <filesystem>
// 创建多级目录
fs::create_directories("a/b/c");
```

---

**删除文件写法**
`fs::remove(<path>);`
```cpp
#include <filesystem>
// 删除文件
fs::remove("file.txt");
```

---

**删除目录写法**
`fs::remove_all(<path>);`
```cpp
#include <filesystem>
// 递归删除目录
fs::remove_all("mydir");
```

---

**检查文件存在写法**
`fs::exists(<path>)`
```cpp
#include <filesystem>
// 检查文件是否存在
if (fs::exists("file.txt")) {
    std::cout << "File exists" << std::endl;
}
```

---

**复制文件写法**
`fs::copy(<src>, <dest>);`
```cpp
#include <filesystem>
// 复制文件
fs::copy("src.txt", "dest.txt");
```

---

**重命名文件写法**
`fs::rename(<old>, <new>);`
```cpp
#include <filesystem>
// 重命名文件
fs::rename("old.txt", "new.txt");
```

---

**获取文件大小写法**
`fs::file_size(<path>)`
```cpp
#include <filesystem>
// 获取文件大小
std::uintmax_t size = fs::file_size("file.txt");
```

---

## 路径操作

**基本写法：创建路径对象**
`fs::path <p>("<path>");`
```cpp
#include <filesystem>
// 创建路径对象
fs::path p("dir/file.txt");
```

---

**拼接写法：路径拼接**
`<p> / "<subpath>"`
```cpp
#include <filesystem>
// 使用 / 运算符拼接路径
fs::path p = "dir";
p /= "subdir";
p /= "file.txt";
```

---

**获取文件名写法**
`<path>.filename()`
```cpp
#include <filesystem>
// 获取文件名
fs::path p("dir/file.txt");
std::cout << p.filename() << std::endl;
```

---

**获取扩展名写法**
`<path>.extension()`
```cpp
#include <filesystem>
// 获取文件扩展名
fs::path p("file.txt");
std::cout << p.extension() << std::endl;
```

---

**获取父路径写法**
`<path>.parent_path()`
```cpp
#include <filesystem>
// 获取父路径
fs::path p("dir/file.txt");
std::cout << p.parent_path() << std::endl;
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
| 文件IO与文件系统 | 018-FileIOFileSystem | 本文自身 |
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
