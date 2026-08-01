# -*- coding: utf-8 -*-
"""修复剩余模块（networking/iot/arch/agent 等）下 ASCII 图表。"""

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

# 032 networking
p = FULL / "032-networking/001-NetworkBasicsAndProtocol.md"
new = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as 客户端\n"
    "    participant S as 服务器\n"
    "    C->>S: SYN (seq=x) ① 客户端发起连接\n"
    "    S-->>C: SYN+ACK (seq=y, ack=x+1) ② 服务器确认并发起连接\n"
    "    C->>S: ACK (ack=y+1) ③ 客户端确认\n"
    "    Note over C,S: 连接建立\n"
    "```"
)
results.append(("net-001-syn", replace_fence(p, "SYN (seq=x)", new)))

new2 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as 客户端\n"
    "    participant S as 服务器\n"
    "    C->>S: FIN ① 客户端请求关闭\n"
    "    S-->>C: ACK ② 服务器确认\n"
    "    S-->>C: FIN ③ 服务器请求关闭\n"
    "    C->>S: ACK ④ 客户端确认\n"
    "    Note over C,S: 连接关闭\n"
    "```"
)
results.append(("net-001-fin", replace_fence(p, "FIN ─", new2)))

p = FULL / "032-networking/002-NetworkSystemManagement.md"
new3 = (
    "```mermaid\nflowchart TD\n"
    "    C[核心交换机 冗余部署] --> A1[汇聚交换机A] --> SW1[接入SW1]\n"
    "    A1 --> SW2[接入SW2]\n"
    "    C --> A2[汇聚交换机B] --> SW3[接入SW3]\n"
    "    A2 --> SW4[接入SW4]\n"
    "```"
)
results.append(("net-002-topo", replace_fence(p, "核心交换机", new3)))

p = FULL / "032-networking/003-NetworkWiringAndConstruction.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    B[建筑群子系统<br/>园区光缆、室外管道]\n"
    "    E[设备间子系统 机房配线架]\n"
    "    M[管理子系统 楼层配线间]\n"
    "    V[垂直干线子系统<br/>大对数电缆/光缆]\n"
    "    H[水平子系统<br/>双绞线/光纤到桌面]\n"
    "    W[工作区子系统<br/>信息插座/终端设备]\n"
    "    E --> V\n"
    "    M --> V\n"
    "    V --> H\n"
    "    H --> W\n"
    "```"
)
results.append(("net-003-wiring", replace_fence(p, "建筑群子系统", new4)))

p = FULL / "032-networking/004-OSITCPIPModel.md"
new5 = (
    "```mermaid\nflowchart TD\n"
    "    TCP[TCP 报文段<br/>源端口16 / 目标端口16<br/>序列号32 / 确认号32<br/>HL Rsv Flags 窗口大小<br/>校验和16 / 紧急指针16]\n"
    "```"
)
results.append(("net-004-tcp", replace_fence(p, "源端口(16)", new5)))

new6 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as 客户端\n"
    "    participant S as 服务器\n"
    "    C->>S: FIN, seq=u（客户端关闭发送）\n"
    "    S-->>C: ACK, ack=u+1（服务器确认）\n"
    "    Note over S: 服务器继续发送\n"
    "    S-->>C: FIN, seq=w（服务器关闭发送）\n"
    "    C->>S: ACK, ack=w+1（客户端确认）\n"
    "    Note over C: TIME_WAIT 2MSL\n"
    "```"
)
results.append(("net-004-fourway", replace_fence(p, "FIN, seq=u", new6)))

new7 = (
    "```mermaid\nflowchart LR\n"
    "    SP[源端口 16] --- DP[目标端口 16]\n"
    "    L[长度 16] --- CK[校验和 16]\n"
    "```"
)
results.append(("net-004-udp", replace_fence(p, "源端口(16)│目标端口", new7)))

