---
order: 10
title: networking 模块文档合集
module: 'networking'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-30'
related: []
prerequisites: []
---

<!-- ============================================================ networking/001-NetworkBasicsAndProtocol ============================================================ -->

## 1. OSI 七层模型

### 1.1 模型概述

OSI（Open Systems Interconnection）参考模型由 ISO 提出，将网络通信划分为七个层次，每层负责特定功能。

| 层次    | 名称       | 功能               | 数据单元    | 典型协议/设备        |
| :------ | :--------- | :----------------- | :---------- | :------------------- |
| 第 7 层 | 应用层     | 为应用程序提供服务 | 报文        | HTTP、FTP、SMTP、DNS |
| 第 6 层 | 表示层     | 数据格式转换、加密 | 报文        | SSL/TLS、JPEG        |
| 第 5 层 | 会话层     | 建立/管理/终止会话 | 报文        | NetBIOS、RPC         |
| 第 4 层 | 传输层     | 端到端可靠传输     | 段(Segment) | TCP、UDP             |
| 第 3 层 | 网络层     | 路由选择与寻址     | 包(Packet)  | IP、ICMP、路由器     |
| 第 2 层 | 数据链路层 | 帧的封装与传输     | 帧(Frame)   | Ethernet、交换机     |
| 第 1 层 | 物理层     | 比特流的传输       | 比特(Bit)   | 光纤、双绞线、集线器 |

### 1.2 数据封装过程

```mermaid
flowchart TD
    T0["应用数据"]
    T1["[应用层] 添加应用层头 → 报文"]
    T2["[传输层] 添加 TCP/UDP 头 → 段"]
    T3["[网络层] 添加 IP 头 → 包"]
    T4["[数据链路层] 添加帧头/帧尾 → 帧"]
    T5["[物理层] 转为比特流 → 比特"]
    T0 --> T1
    T1 --> T2
    T2 --> T3
    T3 --> T4
    T4 --> T5
```

## 2. TCP/IP 协议栈

### 2.1 TCP 三次握手

```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务器
    C->>S: SYN (seq=x) ① 客户端发起连接
    S-->>C: SYN+ACK (seq=y, ack=x+1) ② 服务器确认并发起连接
    C->>S: ACK (ack=y+1) ③ 客户端确认
    Note over C,S: 连接建立
```

### 2.2 TCP 四次挥手

```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务器
    C->>S: FIN ① 客户端请求关闭
    S-->>C: ACK ② 服务器确认
    S-->>C: FIN ③ 服务器请求关闭
    C->>S: ACK ④ 客户端确认
    Note over C,S: 连接关闭
```

### 2.3 常用协议端口

| 协议  | 端口  | 传输层  | 用途     |
| :---- | :---- | :------ | :------- |
| HTTP  | 80    | TCP     | 网页浏览 |
| HTTPS | 443   | TCP     | 安全网页 |
| SSH   | 22    | TCP     | 远程管理 |
| DNS   | 53    | UDP/TCP | 域名解析 |
| DHCP  | 67/68 | UDP     | 地址分配 |
| SMTP  | 25    | TCP     | 邮件发送 |
| FTP   | 20/21 | TCP     | 文件传输 |
| SNMP  | 161   | UDP     | 网络管理 |

## 3. IPv4/IPv6 地址规划

### 3.1 IPv4 地址分类

| 类别 | 范围                        | 默认子网掩码  | 网络规模 |
| :--- | :-------------------------- | :------------ | :------- |
| A 类 | 1.0.0.0 ~ 126.255.255.255   | 255.0.0.0     | 大型网络 |
| B 类 | 128.0.0.0 ~ 191.255.255.255 | 255.255.0.0   | 中型网络 |
| C 类 | 192.0.0.0 ~ 223.255.255.255 | 255.255.255.0 | 小型网络 |

**私有地址范围**：

- A 类：`10.0.0.0 ~ 10.255.255.255`
- B 类：`172.16.0.0 ~ 172.31.255.255`
- C 类：`192.168.0.0 ~ 192.168.255.255`

### 3.2 IPv6 地址

IPv6 地址长度 128 位，使用冒号十六进制表示：

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
缩写 → 2001:db8:85a3::8a2e:370:7334
```

| 类型     | 前缀      | 说明               |
| :------- | :-------- | :----------------- |
| 单播     | 全球路由  | 可路由的公网地址   |
| 链路本地 | fe80::/10 | 同一链路通信       |
| 唯一本地 | fc00::/7  | 等同 IPv4 私有地址 |
| 组播     | ff00::/8  | 一对多通信         |

## 4. 子网划分

### 4.1 子网掩码计算

```
IP 地址:    192.168.1.0/24
子网掩码:   255.255.255.0
主机位数:   32 - 24 = 8
可用主机数: 2^8 - 2 = 254

划分为 4 个子网（借 2 位）：
子网1: 192.168.1.0/26    范围: .1 ~ .62      广播: .63
子网2: 192.168.1.64/26   范围: .65 ~ .126    广播: .127
子网3: 192.168.1.128/26  范围: .129 ~ .190   广播: .191
子网4: 192.168.1.192/26  范围: .193 ~ .254   广播: .255
```

### 4.2 VLSM 可变长子网掩码

VLSM 允许在同一网络中使用不同长度的子网掩码，提高地址利用率：

```
需求: 3 个子网，分别需要 50、20、10 台主机

子网1 (50台): 192.168.1.0/26   → 62 台主机
子网2 (20台): 192.168.1.64/27  → 30 台主机
子网3 (10台): 192.168.1.96/28  → 14 台主机
剩余:        192.168.1.112/28 → 可继续分配
```

## 5. 路由协议

### 5.1 静态路由

```bash
# 华为设备配置静态路由
[Huawei] ip route-static 10.1.2.0 255.255.255.0 10.1.1.2

# Cisco 设备配置静态路由
Router(config)# ip route 10.1.2.0 255.255.255.0 10.1.1.2

# 默认路由
[Huawei] ip route-static 0.0.0.0 0.0.0.0 192.168.1.1
```

### 5.2 动态路由协议对比

| 协议 | 类型     | 算法         | 管理距离 | 适用场景      |
| :--- | :------- | :----------- | :------- | :------------ |
| RIP  | 距离矢量 | Bellman-Ford | 120      | 小型网络      |
| OSPF | 链路状态 | Dijkstra     | 110      | 中大型网络    |
| BGP  | 路径矢量 | 最佳路径选择 | 20/200   | 互联网/企业间 |

### 5.3 OSPF 配置

```bash
# 华为设备 OSPF 配置
[Huawei] ospf 1 router-id 1.1.1.1
[Huawei-ospf-1] area 0
[Huawei-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255

# 查看 OSPF 邻居
[Huawei] display ospf peer
```

### 5.4 BGP 基础配置

```bash
# 华为设备 BGP 配置
[Huawei] bgp 65001
[Huawei-bgp] router-id 1.1.1.1
[Huawei-bgp] peer 10.1.1.2 as-number 65002
[Huawei-bgp] ipv4-family unicast
[Huawei-bgp-af-ipv4] peer 10.1.1.2 enable
[Huawei-bgp-af-ipv4] network 192.168.1.0 255.255.255.0
```

## 6. VLAN 划分

### 6.1 VLAN 原理

VLAN（Virtual Local Area Network）将物理局域网在逻辑上划分为多个广播域，减少广播流量、提高安全性。

```bash
# 华为交换机 VLAN 配置
[Switch] vlan batch 10 20 30          # 批量创建 VLAN
[Switch] interface GigabitEthernet0/0/1
[Switch-GE0/0/1] port link-type access
[Switch-GE0/0/1] port default vlan 10

# Trunk 链路配置
[Switch] interface GigabitEthernet0/0/24
[Switch-GE0/0/24] port link-type trunk
[Switch-GE0/0/24] port trunk allow-pass vlan 10 20 30
```

### 6.2 VLAN 间路由

```bash
# 华为交换机 VLANIF 接口配置
[Switch] interface Vlanif10
[Switch-Vlanif10] ip address 192.168.10.1 24
[Switch] interface Vlanif20
[Switch-Vlanif20] ip address 192.168.20.1 24
```

## 7. 生成树技术

### 7.1 STP/RSTP/MSTP

| 协议 | 收敛速度 | 特点                        |
| :--- | :------- | :-------------------------- |
| STP  | 30~50 秒 | IEEE 802.1D，消除环路       |
| RSTP | 1~3 秒   | IEEE 802.1w，快速收敛       |
| MSTP | 1~3 秒   | IEEE 802.1s，多实例负载均衡 |

```bash
# 华为设备 MSTP 配置
[Switch] stp mode mstp
[Switch] stp region-configuration
[Switch-mst-region] region-name RG1
[Switch-mst-region] instance 1 vlan 10 20
[Switch-mst-region] instance 2 vlan 30 40
[Switch-mst-region] active region-configuration

# 设置根桥
[Switch] stp instance 1 root primary
[Switch] stp instance 2 root secondary
```

## 8. 链路聚合

链路聚合（Eth-Trunk）将多条物理链路捆绑为一条逻辑链路，提高带宽和可靠性。

```bash
# 华为设备链路聚合配置
[Switch] interface Eth-Trunk 1
[Switch-Eth-Trunk1] mode lacp-static
[Switch-Eth-Trunk1] trunkport GigabitEthernet0/0/1
[Switch-Eth-Trunk1] trunkport GigabitEthernet0/0/2
[Switch-Eth-Trunk1] port link-type trunk
[Switch-Eth-Trunk1] port trunk allow-pass vlan all

# 查看 Eth-Trunk 状态
[Switch] display eth-trunk 1
```

## 9. VRRP 协议

VRRP（Virtual Router Redundancy Protocol）实现网关冗余，多台路由器组成虚拟路由器。

```bash
# 华为设备 VRRP 配置
[RouterA] interface Vlanif10
[RouterA-Vlanif10] ip address 192.168.10.1 24
[RouterA-Vlanif10] vrrp vrid 1 virtual-ip 192.168.10.254
[RouterA-Vlanif10] vrrp vrid 1 priority 120    # 主设备优先级更高
[RouterA-Vlanif10] vrrp vrid 1 preempt-mode timer delay 20

[RouterB] interface Vlanif10
[RouterB-Vlanif10] ip address 192.168.10.2 24
[RouterB-Vlanif10] vrrp vrid 1 virtual-ip 192.168.10.254
[RouterB-Vlanif10] vrrp vrid 1 priority 100    # 备设备默认优先级
```

## 10. 广域网与隧道技术

### 10.1 广域网技术

| 技术        | 速率 | 特点                 |
| :---------- | :--- | :------------------- |
| PPP         | 可变 | 点对点协议，支持认证 |
| HDLC        | 可变 | 高级数据链路控制     |
| Frame Relay | 可变 | 帧中继，已逐渐淘汰   |
| MPLS        | 高速 | 多协议标签交换       |

### 10.2 GRE 隧道

```bash
# 华为设备 GRE 隧道配置
[RouterA] interface Tunnel0/0/1
[RouterA-Tunnel0/0/1] tunnel-protocol gre
[RouterA-Tunnel0/0/1] source 202.1.1.1
[RouterA-Tunnel0/0/1] destination 202.1.2.1
[RouterA-Tunnel0/0/1] ip address 10.1.1.1 30
```

## 11. ACL 访问控制列表

```bash
# 基本 ACL（基于源地址）
[Router] acl 2000
[Router-acl-basic-2000] rule 5 permit source 192.168.1.0 0.0.0.255
[Router-acl-basic-2000] rule 10 deny source any

# 高级 ACL（基于五元组）
[Router] acl 3000
[Router-acl-adv-3000] rule 5 permit tcp source 192.168.1.0 0.0.0.255 \
  destination 10.1.1.0 0.0.0.255 destination-port eq 80
[Router-acl-adv-3000] rule 10 deny ip source any destination any

# 应用 ACL
[Router] interface GigabitEthernet0/0/1
[Router-GE0/0/1] traffic-filter inbound acl 3000
```

## 12. SSH 安全配置

```bash
# 华为设备 SSH 配置
[Huawei] rsa local-key-pair create       # 生成 RSA 密钥对
[Huawei] aaa
[Huawei-aaa] local-user admin password cipher Admin@123
[Huawei-aaa] local-user admin service-type ssh
[Huawei-aaa] local-user admin privilege level 15
[Huawei] user-interface vty 0 4
[Huawei-ui-vty0-4] authentication-mode aaa
[Huawei-ui-vty0-4] protocol inbound ssh
[Huawei] stelnet server enable
```

## 13. SNMP 协议

```bash
# 华为设备 SNMP 配置
[Huawei] snmp-agent community read Public@123
[Huawei] snmp-agent community write Private@123
[Huawei] snmp-agent sys-info version v2c
[Huawei] snmp-agent target-host trap address udp-domain 192.168.1.100 \
  params securityname Public@123
[Huawei] snmp-agent trap enable
```

| SNMP 版本 | 认证方式     | 安全性 |
| :-------- | :----------- | :----- |
| v1        | 团体名       | 低     |
| v2c       | 团体名       | 低     |
| v3        | USM 用户认证 | 高     |

## 14. NAPT 网络地址端口转换

```bash
# 华为设备 NAPT 配置
[Router] acl 2000
[Router-acl-basic-2000] rule 5 permit source 192.168.1.0 0.0.0.255
[Router] nat address-group 1 202.1.1.10 202.1.1.20
[Router] interface GigabitEthernet0/0/1
[Router-GE0/0/1] nat outbound 2000 address-group 1

# Easy IP（直接使用接口地址）
[Router] interface GigabitEthernet0/0/1
[Router-GE0/0/1] nat outbound 2000
```

## 15. Web Portal 认证

```bash
# 华为设备 Portal 认证配置
[Switch] portal free-rule 0 destination ip 192.168.1.100 mask 255.255.255.255
[Switch] portal web-server Server1
[Switch-portal-web-server-Server1] url http://192.168.1.100/portal
[Switch] interface Vlanif10
[Switch-Vlanif10] web-auth-server Server1 direct
```

## 16. VPN 与 IPsec

### 16.1 IPsec 协议体系

| 组件     | 协议            | 功能            |
| :------- | :-------------- | :-------------- |
| 安全协议 | AH / ESP        | 数据完整性/加密 |
| 密钥管理 | IKEv1 / IKEv2   | 协商安全参数    |
| 加密算法 | AES / 3DES      | 数据加密        |
| 认证算法 | SHA2 / MD5      | 完整性验证      |
| DH 组    | Group 2/5/14/24 | 密钥交换        |

### 16.2 IPsec VPN 配置

```bash
# 华为设备 IPsec VPN 配置
# 1. 定义感兴趣流
[Router] acl 3001
[Router-acl-adv-3001] rule 5 permit ip source 192.168.1.0 0.0.0.255 \
  destination 10.1.1.0 0.0.0.255

# 2. IKE 提议
[Router] ike proposal 1
[Router-ike-proposal-1] encryption-algorithm aes-256
[Router-ike-proposal-1] dh group14
[Router-ike-proposal-1] authentication-algorithm sha2-256

# 3. IKE 对等体
[Router] ike peer Peer1 v2
[Router-ike-peer-Peer1] ike-proposal 1
[Router-ike-peer-Peer1] pre-shared-key cipher Key@123
[Router-ike-peer-Peer1] remote-address 202.1.2.1

# 4. IPsec 提议
[Router] ipsec proposal Prop1
[Router-ipsec-proposal-Prop1] encapsulation-mode tunnel
[Router-ipsec-proposal-Prop1] transform esp
[Router-ipsec-proposal-Prop1] esp authentication-algorithm sha2-256
[Router-ipsec-proposal-Prop1] esp encryption-algorithm aes-256

# 5. IPsec 策略
[Router] ipsec policy Policy1 10 isakmp
[Router-ipsec-policy-isakmp-Policy1-10] ike-peer Peer1
[Router-ipsec-policy-isakmp-Policy1-10] proposal Prop1
[Router-ipsec-policy-isakmp-Policy1-10] security acl 3001

# 6. 应用策略
[Router] interface GigabitEthernet0/0/1
[Router-GE0/0/1] ipsec policy Policy1
```
## ifconfig 接口配置

**基本写法：查看所有接口**
`ifconfig`
```bash
# 查看所有网络接口
ifconfig
```

**基本写法：查看指定接口**
`ifconfig <接口>`
```bash
# 查看 eth0 接口信息
ifconfig eth0
```

**基本写法：配置 IP 地址**
`ifconfig <接口> <IP> netmask <掩码>`
```bash
# 配置 eth0 的 IP 地址
ifconfig eth0 192.168.1.100 netmask 255.255.255.0
```

**基本写法：启用接口**
`ifconfig <接口> up`
```bash
# 启用 eth0 接口
ifconfig eth0 up
```

**基本写法：禁用接口**
`ifconfig <接口> down`
```bash
# 禁用 eth0 接口
ifconfig eth0 down
```

**基本写法：设置 MTU**
`ifconfig <接口> mtu <大小>`
```bash
# 设置 MTU 为 1500
ifconfig eth0 mtu 1500
```

---

## route 路由配置

**基本写法：查看路由表**
`route -n`
```bash
# 数字格式查看路由表
route -n
```

**基本写法：添加默认网关**
`route add default gw <网关>`
```bash
# 添加默认网关
route add default gw 192.168.1.1
```

**基本写法：添加静态路由**
`route add -net <网络> netmask <掩码> gw <网关>`
```bash
# 添加到 10.0.0.0/24 的路由
route add -net 10.0.0.0 netmask 255.255.255.0 gw 192.168.1.254
```

**基本写法：删除路由**
`route del -net <网络> netmask <掩码>`
```bash
# 删除指定路由
route del -net 10.0.0.0 netmask 255.255.255.0
```

**基本写法：通过接口添加路由**
`route add -net <网络> dev <接口>`
```bash
# 通过 eth1 接口添加路由
route add -net 172.16.0.0/16 dev eth1
```

---

## 静态 IP 配置

**基本写法：配置静态 IP（Netplan）**
```yaml
`network:
  version: 2
  ethernets:
    <接口>:
      addresses: [<IP>/<前缀>]
      gateway4: <网关>
      nameservers:
        addresses: [<DNS>]`
```
```yaml
# Ubuntu Netplan 静态 IP 配置
network:
  version: 2
  ethernets:
    eth0:
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

**基本写法：应用 Netplan 配置**
`netplan apply`
```bash
# 应用 Netplan 配置
netplan apply
```

**基本写法：配置静态 IP（ifupdown）**
```bash
`auto <接口>
iface <接口> inet static
    address <IP>
    netmask <掩码>
    gateway <网关>`
```
```bash
# /etc/network/interfaces 配置
auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    gateway 192.168.1.1
```

**基本写法：重启网络服务**
`systemctl restart networking`
```bash
# 重启网络服务
systemctl restart networking
```

---

## DHCP 配置

**基本写法：DHCP 获取 IP**
`dhclient <接口>`
```bash
# 通过 DHCP 获取 IP 地址
dhclient eth0
```

**基本写法：释放 DHCP 租约**
`dhclient -r <接口>`
```bash
# 释放 DHCP 租约
dhclient -r eth0
```

**基本写法：配置 DHCP（Netplan）**
```yaml
`network:
  version: 2
  ethernets:
    <接口>:
      dhcp4: true`
```
```yaml
# Netplan DHCP 配置
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: true
      dhcp6: true
```

---

## DNS 配置

**基本写法：查看当前 DNS**
`cat /etc/resolv.conf`
```bash
# 查看当前 DNS 配置
cat /etc/resolv.conf
```

**基本写法：设置 DNS 服务器**
`# 编辑 /etc/resolv.conf`
```bash
# 设置 DNS 服务器
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
```

**基本写法：设置 DNS 搜索域**
`# 编辑 /etc/resolv.conf`
```bash
# 设置搜索域
echo "search example.com" >> /etc/resolv.conf
```

**基本写法：使用 systemd-resolved 配置**
`# 编辑 /etc/systemd/resolved.conf`
```bash
# 配置 systemd-resolved
echo "DNS=8.8.8.8 8.8.4.4" >> /etc/systemd/resolved.conf
systemctl restart systemd-resolved
```

---

## ethtool 网卡工具

**基本写法：查看网卡信息**
`ethtool <接口>`
```bash
# 查看 eth0 网卡信息
ethtool eth0
```

**基本写法：查看网卡驱动**
`ethtool -i <接口>`
```bash
# 查看网卡驱动信息
ethtool -i eth0
```

**基本写法：查看网卡统计**
`ethtool -S <接口>`
```bash
# 查看网卡统计信息
ethtool -S eth0
```

**基本写法：设置网卡速率**
`ethtool -s <接口> speed <速率> duplex <模式>`
```bash
# 设置网卡为 1000M 全双工
ethtool -s eth0 speed 1000 duplex full autoneg off
```

**基本写法：查看网卡支持的特性**
`ethtool -k <接口>`
```bash
# 查看网卡支持的卸载特性
ethtool -k eth0
```

---

## 网络接口聚合

**基本写法：创建 bond 接口**
```bash
`modprobe bonding
ip link add bond0 type bond
ip link set eth0 master bond0
ip link set eth1 master bond0`
```
```bash
# 创建 bond0 聚合接口
modprobe bonding
ip link add bond0 type bond
ip link set eth0 master bond0
ip link set eth1 master bond0
ip link set bond0 up
```

**基本写法：配置 bond 模式**
`# /etc/modprobe.d/bonding.conf`
```bash
# 配置 bond 模式为 802.3ad
echo "options bonding mode=4 miimon=100" > /etc/modprobe.d/bonding.conf
```

---

## 网络命名规范

**基本写法：查看接口命名规则**
`ip link show`
```bash
# 查看所有网络接口
ip link show
```

**基本写法：重命名网络接口**
```bash
`ip link set <接口> down
ip link set <接口> name <新名称>
ip link set <新名称> up`
```
```bash
# 重命名 eth0 为 wan0
ip link set eth0 down
ip link set eth0 name wan0
ip link set wan0 up
```

---

## NetworkManager 管理

**基本写法：查看 nmcli 状态**
`nmcli general status`
```bash
# 查看 NetworkManager 状态
nmcli general status
```

**基本写法：查看所有连接**
`nmcli connection show`
```bash
# 列出所有网络连接
nmcli connection show
```

**基本写法：查看设备状态**
`nmcli device status`
```bash
# 查看所有网络设备状态
nmcli device status
```

**基本写法：配置静态 IP**
`nmcli connection modify <连接> ipv4.addresses <IP>/<前缀> ipv4.gateway <网关> ipv4.method manual`
```bash
# 配置静态 IP
nmcli connection modify eth0 ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual
```

**基本写法：配置 DNS**
`nmcli connection modify <连接> ipv4.dns "<DNS1> <DNS2>"`
```bash
# 配置 DNS 服务器
nmcli connection modify eth0 ipv4.dns "8.8.8.8 8.8.4.4"
```

**基本写法：启用连接**
`nmcli connection up <连接>`
```bash
# 启用网络连接
nmcli connection up eth0
```

---

## 网络故障排查

**基本写法：查看网络接口状态**
`ip -s link`
```bash
# 查看接口统计信息
ip -s link
```

**基本写法：检查网关连通性**
`ping -c 3 <网关>`
```bash
# 测试网关连通性
ping -c 3 192.168.1.1
```

**基本写法：检查 DNS 解析**
`nslookup <域名>`
```bash
# 测试 DNS 解析
nslookup example.com
```

**基本写法：查看路由路径**
`traceroute 8.8.8.8`
```bash
# 追踪到外网的路由
traceroute 8.8.8.8
```

**基本写法：重置网络配置**
`systemctl restart NetworkManager`
```bash
# 重启网络管理服务
systemctl restart NetworkManager
```

---

## IPv6 配置

**基本写法：查看 IPv6 地址**
`ip -6 addr`
```bash
# 查看所有 IPv6 地址
ip -6 addr
```

**基本写法：添加 IPv6 地址**
`ip -6 addr add <IPv6>/<前缀> dev <接口>`
```bash
# 添加 IPv6 地址
ip -6 addr add 2001:db8::100/64 dev eth0
```

**基本写法：查看 IPv6 路由**
`ip -6 route`
```bash
# 查看 IPv6 路由表
ip -6 route
```

**基本写法：禁用 IPv6**
`# /etc/sysctl.conf`
```bash
# 禁用 IPv6
echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf
echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf
sysctl -p
```

<!-- ============================================================ networking/002-NetworkSystemManagement ============================================================ -->

## 1. Windows Server 部署

### 1.1 Windows Server 版本

| 版本                | 特点                   | 适用场景     |
| :------------------ | :--------------------- | :----------- |
| Windows Server 2022 | 安全性增强、Azure 混合 | 企业生产环境 |
| Windows Server 2019 | 稳定成熟               | 通用服务器   |
| Windows Server 2016 | Nano Server            | 轻量容器化   |

### 1.2 服务器初始化

```powershell
# 修改计算机名
Rename-Computer -NewName "DC01" -Restart

# 配置静态 IP
New-NetIPAddress -InterfaceIndex 12 -IPAddress 192.168.1.10 `
  -PrefixLength 24 -DefaultGateway 192.168.1.1
Set-DnsClientServerAddress -InterfaceIndex 12 `
  -ServerAddresses 192.168.1.10,8.8.8.8

# 启用远程桌面
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' `
  -name "fDenyTSConnections" -value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# Windows Update 配置
Install-Module PSWindowsUpdate -Force
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

## 2. 活动目录域服务（AD DS）

### 2.1 域控制器安装

```powershell
# 安装 AD DS 角色
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# 提升为域控制器（新建林）
Install-ADDSForest -DomainName "fandex.local" `
  -DomainNetbiosName "FANDEX" `
  -ForestMode WinThreshold `
  -DomainMode WinThreshold `
  -DatabasePath "C:\Windows\NTDS" `
  -LogPath "C:\Windows\NTDS" `
  -SysvolPath "C:\Windows\SYSVOL" `
  -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) `
  -Force
```

### 2.2 组织单位与用户管理

```powershell
# 创建组织单位
New-ADOrganizationalUnit -Name "研发部" -Path "DC=fandex,DC=local"
New-ADOrganizationalUnit -Name "运维部" -Path "DC=fandex,DC=local"

# 批量创建用户
$users = @(
  @{Name="张三"; SamAccountName="zhangsan"; Dept="研发部"},
  @{Name="李四"; SamAccountName="lisi"; Dept="运维部"}
)
foreach ($u in $users) {
  New-ADUser -Name $u.Name -SamAccountName $u.SamAccountName `
    -UserPrincipalName "$($u.SamAccountName)@fandex.local" `
    -Path "OU=$($u.Dept),DC=fandex,DC=local" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) `
    -Enabled $true
}

# 创建安全组
New-ADGroup -Name "研发组" -GroupScope Global -Path "OU=研发部,DC=fandex,DC=local"
Add-ADGroupMember -Identity "研发组" -Members "zhangsan"
```

## 3. DNS 服务配置

### 3.1 DNS 服务器安装与配置

```powershell
# 安装 DNS 角色
Install-WindowsFeature -Name DNS -IncludeManagementTools

# 创建正向查找区域
Add-DnsServerPrimaryZone -Name "fandex.local" -ZoneFile "fandex.local.dns"

# 添加 A 记录
Add-DnsServerResourceRecordA -Name "web" -IPv4Address "192.168.1.20" `
  -ZoneName "fandex.local"

# 添加 CNAME 记录
Add-DnsServerResourceRecordCName -Name "www" -HostNameAlias "web.fandex.local" `
  -ZoneName "fandex.local"

# 添加 MX 记录
Add-DnsServerResourceRecordMX -Name "." -MailExchange "mail.fandex.local" `
  -Preference 10 -ZoneName "fandex.local"
```

### 3.2 DNS 区域类型

| 区域类型 | 说明                 | 适用场景      |
| :------- | :------------------- | :------------ |
| 主要区域 | 可读写的区域副本     | 主 DNS 服务器 |
| 辅助区域 | 只读的区域副本       | 备份 DNS      |
| 存根区域 | 仅包含 NS/SOA/A 记录 | 跨域解析      |

## 4. DHCP 服务配置

```powershell
# 安装 DHCP 角色
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# 授权 DHCP 服务器
Add-DhcpServerInDC -DnsName "DC01.fandex.local"

# 创建作用域
Add-DhcpServerv4Scope -Name "办公网" -StartRange 192.168.1.100 `
  -EndRange 192.168.1.200 -SubnetMask 255.255.255.0 `
  -State Active

# 配置作用域选项
Set-DhcpServerv4OptionValue -ScopeId 192.168.1.0 `
  -DnsServer 192.168.1.10 -Router 192.168.1.1 `
  -DnsDomain "fandex.local"

# 排除地址范围
Add-DhcpServerv4ExclusionRange -ScopeId 192.168.1.0 `
  -StartRange 192.168.1.150 -EndRange 192.168.1.160

# DHCP 保留（绑定 MAC）
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 `
  -IPAddress 192.168.1.50 -ClientId "00-15-5D-01-02-03" `
  -Description "打印机"
```

## 5. IIS Web 服务

```powershell
# 安装 IIS
Install-WindowsFeature -Name Web-Server -IncludeManagementTools

# 创建网站
New-IISSite -Name "FANDEX-Web" -PhysicalPath "C:\inetpub\fandex" `
  -BindingInformation "*:80:www.fandex.local"

# 配置 HTTPS 绑定
New-IISSiteBinding -Name "FANDEX-Web" `
  -BindingInformation "*:443:www.fandex.local" `
  -Protocol https -CertificateThumbprint (Get-ChildItem Cert:\LocalMachine\My)[0].Thumbprint

# 应用程序池配置
Set-IISAppPool -Name "FANDEX-Web Pool" -ManagedRuntimeVersion "v4.0" `
  -ProcessModelIdleTimeout "00:30:00" -PeriodicRestartTime "1.00:00:00"
```

## 6. 文件服务

```powershell
# 安装文件服务角色
Install-WindowsFeature -Name FS-FileServer -IncludeManagementTools

# 创建共享文件夹
New-Item -Path "D:\Share\Public" -ItemType Directory -Force
New-SmbShare -Name "Public" -Path "D:\Share\Public" `
  -FullAccess "FANDEX\Domain Admins" `
  -ChangeAccess "FANDEX\研发组" `
  -ReadAccess "Everyone"

# 配置 NTFS 权限
$acl = Get-Acl "D:\Share\Public"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule(
  "FANDEX\研发组", "Modify", "ContainerInherit,ObjectInherit", "None", "Allow"
)
$acl.SetAccessRule($rule)
Set-Acl "D:\Share\Public" $acl

# 配置磁盘配额
New-FsrmQuota -Path "D:\Share\Public" -Size 10GB `
  -Description "公共目录10GB配额"
```

## 7. 终端服务（RDS）

```powershell
# 安装远程桌面服务
Install-WindowsFeature -Name RDS-RD-Server,RDS-Licensing -IncludeManagementTools

