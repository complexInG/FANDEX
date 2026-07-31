# Networking 网卡绑定与聚合

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## bonding 驱动基础

**基本写法:加载 bonding 模块**
`modprobe bonding`
```bash
# 加载 bonding 内核模块
modprobe bonding

# 查看模块是否加载成功
lsmod | grep bonding
```

**基本写法:设置开机自动加载**
`echo "bonding" > /etc/modules-load.d/bonding.conf`
```bash
# 配置 bonding 模块开机自动加载
echo "bonding" > /etc/modules-load.d/bonding.conf
```

**基本写法:查看 bonding 支持的模式**
`cat /proc/net/bonding/<接口>`
```bash
# 查看指定 bond 接口的详细状态
cat /proc/net/bonding/bond0
```

**基本写法:查看可用 bonding 模式**
`modinfo bonding`
```bash
# 查看 bonding 模块信息和参数
modinfo bonding
```

**基本写法:bonding 七种模式**
```text
# bonding 工作模式说明
mode=0  balance-rr      轮询(默认)
mode=1  active-backup   主备(常用)
mode=2  balance-xor     基于哈希
mode=3  broadcast       广播
mode=4  802.3ad         LACP 动态聚合
mode=5  balance-tlb     自适应负载均衡
mode=6  balance-alb     自适应负载均衡(含负载均衡)
```

---

## bond 接口配置文件

**基本写法:RHEL/CentOS bond 接口配置**
`/etc/sysconfig/network-scripts/ifcfg-bond0`
```bash
# /etc/sysconfig/network-scripts/ifcfg-bond0
DEVICE=bond0
NAME=bond0
TYPE=Bond
BONDING_MASTER=yes
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.1.100
PREFIX=24
GATEWAY=192.168.1.1
DNS1=8.8.8.8
BONDING_OPTS="mode=1 miimon=100 primary=eth0"
```

**基本写法:从接口配置文件**
`/etc/sysconfig/network-scripts/ifcfg-eth0`
```bash
# /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
TYPE=Ethernet
BOOTPROTO=none
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```

**基本写法:Debian/Ubuntu netplan 配置**
`/etc/netplan/01-bond.yaml`
```bash
# /etc/netplan/01-bond.yaml
network:
  version: 2
  renderer: networkd
  bonds:
    bond0:
      dhcp4: no
      addresses: [192.168.1.100/24]
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
      interfaces: [eth0, eth1]
      parameters:
        mode: active-backup
        miimon: 100
        primary: eth0
```

**基本写法:Debian 传统配置**
`/etc/network/interfaces`
```bash
# /etc/network/interfaces Debian 系 bond 配置
auto bond0
iface bond0 inet static
    address 192.168.1.100/24
    gateway 192.168.1.1
    bond-slaves eth0 eth1
    bond-mode 1
    bond-miimon 100
    bond-primary eth0
```

**基本写法:应用 netplan 配置**
`netplan apply`
```bash
# 应用 netplan 配置
netplan apply
```

---

## bond 模式详解

**基本写法:mode=1 主备模式**
`BONDING_OPTS="mode=1 miimon=100 primary=eth0"`
```bash
# 主备模式,eth0 为主,eth1 为备,故障自动切换
BONDING_OPTS="mode=1 miimon=100 primary=eth0 fail_over_mac=1"
```

**基本写法:mode=0 轮询模式**
`BONDING_OPTS="mode=0 miimon=100"`
```bash
# 轮询负载均衡,需交换机支持
BONDING_OPTS="mode=0 miimon=100 xmit_hash_policy=layer2+3"
```

**基本写法:mode=4 LACP 动态聚合**
`BONDING_OPTS="mode=4 miimon=100 lacp_rate=1"`
```bash
# 802.3ad LACP 动态聚合,需交换机支持 LACP
BONDING_OPTS="mode=4 miimon=100 lacp_rate=1 xmit_hash_policy=layer3+4"
```

