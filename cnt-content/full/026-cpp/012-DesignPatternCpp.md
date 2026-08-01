---
order: 58
title: 设计模式与C++
module: cpp
category: C++
difficulty: intermediate
description: GoF设计模式的C++实现
author: fanquanpp
updated: '2026-08-01'
related:
  - cpp/constexpr与编译期计算
  - cpp/命名空间与链接
  - cpp/面向对象进阶
  - cpp/模板元编程
prerequisites:
  - cpp/概述与现代标准
---

# C++ 设计模式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 概述

设计模式是面向对象编程中经过验证的解决方案模板，用于解决常见的软件设计问题。GoF（Gang of Four）定义了 23 种经典设计模式，分为创建型、结构型和行为型三大类。C++ 的多态、模板、RAII 和智能指针等特性为设计模式的实现提供了丰富的手段，使得许多模式在 C++ 中有比传统面向对象语言更优雅的实现方式。

## 基础概念

### 设计模式分类

| 类别   | 说明         | 典型模式             |
| ------ | ------------ | -------------------- |
| 创建型 | 对象创建机制 | 单例、工厂、建造者   |
| 结构型 | 对象组合方式 | 适配器、装饰器、代理 |
| 行为型 | 对象间通信   | 观察者、策略、命令   |

### C++ 实现设计模式的独特优势

- RAII 替代复杂的资源管理模式
- 智能指针简化对象生命周期管理
- 模板实现编译期多态（CRTP）
- Lambda 简化策略和命令模式

## 快速上手

### 单例模式

```cpp
// C++11 线程安全的 Meyer's Singleton
class Database {
public:
    static Database& instance() {
        static Database db;  // C++11 保证线程安全
        return db;
    }

    void query(const std::string& sql) { /* 查询逻辑 */ }

private:
    Database() = default;
    Database(const Database&) = delete;
    Database& operator=(const Database&) = delete;
};

// 使用
Database::instance().query("SELECT * FROM users");
```

### 工厂模式

```cpp
#include <memory>
#include <string>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
};

class Circle : public Shape {
    double radius_;
public:
    explicit Circle(double r) : radius_(r) {}
    double area() const override { return 3.14159 * radius_ * radius_; }
};

class Rectangle : public Shape {
    double width_, height_;
public:
    Rectangle(double w, double h) : width_(w), height_(h) {}
    double area() const override { return width_ * height_; }
};

// 工厂函数
std::unique_ptr<Shape> createShape(const std::string& type, double a, double b = 0) {
    if (type == "circle") return std::make_unique<Circle>(a);
    if (type == "rectangle") return std::make_unique<Rectangle>(a, b);
    throw std::invalid_argument("未知形状");
}
```

### 策略模式（使用 Lambda）

```cpp
#include <functional>
#include <vector>
#include <algorithm>

class Sorter {
    std::function<bool(int, int)> comparator_;
public:
    explicit Sorter(std::function<bool(int, int)> comp) : comparator_(std::move(comp)) {}

    void sort(std::vector<int>& data) {
        std::sort(data.begin(), data.end(), comparator_);
    }
};

// 使用 Lambda 替代策略类
Sorter ascSorter([](int a, int b) { return a < b; });
Sorter descSorter([](int a, int b) { return a > b; });

std::vector<int> data = {3, 1, 4, 1, 5};
ascSorter.sort(data);   // 升序
descSorter.sort(data);  // 降序
```

## 详细用法

### 观察者模式

```cpp
#include <functional>
#include <vector>
#include <string>
#include <algorithm>

class EventBus {
    std::unordered_map<std::string, std::vector<std::function<void(const std::string&)>>> handlers_;
public:
    void subscribe(const std::string& event, std::function<void(const std::string&)> handler) {
        handlers_[event].push_back(std::move(handler));
    }

    void publish(const std::string& event, const std::string& data) {
        auto it = handlers_.find(event);
        if (it != handlers_.end()) {
            for (auto& handler : it->second) {
                handler(data);
            }
        }
    }
};

// 使用
EventBus bus;
bus.subscribe("user.login", [](const std::string& user) {
    std::cout << user << " 已登录" << std::endl;
});
bus.publish("user.login", "张三");
```

