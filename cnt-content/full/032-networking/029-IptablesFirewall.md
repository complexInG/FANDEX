---
order: 290
title: Networking iptables 防火墙
module: 032-networking
category: '032-networking'
difficulty: beginner
description: Networking iptables 防火墙 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## iptables 查看规则

**基本写法：查看所有规则**
`iptables -L`
```bash
# 列出所有链的规则
iptables -L
```

**基本写法：数字格式查看**
`iptables -L -n`
```bash
# 不解析主机名和端口名
iptables -L -n
```

**基本写法：显示规则编号**
`iptables -L --line-numbers`
```bash
# 显示每条规则的编号
iptables -L -n --line-numbers
```

**基本写法：显示详细信息**
`iptables -L -v`
```bash
# 显示数据包和字节数统计
iptables -L -n -v
```

**基本写法：查看指定链**
`iptables -L <链>`
```bash
# 查看 INPUT 链规则
iptables -L INPUT -n
```

**基本写法：查看 NAT 表**
`iptables -t nat -L -n`
```bash
# 查看 NAT 表规则
iptables -t nat -L -n -v
```

---

## 基本规则操作

**基本写法：允许所有入站**
`iptables -P INPUT ACCEPT`
```bash
# 设置 INPUT 链默认策略为允许
iptables -P INPUT ACCEPT
```

**基本写法：拒绝所有入站**
`iptables -P INPUT DROP`
```bash
# 设置 INPUT 链默认策略为拒绝
iptables -P INPUT DROP
```

**基本写法：追加规则**
`iptables -A <链> <规则>`
```bash
# 追加允许 80 端口的规则
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

**基本写法：插入规则**
`iptables -I <链> <位置> <规则>`
```bash
# 在 INPUT 链第 1 条插入规则
iptables -I INPUT 1 -p tcp --dport 22 -j ACCEPT
```

**基本写法：删除规则**
`iptables -D <链> <编号>`
```bash
# 删除 INPUT 链的第 3 条规则
iptables -D INPUT 3
```

**基本写法：按规则删除**
`iptables -D <链> <规则>`
```bash
# 删除指定规则
iptables -D INPUT -p tcp --dport 80 -j ACCEPT
```

---

## 协议与端口规则

**基本写法：允许 TCP 端口**
`iptables -A INPUT -p tcp --dport <端口> -j ACCEPT`
```bash
# 允许 80 端口的 TCP 入站
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

**基本写法：允许 UDP 端口**
`iptables -A INPUT -p udp --dport <端口> -j ACCEPT`
```bash
# 允许 53 端口的 UDP 入站
iptables -A INPUT -p udp --dport 53 -j ACCEPT
```

**基本写法：允许端口范围**
`iptables -A INPUT -p tcp --dport <起始>:<结束> -j ACCEPT`
```bash
# 允许 7000-8000 端口范围
iptables -A INPUT -p tcp --dport 7000:8000 -j ACCEPT
```

**基本写法：允许 ICMP**
`iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT`
```bash
# 允许 ping 请求
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
```

**基本写法：允许多端口**
`iptables -A INPUT -p tcp -m multiport --dports <端口1>,<端口2> -j ACCEPT`
```bash
# 允许 80 和 443 端口
iptables -A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT
```

---

## 源地址与目标地址

**基本写法：按源 IP 过滤**
`iptables -A INPUT -s <IP> -j ACCEPT`
```bash
# 允许来自 192.168.1.100 的所有流量
iptables -A INPUT -s 192.168.1.100 -j ACCEPT
```

**基本写法：按源网段过滤**
`iptables -A INPUT -s <网段>/<前缀> -j ACCEPT`
```bash
# 允许来自 192.168.1.0/24 网段
iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT
```

**基本写法：按目标 IP 过滤**
`iptables -A INPUT -d <IP> -j ACCEPT`
```bash
# 允许访问 192.168.1.50
iptables -A INPUT -d 192.168.1.50 -j ACCEPT
```

**基本写法：按网络接口过滤**
`iptables -A INPUT -i <接口> -j ACCEPT`
```bash
# 允许 eth0 接口的入站
iptables -A INPUT -i eth0 -j ACCEPT
```

---

## 状态匹配规则

**基本写法：允许已建立连接**
`iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT`
```bash
# 允许已建立和相关连接
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

**基本写法：允许新连接**
`iptables -A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT`
```bash
# 允许 80 端口的新连接
iptables -A INPUT -m state --state NEW -p tcp --dport 80 -j ACCEPT
```

**基本写法：使用 conntrack 模块**
`iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT`
```bash
# 使用 conntrack 模块（推荐）
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

---

## 动作类型

**基本写法：ACCEPT 接受**
`iptables -A <链> <条件> -j ACCEPT`
```bash
# 接受匹配的流量
iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT
```

