---
order: 360
title: Cybersecurity OpenSSL 证书管理
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity OpenSSL 证书管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 生成私钥

**基本写法：生成 RSA 私钥**
`openssl genrsa -out <文件> <位数>`
```bash
# 生成 2048 位 RSA 私钥
openssl genrsa -out private.key 2048
```

**基本写法：生成 4096 位私钥**
`openssl genrsa -out <文件> 4096`
```bash
# 生成 4096 位 RSA 私钥（更安全）
openssl genrsa -out private.key 4096
```

**基本写法：生成加密的私钥**
`openssl genrsa -aes256 -out <文件> <位数>`
```bash
# 使用 AES-256 加密私钥
openssl genrsa -aes256 -out private.key 2048
```

**基本写法：生成 EC 私钥**
`openssl ecparam -name <曲线> -genkey -noout -out <文件>`
```bash
# 生成 P-256 椭圆曲线私钥
openssl ecparam -name prime256v1 -genkey -noout -out ec_key.pem
```

**基本写法：从私钥提取公钥**
`openssl rsa -in <私钥> -pubout -out <公钥>`
```bash
# 从 RSA 私钥提取公钥
openssl rsa -in private.key -pubout -out public.key
```

---

## 生成证书签名请求（CSR）

**基本写法：生成 CSR**
`openssl req -new -key <私钥> -out <CSR文件>`
```bash
# 交互式生成 CSR
openssl req -new -key private.key -out request.csr
```

**基本写法：同时生成私钥和 CSR**
`openssl req -newkey rsa:2048 -nodes -keyout <私钥> -out <CSR>`
```bash
# 一步生成私钥和 CSR
openssl req -newkey rsa:2048 -nodes -keyout private.key -out request.csr
```

**基本写法：使用 subject 生成 CSR**
`openssl req -new -key <私钥> -out <CSR> -subj "<主题>"`
```bash
# 非交互式指定主题
openssl req -new -key private.key -out request.csr -subj "/C=CN/ST=Beijing/L=Beijing/O=MyOrg/CN=example.com"
```

**基本写法：带 SAN 的 CSR**
`openssl req -new -key <私钥> -out <CSR> -config <配置>`
```bash
# 生成带 Subject Alternative Names 的 CSR
openssl req -new -key private.key -out request.csr -config <(cat /etc/ssl/openssl.cnf <<(printf "[SAN]\nsubjectAltName=DNS:example.com,DNS:www.example.com"))
```

---

## 查看证书与 CSR

**基本写法：查看 CSR 信息**
`openssl req -text -noout -verify -in <CSR>`
```bash
# 查看 CSR 的详细信息
openssl req -text -noout -verify -in request.csr
```

**基本写法：查看证书信息**
`openssl x509 -text -noout -in <证书>`
```bash
# 查看证书完整信息
openssl x509 -text -noout -in cert.pem
```

**基本写法：查看证书有效期**
`openssl x509 -enddate -noout -in <证书>`
```bash
# 查看证书过期时间
openssl x509 -enddate -noout -in cert.pem
```

**基本写法：查看证书颁发者**
`openssl x509 -issuer -noout -in <证书>`
```bash
# 查看证书颁发者信息
openssl x509 -issuer -noout -in cert.pem
```

**基本写法：查看证书主题**
`openssl x509 -subject -noout -in <证书>`
```bash
# 查看证书主题信息
openssl x509 -subject -noout -in cert.pem
```

**基本写法：查看证书指纹**
`openssl x509 -fingerprint -sha256 -noout -in <证书>`
```bash
# 查看 SHA-256 指纹
openssl x509 -fingerprint -sha256 -noout -in cert.pem
```

---

## 生成自签名证书

**基本写法：生成自签名证书**
`openssl req -x509 -newkey rsa:2048 -keyout <私钥> -out <证书> -days <天数> -nodes`
```bash
# 生成 365 天有效期的自签名证书
openssl req -x509 -newkey rsa:2048 -keyout private.key -out cert.pem -days 365 -nodes
```

**基本写法：指定主题生成自签名证书**
`openssl req -x509 -newkey rsa:2048 -keyout <私钥> -out <证书> -days <天数> -nodes -subj "<主题>"`
```bash
# 非交互式生成自签名证书
openssl req -x509 -newkey rsa:2048 -keyout private.key -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

**基本写法：使用现有私钥生成自签名证书**
`openssl req -x509 -key <私钥> -out <证书> -days <天数>`
```bash
# 使用已有私钥生成证书
openssl req -x509 -key private.key -out cert.pem -days 365
```

---

## 证书签名

**基本写法：使用 CA 签发证书**
`openssl x509 -req -in <CSR> -CA <CA证书> -CAkey <CA私钥> -CAcreateserial -out <证书> -days <天数>`
```bash
# 用 CA 签发客户端证书
openssl x509 -req -in request.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

**基本写法：使用自签名私钥签发证书**
`openssl x509 -req -in <CSR> -signkey <私钥> -out <证书>`
```bash
# 使用自签名私钥签发 CSR
openssl x509 -req -in request.csr -signkey private.key -out cert.pem
```

