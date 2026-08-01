---
order: 250
title: Networking ss 与 netstat
module: networking

category: '032-networking'
difficulty: beginner
description: Networking ss 与 netstat 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ss 基本用法

**基本写法：查看所有连接**
`ss`
```bash
# 查看所有 socket 连接
ss
```

**基本写法：查看 TCP 连接**
`ss -t`
```bash
# 查看所有 TCP 连接
ss -t
```

**基本写法：查看 UDP 连接**
`ss -u`
```bash
# 查看所有 UDP 连接
ss -u
```

**基本写法：查看监听端口**
`ss -l`
```bash
# 查看所有监听端口
ss -l
```

**基本写法：查看 TCP 监听端口**
`ss -tln`
```bash
# 查看 TCP 监听端口（数字格式）
ss -tln
```

**基本写法：查看所有连接含进程**
`ss -tlnp`
```bash
# 查看 TCP 监听端口和对应进程
ss -tlnp
```

---

## ss 详细信息

**基本写法：显示详细信息**
`ss -tlnpe`
```bash
# 显示 TCP 监听端口的扩展信息
ss -tlnpe
```

**基本写法：显示内存使用**
`ss -m`
```bash
# 显示 socket 内存使用情况
ss -m
```

**基本写法：显示内部信息**
`ss -i`
```bash
# 显示 TCP 内部信息
ss -ti
```

**基本写法：显示所有 socket 类型**
`ss -a`
```bash
# 查看所有类型的 socket
ss -a
```

---

## ss 过滤查询

**基本写法：按状态过滤**
`ss -t state <状态>`
```bash
# 查看已建立的 TCP 连接
ss -t state established
```

**基本写法：按端口过滤**
`ss -tln sport = :<端口>`
```bash
# 查看 80 端口的监听情况
ss -tln sport = :80
```

**基本写法：按目标端口过滤**
`ss -t dport = :<端口>`
```bash
# 查看连接到 443 端口的连接
ss -t dport = :443
```

**基本写法：按 IP 过滤**
`ss -t dst <IP>`
```bash
# 查看到指定 IP 的连接
ss -t dst 192.168.1.100
```

**基本写法：过滤特定状态组合**
`ss -t state connected`
```bash
# 查看所有已连接状态的 TCP
ss -t state connected
```

**基本写法：排除特定状态**
`ss -t state excluding TIME-WAIT`
```bash
# 查看除 TIME-WAIT 外的 TCP 连接
ss -t state excluding TIME-WAIT
```

---

## ss 统计信息

**基本写法：按状态统计**
`ss -s`
```bash
# 显示 socket 统计摘要
ss -s
```

**基本写法：统计各状态连接数**
`ss -ant | awk '{print $1}' | sort | uniq -c | sort -rn`
```bash
# 统计各 TCP 状态的连接数
ss -ant | awk '{print $1}' | sort | uniq -c | sort -rn
```

**基本写法：统计各端口连接数**
`ss -tn | awk '{print $4}' | cut -d: -f2 | sort | uniq -c | sort -rn`
```bash
# 统计各端口的连接数
ss -tn | awk '{print $4}' | cut -d: -f2 | sort | uniq -c | sort -rn
```

---

## netstat 经典命令

**基本写法：查看所有连接**
`netstat -a`
```bash
# 查看所有连接和监听端口
netstat -a
```

**基本写法：查看 TCP 连接**
`netstat -t`
```bash
# 查看 TCP 连接
netstat -t
```

**基本写法：查看监听端口**
`netstat -l`
```bash
# 查看所有监听端口
netstat -l
```

**基本写法：查看 TCP 监听端口含进程**
`netstat -tlnp`
```bash
# 查看 TCP 监听端口和进程（需 root）
netstat -tlnp
```

**基本写法：数字格式显示**
`netstat -n`
```bash
# 不解析主机名和端口名
netstat -tn
```

---

## netstat 统计信息

**基本写法：查看接口统计**
`netstat -i`
```bash
# 查看网络接口收发包统计
netstat -i
```

**基本写法：查看路由表**
`netstat -r`
```bash
# 查看内核路由表
netstat -r
```

**基本写法：查看协议统计**
`netstat -s`
```bash
# 查看各协议的统计信息
netstat -s
```

**基本写法：查看 TCP 统计**
`netstat -st`
```bash
# 查看 TCP 协议统计
netstat -st
```

---

## netstat 高级用法

**基本写法：持续刷新**
`netstat -c`
```bash
# 每秒刷新一次连接状态
netstat -c
```

**基本写法：查看指定端口**
`netstat -tlnp | grep <端口>`
```bash
# 查看 8080 端口占用情况
netstat -tlnp | grep 8080
```

**基本写法：统计各状态连接数**
`netstat -ant | awk '{print $6}' | sort | uniq -c | sort -rn`
```bash
# 统计 TCP 各状态连接数
netstat -ant | awk '{print $6}' | sort | uniq -c | sort -rn
```

**基本写法：查看指定进程的连接**
`netstat -tlnp | grep <进程名>`
```bash
# 查看 nginx 的监听端口
netstat -tlnp | grep nginx
```

---

## lsof 端口查看

**基本写法：查看指定端口占用**
`lsof -i :<端口>`
```bash
# 查看 80 端口的进程
lsof -i :80
```

**基本写法：查看所有网络连接**
`lsof -i`
```bash
# 查看所有网络连接
lsof -i
```

**基本写法：查看 TCP 连接**
`lsof -i tcp`
```bash
# 查看所有 TCP 连接
lsof -i tcp
```

**基本写法：查看指定进程的网络连接**
`lsof -i -a -p <PID>`
```bash
# 查看 PID 为 1234 的网络连接
lsof -i -a -p 1234
```

**基本写法：查看指定用户网络连接**
`lsof -i -u <用户>`
```bash
# 查看 root 用户的网络连接
lsof -i -u root
```

---

## TCP 状态排查

**基本写法：统计 TIME_WAIT 连接数**
`ss -ant | grep TIME-WAIT | wc -l`
```bash
# 统计 TIME_WAIT 状态连接数
ss -ant | grep TIME-WAIT | wc -l
```

**基本写法：统计 ESTABLISHED 连接数**
`ss -ant | grep ESTAB | wc -l`
```bash
# 统计已建立连接数
ss -ant | grep ESTAB | wc -l
```

**基本写法：查看指定 IP 的连接数**
`ss -tn | grep <IP> | wc -l`
```bash
# 统计到 192.168.1.100 的连接数
ss -tn | grep 192.168.1.100 | wc -l
```

**基本写法：找出连接数最多的 IP**
`ss -tn | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn | head -10`
```bash
# 找出连接数最多的前 10 个 IP
ss -tn | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn | head -10
```

---

## 常用组合命令

**基本写法：快速查看所有监听端口**
`ss -tulnp`
```bash
# 查看 TCP 和 UDP 监听端口及进程
ss -tulnp
```

**基本写法：查看连接数排行**
`ss -tn state established | awk '{print $4}' | sort | uniq -c | sort -rn`
```bash
# 查看已建立连接中本地端口连接数排行
ss -tn state established | awk '{print $4}' | sort | uniq -c | sort -rn
```

**基本写法：监控连接数变化**
`watch -n 1 'ss -s'`
```bash
# 每秒刷新 socket 统计摘要
watch -n 1 'ss -s'
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
| Networking 连通性检测 | 024-PingTraceroute | 本文的并列主题 |
| Networking ss 与 netstat | 025-SSNetstat | 本文自身 |
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