### 装饰器模式

```cpp
#include <memory>
#include <string>

class Coffee {
public:
    virtual ~Coffee() = default;
    virtual double cost() const = 0;
    virtual std::string description() const = 0;
};

class Espresso : public Coffee {
public:
    double cost() const override { return 10.0; }
    std::string description() const override { return "浓缩咖啡"; }
};

class MilkDecorator : public Coffee {
    std::unique_ptr<Coffee> coffee_;
public:
    explicit MilkDecorator(std::unique_ptr<Coffee> c) : coffee_(std::move(c)) {}
    double cost() const override { return coffee_->cost() + 3.0; }
    std::string description() const override { return coffee_->description() + " + 牛奶"; }
};

class SugarDecorator : public Coffee {
    std::unique_ptr<Coffee> coffee_;
public:
    explicit SugarDecorator(std::unique_ptr<Coffee> c) : coffee_(std::move(c)) {}
    double cost() const override { return coffee_->cost() + 1.0; }
    std::string description() const override { return coffee_->description() + " + 糖"; }
};

// 使用
auto coffee = std::make_unique<SugarDecorator>(
    std::make_unique<MilkDecorator>(
        std::make_unique<Espresso>()));
std::cout << coffee->description() << ": " << coffee->cost() << "元" << std::endl;
// 浓缩咖啡 + 牛奶 + 糖: 14元
```

### 命令模式

```cpp
#include <vector>
#include <memory>
#include <functional>

class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};

class CommandManager {
    std::vector<std::unique_ptr<Command>> history_;
    size_t current_ = 0;
public:
    void execute(std::unique_ptr<Command> cmd) {
        // 删除当前位置之后的历史
        history_.resize(current_);
        cmd->execute();
        history_.push_back(std::move(cmd));
        ++current_;
    }

    void undo() {
        if (current_ > 0) {
            --current_;
            history_[current_]->undo();
        }
    }

    void redo() {
        if (current_ < history_.size()) {
            history_[current_]->execute();
            ++current_;
        }
    }
};

// 使用 Lambda 实现轻量命令
class LambdaCommand : public Command {
    std::function<void()> do_;
    std::function<void()> undo_;
public:
    LambdaCommand(std::function<void()> d, std::function<void()> u)
        : do_(std::move(d)), undo_(std::move(u)) {}
    void execute() override { do_(); }
    void undo() override { undo_(); }
};
```

### 适配器模式

```cpp
#include <string>

// 第三方库的接口
class LegacyLogger {
public:
    void logMessage(int level, const char* msg) {
        std::cout << "[" << level << "] " << msg << std::endl;
    }
};

// 目标接口
class Logger {
public:
    virtual ~Logger() = default;
    virtual void info(const std::string& msg) = 0;
    virtual void error(const std::string& msg) = 0;
};

// 适配器
class LoggerAdapter : public Logger {
    LegacyLogger legacy_;
public:
    void info(const std::string& msg) override {
        legacy_.logMessage(0, msg.c_str());
    }
    void error(const std::string& msg) override {
        legacy_.logMessage(3, msg.c_str());
    }
};
```

## 常见场景

### Pimpl 惯用法（编译防火墙）

```cpp
// widget.h
class Widget {
public:
    Widget();
    ~Widget();
    void process();
private:
    struct Impl;
    std::unique_ptr<Impl> impl_;
};

// widget.cpp
struct Widget::Impl {
    std::vector<int> data;
    void process() { /* 复杂实现 */ }
};

Widget::Widget() : impl_(std::make_unique<Impl>()) {}
Widget::~Widget() = default;
void Widget::process() { impl_->process(); }
```

### CRTP 静态多态

```cpp
// CRTP 替代虚函数实现多态，零运行时开销
template<typename Derived>
class ShapeBase {
public:
    double area() const {
        return static_cast<const Derived*>(this)->computeArea();
    }
};

class Circle : public ShapeBase<Circle> {
    double radius_;
public:
    explicit Circle(double r) : radius_(r) {}
    double computeArea() const { return 3.14159 * radius_ * radius_; }
};

class Square : public ShapeBase<Square> {
    double side_;
public:
    explicit Square(double s) : side_(s) {}
    double computeArea() const { return side_ * side_; }
};
```

