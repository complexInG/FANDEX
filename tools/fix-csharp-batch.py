# -*- coding: utf-8 -*-
"""修复 015-csharp 下 ASCII 图表。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\015-csharp")


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

p = ROOT / "010-CGameDevUnity.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    subgraph DOTS[Unity DOTS]\n"
    "        E[Entities<br/>ECS 框架]\n"
    "        B[Burst Compiler<br/>SIMD 编译器]\n"
    "        J[C# Job System]\n"
    "        C[Collections<br/>NativeArray 等]\n"
    "    end\n"
    "    E --- B\n"
    "    J --- C\n"
    "```"
)
results.append(("010-dots", replace_block(p, "Unity DOTS", new)))

p = ROOT / "012-AsyncProgrammingDetailed.md"
new2 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> Created\n"
    "    Created --> WaitingForActivation\n"
    "    WaitingForActivation --> WaitingToRun\n"
    "    WaitingToRun --> Running\n"
    "    Running --> RanToCompletion\n"
    "    Running --> Faulted\n"
    "    Running --> Canceled\n"
    "```"
)
results.append(("012-task-state", replace_block(p, "WaitingForActivation", new2)))

p = ROOT / "016-SpanMemory.md"
new3 = (
    "```mermaid\nflowchart TD\n"
    "    S[Span&lt;T&gt; 内存布局，Total 16 bytes]\n"
    "    S --> R[ref T _reference 8 bytes<br/>指向内存起始]\n"
    "    S --> L[int _length 4 bytes<br/>视图长度]\n"
    "    S --> P[padding 4 bytes<br/>对齐填充]\n"
    "```"
)
results.append(("016-span", replace_block(p, "ref T _reference", new3)))

new4 = (
    "```mermaid\nflowchart LR\n"
    "    T1[Thread 1 TLS cache size buckets] --> C[Shared central pool per-bucket stacks]\n"
    "    T2[Thread 2 TLS cache size buckets] --> C\n"
    "    T3[Thread 3 TLS cache size buckets] --> C\n"
    "```"
)
results.append(("016-tls", replace_block(p, "TLS cache", new4)))

p = ROOT / "030-EFCoreMigrationOptimization.md"
new5 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> Detached\n"
    "    Detached --> Added: Add()\n"
    "    Added --> Unchanged: SaveChanges()\n"
    "    Unchanged --> Modified: Update()\n"
    "    Modified --> Unchanged: SaveChanges()\n"
    "    Unchanged --> Deleted: Delete()\n"
    "    Modified --> Deleted: Delete()\n"
    "    Deleted --> Detached: SaveChanges()\n"
    "    Detached --> Detached: Detach()\n"
    "```"
)
results.append(("030-efstate", replace_block(p, "Detached ─", new5)))

p = ROOT / "033-GCGeneration.md"
new6 = (
    "```mermaid\nflowchart TD\n"
    "    MH[Managed Heap]\n"
    "    MH --> G0[Gen 0  small ~16MB-256KB<br/>ephemeral, frequent]\n"
    "    MH --> G1[Gen 1  small ~buffer<br/>ephemeral, less freq]\n"
    "    MH --> G2[Gen 2  large, unbounded<br/>full GC]\n"
    "    MH --> LOH[LOH &gt;=85KB objects<br/>collected with Gen 2]\n"
    "    MH --> POH[POH pinned objects .NET 5+<br/>collected with Gen 2]\n"
    "```"
)
results.append(("033-heap", replace_block(p, "Managed Heap", new6)))

for name, ok in results:
    print(f"{name}: {ok}")
