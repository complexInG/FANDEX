# -*- coding: utf-8 -*-
"""修复 001-getting-started 与 003-git 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

FULL = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full")
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

# 004 冯诺依曼
p = FULL / "001-getting-started/004-ComputerArchitecture.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Mem[存储器]<br/>指令1 指令2 指令3 数据1 数据2\n"
    "    end\n"
    "    Mem -->|取指令| C[控制器<br/>指令寄存器/程序计数器]\n"
    "    Mem -->|读/写数据| A[运算器<br/>累加器/ALU]\n"
    "```"
)
results.append(("004-vonneumann", replace_fence(p, "存储器", new)))

new2 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph CPU[CPU]\n"
    "        C[控制器<br/>PC IR MAR MDR 时序发生器]\n"
    "        A[运算器<br/>ALU 累加器 标志寄存器]\n"
    "        C <-->|内部总线| A\n"
    "    end\n"
    "    CPU -->|外部总线| M[存储器]\n"
    "```"
)
results.append(("004-cpu", replace_fence(p, "CPU", new2)))

new3 = (
    "```mermaid\nflowchart LR\n"
    "    F[取指] --> D[译码] --> E[执行] --> W[写回]\n"
    "    W -->|重复执行| F\n"
    "```"
)
results.append(("004-cycle", replace_fence(p, "取指 ──►", new3)))

new4 = (
    "```mermaid\nflowchart TD\n"
    "    R[CPU 寄存器 ~1ns ~几百B 速度↑] --> C[高速缓存 L1/L2/L3 ~几ns ~几MB]\n"
    "    C --> M[主存 内存 ~100ns ~几GB-几TB]\n"
    "    M --> S[辅存 外存 SSD/HDD ~ms级 ~几TB-几PB 容量↑]\n"
    "```"
)
results.append(("004-memhierarchy", replace_fence(p, "CPU寄存器", new4)))

new5 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant CPU as CPU\n"
    "    participant M as 存储器\n"
    "    CPU->>M: 地址 0x1000（地址总线）\n"
    "    CPU->>M: 读信号（控制总线）\n"
    "    M-->>CPU: 数据 0x5A（数据总线）\n"
    "```"
)
results.append(("004-bus", replace_fence(p, "地址(0x1000)", new5)))

# 006 编程基础流程图
p = FULL / "001-getting-started/006-ProgrammingBasics.md"
new6 = (
    "```mermaid\nflowchart TD\n"
    "    A([开始]) --> B[输入 N]\n"
    "    B --> C[sum = 0]<br/>D[i = 1]\n"
    "    C --> E{i <= N?}\n"
    "    E -- 否 --> F[输出 sum] --> G([结束])\n"
    "    E -- 是 --> H[sum = sum + i]<br/>I[i = i + 1]\n"
    "    H --> E\n"
    "```"
)
results.append(("006-flowchart", replace_fence(p, "开始  │", new6)))

# 007 值传递/引用传递
p = FULL / "001-getting-started/007-FunctionModular.md"
new7 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Before[调用前]\n"
    "        BA[a → [10]]\n"
    "    end\n"
    "    subgraph Call[调用时 值传递]\n"
    "        CA[a → [10]]\n"
    "        X[x → [10] 复制了一份]\n"
    "    end\n"
    "    subgraph After[修改后]\n"
    "        AA[a → [10] 不变]\n"
    "        AX[x → [100] 变了]\n"
    "    end\n"
    "```"
)
results.append(("007-byvalue", replace_fence(p, "调用前", new7)))

new8 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Before[调用前]\n"
    "        BA[a → [3]]\n"
    "        BB[b → [5]]\n"
    "    end\n"
    "    subgraph After[修改后 指针传递]\n"
    "        AA[pa → a → [5]]\n"
    "        AB[pb → b → [3]]\n"
    "    end\n"
    "```"
)
results.append(("007-bypointer", replace_fence(p, "调用前", new8)))

# 011 插件生态
p = FULL / "001-getting-started/011-PluginEcosystem.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    Core[应用核心] --> M[插件管理器]\n"
    "    M --> A[插件A]\n"
    "    M --> B[插件B]\n"
    "    M --> C[插件C]\n"
    "    A --> API[扩展 API]\n"
    "    B --> API\n"
    "    C --> API\n"
    "```"
)
results.append(("011-plugin", replace_fence(p, "应用核心", new9)))

# 014 VCS 集中/分布式
p = FULL / "001-getting-started/014-VCSSelection.md"
new10 = (
    "```mermaid\nflowchart TD\n"
    "    C[中央仓库<br/>trunk / tags / branches] --> D1[开发者A 工作副本]\n"
    "    C --> D2[开发者B 工作副本]\n"
    "    C --> D3[开发者C 工作副本]\n"
    "```"
)
results.append(("014-central", replace_fence(p, "中央仓库", new10)))

new11 = (
    "```mermaid\nflowchart TD\n"
    "    R[远程仓库<br/>main / dev] --> L1[本地仓库A 完整副本]\n"
    "    R --> L2[本地仓库B 完整副本]\n"
    "    R --> L3[本地仓库C 完整副本]\n"
    "```"
)
results.append(("014-distributed", replace_fence(p, "远程仓库", new11)))

# 018 二分调试
p = FULL / "001-getting-started/018-DebugThinking.md"
new12 = (
    "```mermaid\nflowchart TD\n"
    "    P[问题范围] --> B1[第一次二分<br/>问题在左半部分]\n"
    "    B1 --> B2[第二次二分<br/>问题在右半部分]\n"
    "    B2 --> B3[第三次二分<br/>问题在左半部分]\n"
    "    B3 --> L[定位到具体行]\n"
    "```"
)
results.append(("018-bisect", replace_fence(p, "问题范围", new12)))

# 003 Git 状态循环
p = FULL / "003-git/003-GitBasicOperation.md"
new13 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> 未追踪\n"
    "    未追踪 --> 已暂存: git add\n"
    "    已暂存 --> 未修改: git commit\n"
    "    未修改 --> 已修改: 编辑文件\n"
    "    已修改 --> 已暂存: git add\n"
    "    已修改 --> 未追踪: rm/删除文件\n"
    "```"
)
results.append(("003-status", replace_fence(p, "未追踪", new13)))

# 007 对象模型
p = FULL / "003-git/007-ObjectModel.md"
new14 = (
    "```mermaid\nflowchart TD\n"
    "    C[commit] --> T[tree]\n"
    "    T --> B1[blob 文件内容]\n"
    "    T --> B2[blob 文件内容]\n"
    "    T --> T2[tree 子目录]\n"
    "    T2 --> B3[blob]\n"
    "    T2 --> B4[blob]\n"
    "    T --> B5[blob 文件内容]\n"
    "    C --> P[parent commit] --> T3[tree] --> B6[...]\n"
    "```"
)
results.append(("007-objects", replace_fence(p, "commit ──→ tree", new14)))

# 009 三棵树
p = FULL / "003-git/009-ThreeTrees.md"
new15 = (
    "```mermaid\nflowchart LR\n"
    "    W[工作区] -->|git add| S[暂存区] -->|git commit| R[仓库]\n"
    "    W -->|git diff 工作区 vs 暂存区| W\n"
    "    S -->|git diff --staged 暂存区 vs 仓库| S\n"
    "    W -->|git checkout -- file 丢弃工作区修改| W\n"
    "    S -->|git reset HEAD file 取消暂存| S\n"
    "    W -->|git diff HEAD 工作区 vs 仓库<br/>git checkout HEAD -- file 恢复到仓库版本| R\n"
    "```"
)
results.append(("009-threetrees", replace_fence(p, "git add", new15)))

# 021 stash
p = FULL / "003-git/021-GitStash.md"
new16 = (
    "```mermaid\nflowchart TD\n"
    "    W[工作区 有修改] -->|git stash| C[工作区 干净]\n"
    "    W --> S[stash 栈<br/>stash@{2} / stash@{1} / stash@{0} 最新]\n"
    "```"
)
results.append(("021-stash", replace_fence(p, "工作区（有修改）", new16)))

# 022 远程跟踪
p = FULL / "003-git/022-RemoteTrackingBranch.md"
new17 = (
    "```mermaid\nflowchart LR\n"
    "    H[HEAD] --> L[本地分支 main]\n"
    "    L --> R[远程跟踪分支 origin/main<br/>远程仓库 main 分支的本地缓存]\n"
    "```"
)
results.append(("022-tracking", replace_fence(p, "本地分支", new17)))

# 023 GitFlow
p = FULL / "003-git/023-GitFlowGitHubFlow.md"
new18 = (
    "```mermaid\nflowchart LR\n"
    "    M[main] --> R[release/1.0]\n"
    "    D[develop] --> F1[feature/A]\n"
    "    D --> F2[feature/B]\n"
    "    F1 --> D\n"
    "    F2 --> D\n"
    "    R --> M\n"
    "    R --> D\n"
    "```"
)
results.append(("023-gitflow", replace_fence(p, "release/1.0", new18)))

new19 = (
    "```mermaid\nflowchart LR\n"
    "    M[main] --> F1[feature/A]\n"
    "    M --> F2[feature/B]\n"
    "    F1 --> M\n"
    "    F2 --> M\n"
    "```"
)
results.append(("023-ghflow", replace_fence(p, "feature/A", new19)))

new20 = (
    "```mermaid\nflowchart LR\n"
    "    M[main<br/>频繁提交，小步前进<br/>功能开关控制未完成功能]\n"
    "```"
)
results.append(("023-trunk", replace_fence(p, "main ─────────", new20)))

# 036 对比
p = FULL / "003-git/036-GitFlowGitHubFlowComparison.md"
new21 = (
    "```mermaid\nflowchart LR\n"
    "    M[main A-E-H]\n"
    "    D[develop B-C-D-F-G]\n"
    "    F[feature/x C'-D']\n"
    "    R[release/1.0 F'-E']\n"
    "    H2[hotfix H']\n"
    "    D --> M\n"
    "    F --> D\n"
    "    R --> M\n"
    "    R --> D\n"
    "    H2 --> M\n"
    "```"
)
results.append(("036-compare", replace_fence(p, "main:", new21)))

new22 = (
    "```mermaid\nflowchart LR\n"
    "    M[main A-B-C-F-G]\n"
    "    F[feature D-E]\n"
    "    F --> M\n"
    "```"
)
results.append(("036-trunk", replace_fence(p, "main:  A──B", new22)))

# 038 revert/reset
p = FULL / "003-git/038-GitRevertResetComparison.md"
new23 = (
    "```mermaid\nflowchart LR\n"
    "    A[A] --> B[B] --> C[C] --> D[D] --> C2[C' C 的逆向变更]\n"
    "```\n\n"
    "原始历史：A──B──C──D；revert C：A──B──C──D──C'"
)
results.append(("038-revert", replace_fence(p, "原始历史", new23)))

new24 = (
    "```mermaid\nflowchart LR\n"
    "    A[A] --> B[B]\n"
    "    B -.C 和 D 从分支历史中消失.-> X\n"
    "```\n\n"
    "原始历史：A──B──C──D（HEAD → D）；reset B：A──B（HEAD → B）"
)
results.append(("038-reset", replace_fence(p, "原始历史", new24)))

for name, ok in results:
    print(f"{name}: {ok}")
