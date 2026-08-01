# -*- coding: utf-8 -*-
"""修复 031-devops 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\031-devops")
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

# 001 反馈循环
p = ROOT / "001-OverviewLinuxBasics.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    A[计划] --> B[编码] --> C[构建] --> D[测试] --> E[发布] --> F[部署] --> G[运维] --> H[监控]\n"
    "    H -.->|持续反馈| A\n"
    "```"
)
results.append(("001-loop", replace_fence(p, "计划 → 编码", new)))

new2 = (
    "```mermaid\nflowchart TD\n"
    "    P[权限位解析 -rwxr-xr--]\n"
    "    P --> O[所有者 rwx 7]\n"
    "    P --> G[组 r-x 5]\n"
    "    P --> U[其他用户 r-- 4]\n"
    "    P --> T[文件类型：- 普通文件，d 目录，l 链接]\n"
    "```"
)
results.append(("001-perms", replace_fence(p, "file.txt", new2)))

# 002 TLS 握手
p = ROOT / "002-NetworkSecurity.md"
new3 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as Client\n"
    "    participant S as Server\n"
    "    C->>S: ClientHello（支持的加密套件）\n"
    "    S-->>C: ServerHello + Certificate（选择的套件 + 证书）\n"
    "    C->>S: Key Exchange\n"
    "    S-->>C: Finished\n"
    "    Note over C,S: 加密通信\n"
    "```"
)
results.append(("002-tls", replace_fence(p, "TLS 握手流程", new3)))

# 003 Docker
p = ROOT / "003-ContainerDocker.md"
new4 = (
    "```mermaid\nflowchart LR\n"
    "    C[Client docker] --> D[Docker Daemon] --> R[Registry Hub/私有]\n"
    "    D --> I[Image]\n"
    "    D --> CT[Container]\n"
    "    D --> N[Network]\n"
    "```"
)
results.append(("003-docker", replace_fence(p, "Client", new4)))

# 004 Kubernetes
p = ROOT / "004-Kubernetes.md"
new5 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph CP[Control Plane]\n"
    "        API[API Server] SCH[Scheduler] CM[Controller Manager]\n"
    "        ETCD[etcd 集群状态存储]\n"
    "    end\n"
    "    N1[Node 1<br/>kubelet Proxy Pods]\n"
    "    N2[Node 2<br/>kubelet Proxy Pods]\n"
    "    N3[Node 3<br/>kubelet Proxy Pods]\n"
    "    NN[Node N<br/>kubelet Proxy Pods]\n"
    "    CP --> N1\n"
    "    CP --> N2\n"
    "    CP --> N3\n"
    "    CP --> NN\n"
    "```"
)
results.append(("004-k8s", replace_fence(p, "Control Plane", new5)))

new6 = (
    "```mermaid\nflowchart LR\n"
    "    O[Operator]\n"
    "    CRD[CRD 自定义资源] <--> C[Controller 协调循环 Reconcile]\n"
    "    O --- CRD\n"
    "    O --- C\n"
    "```"
)
results.append(("004-operator", replace_fence(p, "CRD", new6)))

# 005 GitOps
p = ROOT / "005-CICDPipeline.md"
new7 = (
    "```mermaid\nflowchart LR\n"
    "    D[开发者] -->|push| G[Git 仓库]\n"
    "    A[ArgoCD] <-->|sync| G\n"
    "    A -->|apply| K[Kubernetes]\n"
    "```"
)
results.append(("005-gitops", replace_fence(p, "Git 仓库", new7)))

new8 = (
    "```mermaid\nflowchart LR\n"
    "    B1[Blue v1 当前版本<br/>← 流量] G1[Green v2 新版本<br/>无流量]\n"
    "    B2[Blue v1 旧版本<br/>无流量] G2[Green v2 当前版本<br/>← 流量]\n"
    "    B1 -->|切换流量| G2\n"
    "```"
)
results.append(("005-bluegreen", replace_fence(p, "Blue (v1)", new8)))

# 006 Prometheus
p = ROOT / "006-MonitorAndObservability.md"
new9 = (
    "```mermaid\nflowchart LR\n"
    "    T[Targets 应用/节点] -->|pull| P[Prometheus Server]\n"
    "    P -->|query| G[Grafana 可视化]\n"
    "    P --> A[AlertManager]\n"
    "    P --> TS[TSDB 存储]\n"
    "    P --> SD[SD 服务发现]\n"
    "```"
)
results.append(("006-prom", replace_fence(p, "Prometheus", new9)))

# 008 CloudNativeSRE 分层
p = ROOT / "008-CloudNativeSRE.md"
new10 = (
    "```mermaid\nflowchart TD\n"
    "    App[应用层<br/>微服务 / Serverless / 函数计算] --> R[运行时层<br/>Kubernetes / Container Runtime]\n"
    "    R --> I[基础设施层<br/>云平台 / 存储 / 网络 / 安全]\n"
    "    I --> O[可观测性<br/>Prometheus / Grafana / OpenTelemetry]\n"
    "    O --> CD[CI/CD<br/>ArgoCD / Flux / Tekton]\n"
    "```"
)
results.append(("008-sre-layers", replace_fence(p, "应用层", new10)))

new11 = (
    "```mermaid\nflowchart TD\n"
    "    CP[Control Plane<br/>istiod Pilot + Citadel + Galley]\n"
    "    S1[Service A<br/>Envoy Sidecar<br/>App]\n"
    "    S2[Service B<br/>Envoy Sidecar<br/>App]\n"
    "    CP -->|配置下发| S1\n"
    "    CP -->|配置下发| S2\n"
    "    S1 <--> S2\n"
    "```"
)
results.append(("008-istio", replace_fence(p, "istiod", new11)))

# 011 ServiceMesh
p = ROOT / "011-ServiceMesh.md"
new12 = (
    "```mermaid\nflowchart TD\n"
    "    CP[控制面 istiod<br/>Pilot 流量管理 / Citadel 安全证书 / Galley 配置验证]\n"
    "    DP[数据面 Envoy<br/>Pod A App+Sidecar / Pod B App+Sidecar / Pod C App+Sidecar]\n"
    "    CP <-->|配置下发| DP\n"
    "```"
)
results.append(("011-mesh", replace_fence(p, "控制面 (istiod", new12)))

# 017 故障六要素
p = ROOT / "017-Troubleshooting.md"
new13 = (
    "```mermaid\nflowchart TD\n"
    "    F[故障]\n"
    "    F --> P[人员]\n"
    "    F --> PR[流程]\n"
    "    F --> T[技术]\n"
    "    F --> E[环境]\n"
    "    F --> D[数据]\n"
    "    F --> TL[工具]\n"
    "```"
)
results.append(("017-6m", replace_fence(p, "故障", new13)))

# 019 GitOps
p = ROOT / "019-GitOpsCD.md"
new14 = (
    "```mermaid\nflowchart LR\n"
    "    G[Git 仓库] --> A[ArgoCD] --> K[Kubernetes 集群]\n"
    "    K -.->|状态同步| G\n"
    "```"
)
results.append(("019-gitops", replace_fence(p, "Git 仓库 →", new14)))

new15 = (
    "```mermaid\nflowchart LR\n"
    "    D[开发环境] -->|合并到 dev 分支| S[预发布环境]\n"
    "    S -->|合并到 staging 分支| P[生产环境]\n"
    "    P -->|合并到 main 分支| P\n"
    "```"
)
results.append(("019-promote", replace_fence(p, "开发环境 →", new15)))

for name, ok in results:
    print(f"{name}: {ok}")
