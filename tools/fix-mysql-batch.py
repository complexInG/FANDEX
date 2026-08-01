# -*- coding: utf-8 -*-
"""修复 020-mysql 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\020-mysql")
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

# 001 MySQL 架构分层
p = ROOT / "001-MySQLOverviewDatabaseDesign.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    Conn[客户端连接层 Connection<br/>连接管理、线程池、认证、安全] --> Server[MySQL 服务层 Server<br/>SQL 解析、优化器、缓存、日志]\n"
    "    Server --> SE[存储引擎层 Storage Engine<br/>InnoDB、MyISAM、Memory 等<br/>数据存取、索引管理、事务支持]\n"
    "```"
)
results.append(("001-arch", replace_fence(p, "客户端连接层", new)))

# 008 NDB Cluster
p = ROOT / "008-NDBCluster.md"
new2 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph App[应用层]\n"
    "        N1[SQL Node 1]\n"
    "        N2[SQL Node 2]\n"
    "        N3[SQL Node 3]\n"
    "    end\n"
    "    subgraph Net[NDB Cluster 网络]\n"
    "        D1[Data Node 1]\n"
    "        D2[Data Node 2]\n"
    "        D3[Data Node 3]\n"
    "    end\n"
    "    M[Management Node 管理节点]\n"
    "    N1 --> Net\n"
    "    N2 --> Net\n"
    "    N3 --> Net\n"
    "    M --- Net\n"
    "```"
)
results.append(("008-ndb", replace_fence(p, "SQL  │", new2)))

# 016 JOIN 图解
p = ROOT / "016-SQLFunctionAndAdvancedQuery.md"
new3 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[表A]\n"
    "        A1[1] A2[2] A3[3] A4[4]\n"
    "    end\n"
    "    subgraph B[表B]\n"
    "        B1[A] B2[B] B3[C]\n"
    "    end\n"
    "    A1 --- B1\n"
    "    A2 --- B2\n"
    "    A3 --- B3\n"
    "```\n\n"
    "- 内连接（INNER JOIN）：1, 2, 3（两边都有的）\n"
    "- 左连接（LEFT JOIN）：1, 2, 3, 4（A 全部 + B 匹配的）\n"
    "- 右连接（RIGHT JOIN）：1, 2, 3, A, B, C（B 全部 + A 匹配的）\n"
    "- 全连接（FULL JOIN）：1, 2, 3, 4, A, B, C（两边全部）"
)
results.append(("016-join", replace_fence(p, "内连接 (INNER", new3)))

# 027 四种 JOIN 图解
p = ROOT / "027-MultiTableJoinDetailed.md"
new4 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[表A]\n"
    "        A1[1] A2[2] A3[3] A4[4]\n"
    "    end\n"
    "    subgraph B[表B]\n"
    "        B1[A] B2[B] B3[C]\n"
    "    end\n"
    "    A1 --- B1\n"
    "    A2 --- B2\n"
    "    A3 --- B3\n"
    "```"
)
results.append(("027-inner", replace_fence(p, "表A 表B INNER", new4)))

new5 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[表A]\n"
    "        A1[1] A2[2] A3[3] A4[4]\n"
    "    end\n"
    "    subgraph B[表B]\n"
    "        B1[A] B2[B] B3[C]\n"
    "    end\n"
    "    A1 --- B1\n"
    "    A2 --- B2\n"
    "    A3 --- B3\n"
    "```"
)
results.append(("027-left", replace_fence(p, "表A 表B LEFT", new5)))

new6 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[表A]\n"
    "        A1[1] A2[2]\n"
    "    end\n"
    "    subgraph B[表B]\n"
    "        B1[A] B2[B] B3[C] B4[D]\n"
    "    end\n"
    "    A1 --- B1\n"
    "    A2 --- B2\n"
    "```"
)
results.append(("027-right", replace_fence(p, "表A 表B RIGHT", new6)))

new7 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[表A]\n"
    "        A1[1] A2[2] A3[3]\n"
    "    end\n"
    "    subgraph B[表B]\n"
    "        B1[A] B2[B] B3[C] B4[D]\n"
    "    end\n"
    "    A1 --- B1\n"
    "    A2 --- B2\n"
    "```"
)
results.append(("027-full", replace_fence(p, "表A 表B FULL", new7)))

# 039 JOIN 图解（4 张）
p = ROOT / "039-AdvancedQueryMultiTableOperation.md"
new8 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph A[表A]\n"
    "        A1[1] A2[2] A3[3] A4[4]\n"
    "    end\n"
    "    subgraph B[表B]\n"
    "        B1[A] B2[B] B3[C]\n"
    "    end\n"
    "    A1 --- B1\n"
    "    A2 --- B2\n"
    "    A3 --- B3\n"
    "```"
)
results.append(("039-inner", replace_fence(p, "表A 表B 结果", new8)))
results.append(("039-left", replace_fence(p, "│ 4 │ NULL│", new8)))
results.append(("039-right", replace_fence(p, "│ NULL│ C │", new8)))
results.append(("039-full", replace_fence(p, "│ NULL│ D │", new8)))

# 049 InnoDB 架构
p = ROOT / "049-InnoDBSystemArchitecture.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    Conn[客户端连接层] --> Server[MySQL Server 层<br/>解析器 → 优化器 → 执行器]\n"
    "    Server --> Inno[InnoDB 存储引擎层]\n"
    "    Inno --> BP[Buffer Pool]\n"
    "    Inno --> CB[Change Buffer]\n"
    "    Inno --> AH[Adaptive Hash]\n"
    "    Inno --> LB[Log Buffer]\n"
    "    Inno --> DW[Doublewrite]\n"
    "    Inno --> UT[Undo Tables]\n"
    "    Inno --> FS[文件系统层<br/>.ibd / ibdata1 / ib_logfile0,1]\n"
    "```"
)
results.append(("049-innodb", replace_fence(p, "客户端连接层", new9)))

# 055 主从复制
p = ROOT / "055-ReplicationHA.md"
new10 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant M as 主库 Master\n"
    "    participant S as 从库 Slave\n"
    "    Note over M: 1. 事务提交\n"
    "    M->>S: 2. 写入 binlog\n"
    "    Note over S: 3. IO 线程拉取 binlog<br/>5. 写入 relay log<br/>6. SQL 线程执行 relay log\n"
    "    M-->>M: 4. 返回客户端\n"
    "```"
)
results.append(("055-repl", replace_fence(p, "主库 (Master)", new10)))

new11 = (
    "```mermaid\nflowchart TD\n"
    "    App[Application] --> Router[MySQL Router<br/>读写分离、故障自动切换]\n"
    "    Router --> Cluster[InnoDB Cluster]\n"
    "    Cluster --> P[Primary R/W]\n"
    "    Cluster --> S1[Secondary R/O]\n"
    "    Cluster --> S2[Secondary R/O]\n"
    "    Cluster --> GR[Group Replication]\n"
    "```"
)
results.append(("055-router", replace_fence(p, "MySQL Router", new11)))

new12 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph CS[InnoDB ClusterSet]\n"
    "        subgraph DC1[Primary Cluster DC1]\n"
    "            P[P] S1[S]\n"
    "        end\n"
    "        subgraph DC2[Replica Cluster DC2]\n"
    "            S2[S] S3[S]\n"
    "        end\n"
    "        DC1 -->|异步复制| DC2\n"
    "    end\n"
    "```"
)
results.append(("055-clusterset", replace_fence(p, "Primary Cluster (DC1)", new12)))

# 060 MVCC 行结构
p = ROOT / "060-MVCCSnapshotCurrentRead.md"
new13 = (
    "```mermaid\nflowchart LR\n"
    "    D[数据列 用户数据] --- T[DB_TRX_ID 6字节<br/>最后修改该行的事务ID]\n"
    "    T --- R[DB_ROLL_PTR 7字节<br/>指向 Undo Log 中该行的上一个版本]\n"
    "    R --- W[DB_ROW_ID 6字节<br/>隐藏自增ID 无主键时自动生成]\n"
    "```"
)
results.append(("060-mvcc", replace_fence(p, "DB_TRX_ID", new13)))

# 063 Redo 刷盘
p = ROOT / "063-RedoUndoBinlogWriteTiming.md"
new14 = (
    "```mermaid\nflowchart TD\n"
    "    BP[InnoDB Buffer Pool<br/>脏页 Dirty Pages] -->|刷盘 Checkpoint| RL[Redo Log Files ib_logfile0/1<br/>write pos → checkpoint 之间的区域]<br/>"
    "```"
)
results.append(("063-redo", replace_fence(p, "脏页 (Dirty Pages)", new14)))

new15 = (
    "```mermaid\nflowchart TD\n"
    "    A[1. 写 Undo Log] --> B[2. 写 Redo Log prepare 状态]\n"
    "    B --> C[3. 写 Binlog]\n"
    "    C --> D[4. 写 Redo Log commit 状态]\n"
    "```"
)
results.append(("063-order", replace_fence(p, "写 Undo Log", new15)))

# 064 两阶段提交
p = ROOT / "064-TwoPhaseCommit.md"
new16 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Exec[事务执行阶段]\n"
    "        E1[1. 执行 SQL，修改数据页 Buffer Pool]\n"
    "        E2[2. 生成 Undo Log 写入 Undo Tablespace]\n"
    "        E3[3. 生成 Redo Record 写入 Redo Log Buffer]\n"
    "    end\n"
    "    subgraph Prep[Prepare 阶段]\n"
    "        P1[4. 将 Redo Log Buffer 刷盘 fsync]\n"
    "        P2[5. Redo Log 中标记事务为 XA_PREPARE]\n"
    "        P3[6. 持有行锁，事务对外不可见]\n"
    "    end\n"
    "    subgraph Bin[Binlog 写入阶段]\n"
    "        B1[7. 将 Binlog Cache 写入 Binlog File]\n"
    "        B2[8. 根据 sync_binlog 设置决定是否 fsync]\n"
    "    end\n"
    "    subgraph Com[Commit 阶段]\n"
    "        C1[9. 写 Redo Log commit 标记]\n"
    "        C2[10. 释放行锁，事务对外可见]\n"
    "        C3[11. 释放 Undo Log 标记为可清理]\n"
    "    end\n"
    "    Exec --> Prep --> Bin --> Com\n"
    "```"
)
results.append(("064-2pc", replace_fence(p, "事务执行阶段", new16)))

new17 = (
    "```mermaid\nflowchart LR\n"
    "    A[事务A] --> F[Flush Stage 一次fsync]\n"
    "    B[事务B] --> F\n"
    "    C[事务C] --> F\n"
    "    F --> S[Sync Stage 一次fsync]\n"
    "    S --> K[Commit Stage 顺序commit]\n"
    "```\n\n"
    "阶段1（Flush）：多个事务的 Redo Log 一起 fsync；阶段2（Sync）：多个事务的 Binlog 一起 fsync；阶段3（Commit）：依次标记 commit"
)
results.append(("064-groupcommit", replace_fence(p, "Flush Stage", new17)))

# 066 复制延迟
p = ROOT / "066-ReplicationDelayCauseSolution.md"
new18 = (
    "```mermaid\nflowchart LR\n"
    "    M[主库 Master<br/>Client SQL ↓<br/>Binlog Dump Thread] -->|Binlog 网络传输| S[从库 Slave<br/>Relay Log ↑<br/>I/O Thread<br/>SQL Thread ↑]\n"
    "```"
)
results.append(("066-delay", replace_fence(p, "主库 (Master)", new18)))

# 076 数据库设计 ER
p = ROOT / "076-MySQLProjectExampleDatabaseDesign.md"
new19 = (
    "```mermaid\nerDiagram\n"
    "    users ||--o{ orders : 下单\n"
    "    orders ||--|{ order_items : 包含\n"
    "    orders ||--o{ payments : 支付\n"
    "    users ||--o{ addresses : 拥有\n"
    "    products ||--o{ skus : 规格\n"
    "    products }o--o{ categories : 分类\n"
    "    products }o--o{ brands : 品牌\n"
    "    products }o--o{ attributes : 属性\n"
    "```"
)
results.append(("076-er", replace_fence(p, "orders", new19)))

for name, ok in results:
    print(f"{name}: {ok}")
