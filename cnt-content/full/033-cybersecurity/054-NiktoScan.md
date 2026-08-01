---
order: 540
title: Cybersecurity Nikto Web 扫描
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity Nikto Web 扫描 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## Nikto 基础扫描

**基本写法:基础扫描目标**
`nikto -h <主机>`
```bash
# 对目标主机执行基础扫描
nikto -h https://example.com
```

**基本写法:指定端口扫描**
`nikto -h <主机> -p <端口>`
```bash
# 扫描指定端口的 Web 服务
nikto -h example.com -p 8080
```

**基本写法:扫描多个端口**
`nikto -h <主机> -p <端口1>-<端口2>`
```bash
# 扫描 80-443 端口范围
nikto -h example.com -p 80-443
```

**基本写法:使用 SSL 扫描**
`nikto -h <主机> -ssl`
```bash
# 强制使用 SSL 扫描
nikto -h example.com -ssl -p 443
```

**基本写法:指定输出文件**
`nikto -h <主机> -o <文件>`
```bash
# 扫描结果输出到文件
nikto -h example.com -o scan_result.html -Format htm
```

---

## Nikto 调优与配置

**基本写法:设置扫描调优**
`nikto -h <主机> -Tuning <选项>`
```bash
# 调优选项 1-9(1=有趣文件 2=错误配置 3=信息泄露 4=XSS 8=命令执行 9=SQL 注入)
nikto -h example.com -Tuning 9
```

**基本写法:多项调优组合**
`nikto -h <主机> -Tuning <选项组合>`
```bash
# 同时检测 SQL 注入与 XSS
nikto -h example.com -Tuning 49
```

**基本写法:排除特定测试**
`nikto -h <主机> -SkipHandler <选项>`
```bash
# 跳过特定测试项加快扫描
nikto -h example.com -SkipHandler 2
```

**基本写法:禁用交互式功能**
`nikto -h <主机> -ask no`
```bash
# 禁止交互式确认(适合自动化脚本)
nikto -h example.com -ask no
```

**基本写法:设置超时**
`nikto -h <主机> -timeout <秒数>`
```bash
# 设置请求超时为 10 秒
nikto -h example.com -timeout 10
```

---

## Nikto 认证与代理

**基本写法:使用 Basic 认证**
`nikto -h <主机> -id <用户:密码>`
```bash
# 使用 HTTP Basic 认证扫描受保护区域
nikto -h example.com -id admin:password
```

**基本写法:使用 Cookie 认证**
`nikto -h <主机> -vhost <域名>`
```bash
# 使用虚拟主机头扫描
nikto -h 192.168.1.10 -vhost example.com
```

**基本写法:通过代理扫描**
`nikto -h <主机> -useproxy <代理URL>`
```bash
# 通过 HTTP 代理进行扫描
nikto -h example.com -useproxy http://127.0.0.1:8080
```

**基本写法:配置代理认证**
`nikto -h <主机> -useproxy <代理URL> -id <用户:密码>`
```bash
# 代理需要认证时
nikto -h example.com -useproxy http://127.0.0.1:8080 -id user:pass
```

**基本写法:使用客户端证书**
`nikto -h <主机> -cert <证书> -key <私钥>`
```bash
# 使用客户端证书扫描
nikto -h example.com -cert client.pem -key key.pem
```

---

## Nikto 扫描选项

**基本写法:禁用 SSL 证书校验**
`nikto -h <主机> -nossl`
```bash
# 禁用 SSL 证书验证
nikto -h example.com -ssl -nossl
```

**基本写法:指定 User-Agent**
`nikto -h <主机> -useragent <UA>`
```bash
# 自定义 User-Agent
nikto -h example.com -useragent "Mozilla/5.0 Custom Scanner"
```

**基本写法:自定义请求头**
`nikto -h <主机> -vhost <域名>`
```bash
# 添加 Host 头扫描虚拟主机
nikto -h 192.168.1.10 -p 80 -vhost app.example.com
```

