---
order: 10
title: c 模块文档合集
module: 'c'
category: 计算机科学
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：025-c/001-VariableConstant.md ============ -->

# 变量与常量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量定义与初始化

**基本写法：声明变量**
`<type> <var_name>;`
```c
// 声明整型变量（未初始化，值为随机值）
int a;
```

---

**初始化写法：声明并初始化**
`<type> <var_name> = <value>;`
```c
// 声明变量 b 并初始化为 20
int b = 20;
```

---

**单行写法：多变量声明**
`<type> <var1>, <var2> = <value>, <var3> = <value>;`
```c
// 同时声明并初始化多个变量
int m = 10, n = 20, p = 30;
```

---

**赋值写法：先声明后赋值**
`<var_name> = <value>;`
```c
// 先声明变量再赋值
int a;
a = 10;
```

---

## 存储类

**基本写法：auto 存储类**
`auto <type> <var_name> = <value>;`
```c
// 显式声明 auto 存储类（通常省略）
auto int x = 10;
```

---

**基本写法：static 局部变量**
`static <type> <var_name> = <value>;`
```c
// 静态局部变量，函数结束后不销毁
void counter() {
    static int count = 0;
    count++;
    printf("Count: %d\n", count);
}
```

---

**基本写法：static 全局变量**
`static <type> <var_name> = <value>;`
```c
// 全局静态变量，仅限当前文件访问
static int file_static = 100;
```

---

**基本写法：extern 外部变量声明**
`extern <type> <var_name>;`
```c
// 声明在其他文件中定义的外部变量
extern int global_var;
```

---

**基本写法：register 存储类**
`register <type> <var_name>;`
```c
// 建议将变量存储在寄存器中
register int i;
```

---

## 字面常量

**十进制写法：整数常量**
`<decimal>`
```c
// 十进制整数
int a = 100;
```

---

**十六进制写法：整数常量**
`0x<hex>`
```c
// 十六进制表示 31
int a = 0x1F;
```

---

**八进制写法：整数常量**
`0<octal>`
```c
// 八进制表示 8
int a = 010;
```

---

**二进制写法：整数常量（C99+）**
`0b<binary>`
```c
// 二进制表示 10
int a = 0b1010;
```

---

**后缀写法：整数常量后缀**
`<number>[U|L|UL|LL]`
```c
// 无符号长整数
unsigned long val = 100UL;
```

---

**基本写法：浮点常量**
`<digits>.<digits>[f|L]`
```c
// 单精度浮点数
float f = 3.14f;
```

---

**科学记数法写法：浮点常量**
`<digits>e<exp>`
```c
// 科学记数法表示 0.0025
double d = 2.5e-3;
```

---

**基本写法：字符常量**
`'<char>'`
```c
// 普通字符常量
char c = 'A';
```

---

**转义写法：字符常量**
`'<escape>'`
```c
// 换行符字符常量
char c = '\n';
```

---

**基本写法：字符串常量**
`"<string>"`
```c
// 字符串常量
char *str = "Hello C";
```

---

## 宏定义常量

**基本写法：无参宏定义常量**
`#define <NAME> <value>`
```c
// 定义缓冲区大小常量
#define MAX_BUFFER 1024
```

---

**基本写法：带参宏定义**
`#define <NAME>(<params>) <expression>`
```c
// 定义求最大值的宏
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

---

## const 常量

**基本写法：定义 const 常量**
`const <type> <NAME> = <value>;`
```c
// 定义只读常量
const int DAYS_IN_WEEK = 7;
```

---

**基本写法：指向常量的指针**
`const <type>* <ptr>;`
```c
// 不能通过指针修改所指向的值
const int* p1;
```

---

**基本写法：常量指针**
`<type>* const <ptr> = &<var>;`
```c
// 指针本身不能改变指向
int* const p3 = &x;
```

---

**基本写法：指向常量的常量指针**
`const <type>* const <ptr> = &<var>;`
```c
// 既不能修改值，也不能修改指针
const int* const p4 = &x;
```

---

## 枚举常量

**基本写法：默认枚举值**
`enum <Name> { <MEM1>, <MEM2>, ... };`
```c
// 默认从 0 开始递增
enum Days { SUN, MON, TUE, WED };
```

---

**自定义写法：指定枚举值**
`enum <Name> { <MEM1> = <val>, <MEM2>, ... };`
```c
// 从 1 开始递增
enum Months { JAN = 1, FEB, MAR, APR };
```

---

## 左值与右值

**赋值写法：左值与右值**
`<lvalue> = <rvalue>;`
```c
// x 是左值，10 是右值
int x = 10;
```



<!-- ============ 文档分隔线：025-c/002-ProgramStructureBasicSyntax.md ============ -->

# 程序结构与基本语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 源文件结构

**基本写法：包含头文件**
`#include <<header>>`
```c
// 包含标准输入输出头文件
#include <stdio.h>
```

---

**基本写法：宏定义**
`#define <NAME> <value>`
```c
// 定义圆周率常量
#define PI 3.14159
```

---

**基本写法：类型定义**
`typedef <type> <new_name>;`
```c
// 为 unsigned int 创建别名
typedef unsigned int uint;
```

---

**基本写法：全局变量声明**
`<type> <var_name> = <value>;`
```c
// 声明全局变量并初始化
int global_count = 0;
```

---

**基本写法：函数原型声明**
`<return_type> <func_name>(<parameter_list>);`
```c
// 声明函数原型
void print_hello();
```

---

**基本写法：主函数入口**
`int main() { ... return 0; }`
```c
// 程序主入口
int main() {
    int local_val = 10;
    printf("Value: %d\n", local_val);
    return 0;
}
```

---

**基本写法：函数实现**
`<return_type> <func_name>(<parameter_list>) { ... }`
```c
// 函数具体实现
void print_hello() {
    printf("Hello!\n");
}
```

---

## 头文件保护

**基本写法：防止重复包含**
`#ifndef <HEADER_H> / #define <HEADER_H> / ... / #endif`
```c
// 头文件保护宏
#ifndef MY_HEADER_H
#define MY_HEADER_H
void my_function();
#endif /* MY_HEADER_H */
```

---

## 注释

**单行写法：行内注释**
`// <注释内容>`
```c
// 这是一个单行注释
int x = 10;
```

---

**单行写法：行尾注释**
`<code> // <注释内容>`
```c
// 行尾注释说明变量用途
int x = 10; // 计数器变量
```

---

**多行写法：块注释**
`/* <注释内容> */`
```c
/*
 * 这是一个多行注释
 * 可以跨越多行
 */
int y = 20;
```

---

**文档写法：Doxygen 格式**
`/** @brief <描述> @param <参数> <说明> @return <返回值> */`
```c
/**
 * @brief 计算圆的面积
 * @param radius 圆的半径
 * @return 圆的面积
 */
double calculate_area(double radius) {
    return PI * radius * radius;
}
```

---

## 主函数

**无参写法：无参数主函数**
`int main() { ... return 0; }`
```c
// 无参数形式的 main 函数
int main() {
    printf("Hello\n");
    return 0;
}
```

---

**带参写法：命令行参数主函数**
`int main(int argc, char *argv[]) { ... }`
```c
// argc 为参数个数，argv 为参数字符串数组
int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    return 0;
}
```

---

## 程序终止

**正常写法：正常终止程序**
`return 0;`
```c
// 在 main 函数中正常返回
int main() {
    printf("Done\n");
    return 0;
}
```

---

**强制写法：调用 exit 终止**
`exit(0);`
```c
// 直接终止整个程序
exit(0);
```

---

**异常写法：异常终止程序**
`exit(1);`
```c
// 非零状态码表示异常终止
exit(1);
```

---

## 编译命令

**单文件写法：编译单个源文件**
`gcc <source.c> -o <output>`
```bash
# 编译 hello.c 生成可执行文件 hello
gcc hello.c -o hello
```

---

**优化写法：启用优化编译**
`gcc -O2 <source.c> -o <output>`
```bash
# 启用二级优化
gcc -O2 hello.c -o hello
```

---

**调试写法：生成调试信息**
`gcc -g <source.c> -o <output>`
```bash
# 生成调试信息便于 GDB 调试
gcc -g hello.c -o hello
```

---

**多文件写法：编译多个源文件**
`gcc <file1.c> <file2.c> -o <output>`
```bash
# 一次性编译多个源文件
gcc file1.c file2.c -o program
```

---

**分步写法：分别编译后链接**
`gcc -c <source.c> -o <object.o>`
```bash
# 编译 file1.c 生成目标文件
gcc -c file1.c -o file1.o
```

---

**链接写法：链接目标文件**
`gcc <file1.o> <file2.o> -o <output>`
```bash
# 链接多个目标文件生成可执行文件
gcc file1.o file2.o -o program
```



<!-- ============ 文档分隔线：025-c/003-DynamicMemoryManagement.md ============ -->

# 动态内存管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## malloc 分配内存

**基本写法：分配单个变量内存**
`<type> *<ptr> = (<type> *)malloc(sizeof(<type>));`
```c
#include <stdlib.h>
// 分配单个整型变量的内存
int *p = (int *)malloc(sizeof(int));
```

---

**数组写法：分配数组内存**
`<type> *<ptr> = (<type> *)malloc(<count> * sizeof(<type>));`
```c
#include <stdlib.h>
// 分配 10 个整型元素的数组内存
int *arr = (int *)malloc(10 * sizeof(int));
```

---

**检查写法：检查分配是否成功**
`if (<ptr> == NULL) { ... }`
```c
// 检查内存分配是否成功
int *p = (int *)malloc(sizeof(int));
if (p == NULL) {
    printf("Memory allocation failed\n");
    exit(1);
}
```

---

## calloc 分配并清零

**基本写法：分配并初始化为 0**
`<type> *<ptr> = (<type> *)calloc(<count>, sizeof(<type>));`
```c
#include <stdlib.h>
// 分配 10 个整型元素并初始化为 0
int *arr = (int *)calloc(10, sizeof(int));
```

---

## realloc 调整内存大小

**基本写法：重新调整内存大小**
`<type> *<new_ptr> = (<type> *)realloc(<ptr>, <new_size> * sizeof(<type>));`
```c
#include <stdlib.h>
// 将数组大小调整为 20
int *new_arr = (int *)realloc(arr, 20 * sizeof(int));
```

---

**安全写法：使用临时变量接收 realloc 结果**
`<type> *<tmp> = (<type> *)realloc(<ptr>, <new_size>); if (<tmp>) { <ptr> = <tmp>; }`
```c
// 使用临时变量避免分配失败时丢失原指针
int *tmp = (int *)realloc(arr, 20 * sizeof(int));
if (tmp != NULL) {
    arr = tmp;
}
```

---

## free 释放内存

**基本写法：释放内存**
`free(<ptr>);`
```c
#include <stdlib.h>
// 释放动态分配的内存
free(p);
```

---

**安全写法：释放后置空**
`free(<ptr>); <ptr> = NULL;`
```c
// 释放内存后将指针置空
free(p);
p = NULL;
```

---

## 动态数组

**创建写法：创建动态数组**
`<type> *<arr> = (<type> *)malloc(<size> * sizeof(<type>));`
```c
#include <stdlib.h>
// 创建动态整型数组
int size = 10;
int *arr = (int *)malloc(size * sizeof(int));
```

---

**访问写法：访问动态数组元素**
`<arr>[<index>]`
```c
// 访问动态数组元素
arr[0] = 10;
arr[1] = 20;
```

---

**扩容写法：动态数组扩容**
`<type> *<new_arr> = (<type> *)realloc(<arr>, <new_size> * sizeof(<type>));`
```c
// 将动态数组从 10 扩容到 20
int *new_arr = (int *)realloc(arr, 20 * sizeof(int));
if (new_arr != NULL) {
    arr = new_arr;
    size = 20;
}
```

---

## 动态结构体

**分配写法：分配结构体内存**
`<StructType> *<ptr> = (<StructType> *)malloc(sizeof(<StructType>));`
```c
#include <stdlib.h>
// 分配结构体内存
typedef struct { int x; int y; } Point;
Point *p = (Point *)malloc(sizeof(Point));
```

---

**成员访问写法：通过指针访问结构体成员**
`<ptr>-><member>`
```c
// 通过指针访问结构体成员
p->x = 10;
p->y = 20;
```

---

**数组写法：分配结构体数组**
`<StructType> *<arr> = (<StructType> *)malloc(<count> * sizeof(<StructType>));`
```c
// 分配结构体数组
Point *points = (Point *)malloc(5 * sizeof(Point));
```

---

## 动态字符串

**分配写法：分配字符串内存**
`char *<str> = (char *)malloc(<size> * sizeof(char));`
```c
#include <stdlib.h>
// 分配字符串内存
char *str = (char *)malloc(100 * sizeof(char));
```

---

**复制写法：复制字符串到动态内存**
`strcpy(<dest>, <src>);`
```c
#include <string.h>
// 复制字符串到动态内存
char *str = (char *)malloc(100 * sizeof(char));
strcpy(str, "Hello");
```

---

## 二维动态数组

**分配写法：分配二维数组**
`<type> **<arr> = (<type> **)malloc(<rows> * sizeof(<type> *));`
```c
#include <stdlib.h>
// 分配行指针数组
int rows = 3;
int **arr = (int **)malloc(rows * sizeof(int *));
```

---

**行分配写法：为每行分配内存**
`<arr>[<i>] = (<type> *)malloc(<cols> * sizeof(<type>));`
```c
// 为每行分配列内存
int cols = 4;
for (int i = 0; i < rows; i++) {
    arr[i] = (int *)malloc(cols * sizeof(int));
}
```

---

**访问写法：访问二维动态数组元素**
`<arr>[<row>][<col>]`
```c
// 访问二维动态数组元素
arr[0][0] = 1;
arr[1][2] = 5;
```

---

**释放写法：释放二维动态数组**
`for (...) { free(<arr>[<i>]); } free(<arr>);`
```c
// 先释放每行，再释放行指针数组
for (int i = 0; i < rows; i++) {
    free(arr[i]);
}
free(arr);
```

---

## 内存泄漏检测

**基本写法：使用 valgrind 检测内存泄漏**
`valgrind --leak-check=full ./<program>`
```bash
# 使用 valgrind 检测内存泄漏
valgrind --leak-check=full ./myprogram
```

---

## 内存管理最佳实践

**配对写法：每个 malloc 对应一个 free**
`<type> *<ptr> = malloc(...); ... free(<ptr>);`
```c
// 确保每个 malloc 都有对应的 free
int *p = (int *)malloc(sizeof(int));
// 使用 p
free(p);
p = NULL;
```

---

**错误处理写法：分配失败时清理**
`if (<ptr> == NULL) { free(<other_ptr>); return; }`
```c
// 分配失败时清理已分配的内存
int *a = (int *)malloc(10 * sizeof(int));
int *b = (int *)malloc(20 * sizeof(int));
if (b == NULL) {
    free(a);
    return;
}
```



<!-- ============ 文档分隔线：025-c/004-FunctionDetailed.md ============ -->

# 函数详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数声明与定义

**基本写法：函数声明（原型）**
`<return_type> <func_name>(<parameter_list>);`
```c
// 声明函数原型
int add(int a, int b);
```

---

**无参写法：无参数函数声明**
`<return_type> <func_name>(void);`
```c
// 声明无参数函数
void print_message(void);
```

---

**基本写法：函数定义**
`<return_type> <func_name>(<parameter_list>) { ... return <expr>; }`
```c
// 定义加法函数
int add(int a, int b) {
    return a + b;
}
```

---

**无返回写法：void 函数定义**
`void <func_name>(<params>) { ... }`
```c
// 无返回值的函数
void print_message(void) {
    printf("Hello, Function!\n");
}
```

---

## 参数传递

**传值写法：传值调用**
`<return_type> <func>(<type> <param>) { ... }`
```c
// 修改形参不影响实参
void increment(int x) {
    x++;
}
```

---

**传址写法：传址调用**
`<return_type> <func>(<type> *<param>) { ... }`
```c
// 通过指针修改实参
void increment_by_address(int *x) {
    (*x)++;
}
```

---

**数组参数写法：数组作为参数**
`<return_type> <func>(<type> <arr>[], int <size>) { ... }`
```c
// 传递数组首地址和大小
void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}
```

---

## 返回值

**基本写法：返回基本类型**
`return <expression>;`
```c
// 返回最大值
int max(int a, int b) {
    return (a > b) ? a : b;
}
```

---

**指针返回写法：返回指针**
`<type> *<func>(<params>) { ... return <ptr>; }`
```c
// 返回动态分配的内存
int *create_dynamic_array(int size) {
    return (int *)malloc(size * sizeof(int));
}
```

---

**提前返回写法：void 函数提前返回**
`return;`
```c
// 满足条件时提前返回
void check_number(int n) {
    if (n < 0) {
        printf("Negative!\n");
        return;
    }
    printf("Non-negative\n");
}
```

---

## 递归

**阶乘写法：递归计算阶乘**
`<return_type> <func>(<type> <param>) { if (<base>) return ...; return <recursive_call>; }`
```c
// 递归计算阶乘
long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

---

**斐波那契写法：递归计算斐波那契**
`<return_type> <func>(<type> <param>) { if (<base>) return ...; return <recursive1> + <recursive2>; }`
```c
// 递归计算斐波那契数列
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

---

**二分查找写法：递归二分查找**
`int <search>(<type> <arr>[], int <low>, int <high>, <type> <target>) { ... }`
```c
// 递归实现二分查找
int binary_search(int arr[], int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] > target) return binary_search(arr, low, mid - 1, target);
    else return binary_search(arr, mid + 1, high, target);
}
```

---

## 存储类与作用域

**静态局部写法：静态局部变量**
`static <type> <var> = <value>;`
```c
// 仅首次调用时初始化
void counter() {
    static int count = 0;
    count++;
    printf("Count: %d\n", count);
}
```

---

**外部变量写法：extern 外部变量**
`extern <type> <var>;`
```c
// 声明外部变量
extern int global_var;
```

---

## 函数指针

**基本写法：函数指针定义**
`<return_type> (*<ptr_name>)(<parameter_list>);`
```c
// 定义函数指针
int (*add_ptr)(int, int);
```

---

**赋值写法：函数指针赋值**
`<func_ptr> = <func_name>;`
```c
// 将函数地址赋给指针
add_ptr = add;
```

---

**调用写法：通过函数指针调用**
`<result> = <func_ptr>(<args>);`
```c
// 通过函数指针调用函数
int result = add_ptr(10, 20);
```

---

**typedef 写法：定义回调函数类型**
`typedef <return_type> (*<CallbackName>)(<params>);`
```c
// 定义回调函数类型
typedef void (*Callback)(int);
```

---

**回调写法：使用回调函数**
`void <func>(<type> <arr>[], int <size>, <CallbackType> <callback>) { ... }`
```c
// 执行回调的函数
void process_array(int arr[], int size, Callback callback) {
    for (int i = 0; i < size; i++) {
        callback(arr[i]);
    }
}
```

---

**数组写法：函数指针数组**
`<return_type> (*<array_name>[])(<params>) = { <func1>, <func2>, ... };`
```c
// 函数指针数组
int (*operations[])(int, int) = {add, subtract, multiply};
```

---

## 可变参数函数

**基本写法：可变参数函数定义**
`<return_type> <func>(<fixed_params>, ...) { ... }`
```c
#include <stdarg.h>
// 计算多个整数的和
int sum(int count, ...) {
    va_list valist;
    va_start(valist, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(valist, int);
    }
    va_end(valist);
    return total;
}
```

---

## 内联函数

**基本写法：内联函数定义**
`inline <type> <func>(<params>) { ... }`
```c
// 内联函数可能被编译器内联展开
inline int max(int a, int b) {
    return a > b ? a : b;
}
```



<!-- ============ 文档分隔线：025-c/005-StructAndUnion.md ============ -->

# 结构体与联合体

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 结构体定义

**基本写法：结构体定义**
`struct <Name> { <type> <member>; ... };`
```c
// 定义 Point 结构体
struct Point {
    int x;
    int y;
};
```

---

**typedef 写法：结构体别名**
`typedef struct { <members> } <Name>;`
```c
// 定义 Employee 结构体类型
typedef struct {
    int id;
    char name[50];
    float salary;
} Employee;
```

---

**typedef 写法：为已定义结构体创建别名**
`typedef struct <Name> <Alias>;`
```c
// 为结构体创建别名
struct Point { int x; int y; };
typedef struct Point Point;
```

---

## 结构体变量

**基本写法：声明结构体变量**
`struct <Name> <var_name>;`
```c
// 声明结构体变量
struct Point p1;
```

---

**typedef 写法：使用别名声明**
`<TypeName> <var_name>;`
```c
// 使用类型别名声明
Employee emp;
```

---

**初始化写法：声明并初始化**
`struct <Name> <var> = {<values>};`
```c
// 初始化结构体变量
struct Point p = {10, 20};
```

---

**指定初始化写法：按成员名初始化**
`struct <Name> <var> = {.<member> = <value>, ...};`
```c
// 按成员名初始化
struct Point p = {.x = 10, .y = 20};
```

---

**赋值写法：结构体变量赋值**
`<var1> = <var2>;`
```c
// 结构体变量直接赋值
struct Point p1 = {10, 20};
struct Point p2;
p2 = p1;
```

---

## 结构体成员访问

**基本写法：访问成员**
`<var>.<member>`
```c
// 使用点运算符访问成员
struct Point p = {10, 20};
printf("x: %d\n", p.x);
```

---

**修改写法：修改成员值**
`<var>.<member> = <value>;`
```c
// 修改结构体成员的值
struct Point p = {10, 20};
p.x = 30;
```

---

**指针写法：通过指针访问成员**
`<ptr>-><member>`
```c
// 使用箭头运算符访问成员
struct Point p = {10, 20};
struct Point *ptr = &p;
printf("x: %d\n", ptr->x);
```

---

## 嵌套结构体

**基本写法：结构体嵌套**
`struct <Outer> { struct <Inner> <member>; ... };`
```c
// 嵌套结构体定义
struct Date { int year; int month; int day; };
struct Person {
    char name[50];
    struct Date birthday;
};
```

---

**访问写法：访问嵌套成员**
`<var>.<inner>.<member>`
```c
// 访问嵌套结构体成员
struct Person person;
person.birthday.year = 1990;
```

---

## 结构体数组

**基本写法：结构体数组声明**
`struct <Name> <array_name>[<size>];`
```c
// 声明结构体数组
struct Point points[10];
```

---

**初始化写法：结构体数组初始化**
`struct <Name> <array_name>[<size>] = { {<values>}, ... };`
```c
// 初始化结构体数组
struct Point pts[3] = {{1, 2}, {3, 4}, {5, 6}};
```

---

