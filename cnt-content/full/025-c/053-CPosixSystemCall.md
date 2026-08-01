---
order: 530
title: C POSIX 与系统调用速查
module: 025-c
category: '025-c'
difficulty: beginner
description: C POSIX 与系统调用速查 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
| C 标准库函数速查 | 052-CStandardLibrary | 本文的并列主题 |
| C POSIX 与系统调用速查 | 053-CPosixSystemCall | 本文自身 |
| C23 新特性 | 054-C23NewFeatures | 本文的并列主题 |
| C 编译器命令 语法速查手册 | 055-CCompilerOptions | 本文的并列主题 |
| C gdb 调试 语法速查手册 | 056-CDebugGdb | 本文的并列主题 |
| C Valgrind 内存检测 语法速查手册 | 057-CValgrind | 本文的并列主题 |
