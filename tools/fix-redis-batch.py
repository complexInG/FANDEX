# -*- coding: utf-8 -*-
"""修复 022-redis 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\022-redis")
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

p = ROOT / "001-OverviewCoreDataStructure.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    Top[最高层] --> L2a[第2层] --> L1a[第1层]\n"
    "    L2a --> L2b[第2层节点] --> L1b[第1层节点]\n"
    "    L2b --> L2c[第2层节点] --> L1c[第1层节点]\n"
    "```\n\n"
    "平均查询复杂度：O(logN)，空间复杂度：O(N)"
)
results.append(("001-zset", replace_fence(p, "最高层", new)))

p = ROOT / "002-PersistenceModule.md"
new2 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant M as 主进程\n"
    "    participant C as 子进程\n"
    "    M->>C: fork()\n"
    "    Note over M: 继续处理请求（写时复制 COW）\n"
    "    Note over C: 写入临时 RDB 文件\n"
    "    C-->>M: 信号通知（写入完成）\n"
    "    Note over M: 替换旧 RDB 文件\n"
    "```"
)
results.append(("002-bgsave", replace_fence(p, "fork()──→", new2)))

new3 = (
    "```mermaid\nflowchart TD\n"
    "    RDB[RDB 格式数据（前半）<br/>快速加载] --> AOF[AOF 增量命令（后半）<br/>完整数据]\n"
    "```"
)
results.append(("002-mixed", replace_fence(p, "RDB 格式数据（前半）", new3)))

p = ROOT / "003-ClusterHA.md"
new4 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant S as 从节点\n"
    "    participant M as 主节点\n"
    "    S->>M: PSYNC ? -1\n"
    "    M-->>S: +FULLRESYNC runid offset\n"
    "    M-->>S: RDB 数据\n"
    "    M-->>S: 积压缓冲区数据\n"
    "    Note over S: 加载 RDB → 数据一致\n"
    "```"
)
results.append(("003-fullsync", replace_fence(p, "PSYNC ? -1", new4)))

new5 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant S as 从节点\n"
    "    participant M as 主节点\n"
    "    S->>M: PSYNC runid offset\n"
    "    alt offset 在 repl_backlog 中\n"
    "        M-->>S: 差异数据（增量同步）\n"
    "    else offset 不在积压缓冲区\n"
    "        Note over S, M: 执行全量同步\n"
    "    end\n"
    "```"
)
results.append(("003-incsyc", replace_fence(p, "PSYNC runid offset", new5)))

for name, ok in results:
    print(f"{name}: {ok}")
