---
order: 370
title: Cybersecurity OpenSSL 加密解密
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity OpenSSL 加密解密 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Cybersecurity OpenSSL 加密解密

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 对称加密

**基本写法：AES 加密文件**
`openssl enc -aes-256-cbc -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 AES-256-CBC 加密文件
openssl enc -aes-256-cbc -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

**基本写法：AES 解密文件**
`openssl enc -d -aes-256-cbc -pbkdf2 -in <文件> -out <输出>`
```bash
# 解密 AES 加密的文件
openssl enc -d -aes-256-cbc -pbkdf2 -in encrypted.enc -out decrypted.txt
```

**基本写法：使用密码加密**
`openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:<密码> -in <输入> -out <输出>`
```bash
# 直接指定密码加密
openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:secret123 -in plaintext.txt -out encrypted.enc
```

**基本写法：使用密钥文件加密**
`openssl enc -aes-256-cbc -salt -pbkdf2 -pass file:<密钥文件> -in <输入> -out <输出>`
```bash
# 使用密钥文件加密
openssl enc -aes-256-cbc -salt -pbkdf2 -pass file:./keyfile -in plaintext.txt -out encrypted.enc
```

**基本写法：指定密钥和 IV 加密**
`openssl enc -aes-256-cbc -K <十六进制密钥> -iv <十六进制IV> -in <输入> -out <输出>`
```bash
# 使用指定的密钥和 IV 加密
openssl enc -aes-256-cbc -K 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef -iv 0123456789abcdef0123456789abcdef -in plaintext.txt -out encrypted.enc
```

---

## 支持的加密算法

**基本写法：列出所有支持的算法**
`openssl enc -list`
```bash
# 列出所有支持的加密算法
openssl enc -list
```

**基本写法：ChaCha20 加密**
`openssl enc -chacha20 -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 ChaCha20 加密
openssl enc -chacha20 -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

**基本写法：AES-128 加密**
`openssl enc -aes-128-cbc -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 AES-128-CBC 加密
openssl enc -aes-128-cbc -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

**基本写法：Camellia 加密**
`openssl enc -camellia-256-cbc -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 Camellia-256 加密
openssl enc -camellia-256-cbc -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

---

## 非对称加密（RSA）

**基本写法：使用公钥加密**
`openssl rsautl -encrypt -inkey <公钥> -pubin -in <输入> -out <输出>`
```bash
# 使用 RSA 公钥加密文件
openssl rsautl -encrypt -inkey public.key -pubin -in plaintext.txt -out encrypted.enc
```

**基本写法：使用私钥解密**
`openssl rsautl -decrypt -inkey <私钥> -in <文件> -out <输出>`
```bash
# 使用 RSA 私钥解密
openssl rsautl -decrypt -inkey private.key -in encrypted.enc -out decrypted.txt
```

**基本写法：使用 OAEP 填充加密**
`openssl rsautl -encrypt -oaep -inkey <公钥> -pubin -in <输入> -out <输出>`
```bash
# 使用 OAEP 填充方案更安全
openssl rsautl -encrypt -oaep -inkey public.key -pubin -in plaintext.txt -out encrypted.enc
```

**基本写法：查看 RSA 密钥信息**
`openssl rsa -in <私钥> -text -noout`
```bash
# 查看 RSA 私钥详细信息
openssl rsa -in private.key -text -noout
```

---

## 数字签名

**基本写法：使用 RSA 签名文件**
`openssl dgst -sha256 -sign <私钥> -out <签名> <文件>`
```bash
# 使用 SHA-256 和 RSA 私钥签名文件
openssl dgst -sha256 -sign private.key -out signature.sig document.pdf
```

**基本写法：验证签名**
`openssl dgst -sha256 -verify <公钥> -signature <签名> <文件>`
```bash
# 验证文件的数字签名
openssl dgst -sha256 -verify public.key -signature signature.sig document.pdf
```

**基本写法：使用 ECDSA 签名**
`openssl dgst -sha384 -sign <EC私钥> -out <签名> <文件>`
```bash
# 使用 EC 私钥签名
openssl dgst -sha384 -sign ec_key.pem -out signature.sig document.pdf
```

**基本写法：使用 pkeyutl 签名**
`openssl pkeyutl -sign -inkey <私钥> -in <文件> -out <签名>`
```bash
# 使用 pkeyutl 签名
openssl pkeyutl -sign -inkey private.key -in document.pdf -out signature.sig
```

**基本写法：使用 pkeyutl 验证**
`openssl pkeyutl -verify -inkey <公钥> -pubin -in <文件> -sigfile <签名>`
```bash
# 使用 pkeyutl 验证签名
openssl pkeyutl -verify -inkey public.key -pubin -in document.pdf -sigfile signature.sig
```

---

## 哈希计算

**基本写法：计算文件 SHA-256**
`openssl dgst -sha256 <文件>`
```bash
# 计算文件的 SHA-256 哈希
openssl dgst -sha256 document.pdf
```

**基本写法：计算文件 MD5**
`openssl dgst -md5 <文件>`
```bash
# 计算文件的 MD5 哈希
openssl dgst -md5 document.pdf
```

**基本写法：计算字符串哈希**
`echo -n "<字符串>" | openssl dgst -sha256`
```bash
# 计算字符串的 SHA-256 哈希
echo -n "hello world" | openssl dgst -sha256
```