**遍历写法：遍历结构体数组**
`for (int i = 0; i < <size>; i++) { ... <array>[i].<member> ... }`
```c
// 遍历结构体数组
struct Point pts[3] = {{1, 2}, {3, 4}, {5, 6}};
for (int i = 0; i < 3; i++) {
    printf("(%d, %d)\n", pts[i].x, pts[i].y);
}
```

---

## 结构体与函数

**传值写法：结构体作为函数参数**
`<return_type> <func>(struct <Name> <param>) { ... }`
```c
// 传递结构体副本
void print_point(struct Point p) {
    printf("(%d, %d)\n", p.x, p.y);
}
```

---

**传址写法：结构体指针作为函数参数**
`<return_type> <func>(struct <Name> *<param>) { ... }`
```c
// 传递结构体指针
void move_point(struct Point *p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
}
```

---

**返回写法：函数返回结构体**
`struct <Name> <func>(<params>) { ... return <struct_var>; }`
```c
// 返回结构体
struct Point create_point(int x, int y) {
    struct Point p = {x, y};
    return p;
}
```

---

## 位域

**基本写法：位域定义**
`struct <Name> { <type> <member> : <bits>; ... };`
```c
// 定义位域结构体
struct Flags {
    unsigned int a : 1;
    unsigned int b : 3;
    unsigned int c : 4;
};
```

---

**访问写法：访问位域成员**
`<var>.<member>`
```c
// 访问位域成员
struct Flags f;
f.a = 1;
f.b = 5;
```

---

## 联合体

**基本写法：联合体定义**
`union <Name> { <type> <member>; ... };`
```c
// 定义联合体
union Data {
    int i;
    float f;
    char str[20];
};
```

---

**基本写法：联合体变量声明与初始化**
`union <Name> <var>;`
```c
// 声明联合体变量
union Data data;
```

---

**访问写法：访问联合体成员**
`<var>.<member>`
```c
// 访问联合体成员
union Data data;
data.i = 10;
printf("%d\n", data.i);
```

---

**指针写法：通过指针访问联合体成员**
`<ptr>-><member>`
```c
// 通过指针访问联合体成员
union Data data;
union Data *ptr = &data;
ptr->f = 3.14f;
```

---

## 结构体与联合体混合

**基本写法：结构体包含联合体**
`struct <Name> { <type> <tag>; union <UnionName> <member>; };`
```c
// 结构体包含联合体
struct Value {
    int type;
    union {
        int i;
        float f;
    } data;
};
```

---

**访问写法：访问结构体中的联合体成员**
`<var>.<union_member>.<member>`
```c
// 访问结构体中的联合体成员
struct Value v;
v.type = 0;
v.data.i = 100;
```

---

## 结构体内存对齐

**基本写法：查看结构体大小**
`sizeof(struct <Name>)`
```c
// 查看结构体大小
struct Point { int x; int y; };
printf("Size: %zu\n", sizeof(struct Point));
```

---

**对齐控制写法：指定对齐方式**
`#pragma pack(<n>)`
```c
// 设置 1 字节对齐
#pragma pack(1)
struct Packed {
    char c;
    int i;
};
#pragma pack()
```

---

**对齐属性写法：使用 __attribute__**
`struct __attribute__((aligned(<n>))) <Name> { ... };`
```c
// 指定结构体对齐为 16 字节
struct __attribute__((aligned(16))) AlignedStruct {
    int x;
};
```



<!-- ============ 文档分隔线：025-c/006-VarargsFunction.md ============ -->

# 可变参数函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 可变参数函数定义

**基本写法：可变参数函数声明**
`<return_type> <func_name>(<fixed_params>, ...);`
```c
// 声明可变参数函数
int sum(int count, ...);
```

---

**基本写法：可变参数函数定义**
`<return_type> <func_name>(<fixed_params>, ...) { ... }`
```c
#include <stdarg.h>
// 定义可变参数函数
int sum(int count, ...) {
    va_list valist;
    va_start(valist, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(valist, int);
    }
    va_end(valist);
    return total;
}
```

---

## va_list 相关宏

**基本写法：声明 va_list 变量**
`va_list <valist>;`
```c
#include <stdarg.h>
// 声明参数列表变量
va_list valist;
```

---

**基本写法：初始化 va_list**
`va_start(<valist>, <last_named_param>);`
```c
#include <stdarg.h>
// 初始化参数列表，count 为最后一个命名参数
va_start(valist, count);
```

---

**基本写法：获取下一个参数**
`<type> <val> = va_arg(<valist>, <type>);`
```c
#include <stdarg.h>
// 获取下一个 int 类型的参数
int num = va_arg(valist, int);
```

---

**基本写法：清理 va_list**
`va_end(<valist>);`
```c
#include <stdarg.h>
// 清理参数列表
va_end(valist);
```

---

**拷贝写法：复制 va_list**
`va_copy(<dest>, <src>);`
```c
#include <stdarg.h>
// 复制参数列表
va_list dest;
va_copy(dest, src);
```

---

## 可变参数函数示例

**求和写法：计算多个整数的和**
`int <func>(int <count>, ...) { ... }`
```c
#include <stdarg.h>
// 计算多个整数的和
int sum(int count, ...) {
    va_list valist;
    va_start(valist, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(valist, int);
    }
    va_end(valist);
    return total;
}
```

---

**最大值写法：找出多个整数的最大值**
`int <func>(int <count>, ...) { ... }`
```c
#include <stdarg.h>
// 找出多个整数的最大值
int max(int count, ...) {
    va_list valist;
    va_start(valist, count);
    int max_val = va_arg(valist, int);
    for (int i = 1; i < count; i++) {
        int num = va_arg(valist, int);
        if (num > max_val) {
            max_val = num;
        }
    }
    va_end(valist);
    return max_val;
}
```

---

**打印写法：自定义打印函数**
`void <func>(const char *<format>, ...) { ... }`
```c
#include <stdarg.h>
#include <stdio.h>
// 自定义打印函数
void log_message(const char *format, ...) {
    va_list valist;
    va_start(valist, format);
    vprintf(format, valist);
    va_end(valist);
}
```

---

## vprintf 系列函数

**vprintf 写法：使用 vprintf 输出**
`vprintf(<format>, <valist>);`
```c
#include <stdarg.h>
#include <stdio.h>
// 使用 vprintf 输出可变参数
void log_message(const char *format, ...) {
    va_list valist;
    va_start(valist, format);
    vprintf(format, valist);
    va_end(valist);
}
```

---

**vfprintf 写法：使用 vfprintf 输出到文件**
`vfprintf(<fp>, <format>, <valist>);`
```c
#include <stdarg.h>
#include <stdio.h>
// 使用 vfprintf 输出到文件
void log_to_file(FILE *fp, const char *format, ...) {
    va_list valist;
    va_start(valist, format);
    vfprintf(fp, format, valist);
    va_end(valist);
}
```

---

**vsprintf 写法：使用 vsprintf 写入字符串**
`vsprintf(<buffer>, <format>, <valist>);`
```c
#include <stdarg.h>
#include <stdio.h>
// 使用 vsprintf 写入字符串
void format_string(char *buffer, const char *format, ...) {
    va_list valist;
    va_start(valist, format);
    vsprintf(buffer, format, valist);
    va_end(valist);
}
```

---

**vsnprintf 写法：使用 vsnprintf 安全写入字符串**
`vsnprintf(<buffer>, <size>, <format>, <valist>);`
```c
#include <stdarg.h>
#include <stdio.h>
// 使用 vsnprintf 安全写入字符串（限制长度）
void format_string_safe(char *buffer, size_t size, const char *format, ...) {
    va_list valist;
    va_start(valist, format);
    vsnprintf(buffer, size, format, valist);
    va_end(valist);
}
```

---

## 可变参数函数调用

**基本写法：调用可变参数函数**
`<func_name>(<fixed_args>, <var1>, <var2>, ...);`
```c
// 调用可变参数函数
int result = sum(5, 10, 20, 30, 40, 50);
```

---

**混合类型写法：调用混合类型可变参数函数**
`<func_name>(<format>, <arg1>, <arg2>, ...);`
```c
// 调用 printf 函数
printf("Name: %s, Age: %d\n", "John", 30);
```

---

## 可变参数宏

**基本写法：可变参数宏定义**
`#define <NAME>(<fixed>, ...) <expr>(__VA_ARGS__)`
```c
// 可变参数宏
#define LOG(fmt, ...) printf(fmt, __VA_ARGS__)
```

---

**使用写法：调用可变参数宏**
`<NAME>(<fixed_args>, <var_args>);`
```c
// 调用可变参数宏
LOG("Value: %d\n", 100);
```

---

## 可变参数函数注意事项

**哨兵值写法：使用哨兵值标记结束**
`<func>(<value1>, <value2>, ..., <sentinel>);`
```c
// 使用哨兵值标记参数结束
int sum_sentinel(int first, ...) {
    va_list valist;
    va_start(valist, first);
    int total = first;
    int num;
    while ((num = va_arg(valist, int)) != -1) {
        total += num;
    }
    va_end(valist);
    return total;
}
```

---

**类型安全写法：使用格式字符串指定类型**
`<func>(const char *<format>, ...)`
```c
// 通过格式字符串指定参数类型
void print_values(const char *format, ...) {
    va_list valist;
    va_start(valist, format);
    const char *p = format;
    while (*p) {
        if (*p == 'd') {
            printf("%d ", va_arg(valist, int));
        } else if (*p == 'f') {
            printf("%f ", va_arg(valist, double));
        }
        p++;
    }
    va_end(valist);
}
```



<!-- ============ 文档分隔线：025-c/007-ControlFlow.md ============ -->

# 控制流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## if-else 条件判断

**基本写法：if 语句**
`if (<condition>) { ... }`
```c
// 单条件判断
int score = 85;
if (score >= 60) {
    printf("Pass\n");
}
```

---

**多分支写法：if-else if-else**
`if (<condition>) { ... } else if (<condition>) { ... } else { ... }`
```c
// 多条件分支判断
int score = 85;
if (score >= 90) {
    printf("Excellent\n");
} else if (score >= 80) {
    printf("Very Good\n");
} else {
    printf("Fail\n");
}
```

---

**嵌套写法：嵌套 if-else**
`if (<condition>) { if (<condition>) { ... } else { ... } } else { ... }`
```c
// 嵌套条件判断
int age = 18;
int has_license = 1;
if (age >= 18) {
    if (has_license) {
        printf("You can drive\n");
    } else {
        printf("Need a license\n");
    }
} else {
    printf("Too young\n");
}
```

---

## switch-case 多分支选择

**基本写法：switch-case**
`switch (<expr>) { case <val>: ... break; [default: ...] }`
```c
// 根据成绩等级输出
char grade = 'B';
switch (grade) {
    case 'A':
        printf("Great!\n");
        break;
    case 'B':
        printf("Good!\n");
        break;
    default:
        printf("Unknown\n");
}
```

---

**穿透写法：多 case 共享代码块**
`case <val1>: case <val2>: ... break;`
```c
// 多个 case 执行相同代码
int month = 2;
int days;
switch (month) {
    case 1: case 3: case 5: case 7:
        days = 31;
        break;
    case 4: case 6: case 9:
        days = 30;
        break;
    default:
        days = 28;
}
```

---

## for 循环

**基本写法：for 循环**
`for (<init>; <condition>; <update>) { ... }`
```c
// 打印 0 到 9
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}
```

---

**嵌套写法：嵌套 for 循环**
`for (...) { for (...) { ... } }`
```c
// 打印乘法表
for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= i; j++) {
        printf("%d*%d=%d\t", j, i, i*j);
    }
    printf("\n");
}
```

---

**多变量写法：多变量 for 循环**
`for (<init1>, <init2>; <cond>; <update1>, <update2>) { ... }`
```c
// 使用多个循环变量
for (int i = 0, j = 10; i < j; i++, j--) {
    printf("i=%d, j=%d\n", i, j);
}
```

---

**无限写法：无限 for 循环**
`for (;;) { ... }`
```c
// 无限循环
for (;;) {
    printf("Loop\n");
}
```

---

## while 循环

**基本写法：while 循环**
`while (<condition>) { ... }`
```c
// 当条件为真时循环
int i = 0;
while (i < 10) {
    printf("%d ", i);
    i++;
}
```

---

**无限写法：无限 while 循环**
`while (1) { ... if (<condition>) break; }`
```c
// 无限循环带退出条件
int count = 0;
while (1) {
    count++;
    if (count >= 5) {
        break;
    }
}
```

---

## do-while 循环

**基本写法：do-while 循环**
`do { ... } while (<condition>);`
```c
// 至少执行一次的循环
int i = 10;
do {
    printf("Execute once\n");
    i--;
} while (i < 5);
```

---

## 循环控制语句

**break 写法：跳出循环**
`break;`
```c
// 当 i 等于 5 时退出循环
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;
    }
    printf("%d ", i);
}
```

---

**continue 写法：跳过本次循环**
`continue;`
```c
// 跳过偶数
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        continue;
    }
    printf("%d ", i);
}
```

---

**goto 写法：无条件跳转**
`goto <label>; ... <label>:`
```c
// 跳转到标签处
int i = 0;
start:
printf("i = %d\n", i);
i++;
if (i < 5) {
    goto start;
}
```

---

**goto 写法：跳出多层循环**
`goto <label>;`
```c
// 跳出多层嵌套循环
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == 1 && j == 1) {
            goto end_of_loops;
        }
    }
}
end_of_loops:
printf("Exited\n");
```

---

## 状态机实现

**switch 写法：使用 switch 实现状态机**
`while (<state> != FINAL) { switch (<state>) { ... } }`
```c
// 状态机循环
enum State { STATE_START, STATE_READING, STATE_FINISHED };
enum State current_state = STATE_START;
while (current_state != STATE_FINISHED) {
    switch (current_state) {
        case STATE_START:
            current_state = STATE_READING;
            break;
        case STATE_READING:
            current_state = STATE_FINISHED;
            break;
    }
}
```



<!-- ============ 文档分隔线：025-c/008-EnumTypedef.md ============ -->

# 枚举与typedef

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 枚举定义

**基本写法：枚举定义**
`enum <Name> { <MEM1>, <MEM2>, ... };`
```c
// 定义星期枚举
enum Weekday { MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY };
```

---

**自定义写法：指定枚举值**
`enum <Name> { <MEM1> = <val>, <MEM2>, ... };`
```c
// 从 1 开始递增
enum Months { JAN = 1, FEB, MAR, APR };
```

---

**分散写法：枚举值显式指定**
`enum <Name> { <MEM1> = <val>, <MEM2> = <val>, ... };`
```c
// 显式指定每个枚举值
enum Color { RED = 1, GREEN = 2, BLUE = 4 };
```

---

**typedef 写法：枚举别名**
`typedef enum { <members> } <Name>;`
```c
// 定义枚举类型别名
typedef enum { STATUS_OK, STATUS_ERROR, STATUS_PENDING } Status;
```

---

## 枚举变量

**基本写法：声明枚举变量**
`enum <Name> <var_name>;`
```c
// 声明枚举变量
enum Weekday today;
```

---

**初始化写法：声明并初始化**
`enum <Name> <var> = <MEMBER>;`
```c
// 初始化枚举变量
enum Weekday today = MONDAY;
```

---

**typedef 写法：使用别名声明**
`<TypeName> <var_name>;`
```c
// 使用类型别名声明
Status current_status = STATUS_OK;
```

---

## 枚举在 switch 中使用

**基本写法：switch 处理枚举**
`switch (<enum_var>) { case <MEM1>: ... break; ... }`
```c
// 使用 switch 处理枚举值
enum Weekday today = MONDAY;
switch (today) {
    case MONDAY:
        printf("Start of week\n");
        break;
    case FRIDAY:
        printf("End of week\n");
        break;
    default:
        printf("Middle of week\n");
}
```

---

## typedef 基本用法

**基本写法：为基本类型创建别名**
`typedef <existing_type> <new_name>;`
```c
// 为 unsigned int 创建别名
typedef unsigned int uint;
```

---

**基本写法：为指针类型创建别名**
`typedef <type> *<PtrName>;`
```c
// 为整型指针创建别名
typedef int *IntPtr;
```

---

**基本写法：为数组类型创建别名**
`typedef <type> (<ArrayName>)[<size>];`
```c
// 为整型数组创建别名
typedef int IntArray[10];
```

---

## typedef 与结构体

**基本写法：结构体别名**
`typedef struct { <members> } <Name>;`
```c
// 定义 Point 结构体类型
typedef struct {
    int x;
    int y;
} Point;
```

---

**基本写法：为已定义结构体创建别名**
`typedef struct <Name> <Alias>;`
```c
// 为结构体创建别名
struct Point { int x; int y; };
typedef struct Point Point;
```

---

## typedef 与枚举

**基本写法：枚举别名**
`typedef enum { <members> } <Name>;`
```c
// 定义枚举类型别名
typedef enum { RED, GREEN, BLUE } Color;
```

---

## typedef 与函数指针

**基本写法：函数指针类型别名**
`typedef <return_type> (*<FuncTypeName>)(<params>);`
```c
// 定义函数指针类型
typedef int (*Operation)(int, int);
```

---

**使用写法：使用函数指针类型**
`<FuncTypeName> <var> = <func_name>;`
```c
// 使用函数指针类型声明变量
Operation op = add;
```

---

## typedef 与联合体

**基本写法：联合体别名**
`typedef union { <members> } <Name>;`
```c
// 定义联合体类型别名
typedef union {
    int i;
    float f;
} Data;
```

---

## typedef 复杂类型

**基本写法：多维数组别名**
`typedef <type> (<ArrayName>)[<rows>][<cols>];`
```c
// 为二维数组创建别名
typedef int Matrix[3][3];
```

---

**基本写法：指向数组的指针别名**
`typedef <type> (*<PtrName>)[<size>];`
```c
// 为指向数组的指针创建别名
typedef int (*ArrayPtr)[5];
```

---

## 枚举与整数

**转换写法：枚举转整数**
`int <var> = <ENUM_MEMBER>;`
```c
// 枚举值隐式转换为整数
enum Color c = RED;
int value = c;
```

---

**转换写法：整数转枚举**
`enum <Name> <var> = (<enum_name>)<int_value>;`
```c
// 整数显式转换为枚举
enum Color c = (enum Color)1;
```

---

## 枚举大小

**基本写法：获取枚举大小**
`sizeof(enum <Name>)`
```c
// 查看枚举类型大小
enum Color { RED, GREEN, BLUE };
printf("Size: %zu\n", sizeof(enum Color));
```



<!-- ============ 文档分隔线：025-c/009-DataTypeDetailed.md ============ -->

# 数据类型详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 整型

**基本写法：char 类型声明**
`char <var_name> = <value>;`
```c
// 1 字节字符型
char c = 'A';
```

---

**基本写法：short 类型声明**
`short <var_name> = <value>;`
```c
// 2 字节短整型
short s = 1000;
```

---

**基本写法：int 类型声明**
`int <var_name> = <value>;`
```c
// 4 字节整型
int i = 100000;
```

---

**基本写法：long 类型声明**
`long <var_name> = <value>L;`
```c
// 长整型
long l = 100000L;
```

---

**基本写法：unsigned 整型声明**
`unsigned <type> <var_name> = <value>;`
```c
// 无符号整型
unsigned int u = 100U;
```

---

## 浮点型

**基本写法：float 类型声明**
`float <var_name> = <value>f;`
```c
// 4 字节单精度浮点
float f = 3.14f;
```

---

**基本写法：double 类型声明**
`double <var_name> = <value>;`
```c
// 8 字节双精度浮点
double d = 3.14159;
```

---

**基本写法：long double 类型声明**
`long double <var_name> = <value>L;`
```c
// 长双精度浮点
long double ld = 3.14L;
```

---

## 布尔型

**基本写法：布尔型声明（C99+）**
`bool <var_name> = <true|false>;`
```c
#include <stdbool.h>
// 布尔类型变量
bool is_valid = true;
```

---

## 类型修饰符

**基本写法：signed 修饰符**
`signed <type> <var_name>;`
```c
// 有符号整型（默认）
signed int x = -10;
```

---

**基本写法：unsigned 修饰符**
`unsigned <type> <var_name>;`
```c
// 无符号整型
unsigned int y = 10;
```

---

**基本写法：const 修饰符**
`const <type> <var_name> = <value>;`
```c
// 只读常量
const int MAX_VALUE = 100;
```

---

**基本写法：volatile 修饰符**
`volatile <type> <var_name>;`
```c
// 防止编译器优化
volatile int sensor_value;
```

---

## sizeof 运算符

**基本写法：获取类型大小**
`sizeof(<type>)`
```c
// 获取 int 类型字节数
printf("int: %zu\n", sizeof(int));
```

---

**基本写法：获取变量大小**
`sizeof(<var>)`
```c
// 获取数组元素个数
int arr[10];
size_t count = sizeof(arr) / sizeof(arr[0]);
```

---

## 数组

**基本写法：一维数组声明**
`<type> <array_name>[<size>];`
```c
// 声明大小为 5 的整型数组
int numbers[5];
```

---

**初始化写法：一维数组完全初始化**
`<type> <array_name>[<size>] = {<values>};`
```c
// 完全初始化数组
int arr[5] = {1, 2, 3, 4, 5};
```

---

**自动推断写法：一维数组**
`<type> <array_name>[] = {<values>};`
```c
// 自动推断数组大小为 3
int arr[] = {10, 20, 30};
```

---

**基本写法：二维数组声明**
`<type> <array_name>[<rows>][<cols>];`
```c
// 声明 3x3 矩阵
int matrix[3][3];
```

---

## 指针

**基本写法：指针声明与初始化**
`<type> *<ptr_name> = &<var>;`
```c
// ptr 指向 x 的地址
int x = 10;
int *ptr = &x;
```

---

**解引用写法：通过指针访问值**
`*<ptr>`
```c
// 解引用获取指针指向的值
int x = 10;
int *ptr = &x;
printf("值: %d\n", *ptr);
```

---

## 结构体

**基本写法：结构体定义**
`typedef struct { <members> } <Name>;`
```c
// 定义 Employee 结构体类型
typedef struct {
    int id;
    char name[50];
    float salary;
} Employee;
```

---

**初始化写法：结构体变量初始化**
`<Name> <var> = {<values>};`
```c
// 初始化结构体变量
Employee emp = {101, "John Doe", 5000.0};
```

---

## 联合体

**基本写法：联合体定义**
`union <Name> { <members> };`
```c
// 定义联合体
union Data {
    int i;
    float f;
    char str[20];
};
```

---

## 枚举

**基本写法：枚举定义**
`enum <Name> { <MEM1>, <MEM2>, ... };`
```c
// 定义星期枚举
enum Weekday { MONDAY, TUESDAY, WEDNESDAY };
```

---

