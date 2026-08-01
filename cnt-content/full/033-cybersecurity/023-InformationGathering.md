---
order: 62
title: 信息收集
module: cybersecurity
category: 'eng-infra'
difficulty: intermediate
description: 信息收集技术：被动侦察、主动扫描、OSINT、子域名枚举与指纹识别详解。
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/HTTPS原理
  - cybersecurity/渗透测试方法论
  - cybersecurity/漏洞扫描
  - cybersecurity/安全编码原则
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. 信息收集概述

### 1.1 分类

| 类型     | 描述             | 特点             |
| -------- | ---------------- | ---------------- |
| 被动收集 | 不与目标直接交互 | 隐蔽、信息有限   |
| 主动收集 | 与目标直接交互   | 详细、可能被发现 |

### 1.2 收集目标

- 基础设施信息（IP、域名、网络拓扑）
- 技术栈信息（框架、中间件、CMS）
- 人员信息（员工、邮箱、组织架构）
- 业务信息（业务流程、合作伙伴）

## 2. 被动信息收集

### 2.1 DNS 信息

```bash
# 查询 A 记录
dig example.com A

# 查询所有记录
dig example.com ANY

# 区域传送（若配置不当）
dig axfr example.com @ns1.example.com

# 反向 DNS
dig -x 1.2.3.4
```

### 2.2 子域名枚举

| 工具      | 方法          | 特点       |
| --------- | ------------- | ---------- |
| subfinder | 被动 API 聚合 | 快速、全面 |
| Amass     | 被动+主动     | 最全面     |
| dnsrecon  | 字典+暴力     | 主动发现   |
| crt.sh    | 证书透明度    | 免费、有效 |

```bash
# subfinder
subfinder -d example.com -o subs.txt

# 证书透明度查询
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value'

# DNS 暴力破解
dnsrecon -d example.com -D wordlist.txt -t brt
```

### 2.3 搜索引擎技巧

```
# Google Dork
site:example.com
site:example.com filetype:pdf
site:example.com inurl:admin
site:example.com intitle:"index of"
"example.com" filetype:sql
"example.com" filetype:conf
```

### 2.4 网络空间搜索

| 平台    | 特点          |
| ------- | ------------- |
| Shodan  | IoT、工业设备 |
| FOFA    | 国内资产      |
| Censys  | 证书、服务    |
| ZoomEye | 国内资产      |

### 2.5 WHOIS 与历史记录

```bash
# WHOIS 查询
whois example.com

# 历史记录
# whois-history.com
# viewdns.info
```

## 3. 主动信息收集

### 3.1 端口扫描

```bash
# 常用扫描
nmap -sV -sC -O -p- target

# SYN 扫描（隐蔽）
nmap -sS target

# UDP 扫描
nmap -sU --top-ports 100 target

# 脚本扫描
nmap --script=vuln target
```

**Nmap 扫描类型**：

| 参数 | 类型       | 特点           |
| ---- | ---------- | -------------- |
| -sS  | SYN 扫描   | 半开连接、快速 |
| -sT  | TCP 全连接 | 完整握手       |
| -sU  | UDP 扫描   | 较慢           |
| -sV  | 版本探测   | 识别服务版本   |
| -O   | OS 探测    | 识别操作系统   |

### 3.2 Web 指纹识别

| 工具       | 识别内容          |
| ---------- | ----------------- |
| Wappalyzer | CMS、框架、服务器 |
| WhatWeb    | Web 技术栈        |
| Wapplyzer  | 批量识别          |
| BuiltWith  | 技术栈分析        |

```bash
# WhatWeb
whatweb example.com

# Wappalyzer CLI
wappalyzer https://example.com
```

### 3.3 目录扫描

```bash
# dirsearch
dirsearch -u https://example.com -e php,html,js

# gobuster
gobuster dir -u https://example.com -w wordlist.txt

# feroxbuster
feroxbuster -u https://example.com -w wordlist.txt
```

### 3.4 漏洞扫描

```bash
# Nmap 漏洞脚本
nmap --script=vuln target

# Nikto（Web 漏洞扫描）
nikto -h https://example.com

# Nuclei（模板化扫描）
nuclei -u https://example.com -t cves/
```

## 4. OSINT 框架

### 4.1 常用框架

| 框架         | 特点           |
| ------------ | -------------- |
| Maltego      | 图形化关联分析 |
| SpiderFoot   | 自动化 OSINT   |
| Recon-ng     | 模块化侦察     |
| theHarvester | 邮箱/域名收集  |

### 4.2 社交媒体情报

| 平台     | 信息类型           |
| -------- | ------------------ |
| LinkedIn | 员工、职位、技术栈 |
| GitHub   | 代码泄露、仓库     |
| Twitter  | 技术讨论、泄露     |
| Pastebin | 数据泄露           |

### 4.3 代码仓库泄露

```bash
# 搜索 GitHub 泄露
# 关键词：password、secret、api_key、token、private_key

# truffleHog
trufflehog https://github.com/target/repo

# gitLeaks
gitleaks detect --repo-url=https://github.com/target/repo
```

## 5. 信息整理与分析

### 5.1 攻击面映射

```
域名 → IP → 端口 → 服务 → 版本 → 漏洞
  ↓
子域名 → 邮箱 → 员工 → 社工
```

### 5.2 工具链

```
subfinder → httpx → nuclei → 报告
  ↓          ↓        ↓
子域名   存活检测   漏洞扫描
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

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Web 攻击链详解

注入类：SQLi（参数化防御）、XSS（输出编码 + CSP）、命令注入（白名单）。
身份类：会话固定/劫持（HttpOnly + SameSite）、JWT 算法混淆（固定算法 + 校验）。
逻辑类：越权（IDOR）、竞态（TOCTOU）、支付篡改（服务端重算）。
防护纵深：WAF 拦截已知模式 + 应用层校验 + 监控异常。

### 13.2 零信任架构

核心原则：永不信任、始终验证；身份驱动策略而非网络位置。
组件：身份代理（IdP）、策略引擎（PDP）、网关（PEP）、微隔离。
落地路径：先高价值资产试点，逐步覆盖；配合 MFA 与设备合规。
成本与体验平衡：无密码（passkey）与连续评估是方向。

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
| 信息收集 | 023-InformationGathering | 本文自身 |
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
| Cybersecurity Metasploit 命令(渗透测试) | 052-MetasploitCommands | 本文的并列主题 |
| Cybersecurity Burp Suite 命令行 | 053-BurpSuiteCLI | 本文的并列主题 |
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文的并列主题 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
