---
order: 420
title: Cybersecurity SSH 密钥管理
module: cybersecurity

category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity SSH 密钥管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## ssh-keygen 密钥生成

**基本写法：生成 RSA 密钥**
`ssh-keygen -t rsa -b <位数>`
```bash
# 生成 4096 位 RSA 密钥
ssh-keygen -t rsa -b 4096
```

**基本写法：生成 Ed25519 密钥**
`ssh-keygen -t ed25519`
```bash
# 生成 Ed25519 密钥（推荐）
ssh-keygen -t ed25519 -C "user@example.com"
```

**基本写法：生成 ECDSA 密钥**
`ssh-keygen -t ecdsa -b <位数>`
```bash
# 生成 521 位 ECDSA 密钥
ssh-keygen -t ecdsa -b 521
```

**基本写法：指定密钥文件名**
`ssh-keygen -f <文件名>`
```bash
# 指定密钥文件路径
ssh-keygen -t ed25519 -f ~/.ssh/deploy_key
```

**基本写法：生成无密码密钥**
`ssh-keygen -t rsa -N ""`
```bash
# 生成无密码的密钥（用于自动化）
ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/auto_key
```

**基本写法：添加注释**
`ssh-keygen -t ed25519 -C "<注释>"`
```bash
# 添加注释标识密钥用途
ssh-keygen -t ed25519 -C "production-deploy-2026"
```

---

## 密钥管理

**基本写法：查看密钥指纹**
`ssh-keygen -l -f <公钥>`
```bash
# 查看公钥指纹
ssh-keygen -l -f ~/.ssh/id_rsa.pub
```

**基本写法：查看密钥指纹（SHA256）**
`ssh-keygen -l -E sha256 -f <公钥>`
```bash
# 查看 SHA256 格式指纹
ssh-keygen -l -E sha256 -f ~/.ssh/id_rsa.pub
```

**基本写法：查看密钥图形指纹**
`ssh-keygen -l -v -f <公钥>`
```bash
# 查看随机图形指纹
ssh-keygen -l -v -f ~/.ssh/id_rsa.pub
```

**基本写法：修改密钥密码**
`ssh-keygen -p -f <私钥>`
```bash
# 修改私钥的密码
ssh-keygen -p -f ~/.ssh/id_rsa
```

**基本写法：移除密钥密码**
`ssh-keygen -p -N "" -f <私钥>`
```bash
# 移除私钥密码
ssh-keygen -p -N "" -f ~/.ssh/id_rsa
```

---

## 密钥转换与导出

**基本写法：从私钥提取公钥**
`ssh-keygen -y -f <私钥>`
```bash
# 从私钥提取公钥
ssh-keygen -y -f ~/.ssh/id_rsa > ~/.ssh/id_rsa.pub
```

**基本写法：转换密钥格式**
`ssh-keygen -p -m PEM -f <私钥>`
```bash
# 将密钥转换为 PEM 格式
ssh-keygen -p -m PEM -f ~/.ssh/id_rsa
```

**基本写法：生成 RFC4716 格式公钥**
`ssh-keygen -e -m RFC4716 -f <公钥>`
```bash
# 转换为 RFC4716 格式
ssh-keygen -e -m RFC4716 -f ~/.ssh/id_rsa.pub
```

**基本写法：从 RFC4716 转换回 OpenSSH**
`ssh-keygen -i -m RFC4716 -f <文件>`
```bash
# 从 RFC4716 格式导入
ssh-keygen -i -m RFC4716 -f public.key
```

---

## ssh-copy-id 部署公钥

**基本写法：复制公钥到远程**
`ssh-copy-id <用户>@<主机>`
```bash
# 部署公钥到远程主机
ssh-copy-id user@192.168.1.1
```

**基本写法：指定公钥文件**
`ssh-copy-id -i <公钥> <用户>@<主机>`
```bash
# 指定公钥文件部署
ssh-copy-id -i ~/.ssh/my_key.pub user@192.168.1.1
```

**基本写法：指定端口**
`ssh-copy-id -p <端口> <用户>@<主机>`
```bash
# 指定 SSH 端口
ssh-copy-id -p 2222 user@192.168.1.1
```

**基本写法：指定 SSH 选项**
`ssh-copy-id -o "<选项>" <用户>@<主机>`
```bash
# 传递 SSH 选项
ssh-copy-id -o "StrictHostKeyChecking=no" user@192.168.1.1
```

---

## known_hosts 管理

**基本写法：查看 known_hosts**
`cat ~/.ssh/known_hosts`
```bash
# 查看 known_hosts 文件内容
cat ~/.ssh/known_hosts
```

**基本写法：删除主机记录**
`ssh-keygen -R <主机>`
```bash
# 删除指定主机的记录
ssh-keygen -R 192.168.1.1
```

**基本写法：查看主机指纹**
`ssh-keygen -F <主机>`
```bash
# 查看 known_hosts 中主机的指纹
ssh-keygen -F 192.168.1.1
```

