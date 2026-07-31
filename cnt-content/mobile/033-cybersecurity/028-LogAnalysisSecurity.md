# Cybersecurity 安全日志分析

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 系统日志基础

**基本写法:查看系统日志**
`tail -f /var/log/syslog`
```bash
# 实时查看系统日志
sudo tail -f /var/log/syslog
```

**基本写法:查看认证日志**
`tail -f /var/log/auth.log`
```bash
# 实时查看认证相关日志
sudo tail -f /var/log/auth.log
```

**基本写法:查看内核日志**
`dmesg | tail -20`
```bash
# 查看内核消息日志
sudo dmesg | tail -20
```

**基本写法:使用 journalctl 查询**
`journalctl -u <服务> -f`
```bash
# 实时查看指定服务日志
sudo journalctl -u sshd -f
```

**基本写法:按时间查询**
`journalctl --since "<时间>" --until "<时间>"`
```bash
# 查询指定时间段的日志
sudo journalctl --since "2026-07-31 10:00" --until "2026-07-31 12:00"
```

---

## 登录分析

**基本写法:查看登录失败记录**
`grep "Failed password" /var/log/auth.log`
```bash
# 查找 SSH 登录失败记录
sudo grep "Failed password" /var/log/auth.log
```

**基本写法:统计登录失败次数**
`grep "Failed password" /var/log/auth.log | wc -l`
```bash
# 统计 SSH 登录失败总次数
sudo grep "Failed password" /var/log/auth.log | wc -l
```

**基本写法:统计失败来源 IP**
`grep "Failed password" /var/log/auth.log | grep -oE "from [0-9.]+" | awk '{print $2}' | sort | uniq -c | sort -rn`
```bash
# 统计登录失败来源 IP 排行
sudo grep "Failed password" /var/log/auth.log | grep -oE "from [0-9.]+" | awk '{print $2}' | sort | uniq -c | sort -rn | head
```

**基本写法:查看成功登录记录**
`grep "Accepted password" /var/log/auth.log`
```bash
# 查找 SSH 登录成功记录
sudo grep "Accepted password" /var/log/auth.log
```

**基本写法:使用 last 查看登录历史**
`last -n 20`
```bash
# 查看最近 20 次登录记录
last -n 20
```

**基本写法:查看失败登录历史**
`lastb -n 20`
```bash
# 查看最近 20 次失败登录
sudo lastb -n 20
```

---

## Web 日志分析

**基本写法:统计访问量**
`wc -l /var/log/nginx/access.log`
```bash
# 统计 Nginx 访问日志总行数
wc -l /var/log/nginx/access.log
```

**基本写法:统计访问 IP 排行**
`awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn`
```bash
# 统计访问量最高的 IP
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

**基本写法:统计访问 URL**
`awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -rn`
```bash
# 统计访问最多的 URL
awk '{print $7}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

**基本写法:统计 HTTP 状态码**
`awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn`
```bash
# 统计 HTTP 状态码分布
awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn
```

**基本写法:查找 SQL 注入尝试**
`grep -iE "union.*select|sleep\(|benchmark\(|information_schema" /var/log/nginx/access.log`
```bash
# 检测 SQL 注入攻击痕迹
grep -iE "union.*select|sleep\(|benchmark\(|information_schema" /var/log/nginx/access.log
```

**基本写法:查找 XSS 攻击**
`grep -iE "<script|javascript:|onerror=|onload=" /var/log/nginx/access.log`
```bash
# 检测 XSS 攻击痕迹
grep -iE "<script|javascript:|onerror=|onload=" /var/log/nginx/access.log
```

---

## Apache 日志分析

**基本写法:统计 Apache 访问量**
`wc -l /var/log/apache2/access.log`
```bash
# 统计 Apache 访问日志行数
wc -l /var/log/apache2/access.log
```

**基本写法:统计 User-Agent**
`awk -F\" '{print $6}' /var/log/apache2/access.log | sort | uniq -c | sort -rn`
```bash
# 统计 User-Agent 分布
awk -F\" '{print $6}' /var/log/apache2/access.log | sort | uniq -c | sort -rn | head
```

**基本写法:统计访问路径**
`awk '{print $7}' /var/log/apache2/access.log | sort | uniq -c | sort -rn`
```bash
# 统计访问最多的路径
awk '{print $7}' /var/log/apache2/access.log | sort | uniq -c | sort -rn | head
```

**基本写法:检测扫描行为**
`grep -E "GET /(admin|backup|test|phpmyadmin)" /var/log/apache2/access.log`
```bash
# 检测目录扫描行为
grep -iE "GET /(admin|backup|test|phpmyadmin|wp-admin)" /var/log/apache2/access.log
```

**基本写法:查找异常大请求**
`awk '$10 > 1000000 {print $0}' /var/log/apache2/access.log`
```bash
# 查找响应体超过 1MB 的异常请求
awk '$10 > 1000000 {print $1, $7, $10}' /var/log/apache2/access.log
```

---

## 日志实时监控

**基本写法:实时监控 SSH 登录**
`tail -f /var/log/auth.log | grep --line-buffered "sshd"`
```bash
# 实时监控 SSH 登录事件
sudo tail -f /var/log/auth.log | grep --line-buffered "sshd"
```

**基本写法:监控错误日志**
`tail -f /var/log/nginx/error.log`
```bash
# 实时监控 Nginx 错误日志
sudo tail -f /var/log/nginx/error.log
```

**基本写法:监控异常状态码**
`tail -f /var/log/nginx/access.log | awk '$9 >= 500 {print}'`
```bash
# 实时监控 5xx 错误
tail -f /var/log/nginx/access.log | awk '$9 >= 500 {print $0}'
```

