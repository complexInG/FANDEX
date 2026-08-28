# C 构建系统 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## make 基本语法

**基本写法：Makefile 规则**
`<目标>: <依赖> [; <命令>]`
```makefile
# 目标、依赖、命令（命令行必须以 Tab 开头）
app: main.c utils.c
	gcc -o app main.c utils.c
```

**基本写法：伪目标**
`.PHONY: <目标>`
```makefile
# 声明不对应文件的目标，避免与同名文件冲突
.PHONY: clean
clean:
	rm -f app
```

**基本写法：变量定义**
`<变量名> := <值>`
```makefile
# := 立即展开赋值，= 延迟展开赋值
CC := gcc
CFLAGS := -Wall -O2
```

**基本写法：引用变量**
`$(<变量名>)`
```makefile
# 使用 $(...) 引用变量
$(CC) $(CFLAGS) -o app main.c
```

**基本写法：自动变量**
`$@ $< $^`
```makefile
# $@ 目标名 $< 第一个依赖 $^ 所有依赖
app: main.c utils.c
	$(CC) -o $@ $^
```

---

## make 调用命令

**基本写法：执行默认目标**
`make`
```bash
# 执行 Makefile 第一个目标
make
```

**基本写法：指定目标**
`make <目标>`
```bash
# 执行 clean 目标
make clean
```

**基本写法：指定 Makefile**
`make -f <文件>`
```bash
# 使用非默认名的 Makefile
make -f GNUmakefile
```

**基本写法：并行构建**
`make -j [<数量>]`
```bash
# 并行执行，-j 不限数量，-j4 限定 4 个任务
make -j4
```

**基本写法：传入变量**
`make <变量>=<值>`
```bash
# 命令行覆盖 Makefile 变量
make CC=clang CFLAGS="-O3"
```

**基本写法：仅打印不执行**
`make -n [<目标>]`
```bash
# 显示将要执行的命令但不实际执行
make -n
```

**基本写法：错误继续**
`make -k [<目标>]`
```bash
# 某目标失败时继续构建其他目标
make -k
```

**基本写法：显示执行过程**
`make V=1`
```bash
# 关闭静默模式，打印完整命令
make V=1
```

---

## make 模式规则与函数

**基本写法：模式规则**
`<前缀>%<后缀>: <前缀>%<后缀>`
```makefile
# % 通配符匹配，编译所有 .c 为 .o
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@
```

**基本写法：通配函数**
`$(wildcard <模式>)`
```makefile
# 展开通配符获取文件列表
SRCS := $(wildcard src/*.c)
```

**基本写法：字符串替换**
`$(patsubst <模式>, <替换>, <列表>)`
```makefile
# 将 .c 后缀替换为 .o
OBJS := $(patsubst %.c, %.o, $(SRCS))
```

**基本写法：简化替换**
`$(<列表>:<旧后缀>=<新后缀>)`
```makefile
# 简写的 patsubst
OBJS := $(SRCS:.c=.o)
```

**基本写法：目录处理**
`$(dir <名称>) / $(notdir <名称>) / $(basename <名称>)`
```makefile
# dir 取目录 notdir 取文件名 basename 去后缀
src := src/main.c
d := $(dir $(src))        # src/
f := $(notdir $(src))     # main.c
b := $(basename $(f))     # main
```

---

## make 常用内置变量

**基本写法：编译器变量**
`CC / CXX / AR / LD`
```makefile
# 内置默认编译器，C 用 CC，C++ 用 CXX
# CC 默认 cc，可在命令行覆盖
$(CC) -c main.c
```

**基本写法：标志变量**
`CFLAGS / CPPFLAGS / LDFLAGS / LDLIBS`
```makefile
# CFLAGS 编译选项 CPPFLAGS 预处理选项
# LDFLAGS 链接选项 LDLIBS 链接库
CFLAGS += -I./include
LDLIBS += -lm
```

---

## CMake 基础

**基本写法：CMake 最低版本**
`cmake_minimum_required(VERSION <版本>)`
```cmake
# 声明所需的 CMake 最低版本
cmake_minimum_required(VERSION 3.15)
```

**基本写法：声明项目**
`project(<名称> [VERSION <x.y.z>] [LANGUAGES <语言>])`
```cmake
# 声明项目名称、版本与使用的语言
project(myapp VERSION 1.0.0 LANGUAGES C)
```

**基本写法：生成可执行文件**
`add_executable(<目标> <源文件>...)`
```cmake
# 由源文件构建可执行目标
add_executable(app main.c utils.c)
```

**基本写法：生成静态库**
`add_library(<名称> STATIC <源文件>...)`
```cmake
# 构建静态库 lib<名称>.a
add_library(utils STATIC utils.c)
```

