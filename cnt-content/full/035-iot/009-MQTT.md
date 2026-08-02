---
order: 90
title: MQTT协议
module: 'iot'
category: 云与基础设施
difficulty: intermediate
description: MQTT协议详解：发布/订阅模型、QoS等级、保留消息、遗嘱消息与Broker选型。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'iot/007-SecurityAndPrivacy'
  - 'iot/008-PracticeProject'
  - 'iot/010-CoAP'
  - 'iot/011-ArduinoDevelopment'
prerequisites:
  - 'iot/001-OverviewArchitecture'
---

## 1. MQTT 概述

### 1.1 什么是 MQTT

MQTT（Message Queuing Telemetry Transport）是轻量级的发布/订阅消息协议，专为物联网场景设计。

### 1.2 核心特点

| 特点      | 描述            |
| --------- | --------------- |
| 轻量      | 最小报文 2 字节 |
| 发布/订阅 | 解耦通信双方    |
| 多种 QoS  | 灵活可靠性      |
| 持久会话  | 离线消息保留    |
| 安全      | TLS + 认证      |

### 1.3 架构

```
Publisher → Broker → Subscriber
  (设备)    (服务器)   (应用)
```

## 2. 发布/订阅模型

### 2.1 主题（Topic）

```
home/livingroom/temperature
home/+/temperature          # + 单层通配符
home/#                      # # 多层通配符
```

| 通配符 | 描述     | 示例                                     |
| ------ | -------- | ---------------------------------------- |
| `+`    | 单层匹配 | `sensor/+/temp` 匹配 `sensor/1/temp`     |
| `#`    | 多层匹配 | `sensor/#` 匹配 `sensor/1/temp/humidity` |

### 2.2 主题设计最佳实践

```
# 推荐格式
{version}/{domain}/{device_type}/{device_id}/{property}

# 示例
v1/factory/sensor/temp/device001/value
v1/smart-home/light/switch/livingroom/state
```

## 3. QoS 等级

| QoS | 描述     | 传输次数 | 适用场景              |
| --- | -------- | -------- | --------------------- |
| 0   | 最多一次 | 1 次     | 传感器数据（可丢失）  |
| 1   | 至少一次 | 2+ 次    | 控制命令（需确认）    |
| 2   | 恰好一次 | 4 次     | 支付/计费（不可重复） |

### 3.1 QoS 0 流程

```
Publisher → PUBLISH → Broker → PUBLISH → Subscriber
```

### 3.2 QoS 1 流程

```
Publisher → PUBLISH → Broker → PUBACK → Publisher
Broker → PUBLISH → Subscriber → PUBACK → Broker
```

### 3.3 QoS 2 流程

```
Publisher → PUBLISH → Broker → PUBREC → Publisher → PUBREL → Broker → PUBCOMP → Publisher
Broker → PUBLISH → Subscriber → PUBREC → Broker → PUBREL → Subscriber → PUBCOMP → Broker
```

## 4. 保留消息与遗嘱消息

### 4.1 保留消息（Retained Message）

Broker 保留最新一条消息，新订阅者立即收到。

```python
# 发布保留消息
client.publish("device/status", payload="online", retain=True)
```

### 4.2 遗嘱消息（LWT）

客户端异常断开时，Broker 自动发布遗嘱消息。

```python
client.will_set("device/status", payload="offline", qos=1, retain=True)
```

## 5. MQTT 5.0 新特性

| 特性          | 描述                |
| ------------- | ------------------- |
| 原因码        | 明确的连接/断开原因 |
| 用户属性      | 自定义键值对        |
| 共享订阅      | 负载均衡            |
| 主题别名      | 减少带宽            |
| 流控          | 限制消息速率        |
| 会话/消息过期 | 自动清理            |

## 6. Broker 选型

| Broker    | 特点         | 适用场景    |
| --------- | ------------ | ----------- |
| Mosquitto | 轻量开源     | 小规模/开发 |
| EMQX      | 高性能分布式 | 大规模生产  |
| HiveMQ    | 企业级       | 企业 IoT    |
| VerneMQ   | 分布式       | 高可用      |

### 6.1 EMQX 示例

```bash
# Docker 部署
docker run -d --name emqx \
  -p 1883:1883 \
  -p 8083:8083 \
  -p 8084:8084 \
  -p 8883:8883 \
  -p 18083:18083 \
  emqx/emqx:latest
```

## 7. 代码示例

### 7.1 Python (paho-mqtt)

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with code {rc}")
    client.subscribe("home/+/temperature")

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(client_id="sensor-app")
client.on_connect = on_connect
client.on_message = on_message
client.will_set("device/status", "offline", qos=1, retain=True)

client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()
```

### 7.2 ESP32 (Arduino)

```cpp
#include <WiFi.h>
#include <PubSubClient.h>

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  WiFi.begin("SSID", "password");
  client.setServer("broker.emqx.io", 1883);
}