new8 = (
    "```mermaid\nflowchart TD\n"
    "    IP[IP 数据报头<br/>VER IHL TOS 总长度16<br/>标识16 Flags 片偏移13<br/>TTL8 协议8 校验和16<br/>源IP地址32<br/>目标IP地址32]\n"
    "```"
)
results.append(("net-004-ip", replace_fence(p, "VER│IHL", new8)))

p = FULL / "032-networking/005-SwitchingAndRouting.md"
new9 = (
    "```mermaid\nflowchart LR\n"
    "    DM[目的MAC] --- SM[源MAC] --- TP[TPID 8100] --- TC[TCI VLAN ID]\n"
    "```"
)
results.append(("net-005-vlan", replace_fence(p, "目的MAC", new9)))

p = FULL / "032-networking/011-NetworkDesignPlanning.md"
new10 = (
    "```mermaid\nflowchart TD\n"
    "    S1[Spine1] S2[Spine2] S3[Spine3]\n"
    "    L1[Leaf1] L2[Leaf2] L3[Leaf3] L4[Leaf4]\n"
    "    SRV[服务器 服务器 服务器 服务器]\n"
    "    S1 --- L1\n"
    "    S1 --- L2\n"
    "    S1 --- L3\n"
    "    S1 --- L4\n"
    "    S2 --- L1\n"
    "    S2 --- L2\n"
    "    S2 --- L3\n"
    "    S2 --- L4\n"
    "    S3 --- L1\n"
    "    S3 --- L2\n"
    "    S3 --- L3\n"
    "    S3 --- L4\n"
    "    L1 --> SRV\n"
    "    L2 --> SRV\n"
    "    L3 --> SRV\n"
    "    L4 --> SRV\n"
    "```"
)
results.append(("net-011-spine", replace_fence(p, "Spine1", new10)))

# 035 iot
p = FULL / "035-iot/001-OverviewArchitecture.md"
new11 = (
    "```mermaid\nflowchart TD\n"
    "    App[应用层<br/>智能家居/工业监控/智慧城市/智慧农业] --> Plat[平台层<br/>设备管理/规则引擎/数据存储/AI 分析]\n"
    "    Plat --> Net[网络层<br/>MQTT/CoAP/LoRa/NB-IoT/5G/Wi-Fi]\n"
    "    Net --> Per[感知层<br/>传感器/执行器/MCU/嵌入式系统]\n"
    "```"
)
results.append(("iot-001-layers", replace_fence(p, "应用层 (Application", new11)))

new12 = (
    "```mermaid\nflowchart LR\n"
    "    T[终端设备<br/>传感器 执行器<br/>实时控制 毫秒级] --> E[边缘节点<br/>网关/边缘 AI 推理<br/>本地决策 秒级]\n"
    "    E --> C[云平台<br/>大数据分析 模型训练<br/>全局优化 分钟/小时级]\n"
    "```"
)
results.append(("iot-001-edge", replace_fence(p, "终端设备", new12)))

p = FULL / "035-iot/003-CommunicationProtocol.md"
new13 = (
    "```mermaid\nflowchart LR\n"
    "    P[Publisher 传感器] -->|publish| B[Broker 服务器<br/>Topic: iot/sensor/temp] -->|push| S[Subscriber 应用]\n"
    "```"
)
results.append(("iot-003-mqtt", replace_fence(p, "Publisher", new13)))

new14 = (
    "```mermaid\nflowchart LR\n"
    "    D[终端设备] -->|LoRa| G[网关 Gateway] -->|IP| NS[网络服务器 NS]\n"
    "    NS --> AS[应用服务器 AS]\n"
    "    NS --> JS[加入服务器 JS]\n"
    "```"
)
results.append(("iot-003-lora", replace_fence(p, "LoRa", new14)))

p = FULL / "035-iot/004-EdgeComputing.md"
new15 = (
    "```mermaid\nflowchart LR\n"
    "    C[云端<br/>模型训练 全局分析 长期存储<br/>分钟/小时级] <-->|模型/策略| E[边缘层<br/>数据预处理 AI 推理 规则引擎<br/>毫秒/秒级] <-->|采集/控制| D[设备层<br/>传感器 执行器 MCU<br/>实时]\n"
    "```"
)
results.append(("iot-004-edge", replace_fence(p, "云端", new15)))