# 配置 RDS 授权模式
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' `
  -Name "LicensingMode" -Value 4    # 4=Per-User

# 指定许可证服务器
Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\LicenseServers' `
  -Name "ServerName" -Value "DC01.fandex.local"
```

## 8. 组策略管理

### 8.1 常用组策略

```powershell
# 创建 GPO
New-GPO -Name "安全基线策略" -Comment "企业安全基线配置"

# 链接 GPO 到 OU
New-GPLink -Name "安全基线策略" -Target "OU=研发部,DC=fandex,DC=local"

# 配置 GPO 注册表设置
Set-GPRegistryValue -Name "安全基线策略" `
  -Key "HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\AU" `
  -ValueName "AUOptions" -Type DWord -Value 4

# 常用安全策略
# 账户锁定策略
Set-GPRegistryValue -Name "安全基线策略" `
  -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System" `
  -ValueName "LockoutBadCount" -Type DWord -Value 5

# 禁用 USB 存储
Set-GPRegistryValue -Name "安全基线策略" `
  -Key "HKLM\Software\Policies\Microsoft\Windows\RemovableStorageDevices" `
  -ValueName "Deny_All" -Type DWord -Value 1
```

## 9. Linux 服务器部署

### 9.1 基础服务配置

```bash
# 网络配置（CentOS/Rocky）
nmcli con mod ens33 ipv4.addresses 192.168.1.20/24
nmcli con mod ens33 ipv4.gateway 192.168.1.1
nmcli con mod ens33 ipv4.dns "192.168.1.10,8.8.8.8"
nmcli con mod ens33 ipv4.method manual
nmcli con up ens33

# 防火墙配置
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --permanent --add-port=8080/tcp
firewall-cmd --reload

# SELinux 管理
setenforce 0                          # 临时关闭
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config  # 永久
```

### 9.2 常用服务安装

```bash
# Nginx 安装与配置
dnf install nginx -y
systemctl enable --now nginx

# 配置虚拟主机
cat > /etc/nginx/conf.d/fandex.conf << 'EOF'
server {
    listen 80;
    server_name www.fandex.local;
    root /var/www/fandex;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
EOF

# MariaDB 安装
dnf install mariadb-server -y
systemctl enable --now mariadb
mysql_secure_installation
```

## 10. Shell 脚本编程

### 10.1 网络巡检脚本

```bash
#!/bin/bash
# 网络设备巡检脚本
# 用法: ./net_check.sh

LOG_FILE="/var/log/net_check_$(date +%Y%m%d).log"
DEVICES=("192.168.1.1" "192.168.1.2" "192.168.1.3")

echo "===== 网络巡检 $(date) =====" | tee -a $LOG_FILE

for ip in "${DEVICES[@]}"; do
    echo "--- 检查设备 $ip ---" | tee -a $LOG_FILE

    # Ping 检测
    if ping -c 3 -W 2 $ip &> /dev/null; then
        echo "[OK] $ip 可达" | tee -a $LOG_FILE
    else
        echo "[FAIL] $ip 不可达" | tee -a $LOG_FILE
    fi

    # 端口检测
    for port in 22 80 443; do
        timeout 2 bash -c "echo > /dev/tcp/$ip/$port" 2>/dev/null
        if [ $? -eq 0 ]; then
            echo "[OK] $ip:$port 开放" | tee -a $LOG_FILE
        else
            echo "[WARN] $ip:$port 关闭" | tee -a $LOG_FILE
        fi
    done
done

echo "===== 巡检完成 =====" | tee -a $LOG_FILE
```

### 10.2 自动备份脚本

```bash
#!/bin/bash
# 配置文件自动备份脚本

BACKUP_DIR="/backup/config"
DATE=$(date +%Y%m%d_%H%M%S)
RETAIN_DAYS=30

mkdir -p $BACKUP_DIR

# 备份配置文件
tar czf "$BACKUP_DIR/etc_backup_$DATE.tar.gz" /etc/
tar czf "$BACKUP_DIR/nginx_backup_$DATE.tar.gz" /etc/nginx/

# 清理过期备份
find $BACKUP_DIR -name "*.tar.gz" -mtime +$RETAIN_DAYS -delete

echo "[$DATE] 备份完成，已清理 ${RETAIN_DAYS} 天前的备份"
```

## 11. 数据中心网络搭建

### 11.1 网络架构设计

```mermaid
flowchart TD
    C[核心交换机 冗余部署] --> A1[汇聚交换机A] --> SW1[接入SW1]
    A1 --> SW2[接入SW2]
    C --> A2[汇聚交换机B] --> SW3[接入SW3]
    A2 --> SW4[接入SW4]
```

### 11.2 设备命名规范

| 位置   | 设备类型 | 命名格式             | 示例         |
| :----- | :------- | :------------------- | :----------- |
| 核心层 | 交换机   | DC-CORE-01           | DC-CORE-01   |
| 汇聚层 | 交换机   | DC-AGG-{楼栋}-01     | DC-AGG-A1-01 |
| 接入层 | 交换机   | DC-ACC-{楼层}-{编号} | DC-ACC-3F-01 |
| 防火墙 | FW       | DC-FW-01             | DC-FW-01     |
| 路由器 | RT       | DC-RT-01             | DC-RT-01     |

## 12. 无线网络规划

### 12.1 无线地勘与 AP 点位图设计

地勘流程：

1. **现场勘测**：获取建筑平面图，标注墙体材质、门窗位置
2. **信号覆盖模拟**：使用 Ekahau/iBwave 进行信号仿真
3. **AP 点位规划**：根据覆盖面积和用户密度确定 AP 数量
4. **信道规划**：2.4GHz 使用 1/6/11 信道，5GHz 使用非 DFS 信道
5. **功率调整**：边缘场强 ≥ -65dBm，重叠区域 ≥ -75dBm

### 12.2 无线认证配置

```bash
# 华为 AC 配置 WPA2-Enterprise
[AC] wlan
[AC-wlan-view] security-profile name sec-enterprise
[AC-wlan-sec-prof-sec-enterprise] security wpa2 dot1x aes

# 配置 RADIUS 服务器
[AC] radius-server template radius1
[AC-radius-radius1] radius-server authentication 192.168.1.100 1812
[AC-radius-radius1] radius-server accounting 192.168.1.100 1813
[AC-radius-radius1] radius-server shared-key cipher Radius@123

# 802.1X 认证配置
[AC] aaa
[AC-aaa] authentication-scheme auth1
[AC-aaa-authen-auth1] authentication-mode radius
[AC-aaa] domain default
[AC-aaa-domain-default] authentication-scheme auth1
[AC-aaa-domain-default] radius-server radius1
```

### 12.3 AP 隔离

```bash
# 华为 AC 配置用户隔离
[AC] wlan
[AC-wlan-view] traffic-profile name isolate
[AC-wlan-traffic-prof-isolate] user-isolate l2    # 二层隔离
[AC-wlan-traffic-prof-isolate] user-isolate l3    # 三层隔离
```

### 12.4 数据加密

| 加密方式 | 算法     | 安全级别 | 说明               |
| :------- | :------- | :------- | :----------------- |
| WEP      | RC4      | 极低     | 已淘汰             |
| WPA-TKIP | TKIP     | 低       | 兼容旧设备         |
| WPA2-AES | AES-CCMP | 高       | 企业推荐           |
| WPA3-SAE | SAE      | 最高     | 新标准，抗离线字典 |

### 12.5 AC 热备

```bash
# 华为 AC 双机热备配置
[AC1] wlan
[AC1-wlan-view] ac protect enable
[AC1-wlan-view] ac protect protect-ac 192.168.1.2 priority 6
[AC1-wlan-view] ac protect local-ac 192.168.1.1 priority 8

[AC2] wlan
[AC2-wlan-view] ac protect enable
[AC2-wlan-view] ac protect protect-ac 192.168.1.1 priority 8
[AC2-wlan-view] ac protect local-ac 192.168.1.2 priority 6
```

<!-- ============================================================ networking/003-NetworkWiringAndConstruction ============================================================ -->

## 1. 综合布线工程设计

### 1.1 综合布线系统组成

综合布线系统由六个子系统构成：

```mermaid
flowchart TD
    B[建筑群子系统<br/>园区光缆、室外管道]
    E[设备间子系统 机房配线架]
    M[管理子系统 楼层配线间]
    V[垂直干线子系统<br/>大对数电缆/光缆]
    H[水平子系统<br/>双绞线/光纤到桌面]
    W[工作区子系统<br/>信息插座/终端设备]
    E --> V
    M --> V
    V --> H
    H --> W
```

### 1.2 各子系统设计要点

| 子系统   | 传输介质             | 拓扑结构  | 设计要点            |
| :------- | :------------------- | :-------- | :------------------ |
| 工作区   | 跳线                 | 星型      | 每工位 ≥ 2 个信息点 |
| 水平     | 超5类/6类/6A类双绞线 | 星型      | 链路长度 ≤ 90m      |
| 垂直干线 | 室内多模/单模光缆    | 星型/树型 | 光纤芯数按需冗余    |
| 设备间   | 配线架/跳线          | 星型      | 环境温湿度控制      |
| 管理     | 配线架/标签          | 星型      | 标识规范、变更记录  |
| 建筑群   | 室外光缆             | 星型/环型 | 管道/直埋/架空敷设  |

### 1.3 线缆选型

| 线缆类别     | 最大传输速率 | 带宽频率 | 有效传输距离 | 典型应用        |
| :----------- | :----------- | :------- | :----------- | :-------------- |
| 超5类(Cat5e) | 1Gbps        | 100MHz   | 100m         | 百兆/千兆以太网 |
| 6类(Cat6)    | 1Gbps        | 250MHz   | 100m         | 千兆以太网      |
| 6A类(Cat6A)  | 10Gbps       | 500MHz   | 100m         | 万兆以太网      |
| 多模光缆     | 10Gbps+      | -        | 300~550m     | 楼内垂直主干    |
| 单模光缆     | 100Gbps+     | -        | 10km+        | 建筑群/远距离   |

## 2. 铜缆端接

### 2.1 T568A 与 T568B 线序

```
T568B（国内常用）:
  1-橙白  2-橙  3-绿白  4-蓝  5-蓝白  6-绿  7-棕白  8-棕

T568A:
  1-绿白  2-绿  3-橙白  4-蓝  5-蓝白  6-橙  7-棕白  8-棕
```

> **注意**：同一工程中必须统一使用一种线序标准，推荐 T568B。

### 2.2 线缆类型与用途

| 线缆类型          | 一端线序 | 另一端线序 | 用途                   |
| :---------------- | :------- | :--------- | :--------------------- |
| 直通线(Straight)  | T568B    | T568B      | 主机↔交换机、路由↔交换 |
| 交叉线(Crossover) | T568A    | T568B      | 同类设备直连           |
| 全反线(Rollover)  | 1→8翻转  | 8→1翻转    | Console 配置线         |

### 2.3 端接工艺要求

1. 剥除护套长度：15~20mm
2. 解绞长度：≤ 13mm（超5类/6类），≤ 25mm（6A类）
3. 线对保持绞合状态至端接点
4. 端接后线缆不受侧向拉力
5. 使用专用打线工具（110型/Krone型）

## 3. 光纤熔接

### 3.1 光纤类型

| 类型     | 纤芯直径 | 包层直径 | 光源  | 传输距离  | 颜色标识 |
| :------- | :------- | :------- | :---- | :-------- | :------- |
| OM1 多模 | 62.5μm   | 125μm    | LED   | 275m@10G  | 橙色     |
| OM2 多模 | 50μm     | 125μm    | LED   | 550m@1G   | 橙色     |
| OM3 多模 | 50μm     | 125μm    | VCSEL | 300m@10G  | 水蓝色   |
| OM4 多模 | 50μm     | 125μm    | VCSEL | 400m@10G  | 品红色   |
| OS2 单模 | 9μm      | 125μm    | 激光  | 10km+@10G | 黄色     |

### 3.2 光纤熔接流程

```
1. 剥缆 → 去除光缆外护套（约1.5m）
2. 剥纤 → 去除光纤涂覆层（30~40mm）
3. 清洁 → 无水酒精棉擦拭裸纤
4. 切割 → 精密光纤切割刀，切割长度 16±1mm
5. 熔接 → 光纤熔接机自动对准、放电熔接
6. 估算损耗 → 熔接机显示损耗值（应 ≤ 0.05dB）
7. 盘纤 → 在熔接盒中按规范盘绕余纤
8. 固定 → 热缩管保护熔接点
9. 测试 → OTDR 或光功率计测试链路损耗
```

### 3.3 光纤连接器类型

| 连接器 | 形状   | 插入损耗 | 特点             | 应用       |
| :----- | :----- | :------- | :--------------- | :--------- |
| SC     | 方形   | ≤ 0.3dB  | 推拉式，密度高   | 交换机光口 |
| LC     | 小方形 | ≤ 0.2dB  | 小型化，双工常用 | SFP 模块   |
| FC     | 圆形   | ≤ 0.5dB  | 螺纹锁紧，抗震   | 电信设备   |
| ST     | 圆形   | ≤ 0.5dB  | 卡口式           | 旧设备     |
| MPO    | 矩形   | ≤ 0.5dB  | 多芯（12/24芯）  | 数据中心   |

## 4. 配线架安装

### 4.1 配线架类型

| 类型        | 用途           | 安装位置        |
| :---------- | :------------- | :-------------- |
| 110 配线架  | 语音/数据端接  | 楼层配线间      |
| RJ45 配线架 | 数据网络端接   | 楼层配线间/机房 |
| 光纤配线架  | 光纤端接与分配 | 机房            |
| 理线架      | 线缆整理与导向 | 机柜            |

### 4.2 机柜安装规范

```mermaid
flowchart TD
    R[机柜标准 42U 1U=44.45mm<br/>典型布局 从上到下：<br/>42U 理线架 → 41U 交换机 → 40U 交换机 → 39U 理线架 → 38U 配线架 → 37U 配线架<br/>... → 4U UPS → 3U UPS → 2U PDU → 1U 理线架]
```

### 4.3 机柜环境要求

| 参数 | 要求          | 说明           |
| :--- | :------------ | :------------- |
| 温度 | 18°C ~ 27°C   | ASHRAE 推荐    |
| 湿度 | 40% ~ 60% RH  | 防静电、防凝露 |
| 供电 | 双路 UPS      | 单路负载 ≤ 80% |
| 接地 | 接地电阻 ≤ 1Ω | 独立接地极     |
| 净空 | 前门 ≥ 0.6m   | 后门 ≥ 0.8m    |

## 5. 理线与标识

### 5.1 理线规范

```
1. 线缆从机柜两侧分别走线（左侧/右侧）
2. 使用理线架/理线槽固定线缆走向
3. 强电与弱电分离，间距 ≥ 30cm
4. 线缆弯曲半径：
   - 双绞线 ≥ 外径 8 倍
   - 光缆 ≥ 外径 15 倍
5. 预留适当余量（约 3~5m）
6. 使用魔术贴/尼龙扎带固定（避免过紧）
```

### 5.2 标识规范

| 标识对象   | 标识格式                    | 示例                  |
| :--------- | :-------------------------- | :-------------------- |
| 线缆两端   | 楼栋-楼层-配线架号-端口号   | A-3F-PP01-05          |
| 配线架端口 | 配线架号-端口号             | PP01-05               |
| 信息插座   | 楼栋-楼层-房间号-信息点序号 | A-3F-301-02           |
| 光纤跳线   | 起点设备/端口-终点设备/端口 | SW1-G0/0/1-SW2-G0/0/1 |
| 机柜设备   | 设备类型-编号               | SW-CORE-01            |

## 6. 室外光缆敷设

### 6.1 敷设方式

| 方式 | 适用场景    | 施工要点               |
| :--- | :---------- | :--------------------- |
| 管道 | 园区主干    | 子管敷设，人手孔过渡   |
| 直埋 | 无管道区域  | 埋深 ≥ 0.8m，铺砖保护  |
| 架空 | 临时/远距离 | 钢绞线吊挂，杆距 ≤ 50m |
| 槽道 | 建筑间连廊  | 金属槽道，防火封堵     |

### 6.2 室外光缆选型

```
GYTS — 金属加强构件、松套层绞、钢-聚乙烯护套
GYTA — 金属加强构件、松套层绞、铝-聚乙烯护套
GYFTY — 非金属加强构件、松套层绞、聚乙烯护套（防雷区）
ADSS — 全介质自承式光缆（电力杆塔）
```

### 6.3 人手孔施工

```bash
# 人孔尺寸（标准）
小型人孔: 1.2m × 0.9m × 1.2m(深)
中型人孔: 1.5m × 1.2m × 1.5m(深)
大型人孔: 2.0m × 1.5m × 1.8m(深)

# 手孔尺寸
小型手孔: 0.5m × 0.4m × 0.5m(深)
大型手孔: 0.8m × 0.6m × 0.8m(深)
```

## 7. 信息模块端接

### 7.1 端接步骤

```
1. 剥除双绞线外护套约 50mm
2. 解开线对，按 T568B 线序排列
3. 将线对卡入模块 IDC 端子槽
4. 使用打线刀将线对压入并切断多余线头
5. 安装防尘盖板
6. 使用线缆测试仪验证连通性
```

### 7.2 模块类型

| 类型         | 打线方式     | 特点               |
| :----------- | :----------- | :----------------- |
| 免打线模块   | 无需打线刀   | 快速安装，成本略高 |
| 110 打线模块 | 110 打线刀   | 传统方式，可靠性高 |
| Krone 模块   | Krone 打线刀 | 欧标，接触电阻小   |

## 8. 施工工艺规范

### 8.1 线缆敷设规范

| 项目       | 规范要求                    |
| :--------- | :-------------------------- |
| 牵引力     | 双绞线 ≤ 110N，光缆 ≤ 1500N |
| 弯曲半径   | 双绞线 ≥ 8D，光缆 ≥ 15D     |
| 敷设温度   | 双绞线 ≥ 0°C，光缆 ≥ -15°C  |
| 端接余量   | 每端预留 3~5m               |
| 管线填充率 | 直管 ≤ 40%，弯管 ≤ 30%      |

### 8.2 防火封堵

```
1. 线缆穿越楼板/墙体 → 使用防火泥/防火板封堵
2. 桥架穿越防火分区 → 防火枕 + 防火泥
3. 管道穿墙 → 阻火圈 + 防火密封胶
4. 封堵厚度 ≥ 墙体/楼板厚度
```

## 9. 网络测试

### 9.1 测试类型

| 测试类型 | 测试内容           | 工具           | 标准    |
| :------- | :----------------- | :------------- | :------ |
| 验证测试 | 连通性、线序、长度 | 简易测试仪     | -       |
| 鉴定测试 | 基本性能参数       | 鉴定级测试仪   | -       |
| 认证测试 | 全部参数，出具报告 | Fluke DSX-8000 | TIA-568 |

### 9.2 关键测试参数

| 参数                 | Cat5e 要求 | Cat6 要求 | Cat6A 要求 |
| :------------------- | :--------- | :-------- | :--------- |
| 接线图               | 正确       | 正确      | 正确       |
| 长度                 | ≤ 100m     | ≤ 100m    | ≤ 100m     |
| 衰减(Insertion Loss) | ≤ 21.7dB   | ≤ 20.9dB  | ≤ 20.3dB   |
| 近端串扰(NEXT)       | ≥ 30.1dB   | ≥ 39.9dB  | ≥ 39.9dB   |
| 综合近端串扰(PSNEXT) | ≥ 27.1dB   | ≥ 37.1dB  | ≥ 37.1dB   |
| 回波损耗(RL)         | ≥ 14.0dB   | ≥ 15.0dB  | ≥ 15.0dB   |

### 9.3 光纤链路测试

```bash
# 光功率计测试（衰减法）
1. 校准光源和光功率计
2. 发送端接入光源，接收端接入光功率计
3. 记录光功率值，计算链路损耗

# OTDR 测试（时域反射法）
1. 设置参数：波长 1310/1550nm，脉宽、量程
2. 连接 OTDR 至光纤链路
3. 分析事件表：熔接点、连接器、断裂点
4. 判断链路质量

# 链路损耗预算
损耗 = 光纤衰减 + 熔接损耗 + 连接器损耗 + 余量
     = (0.35dB/km × L) + (0.05dB × N_熔接) + (0.3dB × N_连接器) + 3dB
```

## 10. 项目组织管理

### 10.1 项目阶段

```
需求调研 → 方案设计 → 招标采购 → 施工实施 → 测试验收 → 运维移交
```

### 10.2 项目文档

| 文档类型     | 内容                         | 阶段     |
| :----------- | :--------------------------- | :------- |
| 需求规格书   | 用户需求、功能要求           | 需求调研 |
| 设计方案     | 系统架构、设备选型、图纸     | 方案设计 |
| 施工组织设计 | 施工计划、人员安排、安全措施 | 施工准备 |
| 测试报告     | 认证测试结果、问题记录       | 测试验收 |
| 竣工文档     | 竣工图纸、设备清单、配置表   | 竣工移交 |
| 验收报告     | 验收结论、遗留问题           | 验收     |

### 10.3 施工安全管理

```
1. 施工人员佩戴安全帽、绝缘手套
2. 高空作业系安全带，2m 以上需审批
3. 用电设备接地良好，使用漏电保护器
4. 光纤施工佩戴护目镜，废纤收集处理
5. 每日施工前安全交底，每周安全例会
6. 施工现场设置警示标志和围挡
```

### 10.4 质量控制要点

| 控制环节 | 检查内容               | 频率      |
| :------- | :--------------------- | :-------- |
| 材料进场 | 型号规格、外观、合格证 | 每批次    |
| 管线敷设 | 路由、间距、固定、标识 | 每日巡检  |
| 线缆端接 | 线序、工艺、标签       | 100% 检查 |
| 设备安装 | 位置、固定、接地、标签 | 逐台检查  |
| 系统测试 | 认证测试、功能测试     | 100% 测试 |

<!-- ============================================================ networking/004-OSITCPIPModel ============================================================ -->

## 1. OSI 七层模型详解

### 1.1 各层功能

| 层级 | 名称       | 功能         | PDU         | 设备   |
| ---- | ---------- | ------------ | ----------- | ------ |
| 7    | 应用层     | 网络服务接口 | 数据        | 网关   |
| 6    | 表示层     | 数据格式转换 | 数据        | -      |
| 5    | 会话层     | 会话管理     | 数据        | -      |
| 4    | 传输层     | 端到端通信   | 段(Segment) | 防火墙 |
| 3    | 网络层     | 路由寻址     | 包(Packet)  | 路由器 |
| 2    | 数据链路层 | 帧传输       | 帧(Frame)   | 交换机 |
| 1    | 物理层     | 比特传输     | 比特(Bit)   | 集线器 |

### 1.2 数据封装过程

```
应用数据
    ↓ + 应用层头
表示层PDU
    ↓ + 表示层头
会话层PDU
    ↓ + TCP/UDP头
传输层段(Segment)
    ↓ + IP头
网络层包(Packet)
    ↓ + 帧头+帧尾
数据链路层帧(Frame)
    ↓
物理层比特流(Bit)
```

## 2. TCP/IP 模型

### 2.1 四层结构

| TCP/IP 层  | 对应 OSI 层 | 协议                 |
| ---------- | ----------- | -------------------- |
| 应用层     | 5/6/7       | HTTP, DNS, SMTP, FTP |
| 传输层     | 4           | TCP, UDP, SCTP       |
| 网际层     | 3           | IP, ICMP, ARP        |
| 网络接口层 | 1/2         | Ethernet, Wi-Fi      |

### 2.2 TCP vs OSI

| 特性     | OSI      | TCP/IP   |
| -------- | -------- | -------- |
| 层数     | 7        | 4        |
| 先有模型 | 是       | 否       |
| 实用性   | 理论参考 | 实际标准 |
| 严格分层 | 是       | 较灵活   |

## 3. TCP 协议深度

### 3.1 TCP 首部格式

```mermaid
flowchart TD
    TCP[TCP 报文段<br/>源端口16 / 目标端口16<br/>序列号32 / 确认号32<br/>HL Rsv Flags 窗口大小<br/>校验和16 / 紧急指针16]
```

**标志位**：

| 标志 | 含义             |
| ---- | ---------------- |
| URG  | 紧急指针有效     |
| ACK  | 确认号有效       |
| PSH  | 接收方应尽快交付 |
| RST  | 重置连接         |
| SYN  | 同步序列号       |
| FIN  | 释放连接         |

### 3.2 三次握手

```mermaid
flowchart TD
    T0["客户端                    服务器"]
    T1["SYN, seq=x"]
    T2["SYN+ACK, seq=y,"]
    T3["ack=x+1"]
    T4["ACK, seq=x+1,"]
    T5["ack=y+1"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
```

**为什么三次**：防止已失效的连接请求到达服务器。

### 3.3 四次挥手

```mermaid
sequenceDiagram
    participant C as 客户端
    participant S as 服务器
    C->>S: FIN, seq=u（客户端关闭发送）
    S-->>C: ACK, ack=u+1（服务器确认）
    Note over S: 服务器继续发送
    S-->>C: FIN, seq=w（服务器关闭发送）
    C->>S: ACK, ack=w+1（客户端确认）
    Note over C: TIME_WAIT 2MSL
```

**TIME_WAIT**：等待 2MSL（最大报文段生存时间），确保最后一个 ACK 到达。

### 3.4 滑动窗口

$$\text{发送窗口} = \min(\text{rwnd}, \text{cwnd})$$

- rwnd：接收方通告窗口
- cwnd：拥塞窗口

### 3.5 TCP 状态机

```
CLOSED → SYN_SENT → ESTABLISHED
                ↓
CLOSED → LISTEN → SYN_RCVD → ESTABLISHED

ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED
ESTABLISHED → CLOSE_WAIT → LAST_ACK → CLOSED
```

## 4. UDP 协议

### 4.1 UDP 首部

```mermaid
flowchart LR
    SP[源端口 16] --- DP[目标端口 16]
    L[长度 16] --- CK[校验和 16]
```

仅 8 字节首部，无连接、无确认、无重传。

### 4.2 TCP vs UDP

| 特性     | TCP       | UDP        |
| -------- | --------- | ---------- |
| 连接     | 面向连接  | 无连接     |
| 可靠性   | 可靠      | 不可靠     |
| 顺序     | 有序      | 无序       |
| 流控     | 有        | 无         |
| 拥塞控制 | 有        | 无         |
| 速度     | 较慢      | 快         |
| 首部     | 20~60字节 | 8字节      |
| 适用     | 文件传输  | 实时音视频 |

## 5. IP 协议

### 5.1 IPv4 首部

```mermaid
flowchart TD
    IP[IP 数据报头<br/>VER IHL TOS 总长度16<br/>标识16 Flags 片偏移13<br/>TTL8 协议8 校验和16<br/>源IP地址32<br/>目标IP地址32]
```

### 5.2 IPv6 改进

| 特性     | IPv4         | IPv6       |
| -------- | ------------ | ---------- |
| 地址长度 | 32位         | 128位      |
| 首部     | 可变         | 固定40字节 |
| 分片     | 路由器可分片 | 仅源端分片 |
| 安全     | 可选         | 内置IPsec  |
| 配置     | 手动/DHCP    | 自动配置   |

### 5.3 子网划分

$$\text{子网数} = 2^n$$

$$\text{每子网主机数} = 2^m - 2$$

其中 $n$ 为借用的位数，$m$ 为剩余主机位。

**示例**：192.168.1.0/24 划分为4个子网：

| 子网 | 网络地址         | 可用范围  | 广播地址 |
| ---- | ---------------- | --------- | -------- |
| 1    | 192.168.1.0/26   | .1~.62    | .63      |
| 2    | 192.168.1.64/26  | .65~.126  | .127     |
| 3    | 192.168.1.128/26 | .129~.190 | .191     |
| 4    | 192.168.1.192/26 | .193~.254 | .255     |

## 6. ARP 与 ICMP

### 6.1 ARP 协议

将 IP 地址解析为 MAC 地址：

```
主机A: 谁有 192.168.1.1？告诉 192.168.1.100（广播）
主机B: 192.168.1.1 的 MAC 是 aa:bb:cc:dd:ee:ff（单播）
```

**ARP 缓存**：

```bash
arp -a
ip neigh show
```

### 6.2 ICMP 协议

| 类型 | 代码 | 含义         |
| ---- | ---- | ------------ |
| 0    | 0    | Echo Reply   |
| 3    | 0~15 | 目标不可达   |
| 5    | 0~3  | 重定向       |
| 8    | 0    | Echo Request |
| 11   | 0~1  | 超时         |

**Ping 原理**：发送 ICMP Echo Request，等待 Echo Reply。

**Traceroute 原理**：发送 TTL 递增的 IP 包，通过 ICMP 超时消息确定路径。
## OSI 七层模型

**基本写法：OSI 模型层次**
```text
`7. 应用层 (Application) - HTTP/FTP/SMTP/DNS
6. 表示层 (Presentation) - SSL/TLS/JPEG/ASCII
5. 会话层 (Session) - NetBIOS/RPC
4. 传输层 (Transport) - TCP/UDP
3. 网络层 (Network) - IP/ICMP
2. 数据链路层 (Data Link) - Ethernet/ARP
1. 物理层 (Physical) - 电信号/光信号`
```
```text
# OSI 七层模型从上到下
7. 应用层 - 为应用程序提供网络服务
6. 表示层 - 数据格式转换和加密
5. 会话层 - 管理会话连接
4. 传输层 - 端到端通信
3. 网络层 - 路由和寻址
2. 数据链路层 - 相邻节点通信
1. 物理层 - 比特流传输
```

---

## TCP/IP 四层模型

**基本写法：TCP/IP 模型层次**
```text
`4. 应用层 (Application) - HTTP/FTP/SMTP/DNS/SSH
3. 传输层 (Transport) - TCP/UDP
2. 网络层 (Internet) - IP/ICMP/ARP
1. 网络接口层 (Link) - Ethernet/WiFi`
```
```text
# TCP/IP 四层模型
4. 应用层 - 合并了 OSI 的应用、表示、会话层
3. 传输层 - 对应 OSI 传输层
2. 网络层 - 对应 OSI 网络层
1. 网络接口层 - 合并了 OSI 的数据链路和物理层
```

---

## OSI 与 TCP/IP 对应关系

**基本写法：模型对应映射**
```text
`OSI 模型          TCP/IP 模型        协议示例
7. 应用层    -->   4. 应用层          HTTP, DNS
6. 表示层    -->   4. 应用层          SSL/TLS
5. 会话层    -->   4. 应用层          RPC
4. 传输层    -->   3. 传输层          TCP, UDP
3. 网络层    -->   2. 网络层          IP, ICMP
2. 数据链路层 -->  1. 网络接口层      Ethernet
1. 物理层    -->   1. 网络接口层      双绞线`
```
```text
# OSI 与 TCP/IP 模型对应关系
OSI 7层模型           TCP/IP 4层模型
应用层、表示层、会话层  -->  应用层
传输层              -->  传输层
网络层              -->  网络层
数据链路层、物理层      -->  网络接口层
```

---

## TCP 协议

**基本写法：TCP 三次握手**
```text
`客户端              服务端
  |                   |
  |--- SYN ------->   |  客户端发送 SYN, seq=x
  |                   |
  |<-- SYN-ACK ----   |  服务端回复 SYN+ACK, seq=y, ack=x+1
  |                   |
  |--- ACK ------->   |  客户端发送 ACK, ack=y+1
  |                   |
  |<== 数据传输 ==>|`
```
```text
# TCP 三次握手建立连接
1. 客户端发送 SYN (seq=x)
2. 服务端回复 SYN+ACK (seq=y, ack=x+1)
3. 客户端发送 ACK (ack=y+1)
连接建立完成
```

**基本写法：TCP 四次挥手**
```text
`客户端              服务端
  |                   |
  |--- FIN ------->   |  客户端发送 FIN
  |<-- ACK --------   |  服务端回复 ACK
  |                   |
  |<-- FIN --------   |  服务端发送 FIN
  |--- ACK ------->   |  客户端回复 ACK`
```
```text
# TCP 四次挥手断开连接
1. 客户端发送 FIN
2. 服务端回复 ACK
3. 服务端发送 FIN
4. 客户端回复 ACK
连接断开完成
```

**基本写法：TCP 状态**
```text
`LISTEN       - 服务端监听端口
SYN_SENT     - 客户端已发送 SYN
SYN_RECV     - 服务端已收到 SYN
ESTABLISHED  - 连接已建立
FIN_WAIT_1   - 主动关闭方等待 FIN
FIN_WAIT_2   - 主动关闭方等待对方 FIN
TIME_WAIT    - 等待足够时间确保对方收到 ACK
CLOSE_WAIT   - 被动关闭方等待关闭
LAST_ACK     - 被动关闭方发送 FIN 后等待 ACK
CLOSED       - 连接已关闭`
```
```text
# TCP 连接状态转换
LISTEN -> SYN_RECV -> ESTABLISHED -> FIN_WAIT_1 -> FIN_WAIT_2 -> TIME_WAIT -> CLOSED
```

---

## TCP 特性

**基本写法：TCP 可靠性机制**
```text
`- 序列号：保证数据有序到达
- 确认应答：确认收到的数据
- 超时重传：未收到确认则重传
- 流量控制：滑动窗口机制
- 拥塞控制：避免网络拥塞`
```
```text
# TCP 可靠性保障机制
1. 序列号和确认号 - 保证数据有序和完整
2. 超时重传 - 丢包时自动重传
3. 滑动窗口 - 流量控制
4. 拥塞控制 - 慢启动、拥塞避免
```

**基本写法：TCP 拥塞控制算法**
```text
`- 慢启动 (Slow Start) - 连接开始时缓慢增加窗口
- 拥塞避免 (Congestion Avoidance) - 线性增加窗口
- 快重传 (Fast Retransmit) - 收到 3 个重复 ACK 立即重传
- 快恢复 (Fast Recovery) - 快重传后不回到慢启动`
```
```text
# TCP 拥塞控制四个阶段
1. 慢启动 - 窗口指数增长
2. 拥塞避免 - 窗口线性增长
3. 快重传 - 检测丢包立即重传
4. 快恢复 - 拥塞后快速恢复
```

---

## UDP 协议

**基本写法：UDP 特性**
```text
`- 无连接：不需要建立连接
- 不可靠：不保证数据到达
- 无序：不保证数据顺序
- 快速：无握手和确认开销
- 轻量：头部仅 8 字节`
```
```text
# UDP 协议特点
- 无连接，直接发送数据
- 不保证可靠性，可能丢包
- 头部小（8 字节），开销低
- 适用于实时应用：视频、语音、游戏
```

**基本写法：UDP 应用场景**
```text
`- DNS 查询 - 一次请求一次响应
- DHCP - 动态主机配置
- SNMP - 网络管理
- 流媒体 - 视频音频传输
- 在线游戏 - 实时交互`
```
```text
# UDP 常见应用
- DNS (端口 53) - 域名解析
- DHCP (端口 67/68) - IP 分配
- TFTP (端口 69) - 简单文件传输
- NTP (端口 123) - 时间同步
- SNMP (端口 161) - 网络管理
```

---

## IP 协议

**基本写法：IPv4 地址结构**
`<网络号><主机号>`
```text
# IPv4 地址分类
A 类: 1.0.0.0 - 126.255.255.255   (默认掩码 /8)
B 类: 128.0.0.0 - 191.255.255.255 (默认掩码 /16)
C 类: 192.0.0.0 - 223.255.255.255 (默认掩码 /24)
D 类: 224.0.0.0 - 239.255.255.255 (组播)
E 类: 240.0.0.0 - 255.255.255.255 (保留)
```

**基本写法：私有 IP 地址范围**
```text
`10.0.0.0/8        - A 类私有
172.16.0.0/12     - B 类私有
192.168.0.0/16    - C 类私有`
```
```text
# RFC 1918 私有 IP 地址范围
A 类私有: 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
B 类私有: 172.16.0.0 - 172.31.255.255 (172.16.0.0/12)
C 类私有: 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)
```

**基本写法：CIDR 表示法**
`<IP>/<前缀长度>`
```text
# CIDR 无类域间路由
192.168.1.0/24  - 256 个地址 (254 可用)
10.0.0.0/16     - 65536 个地址
172.16.0.0/12   - 1048576 个地址
```

**基本写法：IPv6 地址**
`<8组十六进制>:<8组十六进制>`
```text
# IPv6 地址格式
2001:0db8:85a3:0000:0000:8a2e:0370:7334

# 简化形式（省略前导零和连续零组）
2001:db8:85a3::8a2e:370:7334

# 回环地址
::1

# 未指定地址
::
```

---

## ICMP 协议

**基本写法：ICMP 类型**
```text
`Type 0  - Echo Reply (ping 响应)
Type 3  - Destination Unreachable (目标不可达)
Type 8  - Echo Request (ping 请求)
Type 11 - Time Exceeded (超时)
Type 5  - Redirect (重定向)`
```
```text
# 常见 ICMP 类型
Type 0  - Echo Reply（ping 响应）
Type 3  - Destination Unreachable（目标不可达）
Type 8  - Echo Request（ping 请求）
Type 11 - Time Exceeded（TTL 超时，traceroute 使用）
```

**基本写法：ping 命令原理**
```bash
`# 发送 ICMP Echo Request
ping <目标>

# 接收 ICMP Echo Reply`
```
```bash
# ping 基于 ICMP 协议
ping -c 4 8.8.8.8
```

---

## ARP 协议

**基本写法：ARP 工作流程**
```text
`1. 主机 A 查询 IP 对应的 MAC
2. 发送 ARP 请求（广播）
3. 目标主机 B 回复 ARP 响应（单播）
4. 主机 A 缓存 ARP 条目`
```
```text
# ARP 地址解析过程
1. 主机 A 需要发送数据给 192.168.1.2
2. 查询 ARP 缓存，未找到
3. 发送 ARP 广播：谁的 IP 是 192.168.1.2？
4. 主机 B 回复：我的 IP 是 192.168.1.2，MAC 是 xx:xx:xx:xx:xx:xx
5. 主机 A 缓存 ARP 条目并发送数据
```

**基本写法：查看 ARP 表**
`arp -a`
```bash
# 查看 ARP 缓存表
arp -a
```

---

## 常见协议端口

**基本写法：常用 TCP 端口**
```text
`20/21  - FTP (文件传输)
22     - SSH (安全 Shell)
23     - Telnet (远程登录)
25     - SMTP (邮件发送)
53     - DNS (域名解析)
80     - HTTP (网页)
110    - POP3 (邮件接收)
143    - IMAP (邮件访问)
443    - HTTPS (安全网页)
3306   - MySQL
5432   - PostgreSQL
6379   - Redis
8080   - HTTP 备用`
```
```text
# 常用 TCP 服务端口
22   - SSH
80   - HTTP
443  - HTTPS
3306 - MySQL
5432 - PostgreSQL
6379 - Redis
```

**基本写法：常用 UDP 端口**
```text
`53     - DNS (域名解析)
67/68  - DHCP (动态主机配置)
69     - TFTP (简单文件传输)
123    - NTP (时间同步)
161    - SNMP (网络管理)`
```
```text
# 常用 UDP 服务端口
53   - DNS
67/68 - DHCP
123  - NTP
161  - SNMP
```

---

## 子网划分

**基本写法：子网掩码计算**
`<IP>/<前缀>`
```text
# 子网掩码示例
/24 = 255.255.255.0    - 256 个地址
/25 = 255.255.255.128  - 128 个地址
/26 = 255.255.255.192  - 64 个地址
/27 = 255.255.255.224  - 32 个地址
/28 = 255.255.255.240  - 16 个地址
/30 = 255.255.255.252  - 4 个地址
```

**基本写法：计算可用主机数**
`可用主机 = 2^(32-前缀) - 2`
```text
# 子网可用主机数计算
/24 网络：2^8 - 2 = 254 个可用主机
/25 网络：2^7 - 2 = 126 个可用主机
/26 网络：2^6 - 2 = 62 个可用主机
/30 网络：2^2 - 2 = 2 个可用主机（点对点链路）
```

**基本写法：子网划分示例**
```bash
`# 将 192.168.1.0/24 划分为 4 个子网
子网 1: 192.168.1.0/26     (0-63)
子网 2: 192.168.1.64/26    (64-127)
子网 3: 192.168.1.128/26   (128-191)
子网 4: 192.168.1.192/26   (192-255)`
```
```text
# 192.168.1.0/24 划分为 4 个 /26 子网
子网 1: 192.168.1.0/26    范围 0-63     可用 1-62
子网 2: 192.168.1.64/26   范围 64-127   可用 65-126
子网 3: 192.168.1.128/26  范围 128-191  可用 129-190
子网 4: 192.168.1.192/26  范围 192-255  可用 193-254
```

<!-- ============================================================ networking/005-SwitchingAndRouting ============================================================ -->

## 1. VLAN 技术

### 1.1 VLAN 原理

VLAN（Virtual LAN）将物理网络划分为多个逻辑广播域：

- 基于端口：将端口分配到 VLAN
- 基于 MAC：根据 MAC 地址分配
- 基于协议：根据协议类型分配

**802.1Q 标签**：

```mermaid
flowchart LR
    DM[目的MAC] --- SM[源MAC] --- TP[TPID 8100] --- TC[TCI VLAN ID]
```

4 字节标签：TPID(0x8100) + PCP(3bit) + DEI(1bit) + VID(12bit, 0~4095)

### 1.2 Trunk 链路

在交换机间传输多个 VLAN 的流量：

```bash
# Cisco 配置
interface GigabitEthernet0/1
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30

# Huawei 配置
interface GigabitEthernet0/0/1
  port link-type trunk
  port trunk allow-pass vlan 10 20 30
```

### 1.3 VLAN 间路由

| 方式     | 设备           | 优缺点   |
| -------- | -------------- | -------- |
| 单臂路由 | 路由器子接口   | 带宽瓶颈 |
| 三层交换 | 三层交换机     | 高性能   |
| SVI      | 交换机虚拟接口 | 最常用   |

## 2. 生成树协议（STP）

### 2.1 STP 原理

防止二层环路，通过阻塞冗余链路实现：

1. 选举根桥（Bridge ID 最小）
2. 每个非根桥选举根端口（到根桥路径开销最小）
3. 每个网段选举指定端口
4. 阻塞非根端口和非指定端口

**BPDU**：Bridge Protocol Data Unit，交换机间交换的信息。

### 2.2 STP 端口状态

| 状态       | 接收BPDU | 发送BPDU | 转发数据 | 学习MAC |
| ---------- | -------- | -------- | -------- | ------- |
| Blocking   | 是       | 否       | 否       | 否      |
| Listening  | 是       | 是       | 否       | 否      |
| Learning   | 是       | 是       | 否       | 是      |
| Forwarding | 是       | 是       | 是       | 是      |

收敛时间：Blocking → Listening(15s) → Learning(15s) → Forwarding = **50秒**

### 2.3 RSTP（802.1w）

快速生成树协议，改进收敛时间：

| 端口角色 | 说明                 |
| -------- | -------------------- |
| 根端口   | 到根桥最优路径       |
| 指定端口 | 网段上转发数据的端口 |
| 替代端口 | 根端口的备份         |
| 备份端口 | 指定端口的备份       |

收敛时间：**1~3秒**

### 2.4 MSTP（802.1s）

多生成树协议，支持多个 VLAN 映射到不同生成树实例：

```bash
stp region-configuration
  region-name RG1
  instance 1 vlan 10 20
  instance 2 vlan 30 40
  active region-configuration
```

## 3. 链路聚合

### 3.1 LACP（802.3ad）

链路聚合控制协议，动态协商聚合链路：

```bash
# Cisco
interface Port-channel1
  switchport mode trunk
interface range GigabitEthernet0/1-2
  channel-group 1 mode active

# Huawei
interface Eth-Trunk1
  port link-type trunk
interface GigabitEthernet0/0/1
  eth-trunk 1
interface GigabitEthernet0/0/2
  eth-trunk 1
```

### 3.2 负载均衡

| 方式        | 说明           |
| ----------- | -------------- |
| src-mac     | 源MAC哈希      |
| dst-mac     | 目的MAC哈希    |
| src-dst-mac | 源+目的MAC哈希 |
| src-ip      | 源IP哈希       |
| dst-ip      | 目的IP哈希     |
| src-dst-ip  | 源+目的IP哈希  |

## 4. 静态路由

### 4.1 配置

```bash
# Cisco
ip route 10.0.0.0 255.255.255.0 192.168.1.1
ip route 0.0.0.0 0.0.0.0 192.168.1.1    # 默认路由

# Huawei
ip route-static 10.0.0.0 255.255.255.0 192.168.1.1
ip route-static 0.0.0.0 0.0.0.0 192.168.1.1

# Linux
ip route add 10.0.0.0/24 via 192.168.1.1
ip route add default via 192.168.1.1
```

### 4.2 路由优先级

1. 最长前缀匹配
2. 管理距离（AD）最小
3. 度量值最小

| 路由来源 | Cisco AD | Huawei 优先级 |
| -------- | -------- | ------------- |
| 直连     | 0        | 0             |
| 静态     | 1        | 60            |
| OSPF     | 110      | 10            |
| RIP      | 120      | 100           |
| BGP      | 20/200   | 255           |

## 5. OSPF 路由协议

### 5.1 OSPF 基础

- 链路状态协议
- 使用 Dijkstra 最短路径算法
- 区域化设计
- 快速收敛

### 5.2 OSPF 区域

| 区域类型         | 说明                   |
| ---------------- | ---------------------- |
| 骨干区域(Area 0) | 必须存在，连接所有区域 |
| 普通区域         | 标准区域               |
| 末梢区域(Stub)   | 不接收外部路由         |
| NSSA             | 允许引入少量外部路由   |
| Totally Stub     | 仅接收默认路由         |

### 5.3 OSPF 配置

```bash
# Cisco
router ospf 1
  router-id 1.1.1.1
  network 10.0.0.0 0.0.0.255 area 0
  network 10.0.1.0 0.0.0.255 area 1

# Huawei
ospf 1 router-id 1.1.1.1
  area 0
    network 10.0.0.0 0.0.0.255
  area 1
    network 10.0.1.0 0.0.0.255
```

### 5.4 OSPF LSA 类型

| 类型 | 名称          | 产生者     | 传播范围 |
| ---- | ------------- | ---------- | -------- |
| 1    | Router LSA    | 每个路由器 | 区域内   |
| 2    | Network LSA   | DR         | 区域内   |
| 3    | Summary LSA   | ABR        | 区域间   |
| 4    | ASBR Summary  | ABR        | 区域间   |
| 5    | External LSA  | ASBR       | 全AS     |
| 7    | NSSA External | NSSA ASBR  | NSSA内   |

## 6. BGP 路由协议

### 6.1 BGP 基础

- 路径向量协议
- 自治系统间路由
- 基于策略的路由选择
- TCP 179 端口

### 6.2 BGP 选路属性

按优先级排序：

1. Weight（Cisco 私有）
2. Local Preference
3. 本地起源
4. AS Path 最短
5. Origin（IGP < EGP < Incomplete）
6. MED
7. eBGP > iBGP
8. IGP 度量最小
9. 最长连接时间
10. 最小 Router ID

### 6.3 BGP 配置

```bash
router bgp 65001
  bgp router-id 1.1.1.1
  neighbor 10.0.0.2 remote-as 65002
  neighbor 10.0.0.2 description ISP-A
  network 192.168.0.0 mask 255.255.0.0
  !
  address-family ipv4
    neighbor 10.0.0.2 activate
    neighbor 10.0.0.2 route-map SET-LOCAL-PREF in
  !
route-map SET-LOCAL-PREF permit 10
  set local-preference 200
```

## 7. 策略路由

### 7.1 PBR 配置

```bash
# 基于源IP的策略路由
access-list 10 permit 192.168.1.0 0.0.0.255
route-map PBR permit 10
  match ip address 10
  set ip next-hop 10.0.0.1

interface GigabitEthernet0/0
  ip policy route-map PBR
```

### 7.2 应用场景

- 多出口链路负载分担
- 特定流量走专线
- 流量清洗引流

<!-- ============================================================ networking/006-NetworkSecurityTech ============================================================ -->

## 1. 防火墙技术

### 1.1 防火墙类型

| 类型     | 工作层        | 检查内容     | 性能 |
| -------- | ------------- | ------------ | ---- |
| 包过滤   | 网络层        | IP/端口/协议 | 高   |
| 状态检测 | 网络层+传输层 | 连接状态     | 中   |
| 应用网关 | 应用层        | 应用协议     | 低   |
| 下一代   | 多层          | 深度包检测   | 中   |

### 1.2 安全域划分

```
Internet ←→ Untrust(外网)
               ↕
            DMZ(隔离区)：Web服务器、邮件服务器
               ↕
            Trust(内网)：办公网络
               ↕
            Management(管理区)：运维管理
```

### 1.3 防火墙配置

```bash
# Cisco ASA
access-list OUTSIDE_IN permit tcp any host 203.0.113.10 eq 80
access-list OUTSIDE_IN permit tcp any host 203.0.113.10 eq 443
access-list OUTSIDE_IN deny ip any any

access-group OUTSIDE_IN in interface outside

# NAT 配置
object network WEB_SERVER
  host 10.0.0.10
  nat (inside,outside) static 203.0.113.10
```

### 1.4 安全策略设计原则

- 默认拒绝，显式允许
- 最小权限
- 纵深防御
- 分区隔离

## 2. IDS/IPS

### 2.1 入侵检测系统

| 类型 | 部署方式 | 检测方法     |
| ---- | -------- | ------------ |
| NIDS | 旁路部署 | 网络流量分析 |
| HIDS | 主机部署 | 系统日志分析 |

### 2.2 检测方法

**特征检测**：

```bash
# Snort 规则
alert tcp $EXTERNAL_NET any -> $HTTP_SERVERS $HTTP_PORTS \
  (msg:"SQL Injection Attempt"; \
   content:"UNION SELECT"; nocase; \
   sid:1000001; rev:1;)
```

**异常检测**：建立正常行为基线，偏离基线触发告警。

### 2.3 IPS 部署

```
Internet → IPS(内联) → 内部网络
              │
              ↓ 阻断恶意流量
```

IPS 在检测到攻击时主动阻断，但误报可能影响正常业务。

## 3. VPN 技术

### 3.1 VPN 类型

| 类型       | 场景     | 协议          |
| ---------- | -------- | ------------- |
| 远程访问   | 单用户   | SSL VPN, L2TP |
| 站点到站点 | 网络互联 | IPsec         |
| MPLS VPN   | 运营商   | MPLS          |

### 3.2 IPsec VPN

**IKE 阶段1（ISAKMP SA）**：

```bash
# Cisco 配置
crypto isakmp policy 10
  encryption aes-256
  hash sha256
  authentication pre-share
  group 14
  lifetime 86400

crypto isakmp key SECRET address 203.0.113.2
```

**IKE 阶段2（IPsec SA）**：

```bash
crypto ipsec transform-set TS esp-aes-256 esp-sha256-hmac

crypto map VPN 10 ipsec-isakmp
  set peer 203.0.113.2
  set transform-set TS
  match address CRYPTO_ACL

interface GigabitEthernet0/0
  crypto map VPN
```

### 3.3 SSL VPN

```
浏览器 → HTTPS → VPN网关 → 内部网络
```

优势：无需客户端，浏览器直接访问。

## 4. NAT 技术

### 4.1 NAT 类型

| 类型     | 映射方式     | 适用场景   |
| -------- | ------------ | ---------- |
| 静态NAT  | 一对一       | 服务器发布 |
| 动态NAT  | 地址池       | 内网上网   |
| NAPT/PAT | 端口多路复用 | 最常用     |

### 4.2 NAT 配置

```bash
# Cisco PAT
access-list NAT_ACL permit 10.0.0.0 0.0.0.255 any
ip nat inside source list NAT_ACL interface GigabitEthernet0/0 overload

interface GigabitEthernet0/0
  ip nat outside
interface GigabitEthernet0/1
  ip nat inside

# 静态NAT（端口转发）
ip nat inside source static tcp 10.0.0.10 80 203.0.113.10 80
```

### 4.3 NAT 穿越问题

| 协议  | 问题                | 解决方案       |
| ----- | ------------------- | -------------- |
| FTP   | 数据连接IP被NAT修改 | ALG/被动模式   |
| SIP   | SDP中IP被NAT修改    | ALG/STUN       |
| IPSec | AH校验失败          | NAT-T(UDP封装) |

## 5. 访问控制

### 5.1 ACL 类型

| 类型    | 编号范围 | 特点                |
| ------- | -------- | ------------------- |
| 标准ACL | 1~99     | 仅源IP              |
| 扩展ACL | 100~199  | 源/目标IP/端口/协议 |
| 命名ACL | -        | 可编辑              |

### 5.2 ACL 配置

```bash
# 扩展ACL
ip access-list extended WEB_ACCESS
  permit tcp any host 10.0.0.10 eq 80
  permit tcp any host 10.0.0.10 eq 443
  deny ip any any log

interface GigabitEthernet0/0
  ip access-group WEB_ACCESS in
```

### 5.3 802.1X 认证

```
客户端(Supplicant) ←EAPOL→ 交换机(Authenticator) ←RADIUS→ 认证服务器
```

```bash
# 交换机配置
aaa new-model
aaa authentication dot1x default group radius
radius server ISE
  address ipv4 10.0.0.100
  key SECRET_KEY

interface GigabitEthernet0/1
  dot1x port-control auto
```

## 6. 网络安全加固

### 6.1 设备安全

```bash
# 关闭不必要服务
no ip http server
no ip http secure-server
no cdp run
no ip source-route

# SSH 访问
line vty 0 4
  transport input ssh
  login local

# 密码加密
service password-encryption
enable secret LEVEL15
```

### 6.2 控制面安全

```bash
# 路由协议认证
router ospf 1
  area 0 authentication message-digest
  interface GigabitEthernet0/0
    ip ospf message-digest-key 1 md5 KEY

# BGP 认证
router bgp 65001
  neighbor 10.0.0.2 password BGP_KEY
```

### 6.3 管理面安全

- 使用 SNMPv3 替代 v2c
- 启用 Syslog 审计
- NTP 认证
- 配置变更管理

<!-- ============================================================ networking/007-WirelessNetwork ============================================================ -->

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

<!-- ============================================================ networking/008-SDNNetworkAutomation ============================================================ -->

## 1. SDN 架构

### 1.1 三层架构

```
应用层：网络应用（负载均衡、防火墙）
    ↕ 北向API（REST）
控制层：SDN控制器
    ↕ 南向API（OpenFlow）
基础设施层：交换机/路由器
```

### 1.2 SDN 优势

- 集中控制：全局视图
- 可编程：灵活部署服务
- 开放接口：设备解耦
- 自动化：减少人工配置

## 2. OpenFlow 协议

### 2.1 流表结构

| 字段     | 说明                       |
| -------- | -------------------------- |
| 匹配字段 | 入端口、MAC、IP、TCP端口等 |
| 优先级   | 匹配规则优先级             |
| 计数器   | 匹配包数、字节数           |
| 动作     | 转发、修改、丢弃、发控制器 |

### 2.2 流表操作

```
数据包 → 匹配流表 → 执行动作
              ↓ 无匹配
         发送到控制器
```

## 3. NETCONF/YANG

### 3.1 NETCONF 协议

基于 XML 的网络配置协议：

```xml
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get-config>
    <source><running/></source>
    <filter type="subtree">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
  </get-config>
</rpc>
```

### 3.2 YANG 建模

```yang
module example-interface {
  namespace "urn:example:interface";
  prefix ex;

  container interfaces {
    list interface {
      key name;
      leaf name { type string; }
      leaf enabled { type boolean; default true; }
      leaf description { type string; }
    }
  }
}
```

## 4. 网络自动化

### 4.1 Ansible 网络模块

```yaml
- name: Configure switch
  cisco.ios.ios_config:
    lines:
      - interface GigabitEthernet0/1
      - description Web Server
      - switchport mode access
      - switchport access vlan 10
```

### 4.2 Python 网络编程

```python
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

with ConnectHandler(**device) as conn:
    output = conn.send_command('show ip interface brief')
    print(output)

    config = [
        'interface Gi0/1',
        'description Configured by Python',
        'no shutdown'
    ]
    conn.send_config_set(config)
```

### 4.3 Nornir 并行框架

```python
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="nornir.yaml")
result = nr.run(task=netmiko_send_command, command_string="show version")
print_result(result)
```

<!-- ============================================================ networking/009-NetworkStorageTechnology ============================================================ -->

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

<!-- ============================================================ networking/010-NetworkDiagnosis ============================================================ -->

## 1. 故障诊断方法论

### 1.1 分层排查

从底层到高层逐层排查：

```
物理层 → 数据链路层 → 网络层 → 传输层 → 应用层
```

### 1.2 分段排查

通过分段隔离定位故障：

```
客户端 → 接入交换机 → 汇聚交换机 → 核心交换机 → 防火墙 → 服务器
```

### 1.3 对比法

与正常配置/状态对比找出差异。

## 2. 物理层故障

### 2.1 常见问题

| 问题       | 现象       | 排查         |
| ---------- | ---------- | ------------ |
| 网线断     | 接口down   | 换线测试     |
| 光纤衰减   | 丢包       | 光功率计     |
| 接口协商   | 速度不匹配 | 查看接口状态 |
| 双工不匹配 | 性能差     | 强制双工模式 |

```bash
# 查看接口状态
show interface GigabitEthernet0/1
show interface status

