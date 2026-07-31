# Networking 网络配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
