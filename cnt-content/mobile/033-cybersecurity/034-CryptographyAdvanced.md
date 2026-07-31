# Cybersecurity 高级密码学命令

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 对称加密

**基本写法:AES 加密文件**
`openssl enc -aes-256-cbc -salt -in <文件> -out <输出>`
```bash
# 使用 AES-256-CBC 加密文件
openssl enc -aes-256-cbc -salt -in secret.txt -out secret.enc
```

**基本写法:AES 解密文件**
`openssl enc -aes-256-cbc -d -in <文件> -out <输出>`
```bash
# 解密 AES 加密的文件
openssl enc -aes-256-cbc -d -in secret.enc -out secret.txt
```

**基本写法:使用密码加密**
`openssl enc -aes-256-cbc -salt -pass pass:<密码> -in <文件> -out <输出>`
```bash
# 通过命令行密码加密
openssl enc -aes-256-cbc -salt -pass pass:mypassword -in secret.txt -out secret.enc
```

**基本写法:使用密钥文件加密**
`openssl enc -aes-256-cbc -salt -pass file:<密钥文件> -in <文件> -out <输出>`
```bash
# 使用密钥文件加密
openssl enc -aes-256-cbc -salt -pass file:key.txt -in secret.txt -out secret.enc
```

**基本写法:GPG 对称加密**
`gpg -c <文件>`
```bash
# 使用 GPG 对称加密文件
gpg -c secret.txt
```

---

## 非对称加密

**基本写法:生成 RSA 密钥对**
`openssl genrsa -out <私钥文件> <位数>`
```bash
# 生成 4096 位 RSA 私钥
openssl genrsa -out private.key 4096
```

**基本写法:提取公钥**
`openssl rsa -in <私钥> -pubout -out <公钥文件>`
```bash
# 从私钥提取公钥
openssl rsa -in private.key -pubout -out public.key
```

**基本写法:RSA 加密文件**
`openssl rsautl -encrypt -inkey <公钥> -pubin -in <文件> -out <输出>`
```bash
# 使用公钥加密文件
openssl rsautl -encrypt -inkey public.key -pubin -in secret.txt -out secret.enc
```

**基本写法:RSA 解密文件**
`openssl rsautl -decrypt -inkey <私钥> -in <文件> -out <输出>`
```bash
# 使用私钥解密文件
openssl rsautl -decrypt -inkey private.key -in secret.enc -out secret.txt
```

**基本写法:生成 ECC 密钥**
`openssl ecparam -name <曲线> -genkey -out <密钥文件>`
```bash
# 生成 ECC 密钥对
openssl ecparam -name prime256v1 -genkey -out ecc.key
```

---

## 数字签名

**基本写法:生成文件签名**
`openssl dgst -sha256 -sign <私钥> -out <签名文件> <文件>`
```bash
# 使用私钥对文件生成签名
openssl dgst -sha256 -sign private.key -out signature.sig secret.txt
```

**基本写法:验证签名**
`openssl dgst -sha256 -verify <公钥> -signature <签名> <文件>`
```bash
# 验证文件签名是否有效
openssl dgst -sha256 -verify public.key -signature signature.sig secret.txt
```

**基本写法:GPG 签名文件**
`gpg --sign <文件>`
```bash
# 使用 GPG 签名文件
gpg --sign secret.txt
```

**基本写法:GPG 清晰签名**
`gpg --clearsign <文件>`
```bash
# 生成 ASCII 文本签名
gpg --clearsign message.txt
```

**基本写法:验证 GPG 签名**
`gpg --verify <签名文件> <原文件>`
```bash
# 验证 GPG 签名
gpg --verify secret.txt.gpg secret.txt
```

---

## 密钥交换

**基本写法:生成 Diffie-Hellman 参数**
`openssl dhparam -out <参数文件> <位数>`
```bash
# 生成 2048 位 DH 参数
openssl dhparam -out dhparam.pem 2048
```

**基本写法:查看 DH 参数**
`openssl dhparam -in <参数文件> -text -noout`
```bash
# 查看 DH 参数详情
openssl dhparam -in dhparam.pem -text -noout
```

**基本写法:生成 EC 参数**
`openssl ecparam -name <曲线> -out <参数文件>`
```bash
# 生成 EC 曲线参数
openssl ecparam -name prime256v1 -out ecparam.pem
```

