---
order: 280
title: 物联网 ESP32 OTA 更新
module: 035-iot
category: '035-iot'
difficulty: beginner
description: 物联网 ESP32 OTA 更新 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## OTA 库引入

**基本写法：包含 OTA 库**
```cpp
// 引入 ArduinoOTA 所需头文件
#include <WiFi.h>
#include <ESPmDNS.h>
#include <NetworkUdp.h>
#include <ArduinoOTA.h>
```

---

## 基础 OTA 配置

**基本写法：设置端口与主机名**
`ArduinoOTA.setPort(<端口>);`
```cpp
// 默认端口 3232
ArduinoOTA.setPort(3232);
```

---

**基本写法：设置主机名**
`ArduinoOTA.setHostname(<名称>);`
```cpp
// 设置 IDE 端口列表显示的主机名
ArduinoOTA.setHostname("esp32-device");
```

---

**基本写法：设置密码**
`ArduinoOTA.setPassword(<密码>);`
```cpp
// 要求上传时输入密码
ArduinoOTA.setPassword("admin123");
```

---

**基本写法：设置密码哈希**
`ArduinoOTA.setPasswordHash(<MD5>);`
```cpp
// 使用 MD5 哈希避免明文密码
ArduinoOTA.setPasswordHash("0192023a7bbd73250516f069df18b500");
```

---

## OTA 回调

**基本写法：开始回调**
`ArduinoOTA.onStart(<回调>);`
```cpp
// 升级开始时触发
ArduinoOTA.onStart([]() {
  String type = (ArduinoOTA.getCommand() == U_FLASH) ? "sketch" : "filesystem";
  Serial.println("Start updating " + type);
});
```

---

**基本写法：结束回调**
`ArduinoOTA.onEnd(<回调>);`
```cpp
// 升级结束时触发
ArduinoOTA.onEnd([]() {
  Serial.println("\nUpdate Finished");
});
```

---

**基本写法：进度回调**
`ArduinoOTA.onProgress(<回调>);`
```cpp
// 实时输出升级进度百分比
ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
  Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
});
```

---

**基本写法：错误回调**
`ArduinoOTA.onError(<回调>);`
```cpp
// 升级失败时触发
ArduinoOTA.onError([](ota_error_t error) {
  Serial.printf("Error[%u]: ", error);
  if (error == OTA_AUTH_ERROR) Serial.println("Auth Failed");
  else if (error == OTA_CONNECT_ERROR) Serial.println("Connect Failed");
  else if (error == OTA_RECEIVE_ERROR) Serial.println("Receive Failed");
  else if (error == OTA_END_ERROR) Serial.println("End Failed");
});
```

---

## 启动与处理

**基本写法：启动 OTA**
`ArduinoOTA.begin();`
```cpp
// 初始化 OTA 服务
ArduinoOTA.begin();
```

---

**基本写法：循环处理**
`ArduinoOTA.handle();`
```cpp
// 在 loop 中调用处理上传请求
void loop() {
  ArduinoOTA.handle();
}
```

---

## 完整 ArduinoOTA 示例

**基本写法：完整 OTA Sketch**
```cpp
// 完整可用的 OTA 升级 sketch
void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin("your_ssid", "your_password");
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.setHostname("esp32-ota");
  ArduinoOTA.setPassword("changeMe");
  ArduinoOTA.begin();
}
void loop() {
  ArduinoOTA.handle();
}
```

---

## 分区表配置

**基本写法：选择 OTA 分区方案**
`Tools -> Partition Scheme -> Default 4MB with spiffs`
```bash
# 选择支持双 OTA 分区的方案
Default 4MB with spiffs (1.9MB APP with OTA)
```

---

**基本写法：自定义分区表**
```
# OTA 分区表 csv 示例
nvs,data,nvs,0x9000,0x5000
otadata,data,ota,0xe000,0x2000
app0,app,ota_0,0x10000,0x140000
app1,app,ota_1,0x150000,0x140000
spiffs,data,spiffs,0x290000,0x160000
```

---

## HTTP OTA 更新

