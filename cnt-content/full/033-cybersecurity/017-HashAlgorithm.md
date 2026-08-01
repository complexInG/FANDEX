---
order: 58
title: 哈希算法
module: cybersecurity
category: 'eng-infra'
difficulty: intermediate
description: '哈希算法原理：SHA-1/SHA-2/SHA-3/MD5/Bcrypt 等算法详解与应用场景。'
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/应急响应
  - cybersecurity/非对称加密
  - cybersecurity/安全开发
  - cybersecurity/合规与审计
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. 哈希算法基础

### 1.1 基本概念

哈希函数将任意长度输入映射为固定长度输出：

$$H: \{0,1\}^* \rightarrow \{0,1\}^n$$

### 1.2 安全性质

| 性质         | 描述                                                      |
| ------------ | --------------------------------------------------------- |
| 抗碰撞性     | 找到 $x \neq y$ 使 $H(x) = H(y)$ 在计算上不可行           |
| 抗原像性     | 给定 $h$，找到 $x$ 使 $H(x) = h$ 在计算上不可行           |
| 抗第二原像性 | 给定 $x$，找到 $y \neq x$ 使 $H(y) = H(x)$ 在计算上不可行 |
| 雪崩效应     | 输入微小变化导致输出巨大变化                              |

### 1.3 Merkle-Damgård 结构

大多数哈希算法采用此结构：

```
消息 → 填充 → 分块 → IV → [压缩函数] → [压缩函数] → ... → 哈希值
```

## 2. MD5 算法

### 2.1 概述

| 参数     | 值         |
| -------- | ---------- |
| 输出长度 | 128 位     |
| 分组长度 | 512 位     |
| 轮数     | 64（4×16） |
| 安全性   | 已破解     |

### 2.2 已知攻击

| 攻击         | 年份 | 描述                   |
| ------------ | ---- | ---------------------- |
| 碰撞攻击     | 2004 | 王小云团队找到实际碰撞 |
| 选择前缀碰撞 | 2006 | 可构造有意义的碰撞文件 |
| MD5 碰撞证书 | 2008 | 伪造 CA 证书           |

### 2.3 当前状态

**禁止用于安全场景**，仅可用于非安全目的（如文件校验、ETag）。

## 3. SHA-1 算法

### 3.1 概述

| 参数     | 值     |
| -------- | ------ |
| 输出长度 | 160 位 |
| 分组长度 | 512 位 |
| 轮数     | 80     |
| 安全性   | 已破解 |

### 3.2 SHAttered 攻击（2017）

Google 与 CWI 研究所成功找到 SHA-1 碰撞，计算代价约 $2^{63}$ 次。

**禁止用于安全场景**。

## 4. SHA-2 家族

### 4.1 概述

| 算法    | 输出长度 | 安全等级 |
| ------- | -------- | -------- |
| SHA-224 | 224 位   | 112 位   |
| SHA-256 | 256 位   | 128 位   |
| SHA-384 | 384 位   | 192 位   |
| SHA-512 | 512 位   | 256 位   |

### 4.2 SHA-256 算法流程

1. 消息填充（添加 1 位 + 零 + 64 位长度）
2. 分成 512 位分组
3. 每个分组进行 64 轮运算
4. 每轮使用：消息调度字、轮常数、位运算（AND、XOR、ROT）

### 4.3 代码示例

```python
import hashlib

# SHA-256
hash_sha256 = hashlib.sha256(b"Hello World").hexdigest()
# a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e

# SHA-512
hash_sha512 = hashlib.sha512(b"Hello World").hexdigest()

# HMAC
import hmac
hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()
```

### 4.4 长度扩展攻击

Merkle-Damgård 结构的弱点：已知 $H(m)$ 和 $m$ 的长度，可以计算 $H(m || padding || m')$ 而不知道 $m$。

**防御**：使用 HMAC 而非直接哈希。

## 5. SHA-3（Keccak）

### 5.1 概述

| 算法     | 输出长度 | 特点     |
| -------- | -------- | -------- |
| SHA3-224 | 224 位   | 海绵结构 |
| SHA3-256 | 256 位   | 海绵结构 |
| SHA3-384 | 384 位   | 海绵结构 |
| SHA3-512 | 512 位   | 海绵结构 |
| SHAKE128 | 可变     | XOF      |
| SHAKE256 | 可变     | XOF      |

### 5.2 海绵结构

```
吸收阶段：消息分块 XOR 到状态中，经过置换函数
挤出阶段：从状态中提取输出
```

**优势**：

- 不受长度扩展攻击影响
- 可扩展输出长度（XOF）
- 与 SHA-2 完全不同的结构

## 6. 密码存储专用哈希

### 6.1 为什么不能用普通哈希

| 攻击     | 描述                           |
| -------- | ------------------------------ |
| 彩虹表   | 预计算哈希值对照表             |
| 暴力破解 | GPU 每秒可计算数十亿次 SHA-256 |
| 字典攻击 | 常见密码列表                   |

### 6.2 Bcrypt

```python
import bcrypt

# 哈希密码
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

# 验证
bcrypt.checkpw(password.encode(), hashed)
```

| 参数         | 值                     |
| ------------ | ---------------------- |
| 输出长度     | 184 位                 |
| 内置盐       | 是                     |
| 自适应       | rounds 参数（默认 12） |
| 最大密码长度 | 72 字节                |

### 6.3 Argon2

```python
from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash("password")
ph.verify(hash, "password")
```

| 参数     | 描述             |
| -------- | ---------------- |
| 时间成本 | 迭代次数         |
| 内存成本 | 内存使用量（MB） |
| 并行度   | 线程数           |

**Argon2 优势**：抗 GPU/ASIC 攻击，2015 年密码哈希竞赛冠军。

### 6.4 PBKDF2

```python
import hashlib
import os

key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 600000, dklen=32)
```

| 参数     | 推荐值              |
| -------- | ------------------- |
| 迭代次数 | 600,000+（SHA-256） |
| 盐长度   | 16+ 字节            |
| 输出长度 | 32+ 字节            |

## 7. 应用场景与算法选择

| 场景       | 推荐算法                   |
| ---------- | -------------------------- |
| 密码存储   | Argon2id > Bcrypt > PBKDF2 |
| 数据完整性 | SHA-256 / SHA-3            |
| 数字签名   | SHA-256 / SHA-384          |
| 文件校验   | SHA-256                    |
| HMAC       | HMAC-SHA256                |
| 禁止使用   | MD5、SHA-1（安全场景）     |

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
| 哈希算法 | 017-HashAlgorithm | 本文自身 |
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
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文的并列主题 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
