# Cybersecurity 证书验证与调试

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## SSL/TLS 连接测试

**基本写法：测试 HTTPS 连接**
`openssl s_client -connect <主机>:<端口>`
```bash
# 测试 HTTPS 连接
openssl s_client -connect example.com:443
```

**基本写法：指定 SNI**
`openssl s_client -connect <主机>:<端口> -servername <域名>`
```bash
# 指定 SNI 测试虚拟主机
openssl s_client -connect example.com:443 -servername example.com
```

**基本写法：查看证书链**
`openssl s_client -showcerts -connect <主机>:<端口>`
```bash
# 查看完整证书链
openssl s_client -showcerts -connect example.com:443
```

**基本写法：静默模式测试**
`echo | openssl s_client -connect <主机>:443 2>/dev/null`
```bash
# 静默测试不阻塞
echo | openssl s_client -connect example.com:443 2>/dev/null
```

**基本写法：测试 SMTP TLS**
`openssl s_client -starttls smtp -connect <主机>:<端口>`
```bash
# 测试 SMTP 服务的 STARTTLS
openssl s_client -starttls smtp -connect smtp.example.com:587
```

---

## TLS 版本测试

**基本写法：测试 TLS 1.2**
`openssl s_client -tls1_2 -connect <主机>:<端口>`
```bash
# 测试服务器是否支持 TLS 1.2
openssl s_client -tls1_2 -connect example.com:443
```

**基本写法：测试 TLS 1.3**
`openssl s_client -tls1_3 -connect <主机>:<端口>`
```bash
# 测试服务器是否支持 TLS 1.3
openssl s_client -tls1_3 -connect example.com:443
```

**基本写法：禁用旧版本**
`openssl s_client -no_ssl3 -no_tls1 -no_tls1_1 -connect <主机>:<端口>`
```bash
# 禁用 SSL3、TLS1.0、TLS1.1
openssl s_client -no_ssl3 -no_tls1 -no_tls1_1 -connect example.com:443
```

**基本写法：查看协商的 TLS 版本**
`openssl s_client -connect <主机>:443 </dev/null 2>&1 | grep Protocol`
```bash
# 查看实际协商的 TLS 版本
openssl s_client -connect example.com:443 </dev/null 2>&1 | grep Protocol
```

---

## 密码套件测试

**基本写法：查看支持的密码套件**
`openssl ciphers -v`
```bash
# 列出所有支持的密码套件
openssl ciphers -v
```

**基本写法：测试特定密码套件**
`openssl s_client -cipher <密码套件> -connect <主机>:<端口>`
```bash
# 测试服务器是否支持特定密码套件
openssl s_client -cipher 'ECDHE-RSA-AES256-GCM-SHA384' -connect example.com:443
```

**基本写法：只使用强密码套件**
`openssl s_client -cipher 'HIGH:!aNULL:!MD5' -connect <主机>:<端口>`
```bash
# 只使用高强度密码套件
openssl s_client -cipher 'HIGH:!aNULL:!MD5:!RC4' -connect example.com:443
```

**基本写法：查看协商的密码套件**
`openssl s_client -connect <主机>:443 </dev/null 2>&1 | grep Cipher`
```bash
# 查看实际协商的密码套件
openssl s_client -connect example.com:443 </dev/null 2>&1 | grep Cipher
```

---

## 证书验证

**基本写法：验证证书链**
`openssl verify -CAfile <CA证书> <证书>`
```bash
# 验证证书是否有效
openssl verify -CAfile ca.crt server.crt
```

**基本写法：验证证书链含中间证书**
`openssl verify -CAfile <CA证书> -untrusted <中间证书> <证书>`
```bash
# 使用中间证书验证
openssl verify -CAfile root.crt -untrusted intermediate.crt server.crt
```

**基本写法：使用系统 CA 验证**
`openssl verify <证书>`
```bash
# 使用系统信任的 CA 验证证书
openssl verify server.crt
```

**基本写法：在线验证证书**
`openssl s_client -connect <主机>:443 -verify_return_error`
```bash
# 连接时验证证书有效性
openssl s_client -connect example.com:443 -verify_return_error
```

---

## 证书信息提取

**基本写法：查看证书过期时间**
`openssl x509 -enddate -noout -in <证书>`
```bash
# 查看证书过期日期
openssl x509 -enddate -noout -in cert.pem
```

**基本写法：从远程服务器获取过期时间**
`echo | openssl s_client -connect <主机>:443 2>/dev/null | openssl x509 -noout -enddate`
```bash
# 查看远程服务器证书过期时间
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -enddate
```

**基本写法：查看证书主题**
`openssl x509 -subject -noout -in <证书>`
```bash
# 查看证书主题
openssl x509 -subject -noout -in cert.pem
```

**基本写法：查看证书颁发者**
`openssl x509 -issuer -noout -in <证书>`
```bash
# 查看证书颁发者
openssl x509 -issuer -noout -in cert.pem
```

**基本写法：查看证书 SAN**
`openssl x509 -text -noout -in <证书> | grep -A1 "Subject Alternative Name"`
```bash
# 查看证书的 Subject Alternative Names
openssl x509 -text -noout -in cert.pem | grep -A1 "Subject Alternative Name"
```

---

## 证书匹配验证

**基本写法：验证证书和私钥匹配**
`openssl x509 -noout -modulus -in <证书> | openssl md5; openssl rsa -noout -modulus -in <私钥> | openssl md5`
```bash
# 对比证书和私钥的 modulus 是否一致
openssl x509 -noout -modulus -in cert.pem | openssl md5
openssl rsa -noout -modulus -in private.key | openssl md5
```

