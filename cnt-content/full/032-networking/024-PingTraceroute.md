---
order: 240
title: Networking 连通性检测
module: networking

category: '032-networking'
difficulty: beginner
description: Networking 连通性检测 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ping 连通性测试

**基本写法：测试主机连通性**
`ping <目标>`
```bash
# 测试与 example.com 的连通性
ping example.com
```

**基本写法：指定发送次数**
`ping -c <次数> <目标>`
```bash
# 发送 4 个包后停止
ping -c 4 example.com
```

**基本写法：指定包大小**
`ping -s <大小> <目标>`
```bash
# 发送 1000 字节的包
ping -s 1000 example.com
```

**基本写法：指定间隔时间**
`ping -i <秒数> <目标>`
```bash
# 每 2 秒发送一个包
ping -i 2 example.com
```

**基本写法：设置超时时间**
`ping -W <秒数> <目标>`
```bash
# 设置 3 秒超时
ping -W 3 example.com
```

**基本写法：设置总超时**
`ping -w <秒数> <目标>`
```bash
# 10 秒后自动停止
ping -w 10 example.com
```

**基本写法：泛洪 ping**
`ping -f <目标>`
```bash
# 高速发送 ping 包（需 root）
ping -f example.com
```

---

## IPv6 ping

**基本写法：ping IPv6 地址**
`ping6 <目标>`
```bash
# 测试 IPv6 连通性
ping6 -c 4 2001:4860:4860::8888
```

**基本写法：指定接口 ping6**
`ping6 -I <接口> <目标>`
```bash
# 通过 eth0 接口 ping IPv6
ping6 -I eth0 fe80::1
```

---

## traceroute 路径追踪

**基本写法：追踪路由路径**
`traceroute <目标>`
```bash
# 追踪到 example.com 的网络路径
traceroute example.com
```

**基本写法：指定最大跳数**
`traceroute -m <跳数> <目标>`
```bash
# 最多追踪 20 跳
traceroute -m 20 example.com
```

**基本写法：指定每跳探测次数**
`traceroute -q <次数> <目标>`
```bash
# 每跳探测 3 次
traceroute -q 3 example.com
```

**基本写法：指定等待时间**
`traceroute -w <秒数> <目标>`
```bash
# 每跳等待 2 秒
traceroute -w 2 example.com
```

**基本写法：使用 TCP 模式**
`traceroute -T <目标>`
```bash
# 使用 TCP SYN 探测（绕过 ICMP 限制）
traceroute -T -p 80 example.com
```

**基本写法：指定源 IP**
`traceroute -s <源IP> <目标>`
```bash
# 指定源 IP 地址
traceroute -s 192.168.1.100 example.com
```

---

## tracepath 路径 MTU 发现

**基本写法：发现路径 MTU**
`tracepath <目标>`
```bash
# 发现到 example.com 的路径 MTU
tracepath example.com
```

**基本写法：指定端口**
`tracepath -p <端口> <目标>`
```bash
# 指定目标端口
tracepath -p 8080 example.com
```

**基本写法：指定最大跳数**
`tracepath -m <跳数> <目标>`
```bash
# 最多 20 跳
tracepath -m 20 example.com
```

---

## mtr 综合网络诊断

**基本写法：实时诊断**
`mtr <目标>`
```bash
# 实时显示 ping 和 traceroute 结果
mtr example.com
```

**基本写法：报告模式**
`mtr --report <目标>`
```bash
# 生成报告模式（发送 10 次后退出）
mtr --report example.com
```

**基本写法：指定报告次数**
`mtr --report --report-cycles <次数> <目标>`
```bash
# 发送 20 次后生成报告
mtr --report --report-cycles 20 example.com
```

**基本写法：使用 TCP 模式**
`mtr --tcp <目标>`
```bash
# 使用 TCP 模式探测
mtr --tcp -P 80 example.com
```

**基本写法：使用 UDP 模式**
`mtr --udp <目标>`
```bash
# 使用 UDP 模式探测
mtr --udp example.com
```

---

## arp 地址解析

**基本写法：查看 ARP 表**
`arp -a`
```bash
# 查看所有 ARP 缓存条目
arp -a
```

**基本写法：查看指定主机 ARP**
`arp <主机>`
```bash
# 查看指定 IP 的 ARP 条目
arp 192.168.1.1
```

**基本写法：删除 ARP 条目**
`arp -d <主机>`
```bash
# 删除指定 IP 的 ARP 条目
arp -d 192.168.1.1
```

**基本写法：添加静态 ARP**
`arp -s <IP> <MAC>`
```bash
# 添加静态 ARP 绑定
arp -s 192.168.1.1 00:11:22:33:44:55
```

---

## arping ARP 请求

**基本写法：发送 ARP 请求**
`arping <IP>`
```bash
# 发送 ARP 请求检测主机
arping 192.168.1.1
```

**基本写法：指定次数**
`arping -c <次数> <IP>`
```bash
# 发送 3 次 ARP 请求
arping -c 3 192.168.1.1
```

**基本写法：指定接口**
`arping -I <接口> <IP>`
```bash
# 通过 eth0 发送 ARP 请求
arping -I eth0 192.168.1.1
```

**基本写法：检测 IP 冲突**
`arping -D <IP>`
```bash
# 检测 IP 是否被占用（重复地址检测）
arping -D 192.168.1.100
```

---

## hostname 主机名管理

**基本写法：查看主机名**
`hostname`
```bash
# 查看当前主机名
hostname
```

**基本写法：查看 FQDN**
`hostname -f`
```bash
# 查看完全限定域名
hostname -f
```

**基本写法：查看所有 IP 地址**
`hostname -I`
```bash
# 查看主机所有 IP 地址
hostname -I
```

**基本写法：临时设置主机名**
`hostname <名称>`
```bash
# 临时设置主机名
hostname myserver
```

---

## fping 批量 ping

**基本写法：批量 ping 多个主机**
`fping <IP1> <IP2> <IP3>`
```bash
# 批量 ping 多个主机
fping 192.168.1.1 192.168.1.2 192.168.1.3
```

**基本写法：扫描网段**
`fping -g <网段>`
```bash
# 扫描 192.168.1.0/24 网段
fping -g 192.168.1.0/24
```

**基本写法：只显示存活主机**
`fping -a -g <网段>`
```bash
# 只显示存活的主机
fping -a -g 192.168.1.0/24 2>/dev/null
```

**基本写法：从文件读取目标**
`fping -f <文件>`
```bash
# 从文件读取 IP 列表
fping -f iplist.txt
```

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
| 隧道技术 | 019-Tunneling | 本文的并列主题 |
| 网络故障排查工具 | 020-NetworkTroubleshootTools | 本文的并列主题 |
| BGP与多线机房互联 | 021-BGP | 本文的并列主题 |
| SDN | 022-SDN | 本文的并列主题 |
| Networking ip 命令 | 023-IPCommands | 本文的并列主题 |
| Networking 连通性检测 | 024-PingTraceroute | 本文自身 |
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