# 常见状态
GigabitEthernet0/1 is up, line protocol is up      # 正常
GigabitEthernet0/1 is down, line protocol is down   # 物理故障
GigabitEthernet0/1 is up, line protocol is down     # 数据链路问题
```

## 3. 数据链路层故障

### 3.1 MAC 地址表问题

```bash
show mac address-table
show mac address-table dynamic address xxxx.xxxx.xxxx
```

### 3.2 VLAN 故障

| 问题       | 原因         | 解决             |
| ---------- | ------------ | ---------------- |
| 跨VLAN不通 | 缺少路由     | 检查SVI/路由     |
| 同VLAN不通 | Trunk问题    | 检查允许的VLAN   |
| 端口不通   | VLAN配置错误 | 检查access/trunk |

### 3.3 STP 问题

```bash
show spanning-tree
show spanning-tree vlan 10

# 常见问题
# 根桥被抢占 → 配置根桥优先级
# 端口被阻塞 → 检查STP拓扑
# 环路 → 检查STP是否正常
```

## 4. 网络层故障

### 4.1 路由问题

```bash
# 查看路由表
show ip route
show ip route ospf

# 路由追踪
traceroute 10.0.0.1

# 常见问题
# 路由缺失 → 检查路由协议
# 路由环路 → 检查路由汇总
# 非对称路由 → 检查往返路径
```

### 4.2 ARP 问题

```bash
show ip arp
show ip arp 10.0.0.1

# ARP 冲突
# 同一IP对应多个MAC → 检查IP冲突
```

### 4.3 ACL 阻断

```bash
show access-lists
show ip interface GigabitEthernet0/1

# 查看ACL命中计数
show access-lists OUTSIDE_IN
```

## 5. 传输层故障

### 5.1 TCP 连接问题

```bash
# 查看连接状态
show tcp brief
ss -tnp

# 常见问题
# SYN无响应 → 防火墙/ACL阻断
# 大量TIME_WAIT → 调整tcp_tw_reuse
# 连接被拒绝 → 服务未启动
```

### 5.2 NAT 问题

```bash
show ip nat translations
show ip nat statistics

# 常见问题
# NAT转换失败 → 检查ACL和接口
# 端口耗尽 → 增加NAT池
```

## 6. 常用诊断工具

### 6.1 Ping 测试

```bash
ping 10.0.0.1              # 基本连通
ping 10.0.0.1 size 1500    # 大包测试
ping 10.0.0.1 repeat 100   # 大量测试
ping 10.0.0.1 df-bit       # 不分片测试MTU
```

### 6.2 抓包分析

```bash
# 交换机抓包
monitor capture point ip cpm CAPTURE both
monitor capture point associate CAPTURE BUFFER1
monitor capture buffer BUFFER1 size 10240
monitor capture point start CAPTURE
# ... 等待流量 ...
monitor capture point stop CAPTURE
show monitor capture buffer BUFFER1
```

### 6.3 流量镜像

```bash
# 本地镜像
monitor session 1 source interface Gi0/1 both
monitor session 1 destination interface Gi0/2

# ERSPAN（远程镜像）
monitor session 1 type erspan-source
  source interface Gi0/1 rx
  destination
    erspan-id 1
    ip address 10.0.0.100
    origin ip address 10.0.0.1
```

## 7. 典型故障案例

### 7.1 MTU 问题

```
现象：小包通，大包不通
原因：路径上MTU不一致，且ICMP被过滤
排查：ping -s 1472 -M do target（1472+28=1500）
解决：调整MTU或允许ICMP碎片需要
```

### 7.2 路由环路

```
现象：traceroute显示TTL递减后超时
原因：路由汇总导致环路
排查：show ip route，检查路由指向
解决：修正路由汇总或添加黑洞路由
```

### 7.3 间歇性丢包

```
现象：偶尔超时，大部分正常
原因：链路质量差/接口错误
排查：show interface（查看CRC/输入错误）
解决：更换线缆/调整协商
```

<!-- ============================================================ networking/011-NetworkDesignPlanning ============================================================ -->

## 1. 层次化网络设计

### 1.1 三层架构

```
核心层：高速交换，不做策略
  ↕
汇聚层：策略执行，路由边界
  ↕
