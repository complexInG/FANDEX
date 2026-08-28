# C++ 工具链

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 编译器

**基本写法：查看版本**
`<编译器> --version`
```bash
# 主流编译器版本查看
g++ --version
clang++ --version
cl 2>&1 | findstr Version   # MSVC
```

---

**基本写法：查看默认标准**
`g++ -dM -E -x c++ /dev/null | grep __cplusplus`
```bash
# 查看编译器默认 C++ 标准宏
g++ -dM -E -x c++ /dev/null | grep __cplusplus
# 202002L 表示 C++20
```

---

**基本写法：查看支持的特性**
`g++ -std=c++2a -dM -E -x c++ /dev/null`
```bash
# 检查特性宏支持
g++ -std=c++20 -dM -E -x c++ /dev/null | grep cpp_impl
# __cpp_impl_coroutine 201902L  支持协程
# __cpp_impl_three_way_comparison 201907L
```

---

## 构建工具

**基本写法：CMake**
`cmake -S . -B build && cmake --build build`
```bash
# CMake 标准流程
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j 8
cmake --install build
```

---

**基本写法：Make**
`make [目标]`
```bash
# 直接用 make
make              # 默认目标
make app          # 指定目标
make -j 8         # 并行 8 任务
make clean        # 清理
make install      # 安装
```

---

**基本写法：Ninja**
`ninja [目标]`
```bash
# Ninja 更快的构建工具
ninja          # 构建
ninja -j 8     # 并行
ninja clean    # 清理
```

---

**基本写法：Meson**
`meson setup <构建目录>`
```bash
# Meson 构建系统
meson setup build
ninja -C build
meson compile -C build
meson install -C build
```

---

**基本写法：Bazel**
`bazel build //<目标>`
```bash
# Bazel 构建工具
bazel build //main:app
bazel test //...
bazel run //main:app
```

---

## 包管理器

**基本写法：vcpkg**
`vcpkg install <包>`
```bash
# vcpkg 包管理
vcpkg install fmt
vcpkg install boost-system
# 配合 CMake
cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE=<vcpkg>/scripts/buildsystems/vcpkg.cmake
```

---

**基本写法：Conan**
`conan install .`
```bash
# Conan 包管理
conan install . --output-folder=build --build=missing
conan profile new default --detect
# conanfile.txt 示例：
# [requires]
# fmt/10.1.1
```

---

**基本写法：FetchContent（CMake）**
`FetchContent_Declare(<名称> ...)`
```cmake
# CMake 内置下载依赖
include(FetchContent)
FetchContent_Declare(
    fmt
    GIT_REPOSITORY https://github.com/fmtlib/fmt.git
    GIT_TAG 10.1.1
)
FetchContent_MakeAvailable(fmt)
target_link_libraries(app PRIVATE fmt::fmt)
```

---

## 静态分析

**基本写法：clang-tidy**
`clang-tidy <源文件> -- -std=c++20`
```bash
# 静态分析工具
clang-tidy main.cpp -- -std=c++20
# 指定检查规则
clang-tidy -checks='bugprone-*,modernize-*' main.cpp -- -std=c++20
# 生成 .clang-tidy 配置
clang-tidy -dump-config > .clang-tidy
```

---

**基本写法：cppcheck**
`cppcheck <源文件>`
```bash
# C/C++ 静态分析
cppcheck --enable=all main.cpp
cppcheck --std=c++20 --enable=warning,style main.cpp
cppcheck --xml --xml-version=2 main.cpp 2> report.xml
```

---

**基本写法：include-what-you-use**
`include-what-you-use <源文件>`
```bash
# 检查头文件使用
include-what-you-use main.cpp
```

---

## 格式化与 Lint

**基本写法：clang-format**
`clang-format -i <源文件>`
```bash
# 代码格式化
clang-format -i main.cpp
clang-format -i src/*.cpp
# 生成配置
clang-format -style=google -dump-config > .clang-format
# 检查是否需格式化
clang-format --dry-run --Werror main.cpp
```

---

**基本写法：clang-tidy 修复**
`clang-tidy --fix <源文件>`
```bash
# 自动修复
clang-tidy -p build --fix main.cpp
```

---

## 文档生成

**基本写法：Doxygen**
`doxygen <配置文件>`
```bash
# 生成 API 文档
doxygen -g          # 生成 Doxyfile
doxygen Doxyfile    # 生成文档
```

---

## 性能分析工具

**基本写法：perf**
`perf record ./app`
```bash
# Linux 性能分析
perf record ./app
perf report
perf stat ./app
```

---

**基本写法：Valgrind**
`valgrind ./app`
```bash
# 内存检测
valgrind --leak-check=full ./app
valgrind --tool=callgrind ./app  # 性能分析
valgrind --tool=massif ./app     # 堆分析
```
