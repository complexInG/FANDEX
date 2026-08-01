---
order: 52
title: 网络安全技术
module: networking
category: 网络技术
difficulty: intermediate
description: 网络安全技术：防火墙、IDS/IPS、VPN、NAT与访问控制
author: fanquanpp
updated: '2026-08-01'
related:
  - 'networking/OSI与TCP-IP模型'
  - networking/交换与路由技术
  - networking/无线网络
  - networking/SDN与网络自动化
prerequisites:
  - networking/网络基础与协议
---

## 1. 防火墙技术

### 1.1 防火墙类型

| 类型     | 工作层        | 检查内容     | 性能 |
| -------- | ------------- | ------------ | ---- |
| 包过滤   | 网络层        | IP/端口/协议 | 高   |
| 状态检测 | 网络层+传输层 | 连接状态     | 中   |
| 应用网关 | 应用层        | 应用协议     | 低   |
| 下一代   | 多层          | 深度包检测   | 中   |

### 1.2 安全域划分

```
Internet ←→ Untrust(外网)
               ↕
            DMZ(隔离区)：Web服务器、邮件服务器
               ↕
            Trust(内网)：办公网络
               ↕
            Management(管理区)：运维管理
```

### 1.3 防火墙配置

```bash
# Cisco ASA
access-list OUTSIDE_IN permit tcp any host 203.0.113.10 eq 80
access-list OUTSIDE_IN permit tcp any host 203.0.113.10 eq 443
access-list OUTSIDE_IN deny ip any any

access-group OUTSIDE_IN in interface outside

# NAT 配置
object network WEB_SERVER
  host 10.0.0.10
  nat (inside,outside) static 203.0.113.10
```

### 1.4 安全策略设计原则

- 默认拒绝，显式允许
- 最小权限
- 纵深防御
- 分区隔离

## 2. IDS/IPS

### 2.1 入侵检测系统

| 类型 | 部署方式 | 检测方法     |
| ---- | -------- | ------------ |
| NIDS | 旁路部署 | 网络流量分析 |
| HIDS | 主机部署 | 系统日志分析 |

### 2.2 检测方法

**特征检测**：

```bash
# Snort 规则
alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS \
  (msg:"SQL Injection Attempt"; \
   content:"UNION SELECT"; nocase; \
   sid:1000001; rev:1;)
```

**异常检测**：建立正常行为基线，偏离基线触发告警。

### 2.3 IPS 部署

```
Internet → IPS(内联) → 内部网络
              │
              ↓ 阻断恶意流量
```

IPS 在检测到攻击时主动阻断，但误报可能影响正常业务。

## 3. VPN 技术

### 3.1 VPN 类型

| 类型       | 场景     | 协议          |
| ---------- | -------- | ------------- |
| 远程访问   | 单用户   | SSL VPN, L2TP |
| 站点到站点 | 网络互联 | IPsec         |
| MPLS VPN   | 运营商   | MPLS          |

### 3.2 IPsec VPN

**IKE 阶段1（ISAKMP SA）**：

```bash
# Cisco 配置
crypto isakmp policy 10
  encryption aes-256
  hash sha256
  authentication pre-share
  group 14
  lifetime 86400

crypto isakmp key SECRET address 203.0.113.2
```

**IKE 阶段2（IPsec SA）**：

```bash
crypto ipsec transform-set TS esp-aes-256 esp-sha256-hmac

crypto map VPN 10 ipsec-isakmp
  set peer 203.0.113.2
  set transform-set TS
  match address CRYPTO_ACL

interface GigabitEthernet0/0
  crypto map VPN
```

### 3.3 SSL VPN

```
浏览器 → HTTPS → VPN网关 → 内部网络
```

优势：无需客户端，浏览器直接访问。

## 4. NAT 技术

### 4.1 NAT 类型