接入层：终端接入，VLAN划分
```

### 1.2 各层设计要点

| 层级   | 关键指标   | 设计原则       |
| ------ | ---------- | -------------- |
| 核心层 | 带宽、延迟 | 冗余、无策略   |
| 汇聚层 | 策略、路由 | 模块化、边界   |
| 接入层 | 密度、安全 | 端口安全、VLAN |

### 1.3 Collapsed Core

中小企业将核心层和汇聚层合并：

```
核心/汇聚层（二层合一）
  ↕
接入层
```

## 2. 数据中心网络

### 2.1 Spine-Leaf 架构

```mermaid
flowchart TD
    S1[Spine1] S2[Spine2] S3[Spine3]
    L1[Leaf1] L2[Leaf2] L3[Leaf3] L4[Leaf4]
    SRV[服务器 服务器 服务器 服务器]
    S1 --- L1
    S1 --- L2
    S1 --- L3
    S1 --- L4
    S2 --- L1
    S2 --- L2
    S2 --- L3
    S2 --- L4
    S3 --- L1
    S3 --- L2
    S3 --- L3
    S3 --- L4
    L1 --> SRV
    L2 --> SRV
    L3 --> SRV
    L4 --> SRV
```

**优势**：

- 任意两台服务器间跳数恒定（2跳）
- 水平扩展：增加 Spine 或 Leaf
- 无阻塞带宽：每台 Leaf 与所有 Spine 互联

**东西向流量**优化：服务器间通信无需经过核心。

### 2.2 超融合网络

| 流量类型 | 协议             | 要求     |
| -------- | ---------------- | -------- |
| 数据     | TCP/IP           | 高带宽   |
| 存储     | FC/iSCSI/NVMe-oF | 低延迟   |
| 管理     | SSH/SNMP         | 可靠     |
| 虚拟化   | VXLAN/Geneve     | 覆盖网络 |

### 2.3 网络虚拟化

**VXLAN**：

```
原始帧 → VXLAN头(8B) → UDP头 → IP头 → 外层帧
         VNI(24bit) = 1600万虚拟网络
```

**NVGRE**：使用 GRE 隧道封装。

**Geneve**：VXLAN 和 NVGRE 的统一替代。

## 3. SD-WAN

### 3.1 SD-WAN 架构

```
分支站点 ←→ SD-WAN控制器 ←→ 总部/数据中心
     ↕           ↕
  多链路      集中策略
(MPLS/Internet/5G)
```

### 3.2 SD-WAN 核心能力

| 能力       | 说明                 |
| ---------- | -------------------- |
| 多链路聚合 | 同时使用多条链路     |
| 智能选路   | 根据应用需求选择路径 |
| 应用识别   | DPI 识别应用类型     |
| 自动VPN    | 自动建立站点间隧道   |
| 集中管理   | 统一策略下发         |

### 3.3 流量调度策略

```
语音/视频 → 低延迟链路(MPLS)
关键业务 → 可靠链路(MPLS/专线)
普通上网 → Internet链路
备份流量 → 最便宜链路
```

## 4. 网络冗余设计

### 4.1 设备冗余

| 方案      | 说明         | 切换时间 |
| --------- | ------------ | -------- |
| VRRP/HSRP | 虚拟路由冗余 | 1~3秒    |
| GLBP      | 网关负载均衡 | 1~3秒    |
| 堆叠/IRF  | 设备虚拟化   | 毫秒级   |
| CSS/VSU   | 集群交换系统 | 毫秒级   |

### 4.2 链路冗余

```bash
# VRRP 配置
interface Vlan10
  ip address 10.0.0.2 255.255.255.0
  vrrp 10 ip 10.0.0.1
  vrrp 10 priority 120
  vrrp 10 preempt
  vrrp 10 track GigabitEthernet0/0 decrement 30
```

### 4.3 路径冗余

- 等价多路径（ECMP）
- 浮动静态路由
- OSPF 多路径

## 5. 网络容量规划

### 5.1 带宽计算

$$\text{所需带宽} = \text{用户数} \times \text{并发率} \times \text{每用户带宽} \times \text{峰值系数}$$

### 5.2 设备选型

| 指标     | 接入层   | 汇聚层   | 核心层  |
| -------- | -------- | -------- | ------- |
| 背板带宽 | 100G+    | 500G+    | 1T+     |
| 包转发率 | 100Mpps+ | 500Mpps+ | 1Bpps+  |
| 端口密度 | 48×1G    | 24×10G   | 36×100G |

## 6. 网络安全设计

### 6.1 安全区域划分

```
Internet ← Untrust
    ↕
DMZ（Web/Mail）
    ↕
Trust（内网办公）
    ↕
Server Zone（服务器区）
    ↕
Management（管理区）
```

### 6.2 零信任网络设计

- 微分段：每个应用独立安全域
- 身份认证：每次访问都验证
- 最小权限：仅开放必要访问
- 持续监控：实时检测异常

<!-- ============================================================ networking/012-DNSDHCP ============================================================ -->

## 1. DNS 体系

### 1.1 域名层次

```mermaid
flowchart TD
    T0["根域(.)"]
    T1["顶级域(.com, .net, .org, .cn)"]
    T2["二级域(example.com)"]
    T3["子域(www.example.com)"]
    T0 --> T1
```

### 1.2 解析流程

```
客户端 → 本地DNS → 根DNS → 顶级域DNS → 权威DNS → 结果
```

递归查询 vs 迭代查询。

### 1.3 记录类型

| 类型  | 说明       | 示例                    |
| ----- | ---------- | ----------------------- |
| A     | IPv4地址   | 1.2.3.4                 |
| AAAA  | IPv6地址   | 2001:db8::1             |
| CNAME | 别名       | www → example.com       |
| MX    | 邮件交换   | 10 mail.example.com     |
| NS    | 名称服务器 | ns1.example.com         |
| TXT   | 文本记录   | SPF/DKIM                |
| SRV   | 服务定位   | \_sip.\_tcp.example.com |

### 1.4 DNSSEC

使用数字签名保护DNS响应：

- RRSIG：资源记录签名
- DNSKEY：公钥
- DS：委托签名者
- NSEC/NSEC3：不存在证明

## 2. DHCP

### 2.1 DORA 流程

```
客户端 → Discover(广播) → 服务器
客户端 ← Offer ← 服务器
客户端 → Request(广播) → 服务器
客户端 ← Ack ← 服务器
```

### 2.2 DHCP 中继

```bash
# 配置DHCP中继
interface Vlan10
  ip helper-address 10.0.0.100
```

### 2.3 IPAM

IP地址管理：统一管理IP分配、子网划分、DNS记录。

<!-- ============================================================ networking/013-LoadBalanceTech ============================================================ -->

## 1. 负载均衡概述

### 1.1 四层 vs 七层

| 维度     | L4       | L7                |
| -------- | -------- | ----------------- |
| 工作层   | 传输层   | 应用层            |
| 判断依据 | IP+端口  | URL/Header/Cookie |
| 性能     | 高       | 中                |
| 灵活性   | 低       | 高                |
| 代表     | LVS, NLB | Nginx, HAProxy    |

## 2. 负载均衡算法

| 算法       | 说明           | 适用       |
| ---------- | -------------- | ---------- |
| 轮询       | 依次分配       | 服务器同构 |
| 加权轮询   | 按权重分配     | 服务器异构 |
| 最少连接   | 选连接最少的   | 长连接     |
| 一致性哈希 | 按请求特征哈希 | 有状态     |
| 随机       | 随机选择       | 简单场景   |

## 3. 健康检查

| 类型   | 方法     | 粒度   |
| ------ | -------- | ------ |
| ICMP   | ping     | 基础   |
| TCP    | 端口连接 | 传输层 |
| HTTP   | GET/HEAD | 应用层 |
| 自定义 | 业务接口 | 精确   |

## 4. 会话保持

| 方式      | 说明            | 优缺点       |
| --------- | --------------- | ------------ |
| Source IP | 按源IP哈希      | 简单，不均匀 |
| Cookie    | 插入/改写Cookie | 精确，需支持 |
| Session   | 服务器间同步    | 复杂         |

## 5. 全局负载均衡（GSLB）

基于DNS的跨地域负载均衡：

```
用户 → DNS查询 → GSLB → 返回最近站点IP
```

策略：地理位置、网络延迟、站点可用性、负载。

<!-- ============================================================ networking/014-NetworkAutomation ============================================================ -->

## 1. NetDevOps 概述

### 1.1 核心理念

将 DevOps 实践应用于网络：

- 版本控制网络配置
- 自动化测试和部署
- 持续集成/持续交付
- 基础设施即代码

### 1.2 工具链

| 类别     | 工具                |
| -------- | ------------------- |
| 配置管理 | Ansible, Salt       |
| 模板引擎 | Jinja2              |
| 版本控制 | Git                 |
| CI/CD    | GitLab CI, Jenkins  |
| 验证     | Batfish, pyATS      |
| 监控     | Prometheus, Grafana |

## 2. 网络配置即代码

### 2.1 Git 工作流

```
main分支（生产配置）
  ↑ PR
develop分支（测试配置）
  ↑ PR
feature分支（变更配置）
```

### 2.2 Jinja2 模板

```jinja2
! 交换机配置模板
hostname {{ hostname }}
!
{% for vlan in vlans %}
vlan {{ vlan.id }}
  name {{ vlan.name }}
{% endfor %}
!
{% for iface in interfaces %}
interface {{ iface.name }}
  description {{ iface.description }}
  switchport mode {{ iface.mode }}
{% if iface.vlan %}
  switchport access vlan {{ iface.vlan }}
{% endif %}
{% endfor %}
```

### 2.3 Ansible 网络自动化

```yaml
- name: Configure access switches
  hosts: access_switches
  gather_facts: false
  tasks:
    - name: Apply VLAN config
      cisco.ios.ios_config:
        src: templates/vlan_config.j2
        backup: yes
      notify: save_config

  handlers:
    - name: save_config
      cisco.ios.ios_command:
        commands: write memory
```

## 3. 网络CI/CD

### 3.1 变更流水线

```
代码提交 → 语法检查 → 模拟验证 → 预发布部署 → 生产部署
```

### 3.2 Batfish 验证

```python
from pybatfish.client.commands import bf_session, bf_init_snapshot

bf_session.host = "batfish"
bf_init_snapshot("network_configs/")

# 验证路由
answer = bf.q.routes().answer()
# 验证ACL
answer = bf.q.filterLineReachability().answer()
# 验证端到端连通性
answer = bf_q.reachability(pathConstraints=PathConstraints(
    startLocation="host1", endLocation="host2")).answer()
```

## 4. 自动化运维

### 4.1 配置合规检查

```python
from pyats import aetest
from pyats.topology import loader

class ComplianceTest(aetest.Testcase):
    @aetest.test
    def check_dns(self, device):
        output = device.execute('show running-config | include name-server')
        assert '8.8.8.8' in output, 'DNS server not configured'

    @aetest.test
    def check_ntp(self, device):
        output = device.execute('show ntp associations')
        assert 'ntp.example.com' in output, 'NTP not configured'
```

### 4.2 自动修复

```yaml
- name: Auto-remediate BGP sessions
  hosts: routers
  tasks:
    - name: Check BGP status
      cisco.ios.ios_command:
        commands: show bgp summary
      register: bgp_status

    - name: Reset BGP if needed
      cisco.ios.ios_command:
        commands: clear bgp * soft
      when: "'Idle' in bgp_status.stdout[0]"
```

<!-- ============================================================ networking/015-LoadBalanceAlgorithm ============================================================ -->

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

<!-- ============================================================ networking/016-HighAvailabilityLVS ============================================================ -->

## 1. LVS 架构

### 1.1 IPVS 内核模块

IPVS 内核模块是高可用LVS的重要组成部分。本节详细介绍IPVS 内核模块的核心概念、工作原理和实际应用。

**关键要点**：

- IPVS 内核模块的定义与核心原理
- IPVS 内核模块的实现方式与技术细节
- IPVS 内核模块在实际场景中的应用与最佳实践
- IPVS 内核模块的常见问题与解决方案

IPVS 内核模块在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 调度器与真实服务器

调度器与真实服务器是高可用LVS的重要组成部分。本节详细介绍调度器与真实服务器的核心概念、工作原理和实际应用。

**关键要点**：

- 调度器与真实服务器的定义与核心原理
- 调度器与真实服务器的实现方式与技术细节
- 调度器与真实服务器在实际场景中的应用与最佳实践
- 调度器与真实服务器的常见问题与解决方案

调度器与真实服务器在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 三种模式

### 2.1 NAT 模式

NAT 模式是高可用LVS的重要组成部分。本节详细介绍NAT 模式的核心概念、工作原理和实际应用。

**关键要点**：

- NAT 模式的定义与核心原理
- NAT 模式的实现方式与技术细节
- NAT 模式在实际场景中的应用与最佳实践
- NAT 模式的常见问题与解决方案

NAT 模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 DR 模式

DR 模式是高可用LVS的重要组成部分。本节详细介绍DR 模式的核心概念、工作原理和实际应用。

**关键要点**：

- DR 模式的定义与核心原理
- DR 模式的实现方式与技术细节
- DR 模式在实际场景中的应用与最佳实践
- DR 模式的常见问题与解决方案

DR 模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 TUN 模式

TUN 模式是高可用LVS的重要组成部分。本节详细介绍TUN 模式的核心概念、工作原理和实际应用。

**关键要点**：

- TUN 模式的定义与核心原理
- TUN 模式的实现方式与技术细节
- TUN 模式在实际场景中的应用与最佳实践
- TUN 模式的常见问题与解决方案

TUN 模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 模式对比

### 3.1 性能

性能是高可用LVS的重要组成部分。本节详细介绍性能的核心概念、工作原理和实际应用。

**关键要点**：

- 性能的定义与核心原理
- 性能的实现方式与技术细节
- 性能在实际场景中的应用与最佳实践
- 性能的常见问题与解决方案

性能在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 网络要求

网络要求是高可用LVS的重要组成部分。本节详细介绍网络要求的核心概念、工作原理和实际应用。

**关键要点**：

- 网络要求的定义与核心原理
- 网络要求的实现方式与技术细节
- 网络要求在实际场景中的应用与最佳实践
- 网络要求的常见问题与解决方案

网络要求在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 适用场景

适用场景是高可用LVS的重要组成部分。本节详细介绍适用场景的核心概念、工作原理和实际应用。

**关键要点**：

- 适用场景的定义与核心原理
- 适用场景的实现方式与技术细节
- 适用场景在实际场景中的应用与最佳实践
- 适用场景的常见问题与解决方案

适用场景在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 高可用方案

### 4.1 Keepalived + LVS

Keepalived + LVS是高可用LVS的重要组成部分。本节详细介绍Keepalived + LVS的核心概念、工作原理和实际应用。

**关键要点**：

- Keepalived + LVS的定义与核心原理
- Keepalived + LVS的实现方式与技术细节
- Keepalived + LVS在实际场景中的应用与最佳实践
- Keepalived + LVS的常见问题与解决方案

Keepalived + LVS在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 健康检查

健康检查是高可用LVS的重要组成部分。本节详细介绍健康检查的核心概念、工作原理和实际应用。

**关键要点**：

- 健康检查的定义与核心原理
- 健康检查的实现方式与技术细节
- 健康检查在实际场景中的应用与最佳实践
- 健康检查的常见问题与解决方案

健康检查在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============================================================ networking/017-KeepalivedDualHotStandby ============================================================ -->

## 1. VRRP 协议

### 1.1 虚拟路由冗余

虚拟路由冗余是Keepalived双机热备的重要组成部分。本节详细介绍虚拟路由冗余的核心概念、工作原理和实际应用。

**关键要点**：

- 虚拟路由冗余的定义与核心原理
- 虚拟路由冗余的实现方式与技术细节
- 虚拟路由冗余在实际场景中的应用与最佳实践
- 虚拟路由冗余的常见问题与解决方案

虚拟路由冗余在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 优先级与抢占

优先级与抢占是Keepalived双机热备的重要组成部分。本节详细介绍优先级与抢占的核心概念、工作原理和实际应用。

**关键要点**：

- 优先级与抢占的定义与核心原理
- 优先级与抢占的实现方式与技术细节
- 优先级与抢占在实际场景中的应用与最佳实践
- 优先级与抢占的常见问题与解决方案

优先级与抢占在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Keepalived 配置

### 2.1 主备配置

主备配置是Keepalived双机热备的重要组成部分。本节详细介绍主备配置的核心概念、工作原理和实际应用。

**关键要点**：

- 主备配置的定义与核心原理
- 主备配置的实现方式与技术细节
- 主备配置在实际场景中的应用与最佳实践
- 主备配置的常见问题与解决方案

主备配置在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 健康检查脚本

健康检查脚本是Keepalived双机热备的重要组成部分。本节详细介绍健康检查脚本的核心概念、工作原理和实际应用。

**关键要点**：

- 健康检查脚本的定义与核心原理
- 健康检查脚本的实现方式与技术细节
- 健康检查脚本在实际场景中的应用与最佳实践
- 健康检查脚本的常见问题与解决方案

健康检查脚本在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 通知机制

通知机制是Keepalived双机热备的重要组成部分。本节详细介绍通知机制的核心概念、工作原理和实际应用。

**关键要点**：

- 通知机制的定义与核心原理
- 通知机制的实现方式与技术细节
- 通知机制在实际场景中的应用与最佳实践
- 通知机制的常见问题与解决方案

通知机制在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 脑裂防护

### 3.1 脑裂原因

脑裂原因是Keepalived双机热备的重要组成部分。本节详细介绍脑裂原因的核心概念、工作原理和实际应用。

**关键要点**：

- 脑裂原因的定义与核心原理
- 脑裂原因的实现方式与技术细节
- 脑裂原因在实际场景中的应用与最佳实践
- 脑裂原因的常见问题与解决方案

脑裂原因在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2仲裁机制

仲裁机制是Keepalived双机热备的重要组成部分。本节详细介绍仲裁机制的核心概念、工作原理和实际应用。

**关键要点**：

- 仲裁机制的定义与核心原理
- 仲裁机制的实现方式与技术细节
- 仲裁机制在实际场景中的应用与最佳实践
- 仲裁机制的常见问题与解决方案

仲裁机制在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 fencing

fencing是Keepalived双机热备的重要组成部分。本节详细介绍fencing的核心概念、工作原理和实际应用。

**关键要点**：

- fencing的定义与核心原理
- fencing的实现方式与技术细节
- fencing在实际场景中的应用与最佳实践
- fencing的常见问题与解决方案

fencing在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 实战

### 4.1 Nginx 高可用

Nginx 高可用是Keepalived双机热备的重要组成部分。本节详细介绍Nginx 高可用的核心概念、工作原理和实际应用。

**关键要点**：

- Nginx 高可用的定义与核心原理
- Nginx 高可用的实现方式与技术细节
- Nginx 高可用在实际场景中的应用与最佳实践
- Nginx 高可用的常见问题与解决方案

Nginx 高可用在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 双主模式

双主模式是Keepalived双机热备的重要组成部分。本节详细介绍双主模式的核心概念、工作原理和实际应用。

**关键要点**：

- 双主模式的定义与核心原理
- 双主模式的实现方式与技术细节
- 双主模式在实际场景中的应用与最佳实践
- 双主模式的常见问题与解决方案

双主模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============================================================ networking/018-NetworkNamespaceVirtualBridge ============================================================ -->

## 1. 网络命名空间

### 1.1 netns 原理

netns 原理是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍netns 原理的核心概念、工作原理和实际应用。

**关键要点**：

- netns 原理的定义与核心原理
- netns 原理的实现方式与技术细节
- netns 原理在实际场景中的应用与最佳实践
- netns 原理的常见问题与解决方案

netns 原理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 ip netns 命令

ip netns 命令是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍ip netns 命令的核心概念、工作原理和实际应用。

**关键要点**：

- ip netns 命令的定义与核心原理
- ip netns 命令的实现方式与技术细节
- ip netns 命令在实际场景中的应用与最佳实践
- ip netns 命令的常见问题与解决方案

ip netns 命令在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 veth pair

veth pair是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍veth pair的核心概念、工作原理和实际应用。

**关键要点**：

- veth pair的定义与核心原理
- veth pair的实现方式与技术细节
- veth pair在实际场景中的应用与最佳实践
- veth pair的常见问题与解决方案

veth pair在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 虚拟网桥

### 2.1 bridge 原理

bridge 原理是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍bridge 原理的核心概念、工作原理和实际应用。

**关键要点**：

- bridge 原理的定义与核心原理
- bridge 原理的实现方式与技术细节
- bridge 原理在实际场景中的应用与最佳实践
- bridge 原理的常见问题与解决方案

bridge 原理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 brctl/ip link 命令

brctl/ip link 命令是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍brctl/ip link 命令的核心概念、工作原理和实际应用。

**关键要点**：

- brctl/ip link 命令的定义与核心原理
- brctl/ip link 命令的实现方式与技术细节
- brctl/ip link 命令在实际场景中的应用与最佳实践
- brctl/ip link 命令的常见问题与解决方案

brctl/ip link 命令在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 STP 生成树

STP 生成树是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍STP 生成树的核心概念、工作原理和实际应用。

**关键要点**：

- STP 生成树的定义与核心原理
- STP 生成树的实现方式与技术细节
- STP 生成树在实际场景中的应用与最佳实践
- STP 生成树的常见问题与解决方案

STP 生成树在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 容器网络

### 3.1 Docker 网络模型

Docker 网络模型是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍Docker 网络模型的核心概念、工作原理和实际应用。

**关键要点**：

- Docker 网络模型的定义与核心原理
- Docker 网络模型的实现方式与技术细节
- Docker 网络模型在实际场景中的应用与最佳实践
- Docker 网络模型的常见问题与解决方案

Docker 网络模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 CNI 接口

CNI 接口是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍CNI 接口的核心概念、工作原理和实际应用。

**关键要点**：

- CNI 接口的定义与核心原理
- CNI 接口的实现方式与技术细节
- CNI 接口在实际场景中的应用与最佳实践
- CNI 接口的常见问题与解决方案

CNI 接口在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 实战

### 4.1 手动构建容器网络

手动构建容器网络是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍手动构建容器网络的核心概念、工作原理和实际应用。

**关键要点**：

- 手动构建容器网络的定义与核心原理
- 手动构建容器网络的实现方式与技术细节
- 手动构建容器网络在实际场景中的应用与最佳实践
- 手动构建容器网络的常见问题与解决方案

手动构建容器网络在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 跨主机通信

跨主机通信是网络命名空间与虚拟网桥的重要组成部分。本节详细介绍跨主机通信的核心概念、工作原理和实际应用。

**关键要点**：

- 跨主机通信的定义与核心原理
- 跨主机通信的实现方式与技术细节
- 跨主机通信在实际场景中的应用与最佳实践
- 跨主机通信的常见问题与解决方案

跨主机通信在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## 命名空间基础操作

**基本写法:创建命名空间**
`ip netns add <名称>`
```bash
# 创建名为 ns1 的网络命名空间
ip netns add ns1
ip netns add ns2
```

**基本写法:列出所有命名空间**
`ip netns list`
```bash
# 查看系统中所有网络命名空间
ip netns list
```

**基本写法:删除命名空间**
`ip netns del <名称>`
```bash
# 删除指定网络命名空间
ip netns del ns1
```

**基本写法:在命名空间中执行命令**
`ip netns exec <命名空间> <命令>`
```bash
# 在 ns1 中查看网络配置
ip netns exec ns1 ip addr
# 在 ns1 中查看路由
ip netns exec ns1 ip route
```

**基本写法:进入命名空间 shell**
`ip netns exec <命名空间> bash`
```bash
# 进入 ns1 的交互式 shell
ip netns exec ns1 bash
# 提示符会改变,exit 退出
```

---

## 命名空间接口配置

**基本写法:查看命名空间内接口**
`ip netns exec <命名空间> ip link`
```bash
# 查看 ns1 中的网络接口
ip netns exec ns1 ip link show
```

**基本写法:启动命名空间的环回接口**
`ip netns exec <命名空间> ip link set lo up`
```bash
# 启动 ns1 中的 lo 接口
ip netns exec ns1 ip link set lo up
```

**基本写法:将接口移入命名空间**
`ip link set <接口> netns <命名空间>`
```bash
# 将 eth1 接口移入 ns1
ip link set eth1 netns ns1
```

**基本写法:在命名空间中配置 IP**
`ip netns exec <命名空间> ip addr add <IP/前缀> dev <接口>`
```bash
# 在 ns1 中为 veth0 配置 IP
ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth0
ip netns exec ns1 ip link set veth0 up
```

**基本写法:查看命名空间路由**
`ip netns exec <命名空间> ip route`
```bash
# 查看 ns1 的路由表
ip netns exec ns1 ip route show
```

---

## veth pair 虚拟以太网对

**基本写法:创建 veth pair**
`ip link add <接口1> type veth peer name <接口2>`
```bash
# 创建一对 veth 虚拟网卡
ip link add veth0 type veth peer name veth1
```

**基本写法:将 veth 一端放入命名空间**
`ip link set <接口> netns <命名空间>`
```bash
# 将 veth0 放入 ns1,veth1 放入 ns2
ip link set veth0 netns ns1
ip link set veth1 netns ns2
```

**基本写法:命名空间间通信**
```bash
# 创建两个命名空间并通过 veth 互联
ip netns add ns1
ip netns add ns2
ip link add veth0 type veth peer name veth1
ip link set veth0 netns ns1
ip link set veth1 netns ns2
ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth0
ip netns exec ns2 ip addr add 10.0.0.2/24 dev veth1
ip netns exec ns1 ip link set veth0 up
ip netns exec ns2 ip link set veth1 up
ip netns exec ns1 ip link set lo up
ip netns exec ns2 ip link set lo up
```

**基本写法:测试命名空间互通**
`ip netns exec <命名空间> ping <目标>`
```bash
# 从 ns1 ping ns2
ip netns exec ns1 ping 10.0.0.2
```

**基本写法:删除 veth pair**
`ip netns exec <命名空间> ip link delete <接口>`
```bash
# 删除 veth(另一端会自动删除)
ip netns exec ns1 ip link delete veth0
```

---

## 命名空间与网桥

**基本写法:创建网桥并连接命名空间**
```bash
# 创建网桥并连接多个命名空间
ip link add br0 type bridge
ip link set br0 up

# 创建 ns1 和 ns2 并连接到 br0
ip netns add ns1
ip netns add ns2

ip link add veth0 type veth peer name veth1
ip link add veth2 type veth peer name veth3

ip link set veth0 netns ns1
ip link set veth2 netns ns2
ip link set veth1 master br0
ip link set veth3 master br0

ip netns exec ns1 ip addr add 10.0.0.1/24 dev veth0
ip netns exec ns2 ip addr add 10.0.0.2/24 dev veth2
ip netns exec ns1 ip link set veth0 up
ip netns exec ns2 ip link set veth2 up
```

**基本写法:为网桥配置 IP**
`ip addr add <IP/前缀> dev <网桥>`
```bash
# 主机通过 br0 与命名空间通信
ip addr add 10.0.0.254/24 dev br0
```

**基本写法:验证桥接连通性**
`ip netns exec <命名空间> ping <网桥IP>`
```bash
# 从 ns1 ping 网桥
ip netns exec ns1 ping 10.0.0.254
```

**基本写法:查看网桥 MAC 表**
`bridge fdb show`
```bash
# 查看网桥转发表
bridge fdb show dev br0
```

---

## 命名空间路由

**基本写法:添加命名空间默认路由**
`ip netns exec <命名空间> ip route add default via <网关>`
```bash
# 为 ns1 设置默认网关
ip netns exec ns1 ip route add default via 10.0.0.254
```

**基本写法:命名空间间路由**
`ip netns exec <命名空间> ip route add <网段> via <网关>`
```bash
# 添加到指定网段的路由
ip netns exec ns1 ip route add 192.168.2.0/24 via 10.0.0.254
```

**基本写法:主机开启转发让命名空间访问外网**
`sysctl -w net.ipv4.ip_forward=1`
```bash
# 主机开启 IP 转发
sysctl -w net.ipv4.ip_forward=1
# 配置 NAT
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j MASQUERADE
```

**基本写法:命名空间访问外网**
`ip netns exec <命名空间> ping 8.8.8.8`
```bash
# 测试命名空间访问外部网络
ip netns exec ns1 ping 8.8.8.8
```

**基本写法:配置命名空间 DNS**
`ip netns exec <命名空间> <命令>`
```bash
# 在命名空间中配置 DNS(通过 resolv.conf)
mkdir -p /etc/netns/ns1
echo "nameserver 8.8.8.8" > /etc/netns/ns1/resolv.conf
```

---

## 命名空间高级管理

**基本写法:为命名空间设置自定义 ID**
`ip netns add <名称>`
```bash
# 命名空间实际是 /var/run/netns 下的挂载点
ls /var/run/netns/
```

**基本写法:重命名命名空间**
`ip netns attach <新名称> <PID>`
```bash
# 通过 PID 附加到现有进程的网络命名空间
ip netns attach ns_new 12345
```

**基本写法:查看命名空间标识**
`ip netns identify <PID>`
```bash
# 查看进程所属的网络命名空间
ip netns identify $$
```

**基本写法:监控命名空间接口**
`ip netns exec <命名空间> ip monitor`
```bash
# 实时监控 ns1 中的网络事件
ip netns exec ns1 ip monitor link
```

**基本写法:批量查看所有命名空间**
```bash
# 遍历所有命名空间查看接口
for ns in $(ip netns list | awk '{print $1}'); do
    echo "=== $ns ==="
    ip netns exec $ns ip addr
