---
order: 10
title: devops 模块文档合集
module: 'devops'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：031-devops/001-OverviewLinuxBasics.md ============ -->

## 1. DevOps 与 SRE 理念

### 1.1 DevOps 定义

DevOps 是一种强调**开发（Development）与运维（Operations）协作**的文化和实践，旨在缩短交付周期、提高部署频率、降低变更失败率。

### 1.2 DevOps 与 SRE 对比

| 维度         | DevOps                 | SRE                  |
| :----------- | :--------------------- | :------------------- |
| **理念**     | 文化与协作             | 工程化方法论         |
| **目标**     | 加速交付               | 保证可靠性           |
| **方法**     | CI/CD、自动化          | SLI/SLO、错误预算    |
| **角色**     | 全栈工程师             | 可靠性工程师         |
| **核心指标** | 部署频率、变更前置时间 | 可用性、延迟、错误率 |

### 1.3 DevOps 核心实践

```mermaid
flowchart LR
    A[计划] --> B[编码] --> C[构建] --> D[测试] --> E[发布] --> F[部署] --> G[运维] --> H[监控]
    H -.->|持续反馈| A
```

| 实践       | 描述               | 工具                    |
| :--------- | :----------------- | :---------------------- |
| **CI/CD**  | 持续集成与持续交付 | GitHub Actions、Jenkins |
| **IaC**    | 基础设施即代码     | Terraform、Ansible      |
| **容器化** | 应用容器化部署     | Docker、Kubernetes      |
| **监控**   | 全链路可观测性     | Prometheus、Grafana     |
| **自动化** | 减少手动操作       | Ansible、Shell          |

## 2. Linux 系统管理

### 2.1 Linux 发行版

| 发行版           | 特点             | 适用场景       |
| :--------------- | :--------------- | :------------- |
| **Ubuntu**       | 用户友好、包丰富 | 开发环境、桌面 |
| **CentOS/Rocky** | 稳定、兼容 RHEL  | 生产服务器     |
| **Debian**       | 极致稳定         | 服务器、嵌入式 |
| **Alpine**       | 轻量（5MB）      | 容器镜像       |

### 2.2 常用系统命令

```bash
# 系统信息
uname -a                    # 内核版本
cat /etc/os-release         # 系统版本
hostname                    # 主机名
uptime                      # 运行时间和负载

# CPU 信息
lscpu                       # CPU 详细信息
nproc                       # CPU 核心数
top / htop                  # 实时进程监控

# 内存信息
free -h                     # 内存使用情况
vmstat 1 5                  # 虚拟内存统计

# 磁盘信息
df -h                       # 磁盘使用情况
du -sh /path/*              # 目录大小
lsblk                       # 块设备列表
fdisk -l                    # 磁盘分区

# 网络信息
ip addr                     # 网络接口
ip route                    # 路由表
ss -tlnp                    # 监听端口
```

## 3. 文件系统

### 3.1 目录结构

```mermaid
flowchart TD
    T0["/           根目录"]
    T1["bin     基本命令（所有用户可用）"]
    T2["sbin    系统管理命令（root 可用）"]
    T3["etc     配置文件"]
    T4["home    用户主目录"]
    T5["root    root 用户主目录"]
    T6["var     可变数据（日志、缓存）"]
    T7["tmp     临时文件"]
    T8["usr     用户程序"]
    T9["bin   用户命令"]
    T10["lib   库文件"]
    T11["local 本地安装"]
    T12["opt     第三方软件"]
    T13["proc    进程信息（虚拟文件系统）"]
    T14["sys     系统信息（虚拟文件系统）"]
    T15["dev     设备文件"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
    T0 --> T6
    T0 --> T7
    T0 --> T8
    T11 --> T12
    T11 --> T13
    T11 --> T14
    T11 --> T15
```

### 3.2 文件操作

```bash
# 文件查看
cat file.txt               # 查看全部内容
less file.txt              # 分页查看
head -n 20 file.txt        # 前 20 行
tail -f /var/log/syslog    # 实时查看日志

# 文件搜索
find / -name "*.conf" 2>/dev/null     # 按名称搜索
find /var -size +100M                 # 按大小搜索
grep -r "error" /var/log/             # 按内容搜索
locate nginx.conf                     # 快速定位（需 updatedb）

# 文件权限
chmod 755 script.sh         # rwxr-xr-x
chmod +x script.sh          # 添加执行权限
chown user:group file.txt   # 修改所有者
chgrp group file.txt        # 修改所属组

# 软链接与硬链接
ln -s /path/target link     # 软链接（符号链接）
ln /path/target link        # 硬链接
```

### 3.3 文件系统类型

| 类型          | 特点             | 适用场景       |
| :------------ | :--------------- | :------------- |
| **ext4**      | Linux 默认、稳定 | 通用           |
| **XFS**       | 大文件性能好     | 数据库、大文件 |
| **Btrfs**     | 快照、压缩       | NAS、容器      |
| **ZFS**       | 数据完整性、快照 | 存储服务器     |
| **OverlayFS** | 联合挂载         | 容器           |

## 4. 用户与权限

### 4.1 用户管理

```bash
# 用户操作
useradd -m -s /bin/bash newuser    # 创建用户
passwd newuser                      # 设置密码
usermod -aG docker newuser         # 添加到组
userdel -r olduser                  # 删除用户及主目录

# 组操作
groupadd developers                 # 创建组
gpasswd -a user developers          # 添加用户到组
groups user                         # 查看用户所属组

# 切换用户
su - username                       # 切换用户
sudo command                        # 以 root 执行

# sudo 配置
visudo                              # 编辑 sudoers
# 添加: newuser ALL=(ALL) NOPASSWD: /usr/bin/docker
```

### 4.2 权限模型

```mermaid
flowchart TD
    P[权限位解析 -rwxr-xr--]
    P --> O[所有者 rwx 7]
    P --> G[组 r-x 5]
    P --> U[其他用户 r-- 4]
    P --> T[文件类型：- 普通文件，d 目录，l 链接]
```

| 权限  | 数字 | 文件     | 目录          |
| :---- | :--- | :------- | :------------ |
| **r** | 4    | 读取内容 | 列出内容      |
| **w** | 2    | 修改内容 | 创建/删除文件 |
| **x** | 1    | 执行     | 进入目录      |

### 4.3 特殊权限

```bash
# SUID - 以文件所有者身份执行
chmod u+s /usr/bin/passwd    # 4755

# SGID - 以文件所属组身份执行 / 新文件继承组
chmod g+s /shared/dir        # 2755

# Sticky Bit - 只有所有者能删除
chmod +t /tmp                # 1777
```

## 5. Shell 脚本

### 5.1 基础语法

```bash
#!/bin/bash

# 变量
NAME="DevOps"
echo "Hello, $NAME"
echo "进程 PID: $$"
echo "脚本路径: $0"
echo "参数数量: $#"
echo "所有参数: $@"

# 条件判断
if [ -f "/etc/nginx/nginx.conf" ]; then
    echo "Nginx 配置文件存在"
elif [ -d "/etc/nginx" ]; then
    echo "Nginx 目录存在但无配置"
else
    echo "Nginx 未安装"
fi

# 循环
for i in {1..10}; do
    echo "第 $i 次循环"
done

while read line; do
    echo "处理: $line"
done < input.txt

# 函数
check_service() {
    local service=$1
    if systemctl is-active --quiet "$service"; then
        echo "$service 运行中"
        return 0
    else
        echo "$service 未运行"
        return 1
    fi
}

check_service nginx
```

### 5.2 实用脚本

```bash
#!/bin/bash
# 系统健康检查脚本

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_ok()   { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $1"; }

# CPU 检查
check_cpu() {
    local load=$(awk '{print $1}' /proc/loadavg)
    local cores=$(nproc)
    local threshold=$(echo "$cores * 0.8" | bc)
    if (( $(echo "$load > $threshold" | bc -l) )); then
        log_warn "CPU 负载过高: $load (阈值: $threshold)"
    else
        log_ok "CPU 负载正常: $load"
    fi
}

# 内存检查
check_memory() {
    local usage=$(free | awk '/Mem/{printf("%.1f"), $3/$2*100}')
    if (( $(echo "$usage > 90" | bc -l) )); then
        log_fail "内存使用率过高: ${usage}%"
    elif (( $(echo "$usage > 80" | bc -l) )); then
        log_warn "内存使用率偏高: ${usage}%"
    else
        log_ok "内存使用率正常: ${usage}%"
    fi
}

# 磁盘检查
check_disk() {
    local usage=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')
    if [ "$usage" -gt 90 ]; then
        log_fail "磁盘使用率过高: ${usage}%"
    elif [ "$usage" -gt 80 ]; then
        log_warn "磁盘使用率偏高: ${usage}%"
    else
        log_ok "磁盘使用率正常: ${usage}%"
    fi
}

# 服务检查
check_services() {
    for svc in nginx docker sshd; do
        if systemctl is-active --quiet "$svc" 2>/dev/null; then
            log_ok "$svc 运行中"
        else
            log_warn "$svc 未运行"
        fi
    done
}

echo "===== 系统健康检查 $(date) ====="
check_cpu
check_memory
check_disk
check_services
echo "===== 检查完成 ====="
```

## 6. 包管理

### 6.1 APT（Debian/Ubuntu）

```bash
# 更新源
sudo apt update && sudo apt upgrade -y

# 安装/卸载
sudo apt install nginx -y
sudo apt remove nginx --purge
sudo apt autoremove

# 搜索
apt search nginx
apt show nginx

# 添加 PPA
sudo add-apt-repository ppa:nginx/stable
```

### 6.2 YUM/DNF（RHEL/CentOS）

```bash
# 更新
sudo dnf update -y

# 安装
sudo dnf install nginx -y
sudo dnf remove nginx

# 搜索
dnf search nginx
dnf info nginx

# 添加仓库
sudo dnf config-manager --add-repo https://repo.example.com/repo.rpm
```

## 7. systemd 服务管理

### 7.1 常用命令

```bash
# 服务管理
systemctl start nginx       # 启动
systemctl stop nginx        # 停止
systemctl restart nginx     # 重启
systemctl reload nginx      # 重载配置
systemctl status nginx      # 查看状态
systemctl enable nginx      # 开机自启
systemctl disable nginx     # 禁用自启

# 日志查看
journalctl -u nginx         # 服务日志
journalctl -f               # 实时日志
journalctl --since "1 hour ago"
journalctl -p err           # 错误级别日志
```

### 7.2 自定义 Service

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application Service
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
User=appuser
Group=appgroup
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5
Environment=NODE_ENV=production
Environment=PORT=3000

# 安全加固
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/opt/myapp/data /var/log/myapp

[Install]
WantedBy=multi-user.target
```

```bash
# 启用自定义服务
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

## 8. 日志管理

### 8.1 日志位置

| 日志         | 路径                    | 内容         |
| :----------- | :---------------------- | :----------- |
| **系统日志** | `/var/log/syslog`       | 系统消息     |
| **认证日志** | `/var/log/auth.log`     | 登录认证     |
| **内核日志** | `/var/log/kern.log`     | 内核消息     |
| **服务日志** | `journalctl -u service` | systemd 服务 |

### 8.2 日志轮转

```bash
# /etc/logrotate.d/myapp
/var/log/myapp/*.log {
    daily
    rotate 30
    compress
    delaycompress
    missingok
    notifempty
    create 0644 appuser appgroup
    postrotate
        systemctl reload myapp > /dev/null 2>&1 || true
    endspostrotate
}
```

### 8.3 日志分析

```bash
# 统计 HTTP 状态码
awk '{print $9}' access.log | sort | uniq -c | sort -rn

# 统计访问量 Top 10 IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10

# 查找错误
grep -E "ERROR|CRITICAL|FATAL" /var/log/app.log | tail -50

# 按时间段统计
awk '$4 >= "[14/Jun/2026:00:00" && $4 <= "[14/Jun/2026:23:59"' access.log | wc -l
```

## 9. 小结

Linux 基础是 DevOps 工程师的必备技能：

1. **DevOps 理念**强调协作和自动化，SRE 强调可靠性和量化
2. **Linux 系统管理**涵盖 CPU、内存、磁盘、网络的监控和排查
3. **文件系统**理解目录结构和权限模型是安全运维的基础
4. **Shell 脚本**是自动化运维的核心工具，需掌握条件、循环和函数
5. **systemd** 是现代 Linux 的服务管理标准，需熟练编写 Service 文件
6. **日志管理**是故障排查的关键，需掌握日志轮转和分析技巧

<!-- ============ 文档分隔线：031-devops/002-NetworkSecurity.md ============ -->

## 1. TCP/IP 协议栈

### 1.1 OSI 七层 vs TCP/IP 四层

| OSI        | TCP/IP     | 协议                | 数据单元  |
| :--------- | :--------- | :------------------ | :-------- |
| 应用层     | 应用层     | HTTP, DNS, SSH, FTP | 数据      |
| 表示层     | 应用层     | TLS/SSL, JPEG       | 数据      |
| 会话层     | 应用层     | RPC, NetBIOS        | 数据      |
| 传输层     | 传输层     | TCP, UDP            | 段/数据报 |
| 网络层     | 网络层     | IP, ICMP, ARP       | 包        |
| 数据链路层 | 网络接口层 | Ethernet, PPP       | 帧        |
| 物理层     | 网络接口层 | 电信号、光纤        | 比特      |

### 1.2 TCP 三次握手与四次挥手

```mermaid
flowchart TD
    T0["三次握手:"]
    T1["Client          Server"]
    T2["SYN"]
    T3["SYN+ACK"]
    T4["ACK"]
    T5["四次挥手:"]
    T6["Client          Server"]
    T7["FIN"]
    T8["ACK"]
    T9["FIN"]
    T10["ACK"]
    T0 --> T1
    T1 --> T2
    T1 --> T3
    T1 --> T4
    T4 --> T5
    T5 --> T6
    T6 --> T7
    T6 --> T8
    T6 --> T9
    T6 --> T10
```

### 1.3 常用端口

| 端口 | 协议       | 用途      |
| :--- | :--------- | :-------- |
| 22   | SSH        | 远程登录  |
| 53   | DNS        | 域名解析  |
| 80   | HTTP       | Web 服务  |
| 443  | HTTPS      | 安全 Web  |
| 3306 | MySQL      | 数据库    |
| 5432 | PostgreSQL | 数据库    |
| 6379 | Redis      | 缓存      |
| 8080 | HTTP Alt   | 代理/应用 |
| 9090 | Prometheus | 监控      |

## 2. DNS

### 2.1 DNS 解析流程

```
浏览器缓存 → 系统缓存 → 路由器缓存 → ISP DNS
    → 根域名服务器 → 顶级域名服务器 → 权威域名服务器
```

### 2.2 DNS 记录类型

| 类型      | 描述       | 示例                                |
| :-------- | :--------- | :---------------------------------- |
| **A**     | IPv4 地址  | `example.com → 93.184.216.34`       |
| **AAAA**  | IPv6 地址  | `example.com → 2606:2800:220:1:...` |
| **CNAME** | 别名       | `www.example.com → example.com`     |
| **MX**    | 邮件服务器 | `example.com → mail.example.com`    |
| **TXT**   | 文本记录   | SPF、DKIM 验证                      |
| **NS**    | 域名服务器 | `example.com → ns1.dns.com`         |
| **SRV**   | 服务记录   | `_http._tcp → server:port`          |

### 2.3 DNS 排查

```bash
# DNS 查询
dig example.com              # 完整查询
dig +short example.com       # 仅显示 IP
nslookup example.com         # Windows 兼容
host example.com             # 简洁输出

# 指定 DNS 服务器
dig @8.8.8.8 example.com

# 反向解析
dig -x 93.184.216.34

# 追踪解析过程
dig +trace example.com

# DNS 缓存清理
sudo systemd-resolve --flush-caches    # systemd-resolved
sudo rndc flush                         # BIND
```

## 3. HTTP/HTTPS

### 3.1 HTTP 请求方法

| 方法   | 用途       | 幂等 | 安全 |
| :----- | :--------- | :--- | :--- |
| GET    | 获取资源   | 是   | 是   |
| POST   | 创建资源   | 否   | 否   |
| PUT    | 更新资源   | 是   | 否   |
| DELETE | 删除资源   | 是   | 否   |
| PATCH  | 部分更新   | 否   | 否   |
| HEAD   | 获取头信息 | 是   | 是   |

### 3.2 HTTP 状态码

| 范围    | 类别       | 常见码                                                                                 |
| :------ | :--------- | :------------------------------------------------------------------------------------- |
| **1xx** | 信息       | 100 Continue                                                                           |
| **2xx** | 成功       | 200 OK, 201 Created, 204 No Content                                                    |
| **3xx** | 重定向     | 301 永久, 302 临时, 304 未修改                                                         |
| **4xx** | 客户端错误 | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests |
| **5xx** | 服务端错误 | 500 Internal Error, 502 Bad Gateway, 503 Unavailable, 504 Timeout                      |

### 3.3 HTTPS 与 TLS

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: ClientHello（支持的加密套件）
    S-->>C: ServerHello + Certificate（选择的套件 + 证书）
    C->>S: Key Exchange
    S-->>C: Finished
    Note over C,S: 加密通信
```

```bash
# 查看证书信息
openssl s_client -connect example.com:443 -showcerts

# 检查证书过期时间
echo | openssl s_client -connect example.com:443 2>/dev/null | \
  openssl x509 -noout -dates

# 生成自签名证书
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem \
  -days 365 -nodes -subj "/CN=localhost"
```

## 4. 防火墙

### 4.1 iptables

```bash
# 查看规则
iptables -L -n -v
iptables -t nat -L -n

# 允许 SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 允许已建立的连接
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 允许本地回环
iptables -A INPUT -i lo -j ACCEPT

# 允许 HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# 默认拒绝
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 保存规则
iptables-save > /etc/iptables/rules.v4
```

### 4.2 firewalld

```bash
# 基本操作
systemctl start firewalld
systemctl enable firewalld
firewall-cmd --state

# 区域管理
firewall-cmd --get-zones               # 列出区域
firewall-cmd --get-default-zone        # 默认区域
firewall-cmd --set-default-zone=public

# 开放端口
firewall-cmd --add-port=80/tcp --permanent
firewall-cmd --add-service=http --permanent
firewall-cmd --reload

# 查看规则
firewall-cmd --list-all
firewall-cmd --list-ports

# 富规则（精细控制）
firewall-cmd --add-rich-rule='
  rule family="ipv4"
  source address="10.0.0.0/8"
  port port="3306" protocol="tcp"
  accept' --permanent
```

### 4.3 UFW（Ubuntu）

```bash
# 基本操作
ufw enable
ufw status verbose

# 开放端口
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow from 10.0.0.0/8 to any port 3306

# 拒绝
ufw deny 3306/tcp
ufw delete allow 8080/tcp

# 限流（防暴力破解）
ufw limit 22/tcp
```

## 5. SSH 安全

### 5.1 SSH 密钥认证

```bash
# 生成密钥对
ssh-keygen -t ed25519 -C "user@host"
# 或 RSA
ssh-keygen -t rsa -b 4096 -C "user@host"

# 复制公钥到服务器
ssh-copy-id user@server
# 或手动
cat ~/.ssh/id_ed25519.pub | ssh user@server "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# SSH 配置文件
cat ~/.ssh/config
Host myserver
    HostName 192.168.1.100
    User deploy
    Port 22
    IdentityFile ~/.ssh/id_ed25519
    ForwardAgent yes
```

### 5.2 SSH 加固

```bash
# /etc/ssh/sshd_config
Port 2222                          # 修改默认端口
PermitRootLogin no                 # 禁止 root 登录
PasswordAuthentication no          # 禁用密码认证
PubkeyAuthentication yes           # 启用密钥认证
MaxAuthTries 3                     # 最大尝试次数
AllowUsers deploy admin            # 限制允许的用户
ClientAliveInterval 300            # 空闲超时
ClientAliveCountMax 2              # 超时次数
LoginGraceTime 30                  # 登录超时
X11Forwarding no                   # 禁用 X 转发

# 重启 SSH
sudo systemctl restart sshd
```

### 5.3 SSH 隧道

```bash
# 本地端口转发
ssh -L 8080:localhost:80 user@server    # 本地 8080 → 服务器 80

# 远程端口转发
ssh -R 9090:localhost:3000 user@server  # 服务器 9090 → 本地 3000

# 动态端口转发（SOCKS 代理）
ssh -D 1080 user@server

# 跳板机
ssh -J bastion user@internal-server
```

## 6. VPN

### 6.1 WireGuard

```bash
# 安装
sudo apt install wireguard

# 生成密钥
wg genkey | tee privatekey | wg pubkey > publickey

# 服务端配置 /etc/wireguard/wg0.conf
[Interface]
PrivateKey = <server_private_key>
Address = 10.0.0.1/24
ListenPort = 51820
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE

[Peer]
PublicKey = <client_public_key>
AllowedIPs = 10.0.0.2/32

# 客户端配置
[Interface]
PrivateKey = <client_private_key>
Address = 10.0.0.2/24
DNS = 8.8.8.8

[Peer]
PublicKey = <server_public_key>
Endpoint = <server_ip>:51820
AllowedIPs = 0.0.0.0/0  # 全部流量走 VPN
PersistentKeepalive = 25

# 启动
sudo wg-quick up wg0
sudo systemctl enable wg-quick@wg0
```

## 7. 网络故障排查

### 7.1 排查流程

```mermaid
flowchart TD
    T0["物理层 → 数据链路层 → 网络层 → 传输层 → 应用层"]
    T1["curl, telnet"]
    T2["ss, netstat"]
    T3["ping, traceroute, ip route"]
    T4["arp, ethtool"]
    T5["ethtool, mii-tool"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T4 --> T5
```

### 7.2 常用排查命令

```bash
# 连通性
ping -c 4 8.8.8.8                    # ICMP 连通
traceroute example.com               # 路由追踪
mtr -rwzbc 100 example.com          # 持续路由统计

# 端口连通
telnet example.com 443               # TCP 连通
nc -zv example.com 443               # 端口扫描
curl -v https://example.com          # HTTP 测试

# DNS 排查
dig example.com                      # DNS 解析
nslookup example.com                 # DNS 查询

# 路由排查
ip route                             # 路由表
ip route get 8.8.8.8                 # 到目标的路径

# 抓包分析
tcpdump -i eth0 port 80              # 抓 HTTP 包
tcpdump -i eth0 host 10.0.0.1        # 抓特定主机
tcpdump -i eth0 -w capture.pcap      # 保存到文件

# 连接统计
ss -tlnp                             # TCP 监听
ss -s                                # 连接概览
netstat -an | grep :80 | wc -l       # 80 端口连接数
```

### 7.3 常见故障与解决

| 故障现象     | 可能原因          | 排查方法                       |
| :----------- | :---------------- | :----------------------------- |
| 无法 ping 通 | 防火墙/路由       | `iptables -L`, `ip route`      |
| DNS 解析失败 | DNS 配置/服务器   | `dig`, `cat /etc/resolv.conf`  |
| 连接超时     | 防火墙/服务未启动 | `telnet`, `ss -tlnp`           |
| 连接拒绝     | 服务未监听        | `ss -tlnp`, `systemctl status` |
| 连接重置     | 防火墙/应用崩溃   | `tcpdump`, 应用日志            |
| 间歇性超时   | 网络拥塞/MTU      | `mtr`, `ping -M do -s 1472`    |

## 8. 小结

网络与安全是运维的核心能力：

1. **TCP/IP** 是网络通信的基础，理解协议栈有助于定位问题
2. **DNS** 故障是最常见的网络问题，需掌握 dig/nslookup 排查
3. **HTTPS/TLS** 是 Web 安全的基石，需了解证书管理和握手过程
4. **防火墙**配置需遵循最小权限原则，默认拒绝、按需开放
5. **SSH 加固**是服务器安全的第一道防线，必须禁用密码登录
6. **网络排查**遵循从底层到高层的思路，逐步缩小问题范围
## docker network create 创建网络

**基本写法：创建桥接网络**
`docker network create <网络名>`
```bash
# 创建自定义桥接网络
docker network create mynet
```

**基本写法：指定子网创建网络**
`docker network create --subnet <CIDR> <网络名>`
```bash
# 创建指定子网的网络
docker network create --subnet 172.20.0.0/16 mynet
```

**基本写法：创建 overlay 网络**
`docker network create -d overlay <网络名>`
```bash
# 创建跨主机 overlay 网络
docker network create -d overlay myoverlay
```

---

## docker network ls 查看网络

**基本写法：列出所有网络**
`docker network ls`
```bash
# 列出所有 Docker 网络
docker network ls
```

**基本写法：过滤网络**
`docker network ls --filter driver=<驱动>`
```bash
# 只列出桥接网络
docker network ls --filter driver=bridge
```

---

## docker network inspect 查看网络详情

**基本写法：查看网络详情**
`docker network inspect <网络名>`
```bash
# 查看 mynet 网络的详细信息
docker network inspect mynet
```

**基本写法：查看网络中的容器**
`docker network inspect --format '{{range .Containers}}{{.Name}} {{end}}' <网络名>`
```bash
# 列出网络中的所有容器
docker network inspect --format '{{range .Containers}}{{.Name}} {{end}}' mynet
```

---

## docker network connect 连接容器到网络

**基本写法：连接容器到网络**
`docker network connect <网络名> <容器>`
```bash
# 将 web 容器连接到 mynet 网络
docker network connect mynet web
```

**基本写法：指定 IP 连接**
`docker network connect --ip <IP> <网络名> <容器>`
```bash
# 指定 IP 连接容器到网络
docker network connect --ip 172.20.0.5 mynet web
```

**基本写法：使用别名连接**
`docker network connect --alias <别名> <网络名> <容器>`
```bash
# 给容器设置网络别名
docker network connect --alias dbhost mynet web
```

---

## docker network disconnect 断开网络

**基本写法：断开容器与网络连接**
`docker network disconnect <网络名> <容器>`
```bash
# 将 web 容器从 mynet 断开
docker network disconnect mynet web
```

**基本写法：强制断开**
`docker network disconnect -f <网络名> <容器>`
```bash
# 强制断开容器网络
docker network disconnect -f mynet web
```

---

## docker network rm/prune 删除网络

**基本写法：删除网络**
`docker network rm <网络名>`
```bash
# 删除 mynet 网络
docker network rm mynet
```

**基本写法：删除所有未使用网络**
`docker network prune`
```bash
# 清理所有未使用的网络
docker network prune -f
```

---

## 容器使用自定义网络

**基本写法：启动容器时指定网络**
`docker run --network <网络名> <镜像>`
```bash
# 启动容器并加入 mynet 网络
docker run -d --name web --network mynet nginx
```

**基本写法：指定网络别名**
`docker run --network <网络名> --network-alias <别名> <镜像>`
```bash
# 给容器设置网络别名
docker run -d --name app --network mynet --network-alias api node
```

---

## 网络驱动类型

**基本写法：bridge 桥接网络**
`docker network create -d bridge <网络名>`
```bash
# 创建默认桥接网络
docker network create -d bridge mybridge
```

**基本写法：host 主机网络**
`docker run --network host <镜像>`
```bash
# 容器使用主机网络
docker run --network host nginx
```

**基本写法：none 无网络**
`docker run --network none <镜像>`
```bash
# 启动无网络的容器
docker run --network none alpine
```

---

## 端口映射

**基本写法：映射单个端口**
`docker run -p <宿主端口>:<容器端口> <镜像>`
```bash
# 映射 8080 到容器 80
docker run -p 8080:80 nginx
```

**基本写法：映射多个端口**
`docker run -p <端口1>:<端口1> -p <端口2>:<端口2> <镜像>`
```bash
# 映射多个端口
docker run -p 80:80 -p 443:443 nginx
```

**基本写法：绑定指定 IP**
`docker run -p <IP>:<宿主端口>:<容器端口> <镜像>`
```bash
# 绑定到指定 IP
docker run -p 127.0.0.1:8080:80 nginx
```

**基本写法：随机端口映射**
`docker run -P <镜像>`
```bash
# 随机映射到宿主机端口
docker run -P nginx
```

---

## DNS 与服务发现

**基本写法：容器间通过名称访问**
`docker run --name <容器名> --network <网络名> <镜像>`
```bash
# 在同一网络中通过容器名访问
docker run -d --name db --network mynet mysql
docker run -d --name web --network mynet nginx
# web 容器可通过 db 名称访问 mysql
```

**基本写法：自定义 DNS 服务器**
`docker run --dns <DNS服务器> <镜像>`
```bash
# 指定 DNS 服务器
docker run --dns 8.8.8.8 nginx
```

---

## 网络问题排查

**基本写法：查看容器网络配置**
`docker inspect --format '{{.NetworkSettings}}' <容器>`
```bash
# 查看容器网络设置
docker inspect --format '{{json .NetworkSettings.Networks}}' web
```

**基本写法：测试容器间连通性**
`docker exec <容器> ping <目标容器>`
```bash
# 测试 web 到 db 的连通性
docker exec web ping db
```

**基本写法：查看容器端口映射**
`docker port <容器>`
```bash
# 查看 web 容器的端口映射
docker port web
```

<!-- ============ 文档分隔线：031-devops/003-ContainerDocker.md ============ -->

## 1. 容器原理

### 1.1 容器 vs 虚拟机

| 维度         | 虚拟机               | 容器        |
| :----------- | :------------------- | :---------- |
| **隔离级别** | 硬件级（Hypervisor） | 操作系统级  |
| **启动速度** | 分钟级               | 秒级        |
| **资源占用** | GB 级                | MB 级       |
| **镜像大小** | GB 级                | MB 级       |
| **性能**     | 有虚拟化开销         | 接近原生    |
| **密度**     | 几个/主机            | 数百个/主机 |

### 1.2 Linux 容器技术

| 技术          | 作用         | 说明                     |
| :------------ | :----------- | :----------------------- |
| **Namespace** | 资源隔离     | PID/NET/MNT/UTS/IPC/USER |
| **Cgroup**    | 资源限制     | CPU/内存/IO/网络         |
| **UnionFS**   | 镜像分层     | OverlayFS / AUFS         |
| **Seccomp**   | 系统调用过滤 | 限制可用 syscall         |

```bash
# Namespace 示例
unshare --pid --fork --mount-proc bash   # 创建新的 PID namespace
ls /proc                                  # 只能看到新 namespace 的进程

# Cgroup 示例
sudo cgcreate -g cpu,memory:/mycontainer
sudo cgset -r memory.limit_in_bytes=512M mycontainer
sudo cgset -r cpu.cfs_quota_us=50000 mycontainer  # 50% CPU
```

## 2. Docker 架构

### 2.1 核心概念

```mermaid
flowchart LR
    C[Client docker] --> D[Docker Daemon] --> R[Registry Hub/私有]
    D --> I[Image]
    D --> CT[Container]
    D --> N[Network]
```

| 概念          | 描述                             |
| :------------ | :------------------------------- |
| **Image**     | 只读模板，包含运行应用所需的一切 |
| **Container** | Image 的运行实例                 |
| **Volume**    | 数据持久化                       |
| **Network**   | 容器间通信                       |
| **Registry**  | 镜像仓库                         |

### 2.2 基础命令

```bash
# 镜像操作
docker pull nginx:1.25              # 拉取镜像
docker images                       # 列出镜像
docker rmi nginx:1.25               # 删除镜像
docker build -t myapp:v1 .          # 构建镜像
docker tag myapp:v1 registry/myapp:v1  # 打标签
docker push registry/myapp:v1       # 推送镜像

# 容器操作
docker run -d --name web -p 80:80 nginx:1.25    # 运行容器
docker ps                                       # 运行中的容器
docker ps -a                                    # 所有容器
docker stop web                                 # 停止
docker start web                                # 启动
docker restart web                              # 重启
docker rm web                                   # 删除
docker logs -f web                              # 查看日志
docker exec -it web bash                        # 进入容器
docker inspect web                               # 详细信息

# 清理
docker system prune -a              # 清理所有未使用资源
docker volume prune                 # 清理未使用卷
```

## 3. Dockerfile

### 3.1 指令详解

```dockerfile
# 基础镜像
FROM python:3.12-slim

# 元数据
LABEL maintainer="dev@example.com"
LABEL version="1.0"
LABEL description="Python Web Application"

# 设置工作目录
WORKDIR /app

# 环境变量
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# 复制依赖文件并安装（利用缓存）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 非root用户
RUN useradd -m appuser
USER appuser

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 3.2 多阶段构建

```dockerfile
# 阶段1：构建
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 阶段2：运行
FROM nginx:1.25-alpine

# 仅复制构建产物
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**多阶段构建优势**：

- 最终镜像只包含运行时所需文件
- 构建工具和源码不会留在最终镜像
- 镜像大小从 GB 级降到 MB 级

### 3.3 常用基础镜像大小

| 镜像                   | 大小   | 适用场景            |
| :--------------------- | :----- | :------------------ |
| `ubuntu:22.04`         | ~77MB  | 需要完整 Linux 环境 |
| `debian:bookworm-slim` | ~74MB  | 较完整的 Linux      |
| `alpine:3.19`          | ~7MB   | 极致轻量            |
| `python:3.12-slim`     | ~150MB | Python 应用         |
| `python:3.12-alpine`   | ~50MB  | Python 轻量         |
| `node:20-alpine`       | ~180MB | Node.js 应用        |
| `nginx:1.25-alpine`    | ~40MB  | Web 服务器          |

## 4. Docker Compose

### 4.1 完整示例

```yaml
# docker-compose.yml
version: '3.8'

services:
  # Web 应用
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - '8000:8000'
    environment:
      - DATABASE_URL=postgresql://app:secret@db:5432/appdb
      - REDIS_URL=redis://cache:6379/0
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    volumes:
      - ./app:/app # 开发时挂载代码
    networks:
      - frontend
      - backend
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 512M
    restart: unless-stopped
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:8000/health']
      interval: 30s
      timeout: 5s
      retries: 3

  # PostgreSQL 数据库
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: app
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U app -d appdb']
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis 缓存
  cache:
    image: redis:7-alpine
    command: redis-server --maxmemory 256mb --maxmemory-policy allkeys-lru
    networks:
      - backend
    volumes:
      - redisdata:/data

  # Nginx 反向代理
  nginx:
    image: nginx:1.25-alpine
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - web
    networks:
      - frontend
    restart: unless-stopped

volumes:
  pgdata:
    driver: local
  redisdata:
    driver: local

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true # 不暴露到外部
```

### 4.2 Compose 命令

```bash
# 启动
docker compose up -d                    # 后台启动
docker compose up -d --build            # 重新构建并启动

# 管理
docker compose ps                       # 查看状态
docker compose logs -f web              # 查看日志
docker compose exec web bash            # 进入容器
docker compose restart web              # 重启服务

# 扩缩容
docker compose up -d --scale web=3      # 扩展到3个实例

# 停止与清理
docker compose down                     # 停止并删除容器
docker compose down -v                  # 同时删除卷
```

## 5. 镜像优化

### 5.1 优化策略

| 策略               | 效果        | 示例                 |
| :----------------- | :---------- | :------------------- |
| **选择小基础镜像** | 减少 50-80% | alpine 替代 ubuntu   |
| **多阶段构建**     | 减少 60-90% | 分离构建和运行       |
| **合并 RUN 指令**  | 减少层数    | `RUN cmd1 && cmd2`   |
| **清理缓存**       | 减少 20-40% | `--no-cache-dir`     |
| **.dockerignore**  | 减少上下文  | 排除 node_modules 等 |
| **利用缓存**       | 加速构建    | 先 COPY 依赖文件     |

### 5.2 .dockerignore

```dockerignore
# Git
.git
.gitignore

# 依赖
node_modules
__pycache__
*.pyc
.venv

# IDE
.vscode
.idea

# 文档
*.md
docs/

# 测试
tests/
.pytest_cache
.coverage

# Docker
Dockerfile
docker-compose*.yml

# 其他
.env
*.log
.DS_Store
```

### 5.3 优化前后对比

```dockerfile
#  优化前（~800MB）
FROM python:3.12
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

#  优化后（~150MB）
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY . .
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
CMD ["python", "main.py"]
```

## 6. 私有仓库

### 6.1 部署 Registry

```yaml
# docker-compose.yml
services:
  registry:
    image: registry:2
    ports:
      - '5000:5000'
    environment:
      REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY: /data
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: 'Registry Realm'
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
    volumes:
      - ./data:/data
      - ./auth:/auth
    restart: always
```

```bash
# 创建认证文件
mkdir auth
docker run --rm -entrypoint htpasswd httpd:2 -Bbn admin password > auth/htpasswd

# 使用私有仓库
docker tag myapp:v1 localhost:5000/myapp:v1
docker push localhost:5000/myapp:v1
docker pull localhost:5000/myapp:v1
```

### 6.2 Harbor（企业级）

Harbor 提供更完善的私有仓库功能：RBAC、镜像扫描、镜像签名、复制策略。

```bash
# 安装 Harbor
wget https://github.com/goharbor/harbor/releases/download/v2.10.0/harbor-online-installer-v2.10.0.tgz
tar xvf harbor-online-installer-*.tgz
cd harbor
cp harbor.yml.tmpl harbor.yml
# 编辑 harbor.yml 配置
./install.sh --with-trivy  # 包含漏洞扫描
```

## 7. 小结

容器技术是现代运维的基石：

1. **容器原理**基于 Namespace（隔离）和 Cgroup（限制），理解原理有助于排查问题
2. **Dockerfile** 编写需遵循最佳实践：小基础镜像、多阶段构建、利用缓存
3. **Docker Compose** 是单机多容器编排的标准工具，适合开发和测试环境
4. **镜像优化**可大幅减小镜像体积，加速部署和降低存储成本
5. **私有仓库**是企业必需，小型团队用 Registry，大型组织用 Harbor
6. 生产环境建议使用 Kubernetes 进行容器编排
## docker run 创建并启动容器

**基本写法：运行容器**
`docker run [选项] <镜像> [命令]`
```bash
# 启动 nginx 容器
docker run nginx
```

**基本写法：后台运行容器**
`docker run -d <镜像>`
```bash
# 后台运行 nginx 容器
docker run -d nginx
```

**基本写法：交互式运行容器**
`docker run -it <镜像> <命令>`
```bash
# 进入 ubuntu 容器的 bash
docker run -it ubuntu bash
```

**基本写法：命名容器并映射端口**
`docker run --name <名称> -p <宿主端口>:<容器端口> <镜像>`
```bash
# 启动命名为 web 的 nginx，映射 8080 到 80
docker run --name web -p 8080:80 nginx
```

**基本写法：挂载数据卷**
`docker run -v <宿主路径>:<容器路径> <镜像>`
```bash
# 挂载当前目录到容器的 /app
docker run -v $(pwd):/app node
```

---

## docker ps 查看容器

**基本写法：查看运行中容器**
`docker ps`
```bash
# 列出正在运行的容器
docker ps
```

**基本写法：查看所有容器（含已停止）**
`docker ps -a`
```bash
# 列出所有容器
docker ps -a
```

**基本写法：只显示容器 ID**
`docker ps -q`
```bash
# 获取所有运行容器的 ID
docker ps -q
```

---

## docker start/stop/restart 生命周期管理

**基本写法：启动已停止的容器**
`docker start <容器>`
```bash
# 启动容器 web
docker start web
```

**基本写法：停止容器**
`docker stop [选项] <容器>`
```bash
# 优雅停止容器 web
docker stop web
```

**基本写法：强制停止容器**
`docker stop -t 0 <容器>`
```bash
# 立即停止容器
docker stop -t 0 web
```

**基本写法：重启容器**
`docker restart <容器>`
```bash
# 重启容器 web
docker restart web
```

---

## docker rm 删除容器

**基本写法：删除已停止容器**
`docker rm <容器>`
```bash
# 删除容器 web
docker rm web
```

**基本写法：强制删除运行中容器**
`docker rm -f <容器>`
```bash
# 强制删除运行中的容器
docker rm -f web
```

**基本写法：删除所有停止的容器**
`docker container prune`
```bash
# 清理所有停止的容器
docker container prune -f
```

---

## docker exec 进入容器执行命令

**基本写法：进入容器交互式 shell**
`docker exec -it <容器> <shell>`
```bash
# 进入 web 容器的 bash
docker exec -it web bash
```

**基本写法：在容器中执行命令**
`docker exec <容器> <命令>`
```bash
# 查看 web 容器的进程列表
docker exec web ps aux
```

**基本写法：以指定用户执行命令**
`docker exec -u <用户> <容器> <命令>`
```bash
# 以 root 用户进入容器
docker exec -u root -it web sh
```

---

## docker logs 查看日志

**基本写法：查看容器日志**
`docker logs <容器>`
```bash
# 查看 web 容器的全部日志
docker logs web
```

**基本写法：实时跟踪日志**
`docker logs -f <容器>`
```bash
# 实时跟踪 web 容器日志
docker logs -f web
```

**基本写法：查看最后 N 行日志**
`docker logs --tail <行数> <容器>`
```bash
# 查看最后 100 行日志
docker logs --tail 100 web
```

**基本写法：查看指定时间后的日志**
`docker logs --since <时间> <容器>`
```bash
# 查看最近 10 分钟的日志
docker logs --since 10m web
```

---

## docker inspect 查看容器详情

**基本写法：查看容器详细信息**
`docker inspect <容器>`
```bash
# 查看 web 容器的完整信息
docker inspect web
```

**基本写法：查看容器 IP 地址**
`docker inspect --format '{{.NetworkSettings.IPAddress}}' <容器>`
```bash
# 提取容器的 IP 地址
docker inspect --format '{{.NetworkSettings.IPAddress}}' web
```

**基本写法：查看容器状态**
`docker inspect --format '{{.State.Status}}' <容器>`
```bash
# 获取容器当前状态
docker inspect --format '{{.State.Status}}' web
```

---

## docker stats 资源监控

**基本写法：查看所有容器资源使用**
`docker stats`
```bash
# 实时显示所有容器资源占用
docker stats
```

**基本写法：查看指定容器资源使用**
`docker stats <容器>`
```bash
# 监控 web 容器的 CPU 和内存
docker stats web
```

**基本写法：只输出一次结果**
`docker stats --no-stream`
```bash
# 一次性输出所有容器资源使用
docker stats --no-stream
```

---

## docker cp 文件拷贝

**基本写法：从容器拷贝文件到宿主机**
`docker cp <容器>:<容器路径> <宿主路径>`
```bash
# 从 web 容器拷贝配置文件到当前目录
docker cp web:/etc/nginx/nginx.conf ./
```

**基本写法：从宿主机拷贝文件到容器**
`docker cp <宿主路径> <容器>:<容器路径>`
```bash
# 拷贝本地文件到容器
docker cp ./app.conf web:/etc/nginx/conf.d/
```

<!-- ============ 文档分隔线：031-devops/004-Kubernetes.md ============ -->

## 1. Kubernetes 架构

### 1.1 整体架构

```mermaid
flowchart TD
    subgraph CP[Control Plane]
        API[API Server] SCH[Scheduler] CM[Controller Manager]
        ETCD[etcd 集群状态存储]
    end
    N1[Node 1<br/>kubelet Proxy Pods]
    N2[Node 2<br/>kubelet Proxy Pods]
    N3[Node 3<br/>kubelet Proxy Pods]
    NN[Node N<br/>kubelet Proxy Pods]
    CP --> N1
    CP --> N2
    CP --> N3
    CP --> NN
```

### 1.2 核心组件

| 组件                   | 职责                                 |
| :--------------------- | :----------------------------------- |
| **API Server**         | 集群入口，RESTful API                |
| **etcd**               | 分布式 KV 存储，保存集群状态         |
| **Scheduler**          | Pod 调度到 Node                      |
| **Controller Manager** | 控制器（Deployment/ReplicaSet/Node） |
| **kubelet**            | 节点代理，管理 Pod 生命周期          |
| **kube-proxy**         | 网络代理，Service 转发               |

## 2. 核心资源

### 2.1 Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
  labels:
    app: web
    version: v1
spec:
  containers:
    - name: web
      image: nginx:1.25-alpine
      ports:
        - containerPort: 80
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
      env:
        - name: NODE_ENV
          value: 'production'
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
      livenessProbe:
        httpGet:
          path: /health
          port: 80
        initialDelaySeconds: 15
        periodSeconds: 10
      readinessProbe:
        httpGet:
          path: /ready
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 5
      volumeMounts:
        - name: config
          mountPath: /etc/config
          readOnly: true
  volumes:
    - name: config
      configMap:
        name: app-config
  restartPolicy: Always
```

### 2.2 Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: myapp:v2
          ports:
            - containerPort: 8080
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
```

### 2.3 Service

```yaml
# ClusterIP（集群内部访问）
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: ClusterIP
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080

---
# NodePort（节点端口暴露）
apiVersion: v1
kind: Service
metadata:
  name: web-nodeport
spec:
  type: NodePort
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080

---
# LoadBalancer（云厂商负载均衡）
apiVersion: v1
kind: Service
metadata:
  name: web-lb
spec:
  type: LoadBalancer
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080
```

### 2.4 Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: 'true'
    nginx.ingress.kubernetes.io/rate-limit: '100'
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - example.com
      secretName: example-tls
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-service
                port:
                  number: 80
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 80
```

## 3. ConfigMap 与 Secret

### 3.1 ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  # 键值对
  DATABASE_HOST: 'postgres.default.svc.cluster.local'
  DATABASE_PORT: '5432'
  LOG_LEVEL: 'info'
  # 完整配置文件
  nginx.conf: |
    server {
      listen 80;
      location / {
        proxy_pass http://web-service:8080;
      }
    }
```

### 3.2 Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  # Base64 编码
  username: YWRtaW4= # admin
  password: c2VjcmV0MTIz # secret123
stringData:
  # 明文（创建时自动编码）
  api-key: 'my-api-key-12345'
```

```bash
# 创建 Secret
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=secret123

# 从文件创建
kubectl create secret generic tls-secret \
  --from-file=tls.crt=./cert.pem \
  --from-file=tls.key=./key.pem
```

## 4. 自动扩缩容

### 4.1 HPA（水平扩缩容）

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
        - type: Percent
          value: 100
          periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
```

### 4.2 VPA（垂直扩缩容）

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: web-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-deployment
  updatePolicy:
    updateMode: Auto # Off / Initial / Recreate / Auto
  resourcePolicy:
    containerPolicies:
      - containerName: web
        minAllowed:
          cpu: 100m
          memory: 128Mi
        maxAllowed:
          cpu: '2'
          memory: 2Gi
```

## 5. 存储

### 5.1 PV 与 PVC

```yaml
# PersistentVolume
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteMany
  nfs:
    server: nfs-server.default.svc.cluster.local
    path: /data/share

---
# PersistentVolumeClaim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

### 5.2 StorageClass

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
  iopsPerGB: '50'
reclaimPolicy: Retain
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

## 6. 网络策略

```yaml
# 默认拒绝所有入站
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress

---
# 允许特定 Pod 访问
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-api
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - protocol: TCP
          port: 8080
```

## 7. Helm

### 7.1 Chart 结构

```mermaid
flowchart TD
    T0["mychart/"]
    T1["Chart.yaml          # Chart 元数据"]
    T2["values.yaml         # 默认值"]
    T3["templates/"]
    T4["deployment.yaml"]
    T5["service.yaml"]
    T6["ingress.yaml"]
    T7["configmap.yaml"]
    T8["_helpers.tpl    # 模板辅助函数"]
    T9["NOTES.txt       # 安装说明"]
    T10[".helmignore"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T9 --> T10
```

### 7.2 Chart.yaml

```yaml
apiVersion: v2
name: myapp
description: My Application Helm Chart
type: application
version: 1.0.0
appVersion: '2.0.0'
dependencies:
  - name: postgresql
    version: '14.x.x'
    repository: 'https://charts.bitnami.com/bitnami'
    condition: postgresql.enabled
```

### 7.3 values.yaml

```yaml
replicaCount: 3

image:
  repository: myapp
  pullPolicy: IfNotPresent
  tag: '2.0.0'

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: example.com
      paths:
        - path: /
          pathType: Prefix

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi

postgresql:
  enabled: true
  auth:
    database: myapp
    username: app
    password: changeme
```

### 7.4 Helm 命令

```bash
# 仓库管理
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# 安装/升级
helm install myapp ./mychart                    # 本地 Chart
helm install myapp bitnami/nginx                # 仓库 Chart
helm upgrade myapp ./mychart --set replicaCount=5  # 升级
helm upgrade --install myapp ./mychart -f values-prod.yaml  # 安装或升级

# 管理
helm list                                       # 列出发布
helm status myapp                               # 查看状态
helm rollback myapp 1                           # 回滚
helm uninstall myapp                            # 卸载

# 调试
helm template myapp ./mychart                   # 渲染模板
helm lint ./mychart                             # 检查 Chart
helm diff upgrade myapp ./mychart               # 查看变更（需插件）
```

## 8. Operator 模式

### 8.1 Operator 原理

Operator = CRD（自定义资源） + Controller（控制器逻辑），将运维知识编码为软件。

```mermaid
flowchart LR
    O[Operator]
    CRD[CRD 自定义资源] <--> C[Controller 协调循环 Reconcile]
    O --- CRD
    O --- C
```

### 8.2 CRD 定义

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: webapps.apps.example.com
spec:
  group: apps.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 100
                image:
                  type: string
  scope: Namespaced
  names:
    plural: webapps
    singular: webapp
    kind: WebApp
    shortNames:
      - wa
```

### 8.3 常用 Operator

| Operator                | 功能           | 适用场景     |
| :---------------------- | :------------- | :----------- |
| **Prometheus Operator** | 管控监控栈     | 可观测性     |
| **Cert Manager**        | 证书管理       | TLS 自动化   |
| **ArgoCD**              | GitOps 部署    | 持续交付     |
| **MySQL Operator**      | MySQL 集群管理 | 数据库运维   |
| **Kafka Operator**      | Kafka 集群管理 | 消息队列运维 |

## 9. 常用 kubectl 命令

```bash
# 资源查看
kubectl get pods -A                        # 所有命名空间的 Pod
kubectl get pods -o wide                   # 详细信息
kubectl get all -n production              # 命名空间所有资源
kubectl describe pod web-app               # 详细描述
kubectl top pods                           # 资源使用

# 调试
kubectl logs -f web-app                    # 查看日志
kubectl logs web-app -c sidecar            # 指定容器
kubectl exec -it web-app -- bash           # 进入容器
kubectl port-forward svc/web 8080:80       # 端口转发

# 资源管理
kubectl apply -f deployment.yaml           # 应用配置
kubectl delete -f deployment.yaml          # 删除资源
kubectl scale deployment web --replicas=5  # 扩缩容
kubectl rollout restart deployment web     # 重启
kubectl rollout undo deployment web        # 回滚
kubectl rollout status deployment web      # 查看状态

# 上下文管理
kubectl config get-contexts
kubectl config use-context prod-cluster
```

## 10. 小结

Kubernetes 是容器编排的事实标准：

1. **架构**理解 Control Plane 和 Node 组件的职责是排障基础
2. **核心资源**（Pod/Deployment/Service/Ingress）覆盖了大部分应用场景
3. **ConfigMap/Secret** 管理配置和敏感信息，避免硬编码
4. **HPA/VPA** 实现自动扩缩容，应对流量波动
5. **Helm** 是 K8s 应用的包管理器，简化部署和管理
6. **Operator** 将运维知识编码化，适合有状态应用
## Pod 资源定义

**基本写法：定义 Pod**
```yaml
`apiVersion: v1
kind: Pod
metadata:
  name: <名称>
spec:
  containers:
    - name: <容器名>
      image: <镜像>`
```
```yaml
# 定义 nginx Pod
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.25
      ports:
        - containerPort: 80
```

**基本写法：多容器 Pod**
```yaml
`spec:
  containers:
    - name: <容器1>
      image: <镜像1>
    - name: <容器2>
      image: <镜像2>`
```
```yaml
# 定义多容器 Pod
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
spec:
  containers:
    - name: app
      image: myapp:v1
    - name: log-sidecar
      image: busybox
      args: [/bin/sh, -c, "tail -f /log/app.log"]
```

---

## Deployment 资源定义

**基本写法：定义 Deployment**
```yaml
`apiVersion: apps/v1
kind: Deployment
metadata:
  name: <名称>
spec:
  replicas: <副本数>
  selector:
    matchLabels:
      app: <标签>
  template:
    metadata:
      labels:
        app: <标签>
    spec:
      containers:
        - name: <容器名>
          image: <镜像>`
```
```yaml
# 定义 nginx Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
```

---

## Service 资源定义

**基本写法：定义 ClusterIP Service**
```yaml
`apiVersion: v1
kind: Service
metadata:
  name: <名称>
spec:
  selector:
    app: <标签>
  ports:
    - port: <端口>
      targetPort: <目标端口>`
```
```yaml
# 定义 ClusterIP Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
```

**基本写法：定义 NodePort Service**
```yaml
`spec:
  type: NodePort
  ports:
    - port: <端口>
      targetPort: <目标端口>
      nodePort: <节点端口>`
```
```yaml
# 定义 NodePort Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

**基本写法：定义 LoadBalancer Service**
```yaml
`spec:
  type: LoadBalancer
  ports:
    - port: <端口>`
```
```yaml
# 定义 LoadBalancer Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
```

---

## ConfigMap 资源定义

**基本写法：定义 ConfigMap**
```yaml
`apiVersion: v1
kind: ConfigMap
metadata:
  name: <名称>
data:
  <键>: <值>`
```
```yaml
# 定义应用配置 ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  config.yaml: |
    server:
      port: 8080
      host: 0.0.0.0
```

---

## Secret 资源定义

**基本写法：定义 Opaque Secret**
```yaml
`apiVersion: v1
kind: Secret
metadata:
  name: <名称>
type: Opaque
data:
  <键>: <Base64值>`
```
```yaml
# 定义数据库密码 Secret
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=
  password: c2VjcmV0MTIz
```

**基本写法：使用 stringData 明文**
```yaml
`apiVersion: v1
kind: Secret
metadata:
  name: <名称>
type: Opaque
stringData:
  <键>: <明文值>`
```
```yaml
# 使用明文定义 Secret
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  username: admin
  password: secret123
```

---

## Ingress 资源定义

**基本写法：定义 Ingress**
```yaml
`apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <名称>
spec:
  rules:
    - host: <域名>
      http:
        paths:
          - path: <路径>
            pathType: Prefix
            backend:
              service:
                name: <服务名>
                port:
                  number: <端口>`
```
```yaml
# 定义 nginx Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: nginx-svc
                port:
                  number: 80
```

---

## 资源配额与限制

**基本写法：定义资源请求和限制**
```yaml
`spec:
  containers:
    - name: <名称>
      resources:
        requests:
          cpu: <CPU请求>
          memory: <内存请求>
        limits:
          cpu: <CPU限制>
          memory: <内存限制>`
```
```yaml
# 设置容器资源配额
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
```

---

## 健康检查

**基本写法：定义存活探针**
```yaml
`spec:
  containers:
    - name: <名称>
      livenessProbe:
        httpGet:
          path: <路径>
          port: <端口>
        initialDelaySeconds: <秒数>`
```
```yaml
# 定义 HTTP 存活探针
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 30
        periodSeconds: 10
```

**基本写法：定义就绪探针**
```yaml
`spec:
  containers:
    - name: <名称>
      readinessProbe:
        httpGet:
          path: <路径>
          port: <端口>`
```
```yaml
# 定义 HTTP 就绪探针
spec:
  containers:
    - name: app
      image: myapp
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 10
```

---

## 持久化存储

**基本写法：定义 PersistentVolumeClaim**
```yaml
`apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: <名称>
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: <大小>`
```
```yaml
# 定义 10GB 的 PVC
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

**基本写法：在 Pod 中使用 PVC**
```yaml
`spec:
  containers:
    - name: <名称>
      volumeMounts:
        - mountPath: <挂载路径>
          name: <卷名>
  volumes:
    - name: <卷名>
      persistentVolumeClaim:
        claimName: <PVC名称>`
```
```yaml
# 在 Pod 中挂载 PVC
spec:
  containers:
    - name: app
      image: myapp
      volumeMounts:
        - mountPath: /data
          name: data-volume
  volumes:
    - name: data-volume
      persistentVolumeClaim:
        claimName: data-pvc
```

---

## 命名空间

**基本写法：定义 Namespace**
```yaml
`apiVersion: v1
kind: Namespace
metadata:
  name: <名称>`
```
```yaml
# 定义开发环境命名空间
apiVersion: v1
kind: Namespace
metadata:
  name: dev
  labels:
    name: dev
```

**基本写法：定义 ResourceQuota**
```yaml
`apiVersion: v1
kind: ResourceQuota
metadata:
  name: <名称>
  namespace: <命名空间>
spec:
  hard:
    requests.cpu: <CPU总量>
    requests.memory: <内存总量>`
```
```yaml
# 限制命名空间资源配额
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: dev
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
```

<!-- ============ 文档分隔线：031-devops/005-CICDPipeline.md ============ -->

## 1. CI/CD 原理

### 1.1 核心概念

| 概念               | 描述                   | 目标           |
| :----------------- | :--------------------- | :------------- |
| **CI（持续集成）** | 频繁合并代码并自动验证 | 尽早发现问题   |
| **CD（持续交付）** | 自动化部署到预生产环境 | 随时可发布     |
| **CD（持续部署）** | 自动化部署到生产环境   | 每次提交都发布 |

### 1.2 流水线阶段

```
代码提交 → 构建 → 单元测试 → 集成测试 → 安全扫描
    → 制品发布 → 部署预发 → 验收测试 → 部署生产
```

## 2. GitHub Actions

### 2.1 基础配置

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # 代码检查
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  # 单元测试
  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  # 构建镜像
  build:
    runs-on: ubuntu-latest
    needs: test
    if: github.event_name == 'push'
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=
            type=ref,event=branch
            type=semver,pattern={{version}}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # 部署
  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/web web=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:sha-${{ github.sha }}
          kubectl rollout status deployment/web --timeout=300s
```

### 2.2 常用 Action

| Action                        | 用途         |
| :---------------------------- | :----------- |
| `actions/checkout@v4`         | 检出代码     |
| `actions/setup-node@v4`       | 配置 Node.js |
| `actions/setup-python@v5`     | 配置 Python  |
| `docker/build-push-action@v5` | 构建推送镜像 |
| `actions/cache@v4`            | 缓存依赖     |

## 3. GitLab CI

### 3.1 基础配置

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - build
  - deploy

variables:
  DOCKER_REGISTRY: registry.example.com
  APP_IMAGE: $DOCKER_REGISTRY/myapp

# 缓存配置
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

# 代码检查
lint:
  stage: lint
  image: node:20-alpine
  script:
    - npm ci
    - npm run lint
    - npm run typecheck
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 测试
test:
  stage: test
  image: node:20-alpine
  services:
    - postgres:16-alpine
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: postgresql://test:test@postgres:5432/testdb
  script:
    - npm ci
    - npm test -- --coverage
  coverage: '/Statements\s*:\s*(\d+\.?\d*)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# 构建镜像
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - echo $CI_REGISTRY_PASSWORD | docker login -u $CI_REGISTRY_USER --password-stdin $CI_REGISTRY
  script:
    - docker build -t $APP_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $APP_IMAGE:$CI_COMMIT_SHORT_SHA
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# 部署生产
deploy:production:
  stage: deploy
  image: bitnami/kubectl
  script:
    - kubectl config use-context production
    - kubectl set image deployment/web web=$APP_IMAGE:$CI_COMMIT_SHORT_SHA
    - kubectl rollout status deployment/web --timeout=300s
  environment:
    name: production
    url: https://example.com
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  when: manual
```

## 4. Jenkins

### 4.1 Jenkinsfile

```groovy
// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    environment {
        REGISTRY = 'registry.example.com'
        IMAGE = "${REGISTRY}/myapp"
        TAG = "${env.BUILD_NUMBER}"
    }

    tools {
        nodejs 'Node20'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Lint') {
            steps {
                sh 'npm run lint'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test -- --coverage'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                    publishHTML(target: [
                        reportDir: 'coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage'
                    ])
                }
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE}:${TAG} ."
                sh "docker push ${IMAGE}:${TAG}"
            }
        }

        stage('Deploy') {
            steps {
                input 'Deploy to production?'
                sh "kubectl set image deployment/web web=${IMAGE}:${TAG}"
                sh 'kubectl rollout status deployment/web --timeout=300s'
            }
        }
    }

    post {
        success {
            slackSend(color: 'good', message: "Build ${TAG} deployed successfully!")
        }
        failure {
            slackSend(color: 'danger', message: "Build ${TAG} failed!")
        }
        always {
            cleanWs()
        }
    }
}
```

## 5. ArgoCD

### 5.1 GitOps 模式

```mermaid
flowchart LR
    D[开发者] -->|push| G[Git 仓库]
    A[ArgoCD] <-->|sync| G
    A -->|apply| K[Kubernetes]
```

### 5.2 ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/myapp-manifests.git
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - ServerSideApply=true
    retry:
      limit: 3
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

## 6. 发布策略

### 6.1 蓝绿发布

```mermaid
flowchart LR
    B1[Blue v1 当前版本<br/>← 流量] G1[Green v2 新版本<br/>无流量]
    B2[Blue v1 旧版本<br/>无流量] G2[Green v2 当前版本<br/>← 流量]
    B1 -->|切换流量| G2
```

```yaml
# 蓝绿发布 - ArgoCD + Service 切换
apiVersion: v1
kind: Service
metadata:
  name: web-active
spec:
  selector:
    app: web
    version: green # 切换时修改 blue/green
  ports:
    - port: 80
      targetPort: 8080
```

### 6.2 金丝雀发布

```yaml
# 使用 Argo Rollouts
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: web-rollout
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 10 # 10% 流量到新版本
        - pause: { duration: 5m }
        - setWeight: 30 # 30% 流量
        - pause: { duration: 5m }
        - setWeight: 60 # 60% 流量
        - pause: { duration: 5m }
        - setWeight: 100 # 全量
      canaryService: web-canary
      stableService: web-stable
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: myapp:v2
```

### 6.3 发布策略对比

| 策略         | 回滚速度 | 风险 | 资源消耗  | 复杂度 |
| :----------- | :------- | :--- | :-------- | :----- |
| **滚动更新** | 中       | 中   | 低        | 低     |
| **蓝绿发布** | 快       | 低   | 高（2倍） | 中     |
| **金丝雀**   | 快       | 低   | 中        | 高     |
| **A/B 测试** | 快       | 低   | 高        | 高     |

## 7. 制品管理

### 7.1 制品仓库

| 仓库                  | 类型   | 特点                       |
| :-------------------- | :----- | :------------------------- |
| **Nexus**             | 通用   | 支持 Docker/NPM/Maven/PyPI |
| **Harbor**            | Docker | 企业级、漏洞扫描           |
| **JFrog Artifactory** | 通用   | 功能最全、商业产品         |
| **GitHub Packages**   | 通用   | 与 GitHub 集成             |

### 7.2 镜像标签策略

| 标签            | 用途      | 示例           |
| :-------------- | :-------- | :------------- |
| `latest`        | 最新版本  | 不推荐生产使用 |
| `sha-xxxxxx`    | Git SHA   | 精确追溯       |
| `v1.2.3`        | 语义版本  | 正式发布       |
| `main-20260614` | 分支+日期 | 持续部署       |

## 8. 流水线设计原则

### 8.1 最佳实践

| 原则           | 描述                              |
| :------------- | :-------------------------------- |
| **快速反馈**   | Lint 和单元测试先行，快速发现问题 |
| **并行执行**   | 独立任务并行运行，缩短总时间      |
| **缓存优化**   | 缓存依赖和构建产物                |
| **安全扫描**   | 集成 SAST/DAST/SCA                |
| **制品不可变** | 一次构建，多处部署                |
| **环境一致**   | 开发/测试/生产使用相同镜像        |
| **最小权限**   | CI/CD 凭证按需授权                |

### 8.2 流水线安全

```yaml
# GitHub Actions 安全实践
jobs:
  build:
    permissions:
      contents: read # 只读代码
      packages: write # 写入包
    steps:
      # 使用 OIDC 而非长期密钥
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-actions
          aws-region: us-east-1

      # 审计第三方 Action
      - uses: actions/checkout@v4 # 使用特定版本，不用 main
```

## 9. 小结

CI/CD 是 DevOps 的核心实践：

1. **GitHub Actions** 适合开源项目和 GitHub 生态
2. **GitLab CI** 适合自托管和完整 DevOps 平台
3. **Jenkins** 适合复杂的企业级流水线
4. **ArgoCD** 实现 GitOps，声明式管理 K8s 部署
5. **金丝雀发布**是生产环境推荐策略，渐进式降低风险
6. 流水线设计需关注**快速反馈、安全扫描和制品不可变性**
## GitLab CI/CD

**基本用法:配置文件结构**
`.gitlab-ci.yml`

```yaml
# .gitlab-ci.yml GitLab CI 基础配置
stages:
  - build
  - test
  - deploy

variables:
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:24.0
  services:
  - docker:24.0-dind
  script:
  - docker build -t $IMAGE .
  - docker push $IMAGE
  only:
  - main

test:
  stage: test
  image: node:20
  script:
  - npm ci
  - npm test
  artifacts:
    reports:
      junit: test-results.xml

deploy:
  stage: deploy
  script:
  - kubectl apply -f k8s/
  only:
  - main
  when: manual
```

---

**基本用法:常用命令**
`gitlab-runner exec|register|verify`

```bash
# 注册 Runner
gitlab-runner register \
  --url https://gitlab.com \
  --token $RUNNER_TOKEN \
  --executor docker \
  --docker-image alpine:latest

# 列出已注册 Runner
gitlab-runner list

# 验证 Runner 连接
gitlab-runner verify

# 启动 Runner
gitlab-runner run

# 手动触发本地 job(测试用)
gitlab-runner exec docker build
```

---

**基本用法:条件与规则**
`rules / only / except`

```yaml
# rules 现代条件控制
build:
  stage: build
  script: make build
  rules:
  - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    when: never
  - if: $CI_COMMIT_BRANCH == "main"
    changes:
    - src/**
    - Dockerfile
  - if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/

# only/except 传统写法
deploy:
  script: deploy.sh
  only:
  - main
  - tags
  except:
  - branches
```

---

**基本用法:artifacts 与 cache**
`artifacts / cache`

```yaml
build:
  script: make build
  artifacts:
    paths:
    - bin/
    - dist/
    expire_in: 1 week
    reports:
      dotenv: build.env
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

test:
  script: npm test
  cache:
    key:
      files:
      - package-lock.json
    paths:
    - node_modules/
    policy: pull-push
```

---

## GitHub Actions

**基本用法:Workflow 配置**
`.github/workflows/ci.yml`

```yaml
# .github/workflows/ci.yml GitHub Actions 基础
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'
    - run: npm ci
    - run: npm test
    - run: npm run build
```

---

**基本用法:常用 actions**
`uses: <动作>@<版本>`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        cache: maven

    - uses: docker/setup-buildx-action@v3
    - uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    - uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

---

**基本用法:环境变量与密钥**
`env / secrets`

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      APP_ENV: production
      REGISTRY: ghcr.io
    steps:
    - uses: actions/checkout@v4
    - name: Deploy
      env:
        KUBE_CONFIG: ${{ secrets.KUBE_CONFIG }}
        DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
      run: |
        echo "$KUBE_CONFIG" | base64 -d > kubeconfig
        kubectl --kubeconfig kubeconfig apply -f k8s/

    - uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
```

---

**基本用法:矩阵构建**
`strategy.matrix`

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: ['18', '20', '22']
        exclude:
        - os: windows-latest
          node-version: '18'
        include:
        - os: ubuntu-latest
          node-version: '20'
          coverage: true
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm ci
    - run: npm test
```

---

## Jenkins Pipeline

**基本用法:声明式 Pipeline**
`Jenkinsfile`

```groovy
// Jenkinsfile 声明式 Pipeline
pipeline {
    agent any
    environment {
        IMAGE = "registry.example.com/myapp:${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS = credentials('docker-registry')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
            post {
                always {
                    junit 'test-results.xml'
                    publishHTML([
                        reportDir: 'coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker push $IMAGE'
                sh 'kubectl apply -f k8s/'
            }
        }
    }
    post {
        success {
            slackSend channel: '#deploy', message: "Build ${env.BUILD_NUMBER} succeeded"
        }
        failure {
            slackSend channel: '#alerts', message: "Build ${env.BUILD_NUMBER} failed"
        }
    }
}
```

---

**基本用法:脚本式 Pipeline**
`node { stage('...') { ... } }`

```groovy
// 脚本式 Pipeline
node('docker') {
    stage('Checkout') {
        git 'https://github.com/org/repo.git'
    }

    stage('Build') {
        def image = docker.build('myapp:latest')
        image.inside {
            sh 'make build'
        }
    }

    stage('Test') {
        try {
            sh 'make test'
        } catch (Exception e) {
            currentBuild.result = 'UNSTABLE'
            emailext subject: 'Tests failed',
                     body: 'Tests failed in build ${BUILD_NUMBER}',
                     to: 'team@example.com'
        }
    }

    stage('Deploy') {
        if (env.BRANCH_NAME == 'main') {
            sh 'make deploy'
        } else {
            echo "Skip deploy for branch ${env.BRANCH_NAME}"
        }
    }
}
```

---

**基本用法:Jenkins CLI**
`java -jar jenkins-cli.jar`

```bash
# 下载 CLI jar
wget http://jenkins:8080/jnlpJars/jenkins-cli.jar

# 列出 jobs
java -jar jenkins-cli.jar -s http://jenkins:8080 list-jobs

# 触发构建
java -jar jenkins-cli.jar -s http://jenkins:8080 build my-app

# 触发构建(带参数)
java -jar jenkins-cli.jar -s http://jenkins:8080 build my-app -p BRANCH=develop

# 查看构建日志
java -jar jenkins-cli.jar -s http://jenkins:8080 console my-app 123

# 重新加载配置
java -jar jenkins-cli.jar -s http://jenkins:8080 reload-configuration
```

---

## 通用工具命令

**基本用法:Docker 构建**
`docker build [选项] <上下文>`

```bash
# 基本构建
docker build -t myapp:latest .

# 指定 Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# 构建并打多标签
docker build -t myapp:latest -t myapp:v1.0 .

# 使用构建参数
docker build --build-arg VERSION=1.0 -t myapp:1.0 .

# 使用 BuildKit
DOCKER_BUILDKIT=1 docker build -t myapp:latest .

# 构建后扫描漏洞
docker build -t myapp:latest .
docker scout cves myapp:latest
```

---

**基本用法:镜像推送**
`docker push <镜像>`

```bash
# 登录仓库
docker login registry.example.com -u user -p pass

# 推送镜像
docker push myapp:latest

# 推送所有标签
docker push --all-tags myapp

# 推送后签名(cosign)
cosign sign --key cosign.key myapp:latest

# 推送多平台镜像
docker buildx build --platform linux/amd64,linux/arm64 \
  -t myapp:latest --push .
```

---

**基本用法:Kubernetes 部署**
`kubectl apply -f <清单>`

```bash
# 部署 YAML 清单
kubectl apply -f k8s/deployment.yaml -n production

# 部署整个目录
kubectl apply -f k8s/ -n production

# 从 Kustomize 部署
kubectl apply -k k8s/overlays/production

# 滚动重启
kubectl rollout restart deployment web -n production

# 等待部署完成
kubectl rollout status deployment web -n production --timeout=5m
```

---

## Helm 部署

**基本用法:CI/CD 中使用 Helm**
`helm upgrade --install <release> <chart>`

```bash
# 部署/升级 Helm Chart
helm upgrade --install myapp ./chart \
  -f values-production.yaml \
  --namespace production --create-namespace \
  --wait --timeout 5m

# 使用原子部署(失败自动回滚)
helm upgrade --install myapp ./chart \
  -f values-production.yaml \
  --namespace production \
  --atomic --wait

# 查看部署差异
helm diff upgrade myapp ./chart -f values-production.yaml

# 部署前 dry-run
helm upgrade --install myapp ./chart \
  -f values-production.yaml \
  --dry-run --debug
```

---

## 制品仓库管理

**基本用法:Nexus 制品仓库**
`curl -u <用户>:<密码> <仓库>/...`

```bash
# 上传 Docker 镜像
docker push nexus.example.com:8082/myapp:v1

# 上传 Maven 制品
curl -u admin:pass --upload-file target/app-1.0.jar \
  "http://nexus:8081/repository/maven-releases/com/example/app/1.0/app-1.0.jar"

# 上传 npm 包
npm publish --registry http://nexus:8081/repository/npm-private/

# 上传 PyPI 包
twine upload --repository-url http://nexus:8081/repository/pypi-hosted/ \
  dist/*.whl -u admin -p pass
```

---

**基本用法:JFrog Artifactory**
`jfrog rt upload|download`

```bash
# 上传制品
jfrog rt upload target/app.jar maven-releases/com/example/app/1.0/

# 下载制品
jfrog rt download maven-releases/com/example/app/1.0/app.jar

# 推送 Docker 镜像
docker push artifactory.example.com/docker/myapp:v1

# 提升制品(晋升)
jfrog rt move maven-snapshots maven-releases \
  --props="version=1.0.0"
```

---

## 通知与集成

**基本用法:Slack 通知**
`curl -X POST <webhook-url> -d '<json>'`

```bash
# 发送 Slack 通知
curl -X POST -H 'Content-Type: application/json' \
  https://hooks.slack.com/services/xxx \
  -d '{
    "text": "Build '"$CI_PIPELINE_ID"' succeeded",
    "channel": "#deploy",
    "attachments": [{
      "color": "good",
      "fields": [
        {"title": "Repository", "value": "'"$CI_PROJECT_NAME"'"},
        {"title": "Branch", "value": "'"$CI_COMMIT_BRANCH"'"}
      ]
    }]
  }'
```

---

**基本用法:钉钉/企业微信通知**
`curl -X POST <webhook-url>`

```bash
# 钉钉机器人通知
curl -X POST 'https://oapi.dingtalk.com/robot/send?access_token=xxx' \
  -H 'Content-Type: application/json' \
  -d '{
    "msgtype": "markdown",
    "markdown": {
      "title": "构建通知",
      "text": "## 构建成功\n项目: '"$CI_PROJECT_NAME"'\n分支: '"$CI_COMMIT_BRANCH"'\n[查看详情]('"$CI_PIPELINE_URL"')"
    }
  }'

# 企业微信通知
curl -X POST 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx' \
  -H 'Content-Type: application/json' \
  -d '{
    "msgtype": "markdown",
    "markdown": {
      "content": "## 构建成功\n> 项目: '"$CI_PROJECT_NAME"'\n> 分支: '"$CI_COMMIT_BRANCH"'"
    }
  }'
```

---

## 安全扫描

**基本用法:Trivy 漏洞扫描**
`trivy image <镜像>`

```bash
# 扫描镜像漏洞
trivy image myapp:latest

# 扫描指定严重级别
trivy image --severity HIGH,CRITICAL myapp:latest

# 输出 JSON 格式
trivy image --format json --output report.json myapp:latest

# 扫描文件系统
trivy fs --security-checks vuln,config .

# 扫描代码仓库
trivy repo https://github.com/org/repo
```

---

**基本用法:其他扫描工具**
`<工具> <参数>`

```bash
# Grype 漏洞扫描
grype myapp:latest

# Snyk 漏洞扫描
snyk container test myapp:latest

# Hadolint Dockerfile lint
hadolint Dockerfile

# kubeval 校验 K8s 清单
kubeval k8s/*.yaml

# conftest 策略检查
conftest test k8s/deployment.yaml -p policies/
```

---

## 缓存与优化

**基本用法:Docker 缓存**
`--cache-from / --cache-to`

```bash
# GitHub Actions 中使用缓存
docker buildx build \
  --cache-from type=gha \
  --cache-to type=gha,mode=max \
  -t myapp:latest .

# GitLab CI 中使用 registry 缓存
docker build \
  --cache-from $CI_REGISTRY_IMAGE:cache \
  -t $CI_REGISTRY_IMAGE:cache \
  -t $CI_REGISTRY_IMAGE:latest .

# 使用 BuildKit 缓存挂载
DOCKER_BUILDKIT=1 docker build \
  --build-arg BUILDKIT_CACHE_MOUNT_NS=app \
  -t myapp:latest .
```

---

**基本用法:依赖缓存**
`cache: <配置>`

```yaml
# GitLab CI npm 缓存
test:
  cache:
    key:
      files:
      - package-lock.json
    paths:
    - node_modules/
    - .npm/
  script:
  - npm ci --cache .npm --prefer-offline

# GitHub Actions 缓存
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'
- run: npm ci

# Maven 缓存
- uses: actions/cache@v4
  with:
    path: ~/.m2/repository
    key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
    restore-keys: ${{ runner.os }}-maven-
```

---

## 排查与调试

**基本用法:本地测试 Pipeline**
`act / gitlab-runner exec`

```bash
# 使用 act 本地运行 GitHub Actions
act -j build

# 指定 event
act push -j build

# 详细输出
act -j build -v

# GitLab Runner 本地执行
gitlab-runner exec docker build

# 重新运行失败的 job
gitlab-runner exec docker --docker-privileged build
```

---

**基本用法:查看构建日志**
`<CI-CLI> logs <job>`

```bash
# GitLab 查看 job 日志
glab ci trace <job-id>

# GitHub Actions 日志
gh run view <run-id> --log

# Jenkins 构建日志
java -jar jenkins-cli.jar console my-app 123

# 实时跟踪日志
gh run watch <run-id>
```

---

**基本用法:排查构建失败**
`<检查步骤>`

```bash
# 进入 CI 容器调试
docker run -it --rm node:20 sh

# 重新运行 job 并保留容器
gitlab-runner exec docker build --docker-keep-cache

# 检查 CI 环境变量
env | grep -E 'CI_|GITHUB_'

# 检查 Docker 守护进程
docker info
docker system df

# 查看构建产物大小
du -sh target/ dist/
```

<!-- ============ 文档分隔线：031-devops/006-MonitorAndObservability.md ============ -->

## 1. 可观测性三大支柱

| 支柱                | 描述               | 工具          | 回答的问题       |
| :------------------ | :----------------- | :------------ | :--------------- |
| **指标（Metrics）** | 数值型时间序列数据 | Prometheus    | 系统发生了什么？ |
| **日志（Logs）**    | 离散的事件记录     | ELK/Loki      | 为什么发生？     |
| **链路（Traces）**  | 请求的完整调用链   | Jaeger/Zipkin | 问题在哪里？     |

```
指标（发现异常）→ 链路（定位问题）→ 日志（分析原因）
```

## 2. Prometheus + Grafana

### 2.1 Prometheus 架构

```mermaid
flowchart LR
    T[Targets 应用/节点] -->|pull| P[Prometheus Server]
    P -->|query| G[Grafana 可视化]
    P --> A[AlertManager]
    P --> TS[TSDB 存储]
    P --> SD[SD 服务发现]
```

### 2.2 Prometheus 配置

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  # 应用监控
  - job_name: 'myapp'
    metrics_path: /metrics
    static_configs:
      - targets: ['app:8080']
    # Kubernetes 服务发现
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true

  # Node Exporter
  - job_name: 'node'
    static_configs:
      - targets: ['node-exporter:9100']

  # Blackbox Exporter（探针）
  - job_name: 'blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]
    static_configs:
      - targets:
          - https://example.com
          - https://api.example.com/health

# 告警规则
rule_files:
  - 'alerts/*.yml'

# Alertmanager
alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']
```

### 2.3 应用暴露指标

```python
# Python 应用暴露 Prometheus 指标
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import FastAPI, Response

app = FastAPI()

# 计数器
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

# 直方图（延迟分布）
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0]
)

# 仪表盘（当前值）
ACTIVE_CONNECTIONS = Gauge(
    'active_connections',
    'Current active connections'
)

@app.get("/api/users")
async def get_users():
    REQUEST_COUNT.labels(method='GET', endpoint='/api/users', status='200').inc()
    with REQUEST_LATENCY.labels(method='GET', endpoint='/api/users').time():
        # 业务逻辑
        return {"users": []}

@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type="text/plain")
```

### 2.4 PromQL 常用查询

```promql
# HTTP 请求速率（每秒）
rate(http_requests_total[5m])

# 按 endpoint 分组的请求速率
sum(rate(http_requests_total[5m])) by (endpoint)

# P95 延迟
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# 错误率
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))

# CPU 使用率
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 内存使用率
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# 磁盘使用率
(1 - (node_filesystem_avail_bytes{fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes)) * 100
```

### 2.5 告警规则

```yaml
# alerts/app.yml
groups:
  - name: app_alerts
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m]))
          /
          sum(rate(http_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: 'High error rate on {{ $labels.job }}'
          description: 'Error rate is {{ $value | humanizePercentage }}'

      - alert: HighLatency
        expr: |
          histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
        for: 10m
        labels:
          severity: warning
        annotations:
          summary: 'High P95 latency on {{ $labels.endpoint }}'

      - alert: PodCrashLooping
        expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
        for: 5m
        labels:
          severity: critical
```

### 2.6 Alertmanager 配置

```yaml
# alertmanager.yml
global:
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alerts@example.com'

route:
  group_by: ['alertname', 'cluster']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'slack-notifications'
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty'
      repeat_interval: 15m

receivers:
  - name: 'slack-notifications'
    slack_configs:
      - api_url: 'https://hooks.slack.com/services/xxx'
        channel: '#alerts'

  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: '<service-key>'

inhibit_rules:
  - source_match:
      severity: critical
    target_match:
      severity: warning
    equal: ['alertname', 'cluster']
```

## 3. 日志系统

### 3.1 ELK Stack

```
应用 → Filebeat → Logstash → Elasticsearch → Kibana
```

```yaml
# Filebeat 配置
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/app/*.log
    fields:
      app: myapp
      env: production
    json.keys_under_root: true

output.logstash:
  hosts: ['logstash:5044']
```

### 3.2 Loki（轻量级日志）

```yaml
# Promtail 配置
server:
  http_listen_port: 9080

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: app
    static_configs:
      - targets:
          - localhost
        labels:
          job: app
          __path__: /var/log/app/*.log
    pipeline_stages:
      - json:
          expressions:
            level: level
            message: message
            timestamp: timestamp
      - labels:
          level:
      - timestamp:
          source: timestamp
          format: RFC3339
```

### 3.3 日志最佳实践

```python
# 结构化日志
import structlog

logger = structlog.get_logger()

# 结构化输出
logger.info("request_processed",
    method="GET",
    path="/api/users",
    status=200,
    duration_ms=45,
    user_id="u123")

# 输出:
# {"event":"request_processed","method":"GET","path":"/api/users","status":200,"duration_ms":45,"user_id":"u123","timestamp":"2026-06-14T10:00:00Z"}
```

| 实践           | 描述                        |
| :------------- | :-------------------------- |
| **结构化日志** | 使用 JSON 格式，便于检索    |
| **关联 ID**    | 每个请求分配唯一 trace_id   |
| **日志级别**   | DEBUG/INFO/WARN/ERROR/FATAL |
| **敏感信息**   | 脱敏处理密码、Token         |
| **日志轮转**   | 避免磁盘写满                |

## 4. 链路追踪

### 4.1 OpenTelemetry

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

# 配置
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://otel-collector:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# 自动埋点
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

# 手动埋点
tracer = trace.get_tracer(__name__)

@app.get("/api/users/{user_id}")
async def get_user(user_id: str):
    with tracer.start_as_current_span("get_user") as span:
        span.set_attribute("user.id", user_id)
        user = fetch_user(user_id)
        span.set_attribute("user.name", user.name)
        return user
```

### 4.2 Jaeger 部署

```yaml
# docker-compose.yml
services:
  jaeger:
    image: jaegertracing/all-in-one:1.54
    environment:
      COLLECTOR_OTLP_ENABLED: true
    ports:
      - '16686:16686' # Jaeger UI
      - '4317:4317' # OTLP gRPC
      - '4318:4318' # OTLP HTTP
```

## 5. SLO/SLI/SLA

### 5.1 概念

| 概念    | 描述                     | 示例                   |
| :------ | :----------------------- | :--------------------- |
| **SLA** | 服务等级协议（合同）     | 99.9% 可用性，否则退款 |
| **SLO** | 服务等级目标（内部目标） | 99.95% 可用性          |
| **SLI** | 服务等级指标（测量值）   | 实际可用性 99.97%      |

### 5.2 错误预算

```
错误预算 = 1 - SLO
月度错误预算（秒）= 30天 × 86400秒 × (1 - SLO)

SLO 99.9% → 月度错误预算 = 43.2 分钟
SLO 99.95% → 月度错误预算 = 21.6 分钟
SLO 99.99% → 月度错误预算 = 4.32 分钟
```

### 5.3 SLO 定义示例

```yaml
# Sloth (SLO 生成器) 配置
version: prometheus/v1
service: myapp
slos:
  - name: 'api-availability'
    objective: 99.9
    description: 'API 服务可用性 SLO'
    sli:
      events:
        error_query: sum(rate(http_requests_total{status=~"5.."}[{{.window}}]))
        total_query: sum(rate(http_requests_total[{{.window}}]))
    alerting:
      name: ApiAvailabilityAlert
      labels:
        team: backend
      page_alert:
        labels:
          severity: critical
      ticket_alert:
        labels:
          severity: warning

  - name: 'api-latency'
    objective: 99.0
    description: 'API P99 延迟 < 500ms'
    sli:
      events:
        error_query: |
          sum(rate(http_request_duration_seconds_bucket{le="0.5"}[{{.window}}]))
          /
          sum(rate(http_request_duration_seconds_count[{{.window}}]))
        total_query: '1'
```

## 6. Grafana Dashboard

### 6.1 关键 Dashboard

| Dashboard      | 核心指标                      |
| :------------- | :---------------------------- |
| **系统概览**   | CPU、内存、磁盘、网络         |
| **应用性能**   | QPS、延迟 P50/P95/P99、错误率 |
| **Kubernetes** | Pod 状态、资源使用、重启次数  |
| **数据库**     | 连接数、查询延迟、慢查询      |
| **业务指标**   | 用户活跃、订单量、转化率      |

### 6.2 Dashboard 即代码

```json
// 使用 Grafana Terraform Provider
resource "grafana_dashboard" "app_dashboard" {
  config_json = jsonencode({
    dashboard = {
      title = "Application Overview"
      panels = [
        {
          title = "Request Rate"
          type  = "timeseries"
          targets = [{
            expr = "sum(rate(http_requests_total[5m])) by (endpoint)"
          }]
        },
        {
          title = "Error Rate"
          type  = "stat"
          targets = [{
            expr = "sum(rate(http_requests_total{status=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m]))"
          }]
          thresholds = {
            steps = [
              { value = null, color = "green" },
              { value = 0.01, color = "yellow" },
              { value = 0.05, color = "red" }
            ]
          }
        }
      ]
    }
  })
}
```

## 7. 小结

可观测性是运维的"眼睛"：

1. **三大支柱**（指标/日志/链路）缺一不可，组合使用效果最佳
2. **Prometheus + Grafana** 是监控的事实标准，PromQL 是核心技能
3. **Loki** 比 ELK 更轻量，适合与 Prometheus 生态集成
4. **OpenTelemetry** 是可观测性的未来，统一了指标/日志/链路的采集
5. **SLO/SLI/SLA** 量化服务质量，错误预算指导发布决策
6. Dashboard 即代码，避免手动配置的不可重复性

<!-- ============ 文档分隔线：031-devops/007-IaC.md ============ -->

## 1. IaC 理念

### 1.1 核心原则

| 原则         | 描述                       |
| :----------- | :------------------------- |
| **声明式**   | 描述期望状态，而非操作步骤 |
| **版本控制** | 所有配置纳入 Git 管理      |
| **幂等性**   | 多次执行结果一致           |
| **不可变**   | 替换而非修改基础设施       |
| **自助服务** | 代码即文档，可重复执行     |

### 1.2 IaC 工具分类

| 类型         | 代表工具               | 特点                 |
| :----------- | :--------------------- | :------------------- |
| **配置管理** | Ansible, Chef, Puppet  | 管理已有服务器的配置 |
| **资源编排** | Terraform, Pulumi, CDK | 创建和管理云资源     |
| **容器编排** | Helm, Kustomize        | 管理 K8s 应用        |
| **GitOps**   | ArgoCD, Flux           | Git 驱动的持续部署   |

## 2. Terraform

### 2.1 核心概念

| 概念         | 描述                               |
| :----------- | :--------------------------------- |
| **Provider** | 云厂商插件（AWS/Azure/GCP/阿里云） |
| **Resource** | 基础设施资源（VM/VPC/数据库）      |
| **Module**   | 可复用的配置包                     |
| **State**    | 资源状态文件                       |
| **Plan**     | 预览变更                           |
| **Apply**    | 执行变更                           |

### 2.2 基础配置

```hcl
# provider.tf
terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # 远程状态存储
  backend "s3" {
    bucket         = "terraform-state-prod"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = "us-east-1"
}
```

### 2.3 资源定义

```hcl
# vpc.tf
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "${var.project}-vpc"
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_subnet" "public" {
  count                   = length(var.public_subnet_cidrs)
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.azs[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.project}-public-${count.index + 1}"
  }
}

resource "aws_subnet" "private" {
  count             = length(var.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.azs[count.index]

  tags = {
    Name = "${var.project}-private-${count.index + 1}"
  }
}

# variables.tf
variable "project" {
  description = "Project name"
  type        = string
  default     = "myapp"
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "public_subnet_cidrs" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "private_subnet_cidrs" {
  type    = list(string)
  default = ["10.0.10.0/24", "10.0.20.0/24", "10.0.30.0/24"]
}
```

### 2.4 EKS 集群

```hcl
# eks.tf
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "${var.project}-${var.environment}"
  cluster_version = "1.29"

  vpc_id     = aws_vpc.main.id
  subnet_ids = aws_subnet.private[*].id

  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = true

  cluster_addons = {
    coredns    = {}
    kube-proxy = {}
    vpc-cni    = {}
  }

  eks_managed_node_groups = {
    general = {
      min_size       = 2
      max_size       = 10
      desired_size   = 3
      instance_types = ["t3.medium"]

      labels = {
        role = "general"
      }
    }
    monitoring = {
      min_size       = 1
      max_size       = 3
      desired_size   = 1
      instance_types = ["t3.small"]

      labels = {
        role = "monitoring"
      }
      taints = [{
        key    = "dedicated"
        value  = "monitoring"
        effect = "NO_SCHEDULE"
      }]
    }
  }
}
```

### 2.5 状态管理

```bash
# 状态操作
terraform state list                    # 列出资源
terraform state show aws_vpc.main       # 查看资源详情
terraform state mv aws_vpc.old aws_vpc.new  # 重命名
terraform state rm aws_vpc.orphan       # 移除（不删除实际资源）

# 导入已有资源
terraform import aws_vpc.main vpc-12345678

# 工作区（环境隔离）
terraform workspace new staging
terraform workspace select production
terraform workspace list
```

### 2.6 模块化

```mermaid
flowchart TD
    T0["modules/"]
    T1["vpc/"]
    T2["main.tf"]
    T3["variables.tf"]
    T4["outputs.tf"]
    T5["versions.tf"]
    T6["eks/"]
    T7["main.tf"]
    T8["variables.tf"]
    T9["outputs.tf"]
    T10["rds/"]
    T11["main.tf"]
    T12["variables.tf"]
    T13["outputs.tf"]
    T14["environments/"]
    T15["production/"]
    T16["main.tf       # 引用模块"]
    T17["backend.tf"]
    T18["terraform.tfvars"]
    T19["staging/"]
    T20["main.tf"]
    T21["backend.tf"]
    T22["terraform.tfvars"]
    T0 --> T1
    T5 --> T6
    T9 --> T10
    T10 --> T11
    T10 --> T12
    T10 --> T13
    T13 --> T14
    T14 --> T15
    T18 --> T19
    T19 --> T20
    T19 --> T21
    T19 --> T22
```

```hcl
# environments/production/main.tf
module "vpc" {
  source = "../../modules/vpc"

  project     = var.project
  environment = "production"
  cidr_block  = "10.0.0.0/16"
}

module "eks" {
  source = "../../modules/eks"

  project     = var.project
  environment = "production"
  vpc_id      = module.vpc.vpc_id
  subnet_ids  = module.vpc.private_subnet_ids
}
```

## 3. Ansible

### 3.1 Inventory

```ini
# inventory/production.ini
[web]
web1 ansible_host=10.0.1.10
web2 ansible_host=10.0.1.11

[db]
db1 ansible_host=10.0.10.20

[monitoring]
prometheus ansible_host=10.0.20.10
grafana ansible_host=10.0.20.11

[production:children]
web
db
monitoring

[production:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/deploy_key
```

### 3.2 Playbook

```yaml
# playbooks/deploy-web.yml
- name: Deploy Web Application
  hosts: web
  become: true
  vars:
    app_version: '2.0.0'
    app_port: 8080

  tasks:
    - name: Ensure app directory exists
      file:
        path: /opt/myapp
        state: directory
        owner: appuser
        group: appgroup

    - name: Pull Docker image
      community.docker.docker_image:
        name: 'registry.example.com/myapp:{{ app_version }}'
        source: pull

    - name: Run application container
      community.docker.docker_container:
        name: myapp
        image: 'registry.example.com/myapp:{{ app_version }}'
        state: started
        restart_policy: unless-stopped
        ports:
          - '{{ app_port }}:8080'
        env:
          NODE_ENV: production
          DATABASE_URL: '{{ vault_database_url }}'
        volumes:
          - /opt/myapp/data:/app/data

    - name: Wait for application to be ready
      uri:
        url: 'http://localhost:{{ app_port }}/health'
        status_code: 200
      register: result
      until: result is success
      retries: 10
      delay: 5

    - name: Notify deployment
      slack:
        token: '{{ vault_slack_token }}'
        msg: 'Deployed myapp {{ app_version }} to {{ inventory_hostname }}'
      delegate_to: localhost
      run_once: true
```

### 3.3 Role 结构

```mermaid
flowchart TD
    T0["roles/nginx/"]
    T1["tasks/"]
    T2["main.yml"]
    T3["handlers/"]
    T4["main.yml"]
    T5["templates/"]
    T6["nginx.conf.j2"]
    T7["files/"]
    T8["ssl/"]
    T9["defaults/"]
    T10["main.yml"]
    T11["vars/"]
    T12["main.yml"]
    T13["meta/"]
    T14["main.yml"]
    T0 --> T1
    T2 --> T3
    T4 --> T5
    T6 --> T7
    T8 --> T9
    T10 --> T11
    T12 --> T13
    T13 --> T14
```

```yaml
# roles/nginx/tasks/main.yml
- name: Install Nginx
  apt:
    name: nginx
    state: present
    update_cache: true

- name: Configure Nginx
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    owner: root
    group: root
    mode: '0644'
  notify: Reload Nginx

- name: Ensure Nginx is running
  service:
    name: nginx
    state: started
    enabled: true

# roles/nginx/handlers/main.yml
- name: Reload Nginx
  service:
    name: nginx
    state: reloaded
```

## 4. Pulumi

### 4.1 Pulumi vs Terraform

| 维度         | Terraform | Pulumi                  |
| :----------- | :-------- | :---------------------- |
| **语言**     | HCL       | Python/TypeScript/Go/C# |
| **学习曲线** | 需学 HCL  | 用已有编程语言          |
| **测试**     | 有限      | 原生单元测试            |
| **逻辑**     | 声明式    | 命令式 + 声明式         |
| **状态**     | 自管理    | Pulumi Cloud 或自管理   |

### 4.2 Pulumi 示例

```python
# __main__.py
import pulumi
import pulumi_aws as aws

# 配置
config = pulumi.Config()
environment = config.require("environment")

# VPC
vpc = aws.ec2.Vpc("main-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    tags={"Name": f"myapp-{environment}-vpc"}
)

# 子网
for i, az in enumerate(["us-east-1a", "us-east-1b"]):
    aws.ec2.Subnet(f"subnet-{i}",
        vpc_id=vpc.id,
        cidr_block=f"10.0.{i+1}.0/24",
        availability_zone=az,
        tags={"Name": f"myapp-{environment}-subnet-{i}"}
    )

# EKS 集群
cluster = aws.eks.Cluster("my-cluster",
    role_arn=cluster_role.arn,
    vpc_config=aws.eks.ClusterVpcConfigArgs(
        subnet_ids=[s.id for s in subnets]
    ),
    version="1.29"
)

# 输出
pulumi.export("cluster_name", cluster.name)
pulumi.export("cluster_endpoint", cluster.endpoint)
```

## 5. GitOps

### 5.1 GitOps 原则

| 原则         | 描述                   |
| :----------- | :--------------------- |
| **声明式**   | 系统描述必须是声明式的 |
| **版本控制** | 期望状态存储在 Git     |
| **自动拉取** | 自动从 Git 拉取并应用  |
| **持续协调** | 软件代理持续协调状态   |

### 5.2 Flux

```yaml
# flux-system/gotk-sync.yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: flux-system
  namespace: flux-system
spec:
  interval: 1m
  ref:
    branch: main
  url: https://github.com/org/myapp-manifests

---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: flux-system
  namespace: flux-system
spec:
  interval: 10m
  path: ./clusters/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-system
  validation: server
```

### 5.3 Kustomize

```mermaid
flowchart TD
    T0["base/"]
    T1["deployment.yaml"]
    T2["service.yaml"]
    T3["kustomization.yaml"]
    T4["overlays/"]
    T5["staging/"]
    T6["kustomization.yaml"]
    T7["patch-replicas.yaml"]
    T8["production/"]
    T9["kustomization.yaml"]
    T10["patch-replicas.yaml"]
    T11["patch-resources.yaml"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T3 --> T4
    T4 --> T5
    T7 --> T8
    T8 --> T9
    T8 --> T10
    T8 --> T11
```

```yaml
# base/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - deployment.yaml
  - service.yaml

# overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
patches:
  - path: patch-replicas.yaml
  - path: patch-resources.yaml

# overlays/production/patch-replicas.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 5
```

## 6. IaC 安全

### 6.1 安全实践

| 实践              | 描述                        |
| :---------------- | :-------------------------- |
| **状态加密**      | 加密远程状态存储            |
| **密钥管理**      | 使用 Vault/云 KMS，不硬编码 |
| **PR 审查**       | 所有变更需 Code Review      |
| **Plan 审查**     | 审查 terraform plan 输出    |
| **最小权限**      | CI/CD 使用最小必要权限      |
| ** drifted 检测** | 定期检测配置漂移            |

### 6.2 Terraform 安全扫描

```bash
# tfsec - Terraform 安全扫描
tfsec .

# checkov - 策略扫描
checkov -d .

# terrascan - 合规扫描
terrascan scan -t aws

# 在 CI 中集成
- name: Security Scan
  run: |
    tfsec --soft-fail .
    checkov -d . --framework terraform
```

## 7. 小结

IaC 是现代运维的基础：

1. **Terraform** 是多云资源编排的事实标准，HCL 语法简洁
2. **Ansible** 适合配置管理和应用部署，无需 Agent
3. **Pulumi** 用编程语言写 IaC，适合有编程背景的团队
4. **GitOps** 是 K8s 部署的最佳实践，ArgoCD 和 Flux 是主流工具
5. **状态管理**是 Terraform 的关键，必须使用远程后端和锁
6. **安全扫描**应集成到 CI/CD，防止不安全配置上线

<!-- ============ 文档分隔线：031-devops/008-CloudNativeSRE.md ============ -->

## 1. 云原生架构

### 1.1 CNCF 云原生定义

云原生技术使组织能够在公有云、私有云和混合云等现代动态环境中构建和运行可扩展的应用。核心要素：

| 要素               | 描述                     |
| :----------------- | :----------------------- |
| **微服务**         | 应用拆分为独立部署的服务 |
| **容器**           | 应用打包和运行的标准     |
| **服务网格**       | 服务间通信的基础设施层   |
| **不可变基础设施** | 替换而非修改             |
| **声明式 API**     | 描述期望状态             |

### 1.2 CNCF 技术栈

```mermaid
flowchart TD
    App[应用层<br/>微服务 / Serverless / 函数计算] --> R[运行时层<br/>Kubernetes / Container Runtime]
    R --> I[基础设施层<br/>云平台 / 存储 / 网络 / 安全]
    I --> O[可观测性<br/>Prometheus / Grafana / OpenTelemetry]
    O --> CD[CI/CD<br/>ArgoCD / Flux / Tekton]
```

## 2. 12-Factor App

### 2.1 十二因素

| #   | 因素               | 描述                       | 示例                           |
| :-- | :----------------- | :------------------------- | :----------------------------- |
| 1   | **代码库**         | 单一代码库，多次部署       | Git 仓库                       |
| 2   | **依赖**           | 显式声明并隔离依赖         | package.json, requirements.txt |
| 3   | **配置**           | 在环境中存储配置           | 环境变量、ConfigMap            |
| 4   | **后端服务**       | 把后端服务当作附加资源     | 数据库、缓存、消息队列         |
| 5   | **构建/发布/运行** | 严格分离构建和运行         | CI/CD 流水线                   |
| 6   | **进程**           | 无状态进程                 | 会话存 Redis                   |
| 7   | **端口绑定**       | 通过端口绑定提供服务       | Web 服务器自包含               |
| 8   | **并发**           | 通过进程模型扩展           | 水平扩展 Pod                   |
| 9   | **易处理**         | 快速启动和优雅终止         | 健康检查、信号处理             |
| 10  | **开发/生产一致**  | 尽可能保持环境一致         | 相同 Docker 镜像               |
| 11  | **日志**           | 将日志视为事件流           | stdout → 日志收集器            |
| 12  | **管理进程**       | 一次性管理进程与应用同环境 | K8s Job/CronJob                |

### 2.2 配置管理示例

```python
#  硬编码配置
DATABASE_URL = "postgresql://admin:password@db:5432/prod"

#  环境变量配置
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    secret_key: str
    debug: bool = False
    max_workers: int = 4

    class Config:
        env_file = ".env"

settings = Settings()
```

## 3. 微服务治理

### 3.1 微服务通信模式

| 模式          | 描述             | 优点       | 缺点           |
| :------------ | :--------------- | :--------- | :------------- |
| **同步 REST** | HTTP 请求/响应   | 简单直观   | 耦合、级联故障 |
| **同步 gRPC** | Protocol Buffers | 高性能     | 需要定义 proto |
| **异步消息**  | 消息队列         | 解耦、削峰 | 复杂性增加     |
| **事件驱动**  | 事件总线         | 最终一致性 | 调试困难       |

### 3.2 服务发现与负载均衡

```yaml
# Kubernetes Service（内置服务发现）
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
    - port: 80
      targetPort: 8080

# 应用内通过 DNS 访问
# http://user-service.default.svc.cluster.local
```

### 3.3 熔断与限流

```python
# 熔断器模式
from circuitbreaker import circuit

@circuit(failure_threshold=5, recovery_timeout=30)
def call_external_service():
    response = requests.get("http://external-service/api")
    return response.json()

# 限流
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)

@app.get("/api/data")
@limiter.limit("100/minute")
async def get_data(request: Request):
    return {"data": "value"}
```

## 4. 服务网格（Istio）

### 4.1 Istio 架构

```mermaid
flowchart TD
    CP[Control Plane<br/>istiod Pilot + Citadel + Galley]
    S1[Service A<br/>Envoy Sidecar<br/>App]
    S2[Service B<br/>Envoy Sidecar<br/>App]
    CP -->|配置下发| S1
    CP -->|配置下发| S2
    S1 <--> S2
```

### 4.2 流量管理

```yaml
# 虚拟服务 - 金丝雀路由
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: web-service
spec:
  hosts:
    - web-service
  http:
    - match:
        - headers:
            x-canary:
              exact: 'true'
      route:
        - destination:
            host: web-service
            subset: canary
    - route:
        - destination:
            host: web-service
            subset: stable
          weight: 90
        - destination:
            host: web-service
            subset: canary
          weight: 10

---
# 目标规则
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: web-service
spec:
  host: web-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: DEFAULT
        http1MaxPendingRequests: 100
        http2MaxRequests: 100
  subsets:
    - name: stable
      labels:
        version: v1
    - name: canary
      labels:
        version: v2
```

### 4.3 可观测性

```yaml
# Telemetry 配置
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: default
spec:
  accessLogging:
    - providers:
        - name: otel
  tracing:
    - providers:
        - name: otel
      randomSamplingPercentage: 10
  metrics:
    - providers:
        - name: prometheus
```

## 5. 混沌工程

### 5.1 混沌工程原则

| 原则         | 描述                       |
| :----------- | :------------------------- |
| **定义稳态** | 建立系统的正常行为基线     |
| **假设稳态** | 假设控制组和实验组行为一致 |
| **引入故障** | 模拟真实世界的故障         |
| **观察差异** | 对比稳态假设和实际结果     |

### 5.2 Chaos Mesh

```yaml
# Pod 故障注入
apiVersion: chaos-mesh.org/v1delta1
kind: PodChaos
metadata:
  name: pod-kill
  namespace: chaos-testing
spec:
  action: pod-kill
  mode: one
  selector:
    namespaces:
      - production
    labelSelectors:
      app: web
  scheduler:
    cron: '@every 30m'

---
# 网络延迟
apiVersion: chaos-mesh.org/v1delta1
kind: NetworkChaos
metadata:
  name: network-delay
spec:
  action: delay
  mode: all
  selector:
    namespaces:
      - production
    labelSelectors:
      app: api
  delay:
    latency: '100ms'
    correlation: '25'
    jitter: '50ms'
  duration: '5m'

---
# CPU 压力
apiVersion: chaos-mesh.org/v1delta1
kind: StressChaos
metadata:
  name: cpu-stress
spec:
  mode: one
  selector:
    labelSelectors:
      app: web
  stressors:
    cpu:
      workers: 2
      load: 80
  duration: '3m'
```

### 5.3 混沌实验流程

```
1. 定义稳态指标 → 2. 设计故障场景 → 3. 在测试环境执行
    → 4. 观察系统行为 → 5. 记录发现 → 6. 修复问题
    → 7. 逐步在生产环境执行
```

## 6. 容量规划

### 6.1 容量指标

| 指标           | 描述           | 计算方法     |
| :------------- | :------------- | :----------- |
| **QPS**        | 每秒请求数     | 监控统计     |
| **资源利用率** | CPU/内存使用率 | Prometheus   |
| **增长趋势**   | 流量增长预测   | 历史数据拟合 |
| **峰值倍数**   | 峰值/均值      | 监控统计     |

### 6.2 容量计算

```
所需 Pod 数 = (目标 QPS × 安全系数) / 单 Pod QPS
所需 Node 数 = (所需 Pod 数 + 缓冲) / 单 Node Pod 数

示例:
- 目标 QPS: 10,000
- 安全系数: 1.5
- 单 Pod QPS: 500
- 缓冲: 20%

所需 Pod = (10000 × 1.5) / 500 = 30
所需 Node = (30 × 1.2) / 10 = 4
```

## 7. 故障复盘

### 7.1 复盘模板

```markdown
# 故障复盘报告

## 基本信息

- **故障时间**: 2026-06-14 14:30 - 15:15 (45分钟)
- **影响范围**: 用户服务 API 不可用
- **影响程度**: 30% 用户受影响
- **SLO 违规**: 是 (可用性低于 99.9%)

## 时间线

- 14:30 - 告警触发：API 错误率上升
- 14:32 - 值班确认：数据库连接池耗尽
- 14:35 - 尝试扩容数据库
- 14:45 - 扩容完成，服务恢复
- 15:00 - 确认所有服务正常
- 15:15 - 告警解除

## 根因分析（5-Why）

1. 为什么 API 不可用？→ 数据库连接池耗尽
2. 为什么连接池耗尽？→ 慢查询阻塞连接
3. 为什么有慢查询？→ 缺少索引的全表扫描
4. 为什么缺少索引？→ 新功能上线未添加索引
5. 为什么未添加索引？→ 缺少数据库迁移审查流程

## 改进措施

| 行动项             | 负责人    | 截止日期 | 优先级 |
| :----------------- | :-------- | :------- | :----- |
| 添加缺失索引       | DBA       | 06-15    | P0     |
| 数据库迁移审查流程 | Tech Lead | 06-20    | P1     |
| 连接池监控告警     | SRE       | 06-18    | P1     |
| 慢查询自动检测     | SRE       | 06-25    | P2     |
```

### 7.2 复盘原则

| 原则         | 描述                       |
| :----------- | :------------------------- |
| **无指责**   | 关注系统和流程，不追究个人 |
| **数据驱动** | 用数据和事实说话           |
| **可执行**   | 改进措施必须具体、可执行   |
| **跟踪**     | 行动项必须有人跟进         |

## 8. On-Call 实践

### 8.1 On-Call 轮值

```yaml
# PagerDuty / OpsGenie 配置
schedules:
  - name: primary-oncall
    rotation: weekly
    members: [sre1, sre2, sre3, sre4]
    handoff_time: '09:00'
    timezone: 'Asia/Shanghai'

  - name: secondary-oncall
    rotation: weekly
    members: [dev1, dev2, dev3, dev4]

escalation_policies:
  - name: critical-alert
    rules:
      - target: primary-oncall
        delay: 5m
      - target: secondary-oncall
        delay: 15m
      - target: engineering-manager
        delay: 30m
```

### 8.2 On-Call 最佳实践

| 实践         | 描述                     |
| :----------- | :----------------------- |
| **轮值公平** | 轮值分配均衡，避免疲劳   |
| **升级机制** | 明确升级路径和超时       |
| **告警降噪** | 减少无效告警，提高信噪比 |
| **Runbook**  | 每个告警有对应的处理手册 |
| **复盘改进** | 每次值班后复盘改进       |
| **补偿机制** | 值班补偿或调休           |

### 8.3 Runbook 模板

```markdown
# 告警: HighErrorRate

## 告警条件

API 5xx 错误率 > 5%，持续 5 分钟

## 快速诊断

1. 检查最近部署: `kubectl rollout history deployment/web`
2. 查看错误日志: `kubectl logs -l app=web --since=10m | grep 500`
3. 检查依赖服务: `kubectl get pods -A | grep -v Running`

## 常见原因与处理

| 原因         | 处理方法                                                |
| :----------- | :------------------------------------------------------ |
| 新版本 Bug   | 回滚: `kubectl rollout undo deployment/web`             |
| 数据库超载   | 扩容: `kubectl scale statefulset/postgres --replicas=3` |
| 下游服务故障 | 熔断: 修改 VirtualService 路由                          |

## 升级

- 联系后端负责人: @backend-oncall
- 联系 DBA: @dba-oncall
```

## 9. 小结

云原生与 SRE 是现代运维的高级实践：

1. **12-Factor App** 是云原生应用的设计原则，配置外置和无状态是核心
2. **服务网格**（Istio）将流量管理、安全和可观测性下沉到基础设施层
3. **混沌工程**主动发现系统弱点，是提高可靠性的有效手段
4. **故障复盘**遵循无指责原则，关注系统和流程改进
5. **On-Call** 需要完善的轮值、升级和 Runbook 机制
6. **容量规划**基于数据预测，避免资源不足或浪费

<!-- ============ 文档分隔线：031-devops/009-ShellScriptProgramming.md ============ -->

## 1. Bash 基础语法

### 1.1 变量

```bash
# 变量赋值（等号两边不能有空格）
name="hello"
echo $name
echo ${name}

# 只读变量
readonly PI=3.14

# 环境变量
export MY_VAR="value"

# 特殊变量
$0    # 脚本名
$1~$9 # 位置参数
$#    # 参数个数
$@    # 所有参数（作为独立字符串）
$*    # 所有参数（作为单个字符串）
$?    # 上一个命令的退出码
$$    # 当前进程PID
```

### 1.2 字符串操作

```bash
str="Hello World"

# 字符串长度
echo ${#str}          # 11

# 子字符串
echo ${str:0:5}       # Hello
echo ${str:6}         # World

# 替换
echo ${str/World/Bash}    # Hello Bash（首次替换）
echo ${str//l/L}          # HeLLo WorLd（全局替换）

# 删除
echo ${str#Hello }        # World（从前删最短匹配）
echo ${str##*o}           # rld（从前删最长匹配）
echo ${str%World}         # Hello（从后删最短匹配）
echo ${str%%*o}           # Hell（从后删最长匹配）

# 默认值
echo ${undefined:-default}  # default
echo ${undefined:=default}  # default（同时赋值）
```

### 1.3 数组

```bash
# 定义数组
arr=(1 2 3 4 5)
arr[0]=10

# 访问
echo ${arr[0]}        # 10
echo ${arr[@]}        # 所有元素
echo ${#arr[@]}       # 元素个数
echo ${#arr[0]}       # 第一个元素的长度

# 遍历
for i in "${arr[@]}"; do
    echo $i
done

# 关联数组
declare -A map
map[name]="Alice"
map[age]=30
echo ${map[name]}
```

## 2. 流程控制

### 2.1 条件判断

```bash
# if-elif-else
if [ -f "/etc/passwd" ]; then
    echo "文件存在"
elif [ -d "/etc" ]; then
    echo "目录存在"
else
    echo "不存在"
fi

# 双括号（支持 &&, ||, <, >）
if [[ $a -gt $b && $a -lt 100 ]]; then
    echo "条件满足"
fi

# case
case $1 in
    start)   echo "启动服务" ;;
    stop)    echo "停止服务" ;;
    restart) echo "重启服务" ;;
    *)       echo "用法: $0 {start|stop|restart}" ;;
esac
```

### 2.2 文件测试操作符

| 操作符 | 含义           |
| ------ | -------------- |
| `-f`   | 是否为普通文件 |
| `-d`   | 是否为目录     |
| `-e`   | 是否存在       |
| `-r`   | 是否可读       |
| `-w`   | 是否可写       |
| `-x`   | 是否可执行     |
| `-s`   | 是否非空       |

### 2.3 循环

```bash
# for 循环
for i in {1..10}; do
    echo $i
done

for i in $(seq 1 2 20); do  # 步长2
    echo $i
done

# C 风格 for
for ((i=0; i<10; i++)); do
    echo $i
done

# while 循环
while read line; do
    echo "$line"
done < input.txt

# until 循环
until [ $count -gt 10 ]; do
    count=$((count + 1))
done
```

## 3. 函数

```bash
# 定义函数
greet() {
    local name=$1
    echo "Hello, $name"
    return 0
}

# 调用
greet "World"

# 返回值
get_status() {
    if systemctl is-active nginx > /dev/null; then
        echo "running"
    else
        echo "stopped"
    fi
}

status=$(get_status)
echo "Nginx status: $status"
```

## 4. 文本处理三剑客

### 4.1 grep

```bash
# 基本搜索
grep "pattern" file.txt

# 常用选项
grep -i "pattern" file     # 忽略大小写
grep -r "pattern" dir/     # 递归搜索
grep -n "pattern" file     # 显示行号
grep -c "pattern" file     # 统计匹配行数
grep -v "pattern" file     # 反向匹配
grep -E "pat1|pat2" file   # 扩展正则

# 实用正则
grep -E "^[0-9]+" file           # 以数字开头
grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" file  # 邮箱
```

### 4.2 sed

```bash
# 替换
sed 's/old/new/' file           # 替换每行第一个
sed 's/old/new/g' file          # 全局替换
sed -i 's/old/new/g' file       # 原地修改

# 删除
sed '/^$/d' file                # 删除空行
sed '1,5d' file                 # 删除1-5行

# 插入和追加
sed '3i\inserted line' file     # 第3行前插入
sed '3a\appended line' file     # 第3行后追加

# 多命令
sed -e 's/a/A/g' -e 's/b/B/g' file
```

### 4.3 awk

```bash
# 基本用法
awk '{print $1, $3}' file       # 打印第1、3列
awk -F: '{print $1}' /etc/passwd  # 指定分隔符

# 条件
awk '$3 > 100 {print $1, $3}' file

# BEGIN/END
awk 'BEGIN{sum=0} {sum+=$1} END{print "Total:", sum}' file

# 内置变量
# NR: 行号  NF: 字段数  FS: 字段分隔符
awk '{print NR, NF, $0}' file

# 格式化输出
awk '{printf "%-10s %5d\n", $1, $2}' file
```

## 5. 实用脚本示例

### 5.1 系统监控脚本

```bash
#!/bin/bash
# 系统资源监控

THRESHOLD=80

check_cpu() {
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d. -f1)
    if [ "$cpu_usage" -gt "$THRESHOLD" ]; then
        echo "WARNING: CPU usage ${cpu_usage}%"
    fi
}

check_memory() {
    local mem_usage=$(free | grep Mem | awk '{printf("%.0f", $3/$2*100)}')
    if [ "$mem_usage" -gt "$THRESHOLD" ]; then
        echo "WARNING: Memory usage ${mem_usage}%"
    fi
}

check_disk() {
    local disk_usage=$(df -h / | tail -1 | awk '{print $5}' | tr -d '%')
    if [ "$disk_usage" -gt "$THRESHOLD" ]; then
        echo "WARNING: Disk usage ${disk_usage}%"
    fi
}

check_cpu
check_memory
check_disk
```

### 5.2 日志分析脚本

```bash
#!/bin/bash
# Nginx 日志分析

LOG_FILE="/var/log/nginx/access.log"

echo "=== 访问量 Top 10 IP ==="
awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -10

echo "=== 状态码统计 ==="
awk '{print $9}' "$LOG_FILE" | sort | uniq -c | sort -rn

echo "=== 访问量 Top 10 URL ==="
awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -rn | head -10

echo "=== 每小时访问量 ==="
awk '{print $4}' "$LOG_FILE" | cut -d: -f2 | sort | uniq -c | sort -n
```

### 5.3 自动备份脚本

```bash
#!/bin/bash
# 数据库自动备份

BACKUP_DIR="/backup/mysql"
DATE=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=7

# 创建备份目录
mkdir -p "$BACKUP_DIR"

# 备份所有数据库
mysqldump -u root -p"$MYSQL_PASS" --all-databases | gzip > "${BACKUP_DIR}/all_${DATE}.sql.gz"

# 清理过期备份
find "$BACKUP_DIR" -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete

echo "Backup completed: all_${DATE}.sql.gz"
```

## 6. 调试与最佳实践

### 6.1 调试技巧

```bash
# 调试模式
bash -x script.sh       # 打印每条命令
bash -n script.sh       # 语法检查

# 在脚本中启用
set -x    # 开启调试
set +x    # 关闭调试

# 严格模式
set -euo pipefail
# -e: 命令失败时退出
# -u: 使用未定义变量时报错
# -o pipefail: 管道中任一命令失败则整个管道失败
```

### 6.2 最佳实践

- 使用 `shellcheck` 检查脚本
- 变量引用加双引号：`"$var"`
- 使用 `local` 声明局部变量
- 使用 `[[ ]]` 替代 `[ ]`
- 使用 `$()` 替代反引号
- 总是处理错误返回值
- 使用 `mktemp` 创建临时文件

<!-- ============ 文档分隔线：031-devops/010-PackageManagementRepository.md ============ -->

## 1. RPM 包管理

### 1.1 RPM 基础

RPM（Red Hat Package Manager）是 Red Hat 系列的包管理格式。

```bash
# 安装
rpm -ivh package.rpm      # 安装并显示进度
rpm -Uvh package.rpm      # 升级安装
rpm -Fvh package.rpm      # 仅升级（已安装才升级）

# 查询
rpm -qa                   # 列出所有已安装包
rpm -qi package           # 查看包信息
rpm -ql package           # 列出包文件
rpm -qf /path/file        # 查询文件所属包
rpm -qR package           # 查看依赖

# 卸载
rpm -e package            # 卸载包
rpm -e --nodeps package   # 忽略依赖卸载

# 验证
rpm -V package            # 验证包完整性
rpm --import RPM-GPG-KEY  # 导入GPG密钥
```

### 1.2 RPM 包结构

```
package-name-version-release.architecture.rpm
例: nginx-1.24.0-1.el9.x86_64.rpm

名称: nginx
版本: 1.24.0
发行号: 1.el9
架构: x86_64
```

RPM 包内部结构：

```mermaid
flowchart TD
    T0["HEADER（元数据）"]
    T1["名称、版本、描述"]
    T2["依赖关系"]
    T3["安装/卸载脚本"]
    T4["文件列表和校验和"]
    T5["PAYLOAD（cpio 归档 + gzip）"]
    T6["实际文件"]
    T4 --> T5
    T5 --> T6
```

### 1.3 SPEC 文件

构建 RPM 包的核心配置文件：

```spec
Name:           myapp
Version:        1.0.0
Release:        1%{?dist}
Summary:        My Application

License:        MIT
URL:            https://example.com
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc, make
Requires:       openssl >= 1.1

%description
My application description.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/myapp
%{_mandir}/man1/myapp.1*

%changelog
* Sat Jun 14 2026 fanquanpp <fanquanpp@example.com> - 1.0.0-1
- Initial package
```

## 2. DEB 包管理

### 2.1 dpkg 基础

```bash
# 安装
dpkg -i package.deb       # 安装
dpkg -r package           # 卸载（保留配置）
dpkg -P package           # 完全卸载

# 查询
dpkg -l                   # 列出所有已安装包
dpkg -l package           # 查看包状态
dpkg -L package           # 列出包文件
dpkg -S /path/file        # 查询文件所属包
dpkg -s package           # 查看包详细信息
```

### 2.2 DEB 包结构

```mermaid
flowchart TD
    T0["package.deb"]
    T1["debian-binary        # 版本信息"]
    T2["control.tar.gz       # 控制信息"]
    T3["control          # 包元数据"]
    T4["preinst          # 安装前脚本"]
    T5["postinst         # 安装后脚本"]
    T6["prerm            # 卸载前脚本"]
    T7["postrm           # 卸载后脚本"]
    T8["data.tar.gz          # 实际文件"]
    T0 --> T1
    T0 --> T2
    T7 --> T8
```

**control 文件**：

```
Package: myapp
Version: 1.0.0
Architecture: amd64
Maintainer: fanquanpp <fanquanpp@example.com>
Description: My Application
 My application description.
Depends: libc6 (>= 2.31), libssl3
```

## 3. YUM/DNF 仓库

### 3.1 YUM/DNF 基础

```bash
# 安装
dnf install package
dnf install package-1.0.0   # 指定版本

# 更新
dnf update                  # 更新所有
dnf update package          # 更新指定包

# 查询
dnf search keyword          # 搜索包
dnf info package            # 查看包信息
dnf list installed          # 列出已安装包
dnf list available          # 列出可用包

# 依赖
dnf deplist package         # 查看依赖
dnf repoquery --requires package  # 查询依赖

# 清理
dnf clean all               # 清理缓存
dnf autoremove              # 删除不需要的依赖
```

### 3.2 配置仓库

```ini
# /etc/yum.repos.d/myrepo.repo
[myrepo]
name=My Custom Repository
baseurl=https://repo.example.com/centos/$releasever/$basearch/
enabled=1
gpgcheck=1
gpgkey=https://repo.example.com/RPM-GPG-KEY
priority=1
```

### 3.3 创建本地仓库

```bash
# 安装工具
dnf install createrepo

# 创建仓库
mkdir -p /repo/rpms
cp *.rpm /repo/rpms/
createrepo /repo/rpms/

# 更新仓库
createrepo --update /repo/rpms/
```

## 4. APT 仓库

### 4.1 APT 基础

```bash
# 安装
apt install package
apt install package=1.0.0    # 指定版本

# 更新
apt update                   # 更新索引
apt upgrade                  # 升级所有
apt full-upgrade             # 完整升级（可删除包）

# 查询
apt search keyword
apt show package
apt list --installed
apt depends package

# 清理
apt autoremove
apt clean
```

### 4.2 配置源

```bash
# /etc/apt/sources.list
deb https://mirrors.aliyun.com/ubuntu/ jammy main restricted
deb https://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted
deb https://mirrors.aliyun.com/ubuntu/ jammy-security main restricted
```

格式：`deb URL distribution component`

### 4.3 创建 APT 仓库

```bash
# 安装工具
apt install dpkg-dev

# 创建仓库
mkdir -p /repo/debs
cp *.deb /repo/debs/
cd /repo
dpkg-scanpackages debs / | gzip > debs/Packages.gz
```

## 5. 制品仓库管理

### 5.1 Artifactory

JFrog Artifactory 是企业级制品仓库：

| 仓库类型 | 说明                   |
| -------- | ---------------------- |
| Local    | 本地仓库，存储内部制品 |
| Remote   | 远程仓库，代理外部仓库 |
| Virtual  | 虚拟仓库，聚合多个仓库 |

**支持的包格式**：Maven、npm、Docker、PyPI、RPM、DEB、Go、Helm 等。

### 5.2 Nexus

Sonatype Nexus 是另一个流行的制品仓库：

```mermaid
flowchart TD
    T0["Nexus"]
    T1["maven-releases (hosted)    # 发布仓库"]
    T2["maven-snapshots (hosted)   # 快照仓库"]
    T3["maven-central (proxy)      # 代理中央仓库"]
    T4["maven-public (group)       # 组仓库"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
```

### 5.3 制品版本管理

**语义化版本（SemVer）**：

$$\text{MAJOR.MINOR.PATCH}$$

- MAJOR：不兼容的 API 变更
- MINOR：向后兼容的功能新增
- PATCH：向后兼容的问题修复

**版本范围**：

```
>=1.0.0 <2.0.0    # 兼容1.x
^1.2.3            # >=1.2.3 <2.0.0
~1.2.3            # >=1.2.3 <1.3.0
1.*               # 1.x任意版本
```

## 6. 安全与签名

### 6.1 GPG 签名

```bash
# 生成密钥对
gpg --full-generate-key

# 签名 RPM
rpm --addsign package.rpm

# 验证签名
rpm --checksig package.rpm

# 签名 DEB
dpkg-sig -s builder -k KEYID package.deb
```

### 6.2 仓库安全

- 启用 GPG 检查（gpgcheck=1）
- 使用 HTTPS 传输
- 定期轮换签名密钥
- 实施访问控制策略

<!-- ============ 文档分隔线：031-devops/011-ServiceMesh.md ============ -->

## 1. 服务网格概述

### 1.1 什么是服务网格

服务网格（Service Mesh）是处理服务间通信的基础设施层，通过 Sidecar 代理模式实现流量管理、安全和可观测性。

**传统微服务通信**：

```
服务A ──直接调用──→ 服务B
```

**服务网格通信**：

```
服务A → Sidecar(Envoy) → Sidecar(Envoy) → 服务B
```

### 1.2 服务网格 vs 传统方式

| 特性     | 传统（SDK集成） | 服务网格       |
| -------- | --------------- | -------------- |
| 代码侵入 | 高              | 无             |
| 语言绑定 | 特定语言        | 语言无关       |
| 升级方式 | 重新编译        | 独立升级       |
| 功能覆盖 | 有限            | 全面           |
| 性能开销 | 低              | 略高（额外跳） |

## 2. Istio 架构

### 2.1 核心组件

```mermaid
flowchart TD
    CP[控制面 istiod<br/>Pilot 流量管理 / Citadel 安全证书 / Galley 配置验证]
    DP[数据面 Envoy<br/>Pod A App+Sidecar / Pod B App+Sidecar / Pod C App+Sidecar]
    CP <-->|配置下发| DP
```

### 2.2 Envoy Sidecar

每个 Pod 自动注入 Envoy 代理，拦截所有入站和出站流量：

- **入站流量**：iptables 重定向到 Envoy → 转发到应用容器
- **出站流量**：应用容器 → iptables 重定向到 Envoy → 转发到目标

### 2.3 istiod 统一控制面

Istio 1.5+ 将 Pilot、Citadel、Galley 合并为 istiod：

- **Pilot**：服务发现、流量管理、配置分发
- **Citadel**：证书管理、mTLS
- **Galley**：配置验证和分发

## 3. 流量管理

### 3.1 VirtualService

定义请求路由规则：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: my-service
spec:
  hosts:
    - my-service
  http:
    - match:
        - headers:
            x-version:
              exact: v2
      route:
        - destination:
            host: my-service
            subset: v2
    - route:
        - destination:
            host: my-service
            subset: v1
          weight: 90
        - destination:
            host: my-service
            subset: v2
          weight: 10
```

### 3.2 DestinationRule

定义目标服务的策略（负载均衡、连接池等）：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: my-service
spec:
  host: my-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: DEFAULT
        http1MaxPendingRequests: 100
    outlierDetection:
      consecutive5xxErrors: 3
      interval: 30s
      baseEjectionTime: 30s
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
      trafficPolicy:
        loadBalancer:
          simple: ROUND_ROBIN
```

### 3.3 金丝雀发布

```yaml
# 90% v1, 10% v2
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: canary
spec:
  hosts:
    - my-app
  http:
    - route:
        - destination:
            host: my-app
            subset: v1
          weight: 90
        - destination:
            host: my-app
            subset: v2
          weight: 10
```

### 3.4 故障注入

```yaml
# 注入延迟
spec:
  http:
    - fault:
        delay:
          percentage:
            value: 100
          fixedDelay: 5s
      route:
        - destination:
            host: my-service

# 注入中断
spec:
  http:
    - fault:
        abort:
          percentage:
            value: 50
          httpStatus: 500
      route:
        - destination:
            host: my-service
```

### 3.5 重试与超时

```yaml
spec:
  http:
    - route:
        - destination:
            host: my-service
      retries:
        attempts: 3
        perTryTimeout: 2s
        retryOn: 5xx,reset,connect-failure
      timeout: 10s
```

## 4. 安全

### 4.1 mTLS（双向 TLS）

Istio 自动为服务间通信启用 mTLS：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT # 严格模式：只允许mTLS
```

| 模式       | 说明                 |
| ---------- | -------------------- |
| UNSET      | 继承父级策略         |
| DISABLE    | 禁用 mTLS            |
| PERMISSIVE | 同时接受 mTLS 和明文 |
| STRICT     | 仅接受 mTLS          |

### 4.2 授权策略

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: httpbin-policy
  namespace: default
spec:
  selector:
    matchLabels:
      app: httpbin
  action: ALLOW
  rules:
    - from:
        - source:
            principals: ['cluster.local/ns/default/sa/sleep']
      to:
        - operation:
            methods: ['GET']
            paths: ['/info*']
      when:
        - key: request.headers[x-token]
          values: ['valid-token']
```

### 4.3 网关

```yaml
apiVersion: networking.istio.io/v1beta1
kind: Gateway
metadata:
  name: my-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
    - port:
        number: 443
        name: https
        protocol: HTTPS
      tls:
        mode: SIMPLE
        credentialName: my-cert
      hosts:
        - '*.example.com'
```

## 5. 可观测性

### 5.1 指标

Istio 自动生成服务网格指标：

| 指标                                | 说明     |
| ----------------------------------- | -------- |
| istio_requests_total                | 请求总数 |
| istio_request_duration_milliseconds | 请求延迟 |
| istio_request_bytes                 | 请求大小 |
| istio_response_bytes                | 响应大小 |

Prometheus 查询示例：

```promql
# 服务成功率
sum(rate(istio_requests_total{response_code!~"5.*"}[5m]))
/
sum(rate(istio_requests_total[5m]))

# P99 延迟
histogram_quantile(0.99,
  sum(rate(istio_request_duration_milliseconds_bucket[5m]))
  by (le, destination_service))
```

### 5.2 分布式追踪

Istio 自动为请求添加追踪头并上报：

- 支持的追踪后端：Jaeger、Zipkin、Lightstep
- 自动传播 B3 追踪头
- 采样率可配置

### 5.3 访问日志

```yaml
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: default
spec:
  accessLogging:
    - providers:
        - name: otel
      outputFormat:
        labels:
          request_method: '%REQ(:METHOD)%'
          request_path: '%REQ(:PATH)%'
          response_code: '%RESPONSE_CODE%'
```

## 6. 其他服务网格

### 6.1 Linkerd

- 轻量级，Rust 实现的微代理
- 配置简单，开箱即用
- 资源开销小

### 6.2 Consul Connect

- HashiCorp 出品
- 与 Consul 服务发现深度集成
- 支持多平台（K8s + VM）

### 6.3 对比

| 特性     | Istio  | Linkerd        | Consul Connect |
| -------- | ------ | -------------- | -------------- |
| 代理     | Envoy  | linkerd2-proxy | Envoy          |
| 复杂度   | 高     | 低             | 中             |
| 功能     | 最全面 | 核心功能       | 核心功能       |
| 性能开销 | 较高   | 低             | 中             |
| 社区     | 最大   | 活跃           | 活跃           |

<!-- ============ 文档分隔线：031-devops/012-LogManagement.md ============ -->

## 1. 日志管理概述

### 1.1 日志级别

| 级别  | 说明                   | 示例               |
| ----- | ---------------------- | ------------------ |
| FATAL | 致命错误，系统无法继续 | 数据库连接失败     |
| ERROR | 错误，影响功能         | API 调用失败       |
| WARN  | 警告，潜在问题         | 磁盘空间不足       |
| INFO  | 重要信息               | 服务启动、请求完成 |
| DEBUG | 调试信息               | 变量值、执行路径   |
| TRACE | 详细跟踪               | 函数进出           |

### 1.2 日志最佳实践

- 使用结构化日志（JSON 格式）
- 包含请求 ID 用于追踪
- 避免记录敏感信息
- 设置合理的日志级别
- 日志轮转和归档

## 2. ELK Stack

### 2.1 架构

```
应用 → Filebeat → Logstash → Elasticsearch → Kibana
                      ↑
                 其他数据源
```

| 组件          | 功能         |
| ------------- | ------------ |
| Elasticsearch | 存储和搜索   |
| Logstash      | 数据处理管道 |
| Kibana        | 可视化界面   |
| Beats         | 轻量级采集器 |

### 2.2 Elasticsearch

**索引管理**：

```bash
# 创建索引
PUT /my-logs
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "timestamp": { "type": "date" },
      "level": { "type": "keyword" },
      "message": { "type": "text" },
      "service": { "type": "keyword" },
      "trace_id": { "type": "keyword" }
    }
  }
}

# 索引生命周期管理（ILM）
PUT _ilm/policy/logs-policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": { "max_age": "1d", "max_size": "50gb" }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "shrink": { "number_of_shards": 1 },
          "forcemerge": { "max_num_segments": 1 }
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": { "freeze": {} }
      },
      "delete": {
        "min_age": "90d",
        "actions": { "delete": {} }
      }
    }
  }
}
```

### 2.3 Logstash

**管道配置**：

```ruby
input {
  beats {
    port => 5044
  }
  kafka {
    topics => ["app-logs"]
    group_id => "logstash"
  }
}

filter {
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:msg}" }
  }
  json {
    source => "message"
    target => "parsed"
  }
  mutate {
    remove_field => ["message"]
    add_field => { "env" => "production" }
  }
  date {
    match => ["timestamp", "ISO8601"]
    target => "@timestamp"
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "logs-%{[service]}-%{+YYYY.MM.dd}"
  }
}
```

### 2.4 Kibana

**常用查询语法（KQL）**：

```
level: "ERROR" AND service: "api-gateway"
trace_id: "abc123"
@timestamp >= "2026-06-14" AND message: "timeout"
```

**可视化**：

- Discover：日志搜索和浏览
- Dashboard：仪表盘
- Lens：可视化构建器
- APM：应用性能监控

## 3. Fluentd / Fluent Bit

### 3.1 Fluentd

统一日志采集和处理：

```ruby
# fluent.conf
<source>
  @type tail
  path /var/log/app/*.log
  pos_file /var/log/fluent/app.log.pos
  tag app.logs
  <parse>
    @type json
  </parse>
</source>

<filter app.**>
  @type record_transformer
  <record>
    hostname "#{Socket.gethostname}"
    environment "production"
  </record>
</filter>

<match app.**>
  @type elasticsearch
  host elasticsearch
  port 9200
  logstash_format true
  logstash_prefix fluentd
  <buffer>
    @type file
    path /var/log/fluent/buffer
    flush_interval 5s
  </buffer>
</match>
```

### 3.2 Fluent Bit

轻量级日志处理器，适合边缘和容器环境：

```ini
[INPUT]
    Name              tail
    Path              /var/log/containers/*.log
    Parser            docker
    Tag               kube.*
    Mem_Buf_Limit     5MB
    Skip_Long_Lines   On

[FILTER]
    Name              kubernetes
    Match             kube.*
    Kube_URL          https://kubernetes.default.svc:443
    Kube_CA_File      /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    Kube_Token_File   /var/run/secrets/kubernetes.io/serviceaccount/token

[OUTPUT]
    Name              es
    Match             *
    Host              elasticsearch
    Port              9200
    Logstash_Format   On
    Replace_Dots      On
    Retry_Limit       False
```

### 3.3 Fluentd vs Fluent Bit

| 特性     | Fluentd  | Fluent Bit |
| -------- | -------- | ---------- |
| 语言     | Ruby + C | C          |
| 内存     | 较高     | 极低       |
| 功能     | 丰富     | 核心功能   |
| 适用场景 | 服务器   | 容器/边缘  |
| 插件     | 500+     | 100+       |

## 4. 结构化日志

### 4.1 JSON 日志格式

```json
{
  "timestamp": "2026-06-14T10:30:00.123Z",
  "level": "INFO",
  "service": "user-service",
  "trace_id": "abc123def456",
  "span_id": "span789",
  "user_id": "user_001",
  "method": "GET",
  "path": "/api/users/001",
  "status_code": 200,
  "duration_ms": 45,
  "message": "Request completed"
}
```

### 4.2 各语言日志库

| 语言    | 日志库                     | 结构化支持 |
| ------- | -------------------------- | ---------- |
| Java    | Logback + Logstash Encoder | 是         |
| Go      | zap, zerolog               | 是         |
| Python  | structlog                  | 是         |
| Node.js | pino, winston              | 是         |
| Rust    | tracing, slog              | 是         |

## 5. 日志采集架构

### 5.1 DaemonSet 模式

每个节点运行一个日志采集器：

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
spec:
  template:
    spec:
      containers:
        - name: fluent-bit
          image: fluent/fluent-bit:3.0
          volumeMounts:
            - name: varlog
              mountPath: /var/log
            - name: containers
              mountPath: /var/lib/docker/containers
      volumes:
        - name: varlog
          hostPath:
            path: /var/log
        - name: containers
          hostPath:
            path: /var/lib/docker/containers
```

### 5.2 Sidecar 模式

每个 Pod 运行一个日志采集器 Sidecar：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-with-logging
spec:
  containers:
    - name: app
      image: my-app
    - name: log-collector
      image: fluent/fluent-bit:3.0
      volumeMounts:
        - name: log-volume
          mountPath: /logs
  volumes:
    - name: log-volume
      emptyDir: {}
```

### 5.3 模式对比

| 模式      | 资源开销 | 灵活性 | 适用场景   |
| --------- | -------- | ------ | ---------- |
| DaemonSet | 低       | 低     | 标准日志   |
| Sidecar   | 高       | 高     | 特殊格式   |
| 应用直推  | 无       | 最高   | 云原生应用 |

## 6. 日志分析

### 6.1 常用分析场景

**错误率监控**：

```promql
sum(rate(log_entries{level="ERROR"}[5m]))
/
sum(rate(log_entries[5m]))
```

**慢请求分析**：

```
KQL: duration_ms: > 1000 AND level: "WARN"
```

**异常检测**：

- 基于统计的异常检测
- 日志模式聚类
- 关联分析（同一 trace_id 的日志）

### 6.2 日志告警

```yaml
# Elasticsearch 告警规则
- name: error_rate_alert
  index: logs-*
  type: frequency
  filter:
    - term:
        level: ERROR
  threshold: 100
  timeframe:
    minutes: 5
  alert:
    - email
    - slack
```

<!-- ============ 文档分隔线：031-devops/013-ConfigManagement.md ============ -->

## 1. 配置管理概述

### 1.1 配置管理原则

- **基础设施即代码**：所有配置以代码形式管理
- **版本控制**：配置变更可追踪
- **幂等性**：多次执行结果相同
- **不可变基础设施**：替换而非修改

### 1.2 配置管理工具对比

| 工具      | 语言   | Agent | 模式  |
| --------- | ------ | ----- | ----- |
| Ansible   | YAML   | 无    | 推送  |
| Puppet    | Ruby   | 有    | 拉取  |
| Chef      | Ruby   | 有    | 拉取  |
| SaltStack | Python | 有    | 推/拉 |

## 2. Ansible

### 2.1 核心概念

| 概念      | 说明     |
| --------- | -------- |
| Inventory | 主机清单 |
| Module    | 功能模块 |
| Playbook  | 任务剧本 |
| Role      | 角色封装 |
| Task      | 具体任务 |

### 2.2 Inventory

```ini
# ini 格式
[webservers]
web1 ansible_host=192.168.1.10
web2 ansible_host=192.168.1.11

[dbservers]
db1 ansible_host=192.168.1.20

[production:children]
webservers
dbservers

[production:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/deploy_key
```

```yaml
# YAML 格式
all:
  children:
    webservers:
      hosts:
        web1:
          ansible_host: 192.168.1.10
        web2:
          ansible_host: 192.168.1.11
    dbservers:
      hosts:
        db1:
          ansible_host: 192.168.1.20
```

### 2.3 Playbook

```yaml
---
- name: Deploy Web Application
  hosts: webservers
  become: yes
  vars:
    app_name: myapp
    app_port: 8080

  tasks:
    - name: Install dependencies
      apt:
        name:
          - nginx
          - python3
          - python3-pip
        state: present
        update_cache: yes

    - name: Copy application code
      synchronize:
        src: /opt/myapp/
        dest: /opt/myapp/
        delete: yes

    - name: Install Python dependencies
      pip:
        requirements: /opt/myapp/requirements.txt
        virtualenv: /opt/myapp/venv

    - name: Configure nginx
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/sites-available/myapp
      notify: Reload nginx

    - name: Enable site
      file:
        src: /etc/nginx/sites-available/myapp
        dest: /etc/nginx/sites-enabled/myapp
        state: link
      notify: Reload nginx

    - name: Start application
      systemd:
        name: myapp
        state: started
        enabled: yes

  handlers:
    - name: Reload nginx
      systemd:
        name: nginx
        state: reloaded
```

### 2.4 常用模块

| 模块             | 用途                |
| ---------------- | ------------------- |
| apt/yum          | 包管理              |
| copy/template    | 文件分发            |
| service/systemd  | 服务管理            |
| user/group       | 用户管理            |
| file             | 文件/目录管理       |
| command/shell    | 执行命令            |
| git              | 代码拉取            |
| docker_container | Docker 管理         |
| k8s              | Kubernetes 资源管理 |

### 2.5 Role 结构

```mermaid
flowchart TD
    T0["roles/myapp/"]
    T1["defaults/"]
    T2["main.yml        # 默认变量"]
    T3["vars/"]
    T4["main.yml        # 优先级更高的变量"]
    T5["tasks/"]
    T6["main.yml        # 主任务"]
    T7["handlers/"]
    T8["main.yml        # 处理器"]
    T9["templates/"]
    T10["nginx.conf.j2   # 模板文件"]
    T11["files/"]
    T12["config.ini      # 静态文件"]
    T13["meta/"]
    T14["main.yml        # 依赖声明"]
    T15["tests/"]
    T16["test.yml        # 测试"]
    T0 --> T1
    T2 --> T3
    T4 --> T5
    T6 --> T7
    T8 --> T9
    T10 --> T11
    T12 --> T13
    T14 --> T15
    T15 --> T16
```

## 3. 配置中心

### 3.1 集中式配置

**Spring Cloud Config**：

```yaml
# config-server 配置
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/org/config-repo
          searchPaths: '{application}/{profile}'
```

**Nacos**：

```bash
# 发布配置
curl -X POST "http://nacos:8848/nacos/v1/cs/configs" \
  -d "dataId=myapp.properties&group=DEFAULT_GROUP&content=server.port=8080"

# 获取配置
curl "http://nacos:8848/nacos/v1/cs/configs?dataId=myapp.properties&group=DEFAULT_GROUP"
```

### 3.2 配置优先级

```
命令行参数 > 环境变量 > 配置中心 > 本地配置文件 > 默认值
```

### 3.3 配置热更新

- **推送模式**：配置中心主动通知应用
- **拉取模式**：应用定期轮询
- **长轮询**：应用发起长连接等待变更

## 4. 环境管理

### 4.1 环境隔离策略

| 策略         | 说明          | 适用场景     |
| ------------ | ------------- | ------------ |
| 命名空间隔离 | K8s namespace | 同集群多环境 |
| 集群隔离     | 独立 K8s 集群 | 生产环境     |
| 账号隔离     | 云账号隔离    | 合规要求     |

### 4.2 环境配置管理

```mermaid
flowchart TD
    T0["config/"]
    T1["base/               # 基础配置"]
    T2["deployment.yaml"]
    T3["service.yaml"]
    T4["overlays/"]
    T5["development/    # 开发环境覆盖"]
    T6["kustomization.yaml"]
    T7["staging/        # 预发布环境覆盖"]
    T8["kustomization.yaml"]
    T9["production/     # 生产环境覆盖"]
    T10["kustomization.yaml"]
    T0 --> T1
    T3 --> T4
```

**Kustomize**：

```yaml
# overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
bases:
  - ../../base
patchesStrategicMerge:
  - deployment-patch.yaml
replicas:
  - name: myapp
    count: 5
```

## 5. 密钥管理

### 5.1 密钥管理原则

- 密钥不硬编码
- 密钥不入版本控制
- 密钥加密存储
- 密钥定期轮换
- 最小权限原则

### 5.2 HashiCorp Vault

```bash
# 启动 Vault
vault server -dev

# 写入密钥
vault kv put secret/myapp db_password="s3cret" api_key="key123"

# 读取密钥
vault kv get secret/myapp

# 动态数据库凭证
vault secrets enable database
vault write database/config/mydb \
  plugin_name=mysql-database-plugin \
  connection_url="{{username}}:{{password}}@tcp(db:3306)/" \
  allowed_roles="readonly"

vault write database/roles/readonly \
  db_name=mydb \
  creation_statements="CREATE USER '{{name}}'@'%' IDENTIFIED BY '{{password}}'; GRANT SELECT ON *.* TO '{{name}}'@'%';" \
  default_ttl="1h" max_ttl="24h"
```

### 5.3 Kubernetes Secrets

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: myapp-secret
type: Opaque
data:
  db-password: c2VjcmV0 # base64 编码
stringData:
  api-key: 'plain-text' # 明文（创建时编码）
```

**加密存储**：

```yaml
# encryption-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
    providers:
      - aescbc:
          keys:
            - name: key1
              secret: <base64-encoded-key>
      - identity: {}
```

### 5.4 External Secrets Operator

从外部密钥管理器同步到 K8s Secrets：

```yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: myapp-secret
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: myapp-secret
  data:
    - secretKey: db-password
      remoteRef:
        key: secret/myapp
        property: db_password
```

## 6. GitOps

### 6.1 GitOps 原则

1. 声明式：系统描述是声明式的
2. 版本控制：期望状态存储在 Git
3. 自动拉取：自动应用期望状态
4. 持续协调：持续确保实际状态与期望一致

### 6.2 ArgoCD

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/manifests.git
    targetRevision: HEAD
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: myapp
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

### 6.3 Flux

```yaml
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: GitRepository
metadata:
  name: myapp
spec:
  url: https://github.com/org/manifests.git
  ref:
    branch: main
  interval: 1m
---
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: myapp
spec:
  sourceRef:
    kind: GitRepository
    name: myapp
  interval: 5m
  prune: true
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: myapp
      namespace: default
```

<!-- ============ 文档分隔线：031-devops/014-PerformanceTuning.md ============ -->

## 1. 性能调优方法论

### 1.1 USE 方法

对每个资源检查：

- **Utilization（利用率）**：资源忙碌的时间比例
- **Saturation（饱和度）**：资源排队等待的程度
- **Errors（错误）**：错误事件计数

### 1.2 性能分析流程

```
1. 定义性能目标
2. 建立基准（Baseline）
3. 识别瓶颈
4. 提出假设
5. 验证假设
6. 实施优化
7. 验证效果
8. 重复3-7
```

### 1.3 阿姆达尔定律

$$S = \frac{1}{(1-f) + f/s}$$

其中 $f$ 为可优化部分的比例，$s$ 为优化倍数。

## 2. CPU 性能分析

### 2.1 CPU 指标

| 指标       | 含义              | 工具             |
| ---------- | ----------------- | ---------------- |
| CPU 利用率 | 用户+系统时间占比 | top, vmstat      |
| 运行队列   | 等待运行的进程数  | vmstat           |
| 上下文切换 | 进程切换次数      | vmstat           |
| 中断次数   | 硬件/软件中断     | /proc/interrupts |

### 2.2 分析工具

```bash
# CPU 使用概况
top -H -p <pid>        # 按线程查看
htop                    # 交互式

# CPU 火焰图
perf record -g -p <pid>
perf script | stackcollapse-perf.pl | flamegraph.pl > cpu.svg

# 系统调用追踪
strace -c -p <pid>     # 统计系统调用
strace -e trace=network -p <pid>  # 追踪网络调用

# 上下文切换分析
perf stat -e context-switches -p <pid>
```

### 2.3 CPU 优化策略

| 策略       | 方法               |
| ---------- | ------------------ |
| 减少计算   | 算法优化、缓存结果 |
| 并行化     | 多线程、异步       |
| CPU 亲和性 | taskset 绑核       |
| 调度优先级 | nice/renice        |
| 中断均衡   | IRQ 亲和性         |

## 3. 内存性能分析

### 3.1 内存指标

```bash
# 内存使用
free -h
cat /proc/meminfo

# 详细信息
vmstat 1              # 每秒统计

# 进程内存
pmap -x <pid>         # 进程内存映射
smem -t -k            # 按进程排序
```

**关键指标**：

| 指标          | 含义                     |
| ------------- | ------------------------ |
| used          | 已使用内存               |
| free          | 空闲内存                 |
| buffers/cache | 内核缓冲和缓存           |
| available     | 可用内存（含可回收缓存） |
| swap used     | 交换空间使用量           |

### 3.2 页缓存与脏页

```bash
# 查看脏页
cat /proc/meminfo | grep -i dirty

# 手动刷盘
sync

# 调整脏页阈值
sysctl vm.dirty_ratio=20              # 脏页占总内存20%时刷盘
sysctl vm.dirty_background_ratio=10   # 后台刷盘阈值
```

### 3.3 OOM 管理

```bash
# OOM 分数
cat /proc/<pid>/oom_score
cat /proc/<pid>/oom_score_adj

# 禁止 OOM Kill
echo -1000 > /proc/<pid>/oom_score_adj

# 查看 OOM 日志
dmesg | grep -i oom
journalctl -k | grep -i oom
```

### 3.4 内存优化

| 策略     | 方法            |
| -------- | --------------- |
| 减少分配 | 对象池、复用    |
| 减少拷贝 | 零拷贝、mmap    |
| 调整 GC  | 堆大小、GC 策略 |
| 大页     | HugePages       |
| 交换优化 | 调整 swappiness |

## 4. 磁盘 I/O 性能

### 4.1 I/O 指标

| 指标     | 含义             |
| -------- | ---------------- |
| IOPS     | 每秒 I/O 操作数  |
| 吞吐量   | 每秒传输数据量   |
| 延迟     | I/O 操作响应时间 |
| 队列深度 | 等待中的 I/O 数  |

### 4.2 分析工具

```bash
# I/O 统计
iostat -xz 1          # 每秒统计
iotop                  # 按进程 I/O 排序

# I/O 延迟分析
biolatency             # eBPF 块 I/O 延迟直方图
biosnoop               # 每次 I/O 追踪

# 文件系统追踪
ext4slower            # eBPF 追踪慢 ext4 操作
```

### 4.3 I/O 调度器

| 调度器      | 特点            | 适用场景 |
| ----------- | --------------- | -------- |
| noop        | 简单 FIFO       | SSD      |
| deadline    | 保证延迟        | 数据库   |
| cfq         | 公平分配        | 通用     |
| mq-deadline | 多队列 deadline | NVMe SSD |
| bfq         | 公平+低延迟     | 桌面     |

```bash
# 查看当前调度器
cat /sys/block/sda/queue/scheduler

# 修改调度器
echo deadline > /sys/block/sda/queue/scheduler
```

## 5. 网络性能

### 5.1 网络指标

| 指标   | 含义         |
| ------ | ------------ |
| 带宽   | 最大传输速率 |
| 吞吐量 | 实际传输速率 |
| 延迟   | 网络往返时间 |
| 丢包率 | 丢失包的比例 |
| 重传率 | 重传包的比例 |

### 5.2 分析工具

```bash
# 连接统计
ss -s                  # 连接概览
ss -tnp                # TCP 连接详情

# 网络统计
sar -n DEV 1           # 网卡流量
sar -n TCP,ETCP 1      # TCP 统计

# 延迟测试
ping -c 10 target
mtr target             # 路由追踪+延迟

# 带宽测试
iperf3 -s              # 服务端
iperf3 -c server       # 客户端

# TCP 追踪
tcplife                # eBPF TCP 连接生命周期
tcpretrans             # eBPF TCP 重传
```

### 5.3 内核参数优化

```bash
# TCP 缓冲区
sysctl net.core.rmem_max=16777216
sysctl net.core.wmem_max=16777216
sysctl net.ipv4.tcp_rmem='4096 87380 16777216'
sysctl net.ipv4.tcp_wmem='4096 65536 16777216'

# 连接队列
sysctl net.core.somaxconn=65535
sysctl net.ipv4.tcp_max_syn_backlog=65535

# TIME_WAIT 优化
sysctl net.ipv4.tcp_tw_reuse=1
sysctl net.ipv4.tcp_fin_timeout=15

# 保活
sysctl net.ipv4.tcp_keepalive_time=600
sysctl net.ipv4.tcp_keepalive_intvl=30
sysctl net.ipv4.tcp_keepalive_probes=3
```

## 6. 应用性能

### 6.1 性能剖析（Profiling）

| 语言    | CPU Profiler        | 内存 Profiler |
| ------- | ------------------- | ------------- |
| Java    | async-profiler, JFR | jmap, MAT     |
| Go      | pprof               | pprof         |
| Python  | cProfile, py-spy    | memray        |
| Node.js | --prof, clinic      | --inspect     |
| Rust    | perf, flamegraph    | valgrind      |

### 6.2 连接池优化

$$\text{最优连接数} \approx \text{CPU核心数} \times (1 + \frac{\text{等待时间}}{\text{计算时间}})$$

### 6.3 缓存策略

| 缓存层      | 命中率目标 | 典型延迟 |
| ----------- | ---------- | -------- |
| L1/L2 Cache | >95%       | ~1ns     |
| 应用缓存    | >80%       | ~1ms     |
| Redis       | >70%       | ~1ms     |
| CDN         | >90%       | ~10ms    |

## 7. 压力测试

### 7.1 压测工具

| 工具     | 特点        | 协议   |
| -------- | ----------- | ------ |
| wrk/wrk2 | 高性能      | HTTP   |
| JMeter   | 功能全面    | 多协议 |
| Locust   | Python 编写 | HTTP   |
| k6       | JavaScript  | HTTP   |
| Gatling  | Scala       | HTTP   |

### 7.2 wrk 使用

```bash
# 基本压测
wrk -t4 -c100 -d30s http://target/

# 延迟分布
wrk -t4 -c100 -d30s --latency http://target/

# 自定义脚本
wrk -t4 -c100 -d30s -s post.lua http://target/
```

### 7.3 性能基准

| 指标     | 优秀   | 良好   | 需优化 |
| -------- | ------ | ------ | ------ |
| P50 延迟 | <10ms  | <50ms  | >100ms |
| P99 延迟 | <50ms  | <200ms | >500ms |
| 错误率   | <0.01% | <0.1%  | >1%    |
| QPS      | >10000 | >1000  | <100   |

<!-- ============ 文档分隔线：031-devops/015-HighAvailabilityArchitecture.md ============ -->

## 1. 高可用概述

### 1.1 可用性指标

$$\text{可用性} = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$$

| 可用性  | 年停机   | 等级     |
| ------- | -------- | -------- |
| 99%     | 3.65天   | 基本     |
| 99.9%   | 8.76小时 | 标准     |
| 99.99%  | 52.6分钟 | 高可用   |
| 99.999% | 5.26分钟 | 极高可用 |

### 1.2 高可用设计原则

- **消除单点故障**：冗余所有关键组件
- **故障检测**：快速发现故障
- **故障转移**：自动切换到备用
- **降级策略**：部分功能不可用时保核心
- **限流保护**：防止雪崩

## 2. 冗余设计

### 2.1 主动-主动模式

多个实例同时提供服务：

```
客户端 → 负载均衡 → 实例1 (活跃)
                  → 实例2 (活跃)
                  → 实例3 (活跃)
```

优点：资源利用率高，无切换延迟
缺点：数据一致性挑战

### 2.2 主动-被动模式

一个主实例服务，备用实例待命：

```
客户端 → 主实例 (活跃)
         备实例 (待命)
```

优点：数据一致性好
缺点：资源利用率低，切换有延迟

### 2.3 多活架构

多个数据中心同时提供服务：

```
用户 → DNS → 北京机房 (活跃)
            → 上海机房 (活跃)
            → 广州机房 (活跃)
```

**数据同步**：跨机房数据同步是核心挑战。

## 3. 负载均衡

### 3.1 四层负载均衡（L4）

基于传输层信息（IP+端口）分发：

| 实现     | 特点                 |
| -------- | -------------------- |
| LVS/IPVS | Linux 内核级，高性能 |
| HAProxy  | 功能丰富             |
| AWS NLB  | 云原生               |

**LVS 模式**：

| 模式 | 原理        | 性能 | 限制               |
| ---- | ----------- | ---- | ------------------ |
| NAT  | 修改目标IP  | 中   | RS网关指向Director |
| DR   | 修改MAC地址 | 高   | RS与Director同网段 |
| TUN  | IP隧道      | 高   | RS支持隧道         |

### 3.2 七层负载均衡（L7）

基于应用层信息（URL、Header、Cookie）分发：

| 实现    | 特点       |
| ------- | ---------- |
| Nginx   | 最广泛使用 |
| HAProxy | 功能丰富   |
| Envoy   | 云原生     |
| AWS ALB | 云原生     |

**Nginx 负载均衡**：

```nginx
upstream backend {
    least_conn;
    server 10.0.0.1:8080 weight=5;
    server 10.0.0.2:8080 weight=3;
    server 10.0.0.3:8080 backup;

    keepalive 32;
    max_fails 3;
    fail_timeout 30s;
}

server {
    location / {
        proxy_pass http://backend;
        proxy_next_upstream error timeout http_503;
    }
}
```

### 3.3 负载均衡算法

| 算法       | 说明           | 适用场景       |
| ---------- | -------------- | -------------- |
| 轮询       | 依次分配       | 服务器性能相同 |
| 加权轮询   | 按权重分配     | 服务器性能不同 |
| 最少连接   | 选连接最少的   | 长连接         |
| 一致性哈希 | 按请求特征哈希 | 有状态服务     |
| 随机       | 随机选择       | 简单场景       |

### 3.4 健康检查

```nginx
# 主动健康检查（Nginx Plus）
upstream backend {
    server 10.0.0.1:8080;
    server 10.0.0.2:8080;

    health_check interval=5s fails=3 passes=2 uri=/health;
}
```

## 4. 故障转移

### 4.1 数据库故障转移

**MySQL MHA**：

```
Master → Slave1
       → Slave2
       → Slave3

Master 故障时：
1. MHA 检测到故障
2. 选择最新 Slave 提升为新 Master
3. 其他 Slave 指向新 Master
4. VIP 漂移到新 Master
```

**Redis Sentinel**：

```
Master ← Sentinel1
       ← Sentinel2
       ← Sentinel3

Master 故障时：
1. Sentinel 投票选举
2. 执行故障转移
3. 通知客户端新 Master 地址
```

### 4.2 VIP 漂移

```bash
# Keepalived 配置
vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1

    virtual_ipaddress {
        192.168.1.100
    }

    track_script {
        check_nginx
    }
}
```

### 4.3 DNS 故障转移

```
service.example.com → 10.0.0.1 (TTL=30s)
                    → 10.0.0.2 (TTL=30s)

10.0.0.1 故障时：
DNS 健康检查检测到 → 移除 10.0.0.1 记录
```

## 5. 限流与降级

### 5.1 限流算法

**固定窗口**：

$$\text{允许} \iff \text{计数} < \text{阈值}$$

问题：窗口边界处可能通过2倍流量。

**滑动窗口**：更精确，但实现复杂。

**令牌桶**：

- 以固定速率 $r$ 生成令牌
- 桶容量 $b$，允许突发 $b$ 个请求
- 长期平均速率不超过 $r$

**漏桶**：

- 请求以固定速率 $r$ 流出
- 桶满时新请求被拒绝
- 输出速率恒定

### 5.2 熔断器

```
关闭状态 → 失败率超阈值 → 打开状态
打开状态 → 超时 → 半开状态
半开状态 → 测试请求成功 → 关闭状态
半开状态 → 测试请求失败 → 打开状态
```

### 5.3 降级策略

| 策略     | 说明           |
| -------- | -------------- |
| 读降级   | 返回缓存数据   |
| 写降级   | 异步写入       |
| 功能降级 | 关闭非核心功能 |
| 限流降级 | 排队或拒绝     |

## 6. 混沌工程

### 6.1 混沌工程原则

1. 建立稳态假设
2. 模拟现实世界事件
3. 在生产环境运行实验
4. 自动化持续运行
5. 最小化爆炸半径

### 6.2 Chaos Monkey

Netflix 开源的混沌工程工具：

- 随机终止生产实例
- 验证自动恢复能力
- 在工作时间运行

### 6.3 Chaos Mesh

Kubernetes 混沌工程平台：

```yaml
# 网络延迟注入
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-delay
spec:
  action: delay
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      app: my-service
  delay:
    latency: '100ms'
    correlation: '50'
  duration: '5m'
```

```yaml
# Pod 故障注入
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: pod-kill
spec:
  action: pod-kill
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      app: my-service
  scheduler:
    cron: '@every 10m'
```

### 6.4 故障注入类型

| 类型     | 工具           | 说明             |
| -------- | -------------- | ---------------- |
| Pod 故障 | Chaos Mesh     | Kill/删除 Pod    |
| 网络故障 | Chaos Mesh, tc | 延迟、丢包、分区 |
| I/O 故障 | Chaos Mesh     | 延迟、错误       |
| CPU 压力 | stress-ng      | CPU 负载         |
| 内存压力 | stress-ng      | 内存消耗         |
| 时间偏移 | Chaos Mesh     | 时钟漂移         |

<!-- ============ 文档分隔线：031-devops/016-AutomationTest.md ============ -->

## 1. 测试金字塔

```
        /  E2E测试  \        少量，慢，脆弱
       /  集成测试    \      适量
      /   单元测试      \    大量，快，稳定
```

| 层级     | 数量 | 速度 | 范围        | 成本 |
| -------- | ---- | ---- | ----------- | ---- |
| 单元测试 | 多   | 毫秒 | 单个函数/类 | 低   |
| 集成测试 | 中   | 秒   | 模块间交互  | 中   |
| E2E测试  | 少   | 分钟 | 完整流程    | 高   |

## 2. 单元测试

### 2.1 测试框架

| 语言       | 框架    | 断言库  |
| ---------- | ------- | ------- |
| Java       | JUnit 5 | AssertJ |
| Python     | pytest  | 内置    |
| Go         | testing | testify |
| JavaScript | Jest    | 内置    |
| Rust       | 内置    | assert! |

### 2.2 测试结构（AAA 模式）

```python
def test_user_creation():
    # Arrange（准备）
    user_data = {"name": "Alice", "email": "alice@example.com"}

    # Act（执行）
    user = create_user(user_data)

    # Assert（断言）
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
```

### 2.3 Mock 与 Stub

```python
from unittest.mock import Mock, patch

# Mock
db = Mock()
db.save.return_value = True
assert db.save({"name": "Alice"}) == True

# Patch
@patch('module.external_api')
def test_with_patch(mock_api):
    mock_api.return_value = {"status": "ok"}
    result = call_api()
    assert result["status"] == "ok"
```

### 2.4 测试覆盖率

| 覆盖率类型 | 说明               |
| ---------- | ------------------ |
| 行覆盖率   | 执行到的代码行比例 |
| 分支覆盖率 | 执行到的分支比例   |
| 函数覆盖率 | 调用到的函数比例   |
| 路径覆盖率 | 执行到的路径比例   |

```bash
# 生成覆盖率报告
pytest --cov=myapp --cov-report=html
go test -coverprofile=coverage.out
jest --coverage
```

## 3. 集成测试

### 3.1 数据库集成测试

```python
import pytest
from testcontainers.postgres import PostgresContainer

@pytest.fixture
def postgres():
    with PostgresContainer("postgres:16") as pg:
        yield pg.get_connection_url()

def test_user_repository(postgres):
    repo = UserRepository(postgres)
    repo.create(User(name="Alice"))
    users = repo.find_all()
    assert len(users) == 1
```

### 3.2 API 集成测试

```python
from fastapi.testclient import TestClient

def test_create_user():
    client = TestClient(app)
    response = client.post("/api/users", json={
        "name": "Alice",
        "email": "alice@example.com"
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"
```

### 3.3 消息队列集成测试

```python
from testcontainers.rabbitmq import RabbitMqContainer

@pytest.fixture
def rabbitmq():
    with RabbitMqContainer("rabbitmq:3-management") as rb:
        yield rb

def test_message_publish(rabbitmq):
    publisher = MessagePublisher(rabbitmq)
    consumer = MessageConsumer(rabbitmq)

    publisher.publish("test_queue", {"event": "created"})
    message = consumer.consume("test_queue", timeout=5)

    assert message["event"] == "created"
```

## 4. E2E 测试

### 4.1 Playwright

```javascript
test('user login flow', async ({ page }) => {
  await page.goto('/login');

  await page.fill('[data-testid="username"]', 'alice');
  await page.fill('[data-testid="password"]', 'secret');
  await page.click('[data-testid="login-btn"]');

  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('.welcome')).toContainText('Alice');
});
```

### 4.2 Cypress

```javascript
describe('User Login', () => {
  it('should login successfully', () => {
    cy.visit('/login');
    cy.get('[data-testid="username"]').type('alice');
    cy.get('[data-testid="password"]').type('secret');
    cy.get('[data-testid="login-btn"]').click();
    cy.url().should('include', '/dashboard');
    cy.get('.welcome').should('contain', 'Alice');
  });
});
```

### 4.3 E2E 测试最佳实践

- 使用 data-testid 选择器
- 避免依赖实现细节
- 测试关键用户流程
- 设置合理的超时
- 并行执行加速
- 视频和截图记录失败

## 5. 契约测试

### 5.1 Pact

消费者驱动契约测试：

```javascript
// 消费者端
const provider = new Pact({
  consumer: 'UserService',
  provider: 'UserAPI',
});

await provider.addInteraction({
  state: 'user exists',
  uponReceiving: 'a request for user',
  withRequest: {
    method: 'GET',
    path: '/api/users/1',
  },
  willRespondWith: {
    status: 200,
    body: { id: 1, name: 'Alice' },
  },
});
```

```javascript
// 提供者端验证
const verifier = new Verifier({
  providerBaseUrl: 'http://localhost:8080',
  pactBrokerUrl: 'http://pact-broker:9292',
  provider: 'UserAPI',
});

await verifier.verify();
```

## 6. 性能测试

### 6.1 负载测试

确定系统在预期负载下的表现：

```javascript
// k6 脚本
import http from 'k6/http';

export const options = {
  stages: [
    { duration: '2m', target: 100 }, // 上升到100用户
    { duration: '5m', target: 100 }, // 维持100用户
    { duration: '2m', target: 0 }, // 下降到0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
  http.get('http://target/api/users');
}
```

### 6.2 压力测试

确定系统的极限：

```javascript
export const options = {
  stages: [
    { duration: '5m', target: 500 },
    { duration: '5m', target: 1000 },
    { duration: '5m', target: 2000 },
    { duration: '5m', target: 0 },
  ],
};
```

### 6.3 浸泡测试

长时间运行检测内存泄漏等问题：

```javascript
export const options = {
  stages: [
    { duration: '1h', target: 50 },
    { duration: '12h', target: 50 },
    { duration: '1h', target: 0 },
  ],
};
```

## 7. CI 中的测试策略

### 7.1 测试门禁

```yaml
# GitHub Actions
- name: Run tests
  run: |
    pytest --cov=myapp --cov-fail-under=80
    pytest integration/ -m "not slow"
```

### 7.2 测试分层执行

| 阶段    | 测试类型 | 频率     | 触发 |
| ------- | -------- | -------- | ---- |
| PR      | 单元测试 | 每次提交 | 自动 |
| PR      | 集成测试 | 每次提交 | 自动 |
| Merge   | E2E 测试 | 合并时   | 自动 |
| Nightly | 性能测试 | 每晚     | 定时 |
| Release | 全量测试 | 发布时   | 手动 |

### 7.3 测试报告

- 覆盖率趋势图
- 测试通过率
- 失败测试分类
- 性能基线对比

<!-- ============ 文档分隔线：031-devops/017-Troubleshooting.md ============ -->

## 1. 故障排查方法论

### 1.1 科学方法

1. **观察**：收集现象和数据
2. **假设**：提出可能的原因
3. **预测**：假设成立时的预期结果
4. **实验**：验证假设
5. **分析**：对比预测与实际结果

### 1.2 二分法

通过逐步缩小范围定位问题：

```
整个系统 → 哪个服务？→ 哪个模块？→ 哪个函数？→ 哪行代码？
```

### 1.3 RED 方法

对每个服务检查：

- **Rate（速率）**：请求量是否异常
- **Errors（错误）**：错误率是否升高
- **Duration（延迟）**：响应时间是否变长

### 1.4 排查流程

```
1. 确认问题：复现、范围、影响
2. 收集信息：日志、指标、追踪
3. 定位范围：网络/系统/应用/数据
4. 分析原因：根因分析
5. 实施修复：临时/永久
6. 验证恢复：确认服务正常
7. 复盘总结：改进措施
```

## 2. 系统诊断工具

### 2.1 进程诊断

```bash
# 进程状态
ps aux | grep myapp
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem

# 进程树
pstree -p <pid>

# 打开的文件
lsof -p <pid>
lsof -i :8080          # 监听8080端口的进程

# 系统调用
strace -p <pid> -e trace=network
strace -p <pid> -c     # 统计

# 进程内存
cat /proc/<pid>/status | grep -E "Vm|Threads"
cat /proc/<pid>/smaps  # 详细内存映射
```

### 2.2 网络诊断

```bash
# 连接状态
ss -s                   # 连接概览
ss -tnp                 # TCP 连接
ss -tn state time-wait  # TIME_WAIT 连接

# 连通性
ping target
traceroute target
mtr target              # 持续追踪

# DNS
dig example.com
nslookup example.com
host example.com

# 抓包
tcpdump -i eth0 -nn port 80
tcpdump -i eth0 -w capture.pcap
tcpdump -i eth0 'tcp[tcpflags] & (tcp-rst|tcp-syn) != 0'

# HTTP 请求
curl -v https://example.com
curl -w "@curl-format.txt" -o /dev/null -s https://example.com
```

### 2.3 磁盘诊断

```bash
# 磁盘使用
df -h
du -sh /var/log/*
du -d1 -h / | sort -rh | head -20

# inode 使用
df -i

# I/O 统计
iostat -xz 1

# 大文件查找
find / -type f -size +100M -exec ls -lh {} \;

# 文件系统检查
fsck -n /dev/sda1       # 只检查不修复
```

## 3. 典型故障模式

### 3.1 CPU 飙高

**排查步骤**：

```bash
1. top -H -p <pid>     # 找到高 CPU 线程
2. printf "%x\n" <tid> # 线程ID转十六进制
3. jstack <pid> | grep <hex_tid>  # Java 线程栈
4. 或 perf record -g -p <pid>     # 生成火焰图
```

**常见原因**：

| 原因     | 特征       | 解决方案        |
| -------- | ---------- | --------------- |
| 死循环   | 单线程100% | 代码修复        |
| GC 频繁  | GC线程高   | 调整堆/优化对象 |
| 正则回溯 | CPU突增    | 优化正则        |
| 加密运算 | 持续高     | 硬件加速        |

### 3.2 内存泄漏

**排查步骤**：

```bash
1. 监控内存增长趋势
2. 生成堆转储：jmap -dump:format=b,file=heap.hprof <pid>
3. 分析堆转储：MAT 或 VisualVM
4. 找到占用最大的对象和引用链
```

**常见原因**：

| 原因             | 特征          | 解决方案           |
| ---------------- | ------------- | ------------------ |
| 集合未清理       | 内存持续增长  | 及时清理           |
| 缓存无上限       | 缓存越来越大  | LRU/大小限制       |
| ThreadLocal 泄漏 | 线程池场景    | 及时 remove        |
| 资源未关闭       | 文件/连接泄漏 | try-with-resources |

### 3.3 网络超时

**排查步骤**：

```bash
1. 确认超时是单向还是双向
2. 检查网络连通性：ping, traceroute
3. 检查连接状态：ss -tnp
4. 检查防火墙/安全组
5. 抓包分析：tcpdump
6. 检查对端服务状态
```

**常见原因**：

| 原因       | 特征         | 解决方案       |
| ---------- | ------------ | -------------- |
| 连接池耗尽 | 获取连接超时 | 增大连接池     |
| DNS 解析慢 | 首次请求慢   | DNS 缓存       |
| TCP 队列满 | SYN 被丢弃   | 增大 somaxconn |
| 对端慢     | 响应时间长   | 优化对端       |

### 3.4 磁盘满

**排查步骤**：

```bash
1. df -h 找到满的分区
2. du -d1 -h / | sort -rh | head -20
3. 找到大文件/日志
4. 检查已删除但未释放的文件：lsof | grep deleted
```

### 3.5 数据库慢查询

**排查步骤**：

```sql
-- MySQL 慢查询
SHOW PROCESSLIST;
SELECT * FROM information_schema.PROCESSLIST WHERE TIME > 5;

-- 查看执行计划
EXPLAIN ANALYZE SELECT ...;

-- 查看锁等待
SHOW ENGINE INNODB STATUS;
```

## 4. 应急响应

### 4.1 应急响应流程

```
发现故障 → 影响评估 → 通报升级 → 止血恢复 → 根因分析 → 改进预防
```

### 4.2 止血策略

| 策略 | 方法             | 影响           |
| ---- | ---------------- | -------------- |
| 回滚 | 部署上一版本     | 功能回退       |
| 降级 | 关闭非核心功能   | 部分功能不可用 |
| 限流 | 降低请求量       | 部分用户受影响 |
| 扩容 | 增加实例         | 成本增加       |
| 熔断 | 停止故障调用     | 功能降级       |
| 切流 | DNS/负载均衡切换 | 需要多机房     |

### 4.3 通报模板

```
【故障通报】
时间：2026-06-14 10:30
影响：用户登录服务不可用
范围：约30%用户受影响
原因：数据库连接池耗尽
状态：已恢复（10:45）
措施：增大连接池，添加监控告警
```

## 5. 根因分析（RCA）

### 5.1 5 Whys 方法

```
为什么登录失败？→ 数据库连接超时
为什么超时？→ 连接池耗尽
为什么耗尽？→ 慢查询占用连接
为什么慢查询？→ 缺少索引
为什么缺少索引？→ 新功能上线未加索引
```

### 5.2 鱼骨图

```mermaid
flowchart TD
    F[故障]
    F --> P[人员]
    F --> PR[流程]
    F --> T[技术]
    F --> E[环境]
    F --> D[数据]
    F --> TL[工具]
```

### 5.3 改进措施

| 类型     | 示例                   |
| -------- | ---------------------- |
| 技术改进 | 添加索引、增大连接池   |
| 流程改进 | 上线检查清单、代码审查 |
| 监控改进 | 添加告警、仪表盘       |
| 文档改进 | 更新运维手册           |

<!-- ============ 文档分隔线：031-devops/018-ContainerSecurity.md ============ -->

## 1. 容器安全概述

### 1.1 容器安全四层模型

```
应用代码安全
    ↓
容器镜像安全
    ↓
容器运行时安全
    ↓
宿主机/平台安全
```

### 1.2 安全原则

- 最小权限原则
- 防御纵深
- 不可变基础设施
- 零信任

## 2. 镜像安全

### 2.1 镜像扫描

```bash
# Trivy 扫描
trivy image nginx:latest
trivy image --severity HIGH,CRITICAL myapp:1.0
trivy image --ignore-unfixed myapp:1.0

# Grype 扫描
grype nginx:latest

# Docker Scout
docker scout cves nginx:latest
```

### 2.2 镜像签名与验证

```bash
# Cosign 签名
cosign sign --key cosign.key myregistry/myapp:1.0

# 验证签名
cosign verify --key cosign.pub myregistry/myapp:1.0

# K8s 中强制验证（Kyverno）
# 拒绝未签名镜像
```

### 2.3 安全基础镜像

| 基础镜像    | 大小  | 攻击面 | 适用场景     |
| ----------- | ----- | ------ | ------------ |
| ubuntu      | ~77MB | 大     | 需要完整环境 |
| debian-slim | ~80MB | 中     | 折中方案     |
| alpine      | ~5MB  | 小     | 精简环境     |
| distroless  | ~2MB  | 最小   | 仅需运行时   |
| scratch     | 0     | 无     | 静态编译     |

### 2.4 Dockerfile 安全最佳实践

```dockerfile
# 使用特定版本标签
FROM node:20.11-alpine3.19

# 创建非root用户
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 最小安装
RUN apk add --no-cache tini

# COPY 而非 ADD
COPY --chown=appuser:appgroup . /app

# 不以root运行
USER appuser

# 健康检查
HEALTHCHECK --interval=30s CMD wget -qO- http://localhost:8080/health || exit 1

# 使用 tini 作为入口
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", "server.js"]
```

## 3. 运行时安全

### 3.1 容器安全策略

```yaml
# Pod 安全标准（Pod Security Standards）
apiVersion: v1
kind: Pod
metadata:
  name: restricted-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: myapp:1.0
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
        runAsNonRoot: true
      resources:
        limits:
          memory: '512Mi'
          cpu: '500m'
```

### 3.2 三级安全策略

| 级别       | 说明         | 适用场景     |
| ---------- | ------------ | ------------ |
| Privileged | 无限制       | 系统组件     |
| Baseline   | 禁止明显提权 | 一般应用     |
| Restricted | 最严格       | 安全敏感应用 |

### 3.3 Seccomp 配置

限制容器可用的系统调用：

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [{ "names": ["read", "write", "exit", "sigreturn"], "action": "SCMP_ACT_ALLOW" }]
}
```

### 3.4 AppArmor / SELinux

**AppArmor 配置**：

```
#include <tunables/global>
profile docker-myapp flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>
  deny /etc/shadow r,
  deny /proc/*/mem rw,
  /app/** r,
  /tmp/** rw,
}
```

## 4. Kubernetes 安全

### 4.1 RBAC

```yaml
# 最小权限角色
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
  - apiGroups: ['']
    resources: ['pods']
    verbs: ['get', 'list', 'watch']
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
  - kind: ServiceAccount
    name: myapp
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### 4.2 NetworkPolicy

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: default
spec:
  podSelector: {}
  policyTypes:
    - Ingress
    - Egress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
spec:
  podSelector:
    matchLabels:
      app: backend
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: frontend
      ports:
        - port: 8080
```

### 4.3 Secret 加密

- 启用 K8s Secret 加密（EncryptionConfiguration）
- 使用外部密钥管理（Vault + External Secrets Operator）
- 审计 Secret 访问

### 4.4 准入控制

**OPA Gatekeeper**：

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
      validation:
        openAPIV3Schema:
          properties:
            labels:
              type: array
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        violation[{"msg": msg}] {
          provided := {label | input.review.object.metadata.labels[label]}
          required := {label | label := input.parameters.labels[_]}
          missing := required - provided
          count(missing) > 0
          msg := sprintf("Missing labels: %v", [missing])
        }
```

## 5. 安全监控

### 5.1 Falco

运行时安全监控：

```yaml
# Falco 规则
- rule: Terminal Shell in Container
  desc: A shell was spawned in a container
  condition: >
    spawned_process and container and
    proc.name in (bash, zsh, sh) and
    not proc.pname in (docker-entrypoint)
  output: 'Shell spawned in container (user=%user.name container=%container.name shell=%proc.name)'
  priority: WARNING
```

### 5.2 审计日志

```yaml
# K8s 审计策略
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  - level: RequestResponse
    resources:
      - group: ''
        resources: ['secrets']
  - level: Metadata
    resources:
      - group: ''
        resources: ['pods', 'services']
    verbs: ['delete']
```

## 6. 合规与认证

### 6.1 CIS Benchmark

```bash
# kube-bench 检查
kube-bench run --targets master,node
kube-bench run --benchmark cis-1.8
```

### 6.2 SOC2 / ISO27001

容器环境合规要求：

- 镜像来源可信
- 漏洞扫描和修复
- 访问控制和审计
- 加密传输和存储
- 变更管理流程

<!-- ============ 文档分隔线：031-devops/019-GitOpsCD.md ============ -->

## 1. GitOps 原则

### 1.1 核心原则

1. **声明式**：系统描述是声明式的
2. **版本控制**：期望状态存储在 Git
3. **自动拉取**：自动应用期望状态
4. **持续协调**：持续确保一致性

### 1.2 Push vs Pull 模式

| 模式 | 触发方式       | 安全性       | 适用场景   |
| ---- | -------------- | ------------ | ---------- |
| Push | CI 推送部署    | 需要凭证     | 传统 CI/CD |
| Pull | Agent 拉取变更 | 凭证在集群内 | GitOps     |

## 2. ArgoCD

### 2.1 核心概念

```mermaid
flowchart LR
    G[Git 仓库] --> A[ArgoCD] --> K[Kubernetes 集群]
    K -.->|状态同步| G
```

### 2.2 Application 配置

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/k8s-manifests.git
    targetRevision: main
    path: overlays/production
    helm:
      valueFiles:
        - values-prod.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: myapp
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - PrunePropagationPolicy=foreground
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### 2.3 App of Apps 模式

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: apps
  namespace: argocd
spec:
  source:
    repoURL: https://github.com/org/argocd-apps.git
    path: apps
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
```

### 2.4 ApplicationSet

多集群/多环境自动生成 Application：

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: myapp
spec:
  generators:
    - git:
        repoURL: https://github.com/org/k8s-manifests.git
        files:
          - path: 'clusters/**/config.json'
  template:
    metadata:
      name: '{{cluster_name}}-myapp'
    spec:
      source:
        repoURL: https://github.com/org/k8s-manifests.git
        targetRevision: '{{branch}}'
        path: overlays/{{overlay}}
      destination:
        server: '{{server}}'
        namespace: myapp
```

## 3. Flux

### 3.1 核心组件

| 组件                    | 功能                 |
| ----------------------- | -------------------- |
| source-controller       | 管理 Git/Helm/OCI 源 |
| kustomize-controller    | Kustomize 构建       |
| helm-controller         | Helm 发布            |
| notification-controller | 通知                 |
| image-automation        | 自动镜像更新         |

### 3.2 基本配置

```yaml
# Git 仓库源
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/org/k8s-manifests.git
  ref:
    branch: main
---
# Kustomize 部署
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 5m
  sourceRef:
    kind: GitRepository
    name: myapp
  path: ./overlays/production
  prune: true
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: myapp
      namespace: default
```

### 3.3 自动镜像更新

```yaml
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageRepository
metadata:
  name: myapp
spec:
  image: registry/myapp
  interval: 1m
---
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: myapp
spec:
  imageRepositoryRef:
    name: myapp
  policy:
    semver:
      range: '^1.x'
---
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImageUpdateAutomation
metadata:
  name: myapp
spec:
  sourceRef:
    kind: GitRepository
    name: myapp
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        name: fluxbot
        email: fluxbot@example.com
      messageTemplate: 'Update image to {{ .Image }}'
    push:
      branch: main
  interval: 1m
```

## 4. 渐进式交付

### 4.1 Argo Rollouts

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: myapp
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 10
        - pause: { duration: 5m }
        - setWeight: 30
        - pause: { duration: 5m }
        - setWeight: 50
        - pause: { duration: 5m }
        - setWeight: 80
        - pause: { duration: 5m }
      canaryService: myapp-canary
      stableService: myapp-stable
      trafficRouting:
        istio:
          virtualServices:
            - name: myapp-vsvc
              routes:
                - primary
      analysis:
        templates:
          - templateName: success-rate
        args:
          - name: service-name
            value: myapp-canary
---
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  args:
    - name: service-name
  metrics:
    - name: success-rate
      provider:
        prometheus:
          address: http://prometheus:9090
          query: |
            sum(rate(http_requests_total{service="{{args.service-name}}",status!~"5.."}[5m]))
            /
            sum(rate(http_requests_total{service="{{args.service-name}}"}[5m]))
      successCondition: result[0] >= 0.99
      interval: 30s
      count: 10
```

### 4.2 Flagger

```yaml
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: myapp
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  service:
    port: 8080
  analysis:
    interval: 1m
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
      - name: request-success-rate
        thresholdRange:
          min: 99
        interval: 1m
      - name: request-duration
        thresholdRange:
          max: 500
        interval: 1m
    webhooks:
      - name: load-test
        url: http://flagger-loadtester/
        timeout: 5s
        metadata:
          cmd: 'hey -z 1m -q 10 -c 2 http://myapp:8080/'
```

### 4.3 发布策略对比

| 策略     | 流量切换 | 回滚速度 | 资源开销  | 风险 |
| -------- | -------- | -------- | --------- | ---- |
| 滚动更新 | 逐步     | 中       | 低        | 中   |
| 蓝绿部署 | 一次性   | 快       | 高（2倍） | 低   |
| 金丝雀   | 渐进     | 快       | 中        | 低   |
| 影子测试 | 复制流量 | 即时     | 高        | 最低 |

## 5. 多环境管理

### 5.1 环境隔离

```mermaid
flowchart TD
    T0["Git 仓库结构："]
    T1["base/                    # 基础配置"]
    T2["kustomization.yaml"]
    T3["deployment.yaml"]
    T4["overlays/"]
    T5["development/         # 开发环境"]
    T6["staging/             # 预发布"]
    T7["production/          # 生产"]
    T8["apps/"]
    T9["dev.yaml             # ArgoCD Application"]
    T10["staging.yaml"]
    T11["prod.yaml"]
    T0 --> T1
    T3 --> T4
    T7 --> T8
    T8 --> T9
    T8 --> T10
    T8 --> T11
```

### 5.2 促销流程（Promotion）

```mermaid
flowchart LR
    D[开发环境] -->|合并到 dev 分支| S[预发布环境]
    S -->|合并到 staging 分支| P[生产环境]
    P -->|合并到 main 分支| P
```

### 5.3 配置差异管理

| 方法               | 说明       | 适用场景   |
| ------------------ | ---------- | ---------- |
| Kustomize overlays | 覆盖差异   | 简单差异   |
| Helm values        | 值文件差异 | Helm 项目  |
| 环境变量           | 运行时注入 | 通用       |
| 配置中心           | 动态配置   | 需要热更新 |

<!-- ============ 文档分隔线：031-devops/020-MonitorAndAlert.md ============ -->

## 1. 监控体系

### 1.1 监控层次

```
业务指标（订单量、转化率）
    ↓
应用指标（QPS、延迟、错误率）
    ↓
系统指标（CPU、内存、磁盘、网络）
    ↓
基础设施（服务器、网络、存储）
```

### 1.2 USE/RED 方法

**USE（系统资源）**：

- Utilization：利用率
- Saturation：饱和度
- Errors：错误

**RED（服务）**：

- Rate：请求速率
- Errors：错误率
- Duration：延迟

## 2. Prometheus

### 2.1 数据模型

Prometheus 使用时间序列数据：

```
metric_name{label1="value1", label2="value2"} value timestamp
```

**四种指标类型**：

| 类型      | 说明           | 示例                          |
| --------- | -------------- | ----------------------------- |
| Counter   | 单调递增计数器 | http_requests_total           |
| Gauge     | 可增减的值     | cpu_usage_percent             |
| Histogram | 分布统计       | http_request_duration_seconds |
| Summary   | 分位数统计     | http_request_duration_seconds |

### 2.2 PromQL

```promql
# 即时查询
http_requests_total{method="GET", status="200"}

# 范围查询
http_requests_total[5m]

# 速率
rate(http_requests_total[5m])

# 聚合
sum(rate(http_requests_total[5m])) by (service)

# 分位数
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# 预测
predict_linear(disk_free_bytes[1h], 4*3600)

# 常用查询
# CPU 使用率
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 内存使用率
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# 磁盘使用率
(1 - (node_filesystem_avail_bytes{fstype!~"tmpfs"} / node_filesystem_size_bytes)) * 100
```

### 2.3 服务发现

```yaml
# Kubernetes 服务发现
scrape_configs:
  - job_name: kubernetes-pods
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
```

### 2.4 记录规则

```yaml
groups:
  - name: service_rules
    interval: 30s
    rules:
      - record: service:request_rate:5m
        expr: sum(rate(http_requests_total[5m])) by (service)
      - record: service:error_rate:5m
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
          /
          sum(rate(http_requests_total[5m])) by (service)
```

## 3. Grafana

### 3.1 仪表盘设计

| 层级     | 内容           | 受众   |
| -------- | -------------- | ------ |
| 概览     | 关键指标、状态 | 管理层 |
| 服务     | QPS/延迟/错误  | 开发者 |
| 基础设施 | CPU/内存/磁盘  | 运维   |
| 调试     | 详细指标、日志 | 排查   |

### 3.2 面板类型

| 类型        | 适用场景 |
| ----------- | -------- |
| Stat        | 单值展示 |
| Time series | 趋势图   |
| Bar gauge   | 对比     |
| Table       | 表格数据 |
| Heatmap     | 分布图   |
| Log         | 日志浏览 |

### 3.3 告警规则

```yaml
# Grafana 告警
apiVersion: 1
groups:
  - orgId: 1
    name: service_alerts
    rules:
      - uid: high_error_rate
        title: High Error Rate
        condition: C
        data:
          - refId: A
            relativeTimeRange:
              from: 300
            datasourceUid: prometheus
            model:
              expr: sum(rate(http_requests_total{status=~"5.."}[5m])) by (service) / sum(rate(http_requests_total[5m])) by (service)
          - refId: C
            reducer: last
            expression: A
            type: reduce
        noDataState: OK
        execErrState: Alerting
        for: 5m
```

## 4. 告警设计

### 4.1 告警分级

| 级别 | 响应时间 | 通知方式  | 示例           |
| ---- | -------- | --------- | -------------- |
| P1   | 5分钟    | 电话+短信 | 服务完全不可用 |
| P2   | 15分钟   | 短信+IM   | 部分功能异常   |
| P3   | 1小时    | IM        | 性能下降       |
| P4   | 24小时   | 邮件      | 非紧急问题     |

### 4.2 告警原则

- **可操作性**：每条告警都有明确的行动
- **低噪音**：避免误报和重复告警
- **及时性**：在影响用户前告警
- **上下文丰富**：包含足够诊断信息

### 4.3 告警规则示例

```yaml
# Prometheus 告警规则
groups:
  - name: service_alerts
    rules:
      - alert: HighErrorRate
        expr: |
          sum(rate(http_requests_total{status=~"5.."}[5m])) by (service)
          /
          sum(rate(http_requests_total[5m])) by (service) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: 'High error rate on {{ $labels.service }}'
          description: 'Error rate is {{ $value | humanizePercentage }} for the last 5 minutes'

      - alert: HighLatency
        expr: |
          histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service))
          > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: 'High P99 latency on {{ $labels.service }}'
          description: 'P99 latency is {{ $value }}s'
```

### 4.4 告警抑制与静默

```yaml
# 抑制规则：P1 告警抑制同服务的 P2 告警
inhibit_rules:
  - source_match:
      severity: critical
    target_match:
      severity: warning
    equal: [service, cluster]
```

## 5. SLI/SLO

### 5.1 概念

| 概念 | 含义         | 示例         |
| ---- | ------------ | ------------ |
| SLI  | 服务水平指标 | 可用性、延迟 |
| SLO  | 服务水平目标 | 99.9% 可用性 |
| SLA  | 服务水平协议 | 合同约束     |

### 5.2 错误预算

$$\text{错误预算} = 1 - \text{SLO}$$

99.9% SLO 的月度错误预算：

$$30 \times 24 \times 60 \times 0.001 = 43.2 \text{ 分钟}$$

### 5.3 SLO 燃尽率

```promql
# 30天窗口的错误预算消耗率
1 - (
  sum(rate(http_requests_total{status!~"5.."}[30d]))
  /
  sum(rate(http_requests_total[30d]))
)
```

## 6. On-Call 实践

### 6.1 On-Call 轮值

- 主备双人值班
- 轮换周期：1周
- 交接会议：每周一次

### 6.2 事故管理

```
发现 → 响应 → 止血 → 恢复 → 复盘
```

### 6.3 无指责复盘

- 关注系统和流程
- 不追究个人责任
- 产出可操作的改进项

<!-- ============ 文档分隔线：031-devops/021-NetworkSecurityAdvanced.md ============ -->

## 1. 零信任网络

### 1.1 零信任原则

- 永不信任，始终验证
- 最小权限访问
- 假设已被入侵
- 微分段隔离
- 持续监控和验证

### 1.2 BeyondCorp 模型

Google BeyondCorp 架构：

```
用户/设备 → 访问代理 → 信任评估 → 资源
              ↑
         身份/设备/上下文
```

核心组件：

| 组件       | 功能               |
| ---------- | ------------------ |
| 信任代理   | 评估设备和用户信任 |
| 访问代理   | 执行访问策略       |
| 身份提供者 | 认证和授权         |
| 设备清单   | 设备注册和状态     |

### 1.3 零信任实现

**Tailscale**：基于 WireGuard 的零信任网络：

```bash
# 安装
curl -fsSL https://tailscale.com/install.sh | sh

# 认证
tailscale up

# 查看状态
tailscale status

# 访问内部服务
curl http://internal-service:8080
```

**Cloudflare Access**：

```
用户 → Cloudflare Edge → 身份验证 → 内部应用
```

## 2. 证书管理

### 2.1 cert-manager

Kubernetes 证书管理工具：

```yaml
# 安装
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.0/cert-manager.yaml

# ClusterIssuer（Let's Encrypt）
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      - http01:
          ingress:
            class: nginx
```

```yaml
# 证书签发
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: myapp-cert
spec:
  secretName: myapp-tls
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  dnsNames:
    - myapp.example.com
```

### 2.2 内部 CA

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ca-issuer
spec:
  ca:
    secretName: ca-key-pair
---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: internal-cert
spec:
  secretName: internal-tls
  issuerRef:
    name: ca-issuer
    kind: ClusterIssuer
  dnsNames:
    - myapp.internal
  duration: 720h # 30天
  renewBefore: 168h # 提前7天续签
```

### 2.3 证书轮换

- 自动续签：cert-manager 在到期前自动续签
- 滚动更新：新证书生效后 Pod 自动重启
- mTLS 证书：服务网格自动轮换

## 3. 安全自动化

### 3.1 安全扫描流水线

```yaml
# CI/CD 安全扫描
stages:
  - test
  - security
  - deploy

sast:
  stage: security
  image: returntocorp/semgrep
  script:
    - semgrep --config auto --json -o sast-results.json .
  artifacts:
    paths:
      - sast-results.json

container-scan:
  stage: security
  image: aquasec/trivy
  script:
    - trivy image --exit-code 1 --severity HIGH,CRITICAL $IMAGE

secret-scan:
  stage: security
  image: zricethezav/gitleaks
  script:
    - gitleaks detect --source . --report-format json --report-path leaks.json
```

### 3.2 安全策略即代码

**Open Policy Agent（OPA）**：

```rego
# 禁止特权容器
package kubernetes.admission

deny[msg] {
    input.request.kind.kind == "Pod"
    container := input.request.object.spec.containers[_]
    container.securityContext.privileged
    msg := sprintf("Privileged container not allowed: %v", [container.name])
}

deny[msg] {
    input.request.kind.kind == "Pod"
    container := input.request.object.spec.containers[_]
    not container.resources.limits.memory
    msg := sprintf("Memory limit required: %v", [container.name])
}
```

### 3.3 安全合规自动化

| 检查项   | 工具                | 频率     |
| -------- | ------------------- | -------- |
| 镜像漏洞 | Trivy/Grype         | 每次构建 |
| 代码漏洞 | Semgrep/SonarQube   | 每次提交 |
| 密钥泄露 | GitLeaks/TruffleHog | 每次提交 |
| K8s 安全 | kube-bench/Polaris  | 每日     |
| 依赖漏洞 | Dependabot/Snyk     | 每日     |
| 合规检查 | InSpec/OPA          | 每周     |

## 4. 网络策略与隔离

### 4.1 Kubernetes 网络策略

```yaml
# 默认拒绝所有入站
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
    - Ingress
---
# 允许特定服务访问
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-to-db
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: database
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: api
      ports:
        - port: 5432
```

### 4.2 服务网格安全

Istio 安全策略：

```yaml
# 严格 mTLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
---
# 授权策略
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: api-to-db
  namespace: production
spec:
  selector:
    matchLabels:
      app: database
  action: ALLOW
  rules:
    - from:
        - source:
            principals: ['cluster.local/ns/production/sa/api']
      to:
        - operation:
            methods: ['GET', 'POST']
            paths: ['/api/*']
```

## 5. 安全事件响应

### 5.1 安全事件分级

| 级别 | 描述                 | 响应时间 |
| ---- | -------------------- | -------- |
| P1   | 数据泄露、系统被入侵 | 立即     |
| P2   | 漏洞被利用、异常访问 | 1小时    |
| P3   | 可疑行为、策略违规   | 4小时    |
| P4   | 安全发现、改进建议   | 24小时   |

### 5.2 应急响应流程

```
1. 检测：安全监控发现异常
2. 遏制：隔离受影响系统
3. 根除：消除威胁
4. 恢复：恢复服务
5. 复盘：改进安全措施
```

### 5.3 取证分析

```bash
# 容器取证
docker commit <container> forensic-image
docker save forensic-image -o forensic.tar

# 日志收集
kubectl logs <pod> --previous > crash.log
journalctl -u docker --since "1 hour ago"

# 网络取证
tcpdump -i any -w capture.pcap host <suspicious-ip>
```

<!-- ============ 文档分隔线：031-devops/022-DatabaseOps.md ============ -->

## 1. 备份与恢复

### 1.1 备份策略

| 策略     | 说明           | 恢复时间 | 存储开销 |
| -------- | -------------- | -------- | -------- |
| 全量备份 | 备份所有数据   | 快       | 大       |
| 增量备份 | 仅备份变更     | 中       | 小       |
| 差异备份 | 相对全量的变更 | 中       | 中       |
| 逻辑备份 | SQL 导出       | 慢       | 中       |
| 物理备份 | 文件拷贝       | 快       | 大       |

### 1.2 MySQL 备份

```bash
# mysqldump 逻辑备份
mysqldump -u root -p --all-databases --single-transaction --routines --triggers > full_backup.sql

# 单库备份
mysqldump -u root -p mydb > mydb_backup.sql

# 增量备份（基于 binlog）
mysqladmin flush-logs
cp /var/lib/mysql/mysql-bin.* /backup/

# XtraBackup 物理备份
xtrabackup --backup --target-dir=/backup/full
xtrabackup --backup --target-dir=/backup/inc1 --incremental-basedir=/backup/full
```

### 1.3 恢复操作

```bash
# 逻辑恢复
mysql -u root -p < full_backup.sql

# 时间点恢复
mysqlbinlog --start-datetime="2026-06-14 10:00:00" \
            --stop-datetime="2026-06-14 10:30:00" \
            mysql-bin.000123 | mysql -u root -p

# XtraBackup 恢复
xtrabackup --prepare --target-dir=/backup/full
xtrabackup --copy-back --target-dir=/backup/full
```

### 1.4 备份验证

```bash
# 定期验证备份可恢复性
mysql -u root -p -e "CREATE DATABASE backup_test"
mysql -u root -p backup_test < backup.sql
mysql -u root -p backup_test -e "SHOW TABLES; SELECT COUNT(*) FROM users"
mysql -u root -p -e "DROP DATABASE backup_test"
```

## 2. 主从复制

### 2.1 MySQL 主从复制

```
主库 → binlog → 从库（IO线程）→ relay log → 从库（SQL线程）→ 数据
```

**配置主库**：

```ini
[mysqld]
server-id = 1
log-bin = mysql-bin
binlog-format = ROW
gtid-mode = ON
enforce-gtid-consistency = ON
```

**配置从库**：

```ini
[mysqld]
server-id = 2
relay-log = relay-bin
read-only = ON
super-read-only = ON
```

**建立复制**：

```sql
-- 从库执行
CHANGE MASTER TO
  MASTER_HOST='master',
  MASTER_USER='repl',
  MASTER_PASSWORD='password',
  MASTER_AUTO_POSITION=1;
START SLAVE;
```

### 2.2 复制延迟监控

```sql
-- 查看复制状态
SHOW SLAVE STATUS\G

-- 关键指标
Seconds_Behind_Master    # 延迟秒数
Slave_IO_Running         # IO 线程状态
Slave_SQL_Running        # SQL 线程状态
Retrieved_Gtid_Set       # 已接收的 GTID
Executed_Gtid_Set        # 已执行的 GTID
```

### 2.3 延迟优化

| 方法       | 说明                              |
| ---------- | --------------------------------- |
| 多线程复制 | slave_parallel_workers            |
| 组提交     | binlog_group_commit               |
| 半同步复制 | rpl_semi_sync                     |
| 并行复制   | slave_parallel_type=LOGICAL_CLOCK |

## 3. 读写分离

### 3.1 读写分离架构

```
客户端 → 代理层 → 主库（写）
                 → 从库1（读）
                 → 从库2（读）
                 → 从库3（读）
```

### 3.2 代理方案

| 代理           | 特点                   |
| -------------- | ---------------------- |
| ProxySQL       | 功能丰富，支持查询缓存 |
| MySQL Router   | Oracle 官方            |
| MyCat          | 国产，功能全面         |
| ShardingSphere | Apache 项目            |

### 3.3 ProxySQL 配置

```sql
-- 添加后端服务器
INSERT INTO mysql_servers (hostgroup_id, hostname, port, weight)
VALUES (0, 'master', 3306, 1),    -- 写组
       (1, 'slave1', 3306, 1),    -- 读组
       (1, 'slave2', 3306, 1);

-- 配置路由规则
INSERT INTO mysql_query_rules (rule_id, active, match_pattern, destination_hostgroup, apply)
VALUES (1, 1, '^SELECT.*FOR UPDATE', 0, 1),  -- 写走主库
       (2, 1, '^SELECT', 1, 1);               -- 读走从库
```

## 4. 分库分表

### 4.1 分片策略

| 策略       | 说明          | 优点     | 缺点     |
| ---------- | ------------- | -------- | -------- |
| 范围分片   | 按 ID 范围    | 扩展方便 | 热点问题 |
| 哈希分片   | 按 key 哈希   | 分布均匀 | 扩展困难 |
| 一致性哈希 | 哈希+虚拟节点 | 扩展方便 | 实现复杂 |
| 查找表     | 映射表路由    | 灵活     | 额外查询 |

### 4.2 ShardingSphere 配置

```yaml
dataSources:
  ds_0:
    url: jdbc:mysql://host0:3306/db_0
  ds_1:
    url: jdbc:mysql://host1:3306/db_1

shardingRule:
  tables:
    t_order:
      actualDataNodes: ds_${0..1}.t_order_${0..15}
      databaseStrategy:
        standard:
          shardingColumn: user_id
          shardingAlgorithmName: order_db_mod
      tableStrategy:
        standard:
          shardingColumn: order_id
          shardingAlgorithmName: order_table_mod

  shardingAlgorithms:
    order_db_mod:
      type: MOD
      props:
        sharding-count: 2
    order_table_mod:
      type: MOD
      props:
        sharding-count: 16
```

### 4.3 分布式 ID

| 方案     | 原理           | 优点         | 缺点         |
| -------- | -------------- | ------------ | ------------ |
| UUID     | 随机生成       | 简单         | 无序，索引差 |
| 雪花算法 | 时间+机器+序列 | 有序，高性能 | 时钟依赖     |
| 号段模式 | 预分配号段     | 简单         | 不连续       |
| Redis    | INCR           | 简单         | 依赖 Redis   |

**雪花算法 ID 结构**：

```
0 | 00000000000000000000000000000000000000000 | 00000 | 00000 | 000000000000
  │                  41位时间戳               │ 5位DC │ 5位机器│  12位序列
```

## 5. 数据迁移

### 5.1 在线迁移工具

**gh-ost（GitHub）**：

```bash
gh-ost \
  --host=master \
  --database=mydb \
  --table=users \
  --alter="ADD COLUMN age INT" \
  --allow-on-master \
  --execute
```

**pt-online-schema-change（Percona）**：

```bash
pt-online-schema-change \
  --host=master \
  --user=root \
  --alter="ADD INDEX idx_email (email)" \
  D=mydb,t=users \
  --execute
```

### 5.2 迁移流程

```
1. 创建影子表（新结构）
2. 在影子表上建立触发器（同步增量变更）
3. 分批拷贝历史数据
4. 验证数据一致性
5. 原子切换表名
6. 清理旧表
```

### 5.3 跨库迁移

```bash
# 使用 DataX 迁移
python datax.py migration.json

# 使用 Canal 监听 binlog 实时同步
canal.instance.master.address=source:3306
canal.instance.filter.regex=source_db\\..*
```

## 6. 数据库巡检

### 6.1 巡检清单

| 检查项   | 方法                      |
| -------- | ------------------------- |
| 连接数   | SHOW PROCESSLIST          |
| 慢查询   | 慢查询日志                |
| 锁等待   | SHOW ENGINE INNODB STATUS |
| 表空间   | information_schema.TABLES |
| 索引使用 | sys.schema_unused_indexes |
| 主从延迟 | SHOW SLAVE STATUS         |
| 磁盘空间 | df -h                     |
| 备份状态 | 验证备份文件              |

### 6.2 自动巡检脚本

```bash
#!/bin/bash
# MySQL 巡检脚本

echo "=== 连接数 ==="
mysql -e "SHOW STATUS LIKE 'Threads_connected'"
mysql -e "SHOW STATUS LIKE 'Max_used_connections'"

echo "=== 慢查询 ==="
mysql -e "SHOW STATUS LIKE 'Slow_queries'"

echo "=== InnoDB 状态 ==="
mysql -e "SHOW ENGINE INNODB STATUS\G" | grep -A5 "TRANSACTIONS"

echo "=== 主从状态 ==="
mysql -e "SHOW SLAVE STATUS\G" | grep -E "Slave_IO_Running|Slave_SQL_Running|Seconds_Behind"
```

<!-- ============ 文档分隔线：031-devops/023-DockerfileMultiBuild.md ============ -->

## 1. 多阶段构建原理

### 1.1 为什么需要多阶段构建

为什么需要多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍为什么需要多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- 为什么需要多阶段构建的定义与核心原理
- 为什么需要多阶段构建的实现方式与技术细节
- 为什么需要多阶段构建在实际场景中的应用与最佳实践
- 为什么需要多阶段构建的常见问题与解决方案

为什么需要多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 FROM ... AS 语法

FROM ... AS 语法是Dockerfile多阶段构建的重要组成部分。本节详细介绍FROM ... AS 语法的核心概念、工作原理和实际应用。

**关键要点**：

- FROM ... AS 语法的定义与核心原理
- FROM ... AS 语法的实现方式与技术细节
- FROM ... AS 语法在实际场景中的应用与最佳实践
- FROM ... AS 语法的常见问题与解决方案

FROM ... AS 语法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 实战示例

### 2.1 Go 应用多阶段构建

Go 应用多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍Go 应用多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- Go 应用多阶段构建的定义与核心原理
- Go 应用多阶段构建的实现方式与技术细节
- Go 应用多阶段构建在实际场景中的应用与最佳实践
- Go 应用多阶段构建的常见问题与解决方案

Go 应用多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Node.js 应用多阶段构建

Node.js 应用多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍Node.js 应用多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- Node.js 应用多阶段构建的定义与核心原理
- Node.js 应用多阶段构建的实现方式与技术细节
- Node.js 应用多阶段构建在实际场景中的应用与最佳实践
- Node.js 应用多阶段构建的常见问题与解决方案

Node.js 应用多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Java 应用多阶段构建

Java 应用多阶段构建是Dockerfile多阶段构建的重要组成部分。本节详细介绍Java 应用多阶段构建的核心概念、工作原理和实际应用。

**关键要点**：

- Java 应用多阶段构建的定义与核心原理
- Java 应用多阶段构建的实现方式与技术细节
- Java 应用多阶段构建在实际场景中的应用与最佳实践
- Java 应用多阶段构建的常见问题与解决方案

Java 应用多阶段构建在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 镜像优化技巧

### 3.1 选择基础镜像

选择基础镜像是Dockerfile多阶段构建的重要组成部分。本节详细介绍选择基础镜像的核心概念、工作原理和实际应用。

**关键要点**：

- 选择基础镜像的定义与核心原理
- 选择基础镜像的实现方式与技术细节
- 选择基础镜像在实际场景中的应用与最佳实践
- 选择基础镜像的常见问题与解决方案

选择基础镜像在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 利用缓存

利用缓存是Dockerfile多阶段构建的重要组成部分。本节详细介绍利用缓存的核心概念、工作原理和实际应用。

**关键要点**：

- 利用缓存的定义与核心原理
- 利用缓存的实现方式与技术细节
- 利用缓存在实际场景中的应用与最佳实践
- 利用缓存的常见问题与解决方案

利用缓存在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 .dockerignore

.dockerignore是Dockerfile多阶段构建的重要组成部分。本节详细介绍.dockerignore的核心概念、工作原理和实际应用。

**关键要点**：

- .dockerignore的定义与核心原理
- .dockerignore的实现方式与技术细节
- .dockerignore在实际场景中的应用与最佳实践
- .dockerignore的常见问题与解决方案

.dockerignore在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 安全基础镜像

安全基础镜像是Dockerfile多阶段构建的重要组成部分。本节详细介绍安全基础镜像的核心概念、工作原理和实际应用。

**关键要点**：

- 安全基础镜像的定义与核心原理
- 安全基础镜像的实现方式与技术细节
- 安全基础镜像在实际场景中的应用与最佳实践
- 安全基础镜像的常见问题与解决方案

安全基础镜像在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 非 root 用户

非 root 用户是Dockerfile多阶段构建的重要组成部分。本节详细介绍非 root 用户的核心概念、工作原理和实际应用。

**关键要点**：

- 非 root 用户的定义与核心原理
- 非 root 用户的实现方式与技术细节
- 非 root 用户在实际场景中的应用与最佳实践
- 非 root 用户的常见问题与解决方案

非 root 用户在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 健康检查

健康检查是Dockerfile多阶段构建的重要组成部分。本节详细介绍健康检查的核心概念、工作原理和实际应用。

**关键要点**：

- 健康检查的定义与核心原理
- 健康检查的实现方式与技术细节
- 健康检查在实际场景中的应用与最佳实践
- 健康检查的常见问题与解决方案

健康检查在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## FROM 基础镜像

**基本写法：指定基础镜像**
`FROM <镜像>[:<标签>]`
```dockerfile
# 使用 nginx 作为基础镜像
FROM nginx:1.25
```

**基本写法：多阶段构建**
`FROM <镜像> AS <阶段名>`
```dockerfile
# 第一阶段构建
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp
```

---

## RUN 执行命令

**基本写法：执行 shell 命令**
`RUN <命令>`
```dockerfile
# 安装 nginx
RUN apt-get update && apt-get install -y nginx
```

**基本写法：exec 形式**
`RUN ["<可执行文件>", "<参数1>", "<参数2>"]`
```dockerfile
# 使用 exec 形式执行
RUN ["npm", "install", "--production"]
```

**基本写法：合并多条命令**
`RUN <命令1> && <命令2> && <命令3>`
```dockerfile
# 合并命令减少镜像层
RUN apt-get update \
    && apt-get install -y curl vim \
    && rm -rf /var/lib/apt/lists/*
```

---

## CMD 容器默认命令

**基本写法：shell 形式**
`CMD <命令>`
```dockerfile
# 默认启动 nginx
CMD nginx -g "daemon off;"
```

**基本写法：exec 形式（推荐）**
`CMD ["<可执行文件>", "<参数1>", "<参数2>"]`
```dockerfile
# exec 形式启动 nginx
CMD ["nginx", "-g", "daemon off;"]
```

**基本写法：作为 ENTRYPOINT 参数**
`CMD ["<参数1>", "<参数2>"]`
```dockerfile
# 给 ENTRYPOINT 提供默认参数
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

---

## ENTRYPOINT 入口点

**基本写法：固定执行命令**
`ENTRYPOINT ["<可执行文件>", "<参数>"]`
```dockerfile
# 固定入口点为 app.py
ENTRYPOINT ["python", "app.py"]
```

**基本写法：shell 形式**
`ENTRYPOINT <命令>`
```dockerfile
# shell 形式入口点
ENTRYPOINT python app.py
```

---

## COPY 复制文件

**基本写法：复制文件到镜像**
`COPY <源路径> <目标路径>`
```dockerfile
# 复制当前目录文件到镜像
COPY . /app
```

**基本写法：复制多个文件**
`COPY <文件1> <文件2> <目标目录>`
```dockerfile
# 复制多个配置文件
COPY package.json package-lock.json /app/
```

**基本写法：通配符匹配**
`COPY <通配符> <目标路径>`
```dockerfile
# 复制所有 .json 文件
COPY *.json /app/config/
```

---

## ADD 高级复制

**基本写法：复制并解压 tar 文件**
`ADD <文件> <目标路径>`
```dockerfile
# 自动解压 tar.gz 文件
ADD app.tar.gz /opt/
```

**基本写法：从 URL 下载文件**
`ADD <URL> <目标路径>`
```dockerfile
# 从 URL 下载文件
ADD https://example.com/file.zip /tmp/
```

---

## WORKDIR 工作目录

**基本写法：设置工作目录**
`WORKDIR <路径>`
```dockerfile
# 设置工作目录为 /app
WORKDIR /app
```

**基本写法：相对路径切换**
`WORKDIR <相对路径>`
```dockerfile
# 在已有工作目录下切换
WORKDIR /app
WORKDIR src
```

---

## ENV 环境变量

**基本写法：设置环境变量**
`ENV <键>=<值>`
```dockerfile
# 设置 NODE_ENV 环境变量
ENV NODE_ENV=production
```

**基本写法：设置多个环境变量**
`ENV <键1>=<值1> <键2>=<值2>`
```dockerfile
# 设置多个环境变量
ENV NODE_ENV=production PORT=3000
```

---

## ARG 构建参数

**基本写法：定义构建参数**
`ARG <参数名>[=<默认值>]`
```dockerfile
# 定义 VERSION 构建参数
ARG VERSION=latest
FROM node:$VERSION
```

**基本写法：使用构建参数**
`ARG <参数名>`
```dockerfile
# 在 RUN 中使用构建参数
ARG BUILD_DATE
RUN echo "Build date: $BUILD_DATE" > /build-date.txt
```

---

## EXPOSE 声明端口

**基本写法：声明容器端口**
`EXPOSE <端口>[/<协议>]`
```dockerfile
# 声明 80 端口
EXPOSE 80
```

**基本写法：声明多个端口**
`EXPOSE <端口1> <端口2>`
```dockerfile
# 声明 HTTP 和 HTTPS 端口
EXPOSE 80 443
```

**基本写法：声明 UDP 端口**
`EXPOSE <端口>/udp`
```dockerfile
# 声明 UDP 端口
EXPOSE 53/udp
```

---

## VOLUME 数据卷

**基本写法：声明匿名数据卷**
`VOLUME <路径>`
```dockerfile
# 声明数据卷
VOLUME /data
```

**基本写法：声明多个数据卷**
`VOLUME ["<路径1>", "<路径2>"]`
```dockerfile
# 声明多个数据卷
VOLUME ["/data", "/logs"]
```

---

## USER 切换用户

**基本写法：指定运行用户**
`USER <用户名>[:<组>]`
```dockerfile
# 切换到 node 用户运行
USER node
```

**基本写法：使用 UID**
`USER <UID>[:<GID>]`
```dockerfile
# 使用 UID 切换用户
USER 1000:1000
```

---

## LABEL 标签

**基本写法：添加镜像标签**
`LABEL <键>=<值>`
```dockerfile
# 添加维护者标签
LABEL maintainer="dev@example.com"
```

**基本写法：添加多个标签**
`LABEL <键1>=<值1> <键2>=<值2>`
```dockerfile
# 添加多个元数据标签
LABEL version="1.0" description="My App" author="dev-team"
```

---

## HEALTHCHECK 健康检查

**基本写法：设置健康检查**
`HEALTHCHECK [选项] CMD <命令>`
```dockerfile
# 每 30 秒检查一次健康状态
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/ || exit 1
```

**基本写法：禁用健康检查**
`HEALTHCHECK NONE`
```dockerfile
# 禁用基础镜像的健康检查
HEALTHCHECK NONE
```

<!-- ============ 文档分隔线：031-devops/024-KubernetesCoreDetailed.md ============ -->

## 1. Pod 与 Deployment

### 1.1 Pod 生命周期

Pod 生命周期是Kubernetes核心资源详解的重要组成部分。本节详细介绍Pod 生命周期的核心概念、工作原理和实际应用。

**关键要点**：

- Pod 生命周期的定义与核心原理
- Pod 生命周期的实现方式与技术细节
- Pod 生命周期在实际场景中的应用与最佳实践
- Pod 生命周期的常见问题与解决方案

Pod 生命周期在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Deployment 滚动更新

Deployment 滚动更新是Kubernetes核心资源详解的重要组成部分。本节详细介绍Deployment 滚动更新的核心概念、工作原理和实际应用。

**关键要点**：

- Deployment 滚动更新的定义与核心原理
- Deployment 滚动更新的实现方式与技术细节
- Deployment 滚动更新在实际场景中的应用与最佳实践
- Deployment 滚动更新的常见问题与解决方案

Deployment 滚动更新在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Service 与 Ingress

### 2.1 Service 类型

Service 类型是Kubernetes核心资源详解的重要组成部分。本节详细介绍Service 类型的核心概念、工作原理和实际应用。

**关键要点**：

- Service 类型的定义与核心原理
- Service 类型的实现方式与技术细节
- Service 类型在实际场景中的应用与最佳实践
- Service 类型的常见问题与解决方案

Service 类型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Ingress 路由规则

Ingress 路由规则是Kubernetes核心资源详解的重要组成部分。本节详细介绍Ingress 路由规则的核心概念、工作原理和实际应用。

**关键要点**：

- Ingress 路由规则的定义与核心原理
- Ingress 路由规则的实现方式与技术细节
- Ingress 路由规则在实际场景中的应用与最佳实践
- Ingress 路由规则的常见问题与解决方案

Ingress 路由规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 配置与密钥

### 3.1 ConfigMap

ConfigMap是Kubernetes核心资源详解的重要组成部分。本节详细介绍ConfigMap的核心概念、工作原理和实际应用。

**关键要点**：

- ConfigMap的定义与核心原理
- ConfigMap的实现方式与技术细节
- ConfigMap在实际场景中的应用与最佳实践
- ConfigMap的常见问题与解决方案

ConfigMap在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Secret

Secret是Kubernetes核心资源详解的重要组成部分。本节详细介绍Secret的核心概念、工作原理和实际应用。

**关键要点**：

- Secret的定义与核心原理
- Secret的实现方式与技术细节
- Secret在实际场景中的应用与最佳实践
- Secret的常见问题与解决方案

Secret在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 有状态与弹性

### 4.1 StatefulSet

StatefulSet是Kubernetes核心资源详解的重要组成部分。本节详细介绍StatefulSet的核心概念、工作原理和实际应用。

**关键要点**：

- StatefulSet的定义与核心原理
- StatefulSet的实现方式与技术细节
- StatefulSet在实际场景中的应用与最佳实践
- StatefulSet的常见问题与解决方案

StatefulSet在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 HPA 自动伸缩

HPA 自动伸缩是Kubernetes核心资源详解的重要组成部分。本节详细介绍HPA 自动伸缩的核心概念、工作原理和实际应用。

**关键要点**：

- HPA 自动伸缩的定义与核心原理
- HPA 自动伸缩的实现方式与技术细节
- HPA 自动伸缩在实际场景中的应用与最佳实践
- HPA 自动伸缩的常见问题与解决方案

HPA 自动伸缩在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：031-devops/025-HelmChartApplicationPackage.md ============ -->

## 1. Chart 结构

### 1.1 目录布局

目录布局是Helm-Chart应用打包的重要组成部分。本节详细介绍目录布局的核心概念、工作原理和实际应用。

**关键要点**：

- 目录布局的定义与核心原理
- 目录布局的实现方式与技术细节
- 目录布局在实际场景中的应用与最佳实践
- 目录布局的常见问题与解决方案

目录布局在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Chart.yaml 与 values.yaml

Chart.yaml 与 values.yaml是Helm-Chart应用打包的重要组成部分。本节详细介绍Chart.yaml 与 values.yaml的核心概念、工作原理和实际应用。

**关键要点**：

- Chart.yaml 与 values.yaml的定义与核心原理
- Chart.yaml 与 values.yaml的实现方式与技术细节
- Chart.yaml 与 values.yaml在实际场景中的应用与最佳实践
- Chart.yaml 与 values.yaml的常见问题与解决方案

Chart.yaml 与 values.yaml在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 模板语法

### 2.1 Go Template

Go Template是Helm-Chart应用打包的重要组成部分。本节详细介绍Go Template的核心概念、工作原理和实际应用。

**关键要点**：

- Go Template的定义与核心原理
- Go Template的实现方式与技术细节
- Go Template在实际场景中的应用与最佳实践
- Go Template的常见问题与解决方案

Go Template在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 内置函数与管道

内置函数与管道是Helm-Chart应用打包的重要组成部分。本节详细介绍内置函数与管道的核心概念、工作原理和实际应用。

**关键要点**：

- 内置函数与管道的定义与核心原理
- 内置函数与管道的实现方式与技术细节
- 内置函数与管道在实际场景中的应用与最佳实践
- 内置函数与管道的常见问题与解决方案

内置函数与管道在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 \_helpers.tpl

\_helpers.tpl是Helm-Chart应用打包的重要组成部分。本节详细介绍\_helpers.tpl的核心概念、工作原理和实际应用。

**关键要点**：

- \_helpers.tpl的定义与核心原理
- \_helpers.tpl的实现方式与技术细节
- \_helpers.tpl在实际场景中的应用与最佳实践
- \_helpers.tpl的常见问题与解决方案

\_helpers.tpl在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Values 管理

### 3.1 默认值与覆盖

默认值与覆盖是Helm-Chart应用打包的重要组成部分。本节详细介绍默认值与覆盖的核心概念、工作原理和实际应用。

**关键要点**：

- 默认值与覆盖的定义与核心原理
- 默认值与覆盖的实现方式与技术细节
- 默认值与覆盖在实际场景中的应用与最佳实践
- 默认值与覆盖的常见问题与解决方案

默认值与覆盖在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 子 Chart Values

子 Chart Values是Helm-Chart应用打包的重要组成部分。本节详细介绍子 Chart Values的核心概念、工作原理和实际应用。

**关键要点**：

- 子 Chart Values的定义与核心原理
- 子 Chart Values的实现方式与技术细节
- 子 Chart Values在实际场景中的应用与最佳实践
- 子 Chart Values的常见问题与解决方案

子 Chart Values在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 仓库与发布

### 4.1 Chart 仓库

Chart 仓库是Helm-Chart应用打包的重要组成部分。本节详细介绍Chart 仓库的核心概念、工作原理和实际应用。

**关键要点**：

- Chart 仓库的定义与核心原理
- Chart 仓库的实现方式与技术细节
- Chart 仓库在实际场景中的应用与最佳实践
- Chart 仓库的常见问题与解决方案

Chart 仓库在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 helm install/upgrade/rollback

helm install/upgrade/rollback是Helm-Chart应用打包的重要组成部分。本节详细介绍helm install/upgrade/rollback的核心概念、工作原理和实际应用。

**关键要点**：

- helm install/upgrade/rollback的定义与核心原理
- helm install/upgrade/rollback的实现方式与技术细节
- helm install/upgrade/rollback在实际场景中的应用与最佳实践
- helm install/upgrade/rollback的常见问题与解决方案

helm install/upgrade/rollback在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：031-devops/026-Terraform.md ============ -->

## 1. Terraform 核心概念

### 1.1 Provider 与 Resource

Provider 与 Resource是Terraform资源编排的重要组成部分。本节详细介绍Provider 与 Resource的核心概念、工作原理和实际应用。

**关键要点**：

- Provider 与 Resource的定义与核心原理
- Provider 与 Resource的实现方式与技术细节
- Provider 与 Resource在实际场景中的应用与最佳实践
- Provider 与 Resource的常见问题与解决方案

Provider 与 Resource在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 HCL 语法

HCL 语法是Terraform资源编排的重要组成部分。本节详细介绍HCL 语法的核心概念、工作原理和实际应用。

**关键要点**：

- HCL 语法的定义与核心原理
- HCL 语法的实现方式与技术细节
- HCL 语法在实际场景中的应用与最佳实践
- HCL 语法的常见问题与解决方案

HCL 语法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 状态管理

### 2.1 State 文件

State 文件是Terraform资源编排的重要组成部分。本节详细介绍State 文件的核心概念、工作原理和实际应用。

**关键要点**：

- State 文件的定义与核心原理
- State 文件的实现方式与技术细节
- State 文件在实际场景中的应用与最佳实践
- State 文件的常见问题与解决方案

State 文件在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 远程后端

远程后端是Terraform资源编排的重要组成部分。本节详细介绍远程后端的核心概念、工作原理和实际应用。

**关键要点**：

- 远程后端的定义与核心原理
- 远程后端的实现方式与技术细节
- 远程后端在实际场景中的应用与最佳实践
- 远程后端的常见问题与解决方案

远程后端在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 State 锁定

State 锁定是Terraform资源编排的重要组成部分。本节详细介绍State 锁定的核心概念、工作原理和实际应用。

**关键要点**：

- State 锁定的定义与核心原理
- State 锁定的实现方式与技术细节
- State 锁定在实际场景中的应用与最佳实践
- State 锁定的常见问题与解决方案

State 锁定在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Module 模块化

### 3.1 Module 结构

Module 结构是Terraform资源编排的重要组成部分。本节详细介绍Module 结构的核心概念、工作原理和实际应用。

**关键要点**：

- Module 结构的定义与核心原理
- Module 结构的实现方式与技术细节
- Module 结构在实际场景中的应用与最佳实践
- Module 结构的常见问题与解决方案

Module 结构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 输入输出变量

输入输出变量是Terraform资源编排的重要组成部分。本节详细介绍输入输出变量的核心概念、工作原理和实际应用。

**关键要点**：

- 输入输出变量的定义与核心原理
- 输入输出变量的实现方式与技术细节
- 输入输出变量在实际场景中的应用与最佳实践
- 输入输出变量的常见问题与解决方案

输入输出变量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 模块注册表

模块注册表是Terraform资源编排的重要组成部分。本节详细介绍模块注册表的核心概念、工作原理和实际应用。

**关键要点**：

- 模块注册表的定义与核心原理
- 模块注册表的实现方式与技术细节
- 模块注册表在实际场景中的应用与最佳实践
- 模块注册表的常见问题与解决方案

模块注册表在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 工作流

### 4.1 init/plan/apply

init/plan/apply是Terraform资源编排的重要组成部分。本节详细介绍init/plan/apply的核心概念、工作原理和实际应用。

**关键要点**：

- init/plan/apply的定义与核心原理
- init/plan/apply的实现方式与技术细节
- init/plan/apply在实际场景中的应用与最佳实践
- init/plan/apply的常见问题与解决方案

init/plan/apply在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 变更检测

变更检测是Terraform资源编排的重要组成部分。本节详细介绍变更检测的核心概念、工作原理和实际应用。

**关键要点**：

- 变更检测的定义与核心原理
- 变更检测的实现方式与技术细节
- 变更检测在实际场景中的应用与最佳实践
- 变更检测的常见问题与解决方案

变更检测在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 导入已有资源

导入已有资源是Terraform资源编排的重要组成部分。本节详细介绍导入已有资源的核心概念、工作原理和实际应用。

**关键要点**：

- 导入已有资源的定义与核心原理
- 导入已有资源的实现方式与技术细节
- 导入已有资源在实际场景中的应用与最佳实践
- 导入已有资源的常见问题与解决方案

导入已有资源在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：031-devops/027-AnsiblePlaybookConfigManagement.md ============ -->

## 1. Ansible 架构

### 1.1 Agentless 模型

Agentless 模型是Ansible-Playbook配置管理的重要组成部分。本节详细介绍Agentless 模型的核心概念、工作原理和实际应用。

**关键要点**：

- Agentless 模型的定义与核心原理
- Agentless 模型的实现方式与技术细节
- Agentless 模型在实际场景中的应用与最佳实践
- Agentless 模型的常见问题与解决方案

Agentless 模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Inventory 清单

Inventory 清单是Ansible-Playbook配置管理的重要组成部分。本节详细介绍Inventory 清单的核心概念、工作原理和实际应用。

**关键要点**：

- Inventory 清单的定义与核心原理
- Inventory 清单的实现方式与技术细节
- Inventory 清单在实际场景中的应用与最佳实践
- Inventory 清单的常见问题与解决方案

Inventory 清单在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Playbook 编写

### 2.1 YAML 语法

YAML 语法是Ansible-Playbook配置管理的重要组成部分。本节详细介绍YAML 语法的核心概念、工作原理和实际应用。

**关键要点**：

- YAML 语法的定义与核心原理
- YAML 语法的实现方式与技术细节
- YAML 语法在实际场景中的应用与最佳实践
- YAML 语法的常见问题与解决方案

YAML 语法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 常用 Module

常用 Module是Ansible-Playbook配置管理的重要组成部分。本节详细介绍常用 Module的核心概念、工作原理和实际应用。

**关键要点**：

- 常用 Module的定义与核心原理
- 常用 Module的实现方式与技术细节
- 常用 Module在实际场景中的应用与最佳实践
- 常用 Module的常见问题与解决方案

常用 Module在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 条件与循环

条件与循环是Ansible-Playbook配置管理的重要组成部分。本节详细介绍条件与循环的核心概念、工作原理和实际应用。

**关键要点**：

- 条件与循环的定义与核心原理
- 条件与循环的实现方式与技术细节
- 条件与循环在实际场景中的应用与最佳实践
- 条件与循环的常见问题与解决方案

条件与循环在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Role 组织

### 3.1 Role 目录结构

Role 目录结构是Ansible-Playbook配置管理的重要组成部分。本节详细介绍Role 目录结构的核心概念、工作原理和实际应用。

**关键要点**：

- Role 目录结构的定义与核心原理
- Role 目录结构的实现方式与技术细节
- Role 目录结构在实际场景中的应用与最佳实践
- Role 目录结构的常见问题与解决方案

Role 目录结构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Galaxy 仓库

Galaxy 仓库是Ansible-Playbook配置管理的重要组成部分。本节详细介绍Galaxy 仓库的核心概念、工作原理和实际应用。

**关键要点**：

- Galaxy 仓库的定义与核心原理
- Galaxy 仓库的实现方式与技术细节
- Galaxy 仓库在实际场景中的应用与最佳实践
- Galaxy 仓库的常见问题与解决方案

Galaxy 仓库在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 幂等性

幂等性是Ansible-Playbook配置管理的重要组成部分。本节详细介绍幂等性的核心概念、工作原理和实际应用。

**关键要点**：

- 幂等性的定义与核心原理
- 幂等性的实现方式与技术细节
- 幂等性在实际场景中的应用与最佳实践
- 幂等性的常见问题与解决方案

幂等性在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 变量管理

变量管理是Ansible-Playbook配置管理的重要组成部分。本节详细介绍变量管理的核心概念、工作原理和实际应用。

**关键要点**：

- 变量管理的定义与核心原理
- 变量管理的实现方式与技术细节
- 变量管理在实际场景中的应用与最佳实践
- 变量管理的常见问题与解决方案

变量管理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 Vault 加密

Vault 加密是Ansible-Playbook配置管理的重要组成部分。本节详细介绍Vault 加密的核心概念、工作原理和实际应用。

**关键要点**：

- Vault 加密的定义与核心原理
- Vault 加密的实现方式与技术细节
- Vault 加密在实际场景中的应用与最佳实践
- Vault 加密的常见问题与解决方案

Vault 加密在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## ansible 命令

**基本用法:临时执行命令**
`ansible <主机模式> -m <模块> -a "<参数>"`

```bash
# 在所有主机上执行 ping
ansible all -m ping

# 在 web 组上执行 shell 命令
ansible web -m shell -a "uptime"

# 指定用户与私钥
ansible web -m ping -u deploy --private-key=~/.ssh/id_rsa

# 切换 sudo 执行
ansible db -m shell -a "systemctl restart nginx" -b --ask-become-pass
```

---

**基本用法:主机模式**
`ansible <模式> [选项]`

```bash
# 所有主机
ansible all -m ping

# 指定主机组
ansible web -m ping

# 多组交集
ansible 'web:&production' -m ping

# 排除某些主机
ansible 'web:!disabled' -m ping

# 直接指定主机
ansible web1.example.com -m ping

# 使用通配符
ansible '*.example.com' -m ping
```

---

**基本用法:常用选项**
`ansible <主机> [选项]`

```bash
# 列出匹配主机(不执行)
ansible all --list-hosts

# 指定清单文件
ansible all -i inventory.ini -m ping

# 指定并发数
ansible all -m ping -f 10

# 输出详细
ansible web -m ping -v
ansible web -m ping -vvv

# 限制单台主机执行
ansible web -m ping --limit web1.example.com
```

---

## ansible-playbook 命令

**基本用法:执行 Playbook**
`ansible-playbook <playbook.yml>`

```bash
# 执行 Playbook
ansible-playbook site.yml

# 指定清单文件
ansible-playbook -i production.ini site.yml

# 指定用户与权限
ansible-playbook site.yml -u deploy -b -K

# 显示差异
ansible-playbook site.yml --diff

# 检查模式(不实际执行)
ansible-playbook site.yml --check
```

---

**基本用法:标签与限制**
`ansible-playbook <playbook> [--tags|--skip-tags]`

```bash
# 仅执行带指定标签的任务
ansible-playbook site.yml --tags "install,configure"

# 跳过指定标签
ansible-playbook site.yml --skip-tags "test"

# 列出所有标签
ansible-playbook site.yml --list-tags

# 限制主机执行
ansible-playbook site.yml --limit web1.example.com

# 限制单台主机并指定起始任务
ansible-playbook site.yml --limit web1 --start-at-task "install nginx"
```

---

**基本用法:变量与额外参数**
`ansible-playbook <playbook> -e "<变量=值>"`

```bash
# 命令行传入变量
ansible-playbook site.yml -e "env=production version=v1.2"

# 从文件传入变量
ansible-playbook site.yml -e @vars.yml

# JSON 格式变量
ansible-playbook site.yml -e '{"env":"prod","replicas":3}'

# 显示主机变量
ansible-playbook site.yml --list-hosts
```

---

## 核心模块

**基本用法:file 文件管理**
`ansible <主机> -m file -a "path=<路径> state=<状态>"`

```bash
# 创建目录
ansible web -m file -a "path=/opt/app state=directory mode=0755"

# 创建符号链接
ansible web -m file -a "src=/etc/nginx/nginx.conf dest=/etc/nginx/nginx.conf.bak state=link"

# 删除文件
ansible web -m file -a "path=/tmp/oldfile state=absent"

# 修改权限
ansible web -m file -a "path=/opt/app owner=deploy group=deploy mode=0644"
```

---

**基本用法:copy 与 template**
`ansible <主机> -m copy -a "src=<源> dest=<目标>"`

```bash
# 复制文件
ansible web -m copy -a "src=app.conf dest=/etc/nginx/conf.d/app.conf owner=root mode=0644"

# 备份原文件
ansible web -m copy -a "src=nginx.conf dest=/etc/nginx/nginx.conf backup=yes"

# 直接写入内容
ansible web -m copy -a "content='Hello World\n' dest=/tmp/test.txt"

# template 模块渲染 Jinja2
ansible web -m template -a "src=nginx.j2 dest=/etc/nginx/nginx.conf"
```

---

**基本用法:包管理**
`ansible <主机> -m yum -a "name=<包名> state=<状态>"`

```bash
# 安装包(yum)
ansible web -m yum -a "name=nginx state=present"

# 安装最新版
ansible web -m yum -a "name=nginx state=latest"

# 卸载包
ansible web -m yum -a "name=nginx state=absent"

# apt 包管理
ansible web -m apt -a "name=nginx state=present update_cache=yes"
```

---

**基本用法:service 服务管理**
`ansible <主机> -m service -a "name=<服务> state=<状态>"`

```bash
# 启动服务
ansible web -m service -a "name=nginx state=started"

# 重启服务
ansible web -m service -a "name=nginx state=restarted"

# 设置开机启动
ansible web -m service -a "name=nginx enabled=yes state=started"

# systemd 模块
ansible web -m systemd -a "name=nginx state=restarted daemon_reload=yes"
```

---

**基本用法:user 与 group**
`ansible <主机> -m user -a "name=<用户> ..."`

```bash
# 创建用户
ansible web -m user -a "name=deploy shell=/bin/bash groups=docker append=yes"

# 创建用户并设置 SSH 公钥
ansible web -m user -a "name=deploy ssh_key_file=~/.ssh/id_rsa.pub"

# 删除用户
ansible web -m user -a "name=olduser state=absent remove=yes"

# 创建组
ansible web -m group -a "name=developers state=present"
```

---

## Playbook 编写

**基本用法:Playbook 结构**
`--- hosts: <主机>`

```yaml
# playbook.yml Playbook 基本结构
---
- name: 部署 Nginx Web 服务
  hosts: web
  become: yes
  vars:
    nginx_port: 80
    server_name: example.com

  tasks:
  - name: 安装 Nginx
    yum:
      name: nginx
      state: present

  - name: 配置 Nginx
    template:
      src: nginx.conf.j2
      dest: /etc/nginx/nginx.conf
    notify: restart nginx

  - name: 启动 Nginx
    service:
      name: nginx
      state: started
      enabled: yes

  handlers:
  - name: restart nginx
    service:
      name: nginx
      state: restarted
```

---

**基本用法:条件与循环**
`when: <条件> / loop: <列表>`

```yaml
# 条件与循环示例
---
- name: 多服务管理
  hosts: web
  tasks:
  - name: 安装多个包
    yum:
      name: "{{ item }}"
      state: present
    loop:
    - nginx
    - git
    - curl

  - name: 根据系统分发执行
    service:
      name: nginx
      state: restarted
    when: ansible_os_family == "RedHat"

  - name: 仅在开发环境执行
    debug:
      msg: "这是开发环境"
    when: env == "dev"

  - name: 创建多个用户
    user:
      name: "{{ item.name }}"
      groups: "{{ item.groups }}"
    loop:
    - { name: alice, groups: dev }
    - { name: bob, groups: ops }
```

---

**基本用法:变量与模板**
`vars:`

```yaml
# 变量使用示例
---
- name: 应用部署
  hosts: web
  vars:
    app_name: myapp
    app_version: "1.2.0"
    app_ports:
    - 8080
    - 8443

  vars_files:
  - vars/secret.yml

  tasks:
  - name: 显示应用信息
    debug:
      msg: "部署 {{ app_name }} 版本 {{ app_version }}"

  - name: 渲染配置文件
    template:
      src: app.conf.j2
      dest: "/etc/{{ app_name }}/app.conf"
```

```
# app.conf.j2 模板文件
server {
    {% for port in app_ports %}
    listen {{ port }};
    {% endfor %}
    server_name {{ app_name }}.example.com;
    version {{ app_version }};
}
```

---

## Roles 角色

**基本用法:创建 Role 目录**
`ansible-galaxy init <角色名>`

```bash
# 创建 Role 标准目录结构
ansible-galaxy init nginx

# 目录结构
# nginx/
# ├── defaults/main.yml      默认变量
# ├── files/                 静态文件
# ├── handlers/main.yml      处理器
# ├── meta/main.yml          元数据
# ├── tasks/main.yml         任务
# ├── templates/             Jinja2 模板
# └── vars/main.yml          变量(高优先级)
```

---

**基本用法:使用 Role**
`roles: - <角色>`

```yaml
# site.yml 使用 Role 示例
---
- name: 部署 Web 服务器
  hosts: web
  become: yes
  roles:
  - role: nginx
    vars:
      nginx_port: 80
  - role: firewall

# 也可以简写
- hosts: web
  roles:
  - nginx
  - monitoring
```

---

**基本用法:Role 依赖**
`meta/main.yml`

```yaml
# nginx/meta/main.yml 角色依赖
dependencies:
- role: common
  vars:
    common_packages:
    - curl
    - vim
- role: firewall
  when: enable_firewall | bool
```

---

## ansible-galaxy

**基本用法:安装 Role**
`ansible-galaxy install <作者>.<角色>`

```bash
# 从 Galaxy 安装 Role
ansible-galaxy install geerlingguy.nginx

# 指定版本
ansible-galaxy install geerlingguy.nginx,v3.1.0

# 从 git 安装
ansible-galaxy install git+https://github.com/geerlingguy/ansible-role-nginx.git

# 安装到指定路径
ansible-galaxy install geerlingguy.nginx -p ./roles
```

---

**基本用法:管理 Role**
`ansible-galaxy list|search|remove`

```bash
# 列出已安装 Role
ansible-galaxy list

# 搜索 Role
ansible-galaxy search nginx

# 查看 Role 信息
ansible-galaxy info geerlingguy.nginx

# 删除 Role
ansible-galaxy remove geerlingguy.nginx

# 通过 requirements.yml 批量安装
ansible-galaxy install -r requirements.yml
```

```yaml
# requirements.yml 依赖列表
- src: geerlingguy.nginx
  version: 3.1.0
- src: git+https://github.com/org/role.git
  name: custom-role
```

---

## Inventory 清单

**基本用法:INI 格式清单**
`/etc/ansible/hosts`

```ini
# inventory.ini 清单文件示例
[web]
web1.example.com ansible_host=192.168.1.10
web2.example.com ansible_host=192.168.1.11

[db]
db1.example.com ansible_host=192.168.1.20

[production:children]
web
db

[production:vars]
ansible_user=deploy
ansible_ssh_private_key_file=~/.ssh/prod_rsa
env=production
```

---

**基本用法:YAML 格式清单**
`inventory.yml`

```yaml
# inventory.yml YAML 格式清单
all:
  children:
    web:
      hosts:
        web1.example.com:
          ansible_host: 192.168.1.10
        web2.example.com:
          ansible_host: 192.168.1.11
      vars:
        nginx_port: 80
    db:
      hosts:
        db1.example.com:
          ansible_host: 192.168.1.20
  vars:
    ansible_user: deploy
    env: production
```

---

**基本用法:动态清单**
`ansible -i <脚本> all --list-hosts`

```bash
# 使用动态清单脚本
ansible -i ./ec2_inventory.py all --list-hosts

# 同时使用多个清单
ansible -i inventory.ini -i ec2.py all -m ping

# 启用清单缓存
export ANSIBLE_INVENTORY_CACHE=True
export ANSIBLE_INVENTORY_CACHE_CONNECTION=redis
```

---

## ansible-vault 加密

**基本用法:加密文件**
`ansible-vault encrypt <文件>`

```bash
# 加密文件
ansible-vault encrypt vars/secret.yml

# 加密时指定密码文件
ansible-vault encrypt vars/secret.yml --vault-password-file ~/.vault_pass

# 加密字符串(用于嵌入)
ansible-vault encrypt_string 'mypassword' --name 'db_password'

# 加密字符串并追加到文件
ansible-vault encrypt_string 'secret' --name 'api_key' >> vars/secrets.yml
```

---

**基本用法:解密与查看**
`ansible-vault view|decrypt <文件>`

```bash
# 查看加密文件内容
ansible-vault view vars/secret.yml

# 解密文件
ansible-vault decrypt vars/secret.yml

# 编辑加密文件
ansible-vault edit vars/secret.yml

# 重新加密(修改密码)
ansible-vault rekey vars/secret.yml
```

---

**基本用法:执行加密 Playbook**
`ansible-playbook --ask-vault-pass <playbook>`

```bash
# 交互式输入密码
ansible-playbook site.yml --ask-vault-pass

# 使用密码文件
ansible-playbook site.yml --vault-password-file ~/.vault_pass

# 使用多个密码文件
ansible-playbook site.yml --vault-password-file ~/.vault_pass --vault-password-file ~/.vault_pass_dev
```

---

## 调试与排查

**基本用法:语法检查**
`ansible-playbook --syntax-check <playbook>`

```bash
# 语法检查
ansible-playbook --syntax-check site.yml

# 检查模式(模拟执行)
ansible-playbook --check site.yml

# 检查模式 + 显示差异
ansible-playbook --check --diff site.yml

# 列出任务
ansible-playbook --list-tasks site.yml
```

---

**基本用法:debug 模块**
`debug: var=<变量>`

```yaml
# Playbook 中使用 debug
- name: 调试示例
  hosts: web
  tasks:
  - name: 显示主机名
    debug:
      msg: "主机名: {{ inventory_hostname }} IP: {{ ansible_host }}"

  - name: 显示变量
    debug:
      var: ansible_distribution

  - name: 注册变量并显示
    shell: uptime
    register: result

  - name: 显示命令输出
    debug:
      var: result.stdout_lines

  - name: 失败时显示
    debug:
      msg: "命令失败: {{ result.stderr }}"
    when: result.failed
```

---

**基本用法:verbose 输出**
`ansible-playbook -v[vvv] <playbook>`

```bash
# 不同详细级别
ansible-playbook site.yml -v       # 基础输出
ansible-playbook site.yml -vv      # 含变量
ansible-playbook site.yml -vvv     # 含 SSH 详情
ansible-playbook site.yml -vvvv    # 含插件详情

# 仅查看执行步骤(详细模式 + 检查模式)
ansible-playbook site.yml --check --diff -v
```

---

## ansible-config 配置

**基本用法:查看配置**
`ansible-config view|list|dump`

```bash
# 查看当前生效配置
ansible-config view

# 列出所有配置选项
ansible-config list

# 查看生效的配置项
ansible-config dump | grep -i host_key

# 查看指定配置项
ansible-config dump | grep DEFAULT_INVENTORY
```

---

**基本用法:常用配置**
`ansible.cfg`

```ini
# ansible.cfg 配置文件
[defaults]
inventory = ./inventory.ini
host_key_checking = False
remote_user = deploy
private_key_file = ~/.ssh/id_rsa
roles_path = ./roles
log_path = /var/log/ansible.log
forks = 10
gathering = smart
fact_caching = redis
fact_caching_connection = localhost:6379

[privilege_escalation]
become = True
become_method = sudo
become_user = root
```

```bash
# 设置环境变量覆盖配置
export ANSIBLE_HOST_KEY_CHECKING=False
export ANSIBLE_FORKS=20

# 生成默认配置文件
ansible-config init --disabled > ansible.cfg
```

<!-- ============ 文档分隔线：031-devops/028-Prometheus.md ============ -->

## 1. Prometheus 架构

### 1.1 Pull 模型

Pull 模型是Prometheus指标采集与告警的重要组成部分。本节详细介绍Pull 模型的核心概念、工作原理和实际应用。

**关键要点**：

- Pull 模型的定义与核心原理
- Pull 模型的实现方式与技术细节
- Pull 模型在实际场景中的应用与最佳实践
- Pull 模型的常见问题与解决方案

Pull 模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 四种指标类型

四种指标类型是Prometheus指标采集与告警的重要组成部分。本节详细介绍四种指标类型的核心概念、工作原理和实际应用。

**关键要点**：

- 四种指标类型的定义与核心原理
- 四种指标类型的实现方式与技术细节
- 四种指标类型在实际场景中的应用与最佳实践
- 四种指标类型的常见问题与解决方案

四种指标类型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. PromQL 查询

### 2.1 即时向量与范围向量

即时向量与范围向量是Prometheus指标采集与告警的重要组成部分。本节详细介绍即时向量与范围向量的核心概念、工作原理和实际应用。

**关键要点**：

- 即时向量与范围向量的定义与核心原理
- 即时向量与范围向量的实现方式与技术细节
- 即时向量与范围向量在实际场景中的应用与最佳实践
- 即时向量与范围向量的常见问题与解决方案

即时向量与范围向量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 聚合操作

聚合操作是Prometheus指标采集与告警的重要组成部分。本节详细介绍聚合操作的核心概念、工作原理和实际应用。

**关键要点**：

- 聚合操作的定义与核心原理
- 聚合操作的实现方式与技术细节
- 聚合操作在实际场景中的应用与最佳实践
- 聚合操作的常见问题与解决方案

聚合操作在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 常用查询模式

常用查询模式是Prometheus指标采集与告警的重要组成部分。本节详细介绍常用查询模式的核心概念、工作原理和实际应用。

**关键要点**：

- 常用查询模式的定义与核心原理
- 常用查询模式的实现方式与技术细节
- 常用查询模式在实际场景中的应用与最佳实践
- 常用查询模式的常见问题与解决方案

常用查询模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 告警配置

### 3.1 告警规则

告警规则是Prometheus指标采集与告警的重要组成部分。本节详细介绍告警规则的核心概念、工作原理和实际应用。

**关键要点**：

- 告警规则的定义与核心原理
- 告警规则的实现方式与技术细节
- 告警规则在实际场景中的应用与最佳实践
- 告警规则的常见问题与解决方案

告警规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Alertmanager 路由

Alertmanager 路由是Prometheus指标采集与告警的重要组成部分。本节详细介绍Alertmanager 路由的核心概念、工作原理和实际应用。

**关键要点**：

- Alertmanager 路由的定义与核心原理
- Alertmanager 路由的实现方式与技术细节
- Alertmanager 路由在实际场景中的应用与最佳实践
- Alertmanager 路由的常见问题与解决方案

Alertmanager 路由在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 抑制与静默

抑制与静默是Prometheus指标采集与告警的重要组成部分。本节详细介绍抑制与静默的核心概念、工作原理和实际应用。

**关键要点**：

- 抑制与静默的定义与核心原理
- 抑制与静默的实现方式与技术细节
- 抑制与静默在实际场景中的应用与最佳实践
- 抑制与静默的常见问题与解决方案

抑制与静默在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 指标命名

指标命名是Prometheus指标采集与告警的重要组成部分。本节详细介绍指标命名的核心概念、工作原理和实际应用。

**关键要点**：

- 指标命名的定义与核心原理
- 指标命名的实现方式与技术细节
- 指标命名在实际场景中的应用与最佳实践
- 指标命名的常见问题与解决方案

指标命名在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 标签设计

标签设计是Prometheus指标采集与告警的重要组成部分。本节详细介绍标签设计的核心概念、工作原理和实际应用。

**关键要点**：

- 标签设计的定义与核心原理
- 标签设计的实现方式与技术细节
- 标签设计在实际场景中的应用与最佳实践
- 标签设计的常见问题与解决方案

标签设计在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 告警分级

告警分级是Prometheus指标采集与告警的重要组成部分。本节详细介绍告警分级的核心概念、工作原理和实际应用。

**关键要点**：

- 告警分级的定义与核心原理
- 告警分级的实现方式与技术细节
- 告警分级在实际场景中的应用与最佳实践
- 告警分级的常见问题与解决方案

告警分级在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## promtool 工具

**基本用法:检查配置**
`promtool check config <配置文件>`

```bash
# 检查 prometheus.yml 配置语法
promtool check config /etc/prometheus/prometheus.yml

# 检查规则文件
promtool check rules /etc/prometheus/rules/*.yml

# 检查告警规则文件
promtool check rules alerts.yml
```

---

**基本用法:测试 PromQL 查询**
`promtool query instant <服务器> <查询表达式>`

```bash
# 即时查询
promtool query instant http://localhost:9090 'up'

# 查询 CPU 使用率
promtool query instant http://localhost:9090 '100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'

# 范围查询
promtool query range http://localhost:9090 'up' --start=2024-01-01T00:00:00Z --end=2024-01-01T01:00:00Z --step=60s
```

---

**基本用法:调试告警规则**
`promtool test rules <test.yaml>`

```yaml
# test.yaml 告警规则测试
rule_files:
- alerts.yml
evaluation_interval: 1m
tests:
- interval: 1m
  input_series:
  - series: 'node_cpu_seconds_total{mode="idle",instance="node1"}'
    values: '0+100x10'
  alert_rule_test:
  - eval_time: 10m
    alertname: HighCpuUsage
    exp_alerts:
    - exp_labels:
        severity: warning
        instance: node1
```

```bash
# 执行测试
promtool test rules test.yaml
```

---

## 基础查询 PromQL

**基本用法:即时查询**
`curl -G <服务器>/api/v1/query --data-urlencode "query=<表达式>"`

```bash
# 通过 HTTP 即时查询
curl -G http://localhost:9090/api/v1/query --data-urlencode "query=up"

# 查询所有节点的 CPU 空闲率
curl -G http://localhost:9090/api/v1/query \
  --data-urlencode "query=node_cpu_seconds_total{mode='idle'}"

# 查询指定时间点的数据
curl -G http://localhost:9090/api/v1/query \
  --data-urlencode "query=up" \
  --data-urlencode "time=1704067200"
```

---

**基本用法:范围查询**
`curl -G <服务器>/api/v1/query_range --data-urlencode "query=<表达式>"`

```bash
# 范围查询(过去 1 小时,每 60 秒采样)
curl -G http://localhost:9090/api/v1/query_range \
  --data-urlencode "query=up" \
  --data-urlencode "start=$(date -d '1 hour ago' +%s)" \
  --data-urlencode "end=$(date +%s)" \
  --data-urlencode "step=60"
```

---

**基本用法:基础指标查询**
`<指标名>`

```promql
# 查询所有 up 指标
up

# 查询指定 job 的指标
up{job="node-exporter"}

# 查询匹配多个标签
node_cpu_seconds_total{job="node-exporter", mode="idle"}

# 使用正则匹配
http_requests_total{method=~"GET|POST"}

# 使用负向匹配
http_requests_total{status!~"5.."}
```

---

## 聚合与计算

**基本用法:聚合函数**
`<函数>(<表达式>) by (<标签>)`

```promql
# 按实例平均 CPU 使用率
avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m]))

# 按 job 统计 HTTP 请求总数
sum by (job) (http_requests_total)

# 按方法统计每秒请求量
sum by (method) (rate(http_requests_total[5m]))

# 计算多实例最大值
max by (instance) (node_memory_MemAvailable_bytes)

# 计算分位数
histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))
```

---

**基本用法:速率计算**
`rate(<指标>[<时间窗口>])`

```promql
# 每秒速率(适用于 counter)
rate(http_requests_total[5m])

# 增量(适用于 counter,不归一化)
increase(http_requests_total[1h])

# irate 即时速率(更高精度但更不稳定)
irate(http_requests_total[1m])

# 计算过去 5 分钟的平均 QPS
sum(rate(http_requests_total[5m]))
```

---

**基本用法:数学运算**
`<表达式> <运算符> <表达式>`

```promql
# 计算内存使用率
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# 计算 CPU 使用率(百分比)
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# 单位转换(字节转 GB)
node_memory_MemTotal_bytes / 1024 / 1024 / 1024

# 使用 clamp 防止异常值
clamp_max(clamp_min(rate(http_requests_total[5m]), 0), 1000)
```

---

## 告警规则

**基本用法:定义告警规则**
`groups: - rules:`

```yaml
# alerts.yml 告警规则文件
groups:
- name: node-alerts
  rules:
  - alert: HighCpuUsage
    expr: 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "CPU 使用率过高 {{ $labels.instance }}"
      description: "实例 {{ $labels.instance }} CPU 使用率超过 80%,当前值: {{ $value }}%"
```

---

**基本用法:多条件告警**
`expr: <表达式1> and <表达式2>`

```yaml
# 多条件组合告警
groups:
- name: composite-alerts
  rules:
  - alert: HighMemoryAndCpu
    expr: >
      (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes < 0.2)
      and
      (100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80)
    for: 10m
    labels:
      severity: critical
    annotations:
      summary: "节点 {{ $labels.instance }} 内存和 CPU 同时告急"

  - alert: PodCrashLooping
    expr: increase(kube_pod_container_status_restarts_total[1h]) > 5
    for: 5m
    labels:
      severity: warning
```

---

**基本用法:告警抑制与静默**
`inhibit_rules:`

```yaml
# 抑制规则:节点宕机时不发送其上所有 Pod 告警
inhibit_rules:
- source_match:
    alert: NodeDown
  target_match_re:
    alert: PodDown|ServiceDown
  equal: ['node']

# 通过 Alertmanager API 创建静默
curl -X POST http://alertmanager:9093/api/v2/silences \
  -H "Content-Type: application/json" \
  -d '{
    "matchers": [{"name": "instance", "value": "node1", "isRegex": false}],
    "startsAt": "2024-01-01T00:00:00Z",
    "endsAt": "2024-01-01T02:00:00Z",
    "createdBy": "admin",
    "comment": "维护窗口"
  }'
```

---

## 服务发现

**基本用法:Kubernetes 服务发现**
`kubernetes_sd_configs`

```yaml
# prometheus.yml K8s 服务发现配置
scrape_configs:
- job_name: 'kubernetes-pods'
  kubernetes_sd_configs:
  - role: pod
  relabel_configs:
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
    action: keep
    regex: true
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
    action: replace
    target_label: __metrics_path__
    regex: (.+)
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port, __meta_kubernetes_pod_ip]
    action: replace
    target_label: __address__
    regex: (.+);(.+)
    replacement: $2:$1
```

---

**基本用法:静态配置**
`static_configs`

```yaml
# 静态目标配置
scrape_configs:
- job_name: 'node-exporter'
  static_configs:
  - targets:
    - 'node1:9100'
    - 'node2:9100'
    labels:
      env: production

- job_name: 'mysql-exporter'
  static_configs:
  - targets: ['mysql-exporter:9104']
```

---

**基本用法:文件服务发现**
`file_sd_configs`

```yaml
# 基于文件的服务发现
scrape_configs:
- job_name: 'file-based'
  file_sd_configs:
  - files:
    - '/etc/prometheus/targets/*.yml'
    refresh_interval: 30s
```

```yaml
# targets/web.yml 目标文件
- targets:
  - web1.example.com:9100
  - web2.example.com:9100
  labels:
    service: web
```

---

## 标签与重新标记

**基本用法:relabel_configs**
`relabel_configs`

```yaml
# 重新标记示例
scrape_configs:
- job_name: 'node'
  static_configs:
  - targets: ['node1:9100']
  relabel_configs:
  - source_labels: [__address__]
    target_label: instance
    regex: '([^:]+):.*'
    replacement: '$1'

  # 过滤目标
  - source_labels: [__meta_kubernetes_pod_phase]
    action: keep
    regex: Running

  # 标签映射
  - source_labels: [__meta_kubernetes_namespace]
    target_label: namespace
```

---

**基本用法:metric_relabel_configs**
`metric_relabel_configs`

```yaml
# 采集后修改指标(过滤、改名等)
scrape_configs:
- job_name: 'app'
  static_configs:
  - targets: ['app:8080']
  metric_relabel_configs:
  # 丢弃高基数指标
  - source_labels: [__name__]
    regex: 'go_.*'
    action: drop

  # 重命名指标
  - source_labels: [__name__]
    target_label: __name__
    regex: 'http_requests_total'
    replacement: 'app_http_requests_total'
```

---

## 远程存储与联邦

**基本用法:远程写入**
`remote_write`

```yaml
# 远程写入配置(发送到 Thanos/Mimir 等)
remote_write:
- url: 'http://mimir:8080/api/v1/push'
  headers:
    X-Scope-OrgID: tenant1
  write_relabel_configs:
  - source_labels: [__name__]
    regex: 'go_.*'
    action: drop

# 远程读取
remote_read:
- url: 'http://mimir:8080/api/v1/read'
```

---

**基本用法:联邦集群**
`scrape_configs with federation`

```yaml
# 联邦配置(从其他 Prometheus 抓取)
scrape_configs:
- job_name: 'federate'
  scrape_interval: 30s
  honor_labels: true
  metrics_path: '/federate'
  params:
    'match[]':
    - '{job="node-exporter"}'
    - '{__name__=~"job:.*"}'
  static_configs:
  - targets: ['prometheus-child:9090']
```

---

## API 查询

**基本用法:查询指标元数据**
`curl <服务器>/api/v1/<端点>`

```bash
# 查询所有指标名
curl http://localhost:9090/api/v1/label/__name__/values

# 查询标签值
curl http://localhost:9090/api/v1/label/job/values

# 查询指标元数据
curl http://localhost:9090/api/v1/metadata

# 查询目标状态
curl http://localhost:9090/api/v1/targets
```

---

**基本用法:查询告警状态**
`curl <服务器>/api/v1/alerts`

```bash
# 查询当前触发的告警
curl http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | {alertname: .labels.alertname, state: .state}'

# 查询规则
curl http://localhost:9090/api/v1/rules | jq '.data.groups[].rules[]'

# 查询 Alertmanager 告警
curl http://alertmanager:9093/api/v2/alerts | jq '.[]'
```

---

**基本用法:管理 Alertmanager 静默**
`curl -X <方法> <alertmanager>/api/v2/silences`

```bash
# 列出所有静默
curl http://alertmanager:9093/api/v2/silences

# 创建静默
curl -X POST http://alertmanager:9093/api/v2/silences \
  -H "Content-Type: application/json" \
  -d '{
    "matchers": [{"name": "alertname", "value": "HighCpuUsage", "isRegex": false}],
    "startsAt": "2024-01-01T00:00:00Z",
    "endsAt": "2024-01-01T04:00:00Z",
    "createdBy": "ops",
    "comment": "夜间维护"
  }'

# 删除静默(需要静默 ID)
curl -X DELETE http://alertmanager:9093/api/v2/silence/<silence-id>
```

---

## 性能与排查

**基本用法:查看采集状态**
`curl <服务器>/api/v1/targets`

```bash
# 查看所有采集目标状态
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job: .labels.job, health: .health, lastError: .lastError}'

# 查看失败的目标
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.health=="down")'

# 查看 TSDB 状态
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data'
```

---

**基本用法:检查配置与规则**
`curl <服务器>/api/v1/status/config`

```bash
# 查看当前配置
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml'

# 查看规则
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[]'

# 查看_flags
curl -s http://localhost:9090/api/v1/status/flags | jq '.data'

# 查看 TSDB 统计信息
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data.seriesCountByMetricName | to_entries | sort_by(.value) | reverse | .[:10]'
```

---

**基本用法:热重载配置**
`curl -X POST <服务器>/-/reload`

```bash
# 热重载配置文件
curl -X POST http://localhost:9090/-/reload

# 或者发送 SIGHUP 信号
kill -HUP $(pgrep prometheus)

# 验证配置生效
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml | fromyaml | .scrape_configs | length'
```

<!-- ============ 文档分隔线：031-devops/029-GrafanaTableConfig.md ============ -->

## 1. 数据源配置

### 1.1 Prometheus

Prometheus是Grafana仪表盘配置的重要组成部分。本节详细介绍Prometheus的核心概念、工作原理和实际应用。

**关键要点**：

- Prometheus的定义与核心原理
- Prometheus的实现方式与技术细节
- Prometheus在实际场景中的应用与最佳实践
- Prometheus的常见问题与解决方案

Prometheus在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Loki

Loki是Grafana仪表盘配置的重要组成部分。本节详细介绍Loki的核心概念、工作原理和实际应用。

**关键要点**：

- Loki的定义与核心原理
- Loki的实现方式与技术细节
- Loki在实际场景中的应用与最佳实践
- Loki的常见问题与解决方案

Loki在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 Elasticsearch

Elasticsearch是Grafana仪表盘配置的重要组成部分。本节详细介绍Elasticsearch的核心概念、工作原理和实际应用。

**关键要点**：

- Elasticsearch的定义与核心原理
- Elasticsearch的实现方式与技术细节
- Elasticsearch在实际场景中的应用与最佳实践
- Elasticsearch的常见问题与解决方案

Elasticsearch在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 面板类型

### 2.1 时间序列图

时间序列图是Grafana仪表盘配置的重要组成部分。本节详细介绍时间序列图的核心概念、工作原理和实际应用。

**关键要点**：

- 时间序列图的定义与核心原理
- 时间序列图的实现方式与技术细节
- 时间序列图在实际场景中的应用与最佳实践
- 时间序列图的常见问题与解决方案

时间序列图在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 仪表盘

仪表盘是Grafana仪表盘配置的重要组成部分。本节详细介绍仪表盘的核心概念、工作原理和实际应用。

**关键要点**：

- 仪表盘的定义与核心原理
- 仪表盘的实现方式与技术细节
- 仪表盘在实际场景中的应用与最佳实践
- 仪表盘的常见问题与解决方案

仪表盘在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 热力图

热力图是Grafana仪表盘配置的重要组成部分。本节详细介绍热力图的核心概念、工作原理和实际应用。

**关键要点**：

- 热力图的定义与核心原理
- 热力图的实现方式与技术细节
- 热力图在实际场景中的应用与最佳实践
- 热力图的常见问题与解决方案

热力图在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.4 表格

表格是Grafana仪表盘配置的重要组成部分。本节详细介绍表格的核心概念、工作原理和实际应用。

**关键要点**：

- 表格的定义与核心原理
- 表格的实现方式与技术细节
- 表格在实际场景中的应用与最佳实践
- 表格的常见问题与解决方案

表格在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 变量与模板

### 3.1 查询变量

查询变量是Grafana仪表盘配置的重要组成部分。本节详细介绍查询变量的核心概念、工作原理和实际应用。

**关键要点**：

- 查询变量的定义与核心原理
- 查询变量的实现方式与技术细节
- 查询变量在实际场景中的应用与最佳实践
- 查询变量的常见问题与解决方案

查询变量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 间隔变量

间隔变量是Grafana仪表盘配置的重要组成部分。本节详细介绍间隔变量的核心概念、工作原理和实际应用。

**关键要点**：

- 间隔变量的定义与核心原理
- 间隔变量的实现方式与技术细节
- 间隔变量在实际场景中的应用与最佳实践
- 间隔变量的常见问题与解决方案

间隔变量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 链接面板

链接面板是Grafana仪表盘配置的重要组成部分。本节详细介绍链接面板的核心概念、工作原理和实际应用。

**关键要点**：

- 链接面板的定义与核心原理
- 链接面板的实现方式与技术细节
- 链接面板在实际场景中的应用与最佳实践
- 链接面板的常见问题与解决方案

链接面板在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 告警集成

### 4.1 Grafana 告警规则

Grafana 告警规则是Grafana仪表盘配置的重要组成部分。本节详细介绍Grafana 告警规则的核心概念、工作原理和实际应用。

**关键要点**：

- Grafana 告警规则的定义与核心原理
- Grafana 告警规则的实现方式与技术细节
- Grafana 告警规则在实际场景中的应用与最佳实践
- Grafana 告警规则的常见问题与解决方案

Grafana 告警规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 通知渠道

通知渠道是Grafana仪表盘配置的重要组成部分。本节详细介绍通知渠道的核心概念、工作原理和实际应用。

**关键要点**：

- 通知渠道的定义与核心原理
- 通知渠道的实现方式与技术细节
- 通知渠道在实际场景中的应用与最佳实践
- 通知渠道的常见问题与解决方案

通知渠道在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## 服务管理

**基本用法:启动 Grafana**
`grafana-server --config=<配置文件>`

```bash
# Linux 启动
systemctl start grafana-server
systemctl enable grafana-server

# 直接运行二进制
grafana-server --config=/etc/grafana/grafana.ini --homepath=/usr/share/grafana

# Docker 启动
docker run -d --name=grafana -p 3000:3000 grafana/grafana:latest

# Docker Compose 启动(带持久化)
docker run -d --name=grafana -p 3000:3000 \
  -v grafana-storage:/var/lib/grafana \
  -v /etc/grafana/provisioning:/etc/grafana/provisioning \
  grafana/grafana:latest
```

---

**基本用法:查看 Grafana 状态**
`systemctl status grafana-server`

```bash
# 查看服务状态
systemctl status grafana-server

# 查看日志
journalctl -u grafana-server -f --tail=50

# 查看容器日志
docker logs -f grafana --tail=50

# 查看版本
grafana-server -v
docker exec grafana grafana-cli --version
```

---

## grafana-cli 命令

**基本用法:安装插件**
`grafana-cli plugins install <插件名>`

```bash
# 安装饼图插件
grafana-cli plugins install grafana-piechart-panel

# 安装时钟插件
grafana-cli plugins install grafana-clock-panel

# 安装点击house 数据源
grafana-cli plugins install vertamedia-clickhouse-datasource

# 重启 Grafana 使插件生效
systemctl restart grafana-server
```

---

**基本用法:管理插件**
`grafana-cli plugins <list|install|remove>`

```bash
# 列出已安装插件
grafana-cli plugins ls

# 升级指定插件
grafana-cli plugins upgrade grafana-piechart-panel

# 卸载插件
grafana-cli plugins remove grafana-piechart-panel

# 安装指定版本
grafana-cli plugins install grafana-piechart-panel 1.5.0
```

---

**基本用法:重置管理员密码**
`grafana-cli admin reset-admin-password <新密码>`

```bash
# 重置 admin 密码
grafana-cli admin reset-admin-password newpassword

# Docker 环境重置密码
docker exec -it grafana grafana-cli admin reset-admin-password newpassword

# 查看用户列表(SQLite)
sqlite3 /var/lib/grafana/grafana.db "SELECT login,email FROM user;"
```

---

## API 操作

**基本用法:认证与获取 API Key**
`curl -u <用户>:<密码> <服务器>/api/...`

```bash
# 基本认证访问 API
curl -u admin:admin http://localhost:3000/api/health

# 创建 API Token
curl -X POST -H "Content-Type: application/json" -u admin:admin \
  http://localhost:3000/api/auth/keys \
  -d '{"name":"ci-key","role":"Admin","secondsToLive":86400}'

# 使用 Token 访问
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/org
```

---

**基本用法:管理数据源**
`curl <服务器>/api/datasources`

```bash
# 列出所有数据源
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/datasources

# 创建 Prometheus 数据源
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/datasources \
  -d '{
    "name": "Prometheus",
    "type": "prometheus",
    "url": "http://prometheus:9090",
    "access": "proxy",
    "isDefault": true
  }'

# 测试数据源连接
curl -X POST -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/datasources/name/Prometheus/health
```

---

**基本用法:管理仪表盘**
`curl <服务器>/api/dashboards`

```bash
# 查找仪表盘
curl -H "Authorization: Bearer <token>" \
  "http://localhost:3000/api/search?query=node"

# 导出仪表盘 JSON
curl -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/dashboards/uid/node-overview > dashboard.json

# 导入仪表盘
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/dashboards/db \
  -d @dashboard.json
```

---

## 仪表盘配置

**基本用法:仪表盘 JSON 结构**
`{ "dashboard": {...}, "folderId": 0, "overwrite": false }`

```json
{
  "dashboard": {
    "id": null,
    "uid": "node-overview",
    "title": "节点概览",
    "tags": ["node", "linux"],
    "timezone": "browser",
    "schemaVersion": 39,
    "refresh": "30s",
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "panels": [
      {
        "id": 1,
        "title": "CPU 使用率",
        "type": "stat",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "100 - avg(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100",
            "legendFormat": "{{instance}}"
          }
        ],
        "gridPos": {"h": 8, "w": 6, "x": 0, "y": 0}
      }
    ]
  },
  "folderId": 0,
  "overwrite": true
}
```

---

**基本用法:变量配置**
`templating.list`

```json
{
  "templating": {
    "list": [
      {
        "name": "datasource",
        "type": "datasource",
        "query": "prometheus",
        "current": {"text": "Prometheus", "value": "Prometheus"}
      },
      {
        "name": "instance",
        "type": "query",
        "datasource": "$datasource",
        "query": "label_values(node_cpu_seconds_total, instance)",
        "refresh": 1,
        "includeAll": true,
        "multi": true
      },
      {
        "name": "interval",
        "type": "interval",
        "options": [
          {"text": "1m", "value": "1m"},
          {"text": "5m", "value": "5m"},
          {"text": "1h", "value": "1h"}
        ],
        "current": {"text": "5m", "value": "5m"}
      }
    ]
  }
}
```

---

**基本用法:面板类型选择**
`type: <类型>`

```json
// 时间序列图
{"type": "timeseries", "title": "CPU 趋势"}

// 仪表盘
{"type": "gauge", "title": "内存使用率"}

// 统计数字
{"type": "stat", "title": "实例总数"}

// 表格
{"type": "table", "title": "节点列表"}

// 热力图
{"type": "heatmap", "title": "请求延迟分布"}

// 日志视图
{"type": "logs", "title": "应用日志"}
```

---

## Provisioning 自动配置

**基本用法:数据源自动配置**
`provisioning/datasources/datasource.yaml`

```yaml
# provisioning/datasources/datasource.yaml
apiVersion: 1

datasources:
- name: Prometheus
  type: prometheus
  access: proxy
  url: http://prometheus:9090
  isDefault: true
  editable: true

- name: Loki
  type: loki
  access: proxy
  url: http://loki:3100

- name: MySQL
  type: mysql
  url: mysql:3306
  user: readonly
  secureJsonData:
    password: ${MYSQL_PASSWORD}
  jsonData:
    database: metrics
```

---

**基本用法:仪表盘自动配置**
`provisioning/dashboards/dashboard.yaml`

```yaml
# provisioning/dashboards/dashboard.yaml
apiVersion: 1

providers:
- name: 'default'
  orgId: 1
  folder: 'Auto Provisioned'
  folderUid: auto-folder
  type: file
  disableDeletion: false
  updateIntervalSeconds: 30
  allowUiUpdates: true
  options:
    path: /var/lib/grafana/dashboards
    foldersFromFilesStructure: true
```

---

**基本用法:告警规则自动配置**
`provisioning/alerting/rules.yaml`

```yaml
# provisioning/alerting/rules.yaml
apiVersion: 1
groups:
- name: node-alerts
  interval: 30s
  rules:
  - uid: high-cpu
    title: High CPU Usage
    condition: A
    data:
    - refId: A
      relativeTimeRange:
        from: 600
        to: 0
      datasourceUid: prometheus-uid
      model:
        expr: "100 - avg(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100 > 80"
        instant: true
    noDataState: NoData
    execErrState: Error
    for: 5m
    annotations:
      summary: "CPU 使用率过高"
    labels:
      severity: warning
```

---

## 告警管理

**基本用法:配置通知渠道**
`provisioning/alerting/contactpoints.yaml`

```yaml
# provisioning/alerting/contactpoints.yaml
apiVersion: 1
contactPoints:
- name: slack-notification
  uid: slack-cp
  type: slack
  settings:
    url: https://hooks.slack.com/services/xxx
    channel: "#alerts"
  disableResolveMessage: false

- name: email-notification
  uid: email-cp
  type: email
  settings:
    addresses: ops@example.com
```

---

**基本用法:通知策略**
`provisioning/alerting/notificationpolicies.yaml`

```yaml
# provisioning/alerting/notificationpolicies.yaml
apiVersion: 1
policies:
- orgId: 1
  receiver: default
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
  - receiver: slack-notification
    matchers:
    - severity="critical"
    group_wait: 10s
  - receiver: email-notification
    matchers:
    - severity="warning"
    mute_time_intervals:
    - offhours
```

---

## 用户与组织管理

**基本用法:管理用户**
`curl -X POST <服务器>/api/admin/users`

```bash
# 创建用户
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/admin/users \
  -d '{"name":"Alice","email":"alice@example.com","login":"alice","password":"pass123"}'

# 修改用户角色
curl -X PATCH -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/org/users/2 \
  -d '{"role":"Editor"}'

# 列出组织成员
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/org/users
```

---

**基本用法:管理组织**
`curl <服务器>/api/orgs`

```bash
# 创建组织
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/orgs \
  -d '{"name":"Engineering"}'

# 切换当前组织
curl -X POST -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/user/using/2

# 列出所有组织
curl -H "Authorization: Bearer <token>" http://localhost:3000/api/orgs
```

---

## 备份与迁移

**基本用法:导出仪表盘**
`curl <服务器>/api/dashboards/uid/<uid>`

```bash
# 导出单个仪表盘
curl -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/dashboards/uid/node-overview > node-overview.json

# 批量导出所有仪表盘
for uid in $(curl -s -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/search?type=dash-db | jq -r '.[].uid'); do
  curl -s -H "Authorization: Bearer <token>" \
    http://localhost:3000/api/dashboards/uid/$uid > "dashboard-${uid}.json"
done
```

---

**基本用法:备份 SQLite 数据库**
`sqlite3 <数据库文件> .backup <备份文件>`

```bash
# 在线备份 SQLite 数据库
sqlite3 /var/lib/grafana/grafana.db ".backup /backup/grafana-$(date +%Y%m%d).db"

# 备份配置与数据卷
docker run --rm -v grafana-storage:/data -v $(pwd):/backup alpine \
  tar czf /backup/grafana-$(date +%Y%m%d).tar.gz /data

# 恢复备份
docker run --rm -v grafana-storage:/data -v $(pwd):/backup alpine \
  tar xzf /backup/grafana-backup.tar.gz -C /
```

---

## 性能与排查

**基本用法:查看 Grafana 健康状态**
`curl <服务器>/api/health`

```bash
# 健康检查
curl http://localhost:3000/api/health

# 查看指标
curl http://localhost:3000/metrics | grep grafana_

# 查看统计信息
curl -H "Authorization: Bearer <token>" \
  http://localhost:3000/api/admin/stats
```

---

**基本用法:配置日志级别**
`log.level = <级别>`

```ini
# grafana.ini 日志配置
[log]
mode = console file
level = info
filters = alerting.notifier:debug

[log.file]
level = info
max_lines = 1000000
max_size_shift = 28
daily_rotate = true
max_days = 7
```

```bash
# 运行时动态修改日志级别
curl -X PUT -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/admin/settings \
  -d '{"log.level":"debug"}'
```

---

**基本用法:查询性能优化**
`Query inspector`

```bash
# 通过 API 检查查询性能
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/ds/query \
  -d '{
    "queries": [{
      "refId": "A",
      "datasource": {"uid": "prometheus"},
      "expr": "rate(http_requests_total[5m])",
      "instant": false,
      "range": true
    }],
    "from": "now-1h",
    "to": "now"
  }'

# 查看慢查询日志
journalctl -u grafana-server | grep "slow query"
```

---

## 集成与导出

**基本用法:导出为图片或 PDF**
`curl <服务器>/render/d/<dashboard-uid>`

```bash
# 渲染仪表盘为图片(需安装 image renderer 插件)
curl "http://localhost:3000/render/d/node-overview?from=now-6h&to=now&width=1000&height=500" \
  -H "Authorization: Bearer <token>" -o dashboard.png

# 渲染特定面板
curl "http://localhost:3000/render/d-solo/node-overview/panel-1?from=now-6h&to=now&width=1000&height=500" \
  -H "Authorization: Bearer <token>" -o panel.png

# 通过共享快照 API
curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" \
  http://localhost:3000/api/snapshots \
  -d @dashboard.json
```

---

**基本用法:嵌入外部网页**
`<iframe src="<grafana-url>/d/<uid>">`

```html
<!-- 启用嵌入模式需要在 grafana.ini 中配置 -->
<!-- [security] allow_embedding = true -->

<iframe
  src="http://grafana:3000/d/node-overview?from=now-6h&to=now&kiosk=tv"
  width="100%"
  height="600"
  frameborder="0">
</iframe>

<!-- 通过 URL 参数控制显示 -->
<!-- kiosk=tv: 电视模式(隐藏顶部栏) -->
<!-- kiosk=1: 全屏模式(隐藏所有控件) -->
<!-- theme=light: 浅色主题 -->
```

<!-- ============ 文档分隔线：031-devops/030-ELKStackLogAnalysis.md ============ -->

## 1. Elasticsearch

### 1.1 索引与分片

索引与分片是ELK-Stack日志分析的重要组成部分。本节详细介绍索引与分片的核心概念、工作原理和实际应用。

**关键要点**：

- 索引与分片的定义与核心原理
- 索引与分片的实现方式与技术细节
- 索引与分片在实际场景中的应用与最佳实践
- 索引与分片的常见问题与解决方案

索引与分片在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 映射与模板

映射与模板是ELK-Stack日志分析的重要组成部分。本节详细介绍映射与模板的核心概念、工作原理和实际应用。

**关键要点**：

- 映射与模板的定义与核心原理
- 映射与模板的实现方式与技术细节
- 映射与模板在实际场景中的应用与最佳实践
- 映射与模板的常见问题与解决方案

映射与模板在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 查询 DSL

查询 DSL是ELK-Stack日志分析的重要组成部分。本节详细介绍查询 DSL的核心概念、工作原理和实际应用。

**关键要点**：

- 查询 DSL的定义与核心原理
- 查询 DSL的实现方式与技术细节
- 查询 DSL在实际场景中的应用与最佳实践
- 查询 DSL的常见问题与解决方案

查询 DSL在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Logstash

### 2.1 输入/过滤/输出插件

输入/过滤/输出插件是ELK-Stack日志分析的重要组成部分。本节详细介绍输入/过滤/输出插件的核心概念、工作原理和实际应用。

**关键要点**：

- 输入/过滤/输出插件的定义与核心原理
- 输入/过滤/输出插件的实现方式与技术细节
- 输入/过滤/输出插件在实际场景中的应用与最佳实践
- 输入/过滤/输出插件的常见问题与解决方案

输入/过滤/输出插件在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Grok 解析

Grok 解析是ELK-Stack日志分析的重要组成部分。本节详细介绍Grok 解析的核心概念、工作原理和实际应用。

**关键要点**：

- Grok 解析的定义与核心原理
- Grok 解析的实现方式与技术细节
- Grok 解析在实际场景中的应用与最佳实践
- Grok 解析的常见问题与解决方案

Grok 解析在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 管道配置

管道配置是ELK-Stack日志分析的重要组成部分。本节详细介绍管道配置的核心概念、工作原理和实际应用。

**关键要点**：

- 管道配置的定义与核心原理
- 管道配置的实现方式与技术细节
- 管道配置在实际场景中的应用与最佳实践
- 管道配置的常见问题与解决方案

管道配置在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Kibana

### 3.1 Discover 探索

Discover 探索是ELK-Stack日志分析的重要组成部分。本节详细介绍Discover 探索的核心概念、工作原理和实际应用。

**关键要点**：

- Discover 探索的定义与核心原理
- Discover 探索的实现方式与技术细节
- Discover 探索在实际场景中的应用与最佳实践
- Discover 探索的常见问题与解决方案

Discover 探索在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Dashboard 仪表盘

Dashboard 仪表盘是ELK-Stack日志分析的重要组成部分。本节详细介绍Dashboard 仪表盘的核心概念、工作原理和实际应用。

**关键要点**：

- Dashboard 仪表盘的定义与核心原理
- Dashboard 仪表盘的实现方式与技术细节
- Dashboard 仪表盘在实际场景中的应用与最佳实践
- Dashboard 仪表盘的常见问题与解决方案

Dashboard 仪表盘在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 KQL 查询

KQL 查询是ELK-Stack日志分析的重要组成部分。本节详细介绍KQL 查询的核心概念、工作原理和实际应用。

**关键要点**：

- KQL 查询的定义与核心原理
- KQL 查询的实现方式与技术细节
- KQL 查询在实际场景中的应用与最佳实践
- KQL 查询的常见问题与解决方案

KQL 查询在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 架构优化

### 4.1 Filebeat 轻量采集

Filebeat 轻量采集是ELK-Stack日志分析的重要组成部分。本节详细介绍Filebeat 轻量采集的核心概念、工作原理和实际应用。

**关键要点**：

- Filebeat 轻量采集的定义与核心原理
- Filebeat 轻量采集的实现方式与技术细节
- Filebeat 轻量采集在实际场景中的应用与最佳实践
- Filebeat 轻量采集的常见问题与解决方案

Filebeat 轻量采集在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 索引生命周期管理

索引生命周期管理是ELK-Stack日志分析的重要组成部分。本节详细介绍索引生命周期管理的核心概念、工作原理和实际应用。

**关键要点**：

- 索引生命周期管理的定义与核心原理
- 索引生命周期管理的实现方式与技术细节
- 索引生命周期管理在实际场景中的应用与最佳实践
- 索引生命周期管理的常见问题与解决方案

索引生命周期管理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## Elasticsearch 基础操作

**基本用法:集群健康检查**
`curl <服务器>/_cluster/health`

```bash
# 查看集群健康状态
curl -X GET "localhost:9200/_cluster/health?pretty"

# 查看集群健康状态(含分片级)
curl -X GET "localhost:9200/_cluster/health?level=indices&pretty"

# 查看节点信息
curl -X GET "localhost:9200/_cat/nodes?v"

# 查看主节点
curl -X GET "localhost:9200/_cat/master?v"
```

---

**基本用法:索引管理**
`curl -X <方法> <服务器>/<索引>`

```bash
# 列出所有索引
curl -X GET "localhost:9200/_cat/indices?v"

# 创建索引(指定分片与副本)
curl -X PUT "localhost:9200/logs-2024-01" -H 'Content-Type: application/json' -d '{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1
  }
}'

# 删除索引
curl -X DELETE "localhost:9200/logs-2024-01"

# 查看索引设置
curl -X GET "localhost:9200/logs-2024-01/_settings?pretty"
```

---

**基本用法:文档增删改查**
`curl -X <方法> <服务器>/<索引>/_doc/<id>`

```bash
# 索引文档(指定 ID)
curl -X PUT "localhost:9200/logs-2024-01/_doc/1" -H 'Content-Type: application/json' -d '{
  "level": "info",
  "message": "服务启动",
  "timestamp": "2024-01-01T00:00:00Z"
}'

# 自动生成 ID
curl -X POST "localhost:9200/logs-2024-01/_doc" -H 'Content-Type: application/json' -d '{
  "level": "error",
  "message": "数据库连接失败"
}'

# 获取文档
curl -X GET "localhost:9200/logs-2024-01/_doc/1?pretty"

# 更新文档
curl -X POST "localhost:9200/logs-2024-01/_update/1" -H 'Content-Type: application/json' -d '{
  "doc": {"level": "warning"}
}'

# 删除文档
curl -X DELETE "localhost:9200/logs-2024-01/_doc/1"
```

---

## Elasticsearch 查询

**基本用法:搜索文档**
`curl -X GET <服务器>/<索引>/_search`

```bash
# 简单查询(匹配所有)
curl -X GET "localhost:9200/logs-2024-01/_search?q=*&pretty"

# 按字段搜索
curl -X GET "localhost:9200/logs-2024-01/_search?q=level:error&pretty"

# 使用 DSL 查询
curl -X GET "localhost:9200/logs-2024-01/_search?pretty" -H 'Content-Type: application/json' -d '{
  "query": {
    "match": {
      "message": "数据库"
    }
  }
}'
```

---

**基本用法:布尔查询**
`bool: must|should|must_not|filter`

```bash
# 多条件组合查询
curl -X GET "localhost:9200/logs-*/_search?pretty" -H 'Content-Type: application/json' -d '{
  "query": {
    "bool": {
      "must": [
        {"match": {"level": "error"}}
      ],
      "filter": [
        {"range": {"timestamp": {"gte": "now-1h"}}}
      ],
      "must_not": [
        {"match": {"message": "debug"}}
      ]
    }
  },
  "sort": [{"timestamp": "desc"}],
  "size": 20
}'
```

---

**基本用法:聚合查询**
`aggs`

```bash
# 按级别分组统计
curl -X GET "localhost:9200/logs-*/_search" -H 'Content-Type: application/json' -d '{
  "size": 0,
  "aggs": {
    "levels": {
      "terms": {"field": "level.keyword", "size": 10}
    }
  }
}'

# 时间直方图聚合
curl -X GET "localhost:9200/logs-*/_search" -H 'Content-Type: application/json' -d '{
  "size": 0,
  "aggs": {
    "logs_over_time": {
      "date_histogram": {
        "field": "timestamp",
        "calendar_interval": "1h"
      }
    }
  }
}'
```

---

## Elasticsearch 索引模板

**基本用法:创建索引模板**
`PUT _index_template`

```bash
# 创建索引模板(匹配 logs-* 索引)
curl -X PUT "localhost:9200/_index_template/logs-template" -H 'Content-Type: application/json' -d '{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "number_of_shards": 3,
      "number_of_replicas": 1,
      "index.lifecycle.name": "logs-policy"
    },
    "mappings": {
      "properties": {
        "timestamp": {"type": "date"},
        "level": {"type": "keyword"},
        "message": {"type": "text"},
        "service": {"type": "keyword"}
      }
    }
  }
}'
```

---

**基本用法:ILM 索引生命周期管理**
`PUT _ilm/policy`

```bash
# 创建 ILM 策略
curl -X PUT "localhost:9200/_ilm/policy/logs-policy" -H 'Content-Type: application/json' -d '{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_age": "7d",
            "max_size": "50gb"
          }
        }
      },
      "warm": {
        "min_age": "30d",
        "actions": {
          "shrink": {"number_of_shards": 1},
          "forcemerge": {"max_num_segments": 1}
        }
      },
      "delete": {
        "min_age": "90d",
        "actions": {"delete": {}}
      }
    }
  }
}'

# 查看 ILM 状态
curl -X GET "localhost:9200/_ilm/policy/logs-policy?pretty"
```

---

## Logstash 配置

**基本用法:Logstash 配置结构**
`input {} filter {} output {}`

```
# logstash.conf 配置文件结构
input {
  beats {
    port => 5044
  }
}

filter {
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:msg}" }
  }
  date {
    match => ["timestamp", "ISO8601"]
    target => "@timestamp"
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "logs-%{+YYYY.MM.dd}"
  }
}
```

---

**基本用法:测试 Logstash 配置**
`bin/logstash -f <配置> -t`

```bash
# 测试配置语法
bin/logstash -f /etc/logstash/conf.d/logs.conf -t

# 启动 Logstash
bin/logstash -f /etc/logstash/conf.d/logs.conf

# 启动时启用配置自动重载
bin/logstash -f /etc/logstash/conf.d/logs.conf --config.reload.automatic

# 直接输入数据测试
echo '{"message":"test log"}' | bin/logstash -e 'input { stdin { codec => json } } output { stdout { codec => rubydebug } }'
```

---

**基本用法:Grok 模式匹配**
`grok { match => { "message" => "<模式>" } }`

```
# 常用 Grok 模式
# 解析 Nginx 访问日志
filter {
  grok {
    match => { "message" => '%{IPORHOST:client_ip} - %{DATA:user} \[%{HTTPDATE:timestamp}\] "%{WORD:method} %{URIPATHPARAM:request} HTTP/%{NUMBER:http_version}" %{NUMBER:status} %{NUMBER:bytes} "%{DATA:referrer}" "%{DATA:agent}"' }
  }
}

# 解析 Java 异常堆栈
filter {
  multiline {
    pattern => "^\s"
    what => "previous"
  }
  grok {
    match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} \[%{DATA:thread}\] %{DATA:logger} - %{GREEDYDATA:msg}" }
  }
}
```

---

**基本用法:条件处理**
`if [字段] == "值" { ... }`

```
# 根据日志级别路由
filter {
  if [level] == "ERROR" {
    mutate {
      add_tag => ["alert"]
    }
  } else if [level] in ["WARN", "INFO"] {
    mutate {
      add_tag => ["info"]
    }
  } else {
    mutate {
      add_tag => ["debug"]
      add_field => { "env" => "unknown" }
    }
  }
}

output {
  if "alert" in [tags] {
    elasticsearch {
      hosts => ["localhost:9200"]
      index => "alerts-%{+YYYY.MM.dd}"
    }
  }
}
```

---

## Kibana 操作

**基本用法:启动 Kibana**
`bin/kibana`

```bash
# Linux 启动
systemctl start kibana
systemctl enable kibana

# 直接运行
bin/kibana --config /etc/kibana/kibana.yml

# Docker 启动
docker run -d --name kibana -p 5601:5601 \
  -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 \
  kibana:8.11.0

# 查看日志
journalctl -u kibana -f
docker logs -f kibana
```

---

**基本用法:Kibana API**
`curl <服务器>:5601/api/...`

```bash
# 健康检查
curl http://localhost:5601/api/status

# 创建索引模式
curl -X POST -u elastic:password -H "Content-Type: application/json" -H "kbn-xsrf: true" \
  http://localhost:5601/api/index_patterns/index_pattern \
  -d '{
    "index_pattern": {
      "title": "logs-*",
      "timeFieldName": "@timestamp"
    }
  }'

# 查询索引模式
curl -u elastic:password http://localhost:5601/api/index_patterns
```

---

**基本用法:导出与导入对象**
`curl <服务器>:5601/api/saved_objects/_export`

```bash
# 导出仪表盘
curl -X POST -u elastic:password -H "Content-Type: application/json" -H "kbn-xsrf: true" \
  http://localhost:5601/api/saved_objects/_export \
  -d '{
    "objects": [
      {"type": "dashboard", "id": "web-logs-dashboard"}
    ]
  }' > dashboard.ndjson

# 导入仪表盘
curl -X POST -u elastic:password -H "Content-Type: application/json" -H "kbn-xsrf: true" \
  http://localhost:5601/api/saved_objects/_import?overwrite=true \
  -F file=@dashboard.ndjson
```

---

## Filebeat 采集

**基本用法:启动 Filebeat**
`filebeat -c <配置>`

```bash
# 启动 Filebeat
systemctl start filebeat
systemctl enable filebeat

# 测试配置
filebeat test config -c /etc/filebeat/filebeat.yml

# 测试输出连接
filebeat test output -c /etc/filebeat/filebeat.yml

# 直接运行(前台)
filebeat -e -c /etc/filebeat/filebeat.yml
```

---

**基本用法:Filebeat 配置**
`filebeat.inputs`

```yaml
# filebeat.yml 输入配置
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/nginx/access.log
  fields:
    service: nginx
    env: production
  fields_under_root: true

- type: container
  paths:
    - /var/lib/docker/containers/*/*.log
  processors:
  - add_kubernetes_metadata:
      host: ${NODE_NAME}
      matchers:
      - logs_path:
          logs_path: "/var/lib/docker/containers/"

output.logstash:
  hosts: ["logstash:5044"]
  indices:
  - "logs-%{[service]}"
```

---

**基本用法:启用模块**
`filebeat modules enable <模块>`

```bash
# 启用 Nginx 模块
filebeat modules enable nginx

# 启用多个模块
filebeat modules enable nginx mysql redis

# 查看已启用模块
filebeat modules list

# 模块配置(在 modules.d/nginx.yml)
cat modules.d/nginx.yml
```

```yaml
# modules.d/nginx.yml Nginx 模块配置
- module: nginx
  access:
    enabled: true
    var.paths: ["/var/log/nginx/access.log"]
  error:
    enabled: true
    var.paths: ["/var/log/nginx/error.log"]
```

---

## 集群管理

**基本用法:节点管理**
`curl <服务器>/_cat/nodes`

```bash
# 查看节点列表
curl "localhost:9200/_cat/nodes?v&h=name,ip,role,master,heap.percent,ram.percent,disk.used_percent"

# 查看节点磁盘使用
curl "localhost:9200/_cat/allocation?v"

# 查看节点统计
curl "localhost:9200/_nodes/stats?pretty"

# 临时排除节点(用于维护)
curl -X PUT "localhost:9200/_cluster/settings" -H 'Content-Type: application/json' -d '{
  "transient": {
    "cluster.routing.allocation.exclude._ip": "192.168.1.100"
  }
}'
```

---

**基本用法:分片管理**
`curl <服务器>/_cat/shards`

```bash
# 查看分片分布
curl "localhost:9200/_cat/shards?v"

# 查看未分配分片
curl "localhost:9200/_cat/shards?v" | grep UNASSIGNED

# 查看分片分配原因
curl "localhost:9200/_cluster/allocation/explain?pretty"

# 手动重新路由分片
curl -X POST "localhost:9200/_cluster/reroute" -H 'Content-Type: application/json' -d '{
  "commands": [
    {
      "move": {
        "index": "logs-2024-01",
        "shard": 0,
        "from_node": "node-1",
        "to_node": "node-2"
      }
    }
  ]
}'
```

---

**基本用法:快照与恢复**
`PUT _snapshot/<仓库>/<快照>`

```bash
# 注册快照仓库
curl -X PUT "localhost:9200/_snapshot/backup" -H 'Content-Type: application/json' -d '{
  "type": "fs",
  "settings": {
    "location": "/backup/es-snapshots"
  }
}'

# 创建快照
curl -X PUT "localhost:9200/_snapshot/backup/snapshot-2024-01-01?wait_for_completion=true"

# 查看快照
curl "localhost:9200/_snapshot/backup/_all?pretty"

# 恢复快照
curl -X POST "localhost:9200/_snapshot/backup/snapshot-2024-01-01/_restore" -H 'Content-Type: application/json' -d '{
  "indices": "logs-*",
  "ignore_unavailable": true
}'
```

---

## 安全与认证

**基本用法:启用安全认证**
`xpack.security.enabled: true`

```yaml
# elasticsearch.yml 启用安全
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: elastic-certificates.p12
```

```bash
# 生成证书
bin/elasticsearch-certutil ca
bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12

# 设置内置用户密码
bin/elasticsearch-setup-passwords auto

# 修改用户密码
curl -u elastic:password -X PUT "localhost:9200/_security/user/elastic/_password" -H 'Content-Type: application/json' -d '{
  "password": "newpassword"
}'
```

---

**基本用法:创建用户与角色**
`POST _security/user/<用户名>`

```bash
# 创建角色
curl -u elastic:password -X POST "localhost:9200/_security/role/logs_reader" -H 'Content-Type: application/json' -d '{
  "indices": [
    {
      "names": ["logs-*"],
      "privileges": ["read", "view_index_metadata"]
    }
  ]
}'

# 创建用户
curl -u elastic:password -X POST "localhost:9200/_security/user/alice" -H 'Content-Type: application/json' -d '{
  "password": "alicepass",
  "roles": ["logs_reader"],
  "full_name": "Alice",
  "email": "alice@example.com"
}'

# 创建 API Key
curl -u elastic:password -X POST "localhost:9200/_security/api_key" -H 'Content-Type: application/json' -d '{
  "name": "logstash-key",
  "role_descriptors": {
    "logs_writer": {
      "indices": [{"names": ["logs-*"], "privileges": ["write", "create_index"]}]
    }
  }
}'
```

---

## 排查与监控

**基本用法:查看集群统计**
`curl <服务器>/_cluster/stats`

```bash
# 集群统计信息
curl "localhost:9200/_cluster/stats?human&pretty"

# 索引统计
curl "localhost:9200/_stats?pretty"

# 节点线程池
curl "localhost:9200/_cat/thread_pool?v"

# 查看正在执行的任务
curl "localhost:9200/_cat/tasks?v"
```

---

**基本用法:排查慢查询**
`index.search.slowlog`

```bash
# 启用慢查询日志
curl -X PUT "localhost:9200/logs-*/_settings" -H 'Content-Type: application/json' -d '{
  "index.search.slowlog.threshold.query.warn": "10s",
  "index.search.slowlog.threshold.query.info": "5s",
  "index.indexing.slowlog.threshold.index.warn": "10s"
}'

# 查看任务
curl "localhost:9200/_tasks?detailed=true&actions=*search*&pretty"

# 取消长时间运行的任务
curl -X POST "localhost:9200/_tasks/<task_id>/_cancel"
```

---

**基本用法:清理与优化**
`POST <索引>/_forcemerge`

```bash
# 强制合并(减少段数量,优化只读索引)
curl -X POST "localhost:9200/logs-2023-*/_forcemerge?max_num_segments=1"

# 清理缓存
curl -X POST "localhost:9200/_cache/clear"

# 删除旧索引
curl -X DELETE "localhost:9200/logs-2023.01.*"

# 关闭索引(不删除但释放资源)
curl -X POST "localhost:9200/logs-2023.01/_close"

# 重新打开索引
curl -X POST "localhost:9200/logs-2023.01/_open"
```

<!-- ============ 文档分隔线：031-devops/031-OpenTelemetry.md ============ -->

## 1. OpenTelemetry 概述

### 1.1 三大信号

三大信号是OpenTelemetry的重要组成部分。本节详细介绍三大信号的核心概念、工作原理和实际应用。

**关键要点**：

- 三大信号的定义与核心原理
- 三大信号的实现方式与技术细节
- 三大信号在实际场景中的应用与最佳实践
- 三大信号的常见问题与解决方案

三大信号在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 架构组件

架构组件是OpenTelemetry的重要组成部分。本节详细介绍架构组件的核心概念、工作原理和实际应用。

**关键要点**：

- 架构组件的定义与核心原理
- 架构组件的实现方式与技术细节
- 架构组件在实际场景中的应用与最佳实践
- 架构组件的常见问题与解决方案

架构组件在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Trace 链路追踪

### 2.1 Span 与上下文传播

Span 与上下文传播是OpenTelemetry的重要组成部分。本节详细介绍Span 与上下文传播的核心概念、工作原理和实际应用。

**关键要点**：

- Span 与上下文传播的定义与核心原理
- Span 与上下文传播的实现方式与技术细节
- Span 与上下文传播在实际场景中的应用与最佳实践
- Span 与上下文传播的常见问题与解决方案

Span 与上下文传播在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 采样策略

采样策略是OpenTelemetry的重要组成部分。本节详细介绍采样策略的核心概念、工作原理和实际应用。

**关键要点**：

- 采样策略的定义与核心原理
- 采样策略的实现方式与技术细节
- 采样策略在实际场景中的应用与最佳实践
- 采样策略的常见问题与解决方案

采样策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 W3C Trace Context

W3C Trace Context是OpenTelemetry的重要组成部分。本节详细介绍W3C Trace Context的核心概念、工作原理和实际应用。

**关键要点**：

- W3C Trace Context的定义与核心原理
- W3C Trace Context的实现方式与技术细节
- W3C Trace Context在实际场景中的应用与最佳实践
- W3C Trace Context的常见问题与解决方案

W3C Trace Context在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Metric 指标

### 3.1 指标类型

指标类型是OpenTelemetry的重要组成部分。本节详细介绍指标类型的核心概念、工作原理和实际应用。

**关键要点**：

- 指标类型的定义与核心原理
- 指标类型的实现方式与技术细节
- 指标类型在实际场景中的应用与最佳实践
- 指标类型的常见问题与解决方案

指标类型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 SDK 自动采集

SDK 自动采集是OpenTelemetry的重要组成部分。本节详细介绍SDK 自动采集的核心概念、工作原理和实际应用。

**关键要点**：

- SDK 自动采集的定义与核心原理
- SDK 自动采集的实现方式与技术细节
- SDK 自动采集在实际场景中的应用与最佳实践
- SDK 自动采集的常见问题与解决方案

SDK 自动采集在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. Log 日志

### 4.1 结构化日志

结构化日志是OpenTelemetry的重要组成部分。本节详细介绍结构化日志的核心概念、工作原理和实际应用。

**关键要点**：

- 结构化日志的定义与核心原理
- 结构化日志的实现方式与技术细节
- 结构化日志在实际场景中的应用与最佳实践
- 结构化日志的常见问题与解决方案

结构化日志在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 与 Trace 关联

与 Trace 关联是OpenTelemetry的重要组成部分。本节详细介绍与 Trace 关联的核心概念、工作原理和实际应用。

**关键要点**：

- 与 Trace 关联的定义与核心原理
- 与 Trace 关联的实现方式与技术细节
- 与 Trace 关联在实际场景中的应用与最佳实践
- 与 Trace 关联的常见问题与解决方案

与 Trace 关联在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：031-devops/032-GitOpsArgoCD.md ============ -->

## 1. GitOps 原则

### 1.1 声明式描述

声明式描述是GitOps与ArgoCD的重要组成部分。本节详细介绍声明式描述的核心概念、工作原理和实际应用。

**关键要点**：

- 声明式描述的定义与核心原理
- 声明式描述的实现方式与技术细节
- 声明式描述在实际场景中的应用与最佳实践
- 声明式描述的常见问题与解决方案

声明式描述在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Git 单一事实来源

Git 单一事实来源是GitOps与ArgoCD的重要组成部分。本节详细介绍Git 单一事实来源的核心概念、工作原理和实际应用。

**关键要点**：

- Git 单一事实来源的定义与核心原理
- Git 单一事实来源的实现方式与技术细节
- Git 单一事实来源在实际场景中的应用与最佳实践
- Git 单一事实来源的常见问题与解决方案

Git 单一事实来源在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 自动化交付

自动化交付是GitOps与ArgoCD的重要组成部分。本节详细介绍自动化交付的核心概念、工作原理和实际应用。

**关键要点**：

- 自动化交付的定义与核心原理
- 自动化交付的实现方式与技术细节
- 自动化交付在实际场景中的应用与最佳实践
- 自动化交付的常见问题与解决方案

自动化交付在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. ArgoCD 架构

### 2.1 核心组件

核心组件是GitOps与ArgoCD的重要组成部分。本节详细介绍核心组件的核心概念、工作原理和实际应用。

**关键要点**：

- 核心组件的定义与核心原理
- 核心组件的实现方式与技术细节
- 核心组件在实际场景中的应用与最佳实践
- 核心组件的常见问题与解决方案

核心组件在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Application CRD

Application CRD是GitOps与ArgoCD的重要组成部分。本节详细介绍Application CRD的核心概念、工作原理和实际应用。

**关键要点**：

- Application CRD的定义与核心原理
- Application CRD的实现方式与技术细节
- Application CRD在实际场景中的应用与最佳实践
- Application CRD的常见问题与解决方案

Application CRD在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 同步策略

### 3.1 自动同步

自动同步是GitOps与ArgoCD的重要组成部分。本节详细介绍自动同步的核心概念、工作原理和实际应用。

**关键要点**：

- 自动同步的定义与核心原理
- 自动同步的实现方式与技术细节
- 自动同步在实际场景中的应用与最佳实践
- 自动同步的常见问题与解决方案

自动同步在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 手动同步

手动同步是GitOps与ArgoCD的重要组成部分。本节详细介绍手动同步的核心概念、工作原理和实际应用。

**关键要点**：

- 手动同步的定义与核心原理
- 手动同步的实现方式与技术细节
- 手动同步在实际场景中的应用与最佳实践
- 手动同步的常见问题与解决方案

手动同步在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 Sync Hook

Sync Hook是GitOps与ArgoCD的重要组成部分。本节详细介绍Sync Hook的核心概念、工作原理和实际应用。

**关键要点**：

- Sync Hook的定义与核心原理
- Sync Hook的实现方式与技术细节
- Sync Hook在实际场景中的应用与最佳实践
- Sync Hook的常见问题与解决方案

Sync Hook在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 多环境管理

### 4.1 App of Apps 模式

App of Apps 模式是GitOps与ArgoCD的重要组成部分。本节详细介绍App of Apps 模式的核心概念、工作原理和实际应用。

**关键要点**：

- App of Apps 模式的定义与核心原理
- App of Apps 模式的实现方式与技术细节
- App of Apps 模式在实际场景中的应用与最佳实践
- App of Apps 模式的常见问题与解决方案

App of Apps 模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 ApplicationSet

ApplicationSet是GitOps与ArgoCD的重要组成部分。本节详细介绍ApplicationSet的核心概念、工作原理和实际应用。

**关键要点**：

- ApplicationSet的定义与核心原理
- ApplicationSet的实现方式与技术细节
- ApplicationSet在实际场景中的应用与最佳实践
- ApplicationSet的常见问题与解决方案

ApplicationSet在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## 应用管理

**基本用法:创建应用**
`argocd app create <应用名> --repo <仓库> --path <路径> --dest-server <集群> --dest-namespace <命名空间>`

```bash
# 从 Git 仓库创建应用
argocd app create web-app \
  --repo https://github.com/org/repo.git \
  --path manifests/web \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace production

# 从 Helm Chart 创建应用
argocd app create helm-app \
  --repo https://github.com/org/charts.git \
  --path charts/nginx \
  --helm-chart nginx \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace production
```

---

**基本用法:查看应用列表**
`argocd app list`

```bash
# 列出所有应用
argocd app list

# 按命名空间筛选
argocd app list -A | grep production

# 输出 JSON 格式
argocd app list -o json | jq '.[].metadata.name'
```

---

**基本用法:查看应用详情**
`argocd app get <应用名>`

```bash
# 查看应用配置与同步状态
argocd app get web-app

# 查看应用完整 YAML
argocd app get web-app -o yaml

# 查看应用状态简报
argocd app get web-app --show-params
```

---

**基本用法:删除应用**
`argocd app delete <应用名>`

```bash
# 删除应用(保留集群中的资源)
argocd app delete web-app

# 级联删除(同时删除集群中资源)
argocd app delete web-app --cascade

# 强制删除
argocd app delete web-app --yes
```

---

## 同步操作

**基本用法:手动同步应用**
`argocd app sync <应用名>`

```bash
# 同步应用
argocd app sync web-app

# 同步指定修订版
argocd app sync web-app --revision=v1.2.0

# 同步前先刷新 Git
argocd app sync web-app --refresh

# 干运行(仅显示变更不执行)
argocd app sync web-app --dry-run
```

---

**基本用法:选择性同步**
`argocd app sync <应用名> --resource <资源>`

```bash
# 仅同步指定资源
argocd app sync web-app --resource deployment:web

# 仅同步指定资源类型
argocd app sync web-app --resource Deployment

# 排除某些资源同步
argocd app sync web-app --resource '!Service'

# 应用同步前钩子
argocd app sync web-app --apply-out-of-sync-only
```

---

**基本用法:同步策略**
`argocd app set <应用名> --sync-policy <策略>`

```bash
# 设置自动同步
argocd app set web-app --sync-policy automated

# 自动同步时自动修剪资源
argocd app set web-app --auto-prune

# 自动同步时自愈(防止手动修改)
argocd app set web-app --self-heal

# 禁用自动同步
argocd app set web-app --sync-policy none
```

---

**基本用法:查看同步状态**
`argocd app sync <应用名> --dry-run`

```bash
# 查看同步差异
argocd app diff web-app

# 查看与指定版本的差异
argocd app diff web-app --revision=HEAD

# 查看本地文件与应用差异
argocd app diff web-app --local=manifests/
```

---

## 应用配置

**基本用法:修改应用参数**
`argocd app set <应用名> [选项]`

```bash
# 设置 Helm 参数
argocd app set web-app --helm-set image.tag=v1.2.0

# 设置 Helm 参数(从文件)
argocd app set web-app --values values-production.yaml

# 设置 Kustomize 镜像
argocd app set web-app --kustomize-image web=nginx:1.25

# 修改目标命名空间
argocd app set web-app --dest-namespace staging
```

---

**基本用法:查看应用参数**
`argocd app get <应用名> --show-params`

```bash
# 显示应用所有参数
argocd app get web-app --show-params

# 查看应用 manifests
argocd app manifests web-app

# 查看应用历史
argocd app history web-app
```

---

**基本用法:回滚应用**
`argocd app rollback <应用名> <版本号>`

```bash
# 查看历史版本
argocd app history web-app

# 回滚到指定版本
argocd app rollback web-app 3

# 回滚后禁用自动同步(避免被自动同步回去)
argocd app set web-app --sync-policy none
```

---

## 仓库与项目

**基本用法:添加仓库**
`argocd repo add <仓库URL>`

```bash
# 添加 Git 仓库
argocd repo add https://github.com/org/repo.git --username user --password pass

# 添加私有仓库(SSH)
argocd repo add git@github.com:org/repo.git --ssh-private-key-path ~/.ssh/id_rsa

# 添加 HTTPS 仓库(带凭据)
argocd repo add https://github.com/org/repo.git --username ci --password $GITHUB_TOKEN
```

---

**基本用法:查看仓库**
`argocd repo list`

```bash
# 列出已配置的仓库
argocd repo list

# 测试仓库连接
argocd repo list -o json | jq '.[].repo'

# 查看仓库详情
argocd repo get https://github.com/org/repo.git
```

---

**基本用法:管理项目**
`argocd proj create <项目名>`

```bash
# 创建项目
argocd proj create my-project \
  --dest https://kubernetes.default.svc,production \
  --src https://github.com/org/repo.git

# 添加允许的目标集群
argocd proj add-destination my-project https://kubernetes.default.svc staging

# 添加允许的源仓库
argocd proj add-source my-project https://github.com/org/another-repo.git

# 查看项目列表
argocd proj list
```

---

**基本用法:项目角色与令牌**
`argocd proj role create <项目> <角色>`

```bash
# 创建项目角色
argocd proj role create my-project ci-role

# 添加策略(允许操作应用)
argocd proj role add-policy my-project ci-role \
  --action '*' --resource '*' --permission allow

# 生成角色令牌
argocd proj role create-token my-project ci-role

# 查看角色
argocd proj role get my-project ci-role
```

---

## 集群管理

**基本用法:添加集群**
`argocd cluster add <上下文名>`

```bash
# 添加当前 kubectl 上下文对应的集群
argocd cluster add my-cluster

# 添加集群到指定命名空间
argocd cluster add my-cluster --name prod-cluster -n argocd

# 添加外部集群(通过 kubeconfig)
argocd cluster add prod-cluster --kubeconfig /path/to/kubeconfig
```

---

**基本用法:查看集群**
`argocd cluster list`

```bash
# 列出所有注册的集群
argocd cluster list

# 查看集群详情
argocd cluster get https://kubernetes.default.svc

# 查看集群名称
argocd cluster list -o json | jq '.[].name'
```

---

## 账户与认证

**基本用法:登录 ArgoCD**
`argocd login <服务器地址>`

```bash
# 登录(交互式)
argocd login argocd.example.com

# 使用用户名密码登录
argocd login argocd.example.com --username admin --password $ARGOCD_PASS

# 跳过 TLS 验证(测试环境)
argocd login argocd.example.com --username admin --password $ARGOCD_PASS --insecure
```

---

**基本用法:管理账户**
`argocd account list`

```bash
# 列出所有账户
argocd account list

# 查看当前用户
argocd account get-user-info

# 修改密码
argocd account update-password

# 生成 API 令牌
argocd account generate-token
```

---

**基本用法:RBAC 配置**
`argocd account get-user-info`

```bash
# 查看当前用户权限
argocd account get-user-info

# 查看项目角色绑定
argocd proj role list my-project

# 通过 ConfigMap 编辑 RBAC 规则
kubectl edit configmap argocd-rbac-cm -n argocd
```

---

## ApplicationSet 多集群部署

**基本用法:创建 ApplicationSet**
`kubectl apply -f <appset.yaml>`

```yaml
# appset.yaml 多集群部署
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: web-multi-cluster
  namespace: argocd
spec:
  generators:
  - list:
      elements:
      - cluster: https://kubernetes.default.svc
        env: prod
      - cluster: https://staging-cluster.example.com
        env: staging
  template:
    metadata:
      name: 'web-{{env}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/org/repo.git
        targetRevision: HEAD
        path: manifests/web
      destination:
        server: '{{cluster}}'
        namespace: '{{env}}'
      syncPolicy:
        automated:
          prune: true
```

---

**基本用法:Git 生成器**
`spec.generators.git`

```yaml
# 基于 Git 目录结构生成应用
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: git-generator
  namespace: argocd
spec:
  generators:
  - git:
      repoURL: https://github.com/org/mono-repo.git
      revision: HEAD
      directories:
      - path: apps/*
  template:
    metadata:
      name: '{{path.basename}}'
    spec:
      source:
        repoURL: https://github.com/org/mono-repo.git
        targetRevision: HEAD
        path: '{{path}}'
      destination:
        server: https://kubernetes.default.svc
        namespace: '{{path.basename}}'
      syncPolicy:
        automated: {}
```

---

## 通知与钩子

**基本用法:Sync Hooks**
`metadata.annotations.argocd.argoproj.io/hook`

```yaml
# deployment-with-hook.yaml 带 PreSync 钩子
apiVersion: batch/v1
kind: Job
metadata:
  name: db-migration
  annotations:
    argocd.argoproj.io/hook: PreSync
    argocd.argoproj.io/hook-delete-policy: HookSucceeded
spec:
  template:
    spec:
      containers:
      - name: migrate
        image: migrate/migrate
        command: ["migrate", "-path", "/migrations", "-database", "$DB_URL", "up"]
      restartPolicy: Never
  backoffLimit: 3
```

---

**基本用法:配置通知**
`kubectl edit configmap argocd-notifications-cm -n argocd`

```yaml
# 通知配置示例
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-notifications-cm
  namespace: argocd
data:
  service.slack: |
    token: $slack-token
  trigger.on-deployed: |
    - when: app.status.operationState.phase in ['Succeeded']
      send: [slack-deployed]
  template.slack-deployed: |
    message: |
      {{.app.metadata.name}} 已成功部署
```

---

## 排查与诊断

**基本用法:查看应用事件**
`argocd app get <应用名> --show-operation`

```bash
# 查看最近的同步操作
argocd app get web-app --show-operation

# 查看应用资源树
argocd app resources web-app

# 查看应用同步日志
argocd app logs web-app
```

---

**基本用法:排查同步失败**
`argocd app sync <应用名> --dry-run`

```bash
# 干运行查看将同步的资源
argocd app sync web-app --dry-run

# 查看同步错误
argocd app get web-app | grep -A 20 "sync"

# 强制重新同步
argocd app sync web-app --replace --force

# 查看 ArgoCD 控制器日志
kubectl logs -n argocd -l app.kubernetes.io/name=argocd-application-controller --tail=50
```

---

**基本用法:刷新与缓存**
`argocd app get <应用名> --refresh`

```bash
# 强制刷新 Git 状态
argocd app get web-app --refresh

# 重新评估应用
argocd app get web-app --hard-refresh

# 刷新所有应用
argocd app list -o json | jq -r '.[].metadata.name' | xargs -I {} argocd app get {} --refresh
```

<!-- ============ 文档分隔线：031-devops/033-KubectlBasics.md ============ -->

## kubectl get 查看资源

**基本写法：查看指定类型资源**
`kubectl get <资源类型>`
```bash
# 查看所有 Pod
kubectl get pods
```

**基本写法：查看所有命名空间的资源**
`kubectl get <资源类型> -A`
```bash
# 查看所有命名空间的 Pod
kubectl get pods -A
```

**基本写法：查看指定命名空间资源**
`kubectl get <资源类型> -n <命名空间>`
```bash
# 查看 kube-system 命名空间的 Pod
kubectl get pods -n kube-system
```

**基本写法：显示详细信息**
`kubectl get <资源类型> -o wide`
```bash
# 查看 Pod 详细信息含 IP 和节点
kubectl get pods -o wide
```

**基本写法：输出 YAML 格式**
`kubectl get <资源类型> <名称> -o yaml`
```bash
# 输出 Pod 的完整 YAML
kubectl get pod nginx -o yaml
```

**基本写法：按标签过滤**
`kubectl get <资源类型> -l <标签选择器>`
```bash
# 查看 app=nginx 的 Pod
kubectl get pods -l app=nginx
```

---

## kubectl describe 查看详情

**基本写法：查看资源详细信息**
`kubectl describe <资源类型> <名称>`
```bash
# 查看 nginx Pod 的详细信息
kubectl describe pod nginx
```

**基本写法：查看指定命名空间资源**
`kubectl describe <资源类型> <名称> -n <命名空间>`
```bash
# 查看 kube-system 命名空间的 Pod
kubectl describe pod kube-apiserver -n kube-system
```

**基本写法：查看节点详情**
`kubectl describe node <节点名>`
```bash
# 查看节点详细信息
kubectl describe node node1
```

---

## kubectl create 创建资源

**基本写法：创建 Deployment**
`kubectl create deployment <名称> --image=<镜像>`
```bash
# 创建 nginx Deployment
kubectl create deployment nginx --image=nginx
```

**基本写法：指定副本数创建**
`kubectl create deployment <名称> --image=<镜像> --replicas=<数量>`
```bash
# 创建 3 副本的 nginx Deployment
kubectl create deployment nginx --image=nginx --replicas=3
```

**基本写法：创建命名空间**
`kubectl create namespace <名称>`
```bash
# 创建新命名空间
kubectl create namespace dev
```

**基本写法：创建 Secret**
`kubectl create secret generic <名称> --from-literal=<键>=<值>`
```bash
# 创建包含密码的 Secret
kubectl create secret generic db-secret --from-literal=password=secret123
```

---

## kubectl apply 应用配置

**基本写法：应用 YAML 文件**
`kubectl apply -f <文件>`
```bash
# 应用 deployment.yaml
kubectl apply -f deployment.yaml
```

**基本写法：应用目录下所有文件**
`kubectl apply -f <目录>`
```bash
# 应用 k8s 目录下所有 YAML
kubectl apply -f ./k8s/
```

**基本写法：从 URL 应用**
`kubectl apply -f <URL>`
```bash
# 从 URL 应用配置
kubectl apply -f https://raw.githubusercontent.com/example/repo/main/deploy.yaml
```

**基本写法：使用 kustomize**
`kubectl apply -k <目录>`
```bash
# 使用 kustomize 应用配置
kubectl apply -k ./overlays/prod
```

---

## kubectl delete 删除资源

**基本写法：删除指定资源**
`kubectl delete <资源类型> <名称>`
```bash
# 删除 nginx Pod
kubectl delete pod nginx
```

**基本写法：从文件删除资源**
`kubectl delete -f <文件>`
```bash
# 删除 deployment.yaml 中定义的资源
kubectl delete -f deployment.yaml
```

**基本写法：按标签删除**
`kubectl delete <资源类型> -l <标签选择器>`
```bash
# 删除所有 app=test 的 Pod
kubectl delete pods -l app=test
```

**基本写法：强制删除 Pod**
`kubectl delete pod <名称> --grace-period=0 --force`
```bash
# 强制立即删除 Pod
kubectl delete pod nginx --grace-period=0 --force
```

---

## kubectl exec 进入容器

**基本写法：进入容器 shell**
`kubectl exec -it <Pod> -- <shell>`
```bash
# 进入 nginx Pod 的 bash
kubectl exec -it nginx -- bash
```

**基本写法：在容器中执行命令**
`kubectl exec <Pod> -- <命令>`
```bash
# 查看 Pod 中的进程
kubectl exec nginx -- ps aux
```

**基本写法：指定容器执行**
`kubectl exec -it <Pod> -c <容器名> -- <shell>`
```bash
# 进入指定容器
kubectl exec -it pod1 -c sidecar -- sh
```

---

## kubectl logs 查看日志

**基本写法：查看 Pod 日志**
`kubectl logs <Pod>`
```bash
# 查看 nginx Pod 的日志
kubectl logs nginx
```

**基本写法：实时跟踪日志**
`kubectl logs -f <Pod>`
```bash
# 实时跟踪日志输出
kubectl logs -f nginx
```

**基本写法：查看指定容器日志**
`kubectl logs <Pod> -c <容器名>`
```bash
# 查看 sidecar 容器的日志
kubectl logs pod1 -c sidecar
```

**基本写法：查看前次容器日志**
`kubectl logs <Pod> --previous`
```bash
# 查看容器崩溃前的日志
kubectl logs nginx --previous
```

**基本写法：查看指定时间段的日志**
`kubectl logs <Pod> --since=<时间>`
```bash
# 查看最近 1 小时的日志
kubectl logs nginx --since=1h
```

---

## kubectl scale 伸缩副本

**基本写法：扩缩容 Deployment**
`kubectl scale deployment <名称> --replicas=<数量>`
```bash
# 将 nginx 扩展到 5 个副本
kubectl scale deployment nginx --replicas=5
```

**基本写法：缩容到 0**
`kubectl scale deployment <名称> --replicas=0`
```bash
# 停止所有 nginx 副本
kubectl scale deployment nginx --replicas=0
```

**基本写法：基于文件扩缩容**
`kubectl scale -f <文件> --replicas=<数量>`
```bash
# 基于 YAML 文件扩缩容
kubectl scale -f deployment.yaml --replicas=3
```

---

## kubectl port-forward 端口转发

**基本写法：转发 Pod 端口**
`kubectl port-forward <Pod> <宿主端口>:<容器端口>`
```bash
# 将本地 8080 转发到 Pod 的 80
kubectl port-forward nginx 8080:80
```

**基本写法：转发 Service 端口**
`kubectl port-forward svc/<Service> <宿主端口>:<服务端口>`
```bash
# 转发 Service 端口到本地
kubectl port-forward svc/nginx 8080:80
```

**基本写法：绑定指定地址**
`kubectl port-forward <Pod> <地址>:<宿主端口>:<容器端口>`
```bash
# 绑定到所有地址
kubectl port-forward nginx 0.0.0.0:8080:80
```

---

## kubectl config 配置管理

**基本写法：查看当前上下文**
`kubectl config current-context`
```bash
# 查看当前使用的上下文
kubectl config current-context
```

**基本写法：切换上下文**
`kubectl config use-context <上下文>`
```bash
# 切换到生产环境上下文
kubectl config use-context prod-cluster
```

**基本写法：列出所有上下文**
`kubectl config get-contexts`
```bash
# 列出所有可用的上下文
kubectl config get-contexts
```

**基本写法：设置默认命名空间**
`kubectl config set-context --current --namespace=<命名空间>`
```bash
# 设置当前上下文的默认命名空间
kubectl config set-context --current --namespace=dev
```

<!-- ============ 文档分隔线：031-devops/034-HelmCommands.md ============ -->

## helm install 安装 Chart

**基本写法：安装 Chart**
`helm install <名称> <Chart>`
```bash
# 安装 nginx Chart
helm install my-nginx bitnami/nginx
```

**基本写法：指定命名空间安装**
`helm install <名称> <Chart> -n <命名空间>`
```bash
# 在 dev 命名空间安装
helm install my-nginx bitnami/nginx -n dev
```

**基本写法：通过 values 文件安装**
`helm install <名称> <Chart> -f <values文件>`
```bash
# 使用自定义 values 安装
helm install my-nginx bitnami/nginx -f custom-values.yaml
```

**基本写法：命令行传参安装**
`helm install <名称> <Chart> --set <键>=<值>`
```bash
# 设置副本数和镜像版本
helm install my-nginx bitnami/nginx --set replicaCount=3 --set image.tag=1.25
```

**基本写法：本地 Chart 安装**
`helm install <名称> <路径>`
```bash
# 安装本地 Chart
helm install my-app ./mychart
```

---

## helm upgrade 升级 Chart

**基本写法：升级 Release**
`helm upgrade <名称> <Chart>`
```bash
# 升级 my-nginx Chart
helm upgrade my-nginx bitnami/nginx
```

**基本写法：升级并安装**
`helm upgrade <名称> <Chart> --install`
```bash
# 不存在则安装，存在则升级
helm upgrade my-nginx bitnami/nginx --install
```

**基本写法：使用新 values 升级**
`helm upgrade <名称> <Chart> -f <values文件>`
```bash
# 使用新配置升级
helm upgrade my-nginx bitnami/nginx -f new-values.yaml
```

**基本写法：命令行传参升级**
`helm upgrade <名称> <Chart> --set <键>=<值>`
```bash
# 通过命令行参数升级
helm upgrade my-nginx bitnami/nginx --set replicaCount=5
```

---

## helm uninstall 卸载 Chart

**基本写法：卸载 Release**
`helm uninstall <名称>`
```bash
# 卸载 my-nginx Release
helm uninstall my-nginx
```

**基本写法：指定命名空间卸载**
`helm uninstall <名称> -n <命名空间>`
```bash
# 卸载指定命名空间的 Release
helm uninstall my-nginx -n dev
```

**基本写法：保留历史记录卸载**
`helm uninstall <名称> --keep-history`
```bash
# 卸载但保留历史记录
helm uninstall my-nginx --keep-history
```

---

## helm list 查看 Release

**基本写法：查看所有 Release**
`helm list`
```bash
# 列出所有已安装的 Release
helm list
```

**基本写法：查看所有命名空间的 Release**
`helm list -A`
```bash
# 列出所有命名空间的 Release
helm list -A
```

**基本写法：包含已卸载的 Release**
`helm list --all`
```bash
# 列出包含已卸载的所有 Release
helm list --all
```

**基本写法：查看指定命名空间**
`helm list -n <命名空间>`
```bash
# 查看 dev 命名空间的 Release
helm list -n dev
```

---

## helm search 搜索 Chart

**基本写法：搜索 Hub 上的 Chart**
`helm search hub <关键词>`
```bash
# 搜索 nginx 相关的 Chart
helm search hub nginx
```

**基本写法：搜索已添加仓库的 Chart**
`helm search repo <关键词>`
```bash
# 在已添加的仓库中搜索
helm search repo nginx
```

---

## helm repo 仓库管理

**基本写法：添加仓库**
`helm repo add <名称> <URL>`
```bash
# 添加 bitnami 仓库
helm repo add bitnami https://charts.bitnami.com/bitnami
```

**基本写法：更新仓库**
`helm repo update`
```bash
# 更新所有已添加的仓库
helm repo update
```

**基本写法：列出所有仓库**
`helm repo list`
```bash
# 列出所有已添加的仓库
helm repo list
```

**基本写法：删除仓库**
`helm repo remove <名称>`
```bash
# 删除 bitnami 仓库
helm repo remove bitnami
```

---

## helm pull 下载 Chart

**基本写法：下载 Chart**
`helm pull <仓库>/<Chart>`
```bash
# 下载 nginx Chart
helm pull bitnami/nginx
```

**基本写法：下载并解压**
`helm pull <仓库>/<Chart> --untar`
```bash
# 下载并解压到当前目录
helm pull bitnami/nginx --untar
```

**基本写法：指定版本下载**
`helm pull <仓库>/<Chart> --version <版本>`
```bash
# 下载指定版本
helm pull bitnami/nginx --version 15.0.0
```

**基本写法：指定下载目录**
`helm pull <仓库>/<Chart> --untar --untardir <目录>`
```bash
# 解压到指定目录
helm pull bitnami/nginx --untar --untardir ./charts
```

---

## helm create 创建 Chart

**基本写法：创建新 Chart**
`helm create <名称>`
```bash
# 创建名为 myapp 的 Chart
helm create myapp
```

**基本写法：指定 Chart 路径**
`helm create <路径>/<名称>`
```bash
# 在指定路径创建 Chart
helm create ./charts/myapp
```

---

## helm template 渲染模板

**基本写法：渲染模板**
`helm template <名称> <Chart>`
```bash
# 渲染 myapp Chart 的模板
helm template myapp ./mychart
```

**基本写法：使用 values 渲染**
`helm template <名称> <Chart> -f <values文件>`
```bash
# 使用 values 渲染模板
helm template myapp ./mychart -f values.yaml
```

**基本写法：命令行传参渲染**
`helm template <名称> <Chart> --set <键>=<值>`
```bash
# 通过命令行参数渲染
helm template myapp ./mychart --set image.tag=v2
```

---

## helm history/rollback 回滚

**基本写法：查看 Release 历史**
`helm history <名称>`
```bash
# 查看 my-nginx 的历史版本
helm history my-nginx
```

**基本写法：回滚到指定版本**
`helm rollback <名称> <版本号>`
```bash
# 回滚到版本 2
helm rollback my-nginx 2
```

---

## helm status 查看 Release 状态

**基本写法：查看 Release 状态**
`helm status <名称>`
```bash
# 查看 my-nginx 的状态
helm status my-nginx
```

**基本写法：查看指定命名空间状态**
`helm status <名称> -n <命名空间>`
```bash
# 查看 dev 命名空间的 Release 状态
helm status my-nginx -n dev
```

**基本写法：显示资源信息**
`helm status <名称> --show-resources`
```bash
# 显示 Release 相关的所有资源
helm status my-nginx --show-resources
```

---

## helm show 查看 Chart 信息

**基本写法：查看 Chart 的 values**
`helm show values <Chart>`
```bash
# 查看 nginx Chart 的默认 values
helm show values bitnami/nginx
```

**基本写法：查看 Chart 信息**
`helm show chart <Chart>`
```bash
# 查看 Chart 的 Chart.yaml 内容
helm show chart bitnami/nginx
```

**基本写法：查看 Chart 全部信息**
`helm show all <Chart>`
```bash
# 查看 Chart 的所有信息
helm show all bitnami/nginx
```

<!-- ============ 文档分隔线：031-devops/035-JenkinsPipeline.md ============ -->

## pipeline 声明式流水线

**基本写法：定义声明式 pipeline**
```groovy
`pipeline {
    agent any
    stages {
        stage('<阶段名>') {
            steps {
                <步骤>
            }
        }
    }
}`
```
```groovy
// 基本声明式流水线
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'make build'
            }
        }
    }
}
```

---

## agent 代理配置

**基本写法：使用任意节点**
`agent any`
```groovy
// 在任意可用节点执行
pipeline {
    agent any
}
```

**基本写法：使用指定标签节点**
`agent { label '<标签>' }`
```groovy
// 在带 docker 标签的节点执行
pipeline {
    agent { label 'docker' }
}
```

**基本写法：使用 Docker 镜像**
`agent { docker { image '<镜像>' } }`
```groovy
// 在 maven 容器中执行
pipeline {
    agent { docker { image 'maven:3.8-openjdk-11' } }
}
```

**基本写法：不分配节点**
`agent none`
```groovy
// 不分配节点，由各 stage 指定
pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'build' }
            steps { sh 'make build' }
        }
    }
}
```

---

## environment 环境变量

**基本写法：定义环境变量**
```groovy
`environment {
    <变量名> = '<值>'
}`
```
```groovy
// 定义构建环境变量
pipeline {
    agent any
    environment {
        VERSION = '1.0.0'
        BUILD_ENV = 'production'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building version ${VERSION}"
            }
        }
    }
}
```

**基本写法：使用 credentials**
```groovy
`environment {
    <变量> = credentials('<凭据ID>')
}`
```
```groovy
// 使用 Jenkins 存储的凭据
pipeline {
    agent any
    environment {
        DOCKER_PASSWORD = credentials('docker-hub-credentials')
    }
}
```

---

## stages 阶段定义

**基本写法：定义多个阶段**
```groovy
`stages {
    stage('<阶段1>') { steps { ... } }
    stage('<阶段2>') { steps { ... } }
}`
```
```groovy
// 完整的 CI/CD 阶段
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
```

---

## steps 步骤

**基本写法：执行 shell 命令**
`sh '<命令>'`
```groovy
// 执行 shell 命令
steps {
    sh 'echo hello'
    sh 'make build'
}
```

**基本写法：执行脚本并获取结果**
`sh script: '<命令>', returnStdout: true`
```groovy
// 获取命令输出
steps {
    script {
        def version = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
        echo "Commit: ${version}"
    }
}
```

**基本写法：打印消息**
`echo '<消息>'`
```groovy
// 打印消息
steps {
    echo 'Starting build process'
}
```

---

## when 条件执行

**基本写法：分支条件**
```groovy
`when {
    branch '<分支名>'
}`
```
```groovy
// 只在 main 分支执行部署
stage('Deploy') {
    when {
        branch 'main'
    }
    steps {
        sh 'kubectl apply -f k8s/'
    }
}
```

**基本写法：表达式条件**
```groovy
`when {
    expression { <条件> }
}`
```
```groovy
// 满足条件时执行
stage('Deploy') {
    when {
        expression { env.BRANCH_NAME == 'main' && params.DEPLOY == true }
    }
    steps {
        sh 'deploy.sh'
    }
}
```

**基本写法：环境变量条件**
```groovy
`when {
    environment name: '<变量>', value: '<值>'
}`
```
```groovy
// 根据 DEPLOY_TO 变量执行
stage('Deploy Prod') {
    when {
        environment name: 'DEPLOY_TO', value: 'production'
    }
    steps {
        sh 'deploy-prod.sh'
    }
}
```

---

## post 构建后操作

**基本写法：成功后操作**
```groovy
`post {
    success { <步骤> }
}`
```
```groovy
// 构建成功后通知
pipeline {
    agent any
    stages { /* ... */ }
    post {
        success {
            echo 'Build succeeded!'
            sh 'curl -X POST https://hooks.slack.com/...'
        }
    }
}
```

**基本写法：失败后操作**
```groovy
`post {
    failure { <步骤> }
}`
```
```groovy
// 构建失败后通知
post {
    failure {
        echo 'Build failed!'
        emailext to: 'team@example.com', subject: 'Build Failed', body: 'Check logs'
    }
}
```

**基本写法：总是执行**
```groovy
`post {
    always { <步骤> }
}`
```
```groovy
// 无论成功失败都清理
post {
    always {
        sh 'docker system prune -f'
        cleanWs()
    }
}
```

---

## parameters 参数化构建

**基本写法：字符串参数**
```groovy
`parameters {
    string(name: '<名称>', defaultValue: '<默认值>', description: '<描述>')
}`
```
```groovy
// 定义字符串参数
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: '构建分支')
    }
    stages {
        stage('Build') {
            steps {
                git branch: params.BRANCH, url: 'https://github.com/repo.git'
            }
        }
    }
}
```

**基本写法：布尔参数**
```groovy
`parameters {
    booleanParam(name: '<名称>', defaultValue: <布尔值>, description: '<描述>')
}`
```
```groovy
// 定义部署开关
parameters {
    booleanParam(name: 'DEPLOY', defaultValue: false, description: '是否部署')
}
```

**基本写法：选项参数**
```groovy
`parameters {
    choice(name: '<名称>', choices: ['<选项1>', '<选项2>'], description: '<描述>')
}`
```
```groovy
// 定义环境选择
parameters {
    choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: '部署环境')
}
```

---

## script 脚本块

**基本写法：执行 Groovy 脚本**
```groovy
`script {
    <Groovy 代码>
}`
```
```groovy
// 在 pipeline 中执行 Groovy
steps {
    script {
        def servers = ['server1', 'server2', 'server3']
        for (server in servers) {
            sh "ssh ${server} 'deploy.sh'"
        }
    }
}
```

---

## 并行执行

**基本写法：并行阶段**
```groovy
`parallel {
    stage('<阶段1>') { steps { ... } }
    stage('<阶段2>') { steps { ... } }
}`
```
```groovy
// 并行执行测试
stage('Test') {
    parallel {
        stage('Unit Test') {
            steps {
                sh 'npm run test:unit'
            }
        }
        stage('Integration Test') {
            steps {
                sh 'npm run test:integration'
            }
        }
    }
}
```

---

## artifacts 归档

**基本写法：归档构建产物**
`archiveArtifacts '<路径>'`
```groovy
// 归档构建产物
steps {
    sh 'make build'
    archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
}
```

**基本写法：归档测试报告**
`junit '<报告路径>'`
```groovy
// 归档 JUnit 测试报告
steps {
    sh 'npm test'
    junit 'reports/**/*.xml'
}
```

---

## 触发器

**基本写法：定时触发**
```groovy
`triggers {
    cron('<Cron 表达式>')
}`
```
```groovy
// 每天凌晨 2 点构建
pipeline {
    agent any
    triggers {
        cron('H 2 * * *')
    }
    stages { /* ... */ }
}
```

**基本写法：上游触发**
```groovy
`triggers {
    upstream(upstreamProjects: '<项目>', threshold: hudson.model.Result.SUCCESS)
}`
```
```groovy
// 上游项目成功后触发
triggers {
    upstream(upstreamProjects: 'my-app-build', threshold: hudson.model.Result.SUCCESS)
}
```

<!-- ============ 文档分隔线：031-devops/036-GitLabCI.md ============ -->

## .gitlab-ci.yml 基本结构

**基本写法：定义流水线**
```yaml
`stages:
  - <阶段1>
  - <阶段2>
<作业名>:
  stage: <阶段>
  script:
    - <命令>`
```
```yaml
# 基本的 GitLab CI 流水线
stages:
  - build
  - test
  - deploy
build:
  stage: build
  script:
    - echo "Building the app"
    - make build
```

---

## image 镜像配置

**基本写法：全局镜像**
```yaml
`image: <镜像>`
```
```yaml
# 全局使用 node 镜像
image: node:18
stages:
  - build
build:
  stage: build
  script:
    - npm install
```

**基本写法：作业级镜像**
```yaml
`<作业名>:
  image: <镜像>
  script:
    - <命令>`
```
```yaml
# 不同作业使用不同镜像
build:
  image: maven:3.8-openjdk-11
  script:
    - mvn package
test:
  image: node:18
  script:
    - npm test
```

---

## stages 阶段定义

**基本写法：定义阶段顺序**
```yaml
`stages:
  - <阶段1>
  - <阶段2>
  - <阶段3>`
```
```yaml
# 定义完整的 CI/CD 阶段
stages:
  - build
  - test
  - deploy
  - cleanup
```

---

## script 执行命令

**基本写法：单行命令**
```yaml
`<作业名>:
  script:
    - <命令>`
```
```yaml
# 执行单条命令
build:
  script:
    - echo "Hello GitLab CI"
```

**基本写法：多行命令**
```yaml
`<作业名>:
  script:
    - <命令1>
    - <命令2>
    - <命令3>`
```
```yaml
# 执行多条命令
build:
  script:
    - npm install
    - npm run build
    - npm run test
```

**基本写法：多行脚本块**
```yaml
`<作业名>:
  script:
    - |
      <多行脚本>`
```
```yaml
# 使用多行脚本块
build:
  script:
    - |
      echo "Starting build"
      npm install
      npm run build
      echo "Build complete"
```

---

## before_script/after_script

**基本写法：全局前置脚本**
```yaml
`before_script:
  - <命令>`
```
```yaml
# 全局前置命令
before_script:
  - apt-get update -y
  - apt-get install -y curl
stages:
  - build
build:
  script:
    - make build
```

**基本写法：作业级前置脚本**
```yaml
`<作业名>:
  before_script:
    - <命令>
  script:
    - <命令>`
```
```yaml
test:
  before_script:
    - npm install
  script:
    - npm test
```

**基本写法：后置脚本**
```yaml
`after_script:
  - <命令>`
```
```yaml
# 全局后置命令
after_script:
  - echo "Pipeline finished"
  - docker system prune -f
```

---

## rules 规则控制

**基本写法：分支规则**
```yaml
`<作业名>:
  rules:
    - if: '$CI_COMMIT_BRANCH == "<分支>"'
      when: on`
```
```yaml
# 只在 main 分支执行
deploy:
  stage: deploy
  script:
    - kubectl apply -f k8s/
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: on
```

**基本写法：多条件规则**
```yaml
`<作业名>:
  rules:
    - if: '<条件1>'
      when: on
    - if: '<条件2>'
      when: never`
```
```yaml
# 多条件控制
deploy:
  script:
    - deploy.sh
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: on
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
      when: never
```

**基本写法：变更文件触发**
```yaml
`<作业名>:
  rules:
    - changes:
        - <文件路径>`
```
```yaml
# 文件变更时触发
build:
  script:
    - make build
  rules:
    - changes:
        - src/**/*
        - Dockerfile
```

---

## only/except 作业控制

**基本写法：指定分支执行**
```yaml
`<作业名>:
  only:
    - <分支>`
```
```yaml
# 只在 main 分支执行
deploy:
  only:
    - main
  script:
    - deploy.sh
```

**基本写法：排除分支**
```yaml
`<作业名>:
  except:
    - <分支>`
```
```yaml
# 除 main 分支外都执行
test:
  except:
    - main
  script:
    - npm test
```

**基本写法：标签触发**
```yaml
`<作业名>:
  only:
    - tags`
```
```yaml
# 只在打标签时执行
release:
  only:
    - tags
  script:
    - publish.sh
```

---

## variables 变量

**基本写法：全局变量**
```yaml
`variables:
  <变量名>: "<值>"`
```
```yaml
# 定义全局变量
variables:
  IMAGE_NAME: "myapp"
  IMAGE_TAG: "latest"
build:
  script:
    - docker build -t $IMAGE_NAME:$IMAGE_TAG .
```

**基本写法：作业级变量**
```yaml
`<作业名>:
  variables:
    <变量名>: "<值>"`
```
```yaml
deploy_prod:
  variables:
    ENV: "production"
  script:
    - deploy.sh $ENV
```

---

## cache 缓存

**基本写法：缓存路径**
```yaml
`cache:
  paths:
    - <路径>`
```
```yaml
# 缓存 node_modules
cache:
  paths:
    - node_modules/
build:
  script:
    - npm install
    - npm run build
```

**基本写法：缓存键**
```yaml
`cache:
  key: <键>
  paths:
    - <路径>`
```
```yaml
# 按分支缓存
cache:
  key: $CI_COMMIT_REF_SLUG
  paths:
    - node_modules/
    - .npm/
```

**基本写法：缓存策略**
```yaml
`cache:
  paths:
    - <路径>
  policy: <策略>`
```
```yaml
# 拉取缓存但不更新
test:
  cache:
    paths:
      - node_modules/
    policy: pull
  script:
    - npm test
```

---

## artifacts 产物

**基本写法：归档产物**
```yaml
`<作业名>:
  artifacts:
    paths:
      - <路径>`
```
```yaml
# 归档构建产物
build:
  script:
    - make build
  artifacts:
    paths:
      - target/*.jar
```

**基本写法：设置产物过期时间**
```yaml
`<作业名>:
  artifacts:
    paths:
      - <路径>
    expire_in: <时间>`
```
```yaml
# 产物保留 1 周
build:
  artifacts:
    paths:
      - target/*.jar
    expire_in: 1 week
```

**基本写法：归档测试报告**
```yaml
`<作业名>:
  artifacts:
    reports:
      junit: <报告路径>`
```
```yaml
# 归档 JUnit 测试报告
test:
  artifacts:
    reports:
      junit: reports/**/*.xml
  script:
    - npm test
```

---

## environment 部署环境

**基本写法：定义环境**
```yaml
`<作业名>:
  environment:
    name: <环境名>`
```
```yaml
# 部署到生产环境
deploy_prod:
  stage: deploy
  environment:
    name: production
  script:
    - kubectl apply -f k8s/prod/
  only:
    - main
```

**基本写法：指定环境 URL**
```yaml
`<作业名>:
  environment:
    name: <环境名>
    url: <URL>`
```
```yaml
# 部署到 staging 环境并指定 URL
deploy_staging:
  environment:
    name: staging
    url: https://staging.example.com
  script:
    - deploy.sh staging
```

---

## services 服务

**基本写法：使用服务容器**
```yaml
`services:
  - <镜像>`
```
```yaml
# 使用 MySQL 服务
services:
  - mysql:8.0
variables:
  MYSQL_DATABASE: testdb
  MYSQL_ROOT_PASSWORD: secret
test:
  script:
    - npm test
```

**基本写法：给服务设置别名**
```yaml
`services:
  - name: <镜像>
    alias: <别名>`
```
```yaml
# 使用 redis 服务并设置别名
services:
  - name: redis:7
    alias: redis-cache
test:
  script:
    - REDIS_HOST=redis-cache npm test
```

---

## retry 重试

**基本写法：作业重试**
```yaml
`<作业名>:
  retry: <次数>`
```
```yaml
# 失败时重试 2 次
test:
  retry: 2
  script:
    - npm test
```

**基本写法：指定重试条件**
```yaml
`<作业名>:
  retry:
    max: <次数>
    when: <条件>`
```
```yaml
# 仅在 runner 失败时重试
deploy:
  retry:
    max: 2
    when: runner_system_failure
  script:
    - deploy.sh
```
