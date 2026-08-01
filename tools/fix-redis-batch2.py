# -*- coding: utf-8 -*-
"""第二批 022-redis ASCII 图表修复。"""

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

# 003 Sentinel 拓扑
p = ROOT / "003-ClusterHA.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    S1[Sentinel 1] --> M[主节点]\n"
    "    S2[Sentinel 2] --> M\n"
    "    S3[Sentinel 3] --> M\n"
    "    S1 --> R1[从节点1]\n"
    "    S2 --> R1\n"
    "    S3 --> R2[从节点2]\n"
    "```"
)
results.append(("003-sentinel", replace_fence(p, "Sentinel 2", new)))

# 003 Cluster 分片
new2 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[节点A 0-5460]\n"
    "        MA[Master A]\n"
    "        SA[Slave A1]\n"
    "    end\n"
    "    subgraph B[节点B 5461-10922]\n"
    "        MB[Master B]\n"
    "        SB[Slave B1]\n"
    "    end\n"
    "    subgraph C[节点C 10923-16383]\n"
    "        MC[Master C]\n"
    "        SC[Slave C1]\n"
    "    end\n"
    "    MA --- MB --- MC\n"
    "```\n\n"
    "分片规则：slot = CRC16(key) % 16384，每个主节点负责一部分槽位，Gossip 协议进行节点间通信"
)
results.append(("003-cluster", replace_fence(p, "Master A", new2)))

# 003 分层存储
new3 = (
    "```mermaid\nflowchart TD\n"
    "    DRAM[DRAM 热数据<br/>微秒级延迟<br/>热键、频繁访问的数据] --> SSD[SSD 温/冷数据<br/>亚毫秒级延迟<br/>不常访问的数据]\n"
    "```\n\n"
    "自动分层：LRU 算法决定数据在 DRAM 还是 SSD，成本降低约 80%，延迟 < 500μs"
)
results.append(("003-tier", replace_fence(p, "DRAM（热数据）", new3)))

# 008 Stream 选型树
p = ROOT / "008-Stream.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    Q1{吞吐量需求?} -->|百万级以上| K1[Kafka / Pulsar]\n"
    "    Q1 -->|十万级以内| Q2{是否需要事务消息?}\n"
    "    Q2 -->|是| R1[RocketMQ]\n"
    "    Q2 -->|否| Q3{是否需要复杂路由?}\n"
    "    Q3 -->|是| R2[RabbitMQ]\n"
    "    Q3 -->|否| Q4{是否已有 Redis 基础设施?}\n"
    "    Q4 -->|是| RS[Redis Stream 推荐]\n"
    "    Q4 -->|否| Q5{是否需要多租户/云原生?}\n"
    "    Q5 -->|是| P1[Pulsar]\n"
    "    Q5 -->|否| K2[Kafka 通用大数据场景]\n"
    "```"
)
results.append(("008-mqtree", replace_fence(p, "消息队列选型决策树", new4)))

# 010 RDB fork 流程
p = ROOT / "010-RDBSnapshotPersistence.md"
new5 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant M as 主进程\n"
    "    participant C as 子进程\n"
    "    M->>C: fork()\n"
    "    Note over M: 继续处理请求\n"
    "    Note over C: rdbSave() 写入临时文件<br/>rename() 替换<br/>退出\n"
    "    C-->>M: SIGCHLD\n"
    "    Note over M: 更新 rdb_save_time_last\n"
    "```"
)
results.append(("010-fork", replace_fence(p, "rdbSave()", new5)))

# 010 RDB 文件结构
new6 = (
    "```mermaid\nflowchart LR\n"
    "    R[REDIS 魔数] --> V[version 版本号] --> DB[databases 数据库数据] --> E[EOF 结束标记] --> C[checksum 校验和]\n"
    "```"
)
results.append(("010-rdbfile", replace_fence(p, "REDIS   │", new6)))

new7 = (
    "```mermaid\nflowchart LR\n"
    "    S[SELECTDB 数据库编号] --> KV1[key-value 对<br/>带过期时间] --> KV2[key-value 对<br/>无过期时间]\n"
    "```"
)
results.append(("010-rdbkv", replace_fence(p, "SELECTDB", new7)))

# 012 混合 AOF
p = ROOT / "012-MixedPersistence.md"
new8 = (
    "```mermaid\nflowchart LR\n"
    "    M[混合 AOF 文件] --> R[RDB 格式<br/>全量快照] --> A[AOF 格式<br/>增量命令]\n"
    "```"
)
results.append(("012-mixed2", replace_fence(p, "混合 AOF 文件", new8)))

new9 = (
    "```mermaid\nflowchart TD\n"
    "    A[加载混合 AOF 文件] --> B[读取前 9 字节<br/>判断是否为 RDB 格式]\n"
    "    B -->|纯 AOF| C[逐条重放命令]\n"
    "    B -->|混合格式| D[RDB 加载全量数据]\n"
    "    D --> E[AOF 重放增量命令]\n"
    "    C --> F[加载完成]\n"
    "    E --> F\n"
    "```"
)
results.append(("012-load", replace_fence(p, "加载混合 AOF 文件", new9)))

# 013 无盘复制
p = ROOT / "013-DisklessReplication.md"
new10 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant S1 as 从节点1\n"
    "    participant S2 as 从节点2\n"
    "    participant S3 as 从节点3\n"
    "    participant M as 主节点\n"
    "    S1->>M: 连接，等待 delay 秒\n"
    "    S2->>M: 连接，等待 delay 秒\n"
    "    S3->>M: 连接，等待 delay 秒\n"
    "    Note over M: delay 到期\n"
    "    M->>S1: 一次性发送 RDB\n"
    "    M->>S2: 一次性发送 RDB\n"
    "    M->>S3: 一次性发送 RDB\n"
    "```"
)
results.append(("013-diskless", replace_fence(p, "从节点1 连接", new10)))

