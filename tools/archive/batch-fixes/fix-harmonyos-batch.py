# -*- coding: utf-8 -*-
"""修复 018-harmonyos 下 ASCII 图表。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\018-harmonyos")


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

# 001: HarmonyOS 版本时间线
p = ROOT / "001-OverviewSetup.md"
new = (
    "```mermaid\ntimeline\n"
    "    title HarmonyOS 版本时间线\n"
    "    2019-08: HarmonyOS 1.0 智慧屏首发、微内核\n"
    "    2020-09: HarmonyOS 2.0 手机适配、开源 OpenHarmony\n"
    "    2022-07: HarmonyOS 3.0 超级终端、原子化服务\n"
    "    2023-08: HarmonyOS 4.0 AI 大模型集成\n"
    "    2024-10: HarmonyOS NEXT 纯血鸿蒙、不兼容 Android\n"
    "```"
)
results.append(("001-version", replace_block(p, "HarmonyOS 1.0 ────", new)))

# 001: shared 依赖
new2 = (
    "```mermaid\nflowchart LR\n"
    "    S[shared] --> E[entry]\n"
    "    S --> F1[feature_A]\n"
    "    S --> F2[feature_B]\n"
    "```"
)
results.append(("001-shared", replace_block(p, "shared ──→ entry", new2)))

# 002 ArkTSArkUI: 装饰器流向
p = ROOT / "002-ArkTSArkUI.md"
new3 = (
    "```mermaid\nflowchart LR\n"
    "    State[@State] --> Prop[@Prop --> 子组件]\n"
    "    State --> Link[@Link <--> 子组件（双向）]\n"
    "    State --> Provide[@Provide --> @Consume（跨层级）]\n"
    "```"
)
results.append(("002-decorators", replace_block(p, "@State ────→ @Prop", new3)))

# 008 CustomComponent: ArkUI 版本时间线
p = ROOT / "008-CustomComponent.md"
new4 = (
    "```mermaid\ntimeline\n"
    "    title ArkUI 版本时间线\n"
    "    2021: ArkUI 1.0 基础装饰器矩阵（@Component/@State/@Prop/@Link）\n"
    "    2022: ArkUI 2.0 状态管理增强（@Watch/@ObjectLink/AppStorage）\n"
    "    2023: ArkUI 3.0 复用与性能（@Reusable/LazyForEach）\n"
    "    2024: ArkUI 4.0 跨端与原子化（@ComponentV2/@AtomicService）\n"
    "```"
)
results.append(("008-arkui", replace_block(p, "基础装饰器矩阵", new4)))

# 011 NetworkRequest: 分层
p = ROOT / "011-NetworkRequest.md"
new5 = (
    "```mermaid\nflowchart TD\n"
    "    UI[UI 层 ArkUI 组件] --> VM[ViewModel 层 @Observed<br/>持有 UI 状态<br/>调用 Repository]\n"
    "    VM --> Repo[Repository 层 数据源抽象<br/>优先读取本地缓存<br/>联网时拉取远端数据<br/>离线时写入待同步队列]\n"
    "    Repo --> LC[LocalCache<br/>RelationalStore]\n"
    "    Repo --> RA[RemoteApi<br/>HttpClient + Retry]\n"
    "```"
)
results.append(("011-network", replace_block(p, "UI 层（ArkUI 组件）", new5)))

# 019 DistributedCapability: 软总线架构
p = ROOT / "019-DistributedCapability.md"
new6 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph App[应用层 Application]\n"
    "        CA[跨设备 Ability]\n"
    "        DD[分布式数据]\n"
    "        DT[分布式任务]\n"
    "        DV[设备虚拟化]\n"
    "    end\n"
    "    subgraph DCF[分布式能力框架层]\n"
    "        SB[分布式软总线 Distributed SoftBus]\n"
    "    end\n"
    "    subgraph TL[传输层 Transport Layer]\n"
    "        W[Wi-Fi]\n"
    "        B[BLE]\n"
    "        E[ETH]\n"
    "        P[Wi-Fi P2P/D2D]\n"
    "    end\n"
    "    CA --> SB\n"
    "    DD --> SB\n"
    "    DT --> SB\n"
    "    DV --> SB\n"
    "    SB --> TL\n"
    "```"
)
results.append(("019-softbus", replace_block(p, "应用层（Application）", new6)))

# 019 迁移时序
new7 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant S as 源设备 d_s\n"
    "    participant T as 目标设备 d_t\n"
    "    S->>T: 1. startAbilityForOptions\n"
    "    Note over T: 2. 创建 Ability 实例\n"
    "    S->>T: 3. continueAbility（Σ_A 序列化）\n"
    "    Note over T: 4. 反序列化、恢复状态\n"
    "    T-->>S: 5. 迁移完成 ACK\n"
    "    Note over S: 6. 本地 Ability 销毁\n"
    "    Note over T: 7. 目标 Ability 激活\n"
    "```"
)
results.append(("019-migrate", replace_block(p, "源设备 d_s", new7)))

# 019 数据对象
new8 = (
    "```mermaid\nflowchart TD\n"
    "    C[协调者设备 智慧屏<br/>维护权威状态<br/>解决冲突]\n"
    "    C -->|DistributedDataObject| A[手机 A<br/>绘制笔迹]\n"
    "    C -->|DistributedDataObject| B[平板 B<br/>绘制笔迹]\n"
    "```"
)
results.append(("019-dataobj", replace_block(p, "协调者设备（智慧屏）", new8)))

# 019 迁移回调
new9 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant S as 源设备 d_s\n"
    "    participant T as 目标设备 d_t\n"
    "    Note over S: 1. onStartContinue() 返回 AGREE\n"
    "    Note over S: 2. onSaveData(reason, params) 返回 Σ_A\n"
    "    S->>T: 3.（软总线传输）\n"
    "    Note over T: 4. onCreate(want)，want.parameters 包含 Σ_A\n"
    "    Note over S: 5. onNewWant(want)\n"
    "    Note over T: 6. onWindowStageCreate()\n"
    "    Note over S: 7. onCompleteContinue(result) 源设备收尾\n"
    "    Note over T: 8. onWindowStageRestore()\n"
    "    Note over S: 9. onContinue() 源设备销毁准备\n"
    "    Note over T: 10. 目标设备 UI 激活\n"
    "```"
)
results.append(("019-callback", replace_block(p, "onStartContinue()", new9)))

# 021 I18n: 资源解析
p = ROOT / "021-I18nAccessibility.md"
new10 = (
    "```mermaid\nflowchart TD\n"
    "    App[应用层 ArkTS / ArkUI<br/>$r('app.string.hello') 调用] --> RM[资源管理器 ResourceManager<br/>读取 locale、colorMode、deviceType<br/>按限定符优先级匹配目录<br/>缓存已匹配资源]\n"
    "    RM --> RD[资源目录 resources/<br/>base / zh_CN / en_US / ar_SA / dark]\n"
    "```"
)
results.append(("021-resource", replace_block(p, "应用层（ArkTS / ArkUI）", new10)))

# 021 无障碍
new11 = (
    "```mermaid\nflowchart TD\n"
    "    AS[无障碍服务<br/>屏幕阅读器 TalkBack 类<br/>开关控制 Switch Access<br/>语音控制 Voice Access]\n"
    "    AS -->|无障碍事件流| AF[无障碍框架 a11y Framework<br/>维护无障碍树<br/>派发事件<br/>执行动作]\n"
    "    AF --> AP[应用层 ArkUI 组件<br/>默认无障碍行为<br/>自定义无障碍属性]\n"
    "```"
)
results.append(("021-a11y", replace_block(p, "无障碍服务（Accessibility", new11)))

# 023 签名时间线
p = ROOT / "023-AppSignaturePublish.md"
new12 = (
    "```mermaid\ntimeline\n"
    "    title 应用签名时间线\n"
    "    2019: HarmonyOS 1.0 RSA 2048 基础签名（仅智慧屏）\n"
    "    2020: HarmonyOS 2.0 Profile 签名 + Debug/Release\n"
    "    2022: HarmonyOS 3.0 多模块打包 + 应用加固\n"
    "    2023: HarmonyOS 4.0 ECDSA 默认 + 密钥轮换\n"
    "    2024: HarmonyOS NEXT 强制 ECDSA + 运行时校验\n"
    "```"
)
results.append(("023-sign", replace_block(p, "基础签名（仅智慧屏）", new12)))

# 024 Stage/FA
p = ROOT / "024-StageFAModelDifference.md"
new13 = (
    "```mermaid\ntimeline\n"
    "    title 应用模型演进时间线\n"
    "    2019: HarmonyOS 1.0 FA 模型唯一\n"
    "    2020: HarmonyOS 2.0 FA + 原子化服务\n"
    "    2022: HarmonyOS 3.0 FA + Stage 并存（Stage 推荐）\n"
    "    2023: HarmonyOS 3.1 Stage API 9 稳定\n"
    "    2023: HarmonyOS 4.0 Stage 默认，FA 收起\n"
    "    2024: HarmonyOS NEXT Stage 唯一，FA 移除\n"
    "```"
)
results.append(("024-stage", replace_block(p, "FA 模型唯一", new13)))

# 029 权限时间线
p = ROOT / "029-PermissionRequest.md"
new14 = (
    "```mermaid\ntimeline\n"
    "    title 权限机制时间线\n"
    "    2019: HarmonyOS 1.0 分级权限雏形（仅 system_grant）\n"
    "    2020: HarmonyOS 2.0 运行时权限引入（user_grant）\n"
    "    2022: HarmonyOS 3.0 权限组、审计日志\n"
    "    2023: HarmonyOS 4.0 分布式权限同步\n"
    "    2024: HarmonyOS NEXT 隐私即设计、权限沙箱\n"
    "```"
)
results.append(("029-permission", replace_block(p, "运行时权限引入", new14)))

# 030 数据管理时间线
p = ROOT / "030-DistributedDataManagement.md"
new15 = (
    "```mermaid\ntimeline\n"
    "    title 分布式数据时间线\n"
    "    2019: HarmonyOS 1.0 distributedData 雏形\n"
    "    2020: HarmonyOS 2.0 KVStore 引入\n"
    "    2022: HarmonyOS 3.0 distributedDataObject + RdbStore\n"
    "    2023: HarmonyOS 4.0 冲突解决 API、端云协同\n"
    "    2024: HarmonyOS NEXT CRDT、数据联邦\n"
    "```"
)
results.append(("030-datatimeline", replace_block(p, "distributedData 雏形", new15)))

# 030 SQLite 表
new16 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Table[本地 SQLite 表]\n"
    "        R1[rowid 1 / id A / data hello / last_modified 1700000000]\n"
    "        R2[rowid 2 / id B / data world / last_modified 1700000005]\n"
    "        R3[rowid 3 / id C / data updated / last_modified 1700000010]\n"
    "    end\n"
    "```"
)
results.append(("030-sqlite", replace_block(p, "本地 SQLite 表", new16)))

# 031 软总线时间线
p = ROOT / "031-CrossDeviceCall.md"
new17 = (
    "```mermaid\ntimeline\n"
    "    title 分布式软总线时间线\n"
    "    2019: HarmonyOS 1.0 DSoftBus 1.0 诞生\n"
    "    2020: HarmonyOS 2.0 DSoftBus 1.5，跨设备 FA 调用\n"
    "    2022: HarmonyOS 3.0 distributedScheduler 引入\n"
    "    2023: HarmonyOS 3.1 Stage 模型稳定，跨设备 UIAbility\n"
    "    2023: HarmonyOS 4.0 DSoftBus 3.0，启动提速 40%\n"
    "    2024: HarmonyOS NEXT 超级终端 2.0，能力联邦\n"
    "```"
)
results.append(("031-bus-timeline", replace_block(p, "跨设备 FA 调用", new17)))

# 031 协议栈
new18 = (
    "```mermaid\nflowchart TD\n"
    "    App[Application Layer<br/>distributedScheduler / KV / File] --> IPC[IPC Session Layer<br/>SoftBus Session / RPC]\n"
    "    IPC --> Trans[Transport Layer<br/>TCP / UDP / BLE GATT]\n"
    "    Trans --> Net[Network Layer<br/>IP / BLE Mesh]\n"
    "    Net --> Link[Link Layer<br/>Wi-Fi / BT / Ethernet]\n"
    "```"
)
results.append(("031-stack", replace_block(p, "Application Layer", new18)))

# 031 迁移时序
new19 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant A as Device A (source)\n"
    "    participant B as DSoftBus\n"
    "    participant C as Device B (target)\n"
    "    A->>B: 1. continueAbility(deviceId)\n"
    "    Note over A: 2. onSaveData(wantParam)，app serializes state\n"
    "    A->>B: 3. Send state（≤100KB）\n"
    "    B->>C: 4. Forward state\n"
    "    Note over C: 5. onCreate(want)<br/>6. onRestoreData(want)<br/>7. onWindowStageCreate()\n"
    "    C-->>B: 8. Restore complete\n"
    "    B-->>A: 9. onContinueStateChange OK\n"
    "    Note over A: 10. onDestroy（optional）\n"
    "```"
)
results.append(("031-migrate", replace_block(p, "Device A (source)", new19)))

# 031 分层详情
new20 = (
    "```mermaid\nflowchart TD\n"
    "    App[Application Layer<br/>distributedScheduler 远程 Ability 调用<br/>distributedKVStore KV 同步<br/>distributedFile 文件同步] --> IPC[IPC Session Layer<br/>SoftBus Session 流式会话<br/>RPC RemoteObject 方法调用<br/>Serialization FlatBuffers]\n"
    "    IPC --> Trans[Transport Layer<br/>TCP 大数据 &gt;100KB<br/>UDP 流媒体<br/>BLE GATT 小数据 &lt;10KB]\n"
    "    Trans --> Net[Network Layer<br/>IP Wi-Fi/Ethernet/Cellular<br/>BLE Mesh]\n"
    "    Net --> Link[Link Layer<br/>Wi-Fi P2P/LAN<br/>Bluetooth BR/BLE<br/>Ethernet<br/>Cellular]\n"
    "```"
)
results.append(("031-layers", replace_block(p, "distributedScheduler (远程", new20)))

# 033 DevEco 时间线
p = ROOT / "033-DevEcoStudioDebugger.md"
new21 = (
    "```mermaid\ntimeline\n"
    "    title DevEco Studio 时间线\n"
    "    2020: DevEco Studio 1.0 基础断点调试\n"
    "    2021: DevEco Studio 2.0 初步 Profiler\n"
    "    2022: DevEco Studio 3.0 CPU/Memory/Network Profiler\n"
    "    2023: DevEco Studio 4.0 HiTrace、分布式调试\n"
    "    2024: DevEco NEXT AI 辅助调试\n"
    "```"
)
results.append(("033-deveco", replace_block(p, "基础断点调试", new21)))

# 033 调试协议栈
new22 = (
    "```mermaid\nflowchart TD\n"
    "    UI[DevEco Studio UI<br/>Debugger/Profiler/Inspector 面板] --> DP[Debug Protocol Layer<br/>DAP Debug Adapter Protocol]\n"
    "    DP --> AT[ArkTS Debug Protocol<br/>V8 Inspector Protocol]\n"
    "    DP --> CP[C++ Debug Protocol<br/>LLDB]\n"
    "    AT --> DT[Device Transport<br/>HDC over USB / TCP]\n"
    "    CP --> DT\n"
    "    DT --> TP[Target Process<br/>ArkTS Engine / Native]\n"
    "```"
)
results.append(("033-debugstack", replace_block(p, "DevEco Studio UI", new22)))

# 033 启动火焰条
new23 = (
    "```mermaid\nflowchart TD\n"
    "    M[main] --> W[onWindowStageCreate]\n"
    "    W --> L[loadContent]\n"
    "    W --> I[init]\n"
    "    L --> P[parseJSON]\n"
    "```"
)
results.append(("033-flame", replace_block(p, "main", new23)))

for name, ok in results:
    print(f"{name}: {ok}")
