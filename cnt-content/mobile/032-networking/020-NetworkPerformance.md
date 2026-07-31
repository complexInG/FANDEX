# Networking 网络性能测试

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## iperf3 基础测试

**基本写法:启动服务端**
`iperf3 -s`
```bash
# 启动 iperf3 服务端监听默认端口 5201
iperf3 -s
# 指定端口
iperf3 -s -p 5201
```

**基本写法:启动后台服务端**
`iperf3 -s -D`
```bash
# 后台守护进程方式启动服务端
iperf3 -s -D
iperf3 -s -D --logfile /var/log/iperf3.log
```

**基本写法:客户端 TCP 测试**
`iperf3 -c <服务器>`
```bash
# 客户端连接服务端测试 TCP 带宽
iperf3 -c 192.168.1.10
```

**基本写法:指定测试时长**
`iperf3 -c <服务器> -t <秒>`
```bash
# 测试 30 秒
iperf3 -c 192.168.1.10 -t 30
```

**基本写法:指定测试数据量**
`iperf3 -c <服务器> -n <字节>`
```bash
# 测试传输 100MB
iperf3 -c 192.168.1.10 -n 100M
```

---

## iperf3 UDP 测试

**基本写法:UDP 带宽测试**
`iperf3 -c <服务器> -u`
```bash
# UDP 模式测试
iperf3 -c 192.168.1.10 -u
```

**基本写法:指定 UDP 带宽**
`iperf3 -c <服务器> -u -b <带宽>`
```bash
# 测试 100Mbps UDP 带宽
iperf3 -c 192.168.1.10 -u -b 100M
# 无限带宽测试
iperf3 -c 192.168.1.10 -u -b 0
```

**基本写法:UDP 丢包率测试**
`iperf3 -c <服务器> -u -b <带宽> -t <秒>`
```bash
# 长时间 UDP 测试观察丢包
iperf3 -c 192.168.1.10 -u -b 1G -t 60
```

**基本写法:UDP 报文长度设置**
`iperf3 -c <服务器> -u -l <字节>`
```bash
# 设置 UDP 包大小为 1400 字节
iperf3 -c 192.168.1.10 -u -l 1400
```

**基本写法:多播测试**
`iperf3 -c <多播地址> -u -B <地址>`
```bash
# UDP 多播测试
iperf3 -s -B 224.0.0.1
iperf3 -c 224.0.0.1 -u -T 32
```

---

## iperf3 并发与反向

**基本写法:多线程并发测试**
`iperf3 -c <服务器> -P <线程数>`
```bash
# 8 线程并发测试
iperf3 -c 192.168.1.10 -P 8
```

**基本写法:反向测试(下行)**
`iperf3 -c <服务器> -R`
```bash
# 测试服务端到客户端方向带宽
iperf3 -c 192.168.1.10 -R
```

**基本写法:双向测试**
`iperf3 -c <服务器> --bidir`
```bash
# 同时双向测试带宽
iperf3 -c 192.168.1.10 --bidir
```

**基本写法:组合测试**
`iperf3 -c <服务器> -P <线程> -t <秒> -R`
```bash
# 多线程反向测试
iperf3 -c 192.168.1.10 -P 4 -t 60 -R
```

**基本写法:JSON 格式输出**
`iperf3 -c <服务器> -J`
```bash
# 输出 JSON 格式结果便于脚本处理
iperf3 -c 192.168.1.10 -J > result.json
```

---

## iperf3 高级选项

**基本写法:指定端口**
`iperf3 -c <服务器> -p <端口>`
```bash
# 指定服务端口
iperf3 -c 192.168.1.10 -p 5201
```

**基本写法:绑定本地端口**
`iperf3 -c <服务器> --bind <本地地址>`
```bash
# 绑定本地 IP 和端口
iperf3 -c 192.168.1.10 --bind 192.168.1.100:12345
```

