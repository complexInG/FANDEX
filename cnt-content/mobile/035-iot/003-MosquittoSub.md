# 物联网 mosquitto_sub 订阅命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本订阅

**基本写法：订阅单个主题**
`mosquitto_sub -h <主机> -t <主题>`
```bash
# 订阅本地 broker 的 test/topic
mosquitto_sub -h localhost -t "test/topic"
```

---

**基本写法：订阅多个主题**
`mosquitto_sub -t <主题1> -t <主题2>`
```bash
# 同时订阅两个主题
mosquitto_sub -t "home/temp" -t "home/humidity"
```

---

**基本写法：订阅所有主题**
`mosquitto_sub -t '#'`
```bash
# 使用通配符订阅所有消息
mosquitto_sub -h localhost -t '#'
```

---

**基本写法：指定端口**
`mosquitto_sub -h <主机> -p <端口> -t <主题>`
```bash
# 连接非默认端口 1884
mosquitto_sub -h localhost -p 1884 -t "test/topic"
```

---

**基本写法：使用 URL 形式**
`mosquitto_sub -L mqtt://<主机>:<端口>/<主题>`
```bash
# 通过 URL 形式订阅
mosquitto_sub -L mqtt://localhost:1883/test/topic
```

---

## 输出格式

**基本写法：详细输出**
`mosquitto_sub -v -t <主题>`
```bash
# 输出主题名与消息内容
mosquitto_sub -v -t "test/topic"
```

---

**基本写法：调试模式**
`mosquitto_sub -d -t <主题>`
```bash
# 打印连接订阅详细调试信息
mosquitto_sub -d -h localhost -t "test/topic"
```

---

**基本写法：静默模式**
`mosquitto_sub --quiet -t <主题>`
```bash
# 仅输出消息内容不输出错误
mosquitto_sub --quiet -t "test/topic"
```

---

## QoS 控制

**基本写法：指定订阅 QoS**
`mosquitto_sub -q <0|1|2> -t <主题>`
```bash
# 以 QoS 1 订阅确保至少一次接收
mosquitto_sub -q 1 -t "test/topic"
```

---

**基本写法：禁用 clean session**
`mosquitto_sub -c -i <客户端ID> -t <主题>`
```bash
# 持久会话断线重连后接收离线消息
mosquitto_sub -c -i "sub-001" -t "test/topic"
```

---

## 客户端身份

**基本写法：指定客户端 ID**
`mosquitto_sub -i <客户端ID> -t <主题>`
```bash
# 设置固定客户端 ID
mosquitto_sub -i "monitor-001" -t "sensor/data"
```

---

**基本写法：客户端 ID 前缀**
`mosquitto_sub -I <前缀> -t <主题>`
```bash
# 使用前缀自动追加进程 ID
mosquitto_sub -I "sub-" -t "test/topic"
```

---

**基本写法：设置心跳**
`mosquitto_sub -k <秒> -t <主题>`
```bash
# 每 60 秒发送一次心跳
mosquitto_sub -k 60 -t "test/topic"
```

---

## 认证

**基本写法：用户名密码认证**
`mosquitto_sub -h <主机> -u <用户名> -P <密码> -t <主题>`
```bash
# 通过用户名密码连接
mosquitto_sub -h localhost -u iot-user -P mypass -t "test/topic"
```

---

**基本写法：使用配置文件**
`mosquitto_sub -o <配置文件> -t <主题>`
```bash
# 从配置文件加载认证信息
mosquitto_sub -o ~/.config/mosquitto_sub -t "test/topic"
```

---

## 遗嘱消息

**基本写法：设置订阅者遗嘱**
`mosquitto_sub --will-topic <主题> --will-payload "<消息>" -t <订阅主题>`
```bash
# 订阅者异常断开时发布遗嘱
mosquitto_sub --will-topic "status/sub" --will-payload "offline" -t "test/topic"
```

---

**基本写法：遗嘱 QoS 与 retain**
`mosquitto_sub --will-topic <主题> --will-payload "<消息>" --will-qos <0|1|2> --will-retain -t <订阅主题>`
```bash
# 遗嘱消息保留且 QoS 1
mosquitto_sub --will-topic "status/sub" --will-payload "offline" --will-qos 1 --will-retain -t "test/topic"
```

---

## 通配符订阅

**基本写法：单层通配符**
`mosquitto_sub -t "<前缀>/+"`
```bash
# 订阅 home/ 下任意单层主题
mosquitto_sub -t "home/+"
```

---

**基本写法：多层通配符**
`mosquitto_sub -t "<前缀>/#"`
```bash
# 订阅 home/ 下所有层级主题
mosquitto_sub -t "home/#"
```

---

**基本写法：组合通配符**
`mosquitto_sub -t "+/sensor/#"`
```bash
# 订阅任意楼层 sensor 下所有主题
mosquitto_sub -t "+/sensor/#"
```

---

## 协议与 TLS

**基本写法：使用 MQTT 5.0**
`mosquitto_sub -V mqtt5 -t <主题>`
```bash
# 使用 MQTT 5.0 协议订阅
mosquitto_sub -V mqtt5 -t "test/topic"
```

---

**基本写法：TLS 加密连接**
`mosquitto_sub -p 8883 --cafile <CA 文件> -t <主题>`
```bash
# 通过 TLS 安全连接 broker
mosquitto_sub -h broker.example.com -p 8883 --cafile /etc/ssl/certs/ca-certificates.crt -t "test/topic"
```

---

**基本写法：客户端证书认证**
`mosquitto_sub --cert <证书> --key <私钥> -t <主题>`
```bash
# 使用客户端证书双向认证
mosquitto_sub -p 8883 --cert client.crt --key client.key --cafile ca.crt -t "test/topic"
```

---

**基本写法：跳过证书校验**
`mosquitto_sub --insecure -t <主题>`
```bash
# 仅测试环境跳过主机名校验
mosquitto_sub --insecure -p 8883 --cafile ca.crt -t "test/topic"
```

---

## 退出控制

**基本写法：收到 N 条消息后退出**
`mosquitto_sub -C <次数> -t <主题>`
```bash
# 收到 5 条消息后自动退出
mosquitto_sub -C 5 -t "test/topic"
```

---

**基本写法：等待 N 秒后退出**
`mosquitto_sub -W <秒> -t <主题>`
```bash
# 订阅 30 秒后自动退出
mosquitto_sub -W 30 -t "test/topic"
```

---

**基本写法：退出码控制**
`mosquitto_sub -E -t <主题>`
```bash
# 第一条消息后退出并返回成功
mosquitto_sub -E -t "test/topic"
```
