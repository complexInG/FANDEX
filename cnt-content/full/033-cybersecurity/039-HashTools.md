---
order: 390
title: Cybersecurity 哈希工具
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity 哈希工具 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## md5sum 哈希计算

**基本写法：计算文件 MD5**
`md5sum <文件>`
```bash
# 计算文件的 MD5 哈希
md5sum document.pdf
```

**基本写法：计算多个文件 MD5**
`md5sum <文件1> <文件2>`
```bash
# 计算多个文件的 MD5
md5sum file1.txt file2.txt file3.txt
```

**基本写法：保存哈希到文件**
`md5sum <文件> > <哈希文件>`
```bash
# 保存 MD5 哈希到文件
md5sum document.pdf > checksums.md5
```

**基本写法：验证文件 MD5**
`md5sum -c <哈希文件>`
```bash
# 验证文件 MD5 是否匹配
md5sum -c checksums.md5
```

**基本写法：计算字符串 MD5**
`echo -n "<字符串>" | md5sum`
```bash
# 计算字符串的 MD5
echo -n "hello world" | md5sum
```

---

## sha256sum 哈希计算

**基本写法：计算文件 SHA-256**
`sha256sum <文件>`
```bash
# 计算文件的 SHA-256 哈希
sha256sum document.pdf
```

**基本写法：保存 SHA-256 到文件**
`sha256sum <文件> > <哈希文件>`
```bash
# 保存 SHA-256 哈希到文件
sha256sum document.pdf > checksums.sha256
```

**基本写法：验证文件 SHA-256**
`sha256sum -c <哈希文件>`
```bash
# 验证文件 SHA-256 是否匹配
sha256sum -c checksums.sha256
```

**基本写法：计算字符串 SHA-256**
`echo -n "<字符串>" | sha256sum`
```bash
# 计算字符串的 SHA-256
echo -n "hello world" | sha256sum
```

**基本写法：批量验证**
`sha256sum -c <哈希文件> --quiet`
```bash
# 只显示验证失败的文件
sha256sum -c checksums.sha256 --quiet
```

---

## 其他哈希工具

**基本写法：计算 SHA-1**
`sha1sum <文件>`
```bash
# 计算文件的 SHA-1 哈希
sha1sum document.pdf
```

**基本写法：计算 SHA-512**
`sha512sum <文件>`
```bash
# 计算文件的 SHA-512 哈希
sha512sum document.pdf
```

**基本写法：计算 SHA-224**
`sha224sum <文件>`
```bash
# 计算文件的 SHA-224 哈希
sha224sum document.pdf
```

**基本写法：计算 SHA-384**
`sha384sum <文件>`
```bash
# 计算文件的 SHA-384 哈希
sha384sum document.pdf
```

---

## OpenSSL 哈希

**基本写法：使用 OpenSSL 计算 SHA-256**
`openssl dgst -sha256 <文件>`
```bash
# 使用 OpenSSL 计算 SHA-256
openssl dgst -sha256 document.pdf
```

**基本写法：使用 OpenSSL 计算 MD5**
`openssl dgst -md5 <文件>`
```bash
# 使用 OpenSSL 计算 MD5
openssl dgst -md5 document.pdf
```

**基本写法：使用 OpenSSL 计算 SHA-3**
`openssl dgst -sha3-256 <文件>`
```bash
# 使用 OpenSSL 计算 SHA3-256
openssl dgst -sha3-256 document.pdf
```

**基本写法：使用 OpenSSL 计算字符串哈希**
`echo -n "<字符串>" | openssl dgst -sha256`
```bash
# 计算字符串的 SHA-256
echo -n "hello world" | openssl dgst -sha256
```

---

## HMAC 计算

**基本写法：计算 HMAC-SHA256**
`openssl dgst -sha256 -hmac "<密钥>" <文件>`
```bash
# 计算 HMAC-SHA256
openssl dgst -sha256 -hmac "secret_key" document.pdf
```

**基本写法：使用十六进制密钥计算 HMAC**
`openssl dgst -sha256 -mac HMAC -macopt hexkey:<密钥> <文件>`
```bash
# 使用十六进制密钥计算 HMAC
openssl dgst -sha256 -mac HMAC -macopt hexkey:369bd7d655 document.pdf
```

**基本写法：计算字符串 HMAC**
`echo -n "<字符串>" | openssl dgst -sha256 -hmac "<密钥>"`
```bash
# 计算字符串的 HMAC-SHA256
echo -n "hello world" | openssl dgst -sha256 -hmac "secret_key"
```

---

## 哈希识别

