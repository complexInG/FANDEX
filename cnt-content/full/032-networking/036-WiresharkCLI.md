---
order: 360
title: Networking Wireshark 命令行
module: 032-networking
category: '032-networking'
difficulty: beginner
description: Networking Wireshark 命令行 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Networking Wireshark 命令行

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## tshark 基础抓包

**基本写法:列出可用网络接口**
`tshark -D`
```bash
# 列出所有可用网络接口
tshark -D
```

**基本写法:指定接口抓包**
`tshark -i <接口>`
```bash
# 在 eth0 接口抓包
tshark -i eth0
```

**基本写法:抓取指定数量包**
`tshark -i <接口> -c <数量>`
```bash
# 抓取 100 个包后停止
tshark -i eth0 -c 100
```

**基本写法:抓包并保存到文件**
`tshark -i <接口> -w <文件>`
```bash
# 抓包保存为 pcap 文件
tshark -i eth0 -w capture.pcap
```

**基本写法:读取 pcap 文件**
`tshark -r <文件>`
```bash
# 读取并分析已抓取的 pcap 文件
tshark -r capture.pcap
```

---

## tshark 过滤抓包

**基本写法:按端口过滤**
`tshark -i <接口> -f "port <端口>"`
```bash
# 抓取 80 端口流量(BPF 过滤)
tshark -i eth0 -f "port 80"
```

**基本写法:按 IP 过滤**
`tshark -i <接口> -f "host <IP>"`
```bash
# 抓取指定 IP 的流量
tshark -i eth0 -f "host 192.168.1.1"
```

**基本写法:按协议过滤**
`tshark -i <接口> -f "<协议>"`
```bash
# 只抓取 TCP 流量
tshark -i eth0 -f "tcp"
# 只抓取 UDP 流量
tshark -i eth0 -f "udp"
```

**基本写法:多条件组合过滤**
`tshark -i <接口> -f "src <IP> and dst port <端口>"`
```bash
# 抓取源 IP 为 192.168.1.1 且目标端口为 80 的流量
tshark -i eth0 -f "src 192.168.1.1 and dst port 80"
```

**基本写法:排除特定流量**
`tshark -i <接口> -f "not port <端口>"`
```bash
# 排除 SSH 流量
tshark -i eth0 -f "not port 22"
```

---

## tshark 显示过滤

**基本写法:按 IP 过滤显示**
`tshark -r <文件> -Y "ip.addr == <IP>"`
```bash
# 显示包含指定 IP 的包
tshark -r capture.pcap -Y "ip.addr == 192.168.1.1"
```

**基本写法:按端口过滤显示**
`tshark -r <文件> -Y "tcp.port == <端口>"`
```bash
# 显示 80 端口流量
tshark -r capture.pcap -Y "tcp.port == 80"
```

**基本写法:按协议过滤显示**
`tshark -r <文件> -Y "<协议>"`
```bash
# 显示 HTTP 协议流量
tshark -r capture.pcap -Y "http"
# 显示 DNS 查询
tshark -r capture.pcap -Y "dns"
```

**基本写法:HTTP 请求方法过滤**
`tshark -r <文件> -Y "http.request.method == <方法>"`
```bash
# 显示所有 GET 请求
tshark -r capture.pcap -Y "http.request.method == GET"
```

**基本写法:组合显示过滤**
`tshark -r <文件> -Y "<条件1> and <条件2>"`
```bash
# 显示来自指定 IP 且是 HTTP 的包
tshark -r capture.pcap -Y "ip.src == 192.168.1.1 and http"
```

---

## tshark 字段提取

**基本写法:提取指定字段**
`tshark -r <文件> -T fields -e <字段>`
```bash
# 提取所有源 IP
tshark -r capture.pcap -T fields -e ip.src
```

**基本写法:提取多个字段**
`tshark -r <文件> -T fields -e <字段1> -e <字段2>`
```bash
# 提取源 IP 和目标端口
tshark -r capture.pcap -T fields -e ip.src -e tcp.dstport
```

