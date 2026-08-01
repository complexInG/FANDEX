---
order: 65
title: 输入验证
module: cybersecurity
category: 'eng-infra'
difficulty: intermediate
description: 输入验证与过滤：验证策略、数据净化、常见绕过与安全实践详解。
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/漏洞扫描
  - cybersecurity/安全编码原则
  - cybersecurity/认证与授权
  - 'cybersecurity/OWASP-Top-10详解'
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. 输入验证原则

### 1.1 核心原则

| 原则             | 描述                       |
| ---------------- | -------------------------- |
| 不信任任何输入   | 所有外部数据都不可信       |
| 白名单优于黑名单 | 定义允许的输入，而非禁止的 |
| 纵深验证         | 多层验证                   |
| 尽早验证         | 在数据入口处验证           |
| 一致验证         | 前后端使用相同规则         |

### 1.2 输入来源

| 来源     | 示例                        |
| -------- | --------------------------- |
| 表单数据 | 用户名、密码、搜索词        |
| URL 参数 | `?id=1&page=2`              |
| HTTP 头  | Cookie、User-Agent、Referer |
| 文件上传 | 文件名、文件内容            |
| API 请求 | JSON/XML 请求体             |
| 数据库   | 二次注入                    |
| 环境变量 | 配置注入                    |

## 2. 验证策略

### 2.1 白名单验证

```python
import re

# 用户名：仅允许字母数字下划线
def validate_username(value):
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', value):
        raise ValueError("Invalid username")
    return value

# 颜色值
def validate_color(value):
    if value not in ['red', 'green', 'blue', 'yellow']:
        raise ValueError("Invalid color")
    return value

# 枚举类型
def validate_status(value):
    valid = {'active', 'inactive', 'pending'}
    if value not in valid:
        raise ValueError("Invalid status")
    return value
```

### 2.2 数据类型验证

```python
# 整数验证
def validate_int(value, min_val=None, max_val=None):
    try:
        num = int(value)
    except (ValueError, TypeError):
        raise ValueError("Must be an integer")
    if min_val is not None and num < min_val:
        raise ValueError(f"Must be >= {min_val}")
    if max_val is not None and num > max_val:
        raise ValueError(f"Must be <= {max_val}")
    return num

# 邮箱验证
def validate_email(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise ValueError("Invalid email format")
    return value

# URL 验证
def validate_url(value):
    from urllib.parse import urlparse
    try:
        result = urlparse(value)
        if result.scheme not in ('http', 'https'):
            raise ValueError("Only HTTP/HTTPS allowed")
        if not result.hostname:
            raise ValueError("Invalid URL")
        return value
    except Exception:
        raise ValueError("Invalid URL format")
```

### 2.3 长度与范围验证

```python
def validate_string(value, min_len=0, max_len=255):
    if not isinstance(value, str):
        raise ValueError("Must be a string")
    if len(value) < min_len:
        raise ValueError(f"Too short (min {min_len})")
    if len(value) > max_len:
        raise ValueError(f"Too long (max {max_len})")
    return value
```

## 3. 数据净化

### 3.1 HTML 净化

```python
import bleach

# 允许安全标签
clean_html = bleach.clean(
    user_input,
    tags=['b', 'i', 'u', 'a', 'p', 'br'],
    attributes={'a': ['href', 'title']},
    protocols=['https']
)
```

### 3.2 SQL 净化

```python
#  正确：参数化查询
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

#  错误：字符串拼接
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

### 3.3 OS 命令净化

```python
import shlex

# 安全引用
safe_arg = shlex.quote(user_input)
os.system(f"ping -c 3 {safe_arg}")
```

### 3.4 文件路径净化

```python
import os

def sanitize_path(base_dir, filename):
    # 移除路径遍历字符
    filename = os.path.basename(filename)
    # 规范化并验证
    full_path = os.path.normpath(os.path.join(base_dir, filename))
    if not full_path.startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid path")
    return full_path
```

## 4. 常见绕过技术

### 4.1 编码绕过

| 编码方式  | 示例                 | 绕过目标    |
| --------- | -------------------- | ----------- |
| URL 编码  | `%3Cscript%3E`       | `<script>`  |
| 双重编码  | `%253C`              | `%3C` → `<` |
| HTML 实体 | `&#60;script&#62;`   | `<script>`  |
| Unicode   | `\u003cscript\u003e` | `<script>`  |
| Base64    | `PHNjcmlwdD4=`       | `<script>`  |

### 4.2 大小写混合

```
<ScRiPt>alert(1)</ScRiPt>
SeLeCt * FrOm users
```

### 4.3 空字节注入

```
file.php%00.jpg   → 服务器截断为 file.php
<scr\x00ipt>      → 某些过滤器跳过空字节
```

### 4.4 换行注入

```
username=admin\nisAdmin=true
Header: value\r\nX-Injected: true
```

## 5. 框架级验证

### 5.1 Python（Pydantic）

```python
from pydantic import BaseModel, EmailStr, validator

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    age: int

    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', v):
            raise ValueError('Invalid username')
        return v

    @validator('age')
    def validate_age(cls, v):
        if not (0 < v < 150):
            raise ValueError('Invalid age')
        return v
```

### 5.2 JavaScript（Joi/Zod）

```javascript
import { z } from 'zod';

const UserSchema = z.object({
  username: z
    .string()
    .min(3)
    .max(20)
    .regex(/^[a-zA-Z0-9_]+$/),
  email: z.string().email(),
  age: z.number().int().min(1).max(149),
});
```

## 6. 验证最佳实践

| 实践        | 描述                 |
| ----------- | -------------------- |
| 前端验证    | 用户体验（不可依赖） |
| 后端验证    | 安全保障（必须）     |
| 数据库约束  | 最后一道防线         |
| 类型系统    | 编译时检查           |
| Schema 验证 | API 层统一验证       |
| 日志记录    | 记录验证失败事件     |

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
| 输入验证 | 026-InputValidation | 本文自身 |
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
