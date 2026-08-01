---
order: 400
title: Cybersecurity hashcat 密码破解
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity hashcat 密码破解 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## hashcat 基本用法

**基本写法：字典攻击**
`hashcat -m <模式> <哈希文件> <字典>`
```bash
# 使用字典破解 MD5 哈希
hashcat -m 0 hashes.txt rockyou.txt
```

**基本写法：指定哈希模式**
`hashcat -m <模式> <哈希> <字典>`
```bash
# 破解 SHA-256 哈希
hashcat -m 1400 sha256hashes.txt rockyou.txt
```

**基本写法：显示破解结果**
`hashcat -m <模式> <哈希文件> <字典> --show`
```bash
# 显示已破解的哈希和明文
hashcat -m 0 hashes.txt --show
```

**基本写法：指定攻击模式**
`hashcat -a <模式> -m <哈希模式> <哈希文件> [参数]`
```bash
# 使用攻击模式 0（字典攻击）
hashcat -a 0 -m 0 hashes.txt rockyou.txt
```

---

## 哈希模式

**基本写法：常见哈希模式**
```text
`0     - MD5
100   - SHA1
1400  - SHA256
1700  - SHA512
1000  - NTLM
1800  - sha512crypt ($6$)
500   - md5crypt ($1$)
3200  - bcrypt ($2a$/$2b$)`
```
```bash
# 查看所有支持的哈希模式
hashcat --help | grep -i "hash-type"
```

**基本写法：查看所有哈希模式**
`hashcat --help`
```bash
# 列出所有支持的哈希类型
hashcat --help
```

**基本写法：破解 NTLM 哈希**
`hashcat -m 1000 <哈希文件> <字典>`
```bash
# 破解 Windows NTLM 哈希
hashcat -m 1000 ntlm_hashes.txt rockyou.txt
```

**基本写法：破解 bcrypt 哈希**
`hashcat -m 3200 <哈希文件> <字典>`
```bash
# 破解 bcrypt 哈希（速度较慢）
hashcat -m 3200 bcrypt_hashes.txt rockyou.txt
```

---

## 攻击模式

**基本写法：字典攻击（模式 0）**
`hashcat -a 0 -m <模式> <哈希文件> <字典>`
```bash
# 标准字典攻击
hashcat -a 0 -m 0 hashes.txt rockyou.txt
```

**基本写法：组合字典攻击（模式 1）**
`hashcat -a 1 -m <模式> <哈希文件> <字典1> <字典2>`
```bash
# 组合两个字典
hashcat -a 1 -m 0 hashes.txt dict1.txt dict2.txt
```

**基本写法：掩码暴力破解（模式 3）**
`hashcat -a 3 -m <模式> <哈希文件> <掩码>`
```bash
# 暴力破解 8 位数字密码
hashcat -a 3 -m 0 hashes.txt ?d?d?d?d?d?d?d?d
```

**基本写法：基于规则的攻击（模式 6）**
`hashcat -a 6 -m <模式> <哈希文件> <字典> <掩码>`
```bash
# 字典 + 掩码组合攻击
hashcat -a 6 -m 0 hashes.txt rockyou.txt ?d?d?d?d
```

**基本写法：混合攻击（模式 7）**
`hashcat -a 7 -m <模式> <哈希文件> <掩码> <字典>`
```bash
# 掩码 + 字典组合攻击
hashcat -a 7 -m 0 hashes.txt ?d?d?d?d rockyou.txt
```

---

## 掩码字符集

**基本写法：内置字符集**
```text
`?l - 小写字母 a-z
?u - 大写字母 A-Z
?d - 数字 0-9
?s - 特殊字符
?a - 所有字符
?b - 二进制
?h - 十六进制小写
?H - 十六进制大写`
```
```bash
# 查看掩码字符集说明
hashcat --help | grep "Built-in"
```

**基本写法：自定义字符集**
`hashcat -<数字> <字符集> -a 3 -m <模式> <哈希文件> <掩码>`
```bash
# 自定义字符集只包含 abc123
hashcat -1 abc123 -a 3 -m 0 hashes.txt ?1?1?1?1?1
```

**基本写法：常见密码模式**
```bash
`# 8 位数字密码
?d?d?d?d?d?d?d?d
# 6-8 位小写字母
?l?l?l?l?l?l?l?l
# 大写开头 + 小写 + 数字
?u?l?l?l?l?d?d`
```
```bash
# 8 位小写字母密码
hashcat -a 3 -m 0 hashes.txt ?l?l?l?l?l?l?l?l
```

---

## 规则文件

