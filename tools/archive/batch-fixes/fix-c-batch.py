# -*- coding: utf-8 -*-
"""修复 025-c 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\025-c")
BOX = re.compile(
    "[\u250c\u2510\u2514\u2518\u251c\u2524\u252c\u2534\u253c\u2500\u2502"
    "\u2554\u2557\u255a\u255d\u2560\u2563\u2566\u2569\u256c\u2550\u2551"
    "\u256d\u256e\u256f\u2570]|\+[-=+]{2,}\+"
)


def replace_fence(path: pathlib.Path, keyword: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    idx = text.find(keyword)
    while idx >= 0:
        start = text.rfind("```", 0, idx)
        end = text.find("```", idx)
        if start >= 0 and end > start and BOX.search(text[start:end]):
            path.write_text(text[:start] + new + text[end + 3 :], encoding="utf-8")
            return True
        idx = text.find(keyword, idx + 1)
    return False


results = []

# 001 C 语言时间线
p = ROOT / "001-CLanguageOverview.md"
new = (
    "```mermaid\ntimeline\n"
    "    title C 语言发展时间线\n"
    "    1967: BCPL（Martin Richards, Cambridge）\n"
    "    1969: B 语言（Ken Thompson, Bell Labs, PDP-7）\n"
    "    1972: C 语言诞生（Dennis Ritchie, Bell Labs, PDP-11）\n"
    "    1973: UNIX 内核用 C 重写\n"
    "    1978: K&R《The C Programming Language》出版\n"
    "    1983: ANSI X3J11 委员会成立\n"
    "    1989: ANSI C89 标准发布\n"
    "    1990: ISO C90 标准发布\n"
    "    1995: C95 (AMD1) 修订\n"
    "    1999: ISO C99 标准发布\n"
    "    2011: ISO C11 标准发布\n"
    "    2018: ISO C17 (C18) 标准发布\n"
    "    2024: ISO C23 标准发布\n"
    "    2025+: C2y 草案讨论中\n"
    "```"
)
results.append(("001-timeline", replace_fence(p, "BCPL", new)))

# 002 语法演进
p = ROOT / "002-ProgramStructureBasicSyntax.md"
new2 = (
    "```mermaid\ntimeline\n"
    "    title C 语法演进时间线\n"
    "    1978: K&R C 隐式 int、旧式函数定义、/* */ 注释\n"
    "    1989: C89 函数原型、void、const/volatile\n"
    "    1999: C99 // 注释、long long、for 内声明\n"
    "    2011: C11 _Generic、_Atomic、_Static_assert\n"
    "    2018: C17 C11 bug-fix\n"
    "    2024: C23 nullptr、bool、auto 推断、constexpr、属性\n"
    "    2025+: C2y 模块、协程（草案）\n"
    "```"
)
results.append(("002-syntax", replace_fence(p, "K&R C", new2)))

new3 = (
    "```mermaid\nflowchart TD\n"
    "    S1[1. 预处理指令<br/>#include / #define / #if / #ifdef / #endif]\n"
    "    S2[2. 类型定义<br/>typedef struct / typedef enum]\n"
    "    S3[3. 全局变量声明<br/>extern int / static int]\n"
    "    S4[4. 函数原型<br/>int function(int, int)]\n"
    "    S5[5. main 函数<br/>int main(int argc, char *argv[])]\n"
    "    S6[6. 函数定义<br/>int function(int a, int b)]\n"
    "    S1 --> S2 --> S3 --> S4 --> S5 --> S6\n"
    "```"
)
results.append(("002-structure", replace_fence(p, "预处理指令", new3)))

# 004 内存布局
p = ROOT / "004-VariableConstant.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    K[Kernel space 操作系统保留 高地址] --> S[Stack 局部变量 向下增长]\n"
    "    S --> H[Heap malloc 分配 向上增长]\n"
    "    H --> B[bss 未初始化全局/静态变量]\n"
    "    B --> D[data 已初始化全局/静态变量]\n"
    "    D --> R[rodata 字符串字面量 const 全局]\n"
    "    R --> T[text 代码段 低地址]\n"
    "```"
)
results.append(("004-memory", replace_fence(p, "Kernel space", new4)))

# 009 内存布局2
p = ROOT / "009-DynamicMemoryManagement.md"
new5 = (
    "```mermaid\nflowchart TD\n"
    "    K[Kernel 高地址] --> S[Stack 函数局部变量 alloca]\n"
    "    S --> M[mmap region 大对象 mmap 分配]\n"
    "    M --> H[Heap malloc/calloc/realloc 向上增长]\n"
    "    H --> B[bss 未初始化全局变量]\n"
    "    B --> D[data 已初始化全局变量]\n"
    "    D --> R[rodata 字符串字面量 const]\n"
    "    R --> T[text 代码段 低地址]\n"
    "```"
)
results.append(("009-memory", replace_fence(p, "mmap region", new5)))

# 030 国际化标准演进
p = ROOT / "030-HelloWorldOrOr.md"
new6 = (
    "```mermaid\ntimeline\n"
    "    title C 标准演进（国际化视角）\n"
    "    1989: C89 locale.h setlocale LC_*\n"
    "    1995: C95 wchar.h wchar_t wprintf\n"
    "    1999: C99 wctype mbrlen wcrtomb\n"
    "    2011: C11 uchar.h char16_t char32_t\n"
    "    2018: C17 勘误\n"
    "    2024: C23 char8_t u8=ch8 #embed\n"
    "```"
)
results.append(("030-i18n", replace_fence(p, "C 标准演进时间线", new6)))

new7 = (
    "```mermaid\nflowchart TD\n"
    "    M[menu.c 应用代码] --> I[i18n_lite.c 轻量级 i18n 库 <10KB]\n"
    "    I --> H[messages.h 消息表 const 存储在 Flash]\n"
    "    H --> U[utf8.c UTF-8 字符串操作]\n"
    "```"
)
results.append(("030-modules", replace_fence(p, "menu.c", new7)))

# 040 内存布局3
p = ROOT / "040-MemoryManagement.md"
new8 = (
    "```mermaid\nflowchart TD\n"
    "    S[栈区 Stack 局部变量 函数调用信息 向下增长 高地址]\n"
    "    F[空闲区域]\n"
    "    H[堆区 Heap 动态分配内存 向上增长]\n"
    "    B[BSS 段 未初始化全局/静态变量 自动清零]\n"
    "    D[数据段 Data 已初始化全局/静态变量]\n"
    "    T[代码段 Text 可执行指令 只读 低地址]\n"
    "    S --> F --> H --> B --> D --> T\n"
    "```"
)
results.append(("040-memory", replace_fence(p, "栈区 (Stack)", new8)))

# 043 栈帧
p = ROOT / "043-FunctionCallStackFrame.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    P[参数 N N>6 ... 参数 7 调用方压栈 高地址]\n"
    "    P --> R[返回地址 call 指令自动压栈 rbp 指向此处]\n"
    "    R --> S[保存的 rbp push rbp]\n"
    "    S --> L[局部变量/临时存储]\n"
    "    L --> C[保存的 callee-saved 寄存器 rbx r12-15]\n"
    "    C --> G[栈金丝雀 canary -fstack-protector]\n"
    "    G --> A[对齐填充 确保 rsp % 16 == 0 rsp 指向此处 低地址]\n"
    "```"
)
results.append(("043-frame", replace_fence(p, "参数 N (N > 6)", new9)))

# 045 指针体系
p = ROOT / "045-DoublePointerPointerArray.md"
new10 = (
    "```mermaid\nflowchart TD\n"
    "    P1[一级指针基础 T*] --> P2[二级指针语义 T**<br/>内存布局与解引用]\n"
    "    P2 --> PA[指针数组 T *arr[N]]\n"
    "    P2 --> AP[数组指针 T (*p)[N]]\n"
    "    PA --> MD[多维数组与指针衰减]\n"
    "    AP --> MD\n"
    "    MD --> FP[函数指针与函数指针数组]\n"
    "    FP --> ENG[二级指针工程模式 链表/树/回调]\n"
    "    ENG --> CMP[跨语言对比与陷阱分析]\n"
    "```"
)
results.append(("045-pointer-tree", replace_fence(p, "一级指针基础", new10)))

new11 = (
    "```mermaid\nflowchart LR\n"
    "    A[0x1000 a=1 0x1004 b=2 0x1008 c=3 0x100c d=4 0x1010 e=5]\n"
    "    ARR[arr[0] 0x2000→a<br/>arr[1] 0x2008→b<br/>arr[2] 0x2010→c<br/>arr[3] 0x2018→d<br/>arr[4] 0x2020→e]\n"
    "    A --- ARR\n"
    "```"
)
results.append(("045-ptr-array", replace_fence(p, "0x1000", new11)))

new12 = (
    "```mermaid\nflowchart LR\n"
    "    AV[argv] --> A0[[0] → ./program]<br/>A1[[1] → hello]<br/>A2[[2] → world]<br/>A3[[3] → NULL]\n"
    "```"
)
results.append(("045-argv", replace_fence(p, "argv ──►", new12)))

new13 = (
    "```mermaid\nflowchart LR\n"
    "    A[0x1000 arr[0]=1 0x1004 arr[1]=2 0x1008 arr[2]=3 0x100c arr[3]=4 0x1010 arr[4]=5]\n"
    "    P[ptr 0x2000 → 指向整个 arr 数组]\n"
    "    P --- A\n"
    "```"
)
results.append(("045-arr-ptr", replace_fence(p, "arr[0]", new13)))

# 047 内存屏障
p = ROOT / "047-LinuxKernelMemoryBarriers.md"
new14 = (
    "```mermaid\nflowchart TD\n"
    "    C0[CPU 0<br/>L1 ~1ns<br/>L2 ~3ns]\n"
    "    C1[CPU 1<br/>L1 ~1ns<br/>L2 ~3ns]\n"
    "    L3[L3 ~10ns]\n"
    "    MEM[Memory ~100ns]\n"
    "    C0 --> L3\n"
    "    C1 --> L3\n"
    "    L3 --> MEM\n"
    "```"
)
results.append(("047-cache", replace_fence(p, "CPU 0", new14)))

for name, ok in results:
    print(f"{name}: {ok}")
