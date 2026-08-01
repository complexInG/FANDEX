---
order: 300
title: Networking SSH 远程连接
module: 032-networking
category: '032-networking'
difficulty: beginner
description: Networking SSH 远程连接 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
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
| Networking SSH 远程连接 | 030-SSHRemote | 本文自身 |
| Networking nc 与 nmap | 031-NetcatNmap | 本文的并列主题 |
| Networking ARP 与路由 | 032-ARPRouting | 本文的并列主题 |
| Networking HTTP 协议 | 033-HTTPProtocol | 本文的并列主题 |
| Networking wget 文件下载 | 034-WgetDownload | 本文的并列主题 |
| Networking VPN 配置命令 | 035-VPNConfig | 本文的并列主题 |
| Networking Wireshark 命令行 | 036-WiresharkCLI | 本文的并列主题 |
| Networking IPv6 网络命令 | 037-IPv6Commands | 本文的并列主题 |
| Networking 代理配置 | 038-ProxyConfig | 本文的并列主题 |