# 015 SDS 结构
p = ROOT / "015-StringSDSStructure.md"
new11 = (
    "```mermaid\nflowchart LR\n"
    "    L[len 1字节<br/>5] --> A[alloc 1字节<br/>10] --> F[flags 1字节<br/>s8] --> B[buf[] 11字节 alloc+1<br/>'Hello'] --> Z[\\0 1字节<br/>0]\n"
    "```\n\n"
    "len = 5：已使用 5 字节；alloc = 10：总容量 10 字节（不含 header 和 \\0）；剩余空间 = alloc - len = 5 字节"
)
results.append(("015-sds", replace_fence(p, "sdshdr8", new11)))

# 016 跳表层次
p = ROOT / "016-SkipListAndSortedSet.md"
new12 = (
    "```mermaid\nflowchart LR\n"
    "    L4[Level 4: 1 - 50]\n"
    "    L3[Level 3: 1 - 25 - 50]\n"
    "    L2[Level 2: 1 - 13 - 25 - 38 - 50]\n"
    "    L1[Level 1: 1 - 7 - 13 - 19 - 25 - 31 - 38 - 44 - 50]\n"
    "    L0[Level 0: 1 3 7 9 13 16 19 22 25 28 31 34 38 41 44 47 50]\n"
    "```"
)
results.append(("016-levels", replace_fence(p, "Level 4:", new12)))

new13 = (
    "```mermaid\nflowchart LR\n"
    "    H[header 虚拟头节点 64层]\n"
    "    H --> L3[Level 3: score=1 - score=50]\n"
    "    H --> L2[Level 2: score=1 - score=25 - score=50]\n"
    "    H --> L1[Level 1: 1 - 13 - 25 - 38 - 50]\n"
    "    H --> L0[Level 0: 1 - 7 - 13 - 19 - 25 - 31 - 38 - 50]\n"
    "```\n\n"
    "每个节点的 level 数量随机生成（1-32 层），span 记录到下一节点的跳过节点数，用于计算排名"
)
results.append(("016-skiplist", replace_fence(p, "header (虚拟头节点", new13)))

# 017 repl_backlog
p = ROOT / "017-ReplicationBuffer.md"
new14 = (
    "```mermaid\nflowchart LR\n"
    "    B[repl_backlog 定长环形缓冲区<br/>[cmd1][cmd2][cmd3]...[cmdN]]\n"
    "    B --> H[repl_backlog_histlen 有效数据起始]\n"
    "    B --> I[repl_backlog_idx 写入位置]\n"
    "```\n\n"
    "总大小：repl_backlog_size（默认 1MB）。新数据写入 repl_backlog_idx 位置，写满后环绕到开头覆盖最旧数据"
)
results.append(("017-backlog", replace_fence(p, "repl_backlog_histlen", new14)))

# 018 Sentinel 选举
p = ROOT / "018-SentinelElection.md"
new15 = (
    "```mermaid\nflowchart TD\n"
    "    S1[Sentinel 1] --> M[Master]\n"
    "    S2[Sentinel 2] --> M\n"
    "    S3[Sentinel 3] --> M\n"
    "    M --> R1[Replica1]\n"
    "    M --> R2[Replica2]\n"
    "```"
)
results.append(("018-election", replace_fence(p, "Sentinel 1│", new15)))

# 020 Pipeline
p = ROOT / "020-PipeTransactionAtomic.md"
new16 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as 客户端\n"
    "    participant S as 服务端\n"
    "    C->>S: SET key1 val1\n"
    "    S-->>C: OK\n"
    "    C->>S: SET key2 val2\n"
    "    S-->>C: OK\n"
    "    C->>S: SET key3 val3\n"
    "    S-->>C: OK\n"
    "    Note over C,S: 无 Pipeline：3 RTT\n"
    "```\n\n"
    "有 Pipeline：客户端一次性发送 3 条命令，服务端返回 OK, OK, OK，总计 1 RTT"
)
results.append(("020-pipeline", replace_fence(p, "SET key1 val1", new16)))

# 022 布隆过滤器
p = ROOT / "022-CachePenetrationBreakdownAvalanche.md"
new17 = (
    "```mermaid\nflowchart TD\n"
    "    R[请求] --> BF[布隆过滤器]\n"
    "    BF -->|可能存在| Q[查缓存] --> DB[查数据库]\n"
    "    BF -->|一定不存在| RET[直接返回]\n"
    "```"
)
results.append(("022-bloom", replace_fence(p, "布隆过滤器 →", new17)))

new18 = (
    "```mermaid\nflowchart TD\n"
    "    S1[1. 限流：控制请求速率] --> S2[2. 布隆过滤器：拦截无效请求]\n"
    "    S2 --> S3[3. 本地缓存：L1 缓存]\n"
    "    S3 --> S4[4. Redis 缓存：L2 缓存 随机TTL]\n"
    "    S4 --> S5[5. 互斥锁：防止击穿]\n"
    "    S5 --> S6[6. 熔断降级：保护数据库]\n"
    "    S6 --> S7[7. 数据库：最终数据源]\n"
    "```"
)
results.append(("022-defense", replace_fence(p, "限流：控制请求速率", new18)))

for name, ok in results:
    print(f"{name}: {ok}")
