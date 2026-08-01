# -*- coding: utf-8 -*-
"""修复 017-lua 下 ASCII 图表。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\017-lua")


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

p = ROOT / "004-FunctionAndClosure.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    U[upvalue u] --> F[closure f]\n"
    "    U --> G[closure g]\n"
    "```"
)
results.append(("004-closure", replace_block(p, "upvalue u", new)))

p = ROOT / "015-LuaRedisScript.md"
new2 = (
    "```mermaid\nflowchart LR\n"
    "    A1[应用节点 1] --> R[Redis 集群（分片）]\n"
    "    A2[应用节点 2] --> R\n"
    "    AN[应用节点 N] --> R\n"
    "```"
)
results.append(("015-redis", replace_block(p, "应用节点 1", new2)))

p = ROOT / "026-CoroutineNonPreemptiveScheduling.md"
new3 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> suspended\n"
    "    suspended --> running: resume()\n"
    "    running --> suspended: yield()\n"
    "    running --> dead: return\n"
    "    suspended --> dead: close()\n"
    "    dead --> [*]\n"
    "```"
)
results.append(("026-state", replace_block(p, "suspended │", new3)))

new4 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant Main as 主协程\n"
    "    participant Sub as 被调协程\n"
    "    Main->>Sub: resume(a, b)\n"
    "    Note over Sub: 执行\n"
    "    Sub-->>Main: yield(c, d)\n"
    "    Note over Sub: 暂停\n"
    "    Main->>Sub: resume(e, f)\n"
    "    Note over Sub: 恢复，yield 返回 e, f\n"
    "    Sub-->>Main: return(g)\n"
    "    Note over Sub: dead\n"
    "```"
)
results.append(("026-seq", replace_block(p, "主协程             被调协程", new4)))

new5 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> suspended\n"
    "    suspended --> running: resume()\n"
    "    running --> suspended: yield()\n"
    "    running --> dead: return\n"
    "    suspended --> dead: close()\n"
    "    dead --> [*]\n"
    "```"
)
results.append(("026-state2", replace_block(p, "suspended  │", new5)))

new6 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant Main as main coroutine\n"
    "    participant Sub as sub coroutine\n"
    "    Main->>Sub: resume(co, a, b)（首次作为函数参数，后续作为 yield 返回值）\n"
    "    Note over Sub: 执行...\n"
    "    Sub-->>Main: yield(c, d)（resume 返回 true, c, d）\n"
    "    Note over Sub: 暂停\n"
    "    Main->>Sub: resume(co, e, f)（e, f 作为 yield 返回值）\n"
    "    Note over Sub: 恢复执行\n"
    "    Sub-->>Main: return(g)（resume 返回 true, g）\n"
    "    Note over Sub: dead\n"
    "```"
)
results.append(("026-seq2", replace_block(p, "main coroutine", new6)))

for name, ok in results:
    print(f"{name}: {ok}")