**基本写法:列出支持的曲线**
`openssl ecparam -list_curves`
```bash
# 列出所有支持的椭圆曲线
openssl ecparam -list_curves
```

**基本写法:生成密钥派生**
`openssl kdf -keylen <长度> -kdfopt digest:sha256 -kdfopt pass:<密码> -kdfopt salt:<盐> PBKDF2`
```bash
# 使用 PBKDF2 派生密钥
openssl kdf -keylen 32 -kdfopt digest:sha256 -kdfopt pass:password -kdfopt salt:salt PBKDF2
```

---

## 证书管理

**基本写法:生成自签名证书**
`openssl req -x509 -newkey rsa:4096 -keyout <私钥> -out <证书> -days <天数> -nodes`
```bash
# 生成自签名证书有效期 1 年
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

**基本写法:生成 CSR**
`openssl req -new -key <私钥> -out <CSR文件>`
```bash
# 生成证书签名请求
openssl req -new -key private.key -out request.csr -subj "/CN=example.com"
```

**基本写法:查看 CSR 信息**
`openssl req -in <CSR> -text -noout`
```bash
# 查看 CSR 详细信息
openssl req -in request.csr -text -noout
```

**基本写法:使用 CA 签发证书**
`openssl x509 -req -in <CSR> -CA <CA证书> -CAkey <CA私钥> -CAcreateserial -out <证书> -days <天数>`
```bash
# 使用 CA 证书签发客户端证书
openssl x509 -req -in request.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365
```

**基本写法:转换为 PKCS12**
`openssl pkcs12 -export -out <PFX文件> -inkey <私钥> -in <证书>`
```bash
# 转换为 PKCS12 格式
openssl pkcs12 -export -out cert.pfx -inkey private.key -in cert.pem
```

---

## 密码哈希

**基本写法:生成 SHA256 哈希**
`echo -n "<字符串>" | sha256sum`
```bash
# 计算字符串 SHA256 哈希
echo -n "hello" | sha256sum
```

**基本写法:计算文件哈希**
`sha256sum <文件>`
```bash
# 计算文件 SHA256 哈希
sha256sum file.txt
```

**基本写法:计算 SHA512**
`echo -n "<字符串>" | sha512sum`
```bash
# 计算 SHA512 哈希
echo -n "hello" | sha512sum
```

**基本写法:计算 HMAC**
`echo -n "<消息>" | openssl dgst -sha256 -hmac "<密钥>"`
```bash
# 计算 HMAC-SHA256
echo -n "message" | openssl dgst -sha256 -hmac "secretkey"
```

**基本写法:bcrypt 密码哈希**
`python3 -c "import bcrypt; print(bcrypt.hashpw(b'<密码>', bcrypt.gensalt()).decode())"`
```bash
# 使用 bcrypt 生成密码哈希
python3 -c "import bcrypt; print(bcrypt.hashpw(b'mypassword', bcrypt.gensalt()).decode())"
```

---

## 密码学随机数

**基本写法:生成随机字节**
`openssl rand -hex <字节数>`
```bash
# 生成 32 字节随机数
openssl rand -hex 32
```

**基本写法:生成 Base64 随机**
`openssl rand -base64 <字节数>`
```bash
# 生成 Base64 编码随机数
openssl rand -base64 32
```

**基本写法:从 /dev/urandom 读取**
`head -c <字节数> /dev/urandom | xxd -p`
```bash
# 从 urandom 读取随机字节
head -c 32 /dev/urandom | xxd -p
```

**基本写法:Python 生成随机数**
`python3 -c "import secrets; print(secrets.token_hex(32))"`
```bash
# 使用 secrets 模块生成安全随机数
python3 -c "import secrets; print(secrets.token_hex(32))"
```

**基本写法:生成 UUID**
`python3 -c "import uuid; print(uuid.uuid4())"`
```bash
# 生成 UUID v4
python3 -c "import uuid; print(uuid.uuid4())"
```

---

## PGP/GPG 操作

**基本写法:生成 GPG 密钥对**
`gpg --gen-key`
```bash
# 生成 GPG 密钥对
gpg --full-generate-key
```

**基本写法:列出密钥**
`gpg --list-keys`
```bash
# 列出所有 GPG 公钥
gpg --list-keys
```

**基本写法:列出私钥**
`gpg --list-secret-keys`
```bash
# 列出所有 GPG 私钥
gpg --list-secret-keys
```

**基本写法:导出公钥**
`gpg --export -a <用户> > <文件>`
```bash
# 导出 ASCII 格式公钥
gpg --export -a user@example.com > public.asc
```

**基本写法:导入公钥**
`gpg --import <文件>`
```bash
# 导入他人公钥
gpg --import public.asc
```

**基本写法:加密给他人**
`gpg -e -r <收件人> <文件>`
```bash
# 使用收件人公钥加密文件
gpg -e -r recipient@example.com secret.txt
```

---

## 编码与解码

**基本写法:Base32 编码**
`echo -n "<字符串>" | base32`
```bash
# Base32 编码字符串
echo -n "hello" | base32
```

**基本写法:Base58 编码**
`python3 -c "import base58; print(base58.b58encode(b'<字符串>').decode())"`
```bash
# Base58 编码
python3 -c "import base58; print(base58.b58encode(b'hello').decode())"
```

**基本写法:Hex 编码**
`echo -n "<字符串>" | xxd -p`
```bash
# 十六进制编码
echo -n "hello" | xxd -p
```

**基本写法:URL 安全 Base64**
`python3 -c "import base64; print(base64.urlsafe_b64encode(b'<字符串>').decode())"`
```bash
# URL 安全的 Base64 编码
python3 -c "import base64; print(base64.urlsafe_b64encode(b'hello?world').decode())"
```

**基本写法:Morse 编码**
`python3 -c "morse={'.':'E'}; print(''.join(morse.get(c, c) for c in '.... . .-.. .-.. ---'))"`
```bash
# 简单 Morse 解码示例
python3 -c "print('.... . .-.. .-.. ---'.replace('.','').replace(' ',''))"
```

---

## 密码破解

**基本写法:破解哈希(Hashcat)**
`hashcat -m <类型> <哈希文件> <字典>`
```bash
# 破解 SHA256 哈希(类型 1400)
hashcat -m 1400 hash.txt rockyou.txt
```

**基本写法:使用规则破解**
`hashcat -m <类型> <哈希> <字典> -r <规则文件>`
```bash
# 使用规则文件扩展字典
hashcat -m 0 hash.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**基本写法:掩码破解**
`hashcat -m <类型> <哈希> -a 3 <掩码>`
```bash
# 暴力破解 8 位数字密码
hashcat -m 0 hash.txt -a 3 '?d?d?d?d?d?d?d?d'
```

