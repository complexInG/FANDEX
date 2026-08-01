---
order: 260
title: 物联网 ESP32 SPI 与 UART
module: iot

category: '035-iot'
difficulty: beginner
description: 物联网 ESP32 SPI 与 UART 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## SPI 库引入

**基本写法：包含 SPI 库**
`#include <SPI.h>`
```cpp
// 引入 ESP32 SPI 标准库
#include <SPI.h>
```

---

## SPI 初始化

**基本写法：默认引脚初始化**
`SPI.begin();`
```cpp
// 使用 VSPI 默认引脚 SCK=18 MISO=19 MOSI=23 SS=5
SPI.begin();
```

---

**基本写法：自定义引脚初始化**
`SPI.begin(<SCK>, <MISO>, <MOSI>, <SS>);`
```cpp
// 自定义 HSPI 引脚 SCK=14 MISO=12 MOSI=13 SS=15
SPI.begin(14, 12, 13, 15);
```

---

**基本写法：设置时钟分频**
`SPI.setFrequency(<频率>);`
```cpp
// 设置 SPI 时钟 1MHz
SPI.setFrequency(1000000);
```

---

**基本写法：设置数据模式**
`SPI.setDataMode(<模式>);`
```cpp
// 设置 SPI 模式 0 CPOL=0 CPHA=0
SPI.setDataMode(SPI_MODE0);
```

---

**基本写法：设置位序**
`SPI.setBitOrder(<顺序>);`
```cpp
// 高位在前
SPI.setBitOrder(MSBFIRST);
```

---

## SPI 数据传输

**基本写法：传输单字节**
`SPI.transfer(<字节>)`
```cpp
// 发送并接收一个字节
uint8_t rx = SPI.transfer(0xFF);
```

---

**基本写法：传输多字节**
`SPI.transfer(<缓冲区>, <长度>)`
```cpp
// 收发缓冲区数据
SPI.transfer(buffer, length);
```

---

**基本写法：仅发送不接收**
`SPI.write(<字节>);`
```cpp
// 仅写不读提高效率
SPI.write(0xAA);
```

---

**基本写法：连续发送字节**
`SPI.writeBytes(<缓冲区>, <长度>);`
```cpp
// 高效发送字节数组
SPI.writeBytes(tx_buf, 16);
```

---

**基本写法：连续传输缓冲区**
`SPI.transferBytes(<发送>, <接收>, <长度>);`
```cpp
// 同时发送并接收字节数组
SPI.transferBytes(tx_buf, rx_buf, 16);
```

---

## SPI 片选控制

**基本写法：手动控制片选**
```cpp
// 主模式手动拉低 SS 启用从设备
digitalWrite(SS, LOW);
SPI.transfer(0x9F);
digitalWrite(SS, HIGH);
```

---

**基本写法：使用 SPI 类自带 SS**
`SPI.begin(<SCK>, <MISO>, <MOSI>, <SS>);`
```cpp
// 让 SPI 库管理 SS 引脚
SPI.begin(18, 19, 23, 5);
```

---

**基本写法：beginTransaction 与 endTransaction**
```cpp
// 使用事务确保配置一致
SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
digitalWrite(SS, LOW);
SPI.transfer(0x9F);
digitalWrite(SS, HIGH);
SPI.endTransaction();
```

---

## 多从设备 SPI

**基本写法：定义多个片选**
```cpp
// 为不同从设备定义独立 SS
#define SS_FLASH 5
#define SD_CS    15
```

---

**基本写法：访问指定从设备**
```cpp
// 选中 SD 卡进行通信
digitalWrite(SD_CS, LOW);
SPI.transfer(0xFF);
digitalWrite(SD_CS, HIGH);
```

---

## UART 串口

**基本写法：使用默认 HardwareSerial**
`Serial.begin(<波特率>);`
```cpp
// 使用 UART0 默认引脚 TX=1 RX=3
Serial.begin(115200);
```

---

