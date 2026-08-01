# -*- coding: utf-8 -*-
"""云与基础设施类模块知识库。"""

KB_CLOUD = {}


def _c(label, hint, history, theory, pitfalls, practices, comparisons, engineering,
       case, summary, refs, more, deep):
    axes = [
        f"能够说出 {label} 的核心概念、组件与标准流程。",
        f"能够解释 {label} 的工作原理与关键机制。",
        f"能够执行 {label} 相关的标准操作与配置。",
        f"能够分析 {label} 方案在可靠性、成本与性能上的权衡。",
        f"能够评价 {label} 中的技术选型。",
        f"能够设计基于 {label} 的完整解决方案。",
    ]
    return {
        "label": label, "related_title_hint": hint, "axes": axes,
        "history": history, "history_tail": [], "definitions": theory[:3],
        "theory": theory, "pitfalls": pitfalls, "practices": practices,
        "comparisons": comparisons, "engineering": engineering, "case": case,
        "summary": summary, "refs": refs, "more": more,
        "supplement_examples": [], "deep_topics": deep,
    }


KB_CLOUD["devops"] = _c(
    "DevOps", "CI/CD、容器、编排、监控、GitOps",
    [
        "DevOps 源于 2009 年（“DevOpsDays”），核心是打破开发与运维壁垒，用自动化与协作缩短交付周期；CALMS 文化（文化、自动化、精益、度量、共享）是其框架。",
        "技术栈演进：持续集成（CI）与持续交付（CD）、基础设施即代码（IaC）、容器（Docker）与编排（Kubernetes）、可观测性（监控/日志/追踪）。",
        "2020 年代趋势：GitOps（声明式 + 自动同步）、平台工程（内部开发者平台）、FinOps（成本治理）、AI 辅助运维。",
    ],
    [
        "CI/CD 管线：代码提交 -> 构建 -> 测试 -> 制品 -> 部署；流水线即代码（GitHub Actions/Jenkins/GitLab CI）。",
        "容器与镜像：OCI 规范、Dockerfile 分层、镜像仓库与签名；容器隔离（cgroup/namespace）。",
        "编排：Kubernetes 的 Pod/Deployment/Service 抽象；声明式期望状态与控制器调和。",
        "可观测性三支柱：指标（Prometheus）、日志（Loki/ELK）、追踪（OpenTelemetry）。",
    ],
    [
        ("环境漂移", "手工配置导致环境不一致。全部走 IaC 与镜像。"),
        ("秘密硬编码", "密钥进仓库。使用 Secret 管理与注入。"),
        ("构建不可复现", "依赖未锁定。锁定依赖版本与基础镜像 digest。"),
        ("测试后置", "问题到生产才发现。左移：单元/集成/E2E 分层。"),
        ("回滚缺失", "发布失败无法回退。保留历史镜像与一键回滚。"),
        ("监控盲区", "无指标与告警。核心链路全量可观测。"),
        ("权限过大", "CI 权限超需求。最小权限与短期凭证。"),
        ("部署频率低", "大爆炸发布风险高。小步快跑与灰度。"),
    ],
    [
        "一切皆代码：流水线、基础设施、配置版本化。",
        "发布可重复：相同代码 + 相同制品 -> 相同环境。",
        "失败可预期：小批量、金丝雀、自动回滚。",
        "度量驱动：DORA 指标（部署频率、变更前置时间、恢复时间、变更失败率）。",
    ],
    [
        "CI 与 CD：CI 保证可集成，CD 保证可交付；两者可独立实施。",
        "Kubernetes 与 Docker Compose：K8s 生产级编排；Compose 单机开发。",
        "传统运维与 SRE：SRE 用软件工程方法运维，错误预算与 SLO。",
    ],
    [
        "GitHub Actions：workflow/job/step 模型，矩阵测试，环境与密钥管理。",
        "GitOps：Argo CD 同步 Git 仓库与集群状态，PR 即发布审批。",
        "平台工程：模板化应用脚手架（Backstage）、自助环境、成本可视化。",
    ],
    [
        "需求：为微服务搭建从提交到生产的自动化管线。",
        "方案：GitHub Actions 构建镜像 + 测试 + 扫描，Argo CD 部署到 K8s，Prometheus 监控。",
        "要点：镜像 tag 用 commit SHA；金丝雀发布；回滚演练。",
        "验证：发布频率与失败率度量、故障注入演练。",
    ],
    [
        "DevOps 的本质是自动化与协作，工具只是载体。",
        "可重复、可回滚、可观测是三条主线。",
        "从 DORA 指标开始度量改进，避免为工具而工具。",
    ],
    [
        "GitHub Actions 文档：https://docs.github.com/zh/actions",
        "GitLab CI 文档：https://docs.gitlab.com/ci/",
        "Argo CD：https://argo-cd.readthedocs.io/",
        "DORA 研究：https://dora.dev/",
        "DevOps 手册（Gene Kim 等）：https://itrevolution.com/devops-handbook/",
    ],
    [
        "Docker 与 Kubernetes 深入，见 031-devops 模块文档。",
        "CI/CD 管线设计，见 031-devops 模块 CICD 文档。",
        "云原生架构，见 034-cloud-computing 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 DevOps 课程。",
    ],
    [
        ("GitOps 与声明式交付", [
            "Git 是唯一事实来源：集群状态由仓库声明驱动，差异由控制器调和（Argo CD/Flux）。",
            "PR 流程即变更审批，合并即发布意图；回滚 = revert 提交。",
            "与 CI 衔接：CI 产出镜像，CD 更新清单引用新 digest。",
            "安全：仓库签名、密钥加密（SOPS）、审计日志。",
        ]),
        ("可观测性与 SLO", [
            "指标：RED（请求率、错误、时长）与 USE（利用率、饱和、错误）。",
            "日志：结构化（JSON）、集中采集、关联 trace_id。",
            "追踪：OpenTelemetry 传播上下文，瀑布分析延迟。",
            "SLO/错误预算：目标可用性 99.9% 对应每月约 43 分钟不可用预算，驱动发布决策。",
        ]),
    ],
)