| 类型     | 映射方式     | 适用场景   |
| -------- | ------------ | ---------- |
| 静态NAT  | 一对一       | 服务器发布 |
| 动态NAT  | 地址池       | 内网上网   |
| NAPT/PAT | 端口多路复用 | 最常用     |

### 4.2 NAT 配置

```bash
# Cisco PAT
access-list NAT_ACL permit 10.0.0.0 0.0.0.255 any
ip nat inside source list NAT_ACL interface GigabitEthernet0/0 overload

interface GigabitEthernet0/0
  ip nat outside
interface GigabitEthernet0/1
  ip nat inside

# 静态NAT（端口转发）
ip nat inside source static tcp 10.0.0.10 80 203.0.113.10 80
```

### 4.3 NAT 穿越问题

| 协议  | 问题                | 解决方案       |
| ----- | ------------------- | -------------- |
| FTP   | 数据连接IP被NAT修改 | ALG/被动模式   |
| SIP   | SDP中IP被NAT修改    | ALG/STUN       |
| IPSec | AH校验失败          | NAT-T(UDP封装) |

## 5. 访问控制

### 5.1 ACL 类型

| 类型    | 编号范围 | 特点                |
| ------- | -------- | ------------------- |
| 标准ACL | 1~99     | 仅源IP              |
| 扩展ACL | 100~199  | 源/目标IP/端口/协议 |
| 命名ACL | -        | 可编辑              |

### 5.2 ACL 配置

```bash
# 扩展ACL
ip access-list extended WEB_ACCESS
  permit tcp any host 10.0.0.10 eq 80
  permit tcp any host 10.0.0.10 eq 443
  deny ip any any log

interface GigabitEthernet0/0
  ip access-group WEB_ACCESS in
```

### 5.3 802.1X 认证

```
客户端(Supplicant) ←EAPOL→ 交换机(Authenticator) ←RADIUS→ 认证服务器
```

```bash
# 交换机配置
aaa new-model
aaa authentication dot1x default group radius
radius server ISE
  address ipv4 10.0.0.100
  key SECRET_KEY

interface GigabitEthernet0/1
  dot1x port-control auto
```

## 6. 网络安全加固

### 6.1 设备安全

```bash
# 关闭不必要服务
no ip http server
no ip http secure-server
no cdp run
no ip source-route

# SSH 访问
line vty 0 4
  transport input ssh
  login local

# 密码加密
service password-encryption
enable secret LEVEL15
```

### 6.2 控制面安全

```bash
# 路由协议认证
router ospf 1
  area 0 authentication message-digest
  interface GigabitEthernet0/0
    ip ospf message-digest-key 1 md5 KEY

# BGP 认证
router bgp 65001
  neighbor 10.0.0.2 password BGP_KEY
```

### 6.3 管理面安全

- 使用 SNMPv3 替代 v2c
- 启用 Syslog 审计
- NTP 认证
- 配置变更管理

## 参考文献



MDN HTTP 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTTP
RFC 9110（HTTP 语义）：https://www.rfc-editor.org/rfc/rfc9110
TCP/IP 详解（W. Richard Stevens）：https://www.oreilly.com/library/view/tcpip-illustrated-vol/
Cloudflare 学习中心：https://www.cloudflare.com/learning/
DNS 原理（RFC 1035）：https://www.rfc-editor.org/rfc/rfc1035

## 延伸阅读



网络基础与协议，见 032-networking 模块文档。
网络安全（TLS/WAF），见 033-cybersecurity 模块。
负载均衡与网关，见 031-devops 模块相关文档。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供计算机网络课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 TCP 拥塞控制

慢启动：指数增长直到 ssthresh；拥塞避免：线性增长；快速重传/快速恢复处理丢包。
BBR（Google）基于带宽与延迟估计，替代丢包驱动的传统算法。
队列与缓冲膨胀（bufferbloat）导致延迟抖动；AQM（CoDel）缓解。
调优：理解 RTT、窗口与带宽延迟积（BDP）的关系。