p = FULL / "035-iot/006-DataProcessingAnalysis.md"
new16 = (
    "```mermaid\nflowchart LR\n"
    "    P[物理实体 设备/系统] -->|实时数据| T[数字孪生 数字模型] -->|分析决策| O[优化控制 指令]\n"
    "    O -->|控制指令| P\n"
    "```"
)
results.append(("iot-006-twin", replace_fence(p, "物理实体", new16)))

p = FULL / "035-iot/007-SecurityAndPrivacy.md"
new17 = (
    "```mermaid\nflowchart TD\n"
    "    T[IoT 安全威胁]\n"
    "    T --> D[设备层威胁<br/>物理攻击 固件篡改 侧信道攻击]\n"
    "    T --> N[网络层威胁<br/>中间人攻击 DDoS 协议攻击]\n"
    "    T --> A[应用层威胁<br/>数据泄露 权限提升 注入攻击]\n"
    "```"
)
results.append(("iot-007-threats", replace_fence(p, "IoT 安全威胁", new17)))

new18 = (
    "```mermaid\nflowchart LR\n"
    "    A[分区A 当前固件 v1.0.0<br/>↑ 活跃] B[分区B 新固件 v1.1.0]\n"
    "```\n\n"
    "更新流程：写入 B → 切换启动 → 验证 → 确认/回滚"
)
results.append(("iot-007-ab", replace_fence(p, "分区 A", new18)))

p = FULL / "035-iot/008-PracticeProject.md"
new19 = (
    "```mermaid\nflowchart LR\n"
    "    D[智能设备<br/>灯/空调 门锁/窗帘] <-->|Wi-Fi/BLE| G[家庭网关 ESP32] -->|MQTT| C[云平台]\n"
    "    C --> M[手机 App]\n"
    "```"
)
results.append(("iot-008-project", replace_fence(p, "智能设备", new19)))

p = FULL / "035-iot/010-CoAP.md"
new20 = (
    "```mermaid\nflowchart TD\n"
    "    App[Application] --> CoAP[CoAP]\n"
    "    CoAP --> DTLS[DTLS] --> UDP[UDP]\n"
    "    UDP --> IP[IPv4/IPv6]\n"
    "    IP --> WP[6LoWPAN]\n"
    "```"
)
results.append(("iot-010-coap", replace_fence(p, "CoAP", new20)))

p = FULL / "035-iot/013-RTThread.md"
new21 = (
    "```mermaid\nflowchart TD\n"
    "    App[应用层] --> Comp[组件层 FinSH/DFS/Net/...]\n"
    "    Comp --> Kern[内核层 线程/IPC/定时器/内存]\n"
    "    Kern --> HW[硬件层 BSP/驱动]\n"
    "```"
)
results.append(("iot-013-rtthread", replace_fence(p, "应用层", new21)))

# 038 software-architecture
p = FULL / "038-software-architecture/001-SoftwareArchitectureOverview.md"
new22 = (
    "```mermaid\nflowchart TD\n"
    "    A[架构师能力模型]\n"
    "    A --> TD[技术深度 对特定领域的深入理解]\n"
    "    A --> TB[技术广度 跨领域的技术视野]\n"
    "    A --> BU[业务理解 将业务需求转化为技术方案]\n"
    "    A --> COM[沟通能力 与不同角色有效沟通]\n"
    "    A --> DEC[决策能力 在不确定性下做出决策]\n"
    "    A --> LDR[领导力 引导团队走向正确方向]\n"
    "```"
)
results.append(("arch-001-skills", replace_fence(p, "技术深度", new22)))

