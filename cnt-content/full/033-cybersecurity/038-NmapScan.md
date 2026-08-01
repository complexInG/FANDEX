---
order: 380
title: Cybersecurity nmap 端口扫描
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity nmap 端口扫描 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## nmap 基本扫描

**基本写法：扫描单个主机**
`nmap <主机>`
```bash
# 扫描目标主机常用端口
nmap 192.168.1.1
```

**基本写法：扫描域名**
`nmap <域名>`
```bash
# 扫描域名
nmap example.com
```

**基本写法：扫描 IP 范围**
`nmap <起始IP>-<结束IP>`
```bash
# 扫描 IP 范围
nmap 192.168.1.1-100
```

**基本写法：扫描整个子网**
`nmap <网段>/<前缀>`
```bash
# 扫描 192.168.1.0/24 网段
nmap 192.168.1.0/24
```

**基本写法：从文件读取目标**
`nmap -iL <文件>`
```bash
# 从文件读取目标列表
nmap -iL targets.txt
```

---

## 主机发现

**基本写法：只发现存活主机**
`nmap -sn <目标>`
```bash
# Ping 扫描发现存活主机
nmap -sn 192.168.1.0/24
```

**基本写法：跳过主机发现**
`nmap -Pn <目标>`
```bash
# 跳过 Ping 直接扫描端口
nmap -Pn 192.168.1.1
```

**基本写法：使用 ARP 发现**
`nmap -PR <目标>`
```bash
# 使用 ARP 请求发现主机
nmap -PR 192.168.1.0/24
```

**基本写法：使用 ICMP 发现**
`nmap -PE <目标>`
```bash
# 使用 ICMP Echo 请求发现主机
nmap -PE 192.168.1.0/24
```

**基本写法：禁用 DNS 解析**
`nmap -n <目标>`
```bash
# 跳过 DNS 解析加快扫描
nmap -n 192.168.1.0/24
```

---

## 端口扫描技术

**基本写法：SYN 半开扫描**
`nmap -sS <目标>`
```bash
# SYN 半开扫描（需 root 权限）
nmap -sS 192.168.1.1
```

**基本写法：TCP 全连接扫描**
`nmap -sT <目标>`
```bash
# TCP 全连接扫描
nmap -sT 192.168.1.1
```

**基本写法：UDP 扫描**
`nmap -sU <目标>`
```bash
# UDP 端口扫描
nmap -sU 192.168.1.1
```

**基本写法：FIN 扫描**
`nmap -sF <目标>`
```bash
# FIN 扫描绕过防火墙
nmap -sF 192.168.1.1
```

**基本写法：Xmas 扫描**
`nmap -sX <目标>`
```bash
# Xmas 扫描（FIN+PSH+URG）
nmap -sX 192.168.1.1
```

**基本写法：Null 扫描**
`nmap -sN <目标>`
```bash
# Null 扫描（无标志位）
nmap -sN 192.168.1.1
```

---

## 端口指定

**基本写法：扫描指定端口**
`nmap -p <端口> <目标>`
```bash
# 扫描 80 端口
nmap -p 80 192.168.1.1
```

**基本写法：扫描多个端口**
`nmap -p <端口1>,<端口2> <目标>`
```bash
# 扫描 80 和 443 端口
nmap -p 80,443 192.168.1.1
```

**基本写法：扫描端口范围**
`nmap -p <起始>-<结束> <目标>`
```bash
# 扫描 1-1000 端口
nmap -p 1-1000 192.168.1.1
```

**基本写法：扫描所有端口**
`nmap -p- <目标>`
```bash
# 扫描所有 65535 个端口
nmap -p- 192.168.1.1
```

**基本写法：扫描常用端口**
`nmap -F <目标>`
```bash
# 快速扫描 100 个常用端口
nmap -F 192.168.1.1
```

**基本写法：扫描指定协议端口**
`nmap -p <协议>:<端口> <目标>`
```bash
# 扫描 TCP 80 和 UDP 53
nmap -p T:80,U:53 192.168.1.1
```

---

## 服务与版本探测

**基本写法：服务版本探测**
`nmap -sV <目标>`
```bash
# 探测端口运行的服务版本
nmap -sV 192.168.1.1
```

**基本写法：操作系统探测**
`nmap -O <目标>`
```bash
# 探测目标操作系统
nmap -O 192.168.1.1
```

**基本写法：全面扫描**
`nmap -A <目标>`
```bash
# 启用所有高级探测功能
nmap -A 192.168.1.1
```

**基本写法：设置版本探测强度**
`nmap -sV --version-intensity <级别> <目标>`
```bash
# 设置版本探测强度（0-9）
nmap -sV --version-intensity 9 192.168.1.1
```

**基本写法：轻量级版本探测**
`nmap -sV --version-light <目标>`
```bash
# 轻量级版本探测
nmap -sV --version-light 192.168.1.1
```

---

## 扫描时序与性能

**基本写法：设置时序模板**
`nmap -T<级别> <目标>`
```bash
# 使用 T4 时序模板（0-5）
nmap -T4 192.168.1.1
```

**基本写法：并行扫描**
`nmap --min-parallelism <数量> <目标>`
```bash
# 设置最小并行探测数
nmap --min-parallelism 10 192.168.1.1
```

**基本写法：限制扫描速率**
`nmap --max-rate <速率> <目标>`
```bash
# 限制每秒最大 100 个包
nmap --max-rate 100 192.168.1.1
```

