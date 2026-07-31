# Cybersecurity Wireshark 安全分析

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## tshark 基础操作

**基本写法:列出所有接口**
`tshark -D`
```bash
# 列出所有可用抓包接口
tshark -D
```

**基本写法:实时抓包**
`tshark -i <接口>`
```bash
# 监听 eth0 接口实时抓包
tshark -i eth0
```

**基本写法:抓包保存到文件**
`tshark -i <接口> -w <文件>`
```bash
# 抓包并保存为 PCAP 文件
tshark -i eth0 -w capture.pcap
```

**基本写法:读取 PCAP 文件**
`tshark -r <PCAP文件>`
```bash
# 读取并显示 PCAP 文件内容
tshark -r capture.pcap
```

**基本写法:限制抓包数量**
`tshark -i <接口> -c <数量>`
```bash
# 抓取 100 个包后停止
tshark -i eth0 -c 100
```

---

## tshark 显示过滤

**基本写法:按 IP 过滤**
`tshark -r <PCAP文件> -Y "ip.addr == <IP>"`
```bash
# 过滤指定 IP 的所有流量
tshark -r capture.pcap -Y "ip.addr == 192.168.1.100"
```

**基本写法:按端口过滤**
`tshark -r <PCAP文件> -Y "tcp.port == <端口>"`
```bash
# 过滤指定端口的流量
tshark -r capture.pcap -Y "tcp.port == 443"
```

**基本写法:按协议过滤**
`tshark -r <PCAP文件> -Y "<协议>"`
```bash
# 过滤 HTTP 协议流量
tshark -r capture.pcap -Y "http"
```

**基本写法:组合过滤条件**
`tshark -r <PCAP文件> -Y "ip.src == <IP> and tcp.port == <端口>"`
```bash
# 组合源 IP 与端口过滤
tshark -r capture.pcap -Y "ip.src == 192.168.1.100 and tcp.port == 80"
```

**基本写法:过滤 HTTP 方法**
`tshark -r <PCAP文件> -Y "http.request.method == <方法>"`
```bash
# 过滤 POST 请求
tshark -r capture.pcap -Y "http.request.method == POST"
```

---

## tshark 抓包过滤(BPF)

**基本写法:抓取指定主机流量**
`tshark -i <接口> -f "host <IP>"`
```bash
# 仅抓取指定主机的流量
tshark -i eth0 -f "host 192.168.1.100"
```

**基本写法:抓取指定端口**
`tshark -i <接口> -f "port <端口>"`
```bash
# 仅抓取 80 端口流量
tshark -i eth0 -f "port 80"
```

**基本写法:抓取多端口流量**
`tshark -i <接口> -f "port 80 or port 443"`
```bash
# 抓取 Web 流量(80/443)
tshark -i eth0 -f "port 80 or port 443"
```

**基本写法:排除 SSH 流量**
`tshark -i <接口> -f "not port 22"`
```bash
# 抓取除 SSH 外的所有流量
tshark -i eth0 -f "not port 22"
```

**基本写法:抓取特定网段**
`tshark -i <接口> -f "net <网段>"`
```bash
# 抓取特定网段流量
tshark -i eth0 -f "net 192.168.1.0/24"
```

---

## HTTP 流量分析

**基本写法:提取 HTTP 请求 URL**
`tshark -r <PCAP文件> -Y "http.request" -T fields -e http.host -e http.request.uri`
```bash
# 提取所有 HTTP 请求的主机和 URI
tshark -r capture.pcap -Y "http.request" -T fields -e http.host -e http.request.uri
```

**基本写法:提取 HTTP User-Agent**
`tshark -r <PCAP文件> -Y "http.user_agent" -T fields -e http.user_agent`
```bash
# 提取 HTTP 请求中的 User-Agent
tshark -r capture.pcap -Y "http.user_agent" -T fields -e http.user_agent | sort -u
```

**基本写法:提取 HTTP 响应状态码**
`tshark -r <PCAP文件> -Y "http.response" -T fields -e http.response.code`
```bash
# 提取 HTTP 响应状态码
tshark -r capture.pcap -Y "http.response" -T fields -e http.response.code
```

**基本写法:提取 POST 数据**
`tshark -r <PCAP文件> -Y "http.request.method == POST" -T fields -e http.file_data`
```bash
# 提取 POST 请求体数据
tshark -r capture.pcap -Y "http.request.method == POST" -T fields -e http.file_data
```

