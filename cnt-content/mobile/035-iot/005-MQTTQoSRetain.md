# 物联网 MQTT QoS 与 Retained

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## QoS 0 至多一次

**基本写法：QoS 0 发布**
`mosquitto_pub -q 0 -t <主题> -m "<消息>"`
```bash
# 发送即忘不保证送达适合高频遥测
mosquitto_pub -q 0 -t "sensor/temp" -m "23.5"
```

---

**基本写法：QoS 0 订阅**
`mosquitto_sub -q 0 -t <主题>`
```bash
# 订阅者以 QoS 0 接收消息
mosquitto_sub -q 0 -t "sensor/temp"
```

---

## QoS 1 至少一次

**基本写法：QoS 1 发布**
`mosquitto_pub -q 1 -t <主题> -m "<消息>"`
```bash
# 保证送达可能重复适合控制命令
mosquitto_pub -q 1 -t "cmd/light" -m "on"
```

---

**基本写法：QoS 1 订阅**
`mosquitto_sub -q 1 -t <主题>`
```bash
# 订阅者以 QoS 1 接收离线消息需配合 -c
mosquitto_sub -q 1 -c -i "sub-001" -t "cmd/light"
```

---

## QoS 2 恰好一次

**基本写法：QoS 2 发布**
`mosquitto_pub -q 2 -t <主题> -m "<消息>"`
```bash
# 严格一次开销最大适合计费场景
mosquitto_pub -q 2 -t "billing/charge" -m "100"
```

---

**基本写法：QoS 2 订阅**
`mosquitto_sub -q 2 -t <主题>`
```bash
# 订阅者以 QoS 2 接收确保不重复
mosquitto_sub -q 2 -t "billing/charge"
```

---

## QoS 握手协议

**基本写法：PUBACK 应答**
`QoS 1 流程: PUBLISH -> PUBACK`
```bash
# QoS 1 broker 收到后回复 PUBACK
QoS 1: PUBLISH -> PUBACK
```

---

**基本写法：QoS 2 四次握手**
`QoS 2 流程: PUBLISH -> PUBREC -> PUBREL -> PUBCOMP`
```bash
# QoS 2 通过四步握手确保恰好一次
QoS 2: PUBLISH -> PUBREC -> PUBREL -> PUBCOMP
```

---

## Retained 消息

**基本写法：发布 retained 消息**
`mosquitto_pub -r -t <主题> -m "<消息>"`
```bash
# 发布保留消息新订阅者立即收到
mosquitto_pub -r -t "device/status" -m "online"
```

---

**基本写法：retained 携带 QoS**
`mosquitto_pub -r -q <0|1|2> -t <主题> -m "<消息>"`
```bash
# 保留消息并指定 QoS 1
mosquitto_pub -r -q 1 -t "device/status" -m "online"
```

---

**基本写法：查看 retained 消息**
`mosquitto_sub -C 1 -t <主题>`
```bash
# 订阅后立即收到一条 retained 后退出
mosquitto_sub -C 1 -t "device/status"
```

---

**基本写法：清除 retained 消息**
`mosquitto_pub -n -r -t <主题>`
```bash
# 发送空消息清除该主题的 retained
mosquitto_pub -n -r -t "device/status"
```

---

**基本写法：retained 与通配符**
`mosquitto_sub -t "<前缀>/+"`
```bash
# 订阅时收到匹配主题的最近一条 retained
mosquitto_sub -t "device/+"
```

---

## 持久会话

**基本写法：客户端启用持久会话**
`mosquitto_sub -c -i <客户端ID> -t <主题>`
```bash
# 断线重连后接收离线期间 QoS>=1 消息
mosquitto_sub -c -i "persist-sub" -t "cmd/light"
```

---

**基本写法：发布者持久会话**
`mosquitto_pub -c -i <客户端ID> -t <主题> -m "<消息>"`
```bash
# 发布者保持会话状态
mosquitto_pub -c -i "persist-pub" -t "cmd/light" -m "on"
```

---

**基本写法：MQTT 5 会话过期间隔**
`mosquitto_pub -V mqtt5 -x <秒> -t <主题> -m "<消息>"`
```bash
# 设置会话 3600 秒后过期
mosquitto_pub -V mqtt5 -x 3600 -t "cmd/light" -m "on"
```

---

## 消息属性

**基本写法：MQTT 5 消息过期间隔**
`mosquitto_pub -V mqtt5 -D PUBLISH MessageExpiryInterval <秒> -t <主题> -m "<消息>"`
```bash
# 设置消息 60 秒后过期不投递
mosquitto_pub -V mqtt5 -D PUBLISH MessageExpiryInterval 60 -t "cmd/light" -m "on"
```

---

**基本写法：MQTT 5 内容类型**
`mosquitto_pub -V mqtt5 -D PUBLISH ContentType <类型> -t <主题> -m "<消息>"`
```bash
# 标记消息内容为 JSON
mosquitto_pub -V mqtt5 -D PUBLISH ContentType "application/json" -t "data" -m '{"t":23.5}'
```

---

**基本写法：MQTT 5 响应主题**
`mosquitto_pub -V mqtt5 -D PUBLISH ResponseTopic <主题> -t <请求主题> -m "<消息>"`
```bash
# 请求响应模式指定响应主题
mosquitto_pub -V mqtt5 -D PUBLISH ResponseTopic "resp/001" -t "req/service" -m "ping"
```

---

## QoS 选择策略

**基本写法：遥测数据用 QoS 0**
`mosquitto_pub -q 0 -t "telemetry/<device>" -m "<数据>"`
```bash
# 高频温度遥测允许少量丢失
mosquitto_pub -q 0 -t "telemetry/sensor-001" -m "23.5"
```

---

**基本写法：控制命令用 QoS 1**
`mosquitto_pub -q 1 -t "cmd/<device>" -m "<命令>"`
```bash
# 灯控命令需确保送达
mosquitto_pub -q 1 -t "cmd/light-001" -m "toggle"
```

---

**基本写法：计费数据用 QoS 2**
`mosquitto_pub -q 2 -t "billing/<device>" -m "<金额>"`
```bash
# 充值扣费严格一次不可重复
mosquitto_pub -q 2 -t "billing/user-001" -m "100"
```

---

## Broker 配置

**基本写法：限制最大 QoS**
`max_qos 1`
```bash
# 在配置文件中限制 broker 最大 QoS 为 1
max_qos 1
```

---

**基本写法：队列配置**
`max_queued_messages 1000`
```bash
# 离线消息队列最大长度
max_queued_messages 1000
```

---

**基本写法：消息过期清理**
`max_queued_messages 1000`
```bash
# 离线消息队列长度限制自动丢弃旧消息
max_queued_messages 1000
```