**基本写法：设置超时**
`nmap --host-timeout <时间> <目标>`
```bash
# 设置每主机超时 30 分钟
nmap --host-timeout 30m 192.168.1.1
```

**基本写法：设置重试次数**
`nmap --max-retries <次数> <目标>`
```bash
# 设置最大重试次数
nmap --max-retries 2 192.168.1.1
```

---

## NSE 脚本引擎

**基本写法：使用默认脚本**
`nmap -sC <目标>`
```bash
# 使用默认脚本集合
nmap -sC 192.168.1.1
```

**基本写法：指定脚本扫描**
`nmap --script <脚本> <目标>`
```bash
# 使用 vuln 类脚本扫描漏洞
nmap --script vuln 192.168.1.1
```

**基本写法：使用多个脚本**
`nmap --script <脚本1>,<脚本2> <目标>`
```bash
# 同时使用多个脚本
nmap --script http-title,ssl-cert 192.168.1.1
```

**基本写法：HTTP 标题枚举**
`nmap --script http-title -p <端口> <目标>`
```bash
# 获取 HTTP 服务标题
nmap --script http-title -p 80,443 192.168.1.1
```

**基本写法：SSL 证书枚举**
`nmap --script ssl-cert -p 443 <目标>`
```bash
# 获取 SSL 证书信息
nmap --script ssl-cert -p 443 example.com
```

**基本写法：检测弱密码套件**
`nmap --script ssl-enum-ciphers -p 443 <目标>`
```bash
# 枚举 SSL 支持的密码套件
nmap --script ssl-enum-ciphers -p 443 example.com
```

**基本写法：脚本参数设置**
`nmap --script <脚本> --script-args <参数>=<值> <目标>`
```bash
# 给脚本传递参数
nmap --script http-enum --script-args http-enum.basepath=/admin/ -p 80 192.168.1.1
```

---

## 防火墙与 IDS 规避

**基本写法：分片发送数据包**
`nmap -f <目标>`
```bash
# 使用小分片绕过 IDS
nmap -f 192.168.1.1
```

**基本写法：设置 MTU**
`nmap --mtu <大小> <目标>`
```bash
# 设置自定义 MTU 大小
nmap --mtu 24 192.168.1.1
```

**基本写法：使用诱饵**
`nmap -D <诱饵1>,<诱饵2> <目标>`
```bash
# 使用诱饵 IP 隐藏真实源
nmap -D 192.168.1.100,192.168.1.101,ME 192.168.1.1
```

**基本写法：随机诱饵**
`nmap -D RND:<数量> <目标>`
```bash
# 使用 5 个随机诱饵
nmap -D RND:5 192.168.1.1
```

**基本写法：伪造源端口**
`nmap --source-port <端口> <目标>`
```bash
# 使用 53 端口作为源端口
nmap --source-port 53 192.168.1.1
```

**基本写法：随机化目标顺序**
`nmap --randomize-hosts <目标>`
```bash
# 随机化扫描顺序
nmap --randomize-hosts 192.168.1.0/24
```

---

## 输出格式

**基本写法：标准输出到文件**
`nmap -oN <文件> <目标>`
```bash
# 输出标准格式到文件
nmap -oN scan.txt 192.168.1.1
```

**基本写法：XML 格式输出**
`nmap -oX <文件> <目标>`
```bash
# 输出 XML 格式便于程序解析
nmap -oX scan.xml 192.168.1.1
```

**基本写法：Grep 格式输出**
`nmap -oG <文件> <目标>`
```bash
# 输出 grep 友好格式
nmap -oG scan.gnmap 192.168.1.1
```

**基本写法：输出所有格式**
`nmap -oA <文件名> <目标>`
```bash
# 同时输出所有格式
nmap -oA scanresult 192.168.1.1
```

**基本写法：追加到输出文件**
`nmap --append-output -oN <文件> <目标>`
```bash
# 追加结果到已有文件
nmap --append-output -oN scan.txt 192.168.1.2
```

---

## 实用扫描组合

**基本写法：快速发现存活主机**
`nmap -sn -T4 <网段>`
```bash
# 快速扫描网段存活主机
nmap -sn -T4 192.168.1.0/24
```

**基本写法：全面扫描单主机**
`nmap -sS -sV -O -A -T4 -p- <主机>`
```bash
# 全面扫描所有端口和服务
nmap -sS -sV -O -A -T4 -p- 192.168.1.1
```

**基本写法：扫描并保存结果**
`nmap -sV -oA <文件名> -p- <主机>`
```bash
# 扫描所有端口并保存结果
nmap -sV -oA fullscan -p- 192.168.1.1
```

**基本写法：隐蔽扫描**
`nmap -sS -f -T2 -D RND:3 --randomize-hosts <目标>`
```bash
# 慢速隐蔽扫描
nmap -sS -f -T2 -D RND:3 --randomize-hosts 192.168.1.1
```

**基本写法：扫描 Web 服务**
`nmap -p 80,443,8080,8443 -sV --script http-title,http-headers <目标>`
```bash
# 扫描常见 Web 端口并获取标题
nmap -p 80,443,8080,8443 -sV --script http-title,http-headers 192.168.1.1
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
| Cybersecurity nmap 端口扫描 | 038-NmapScan | 本文自身 |
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
| Cybersecurity Metasploit 命令(渗透测试) | 052-MetasploitCommands | 本文的并列主题 |
| Cybersecurity Burp Suite 命令行 | 053-BurpSuiteCLI | 本文的并列主题 |
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文的并列主题 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
