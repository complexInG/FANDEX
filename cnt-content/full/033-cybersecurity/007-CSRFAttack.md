---
order: 51
title: CSRF攻击
module: cybersecurity
category: 'eng-infra'
difficulty: intermediate
description: 跨站请求伪造攻击原理、攻击方式与防御机制详解。
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/XSS攻击
  - cybersecurity/安全模型与框架
  - cybersecurity/密码学应用
  - cybersecurity/SQL注入
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. CSRF 攻击原理

### 1.1 什么是 CSRF

跨站请求伪造（Cross-Site Request Forgery, CSRF）是一种利用用户已认证的身份，在用户不知情的情况下发起恶意请求的攻击方式。

### 1.2 攻击流程

```
1. 用户登录受信网站 A → 获得有效 Cookie/Session
2. 用户访问恶意网站 B → B 中包含对 A 的伪造请求
3. 浏览器自动携带 A 的 Cookie → A 服务器认为是合法请求
4. 攻击完成 → 用户账户执行了非预期操作
```

### 1.3 与 XSS 的区别

| 对比项           | CSRF             | XSS          |
| ---------------- | ---------------- | ------------ |
| 攻击目标         | 伪造用户请求     | 注入恶意脚本 |
| 是否需要脚本执行 | 不一定           | 必须         |
| 能否读取响应     | 不能（同源策略） | 能           |
| Cookie 可见性    | 不可见           | 可见         |
| 防御重点         | 请求来源验证     | 输入输出过滤 |

## 2. CSRF 攻击方式

### 2.1 GET 型 CSRF

最简单的攻击方式，通过图片标签或链接触发：

```html
<!-- 转账攻击 -->
<img src="https://bank.com/transfer?to=attacker&amount=10000" />

<!-- 修改密码 -->
<img src="https://example.com/changepwd?newpwd=hacked123" />

<!-- 诱导点击 -->
<a href="https://example.com/delete?id=1">点击领取奖品</a>
```

### 2.2 POST 型 CSRF

通过自动提交的表单发起 POST 请求：

```html
<form id="csrf-form" action="https://bank.com/transfer" method="POST">
  <input type="hidden" name="to" value="attacker" />
  <input type="hidden" name="amount" value="10000" />
</form>
<script>
  document.getElementById('csrf-form').submit();
</script>
```

### 2.3 AJAX 型 CSRF

利用 XMLHttpRequest 或 Fetch API：

```javascript
fetch('https://example.com/api/delete', {
  method: 'POST',
  credentials: 'include', // 携带 Cookie
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ id: 1 }),
});
```

> 注：当 `Content-Type` 为 `application/json` 时，浏览器会先发送 OPTIONS 预检请求（CORS），但某些服务器配置不当仍可能被利用。

### 2.4 JSON 型 CSRF

某些应用接受 `Content-Type: text/plain` 或表单格式的 JSON：

```html
<form action="https://api.example.com/action" method="POST" enctype="text/plain">
  <input type="hidden" name='{"action":"delete","id":' value='1,"ignore":"' />
</form>
```

## 3. CSRF 防御机制

### 3.1 CSRF Token

最主流的防御方式，服务器为每个会话/表单生成随机 Token：

**服务端生成**：

```python
# Flask 示例
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

# 模板中自动注入
# <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
```

**验证流程**：

```
1. 服务器生成随机 Token → 存入 Session
2. 表单中嵌入隐藏字段携带 Token
3. 提交时服务器验证 Token 是否匹配
4. 攻击者无法获取 Token → 伪造请求失败
```

### 3.2 SameSite Cookie

```http
Set-Cookie: session=abc123; SameSite=Strict
```

| 值       | 效果                                 |
| -------- | ------------------------------------ |
| `Strict` | 完全禁止跨站请求携带 Cookie          |
| `Lax`    | GET 导航请求允许，POST/iframe 等禁止 |
| `None`   | 允许跨站携带（需配合 `Secure`）      |

**推荐**：大多数场景使用 `SameSite=Lax`，兼顾安全与用户体验。

### 3.3 Referer / Origin 检查

```python
# 验证请求来源
def verify_origin(request):
    origin = request.headers.get('Origin')
    referer = request.headers.get('Referer')
    allowed = ['https://example.com']

    if origin and origin not in allowed:
        return False
    if referer and not any(referer.startswith(a) for a in allowed):
        return False
    return True
```

**局限性**：

- 隐私设置可能移除 Referer
- Origin 在 GET 请求中可能为空
- 子域名可能被绕过

### 3.4 双重 Cookie 验证

```
1. 服务器将 Token 写入 Cookie
2. 前端 JavaScript 读取 Cookie → 添加到请求头/参数
3. 服务器验证 Cookie 中的 Token 与请求中的 Token 一致
```

攻击者无法读取跨域 Cookie，因此无法在请求中附加该 Token。

### 3.5 自定义请求头

```javascript
// 前端添加自定义头
fetch('/api/action', {
  method: 'POST',
  headers: { 'X-Requested-With': 'XMLHttpRequest' },
});
```

由于 CORS 限制，跨域请求无法添加自定义头，因此 CSRF 攻击无法携带此头。

## 4. RESTful API 的 CSRF 防护

| 策略                | 适用场景                              |
| ------------------- | ------------------------------------- |
| Bearer Token（JWT） | SPA + API 架构，Token 存 localStorage |
| CSRF Token          | 传统表单提交                          |
| SameSite Cookie     | 所有场景的基础防护                    |
| Origin 检查         | API 网关层验证                        |

## 5. CSRF 攻击检测

### 5.1 自动化工具

| 工具                | 特点               |
| ------------------- | ------------------ |
| Burp Suite CSRF POC | 一键生成 CSRF PoC  |
| OWASP ZAP           | 自动化 CSRF 检测   |
| CSRF Tester         | 专用 CSRF 测试工具 |

### 5.2 手动测试要点

- 检查关键操作（转账、改密、删除）是否验证 CSRF Token
- 验证 Token 是否可预测或固定
- 检查是否验证 Referer/Origin
- 测试 SameSite Cookie 配置
- 检查 JSON API 是否仅依赖 Cookie 认证

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
| CSRF攻击 | 007-CSRFAttack | 本文自身 |
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
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文的并列主题 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