KB_CLOUD["networking"] = _c(
    "网络", "TCP/IP、HTTP、DNS、网络安全、负载均衡",
    [
        "网络是分布式系统的地基：从 ARPANET（1969）到互联网，TCP/IP 协议族（1974 年提出）成为事实标准；HTTP 从 1991 年至今演进到 HTTP/3。",
        "分层模型：OSI 七层与 TCP/IP 四层；每层职责清晰，上层依赖下层服务；理解分层才能定位故障。",
        "现代网络主题：IPv6 过渡、HTTP/2/3、TLS 加密、CDN 与边缘计算、软件定义网络（SDN）。",
    ],
    [
        "TCP：三次握手建立、四次挥手关闭；可靠传输（序号/确认/重传）、流量控制（滑动窗口）、拥塞控制（慢启动/拥塞避免）。",
        "HTTP：请求-响应模型；方法（GET/POST/PUT/DELETE）、状态码（2xx/3xx/4xx/5xx）、头字段；无状态 + Cookie/Token 会话。",
        "DNS：域名到 IP 的分布式解析，递归与迭代查询，缓存与 TTL；HTTP 层通过域名访问。",
        "TLS：握手协商密钥（证书 + 密钥交换），加密传输，防窃听防篡改；HTTPS 是 HTTP + TLS。",
    ],
    [
        ("TCP 与 UDP 误用", "可靠传输选 TCP，实时低延迟可容忍丢包选 UDP/QUIC。"),
        ("HTTP 状态码误用", "业务错误返回 200 导致监控失真。按语义使用 4xx/5xx。"),
        ("DNS 缓存问题", "域名变更后本地缓存旧 IP。TTL 与刷新策略。"),
        ("TLS 证书过期", "服务突然不可用。证书监控与自动续期。"),
        ("长连接泄漏", "连接未复用或超时未清理。连接池 + 空闲超时。"),
        ("CORS 误解", "CORS 是浏览器策略非服务器安全。正确配置白名单。"),
        ("NAT 与内网穿透", "P2P 场景需 NAT 打洞与中继。"),
        ("MTU 分片", "大包触发分片丢包。合理设置 MSS/MTU。"),
    ],
    [
        "域名与证书：统一管理 DNS、TLS 证书（自动续期）。",
        "性能：HTTP/2 多路复用、连接复用、压缩、缓存头。",
        "安全：TLS 1.2+、HSTS、安全 Cookie 属性。",
        "故障排查：ping/traceroute/curl/Dig/nslookup 分步定位。",
    ],
    [
        "TCP 与 UDP：TCP 可靠有序、UDP 快速无连接；QUIC 在 UDP 上实现可靠与多路复用。",
        "HTTP/1.1 与 HTTP/2：多路复用、头部压缩、服务器推送；HTTP/3 基于 QUIC 降低握手延迟。",
        "负载均衡四层与七层：四层（L4）转发 IP/端口，七层（L7）按 HTTP 内容路由。",
    ],
    [
        "架构：CDN 加速静态内容、反向代理（Nginx）终结 TLS、网关统一入口。",
        "监控：延迟、丢包、带宽、HTTP 错误率；链路追踪定位跨服务延迟。",
        "安全：WAF、DDoS 防护、速率限制、访问日志审计。",
    ],
    [
        "需求：优化 Web 应用访问延迟与安全性。",
        "方案：CDN 静态加速 + HTTP/3 + TLS 1.3 + 连接池优化。",
        "要点：证书自动化、缓存策略、核心指标监控。",
        "验证：多地测速、Lighthouse、安全扫描。",
    ],
    [
        "网络问题的排查遵循分层法：物理/链路 -> 网络 -> 传输 -> 应用。",
        "HTTP 与 TLS 是现代应用的两大接触面，状态码与证书是高频故障点。",
        "性能与安全并存：加密、缓存、负载均衡是标配。",
    ],
    [
        "MDN HTTP 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTTP",
        "RFC 9110（HTTP 语义）：https://www.rfc-editor.org/rfc/rfc9110",
        "TCP/IP 详解（W. Richard Stevens）：https://www.oreilly.com/library/view/tcpip-illustrated-vol/",
        "Cloudflare 学习中心：https://www.cloudflare.com/learning/",
        "DNS 原理（RFC 1035）：https://www.rfc-editor.org/rfc/rfc1035",
    ],
    [
        "网络基础与协议，见 032-networking 模块文档。",
        "网络安全（TLS/WAF），见 033-cybersecurity 模块。",
        "负载均衡与网关，见 031-devops 模块相关文档。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供计算机网络课程。",
    ],
    [
        ("TCP 拥塞控制", [
            "慢启动：指数增长直到 ssthresh；拥塞避免：线性增长；快速重传/快速恢复处理丢包。",
            "BBR（Google）基于带宽与延迟估计，替代丢包驱动的传统算法。",
            "队列与缓冲膨胀（bufferbloat）导致延迟抖动；AQM（CoDel）缓解。",
            "调优：理解 RTT、窗口与带宽延迟积（BDP）的关系。",
        ]),
        ("HTTPS 与证书体系", [
            "TLS 握手：ClientHello -> ServerHello + 证书 -> 密钥交换 -> Finished；1.3 一轮往返完成。",
            "证书链：根 CA -> 中间 CA -> 站点证书；OCSP/CRL 吊销检查。",
            "Let's Encrypt 自动化签发与续期（ACME 协议）。",
            "配置基线：TLS 1.2+、禁用弱套件、HSTS、证书透明度。",
        ]),
    ],
)