**自定义写法：指定枚举值**
`enum <Name> { <MEM1> = <val>, <MEM2> = <val>, ... };`
```c
// 显式指定枚举值
enum Color { RED = 1, GREEN = 2, BLUE = 4 };
```

---

## 空类型

**基本写法：void 函数返回类型**
`void <func_name>(<params>) { ... }`
```c
// 无返回值的函数
void print_hello() {
    printf("Hello!\n");
}
```

---

**基本写法：void 函数参数**
`<type> <func_name>(void) { ... }`
```c
// 明确表示无参数
int main(void) {
    return 0;
}
```

---

**基本写法：void 通用指针**
`void *<ptr_name>;`
```c
// 可以指向任何类型的通用指针
void *generic_ptr;
```

---

## 类型转换

**隐式写法：自动类型转换**
`<type> <var> = <other_type_var>;`
```c
// int 隐式转换为 double
int x = 10;
double y = x;
```

---

**显式写法：强制类型转换**
`(<target_type>)<expression>`
```c
// double 显式转换为 int
double pi = 3.14159;
int rounded_pi = (int)pi;
```

---

**指针转换写法：指针类型转换**
`(<target_type> *)<ptr>`
```c
// void 指针转换为 int 指针
void *ptr = &x;
int *int_ptr = (int *)ptr;
```

---

## typedef 类型别名

**基本写法：为基本类型创建别名**
`typedef <existing_type> <new_name>;`
```c
// 为 unsigned int 创建别名
typedef unsigned int uint;
```

---

**基本写法：为结构体创建别名**
`typedef struct { <members> } <Name>;`
```c
// 定义 Point 结构体别名
typedef struct {
    int x;
    int y;
} Point;
```

---

## 标准固定宽度整数

**基本写法：stdint.h 固定宽度类型**
`#include <stdint.h>`
```c
// 包含固定宽度整数类型定义
#include <stdint.h>
```

---

**基本写法：8 位整数声明**
`int8_t <var>;` 或 `uint8_t <var>;`
```c
// 有符号和无符号 8 位整数
int8_t s8 = -1;
uint8_t u8 = 255;
```

---

**基本写法：32 位整数声明**
`int32_t <var>;` 或 `uint32_t <var>;`
```c
// 有符号和无符号 32 位整数
int32_t s32 = -1000;
uint32_t u32 = 1000;
```



<!-- ============ 文档分隔线：025-c/010-ArrayDetailed.md ============ -->

# 数组详解

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 一维数组

**基本写法：数组声明**
`<type> <array_name>[<size>];`
```c
// 声明大小为 5 的整型数组
int numbers[5];
```

---

**完全初始化写法：数组初始化**
`<type> <array_name>[<size>] = {<values>};`
```c
// 完全初始化数组
int arr[5] = {1, 2, 3, 4, 5};
```

---

**部分初始化写法：部分初始化**
`<type> <array_name>[<size>] = {<values>};`
```c
// 部分初始化，其余元素为 0
int arr[5] = {1, 2, 3};
```

---

**自动推断写法：省略大小**
`<type> <array_name>[] = {<values>};`
```c
// 自动推断数组大小为 3
int arr[] = {10, 20, 30};
```

---

**清零写法：全部初始化为 0**
`<type> <array_name>[<size>] = {0};`
```c
// 所有元素初始化为 0
int arr[10] = {0};
```

---

**访问写法：访问数组元素**
`<array_name>[<index>]`
```c
// 访问数组第一个元素
int arr[5] = {10, 20, 30, 40, 50};
printf("%d\n", arr[0]);
```

---

**遍历写法：遍历数组**
`for (int i = 0; i < <size>; i++) { ... }`
```c
// 遍历打印数组元素
int arr[5] = {1, 2, 3, 4, 5};
for (int i = 0; i < 5; i++) {
    printf("arr[%d] = %d\n", i, arr[i]);
}
```

---

**计算大小写法：计算数组元素个数**
`sizeof(<array>) / sizeof(<array>[0])`
```c
// 计算数组元素个数
int arr[] = {1, 2, 3, 4, 5};
int size = sizeof(arr) / sizeof(arr[0]);
```

---

## 多维数组

**基本写法：二维数组声明与初始化**
`<type> <array_name>[<rows>][<cols>] = { {<values>}, ... };`
```c
// 完整初始化二维数组
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

---

**访问写法：访问二维数组元素**
`<array_name>[<row>][<col>]`
```c
// 访问第二行第三列元素
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
printf("%d\n", matrix[1][2]);
```

---

**遍历写法：遍历二维数组**
`for (int i = 0; i < <rows>; i++) { for (int j = 0; j < <cols>; j++) { ... } }`
```c
// 遍历二维数组
int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        printf("%d ", matrix[i][j]);
    }
}
```

---

**三维写法：三维数组**
`<type> <array_name>[<depth>][<rows>][<cols>];`
```c
// 声明三维数组
int cube[2][2][2] = {
    {{1, 2}, {3, 4}},
    {{5, 6}, {7, 8}}
};
```

---

**函数参数写法：多维数组作为函数参数**
`<return_type> <func>(<type> <arr>[][<cols>], int <rows>) { ... }`
```c
// 需要指定除第一维外的所有维度大小
void print_matrix(int matrix[][3], int rows) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", matrix[i][j]);
        }
    }
}
```

---

## 字符数组与字符串

**字符数组写法：字符数组定义**
`char <array_name>[<size>] = {<chars>};`
```c
// 普通字符数组
char chars[5] = {'H', 'e', 'l', 'l', 'o'};
```

---

**字符串写法：字符串初始化**
`char <str>[] = "<string>";`
```c
// 自动包含 '\0'，大小为 6
char str[] = "Hello";
```

---

**strlen 写法：计算字符串长度**
`strlen(<str>)`
```c
#include <string.h>
// 计算字符串长度
char src[] = "Hello";
int len = strlen(src);
```

---

**strcpy 写法：复制字符串**
`strcpy(<dest>, <src>)`
```c
#include <string.h>
// 复制字符串
char dest[50];
char src[] = "Hello";
strcpy(dest, src);
```

---

**strcat 写法：连接字符串**
`strcat(<dest>, <src>)`
```c
#include <string.h>
// 连接字符串
char dest[50] = "Hello";
strcat(dest, " World");
```

---

**strcmp 写法：比较字符串**
`strcmp(<str1>, <str2>)`
```c
#include <string.h>
// 比较字符串，0 相等，<0 小于，>0 大于
int result = strcmp("abc", "abd");
```

---

**fgets 写法：读取一行字符串**
`fgets(<str>, <size>, stdin)`
```c
// 读取一行（包括空格）
char str[100];
fgets(str, sizeof(str), stdin);
```

---

## 数组与指针

**基本写法：数组名与指针的关系**
`<array_name>` 等同于 `&<array_name>[0]`
```c
// 数组名即首元素地址
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
```

---

**指针算术写法：指针访问数组**
`*(<ptr> + <n>)`
```c
// 使用指针算术访问数组元素
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
printf("%d\n", *(p + 1));
```

---

**指针数组写法：存储指针的数组**
`<type> *<array_name>[<size>];`
```c
// 指针数组
int *ptr_array[3];
int a = 10, b = 20, c = 30;
ptr_array[0] = &a;
```

---

**数组指针写法：指向数组的指针**
`<type> (*<ptr_name>)[<size>];`
```c
// 指向整个数组的指针
int arr[5] = {1, 2, 3, 4, 5};
int (*p)[5] = &arr;
```

---

## 变长数组（VLA，C99+）

**基本写法：运行时确定数组大小**
`<type> <array_name>[<variable>];`
```c
// 数组大小由参数决定
void func(int n) {
    int arr[n];
}
```

---

## 动态数组

**malloc 写法：创建动态数组**
`<type> *<ptr> = (<type> *)malloc(<size> * sizeof(<type>));`
```c
#include <stdlib.h>
// 动态分配数组
int size = 10;
int *arr = (int *)malloc(size * sizeof(int));
```

---

**realloc 写法：动态调整数组大小**
`<type> *<new_ptr> = (<type> *)realloc(<ptr>, <new_size> * sizeof(<type>));`
```c
#include <stdlib.h>
// 重新调整数组大小
int *new_arr = (int *)realloc(arr, 20 * sizeof(int));
```

---

## 数组排序

**冒泡排序写法：冒泡排序实现**
`void <sort>(<type> <arr>[], int <size>) { ... }`
```c
// 冒泡排序算法
void bubble_sort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
```

---

**二分查找写法：二分查找实现**
`int <search>(<type> <arr>[], int <low>, int <high>, <type> <target>) { ... }`
```c
// 二分查找算法
int binary_search(int arr[], int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] > target) return binary_search(arr, low, mid - 1, target);
    else return binary_search(arr, mid + 1, high, target);
}
```



<!-- ============ 文档分隔线：025-c/011-BitField.md ============ -->

# 位域

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 位域定义

**基本写法：位域定义**
`struct <Name> { <type> <member> : <bits>; ... };`
```c
// 定义位域结构体
struct Flags {
    unsigned int a : 1;
    unsigned int b : 3;
    unsigned int c : 4;
};
```

---

**单字段写法：单字段位域**
`struct <Name> { <type> <member> : <bits>; };`
```c
// 单字段位域
struct SingleFlag {
    unsigned int flag : 1;
};
```

---

**多字段写法：多字段位域**
`struct <Name> { <type> <m1> : <bits>; <type> <m2> : <bits>; ... };`
```c
// 多字段位域
struct Status {
    unsigned int ready : 1;
    unsigned int error : 1;
    unsigned int busy : 1;
    unsigned int reserved : 5;
};
```

---

## 位域变量

**基本写法：声明位域变量**
`struct <Name> <var_name>;`
```c
// 声明位域变量
struct Flags flags;
```

---

**初始化写法：位域变量初始化**
`struct <Name> <var> = {<values>};`
```c
// 初始化位域变量
struct Flags flags = {1, 5, 10};
```

---

## 位域成员访问

**基本写法：访问位域成员**
`<var>.<member>`
```c
// 访问位域成员
struct Flags flags;
flags.a = 1;
```

---

**修改写法：修改位域成员值**
`<var>.<member> = <value>;`
```c
// 修改位域成员的值
struct Flags flags;
flags.b = 5;
```

---

**指针写法：通过指针访问位域成员**
`<ptr>-><member>`
```c
// 通过指针访问位域成员
struct Flags flags;
struct Flags *ptr = &flags;
ptr->a = 1;
```

---

## 位域与普通成员混合

**基本写法：位域与普通成员混合**
`struct <Name> { <type> <normal_member>; <type> <bit_member> : <bits>; ... };`
```c
// 位域与普通成员混合
struct Mixed {
    int id;
    unsigned int active : 1;
    unsigned int level : 3;
};
```

---

## 无名位域

**基本写法：无名位域用于填充**
`<type> : <bits>;`
```c
// 无名位域用于填充
struct Padded {
    unsigned int a : 4;
    unsigned int : 4;  // 填充 4 位
    unsigned int b : 8;
};
```

---

**对齐写法：无名位域用于对齐**
`<type> : 0;`
```c
// 无名位域宽度为 0，强制下一个成员从新存储单元开始
struct Aligned {
    unsigned int a : 4;
    unsigned int : 0;
    unsigned int b : 4;
};
```

---

## 位域大小

**基本写法：查看位域结构体大小**
`sizeof(struct <Name>)`
```c
// 查看位域结构体大小
struct Flags { unsigned int a : 1; unsigned int b : 3; };
printf("Size: %zu\n", sizeof(struct Flags));
```

---

## 位域应用

**硬件寄存器写法：使用位域映射硬件寄存器**
`struct <Name> { volatile <type> <member> : <bits>; ... };`
```c
// 使用位域映射硬件寄存器
struct UART_Reg {
    volatile unsigned int data : 8;
    volatile unsigned int parity : 1;
    volatile unsigned int stop : 1;
    volatile unsigned int enable : 1;
};
```

---

**标志位写法：使用位域管理标志**
`struct <Name> { <type> <flag1> : 1; <type> <flag2> : 1; ... };`
```c
// 使用位域管理多个标志
struct ProcessFlags {
    unsigned int running : 1;
    unsigned int paused : 1;
    unsigned int error : 1;
    unsigned int completed : 1;
};
```

---

## 位域与位运算对比

**位域写法：使用位域访问位**
`<var>.<member> = <value>;`
```c
// 使用位域访问位
struct Flags flags;
flags.a = 1;
```

---

**位运算写法：使用位运算访问位**
`<var> |= (1 << <bit>);`
```c
// 使用位运算设置位
unsigned int flags = 0;
flags |= (1 << 0);
```

---

**位运算写法：检查某一位**
`<var> & (1 << <bit>)`
```c
// 使用位运算检查位
unsigned int flags = 5;
if (flags & (1 << 0)) {
    printf("Bit 0 is set\n");
}
```

---

**位运算写法：清除某一位**
`<var> &= ~(1 << <bit>);`
```c
// 使用位运算清除位
unsigned int flags = 5;
flags &= ~(1 << 0);
```

---

## 位域限制

**跨平台写法：位域顺序与平台相关**
`struct <Name> { <type> <m1> : <bits>; <type> <m2> : <bits>; };`
```c
// 位域的内存布局与平台相关
struct CrossPlatform {
    unsigned int a : 1;
    unsigned int b : 7;
};
```



<!-- ============ 文档分隔线：025-c/012-FileIOOperation.md ============ -->

# 文件IO操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件打开与关闭

**基本写法：打开文件**
`FILE *<fp> = fopen("<filename>", "<mode>");`
```c
#include <stdio.h>
// 以只读方式打开文件
FILE *fp = fopen("data.txt", "r");
```

---

**基本写法：关闭文件**
`fclose(<fp>);`
```c
// 关闭文件
fclose(fp);
```

---

**错误检查写法：检查文件是否打开成功**
`if (<fp> == NULL) { ... }`
```c
// 检查文件是否成功打开
FILE *fp = fopen("data.txt", "r");
if (fp == NULL) {
    perror("Failed to open file");
    return 1;
}
```

---

## 文件打开模式

**只读写法：以只读方式打开**
`fopen("<filename>", "r")`
```c
// 只读模式打开文本文件
FILE *fp = fopen("data.txt", "r");
```

---

**只写写法：以只写方式打开**
`fopen("<filename>", "w")`
```c
// 只写模式打开文件（覆盖）
FILE *fp = fopen("output.txt", "w");
```

---

**追加写法：以追加方式打开**
`fopen("<filename>", "a")`
```c
// 追加模式打开文件
FILE *fp = fopen("log.txt", "a");
```

---

**读写写法：以读写方式打开**
`fopen("<filename>", "r+")`
```c
// 读写模式打开文件
FILE *fp = fopen("data.txt", "r+");
```

---

**二进制写法：以二进制方式打开**
`fopen("<filename>", "rb")`
```c
// 二进制只读模式打开
FILE *fp = fopen("data.bin", "rb");
```

---

## 字符读写

**基本写法：读取单个字符**
`int <ch> = fgetc(<fp>);`
```c
// 从文件读取单个字符
int ch = fgetc(fp);
```

---

**基本写法：写入单个字符**
`fputc(<ch>, <fp>);`
```c
// 向文件写入单个字符
fputc('A', fp);
```

---

**EOF 写法：检测文件结束**
`while ((<ch> = fgetc(<fp>)) != EOF) { ... }`
```c
// 循环读取直到文件结束
int ch;
while ((ch = fgetc(fp)) != EOF) {
    putchar(ch);
}
```

---

## 字符串读写

**基本写法：读取字符串**
`char *<result> = fgets(<buffer>, <size>, <fp>);`
```c
// 从文件读取一行字符串
char buffer[100];
fgets(buffer, sizeof(buffer), fp);
```

---

**基本写法：写入字符串**
`fputs("<string>", <fp>);`
```c
// 向文件写入字符串
fputs("Hello World", fp);
```

---

## 格式化读写

**基本写法：格式化读取**
`fscanf(<fp>, "<format>", &<var>);`
```c
// 从文件按格式读取
int age;
fscanf(fp, "%d", &age);
```

---

**基本写法：格式化写入**
`fprintf(<fp>, "<format>", <values>);`
```c
// 向文件按格式写入
fprintf(fp, "Name: %s, Age: %d\n", "John", 30);
```

---

## 块读写

**基本写法：读取数据块**
`size_t <count> = fread(<buffer>, <size>, <count>, <fp>);`
```c
// 从文件读取数据块
int data[10];
fread(data, sizeof(int), 10, fp);
```

---

**基本写法：写入数据块**
`size_t <count> = fwrite(<buffer>, <size>, <count>, <fp>);`
```c
// 向文件写入数据块
int data[5] = {1, 2, 3, 4, 5};
fwrite(data, sizeof(int), 5, fp);
```

---

## 文件定位

**基本写法：获取当前位置**
`long <pos> = ftell(<fp>);`
```c
// 获取当前文件位置
long pos = ftell(fp);
```

---

**基本写法：设置文件位置**
`fseek(<fp>, <offset>, <origin>);`
```c
// 从文件开头偏移 10 字节
fseek(fp, 10, SEEK_SET);
```

---

**基本写法：回到文件开头**
`rewind(<fp>);`
```c
// 将文件指针重置到开头
rewind(fp);
```

---

**末尾写法：定位到文件末尾**
`fseek(<fp>, 0, SEEK_END);`
```c
// 定位到文件末尾
fseek(fp, 0, SEEK_END);
```

---

**fgetpos 写法：获取文件位置**
`fgetpos(<fp>, &<pos>);`
```c
// 获取文件位置
fpos_t pos;
fgetpos(fp, &pos);
```

---

**fsetpos 写法：设置文件位置**
`fsetpos(<fp>, &<pos>);`
```c
// 设置文件位置
fpos_t pos;
fsetpos(fp, &pos);
```

---

## 文件状态检查

**基本写法：检查文件结束**
`feof(<fp>)`
```c
// 检查是否到达文件末尾
if (feof(fp)) {
    printf("End of file\n");
}
```

---

**基本写法：检查文件错误**
`ferror(<fp>)`
```c
// 检查文件读写错误
if (ferror(fp)) {
    printf("File error\n");
}
```

---

**基本写法：清除文件错误标志**
`clearerr(<fp>);`
```c
// 清除文件错误标志
clearerr(fp);
```

---

## 标准流

**基本写法：使用标准输入**
`stdin`
```c
// 从标准输入读取
char buffer[100];
fgets(buffer, sizeof(buffer), stdin);
```

---

**基本写法：使用标准输出**
`stdout`
```c
// 向标准输出写入
fputs("Hello\n", stdout);
```

---

**基本写法：使用标准错误**
`stderr`
```c
// 向标准错误输出
fprintf(stderr, "Error message\n");
```

---

## 文件删除与重命名

**基本写法：删除文件**
`remove("<filename>");`
```c
// 删除文件
remove("temp.txt");
```

---

**基本写法：重命名文件**
`rename("<old_name>", "<new_name>");`
```c
// 重命名文件
rename("old.txt", "new.txt");
```

---

## 临时文件

**基本写法：创建临时文件**
`FILE *<fp> = tmpfile();`
```c
// 创建临时文件（关闭后自动删除）
FILE *tmp = tmpfile();
```

---

**基本写法：生成临时文件名**
`char *<name> = tmpnam(<buffer>);`
```c
// 生成临时文件名
char name[L_tmpnam];
tmpnam(name);
```

---

## 文件缓冲

**基本写法：设置缓冲区**
`setvbuf(<fp>, <buffer>, <mode>, <size>);`
```c
// 设置全缓冲
char buffer[1024];
setvbuf(fp, buffer, _IOFBF, sizeof(buffer));
```

---

**基本写法：刷新缓冲区**
`fflush(<fp>);`
```c
// 刷新文件缓冲区
fflush(fp);
```

---

## 获取文件大小

**基本写法：通过 fseek 和 ftell 获取文件大小**
`fseek(<fp>, 0, SEEK_END); long <size> = ftell(<fp>);`
```c
// 获取文件大小
fseek(fp, 0, SEEK_END);
long file_size = ftell(fp);
rewind(fp);
```

---

## 二进制文件读写

**结构体写法：写入结构体到二进制文件**
`fwrite(&<struct_var>, sizeof(<StructType>), 1, <fp>);`
```c
// 将结构体写入二进制文件
typedef struct { int id; char name[50]; } Record;
Record r = {1, "John"};
fwrite(&r, sizeof(Record), 1, fp);
```

---

**结构体读取写法：从二进制文件读取结构体**
`fread(&<struct_var>, sizeof(<StructType>), 1, <fp>);`
```c
// 从二进制文件读取结构体
Record r;
fread(&r, sizeof(Record), 1, fp);
```



<!-- ============ 文档分隔线：025-c/013-PreprocessorMacro.md ============ -->

# 预处理器与宏

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件包含

**系统头文件写法：包含系统头文件**
`#include <<header>>`
```c
// 包含标准输入输出头文件
#include <stdio.h>
```

---

**用户头文件写法：包含自定义头文件**
`#include "<header>"`
```c
// 包含当前目录下的头文件
#include "myheader.h"
```

---

## 宏定义

**基本写法：无参宏定义常量**
`#define <NAME> <value>`
```c
// 定义缓冲区大小常量
#define MAX_BUFFER 1024
```

---

**字符串写法：宏定义字符串**
`#define <NAME> "<string>"`
```c
// 定义版本号字符串
#define VERSION "1.0.0"
```

---

**带参写法：带参宏定义**
`#define <NAME>(<params>) <expression>`
```c
// 定义求最大值的宏
#define MAX(a, b) ((a) > (b) ? (a) : (b))
```

---

**多行写法：多行宏定义**
`#define <NAME>(<params>) do { ... } while(0)`
```c
// 多行宏定义
#define LOG_ERROR(msg) do { \
    fprintf(stderr, "Error: %s\n", msg); \
    exit(1); \
} while(0)
```

---

**字符串化写法：# 运算符**
`#define <NAME>(x) #x`
```c
// 将参数转换为字符串
#define STRINGIFY(x) #x
```

---

**标记拼接写法：## 运算符**
`#define <NAME>(a, b) a##b`
```c
// 拼接两个标记
#define CONCAT(a, b) a##b
```

---

**可变参数写法：可变参数宏**
`#define <NAME>(<fixed>, ...) <expr>(__VA_ARGS__)`
```c
// 可变参数宏
#define LOG(fmt, ...) printf(fmt, __VA_ARGS__)
```

---

## 宏取消定义

**基本写法：取消宏定义**
`#undef <NAME>`
```c
// 取消 MAX_BUFFER 的定义
#undef MAX_BUFFER
```

---

## 条件编译

