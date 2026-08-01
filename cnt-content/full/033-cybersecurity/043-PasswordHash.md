---
order: 430
title: Cybersecurity 密码哈希
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity 密码哈希 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## bcrypt 哈希

**基本写法：使用 Python 生成 bcrypt 哈希**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt()).decode())"`
```bash
# 生成 bcrypt 哈希
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt(12)).decode())"
```

**基本写法：指定计算成本**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt(<成本>)).decode())"`
```bash
# 使用成本因子 12（默认 12）
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt(14)).decode())"
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
# 使用 Apache htpasswd 生成 bcrypt
htpasswd -nbB admin secret123
```

**基本写法：使用 Node.js 生成 bcrypt**
`node -e "const bcrypt=require('bcrypt'); console.log(bcrypt.hashSync('密码', 12))"`
```bash
# Node.js 生成 bcrypt
node -e "const bcrypt=require('bcrypt'); console.log(bcrypt.hashSync('mypassword', 12))"
```

---

## Argon2 哈希

**基本写法：使用 argon2 命令行工具**
`argon2 <盐> -id -t <迭代次数> -m <内存> -p <并行数> -l <长度>`
```bash
# 使用 argon2 生成哈希
echo -n "mypassword" | argon2 somesalt -id -t 3 -m 65536 -p 1 -l 32
```

**基本写法：使用 Python argon2**
`python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.hash('<密码>'))"`
```bash
# 使用 argon2-cffi 库
python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.hash('mypassword'))"
```

**基本写法：验证 argon2 密码**
`python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.verify('<哈希>', '<密码>'))"`
```bash
# 验证 argon2 密码
python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.verify('\$argon2id\$...', 'mypassword'))"
```

**基本写法：使用 Node.js argon2**
`node -e "const argon2=require('argon2'); argon2.hash('密码').then(console.log)"`
```bash
# Node.js 生成 argon2
node -e "const argon2=require('argon2'); argon2.hash('mypassword').then(console.log)"
```

---

## PBKDF2 哈希

**基本写法：使用 Python PBKDF2**
`python3 -c "import hashlib, binascii, os; salt=os.urandom(16); print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'<密码>', salt, <迭代次数>)).decode())"`
```bash
# 使用 PBKDF2-SHA256 派生密钥
python3 -c "import hashlib, binascii, os; salt=os.urandom(16); print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'mypassword', salt, 600000)).decode())"
```

**基本写法：使用 OpenSSL PBKDF2**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:iter:<迭代次数> PBKDF2`
```bash
# OpenSSL 生成 PBKDF2 密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt:iter:600000 PBKDF2
```

**基本写法：使用 Django PBKDF2**
`python3 -c "from django.contrib.auth.hashers import PBKDF2PasswordHasher; h=PBKDF2PasswordHasher(); print(h.encode('<密码>', h.salt()))"`
```bash
# Django 风格 PBKDF2 哈希
python3 -c "from django.contrib.auth.hashers import PBKDF2PasswordHasher; h=PBKDF2PasswordHasher(); print(h.encode('mypassword', h.salt()))"
```

---

## scrypt 哈希

**基本写法：使用 OpenSSL scrypt**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:n:<N>:r:<r>:p:<p> scrypt`
```bash
# 使用 scrypt 派生密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt:n:16384:r:8:p:1 scrypt
```

**基本写法：使用 Python scrypt**
`python3 -c "import hashlib; print(hashlib.scrypt(b'<密码>', salt=b'<盐>', n=16384, r=8, p=1, dklen=32).hex())"`
```bash
# Python 生成 scrypt 哈希
python3 -c "import hashlib; print(hashlib.scrypt(b'mypassword', salt=b'salt', n=16384, r=8, p=1, dklen=32).hex())"
```

**基本写法：使用 Node.js scrypt**
`node -e "const crypto=require('crypto'); console.log(crypto.scryptSync('密码', '盐', 64).toString('hex'))"`
```bash
# Node.js 生成 scrypt 哈希
node -e "const crypto=require('crypto'); console.log(crypto.scryptSync('mypassword', 'salt', 64).toString('hex'))"
```

---

## Linux 系统密码哈希

**基本写法：使用 mkpasswd**
`mkpasswd -m <算法> <密码>`
```bash
# 生成 SHA-512 密码哈希
mkpasswd -m sha-512 mypassword
```

**基本写法：使用 openssl 生成 crypt 哈希**
`openssl passwd -6 <密码>`
```bash
# 生成 SHA-512crypt 哈希
openssl passwd -6 mypassword
```

**基本写法：使用 openssl 生成 bcrypt**
`openssl passwd -bcrypt <密码>`
```bash
# 生成 bcrypt 哈希
openssl passwd -bcrypt mypassword
```

**基本写法：使用 Python crypt**
`python3 -c "import crypt; print(crypt.crypt('<密码>', crypt.mksalt(crypt.METHOD_SHA512)))"`
```bash
# 生成 SHA-512crypt 密码哈希
python3 -c "import crypt; print(crypt.crypt('mypassword', crypt.mksalt(crypt.METHOD_SHA512)))"
```

---

## 密码哈希验证

**基本写法：使用 Python crypt 验证**
`python3 -c "import crypt; print(crypt.crypt('<密码>', '<哈希>') == '<哈希>')"`
```bash
# 验证密码哈希
python3 -c "import crypt; print(crypt.crypt('mypassword', '\$6\$...') == '\$6\$...')"
```