done
```

---

## 命名空间与进程

**基本写法:在命名空间中运行进程**
`ip netns exec <命名空间> <进程>`
```bash
# 在 ns1 中运行 nginx
ip netns exec ns1 nginx -g "daemon off;"
```

**基本写法:将现有进程移入命名空间**
`nsenter -n -t <PID>`
```bash
# 进入指定进程的网络命名空间
nsenter -n -t 12345 ip addr
```

**基本写法:运行容器并指定命名空间**
`ip netns exec <命名空间> python3 -m http.server`
```bash
# 在指定命名空间中启动 HTTP 服务
ip netns exec ns1 python3 -m http.server 8080
```

**基本写法:查看进程的命名空间**
`ls -l /proc/<PID>/ns/net`
```bash
# 查看进程网络命名空间链接
ls -l /proc/$$/ns/net
readlink /proc/$$/ns/net
```

**基本写法:绑定命名空间到文件**
`mount --bind /proc/<PID>/ns/net /var/run/netns/<名称>`
```bash
# 持久化命名空间(避免进程退出后消失)
touch /var/run/netns/persistent_ns
mount --bind /proc/12345/ns/net /var/run/netns/persistent_ns
```

---

## 命名空间与容器网络

**基本写法:Docker 容器使用自定义命名空间**
`docker run --network container:<容器> <镜像>`
```bash
# 让新容器共享已有容器的网络命名空间
docker run --network container:web1 -it alpine sh
```

**基本写法:将容器接口移到命名空间**
```bash
# 容器网络是命名空间的典型应用
docker run -d --name test nginx
PID=$(docker inspect -f '{{.State.Pid}}' test)
ln -s /proc/$PID/ns/net /var/run/netns/docker_test
ip netns exec docker_test ip addr
```

**基本写法:命名空间中运行测试工具**
`ip netns exec <命名空间> tcpdump`
```bash
# 在命名空间中抓包
ip netns exec ns1 tcpdump -i veth0 -n
```

**基本写法:命名空间中端口监听**
`ip netns exec <命名空间> nc -l <端口>`
```bash
# 在 ns1 中监听 8080 端口
ip netns exec ns1 nc -l 8080
# 另一命名空间连接
ip netns exec ns2 nc 10.0.0.1 8080
```

---

## 命名空间故障排查

**基本写法:检查命名空间是否存在**
`ip netns list | grep <名称>`
```bash
# 检查 ns1 是否存在
ip netns list | grep ns1
```

**基本写法:命名空间内 ping 测试**
`ip netns exec <命名空间> ping <目标>`
```bash
# 在 ns1 中测试连通性
ip netns exec ns1 ping -c 4 10.0.0.2
ip netns exec ns1 ping -c 4 8.8.8.8
```

**基本写法:命名空间内抓包**
`ip netns exec <命名空间> tcpdump -i <接口>`
```bash
# 在 ns1 的 veth0 上抓包
ip netns exec ns1 tcpdump -i veth0 -nn
```

**基本写法:查看命名空间路由表**
`ip netns exec <命名空间> ip route show`
```bash
# 检查 ns1 的路由配置
ip netns exec ns1 ip route show
ip netns exec ns1 ip rule show
```

**基本写法:清理所有命名空间**
```bash
# 删除所有网络命名空间(谨慎操作)
for ns in $(ip netns list | awk '{print $1}'); do
    ip netns del $ns
done
```

**基本写法:清理残留 veth**
`ip link delete <接口>`
```bash
# 删除残留的 veth 接口
ip link delete veth0
ip link delete br0
```
## brctl 基础操作

**基本写法:创建网桥**
`brctl addbr <网桥名>`
```bash
# 创建名为 br0 的网桥
brctl addbr br0
```

**基本写法:删除网桥**
`brctl delbr <网桥名>`
```bash
# 删除 br0 网桥
ip link set br0 down
brctl delbr br0
```

**基本写法:查看所有网桥**
`brctl show`
```bash
# 查看系统中所有网桥及其接口
brctl show
```

**基本写法:查看指定网桥详细信息**
`brctl show <网桥名>`
```bash
# 查看 br0 网桥的接口列表
brctl show br0
```

**基本写法:查看网桥 MAC 表**
`brctl showmacs <网桥名>`
```bash
# 查看 br0 学习到的 MAC 地址表
brctl showmacs br0
```

---

## 网桥接口管理

**基本写法:添加接口到网桥**
`brctl addif <网桥> <接口>`
```bash
# 将 eth0 加入 br0
brctl addif br0 eth0
```

**基本写法:从网桥移除接口**
`brctl delif <网桥> <接口>`
```bash
# 从 br0 移除 eth0
brctl delif br0 eth0
```

**基本写法:启用网桥接口**
`ip link set <网桥> up`
```bash
# 启动 br0 接口
ip link set br0 up
```

**基本写法:为网桥配置 IP**
`ip addr add <IP/前缀> dev <网桥>`
```bash
# 为 br0 配置 IP 地址
ip addr add 192.168.1.1/24 dev br0
ip link set br0 up
```

**基本写法:完整网桥创建流程**
```bash
# 创建网桥并加入两个接口
brctl addbr br0
brctl addif br0 eth0
brctl addif br0 eth1
ip link set br0 up
ip link set eth0 up
ip link set eth1 up
ip addr add 192.168.1.1/24 dev br0
```

---

## 网桥 STP 配置

**基本写法:启用 STP 生成树协议**
`brctl stp <网桥> on`
```bash
# 启用 br0 的 STP 防止环路
brctl stp br0 on
```

**基本写法:禁用 STP**
`brctl stp <网桥> off`
```bash
# 禁用 br0 的 STP
brctl stp br0 off
```

**基本写法:查看 STP 状态**
`brctl showstp <网桥>`
```bash
# 查看 br0 的 STP 详细状态
brctl showstp br0
```

**基本写法:设置 STP 优先级**
`brctl setbridgeprio <网桥> <优先级>`
```bash
# 设置网桥优先级(用于根桥选举)
brctl setbridgeprio br0 4096
```

**基本写法:设置路径开销**
`brctl setpathcost <网桥> <接口> <开销>`
```bash
# 设置接口的路径开销
brctl setpathcost br0 eth0 100
```

---

## bridge 命令高级操作

**基本写法:使用 ip 命令创建网桥**
`ip link add <网桥> type bridge`
```bash
# 使用 iproute2 创建网桥(推荐)
ip link add name br0 type bridge
ip link set br0 up
```

**基本写法:使用 ip 命令删除网桥**
`ip link delete <网桥> type bridge`
```bash
# 删除网桥
ip link delete br0 type bridge
```

**基本写法:将接口加入网桥**
`ip link set <接口> master <网桥>`
```bash
# 将 eth0 加入 br0
ip link set eth0 master br0
```

**基本写法:将接口从网桥移除**
`ip link set <接口> nomaster`
```bash
# 从网桥移除 eth0
ip link set eth0 nomaster
```

**基本写法:查看网桥信息**
`ip link show type bridge`
```bash
# 查看所有 bridge 类型接口
ip link show type bridge
ip -d link show br0
```

---

## bridge fdb 转发表管理

**基本写法:查看转发数据库**
`bridge fdb show`
```bash
# 查看所有网桥的 MAC 转发表
bridge fdb show
```

**基本写法:查看指定网桥转发表**
`bridge fdb show dev <网桥>`
```bash
# 查看 br0 的转发表
bridge fdb show dev br0
```

**基本写法:添加静态 MAC 条目**
`bridge fdb add <MAC> dev <接口> [master]`
```bash
# 添加静态 MAC 地址到接口
bridge fdb add 00:11:22:33:44:55 dev eth0 master br0
```

**基本写法:删除 MAC 条目**
`bridge fdb del <MAC> dev <接口>`
```bash
# 删除转发表中的 MAC 条目
bridge fdb del 00:11:22:33:44:55 dev eth0
```

**基本写法:查看指定 MAC**
`bridge fdb get <MAC> dev <网桥>`
```bash
# 查询特定 MAC 地址在转发表中的信息
bridge fdb get 00:11:22:33:44:55 dev br0
```

---

## bridge vlan 管理

**基本写法:查看网桥 VLAN 信息**
`bridge vlan show`
```bash
# 查看所有接口的 VLAN 配置
bridge vlan show
```

**基本写法:为接口添加 VLAN**
`bridge vlan add dev <接口> vid <VLANID>`
```bash
# 为 eth0 添加 VLAN 100
bridge vlan add dev eth0 vid 100
```

**基本写法:删除接口 VLAN**
`bridge vlan del dev <接口> vid <VLANID>`
```bash
# 删除 eth0 的 VLAN 100
bridge vlan del eth0 vid 100
```

**基本写法:Trunk 模式配置**
`bridge vlan add dev <接口> vid <范围>`
```bash
# 配置 trunk 接口允许 VLAN 10-20
bridge vlan add dev eth0 vid 10-20
```

**基本写法:查看指定接口 VLAN**
`bridge vlan show dev <接口>`
```bash
# 查看 eth0 的 VLAN 信息
bridge vlan show dev eth0
```

---

## bridge link 链路管理

**基本写法:查看从接口状态**
`bridge link show`
```bash
# 查看所有网桥从接口状态
bridge link show
```

**基本写法:设置接口 STP 状态**
`bridge link set dev <接口> state <状态>`
```bash
# 设置接口 STP 状态
bridge link set dev eth0 state forwarding
bridge link set dev eth0 state blocking
```

**基本写法:设置接口优先级**
`bridge link set dev <接口> priority <优先级>`
```bash
# 设置 eth0 在 STP 中的优先级
bridge link set dev eth0 priority 128
```

**基本写法:设置接口 cost**
`bridge link set dev <接口> cost <开销>`
```bash
# 设置接口路径开销
bridge link set dev eth0 cost 200
```

**基本写法:启用 HW 学习模式**
`bridge link set dev <接口> hwmode vepa`
```bash
# 启用硬件学习模式
bridge link set dev eth0 hwmode vepa
bridge link set dev eth0 learning on
```

---

## 网桥与 VLAN 子接口

**基本写法:创建 VLAN 子接口**
`ip link add link <接口> name <子接口> type vlan id <VLANID>`
```bash
# 在 eth0 上创建 VLAN 100 子接口
ip link add link eth0 name eth0.100 type vlan id 100
ip link set eth0.100 up
```

**基本写法:VLAN 子接口加入网桥**
```bash
# 将不同 VLAN 子接口加入不同网桥
ip link add br100 type bridge
ip link add br200 type bridge
ip link add link eth0 name eth0.100 type vlan id 100
ip link add link eth0 name eth0.200 type vlan id 200
ip link set eth0.100 master br100
ip link set eth0.200 master br200
ip link set br100 up
ip link set br200 up
```

**基本写法:删除 VLAN 子接口**
`ip link delete <子接口>`
```bash
# 删除 VLAN 子接口
ip link delete eth0.100
```

**基本写法:VLAN 网桥配置 IP**
`ip addr add <IP/前缀> dev <网桥>`
```bash
# 为 VLAN 网桥配置网关 IP
ip addr add 192.168.100.1/24 dev br100
ip addr add 192.168.200.1/24 dev br200
```

---

## 网桥监控与调试

**基本写法:实时监控桥接事件**
`bridge monitor`
```bash
# 实时监控网桥状态变化
bridge monitor
```

**基本写法:查看桥接接口统计**
`ip -s link show <网桥>`
```bash
# 查看网桥收发包统计
ip -s link show br0
ip -s -s link show br0
```

**基本写法:抓包分析网桥流量**
`tcpdump -i <网桥> -n`
```bash
# 抓取网桥上的数据包
tcpdump -i br0 -n
tcpdump -i br0 -n -e
```

**基本写法:查看网桥学习到的 MAC**
`bridge fdb show dev <网桥>`
```bash
# 查看网桥转发表
bridge fdb show dev br0
```

**基本写法:监控接口链路状态**
`ip monitor link`
```bash
# 实时监控接口链路状态变化
ip monitor link
```

---

## 网桥持久化配置

**基本写法:RHEL/CentOS 配置文件**
`/etc/sysconfig/network-scripts/ifcfg-br0`
```bash
# /etc/sysconfig/network-scripts/ifcfg-br0
DEVICE=br0
TYPE=Bridge
BOOTPROTO=static
IPADDR=192.168.1.1
PREFIX=24
ONBOOT=yes
STP=yes

# /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
TYPE=Ethernet
BOOTPROTO=none
ONBOOT=yes
BRIDGE=br0
```

**基本写法:netplan 配置网桥**
```bash
# /etc/netplan/01-bridge.yaml
network:
  version: 2
  renderer: networkd
  bridges:
    br0:
      dhcp4: no
      addresses: [192.168.1.1/24]
      interfaces: [eth0, eth1]
      parameters:
        stp: true
        forward-delay: 4
```

**基本写法:Debian 传统配置**
`/etc/network/interfaces`
```bash
# /etc/network/interfaces
auto br0
iface br0 inet static
    address 192.168.1.1/24
    bridge_ports eth0 eth1
    bridge_stp on
    bridge_fd 4
```

**基本写法:应用配置**
`netplan apply`
```bash
# 应用 netplan 配置
netplan apply

# 重启网络服务
systemctl restart network
```

<!-- ============================================================ networking/019-Tunneling ============================================================ -->

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

<!-- ============================================================ networking/020-NetworkTroubleshootTools ============================================================ -->

## 1. 抓包分析

### 1.1 tcpdump 过滤表达式

tcpdump 过滤表达式是网络故障排查工具的重要组成部分。本节详细介绍tcpdump 过滤表达式的核心概念、工作原理和实际应用。

**关键要点**：

- tcpdump 过滤表达式的定义与核心原理
- tcpdump 过滤表达式的实现方式与技术细节
- tcpdump 过滤表达式在实际场景中的应用与最佳实践
- tcpdump 过滤表达式的常见问题与解决方案

tcpdump 过滤表达式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 常用抓包模式

常用抓包模式是网络故障排查工具的重要组成部分。本节详细介绍常用抓包模式的核心概念、工作原理和实际应用。

**关键要点**：

- 常用抓包模式的定义与核心原理
- 常用抓包模式的实现方式与技术细节
- 常用抓包模式在实际场景中的应用与最佳实践
- 常用抓包模式的常见问题与解决方案

常用抓包模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 连接状态

### 2.1 ss 命令

ss 命令是网络故障排查工具的重要组成部分。本节详细介绍ss 命令的核心概念、工作原理和实际应用。

**关键要点**：

- ss 命令的定义与核心原理
- ss 命令的实现方式与技术细节
- ss 命令在实际场景中的应用与最佳实践
- ss 命令的常见问题与解决方案

ss 命令在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 netstat 命令

netstat 命令是网络故障排查工具的重要组成部分。本节详细介绍netstat 命令的核心概念、工作原理和实际应用。

**关键要点**：

- netstat 命令的定义与核心原理
- netstat 命令的实现方式与技术细节
- netstat 命令在实际场景中的应用与最佳实践
- netstat 命令的常见问题与解决方案

netstat 命令在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 连接状态解读

连接状态解读是网络故障排查工具的重要组成部分。本节详细介绍连接状态解读的核心概念、工作原理和实际应用。

**关键要点**：

- 连接状态解读的定义与核心原理
- 连接状态解读的实现方式与技术细节
- 连接状态解读在实际场景中的应用与最佳实践
- 连接状态解读的常见问题与解决方案

连接状态解读在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 性能测试

### 3.1 iperf3 带宽测试

iperf3 带宽测试是网络故障排查工具的重要组成部分。本节详细介绍iperf3 带宽测试的核心概念、工作原理和实际应用。

**关键要点**：

- iperf3 带宽测试的定义与核心原理
- iperf3 带宽测试的实现方式与技术细节
- iperf3 带宽测试在实际场景中的应用与最佳实践
- iperf3 带宽测试的常见问题与解决方案

iperf3 带宽测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 ping/mtr 路由追踪

ping/mtr 路由追踪是网络故障排查工具的重要组成部分。本节详细介绍ping/mtr 路由追踪的核心概念、工作原理和实际应用。

**关键要点**：

- ping/mtr 路由追踪的定义与核心原理
- ping/mtr 路由追踪的实现方式与技术细节
- ping/mtr 路由追踪在实际场景中的应用与最佳实践
- ping/mtr 路由追踪的常见问题与解决方案

ping/mtr 路由追踪在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. DNS 排查

### 4.1 dig/nslookup

dig/nslookup是网络故障排查工具的重要组成部分。本节详细介绍dig/nslookup的核心概念、工作原理和实际应用。

**关键要点**：

- dig/nslookup的定义与核心原理
- dig/nslookup的实现方式与技术细节
- dig/nslookup在实际场景中的应用与最佳实践
- dig/nslookup的常见问题与解决方案

dig/nslookup在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 常见 DNS 问题

常见 DNS 问题是网络故障排查工具的重要组成部分。本节详细介绍常见 DNS 问题的核心概念、工作原理和实际应用。

**关键要点**：

- 常见 DNS 问题的定义与核心原理
- 常见 DNS 问题的实现方式与技术细节
- 常见 DNS 问题在实际场景中的应用与最佳实践
- 常见 DNS 问题的常见问题与解决方案

常见 DNS 问题在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============================================================ networking/021-BGP ============================================================ -->

## 1. 多线接入

### 1.1 单线/双线/BGP 多线

单线/双线/BGP 多线是BGP与多线机房互联的重要组成部分。本节详细介绍单线/双线/BGP 多线的核心概念、工作原理和实际应用。

**关键要点**：

- 单线/双线/BGP 多线的定义与核心原理
- 单线/双线/BGP 多线的实现方式与技术细节
- 单线/双线/BGP 多线在实际场景中的应用与最佳实践
- 单线/双线/BGP 多线的常见问题与解决方案

单线/双线/BGP 多线在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 BGP 多线优势

BGP 多线优势是BGP与多线机房互联的重要组成部分。本节详细介绍BGP 多线优势的核心概念、工作原理和实际应用。

**关键要点**：

- BGP 多线优势的定义与核心原理
- BGP 多线优势的实现方式与技术细节
- BGP 多线优势在实际场景中的应用与最佳实践
- BGP 多线优势的常见问题与解决方案

BGP 多线优势在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Anycast

### 2.1 Anycast 原理

Anycast 原理是BGP与多线机房互联的重要组成部分。本节详细介绍Anycast 原理的核心概念、工作原理和实际应用。

**关键要点**：

- Anycast 原理的定义与核心原理
- Anycast 原理的实现方式与技术细节
- Anycast 原理在实际场景中的应用与最佳实践
- Anycast 原理的常见问题与解决方案

Anycast 原理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 BGP Anycast 实现

BGP Anycast 实现是BGP与多线机房互联的重要组成部分。本节详细介绍BGP Anycast 实现的核心概念、工作原理和实际应用。

**关键要点**：

- BGP Anycast 实现的定义与核心原理
- BGP Anycast 实现的实现方式与技术细节
- BGP Anycast 实现在实际场景中的应用与最佳实践
- BGP Anycast 实现的常见问题与解决方案

BGP Anycast 实现在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 机房互联

### 3.1 专线互联

专线互联是BGP与多线机房互联的重要组成部分。本节详细介绍专线互联的核心概念、工作原理和实际应用。

**关键要点**：

- 专线互联的定义与核心原理
- 专线互联的实现方式与技术细节
- 专线互联在实际场景中的应用与最佳实践
- 专线互联的常见问题与解决方案

专线互联在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 VPN 互联

VPN 互联是BGP与多线机房互联的重要组成部分。本节详细介绍VPN 互联的核心概念、工作原理和实际应用。

**关键要点**：

- VPN 互联的定义与核心原理
- VPN 互联的实现方式与技术细节
- VPN 互联在实际场景中的应用与最佳实践
- VPN 互联的常见问题与解决方案

VPN 互联在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 SD-WAN

SD-WAN是BGP与多线机房互联的重要组成部分。本节详细介绍SD-WAN的核心概念、工作原理和实际应用。

**关键要点**：

- SD-WAN的定义与核心原理
- SD-WAN的实现方式与技术细节
- SD-WAN在实际场景中的应用与最佳实践
- SD-WAN的常见问题与解决方案

SD-WAN在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 流量工程

### 4.1 BGP 属性调优

BGP 属性调优是BGP与多线机房互联的重要组成部分。本节详细介绍BGP 属性调优的核心概念、工作原理和实际应用。

**关键要点**：

- BGP 属性调优的定义与核心原理
- BGP 属性调优的实现方式与技术细节
- BGP 属性调优在实际场景中的应用与最佳实践
- BGP 属性调优的常见问题与解决方案

BGP 属性调优在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 流量调度策略

流量调度策略是BGP与多线机房互联的重要组成部分。本节详细介绍流量调度策略的核心概念、工作原理和实际应用。

**关键要点**：

- 流量调度策略的定义与核心原理
- 流量调度策略的实现方式与技术细节
- 流量调度策略在实际场景中的应用与最佳实践
- 流量调度策略的常见问题与解决方案

流量调度策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============================================================ networking/022-SDN ============================================================ -->

## 1. SDN 架构

### 1.1 三层架构

三层架构是SDN的重要组成部分。本节详细介绍三层架构的核心概念、工作原理和实际应用。

**关键要点**：

- 三层架构的定义与核心原理
- 三层架构的实现方式与技术细节
- 三层架构在实际场景中的应用与最佳实践
- 三层架构的常见问题与解决方案

三层架构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 控制平面与数据平面分离

控制平面与数据平面分离是SDN的重要组成部分。本节详细介绍控制平面与数据平面分离的核心概念、工作原理和实际应用。

**关键要点**：

- 控制平面与数据平面分离的定义与核心原理
- 控制平面与数据平面分离的实现方式与技术细节
- 控制平面与数据平面分离在实际场景中的应用与最佳实践
- 控制平面与数据平面分离的常见问题与解决方案

控制平面与数据平面分离在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. OpenFlow

### 2.1 流表结构

流表结构是SDN的重要组成部分。本节详细介绍流表结构的核心概念、工作原理和实际应用。

**关键要点**：

- 流表结构的定义与核心原理
- 流表结构的实现方式与技术细节
- 流表结构在实际场景中的应用与最佳实践
- 流表结构的常见问题与解决方案

流表结构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 匹配与动作

匹配与动作是SDN的重要组成部分。本节详细介绍匹配与动作的核心概念、工作原理和实际应用。

**关键要点**：

- 匹配与动作的定义与核心原理
- 匹配与动作的实现方式与技术细节
- 匹配与动作在实际场景中的应用与最佳实践
- 匹配与动作的常见问题与解决方案

匹配与动作在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. SDN 控制器

### 3.1 ONOS

ONOS是SDN的重要组成部分。本节详细介绍ONOS的核心概念、工作原理和实际应用。

**关键要点**：

- ONOS的定义与核心原理
- ONOS的实现方式与技术细节
- ONOS在实际场景中的应用与最佳实践
- ONOS的常见问题与解决方案

ONOS在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 OpenDaylight

OpenDaylight是SDN的重要组成部分。本节详细介绍OpenDaylight的核心概念、工作原理和实际应用。

**关键要点**：

- OpenDaylight的定义与核心原理
- OpenDaylight的实现方式与技术细节
- OpenDaylight在实际场景中的应用与最佳实践
- OpenDaylight的常见问题与解决方案

OpenDaylight在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 Ryu

Ryu是SDN的重要组成部分。本节详细介绍Ryu的核心概念、工作原理和实际应用。

**关键要点**：

- Ryu的定义与核心原理
- Ryu的实现方式与技术细节
- Ryu在实际场景中的应用与最佳实践
- Ryu的常见问题与解决方案

Ryu在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 应用场景

### 4.1 数据中心网络

数据中心网络是SDN的重要组成部分。本节详细介绍数据中心网络的核心概念、工作原理和实际应用。

**关键要点**：

- 数据中心网络的定义与核心原理
- 数据中心网络的实现方式与技术细节
- 数据中心网络在实际场景中的应用与最佳实践
- 数据中心网络的常见问题与解决方案

数据中心网络在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 SD-WAN

SD-WAN是SDN的重要组成部分。本节详细介绍SD-WAN的核心概念、工作原理和实际应用。

**关键要点**：

- SD-WAN的定义与核心原理
- SD-WAN的实现方式与技术细节
- SD-WAN在实际场景中的应用与最佳实践
- SD-WAN的常见问题与解决方案

SD-WAN在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 网络虚拟化

网络虚拟化是SDN的重要组成部分。本节详细介绍网络虚拟化的核心概念、工作原理和实际应用。

**关键要点**：

- 网络虚拟化的定义与核心原理
- 网络虚拟化的实现方式与技术细节
- 网络虚拟化在实际场景中的应用与最佳实践
- 网络虚拟化的常见问题与解决方案

网络虚拟化在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============================================================ networking/023-IPCommands ============================================================ -->

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

<!-- ============================================================ networking/024-PingTraceroute ============================================================ -->

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

<!-- ============================================================ networking/025-SSNetstat ============================================================ -->

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

<!-- ============================================================ networking/026-Tcpdump ============================================================ -->

## tcpdump 基本用法

**基本写法：抓取所有流量**
`tcpdump`
```bash
# 抓取默认接口的所有流量
tcpdump
```

**基本写法：指定接口抓包**
`tcpdump -i <接口>`
```bash
# 抓取 eth0 接口的流量
tcpdump -i eth0
```

**基本写法：抓取所有接口**
`tcpdump -i any`
```bash
# 抓取所有接口的流量
tcpdump -i any
```

**基本写法：不解析主机名和端口名**
`tcpdump -n`
```bash
# 快速抓包不解析名称
tcpdump -n
```

**基本写法：详细输出**
`tcpdump -v`
```bash
# 显示详细信息
tcpdump -v
```

**基本写法：更详细的输出**
`tcpdump -vv`
```bash
# 显示更详细的信息
tcpdump -vv
```

**基本写法：显示数据链路层信息**
`tcpdump -e`
```bash
# 显示 MAC 地址信息
tcpdump -e
```

---

## 保存与读取抓包文件

**基本写法：保存到文件**
`tcpdump -w <文件>`
```bash
# 保存抓包结果到 capture.pcap
tcpdump -w capture.pcap
```

**基本写法：从文件读取**
`tcpdump -r <文件>`
```bash
# 读取并显示抓包文件
tcpdump -r capture.pcap
```

**基本写法：限制抓包大小**
`tcpdump -C <大小> -w <文件>`
```bash
# 每个文件最大 10MB
tcpdump -C 10 -w capture.pcap
```

**基本写法：限制抓包文件数量**
`tcpdump -W <数量> -C <大小> -w <文件>`
```bash
# 最多保留 5 个文件，每个 10MB
tcpdump -W 5 -C 10 -w capture.pcap
```

**基本写法：限制抓包数量**
`tcpdump -c <数量>`
```bash
# 抓取 100 个包后停止
tcpdump -c 100
```

---

## 主机过滤

**基本写法：按主机过滤**
`tcpdump host <IP>`
```bash
# 抓取指定主机的所有流量
tcpdump host 192.168.1.100
```

**基本写法：按源主机过滤**
`tcpdump src host <IP>`
```bash
# 抓取源 IP 为 192.168.1.100 的流量
tcpdump src host 192.168.1.100
```

**基本写法：按目标主机过滤**
`tcpdump dst host <IP>`
```bash
# 抓取目标 IP 为 192.168.1.100 的流量
tcpdump dst host 192.168.1.100
```

**基本写法：多主机过滤**
`tcpdump host <IP1> and host <IP2>`
```bash
# 抓取两台主机之间的流量
tcpdump host 192.168.1.1 and host 192.168.1.2
```

---

## 端口过滤

**基本写法：按端口过滤**
`tcpdump port <端口>`
```bash
# 抓取 80 端口的所有流量
tcpdump port 80
```

**基本写法：按源端口过滤**
`tcpdump src port <端口>`
```bash
# 抓取源端口为 8080 的流量
tcpdump src port 8080
```

**基本写法：按目标端口过滤**
`tcpdump dst port <端口>`
```bash
# 抓取目标端口为 443 的流量
tcpdump dst port 443
```

**基本写法：端口范围过滤**
`tcpdump portrange <起始>-<结束>`
```bash
# 抓取 8080-8090 端口范围的流量
tcpdump portrange 8080-8090
```

---

## 协议过滤

**基本写法：按协议过滤**
`tcpdump <协议>`
```bash
# 只抓取 TCP 流量
tcpdump tcp
```

**基本写法：抓取 UDP 流量**
`tcpdump udp`
```bash
# 只抓取 UDP 流量
tcpdump udp
```

**基本写法：抓取 ICMP 流量**
`tcpdump icmp`
```bash
# 抓取 ICMP 流量（如 ping）
tcpdump icmp
```

**基本写法：抓取 ARP 流量**
`tcpdump arp`
```bash
# 抓取 ARP 协议流量
tcpdump arp
```

**基本写法：抓取 IPv6 流量**
`tcpdump ip6`
```bash
# 抓取 IPv6 流量
tcpdump ip6
```

---

## 组合过滤

**基本写法：AND 组合**
`tcpdump <条件1> and <条件2>`
```bash
# 抓取主机 192.168.1.100 的 80 端口流量
tcpdump host 192.168.1.100 and port 80
```

**基本写法：OR 组合**
`tcpdump <条件1> or <条件2>`
```bash
# 抓取 80 或 443 端口流量
tcpdump port 80 or port 443
```

**基本写法：NOT 排除**
`tcpdump not <条件>`
```bash
# 排除 SSH 流量
tcpdump not port 22
```

**基本写法：复杂组合**
`tcpdump <条件1> and ( <条件2> or <条件3> )`
```bash
# 抓取主机 192.168.1.100 的 80 或 443 端口
tcpdump host 192.168.1.100 and \( port 80 or port 443 \)
```

---

## TCP 标志过滤

**基本写法：抓取 SYN 包**
`tcpdump 'tcp[tcpflags] & tcp-syn != 0'`
```bash
# 抓取 TCP SYN 包
tcpdump 'tcp[tcpflags] & tcp-syn != 0'
```

**基本写法：抓取 ACK 包**
`tcpdump 'tcp[tcpflags] & tcp-ack != 0'`
```bash
# 抓取 TCP ACK 包
tcpdump 'tcp[tcpflags] & tcp-ack != 0'
```

**基本写法：抓取 FIN 包**
`tcpdump 'tcp[tcpflags] & tcp-fin != 0'`
```bash
# 抓取 TCP FIN 包
tcpdump 'tcp[tcpflags] & tcp-fin != 0'
```

**基本写法：抓取 RST 包**
`tcpdump 'tcp[tcpflags] & tcp-rst != 0'`
```bash
# 抓取 TCP RST 包
tcpdump 'tcp[tcpflags] & tcp-rst != 0'
```

**基本写法：抓取 SYN 和 ACK**
`tcpdump 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0'`
```bash
# 抓取 SYN 或 ACK 包
tcpdump 'tcp[tcpflags] & (tcp-syn|tcp-ack) != 0'
```

---

## 数据包内容查看

**基本写法：以 ASCII 显示**
`tcpdump -A`
```bash
# 以 ASCII 显示数据包内容
tcpdump -A
```

**基本写法：以十六进制和 ASCII 显示**
`tcpdump -X`
```bash
# 以十六进制和 ASCII 显示数据包
tcpdump -X
```

**基本写法：完整十六进制输出**
`tcpdump -XX`
```bash
# 包含链路层头的十六进制输出
tcpdump -XX
```

**基本写法：指定抓取长度**
`tcpdump -s <长度>`
```bash
# 抓取每个包的前 256 字节
tcpdump -s 256
```

**基本写法：抓取完整数据包**
`tcpdump -s 0`
```bash
# 抓取完整数据包（默认 65535 字节）
tcpdump -s 0
```

---

## HTTP 抓包实战

**基本写法：抓取 HTTP 请求**
`tcpdump -A -s 0 'tcp port 80 and tcp[((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)):4] = 0x47455420'`
```bash
# 抓取 HTTP GET 请求
tcpdump -A -s 0 'tcp port 80 and tcp[((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)):4] = 0x47455420'
```

**基本写法：简单 HTTP 流量抓取**
`tcpdump -A -s 0 -i eth0 'tcp port 80'`
```bash
# 抓取 80 端口并显示内容
tcpdump -A -s 0 -i eth0 'tcp port 80'
```