**基本写法：ifdef 条件编译**
`#ifdef <MACRO> ... #endif`
```c
// 如果定义了 DEBUG 宏则编译
#ifdef DEBUG
    printf("Debug mode\n");
#endif
```

---

**基本写法：ifndef 条件编译**
`#ifndef <MACRO> ... #endif`
```c
// 如果未定义 HEADER_H 则编译
#ifndef HEADER_H
#define HEADER_H
void my_function();
#endif
```

---

**基本写法：if 条件编译**
`#if <condition> ... #endif`
```c
// 根据条件编译
#if VERSION >= 2
    printf("Version 2+\n");
#endif
```

---

**多分支写法：if-elif-else 条件编译**
`#if <cond1> ... #elif <cond2> ... #else ... #endif`
```c
// 多分支条件编译
#if defined(WIN32)
    #define OS "Windows"
#elif defined(LINUX)
    #define OS "Linux"
#else
    #define OS "Unknown"
#endif
```

---

**defined 写法：检查宏是否定义**
`#if defined(<MACRO>)`
```c
// 检查宏是否已定义
#if defined(DEBUG) && defined(VERBOSE)
    printf("Debug verbose mode\n");
#endif
```

---

## 预定义宏

**基本写法：使用预定义宏**
`__FILE__` / `__LINE__` / `__DATE__` / `__TIME__`
```c
// 输出文件名和行号
printf("File: %s, Line: %d\n", __FILE__, __LINE__);
```

---

**基本写法：使用 __func__**
`__func__`
```c
// 输出当前函数名
void my_function() {
    printf("Function: %s\n", __func__);
}
```

---

## pragma 指令

**基本写法：使用 pragma**
`#pragma <directive>`
```c
// 使用 once 防止重复包含
#pragma once
```

---

**pack 写法：设置结构体对齐**
`#pragma pack(<n>)`
```c
// 设置 1 字节对齐
#pragma pack(1)
struct Packed {
    char c;
    int i;
};
#pragma pack()
```

---

**message 写法：编译时输出消息**
`#pragma message("<message>")`
```c
// 编译时输出提示信息
#pragma message("Compiling " __FILE__)
```

---

## 行控制

**基本写法：修改行号和文件名**
`#line <line_number> "<filename>"`
```c
// 修改编译器报告的行号和文件名
#line 100 "custom_file.c"
```

---

## 错误指令

**基本写法：编译时错误**
`#error <message>`
```c
// 编译时产生错误
#ifndef VERSION
#error "VERSION must be defined"
#endif
```

---

## 宏与函数对比

**宏写法：使用宏实现简单函数**
`#define <NAME>(<params>) <expression>`
```c
// 使用宏实现平方运算
#define SQUARE(x) ((x) * (x))
```

---

**内联写法：使用内联函数替代宏**
`inline <type> <func>(<params>) { ... }`
```c
// 使用内联函数实现平方运算
inline int square(int x) {
    return x * x;
}
```

---

## 头文件保护

**基本写法：使用 ifndef 保护头文件**
`#ifndef <HEADER_H> / #define <HEADER_H> / ... / #endif`
```c
// 头文件保护宏
#ifndef MY_HEADER_H
#define MY_HEADER_H
void my_function();
#endif /* MY_HEADER_H */
```

---

**once 写法：使用 pragma once**
`#pragma once`
```c
// 使用 pragma once 防止重复包含
#pragma once
void my_function();
```

---

## 预处理运算符

**字符串化写法：# 运算符**
`#define <NAME>(x) #x`
```c
// 将宏参数转换为字符串
#define PRINT_VAR(x) printf(#x " = %d\n", x)
```

---

**标记拼接写法：## 运算符**
`#define <NAME>(a, b) a##b`
```c
// 拼接两个标记形成新标识符
#define CREATE_VAR(name) int name##Var = 0
```



<!-- ============ 文档分隔线：025-c/014-OperatorExpression.md ============ -->

# 运算符与表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 算术运算符

**加法写法：加法运算**
`<expr> + <expr>`
```c
// 计算两数之和
int a = 10, b = 3;
int sum = a + b;
```

---

**减法写法：减法运算**
`<expr> - <expr>`
```c
// 计算两数之差
int a = 10, b = 3;
int diff = a - b;
```

---

**乘法写法：乘法运算**
`<expr> * <expr>`
```c
// 计算两数之积
int a = 10, b = 3;
int product = a * b;
```

---

**除法写法：除法运算**
`<expr> / <expr>`
```c
// 整数除法（舍去小数）
int a = 10, b = 3;
int quotient = a / b;
```

---

**取模写法：取模运算**
`<expr> % <expr>`
```c
// 计算余数
int a = 10, b = 3;
int remainder = a % b;
```

---

**后置写法：后置自增**
`<var>++`
```c
// 返回原值后自增
int c = 5;
int result = c++;
```

---

**前置写法：前置自增**
`++<var>`
```c
// 先自增后返回新值
int c = 5;
int result = ++c;
```

---

**后置写法：后置自减**
`<var>--`
```c
// 返回原值后自减
int c = 5;
int result = c--;
```

---

**前置写法：前置自减**
`--<var>`
```c
// 先自减后返回新值
int c = 5;
int result = --c;
```

---

## 关系运算符

**等于写法：等于比较**
`<expr> == <expr>`
```c
// 判断两数是否相等
int a = 10, b = 3;
int result = (a == b);
```

---

**不等于写法：不等于比较**
`<expr> != <expr>`
```c
// 判断两数是否不等
int a = 10, b = 3;
int result = (a != b);
```

---

**大于写法：大于比较**
`<expr> > <expr>`
```c
// 判断 a 是否大于 b
int a = 10, b = 3;
int result = (a > b);
```

---

**小于写法：小于比较**
`<expr> < <expr>`
```c
// 判断 a 是否小于 b
int a = 10, b = 3;
int result = (a < b);
```

---

## 逻辑运算符

**逻辑与写法：逻辑与运算**
`<expr> && <expr>`
```c
// 短路逻辑与，左为假时右不执行
int a = 10, b = 0;
int result = (a > 0) && (b > 0);
```

---

**逻辑或写法：逻辑或运算**
`<expr> || <expr>`
```c
// 短路逻辑或，左为真时右不执行
int a = 10, b = 0;
int result = (a > 0) || (b > 0);
```

---

**逻辑非写法：逻辑非运算**
`!<expr>`
```c
// 逻辑取反
int a = 10;
int result = !(a > 0);
```

---

## 位运算符

**按位与写法：按位与运算**
`<expr> & <expr>`
```c
// 按位与
int a = 6, b = 3;
int result = a & b;
```

---

**按位或写法：按位或运算**
`<expr> | <expr>`
```c
// 按位或
int a = 6, b = 3;
int result = a | b;
```

---

**按位异或写法：按位异或运算**
`<expr> ^ <expr>`
```c
// 按位异或
int a = 6, b = 3;
int result = a ^ b;
```

---

**按位取反写法：按位取反运算**
`~<expr>`
```c
// 按位取反
int a = 6;
int result = ~a;
```

---

**左移写法：左移运算**
`<expr> << <n>`
```c
// 左移 1 位
int a = 6;
int result = a << 1;
```

---

**右移写法：右移运算**
`<expr> >> <n>`
```c
// 右移 1 位
int a = 6;
int result = a >> 1;
```

---

**位操作宏写法：检查某一位**
`#define <NAME>(x, pos) ((x) & (1U << (pos)))`
```c
// 检查指定位是否为 1
#define CHECK_BIT(x, pos) ((x) & (1U << (pos)))
```

---

**位操作宏写法：设置某一位**
`#define <NAME>(x, pos) ((x) |= (1U << (pos)))`
```c
// 设置指定位为 1
#define SET_BIT(x, pos) ((x) |= (1U << (pos)))
```

---

**位操作宏写法：清除某一位**
`#define <NAME>(x, pos) ((x) &= ~(1U << (pos)))`
```c
// 清除指定位为 0
#define CLEAR_BIT(x, pos) ((x) &= ~(1U << (pos)))
```

---

## 赋值运算符

**基本写法：简单赋值**
`<var> = <expr>;`
```c
// 简单赋值
int a = 10;
```

---

**复合写法：加赋值**
`<var> += <expr>;`
```c
// 等价于 a = a + b
int a = 10, b = 3;
a += b;
```

---

**复合写法：减赋值**
`<var> -= <expr>;`
```c
// 等价于 a = a - b
int a = 10, b = 3;
a -= b;
```

---

**复合写法：乘赋值**
`<var> *= <expr>;`
```c
// 等价于 a = a * b
int a = 10, b = 3;
a *= b;
```

---

**复合写法：除赋值**
`<var> /= <expr>;`
```c
// 等价于 a = a / b
int a = 10, b = 3;
a /= b;
```

---

## 其他运算符

**sizeof 写法：获取大小**
`sizeof(<type|var>)`
```c
// 获取 int 类型字节数
size_t size = sizeof(int);
```

---

**取地址写法：获取变量地址**
`&<var>`
```c
// 获取变量地址
int a = 10;
int *p = &a;
```

---

**解引用写法：通过指针访问值**
`*<ptr>`
```c
// 解引用指针获取值
int a = 10;
int *p = &a;
int val = *p;
```

---

**三目写法：条件运算符**
`<condition> ? <expr1> : <expr2>`
```c
// 找出最大值
int a = 10, b = 3;
int max = (a > b) ? a : b;
```

---

**逗号写法：逗号运算符**
`<expr1>, <expr2>, ..., <exprN>`
```c
// 从左到右执行，返回最后一个表达式的值
int c = (a = 5, b = 10, a + b);
```

---

## 表达式类型转换

**隐式写法：自动类型转换**
`<type> <var> = <other_type_var>;`
```c
// int 转换为 float
int a = 10;
float result = a + 3.14f;
```

---

**显式写法：强制类型转换**
`(<target_type>)<expression>`
```c
// 显式转换 double 为 int
double pi = 3.14159;
int area = (int)(pi * 5 * 5);
```



<!-- ============ 文档分隔线：025-c/015-PointerDeep.md ============ -->

# 指针深度解析

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 指针基础

**基本写法：指针声明与初始化**
`<type> *<ptr_name> = &<var>;`
```c
// ptr 指向 x 的地址
int x = 10;
int *ptr = &x;
```

---

**基本写法：指针声明（未初始化）**
`<type> *<ptr_name>;`
```c
// 声明未初始化的指针
int *ptr;
```

---

**空指针写法：初始化为 NULL**
`<type> *<ptr_name> = NULL;`
```c
// 初始化为空指针
int *ptr = NULL;
```

---

**解引用写法：通过指针读取值**
`*<ptr>`
```c
// 解引用获取指针指向的值
int x = 10;
int *ptr = &x;
printf("值: %d\n", *ptr);
```

---

**解引用写法：通过指针修改值**
`*<ptr> = <new_value>;`
```c
// 通过指针修改变量的值
int x = 10;
int *ptr = &x;
*ptr = 20;
```

---

**取地址写法：获取变量地址**
`&<var>`
```c
// 获取变量地址
int x = 10;
printf("地址: %p\n", (void*)&x);
```

---

## 指针类型

**基本写法：不同类型指针**
`<type> *<ptr_name>;`
```c
// 不同类型的指针
int *int_ptr;
char *char_ptr;
double *double_ptr;
```

---

**void 指针写法：通用指针**
`void *<ptr_name>;`
```c
// 可以指向任何类型的通用指针
void *generic_ptr;
int x = 10;
generic_ptr = &x;
```

---

**void 指针转换写法：类型转换**
`(<target_type> *)<void_ptr>`
```c
// void 指针转换为具体类型指针
void *ptr = &x;
int *int_ptr = (int *)ptr;
```

---

**const 指针写法：指向常量的指针**
`const <type> *<ptr_name>;`
```c
// 不能通过指针修改所指向的值
const int *p1;
```

---

**常量指针写法：指针本身为常量**
`<type> * const <ptr_name> = &<var>;`
```c
// 指针本身不能改变指向
int x = 10;
int* const p3 = &x;
```

---

**双重 const 写法：指向常量的常量指针**
`const <type> * const <ptr_name> = &<var>;`
```c
// 既不能修改值，也不能修改指针
int x = 10;
const int* const p4 = &x;
```

---

## 指针与数组

**基本写法：数组名作为指针**
`<type> *<ptr> = <array_name>;`
```c
// 数组名即首元素地址
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
```

---

**指针算术写法：指针加减运算**
`<ptr> + <n>` 或 `<ptr> - <n>`
```c
// 指针向后移动 n 个元素
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
int *q = p + 2;
```

---

**自增写法：指针自增**
`<ptr>++` 或 `++<ptr>`
```c
// 指针指向下一个元素
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
p++;
```

---

**指针差写法：计算两个指针间元素个数**
`<ptr1> - <ptr2>`
```c
// 计算指针间元素个数
int arr[5] = {1, 2, 3, 4, 5};
int *p1 = &arr[0];
int *p2 = &arr[3];
int diff = p2 - p1;
```

---

**下标写法：指针下标访问**
`<ptr>[<index>]`
```c
// 指针使用下标访问
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
printf("%d\n", p[2]);
```

---

## 指针数组与数组指针

**指针数组写法：存储指针的数组**
`<type> *<array_name>[<size>];`
```c
// 指针数组
int *ptr_array[3];
int a = 10, b = 20, c = 30;
ptr_array[0] = &a;
```

---

**数组指针写法：指向数组的指针**
`<type> (*<ptr_name>)[<size>];`
```c
// 指向整个数组的指针
int arr[5] = {1, 2, 3, 4, 5};
int (*p)[5] = &arr;
```

---

## 字符串指针

**基本写法：字符串指针**
`char *<str> = "<string>";`
```c
// 字符串指针指向字符串常量
char *str = "Hello C";
```

---

**字符数组写法：字符数组**
`char <str>[] = "<string>";`
```c
// 字符数组存储字符串
char str[] = "Hello C";
```

---

**遍历写法：使用指针遍历字符串**
`while (*<ptr> != '\0') { ... <ptr>++; }`
```c
// 使用指针遍历字符串
char *str = "Hello";
while (*str != '\0') {
    printf("%c", *str);
    str++;
}
```

---

## 函数指针

**基本写法：函数指针定义**
`<return_type> (*<ptr_name>)(<parameter_list>);`
```c
// 定义函数指针
int (*add_ptr)(int, int);
```

---

**赋值写法：函数指针赋值**
`<func_ptr> = <func_name>;`
```c
// 将函数地址赋给指针
add_ptr = add;
```

---

**调用写法：通过函数指针调用**
`<result> = <func_ptr>(<args>);`
```c
// 通过函数指针调用函数
int result = add_ptr(10, 20);
```

---

**typedef 写法：定义回调函数类型**
`typedef <return_type> (*<CallbackName>)(<params>);`
```c
// 定义回调函数类型
typedef void (*Callback)(int);
```

---

**回调写法：使用回调函数**
`void <func>(<type> <arr>[], int <size>, <CallbackType> <callback>) { ... }`
```c
// 执行回调的函数
void process_array(int arr[], int size, Callback callback) {
    for (int i = 0; i < size; i++) {
        callback(arr[i]);
    }
}
```

---

**数组写法：函数指针数组**
`<return_type> (*<array_name>[])(<params>) = { <func1>, <func2>, ... };`
```c
// 函数指针数组
int (*operations[])(int, int) = {add, subtract, multiply};
```

---

## 多级指针

**二级指针写法：指向指针的指针**
`<type> **<ptr_name>;`
```c
// 二级指针
int x = 10;
int *p = &x;
int **pp = &p;
```

---

**二级指针访问写法：解引用二级指针**
`**<ptr_name>`
```c
// 通过二级指针访问原始值
int x = 10;
int *p = &x;
int **pp = &p;
printf("%d\n", **pp);
```

---

**三级指针写法：三级指针**
`<type> ***<ptr_name>;`
```c
// 三级指针
int x = 10;
int *p = &x;
int **pp = &p;
int ***ppp = &pp;
```

---

## 动态内存分配

**malloc 写法：分配内存**
`<type> *<ptr> = (<type> *)malloc(<size> * sizeof(<type>));`
```c
#include <stdlib.h>
// 分配单个变量的内存
int *p = (int *)malloc(sizeof(int));
```

---

**calloc 写法：分配并清零**
`<type> *<ptr> = (<type> *)calloc(<count>, sizeof(<type>));`
```c
#include <stdlib.h>
// 分配数组并初始化为 0
int *arr = (int *)calloc(10, sizeof(int));
```

---

**realloc 写法：重新分配内存**
`<type> *<new_ptr> = (<type> *)realloc(<ptr>, <new_size> * sizeof(<type>));`
```c
#include <stdlib.h>
// 重新调整内存大小
int *new_arr = (int *)realloc(arr, 20 * sizeof(int));
```

---

**free 写法：释放内存**
`free(<ptr>);`
```c
#include <stdlib.h>
// 释放动态分配的内存
free(p);
```

---

## 指针与结构体

**基本写法：指向结构体的指针**
`<StructType> *<ptr_name> = &<var>;`
```c
// 指向结构体的指针
typedef struct { int x; int y; } Point;
Point p = {10, 20};
Point *ptr = &p;
```

---

**成员访问写法：通过指针访问成员**
`<ptr>-><member>`
```c
// 使用 -> 访问结构体成员
printf("x: %d\n", ptr->x);
```

---

## 指针常见陷阱

**野指针写法：未初始化的指针**
`<type> *<ptr>;` （危险）
```c
// 危险：未初始化的指针
int *ptr;
// *ptr = 10; // 未定义行为
```

---

**悬空指针写法：释放后仍使用**
`free(<ptr>); <ptr> = NULL;`
```c
// 释放后将指针置空
free(p);
p = NULL;
```



<!-- ============ 文档分隔线：025-c/016-CStandardLibrary.md ============ -->

# C 标准库函数速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 输入输出

**基本写法：printf 格式输出**
`printf("<格式串>"[, <参数>...]);`
```c
// 格式化输出
printf("Value: %d, Name: %s\n", 42, "Alice");
```

---

**基本写法：scanf 格式输入**
`scanf("<格式串>", &<变量>[, &<变量>...]);`
```c
// 读取整数
int x;
scanf("%d", &x);
```

---

**基本写法：fprintf 文件输出**
`fprintf(<FILE*>, "<格式串>"[, <参数>...]);`
```c
// 输出到文件
FILE* fp = fopen("out.txt", "w");
fprintf(fp, "Count: %d\n", 10);
```

---

**基本写法：fopen 打开文件**
`fopen("<路径>", "<模式>");`
```c
// 打开文件读取
FILE* fp = fopen("data.txt", "r");
// 模式: r 读, w 写, a 追加, rb/wb 二进制
```

---

**基本写法：fclose 关闭文件**
`fclose(<FILE*>);`
```c
// 关闭文件
fclose(fp);
```

---

## 字符串操作

**基本写法：strcpy 复制**
`strcpy(<目标>, <源>);`
```c
// 复制字符串
char dest[100];
strcpy(dest, "Hello");
```

---

**基本写法：strncpy 安全复制**
`strncpy(<目标>, <源>, <长度>);`
```c
// 限制长度复制
char dest[10];
strncpy(dest, "Hello", sizeof(dest) - 1);
dest[sizeof(dest) - 1] = '\0';
```

---

**基本写法：strcat 拼接**
`strcat(<目标>, <源>);`
```c
// 拼接字符串
char s[100] = "Hello, ";
strcat(s, "World!");
```

---

**基本写法：strlen 长度**
`strlen(<字符串>);`
```c
// 获取字符串长度
size_t len = strlen("Hello");
```

---

**基本写法：strcmp 比较**
`strcmp(<字符串1>, <字符串2>);`
```c
// 比较字符串
int result = strcmp("abc", "def");
// 返回 0 表示相等
```

---

## 内存操作

**基本写法：malloc 分配**
`malloc(<字节数>);`
```c
// 动态分配内存
int* arr = (int*)malloc(10 * sizeof(int));
```

---

**基本写法：calloc 清零分配**
`calloc(<数量>, <单个大小>);`
```c
// 分配并清零
int* arr = (int*)calloc(10, sizeof(int));
```

---

**基本写法：realloc 重分配**
`realloc(<指针>, <新大小>);`
```c
// 重新调整内存大小
arr = (int*)realloc(arr, 20 * sizeof(int));
```

---

**基本写法：free 释放**
`free(<指针>);`
```c
// 释放动态分配的内存
free(arr);
arr = NULL;
```

---

**基本写法：memcpy 内存复制**
`memcpy(<目标>, <源>, <字节数>);`
```c
// 复制内存块
int src[5] = {1, 2, 3, 4, 5};
int dest[5];
memcpy(dest, src, 5 * sizeof(int));
```

---

**基本写法：memset 内存填充**
`memset(<指针>, <值>, <字节数>);`
```c
// 内存清零
memset(arr, 0, 10 * sizeof(int));
```

---

## 数学函数

**基本写法：abs 绝对值**
`abs(<整数>);`
```c
// 整数绝对值
int x = abs(-10);
```

---

**基本写法：sqrt 平方根**
`sqrt(<浮点数>);`
```c
// 求平方根
double r = sqrt(16.0);
```

---

**基本写法：pow 幂运算**
`pow(<底数>, <指数>);`
```c
// 计算 2 的 10 次方
double r = pow(2.0, 10.0);
```

---