p = FULL / "038-software-architecture/002-LayeredArchitecture.md"
new23 = (
    "```mermaid\nflowchart TD\n"
    "    P[表现层 Presentation<br/>用户界面] --> B[业务层 Business<br/>业务逻辑]\n"
    "    B --> PE[持久层 Persistence<br/>数据访问]\n"
    "    PE --> D[数据库层 Database<br/>数据存储]\n"
    "```"
)
results.append(("arch-002-layers", replace_fence(p, "表现层 (Presentation", new23)))

new24 = (
    "```mermaid\nflowchart LR\n"
    "    P[表现层] --> B[业务层] --> PE[持久层] --> D[数据库]\n"
    "    P -.->|简单查询可跳过业务层| PE\n"
    "```"
)
results.append(("arch-002-flow", replace_fence(p, "表现层 → 业务层", new24)))

p = FULL / "038-software-architecture/004-EventDrivenArchitecture.md"
new25 = (
    "```mermaid\nflowchart TD\n"
    "    E[事件流]<br/>1 AccountCreated {id: A1}<br/>2 MoneyDeposited {amt: 500}<br/>3 MoneyDeposited {amt: 300}<br/>4 MoneyWithdrawn {amt: 100}\n"
    "```"
)
results.append(("arch-004-events", replace_fence(p, "AccountCreated", new25)))

new26 = (
    "```mermaid\nflowchart LR\n"
    "    C[客户端] --> CM[命令模型 写] --> WDB[写数据库]\n"
    "    C --> QM[查询模型 读] --> RDB[读数据库]\n"
    "    WDB -.->|事件同步| QM\n"
    "```"
)
results.append(("arch-004-cqrs", replace_fence(p, "命令模型 (写)", new26)))

new27 = (
    "```mermaid\nflowchart TD\n"
    "    C[命令] --> A[聚合根] --> EV[产生事件] --> ES[事件存储]\n"
    "    ES --> P1[投影1] --> RM1[读模型1]\n"
    "    ES --> P2[投影2] --> RM2[读模型2]\n"
    "    ES --> P3[投影3] --> RM3[读模型3]\n"
    "```"
)
results.append(("arch-004-es", replace_fence(p, "命令 → 聚合根", new27)))

p = FULL / "038-software-architecture/007-DDD.md"
new28 = (
    "```mermaid\nflowchart LR\n"
    "    O[订单上下文<br/>Order OrderItem OrderStatus]\n"
    "    P[商品上下文<br/>Product Category Inventory]\n"
    "    PAY[支付上下文<br/>Payment Transaction Refund]\n"
    "    O <-->|上下文映射| P\n"
    "    O <-->|上下文映射| PAY\n"
    "    P <-->|上下文映射| PAY\n"
    "```"
)
results.append(("arch-007-bc", replace_fence(p, "订单上下文", new28)))

new29 = (
    "```mermaid\nflowchart TD\n"
    "    UI[用户界面/展示层] --> APP[应用层 Application<br/>用例编排]\n"
    "    APP --> DOM[领域层 Domain<br/>核心业务逻辑]\n"
    "    DOM --> INF[基础设施层 Infra<br/>技术实现]\n"
    "```"
)
results.append(("arch-007-ddd", replace_fence(p, "用户界面/展示层", new29)))

# 021 postgresql
p = FULL / "021-postgresql/005-ReplicationHA.md"
new30 = (
    "```mermaid\nflowchart LR\n"
    "    P[主节点 Primary<br/>WAL 发送进程<br/>读写请求] -->|WAL 流| S[备节点 Standby<br/>WAL 接收进程 WAL 回放进程<br/>只读查询]\n"
    "```"
)
results.append(("pg-005-repl", replace_fence(p, "主节点 (Primary)", new30)))

new31 = (
    "```mermaid\nflowchart TD\n"
    "    C[客户端] --> PB[PgBouncer 连接池]\n"
    "    PB --> P1[Patroni Node1 主] --> ETCD[etcd Leader 选举]\n"
    "    PB --> P2[Patroni Node2 备] --> ETCD\n"
    "    PB --> P3[Patroni Node3 备] --> ETCD\n"
    "    C --> HA[HAProxy 自动路由到主节点<br/>:5000 写 主节点<br/>:5001 读 备节点]\n"
    "```"
)
results.append(("pg-005-patroni", replace_fence(p, "PgBouncer", new31)))

