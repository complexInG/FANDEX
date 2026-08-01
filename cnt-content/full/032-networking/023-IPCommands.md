---
order: 230
title: Networking ip 命令
module: 032-networking
category: '032-networking'
difficulty: beginner
description: Networking ip 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Networking ip 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ip addr 地址管理

**基本写法：查看所有网络接口**
`ip addr`
```bash
# 查看所有接口和 IP 地址
ip addr
```

**基本写法：简写形式**
`ip a`
```bash
# 简写查看接口信息
ip a
```

**基本写法：查看指定接口**
`ip addr show <接口>`
```bash
# 查看 eth0 接口信息
ip addr show eth0
```

**基本写法：添加 IP 地址**
`ip addr add <IP>/<前缀> dev <接口>`
```bash
# 给 eth0 添加 IP 地址
ip addr add 192.168.1.100/24 dev eth0
```

**基本写法：删除 IP 地址**
`ip addr del <IP>/<前缀> dev <接口>`
```bash
# 删除 eth0 上的 IP 地址
ip addr del 192.168.1.100/24 dev eth0
```

---

## ip link 链路管理

**基本写法：查看链路状态**
`ip link show`
```bash
# 查看所有网络接口链路状态
ip link show
```

**基本写法：启用接口**
`ip link set <接口> up`
```bash
# 启用 eth0 接口
ip link set eth0 up
```

**基本写法：禁用接口**
`ip link set <接口> down`
```bash
# 禁用 eth0 接口
ip link set eth0 down
```

**基本写法：设置 MTU**
`ip link set <接口> mtu <大小>`
```bash
# 设置 eth0 的 MTU 为 1500
ip link set eth0 mtu 1500
```

**基本写法：修改 MAC 地址**
`ip link set <接口> address <MAC>`
```bash
# 修改 eth0 的 MAC 地址
ip link set eth0 address 00:11:22:33:44:55
```

---

## ip route 路由管理

**基本写法：查看路由表**
`ip route`
```bash
# 查看完整路由表
ip route
```

**基本写法：添加默认网关**
`ip route add default via <网关>`
```bash
# 设置默认网关
ip route add default via 192.168.1.1
```

**基本写法：添加静态路由**
`ip route add <目标网络>/<前缀> via <网关>`
```bash
# 添加到 10.0.0.0/24 的路由
ip route add 10.0.0.0/24 via 192.168.1.254
```

**基本写法：通过指定接口添加路由**
`ip route add <目标网络>/<前缀> dev <接口>`
```bash
# 通过 eth0 接口添加路由
ip route add 172.16.0.0/16 dev eth0
```

**基本写法：删除路由**
`ip route del <目标网络>/<前缀>`
```bash
# 删除指定路由
ip route del 10.0.0.0/24
```

**基本写法：查看路由缓存**
`ip route get <目标IP>`
```bash
# 查看到 8.8.8.8 的路由决策
ip route get 8.8.8.8
```

---

## ip neigh 邻居表（ARP）

**基本写法：查看 ARP 表**
`ip neigh`
```bash
# 查看 ARP 邻居表
ip neigh
```

**基本写法：查看指定接口的 ARP**
`ip neigh show dev <接口>`
```bash
# 查看 eth0 接口的 ARP 表
ip neigh show dev eth0
```

**基本写法：删除 ARP 条目**
`ip neigh del <IP> dev <接口>`
```bash
# 删除指定 IP 的 ARP 条目
ip neigh del 192.168.1.100 dev eth0
```

**基本写法：刷新 ARP 缓存**
`ip neigh flush dev <接口>`
```bash
# 刷新 eth0 的 ARP 缓存
ip neigh flush dev eth0
```

---

## ip rule 策略路由

**基本写法：查看路由策略**
`ip rule`
```bash
# 查看策略路由规则
ip rule
```

**基本写法：添加策略路由规则**
`ip rule add from <源IP> table <表号>`
```bash
# 来自 192.168.1.100 的流量走表 100
ip rule add from 192.168.1.100 table 100
```

**基本写法：删除策略路由规则**
`ip rule del from <源IP> table <表号>`
```bash
# 删除策略路由规则
ip rule del from 192.168.1.100 table 100
```

---

## ip -s 统计信息

**基本写法：查看接口统计**
`ip -s link`
```bash
# 查看接口收发包统计
ip -s link
```

**基本写法：详细统计信息**
`ip -s -s link`
```bash
# 查看更详细的接口统计
ip -s -s link
```

**基本写法：查看指定接口统计**
`ip -s link show <接口>`
```bash
# 查看 eth0 的收发包统计
ip -s link show eth0
```

---

## ip monitor 监控

**基本写法：监控网络变化**
`ip monitor`
```bash
# 实时监控网络状态变化
ip monitor
```

**基本写法：监控特定类型**
`ip monitor <类型>`
```bash
# 只监控路由变化
ip monitor route
```

**基本写法：监控链路状态**
`ip monitor link`
```bash
# 监控网络接口状态变化
ip monitor link
```

---

## VLAN 与网桥

**基本写法：创建 VLAN 接口**
`ip link add link <接口> name <VLAN名> type vlan id <VLAN ID>`
```bash
# 在 eth0 上创建 VLAN 100
ip link add link eth0 name eth0.100 type vlan id 100
```

**基本写法：创建网桥**
`ip link add name <网桥名> type bridge`
```bash
# 创建 br0 网桥
ip link add name br0 type bridge
```

**基本写法：将接口加入网桥**
`ip link set <接口> master <网桥>`
```bash
# 将 eth0 加入 br0 网桥
ip link set eth0 master br0
```

**基本写法：从网桥移除接口**
`ip link set <接口> nomaster`
```bash
# 从网桥移除 eth0
ip link set eth0 nomaster
```

---

## 网络命名空间

**基本写法：创建命名空间**
`ip netns add <名称>`
```bash
# 创建名为 ns1 的网络命名空间
ip netns add ns1
```

**基本写法：列出所有命名空间**
`ip netns list`
```bash
# 列出所有网络命名空间
ip netns list
```

**基本写法：在命名空间中执行命令**
`ip netns exec <命名空间> <命令>`
```bash
# 在 ns1 中查看 IP 地址
ip netns exec ns1 ip addr
```

**基本写法：将接口移入命名空间**
`ip link set <接口> netns <命名空间>`
```bash
# 将 eth1 移入 ns1 命名空间
ip link set eth1 netns ns1
```

**基本写法：删除命名空间**
`ip netns del <名称>`
```bash
# 删除 ns1 命名空间
ip netns del ns1
```

---

## 隧道

**基本写法：创建 GRE 隧道**
`ip tunnel add <名称> mode gre remote <远端IP> local <本地IP>`
```bash
# 创建 GRE 隧道
ip tunnel add gre1 mode gre remote 10.0.0.2 local 10.0.0.1
```

**基本写法：创建 IPIP 隧道**
`ip tunnel add <名称> mode ipip remote <远端IP> local <本地IP>`
```bash
# 创建 IPIP 隧道
ip tunnel add tunl0 mode ipip remote 10.0.0.2 local 10.0.0.1
```

**基本写法：查看隧道**
`ip tunnel show`
```bash
# 查看所有隧道
ip tunnel show
```

**基本写法：删除隧道**
`ip tunnel del <名称>`
```bash
# 删除 gre1 隧道
ip tunnel del gre1
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
| Networking ip 命令 | 023-IPCommands | 本文自身 |
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