**基本写法:指定测试间隔**
`iperf3 -c <服务器> -i <秒>`
```bash
# 每 2 秒输出一次结果
iperf3 -c 192.168.1.10 -i 2
```

**基本写法:TCP 窗口大小**
`iperf3 -c <服务器> -w <字节>`
```bash
# 设置 TCP 窗口大小
iperf3 -c 192.168.1.10 -w 256K
```

**基本写法:TCP 报文长度**
`iperf3 -c <服务器> -l <字节>`
```bash
# 设置 TCP 包长度
iperf3 -c 192.168.1.10 -l 8K
```

---

## mtr 网络路径分析

**基本写法:基本 mtr 测试**
`mtr <目标>`
```bash
# 实时显示到目标的路由路径和丢包率
mtr 8.8.8.8
```

**基本写法:报告模式**
`mtr -r <目标>`
```bash
# 输出一次报告后退出
mtr -r 8.8.8.8
mtr -r -c 10 8.8.8.8
```

**基本写法:指定 ping 次数**
`mtr -c <次数> <目标>`
```bash
# 发送 20 个包后停止
mtr -c 20 8.8.8.8
```

**基本写法:UDP 模式**
`mtr -u <目标>`
```bash
# 使用 UDP 协议测试
mtr -u 8.8.8.8
```

**基本写法:TCP 模式**
`mtr -T <目标>`
```bash
# 使用 TCP SYN 模式测试
mtr -T -P 80 8.8.8.8
```

**基本写法:显示 IP 同时显示主机名**
`mtr -b <目标>`
```bash
# 同时显示 IP 和主机名
mtr -b 8.8.8.8
```

---

## mtr 高级用法

**基本写法:输出 CSV 格式**
`mtr -r -C -c <次数> <目标>`
```bash
# CSV 格式报告
mtr -r -C -c 10 8.8.8.8
```

**基本写法:输出 JSON 格式**
`mtr -r -J -c <次数> <目标>`
```bash
# JSON 格式报告
mtr -r -J -c 10 8.8.8.8
```

**基本写法:指定包大小**
`mtr -s <字节> <目标>`
```bash
# 设置 ping 包大小
mtr -s 1000 8.8.8.8
```

**基本写法:指定间隔时间**
`mtr -i <秒> <目标>`
```bash
# 每 2 秒发送一个包
mtr -i 2 8.8.8.8
```

**基本写法:指定最大跳数**
`mtr -m <跳数> <目标>`
```bash
# 最多显示 15 跳
mtr -m 15 8.8.8.8
```

---

## iperf 老版本测试

**基本写法:启动 iperf 服务端**
`iperf -s`
```bash
# 启动 iperf(老版本)服务端
iperf -s
```

**基本写法:客户端 TCP 测试**
`iperf -c <服务器>`
```bash
# 基础 TCP 带宽测试
iperf -c 192.168.1.10
```

**基本写法:UDP 测试**
`iperf -c <服务器> -u -b <带宽>`
```bash
# UDP 模式指定带宽
iperf -c 192.168.1.10 -u -b 100M
```

**基本写法:多线程测试**
`iperf -c <服务器> -P <线程数>`
```bash
# 多线程并发测试
iperf -c 192.168.1.10 -P 4
```

**基本写法:双向测试**
`iperf -c <服务器> -d`
```bash
# 同时双向测试
iperf -c 192.168.1.10 -d
```

---

## 网络延迟测试

**基本写法:ping 测试延迟**
`ping -c <次数> <目标>`
```bash
# 发送 10 个包测试延迟
ping -c 10 8.8.8.8
```

**基本写法:洪水 ping 测试**
`ping -f <目标>`
```bash
# 洪水模式测试(需 root,生产慎用)
ping -f 192.168.1.1
```

**基本写法:指定包大小**
`ping -c <次数> -s <字节> <目标>`
```bash
# 大包测试
ping -c 10 -s 1400 8.8.8.8
```

