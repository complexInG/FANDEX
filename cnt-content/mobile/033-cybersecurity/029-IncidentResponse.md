# Cybersecurity 应急响应命令

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 系统信息收集

**基本写法:查看系统基本信息**
`uname -a && cat /etc/os-release`
```bash
# 收集系统版本与内核信息
uname -a && cat /etc/os-release
```

**基本写法:查看运行时长**
`uptime`
```bash
# 查看系统运行时间与负载
uptime
```

**基本写法:查看登录用户**
`w`
```bash
# 查看当前登录的所有用户
w
```

**基本写法:查看用户登录历史**
`last | head -20`
```bash
# 查看最近登录历史记录
last | head -20
```

**基本写法:查看失败登录记录**
`lastb | head -20`
```bash
# 查看失败登录记录
sudo lastb | head -20
```

---

## 进程分析

**基本写法:查看所有进程**
`ps auxf`
```bash
# 查看所有进程与父子关系
ps auxf
```

**基本写法:查看 CPU 占用最高的进程**
`ps aux --sort=-%cpu | head -10`
```bash
# 找出 CPU 占用最高的 10 个进程
ps aux --sort=-%cpu | head -10
```

**基本写法:查看内存占用最高的进程**
`ps aux --sort=-%mem | head -10`
```bash
# 找出内存占用最高的 10 个进程
ps aux --sort=-%mem | head -10
```

**基本写法:查找隐藏进程**
`ps -ef | awk '{print $2}' | sort | uniq -d`
```bash
# 查找重复 PID 的可疑进程
ps -ef | awk '{print $2}' | sort | uniq -d
```

**基本写法:对比 /proc 与 ps**
`ls -d /proc/[0-9]* | awk -F/ '{print $3}' | sort > /tmp/proc.txt; ps -ef | awk 'NR>1{print $2}' | sort > /tmp/ps.txt; diff /tmp/proc.txt /tmp/ps.txt`
```bash
# 对比 /proc 与 ps 结果查找隐藏进程
comm -23 <(ls -d /proc/[0-9]* | awk -F/ '{print $3}' | sort) <(ps -ef | awk 'NR>1{print $2}' | sort)
```

---

## 网络连接分析

**基本写法:查看所有网络连接**
`netstat -tunlap`
```bash
# 查看所有 TCP/UDP 连接与监听端口
sudo netstat -tunlap
```

**基本写法:查看监听端口**
`ss -tlnp`
```bash
# 查看所有 TCP 监听端口与进程
sudo ss -tlnp
```

**基本写法:查找异常连接**
`netstat -anp | grep ESTABLISHED`
```bash
# 查看所有已建立的连接
sudo netstat -anp | grep ESTABLISHED
```

**基本写法:查找监听异常端口**
`ss -tlnp | grep -vE ":(22|80|443|8080)"`
```bash
# 查找非标准端口的监听服务
sudo ss -tlnp | grep -vE ":(22|80|443|8080)"
```

**基本写法:查看网络接口**
`ip addr && ip route`
```bash
# 查看网络接口与路由表
ip addr && ip route
```

---

## 文件系统取证

**基本写法:查找最近修改的文件**
`find / -mtime -1 -type f 2>/dev/null`
```bash
# 查找最近 24 小时内修改的文件
sudo find / -mtime -1 -type f 2>/dev/null
```

**基本写法:查找 SUID 文件**
`find / -perm -4000 -type f 2>/dev/null`
```bash
# 查找所有 SUID 权限文件(可能被植入后门)
sudo find / -perm -4000 -type f 2>/dev/null
```

**基本写法:查找隐藏文件**
`find / -name ".*" -type f 2>/dev/null | head`
```bash
# 查找所有隐藏文件
sudo find / -name ".*" -type f 2>/dev/null | head -20
```

**基本写法:查找可疑可执行文件**
`find /tmp /var/tmp /dev/shm -type f -executable 2>/dev/null`
```bash
# 查找临时目录中的可执行文件
sudo find /tmp /var/tmp /dev/shm -type f -executable 2>/dev/null
```