p = FULL / "021-postgresql/040-ParallelQuery.md"
new32 = (
    "```mermaid\nflowchart TD\n"
    "    B[Backend Leader<br/>用户连接进程]\n"
    "    B -->|Gather / Gather Merge| W1[Worker 1]<br/>W2[Worker 2]<br/>W3[Worker 3 后台工作进程]\n"
    "```"
)
results.append(("pg-040-parallel", replace_fence(p, "Backend", new32)))

p = FULL / "021-postgresql/041-LogicalPhysicalReplicationCompare.md"
new33 = (
    "```mermaid\nflowchart LR\n"
    "    P[主库 Primary<br/>WAL Sender 进程] -->|WAL 流| S[从库 Standby<br/>WAL Receiver 进程] --> R[Recovery 重放WAL]\n"
    "```"
)
results.append(("pg-041-physical", replace_fence(p, "主库 (Primary)", new33)))

new34 = (
    "```mermaid\nflowchart LR\n"
    "    P[主库 Publisher<br/>WAL Sender 逻辑解码] -->|逻辑变更| S[从库 Subscriber<br/>Apply Worker]\n"
    "```\n\n"
    "发布端：PUBLICATION（定义要发布的表）；订阅端：SUBSCRIPTION（定义从哪个发布端订阅）"
)
results.append(("pg-041-logical", replace_fence(p, "主库 (Publisher", new34)))

# 041 agent
p = FULL / "041-agent/001-AIAgentOverviewArchitecture.md"
new35 = (
    "```mermaid\nflowchart TD\n"
    "    A[AI Agent]\n"
    "    A --> LLM[LLM 大脑<br/>推理/规划/决策]\n"
    "    A --> MEM[记忆系统<br/>短期/长期]\n"
    "    A --> TOOL[工具集<br/>搜索/代码/API]\n"
    "    A --> PLAN[规划模块<br/>任务分解/反思/改进]\n"
    "```"
)
results.append(("agent-001-core", replace_fence(p, "AI Agent", new35)))

new36 = (
    "```mermaid\nflowchart LR\n"
    "    P[感知模块 Perception] --> D[决策模块 Decision]\n"
    "    D --> A[行动模块 Action]\n"
    "    M[记忆 Memory] <--> D\n"
    "    PL[规划 Planning] --> D\n"
    "    A -.->|反馈| P\n"
    "```"
)
results.append(("agent-001-loop", replace_fence(p, "感知模块", new36)))

p = FULL / "041-agent/005-MemoryAndPlanning.md"
new37 = (
    "```mermaid\nflowchart TD\n"
    "    A[Agent 记忆系统]\n"
    "    A --> S[短期记忆 上下文窗口<br/>当前对话 最近操作]\n"
    "    A --> L[长期记忆]<br/>V[向量记忆 语义检索]<br/>K[知识图谱 关系检索]<br/>ST[结构化存储 KV/SQL]\n"
    "```"
)
results.append(("agent-005-memory", replace_fence(p, "Agent 记忆系统", new37)))

p = FULL / "041-agent/006-Agent.md"
new38 = (
    "```mermaid\nflowchart TD\n"
    "    M[多 Agent 协作模式]\n"
    "    M --> SEQ[顺序协作 Pipeline]\n"
    "    M --> PAR[并行协作 Parallel]\n"
    "    M --> V[辩论/投票 Debate/Vote]\n"
    "    M --> H[层级协作 Hierarchy]\n"
    "    M --> G[群聊协作 GroupChat]\n"
    "    M --> HY[混合模式 Hybrid]\n"
    "```"
)
results.append(("agent-006-modes", replace_fence(p, "多 Agent 协作模式", new38)))