**基本写法：带扩展签发证书**
`openssl x509 -req -in <CSR> -CA <CA证书> -CAkey <CA私钥> -extfile <配置> -extensions <节> -out <证书>`
```bash
# 签发带扩展的证书
openssl x509 -req -in request.csr -CA ca.crt -CAkey ca.key -extfile <(printf "subjectAltName=DNS:example.com") -out cert.pem
```

---

## 证书格式转换

**基本写法：PEM 转 DER**
`openssl x509 -outform der -in <证书> -out <DER文件>`
```bash
# PEM 格式转 DER 格式
openssl x509 -outform der -in cert.pem -out cert.der
```

**基本写法：DER 转 PEM**
`openssl x509 -inform der -in <DER文件> -out <证书>`
```bash
# DER 格式转 PEM 格式
openssl x509 -inform der -in cert.der -out cert.pem
```

**基本写法：PKCS12 转 PEM**
`openssl pkcs12 -in <PFX文件> -out <证书> -nodes`
```bash
# PFX/P12 转 PEM（含私钥和证书）
openssl pkcs12 -in cert.pfx -out cert.pem -nodes
```

**基本写法：PEM 转 PKCS12**
`openssl pkcs12 -export -out <PFX文件> -inkey <私钥> -in <证书>`
```bash
# PEM 私钥和证书转 PFX
openssl pkcs12 -export -out cert.pfx -inkey private.key -in cert.pem
```

**基本写法：带 CA 证书链转 PKCS12**
`openssl pkcs12 -export -out <PFX文件> -inkey <私钥> -in <证书> -certfile <CA证书>`
```bash
# 包含 CA 证书链的 PFX
openssl pkcs12 -export -out cert.pfx -inkey private.key -in cert.pem -certfile ca.crt
```

---

## 验证证书

**基本写法：验证证书链**
`openssl verify -CAfile <CA证书> <证书>`
```bash
# 验证证书是否由 CA 签发
openssl verify -CAfile ca.crt client.crt
```

**基本写法：验证证书和私钥匹配**
`openssl x509 -noout -modulus -in <证书> | openssl md5; openssl rsa -noout -modulus -in <私钥> | openssl md5`
```bash
# 对比证书和私钥的 modulus 是否一致
openssl x509 -noout -modulus -in cert.pem | openssl md5
openssl rsa -noout -modulus -in private.key | openssl md5
```

**基本写法：验证 SSL 连接**
`openssl s_client -connect <主机>:<端口>`
```bash
# 测试 HTTPS 连接并查看证书链
openssl s_client -connect example.com:443
```

**基本写法：指定 SNI 验证**
`openssl s_client -connect <主机>:<端口> -servername <域名>`
```bash
# 指定 SNI 验证虚拟主机证书
openssl s_client -connect example.com:443 -servername example.com
```

**基本写法：只查看证书**
`openssl s_client -connect <主机>:<端口> -showcerts`
```bash
# 查看服务器返回的完整证书链
openssl s_client -connect example.com:443 -showcerts
```

---

## 证书撤销列表（CRL）

**基本写法：生成 CRL**
`openssl ca -gencrl -out <CRL文件>`
```bash
# 生成证书撤销列表
openssl ca -gencrl -out crl.pem
```

**基本写法：查看 CRL**
`openssl crl -text -noout -in <CRL文件>`
```bash
# 查看 CRL 内容
openssl crl -text -noout -in crl.pem
```

**基本写法：使用 CRL 验证证书**
`openssl verify -crl_check -CAfile <CA证书> -CRLfile <CRL文件> <证书>`
```bash
# 验证证书是否被撤销
openssl verify -crl_check -CAfile ca.crt -CRLfile crl.pem client.crt
```

---

## 证书信息提取

**基本写法：提取公钥**
`openssl x509 -pubkey -noout -in <证书>`
```bash
# 从证书提取公钥
openssl x509 -pubkey -noout -in cert.pem > public.key
```

**基本写法：提取序列号**
`openssl x509 -serial -noout -in <证书>`
```bash
# 获取证书序列号
openssl x509 -serial -noout -in cert.pem
```

**基本写法：提取有效期**
`openssl x509 -dates -noout -in <证书>`
```bash
# 获取证书起止日期
openssl x509 -dates -noout -in cert.pem
```

**基本写法：提取所有主题信息**
`openssl x509 -subject -nameopt RFC2253 -noout -in <证书>`
```bash
# 以 RFC2253 格式输出主题
openssl x509 -subject -nameopt RFC2253 -noout -in cert.pem
```

---

## 常用证书操作

**基本写法：检查证书过期时间**
`openssl x509 -enddate -noout -in <证书> | cut -d= -f2`
```bash
# 提取证书过期日期
openssl x509 -enddate -noout -in cert.pem | cut -d= -f2
```

**基本写法：批量检查证书过期**
`for f in *.pem; do echo "$f: $(openssl x509 -enddate -noout -in $f)"; done`
```bash
# 批量检查当前目录所有证书的过期时间
for f in *.pem; do echo "$f: $(openssl x509 -enddate -noout -in $f)"; done
```

**基本写法：从 HTTPS 服务提取证书**
`echo | openssl s_client -connect <主机>:443 2>/dev/null | openssl x509 -out <文件>`
```bash
# 从远程服务器下载证书
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -out cert.pem
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
| Cybersecurity OpenSSL 证书管理 | 036-OpenSSLCert | 本文自身 |
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
