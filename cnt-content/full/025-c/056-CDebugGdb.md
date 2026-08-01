---
order: 560
title: C gdb 调试 语法速查手册
module: c

category: '025-c'
difficulty: beginner
description: C gdb 调试 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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
| C POSIX 与系统调用速查 | 053-CPosixSystemCall | 本文的并列主题 |
| C23 新特性 | 054-C23NewFeatures | 本文的并列主题 |
| C 编译器命令 语法速查手册 | 055-CCompilerOptions | 本文的并列主题 |
| C gdb 调试 语法速查手册 | 056-CDebugGdb | 本文自身 |
| C Valgrind 内存检测 语法速查手册 | 057-CValgrind | 本文的并列主题 |
