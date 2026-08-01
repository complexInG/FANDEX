# -*- coding: utf-8 -*-
"""修复 052-big-data 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\052-big-data")
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

# 001 大数据时间线
p = ROOT / "001-DataOverview.md"
new = (
    "```mermaid\ntimeline\n"
    "    title 大数据发展时间线\n"
    "    2003: Google GFS 论文发布\n"
    "    2004: Google MapReduce 论文发布\n"
    "    2006: Hadoop 项目启动（Doug Cutting），大数据概念正式提出\n"
    "    2008: Hadoop 成为 Apache 顶级项目\n"
    "    2010: Spark 项目启动（UC Berkeley AMPLab）\n"
    "    2012: Hadoop 2.0（YARN）发布\n"
    "    2014: Spark 成为 Apache 顶级项目，Flink 项目孵化\n"
    "    2016: 数据湖概念兴起\n"
    "    2018: 流批一体架构成为趋势\n"
    "    2020: Lakehouse 架构提出\n"
    "    2022+: 实时湖仓、AI+大数据深度融合\n"
    "```"
)
results.append(("001-timeline", replace_fence(p, "Google GFS", new)))

# 001 技术栈分层
new2 = (
    "```mermaid\nflowchart TD\n"
    "    App[数据应用层<br/>BI报表 / 数据挖掘 / 机器学习 / 实时监控 / 推荐系统] --> Calc[计算引擎层<br/>MapReduce / Spark / Flink / Presto / ClickHouse]\n"
    "    Calc --> Store[数据存储层<br/>HDFS / HBase / Kafka / Cassandra / Elasticsearch]\n"
    "    Store --> Integ[数据集成层<br/>Sqoop / Flume / Kafka Connect / Debezium / Airflow]\n"
    "    Integ --> Coord[协调与管理层<br/>Zookeeper / YARN / Oozie / Kubernetes]\n"
    "    Coord --> Gov[数据治理层<br/>Hive Metastore / Atlas / Ranger / DataHub]\n"
    "```"
)
results.append(("001-stack", replace_fence(p, "数据应用层", new2)))

# 001 Lambda 架构
new3 = (
    "```mermaid\nflowchart LR\n"
    "    SRC[数据源] --> B[Batch Layer HDFS+Spark<br/>全量数据批处理]\n"
    "    SRC --> S[Speed Layer Kafka+Flink<br/>实时增量处理]\n"
    "    B --> M[合并] --> Q[查询服务]\n"
    "    S --> M\n"
    "```"
)
results.append(("001-lambda", replace_fence(p, "Batch Layer", new3)))

# 002 HDFS 架构
p = ROOT / "002-HDFSDistributedFileSystem.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    C[Client] --> NN1[NameNode Active<br/>FsImage / EditLog<br/>元数据管理 / 块映射管理]\n"
    "    C --> NN2[NameNode Standby<br/>FsImage / EditLog<br/>元数据同步 / 故障接管]\n"
    "    NN1 <-->|JournalNodes| NN2\n"
    "    NN1 --> DN1[DataNode1<br/>Block A B C]\n"
    "    NN1 --> DN2[DataNode2<br/>Block A C D]\n"
    "    NN1 --> DN3[DataNode3<br/>Block A B D]\n"
    "```"
)
results.append(("002-hdfs", replace_fence(p, "NameNode (Active)", new4)))

# 002 写入管线
new5 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as Client\n"
    "    participant N as NameNode\n"
    "    participant D1 as DataNode1\n"
    "    participant D2 as DataNode2\n"
    "    participant D3 as DataNode3\n"
    "    C->>N: create /path/file\n"
    "    N-->>C: block locations\n"
    "    C->>D1: write packet\n"
    "    D1->>D2: forward\n"
    "    D2->>D3: forward\n"
    "    D3-->>D1: ack\n"
    "    D1-->>C: ack pipeline\n"
    "    C->>N: close file\n"
    "    N-->>C: complete\n"
    "```"
)
results.append(("002-write", replace_fence(p, "create /path/file", new5)))

# 002 HA 架构
new6 = (
    "```mermaid\nflowchart TD\n"
    "    ZK[ZooKeeper 集群<br/>Leader 选举]\n"
    "    ZK --> Z1[ZKFC Active]\n"
    "    ZK --> JQ[JournalNode Quorum]\n"
    "    ZK --> Z2[ZKFC Standby]\n"
    "    Z1 --> NN1[Active NameNode]\n"
    "    JQ -->|EditLog| NN1\n"
    "    JQ -->|EditLog| NN2[Standby NameNode]\n"
    "    Z2 --> NN2\n"
    "```"
)
results.append(("002-ha", replace_fence(p, "ZooKeeper 集群", new6)))

# 003 MapReduce
p = ROOT / "003-MapReduce.md"
new7 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Map[Map端]\n"
    "        MO[Map 输出] --> MP[Partition 按Key分区]\n"
    "        MP --> MS[Sort 内存排序]\n"
    "        MS --> MSp[Spill 溢写到磁盘]\n"
    "        MSp --> MM[Merge 合并溢写文件]\n"
    "    end\n"
    "    subgraph Reduce[Reduce端]\n"
    "        RC[Copy 从Map端拉取数据] --> RM[Merge 合并排序]\n"
    "        RM --> RG[Group 按Key分组]\n"
    "        RG --> RR[Reduce 调用Reduce函数]\n"
    "    end\n"
    "    MM -->|网络传输| RC\n"
    "```"
)
results.append(("003-mr", replace_fence(p, "Map端", new7)))

new8 = (
    "```mermaid\nflowchart LR\n"
    "    M1[Map: hello,1 ×3] -->|网络| R1[Reduce: hello,[1,1,1] → hello,3]\n"
    "    M2[Map: hello,1 ×3] --> C2[Combiner: hello,3] -->|网络| R2[Reduce: hello,[3] → hello,3]\n"
    "```"
)
results.append(("003-combiner", replace_fence(p, "无Combiner", new8)))

# 004 SparkCore
p = ROOT / "004-SparkCore.md"
new9 = (
    "```mermaid\nflowchart LR\n"
    "    A[RDD_A] -->|map| B[RDD_B] -->|filter| C[RDD_C] -->|reduceByKey| D[RDD_D]\n"
    "    C -.->|分区丢失时从 RDD_C 重新计算| C\n"
    "```"
)
results.append(("004-rdd", replace_fence(p, "RDD_A ──map", new9)))

new10 = (
    "```mermaid\nflowchart TD\n"
    "    D[Driver<br/>SparkContext / SparkSession<br/>DAGScheduler → TaskScheduler]\n"
    "    D --> E1[Executor<br/>Task1 Task2 Cache]\n"
    "    D --> E2[Executor<br/>Task3 Task4 Cache]\n"
    "    D --> E3[Executor<br/>Task5 Task6 Cache]\n"
    "```"
)
results.append(("004-driver", replace_fence(p, "Driver", new10)))

# 005 SparkStreaming
p = ROOT / "005-SparkStreaming.md"
new11 = (
    "```mermaid\nflowchart TD\n"
    "    S[实时数据流] --> B[t1批次 [0-1s] → RDD1]\n"
    "    S --> B2[t2批次 [1-2s] → RDD2]\n"
    "    S --> B3[t3批次 [2-3s] → RDD3]\n"
    "    S --> B4[t4批次 [3-4s] → RDD4]\n"
    "```"
)
results.append(("005-batches", replace_fence(p, "实时数据流", new11)))

new12 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Input[无界输入表]\n"
    "        R1[key A value 10 timestamp 10:00:01 批次1]\n"
    "        R2[key B value 20 timestamp 10:00:02]\n"
    "        R3[key A value 30 timestamp 10:00:03 批次2]\n"
    "        R4[key C value 40 timestamp 10:00:04]\n"
    "        R5[... 持续追加]\n"
    "    end\n"
    "    Input -->|查询| Result[结果表 Result Table]\n"
    "```"
)
results.append(("005-table", replace_fence(p, "无界输入表", new12)))

# 006 Hive
p = ROOT / "006-HiveDataWarehouse.md"
new13 = (
    "```mermaid\nflowchart TD\n"
    "    UI[用户接口层<br/>CLI / Beeline / JDBC-ODBC / Web UI] --> D[驱动层<br/>Compiler / Optimizer / Executor]\n"
    "    D --> M[元数据层<br/>Metastore MySQL/PostgreSQL]\n"
    "    M --> SC[存储与计算层<br/>HDFS / MapReduce / Spark / Tez]\n"
    "```"
)
results.append(("006-hive", replace_fence(p, "用户接口层", new13)))

# 007 HBase
p = ROOT / "007-HBaseDatabase.md"
new14 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph CF1[CF1]\n"
    "        R1a[col1:t2 val3]\n"
    "        R1b[col2:t1 val1]\n"
    "    end\n"
    "    subgraph CF2[CF2]\n"
    "        R2a[col1:t1 val2]\n"
    "    end\n"
    "    RK[RowKey row1] --- CF1\n"
    "    RK --- CF2\n"
    "```"
)
results.append(("007-rowkey", replace_fence(p, "RowKey    CF1", new14)))

new15 = (
    "```mermaid\nflowchart TD\n"
    "    C[Client]\n"
    "    M[HMaster<br/>表/Region管理 负载均衡 元数据维护]\n"
    "    Z[ZooKeeper<br/>Master选举 Region定位 集群状态]\n"
    "    C --> M\n"
    "    C --> Z\n"
    "    M --> R1[RegionServer1<br/>Region A,B]\n"
    "    M --> R2[RegionServer2<br/>Region C,D]\n"
    "    M --> R3[RegionServer3<br/>Region E,F]\n"
    "```"
)
results.append(("007-hbase", replace_fence(p, "HMaster", new15)))

# 008 Kafka
p = ROOT / "008-KafkaMessageQueue.md"
new16 = (
    "```mermaid\nflowchart TD\n"
    "    Z[ZooKeeper / KRaft<br/>元数据管理 / Controller 选举]\n"
    "    B0[Broker 0<br/>P0-L P2-F]\n"
    "    B1[Broker 1<br/>P0-F P2-L]\n"
    "    B2[Broker 2<br/>P1-L P3-L]\n"
    "    B3[Broker 3<br/>P1-F P3-F]\n"
    "    P1[Prod-1] --> B0\n"
    "    P2[Prod-2] --> B1\n"
    "    C1[Cons-1] <--> B2\n"
    "    C2[Cons-2] <--> B3\n"
    "    Z --- B0\n"
    "    Z --- B1\n"
    "    Z --- B2\n"
    "    Z --- B3\n"
    "```"
)
results.append(("008-kafka", replace_fence(p, "ZooKeeper / KRaft", new16)))

# 009 Flink
p = ROOT / "009-FlinkStreamHandling.md"
new17 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph JM[JobManager]\n"
    "        D[Dispatcher] RM[ResourceManager]\n"
    "        JMA[JobMaster 每个Job一个<br/>ExecutionGraph / CheckpointCoordinator]\n"
    "    end\n"
    "    TM1[TaskManager<br/>Slot 0 1<br/>Task A B]\n"
    "    TM2[TaskManager<br/>Slot 0 1<br/>Task C D]\n"
    "    TM3[TaskManager<br/>Slot 0 1<br/>Task E F]\n"
    "    JM --> TM1\n"
    "    JM --> TM2\n"
    "    JM --> TM3\n"
    "```"
)
results.append(("009-jm", replace_fence(p, "JobManager", new17)))

new18 = (
    "```mermaid\ntimeline\n"
    "    title Flink 窗口类型\n"
    "    滚动窗口: Tumbling Window，固定 5s 无缝衔接\n"
    "    滑动窗口: Sliding Window，固定 5s 长度 + 滑动步长\n"
    "    会话窗口: Session Window，按 gap 切分\n"
    "    全局窗口: Global Window，无限窗口\n"
    "```"
)
results.append(("009-windows", replace_fence(p, "滚动窗口", new18)))

new19 = (
    "```mermaid\nflowchart LR\n"
    "    E1[e1 3] E2[e2 5] E3[e3 4] E4[e4 8] E5[e5 7] E6[e6 10]\n"
    "    T[时间轴 3 4 5 6 7 8 9 10]\n"
    "    W[水位线 W=3 W=4 W=5 W=7 W=8 W=10]\n"
    "    E1 --> T\n"
    "    E2 --> T\n"
    "    E3 --> T\n"
    "    E4 --> T\n"
    "    E5 --> T\n"
    "    E6 --> T\n"
    "    T --> W\n"
    "```"
)
results.append(("009-watermark", replace_fence(p, "事件时间轴", new19)))

new20 = (
    "```mermaid\nflowchart LR\n"
    "    S1[Source-1] -->|B1 Barrier| M[Map] -->|B1 Barrier| K[Sink]\n"
    "    S2[Source-2] -->|B1 Barrier| M\n"
    "```\n\n"
    "所有算子收到 Barrier 后保存状态快照"
)
results.append(("009-checkpoint", replace_fence(p, "Source-1 ──→ Map", new20)))

# 010 DataLake
p = ROOT / "010-DataLake.md"
new21 = (
    "```mermaid\nflowchart TD\n"
    "    Cat[Catalog<br/>当前元数据指针 metadata file 路径]\n"
    "    ML[Metadata Layer<br/>metadata.json v2<br/>schema / partition-spec / sort-order / snapshot 列表<br/>manifest-list snap-xxx.avro<br/>manifest-file xxx-m0.avro 含 data-file 统计信息]\n"
    "    DL[Data Layer<br/>Parquet / ORC / Avro 数据文件]\n"
    "    Cat --> ML --> DL\n"
    "```"
)
results.append(("010-iceberg", replace_fence(p, "Catalog", new21)))

new22 = (
    "```mermaid\nflowchart TD\n"
    "    L[_delta_log/<br/>000...000.json 事务日志<br/>000...001.json<br/>000...003.checkpoint.parquet 检查点]\n"
    "    D[数据文件 Parquet<br/>part-00000-xxx.snappy.parquet<br/>part-00001-xxx.snappy.parquet]\n"
    "    L --> D\n"
    "```"
)
results.append(("010-delta", replace_fence(p, "_delta_log", new22)))

# 011 Zookeeper
p = ROOT / "011-Zookeeper.md"
new23 = (
    "```mermaid\nflowchart TD\n"
    "    C[Client]\n"
    "    L[Leader<br/>读写<br/>事务处理]\n"
    "    F1[Follower<br/>读+转发<br/>投票参与]\n"
    "    F2[Follower<br/>读+转发<br/>投票参与]\n"
    "    Q[Quorum<br/>过半协议]\n"
    "    C --> L\n"
    "    C --> F1\n"
    "    C --> F2\n"
    "    L --> Q\n"
    "    F1 --> Q\n"
    "    F2 --> Q\n"
    "```"
)
results.append(("011-zk", replace_fence(p, "Client", new23)))

new24 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> LOOKING\n"
    "    LOOKING --> FOLLOWING: 选举完成\n"
    "    LOOKING --> LEADING: 成为 Leader\n"
    "```"
)
results.append(("011-zkstate", replace_fence(p, "LOOKING", new24)))

# 012 YARN
p = ROOT / "012-YARNManagement.md"
new25 = (
    "```mermaid\nflowchart TD\n"
    "    RM[ResourceManager<br/>Scheduler 调度器<br/>ApplicationsManager 应用管理器]\n"
    "    N1[NodeManager<br/>Container AppMgr]\n"
    "    N2[NodeManager<br/>Container AppMgr]\n"
    "    N3[NodeManager<br/>Container]\n"
    "    N4[NodeManager<br/>Container]\n"
    "    RM --> N1\n"
    "    RM --> N2\n"
    "    RM --> N3\n"
    "    RM --> N4\n"
    "```"
)
results.append(("012-yarn", replace_fence(p, "ResourceManager", new25)))

new26 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as Client\n"
    "    participant RM as ResourceManager\n"
    "    participant AM as ApplicationMaster\n"
    "    participant NM as NodeManager\n"
    "    C->>RM: 提交应用\n"
    "    RM->>NM: 分配 AM 容器\n"
    "    NM->>AM: 启动 AM\n"
    "    AM->>RM: 注册并申请资源\n"
    "    RM-->>AM: 分配 Container\n"
    "    AM->>NM: 通知启动 Task\n"
    "    Note over NM: Task 运行\n"
    "    AM->>RM: 注销\n"
    "```"
)
results.append(("012-app", replace_fence(p, "Client → RM", new26)))

new27 = (
    "```mermaid\nflowchart TD\n"
    "    RQ[Root Queue]\n"
    "    RQ --> DEV[dev 60%<br/>d1 d2]\n"
    "    RQ --> TST[test 20%]\n"
    "    RQ --> PRD[prod 20%]\n"
    "```"
)
results.append(("012-queue", replace_fence(p, "Root Queue", new27)))

new28 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> NEW\n"
    "    NEW --> LOCALIZED\n"
    "    LOCALIZED --> RUNNING\n"
    "    RUNNING --> EXITED\n"
    "    EXITED --> DONE\n"
    "    RUNNING --> KILLED\n"
    "    KILLED --> DONE\n"
    "```"
)
results.append(("012-container", replace_fence(p, "NEW → LOCALIZED", new28)))

new29 = (
    "```mermaid\nflowchart TD\n"
    "    RMA[RM Active<br/>处理客户端请求]\n"
    "    RMS[RM Standby<br/>接收状态同步]\n"
    "    Z[ZooKeeper<br/>Leader 选举]\n"
    "    RMA --> Z\n"
    "    RMS --> Z\n"
    "```"
)
results.append(("012-rmha", replace_fence(p, "RM (Active)", new29)))

for name, ok in results:
    print(f"{name}: {ok}")
