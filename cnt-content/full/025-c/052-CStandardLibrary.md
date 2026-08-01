---
order: 520
title: C 标准库函数速查
module: 025-c
category: '025-c'
difficulty: beginner
description: C 标准库函数速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 参考文献

cppreference C 文档：https://zh.cppreference.com/w/c
C 标准草案：https://www.open-std.org/jtc1/sc22/wg14/
GCC 官方文档：https://gcc.gnu.org/onlinedocs/
Linux man pages：https://man7.org/linux/man-pages/
C 语言常见误解：https://www.yodaiken.com/

## 延伸阅读

C 指针与数组深入，见 025-c 模块指针文档。
C 枚举与 typedef，见 025-c/007-EnumTypedef 文档。
C++ 面向对象与模板，见 026-cpp 模块。
嵌入式 C 与硬件交互，见 035-iot 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 C 语言课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 指针与数组的等价与差异

数组名是常量地址（不可赋值），`sizeof(arr)` 返回整个数组字节数；作为函数实参时退化为首元素指针，`sizeof` 变为指针大小。
指针算术：`p + i` 移动 i 个元素；二维数组 `int a[3][4]` 中 `a` 类型为 `int (*)[4]`，`a[i][j]` 等价 `*(*(a+i)+j)`。
函数指针：`int (*fp)(int)` 可赋值、传参、构成回调表；typedef 简化声明。
const 位置语义：`const int *p`（指向常量的指针）与 `int *const p`（常量指针）不同，从内向外读声明可避免混淆。

### 13.2 C 内存布局与对齐

进程内存分为代码段、数据段、BSS、堆、栈；栈向下增长，堆向上增长，中间为空洞。
结构体成员按对齐规则布局：成员偏移为自身对齐值的倍数，结构体大小为最大对齐值的倍数；重排成员可减少 padding。
位域（bit-field）依赖编译器布局，序列化跨平台数据时应使用显式移位。
理解布局有助于调试（指针偏移、序列化、共享内存）与优化（缓存友好结构体）。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C 语言概述 | 001-CLanguageOverview | 本文的前置基础 |
| 程序结构与基本语法 | 002-ProgramStructureBasicSyntax | 本文的并列主题 |
| 数据类型详解 | 003-DataTypeDetailed | 本文的并列主题 |
| 变量与常量 | 004-VariableConstant | 本文的并列主题 |
| 位运算与位域 | 005-BitwiseBitField | 本文的并列主题 |
| 运算符与表达式 | 006-OperatorExpression | 本文的并列主题 |
| 枚举与typedef | 007-EnumTypedef | 本文的并列主题 |
| 多文件编译 | 008-TheLinuxProgrammingInterface | 本文的并列主题 |
| 动态内存管理 | 009-DynamicMemoryManagement | 本文的并列主题 |
| 函数指针与回调 | 010-FunctionPointerCallback | 本文的并列主题 |
| 可变参数函数 | 011-VarargsFunction | 本文的并列主题 |
| 信号处理 | 012-SignalHandling | 本文的并列主题 |
| 原子操作与内存模型 | 013-AtomicAndMemoryModel | 本文的并列主题 |
| 泛型选择 | 014-GenericSelection | 本文的并列主题 |
| 位域 | 015-BitField | 本文的并列主题 |
| 对齐与内存布局 | 016-AlignmentMemoryLayout | 本文的并列主题 |
| 控制流 | 017-ControlFlow | 本文的并列主题 |
| 属性与编译器扩展 | 018-AttributeCompilerExtension | 本文的并列主题 |
| 安全函数与边界检查 | 019-SafeFunctionBoundsCheck | 本文的安全延伸 |
| 内联函数与宏 | 020-InlineFunctionMacro | 本文的并列主题 |
| 复杂声明解析 | 021-ComplexDeclarationParsing | 本文的并列主题 |
| 线程与并发 | 022-ThreadConcurrency | 本文的并列主题 |
| POSIX线程 | 023-POSIXThread | 本文的并列主题 |
| Socket网络编程 | 024-SocketNetworkProgramming | 本文的并列主题 |
| 进程与管道 | 025-ProcessAndPipe | 本文的并列主题 |
| 共享内存与信号量 | 026-SharedMemorySemaphore | 本文的并列主题 |
| 文件系统操作 | 027-FileSystemOperation | 本文的并列主题 |
| 函数详解 | 028-FunctionDetailed | 本文的并列主题 |
| 动态库与静态库 | 029-DynamicStaticLibrary | 本文的并列主题 |
| 国际化与本地化 | 030-HelloWorldOrOr | 本文的并列主题 |
| 构建系统 | 031-BuildSystem | 本文的并列主题 |
| 静态分析与调试 | 032-StaticAnalysisDebug | 本文的并列主题 |
| 跨平台编程 | 033-CrossPlatformProgramming | 本文的并列主题 |
| 嵌入式C编程 | 034-EmbeddedCProgramming | 本文的并列主题 |
| C与汇编交互 | 035-CAssemblyInteraction | 本文的并列主题 |
| 数组详解 | 036-ArrayDetailed | 本文的并列主题 |
| 预处理器与宏 | 037-PreprocessorMacro | 本文的并列主题 |
| C23 与 C2y 新标准 | 038-C23C2y | 本文的并列主题 |
| 指针深度解析 | 039-PointerDeep | 本文的并列主题 |
| 内存管理 | 040-MemoryManagement | 本文的并列主题 |
| 内存对齐 | 041-MemoryAlignment | 本文的并列主题 |
| 结构体与联合体 | 042-StructAndUnion | 本文的并列主题 |
| 函数调用栈帧 | 043-FunctionCallStackFrame | 本文的并列主题 |
| 指针与数组的区别 | 044-PointerArrayDifference | 本文的并列主题 |
| 二级指针与指针数组 | 045-DoublePointerPointerArray | 本文的并列主题 |
| 函数指针回调与跳转表 | 046-FunctionPointerCallbackJumpTable | 本文的并列主题 |
| volatile关键字 | 047-LinuxKernelMemoryBarriers | 本文的并列主题 |
| 文件 I/O 操作 | 048-IO | 本文的并列主题 |
| C 语言理论知识点 | 049-CLanguageTheory | 本文的并列主题 |
| C 语言高级特性与系统编程 | 050-CAdvancedSystemProgramming | 本文的并列主题 |
| C 语言项目示例：学生成绩管理系统 | 051-CProjectExampleStudentGradeSystem | 本文的综合应用 |
| C 标准库函数速查 | 052-CStandardLibrary | 本文自身 |
| C POSIX 与系统调用速查 | 053-CPosixSystemCall | 本文的并列主题 |
| C23 新特性 | 054-C23NewFeatures | 本文的并列主题 |
| C 编译器命令 语法速查手册 | 055-CCompilerOptions | 本文的并列主题 |
| C gdb 调试 语法速查手册 | 056-CDebugGdb | 本文的并列主题 |
| C Valgrind 内存检测 语法速查手册 | 057-CValgrind | 本文的并列主题 |
