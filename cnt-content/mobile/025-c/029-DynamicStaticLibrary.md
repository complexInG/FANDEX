# C 动态静态库

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 静态库创建

**基本写法：编译目标文件**
`gcc -c <源文件> -o <目标.o>`
```c
// 编译生成目标文件
gcc -c libfoo.c -o libfoo.o
```

---

**基本写法：创建静态库**
`ar rcs <库文件.a> <目标文件>...`
```c
// 打包目标文件为静态库
ar rcs libfoo.a libfoo.o
```

---

**基本写法：查看静态库内容**
`ar -t <库文件.a>`
```c
// 列出库中的目标文件
ar -t libfoo.a
```

---

**基本写法：链接静态库**
`gcc <主文件> -L<路径> -l<库名> -o <输出>`
```c
// 链接当前目录的 libfoo.a
gcc main.c -L. -lfoo -o main
```

---

## 动态库创建

**基本写法：编译位置无关代码**
`gcc -fPIC -c <源文件> -o <目标.o>`
```c
// 生成位置无关目标文件
gcc -fPIC -c libfoo.c -o libfoo.o
```

---

**基本写法：创建动态库**
`gcc -shared -o <库文件.so> <目标文件>...`
```c
// 链接为动态共享库
gcc -shared -o libfoo.so libfoo.o
```

---

**基本写法：指定版本**
`gcc -shared -Wl,-soname,<库名.so.1> -o <库.so.1.0> <目标>`
```c
// 设置共享库版本
gcc -shared -Wl,-soname,libfoo.so.1 -o libfoo.so.1.0 libfoo.o
```

---

**基本写法：链接动态库**
`gcc <主文件> -L<路径> -l<库名> -o <输出>`
```c
// 链接动态库 libfoo.so
gcc main.c -L. -lfoo -o main
```

---

**基本写法：运行时指定库路径**
`LD_LIBRARY_PATH=<路径> ./<程序>`
```c
// 运行时设置库搜索路径
LD_LIBRARY_PATH=. ./main
```

---

**基本写法：链接时指定运行时路径**
`gcc -Wl,-rpath,<路径> <其他参数>`
```c
// 内嵌运行时搜索路径
gcc main.c -L. -lfoo -Wl,-rpath,. -o main
```

---

## 运行时加载 dlopen

**基本写法：打开动态库**
`dlopen(<库路径>, RTLD_LAZY);`
```c
// 运行时加载共享库
void* handle = dlopen("./libfoo.so", RTLD_LAZY);
```

---

**基本写法：获取符号**
`dlsym(<handle>, <符号名>);`
```c
// 取得函数指针
typedef int (*func_t)(int);
func_t f = (func_t)dlsym(handle, "add");
```

---

**基本写法：调用动态函数**
`<函数指针>(<参数>);`
```c
// 调用从动态库取得的函数
int r = f(42);
```

---

**基本写法：关闭动态库**
`dlclose(<handle>);`
```c
// 卸载动态库
dlclose(handle);
```

---

**基本写法：获取错误信息**
`dlerror();`
```c
// 查询最近一次错误
const char* err = dlerror();
```

---

**基本写法：编译需链接 dl**
`gcc <文件> -ldl -o <输出>`
```c
// 链接 dl 库使用 dlopen
gcc main.c -ldl -o main
```

---

## 库的导出符号

**基本写法：默认导出**
`int <函数>(...) { }`
```c
// 默认所有全局符号导出
int add(int a, int b) { return a + b; }
```

---

**基本写法：可见性控制**
`__attribute__((visibility("default"))) int <函数>();`
```c
// 显式声明导出
__attribute__((visibility("default"))) int add(int a, int b);
```

---

**基本写法：隐藏符号**
`__attribute__((visibility("hidden"))) int <函数>();`
```c
// 隐藏不导出
__attribute__((visibility("hidden"))) static int helper();
```

---

**基本写法：默认隐藏编译**
`gcc -fvisibility=hidden -shared ...`
```c
// 默认隐藏所有符号
gcc -fvisibility=hidden -shared -o libfoo.so libfoo.o
```

---

## 库查询工具

**基本写法：查看依赖**
`ldd <程序>`
```c
// 查看程序依赖的动态库
ldd ./main
```

---

**基本写法：列出符号**
`nm <库文件>`
```c
// 查看库中的符号表
nm libfoo.a
```

---

**基本写法：查看动态符号**
`nm -D <库.so>`
```c
// 查看动态库导出符号
nm -D libfoo.so
```

---

**基本写法：查看符号所属库**
`readelf -d <库.so>`
```c
// 查看动态库信息
readelf -d libfoo.so
```

---

## 头文件与库组织

**基本写法：声明导出函数**
`<头文件.h>` 中声明
```c
// 头文件中声明供外部使用
#ifndef FOO_H
#define FOO_H
int add(int a, int b);
#endif
```

---

**基本写法：使用库**
`#include <<头文件>>` 编译链接
```c
// 主程序使用库
#include "foo.h"
int r = add(1, 2);
```