## 注意事项

- 不要为了使用模式而使用模式，模式是解决特定问题的工具，不是目标
- C++ 的 RAII 和智能指针可以替代许多传统模式中的资源管理代码
- Lambda 表达式可以简化策略、命令和观察者模式的实现
- 模板和 CRTP 可以在编译期实现某些模式，避免虚函数开销
- 单例模式应谨慎使用，全局状态会增加耦合和测试难度
- 过度使用设计模式会导致代码过度抽象，增加理解成本

## 进阶用法

### 类型擦除（现代 C++ 风格）

```cpp
#include <memory>
#include <functional>

// 使用类型擦除实现类似 std::function 的效果
class Drawable {
    struct Concept {
        virtual ~Concept() = default;
        virtual void draw() const = 0;
    };

    template<typename T>
    struct Model : Concept {
        T obj_;
        Model(T obj) : obj_(std::move(obj)) {}
        void draw() const override { obj_.draw(); }
    };

    std::shared_ptr<const Concept> impl_;
public:
    template<typename T>
    Drawable(T obj) : impl_(std::make_shared<Model<T>>(std::move(obj))) {}

    void draw() const { impl_->draw(); }
};

// 任何有 draw() 方法的类型都可以使用
struct Circle { void draw() const { std::cout << "画圆" << std::endl; } };
struct Square { void draw() const { std::cout << "画方" << std::endl; } };

Drawable d1 = Circle{};
Drawable d2 = Square{};
d1.draw();  // 画圆
d2.draw();  // 画方
```

### 依赖注入

```cpp
#include <memory>

// 接口
class ILogger {
public:
    virtual ~ILogger() = default;
    virtual void log(const std::string& msg) = 0;
};

// 具体实现
class ConsoleLogger : public ILogger {
public:
    void log(const std::string& msg) override {
        std::cout << "[LOG] " << msg << std::endl;
    }
};

// 依赖注入
class Service {
    std::shared_ptr<ILogger> logger_;
public:
    explicit Service(std::shared_ptr<ILogger> logger) : logger_(std::move(logger)) {}

    void doWork() {
        logger_->log("开始工作");
        // ...
        logger_->log("工作完成");
    }
};

// 使用
auto logger = std::make_shared<ConsoleLogger>();
Service svc(logger);
svc.doWork();
```
## 单例模式 Singleton

**基本写法：Meyers 单例**
`static <类型>& <实例>()`
```cpp
// 线程安全的局部静态变量
class Logger {
public:
    static Logger& instance() {
        static Logger inst; // C++11 起线程安全
        return inst;
    }
    Logger(const Logger&) = delete;
    Logger& operator=(const Logger&) = delete;
private:
    Logger() = default;
};
```

---

## 工厂模式 Factory

**基本写法：简单工厂**
`static <基类指针> create(<类型标识>)`
```cpp
// 根据参数创建不同子类
struct Shape { virtual void draw() = 0; virtual ~Shape() = default; };
struct Circle : Shape { void draw() override {} };
struct Square : Shape { void draw() override {} };

struct ShapeFactory {
    static std::unique_ptr<Shape> create(const std::string& kind) {
        if (kind == "circle") return std::make_unique<Circle>();
        if (kind == "square") return std::make_unique<Square>();
        return nullptr;
    }
};
```

---

**基本写法：抽象工厂**
`struct <抽象工厂接口> { virtual <产品> create() = 0; };`
```cpp
// 工厂接口与具体工厂
struct GUIFactory {
    virtual std::unique_ptr<class Button> makeButton() = 0;
    virtual ~GUIFactory() = default;
};
struct WinFactory : GUIFactory {
    std::unique_ptr<Button> makeButton() override;
};
struct MacFactory : GUIFactory {
    std::unique_ptr<Button> makeButton() override;
};
```

---

## 观察者模式 Observer

**基本写法：订阅/通知**
`<subject>.attach(<observer>); <subject>.notify();`
```cpp
#include <functional>
#include <vector>
struct Subject {
    using Slot = std::function<void(int)>;
    std::vector<Slot> observers;
    void attach(Slot s) { observers.push_back(std::move(s)); }
    void notify(int value) {
        for (auto& s : observers) s(value);
    }
};
// 使用
Subject s;
s.attach([](int v){ std::cout << v; });
s.notify(42);
```

