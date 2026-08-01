---
order: 200
title: 物联网 Mosquitto Broker 管理
module: iot

category: '035-iot'
difficulty: beginner
description: 物联网 Mosquitto Broker 管理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 服务安装

**基本写法：安装 Mosquitto**
`sudo apt-get install -y mosquitto mosquitto-clients`
```bash
# 在 Debian/Ubuntu 上安装 broker 与客户端工具
sudo apt-get install -y mosquitto mosquitto-clients
```

---

**基本写法：查看版本**
`mosquitto -h`
```bash
# 查看 Mosquitto broker 版本信息
mosquitto -h
```

---

**基本写法：前台启动 Broker**
`mosquitto -v`
```bash
# 以详细日志模式前台运行
mosquitto -v
```

---

**基本写法：指定端口启动**
`mosquitto -v -p <端口>`
```bash
# 在 1884 端口启动 broker
mosquitto -v -p 1884
```

---

**基本写法：指定配置文件启动**
`mosquitto -c <配置文件> -v`
```bash
# 使用自定义配置启动
mosquitto -c /etc/mosquitto/mosquitto.conf -v
```

---

## 服务控制

**基本写法：启动服务**
`sudo systemctl start mosquitto`
```bash
# 启动 Mosquitto 系统服务
sudo systemctl start mosquitto
```

---

**基本写法：停止服务**
`sudo systemctl stop mosquitto`
```bash
# 停止 Mosquitto 服务
sudo systemctl stop mosquitto
```

---

**基本写法：重启服务**
`sudo systemctl restart mosquitto`
```bash
# 修改配置后重启服务
sudo systemctl restart mosquitto
```

---

**基本写法：查看服务状态**
`sudo systemctl status mosquitto`
```bash
# 查看 broker 运行状态
sudo systemctl status mosquitto
```

---

**基本写法：开机自启**
`sudo systemctl enable mosquitto`
```bash
# 设置开机自动启动
sudo systemctl enable mosquitto
```

---

**基本写法：禁止开机自启**
`sudo systemctl disable mosquitto`
```bash
# 取消开机自启
sudo systemctl disable mosquitto
```

---

## 配置文件

**基本写法：监听端口配置**
```
listener 1883
```
```bash
# 在配置文件中指定监听端口
listener 1883
```

---

**基本写法：允许匿名访问**
```
allow_anonymous true
```
```bash
# 允许无认证连接（仅测试用）
allow_anonymous true
```

---

**基本写法：禁用匿名访问**
```
allow_anonymous false
```
```bash
# 强制要求认证
allow_anonymous false
```

---

**基本写法：配置密码文件**
```
password_file /etc/mosquitto/passwd
```
```bash
# 指定用户密码文件路径
password_file /etc/mosquitto/passwd
```

---

**基本写法：配置 TLS 证书**
```
listener 8883
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
cafile /etc/mosquitto/certs/ca.crt
```
```bash
# 配置 8883 端口 TLS 加密通信
listener 8883
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
cafile /etc/mosquitto/certs/ca.crt
```

---

**基本写法：配置持久化**
```
persistence true
persistence_location /var/lib/mosquitto/
```
```bash
# 开启消息持久化存储
persistence true
persistence_location /var/lib/mosquitto/
```

---

## 日志查看

**基本写法：实时查看日志**
`tail -f /var/log/mosquitto/mosquitto.log`
```bash
# 实时跟踪 broker 日志输出
tail -f /var/log/mosquitto/mosquitto.log
```

---

**基本写法：查看最近 N 行日志**
`tail -n <行数> /var/log/mosquitto/mosquitto.log`
```bash
# 查看最近 100 行日志
tail -n 100 /var/log/mosquitto/mosquitto.log
```

---

## 用户管理

**基本写法：创建用户并设置密码**
`sudo mosquitto_passwd -c /etc/mosquitto/passwd <用户名>`
```bash
# 首次创建密码文件并添加用户
sudo mosquitto_passwd -c /etc/mosquitto/passwd iot-user
```

---

**基本写法：追加用户**
`sudo mosquitto_passwd /etc/mosquitto/passwd <用户名>`
```bash
# 向已有密码文件追加用户
sudo mosquitto_passwd /etc/mosquitto/passwd second-user
```

---

**基本写法：删除用户**
`sudo mosquitto_passwd -D /etc/mosquitto/passwd <用户名>`
```bash
# 从密码文件中删除指定用户
sudo mosquitto_passwd -D /etc/mosquitto/passwd iot-user
```

---

## 端口防火墙

**基本写法：放行 MQTT 端口**
`sudo ufw allow 1883/tcp`
```bash
# 开放默认 MQTT 端口
sudo ufw allow 1883/tcp
```

---

**基本写法：放行 MQTT over TLS**
`sudo ufw allow 8883/tcp`
```bash
# 开放加密 MQTT 端口
sudo ufw allow 8883/tcp
```

---

**基本写法：放行 WebSocket**
`sudo ufw allow 9001/tcp`
```bash
# 开放 MQTT WebSocket 端口
sudo ufw allow 9001/tcp
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
| 物联网 Mosquitto Broker 管理 | 020-MosquittoBrokerManage | 本文自身 |
| 物联网 mosquitto_pub 发布命令 | 021-MosquittoPub | 本文的并列主题 |
| 物联网 mosquitto_sub 订阅命令 | 022-MosquittoSub | 本文的并列主题 |
| 物联网 ESP32 开发环境 | 023-ESP32Setup | 本文的前置基础 |
| 物联网 ESP32 GPIO 与引脚 | 024-ESP32GPIOPinout | 本文的并列主题 |
| 物联网 ESP32 I2C 通信 | 025-ESP32I2C | 本文的并列主题 |
| 物联网 ESP32 SPI 与 UART | 026-ESP32SPIUART | 本文的并列主题 |
| 物联网 ESP32 WiFi 配置 | 027-ESP32WiFiConfig | 本文的并列主题 |
| 物联网 ESP32 OTA 更新 | 028-ESP32OTA | 本文的并列主题 |