**基本写法：识别哈希类型**
`hashid <哈希值>`
```bash
# 识别哈希值的类型
hashid 5d41402abc4b2a76b9719d911017c592
```

**基本写法：按长度识别**
```text
# 根据哈希长度判断算法
32 字符  -> MD5
40 字符  -> SHA1
56 字符  -> SHA224
64 字符  -> SHA256
96 字符  -> SHA384
128 字符 -> SHA512
```
```bash
# 常见哈希长度对照
echo "MD5: $(echo -n 'test' | md5sum | cut -d' ' -f1 | wc -c)"
echo "SHA256: $(echo -n 'test' | sha256sum | cut -d' ' -f1 | wc -c)"
```

**基本写法：识别密码哈希格式**
```text
# 常见密码哈希前缀
$2a$ / $2b$  -> bcrypt
$6$          -> SHA512crypt
$5$          -> SHA256crypt
$1$          -> MD5crypt
$y$          -> yescrypt
$argon2id$   -> Argon2id
```
```bash
# 查看 /etc/shadow 中的哈希格式
grep $USER /etc/shadow
```

---

## 文件完整性校验

**基本写法：生成校验文件**
`sha256sum <文件1> <文件2> > <校验文件>`
```bash
# 生成多个文件的校验文件
sha256sum file1.txt file2.txt file3.txt > checksums.sha256
```

**基本写法：验证文件完整性**
`sha256sum -c <校验文件>`
```bash
# 验证所有文件的完整性
sha256sum -c checksums.sha256
```

**基本写法：递归计算目录哈希**
`find <目录> -type f -exec sha256sum {} + > <校验文件>`
```bash
# 递归计算目录下所有文件的 SHA-256
find /important/data -type f -exec sha256sum {} + > checksums.sha256
```

**基本写法：只显示验证失败的文件**
`sha256sum -c <校验文件> --quiet`
```bash
# 静默模式只显示失败的验证
sha256sum -c checksums.sha256 --quiet
```

**基本写法：严格模式验证**
`sha256sum -c <校验文件> --strict`
```bash
# 严格模式遇到错误返回非零退出码
sha256sum -c checksums.sha256 --strict
```

---

## bcrypt 密码哈希

**基本写法：使用 Python 生成 bcrypt 哈希**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt()).decode())"`
```bash
# 生成 bcrypt 密码哈希
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt(12)).decode())"
```

**基本写法：验证 bcrypt 密码**
`python3 -c "import bcrypt; print(bcrypt.checkpw(b'<密码>', b'<哈希>'))"`
```bash
# 验证 bcrypt 密码
python3 -c "import bcrypt; print(bcrypt.checkpw(b'mypassword', b'\$2b\$12\$...'))"
```

**基本写法：使用 htpasswd 生成 bcrypt**
`htpasswd -nbB <用户> <密码>`
```bash
# 使用 Apache htpasswd 生成 bcrypt 哈希
htpasswd -nbB admin secret123
```

---

## PBKDF2 密钥派生

**基本写法：使用 OpenSSL PBKDF2**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:iter:<迭代次数> PBKDF2`
```bash
# 使用 PBKDF2 派生 32 字节密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt:iter:600000 PBKDF2
```

**基本写法：使用 Python PBKDF2**
`python3 -c "import hashlib, binascii; print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'<密码>', b'<盐>', <迭代次数>)).decode())"`
```bash
# 使用 Python 计算 PBKDF2
python3 -c "import hashlib, binascii; print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 600000)).decode())"
```

---

## 实用哈希组合

**基本写法：比较两个文件是否相同**
`sha256sum <文件1> <文件2> | cut -d' ' -f1 | uniq -d`
```bash
# 比较两个文件的哈希是否相同
sha256sum file1.txt file2.txt
```

**基本写法：批量检查文件变更**
`sha256sum -c <校验文件> --quiet && echo "文件无变更" || echo "文件已变更"`
```bash
# 检查文件是否被篡改
sha256sum -c checksums.sha256 --quiet && echo "文件无变更" || echo "文件已变更"
```

**基本写法：生成文件指纹**
`sha256sum <文件> | cut -d' ' -f1`
```bash
# 只输出哈希值
sha256sum document.pdf | cut -d' ' -f1
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
| Cybersecurity OpenSSL 证书管理 | 036-OpenSSLCert | 本文的并列主题 |
| Cybersecurity OpenSSL 加密解密 | 037-OpenSSLEncrypt | 本文的安全延伸 |
| Cybersecurity nmap 端口扫描 | 038-NmapScan | 本文的并列主题 |
| Cybersecurity 哈希工具 | 039-HashTools | 本文自身 |
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