**基本写法:提取 HTTP URL**
`tshark -r <文件> -Y http.request -T fields -e http.host -e http.request.uri`
```bash
# 提取 HTTP 访问的域名和路径
tshark -r capture.pcap -Y "http.request" -T fields -e http.host -e http.request.uri
```

**基本写法:输出 JSON 格式**
`tshark -r <文件> -T json -e <字段>`
```bash
# 以 JSON 格式输出
tshark -r capture.pcap -T json -e ip.src -e ip.dst -e tcp.dstport
```

**基本写法:带表头输出**
`tshark -r <文件> -T fields -e <字段> -E header=y -E separator=,`
```bash
# CSV 格式输出带表头
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.dstport -E header=y -E separator=,
```

---

## dumpcap 抓包工具

**基本写法:dumpcap 基本抓包**
`dumpcap -i <接口> -w <文件>`
```bash
# 使用 dumpcap 抓包(更轻量)
dumpcap -i eth0 -w capture.pcap
```

**基本写法:按大小切割文件**
`dumpcap -i <接口> -w <文件> -b filesize:<大小>`
```bash
# 每 10MB 切割一个文件
dumpcap -i eth0 -w capture.pcap -b filesize:10240
```

**基本写法:按时间切割文件**
`dumpcap -i <接口> -w <文件> -b duration:<秒>`
```bash
# 每 60 秒切割一个文件
dumpcap -i eth0 -w capture.pcap -b duration:60
```

**基本写法:限制文件数量**
`dumpcap -i <接口> -w <文件> -b files:<数量>`
```bash
# 最多保留 5 个文件,循环覆盖
dumpcap -i eth0 -w capture.pcap -b files:5 -b filesize:10240
```

**基本写法:查看接口列表**
`dumpcap -D`
```bash
# 列出所有可用接口
dumpcap -D
```

---

## tshark 协议解析

**基本写法:详细显示包内容**
`tshark -r <文件> -V`
```bash
# 详细显示每个包的协议层级
tshark -r capture.pcap -V
```

**基本写法:查看 TCP 三次握手**
`tshark -r <文件> -Y "tcp.flags.syn == 1"`
```bash
# 显示所有 SYN 包(含握手)
tshark -r capture.pcap -Y "tcp.flags.syn == 1"
# 仅握手第一个 SYN
tshark -r capture.pcap -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0"
```

**基本写法:查看 DNS 查询**
`tshark -r <文件> -Y "dns.qry.name" -T fields -e dns.qry.name`
```bash
# 提取所有 DNS 查询的域名
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name
```

**基本写法:查看 HTTP 状态码**
`tshark -r <文件> -Y "http.response.code" -T fields -e http.response.code`
```bash
# 提取所有 HTTP 响应状态码
tshark -r capture.pcap -Y "http.response.code" -T fields -e http.response.code
```

**基本写法:跟踪 TCP 流**
`tshark -r <文件> -z "follow,tcp,ascii,<流ID>"`
```bash
# 跟踪 TCP 流 0 的内容
tshark -r capture.pcap -z "follow,tcp,ascii,0"
```

---

## tshark 统计分析

**基本写法:协议层次统计**
`tshark -r <文件> -z io,phs`
```bash
# 显示协议层次结构的统计信息
tshark -r capture.pcap -z io,phs
```

**基本写法:会话统计**
`tshark -r <文件> -z conv,tcp`
```bash
# 显示 TCP 会话统计
tshark -r capture.pcap -z conv,tcp
# IP 层会话
tshark -r capture.pcap -z conv,ip
```

**基本写法:端点统计**
`tshark -r <文件> -z endpoints,ip`
```bash
# 显示 IP 端点统计
tshark -r capture.pcap -z endpoints,ip
```

**基本写法:IO 统计**
`tshark -r <文件> -z io,stat,<间隔>`
```bash
# 每 1 秒统计 IO 数据
tshark -r capture.pcap -z io,stat,1
```

**基本写法:HTTP 请求统计**
`tshark -r <文件> -z http,tree`
```bash
# HTTP 请求分布统计
tshark -r capture.pcap -z http,tree
```

---

## tshark 实时监控

