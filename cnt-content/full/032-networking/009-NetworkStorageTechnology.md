---
order: 55
title: 网络存储技术
module: networking
category: 网络技术
difficulty: intermediate
description: 网络存储技术：SAN、NAS、iSCSI、FC、分布式存储与数据保护
author: fanquanpp
updated: '2026-08-01'
related:
  - networking/无线网络
  - networking/SDN与网络自动化
  - networking/网络故障诊断
  - networking/网络设计与规划
prerequisites:
  - networking/网络基础与协议
---

## 1. 存储架构

### 1.1 DAS/NAS/SAN

| 类型 | 协议         | 特点       | 适用     |
| ---- | ------------ | ---------- | -------- |
| DAS  | SCSI/SATA    | 直连，简单 | 小型     |
| NAS  | NFS/SMB/CIFS | 文件级共享 | 文件共享 |
| SAN  | FC/iSCSI     | 块级共享   | 数据库   |

### 1.2 块存储 vs 文件存储 vs 对象存储

| 类型     | 访问方式 | 协议     | 场景           |
| -------- | -------- | -------- | -------------- |
| 块存储   | 块设备   | FC/iSCSI | 数据库、虚拟机 |
| 文件存储 | 文件系统 | NFS/SMB  | 文件共享       |
| 对象存储 | REST API | S3/Swift | 备份、大数据   |

## 2. SAN 存储

### 2.1 FC SAN

```
服务器 ←→ HBA ←→ FC交换机 ←→ 存储阵列
              WWN标识
```

**FC 拓扑**：

| 拓扑   | 说明     | 适用     |
| ------ | -------- | -------- |
| 点对点 | 直连     | 简单     |
| FC-AL  | 仲裁环   | 少量设备 |
| Fabric | 交换网络 | 企业     |

### 2.2 iSCSI SAN

```
服务器 ←→ iSCSI Initiator ←→ IP网络 ←→ iSCSI Target ←→ 存储
```

```bash
# Linux iSCSI 配置
yum install iscsi-initiator-utils
systemctl start iscsid

# 发现目标
iscsiadm -m discovery -t st -p 10.0.0.100

# 登录目标
iscsiadm -m node -T iqn.2026-01.com.example:storage -p 10.0.0.100 -l
```

### 2.3 FCoE

FC over Ethernet，在以太网上传输 FC 帧：

- 需要无损以太网（DCB）
- 统一网络架构
- 减少 I/O 适配器

## 3. NAS 存储

### 3.1 NFS

```bash
# 服务端
mkdir /export/data
echo "/export/data 10.0.0.0/24(rw,sync,no_subtree_check)" >> /etc/exports
exportfs -a

# 客户端
mount -t nfs server:/export/data /mnt/data
```

**NFS 版本**：

| 版本    | 特点                  |
| ------- | --------------------- |
| NFSv3   | 无状态，UDP/TCP       |
| NFSv4   | 有状态，TCP，安全增强 |
| NFSv4.1 | pNFS 并行             |

### 3.2 SMB/CIFS

```bash
# Samba 配置
[share]
  path = /srv/samba/share
  browseable = yes
  read only = no
  valid users = @smbgroup
```

## 4. 分布式存储

### 4.1 Ceph

统一分布式存储：块(RBD)、文件(CephFS)、对象(RGW)

```
Ceph 架构：
  客户端 → MON(监控) → OSD(存储) → 磁盘
              ↑
           MDS(元数据，CephFS)
```

**CRUSH 算法**：确定性数据分布，避免查表。

$$\text{PG数} = \frac{\text{OSD数} \times 100}{\text{副本数}}$$

### 4.2 GlusterFS

无元数据服务器的分布式文件系统：

```
客户端 → GlusterFS Volume → Brick1(服务器1)
                            → Brick2(服务器2)
                            → Brick3(服务器3)
```

卷类型：

| 类型       | 说明   | 冗余 |
| ---------- | ------ | ---- |
| Distribute | 分布   | 无   |
| Replicate  | 复制   | 有   |
| Stripe     | 条带   | 无   |
| Disperse   | 纠删码 | 有   |

## 5. 数据保护

### 5.1 RAID

| 级别   | 最少盘 | 容错    | 利用率  | 适用     |
| ------ | ------ | ------- | ------- | -------- |
| RAID0  | 2      | 无      | 100%    | 临时数据 |
| RAID1  | 2      | 1盘     | 50%     | 系统盘   |
| RAID5  | 3      | 1盘     | (n-1)/n | 通用     |
| RAID6  | 4      | 2盘     | (n-2)/n | 重要数据 |
| RAID10 | 4      | 每组1盘 | 50%     | 数据库   |

### 5.2 快照

- 写时复制（COW）快照
- 重定向写（ROW）快照

### 5.3 备份策略

3-2-1 原则：3份副本、2种介质、1份异地。

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
| 网络存储技术 | 009-NetworkStorageTechnology | 本文自身 |
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