### 13.2 HTTPS 与证书体系

TLS 握手：ClientHello -> ServerHello + 证书 -> 密钥交换 -> Finished；1.3 一轮往返完成。
证书链：根 CA -> 中间 CA -> 站点证书；OCSP/CRL 吊销检查。
Let's Encrypt 自动化签发与续期（ACME 协议）。
配置基线：TLS 1.2+、禁用弱套件、HSTS、证书透明度。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 网络基础与协议 | 001-NetworkBasicsAndProtocol | 本文的前置基础 |
| 网络系统管理 | 002-NetworkSystemManagement | 本文的并列主题 |
| 网络布线与施工 | 003-NetworkWiringAndConstruction | 本文的并列主题 |
| OSI与TCP-IP模型 | 004-OSITCPIPModel | 本文的并列主题 |
| 交换与路由技术 | 005-SwitchingAndRouting | 本文的并列主题 |
| 网络安全技术 | 006-NetworkSecurityTech | 本文自身 |
| 无线网络 | 007-WirelessNetwork | 本文的并列主题 |
| SDN与网络自动化 | 008-SDNNetworkAutomation | 本文的并列主题 |
| 网络存储技术 | 009-NetworkStorageTechnology | 本文的并列主题 |
| 网络故障诊断 | 010-NetworkDiagnosis | 本文的并列主题 |
| 网络设计与规划 | 011-NetworkDesignPlanning | 本文的并列主题 |
| DNS与DHCP | 012-DNSDHCP | 本文的并列主题 |
| 负载均衡技术 | 013-LoadBalanceTech | 本文的并列主题 |
| 网络自动化 | 014-NetworkAutomation | 本文的并列主题 |
| 负载均衡算法 | 015-LoadBalanceAlgorithm | 本文的并列主题 |
| 高可用LVS | 016-HighAvailabilityLVS | 本文的并列主题 |
| Keepalived双机热备 | 017-KeepalivedDualHotStandby | 本文的并列主题 |
| 网络命名空间与虚拟网桥 | 018-NetworkNamespaceVirtualBridge | 本文的并列主题 |
| 隧道技术 | 019-Tunneling | 本文的并列主题 |
| 网络故障排查工具 | 020-NetworkTroubleshootTools | 本文的并列主题 |
| BGP与多线机房互联 | 021-BGP | 本文的并列主题 |
| SDN | 022-SDN | 本文的并列主题 |
| Networking ip 命令 | 023-IPCommands | 本文的并列主题 |
| Networking 连通性检测 | 024-PingTraceroute | 本文的并列主题 |
| Networking ss 与 netstat | 025-SSNetstat | 本文的并列主题 |
| Networking tcpdump 抓包 | 026-Tcpdump | 本文的并列主题 |
| Networking DNS 查询 | 027-DigNslookup | 本文的并列主题 |
| Networking curl HTTP 请求 | 028-CurlHTTPRequest | 本文的并列主题 |
| Networking iptables 防火墙 | 029-IptablesFirewall | 本文的并列主题 |
| Networking SSH 远程连接 | 030-SSHRemote | 本文的并列主题 |
| Networking nc 与 nmap | 031-NetcatNmap | 本文的并列主题 |
| Networking ARP 与路由 | 032-ARPRouting | 本文的并列主题 |
| Networking HTTP 协议 | 033-HTTPProtocol | 本文的并列主题 |
| Networking wget 文件下载 | 034-WgetDownload | 本文的并列主题 |
| Networking VPN 配置命令 | 035-VPNConfig | 本文的并列主题 |
| Networking Wireshark 命令行 | 036-WiresharkCLI | 本文的并列主题 |
| Networking IPv6 网络命令 | 037-IPv6Commands | 本文的并列主题 |
| Networking 代理配置 | 038-ProxyConfig | 本文的并列主题 |
