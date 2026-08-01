# -*- coding: utf-8 -*-
"""修复 013-java/050-ConcurrencyDetailed.md 的 ASCII 图表（逐块替换）。"""

from __future__ import annotations

import pathlib

p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\013-java\050-ConcurrencyDetailed.md")
text = p.read_text(encoding="utf-8")


def replace_block(marker: str, new: str) -> bool:
    global text
    idx = text.find(marker)
    if idx < 0:
        return False
    # 找到包含 marker 的围栏块
    start = text.rfind("```", 0, idx)
    end = text.find("```", idx)
    if start < 0 or end < 0 or end < start:
        return False
    end += 3
    text = text[:start] + new + text[end:]
    return True


# 1) 时间线
new1 = (
    "```mermaid\ntimeline\n"
    "    title Java 并发发展时间线\n"
    "    1995: Java 1.0：Thread、Runnable、synchronized，仅 green threads，无真正内核线程映射\n"
    "    1997: Java 1.1：wait/notify/notifyAll（Object 方法）\n"
    "    2002: J2SE 1.4：NIO（非阻塞 IO 基础）\n"
    "    2004: Java 5：JSR 166（java.util.concurrent），Doug Lea 并发库进入 JDK，Executor/Future/Atomic/Lock/Condition，ConcurrentHashMap、CopyOnWriteArrayList\n"
    "    2006: Java 6：并发性能优化，synchronized 偏向锁，AQS 框架成熟\n"
    "    2011: Java 7：ForkJoinPool（JSR 166y），Phaser、TransferQueue\n"
    "    2014: Java 8：CompletableFuture、StampedLock，Lambda 简化并发代码，并行流基于 ForkJoinPool\n"
    "    2017: Java 9：Publisher/Subscriber（reactive streams），Flow 类（JEP 266）\n"
    "    2018: Java 11：VarHandle（JEP 193）替代 sun.misc.Unsafe，Flight Recorder 开源\n"
    "    2021: Java 17：强封装限制 sun.misc.Unsafe，sealed class 配合并发模式\n"
    "    2023: Java 21 LTS：虚拟线程 GA（JEP 444），Scoped Values 预览，结构化并发预览，默认禁用偏向锁\n"
    "    2024-2025: Java 22-25：结构化并发 GA，虚拟线程性能优化\n"
    "```"
)
ok1 = replace_block("1995 ──── Java 1.0", new1)

# 2) Mark Word 行
new2 = (
    "```mermaid\nflowchart LR\n"
    "    MW[Mark Word（64 bits）] --- CP[Class Pointer（32/64 bits）]\n"
    "    CP --- AL[Array Length（32 bits，仅数组）]\n"
    "```"
)
ok2 = replace_block("Class Pointer", new2)

# 3) Mark Word 状态表
new3 = (
    "```mermaid\nflowchart TD\n"
    "    MW[Mark Word（64 bits）]\n"
    "    MW --> U[无锁：hash(25) / age(4) / 0 / 01]\n"
    "    MW --> B[偏向锁：thread(54) / epoch(2) / 1 / 01]\n"
    "    MW --> L[轻量锁：ptr_to_lock_record(62) / 00]\n"
    "    MW --> H[重量锁：ptr_to_heavy_monitor(62) / 10]\n"
    "    MW --> G[GC 标记：- / 11]\n"
    "```"
)
ok3 = replace_block("无锁       │ hash (25)", new3)

# 4) 锁升级状态机
new4 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> 无锁\n"
    "    无锁 --> 偏向锁\n"
    "    偏向锁 --> 轻量级锁\n"
    "    轻量级锁 --> 重量级锁\n"
    "    重量级锁 --> [*]\n"
    "```"
)
ok4 = replace_block("无锁 ──→ 偏向锁", new4)

# 5) AQS 双向队列
new5 = (
    "```mermaid\nflowchart LR\n"
    "    H[head] --> N1[Node]\n"
    "    N1 -->|next| N2[Node]\n"
    "    N2 -->|next| N3[Node]\n"
    "    N3 --> T[tail]\n"
    "    N3 -->|prev| N2\n"
    "    N2 -->|prev| N1\n"
    "    N2 --> S[后继节点自旋检查前驱]\n"
    "```"
)
ok5 = replace_block("head                                          tail", new5)

p.write_text(text, encoding="utf-8")
print("timeline:", ok1, "markword:", ok2, "status:", ok3, "upgrade:", ok4, "queue:", ok5)