**基本写法：抓取 HTTP POST 请求**
`tcpdump -A -s 0 'tcp port 80 and tcp[((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)):4] = 0x504f5354'`
```bash
# 抓取 HTTP POST 请求
tcpdump -A -s 0 'tcp port 80 and tcp[((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)):4] = 0x504f5354'
```

---

## DNS 抓包

**基本写法：抓取 DNS 查询**
`tcpdump -i eth0 'port 53'`
```bash
# 抓取所有 DNS 查询和响应
tcpdump -i eth0 'port 53'
```

**基本写法：详细显示 DNS 内容**
`tcpdump -vv -i eth0 'port 53'`
```bash
# 详细显示 DNS 查询内容
tcpdump -vv -i eth0 'port 53'
```

---

## 实用抓包组合

**基本写法：抓取指定主机的 HTTP 流量并保存**
`tcpdump -w <文件> host <IP> and port 80`
```bash
# 抓取指定主机的 HTTP 流量并保存
tcpdump -w http.pcap host 192.168.1.100 and port 80
```

**基本写法：排除 SSH 和 DNS 流量**
`tcpdump -n 'not port 22 and not port 53'`
```bash
# 抓取除 SSH 和 DNS 外的流量
tcpdump -n 'not port 22 and not port 53'
```

**基本写法：按时间限制抓包**
`timeout <秒数> tcpdump -w <文件>`
```bash
# 抓取 60 秒的流量
timeout 60 tcpdump -w capture.pcap
```

**基本写法：实时显示带时间戳**
`tcpdump -tttt`
```bash
# 显示带完整时间戳的数据包
tcpdump -tttt -i eth0
```

<!-- ============================================================ networking/027-DigNslookup ============================================================ -->

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

<!-- ============================================================ networking/028-CurlHTTPRequest ============================================================ -->

## curl 基本 GET 请求

**基本写法：发送 GET 请求**
`curl <URL>`
```bash
# 获取网页内容
curl https://example.com
```

**基本写法：显示响应头**
`curl -I <URL>`
```bash
# 只获取响应头
curl -I https://example.com
```

**基本写法：显示详细通信过程**
`curl -v <URL>`
```bash
# 显示请求和响应详细信息
curl -v https://example.com
```

**基本写法：跟随重定向**
`curl -L <URL>`
```bash
# 跟随 301/302 重定向
curl -L https://example.com
```

**基本写法：保存到文件**
`curl -o <文件> <URL>`
```bash
# 保存响应到文件
curl -o page.html https://example.com
```

**基本写法：使用原文件名保存**
`curl -O <URL>`
```bash
# 使用 URL 中的文件名保存
curl -O https://example.com/file.zip
```

---

## POST 请求

**基本写法：发送 POST 请求**
`curl -X POST <URL>`
```bash
# 发送 POST 请求
curl -X POST https://api.example.com/users
```

**基本写法：发送表单数据**
`curl -d "<数据>" <URL>`
```bash
# 发送表单数据
curl -d "name=John&age=30" https://api.example.com/users
```

**基本写法：发送 JSON 数据**
`curl -H "Content-Type: application/json" -d '<JSON>' <URL>`
```bash
# 发送 JSON 格式数据
curl -H "Content-Type: application/json" -d '{"name":"John","age":30}' https://api.example.com/users
```

**基本写法：从文件发送数据**
`curl -d @<文件> <URL>`
```bash
# 从文件读取数据发送
curl -d @data.json https://api.example.com/users
```

**基本写法：表单文件上传**
`curl -F "<字段>=@<文件>" <URL>`
```bash
# 上传文件
curl -F "file=@photo.jpg" https://api.example.com/upload
```

---

## HTTP 方法

**基本写法：PUT 请求**
`curl -X PUT -d '<数据>' <URL>`
```bash
# 更新资源
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Jane"}' https://api.example.com/users/1
```

**基本写法：DELETE 请求**
`curl -X DELETE <URL>`
```bash
# 删除资源
curl -X DELETE https://api.example.com/users/1
```

**基本写法：PATCH 请求**
`curl -X PATCH -d '<数据>' <URL>`
```bash
# 部分更新资源
curl -X PATCH -d '{"age":31}' https://api.example.com/users/1
```

**基本写法：HEAD 请求**
`curl -I <URL>`
```bash
# 只获取响应头
curl -I https://example.com
```

---

## 请求头设置

**基本写法：添加请求头**
`curl -H "<头部>: <值>" <URL>`
```bash
# 添加自定义请求头
curl -H "Authorization: Bearer token123" https://api.example.com/users
```

**基本写法：添加多个请求头**
`curl -H "<头部1>" -H "<头部2>" <URL>`
```bash
# 添加多个请求头
curl -H "Authorization: Bearer token" -H "Content-Type: application/json" https://api.example.com/users
```

**基本写法：设置 User-Agent**
`curl -A "<UA>" <URL>`
```bash
# 设置 User-Agent
curl -A "Mozilla/5.0" https://example.com
```

**基本写法：设置 Referer**
`curl -e "<URL>" <URL>`
```bash
# 设置 Referer
curl -e "https://google.com" https://example.com
```

---

## 认证

**基本写法：基本认证**
`curl -u <用户>:<密码> <URL>`
```bash
# HTTP 基本认证
curl -u admin:secret https://api.example.com/admin
```

**基本写法：Bearer Token 认证**
`curl -H "Authorization: Bearer <token>" <URL>`
```bash
# Bearer Token 认证
curl -H "Authorization: Bearer abc123" https://api.example.com/secure
```

**基本写法：客户端证书认证**
`curl --cert <证书> --key <私钥> <URL>`
```bash
# 使用客户端证书
curl --cert client.pem --key key.pem https://api.example.com
```

**基本写法：跳过证书验证**
`curl -k <URL>`
```bash
# 忽略 SSL 证书验证
curl -k https://self-signed.example.com
```

---

## Cookie 处理

**基本写法：发送 Cookie**
`curl -b "<cookie>" <URL>`
```bash
# 发送 Cookie
curl -b "session=abc123" https://example.com/dashboard
```

**基本写法：从文件加载 Cookie**
`curl -b <文件> <URL>`
```bash
# 从 cookie 文件加载
curl -b cookies.txt https://example.com
```

**基本写法：保存 Cookie 到文件**
`curl -c <文件> <URL>`
```bash
# 保存响应中的 Cookie
curl -c cookies.txt https://example.com/login
```

**基本写法：同时保存和使用 Cookie**
`curl -b <文件> -c <文件> <URL>`
```bash
# 加载并更新 Cookie
curl -b cookies.txt -c cookies.txt https://example.com
```

---

## 超时与重试

**基本写法：设置连接超时**
`curl --connect-timeout <秒数> <URL>`
```bash
# 设置 5 秒连接超时
curl --connect-timeout 5 https://example.com
```

**基本写法：设置总超时**
`curl --max-time <秒数> <URL>`
```bash
# 设置 10 秒总超时
curl --max-time 10 https://example.com
```

**基本写法：重试请求**
`curl --retry <次数> <URL>`
```bash
# 失败时重试 3 次
curl --retry 3 https://example.com
```

**基本写法：重试并延迟**
`curl --retry <次数> --retry-delay <秒数> <URL>`
```bash
# 重试 3 次，每次间隔 2 秒
curl --retry 3 --retry-delay 2 https://example.com
```

---

## 代理设置

**基本写法：使用 HTTP 代理**
`curl -x <代理地址> <URL>`
```bash
# 通过 HTTP 代理访问
curl -x http://proxy.example.com:8080 https://example.com
```

**基本写法：使用 SOCKS5 代理**
`curl --socks5 <代理地址> <URL>`
```bash
# 通过 SOCKS5 代理访问
curl --socks5 proxy.example.com:1080 https://example.com
```

**基本写法：代理认证**
`curl -x http://<用户>:<密码>@<代理> <URL>`
```bash
# 代理认证
curl -x http://user:pass@proxy.example.com:8080 https://example.com
```

**基本写法：忽略代理**
`curl --noproxy <域名> <URL>`
```bash
# 指定域名不使用代理
curl --noproxy example.com https://example.com
```

---

## 输出格式化

**基本写法：输出到标准错误**
`curl -o /dev/null -w "<格式>" <URL>`
```bash
# 只输出 HTTP 状态码
curl -o /dev/null -w "%{http_code}\n" https://example.com
```

**基本写法：输出详细信息**
`curl -w "<格式>" <URL>`
```bash
# 输出响应时间和状态码
curl -w "HTTP Code: %{http_code}\nTime: %{time_total}s\n" -o /dev/null https://example.com
```

**基本写法：JSON 美化输出**
`curl -s <URL> | python3 -m json.tool`
```bash
# 美化 JSON 输出
curl -s https://api.example.com/data | python3 -m json.tool
```

**基本写法：静默模式**
`curl -s <URL>`
```bash
# 静默模式不显示进度
curl -s https://example.com
```

---

## 下载控制

**基本写法：断点续传**
`curl -C - -o <文件> <URL>`
```bash
# 断点续传下载
curl -C - -o bigfile.zip https://example.com/bigfile.zip
```

**基本写法：限速下载**
`curl --limit-rate <速度> -o <文件> <URL>`
```bash
# 限制下载速度为 1MB/s
curl --limit-rate 1M -o file.zip https://example.com/file.zip
```

**基本写法：多部分下载**
`curl -r <范围> -o <文件> <URL>`
```bash
# 下载文件的 0-1024 字节
curl -r 0-1024 -o part.bin https://example.com/file.bin
```

---

## 实用组合

**基本写法：测试接口性能**
`curl -o /dev/null -s -w "时间: %{time_total}s\n大小: %{size_download}字节\n" <URL>`
```bash
# 测试接口响应时间和大小
curl -o /dev/null -s -w "时间: %{time_total}s\n大小: %{size_download}字节\n" https://api.example.com
```

**基本写法：下载并解压**
`curl -sL <URL> | tar xz`
```bash
# 下载并解压 tar.gz 文件
curl -sL https://example.com/archive.tar.gz | tar xz
```

**基本写法：检查证书过期时间**
`curl -vI <URL> 2>&1 | grep -i expire`
```bash
# 检查 HTTPS 证书过期时间
curl -vI https://example.com 2>&1 | grep -i expire_date
```

<!-- ============================================================ networking/029-IptablesFirewall ============================================================ -->

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

<!-- ============================================================ networking/030-SSHRemote ============================================================ -->

## ssh 基本连接

**基本写法：连接远程主机**
`ssh <用户>@<主机>`
```bash
# 以 root 用户连接到 192.168.1.1
ssh root@192.168.1.1
```

**基本写法：指定端口连接**
`ssh -p <端口> <用户>@<主机>`
```bash
# 连接到 2222 端口
ssh -p 2222 root@192.168.1.1
```

**基本写法：指定私钥文件**
`ssh -i <私钥> <用户>@<主机>`
```bash
# 使用指定私钥连接
ssh -i ~/.ssh/id_rsa user@192.168.1.1
```

**基本写法：执行远程命令**
`ssh <用户>@<主机> <命令>`
```bash
# 在远程主机执行命令
ssh root@192.168.1.1 "df -h"
```

**基本写法：分配伪终端**
`ssh -t <用户>@<主机> <命令>`
```bash
# 远程执行需要终端的命令
ssh -t root@192.168.1.1 "top"
```

---

## ssh 配置文件

**基本写法：配置主机别名**
```sshconfig
`Host <别名>
    HostName <主机>
    User <用户>
    Port <端口>
    IdentityFile <私钥>`
```
```sshconfig
# 配置 SSH 主机别名
Host prod
    HostName 192.168.1.100
    User deploy
    Port 22
    IdentityFile ~/.ssh/prod_key
```

**基本写法：使用别名连接**
`ssh <别名>`
```bash
# 使用配置的别名连接
ssh prod
```

**基本写法：禁用严格主机密钥检查**
`ssh -o StrictHostKeyChecking=no <用户>@<主机>`
```bash
# 跳过主机密钥确认
ssh -o StrictHostKeyChecking=no root@192.168.1.1
```

**基本写法：保持连接活跃**
`ssh -o ServerAliveInterval=<秒数> <用户>@<主机>`
```bash
# 每 60 秒发送心跳保持连接
ssh -o ServerAliveInterval=60 user@192.168.1.1
```

---

## ssh-agent 密钥代理

**基本写法：启动 ssh-agent**
`eval $(ssh-agent)`
```bash
# 启动 ssh-agent
eval $(ssh-agent)
```

**基本写法：添加私钥到 agent**
`ssh-add <私钥>`
```bash
# 添加私钥到 agent
ssh-add ~/.ssh/id_rsa
```

**基本写法：添加所有默认私钥**
`ssh-add`
```bash
# 添加默认私钥
ssh-add
```

**基本写法：列出已加载的密钥**
`ssh-add -l`
```bash
# 列出 agent 中的密钥指纹
ssh-add -l
```

**基本写法：删除密钥**
`ssh-add -d <私钥>`
```bash
# 从 agent 中删除密钥
ssh-add -d ~/.ssh/id_rsa
```

**基本写法：删除所有密钥**
`ssh-add -D`
```bash
# 清空 agent 中所有密钥
ssh-add -D
```

---

## ssh 端口转发

**基本写法：本地端口转发**
`ssh -L <本地端口>:<目标主机>:<目标端口> <用户>@<SSH主机>`
```bash
# 将本地 8080 转发到远程的 80
ssh -L 8080:localhost:80 user@192.168.1.1
```

**基本写法：远程端口转发**
`ssh -R <远程端口>:<目标主机>:<目标端口> <用户>@<SSH主机>`
```bash
# 将远程 8080 转发到本地 80
ssh -R 8080:localhost:80 user@192.168.1.1
```

**基本写法：动态端口转发（SOCKS 代理）**
`ssh -D <本地端口> <用户>@<SSH主机>`
```bash
# 创建 SOCKS5 代理
ssh -D 1080 user@192.168.1.1
```

**基本写法：后台端口转发**
`ssh -fNL <本地端口>:<目标>:<端口> <用户>@<主机>`
```bash
# 后台运行本地端口转发
ssh -fNL 8080:localhost:80 user@192.168.1.1
```

**基本写法：指定绑定地址**
`ssh -L <地址>:<本地端口>:<目标>:<端口> <用户>@<主机>`
```bash
# 绑定到所有地址
ssh -L 0.0.0.0:8080:localhost:80 user@192.168.1.1
```

---

## scp 远程拷贝

**基本写法：上传文件到远程**
`scp <本地文件> <用户>@<主机>:<远程路径>`
```bash
# 上传文件到远程主机
scp file.txt root@192.168.1.1:/tmp/
```

**基本写法：从远程下载文件**
`scp <用户>@<主机>:<远程文件> <本地路径>`
```bash
# 从远程主机下载文件
scp root@192.168.1.1:/var/log/syslog ./
```

**基本写法：递归拷贝目录**
`scp -r <目录> <用户>@<主机>:<路径>`
```bash
# 上传整个目录
scp -r ./project root@192.168.1.1:/opt/
```

**基本写法：指定端口**
`scp -P <端口> <文件> <用户>@<主机>:<路径>`
```bash
# 指定端口 2222
scp -P 2222 file.txt root@192.168.1.1:/tmp/
```

**基本写法：压缩传输**
`scp -C <文件> <用户>@<主机>:<路径>`
```bash
# 启用压缩传输
scp -C bigfile.tar root@192.168.1.1:/tmp/
```

**基本写法：限速传输**
`scp -l <速率> <文件> <用户>@<主机>:<路径>`
```bash
# 限制速率为 1000 Kbps
scp -l 1000 file.txt root@192.168.1.1:/tmp/
```

---

## sftp 安全文件传输

**基本写法：连接 SFTP**
`sftp <用户>@<主机>`
```bash
# 连接到 SFTP 服务器
sftp user@192.168.1.1
```

**基本写法：上传文件**
`sftp> put <本地文件> [远程路径]`
```bash
# 在 sftp 交互模式中上传
sftp> put file.txt /tmp/
```

**基本写法：下载文件**
`sftp> get <远程文件> [本地路径]`
```bash
# 在 sftp 交互模式中下载
sftp> get /var/log/syslog ./
```

**基本写法：递归上传目录**
`sftp> put -r <本地目录>`
```bash
# 递归上传整个目录
sftp> put -r ./project
```

**基本写法：递归下载目录**
`sftp> get -r <远程目录>`
```bash
# 递归下载整个目录
sftp> get -r /var/log
```

---

## ssh-keygen 密钥生成

**基本写法：生成 RSA 密钥**
`ssh-keygen -t rsa -b <位数>`
```bash
# 生成 4096 位 RSA 密钥
ssh-keygen -t rsa -b 4096
```

**基本写法：生成 Ed25519 密钥**
`ssh-keygen -t ed25519`
```bash
# 生成 Ed25519 密钥（推荐）
ssh-keygen -t ed25519 -C "user@example.com"
```

**基本写法：指定密钥文件名**
`ssh-keygen -f <文件名>`
```bash
# 指定密钥文件路径
ssh-keygen -f ~/.ssh/my_key
```

**基本写法：不设置密码**
`ssh-keygen -t rsa -N ""`
```bash
# 生成无密码的密钥
ssh-keygen -t rsa -N "" -f ~/.ssh/deploy_key
```

**基本写法：更改密钥密码**
`ssh-keygen -p -f <私钥>`
```bash
# 修改密钥的密码
ssh-keygen -p -f ~/.ssh/id_rsa
```

**基本写法：查看密钥指纹**
`ssh-keygen -l -f <公钥>`
```bash
# 查看公钥指纹
ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

---

## ssh-copy-id 部署公钥

**基本写法：复制公钥到远程**
`ssh-copy-id <用户>@<主机>`
```bash
# 将公钥部署到远程主机
ssh-copy-id user@192.168.1.1
```

**基本写法：指定公钥文件**
`ssh-copy-id -i <公钥> <用户>@<主机>`
```bash
# 指定公钥文件部署
ssh-copy-id -i ~/.ssh/my_key.pub user@192.168.1.1
```

**基本写法：指定端口**
`ssh-copy-id -p <端口> <用户>@<主机>`
```bash
# 指定端口部署公钥
ssh-copy-id -p 2222 user@192.168.1.1
```

---

## sshd 服务管理

**基本写法：重启 SSH 服务**
`systemctl restart sshd`
```bash
# 重启 SSH 服务
systemctl restart sshd
```

**基本写法：查看 SSH 服务状态**
`systemctl status sshd`
```bash
# 查看 SSH 服务运行状态
systemctl status sshd
```

**基本写法：测试 sshd 配置**
`sshd -t`
```bash
# 测试配置文件语法
sshd -t
```

**基本写法：禁止 root 登录**
`# 修改 /etc/ssh/sshd_config`
```bash
# 编辑 sshd_config 配置
sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart sshd
```

**基本写法：禁止密码登录**
`# 修改 /etc/ssh/sshd_config`
```bash
# 只允许密钥登录
sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd
```

<!-- ============================================================ networking/031-NetcatNmap ============================================================ -->

## nc 基本用法

**基本写法：连接 TCP 端口**
`nc <主机> <端口>`
```bash
# 连接到 example.com 的 80 端口
nc example.com 80
```

**基本写法：监听端口**
`nc -l <端口>`
```bash
# 监听 8080 端口
nc -l 8080
```

**基本写法：指定超时**
`nc -w <秒数> <主机> <端口>`
```bash
# 设置 5 秒超时
nc -w 5 example.com 80
```

**基本写法：UDP 连接**
`nc -u <主机> <端口>`
```bash
# UDP 模式连接
nc -u example.com 53
```

**基本写法：UDP 监听**
`nc -ul <端口>`
```bash
# 监听 UDP 端口
nc -ul 8080
```

---

## nc 端口扫描

**基本写法：扫描单个端口**
`nc -zv <主机> <端口>`
```bash
# 扫描 80 端口
nc -zv example.com 80
```

**基本写法：扫描端口范围**
`nc -zv <主机> <起始>-<结束>`
```bash
# 扫描 1-1000 端口范围
nc -zv example.com 1-1000
```

**基本写法：指定超时扫描**
`nc -zvw <秒数> <主机> <端口>`
```bash
# 设置 2 秒超时扫描
nc -zvw 2 example.com 1-1000
```

**基本写法：使用 IPv6**
`nc -6 -zv <主机> <端口>`
```bash
# 使用 IPv6 扫描
nc -6 -zv example.com 80
```

---

## nc 文件传输

**基本写法：接收文件**
`nc -l <端口> > <文件>`
```bash
# 监听 8080 端口接收文件
nc -l 8080 > received.txt
```

**基本写法：发送文件**
`nc <主机> <端口> < <文件>`
```bash
# 发送文件到远程主机
nc 192.168.1.100 8080 < file.txt
```

**基本写法：传输目录**
`tar czf - <目录> | nc <主机> <端口>`
```bash
# 压缩并传输目录
tar czf - /data | nc 192.168.1.100 8080
```

**基本写法：接收并解压**
`nc -l <端口> | tar xzf -`
```bash
# 接收并解压目录
nc -l 8080 | tar xzf - -C /backup
```

---

## nc 高级用法

**基本写法：保持监听**
`nc -lk <端口>`
```bash
# 持续监听 8080 端口
nc -lk 8080
```

**基本写法：HTTP 请求**
`echo -e "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | nc example.com 80`
```bash
# 通过 nc 发送 HTTP 请求
echo -e "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | nc example.com 80
```

**基本写法：聊天服务器**
`nc -l <端口>`
```bash
# 在主机 A 启动监听
nc -l 8080
# 在主机 B 连接
nc 192.168.1.1 8080
```

**基本写法：端口转发**
`nc -l <本地端口> -c 'nc <目标> <端口>'`
```bash
# 端口转发
nc -l 8080 -c 'nc example.com 80'
```

---

## nmap 基本扫描

**基本写法：扫描单个主机**
`nmap <主机>`
```bash
# 扫描 example.com 常用端口
nmap example.com
```

**基本写法：扫描 IP 范围**
`nmap <起始IP>-<结束IP>`
```bash
# 扫描 192.168.1.1 到 192.168.1.100
nmap 192.168.1.1-100
```

**基本写法：扫描网段**
`nmap <网段>/<前缀>`
```bash
# 扫描 192.168.1.0/24 网段
nmap 192.168.1.0/24
```

**基本写法：从文件读取目标**
`nmap -iL <文件>`
```bash
# 从文件读取目标列表扫描
nmap -iL targets.txt
```

**基本写法：排除指定主机**
`nmap <网段> --exclude <IP>`
```bash
# 排除指定主机扫描
nmap 192.168.1.0/24 --exclude 192.168.1.1
```

---

## nmap 端口扫描

**基本写法：扫描指定端口**
`nmap -p <端口> <主机>`
```bash
# 扫描 80 端口
nmap -p 80 example.com
```

**基本写法：扫描端口范围**
`nmap -p <起始>-<结束> <主机>`
```bash
# 扫描 1-1000 端口
nmap -p 1-1000 example.com
```

**基本写法：扫描所有端口**
`nmap -p- <主机>`
```bash
# 扫描所有 65535 个端口
nmap -p- example.com
```

**基本写法：扫描指定协议端口**
`nmap -p <协议>:<端口> <主机>`
```bash
# 扫描 UDP 53 端口
nmap -p U:53 example.com
```

**基本写法：快速扫描常用端口**
`nmap -F <主机>`
```bash
# 快速扫描 100 个常用端口
nmap -F example.com
```

---

## nmap 扫描类型

**基本写法：SYN 半开扫描**
`nmap -sS <主机>`
```bash
# SYN 半开扫描（需 root）
nmap -sS example.com
```

**基本写法：TCP 全连接扫描**
`nmap -sT <主机>`
```bash
# TCP 全连接扫描
nmap -sT example.com
```

**基本写法：UDP 扫描**
`nmap -sU <主机>`
```bash
# UDP 端口扫描
nmap -sU example.com
```

**基本写法：Ping 扫描**
`nmap -sn <网段>`
```bash
# 只发现存活主机
nmap -sn 192.168.1.0/24
```

**基本写法：无 Ping 扫描**
`nmap -Pn <主机>`
```bash
# 跳过主机发现直接扫描端口
nmap -Pn example.com
```

---

## nmap 服务与版本探测

**基本写法：服务版本探测**
`nmap -sV <主机>`
```bash
# 探测端口对应的服务版本
nmap -sV example.com
```

**基本写法：操作系统探测**
`nmap -O <主机>`
```bash
# 探测目标操作系统
nmap -O example.com
```

**基本写法：全面扫描**
`nmap -A <主机>`
```bash
# 启用所有高级探测功能
nmap -A example.com
```

**基本写法：指定版本探测强度**
`nmap -sV --version-intensity <级别> <主机>`
```bash
# 设置版本探测强度为 9
nmap -sV --version-intensity 9 example.com
```

---

## nmap 时间与性能

**基本写法：设置扫描时序**
`nmap -T<级别> <主机>`
```bash
# 使用激进时序模板（0-5）
nmap -T4 example.com
```

**基本写法：设置并发速率**
`nmap --max-rate <速率> <主机>`
```bash
# 限制最大每秒 100 个包
nmap --max-rate 100 example.com
```

**基本写法：设置并行数**
`nmap --min-parallelism <数量> <主机>`
```bash
# 设置最小并行探测数
nmap --min-parallelism 10 example.com
```

**基本写法：设置超时**
`nmap --host-timeout <时间> <主机>`
```bash
# 设置每主机超时 30 分钟
nmap --host-timeout 30m example.com
```

---

## nmap 脚本引擎

**基本写法：使用默认脚本**
`nmap -sC <主机>`
```bash
# 使用默认脚本集合扫描
nmap -sC example.com
```

**基本写法：指定脚本扫描**
`nmap --script <脚本> <主机>`
```bash
# 使用 vuln 脚本扫描漏洞
nmap --script vuln example.com
```

**基本写法：HTTP 标题枚举**
`nmap --script http-title -p <端口> <主机>`
```bash
# 获取 HTTP 服务标题
nmap --script http-title -p 80,443 example.com
```

**基本写法：SSL 证书枚举**
`nmap --script ssl-cert -p 443 <主机>`
```bash
# 获取 SSL 证书信息
nmap --script ssl-cert -p 443 example.com
```

**基本写法：列举脚本**
`nmap --script-help <类别>`
```bash
# 列出所有 vuln 类别脚本
nmap --script-help vuln
```

---

## nmap 输出格式

**基本写法：输出到文件**
`nmap -oN <文件> <主机>`
```bash
# 输出标准格式到文件
nmap -oN scan.txt example.com
```

**基本写法：输出 XML 格式**
`nmap -oX <文件> <主机>`
```bash
# 输出 XML 格式便于程序解析
nmap -oX scan.xml example.com
```

**基本写法：输出 Grep 格式**
`nmap -oG <文件> <主机>`
```bash
# 输出 grep 友好格式
nmap -oG scan.gnmap example.com
```

**基本写法：输出所有格式**
`nmap -oA <文件名> <主机>`
```bash
# 同时输出所有格式
nmap -oA scanresult example.com
```

---

## 实用扫描组合

**基本写法：快速存活主机发现**
`nmap -sn -T4 <网段>`
```bash
# 快速扫描网段存活主机
nmap -sn -T4 192.168.1.0/24
```

**基本写法：全面扫描单主机**
`nmap -sS -sV -O -A -T4 -p- <主机>`
```bash
# 全面扫描所有端口和服务
nmap -sS -sV -O -A -T4 -p- example.com
```

**基本写法：扫描并保存结果**
`nmap -sV -oA <文件名> -p- <主机>`
```bash
# 扫描所有端口并保存结果
nmap -sV -oA fullscan -p- 192.168.1.1
```

<!-- ============================================================ networking/032-ARPRouting ============================================================ -->

## arp 命令

**基本写法：查看 ARP 缓存**
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

**基本写法：数字格式查看**
`arp -an`
```bash
# 不解析主机名查看 ARP
arp -an
```

**基本写法：添加静态 ARP**
`arp -s <IP> <MAC>`
```bash
# 添加静态 ARP 绑定
arp -s 192.168.1.1 00:11:22:33:44:55
```

**基本写法：删除 ARP 条目**
`arp -d <IP>`
```bash
# 删除指定 IP 的 ARP 条目
arp -d 192.168.1.1
```

**基本写法：指定接口操作**
`arp -i <接口> -a`
```bash
# 查看 eth0 接口的 ARP
arp -i eth0 -a
```

---

## ip neigh 邻居管理

**基本写法：查看邻居表**
`ip neigh`
```bash
# 查看 ARP 邻居表
ip neigh
```

**基本写法：简写形式**
`ip n`
```bash
# 简写查看邻居表
ip n
```

**基本写法：查看指定接口邻居**
`ip neigh show dev <接口>`
```bash
# 查看 eth0 接口的邻居
ip neigh show dev eth0
```

**基本写法：添加邻居条目**
`ip neigh add <IP> lladdr <MAC> dev <接口>`
```bash
# 添加邻居条目
ip neigh add 192.168.1.100 lladdr 00:11:22:33:44:55 dev eth0
```

**基本写法：删除邻居条目**
`ip neigh del <IP> dev <接口>`
```bash
# 删除邻居条目
ip neigh del 192.168.1.100 dev eth0
```

**基本写法：刷新邻居缓存**
`ip neigh flush dev <接口>`
```bash
# 刷新 eth0 接口的邻居缓存
ip neigh flush dev eth0
```

---

## route 路由管理

**基本写法：查看路由表**
`route -n`
```bash
# 数字格式查看路由表
route -n
```

**基本写法：添加默认网关**
`route add default gw <网关>`
```bash
# 添加默认网关
route add default gw 192.168.1.1
```

**基本写法：删除默认网关**
`route del default gw <网关>`
```bash
# 删除默认网关
route del default gw 192.168.1.1
```

**基本写法：添加主机路由**
`route add -host <IP> gw <网关>`
```bash
# 添加到指定主机的路由
route add -host 10.0.0.1 gw 192.168.1.254
```

**基本写法：添加网络路由**
`route add -net <网络>/<前缀> gw <网关>`
```bash
# 添加到指定网络的路由
route add -net 10.0.0.0/24 gw 192.168.1.254
```

**基本写法：拒绝路由**
`route add -net <网络> reject`
```bash
# 拒绝到指定网络的路由
route add -net 10.0.0.0/24 reject
```

---

## ip route 路由管理

**基本写法：查看路由表**
`ip route`
```bash
# 查看完整路由表
ip route
```

**基本写法：简写形式**
`ip r`
```bash
# 简写查看路由表
ip r
```

**基本写法：添加默认路由**
`ip route add default via <网关>`
```bash
# 添加默认路由
ip route add default via 192.168.1.1
```