KB_CLOUD["cybersecurity"] = _c(
    "网络安全", "加密、认证、Web 安全、渗透测试、应急响应",
    [
        "网络安全伴随计算机发展而来：1970 年代漏洞概念出现，1988 年 Morris 蠕虫推动 CERT 成立；现代安全已从“边界防御”转向“零信任”。",
        "核心框架：CIA 三元组（机密性、完整性、可用性）；STRIDE 威胁建模；OWASP Top 10 是 Web 安全事实清单。",
        "现代主题：零信任架构、供应链安全（SBOM）、云安全、DevSecOps、AI 安全；合规（等保、GDPR）驱动企业实践。",
    ],
    [
        "密码学基础：对称加密（AES）、非对称（RSA/ECC）、哈希（SHA-2/3）、HMAC；密码学是加密、签名与认证的地基。",
        "认证与授权：口令哈希（bcrypt/argon2）、MFA、Session/JWT、OAuth 2.0/OIDC、RBAC/ABAC。",
        "Web 攻击面：注入（SQL/XSS）、CSRF、SSRF、文件上传、反序列化；防御（输入校验、输出编码、CSP、SameSite）。",
        "渗透测试流程：信息收集 -> 漏洞扫描 -> 利用 -> 提权 -> 横向 -> 报告；工具（Nmap、Burp、Metasploit）。",
    ],
    [
        ("弱口令", "默认口令与弱密码是最大入口。强制策略 + MFA。"),
        ("SQL 注入", "拼接 SQL 直接执行。参数化查询 + 最小权限。"),
        ("XSS 未过滤", "反射/存储型 XSS 窃取会话。输出编码 + CSP。"),
        ("敏感信息泄露", "日志与前端暴露密钥。密钥管理 + 脱敏。"),
        ("依赖漏洞", "第三方库已知漏洞。SCA 扫描 + 更新。"),
        ("权限过度", "账号权限超出职责。最小权限 + 定期审计。"),
        ("备份缺失", "勒索软件无法恢复。离线备份 + 恢复演练。"),
        ("安全意识薄弱", "钓鱼与社会工程。培训 + 模拟演练。"),
    ],
    [
        "纵深防御：网络、主机、应用、数据多层防线。",
        "最小权限与默认拒绝。",
        "安全左移：威胁建模与扫描进 CI。",
        "事件响应预案：检测、遏制、根除、恢复、复盘。",
    ],
    [
        "白盒与黑盒：白盒审代码，黑盒测外部；红蓝对抗验证整体。",
        "等保 2.0 与 ISO 27001：合规框架驱动管理安全。",
        "传统边界与零信任：零信任默认不信任任何请求，持续验证。",
    ],
    [
        "开发安全：依赖扫描、SAST（静态）、DAST（动态）、密钥扫描。",
        "运行时：WAF、IDS/IPS、EDR、日志审计与 SIEM。",
        "应急响应：SOP 文档、证据保全、复盘报告。",
    ],
    [
        "需求：为 Web 应用建立安全基线并验证。",
        "方案：OWASP Top 10 对照加固 + 扫描 + 渗透测试。",
        "要点：输入输出编码、CSP、认证加固、日志告警。",
        "验证：漏扫报告清零高危、红队演练、事件响应演练。",
    ],
    [
        "安全是设计出来的，不是事后补救。",
        "OWASP Top 10 与 CIA 模型是入门主线。",
        "纵深防御 + 最小权限 + 持续验证构成现代基线。",
    ],
    [
        "OWASP Top 10：https://owasp.org/www-project-top-ten/",
        "OWASP Cheat Sheets：https://cheatsheetseries.owasp.org/",
        "NIST 网络安全框架：https://www.nist.gov/cyberframework",
        "CWE 数据库：https://cwe.mitre.org/",
        "PortSwigger Web Security Academy：https://portswigger.net/web-security",
    ],
    [
        "密码学与证书，见 033-cybersecurity 模块文档。",
        "Web 攻击与防御，见 033-cybersecurity 模块相关文档。",
        "网络层安全，见 032-networking 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供网络安全课程。",
    ],
    [
        ("Web 攻击链详解", [
            "注入类：SQLi（参数化防御）、XSS（输出编码 + CSP）、命令注入（白名单）。",
            "身份类：会话固定/劫持（HttpOnly + SameSite）、JWT 算法混淆（固定算法 + 校验）。",
            "逻辑类：越权（IDOR）、竞态（TOCTOU）、支付篡改（服务端重算）。",
            "防护纵深：WAF 拦截已知模式 + 应用层校验 + 监控异常。",
        ]),
        ("零信任架构", [
            "核心原则：永不信任、始终验证；身份驱动策略而非网络位置。",
            "组件：身份代理（IdP）、策略引擎（PDP）、网关（PEP）、微隔离。",
            "落地路径：先高价值资产试点，逐步覆盖；配合 MFA 与设备合规。",
            "成本与体验平衡：无密码（passkey）与连续评估是方向。",
        ]),
    ],
)

