---
order: 104
title: 隧道技术
module: networking
category: 'eng-infra'
difficulty: intermediate
description: '网络隧道技术：VxLAN、GRE、IPIP 原理与配置。'
author: fanquanpp
updated: '2026-08-01'
related:
  - networking/Keepalived双机热备
  - networking/网络命名空间与虚拟网桥
  - networking/网络故障排查工具
  - networking/BGP与多线机房互联
prerequisites:
  - networking/网络基础与协议
---

## 1. 隧道技术概述

### 1.1 封装与解封装

封装与解封装是隧道技术的重要组成部分。本节详细介绍封装与解封装的核心概念、工作原理和实际应用。

**关键要点**：

- 封装与解封装的定义与核心原理
- 封装与解封装的实现方式与技术细节
- 封装与解封装在实际场景中的应用与最佳实践
- 封装与解封装的常见问题与解决方案

封装与解封装在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 应用场景

应用场景是隧道技术的重要组成部分。本节详细介绍应用场景的核心概念、工作原理和实际应用。

**关键要点**：

- 应用场景的定义与核心原理
- 应用场景的实现方式与技术细节
- 应用场景在实际场景中的应用与最佳实践
- 应用场景的常见问题与解决方案

应用场景在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. VxLAN

### 2.1 VNI 与 MAC 学习

VNI 与 MAC 学习是隧道技术的重要组成部分。本节详细介绍VNI 与 MAC 学习的核心概念、工作原理和实际应用。

**关键要点**：

- VNI 与 MAC 学习的定义与核心原理
- VNI 与 MAC 学习的实现方式与技术细节
- VNI 与 MAC 学习在实际场景中的应用与最佳实践
- VNI 与 MAC 学习的常见问题与解决方案

VNI 与 MAC 学习在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 VTEP 配置

VTEP 配置是隧道技术的重要组成部分。本节详细介绍VTEP 配置的核心概念、工作原理和实际应用。

**关键要点**：

- VTEP 配置的定义与核心原理
- VTEP 配置的实现方式与技术细节
- VTEP 配置在实际场景中的应用与最佳实践
- VTEP 配置的常见问题与解决方案

VTEP 配置在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 EVPN 控制

EVPN 控制是隧道技术的重要组成部分。本节详细介绍EVPN 控制的核心概念、工作原理和实际应用。

**关键要点**：

- EVPN 控制的定义与核心原理
- EVPN 控制的实现方式与技术细节
- EVPN 控制在实际场景中的应用与最佳实践
- EVPN 控制的常见问题与解决方案

EVPN 控制在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. GRE

### 3.1 GRE 封装格式

GRE 封装格式是隧道技术的重要组成部分。本节详细介绍GRE 封装格式的核心概念、工作原理和实际应用。

**关键要点**：

- GRE 封装格式的定义与核心原理
- GRE 封装格式的实现方式与技术细节
- GRE 封装格式在实际场景中的应用与最佳实践
- GRE 封装格式的常见问题与解决方案

GRE 封装格式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 配置与路由

配置与路由是隧道技术的重要组成部分。本节详细介绍配置与路由的核心概念、工作原理和实际应用。

**关键要点**：

- 配置与路由的定义与核心原理
- 配置与路由的实现方式与技术细节
- 配置与路由在实际场景中的应用与最佳实践
- 配置与路由的常见问题与解决方案

配置与路由在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. IPIP

### 4.1 IPIP 封装

IPIP 封装是隧道技术的重要组成部分。本节详细介绍IPIP 封装的核心概念、工作原理和实际应用。

**关键要点**：

- IPIP 封装的定义与核心原理
- IPIP 封装的实现方式与技术细节
- IPIP 封装在实际场景中的应用与最佳实践
- IPIP 封装的常见问题与解决方案

IPIP 封装在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 与 GRE 对比

与 GRE 对比是隧道技术的重要组成部分。本节详细介绍与 GRE 对比的核心概念、工作原理和实际应用。

**关键要点**：

- 与 GRE 对比的定义与核心原理
- 与 GRE 对比的实现方式与技术细节
- 与 GRE 对比在实际场景中的应用与最佳实践
- 与 GRE 对比的常见问题与解决方案

与 GRE 对比在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

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
| 负载均衡算法 | 015-LoadBalanceAlgorithm | 本文的并列主题 |
| 高可用LVS | 016-HighAvailabilityLVS | 本文的并列主题 |
| Keepalived双机热备 | 017-KeepalivedDualHotStandby | 本文的并列主题 |
| 网络命名空间与虚拟网桥 | 018-NetworkNamespaceVirtualBridge | 本文的并列主题 |
| 隧道技术 | 019-Tunneling | 本文自身 |
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