**基本写法：列出所有摘要算法**
`openssl list -digest-algorithms`
```bash
# 列出所有支持的哈希算法
openssl list -digest-algorithms
```

**基本写法：计算 HMAC**
`openssl dgst -sha256 -hmac "<密钥>" <文件>`
```bash
# 计算文件的 HMAC-SHA256
openssl dgst -sha256 -hmac "secret_key" document.pdf
```

**基本写法：二进制哈希输出**
`openssl dgst -binary -sha256 <文件>`
```bash
# 输出二进制形式的哈希
openssl dgst -binary -sha256 document.pdf
```

---

## 随机数生成

**基本写法：生成随机字节**
`openssl rand -hex <字节数>`
```bash
# 生成 16 字节的随机十六进制字符串
openssl rand -hex 16
```

**基本写法：生成 Base64 随机数**
`openssl rand -base64 <字节数>`
```bash
# 生成 32 字节的 Base64 随机数
openssl rand -base64 32
```

**基本写法：生成二进制随机数**
`openssl rand <字节数> > <文件>`
```bash
# 生成 1024 字节随机数到文件
openssl rand 1024 > random.bin
```

**基本写法：使用随机数作为密钥**
`openssl rand -hex 32`
```bash
# 生成 256 位的十六进制密钥
openssl rand -hex 32
```

---

## Base64 编码解码

**基本写法：Base64 编码**
`openssl base64 -in <输入> -out <输出>`
```bash
# 编码文件为 Base64
openssl base64 -in plaintext.txt -out encoded.b64
```

**基本写法：Base64 解码**
`openssl base64 -d -in <文件> -out <输出>`
```bash
# 解码 Base64 文件
openssl base64 -d -in encoded.b64 -out decoded.txt
```

**基本写法：字符串编码**
`echo -n "<字符串>" | openssl base64`
```bash
# 编码字符串为 Base64
echo -n "hello world" | openssl base64
```

**基本写法：字符串解码**
`echo "<Base64>" | openssl base64 -d`
```bash
# 解码 Base64 字符串
echo "aGVsbG8gd29ybGQ=" | openssl base64 -d
```

---

## 加密通信测试

**基本写法：测试 TLS 连接**
`openssl s_client -connect <主机>:<端口>`
```bash
# 测试 HTTPS 连接
openssl s_client -connect example.com:443
```

**基本写法：指定 TLS 版本**
`openssl s_client -tls1_2 -connect <主机>:<端口>`
```bash
# 强制使用 TLS 1.2
openssl s_client -tls1_2 -connect example.com:443
```

**基本写法：查看证书链**
`openssl s_client -showcerts -connect <主机>:<端口>`
```bash
# 查看完整证书链
openssl s_client -showcerts -connect example.com:443
```

**基本写法：测试 SMTP TLS**
`openssl s_client -starttls smtp -connect <主机>:<端口>`
```bash
# 测试 SMTP 服务的 TLS
openssl s_client -starttls smtp -connect smtp.example.com:587
```

**基本写法：列出支持的密码套件**
`openssl ciphers -v`
```bash
# 列出所有支持的密码套件
openssl ciphers -v
```

**基本写法：测试特定密码套件**
`openssl s_client -cipher <密码套件> -connect <主机>:<端口>`
```bash
# 测试服务器是否支持特定密码套件
openssl s_client -cipher 'ECDHE-RSA-AES256-GCM-SHA384' -connect example.com:443
```

---

## 实用加密组合

**基本写法：加密大文件（混合加密）**
```bash
`# 1. 生成随机密钥
openssl rand -hex 32 > key.bin
# 2. 用 AES 加密文件
openssl enc -aes-256-cbc -salt -pbkdf2 -in largefile -out largefile.enc -pass file:./key.bin
# 3. 用 RSA 公钥加密密钥
openssl rsautl -encrypt -inkey public.key -pubin -in key.bin -out key.bin.enc
# 4. 删除原始密钥
rm key.bin`
```
```bash
# 混合加密大文件
openssl rand -hex 32 > key.bin
openssl enc -aes-256-cbc -salt -pbkdf2 -in largefile -out largefile.enc -pass file:./key.bin
openssl rsautl -encrypt -inkey public.key -pubin -in key.bin -out key.bin.enc
rm key.bin
```

**基本写法：解密大文件**
```bash
`# 1. 用 RSA 私钥解密密钥
openssl rsautl -decrypt -inkey private.key -in key.bin.enc -out key.bin
# 2. 用 AES 解密文件
openssl enc -d -aes-256-cbc -pbkdf2 -in largefile.enc -out largefile -pass file:./key.bin`
```
```bash
# 解密混合加密的大文件
openssl rsautl -decrypt -inkey private.key -in key.bin.enc -out key.bin
openssl enc -d -aes-256-cbc -pbkdf2 -in largefile.enc -out largefile -pass file:./key.bin
```

---

## 密钥派生

**基本写法：使用 PBKDF2 派生密钥**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:iter:<迭代次数> PBKDF2`
```bash
# 使用 PBKDF2 派生 32 字节密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt123:iter:100000 PBKDF2
```

**基本写法：使用 scrypt 派生密钥**
`openssl kdf -keylen <长度> -kdfopts pass:<密码> scrypt`
```bash
# 使用 scrypt 派生密钥
openssl kdf -keylen 32 -kdfopts pass:password scrypt
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
| Cybersecurity OpenSSL 加密解密 | 037-OpenSSLEncrypt | 本文自身 |
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