**基本写法：floor/ceil 取整**
`floor(<浮点数>);` `<br>`ceil(<浮点数>);`
```c
// 向下取整
double f = floor(3.7);
// 向上取整
double c = ceil(3.2);
```

---

## 时间函数

**基本写法：time 获取时间**
`time(<time_t*>);`
```c
// 获取当前时间戳
time_t now = time(NULL);
```

---

**基本写法：clock 计时**
`clock();`
```c
// 测量执行时间
clock_t start = clock();
// ... 代码 ...
clock_t end = clock();
double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
```

---

## 字符分类

**基本写法：isdigit 数字判断**
`isdigit(<字符>);`
```c
// 判断是否为数字
if (isdigit('5')) { /* 是数字 */ }
```

---

**基本写法：isalpha 字母判断**
`isalpha(<字符>);`
```c
// 判断是否为字母
if (isalpha('A')) { /* 是字母 */ }
```

---

**基本写法：tolower 转小写**
`tolower(<字符>);`
```c
// 转换为小写
char lower = tolower('A');
```

---

**基本写法：toupper 转大写**
`toupper(<字符>);`
```c
// 转换为大写
char upper = toupper('a');
```



<!-- ============ 文档分隔线：025-c/017-CPosixSystemCall.md ============ -->

# C POSIX 与系统调用速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件描述符

**基本写法：open 打开文件**
`open("<路径>", <标志> [, <权限>]);`
```c
// 打开文件读写
int fd = open("file.txt", O_RDWR | O_CREAT, 0644);
```

---

**基本写法：read 读取**
`read(<文件描述符>, <缓冲区>, <字节数>);`
```c
// 读取最多 100 字节
char buf[100];
ssize_t n = read(fd, buf, sizeof(buf));
```

---

**基本写法：write 写入**
`write(<文件描述符>, <缓冲区>, <字节数>);`
```c
// 写入字符串
write(fd, "Hello", 5);
```

---

**基本写法：close 关闭**
`close(<文件描述符>);`
```c
// 关闭文件描述符
close(fd);
```

---

**基本写法：lseek 移动指针**
`lseek(<文件描述符>, <偏移>, <起点>);`
```c
// 移动到文件开头
lseek(fd, 0, SEEK_SET);
// 跳过 10 字节
lseek(fd, 10, SEEK_CUR);
```

---

## 进程控制

**基本写法：fork 创建进程**
`fork();`
```c
// 创建子进程
pid_t pid = fork();
if (pid == 0) {
    // 子进程
} else {
    // 父进程
}
```

---

**基本写法：exec 执行程序**
`execlp("<程序>", "<参数0>", ..., NULL);`
```c
// 执行 ls 命令
execlp("ls", "ls", "-l", NULL);
```

---

**基本写法：wait 等待子进程**
`wait(<状态指针>);`
```c
// 等待子进程结束
int status;
wait(&status);
```

---

**基本写法：exit 退出进程**
`exit(<状态码>);`
```c
// 正常退出
exit(0);
```

---

## 进程信息

**基本写法：getpid 获取进程 ID**
`getpid();`
```c
// 获取当前进程 ID
pid_t pid = getpid();
```

---

**基本写法：getppid 获取父进程 ID**
`getppid();`
```c
// 获取父进程 ID
pid_t ppid = getppid();
```

---

## 信号处理

**基本写法：signal 注册信号**
`signal(<信号>, <处理函数>);`
```c
// 捕获 Ctrl+C
void handler(int sig) { /* 处理信号 */ }
signal(SIGINT, handler);
```

---

**基本写法：kill 发送信号**
`kill(<进程ID>, <信号>);`
```c
// 发送终止信号
kill(1234, SIGTERM);
```

---

**基本写法：raise 自发送信号**
`raise(<信号>);`
```c
// 给自己发送信号
raise(SIGTERM);
```

---

## 进程间通信

**基本写法：pipe 管道**
`pipe(<描述符数组>);`
```c
// 创建管道
int fds[2];
pipe(fds);
// fds[0] 读端, fds[1] 写端
```

---

**基本写法：mkfifo 命名管道**
`mkfifo("<路径>", <权限>);`
```c
// 创建命名管道
mkfifo("/tmp/myfifo", 0644);
```

---

## 内存映射

**基本写法：mmap 内存映射**
`mmap(NULL, <长度>, <保护>, <标志>, <文件描述符>, <偏移>);`
```c
// 映射文件到内存
void* ptr = mmap(NULL, 4096, PROT_READ | PROT_WRITE,
                 MAP_SHARED, fd, 0);
```

---

**基本写法：munmap 解除映射**
`munmap(<指针>, <长度>);`
```c
// 解除内存映射
munmap(ptr, 4096);
```

---

## 系统信息

**基本写法：getenv 获取环境变量**
`getenv("<变量名>");`
```c
// 读取 PATH 环境变量
char* path = getenv("PATH");
```

---

**基本写法：system 执行命令**
`system("<命令>");`
```c
// 执行 shell 命令
system("ls -l");
```

---

## 目录操作

**基本写法：opendir 打开目录**
`opendir("<路径>");`
```c
// 打开当前目录
DIR* dir = opendir(".");
```

---

**基本写法：readdir 读取目录**
`readdir(<目录指针>);`
```c
// 遍历目录
struct dirent* entry;
while ((entry = readdir(dir)) != NULL) {
    printf("%s\n", entry->d_name);
}
```

---

**基本写法：mkdir 创建目录**
`mkdir("<路径>", <权限>);`
```c
// 创建目录
mkdir("newdir", 0755);
```

---

## 错误处理

**基本写法：errno 错误码**
`errno;`
```c
// 检查错误码
if (fd == -1) {
    printf("Error: %s\n", strerror(errno));
}
```

---

**基本写法：perror 错误输出**
`perror("<前缀>");`
```c
// 输出错误信息
perror("open failed");
```



<!-- ============ 文档分隔线：025-c/018-FunctionPointerCallback.md ============ -->

# C 函数指针与回调

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数指针基础

**基本写法：声明函数指针**
`<返回类型> (*<指针名>)(<参数>);`
```c
// 声明指向 int(int) 函数的指针
int (*fp)(int);
```

---

**基本写法：赋值函数地址**
`<指针名> = <函数名>;` 或 `<指针名> = &<函数名>;`
```c
// 函数名即地址
int sq(int x) { return x * x; }
fp = sq;
```

---

**基本写法：通过指针调用**
`<指针名>(<参数>);` 或 `(*<指针名>)(<参数>);`
```c
// 两种调用方式等价
int r = fp(5);
```

---

## 函数指针类型别名

**基本写法：typedef 别名**
`typedef <返回类型> (*<别名>)(<参数>);`
```c
// 定义函数指针类型
typedef int (*BinOp)(int, int);
BinOp op = add;
```

---

**基本写法：使用别名声明变量**
`<别名> <变量> = <函数>;`
```c
// 用别名声明更清晰
BinOp op = add;
int r = op(2, 3);
```

---

## 回调函数

**基本写法：回调参数**
`void <函数>(<参数>, <返回类型> (*<回调>)(<回调参数>));`
```c
// 函数接收回调
void process(int x, int (*cb)(int)) {
    int r = cb(x);
}
```

---

**基本写法：传递函数作为回调**
`<函数>(<参数>, <回调函数>);`
```c
// 传入函数名作为回调
process(5, sq);
```

---

**基本写法：回调上下文指针**
`void <函数>(void* <ctx>, void (*<回调>)(void*, int));`
```c
// 携带上下文的回调
void iterate(int* arr, int n, void* ctx, void (*cb)(void*, int)) {
    for (int i = 0; i < n; i++) cb(ctx, arr[i]);
}
```

---

## 函数指针数组

**基本写法：函数指针数组**
`<返回类型> (*<数组名>[<数量>])(<参数>);`
```c
// 存储多个函数指针
int (*ops[4])(int, int) = {add, sub, mul, div};
```

---

**基本写法：通过索引调用**
`<数组名>[<索引>](<参数>);`
```c
// 选择调用对应函数
int r = ops[0](2, 3);
```

---

## 跳转表

**基本写法：跳转表实现**
`<别名> <表名>[] = { <函数1>, <函数2>, ... };`
```c
// 用枚举索引选择操作
typedef int (*Op)(int, int);
Op table[] = { add, sub, mul, div };
int r = table[OP_ADD](a, b);
```

---

## qsort 回调

**基本写法：qsort 比较函数**
`int <比较>(const void* <a>, const void* <b>);`
```c
// 标准库排序比较函数
int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}
```

---

**基本写法：调用 qsort**
`qsort(<数组>, <数量>, <大小>, <比较函数>);`
```c
// 排序整型数组
qsort(arr, n, sizeof(int), cmp);
```

---

## bsearch 回调

**基本写法：二分查找**
`bsearch(<关键字>, <数组>, <数量>, <大小>, <比较函数>);`
```c
// 在有序数组中查找
int key = 42;
int* found = bsearch(&key, arr, n, sizeof(int), cmp);
```

---

## 返回函数指针

**基本写法：函数返回函数指针**
`<别名> <函数名>(<参数>);`
```c
// 根据条件返回不同操作
BinOp select_op(char c) {
    if (c == '+') return add;
    return sub;
}
```

---

## 复杂声明

**基本写法：指向返回函数指针的函数的指针**
`<返回类型> (*(*<指针>)(<参数>))(<参数>);`
```c
// 指向返回 BinOp 的函数的指针
BinOp (*selector)(char) = select_op;
```

---

## 注意事项

**基本写法：函数指针可为 NULL**
`if (<指针> != NULL) <指针>(<参数>);`
```c
// 调用前检查有效性
if (cb != NULL) cb(data);
```

---

**基本写法：函数指针类型转换**
`(void (*)(void))<函数>`
```c
// 转为通用函数指针类型
void (*generic)(void) = (void (*)(void))cb;
```



<!-- ============ 文档分隔线：025-c/019-BitwiseOperation.md ============ -->

# C 位运算

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本位运算

**基本写法：按位与**
`<a> & <b>`
```c
// 按位与常用于掩码
int r = 0xF0 & 0x0F;   // 结果 0
```

---

**基本写法：按位或**
`<a> | <b>`
```c
// 按位或常用于置位
int r = 0xF0 | 0x0F;   // 结果 0xFF
```

---

**基本写法：按位异或**
`<a> ^ <b>`
```c
// 异或可用于翻转位
int r = 0xFF ^ 0x0F;   // 结果 0xF0
```

---

**基本写法：按位取反**
`~<a>`
```c
// 取反所有位
int r = ~0;   // -1
```

---

## 移位运算

**基本写法：左移**
`<a> << <位数>`
```c
// 左移一位相当于乘 2
int r = 1 << 4;   // 16
```

---

**基本写法：右移**
`<a> >> <位数>`
```c
// 右移一位相当于除 2
int r = 256 >> 2;   // 64
```

---

## 位掩码操作

**基本写法：置位**
`<变量> |= (1 << <位号>);`
```c
// 将第 3 位置 1
flags |= (1 << 3);
```

---

**基本写法：清位**
`<变量> &= ~(1 << <位号>);`
```c
// 将第 3 位清 0
flags &= ~(1 << 3);
```

---

**基本写法：翻转位**
`<变量> ^= (1 << <位号>);`
```c
// 翻转第 3 位
flags ^= (1 << 3);
```

---

**基本写法：检测位**
`if (<变量> & (1 << <位号>))`
```c
// 判断第 3 位是否为 1
if (flags & (1 << 3)) { /* 已置位 */ }
```

---

## 常用技巧

**基本写法：判断奇偶**
`<n> & 1`
```c
// 最低位为 1 即奇数
if ((n & 1) == 0) { /* 偶数 */ }
```

---

**基本写法：交换两数**
`<a> ^= <b>; <b> ^= <a>; <a> ^= <b>;`
```c
// 异或交换无需临时变量
a ^= b; b ^= a; a ^= b;
```

---

**基本写法：求绝对值**
`(<n> ^ (<n> >> 31)) - (<n> >> 31)`
```c
// 32 位整数求绝对值
int abs_n = (n ^ (n >> 31)) - (n >> 31);
```

---

**基本写法：判断 2 的幂**
`<n> > 0 && !(<n> & (<n> - 1))`
```c
// 2 的幂只有一个 1 位
if (n > 0 && !(n & (n - 1))) { /* 是 2 的幂 */ }
```

---

**基本写法：最低位的 1**
`<n> & -<n>`
```c
// 取最低有效位
int low = n & -n;
```

---

## 位域

**基本写法：定义位域**
`struct <名称> { <类型> <成员> : <位数>; };`
```c
// 紧凑存储多个标志
struct Flags {
    unsigned int a : 1;
    unsigned int b : 3;
    unsigned int c : 4;
};
```

---

**基本写法：访问位域成员**
`<变量>.<成员>`
```c
// 直接访问位域
struct Flags f;
f.a = 1;
f.b = 5;
```

---

## stdbit.h C23

**基本写法：统计 1 的个数**
`stdc_count_ones(<值>)`
```c
// C23 标准位计数
unsigned n = stdc_count_ones(0xFF);   // 8
```

---

**基本写法：统计前导零**
`stdc_leading_zeros(<值>)`
```c
// C23 前导零数量
unsigned z = stdc_leading_zeros(1u);
```

---

**基本写法：统计末尾零**
`stdc_trailing_zeros(<值>)`
```c
// C23 末尾零数量
unsigned z = stdc_trailing_zeros(8u);   // 3
```

---

**基本写法：查找最高位**
`stdc_bit_width(<值>)`
```c
// C23 计算所需位数
unsigned w = stdc_bit_width(255);   // 8
```

---

## 二进制字面量 C23

**基本写法：二进制常量**
`0b<二进制>` 或 `0B<二进制>`
```c
// C23 支持二进制字面量
int mask = 0b10101010;
```

---

**基本写法：数字分隔符**
`<数字>'<数字>`
```c
// C23 数字分隔符提高可读性
int big = 0b1010'1010;
```



<!-- ============ 文档分隔线：025-c/020-GenericSelection.md ============ -->

# C 泛型选择 _Generic

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## _Generic 基础

**基本写法：泛型选择表达式**
`_Generic(<表达式>, <类型>: <结果>, default: <默认>)`
```c
// 根据表达式类型选择结果
const char* name = _Generic(x,
    int: "int",
    double: "double",
    default: "other");
```

---

**基本写法：多类型分支**
`_Generic(<表达式>, <类型1>: <值1>, <类型2>: <值2>)`
```c
// 编译期类型分派
int s = _Generic(arr,
    int*: sizeof(int),
    char*: sizeof(char),
    default: 0);
```

---

## 泛型宏

**基本写法：类型感知打印宏**
`#define <宏名>(<x>) _Generic((<x>), ...)`
```c
// 根据类型选择打印格式
#define print_val(x) _Generic((x), \
    int: printf("%d\n", (x)), \
    double: printf("%f\n", (x)), \
    char*: printf("%s\n", (x)))
```

---

**基本写法：泛型打印调用**
`<宏名>(<值>);`
```c
// 调用自动分派
print_val(42);
print_val(3.14);
```

---

## 泛型函数分发

**基本写法：泛型函数选择**
`#define <宏名>(<x>) _Generic((<x>), <类型>: <函数>, ...)`
```c
// 类型对应的实现函数
int add_i(int a, int b);
double add_d(double a, double b);
#define add(x, y) _Generic((x), \
    int: add_i, \
    double: add_d)((x), (y))
```

---

**基本写法：调用泛型函数**
`<宏名>(<参数1>, <参数2>);`
```c
// 自动选择 int 或 double 版本
int r1 = add(1, 2);
double r2 = add(1.0, 2.0);
```

---

## 类型分组

**基本写法：用 default 兜底**
`_Generic(<表达式>, <类型>: <值>, default: <默认值>)`
```c
// 未匹配类型走 default
int kind = _Generic(x, int: 1, double: 2, default: 0);
```

---

**基本写法：区分有符号无符号**
`_Generic(<表达式>, int: ..., unsigned int: ...)`
```c
// 分别处理有符号无符号
const char* s = _Generic(x,
    int: "signed",
    unsigned int: "unsigned");
```

---

## 实用示例

**基本写法：安全的数组大小宏**
`#define ARR_LEN(<a>) (sizeof(<a>) / sizeof((<a>)[0]))`
```c
// 配合 _Generic 校验类型
#define arr_len(a) _Generic((a), \
    int*: sizeof(a)/sizeof(int), \
    default: sizeof(a)/sizeof((a)[0]))
```

---

**基本写法：类型名查询宏**
`#define TYPE_NAME(<x>) _Generic((<x>), ...)`
```c
// 返回类型名字符串
#define TYPE_NAME(x) _Generic((x), \
    _Bool: "bool", \
    char: "char", \
    signed char: "signed char", \
    short: "short", \
    int: "int", \
    long: "long", \
    long long: "long long", \
    float: "float", \
    double: "double", \
    default: "unknown")
```

---

## 复合类型

**基本写法：处理指针类型**
`_Generic(<表达式>, <类型>*: <分支>)`
```c
// 区分指针与普通类型
const char* s = _Generic(x,
    int*: "pointer",
    int: "value",
    default: "?");
```

---

**基本写法：处理 const**
`_Generic(<表达式>, const <类型>: <分支>, <类型>: <分支>)`
```c
// const 与非 const 视为不同类型
const char* s = _Generic(x,
    const int: "const int",
    int: "int");
```

---

## 注意事项

**基本写法：_Generic 是编译期选择**
`_Generic(<表达式>, ...)  // 仅求值类型不求值表达式`
```c
// 副作用表达式仅类型被使用
int r = _Generic(side_effect(), int: 0);
// side_effect 不会实际调用
```

---

**基本写法：数组退化为指针**
`_Generic(<数组名>, <类型>*: ...)`
```c
// 数组在 _Generic 中退化为指针
int arr[10];
const char* s = _Generic(arr, int*: "ptr", default: "other");
```



<!-- ============ 文档分隔线：025-c/021-AtomicAndMemoryModel.md ============ -->

# C 原子操作与内存模型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 原子类型

**基本写法：声明原子变量**
`_Atomic(<类型>) <变量>;`
```c
// 声明原子整型
_Atomic(int) counter = 0;
```

---

**基本写法：原子类型简写**
`_Atomic <类型> <变量>;`
```c
// 简写形式
_Atomic int counter = 0;
```

---

**基本写法：原子标志**
`atomic_flag <变量> = ATOMIC_FLAG_INIT;`
```c
// 最轻量的原子类型
atomic_flag lock = ATOMIC_FLAG_INIT;
```

---

## 原子操作

**基本写法：原子加载**
`atomic_load(&<变量>);`
```c
// 原子读取值
int v = atomic_load(&counter);
```

---

**基本写法：原子存储**
`atomic_store(&<变量>, <值>);`
```c
// 原子写入值
atomic_store(&counter, 10);
```

---

**基本写法：原子交换**
`atomic_exchange(&<变量>, <值>);`
```c
// 替换并返回旧值
int old = atomic_exchange(&counter, 5);
```

---

**基本写法：原子比较交换**
`atomic_compare_exchange_strong(&<变量>, &<期望>, <新值>);`
```c
// CAS 操作成功返回 true
int expected = 0;
bool ok = atomic_compare_exchange_strong(&counter, &expected, 1);
```

---

**基本写法：弱版本 CAS**
`atomic_compare_exchange_weak(&<变量>, &<期望>, <新值>);`
```c
// 可能伪失败适合循环中
while (!atomic_compare_exchange_weak(&counter, &expected, expected + 1));
```

---

**基本写法：原子加法**
`atomic_fetch_add(&<变量>, <值>);`
```c
// 原子加并返回旧值
int prev = atomic_fetch_add(&counter, 1);
```

---

**基本写法：原子减法**
`atomic_fetch_sub(&<变量>, <值>);`
```c
// 原子减并返回旧值
int prev = atomic_fetch_sub(&counter, 1);
```

---

**基本写法：原子按位与**
`atomic_fetch_and(&<变量>, <值>);`
```c
// 原子按位与
int prev = atomic_fetch_and(&flags, 0xFF);
```

---

**基本写法：原子按位或**
`atomic_fetch_or(&<变量>, <值>);`
```c
// 原子按位或
int prev = atomic_fetch_or(&flags, 0x10);
```

---

## 自旋锁示例

**基本写法：自旋锁加锁**
`while (atomic_flag_test_and_set(&<锁>)) {}`
```c
// 使用 atomic_flag 实现自旋锁
while (atomic_flag_test_and_set(&lock)) {
    // 等待
}
```

---

**基本写法：自旋锁解锁**
`atomic_flag_clear(&<锁>);`
```c
// 释放自旋锁
atomic_flag_clear(&lock);
```

---

## 内存顺序

**基本写法：顺序一致**
`memory_order_seq_cst`
```c
// 最严格的全局顺序
atomic_store(&v, 1, memory_order_seq_cst);
```

---

**基本写法：获取语义**
`memory_order_acquire`
```c
// 加载时防止后续读重排
int v = atomic_load(&flag, memory_order_acquire);
```

---

**基本写法：释放语义**
`memory_order_release`
```c
// 存储时防止前面写重排
atomic_store(&flag, 1, memory_order_release);
```

---

**基本写法：宽松语义**
`memory_order_relaxed`
```c
// 仅原子无顺序约束
atomic_fetch_add(&counter, 1, memory_order_relaxed);
```

---

**基本写法：带内存顺序的 CAS**
`atomic_compare_exchange_strong_explicit(&<变量>, &<期望>, <新值>, <成功序>, <失败序>);`
```c
// 显式指定内存顺序
atomic_compare_exchange_strong_explicit(
    &v, &expected, newval,
    memory_order_acq_rel, memory_order_acquire);
```

---

## 栅栏

**基本写法：线程栅栏**
`atomic_thread_fence(<内存序>);`
```c
// 显式内存屏障
atomic_thread_fence(memory_order_release);
```

---

**基本写法：信号栅栏**
`atomic_signal_fence(<内存序>);`
```c
// 信号处理函数内屏障
atomic_signal_fence(memory_order_acquire);
```

---

## 同步关系

**基本写法：发布订阅模式**
`store(release)` ↔ `load(acquire)`
```c
// 线程间建立先行关系
// 线程 A
data = 42;
atomic_store(&flag, 1, memory_order_release);
// 线程 B
while (!atomic_load(&flag, memory_order_acquire));
// 此处能看到 data == 42
```

---

## 常用查询

**基本写法：是否锁自由**
`atomic_is_lock_free(&<变量>);`
```c
// 查询是否无锁实现
bool free = atomic_is_lock_free(&counter);
```

---

**基本写法：原子大小**
`_Atomic(<类型>)` 大小通常与原类型相同
```c
// 原子类型大小
size_t sz = sizeof(_Atomic(int));
```



<!-- ============ 文档分隔线：025-c/022-C11ThreadConcurrency.md ============ -->

# C11 线程并发

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 线程创建

**基本写法：创建线程**
`thrd_create(&<线程>, <函数>, <参数>);`
```c
// 启动新线程执行函数
thrd_t t;
thrd_create(&t, worker, arg);
```

---

**基本写法：线程函数签名**
`int <函数名>(void* <参数>);`
```c
// 线程入口函数返回 int
int worker(void* arg) {
    return 0;
}
```

---

**基本写法：等待线程结束**
`thrd_join(<线程>, [&<结果>]);`
```c
// 阻塞等待线程完成
int result;
thrd_join(t, &result);
```

---

**基本写法：分离线程**
`thrd_detach(<线程>);`
```c
// 线程独立运行
thrd_detach(t);
```

---

**基本写法：当前线程让出**
`thrd_yield();`
```c
// 主动让出 CPU
thrd_yield();
```

---

**基本写法：线程休眠**
`thrd_sleep(&<时长>, NULL);`
```c
// 休眠指定时长
struct timespec ts = {2, 0};
thrd_sleep(&ts, NULL);
```

---

**基本写法：获取当前线程**
`thrd_current();`
```c
// 获取当前线程标识
thrd_t self = thrd_current();
```

---

## 互斥锁

**基本写法：创建互斥锁**
`mtx_t <变量>; mtx_init(&<变量>, mtx_plain);`
```c
// 初始化普通互斥锁
mtx_t m;
mtx_init(&m, mtx_plain);
```

