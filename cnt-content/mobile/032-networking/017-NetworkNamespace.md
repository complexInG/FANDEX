# Networking Linux 网络命名空间

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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
