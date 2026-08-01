---
order: 210
title: 物联网 mosquitto_pub 发布命令
module: iot

category: '035-iot'
difficulty: beginner
description: 物联网 mosquitto_pub 发布命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 基本发布

**基本写法：发布单条消息**
`mosquitto_pub -h <主机> -t <主题> -m "<消息>"`
```bash
# 向本地 broker 发布消息
mosquitto_pub -h localhost -t "test/topic" -m "Hello, MQTT!"
```

---

**基本写法：指定端口**
`mosquitto_pub -h <主机> -p <端口> -t <主题> -m "<消息>"`
```bash
# 连接非默认端口 1884
mosquitto_pub -h localhost -p 1884 -t "test/topic" -m "Hi"
```

---

**基本写法：使用 URL 形式**
`mosquitto_pub -L mqtt://<主机>:<端口>/<主题> -m "<消息>"`
```bash
# 通过 URL 形式发布
mosquitto_pub -L mqtt://localhost:1883/test/topic -m "Hi"
```

---

## 消息内容来源

**基本写法：从命令行消息**
`mosquitto_pub -t <主题> -m "<消息>"`
```bash
# 直接在命令行指定消息内容
mosquitto_pub -t "home/temp" -m "23.5"
```

---

**基本写法：从文件读取**
`mosquitto_pub -t <主题> -f <文件路径>`
```bash
# 将文件内容作为消息发送
mosquitto_pub -t "data/log" -f ./payload.txt
```

---

**基本写法：从标准输入按行发送**
`mosquitto_pub -t <主题> -l`
```bash
# 逐行读取标准输入并分别发送
echo -e "line1\nline2" | mosquitto_pub -t "test/bulk" -l
```

---

**基本写法：从标准输入整体发送**
`mosquitto_pub -t <主题> -s`
```bash
# 将整个标准输入作为单条消息
echo '{"temp":23.5}' | mosquitto_pub -t "data/json" -s
```

---

**基本写法：发送空消息**
`mosquitto_pub -t <主题> -n`
```bash
# 发送空消息用于清除 retained
mosquitto_pub -t "home/temp" -n -r
```

---

## QoS 与保留

**基本写法：指定 QoS 级别**
`mosquitto_pub -t <主题> -m "<消息>" -q <0|1|2>`
```bash
# 以 QoS 1 至少一次方式发布
mosquitto_pub -h localhost -t "test/topic" -m "Reliable" -q 1
```

---

**基本写法：发布 retained 消息**
`mosquitto_pub -t <主题> -m "<消息>" -r`
```bash
# 发布保留消息新订阅者将立即收到
mosquitto_pub -h localhost -t "test/topic" -m "Persistent" -r
```

---

**基本写法：清除 retained 消息**
`mosquitto_pub -t <主题> -n -r`
```bash
# 发送空 retain 消息清除历史保留
mosquitto_pub -t "home/temp" -n -r
```

---

## 客户端身份

**基本写法：指定客户端 ID**
`mosquitto_pub -i <客户端ID> -t <主题> -m "<消息>"`
```bash
# 设置固定客户端 ID 便于追踪
mosquitto_pub -i "sensor-001" -t "sensor/data" -m "23.5"
```

---

**基本写法：指定客户端 ID 前缀**
`mosquitto_pub -I <前缀> -t <主题> -m "<消息>"`
```bash
# 使用前缀 broker 自动追加进程 ID
mosquitto_pub -I "pub-" -t "test/topic" -m "Hello"
```

---

**基本写法：设置心跳间隔**
`mosquitto_pub -k <秒> -t <主题> -m "<消息>"`
```bash
# 每 30 秒发送一次心跳
mosquitto_pub -k 30 -t "test/topic" -m "Hello"
```

---

## 认证

