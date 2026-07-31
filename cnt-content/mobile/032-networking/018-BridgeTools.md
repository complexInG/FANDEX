# Networking 网桥工具

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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