**基本写法:统计 HTTP 状态码**
`tshark -r <PCAP文件> -Y "http.response" -T fields -e http.response.code | sort | uniq -c`
```bash
# 统计各 HTTP 状态码出现次数
tshark -r capture.pcap -Y "http.response" -T fields -e http.response.code | sort | uniq -c | sort -rn
```

---

## DNS 流量分析

**基本写法:提取 DNS 查询域名**
`tshark -r <PCAP文件> -Y "dns.qry.name" -T fields -e dns.qry.name`
```bash
# 提取所有 DNS 查询的域名
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | sort -u
```

**基本写法:统计 DNS 查询频率**
`tshark -r <PCAP文件> -Y "dns.qry.name" -T fields -e dns.qry.name | sort | uniq -c | sort -rn`
```bash
# 统计域名查询频率检测 DNS 隧道
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | sort | uniq -c | sort -rn | head
```

**基本写法:查找 TXT 记录查询**
`tshark -r <PCAP文件> -Y "dns.qry.type == 16"`
```bash
# 查找 TXT 类型 DNS 查询(可能用于数据外传)
tshark -r capture.pcap -Y "dns.qry.type == 16"
```

**基本写法:检测异常长子域名**
`tshark -r <PCAP文件> -Y "dns.qry.name" -T fields -e dns.qry.name | awk '{if(length($0)>50) print}'`
```bash
# 检测超长子域名可能为 DNS 隧道
tshark -r capture.pcap -Y "dns.qry.name" -T fields -e dns.qry.name | awk '{if(length($0)>50) print}'
```

---

## TLS/SSL 流量分析

**基本写法:提取 TLS SNI**
`tshark -r <PCAP文件> -Y "tls.handshake.extensions_server_name" -T fields -e tls.handshake.extensions_server_name`
```bash
# 提取 TLS 握手中的 SNI 域名
tshark -r capture.pcap -Y "tls.handshake.extensions_server_name" -T fields -e tls.handshake.extensions_server_name
```

**基本写法:统计 TLS 版本**
`tshark -r <PCAP文件> -Y "tls.record.version" -T fields -e tls.record.version | sort | uniq -c`
```bash
# 统计使用的 TLS 版本
tshark -r capture.pcap -Y "tls.record.version" -T fields -e tls.record.version | sort | uniq -c
```

**基本写法:提取证书**
`tshark -r <PCAP文件> -Y "tls.handshake.type == 11" -T fields -e x509sat.printableString`
```bash
# 提取 TLS 证书信息
tshark -r capture.pcap -Y "tls.handshake.type == 11" -T fields -e x509sat.printableString
```

**基本写法:检测弱密码套件**
`tshark -r <PCAP文件> -Y "tls.handshake.ciphersuite"`
```bash
# 查看协商的密码套件
tshark -r capture.pcap -Y "tls.handshake.ciphersuite" -T fields -e tls.handshake.ciphersuite
```

---

## 异常流量检测

**基本写法:统计各 IP 流量**
`tshark -r <PCAP文件> -q -z conv,ip`
```bash
# 统计各 IP 之间的会话流量
tshark -r capture.pcap -q -z conv,ip
```

**基本写法:检测端口扫描**
`tshark -r <PCAP文件> -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" -T fields -e ip.src -e tcp.dstport | sort -u`
```bash
# 检测 SYN 扫描行为
tshark -r capture.pcap -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" -T fields -e ip.src -e tcp.dstport | sort -u
```

**基本写法:统计目标端口**
`tshark -r <PCAP文件> -Y "tcp.flags.syn == 1" -T fields -e tcp.dstport | sort | uniq -c | sort -rn`
```bash
# 统计 SYN 包目标端口分布
tshark -r capture.pcap -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" -T fields -e tcp.dstport | sort | uniq -c | sort -rn | head
```

**基本写法:检测 ARP 欺骗**
`tshark -r <PCAP文件> -Y "arp.duplicate-address-detected"`
```bash
# 检测 ARP 冲突(可能为 ARP 欺骗)
tshark -r capture.pcap -Y "arp.duplicate-address-detected"
```

