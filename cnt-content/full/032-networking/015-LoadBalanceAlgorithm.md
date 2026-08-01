---
order: 100
title: 负载均衡算法
module: networking
category: 'eng-infra'
difficulty: intermediate
description: 负载均衡算法：轮询、加权轮询、最少连接、一致性哈希与一致性哈希虚拟节点。
author: fanquanpp
updated: '2026-08-01'
related:
  - networking/负载均衡技术
  - networking/网络自动化
  - networking/高可用LVS
  - networking/Keepalived双机热备
prerequisites:
  - networking/网络基础与协议
---

## 1. 静态算法

### 1.1 轮询 Round Robin

轮询 Round Robin是负载均衡算法的重要组成部分。本节详细介绍轮询 Round Robin的核心概念、工作原理和实际应用。

**关键要点**：

- 轮询 Round Robin的定义与核心原理
- 轮询 Round Robin的实现方式与技术细节
- 轮询 Round Robin在实际场景中的应用与最佳实践
- 轮询 Round Robin的常见问题与解决方案

轮询 Round Robin在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 加权轮询 WRR

加权轮询 WRR是负载均衡算法的重要组成部分。本节详细介绍加权轮询 WRR的核心概念、工作原理和实际应用。

**关键要点**：

- 加权轮询 WRR的定义与核心原理
- 加权轮询 WRR的实现方式与技术细节
- 加权轮询 WRR在实际场景中的应用与最佳实践
- 加权轮询 WRR的常见问题与解决方案

加权轮询 WRR在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 哈希分流

哈希分流是负载均衡算法的重要组成部分。本节详细介绍哈希分流的核心概念、工作原理和实际应用。

**关键要点**：

- 哈希分流的定义与核心原理
- 哈希分流的实现方式与技术细节
- 哈希分流在实际场景中的应用与最佳实践
- 哈希分流的常见问题与解决方案

哈希分流在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 动态算法

### 2.1 最少连接

最少连接是负载均衡算法的重要组成部分。本节详细介绍最少连接的核心概念、工作原理和实际应用。

**关键要点**：

- 最少连接的定义与核心原理
- 最少连接的实现方式与技术细节
- 最少连接在实际场景中的应用与最佳实践
- 最少连接的常见问题与解决方案

最少连接在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 加权最少连接

加权最少连接是负载均衡算法的重要组成部分。本节详细介绍加权最少连接的核心概念、工作原理和实际应用。

**关键要点**：

- 加权最少连接的定义与核心原理
- 加权最少连接的实现方式与技术细节
- 加权最少连接在实际场景中的应用与最佳实践
- 加权最少连接的常见问题与解决方案

加权最少连接在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 最短响应时间

最短响应时间是负载均衡算法的重要组成部分。本节详细介绍最短响应时间的核心概念、工作原理和实际应用。

**关键要点**：

- 最短响应时间的定义与核心原理
- 最短响应时间的实现方式与技术细节
- 最短响应时间在实际场景中的应用与最佳实践
- 最短响应时间的常见问题与解决方案

最短响应时间在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 一致性哈希

### 3.1 原理与虚拟节点

原理与虚拟节点是负载均衡算法的重要组成部分。本节详细介绍原理与虚拟节点的核心概念、工作原理和实际应用。

**关键要点**：

- 原理与虚拟节点的定义与核心原理
- 原理与虚拟节点的实现方式与技术细节
- 原理与虚拟节点在实际场景中的应用与最佳实践
- 原理与虚拟节点的常见问题与解决方案

原理与虚拟节点在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Ketama 算法

Ketama 算法是负载均衡算法的重要组成部分。本节详细介绍Ketama 算法的核心概念、工作原理和实际应用。

**关键要点**：

- Ketama 算法的定义与核心原理
- Ketama 算法的实现方式与技术细节
- Ketama 算法在实际场景中的应用与最佳实践
- Ketama 算法的常见问题与解决方案

Ketama 算法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 节点变更影响

节点变更影响是负载均衡算法的重要组成部分。本节详细介绍节点变更影响的核心概念、工作原理和实际应用。

**关键要点**：

- 节点变更影响的定义与核心原理
- 节点变更影响的实现方式与技术细节
- 节点变更影响在实际场景中的应用与最佳实践
- 节点变更影响的常见问题与解决方案

节点变更影响在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 算法选择

### 4.1 场景对比

场景对比是负载均衡算法的重要组成部分。本节详细介绍场景对比的核心概念、工作原理和实际应用。

**关键要点**：

- 场景对比的定义与核心原理
- 场景对比的实现方式与技术细节
- 场景对比在实际场景中的应用与最佳实践
- 场景对比的常见问题与解决方案

场景对比在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 L4 vs L7 负载均衡

L4 vs L7 负载均衡是负载均衡算法的重要组成部分。本节详细介绍L4 vs L7 负载均衡的核心概念、工作原理和实际应用。

**关键要点**：

- L4 vs L7 负载均衡的定义与核心原理
- L4 vs L7 负载均衡的实现方式与技术细节
- L4 vs L7 负载均衡在实际场景中的应用与最佳实践
- L4 vs L7 负载均衡的常见问题与解决方案

L4 vs L7 负载均衡在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

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
| 无线网络 | 007-WirelessNetwork | 本文的并列主题 |
| SDN与网络自动化 | 008-SDNNetworkAutomation | 本文的并列主题 |
| 网络存储技术 | 009-NetworkStorageTechnology | 本文的并列主题 |
| 网络故障诊断 | 010-NetworkDiagnosis | 本文的并列主题 |
| 网络设计与规划 | 011-NetworkDesignPlanning | 本文的并列主题 |
| DNS与DHCP | 012-DNSDHCP | 本文的并列主题 |
| 负载均衡技术 | 013-LoadBalanceTech | 本文的并列主题 |
| 网络自动化 | 014-NetworkAutomation | 本文的并列主题 |
| 负载均衡算法 | 015-LoadBalanceAlgorithm | 本文自身 |
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