KB_CLOUD["cloud-computing"] = _c(
    "云计算", "IaaS/PaaS/SaaS、虚拟化、云原生、成本治理",
    [
        "云计算源于 1960 年代分时思想，2006 年 AWS 推出 EC2/S3 开启现代云服务时代；公有云（AWS/Azure/GCP/阿里云/华为云）与私有云、混合云并存。",
        "服务模型：IaaS（虚拟机/存储/网络）、PaaS（托管运行时/数据库）、SaaS（应用即服务）；FaaS（函数即服务）进一步抽象。",
        "云原生：容器、微服务、服务网格、声明式 API、不可变基础设施；CNCF 生态是云原生事实标准。",
    ],
    [
        "虚拟化：虚拟机（Hypervisor 硬件隔离）与容器（OS 级隔离）；虚拟化是弹性与多租户的基础。",
        "核心服务：计算（EC2/ECS）、存储（对象/块/文件）、网络（VPC/负载均衡/CDN）、数据库（托管 RDS/NoSQL）。",
        "弹性与计费：按需、预留、Spot；自动扩缩容（HPA/ASG）；FinOps 治理成本。",
        "高可用设计：多可用区、故障域、跨区域容灾；RPO/RTO 目标驱动方案。",
    ],
    [
        ("单可用区部署", "单点故障。多 AZ + 自动故障转移。"),
        ("安全组过宽", "0.0.0.0/0 全开。最小暴露 + 堡垒机。"),
        ("存储类型误选", "成本与性能失衡。按访问频率选择热/冷存储。"),
        ("实例规格浪费", "长期高配低用。右尺寸 + 弹性伸缩。"),
        ("成本失控", "无预算告警。预算 + 标签 + 异常检测。"),
        ("忽略供应商锁定", "迁移困难。优先开源标准（K8s、Terraform）。"),
        ("备份未验证", "备份不可恢复等于没有。定期恢复演练。"),
        ("密钥管理混乱", "AK 泄露事故。使用云 KMS 与临时凭证。"),
    ],
    [
        "IaC：Terraform/CloudFormation 管理资源，代码评审与审批。",
        "标签与成本分摊：环境/项目/团队标签驱动 FinOps。",
        "安全基线：CIS 基准扫描、IAM 最小权限、加密默认开启。",
        "架构评审：Well-Architected 五支柱（可靠性、安全、成本、性能、运维）。",
    ],
    [
        "公有云、私有云、混合云：公有云弹性成本优，私有云合规可控，混合云过渡。",
        "虚拟机与容器：VM 强隔离通用，容器轻量交付快。",
        "Serverless 与容器：FaaS 免运维按调用计费，容器可移植控制强。",
    ],
    [
        "云原生应用：12 要素（配置注入、无状态、日志输出）、K8s 部署、服务网格（Istio）可观测。",
        "迁移路径：Rehost（直接搬）、Replatform（小改）、Refactor（重构）、Retire。",
        "多集群管理：GitOps + 联邦/平台抽象。",
    ],
    [
        "需求：把单体 Web 应用迁移到云原生架构。",
        "方案：容器化 -> K8s 部署 -> 托管数据库 -> 监控告警。",
        "要点：无状态化、配置外置、探针、弹性伸缩。",
        "验证：故障演练（节点/区域故障）、压测弹性、成本对比。",
    ],
    [
        "云计算的本质是资源抽象与按需供给。",
        "可靠性、安全与成本是架构三支柱。",
        "云原生（容器 + 声明式 + 自动化）是主流交付形态。",
    ],
    [
        "AWS 文档：https://docs.aws.amazon.com/",
        "Microsoft Azure 文档：https://learn.microsoft.com/zh-cn/azure/",
        "Google Cloud 文档：https://cloud.google.com/docs?hl=zh-cn",
        "阿里云文档：https://help.aliyun.com/",
        "CNCF 云原生全景：https://landscape.cncf.io/",
    ],
    [
        "虚拟化与容器，见 034-cloud-computing 模块相关文档。",
        "Kubernetes 架构，见 034-cloud-computing 模块 K8s 文档。",
        "DevOps 与 IaC，见 031-devops 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供云计算课程。",
    ],
    [
        ("FinOps 成本治理", [
            "三阶段：可见（成本分配与预算）、优化（右尺寸、Spot、闲置清理）、运营（持续迭代与责任到团队）。",
            "工具：云厂商成本中心、OpenCost、Kubecost。",
            "组织：FinOps 实践者角色、定期 review、浪费告警。",
            "度量：单位成本（每请求/每用户成本）而非绝对金额。",
        ]),
        ("高可用与容灾设计", [
            "可用性数学：99.9% 年停机约 8.7 小时，99.99% 约 52 分钟；多副本降低单点风险。",
            "RPO（可容忍数据丢失）与 RTO（恢复时间）驱动备份与复制策略。",
            "模式：多可用区部署、跨区域异步复制、数据库主备、对象存储版本。",
            "演练：混沌工程（Chaos Monkey 思想）验证真实故障行为。",
        ]),
    ],
)