void loop() {
  if (!client.connected()) {
    client.connect("esp32-client");
  }
  client.publish("home/temperature", String(readTemperature()).c_str());
  client.loop();
  delay(5000);
}
```
## 主题层级

**基本写法：单层主题**
`<名称>`
```bash
# 单层主题用于简单场景
home
```

---

**基本写法：多层级主题**
`<层级1>/<层级2>/<层级3>`
```bash
# 使用斜杠分隔多个层级
home/livingroom/temperature
```

---

**基本写法：以斜杠开头**
`/<层级>`
```bash
# 开头斜杠会创建一个空层级
/home/livingroom
```

---

**基本写法：以斜杠结尾**
`<层级>/`
```bash
# 结尾斜杠会创建一个空层级
home/livingroom/
```

---

## 主题设计规范

**基本写法：层级命名规范**
`<building>/<floor>/<room>/<sensor>/<metric>`
```bash
# 按物理位置组织主题
buildingA/floor1/room101/dht22/temperature
```

---

**基本写法：使用小写与短横线**
`<service>-<instance>/<action>`
```bash
# 主题命名避免空格与特殊字符
device-001/status/online
```

---

**基本写法：避免空层级**
`home//temperature`
```bash
# 不推荐使用空层级
home//temperature
```

---

## 单层通配符 +

**基本写法：单层匹配**
`<前缀>/+/<后缀>`
```bash
# 匹配 home 任意房间下的 temperature
home/+/temperature
```

---

**基本写法：仅匹配单层**
`<前缀>/+`
```bash
# 仅匹配 home 下一层不递归
home/+
```

---

**基本写法：组合单层通配符**
`<前缀>/+/sensor/<后缀>`
```bash
# 中间层任意但前后固定
building/+/sensor/temp
```

---

**基本写法：多位置使用 +**
`<前缀>/+/+/+`
```bash
# 多个单层通配符组合
home/+/+/+/
```

---

## 多层通配符 #

**基本写法：递归匹配所有子层**
`<前缀>/#`
```bash
# 订阅 home 下所有层级所有主题
home/#
```

---

**基本写法：根通配符**
`#`
```bash
# 订阅 broker 上所有消息慎用
#
```

---

**基本写法：通配符必须在末尾**
`<前缀>/#/<后缀>`
```bash
# 错误写法 # 必须是主题最后一个字符
home/#/temp
```

---

**基本写法：前缀加 #**
`home/livingroom/#`
```bash
# 订阅 livingroom 下所有子主题
home/livingroom/#
```

---

## 系统主题

**基本写法：Broker 系统主题**
`$SYS/<子系统>`
```bash
# 订阅 broker 内置系统信息
$SYS/broker/version
```

---

**基本写法：查看连接数**
`$SYS/broker/clients/connected`
```bash
# 订阅当前在线客户端数
$SYS/broker/clients/connected
```

---

**基本写法：查看 broker 负载**
`$SYS/broker/load/messages/+`
```bash
# 订阅消息发送速率所有统计周期
$SYS/broker/load/messages/+
```

---

**基本写法：查看运行时间**
`$SYS/broker/uptime`
```bash
# 订阅 broker 启动至今时长
$SYS/broker/uptime
```

---

## 主题最佳实践

**基本写法：状态主题**
`<device>/status/<attribute>`
```bash
# 设备状态上报主题
sensor-001/status/online
```

---

**基本写法：命令主题**
`<device>/cmd/<action>`
```bash
# 下行控制命令主题
light-001/cmd/toggle
```

---

**基本写法：事件主题**
`<device>/event/<type>`
```bash
# 设备事件通知主题
door-001/event/open
```

---

**基本写法：数据主题**
`<device>/data/<metric>`
```bash
# 周期性数据上报主题
meter-001/data/power
```

---

**基本写法：响应主题**
`<device>/resp/<requestId>`
```bash
# RPC 响应主题带请求 ID
device-001/resp/abc123
```

---

## 通配符订阅示例

**基本写法：监听所有传感器数据**
`+/data/#`
```bash
# 监听所有设备的 data 主题
+/data/#
```

---

**基本写法：监听特定房间所有设备**
`home/livingroom/#`
```bash
# 监听客厅所有设备消息
home/livingroom/#
```

---

**基本写法：监听所有设备上下线**
`+/status/online`
```bash
# 监听所有设备上线状态
+/status/online
```

---

**基本写法：监听所有告警事件**
`+/event/alert/#`
```bash
# 监听所有设备的告警事件
+/event/alert/#
```

---

## 共享订阅

**基本写法：MQTT 5 共享订阅**
`$share/<组名>/<主题>`
```bash
# 多个订阅者负载均衡消费
$share/workers/queue/tasks
```

---

**基本写法：共享订阅通配符**
`$share/<组名>/<前缀>/#`
```bash
# 共享订阅匹配多层级
$share/group1/sensors/#
```

## 延伸阅读
MQTT 与设备接入，见 035-iot 模块文档。
嵌入式 C 与硬件，见 025-c 模块。
时序数据与数据平台，见 052-big-data 模块。