**基本写法:查找最近创建的文件**
`find / -mmin -60 -type f 2>/dev/null`
```bash
# 查找最近 60 分钟内创建的文件
sudo find / -mmin -60 -type f 2>/dev/null
```

---

## 用户与权限分析

**基本写法:查看所有用户**
`cat /etc/passwd | grep -v nologin | grep -v false`
```bash
# 查看可登录的用户账户
cat /etc/passwd | grep -v nologin | grep -v false
```

**基本写法:查看 UID 为 0 的用户**
`awk -F: '$3 == 0 {print $1}' /etc/passwd`
```bash
# 查找 UID 为 0 的用户(正常应只有 root)
awk -F: '$3 == 0 {print $1}' /etc/passwd
```

**基本写法:查看 sudo 权限用户**
`cat /etc/sudoers | grep -v "^#" | grep -v "^$"`
```bash
# 查看具有 sudo 权限的用户
sudo cat /etc/sudoers | grep -v "^#" | grep -v "^$"
```

**基本写法:查看空密码用户**
`awk -F: '($2 == "") {print $1}' /etc/shadow`
```bash
# 查找密码为空的用户
sudo awk -F: '($2 == "") {print $1}' /etc/shadow
```

**基本写法:查看用户最后登录时间**
`lastlog | grep -v "Never"`
```bash
# 查看所有用户的最后登录时间
lastlog | grep -v "Never logged in"
```

---

## 计划任务检查

**基本写法:查看 cron 任务**
`crontab -l && ls -la /etc/cron.*`
```bash
# 查看当前用户 cron 任务与系统 cron 配置
crontab -l && ls -la /etc/cron.*
```

**基本写法:查看系统级 cron**
`cat /etc/crontab`
```bash
# 查看系统级 cron 任务
cat /etc/crontab
```

**基本写法:查看 cron 目录**
`ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/`
```bash
# 查看 cron 目录中的定时任务
ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/ /etc/cron.weekly/ /etc/cron.monthly/
```

**基本写法:查看所有用户 cron**
`for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l 2>/dev/null; done`
```bash
# 查看所有用户的 cron 任务
for user in $(cut -f1 -d: /etc/passwd); do echo "用户 $user:"; sudo crontab -u $user -l 2>/dev/null; done
```

**基本写法:查看 systemd 定时器**
`systemctl list-timers --all`
```bash
# 查看 systemd 定时任务
systemctl list-timers --all
```

---

## 内存与启动项分析

**基本写法:查看内存使用**
`free -m && vmstat 1 5`
```bash
# 查看内存使用与虚拟内存统计
free -m && vmstat 1 5
```

**基本写法:查看启动项**
`systemctl list-unit-files --state=enabled`
```bash
# 查看开机自启服务
systemctl list-unit-files --state=enabled
```

**基本写法:查看 rc.local**
`cat /etc/rc.local`
```bash
# 查看 rc.local 启动脚本
cat /etc/rc.local 2>/dev/null
```

**基本写法:查看 init.d 服务**
`ls /etc/init.d/`
```bash
# 查看传统 init 服务
ls -la /etc/init.d/
```

**基本写法:检查内核模块**
`lsmod | grep -vE "^Module|^$" | sort`
```bash
# 查看加载的内核模块
lsmod | grep -vE "^Module|^$" | sort
```

---

## 恶意软件检测

**基本写法:扫描 rootkit**
`rkhunter --check`
```bash
# 使用 rkhunter 扫描 rootkit
sudo rkhunter --check --sk
```

**基本写法:更新 rkhunter 数据库**
`rkhunter --update`
```bash
# 更新 rkhunter 数据库
sudo rkhunter --update
```

**基本写法:chkrootkit 扫描**
`chkrootkit`
```bash
# 使用 chkrootkit 扫描 rootkit
sudo chkrootkit
```

**基本写法:ClamAV 病毒扫描**
`clamscan -r /`
```bash
# 使用 ClamAV 扫描整个文件系统
sudo clamscan -r --max-filesize=100M /
```

**基本写法:扫描特定目录**
`clamscan -r /home /tmp /var/tmp`
```bash
# 扫描用户主目录与临时目录
sudo clamscan -r /home /tmp /var/tmp
```