**基本写法:禁用 404 检测**
`nikto -h <主机> -404code`
```bash
# 禁用 404 错误码检测(避免误报)
nikto -h example.com -404code
```

**基本写法:显示详细输出**
`nikto -h <主机> -Display V`
```bash
# 显示详细输出信息
nikto -h example.com -Display V
```

---

## Nikto 批量扫描

**基本写法:从文件读取目标**
`nikto -h <主机文件>`
```bash
# 批量扫描文件中的主机
nikto -h hosts.txt
```

**基本写法:多端口批量扫描**
`nikto -h <主机> -p <端口列表>`
```bash
# 扫描多个指定端口
nikto -h example.com -p 80,443,8080,8443
```

**基本写法:循环批量扫描**
`for host in $(cat <文件>); do nikto -h $host; done`
```bash
# 使用 shell 循环批量扫描
for host in $(cat hosts.txt); do nikto -h $host -o "${host}_scan.html" -Format htm; done
```

**基本写法:并行批量扫描**
`cat <文件> | xargs -P <并发数> -I {} nikto -h {}`
```bash
# 使用 xargs 并行扫描多个主机
cat hosts.txt | xargs -P 4 -I {} nikto -h {} -ask no -o "{}.txt"
```

**基本写法:按端口批量扫描**
`for port in <端口列表>; do nikto -h <主机> -p $port; done`
```bash
# 对单个主机扫描多个端口
for port in 80 443 8080 8443; do nikto -h example.com -p $port -o "scan_${port}.txt"; done
```

---

## Nikto 输出与报告

**基本写法:输出为 CSV 格式**
`nikto -h <主机> -o <文件> -Format csv`
```bash
# 输出 CSV 格式扫描结果
nikto -h example.com -o scan.csv -Format csv
```

**基本写法:输出为 HTML 格式**
`nikto -h <主机> -o <文件> -Format htm`
```bash
# 输出 HTML 格式报告
nikto -h example.com -o report.html -Format htm
```

**基本写法:输出为 JSON 格式**
`nikto -h <主机> -o <文件> -Format json`
```bash
# 输出 JSON 格式便于后续处理
nikto -h example.com -o scan.json -Format json
```

**基本写法:输出到标准输出**
`nikto -h <主机> -Format txt`
```bash
# 输出纯文本到终端
nikto -h example.com -Format txt
```

**基本写法:输出到 SQLite 数据库**
`nikto -h <主机> -o <数据库文件> -Format sql`
```bash
# 存入 SQLite 数据库便于分析
nikto -h example.com -o results.db -Format sql
```

---

## Nikto 高级选项

**基本写法:启用互操作测试**
`nikto -h <主机> -mutate <选项>`
```bash
# 启用变异测试(1=测试所有方法 2=测试目录字典)
nikto -h example.com -mutate 2
```

**基本写法:使用自定义字典**
`nikto -h <主机> -mutate <选项> -mutate-options <字典文件>`
```bash
# 使用自定义字典测试目录
nikto -h example.com -mutate 3 -mutate-options custom_dirs.txt
```

**基本写法:启用强制浏览**
`nikto -h <主机> -mutate 6 -mutate-options <目录列表>`
```bash
# 强制浏览特定目录列表
nikto -h example.com -mutate 6 -mutate-options admin,test,backup
```

**基本写法:使用 evasion 选项**
`nikto -h <主机> -evasion <编号>`
```bash
# 启用绕过 IDS 检测的 evasion 模式
# 1=随机 URI 编码 2=目录自引用 3=提前结束 URL 4=长 URL 5=伪造参数 6=使用 TAB 7=使用空格 8=大小写
nikto -h example.com -evasion 1
```

**基本写法:组合 evasion 模式**
`nikto -h <主机> -evasion <组合>`
```bash
# 组合多种 evasion 技术
nikto -h example.com -evasion 18
```

---