**基本写法：包含 HTTPUpdate 库**
```cpp
// 引入 HTTP 远程更新库
#include <HTTPClient.h>
#include <HTTPUpdate.h>
```

---

**基本写法：从 URL 更新**
`httpUpdate.update(<客户端>, <URL>);`
```cpp
// 从 HTTP 服务器下载固件并更新
WiFiClient client;
t_httpUpdate_return ret = httpUpdate.update(client, "http://server.com/firmware.bin");
```

---

**基本写法：处理更新结果**
```cpp
// 根据返回值处理更新结果
switch (ret) {
  case HTTP_UPDATE_OK:
    Serial.println("Update successful");
    break;
  case HTTP_UPDATE_FAILED:
    Serial.println("Update failed");
    break;
  case HTTP_UPDATE_NO_UPDATES:
    Serial.println("No updates available");
    break;
}
```

---

**基本写法：带版本检查的更新**
```cpp
// 先获取服务器版本号再决定是否更新
HTTPClient http;
http.begin("http://server.com/version.txt");
if (http.GET() == HTTP_CODE_OK) {
  String latest = http.getString();
  if (latest != currentVersion) {
    performUpdate();
  }
}
http.end();
```

---

## Update 库底层操作

**基本写法：包含 Update 库**
`#include <Update.h>`
```cpp
// 引入底层 Update 接口
#include <Update.h>
```

---

**基本写法：开始更新**
`Update.begin(<大小>);`
```cpp
// 开始更新指定大小的固件
if (!Update.begin(UPDATE_SIZE_UNKNOWN)) {
  Serial.println("Begin failed");
}
```

---

**基本写法：写入数据**
`Update.write(<数据>, <长度>);`
```cpp
// 写入固件数据块
size_t written = Update.write(buffer, len);
```

---

**基本写法：完成更新**
`Update.end();`
```cpp
// 结束更新并校验
if (Update.end()) {
  Serial.println("Update complete");
}
```

---

**基本写法：重启设备**
`ESP.restart();`
```cpp
// 更新完成后重启运行新固件
ESP.restart();
```

---

**基本写法：设置 MD5 校验**
`Update.setMD5(<MD5 字符串>);`
```cpp
// 设置预期 MD5 用于完整性校验
Update.setMD5("d41d8cd98f00b204e9800998ecf8427e");
```

---

**基本写法：检查完成状态**
`Update.isFinished()`
```cpp
// 检查更新是否完成
if (Update.isFinished()) {
  Serial.println("Finished successfully");
}
```

---

## ElegantOTA Web 更新

**基本写法：包含 ElegantOTA**
`#include <ElegantOTA.h>`
```cpp
// 引入 ElegantOTA 库
#include <ElegantOTA.h>
```

---

**基本写法：初始化 ElegantOTA**
`ElegantOTA.begin(&<server>);`
```cpp
// 在 setup 中绑定到 WebServer
ElegantOTA.begin(&server);
```

---

**基本写法：循环处理**
`ElegantOTA.loop();`
```cpp
// 在 loop 中调用
void loop() {
  server.handleClient();
  ElegantOTA.loop();
}
```

---

**基本写法：访问更新页面**
`http://<ESP32 IP>/update`
```bash
# 浏览器访问 OTA 上传页面
http://192.168.1.87/update
```

---

## 固件加密

**基本写法：AES 解密更新**
```cpp
// 使用 Update 库配合解密回调
const uint8_t aesKey[32] = { /* 32 字节密钥 */ };
Update.onError([](ota_error_t e) { /* 处理错误 */ });
// 自定义解密逻辑需配合 secure update 流程
```

---

**基本写法：HTTPS 固件下载**
`httpUpdate.update(<客户端>, <URL>, <指纹>);`
```cpp
// 通过 HTTPS 验证服务器证书指纹
WiFiClientSecure client;
client.setFingerprint("AA BB CC DD ...");
httpUpdate.update(client, "https://server.com/firmware.bin");
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
| 物联网 ESP32 WiFi 配置 | 027-ESP32WiFiConfig | 本文的并列主题 |
| 物联网 ESP32 OTA 更新 | 028-ESP32OTA | 本文自身 |
