---
order: 58
title: 安全开发
module: cybersecurity
category: 网络安全
difficulty: intermediate
description: 安全开发：SDL、威胁建模、安全编码、SAST/DAST与安全测试
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/非对称加密
  - cybersecurity/哈希算法
  - cybersecurity/合规与审计
  - cybersecurity/数字证书
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. 安全开发生命周期（SDL）

### 1.1 SDL 阶段

| 阶段 | 安全活动           |
| ---- | ------------------ |
| 需求 | 安全需求、合规要求 |
| 设计 | 威胁建模           |
| 实现 | 安全编码、代码审查 |
| 测试 | SAST/DAST/渗透测试 |
| 发布 | 安全评估、签名     |
| 运维 | 漏洞响应、监控     |

### 1.2 安全左移

将安全活动前移到开发早期，降低修复成本：

$$\text{修复成本}：\text{需求阶段} \times 1 < \text{编码阶段} \times 10 < \text{测试阶段} \times 100 < \text{生产阶段} \times 1000$$

## 2. 威胁建模

### 2.1 STRIDE 模型

| 威胁              | 安全属性 | 示例     |
| ----------------- | -------- | -------- |
| Spoofing          | 认证     | 身份冒充 |
| Tampering         | 完整性   | 数据篡改 |
| Repudiation       | 不可否认 | 否认操作 |
| Info Disclosure   | 机密性   | 信息泄露 |
| Denial of Service | 可用性   | 服务拒绝 |
| Elevation         | 授权     | 权限提升 |

### 2.2 威胁建模流程

```
1. 绘制系统架构图
2. 识别信任边界
3. 应用STRIDE识别威胁
4. 评估风险等级
5. 制定缓解措施
```

## 3. 安全编码

### 3.1 输入验证

```python
# 白名单验证
import re
if not re.match(r'^[a-zA-Z0-9_]{1,50}$', username):
    raise ValueError("Invalid username")

# 参数化查询
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### 3.2 输出编码

```python
from markupsafe import escape
html = f"<p>Hello, {escape(name)}</p>"
```

### 3.3 安全配置

```python
# Cookie安全
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# 安全头
@app.after_request
def set_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

## 4. 安全测试

### 4.1 SAST

静态应用安全测试，扫描源代码：

| 工具      | 语言   |
| --------- | ------ |
| Semgrep   | 多语言 |
| SonarQube | 多语言 |
| CodeQL    | 多语言 |
| Bandit    | Python |
| Brakeman  | Ruby   |

### 4.2 DAST

动态应用安全测试，测试运行中的应用：

| 工具       | 特点      |
| ---------- | --------- |
| OWASP ZAP  | 开源      |
| Burp Suite | 专业      |
| Nikto      | Web服务器 |

### 4.3 SCA

软件成分分析，检查依赖漏洞：

| 工具                   | 说明       |
| ---------------------- | ---------- |
| Dependabot             | GitHub集成 |
| Snyk                   | 商业       |
| Trivy                  | 开源       |
| OWASP Dependency-Check | 开源       |

## 5. 安全代码审查

### 5.1 审查清单

| 类别 | 检查项             |
| ---- | ------------------ |
| 认证 | 密码存储、会话管理 |
| 授权 | 访问控制、权限检查 |
| 输入 | 验证、过滤、编码   |
| 输出 | 编码、CSP          |
| 加密 | 算法选择、密钥管理 |
| 日志 | 敏感信息脱敏       |
| 错误 | 不暴露堆栈信息     |

### 5.2 常见安全缺陷

| 缺陷           | CWE     | 严重度 |
| -------------- | ------- | ------ |
| SQL注入        | CWE-89  | 高     |
| XSS            | CWE-79  | 高     |
| 硬编码密码     | CWE-259 | 高     |
| 不安全反序列化 | CWE-502 | 高     |
| 路径遍历       | CWE-22  | 高     |
| 不安全随机数   | CWE-330 | 中     |

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
| 安全开发 | 018-SecureDevelopment | 本文自身 |
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