**基本写法:检测数据外传**
`tshark -r <PCAP文件> -q -z conv,ip | sort -k 4 -rn | head`
```bash
# 按字节数排序查找异常大流量
tshark -r capture.pcap -q -z conv,ip | sort -k 4 -rn | head
```

---

## 流量统计与分析

**基本写法:协议层次统计**
`tshark -r <PCAP文件> -q -z io,phs`
```bash
# 统计协议层次分布
tshark -r capture.pcap -q -z io,phs
```

**基本写法:按时间统计流量**
`tshark -r <PCAP文件> -q -z io,stat,<间隔秒>`
```bash
# 每 60 秒统计一次流量
tshark -r capture.pcap -q -z io,stat,60
```

**基本写法:TCP 会话统计**
`tshark -r <PCAP文件> -q -z conv,tcp`
```bash
# 统计所有 TCP 会话
tshark -r capture.pcap -q -z conv,tcp
```

**基本写法:提取 HTTP 流**
`tshark -r <PCAP文件> -Y "http" -T fields -e tcp.stream | sort -u`
```bash
# 提取所有包含 HTTP 的 TCP 流
tshark -r capture.pcap -Y "http" -T fields -e tcp.stream | sort -u
```

**基本写法:统计包大小分布**
`tshark -r <PCAP文件> -T fields -e frame.len | awk '{if($1<100)s++;else if($1<1000)m++;else l++} END{print "小包:"s,"中包:"m,"大包:"l}'`
```bash
# 统计包大小分布检测异常
tshark -r capture.pcap -T fields -e frame.len | awk '{if($1<100)s++;else if($1<1000)m++;else l++} END{print "小包:"s,"中包:"m,"大包:"l}'
```

---

## 安全事件取证

**基本写法:提取所有明文密码**
`tshark -r <PCAP文件> -Y "ftp or telnet or pop or imap" -T fields -e frame.number -e ip.src -e ip.dst -e tcp.payload`
```bash
# 提取明文协议可能包含密码的流量
tshark -r capture.pcap -Y "ftp or telnet or pop or imap" -T fields -e frame.number -e ip.src -e tcp.payload
```

**基本写法:提取文件传输**
`tshark -r <PCAP文件> --export-objects http,<目录>`
```bash
# 导出 HTTP 传输的文件
tshark -r capture.pcap --export-objects http,./extracted
```

**基本写法:提取 SMB 文件**
`tshark -r <PCAP文件> --export-objects smb,<目录>`
```bash
# 导出 SMB 协议传输的文件
tshark -r capture.pcap --export-objects smb,./smb_files
```

**基本写法:提取特定流的完整数据**
`tshark -r <PCAP文件> -Y "tcp.stream == <流ID>" -T fields -e tcp.payload`
```bash
# 提取指定 TCP 流的完整 payload
tshark -r capture.pcap -Y "tcp.stream == 5" -T fields -e tcp.payload
```

**基本写法:重组 HTTP 会话**
`tshark -r <PCAP文件> -Y "tcp.stream == <流ID>" -z "follow,tcp,ascii,<流ID>"`
```bash
# 跟踪并显示完整 TCP 流会话
tshark -r capture.pcap -Y "tcp.stream == 5" -z "follow,tcp,ascii,5"
```

---

## 抓包性能优化

**基本写法:设置抓包大小**
`tshark -i <接口> -s <字节数>`
```bash
# 仅抓取前 96 字节加快抓包速度
tshark -i eth0 -s 96
```

**基本写法:使用缓冲区**
`tshark -i <接口> -B <缓冲大小KB>`
```bash
# 设置 10MB 内核缓冲区
tshark -i eth0 -B 10240
```

**基本写法:启用 ring buffer**
`tshark -i <接口> -b filesize:<大小KB> -w <文件>`
```bash
# 每 10MB 切换一个抓包文件
tshark -i eth0 -b filesize:10240 -w capture.pcap
```

**基本写法:设置抓包时长**
`tshark -i <接口> -a duration:<秒数>`
```bash
# 抓包 60 秒后自动停止
tshark -i eth0 -a duration:60 -w capture.pcap
```

**基本写法:多文件循环抓包**
`tshark -i <接口> -b duration:<秒> -b files:<文件数> -w <文件前缀>`
```bash
# 每 300 秒切换文件保留最近 10 个
tshark -i eth0 -b duration:300 -b files:10 -w capture.pcap
```