**基本写法：使用 openssl 验证**
`openssl passwd -6 -salt <盐> <密码>`
```bash
# 验证密码哈希
openssl passwd -6 -salt abc123 mypassword
```

**基本写法：使用 htpasswd 验证**
`htpasswd -bv <密码文件> <用户> <密码>`
```bash
# 验证 htpasswd 中的密码
htpasswd -bv /etc/nginx/.htpasswd admin secret123
```

---

## Django 密码哈希

**基本写法：使用 Django 生成密码哈希**
`python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('<密码>'))"`
```bash
# Django 生成 PBKDF2 密码哈希
python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('mypassword'))"
```

**基本写法：使用 Django 验证密码**
`python3 -c "from django.contrib.auth.hashers import check_password; print(check_password('<密码>', '<哈希>'))"`
```bash
# Django 验证密码
python3 -c "from django.contrib.auth.hashers import check_password; print(check_password('mypassword', 'pbkdf2_sha256\$...'))"
```

**基本写法：使用 Django Argon2**
`python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('<密码>', hasher='argon2'))"`
```bash
# Django 使用 Argon2 哈希
python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('mypassword', hasher='argon2'))"
```

---

## Spring Security 密码编码

**基本写法：使用 BCryptPasswordEncoder**
```java
`BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
String hash = encoder.encode("密码");
boolean match = encoder.matches("密码", hash);`
```
```java
// Spring Security BCrypt 编码
BCryptPasswordEncoder encoder = new BCryptPasswordEncoder(12);
String hash = encoder.encode("mypassword");
boolean match = encoder.matches("mypassword", hash);
```

**基本写法：使用 Argon2PasswordEncoder**
```java
`Argon2PasswordEncoder encoder = new Argon2PasswordEncoder();
String hash = encoder.encode("密码");`
```
```java
// Spring Security Argon2 编码
Argon2PasswordEncoder encoder = new Argon2PasswordEncoder();
String hash = encoder.encode("mypassword");
```

---

## Node.js 密码哈希

**基本写法：使用 bcrypt**
`node -e "const bcrypt=require('bcrypt'); bcrypt.hash('密码', 12).then(console.log)"`
```bash
# Node.js bcrypt 哈希
node -e "const bcrypt=require('bcrypt'); bcrypt.hash('mypassword', 12).then(console.log)"
```

**基本写法：验证 bcrypt**
`node -e "const bcrypt=require('bcrypt'); bcrypt.compare('密码', '哈希').then(console.log)"`
```bash
# Node.js 验证 bcrypt
node -e "const bcrypt=require('bcrypt'); bcrypt.compare('mypassword', '\$2b\$...').then(console.log)"
```

**基本写法：使用 scrypt**
`node -e "const crypto=require('crypto'); const hash=crypto.scryptSync('密码','盐',64).toString('hex'); console.log(hash)"`
```bash
# Node.js 内置 scrypt
node -e "const crypto=require('crypto'); const hash=crypto.scryptSync('mypassword','salt',64).toString('hex'); console.log(hash)"
```

---

## 密码强度检测

**基本写法：检查密码长度**
`python3 -c "p='<密码>'; print(len(p) >= 12 and '足够' or '不足')"`
```bash
# 检查密码长度是否至少 12 位
python3 -c "p='mypassword'; print('OK' if len(p) >= 12 else 'Too short')"
```

**基本写法：检查密码复杂度**
`python3 -c "import re; p='<密码>'; print(bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@\$!%*?&]).{12,}$', p)))"`
```bash
# 检查密码是否包含大小写字母数字特殊字符
python3 -c "import re; p='MyP@ssw0rd2026'; print(bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@\$!%*?&]).{12,}$', p)))"
```

**基本写法：使用 passlib 检测**
`python3 -c "from passlib.hash import bcrypt; print(bcrypt.using(rounds=12).hash('<密码>'))"`
```bash
# 使用 passlib 库生成 bcrypt
python3 -c "from passlib.hash import bcrypt; print(bcrypt.using(rounds=12).hash('mypassword'))"
```

---

## 密码哈希最佳实践

**基本写法：推荐算法对比**
```text
`算法       推荐参数                  说明
Argon2id   memory=64MB, iter=3      首选，抗 GPU/ASIC
bcrypt     cost=12+                 成熟可靠
scrypt     N=16384, r=8, p=1        内存困难函数
PBKDF2     iterations=600000+       兼容性最好但较弱`
```
```text
# 密码哈希算法推荐顺序
1. Argon2id（最佳，FIPS 203 标准）
2. bcrypt（成熟，cost >= 12）
3. scrypt（内存困难，N=16384）
4. PBKDF2（兼容性，迭代 >= 600000）
```

**基本写法：弱算法警告**
```text
`已废弃：MD5、SHA1、DES、3DES、RC4
不推荐：直接使用 SHA256 哈希密码
推荐：使用专门的密码哈希函数 bcrypt/Argon2`
```
```bash
# 检查 /etc/shadow 中的哈希算法
grep $USER /etc/shadow | cut -d: -f2 | cut -d$ -f2
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
| Cybersecurity 哈希工具 | 039-HashTools | 本文的并列主题 |
| Cybersecurity hashcat 密码破解 | 040-Hashcat | 本文的并列主题 |
| Cybersecurity GPG 加密与签名 | 041-GPGEncrypt | 本文的安全延伸 |
| Cybersecurity SSH 密钥管理 | 042-SSHKeys | 本文的并列主题 |
| Cybersecurity 密码哈希 | 043-PasswordHash | 本文自身 |
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
