# -*- coding: utf-8 -*-
"""修复 024-cs-fundamentals 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\024-cs-fundamentals")
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

# 007 指令格式
p = ROOT / "007-ComputerPrinciple.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    OP[操作码 opcode] --- SRC[源操作数 src] --- DST[目标操作数 dst]\n"
    "```"
)
results.append(("007-instr", replace_fence(p, "操作码", new)))

# 009 分支预测
p = ROOT / "009-DirectivePipeline.md"
new2 = (
    "```mermaid\nflowchart LR\n"
    "    G[全局预测器 gshare] --> SEL[选择器] --> P[最终预测]\n"
    "    L[局部预测器 2-bit] --> SEL\n"
    "```"
)
results.append(("009-predictor", replace_fence(p, "全局预测器", new2)))

new3 = (
    "```mermaid\nflowchart LR\n"
    "    A[ALU 操作 32位] --- B[ALU 操作 32位] --- C[访存操作 32位] --- D[分支操作 32位]\n"
    "```\n\n"
    "一条 128 位 VLIW 指令"
)
results.append(("009-vliw", replace_fence(p, "ALU 操作", new3)))

# 010 页表项
p = ROOT / "010-StorageSystem.md"
new4 = (
    "```mermaid\nflowchart LR\n"
    "    V[有效位] --- RW[读写位] --- U[用户位] --- D[脏位] --- A[访问位] --- P[物理页号]\n"
    "```"
)
results.append(("010-pte", replace_fence(p, "有效位", new4)))

# 011 总线握手
p = ROOT / "011-BusAndInterface.md"
new5 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant M as 主设备\n"
    "    participant S as 从设备\n"
    "    M->>S: 发请求 REQ\n"
    "    S-->>M: 发应答 ACK\n"
    "    M->>S: 撤销 REQ\n"
    "    S-->>M: 撤销 ACK\n"
    "```"
)
results.append(("011-handshake", replace_fence(p, "发请求(REQ)", new5)))

new6 = (
    "```mermaid\nflowchart LR\n"
    "    T[TLP 头 3-4DW] --- O[可选头 0-3DW] --- D[数据负载 0-1024DW] --- E[ECRC 1DW]\n"
    "```"
)
results.append(("011-tlp", replace_fence(p, "TLP头", new6)))

# 012 并行计算
p = ROOT / "012-ParallelCalculate.md"
new7 = (
    "```mermaid\nflowchart LR\n"
    "    C0[CPU0] --> N[互连网络] --> S[共享内存]\n"
    "    C1[CPU1] --> N\n"
    "    C2[CPU2] --> N\n"
    "    C3[CPU3] --> N\n"
    "```"
)
results.append(("012-uma", replace_fence(p, "CPU0 ──┐", new7)))

new8 = (
    "```mermaid\nflowchart LR\n"
    "    C0[CPU0 + 内存0] --> N[互连网络]\n"
    "    C1[CPU1 + 内存1] --> N\n"
    "    C2[CPU2 + 内存2] --> N\n"
    "    C3[CPU3 + 内存3] --> N\n"
    "```"
)
results.append(("012-numa", replace_fence(p, "CPU0 + 内存0", new8)))

# 017 编译流水线
p = ROOT / "017-CompilePrinciple.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    SRC[源代码] --> FE[前端<br/>词法分析 Lexical<br/>语法分析 Syntax<br/>语义分析 Semantic]\n"
    "    FE --> IR[IR 中间表示] --> BE[后端<br/>中间代码优化<br/>目标代码生成<br/>汇编/链接]\n"
    "    FE --> ST[符号表/AST]\n"
    "    BE --> OBJ[目标代码]\n"
    "```"
)
results.append(("017-pipeline", replace_fence(p, "编译器流水线", new9)))

# 020 LR 分析
p = ROOT / "020-CompilePrincipleAdvanced.md"
new10 = (
    "```mermaid\nflowchart LR\n"
    "    I[输入] --> ST[栈<br/>状态+符号] --> A[动作]\n"
    "```"
)
results.append(("020-lr", replace_fence(p, "输入 ──→", new10)))

# 021 inode
p = ROOT / "021-OperatingSystemAdvanced.md"
new11 = (
    "```mermaid\nflowchart TD\n"
    "    D[直接块指针 ×12 小文件] --> I1[一级间接块指针 中等文件]\n"
    "    I1 --> I2[二级间接块指针 大文件]\n"
    "    I2 --> I3[三级间接块指针 超大文件]\n"
    "```"
)
results.append(("021-inode", replace_fence(p, "直接块指针", new11)))

# 022 拥塞控制
p = ROOT / "022-ComputerNetworkAdvanced.md"
new12 = (
    "```mermaid\nflowchart LR\n"
    "    SS[慢启动] --> SH[ssthresh] --> CA[拥塞避免]\n"
    "    CA -->|超时 ssthresh=cwnd/2 cwnd=1| SS\n"
    "    CA -->|3重复ACK| FR[快速恢复] -->|新ACK| CA\n"
    "```"
)
results.append(("022-congestion", replace_fence(p, "慢启动", new12)))

# 024 GOP
p = ROOT / "024-MultimediaTechnology.md"
new13 = (
    "```mermaid\nflowchart LR\n"
    "    I[I] B1[B] B2[B] P1[P] B3[B] B4[B] P2[P] B5[B] B6[B] I2[I]\n"
    "    I --- B1 --- B2 --- P1 --- B3 --- B4 --- P2 --- B5 --- B6 --- I2\n"
    "```\n\n"
    "I 帧为 GOP 起始，新 GOP 从下一个 I 帧开始"
)
results.append(("024-gop", replace_fence(p, "I B B P", new13)))

for name, ok in results:
    print(f"{name}: {ok}")