**基本写法:TCP 延迟测试**
`hping3 -S -p <端口> <目标>`
```bash
# 使用 hping3 测试 TCP 延迟
hping3 -S -p 80 8.8.8.8
```

**基本写法:UDP 延迟测试**
`nping --udp -p <端口> <目标>`
```bash
# 使用 nping 测试 UDP 延迟
nping --udp -p 53 -c 10 8.8.8.8
```

---

## 带宽与吞吐量测试

**基本写法:使用 nuttcp 测试**
`nuttcp -i <服务器>`
```bash
# 服务端模式
nuttcp -S
# 客户端测试
nuttcp -i 1 -T 10 192.168.1.10
```

**基本写法:使用 netperf 测试**
`netperf -H <服务器>`
```bash
# 启动服务端
netserver
# 客户端 TCP_STREAM 测试
netperf -H 192.168.1.10 -t TCP_STREAM
```

**基本写法:UDP_STREAM 测试**
`netperf -H <服务器> -t UDP_STREAM`
```bash
# UDP 流量测试
netperf -H 192.168.1.10 -t UDP_STREAM -- -r 1024
```

**基本写法:使用 dd 网络传输测试**
`dd if=/dev/zero bs=1M count=1000 | ssh <主机> "cat > /dev/null"`
```bash
# 通过 SSH 测试网络传输速率
dd if=/dev/zero bs=1M count=1000 | ssh user@192.168.1.10 "cat > /dev/null"
```

**基本写法:简单 HTTP 下载测速**
`curl -o /dev/null -w "%{speed_download}" <URL>`
```bash
# 测试 HTTP 下载速度
curl -o /dev/null -w "速度: %{speed_download} 字节/秒\n" http://192.168.1.10/largefile
```

---

## 网络质量综合分析

**基本写法:抓包分析重传**
`tshark -i <接口> -Y "tcp.analysis.retransmission"`
```bash
# 实时监控 TCP 重传
tshark -i eth0 -Y "tcp.analysis.retransmission"
```

**基本写法:统计网卡丢包**
`ip -s link show <接口>`
```bash
# 查看网卡收发丢包统计
ip -s link show eth0
```

**基本写法:ethtool 查看网卡统计**
`ethtool -S <接口>`
```bash
# 查看网卡详细统计(含丢包、错误)
ethtool -S eth0 | grep -i drop
```

**基本写法:查看 TCP 重传统计**
`ss -ti`
```bash
# 查看 TCP 连接统计信息
ss -ti
ss -s
```

**基本写法:网络队列丢包**
`netstat -s | grep -i drop`
```bash
# 查看网络栈丢包统计
netstat -s | grep -i drop
netstat -s | grep -i retrans
```

---

## 性能测试脚本

**基本写法:iperf3 自动化测试**
```bash
# 自动化 iperf3 测试脚本
#!/bin/bash
SERVER=192.168.1.10
LOG=/tmp/iperf_result.txt
echo "=== TCP 上行测试 ===" > $LOG
iperf3 -c $SERVER -t 30 -J >> $LOG
echo "=== TCP 下行测试 ===" >> $LOG
iperf3 -c $SERVER -t 30 -R -J >> $LOG
echo "=== UDP 测试 ===" >> $LOG
iperf3 -c $SERVER -u -b 1G -t 30 -J >> $LOG
```

**基本写法:多目标延迟测试**
```bash
# 批量测试多个目标的延迟
for host in 8.8.8.8 8.8.4.4 1.1.1.1; do
    echo "=== $host ==="
    ping -c 10 $host | tail -1
done
```

**基本写法:持续监控带宽**
```bash
# 每 60 秒测试一次带宽
while true; do
    echo "$(date): $(iperf3 -c 192.168.1.10 -t 10 | tail -1)"
    sleep 60
done
```

**基本写法:mtr 定期报告**
```bash
# 定期生成 mtr 报告
while true; do
    echo "=== $(date) ===" >> mtr.log
    mtr -r -c 10 8.8.8.8 >> mtr.log
    sleep 300
done
```