**基本写法:mode=6 自适应负载均衡**
`BONDING_OPTS="mode=6 miimon=100"`
```bash
# ALB 模式,无需交换机配置即可负载均衡
BONDING_OPTS="mode=6 miimon=100"
```

**基本写法:监控间隔参数**
`miimon=<毫秒>`
```bash
# 每 100 毫秒检测链路状态
miimon=100
# 使用 ARP 监控(替代 MII)
arp_interval=1000
arp_ip_target=192.168.1.1
```

---

## teamd 团队接口

**基本写法:安装 teamd**
`yum install teamd`
```bash
# CentOS/RHEL 安装 teamd
yum install -y teamd

# Debian/Ubuntu 安装
apt install -y teamd
```

**基本写法:创建 team 接口配置**
`teamd -f <配置文件> -d`
```bash
# 创建主备模式 team 接口
cat > /etc/teamd/team0.conf <<EOF
{
    "device": "team0",
    "runner": {
        "name": "activebackup",
        "hwaddr_policy": "by_active"
    },
    "link_watch": {
        "name": "ethtool"
    },
    "ports": {
        "eth0": {},
        "eth1": {}
    }
}
EOF
```

**基本写法:team 模式配置示例**
```bash
# LACP 聚合模式 team 配置
cat > /etc/teamd/team0.conf <<EOF
{
    "device": "team0",
    "runner": {
        "name": "lacp",
        "active": true,
        "fast_rate": true,
        "tx_hash": ["eth", "ipv4", "ipv6"]
    },
    "link_watch": {"name": "ethtool"},
    "ports": {"eth0": {}, "eth1": {}}
}
EOF
```

**基本写法:负载均衡 team 配置**
```bash
# loadbalance 模式 team 配置
cat > /etc/teamd/team0.conf <<EOF
{
    "device": "team0",
    "runner": {
        "name": "loadbalance",
        "tx_hash": ["eth", "ipv4", "ipv6"]
    },
    "link_watch": {"name": "ethtool"},
    "ports": {"eth0": {}, "eth1": {}}
}
EOF
```

**基本写法:启动 team 接口**
`teamd -f <配置文件> -d`
```bash
# 启动 team0 接口
teamd -f /etc/teamd/team0.conf -d

# 停止 team 接口
teamd -f /etc/teamd/team0.conf -k
```

---

## team 接口管理

**基本写法:配置 team 接口 IP**
`ip addr add <IP/前缀> dev <接口>`
```bash
# 为 team 接口配置 IP 地址
ip addr add 192.168.1.100/24 dev team0
ip link set team0 up
```

**基本写法:team 接口 nmcli 配置**
`nmcli connection add type team con-name <名称>`
```bash
# 使用 nmcli 创建 team 接口
nmcli connection add type team con-name team0 ifname team0 config '{"runner":{"name":"activebackup"}}'
nmcli connection modify team0 ipv4.addresses 192.168.1.100/24
nmcli connection modify team0 ipv4.method manual
```

**基本写法:添加从接口到 team**
`nmcli connection add type team-slave`
```bash
# 添加从接口
nmcli connection add type team-slave con-name team0-port1 ifname eth0 master team0
nmcli connection add type team-slave con-name team0-port2 ifname eth1 master team0
```

**基本写法:激活 team 连接**
`nmcli connection up <名称>`
```bash
# 激活 team0 连接
nmcli connection up team0
```

**基本写法:查看 team 状态**
`teamdctl <接口> state`
```bash
# 查看 team0 接口状态
teamdctl team0 state
teamdctl team0 state dump
```

---

## 链路状态监控

**基本写法:查看 bonding 详细状态**
`cat /proc/net/bonding/bond0`
```bash
# 查看 bond0 的主从接口、模式和链路状态
cat /proc/net/bonding/bond0
```

**基本写法:查看 team 接口状态**
`teamdctl team0 state`
```bash
# 查看 team0 当前活动端口和运行状态
teamdctl team0 state
```

