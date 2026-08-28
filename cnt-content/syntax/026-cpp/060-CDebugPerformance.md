# C/C++ 调试与性能分析

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 调试工具

**基本写法：gdb 调试**
`gdb <程序>`
```bash
# 启动 gdb
g++ -g -O0 main.cpp -o app
gdb ./app
# 常用命令
# break main / run / next / step / print x / backtrace
```

---

**基本写法：lldb 调试**
`lldb <程序>`
```bash
# clang 配套调试器
lldb ./app
lldb> breakpoint set --name main
lldb> run
lldb> frame variable
```

---

**基本写法：核心转储分析**
`gdb <程序> <core文件>`
```bash
# 分析崩溃转储
ulimit -c unlimited      # 启用 core
./app                    # 崩溃生成 core
gdb ./app core
gdb> bt                  # 查看崩溃栈
```

---

## 内存检测

**基本写法：AddressSanitizer**
`g++ -fsanitize=address -g`
```bash
# 内存错误检测（编译时）
g++ -fsanitize=address -g main.cpp -o app
./app
# 检测：堆栈溢出、释放后使用、双重释放、内存泄漏
```

---

**基本写法：MemorySanitizer**
`g++ -fsanitize=memory -g`
```bash
# 检测未初始化内存读取（clang）
clang++ -fsanitize=memory -g main.cpp -o app
./app
```

---

**基本写法：ThreadSanitizer**
`g++ -fsanitize=thread -g`
```bash
# 数据竞争检测
g++ -fsanitize=thread -g main.cpp -o app
./app
# 检测：多线程数据竞争、死锁
```

---

**基本写法：UndefinedBehaviorSanitizer**
`g++ -fsanitize=undefined -g`
```bash
# 未定义行为检测
g++ -fsanitize=undefined -g main.cpp -o app
./app
# 检测：整数溢出、空指针、除零等
```

---

## Valgrind

**基本写法：内存泄漏检测**
`valgrind --leak-check=full <程序>`
```bash
# 检测内存泄漏
valgrind --leak-check=full --show-leak-kinds=all ./app
# 输出：definitely lost / indirectly lost 等
```

---

**基本写法：调用图分析**
`valgrind --tool=callgrind <程序>`
```bash
# 性能分析
valgrind --tool=callgrind ./app
# 生成 callgrind.out.<pid>
callgrind_annotate callgrind.out.12345  # 查看报告
# 或用 kcachegrind 图形化查看
```

---

**基本写法：缓存分析**
`valgrind --tool=cachegrind <程序>`
```bash
# 缓存命中分析
valgrind --tool=cachegrind ./app
# 生成 cachegrind.out.<pid>
cg_annotate cachegrind.out.12345
```

---

## perf 性能分析

**基本写法：perf record**
`perf record -g <程序>`
```bash
# 采样性能数据
perf record -g ./app
perf report                    # 查看报告
perf report --sort=symbol      # 按符号排序
```

---

**基本写法：perf stat**
`perf stat <程序>`
```bash
# 统计硬件事件
perf stat ./app
# 输出：CPU 周期、指令数、缓存缺失等
perf stat -e cache-misses,cache-references ./app
```

---

**基本写法：perf top**
`perf top`
```bash
# 实时热点分析
perf top
perf top -p <pid>     # 指定进程
```

---

## 火焰图

**基本写法：生成火焰图**
`perf script | <flamegraph工具>`
```bash
# 生成火焰图（需 FlameGraph 工具）
perf record -F 99 -g ./app
perf script > out.perf
git clone https://github.com/brendangregg/FlameGraph
./FlameGraph/stackcollapse-perf.pl out.perf > out.folded
./FlameGraph/flamegraph.pl out.folded > flame.svg
```

---

## 编译诊断

**基本写法：警告选项**
`g++ -Wall -Wextra -Werror`
```bash
# 严格警告
g++ -Wall -Wextra -Wpedantic -Werror main.cpp
# 转换警告
g++ -Wconversion -Wsign-conversion main.cpp
```

---

**基本写法：静态分析**
`cppcheck --enable=all`
```bash
# 静态分析
cppcheck --enable=all --inconclusive main.cpp
cppcheck --xml --xml-version=2 main.cpp 2> report.xml
```

---

**基本写法：clang-tidy**
`clang-tidy -p <build> <源文件>`
```bash
# clang 静态检查
clang-tidy -p build main.cpp
clang-tidy -checks='bugprone-*,modernize-*,performance-*' main.cpp
```

---

## 时间测量

**基本写法：chrono 精确计时**
`std::chrono::high_resolution_clock`
```cpp
#include <chrono>
auto t1 = std::chrono::high_resolution_clock::now();
work();
auto t2 = std::chrono::high_resolution_clock::now();
auto ns = std::chrono::duration_cast<std::chrono::nanoseconds>(t2-t1).count();
std::cout << ns << " ns";
```

---

**基本写法：clock 测 CPU 时间**
`std::clock()`
```cpp
#include <ctime>
std::clock_t start = std::clock();
work();
double seconds = double(std::clock() - start) / CLOCKS_PER_SEC;
```