**基本写法：生成动态库**
`add_library(<名称> SHARED <源文件>...)`
```cmake
# 构建动态库 lib<名称>.so
add_library(mylib SHARED mylib.c)
```

---

## CMake 链接与依赖

**基本写法：链接库**
`target_link_libraries(<目标> <库>...)`
```cmake
# 为目标链接其他库
target_link_libraries(app utils m)
```

**基本写法：包含目录**
`target_include_directories(<目标> <模式> <目录>...)`
```cmake
# 添加头文件搜索路径，PUBLIC 对外可见
target_include_directories(app PUBLIC include)
```

**基本写法：设置编译选项**
`target_compile_options(<目标> <模式> <选项>...)`
```cmake
# 为目标添加编译选项
target_compile_options(app PRIVATE -Wall -O2)
```

**基本写法：设置宏定义**
`target_compile_definitions(<目标> <模式> <名称>=<值>)`
```cmake
# 添加预处理宏
target_compile_definitions(app PRIVATE DEBUG=1)
```

**基本写法：查找系统库**
`find_package(<包> [REQUIRED] [COMPONENTS <组件>])`
```cmake
# 查找并加载已安装的第三方库
find_package(Threads REQUIRED)
target_link_libraries(app Threads::Threads)
```

---

## CMake 变量与条件

**基本写法：设置变量**
`set(<变量> <值>)`
```cmake
# 设置普通变量
set(SRCS main.c utils.c)
```

**基本写法：列表追加**
`list(APPEND <列表> <元素>)`
```cmake
# 向列表变量追加元素
list(APPEND SRCS extra.c)
```

**基本写法：条件判断**
`if(<条件>) ... elseif() ... else() ... endif()`
```cmake
# 按构建类型或平台分支
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    add_compile_options(-g -O0)
endif()
```

**基本写法：选项开关**
`option(<名称> "<说明>" <默认值>)`
```cmake
# 声明可配置的布尔开关
option(BUILD_TESTS "Build unit tests" ON)
if(BUILD_TESTS)
    add_subdirectory(tests)
endif()
```

---

## CMake 构建命令

**基本写法：生成构建系统**
`cmake -S <源目录> -B <构建目录>`
```bash
# 在 build 目录生成构建文件，源码在当前目录
cmake -S . -B build
```

**基本写法：指定生成器**
`cmake -G <生成器> -S <源> -B <构建>`
```bash
# 指定构建系统生成器
cmake -G "Unix Makefiles" -S . -B build
cmake -G Ninja -S . -B build
```

**基本写法：指定构建类型**
`cmake -DCMAKE_BUILD_TYPE=<类型> -S <源> -B <构建>`
```bash
# 常见类型：Debug Release RelWithDebInfo MinSizeRel
cmake -DCMAKE_BUILD_TYPE=Release -S . -B build
```

**基本写法：执行构建**
`cmake --build <构建目录> [--target <目标>]`
```bash
# 跨生成器统一构建命令
cmake --build build
cmake --build build --target clean
```

**基本写法：并行构建**
`cmake --build <构建目录> --parallel [<数量>]`
```bash
# 并行编译，-j 不限数量
cmake --build build -j8
```

**基本写法：安装**
`cmake --install <构建目录>`
```bash
# 按配置的 install 规则安装
cmake --install build --prefix /usr/local
```

---

## CMake 安装规则

**基本写法：安装目标**
`install(TARGETS <目标>...)`
```cmake
# 安装可执行文件或库到默认路径
install(TARGETS app LIBRARY DESTINATION lib RUNTIME DESTINATION bin)
```

**基本写法：安装头文件**
`install(FILES <文件> DESTINATION <目录>)`
```cmake
# 安装头文件到 include 目录
install(FILES mylib.h DESTINATION include)
```

**基本写法：安装目录**
`install(DIRECTORY <目录> DESTINATION <目标>)`
```cmake
# 递归安装整个目录
install(DIRECTORY include/ DESTINATION include)
```

---

## CMake 子项目组织

**基本写法：包含子目录**
`add_subdirectory(<目录>)`
```cmake
# 将子目录的 CMakeLists.txt 纳入构建
add_subdirectory(src)
add_subdirectory(lib/utils)
```

**基本写法：自定义命令**
`add_custom_command(OUTPUT <产物> COMMAND <命令>)`
```cmake
# 生成文件的自定义规则
add_custom_command(OUTPUT gen.c
    COMMAND python gen.py > gen.c
    DEPENDS gen.py)
```

**基本写法：自定义目标**
`add_custom_target(<名称> COMMAND <命令>)`
```cmake
# 不产生文件的目标，便于聚合任务
add_custom_target(run COMMAND app DEPENDS app)
```