**基本写法：添加静态路由**
`ip route add <网络>/<前缀> via <网关>`
```bash
# 添加到 10.0.0.0/24 的路由
ip route add 10.0.0.0/24 via 192.168.1.254
```

**基本写法：通过接口添加路由**
`ip route add <网络>/<前缀> dev <接口>`
```bash
# 通过 eth1 添加路由
ip route add 172.16.0.0/16 dev eth1
```

**基本写法：设置路由度量值**
`ip route add <网络>/<前缀> via <网关> metric <值>`
```bash
# 添加带度量值的路由
ip route add 10.0.0.0/24 via 192.168.1.254 metric 100
```

**基本写法：删除路由**
`ip route del <网络>/<前缀>`
```bash
# 删除指定路由
ip route del 10.0.0.0/24
```

**基本写法：修改路由**
`ip route change <网络>/<前缀> via <网关>`
```bash
# 修改现有路由
ip route change 10.0.0.0/24 via 192.168.1.253
```

**基本写法：替换路由**
`ip route replace <网络>/<前缀> via <网关>`
```bash
# 替换或添加路由
ip route replace 10.0.0.0/24 via 192.168.1.254
```

---

## 路由查询

**基本写法：查询到目标的路由**
`ip route get <目标IP>`
```bash
# 查询到 8.8.8.8 的路由
ip route get 8.8.8.8
```

**基本写法：从指定源查询路由**
`ip route get <目标IP> from <源IP>`
```bash
# 从指定源 IP 查询路由
ip route get 8.8.8.8 from 192.168.1.100
```

**基本写法：指定 TOS 查询路由**
`ip route get <目标IP> tos <TOS>`
```bash
# 指定 TOS 查询路由
ip route get 8.8.8.8 tos 0x10
```

---

## 策略路由

**基本写法：查看路由策略**
`ip rule`
```bash
# 查看策略路由规则
ip rule
```

**基本写法：基于源 IP 的策略路由**
`ip rule add from <源IP> table <表号>`
```bash
# 来自 192.168.1.100 的流量走表 100
ip rule add from 192.168.1.100 table 100
```

**基本写法：基于目标 IP 的策略路由**
`ip rule add to <目标IP> table <表号>`
```bash
# 到 10.0.0.1 的流量走表 200
ip rule add to 10.0.0.1 table 200
```

**基本写法：基于端口的策略路由**
`ip rule add sport <端口> table <表号>`
```bash
# 来自 80 端口的流量走表 100
ip rule add sport 80 table 100
```

**基本写法：设置规则优先级**
`ip rule add from <IP> table <表号> priority <优先级>`
```bash
# 设置规则优先级为 100
ip rule add from 192.168.1.100 table 100 priority 100
```

**基本写法：删除策略路由规则**
`ip rule del from <源IP> table <表号>`
```bash
# 删除策略路由规则
ip rule del from 192.168.1.100 table 100
```

---

## 路由表管理

**基本写法：查看指定路由表**
`ip route show table <表号>`
```bash
# 查看表 100 的路由
ip route show table 100
```

**基本写法：添加路由到指定表**
`ip route add <网络>/<前缀> via <网关> table <表号>`
```bash
# 添加路由到表 100
ip route add default via 192.168.1.1 table 100
```

**基本写法：清空路由表**
`ip route flush table <表号>`
```bash
# 清空表 100 的所有路由
ip route flush table 100
```

---

## 多路径路由

**基本写法：添加多路径路由**
`ip route add <网络>/<前缀> nexthop via <网关1> nexthop via <网关2>`
```bash
# 添加多路径负载均衡路由
ip route add 10.0.0.0/24 nexthop via 192.168.1.1 weight 1 nexthop via 192.168.1.2 weight 1
```

**基本写法：指定多路径接口**
`ip route add <网络>/<前缀> nexthop dev <接口1> nexthop dev <接口2>`
```bash
# 通过多个接口负载均衡
ip route add default nexthop dev eth0 nexthop dev eth1
```

---

## 路由持久化

**基本写法：Ubuntu 持久化路由**
`# /etc/netplan/01-routes.yaml`
```yaml
# Netplan 持久化路由配置
network:
  version: 2
  ethernets:
    eth0:
      routes:
        - to: 10.0.0.0/24
          via: 192.168.1.254
        - to: 172.16.0.0/16
          via: 192.168.1.253
```

**基本写法：CentOS 持久化路由**
`# /etc/sysconfig/network-scripts/route-<接口>`
```bash
# 持久化路由配置
echo "10.0.0.0/24 via 192.168.1.254 dev eth0" > /etc/sysconfig/network-scripts/route-eth0
```

**基本写法：RHEL 8+ 持久化路由**
`nmcli connection modify <连接> +ipv4.routes "<网络>/<前缀> <网关>"`
```bash
# 通过 nmcli 添加持久路由
nmcli connection modify eth0 +ipv4.routes "10.0.0.0/24 192.168.1.254"
nmcli connection up eth0
```

---

## ARP 排查

**基本写法：检查 ARP 冲突**
`arping -D <IP>`
```bash
# 检测 IP 地址冲突
arping -D 192.168.1.100
```

**基本写法：清除 ARP 缓存**
`ip neigh flush all`
```bash
# 清除所有 ARP 缓存
ip neigh flush all
```

**基本写法：查看 ARP 请求**
`tcpdump -i eth0 arp`
```bash
# 抓取 ARP 协议流量
tcpdump -i eth0 arp
```

**基本写法：统计 ARP 表**
`ip neigh | wc -l`
```bash
# 统计 ARP 表条目数
ip neigh | wc -l
```

<!-- ============================================================ networking/033-HTTPProtocol ============================================================ -->

## HTTP 请求方法

**基本写法：GET 请求资源**
`GET <路径> HTTP/1.1`
```http
# 获取指定资源
GET /api/users HTTP/1.1
Host: example.com
```

**基本写法：POST 创建资源**
`POST <路径> HTTP/1.1`
```http
# 提交数据创建资源
POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 25

{"name":"John","age":30}
```

**基本写法：PUT 更新资源**
`PUT <路径> HTTP/1.1`
```http
# 完整更新资源
PUT /api/users/1 HTTP/1.1
Host: example.com
Content-Type: application/json

{"name":"Jane","age":25}
```

**基本写法：DELETE 删除资源**
`DELETE <路径> HTTP/1.1`
```http
# 删除指定资源
DELETE /api/users/1 HTTP/1.1
Host: example.com
```

**基本写法：PATCH 部分更新**
`PATCH <路径> HTTP/1.1`
```http
# 部分更新资源
PATCH /api/users/1 HTTP/1.1
Host: example.com
Content-Type: application/json

{"age":26}
```

**基本写法：HEAD 获取头信息**
`HEAD <路径> HTTP/1.1`
```http
# 只获取响应头
HEAD /api/users HTTP/1.1
Host: example.com
```

**基本写法：OPTIONS 探测支持的方法**
`OPTIONS <路径> HTTP/1.1`
```http
# 查询服务器支持的方法
OPTIONS /api/users HTTP/1.1
Host: example.com
```

---

## HTTP 状态码

**基本写法：2xx 成功响应**
`HTTP/1.1 <状态码> <原因短语>`
```http
# 200 OK 请求成功
HTTP/1.1 200 OK
Content-Type: application/json

{"id":1,"name":"John"}
```

**基本写法：3xx 重定向**
`HTTP/1.1 301 Moved Permanently`
```http
# 301 永久重定向
HTTP/1.1 301 Moved Permanently
Location: https://example.com/new-path
```

**基本写法：4xx 客户端错误**
`HTTP/1.1 404 Not Found`
```http
# 404 资源不存在
HTTP/1.1 404 Not Found
Content-Type: application/json

{"error":"User not found"}
```

**基本写法：5xx 服务端错误**
`HTTP/1.1 500 Internal Server Error`
```http
# 500 服务器内部错误
HTTP/1.1 500 Internal Server Error
Content-Type: application/json

{"error":"Database connection failed"}
```

---

## 常用请求头

**基本写法：Host 头**
`Host: <域名>`
```http
# 指定目标主机
Host: example.com
```

**基本写法：User-Agent**
`User-Agent: <UA字符串>`
```http
# 标识客户端类型
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
```

**基本写法：Accept**
`Accept: <MIME类型>`
```http
# 指定可接受的内容类型
Accept: application/json, text/html
```

**基本写法：Authorization**
`Authorization: <类型> <凭证>`
```http
# Bearer Token 认证
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**基本写法：Content-Type**
`Content-Type: <MIME类型>`
```http
# 指定请求体类型
Content-Type: application/json
```

**基本写法：Cookie**
`Cookie: <键>=<值>[; <键>=<值>]`
```http
# 发送 Cookie
Cookie: session=abc123; user_id=1001
```

---

## 常用响应头

**基本写法：Content-Type 响应**
`Content-Type: <MIME类型>`
```http
# 指定响应内容类型
Content-Type: application/json; charset=utf-8
```

**基本写法：Set-Cookie**
`Set-Cookie: <键>=<值>; <选项>`
```http
# 设置 Cookie
Set-Cookie: session=abc123; Path=/; HttpOnly; Secure; Max-Age=3600
```

**基本写法：Cache-Control**
`Cache-Control: <指令>`
```http
# 控制缓存行为
Cache-Control: no-cache, no-store, must-revalidate
```

**基本写法：CORS 头**
`Access-Control-Allow-Origin: <源>`
```http
# 允许跨域访问
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

**基本写法：Location**
`Location: <URL>`
```http
# 重定向目标
Location: https://example.com/new-page
```

---

## HTTP 认证方式

**基本写法：Basic 认证**
`Authorization: Basic <Base64编码>`
```http
# 用户名密码 Base64 编码
Authorization: Basic dXNlcjpwYXNzd29yZA==
```

**基本写法：Bearer Token**
`Authorization: Bearer <token>`
```http
# Bearer Token 认证
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
```

**基本写法：API Key**
`X-API-Key: <密钥>`
```http
# API Key 认证
X-API-Key: abc123def456
```

**基本写法：Digest 认证**
`Authorization: Digest <参数>`
```http
# Digest 摘要认证
Authorization: Digest username="admin", realm="example", nonce="abc", uri="/api", response="xyz"
```

---

## URL 结构

**基本写法：完整 URL 结构**
`<协议>://<用户>:<密码>@<主机>:<端口>/<路径>?<查询>#<片段>`
```text
# URL 各部分组成
https://user:pass@example.com:8080/api/users?page=1#section1
```

**基本写法：URL 编码**
`<编码字符>`
```text
# 特殊字符编码：空格为 %20 或 +
# / 为 %2F
# ? 为 %3F
# & 为 %26
# = 为 %3D
```

---

## Cookie 属性

**基本写法：设置 Cookie 过期时间**
`Set-Cookie: <键>=<值>; Expires=<日期>`
```http
# 设置 Cookie 过期时间
Set-Cookie: session=abc123; Expires=Wed, 09 Jun 2026 10:18:14 GMT
```

**基本写法：设置 Cookie 最大存活时间**
`Set-Cookie: <键>=<值>; Max-Age=<秒数>`
```http
# 设置 Cookie 存活 3600 秒
Set-Cookie: token=xyz; Max-Age=3600
```

**基本写法：设置 Cookie 作用域**
`Set-Cookie: <键>=<值>; Domain=<域>; Path=<路径>`
```http
# 设置 Cookie 作用域
Set-Cookie: session=abc123; Domain=.example.com; Path=/
```

**基本写法：安全 Cookie**
`Set-Cookie: <键>=<值>; Secure; HttpOnly; SameSite=<策略>`
```http
# 安全 Cookie 设置
Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Strict
```

---

## HTTP 缓存

**基本写法：强缓存**
`Cache-Control: max-age=<秒数>`
```http
# 浏览器强缓存 3600 秒
Cache-Control: max-age=3600
```

**基本写法：协商缓存**
`ETag: "<标签>"`
```http
# 资源唯一标识
ETag: "abc123"
```

**基本写法：Last-Modified**
`Last-Modified: <日期>`
```http
# 资源最后修改时间
Last-Modified: Wed, 09 Jun 2026 10:18:14 GMT
```

**基本写法：条件请求**
`If-None-Match: "<标签>"`
```http
# 客户端验证资源是否变更
If-None-Match: "abc123"
```

---

## HTTPS 与 SSL/TLS

**基本写法：HTTPS 请求**
`https://<域名>/<路径>`
```text
# HTTPS 加密连接
https://example.com/api/users
```

**基本写法：TLS 握手**
```text
# TLS 握手过程
1. ClientHello -> 客户端发送支持的加密套件
2. ServerHello -> 服务器选择加密套件
3. Certificate -> 服务器发送证书
4. KeyExchange -> 密钥交换
5. Finished -> 握手完成
```

**基本写法：HSTS 强制 HTTPS**
`Strict-Transport-Security: max-age=<秒数>`
```http
# 强制浏览器使用 HTTPS
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

---

## HTTP 版本对比

**基本写法：HTTP/1.1 请求**
`GET / HTTP/1.1`
```http
# HTTP/1.1 持久连接
GET /api/users HTTP/1.1
Host: example.com
Connection: keep-alive
```

**基本写法：HTTP/2 特性**
```text
# HTTP/2 主要特性
- 多路复用：单个连接并行多个请求
- 头部压缩：HPACK 算法压缩头部
- 服务端推送：Server Push
- 二进制分帧：二进制格式传输
```

**基本写法：HTTP/3 特性**
```text
# HTTP/3 基于 QUIC 协议
- 使用 UDP 而非 TCP
- 集成 TLS 1.3
- 解决队头阻塞问题
- 连接迁移
```

---

## 实用 HTTP 调试

**基本写法：使用 curl 发送请求**
`curl -v <URL>`
```bash
# 详细模式查看 HTTP 通信过程
curl -v https://example.com
```

**基本写法：查看响应头**
`curl -I <URL>`
```bash
# 只查看响应头
curl -I https://example.com
```

**基本写法：telnet 测试 HTTP**
`telnet <主机> <端口>`
```bash
# 使用 telnet 手动发送 HTTP 请求
telnet example.com 80
GET / HTTP/1.1
Host: example.com

```

**基本写法：查看 TLS 证书**
`openssl s_client -connect <主机>:443`
```bash
# 查看 HTTPS 证书详情
openssl s_client -connect example.com:443 -servername example.com
```

<!-- ============================================================ networking/034-WgetDownload ============================================================ -->

## wget 基本下载

**基本写法：下载文件**
`wget <URL>`
```bash
# 下载文件到当前目录
wget https://example.com/file.zip
```

**基本写法：指定保存文件名**
`wget -O <文件名> <URL>`
```bash
# 保存为指定文件名
wget -O archive.zip https://example.com/file.zip
```

**基本写法：指定保存目录**
`wget -P <目录> <URL>`
```bash
# 保存到指定目录
wget -P /tmp/downloads https://example.com/file.zip
```

**基本写法：静默下载**
`wget -q <URL>`
```bash
# 静默模式不显示输出
wget -q https://example.com/file.zip
```

**基本写法：显示进度条**
`wget --show-progress <URL>`
```bash
# 显示下载进度条
wget --show-progress https://example.com/file.zip
```

---

## 断点续传

**基本写法：继续中断的下载**
`wget -c <URL>`
```bash
# 断点续传下载大文件
wget -c https://example.com/bigfile.iso
```

**基本写法：限制重试次数**
`wget -t <次数> <URL>`
```bash
# 失败时重试 5 次
wget -t 5 https://example.com/file.zip
```

**基本写法：无限重试**
`wget -t inf <URL>`
```bash
# 无限重试直到成功
wget -t inf https://example.com/file.zip
```

**基本写法：设置重试间隔**
`wget --waitretry=<秒数> <URL>`
```bash
# 每次重试等待 10 秒
wget --waitretry=10 https://example.com/file.zip
```

---

## 递归下载

**基本写法：递归下载网站**
`wget -r <URL>`
```bash
# 递归下载整个网站
wget -r https://example.com/
```

**基本写法：指定递归深度**
`wget -r -l <深度> <URL>`
```bash
# 递归深度为 2
wget -r -l 2 https://example.com/
```

**基本写法：不追溯父目录**
`wget -r -np <URL>`
```bash
# 只下载指定目录下内容
wget -r -np https://example.com/docs/
```

**基本写法：转换为本地链接**
`wget -r -k <URL>`
```bash
# 下载后将链接转换为本地链接
wget -r -k https://example.com/
```

**基本写法：下载完整页面资源**
`wget -r -k -p <URL>`
```bash
# 下载页面所有依赖资源（图片、CSS、JS）
wget -r -k -p https://example.com/page.html
```

---

## 镜像网站

**基本写法：镜像整个网站**
`wget -m <URL>`
```bash
# 镜像网站（等同 -r -N -l inf）
wget -m https://example.com/
```

**基本写法：完整镜像**
`wget -m -k -K -E <URL>`
```bash
# 镜像并转换链接为本地可浏览
wget -m -k -K -E https://example.com/
```

**基本写法：指定 User-Agent 镜像**
`wget -m --user-agent="<UA>" <URL>`
```bash
# 伪装浏览器镜像
wget -m --user-agent="Mozilla/5.0" https://example.com/
```

---

## 过滤下载

**基本写法：接受指定文件类型**
`wget -r -A <类型> <URL>`
```bash
# 只下载 PDF 文件
wget -r -A pdf https://example.com/
```

**基本写法：拒绝指定文件类型**
`wget -r -R <类型> <URL>`
```bash
# 不下载图片文件
wget -r -R jpg,jpeg,png,gif https://example.com/
```

**基本写法：接受指定文件模式**
`wget -r -A "<模式>" <URL>`
```bash
# 只下载特定模式的文件
wget -r -A "*.tar.gz" https://example.com/
```

**基本写法：拒绝指定目录**
`wget -r -X <目录> <URL>`
```bash
# 不下载指定目录
wget -r -X /private /admin https://example.com/
```

**基本写法：只下载指定目录**
`wget -r -I <目录> <URL>`
```bash
# 只下载指定目录
wget -r -I /docs,/api https://example.com/
```

---

## 认证下载

**基本写法：HTTP 基本认证**
`wget --http-user=<用户> --http-password=<密码> <URL>`
```bash
# HTTP 基本认证下载
wget --http-user=admin --http-password=secret https://example.com/file.zip
```

**基本写法：FTP 认证**
`wget --ftp-user=<用户> --ftp-password=<密码> <URL>`
```bash
# FTP 认证下载
wget --ftp-user=user --ftp-password=pass ftp://example.com/file.zip
```

**基本写法：从文件读取认证**
`wget --auth-no-challenge --http-user=<用户> --http-password=<密码> <URL>`
```bash
# 强制发送认证信息
wget --auth-no-challenge --http-user=admin --http-password=secret https://example.com/
```

---

## Cookie 处理

**基本写法：发送 Cookie**
`wget --header="Cookie: <cookie>" <URL>`
```bash
# 通过 Header 发送 Cookie
wget --header="Cookie: session=abc123" https://example.com/protected
```

**基本写法：加载 Cookie 文件**
`wget --load-cookies <文件> <URL>`
```bash
# 从文件加载 Cookie
wget --load-cookies cookies.txt https://example.com/
```

**基本写法：保存 Cookie**
`wget --save-cookies <文件> <URL>`
```bash
# 保存响应中的 Cookie
wget --save-cookies cookies.txt https://example.com/login
```

**基本写法：保持会话**
`wget --keep-session-cookies --save-cookies <文件> <URL>`
```bash
# 保持会话 Cookie
wget --keep-session-cookies --save-cookies cookies.txt https://example.com/
```

---

## 限速与超时

**基本写法：限制下载速度**
`wget --limit-rate=<速度> <URL>`
```bash
# 限制下载速度为 1MB/s
wget --limit-rate=1M https://example.com/file.zip
```

**基本写法：设置超时**
`wget -T <秒数> <URL>`
```bash
# 设置 30 秒超时
wget -T 30 https://example.com/file.zip
```

**基本写法：设置连接超时**
`wget --connect-timeout=<秒数> <URL>`
```bash
# 设置 10 秒连接超时
wget --connect-timeout=10 https://example.com/file.zip
```

**基本写法：等待间隔**
`wget -w <秒数> <URL>`
```bash
# 每次请求间隔 2 秒
wget -w 2 -r https://example.com/
```

**基本写法：随机等待**
`wget --random-wait -r <URL>`
```bash
# 随机等待 0.5-1.5 秒避免被封锁
wget --random-wait -r https://example.com/
```

---

## 代理设置

**基本写法：使用 HTTP 代理**
`wget -e "http_proxy=<代理>" <URL>`
```bash
# 通过 HTTP 代理下载
wget -e "http_proxy=http://proxy.example.com:8080" https://example.com/
```

**基本写法：使用环境变量代理**
```bash
`export http_proxy=http://<代理>:<端口>
export https_proxy=http://<代理>:<端口>
wget <URL>`
```
```bash
# 通过环境变量设置代理
export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080
wget https://example.com/
```

**基本写法：使用 HTTPS 代理**
`wget -e "https_proxy=<代理>" <URL>`
```bash
# 通过 HTTPS 代理下载
wget -e "https_proxy=http://proxy.example.com:8080" https://example.com/
```

---

## 批量下载

**基本写法：从文件读取 URL 批量下载**
`wget -i <文件>`
```bash
# 从 urls.txt 读取 URL 列表下载
wget -i urls.txt
```

**基本写法：指定输入文件并断点续传**
`wget -c -i <文件>`
```bash
# 批量断点续传下载
wget -c -i urls.txt
```

**基本写法：后台批量下载**
`wget -b -i <文件>`
```bash
# 后台批量下载
wget -b -i urls.txt
```

**基本写法：使用 URL 模板批量下载**
`wget <URL模式>`
```bash
# 批量下载编号文件
wget https://example.com/file{1..100}.zip
```

---

## 后台下载

**基本写法：后台运行下载**
`wget -b <URL>`
```bash
# 后台下载文件
wget -b https://example.com/bigfile.iso
```

**基本写法：指定日志文件**
`wget -b -o <日志> <URL>`
```bash
# 后台下载并记录日志
wget -b -o download.log https://example.com/file.zip
```

**基本写法：追加日志**
`wget -b -a <日志> <URL>`
```bash
# 后台下载并追加日志
wget -b -a download.log https://example.com/file.zip
```

---

## 实用下载组合

**基本写法：下载并解压**
`wget -qO- <URL> | tar xz`
```bash
# 下载 tar.gz 并直接解压
wget -qO- https://example.com/archive.tar.gz | tar xz
```

**基本写法：下载到标准输出**
`wget -qO- <URL>`
```bash
# 输出到标准输出而非文件
wget -qO- https://example.com/script.sh | bash
```

**基本写法：检查 URL 是否存在**
`wget --spider <URL>`
```bash
# 只检查 URL 可用性不下载
wget --spider https://example.com/file.zip
```

**基本写法：下载完整网站用于离线浏览**
`wget --mirror --convert-links --adjust-extension --page-requisites --no-parent <URL>`
```bash
# 完整镜像网站用于离线浏览
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com/
```

**基本写法：模拟浏览器下载**
`wget --user-agent="<UA>" --referer="<来源>" <URL>`
```bash
# 伪装浏览器来源下载
wget --user-agent="Mozilla/5.0" --referer="https://google.com" https://example.com/file.zip
```

<!-- ============================================================ networking/035-VPNConfig ============================================================ -->

## OpenVPN 服务端配置

**基本写法:初始化 PKI 证书目录**
`./easyrsa init-pki`
```bash
# 进入 EasyRSA 目录并初始化 PKI
cd /etc/openvpn/easy-rsa
./easyrsa init-pki
```

**基本写法:构建 CA 根证书**
`./easyrsa build-ca`
```bash
# 构建证书颁发机构(输入 CA 名称和密码)
./easyrsa build-ca nopass
```

**基本写法:生成服务端证书**
`./easyrsa gen-req <名称> <参数>`
```bash
# 生成服务端证书请求和私钥
./easyrsa gen-req server nopass
```

**基本写法:签发服务端证书**
`./easyrsa sign-req server <名称>`
```bash
# 用 CA 签发服务端证书
./easyrsa sign-req server server
```

**基本写法:生成 Diffie-Hellman 参数**
`./easyrsa gen-dh`
```bash
# 生成 DH 参数文件(用于密钥交换)
./easyrsa gen-dh
```

**基本写法:生成 TLS-AUTH 密钥**
`openvpn --genkey --secret <文件>`
```bash
# 生成 tls-auth 共享密钥增强安全性
openvpn --genkey --secret /etc/openvpn/ta.key
```

---

## OpenVPN 服务配置文件

**基本写法:服务端主配置**
`port <端口>`
```bash
# /etc/openvpn/server.conf 主要参数
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh.pem
server 10.8.0.0 255.255.255.0
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 8.8.8.8"
keepalive 10 120
cipher AES-256-GCM
auth SHA256
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
verb 3
```

**基本写法:启动 OpenVPN 服务端**
`openvpn --config <配置文件>`
```bash
# 前台调试运行 OpenVPN
openvpn --config /etc/openvpn/server.conf
```

**基本写法:通过 systemd 启动服务**
`systemctl start openvpn@<实例>`
```bash
# 启动指定实例的 OpenVPN 服务
systemctl start openvpn@server
systemctl enable openvpn@server
```

**基本写法:启用 IP 转发**
`sysctl -w net.ipv4.ip_forward=1`
```bash
# 临时开启 IPv4 转发
sysctl -w net.ipv4.ip_forward=1

# 永久生效写入配置文件
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p
```

**基本写法:配置 NAT 转发**
`iptables -t nat -A POSTROUTING -s <网段> -o <出口网卡> -j MASQUERADE`
```bash
# 对 VPN 网段做 NAT 转发
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
```

---

## OpenVPN 客户端配置

**基本写法:客户端配置文件**
`client`
```bash
# /etc/openvpn/client.conf 主要参数
client
dev tun
proto udp
remote your-server.example.com 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert client1.crt
key client1.key
remote-cert-tls server
cipher AES-256-GCM
auth SHA256
verb 3
```

**基本写法:启动客户端连接**
`openvpn --config <配置文件>`
```bash
# 前台运行 OpenVPN 客户端
openvpn --config /etc/openvpn/client.conf
```

**基本写法:后台守护进程方式启动**
`openvpn --config <配置文件> --daemon`
```bash
# 以守护进程方式运行
openvpn --config /etc/openvpn/client.conf --daemon --log /var/log/openvpn.log
```

**基本写法:使用用户名密码认证**
`auth-user-pass <文件>`
```bash
# 客户端配置中使用密码文件
echo "username" > /etc/openvpn/pass.txt
echo "password" >> /etc/openvpn/pass.txt
chmod 600 /etc/openvpn/pass.txt
# 配置文件加入
# auth-user-pass /etc/openvpn/pass.txt
```

**基本写法:连接指定协议端口**
`remote <服务器> <端口> <协议>`
```bash
# 使用 TCP 协议连接 443 端口
# 在 client.conf 中配置
remote vpn.example.com 443 tcp
```

---

## OpenVPN 管理与调试

**基本写法:查看连接状态**
`cat /etc/openvpn/openvpn-status.log`
```bash
# 查看当前连接的客户端列表
cat /etc/openvpn/openvpn-status.log
```

**基本写法:开启管理接口**
`management <地址> <端口> <密码文件>`
```bash
# 在 server.conf 中启用管理接口
# management 127.0.0.1 7505
# 重启服务后连接
telnet 127.0.0.1 7505
```

**基本写法:查看路由表**
`ip route show`
```bash
# 查看是否成功注入 VPN 路由
ip route show
```

**基本写法:调试模式运行**
`openvpn --config <配置文件> --verb <级别>`
```bash
# 最高级别详细日志输出
openvpn --config /etc/openvpn/client.conf --verb 5
```

**基本写法:查看 OpenVPN 日志**
`tail -f /var/log/openvpn.log`
```bash
# 实时查看 OpenVPN 日志输出
tail -f /var/log/openvpn.log
```

---

## WireGuard 安装与初始化

**基本写法:安装 WireGuard**
`apt install wireguard`
```bash
# Debian/Ubuntu 安装 WireGuard
apt update && apt install -y wireguard wireguard-tools
```

**基本写法:生成服务端私钥**
`wg genkey > <文件>`
```bash
# 生成服务端私钥
wg genkey > /etc/wireguard/server_private.key
chmod 600 /etc/wireguard/server_private.key
```

**基本写法:生成服务端公钥**
`cat <私钥文件> | wg pubkey > <文件>`
```bash
# 由私钥派生公钥
cat /etc/wireguard/server_private.key | wg pubkey > /etc/wireguard/server_public.key
```

**基本写法:生成预共享密钥**
`wg genpsk > <文件>`
```bash
# 生成预共享密钥提升安全性
wg genpsk > /etc/wireguard/preshared.key
```

**基本写法:一次性生成密钥对**
`wg genkey | tee <私钥> | wg pubkey > <公钥>`
```bash
# 同时生成私钥和公钥
wg genkey | tee /etc/wireguard/client_private.key | wg pubkey > /etc/wireguard/client_public.key
```

---

## WireGuard 服务端配置

**基本写法:服务端配置文件**
`wg setconf wg0 <配置文件>`
```bash
# /etc/wireguard/wg0.conf 服务端配置
[Interface]
PrivateKey = <server_private_key>
Address = 10.0.0.1/24
ListenPort = 51820
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = <client_public_key>
PresharedKey = <preshared_key>
AllowedIPs = 10.0.0.2/32
```

**基本写法:启动 WireGuard 接口**
`wg-quick up <接口名>`
```bash
# 启动 wg0 接口
wg-quick up wg0
```

**基本写法:停止接口**
`wg-quick down <接口名>`
```bash
# 停止 wg0 接口
wg-quick down wg0
```

**基本写法:设置开机自启**
`systemctl enable wg-quick@<接口>`
```bash
# 设置 wg0 开机自启
systemctl enable wg-quick@wg0
systemctl start wg-quick@wg0
```

**基本写法:查看接口状态**
`wg show`
```bash
# 查看所有 WireGuard 接口状态
wg show
```

---

## WireGuard 客户端配置

**基本写法:客户端配置文件**
```bash
# /etc/wireguard/wg0.conf 客户端配置
[Interface]
PrivateKey = <client_private_key>
Address = 10.0.0.2/24
DNS = 8.8.8.8

[Peer]
PublicKey = <server_public_key>
PresharedKey = <preshared_key>
Endpoint = vpn.example.com:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

**基本写法:启动客户端**
`wg-quick up <接口>`
```bash
# 启动客户端 VPN 接口
wg-quick up wg0
```

**基本写法:AllowedIPs 全局代理**
`AllowedIPs = 0.0.0.0/0`
```bash
# 所有流量走 VPN(全局代理)
# 在 [Peer] 段配置
AllowedIPs = 0.0.0.0/0
```

**基本写法:仅代理特定网段**
`AllowedIPs = <网段>`
```bash
# 仅特定网段走 VPN(分流)
AllowedIPs = 10.0.0.0/24, 192.168.10.0/24
```