---

**基本写法：加锁解锁**
`mtx_lock(&<锁>);` `mtx_unlock(&<锁>);`
```c
// 临界区保护
mtx_lock(&m);
// 临界区
mtx_unlock(&m);
```

---

**基本写法：尝试加锁**
`mtx_trylock(&<锁>);`
```c
// 非阻塞加锁
if (mtx_trylock(&m) == thrd_success) { }
```

---

**基本写法：定时加锁**
`mtx_timedlock(&<锁>, &<超时>);`
```c
// 限时等待加锁
struct timespec ts;
mtx_timedlock(&m, &ts);
```

---

**基本写法：销毁互斥锁**
`mtx_destroy(&<锁>);`
```c
// 释放互斥锁资源
mtx_destroy(&m);
```

---

**基本写法：递归互斥锁**
`mtx_init(&<锁>, mtx_recursive);`
```c
// 同一线程可多次加锁
mtx_init(&m, mtx_recursive);
```

---

## 条件变量

**基本写法：创建条件变量**
`cnd_t <变量>; cnd_init(&<变量>);`
```c
// 初始化条件变量
cnd_t cv;
cnd_init(&cv);
```

---

**基本写法：等待条件**
`cnd_wait(&<cv>, &<锁>);`
```c
// 释放锁并等待唤醒
mtx_lock(&m);
while (!ready) cnd_wait(&cv, &m);
mtx_unlock(&m);
```

---

**基本写法：通知一个**
`cnd_signal(&<cv>);`
```c
// 唤醒一个等待线程
cnd_signal(&cv);
```

---

**基本写法：通知所有**
`cnd_broadcast(&<cv>);`
```c
// 唤醒所有等待线程
cnd_broadcast(&cv);
```

---

**基本写法：销毁条件变量**
`cnd_destroy(&<cv>);`
```c
// 释放条件变量资源
cnd_destroy(&cv);
```

---

## 线程局部存储

**基本写法：线程局部变量**
`_Thread_local <类型> <变量>;`
```c
// 每个线程独立副本
_Thread_local int tid = 0;
```

---

**基本写法：使用 TSS**
`tss_t <键>; tss_create(&<键>, NULL); tss_set(<键>, <指针>);`
```c
// 线程特定存储
tss_t key;
tss_create(&key, NULL);
tss_set(key, ptr);
void* p = tss_get(key);
```

---

## 一次性初始化

**基本写法：call_once**
`once_flag <标志> = ONCE_FLAG_INIT; call_once(&<标志>, <函数>);`
```c
// 保证函数只执行一次
once_flag flag = ONCE_FLAG_INIT;
call_once(&flag, init_func);
```

---

## 信号量 C23

**基本写法：创建信号量**
`#include <semaphore.h>` `sem_t <变量>; sem_init(&<变量>, 0, <初始>);`
```c
// 计数信号量
sem_t sem;
sem_init(&sem, 0, 3);
```

---

**基本写法：等待与释放**
`sem_wait(&<sem>);` `sem_post(&<sem>);`
```c
// P 操作与 V 操作
sem_wait(&sem);
// 临界区
sem_post(&sem);
```



<!-- ============ 文档分隔线：025-c/023-POSIXThreadPthread.md ============ -->

# C POSIX 线程 pthread

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 线程创建

**基本写法：创建线程**
`pthread_create(&<线程>, [NULL], <函数>, <参数>);`
```c
// 创建新线程
pthread_t tid;
pthread_create(&tid, NULL, worker, arg);
```

---

**基本写法：线程函数签名**
`void* <函数名>(void* <参数>);`
```c
// 线程入口函数返回 void 指针
void* worker(void* arg) {
    return NULL;
}
```

---

**基本写法：等待线程**
`pthread_join(<线程>, [&<返回值>]);`
```c
// 阻塞等待线程结束
void* ret;
pthread_join(tid, &ret);
```

---

**基本写法：分离线程**
`pthread_detach(<线程>);`
```c
// 分离线程自动回收资源
pthread_detach(tid);
```

---

**基本写法：获取自身 ID**
`pthread_self();`
```c
// 当前线程 ID
pthread_t self = pthread_self();
```

---

**基本写法：比较线程 ID**
`pthread_equal(<t1>, <t2>);`
```c
// 比较两个线程是否相同
if (pthread_equal(t1, t2)) { }
```

---

**基本写法：线程退出**
`pthread_exit([<返回值>]);`
```c
// 退出当前线程
pthread_exit(NULL);
```

---

## 互斥锁

**基本写法：静态初始化**
`pthread_mutex_t <变量> = PTHREAD_MUTEX_INITIALIZER;`
```c
// 静态初始化互斥锁
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
```

---

**基本写法：动态初始化**
`pthread_mutex_init(&<锁>, [NULL]);`
```c
// 运行时初始化
pthread_mutex_init(&m, NULL);
```

---

**基本写法：加锁解锁**
`pthread_mutex_lock(&<锁>);` `pthread_mutex_unlock(&<锁>);`
```c
// 临界区保护
pthread_mutex_lock(&m);
// 临界区
pthread_mutex_unlock(&m);
```

---

**基本写法：尝试加锁**
`pthread_mutex_trylock(&<锁>);`
```c
// 非阻塞加锁
if (pthread_mutex_trylock(&m) == 0) { }
```

---

**基本写法：销毁互斥锁**
`pthread_mutex_destroy(&<锁>);`
```c
// 释放资源
pthread_mutex_destroy(&m);
```

---

## 条件变量

**基本写法：静态初始化条件变量**
`pthread_cond_t <变量> = PTHREAD_COND_INITIALIZER;`
```c
// 静态初始化
pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
```

---

**基本写法：等待条件**
`pthread_cond_wait(&<cv>, &<锁>);`
```c
// 释放锁等待唤醒
pthread_mutex_lock(&m);
while (!ready) pthread_cond_wait(&cv, &m);
pthread_mutex_unlock(&m);
```

---

**基本写法：超时等待**
`pthread_cond_timedwait(&<cv>, &<锁>, &<超时>);`
```c
// 限时等待
struct timespec ts;
pthread_cond_timedwait(&cv, &m, &ts);
```

---

**基本写法：通知一个**
`pthread_cond_signal(&<cv>);`
```c
// 唤醒一个线程
pthread_cond_signal(&cv);
```

---

**基本写法：通知所有**
`pthread_cond_broadcast(&<cv>);`
```c
// 唤醒所有线程
pthread_cond_broadcast(&cv);
```

---

## 读写锁

**基本写法：创建读写锁**
`pthread_rwlock_t <变量> = PTHREAD_RWLOCK_INITIALIZER;`
```c
// 读写锁支持多读单写
pthread_rwlock_t rw = PTHREAD_RWLOCK_INITIALIZER;
```

---

**基本写法：读锁**
`pthread_rwlock_rdlock(&<锁>);`
```c
// 共享读
pthread_rwlock_rdlock(&rw);
```

---

**基本写法：写锁**
`pthread_rwlock_wrlock(&<锁>);`
```c
// 独占写
pthread_rwlock_wrlock(&rw);
```

---

## 信号量

**基本写法：创建信号量**
`sem_t <变量>; sem_init(&<变量>, 0, <初始>);`
```c
// 初始化信号量
sem_t sem;
sem_init(&sem, 0, 1);
```

---

**基本写法：等待与释放**
`sem_wait(&<sem>);` `sem_post(&<sem>);`
```c
// P 与 V 操作
sem_wait(&sem);
// 临界区
sem_post(&sem);
```

---

**基本写法：销毁信号量**
`sem_destroy(&<sem>);`
```c
// 释放信号量资源
sem_destroy(&sem);
```

---

## 线程属性

**基本写法：设置分离状态**
`pthread_attr_setdetachstate(&<属性>, PTHREAD_CREATE_DETACHED);`
```c
// 创建即分离的线程
pthread_attr_t attr;
pthread_attr_init(&attr);
pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
pthread_create(&tid, &attr, worker, NULL);
```

---

**基本写法：编译链接**
`gcc -pthread <文件>.c -o <输出>`
```c
// 链接 pthread 库
gcc -pthread main.c -o main
```



<!-- ============ 文档分隔线：025-c/024-SignalHandling.md ============ -->

# C 信号处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 信号基础

**基本写法：发送信号**
`raise(<信号>);`
```c
// 向自身发送信号
raise(SIGINT);
```

---

**基本写法：向进程发送信号**
`kill(<pid>, <信号>);`
```c
// 给指定进程发信号
kill(pid, SIGTERM);
```

---

## 注册信号处理函数

**基本写法：signal 注册**
`signal(<信号>, <处理函数>);`
```c
// 简单注册信号处理
signal(SIGINT, handler);
```

---

**基本写法：信号处理函数签名**
`void <函数名>(int <信号>);`
```c
// 信号处理函数原型
void handler(int sig) {
    // 仅调用异步信号安全函数
}
```

---

**基本写法：忽略信号**
`signal(<信号>, SIG_IGN);`
```c
// 忽略指定信号
signal(SIGINT, SIG_IGN);
```

---

**基本写法：恢复默认处理**
`signal(<信号>, SIG_DFL);`
```c
// 恢复默认行为
signal(SIGINT, SIG_DFL);
```

---

## sigaction

**基本写法：sigaction 注册**
`sigaction(<信号>, &<新动作>, [NULL]);`
```c
// 更健壮的信号注册方式
struct sigaction sa;
sa.sa_handler = handler;
sigemptyset(&sa.sa_mask);
sa.sa_flags = 0;
sigaction(SIGINT, &sa, NULL);
```

---

**基本写法：设置 sa_flags**
`<sa>.sa_flags = SA_RESTART;`
```c
// 被中断系统调用自动重启
sa.sa_flags = SA_RESTART;
```

---

**基本写法：获取旧动作**
`sigaction(<信号>, &<新动作>, &<旧动作>);`
```c
// 保存原有处理方式
struct sigaction oldsa;
sigaction(SIGINT, &sa, &oldsa);
```

---

## 信号集

**基本写法：初始化空信号集**
`sigemptyset(&<集合>);`
```c
// 清空信号集
sigset_t set;
sigemptyset(&set);
```

---

**基本写法：添加信号**
`sigaddset(&<集合>, <信号>);`
```c
// 向集合添加信号
sigaddset(&set, SIGINT);
```

---

**基本写法：填充所有信号**
`sigfillset(&<集合>);`
```c
// 集合包含所有信号
sigfillset(&set);
```

---

**基本写法：删除信号**
`sigdelset(&<集合>, <信号>);`
```c
// 从集合删除信号
sigdelset(&set, SIGINT);
```

---

**基本写法：判断信号是否在集合**
`sigismember(&<集合>, <信号>);`
```c
// 检查信号是否属于集合
if (sigismember(&set, SIGINT)) { }
```

---

## 信号屏蔽

**基本写法：设置屏蔽字**
`sigprocmask(<how>, &<集合>, [NULL]);`
```c
// 阻塞指定信号
sigset_t set;
sigemptyset(&set);
sigaddset(&set, SIGINT);
sigprocmask(SIG_BLOCK, &set, NULL);
```

---

**基本写法：解除屏蔽**
`sigprocmask(SIG_UNBLOCK, &<集合>, NULL);`
```c
// 解除信号阻塞
sigprocmask(SIG_UNBLOCK, &set, NULL);
```

---

**基本写法：获取未决信号**
`sigpending(&<集合>);`
```c
// 查询被阻塞的未决信号
sigset_t pending;
sigpending(&pending);
```

---

## 等待信号

**基本写法：暂停等待信号**
`pause();`
```c
// 挂起直到收到任意信号
pause();
```

---

**基本写法：sigsuspend 等待**
`sigsuspend(&<临时集合>);`
```c
// 原子替换屏蔽字并等待
sigset_t empty;
sigemptyset(&empty);
sigsuspend(&empty);
```

---

## 常用信号

**基本写法：终止信号**
`SIGTERM` / `SIGKILL`
```c
// SIGTERM 可捕获 SIGKILL 不可捕获
kill(pid, SIGTERM);
```

---

**基本写法：中断信号**
`SIGINT`
```c
// Ctrl+C 产生
signal(SIGINT, handler);
```

---

**基本写法：闹钟信号**
`alarm(<秒数>);`
```c
// 定时发送 SIGALRM
alarm(5);
```

---

**基本写法：子进程状态变化**
`SIGCHLD`
```c
// 子进程结束时发送
signal(SIGCHLD, handler);
```

---

## 异步信号安全

**基本写法：可重入处理函数**
`void <handler>(int <sig>) { write(STDERR_FILENO, "sig", 3); }`
```c
// 仅调用 write 等异步信号安全函数
void handler(int sig) {
    write(2, "interrupt\n", 10);
}
```

---

**基本写法：自管道技巧**
`write(<管道写端>, &<sig>, sizeof(int));`
```c
// 信号处理仅写管道主循环读取处理
void handler(int sig) {
    write(pipefd[1], &sig, sizeof(sig));
}
```



<!-- ============ 文档分隔线：025-c/025-ProcessAndPipe.md ============ -->

# C 进程与管道

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 进程创建

**基本写法：创建子进程**
`fork();`
```c
// 创建当前进程的副本
pid_t pid = fork();
```

---

**基本写法：区分父子进程**
`if (<pid> == 0) { /* 子进程 */ } else { /* 父进程 */ }`
```c
// 通过返回值区分
pid_t pid = fork();
if (pid == 0) {
    // 子进程代码
} else if (pid > 0) {
    // 父进程代码
}
```

---

**基本写法：替换进程映像**
`execlp(<程序>, <参数0>, ..., NULL);`
```c
// 用新程序替换当前进程
execlp("ls", "ls", "-l", NULL);
```

---

**基本写法：execv 系列**
`execv(<路径>, <参数数组>);`
```c
// 使用数组传参
char* args[] = {"ls", "-l", NULL};
execv("/bin/ls", args);
```

---

**基本写法：fork + exec 组合**
`fork(); execlp(...);`
```c
// 子进程执行新程序
pid_t pid = fork();
if (pid == 0) {
    execlp("echo", "echo", "hi", NULL);
    _exit(1);
}
```

---

## 等待进程

**基本写法：等待任意子进程**
`wait(&<状态>);`
```c
// 阻塞等待子进程结束
int status;
wait(&status);
```

---

**基本写法：等待指定子进程**
`waitpid(<pid>, &<状态>, 0);`
```c
// 等待特定子进程
int status;
waitpid(pid, &status, 0);
```

---

**基本写法：非阻塞等待**
`waitpid(<pid>, &<状态>, WNOHANG);`
```c
// 立即返回不阻塞
int r = waitpid(pid, &status, WNOHANG);
```

---

**基本写法：检查退出码**
`WEXITSTATUS(<状态>);`
```c
// 取出子进程退出值
if (WIFEXITED(status)) {
    int code = WEXITSTATUS(status);
}
```

---

**基本写法：获取自身 PID**
`getpid();`
```c
// 当前进程 ID
pid_t self = getpid();
```

---

**基本写法：获取父进程 PID**
`getppid();`
```c
// 父进程 ID
pid_t parent = getppid();
```

---

## 进程退出

**基本写法：正常退出**
`exit(<状态码>);`
```c
// 调用注册的清理函数后退出
exit(0);
```

---

**基本写法：立即退出**
`_exit(<状态码>);`
```c
// 不执行 atexit 注册函数直接退出
_exit(1);
```

---

**基本写法：注册退出函数**
`atexit(<函数>);`
```c
// 注册程序退出时调用的函数
atexit(cleanup);
```

---

## 管道

**基本写法：创建匿名管道**
`pipe(<int[2]>);`
```c
// 创建一对读写描述符
int fd[2];
pipe(fd);
```

---

**基本写法：父子进程通信**
`pipe(fd); fork();`
```c
// 父进程写子进程读
int fd[2];
pipe(fd);
pid_t pid = fork();
if (pid == 0) {
    close(fd[1]);       // 子进程关闭写端
    read(fd[0], buf, n);
} else {
    close(fd[0]);       // 父进程关闭读端
    write(fd[1], buf, n);
}
```

---

**基本写法：写管道**
`write(<写端>, <数据>, <大小>);`
```c
// 向管道写入数据
write(fd[1], data, sizeof(data));
```

---

**基本写法：读管道**
`read(<读端>, <缓冲>, <大小>);`
```c
// 从管道读取数据
ssize_t n = read(fd[0], buf, sizeof(buf));
```

---

## popen

**基本写法：执行命令并获取输出**
`popen(<命令>, "r");`
```c
// 通过管道读取命令输出
FILE* fp = popen("ls -l", "r");
```

---

**基本写法：读取命令输出**
`fgets(<缓冲>, <大小>, <fp>);`
```c
// 逐行读取
char line[256];
while (fgets(line, sizeof(line), fp)) { }
```

---

**基本写法：关闭 popen**
`pclose(<fp>);`
```c
// 关闭并等待命令结束
pclose(fp);
```

---

## 命名管道 FIFO

**基本写法：创建 FIFO**
`mkfifo(<路径>, <权限>);`
```c
// 创建命名管道文件
mkfifo("/tmp/myfifo", 0666);
```

---

**基本写法：打开 FIFO**
`open(<路径>, <标志>);`
```c
// 以读写方式打开
int fd = open("/tmp/myfifo", O_RDWR);
```

---

**基本写法：删除 FIFO**
`unlink(<路径>);`
```c
// 删除管道文件
unlink("/tmp/myfifo");
```

---

## 环境变量

**基本写法：获取环境变量**
`getenv(<名称>);`
```c
// 读取环境变量值
char* path = getenv("PATH");
```

---

**基本写法：设置环境变量**
`setenv(<名称>, <值>, 1);`
```c
// 设置或覆盖环境变量
setenv("MY_VAR", "1", 1);
```

---

**基本写法：删除环境变量**
`unsetenv(<名称>);`
```c
// 删除环境变量
unsetenv("MY_VAR");
```



<!-- ============ 文档分隔线：025-c/026-SharedMemorySemaphore.md ============ -->

# C 共享内存与信号量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## System V 共享内存

**基本写法：创建共享内存**
`shmget(<键>, <大小>, IPC_CREAT | 0666);`
```c
// 创建共享内存段
int shmid = shmget(IPC_PRIVATE, 4096, IPC_CREAT | 0666);
```

---

**基本写法：附加共享内存**
`shmat(<shmid>, NULL, 0);`
```c
// 将共享内存映射到进程地址空间
void* addr = shmat(shmid, NULL, 0);
```

---

**基本写法：分离共享内存**
`shmdt(<地址>);`
```c
// 解除映射但不删除
shmdt(addr);
```

---

**基本写法：删除共享内存**
`shmctl(<shmid>, IPC_RMID, NULL);`
```c
// 标记删除等所有进程分离后回收
shmctl(shmid, IPC_RMID, NULL);
```

---

**基本写法：生成键**
`ftok(<路径>, <项目ID>);`
```c
// 通过文件路径生成键
key_t key = ftok("/tmp/shm", 'A');
```

---

## POSIX 共享内存

**基本写法：创建共享内存对象**
`shm_open(<名称>, O_CREAT | O_RDWR, 0666);`
```c
// 创建 POSIX 共享内存
int fd = shm_open("/myshm", O_CREAT | O_RDWR, 0666);
```

---

**基本写法：设置大小**
`ftruncate(<fd>, <大小>);`
```c
// 设置共享内存大小
ftruncate(fd, 4096);
```

---

**基本写法：映射内存**
`mmap(NULL, <大小>, PROT_READ | PROT_WRITE, MAP_SHARED, <fd>, 0);`
```c
// 映射到地址空间
void* addr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
```

---

**基本写法：解除映射**
`munmap(<地址>, <大小>);`
```c
// 解除映射
munmap(addr, 4096);
```

---

**基本写法：关闭与删除**
`close(<fd>); shm_unlink(<名称>);`
```c
// 关闭并删除共享内存对象
close(fd);
shm_unlink("/myshm");
```

---

## mmap 文件映射

**基本写法：映射文件**
`mmap(NULL, <大小>, <保护>, MAP_SHARED, <fd>, 0);`
```c
// 将文件映射到内存
int fd = open("data.bin", O_RDWR);
void* addr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
```

---

**基本写法：同步到磁盘**
`msync(<地址>, <大小>, MS_SYNC);`
```c
// 将修改刷回文件
msync(addr, 4096, MS_SYNC);
```

---

## System V 信号量

**基本写法：创建信号量集**
`semget(<键>, <数量>, IPC_CREAT | 0666);`
```c
// 创建包含 1 个信号量的集合
int semid = semget(key, 1, IPC_CREAT | 0666);
```

---

**基本写法：初始化信号量**
`semctl(<semid>, 0, SETVAL, <值>);`
```c
// 设置初值
semctl(semid, 0, SETVAL, 1);
```

---

**基本写法：PV 操作**
`struct sembuf <op> = {0, -1, 0}; semop(<semid>, &<op>, 1);`
```c
// P 操作减 1
struct sembuf p = {0, -1, 0};
semop(semid, &p, 1);
// V 操作加 1
struct sembuf v = {0, 1, 0};
semop(semid, &v, 1);
```

---

**基本写法：删除信号量集**
`semctl(<semid>, 0, IPC_RMID);`
```c
// 删除信号量集
semctl(semid, 0, IPC_RMID);
```

---

## POSIX 信号量

**基本写法：创建命名信号量**
`sem_open(<名称>, O_CREAT, 0666, <初始>);`
```c
// 创建命名信号量
sem_t* sem = sem_open("/mysem", O_CREAT, 0666, 1);
```

---

**基本写法：等待与释放**
`sem_wait(<sem>);` `sem_post(<sem>);`
```c
// P 与 V 操作
sem_wait(sem);
// 临界区
sem_post(sem);
```

---

**基本写法：关闭与删除**
`sem_close(<sem>);` `sem_unlink(<名称>);`
```c
// 关闭并删除命名信号量
sem_close(sem);
sem_unlink("/mysem");
```

---

**基本写法：无名信号量**
`sem_t <变量>; sem_init(&<变量>, 1, <初始>);`
```c
// 用于共享内存的无名信号量
sem_t sem;
sem_init(&sem, 1, 1);
```

---

## 消息队列

**基本写法：创建消息队列**
`msgget(<键>, IPC_CREAT | 0666);`
```c
// 创建 System V 消息队列
int msqid = msgget(key, IPC_CREAT | 0666);
```

---

**基本写法：发送消息**
`msgsnd(<msqid>, &<消息>, <数据大小>, 0);`
```c
// 发送消息
struct Msg { long type; char data[100]; } msg;
msgsnd(msqid, &msg, sizeof(msg.data), 0);
```

---

