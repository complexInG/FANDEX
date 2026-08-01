# -*- coding: utf-8 -*-
"""修复剩余 P0 ASCII 图表：精确定位含制表符的围栏。"""

from __future__ import annotations

import pathlib
import re

BOX = re.compile(
    "[\u250c\u2510\u2514\u2518\u251c\u2524\u252c\u2534\u253c\u2500\u2502"
    "\u2554\u2557\u255a\u255d\u2560\u2563\u2566\u2569\u256c\u2550\u2551"
    "\u256d\u256e\u256f\u2570]|\+[-=+]{2,}\+"
)


def replace_fence(path: pathlib.Path, keyword: str, new: str) -> bool:
    """替换包含 keyword 且含制表符的最近围栏。"""
    text = path.read_text(encoding="utf-8")
    idx = text.find(keyword)
    while idx >= 0:
        start = text.rfind("```", 0, idx)
        end = text.find("```", idx)
        if start >= 0 and end > start:
            block = text[start:end]
            if BOX.search(block):
                path.write_text(text[:start] + new + text[end + 3 :], encoding="utf-8")
                return True
        idx = text.find(keyword, idx + 1)
    return False


results = []

# 015-csharp/010: Unity DOTS
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\015-csharp\010-CGameDevUnity.md")
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
results.append(("csharp-010-dots", replace_fence(p, "ECS框架", new)))

# 015-csharp/012: Task 状态机
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\015-csharp\012-AsyncProgrammingDetailed.md")
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
results.append(("csharp-012-task", replace_fence(p, "RanToCompletion", new2)))

# 015-csharp/016: Span 布局
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\015-csharp\016-SpanMemory.md")
new3 = (
    "```mermaid\nflowchart TD\n"
    "    S[Span&lt;T&gt; 内存布局，Total 16 bytes]\n"
    "    S --> R[ref T _reference 8 bytes<br/>指向内存起始]\n"
    "    S --> L[int _length 4 bytes<br/>视图长度]\n"
    "    S --> P[padding 4 bytes<br/>对齐填充]\n"
    "```"
)
results.append(("csharp-016-span", replace_fence(p, "_reference", new3)))

# 018-harmonyos/008: ArkUI 时间线
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\018-harmonyos\008-CustomComponent.md")
new4 = (
    "```mermaid\ntimeline\n"
    "    title ArkUI 版本时间线\n"
    "    2021: ArkUI 1.0 基础装饰器矩阵（@Component/@State/@Prop/@Link）\n"
    "    2022: ArkUI 2.0 状态管理增强（@Watch/@ObjectLink/AppStorage）\n"
    "    2023: ArkUI 3.0 复用与性能（@Reusable/LazyForEach）\n"
    "    2024: ArkUI 4.0 跨端与原子化（@ComponentV2/@AtomicService）\n"
    "```"
)
results.append(("harmony-008-arkui", replace_fence(p, "LazyForEach", new4)))

# 018-harmonyos/022: 测试目录树
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\018-harmonyos\022-TestDebug.md")
new5 = (
    "```mermaid\nflowchart TD\n"
    "    M[main/ets 生产代码] --> MU[utils/Calculator.ets]\n"
    "    M --> MS[services/UserService.ets]\n"
    "    M --> MD[data/UserRepository.ets]\n"
    "    T[test/ets 单元测试] --> TU[utils/Calculator.test.ets]\n"
    "    T --> TS[services/UserService.test.ets]\n"
    "    T --> TD[data/UserRepository.test.ets]\n"
    "    O[ohosTest/ets UI 与集成测试] --> OP[pages/LoginPage.test.ets]\n"
    "```"
)
results.append(("harmony-022-tree", replace_fence(p, "Calculator.ets", new5)))

# 018-harmonyos/029: 权限时间线
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\018-harmonyos\029-PermissionRequest.md")
new6 = (
    "```mermaid\ntimeline\n"
    "    title 权限机制时间线\n"
    "    2019: HarmonyOS 1.0 分级权限雏形（仅 system_grant）\n"
    "    2020: HarmonyOS 2.0 运行时权限引入（user_grant）\n"
    "    2022: HarmonyOS 3.0 权限组、审计日志\n"
    "    2023: HarmonyOS 4.0 分布式权限同步\n"
    "    2024: HarmonyOS NEXT 隐私即设计、权限沙箱\n"
    "```"
)
results.append(("harmony-029-perm", replace_fence(p, "user_grant", new6)))

# 018-harmonyos/031: 迁移时序
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\018-harmonyos\031-CrossDeviceCall.md")
new7 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant A as Device A (source)\n"
    "    participant B as DSoftBus\n"
    "    participant C as Device B (target)\n"
    "    A->>B: 1. continueAbility(deviceId)\n"
    "    Note over A: 2. onSaveData(wantParam)，app serializes state\n"
    "    A->>B: 3. Send state（≤100KB）\n"
    "    B->>C: 4. Forward state\n"
    "    Note over C: 5. onCreate(want)<br/>6. onRestoreData(wantParam)<br/>7. onWindowStageCreate()\n"
    "    C-->>B: 8. Restore complete\n"
    "    B-->>A: 9. onContinueStateChange OK\n"
    "    Note over A: 10. onDestroy（optional）\n"
    "```"
)
results.append(("harmony-031-migrate", replace_fence(p, "onRestoreData", new7)))

for name, ok in results:
    print(f"{name}: {ok}")