**基本写法：用户名密码认证**
`mosquitto_pub -h <主机> -u <用户名> -P <密码> -t <主题> -m "<消息>"`
```bash
# 通过用户名密码连接 broker
mosquitto_pub -h localhost -u iot-user -P mypass -t "test/topic" -m "Secret"
```

---

**基本写法：禁用 clean session**
`mosquitto_pub -c -i <客户端ID> -t <主题> -m "<消息>"`
```bash
# 保持会话状态需配合固定客户端 ID
mosquitto_pub -c -i "sensor-001" -t "test/topic" -m "Hello"
```

---

## 遗嘱消息

**基本写法：设置遗嘱主题与内容**
`mosquitto_pub --will-topic <主题> --will-payload "<消息>" -t <主题> -m "<消息>"`
```bash
# 客户端异常断开时 broker 自动发布遗嘱
mosquitto_pub --will-topic "status/sensor" --will-payload "offline" -t "data/sensor" -m "23.5"
```

---

**基本写法：遗嘱 QoS 与 retain**
`mosquitto_pub --will-topic <主题> --will-payload "<消息>" --will-qos <0|1|2> --will-retain -t <主题> -m "<消息>"`
```bash
# 设置 QoS 1 并保留的遗嘱消息
mosquitto_pub --will-topic "status/sensor" --will-payload "offline" --will-qos 1 --will-retain -t "data/sensor" -m "23.5"
```

---

## 调试输出

**基本写法：开启调试模式**
`mosquitto_pub -d -t <主题> -m "<消息>"`
```bash
# 打印连接与发送的详细调试信息
mosquitto_pub -d -h localhost -t "test/topic" -m "Debug"
```

---

**基本写法：静默模式**
`mosquitto_pub --quiet -t <主题> -m "<消息>"`
```bash
# 不输出任何错误信息
mosquitto_pub --quiet -t "test/topic" -m "Silent"
```

---

## 重复发送

**基本写法：重复发送多次**
`mosquitto_pub --repeat <次数> -t <主题> -m "<消息>"`
```bash
# 重复发送 5 次相同消息
mosquitto_pub --repeat 5 -t "test/topic" -m "Repeat"
```

---

**基本写法：重复间隔**
`mosquitto_pub --repeat <次数> --repeat-delay <秒> -t <主题> -m "<消息>"`
```bash
# 每秒发送一次共发送 10 次
mosquitto_pub --repeat 10 --repeat-delay 1 -t "test/topic" -m "Periodic"
```

---

## 协议版本

**基本写法：指定 MQTT 协议版本**
`mosquitto_pub -V <mqtt5|mqtt311|mqtt31> -t <主题> -m "<消息>"`
```bash
# 使用 MQTT 5.0 协议发布
mosquitto_pub -V mqtt5 -t "test/topic" -m "v5"
```

---

**基本写法：通过配置文件提供参数**
`mosquitto_pub -o <配置文件> -t <主题> -m "<消息>"`
```bash
# 从配置文件加载认证参数避免命令行暴露
mosquitto_pub -o ~/.config/mosquitto_pub -t "test/topic" -m "Hello"
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
| 物联网 mosquitto_pub 发布命令 | 021-MosquittoPub | 本文自身 |
| 物联网 mosquitto_sub 订阅命令 | 022-MosquittoSub | 本文的并列主题 |
| 物联网 ESP32 开发环境 | 023-ESP32Setup | 本文的前置基础 |
| 物联网 ESP32 GPIO 与引脚 | 024-ESP32GPIOPinout | 本文的并列主题 |
| 物联网 ESP32 I2C 通信 | 025-ESP32I2C | 本文的并列主题 |
| 物联网 ESP32 SPI 与 UART | 026-ESP32SPIUART | 本文的并列主题 |
| 物联网 ESP32 WiFi 配置 | 027-ESP32WiFiConfig | 本文的并列主题 |
| 物联网 ESP32 OTA 更新 | 028-ESP32OTA | 本文的并列主题 |