---

## 数据收集与取证

**基本写法:收集系统快照**
`./sysinfo.sh`
```bash
# 使用 sysinfo 工具收集系统信息
# sysinfo -o /tmp/system_info.txt
```

**基本写法:打包日志文件**
`tar -czf logs.tar.gz /var/log/`
```bash
# 打包日志用于取证分析
sudo tar -czf /tmp/logs.tar.gz /var/log/
```

**基本写法:制作内存镜像**
`dd if=/dev/mem of=/tmp/memory.dump`
```bash
# 制作内存镜像用于取证(需 root)
sudo dd if=/dev/mem of=/tmp/memory.dump bs=1M
```

**基本写法:计算文件哈希**
`sha256sum <文件>`
```bash
# 计算文件 SHA256 哈希保证取证完整性
sha256sum /tmp/logs.tar.gz
```

**基本写法:使用 LiME 制作内存镜像**
`insmod lime.ko "path=/tmp/memory.lime format=lime"`
```bash
# 使用 LiME 内核模块制作内存镜像
sudo insmod lime.ko "path=/tmp/memory.lime format=lime"
```

---

## 应急响应处置

**基本写法:隔离主机网络**
`ifconfig <接口> down`
```bash
# 立即断开网络隔离受感染主机
sudo ifconfig eth0 down
```

**基本写法:终止可疑进程**
`kill -9 <PID>`
```bash
# 强制终止可疑进程
sudo kill -9 12345
```

**基本写法:封禁恶意 IP**
`iptables -A INPUT -s <IP> -j DROP`
```bash
# 通过 iptables 阻断恶意 IP
sudo iptables -A INPUT -s 203.0.113.10 -j DROP
```

**基本写法:禁用用户账户**
`passwd -l <用户>`
```bash
# 锁定可疑用户账户
sudo passwd -l suspicious_user
```

**基本写法:关闭受感染服务**
`systemctl stop <服务>`
```bash
# 立即停止受感染服务
sudo systemctl stop vulnerable_service
```

---

## 事后清理与恢复

**基本写法:清除恶意文件**
`rm -f <文件路径>`
```bash
# 删除已确认的恶意文件
sudo rm -f /tmp/malware.sh
```

**基本写法:清除 cron 后门**
`crontab -r`
```bash
# 清除当前用户所有 cron 任务
crontab -r
```

**基本写法:恢复被篡改文件**
`apt-get install --reinstall <包名>`
```bash
# 重新安装被篡改的系统包
sudo apt-get install --reinstall coreutils
```

**基本写法:更新所有软件包**
`apt-get update && apt-get upgrade`
```bash
# 更新所有软件包修复已知漏洞
sudo apt-get update && sudo apt-get upgrade -y
```

**基本写法:重置所有用户密码**
`passwd <用户>`
```bash
# 重置用户密码
sudo passwd root
```

---

## 报告与归档

**基本写法:生成系统快照报告**
`hostname && date && uname -a > /tmp/incident_report.txt`
```bash
# 创建事件响应报告文件
echo "事件响应报告 $(date)" > /tmp/incident_report.txt
echo "主机名: $(hostname)" >> /tmp/incident_report.txt
echo "时间: $(date)" >> /tmp/incident_report.txt
echo "内核: $(uname -r)" >> /tmp/incident_report.txt
```

**基本写法:归档所有证据**
`tar -czf evidence-$(date +%F).tar.gz /tmp/incident_*/`
```bash
# 打包归档所有取证证据
sudo tar -czf evidence-$(date +%F).tar.gz /tmp/incident_report.txt /tmp/logs.tar.gz /tmp/memory.dump
```

**基本写法:计算证据哈希**
`sha256sum evidence-*.tar.gz > evidence.hash`
```bash
# 计算证据文件哈希保证完整性
sha256sum evidence-*.tar.gz > evidence.hash
```

**基本写法:验证证据完整性**
`sha256sum -c evidence.hash`
```bash
# 验证证据文件完整性
sha256sum -c evidence.hash
```