**基本写法:查看网卡链路状态**
`ethtool <网卡>`
```bash
# 查看指定网卡链路状态
ethtool eth0
```

**基本写法:查看网卡统计信息**
`ip -s link show <网卡>`
```bash
# 查看网卡收发包统计
ip -s link show eth0
ip -s -s link show eth0
```

**基本写法:实时监控链路变化**
`ip monitor link`
```bash
# 实时监控网卡链路状态变化
ip monitor link
```

---

## bonding 运行时管理

**基本写法:查看当前活动接口**
`cat /proc/net/bonding/bond0 | grep "Currently Active"`
```bash
# 查看当前活动的主接口
cat /proc/net/bonding/bond0 | grep "Currently Active Slave"
```

**基本写法:手动切换主接口**
`ifenslave -c <bond> <接口>`
```bash
# 在主备模式下手动切换到 eth1
ifenslave -c bond0 eth1
```

**基本写法:添加从接口**
`ifenslave <bond> <接口>`
```bash
# 动态添加 eth2 到 bond0
ifenslave bond0 eth2
```

**基本写法:移除从接口**
`ifenslave -d <bond> <接口>`
```bash
# 从 bond0 移除 eth1
ifenslave -d bond0 eth1
```

**基本写法:修改 bonding 参数**
`echo <值> > /sys/class/net/<bond>/bonding/<参数>`
```bash
# 动态修改 bonding 模式(需接口降下)
ip link set bond0 down
echo 1 > /sys/class/net/bond0/bonding/mode
echo 100 > /sys/class/net/bond0/bonding/miimon
ip link set bond0 up
```

---

## 网卡聚合测试与故障排查

**基本写法:测试 bond 带宽**
`iperf3 -c <服务器>`
```bash
# 通过 bond 接口测试带宽
iperf3 -c 192.168.1.10 -t 30 -P 4
```

**基本写法:模拟网卡故障**
`ip link set <网卡> down`
```bash
# 模拟 eth0 故障测试主备切换
ip link set eth0 down

# 恢复网卡
ip link set eth0 up
```

**基本写法:检查聚合是否生效**
`cat /proc/net/bonding/bond0`
```bash
# 查看是否正确识别主备和切换事件
cat /proc/net/bonding/bond0 | grep -E "Slave Interface|MII Status|Link Failure"
```

**基本写法:抓包验证负载均衡**
`tcpdump -i <bond> -n`
```bash
# 抓包查看流量是否在多个接口上分布
tcpdump -i bond0 -n -e
```

**基本写法:检查交换机 LACP 状态**
`show etherchannel summary`
```bash
# Cisco 交换机查看 LACP 聚合组状态
show etherchannel summary
show lacp neighbor
```

---

## 高级聚合配置

**基本写法:VLAN over bond**
`/etc/sysconfig/network-scripts/ifcfg-bond0.100`
```bash
# 在 bond 上配置 VLAN 子接口
DEVICE=bond0.100
BOOTPROTO=none
ONBOOT=yes
IPADDR=10.0.100.1
PREFIX=24
VLAN=yes
PHYSDEV=bond0
```

**基本写法:netplan 配置 VLAN over bond**
```bash
# /etc/netplan/01-bond-vlan.yaml
network:
  version: 2
  renderer: networkd
  bonds:
    bond0:
      interfaces: [eth0, eth1]
      parameters:
        mode: 802.3ad
        miimon: 100
  vlans:
    bond0.100:
      id: 100
      link: bond0
      addresses: [10.0.100.1/24]
```

**基本写法:网桥与 bond 结合**
```bash
# 在 bond 接口上创建网桥
ip link add name br0 type bridge
ip link set bond0 master br0
ip link set br0 up
ip addr add 192.168.1.100/24 dev br0
```

**基本写法:多 bond 接口配置**
`options bonding max_bonds=2`
```bash
# 加载 bonding 模块时支持多个 bond 接口
echo "options bonding max_bonds=2 miimon=100" > /etc/modprobe.d/bonding.conf
```