**基本写法:配置持久保活**
`PersistentKeepalive = <秒>`
```bash
# 每 25 秒发送保活包穿越 NAT
PersistentKeepalive = 25
```

---

## WireGuard 动态管理

**基本写法:动态添加 Peer**
`wg set <接口> peer <公钥> allowed-ips <网段>`
```bash
# 动态向 wg0 添加 Peer(无需重启)
wg set wg0 peer $(cat client_public.key) allowed-ips 10.0.0.3/32
```

**基本写法:动态删除 Peer**
`wg set <接口> peer <公钥> remove`
```bash
# 动态删除指定 Peer
wg set wg0 peer ABCD...KEY...XYZ= remove
```

**基本写法:查看 Peer 信息**
`wg show <接口>`
```bash
# 查看 wg0 接口详细状态
wg show wg0
```

**基本写法:查看接口握手时间**
`wg show all latest-handshakes`
```bash
# 查看所有接口的最近握手时间
wg show all latest-handshakes
```

**基本写法:保存当前配置**
`wg-quick save <接口>`
```bash
# 将当前运行时配置保存到配置文件
wg-quick save wg0
```

---

## IPsec strongSwan 配置

**基本写法:安装 strongSwan**
`apt install strongswan`
```bash
# 安装 strongSwan IPsec 套件
apt install -y strongswan strongswan-charon strongswan-starter
```

**基本写法:配置 IPsec 配置文件**
`/etc/ipsec.conf`
```bash
# /etc/ipsec.conf 主配置文件
config setup
    charondebug="ike 2, knl 2, cfg 2"
    uniqueids=no

conn %default
    keyexchange=ikev2
    ike=aes256-sha256-modp2048!
    esp=aes256-sha256!
    dpdaction=clear
    dpddelay=300s
    rekey=no

conn ikev2-vpn
    auto=add
    compress=no
    type=tunnel
    fragmentation=yes
    left=0.0.0.0
    leftcert=server.cert.pem
    leftsendcert=always
    leftsubnet=0.0.0.0/0
    right=%any
    rightauth=eap-mschapv2
    rightsourceip=10.10.10.0/24
    rightdns=8.8.8.8
    eap_identity=%any
```

**基本写法:配置预共享密钥**
`/etc/ipsec.secrets`
```bash
# /etc/ipsec.secrets 认证密钥文件
: RSA "server.key.pem"
user1 : EAP "password123"
user2 : EAP "anotherpass"
# PSK 预共享密钥示例
%any %any : PSK "shared_secret_key"
```

**基本写法:启动 IPsec 服务**
`systemctl start ipsec`
```bash
# 启动 strongSwan IPsec 服务
systemctl start ipsec
systemctl enable ipsec
```

**基本写法:重载 IPsec 配置**
`ipsec reload`
```bash
# 重新加载 IPsec 配置
ipsec reload
```

---

## IPsec 状态与调试

**基本写法:查看 IPsec 状态**
`ipsec status`
```bash
# 查看 IPsec 连接状态
ipsec status
```

**基本写法:查看所有连接**
`ipsec statusall`
```bash
# 查看所有 IPsec 连接详细信息
ipsec statusall
```

**基本写法:发起连接**
`ipsec up <连接名>`
```bash
# 手动发起 IPsec 连接
ipsec up ikev2-vpn
```

**基本写法:断开连接**
`ipsec down <连接名>`
```bash
# 断开指定 IPsec 连接
ipsec down ikev2-vpn
```

**基本写法:查看安全关联**
`ipsec xfrm state`
```bash
# 查看 IPsec SA 状态
ipsec xfrm state
ipsec xfrm policy
```

**基本写法:查看 charon 日志**
`journalctl -u charon`
```bash
# 实时查看 charon 守护进程日志
journalctl -u charon -f
```

---

## VPN 防火墙配置

**基本写法:开放 OpenVPN 端口**
`iptables -A INPUT -p udp --dport <端口> -j ACCEPT`
```bash
# 开放 OpenVPN 默认 UDP 1194 端口
iptables -A INPUT -p udp --dport 1194 -j ACCEPT
```

**基本写法:开放 WireGuard 端口**
`iptables -A INPUT -p udp --dport 51820 -j ACCEPT`
```bash
# 开放 WireGuard 默认 UDP 51820 端口
iptables -A INPUT -p udp --dport 51820 -j ACCEPT
```

**基本写法:开放 IPsec 端口**
`iptables -A INPUT -p udp -m multiport --dports 500,4500 -j ACCEPT`
```bash
# 开放 IPsec IKE(500)和 NAT-T(4500)端口
iptables -A INPUT -p udp -m multiport --dports 500,4500 -j ACCEPT
iptables -A INPUT -p esp -j ACCEPT
```

**基本写法:允许 VPN 网段转发**
`iptables -A FORWARD -s <网段> -j ACCEPT`
```bash
# 允许 VPN 客户端网段转发
iptables -A FORWARD -s 10.8.0.0/24 -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
```

**基本写法:firewalld 添加服务**
`firewall-cmd --permanent --add-service=openvpn`
```bash
# 使用 firewalld 开放 OpenVPN 服务
firewall-cmd --permanent --add-service=openvpn
firewall-cmd --permanent --add-masquerade
firewall-cmd --reload
```

---

## VPN 故障排查

**基本写法:检查 VPN 接口**
`ip addr show <接口>`
```bash
# 查看 tun/wg 接口是否正常
ip addr show tun0
ip addr show wg0
```

**基本写法:测试 VPN 连通性**
`ping <VPN网关>`
```bash
# 测试到 VPN 网关的连通性
ping -c 4 10.8.0.1
```

**基本写法:跟踪路由路径**
`traceroute <目标>`
```bash
# 查看到目标的路径确认是否走 VPN
traceroute 8.8.8.8
```

**基本写法:验证 DNS 解析**
`nslookup <域名> <DNS>`
```bash
# 通过 VPN 的 DNS 服务器解析域名
nslookup example.com 8.8.8.8
```

**基本写法:抓包分析 VPN 流量**
`tcpdump -i <接口> -n`
```bash
# 抓取 VPN 接口数据包
tcpdump -i tun0 -n
tcpdump -i wg0 -n udp port 51820
```

<!-- ============================================================ networking/036-WiresharkCLI ============================================================ -->

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

<!-- ============================================================ networking/037-IPv6Commands ============================================================ -->

## IPv6 地址配置

**基本写法:查看 IPv6 地址**
`ip -6 addr show`
```bash
# 查看所有接口的 IPv6 地址
ip -6 addr show
# 查看指定接口
ip -6 addr show dev eth0
```

**基本写法:添加 IPv6 地址**
`ip -6 addr add <IPv6/前缀> dev <接口>`
```bash
# 为 eth0 添加 IPv6 地址
ip -6 addr add 2001:db8::1/64 dev eth0
```

**基本写法:删除 IPv6 地址**
`ip -6 addr del <IPv6/前缀> dev <接口>`
```bash
# 删除指定 IPv6 地址
ip -6 addr del 2001:db8::1/64 dev eth0
```

**基本写法:启用 IPv6**
`sysctl -w net.ipv6.conf.all.disable_ipv6=0`
```bash
# 临时启用 IPv6
sysctl -w net.ipv6.conf.all.disable_ipv6=0
sysctl -w net.ipv6.conf.default.disable_ipv6=0
```

**基本写法:禁用 IPv6**
`sysctl -w net.ipv6.conf.all.disable_ipv6=1`
```bash
# 临时禁用 IPv6
sysctl -w net.ipv6.conf.all.disable_ipv6=1
```

---

## IPv6 路由配置

**基本写法:查看 IPv6 路由表**
`ip -6 route show`
```bash
# 查看 IPv6 路由表
ip -6 route show
```

**基本写法:添加默认路由**
`ip -6 route add default via <网关> dev <接口>`
```bash
# 添加 IPv6 默认路由
ip -6 route add default via 2001:db8::1 dev eth0
```

**基本写法:添加静态路由**
`ip -6 route add <网段> via <网关>`
```bash
# 添加到指定网段的 IPv6 路由
ip -6 route add 2001:db8:1::/64 via 2001:db8::1
```

**基本写法:删除路由**
`ip -6 route del <网段> via <网关>`
```bash
# 删除指定 IPv6 路由
ip -6 route del 2001:db8:1::/64 via 2001:db8::1
```

**基本写法:查看路由缓存**
`ip -6 route get <目标>`
```bash
# 查看到目标的实际路由
ip -6 route get 2001:db8::100
```

---

## IPv6 邻居发现

**基本写法:查看邻居表**
`ip -6 neigh show`
```bash
# 查看 IPv6 邻居发现缓存(类似 ARP)
ip -6 neigh show
```

**基本写法:添加静态邻居**
`ip -6 neigh add <IPv6> lladdr <MAC> dev <接口>`
```bash
# 添加静态邻居条目
ip -6 neigh add 2001:db8::2 lladdr 00:11:22:33:44:55 dev eth0
```

**基本写法:删除邻居条目**
`ip -6 neigh del <IPv6> dev <接口>`
```bash
# 删除指定邻居条目
ip -6 neigh del 2001:db8::2 dev eth0
```

**基本写法:刷新邻居缓存**
`ip -6 neigh flush dev <接口>`
```bash
# 刷新指定接口的邻居缓存
ip -6 neigh flush dev eth0
```

**基本写法:查看邻居代理**
`ip -6 neigh show proxy`
```bash
# 查看 IPv6 邻居代理
ip -6 neigh show proxy
```

---

## IPv6 ping 与探测

**基本写法:基本 ping6 测试**
`ping6 <目标>`
```bash
# 测试 IPv6 连通性
ping6 2001:db8::1
ping6 -c 4 2001:db8::1
```

**基本写法:指定接口 ping**
`ping6 -I <接口> <目标>`
```bash
# 通过指定接口 ping
ping6 -I eth0 fe80::1
```

**基本写法:链路本地地址 ping**
`ping6 -I <接口> fe80::<地址>`
```bash
# ping 链路本地地址必须指定接口
ping6 -I eth0 fe80::1
```

**基本写法:大包 ping 测试**
`ping6 -s <字节> <目标>`
```bash
# 发送大包测试
ping6 -s 1400 -c 4 2001:db8::1
```

**基本写法:持续 ping**
`ping6 <目标>`
```bash
# 持续 ping 直到手动停止
ping6 2001:db8::1
```

---

## IPv6 路由跟踪

**基本写法:traceroute6 跟踪**
`traceroute6 <目标>`
```bash
# IPv6 路由跟踪
traceroute6 2001:db8::1
```

**基本写法:指定跳数**
`traceroute6 -m <跳数> <目标>`
```bash
# 最多 15 跳
traceroute6 -m 15 2001:db8::1
```

**基本写法:指定探测次数**
`traceroute6 -q <次数> <目标>`
```bash
# 每跳探测 3 次
traceroute6 -q 3 2001:db8::1
```

**基本写法:tracepath6 跟踪**
`tracepath6 <目标>`
```bash
# 显示路径并探测 MTU
tracepath6 2001:db8::1
```

**基本写法:mtr6 跟踪**
`mtr -6 <目标>`
```bash
# 使用 mtr 的 IPv6 模式
mtr -6 2001:db8::1
```

---

## IPv6 网络服务

**基本写法:telnet IPv6 服务**
`telnet -6 <地址> <端口>`
```bash
# 测试 IPv6 端口连通性
telnet -6 2001:db8::1 80
```

**基本写法:curl IPv6**
`curl -6 http://[<IPv6>]:<端口>/`
```bash
# 通过 IPv6 访问 HTTP 服务
curl -6 -v http://[2001:db8::1]:8080/
```

**基本写法:ssh 通过 IPv6**
`ssh -6 <用户>@<IPv6>`
```bash
# SSH 连接到 IPv6 主机
ssh -6 user@2001:db8::1
```

**基本写法:netcat IPv6 测试**
`nc -6 <地址> <端口>`
```bash
# 使用 nc 测试 IPv6 端口
nc -6 -zv 2001:db8::1 80
```

**基本写法:wget 通过 IPv6**
`wget -6 http://[<IPv6>]/`
```bash
# 使用 wget 强制 IPv6 下载
wget -6 http://[2001:db8::1]/index.html
```

---

## IPv6 DNS 解析

**基本写法:AAAA 记录查询**
`dig AAAA <域名>`
```bash
# 查询域名 IPv6 地址
dig AAAA example.com
dig AAAA example.com +short
```

**基本写法:nslookup 查询 IPv6**
`nslookup -type=AAAA <域名>`
```bash
# 使用 nslookup 查询 IPv6
nslookup -type=AAAA example.com
```

**基本写法:host 查询 IPv6**
`host -t AAAA <域名>`
```bash
# 使用 host 命令查询
host -t AAAA example.com
```

**基本写法:反向 DNS 解析**
`dig -x <IPv6>`
```bash
# IPv6 反向解析
dig -x 2001:db8::1
```

**基本写法:指定 DNS 服务器查询**
`dig @<DNS服务器> AAAA <域名>`
```bash
# 通过指定 DNS 服务器查询 IPv6
dig @8.8.8.8 AAAA example.com
```

---

## IPv6 隧道配置

**基本写法:6to4 隧道**
`ip tunnel add <隧道> mode sit remote <IPv4> local <IPv4>`
```bash
# 创建 6to4 隧道
ip tunnel add tun6to4 mode sit remote any local 203.0.113.1
ip link set tun6to4 up
ip -6 addr add 2002:cb00:7101::1/16 dev tun6to4
ip -6 route add 2002::/16 dev tun6to4
```

**基本写法:GRE IPv6 隧道**
`ip tunnel add <名称> mode ip6gre remote <IPv6> local <IPv6>`
```bash
# 创建 IPv6 GRE 隧道
ip tunnel add gre6 mode ip6gre remote 2001:db8::2 local 2001:db8::1
ip link set gre6 up
```

**基本写法:删除隧道**
`ip tunnel del <隧道名>`
```bash
# 删除隧道接口
ip tunnel del tun6to4
```

**基本写法:查看隧道**
`ip tunnel show`
```bash
# 查看所有隧道
ip tunnel show
```

**基本写法:6in4 隧道配置**
```bash
# Hurricane Electric 隧道 broker 配置示例
ip tunnel add he-ipv6 mode sit remote 216.66.84.42 local 203.0.113.1
ip link set he-ipv6 up
ip addr add 2001:470:xxxx::2/64 dev he-ipv6
ip -6 route add default dev he-ipv6
```

---

## IPv6 多播与组管理

**基本写法:查看多播组**
`ip -6 maddr show`
```bash
# 查看 IPv6 多播组
ip -6 maddr show
```

**基本写法:查看接口多播**
`ip -6 maddr show dev <接口>`
```bash
# 查看指定接口多播组
ip -6 maddr show dev eth0
```

**基本写法:加入多播组**
`ip -6 maddr add <多播地址> dev <接口>`
```bash
# 加入指定多播组
ip -6 maddr add ff02::1 dev eth0
```

**基本写法:查看 MLD**
`netstat -g -6`
```bash
# 查看 MLD(组播侦听者发现)
netstat -gn
```

**基本写法:多播路由**
`ip -6 mroute show`
```bash
# 查看 IPv6 多播路由
ip -6 mroute show
```

---

## IPv6 防火墙

**基本写法:ip6tables 基本规则**
`ip6tables -A INPUT -p tcp --dport <端口> -j ACCEPT`
```bash
# 允许 IPv6 SSH
ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
# 允许 ICMPv6(必需)
ip6tables -A INPUT -p icmpv6 -j ACCEPT
```

**基本写法:允许 ICMPv6**
`ip6tables -A INPUT -p icmpv6 -j ACCEPT`
```bash
# ICMPv6 对 IPv6 必需(邻居发现等)
ip6tables -A INPUT -p icmpv6 -j ACCEPT
ip6tables -A OUTPUT -p icmpv6 -j ACCEPT
```

**基本写法:设置默认策略**
`ip6tables -P INPUT DROP`
```bash
# 设置默认策略
ip6tables -P INPUT DROP
ip6tables -P FORWARD DROP
ip6tables -P OUTPUT ACCEPT
```

**基本写法:查看规则**
`ip6tables -L -n -v`
```bash
# 查看 IPv6 防火墙规则
ip6tables -L -n -v
ip6tables -L -n --line-numbers
```

**基本写法:保存规则**
`ip6tables-save > /etc/iptables/rules.v6`
```bash
# 保存 IPv6 防火墙规则
ip6tables-save > /etc/iptables/rules.v6
ip6tables-restore < /etc/iptables/rules.v6
```

---

## IPv6 故障排查

**基本写法:验证 IPv6 启用**
`cat /proc/sys/net/ipv6/conf/all/disable_ipv6`
```bash
# 检查 IPv6 是否启用
cat /proc/sys/net/ipv6/conf/all/disable_ipv6
# 0 表示启用,1 表示禁用
```

**基本写法:测试 IPv6 连通性**
`ping6 -c 3 2001:4860:4860::8888`
```bash
# 测试到 Google IPv6 DNS 的连通性
ping6 -c 3 2001:4860:4860::8888
```

**基本写法:查看 IPv6 监听端口**
`ss -6 -tlnp`
```bash
# 查看服务是否监听 IPv6
ss -6 -tlnp
netstat -6 -tlnp
```

**基本写法:抓包分析 IPv6**
`tcpdump -i <接口> ip6 -n`
```bash
# 抓取 IPv6 数据包
tcpdump -i eth0 ip6 -n
tcpdump -i eth0 icmp6 -n
```

**基本写法:检查 IPv6 路由**
`ip -6 route show`
```bash
# 检查 IPv6 路由配置是否正确
ip -6 route show
ip -6 rule show
```

<!-- ============================================================ networking/038-ProxyConfig ============================================================ -->

## 环境变量代理

**基本写法:设置 HTTP 代理**
`export http_proxy=http://<代理>:<端口>`
```bash
# 设置 HTTP 代理环境变量
export http_proxy=http://proxy.example.com:8080
export HTTP_PROXY=http://proxy.example.com:8080
```

**基本写法:设置 HTTPS 代理**
`export https_proxy=http://<代理>:<端口>`
```bash
# 设置 HTTPS 代理环境变量
export https_proxy=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

**基本写法:设置不代理地址**
`export no_proxy=<地址列表>`
```bash
# 设置不走代理的地址
export no_proxy=localhost,127.0.0.1,192.168.0.0/16,*.local
export NO_PROXY=localhost,127.0.0.1
```

**基本写法:带认证的代理**
`export http_proxy=http://<用户>:<密码>@<代理>:<端口>`
```bash
# 设置带用户名密码认证的代理
export http_proxy=http://user:password@proxy.example.com:8080
```

**基本写法:取消代理设置**
`unset http_proxy https_proxy`
```bash
# 取消所有代理环境变量
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY no_proxy NO_PROXY
```

---

## Squid 代理服务器

**基本写法:安装 Squid**
`yum install squid`
```bash
# 安装 Squid 代理服务器
yum install -y squid
# Debian/Ubuntu
apt install -y squid
```

**基本写法:Squid 基本配置**
`/etc/squid/squid.conf`
```bash
# /etc/squid/squid.conf 主配置
http_port 3128
cache_dir ufs /var/spool/squid 100 16 256
cache_mem 256 MB
maximum_object_size 100 MB
access_log /var/log/squid/access.log
cache_log /var/log/squid/cache.log
visible_hostname proxy.example.com

# 允许本地网段访问
acl localnet src 192.168.0.0/16
acl localnet src 10.0.0.0/8
http_access allow localnet
http_access deny all
```

**基本写法:配置认证代理**
`/etc/squid/squid.conf`
```bash
# 配置基本认证
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm Squid Proxy
auth_param basic credentialsttl 2 hours
acl authenticated proxy_auth REQUIRED
http_access allow authenticated
http_access deny all
```

**基本写法:生成认证密码文件**
`htpasswd -c /etc/squid/passwd <用户>`
```bash
# 创建 Squid 认证密码文件
htpasswd -c /etc/squid/passwd user1
htpasswd /etc/squid/passwd user2
```

**基本写法:启动 Squid**
`systemctl start squid`
```bash
# 启动 Squid 服务
systemctl start squid
systemctl enable squid
systemctl reload squid
```

---

## Squid 访问控制

**基本写法:基于时间控制**
`acl <名称> time <时间>`
```bash
# 工作时间访问控制
acl workhours time MTWHF 09:00-18:00
acl weekend time SA
http_access allow localnet workhours
http_access deny all
```

**基本写法:基于域名控制**
`acl <名称> dstdomain <域名>`
```bash
# 域名访问控制
acl allowed_sites dstdomain .example.com .google.com
acl blocked_sites dstdomain .badsite.com
http_access deny blocked_sites
http_access allow localnet allowed_sites
```

**基本写法:基于 URL 正则**
`acl <名称> url_regex <正则>`
```bash
# 通过 URL 关键字过滤
acl blockfiles urlpath_regex -i \.mp4$ \.avi$ \.exe$
http_access deny blockfiles
```

**基本写法:基于端口控制**
`acl <名称> port <端口>`
```bash
# 限制可访问端口
acl allowed_ports port 80 443 8080
http_access deny !allowed_ports
```

**基本写法:基于源 IP 限制**
`acl <名称> src <IP>`
```bash
# 基于源 IP 限制
acl allowed_clients src 192.168.1.0/24
http_access allow allowed_clients
http_access deny all
```

---

## HAProxy 负载均衡

**基本写法:安装 HAProxy**
`yum install haproxy`
```bash
# 安装 HAProxy
yum install -y haproxy
apt install -y haproxy
```

**基本写法:HAProxy 基本配置**
`/etc/haproxy/haproxy.cfg`
```bash
# /etc/haproxy/haproxy.cfg
global
    log /dev/log local0
    maxconn 4096
    user haproxy
    group haproxy
    daemon

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000ms
    timeout client  50000ms
    timeout server  50000ms

frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server web1 192.168.1.10:80 check
    server web2 192.168.1.11:80 check
```

**基本写法:基于域名的转发**
`/etc/haproxy/haproxy.cfg`
```bash
# 基于域名分发
frontend http_front
    bind *:80
    acl is_site1 hdr(host) -i site1.example.com
    acl is_site2 hdr(host) -i site2.example.com
    use_backend site1_back if is_site1
    use_backend site2_back if is_site2
    default_backend site1_back

backend site1_back
    server web1 192.168.1.10:80 check

backend site2_back
    server web2 192.168.1.11:80 check
```

**基本写法:TCP 模式负载均衡**
`/etc/haproxy/haproxy.cfg`
```bash
# TCP 模式(用于 MySQL 等)
frontend mysql_front
    bind *:3306
    mode tcp
    default_backend mysql_back

backend mysql_back
    mode tcp
    balance leastconn
    server db1 192.168.1.20:3306 check
    server db2 192.168.1.21:3306 check
```

**基本写法:启动 HAProxy**
`systemctl start haproxy`
```bash
# 启动 HAProxy
systemctl start haproxy
systemctl enable haproxy
systemctl reload haproxy
```

---

## HAProxy 监控与统计

**基本写法:开启统计页面**
`/etc/haproxy/haproxy.cfg`
```bash
# 开启 HAProxy 统计页面
listen stats
    bind *:8080
    mode http
    stats enable
    stats uri /stats
    stats realm HAProxy\ Statistics
    stats auth admin:password
    stats admin if TRUE
```

**基本写法:健康检查配置**
`option httpchk <方法> <路径>`
```bash
# HTTP 健康检查
backend http_back
    option httpchk GET /health
    http-check expect status 200
    server web1 192.168.1.10:80 check inter 2000 rise 2 fall 3
```

**基本写法:会话保持**
`cookie <名称>`
```bash
# 基于 cookie 的会话保持
backend http_back
    cookie SERVERID insert indirect nocache
    server web1 192.168.1.10:80 cookie server1 check
    server web2 192.168.1.11:80 cookie server2 check
```

**基本写法:访问控制列表**
`acl <名称> <条件>`
```bash
# ACL 综合应用
frontend http_front
    bind *:80
    acl is_https dst_port 80
    acl blocked_ip src 192.168.1.100
    http-request deny if blocked_ip
    default_backend http_back
```

---

## Nginx 反向代理

**基本写法:基本反向代理**
`/etc/nginx/conf.d/proxy.conf`
```bash
# /etc/nginx/conf.d/proxy.conf
server {
    listen 80;
    server_name proxy.example.com;

    location / {
        proxy_pass http://192.168.1.10:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

**基本写法:负载均衡代理**
`/etc/nginx/conf.d/lb.conf`
```bash
# Nginx 负载均衡
upstream backend {
    server 192.168.1.10:8080 weight=3;
    server 192.168.1.11:8080 weight=2;
    server 192.168.1.12:8080;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```

**基本写法:负载均衡算法**
```bash
# 不同负载均衡算法
upstream backend_round {
    # 轮询(默认)
    server 192.168.1.10:8080;
    server 192.168.1.11:8080;
}

upstream backend_ip {
    # IP 哈希(会话保持)
    ip_hash;
    server 192.168.1.10:8080;
    server 192.168.1.11:8080;
}

upstream backend_least {
    # 最少连接
    least_conn;
    server 192.168.1.10:8080;
    server 192.168.1.11:8080;
}
```

**基本写法:HTTPS 反向代理**
`/etc/nginx/conf.d/ssl-proxy.conf`
```bash
# HTTPS 反向代理到 HTTP 后端
server {
    listen 443 ssl;
    server_name proxy.example.com;

    ssl_certificate /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    location / {
        proxy_pass http://192.168.1.10:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
    }
}
```

**基本写法:健康检查被动模式**
```bash
# Nginx 被动健康检查
upstream backend {
    server 192.168.1.10:8080 max_fails=3 fail_timeout=30s;
    server 192.168.1.11:8080 max_fails=3 fail_timeout=30s;
}
```

---

## Nginx 代理高级配置

**基本写法:缓存配置**
`/etc/nginx/nginx.conf`
```bash
# 代理缓存配置
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m;

server {
    location / {
        proxy_cache my_cache;
        proxy_cache_valid 200 302 10m;
        proxy_cache_valid 404 1m;
        proxy_pass http://backend;
    }
}
```

**基本写法:WebSocket 代理**
```bash
# 支持 WebSocket 的反向代理
location /ws/ {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 86400;
}
```

**基本写法:超时控制**
```bash
# 代理超时配置
location / {
    proxy_pass http://backend;
    proxy_connect_timeout 5s;
    proxy_send_timeout 30s;
    proxy_read_timeout 60s;
    proxy_buffering on;
    proxy_buffer_size 16k;
    proxy_buffers 8 32k;
}
```

**基本写法:重定向后端**
```bash
# 路径重写
location /api/ {
    rewrite ^/api/(.*)$ /$1 break;
    proxy_pass http://backend;
}
```

**基本写法:Nginx 启动与重载**
`nginx -t && systemctl reload nginx`
```bash
# 测试配置并重载
nginx -t
systemctl reload nginx
systemctl restart nginx
```

---

## 代理客户端配置

**基本写法:curl 使用代理**
`curl -x <代理> <URL>`
```bash
# curl 指定 HTTP 代理
curl -x http://proxy.example.com:8080 http://target.com
# SOCKS5 代理
curl --socks5 127.0.0.1:1080 http://target.com
```

**基本写法:wget 使用代理**
`wget -e "http_proxy=<代理>" <URL>`
```bash
# wget 指定代理
wget -e "http_proxy=http://proxy.example.com:8080" http://target.com
```

**基本写法:SSH 通过代理**
`ssh -o ProxyCommand="nc -X 5 -x <代理> %h %p" <主机>`
```bash
# SSH 通过 SOCKS 代理连接
ssh -o ProxyCommand="nc -X 5 -x 127.0.0.1:1080 %h %p" user@target.com
```

**基本写法:apt 使用代理**
`/etc/apt/apt.conf.d/proxy`
```bash
# 配置 apt 走代理
echo 'Acquire::http::Proxy "http://proxy.example.com:8080";' > /etc/apt/apt.conf.d/proxy
echo 'Acquire::https::Proxy "http://proxy.example.com:8080";' >> /etc/apt/apt.conf.d/proxy
```

**基本写法:YUM 使用代理**
`/etc/yum.conf`
```bash
# 配置 yum 走代理
echo "proxy=http://proxy.example.com:8080" >> /etc/yum.conf
echo "proxy_username=user" >> /etc/yum.conf
echo "proxy_password=password" >> /etc/yum.conf
```

---

## 代理故障排查

**基本写法:测试代理连通性**
`curl -v -x <代理> http://<目标>`
```bash
# 详细模式测试代理
curl -v -x http://proxy.example.com:8080 http://httpbin.org/ip
```

**基本写法:检查代理端口**
`telnet <代理> <端口>`
```bash
# 测试代理端口是否开放
telnet proxy.example.com 8080
nc -zv proxy.example.com 8080
```

**基本写法:查看代理日志**
`tail -f /var/log/squid/access.log`
```bash
# 实时查看 Squid 访问日志
tail -f /var/log/squid/access.log
tail -f /var/log/haproxy.log
tail -f /var/log/nginx/access.log
```

**基本写法:抓包分析代理流量**
`tcpdump -i <接口> port <端口>`
```bash
# 抓取代理端口流量
tcpdump -i eth0 port 3128 -n
tcpdump -i eth0 port 8080 -n -A
```

**基本写法:检查代理状态**
`systemctl status squid`
```bash
# 检查代理服务状态
systemctl status squid
systemctl status haproxy
systemctl status nginx
```

---

## SOCKS 代理

**基本写法:SSH 创建 SOCKS 代理**
`ssh -D <端口> <主机>`
```bash
# 通过 SSH 创建本地 SOCKS5 代理
ssh -D 1080 user@remote.example.com
# 后台运行
ssh -fN -D 1080 user@remote.example.com
```

**基本写法:动态端口转发**
`ssh -D <本地端口> -N <主机>`
```bash
# 仅做端口转发不执行命令
ssh -D 1080 -N -C user@remote.example.com
```

**基本写法:使用 dante SOCKS 服务器**
`/etc/sockd.conf`
```bash
# /etc/sockd.conf dante 服务器配置
logoutput: /var/log/sockd.log
internal: eth0 port = 1080
external: eth0
socksmethod: username
user.privileged: root
user.notprivileged: nobody

client pass {
    from: 192.168.0.0/16
    to: 0.0.0.0/0
    log: connect disconnect error
}

socks pass {
    from: 192.168.0.0/16
    to: 0.0.0.0/0
    log: connect disconnect error
}
```

**基本写法:验证 SOCKS 代理**
`curl --socks5 <代理> http://<目标>`
```bash
# 验证 SOCKS5 代理
curl --socks5 127.0.0.1:1080 http://httpbin.org/ip
# SOCKS5 远程 DNS 解析
curl --socks5-hostname 127.0.0.1:1080 http://httpbin.org/ip
```
