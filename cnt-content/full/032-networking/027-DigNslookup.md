---
order: 270
title: Networking DNS 查询
module: 032-networking
category: '032-networking'
difficulty: beginner
description: Networking DNS 查询 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Networking DNS 查询

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## dig 基本查询

**基本写法：查询域名 A 记录**
`dig <域名>`
```bash
# 查询 example.com 的 A 记录
dig example.com
```

**基本写法：指定记录类型**
`dig <域名> <类型>`
```bash
# 查询 MX 记录
dig example.com MX
```

**基本写法：查询简短输出**
`dig +short <域名>`
```bash
# 只输出解析的 IP 地址
dig +short example.com
```

**基本写法：指定 DNS 服务器**
`dig @<DNS服务器> <域名>`
```bash
# 使用 8.8.8.8 作为 DNS 服务器查询
dig @8.8.8.8 example.com
```

**基本写法：查询所有记录类型**
`dig <域名> ANY`
```bash
# 查询所有类型的 DNS 记录
dig example.com ANY
```

---

## dig 常用记录类型

**基本写法：查询 A 记录（IPv4）**
`dig <域名> A`
```bash
# 查询 IPv4 地址
dig example.com A
```

**基本写法：查询 AAAA 记录（IPv6）**
`dig <域名> AAAA`
```bash
# 查询 IPv6 地址
dig example.com AAAA
```

**基本写法：查询 CNAME 记录**
`dig <域名> CNAME`
```bash
# 查询别名记录
dig www.example.com CNAME
```

**基本写法：查询 NS 记录**
`dig <域名> NS`
```bash
# 查询域名服务器记录
dig example.com NS
```

**基本写法：查询 TXT 记录**
`dig <域名> TXT`
```bash
# 查询 TXT 记录
dig example.com TXT
```

**基本写法：查询 SOA 记录**
`dig <域名> SOA`
```bash
# 查询起始授权机构记录
dig example.com SOA
```

---

## dig 高级选项

**基本写法：反向查询**
`dig -x <IP>`
```bash
# 反向解析 IP 地址
dig -x 8.8.8.8
```

**基本写法：追踪解析过程**
`dig +trace <域名>`
```bash
# 显示 DNS 解析的完整路径
dig +trace example.com
```

**基本写法：显示详细统计**
`dig +stats <域名>`
```bash
# 显示查询统计信息
dig +stats example.com
```

**基本写法：指定端口号**
`dig -p <端口> <域名>`
```bash
# 指定 DNS 服务器端口
dig -p 5353 @8.8.8.8 example.com
```

**基本写法：指定 TCP 协议**
`dig +tcp <域名>`
```bash
# 使用 TCP 协议查询
dig +tcp example.com
```

**基本写法：设置超时时间**
`dig +time=<秒数> <域名>`
```bash
# 设置 5 秒超时
dig +time=5 example.com
```

---

## nslookup 查询

**基本写法：基本查询**
`nslookup <域名>`
```bash
# 查询域名 IP 地址
nslookup example.com
```

**基本写法：指定 DNS 服务器**
`nslookup <域名> <DNS服务器>`
```bash
# 使用指定 DNS 服务器查询
nslookup example.com 8.8.8.8
```

**基本写法：查询指定记录类型**
`nslookup -type=<类型> <域名>`
```bash
# 查询 MX 记录
nslookup -type=mx example.com
```

**基本写法：交互模式**
`nslookup`
```bash
# 进入交互模式
nslookup
> server 8.8.8.8
> example.com
> exit
```

**基本写法：反向解析**
`nslookup <IP>`
```bash
# 反向解析 IP 地址
nslookup 8.8.8.8
```

**基本写法：调试模式**
`nslookup -debug <域名>`
```bash
# 显示详细查询过程
nslookup -debug example.com
```

---

## host 命令

**基本写法：查询域名 IP**
`host <域名>`
```bash
# 查询域名对应的 IP
host example.com
```

**基本写法：查询指定记录类型**
`host -t <类型> <域名>`
```bash
# 查询 MX 记录
host -t MX example.com
```

**基本写法：查询所有记录**
`host -a <域名>`
```bash
# 查询所有 DNS 记录
host -a example.com
```

**基本写法：反向解析**
`host <IP>`
```bash
# 反向解析 IP 地址
host 8.8.8.8
```

**基本写法：指定 DNS 服务器**
`host <域名> <DNS服务器>`
```bash
# 指定 DNS 服务器查询
host example.com 8.8.8.8
```

**基本写法：查询域名服务器**
`host -t ns <域名>`
```bash
# 查询域名的 NS 记录
host -t ns example.com
```

---

## DNS 故障排查

**基本写法：检查域名解析**
`dig +short <域名> A`
```bash
# 快速获取域名 IP
dig +short example.com A
```

**基本写法：对比不同 DNS 解析结果**
`dig @8.8.8.8 +short example.com; dig @1.1.1.1 +short example.com`
```bash
# 对比 Google 和 Cloudflare DNS 解析结果
dig @8.8.8.8 +short example.com
dig @1.1.1.1 +short example.com
```

**基本写法：检查 DNS 缓存**
`dig +nocmd +noall +answer <域名>`
```bash
# 只显示 ANSWER 部分
dig +nocmd +noall +answer example.com
```

**基本写法：检查 TTL 值**
`dig <域名> | grep -i ttl`
```bash
# 查看记录的 TTL 值
dig example.com | grep -i ttl
```

---

## whois 域名信息

**基本写法：查询域名注册信息**
`whois <域名>`
```bash
# 查询域名 whois 信息
whois example.com
```

**基本写法：查询 IP 持有者**
`whois <IP>`
```bash
# 查询 IP 地址归属
whois 8.8.8.8
```

**基本写法：指定 whois 服务器**
`whois -h <服务器> <域名>`
```bash
# 指定 whois 服务器查询
whois -h whois.verisign-grs.com example.com
```

---

## 批量 DNS 查询

**基本写法：批量查询域名**
`for d in <域名1> <域名2>; do dig +short $d; done`
```bash
# 批量查询多个域名
for d in google.com github.com; do echo "$d: $(dig +short $d)"; done
```

**基本写法：从文件批量查询**
`while read d; do dig +short $d; done < <文件>`
```bash
# 从文件读取域名批量查询
while read d; do echo "$d: $(dig +short $d)"; done < domains.txt
```

---

## DNS 协议详解查询

**基本写法：显示完整响应**
`dig +noall +answer <域名>`
```bash
# 只显示 ANSWER 段
dig +noall +answer example.com
```

**基本写法：显示 TTL 和详细信息**
`dig +noall +comments +answer <域名>`
```bash
# 显示注释和答案
dig +noall +comments +answer example.com
```

**基本写法：查询 DNSSEC 记录**
`dig +dnssec <域名>`
```bash
# 查询 DNSSEC 相关记录
dig +dnssec example.com
```

**基本写法：查询 CDN CNAME 链**
`dig +trace +nodnssec <域名>`
```bash
# 追踪 CNAME 链
dig +trace +nodnssec www.example.com
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
| Networking ss 与 netstat | 025-SSNetstat | 本文的并列主题 |
| Networking tcpdump 抓包 | 026-Tcpdump | 本文的并列主题 |
| Networking DNS 查询 | 027-DigNslookup | 本文自身 |
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