**基本写法：验证 CSR 和私钥匹配**
`openssl req -noout -modulus -in <CSR> | openssl md5; openssl rsa -noout -modulus -in <私钥> | openssl md5`
```bash
# 对比 CSR 和私钥的 modulus
openssl req -noout -modulus -in request.csr | openssl md5
openssl rsa -noout -modulus -in private.key | openssl md5
```

**基本写法：一键验证匹配**
`[ "$(openssl x509 -noout -modulus -in cert.pem | openssl md5)" = "$(openssl rsa -noout -modulus -in private.key | openssl md5)" ] && echo "匹配" || echo "不匹配"`
```bash
# 一键检查证书和私钥是否匹配
[ "$(openssl x509 -noout -modulus -in cert.pem | openssl md5)" = "$(openssl rsa -noout -modulus -in private.key | openssl md5)" ] && echo "匹配" || echo "不匹配"
```

---

## 证书下载与导出

**基本写法：下载服务器证书**
`echo | openssl s_client -connect <主机>:443 2>/dev/null | openssl x509 -out <文件>`
```bash
# 下载远程服务器证书
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -out cert.pem
```

**基本写法：下载完整证书链**
`openssl s_client -showcerts -connect <主机>:443 </dev/null 2>/dev/null | openssl x509 -out <文件>`
```bash
# 下载完整证书链
openssl s_client -showcerts -connect example.com:443 </dev/null 2>/dev/null | awk '/-----BEGIN/,/-----END/{print}' > chain.pem
```

**基本写法：从 PFX 导出证书和私钥**
`openssl pkcs12 -in <PFX> -clcerts -nokeys -out <证书>; openssl pkcs12 -in <PFX> -nocerts -nodes -out <私钥>`
```bash
# 从 PFX 文件分别导出证书和私钥
openssl pkcs12 -in cert.pfx -clcerts -nokeys -out cert.pem
openssl pkcs12 -in cert.pfx -nocerts -nodes -out private.key
```

---

## 证书过期监控

**基本写法：检查证书剩余天数**
`openssl x509 -enddate -noout -in <证书> | cut -d= -f2`
```bash
# 查看证书过期日期
openssl x509 -enddate -noout -in cert.pem | cut -d= -f2
```

**基本写法：计算剩余天数**
```bash
`expiry=$(echo | openssl s_client -connect <主机>:443 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)
days=$(( ( $(date -d "$expiry" +%s) - $(date +%s) ) / 86400 ))
echo "剩余 $days 天"`
```
```bash
# 计算远程证书剩余有效天数
expiry=$(echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -enddate | cut -d= -f2)
days=$(( ( $(date -d "$expiry" +%s) - $(date +%s) ) / 86400 ))
echo "证书剩余 $days 天"
```

**基本写法：批量检查证书过期**
`for f in *.pem; do echo "$f: $(openssl x509 -enddate -noout -in $f | cut -d= -f2)"; done`
```bash
# 批量检查所有证书的过期时间
for f in *.pem; do echo "$f: $(openssl x509 -enddate -noout -in $f | cut -d= -f2)"; done
```

---

## 证书调试

**基本写法：查看证书完整信息**
`openssl x509 -text -noout -in <证书>`
```bash
# 查看证书完整详细信息
openssl x509 -text -noout -in cert.pem
```

**基本写法：查看证书序列号**
`openssl x509 -serial -noout -in <证书>`
```bash
# 查看证书序列号
openssl x509 -serial -noout -in cert.pem
```

**基本写法：查看证书指纹**
`openssl x509 -fingerprint -sha256 -noout -in <证书>`
```bash
# 查看 SHA256 指纹
openssl x509 -fingerprint -sha256 -noout -in cert.pem
```

**基本写法：查看公钥信息**
`openssl x509 -pubkey -noout -in <证书> | openssl rsa -pubin -text -noout`
```bash
# 查看证书中的公钥信息
openssl x509 -pubkey -noout -in cert.pem | openssl rsa -pubin -text -noout
```

---

## nmap SSL 扫描

**基本写法：枚举 SSL 密码套件**
`nmap --script ssl-enum-ciphers -p 443 <主机>`
```bash
# 使用 nmap 枚举 SSL 支持的密码套件
nmap --script ssl-enum-ciphers -p 443 example.com
```

**基本写法：检测 SSL 漏洞**
`nmap --script ssl-* -p 443 <主机>`
```bash
# 运行所有 SSL 相关脚本
nmap --script ssl-* -p 443 example.com
```

**基本写法：获取 SSL 证书**
`nmap --script ssl-cert -p 443 <主机>`
```bash
# 使用 nmap 获取 SSL 证书信息
nmap --script ssl-cert -p 443 example.com
```

---

## 证书吊销检查

**基本写法：检查 OCSP 状态**
`openssl ocsp -issuer <CA证书> -cert <证书> -url <OCSP URL> -no_nonce`
```bash
# 检查证书的 OCSP 吊销状态
openssl ocsp -issuer ca.crt -cert server.crt -url http://ocsp.example.com -no_nonce
```

**基本写法：从证书提取 OCSP URL**
`openssl x509 -text -noout -in <证书> | grep "OCSP"`
```bash
# 提取证书中的 OCSP URL
openssl x509 -text -noout -in cert.pem | grep "OCSP - URI"
```

**基本写法：检查 CRL**
`openssl crl -text -noout -in <CRL文件>`
```bash
# 查看证书吊销列表内容
openssl crl -text -noout -in crl.pem
```