**基本写法:多文件实时监控**
`tail -f /var/log/nginx/access.log /var/log/nginx/error.log`
```bash
# 同时监控多个日志文件
sudo tail -f /var/log/nginx/access.log /var/log/nginx/error.log
```

**基本写法:监控特定关键字**
`tail -f /var/log/syslog | grep -iE "error|critical|failed"`
```bash
# 实时监控错误关键字
sudo tail -f /var/log/syslog | grep --line-buffered -iE "error|critical|failed"
```

---

## 日志统计与报告

**基本写法:按小时统计访问量**
`awk '{print $4}' /var/log/nginx/access.log | cut -c 14-15 | sort | uniq -c`
```bash
# 统计每小时访问量分布
awk '{print $4}' /var/log/nginx/access.log | cut -c 14-15 | sort | uniq -c
```

**基本写法:按天统计访问量**
`awk '{print $4}' /var/log/nginx/access.log | cut -c 2-12 | sort | uniq -c`
```bash
# 统计每天访问量
awk '{print $4}' /var/log/nginx/access.log | cut -c 2-12 | sort | uniq -c
```

**基本写法:统计爬虫访问**
`awk -F\" '{print $6}' /var/log/nginx/access.log | grep -iE "bot|crawler|spider" | sort | uniq -c`
```bash
# 统计搜索引擎爬虫访问
awk -F\" '{print $6}' /var/log/nginx/access.log | grep -iE "bot|crawler|spider" | sort | uniq -c | sort -rn | head
```

**基本写法:统计流量最大的 URL**
`awk '{sum[$7]+=$10} END {for(u in sum) print sum[u], u}' /var/log/nginx/access.log | sort -rn`
```bash
# 按流量排序找出消耗带宽最多的 URL
awk '{sum[$7]+=$10} END {for(u in sum) print sum[u], u}' /var/log/nginx/access.log | sort -rn | head
```

**基本写法:生成访问摘要报告**
`goaccess /var/log/nginx/access.log --log-format=COMBINED`
```bash
# 使用 goaccess 生成实时分析报告
goaccess /var/log/nginx/access.log --log-format=COMBINED -o report.html
```

---

## 安全事件检索

**基本写法:查找暴力破解来源**
`grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head`
```bash
# 查找暴力破解攻击来源 IP
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head
```

**基本写法:查找异常 sudo 使用**
`grep "sudo:" /var/log/auth.log`
```bash
# 查找 sudo 命令使用记录
sudo grep "sudo:" /var/log/auth.log
```

**基本写法:查找文件权限变更**
`grep "chmod\|chown" /var/log/audit/audit.log`
```bash
# 从审计日志查找权限变更
sudo grep "chmod\|chown" /var/log/audit/audit.log
```

**基本写法:查找网络连接异常**
`grep -i "connection\|connect" /var/log/syslog | grep -iE "refused\|timeout\|reset"`
```bash
# 查找网络连接异常记录
sudo grep -i "connection\|connect" /var/log/syslog | grep -iE "refused\|timeout\|reset"
```

**基本写法:查找进程崩溃**
`dmesg | grep -i "segfault\|killed process"`
```bash
# 查找进程崩溃记录
sudo dmesg | grep -i "segfault\|killed process"
```

---

## 日志归档与清理

**基本写法:压缩归档日志**
`gzip /var/log/nginx/access.log.1`
```bash
# 压缩归档旧日志文件
sudo gzip /var/log/nginx/access.log.1
```

**基本写法:删除过期日志**
`find /var/log/ -name "*.log.*" -mtime +30 -delete`
```bash
# 删除 30 天前的归档日志
sudo find /var/log/ -name "*.log.*" -mtime +30 -delete
```

**基本写法:日志轮转配置**
`cat /etc/logrotate.d/nginx`
```bash
# 查看 Nginx 日志轮转配置
cat /etc/logrotate.d/nginx
```

**基本写法:手动触发日志轮转**
`logrotate -f /etc/logrotate.d/nginx`
```bash
# 强制触发 Nginx 日志轮转
sudo logrotate -f /etc/logrotate.d/nginx
```

**基本写法:统计日志大小**
`du -sh /var/log/*`
```bash
# 统计各日志目录大小
sudo du -sh /var/log/*
```

---

## 日志集中化管理

**基本写法:配置 rsyslog 转发**
`echo "*.* @<远程服务器>:514" >> /etc/rsyslog.conf`
```bash
# 转发日志到远程服务器(UDP)
echo "*.* @192.168.1.100:514" | sudo tee -a /etc/rsyslog.conf
```

**基本写法:使用 TCP 转发**
`echo "*.* @@<远程服务器>:514" >> /etc/rsyslog.conf`
```bash
# 使用 TCP 协议转发日志(可靠传输)
echo "*.* @@192.168.1.100:514" | sudo tee -a /etc/rsyslog.conf
```

**基本写法:重启 rsyslog**
`systemctl restart rsyslog`
```bash
# 重启 rsyslog 使配置生效
sudo systemctl restart rsyslog
```

**基本写法:测试日志转发**
`logger "test log message"`
```bash
# 发送测试日志验证转发配置
logger -t test "test log message"
```

**基本写法:配置日志加密传输**
`cat /etc/rsyslog.d/tls.conf`
```bash
# 配置 TLS 加密日志传输
# $DefaultNetstreamDriver gtls
# $DefaultNetstreamDriverMode 1
# $DefaultNetstreamDriverAuthMode x509/name
# *.* @@192.168.1.100:6514
```