new39 = (
    "```mermaid\nflowchart TD\n"
    "    MG[Manager<br/>决策、分配、审核]\n"
    "    MG --> A1[Agent1 执行具体任务]\n"
    "    MG --> A2[Agent2 执行具体任务]\n"
    "    MG --> A3[Agent3 执行具体任务]\n"
    "```"
)
results.append(("agent-006-hierarchy", replace_fence(p, "Manager", new39)))

new40 = (
    "```mermaid\nflowchart LR\n"
    "    A1[Agent1] <--> A2[Agent2] <--> A3[Agent3]\n"
    "    A1 <--> B[共享消息板]\n"
    "    A2 <--> B\n"
    "    A3 <--> B\n"
    "```"
)
results.append(("agent-006-group", replace_fence(p, "Agent1", new40)))

p = FULL / "041-agent/007-Agent.md"
new41 = (
    "```mermaid\nflowchart TD\n"
    "    T[Agent 安全威胁]\n"
    "    T --> P[Prompt 注入 直接/间接]\n"
    "    T --> J[越狱攻击 绕过安全限制]\n"
    "    T --> D[数据泄露 敏感信息]\n"
    "    T --> A[工具滥用 未授权操作]\n"
    "    T --> S[供应链攻击 恶意工具]\n"
    "    T --> R[拒绝服务 资源耗尽]\n"
    "```"
)
results.append(("agent-007-threats", replace_fence(p, "Agent 安全威胁", new41)))

p = FULL / "041-agent/008-PracticeProject.md"
new42 = (
    "```mermaid\nflowchart TD\n"
    "    U[用户消息] --> I[意图识别] --> R[路由分发]\n"
    "    R --> F[FAQ 回答]\n"
    "    R --> T[工单创建]\n"
    "    R --> H[人工转接]\n"
    "    F --> RE[回复用户]\n"
    "    T --> RE\n"
    "    H --> RE\n"
    "```"
)
results.append(("agent-008-router", replace_fence(p, "用户消息", new42)))

new43 = (
    "```mermaid\nflowchart LR\n"
    "    F[前端 Vue3] --> G[API 网关 Nginx] --> A[Agent 服务 FastAPI] --> L[LLM API OpenAI]\n"
    "    A --> R[Redis 缓存]\n"
    "    A --> C[Chroma 向量库]\n"
    "    A --> M[MySQL 持久化]\n"
    "```"
)
results.append(("agent-008-arch", replace_fence(p, "前端", new43)))

p = FULL / "041-agent/010-MCPA2A.md"
new44 = (
    "```mermaid\nflowchart LR\n"
    "    A[Agent A] <-->|A2A| B[Agent B] <-->|A2A| C[Agent C]\n"
    "    A -->|MCP| TA[工具/DB]\n"
    "    B -->|MCP| TB[工具/DB]\n"
    "    C -->|MCP| TC[工具/DB]\n"
    "```"
)
results.append(("agent-010-ecosystem", replace_fence(p, "Agent 生态协议层", new44)))

new45 = (
    "```mermaid\nflowchart LR\n"
    "    H[MCP Host Agent/LLM] <-->|协议| S[MCP Server 工具提供方]\n"
    "    H --> C[MCP Client 协议客户端]\n"
    "    S --> R[本地/远程资源]\n"
    "```"
)
results.append(("agent-010-mcp", replace_fence(p, "MCP 架构", new45)))

new46 = (
    "```mermaid\nflowchart LR\n"
    "    O[协调 Agent Orchestrator] <-->|A2A 委派任务| R[研究 Agent Researcher]\n"
    "    O -->|MCP| FS[文件系统/数据库]\n"
    "    R -->|MCP| SE[搜索引擎/论文库]\n"
    "```\n\n"
    "协调 Agent 通过 A2A 委派任务给研究 Agent，各 Agent 通过 MCP 访问各自的工具和数据源"
)
results.append(("agent-010-coop", replace_fence(p, "MCP + A2A 协同架构", new46)))

for name, ok in results:
    print(f"{name}: {ok}")