**基本写法：自定义引脚串口**
`Serial.begin(<波特率>, SERIAL_8N1, <RX>, <TX>);`
```cpp
// 使用 GPIO16 RX GPIO17 TX
Serial.begin(115200, SERIAL_8N1, 16, 17);
```

---

**基本写法：创建第二串口**
`HardwareSerial <名称>(<UART 编号>);`
```cpp
// 使用 UART1 创建 mySerial
HardwareSerial mySerial(1);
```

---

**基本写法：初始化第二串口**
`<名称>.begin(<波特率>, <配置>, <RX>, <TX>);`
```cpp
// UART1 RX=GPIO26 TX=GPIO27
mySerial.begin(9600, SERIAL_8N1, 26, 27);
```

---

**基本写法：创建第三串口**
```cpp
// 使用 UART2 RX=GPIO16 TX=GPIO17
HardwareSerial Serial2(2);
Serial2.begin(115200);
```

---

## UART 数据读写

**基本写法：检查可读字节**
`<串口>.available()`
```cpp
// 返回接收缓冲区字节数
int n = mySerial.available();
```

---

**基本写法：读取单字节**
`<串口>.read()`
```cpp
// 读取一个字节
int c = mySerial.read();
```

---

**基本写法：写入字节**
`<串口>.write(<字节>);`
```cpp
// 发送一个字节
mySerial.write(0xAA);
```

---

**基本写法：写入字符串**
`<串口>.print("<字符串>");`
```cpp
// 发送字符串
mySerial.print("AT+RST\r\n");
```

---

**基本写法：读取一行**
`<串口>.readStringUntil('<终止符>')`
```cpp
// 读取到换行符
String line = mySerial.readStringUntil('\n');
```

---

## 串口配置

**基本写法：设置串口配置**
`Serial.begin(<波特率>, <配置>);`
```cpp
// 8 数据位 无校验 1 停止位
Serial.begin(115200, SERIAL_8N1);
```

---

**基本写法：设置 8E1 配置**
`Serial.begin(<波特率>, SERIAL_8E1);`
```cpp
// 8 数据位 偶校验 1 停止位
Serial.begin(9600, SERIAL_8E1);
```

---

**基本写法：设置接收缓冲区**
`<串口>.setRxBufferSize(<字节>);`
```cpp
// 扩大接收缓冲区到 1024 字节
mySerial.setRxBufferSize(1024);
```

---

## UART 模块通信

**基本写法：发送 AT 命令**
```cpp
// 向 ESP8266 等模块发送 AT 指令
mySerial.print("AT+CWMODE=1\r\n");
delay(1000);
String resp = mySerial.readString();
```

---

**基本写法：等待指定响应**
```cpp
// 阻塞等待响应包含 OK
unsigned long start = millis();
while (millis() - start < 5000) {
  if (mySerial.available()) {
    String resp = mySerial.readStringUntil('\n');
    if (resp.indexOf("OK") >= 0) return true;
  }
}
```

---

**基本写法：Modbus RTU 帧**
```cpp
// 发送 Modbus RTU 命令帧
uint8_t frame[] = {0x01, 0x03, 0x00, 0x00, 0x00, 0x0A, 0xC5, 0xCD};
mySerial.write(frame, sizeof(frame));
```

---

## SPI 常见外设

**基本写法：读取 SD 卡**
```cpp
// 使用 SD 库初始化 SD 卡
#include <SD.h>
SD.begin(SD_CS);
File f = SD.open("/data.txt", FILE_READ);
```

---

**基本写法：读取 Flash W25Q128**
```cpp
// 读取 SPI Flash JEDEC ID
digitalWrite(SS_FLASH, LOW);
SPI.transfer(0x9F);
uint8_t m = SPI.transfer(0);
uint8_t t = SPI.transfer(0);
uint8_t c = SPI.transfer(0);
digitalWrite(SS_FLASH, HIGH);
```

---

**基本写法：MFRC522 RFID**
```cpp
// 初始化 MFRC522 读卡器
#include <MFRC522.h>
MFRC522 rfid(SS, 32);
SPI.begin();
rfid.PCD_Init();
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
