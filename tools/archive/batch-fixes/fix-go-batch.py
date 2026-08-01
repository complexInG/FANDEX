# -*- coding: utf-8 -*-
"""批量修复 016-go 下的 ASCII 图表。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\016-go")


def replace_block(path: pathlib.Path, marker: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx < 0:
        return False
    start = text.rfind("```", 0, idx)
    end = text.find("```", idx)
    if start < 0 or end < 0 or end < start:
        return False
    end += 3
    path.write_text(text[:start] + new + text[end:], encoding="utf-8")
    return True


results = []

# 004-GoDataStructure: 切片布局
p = ROOT / "004-GoDataStructure.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Header[SliceHeader]\n"
    "        P[ptr 指针]\n"
    "        L[len 长度]\n"
    "        C[cap 容量]\n"
    "    end\n"
    "    subgraph Arr[底层数组]\n"
    "        A0[10] A1[20] A2[30] A3[40] A4[50]\n"
    "    end\n"
    "    P --> A1\n"
    "```"
)
results.append(("004-slice", replace_block(p, "┌─────────┬──────────┬──────────────┐", new)))

# 004-GoDataStructure: hmap
new2 = (
    "```mermaid\nflowchart TD\n"
    "    H[hmap 结构]\n"
    "    H --> F1[count int：元素数量]\n"
    "    H --> F2[B uint8：桶数量 = 2^B]\n"
    "    H --> F3[hash0 uint32：哈希种子]\n"
    "    H --> F4[buckets unsafe.Pointer：桶数组]\n"
    "    H --> F5[oldbuckets unsafe.Pointer：扩容时旧桶]\n"
    "    H --> F6[...]\n"
    "    B[bmap 桶，存储 8 个键值对]\n"
    "    B --> T[tophash[0-7] 哈希高 8 位]\n"
    "    B --> K[key0-key7]\n"
    "    B --> V[val0-val7]\n"
    "    B --> O[overflow pointer 溢出桶指针]\n"
    "```"
)
results.append(("004-hmap", replace_block(p, "hmap 结构", new2)))

# 005-GoInterfaceComposition
p = ROOT / "005-GoInterfaceComposition.md"
new3 = (
    "```mermaid\nflowchart LR\n"
    "    TD[类型指针 type descriptor] -->|具体类型信息| T\n"
    "    DP[数据指针 data pointer] -->|实际值的副本（或指针）| T\n"
    "```"
)
results.append(("005-iface", replace_block(p, "类型指针 (type descriptor)", new3)))

# 006-GoConcurrentProgramming: 调度器
p = ROOT / "006-GoConcurrentProgramming.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    G[G goroutine 协程，用户级轻量线程]\n"
    "    M[M machine 操作系统线程]\n"
    "    PP[P processor 逻辑处理器，持有本地运行队列]\n"
    "    S[Scheduler]\n"
    "    S --> P0[P0 [G G]]\n"
    "    S --> P1[P1 [G G]]\n"
    "    S --> P2[P2 [G G]]\n"
    "    S --> P3[P3 [G G]]\n"
    "    S --> GQ[全局队列 [G G G]]\n"
    "    P0 --> M0[M0]\n"
    "    P1 --> M1[M1]\n"
    "    P2 --> M2[M2]\n"
    "    P3 --> M3[M3]\n"
    "```\n\n"
    "调度策略：\n"
    "- Work Stealing：P 的本地队列为空时，从其他 P 或全局队列窃取 G\n"
    "- Hand Off：M 阻塞（如系统调用）时，P 绑定到新的 M 继续运行\n"
    "- 抢占式调度：基于协作（函数调用检查）+ 基于信号（Go 1.14+）"
)
results.append(("006-scheduler", replace_block(p, "G (Goroutine)", new4)))

# 006-GoConcurrentProgramming: hchan
new5 = (
    "```mermaid\nflowchart TD\n"
    "    H[hchan 结构]\n"
    "    H --> F1[buf *array 环形缓冲区]\n"
    "    H --> F2[sendx uint 发送索引]\n"
    "    H --> F3[recvx uint 接收索引]\n"
    "    H --> F4[qcount uint 缓冲区元素数]\n"
    "    H --> F5[dataqsiz uint 缓冲区大小]\n"
    "    H --> F6[elemtype *type 元素类型]\n"
    "    H --> F7[closed uint32 是否关闭]\n"
    "    H --> F8[sendq waitq 发送等待队列]\n"
    "    H --> F9[recvq waitq 接收等待队列]\n"
    "    H --> F10[lock mutex 互斥锁]\n"
    "```"
)
results.append(("006-hchan", replace_block(p, "hchan 结构", new5)))

# 012-MapPrinciple: 演进时间线
p = ROOT / "012-MapPrinciple.md"
new6 = (
    "```mermaid\ntimeline\n"
    "    title Go map 演进时间线\n"
    "    2012: Go 1.0 bucket chaining（8 slots/bucket）\n"
    "    2015: Go 1.5 runtime 重写为 Go，类型特化（fast64/faststr）\n"
    "    2017: Go 1.9 sync.Map（read/write 分离）\n"
    "    2022: Go 1.18 泛型支持（语法层）\n"
    "    2023: Go 1.21 maps 标准包\n"
    "    2024: Go 1.22 小 map 分配优化\n"
    "    2025: Go 1.24 Swiss Table（开放寻址 + SIMD metadata）\n"
    "```"
)
results.append(("012-map-timeline", replace_block(p, "Go 1.0  (2012)", new6)))

# 012-MapPrinciple: bmap 布局
new7 = (
    "```mermaid\nflowchart TD\n"
    "    B[bmap 内存布局]\n"
    "    B --> T[tophash[8] 8 字节]\n"
    "    B --> K[key[0] - key[7]]\n"
    "    B --> V[value[0] - value[7]]\n"
    "    B --> PD[padding 可选，确保 overflow 指针 8 字节对齐]\n"
    "    B --> O[overflow *bmap 8 字节]\n"
    "```"
)
results.append(("012-bmap", replace_block(p, "tophash[8]", new7)))

# 012-MapPrinciple: swiss group
new8 = (
    "```mermaid\nflowchart TD\n"
    "    G0[group[0]]\n"
    "    G0 --> C0[ctrl 8 字节]\n"
    "    G0 --> S0[slot[0].key / slot[0].value]\n"
    "    G0 --> S1[slot[1].key / slot[1].value]\n"
    "    G0 --> S7[slot[7].key / slot[7].value]\n"
    "    G1[group[1]]\n"
    "    G0 --> G1\n"
    "```"
)
results.append(("012-swiss", replace_block(p, "group[0]", new8)))

for name, ok in results:
    print(f"{name}: {ok}")