**基本写法：接收消息**
`msgrcv(<msqid>, &<消息>, <大小>, <类型>, 0);`
```c
// 接收指定类型消息
msgrcv(msqid, &msg, sizeof(msg.data), 1, 0);
```

---

**基本写法：删除消息队列**
`msgctl(<msqid>, IPC_RMID, NULL);`
```c
// 删除消息队列
msgctl(msqid, IPC_RMID, NULL);
```



<!-- ============ 文档分隔线：025-c/027-SocketNetworkProgramming.md ============ -->

# C Socket 网络编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Socket

**基本写法：创建 TCP socket**
`socket(AF_INET, SOCK_STREAM, 0);`
```c
// 创建 IPv4 TCP 套接字
int fd = socket(AF_INET, SOCK_STREAM, 0);
```

---

**基本写法：创建 UDP socket**
`socket(AF_INET, SOCK_DGRAM, 0);`
```c
// 创建 IPv4 UDP 套接字
int fd = socket(AF_INET, SOCK_DGRAM, 0);
```

---

**基本写法：创建本地 socket**
`socket(AF_UNIX, SOCK_STREAM, 0);`
```c
// 创建 Unix 域套接字
int fd = socket(AF_UNIX, SOCK_STREAM, 0);
```

---

## 地址结构

**基本写法：IPv4 地址结构**
`struct sockaddr_in <变量>;`
```c
// 初始化服务器地址
struct sockaddr_in addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.s_addr = INADDR_ANY;
```

---

**基本写法：字符串转地址**
`inet_pton(AF_INET, <IP串>, &<地址>);`
```c
// 将点分十进制转为二进制
inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);
```

---

**基本写法：地址转字符串**
`inet_ntop(AF_INET, &<地址>, <缓冲>, <大小>);`
```c
// 二进制地址转可读字符串
char ip[INET_ADDRSTRLEN];
inet_ntop(AF_INET, &addr.sin_addr, ip, sizeof(ip));
```

---

## 服务端流程

**基本写法：绑定地址**
`bind(<fd>, (struct sockaddr*)&<地址>, sizeof(<地址>));`
```c
// 绑定本地地址端口
bind(fd, (struct sockaddr*)&addr, sizeof(addr));
```

---

**基本写法：监听连接**
`listen(<fd>, <队列长度>);`
```c
// 开始监听客户端连接
listen(fd, 5);
```

---

**基本写法：接受连接**
`accept(<fd>, (struct sockaddr*)&<客户端地址>, &<长度>);`
```c
// 接受新连接返回新描述符
struct sockaddr_in cli;
socklen_t len = sizeof(cli);
int cfd = accept(fd, (struct sockaddr*)&cli, &len);
```

---

## 客户端流程

**基本写法：连接服务器**
`connect(<fd>, (struct sockaddr*)&<服务器地址>, sizeof(<地址>));`
```c
// 主动连接服务器
connect(fd, (struct sockaddr*)&srv, sizeof(srv));
```

---

## 数据收发

**基本写法：发送数据**
`send(<fd>, <数据>, <大小>, 0);`
```c
// TCP 发送数据
send(fd, buf, n, 0);
```

---

**基本写法：接收数据**
`recv(<fd>, <缓冲>, <大小>, 0);`
```c
// TCP 接收数据
ssize_t n = recv(fd, buf, sizeof(buf), 0);
```

---

**基本写法：UDP 发送**
`sendto(<fd>, <数据>, <大小>, 0, (struct sockaddr*)&<目标>, sizeof(<目标>));`
```c
// UDP 发送数据到指定地址
sendto(fd, buf, n, 0, (struct sockaddr*)&dst, sizeof(dst));
```

---

**基本写法：UDP 接收**
`recvfrom(<fd>, <缓冲>, <大小>, 0, (struct sockaddr*)&<来源>, &<长度>);`
```c
// UDP 接收数据并获取来源
struct sockaddr_in src;
socklen_t len = sizeof(src);
recvfrom(fd, buf, sizeof(buf), 0, (struct sockaddr*)&src, &len);
```

---

## Socket 选项

**基本写法：设置地址复用**
`setsockopt(<fd>, SOL_SOCKET, SO_REUSEADDR, &<值>, sizeof(<值>));`
```c
// 避免地址占用错误
int opt = 1;
setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
```

---

**基本写法：设置接收超时**
`setsockopt(<fd>, SOL_SOCKET, SO_RCVTIMEO, &<时长>, sizeof(<时长>));`
```c
// 设置接收超时
struct timeval tv = {5, 0};
setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
```

---

## I/O 多路复用

**基本写法：select 等待**
`select(<最大fd+1>, &<读集>, NULL, NULL, &<超时>);`
```c
// 监视多个描述符
fd_set rfds;
FD_ZERO(&rfds);
FD_SET(fd, &rfds);
struct timeval tv = {5, 0};
select(fd + 1, &rfds, NULL, NULL, &tv);
```

---

**基本写法：poll 等待**
`poll(<数组>, <数量>, <超时毫秒>);`
```c
// 使用 poll 监视
struct pollfd fds[1];
fds[0].fd = fd;
fds[0].events = POLLIN;
poll(fds, 1, 5000);
```

---

**基本写法：epoll 创建**
`epoll_create1(0);`
```c
// Linux 高效多路复用
int epfd = epoll_create1(0);
```

---

**基本写法：epoll 注册**
`epoll_ctl(<epfd>, EPOLL_CTL_ADD, <fd>, &<事件>);`
```c
// 添加描述符到 epoll
struct epoll_event ev;
ev.events = EPOLLIN;
ev.data.fd = fd;
epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &ev);
```

---

**基本写法：epoll 等待**
`epoll_wait(<epfd>, <事件数组>, <最大数>, <超时>);`
```c
// 等待事件发生
struct epoll_event events[10];
int n = epoll_wait(epfd, events, 10, -1);
```

---

## 关闭 Socket

**基本写法：关闭描述符**
`close(<fd>);`
```c
// 关闭并释放资源
close(fd);
```

---

**基本写法：优雅关闭**
`shutdown(<fd>, SHUT_WR);`
```c
// 单向关闭写端
shutdown(fd, SHUT_WR);
```

---

## 主机与服务查询

**基本写法：获取主机信息**
`getaddrinfo(<主机>, <服务>, &<提示>, &<结果>);`
```c
// 现代地址查询接口
struct addrinfo hints = {0};
hints.ai_family = AF_INET;
hints.ai_socktype = SOCK_STREAM;
struct addrinfo* res;
getaddrinfo("example.com", "80", &hints, &res);
```

---

**基本写法：释放结果**
`freeaddrinfo(<结果>);`
```c
// 释放 getaddrinfo 结果
freeaddrinfo(res);
```



<!-- ============ 文档分隔线：025-c/028-FileSystemOperation.md ============ -->

# C 文件系统操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件信息

**基本写法：获取文件状态**
`stat(<路径>, &<结构>);`
```c
// 获取文件元数据
struct stat st;
stat("file.txt", &st);
```

---

**基本写法：获取文件大小**
`<st>.st_size`
```c
// 取出文件字节数
off_t size = st.st_size;
```

---

**基本写法：判断是否目录**
`S_ISDIR(<st>.st_mode)`
```c
// 检查是否为目录
if (S_ISDIR(st.st_mode)) { }
```

---

**基本写法：判断是否普通文件**
`S_ISREG(<st>.st_mode)`
```c
// 检查是否为普通文件
if (S_ISREG(st.st_mode)) { }
```

---

**基本写法：获取文件权限**
`<st>.st_mode & 0777`
```c
// 取出权限位
mode_t perm = st.st_mode & 0777;
```

---

**基本写法：获取修改时间**
`<st>.st_mtime`
```c
// 文件最后修改时间戳
time_t mtime = st.st_mtime;
```

---

## 目录操作

**基本写法：创建目录**
`mkdir(<路径>, <权限>);`
```c
// 创建目录
mkdir("newdir", 0755);
```

---

**基本写法：删除目录**
`rmdir(<路径>);`
```c
// 删除空目录
rmdir("newdir");
```

---

**基本写法：打开目录**
`opendir(<路径>);`
```c
// 打开目录流
DIR* dir = opendir(".");
```

---

**基本写法：读取目录项**
`readdir(<dir>);`
```c
// 逐个读取目录项
struct dirent* entry;
while ((entry = readdir(dir)) != NULL) {
    printf("%s\n", entry->d_name);
}
```

---

**基本写法：关闭目录**
`closedir(<dir>);`
```c
// 关闭目录流
closedir(dir);
```

---

**基本写法：切换工作目录**
`chdir(<路径>);`
```c
// 改变当前工作目录
chdir("/tmp");
```

---

**基本写法：获取工作目录**
`getcwd(<缓冲>, <大小>);`
```c
// 取得当前工作目录
char buf[256];
getcwd(buf, sizeof(buf));
```

---

## 文件操作

**基本写法：创建文件**
`creat(<路径>, <权限>);`
```c
// 创建或截断文件
int fd = creat("file.txt", 0644);
```

---

**基本写法：删除文件**
`unlink(<路径>);`
```c
// 删除文件
unlink("file.txt");
```

---

**基本写法：重命名**
`rename(<旧名>, <新名>);`
```c
// 重命名或移动文件
rename("old.txt", "new.txt");
```

---

**基本写法：链接文件**
`link(<原路径>, <新路径>);`
```c
// 创建硬链接
link("file.txt", "hardlink.txt");
```

---

**基本写法：符号链接**
`symlink(<目标>, <链接名>);`
```c
// 创建软链接
symlink("file.txt", "softlink.txt");
```

---

**基本写法：读取符号链接**
`readlink(<链接>, <缓冲>, <大小>);`
```c
// 读取链接指向的目标
char buf[256];
ssize_t n = readlink("softlink.txt", buf, sizeof(buf));
buf[n] = '\0';
```

---

## 权限与所有者

**基本写法：修改权限**
`chmod(<路径>, <权限>);`
```c
// 修改文件权限
chmod("file.txt", 0644);
```

---

**基本写法：修改所有者**
`chown(<路径>, <uid>, <gid>);`
```c
// 修改文件所有者
chown("file.txt", 1000, 1000);
```

---

**基本写法：修改文件描述符权限**
`fchmod(<fd>, <权限>);`
```c
// 通过描述符修改权限
fchmod(fd, 0644);
```

---

## 文件描述符操作

**基本写法：复制描述符**
`dup(<fd>);` / `dup2(<fd>, <新fd>);`
```c
// 重定向到指定描述符
dup2(fd, STDOUT_FILENO);
```

---

**基本写法：打开文件**
`open(<路径>, <标志>);`
```c
// 读写方式打开
int fd = open("file.txt", O_RDWR | O_CREAT, 0644);
```

---

**基本写法：读写**
`read(<fd>, <缓冲>, <大小>);` `write(<fd>, <数据>, <大小>);`
```c
// 底层读写
ssize_t n = read(fd, buf, sizeof(buf));
write(fd, buf, n);
```

---

**基本写法：定位文件偏移**
`lseek(<fd>, <偏移>, <起始>);`
```c
// 移动文件读写位置
lseek(fd, 0, SEEK_SET);   // 回到开头
```

---

**基本写法：关闭描述符**
`close(<fd>);`
```c
// 关闭文件描述符
close(fd);
```

---

## 遍历目录树

**基本写法：递归遍历目录**
`nftw(<路径>, <回调>, <深度>, <标志>);`
```c
// 文件树遍历
int cb(const char* path, const struct stat* st, int type, struct FTW* ftw) {
    if (type == FTW_F) printf("%s\n", path);
    return 0;
}
nftw(".", cb, 10, FTW_PHYS);
```

---

## glob 模式匹配

**基本写法：通配符匹配文件**
`glob(<模式>, 0, NULL, &<结果>);`
```c
// 匹配所有 .txt 文件
glob_t g;
glob("*.txt", 0, NULL, &g);
for (size_t i = 0; i < g.gl_pathc; i++) {
    printf("%s\n", g.gl_pathv[i]);
}
globfree(&g);
```

---

## 临时文件

**基本写法：创建临时文件**
`tmpfile();`
```c
// 创建自动删除的临时文件
FILE* fp = tmpfile();
```

---

**基本写法：生成临时文件名**
`mkstemp(<模板>);`
```c
// 安全创建临时文件
char tmpl[] = "/tmp/myfileXXXXXX";
int fd = mkstemp(tmpl);
```



<!-- ============ 文档分隔线：025-c/029-DynamicStaticLibrary.md ============ -->

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



<!-- ============ 文档分隔线：025-c/030-C23NewFeatures.md ============ -->

# C23 新特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## nullptr

**基本写法：空指针常量**
`nullptr`
```c
// C23 类型安全的空指针
int* p = nullptr;
```

---

**基本写法：空指针类型**
`nullptr_t`
```c
// 空指针类型定义
nullptr_t np = nullptr;
```

---

**基本写法：与 NULL 区别**
`f(nullptr)` 不可隐式转整型
```c
// nullptr 仅能转指针避免歧义
void f(void* p);
f(nullptr);   // 明确传入空指针
```

---

## auto 类型推断

**基本写法：自动类型推导**
`auto <变量> = <表达式>;`
```c
// 编译器推导变量类型
auto x = 42;       // int
auto y = 3.14;     // double
```

---

**基本写法：复杂类型推断**
`auto <迭代器> = <表达式>;`
```c
// 简化复杂类型书写
struct Config* c = load_config();
auto cfg = load_config();
```

---

**基本写法：auto 限制**
`auto <变量>;  // 错误必须初始化`
```c
// auto 必须有初始化器
auto x = 10;   // 正确
// auto y;     // 错误
```

---

## constexpr

**基本写法：编译期常量**
`constexpr <类型> <变量> = <常量表达式>;`
```c
// 真正的编译期常量
constexpr int size = 10;
int arr[size];   // 合法
```

---

**基本写法：与 const 区别**
`const int n = <值>;  // 非编译期`
```c
// constexpr 可用于数组维度与 case 标签
constexpr int max = 100;
switch (x) { case max: break; }
```

---

**基本写法：constexpr 函数**
`constexpr int <函数名>(<参数>) { }`
```c
// 编译期可求值函数
constexpr int square(int x) { return x * x; }
int arr[square(5)];
```

---

## typeof / typeof_unqual

**基本写法：获取表达式类型**
`typeof(<表达式>) <变量> = <值>;`
```c
// 取表达式的类型声明变量
int a = 0;
typeof(a) b = 1;
```

---

**基本写法：去限定类型**
`typeof_unqual(<表达式>) <变量>;`
```c
// 去除 const volatile 限定
const int ci = 0;
typeof_unqual(ci) cu = 1;   // int
```

---

**基本写法：typeof 用于宏**
`#define SWAP(a, b) { typeof(a) tmp = a; a = b; b = tmp; }`
```c
// 通用交换宏
#define SWAP(a, b) do { \
    typeof(a) tmp = (a); \
    (a) = (b); \
    (b) = tmp; \
} while (0)
```

---

## 二进制字面量

**基本写法：二进制常量**
`0b<二进制>`
```c
// C23 支持二进制字面量
int mask = 0b10101010;
```

---

**基本写法：数字分隔符**
`<数字>'<数字>`
```c
// 提高数字可读性
int big = 1'000'000;
int bin = 0b1010'1010;
```

---

## bool 成为关键字

**基本写法：直接使用 bool**
`bool <变量> = true;`
```c
// C23 不再需要 stdbool.h
bool ready = true;
if (!ready) { }
```

---

**基本写法：true 与 false**
`true` / `false`
```c
// 直接使用布尔字面量
bool flag = false;
flag = (x > 0);
```

---

## 位精确整数

**基本写法：声明位宽整数**
`_BitInt(<位数>) <变量>;`
```c
// 指定精确位宽的整数
_BitInt(32) a = 100;
unsigned _BitInt(8) b = 200;
```

---

**基本写法：检查整数运算**
`ckd_add(&<结果>, <a>, <b>);`
```c
// C23 检查溢出的运算
_BitInt(32) r;
if (ckd_add(&r, a, b)) {
    // 发生溢出
}
```

---

## 标准属性

**基本写法：nodiscard 属性**
`[[nodiscard]] <返回类型> <函数>();`
```c
// 提示返回值不应被忽略
[[nodiscard]] int compute(void);
```

---

**基本写法：deprecated 属性**
`[[deprecated("[<消息>]")]] <声明>`
```c
// 标记弃用的函数
[[deprecated("use new_func")]]
void old_func(void);
```

---

**基本写法：maybe_unused 属性**
`[[maybe_unused]] <声明>`
```c
// 抑制未使用警告
[[maybe_unused]] static int x;
```

---

**基本写法：fallthrough 属性**
`[[fallthrough]];`
```c
// 标注 switch 故意穿透
switch (x) {
case 1:
    do_a();
    [[fallthrough]];
case 2:
    do_b();
    break;
}
```

---

## 预处理器新指令

**基本写法：#warning**
`#warning "<消息>"`
```c
// 产生编译警告
#warning "此功能尚未稳定"
```

---

**基本写法：#elifdef**
`#elifdef <宏>`
```c
// 等价 #elif defined
#ifdef A
#elifdef B
#endif
```

---

**基本写法：#elifndef**
`#elifndef <宏>`
```c
// 等价 #elif !defined
#ifdef A
#elifndef B
#endif
```

---

## #embed 嵌入二进制

**基本写法：嵌入文件**
`#embed <文件路径>`
```c
// 将文件内容作为字节数组
const unsigned char data[] = {
    #embed "logo.png"
};
```

---

**基本写法：限制嵌入大小**
`#embed <文件> limit(<字节数>)`
```c
// 仅嵌入前 N 字节
const unsigned char head[] = {
    #embed "data.bin" limit(16)
};
```

---

## stdbit.h 位操作

**基本写法：统计 1 的个数**
`stdc_count_ones(<值>)`
```c
// C23 标准位计数函数
unsigned n = stdc_count_ones(0xFFu);   // 8
```

---

**基本写法：统计前导零**
`stdc_leading_zeros(<值>)`
```c
// 前导零数量
unsigned z = stdc_leading_zeros(1u);
```

---

**基本写法：统计末尾零**
`stdc_trailing_zeros(<值>)`
```c
// 末尾零数量
unsigned z = stdc_trailing_zeros(8u);   // 3
```

---

**基本写法：位宽**
`stdc_bit_width(<值>)`
```c
// 表示该数所需位数
unsigned w = stdc_bit_width(255u);   // 8
```

---

## 初始化改进

**基本写法：空初始化**
`<类型> <变量> = {};`
```c
// C23 零初始化简写
int arr[10] = {};
struct Point p = {};
```

---

**基本写法：复合字面量改进**
`(<类型>){<成员>}`
```c
// 复合字面量可用于更多场景
struct Point* p = &(struct Point){1, 2};
```

---

## 编译选项

**基本写法：启用 C23**
`gcc -std=c23 <文件>.c`
```c
// 编译 C23 标准
gcc -std=c23 main.c -o main
```

---

**基本写法：检查 C23 版本**
`__STDC_VERSION__`
```c
// 查看标准版本宏
#if __STDC_VERSION__ >= 202311L
    /* C23 特性 */
#endif
```



<!-- ============ 文档分隔线：025-c/031-CBuildSystem.md ============ -->

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



<!-- ============ 文档分隔线：025-c/032-CCompilerOptions.md ============ -->

# C 编译器命令 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本编译命令

**基本写法：编译为可执行文件**
`gcc <源文件> -o <输出>`
```bash
# 编译 main.c 为 app 可执行文件
gcc main.c -o app
```

**基本写法：仅编译不链接**
`gcc -c <源文件>`
```bash
# 生成目标文件 main.o
gcc -c main.c
```

**基本写法：指定 C 标准**
`gcc -std=<标准> <源文件>`
```bash
# 常用标准：c99 c11 c17 c23
gcc -std=c11 main.c -o app
```

**基本写法：clang 替代 gcc**
`clang <源文件> -o <输出>`
```bash
# clang 命令行与 gcc 基本兼容
clang -std=c11 main.c -o app
```

**基本写法：指定输出名**
`gcc <源文件> -o <输出路径>`
```bash
# -o 指定输出文件路径
gcc main.c utils.c -o bin/app
```

---

## 警告与错误

**基本写法：开启全部警告**
`gcc -Wall <源文件>`
```bash
# 启用常见警告
gcc -Wall main.c -o app
```

**基本写法：额外警告**
`gcc -Wextra <源文件>`
```bash
# 在 -Wall 基础上启用更多警告
gcc -Wall -Wextra main.c -o app
```

**基本写法：警告转为错误**
`gcc -Werror <源文件>`
```bash
# 将所有警告视为编译错误
gcc -Wall -Werror main.c -o app
```

**基本写法：特定警告开关**
`gcc -W<警告名> / -Wno-<警告名>`
```bash
# -W<name> 开启 -Wno-<name> 关闭
gcc -Wunused -Wno-unused-parameter main.c
```

**基本写法：格式字符串检查**
`gcc -Wformat -Wformat-security`
```bash
# 检查 printf/scanf 格式串安全性
gcc -Wformat -Wformat-security main.c
```

---

## 优化选项

**基本写法：优化级别**
`gcc -O<级别> <源文件>`
```bash
# 0 不优化 1 2 3 逐步加强 s 减小体积 g 调试友好
gcc -O2 main.c -o app
```

**基本写法：调试信息**
`gcc -g <源文件>`
```bash
# 生成 DWARF 调试信息，供 gdb 使用
gcc -g -O0 main.c -o app
```

**基本写法：分级调试信息**
`gcc -g<级别> <源文件>`
```bash
# g1 最少 g2 默认 g3 包含宏定义
gcc -g3 main.c -o app
```

**基本写法：链接时优化**
`gcc -flto <源文件>`
```bash
# 跨编译单元链接时优化
gcc -O2 -flto main.c utils.c -o app
```

**基本写法：目标架构优化**
`gcc -march=<架构> <源文件>`
```bash
# 针对特定 CPU 架构优化
gcc -march=native main.c -o app
```

---

## 预处理选项

**基本写法：定义宏**
`gcc -D<名称>[=<值>] <源文件>`
```bash
# 编译期定义宏，不带值默认为 1
gcc -DDEBUG -DVERSION=2 main.c
```

**基本写法：取消宏定义**
`gcc -U<名称> <源文件>`
```bash
# 取消已定义的宏
gcc -UDEBUG main.c
```

**基本写法：添加包含目录**
`gcc -I<目录> <源文件>`
```bash
# 添加头文件搜索路径
gcc -I./include -I./src main.c
```

**基本写法：仅预处理**
`gcc -E <源文件>`
```bash
# 输出预处理后的源码到 stdout
gcc -E main.c
```

