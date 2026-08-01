# -*- coding: utf-8 -*-
"""修复 034-cloud-computing 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\034-cloud-computing")
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

# 001 SaaS/PaaS/IaaS
p = ROOT / "001-CloudComputingBasics.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    SaaS[SaaS 软件即服务<br/>完整应用：Gmail、Salesforce、钉钉] --> PaaS[PaaS 平台即服务<br/>运行环境：Heroku、Cloud Run、函数计算]\n"
    "    PaaS --> IaaS[IaaS 基础设施即服务<br/>虚拟机/网络：AWS EC2、阿里云 ECS]\n"
    "    IaaS --> HW[物理硬件（数据中心）]\n"
    "```"
)
results.append(("001-spi", replace_fence(p, "SaaS (软件即服务)", new)))

new2 = (
    "```mermaid\nflowchart LR\n"
    "    P[私有云<br/>核心业务<br/>敏感数据] <--> G[混合云网关<br/>专线/VPN<br/>数据同步] <--> U[公有云<br/>弹性业务<br/>大数据分析]\n"
    "```"
)
results.append(("001-hybrid", replace_fence(p, "私有云", new2)))

new3 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Region[Region 区域]\n"
    "        subgraph AZa[AZ-a]\n"
    "            A1[实例 x2]\n"
            "            R1[RDS 主]\n"
    "        end\n"
    "        subgraph AZb[AZ-b]\n"
    "            A2[实例 x2]\n"
    "            R2[RDS 从]\n"
    "        end\n"
    "        subgraph AZc[AZ-c]\n"
    "            A3[实例 x2]\n"
    "            R3[RDS 从]\n"
    "        end\n"
    "    end\n"
    "```"
)
results.append(("001-az", replace_fence(p, "AZ-a", new3)))

# 002 VPC
p = ROOT / "002-CloudNetworkStorage.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph VPC[VPC 10.0.0.0/16]\n"
    "        subgraph Pub[公有子网 10.0.1.0/24]\n"
    "            ALB[ALB]\n"
    "            NAT[NAT GW]\n"
    "        end\n"
    "        subgraph Priv[私有子网 10.0.2.0/24]\n"
    "            App[App]\n"
    "            DB[DB]\n"
    "        end\n"
    "    end\n"
    "    VPC --> IGW[Internet GW]\n"
    "    IGW --> Net[Internet]\n"
    "```"
)
results.append(("002-vpc", replace_fence(p, "公有子网", new4)))

# 003 K8s Cluster
p = ROOT / "003-ContainerOrchestration.md"
new5 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Cluster[Kubernetes Cluster]\n"
    "        CP[Control Plane<br/>API Server / etcd / Scheduler / Controller Mgr]\n"
    "        subgraph N1[Node 1]\n"
            "            P1[Pod A] P2[Pod B]\n"
    "            K1[kubelet kube-proxy]\n"
    "        end\n"
    "        subgraph N2[Node 2]\n"
    "            P3[Pod C] P4[Pod D]\n"
    "            K2[kubelet kube-proxy]\n"
    "        end\n"
    "        subgraph N3[Node 3]\n"
    "            P5[Pod E] P6[Pod F]\n"
    "            K3[kubelet kube-proxy]\n"
    "        end\n"
    "        CP --- N1\n"
    "        CP --- N2\n"
    "        CP --- N3\n"
    "    end\n"
    "```"
)
results.append(("003-k8s", replace_fence(p, "Control Plane", new5)))

# 005 IaaS/PaaS/SaaS
p = ROOT / "005-IaaSPaaSSaaS.md"
new6 = (
    "```mermaid\nflowchart TD\n"
    "    SaaS[SaaS 应用层] --> PaaS[PaaS 平台层] --> IaaS[IaaS 基础设施层] --> HW[物理硬件/数据中心]\n"
    "```"
)
results.append(("005-spi2", replace_fence(p, "SaaS", new6)))

# 006 虚拟化技术
p = ROOT / "006-VirtualizationTech.md"
new7 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph VMs[VM 1 / VM 2 / VM 3<br/>Guest OS]\n"
    "    end\n"
    "    H[Type 1 Hypervisor<br/>VMware ESXi / Hyper-V / KVM]\n"
    "    HW[Physical Hardware]\n"
    "    VMs --> H --> HW\n"
    "```"
)
results.append(("006-t1", replace_fence(p, "Type 1 Hypervisor", new7)))

new8 = (
    "```mermaid\nflowchart TD\n"
    "    VMs[VM 1 / VM 2<br/>Guest OS] --> H[Type 2 Hypervisor<br/>VMware Workstation / VirtualBox]\n"
    "    H --> OS[Host Operating System] --> HW[Physical Hardware]\n"
    "```"
)
results.append(("006-t2", replace_fence(p, "Type 2 Hypervisor", new8)))

new9 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph User[User Space]\n"
        "        Q1[QEMU vCPU0]\n"
    "        Q2[QEMU vCPU1]\n"
    "        KIO[/dev/kvm ioctl]\n"
    "    end\n"
    "    subgraph Kernel[Kernel Space]\n"
    "        KM[KVM Kernel Module<br/>vCPU Thread / MMU EPT]\n"
    "    end\n"
    "    HW[Physical Hardware<br/>Intel VT-x / AMD-V + EPT/RVI]\n"
    "    Q1 --> KIO\n"
    "    Q2 --> KIO\n"
    "    KIO --> KM\n"
    "    KM --> HW\n"
    "```"
)
results.append(("006-kvm", replace_fence(p, "QEMU   │", new9)))

new10 = (
    "```mermaid\nflowchart TD\n"
    "    V[VMCS Virtual Machine Control Structure]\n"
    "    V --> G[Guest-state Area<br/>Guest 寄存器状态]\n"
    "    V --> H[Host-state Area<br/>Host 寄存器状态]\n"
    "    V --> E[VM-execution control fields 执行控制]\n"
    "    V --> X[VM-exit control fields 退出控制]\n"
    "    V --> N[VM-entry control fields 进入控制]\n"
    "    V --> I[VM-exit information fields 退出原因信息]\n"
    "```"
)
results.append(("006-vmcs", replace_fence(p, "VMCS", new10)))

new11 = (
    "```mermaid\nflowchart LR\n"
    "    G[virtio-net driver] -->|virtqueue shared mem| H[vhost-net backend]\n"
    "    H -->|notification| G\n"
    "```"
)
results.append(("006-virtio", replace_fence(p, "virtio-net", new11)))

new12 = (
    "```mermaid\nflowchart TD\n"
    "    V[vring]\n"
    "    V --> D[Descriptor Table 描述符表<br/>描述 buffer 地址与长度]\n"
    "    V --> A[Available Ring 可用环<br/>Guest → Host 方向]\n"
    "    V --> U[Used Ring 已用环<br/>Host → Guest 方向]\n"
    "```"
)
results.append(("006-vring", replace_fence(p, "vring", new12)))

new13 = (
    "```mermaid\nflowchart TD\n"
    "    V1[VM 1 VF0] --> PF[PF Physical Function 物理网卡]\n"
    "    V2[VM 2 VF1] --> PF\n"
    "    V3[VM 3 VF2] --> PF\n"
    "```"
)
results.append(("006-sr-iov", replace_fence(p, "PF (Physical", new13)))

new14 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph VM[虚拟机]\n"
    "        VA[App A<br/>Bins/Libs<br/>Guest OS]\n"
    "        VB[App B<br/>Bins/Libs<br/>Guest OS]\n"
    "        VH[Hypervisor]\n"
    "        VOS[Host OS]\n"
    "        VHW[Physical Hardware]\n"
    "    end\n"
    "    subgraph Container[容器]\n"
    "        CA[App A<br/>Bins/Libs<br/>Container]\n"
    "        CB[App B<br/>Bins/Libs<br/>Container]\n"
    "        CR[Container Runtime]\n"
    "        COS[Host OS]\n"
    "        CHW[Physical Hardware]\n"
    "    end\n"
    "```"
)
results.append(("006-vm-vs-container", replace_fence(p, "App A   │ │  App B", new14)))

new15 = (
    "```mermaid\nflowchart TD\n"
    "    W[可写层 Container Layer<br/>容器运行时修改] --> L3[Layer 3 App Code<br/>应用代码]\n"
    "    L3 --> L2[Layer 2 Dependencies<br/>依赖库]\n"
    "    L2 --> L1[Layer 1 Base OS<br/>基础镜像]\n"
    "```"
)
results.append(("006-image-layers", replace_fence(p, "可写层 (Container", new15)))

# 007 云架构设计
p = ROOT / "007-CloudArchitectureDesign.md"
new16 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph BC[限界上下文 Bounded Context]\n"
        "        O[订单上下文<br/>Aggregate Order]\n"
    "        P[支付上下文<br/>Aggregate Payment]\n"
    "        S[库存上下文<br/>Aggregate Stock]\n"
    "    end\n"
    "```"
)
results.append(("007-bc", replace_fence(p, "订单上下文", new16)))

new17 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Mesh[Service Mesh]\n"
    "        A[Service A<br/>Sidecar] <--> B[Service B<br/>Sidecar]\n"
    "        CP[Control Plane<br/>Pilot / Citadel / Galley]\n"
    "    end\n"
    "```"
)
results.append(("007-mesh", replace_fence(p, "Service A│", new17)))

new18 = (
    "```mermaid\nflowchart LR\n"
    "    Prod[事件生产者] -->|事件| Router[事件路由器] -->|事件| Cons[事件消费者]\n"
    "    Router --> Store[事件存储<br/>可选，用于事件回放]\n"
    "```"
)
results.append(("007-events", replace_fence(p, "事件生产者", new18)))

new19 = (
    "```mermaid\nflowchart LR\n"
    "    W[Write Side API] -->|Command| CM[Command Model OLTP] -->|Event| QM[Query Model OLAP]\n"
    "    R[Read Side API] <-->|Query| QM\n"
    "```"
)
results.append(("007-cqrs", replace_fence(p, "Write Side", new19)))

new20 = (
    "```mermaid\nflowchart LR\n"
    "    A[请求到达] --> B[冷启动] --> C[初始化运行时] --> D[执行函数] --> E[返回结果] --> F[实例保活] --> G[超时回收]\n"
    "    G -.->|下次请求，若实例已回收| B\n"
    "```"
)
results.append(("007-serverless", replace_fence(p, "请求到达 →", new20)))

new21 = (
    "```mermaid\nflowchart TD\n"
    "    GLB[全球负载均衡 DNS/CDN]\n"
    "    subgraph RA[区域 A]\n"
        "        ALB1[ALB 多 AZ]\n"
    "        AZ1[AZ1] AZ2[AZ2] AZ3[AZ3]\n"
    "        DB1[数据库主]\n"
    "    end\n"
    "    subgraph RB[区域 B]\n"
    "        ALB2[ALB 多 AZ]\n"
    "        BZ1[AZ1] BZ2[AZ2] BZ3[AZ3]\n"
    "        DB2[数据库从]\n"
    "    end\n"
    "    GLB --> ALB1\n"
    "    GLB --> ALB2\n"
    "```"
)
results.append(("007-glb", replace_fence(p, "全球负载均衡", new21)))

# 008 混合云
p = ROOT / "008-PublicCloudPrivateCloudHybridCloud.md"
new22 = (
    "```mermaid\nflowchart LR\n"
    "    P[私有云<br/>核心业务] <-->|专线/VPN| U[公有云<br/>弹性负载]\n"
    "```"
)
results.append(("008-hybrid", replace_fence(p, "私有云", new22)))

# 010 云原生
p = ROOT / "010-CloudNativeApp.md"
new23 = (
    "```mermaid\nflowchart TD\n"
    "    App[应用层<br/>Serverless / Batch / Streaming / ML Pipeline] --> Plat[平台层<br/>Kubernetes / Service Mesh / CI-CD / Observability]\n"
    "    Plat --> Infra[基础设施层<br/>Container Runtime / IaC / Cloud Provider APIs]\n"
    "```"
)
results.append(("010-cn-layers", replace_fence(p, "应用层", new23)))

new24 = (
    "```mermaid\nflowchart LR\n"
    "    O[可观测性]\n"
    "    O --> M[指标 Metrics<br/>Prometheus / Grafana / Datadog]\n"
    "    O --> L[日志 Logs<br/>Fluentd / Loki / Elasticsearch]\n"
    "    O --> T[追踪 Traces<br/>OpenTelemetry / Jaeger / Tempo]\n"
    "```"
)
results.append(("010-observability", replace_fence(p, "可观测性", new24)))

# 011 K8s 架构
p = ROOT / "011-KubernetesArchitecture.md"
new25 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph CP[控制平面]\n"
        "        API[API Server]\n"
    "        SCH[Scheduler]\n"
    "        CM[Controller Manager]\n"
    "        ETCD[etcd]\n"
    "    end\n"
    "    subgraph N1[Node 1]\n"
    "        K1[kubelet] P1[kube-proxy] PD1[Pods]\n"
    "    end\n"
    "    subgraph N2[Node 2]\n"
    "        K2[kubelet] P2[kube-proxy] PD2[Pods]\n"
    "    end\n"
    "    CP --> N1\n"
    "    CP --> N2\n"
    "```"
)
results.append(("011-k8s-arch", replace_fence(p, "控制平面", new25)))

new26 = (
    "```mermaid\nflowchart TD\n"
    "    LB[负载均衡器 LB]\n"
    "    M1[Master 1 leader]\n"
    "    M2[Master 2 follower]\n"
    "    M3[Master 3 follower]\n"
    "    LB --> M1\n"
    "    LB --> M2\n"
    "    LB --> M3\n"
    "```"
)
results.append(("011-ha", replace_fence(p, "负载均衡器 (LB)", new26)))

# 012 云数据库
p = ROOT / "012-CloudDatabaseService.md"
new27 = (
    "```mermaid\nflowchart LR\n"
    "    S[云数据库服务]\n"
    "    S --> R[关系型<br/>RDS/Cloud SQL/MySQL/PostgreSQL/SQL Server/Oracle]\n"
    "    S --> N[NoSQL<br/>DynamoDB/MongoDB Atlas/ElastiCache/Firestore]\n"
    "    S --> C[云原生/新架构<br/>Aurora/PolarDB/TiDB Cloud/CockroachDB/PlanetScale]\n"
    "```"
)
results.append(("012-dbtypes", replace_fence(p, "云数据库服务", new27)))

new28 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Region[AWS Region]\n"
    "        subgraph AZA[AZ-A]\n"
    "            P[Primary R/W]\n"
    "        end\n"
    "        subgraph AZB[AZ-B]\n"
    "            S1[Standby R]\n"
    "        end\n"
    "        RR[Read Replica<br/>异步复制，跨区域可选]\n"
    "    end\n"
    "    P <-->|同步复制| S1\n"
    "    P --> RR\n"
    "```"
)
results.append(("012-ha", replace_fence(p, "Primary│", new28)))

new29 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Aurora[Aurora 架构]\n"
    "        subgraph Compute[计算层]\n"
    "            W[Writer Instance]\n"
    "            R1[Reader 1 Instance]\n"
    "            R2[Reader 2 Instance]\n"
    "        end\n"
    "        subgraph Storage[Aurora Storage 6 副本/3 AZ]\n"
    "            P1[P1 AZ-A] P2[P2 AZ-A] P3[P3 AZ-B] P4[P4 AZ-B] P5[P5 AZ-C] P6[P6 AZ-C]\n"
    "        end\n"
    "        W --> Storage\n"
    "        R1 --> Storage\n"
    "        R2 --> Storage\n"
    "    end\n"
    "```"
)
results.append(("012-aurora", replace_fence(p, "Writer   │", new29)))

new30 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph TiDBCloud[TiDB Cloud 架构]\n"
    "        TDB[TiDB SQL 层<br/>解析 → 优化 → 执行 → 返回]\n"
    "        TKV[TiKV 行存/OLTP<br/>Raft 复制]\n"
    "        TF[TiFlash 列存/OLAP<br/>异步复制]\n"
    "        PD[PD 调度器]\n"
    "    end\n"
    "    TDB --> TKV\n"
    "    TDB --> TF\n"
    "    TKV --> PD\n"
    "    TF --> PD\n"
    "```"
)
results.append(("012-tidb", replace_fence(p, "TiDB (SQL", new30)))

new31 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph P[主区域 us-1]\n"
    "        PW[Writer]\n"
    "        PS[Storage 6副本]\n"
    "        PW --> PS\n"
    "    end\n"
    "    subgraph B[备区域 eu-1]\n"
    "        BR[Reader]\n"
    "        BS[Storage 6副本]\n"
    "        BR --> BS\n"
    "    end\n"
    "    PS -->|复制| BS\n"
    "```"
)
results.append(("012-region", replace_fence(p, "主区域 (us-1)", new31)))

# 014 云存储
p = ROOT / "014-CloudStorageService.md"
new32 = (
    "```mermaid\nflowchart TD\n"
    "    H[标准/热存储<br/>频繁访问，低延迟] --> W[低频/温存储<br/>月访问1-2次，检索费]\n"
    "    W --> C[归档/冷存储<br/>年访问1-2次，恢复需小时]\n"
    "    C --> D[深度归档<br/>极少访问，合规保留]\n"
    "```\n\n"
    "成本递减，存取成本递增"
)
results.append(("014-tier", replace_fence(p, "标准/热存储", new32)))

new33 = (
    "```mermaid\nflowchart TD\n"
    "    B[Bucket 桶]\n"
    "    B --> O1[Object 对象]\n"
    "    O1 --> D1[Data 数据]\n"
    "    O1 --> K1[Key 键名]\n"
    "    O1 --> M1[Metadata 元数据]\n"
    "    O1 --> V1[Version ID 版本ID]\n"
    "    B --> O2[Object ...]\n"
    "```"
)
results.append(("014-object", replace_fence(p, "Bucket (桶)", new33)))

new34 = (
    "```mermaid\nflowchart LR\n"
    "    P1[Part 1 5MB] --> S3[S3]\n"
    "    P2[Part 2 5MB] --> S3\n"
    "    P3[Part 3 5MB] --> S3\n"
    "    PN[Part N 5MB] --> S3\n"
    "    CM[Complete Multipart Upload] --> S3\n"
    "```"
)
results.append(("014-multipart", replace_fence(p, "Part 1 (5MB)", new34)))

new35 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph EFS[EFS]\n"
    "        FS[文件系统 自动伸缩<br/>/data/<br/>app1 / app2 / shared]\n"
    "    end\n"
    "    E1[EC2-1 mount] --> FS\n"
    "    E2[EC2-2 mount] --> FS\n"
    "    E3[ECS mount] --> FS\n"
    "```"
)
results.append(("014-efs", replace_fence(p, "文件系统 (自动伸缩", new35)))

new36 = (
    "```mermaid\nflowchart TD\n"
    "    H[频繁访问层] -->|30天未访问| W[低频访问层] -->|访问时自动回热| H\n"
    "    W -->|30天| A[归档即时访问层] -->|90天| D[归档灵活访问层] -->|180天| DD[深度归档访问层]\n"
    "```"
)
results.append(("014-tiering", replace_fence(p, "S3 Intelligent-Tiering", new36)))

new37 = (
    "```mermaid\nflowchart LR\n"
    "    A[源区域 Bucket A<br/>us-east-1] -->|复制 异步| B[目标区域 Bucket B<br/>eu-west-1]\n"
    "```"
)
results.append(("014-replication", replace_fence(p, "源区域", new37)))

# 015 K8s 网络
p = ROOT / "015-KubernetesNetwork.md"
new38 = (
    "```mermaid\nflowchart TD\n"
    "    I[Ingress 网络<br/>外部流量入口] --> S[Service 网络<br/>虚拟 IP ClusterIP]\n"
    "    S --> P[Pod 网络<br/>容器 IP]\n"
    "    P --> N[Node 网络<br/>物理网络]\n"
    "```"
)
results.append(("015-k8snet", replace_fence(p, "Ingress 网络", new38)))

# 016 VPC
p = ROOT / "016-CloudNetworkService.md"
new39 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph VPC[VPC 10.0.0.0/16]\n"
    "        subgraph Pub[公有子网 10.0.1.0/24]\n"
    "            ALB[ALB]\n"
    "            BS[Bastion]\n"
    "        end\n"
    "        subgraph Priv[私有子网 10.0.2.0/24]\n"
    "            APP[App]\n"
    "            DB[DB]\n"
    "        end\n"
    "        IGW[Internet Gateway]\n"
    "    end\n"
    "```"
)
results.append(("016-vpc2", replace_fence(p, "公有子网", new39)))

# 016 LB/CDN/边缘/中继
p = ROOT / "016-CloudNetworkService.md"
new40 = (
    "```mermaid\nflowchart LR\n"
    "    L4[L4 传输层<br/>NLB<br/>TCP/UDP/TLS<br/>超低延迟 百万RPS 保留源IP]\n"
    "    L7[L7 应用层<br/>ALB<br/>HTTP/HTTPS/gRPC<br/>路径/主机路由 SSL 终止 认证/速率限制]\n"
    "```"
)
results.append(("016-lb", replace_fence(p, "L4 (传输层", new40)))

new41 = (
    "```mermaid\nflowchart TD\n"
    "    R1[IF Host = api.example.com AND Path = /users/* → Forward to user-service]\n"
    "    R2[IF Host = api.example.com AND Path = /orders/* → Forward to order-service]\n"
    "    R3[IF Path = /static/* → Redirect to CDN]\n"
    "    R4[IF Header[X-Canary] = true → Forward to canary-service 10%]\n"
    "```"
)
results.append(("016-alb-rules", replace_fence(p, "AND Path = /users/*", new41)))

new42 = (
    "```mermaid\nflowchart TD\n"
    "    R[请求] --> H{命中缓存?}\n"
    "    H -- 是 --> RET[直接返回]\n"
    "    H -- 未命中 --> O[回源获取] --> C[缓存] --> RET\n"
    "```"
)
results.append(("016-cdn", replace_fence(p, "命中缓存?", new42)))

new43 = (
    "```mermaid\nflowchart LR\n"
    "    IoT[IoT<br/>&lt;1ms] --> PoP[CDN PoP<br/>&lt;10ms] --> Reg[Regional<br/>&lt;50ms] --> Cen[Central<br/>&lt;100ms]\n"
    "```"
)
results.append(("016-edge", replace_fence(p, "IoT)    (CDN", new43)))

new44 = (
    "```mermaid\nflowchart TD\n"
    "    TG[Transit Gateway<br/>中心化网络枢纽] --> VPC_A[VPC A<br/>支持传递路由]\n"
    "    TG --> VPC_B[VPC B]\n"
    "    TG --> VPC_C[VPC C]\n"
    "```"
)
results.append(("016-tgw", replace_fence(p, "Transit Gateway", new44)))

new45 = (
    "```mermaid\nflowchart TD\n"
    "    Root[组织网络] --> P[生产VPC<br/>3层架构]\n"
    "    Root --> T[测试VPC<br/>3层架构]\n"
    "    Root --> D[开发VPC<br/>简化]\n"
    "    Root --> S[共享VPC<br/>DNS/NTP/日志]\n"
    "```"
)
results.append(("016-vpc-topology", replace_fence(p, "生产VPC", new45)))

# 017 K8s 存储
p = ROOT / "017-KubernetesStorage.md"
new46 = (
    "```mermaid\nflowchart TD\n"
    "    App[应用 Pod] --> PVC[PVC 声明]\n"
    "    PVC --> PV[PV 卷]\n"
    "    PV --> SC[StorageClass 类]\n"
    "    SC --> CSI[CSI 驱动]\n"
    "    CSI --> Backend[后端存储]\n"
    "```"
)
results.append(("017-storage", replace_fence(p, "应用 (Pod)", new46)))

# 018 云安全
p = ROOT / "018-CloudSecurityService.md"
new47 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Shared[责任共担]\n"
        "        I[IaaS<br/>云厂商：物理安全、基础设施、网络<br/>客户：OS、应用、数据]\n"
    "        P[PaaS<br/>云厂商：物理、基础设施、OS、运行时<br/>客户：应用代码、数据]\n"
    "        S[SaaS<br/>云厂商：几乎全部<br/>客户：数据、访问控制]\n"
    "    end\n"
    "```"
)
results.append(("018-shared", replace_fence(p, "云厂商责任", new47)))

new48 = (
    "```mermaid\nflowchart LR\n"
    "    P[Principal 谁] --> R[Role 角色] --> PL[Policy 权限] --> Res[Resource 什么资源]\n"
    "```\n\n"
    "认证（AuthN）：你是谁？授权（AuthZ）：你能做什么？审计（Audit）：你做了什么？"
)
results.append(("018-iam", replace_fence(p, "Principal", new48)))

new49 = (
    "```mermaid\nflowchart LR\n"
    "    IdP[企业 IdP AD/LDAP] -->|SAML/OIDC 联合认证| IAM[IAM Role 临时凭证] --> AWS[AWS 资源]\n"
    "```"
)
results.append(("018-federation", replace_fence(p, "企业 IdP", new49)))

new50 = (
    "```mermaid\nflowchart TD\n"
    "    A[应用层加密<br/>应用代码实现，最灵活] --> S[存储层加密<br/>数据库/文件系统透明加密]\n"
    "    S --> D[磁盘层加密<br/>EBS 加密，操作系统不可见]\n"
    "    D --> N[网络层加密<br/>TLS/IPsec，传输中保护]\n"
    "```"
)
results.append(("018-encryption", replace_fence(p, "加密层次", new50)))

new51 = (
    "```mermaid\nflowchart TD\n"
    "    AWS[AWS 托管密钥 aws/*] --> HSM[HSM 硬件安全模块<br/>密钥在 HSM 中生成和存储]\n"
    "    CUST[客户托管密钥 alias/*] --> HSM\n"
    "    BYOK[客户自带密钥 ext/*] --> HSM\n"
    "```"
)
results.append(("018-kms", replace_fence(p, "AWS 托管", new51)))

new52 = (
    "```mermaid\nflowchart TD\n"
    "    B[边界防护<br/>WAF / Shield / CloudFront] --> N[网络防护<br/>VPC / 安全组 / NACL / VPC Endpoint]\n"
    "    N --> H[主机防护<br/>OS 加固 / 漏洞修补 / 运行时保护]\n"
    "    H --> A[应用防护<br/>输入验证 / 认证授权 / 会话管理]\n"
    "    A --> D[数据防护<br/>加密 / 脱敏 / 访问控制]\n"
    "```"
)
results.append(("018-defense", replace_fence(p, "深度防御层级", new52)))

new53 = (
    "```mermaid\nflowchart TD\n"
    "    RC[资源变更] --> CR[Config Recorder] --> CI[配置项]\n"
    "    CR --> RULE[合规规则]\n"
    "    RULE --> COMP[COMPLIANT]\n"
    "    RULE --> NON[NON_COMPLIANT] --> FIX[自动修正]\n"
    "```"
)
results.append(("018-config", replace_fence(p, "AWS Config", new53)))

new54 = (
    "```mermaid\nflowchart LR\n"
    "    D[检测<br/>GuardDuty/SecurityHub/Config] --> A[分析<br/>上下文/取证] --> C[遏制<br/>隔离/撤销权限]\n"
    "    C --> E[根除<br/>修补/清除恶意] --> R[恢复<br/>验证/恢复服务] --> X[复盘<br/>改进/文档/策略]\n"
    "```"
)
results.append(("018-ops", replace_fence(p, "安全运营流程", new54)))

new55 = (
    "```mermaid\nflowchart LR\n"
    "    GD[GuardDuty 发现] --> EB[EventBridge] --> L[Lambda 自动动作]\n"
    "    L --> A1[撤销 IAM 凭证]\n"
    "    L --> A2[隔离 EC2 实例]\n"
    "    L --> A3[阻止恶意 IP]\n"
    "    L --> A4[通知安全团队]\n"
    "    L --> A5[创建 JIRA 工单]\n"
    "```"
)
results.append(("018-guardduty", replace_fence(p, "GuardDuty 发现", new55)))

# 020 成本优化
p = ROOT / "020-CloudCostOptimization.md"
new56 = (
    "```mermaid\nflowchart LR\n"
    "    Crawl[Crawl 爬行<br/>基础可见性、成本分配、标签策略、预算告警] --> Walk[Walk 行走<br/>优化与治理、预留采购、异常检测、团队问责]\n"
    "    Walk --> Run[Run 奔跑<br/>持续优化与自动化、智能伸缩、自动 Right-sizing、单位经济学驱动]\n"
    "```"
)
results.append(("020-finops", replace_fence(p, "FinOps 成熟度", new56)))

new57 = (
    "```mermaid\nflowchart TD\n"
    "    OD[按需实例 N 个<br/>核心容量，保证基线] + SP[Spot 实例 M 个<br/>弹性容量，可被中断]\n"
    "    OD --> T[总容量 = N + M<br/>保证容量 ≥ N]\n"
    "    SP --> T\n"
    "```"
)
results.append(("020-spot", replace_fence(p, "Spot 混合策略", new57)))

new58 = (
    "```mermaid\nflowchart TD\n"
    "    Q{数据访问频率?}\n"
    "    Q -->|频繁 >1次/天| S1[Standard]\n"
    "    Q -->|偶尔 >1次/月| S2[Standard-IA]\n"
    "    Q -->|稀少 >1次/年| S3[Glacier Instant]\n"
    "    Q -->|极少 <1次/年| S4[Glacier Deep Archive]\n"
    "    Q -->|未知| S5[Intelligent-Tiering]\n"
    "```"
)
results.append(("020-tiering", replace_fence(p, "存储分层决策树", new58)))

new59 = (
    "```mermaid\nflowchart TD\n"
    "    F[财务<br/>预算/预测/报告] --> FP[FinOps 平台/流程]\n"
    "    E[工程<br/>优化/架构/自动化] --> FP\n"
    "    B[业务<br/>价值/优先级/ROI] --> FP\n"
    "```"
)
results.append(("020-org", replace_fence(p, "FinOps 组织架构", new59)))

new60 = (
    "```mermaid\nflowchart LR\n"
    "    I[Inform 告知<br/>成本分配与可视化/预算与告警/异常检测] --> O[Optimize 优化<br/>Right-sizing/预留采购/存储分层/架构优化]\n"
    "    O --> P[Operate 运营<br/>自动化策略/治理与合规/持续监控]\n"
    "    P --> I\n"
    "```"
)
results.append(("020-loop", replace_fence(p, "FinOps 持续优化循环", new60)))

# 022 微服务
p = ROOT / "022-MicroserviceArchitecture.md"
new61 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph O[订单上下文]\n"
    "        OS[OrderService] OD[OrderDB]\n"
    "    end\n"
    "    subgraph I[库存上下文]\n"
    "        IS[InventorySvc] ID[InventoryDB]\n"
    "    end\n"
    "    subgraph P[支付上下文]\n"
    "        PS[PaymentService] PD[PaymentDB]\n"
    "    end\n"
    "```"
)
results.append(("022-bounded", replace_fence(p, "订单上下文", new61)))

# 023 Service Mesh
p = ROOT / "023-ServiceMesh.md"
new62 = (
    "```mermaid\nflowchart TD\n"
    "    CP[控制平面<br/>配置分发、证书管理、策略]\n"
    "    S1[Sidecar Proxy<br/>Service A]\n"
    "    S2[Sidecar Proxy<br/>Service B]\n"
    "    CP --> S1\n"
    "    CP --> S2\n"
    "    S1 <--> S2\n"
    "```"
)
results.append(("023-mesh", replace_fence(p, "控制平面", new62)))

# 016 混合连接
p = ROOT / "016-CloudNetworkService.md"
new63 = (
    "```mermaid\nflowchart LR\n"
    "    DC[本地数据中心] <-->|IPsec 隧道| VPN[VPN Gateway VPC]\n"
    "```"
)
results.append(("016-vpn", replace_fence(p, "本地数据中心│◄", new63)))

new64 = (
    "```mermaid\nflowchart LR\n"
    "    DC[本地数据中心] <-->|专用光纤| DX[DX 位置 Colocation] <-->|专用连接| VPC[VPC]\n"
    "```"
)
results.append(("016-directconnect", replace_fence(p, "DX 位置", new64)))

new65 = (
    "```mermaid\nflowchart TD\n"
    "    DC[本地数据中心] -->|专线 主路径 低延迟| V1[VPC]\n"
    "    DC -->|VPN 备份路径 高可用| V1\n"
    "```"
)
results.append(("016-hybrid-links", replace_fence(p, "专线 (主路径", new65)))

new66 = (
    "```mermaid\nflowchart LR\n"
    "    A[VPC A] <-->|Peering| B[VPC B]\n"
    "    B <-->|Peering| C[VPC C]\n"
    "    A -.->|不支持传递路由| C\n"
    "```"
)
results.append(("016-peering", replace_fence(p, "VPC A ◄── Peering", new66)))

new67 = (
    "```mermaid\nflowchart TD\n"
    "    TG[Transit Gateway] --> A[VPC A 支持传递路由]\n"
    "    TG --> B[VPC B]\n"
    "    TG --> C[VPC C]\n"
    "```"
)
results.append(("016-tgw2", replace_fence(p, "Transit    │", new67)))

for name, ok in results:
    print(f"{name}: {ok}")
