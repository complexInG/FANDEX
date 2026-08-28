# C++ 设计模式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