**基本写法：DROP 丢弃**
`iptables -A <链> <条件> -j DROP`
```bash
# 静默丢弃匹配的流量
iptables -A INPUT -s 10.0.0.0/8 -j DROP
```

**基本写法：REJECT 拒绝**
`iptables -A <链> <条件> -j REJECT`
```bash
# 拒绝并返回错误消息
iptables -A INPUT -s 10.0.0.0/8 -j REJECT
```

**基本写法：LOG 记录日志**
`iptables -A <链> <条件> -j LOG --log-prefix "<前缀>"`
```bash
# 记录日志前缀
iptables -A INPUT -p tcp --dport 22 -j LOG --log-prefix "SSH access: "
```

**基本写法：SNAT 源地址转换**
`iptables -t nat -A POSTROUTING -o <接口> -j SNAT --to <IP>`
```bash
# 出站流量源地址转换
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to 203.0.113.1
```

**基本写法：DNAT 目标地址转换**
`iptables -t nat -A PREROUTING -i <接口> -p tcp --dport <端口> -j DNAT --to <目标IP>:<端口>`
```bash
# 端口转发到内部服务器
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.1.100:80
```

---

## 限流规则

**基本写法：限制连接速率**
`iptables -A INPUT -p tcp --dport <端口> -m limit --limit <速率> -j ACCEPT`
```bash
# 限制 80 端口每分钟最多 25 个连接
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute -j ACCEPT
```

**基本写法：限制并发连接数**
`iptables -A INPUT -p tcp --dport <端口> -m connlimit --connlimit-above <数量> -j DROP`
```bash
# 限制 SSH 并发连接数为 3
iptables -A INPUT -p tcp --dport 22 -m connlimit --connlimit-above 3 -j DROP
```

**基本写法：限制 SYN 速率**
`iptables -A INPUT -p tcp --syn -m limit --limit <速率> -j ACCEPT`
```bash
# 限制每秒 1 个 SYN 包
iptables -A INPUT -p tcp --syn -m limit --limit 1/s -j ACCEPT
```

**基本写法：防端口扫描**
`iptables -A INPUT -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit <速率> -j ACCEPT`
```bash
# 限制 RST 包速率防止端口扫描
iptables -A INPUT -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s -j ACCEPT
```

---

## 规则持久化

**基本写法：保存规则**
`iptables-save > <文件>`
```bash
# 保存当前规则到文件
iptables-save > /etc/iptables/rules.v4
```

**基本写法：恢复规则**
`iptables-restore < <文件>`
```bash
# 从文件恢复规则
iptables-restore < /etc/iptables/rules.v4
```

**基本写法：Ubuntu/Debian 持久化**
`netfilter-persistent save`
```bash
# 使用 netfilter-persistent 保存
netfilter-persistent save
```

**基本写法：CentOS/RHEL 持久化**
`service iptables save`
```bash
# CentOS 保存规则
service iptables save
```

---

## 清空规则

**基本写法：清空所有规则**
`iptables -F`
```bash
# 清空所有链的所有规则
iptables -F
```

**基本写法：清空指定链**
`iptables -F <链>`
```bash
# 清空 INPUT 链规则
iptables -F INPUT
```

**基本写法：清空 NAT 表**
`iptables -t nat -F`
```bash
# 清空 NAT 表所有规则
iptables -t nat -F
```

**基本写法：删除自定义链**
`iptables -X`
```bash
# 删除所有自定义链
iptables -X
```

**基本写法：重置计数器**
`iptables -Z`
```bash
# 清零所有规则的数据包和字节计数器
iptables -Z
```

---

## 常用防火墙配置

**基本写法：完整基础防火墙**
```bash
`iptables -F
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT`
```
```bash
# 基础防火墙配置：允许 SSH/HTTP/HTTPS，拒绝其他入站
iptables -F
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
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
| Networking DNS 查询 | 027-DigNslookup | 本文的并列主题 |
| Networking curl HTTP 请求 | 028-CurlHTTPRequest | 本文的并列主题 |
| Networking iptables 防火墙 | 029-IptablesFirewall | 本文自身 |
| Networking SSH 远程连接 | 030-SSHRemote | 本文的并列主题 |
| Networking nc 与 nmap | 031-NetcatNmap | 本文的并列主题 |
| Networking ARP 与路由 | 032-ARPRouting | 本文的并列主题 |
| Networking HTTP 协议 | 033-HTTPProtocol | 本文的并列主题 |
| Networking wget 文件下载 | 034-WgetDownload | 本文的并列主题 |
| Networking VPN 配置命令 | 035-VPNConfig | 本文的并列主题 |
| Networking Wireshark 命令行 | 036-WiresharkCLI | 本文的并列主题 |
| Networking IPv6 网络命令 | 037-IPv6Commands | 本文的并列主题 |
| Networking 代理配置 | 038-ProxyConfig | 本文的并列主题 |
