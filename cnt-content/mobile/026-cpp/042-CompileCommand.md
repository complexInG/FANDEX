# C++ 编译命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## g++/gcc 编译

**基本写法：基础编译**
`g++ <源文件> -o <输出文件>`
```bash
# 编译单个文件
g++ main.cpp -o main
# 运行
./main
```

---

**基本写法：指定 C++ 标准**
`g++ -std=<标准> <源文件>`
```bash
# 指定语言标准
g++ -std=c++20 main.cpp -o main
g++ -std=c++23 main.cpp -o main
g++ -std=c++17 main.cpp -o main
```

---

**基本写法：优化级别**
`g++ -O<级别> <源文件>`
```bash
# 优化选项
g++ -O0 main.cpp -o main   # 不优化（调试用）
g++ -O1 main.cpp -o main   # 基本优化
g++ -O2 main.cpp -o main   # 标准优化（推荐）
g++ -O3 main.cpp -o main   # 激进优化
g++ -Os main.cpp -o main   # 优化体积
g++ -Ofast main.cpp -o main # O3 + 快速数学
```

---

**基本写法：警告选项**
`g++ -W<警告> <源文件>`
```bash
# 常用警告
g++ -Wall main.cpp          # 常用警告
g++ -Wextra main.cpp        # 额外警告
g++ -Werror main.cpp        # 警告视为错误
g++ -Wpedantic main.cpp     # 严格标准
g++ -Wall -Wextra -Werror main.cpp # 组合
```

---

**基本写法：包含与库路径**
`g++ -I<路径> -L<路径> -l<库> <源文件>`
```bash
# 头文件搜索路径、库搜索路径、链接库
g++ -I./include -L./lib -lmylib main.cpp -o main
# -I  头文件搜索路径
# -L  库文件搜索路径
# -l  链接库（libmylib.so / libmylib.a）
```

---

**基本写法：生成调试信息**
`g++ -g <源文件>`
```bash
# 生成调试信息（配合 gdb）
g++ -g -O0 main.cpp -o main
# -g         生成调试信息
# -ggdb      生成 gdb 专用调试信息
# -g3        最详细调试信息
```

---

**基本写法：多文件编译**
`g++ <源1> <源2> ... -o <输出>`
```bash
# 多文件一起编译
g++ main.cpp utils.cpp io.cpp -o app
```

---

**基本写法：分步编译**
`g++ -c <源文件>` → `g++ <对象文件> -o <输出>`
```bash
# 先编译为目标文件
g++ -c main.cpp -o main.o
g++ -c utils.cpp -o utils.o
# 再链接
g++ main.o utils.o -o app
```

---

**基本写法：生成静态库**
`ar rcs <库文件> <对象文件>...`
```bash
# 打包目标文件为静态库
g++ -c utils.cpp -o utils.o
ar rcs libutils.a utils.o
# 使用静态库
g++ main.cpp -L. -lutils -o app
```

---

**基本写法：生成动态库**
`g++ -shared -fPIC -o <库文件> <源文件>`
```bash
# 编译为动态库
g++ -shared -fPIC -o libutils.so utils.cpp
# -fPIC  位置无关代码
# -shared 生成共享库
# 使用动态库
g++ main.cpp -L. -lutils -o app
LD_LIBRARY_PATH=. ./app
```

---

## clang++ 编译

**基本写法：clang++ 基础**
`clang++ <选项> <源文件>`
```bash
# clang++ 与 g++ 选项基本兼容
clang++ -std=c++20 -O2 main.cpp -o main
# 使用 libc++ 标准库
clang++ -stdlib=libc++ -std=c++20 main.cpp -o main
```

---

**基本写法：clang 静态分析**
`clang++ --analyze <源文件>`
```bash
# 静态分析
clang++ --analyze main.cpp
# 生成分析报告
scan-build g++ main.cpp -o main
```

---

## MSVC cl 编译

**基本写法：cl 基础**
`cl [选项] <源文件>`
```bash
# MSVC 编译
cl /std:c++20 /EHsc main.cpp
# /std:c++20  C++20 标准
# /EHsc       启用异常
# /O2         优化
# /Fe:out.exe 指定输出名
```

---

**基本写法：MSVC 头文件与库**
`cl /I<路径> <源文件> /link /LIBPATH:<路径> <库>.lib`
```bash
# 包含路径与链接库
cl /Iinclude main.cpp /link /LIBPATH:lib utils.lib
```

---

## 预处理与汇编

**基本写法：只预处理**
`g++ -E <源文件>`
```bash
# 输出预处理结果
g++ -E main.cpp -o main.ii
```

---

**基本写法：只编译为汇编**
`g++ -S <源文件>`
```bash
# 生成汇编代码
g++ -S main.cpp -o main.s
```

---

**基本写法：生成目标文件**
`g++ -c <源文件>`
```bash
# 只编译不链接
g++ -c main.cpp -o main.o
```

---

## 其他常用选项

**基本写法：开启全部特性**
`g++ -std=c++20 -O2 -Wall -Wextra -g <源文件>`
```bash
# 推荐开发组合
g++ -std=c++20 -O2 -Wall -Wextra -g -fsanitize=address main.cpp -o main
# -fsanitize=address  地址消毒器（检测内存错误）
# -fsanitize=undefined 未定义行为检测
```

---

**基本写法：多线程链接**
`g++ -pthread <源文件>`
```bash
# 链接 pthread 库（Linux）
g++ -std=c++20 -pthread main.cpp -o main
```

---

**基本写法：查看编译选项**
`g++ --help` `g++ -v`
```bash
# 查看帮助与版本
g++ --help
g++ -v              # 详细版本与配置
g++ -dM -E -x c++ /dev/null | sort # 查看预定义宏
```
