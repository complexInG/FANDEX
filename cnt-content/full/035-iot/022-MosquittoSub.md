---
order: 220
title: 物联网 mosquitto_sub 订阅命令
module: 035-iot
category: '035-iot'
difficulty: beginner
description: 物联网 mosquitto_sub 订阅命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

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

## 参考文献



MQTT 规范：https://mqtt.org/
CoAP（RFC 7252）：https://www.rfc-editor.org/rfc/rfc7252
EMQX 文档：https://www.emqx.io/docs/zh/latest/
AWS IoT Core：https://aws.amazon.com/iot-core/
InfluxDB 文档：https://docs.influxdata.com/

## 延伸阅读



MQTT 与设备接入，见 035-iot 模块文档。
嵌入式 C 与硬件，见 025-c 模块。
时序数据与数据平台，见 052-big-data 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供物联网课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 MQTT 协议深入

报文类型：CONNECT/CONNACK/PUBLISH/PUBACK/SUBSCRIBE/SUBACK/PINGREQ/DISCONNECT。
会话状态：clean session、持久会话、消息保留（retain）与遗嘱（LWT）。
QoS 语义：0 至多一次，1 至少一次，2 恰好一次；QoS2 四步握手。
共享订阅（shared subscription）实现负载均衡；主题层级与通配符（+/#）。

### 13.2 边缘计算架构

边缘节点形态：网关、边缘服务器、设备端推理；部署容器或原生应用。
断网续传：本地消息队列 + 持久化 + 重连补传。
云端协同：模型下发（边缘推理）、规则下沉、影子同步。
KubeEdge/OpenYurt 把 K8s 延伸到边缘。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与架构 | 001-OverviewArchitecture | 本文的前置基础 |
| 传感器与嵌入式 | 002-SensorEmbedded | 本文的并列主题 |
| 通信协议 | 003-CommunicationProtocol | 本文的并列主题 |
| 边缘计算 | 004-EdgeComputing | 本文的并列主题 |
| IoT 平台 | 005-IoT | 本文的并列主题 |
| 数据处理与分析 | 006-DataProcessingAnalysis | 本文的并列主题 |
| 安全与隐私 | 007-SecurityAndPrivacy | 本文的安全延伸 |
| 实战项目 | 008-PracticeProject | 本文的综合应用 |
| MQTT协议 | 009-MQTT | 本文的并列主题 |
| CoAP协议 | 010-CoAP | 本文的并列主题 |
| Arduino开发 | 011-ArduinoDevelopment | 本文的并列主题 |
| ESP32开发 | 012-ESP32Development | 本文的并列主题 |
| RT-Thread实时系统 | 013-RTThread | 本文的并列主题 |
| 边缘AI | 014-AI | 本文的并列主题 |
| LwM2M设备管理 | 015-LwM2MManagement | 本文的并列主题 |
| 时序数据库 | 016-TimeSeriesDatabase | 本文的并列主题 |
| 物联网安全 | 017-IoTSecurity | 本文的安全延伸 |
| 主流IoT平台 | 018-IoT | 本文的并列主题 |
| 数字孪生 | 019-DigitalTwin | 本文的并列主题 |
| 物联网 Mosquitto Broker 管理 | 020-MosquittoBrokerManage | 本文的并列主题 |
| 物联网 mosquitto_pub 发布命令 | 021-MosquittoPub | 本文的并列主题 |
| 物联网 mosquitto_sub 订阅命令 | 022-MosquittoSub | 本文自身 |
| 物联网 ESP32 开发环境 | 023-ESP32Setup | 本文的前置基础 |
| 物联网 ESP32 GPIO 与引脚 | 024-ESP32GPIOPinout | 本文的并列主题 |
| 物联网 ESP32 I2C 通信 | 025-ESP32I2C | 本文的并列主题 |
| 物联网 ESP32 SPI 与 UART | 026-ESP32SPIUART | 本文的并列主题 |
| 物联网 ESP32 WiFi 配置 | 027-ESP32WiFiConfig | 本文的并列主题 |
| 物联网 ESP32 OTA 更新 | 028-ESP32OTA | 本文的并列主题 |