## Nikto 插件与配置

**基本写法:启用特定插件**
`nikto -h <主机> -Plugins <插件名>`
```bash
# 仅运行指定插件
nikto -h example.com -Plugins "apacheusers;reporting"
```

**基本写法:列出所有插件**
`nikto -list-plugins`
```bash
# 列出所有可用插件
nikto -list-plugins
```

**基本写法:使用配置文件**
`nikto -h <主机> -config <配置文件>`
```bash
# 使用自定义配置文件
nikto -h example.com -config /etc/nikto.conf
```

**基本写法:更新 Nikto 数据库**
`nikto -update`
```bash
# 更新 Nikto 扫描数据库
nikto -update
```

**基本写法:查看 Nikto 版本**
`nikto -Version`
```bash
# 查看 Nikto 版本信息
nikto -Version
```

---

## Nikto 扫描结果分析

**基本写法:统计漏洞数量**
`grep -c "OSVDB" <报告文件>`
```bash
# 统计发现的漏洞数量
grep -c "OSVDB" scan_result.txt
```

**基本写法:提取高危漏洞**
`grep -i "high\|critical" <报告文件>`
```bash
# 提取高危漏洞信息
grep -iE "high|critical|risk" scan_result.txt
```

**基本写法:提取特定漏洞类型**
`grep -i "sql\|xss\|rce" <报告文件>`
```bash
# 提取 SQL 注入、XSS、远程命令执行漏洞
grep -iE "sql injection|xss|remote code|command execution" scan_result.txt
```

**基本写法:JSON 结果解析**
`python3 -c "import json; data=json.load(open('<文件>')); print(len(data.get('vulnerabilities',[])))"`
```bash
# 解析 JSON 结果统计漏洞数
python3 -c "import json; data=json.load(open('scan.json')); print('漏洞数:', len(data.get('vulnerabilities',[])))"
```

**基本写法:生成扫描摘要**
`nikto -h <主机> -Display 1 | tail -5`
```bash
# 显示扫描摘要信息
nikto -h example.com -Display 1 | grep -E "entries|tested"
```

---

## Nikto 自动化集成

**基本写法:结合 cron 定时扫描**
`0 2 * * * nikto -h <主机> -o <文件>`
```bash
# 每天凌晨 2 点自动扫描
# 0 2 * * * nikto -h example.com -ask no -o /var/log/nikto/scan_$(date +\%F).html -Format htm
```

**基本写法:结合邮件通知**
`nikto -h <主机> -o <文件> && mail -s "扫描报告" <邮箱> < <文件>`
```bash
# 扫描完成后发送邮件
nikto -h example.com -o scan.txt -Format txt && mail -s "Nikto 扫描报告" admin@example.com < scan.txt
```

**基本写法:与 nmap 联动扫描**
`nmap -p 80,443 <目标> -oG - | awk '/80\|443/{print $2}' | nikto -h -`
```bash
# nmap 发现端口后用 Nikto 深入扫描
nmap -p 80,443 192.168.1.0/24 -oG - | awk '/Up/{print $2}' | xargs -I {} nikto -h {} -ask no
```

**基本写法:输出到 ELK 系统**
`nikto -h <主机> -Format json | python3 <转换脚本>`
```bash
# 输出 JSON 供 ELK 系统分析
nikto -h example.com -Format json -o - | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin),indent=2))"
```

**基本写法:与 OWASP Dependency Check 联动**
`nikto -h <主机> -o <文件> -Format json && dependency-check --scan <应用>`
```bash
# 组合 Nikto 与依赖检查全面评估
nikto -h example.com -o web_scan.json -Format json && dependency-check --scan ./target/app.jar --out dep_report
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
| Cybersecurity Metasploit 命令(渗透测试) | 052-MetasploitCommands | 本文的并列主题 |
| Cybersecurity Burp Suite 命令行 | 053-BurpSuiteCLI | 本文的并列主题 |
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文自身 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