**基本写法：哈希 known_hosts**
`ssh-keygen -H`
```bash
# 哈希 known_hosts 文件中的主机名
ssh-keygen -H -f ~/.ssh/known_hosts
```

**基本写法：验证主机密钥**
`ssh-keygen -F <主机> -l`
```bash
# 查看主机密钥指纹
ssh-keygen -F github.com -l
```

---

## ssh-agent 代理

**基本写法：启动 ssh-agent**
`eval $(ssh-agent)`
```bash
# 启动 ssh-agent
eval $(ssh-agent)
```

**基本写法：添加密钥到 agent**
`ssh-add <私钥>`
```bash
# 添加私钥到 agent
ssh-add ~/.ssh/id_rsa
```

**基本写法：添加所有默认密钥**
`ssh-add`
```bash
# 添加默认密钥
ssh-add
```

**基本写法：列出已添加的密钥**
`ssh-add -l`
```bash
# 列出 agent 中的密钥指纹
ssh-add -l
```

**基本写法：列出密钥公钥**
`ssh-add -L`
```bash
# 列出 agent 中的密钥公钥
ssh-add -L
```

**基本写法：删除指定密钥**
`ssh-add -d <私钥>`
```bash
# 从 agent 中删除密钥
ssh-add -d ~/.ssh/id_rsa
```

**基本写法：删除所有密钥**
`ssh-add -D`
```bash
# 清空 agent 中所有密钥
ssh-add -D
```

**基本写法：锁定 agent**
`ssh-add -x`
```bash
# 用密码锁定 agent
ssh-add -x
```

**基本写法：解锁 agent**
`ssh-add -X`
```bash
# 解锁 agent
ssh-add -X
```

---

## SSH 配置文件

**基本写法：配置主机别名**
```sshconfig
`Host <别名>
    HostName <主机>
    User <用户>
    Port <端口>
    IdentityFile <私钥>`
```
```sshconfig
# SSH 配置文件 ~/.ssh/config
Host prod
    HostName 192.168.1.100
    User deploy
    Port 22
    IdentityFile ~/.ssh/prod_key
```

**基本写法：通配符配置**
```sshconfig
`Host *.<域名>
    User <用户>
    IdentityFile <私钥>`
```
```sshconfig
# 配置所有 *.example.com 主机
Host *.example.com
    User admin
    IdentityFile ~/.ssh/work_key
```

**基本写法：安全配置**
```sshconfig
`Host *
    ServerAliveInterval <秒数>
    ServerAliveCountMax <次数>
    StrictHostKeyChecking <yes/no>`
```
```sshconfig
# 全局安全配置
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    StrictHostKeyChecking yes
```

---

## 证书认证

**基本写法：生成 CA 密钥**
`ssh-keygen -t ed25519 -f <CA密钥>`
```bash
# 生成 SSH CA 密钥
ssh-keygen -t ed25519 -f ~/.ssh/ca_key
```

**基本写法：签名用户公钥**
`ssh-keygen -s <CA密钥> -I <标识> -n <用户> <用户公钥>`
```bash
# 用 CA 签名用户公钥
ssh-keygen -s ~/.ssh/ca_key -I user_alice -n alice ~/.ssh/alice.pub
```

**基本写法：签名主机密钥**
`ssh-keygen -s <CA密钥> -I <标识> -h -n <主机名> <主机公钥>`
```bash
# 用 CA 签名主机密钥
ssh-keygen -s ~/.ssh/ca_key -I host_server1 -h -n server1.example.com /etc/ssh/ssh_host_ed25519_key.pub
```

**基本写法：信任 CA**
`# /etc/ssh/sshd_config`
```bash
# 配置服务器信任 CA
echo "TrustedUserCAKeys /etc/ssh/ca_key.pub" >> /etc/ssh/sshd_config
systemctl restart sshd
```

---

## 安全最佳实践

**基本写法：禁用密码登录**
`# /etc/ssh/sshd_config`
```bash
# 禁用密码认证只允许密钥
sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
systemctl restart sshd
```

**基本写法：禁止 root 登录**
`# /etc/ssh/sshd_config`
```bash
# 禁止 root 直接登录
sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart sshd
```

**基本写法：限制登录尝试**
`# /etc/ssh/sshd_config`
```bash
# 限制最大认证尝试次数
echo "MaxAuthTries 3" >> /etc/ssh/sshd_config
systemctl restart sshd
```

**基本写法：限制用户组**
`# /etc/ssh/sshd_config`
```bash
# 只允许特定组登录
echo "AllowGroups ssh-users" >> /etc/ssh/sshd_config
systemctl restart sshd
```

**基本写法：设置登录宽限时间**
`# /etc/ssh/sshd_config`
```bash
# 设置登录宽限时间 30 秒
echo "LoginGraceTime 30" >> /etc/ssh/sshd_config
systemctl restart sshd
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
| Cybersecurity SSH 密钥管理 | 042-SSHKeys | 本文自身 |
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