**基本写法：使用规则文件**
`hashcat -m <模式> <哈希文件> <字典> -r <规则文件>`
```bash
# 使用最佳 64 规则
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**基本写法：组合多个规则**
`hashcat -m <模式> <哈希文件> <字典> -r <规则1> -r <规则2>`
```bash
# 组合多个规则文件
hashcat -m 0 hashes.txt rockyou.txt -r rules1.rule -r rules2.rule
```

**基本写法：常用规则文件**
```bash
`/usr/share/hashcat/rules/best64.rule
/usr/share/hashcat/rules/rockyou-30000.rule
/usr/share/hashcat/rules/d3ad0ne.rule
/usr/share/hashcat/rules/toggles5.rule`
```
```bash
# 使用 rockyou-30000 规则
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule
```

---

## 性能优化

**基本写法：指定工作负载**
`hashcat -w <级别> -m <模式> <哈希文件> <字典>`
```bash
# 设置工作负载为高（1-4）
hashcat -w 3 -m 0 hashes.txt rockyou.txt
```

**基本写法：指定设备类型**
`hashcat -D <设备> -m <模式> <哈希文件> <字典>`
```bash
# 使用 GPU 设备
hashcat -D 2 -m 0 hashes.txt rockyou.txt
```

**基本写法：显示性能测试**
`hashcat -b -m <模式>`
```bash
# 性能基准测试
hashcat -b -m 0
```

**基本写法：限制 GPU 速度**
`hashcat --gpu-temp-abort=<温度> -m <模式> <哈希文件> <字典>`
```bash
# GPU 温度超过 90 度时停止
hashcat --gpu-temp-abort=90 -m 0 hashes.txt rockyou.txt
```

**基本写法：启用优化内核**
`hashcat -O -m <模式> <哈希文件> <字典>`
```bash
# 启用优化内核提升性能
hashcat -O -m 0 hashes.txt rockyou.txt
```

---

## 会话管理

**基本写法：恢复会话**
`hashcat --session <名称> --restore`
```bash
# 恢复之前的破解会话
hashcat --session mysession --restore
```

**基本写法：指定会话名称**
`hashcat --session <名称> -m <模式> <哈希文件> <字典>`
```bash
# 启动命名会话
hashcat --session mysession -m 0 hashes.txt rockyou.txt
```

**基本写法：自动恢复**
`hashcat --restore`
```bash
# 恢复最近的会话
hashcat --restore
```

---

## 输出与结果

**基本写法：查看破解结果**
`hashcat -m <模式> <哈希文件> --show`
```bash
# 显示已破解的哈希
hashcat -m 0 hashes.txt --show
```

**基本写法：输出到文件**
`hashcat -m <模式> <哈希文件> <字典> -o <输出文件>`
```bash
# 将破解结果保存到文件
hashcat -m 0 hashes.txt rockyou.txt -o cracked.txt
```

**基本写法：输出格式化**
`hashcat -m <模式> <哈希文件> <字典> -o <输出文件> --outfile-format <格式>`
```bash
# 指定输出格式（2 = 哈希:明文）
hashcat -m 0 hashes.txt rockyou.txt -o cracked.txt --outfile-format 2
```

**基本写法：显示状态**
`hashcat -m <模式> <哈希文件> <字典> --status`
```bash
# 自动显示状态更新
hashcat -m 0 hashes.txt rockyou.txt --status
```

---

## 字典处理

**基本写法：使用多个字典**
`cat <字典1> <字典2> > <合并字典>`
```bash
# 合并多个字典文件
cat dict1.txt dict2.txt dict3.txt > combined.txt
hashcat -m 0 hashes.txt combined.txt
```

**基本写法：从字典文件读取**
`hashcat -m <模式> <哈希文件> <字典>`
```bash
# 使用 rockyou 字典
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

**基本写法：解压 rockyou 字典**
`gunzip /usr/share/wordlists/rockyou.txt.gz`
```bash
# 解压 rockyou 字典文件
gunzip /usr/share/wordlists/rockyou.txt.gz
```

---

## 实用破解组合

**基本写法：常见密码模式破解**
`hashcat -a 3 -m <模式> <哈希文件> ?d?d?d?d?d?d?d?d`
```bash
# 破解 8 位数字密码
hashcat -a 3 -m 0 hashes.txt ?d?d?d?d?d?d?d?d
```

**基本写法：字典 + 规则破解**
`hashcat -m <模式> <哈希文件> <字典> -r <规则>`
```bash
# 字典 + 规则组合攻击
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**基本写法：渐进式破解**
```bash
`# 1. 先用常用字典
hashcat -m 0 hashes.txt rockyou.txt
# 2. 再用规则扩展
hashcat -m 0 hashes.txt rockyou.txt -r best64.rule
# 3. 最后暴力破解
hashcat -a 3 -m 0 hashes.txt ?a?a?a?a?a?a?a?a`
```
```bash
# 渐进式破解策略
hashcat -m 0 hashes.txt rockyou.txt
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
hashcat -a 3 -m 0 hashes.txt ?a?a?a?a?a?a?a?a
```

---

## John the Ripper 替代

**基本写法：破解哈希文件**
`john --wordlist=<字典> <哈希文件>`
```bash
# 使用 John the Ripper 破解
john --wordlist=rockyou.txt hashes.txt
```

**基本写法：显示破解结果**
`john --show <哈希文件>`
```bash
# 显示已破解的密码
john --show hashes.txt
```

**基本写法：指定哈希格式**
`john --format=<格式> --wordlist=<字典> <哈希文件>`
```bash
# 指定 MD5 格式破解
john --format=raw-md5 --wordlist=rockyou.txt hashes.txt
```

**基本写法：破解 SSH 密钥密码**
`ssh2john <密钥> > <哈希文件>; john <哈希文件>`
```bash
# 破解 SSH 私钥密码
ssh2john id_rsa > ssh_hash.txt
john ssh_hash.txt
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
| Cybersecurity hashcat 密码破解 | 040-Hashcat | 本文自身 |
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