**基本写法:破解哈希(John)**
`john --wordlist=<字典> --format=<格式> <哈希文件>`
```bash
# 破解 MD5 哈希
john --wordlist=rockyou.txt --format=raw-md5 hash.txt
```

**基本写法:显示破解结果**
`john --show <哈希文件>`
```bash
# 显示已破解的密码
john --show hash.txt
```

---

## 加密通信

**基本写法:使用 nc 传输加密**
`nc -l <端口> | openssl enc -d -aes-256-cbc`
```bash
# 接收并解密数据
nc -l 4444 | openssl enc -d -aes-256-cbc > received.txt
```

**基本写法:发送加密数据**
`openssl enc -aes-256-cbc -in <文件> | nc <目标> <端口>`
```bash
# 加密并发送数据
openssl enc -aes-256-cbc -in secret.txt | nc 192.168.1.5 4444
```

**基本写法:使用 stunnel 加密隧道**
`stunnel <配置文件>`
```bash
# 启动 stunnel 加密隧道
stunnel /etc/stunnel/stunnel.conf
```

**基本写法:SSH 加密文件传输**
`scp -i <密钥> <文件> <用户>@<主机>:<路径>`
```bash
# 使用 SSH 加密传输文件
scp -i id_rsa secret.txt user@example.com:/tmp/
```

**基本写法:使用 openssl 加密备份**
`tar czf - <目录> | openssl enc -aes-256-cbc -salt -out <备份文件>`
```bash
# 加密备份整个目录
tar czf - /important | openssl enc -aes-256-cbc -salt -out backup.tar.enc
```