---

## 策略模式 Strategy

**基本写法：函数对象策略**
`std::function<<签名>> <策略>`
```cpp
// 用 std::function 持有策略
struct Context {
    std::function<int(int, int)> strategy;
    int execute(int a, int b) { return strategy(a, b); }
};
Context c;
c.strategy = [](int a, int b){ return a + b; };
c.execute(2, 3); // 5
c.strategy = [](int a, int b){ return a * b; };
c.execute(2, 3); // 6
```

---

## RAII 资源管理

**基本写法：RAII 包装**
`struct <包装类> { <资源> res; ~<类>() { <释放>; } };`
```cpp
// 构造获取资源，析构释放
struct FileGuard {
    FILE* fp;
    explicit FileGuard(const char* path) : fp(fopen(path, "r")) {}
    ~FileGuard() { if (fp) fclose(fp); }
    FileGuard(const FileGuard&) = delete;
    FileGuard& operator=(const FileGuard&) = delete;
};
```

---

## Pimpl 惯用法

**基本写法：指针隐藏实现**
`struct <类> { struct Impl; std::unique_ptr<Impl> pimpl; };`
```cpp
// 头文件 widget.h
class Widget {
public:
    Widget();
    ~Widget(); // 需在源文件定义（因 unique_ptr 完整类型要求）
    void doWork();
private:
    struct Impl;
    std::unique_ptr<Impl> pimpl;
};
// 源文件 widget.cpp 中实现 Impl
```

---

## 模板方法模式

**基本写法：非虚接口模式**
`<基类> { public: void <模板方法>() final; private: virtual void <步骤>() = 0; };`
```cpp
// 基类定义算法骨架
struct Task {
    void run() {        // 模板方法
        step1();
        step2();
    }
    virtual ~Task() = default;
private:
    virtual void step1() = 0;
    virtual void step2() = 0;
};
struct MyTask : Task {
    void step1() override { /* */ }
    void step2() override { /* */ }
};
```

---

## 适配器模式 Adapter

**基本写法：对象适配器**
`struct <适配器> : <目标接口> { <被适配者> adaptee; };`
```cpp
// 适配不同接口
struct Target { virtual void request() = 0; virtual ~Target() = default; };
struct Adaptee { void specificRequest() {} };

struct Adapter : Target {
    Adaptee adaptee;
    void request() override { adaptee.specificRequest(); }
};
```

---

## 装饰器模式 Decorator

**基本写法：包装增强**
`struct <装饰器> : <组件> { <组件*> wrapped; };`
```cpp
// 递归包装
struct Component { virtual void op() = 0; virtual ~Component() = default; };
struct Decorator : Component {
    std::unique_ptr<Component> inner;
    void op() override { inner->op(); }
};
struct LoggingDecorator : Decorator {
    void op() override { std::cout << "log"; Decorator::op(); }
};
```

---

## 命令模式 Command

**基本写法：命令封装**
`struct <命令> { virtual void execute() = 0; };`
```cpp
// 将操作封装为对象
struct Command {
    virtual void execute() = 0;
    virtual ~Command() = default;
};
struct LightOnCmd : Command {
    void execute() override { /* 开灯 */ }
};
// 调用者持有命令
std::vector<std::unique_ptr<Command>> cmds;
cmds.push_back(std::make_unique<LightOnCmd>());
cmds.back()->execute();
```

---

## 现代模式速查

**基本写法：用 lambda 替代策略**
`auto <策略> = [](<参数>) { ... };`
```cpp
// 现代 C++ 倾向用 lambda/std::function 替代部分模式
std::vector<int> v = {3, 1, 4, 1, 5};
std::sort(v.begin(), v.end(), [](int a, int b){ return a > b; });
// 命令模式也可用 std::function
std::vector<std::function<void()>> actions;
actions.push_back([]{ std::cout << "hi"; });
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
| 设计模式与C++ | 012-DesignPatternCpp | 本文自身 |
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