**基本写法：生成依赖关系**
`gcc -M <源文件> / gcc -MM <源文件>`
```bash
# 输出 Makefile 依赖，-MM 忽略系统头文件
gcc -MM main.c
```

**基本写法：输出到文件**
`gcc -E <源文件> -o <输出>`
```bash
# 预处理结果写入文件
gcc -E main.c -o main.i
```

---

## 链接选项

**基本写法：链接库**
`gcc <源文件> -l<库名>`
```bash
# 链接 lib<name>.so 或 lib<name>.a
gcc main.c -lm -lpthread
```

**基本写法：库搜索目录**
`gcc -L<目录> <源文件> -l<库>`
```bash
# 添加库文件搜索路径
gcc -L./lib main.c -lmylib
```

**基本写法：静态链接指定库**
`gcc -Wl,-Bstatic -l<库> -Wl,-Bdynamic`
```bash
# 强制静态链接某库后恢复动态链接
gcc main.c -Wl,-Bstatic -lmylib -Wl,-Bdynamic
```

**基本写法：完全静态链接**
`gcc -static <源文件>`
```bash
# 生成不依赖动态库的可执行文件
gcc -static main.c -o app
```

**基本写法：共享库名**
`gcc -Wl,-soname,<名称> -shared -o <库>`
```bash
# 生成带 SONAME 的动态库
gcc -shared -Wl,-soname,libmy.so.1 -o libmy.so.1.0 my.c
```

**基本写法：运行时库路径**
`gcc -Wl,-rpath,<目录> <源文件>`
```bash
# 写入可执行文件运行时搜索路径
gcc -Wl,-rpath,./lib main.c -lmylib
```

---

## 输出与文件类型

**基本写法：生成汇编**
`gcc -S <源文件>`
```bash
# 生成 .s 汇编文件不汇编
gcc -S main.c
```

**基本写法：生成动态库**
`gcc -shared -fPIC <源文件> -o <库>`
```bash
# -fPIC 生成位置无关代码，-shared 生成动态库
gcc -fPIC -shared mylib.c -o libmy.so
```

**基本写法：位置无关代码**
`gcc -fPIC -c <源文件>`
```bash
# 编译为位置无关目标文件，用于动态库
gcc -fPIC -c mylib.c
```

**基本写法：指定输出文件类型**
`gcc -x <语言> <文件>`
```bash
# 强制按指定语言处理输入文件
gcc -x c header.h
```

---

## 平台与目标

**基本写法：指定目标平台**
`gcc --target=<三元组> <源文件>`
```bash
# 交叉编译目标三元组
gcc --target=arm-linux-gnueabihf main.c
```

**基本写法：指定 sysroot**
`gcc --sysroot=<目录> <源文件>`
```bash
# 交叉编译时指定系统根目录
gcc --sysroot=/opt/arm-rootfs main.c
```

**基本写法：32/64 位**
`gcc -m32 / -m64 <源文件>`
```bash
# 生成 32 位或 64 位代码
gcc -m32 main.c -o app32
```

---

## 诊断与信息

**基本写法：查看预定义宏**
`gcc -dM -E - < /dev/null`
```bash
# 输出所有预定义宏
gcc -dM -E - < /dev/null
```

**基本写法：查看包含路径**
`gcc -print-search-dirs`
```bash
# 显示编译器搜索路径
gcc -print-search-dirs
```

**基本写法：查看默认标准**
`gcc -dM -E - < /dev/null | grep __STDC`
```bash
# 查看默认 C 标准版本
gcc -dM -E - < /dev/null | grep __STDC_VERSION
```

**基本写法：查看版本**
`gcc --version`
```bash
# 显示编译器版本信息
gcc --version
```

**基本写法：详细编译过程**
`gcc -v <源文件>`
```bash
# 显示完整编译各阶段命令
gcc -v main.c -o app
```

**基本写法：保存所有中间文件**
`gcc -save-temps <源文件>`
```bash
# 保留预处理、汇编、目标文件
gcc -save-temps main.c -o app
```

---

## 安全与硬化选项

**基本写法：栈保护**
`gcc -fstack-protector-strong <源文件>`
```bash
# 插入栈溢出检测 canary
gcc -fstack-protector-strong main.c
```

**基本写法：地址随机化**
`gcc -fPIE -pie <源文件>`
```bash
# 生成位置无关可执行文件
gcc -fPIE -pie main.c -o app
```

**基本写法：Fortify 源码**
`gcc -D_FORTIFY_SOURCE=<级别> -O<级别>`
```bash
# 缓冲区函数加强检查，需配合优化
gcc -D_FORTIFY_SOURCE=2 -O2 main.c
```

**基本写法：RelRO**
`gcc -Wl,-z,relro,-z,now <源文件>`
```bash
# 启用完全只读重定位
gcc -Wl,-z,relro,-z,now main.c
```

---

## Clang 专属特性

**基本写法：Clang 静态分析**
`clang --analyze <源文件>`
```bash
# 运行静态分析器查找缺陷
clang --analyze main.c
```

**基本写法：彩色诊断输出**
`clang -fcolor-diagnostics <源文件>`
```bash
# 彩色高亮警告与错误信息
clang -fcolor-diagnostics main.c
```

**基本写法：AddressSanitizer**
`gcc -fsanitize=address <源文件>`
```bash
# 启用内存越界检测（gcc 与 clang 通用）
gcc -fsanitize=address -g main.c -o app
```

**基本写法：UBSan**
`gcc -fsanitize=undefined <源文件>`
```bash
# 启用未定义行为检测
gcc -fsanitize=undefined -g main.c -o app
```

**基本写法：多 sanitizer 组合**
`gcc -fsanitize=address,undefined <源文件>`
```bash
# 同时启用多个 sanitizer
gcc -fsanitize=address,undefined -g main.c
```

---

## 多文件构建

**基本写法：分别编译后链接**
`gcc -c <源>... && gcc <目标>... -o <输出>`
```bash
# 分步编译加快增量构建
gcc -c main.c
gcc -c utils.c
gcc main.o utils.o -o app
```

**基本写法：一步多文件编译**
`gcc <源1> <源2> ... -o <输出>`
```bash
# 一次性编译链接多个源文件
gcc main.c utils.c -o app
```



<!-- ============ 文档分隔线：025-c/033-CDebugGdb.md ============ -->

# C gdb 调试 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 启动与退出

**基本写法：调试可执行文件**
`gdb <可执行文件>`
```bash
# 加载程序进入交互调试
gdb ./app
```

**基本写法：调试带参数程序**
`gdb --args <程序> <参数>...`
```bash
# 启动并预设程序运行参数
gdb --args ./app -c config.txt
```

**基本写法：附加到运行中进程**
`gdb -p <PID>`
```bash
# 附加到已运行的进程进行调试
gdb -p 12345
```

**基本写法：调试 core 文件**
`gdb <程序> <core文件>`
```bash
# 分析崩溃转储文件
gdb ./app core.12345
```

**基本写法：退出 gdb**
`quit / q`
```bash
# 退出调试器，缩写 q
(gdb) q
```

---

## 运行控制

**基本写法：运行程序**
`run [r] [<参数>]`
```bash
# 从头开始运行程序
(gdb) run
```

**基本写法：重新运行**
`run`
```bash
# 重新开始运行程序
(gdb) r
```

**基本写法：单步步过**
`next [n] [<次数>]`
```bash
# 执行下一行，不进入函数内部
(gdb) n
```

**基本写法：单步步入**
`step [s] [<次数>]`
```bash
# 执行下一行，进入函数内部
(gdb) s
```

**基本写法：继续运行**
`continue [c] [<忽略次数>]`
```bash
# 继续执行到下一断点
(gdb) c
```

**基本写法：执行到指定行**
`until [u] [<行号>]`
```bash
# 运行直到大于当前行号
(gdb) until 50
```

**基本写法：跳出当前函数**
`finish`
```bash
# 执行到函数返回并停止
(gdb) finish
```

**基本写法：终止程序**
`kill [k]`
```bash
# 终止当前调试的程序
(gdb) kill
```

---

## 断点管理

**基本写法：设置行断点**
`break [b] <位置>`
```bash
# 在指定行或函数处设置断点
(gdb) b main.c:42
(gdb) b main
```

**基本写法：条件断点**
`break <位置> if <条件>`
```bash
# 仅当条件为真时中断
(gdb) b main.c:50 if i == 100
```

**基本写法：查看断点**
`info breakpoints [i b]`
```bash
# 列出所有断点与编号
(gdb) info b
```

**基本写法：删除断点**
`delete [d] [<编号>]`
```bash
# 删除指定编号断点，无编号则全删
(gdb) delete 2
```

**基本写法：禁用断点**
`disable [<编号>]`
```bash
# 临时禁用断点不触发
(gdb) disable 1
```

**基本写法：启用断点**
`enable [<编号>]`
```bash
# 重新启用已禁用的断点
(gdb) enable 1
```

**基本写法：忽略断点若干次**
`ignore <编号> <次数>`
```bash
# 跳过断点前 N 次触发
(gdb) ignore 1 10
```

**基本写法：临时断点**
`tbreak <位置>`
```bash
# 一次性断点，触发后自动删除
(gdb) tbreak main.c:30
```

**基本写法：监视点**
`watch <表达式>`
```bash
# 表达式值变化时暂停
(gdb) watch counter
```

**基本写法：捕获点**
`catch <事件>`
```bash
# 捕获 throw、exec、fork 等事件
(gdb) catch throw
```

---

## 变量与表达式

**基本写法：打印变量**
`print [p] <表达式>`
```bash
# 输出变量或表达式的值
(gdb) p count
(gdb) p arr[0]
```

**基本写法：打印数组**
`print *<指针>@<数量>`
```bash
# 以数组形式打印连续内存
(gdb) p *arr@10
```

**基本写法：按格式打印**
`print/<格式> <表达式>`
```bash
# x 十六进制 d 十进制 c 字符 t 二进制 f 浮点
(gdb) p/x 255
(gdb) p/t flags
```

**基本写法：自动显示**
`display <表达式>`
```bash
# 每次停止自动打印该表达式
(gdb) display i
```

**基本写法：取消自动显示**
`undisplay <编号>`
```bash
# 移除 display 的自动打印项
(gdb) undisplay 1
```

**基本写法：查看局部变量**
`info locals`
```bash
# 列出当前函数所有局部变量
(gdb) info locals
```

**基本写法：查看参数**
`info args`
```bash
# 列出当前函数参数
(gdb) info args
```

**基本写法：修改变量值**
`set var <变量> = <值>`
```bash
# 运行时修改变量内容
(gdb) set var count = 0
```

---

## 查看内存

**基本写法：检查内存**
`x/<数量><格式><单位> <地址>`
```bash
# 按格式查看内存内容
# 格式：x d c s t；单位：b 字节 h 半字 w 字 g 双字
(gdb) x/16xb arr
```

**基本写法：查看字符串**
`x/s <指针>`
```bash
# 以 C 字符串形式查看内存
(gdb) x/s str
```

**基本写法：查看内存地址**
`print &<变量>`
```bash
# 输出变量地址
(gdb) p &count
```

---

## 调用栈

**基本写法：查看调用栈**
`backtrace [bt] [<深度>]`
```bash
# 显示函数调用栈
(gdb) bt
```

**基本写法：切换栈帧**
`frame [f] <编号>`
```bash
# 切换到指定栈帧
(gdb) frame 2
```

**基本写法：向上切换**
`up [<数量>]`
```bash
# 向调用者方向移动栈帧
(gdb) up
```

**基本写法：向下切换**
`down [<数量>]`
```bash
# 向被调用者方向移动栈帧
(gdb) down
```

**基本写法：查看栈帧信息**
`info frame [f]`
```bash
# 显示当前栈帧详细内容
(gdb) info frame
```

---

## 源码查看

**基本写法：查看源码**
`list [l] [<位置>]`
```bash
# 显示当前行附近源码
(gdb) list
(gdb) l main.c:30
```

**基本写法：指定显示行数**
`set listsize <数量>`
```bash
# 设置 list 默认显示行数
(gdb) set listsize 20
```

**基本写法：向前查看**
`list -`
```bash
# 显示当前源码之前的部分
(gdb) list -
```

**基本写法：查看函数源码**
`list <函数名>`
```bash
# 显示指定函数源码
(gdb) l do_work
```

---

## 多线程调试

**基本写法：查看线程**
`info threads`
```bash
# 列出所有线程及当前位置
(gdb) info threads
```

**基本写法：切换线程**
`thread <编号>`
```bash
# 切换到指定线程
(gdb) thread 3
```

**基本写法：线程上设置断点**
`break <位置> thread <编号>`
```bash
# 仅在指定线程触发断点
(gdb) b main.c:50 thread 2
```

**基本写法：所有线程执行命令**
`thread apply all <命令>`
```bash
# 对所有线程执行同一命令
(gdb) thread apply all bt
```

**基本写法：锁调度器**
`set scheduler-locking on`
```bash
# 仅当前线程执行，其他线程暂停
(gdb) set scheduler-locking on
```

---

## 汇编与寄存器

**基本写法：查看寄存器**
`info registers [i r] [<名称>]`
```bash
# 显示所有或指定寄存器
(gdb) info registers
```

**基本写法：反汇编**
`disassemble [disas] [<范围>]`
```bash
# 反汇编当前函数或指定地址范围
(gdb) disas main
```

**基本写法：汇编级单步**
`stepi [si] / nexti [ni]`
```bash
# 单步执行一条机器指令
(gdb) si
```

---

## 进阶功能

**基本写法：执行命令序列**
`commands <断点编号>`
```bash
# 断点触发时自动执行命令
(gdb) commands 1
> p count
> continue
> end
```

**基本写法：调用函数**
`call <函数调用>`
```bash
# 调试中调用程序内函数
(gdb) call sum(1, 2)
```

**基本写法：导出 core 文件**
`generate-core-file <文件>`
```bash
# 生成当前进程的 core 转储
(gdb) generate-core-file app.core
```

**基本写法：记录会话**
`set logging on [file <文件>]`
```bash
# 将 gdb 输出写入日志文件
(gdb) set logging on
```

**基本写法：执行 shell 命令**
`shell <命令>`
```bash
# 在 gdb 中执行系统命令
(gdb) shell ls
```

**基本写法：加载调试脚本**
`source <脚本>`
```bash
# 加载 gdb 命令脚本
(gdb) source mycmds.gdb
```

---

## 常用初始化

**基本写法：.gdbinit 配置**
`~/.gdbinit`
```bash
# 启动时自动执行的配置文件
# 内容示例：
# set print pretty on
# set print array on
# set pagination off
```

**基本写法：美化输出**
`set print pretty on`
```bash
# 结构体打印时换行缩进
(gdb) set print pretty on
```

**基本写法：关闭分页**
`set pagination off`
```bash
# 长输出时不暂停分页
(gdb) set pagination off
```



<!-- ============ 文档分隔线：025-c/034-CValgrind.md ============ -->

# C Valgrind 内存检测 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本运行

**基本写法：运行内存检测**
`valgrind [<选项>] <程序> [<参数>]`
```bash
# 默认使用 memcheck 工具运行程序
valgrind ./app
```

**基本写法：带程序参数**
`valgrind <程序> <参数>...`
```bash
# 直接跟程序参数运行
valgrind ./app -c config.txt
```

**基本写法：指定工具**
`valgrind --tool=<工具> <程序>`
```bash
# 可选工具：memcheck cachegrind callgrind massif helgrind drd
valgrind --tool=memcheck ./app
```

**基本写法：输出到文件**
`valgrind --log-file=<文件> <程序>`
```bash
# 将诊断信息写入指定文件
valgrind --log-file=val.log ./app
```

---

## Memcheck 内存检测

**基本写法：完整内存检测**
`valgrind --leak-check=full <程序>`
```bash
# 详细检查内存泄漏并分类报告
valgrind --leak-check=full ./app
```

**基本写法：显示可达内存**
`valgrind --show-reachable=yes <程序>`
```bash
# 显示仍可达但未释放的内存
valgrind --leak-check=full --show-reachable=yes ./app
```

**基本写法：泄漏检测级别**
`valgrind --leak-check=<级别> <程序>`
```bash
# no 不检查 summary 概要 full 详细
valgrind --leak-check=summary ./app
```

**基本写法：未初始化值追踪**
`valgrind --track-origins=yes <程序>`
```bash
# 追踪未初始化值的来源
valgrind --track-origins=yes ./app
```

**基本写法：错误汇总**
`valgrind --error-exitcode=<码> <程序>`
```bash
# 发现错误时以指定退出码退出，便于 CI 检测
valgrind --error-exitcode=1 ./app
```

**基本写法：限制错误数**
`valgrind --errors-for-leak-kinds=<类型> <程序>`
```bash
# 指定计入错误的泄漏类型
# definite possible reachable
valgrind --errors-for-leak-kinds=definite ./app
```

---

## 调试符号与源码

**基本写法：带调试信息运行**
`gcc -g -O0 <源> && valgrind <程序>`
```bash
# 编译时加 -g 才能在报告中显示源码位置
gcc -g -O0 main.c -o app
valgrind --leak-check=full ./app
```

**基本写法：显示源码行**
`valgrind --num-callers=<深度> <程序>`
```bash
# 设置调用栈回溯深度
valgrind --num-callers=30 ./app
```

**基本写法：符号还原**
`valgrind --demangle=yes <程序>`
```bash
# 还原 C++ 符号名，C 程序默认即可
valgrind --demangle=yes ./app
```

---

## 缓存分析 Cachegrind

**基本写法：缓存命中分析**
`valgrind --tool=cachegrind <程序>`
```bash
# 分析 CPU 缓存命中率与缺失次数
valgrind --tool=cachegrind ./app
```

**基本写法：输出分析文件**
`valgrind --tool=cachegrind --cachegrind-out-file=<文件> <程序>`
```bash
# 生成 cgout 文件供 cg_annotate 分析
valgrind --tool=cachegrind --cachegrind-out-file=cg.out ./app
```

**基本写法：查看缓存报告**
`cg_annotate <文件>`
```bash
# 解析 cachegrind 输出文件
cg_annotate cg.out
```

---

## 调用分析 Callgrind

**基本写法：函数调用分析**
`valgrind --tool=callgrind <程序>`
```bash
# 收集函数调用次数与开销
valgrind --tool=callgrind ./app
```

**基本写法：收集缓存事件**
`valgrind --tool=callgrind --cache-sim=yes <程序>`
```bash
# 同时收集 I/D 缓存模拟数据
valgrind --tool=callgrind --cache-sim=yes ./app
```

**基本写法：查看调用报告**
`callgrind_annotate <文件>`
```bash
# 解析 callgrind 输出
callgrind_annotate callgrind.out.1234
```

**基本写法：图形化查看**
`kcachegrind <文件>`
```bash
# 用 GUI 工具浏览调用图
kcachegrind callgrind.out.1234
```

---

## 堆分析 Massif

**基本写法：堆内存快照**
`valgrind --tool=massif <程序>`
```bash
# 记录堆内存随时间变化
valgrind --tool=massif ./app
```

**基本写法：包含栈内存**
`valgrind --tool=massif --stacks=yes <程序>`
```bash
# 同时统计栈内存使用
valgrind --tool=massif --stacks=yes ./app
```

**基本写法：查看堆报告**
`ms_print <文件>`
```bash
# 解析 massif 输出为文本图表
ms_print massif.out.1234
```

---

## 线程检测 Helgrind/DRD

**基本写法：竞态检测**
`valgrind --tool=helgrind <程序>`
```bash
# 检测多线程数据竞争
valgrind --tool=helgrind ./app
```

**基本写法：锁顺序分析**
`valgrind --tool=helgrind --track-lockorders=yes <程序>`
```bash
# 检测潜在死锁
valgrind --tool=helgrind ./app
```

**基本写法：DRD 替代工具**
`valgrind --tool=drd <程序>`
```bash
# 另一个线程错误检测器，开销较低
valgrind --tool=drd ./app
```

**基本写法：检测原子操作**
`valgrind --tool=drd --check-stack-var=yes <程序>`
```bash
# 检查栈变量上的线程错误
valgrind --tool=drd --check-stack-var=yes ./app
```

---

## 抑制误报

**基本写法：使用抑制文件**
`valgrind --suppressions=<文件> <程序>`
```bash
# 加载抑制规则屏蔽已知误报
valgrind --suppressions=lib.supp ./app
```

**基本写法：自动生成抑制规则**
`valgrind --gen-suppressions=all <程序>`
```bash
# 输出每个错误的抑制规则模板
valgrind --gen-suppressions=all ./app
```

**基本写法：抑制文件格式**
`{ <名称>, <工具>, <模式> ... }`
```
# 抑制规则示例
{
   libfoo_false_positive
   Memcheck:Cond
   fun:foo_internal
}
```

---

## 性能与控制

**基本写法：统计子进程**
`valgrind --trace-children=yes <程序>`
```bash
# 跟踪 fork/exec 产生的子进程
valgrind --trace-children=yes ./app
```

**基本写法：运行超时**
`valgrind --time-stamp=yes <程序>`
```bash
# 在每条信息前加时间戳
valgrind --time-stamp=yes ./app
```

**基本写法： quieter 模式**
`valgrind -q <程序>`
```bash
# 静默模式，仅打印错误摘要
valgrind -q ./app
```

**基本写法：详细级别**
`valgrind --verbose <程序>`
```bash
# 输出更详细的执行信息
valgrind -v ./app
```

---

## 报告解读

**基本写法：错误类型**
`Invalid read/write / Use of uninitialised value`
```bash
# Invalid read   越界读
# Invalid write  越界写
# Uninit value   使用未初始化值
# Invalid free   重复释放或释放非法指针
# definitely lost 确定泄漏
```

**基本写法：泄漏分类**
`definitely / indirectly / possibly / still reachable`
```bash
# definitely lost   确定泄漏，无指针指向
# indirectly lost   间接泄漏，仅被泄漏内存引用
# possibly lost     可能泄漏，指针指向中间
# still reachable   程序退出时仍可达，通常无害
```

---

## 与 gcc sanitizer 对比

**基本写法：编译期地址检测**
`gcc -fsanitize=address -g <源>`
```bash
# AddressSanitizer 速度更快，作为 valgrind 替代
gcc -fsanitize=address -g main.c -o app
./app
```

**基本写法：运行时检测泄漏**
`ASAN_OPTIONS=detect_leaks=1 ./<程序>`
```bash
# ASan 配合 LeakSanitizer 检测泄漏
ASAN_OPTIONS=detect_leaks=1 ./app
```

**基本写法：选型建议**
`valgrind 用于完整检测，ASan 用于高频测试`
```bash
# valgrind 无需重编译，覆盖全面但慢 10-30 倍
# ASan 需重新编译，速度快但仅检测地址越界
# 建议开发用 ASan，发布前用 valgrind 复核
```
