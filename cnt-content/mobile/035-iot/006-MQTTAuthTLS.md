# 物联网 MQTT 认证与 TLS

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 用户名密码认证

**基本写法：发布带认证**
`mosquitto_pub -u <用户名> -P <密码> -t <主题> -m "<消息>"`
```bash
# 通过用户名密码连接 broker
mosquitto_pub -h broker.local -u iot-user -P mypass -t "test/topic" -m "Hi"
```

---

**基本写法：订阅带认证**
`mosquitto_sub -u <用户名> -P <密码> -t <主题>`
```bash
# 订阅时也需提供认证信息
mosquitto_sub -h broker.local -u iot-user -P mypass -t "test/topic"
```

---

**基本写法：配置文件存放认证**
`-o <配置文件>`
```bash
# 配置文件内容 -u iot-user -P mypass 避免命令行暴露
mosquitto_pub -o ~/.config/mosquitto_pub -t "test/topic" -m "Hi"
```

---

## 密码文件管理

**基本写法：创建密码文件**
`mosquitto_passwd -c <文件> <用户名>`
```bash
# 首次创建密码文件并添加用户
sudo mosquitto_passwd -c /etc/mosquitto/passwd iot-user
```

---

**基本写法：追加用户**
`mosquitto_passwd <文件> <用户名>`
```bash
# 向已有密码文件追加用户
sudo mosquitto_passwd /etc/mosquitto/passwd second-user
```

---

**基本写法：批量添加用户**
`mosquitto_passwd -b <文件> <用户名> <密码>`
```bash
# 命令行直接指定密码适合脚本
sudo mosquitto_passwd -b /etc/mosquitto/passwd user3 pass3
```

---

**基本写法：删除用户**
`mosquitto_passwd -D <文件> <用户名>`
```bash
# 从密码文件移除指定用户
sudo mosquitto_passwd -D /etc/mosquitto/passwd iot-user
```

---

**基本写法：使用 bcrypt 加密**
`mosquitto_passwd -b <文件> <用户名> <密码>`
```bash
# 默认使用 bcrypt 加密存储密码
sudo mosquitto_passwd -b /etc/mosquitto/passwd user1 mypassword
```

---

## Broker 认证配置

**基本写法：禁用匿名访问**
```
allow_anonymous false
```
```bash
# 强制所有连接必须认证
allow_anonymous false
```

---

**基本写法：指定密码文件**
```
password_file /etc/mosquitto/passwd
```
```bash
# 加载密码文件用于认证
password_file /etc/mosquitto/passwd
```

---

**基本写法：基于主题的访问控制**
```
user iot-user
topic readwrite sensor/#
topic read cmd/#
```
```bash
# 限制用户只能读写特定主题
user iot-user
topic readwrite sensor/#
topic read cmd/#
```

---

**基本写法：模式匹配访问控制**
```
pattern readwrite %u/#
```
```bash
# 用户只能访问自己用户名下的主题
pattern readwrite %u/#
```

---

**基本写法：默认匿名用户权限**
```
topic read $SYS/#
```
```bash
# 匿名用户仅能读取系统主题
topic read $SYS/#
```

---

## TLS 单向认证

**基本写法：指定 CA 证书**
`mosquitto_pub --cafile <CA 文件> -p 8883 -t <主题> -m "<消息>"`
```bash
# 客户端校验 broker 证书
mosquitto_pub --cafile ca.crt -h broker.local -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：指定 CA 证书目录**
`mosquitto_pub --capath <目录> -p 8883 -t <主题> -m "<消息>"`
```bash
# 通过目录加载多个 CA 证书
mosquitto_pub --capath /etc/ssl/certs -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：使用系统证书**
`mosquitto_pub -p 8883 -t <主题> -m "<消息>"`
```bash
# 端口 8883 自动加载系统证书
mosquitto_pub -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：禁用 TLS**
`mosquitto_pub --no-tls -t <主题> -m "<消息>"`
```bash
# 显式禁用 TLS 连接
mosquitto_pub --no-tls -t "test/topic" -m "Hi"
```

---

## TLS 双向认证

**基本写法：客户端证书认证**
`mosquitto_pub --cert <证书> --key <私钥> --cafile <CA> -p 8883 -t <主题> -m "<消息>"`
```bash
# 客户端提供证书供 broker 校验
mosquitto_pub --cert client.crt --key client.key --cafile ca.crt -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：证书与用户名组合**
`mosquitto_pub --cert <证书> --key <私钥> -u <用户名> -P <密码> -p 8883 -t <主题> -m "<消息>"`
```bash
# 双重认证证书加用户名密码
mosquitto_pub --cert client.crt --key client.key -u user -P pass -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：跳过主机名校验**
`mosquitto_pub --insecure --cafile <CA> -p 8883 -t <主题> -m "<消息>"`
```bash
# 仅测试环境跳过证书主机名校验
mosquitto_pub --insecure --cafile ca.crt -p 8883 -t "test/topic" -m "Hi"
```

---

## TLS-PSK 认证

**基本写法：使用 PSK 加密**
`mosquitto_pub --psk <十六进制密钥> --psk-identity <标识> -p 8883 -t <主题> -m "<消息>"`
```bash
# 使用预共享密钥认证无需证书
mosquitto_pub --psk 1234567890abcdef --psk-identity "client1" -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：指定 TLS 版本**
`mosquitto_pub --tls-version <版本> --cafile <CA> -p 8883 -t <主题> -m "<消息>"`
```bash
# 强制使用 TLS 1.2
mosquitto_pub --tls-version tlsv1.2 --cafile ca.crt -p 8883 -t "test/topic" -m "Hi"
```

---

**基本写法：指定加密套件**
`mosquitto_pub --ciphers <套件> --cafile <CA> -p 8883 -t <主题> -m "<消息>"`
```bash
# 限定加密套件
mosquitto_pub --ciphers "AES256-SHA" --cafile ca.crt -p 8883 -t "test/topic" -m "Hi"
```

---

## Broker TLS 配置

**基本写法：配置 TLS 监听**
```
listener 8883
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
cafile /etc/mosquitto/certs/ca.crt
require_certificate true
```
```bash
# 启用双向 TLS 认证
listener 8883
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
cafile /etc/mosquitto/certs/ca.crt
require_certificate true
```

---

**基本写法：配置 PSK**
```
listener 8883
psk_hint hint1
psk_file /etc/mosquitto/psk.db
```
```bash
# 启用 PSK 认证模式
listener 8883
psk_hint hint1
psk_file /etc/mosquitto/psk.db
```

---

## WebSocket 配置

**基本写法：启用 WebSocket 监听**
```
listener 9001
protocol websockets
```
```bash
# 让浏览器通过 WebSocket 连接
listener 9001
protocol websockets
```

---

**基本写法：WebSocket over TLS**
```
listener 9443
protocol websockets
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
```
```bash
# 加密的 WebSocket 连接
listener 9443
protocol websockets
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
```
