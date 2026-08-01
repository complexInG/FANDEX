---
order: 53
title: 无线网络
module: networking
category: 网络技术
difficulty: intermediate
description: 无线网络：WiFi标准、WLAN架构、无线安全、无线规划与优化
author: fanquanpp
updated: '2026-08-01'
related:
  - networking/交换与路由技术
  - networking/网络安全技术
  - networking/SDN与网络自动化
  - networking/网络存储技术
prerequisites:
  - networking/网络基础与协议
---

## 1. WiFi 标准演进

### 1.1 主要标准

| 标准   | IEEE     | 频段       | 最大速率  | 年份 |
| ------ | -------- | ---------- | --------- | ---- |
| WiFi 1 | 802.11b  | 2.4GHz     | 11 Mbps   | 1999 |
| WiFi 2 | 802.11a  | 5GHz       | 54 Mbps   | 1999 |
| WiFi 3 | 802.11g  | 2.4GHz     | 54 Mbps   | 2003 |
| WiFi 4 | 802.11n  | 2.4/5GHz   | 600 Mbps  | 2009 |
| WiFi 5 | 802.11ac | 5GHz       | 6.93 Gbps | 2014 |
| WiFi 6 | 802.11ax | 2.4/5/6GHz | 9.6 Gbps  | 2020 |
| WiFi 7 | 802.11be | 2.4/5/6GHz | 46 Gbps   | 2024 |

### 1.2 WiFi 6 关键技术

| 技术         | 说明                         |
| ------------ | ---------------------------- |
| OFDMA        | 正交频分多址，多用户并行传输 |
| MU-MIMO      | 多用户多入多出               |
| BSS Coloring | 减少同频干扰                 |
| TWT          | 目标唤醒时间，省电           |
| 1024-QAM     | 更高调制效率                 |

### 1.3 WiFi 7 增强

- 320MHz 信道带宽
- 4096-QAM 调制
- 多链路操作（MLO）
- 多RU分配

## 2. WLAN 架构

### 2.1 架构类型

| 架构     | 说明     | 适用场景 |
| -------- | -------- | -------- |
| 自治AP   | 独立管理 | 小型网络 |
| AC+AP    | 集中控制 | 企业网络 |
| 云管理AP | 云端管理 | 分支机构 |

### 2.2 AC+AP 架构

```
AP ←→ AC（无线控制器）←→ 核心交换机
 ↑
CAPWAP 隧道（控制+数据）
```

**CAPWAP 协议**：

- 控制隧道：UDP 5246，管理AP
- 数据隧道：UDP 5247，转发数据

### 2.3 转发模式

| 模式     | 数据路径   | 优缺点         |
| -------- | ---------- | -------------- |
| 集中转发 | AP→AC→网络 | 安全，AC压力大 |
| 本地转发 | AP→网络    | 性能好，控制弱 |

## 3. 无线安全

### 3.1 安全协议

| 协议 | 加密     | 认证       | 安全性 |
| ---- | -------- | ---------- | ------ |
| WEP  | RC4      | 共享密钥   | 已破解 |
| WPA  | TKIP     | PSK/802.1X | 弱     |
| WPA2 | AES-CCMP | PSK/802.1X | 强     |
| WPA3 | AES-GCMP | SAE/802.1X | 最强   |

### 3.2 WPA3 改进

- **SAE（Simultaneous Authentication of Equals）**：替代 PSK，防离线字典攻击
- **192位安全套件**：企业级加密
- **OWE（Opportunistic Wireless Encryption）**：开放网络加密

### 3.3 802.1X 无线认证

```
客户端 ←EAPOL→ AP ←RADIUS→ ACS/ISE
```

EAP 方法：

| 方法          | 说明                |
| ------------- | ------------------- |
| EAP-TLS       | 证书双向认证        |
| PEAP-MSCHAPv2 | 服务器证书+用户密码 |
| EAP-TTLS      | 隧道认证            |

## 4. 无线规划

### 4.1 信道规划

**2.4GHz 不重叠信道**：1、6、11

**5GHz 信道**：36~165（更多不重叠信道）

信道复用模式：

```
信道1  信道6  信道11  信道1  信道6
  AP1    AP2    AP3    AP4    AP5
```

### 4.2 功率控制

$$\text{接收功率} = P_{tx} - P_{loss} + G_{tx} + G_{rx}$$

- $P_{tx}$：发射功率
- $P_{loss}$：路径损耗
- $G_{tx}/G_{rx}$：天线增益

自由空间路径损耗：

$$FSPL = 20\log_{10}(d) + 20\log_{10}(f) + 32.44$$

### 4.3 容量规划

$$\text{AP数量} = \frac{\text{总用户数}}{\text{每AP用户数}} \times \text{冗余系数}$$

| 场景 | 每AP用户数 | 带宽/用户  |
| ---- | ---------- | ---------- |
| 办公 | 20~30      | 2~5 Mbps   |
| 会议 | 40~60      | 1~2 Mbps   |
| 密集 | 80~100     | 0.5~1 Mbps |

## 5. 无线优化

### 5.1 射频优化

- 自动信道调整
- 自动功率调整
- 射频干扰检测
- 频段引导（Band Steering）

### 5.2 漫游优化

| 漫游类型 | 延迟      | 技术                      |
| -------- | --------- | ------------------------- |
| 普通漫游 | 100~500ms | 802.11                    |
| 快速漫游 | 20~50ms   | 802.11r                   |
| OKC漫游  | 20~50ms   | Opportunistic Key Caching |

**802.11r（快速BSS转换）**：

预先在AC上缓存密钥，漫游时无需完整认证。

### 5.3 常见问题排查

| 问题     | 原因          | 解决方案        |
| -------- | ------------- | --------------- |
| 信号弱   | 距离远/障碍物 | 增加AP/调整位置 |
| 速度慢   | 干扰/拥塞     | 信道调整/5GHz   |
| 漫游掉线 | 漫游参数不当  | 启用802.11r     |
| 连接失败 | 认证问题      | 检查证书/密码   |

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
| 网络安全技术 | 006-NetworkSecurityTech | 本文的安全延伸 |
| 无线网络 | 007-WirelessNetwork | 本文自身 |
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