**基本写法:实时显示 HTTP 请求**
`tshark -i <接口> -Y http.request -T fields -e http.host -e http.request.uri`
```bash
# 实时监控 HTTP 访问
tshark -i eth0 -Y "http.request" -T fields -e http.host -e http.request.uri
```

**基本写法:实时监控 DNS 查询**
`tshark -i <接口> -Y dns.qry.name -T fields -e dns.qry.name`
```bash
# 实时监控 DNS 查询
tshark -i eth0 -Y "dns.qry.name" -T fields -e dns.qry.name
```

**基本写法:实时统计流量**
`tshark -i <接口> -z io,stat,<间隔>`
```bash
# 实时每秒统计流量
tshark -i eth0 -z io,stat,1
```

**基本写法:实时显示新连接**
`tshark -i <接口> -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0"`
```bash
# 实时显示新的 TCP 连接
tshark -i eth0 -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0"
```

---

## tshark 高级应用

**基本写法:解密 TLS 流量**
`tshark -r <文件> -o ssl.keys_list:<IP>,<端口>,http,<密钥文件>`
```bash
# 使用私钥解密 HTTPS 流量
tshark -r capture.pcap -o "ssl.keys_list:443,http,/path/to/server.key"
```

**基本写法:提取文件**
`tshark -r <文件> --export-objects http,<目录>`
```bash
# 从 pcap 中提取 HTTP 传输的文件
tshark -r capture.pcap --export-objects http,/tmp/extracted/
```

**基本写法:统计 IP 流量排序**
`tshark -r <文件> -z conv,ip | sort -k1 -n -r`
```bash
# 按 IP 流量大小排序
tshark -r capture.pcap -z conv,ip | sort -k1 -n -r
```

**基本写法:环回接口抓包**
`tshark -i lo`
```bash
# 抓取本地环回接口流量
tshark -i lo
```

**基本写法:使用 BPF 过滤指定网段**
`tshark -i <接口> -f "net <网段>"`
```bash
# 抓取指定网段流量
tshark -i eth0 -f "net 192.168.1.0/24"
```

---

## tshark 输出格式化

**基本写法:自定义显示列**
`tshark -r <文件> -e <字段1> -e <字段2> -o gui.column.format:"<列名>,%<格式>,<列名>,%<格式>"`
```bash
# 自定义输出列
tshark -r capture.pcap -o "gui.column.format:\"Time\",\"%t\",\"Source\",\"%s\",\"Destination\",\"%d\",\"Protocol\",\"%p\""
```

**基本写法:时间格式调整**
`tshark -r <文件> -t <格式>`
```bash
# 显示绝对时间
tshark -r capture.pcap -t ad
# 显示相对时间
tshark -r capture.pcap -t r
```

**基本写法:CSV 格式输出**
`tshark -r <文件> -T fields -e <字段> -E header=y -E separator=, -E quote=d`
```bash
# 完整 CSV 格式输出
tshark -r capture.pcap -T fields -e frame.number -e ip.src -e ip.dst -e tcp.dstport -E header=y -E separator=, -E quote=d
```

**基本写法:静默模式**
`tshark -i <接口> -q -z <统计>`
```bash
# 静默模式不显示包,只显示统计
tshark -i eth0 -q -z io,stat,10
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
| Networking iptables 防火墙 | 029-IptablesFirewall | 本文的并列主题 |
| Networking SSH 远程连接 | 030-SSHRemote | 本文的并列主题 |
| Networking nc 与 nmap | 031-NetcatNmap | 本文的并列主题 |
| Networking ARP 与路由 | 032-ARPRouting | 本文的并列主题 |
| Networking HTTP 协议 | 033-HTTPProtocol | 本文的并列主题 |
| Networking wget 文件下载 | 034-WgetDownload | 本文的并列主题 |
| Networking VPN 配置命令 | 035-VPNConfig | 本文的并列主题 |
| Networking Wireshark 命令行 | 036-WiresharkCLI | 本文自身 |
| Networking IPv6 网络命令 | 037-IPv6Commands | 本文的并列主题 |
| Networking 代理配置 | 038-ProxyConfig | 本文的并列主题 |
