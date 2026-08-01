---
order: 270
title: 物联网 ESP32 WiFi 配置
module: 035-iot
category: '035-iot'
difficulty: beginner
description: 物联网 ESP32 WiFi 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 物联网 ESP32 WiFi 配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## WiFi 库引入

**基本写法：包含 WiFi 库**
`#include <WiFi.h>`
```cpp
// 引入 ESP32 WiFi 标准库
#include <WiFi.h>
```

---

## STA 模式连接

**基本写法：启动连接**
`WiFi.begin(<SSID>, <密码>);`
```cpp
// 连接到指定 SSID
WiFi.begin("MyWiFi", "mypassword");
```

---

**基本写法：等待连接成功**
`WiFi.waitForConnectResult()`
```cpp
// 阻塞等待连接返回状态码
if (WiFi.waitForConnectResult() != WL_CONNECTED) {
  Serial.println("Connection Failed");
}
```

---

**基本写法：循环等待连接**
```cpp
// 非阻塞循环检查连接状态
while (WiFi.status() != WL_CONNECTED) {
  delay(500);
  Serial.print(".");
}
```

---

**基本写法：检查连接状态**
`WiFi.status()`
```cpp
// 返回当前连接状态
wl_status_t status = WiFi.status();
```

---

**基本写法：获取本机 IP**
`WiFi.localIP()`
```cpp
// 获取分配到的 IP 地址
IPAddress ip = WiFi.localIP();
```

---

**基本写法：获取 MAC 地址**
`WiFi.macAddress()`
```cpp
// 返回 MAC 地址字节数组
byte mac[6];
WiFi.macAddress(mac);
```

---

**基本写法：获取信号强度**
`WiFi.RSSI()`
```cpp
// 获取当前信号强度 dBm
int rssi = WiFi.RSSI();
```

---

**基本写法：断开连接**
`WiFi.disconnect([<wifioff>]);`
```cpp
// 断开当前 WiFi
WiFi.disconnect();
```

---

## AP 模式

**基本写法：启动 AP 模式**
`WiFi.softAP(<SSID>, <密码>);`
```cpp
// 创建开放热点 MyAP
WiFi.softAP("MyAP");
```

---

**基本写法：加密 AP**
`WiFi.softAP(<SSID>, <密码>, <通道>, <隐藏>, <最大连接>);`
```cpp
// 创建 WPA2 加密热点
WiFi.softAP("MyAP", "password123", 1, false, 4);
```

---

**基本写法：获取 AP IP**
`WiFi.softAPIP()`
```cpp
// 获取 AP 模式下的 IP 通常 192.168.4.1
IPAddress ip = WiFi.softAPIP();
```

---

**基本写法：获取已连接客户端数**
`WiFi.softAPgetStationNum()`
```cpp
// 返回当前连接到 AP 的客户端数
int n = WiFi.softAPgetStationNum();
```

---

**基本写法：关闭 AP**
`WiFi.softAPdisconnect();`
```cpp
// 关闭热点模式
WiFi.softAPdisconnect();
```

---

## STA+AP 混合模式

**基本写法：同时启用 STA 与 AP**
```cpp
// STA 连接路由器同时开启 AP
WiFi.mode(WIFI_AP_STA);
WiFi.begin("MyWiFi", "password");
WiFi.softAP("MyAP", "appassword");
```

---

**基本写法：设置模式**
`WiFi.mode(<模式>);`
```cpp
// 仅 STA 模式
WiFi.mode(WIFI_STA);
```

---

**基本写法：仅 AP 模式**
`WiFi.mode(WIFI_AP);`
```cpp
// 仅热点模式
WiFi.mode(WIFI_AP);
```

---

**基本写法：关闭 WiFi**
`WiFi.mode(WIFI_OFF);`
```cpp
// 完全关闭 WiFi 节省功耗
WiFi.mode(WIFI_OFF);
```

---

## 扫描网络

**基本写法：扫描周边网络**
`WiFi.scanNetworks()`
```cpp
// 返回发现的网络数量
int n = WiFi.scanNetworks();
```

---

**基本写法：获取 SSID**
`WiFi.SSID(<索引>)`
```cpp
// 获取指定索引的 SSID
String ssid = WiFi.SSID(0);
```

---

**基本写法：获取 RSSI**
`WiFi.RSSI(<索引>)`
```cpp
// 获取指定索引的信号强度
int rssi = WiFi.RSSI(0);
```

---

**基本写法：获取加密类型**
`WiFi.encryptionType(<索引>)`
```cpp
// 获取加密类型 7 为 WPA2
int enc = WiFi.encryptionType(0);
```