KB_CLOUD["iot"] = _c(
    "物联网", "传感器、协议、边缘计算、设备管理",
    [
        "物联网（IoT）指设备互联的物理网络，起源可追溯到 1980 年代传感器网络；Kevin Ashton 1999 年提出 IoT 术语，RFID 是其早期载体。",
        "架构分层：感知层（传感器/执行器）、网络层（连接）、平台层（设备管理/数据）、应用层（业务）；边缘计算将处理下沉到设备侧。",
        "协议版图：MQTT（轻量发布订阅）、CoAP（受限设备）、HTTP/HTTPS、LoRa/NB-IoT（低功耗广域）、Zigbee/BLE（短距）。",
    ],
    [
        "MQTT：基于 TCP 的发布/订阅，QoS 0/1/2 分级投递，遗嘱消息；适合低带宽高延迟网络。",
        "设备接入：设备注册、鉴权（X.509/Token）、上下行消息、影子设备（desired/reported 状态）。",
        "边缘计算：边缘网关聚合数据、本地推理与断网续传；云端统一管理。",
        "数据链路：采集 -> 清洗 -> 时序存储（InfluxDB/TDengine）-> 规则引擎 -> 应用。",
    ],
    [
        ("协议选择错误", "高功耗设备用 HTTP 轮询浪费电。低功耗场景用 MQTT/CoAP。"),
        ("安全裸奔", "设备弱口令与明文传输。证书鉴权 + TLS。"),
        ("消息乱序", "QoS 与重连导致乱序。设计幂等与序号。"),
        ("断网数据丢失", "边缘缓冲未实现。本地存储 + 续传。"),
        ("时间不同步", "设备时钟漂移影响时序。NTP 同步。"),
        ("设备风暴", "大量设备同时上报。抖动、限流与批处理。"),
        ("固件升级事故", "升级中断变砖。OTA 分批 + 回滚。"),
        ("数据量失控", "全量高频上报成本高。边缘过滤与降采样。"),
    ],
    [
        "设备全生命周期：注册、激活、监控、OTA、注销。",
        "消息幂等与 QoS 匹配业务可靠性需求。",
        "安全：唯一凭证、TLS、设备证书轮换、最小权限。",
        "数据治理：时序库 + 冷热分层 + 保留策略。",
    ],
    [
        "MQTT 与 CoAP：MQTT 可靠投递与复杂订阅；CoAP 类 HTTP 请求响应，UDP 更轻。",
        "边缘与云端计算：边缘低延迟省带宽，云端算力与全局视图。",
        "短距与广域：BLE/Zigbee 室内短距；LoRa/NB-IoT 广域低功耗。",
    ],
    [
        "平台选型：EMQX/Mosquitto 自建或云厂商 IoT 平台（阿里云 IoT、AWS IoT Core）。",
        "规则引擎：设备数据触发告警与自动化（云函数）。",
        "可视化：时序仪表盘（Grafana）+ 设备地图。",
    ],
    [
        "需求：实现温湿度监控系统（传感器 -> 网关 -> 平台 -> 告警）。",
        "方案：ESP32 采集经 MQTT 上报，EMQX 接入，规则引擎告警，Grafana 展示。",
        "要点：QoS 1、断线重连、数据时间戳、阈值告警。",
        "验证：丢包与延迟测试、断电恢复、告警准确性。",
    ],
    [
        "IoT 的关键是端-管-云协同：协议、边缘、平台缺一不可。",
        "安全与可靠性是设备规模化的前提。",
        "从最小闭环（采集-传输-展示-告警）开始迭代。",
    ],
    [
        "MQTT 规范：https://mqtt.org/",
        "CoAP（RFC 7252）：https://www.rfc-editor.org/rfc/rfc7252",
        "EMQX 文档：https://www.emqx.io/docs/zh/latest/",
        "AWS IoT Core：https://aws.amazon.com/iot-core/",
        "InfluxDB 文档：https://docs.influxdata.com/",
    ],
    [
        "MQTT 与设备接入，见 035-iot 模块文档。",
        "嵌入式 C 与硬件，见 025-c 模块。",
        "时序数据与数据平台，见 052-big-data 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供物联网课程。",
    ],
    [
        ("MQTT 协议深入", [
            "报文类型：CONNECT/CONNACK/PUBLISH/PUBACK/SUBSCRIBE/SUBACK/PINGREQ/DISCONNECT。",
            "会话状态：clean session、持久会话、消息保留（retain）与遗嘱（LWT）。",
            "QoS 语义：0 至多一次，1 至少一次，2 恰好一次；QoS2 四步握手。",
            "共享订阅（shared subscription）实现负载均衡；主题层级与通配符（+/#）。",
        ]),
        ("边缘计算架构", [
            "边缘节点形态：网关、边缘服务器、设备端推理；部署容器或原生应用。",
            "断网续传：本地消息队列 + 持久化 + 重连补传。",
            "云端协同：模型下发（边缘推理）、规则下沉、影子同步。",
            "KubeEdge/OpenYurt 把 K8s 延伸到边缘。",
        ]),
    ],
)