---

**基本写法：遍历扫描结果**
```cpp
// 打印所有发现的 WiFi 信息
int n = WiFi.scanNetworks();
for (int i = 0; i < n; i++) {
  Serial.printf("%s (%d) %d\n", WiFi.SSID(i).c_str(), WiFi.RSSI(i), WiFi.encryptionType(i));
}
```

---

**基本写法：清除扫描结果**
`WiFi.scanDelete();`
```cpp
// 释放扫描结果内存
WiFi.scanDelete();
```

---

## 静态 IP 配置

**基本写法：配置静态 IP**
`WiFi.config(<IP>, <网关>, <子网> [, <DNS>]);`
```cpp
// 设置静态 IP 配置
IPAddress ip(192, 168, 1, 100);
IPAddress gw(192, 168, 1, 1);
IPAddress sn(255, 255, 255, 0);
WiFi.config(ip, gw, sn);
```

---

**基本写法：指定 DNS**
`WiFi.config(<IP>, <网关>, <子网>, <DNS1>, <DNS2>);`
```cpp
// 同时指定主备 DNS
IPAddress dns1(8, 8, 8, 8);
IPAddress dns2(8, 8, 4, 4);
WiFi.config(ip, gw, sn, dns1, dns2);
```

---

**基本写法：设置主机名**
`WiFi.setHostname(<名称>);`
```cpp
// 设置 mDNS 主机名
WiFi.setHostname("esp32-sensor");
```

---

## 事件回调

**基本写法：注册事件回调**
`WiFi.onEvent(<回调> [, <事件>]);`
```cpp
// 注册 WiFi 事件回调
WiFi.onEvent(WiFiEvent);
```

---

**基本写法：事件回调实现**
```cpp
// 处理各类 WiFi 事件
void WiFiEvent(WiFiEvent_t event) {
  switch (event) {
    case SYSTEM_EVENT_STA_CONNECTED:
      Serial.println("Connected to AP");
      break;
    case SYSTEM_EVENT_STA_GOT_IP:
      Serial.println("Got IP");
      break;
    case SYSTEM_EVENT_STA_DISCONNECTED:
      Serial.println("Disconnected");
      break;
  }
}
```

---

**基本写法：注册特定事件**
`WiFi.onEvent(<回调>, <事件类型>);`
```cpp
// 仅监听获取 IP 事件
WiFi.onEvent(onGotIP, SYSTEM_EVENT_STA_GOT_IP);
```

---

## 自动重连

**基本写法：启用自动重连**
`WiFi.setAutoReconnect(true);`
```cpp
// 断线后自动尝试重连
WiFi.setAutoReconnect(true);
```

---

**基本写法：设置持久化**
`WiFi.persistent(true);`
```cpp
// 将 WiFi 配置保存到 NVS
WiFi.persistent(true);
```

---

## 低功耗

**基本写法：设置睡眠模式**
`WiFi.setSleep(<模式>);`
```cpp
// 启用最小功耗睡眠模式
WiFi.setSleep(WIFI_PS_MIN_MODEM);
```

---

**基本写法：设置发射功率**
`WiFi.setTxPower(<功率>);`
```cpp
// 设置发射功率为 8dBm 降低功耗
WiFi.setTxPower(WIFI_POWER_8dBm);
```

---

## WebServer 配置

**基本写法：创建配置门户**
```cpp
// 通过 AP 模式提供 WiFi 配置页面
#include <WebServer.h>
WebServer server(80);
server.on("/", handleRoot);
server.begin();
```

---

**基本写法：使用 WiFiManager 自动配置**
```cpp
// 使用 WiFiManager 库简化配网流程
#include <WiFiManager.h>
WiFiManager wm;
wm.autoConnect("ESP32-Setup");
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
| 物联网 mosquitto_sub 订阅命令 | 022-MosquittoSub | 本文的并列主题 |
| 物联网 ESP32 开发环境 | 023-ESP32Setup | 本文的前置基础 |
| 物联网 ESP32 GPIO 与引脚 | 024-ESP32GPIOPinout | 本文的并列主题 |
| 物联网 ESP32 I2C 通信 | 025-ESP32I2C | 本文的并列主题 |
| 物联网 ESP32 SPI 与 UART | 026-ESP32SPIUART | 本文的并列主题 |
| 物联网 ESP32 WiFi 配置 | 027-ESP32WiFiConfig | 本文自身 |
| 物联网 ESP32 OTA 更新 | 028-ESP32OTA | 本文的并列主题 |
